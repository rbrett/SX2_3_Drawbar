%
O1902 (float lug mounting holes)
(Part: Float lug, each, mounting face)
(Setup: Mounting (40 x 20) face up, 40 along X)
(Z0: mounting face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X6 Y10
G0 Z5
G81 G99 X6 Y10 Z-1 R2 F150
X34 Y10
G80
G0 Z25
M5
M9
G0 Z25
(T19: Jobber drill 7.0 mm - Z: 7 mm clearance through the 24)
T19 M6
G43 H19
S2728 M3
M8
G0 Z25
G0 X6 Y10
G0 Z5
G83 G99 X6 Y10 Z-24.5 R2 Q2 F229
X34 Y10
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
