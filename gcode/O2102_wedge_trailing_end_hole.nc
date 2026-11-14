%
O2102 (wedge trailing end hole)
(Part: Wedge, 4140, trailing end face)
(Setup: Wedge standing on its trailing end, 40.6 along X, as-milled TOP face toward +Y; X0 Y0 at the lower-left corner of the end face as seen from above (Y0 on the slope side))
(Z0: trailing end face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S1000 M3
M8
G0 Z25
G0 X20.3 Y12.05
G0 Z5
G81 G99 X20.3 Y12.05 Z-1 R2 F60
G80
G0 Z25
M5
M9
G0 Z25
(T18: Jobber drill 6.8 mm - pilot)
T18 M6
G43 H18
S842 M3
M8
G0 Z25
G0 X20.3 Y12.05
G0 Z5
G83 G99 X20.3 Y12.05 Z-18 R2 Q1 F46
G80
G0 Z25
M5
M9
G0 Z25
(T21: Jobber drill 12.5 mm - M14 x 1.5 tap drill; flat-bottom with an end mill if you can; tap 14 full thread)
T21 M6
G43 H21
S458 M3
M8
G0 Z25
G0 X20.3 Y12.05
G0 Z5
G83 G99 X20.3 Y12.05 Z-18 R2 Q1 F46
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
