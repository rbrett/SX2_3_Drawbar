r"""Replace '&#91;image: alt\]' placeholders in the Claude Docs markdown export of the build manual with repo image links.
Usage: python3 md_images.py build-manual.md"""
import re, sys
M = [('Axonometric view', '../drawings/axonometric/drawbar-axonometric.png'), ('Side view of the assembled', 'img/asm-side-view.png'),
     ('Exploded view', 'img/asm-exploded.png'), ('Drawbar machining', 'img/drawbar.png'), ('Small parts', 'img/small-parts.png'),
     ('Collar machining', 'img/collar.png'), ('Wedge and anvil design', 'img/wedge-anvil-design.png'),
     ('Wedge machining', '../drawings/plate-parts/wedge.png'), ('Anvil machining', '../drawings/plate-parts/anvil.png'),
     ('Roof wear plate drawing', '../drawings/plate-parts/wear-plate.png'), ('Side plate (2 off', '../drawings/plate-parts/side-plate.png'),
     ('Fork plate', '../drawings/plate-parts/fork-plate.png'), ('Head-top base plate', '../drawings/plate-parts/base-plate.png'),
     ('Cylinder mount plate', '../drawings/plate-parts/mount-plate.png'), ('Roof block (1 off)', '../drawings/plate-parts/roof-block.png'),
     ('Rear thrust bar', '../drawings/plate-parts/thrust-bar.png'), ('Rear stop block', '../drawings/plate-parts/stop-block.png'),
     ('Float lug', '../drawings/plate-parts/lug.png'), ('Roller cage', '../drawings/plate-parts/roller-cage.png'),
     ('Base plate and float', 'img/base-plate-guides.png'), ('Side plates and fork plate', 'img/side-plates-fork-asm.png'),
     ('Roof block, wear plate', 'img/roof-wear-cage-design.png'), ('SDA 80', 'img/cylinder.jpg'),
     ('Pneumatic and control', 'img/pneumatic.png'), ('Control wiring', 'img/wiring.png')]
def r(mo):
    alt = mo.group(1)
    for k, v in M:
        if alt.startswith(k):
            return f'![{alt}]({v})'
    print('UNMAPPED', alt)
    return mo.group(0)
p = sys.argv[1]
s, n = re.subn(r'&#91;image: ([^\n\\]*?)\\?\]', r, open(p).read())
open(p, 'w').write(s)
print(n, 'images linked')
