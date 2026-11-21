from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan067'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='c8c3c616d959e5d55b2d36441dcde7509d4ae39736c47855317b0f2c6733cae7'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B01':'The complete opening and end helper were viewed. No complete ou or other word is visible between the comma and i: the faint arc and specks do not form a recoverable glyph. The descender in pi(j) supports j, even though the role of the opposite edge may suggest i mathematically. The labelled arrow has the same reading in both transcriptions.',
'B02':'The title and end helper show de-cou-p-ee, with a descending p and no separate m/po group for decomposee. The word is live; its retracing is not a complete cancellation. A comma follows pantaloniquement. After the crossed old graphe a small un precedes squelette, whose q descender and two l ascenders are visible. Pantalonique generalise has a q descender and the long g/e/n/r/a/l/ise run; it is not pantalonien globulise. The compressed ending of the inserted orientee is left doubtful. The old graphe remains doubtful under its strike.',
'B03':'The whole definition, upper/lower and replacement helpers were viewed. An opening parenthesis precedes i.e.; a comma follows the orientee parenthesis. Topologiques, et avec une, and the raised drapeaux de types 0,1 are supported by their visible stems and descenders. The final s of types and final e/s of incidente are compressed and remain open. The old qualifier remains orientee/reperee under the strike. The first line is certainly struck. The long diagonals and lower enclosing return support cancellation of the larger block, but its exact scope is now explicitly qualified because some strokes also frame the construction.',
'B04':'The entire canonical crop was viewed through its verified pixel-identical lossless WebP. Five left-to-outer, four inter-hole and three right-to-outer runs are visible. The inter-hole initials are heavily retraced: open outer c-like curves coexist with closed or ascending inner traces compatible with a on the left and b on the right; all eight are now doubtful, not high-confidence c readings. The irregular contours, disconnected earlier fragments, doubled short lower-right red mark and small circular arrow are preserved. Filled junctions are retained where dark compact blobs are visible; b3 at the left is a crossing without an independent dot. No continuity is invented across the disconnected lower-right fragments.',
'B05':'The graph and complete equality were viewed. The low loop with a raised arm is the same gamma form used in the clear gamma=4 annotation in B11 and the gamma equations in B09; sigma is not adopted here. The separate small loop before the left gamma-prime may be overwritten alpha and remains doubtful. Elevated clusters above the right alpha/beta are real but overlap cf and a boundary stroke; stars versus intrusive ink remain open. The extended crossing strokes belong to the larger cancellation/framing question, whose scope is qualified in place.',
'B06':'The entire torsor clause and both circular sums were viewed, with the larger B07 context. La donnee d\'un and the short live isom without a point are clear. The crossed former word permits isom/auto. The group divisor is overworked and its extra low stroke may be an index; it stays doubtful. The parenthetical gamma-prime forms match the page\'s looped gamma. There is no de after the right circulaire: the next line begins with the bracket. The intervening sign has a curved upper stroke and a lower bar; the diagonal continues far beyond it as a global stroke, so the underlying sign is simeq. A dark terminal point follows the right bracket; no colon follows the group quotient. Cancellation scope is retained as probable but explicitly uncertain.',
'B07':'Both overlapping lossless PNG tiles cover the complete canonical box. The already-existing full-map JPEG transport was also viewed for contour context, not to decide fine letters. The second drawing follows the irregular pale loops, partitions, six A labels, the black pentagon and five legs more closely. Its leftward leg has a dark pointed termination beneath the formula and is retained as an arrow. Long diagonal strokes are drawn separately from that leg and from the thin enclosure. The obscured older connectivity is left uncertain; cropped or faded contour ends are not joined speculatively.',
'B08':'All four loop groups were viewed. The upper chord is unheaded. The five marks on the upper-left contour include a short heavy bar, a compact point and three angular/retraced marks, rather than five uniform circular dots. The contour arrows and the lower-leftward short arrow remain. The open ends of the three lower arc groups and the three heavy spots in the lowest right group are visible. The caption has a closed first digit compatible with 0, a two-armed alpha and the second [1,beta) group; the opening digit is still doubtful. The second geometric tracing is adopted, with the caption alternative restricted to 0/1 rather than gamma.',
'B09':'The full algebra and pale-layer helper were viewed. All three dark equations and their halves agree. A pale alpha= precedes the lower old parenthesis; its interior is more compatible with unprimed alpha+beta+gamma than with the first transcription\'s primed numerator, but remains partly masked. Inside the right old parenthesis the visible short horizontal stroke has no secure upright, so beta-minus-gamma remains primary. The line lies below that parenthesis, not securely through it; its deletion status is left open. An additional pale half-sum fraction is visible below the dark gamma row and is now retained there. The separate lower-right alpha-prime and terminal pale equals are kept spatially separate. The upper old prefix/fraction remains doubtful rather than being reconstructed from algebra.',
'B10':'All three pencil trials were viewed as whole formulas. After the first closing parenthesis there are faint minus and alpha-prime traces before the equality; the RHS begins with beta-prime, not an additional alpha-prime. That first line remains doubtful. In the second line both right primes and the beta and gamma loops are visible, and a short underline lies below 2alpha. The third beta+gamma=alpha-prime has a separate raised tick over the final alpha. These latter two C doubts can be resolved on this crop. No terminal comma or period is supplied.',
'B11':'The four c labels, five b labels, three a labels and all three numerical equalities were read individually. Gamma=4 has the same low loop and raised arm as the disputed gamma forms above. The left side visibly stops short of the base; the second tracing preserves this gap instead of closing the triangle. No label or count changes.',
'B12':'The curved row of c1 through c4, the central compact dot and b5 through b1 is visible across the triangle. The three a labels sit on successive levels; the last 1 is higher than a normal low index, so a-superscript-1/a-subscript-1 remains open. The short isolated lower-right slash is present and restored to the second tracing. Both lower corners have gaps in their pale contours.',
'B13':'The whole small triangle was viewed. The lowest left initial is an open c-like form, while the four higher labels have b ascenders; c5/b5 remains open. The middle right a2 overlaps a larger earlier A-like form and an adjacent low loop; a2/a20 and earlier A0 remain qualified rather than assigned one certain layer. A pale A-infinity below the base and A-like side traces are now transcribed explicitly with doubts. The base has nine separate short strokes, in uneven groups, not four uniform ticks. Its four heavily retraced letter groups remain c-like with possible earlier a traces. The vertex a and b remain distinct from the pale 0 and dark 1.',
'B14':'NB has a separate underline. Three raised prime ticks follow the initial Greek letters. After the looped O and angular K there are two s-like bends and a short i, supporting OK ssi rather than OK si. The sum ends in the handwritten word pair.',
'B15':'The three central dark vertices and their 0,1,infinity labels are clear. Five visible runs extend between 0 and 1, but some fade before a junction. The outer contour and several wrapping runs are irregular, partly disconnected and retraced; the second tracing preserves those visible ends rather than completing smooth ellipses. The local circles have separate dark and broken sectors and clear arrows at 0 and 1. No distinct infinity arrowhead is forced from its short angular trace. The older connectivity remains qualified.',
'B16':'The counts and complete formulas were viewed. The upper right word has a compressed exit, leaving sommets/sommet open, but d\'ordre and the three raised prime marks are clear. In the overworked edge word a long g-like descender survives, so the older bigones layer cannot be discarded in favour of a wholly clear aretes. The cancelled old sum remains doubtful. The raised total ends with a single low turn and exit compatible with 2, not a two-lobed 3. The author\'s sum of three (quantity-1) terms would arithmetically end in -3, but the written -2 is retained. The final face total has -1.',
'B17':'The pale folio has two long upper curves returning into low closed loops: 66. Margin versus mspage is a wrapper-only difference; mspage is retained.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
V={b:x['first'] for b,x in C.items()}
V['B02']=V['B02'].replace(r'\inserted{orientée}',r'\inserted{\unsure{orientée|orienté}}').replace('décomposée pantaloniquement','découpée pantaloniquement,').replace('} squelette','} un squelette')
V['B03']=V['B03'].replace(r'\deleted{i.e.',r'\deleted{(i.e.').replace('orientée}) dont','orientée}), dont').replace('de types $0,1$',r'de \unsure{types|type} $0,1$').replace('arête incidente)',r'arête \unsure{incidente|incidents})')
V['B03']=r'\unsure{'+V['B03']+'}'
V['B04']=C['B04']['second']
for i in range(1,5):
 for a,z in [('a','0'),('b','1')]:
  old=f'{a}_{i}^{z}';new=rf'\unsure{{c_{i}^{z}|{old}}}'
  V['B04']=V['B04'].replace(r'\unsure{'+old+'}',new) if r'\unsure{'+old+'}' in V['B04'] else V['B04'].replace('$'+old+'$','$'+new+'$')
pts=[(1300,1200),(1100,1240),(960,1480),(1050,1690),(1430,1330),(1470,1590),(1370,1790),(1200,1810),(2075,1330),(1900,1600),(1920,1790),(2100,1900),(2280,1850)]
V['B04']=V['B04'].replace(r'\end{tikzpicture}', '\n'.join(rf'\fill[black] ({x},{y}) circle[radius=7];' for x,y in pts)+'\n'+r'\end{tikzpicture}')
V['B05']=V['B05'].replace(r'\deleted{\underbrace',r'\unsure{\deleted{\underbrace').replace("_{\\gamma'_t}}", "_{\\gamma'_t}}}")
V['B06']=V['B06'].replace(r'\unsure{isom}',r'\unsure{isom|auto}').replace(r'\unsure{\gamma}',r'\unsure{\gamma|\gamma_t}').replace(r'\unsure{\simeq|\not\simeq}',r'\simeq').replace(r'\text{circulaire de}',r'\text{circulaire}').replace(r'[1,\beta_t]}}',r'[1,\beta_t]}.}')
V['B06']=r'\unsure{'+V['B06']+'}'
V['B07']=C['B07']['second'].replace('(1580,1202)--(1585,1380) (1440,1069)--(1115,1165);','(1580,1202)--(1585,1380);\n'+r'\draw[black,line width=.6pt,->] (1440,1069)--(1115,1165);')+'\n% crop-candidate: scan 67'
V['B08']=C['B08']['second']
oldexpr=r"\unsure{(\alpha'+\beta'-\gamma')-\deleted{(\beta-\gamma)}|(\alpha'+\beta'-\gamma')-(\beta-\gamma)}\ \unsure{=}"
newexpr=r"\unsure{\alpha=(\alpha+\beta+\gamma)-(\beta-\gamma)|\alpha=(\alpha'+\beta'-\gamma')-\deleted{(\beta-\gamma)}}\ \unsure{=}"
V['B09']=V['B09'].replace(oldexpr,newexpr).replace(r'\node[gray] at (9.8,-3.05)',r"\node[gray,anchor=west,font=\small] at (5.2,-3.05) {$\unsure{\dfrac{\alpha'+\beta'+\gamma'}2}$};"+'\n'+r'\draw[gray] (8.2,-2.34)--(9.85,-2.34);'+'\n'+r'\node[gray] at (9.8,-3.05)')
V['B10']=r'''{\color{gray}
\[
\begin{aligned}
&\unsure{2(\alpha+\beta+\gamma)-\alpha'=\beta'+\gamma'}\\
&\uline{2\alpha}+\beta+\gamma=\beta'+\gamma'\\
&\beta+\gamma=\alpha'
\end{aligned}
\]}'''
V['B11']=C['B11']['second']
V['B12']=C['B12']['second'].replace('$a_1$',r'$\unsure{a^1|a_1}$').replace(r'\end{tikzpicture}',r'\draw[black,line width=.65pt] (1490,1735)--(1535,1825);'+'\n'+r'\end{tikzpicture}')
V['B13']=C['B13']['second'].replace(r'\unsure{a_2|a_{20}}',r'\unsure{a_2|a_{2\,0}}')
for i in range(1,5):
 old=rf'\unsure{{c_{i}|a_{i}}}' if i<3 else rf'\unsure{{c_{i}}}'
 V['B13']=V['B13'].replace(old,rf'\unsure{{c_{i}|\deleted{{a_{i}}}c_{i}}}')
V['B15']=C['B15']['second']
V['B16']=V['B16'].replace(r'\text{sommets d',r'\text{\unsure{sommets|sommet} d')
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,v in V.items():
 if v!=C[b]['first']:
  assert C[b]['first'] in s,b
  s=s.replace(C[b]['first'],v)
  D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
bm={1:'B01',2:'B01',3:'B01',4:'B02',5:'B02',6:'B02',7:'B02',8:'B02',9:'B03',10:'B03',11:'B03',12:'B03',13:'B03',14:'B03',15:'B03',16:'B03',17:'B03',18:'B03',19:'B05',20:'B05',21:'B06',22:'B06',23:'B06',24:'B06',25:'B06',26:'B06',27:'B06',28:'B06',29:'B07',30:'B07',31:'B04',32:'B04',33:'B04',34:'B04',35:'B08',36:'B08',37:'B08',38:'B09',39:'B09',40:'B09',41:'B09',42:'B09',43:'B09',44:'B10',45:'B10',46:'B10',47:'B12',48:'B12',49:'B12',50:'B13',51:'B13',52:'B13',53:'B13',54:'B14',55:'B14',56:'B15',57:'B15',58:'B16',59:'B16',60:'B16',61:'B16',62:'B16',63:'B17',64:'B09'}
for x in r['changes']:
 n=int(x['id'].rsplit('-',1)[1]);b=bm[n]
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b])
 if n==4:x.update(final='découpée',diff_c=True,confidence='high')
 if n==8:x.update(final='un squelette pantalonique généralisé',diff_c=True)
 if n==9:x.update(final=V['B03'],confidence='low')
 if n==10:x.update(final='orientée}), dont',diff_c=True,diff_h=False)
 if n==14:x.update(final=r'\inserted{drapeaux de \unsure{types|type} $0,1$}')
 if n==15:x['diff_c']=False
 if n==22:x.update(final=r'\deleted{\unsure{isom|auto}}')
 if n==24:x.update(final=r"sous $\mathbb Z/\unsure{\gamma|\gamma_t}$ $(\gamma=\gamma'_s=\gamma'_t)$",confidence='low')
 if n==25:x.update(final='somme circulaire; somme circulaire',diff_c=True)
 if n==26:x.update(final=r'\simeq',diff_c=False,confidence='high')
 if n==27:x.update(final=r'no colon after quotient; [1,\beta_t].',diff_c=False,confidence='high')
 if n==28:x.update(final=V['B06'],confidence='low')
 if n in [29,30,32,33,34,35,36,37,43,47,56,57]:x['final']=V[b]
 if n==31:x.update(final='; '.join(rf'\unsure{{c_{i}^{z}|{a}_{i}^{z}}}' for a,z in [('a','0'),('b','1')] for i in range(1,5)),confidence='low')
 if n==39:x.update(final=newexpr,diff_h=True)
 if n==44:x.update(final=r"\unsure{2(\alpha+\beta+\gamma)-\alpha'=\beta'+\gamma'}",diff_c=True)
 if n==45:x.update(final=r"\uline{2\alpha}+\beta+\gamma=\beta'+\gamma'",diff_c=True,confidence='high')
 if n==46:x['final']=V['B10']
 if n==52:x.update(final=r'\unsure{a_2|a_{2\,0}}',diff_c=False,diff_h=False)
 if n==53:x.update(place='Earlier A labels and overwritten base labels',final=r'\unsure{A_\infty};\ \unsure{A};\ \unsure{A_0};\ '+ '; '.join(rf'\unsure{{c_{i}|\deleted{{a_{i}}}c_{i}}}' for i in range(1,5)),kind='omission',error_kind='Omissions')
def add(n,place,c,h,final,b,kind='omission',cat='Omissions',dc=True,dh=True,conf='high'):
 r['changes'].append(dict(id=f'{p}-{n:02}',place=place,c=c,h=h,final=final,diff_c=dc,diff_h=dh,kind=kind,error_kind=cat,evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],confidence=conf,marked_in_h=False,consequential=False))
add(65,'Comma after pantaloniquement','pantaloniquement de','pantalonniquement de','pantaloniquement, de','B02')
add(66,'Opening parenthesis before i.e.','i.e.','i.e.','(i.e.','B03')
add(67,'Separate lower pale half-sum fraction','absent at this position','absent',r"\unsure{\dfrac{\alpha'+\beta'+\gamma'}2}",'B09',conf='low')
add(68,'First triangle, open lower-left corner','closed triangular contour','triangle synopsis',V['B11'],'B11','drawing or diagram','Drawings and diagrams',dh=False)
add(69,'Small triangle, nine base ticks','four base ticks','labels only in drawing synopsis','nine unevenly grouped short strokes','B13','drawing or diagram','Drawings and diagrams',dh=False)
for x in r['decisions']:
 mid=x['id'];b=None
 if mid=='M0785':b='B08';x['reading']=r'\unsure{[0,\alpha][1,\beta)|[1,\alpha][1,\beta)}'
 if mid=='M0787':b='B10';x.update(reading=r"\unsure{2(\alpha+\beta+\gamma)-\alpha'=\beta'+\gamma'}",decision='undecided')
 if mid=='M0788':b='B10';x.update(reading=r"\uline{2\alpha}+\beta+\gamma=\beta'+\gamma'",decision='first',confidence='high')
 if mid=='M0789':b='B10';x.update(reading=r"\beta+\gamma=\alpha'",decision='first',confidence='high')
 if mid=='M0790':b='B09';x['reading']=newexpr
 if mid=='M0792':b='B09';x['reading']=r"\unsure{\alpha'=\dfrac{\alpha'+\beta'+\gamma'}2};\ \unsure{\dfrac{\alpha'+\beta'+\gamma'}2}"
 if mid=='M0796':b='B13';x['reading']=r'a_3\quad\unsure{a_2|a_{2\,0}}\quad\unsure{a_1}'
 if mid=='M0799':b='B16'
 if b:x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b])
old_to_new={oldexpr:newexpr,r'\unsure{[0,\alpha][1,\beta)|[1,\gamma][1,\beta)}':r'\unsure{[0,\alpha][1,\beta)|[1,\alpha][1,\beta)}',r'\deleted{\unsure{isom}}':r'\deleted{\unsure{isom|auto}}',r'\mathbb Z/\unsure{\gamma}':r'\mathbb Z/\unsure{\gamma|\gamma_t}',r'\unsure{a_{2\,0}|a_2}':r'\unsure{a_2|a_{2\,0}}',r"2(\alpha+\beta+\gamma)=\unsure{\alpha'+\beta'+\gamma'}":r"\unsure{2(\alpha+\beta+\gamma)-\alpha'=\beta'+\gamma'}"}
removed={'Sign between circular sums','Second lower pencil equality','Third lower pencil equality','Small triangle, pale side fragments'}
r['doubts']=[x for x in r['doubts'] if x['place'] not in removed]
for x in r['doubts']:
 old=x['reading'].replace('\\\\','\\')
 if old in old_to_new:x['reading']=old_to_new[old]
 if x['place']=='Pale older expression near gamma row':x.update(reason=E['B09'],alternatives='unprimed left parenthesis; old primed numerator; right group locally cancelled or only underlined')
 if x['place']=='First lower pencil equality':x.update(reason=E['B10'],alternatives='minus alpha-prime after the parenthesis; faint or obscured signs')
 if x['place']=='Small triangle, middle right label':x.update(reason=E['B13'],alternatives='a2 beside earlier A0; a20 with an extra low loop')
def doubt(place,reading,b,alts):r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=E[b]))
doubt('Inserted title ending',r'\inserted{\unsure{orientée|orienté}}','B02','orientée; orienté')
doubt('Definition, types ending and incidente ending',r'\unsure{types|type};\ \unsure{incidente|incidents}','B03','types/type; incidente/incidents')
doubt('Extent of the large cancellation',r'\unsure{\deleted{...}}','B07','complete definition and torsor block cancelled; some enclosing and diagonal strokes belong to framing or earlier drawing')
doubt('Eight retraced inter-hole initials','; '.join(rf'\unsure{{c_{i}^{z}|{a}_{i}^{z}}}' for a,z in [('a','0'),('b','1')] for i in range(1,5)),'B04','c with earlier a/b traces; current a on 0 and b on 1')
doubt('Lower pale half-sum',r"\unsure{\dfrac{\alpha'+\beta'+\gamma'}2}",'B09','primed half-sum; partly overlaid numerator')
doubt('Earlier A labels on the small triangle',r'\unsure{A};\ \unsure{A_0};\ \unsure{A_\infty}','B13','A-like older labels; uncertain index/layer assignment')
doubt('Irregular old-map and sphere connectivity',r'\unsure{\figure{...}}','B15','visible separate runs; obscured connections left uncompleted')
doubt('Upper right sommets ending',r'\unsure{sommets|sommet}','B16','sommets; sommet')
r['notes'].append(dict(id=p+'-N-audit',text='All 17 unequal boxes were directly adjudicated after the independent reading was frozen. The title is decoupee and un squelette; its comma and the opening parenthesis before i.e. are restored. Gamma is retained consistently by comparison of its low loop in the graph, the algebra and the clear gamma=4 annotation. The retraced inter-hole c initials are now explicitly doubtful against a/b. The large cancellation remains the primary state but its extent is qualified. The pale lower trial now includes a doubtful minus alpha-prime; this was read from visible traces and not supplied to make the algebra work. Additional pale layers and the small triangle\'s uneven ticks are retained. The final face count still reads -2 above the three (quantity-1) terms and -1 for the overall faces; the elementary arithmetic discrepancy is not repaired. Geometric refinements without a changed mark, line, label or connection are not counted as separate witness errors.'))
r['notation'].append(dict(sign=r'\gamma; retraced c/a/b',meaning_or_form='Gamma has a low loop and raised arm that can resemble sigma; use the clear gamma=4 and the three dark equations on this leaf. The eight inter-hole initials have mixed outer/inner strokes and remain locally doubtful.',places='Second boxes B04, B05, B06, B09, B10, B11',universality='Gamma form recurs consistently in this leaf; do not remove the local overtrace doubts from the c/a/b labels.',witness_errors='Both witnesses read a/b at the inter-hole labels; the accepted c primary is now low confidence. The blind second reader proposed sigma at some gamma occurrences.'))
extra=[f'crops/{p}_second_{z}.png' for z in ['B01_end','B02_end','B03_upper','B03_replacement','B03_lower','B07_top','B07_bottom','B09_pale']]
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra,'transport_views':{'B04':'verified pixel-identical lossless WebP','B07':'complete two overlapping lossless PNG tiles; existing full-map q98 JPEG used only for contour context'}}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
