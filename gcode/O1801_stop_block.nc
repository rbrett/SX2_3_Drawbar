%
O1801 (stop block)
(Part: Rear stop block, 6061-T6 42 x 20 x 10)
(Setup: Wedge face up, 42 along X)
(Z0: wedge face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X21 Y10
G0 Z5
G81 G99 X21 Y10 Z-1 R2 F150
G80
G0 Z25
M5
M9
G0 Z25
(T18: Jobber drill 6.8 mm - W: M8 tap drill through; tap square)
T18 M6
G43 H18
S2808 M3
M8
G0 Z25
G0 X21 Y10
G0 Z5
G83 G99 X21 Y10 Z-10.5 R2 Q2 F229
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
