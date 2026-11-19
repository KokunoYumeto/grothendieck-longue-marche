from pathlib import Path
from datetime import datetime, timezone
import json

base = Path('/workspace/scratch/4770596940a0')
out = base / 'out/readers/R3'
source = base / 'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan028.jpg'
cpath = base / 'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan028.tex'
tex = cpath.read_text()
old = r"\deleted{\deleted{\uline{Proposition}} Soient $\unsure{F|\mathcal F},G$ deux figures \unsure{ens.} de $\mathcal L$. \deleted{\unsure{Cons}} Soit \deleted{$\unsure{K|H}$}}"
new = r"\deleted{\uline{Proposition}} Soient $F,G$ deux figures \unsure{ens.} de $\mathcal L$. \deleted{\unsure{Cons}} Soit \deleted{$\unsure{K|H}$}"
assert old in tex
tex = tex.replace('% @ top, cancelled proposition lines 1–2', '% @ top, individually cancelled heading and abandoned start; opening sentence retained live')
tex = tex.replace(old, new)
tex = tex.replace(r"(i,\unsure{j'|j})", r"(i,j')")
tex = tex.replace(r"\unsure{A_i'|A_i}&", r"A_i'&")
(out / 'scan028.tex').write_text(tex)

crops = json.loads((out / 'scan028_crops.json').read_text())
cp = {c['name']: c['path'] for c in crops}
diffs = []
def d(place, C, H, reading, ink, confidence, kind, crop, ac=False, ah=True, mh=False):
    ident = f'R3-028-D{len(diffs)+1:02}'
    diffs.append(dict(id=ident, place=place, C=C, H=H, reading=reading, ink=ink,
                      confidence=confidence, kind=kind, crop=cp[crop],
                      against_C=ac, against_H=ah, marked_in_H=mh))
    return ident

d('top, cancellation boundary of opening two lines',
  r'\deleted{... Soient F,G deux figures ens. de L. ... Soit ...}',
  'Opening sentence live; later editorial note says cancellation begins at Soit K.',
  'Opening sentence and Soit live; only Proposition, Cons and the letter after Soit individually deleted.',
  'No crossing stroke traverses Soient F,G deux figures or ens. de L. The heading has its own short crossings. The uppermost long diagonal begins around the abandoned Cons and goes down left across the construction below. The extent intended for the cancellation is not fully decidable from these endpoints.',
  'medium', 'deletion state (struck given live or live given struck)', 'top', True, False)
d('top, heading Proposition', r'\deleted{\uline{Proposition}}', r'\struck{Proposition}',
  r'\deleted{\uline{Proposition}}',
  'A nearly horizontal rule is directly beneath the heading, distinct from the short rising cancellation strokes through its letters.',
  'high', 'omission', 'top')
c01 = d('top, first F', r'\unsure{F|\mathcal F}', 'F', 'F',
  'An upright with two separate straight rightward arms; no enclosing loop or swept lower return.',
  'high', 'other', 'top', True, False)
c02 = d('top, abbreviation after figures', r'\unsure{ens.}', r'\uncertain{ens.}', r'\unsure{ens.}',
  'Low initial loop, joined humps and terminal point. ens. is supported, but the compressed middle is not independently resolved.',
  'medium', 'other', 'top', False, False, True)
d('top, preposition before L', 'de', 'dans', 'de',
  'A looped d followed by a short low horizontal e; no n/s continuation.',
  'high', 'misread word', 'top')
c03 = d('top, abandoned start before Soit', r'\deleted{\unsure{Cons}}', r'\struck{Considérons}',
  r'\deleted{\unsure{Cons}}',
  'A C-like loop and short ons-like low run survive. There is no space or sequence of upright letters for the expanded Considérons. The deletion masks the last short strokes, so Cons remains marked.',
  'medium', 'abbreviation expanded or spelling modernised', 'top')
c04 = d('top, deleted letter after Soit', r'\deleted{\unsure{K|H}}', r'\struck{K}',
  r'\deleted{\unsure{K|H}}',
  'Intersecting short diagonals cross an upright and crossbar. The right fork can belong to K or to the cancellation over H.',
  'low', 'misread symbol or index', 'top')
c05 = d('top, older letter after K in set definition', r'\deleted{\unsure{I|J}}', r'\struck{I}',
  r'\deleted{\unsure{I|J}}',
  'Broad top and bottom bars with a dark overwritten upright; the lower turn is obscured, so I/J remains open.',
  'low', 'misread symbol or index', 'top')
d('upper and middle construction, block cancellation',
  'Construction from the defining set through C_k enclosed in deleted macros.',
  'Formulae and argument rendered live; cancellation conveyed only by a following editorial note.',
  'Defining set, de sorte que, coproduct, following argument and C_k display deleted; no editorial sentence in transcription.',
  'Several long rising diagonals cross the successive lines, including the final C_k=A cap B. These are block cancellation strokes, additional to local word corrections.',
  'high', 'deletion state (struck given live or live given struck)', 'cancelled_middle')
d('upper connector between first set and coproduct', r'\deleted{de sorte que}', r'\struck{Il est clair} que',
  r'\deleted{de sorte que}',
  'At left a small d/e group, then s-o-r-t-e with a tall t-like turn, and a long descending q in que. There is no separate Il or clair.',
  'high', 'misread word', 'coproduct')
c06 = d('upper coproduct, support at left', r'|F\unsure{\cap\,\mid|\mid\cap\mid}G|', r'|F|\cap|G|',
  r'|F\unsure{\cap\,\mid|\mid\cap\mid}G|',
  'The outer bars and the bar just before G are clear. Immediately after F, a short upright merges with the cap; a distinct closing bar for F cannot be securely isolated.',
  'low', 'misread symbol or index', 'coproduct')
c07 = d('upper coproduct, older lower-limit letter', r'\deleted{\unsure{I|J}}K', 'K',
  r'\deleted{\unsure{I|J}}K',
  'Dark older top and bottom bars remain behind the K in the lower limit; the bottom turn is overwritten. This is a separate occurrence from the first defining set.',
  'low', 'omission', 'coproduct')
d('cancelled paragraph, first equivalence abbreviation', "d'équi.", "d'équiv.", "d'équi.",
  'After the q descender the ending has a low u, a small dotted i and a point; no separate final v is distinguishable.',
  'high', 'abbreviation expanded or spelling modernised', 'cancelled_middle')
d('cancelled paragraph, interlinear equivalence abbreviation', r"\inserted{d'équi.}", "d'équiv. on baseline", r"\inserted{d'équi.}",
  'The short d’équi. group is above the baseline between relations and induites. Its ending is the small i/point form, not an additional v.',
  'high', 'insertion or placement', 'cancelled_middle')
c08 = d('cancelled paragraph, correction immediately before induites', r"\inserted{d'équi.} \deleted{\unsure{H}}induites",
  r"d'équiv. \struck{induites} \add{induites}", r"\inserted{d'équi.} \deleted{\unsure{H}}induites",
  'Below the added d’équi. is a compact crossed capital-like pair of uprights. The following induites occupies the baseline once; no second written induites appears above it. The small cancelled capital itself remains uncertain.',
  'low', 'insertion or placement', 'cancelled_middle')
c09 = d('cancelled paragraph, relation letter with subscript F', r'\unsure{\mathcal R|\mathscr R}_F', 'R_F',
  r'\unsure{\mathcal R|\mathscr R}_F',
  'A large leftward loop and swept diagonal leg form a script R, with a small F below. The boundary between the calligraphic and script rendering remains undecided.',
  'medium', 'misread symbol or index', 'cancelled_middle')
d('cancelled paragraph, relation letter with subscript G', r'\mathcal R_G', 'R_G', r'\mathcal R_G',
  'The second R again has a loop extending left of the shaft and a sweeping leg; the recurring alphabet doubt is marked on the first R of the page. G is open and curved below.',
  'medium', 'misread symbol or index', 'cancelled_middle')
d('end of cancelled paragraph, after deleted des', 'pour k=(A,B)', 'les parties, then displayed k=(A,B),',
  'pour k=(A,B), in the prose line, without a written comma after the closing parenthesis',
  'A long p descender starts the short low word pour. The k=(A,B) lies on the same manuscript line. No les parties or terminal comma is visible.',
  'high', 'misread word', 'cancelled_middle')
c10 = d('last cancelled formula, overwritten item before C_k', r'\deleted{\unsure{A_k}}', 'omitted',
  r'\deleted{\unsure{A_k}}',
  'A crossed triangular capital and a small low k-like mark remain immediately to the left of C_k; the small index is not fully separable from the overtrace.',
  'low', 'omission', 'cancelled_middle')
d('first diagram, inclusion signs and relative position of objects',
  'L above S and S-prime; two rotated inclusion signs without connecting shafts.',
  'Hook arrows from S and S-prime to L, with S and L on one upper row; an editorial description follows.',
  'Retain C diagram with L above the two subset objects and the two isolated slanted inclusion signs.',
  'The marks between the upper L and the two S objects are open curved subset/superset glyphs. They have no shafts or distinct arrowheads. The actual vertical arrows below are shafted and headed.',
  'high', 'drawing or diagram', 'diagram1')
c11 = d('first diagram, old letter behind S-prime', r'\deleted{\unsure{T}}', 'omitted',
  r'\deleted{\unsure{T}}',
  'A horizontal bar projects left behind the overdrawn S-prime and a central older downstroke is partly visible. T remains probable but not certain under the S.',
  'medium', 'omission', 'diagram1')
c12 = d('first diagram, small cancelled subscript by S-prime', r'\deleted{\unsure{k|n}}', 'omitted',
  r'\deleted{\unsure{k|n}}',
  'Small angular uprights and a crossing below the prime remain. Both k and n are possible; the overtrace prevents a firm choice.',
  'low', 'omission', 'diagram1')
d('after first diagram, H explanatory note', 'no editorial note',
  'Note explaining inclusion signs and asserting there is no other croquis.',
  'No editorial note; retain the manuscript side text I,J ens. ord.',
  'The right-hand side of the diagram carries only I,J ens. ord. The explanatory French sentence in H has no corresponding ink.',
  'high', 'text not on the page', 'diagram1')
c13 = d('second diagram, left vertical label', r'\unsure{\psi|Y}', r'\psi', r'\unsure{\psi|Y}',
  'Two upward arms meet a long lower stroke; there is no loop resolving a Greek psi against capital Y. Nearby phi labels do not settle this glyph.',
  'medium', 'misread symbol or index', 'diagram2')
d('second diagram, left vertical edge S cap T to K', 'headless vertical line', 'downward arrow', 'headless vertical line',
  'The lower end is a bent continuation of the shaft, without two converging arrowhead strokes; the nearby arrows to I and I-prime have visible heads.',
  'high', 'drawing or diagram', 'diagram2')
c14 = d('second diagram, object below the headless line', r'\deleted{\unsure{J|I}}K', 'K',
  r'\deleted{\unsure{J|I}}K',
  'An older barred letter has a leftward hooked base beneath the K overtrace. That hooked base is not a box surrounding K; J/I remains uncertain.',
  'low', 'omission', 'diagram2')
d('second diagram, rightmost L', 'L', r'\mathcal L', 'L',
  'Long straight upright with an angular horizontal foot; no lower-left loop of the L in the first diagram.',
  'high', 'misread symbol or index', 'diagram2')
d('foot, word before K image definition', 'avec', 'où', 'avec',
  'Four low joined strokes start with a small a and end in an open c-like turn; no elevated accent or distinct où group.',
  'high', 'misread word', 'bottom')
c15 = d('foot, pair inside the comprehension', r"(i,\unsure{j'|j})", "(i,i')", "(i,j')",
  'Second component has a long descender and leftward hooked bottom, unlike the first dotted i. A separate high oblique tick precedes the closing parenthesis.',
  'high', 'misread symbol or index', 'edge_set', True, True)
c16 = d('foot, cancelled letter before the second intersection factor', r'\deleted{\unsure{B}}', 'omitted',
  r'\deleted{\unsure{B}}',
  'Two rounded remnants survive under the heavily redrawn capital; B is the best recoverable older form but the crossings are dense.',
  'low', 'omission', 'edge_set')
c17 = d('foot, live second intersection factor and its subscript', r'\unsure{A_{i\prime}^{\prime\circ}|B_{j\prime}^{\prime\circ}}', r"A'^{\circ}_{i'}",
  r"\unsure{A_{i'}^{\prime\circ}|B_{j'}^{\prime\circ}}",
  'The capital and low index are both overdrawn. A diagonal outline favours A, but a bowed B and descending j-like subscript remain possible; prime and raised circle are present. The boxed formula is not used to settle the overtrace.',
  'low', 'misread symbol or index', 'edge_set')
d('bottom left, words after si j=(i,i-prime)', 'on aura', 'on pose', 'on aura',
  'The second word begins with a low a/u run and ends in a small r/a turn. It has no initial p descender; contrast the actual pose at bottom right.',
  'high', 'misread word', 'bottom')
c18 = d('bottom right, left side of first definition', r"\unsure{A_i'|A_i}", 'A_i', "A_i'",
  'A detached high vertical tick stands to the upper right of A and above its low dotted i. It is absent from the boxed A_i on the left.',
  'high', 'misread symbol or index', 'defs', True, True)
c19 = d('bottom right, old letter beneath second definition', r'\deleted{\unsure{A}}', 'omitted',
  r'\deleted{\unsure{A}}',
  'Two converging diagonals and a crossbar remain under the bowed replacement. The layers cannot be completely separated, so the older A stays uncertain.',
  'low', 'omission', 'defs')
c20 = d('bottom right, current left side of second definition', r"\unsure{B_j'|A_j'}", "A'_{i'}",
  r"\unsure{B_j'|A_j'}",
  'Upper and lower bowed portions favour B over A, but both letter layers remain. The subscript has a long hooked descent like j and the prime is high beside the capital; it is not a short i-prime index.',
  'low', 'misread symbol or index', 'defs')
d('bottom right, bound in the second preimage', r"I'_{\leq j}", r"I'_{\leq i'}", r"I'_{\leq j}",
  'The bound has a long stroke below the baseline turning left. No detached prime follows this bound; the prime belongs to I above.',
  'high', 'misread symbol or index', 'defs')
d('after bottom display, H explanatory note', 'no editorial note',
  'Note asserting boxed K in the diagram and commenting on expected I times I-prime.',
  'No editorial sentence; K is an overwritten diagram object and the written target remains I times J.',
  'There is no boxed K: the surrounding lower strokes are the older barred letter. The only manuscript box encloses A_j=A_i cap A-prime_i-prime. There is no prose stating the expected target.',
  'high', 'text not on the page', 'bottom')

cd_ids = [c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20]
resolved = {1,15,18}
cd = []
for n, ident in enumerate(cd_ids, 1):
    x = next(x for x in diffs if x['id'] == ident)
    cd.append(dict(occurrence=n, difference_id=ident, place=x['place'], C=x['C'],
                   reading=x['reading'], status='resolved' if n in resolved else 'retained',
                   confidence=x['confidence'], ink=x['ink'], crop=x['crop']))

inventory=[]
def inv(kind, position, content):
    inventory.append(dict(scan='028', sheet_kind='text', hand='his hand',
                          element=f'R3-028-I{len(inventory)+1:02}', kind=kind,
                          position=position, first_words_or_objects=content, transcribed='yes'))
inv('text','top centre','manuscript page number 27')
inv('deletion','top left','underlined Proposition, individually crossed')
inv('text','top two lines','Soient F,G deux figures ens. de L. ... Soit')
inv('deletion','top second line','Cons, abandoned start')
inv('deletion','top second line after Soit','K|H, individually crossed')
inv('display','upper first display, cancelled','K deleted(I|J)={(A,B) in F times G | A-circle cap B-circle nonempty}')
inv('deletion','upper first display','older I|J')
inv('deletion','upper connector','de sorte que')
inv('display','upper second display, cancelled','support intersection = coproduct of A-circle cap B-circle')
inv('deletion','coproduct lower limit','older I|J behind K')
inv('deletion','middle five-line block','et que les ... classes ... borne sup ... Considérons ... pour k=(A,B)')
inv('deletion','middle first line','relations')
inv('insertion','above middle induites','d’équi.')
inv('deletion','middle before induites','H-like cancelled capital')
inv('deletion','middle Considérons line','la famille')
inv('deletion','middle following line','des')
inv('display','last cancelled display','deleted A_k, C_k=A cap B')
inv('deletion','last cancelled display before C_k','A_k')
inv('diagram','lower middle','L over S and S-prime; slanted inclusion signs; phi surj and phi-prime surj to I,I-prime')
inv('deletion','first diagram, before S-prime','older T')
inv('deletion','first diagram, below S-prime','small k|n')
inv('text','right beside first diagram','I,J ens. ord.')
inv('text','lower introduction','Considérons')
inv('diagram','lower diagram','S cap T, S,T,L,I,I-prime,K; hooked inclusions, phi, phi-prime, headless psi|Y line and projection arrows')
inv('deletion','second diagram, lower-left object','J|I beneath K')
inv('text','foot before image formula','avec')
inv('display','foot across page','K=Im(S cap T to I times J)={(i,j-prime) in I times I-prime | ... nonempty}')
inv('deletion','far right of image formula','older B beneath second intersection factor')
inv('text','bottom left','si j=(i,i-prime), on aura')
inv('display','bottom centre','boxed A_j=A_i cap A-prime_i-prime')
inv('text','bottom right before definitions','où on pose')
inv('display','bottom right, two lines','A_i-prime=phi inverse(I<=i); deleted A, B_j-prime|A_j-prime=phi-prime inverse(I-prime<=j)')
inv('deletion','bottom right second definition','older A under B|A')

remaining = [dict(place=x['place'], reading=x['reading'], confidence=x['confidence'], crop=x['crop']) for x in cd if x['status']=='retained']
remaining.append(dict(place='top cancellation boundary', reading='Opening sentence and Soit retained live; intended scope of the subsequent cancellation remains a state-of-page question.', confidence='medium', crop=cp['top']))

notes = [
 dict(id='R3-028-N1', text='The upper abandoned construction uses nonempty intersections of A-circle and B-circle, states a disjoint-union support formula, describes induced equivalence classes as a borne sup, and begins C_k=A cap B. The construction is cancelled; the opening sentence is proposed live from the physical stroke boundary. No claim that C_k is a figure is proved on this page.'),
 dict(id='R3-028-N2', text='A targeted elementary check: for maps f and g on the same set, the fibre of (f,g) at (i,j) is f^{-1}(i) intersect g^{-1}(j). Thus a pair belongs to the image exactly when this intersection is nonempty. This checks only the set-theoretic pattern; identifying the manuscript A-circle strata with those fibres is an additional premise, not established here.'),
 dict(id='R3-028-N3', text='If equivalence relations are ordered by inclusion, intersections of their classes define the meet/intersection of the relations. The literal borne sup in the deleted paragraph is therefore not that order’s join in general. The author’s order convention is not fixed on this sheet, so no textual emendation follows.'),
 dict(id='R3-028-N4', text='The diagrams and lower formula shift between I-prime and J. The image target visibly reads I times J, while the comprehension reads I times I-prime; the pair in that comprehension is (i,j-prime). The box uses j=(i,i-prime) and A_j=A_i cap A-prime_i-prime. These different indices were each reread separately and retained.'),
 dict(id='R3-028-N5', text='The first lower definition has a visible prime on A_i although its preimage uses unprimed phi. The second lower definition has an overwritten capital B|A and a descending j on the left and in the bound. H regularizes both formulae to the boxed construction; the ink does not support that normalization.'),
 dict(id='R3-028-N6', text='The ordinary inverse-image identity (f,g)^{-1}(I_{<=i} times J_{<=j})=f^{-1}(I_{<=i}) intersect g^{-1}(J_{<=j}) follows pointwise, and conditionally explains the intersection in the boxed construction. This does not establish any figure axioms or the surjectivity of the drawn maps.'),
 dict(id='R3-028-N7', text='Manuscript page number 27; no title sheet, date or stated total page count. Two complete diagrams, no separate freehand drawing and no independent marginal or sideways note were found. Only the three supplied scan images and recorded crops were used; no OCR or external mathematical source was used.')
]
who='GPT-6 Astra Pro; effort inherited, not separately exposed; reader R3, scan028'
today=datetime.now(timezone.utc).date().isoformat()
checks=[
 dict(statement_id='R3-028-N2',date=today,who=who,type='targeted proof check',outcome='For every x, (f(x),g(x))=(i,j) iff f(x)=i and g(x)=j. Hence the pair fibre is the intersection and it is nonempty iff the pair is in the image. Conditional identification with the manuscript strata remains unproved.'),
 dict(statement_id='R3-028-N3',date=today,who=who,type='targeted proof check',outcome='Under inclusion order, the relation requiring both equivalences is their set intersection and greatest common lower bound. On a two-point set, take one relation universal and the other equality: class intersections give equality while their join is universal. This checks the conditional order issue only; the author’s possibly reversed convention is not settled.'),
 dict(statement_id='R3-028-N6',date=today,who=who,type='targeted proof check',outcome='Pointwise, the simultaneous pair belongs to the lower rectangle iff each coordinate belongs to its lower set. Therefore the inverse image is the intersection. No figure-closure, topology or surjectivity result was checked.'),
 dict(statement_id='R3-028-N1',date=today,who=who,type='carried as background without fault found',outcome='The intended figure/stratum interpretation and the surjectivity labels are carried as the manuscript’s premises. They were read, not independently proved.')
]

report=dict(
 scan='028',reader='R3',model='GPT-6 Astra Pro (inherited)',effort='inherited; not separately exposed',
 start_utc=(out/'scan028_start.txt').read_text().strip(),end_utc=datetime.now(timezone.utc).isoformat(),
 source_C=str(cpath),source_H=str(base/'working/H/scan028.tex'),
 source_C_doubts=str(base/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_doubts.md'),
 source_C_notes=str(base/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_notes.md'),
 images_viewed=[str(source),str(source.with_name(source.stem+'_a.jpg')),str(source.with_name(source.stem+'_b.jpg'))]+[c['path'] for c in crops],
 image_order='Initial viewing: whole, then a, then b. Then enlarged crops; several crops and the whole page were revisited for the comparison and inventory. The final four crops were re-emitted individually after a multi-image output was truncated.',
 crops=crops,reading_file=str(out/'scan028.tex'),differences=diffs,C_doubts=cd,
 difference_boolean_convention='against_C/against_H compares the proposed reading and meaningful uncertainty/deletion state, not merely macro names. Resolving or broadening a doubt is counted; retained C doubt review rows have against_C false. H editorial prose is recorded as text absent from the manuscript.',
 S_decisions=[dict(scan='028',decision='no applicable row',source=str(base/'source/SP34_CW_156-5_sweep3/readings/156-5_CORRECTIONS.tsv'),evidence='No scan028 correction row found; no S reading adopted for this page.')],
 inventory=inventory,remaining_doubts=remaining,
 notation=[
  dict(place='top and cancelled displays',reading='F,G; A^circ,B^circ; K over I|J',ink='F has two straight arms; circles are small raised open loops; older barred letters are overwritten.'),
  dict(place='cancelled paragraph',reading=r'\unsure{\mathcal R|\mathscr R}_F,\mathcal R_G',ink='Looped script R; the alphabet distinction is marked on its first occurrence.'),
  dict(place='first versus second diagram',reading=r'\mathcal L versus L',ink='Upper L has a lower-left loop; lower L has an angular foot.'),
  dict(place='diagram maps',reading=r'\varphi,\varphi\prime; \unsure{\psi|Y}',ink='Phi has a loop bisected by a descending stem; the left lower label has two arms and a plain descending stroke.'),
  dict(place='diagram edges',reading='isolated slanted inclusion signs in first diagram; headed hooked arrows and one headless line in second',ink='Arrowheads are present on the lower inclusion arrows and projections, absent from the long left vertical line.'),
  dict(place='foot indices',reading="(i,j'), j=(i,i'), A_i', B_j'|A_j', I'_{<=j}",ink='The j strokes descend and bend left. The first definition has a detached high prime; the two lower bounds i and j have visibly different depths.'),
  dict(place='abbreviations',reading='ens.; rel.; d’équi.; sup; surj; ord.; Im',ink='Stops retained where visible; no expansion made in the page text.')
 ],notes_while_reading=notes,check_events=checks,
 legibility='Main prose and large symbols are generally legible after enlargement. The weakest places are overwritten older letters, the inner support bar, the exact script R alphabet, and the overwritten bottom factor and second definition. The cancellation boundary above the defining set is an interpretive state-of-page uncertainty. No reader or root decision files were consulted.',
 verification='Both complete diagrams retained as tikz-cd. Every C unsure occurrence has its own review; every H lexical, symbol, omission, state or diagram discrepancy noticed in the line-by-line comparison is listed. No compilation performed.'
)
(out/'scan028.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(diffs),C_doubts=len(cd),resolved_C_doubts=len(resolved),inventory=len(inventory),remaining_doubts=len(remaining)),ensure_ascii=False))
