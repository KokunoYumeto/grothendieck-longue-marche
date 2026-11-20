from decision_helpers import *
import copy
r=load_reports(180)
diffs=[row(r,'A',i) for i in range(18)]
cm={0:'main/01_type_quote_open.jpg',1:'main/03_ad_hoc.jpg',2:'A/L6_f_connector.png',3:'main/04_alors.jpg',4:'A/L9_loc_stop.png',5:'main/05_morphisme_quotes.jpg',6:'A/L12_X_point.png',7:'B/L13_mutuels_verticaux.png',8:'C/L13_cancelled_mark.png',9:'C/L16_four_operations.png',10:'C/L17_partition_insertion.png',11:'C/L16_four_operations.png',12:'A/L18a_primed_insertion.png',13:'A/L19_f_punctuation.png',14:'A/L19_g_connector.png',15:'C/L20_standart_seuls.png',16:'C/L20_standart_seuls.png',17:'C/L20_standart_seuls.png'}
for i,p in cm.items():diffs[i]['crop']='crops/scan180/'+p
diffs[0]['evidence']='Both quotation boundaries have paired high strokes. The opening is at the right end of L1, and the closing is separately inspected at the left of L2 in crops/scan180/main/02_type_quote_close.jpg. Neither edge has angular guillemets.'
diffs[1].update(kind='other',evidence='A short isolated horizontal stroke stands between ad and hoc. Main inspected the complete compound; the medial lexical hyphen is preserved.')
diffs[3]['evidence']='The new baseline begins with a separate a, tall l, low connected ending and a distinctly descending comma before choisissant. The complete alors, omitted by H, is retained.'
diffs[4]['evidence']+=' Root selects A against B/C: the dark upper terminal belongs to the c, with no detached dark stop in the following gap. The much lighter flecks in that gap resemble reproduction grain.'
diffs[6].update(final='$X$. dans',kind='other',evidence='A compact black point lies just beyond the lower right limb of X, separated by a pale gap and aligned with the low writing level. Root selects B/C’s literal inline point over A’s nontext drawing. Its presence is secure; its origin, possible association with the X pen exit and any sentence-boundary role remain unassigned.')
diffs[7].update(final=r'\unsure{virtuels|mutuels}',evidence='The clear right end has u/e-like low strokes, a tall closed l loop and a hooked terminal s, excluding verticaux. At the left, a v-like bowl leads to a low i-like continuation; a small detached point lies above it, followed by an angular r-like entry before the t. Root selects B’s preferred virtuels, while retaining mutuels because the faint early strokes cannot be separated with certainty. A preferred mutuels with verticaux retained; C resolved mutuels. No mathematical expectation settles the word.',confidence='medium',consequential='Against C: the adjective qualifying the diagram morphisms does not support verticaux. The ink favours virtuels, with mutuels retained, so the consolidated text does not supply a definite verticality condition.')
diffs[8].update(final=r'\deleted{\unsure{a|à|,}}',differs_C=True,evidence='A small a-like loop survives above a heavy crossing stroke and a low oblique tail. No separate accent is secure. Root prefers C’s literal unaccented a, while retaining à and comma as supported alternatives. A/B preferred à with comma alternative; all three agree that the mark is cancelled.',confidence='low')
diffs[9]['evidence']+=' Main inspected the full four-operation crop: the first high narrow loop and doubled stem are additional to the live g bowl; all four live letters are g. The first star and bang are low, the last star and bang high. The bangs have detached points and are not primes.'
diffs[10]['kind']='other'
diffs[10]['evidence']+=' The difference against H is uncertainty only at the first capital; its preferred calligraphic alphabet agrees. Both capital occurrences were inspected independently within this contiguous addition.'
diffs[11]['kind']='drawing or diagram'
diffs[15]['evidence']='The final character rises into a crossed/twisted tall stroke and lacks a separate closed d bowl. The visible local spelling is standart; it is not modernized.'
diffs[16]['confidence']='high'
diffs[17]['kind']='drawing or diagram'
diffs[17]['evidence']='Two compact dark points lie above the beginning of Enfin, one slightly higher and to the right of the other, at approximately (1000,1994) and (996,2001). They are visibly distinct from pale copy grain and from the letter below. Their shape and relative position are drawn; their origin and function remain unassigned.'
comparisons=[
 {'place':'L9 first loc','A':'loc without stop','B':'loc.','C':'loc.','decision':'Select A. The dark terminal shape is the c itself, with no detached dark point in the following gap. The weak flecks are comparable to copy grain (A/L9_loc_stop.png). The later loc. remains independently confirmed by all three readers.'},
 {'place':'L12 point beside X','A':'nontext point drawn in TikZ','B':'literal inline point after X','C':'literal inline point after X','decision':'Select B/C’s literal point. A compact separated black mark lies at the low inline writing level. This choice records shape and position, not a sentence boundary or authorship (A/L12_X_point.png).'},
 {'place':'L13 adjective after morphismes','A':'mutuels / verticaux','B':'virtuels / mutuels','C':'mutuels resolved','decision':'Select B’s preferred virtuels, retaining mutuels. The low v/i-like first run, high small point and angular r-like entry favour virtuels; the early strokes remain faint. The clear tall l and final s exclude verticaux (B/L13_mutuels_verticaux.png).'},
 {'place':'L13 cancelled mark','A':'à / comma','B':'à / comma','C':'a / à / comma','decision':'Select C’s preferred literal a, retaining à and comma. The loop is visible but no separate accent is secure beneath/around the heavy crossing (C/L13_cancelled_mark.png).'},
 {'place':'Scope of the remaining-doubts table','A':'seven text doubts plus three physical marks whose origin/function is uncertain','B':'seven text doubts; physical-mark uncertainty in notes','C':'six text doubts; adjective resolved; physical-mark uncertainty in notes','decision':'Retain seven textual uncertainties after restoring the adjective doubt. All three marks are physically clear; their unassigned origin/function stays in the notes and inventory rather than becoming a doubtful word or an unsupported punctuation interpretation.'}
]
unresolved=copy.deepcopy(r['B']['unresolved'])
unresolved[2].update(reading='a',alternatives=['à',','],reason='A-type loop and heavy cancellation are visible, but no separate accent or secure underlying tail can be isolated.')
for u,p in zip(unresolved,['A/L6_f_connector.png','B/L13_mutuels_verticaux.png','C/L13_cancelled_mark.png','C/L16_four_operations.png','C/L17_partition_insertion.png','A/L19_f_punctuation.png','A/L19_g_connector.png']):u['crop']='crops/scan180/'+p
review=[]
qmaps={1:[2],2:[8],3:[9],4:[10],5:[14],6:[13],7:[16],8:[1],9:[2,14],10:[7],11:[9],12:[10,12],13:[13],14:[15,16]}
for i,q in enumerate(r['A']['C_doubt_review'],1):
 ev=q['ink_evidence'];final=q['final_reading'];status=q['decision']
 if i==2:final=diffs[8]['final'];ev=diffs[8]['evidence']
 if i==10:final=r'morphismes \unsure{virtuels|mutuels}; variétés à bord sur d’autres';ev=diffs[7]['evidence']+' The following phrase has no inserted compact; all three independent half readings agree.'
 if i in qmaps:
  ev+=' Main inspected '+', '.join(diffs[j]['crop'] for j in qmaps[i])+'.'
 else:ev+=' All three complete independent half readings agree.'
 if i==8:ev+=' The numeral 6 is confirmed independently by all three half readings.'
 if i==14:ev+=' All three independently read the complete de fondements addition and its guide after travail in the bottom half.'
 review.append({'place':q['question'],'earlier':q['question'],'decision':status+': '+final,'evidence':ev})
inv=[copy.deepcopy(r['A']['inventory'][i]) for i in [0,1,7,2,3,8,4,5,9,6,10]]
inv[2].update(element='literal inline point beside X',kind='text',hand='origin unassigned; main-ink appearance',first_words_or_objects='X. dans; literal visible point without assigned sentence role')
inv[3]['first_words_or_objects']=r'\deleted{\unsure{a|à|,}}'
notes=r'''**S180-notes.** Continuing the sentence from scan 179, the author says that only the “type d'homotopie” needs to be retained, then writes **“On prévoit que les 6 opérations”** on the sheaves can be translated ad-hoc into that framework. For a moderate map between compact moderate spaces, he considers equisingular stratifications adapted to the map and says **“on doit trouver un ``morphisme''”** between the diagrams of manifolds with boundary expressing the two spaces. These are source proposals, not results proved on this sheet.

The four written live operations are Rg_*, Rg_!, Lg^*, g^!, with a doubtful cancelled f under the first live g. Their stars and exclamation marks occur at their respective lower and upper levels; the exclamation marks have distinct points. The constructibility qualification uses the separately inspected partition capitals with low X/Y indices and baseline hyphens. The primed pair X′, Y′ is inserted after loc. fermés, not before it. For unions of strata, the author expects the operations to be expressed through homotopy types. He immediately qualifies the constructions as **“encore partiellement hypothétiques”**, adding **“(y a du travail de fondements sur la planche!)”**. The sentence ends on doivent and continues beyond this page.

The central lexical disagreement remains explicit: **virtuels / mutuels**, with virtuels preferred from the first v/i-like run, a small high point and an angular r-like entry. The clear final tall l and hooked s do not support C's verticaux. This uncertainty concerns the adjective qualifying the diagram morphisms; the text is not repaired to a mathematically expected description. Likewise the two connectors retain plain-line/right-arrow alternatives: an upright terminal turn at L6 and a small near-terminal rise at L19 do not show complete heads. No local proof, type deduction, re-proof or computation was performed by any reader or by root on this page. All three check_events arrays are empty; visual sign inspection is not a mathematical check.

The first loc has no independent stop after the terminal c; root selects A against B/C. The later loc. remains separately confirmed. The cancelled small mark has a loop but no secure accent, so literal a is preferred with à and comma retained. The mark following f is low and elongated, but comma versus point remains uncertain. The word seuls resolves, and the spelling standart and medial hyphen in ad-hoc are preserved. The literal point after X is distinct and inline; no sentence boundary or particular writing hand is inferred. The short oblique stroke below the operation line and the pair of points above Enfin are drawn without assigning a function. Clear physical presence and uncertain origin are distinguished.

There are 23 main baselines, three guided additions and two cancelled/overwritten sites, in one continuing paragraph. Neither mid-line Enfin starts a new paragraph. No display, diagram, independent margin prose, author emphasis underline, heading, date, closing or signature occurs; long strokes under additions are attachment guides. The sheet carries author page **35** and archive pencil **180**. H's numbering note agrees with these separate roles and is editorial metadata only. Supplied English-version comparisons were not consulted or used.
'''
text=(ROOT/'records/scan180/A/reading.tex').read_text()
old=r'$X\raisebox{0pt}[0pt][0pt]{\parbox{0pt}{\figure{\begin{tikzpicture}[overlay]\fill (0.06,0) circle (0.014);\end{tikzpicture}}}}$'
assert old in text
text=text.replace(old,'$X$.')
text=text.replace('% L12: distinct nontext point at about (854,1096), beside the lower right of X; origin uncertain.','% L12: distinct inline point at about (854,1096), just beyond X; origin and sentence role unassigned.')
text=text.replace(r'\unsure{mutuels|verticaux}',r'\unsure{virtuels|mutuels}')
text=text.replace(r'\deleted{\unsure{à|,}}',r'\deleted{\unsure{a|à|,}}')
text=text.replace(r'X\unsure{-|\to}Y',r'X\mathrel{\unsure{-|\to}}Y')
text=text.replace(r"X'\unsure{-|\to}Y'",r"X'\mathrel{\unsure{-|\to}}Y'")
viewed=(ROOT/'records/scan180/main_viewed_crops.txt').read_text().splitlines()
d=write_decision(180,'A',[],diffs,comparisons,unresolved,inv,notes,r['A']['abbreviations'],review,viewed,brief='briefs/brief_v11_scan180.md',workflow_note='Three fresh independent readers each inspected whole/a/b once and covered 23 main baselines, three additions, two cancellation sites, all 14 supplied question rows and the earlier notes. A made 14 crops, B 10, C 9. Main read every field of all three complete returns before image adjudication; it reused 11 saved crops and made five new crops for uncropped witness differences (the wrapped quotation has separate opening and closing edge crops). All 16 root inspections succeeded once, with no recropping or failed display. Distinct reader alternatives about loc, the adjective, the cancelled accent and inline-point treatment were decided from the saved images. No TeX or rendering operation occurred.',text_override=text)
by={}
for rep in r.values():
 for c in rep['crops']:by[c['path']]=c.get('bbox')
for x in d['differences']:
 cp=x['crop'];m=(ROOT/cp).with_suffix('.json');box=json.loads(m.read_text()).get('bbox') if m.exists() else by.get(cp)
 if box:
  if x.get('bbox')!=box:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=box
(ROOT/'records/scan180/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Four operation attachments',r'\mathrm R\deleted{\unsure f}g_*, \mathrm Rg_!, \mathrm Lg^*, g^!','180 L16: all four live g forms inspected together; first two signs low, last two high. Each bang has a separate point. Old first f remains uncertain.'),
 ('Adapted partition capitals',r'\unsure{\mathcal P|P}_X-, then \mathcal P_Y-','180 L17a: both long returning oval capitals independently inspected; X/Y low, hyphens at text level. Same preferred alphabet as earlier partition notation.'),
 ('Two connector forms',r'f:X\unsure{-|\to}Y; g:X′\unsure{-|\to}Y′','180 L6/L19: first endpoint upright, second with a small near-terminal rise and faint tail. Their arrow doubts remain local, not resolved by the word morphisme.'),
 ('Variable abbreviation stops','loc; later loc.','180 L9/L18: first c has no detached stop; later abbreviation independently read with a point. Do not regularize.'),
 ('Literal inline point','$X$. dans','180 L12: a separated compact point lies just beyond X at the low writing level; no sentence-boundary or authorship inference is made.')
])
register_note_statements(180,[
 {'place':'L1–L4; notes paragraph 1','statement':'The author proposes retaining only the homotopy type and anticipates translating six sheaf operations ad-hoc into this framework.'},
 {'place':'L5–L15; notes paragraph 1','statement':'For an adapted equisingular stratification of a moderate map, the author proposes a morphism between diagrams of manifolds with boundary; the adjective qualifying its component morphisms remains virtuels/mutuels.'},
 {'place':'L16–L21; notes paragraph 2','statement':'The four written operations for an induced map on locally closed unions of strata are expected to be expressible through operations between homotopy types.'},
 {'place':'L21–L23; notes paragraph 2','statement':'The author explicitly calls the constructions partly hypothetical and says foundational work remains.'}
])
