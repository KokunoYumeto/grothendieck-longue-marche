from pathlib import Path
import json
p=Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R3')
base='readings/scan013/R3/'
findings=[]
def add(id,place,c,h,final,evidence,confidence,kind,marked=False,dc=False,dh=False,bbox=None,crop='',action='',math=''):
    findings.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked,diff_c=dc,diff_h=dh,bbox=bbox,crop=base+crop if crop else '',doubt_action=action,s_id='',math_note=math))
add('C01','Top diagram: label to the right of the upward Z-to-Z arrow',r'\unsure{2|\wr}',r'\mathrm{id}',r'\unsure{2|\wr}',
    'Crop 01: a small continuous hooked stroke with a lower right foot; no separate d is visible. The numeral-like and upright-wave alternatives remain.', 'medium','misread symbol or index',dh=True,bbox=[561,130,598,187],crop='01_vertical_label.png',action='retain',math='The equal object names do not supply an identity label; no mathematical normalization was used.')
add('F01','Top diagram: upper Z-to-G shaft',r'Z\arrow[r,dash]G',r'Z\arrow[r]G',r'Z\arrow[r]G',
    'Crop 02 shows a small triangular point at the right endpoint, distinct from the blunt downward turn in crop 03.', 'medium','drawing or diagram',dc=True,bbox=[623,91,691,119],crop='02_upper_shaft.png')
add('F02','Top diagram: upper G-to-Gamma and Gamma-to-1, and all four lower horizontal connectors',r'G---\Gamma---1;\quad1---Z---G\prime---\Gamma\prime---1',r'G\to\Gamma\to1;\quad1\to Z\to G\prime\to\Gamma\prime\to1',r'G---\Gamma---1;\quad1---Z---G\prime---\Gamma\prime---1',
    'The upper half settles the unheaded strokes; crop 03 resolves the small lower-left terminal turn as a blunt end, without a paired arrowhead.', 'high','drawing or diagram',dh=True,bbox=[425,87,1030,249],crop='03_lower_shaft.png')
add('C02','Conditional sentence immediately below the diagram',r'\unsure{splitte}','splittée','splitte',
    'Crop 04 separates the i point from the two tall t strokes and a reduced final e. There is no acute accent or distinct extra final e.', 'high','misread word',dc=True,dh=True,bbox=[808,330,946,379],crop='04_splitte.png',action='resolve')
add('C03','Raised label before Toute and its curved connector',r'\inserted{\unsure{Rmq}}',r'\emph{Remarque}',r'\inserted{Rmq}, raised above Toute with the curved connector drawn',
    'Upper half: capital R, compressed m and descending q are distinguishable. The curved stroke runs below the label toward the opening T; it is not ordinary baseline text.', 'high','abbreviation expanded or spelling modernised',dc=True,dh=True,bbox=[290,403,442,512],action='resolve')
add('F03','Remark: de un Gamma par un Z','de un $\\Gamma$ par un $Z$','de $\\Gamma$ par $Z$','de un $\\Gamma$ par un $Z$',
    'Upper half shows separate un traces after de and after par; both are written.', 'high','omission',dh=True,bbox=[1040,444,1487,515])
add('C04','Remark: canceled word before live l\u2019ext.',r"d'\deleted{\unsure{une}}l'ext.",r"d'une ext.",r"d'\deleted{\unsure{une}}l'ext.",
    'Crop 05 shows a dark horizontal cancellation over the short word, followed by a tall loop and apostrophe of live l\u2019ext. The canceled interior remains compressed.', 'low','deletion state (struck given live or live given struck)',dh=True,bbox=[1004,549,1098,586],crop='05_canceled_une.png',action='retain')
add('F11','Detached marks above/right of Z.Aut(Z)', '[omitted]','[omitted]','Two detached oblong points drawn, marked unsure without a punctuation assignment',
    'Crop 14 shows two dark oblong traces touching or nearly touching; their origin as writing versus ink/surface debris cannot be settled.', 'low','other',dc=True,dh=True,bbox=[1149,647,1163,666],crop='14_upper_detached.png')
add('F04','Divider below the remark',r'\figure{two nearly horizontal strokes}','[omitted]',r'\figure{two nearly horizontal strokes}',
    'Upper half: two distinct separated rules, upper slightly rising and longer; both retained as a TikZ drawing.', 'high','drawing or diagram',dh=True,bbox=[780,764,1025,802])
add('F05','Cardinal 2: noun after the double-headed arrow','torseur','torseurs','torseur',
    'Crop 06 shows the final small r-like return after the u; there is no additional s stroke.', 'high','misread word',dh=True,bbox=[1260,1077,1435,1129],crop='06_torseur_sur.png')
add('C05','Cardinal 2: preposition after torseur',r'\unsure{sur|sous}','sous',r'\unsure{sur|sous}',
    'Crop 06: the low waves end in a short downward turn. The compressed middle and ending do not exclude sous, although sur is the closer primary reading.', 'medium','misread word',dh=True,bbox=[1456,1082,1528,1127],crop='06_torseur_sur.png',action='retain')
add('F06','Cardinal 2: location of the opening parenthesis','ou encore, ... $\\mathbb F_2$ (ou encore,','(ou encore, ... $\\mathbf F_2$ ... ou encore,','ou encore, ... $\\mathbb F_2$ (ou encore,',
    'The halves show no opening curve before the first ou encore. Crop 09 shows a tall opening curve immediately before the second ou encore.', 'high','insertion or placement',dh=True,bbox=[343,1180,1414,1255],crop='09_canceled_word.png')
add('C06','Underlined espace affine: canceled short word and underline extent',r'\uline{espace affine \deleted{\unsure{sous}}}',r'\emph{espace affine sur $\mathbf F_2$}',r'\uline{espace affine \deleted{\unsure{sous|sur}}}',
    'Crop 07: a dark crossing stroke traverses the short word, independently of the long underline below it. A low loop permits sous; the obliterated end also permits sur. The underline stops before the field letter, as seen in the lower half and crop 08.', 'medium','deletion state (struck given live or live given struck)',dc=True,dh=True,bbox=[1017,1195,1093,1234],crop='07_canceled_sous.png',action='retain')
add('C07','First overwritten field, after the underlined phrase',r'\deleted{\unsure{\mathbb Z}}\mathbb F_2',r'\mathbf F_2',r'\deleted{\unsure{\mathbb Z|Z}}\mathbb F_2',
    'Crop 08: surviving oblique and lower strokes favor Z beneath the final doubled-upright F. The older letter\u2019s doubled versus single alphabet cannot be isolated securely from the overwriting.', 'medium','omission',dc=True,dh=True,bbox=[1113,1184,1166,1243],crop='08_overwritten_field.png',action='retain')
add('C08','After the second ou encore: obliterated word',r'(ou encore, \deleted{\illegible{1}}',r'\struck{\ill{}} ou encore,',r'(ou encore, \deleted{\illegible{1}}',
    'Crop 09: only an initial raised hook, the crossing stroke and a short lower projection survive. Attempts to read a word do not produce distinguishable letters. The deletion follows the comma, not the field preceding ou encore.', 'low','insertion or placement',marked=True,dh=True,bbox=[1431,1211,1543,1241],crop='09_canceled_word.png',action='retain')
add('C09','Box: decorative S alphabet',r'\unsure{\mathfrak S|\mathcal S}',r'\mathfrak S',r'\unsure{\mathfrak S|\mathcal S}',
    'Crop 10: large rounded outer sweep, inner return and raised upper-right tip; the handwritten alphabet remains ambiguous. The same primary alphabet is used at the later S_3.', 'medium','misread symbol or index',bbox=[1148,1595,1218,1659],crop='10_box_S.png',action='retain')
add('C10','Box: subscript of decorative S',r'_{\unsure{2|n}}',r'_2',r'_{\unsure{2|n}}',
    'Crop 10: the subscript is a shallow descending-then-rising trace; it lacks the fully separated head and foot of the clearer 2 on nearby Z. Both 2 and n remain possible.', 'low','misread symbol or index',bbox=[1215,1638,1247,1662],crop='10_box_S.png',action='retain',math='Check M01 establishes the expected degree-two comparison mathematically, but was not used to choose the written subscript.')
add('F12','Detached paired points to the right of the box','[omitted]','[omitted]','Two diagonal detached points drawn, marked unsure without a punctuation assignment',
    'Crop 15: two small dark spots lie diagonally, unlike an attached word or formula sign; ink versus surface trace remains unsettled.', 'low','other',dc=True,dh=True,bbox=[1501,1640,1519,1660],crop='15_box_detached.png')
add('C11','Parenthesized A_2 condition below the box',r'\unsure{\mathcal A|A}_2',r'\mathfrak A_2',r'\unsure{\mathcal A|A}_2',
    'Crop 11 shows a tall open rounded bowl and a short right stem, without the angular features expected of the proposed fraktur rendering. Calligraphic versus ordinary handwritten A remains open.', 'medium','misread symbol or index',dh=True,bbox=[940,1719,1008,1780],crop='11_A2.png',action='retain')
add('F08','Placement of the parenthesized A_2 condition',r'\[ (\unsure{\mathcal A|A}_2=\{1\}) \] (separate centered display)',r'\boxed{...}\qquad(\mathfrak A_2=\{1\}) (same baseline)',r'(\unsure{\mathcal A|A}_2=\{1\}), below the box toward its right',
    'Lower half: the condition is outside and below the box, with its opening near the box\u2019s midpoint; crop 11 confirms the complete parentheses and braces.', 'high','insertion or placement',dc=True,dh=True,bbox=[524,1570,1280,1800],crop='11_A2.png')
add('F09','Cardinal 3: vertical sign immediately under Aff(1,F_3)',r'\rotatebox{90}{$\simeq$}',r'\wr',r'\rotatebox{90}{$\simeq$}',
    'Lower half: one curved upright stroke has a separate straight upright immediately to its right. Both components are retained.', 'high','misread symbol or index',dh=True,bbox=[797,1949,832,1984])
add('C12','Cardinal 3: vertical sign between F_3^+ and Z_3',r'\rotatebox{90}{$\unsure{\simeq|=}$}',r'\note{signes $\simeq$ et $=$ verticaux ...}',r'\rotatebox{90}{$\simeq$}',
    'Crop 12 shows a curved left stroke and a straighter right stroke. The left is visibly unlike the two straighter strokes in the neighboring equality, even though the middle is heavily inked.', 'high','misread symbol or index',dc=True,bbox=[739,2057,769,2093],crop='12_lower_signs.png',action='resolve',math='The additive group of F_3 is cyclic of order three, but the stroke shape, not that fact, resolves the sign.')
add('F10','Final display: recurring A_3 alphabet',r'\mathcal A_3',r'\mathfrak A_3',r'\mathcal A_3',
    'Lower half: the same rounded open A construction seen in the A_2 condition recurs. Its uncertainty is marked at the first occurrence only, following the recurring-glyph convention.', 'medium','misread symbol or index',dh=True,bbox=[559,2148,637,2225])
add('C13','Final display: canceled Z under F_3^+',r'\deleted{\unsure{\mathbb Z}}\mathbb F_3^+',r'\mathbf F_3^+',r'\deleted{\mathbb Z}\mathbb F_3^+',
    'Crop 13 separates two oblique strokes and the older top/bottom Z strokes from the upright F strokes. The double-stroked Z underform is readable here.', 'high','omission',dc=True,dh=True,bbox=[722,2153,787,2216],crop='13_last_field.png',action='resolve')

def inv(element,kind,position,first,hand='his hand'):
    return dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inventory=[
inv('Two-row extension diagram','diagram','top, [393,70,1295,260]','1, Z, G, Gamma, 1; G\u2032, Gamma\u2032; (E), (E\u2032)'),
inv('Conditional paragraph','text','[298,320,1330,388]',"Si l'extension (E) splitte"),
inv('Raised remark abbreviation','insertion','[291,403,397,449]','Rmq'),
inv('Curved remark callout stroke','drawing','[298,432,395,488]','curved connector from below Rmq toward Toute'),
inv('Remark paragraph','text','[317,453,1484,624]','Toute extension splittée G de un Gamma par un Z'),
inv('Canceled short word in remark','deletion','[1004,549,1098,586]','une, uncertain, before live l\u2019ext.'),
inv('Remark product display','display','[284,658,527,719]','Z.Aut(Z).'),
inv('Detached upper traces','drawing','[1149,647,1163,666]','two small oblong dark traces; uncertain writing/debris','unnamed hand'),
inv('Double divider','drawing','[780,764,1025,802]','two horizontal rules'),
inv('Section heading','text','[300,900,1152,968]','4) Ens. de petit cardinal'),
inv('Subsection a heading and underline','text','[294,1073,631,1143]','a) Cardinal 2'),
inv('Cardinal-two paragraph','text','[343,1078,1621,1557]','Ens de cardinal 2; torseur; espace affine; can. isomorphes'),
inv('Underlined words','drawing','[653,1242,1120,1259]','underline beneath espace affine and the canceled short word'),
inv('Canceled preposition','deletion','[1017,1195,1093,1234]','sous|sur'),
inv('Overwritten first field underform','deletion','[1113,1184,1166,1243]','double/plain Z beneath F_2'),
inv('Obliterated word','deletion','[1431,1211,1543,1241]','one unreadable word after second ou encore'),
inv('Boxed cardinal-two comparison','display','[579,1600,1243,1677]','Aff(1,F_2) simeq Aff(Z_2) simeq decorative S with subscript 2|n'),
inv('Hand-drawn enclosure','drawing','[527,1564,1277,1718]','four roughly rectilinear sides; upper-left and lower-right gaps'),
inv('Detached points beside enclosure','drawing','[1501,1640,1519,1660]','two diagonal points; uncertain writing/debris','unnamed hand'),
inv('Parenthesized condition below/right of box','display','[902,1716,1185,1799]','(A_2={1})'),
inv('Subsection b heading and underline','text','[327,1781,675,1855]','b) Cardinal 3'),
inv('Cardinal-three multi-level comparison','display','[524,1878,1545,2135]','S_3; Aff(1,F_3); Gl(2,F_2); GP(1,F_2); lower field factors, vertical signs, cyclic groups, quotient'),
inv('Final alternating-group comparison','display','[555,2143,987,2233]','A_3 simeq F_3^+ (simeq Z_3)'),
inv('Overwritten final Z','deletion','[722,2153,787,2216]','double-stroked Z under F_3^+'),
inv('Archive foliation, comment only','margin note','lower left, [42,2279,116,2320]','12','unnamed hand')]

notation=[
{'sign':'Z, G, Gamma; prime','reading':r'Z,G,\Gamma; G\prime,\Gamma\prime','ink':'Plain single Z diagonals, rounded G with short ledge, angular Gamma; detached raised prime ticks.','place':'top diagram and remark'},
{'sign':'small upward-arrow label','reading':r'\unsure{2|\wr}','ink':'Small continuous hooked form with a low right foot; no visible d.','place':'between the two top-diagram Z objects'},
{'sign':'double-stroked F and Z','reading':r'\mathbb F_2,\mathbb F_3,\mathbb Z_2,\mathbb Z_3','ink':'Separated upright strokes on F and separated oblique strokes on Z; each clear live occurrence inspected in the halves. H\u2019s declared bold encoding is equivalent here.','place':'cardinal-two and cardinal-three blocks'},
{'sign':'decorative S','reading':r'\unsure{\mathfrak S|\mathcal S}, later \mathfrak S','ink':'Large outer rounded sweep, small inner return, and raised tip; alphabet remains ambiguous.','place':'box and opening of cardinal-three comparison'},
{'sign':'rounded A','reading':r'\unsure{\mathcal A|A}, later \mathcal A','ink':'Tall open bowl with a short right stem, no secure angular/fraktur construction.','place':'A_2 condition and final A_3'},
{'sign':'simeq and equals, rotated','reading':r'\simeq,\rotatebox{90}{$\simeq$},\rotatebox{90}{$=$}','ink':'Curved-plus-straight pairs distinguish isomorphisms from the neighboring pair of upright straight strokes.','place':'comparison displays and vertical correspondences'},
{'sign':'plus, asterisk, low multiplication point','reading':r'{}^{+},{}^{*},.','ink':'Raised cross and raised asterisk; separate product point at the field-letter baseline.','place':'F_3^+.F_3^*, quotient denominator, final F_3^+'},
{'sign':'Gl; GP','reading':r'\operatorname{Gl},\operatorname{GP}','ink':'Narrow lower-case l after G in Gl; upright capital P after G in GP.','place':'cardinal-three comparison and quotient'}]
abbr=[{'written':'ext.','expansion':'extension'},{'written':'Rmq','expansion':'Remarque'},{'written':'Ens. / Ens','expansion':'Ensembles / Ensemble'},{'written':'dim','expansion':'dimension'},{'written':'vect.','expansion':'vectoriels'},{'written':'can.','expansion':'canoniquement'}]
notes=[
'The page continues an extension diagram and discusses splitting, then begins section 4, Ens. de petit cardinal, with a) Cardinal 2 and b) Cardinal 3. No date appears. Archive 12 is recorded only in a comment.',
'The raised Rmq and its curved callout are preserved; this is not a full written Remarque heading. The literal de un Gamma and par un Z are retained.',
'No authorial doubt word or question mark was identified. Editorial uncertainty remains at compressed words, alphabets, the boxed subscript, and two detached trace pairs.',
'All three images were displayed once in the prescribed order: whole, upper half, lower half. Fifteen distinct tight crops were then created and displayed once each; no settled locus was recropped.',
'S.json is the empty array: there are no sweep rows to confirm or overturn. The packet contains no H_drawings supplement.',
'H\u2019s page marker, bold encodings of doubled fields, and equivalent operator macros are not counted as collation differences. H\u2019s uncertainty on Ens. has the same primary reading and is not counted as a substantive difference.',
'The underlined space-affine phrase ends before the field symbol. The parenthesized A_2 condition is below/right of the box. The lower field factors, both vertical correspondences and cyclic groups are physically retained in their separate levels.',
'The two detached paired-trace loci are drawn without interpreting them as punctuation or mathematical signs; writing versus debris is unresolved.',
'Mathematical expectations did not decide the small diagram label, the boxed subscript, or either ambiguous alphabet. The stated checks below are actual calculations, separated from visual transcription checks.'
]
checks=[
{'id':'M01','statement':'Aff(1,F_2) has two elements and acts as all permutations of its two points; A_2 is trivial.','event_type':'explicit algebraic check','reasoning':'An affine map has the form x -> ax+b. In F_2 the only nonzero a is 1, and b is 0 or 1, producing the identity and the swap. Only the identity among these two permutations is even.','outcome':'The degree-two group comparison and the trivial alternating group are consistent. This does not select the written S subscript between 2 and n.'},
{'id':'M02','statement':'The degree-three comparison groups have faithful permutation actions of order six; F_3^+ and F_3^* have orders three and two.','event_type':'explicit counting and faithfulness check','reasoning':'Aff(1,F_3) has 3 times 2 = 6 distinct affine maps of a three-element set, so its faithful action gives S_3. Gl(2,F_2) has (4-1)(4-2)=6 matrices; its action on the three nonzero vectors is faithful because fixing a basis fixes the linear map. F_2^* has one element, so quotienting Gl(2,F_2) by it changes nothing. Addition in F_3 is cyclic of order three, and F_3^*={1,2} is cyclic of order two.','outcome':'The written comparison chain, lower correspondences and quotient are mathematically consistent, without using cardinality alone as a proof of the first two isomorphisms.'},
{'id':'M03','statement':'A_3 is cyclic of order three.','event_type':'explicit permutation check','reasoning':'The even permutations on three letters are the identity and the two 3-cycles. A 3-cycle generates these three elements.','outcome':'The final A_3 comparison with the additive group of F_3 and Z_3 is consistent; the overwritten letter was read from crop 13 independently.'}
]
unresolved=[
{'place':'top Z-to-Z arrow label','reading':r'\unsure{2|\wr}','alternatives':'2; upright wave (wr)','confidence':'medium'},
{'place':'remark cancellation before l\u2019ext.','reading':r'\deleted{\unsure{une}}','alternatives':'une; exact interior obscured by cancellation','confidence':'low'},
{'place':'after torseur','reading':r'\unsure{sur|sous}','alternatives':'sur; sous','confidence':'medium'},
{'place':'canceled short word after espace affine','reading':r'\deleted{\unsure{sous|sur}}','alternatives':'sous; sur (both definitely canceled)','confidence':'medium'},
{'place':'first overwritten field','reading':r'\deleted{\unsure{\mathbb Z|Z}}\mathbb F_2','alternatives':'double-stroked Z; plain Z under the final F','confidence':'medium'},
{'place':'after second ou encore','reading':r'\deleted{\illegible{1}}','alternatives':'one canceled word; surviving projections do not support a letter-complete candidate','confidence':'low'},
{'place':'box and recurring S_3 alphabet','reading':r'\unsure{\mathfrak S|\mathcal S}','alternatives':'fraktur S; calligraphic S','confidence':'medium'},
{'place':'boxed S subscript','reading':r'_{\unsure{2|n}}','alternatives':'2; n','confidence':'low'},
{'place':'A_2 and recurring A_3 alphabet','reading':r'\unsure{\mathcal A|A}','alternatives':'calligraphic A; ordinary handwritten A','confidence':'medium'},
{'place':'detached upper trace pair','reading':'uncertain paired-trace TikZ drawing','alternatives':'ink traces; surface/debris marks; no punctuation assignment','confidence':'low'},
{'place':'detached trace pair to right of box','reading':'uncertain paired-point TikZ drawing','alternatives':'ink traces; surface/debris marks; no punctuation assignment','confidence':'low'}
]
map_=[{'id':f'C{i:02}','finding_id':f'C{i:02}','disposition':next(x['doubt_action'] for x in findings if x['id']==f'C{i:02}')} for i in range(1,14)]
report=dict(scan=13,reader='R3',start_utc='2026-11-20 03:35:49 UTC',end_utc='',images_viewed=[
'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013.jpg',
'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_a.jpg',
'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_b.jpg'],reading_file=str(p/'reading.tex'),crop_count=15,findings=findings,inventory=inventory,notation=notation,abbreviations=abbr,notes=notes,checks=checks,unresolved=unresolved,c_doubt_map=map_,sweep_rows=[],image_dimensions={'whole':[1687,2362],'upper_half':[1687,1261],'lower_half':[1687,1261],'lower_half_original_y_offset':1101},self_check={})
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
m=json.loads((p/'crop_manifest.json').read_text())
for c in m['crops']: c['viewed']=True
m['crop_count']=len(m['crops'])
(p/'crop_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
s=(p/'reading.tex').read_text().replace(r'\begin{array}{c@{\;}c@{\;}c}',r'\begin{array}[t]{c@{\;}c@{\;}c}')
(p/'reading.tex').write_text(s)
print('Wrote complete reading and report:',len(findings),'findings,',len(inventory),'inventory entries,',len(unresolved),'remaining doubt loci.')
