%
O1701 (thrust bar anvil face)
(Part: Rear thrust bar, 6061-T6 42 x 30 x 10)
(Setup: Anvil face up, 42 along X)
(Z0: anvil face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X6 Y15
G0 Z5
G81 G99 X6 Y15 Z-1 R2 F150
X36 Y15
G80
G0 Z25
M5
M9
G0 Z25
(T10: Jobber drill 2.5 mm - T: M3 tap drill, tap 8 deep)
T10 M6
G43 H10
S5000 M3
M8
G0 Z25
G0 X6 Y15
G0 Z5
G83 G99 X6 Y15 Z-9 R2 Q2 F229
X36 Y15
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
