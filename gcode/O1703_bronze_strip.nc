%
O1703 (bronze strip)
(Part: Bronze strip 40 x 25 x 3)
(Setup: Strip taped to a sacrificial plate, 40 along X)
(Z0: top face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X5 Y12.5
G0 Z5
G81 G99 X5 Y12.5 Z-1 R2 F150
X35 Y12.5
G80
G0 Z25
M5
M9
G0 Z25
(T11: Jobber drill 3.4 mm - V: M3 clearance; countersink 90 deg by hand so heads sit 0.3 below)
T11 M6
G43 H11
S4681 M3
M8
G0 Z25
G0 X5 Y12.5
G0 Z5
G83 G99 X5 Y12.5 Z-3.5 R2 Q1.5 F191
X35 Y12.5
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
