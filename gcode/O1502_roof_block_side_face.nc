%
O1502 (roof block side face)
(Part: Roof block, each 60 x 19 side face)
(Setup: Block on its side, one 60 x 19 face up, 60 along X, Y0 at the BOTTOM (wear-plate) face; run once for each side face)
(Z0: side face as clamped; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X15 Y10
G0 Z5
G81 G99 X15 Y10 Z-1 R2 F150
X45 Y10
X30 Y10
G80
G0 Z25
M5
M9
G0 Z25
(T18: Jobber drill 6.8 mm - Q: M8 tap drill, tap 14 deep)
T18 M6
G43 H18
S2808 M3
M8
G0 Z25
G0 X15 Y10
G0 Z5
G83 G99 X15 Y10 Z-17 R2 Q2 F229
X45 Y10
G80
G0 Z25
M5
M9
G0 Z25
(T16: Jobber drill 5.8 mm - R: dowel, ream 6 H7 x 10 deep with the plates (manual))
T16 M6
G43 H16
S3292 M3
M8
G0 Z25
G0 X30 Y10
G0 Z5
G83 G99 X30 Y10 Z-11 R2 Q2 F229
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
