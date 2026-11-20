"""Assemble scan 004 from the three returns and the main reader's crop decisions."""
from pathlib import Path
import json, copy

O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'records/scan004/reader_{a}/report.json').read_text()) for a in 'ABC'}
I={a:{x['id']:x for x in R[a]['issues']} for a in 'ABC'}
mapping={
1:('B01','T01'),2:('B02','T02'),3:('B05','T04'),4:('B06','T03'),
5:('B07','T07'),6:('B08','T08'),7:('B09','T09'),8:('B09','T10'),
9:('B12','T11'),10:('B10','T12'),11:('B11','T13'),12:('B13','T14'),13:('B14','T15'),
14:('B47|B48','G01'),15:('',''),16:('B49','G02'),17:('',''),18:('',''),19:('',''),
20:('B15','F01'),21:('B16','F02'),22:('B17','F03'),23:('B18','F04'),24:('B19','F05'),
25:('B18','F06'),26:('B20',''),27:('',''),28:('B21','F07'),29:('','G03'),
30:('B50','G04'),31:('B51',''),32:('B52','G05'),33:('B23','X01'),34:('B24','X02'),
35:('B25','X03'),36:('B25','X03'),37:('B26','I01'),38:('B28','I04'),39:('B27','I05'),
40:('B29','I03|I06'),41:('B29','I07'),42:('B30','I09'),43:('B31','I09'),44:('B32','I10'),
45:('B33','P01'),46:('B34','P02'),47:('B36',''),48:('B36',''),49:('B35','P03'),
50:('B37','P05'),51:('B39','P07'),52:('B40','P08'),53:('B41','P09'),54:('B42','P10'),
55:('B38','P06'),56:('B54','G06'),57:('B54','G06'),58:('B44','A01'),59:('B45','A02'),
60:('B46','A03'),61:('B46','A03'),62:('',''),63:('',''),64:('','')}

def rp(a,name):return f'records/scan004/reader_{a}/crops/{name}.png'
def mp(name):return f'crops/scan004_{name}.png'
crop_by_n={
1:rp('B','01_top_index'),2:rp('A','01_top_arrow'),3:mp('up_arrows'),4:rp('C','02_endpoint'),
5:rp('C','03_corrections'),6:rp('C','03_corrections'),7:rp('C','03_corrections'),8:rp('C','03_corrections'),
**{n:rp('A','04_third_row') for n in range(9,14)},
**{n:rp('A','13_prism') for n in range(14,20)},
**{n:rp('A','05_f3_row') for n in range(20,23)},
**{n:rp('A','06_fn_start') for n in range(23,28)},28:rp('C','17_Fn_factors'),29:mp('open_rectangle'),
30:rp('A','14_square'),31:rp('A','14_square'),32:mp('cylinder'),
**{n:rp('A','07_x_pair') for n in range(33,37)},37:mp('bullet'),
**{n:rp('B','11_inclusions') for n in range(38,42)},
**{n:rp('C','09_right_inclusion') for n in range(42,45)},
**{n:rp('A','10_product_question') for n in range(45,50)},50:rp('C','14_pair_alphabets'),
**{n:rp('C','11_last_pair') for n in range(51,55)},55:mp('pair_continuation'),
56:mp('lower_grid'),57:mp('lower_grid'),
**{n:rp('C','10_pushout') for n in range(58,62)},62:rp('C','02_endpoint'),
63:rp('B','11_inclusions'),64:rp('C','14_pair_alphabets')}

def reading(a,ids,default):
    return '; '.join(I[a][i]['reading'] for i in ids.split('|')) if ids else 'Retained witness C in reading.tex: '+default
issues=[]
for n,(b,c) in mapping.items():
    x=copy.deepcopy(I['A'][f'004A{n:02d}'])
    x['final']=x.pop('reading')
    x['readers']={'A':x['final'],'B':reading('B',b,x['C']),'C':reading('C',c,x['C'])}
    x['crop']=crop_by_n[n]
    x['marked_in_H']='yes' if n==59 else 'no'
    issues.append(x)
D={int(x['id'][-2:]):x for x in issues}
def upd(n,**kw):D[n].update(kw)

upd(1,consequential='Top source is Ob C_4, not H’s C_1; the transverse stroke resolves C’s 4/1 doubt.')
upd(3,diff_C=True,final='Two upward arrows; left shaft retraced, right head detached from its shaft, short lower feet.',
    evidence=D[3]['evidence']+' The main crop additionally shows a white gap between the right head and shaft and a long return beside the left shaft. All three readers use ordinary joined arrowheads; literal paths preserve the observed separation.')
upd(4,diff_C=True,final=r'\mathrm{Fl}_0(\ell_{\unsure{n|1}})',
    evidence='The argument is a tall closed ascending loop matching adjacent l, unlike the open C of the factors. Main resolves the letter to ell, pruning C-reader’s C alternatives and rejecting A/B’s fixed C. The low shouldered stroke favours n but also permits 1; it remains doubtful.',
    consequential='The top target argument is looped ell with unresolved n/1 index, not the witnesses’ C.')
upd(7,final=r'\mathbb F\mathrm l_0(\ell_1)\times\mathrm{Ob}\,C_2',
    evidence='The new lower F has two long uprights with a clear white channel. Its argument is a closed ascending loop, unlike an open C, followed by a separate low 1. Main resolves ell_1, choosing neither witness nor A/B’s C_1, and resolves C-reader’s ell_1/C_1 alternative. The term is live and inserted below the struck old group.',
    consequential='The live lower replacement has doubled F and ell_1. H omits the live line and the two witnesses use C_1 for its argument.')
upd(13,evidence=D[13]['evidence']+' Main chooses A’s F-first alternatives over B’s Fl-first order and C-reader’s unqualified old Fl; the old l cannot be isolated securely.')
upd(19,final=D[19]['final']+'; add short separate upper-right inner stroke near (1648,178)–(1647,189)',
    evidence=D[19]['evidence']+' Main also sees a short separate descending stroke beside the upper-right inner edge, missing in all three returns; it is added.')
upd(21,consequential='The F_3 product contains a literal < shaped sign, not H’s multiplication cross; C’s doubt is resolved.')
upd(22,final=r'\ell_3',consequential='Third F_3 argument is a closed looped ell_3, not H’s C_3; C’s l/C doubt is resolved.')
upd(24,final=r'\mathrel{2}',confidence='high',unresolved=False,
    evidence='The sign is one connected upper turn, diagonal descent and lower foot. No two detached equality bars are present. Main adopts C-reader’s literal 2-shaped glyph, resolving A/B’s 2/equals alternatives without substituting the expected equality.',
    consequential='The separator after F_n is literally 2-shaped; the formula is not repaired to equality.')
upd(27,consequential='After the first C_1 in the F_n row, the visible two-armed wedge is <; both witnesses give multiplication.')
upd(30,evidence=D[30]['evidence']+' Main adopts A’s irregular knot and small white-counter geometry; C-reader’s larger regular ellipses are not used.')
upd(32,evidence=D[32]['evidence']+' Main also retains a short leftward hook at the lower endpoint of the left side; that turn was absent from the returned C-based paths.',
    diff_C=True,final='C rim gaps, long inner line, uneven hatches and separate arcs; add short leftward lower-side hook.')
upd(36,readers={'A':D[36]['readers']['A'],'B':D[36]['readers']['B'],
    'C':'Connecting trace and detached upper fleck retained; extra short first-X diagonal omitted in reading.tex.'})
upd(42,final=r'\hat{\mathbb F} (first candidate of the overlay-order doubt)',unresolved=False,
    evidence='The raised mark arches up and then down, with white beneath its left portion. Main resolves the hat against A’s retained dot alternative; B/C also select hat. The F body has a returning stem, recorded as doubled in the selected first candidate. The separate overwrite-order doubt is recorded in the next row.')
upd(43,diff_C=True,final=r'\unsure{\deleted{O}\hat{\mathbb F}|\deleted{\mathbb F}\hat O}',unresolved=True,
    evidence='The large O oval and the two F arms/return are both visible, but the static overlap does not establish which was written last. Main adopts C-reader’s explicit two orders; A/B commit to an older O. H acknowledges overlap editorially but omits its body from the formula.')
upd(50,evidence='The second F has a narrow looped/doubled upright, with middle arm and low 2. Main confirms it; the first-pair F is separately corrected below, contrary to A’s claim that it has one stem.')
upd(53,final=r'\unsure{F_n|F_{n+1}|F_3}',evidence=D[53]['evidence']+' Main retains n first (A/C), then n+1 and 3; B’s preferred n+1 cannot be isolated securely and H’s unqualified reading is rejected.')
upd(56,diff_C=True,final='Upper-left and lower-right gaps; divider meets top; small upper side stroke; gap before detached lower divider stub; faint upper right-side segment.',
    evidence=D[56]['evidence']+' Main confirms C-reader’s short slant beside the upper divider. Below the bottom knot a white interval precedes a detached short descending stub; all three returned paths join it. A thin upper right-side segment also begins around (1624,1200), above the starts in the returns. Both are preserved.')
upd(59,diff_C=True,final=r'\unsure{\deleted{O}\dot{\mathbb F}|\dot B}\times I',confidence='low',unresolved=True,
    evidence='The small sign has a compact oblique raised dot, a doubled/returning stem, an upper arm/counter and a larger oval at right. Main adopts C-reader’s local O/F-composite versus B uncertainty. A/B’s secure old-O-plus-F is not justified; the chronology shares the earlier overlay doubt. The cross and barred I are clear.')
upd(60,diff_C=True,final=r'\deleted{O}\hat{\mathbb F} (first candidate of earlier overlay-order doubt)',
    evidence=D[60]['evidence']+' Main confirms the doubled return but not a unique overwrite chronology. This occurrence follows the first candidate of the already marked same-page doubt, with an explicit local comment, rather than introducing a new assertion of chronology.')
upd(61,final=r'\hat{\mathbb F}',unresolved=False,evidence=D[61]['evidence']+' Main retains the angular raised mark as a hat; the subscript occurrence has a distinct compact dot and is not normalized to it.')
upd(62,final='Ob and Fl/Fl_0 retained; low oval after Fl is zero; looped arguments corrected separately.',
    evidence='The top target crop confirms the low zero and looped l in Fl_0. Its argument is also looped ell, not C; this independent correction is recorded above. The generic Ob/Fl labels elsewhere were checked in all three authorized half readings.',
    readers={'A':I['A']['004A62']['reading'],'B':'Ob/Fl labels retained; top argument C_1|C_n.','C':'Ob/Fl labels retained; closed-loop arguments have ell/C alternatives.'})

def add_from(a,key,newid,crop,readers,**updates):
    x=copy.deepcopy(I[a][key]);x['id']=newid;x['final']=x.pop('reading');x['crop']=crop;x['readers']=readers;x.update(updates);issues.append(x);return x
add_from('B','B03','004N01',rp('C','15_top_factor'),
    {'A':r'\mathrm{Fl}\,C_1','B':I['B']['B03']['reading'],'C':I['C']['T05']['reading']})
add_from('B','B04','004N02',rp('C','15_top_factor'),
    {'A':'Omitted.','B':I['B']['B04']['reading'],'C':I['C']['T06']['reading']})
add_from('C','I02','004N03',rp('B','11_inclusions'),
    {'A':r'F_1','B':r'\mathbb F_1','C':r'\mathbb F_1'})
add_from('C','I08','004N04',rp('B','11_inclusions'),
    {'A':r'F_n','B':r'\mathbb F_n','C':r'\mathbb F_n'})
add_from('C','P04','004N05',rp('C','14_pair_alphabets'),
    {'A':r'F_1','B':r'\mathbb F_1','C':r'\mathbb F_1'})
add_from('B','B53','004N06',mp('cylinder'),
    {'A':'Retained C hatch positions.','B':I['B']['B53']['reading'],'C':'Retained C hatch positions.'},
    evidence=I['B']['B53']['evidence']+' Main full-cylinder crop confirms these placements; B’s partial lens crop was not additionally viewed.')
add_from('B','B43','004N07',rp('C','11_last_pair'),
    {'A':'Final period retained.','B':I['B']['B43']['reading'],'C':'Final period retained.'})
# G07's short grid stroke is incorporated in A56 with its two other refinements.
D[56]['readers']['C'] += '; '+I['C']['G07']['reading']

def main_issue(num,location,final,evidence,crop,bbox,confidence='high',unresolved=False,C='Omitted',H='Omitted',readers=None,kind='omission'):
    x={'id':f'004M{num:02d}','location':location,'C':C,'H':H,'final':final,'evidence':evidence,
       'confidence':confidence,'diff_C':True,'diff_H':True,'kind':kind,'marked_in_H':'no','crop':crop,
       'bbox':bbox,'readers':readers or {a:'Omitted in reading.tex.' for a in 'ABC'},'unresolved':unresolved}
    issues.append(x);return x
main_issue(1,'Top arrow, detached point above shaft','Small literal point near (950,130), function unassigned.',
    'The main arrow crop shows a compact isolated dark point above the shaft with white between; none of the returned traces contains it.',rp('A','01_top_arrow'),[945,125,956,136])
main_issue(2,'Top target, fleck left of lower F stem','Small literal point near (1110,214), function unassigned.',
    'A detached compact fleck sits just left of the lower F stem; it is traced without calling it punctuation.',rp('C','02_endpoint'),[1106,210,1115,218])
main_issue(3,'Live lower replacement, point above-right of cross','Small literal point near (981,250), function unassigned.',
    'A compact isolated mark lies above-right of the live cross, separated from the cancelled upper strokes.',rp('C','03_corrections'),[978,247,985,254])
main_issue(4,'F_3 row, third Fl capital',r'\unsure{\mathbb F|F}\mathrm l',
    'The third F has a narrow white counter/return along its upper upright, while the lower continuation is not distinctly doubled. All three readers and both witnesses print plain F; main retains the local alphabet doubt with doubled F first.',rp('A','05_f3_row'),[835,475,878,548],
    confidence='medium',unresolved=True,C=r'\mathrm{Fl}',H=r'\mathrm{Fl}',readers={a:r'\mathrm{Fl}' for a in 'ABC'},kind='misread symbol or index')
main_issue(5,'F_n row, last Fl capital',r'\mathbb F\mathrm l (first candidate of preceding local alphabet doubt)',
    'The last F has the same narrow enclosed upper return, without an equally separate lower doubled stem, as the third F of the F_3 row. The first candidate of that same-page ambiguity is used here; no uniform alphabet is inferred.',rp('C','17_Fn_factors'),[964,709,1027,779],
    confidence='medium',C=r'\mathrm{Fl}',H=r'\mathrm{Fl}',readers={a:r'\mathrm{Fl}' for a in 'ABC'},kind='misread symbol or index')
main_issue(6,'Open rectangle, detached marks and short returns','Two small points, downward upper peg and upward lower-left hook.',
    'Main crop confirms isolated compact marks near (1603,608) and (1641,613), a short downstroke near (1627,615), and a small upward lower-left hook near (1600,730). They are separate from the principal retraced sides; no label or mathematical role is assigned.',mp('open_rectangle'),[1595,600,1647,743],kind='drawing or diagram')
main_issue(7,'Cylinder, detached upper point','Point above right side endpoint near (1925,729).',
    'A compact dark point is separated by a white gap from the upper end of the right side stroke. It is reproduced without interpreting a punctuation or endpoint symbol.',mp('cylinder'),[1920,725,1930,733])
main_issue(8,'Inclusion sequence, point above-left of final F','Small point near (1191,1033).',
    'The full-row crop shows a compact detached dark point above-left of the final F. Its origin and linguistic role are unassigned.',rp('B','11_inclusions'),[1187,1029,1196,1037])
main_issue(9,'Isolated right inclusion, low left slant','Short detached low slant to the left of the overlaid body.',
    'The crop shows a separate sloping stroke below-left of the overlaid O/F; its upper end stops short of the large body. Main preserves it graphically without deciding whether it belongs to the earlier writing.',rp('C','09_right_inclusion'),[1673,1102,1687,1127],confidence='medium')
main_issue(10,'First starred pair, closing-parenthesis return','Closing parenthesis with a short extra inward slant.',
    'The first closing parenthesis has a short slant branching inward from the middle of the curve, unlike a plain single arc. It is retained graphically, not read as an extra letter.',rp('C','14_pair_alphabets'),[648,1337,673,1428],kind='drawing or diagram')
main_issue(11,'Pair continuation, detached point before dash','Short point/tick near (992,1372), then one continuous dash.',
    'The main crop contains one long continuous dash and a separate short dark mark to its left. All returns preserve only the dash. No ellipsis or punctuation value is imposed on the isolated mark.',mp('pair_continuation'),[988,1367,999,1379])

# Consolidated text starts with A's fullest geometrical return, with the above choices applied once.
s=(O/'records/scan004/reader_A/reading.tex').read_text()
def rep(old,new):
    global s
    if old not in s:raise ValueError('Absent patch anchor: '+old[:120])
    s=s.replace(old,new,1)
rep(r'\tikz[baseline=-.4ex,x=.008cm',r'\tikz[baseline=(current bounding box.center),x=.008cm')
rep(r'  \fill (999,162)',r'  \fill (950,130) circle[radius=1.3];'+'\n'+r'  \fill (999,162)')
rep(r'\mathrm{Fl}_0(\unsure{C_1|C_n})',r'''\tikz[baseline=(targetF.base)]{
 \node[inner sep=0pt] (targetF) {\(\mathrm{Fl}_0\)};
 \fill ([xshift=-.13em,yshift=.02em]targetF.south west) circle[radius=.025em];}
 (\ell_{\unsure{n|1}})''')
rep(r'{\bigl(\mathrm{Fl}\,C_1\times\mathrm{Ob}\,C_2\bigr)}',r'''{\tikz[baseline=(topproduct.base)]{
 \node[inner sep=0pt] (topproduct) {\(\bigl(\mathbb F\mathrm l\,C_1\times\mathrm{Ob}\,C_2\bigr)\)};
 \fill ([xshift=1.05em,yshift=-.48em]topproduct.west) circle[radius=.025em];}}''')
rep(r' \arrow[u,shift left=.55ex]\arrow[u,shift right=.55ex]',r''' \arrow[u,phantom,"{\tikz[baseline=(current bounding box.center),x=.008cm,y=-.008cm,line cap=round,line join=round]{
  \draw[line width=.45pt] (286,260)--(289,178) (276,208)--(289,178)--(298,199)
   (284,254)..controls(282,246)and(284,202)..(287,185)
   (286,260)--(292,257) (321,257)--(318,184) (321,257)--(327,254)
   (307,190)--(327,173)--(334,182);
 }}" description,pos=.5]''')
rep(r'\inserted{\mathbb F\mathrm l_0(C_1)\times\mathrm{Ob}\,C_2}',r'''\inserted{\mathbb F\mathrm l_0(\ell_1)
 \mathbin{\tikz[baseline=(replacementcross.base)]{
  \node[inner sep=0pt] (replacementcross) {\(\times\)};
  \fill ([xshift=.09em,yshift=.12em]replacementcross.north east) circle[radius=.025em];}}
 \mathrm{Ob}\,C_2}''')
rep('% are traced without asserting a separately cancelled earlier left arrow.',
    '% are traced without asserting a separately cancelled earlier left arrow.\n% Detached points have unassigned origin/function; the right upward head is gapped.')
rep(r'\draw (1718,101)--(1724,101);',r'\draw (1718,101)--(1724,101) (1648,178)--(1647,189);')
rep(r'\,<\,\mathrm{Fl}\,l_3',r'\,<\,\unsure{\mathbb F|F}\mathrm l\,\ell_3')
rep(r'\mathbb F_n\mathrel{\unsure{2|=}}',r'\mathbb F_n\mathrel{2}')
rep(r'\times\mathrm{Fl}\,C_n',r'\times\mathbb F\mathrm l\,C_n')
rep(r'\deleted{\times\mathrm{Ob}\,C_4}',r'''\deleted{\times\mathrm{Ob}\,C_4}
% The last Fl follows the first candidate of the preceding F-alphabet doubt.
% The small point before C_1 is reproduced without a punctuation assignment.''')
rep(r'\draw (1538,817)',r'''\fill (1603,608) circle[radius=1.2] (1641,613) circle[radius=.8];
\draw (1627,611)--(1627,616) (1600,730)--(1601,740);
\draw (1538,817)''')
rep('(1763,785)--(1779,883)','(1763,785)--(1779,883)--(1774,881)')
rep(r'\draw (1789,900)',r'\fill (1925,729) circle[radius=.9];'+'\n'+r'\draw (1789,900)')
rep('(1811,865)--(1807,902) (1825,854)--(1815,915) (1845,858)--(1838,900)',
    '(1801,876)--(1806,897) (1822,864)--(1816,916) (1845,858)--(1838,887)')
rep(r'\bullet\quad O_1\subset F_1',r'\bullet\quad O_1\subset\mathbb F_1')
rep(r'O_n\subset F_n',r'''O_n\subset
\tikz[baseline=(lastinclusionF.base)]{
 \node[inner sep=0pt] (lastinclusionF) {\(\mathbb F_n\)};
 \fill ([xshift=-.25em,yshift=.09em]lastinclusionF.north west) circle[radius=.023em];}''')
rep(r'\deleted{O}\unsure{\hat F|\dot F}\subset\mathbb F',r'''\tikz[baseline=(rightoverlay.base)]{
 \node[inner sep=0pt] (rightoverlay) {\(\unsure{\deleted{O}\hat{\mathbb F}|\deleted{\mathbb F}\hat O}\)};
 \draw[line width=.3pt] ([xshift=-.16em,yshift=-.1em]rightoverlay.south west)
 --([xshift=-.02em,yshift=.22em]rightoverlay.south west);}
 \subset\mathbb F
% Overlay order is uncertain. The low left slant is literal, with function unassigned.''')
rep(r'(O_1,F_1)\mathbin{*}',r'''(O_1,\mathbb F_1
\tikz[baseline=(pairclose.base)]{
 \node[inner sep=0pt] (pairclose) {\()\)};
 \draw[line width=.3pt] ([xshift=-.02em,yshift=.04em]pairclose.center)
 --([xshift=-.22em,yshift=-.2em]pairclose.center);}
\mathbin{*}''')
rep(r'(O_2,\mathbb F_2)\ \text{---}\mathbin{*}',r'''(O_2,\mathbb F_2)\ 
\tikz[baseline=(pairdash.base)]{
 \node[inner sep=0pt] (pairdash) {\(\text{---}\)};
 \fill ([xshift=-.25em,yshift=.08em]pairdash.west) ellipse[x radius=.02em,y radius=.04em];}
\mathbin{*}''')
rep(r'\unsure{F_n|F_3|F_{n+1}}',r'\unsure{F_n|F_{n+1}|F_3}')
rep('(1502,1200)--(1495,1331)--(1490,1478)',
    '(1502,1200)--(1495,1331)--(1490,1466) (1490,1471)--(1490,1478)\n (1499,1213)--(1495,1235)')
rep(r'\fill (1365,1315)',r'\draw[line width=.3pt] (1624,1200)--(1627,1217);'+'\n'+r'\fill (1365,1315)')
rep(r'(F\times I)\mathbin{\amalg}_{\deleted{O}\dot F\times I}\deleted{O}\hat F',r'''(F\times I)\mathbin{\amalg}_{\unsure{\deleted{O}\dot{\mathbb F}|\dot B}\times I}
\deleted{O}\hat{\mathbb F}
% The final overlay follows the first candidate of the earlier order doubt.
% The small subscript composite retains a separate B alternative.''')
(O/'pages/H104-01_104_scan004.tex').write_text(s)

inv=copy.deepcopy(R['C']['inventory'])
changes={
 'top_diagram':'Ob C_4; literal retraced right arrow with detached point; Fl_0(ell_n/1); two upward arrows with right-head gap',
 'lower_replacement':'Doubled Fl_0(ell_1) x Ob C_2, live below old text; detached point by cross',
 'third_old_letters':'Possible old F/Fl inside Ob',
 'F3_product':'Doubled F_3 = Fl C_1 x Fl C_2 < doubtful doubled/plain Fl ell_3 x Ob C_4',
 'Fn_product':'Doubled F_n; literal 2; doubled Fl.C_1 < Fl C_2 — x doubtful doubled Fl C_n',
 'open_rectangle':'Open retraced rectangle; two detached marks and short upper/lower-left returns',
 'curved_body':'Open rim and side gaps; long inner stroke; irregular lens hatches; upper-right point and lower-left hook',
 'isolated_inclusion':'Hatted overlaid doubled F/O with uncertain order, low left slant, inclusion in doubled F',
 'four_cell_grid':'Four cells; corner gaps; short divider-side stroke; two dark knots; separated lower stub',
 'starred_pairs':'Two comma-separated pairs with doubled F; first closing-parenthesis return; detached mark and dash; star; uncertain final pair without comma; period'
}
for x in inv:
    x['sheet_kind']='text'
    if x['element'] in changes:x['first_words_or_objects']=changes[x['element']]
# Each graphic refinement is inventoried within the complete parent display/drawing.
remaining=[]
for x in issues:
    if x.get('unresolved'):
        remaining.append({'location':x['location'],'reading':x['final'],
          'alternatives':'See the explicit local candidates; graphic writing history is unassigned where stated.',
          'confidence':x['confidence'],'reason':x['evidence']})
notes=[
 'Landscape handwritten mathematical working sheet with six principal sketches, no prose title, date or manuscript folio. The isolated bottom-left 3 is an archive number and is represented only in a comment. Pale reverse-side remnants do not establish a recoverable typed passage; all three readers independently found no continuous readable type. The sheet is classified text on the observed evidence, without adopting H’s typed-verso description as manuscript text.',
 'The upper diagram relates Ob and Fl labels with a heavily retraced right arrow and two upward arrows. Top source is Ob C_4. Both the top target and the live lower replacement contain closed-loop ell arguments, contrary to both witnesses’ C. The target’s low n/1 remains doubtful; the replacement’s 1 is clear. The cancelled amalgamation and old Fl group remain above the live replacement.',
 'Two further rows contain F_3 and F_n products. The third F_3 argument is ell_3. Two wedge-shaped signs are transcribed literally as <, including one where both witnesses give multiplication. The separator following F_n is one connected 2-shaped stroke, not separate equality bars. The possible intended equality and multiplications are not substituted. These are observations of surprising ink, not demonstrated mathematical errors.',
 'F alphabets are read occurrence by occurrence. Separate upright strokes justify doubled F in the parenthesized top product, second Fl of the next product, inclusion terms and first two starred pairs. Narrow upper returns leave the third F_3 Fl and last F_n Fl locally ambiguous between doubled and plain F. The doubt is marked at its first occurrence on the page; the later matching occurrence uses its first candidate.',
 'The lower sheet records inclusions, a product ending literally (- ?), a sequence of starred pairs, and (F x I) followed by an amalgamation sign with a lower composite label. The question mark in (- ?) is the author’s explicit doubt; there is no written “à vérifier”, “sauf erreur” or “je présume”. No proof or calculation is provided or checked.',
 'The first two starred pairs have commas. The last pair has no visible comma, an old O/0 loop, a live O_3/O_n uncertainty, and a final plain F with a heavily overwritten index n/n+1/3. H’s definite n+1 is not established. A final period is visible. Continuous dashes and six-rayed stars are retained; the small detached mark preceding the pair-row dash is not converted into an ellipsis.',
 'The right-hand O/F composites retain uncertain overwrite order. Large raised marks are arched/peaked and encoded as hats; the smaller subscript mark is a compact oblique dot. The small composite also permits B. No boundary construction or universal property is inferred from these forms.',
 'The sketches preserve skewed cells, interrupted edges, separate traces, dark knots with tiny white counters, an open three-sided rectangle, and a hatched lens with a long descending inner stroke. Main-crop refinements include a detached upward-arrow head, gaps near the lower grid stub, small returns and isolated dark marks. Their ink is traced without assigning mathematical meanings or interpreting grey paper texture as objects.',
 'H’s separate drawing code was checked by all three readers against their source views; the main reader adjudicated every reported difference on a crop. No OCR, external research or compilation was used. No theorem was proved or used as mathematical background, so CHECK_EVENTS receives no event for this page.'
]
decision={'scan':4,'folder':'H104-01','issues':issues,'remaining':remaining,'inventory':inv,
 'notes':notes,'checks':[],'crop_counts':{'A':14,'B':20,'C':18,'main':6},'main_adjudication_complete':True}
(O/'records/scan004/decision.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'issues':len(issues),'remaining':len(remaining),'inventory':len(inv)}))
