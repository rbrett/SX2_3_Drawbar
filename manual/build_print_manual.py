import json, base64, re, sys
import docx
from docx.shared import Mm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
def load(f):
    j = json.load(open(f))
    return base64.b64decode(j['data']['bytes_b64'])
jdocx, jmd, out, mdout, date = sys.argv[1:6]
open('export.docx', 'wb').write(load(jdocx))
md = load(jmd).decode()
blob = {'c737813b-ffef':'manual/img/drawbar.png','66c5bbbb-32d2':'manual/img/small-parts.png','358775f0-169d':'manual/img/collar.png',
 '2b78811c-4500':'manual/img/wedge-anvil-design.png','964a84be-b127':'manual/img/roof-wear-cage-design.png','a04594ac-1faf':'manual/img/base-plate-guides.png',
 'f7cb09b2-b779':'manual/img/side-plates-fork-asm.png','972906bf-2613':'manual/img/cylinder.jpg','3f46a1e4-ed87':'manual/img/pneumatic.png','4c0f04fb-4ce2':'manual/img/wiring.png',
 'b77e5b61-fde4':'manual/img/asm-side-view.png','dcf6427d-7524':'manual/img/asm-exploded.png'}
open(mdout, 'w').write(md)
d = docx.Document('export.docx')
for s in d.sections:
    s.page_width = Mm(210); s.page_height = Mm(297)
    s.left_margin = s.right_margin = Mm(18); s.top_margin = Mm(20); s.bottom_margin = Mm(18)
    hp = s.header.paragraphs[0]; hp.text = f'SX2.3 Power Drawbar – Build Manual (printed {date})'; hp.runs[0].font.size = Pt(8)
    fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = fp.add_run('Page '); r1.font.size = Pt(8)
    r2 = fp.add_run(); r2.font.size = Pt(8)
    for t, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
        if t:
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), t)
        else:
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt
        r2._r.append(e)
maxw = Mm(174)
for sh in d.inline_shapes:
    if sh.width > maxw:
        ratio = maxw / sh.width; sh.width = int(maxw); sh.height = int(sh.height * ratio)
for t in d.tables:
    pr = t._tbl.tblPr
    w = pr.find(qn('w:tblW'))
    if w is None:
        w = OxmlElement('w:tblW'); pr.append(w)
    w.set(qn('w:type'), 'pct'); w.set(qn('w:w'), '5000')
    lay = pr.find(qn('w:tblLayout'))
    if lay is not None: pr.remove(lay)
d.save(out)
print('built', out, len(d.inline_shapes), 'images', len(d.tables), 'tables')
