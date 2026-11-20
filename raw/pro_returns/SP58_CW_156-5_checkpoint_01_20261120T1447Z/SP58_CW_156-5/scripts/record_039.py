from records import commit,OUT
tex=(OUT.parents[1]/'source/SP58_CW_156-5_witnesses/codex/J156-5-05/pages/J156-5-05_156-5_scan039.tex').read_text()
for a,b in [(r"(S',T')\leq(S,T)",r"(S',T')\preccurlyeq(S,T)"),(r"$F'\leq F$",r"$F'\preccurlyeq F$"),(r'\rotatebox{90}{$\leq$}',r'\rotatebox{90}{$\preccurlyeq$}'),(r'\unsure{ultra}','ultra'),(r'\unsure{cette ultra}','cette ultra'),(r'\unsure{quelc.}','quelc.'),(r'\unsure{on reprend|en reprenant}','on reprend'),(r'\unsure{G|C}','G'),(r'\unsure{en}','en'),(r'\unsure{prend}','prend'),(r'\unsure{réunions}','réunions'),(r'{\unsure{\tau|\mathcal T}}_0^{\unsure{+|*}}',r'\tau_0^{+}'),(r'\unsure{notion|création|coïtion}','notion'),(r'\unsure{induite|intersection}','induite'),(r'\unsure{images inverses}','images inverses'),(r'\unsure{relations de préordres|relation des préordres}','relations de préordres'),(r'\unsure{donc ici}','donc ici'),(r'\unsure{i|j}','i')]:
 assert a in tex,a
 # Only the first vertical comparison is the curved subdivision sign.
 tex=tex.replace(a,b,1) if a==r'\rotatebox{90}{$\leq$}' else tex.replace(a,b)
ch=[]
def add(place,c,h,f,e,k='misread word',conf='high',ac=False,ah=True,hm=False,con=''):ch.append((place,c,h,f,e,k,conf,ac,ah,hm,con))
add('opening displayed comparison','≤','≼','≼','Upper half y70–130: bowed upper wedge and curved lower stroke, unlike the straight ≤ in the topology comparison.','misread symbol or index','high',True,False,False,'Subdivision sign ≼ retained for equal-support refinement; ordinary ≤ is used separately for topologies.')
add('first small array, vertical comparison','≤ rotated','≼ (linearised)','≼ rotated','Upper half y600–645: two bowed strokes, rotated relative to the horizontal subdivision sign.','misread symbol or index','high',True,False)
add('F′ compared with F in main text','≤','≼','≼','Lower half y1290–1345: same curved sign as at the top of the page.','misread symbol or index','high',True,False)
add('margin first block, ultra insertion and deletion','inserted double-underlined ultra; cancelled ultra after topologie','ill. before topologie','C insertion and deletion retained','039 margin1 crop (20,17,310,850), rotated −90°: ultra is inserted above with two underlines; a separate ultra on the baseline is crossed.','insertion or placement','high',False,True,True)
add('margin first block, family insertion','inserted la famille des','les','inserted la famille des','Same margin1 crop: full phrase below the S→S_i line, attached by a curved guide.','insertion or placement')
add('margin first block, after S_i','muni de T_i :','munis de T_i), i.e.','muni de T_i :','Same margin1 crop: muni has no s; colon follows T_i, with no closing parenthesis or i.e. on this baseline.','text not on the page')
add('margin first block, crossed start','cette ultra','ill.','cette ultra','Same margin1 crop: tall t strokes and looped ultra survive beneath horizontal strike.','readable ink left as \\ill{}','medium',False,True,True)
add('margin first block, live continuation','top. pour une famille quelc. d’applications','la top. ill. ill. famille d’applications','top. pour une famille quelc. d’applications','Same margin1 crop: pour une and quelc. are visible in the two lines; no extra la.','readable ink left as \\ill{}','high',False,True,True)
add('margin first block, cancelled map start','f, uncertain','omitted','f, uncertain','Same margin1 crop: small crossed descender above the rewritten f_i.','omission','low')
add('margin first block, map shaft','bare line','arrow','bare line','Same margin1 crop: f_i:S–S_i has a straight blunt shaft.','drawing or diagram')
add('margin second block opening','de S dans des S_i munis de T_i existe toujours, en ultr. topologie','ill. des S_i munis de T_i ill. toujours, on a la topologie','de S dans des S_i munis de T_i existe (doubtful) toujours, en ultr. topologie','039 margin2 crop (15,850,366,1450), rotated −90°: de S dans des and munis legible; existe is crowded; after comma a reduced en; underlined ultr. precedes topologie.','readable ink left as \\ill{}','medium',False,True,True)
add('margin second block, before inverse images','inserted fermés','omitted','inserted fermés','Same margin2 crop: small fermés beneath les, with an upward placement mark.','omission')
add('margin second block, after F_i','fermé ds T_i','fermé dans T_i','fermé ds T_i','Same crop: abbreviation ds, not expanded.','expansion or normalisation')
add('margin second block, generation','intersections quelc. de réunions quelc. d’ensembles de la forme','intersections ill. réunions quelconques ill. de la forme','intersections quelc. de réunions quelc. d’ensembles de la forme','Same margin2 crop: both quelc. abbreviations, de and d’ensembles visible; intersections is inserted above cancelled réunions.','readable ink left as \\ill{}','high',False,True,True)
add('margin third block, cancelled engendrée','engendrée, doubtful','ill.','engendrée, doubtful','039 margin3 crop (17,1430,295,2035), rotated −90°: long g loop survives beneath the heavy cancellation.','readable ink left as \\ill{}','low',False,True,True)
add('margin third block, revision after induite','cancelled de des; inserted images inverses','par une famille de','cancelled de des, doubtful; inserted images inverses','Same margin3 crop: crossed de-like groups above a distinct inserted images inverses; no par une famille.','insertion or placement','medium')
add('margin third block, parenthesis','(relations de préordres), opening doubtful','relations de préordres, no parentheses','(relations de préordres), opening doubtful','Same margin3 crop: closing curved bracket clear; opening partly merged with guide line.','omission','medium')
add('margin third block, cancelled final words','donc ici, doubtful','omitted','donc ici','Same margin3 crop: d and c at left and two dotted i-like strokes at right beneath one cancellation.','omission','medium')
add('first array, old letter under G′','cancelled F','omitted','cancelled F, doubtful','Upper half: straight stem and short crossbar survive at left of the overwritten G′.','omission','low')
add('second array, old words','cancelled on a','ill.','cancelled on a, doubtful','039 array crop (628,850,918,1090): terminal a-like loop and initial rounded strokes amid dense zigzag cancellation.','readable ink left as \\ill{}','low',False,True,True)
add('second array, T–S','hooked headless line','hooked arrow','hooked headless line','Upper half: hook at T end and no point at S.','drawing or diagram')
add('topology symbols, throughout page','τ family','calligraphic T family','τ family','Upper/lower halves: continuous looped tau with descending curved tail, repeated in the arrays, inequalities and prose.','misread symbol or index')
add('second array, decoration on τ_0','+ / *','unreadable superscript in note','+','Array crop: one upright and a short rightward cross stroke, without asterisk diagonals.','misread symbol or index','high',False,True,True)
add('T fermé de','de','dans','de','Lower half first baseline: reduced de, no ans extension.','misread word')
add('before induisent τ′_0','cancelled in','omitted','cancelled in, doubtful','Lower half y1540–1585: short i/n-like start crossed before the restarted induisent.','omission','medium')
add('condition 2 first object','cancelled S before T','T alone','cancelled S before T, doubtful','Lower half: looped old capital extends below the live T crossbar.','omission','low')
add('power-set glyphs at foot','P / calligraphic variants; P_tau','Fraktur P','P / calligraphic variants; P_tau','Lower half y2010–2130: plain angular bowl and upright, not a recognisable Fraktur form; first glyph remains style-ambiguous.','misread symbol or index','medium')
add('foot, before A∈P_tau','i.e., live and uncertain','cancelled ill.','i.e., live and uncertain','039 ie crop (335,2065,440,2150): reduced retraced letters and dots, without a distinct horizontal cancellation.','readable ink left as \\ill{}','low',False,True,True)
add('foot universal quantifier','underlined ∀','underlined tout','underlined ∀','Lower half, y2145–2195: explicit quantifier glyph with short underline.','expansion or normalisation')
add('foot raised hypothesis','Si on veut =′ τ′_0=τ′|T','Si ill. ill. τ′_0=τ′|T','Si on veut =′ (doubtful) τ′_0=τ′|T','039 foot crop (820,2160,1615,2340): Si on veut is readable and an equal sign plus detached prime-like mark precede the separate restriction equation.','readable ink left as \\ill{}','medium',False,True,True)
add('foot T étant fermé','baseline T étant fermé, cancelled pou then pour τ','inserted T étant fermé pour τ','baseline T étant fermé, cancelled pou (doubtful) then pour τ','Foot crop: this baseline follows the inserted hypothesis; the guide belongs to the hypothesis, not a separate insertion of T étant fermé.','insertion or placement','medium')
add('foot parties de T','cancelled de; inserted fermées; de T, inserted pour τ′_0','cancelled fermées; de T; cancelled pour τ′_0','C states retained','Foot crop: fermées sits above a crossed short de-like group; pour τ′_0 is above the baseline with a guide, not struck.','insertion or placement','high')
inv=[('text','top centre','38'),('display','opening','(S′,T′)≼(S,T)'),('text','opening continuation','signifie que S′=S'),('margin note','left upper vertical','Description de meet_i(S_i,T_i)'),('insertion','left upper vertical','ultra; la famille des'),('deletion','left upper vertical','ultra; cette ultra; f'),('text','upper','Revenons à la situation'),('diagram','upper','G⊂F; G′ below G'),('deletion','first array','F under G′'),('text','before second array','donc, posant T=|G|, S=|F|'),('margin note','left middle vertical','de S dans des S_i'),('insertion','left middle vertical','fermés; intersections'),('deletion','left middle vertical','réunions'),('diagram','middle','T–S; τ_0+ above τ′_0'),('deletion','left of second array','on a'),('text','middle','T fermé de (S,τ)'),('deletion','middle','topologies; in'),('margin note','left lower vertical','correspond à la notion'),('deletion','left lower vertical','engendrée; de des; donc ici'),('insertion','left lower vertical','induite; images inverses'),('display','lower','1° and 2° continuity conditions'),('deletion','condition 2','S'),('text','lower','situation mixte à cheval'),('diagram','lower','T→S→S with τ′_0,τ′?,τ'),('margin note','right of diagram','on sait que le composé est continu'),('text','foot','Donc on veut (i)'),('deletion','foot','i.e.; pou; de'),('insertion','foot','Si on veut =′ τ′_0=τ′|T; fermées; pour τ′_0')]
notes='''### 039-N1 — Statements

Same-support subdivision corresponds to a finer topology, with reversed topology order (more closed sets means smaller in the written order). The main problem is extension of a refined topology τ′_0 on a closed T⊂S to a refinement τ′ of τ. The two displayed continuity requirements are distinguished from the further requirement that the restriction equal τ′_0. The final insertion makes that extra requirement explicit. Manuscript page 38; no date.

### 039-N2 — Margin and interpretation

The sideways note describes the meet of figures using S=intersection of the S_i and the initial ultratopology. It prescribes arbitrary intersections of arbitrary unions of inverse images of closed sets, after cancelling réunions in favour of intersections. Its preorder formula is x≤y iff f_i(x)≤f_i(y) for every i. The order of the displayed revisions is preserved; the words images inverses are inserted, not the phrase par une famille supplied by H. The first topology in the array has an unexplained plus decoration, retained as τ_0+; no later formula on this sheet explains it.

### 039-N3 — Reading checks and scope

The mathematical roles prompted close examination of the subdivision signs and the distinction between continuity and equality of the restriction. Ink, not that expectation, determines the choices. No new proof or experiment was performed for the initial-ultratopology construction or extension problem on this page. Remaining uncertainty is concentrated in overwritten words and the reduced =′ sign in the final insertion.'''
doubts=r'''| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| margin 1 cancelled f | f | unidentifiable crossed descender | low |
| first array old letter | F | obscured capital | low |
| margin 2 verb | existe | no secure alternative | low |
| second array old words | on a | heavily crossed remnants | low |
| main crossed word start | in | no secure alternative | medium |
| margin 3 cancellation | engendrée | no secure alternative | low |
| margin 3 short cancellation | de des | overlapping de-like starts | low |
| margin 3 opening parenthesis | ( | insertion guide | low |
| condition 2 old letter | S | obscured loop | low |
| first P style | P | calligraphic/script P | medium |
| first i.e. at foot | i.e. | reduced/retraced abbreviation | low |
| raised sign after Si on veut | =′ | unexplained sign, possibly abbreviation | low |
| cancelled before pour τ | pou | overwritten pour start | medium |
| after parties | cancelled de; live de | dense insertion guide obscures state | low/medium |

All 31 C doubt entries were examined. Resolved by the halves or six locus crops: ultra, cette ultra, quelc., on reprend, G, en, prend, réunions, τ and its +, notion, inserted induite, images inverses, relations de préordres, cancelled donc ici, and map i. The remaining table retains the unresolved places explicitly.'''
hand='''Across this sheet the curved ≼ appears at the top, in the first vertical array and between F′ and F. Straight ≤ compares the topologies and points of preorders. The topology glyph is a looped τ, unlike a capital T. Its raised decoration in the second array is a two-stroke +. The marginal word notion is highly reduced but its not- and -tion strokes are separable. Long insertion guides pass through neighbouring writing and should not be treated as blanket deletions.'''
commit(39,tex,ch,inv,notes,doubts,hand,notation='τ,τ′,τ_0,τ′_0 are topology symbols; the isolated τ_0+ is unexplained. F′≼F is a same-support subdivision. The topology convention τ′≤τ means finer. P(S),P_τ(S) denote subsets and closed subsets.',abbr='ultr. = ultra; quelc. = quelconques; ds = dans; top. = topologie; = probably même, but the following prime-like mark is unexplained.')
