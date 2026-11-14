%
O1103 (side plate lift and spring pockets)
(Part: Side plate, each, inner face)
(Setup: Plate inner face up (same program for both: the pocket is on the centreline x 65), front edge to +X for the LEFT plate, to -X for the RIGHT plate; X0 Y0 at the lower-left corner as clamped)
(Z0: inner face; X0 Y0 = lower-left corner of the view, G54)
(Generated 14 Nov 2026 for the SX2.3 power drawbar build manual. Prove on air first.)
G21 G17 G40 G49 G80 G90 G94
G54
(T2: 6 mm carbide end mill, 2 or 3 flute)
T2 M6
G43 H2
S5000 M3
M8
G0 Z25
(G1 anvil lift pocket 7 x 9 x 3.5)
G0 X64.5 Y105.9
G0 Z1
G1 Z-0.875 F120
G1 X65.5 Y105.9 F400
G1 Y108.9 F400
G1 X64.5 Y108.9 F400
G1 X64.5 Y105.9 F400
G1 X65.5
G1 Y108.9
G1 X64.5
G1 Y105.9
G0 Z2
G0 X64.5 Y105.9
G0 Z1
G1 Z-1.75 F120
G1 X65.5 Y105.9 F400
G1 Y108.9 F400
G1 X64.5 Y108.9 F400
G1 X64.5 Y105.9 F400
G1 X65.5
G1 Y108.9
G1 X64.5
G1 Y105.9
G0 Z2
G0 X64.5 Y105.9
G0 Z1
G1 Z-2.625 F120
G1 X65.5 Y105.9 F400
G1 Y108.9 F400
G1 X64.5 Y108.9 F400
G1 X64.5 Y105.9 F400
G1 X65.5
G1 Y108.9
G1 X64.5
G1 Y105.9
G0 Z2
G0 X64.5 Y105.9
G0 Z1
G1 Z-3.5 F120
G1 X65.5 Y105.9 F400
G1 Y108.9 F400
G1 X64.5 Y108.9 F400
G1 X64.5 Y105.9 F400
G1 X65.5
G1 Y108.9
G1 X64.5
G1 Y105.9
G0 Z2
G0 Z25
(G2 spring pocket, 6 wide, z 92.9 to 102.9, 3.5 deep)
G0 X65 Y95.9
G0 Z2
G1 Z-0.875 F120
G1 X65 Y102.9 F400
G0 Z2
G0 X65 Y95.9
G1 Z-1.75 F120
G1 X65 Y102.9 F400
G0 Z2
G0 X65 Y95.9
G1 Z-2.625 F120
G1 X65 Y102.9 F400
G0 Z2
G0 X65 Y95.9
G1 Z-3.5 F120
G1 X65 Y102.9 F400
G0 Z2
G0 X65 Y95.9
G0 Z25
M5
M9
G0 Z25
G0 Z50
M30
%
