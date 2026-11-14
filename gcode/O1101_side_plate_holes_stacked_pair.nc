%
O1101 (side plate holes, stacked pair)
(Part: Side plates (2), 12 mm 6060)
(Setup: Both blanks finished to 130 x 189, screwed back to back through the window area, clamped flat on a sacrificial plate; outer face of the LEFT plate up, front edge to +X)
(Z0: top face of the stack; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T1: Spot drill 90 deg (6 mm or larger))
T1 M6
G43 H1
S3000 M3
M8
G0 Z25
G0 X50 Y179.9
G0 Z5
G81 G99 X50 Y179.9 Z-1 R2 F150
X80 Y179.9
X65 Y179.9
X25 Y158
X105 Y158
X25 Y135
X105 Y121
X37 Y103
X37 Y121
X8 Y140.8
X8 Y150.8
X89 Y51
X117 Y51
G80
G0 Z25
M5
M9
G0 Z25
(T20: Jobber drill 8.5 mm - A: M8 clearance)
T20 M6
G43 H20
S2246 M3
M8
G0 Z25
G0 X50 Y179.9
G0 Z5
G83 G99 X50 Y179.9 Z-25.5 R2 Q2 F229
X80 Y179.9
G80
G0 Z25
M5
M9
G0 Z25
(T16: Jobber drill 5.8 mm - B: dowel, ream 6 H7 later with the roof block)
T16 M6
G43 H16
S3292 M3
M8
G0 Z25
G0 X65 Y179.9
G0 Z5
G83 G99 X65 Y179.9 Z-25.5 R2 Q2 F229
G80
G0 Z25
M5
M9
G0 Z25
(T14: Jobber drill 5.1 mm - C: cage cross pins)
T14 M6
G43 H14
S3744 M3
M8
G0 Z25
G0 X25 Y158
G0 Z5
G83 G99 X25 Y158 Z-25.5 R2 Q2 F229
X105 Y158
X25 Y135
X105 Y121
G80
G0 Z25
M5
M9
G0 Z25
(T15: Jobber drill 5.5 mm - D, E: M5 clearance)
T15 M6
G43 H15
S3472 M3
M8
G0 Z25
G0 X37 Y103
G0 Z5
G83 G99 X37 Y103 Z-25.5 R2 Q2 F229
X37 Y121
X8 Y140.8
X8 Y150.8
G80
G0 Z25
M5
M9
G0 Z25
(T13: Jobber drill 5.0 mm - F: tap M6 through after)
T13 M6
G43 H13
S3819 M3
M8
G0 Z25
G0 X89 Y51
G0 Z5
G83 G99 X89 Y51 Z-25.5 R2 Q2 F229
X117 Y51
G80
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
