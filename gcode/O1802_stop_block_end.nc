%
O1802 (stop block end)
(Part: Rear stop block, each 10 x 20 end)
(Setup: Block on end, 20 along Y, 10 along X; run for each end)
(Z0: end face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X5 Y5
G0 Z5
G81 G99 X5 Y5 Z-1 R2 F150
X5 Y15
G80
G0 Z25
M5
M9
G0 Z25
(T12: Jobber drill 4.2 mm - X: M5 tap drill, tap 12 deep)
T12 M6
G43 H12
S4547 M3
M8
G0 Z25
G0 X5 Y5
G0 Z5
G83 G99 X5 Y5 Z-15 R2 Q2 F229
X5 Y15
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
