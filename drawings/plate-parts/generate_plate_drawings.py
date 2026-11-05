"""Plate-part drawings: one SVG per part, origin (0,0) at the lower-left of each view, mm.
Emits JSX widget code (Claude Docs) and plain SVG (for PNG) from the same geometry."""
import json, math, re, sys

TOK = {'ink': 'var(--cds-text-primary)', 'quiet': 'var(--cds-text-secondary)',
       'edge': 'var(--cds-chart-axis)', 'acc': 'var(--cds-chart-categorical-1)',
       'hid': 'var(--cds-chart-categorical-2)', 'brz': 'var(--cds-chart-categorical-3)'}
HEX = {'ink': '#1f1e1d', 'quiet': '#6b6a66', 'edge': '#8a8984', 'acc': '#2f6fb0',
       'hid': '#c2410c', 'brz': '#a16207'}

# ---------------------------------------------------------------- part data
# outline: list of ('M',x,y) ('L',x,y) ('A',r,large,sweep_ccw,x,y) ('Z',)
# holes: (id, x, y, dia_draw, size_text, depth_text, kind)  kind: 'thru','blind','tap','edge'
# rects (pockets/windows, dashed): (x0,y0,x1,y1,label)

def rect(w, h):
    return [('M', 0, 0), ('L', w, 0), ('L', w, h), ('L', 0, h), ('Z',)]

PARTS = []

# 1. Side plate ------------------------------------------------------------
PARTS.append(dict(
    slug='side-plate', title='Side plate (2 off, mirrored pair)',
    sub='12 mm 6061-T6 (or 5083-H116). View from the machine\'s left, front to the right; 0,0 = rear bottom corner (X −65, Z −37).',
    views=[
        dict(name='Face', w=130, h=189,
             outline=[('M', 0, 0), ('L', 39, 0), ('L', 39, 20), ('L', 19, 20), ('L', 19, 36.2), ('L', 39, 36.2),
                      ('L', 39, 45), ('L', 91, 45), ('L', 91, 36.2), ('L', 111, 36.2), ('L', 111, 20), ('L', 91, 20),
                      ('L', 91, 0), ('L', 130, 0), ('L', 130, 189), ('L', 0, 189), ('Z',)],
             xs=[0, 19, 39, 65, 91, 111, 130], ys=[0, 20, 36.2, 45, 189],
             holes=[('A1', 50, 179.9, 8.5, 'Ø8.5', 'thru', 'thru'), ('A2', 80, 179.9, 8.5, 'Ø8.5', 'thru', 'thru'),
                    ('B1', 65, 179.9, 6, 'Ø6 H7', 'thru, ream with roof block', 'thru'),
                    ('C1', 25, 158, 5.1, 'Ø5.1', 'thru', 'thru'), ('C2', 105, 158, 5.1, 'Ø5.1', 'thru', 'thru'),
                    ('C3', 25, 135, 5.1, 'Ø5.1', 'thru', 'thru'), ('C4', 105, 121, 5.1, 'Ø5.1', 'thru', 'thru'),
                    ('D1', 37, 103, 5.5, 'Ø5.5', 'thru', 'thru'), ('D2', 37, 121, 5.5, 'Ø5.5', 'thru', 'thru'),
                    ('E1', 8, 140.8, 5.5, 'Ø5.5', 'thru', 'thru'), ('E2', 8, 150.8, 5.5, 'Ø5.5', 'thru', 'thru'),
                    ('F1', 89, 51, 6, 'M6 (drill Ø5.0)', 'thru', 'tap'), ('F2', 117, 51, 6, 'M6 (drill Ø5.0)', 'thru', 'tap'),
                    ('G2', 65, 97.9, 6, 'Ø6 spring pocket', 'Z 92.9–102.9', 'pocket')],
             rects=[(61.5, 102.9, 68.5, 111.9, 'G1')]),
        dict(name='Front edge', w=12, h=189, outline=rect(12, 189), xs=[0, 6, 12], ys=[], gap=26,
             holes=[('H1', 6, 124, 6, 'M6 Helicoil', '15 deep', 'tap'), ('H2', 6, 154, 6, 'M6 Helicoil', '15 deep', 'tap')]),
        dict(name='Bottom edge', w=130, h=12, outline=rect(130, 12), xs=[29, 101], ys=[6], below=True,
             holes=[('J1', 29, 6, 6.6, 'Ø6.6', 'thru the 20 foot', 'thru'), ('J2', 101, 6, 6.6, 'Ø6.6', 'thru the 20 foot', 'thru')]),
    ],
    notes=['Window 92 × 16.2 (x 19–111, y 20–36.2) takes the fork; slot 52 wide (x 39–91) open to y 45. Inside corners R2.',
           'G1: anvil lift pocket 7 × 9 × 3.5 deep, inner face only. G2: Ø6 × 10 spring pocket below it, on the pocket centre line.',
           'Machine both plates stacked; coordinates are the same for both in this view. Pockets go on the two inner faces.',
           'Edge views: x across the 12 thickness (H, J at mid-thickness 6). H in the front edge (x 130 on the face view), J up through each foot.']))

# 2. Fork plate ------------------------------------------------------------
PARTS.append(dict(
    slug='fork-plate', title='Fork plate (1 off)',
    sub='16 mm mild steel. Plan from above, open end of the slot at the bottom; 0,0 = lower-left corner.',
    views=[dict(name='Plan', w=92, h=66,
                outline=[('M', 0, 0), ('L', 19, 0), ('L', 19, 33), ('A', 27, 0, 1, 73, 33), ('L', 73, 0), ('L', 92, 0),
                         ('L', 92, 66), ('L', 0, 66), ('Z',)],
                xs=[0, 10, 19, 46, 73, 82, 92], ys=[0, 6, 33, 60, 66],
                holes=[('K1', 10, 6, 6, 'M6 (drill Ø5.0)', '12 deep from below', 'tap'),
                       ('K2', 82, 6, 6, 'M6 (drill Ø5.0)', '12 deep from below', 'tap'),
                       ('K3', 10, 60, 6, 'M6 (drill Ø5.0)', '12 deep from below', 'tap'),
                       ('K4', 82, 60, 6, 'M6 (drill Ø5.0)', '12 deep from below', 'tap')])],
    notes=['Slot 54 +0.2/0 wide (x 19–73), open at y 0, closed end R27 centred at (46, 33).',
           'Top face flat (fly-cut): it bears on the collar flange. Break the slot edges 0.5.']))

# 3. Base plate ------------------------------------------------------------
yarc = 60 + math.sqrt(47 ** 2 - 40 ** 2)
PARTS.append(dict(
    slug='base-plate', title='Head-top base plate (1 off)',
    sub='12 mm 6061-T6. Plan from above, front at the bottom; 0,0 = front-left corner. Spindle axis at (57.5, 60).',
    views=[dict(name='Plan', w=115, h=107,
                outline=[('M', 0, 7), ('L', 7, 0), ('L', 108, 0), ('L', 115, 7), ('L', 115, 107), ('L', 97.5, 107),
                         ('L', 97.5, yarc), ('A', 47, 1, 1, 17.5, yarc), ('L', 17.5, 107), ('L', 0, 107), ('Z',)],
                xs=[0, 8.5, 17.5, 27.5, 57.5, 87.5, 97.5, 106.5, 115], ys=[0, 7.5, 13, 22, 60, 84.7, 90, 100, 107],
                axis=(57.5, 60),
                holes=[('A1', 27.5, 7.5, 6.6, 'Ø6.6', 'thru', 'thru'), ('A2', 87.5, 7.5, 6.6, 'Ø6.6', 'thru', 'thru'),
                       ('B1', 8.5, 100, 6.6, 'Ø6.6', 'thru', 'thru'), ('B2', 106.5, 100, 6.6, 'Ø6.6', 'thru', 'thru'),
                       ('C1', 10.5, 22, 8, 'M8 (drill Ø6.8)', 'thru, square within 0.05', 'tap'),
                       ('C2', 104.5, 22, 8, 'M8 (drill Ø6.8)', 'thru, square within 0.05', 'tap'),
                       ('D1', 57.5, 7.5, 6, 'Ø6 H7', 'thru; drill Ø5.8, ream on the head', 'thru'),
                       ('D2', 8.5, 90, 6, 'Ø6 H7', 'thru; drill Ø5.8, ream on the head', 'thru')])],
    notes=['Front corners chamfered 7 × 7. Cut-out R47 on the spindle axis, opening into a slot 80 wide (x 17.5–97.5) to the rear edge.',
           'D1 leaves a 2.5 web to the R47 cut-out: drill it after profiling and deburr gently.',
           'A and B: spot through onto the head, drill Ø5.0 through the 9 mm casting and tap M6.']))

# 4. Mount plate -----------------------------------------------------------
c = 50 - 74.07 / 2
PARTS.append(dict(
    slug='mount-plate', title='Cylinder mount plate (1 off)',
    sub='12 mm 6061-T6. Either face (symmetric); 0,0 = lower-left corner. Centre (50, 50) on the cylinder axis, Z 102.',
    views=[dict(name='Face', w=100, h=100, outline=rect(100, 100),
                xs=[0, 12.97, 23, 50, 77, 87.03, 100], ys=[0, 12.97, 35, 50, 65, 87.03, 100],
                holes=[('L1', c, c, 13, 'Ø13', 'thru', 'thru'), ('L2', 100 - c, c, 13, 'Ø13', 'thru', 'thru'),
                       ('L3', c, 100 - c, 13, 'Ø13', 'thru', 'thru'), ('L4', 100 - c, 100 - c, 13, 'Ø13', 'thru', 'thru'),
                       ('M1', 50, 50, 40, 'Ø40 bore', 'thru', 'thru'),
                       ('N1', 23, 35, 6.6, 'Ø6.6', 'thru', 'thru'), ('N2', 77, 35, 6.6, 'Ø6.6', 'thru', 'thru'),
                       ('N3', 23, 65, 6.6, 'Ø6.6', 'thru', 'thru'), ('N4', 77, 65, 6.6, 'Ø6.6', 'thru', 'thru')])],
    notes=['L: 74.07 square for the M12 cylinder screws; spot them from the cylinder itself rather than marking out.',
           'N: M6 × 25 into the side plates\' front edges (Z 87 and 117).']))

# 5. Roof block ------------------------------------------------------------
PARTS.append(dict(
    slug='roof-block', title='Roof block (1 off)',
    sub='6061-T6, 60 × 42 × 19 from 20 mm plate. 0,0 = lower-left of each view; x along the wedge travel.',
    views=[dict(name='Top face', w=60, h=42, outline=rect(60, 42), xs=[0, 5, 30, 55, 60], ys=[0, 7, 35, 42],
                holes=[('P1', 5, 7, 3.4, 'Ø3.4, c\'bore Ø6.5 × 3.5', 'thru', 'cb'), ('P2', 55, 7, 3.4, 'Ø3.4, c\'bore Ø6.5 × 3.5', 'thru', 'cb'),
                       ('P3', 5, 35, 3.4, 'Ø3.4, c\'bore Ø6.5 × 3.5', 'thru', 'cb'), ('P4', 55, 35, 3.4, 'Ø3.4, c\'bore Ø6.5 × 3.5', 'thru', 'cb')]),
           dict(name='Side face (both)', w=60, h=19, outline=rect(60, 19), xs=[0, 15, 30, 45, 60], ys=[0, 10, 19], below=True,
                holes=[('Q1', 15, 10, 8, 'M8 (drill Ø6.8 × 17)', '14 deep', 'tap'), ('Q2', 45, 10, 8, 'M8 (drill Ø6.8 × 17)', '14 deep', 'tap'),
                       ('R1', 30, 10, 6, 'Ø6 H7', '10 deep', 'blind')])],
    notes=['42 −0/−0.05 wide: it sets the side-plate spacing. Side faces square to the base within 0.02.',
           'Q and R on both 60 × 19 side faces (the faces against the side plates).']))

# 6. Wear plate ------------------------------------------------------------
PARTS.append(dict(
    slug='wear-plate', title='Roof wear plate (1 off)',
    sub='O1 ground flat stock 40 × 5, 60 long. Top (non-rolling) face; 0,0 = lower-left corner.',
    views=[dict(name='Top face', w=60, h=40, outline=rect(60, 40), xs=[0, 5, 55, 60], ys=[0, 6, 34, 40],
                holes=[('S1', 5, 6, 3, 'M3 (drill Ø2.5 × 3.2 flat)', '3 deep', 'tap'), ('S2', 55, 6, 3, 'M3 (drill Ø2.5 × 3.2 flat)', '3 deep', 'tap'),
                       ('S3', 5, 34, 3, 'M3 (drill Ø2.5 × 3.2 flat)', '3 deep', 'tap'), ('S4', 55, 34, 3, 'M3 (drill Ø2.5 × 3.2 flat)', '3 deep', 'tap')])],
    notes=['Drill and tap before hardening; 1.8 of skin is left, so the rolling face stays unbroken.',
           'Harden 58–62 HRC, grind both faces parallel within 0.005.']))

# 7. Thrust bar + bronze strip ---------------------------------------------
PARTS.append(dict(
    slug='thrust-bar', title='Rear thrust bar and bronze strip (1 off each)',
    sub='Bar 6061-T6 42 × 30 × 10; strip bronze 40 × 25 × 3. 0,0 = lower-left of each view.',
    views=[dict(name='Anvil face', w=42, h=30, outline=rect(42, 30), xs=[0, 6, 36, 42], ys=[0, 15, 30],
                holes=[('T1', 6, 15, 3, 'M3 (drill Ø2.5)', '8 deep', 'tap'), ('T2', 36, 15, 3, 'M3 (drill Ø2.5)', '8 deep', 'tap')]),
           dict(name='End (both)', w=10, h=30, outline=rect(10, 30), xs=[0, 5, 10], ys=[6, 24], gap=30,
                holes=[('U1', 5, 6, 5, 'M5 (drill Ø4.2 × 15)', '12 deep', 'tap'), ('U2', 5, 24, 5, 'M5 (drill Ø4.2 × 15)', '12 deep', 'tap')]),
           dict(name='Bronze strip', w=40, h=25, outline=rect(40, 25), xs=[0, 5, 35, 40], ys=[0, 12.5, 25], below=True,
                holes=[('V1', 5, 12.5, 3.4, 'Ø3.4, 90° csk', 'thru', 'thru'), ('V2', 35, 12.5, 3.4, 'Ø3.4, 90° csk', 'thru', 'thru')])],
    notes=['42 −0/−0.1 long with square ends. Strip sits 1 in from each end and 2.5 from each long edge; heads 0.3 below the bronze face.']))

# 8. Stop block ------------------------------------------------------------
PARTS.append(dict(
    slug='stop-block', title='Rear stop block (1 off)',
    sub='6061-T6 42 × 20 × 10. 0,0 = lower-left of each view.',
    views=[dict(name='Wedge face', w=42, h=20, outline=rect(42, 20), xs=[0, 21, 42], ys=[0, 10, 20],
                holes=[('W1', 21, 10, 8, 'M8 (drill Ø6.8)', 'thru, square within 0.05', 'tap')]),
           dict(name='End (both)', w=10, h=20, outline=rect(10, 20), xs=[0, 5, 10], ys=[5, 15], gap=30,
                holes=[('X1', 5, 5, 5, 'M5 (drill Ø4.2 × 15)', '12 deep', 'tap'), ('X2', 5, 15, 5, 'M5 (drill Ø4.2 × 15)', '12 deep', 'tap')])],
    notes=['42 −0/−0.1 long with square ends. M8 × 30 set screw and lock nut in W1 sets the wedge stop.']))

# 9. Lugs ------------------------------------------------------------------
PARTS.append(dict(
    slug='lug', title='Float lug (2 off)',
    sub='6061-T6 40 × 24 × 20 from 25 × 20 flat. 0,0 = lower-left; mounting face at y 0 in the plan.',
    views=[dict(name='Plan (top)', w=40, h=24, outline=rect(40, 24), xs=[0, 6, 20, 34, 40], ys=[0, 14, 24],
                holes=[('Y1', 20, 14, 16, 'Ø16 H7 (bush, then ream Ø12 H8)', 'thru the 20', 'thru')],
                hidden=[(6, 0, 6, 24), (34, 0, 34, 24)]),
           dict(name='Mounting face', w=40, h=20, outline=rect(40, 20), xs=[0, 6, 34, 40], ys=[0, 10, 20], below=True,
                holes=[('Z1', 6, 10, 7, 'Ø7', 'thru the 24', 'thru'), ('Z2', 34, 10, 7, 'Ø7', 'thru the 24', 'thru')])],
    notes=['Bush bore leaves a 2 wall on the outer face (24 − 14 − 8): light duty only, but take care when reaming.',
           'Z1, Z2 at 28 centres match the side plate F1, F2; Ø7 gives a little float for fitting on the pins.']))

# 10. Roller cage ----------------------------------------------------------
PARTS.append(dict(
    slug='roller-cage', title='Roller cage (2 off)',
    sub='2 mm brass sheet. 0,0 = lower-left corner of the overall 52 × 41 blank.',
    views=[dict(name='Plan', w=52, h=41,
                outline=[('M', 6, 0), ('L', 46, 0), ('L', 46, 19), ('L', 52, 19), ('L', 52, 22), ('L', 46, 22), ('L', 46, 41),
                         ('L', 6, 41), ('L', 6, 22), ('L', 0, 22), ('L', 0, 19), ('L', 6, 19), ('Z',)],
                xs=[0, 6, 9.85, 24.15, 27.85, 42.15, 46, 52], ys=[0, 2.2, 19, 22, 38.8, 41],
                holes=[], rects=[(9.85, 2.2, 24.15, 38.8, 'Z1 window'), (27.85, 2.2, 42.15, 38.8, 'Z2 window')], solidrects=True)],
    notes=['Windows 14.3 × 36.6, centres (17, 20.5) and (35, 20.5), 18 pitch; rollers Ø14 × 36 with 0.3 / 0.6 play.',
           'Tongues 6 × 3 each side carry the centring springs. Break all window edges.']))

# ---------------------------------------------------------------- rendering

def fmt(v):
    s = ('%.2f' % v).rstrip('0').rstrip('.')
    return s


class Svg:
    def __init__(self):
        self.parts = []
        self.ids = set()

    def tid(self, base):
        base = re.sub(r'[^A-Za-z0-9_-]', '-', base)[:56] or 't'
        i, b = 1, base
        while b in self.ids:
            i += 1
            b = f'{base}-{i}'
        self.ids.add(b)
        return b

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, idbase, size=11, color='ink', anchor='start', weight=None, rot=None):
        a = f" textAnchor='{anchor}'" if anchor != 'start' else ''
        w = f" fontWeight='{weight}'" if weight else ''
        r = f" transform='rotate(-90 {fmt(x)} {fmt(y)})'" if rot else ''
        s = s.replace('&', 'and')
        self.add(f"<text data-claude-text-id='{self.tid(idbase)}' x='{fmt(x)}' y='{fmt(y)}' fontSize='{size}'{a}{w}{r} fill='@{color}'>{s}</text>")


def build(part):
    sv = Svg()
    W = 760
    views = part['views']
    # scale: fit the main view into ~430 px wide and ~430 tall
    main = views[0]
    s = min(430 / main['w'], 420 / main['h'], 6)
    for v in views[1:]:
        pass
    left = 70
    top = 96
    # layout: main view at (left, top); views with below=True go under the main; others to the right of the main
    pos = []
    x_right = left + main['w'] * s
    y_below = top + main['h'] * s + 74
    for i, v in enumerate(views):
        if i == 0:
            pos.append((left, top))
        elif v.get('below'):
            pos.append((left, y_below))
            y_below += v['h'] * s + 74
        else:
            gx = x_right + v.get('gap', 40) + 30
            pos.append((gx, top))
            x_right = gx + v['w'] * s
    chart_x = max(x_right + 46, 360)
    longest = max([len(h_[4]) + len(h_[5]) + 3 for v in views for h_ in v['holes']] or [0])
    if 760 - chart_x - 16 < 132 + longest * 5.6:
        chart_x = None  # chart goes below
    body = []

    def P(ox, oy, h, x, y):
        return ox + x * s, oy + (h - y) * s

    for v, (ox, oy) in zip(views, pos):
        h = v['h']
        # outline path
        d = ''
        for seg in v['outline']:
            if seg[0] == 'M' or seg[0] == 'L':
                X, Y = P(ox, oy, h, seg[1], seg[2])
                d += f"{seg[0]}{fmt(X)} {fmt(Y)}"
            elif seg[0] == 'A':
                r, large, sweep, x2, y2 = seg[1:]
                X, Y = P(ox, oy, h, x2, y2)
                d += f"A{fmt(r * s)} {fmt(r * s)} 0 {large} {sweep} {fmt(X)} {fmt(Y)}"
            else:
                d += 'Z'
        sv.add(f"<g data-claude-anchor='{part['slug']}-{sv.tid('view')}'>")
        sv.add(f"<path d='{d}' fill='@acc' fillOpacity='0.10' stroke='@acc' strokeWidth='1.5'/>")
        for (x0, y0, x1, y1, lab) in v.get('rects', []):
            X0, Y1 = P(ox, oy, h, x0, y0)
            X1, Y0 = P(ox, oy, h, x1, y1)
            dash = '' if v.get('solidrects') else " strokeDasharray='4 3'"
            sv.add(f"<rect x='{fmt(X0)}' y='{fmt(Y0)}' width='{fmt(X1 - X0)}' height='{fmt(Y1 - Y0)}' fill='none' stroke='@{'acc' if v.get('solidrects') else 'hid'}' strokeWidth='1.25'{dash}/>")
        for (x0, y0, x1, y1) in v.get('hidden', []):
            X0, Y0 = P(ox, oy, h, x0, y0)
            X1, Y1 = P(ox, oy, h, x1, y1)
            sv.add(f"<path d='M{fmt(X0)} {fmt(Y0)}L{fmt(X1)} {fmt(Y1)}' stroke='@hid' strokeWidth='1' strokeDasharray='4 3' fill='none'/>")
        if v.get('axis'):
            X, Y = P(ox, oy, h, *v['axis'])
            sv.add(f"<path d='M{fmt(X - 14)} {fmt(Y)}H{fmt(X + 14)}M{fmt(X)} {fmt(Y - 14)}V{fmt(Y + 14)}' stroke='@edge' strokeWidth='0.75' strokeDasharray='6 2 2 2' fill='none'/>")
        for (hid_, x, y, dia, size, depth, kind) in v['holes']:
            X, Y = P(ox, oy, h, x, y)
            r = dia * s / 2
            col = 'hid' if kind == 'pocket' else 'acc'
            dash = " strokeDasharray='4 3'" if kind in ('pocket',) else ''
            sv.add(f"<circle cx='{fmt(X)}' cy='{fmt(Y)}' r='{fmt(r)}' fill='none' stroke='@{col}' strokeWidth='1.25'{dash}/>")
            if kind == 'tap':
                rr = r * 1.18
                sv.add(f"<path d='M{fmt(X + rr)} {fmt(Y)}A{fmt(rr)} {fmt(rr)} 0 1 1 {fmt(X)} {fmt(Y - rr)}' fill='none' stroke='@acc' strokeWidth='0.75'/>")
            if kind == 'cb':
                sv.add(f"<circle cx='{fmt(X)}' cy='{fmt(Y)}' r='{fmt(6.5 * s / 2)}' fill='none' stroke='@acc' strokeWidth='0.75'/>")
            sv.add(f"<path d='M{fmt(X - 3)} {fmt(Y)}H{fmt(X + 3)}M{fmt(X)} {fmt(Y - 3)}V{fmt(Y + 3)}' stroke='@edge' strokeWidth='0.6' fill='none'/>")
        sv.add('</g>')
        # hole labels (outside the group so they are editable words)
        for (hid_, x, y, dia, size, depth, kind) in v['holes']:
            X, Y = P(ox, oy, h, x, y)
            r = dia * s / 2
            sv.text(X + r * 0.75 + 2, Y - r * 0.75 - 2, hid_, f"lbl-{part['slug']}-{hid_}", size=10.5, weight='600')
        for (x0, y0, x1, y1, lab) in v.get('rects', []):
            X1, Y0 = P(ox, oy, h, x1, y1)
            if not v.get('solidrects'):
                sv.text(X1 + 3, Y0 + 9, lab, f"lbl-{part['slug']}-{lab}", size=10.5, weight='600', color='hid')
        # view name
        sv.text(ox, oy - (12 if v['w'] * s >= 150 else 26), v['name'], f"view-{part['slug']}-{v['name']}", size=12, weight='600')
        # ordinate dims along bottom (x) and left (y)
        by = oy + h * s
        xs = sorted(set(v.get('xs', [])))
        lastX, row = -99, 0
        for xv in xs:
            X = ox + xv * s
            row = (row + 1) % 2 if X - lastX < 13 else 0
            lastX = X
            L = 8 + row * 26
            sv.add(f"<path d='M{fmt(X)} {fmt(by + 2)}V{fmt(by + L + 2)}' stroke='@edge' strokeWidth='0.75' fill='none'/>")
            sv.text(X + 3.5, by + L + 4, fmt(xv), f"ox-{part['slug']}-{v['name']}-{fmt(xv)}", size=10, color='quiet', anchor='end', rot=True)
        ys = sorted(set(v.get('ys', [])))
        lastY, row = 1e9, 0
        for yv in ys:
            Y = oy + (h - yv) * s
            row = (row + 1) % 2 if lastY - Y < 11 else 0
            lastY = Y
            L = 8 + row * 30
            sv.add(f"<path d='M{fmt(ox - 2)} {fmt(Y)}H{fmt(ox - L - 2)}' stroke='@edge' strokeWidth='0.75' fill='none'/>")
            sv.text(ox - L - 4, Y + 3.5, fmt(yv), f"oy-{part['slug']}-{v['name']}-{fmt(yv)}", size=10, color='quiet', anchor='end')
        # overall size label
        if v['w'] * s >= 150:
            sv.text(ox + v['w'] * s, oy - 12, f"{fmt(v['w'])} × {fmt(v['h'])}", f"size-{part['slug']}-{v['name']}", size=10.5, color='quiet', anchor='end')
        else:
            sv.text(ox, oy - 0.5 * 12 + 4, f"{fmt(v['w'])} × {fmt(v['h'])}", f"size-{part['slug']}-{v['name']}", size=10.5, color='quiet')
        # origin marker
        sv.add(f"<circle cx='{fmt(ox)}' cy='{fmt(by)}' r='3' fill='@ink'/>")

    bottom = max(oy + v['h'] * s for v, (ox, oy) in zip(views, pos)) + 52
    # hole chart
    rows = [(h_[0], h_[1], h_[2], h_[4], h_[5], v['name']) for v in views for h_ in v['holes']]
    if chart_x is None:
        cx, cy = 24, bottom + 14
    else:
        cx, cy = chart_x, top + 4
    if rows:
        sv.text(cx, cy, 'Hole chart (mm from 0,0 of its view)', f"chart-{part['slug']}", size=12, weight='600')
        cy += 20
        cols = [0, 34, 76, 118] if chart_x else [0, 40, 100, 160]
        hdr = ['ID', 'x', 'y', 'Size · depth']
        for c_, t in zip(cols, hdr):
            sv.text(cx + c_, cy, t, f"hdr-{part['slug']}-{t}", size=10.5, color='quiet', weight='600')
        sv.add(f"<path d='M{fmt(cx)} {fmt(cy + 5)}H{fmt(cx + (250 if chart_x else 700))}' stroke='@edge' strokeWidth='0.75'/>")
        cy += 18
        for (i_, x, y, size, depth, vn) in rows:
            vals = [i_, fmt(x), fmt(y), f"{size} · {depth}"]
            for c_, t in zip(cols, vals):
                sv.text(cx + c_, cy, t, f"r-{part['slug']}-{i_}-{c_}", size=10.5)
            cy += 16
        if chart_x:
            bottom = max(bottom, cy + 10)
        else:
            bottom = cy + 10
    # notes
    ny = bottom + 8
    for k, n in enumerate(part['notes']):
        sv.text(24, ny, n, f"note-{part['slug']}-{k}", size=11, color='ink' if k == 0 else 'ink')
        ny += 17
    sv.text(24, ny + 4, 'Dots mark 0,0. Ordinates are mm from 0,0. Arc over a hole = tapped; double circle = counterbore; dashed = pocket or hidden.', f"key-{part['slug']}", size=10.5, color='quiet')
    H = ny + 22
    head = [f"<text data-claude-text-id='title' x='24' y='30' fontSize='15' fontWeight='600' fill='@ink'>{part['title']}</text>",
            f"<text data-claude-text-id='subtitle' x='24' y='50' fontSize='11' fill='@quiet'>{part['sub']}</text>"]
    inner = ''.join(head + sv.parts)
    return inner, int(math.ceil(H))


def jsx(part):
    inner, H = build(part)
    code = inner
    for k, v in TOK.items():
        code = code.replace(f"'@{k}'", f"'{v}'")
    svg = f"<svg viewBox='0 0 760 {H}' role='img' aria-label='{part['title']}' fontSize='11'>{code}</svg>"
    return 'export default () => ' + svg + ';'


def plain(part):
    inner, H = build(part)
    for k, v in HEX.items():
        inner = inner.replace(f"'@{k}'", f"'{v}'")
    conv = {'fillOpacity': 'fill-opacity', 'strokeWidth': 'stroke-width', 'strokeDasharray': 'stroke-dasharray',
            'textAnchor': 'text-anchor', 'fontSize': 'font-size', 'fontWeight': 'font-weight'}
    for a, b in conv.items():
        inner = inner.replace(a + '=', b + '=')
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 {H}' width='1520' height='{2 * H}' "
            f"font-family='Helvetica, Arial, sans-serif'><rect width='760' height='{H}' fill='white'/>{inner}</svg>")


if __name__ == '__main__':
    out = sys.argv[1]
    import os
    os.makedirs(out, exist_ok=True)
    meta = []
    for p in PARTS:
        open(f"{out}/{p['slug']}.jsx", 'w').write(jsx(p))
        open(f"{out}/{p['slug']}.svg", 'w').write(plain(p))
        meta.append(p['slug'])
    json.dump(PARTS, open(f'{out}/parts.json', 'w'), ensure_ascii=False, indent=1)
    print(meta)
