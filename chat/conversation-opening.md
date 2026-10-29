# Conversation — opening turns (verbatim)

Source chat: "Pneumatic drawbar for Sieg SX2.3" (224 turns, 25–30 Oct 2026). Turns 0–4 are reproduced verbatim below; tool-call blocks are kept as they appeared. The rest of the conversation is summarised in [CONTEXT.md](CONTEXT.md) and its outcome is the design doc in [../docs/design-doc.md](../docs/design-doc.md).


---

## Turn 0 — User

I have a Sieg sx 2.3 milling machine that I want to create an pneumatic drawbar for, using bevel washers.  Are there any designs out there that we can copy or use as a foundation?


---

## Turn 1 — Claude

I'll check what I have on your mill, then search for existing SX2-family pneumatic drawbar designs.
`[tool: mcp__memory__memory_read]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebSearch]`
`[tool: WebFetch]`
`[tool: WebFetch]`
The X2-family and G0704 communities have solved this several times, and those designs are good starting points. Two things about your SX2.3 decide which one to copy, so confirm those first.

## Check these first

**1. Which spindle taper you have.** Sieg's SX2.3 manual lists MT#3 or R8. A push-to-release drawbar relies on the ability of a MT3 or R8 collet, when pushed from the rear of the collet, to relax its hold on a parallel 3/4″ shaft, enough for gravity to drop the tool holder, which is the Tormach TTS approach. That works with MT3 only if you use a TTS-style MT3 collet holding 3/4" shanks, which Tormach also make (part #30251). Plain MT3 tooling (chucks, arbors) self-holds and won't drop out reliably. R8 is the easier path. In Sieg-market tooling, the MT3 drawbar thread is typically M12 and R8 is 7/16" UNF. That sets the bore of your Belleville washers.

**2. The quill.** The SX2.3 has 45 mm of spindle travel, so it has a moving quill. Some designs push straight down on the drawbar, so the spindle bearings and quill lock carry the release force. Hoss's "floating" design exists for exactly this reason: it was originally created for the X3 which like the G0704 has a moving quill, and X3's had a real problem with the lock even being able to resist the force from low power direct acting pdb's. For your machine, copy a floating or "squeeze" design, one that reacts the force against the spindle itself, rather than a plain push-down one.

## Designs worth using

**Hoss X2 PDB (the original).** Hoss built this for his X2 in 2007 as the core of an automatic tool changer. He posted free plans with a complete parts list and a total cost of about $50 US. The catch is that at one time Hoss provided The X2 PDB drawings on his website. Unfortunately this information is no longer available. The Wayback Machine may have hossmachine.info archived, but I haven't checked.

**CNC4XR7 X2 PDB kit (a commercial version of Hoss's design).** It includes Correct Belleville Spring washers ( 6 ), Bimba Air cylinder, Lever arm 304 Stainless Steel, 6061 Side / Top plate and is available for Seig X2 , X2XD, or LMS 3990 at USD $195. They note the OEM Draw bar nut may need to be shortened for proper clearance. It's not listed for the SX2.3. The SX2.3 parts list uses X2.3-prefixed part numbers, but I can't confirm its spindle top or head casting matches the X2. Check the bolt pattern and spindle stick-up before buying, or just use it as reference geometry.

**Hoss G0704 PDB v2 / PDB3 (floating lever).** This is the closest match for your quill situation. One builder who used PDB v2 noted it puts no force on the spindle bearings, and that it works by clamping the tophat. Hoss says the lever version can provide a large force to compress the bellevilles with a single stage and more affordable sized air cylinder. The plans were posted as free for the asking on g0704.com. I haven't checked whether they're still up. That same builder warns that mechanical advantage cuts both ways: he forgot about the 1.76 multiplier and actually bent the steel lifting plate with 4000 lbs of force (on a hydraulic variant).

**DJ Bird design, built on a Sieg SX2.** This is the closest documented build to your machine. The builder's design is based on a design by DJ Bird, with the plans posted as a CNCzone attachment. He substituted a bought Fabco AA-521-X 1/4″ stroke air cylinder instead of making one. Part 2 of his write-up covers the plate and posts.

**Shane Wighton, X2 wedge design.** This one uses a wedge for force multiplication instead of a lever, and it's compact. The spring pack is a stack of eight belleville washers in series, and he ended up ordering spare belleville springs used on a tormach. He solved the bearing-load problem with a flange built into the spindle that the drawbar pulls against with a gap so that the drawbar isn't touching when the spindle is moving. The plans were never published, but the write-up is a good architecture reference.

**Tormach, for scale.** The TTS cylinder is a Pneumatic Cylinder, Double Acting, 100 mm Bore, 12 mm Stroke, 3-Stack. That's the size you need if you don't use leverage. The Tormach 31319 - Power DB Spring Washer fits a 7/16" drawbar and is a known-good Belleville washer for the R8 case.

## Design traps others have documented

- **Clamp force:** for a machine your size, Hoss's advice is If you want to use bigger endmills or flycutters shoot for 1500-2000lbs. 2500 or more is just overkill on such a small machine.
- **Series vs parallel stacking:** Belleville spring washers stacked in series do not increase the working load, it simply increases the deflection distance. Parallel stacking multiplies force. A mixed stack like `((()))((()))` gives you both.
- **Release force is higher than clamp force,** because the washers are already preloaded and you have to compress them further. One CNCzone poster warns the Belleville force increases almost exponentially once you go beyond the rated compression, which can easily make the required release force 2X the working tension. Size the cylinder or lever for release force at full stroke, and check washer fatigue life against your expected cycle count. Use the DIN 2093 / DIN EN 16983 load-deflection curves for this, not the nominal rating.
- **Cylinder damping:** fit exhaust flow restrictors. Without them the action of the air cylinder is extremely fast & rough which likely would damage the mechanism.
- **Interlock:** one builder used electric air solenoid valves rather than manual valves so I could enable the Power Draw Bar only when the spindle is not turning as a safety feature. That's worth doing.

## Recommended path

Take the Hoss G0704 floating-lever architecture (PDB v2/PDB3), use the CNC4XR7 X2 kit and the Sieg SX2 build as dimensional references, and size the washer stack yourself. My reasons, which are judgement rather than anything sourced: it's the only proven family designed for a moving quill, a single-stage cylinder is cheap and easy to get here, and lever geometry is easy to adapt to an unknown spindle top.

If you send me the taper you have, the spindle OD and stick-up above the head casting, the existing drawbar thread and head height, and your regulator pressure, I'll size a DIN 2093 washer stack, the stacking arrangement, the lever ratio and the cylinder bore against a ~1,500–2,000 lbf clamp target.

Sources:
- [SX2.3 manual EN (SIEG-Machines Germany)](https://www.sieg-machines.de/mediafiles/Sonstiges/SX2.3%20manual%20EN.pdf)
- [Power Drawbar – Part 1, Design (Sieg SX2 build, DJ Bird design)](https://blog.hslracing.com/workshop/2020/06/power-drawbar-part-1-design-plate-and.html)
- [CNC4XR7 X2 PDB kit](https://cnc4xr7.com/x2-mini-mill-parts-kit.php)
- [Hoss — Power Drawbar for the Minimill (HSM BBS)](https://bbs.homeshopmachinist.net/forum/general/26834-power-drawbar-for-the-minimill)
- [G0704 Power Drawbar Question (CNCzone, Hoss on floating design)](https://www.cnczone.com/forums/benchtop-machines/322024-forum.html)
- [Hoss's G0704 archive, p.12 (CNCzone)](https://www.cnczone.com/forums/archive/index.php/t-111863-p-12.html)
- [LinuxCNC G0704: Hydraulic Power Drawbar](http://linuxcnc-g0704.blogspot.com/2014/09/hydraulic-power-drawbar.html)
- [Shane Wighton — Power Drawbar for X2 Mini Mill](https://shane.engineer/blog/power-drawbar-x2-mini-mill)
- [Tormach power drawbar parts lists](https://docs.tormach.com/Content/Online-Only/power_drawbar_diagrams_parts_lists.htm)
- [Manual Power Drawbar (CNCArena, Hoss force guidance)](https://en.cncarena.com/forum/thread/311013-manual-power-drawbar/)
- [Power draw bar idea – Feasible? (CNCzone)](https://www.cnczone.com/forums/benchtop-machines/171662-power-draw-bar-idea-feasible.html)
- [Shop-built CNC mill PDB (Hobby-Machinist)](https://www.hobby-machinist.com/threads/shop-built-cnc-mill-project.105358/latest)
- [viking45 PDB posts (CNCArena)](https://de.cncarena.com/forum/user-post-list/330656-viking45/)
- [Ausee Sieg tooling store (thread references)](https://www.ebay.de/str/auseeptyltd)


---

## Turn 2 — User

I have a R8 taper, that I will have a R8 19mm collet installed in on the draw bar, and I intend to use my TTS tooling systems, that plug into the R8 collet.


---

## Turn 3 — Claude

`[tool: WebSearch]`
`[tool: WebSearch]`
R8 with TTS is exactly what the designs I listed were built for: the drawbar only needs pushing down, not rotating. One part of your plan needs checking before you design around it: the 19 mm collet.

## The 19 mm collet versus 3/4" TTS shanks

TTS holders have 3/4" shanks (19.05 mm), held in a modified R8 collet whose tip is ground flatter than a normal R8 collet, so that it does not protrude from the nose of the spindle when drawn in by the drawbar. There are two possible problems with a standard 19 mm metric collet:

1. **Bore size (my reasoning, not from a source).** A true 19.00 mm bore is nominally 0.05 mm under a 19.05 mm shank. With a push-release drawbar the holder has to slide in and drop out freely when the collet is pushed open. For reference, one Tormach ATC user reports about 0.030" radial clearance when the collet is open around the 0.750" TTS shank. An undersize bore eats into that, and you may find holders sticking or needing a shove to seat. Measure your collet's bore before relying on it.
2. **Tool-length repeatability.** The modification to the TTS collet consists of removing a small amount from the face of the collet so the TTS holder seats against the spindle face. That is what gives TTS repeatable tool lengths. If your collet's nose sticks out of the SX2.3 spindle, the holder's shoulder will land on the collet face instead of the spindle, and tool length will vary with drawbar force. I haven't verified how far a standard collet protrudes from the SX2.3 spindle. Check with a holder fitted and the drawbar tight.

The low-risk fix is a proper TTS adapter collet, Tormach 50568, which has a 7/16-20 UNF thread. Check your drawbar thread first. Some Sieg R8 machines may use M12 rather than 7/16-20; I haven't confirmed which the SX2.3 uses. That thread also sets the bore of your Belleville washers.

## Design requirements that come from TTS

- **Release stroke.** A TTS drawbar only needs to push the collet down about 1/4" to release the tool. On the Tormach, the R8 collet should only protrude 1/8" or less from the spindle nose when open, and the gap between the actuator and the drawbar is set to about the same. Design your cylinder or lever for roughly 3–6 mm of usable stroke at the drawbar, with the lever ratio chosen to suit.
- **Clamp force.** Hoss's figure for TTS on small machines is 1,500–2,000 lbf (about 6.7–8.9 kN), and he regards 2,500+ as overkill for this size of mill. One commercial drawbar maker says pull-out isn't a TTS weakness as long as the drawbar tension is adequate, and blames slipping tools on worn spindle tapers or weak springs.
- **Never leave the spindle empty.** With no holder fitted, the springs will pull the R8 collet deep inside the spindle, which will cause fatigue and eventual failure of the collet. You can engineer this out with a hard stop that limits how far the drawbar can rise. That's my suggestion rather than something from the sources, but it's cheap insurance on a home-built unit.
- **Collets wear out.** Tormach users recommend replacing the spindle collet annually. A worn one stops opening fully and holders stop dropping out. Allow for it in the design.

## The washer stack check

Whatever washer you choose, the stack has to do two things. At installed height it must give your target clamp force. When the release stroke is added, it must still stay within the washer's allowable deflection: commonly about 75% of free cone height for fatigue life, though you should confirm that limit on the supplier's DIN 2093 / EN 16983 datasheet. If you only check the force, release ends up much harder than clamping and the washers fatigue early. For a known-good starting point, Tormach's 31319 washers suit a 7/16" drawbar. One documented build stacked 6 washers in series to get 0.150" total deflection.

## Recommendation

My recommendation is unchanged: use a floating lever design, adapting Hoss's G0704 arrangement, because the SX2.3 has a quill. With TTS confirmed, the force and stroke targets are now set.

To size the washer stack, lever ratio and cylinder, I need:
- your drawbar thread (7/16-20 or M12) and its overall length
- the spindle OD and how far it sticks up above the head casting or pulley
- the free height available above the spindle, under any cover
- the bore of your 19 mm collet, if you're keeping it
- your regulator pressure

Sources:
- [MakeIt Labs wiki – Tormach tool holding (TTS collet, empty-spindle warning)](https://sites.google.com/a/makeitlabs.com/wiki/resource-areas/machine-shop/tormach-pcnc1100-cnc-milling-machine/tool-holding)
- [Tormach TTS Adapter Collet R8, PN 50568](https://tormach.com/tts-adapter-collet-r8-50568.html)
- [Hobby-Machinist – R8 quick change collets (TTS collet modification)](https://hobby-machinist.com/threads/r8-quick-change-collets.66913/page-3)
- [Hobby-Machinist – TTS PDB push stroke](https://www.hobby-machinist.com/goto/post?id=839021)
- [CNCArena – astro_eng posts (collet stickout, open clearance)](https://en.cncarena.com/forum/user-post-list/605902-astro-eng/)
- [CNCArena – R8 taper a question (drawbar tension, pull-out)](https://en.cncarena.com/forum/thread/288023-r8-taper-a-question/)
- [Tormach forum – TTS holder won't come out of R8 collet](https://forums.tormach.com/t/tts-holder-wont-come-out-of-r8-collet/1001)
- [CNCArena – Manual Power Drawbar (Hoss force guidance)](https://en.cncarena.com/forum/thread/311013-manual-power-drawbar/)
- [CNCArena – viking45 posts (Tormach 31319 washers)](https://de.cncarena.com/forum/user-post-list/330656-viking45/)
- [Hobby-Machinist – shop-built CNC mill PDB](https://www.Hobby-machinist.Com/threads/shop-built-cnc-mill-project.105358/latest)


---

## Turn 4 — User

M12 drawbar.  I will need to measure the rest, and the regulator pressure can be set to whatever we need.  I can also grind the face of the collet so it doesn't protrude, if that is a problem, but I will measure the ability for the TTS adapters to release, otherwise I will go purchase the genuine collet for the job.
