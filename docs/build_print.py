"""Rebuild the printable docx from a Claude Docs docx export: A4, header/footer, equations as images, full-width tables.
Usage: python3 build.py <export.json docx> <export.json md> <out.docx> <repo design-doc.md> <date text>"""
import json, base64, re, sys
import docx
from docx.shared import Mm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

EQ = '/tmp/claude-0/-home-claude/e34ac547-9d25-5693-9c29-89aaaa1dff19/scratchpad/print2/eq/'


def load(f):
    j = json.load(open(f))
    t = ''.join(x['text'] for x in j if x['type'] == 'text')
    return base64.b64decode(re.search(r'"bytes_b64":"([A-Za-z0-9+/=]+)"', t).group(1))


jdocx, jmd, out, mdout, date = sys.argv[1:6]
open('export.docx', 'wb').write(load(jdocx))
md = load(jmd).decode()
m = {'Side plate': 'side-plate', 'Fork plate': 'fork-plate', 'Head-top base plate': 'base-plate',
     'Cylinder mount plate': 'mount-plate', 'Roof block': 'roof-block', 'Roof wear plate': 'wear-plate',
     'Rear thrust bar': 'thrust-bar', 'Rear stop block': 'stop-block', 'Float lug': 'lug', 'Roller cage': 'roller-cage'}


def r(mo):
    alt = mo.group(1)
    for k, v in m.items():
        if alt.startswith(k):
            return f'![{alt}](../drawings/plate-parts/{v}.png)'
    return mo.group(0)


md = re.sub(r'&#91;image: ([^\]\\]*– dimensioned drawing)\\\]', r, md)
open(mdout, 'w').write(md)

d = docx.Document('export.docx')
eqtext = {'F_d = F_{stack}': 'eq201', 'F_{cyl} \\ge': 'eq202', 'D = \\sqrt': 'eq203', 'h_{cyl} \\ge': 'eq204', 's_p + s_r \\le': 'eq205'}
for p in d.paragraphs:
    for k, v in eqtext.items():
        if p.style.name == 'Code' and p.text.startswith(k):
            for rr in list(p.runs):
                rr._r.getparent().remove(rr._r)
            p.style = d.styles['Normal']
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(EQ + v + '.png', height=Mm(14))
for s in d.sections:
    s.page_width = Mm(210); s.page_height = Mm(297)
    s.left_margin = s.right_margin = Mm(18); s.top_margin = Mm(20); s.bottom_margin = Mm(18)
    hp = s.header.paragraphs[0]; hp.text = f'SX2.3 Power Drawbar – Design (printed {date})'; hp.runs[0].font.size = Pt(8)
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
    if lay is not None:
        pr.remove(lay)
d.save(out)
print('built', out)
