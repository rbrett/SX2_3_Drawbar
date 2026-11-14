%
O1601 (roof wear plate)
(Part: Wear plate, O1 60 x 40 x 5 (annealed, before hardening))
(Setup: Plate on parallels, top (non-rolling) face up, 60 along X)
(Z0: top face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S1000 M3
M8
G0 Z25
G0 X5 Y6
G0 Z5
G81 G99 X5 Y6 Z-0.6 R2 F60
X55 Y6
X5 Y34
X55 Y34
G80
G0 Z25
M5
M9
G0 Z25
(T10: Jobber drill 2.5 mm - S: M3 tap drill to 3.2; tap 3 deep with a bottoming tap)
T10 M6
G43 H10
S2291 M3
M8
G0 Z25
G0 X5 Y6
G0 Z5
G83 G99 X5 Y6 Z-3.2 R2 Q1 F46
X55 Y6
X5 Y34
X55 Y34
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
