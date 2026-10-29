from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
F='Arial'
blue=Font(name=F,color='0000FF'); black=Font(name=F); bold=Font(name=F,bold=True)
title=Font(name=F,bold=True,size=13); note=Font(name=F,italic=True,color='595959')
hdr=PatternFill('solid',fgColor='D9E1F2'); yel=PatternFill('solid',fgColor='FFFF00')
thin=Side(style='thin',color='BFBFBF'); box=Border(left=thin,right=thin,top=thin,bottom=thin)
wb=Workbook()
wi=wb.active; wi.title='Inputs'
wd=wb.create_sheet('Design'); ws=wb.create_sheet('Stroke scenarios'); wo=wb.create_sheet('Wedge and pressure'); wn=wb.create_sheet('Notes')

# ---------- Inputs ----------
wi['A1']='Design inputs: change the blue cells'; wi['A1'].font=title
wi['A2']='Yellow = measurement still pending; replace when measured.'; wi['A2'].font=note
for j,h in enumerate(['Input','Value','Unit','Source / status'],1):
    c=wi.cell(3,j,h); c.font=bold; c.fill=hdr; c.border=box
inputs=[
 ('sr','Release stroke at the drawbar, s_r',1.2,'mm','Assumed; replace with the release test (sheet section 5)',True),
 ('g','Running gap, anvil to push pad',1.0,'mm','Design choice (anvil lift springs)',False),
 ('W','Preload target, W',8.2,'kN','Hoss guidance 6.7-8.9 kN for TTS on small mills',False),
 ('P','Collet push-out force, P',0.5,'kN','Assumed; first feel from the taper break test',True),
 ('Ff','Washer flat load',14.2,'kN','Tormach 31319 not published: Solon 7H89 rate (23.6 kN/mm) x 0.6 mm h0',True),
 ('h0','Washer cone height, h0',0.6,'mm','Tormach 31319, measured by viking45 (2.9 - 2.3 mm)',True),
 ('l0','Washer free height, l0',2.9,'mm','Tormach 31319, measured by viking45; measure your own',True),
 ('lim','Release deflection limit',0.9,'x h0','Keeps the washers off flat; Tormach runs them deep',False),
 ('n','Washers fitted, n',8,'pcs','Locked: 8 x genuine Tormach 31319, as Tormach fits',False),
 ('mw','Washer mass each',11,'g','Calculated from 31319 dimensions',False),
 ('price','Washer unit price',4.95,'US$','Tormach 31319 listed price',False),
 ('nbuy','Washers to buy',16,'pcs','Two Tormach sets of 8: stack plus spares',False),
 ('D','Cylinder bore',80,'mm','SDA 80 x 25 (owned)',False),
 ('S','Cylinder stroke',25,'mm','SDA 80 x 25 (owned)',False),
 ('d','Cylinder rod diameter',25,'mm','Measured 28 Oct 2026',False),
 ('p','Regulator setting',5.0,'bar','Design setting',False),
 ('pmax','Supply pressure, maximum',6.2,'bar','90 psi supply',False),
 ('th','Wedge angle',9.5,'deg','Design: tan 9.5 deg is about 1/6',False),
 ('eta','Wedge efficiency (rolling)',0.9,'','Assumed; rollers make friction small',False),
 ('hold','Collar axial holding, estimate',14,'kN','Estimate for two-piece collar, 3 x M8 12.9 per side',False),
 ('H','Drawbar tip to spindle end face, H',250,'mm','From existing drawbar; confirm with new collet (sheet 3.5)',True),
 ('L1','Lower thread length, L1',18,'mm','Collet thread depth + 3; placeholder (sheet 3.7)',True),
 ('sh','Collar shoulder thickness',6,'mm','Collar design',False),
 ('tb','Base thrust washer',3,'mm','Design',False),
 ('tt','Top thrust washer',4,'mm','Design',False),
 ('tth','Top thread length',28,'mm','Nut, jam nut, adjustment, pad',False),
 ('rd','Roller diameter',14,'mm','Dowel pins, ISO 8734, 58-62 HRC (purchased)',False),
 ('rl','Roller contact length (flat, between end chamfers)',36,'mm','36 mm pins; measure the flat length and enter it',True),
 ('nr','Rollers per face',2,'pcs','Design',False),
 ('E','Young\'s modulus, steel',210,'GPa','Standard value',False),
 ('nu','Poisson\'s ratio, steel',0.3,'','Standard value',False),
 ('Yh','Track yield, hardened 4140 (wedge, anvil)',1380,'MPa','Atlas 4140 datasheet: yield above 1380 MPa when tempered 175-230 C',False),
 ('Ys','Track yield, 4140 as supplied',740,'MPa','Atlas 4140 datasheet: condition U, 0.2% proof 740 MPa min (bar to 180 mm)',False),
 ('ky','Line-contact first yield, p0 / yield',1.79,'','Johnson, Contact Mechanics (1985), von Mises; from memory',False),
 ('tw','Wedge thickness at the trailing end',23.5,'mm','Wedge drawing',False),
 ('hc','Hole centre below the wedge top',11.75,'mm','Wedge drawing (centred)',False),
 ('Dt','Rod-joint thread, major diameter',14,'mm','M14 x 1.5 (rod re-measured 29 Oct 2026; SMC JA40-14-150)',False),
 ('lt','Thread depth in the wedge',14,'mm','Wedge drawing',False),
 ('Dd','Tap drill diameter',12.5,'mm','M14 x 1.5 tap drill',False),
 ('ld','Drill depth',18,'mm','Wedge drawing',False),
 ('tp','Roof wear plate thickness',5,'mm','O1 40 x 5 ground flat stock (ordered 29 Oct 2026)',False),
 ('S2','Hard stop beyond the release stroke',0.3,'mm','Design: stop at s_r + 0.3',False),
]
ref={}
for k,(key,lab,val,unit,src,pend) in enumerate(inputs):
    r=4+k; ref[key]=f'Inputs!$B${r}'
    wi.cell(r,1,lab).font=black
    c=wi.cell(r,2,val); c.font=blue
    if pend: c.fill=yel
    wi.cell(r,3,unit).font=black; wi.cell(r,4,src).font=note
    for j in range(1,5): wi.cell(r,j).border=box
wi.column_dimensions['A'].width=38; wi.column_dimensions['B'].width=10; wi.column_dimensions['C'].width=8; wi.column_dimensions['D'].width=62
R=ref

# ---------- Design ----------
wd['A1']='Design results for the current inputs'; wd['A1'].font=title
wd['A2']='All formulas; washer force taken as linear, flat load / h0 (Solon 7H89 at low cone height).'; wd['A2'].font=note
for j,h in enumerate(['Result','Value','Unit','Check'],1):
    c=wd.cell(3,j,h); c.font=bold; c.fill=hdr; c.border=box
rows=[]
def add(key,lab,f,unit,fmt='0.00',chk=None):
    rows.append((key,lab,f,unit,fmt,chk))
add('i','Mechanical advantage, 1/tan(angle)',f'=1/TAN(RADIANS({R["th"]}))','','0.00')
add('k','Washer rate, per washer',f'={R["Ff"]}/{R["h0"]}','kN/mm','0.0')
add('sp','Preload deflection per washer',f'={R["W"]}/{{k}}','mm','0.000')
add('spf','Preload deflection',f'={{sp}}/{R["h0"]}','x h0','0.00')
add('nmin','Washers needed for the limit at this stroke',f'=ROUNDUP({R["sr"]}/(({R["lim"]}-{{spf}})*{R["h0"]}),0)','pcs','0')
add('srel','Release deflection per washer',f'={{sp}}+{R["sr"]}/{R["n"]}','mm','0.000')
add('srf','Release deflection',f'={{srel}}/{R["h0"]}','x h0','0.00',f'=IF({{srf}}<={R["lim"]},"OK","Add washers")')
add('Frel','Stack force at release',f'=MIN({{k}}*{{srel}},{R["Ff"]})','kN','0.0')
add('Fd','Required at drawbar, incl. P',f'={{Frel}}+{R["P"]}','kN','0.0')
add('A','Bore area',f'=PI()*{R["D"]}^2/4','mm2','0')
add('Fc','Cylinder push at regulator',f'={{A}}*{R["p"]}/10/1000','kN','0.00')
add('Fav','Drawbar force available',f'={{Fc}}*{{i}}*{R["eta"]}','kN','0.0')
add('mar','Release margin',f'={{Fav}}/{{Fd}}-1','','0%',f'=IF({{mar}}>=0.1,"OK",IF({{mar}}>=0,"Thin","Will not release"))')
add('prel','Expected release pressure',f'={{Fd}}*1000/({{A}}*{{i}}*{R["eta"]})*10','bar','0.0',f'=IF({{prel}}<={R["p"]}-0.5,"OK","Thin: under 0.5 bar headroom")')
add('trav','Wedge (cylinder) travel needed',f'={{i}}*({R["sr"]}+{R["g"]})','mm','0.0',f'=IF({{trav}}<={R["S"]}-3,"OK","Short of stroke")')
add('srmax','Largest stroke the cylinder covers',f'=({R["S"]}-3)/{{i}}-{R["g"]}','mm','0.0')
add('Lfree','Stack free length',f'={R["n"]}*{R["l0"]}','mm','0.0')
add('Lpre','Stack preloaded length (set to this)',f'={R["n"]}*({R["l0"]}-{{sp}})','mm','0.0')
add('ztop','Top thrust washer top above spindle face',f'={R["sh"]}+{R["tb"]}+{{Lpre}}+{R["tt"]}','mm','0.0')
add('Ldb','Drawbar overall length',f'={R["H"]}+{{ztop}}+{R["tth"]}','mm','0')
add('Lg','Guide section length (11.2 mm)',f'=3+{{ztop}}','mm','0.0')
add('Lb','Body length (11.0 mm)',f'={R["H"]}-{R["L1"]}-3','mm','0')
add('Fcmax','Cylinder push at full supply',f'={{A}}*{R["pmax"]}/10/1000','kN','0.00')
add('cl','Stuck-collet collar load at regulator',f'={{Fav}}-{R["W"]}','kN','0.0')
add('clm','Collar margin at regulator',f'={R["hold"]}/{{cl}}','x','0.0',f'=IF({{clm}}>=2,"OK",IF({{clm}}>=1.5,"Thin","Low"))')
add('clx','Stuck-collet collar load at full supply',f'={{Fcmax}}*{{i}}*{R["eta"]}-{R["W"]}','kN','0.0')
add('clxm','Collar margin at full supply',f'={R["hold"]}/{{clx}}','x','0.0')
add('stop','Wedge travel to the hard stop',f'={{i}}*({R["sr"]}+{R["S2"]}+{R["g"]})','mm','0.0',f'=IF({{stop}}<={R["S"]}-3,"OK","Short of stroke")')
add('rtrav','Cage travel at the hard stop (half the wedge)',f'={{stop}}/2','mm','0.0')
add('Fdx','Drawbar force at full supply',f'={{Fcmax}}*{{i}}*{R["eta"]}','kN','0.0')
add('N','Normal load on each roller face, full supply',f'={{Fdx}}/COS(RADIANS({R["th"]}))','kN','0.0')
add('Est','Contact modulus E*',f'={R["E"]}*1000/(2*(1-{R["nu"]}^2))','MPa','0')
add('ph5','Hertz peak, rollers sharing, at regulator',f'=SQRT({{Fav}}/COS(RADIANS({R["th"]}))*1000/{R["nr"]}*{{Est}}/(PI()*{R["rl"]}*{R["rd"]}/2))','MPa','0')
add('ph','Hertz peak, rollers sharing, full supply',f'=SQRT({{N}}*1000/{R["nr"]}*{{Est}}/(PI()*{R["rl"]}*{R["rd"]}/2))','MPa','0',f'=IF({{ph}}<={R["ky"]}*{R["Ys"]},"OK even unhardened",IF({{ph}}<={R["ky"]}*{R["Yh"]},"OK hardened","Yields"))')
add('ph1','Hertz peak, one roller takes all, full supply',f'=SQRT({{N}}*1000*{{Est}}/(PI()*{R["rl"]}*{R["rd"]}/2))','MPa','0',f'=IF({{ph1}}<={R["ky"]}*{R["Ys"]},"OK even unhardened",IF({{ph1}}<={R["ky"]}*{R["Yh"]},"OK hardened only","Yields: grind faces parallel"))')
add('pyh','First-yield contact pressure, hardened 4140',f'={R["ky"]}*{R["Yh"]}','MPa','0')
add('myh','Margin, one roller takes all, hardened',f'={{pyh}}/{{ph1}}','x','0.00',f'=IF({{myh}}>=1.3,"OK","Thin")')
add('pys','First-yield contact pressure, 4140 as supplied',f'={R["ky"]}*{R["Ys"]}','MPa','0')
add('mys','Margin, rollers sharing, as supplied',f'={{pys}}/{{ph}}','x','0.00')
add('wt','Wedge hole: wall to the slope at thread bottom',f'=({R["tw"]}-{R["lt"]}*TAN(RADIANS({R["th"]})))-({R["hc"]}+{R["Dt"]}/2)','mm','0.00',f'=IF({{wt}}>=2,"OK","Thin")')
add('wd','Wedge hole: wall to the slope at drill bottom',f'=({R["tw"]}-{R["ld"]}*TAN(RADIANS({R["th"]})))-({R["hc"]}+{R["Dd"]}/2)','mm','0.00',f'=IF({{wd}}>=2,"OK","Thin")')
add('wtop','Wedge hole: wall to the top face',f'={R["hc"]}-{R["Dt"]}/2','mm','0.00')
add('rbh','Roof block height to keep the plate face fixed',f'=24-{R["tp"]}','mm','0')
add('Fh','Anvil forward thrust, full supply',f'={{Fdx}}*TAN(RADIANS({R["th"]}))','kN','0.00')
add('air','Free air per release',f'=({{A}}+({{A}}-PI()*{R["d"]}^2/4))*{{trav}}*({R["p"]}+1.013)/1.013/1000000','L','0.00')
add('mass','Stack mass',f'={R["n"]}*{R["mw"]}','g','0')
add('cost','Washer cost',f'={R["nbuy"]}*{R["price"]}','US$','$#,##0.00')
pos={key:4+k for k,(key,*_) in enumerate(rows)}
def sub(s): 
    for key,r in pos.items(): s=s.replace('{'+key+'}',f'$B${r}')
    return s
for key,lab,f,unit,fmt,chk in rows:
    r=pos[key]
    wd.cell(r,1,lab).font=black
    c=wd.cell(r,2,sub(f)); c.font=black; c.number_format=fmt
    wd.cell(r,3,unit).font=black
    if chk: wd.cell(r,4,sub(chk)).font=bold
    for j in range(1,5): wd.cell(r,j).border=box
wd.column_dimensions['A'].width=42; wd.column_dimensions['B'].width=12; wd.column_dimensions['C'].width=8; wd.column_dimensions['D'].width=26
D={k:f'Design!$B${v}' for k,v in pos.items()}

# ---------- Stroke scenarios ----------
ws['A1']='Performance of the fitted stack by release stroke'; ws['A1'].font=title
ws['A2']='Uses the washer count fitted on Inputs (8). Release beyond the deflection limit or a negative margin means: fit a genuine Tormach collet or raise the regulator.'; ws['A2'].font=note
hs=['Release stroke (mm)','Washers fitted','Release deflection (x h0)','Release force (kN)','Required at drawbar (kN)','Margin at regulator','Expected release pressure (bar)','Preloaded stack (mm)','Drawbar length (mm)','Cylinder travel (mm)','Within deflection limit?','Margin at 5.5 bar']
for j,h in enumerate(hs,1):
    c=ws.cell(4,j,h); c.font=bold; c.fill=hdr; c.border=box; c.alignment=Alignment(wrap_text=True,vertical='top')
ws.row_dimensions[4].height=45
for k,s in enumerate([0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]):
    r=5+k
    ws.cell(r,1,s).font=blue
    ws.cell(r,2,f'={R["n"]}')
    ws.cell(r,3,f'=({D["sp"]}+A{r}/B{r})/{R["h0"]}')
    ws.cell(r,4,f'=MIN({D["k"]}*({D["sp"]}+A{r}/B{r}),{R["Ff"]})')
    ws.cell(r,5,f'=D{r}+{R["P"]}')
    ws.cell(r,6,f'={D["Fav"]}/E{r}-1')
    ws.cell(r,7,f'=E{r}*1000/({D["A"]}*{D["i"]}*{R["eta"]})*10')
    ws.cell(r,8,f'=B{r}*({R["l0"]}-{D["sp"]})')
    ws.cell(r,9,f'={R["H"]}+{R["sh"]}+{R["tb"]}+H{r}+{R["tt"]}+{R["tth"]}')
    ws.cell(r,10,f'={D["i"]}*(A{r}+{R["g"]})')
    ws.cell(r,11,f'=IF(C{r}<={R["lim"]},"Yes","No")')
    ws.cell(r,12,f'={D["A"]}*5.5/10/1000*{D["i"]}*{R["eta"]}/E{r}-1')
    fm=['0.00','0','0.00','0.0','0.0','0%','0.0','0.0','0','0.0','@','0%']
    for j in range(1,13):
        c=ws.cell(r,j); c.border=box; c.number_format=fm[j-1]
        if j>1: c.font=black
for j,w in enumerate([11,11,12,11,12,11,12,11,11,11,9,13],1):
    ws.column_dimensions[chr(64+j)].width=w

# ---------- Lever and pressure ----------
wo['A1']='Wedge angle and regulator options'; wo['A1'].font=title
wo['A2']='Release margin uses the required drawbar force from Design; collar load is the stuck-collet case.'; wo['A2'].font=note
ratios=[8.5,9.5,10.5]; press=[4.5,5.0,5.5,6.2]
def block(top,titletxt,formula,fmt):
    wo.cell(top,1,titletxt).font=bold
    wo.cell(top+1,1,'Wedge angle (deg) \\ bar').font=bold; wo.cell(top+1,1).fill=hdr; wo.cell(top+1,1).border=box
    for j,p in enumerate(press):
        c=wo.cell(top+1,2+j,p); c.font=blue; c.fill=hdr; c.border=box; c.number_format='0.0'
    for k,ri in enumerate(ratios):
        r=top+2+k; c=wo.cell(r,1,ri); c.font=blue; c.border=box
        for j in range(len(press)):
            col=chr(66+j)
            c=wo.cell(r,2+j,formula(f'$A{r}',f'{col}${top+1}')); c.number_format=fmt; c.border=box; c.font=black
force=lambda ri,p: f'={D["A"]}*{p}/10/1000/TAN(RADIANS({ri}))*{R["eta"]}'
block(4,'Drawbar force available (kN)',force,'0.0')
block(10,'Release margin over required drawbar force',lambda ri,p: f'={D["A"]}*{p}/10/1000/TAN(RADIANS({ri}))*{R["eta"]}/{D["Fd"]}-1','0%')
block(16,'Stuck-collet collar load (kN)',lambda ri,p: f'={D["A"]}*{p}/10/1000/TAN(RADIANS({ri}))*{R["eta"]}-{R["W"]}','0.0')
block(22,'Collar margin (estimated holding / load)',lambda ri,p: f'={R["hold"]}/({D["A"]}*{p}/10/1000/TAN(RADIANS({ri}))*{R["eta"]}-{R["W"]})','0.0')
block(28,'Wedge travel needed for the current stroke (mm), of 25',lambda ri,p: f'=1/TAN(RADIANS({ri}))*({R["sr"]}+{R["g"]})','0.0')
wo['A35']='Current design: 9.5 deg (about 6:1) at 5.0 bar. Aim for release margin of at least 10% and collar margin of at least 2.'; wo['A35'].font=note
wo.column_dimensions['A'].width=30
for col in 'BCDE': wo.column_dimensions[col].width=10

# ---------- Notes ----------
notes=['Notes and sources',
'Washers: 8 x genuine Tormach 31319 (30.2 x 11.4 x 2.3 mm, US$4.95, sets of 8). Load not published; rate taken from the same-size Solon 7H89177 (15.1 kN flat at 0.64 mm). https://www.solonmfg.com/7h89177',
'Tormach 31319 product page: https://tormach.com/power-drawbar-spring-washer-31319.html ; free height 2.9 mm measured by viking45 (CNCArena).',
'Tormach PCNC 1100 power drawbar uses 8 x 31319. https://tormach.com/media/asset/t/d/td10039_pcnc1100_powerdrawbar_1119a.pdf',
'Washer force is modelled as linear (flat load / h0); real Belleville curves are slightly regressive, so forces near flat are a little high here.',
'Collar holding (14 kN) is an engineering estimate, not a published rating; verify with the witness line.',
'Hertz line contact: p = sqrt(F E* / (pi L R)), E* = E / (2(1 - nu^2)); F per roller = normal face load / rollers per face. Enter the measured flat length of the pins as L.','Wedge geometry: drawbar force = cylinder force / tan(angle) x efficiency; anvil forward thrust = drawbar force x tan(angle), taken by the rear thrust bar (bronze faced).',
'Stack heights exclude the nut and pad; drawbar length = H + shoulder + base washer + preloaded stack + top washer + top thread.',
'Contact check (29 Oct 2026): first yield of a line contact at p0 = 1.79 x yield (von Mises; Johnson 1985, from memory). Wedge and anvil are 4140 hardened and tempered at about 200 C (Atlas: yield above 1380 MPa). https://atlassteels.com.au/wp-content/uploads/2021/09/Through-Hardening-Low-Alloy-Steel-Bar-4140-Grade-Data-Sheet-10-09-21-1.pdf',
'Floating joint SMC JA40-14-150, 4400 N max tension/compression. https://static.smc.eu/pdf/JA-A_EU.pdf . Wedge M14 x 1.5 hole kept to 14 deep thread, 18 deep drill so the 9.5 deg slope leaves at least about 2.4 mm wall; the JA nut bears on the end face.',
'Yellow inputs are pending measurements or unpublished data: release stroke, push-out force, washer rate and heights, rod diameter, H and L1.','If release needs more stroke than the 8-washer stack allows, fit a genuine Tormach collet before adding washers (design decision 28 Oct 2026).']
for k,t in enumerate(notes):
    wn.cell(1+k,1,t).font=title if k==0 else black
wn.column_dimensions['A'].width=140
wb.save('PDB_design_calculator.xlsx')
