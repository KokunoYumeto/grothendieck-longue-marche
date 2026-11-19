from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
d={'cote':53,'scan':8,'sheet_kind':'text','hand':'his hand','replace':[
(r'\unsure{ouv|ouv.}','ouv'),
(r'\unsure{ssi|ses}','ssi'),
(r'\unsure{tout|tt}',r'\unsure{tt|tout}'),
(r'\unsure{t.|T.}','t.'),
(r'\unsure{c|c)}','c'),
(r'\unsure{$\Rightarrow$|$\Longrightarrow$}',r'$\Longrightarrow$'),
(r'\unsure{?|!?}','?'),
(r'\illegible{1}',r'\unsure{est}'),
(r'\unsure{Est.|Ex.}',r'\unsure{Esq.|Est.}'),
(r'pour que $g$ \unsure{soit géom|soit} il \unsure{suffit que|suffit} $g$,',r'pour que $g$ \unsure{$G$ est géom normal en $g$|soit géom il suffit que $g$},'),
], 'review':'Personally read the whole image, both halves, and every line against C and H. Enlarged all text blocks at 2×, the implication chain at 3×, and all doubtful or differing details at 5×. Read the right margin upright after clockwise 7° rotation at 3× and the left slanted note after clockwise 37° rotation at 3×; its opaque cancelled line was then enlarged to an effective 6×. Formula letters, ideal/local-ring notation, arrows, indices, cancellation extents and insertion guides were checked. The heavily overlined abandoned proof sentence remains expressly uncertain. No context was opened.', 'decisions':[], 'inventory':[]}
def a(place,c,h,final,shows,conf='high',cc=False,hc=False,kind='other',marked='no',conseq=None):
 x=dict(place=place,c=c,h=h,final=final,shows=shows,confidence=conf,c_changed=cc,h_changed=hc,kind=kind,marked_in_H=marked)
 if conseq:x['consequential']=conseq
 d['decisions'].append(x)
a('opening abbreviation',r'\unsure{ouv|ouv.}','ouv.','ouv','The low o-u-v form is followed by clear space and est; no terminal dot. (538,185,601,214), 5×.','high',True,True,'abbreviation expanded or spelling modernised')
a('opening condition',r'\unsure{ssi|ses}','ssi','ssi','Two s forms and a final compact i stroke are visible. (882,181,953,216), 5×.','medium',True)
a('opening universal abbreviation',r'\unsure{tout|tt}',r'deleted ill. followed by tt',r'\unsure{tt|tout}','The compact crossed strokes occupy a single group after pour. They favor tt, but are too entangled to settle whether more letters were attempted; no separate preceding cancelled group can be distinguished. (1123,172,1207,219), 5×.','low',True,True,'deletion state (struck given live or live given struck)')
a('first corollary inserted qualification',r'\unsure{au cas une|au cas d’une} ext. de \unsure{t.|T.} f.','uncertain au-dessus d’une ext. de t.f.','au cas une / au cas d’une remains doubtful; t. resolved','The beginning has au cas-like short strokes, without the long dessus form. Its compressed middle stays uncertain. The t is a narrow upright followed by a dot, rather than a capital crossbar. (1380,221,1698,265), 5×.','low',True,True,'misread word','yes')
a('first corollary transcendence word',r'\unsure{transcend.te|transcendante|transcend. ou}','transcend.','C retained','The abbreviation-like first part ends with a dot and is followed by two low connected strokes before pure; those strokes are not simply blank space. (603,323,869,372), 5×.','low',hc=True,kind='misread word')
a('first corollary pure','pure','uncertain pure','pure retained','The descending p and joined u-r-e are distinct. Top (149,165,1713,377), 2×.',hc=True,kind='other',marked='yes')
a('normality NB opening',r'un \unsure{réslt|rés\textsuperscript{t}}','une série','C retained','The article ends in n, and the following compact word has a final tall crossed t. Its interior l/s strokes remain compressed; série does not fit the ending. (605,637,708,683), 5×.','low',hc=True,kind='misread word')
a('normality NB rewritten hypothesis',r'deleted \unsure{géom normal|géom norm}; inserted loc de','deleted géom ill.; loc. de inline','C retained','The old géom... word lies under the horizontal strike; loc de is placed above it as the replacement. Normal (167,623,1714,891), 2×; (895,710,1152,752), 5×.','low',hc=True,kind='insertion or placement')
a('normality NB final delimiter','opening square bracket, closing parenthesis','matching square brackets','C retained','The opening bracket is angular; the terminal mark is one curved parenthesis. Normal, 2×.',hc=True,kind='misread symbol or index')
a('separator drawing','long slightly curved line','omitted','C drawing retained','The continuous separator runs across the sheet beneath the NB and above Proposition; its slight rises and dips are visible in whole and half views.',hc=True,kind='drawing or diagram')
a('proposition a abandoned qualifier',r'\deleted{\unsure{géom norm|géom. normal}}',r'\struck{\ill{}}','C retained','The g descender and remaining low strokes survive under a heavy baseline strike; the exact final abbreviation is not secure. (342,1025,515,1064), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('proposition a prime base and deletion',r'G sép./k deleted en un point',r'G sép. deleted ill.','C retained','The slash and k are uncancelled; the following en un point is separately struck but readable. Prop (191,930,1310,1223), 2×.',hc=True,kind=r'readable ink left as \ill{}')
a('right margin overwritten noun',r'\deleted{\unsure{gpe|esp.}} inserted schéma',r'\struck{\ill{}} schéma','C retained','The old group has a long p/g-like descender under the cancellation; schéma is written above it. (1550,985,1663,1029), 5×; right margin (1198,925,1721,1274), clockwise 7°, 3×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('right margin discarded map',r'deleted G×X arrow label \unsure{π|p} to X','deleted G×X only','C retained','The cancelled expression includes an arrow and target X. Its small upper label has a thick top and short descender but is insufficiently open to settle π/p. (1520,1048,1708,1104), 5×; (1629,1024,1664,1081), 5×.',hc=True,kind='omission',conf='low')
a('right margin discarded map placement','after et tel que','before et tel que','C retained','The crossed old map is to the right of et tel que, above the rewritten map, not before that connective. Right margin rotated, 3×.',hc=True,kind='insertion or placement')
a('right margin homogeneity word','essentiellement homogène','uncertain universellement homogène','C retained','The word starts with e-s-s and has the long ...tiellement sequence; no initial uni- appears. Right margin rotated, 3×.',hc=True,kind='misread word',marked='yes')
a('implication chain inserted source',r'\inserted{\unsure{c|c)} implies}','c) implies inline','inserted c implies','A tiny open c sits above the line beside a sloping double arrow into b); it has no right parenthesis. (531,1240,566,1282), 5×; chain (232,1235,1080,1325), 3×.','high',True,True,'insertion or placement')
a('implication chain a prime to a',r'unsure Rightarrow/Longrightarrow a)','deleted arrow a)','Longrightarrow a), live','The two horizontal shafts end in a right head and the following a) is not crossed. The cancellation begins after a). Chain 3×; (767,1258,1046,1304), 5×.','high',True,True,'deletion state (struck given live or live given struck)',conseq='The written a′⇒a implication remains live.')
a('implication chain cancelled final arrow',r'deleted unsure Rightarrow/Longrightarrow unsure b)/b)?',r'deleted ill.','deleted Longrightarrow unsure b)/b)?','A double right arrow survives under multiple diagonal strokes. The final b has a lower bowl, but the following punctuation remains overworked. Same arrow crop, 5×.','low',True,True,r'readable ink left as \ill{}')
a('left marginal question earlier re',r'\deleted{\unsure{re|ré}}','omitted','C retained','A small independently crossed re-like group precedes the rewritten réduit. Left margin (24,1353,497,1736), clockwise 37°, 3×.','low',hc=True,kind='omission')
a('left marginal question réduit',r'\unsure{réduit|reduit}','uncertain réduit','C retained','The word is readable, but the tiny mark above its first vowel may belong to adjoining ink; the accent stays uncertain. Same rotated crop, 3×.','low')
a('left marginal question punctuation',r'\unsure{?|!?}','?','?','One curved question hook and its lower dot stand after the abbreviation sép.; there is no separate exclamation stem. Same rotated crop, 3×.','high',True)
a('left marginal cancelled parenthesis opening',r'\unsure{est-ce que|et si pas|est-ce} le','uncertain supposé ill.','C retained','The struck beginning has several surviving short joins and a long descender, but cannot be divided reliably; le follows. The cancellation crosses the whole unfinished parenthesis. Rotated left crop at effective 6×.','low',hc=True,kind='deletion state (struck given live or live given struck)',marked='yes')
a('left marginal cancelled base and final phrase',r'\unsure{k|h} illegible one word \unsure{stable dans|étant donné}','ill.',r'\unsure{k|h} \unsure{est} \unsure{stable dans|étant donné}','After the tall k/h-like letter, a low loop, s-like bend and upright stroke favor est, though the bar still prevents certainty. The final phrase remains crossed and uncertain. Rotated left crop at effective 6×.','low',True,True,r'readable ink left as \ill{}')
a('proof initial live maximal point','deleted un, live pt maximal de G','un pt maximal de G included in large deletion','C retained','Only un has its own overstrike on the higher line; pt maximal de G sits clearly above the old cancelled sentence. Proof (270,1304,1698,1822), 2×; (754,1300,1649,1372), 5×.',hc=True,kind='deletion state (struck given live or live given struck)',conseq='The maximal-point hypothesis remains live; H cancels it with the discarded wording below.')
a('proof small cancelled géom',r'\deleted{\unsure{géom|gén.}}','omitted','C retained','A separate dense crossed word above the long old line starts with a looped g; its ending remains covered. (1220,1317,1334,1347), 5×.','low',hc=True,kind='omission')
a('proof abandoned long first sentence',r'pour que g unsure soit géom/soit il unsure suffit que/suffit g','tel que G est séparable ill.',r'pour que g unsure G est géom normal en g / soit géom il suffit que g','The long strike crosses two draft layers. Toward the right, n-o-r-m-a-l and en g are more consistent with the surviving low strokes than suffit que; the central G/soit group is still overlaid. Both full alternatives remain explicit. (754,1300,1649,1372), 5×, with (936,1335,1246,1368) and (1323,1336,1612,1369), 5×.','low',True,True,'misread word')
a('proof first resulting assertion','Alors k(g) ... donc G est géom normal en g, live','Donc k(g) ... through en g struck','C retained','Alors is written on the higher line at right; its continuation and the next line are uncrossed. The long cancellation below belongs to the discarded attempt, not this assertion. Proof 2×; oldline detail 5×.',hc=True,kind='deletion state (struck given live or live given struck)',conseq='The separability of k(g) and normality at g are retained as live assertions.')
a('proof discarded extension phrase',r'Donc, quitte \unsure{à faire une extension|à une extension}','Donc, quitte à faire une extension de la base','C retained','The crossed interline visibly includes faire and extension-like tall strokes; its beginning is crowded and stays doubtful. No de la base follows before the next par descente. (568,1402,915,1435), 5×; proof 2×.','low',hc=True,kind='misread word')
a('proof discarded descent step',r'par descente on est ramené à \unsure{voir le cas|voir l’assert}','on est ramené à le voir','C retained','Par descente is legible beneath the smaller cancelled extension interline. The later words under the long strike remain too merged to distinguish the C alternatives. (1106,1401,1313,1456), 5×; proof 2×.','low',hc=True,kind='omission')
a('proof unchanged-property sign','de = pour tt','de même pour tt','C retained','Two short parallel horizontal strokes stand on the next line after de, with no letters spelling même. Proof, 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
a('proof rational-point reduction','au cas où g, g prime rat/k','au cas g, g prime rat/k','C retained','The small où follows cas before the two point labels. Proof, 2×.',hc=True,kind='omission')
a('reverse implication proof abbreviation',r'\unsure{Est.|Ex.} en démonstration','Esq. de démonstration',r'\unsure{Esq.|Est.} en démonstration','The final compact letter has a short descending right stroke, favoring q over t; it is not the two-stroke x. The following word has low e-n strokes without a d ascender. (566,1844,644,1891) and (563,1839,1083,1896), 5×.','low',True,True,'misread word')
a('final corollary reduced subscript',r'\unsure{red|réd}','réd','C retained','The tiny subscript is written densely, with the possible accent merging into the following heavy d. (994,1961,1065,2001), 5×.','low')
a('final corollary final barred character',r'\unsure{bar k|k|bar B}','omitted','C retained','A separate dark letter with a distinct top bar follows normal. Its interior strokes do not securely distinguish k from a B-like form. (1522,1939,1574,2001), 5×.','low',hc=True,kind='omission')
d['unresolved']='Opening tt/tout; inserted au cas une/au cas d’une; transcend.te/transcendante/transcend. ou; réslt/rés raised t; both cancelled geometric-normality qualifiers; right margin old gpe/esp. and map label π/p; cancelled final b punctuation; left margin re/ré, réduit accent, and cancelled parenthesis including tentative est; small cancelled géom/gén.; heavily struck first proof sentence, extension and descent fragments; Esq./Est.; final red/réd and barred character.'
d['inventory']=[
['text','first corollary','Cet ouv est dense ssi'],
['insertion','above separable-extension equivalence','au cas une/au cas d’une ext. de t. f.'],
['text','second corollary','Si k est parfait'],
['text','normality NB','On a un réslt analogue'],
['deletion','normality NB hypothesis','géom normal/géom norm'],
['insertion','normality NB hypothesis','loc de'],
['insertion','normality NB conclusion','et dense si k est parfait'],
['drawing','between NB and proposition','long curved separator'],
['text','proposition heading','G groupe sur corps k'],
['text','proposition conditions','a, a prime, b, c'],
['deletion','condition a','géom norm/géom. normal'],
['deletion','condition a prime','en un point'],
['margin note','upper right slanted','marche aussi si X un schéma'],
['deletion','right margin overwritten noun','gpe/esp.'],
['insertion','right margin replacement','schéma'],
['deletion','right margin old map','G×X arrow π/p to X'],
['display','right margin new map','G×X→X×X; (g,x) maps to (gx,x)'],
['text','right margin parenthesis','X essentiellement homogène'],
['display','implication chain','c implies b implies a prime implies a'],
['insertion','above implication chain','c implies'],
['deletion','end of implication chain','implies b)/b)?'],
['margin note','lower left slanted','NB Si G de t. f. sur k'],
['deletion','left margin first attempt','re/ré'],
['deletion','left margin final parenthesis','est-ce que/et si pas/est-ce le k/h est ...'],
['text','proof a implies b','Soit g in G, pt maximal'],
['deletion','above proof first draft','un'],
['deletion','above proof first line','géom/gén.'],
['deletion','proof abandoned first sentence','pour que g ... géom normal en g'],
['text','proof live continuation','Alors k(g) est une ext. séparable'],
['deletion','proof abandoned reduction','Donc, quitte ... par descente'],
['deletion','proof cancelled block','Soit g prime un pt maximal ... faisant une extension'],
['text','proof restarted conclusion','Donc G a un pt g'],
['text','proof rational-point argument','Prouvons qu’il en est de ='],
['text','reverse implication','b implies a; Esq./Est. en démonstration'],
['text','final corollary','Corollaire 1 Soit k parfait'],
]
runpy.run_path(str(root/'scripts/review.py'))['commit'](d)
