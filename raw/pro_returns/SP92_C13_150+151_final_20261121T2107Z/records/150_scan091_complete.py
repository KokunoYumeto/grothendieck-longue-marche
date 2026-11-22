from pathlib import Path
import json
base=Path('/workspace/scratch/d7279cb02214')
rec=base/'SP92_C13_150+151_work/records'
obj=json.loads((rec/'150_scan091.json').read_text())
p=json.loads((base/'reading_packets/150_scan091/packet.json').read_text())
crops={x['crop'].removeprefix('crops/150_scan091_').removesuffix('.png'):x for x in obj['crop_manifest']}
for x in obj['changes']:
 if x['id'] in ('C01','C14'): x['against_C']=True
 if x['id'] in ('C03','C06','C08'): x['consequential']=False
coverage={
476:('editorial-only',[],'C scan metadata 91 is compared with H editorial introduction to the authorial number 42; both witnesses preserve 42. The editorial description is not manuscript prose.'),
477:('editorial-only',[],'H prose de sa main identifies the hand of 42 and is editorial; the number itself is transcribed and separately audited.'),
478:('reading',[],'Cancelled filtration/stratification remains unresolved in doubt D01. Filtration stays first as in both witnesses; C has an alternative and H does not. No first-reading or state change is made.'),
479:('reading',[],'The raised, then cancelled adjective remains ordinaire|indicielle in doubt D02. Crossings prevent a complete letter-level resolution; H gives only the same first reading.'),
480:('reading',['C01'],'The separate live adjective resolves to ordinaire on its crop; C mark M0716 is resolved first, with no inference from the crossed occurrence.'),
481:('reading',['C02'],'The running word deux is clear. H running text has an illegibility marker, although its later editorial note independently quotes the correct phrase.'),
482:('macro-only',[],'H itemize wrapper; no manuscript wording differs.'),
483:('macro-only',[],'Closing item-label bracket from the H itemize syntax; no source bracket.'),
484:('reading',['C04'],'Loc! has an upright exclamation stem and detached dot. This resolves C M0717 to its alternative and rejects H ordinary stop.'),
485:('reading',[],'Final fini/finie remains unresolved in doubt D03 and decision M0718; the final curl cannot be separated from a pen return. H has the same first reading only.'),
486:('reading',['C07'],'The dot after X in the lower addition is a full stop; H semicolon is not supported. The adjoining item wrapper is macro syntax.'),
487:('macro-only',[],'Closing H item-label bracket only.'),
488:('reading',['C09'],'H semicolon after croissante is absent in the ink. The adjacent item bracket is macro syntax.'),
489:('macro-only',[],'Closing H item-label bracket only.'),
490:('macro-only',[],'C display delimiter versus H inline setting of the same intersection/union formula.'),
491:('editorial-only',[],'Closing display/itemize syntax and H editorial note about two versus three conditions and the margin location; actual margin wording is covered in D0492-D0493.'),
492:('reading',['C10'],'The rotated margin crop reads sont; H running margin quotation leaves illegible material. The complete margin reading is logged once.'),
493:('reading',['C10','C11'],'This alignment span joins two real places: the margin has quoted strates and feminine fermées, and the later cancelled phrase now has Posons les conditions first with its uncertainty preserved. H editorial lecture incertaine is excluded.'),
494:('reading',['C13'],'The d-in-Drap-I label belongs to the cancelled operator; C instead puts it live after X_d. Operator identity remains doubt D05, with the same first reading as H.'),
495:('macro-only',[],'The apparent comma is the LaTeX thin-space command in H Drap\\,I; no literal comma is written or introduced.'),
496:('reading',['C13'],'The shifted X_d token reflects the same cancelled-index attachment difference as D0494; it is not a second omitted X_d.'),
497:('reading',['C14'],'Four crossed but individually visible letters resolve to syst. Only the possible full stop swallowed by the strike remains uncertain; doubt D06.'),
498:('reading',['C15','C16'],'Two distinctions: H offers no lexical reading for the cancelled word, for which large remains tentative, and omits the separate live words au sens large entirely.'),
499:('reading',['C17'],'There is one baseline comma after the closing parenthesis, with the raised insertion attached immediately before it. C adds an unsupported comma inside the insertion.'),
500:('reading',['C18'],'The raised words are au dessus with a space, not H normalized hyphen.'),
501:('reading',['C19'],'The joined middle and tall final t give fournit, not H forme.'),
502:('reading',['C20'],'The source has paired raised quotation ticks around résolution, not guillemets.'),
503:('reading',['C22'],'A closed O/n word followed by separate aura gives On aura, rejecting H uncertain Ainsi.'),
504:('reading',['C23'],'Two t stems give literal tt; H expands this to tout.'),
505:('macro-only',[],'C aligned environment records the two display rows; H linearizes the same equality chain.'),
506:('macro-only',[],'Closing aligned wrapper only; both display rows and all math were independently read.'),
507:('reading',['C24'],'The article ends with an e return, giving le rather than H la.'),
508:('reading',['C25'],'The only terminal curve closes (89); no separate comma follows. C comma is removed, agreeing with H.'),
509:('reading',['C26'],'Detached apostrophe and tall t followed by separate p give n\'est pas rather than assez peu.'),
510:('reading',['C27'],'The small o before n and the short final e of remplace give on remplace rather than en remplaçant.'),
511:('macro-only',[],'Superscript/subscript serialization order differs for the same final X_{i_0}^*.'),
512:('macro-only',[],'Other half of the same superscript/subscript order difference. The separate first starred index gains doubt D08 only, without a changed first reading.'),
513:('reading',['C28','C29'],'The last words read en posant, and separate later foliation 90 is omitted by H. These are separate manuscript places and are logged separately.')}
obj['diff_coverage']=[{'diff_id':d['diff_id'],'classification':coverage[int(d['diff_id'][1:])][0],'change_ids':coverage[int(d['diff_id'][1:])][1],'reason':coverage[int(d['diff_id'][1:])][2]} for d in p['differences']]

def rev(item,state,attachment,evidence,crop):
 c=crops[crop]; return {'item':item,'state':state,'attachment':attachment,'evidence':evidence,'crop':c['crop'],'box':c['box']}
obj['deletion_insertion_review']=[
rev('Whole opening Une ... de type I','deleted','One cancelled introductory phrase; it is separate from the live Soient sentence and live definition below.','A continuous cancellation crosses the first phrase; filtration|stratification stays doubtful because parts of the letter bodies are occluded.','heading_cancel'),
rev('Raised ordinaire|indicielle inside the opening cancelled phrase','inserted, then deleted','Placed above the gap after the doubtful noun and before de type I; represented as an inserted, cancelled item inside the whole cancelled phrase.','The small adjective is above the original baseline and has its own crossing stroke as well as the enclosing phrase cancellation. It is not live.','heading_cancel'),
rev('Strat 1 est un recouvrement','inserted and live','Raised above the main line, attaches after the second X_i and before baseline loc! fini(e).','The long curved leader lands before loc; the short independent line directly under recouvrement is its underline.','strat1'),
rev('Strat 1 de X.','inserted and live','Lower/right addition attaches after fini(e); it supplies the actual full stop of Strat 1.','The low curved attachment stroke is distinct from the letters de X and their final stop. Baseline loc! fini(e) is not part of either insertion.','loc_fini'),
rev('Cancelled Posons les conditions|Pour ces conditions','deleted','Standalone cancelled phrase before Pour tout drapeau.','The horizontal stroke crosses the complete phrase; surviving Posons/les shapes favor changing the first reading but do not remove the alternative.','cancelled_conditions'),
rev('Cancelled varinjlim|les and d in Drap I label','deleted','The subscript belongs to the cancelled operator, not as a live appended family index after X_d. The following X_d remains live.','Small letters are centered below the operator and end before the separate baseline X_d. Operator identity and its under-stroke remain doubtful.','cancelled_lim'),
rev('Cancelled syst with doubtful stop','deleted','Between forment un and espace semi-simplicial.','Four letter bodies s-y-s-t survive the heavy strike. A separate stop is not visible; its possible presence within the strike stays locally doubtful.','cancelled_syst'),
rev('Cancelled large','deleted','After espace semi-simplicial and before the separate live au sens large.','The first l/g-bearing word is crossed; the following au sens large has no cancellation and is not included in the deleted span.','large_context'),
rev('Raised au dessus de X','inserted and live','The leader attaches between the closing parenthesis after types and the sole existing baseline comma; then qui fournit continues on that baseline.','The raised words have no leading comma and no hyphen. The leader crosses near the f ascender of fournit without cancelling it.','insertion_fournit'),
rev('Last paragraph raised X_i,','inserted and live','Inserted between les and the original X_d in Mais les X_i, X_d sont ... .','A clear downward V-shaped leader reaches the gap after les. The comma is part of the raised insertion; the baseline X_d is intact.','xi_insertion')]

inventory=[]
def inv(element,kind,position,first,hand='Grothendieck'):
 inventory.append({'sheet_kind':'text','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('Authorial page number','margin note','upper-left, x24-83 y31-85','42')
inv('Cancelled opening phrase','deletion','top, y20-125','Une filtration|stratification ... de type I')
inv('Cancelled adjective added to opening phrase','insertion','raised within top deletion, y20-125','ordinaire|indicielle; added and then cancelled')
inv('Opening assumptions','text','main column, around y130','Soient X un espace, I un ens. ordonné.')
inv('Live definition','text','main column, y145-300','Une stratification ordinaire, de type I, de X, est une application')
inv('Definition mapping','display','main column, y305-380','I to P(X); i tailbar-plus-headless-shaft X_i')
inv('Introduction to conditions','text','main column, y383-447','satisfaisant les deux conditions')
inv('Strat 1 baseline','text','main column, y437-514','les X_i fermés, la famille des X_i ... loc! fini|finie')
inv('First Strat 1 insertion','insertion','above baseline, within y384-535','est un recouvrement; recouvrement underlined')
inv('Second Strat 1 insertion','insertion','below/right baseline, y437-534','de X.')
inv('Strat 2','text','main column, y543-625','i≤j implies X_i subset X_j; i to X_i est croissante')
inv('Strat 3 introduction','text','main column, y625-753','forall i,j in I, on a')
inv('Strat 3 intersection formula','display','same physical baseline as Strat 3, right side, y625-753','X_i cap X_j = union over k in bar i cap bar j of X_k.')
inv('Slanted condition margin note','margin note','left margin, x18-240 y462-795','les X_i sont les double-quoted strates, underlined fermées')
inv('Cancelled pre-flag phrase','deletion','main column, y789-861','Posons les conditions|Pour ces conditions')
inv('Flag introduction','text','main column, around y900','Pour tout drapeau')
inv('Flag display','display','main column, around y975','d=(i_0 < two continuation marks < i_n)')
inv('Definition lead-in','text','main column, around y1060','de I, posons')
inv('Formula 88','display','main column, around y1135','(88) X_d=X_{i_0},')
inv('Semisimplicial construction paragraph','text','main column, y1191-1750','alors ... X_d forment un ... espace semi-simplicial ... au sens large ...')
inv('Cancelled operator and index','deletion','within first construction line, x485-718 y1191-1309','varinjlim|les with d in Drap I below')
inv('Cancelled abbreviation','deletion','first construction line, x1076-1212 y1209-1280','syst; stop doubtful')
inv('Cancelled adjective','deletion','start of next construction line, y1318-1387','large, doubtful')
inv('Added relative-base phrase','insertion','raised near right end, x1206-1649 y1327-1488','au dessus de X')
inv('Resolution and cohomology lead-in','text','main column, y1475-1750','en un sens convenable une double-quoted résolution semi-simpl de X. On aura p.ex. pour tt faisceau abélien F sur X')
inv('Formula 89, two rows','display','main column, y1760-1970','(89) H^*(X,F) left double arrow E_2^{pq}=H^p(...); second row =H^p_ss(...)')
inv('Final paragraph','text','main column, y1973-2271','Mais les ... X_d sont des espaces souvent compliqués, et le dévissage (89) souvent n\'est pas pratique, on remplace ... en posant')
inv('Raised first family in final paragraph','insertion','above final paragraph, x440-707 y1973-2090','X_i,')
inv('Later foliation','margin note','lower-left, x18-84 y2285-2347','90','another, later foliation hand')
obj['inventory']=inventory
obj['notes']='''## Content and source state

The page defines an ordinary stratification of a space X of type an ordered set I. It gives a closed family, a locally finite covering condition, monotonicity, and an intersection expressed as a union over the common lower indices. The source explicitly introduces “les deux conditions” and then labels three items Strat 1, Strat 2 and Strat 3. That discrepancy is retained as an authorial slip, not corrected to trois. H's running illegibility marker is distinguished from its editorial note, which already quotes deux correctly.

For a flag d the page puts X_d=X_{i_0} in (88), describes a semisimplicial space au sens large for strictly increasing maps of standard simplices, inserts that it is above X, and calls it a semisimplicial resolution in a suitable sense. It then writes the two-row cohomology/spectral-sequence expression (89). The final paragraph says these spaces are often complicated, the dévissage is often not practical, and starts replacing them by starred spaces. The sentence ends at en posant and is left incomplete on this page. No text from a following page is supplied.

## Mathematics prompted visual checks, not a proof

The relation signs and both ends of every mapping were checked. The two mappings in the definition and Strat 2 have a left tailbar and a blunt/upturned endpoint with no pointed head, while the adjacent I-to-P arrow and both mappings in (89) have clear heads. Literal headless tailbar shafts are preserved. The typeface difference between C's calligraphic P and H's fraktur P does not establish a different written alphabet: the ink gives the same capital P with a loop and stem, so no reading row is manufactured from the font wrappers.

The full flag formula was read around its zero and its continuation marks: there are two visible continuation marks, not a completed three-dot ellipsis. Formula (88), the entire Strat 3 intersection/union expression with its bars, and all of (89) were read, including 88, 89, the spectral-sequence 2, p/q positions, double left arrow, both mapping heads, ss, brackets and indices. The cancelled operator was checked together with its label and the adjacent live X_d: the d-in-Drap-I label is attached to the cancelled operator, not a second live index on X_d. Its lexical identity remains doubtful. These are transcription checks only; no argument, convergence claim or cohomological identification was proved or used. Accordingly check_events is empty.

The complete last inline math group was compared internally. The first starred X has a detached dot supporting i, but its low bowl, tall stem and right foot resemble the adjacent d. The final i_0 has the ordinary short curved i with detached dot. The first index therefore remains narrowly i|d, without replacing ink from the expected indexing scheme. Adding this uncertainty alone is not a counted reading-change row.

## Revisions, punctuation and unresolved ink

All C insertions and deletions were separately checked for state, bounds and attachment. In Strat 1 the upper and lower curves are insertion leaders, not an underline of loc! fini(e); recouvrement alone has the independent underline. The raised au dessus de X has no hyphen or leading comma. Its leader attaches just before the sole baseline comma after the parenthesis. That leader does not cancel fournit. The lower raised X_i, attaches after les and before X_d. Crossed text is never made live to repair the prose.

The live ordinaire and loc! are resolved on their crops. The crossed initial noun and its crossed raised adjective remain doubtful. Posons les conditions is favored over Pour ces conditions inside the cancellation, but the alternative remains. The letters syst are individually visible; only a possible stop hidden in its strike stays doubtful. The cancelled large remains tentative, while the following live au sens large is clear. The adjective fini|finie remains undecided because the last curl may be a final e or a pen return.

The page uses paired raised quotation ticks around strates and résolution. It writes tt, p.ex. and semi-simpl without expansion. A new right-edge crop resolved the initially truncated abbreviation ending: the final l has a connected foot and no separate stop before the paper edge, so both witnesses' supplied stop is removed. Reopening the existing lower dévissage crop likewise showed only the closing parenthesis after 89, not a separate comma; H agrees there. Semicolons supplied by H after Strat 1 and Strat 2 are not carried over. The explicit stop after the inserted de X. and the separate comma after pratique remain.

## Sheet and numbering

This is a handwritten text sheet, with no separate title or date and no genuine diagram or drawing. The dark upper-left 42 is authorial numbering. The thin grey lower-left 90 is later foliation in another hand and is represented as a margin note. The source image is upright; show-through and background marks are not transcribed. The count of 25 principal baselines excludes raised insertions, the oblique margin note and the two separate numbers, all of which are included in the inventory and blind boxes.
'''
obj['notation']=[
{'sign':r'i\mathrel{\mapstochar\relbar\joinrel\relbar}X_i','reading':'Mapping written with a left tailbar and long headless shaft.','evidence':'Definition display: tailbar and blunt/upturned endpoint, unlike its clearly pointed neighboring I-to-P arrow.'},
{'sign':r'i\mathrel{\mapstochar\relbar}X_i','reading':'The same headless tailbar mapping form with a shorter shaft.','evidence':'Strat 2 repeats the left tailbar and lacks a pointed right head; the two mappings in (89) visibly do have heads.'},
{'sign':r'\cdotp\cdotp','reading':'Two written continuation marks.','evidence':'Flag d=(i_0<...<i_n): two separated dark marks only, second slightly elongated.'},
{'sign':'loc!','reading':'Written local-finiteness abbreviation ending in an exclamation sign.','evidence':'An upright plus detached lower dot, not a superscript t or a simple abbreviation stop.'},
{'sign':r'\bar i\cap\bar j','reading':'Intersection of the two lower-index sets in the union subscript.','evidence':'Both short bars are separate over the dotted/descending letter bodies in Strat 3; their placement was read with the complete formula.'},
{'sign':r'X_{\unsure{i|d}}^*','reading':'First starred-space index remains i versus d.','evidence':'Detached dot favors i, but full left bowl and right foot resemble adjacent d; no certainty based on mathematical expectation.'}]
obj['hand_log']=[
{'habit':'Compressed prose can reduce several vowels to a long low stroke while leaving decisive ascenders, descenders and dots.','places':'150_scan091: fournit; On aura; le dévissage; n\'est pas; on remplace; en posant.','scope':'Observed at these six places; not a rule replacing inspection of other words.','witness_errors':'H reads forme, Ainsi, la, assez peu, en remplaçant and on pourrait respectively.'},
{'habit':'A final small curl can be either e or a terminal pen return.','places':'150_scan091: fini|finie in Strat 1.','scope':'Local unresolved case; no blanket identification of terminal curls as e.','witness_errors':'C retains both possibilities; H chooses fini. The crop does not decide.'},
{'habit':'Curved insertion leaders may resemble underlining or punctuation and may cross letter ascenders.','places':'150_scan091: both Strat 1 additions; au dessus de X; raised X_i,.','scope':'All four live additions checked separately for attachment.','witness_errors':'C underlines loc! fini(e) from enclosing leaders and supplies an extra insertion comma; H incorporates baseline loc/fini into the upper insertion.'},
{'habit':'Headless tailbar shafts coexist with pointed mapping arrows on one page.','places':'150_scan091: definition mapping and Strat 2 versus both mapsto signs in (89).','scope':'Only the first two lack clear heads; no global deletion of heads from the other arrows.','witness_errors':'Both C and H normalize the first two to headed mapsto signs.'},
{'habit':'Ordinary mathematical i is often a short low curve with detached dot, whereas d has a tall stem, left bowl and right foot.','places':'150_scan091: lower final i_0 and adjacent X_d^*; first starred-space index.','scope':'Local contrast is clear, but the first starred index combines the dot and d-like bowl and remains unresolved.','witness_errors':'Both witnesses give the first starred index as i without marking its conflicting body shape.'},
{'habit':'Crossing strokes can hide joins while leaving independently legible upper and lower letter bodies.','places':'150_scan091: cancelled syst, initial headings, cancelled conditions phrase, cancelled large.','scope':'Only syst letters are resolved in full; the other cancellations keep their bounded doubts.','witness_errors':'C syst.|objet narrows to syst with punctuation doubt; other cancelled C choices are not assumed correct or discarded.'},
{'habit':'Paired raised pen ticks are his double quotation marks on this leaf.','places':'150_scan091: strates in margin; résolution in main prose.','scope':'Confirmed at both quoted words on this page.','witness_errors':'H uses guillemets around résolution and leaves the quoted margin word unread.'},
{'habit':'Connected feet and pen returns are not independent stops or commas.','places':'150_scan091: semi-simpl at right edge; closing (89) in final paragraph; end of croissante.','scope':'These three endings were checked separately; genuine de X. stop and pratique comma remain.','witness_errors':'Both witnesses supply a semi-simpl stop; C supplies a comma after (89); H supplies a croissante semicolon.'},
{'habit':'A thin grey later foliation hand differs from the dark authorial numbering.','places':'150_scan091: lower-left 90 versus upper-left 42.','scope':'Both complete two-digit groups independently inspected.','witness_errors':'H omits later 90; it is not treated as Grothendieck\'s page number.'}]
obj['abbreviations']=[{'form':'ens.','expansion':'ensemble'},{'form':'loc!','expansion':'localement (written loc! retained)'},{'form':'i.e.','expansion':'id est'},{'form':'syst [stop uncertain, cancelled]','expansion':'système'},{'form':'semi-simpl','expansion':'semi-simpliciale'},{'form':'p.ex.','expansion':'par exemple'},{'form':'tt','expansion':'tout'},{'form':'Drap','expansion':'drapeaux'}]

def doubt(did,place,reading,alternatives,confidence,reason,crop,C,H):
 c=crops[crop]; return {'id':did,'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason,'crop':c['crop'],'box':c['box'],'C':C,'H':H}
obj['doubts']=[
doubt('D01','Cancelled opening noun',r'\deleted{\unsure{filtration|stratification}}',['filtration','stratification'],'low','Filtration remains first, but the dense strike obscures the lower bodies and joins. The condition for resolving every letter of cancelled text is not met.','heading_cancel',r'\unsure{filtration|stratification}','filtration'),
doubt('D02','Raised and cancelled opening adjective',r'\inserted{\deleted{\unsure{ordinaire|indicielle}}}',['ordinaire','indicielle'],'low','Ordinaire is favored by the initial tall d-like stroke, but this small word is independently crossed and several letter bodies are obscured. The clear live word below does not settle this separate occurrence.','heading_cancel',r'\inserted{\deleted{\unsure{ordinaire|indicielle}}}',r'\add{\struck{ordinaire}}'),
doubt('D03','Strat 1 adjective',r'\unsure{fini|finie}',['fini','finie'],'low','The dotted final i is clear; a low trailing curl can be either a separate final e or the terminal return of i. Enclosing insertion leaders do not resolve it. Decision M0718 remains undecided.','loc_fini',r'\unsure{fini|finie}','fini'),
doubt('D04','Cancelled pre-flag phrase',r'\deleted{\unsure{Posons les conditions|Pour ces conditions}}',['Posons les conditions','Pour ces conditions'],'medium','Surviving round bodies favor Posons and a tall l favors les, so the first reading changes, but the crossing hides parts of the joined letters and conditions. Change C11 records only the favored first reading.','cancelled_conditions',r'\deleted{\unsure{Pour ces conditions|Posons les conditions}}',r'\struck{Posons les conditions}'),
doubt('D05','Cancelled operator after alors',r'\deleted{$\unsure{\varinjlim|\text{les}}_{d\in\mathrm{Drap}I}$}',[r'\varinjlim',r'\text{les}'],'low','Looped/tall remnants favor a limit abbreviation, but the strike obscures the middle and the possible lower arrow. The attached index placement is clear and separately changed in C13; lexical/operator identity remains unresolved.','cancelled_lim',r'\deleted{\unsure{$\varinjlim$|les}}',r'\struck{$\varinjlim_{d\in\mathrm{Drap}\,I}$}'),
doubt('D06','Stop after cancelled syst',r'\deleted{syst\unsure{.|}}',['full stop swallowed by strike','no full stop'],'low','The letters s-y-s-t are individually readable. No separate stop is visible, but the heavy horizontal strike passes through the position where one could have been written; uncertainty is limited to punctuation.','cancelled_syst',r'\deleted{\unsure{syst.|objet}}',r'\struck{syst.}'),
doubt('D07','Cancelled large after semi-simplicial',r'\deleted{\unsure{large}}',['large','unresolved crossed letters'],'low','The tall l and g descender support large, while the crossed a/r/e do not meet the all-letters-plain threshold. The following separate live au sens large is fully readable.','large_context',r'\deleted{\unsure{large}}',r'\struck{\ill{}}'),
doubt('D08','First starred-space index in final inline math',r'X_{\unsure{i|d}}^*',['i','d'],'low','A detached dot supports i, but the left bowl, tall stem and right foot resemble the adjacent d, unlike the short dotted i in the final i_0. The whole group was read and remains unresolved; adding this doubt alone does not count as a change.','lower_math',r'X_i^*',r'X_i^{*}')]
boxes=[]
def box(kind,coords,reading):
 boxes.append({'box':f'B{len(boxes)+1:02d}','kind':kind,'x0':coords[0],'y0':coords[1],'x1':coords[2],'y1':coords[3],'reading':reading})
box('authorial handwritten number',[24,31,83,85],r'\mspage{42}')
box('cancelled opening phrase and raised cancelled insertion; two C doubts',[230,20,1010,125],r'\deleted{Une \unsure{filtration|stratification} \inserted{\deleted{\unsure{ordinaire|indicielle}}} de type $I$}')
box('complete live definition; resolved C adjective',[245,145,1665,300],r'Une \uline{stratification ordinaire}, de type $I$, de $X$, est une application')
box('whole definition mapping; literal arrow geometry',[555,305,1395,380],r'I\longrightarrow\mathcal P(X)\qquad i\mathrel{\mapstochar\relbar\joinrel\relbar}X_i')
box('deux; Strat 1 number; both insertions and C adjective/exclamation doubts',[240,383,1655,535],r'satisfaisant les deux conditions'+'\n\n'+r'(Strat 1) les $X_i$ fermés, la famille des $X_i$ \inserted{est un \uline{recouvrement}} loc! \unsure{fini|finie}\inserted{ de $X$.}')
box('Strat 2 number and whole mapping/condition; punctuation',[270,543,1656,625],r'(Strat 2) $i\leq j\Longrightarrow X_i\subset X_j$ i.e. $i\mathrel{\mapstochar\relbar}X_i$ est croissante')
box('Strat 3 number and complete formula including barred indices',[271,625,1595,753],r'(Strat 3) $\forall i,j\in I$, on a'+'\n'+r'\[X_i\cap X_j=\bigcup_{k\in\bar i\cap\bar j}X_k.\]')
box('complete slanted margin note',[18,462,240,795],r'\margin{les $X_i$ sont les ``strates\'\' \uline{fermées}}'.replace("\\'", "'"))
box('cancelled phrase; changed first reading with uncertainty',[257,789,851,861],r'\deleted{\unsure{Posons les conditions|Pour ces conditions}}')
box('whole flag and formula 88; continuation marks, all zeros and number 88',[268,858,1054,1161],r'Pour tout drapeau'+'\n'+r'\[d=(i_0<\cdotp\cdotp<i_n)\]'+'\n'+r'de $I$, posons'+'\n'+r'\[(88)\qquad X_d=X_{i_0},\]')
box('cancelled operator whole formula and index attachment; cancelled syst',[270,1180,1665,1317],r'alors \deleted{$\unsure{\varinjlim|\text{les}}_{d\in\mathrm{Drap}I}$} $X_d$ forment un \deleted{syst\unsure{.|}} espace semi-simplicial')
box('cancelled large; live omitted qualification; raised insertion and comma; fournit',[285,1318,1665,1490],r'\deleted{\unsure{large}} au sens large (pour des applications strictement croissantes sur les simplexes types)\inserted{au dessus de $X$}, qui fournit')
box('quotation ticks and abbreviation ending at right edge',[285,1475,1670,1567],r'en un sens convenable une ``résolution\'\' semi-simpl'.replace("\\'", "'"))
box('On aura; p.ex.; tt and complete cohomology lead-in',[285,1573,1665,1750],r'de $X$. On aura p.ex. pour tt faisceau abélien $F$ sur $X$')
box('whole formula 89 including E subscript 2 and both headed mappings',[280,1760,1666,1970],r'\['+'\n'+r'(89)\qquad\begin{aligned}'+'\n'+r'H^*(X,F)\Longleftarrow E_2^{pq}&=H^p(I,i\mapsto H^q(X_i,F))\\'+'\n'+r'&=H^p_{ss}(\mathrm{Drap}(I),d\mapsto H^q(X_d,F))'+'\n'+r'\end{aligned}'+'\n'+r'\]')
box('last paragraph first line and raised X_i insertion',[280,1973,1665,2096],r'Mais les \inserted{$X_i$,} $X_d$ sont des espaces souvent compliqués,')
box('last two lines: le/n est pas/on remplace/en posant; 89 and whole final math with doubtful index and zero',[298,2080,1665,2271],r"et le dévissage (89) souvent n'est pas pratique, on remplace par les $X_{\unsure{i|d}}^*$, $X_d^*=X_{i_0}^*$, en posant")
box('later handwritten foliation number',[18,2285,84,2347],r'\margin{90}')
obj['second_boxes']=boxes
obj['status']='complete candidate; awaiting root finalization and independent blind reread'
(rec/'150_scan091.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('Complete JSON:',len(obj['changes']),'changes;',len(obj['diff_coverage']),'diffs;',len(obj['decisions']),'marks;',len(obj['second_boxes']),'blind boxes;',len(obj['inventory']),'inventory items;',len(obj['doubts']),'doubts')
