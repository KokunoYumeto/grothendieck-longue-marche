from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
d={'cote':53,'scan':6,'sheet_kind':'text','hand':'his hand','replace':[
(r'\unsure{2/|2)}','2/'),
(r'\deleted{\unsure{Si}}',r'\deleted{Si}'),
('hom de groupes','hom de g.pes'),
(r'\deleted{spécialisation} générisation}',r'\deleted{spécialisation} générérisat.}'),
(r'\deleted{\uline{\unsure{Prop}} Su} $H$ réduit',r'\deleted{\uline{\unsure{Prop}} Su} avec $H$ réduit'),
('générisation et contient}',r'générisation et \unsure{cont.|contient}}'),
(r'\unsure{ouvert|affine}',r'\unsure{affine|ouvert}'),
(r'\unsure{b)|c)}','b)'),
(r'\deleted{\unsure{OK}}',r'\deleted{OK}'),
(r'\deleted{\unsure{avec}}',r'\deleted{avec}'),
(r'\unsure{que|pour}','pour'),
(r'\unsure{spécia|spéc.}','spécia'),
(r'\unsure{ev.|ev}','ev.'),
(r'\unsure{profétales|profinis}','profétales'),
(r'\unsure{f.}','f.'),
(r'tordus\unsure{)|{}}','tordus'),
(r'\unsure{\underline{\approx}|\cong}',r'\underline{\approx}')
], 'review':'Personally read the whole image and both halves, then enlarged every block, deletion, insertion, critical formula and diagram. Both slanted margin notes were rotated (first clockwise 47° then 31°, second 49° then 36°) and viewed at 3×, with the clearer rotations used for decisions. Small details were viewed at 4–5×; the opaque cancelled proof word at 6×. The large cancellation starts at the discarded concluding clause and corollary, not at the preceding proposition heading. Every word in the diagrams and lower table was read. No context was opened.',
'decisions':[], 'inventory':[]}
# Correct the intentionally explicit replacement target below to the exact observed abbreviation.
d['replace']=[(x,y.replace('générérisat.','générisat.')) for x,y in d['replace']]
def a(place,c,h,final,shows,conf='high',cc=False,hc=False,kind='other',marked='no',conseq=None):
 x=dict(place=place,c=c,h=h,final=final,shows=shows,confidence=conf,c_changed=cc,h_changed=hc,kind=kind,marked_in_H=marked)
 if conseq:x['consequential']=conseq
 d['decisions'].append(x)
a('opening number',r'\unsure{2/|2)}','4)','2/','A small looped 2 is followed by a straight oblique slash, without the hook of a parenthesis. (137,214,187,250), 4×.','medium',True,True,'misread symbol or index')
a('opening replacement hypothesis','inserted stable par spécialisation','same words inline','C retained','The phrase is above the cancelled ouvert et fermé, attached as its replacement. Top (131,175,1668,415), 2×.',hc=True,kind='insertion or placement')
a('opening inverse image containment',r'\pi^{-1}(W)\subset G\times W',r'\pi^{-1}(W)\subset G^0\times W','C retained','The G has no upper-right exponent, in contrast to the two clearly raised zeros on the following lines. Top, 2×.',hc=True,kind='misread symbol or index',conseq='The ambient product is G×W; H adds an unwritten exponent 0.')
a('upper separator drawing','two short horizontal strokes','omitted','C drawing retained','Two separate unequal strokes are visible in the whole and top-half image; upper line longer and slightly sloping.',hc=True,kind='drawing or diagram')
a('proposition deletion extent','proposition live with local deletions','whole proposition struck','C retained','No oblique cancellation crosses the heading or assertion. The enclosure turns from the discarded donc clause down into the following corollary. Prop (187,479,1624,692), 2×; cancelledcor (225,639,1674,1014), 2×.',hc=True,kind='deletion state (struck given live or live given struck)',conseq='The initial proposition is not globally cancelled; the later discarded corollary is.')
a('proposition overwritten map label',r'\deleted{\unsure{\lambda|v}}u','u only','C retained','A long earlier stroke extends below the arrow and is cancelled at its foot; the exact earlier label remains uncertain. (484,483,556,568), 4×.','low',hc=True,kind='omission')
a('proposition deleted Si',r'\deleted{\unsure{Si}}',r'\ill{}',r'\deleted{Si}','The large S and separate i-dot survive the diagonal crossing. (627,503,718,545), 4×.','high',True,True,r'readable ink left as \ill{}')
a('proposition group abbreviation','hom de groupes','hom de gr. uncertain alg.','hom de g.pes','The ink has a g, a detached dot, and compressed pes; no alg. is written here. (729,497,1100,557), 4×.','medium',True,True,'abbreviation expanded or spelling modernised','yes')
a('proposition cancelled compactness hypothesis','avec G qu. cpt','ill.','C retained, deleted','The whole short phrase is crossed once; G and the compactness abbreviation remain readable. Prop, 2×.',hc=True,kind=r'readable ink left as \ill{}')
a('proposition pointwise hypothesis','Si u est plat (inserted générisant) en un p^t','Si u est plat sur un uncertain ouvert; générisant displaced','C retained','The preposition en and un are visible, followed by p with a raised t. The parenthesized replacement sits directly above plat and is led into that position. Prop, 2×.',hc=True,kind='insertion or placement',marked='yes',conseq='The written hypothesis is at one point, not on an open subset.')
a('proposition discarded generic-point parenthesis',r'\deleted{(au \unsure{p. gén.})}',r'\ill{}','C retained','The letters after au are heavily crossed; a p-like stroke, dot and descending g remain. (961,533,1164,585), 4×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('proposition universal replacement','inserted (underlined univ générisant)','univ. générisant elsewhere','C retained','The replacement is above the second plat; univ is underlined and has no terminal period. Prop, 2×.',hc=True,kind='insertion or placement')
a('proposition cancelled et donc est plat',r'et \unsure{donc} \unsure{est} plat',r'\ill{}','C retained, deleted','et and plat are distinguishable; the intervening rounded strokes lie beneath a thick double bar, so donc and est stay doubtful. (970,572,1381,617), 4×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('proposition discarded image conclusion','deleted donc u(G) stable par deleted spécialisation générisation','fragmentary ill. u(G) stable par ill. générisat.','deleted donc u(G) stable par deleted spécialisation générisat.','The phrase has its own enclosure/cancellation; spécialisation is independently overwritten. The replacement word ends in a crossed t and detached dot, with no ion. Prop 2×; (832,627,1074,690), 4×.','high',True,True,r'readable ink left as \ill{}')
a('first slanted margin','Il faut un argument pour double-quoted univ générisant','several words uncertain; guillemets and univ.','C retained','All words are readable after rotation, including un argument; the quotes are paired short strokes and univ has no terminal dot. (24,630,241,946), clockwise 31°, 3×.',hc=True,kind='misread word',marked='yes')
a('cancelled corollary abandoned opening',r'\deleted{que H \unsure{qu cpt} qu’il existe}','omitted','C retained','The strike traverses an earlier que H compactness phrase and first qu’il existe, before the repeated live-within-draft wording. (700,718,819,761), 4×; cancelledcor 2×.','low',hc=True,kind='omission')
a('cancelled corollary overwritten X',r'\deleted{\unsure{X}}','omitted','C retained','Two crossing diagonal forms and extra cancellation strokes remain before u est plat. (229,868,277,918), 4×.','low',hc=True,kind='omission')
a('cancelled corollary reducedness insertion','inserted si H est réduit','same words inline','C retained','The condition is above u est plat with a curved guide. Cancelledcor, 2×.',hc=True,kind='insertion or placement')
a('cancelled corollary second-level cancellation',r'\deleted{donc généris\unsure{ant} (donc générisant ...)}','same words without inner cancellation','C retained','An additional horizontal stroke crosses this whole subordinate phrase inside the globally cancelled draft. The first ant ending remains compressed. Cancelledcor 2×; (725,851,893,895), 4×.','low',hc=True,kind='deletion state (struck given live or live given struck)')
a('cancelled corollary inserted ne','inserted ne','ne inline','C retained','The short ne is above on suppose pas. Cancelledcor, 2×.',hc=True,kind='insertion or placement')
a('cancelled corollary aborted Prop Su',r'\deleted{\uline{\unsure{Prop}} Su}','omitted','C retained','A dense struck heading has a surviving p descender and underline; Su is crossed to its right. (234,922,335,969), 4×; cancelledcor 2×.','low',hc=True,kind='omission')
a('cancelled corollary before H réduit','nothing','nothing','avec','A small a-v join, short upper e stroke and open terminal c stand before H réduit. (438,914,541,961), 4×.','medium',True,True,'omission')
a('cancelled corollary local et and de',r'\deleted{et}; \deleted{\unsure{de}}','ill.','C retained','et is locally blacked; the later small word after l’image is crossed heavily and stays tentative de. (1460,904,1516,948), 4×; cancelledcor 2×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('cancelled corollary final inserted en and ending','inserted en before par; et contient','no en; ending ill.',r'inserted en before par; et \unsure{cont.|contient}','The small en is above par. The last word is compressed to c...t with a dot-like terminal mark; cont. is favored over an expanded contient. (235,963,1168,1016), 4×.','low',True,True,'omission')
a('live corollary cancelled qualifier',r'\deleted{\unsure{ouvert|affine}}','omitted',r'\deleted{\unsure{affine|ouvert}}','Two high f-like strokes favor affine, but the crossing prevents a secure full reading. (331,1077,436,1108), 4×.','low',True,True,'omission')
a('live corollary universal insertion','univ','univ.','univ','No terminal dot appears after the final v; it is inserted above générisant. Cor (239,1029,1690,1342), 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
a('live corollary b function letter',r'\unsure{U(G)|u(G)}','u(G)','C retained','The rounded letter is unusually tall, with two vertical sides; case remains uncertain. (421,1166,473,1207), 4×.','low')
a('live corollary b group index',r'\deleted G H_0','H^0',r'\deleted G H_0','A G is overwritten by H and the small 0 is below the baseline at right. Cor, 2×.',hc=True,kind='misread symbol or index',conseq='The written index is a subscript 0 and the overwritten G is retained.')
a('live corollary c inserted point label','inserted x','x inline','C retained','Small x sits above the line immediately after maximal, with an insertion guide. Cor, 2×.',hc=True,kind='insertion or placement')
a('live corollary cancelled parenthesis',r'(donc \unsure{fermé si} G qu. cpt)',r'(\ill{})','C retained, deleted','donc and G qu. cpt are readable; between them the tall f and low joins remain crossed. (1214,1296,1410,1341), 4×; cor 2×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('live corollary right-margin cancelled qualification',r'\deleted{\unsure{et H l. t. f.}}',r'c) trailing \ill{}','C retained','The oval-enclosed note at the right contains H and tall t/f strokes, crossed along the baseline. The small lead-in is uncertain. (1526,1248,1700,1319), 4×.','low',hc=True,kind='insertion or placement')
a('proof first implication',r'a)\Longrightarrow a prime)','a) iff a prime)','C retained','The double horizontal shaft has one arrowhead on the right, none at the left. Proof (287,1343,1658,1626), 2×.',hc=True,kind='misread symbol or index')
a('proof middle equivalence',r'a prime)\Longleftrightarrow\unsure{b)|c)}','a prime) leftarrow c)',r'a prime)\Longleftrightarrow b)','The letter has a closed lower bowl and short ascender; the sign has both left and right heads. (994,1336,1073,1374), 4×; proof 2×.','medium',True,True,'misread symbol or index')
a('proof opaque cancelled word',r'\deleted{\illegible{1}}',r'\struck{\ill{}}','C retained','A tall initial stroke and fragments of mid-letter ascenders survive, but thick bars prevent a reliable word even at 6×. (1097,1347,1307,1384).','low')
a('proof target implication',r'prouvons c)\longrightarrow b','prouvons a) implies b','C retained','The small starting letter is an open c followed by a parenthesis; the arrow has a single shaft. Proof, 2×.',hc=True,kind='misread symbol or index')
a('proof overwritten acting group',r'\uline{par \deleted G H_0}','par H_0','C retained','The former G is visible behind the replacement H, and the underline includes par. Proof, 2×.',hc=True,kind='omission')
a('proof orbit maps','les phi_x étant générisants','uncertain les ill. étant générisant','C retained','The phi loop and lower x are visible; the adjective has the final s join. Proof, 2×.',hc=True,kind=r'readable ink left as \ill{}',marked='yes')
a('proof cancelled OK',r'\deleted{\unsure{OK}}',r'\struck{\ill{}}',r'\deleted{OK}','O retains its left loop and K its right descending branch beneath cancellation. (760,1546,830,1601), 5×.','high',True,True,r'readable ink left as \ill{}')
a('second slanted margin deleted lead-in',r'\deleted{\unsure{avec}}','omitted',r'\deleted{avec}','The looped a and v/e/c sequence remain recognizable under three strikes. (21,1515,288,2184), clockwise 36°, 3×.','medium',True,True,'omission')
a('second slanted margin question','Est-il underlined tjrs vrai que u(G) stable par spécialisation?','uncertain Est-il vrai que ill. stable par spécialisation?','C retained','The full question is legible upright, including tjrs and u(G), and ends in a question mark. Second margin, clockwise 36°, 3×.',hc=True,kind=r'readable ink left as \ill{}',marked='yes')
a('second slanted margin response connective',r'Oui. Je prouve \unsure{que|pour} tt ss-ens.','ill.','Oui. Je prouve pour tt ss-ens.','The word after prouve has an initial p descender and low our, matching pour on the following line. Second margin, clockwise 36°, 3×.','medium',True,True,r'readable ink left as \ill{}')
a('second slanted margin final line',r'stable par mult (et sym.) → stable par \unsure{spécia|spéc.}','omitted','stable par mult (et sym.) → stable par spécia','Both stability clauses, parenthesis and arrow can be read. The last abbreviation has a final low a-like loop and no separated period. Second margin, clockwise 36°, 3×.','medium',True,True,'omission')
a('image corollary cancelled earlier wording',r'\unsure{domination} de H^{\unsure{red|t}}\unsure{sur}','dominant ill.','C retained','The thin cancelled baseline contains the long domin... word, de, H with a compact raised annotation, and a final low stroke group. These remain tentative. (838,1655,1305,1700), 4×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('image corollary replacement','inserted Im u est fermée','uncertain Im u est fermée','C retained','The new phrase sits above the crossed baseline; every word, including feminine fermée, is clear. Corprop (265,1623,1659,1923), 2×.',hc=True,kind='insertion or placement',marked='yes')
a('finite-type proposition crossed H','deleted H','ill.','C retained','Two vertical stems and crossbar of H remain inside the cross-hatching. Corprop, 2×.',hc=True,kind=r'readable ink left as \ill{}')
a('finite-type proposition inserted H hypothesis','inserted H l. t. f.','attached to preceding Cor','C retained','The high note at right is led down to the finite-type proposition by a long curved insertion guide. Corprop, 2×.',hc=True,kind='insertion or placement',conseq='H locally of finite type belongs to the monomorphism proposition.')
a('lower separator drawing','two long curved horizontal strokes','omitted','C retained','Both long unequal strokes are present in the lower-half image; neither is text or a deletion of the following table.',hc=True,kind='drawing or diagram')
a('first table ev. abbreviation',r'\unsure{ev.|ev}','ou','ev.','The e-v join is followed by a detached dot. (688,2122,765,2169), 4×.','high',True,True,'misread word')
a('first table second group word',r'\unsure{profétales|profinis}','profinis','profétales','The long word visibly contains an accented é and tall t before ales, rather than inis. (525,2171,714,2243), 4×.','high',True,True,'misread word')
a('first table second-line f.',r'\unsure{f.}','omitted','f.','Separate tall f with a short cross stroke and dot precedes the parenthesis. Same crop, 4×.','high',True,True,'omission')
a('first table third-line abbreviation','ev.','ou','ev.','The repeated e-v-dot form is visible before tordus. Bottom1 (191,2116,1693,2520), 2×.',hc=True,kind='misread word')
a('first table missing closing parenthesis',r'tordus\unsure{)|{}}','tordus)','tordus','The word ends before blank space and the separate vertical divider; no right parenthesis is written. (1246,2243,1415,2292), 4×.','high',True,True,'text not on the page')
a('first table grouping geometry','left brace and right vertical divider','brace, unseparated right label','C retained','The right label is behind a visible long vertical line. Bottom1, 2×.',hc=True,kind='drawing or diagram')
a('topological identification sign',r'\unsure{\underline{\approx}|\cong}',r'\simeq',r'\underline{\approx}','Two distinct wavy lines stand above one short straight underline. Bottom1, 2×.','high',True,True,'misread symbol or index')
a('topological group description','loc. compact; inserted tot. disc.','loc. compacts tot. discont.','C retained','compact has no separate final s; tot. disc. is a small interlinear insertion and stops at disc. Bottom1, 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
a('connected-groups title initial correction',r'\deleted{\unsure{s|S}}Séparables','Séparables','C retained','An earlier S/s-shaped loop is crossed directly before the rewritten capital S; case is not secure. (451,2617,517,2666), 4×.','low',hc=True,kind='omission')
a('connected-groups right final qualification','partie abélienne de dim. majorée','ill.','C retained','The final two lines are visible down to the lower edge; abélienne has tall looped letters and majorée ends with an accent and point. Bottom2 (217,2538,1665,2802), 2×.',hc=True,kind=r'readable ink left as \ill{}',conseq='The bounded-dimension qualification on the abelian part is retained.')
d['unresolved']='Deleted map label λ/v; discarded p. gén., donc and est; cancelled qu cpt, X, générisant ending, Prop, de and final cont./contient; live-corollary deleted affine/ouvert, U/u, cancelled fermé si and et H l. t. f.; one opaque proof word; cancelled domination, H exponent red/t and sur; overwritten initial s/S in Séparables.'
d['inventory']=[
['text','opening paragraph','2/ Réciproquement, si W est'],
['deletion','opening hypothesis','ouvert et fermé'],
['insertion','above opening hypothesis','stable par spécialisation'],
['deletion','opening conclusion','est ouvert et fermé'],
['insertion','above opening conclusion','aussi'],
['drawing','above proposition','two short separator strokes'],
['text','upper proposition','Prop Soit G→H hom de g.pes'],
['deletion','upper proposition arrow label','lambda/v'],
['deletion','after target H','Si'],
['deletion','upper proposition first line','avec G qu. cpt'],
['insertion','above first plat','générisant'],
['deletion','above second plat','au p. gén.'],
['insertion','above second plat','underlined univ générisant'],
['deletion','after second plat','et donc est plat'],
['deletion','upper conclusion','donc u(G) stable par spécialisation/générisat.'],
['deletion','inside upper conclusion','spécialisation'],
['margin note','upper left slanted','Il faut un argument pour univ générisant'],
['deletion','large cancelled block','Cor Supposons qu’il existe'],
['deletion','within large cancelled block first line','que H qu cpt qu’il existe'],
['deletion','within large cancelled block before u est plat','X'],
['insertion','within cancelled block above u est plat','si H est réduit'],
['deletion','within cancelled block','donc générisant (donc générisant ...)'],
['insertion','within cancelled block above on suppose','ne'],
['deletion','within cancelled block lower left','Prop Su'],
['deletion','within cancelled block before l’image','et'],
['deletion','within cancelled block after l’image','de'],
['insertion','within cancelled block final line','en'],
['text','live corollary heading','Conditions équivalentes sur u'],
['deletion','above a)','affine/ouvert'],
['text','live corollary a and a prime','u est générisant; u générisant en un point'],
['insertion','above a) générisant','univ'],
['display','live corollary b','U/u(G) contains overwritten G H_0'],
['deletion','b overwritten acting group','G'],
['text','live corollary c','exists un point maximal de G'],
['insertion','c above maximal','x'],
['text','after c','Sous ces conditions u(G) stable'],
['deletion','after stability statement','donc fermé si G qu. cpt'],
['margin note','right of stability statement','et H l. t. f.'],
['deletion','right oval note','et H l. t. f.'],
['text','proof first line','Dém a implies a prime connu'],
['deletion','proof first line','one illegible word'],
['text','proof continuation','b implies c trivial, prouvons c→b'],
['deletion','proof acting group','G overwritten H_0'],
['deletion','proof end','OK'],
['margin note','lower left slanted','Est-il tjrs vrai que u(G) stable'],
['deletion','lower slanted margin lead-in','avec'],
['text','image corollary','Cor Si G qu. cpt'],
['deletion','image corollary original continuation','domination de H exponent sur'],
['insertion','above image corollary','Im u est fermée'],
['text','finite-type proposition','Si G→H un mono'],
['deletion','finite-type hypothesis','H'],
['insertion','finite-type proposition upper right','H l. t. f.'],
['drawing','above tables','two long curved separator strokes'],
['diagram','bottom first table','1) Groupes discrets; profétales f.; loc. cpts'],
['display','topological interpretation','underlined approximately; groupes topologiques loc. compact'],
['insertion','topological interpretation interline','tot. disc.'],
['display','action formula','pi×G→G continue'],
['diagram','bottom second table','2) Groupes connexes; Séparables; sur corps parfait'],
['deletion','second-table initial capital','s/S'],
]
runpy.run_path(str(root/'scripts/review.py'))['commit'](d)
