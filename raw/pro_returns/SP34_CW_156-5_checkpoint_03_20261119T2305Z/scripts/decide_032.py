from adjudication import *
n=32;rr=reports(n)
t=(O/'documentation/main_032_proposal.tex').read_text().replace('% Provisional main-reader proposal, before comparison of the three reports.','% Adjudicated after the three independent readings and supplemental close checks.')
a=[differences(d) for d in rr]
m1={1:1,2:2,3:3,4:4,5:5,6:7,7:8,8:9,9:10,10:11,11:15,12:12,13:13,14:15,15:14,16:15,19:16,20:18,21:18,22:17,23:18,24:19,25:20,26:21,27:22,28:23,29:24,30:27,31:25,32:26,33:27,34:28,35:29,36:30,37:31,38:31,39:32,40:32,41:32,42:33,43:34,44:35,45:15,46:36,47:37,48:38,49:40,50:40,52:43}
m2={1:1,2:2,3:26,4:3,5:4,6:27,7:28,8:30,9:5,10:6,11:31,12:32,13:33,15:7,16:34,18:35,19:51,20:36,21:37,22:8,23:38,24:9,25:10,26:11,27:12,28:13,29:14,30:41,31:15,32:16,33:42,34:40,35:17,36:18,37:44,38:45,39:46,40:47,41:47,42:19,43:20,44:21,45:48,46:22,47:23,48:24,49:49,50:50,52:29}
cr={1:'top',2:'top_erased',3:'a_compare',4:'top_mark',5:'top_on',6:'top',7:'top',8:'top',9:'ultra',10:'heading',11:'heading',12:'heading',13:'a',14:'a',15:'element',16:'a_attachment',17:'a_attachment',18:'a',19:'a_smallmark',20:'star_word',21:'star',22:'star_word',23:'star',24:'long_top',25:'long_top',26:'long_top',27:'precedemment',28:'margin_wordline',29:'precedemment',30:'margin_full',31:'margin_full',32:'margin_full',33:'margin_full',34:'margin_full',35:'b',36:'NB',37:'NB',38:'b',39:'c_d',40:'c_d',41:'c_d',42:'proof_on',43:'proof_on',44:'proof_on',45:'proof_on',46:'proof',47:'inclusion',48:'inclusion',49:'inclusion',50:'inclusion',51:'proof',52:'setminus_hook'}
rows=[]
for i,x in enumerate(a[2],1):
    reads=[reading(a[0][m1[i]-1]) if i in m1 else 'see explicit proposal',reading(a[1][m2[i]-1]) if i in m2 else 'see explicit proposal',reading(x)]
    y=row(n,i,x,reads,f'crops/root/032_{cr[i]}.png')
    if i==1:
        y.update(final='F',against_C=True,against_H=False,confidence='medium')
        y['ink']='Main compared the upright and two right crossbars with the plain F forms in the union and later formulas. The return curve is part of the same hand’s ordinary capital; no separate alphabet is imposed. R1/R2 retain alphabet uncertainty; R3 and main choose plain F.'
    if i==2:y['final']=r'\deleted{Reste}'
    if i==3:
        y.update(final=r'reste \unsure{à|:} voir que une strate',against_C=True,against_H=True,confidence='low')
        y['ink']='Lowercase reste and separate que une are clear. All three readers choose à. Main’s isolated enlargement shows a small rounded lower body and a separate curved upper stroke: an accented a is first, but a colon remains possible because there is no secure exit stroke on the lower component. The uncertainty is preserved rather than settled by grammar.'
    if i==4:
        y['final']=r'\inserted{\unsure{$G$|$\in$}}'
        y['ink']+=' R2 resolves G; main retains G/membership uncertainty because the shared upper stroke and inward middle bar do not fully distinguish the forms.'
    if i==5:
        y.update(final=r'\deleted{On}',against_C=True,against_H=False,confidence='medium')
        y['ink']='Main compared the open entry curve, inner loop and connected low n with the single live On at the foot. The same construction survives the separate horizontal cancellation here. This resolves On with R2; R1/R3 retain uncertainty.'
        y['crop']+=' Comparison: crops/root/032_proof_on.png.'
    if i in (6,7):
        y['consequential']='Retain the visible first-case G′ prime at this separate occurrence; H’s unprimed G is not what the ink shows. Any mathematical issue is discussed separately.'
    if i==11:y['readers']=[r'\uline{Corollaire}']*3
    if i==14:y['readers']=['whole condition deleted; X described but not drawn','whole condition deleted; X not drawn','whole condition deleted; X drawn'];y['final']='complete a), locally revised and globally cancelled, with both diagonals drawn'
    if i==16:y['readers']=['deleted underlined maximal, replacement above']*3
    if i==17:y['readers']=['comma absent from submitted TEX','comma absent from submitted TEX','comma after the cancelled maximal/replacement group'];y['final']='comma before pour, following the local replacement group'
    if i==18:y['readers']=["l’ens without point"]*3
    if i==20:
        y.update(final=r'\unsure{cela|cel} revient',against_C=True,against_H=True,confidence='medium')
        y['readers']=['cela revient']*3
        y['ink']='The rotated crop shows c/e, a tall looped l and a short terminal movement. All three readers read cela; main puts that first but retains the possibility of a contracted cel because the final a body is not independently clear. H’s il is excluded by the initial c-like stroke and longer group.'
    if i==21:y['readers']=['au =']*3
    if i==23:y['readers']=['d’une = F']*3
    if i==26:y['readers']=[r'\uline{impliquées} par a)']*3
    if i==27:
        y.update(final=r'\unsure{lesquelles|laquelle}',against_C=False,against_H=False,confidence='medium')
        y['ink']='The q descender and two l loops are clear. Main retains the initial le/la and final singular/plural uncertainty with R1 because the short low strokes meet the oblique crossing; R2/R3 resolve lesquelles. The unresolved alternative is retained in place.'
    if i==29:
        y.update(final=r'la subdivision construite \unsure{précédemm\textsuperscript{t}|précédemment|précédemment\textsuperscript{\#}}',against_C=True,against_H=True,confidence='medium')
        y['ink']='Main separately enlarged the ending: a compact double-upright crossed mark stands above the reduced final run. R1’s abbreviated précédemm with raised t is first; R3 reads the full word, and R2 retains a possible separate hash-like call. The height and all viable alternatives are preserved; the mark is not moved back onto construite as in H.'
    if i==34:
        y.update(final='complete note inside an uncertain deletion marking, with its internal curved stroke drawn',kind='deletion state (struck given live or live given struck)',against_C=True,against_H=True,confidence='medium')
        y['ink']='The curve passes through conditions, équivalentes, impliquées, the later noun/verb lines and the final line, rather than following an exterior edge. All three readers prefer or allow cancellation, with a non-cancelling grouping/review stroke still possible. Main draws the path and uses an outer unsure around the full deletion; that outer doubt concerns state only. Every word remains present.'
        y['consequential']='The long oblique correction is fully preserved with explicitly uncertain whole-note cancellation state; it is not treated as a certainly live replacement of the displayed implication cycle.'
    if i==37:y['readers']=['surj. donc ... ici, without extra comma']*3
    if i==38:
        y['readers']=['underlined injectivité and drawn left rule','underlined injectivité and left rule with small lower bend','underlined injectivité and drawn left rule']
        y['final']='plain NB.; underlined injectivité; thin left rule with slight bottom hook'
        y['ink']+=' Main retains the slight lower bend visible at the base, also distinguished by R2.'
    if i==40:y['readers']=['ouverte live in the upper replacement']*3
    if i==41:
        y['readers']=['report identifies insertion; TEX leaves it unwrapped','full replacement including lower de F′ marked inserted','full replacement including lower de F′ marked inserted']
        y['final']='upper quantified replacement marked inserted; lower de F′ retained on its continuing baseline'
        y['ink']+=' Main marks the physically interlinear words as inserted and keeps the lower continuation at its own level, without asserting when that lower continuation was first written.'
    if i==45:y['readers']=[r'\uline{Dém}, no point']*3
    if i==46:y['final']=r'\deleted{\uline{Dém}}'
    if i==48:
        y['H']='identité, without the live replacement layer'
        y['final']=r'\unsure{inclusion}'
        y['ink']+=' R1/R2 resolve inclusion; main and R3 retain uncertainty because the darker low ending and older t/é strokes remain inseparable in places. This uncertainty does not promote identité to the live layer.'
    if i==50:y['readers']=[r'\inserted{can. $F\setminus G\hookrightarrow F$}']*3
    if i==51:y['readers']=['d)⇒b) Si, no intervening point']*3
    if i==52:
        y['readers']=[r'\unsure{\swarrow} beneath the slash','actual hook strokes drawn beneath slash','actual hook strokes drawn beneath slash']
        y['final']='separate down-left hook/arrow-like strokes drawn below the set-difference slash, without assigned function'
        y['ink']='Main’s 4.5× crop shows a white gap below the thick slash, then a long curving downward-left stroke, shorter left arm and joined low foot. R2 found it independently; R1/R3 independently rechecked it in supplements. Its shape is reproduced without selecting a mathematical arrow meaning.'
    rows.append(y)

def add(i,place,C,H,reads,final,ink,crop,kind='other',c=False,h=False,confidence='high',review=None):
    x=dict(id=f'032-{i:02}',place=place,C=C,H=H,readers=reads,final=final,ink=ink,crop='Main enlargement crops/root/032_'+crop+'.png; recipes in documentation/crops.jsonl.',kind=kind,against_C=c,against_H=h,confidence=confidence,marked_in_H='no')
    if review:x['review_type']=review
    rows.append(x)
add(53,'bottom equality, terminal punctuation','no point','point',['point']*3,'point after F′ minus G′','A separate dark point stands after the closing G′ at the bottom edge; it is distinct from the page border.','proof',c=True)
add(54,'cancelled union, lower index','B≤F','B≤F',['B≤F']*3,'B≤F, literally','The lower terminal F has a stem and two right arms like the F above. It is not silently changed to A. The ≤ lower dash is separate and B carries the same capital form as above.','union',review='C notation/slip review')
add(55,'remaining mathematical signs and primes','C signs','same substantive signs',['C signs retained']*3,'F″, F′, G′; order with lower curve and star; tilde over right arrow; open circle on A; superset; four rightward double arrows; restriction bar','All occurrences were checked individually in the upper argument, a), b), c), d), the implication cycle and bottom equality. This is a notation review, not an independent proof.','top',review='C notation review')
add(56,'leader for inserted chacune','insertion text, no leader drawing','added des, no leader drawing',['insertion identified, leader not drawn']*3,'curved leader to the insertion point before des, drawn with the full corollary','The thin curve descends from the end of the raised word and turns to the left of baseline des. It is separate from the cancellation through raffinement.','heading',kind='drawing or diagram',c=True,h=True)
add(57,'a), local attachment and wavy underline','no paths drawn','no paths drawn',['not drawn']*3,'thin attachment from maximal to its raised replacement; wavy stroke below pour/order','The thin upper line leaves the right of the cancelled maximal and reaches the raised replacement. A distinct shallow wavy stroke lies below pour and the order sign, independently of the two large diagonals.','a_attachment',kind='drawing or diagram',c=True,h=True)
add(58,'a), retraced start of dans','dans','dans',['dans, no separate old word','dans; older p/word not securely separable','dans, no separate old word'],'dans, without invented underlying text','The first letter has a long retraced lower loop. Main rechecked it against R2’s specific review; the live dans is readable but a former letter cannot be recovered independently of its own d strokes.','a',review='revision review; no recoverable extra text')
add(59,'top insertion, oblique placement stroke','raised glyph; leader not drawn','added de G; leader not drawn',['not drawn']*3,'raised uncertain G/membership glyph and its oblique leader','The curved oblique stroke lies to the right of the raised glyph and reaches the gap before de F; it has no arrowhead. Both the mark and its placement are preserved.','top_mark',kind='drawing or diagram',c=True,h=True)

inv=json.loads((O/'documentation/main_032_inventory.json').read_text())
notes=(O/'documentation/main_032_notes.txt').read_text()
notes+='\n[TXT032-small-readings] Main retains à/colon at the opening despite the three readers’ preference for à, and cela/cel in the starred gloss despite their full-word reading. The small raised mark after strate remains G/membership, with R2 preferring G. The abbreviation/raised t/hash alternatives after construite remain explicit. R1/R2 resolve the final inclusion while main/R3 retain a doubt in its crowded live layer. The comma before pour in a) and the terminal point after the bottom equality are restored. Both small unidentified graphic marks are preserved.\n'
notation=[{'sign':'ordinary F and G primes','form':'F; A∉G′ and F\\G′⊂F′ in first case','evidence':'032_top and 032_union; separate high ticks at both G occurrences.','ambiguity':'R1/R2 retain F alphabet uncertainty; main/R3 use ordinary F. First-case primes remain literal despite the limited set-family counterexample.'},{'sign':'literal equals shorthand','form':'au =; d’une = F','evidence':'032_star, rotated clockwise.','ambiguity':'Do not expand either sign to même in the transcription.'},{'sign':'raised contracted ending','form':r'\unsure{précédemm\textsuperscript{t}|précédemment|précédemment\textsuperscript{\#}}','evidence':'032_precedemment.','ambiguity':'Raised crossed ending: abbreviated t, full-word terminal t or separate hash-like call.'},{'sign':'small unassigned pen marks','form':'TikZ angular mark below qui; hooked mark below set-difference slash','evidence':'032_a_smallmark and 032_setminus_hook.','ambiguity':'Neither is assigned an alphabetic or mathematical role.'}]
extra=json.loads((O/'documentation/main_032_checks.json').read_text())
save(n,t,rows,inv,notes,rr,notation,{'can.':'canonique','p. ex':'par exemple','tjrs / tojrs':'toujours','cond.':'conditions (uncertain abbreviation)','précédemm with raised t':'précédemment (uncertain contraction)','cel':'cela (possible contracted spelling)','ens':'ensemble'},'Whole page then both halves read independently by all three readers and main; every C doubt and C/H discrepancy enlarged; oblique notes rotated. All 25 C doubt occurrences individually reviewed. Supplemental independent checks covered the lower hook beneath the set-difference slash and the angular mark beneath qui. Graphic cancellation/attachment strokes preserved with complete wording.',extra_checks=extra)
