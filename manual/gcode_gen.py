"""G-code for the SX2.3 power drawbar parts, Centroid Acorn (CNC12), metric.

Conventions (agreed 14 Nov 2026): G54, mm, X/Y zero at the lower-left corner of the view named in
the build manual, Z zero on the top face of the part as clamped. Max spindle 5,000 rpm (confirmed 14 Nov 2026), mist/flood (M8).
Tools: T1 spot drill 90 deg; T2 6 mm carbide end mill; T3 10 mm carbide end mill; drills T10+ by size.
Feeds and speeds are conservative starting values for a light bench mill (my judgement, not sourced):
check them on scrap first. Every program is unproven until single-blocked on air above the part.
"""
import math, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else 'gcode'
os.makedirs(OUT, exist_ok=True)

DRILLS = {2.5: 10, 3.4: 11, 4.2: 12, 5.0: 13, 5.1: 14, 5.5: 15, 5.8: 16, 6.6: 17, 6.8: 18, 7.0: 19, 8.5: 20, 12.5: 21, 4.8: 22}
TOOLS = {1: 'Spot drill 90 deg (6 mm or larger)', 2: '6 mm carbide end mill, 2 or 3 flute', 3: '10 mm carbide end mill, 2 or 3 flute'}
for d, t in DRILLS.items():
    TOOLS[t] = f'Jobber drill {d} mm'

MAT = {  # rpm cap, surface speed m/min for drills, end-mill (rpm, feed mm/min, plunge, stepdown) per tool
    'al': {'drill_vc': 60, 'spot': (3000, 150), 2: (5000, 400, 120, 1.0), 3: (4000, 500, 150, 1.5), 'peck': 2.0},
    'steel': {'drill_vc': 18, 'spot': (1000, 60), 2: (1600, 100, 40, 0.5), 3: (1000, 90, 30, 0.8), 'peck': 1.0},
    'brass': {'drill_vc': 50, 'spot': (3000, 150), 2: (4500, 300, 90, 0.7), 3: (3500, 350, 100, 1.0), 'peck': 1.5},
}


def f(v):
    s = ('%.3f' % v).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


class Prog:
    def __init__(self, num, name, part, mat, setup, zinfo):
        self.num, self.name, self.part, self.mat = num, name, part, MAT[mat]
        self.matname = mat
        self.l = []
        self.tool = None
        self.used = []
        self.xs, self.ys = [], []
        self.setup, self.zinfo = setup, zinfo
        self.l += ['%', f'O{num} ({name})', f'(Part: {part})', f'(Setup: {setup})', f'(Z0: {zinfo}; X0 Y0 = lower-left corner of the view, G54)',
                   '(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)',
                   'G21 G17 G40 G49 G80 G90 G94', 'G54']

    def track(self, x, y):
        self.xs.append(x); self.ys.append(y)

    def tc(self, t, rpm, note=''):
        rpm = min(int(rpm), 5000)
        if self.tool != t:
            if self.tool is not None:
                self.l += ['M5', 'M9', 'G0 Z25']
            self.l += [f'(T{t}: {TOOLS[t]}{" - " + note if note else ""})', f'T{t} M6', f'G43 H{t}', f'S{rpm} M3', 'M8', 'G0 Z25']
            self.tool = t
            if t not in self.used:
                self.used.append(t)

    def spot(self, pts, depth=1.0):
        rpm, fd = self.mat['spot']
        self.tc(1, rpm)
        self.l.append(f'G0 X{f(pts[0][0])} Y{f(pts[0][1])}')
        self.l.append('G0 Z5')
        first = True
        for x, y in pts:
            self.track(x, y)
            if first:
                self.l.append(f'G81 G99 X{f(x)} Y{f(y)} Z-{f(depth)} R2 F{fd}'); first = False
            else:
                self.l.append(f'X{f(x)} Y{f(y)}')
        self.l += ['G80', 'G0 Z25']

    def drill(self, d, pts, depth, note=''):
        t = DRILLS[d]
        rpm = 1000 * self.mat['drill_vc'] / (math.pi * d)
        fd = max(30, min(250, round(rpm * d * (0.012 if self.matname != 'steel' else 0.008))))
        self.tc(t, rpm, note)
        self.l.append(f'G0 X{f(pts[0][0])} Y{f(pts[0][1])}')
        self.l.append('G0 Z5')
        first = True
        for x, y in pts:
            self.track(x, y)
            if first:
                self.l.append(f'G83 G99 X{f(x)} Y{f(y)} Z-{f(depth)} R2 Q{f(self.mat["peck"])} F{fd}'); first = False
            else:
                self.l.append(f'X{f(x)} Y{f(y)}')
        self.l += ['G80', 'G0 Z25']

    def mill(self, t):
        rpm, fd, pl, sd = self.mat[t]
        self.tc(t, rpm)
        return fd, pl, sd

    def levels(self, depth, sd):
        n = max(1, math.ceil(depth / sd - 1e-9))
        return [depth * (k + 1) / n for k in range(n)]

    def path(self, t, pts, depth, closed=False, arcs=None, note=''):
        """Contour along pts (list of (x,y) or ('G2'/'G3', x, y, i, j)) at stepped depth, plunge-ramping at the start."""
        fd, pl, sd = self.mill(t)
        if note:
            self.l.append(f'({note})')
        x0, y0 = pts[0]
        self.track(x0, y0)
        self.l += [f'G0 X{f(x0)} Y{f(y0)}', 'G0 Z2']
        for z in self.levels(depth, sd):
            self.l.append(f'G1 Z-{f(z)} F{pl}')
            seq = pts[1:] + ([pts[0]] if closed else [])
            for p in seq:
                if isinstance(p[0], str):
                    g, x, y, i, j = p
                    self.l.append(f'{g} X{f(x)} Y{f(y)} I{f(i)} J{f(j)} F{fd}')
                    self.track(x, y)
                else:
                    self.l.append(f'G1 X{f(p[0])} Y{f(p[1])} F{fd}')
                    self.track(*p)
            if not closed:
                self.l.append('G0 Z2')
                self.l.append(f'G0 X{f(x0)} Y{f(y0)}')
        self.l.append('G0 Z25')

    def helix(self, t, cx, cy, dia, depth, note=''):
        """Helical bore of finished diameter dia with end mill t, full turns of 0.5 x stepdown."""
        fd, pl, sd = self.mill(t)
        tooldia = 6 if t == 2 else 10
        r = (dia - tooldia) / 2
        if r <= 0.05:
            raise ValueError('bore too small for tool')
        pitch = sd * 0.5
        self.l += [f'({note or "helical bore"} D{f(dia)} at X{f(cx)} Y{f(cy)})', f'G0 X{f(cx + r)} Y{f(cy)}', 'G0 Z2', 'G1 Z0 F' + str(pl)]
        z = 0.0
        while z < depth - 1e-9:
            z = min(depth, z + pitch)
            self.l.append(f'G3 X{f(cx + r)} Y{f(cy)} Z-{f(z)} I{f(-r)} J0 F{fd}')
        self.l.append(f'G3 X{f(cx + r)} Y{f(cy)} I{f(-r)} J0 F{fd}')
        self.l += ['G1 X' + f(cx) + ' Y' + f(cy), 'G0 Z25']
        self.track(cx + r, cy); self.track(cx - r, cy)   # tool-centre extremes
        self.track(cx, cy + r); self.track(cx, cy - r)

    def pocket_rect(self, t, x0, y0, x1, y1, depth, note=''):
        """Rectangular pocket x0..x1, y0..y1 (finished size), zigzag then a finishing contour."""
        fd, pl, sd = self.mill(t)
        rr = 3 if t == 2 else 5
        ax0, ay0, ax1, ay1 = x0 + rr, y0 + rr, x1 - rr, y1 - rr
        self.l.append(f'({note})')
        for z in self.levels(depth, sd):
            self.l += [f'G0 X{f(ax0)} Y{f(ay0)}', 'G0 Z1', f'G1 Z-{f(z)} F{pl}']
            if ax1 > ax0 + 1e-6:
                y = ay0; up = True
                while True:
                    self.l.append(f'G1 X{f(ax1 if up else ax0)} Y{f(y)} F{fd}')
                    if y >= ay1 - 1e-6:
                        break
                    y = min(ay1, y + rr * 1.2)
                    self.l.append(f'G1 Y{f(y)} F{fd}')
                    up = not up
                self.l += [f'G1 X{f(ax0)} Y{f(ay0)} F{fd}', f'G1 X{f(ax1)}', f'G1 Y{f(ay1)}', f'G1 X{f(ax0)}', f'G1 Y{f(ay0)}']
            else:
                self.l.append(f'G1 Y{f(ay1)} F{fd}')
                self.l.append(f'G1 Y{f(ay0)}')
            self.l.append('G0 Z2')
        self.l.append('G0 Z25')
        for p in ((ax0, ay0), (ax1, ay1)):   # tool-centre extremes
            self.track(*p)

    def sloped_face(self, t, xlen, ywid, dfun, note=''):
        """Surface a face whose depth below Z0 is dfun(x) (>=0) with a flat end mill, passes along Y.
        Each pass is cut no deeper than the finished surface anywhere under the cutter, so the slope is never gouged;
        the 1 mm finishing stepover leaves steps of about 0.17 mm, inside the 0.3 grinding allowance."""
        fd, pl, sd = self.mill(t)
        rc = 3.0 if t == 2 else 5.0
        def safe(c):
            lo, hi = max(0.0, c - rc), min(xlen, c + rc)
            if lo > hi:
                return 0.0
            return max(0.0, min(dfun(lo), dfun(hi)))
        dmax = max(dfun(0), dfun(xlen))
        xs = [-rc + k * 4.0 for k in range(int(math.ceil((xlen + 2 * rc) / 4.0)) + 1)]
        self.l.append(f'({note})')
        z = 0.0
        while z < dmax - 1e-9:
            z = min(dmax, z + sd)
            rows = [x for x in xs if safe(x) > z - sd + 1e-6]
            if not rows:
                continue
            self.l.append(f'(layer to {f(z)} below Z0, capped at the finished slope)')
            for x in rows:
                d = min(z, safe(x))
                self.l += [f'G0 X{f(x)} Y-7', f'G1 Z-{f(d)} F{pl}', f'G1 Y{f(ywid + 7)} F{fd}', 'G0 Z1']
                self.track(x, -7); self.track(x, ywid + 7)
        self.l.append('(finishing: 1 mm stepover along X)')
        x = -rc
        while x <= xlen + rc + 1e-6:
            d = safe(x)
            self.l += [f'G0 X{f(x)} Y-7', f'G1 Z-{f(d)} F{pl}', f'G1 Y{f(ywid + 7)} F{fd}', 'G0 Z1']
            self.track(x, -7); self.track(x, ywid + 7)
            x += 1.0
        self.l.append('G0 Z25')

    def end(self):
        self.l += ['M5', 'M9', 'G0 Z25', 'G53 G0 Z0' if False else 'G0 Z50', 'M30', '%']
        fn = os.path.join(OUT, f'O{self.num}_{self.name.replace(" ", "_").replace(",", "")}.nc')
        open(fn, 'w').write('\n'.join(self.l) + '\n')
        return dict(num=self.num, name=self.name, part=self.part, file=os.path.basename(fn), tools=self.used,
                    setup=self.setup, z0=self.zinfo, xmin=min(self.xs), xmax=max(self.xs), ymin=min(self.ys), ymax=max(self.ys), mat=self.matname)


progs = []
yarc = 60 + math.sqrt(47 ** 2 - 40 ** 2)

# ---- Side plates ----
p = Prog(1101, 'side plate holes, stacked pair', 'Side plates (2), 12 mm 6060', 'al',
         'Both blanks finished to 130 x 189, screwed back to back through the window area, clamped flat on a sacrificial plate; outer face of the LEFT plate up, front edge to +X',
         'top face of the stack')
A = [(50, 179.9), (80, 179.9)]; B = [(65, 179.9)]; C = [(25, 158), (105, 158), (25, 135), (105, 121)]
DE = [(37, 103), (37, 121), (8, 140.8), (8, 150.8)]; F = [(89, 51), (117, 51)]
p.spot(A + B + C + DE + F)
p.drill(8.5, A, 25.5, 'A: M8 clearance')
p.drill(5.8, B, 25.5, 'B: dowel, ream 6 H7 later with the roof block')
p.drill(5.1, C, 25.5, 'C: cage cross pins')
p.drill(5.5, DE, 25.5, 'D, E: M5 clearance')
p.drill(5.0, F, 25.5, 'F: tap M6 through after')
progs.append(p.end())

p = Prog(1102, 'side plate window and notch', 'Side plate, each, 12 mm 6060', 'al',
         'One plate at a time on a sacrificial plate, outer face up, front edge to +X; rough out the notch and window with a saw first, 2 mm inside the lines',
         'top face of the plate')
win = [(42, -6), (42, 23), (22, 23), (22, 33.2), (42, 33.2), (42, 42), (88, 42), (88, 33.2), (108, 33.2), (108, 23), (88, 23), (88, -6)]
p.path(2, win, 12.5, note='window and notch, 6 mm cutter on the inside (inside corners come out R3)')
p.path(2, [(25, 28.1), (105, 28.1)], 12.5, note='window centre clearing pass')
progs.append(p.end())

p = Prog(1103, 'side plate lift and spring pockets', 'Side plate, each, inner face', 'al',
         'Plate inner face up (same program for both: the pocket is on the centreline x 65), front edge to +X for the LEFT plate, to -X for the RIGHT plate; X0 Y0 at the lower-left corner as clamped',
         'inner face')
p.pocket_rect(2, 61.5, 102.9, 68.5, 111.9, 3.5, 'G1 anvil lift pocket 7 x 9 x 3.5')
p.path(2, [(65, 95.9), (65, 102.9)], 3.5, note='G2 spring pocket, 6 wide, z 92.9 to 102.9, 3.5 deep')
progs.append(p.end())

# ---- Fork plate ----
p = Prog(1201, 'fork plate', 'Fork plate, 16 mm mild steel', 'steel',
         'Blank 92 x 66 x 16 (edges and faces already milled), bottom face up for the holes, then top face up for the slot; slot open end toward -Y; rough the slot with a saw first',
         'face as clamped')
K = [(10, 6), (82, 6), (10, 60), (82, 60)]
p.spot(K)
p.drill(5.0, K, 15, 'K: M6 tap drill, from the BOTTOM face, tap 12 deep (pattern is symmetric, so the same X/Y work from either face)')
p.l += ['M5', 'M9', 'G0 Z50']
p.l.append('M0 (turn the plate over: TOP face up, re-zero Z on the top face, same X0 Y0 corner)')
p.tool = None
slot = [(24, -6), (24, 33), ('G2', 68, 33, 22, 0), (68, -6)]
p.path(3, slot, 16.5, note='slot 54 wide with R27 end, 10 mm cutter on the inside')
progs.append(p.end())

# ---- Base plate ----
p = Prog(1301, 'head-top base plate', 'Base plate, 12 mm 6060', 'al',
         'Blank finished to 115 x 107 x 12, front edge toward -Y, on a sacrificial plate; saw out the R47 cut-out and slot to 3 mm inside the line first',
         'top face')
pA = [(27.5, 7.5), (87.5, 7.5)]; pB = [(8.5, 100), (106.5, 100)]; pC = [(10.5, 22), (104.5, 22)]; pD = [(57.5, 7.5), (8.5, 90)]
p.spot(pA + pB + pC + pD)
p.drill(6.6, pA + pB, 12.5, 'A, B: M6 clearance')
p.drill(6.8, pC, 12.5, 'C: M8 tap drill; tap square with the plate still clamped')
p.drill(5.8, pD, 12.5, 'D: dowels, ream 6 H7 on the head later')
ix = 57.5 - 42 * math.sqrt(1 - (35 / 42) ** 2) * 0  # placeholder for clarity
yy = 60 + math.sqrt(42 ** 2 - 35 ** 2)
cut = [(22.5, 113), (22.5, yy), ('G3', 92.5, yy, 35, 60 - yy), (92.5, 113)]
p.path(3, cut, 12.5, note='R47 cut-out and 80 slot, 10 mm cutter inside')
p.path(3, [(-6, 7 - 5 * math.sqrt(2) + 6), (7 - 5 * math.sqrt(2) + 6, -6)], 12.5, note='front-left 7 x 7 chamfer')
p.path(3, [(121, 7 - 5 * math.sqrt(2) + 6), (115 - (7 - 5 * math.sqrt(2) + 6), -6)], 12.5, note='front-right 7 x 7 chamfer')
progs.append(p.end())

# ---- Mount plate ----
c = 50 - 74.07 / 2
p = Prog(1401, 'cylinder mount plate', 'Mount plate, 12 mm 6060', 'al',
         'Blank finished to 100 x 100 x 12 on a sacrificial plate. Better: spot the L holes from the cylinder itself (see manual) and skip the L section',
         'top face')
L = [(c, c), (100 - c, c), (c, 100 - c), (100 - c, 100 - c)]; N = [(23, 35), (77, 35), (23, 65), (77, 65)]
p.spot(L + N + [(50, 50)])
p.drill(6.6, N, 12.5, 'N: M6 clearance')
p.drill(6.8, L, 12.5, 'L: pilot for the 13 mm holes')
for x, y in L:
    p.helix(3, x, y, 13, 12.5, 'L: 13 mm clearance for M12')
p.helix(3, 50, 50, 40, 12.5, 'M1: 40 mm bore')
progs.append(p.end())

# ---- Roof block ----
p = Prog(1501, 'roof block top face', 'Roof block, 6061-T6, 60 x 42 x 19', 'al',
         'Block finished to 60 x 42 x 19, top face up, 60 along X', 'top face')
P4 = [(5, 7), (55, 7), (5, 35), (55, 35)]
p.spot(P4)
p.drill(3.4, P4, 19.5, 'P: M3 clearance')
for x, y in P4:
    p.helix(2, x, y, 6.5, 3.5, 'P: counterbore 6.5 x 3.5')
progs.append(p.end())

p = Prog(1502, 'roof block side face', 'Roof block, each 60 x 19 side face', 'al',
         'Block on its side, one 60 x 19 face up, 60 along X, Y0 at the BOTTOM (wear-plate) face; run once for each side face', 'side face as clamped')
p.spot([(15, 10), (45, 10), (30, 10)])
p.drill(6.8, [(15, 10), (45, 10)], 17, 'Q: M8 tap drill, tap 14 deep')
p.drill(5.8, [(30, 10)], 11, 'R: dowel, ream 6 H7 x 10 deep with the plates (manual)')
progs.append(p.end())

# ---- Wear plate (O1, annealed) ----
p = Prog(1601, 'roof wear plate', 'Wear plate, O1 60 x 40 x 5 (annealed, before hardening)', 'steel',
         'Plate on parallels, top (non-rolling) face up, 60 along X', 'top face')
S4 = [(5, 6), (55, 6), (5, 34), (55, 34)]
p.spot(S4, 0.6)
p.drill(2.5, S4, 3.2, 'S: M3 tap drill to 3.2; tap 3 deep with a bottoming tap')
progs.append(p.end())

# ---- Thrust bar and strip ----
p = Prog(1701, 'thrust bar anvil face', 'Rear thrust bar, 6061-T6 42 x 30 x 10', 'al', 'Anvil face up, 42 along X', 'anvil face')
p.spot([(6, 15), (36, 15)])
p.drill(2.5, [(6, 15), (36, 15)], 9, 'T: M3 tap drill, tap 8 deep')
progs.append(p.end())
p = Prog(1702, 'thrust bar end', 'Rear thrust bar, each 10 x 30 end', 'al', 'Bar on end in the vise, 30 along Y, 10 along X; run for each end', 'end face')
p.spot([(5, 6), (5, 24)])
p.drill(4.2, [(5, 6), (5, 24)], 15, 'U: M5 tap drill, tap 12 deep')
progs.append(p.end())
p = Prog(1703, 'bronze strip', 'Bronze strip 40 x 25 x 3', 'brass', 'Strip taped to a sacrificial plate, 40 along X', 'top face')
p.spot([(5, 12.5), (35, 12.5)])
p.drill(3.4, [(5, 12.5), (35, 12.5)], 3.5, 'V: M3 clearance; countersink 90 deg by hand so heads sit 0.3 below')
progs.append(p.end())

# ---- Stop block ----
p = Prog(1801, 'stop block', 'Rear stop block, 6061-T6 42 x 20 x 10', 'al', 'Wedge face up, 42 along X', 'wedge face')
p.spot([(21, 10)])
p.drill(6.8, [(21, 10)], 10.5, 'W: M8 tap drill through; tap square')
progs.append(p.end())
p = Prog(1802, 'stop block end', 'Rear stop block, each 10 x 20 end', 'al', 'Block on end, 20 along Y, 10 along X; run for each end', 'end face')
p.spot([(5, 5), (5, 15)])
p.drill(4.2, [(5, 5), (5, 15)], 15, 'X: M5 tap drill, tap 12 deep')
progs.append(p.end())

# ---- Lugs ----
p = Prog(1901, 'float lug bore', 'Float lug, each, 40 x 24 x 20, top face', 'al',
         'Top (40 x 24) face up, 40 along X, mounting face toward -Y (Y0 on the mounting face)', 'top face')
p.spot([(20, 14)])
p.drill(6.8, [(20, 14)], 20.5, 'pilot')
p.helix(3, 20, 14, 15.8, 20.5, 'Y1: rough bore 15.8, then ream 16 H7 by hand or on the mill')
progs.append(p.end())
p = Prog(1902, 'float lug mounting holes', 'Float lug, each, mounting face', 'al',
         'Mounting (40 x 20) face up, 40 along X', 'mounting face')
p.spot([(6, 10), (34, 10)])
p.drill(7.0, [(6, 10), (34, 10)], 24.5, 'Z: 7 mm clearance through the 24')
progs.append(p.end())

# ---- Roller cage (brass) ----
p = Prog(2001, 'roller cage', 'Roller cage, each, 2 mm brass', 'brass',
         'Brass blank 56 x 45 taped to a sacrificial plate; X0 Y0 at the lower-left of the 52 x 41 outline (blank overhangs 2 mm each side)', 'top face')


def dogbone_rect(x0, y0, x1, y1, rr):
    """Inside contour of a rectangle with dog-bone corner reliefs for cutter radius rr."""
    a = rr / math.sqrt(2)
    cx0, cy0, cx1, cy1 = x0 + rr, y0 + rr, x1 - rr, y1 - rr
    pts = [(cx0, cy0), (x0 + a, y0 + a), (cx0, cy0), (cx1, cy0), (x1 - a, y0 + a), (cx1, cy0),
           (cx1, cy1), (x1 - a, y1 - a), (cx1, cy1), (cx0, cy1), (x0 + a, y1 - a), (cx0, cy1), (cx0, cy0)]
    return pts


p.path(2, dogbone_rect(9.85, 2.2, 24.15, 38.8, 3), 2.3, note='window 1, dog-bone corners so the rollers sit square')
p.path(2, dogbone_rect(27.85, 2.2, 42.15, 38.8, 3), 2.3, note='window 2')
outline = [(6, -3), (6, 19 - 3), (-3, 16), (-3, 25), (6 - 3, 25), (3, 41 + 3), (49, 44), (49, 25), (55, 25), (55, 16), (49, 16), (49, -3), (6 - 3, -3)]
outline = [(3, -3), (3, 16), (-3, 16), (-3, 25), (3, 25), (3, 44), (49, 44), (49, 25), (55, 25), (55, 16), (49, 16), (49, -3), (3, -3)]
p.path(2, outline, 2.3, note='outline with tongues, 6 mm cutter outside (tongue roots come out R3: file square)')
progs.append(p.end())

# ---- Wedge (4140 pre-hardened, before heat treatment) ----
t_lead, t_trail, L, slope = 10.11, 23.5, 80.0, math.tan(math.radians(9.5))
p = Prog(2101, 'wedge underside slope', 'Wedge, 4140, before hardening', 'steel',
         'Blank milled to 80.0 x 40.6 x 24.1 (top already flat), TOP face down on parallels, 80 along X with the THIN (leading) end at X0, 40.6 along Y; saw off the bulk first, 1.5 above the line',
         'top of the blank as clamped (24.1 above the parallels)')
dw = lambda x: max(0.0, 24.1 - (t_lead + x * slope + 0.6))
p.sloped_face(3, L, 40.6, dw, 'underside at 9.5 deg, leaving 0.3 for grinding (top also has 0.3)')
progs.append(p.end())

p = Prog(2102, 'wedge trailing end hole', 'Wedge, 4140, trailing end face', 'steel',
         'Wedge standing on its trailing end, 40.6 along X, as-milled TOP face toward +Y; X0 Y0 at the lower-left corner of the end face as seen from above (Y0 on the slope side)',
         'trailing end face')
yc = 24.1 - 12.05
p.spot([(20.3, yc)])
p.drill(6.8, [(20.3, yc)], 18, 'pilot')
p.drill(12.5, [(20.3, yc)], 18, 'M14 x 1.5 tap drill; flat-bottom with an end mill if you can; tap 14 full thread')
progs.append(p.end())

# ---- Anvil ----
p = Prog(2201, 'anvil top slope', 'Anvil, 4140, before hardening', 'steel',
         'Blank squared to 40.0 x 40.6 x 23.3, underside down, 40 along X with the THRUST (rear, tall) end at X0', 'top of the blank (23.3 above the parallels)')
da = lambda x: x * slope
p.sloped_face(3, 40.0, 40.6, da, 'top at 9.5 deg falling toward +X, leaving 0.3 for grinding')
progs.append(p.end())

p = Prog(2202, 'anvil lift pin holes', 'Anvil, 4140, each side face', 'steel',
         'Anvil on its side, a 40 x 23.3 side face up, thrust face at X0, as-milled underside at Y0; run for each side',
         'side face')
p.spot([(20.0, 8.3)])
p.drill(4.8, [(20.0, 8.3)], 7.5, 'pin hole, tip depth 7.5 (full dia about 6.1): hand-ream 5 H7 to 6.5 after')
progs.append(p.end())

# ---- index ----
import json
json.dump(dict(progs=progs, tools={str(k): v for k, v in TOOLS.items()}), open(os.path.join(OUT, 'index.json'), 'w'), indent=1)
for q in progs:
    print(q['num'], q['file'], 'X', f(q['xmin']), f(q['xmax']), 'Y', f(q['ymin']), f(q['ymax']), q['tools'])
