from pathlib import Path
from datetime import datetime, timezone
import json, re

b=Path('/workspace/scratch/4770596940a0')
out=b/'out/readers/R1'
rows=[]
def add(i,place,C,H,reading,ink,confidence,kind,crop,ac,ah,mh=False):
    rows.append(dict(id=i,place=place,C=C,H=H,reading=reading,ink=ink,
        confidence=confidence,kind=kind,crop=['crops/R1/scan033_'+c+'.png' for c in crop],
        against_C=ac,against_H=ah,marked_in_H=mh))

add('D01','cancelled opening fragment before 1°)',r'\deleted{\unsure{R|P}}',r'\struck{Or}',
    r'\deleted{\unsure{$R\Rightarrow$|$P\Rightarrow$|Or}}',
    'Looped and upright strokes are heavily cancelled. To their right are two near-horizontal strokes ending in an arrow-like pointed turn. It is uncertain whether that tail is an arrow or part of the cancelled word/stroke. Or is retained as an alternative, not confidently rejected.',
    'low','C doubt expanded; H uncertain initial fragment',['top_delete'],True,True)
add('D02','first F in 1°)',r'\unsure{F|\mathcal F}','F','F',
    'A simple upright, short middle arm and detached curved top arm; no separate calligraphic loop. Read as ordinary F.',
    'high','C doubt resolved',['first_F'],True,False)
add('D03','sideways note, first word',r'\unsure{voir}',r'\uncertain{va ...}','va',
    'Clockwise rotation shows a short v and a filled oval a. No separate i-dot or r ending is present in this group.',
    'high','C doubt resolved differently; H uncertainty resolved',['margin','margin_begin'],True,False,True)
add('D04','sideways note, second word',r'\unsure{une|sa}',r'\uncertain{se ...}','se',
    'A short s-like angled entry and low e-like exit form the second group; the longer une sequence is not present.',
    'high','C doubt resolved differently; H uncertainty resolved',['margin','margin_begin'],True,False,True)
add('D05','sideways note, long word',r'\unsure{simplification}',r'\uncertain{simplifier}','simplifier',
    'The initial si, long mp/l sequence and tall f are followed by a small dotted i and reduced er ending. No separate tall t or tion ending is visible.',
    'high','C doubt resolved differently; H uncertainty resolved',['margin','margin_begin','margin_end'],True,False,True)
add('D06','sideways note ending and long bounding stroke','cf plus bas; margin rule only implicit',r'cf plus \ill{}; editorial note records long rule',
    'cf plus bas; accompanying long curved near-vertical rule reproduced in TikZ',
    'The rotated ending has the c/f and plus groups, then a tall b with low as ending. A separate thin line bounds the note and spans the first two inclusion arguments; it does not cross the body text.',
    'high','H lacuna; graphical boundary preserved',['margin','margin_end'],True,True,True)
add('D07','2°), first tiny superscript after right-hand A',r'A^{\deleted{\unsure{\prime|\ast|?}}}','A',
    r'A^{\deleted{\unsure{\prime|\ast|?}}}',
    'A tiny high hook/angled form has been thickly retraced. The older prime, star or question-mark shape cannot be separated confidently. The glyph is present and locally worked over.',
    'low','C doubt retained; H omitted revision',['case2_right'],False,True)
add('D08','2°), second tiny superscript, before circle(F)',r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}',r'A^{\circ(F)}',
    r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}',
    'The second high dark hook is separate from the small open circle to its right; its prior form is no more securely recoverable than the first occurrence.',
    'low','C doubt retained; H omitted revision',['case2_right'],False,True)
add('D09','2°), bracket around the two inclusions','underline with short end rules','omitted',
    'Long lower bracket with two raised end caps, both formulas retained in a TikZ node',
    'The horizontal stroke runs below the two inclusions; the left end rises and the right end turns upward at the paper edge. It is a grouping mark rather than cancellation.',
    'high','graphical bracket; H omission',['case2','case2_right'],True,True)
add('D10','2°), far-right ending of second inclusion',r'\circ(F)',r'\circ(F)',
    r'\circ(\unsure{F)}',
    'The F is at the cut right edge of the paper/image. The completion of the parenthetical ending is not fully visible; no extra prime is positively seen. Uncertainty is placed on the visible-edge ending rather than supplying a confident completion.',
    'low','new edge-clipping doubt',['case2_right'],True,True)
add('D11','2°), d’où after A-prime equals A',r'd’où A\in F',r'd’où A\prime\in F',r'd’où A\in F',
    'The A has no detached high prime. Its crossbar extends toward the adjacent membership sign; this is not an A-prime stroke.',
    'high','C slip review; H added prime',['dou'],False,True)
add('D12','2°), cancelled words after the bracket/parenthesis','On a','Or',r'\deleted{On a}',
    'An open round O is followed by a low n group and separate a-like ending, all on the crossing stroke. It resembles the earlier cancelled On a on the same paragraph.',
    'high','H cancelled wording',['case2','case2_right'],False,True)
add('D13','after donc A in F-prime, before Il en résulte',r'\deleted{\unsure{et}}',r'\struck{et}',
    r'\deleted{\unsure{et}}',
    'Short joined loop and upright traces survive the dense crossing. Et remains plausible, but the overwriting prevents certainty.',
    'low','C doubt retained',['jedis2','insertion'],False,False)
add('D14','insertion after F-prime preceq F',r'il suffirait F\prime\ll F',r'i.e. sachant F\prime\ll F',
    r'\inserted{il suffirait F\prime\ll F}',
    'Two short initial il strokes precede s and two tall f strokes, then the reduced irait run. The paired left angle tips in the formula are clear. There is no e in an initial i.e. or the expected ch/ant strokes of sachant.',
    'high','H interlinear wording',['insertion'],False,True)
add('D15','parenthesis before cf lemme plus bas',r'\deleted{)}','no deleted parenthesis',r'\deleted{)}',
    'The former closing parenthesis directly after F is crossed by the insertion connector; a later live closing parenthesis follows plus bas.',
    'high','H omitted revision',['insertion','jedis2'],False,True)
add('D16','after cf lemme plus bas)',r'et \deleted{\unsure{bien}}',r'\uncertain{d’autre part}',
    r'et \uline{\unsure{bien}}',
    'There is a short et-like group, then a tall b loop, dotted i and low en ending. A short separate stroke lies just below the middle/baseline, favouring an underline over cancellation. The lexical reading bien is retained cautiously; the state remains uncertain.',
    'medium','C doubt retained with state revised; H wording',['et_bien'],True,True,True)
add('D17','cancelled sign before A,A-prime in F-prime',r'\deleted{\unsure{F|\in}}',r'\struck{\exists}',
    r'\deleted{\unsure{F|\in|\exists}}',
    'An upright with upper/middle arms and a curved lower stroke is intersected by heavy diagonals. A short right upright also survives. The old sign cannot be assigned securely; the H existential candidate remains possible.',
    'low','C doubt expanded; H uncertain glyph',['deleted_quantifier'],True,True)
add('D18','Donc, faint words before prouvé',r'\unsure{on a}','on a',r'\unsure{on a}',
    'Two light separated groups remain, the second little more than a dot/short stroke. On a is compatible with the ink but cannot be made confident from context alone.',
    'low','C doubt retained',['donc_head'],False,False)
add('D19','Donc, overwritten letter under first A-prime',r'\deleted{\unsure{F|A}}A\prime','A-prime without older layer',
    r'\deleted{\unsure{F|A}}A\prime',
    'The overtraced A-prime has extra horizontal cap/arm strokes and a rounded left upright underneath. F and an earlier A are both possible; the final A-prime is clear.',
    'low','C doubt retained; H omitted layer',['donc_head'],False,True)
add('D20','parenthetical d’où ... qed punctuation',r'(d’où A\prime\in F\setminus G\deleted{)}, qed)',r'd’où A\prime\in F\smallsetminus G (qed)',
    r'(d’où A\prime\in F\setminus G\deleted{)}, qed)',
    'The opening parenthesis precedes d’où. A crossed closing parenthesis follows the set difference; qed is then enclosed by a later live close. H relocates the parenthesis.',
    'high','H revision and punctuation placement',['donc'],False,True)
add('D21','next contradiction sentence','Sinon on aurait','Si on avait','Sinon on aurait',
    'After Si, a separate reduced non run remains before the on group. The final word has the additional low ur run before the a-i-t ending.',
    'high','H wording',['sinon'],False,True)
add('D22','pale mark above final live parenthetical line','omitted','omitted',
    'Faint left-pointing arrow-shaped mark reproduced in TikZ; identification/function/hand uncertain',
    'A near-horizontal pale shaft joins two oblique strokes meeting at the left. Small darker spots lie on the upper head arm. It is separate from the black et below and the support formula above. It is not used as a mathematical relation.',
    'medium','new graphical annotation in both witnesses',['pale_trace','donc'],True,True)
add('D23','cancelled b=>c block, word after strate',r'\uline{strate ouverte ... de F\prime}',r'strate \ill{} de F\prime',
    r'\uline{strate ouverte ... de F\prime}',
    'The word ouverte has the initial ou, middle v/er run and final tall t. A long separate underline begins at strate and continues beneath the revised phrase through F-prime.',
    'high','H lacuna and underline',['cancelled'],False,True,True)
add('D24','cancelled b=>c, local crossed words before de F-prime',r'\deleted{dans \unsure{la}}',r'\ill{} with no local revision reading',
    r'\deleted{dans \unsure{la}}',
    'Dans is discernible under one diagonal; the following small group has a tall initial and a low remnant, but several cancellation bars obscure it. La remains only tentative. A lower live de-like ending precedes F-prime.',
    'low','C doubt retained; H omitted local revision',['cancel_words'],False,True,True)
add('D25','cancelled block, after l’unique élément',r'\deleted{de}','omitted',r'\deleted{de}',
    'The d/e loop and exit are cut by a short horizontal stroke, independently of the long diagonal cancellation of the whole block.',
    'high','H omitted local deletion',['cancel_de'],False,True)
add('D26','cancelled b=>c, interlinear assumption','inserted On suppose b) ... phi induces displayed bijection','same words recorded in an external note',
    r'\inserted{On suppose b) i.e. \varphi induit F\prime\setminus G\prime\overset{\sim}{\longrightarrow}F\setminus G}, within global deletion',
    'On suppose b) is legible along the inserted line; a long connector curves down before Soit. The same long oblique cancellation strokes cross the insertion and main paragraph. The mapping arrow points right and carries a high wave.',
    'high','revision-placement review',['cancel_insert','cancelled'],False,False)
add('D27','foot, punctuation after U','soit U,','soit U.','soit U,',
    'A long descending comma follows U at the right edge; it is not a point.',
    'high','H punctuation',['bottom'],False,True)
add('D28','foot, first forked exponent on I',r'I^{\unsure{\ast|k|+}}',r'I^{*}',r'I^{\unsure{k|\ast|+}}',
    'A vertical stem with two rightward projecting arms resembles a small k. A compressed star or cross remains possible. Preference is based on the forked shape rather than the expected open-index notation.',
    'medium','C doubt reordered; H unmarked ambiguity',['bottom_symbols'],True,True)
add('D29','foot, older overwritten operation between F-prime and G-prime',r'\deleted{\unsure{\times|\setminus}}','no older layer',
    r'\deleted{\unsure{\times|\setminus}}',
    'Several angular crossing strokes form a dark patch. The older operator cannot be separated confidently into a cross or a prior slash.',
    'low','C doubt retained; H omitted revision',['bottom_symbols'],False,True)
add('D30','foot, live operation in that same patch',r'\unsure{\setminus}',r'\smallsetminus',r'\unsure{\setminus}',
    'A heavy descending diagonal is visible in the patch, compatible with a set-difference slash; surrounding crossing strokes prevent certainty about the final layer.',
    'low','C doubt retained',['bottom_symbols'],False,False)
add('D31','foot, repeated forked exponent on I-prime',r'I\prime^{\ast}',r'I\prime^{*}',r'{I\prime}^{k}',
    'The second exponent has the same vertical stem and two rightward branches as the first. The first-occurrence uncertainty governs both; k is repeated as the preferred candidate, not newly certified.',
    'medium','recurring ambiguous glyph; preference propagated',['bottom_symbols'],True,True)
add('D32','foot, I after ordonnés','I','I',r'\unsure{I|\vec I}',
    'The I has a thick top bar with a hooked right end and a faint oblique upper arm. This could be a pen turn/correction on the cap or an arrow-like decoration; a separate vector arrow is not certain.',
    'low','new notation doubt',['bottom_I','bottom_ord'],True,True)
add('D33','foot, cancelled triangular letter after I',r'\deleted{\unsure{A|\Delta}}','omitted',r'\deleted{A}',
    'Two angled legs and a raised crossbar are visible beneath a diagonal cancellation. The crossbar is above the bottom rather than closing a delta triangle.',
    'high','C doubt resolved; H omitted deletion',['bottom_I','bottom_ord'],True,True)
add('D34','foot, last open parenthetical phrase and abbreviation','des ens ... I-prime(=F-prime). On a',
    'des ens. ... I-prime(=F-prime)). On a','des ens ... I-prime(=F-prime). On a',
    'No separate point after ens is visible. Only the close belonging to (=F-prime) is present at the end; the outer opening before parties has no visible second close. The last words are On a.',
    'high','H punctuation supplied beyond ink',['bottom'],False,True)
add('D35','manuscript page number','32.','32','32.',
    'A detached point follows the handwritten 32 at the top centre.',
    'high','H omitted visible page-number punctuation',['top'],False,True)
add('D36','all main mathematical relations and exponents','C readings','same substantive readings except separately listed loci','Retain the displayed/in-line C relations',
    'Individually reviewed: both set-difference inclusions; all membership and slashed membership signs; G<=F and G-prime<=F-prime as straight less-or-equal signs; F to the A-prime power; circles with parenthetical F/F-prime; A-prime=A; support bars; F-prime preceq F versus the inserted paired-angle F-prime<<F; the double-headed b iff c arrow and the tilde over the cancelled rightward map.',
    'high','C notation reviews',['top','case2','case2_right','jedis1','jedis2','insertion','donc','cancelled','bottom'],False,False)

specs=[
('CD01','cancelled opening R/P','D01','expanded'),('CD02','first F alphabet','D02','resolved'),
('CD03','margin voir','D03','resolved as va'),('CD04','margin une/sa','D04','resolved as se'),
('CD05','margin simplification','D05','resolved as simplifier'),
('CD06','first cancelled superscript','D07','retained'),('CD07','second cancelled superscript','D08','retained'),
('CD08','cancelled et','D13','retained'),('CD09','bien','D16','word doubt retained; state revised tentatively'),
('CD10','cancelled F/in sign','D17','expanded'),('CD11','on a','D18','retained'),
('CD12','overwritten F/A','D19','retained'),('CD13','cancelled la','D24','retained'),
('CD14','first star/k/plus','D28','preference reordered'),('CD15','old times/slash','D29','retained'),
('CD16','live slash','D30','retained'),('CD17','cancelled A/delta','D33','resolved as A')]
cd=[dict(id=i,occurrence=o,difference_id=d,status=s) for i,o,d,s in specs]

inventory=[]
def inv(i,kind,pos,words,hand='his hand',state=None):
    a=dict(element=i,kind=kind,position=pos,first_words_or_objects=words,
           sheet_kind='text',hand=hand,transcribed='yes')
    if state:a['state']=state
    inventory.append(a)
inv('I01','page number','top centre','32.')
inv('I02','cancelled fragment','before 1°)','R/P/Or with uncertain rightward arrow-like tail')
inv('I03','body proof block','top','1°) F minus G subset F-prime minus G-prime; Tout ... En effet ... A in G')
inv('I04','local deletion','top third line','A in')
inv('I05','sideways note','left edge','va se simplifier, cf plus bas')
inv('I06','long bounding line','left of first two arguments','curved near-vertical rule; reproduced in TikZ')
inv('I07','body proof block','upper middle','2°) F-prime minus G-prime subset F minus G; Soit A-prime ... plus petit él. de F to A-prime')
inv('I08','local deletion','2°), before Soit A le','On a')
inv('I09','bracketed pair of formulas','upper right','A-prime subset A; A-prime-circle(F-prime) subset A-circle(F)')
inv('I10','worked-over superscript','first right-hand A','prime/star/question-mark, uncertain')
inv('I11','worked-over superscript','second right-hand A','prime/star/question-mark, uncertain')
inv('I12','bracket drawing','under two formulas','long lower stroke and raised ends, reproduced in TikZ')
inv('I13','body continuation','after bracket','prouvons que A-prime=A (d’où A in F)')
inv('I14','local deletion','after d’où parenthesis','On a')
inv('I15','body paragraph','middle','Je dis que A in F minus G ... absurde')
inv('I16','local deletion','before Donc A in F minus G','Mais')
inv('I17','body paragraph','middle','Donc A in F minus G, donc A in F-prime, Il en résulte ... ce qui prouve A=A-prime')
inv('I18','local deletion','before Il en résulte','et, uncertain')
inv('I19','interlinear insertion','after car F-prime preceq F','il suffirait F-prime << F; insertion connector')
inv('I20','local deletion','before cf lemme plus bas','former closing parenthesis')
inv('I21','tentatively underlined word','after cf lemme plus bas)','et bien',state='bien uncertain; short stroke tentatively underline, cancellation possible')
inv('I22','cancelled sign','before A,A-prime in F-prime','F/in/exists, uncertain')
inv('I23','body proof block','lower middle','Donc on a prouvé ... Prouvons ... Sinon on aurait ... absurde')
inv('I24','overwritten letter','first A-prime in Donc block','old F/A beneath final A-prime')
inv('I25','revised punctuation','d’où ... qed','crossed close before qed; later live close')
inv('I26','pale separate annotation','above final parenthetical line','left-pointing arrow shape, reproduced in TikZ',hand='uncertain; pale annotation distinct in tone from main black ink',state='presence clear; identification, function and hand uncertain')
inv('I27','globally cancelled proof block','lower third','b) => c) ... Prouvons A-prime-circle(F-prime)=A-circle(F); multiple long oblique strokes')
inv('I28','interlinear insertion within cancelled block','above Soit','On suppose b) i.e. phi induit F-prime minus G-prime ~-> F minus G')
inv('I29','insertion connector','under interlinear assumption','long line curving down before Soit')
inv('I30','underlined phrase','cancelled b=>c','strate ouverte ... de F-prime')
inv('I31','local deletion within cancelled block','before de F-prime','dans la, last word uncertain')
inv('I32','local deletion within cancelled block','after l’unique élément','de')
inv('I33','restarted argument heading','bottom','b iff c')
inv('I34','local deletion','after b iff c','Posons')
inv('I35','body and support equality','bottom','On a |F| minus |G| = |F-prime| minus |G-prime|, soit U,')
inv('I36','body and definitions','bottom','Posons F minus G=I to forked mark; F-prime minus G-prime=I-prime to same mark')
inv('I37','overwriting at operator','between bottom F-prime and G-prime','old times/slash and live slash, both uncertain')
inv('I38','open parenthetical explanation','bottom','parties ouvertes des ens d’indices ordonnés I (=F), I-prime(=F-prime)')
inv('I39','uncertain letter decoration','I after ordonnés','hooked top bar, possibly arrow-like')
inv('I40','local deletion','after I, before (=F)','A')
inv('I41','final incomplete continuation','bottom edge','On a')

tex=(out/'scan033.tex').read_text()
Ctex=(b/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan033.tex').read_text()
assert Ctex.count('\\unsure{')==17
assert len(cd)==17
assert all((b/p).exists() for r in rows for p in r['crop'])
assert len({r['id'] for r in rows})==len(rows)
depth=0;minimum=0
for c in tex:
    if c=='{':depth+=1
    if c=='}':depth-=1
    minimum=min(minimum,depth)
syntax=dict(brace_balance=depth,minimum_brace_depth=minimum,dollar_count=tex.count('$'),
    dollar_count_even=tex.count('$')%2==0,display_opens=tex.count('\\['),display_closes=tex.count('\\]'),
    environments_begin=re.findall(r'\\begin\{([^}]+)\}',tex),
    environments_end=re.findall(r'\\end\{([^}]+)\}',tex),compiled=False,
    scope='Mechanical brace, math delimiter and environment balance only; no LaTeX compilation')
assert depth==0 and minimum==0 and syntax['dollar_count_even']
assert syntax['display_opens']==syntax['display_closes']
assert sorted(syntax['environments_begin'])==sorted(syntax['environments_end'])

now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
run='R1-scan033-20261119T222636Z'; model='GPT-6 Astra Pro'; effort='inherited; not separately exposed'
recipes=json.loads((b/'crops/R1/scan033_recipes.json').read_text())
report=dict(scan=33,manuscript_page='32.',reader='R1',model=model,effort=effort,run=run,
    start_utc='2026-11-19 22:26:36 UTC',end_utc=now,
    images_viewed=[
        'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033.jpg',
        'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033_a.jpg',
        'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033_b.jpg']+[r['file'] for r in recipes],
    viewing_order='Whole image first, then half a, then half b; all 26 listed enlarged crops subsequently emitted and inspected. Sideways note rotated clockwise 90 degrees; no OCR.',
    crops=recipes,differences=rows,C_doubt_resolutions=cd,
    C_doubt_coverage=dict(in_place_occurrences=17,reviewed=17,
        additional_notation_and_slip_rows=['D11','D14','D26','D28','D31','D36']),
    S_decisions=[],S_coverage=dict(source='source/SP34_CW_156-5_sweep3/readings/156-5_CORRECTIONS.tsv',
        applicable_rows=0,decision='No S correction row applies to scan033.'),
    inventory=inventory,
    remaining_doubts=[dict(difference_id=r['id'],place=r['place'],reading=r['reading'],confidence=r['confidence'])
        for r in rows if r['id'] in ['D01','D07','D08','D10','D13','D16','D17','D18','D19','D22','D24','D28','D29','D30','D31','D32']],
    notation=[
        dict(place='top and both numbered arguments',reading=r'F,G,F\prime,G\prime; \subset,\in,\notin; G\leq F; G\prime\leq F\prime',decision='Ordinary F chosen at first occurrence; relation directions and all primes inspected individually.'),
        dict(place='smallest-element sentence and bracket',reading=r'F^{A\prime}; A\prime\subset A; {A\prime}^{\circ(F\prime)}\subset A^{\circ(F)}',decision='Two cancelled high marks retained independently; right-edge ending remains doubtful; grouping bracket drawn.'),
        dict(place='middle lemma reference',reading=r'F\prime\preceq F; F\prime\ll F',decision='The main sign is stacked/curved; the inserted sign has two distinct left tips. Neither was normalized to the other.'),
        dict(place='circle equalities and inclusions',reading=r'A^{\circ(F)}=A^{\circ(F\prime)}; {A\prime}^{\circ(F\prime)}\subset A^{\circ(F\prime)}',decision='F-prime positions and open circles preserved as written; the stated lemma was not independently proved.'),
        dict(place='foot index notation',reading=r'I^{\unsure{k|\ast|+}}; {I\prime}^{k}',decision='Same ambiguous forked glyph in both positions. Preferred k based on stem/arms; star and plus retained at first occurrence.'),
        dict(place='later I after ordonnés',reading=r'\unsure{I|\vec I}',decision='Hooked top bar with faint upper arm; separate arrow status unresolved.'),
        dict(place='pale interlinear annotation',reading='left-pointing arrow shape',decision='Preserved graphically without assigning mathematical meaning or confident authorship.'),
    ],
    notes=[
        dict(id='N033-1',type='reading note',text='The page continues the equality goal by two numbered inclusions. The unprimed A in d’où A in F is retained from ink despite H’s prime.'),
        dict(id='N033-2',type='reading note',text='The main proof invokes cf lemme plus bas; the sideways note reads va se simplifier, cf plus bas. Neither referenced later passage was opened.'),
        dict(id='N033-3',type='reading note',text='The first b=>c proof and its interlinear assumption are globally cancelled. The page restarts b iff c with a support-difference equality and index-set definitions, ending On a.'),
        dict(id='N033-4',type='uncertainty note',text='The short stroke at bien is tentatively treated as an underline; its state remains doubtful. The forked foot superscripts and the operator overwritten between F-prime and G-prime remain explicitly uncertain.'),
        dict(id='N033-5',type='scope note',text='All C doubt occurrences were reviewed from enlarged ink. No other-reader/root report or crop and no scan034 was consulted. Reading and symbol identification are not mathematical checks.'),
    ],
    checks=[dict(statement_id='R1-033-CHECK-1',place='relationship of 1°), 2°) to the set-equality goal',
        date_utc=now,model=model,effort=effort,run=run,type='targeted proof check',
        statement='Conditional sufficiency of the two displayed inclusions for equality of F minus G and F-prime minus G-prime.',
        outcome='Passed as a conditional elementary set-theoretic implication.',
        reasoning='With subset understood as non-strict inclusion, every element of the first difference lies in the second by 1°), and conversely by 2°); extensionality gives equality.',
        limits='This checks only the organization by double inclusion. It does not verify the manuscript’s proofs of the inclusions, the later lemma about open strata, or the b/c equivalence.')],
    reading_coverage=dict(whole=True,both_halves=True,all_lines=True,all_C_doubts=True,
        all_C_H_discrepancies_reviewed=True,sideways_note_rotated=True,no_OCR=True,
        every_listed_crop_actually_viewed=True,no_later_page=True,independent_of_other_readers=True),
    proposed_tex='out/readers/R1/scan033.tex',syntax_check=syntax)
(out/'scan033.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(out/'scan033_crops.json').write_text(json.dumps(recipes,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(saved='out/readers/R1/scan033.json',differences=len(rows),C_doubts=len(cd),
    inventory=len(inventory),crops=len(recipes),checks=len(report['checks']),end_utc=now,syntax=syntax),ensure_ascii=False))
