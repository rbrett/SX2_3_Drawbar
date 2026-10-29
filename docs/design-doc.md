# SX2.3 Power Drawbar – Design

Oct 26, 2026 · @Russell Brett

A floating-yoke pneumatic drawbar for TTS tooling on the SX2.3 R8 spindle. A Belleville stack clamps the collet; an air cylinder driving a 9.5° wedge (6:1) releases it through a closed force loop, so the spindle bearings carry no release load. The wedge was chosen over a 6:1 lever, which is kept in Appendix B for reference.

## Design basis

The design is fixed by six requirements and the measured machine data below. Measurements are from the 25–26 Oct measurement sheet; "pending" items wait on the new 3/4" collet.

**Requirements**

1. Zero release load through the spindle bearings, quill, rack or pinion: the release force closes inside a spindle–collet–drawbar–actuator loop.
2. Clamp TTS holders (19.00 mm shanks) with a Belleville stack; target preload 6.7–8.9 kN (1,500–2,000 lbf), Hoss's guidance for TTS on small mills.
3. Release by pushing the drawbar down only; no rotation.
4. Release reliably with the regulator at 5.0 bar. Supply is 90 psi (6.2 bar) at 9 CFM, so this allows for line drop and the compressor sitting near cut-in.
5. No contact with the spindle while it turns; release blocked unless the spindle is stopped.
6. Removable, so the machine can revert to a manual drawbar.

**Machine data**

| Item | Value | Status |
| --- | --- | --- |
| Spindle taper | R8 | Measured |
| Collet | 3/4" TTS-style R8, 7/16-20 UNF | On order |
| TTS shank diameter | 19.00 mm, genuine and copies | Measured |
| Spindle top | 6-spline, 21.9 mm over crests, no thread | Measured |
| Spindle bore at top | 13.1 mm | Measured |
| Spindle stick-up above pulley | 64 mm | Measured |
| Pulley | 64 mm OD, 22 mm tall, splined to spindle | Measured |
| Drawbar seat | Spindle end face | Measured |
| Quill | Locked fully up under CNC; Z moves the head | Confirmed |
| Head top | 255 × 115 mm; spindle 60 mm from front, centred | Measured |
| Mounting | Tapped holes in head sides, top 20 mm band clear | Proposed |
| Headroom | Over 1,000 mm | Measured |
| Existing drawbar | 7/16-20 UNF, 250 mm rod + 15 mm head, 11.5 mm body | Measured |
| Collet stick-out (sample) | 3.8 mm proud of spindle nose, clamped | Measured |
| Holder flange to spindle nose | 2 mm gap | Measured |
| Release stroke | — | Pending |
| Holder counterbore depth | 2.0 mm rebate in holder face | Measured |
| Air supply | 90PSI air is available at up to 9CFM. | Confirmed |

## Concept layout

The yoke hooks under the spindle cap and pushes the drawbar down through the wedge, so the cylinder's reaction never leaves the yoke–cap–spindle–drawbar loop.

&#91;embedded content: wedge actuator · side view, draft\]

At rest the fork and the anvil both sit clear by their running gaps, so nothing touches the turning spindle. One float spring and guide pin is drawn; there is one on each side of the head.

## Force path

At every phase the net axial force on the spindle is zero, so the bearings see no release load. W is the washer preload, F the actuator squeeze force (yoke pulls the cap up by F, wedge pushes the drawbar down by F), P the force to push the collet out of the taper. This is a free-body analysis of the concept, not a measured result.

| Phase | Condition | Cap shoulder on spindle face | Collet pull on taper | Spindle clamp load | Net on spindle |
| --- | --- | --- | --- | --- | --- |
| 0. Running | F = 0, gaps open | W down | W up | 0 | 0 |
| 1. Squeeze | 0 < F < W | W − F down | W − F up | 0 | 0 |
| 2. Release | F = W | 0 | 0 | 0 | 0 |
| 3. Push-out | F > W, collet moving | 0 | P down (friction) | P up | 0 |
| 4. Hard stop | Wedge on its stop | 0 | P down | P up | 0 |

Three consequences drive the detail design:

- **The cap clamp only ever carries P**, the collet push-out force, never W. P is small for a non-locking R8 taper; the "taper break effort" test on the measurement sheet gives a first feel for it.
- **A hard stop on the yoke ends the stroke.** Any cylinder force beyond what the stroke needs goes into the stop, inside the yoke. It never reaches the drawbar, the cap clamp or the washers. The same stop caps washer deflection at its allowable limit.
- **The yoke floats.** It rests on stop collars on guide pins fixed to the head sides, and lifts off them by the hook gap when it actuates, so the cylinder reaction stays in the yoke. The head carries only the yoke's weight and the hold-down spring force; the spindle carries nothing.

The principle follows Hoss's floating drawbar (PDB v2 / PDB3) and Shane Wighton's X2 design, which pulls against a flange on the spindle with a running gap.

## Components

Eight parts make up the drawbar; dimensions here are preliminary and get fixed once the release stroke and washer choice are known.

| Component | Design | Still to fix |
| --- | --- | --- |
| Spindle cap | Two-piece clamp collar, 52 mm OD, bore a slip fit on the 21.9 mm spline crests. Internal shoulder seats on the spindle end face and centres the drawbar; the washers sit on its top face. Clamp of 3 × M8 per side grips the spline crests. External flange for the yoke hook. Sits at least 5 mm clear of the pulley. | Length, flange size, clamp holding vs P |
| Drawbar | 4140 high-tensile. 7/16-20 UNF to the collet; body under 13.1 mm through the spindle; 11.0 mm body; 11.2 mm guide section through the cap shoulder and washer stack; 7/16-20 top thread; heavy preload nut plus jam nut; hardened push pad on top. | Overall length, collet thread engagement |
| Washer stack | 8 × genuine Tormach 31319, singly in series, guided on the drawbar, hardened thrust washers at each end. Preload set by measured stack height, cross-checked against Tormach's two turns past hand-tight. | Fixed at 8; if the stroke is too long, fit a genuine Tormach collet |
| Housing (yoke) | Housing straddling the cap. Forked lower plate hooks under the cap flange with a 0.5–1 mm running gap. Side plates carry the roof block, rollers, wedge and cylinder mount plate. A hard stop on the wedge ends the stroke. | Plate sizes, stop position |
| Wedge and rollers | A 9.5° hardened 4140 wedge, pushed rearward by the cylinder, runs between two pairs of Ø14 × 36 hardened rollers: the upper pair under the roof wear plate, the lower pair on the anvil, which presses the push pad. Springs hold the anvil 1 mm clear at rest. | Ratio 6:1, fixed by the wedge angle |
| Cylinder | SDA 80 × 25 compact cylinder (Airtac pattern, already owned; the SDA 80 × 30 bought from AliExpress is now a spare), double-acting, rubber bumpers. Front face bolted to the housing mount plate; a floating joint couples the rod to the wedge. | Body 94.07 mm square × 66.1 mm, measured; mounting and rod-end threads: see Cylinder |
| Mounts | A 10 mm base plate on the head top, fixed with 4 × M6 into new holes tapped through the 9 mm casting top and located by 2 × Ø6 dowels; it carries two guide pins, so the head side walls need no new holes. Vertical guide pins; the yoke slides on bronze bushes and rests on adjustable stop collars that set the hook gap; light springs hold it down against Z-axis decelerations. | Hole positions, spring rate |
| Controls | 5/2 solenoid valve, 24 VDC, with meter-out flow controls to stop the cylinder slamming. Filter-regulator. Release button on the front faceplate, wired through the casting. Valve enabled only when the CNC controller reports spindle stopped; the same output can later serve an M-code tool-change macro. | Controller signal (24 VDC for the valve comes from the control supply's spare output) |

## Sizing

On the working assumptions below, the SDA 80 × 25 cylinder with the 6:1 wedge and the regulator at 5.0 bar does the job; a 63 mm bore would fall short at that pressure. The numbers firm up once the release stroke and washer datasheet are in.

**Method**

Design release force at the drawbar, where F\_stack(x) is the stack force at deflection x (from the washer datasheet), s\_p the preload deflection, s\_r the release stroke:

```latex
F_d = F_{stack}(s_p + s_r) + P
```

Cylinder force, with mechanical advantage i and efficiency η (0.9 assumed):

```latex
F_{cyl} \ge \frac{F_d}{i\,\eta}
```

Cylinder bore at the design pressure p\_min = 0.50 MPa (5.0 bar regulator setting; supply is 6.2 bar):

```latex
D = \sqrt{\frac{4\,F_{cyl}}{\pi\,p_{min}}}
```

Cylinder stroke, with g the pusher running gap:

```latex
h_{cyl} \ge i\,(s_r + g) + \text{margin}
```

Washer limit, with h0 the free cone height and n washers in series (confirm the allowable fraction on the supplier datasheet):

```latex
s_p + s_r \le 0.75\,h_0\,n
```

**Cylinder output** (theoretical, F = p × A; last two columns apply a 6:1 wedge at η = 0.9)

| Bore (mm) | 5.0 bar (N) | 6.2 bar (N) | At drawbar, 5.0 bar (kN) | At drawbar, 6.2 bar (kN) |
| --- | --- | --- | --- | --- |
| 50 | 982 | 1,217 | 5.3 | 6.6 |
| 63 | 1,559 | 1,933 | 8.4 | 10.4 |
| 80 (SDA 80 × 25) | 2,513 | 3,116 | 13.6 | 16.8 |
| 100 | 3,927 | 4,869 | 21.2 | 26.3 |

**Working example** (illustrative inputs, to be replaced by measured values)

- Preload W = 8.2 kN; stack force at release 11.7 kN (8 Tormach washers at a 1.2 mm stroke, next section); push-out P = 0.5 kN; so F\_d = 12.2 kN.
- At i = 6: F\_cyl = 2.27 kN, so D = 76 mm at 5.0 bar. Next standard bore up is 80 mm: 13.6 kN at the drawbar, 11% margin, and an expected release pressure of about 4.5 bar.
- Stroke: s\_r = 1.2 mm, g = 1 mm, i = 6, so i(s\_r + g) = 13.2 mm, well within the SDA's 25 mm stroke (the hard stop needs 15 mm, and even the washer-flat limit of about 1.9 mm needs only 17.4 mm). With 8 washers the stroke limit is the washers going flat at about 2 mm, not the cylinder.
- At the full 6.2 bar the 80 mm cylinder at 6:1 can deliver about 16.8 kN at the drawbar; everything above F\_d ends in the hard stop. Air use is about 0.8 L of free air per release, negligible against 9 CFM (about 255 L/min).
- Drawbar thread stress at 8.2 kN: 7/16-20 tensile stress area about 76.6 mm² (standard thread tables, from memory), so about 107 MPa, well under the roughly 600 MPa proof stress of grade 8 / 8.8 material.

## Drawbar and washer stack

Eight genuine Tormach 31319 washers, stacked singly in series and guided on the drawbar, give 8.2 kN preload: the same count Tormach fits on its own PCNC power drawbar with an R8 TTS collet. With the 6:1 wedge at 5.0 bar they release strokes up to about 1.2 mm with 10% margin, or about 1.6 mm at 5.5 bar. If the release test needs more, fit a genuine Tormach collet before adding washers.

**Why 30 mm high-load washers, not DIN 2093.** DIN 2093 ties OD to bore at about 2:1, so DIN washers that fit a 7/16" drawbar are 22–25 mm OD and carry only 2–3 kN. Bolt-joint Bellevilles are thicker for their size and carry about five times the load in the same bore. Appendix A lists suppliers.

**Reference washers**

| Washer | OD (mm) | Bore (mm) | t (mm) | Free height (mm) | h0 (mm) | Flat load (kN) | Mass, calculated (g) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Solon 7H89](https://www.solonmfg.com/7h89177), 7/16" size | 30.2 | 11.4 | 2.44 | 3.07 | 0.64 | 15.1 | about 11.7 |
| Tormach 31319 ([measured by viking45](https://de.cncarena.com/forum/user-post-list/330656-viking45/)) | 30.1 | 11.5 | 2.3 | 2.9 | 0.6 | not published | about 11 |

**Release range, 8 washers** (8 × Tormach 31319, 6:1 wedge, P = 0.5 kN; forces assume the Solon 7H89 rate)

| Release stroke (mm) | Release deflection | Release force (kN) | Required incl. P (kN) | Margin at 5.0 bar (13.6 kN) | Margin at 5.5 bar (14.9 kN) |
| --- | --- | --- | --- | --- | --- |
| 0.8 | 0.75 h0 | 10.6 | 11.1 | 23% | 35% |
| 1.0 | 0.79 h0 | 11.2 | 11.7 | 16% | 28% |
| 1.2 | 0.83 h0 | 11.7 | 12.2 | 11% | 22% |
| 1.4 | 0.87 h0 | 12.3 | 12.8 | 6% | 16% |
| 1.6 | 0.91 h0 | 12.9 | 13.4 | 1% | 11% |
| 1.8 | 0.96 h0 | 13.5 | 14.0 | Won't release | 7% |

The table assumes the 31319 behaves like the same-size Solon 7H89 (23.6 kN/mm per washer, so 2.95 kN/mm for the stack), with h0 = 0.6 mm from viking45's measurement; Tormach doesn't publish a load rating. Preload sits at 0.35 mm per washer (0.58 h0), the stack is 23.2 mm free and 20.4 mm preloaded, and the washers go flat after about 2.0 mm of stroke. Set the hard stop at s\_r + 0.3 mm and never beyond about 1.9 mm. Releasing at 0.8–0.9 h0 is deeper than a longer stack would need, but it is how Tormach runs the same washers: it calls for a monthly crack check, immediate replacement of damaged washers, and anti-seize between washers every 5,000 cycles or six months. Keep a spare set. The first release test at stepped pressure measures the real force.

**Rotating mass and imbalance** (my estimates; worst case assumes every washer sits to one side of its guide clearance)

|  | DIN A50 stack (rejected) | 8 × Tormach 31319 |
| --- | --- | --- |
| Stack mass | about 520 g | about 88 g |
| Guide | Cap bore, 0.6 mm diametral clearance | Drawbar, about 0.2 mm |
| Worst-case unbalance | about 156 g·mm | about 9 g·mm |
| Rotating force at 2,500 rpm | about 11 N | about 0.6 N |

For scale, ISO 21940-11 grade G2.5, typical for machine-tool spindles (from memory), allows about 30 g·mm for a 3 kg rotor at 2,500 rpm. Rotating force grows with speed squared.

**Axial stack-up above the spindle end face** (8 washers, preloaded, at rest; nut heights from standard tables, from memory)

| Item | Height (mm) | Top above spindle end face (mm) |
| --- | --- | --- |
| Cap shoulder | 6.0 | 6.0 |
| Base thrust washer, hardened, 32 OD | 3.0 | 9.0 |
| Washer stack, 8 preloaded | 20.4 | 29.4 |
| Top thrust washer, hardened, 32 OD | 4.0 | 33.4 |
| Preload nut, 7/16-20 heavy hex | 10.7 | 44.1 |
| Jam nut | 6.4 | 50.5 |
| Top thread: 5 free, 6 under the pad | 10.9 | 61.4 (thread end) |
| Push pad, 8 mm (6 mm on the thread) | 2.0 above the thread end | 63.4 |

**Spindle cap** (now a clamped collar; the washers sit on top of it)

| Feature | Dimension |
| --- | --- |
| Material | 4140 pre-hardened |
| Spline bore | 22.0 mm, slip fit on the 21.9 mm crests |
| Clamp skirt | 54 mm below the spindle end face, leaving 10 mm clear of the pulley |
| Clamp | Two-piece, 3 × M8 12.9 per side at 32 Nm (see Spindle collar detail) |
| Shoulder | 6 mm thick; 11.3 mm hole, a close fit on the drawbar guide so it centres the drawbar in the 13.1 mm spindle bore |
| Washer seat | Top face of the shoulder, 32 mm diameter, flat and smooth |
| OD | 52 mm |
| Hook flange | 64 mm OD × 6 mm, level with the shoulder |
| Overall height | 60 mm |
| Shroud | Optional light sleeve to keep chips and coolant off the stack; not load-bearing |

**Drawbar**

| Feature | Dimension |
| --- | --- |
| Material | 4140 condition T (about 270–300 HB), turned from 16 mm bar |
| Lower thread | 7/16-20 UNF; length = collet thread depth + 3 mm (row 3.7, pending) |
| Body | 11.0 mm (down from the old 11.5 so it passes the collar's 11.3 centring hole), through the 13.1 mm spindle bore |
| Guide section | 11.2 mm through the cap shoulder and washer stack, about 0.2 mm clearance in the 11.4 mm washer bore; harden if practical (DIN guidance for guide surfaces is at least 55 HRC) |
| Tip to spindle end face | About 250 mm, from the existing drawbar; confirm with the new collet (row 3.5) |
| Top thread | 7/16-20 UNF, about 28 mm, for nut, jam nut and adjustment |
| Above spindle end face | About 61.4 mm to the thread end; push pad top at 63.4 mm |
| Overall length | About 311 mm |
| Push pad | Hardened, screwed on and thread-locked |
| Tension at preload | 8.2 kN on about 76.6 mm² stress area, about 107 MPa |

Set preload by stack height, not torque. Measure the free height of your washers first (viking45 measured 2.9 mm), then tighten the nut until the stack between the thrust washers is 8 × (free height − 0.35 mm): about 20.4 mm. Lock it with the jam nut. As a cross-check, that is about 2.8 mm of compression, about 2.2 turns of the 7/16-20 thread past hand-tight, close to Tormach's "hand tight plus two turns". Re-check after two weeks: a stack loses about 5% of its force in the first two weeks ([Surisa](https://www.surisa.es/en/collections/disc-springs-din-2093)).

## Spindle collar detail

A two-piece clamp collar with a 54 mm skirt and 3 × M8 12.9 per side is estimated to hold about 14 kN axially. With the regulator at 5.0 bar and the 6:1 wedge, the worst case of a stuck collet loads it to about 5.4 kN, a margin of about 2.6. The holding figure is an estimate, so a witness line still checks it in service, and a positive groove is the fallback if the spindle can be machined.

**Worst-case load** (stuck collet)

If the collet sticks in the taper, the drawbar cannot move. The stack stays at its 8.2 kN preload while the cylinder pushes the drawbar down and the yoke pulls the collar up. The collar clamp carries the difference until the button is released.

| Regulator setting | Drawbar force, 80 mm at 6:1 (kN) | Collar load (kN) |
| --- | --- | --- |
| 6.2 bar (full supply) | 16.8 | 8.6 |
| 5.5 bar | 14.9 | 6.7 |
| 5.0 bar (setting) | 13.6 | 5.4 |

Normal duty is only P, the push-out force of a released R8 collet, which should be well under 1 kN because the 16°51′ taper is not self-locking. 5.0 bar is still about 0.5 bar above the expected 4.5 bar release pressure (8 washers, 1.2 mm stroke).

**Clamp options compared** (my estimates)

Axial holding ≈ 0.25 × 2π × μ × T, where T is the screw tension across one cut, μ = 0.15 dry steel, and 0.25 is a conservative allowance for a stiff ring gripping spline crests only. In this thin-ring model, holding rises with screw tension per cut, not with the number of cuts or the contact length. Screw tension uses T ≈ 0.2 × F × d.

| Option | Screws | Tension per cut (kN) | Holding (kN) | Margin at 5.0 bar | OD (mm) |
| --- | --- | --- | --- | --- | --- |
| One-piece, 25 mm skirt (previous) | 2 × M6 at 16 Nm | 26 | about 6 | 1.1 | 42 |
| Two-piece, 40 mm skirt | 3 × M6 per side at 16 Nm | 40 | about 9.4 | 1.7 | 44 |
| **Two-piece, 54 mm skirt (recommended)** | **3 × M8 per side at 32 Nm** | **60** | **about 14** | **2.6** | **52** |

The two-piece form also clamps more evenly than a single-slit ring, is self-balancing, and its centring hole stays put when the screws are tightened. M8 12.9 at 32 Nm is about 20 kN per screw, roughly 56% of its proof load of about 35 kN (from memory).

**Recommended collar**

| Feature | Dimension and notes |
| --- | --- |
| Type | Two-piece clamp collar, split on a diameter through skirt, shoulder and flange |
| Material | 4140 condition T (about 270–300 HB) |
| Spline bore | 22.0 mm, finished with the halves shimmed apart (below) so they close onto the 21.9 mm crests |
| Shoulder | 6 mm thick; underside flat and square to the bore, seats on the spindle end face |
| Centring hole | 11.3 +0.02/0 mm through the shoulder, close fit on the 11.2 mm drawbar guide |
| Washer seat | Top face of the shoulder, 32 mm diameter, flat, smooth and square to the bore |
| Clamp skirt | 54 mm below the shoulder; leaves 10 mm clear of the pulley (64 mm stick-up). Lengthened from 40 mm so the top screw heads clear the fork plate |
| OD | 52 mm |
| Clamp screws | 3 × M8 × 25 socket head, grade 12.9, per side, on axes 17 mm from the bore axis, at 20, 32 and 44 mm below the shoulder; heads on alternate halves row by row. The heads stand out to about Ø60, inside the Ø64 flange; 32 Nm, tightened evenly so both joint gaps stay equal |
| Hook flange | 64 mm OD × 6 mm, level with the shoulder; underside flat, carries the yoke hook |
| Clamp surfaces | Bore as turned, not polished; degrease bore and spline crests before fitting, and keep the MoS₂ from the washer stack off them |
| Mass | About 0.85 kg (calculated) |

&#91;embedded content: collar machining drawing · half section, outside view, plan\]

**Making it**

1. Turn the blank: OD, flange, and rough bores about 1 mm undersize.
2. Drill and tap the six M8 holes and counterbore the heads, then split on the diameter with a slitting saw (about 1.5 mm kerf).
3. Reassemble the halves with 0.2 mm shims in both joints and torque the screws.
4. In one setting, finish-bore 22.0 mm and the 11.3 mm centring hole, and face the shoulder underside and washer seat.
5. Remove the shims for fitting, so each joint can close 0.2 mm onto the spline.

**Checks and fallback**

- Scribe a witness line across collar and spindle; check it at commissioning, after any stuck-collet event, and monthly.
- Release the button at once if the tool does not drop; holding the button on a stuck collet is the only way to load the collar this hard.
- Fallback if the collar ever moves: if the spline is soft enough to file, cut a 1 mm deep groove across the crests about 15 mm below the end face (spindle out, in the lathe), and add a matching internal rib to the collar halves. That makes the axial hold positive instead of frictional.

## Drawbar detail

The drawbar is four turned sections from one piece of 16 mm 4140 bar, about 311 mm long with the 8-washer stack. Two lengths stay open until the new collet arrives: L1, the lower thread length, and H, the tip-to-spindle-face length.

| Section, from the collet end | Diameter | Length | Notes |
| --- | --- | --- | --- |
| A. Lower thread | 7/16-20 UNF-2A | L1 = collet thread depth + 3 mm (row 3.7, pending) | 45° chamfer on the tip; 1.5 mm thread relief at the runout |
| B. Body | 11.0 ±0.1 mm | H − L1 − 3 mm (about 225 mm; H about 250 mm, row 3.5, pending) | Under the collar's 11.3 centring hole, so the bar and stack lift out with the collar still clamped; runs in the 13.1 mm spindle bore |
| C. Guide | 11.2 −0.02/−0.05 mm | From 3 mm below the spindle end face to 33.4 mm above it: about 36 mm | Fine-turned or ground; nitride or harden if practical. Runs through the collar centring hole and the washer bores (about 0.2 mm clearance in the 11.4 mm washer bore) |
| D. Top thread | 7/16-20 UNF-2A | 28 mm | Preload nut, jam nut, about 5 mm adjustment, push pad |
| Push pad | 16 mm × 8 mm | 6 mm on the thread, top about 63.4 mm above the spindle end face | 4140 from the Ø16 drawbar offcut, hardened with the wedge and anvil; tapped 7/16-20 blind; flat top; thread-locked |

&#91;embedded content: drawbar machining drawing · whole bar, top-end and collet-end details, push pad\]

**Manufacturing notes**

- Turn between centres so the guide section and both threads stay concentric; aim for 0.02 mm runout or better on the guide (my judgement).
- Single-point the threads to class 2A and check them with a 7/16-20 nut and the new collet before parting off.
- Put a small undercut at each diameter step rather than a sharp corner; the body-to-guide step sits in the spindle bore, not under load.
- Overall length = H + 33.4 + 28 mm, about 311 mm for H = 250 mm and 8 washers.

## Wedge actuator

A 9.5° wedge between caged rollers gives 6:1 in a housing whose top is about Z 152, about 4.9 kg with the cylinder (my estimate). The price is precision work: a hardened, ground wedge, anvil and wear plate. The side view under Concept layout shows it assembled; the exploded view below shows every part.

**How it works.** The cylinder lies horizontal in front of the spindle and pushes a wedge rearward between two pairs of rollers. The upper rollers run under a hardened roof plate; the lower rollers run on the anvil, whose top is cut at the same 9.5° so the faces stay parallel. As the wedge advances, the anvil is driven down onto the push pad. The roof's reaction goes up through the housing side plates to the fork under the collar flange: the closed force loop described under Force path. The cylinder mount reacts the wedge's horizontal load, and a rear thrust bar reacts the anvil's (about 2.8 kN, pushing the anvil rearward).

**Orientation (decided 28 Oct 2026).** The cylinder faces forward, sitting in front of the spindle above the head, and the wedge travels toward the rear. That keeps the space behind the spindle, over the motor pulley, clear for a possible motor-shaft encoder later. The four belt-cover posts come off and the housing base takes the belt cover's place. The drawings are unchanged: the side view is seen from the machine's left, so the front is to the right. Ports face the machine's left (decided 29 Oct 2026), toward the viewer in the side view. Ports up would put the PC10-03 fittings above the housing top (port face about Z 149 against a top at about Z 152), and ports down would foul the wedge and roof block.

&#91;embedded content: wedge design · exploded view, balloons match List B\]

**Design**

| Feature | Value | Notes |
| --- | --- | --- |
| Wedge angle | 9.5° on the underside, top flat | tan 9.5° ≈ 1/6, so 6:1 |
| Wedge travel | 13 mm for a 1.2 mm stroke + 1 mm gap | The 25 mm cylinder stroke is not the limit; 8 washers go flat at about 2 mm |
| Wedge | 4140 (from Ø50 round bar or 25 mm plate), about 80 × 40 mm; 10 mm thick at the leading end, 23.5 mm at the trailing end | Through-hardened to about 50 HRC; top and underside ground |
| Rollers | 4 × Ø14 × 36 mm hardened ground dowel pins (ISO 8734), 2 per face at 18 mm pitch, in two 2 mm brass cages with light centring springs (drawing below) | Free rollers between parallel faces: no axles or bearings to overload |
| Roof | O1 wear plate 60 × 40 × 5 mm, hardened and ground, under a 19 mm 6061-T6 roof block |  |
| Anvil | 4140, 40 × 40 mm, 16.0–22.7 mm tall with the 9.5° top; bottom flat on the push pad; through-hardened to about 50 HRC and ground | The 9.5° faces push the anvil the way the wedge travels (rearward), so its rear face bears on a bronze-faced rear thrust bar; two sprung Ø5 lift pins hold it 1 mm up at rest |
| Housing | Two 12 mm 6061-T6 side plates 130 × 189, 42 mm apart inside (set by the roof block), each with a window for the fork plate and a notch round the collar; roof block, cylinder mount plate | The side plates also carry the fork plate and the float lugs |
| Cylinder | SDA 80 × 25, horizontal with its axis at Z 102, level with the wedge's M14 hole, front face bolted to the mount plate with M12 screws into its front threads, or M10 through-bolts the full length of the body | Pushes on the full bore; M14 × 1.5 floating joint (SMC JA40-14-150) between the rod and the wedge (List B row 13) |
| Hard stop | Screw in the housing at the wedge's leading end | Sets maximum travel |
| Height | About Z 152 | The lever alternative (Appendix B) reaches about Z 275 |

**Load check** (my calculations; full 6.2 bar supply, 5.0 bar setting in brackets)

| Item | Load | Section | Stress | Verdict |
| --- | --- | --- | --- | --- |
| Roller line contact | 16.8 (13.6) kN per face, 2 rollers | Ø14 × 36 mm each | about 1,110 (1,000) MPa Hertz peak | OK in hardened 4140 in every case, including one roller taking the whole load (see the material note below) |
| Anvil on push pad | 16.8 kN | Flat on the 16 mm pad, 201 mm² | 84 MPa | Far easier than the lever's line contact |
| Anvil horizontal thrust | 2.8 (2.3) kN | Bronze wear strip | Low | Friction about 0.3 kN, within the 0.9 efficiency |
| Roof block | 168 N·m over a 40 mm span | 19 × 60 mm 6061-T6 | 47 MPa (6061-T6 yields at about 240) | OK |
| Side plates | 16.8 kN tension, shared | 2 × 12 × 80 mm 6061 | 9 MPa | OK |
| Cylinder mount | 3.1 kN | 4 screws in the front face | Low | OK |
| Fork plate tines | 16.8 kN, 8.4 kN per tine | 19 × 16 mm mild steel, 54 mm span between the feet | 96 MPa bending | OK; 10 mm thick would be about 168 MPa |
| Flange on the fork | 16.8 kN | About 230 mm² where the tines overlap the flange | About 73 MPa | OK |
| Side-plate feet | 4.2 kN per foot | 12 × 20 mm 6061, 20 mm cantilever | About 53 MPa | OK |

The wedge back-drives: 9.5° is steeper than the friction angle even for sliding steel (about 5.7°), so it can't jam, and the cylinder pulls it back on retract.

**Points to watch**

- **Load sharing.** Grind the wedge, anvil and roof faces flat and parallel to about 0.01 mm (my judgement), across the 40 mm width as well as along the length. If one roller of a pair carries everything, its contact stress rises to about 1,560 MPa.
- **Cage creep.** Free rollers travel at half the wedge speed and can walk over many cycles. Centre the cage with two light springs and check it after run-in.
- **Grinding.** The wedge, anvil and roof plate need a surface grinder after hardening, or can be sent out.
- **Ratio.** It is fixed by the wedge angle. Changing it means a new wedge and anvil, whereas the lever's slotted pivot adjusts from 5:1 to 6:1.

&#91;embedded content: wedge and anvil machining drawing\]

&#91;embedded content: roof block, wear plate and roller cage drawing\]

&#91;embedded content: small parts drawing · push pad, thrust washers, rear thrust bar, stop block, cylinder mount plate\]

The push pad comes from the Ø16 4140 drawbar offcut and the thrust washers from the Ø50 4140 bar; all three are hardened with the wedge and anvil (decided 29 Oct 2026: no Ø35 silver steel needed). The mount plate's Ø40 bore clears the rod, its boss and the JA joint.

&#91;embedded content: base plate and float guides · plan of the head-top plate, one guide in elevation\]

The housing rests on two Ø12 guide pins standing on a base plate that replaces the belt cover. The rest collars set the fork-to-flange gap; the springs above the lugs (about 24 N each, roughly half the housing weight) keep it down during Z moves. Those springs push on the spindle only during release, when the housing lifts the gap off the collars.

&#91;embedded content: side plates and fork plate · elevation of one plate with all holes, fork plate plan\]

The fork slides in sideways through a window in both side plates and sits on the plates' feet, so the release reaction goes into the aluminium in bearing rather than through screws in tension. A notch up the middle of each plate clears the collar and its clamp screws. The fork is 16 mm thick, not the 10 mm first listed: at 10 mm the tines would have reached about 168 MPa in bending at the worst-case 16.8 kN, too close to mild steel's yield.

**Housing details fixed by these parts.**

- **Cylinder axis at Z 102**, level with the wedge's M14 hole. That brings the housing top down to about Z 152.
- **Rear thrust bar** between the side plates (6061-T6 10 × 30 × 42, faced with the bronze strip) takes the anvil's 2.8 kN horizontal load. The 9.5° faces push the anvil the way the wedge travels (rearward), so the bar sits behind the anvil.
- **Anvil lift:** two Ø5 m6 × 10 dowel pins (ISO 8734) pressed into the anvil's sides (silver steel is ground under nominal, so it would be loose in an H7 hole) run in slots 7 wide × 9 tall in the side plates. A light spring in a Ø6 pocket under each pin holds the anvil 1 mm clear of the push pad at rest.
- **Cage springs** bear on four Ø5 silver-steel cross pins through the side plates at X ±40: Z about 121 for the upper cage, and about 98 (rear) and 84 (front) for the lower cage. Each cage moves half the wedge travel, 7.5 mm at the hard stop, so the springs stay well short of solid.
- **Roof block** is 42 wide and sets the side-plate spacing; each side fixes with 2 × M8 and a Ø6 dowel.
- **Head mounting (decided 29 Oct 2026):** a 12 mm 6061-T6 base plate takes the belt cover's place on the flat head top (Z −93, measured: boss 5 + pulley clearance 24 + spindle 64 above the pulley). It is fixed with 4 × M6 × 20 into new holes tapped through the 9 mm casting top (1.5 × d engagement in iron), and located by 2 × Ø6 dowels reamed with the plate centred on the spindle. The screws only carry the housing's weight (about 4.9 kg, roughly 48 N) plus Z-move inertia, because the release force stays in the closed loop. The rear slot clears the belt: with equal Ø64 pulleys at about 96 centres the belt runs straight at about ±33 from the axis, and the arms stop 45 behind the axis, well ahead of the motor pulley (front edge about 64 behind, more once the belt is tensioned). The whole head top is flat (sheet 9.10). Scrape the paint off under the plate's footprint so it beds on bare iron, which keeps the guide pins square to the head. The existing M4 corner holes are not used. Do not use the four M4 holes in the 90 mm boss: they hold the spindle's top bearing cap, and their original cap screws should go back in once the old sensor's aluminium standoffs come out.
- **Mass (updated 29 Oct 2026, my estimate from part volumes):** the mount plate, base plate, roof block, lugs, thrust bar and stop block are 6061-T6; the fork stays steel because it bears on the hardened collar flange. The floating housing is about 4.9 kg: side plates 1.40, cylinder 1.20, wedge and anvil 0.66, fork 0.40, mount plate 0.28, roof block and wear plate 0.22, JA joint and stud 0.21, rollers 0.17, lugs 0.10, and about 0.3 for the thrust bar, stop block, cages and screws. The base plate, guide pins and collars fixed to the head add about 0.5 kg, and the collar, washers and push pad on the spindle about 0.95 kg. That is about 6.4 kg, roughly 63 N, added to the head, less the belt cover and posts that come off. A Z-axis gas strut needs about 63 N more lift than the head needs today.
- **Z-axis gas strut (sizing; brackets still to design):** it should carry most of the head's weight so the Z stepper is not holding it all, but never lift the head on its own if the Z drive loses power. The drawbar adds about 63 N to what it must carry.
  - **Stroke:** the SX2.3 manual gives 240 mm of headstock travel, so the strut needs at least 250 mm of stroke (check your CNC soft limits). A gas spring is typically about twice its stroke plus 50–80 mm of end fittings long when extended (my recollection; use the maker's table), so expect about 560–600 mm extended and 310–350 mm compressed, between a bracket at the column top and one on the head.
  - **Force:** a gas spring pushes harder as it compresses, typically 1.2–1.4 times its extended force over the stroke (from memory). Mount it so it is longest with the head at the bottom, and choose the extended rating at about 0.7 × the total head weight W. With about 1.3 progression it then balances roughly 70–90% of W over the travel, and the head always tends to settle down.
  - **Measuring W:** with the Z motor coupling undone, hang the head from a luggage scale and read the force just as it starts to rise and just as it starts to fall. The average cancels the slide friction. Do it with the drawbar housing fitted, or add 63 N.
  - **Buying:** order a gas spring with a bleed valve, charged a little above the estimate, then bleed it down on the machine until the head just settles under its own weight at the top of its travel. Mount it rod-down where the brackets allow; that is the usual makers' advice for seal life (from memory).
- **Rear stop block** (6061-T6 10 × 20 × 42) carries the M8 hard-stop screw against the wedge's leading end, set for 15 mm of wedge travel (1.5 mm at the drawbar).
- **Floating joint:** the rod is female M14 × 1.5 (re-measured 29 Oct 2026; first recorded as M12 × 1.75). An M14 × 1.5 stud goes into the rod, the joint's female socket screws onto it, and the joint's male M14 × 1.5 stud screws into the wedge. Part: SMC JA40-14-150, a standard catalogue item rated at 4,400 N maximum tension/compression, 0.75 mm eccentricity and ±5°, 0.16 kg ([SMC JA catalogue](https://static.smc.eu/pdf/JA-A_EU.pdf)). That is 1.4 × the worst-case cylinder thrust of 3.1 kN at an unregulated 6.2 bar, and 1.75 × the 2.51 kN at 5.0 bar. Its overall length (about 60 mm from the catalogue table; I couldn't confirm which dimension that is) must be checked against the rod-to-wedge gap before the cylinder mount plate is drawn. Installation per SMC: screw the socket on until it bottoms, back off 1–2 turns, then lock with thread adhesive. **Wedge hole:** M14 × 1.5, thread 14 deep, 12.5 mm tap drill 18 deep, tapped before hardening. Correction to my earlier 20/26 mm depths: the 9.5° underside closes in on the hole as it goes deeper, and at those depths the wall to the slope would have been only about 1.2–1.4 mm. At 14/18 mm the minimum wall is about 2.4 mm, at the bottom of the hole, rising to 4.75 mm at the end face. Lock the JA stud's nut against the wedge end face, so the push goes through the face and the thread only carries the light retract load. Check that the stud can't bottom in the 14 mm thread; add a washer under the nut if it is longer.

**Material choice (decided 29 Oct 2026).** The wedge and anvil are 4140 rather than O1, because O1 in 40 × 25 section proved hard to source. The rollers only stress a thin surface layer: the contact strip is about 0.24–0.38 mm wide, with the peak shear about 0.10–0.15 mm below the surface. For a roller on a flat, first yield occurs at a peak contact pressure of about 1.79 × the yield strength (von Mises; Johnson, *Contact Mechanics*, 1985, quoted from memory). The three load cases therefore need a yield of about 560 MPa (1,000 MPa contact, 5.0 bar, rollers sharing), 620 MPa (1,110 MPa, 6.2 bar) and 880 MPa (1,574 MPa, one roller taking the load). Atlas lists 4140 bar up to Ø180 as supplied at 740 MPa minimum 0.2% proof (269–331 HB). That is enough when the rollers share, but short of 880 MPa in the one-roller case. Hardened at 850–860 °C, oil quenched and tempered at 175–230 °C, Atlas gives a yield above 1,380 MPa, about 1.6 × the worst case. A 25 mm section won't harden fully in the core, but only the surface layer carries the contact stress. Stock: the wedge section (40 × 23.5, 46.4 mm diagonal) and the anvil (40 × 22.7, 46.0 mm diagonal) both come out of Ø50 round bar, or from 25 mm plate. The wear plate stays O1 ground flat stock, which is easy to buy in thin sections.

**Hardened parts: heat treatment and grinding.** The wedge and anvil (4140) and the wear plate (O1) are rough-machined, hardened, tempered, then ground. The wedge and anvil slopes are ground on the same sine-bar setting so they match.

| Step | Wedge and anvil (4140); wear plate (O1) | Notes |
| --- | --- | --- |
| 1. Rough machine | Saw and mill the wedge and anvil from Ø50 4140 round (or 25 mm plate) and the wear plate from O1 flat stock, leaving about 0.3 mm per face to grind (wedge and anvil slopes, top, underside and sides; both wear plate faces). Drill and tap the wedge's M14 × 1.5 and the wear plate's M3 holes, ream the anvil's Ø5 H7 holes, break all edges, mark each part | Grinding allowance is my judgement; it also removes any decarburised skin |
| 2. Protect | Wrap in stainless heat-treat foil, or coat with anti-scale compound | Limits scale and decarburisation (common practice; not from the datasheets) |
| 3. Preheat | 4140: heat slowly, no separate preheat. O1: 650 °C, equalise | 4140: Atlas datasheet ("heat slowly"). O1: Industeel 1.2510 datasheet; Hudson gives 649–704 °C, heating no faster than 222 °C/h |
| 4. Harden | 4140: 850–860 °C, hold until uniform. O1: 800–815 °C, 30 min after the part reaches temperature | 4140: Atlas 850–860 °C. O1: Hudson 802–816 °C, 30 min per 25 mm; Industeel 780–820 °C |
| 5. Quench | 4140: quench vigorously in oil, agitating the part. O1: warm, agitated quench oil (about 55 °C); take the parts out while still hand-warm (above about 50 °C) | 4140: Atlas (polymer quenchant also acceptable if equivalent). O1: Industeel and Hudson. Both can crack at sharp internal corners, so keep the radii |
| 6. Temper | Immediately, while still warm. 4140: 200 °C for 2 h, air cool; never hold it between 230 and 370 °C. O1: 180–200 °C for 2 h, air cool, then a second temper | 4140: Atlas gives 175–230 °C for ½–2 h for a yield above 1,380 MPa, and says to avoid 230–370 °C (blue brittleness); about 50 HRC is my estimate from typical tempering curves, not from Atlas. O1: Hudson 177–204 °C, 2 h minimum; Industeel calls for a double temper; as-quenched is about 64 HRC (Industeel) and 58–62 HRC after tempering is my reading of typical curves. Check both with a hardness tester or file |
| 7. Grind references | Wedge top; anvil underside; both wear plate faces parallel within 0.005 | These are the faces the slopes are measured from |
| 8. Grind slopes | Reference face down on a sine bar set to 9.5°: gauge stack 16.505 mm on a 100 mm bar, or 0.8252″ on a 5″ bar. Grind the wedge underside, then, without changing the stack, the anvil top | sin 9.5° = 0.16505; ±0.05° is about ±0.09 mm on the 100 mm stack |
| 9. Grind sides | Wedge and anvil to 40 −0.1/−0.2 | 1 mm side clearance to the side plates |
| 10. Check the match | On a surface plate: anvil, two of your matched Ø14 pins, then the wedge. The wedge top must be parallel to the plate within 0.01 mm along and across. If it isn't, regrind the anvil slope | Tests the parts the way they will carry load |

If you'd rather not quench at home, a commercial heat-treater can do steps 3–6: ask for the 4140 parts hardened and tempered at about 200 °C to at least 48 HRC, and the O1 wear plate at 58–62 HRC with a double temper.

**Cutting list for the Edcon bars (ordered 29 Oct 2026).** Saw lengths include facing allowance; allow about 2 mm per bandsaw cut. The Ø50 bar is 150 long, so take the washers off its end on the lathe first, then saw the wedge (82) and the anvil (42); about 8 mm is left over. Check the lengths you ordered against the minimum per bar.

| Bar | Part | Finished size | Saw length (mm) | Minimum bar (mm) |
| --- | --- | --- | --- | --- |
| 4140 Ø16 | Drawbar | about 311 long (H + 61.4; H to confirm with the new collet) | 320 | 340, with the push pad |
| 4140 Ø16 | Push pad | Ø16 × 8 | 12 | (from the same bar) |
| 4140 Ø50 | Wedge | 80 × 40 × 23.5, bar axis along the 80 | 82 | 140 with the anvil and washers (you have 150) |
| 4140 Ø50 | Anvil | 40 × 40 × 22.7, bar axis along one 40 side | 42 | (from the same bar) |
| 4140 Ø50 | 2 thrust washers | Ø32 × 11.3 bore, 3 and 4 thick | 14, turned off the bar end before sawing | (from the same bar; or the Ø65 collar offcut) |
| 4140 Ø65 | Collar | Ø64 flange, 60 high | 66 | 66 |
| W1 Ø5 | 4 cross pins | about 75 each, confirmed when the side plates are drawn | 4 × 80 | 335 (you have 2 m) |
| O1 40 × 5 | Wear plate | 60 × 40 × 5 | 65 | 65 (you have 500) |

**Cutting the 150 mm Ø50 bar, in order.**

| Step | Operation | Uses (mm) | Bar left (mm) |
| --- | --- | --- | --- |
| 1 | Lathe: chuck the bar, face, turn 14 long to Ø32, drill and bore 11.30 +0.05/0, part off the 4.3 washer, face, part off the 3.3 washer | 14 | 136 |
| 2 | Saw the wedge blank | 82 + 2 kerf | 52 |
| 3 | Saw the anvil blank | 42 + 2 kerf | about 8 spare |

Check each saw cut is square before facing: the wedge has 1 mm a side to face, and the anvil about 0.7 mm a side before its sides are milled to 40.6 and ground. If a cut goes wrong, make the washers from the Ø65 offcut left after the collar instead (that bar needs to be at least 80 long), which frees the first 14 mm of the Ø50.

**Machining sequence: wedge and anvil.** Both come out of the Ø50 bar with every face cleaning up (wedge section diagonal 47.2 mm and anvil 46.8 mm, including grinding allowance).

1. Turn the two thrust washers off the end of the Ø50 bar first (see the guidance table), then saw an 82 mm wedge blank and a 42 mm anvil blank. With only 1 mm a side to face, check the saw cuts are square before facing.
2. Wedge: hold the blank in a V-block, mill one flat, turn onto it and mill the opposite face to 24.1 (23.5 plus 0.3 per face to grind). Mill the sides to 40.6, then the ends square to 80.0.
3. Mill the 9.5° underside, leaving 0.3 to grind: as a ramp on the CNC, or with the block on a 9.5° angle plate. The leading end comes out at about 10.7 before grinding.
4. Trailing end: spot on the centreline 12.05 below the as-milled top (11.75 plus the 0.3 top allowance). Drill Ø12.5 to 18 deep and flat-bottom it, then tap M14 × 1.5 to 14 full thread with a bottoming tap.
5. Anvil: square the blank to 40.6 × 23.3 × 40 the same way. Mill the 9.5° top leaving 0.3, then ream the two Ø5 H7 holes 6 deep, 20.3 from the as-milled thrust face and 8.3 above the as-milled underside.
6. Deburr, radius any internal corners, break edges 0.3, and stamp a mark on a non-working face.
7. Heat-treat the wedge, anvil, push pad and both thrust washers together, following the 4140 column of the heat-treat table.
8. Grind as in steps 7–10 of the table, then check the match on the surface plate.
9. Press the two Ø5 m6 × 10 dowels into the anvil, 4 mm proud each side.

**Machining guidance: the other parts.** The 4140 is supplied pre-hardened (Atlas condition U: 269–331 HB), so carbide tooling is the easier choice. The collar and drawbar follow their own detail sections.

| Part | From | Sequence | Watch |
| --- | --- | --- | --- |
| Thrust washers (2) | End of the Ø50 4140 bar, before sawing (14 mm of it) | Chuck the bar; face; turn the OD to 32 for 14 mm; drill and bore 11.30 +0.05/0; part off at 4.3, face, part off at 3.3; face the parted sides; harden with the wedge batch; lap to 4.0 and 3.0 | Faces flat and parallel within 0.01; lap on a plate with figure-of-eight strokes |
| Push pad | Ø16 4140 offcut | Face to 8.0; drill 9.9 (25/64″) to 6.0 and flat-bottom with an end mill; bottoming tap 7/16-20; check on the drawbar; harden | Top face square to the thread within 0.02. Six mm of thread carries the 16.8 kN worst case at about 160 MPa thread shear (my calculation), so the drawbar end touching the floor is not essential |
| Side plates (2) | 12 mm 6061-T6 | Screw the two blanks back to back; machine the outline, window, notch and all through-holes as a pair; separate; mill the lift and spring pockets on each inner face as mirror images; drill the front-edge M6 and the feet Ø6.6 with each plate on edge in the vice | Window 16.2 +0.1/0 high so the fork slides; inside corners R2; drill the dowel holes Ø5.8 for now and ream them with the roof block in place |
| Roof block | 20 mm 6061-T6 plate | Mill to 19 × 60 × 42 −0/−0.05; tap 4 × M8 14 deep in the ends; Ø3.4 holes counterbored Ø6.5 for the wear plate | The 42 sets the plate spacing and its ends set the plates parallel: ends square to the base within 0.02 |
| Fork plate | 16 mm mild steel | Mill to 92 × 66 × 16.0 −0/−0.1; cut the 54 +0.2/0 slot with its R27 end on the CNC; tap 4 × M6 12 deep from below; break the slot edges 0.5 | Top face flat (fly-cut): it bears on the collar flange |
| Base plate | 12 mm 6061-T6 | Profile, R47 and slot on the CNC; drill A and B Ø6.6; drill and tap C M8 with the plate flat on the table; drill D Ø5.8 for now | C square to the face within 0.05: it sets the guide pins vertical |
| Guide pins (2) | Ø12 h6 ground rod | Cut to 140; turn an M8 spigot 11 long with a small undercut; face the shoulder in the same setting; die-cut M8 × 1.25; chamfer the top | The shoulder squareness is what keeps the pin vertical |
| Lugs (2) | 25 × 20 6061-T6 flat, 2 × 42 | Mill to 40 × 24 × 20; drill and ream Ø16 H7 through, centred on the 40 and 14 from the mounting face; press in the bush and ream it Ø12 H8 afterwards; drill 2 × Ø7 at 28 centres | The Ø7 holes give a little float for fitting on the pins (below) |
| Mount plate | 12 mm 6061-T6 | Profile 100 × 100; bore Ø40; spot the 4 × Ø13 from the cylinder's own front threads; drill 4 × Ø6.6 | Spot the 74.07 pattern from the cylinder rather than marking it out; fit steel thread inserts in the side plates' front-edge M6 holes, since this plate comes off whenever the cylinder does |
| Thrust bar, stop block | 10 × 30 6061-T6 flat | Mill to 42 −0/−0.1 with square ends; tap 2 × M5 12 deep in each end; bar: 2 × M3 for the bronze strip; block: M8 through | Same 42 as the roof block; stop block's M8 square to the face within 0.05 |
| Cage cross pins (4) | Ø5 W1 | Cut about 75; groove for e-clips just outside each plate | Check the length on the assembled plates; no hardening needed |

**Fitting the housing to the head.**

1. Assemble the side plates and roof block with the M8s finger-tight, ream both Ø6 dowel holes through plate and block together, fit the dowels and tighten. Fit the thrust bar, stop block and cage pins.
2. Scrape the paint from the head top under the base plate. Turn a centring ring, bore Ø90 to fit the boss and OD Ø94 to fit the plate's cut-out, about 4 high. With the ring locating the plate, spot A and B through onto the head, drill Ø5.0 through the 9 mm top (grease the drill, vacuum the chips) and tap M6.
3. Screw the plate down, then drill and ream the two D holes Ø6 through the plate and 8 deep into the head; fit the dowels. Remove the ring.
4. Screw in the guide pins with retaining compound and fit the rest collars low.
5. Fit the lugs loosely to the side plates, lower the housing onto the pins with the anvil clear of the push pad, and slide the fork in under the collar flange; fit its four screws. Raise the rest collars until the fork-to-flange gap is 0.5–1 mm on feelers, then tighten the lug screws with the housing hanging free on the pins. Fit the springs and top collars.
6. Fit the cylinder and JA joint, set the spacer-tube length, then transfer the mount plate's M6 holes into the side plates' front edges and tap them.

## Cylinder

**Cylinder as fitted: SDA 80 × 25** (measured 28 Oct 2026)

&#91;image: SDA 80 × 25 compact cylinder, rod end up, with PC10-03 push-in fittings on the port side\]

| Feature | Measured | Notes |
| --- | --- | --- |
| Bore × stroke | 80 × 25 mm | Force is set by the bore, so it is the same as the 80 × 30: 2.51 kN at 5.0 bar |
| Body | 94 mm square (94.07 measured) × 66.28 mm | Rear face to front face. Rear face is flat, with an 82.6 mm rebate down to a near-flush Ø45 centre |
| Width over the port boss | 104 mm | Both ports central on one side face (the face the label calls the top); the fittings stand out further than this |
| Rod end, retracted | 78.41 mm from the rear face | Rod boss 70.9 mm from the rear face; the rod stands 12.1 mm proud of the front face |
| Rod end, extended | about 103.4 mm (derived: 78.41 + 25) | Not measured; stroke taken as the nominal 25 |
| Mounting holes | 4 × M12 × 1.75 on a 74.07 mm square (centres 10 mm in from each edge). From each face: 14 mm plain, then 14 mm of thread; a 10 mm clear bore joins the two, so an M10 bolt passes right through | Both faces tapped the same (measured) |
| Rod end thread | Female M14 × 1.5 (re-measured; first recorded as M12 × 1.75), 32 mm of thread in a 33 mm deep hole | Rod diameter 25.00 mm (measured) |
| Ports | PC10-03 push-in: 10 mm tube, R3/8 thread | Already fitted. Mounted with the ports facing the machine's left; the square hole pattern allows any of four positions |
| Mass | 1.199 kg including the fittings | Used in the lever vs wedge comparison (was assumed 1.5 kg) |
| Label and rating | LAIZE SDA80×25, 0.15–0.8 MPa | 0.8 MPa is well above the 0.62 MPa supply; the regulator runs it at 0.50 |
| Magnetic piston | No | No reed switch is possible. Wedge position is not sensed; the K1 auxiliary contact is the interlock |
| Rod side play | Not measured (sheet item 7.13) | The floating joint takes up misalignment, so this is information only |

**What the 25 mm stroke changes.** Nothing on force. On travel, the normal release needs 13.2 mm, the hard stop 15 mm and the washer-flat limit 17.4 mm, so at least 7.6 mm of stroke stays unused. The calculator now has S = 25 and still shows OK; the largest drawbar stroke the cylinder could cover is 2.7 mm, more than the washers allow.

**Air.** Extending 15 mm sweeps about 75 cm³, so about 0.45 L of free air at 5.0 bar, and the return stroke uses a similar amount. That is under 1 L per tool change against a 9 CFM (about 255 L/min) supply, so the 10 mm tubing is more than enough. Release speed is set by the valve and the flow controls, not the tube.

**Valve.** The control power supply has a spare 24 VDC output for the coil. A 5/2 single-solenoid, spring-return, internally piloted valve with 1/4 BSP ports suits this, for example the Airtac 4V210-08 24 VDC (reseller listing: 1/4" BSP ports, 21–114 psi, about 1.5–7.9 bar). Use a DIN coil plug with an LED and suppression. Coil current should be checked against the supply's spare capacity and the relay contact rating once a valve is chosen.

## Pneumatic and control circuit

The valve is single-solenoid with spring return, so the tool stays clamped unless air, 24 V and an Acorn release signal are all present and the spindle is stopped. Loss of any one leaves the cylinder retracted and the washers clamping.

&#91;embedded content: pneumatic and control circuit · air path, release logic, interlock\]

| Part | Specification | Why |
| --- | --- | --- |
| Filter-regulator | With gauge, set to 5.0 bar | Keeps the cylinder below full supply, which limits the worst-case collar load to about 5.4 kN |
| 5/2 valve | Single solenoid, spring return, 24 VDC coil from the control supply's spare output; 1/4 BSP ports (e.g. Airtac 4V210-08) | De-energised = retract port pressurised = wedge withdrawn, anvil clear |
| Flow controls | Meter-out, one on each cylinder port (or speed-control silencers on the valve exhausts) | Controls speed in both directions without slamming the wedge into the stop |
| Silencers | On both valve exhausts | Noise |
| Tube | 6–8 mm OD polyurethane, push-in fittings | Each release uses under 1 L of free air, so flow is not critical |
| Valve relay | Driven by a spare Acorn output; contact rated for the coil | The Acorn's open-collector outputs need a relay to drive a solenoid |
| Hardware interlock | Normally closed contact of the spindle run relay, in series with the valve coil | Blocks release even if the software misbehaves |
| Lubricator | Not fitted | Modern cylinders come pre-greased; once air is lubricated it must stay lubricated (general practice, my judgement) |

The interlock wiring stays a concept until the spindle drive and the free Acorn inputs and outputs are confirmed.

**Control wiring (draft).** The valve is switched by its own relay, K1, through two hardware interlocks in series: K1 itself, and K2T, an off-delay timer relay on the spindle-on signal. K2T's contact opens the moment the spindle is switched on and only recloses after the coast-down time has passed. The Acorn sees a K1 auxiliary contact so its PLC can refuse a spindle start while the tool is released, and a spare open-collector output can drive K1 for an M-code release later.

&#91;embedded content: control wiring · 24 VDC ladder, draft\]

**Acorn I/O facts used** (Centroid Acorn spec manual): 8 inputs, optically isolated, 24 VDC, on when pulled below 5.9 V, about 20 mA each; outputs 1–2 are relays rated 5 A at 30 VDC; outputs 3–8 are open collector, 50 mA maximum. The valve coil (a few watts, roughly 0.1–0.2 A at 24 V for a valve like the 4V210, to confirm on the coil label) is over that 50 mA, so it must go through K1.

**Still to confirm on your controller:** which spare input and output terminals to use; where a 24 V spindle-on signal can be taken without loading the drive's own run input; the spindle's coast-down time from full speed; and how your Acorn software version exposes a spindle-start inhibit and custom M-codes. I could not find Centroid's Wizard function names for a power drawbar in public documentation, so the PLC side is described by function, not by menu name.

**Acorn logic, in plain terms.** The hardware rungs (K2T and K1 in series with the valve coil) already stop a release while the spindle turns; the PLC adds a second, software layer and reports state. Terminal numbers wait on sheet 9.13.

1. **Inputs and outputs:** one spare input for "release active" from K1's auxiliary contact; one open-collector output (OUT3) to drive K1's coil for an M-code release.
2. **Block spindle start:** while "release active" is on, the PLC refuses to start the spindle and shows a message such as "drawbar released".
3. **Fault on conflict:** if "release active" comes on while the spindle is commanded on (which the hardware should prevent), stop the spindle and raise a fault.
4. **M-code release (later):** the release M-code turns OUT3 on only when the spindle is commanded off and a software timer at least as long as K2T's delay has run since spindle-off; the clamp M-code, or a timeout of about 10 s, turns it off.
5. **Manual button:** S1 drives K1 directly through the hardware rungs, so it works even if the PLC has faulted; the PLC sees it through the same "release active" input.

## Commissioning

Set the parts in this order: collet, collar, preload, gaps, hard stop, then air. Each step fixes a reference the next one measures from. With 8 washers and a 1.2 mm stroke the tool should release at about 4.5 bar; a much higher figure means friction, a wrong preload or a sticking collet.

**Assembly and adjustment**

1. **Collet.** Grind the nose so clamped stick-out is 1.5 mm or less. Clean the spindle taper; anti-seize the collet outside and threads.
2. **Collar.** Slide it down the spline until the shoulder sits on the spindle end face. Torque the six M8 screws evenly to 32 Nm, keeping both joint gaps equal. Scribe a witness line across collar and spindle.
3. **Drawbar and stack.** With a TTS holder in the collet, thread the drawbar fully into the collet and record the turns. Fit the base thrust washer, then the washers in series (alternating), greased with MoS₂, then the top thrust washer and preload nut.
4. **Preload.** Measure the washers' free height, then tighten the nut until the stack measures 8 × (free height − 0.35 mm) between the thrust washers: about 20.4 mm. Fit and lock the jam nut, then the push pad. Check the holder flange is down on the spindle nose: a 0.02 mm feeler should not enter.
5. **Housing and gaps.** Fit the housing on its float pins. Set the fork-to-flange gap at 0.5–1 mm and check the anvil sits about 1 mm clear of the push pad with the wedge retracted. Turn the spindle by hand: nothing may touch.
6. **Hard stop.** With a dial indicator on the push pad, set the stop so the wedge can push the drawbar s\_r + 0.3 mm beyond first contact, and never more than about 1.9 mm, or the washers go flat.

**Air and first release**

1. Close both flow controls, then open each one turn. Set the regulator to 3 bar.
2. Press release. At 3 bar nothing should happen: the cylinder cannot beat the preload. If the tool drops, the preload is low.
3. Raise the pressure in 0.5 bar steps until the holder drops freely. Record the pressure; about 4.5 bar is expected.
4. Set the regulator to 5.0 bar for service, about 0.5 bar above the expected release pressure; this caps the collar load if a collet ever sticks.
5. Adjust the flow controls until extend and retract are smooth, about half a second each, with no slam (my suggestion).

**Interlock and fail-safe checks**

- Spindle running: press release, nothing happens.
- Spindle just stopped: release stays blocked until the coast-down delay ends.
- Cut power to the valve mid-release: the cylinder retracts and the tool clamps.
- Shut off the air mid-release: the washers clamp the tool.

**Run-in**

- Cycle 50 tool changes. Check the witness line, the stack height and the holder seating.
- Touch off the same tool 10 times with a change between each; the spread is your tool-length repeatability.

**After two weeks and in service**

- Re-measure the stack and reset it to height: stacks lose about 5% of force in the first two weeks ([Surisa](https://www.surisa.es/en/collections/disc-springs-din-2093)).
- Monthly: inspect the washers for cracks and replace any damaged ones at once; anti-seize or grease between washers every 5,000 cycles or six months ([Tormach](https://docs.tormach.com/Content/Online-Only/power_drawbar_maintenance.htm)). Check the witness line.
- Replace the spindle collet when holders stop dropping out freely; Tormach users treat it as a wear item.

## Parts list

32 lines for the wedge design: 11 purchased, 11 committed and ready to source, and 10 still proposed until their design is finished. Change the Status column as parts are bought. "Committed" means the design is fixed and the part can be ordered; "Proposed" means its design or size may still change. The lever design's list is List A in Appendix B.

**List B: wedge design**

Rows 1–8 and 20–29 are common to List A (lever design, Appendix B).

| # | Item | Qty | Specification | Source | Waiting on | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Air cylinder | 1 | SDA 80 × 25 compact, double-acting (owned) | Owned | — | Purchased |
| 2 | R8 collet, 3/4" | as ordered | TTS-style, 7/16-20 UNF; grind nose to ≤1.5 mm stick-out | Ordered | Arrival | Purchased |
| 3 | Belleville washers | 2 sets (16) | Genuine Tormach 31319 (30.2 × 11.4 × 2.3 mm), sets of 8: one for the stack, one spare | Tormach | Quote from AU Tormach distributor | Committed |
| 4 | Drawbar bar | 1 m | 4140/709M, 16 mm peeled round × 1 m (Edcon 4140RND.16, ordered 29 Oct 2026) | Edcon Steel | — | Purchased |
| 5 | Collar blank | 1 | 4140/709M, 65 mm peeled round (Edcon 4140RND.65, ordered 29 Oct 2026) for the 52 OD, Ø64 flange, 60 high collar; only 0.5 mm per side to clean up the flange | Edcon Steel | — | Purchased |
| 6 | Push pad and thrust washers | 1 bar | 4140 from bars already ordered: push pad Ø16 × 8 from the Ø16 drawbar offcut; two thrust washers 32 OD × 11.3 bore, 3 and 4 mm, from the Ø50 bar (or the Ø65 collar offcut); all hardened and tempered with the wedge and anvil | Edcon Steel (ordered bars) | — | Purchased |
| 7 | Drawbar nuts | 2 + spares | 7/16-20 UNF heavy hex nut and jam nut, grade 8 | Fastener supplier | — | Committed |
| 8 | Collar clamp screws | 6 + 2 spare | M8 × 25 socket head, grade 12.9 | Fastener supplier | — | Committed |
| 9 | Wedge and anvil stock | 1 | 4140/709M, 50 mm peeled round (Edcon 4140RND.50, ordered 29 Oct 2026): wedge 80 long, anvil 40 long, plus saw and facing allowance | Edcon Steel | — | Purchased |
| 10 | Roof wear plate stock | 1 | O1 ground flat stock 40 × 5 × 500 (Edcon fgsfl.40.5.500, ordered 29 Oct 2026); wear plate finished 60 × 40 × 5; plus 4 × M3 × 18 cap screws | Edcon Steel | — | Purchased |
| 11 | Rollers | 4 + 1 spare | Ø14 × 36 mm hardened, ground dowel pins, ISO 8734, 58–62 HRC (supplier spec) | Purchased | — | Purchased |
| 12 | Roller cage and springs | 1 set | 2 cages from 2 mm brass sheet; 4 light compression springs Ø5 × 16 free (about 0.1 N/mm); 4 × Ø5 silver-steel cross pins with e-clips (Ø5 W1 silver steel ordered from Edcon, 2 × 1 m) | Engineering supplier | — | Committed |
| 13 | Floating joint | 1 | SMC JA40-14-150 floating joint, M14 × 1.5, rated 4,400 N tension/compression,&#32; plus an M14 × 1.5 × 40 grade 10.9 or 12.9 stud (or fine-thread bolt with the head cut off) into the rod; check the joint's overall length against the rod-to-wedge gap | Pneumatics supplier | — | Purchased |
| 14 | Housing side plates | 2 | 12 mm 6061-T6, 130 × 189, a mirrored pair: fork window, collar notch, anvil lift pockets and all holes as the side plate drawing | Aluminium supplier | — | Proposed |
| 15 | Roof block | 1 | 6061-T6, 19 × 60 × 42 mm finished (from 20 mm plate; 19 because the wear plate is 5 mm); 4 × Ø3.4 holes counterbored Ø6.5 × 3.5 for M3 × 18 | Steel supplier or offcut | — | Committed |
| 16 | Cylinder mount plate | 1 | 12 mm 6061-T6, 100 × 100, Ø40 centre bore; 4 × M12 × 1.75 socket heads into the cylinder's front threads; 4 × M6 × 25 into the side plates' front edges; spacer tubes on the M12s if the JA joint needs more room | Steel supplier, fastener supplier | — | Proposed |
| 17 | Fork plate | 1 | 16 mm mild steel, 92 × 66, slot 54 wide with an R27 end; slides through the side-plate windows under the collar flange and rests on the plates' feet; 4 × M6 × 30 up through the feet | Steel supplier | — | Proposed |
| 18 | Anvil parts | 1 set | Rear thrust bar, 6061-T6 10 × 30 × 42, faced with a 3 × 25 × 40 bronze strip; 2 × Ø5 m6 × 10 dowel pins (ISO 8734) as lift pins, pressed into the reamed H7 holes; 2 light springs under them | Engineering supplier | — | Proposed |
| 19 | Hard stop | 1 | M8 set screw and lock nut in a rear stop block (6061-T6 10 × 20 × 42) between the side plates | Fastener supplier | — | Proposed |
| 20 | Float guides | 2 sets | 2 × Ø12 h6 ground rod 140 long (M8 × 11 spigot turned on one end); 2 lugs (6061-T6 40 × 24 × 20) with Ø12/Ø16 × 20 bronze bushes; 4 × Ø22 × 10 set-screw collars; 2 compression springs, about 13 ID × 20 free, about 3 N/mm, fitted at 12 long (about 24 N each) | Bearing or engineering supplier | — | Proposed |
| 21 | Head-top base plate | 2 | 12 mm 6061-T6 replacing the belt cover: outline flush with the head top, R47 cut-out round the spindle opening into an 80 wide slot to the rear for the belt; 4 × M6 × 20 (8.8) into new holes tapped through the 9 mm casting top; 2 × Ø6 dowels; carries the two float guide pins (see the base plate drawing) | Steel supplier | Corner-hole positions and depth (sheet 9.9), 9.8, 9.10 | Proposed |
| 22 | Filter-regulator | 1 | With gauge, 1/4" ports, set to 5.0 bar | Pneumatics supplier | — | Committed |
| 23 | Solenoid valve | 1 | 5/2 single solenoid, spring return, 24 VDC | Pneumatics supplier | — | Committed |
| 24 | Flow controls | 2 | Meter-out, push-in, 10 mm tube × R3/8, in place of the PC10-03 fittings | Pneumatics supplier | Port thread | Purchased |
| 25 | Silencers | 2 | To suit the valve exhaust ports | Pneumatics supplier | Valve choice | Purchased |
| 26 | Tube and fittings | 1 lot | 10 mm PU tube about 3 m; PC10-02 fittings for the valve's 1/4 BSP ports | Pneumatics supplier | — | Committed |
| 27 | Release button | 1 | Momentary pushbutton, panel mount, front faceplate | Electrical supplier | — | Committed |
| 28 | Valve relay | 1 | K1: 24 VDC coil drawing under 50 mA (so an Acorn open-collector output can drive it), contacts rated at least 1 A DC, one spare NO for the Acorn input; flyback diode | Electrical supplier | Acorn I/O | Proposed |
| 29 | Consumables | 1 lot | MoS₂ grease, anti-seize, thread-locker | Hardware store | — | Committed |
| 30 | Timer relay K2T | 1 | 24 VDC multifunction DIN-rail timer relay with an off-delay (delay-on-release) mode, adjustable about 0.5–10 s | Electrical supplier | Spindle-on signal source | Proposed |
| 31 | Fuse and terminals | 1 lot | F1 1 A fuse and DIN-rail holder; DIN-rail terminals; 1N4007 flyback diode | Electrical supplier | — | Committed |
| 32 | Z-axis gas strut | 1 | Stroke at least 250 mm; extended force about 0.7 × the measured head weight; bleed-valve type; eye or M8 ball-joint ends | Gas spring supplier | Head weight measurement | Proposed |

**Ready to order now** (the Committed rows of List B, grouped by supplier)

| Supplier | Rows | Order |
| --- | --- | --- |
| Tormach AU distributor | 3 | 2 sets of 31319 washers (16), quote pending |
| Edcon Steel (ordered 29 Oct 2026) | 4, 5, 6, 9, 10, 12 | 4140/709M peeled round: Ø16 × 1 m, Ø50 × 150, Ø65 for the collar; O1 ground flat stock 40 × 5 × 500; Ø5 W1 silver steel 2 × 1 m |
| Aluminium supplier | 14, 15, 16, 18, 19, 20, 21 | All 6061-T6. Plate 12 × 400 × 250: side plates 2 × 130 × 189 side by side, with the base plate (115 × 107) and mount plate (100 × 100) stacked beside them. Plate or bar 20 × 60 × 50: roof block (19 × 60 × 42 finished). Flat 10 × 30 × 100: thrust bar and stop block (42 each). Flat 25 × 20 × 90: two lugs (40 × 24 × 20 finished). |
| Engineering supplier | 12, 17, 18, 20 | Mild steel 16 × 100 × 70 (fork plate); 2 mm brass sheet about 100 × 50 (cages); bronze strip 3 × 25 × 40; Ø12 h6 ground rod 2 × 140; 2 bronze bushes Ø12/Ø16 × 20; 4 × Ø12 shaft collars |
| Gas spring supplier | 32 | Z-axis gas strut, once the head weight is measured (see Z-axis gas strut) |
| Fasteners | 7, 8, and the hardware list | Everything in the hardware list below: screws, dowels, springs, e-clips and thread inserts |
| Pneumatics | 22, 23, 26 | Filter-regulator with gauge, 1/4″; \
5/2 single-solenoid, spring-return valve, 24 VDC, 1/4 BSP (for example 4V210-08), with an LED and suppression DIN plug; \
10 mm PU tube about 3 m; \
2 × PC10-02 for the valve plus a fitting for the regulator |
| Electrical | 27, 31 | Momentary NO panel pushbutton; \
1 A fuse and DIN-rail holder; \
DIN-rail terminals; \
1N4007 diode |
| Hardware store | 29 | MoS₂ grease, anti-seize, thread-locker |

The floating joint (row 13) can be ordered as the SMC JA40-14-150, whose 4,400 N rating covers the load; confirm its length against the rod-to-wedge gap first. Hold off on the housing plates (rows 14, 16–19, 21) until the head measurements are in.

**Hardware list (wedge design).** Every screw, pin and small bought part in one place. Lengths are checked against the parts they pass through; grade 8.8 unless stated.

| Item | Qty | Size and spec | Where |
| --- | --- | --- | --- |
| Socket head cap screw | 6 + 2 spare | M8 × 25, grade 12.9 | Collar clamp |
| Heavy hex nut and jam nut | 1 + 1, plus spares | 7/16-20 UNF, grade 8 | Drawbar preload |
| Stud | 1 | M14 × 1.5 × 40, grade 10.9 or 12.9 (or a fine-thread bolt with the head cut off) | Cylinder rod to JA joint |
| Thin nut | 1 | M14 × 1.5 (if not supplied with the JA) | JA stud, locked against the wedge end |
| Socket head cap screw | 4 | M12 × (35 + spacer length); through the 12 mm plate this engages 9 mm of the cylinder's 14 mm thread | Cylinder to mount plate |
| Spacer tube | 4 | ×13 ID, length set from the JA measurement (may be none) | Behind the cylinder |
| Socket head cap screw | 4 | M6 × 25 | Mount plate to side-plate front edges |
| Socket head cap screw | 4 | M8 × 25 | Roof block to side plates |
| Dowel pin, ISO 8734 | 2 | ×6 m6 × 20 | Roof block to side plates |
| Socket head cap screw | 4 | M3 × 18 | Wear plate up into roof block |
| Socket head cap screw | 8 | M5 × 20 | Thrust bar and stop block ends |
| Countersunk screw | 2 | M3 × 8 | Bronze strip to thrust bar |
| Hex set screw and nut | 1 + 1 | M8 × 30, full thread | Hard stop |
| Socket head cap screw | 4 | M6 × 30 | Fork plate, up through the feet |
| Socket head cap screw | 4 | M6 × 35 | Float lugs to side plates |
| Socket head cap screw | 4 | M6 × 20: through the 12 mm plate, 8 mm into the 9 mm casting top, so nothing pokes through | Base plate to head |
| Dowel pin, ISO 8734 | 2 | ×6 m6 × 16 | Base plate to head |
| Dowel pin, ISO 8734 | 2 | ×5 m6 × 10 | Anvil lift pins |
| Shaft collar, set-screw type | 4 | ×12 bore | Float guide rest and top collars |
| Sintered bronze bush | 2 | ×12 × ×16 × 20 | Float lugs |
| Compression spring | 2 | to suit ×12 pin, about 20 free, about 3 N/mm | Float hold-down, about 24 N fitted |
| Compression spring | 4 | ×5 × 16 free, about 0.1 N/mm | Roller cages |
| Compression spring | 2 | to fit a ×6 pocket, about 10 free, 1–2 N fitted | Anvil lift |
| E-clip, DIN 6799 | 8 | for ×5 shaft | Cage cross pins |
| Thread insert, Helicoil type | 4 | M6, 1.5 × d long | Side plates' front edges, for the mount-plate screws (removed with the cylinder) |
| Thread insert, Helicoil type (optional) | 4 | M8, 1.5 × d long | Roof block ends, if the box will be taken apart often |

## Open items

The release stroke is the critical input; most other dimensions follow from it.

- [ ] Release stroke s\_r: section 5 test with the new 3/4" collet and the existing 7/16-20 drawbar at 15–20 Nm
- [ ] Collet thread length and engagement (rows 3.5–3.7)
- [ ] Grind the new collet nose so clamped stick-out is 1.5 mm or less, at least 0.5 mm under the 2.0 mm holder rebate; measure stick-out at design preload before grinding (the sample collet would need about 2.3 mm removed)
- [ ] Taper break effort: first estimate of push-out force P
- [ ] Spline profile: crest width, root diameter, hardness (file test) for the cap clamp
- [ ] Air supply: 90 psi at 9 CFM confirmed; still need compressor cut-in pressure and fittings at the mill
- [ ] Controller: 24 VDC for the valve is available from the spare supply outputs; still need the spindle-on signal source and spare Acorn I/O (sheet 9.13)
- [ ] Washers fixed at 8 × Tormach 31319: check the release stroke is within about 1.2 mm (1.6 mm at 5.5 bar); if not, fit a genuine Tormach collet. Measure the washers' free height before setting preload
- [ ] Order 2 sets of genuine Tormach 31319 (16 washers)
- [ ] File-test the spline: if it is soft, the grooved, positive-hold collar is available as a fallback
- [ ] Pilot-drill, or look under the head top, at the four new M6 base-plate positions to make sure they miss any ribs
- [ ] Spindle coast-down time (sheet 9.12) to set the K2T off-delay
- [ ] Measure the JA40-14-150 fitted to the rod, cylinder retracted: from the cylinder front face to the face of the JA's stud nut. Up to 30 mm fits as drawn; anything over 30 mm is the length of the spacer tubes behind the cylinder
- [ ] Cylinder rod side play (sheet 7.13), for information
- [ ] Quick check: the cylinder's rod boss is under Ø38, so it clears the mount plate's Ø40 bore (only matters if no spacers are needed)
- [ ] Lengths of the Ø16 and Ø65 bars as delivered, against the cutting list (the Ø50 is 150, which is enough)
- [ ] Head weight W for the gas strut: Z coupling undone, luggage scale, average of the just-rising and just-falling readings; then the strut's column and head bracket positions

## Appendix A – Washer suppliers

Tormach is the only source found with a published price and stock for a 30 mm high-load drawbar washer: US$4.95 each. Everything else is quote-only, and none of the US sources shows shipping to Australia. Prices are as listed on 27 Oct 2026.

**Spec to quote against**

- About 30 mm OD; bore 11.3–11.5 mm (clears the 7/16" thread, guides on an 11.2 mm section); 2.3–2.5 mm thick
- Free height about 2.9–3.1 mm (cone height about 0.6 mm); flat load about 13–15 kN
- Hardened spring steel or 17-7PH; not 304 stainless
- About 24 pieces from one batch (20 for the stack plus spares); fewer if the release stroke is short

| Supplier | Part | OD × bore × t (mm) | Load data | Price and availability | Notes |
| --- | --- | --- | --- | --- | --- |
| [Tormach](https://tormach.com/power-drawbar-spring-washer-31319.html) (US) | 31319 Power Drawbar Spring Washer | 30.2 × 11.4 × 2.3 | Not published | US$4.95 each, in stock; ask Tormach about shipping to Australia | Made for 7/16" R8 drawbars, the proven reference part |
| [Solon](https://www.solonmfg.com/7h89177) (US), via distributors | 7H89177 | 30.2 × 11.4 × 2.44, height 3.07 | 15.1 kN flat at 0.64 mm | Not listed | 17-7PH; the basis for this design's sizing. Specify 7H89177: the [7H89301](https://www.eindustrialsolutions.com/solon-7h89301-belleville-spring-washer-imperial-7/16-in-0-45-in-id-1-188-in-od-0-096-in-thick-stainless-steel) (301 stainless, height 3.63) is a different washer at 12.0 kN flat |
| McMaster-Carr (US) | 9712K436 | Not confirmed | About 8.4 kN working load (builder's figure) | Not checked | Used on a [PM728 build](https://hobby-machinist.com/threads/made-a-power-drawbar-for-the-pm728.91641); check whether McMaster will ship to you |
| [Bell Springs](https://www.bellsprings.com.au/category/disc-springs-din-2093) (Melbourne) | Quote to the spec above | — | — | Earlier DIN A50 quote: $131; re-quote to this spec | Local, no import freight; 03 9464 6611, sales@bellsprings.com.au |
| [Belleville Springs](https://www.bellevillesprings.com/heavy-duty-bolting-washers/) (UK) | CW29133 heavy-duty bolting washer | 29 × 13 × 3, height 3.95 | 34.1 kN flat | Contact | Not recommended: about 36 kN/mm, so about 30 washers for a 2.5 mm stroke, and the 13 mm bore needs a guide sleeve |

[Newcastle Hi-Tensile Bolt](https://nhtb.com.au/washers-disc-spring-belleville-washers.html) (NSW) sells disc springs online in single quantities, but its M12 range tops out at 1.5 mm thick, too light for this stack.

**Decision.** Genuine Tormach 31319, two sets of 8 (US$79 before shipping): one set in the stack, one spare. The other suppliers are kept for reference.

**Care in service.** Tormach says to inspect the stack monthly for cracks, replace damaged washers immediately, and apply anti-seize between washers every 5,000 cycles or six months ([Tormach power drawbar maintenance](https://docs.tormach.com/Content/Online-Only/power_drawbar_maintenance.htm)).

## Appendix B – Lever actuator (alternative)

The 6:1 lever on a floating yoke was the first design. It works, and it is kept here for reference. The wedge in the main body was chosen for its lower mass (about 4.9 kg against 8.5 kg), lower height (about Z 152 against Z 275) and flat anvil contact. The collar, drawbar, washer stack, cylinder, pneumatics and controls are common to both.

**Lever or wedge**

|  | Lever (Appendix B) | Wedge (chosen) |
| --- | --- | --- |
| Estimated mass, cylinder weighed at 1.2 kg | About 8.5 kg | About 4.9 kg |
| Height above the spindle end face | Top plate at about Z 250 to 275 | About Z 152 |
| Centre of gravity | High; cylinder above the lever | Low; cylinder level with the wedge |
| Contact on the push pad | R30 line contact, about 1,300 MPa | Flat anvil, 84 MPa |
| Hardened, ground parts | Nose insert, push pad | Wedge, anvil, roof plate, 4 rollers, push pad |
| Machines needed | Mill and lathe | Mill, lathe and surface grinder (all available) |
| Cylinder mount | Clevis at both ends | Front face bolted, floating joint on the rod |
| Ratio adjustment | Slotted pivot, 5–6:1 | Fixed; new wedge and anvil |
| Main risk | Weight and height on the head | Roller load sharing and cage creep |

**Mass breakdown** (my estimates from part sizes; the SDA 80 × 25 weighed 1.199 kg with fittings)

- **Lever:** top plate 1.8 kg, side plates 1.85, lever 1.0, pivot cheeks 0.7, fork 0.6, clevis plates and pins 0.9, float lugs and stop 0.4, cylinder 1.2: about 8.5 kg. The side plates and cheeks grew with the 22 mm taller yoke, which cancels the lighter cylinder.
- **Wedge (updated 29 Oct 2026):** side plates 1.40 kg, cylinder 1.20, wedge and anvil 0.66, fork 0.40 (steel), mount plate 0.28, roof block and wear plate 0.22, JA joint and stud 0.21, rollers 0.17, lugs 0.10, small parts about 0.3: about 4.9 kg floating, plus about 0.5 kg of base plate and guide pins fixed to the head. Most of the frame is 6061-T6; only the fork and the hardened parts are steel.

&#91;embedded content: concept section · floating yoke, lever and cylinder over the spindle cap\]

### Yoke and lever layout (draft)

The yoke is a rigid frame: a fork plate under the collar flange, two side plates, and a top plate carrying the lever pivot and the cylinder. The lever pivots 30 mm behind the drawbar axis and the cylinder acts 150 mm in front of it, giving 6:1. Everything below the top plate is fixed now; with the measured cylinder the top plate sits at about Z 250 to 275; the guide-pin positions still wait on the head-side measurements.

&#91;embedded content: yoke and lever layout · side view, draft\]

**Geometry** (X from the drawbar axis toward the cylinder, Z up from the spindle end face, mm; 8-washer stack)

| Point | X | Z | Notes |
| --- | --- | --- | --- |
| Push pad top | 0 | 63.4 | From the stack-up |
| Nose contact at rest | 0 | 64.4 | 1 mm running gap |
| Lever pivot | −30 | 95 | Lever centreline |
| Cylinder rod pin | +150 | 95 | 180 mm from the pivot, so 6:1 |
| Cylinder rear pin | +150 | 95 + L ≈ 241 | L = pin-to-pin length, about 146 mm (30 + 78.5 + 37), ±5 mm on the rod clevis thread |
| Top plate underside | — | about 95 + L + 9 ≈ 250 | Rear clevis cheeks hang 18 mm |
| Fork plate top | ±46 to ±27 | −0.5 to −1 | Under the flange underside at Z 0 |
| Hard stop | +30 | Adjust | The lever moves 2 × the drawbar travel here |

The lever runs toward the back of the head: the spindle is 60 mm from the front, leaving about 195 mm behind it, and the cylinder sits well above the pulleys.

**Load check** (my calculations; full 6.2 bar supply as the worst case, 5.0 bar setting in brackets)

| Member | Load | Section | Stress | Verdict |
| --- | --- | --- | --- | --- |
| Cylinder push | 3.12 (2.51) kN | — | — | — |
| Drawbar push (η 0.9) | 16.8 (13.6) kN | — | — | — |
| Pivot pin | about 15.6 (12.6) kN | 12 mm, double shear | 69 MPa shear; 108 MPa bearing in the lever | OK for hardened pin and mild steel |
| Lever at the nose | 468 (377) N·m | 50 × 12 mm, Z = 5,000 mm³ | 94 (75) MPa | OK; mild steel yields about 250 MPa (from memory) |
| Nose on push pad | 16.8 (13.6) kN | R30 line contact, 12 mm wide | about 1,300 (1,170) MPa Hertz peak | Needs a hardened insert and pad, at least about 55 HRC |
| Top plate | about 0.41 kN·m | 25 × 100 mm 6061-T6 | about 40 MPa | OK; about 240 MPa yield (from memory) |
| Side plates | 16.8 kN tension, shared | 2 × 10 × 40 mm | 21 MPa | OK |
| Fork under flange | 16.8 kN | 2 contacts, about 6 × 40 mm | 35 MPa | OK |
| Hard stop | up to about 6.2 kN | M10 screw | Low | OK |

**A nose, not a roller.** At up to 17 kN, a small rolling bearing is far beyond its rating; a 608 is about 1.4 kN static (from memory). A hardened R30 nose insert on the hardened push pad carries it as line contact. The nose rolls and slides about 4 mm across the 16 mm pad over the stroke; keep it greased.

**Float and rest.** The yoke sits by gravity on adjustable stop collars on two 12 mm guide pins fixed to the head-side brackets; the collars set the 0.5–1 mm hook gap. Light compression springs above the bushes hold it down against Z-axis decelerations, with preload about equal to the yoke's weight. On release the yoke lifts by the hook gap and all force stays inside the loop. The mass estimate is about 8.5 kg with the cylinder (see the comparison at the start of this appendix), so check that the Z axis and any head counterbalance can carry it.

### Lever cylinder mounts

The SDA 80 × 25 hangs from the yoke on a pinned clevis at each end. The cylinder then swings with the lever, and its short rod bearing carries only axial load. Loads are small (3.1 kN maximum), so the parts are sized for stiffness and easy machining, not strength. The cylinder's measured dimensions are under Cylinder in the main body.

&#91;embedded content: cylinder mounts · rear clevis, rod clevis, pins\]

**Pin-to-pin length.** Because the rod is female-threaded, the rod clevis gets an integral male spigot. My layout values: rear pin 30 mm behind the rear face (12 mm plate + 18 mm to the pin), 78.5 mm of cylinder and rod, and 37 mm from the rod face to the rod pin (8 mm jam nut, 5 mm adjustment, 24 mm of clevis). That gives L ≈ 146 mm, with the rear pin at about Z 241 and the top plate at about Z 250 to 275.

**Rear clevis plate** (on the cylinder)

| Feature | Dimension and notes |
| --- | --- |
| Material | 6061-T6 aluminium or mild steel, from one block (about 40 mm thick before machining) |
| Plate | 94 × 94 mm (the body is 94.07 mm square) × 12 mm thick |
| Fixing | 4 socket head screws into the cylinder's rear tapped holes, M12 × 1.75 on a 74.07 mm square, with the thread starting 14 mm below the face and running 14 mm. M12 × 35 socket heads through the 12 mm plate (heads on the plate face, not counterbored) give about 9 mm of engagement and stop about 5 mm short of the end of the thread. That is under the usual 1.5 × d, but each screw carries only about 0.8 kN, so I estimate the margin on stripping is still well over 10× |
| Location | If the rear face has a boss or recess, machine a matching spigot so the tongue sits on the cylinder axis |
| Tongue | 12 mm thick × 30 mm wide, centred, projecting 30 mm; end radius R15 |
| Pin hole | 10 mm H8, 18 mm from the plate face, square to the tongue faces |

**Yoke rear bracket** (double clevis)

| Feature | Dimension and notes |
| --- | --- |
| Cheeks | Two 8 mm mild steel plates, 12.2 +0.2/0 mm apart, bolted or welded to the yoke top plate |
| Pin hole | 10 mm H8, drilled and reamed through both cheeks in one pass so they line up |
| Orientation | Pin axis parallel to the lever pivot, about 0.2 mm in 100 mm (my judgement) |

**Rod clevis**

| Feature | Dimension and notes |
| --- | --- |
| Material | Mild steel or 4140 offcut, about 30 mm square × 38 mm, with an integral threaded spigot |
| Rod connection | The rod is female-threaded M14 × 1.5, 33 mm deep, so the clevis has an M14 × 1.5 spigot about 26 mm long: 21 mm (1.5 × d) of engagement plus about 5 mm for adjustment, and at least 7 mm clear of the bottom of the hole |
| Lock | M14 × 1.5 thin jam nut (DIN 439, 8 mm) on the spigot, locked against the rod end; the screwed length sets the lever's rest gap |
| Slot | 12.2 +0.2/0 mm wide × 28 mm deep; cheeks 9 mm each |
| Pin hole | 10 mm H8, 14 mm from the end, square to the slot |

**Pins and lever end**

| Feature | Dimension and notes |
| --- | --- |
| Pins | 10 mm hardened: ISO 7379 shoulder bolt with nyloc nut, or a dowel with e-clips; lightly greased |
| Lever end | 12 mm steel plate, R15 end, 10 mm H8 hole, or a 10 mm flanged bronze bush for wear |

**Load check** (my calculation; rod diameter 25 mm, measured)

| Item | Value |
| --- | --- |
| Maximum push, 80 mm bore at 6.2 bar | 3.12 kN |
| Maximum pull on retract, 25 mm rod, 6.2 bar (2.27 kN at 5.0 bar) | about 2.81 kN |
| Pin shear, 10 mm in double shear | about 20 MPa |
| Bearing, 10 mm pin in a 12 mm tongue | about 26 MPa |
| Rear screws, 4 off | about 0.8 kN each |

All of these are a small fraction of what 6061-T6 or mild steel takes, so there is room to thin the parts if the yoke layout needs it.

**Kinematics.** The rod pin sits 180 mm from the lever pivot. The normal release (13.2 mm of cylinder travel) turns the lever about 4.2°, the hard stop (15 mm) about 4.8°, and the washer-flat limit (17.4 mm) about 5.5°. The rod pin moves sideways at most about 0.8 mm, which swings the cylinder about 0.3° on its rear pin with L ≈ 146 mm, well within normal pin clearances.

**Option.** If you can't hold the pins parallel to the lever pivot, use a female spherical rod end (heim joint) on a stud adapter in place of the rod clevis. It tolerates a few degrees of out-of-plane misalignment.

**List A: lever design**

| # | Item | Qty | Specification | Source | Waiting on | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Air cylinder | 1 | SDA 80 × 25 compact, double-acting (owned; the SDA 80 × 30 from AliExpress is a spare) | Owned | — | Purchased |
| 2 | R8 collet, 3/4" | as ordered | TTS-style, 7/16-20 UNF; grind nose to ≤1.5 mm stick-out | Ordered | Arrival | Purchased |
| 3 | Belleville washers | 2 sets (16) | Genuine Tormach 31319 (30.2 × 11.4 × 2.3 mm), sold in sets of 8: one set for the stack, one spare set | Tormach (US$4.95 each, US$79 for 16) | Quote from AU Tormach Distributor | Committed |
| 4 | Drawbar bar | 1 m | 4140 condition T, 16 mm round | Collier & Miller, The Metal Warehouse, Russell Steel | — | Committed |
| 5 | Collar blank | 1 | 4140 condition T, 66 mm round × 70 mm (52 OD, 64 flange, 60 high) | Russell Steel, or a club offcut | — | Committed |
| 6 | Push pad and thrust washers | 1 bar | Silver steel, 35 mm round × 50 mm: pad 16 × 8 mm, two thrust washers 32 OD × 11.3 bore, 3 and 4 mm, all hardened and tempered | Engineering supplier | — | Committed |
| 7 | Drawbar nuts | 2 + spares | 7/16-20 UNF heavy hex nut and jam nut, grade 8 | Fastener supplier | — | Committed |
| 8 | Collar clamp screws | 6 + 2 spare | M8 × 25 socket head, grade 12.9 | Fastener supplier | — | Committed |
| 9 | Clevis pins | 2 | 10 mm hardened shoulder bolt, ISO 7379, about 10 × 30–35 shoulder, M8 nyloc nut | Fastener supplier | Cheek widths | Committed |
| 10 | Rear clevis plate blank | 1 | 6061-T6, 94 mm square × 40 mm thick, plus 4 × M12 × 35 socket head screws | Metal supplier | — | Committed |
| 11 | Rod clevis blank | 1 | Mild steel or 4140, 30 mm square × 70 mm (38 mm body plus an M14 × 1.5 spigot turned from the solid), plus an M14 × 1.5 thin jam nut | Metal supplier or offcut | — | Committed |
| 12 | Lever nose insert | 1 | Silver steel or O1, 12 × 20 × 25 mm, R30 contact face, hardened | Engineering supplier | — | Committed |
| 13 | Lever | 1 | Mild steel flat, 50 × 12 mm × about 220 mm | Steel supplier | Yoke layout | Proposed |
| 14 | Yoke plates | 1 set | Top plate 6061-T6 25 mm; side plates and pivot cheeks 10 mm steel; fork plate 10 mm steel | Steel and aluminium supplier | Yoke layout, cylinder length | Proposed |
| 15 | Pivot pin | 1 | 12 mm hardened dowel or shoulder bolt, double shear | Fastener supplier | Yoke layout | Proposed |
| 16 | Float guides | 2 sets | 12 mm ground rod, 12 mm bronze bushes, stop collars, light compression springs | Bearing or engineering supplier | Head brackets | Proposed |
| 17 | Side brackets | 2 | 10 mm steel plate; new tapped holes in the head sides | Steel supplier | Head-side measurements | Proposed |
| 18 | Hard stop | 1 | M10 set screw and lock nut in a lug under the lever | Fastener supplier | Yoke layout | Proposed |
| 19 | Filter-regulator | 1 | With gauge, 1/4" ports, set to 5.0 bar | Pneumatics supplier | — | Committed |
| 20 | Solenoid valve | 1 | 5/2 single solenoid, spring return, 24 VDC | Pneumatics supplier | — | Committed |
| 21 | Flow controls | 2 | Meter-out, push-in, 10 mm tube × R3/8, in place of the PC10-03 fittings | Pneumatics supplier | Port thread | Committed |
| 22 | Silencers | 2 | To suit the valve exhaust ports | Pneumatics supplier | Valve choice | Committed |
| 23 | Tube and fittings | 1 lot | 10 mm PU tube about 3 m (matches the PC10-03 fittings); PC10-02 fittings for the valve's 1/4 BSP ports | Pneumatics supplier | — | Committed |
| 24 | Release button | 1 | Momentary pushbutton, panel mount, front faceplate | Electrical supplier | — | Committed |
| 25 | Valve relay | 1 | 24 VDC coil, contact rated for the valve coil | Electrical supplier | Acorn I/O | Proposed |
| 26 | 24 VDC supply | 1 | Not needed: the control power supply has a spare 24 VDC output | Electrical supplier | Acorn I/O | Proposed |
| 27 | Reed switch | 1 | Not possible with the owned SDA 80×25: no magnetic piston (measured) | Pneumatics supplier | Cylinder check | Proposed |
| 28 | Consumables | 1 lot | MoS₂ grease, anti-seize, thread-locker | Hardware store | — | Committed |

## Sources

- [SX2.3 manual EN (spindle taper, travel)](https://www.sieg-machines.de/mediafiles/Sonstiges/SX2.3%20manual%20EN.pdf)
- [CNCzone – G0704 Power Drawbar Question (Hoss floating lever)](https://www.cnczone.com/forums/benchtop-machines/322024-forum.html)
- [LinuxCNC G0704 – Hydraulic Power Drawbar (Hoss PDB v2, no bearing load)](http://linuxcnc-g0704.blogspot.com/2014/09/hydraulic-power-drawbar.html)
- [Shane Wighton – Power Drawbar for X2 Mini Mill](https://shane.engineer/blog/power-drawbar-x2-mini-mill)
- [CNCArena – Manual Power Drawbar (Hoss TTS force guidance)](https://en.cncarena.com/forum/thread/311013-manual-power-drawbar/)
- [CNCzone – Power draw bar idea, feasible? (release force vs clamp force)](https://www.cnczone.com/forums/benchtop-machines/171662-power-draw-bar-idea-feasible.html)
- [Tormach TTS Adapter Collet R8 (50568)](https://tormach.com/tts-adapter-collet-r8-50568.html)
- [Tormach – Power drawbar parts lists](https://docs.tormach.com/Content/Online-Only/power_drawbar_diagrams_parts_lists.htm)
- [McMaster-Carr – R8 collets (grip tolerance)](https://www.mcmaster.com/products/collets/collet-size~3-4/)

* [Fasten.it – DIN 2093 disc spring dimensions and loads](https://www.fasten.it/en/norms/norm/din_2093)
* [Wikipedia – Belleville washer (stacking, 3 × OD stack-height guide)](https://en.wikipedia.org/wiki/Belleville_washer)
* [CNCArena – viking45 (Tormach 31319 washer dimensions)](https://de.cncarena.com/forum/user-post-list/330656-viking45/)

- [Solon 7H89177 Belleville spring washer (7/16" size, flat load)](https://www.solonmfg.com/7h89177)
- [Hobby-Machinist – PM728 power drawbar (McMaster 9712K436 washers)](https://hobby-machinist.com/threads/made-a-power-drawbar-for-the-pm728.91641)
- [Hobby-Machinist – shop-built CNC mill PDB (6 washers in series)](https://www.Hobby-machinist.Com/threads/shop-built-cnc-mill-project.105358/latest)
- [Surisa – DIN 2093 guiding, hardness and relaxation](https://www.surisa.es/en/collections/disc-springs-din-2093)
- [SMC – JA/JAH floating joint catalogue (JA40-14-150: M14 × 1.5, 40 mm bore, 4,400 N max tension/compression, 0.75 mm eccentricity, ±5°, installation notes)](https://static.smc.eu/pdf/JA-A_EU.pdf)
- [Atlas Steels – 4140 through-hardening bar datasheet (supply condition, hardening 850–860 °C oil, tempering 175–230 °C, 230–370 °C to avoid)](https://atlassteels.com.au/wp-content/uploads/2021/09/Through-Hardening-Low-Alloy-Steel-Bar-4140-Grade-Data-Sheet-10-09-21-1.pdf)
- [Edcon Steel – O1 flat ground stock 40 × 5 × 500](https://edconsteel.com.au/store/sp/fgsfl.40.5.500)
- [Edcon Steel – Gauge plate (O1) range](https://edconsteel.com.au/gauge-plate)
- Johnson, K. L., *Contact Mechanics*, Cambridge University Press, 1985: line-contact first yield and shakedown (cited from memory)
