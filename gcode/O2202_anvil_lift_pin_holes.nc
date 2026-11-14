%
O2202 (anvil lift pin holes)
(Part: Anvil, 4140, each side face)
(Setup: Anvil on its side, a 40 x 23.3 side face up, thrust face at X0, as-milled underside at Y0; run for each side)
(Z0: side face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S1000 M3
M8
G0 Z25
G0 X20 Y8.3
G0 Z5
G81 G99 X20 Y8.3 Z-1 R2 F60
G80
G0 Z25
M5
M9
G0 Z25
(T22: Jobber drill 4.8 mm - pin hole, tip depth 7.5 (full dia about 6.1): hand-ream 5 H7 to 6.5 after)
T22 M6
G43 H22
S1193 M3
M8
G0 Z25
G0 X20 Y8.3
G0 Z5
G83 G99 X20 Y8.3 Z-7.5 R2 Q1 F46
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
