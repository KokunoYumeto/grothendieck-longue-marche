from pathlib import Path
import json
from datetime import datetime, timezone
R=Path('/workspace/scratch/8db4dde48936/sp53_recovery')
O=R/'out/readers/scan015/R1'
A=str(R/'source/SP53_CW_156-6_scans/J156-6-02_156-6_scan015_a.jpg')
B=str(R/'source/SP53_CW_156-6_scans/J156-6-02_156-6_scan015_b.jpg')
W=str(R/'source/SP53_CW_156-6_scans/J156-6-02_156-6_scan015.jpg')
plan=json.loads((O/'crop_plan.json').read_text())
CROPS={int(x['name'][:2]):x for x in plan}
def locus(n=None,box=None,source=None):
 if n is not None:
  p=CROPS[n]
  return {'crop':'readers/scan015/R1/crops/'+p['name']+'.jpg','crop_box':p['box'],'crop_source':p['source']}
 return {'crop':None,'crop_box':box,'crop_source':source}
differences=[]
def diff(place,c,h,reading,against_C,against_H,kind,evidence,confidence='high',marked_in_H='no',mathematical=False,n=None,box=None,source=None):
 differences.append({'id':f'R1-015-D{len(differences)+1:02d}','place':place,'c':c,'h':h,'reading':reading,'against_C':against_C,'against_H':against_H,'kind':kind,'marked_in_H':marked_in_H,'confidence':confidence,'evidence':evidence,**locus(n,box,source),'mathematical':mathematical})
F=r'\mathcal{F}'
M=r'\mathcal{M}'
P=r'\mathcal{P}'
kind='misread symbol or index'
diff('Opening: family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,kind,'The cap has a long left entry and rising curled right tip; it is detached from the single stem, which has a crossed middle arm and a returning lower foot. The family-letter identity is clear. Exact calligraphic/fraktur typography remains underdetermined; the supplied notation candidates are retained.',confidence='medium',mathematical=True,n=1)
diff('Opening: c\'est de la donnée','c\'est de la donnée','c\'est la donnée','c\'est de la donnée',False,True,'omission','The first line ends with a separate de after c\'est; the next begins la donnée. H omits this de.',box=[1260,80,1525,155],source=A)
diff('(1.30): enclosing lines',r'\boxed{...}',r'\boxed{...}; note: la formule est encadrée','Three-sided enclosure open at the right paper edge, with a gap at upper left and a smaller lower-left gap.',True,True,'drawing or diagram','The top line starts near (550,258) and reaches (1662,241); the left upright starts only near (549,281); the bottom begins near (560,406) and reaches the right edge. No right vertical occurs. H correctly notices an enclosure, but both boxed renderings close a side that the scan does not show.',box=[535,230,1671,420],source=A)
diff('(1.30): brace and gloss placement',r'\underset{\overbrace{\scriptstyle\text{rel. d\'ordre dans }\mathcal{F}}}{\leq,\quad\ll}',r'Inline parenthesis in the formula; note places gloss below the two signs with a brace','Gloss below the row, with a brace above it shifted to the right of the first order sign.',True,True,'drawing or diagram','The brace runs from about x681 to x1030 and its upward cusp lies near x885, between the second order sign and telles. The gloss begins around x695. Thus the physical brace/gloss is shifted right, rather than centered strictly under the two signs. H\'s note is credited for the below-row gloss and brace.',box=[666,293,1041,399],source=A)
diff('(1.30): family F in rel. d\'ordre dans',F,r'\mathfrak{F}',F,False,True,kind,'The small final capital has the familiar cap, crossed stem and foot. It is the family F, distinct from the ordinary F operands on the same row. The first-occurrence alphabet doubt governs this later occurrence.',confidence='medium',mathematical=True,box=[959,341,1010,398],source=A)
diff('En termes de celles-ci: definit',r'\unsure{definit|définit}','définit','definit',True,True,'misread word','No separate acute occurs above the e between the d and the tall f. The large ascending stroke belongs continuously to f. A dot over the later i is present and distinct.',n=2)
diff('Canceled symbol following definit',r'\deleted{$\unsure{M|\mathcal{F}}$}',r'\struck{$\mathcal{M}$}',r'\deleted{$\unsure{\mathcal{M}|M}$}',True,True,kind,'Beneath the crossing strokes are two upright peaks joined by a rounded trough, with the long rising left entry characteristic of the page\'s M. This resolves M against F. The recurrent calligraphic/ordinary M alphabet question remains at this first occurrence; the cancellation itself is certain.',confidence='medium',mathematical=True,n=3)
diff('First inclusion: M on the left','M',M,M,True,False,kind,'Two tall peaks, a broad rising entry and a rounded middle trough form the same cursive capital as the canceled letter. Calligraphic M is used under the first-occurrence alphabet doubt.',confidence='medium',mathematical=True,n=4)
diff('First inclusion: family F on the right',F,r'\mathfrak{F}',F,False,True,kind,'A broad left-overhanging cap, single stem and middle crossbar distinguish this from the ordinary member F. The recurring alphabet doubt is not restated.',confidence='medium',mathematical=True,box=[883,635,955,711],source=A)
diff('After (1.20): avec','avec',r'\uncertain{avec}','avec',False,True,'other','The low a/v strokes and final c-shaped return read avec in the half; no alternative word is suggested by the visible sequence. H\'s explicit uncertainty is removed.',marked_in_H='yes',box=[639,744,766,800],source=A)
diff('First induced-order pair: M under ≤',r'\underset{M}{\leq}',r'\leq_{\mathcal{M}}',r'\underset{\mathcal{M}}{\leq}',True,True,kind,'The small two-peaked cursive M is centered below the order sign, not displaced to its lower right. C\'s alphabet and H\'s label placement differ.',confidence='medium',mathematical=True,box=[1224,738,1297,822],source=A)
diff('First induced-order pair: M under ≪',r'\underset{M}{\ll}',r'\ll_{\mathcal{M}}',r'\underset{\mathcal{M}}{\ll}',True,True,kind,'The small cursive M is centered directly below the two chevrons. Its entry, two peaks and lower return recur locally; H places the label as a lower-right subscript.',confidence='medium',mathematical=True,box=[1310,738,1396,824],source=A)
diff('Second induced-order pair: family F under ≤',r'\underset{\mathcal{F}}{\leq}',r'\leq_{\mathfrak{F}}',r'\underset{\mathcal{F}}{\leq}',False,True,kind,'The attached cap and returning foot identify the family F. The label is centered under ≤, so H differs in both alphabet and placement. This was settled in half_a; its tight coordinates are supplied without another targeted crop.',confidence='medium',mathematical=True,box=[423,853,484,951],source=A)
diff('Second induced-order pair: fourth index under ≪',r'\underset{\unsure{\mathcal{F}|\overline{f}}}{\ll}',r'\ll_{\mathfrak{F}}',r'\underset{\unsure{\mathcal{F}|\overline f}}{\ll}',False,True,kind,'A horizontal cap floats well above a short crossed lower stem with a hooked foot. The adjacent F supplies a close comparison, but the cap\'s detachment leaves family F versus barred f genuinely open. Its position is centered below ≪.',confidence='medium',mathematical=True,n=5)
diff('Second inclusion: M after L ⊂','M',M,M,True,False,kind,'The tall capital has a long rising entry, two steep peaks and a rounded lower return; it is the recurring cursive M.',confidence='medium',mathematical=True,box=[912,936,1007,1021],source=A)
diff('Reference before L\'application',r'(1.2\unsure{6|5})','(1.25), with a note suggesting the definition is elsewhere','(1.25)',True,False,'misread symbol or index','The last digit has an extended upper stroke, a descending left portion and a short lower turn. There is no closed lower loop of 6. Literal 5 is retained; no other page was consulted and the cross-reference is not mathematically repaired.',mathematical=True,n=6)
diff('(*) source family F',F,r'\mathfrak{F}',F,False,True,kind,'The domain has a high returning cap, crossed single stem and lower hook, unlike the ordinary live F before the maps-to arrow.',confidence='medium',mathematical=True,box=[559,1147,634,1232],source=A)
diff('(*) destination power-set P',r'\unsure{\mathcal{P}|\mathrm{P}}',r'\mathfrak{P}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}',True,True,kind,'The P has an angular broad bowl, an overhanging upper entry and a lower-left returning loop crossing its long stem. These ornamental strokes disfavor plain roman P, while the exact script/calligraphic/fraktur family remains underdetermined.',confidence='medium',mathematical=True,n=8)
diff('(*) destination: M inside P(M)','M',M,M,True,False,kind,'Two steep peaks and the long curved entry identify the same cursive M in this parenthesis. The alphabet decision was made in half_a; the P crop later includes it only as adjacent context.',confidence='medium',mathematical=True,box=[871,1142,949,1217],source=A)
diff('(*) overwritten source X/F',r'\deleted{\unsure{X}}F',r'F; explicit note: un X biffé précède F',r'\mathord{\rlap{$\deleted{X}$}F}',True,False,'misread symbol or index','Two oblique arms cross as an X below the live F\'s top and middle arms; the F stem is separately visible. X is resolved. H\'s explicit note is credited, so its formula-only omission is not counted as disagreement.',mathematical=True,n=9)
diff('(*) operator after tilde F =',r'\unsure{\mathrm{Dep}|\mathrm{Def}}',r'\mathrm{Dépl}',r'\mathrm{Dep}',True,True,'misread word','The last letter descends in a narrow loop and returns to a small right arm: p, not f. After it comes the opening parenthesis immediately; no final l appears. There is no isolated acute above e.',mathematical=True,n=10)
diff('Insertion between est and definie',r'\inserted{alors}',r'\add{donc}',r'\inserted{alors}',False,True,'misread word','Above the insertion curve, a low a is followed by a looped l, compact o, r shoulder and final s. The word is alors; the placement between est and definie is recognized by both witnesses.',n=11)
diff('Verb after inserted alors',r'\unsure{définie|definie}','définie','definie',True,True,'misread word','The large stroke over de is the insertion curve connected to the insertion location; no separate acute over e can be isolated. The tall following stroke belongs to f. The literal verb is transcribed without an acute.',n=11)
diff('(1.31): M in X ∈ M','M',M,M,True,False,kind,'The membership operand is the compact two-peaked cursive M, with its rounded inner trough. C uses ordinary M.',confidence='medium',mathematical=True,box=[858,253,927,327],source=B)
diff('(**) source family F',F,r'\mathfrak{F}',F,False,True,kind,'The broad rising cap, thin crossed stem and hooked foot again identify the family letter; the arrow to its right has a separate hook.',confidence='medium',mathematical=True,box=[576,434,646,528],source=B)
diff('(**) destination: M in Fig(M)','M',M,M,True,False,kind,'The compact M in the destination has two upright peaks and a long initial rise. It belongs to the recurring cursive M series.',confidence='medium',mathematical=True,box=[861,444,928,521],source=B)
diff('(**) source before maps-to: possible overwritten X',r'\deleted{\unsure{X}}F','F',r'\unsure{\mathord{\rlap{$\deleted{X}$}F}|F}',True,True,'deletion state','A long rising oblique runs from well below-left into the top of F; the F has a live top arm, middle arm and hooked lower stem. Unlike the first map, a second independent X diagonal cannot be separated. Both an overwritten X and an unexplained extra stroke on live F remain possible; uncertainty concerns deletion history, not merely the letter X.',confidence='low',mathematical=True,n=13)
diff('(**) image: M subscript of Fig_M(F)','M',M,M,True,False,kind,'The genuine lower-right subscript is a short two-peaked M. Here lower-right placement is correct in both witnesses; the disagreement is C\'s ordinary alphabet.',confidence='medium',mathematical=True,box=[1293,467,1354,518],source=B)
diff('Punctuation after par (1.4)','par (1.4) :','par (1.4)','par (1.4) :',False,True,'omission','Two separate points occur to the right of the reference, the upper near (535,578), the lower near (543,585). This is a colon, not a single speck or an equation mark.',box=[517,563,558,600],source=B)
diff('Struck-label display: M subscript of initial Fig_M(F)','M',M,M,True,False,kind,'The small M beneath and to the right of Fig has the same two peaks and returning end. The original subscript is retained as cursive M.',confidence='medium',mathematical=True,box=[679,652,738,708],source=B)
diff('Struck-label display: second power-set P',P,r'\mathfrak{P}',P,False,True,kind,'The second P has an angular bowl and crossed long stem with a small left overhang. It repeats the ornamental alphabet seen in (*); the first occurrence carries the alphabet alternatives.',confidence='medium',mathematical=True,box=[1314,575,1398,658],source=B)
diff('Struck-label display: M inside final P(M)','M',M,M,True,False,kind,'The final parenthetical M is the narrow two-peaked cursive capital. No ordinary straight-sided M form is substituted.',confidence='medium',mathematical=True,box=[1424,577,1502,640],source=B)
diff('Definition of tilde X: M in Y ∈ M','M',M,M,True,False,kind,'The membership operand again has a rounded trough between two tall peaks and a sloping left entry. This is another individual C alphabet difference.',confidence='medium',mathematical=True,box=[973,713,1040,788],source=B)
diff('Ainsi paragraph: family F',F,r'\mathfrak{F}',F,False,True,kind,'The capital after Ainsi has a long slanted cap, one stem, short middle arm and turning lower end; it is the family F, not the ordinary F appearing in the final formula.',confidence='medium',mathematical=True,box=[538,879,614,975],source=B)
diff('Ainsi paragraph: M after dans','M',M,M,True,False,kind,'The M in dans M has two steep peaks, the long rising first stroke and returning terminal seen in the displayed M occurrences.',confidence='medium',mathematical=True,box=[966,969,1048,1035],source=B)
diff('Final paragraph: s\'interprète',r'\unsure{s\'interprète|s\'interprête}','s\'interprète','s\'interprète',True,False,'misread word','At the final e/t group the faint short accent is a single oblique, not a joined two-legged circumflex. The higher cut-off descender belongs to parties on the preceding line; the initial high marks belong to the apostrophe/i group. The grave reading is preferred at medium confidence.',confidence='medium',n=14)
# Every original C unsure locus, with duplicate context-table entries merged.
c_doubts=[]
def doubt(place,c,reading,disposition,evidence,n):
 c_doubts.append({'place':place,'c':c,'reading':reading,'disposition':disposition,'evidence':evidence,**locus(n)})
doubt('Opening family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Letter F and ornamental cap/foot are clear; exact typographic alphabet is not. The supplied notation-table alternatives replace the earlier script-only alternative.',1)
doubt('Verb definit',r'\unsure{definit|définit}','definit','resolved','No isolated acute above e; the tall neighboring stroke is continuously the f.',2)
doubt('Canceled symbol after definit',r'\deleted{$\unsure{M|\mathcal{F}}$}',r'\deleted{$\unsure{\mathcal{M}|M}$}','resolved','Two peaks and a rounded trough settle M against F. A separate recurring mathcal/ordinary M typography doubt is retained at this first occurrence; cancellation is clear.',3)
doubt('Fourth order index, below ≪',r'\unsure{\mathcal{F}|\overline f}',r'\unsure{\mathcal{F}|\overline f}','retained','The cap is visibly detached above a short crossed hooked stem. Family F is plausible, but a barred f cannot be excluded from this ink.',5)
doubt('Reference before L\'application',r'(1.2\unsure{6|5})','(1.25)','resolved','Long upper stroke and short open lower turn, without a closed lower bowl, support 5. No cross-page correction is applied.',6)
doubt('First power-set P',r'\unsure{\mathcal{P}|\mathrm{P}}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}','retained','The large angular bowl and lower-left returning loop reject a plain roman form, but ornamental typographic alternatives remain unresolved.',8)
doubt('Canceled X at first map',r'\deleted{\unsure{X}}F',r'\mathord{\rlap{$\deleted{X}$}F}','resolved','Two independent crossing obliques are visible under the live F arms and stem, so X is identifiable.',9)
doubt('Operator in first map',r'\unsure{\mathrm{Dep}|\mathrm{Def}}',r'\mathrm{Dep}','resolved','The final narrow descending loop and small shoulder are p. No separate acute or following l is inked.',10)
doubt('Defining verb after inserted alors',r'\unsure{définie|definie}','definie','resolved','The conspicuous upper curve is the insertion mark; no independent acute can be isolated above e.',11)
doubt('Possible canceled X at second map',r'\deleted{\unsure{X}}F',r'\unsure{\mathord{\rlap{$\deleted{X}$}F}|F}','retained','Only one long extra oblique is separable; the second putative X arm merges with live F. The uncertainty is expanded to show whether there is a canceled X at all.',13)
doubt('Final s\'interprète',r'\unsure{s\'interprète|s\'interprête}','s\'interprète','resolved','The small accent is a single oblique with no clear second circumflex leg; vertical context separates it from the preceding line\'s descender. Confidence is medium.',14)
# Top-to-bottom material inventory.
inventory=[]
def inv(element,kind,position,first):
 inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('Author page number','text','Top centre, whole image around (810,32)','14; represented by \\mspage{14}')
inv('Opening paragraph','text','half_a, y70–231','En résumé, en termes de ... c\'est de la donnée de deux relations d\'ordre; separate single underlines under relations and d\'ordre')
inv('Order-data display and label','display','half_a, x240–1665, y240–409','(1.30), ≤, ≪, telles que F ≤ G ⇒ F ≪ G; three-sided enclosure')
inv('Order gloss and brace','text','half_a, x680–1030, y303–393','rel. d\'ordre dans F, below the row, with an overlying offset brace')
inv('Sentence ending after order display','text','half_a, y451–544','que je vais partir.')
inv('Definition introduction','text','half_a, y529–624','En termes de celles-ci, on definit')
inv('Canceled M after definit','deletion','half_a, x1530–1630, y540–593','Canceled two-peaked M; exact mathcal/ordinary alphabet alternatives marked')
inv('First inclusion','display','half_a, y640–707','M ⊂ F')
inv('Definition by (1.20) and induced relations','text','half_a, y731–822','par (1.20), avec les relations ≤ and ≪ with centered M labels, induites')
inv('Second pair of induced relations','text','half_a, y849–955','par ≤ and ≪ with centered family labels, puis; fourth label retains F/barred-f alternatives')
inv('Second inclusion','display','half_a, y943–1019','L ⊂ M')
inv('Reference and application introduction','text','half_a, y1052–1127','par (1.25). L\'application')
inv('First application and label','display','half_a, y1137–1241; half_b, y37–141','(*), family F hooked arrow P(M); live F maps to tilde F = Dep(F)')
inv('Overwritten X at first maps-to source','deletion','half_b, x1100–1148, y59–110','Canceled X underneath live F')
inv('Insertion alors','insertion','half_b, x344–443, y139–181','alors, above a curved insertion indicator, to follow est')
inv('Definition introduction below first application','text','half_b, y174–242','est [inserted alors] definie par')
inv('Principal-subset definition','display','half_b, y246–352','(1.31), tilde F = {X ∈ M | X ≤ F}')
inv('Connecting et','text','half_b, x260–319, y392–441','et')
inv('Second application and label','display','half_b, y440–549','(**), family F hooked arrow Fig(M); source F maps to Fig_M(F)')
inv('Possible overwritten X at second maps-to source','deletion','half_b, x1060–1120, y444–500','Extra rising oblique beneath/through live F; canceled-X versus live-F state alternatives retained')
inv('Reference introducing figure definition','text','half_b, y563–632','par (1.4) :; both colon points included')
inv('Canceled old equation label','deletion','half_b, x282–432, y649–699','(1.32), struck through at the left of the following figure-set equation')
inv('Figure-set equation','display','half_b, y578–711','Fig_M(F) = {tilde X | X ∈ tilde F} ⊂ P(M)')
inv('Connecting avec','text','half_b, x278–390, y752–788','avec')
inv('Principal-subset definition for X','display','half_b, y711–808','tilde X = {Y ∈ M | Y ≤ X}, with a final point')
inv('Interpretation paragraph','text','half_b, y884–1141','Ainsi, family F est interprété comme un ens. de parties dans M via (*), et ≤ s\'interprète simplement par l\'inclusion')
inv('Concluding equivalence','display','half_b, y1134–1221','(1.32), F ≤ G ⇔ tilde F ⊂ tilde G; no final point visible')
view_log=[{'image':W,'role':'whole','viewed_utc':'2026-11-20 12:47:52 UTC'},{'image':A,'role':'half_a','viewed_utc':'2026-11-20 12:47:59 UTC'},{'image':B,'role':'half_b','viewed_utc':'2026-11-20 12:49:03 UTC'}]
times=['12:51:30','12:51:31','12:51:31','12:51:55','12:51:55','12:51:56','12:52:17','12:52:17','12:52:17','12:53:02','12:53:03','12:53:03','12:53:21','12:53:22']
for p,t in zip(plan,times):
 view_log.append({'image':str(O/'crops'/(p['name']+'.jpg')),'role':'crop','viewed_utc':'2026-11-20 '+t+' UTC'})
notes={
 'content':'The page summarizes a proposed starting point: two order relations on the family F, with F ≤ G implying F ≪ G. It recalls M and L from earlier numbered definitions, then writes two injections, one assigning a subset tilde F of M and one assigning the corresponding collection of principal subsets Fig_M(F). It ends by stating that ≤ is represented by inclusion of the assigned subsets. The prose, punctuation, nine displays, offset gloss, enclosure, one insertion, and all certain/possible deletions are included.',
 'math_reading_decisions':[
  'Literal reference (1.25) is transcribed. H\'s note proposing that L is actually defined in (1.26) is an editorial claim, not manuscript ink; no other page was read.',
  'The ordinary operand F is kept distinct from the ornamental domain/family F in every occurrence. Eight family-F occurrences, thirteen M occurrences including the canceled one, and two P occurrences are individually collated.',
  'The fourth order label remains family F versus barred f. All four order labels are centered below their signs; genuine Fig_M subscripts remain lower right.',
  'The operator is literally Dep, without an acute or final l; no expansion to Dépl is made.',
  'The three set separators are single vertical strokes, and the subset signs lack an equality underbar. Tildes are waves over F, X and G, not bars.',
  'The first canceled X is visually identifiable. The second source has one clear extra oblique but no independently separable complete X, so live/canceled-state alternatives are explicit.',
  'The two map expressions are ordinary displayed formulas, not multi-node diagrams. The enclosure/brace is preserved with inline TikZ inside its mathematical display; there is no independent geometrical illustration on this page.',
  'The crossed old (1.32) remains crossed beside the figure-set formula; the later live (1.32) is preserved without renumbering.',
  'The irregular star labels were inspected closely. Their current readings are (*) and (**); no independent former character is securely separable, so no canceled numeral or symbol is invented.'
 ],
 'author_doubts':[],
 'titles_dates_counts':{'manuscript_page':'14','scan':15,'title':None,'date':None,'archive_pencil_number':None,'math_displays':9,'certain_deletions':3,'possible_deletions':1,'insertions':1,'single_underlined_words_or_phrases':2,'independent_margin_notes':0,'actual_crops':14,'whole_views':1,'half_a_views':1,'half_b_views':1,'note':'No explicit authorial doubt, verification request, or question occurs on this page.'}
}
check_events=[
 {'statement_id':'scan015.(1.30)','type':'carried as background without fault found','outcome':'Read as the author\'s assertion about two order relations; no mathematical verification performed.'},
 {'statement_id':'scan015.M-and-L-references','type':'carried as background without fault found','outcome':'Read the literal references (1.20) and (1.25); no referenced page was consulted and no mathematical verification performed.'},
 {'statement_id':'scan015.(*)-and-(1.31)','type':'carried as background without fault found','outcome':'Read the asserted injection and its stated subset definition; no proof of injectivity or other mathematical verification performed.'},
 {'statement_id':'scan015.(**)-and-Fig-definition','type':'carried as background without fault found','outcome':'Read the asserted injection and the displayed Fig_M(F) formula, including the definition of tilde X; no mathematical verification performed.'},
 {'statement_id':'scan015.(1.32)','type':'carried as background without fault found','outcome':'Read as the author\'s assertion of order equivalence with inclusion; no targeted proof check, independent re-proof, computation, or formal certificate was performed.'}
]
notation_proposals=[
 {'sign':'Family/domain F','latex':r'\unsure{\mathcal{F}|\mathfrak{F}} at first occurrence; \mathcal{F} subsequently','ink':'Long overhanging, often detached cap, crossed stem and returning foot; eight written occurrences on this page. Ordinary F operands have simpler arms.','alternatives':[r'\mathfrak{F}']},
 {'sign':'Collection M','latex':r'\unsure{\mathcal{M}|M} at first (canceled) occurrence; \mathcal{M} subsequently','ink':'Long rising entry, two peaks and a rounded inner trough, seen in the canceled introductory letter and twelve live occurrences.','alternatives':['M']},
 {'sign':'Power-set P','latex':r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}} at first occurrence; \mathcal{P} subsequently','ink':'Long stem, unusually broad angular bowl, overhanging upper entry and lower-left return, repeated twice.','alternatives':[r'\mathscr{P}',r'\mathfrak{P}']},
 {'sign':'Fourth centered order label','latex':r'\underset{\unsure{\mathcal{F}|\overline f}}{\ll}','ink':'A detached horizontal cap is clearly separated from a short crossed lower stem with a curved foot.','alternatives':[r'\overline f']},
 {'sign':'Deployment operator','latex':r'\mathrm{Dep}','ink':'D followed by a low e and a descending-loop p; no isolated acute and no following l.','alternatives':[]},
 {'sign':'Current map labels','latex':'(*) and (**)','ink':'Irregular and partly retraced star strokes; no separately readable former label.','alternatives':[]}
]
abbreviations=[{'form':'rel.','expansion':'relation(s)'},{'form':'ens.','expansion':'ensemble'},{'form':'Dep','expansion':'déploiement (probable name; retained as the literal operator in the transcription)'},{'form':'Fig','expansion':'figure(s), operator name retained'}]
unresolved=[
 {'place':'First family F, governing eight family occurrences','reading':r'\mathcal{F}','alternatives':[r'\mathfrak{F}'],'confidence':'medium','evidence':'Cap, crossed stem and hooked foot identify the family letter, but no unique typographic family follows from handwriting; crop 01.'},
 {'place':'First (canceled) M, governing thirteen M occurrences','reading':r'\mathcal{M}','alternatives':['M'],'confidence':'medium','evidence':'The two peaks and rounded trough settle letter identity, while calligraphic versus ordinary handwritten M remains underdetermined; crops 03–04.'},
 {'place':'Fourth order label below ≪','reading':r'\mathcal{F}','alternatives':[r'\overline f'],'confidence':'medium','evidence':'Detached cap and small crossed hooked stem can represent either a compressed family F or barred f; crop 05.'},
 {'place':'First power-set P, governing two P occurrences','reading':r'\mathcal{P}','alternatives':[r'\mathscr{P}',r'\mathfrak{P}'],'confidence':'medium','evidence':'Broad angular bowl and lower-left loop are ornamental but do not settle one font family; crop 08.'},
 {'place':'(**) source before maps-to','reading':r'\mathord{\rlap{$\deleted{X}$}F}','alternatives':['F with the observed extra oblique, without an established canceled X'],'confidence':'low','evidence':'Only one long diagonal is independent of F; a complete predecessor X cannot be separated. Both live/canceled states are printed; crop 13.'}
]
report={'scan':15,'reader':'R1','status':'complete','started_utc':'2026-11-20 12:47:47 UTC','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'view_log':view_log,'differences':differences,'c_doubts':c_doubts,'s_rows':[],'inventory':inventory,'notes':notes,'check_events':check_events,'notation_proposals':notation_proposals,'abbreviations':abbreviations,'unresolved':unresolved,'brief_feedback':[]}
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Report written:',len(differences),'differences;',len(c_doubts),'C doubts;',len(inventory),'inventory items;',len(unresolved),'unresolved loci;',len(view_log),'actual image emissions.')
