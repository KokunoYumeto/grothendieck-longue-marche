from pathlib import Path
import json
base=Path('/workspace/scratch/ddf8babdc42e')
manifest=json.loads((base/'out/review/scan004_crop_manifest.json').read_text())
boxes={x['name']:x['box'] for x in manifest['crops']}
changes=[]
def add(n,place,C,H,final,shows,conf,kind,crop,ac,ah,mh=False,con=True):
    changes.append(dict(id=f'S004-{n:03d}',place=place,C=C,H=H,final=final,scan_shows=shows,confidence=conf,kind=kind,crop=f'out/crops/scan004_{crop}.png',box=boxes[crop],against_C=ac,against_H=ah,marked_in_H=mh,consequential=con))
add(1,'opening before (et','(et','» (et','(et','The first dark stroke is one opening parenthesis, followed directly by et. No preceding guillemet is present.','high','spurious punctuation in H','opening_start',False,True,False,False)
add(2,'opening line: resté','resté','tenté','resté','Initial r has a short entrance and low joining stroke; the medial low run and tall t precede the accent. There is no initial crossed t of tenté.','high','word','reste_muet',False,True,True)
add(3,'opening line: muet','muet','uncertain maintenant','muet','The word is a short sequence of low m/u strokes and final tall crossed t; it does not contain the repeated ascenders and much longer sequence of maintenant.','high','word','reste_muet',False,True,True)
add(4,'reference after précédente','unsure GF|CF','GF','GF','The first capital has a lower-right terminal that turns downward, matching G elsewhere on this leaf, not the open C candidate.','high','resolved C doubt','reference',True,False,False)
add(5,'reference numeral VI','VI with upper and lower bars','VI without bars','VI with upper and lower bars','A continuous horizontal stroke spans the numeral above and a separate stroke lies below it. The numeral has the two arms of V and a separate upright I.','high','numeral decoration','reference',False,True,False,False)
add(6,'comme figure','comme figure','comme une figure','comme figure','The low strokes completing comme end before an empty gap and the tall initial f of figure. There is no intervening word une.','high','word omission/addition','comme_figure',False,True,False)
add(7,'symbol after lieux; repeated in the two Fig expressions','unsure L|mathcal L, later L','mathcal L','unsure L|mathcal L, later L','A rising oblique stem joins a looped foot and horizontal baseline. This does not settle plain italic versus calligraphic L; the small forms in Fig have the same structure. Retain the first-occurrence doubt.','low','alphabet doubt retained','lieux_deleted',False,True,False)
add(8,'struck word after L','deleted unsure ou|de','struck ce','deleted unsure ou|de|ce','A sloping cancellation crosses the word. One small loop survives above the stroke; the remaining low ink is fused with the cancellation. No candidate can be read letter by letter. H’s ce remains an admissible additional candidate, not a resolution.','low','struck word doubt retained','lieux_deleted',True,True,False)
add(9,'comma after L in H','no separate comma','comma after L','no separate comma','The diagonal stroke below and to the right of L is continuous with the cancellation of the following word. No distinct dark comma separates L from that crossed material.','medium','punctuation','lieux_deleted',False,True,False,False)
add(10,'parenthetical prose: cela','cela','ceci','cela','The word ends with a looped l and a low terminal run. There is no dot for a terminal i; its shape agrees with cela, not ceci.','high','word','cela_quon_a',False,True,False)
add(11,'parenthetical prose: qu’on a','qu’on a','que c’est','qu’on a','After the q and joining low strokes there is an apostrophe and short n, then a separate small a. No crossed t or c’est sequence is written.','high','words','cela_quon_a',False,True,False)
add(12,'after ensembliste)','),',') without comma','),','A separate comma lies below the closing parenthesis at the right edge.','high','punctuation','ensembliste_close',False,True,False,False)
add(13,'name of the multiombre expression','mulomb(F)','multomb(F)','mulomb(F)','The sequence is m-u-looped l-o-m-b. There is no t stem or crossbar between the l and o.','high','notation word','mulomb',False,True,False)
add(14,'underlined heading after Données','deleted unsure pré; unsure premières','préliminaires','C’s doubtful heading encoding provisionally retained','The visible terminal sequence is mières; préliminaires is not supported by the length or strokes. The central scribble intersects a tall stroke within a continuous word. The crop does not warrant resolving C’s cancelled pré or endorsing its exact scope as a separate prefixed word. See doubt and deletion audit.','low','heading with unresolved overwrite','heading',False,True,False)
add(15,'alphabet of ensemble-of-figures symbol','unsure mathscr F|mathcal F; later mathscr F','mathfrak F','unsure mathscr F|mathcal F; later mathscr F','The defining F has a long swash and looped upper stroke, with a curling lower stem; it is a handwritten script form rather than a plainly angular Gothic capital. Script versus calligraphic typesetting remains doubtful. The smaller F below repeats the curling stem.','medium','alphabet','figure_alphabet',False,True,False)
add(16,'inclusion relation label: rellation','unsure rellation|relation','relation','unsure rellation|relation','There is a crowded group of repeated tall loops after re. The crop does not cleanly separate an extra l from the following a, so the original spelling doubt is retained.','low','word doubt retained','relation',False,True,False,False)
add(17,'inclusion relation label: de/des','unsure de|des','des','unsure de|des','The d loop is clear; the final low horizontal run could include s or be the e’s extended terminal. Grammar is not used to settle the ending.','low','word doubt retained','relation',False,True,False,False)
add(18,'end of inclusion label','figures with no comma','figures,','figures with no comma','The terminal s ends in a descending flourish; no separate comma follows it before the lower formula begins.','high','punctuation','relation',False,True,False,False)
add(19,'F sous figure de G','sous figure','sous-figure','sous figure','The space between the final low stroke of sous and the tall f is blank; no hyphen is written.','high','word joining','inclusion_formula',False,True,False,False)
add(20,'end of raffinement label','raffinement with no comma','raffinement,','raffinement with no comma','The last t’s stroke closes the label. The surrounding blank area contains no comma.','high','punctuation','raffinement_formula',False,True,False,False)
add(21,'second equivalence label','def','déf','def','Above the second double arrow, d-e-f form one connected label; there is no separate accent stroke above e.','high','accent','raffinement_formula',False,True,False,False)
add(22,'At 0 label','At underlined, 0 not underlined','At 0 all emphasized','At underlined, 0 not underlined','The heavy underline stops below At, to the left of the separate zero.','high','underline extent','axiom',False,True,False,False)
add(23,'slanted note by At 0','NB. Ce sera aussi contenu dans At 4 plus bas','NB. Ce uncertain serait ill. dans At 4 plus bas','NB. Ce sera aussi contenu dans At 4 plus bas','After rotation, sera has no terminal t, the following short word has the two s strokes and dotted i of aussi, and the next baseline reads contenu dans. At alone is underlined before 4.','high','marginal words','margin_at4',False,True,True)
add(24,'axiome sentence','je ne l’avais pas inclus','je ne uncertain le mets pas uncertain inclus','je ne l’avais pas inclus','A looped l, apostrophe, low av run, and dotted i followed by s precede pas. The following line begins inclus with its dotted initial i and tall l. No le mets sequence is present.','high','words','axiome',False,True,True)
add(25,'row (a): quotes and four underlined terms','underlined figure, engendrée, réunion, somme; paired upper quotes','ununderlined figure and quoted terms in guillemets','underlined figure, engendrée, réunion, somme; paired upper quotes','Each quotation mark is a pair of short upper strokes. Separate underlines lie below figure, engendrée, réunion, and somme. They are not guillemet chevrons.','high','quotation shape and underlining','a_quotes',False,True,False,False)
add(26,'end of row (a)','no semicolon after ll','semicolon after the added phrase assigned to (a)','no semicolon after ll','The line ends with two less-than strokes and blank space; no semicolon is written. The separately added phrase belongs to the next row by its connector.','high','punctuation','a_exists',False,True,False,False)
add(27,'ou Inf pour ≤ insertion','inserted after intersection in (b)','added to end of (a), placement noted uncertain','inserted after intersection in (b)','The addition is written above row (b). Its long lower bracket curves downward at the left end and terminates directly after intersection, before the dash and existe. It does not connect to the final ll of (a).','high','insertion attachment','b_text',False,True,True)
add(28,'heading of first left marginal note','deleted unsure Question; inserted NB.','NB in main text; an editorial note mentions a possibly struck Question','deleted unsure Question; inserted NB.','The long horizontal strike crosses the baseline word from its initial Q to the end; NB. is above it. The colon at the right survives outside the cancellation. Not every letter beneath the line is plain, so Question remains doubtful.','high','deletion and insertion state','margin_question',False,True,True)
add(29,'punctuation after added NB in first left note','NB. :','NB :','NB. :','A separate small period stands immediately to the right of the B, above the baseline colon that follows the struck heading.','high','punctuation','margin_question',False,True,False,False)
add(30,'first left note: tjrs','tjrs','toujours','tjrs','The compact sequence contains the tall t/j strokes and brief rs ending, with no written ou/ou sequence.','high','abbreviation retained','margin_question',False,True,False,False)
add(31,'first left note: néc.','néc.','nécessairement','néc.','The word is a short three-letter group followed by a period, rather than the long expanded form.','high','abbreviation retained','margin_question',False,True,False,False)
add(32,'row (b), whole defining formula','Inf^≤(F, unsure c|G)','Inf^≤(F,G)','Inf^≤(F, unsure c|G)','The second argument is a small open bowl with a short low terminal, substantially smaller than F. It may be c or the reduced C-shaped G used elsewhere; the crop does not securely settle case/letter. Both parentheses and the raised ≤ are present.','low','whole-formula doubt retained','b_formula',False,True,False)
add(33,'row (b), before existe','— existe','(existe','— existe','A short independent horizontal dash precedes existe. The larger curved line to its left belongs to the insertion bracket whose upper segment runs beneath ou Inf pour ≤.','high','connector versus punctuation','b_text',False,True,True)
add(34,'row (b), abbreviation before pour familles','overlined m','expanded même','overlined m','One low m has a distinct short horizontal bar above it. No full word même is written. The ambiguous opening stroke immediately before it is retained separately as C’s doubt.','high','abbreviation retained','b_text',False,True,True,False)
add(35,'row (b), familles','unsure familles','familles inside uncertain span','familles','The tall initial f, low a/m strokes, two ascenders for ll, and the final es run are visible. This word is readable on the crop.','high','resolved C doubt','b_text',True,False,True,False)
add(36,'row (b), infinie','infinie','infinies','infinie','The word ends with a small e; no separate s or extended s terminal follows before the next opening parenthesis. Retain the author’s singular ending.','high','ending','b_text',False,True,True,False)
add(37,'row (b), non vide','non vide','non vides','non vide','After the final e of vide there are immediately two closing parentheses. There is no s.','high','ending','b_text',False,True,True,False)
add(38,'row (b), en = temps','en = unsure temps|tps','uncertain en outre','en = temps','The two parallel strokes are an equals sign. The following word has t, a low joining em run, descending p and terminal s. It is not outre; the low em run supports temps rather than tps.','medium','words and resolved C doubt','b_text',True,True,True)
add(39,'row (b), F∨C/G','F∨unsure C|G','F∨G','F∨unsure C|G','The final capital is an open C-shaped curve with no clearly separate inward G bar. G elsewhere can approach this shape, so the doubt remains and the written C-shaped form stays first. The whole formula was read.','low','whole-formula doubt retained','b_text',False,True,False)
add(40,'row (b), final punctuation','period after ll','semicolon after ll','period after ll','One dark round dot follows the two less-than strokes. There is no lower comma stroke.','high','punctuation','b_text',False,True,False,False)
add(41,'last word of bottom-left marginal note','unsure méchisé|mechisé|quoted mechisé','uncertain rectiligne','unsure mechisé|méchisé','The short word begins with a low m-shaped run and contains a tall h-like stroke, dotted i, and a final acute-like stroke. No leading r or rectiligne sequence is visible. There are no paired quotation strokes enclosing it. The exact word and initial accent remain doubtful.','low','marginal word doubt retained','margin_existe',True,True,True)
add(42,'circled row labels','circled a, b, unsure c, unsure d','parenthesized (a) to (d), editorially uncertain','circled a, b, unsure c, unsure d','Each label is enclosed by a single continuous oval. The first a and second b are readable; the third and fourth inner forms are cramped and remain doubtful. Parentheses do not reproduce the enclosing strokes.','high','label form','a_formula',False,True,True,False)
add(43,'row (c), second argument of Inf','Inf^ll(F,c)','Inf^ll(F,G)','Inf^ll(F,c)','The small open c-shaped second argument has no visible inward G stroke. It matches the preferred c candidate of the preceding Inf formula; the recurring c/G uncertainty is recorded at that first occurrence and in notation.','medium','formula letter','c_formula',False,True,False)
add(44,'row (c), multiplication-like dot','F low dot G','F centered dot G','F low dot G','The dark dot lies low, near the lower ends of the capitals, rather than midway up their stems. Preserve the low-dot placement.','high','sign placement','c_formula',False,True,False,False)
add(45,'row (c), intersection fine typography','intersection and fine both underlined; paired quotes','only fine emphasized; guillemets','intersection and fine both underlined; paired quotes, closing quotes doubtful','Separate horizontal underlines stand below both words. The opening mark is two upper strokes. The alleged closing pair is not cleanly separable from neighboring strokes and is left newly doubtful in the proposed text.','medium','underlining and quotation shape','c_text',False,True,False,False)
add(46,'short cancellation under row (c)','deleted unsure G|CG','omitted in text; note says a short word is crossed out','deleted unsure G|CG','Several horizontal/oblique cancelling strokes cross a compact group. Some curved portions survive, but they do not expose every letter. C’s deleted-text doubt is retained without resolution.','low','deleted material','deleted_short',False,True,True)
add(47,'row (d), script F in subscript and prose','mathscr F','mathfrak F','mathscr F (first-occurrence script/calligraphic doubt retained)','The small F has the same curved lower hook as the defining script F, rather than a plainly angular Gothic construction. Both the subscript and the prose occurrence were checked.','medium','alphabet','d_formula',False,True,False)
add(48,'row (d), parentheses and final punctuation','(pour ≤ et pour ll), no final period','pour ≤ et pour ll, final period','(pour ≤ et pour ll), no final period','The rightmost mark is a closing parenthesis. The corresponding opening curve precedes pour. No following period is visible. The underline is confined to et.','high','punctuation','d_text',False,True,False,False)

# Every unresolved C doubt is explicitly represented, including those in deleted material.
doubts=[
 dict(place='lieux L, repeated Fig(L)',reading='L',alternatives=['mathcal L'],confidence='low',reason='The looped foot is compatible with either italic or calligraphic L. Crop scan004_lieux_deleted.png; repeated forms were checked in both left notes. First-occurrence C doubt retained.'),
 dict(place='struck word after L',reading='ou',alternatives=['de','ce'],confidence='low',reason='Only one small loop and fused low strokes survive the strike. Not every letter is plain; preserve C’s doubt and admit H’s ce without adopting it.'),
 dict(place='heading: cancelled material and its scope',reading='C: deleted pré before premières, provisional only',alternatives=['a shorter cancelled stroke/group inside the word, possibly l or li'],confidence='low',reason='The dark crossing is central in a continuous word. It does not plainly cancel a separate initial pré. C’s doubtful encoding is preserved for adjudication, not certified. Crop scan004_heading.png.'),
 dict(place='heading: live word',reading='premières',alternatives=['prémières'],confidence='low',reason='The terminal mières is visible; the overwritten central group obscures the exact initial sequence and whether an apparent upper stroke is an accent. C’s live-word doubt remains.'),
 dict(place='defining ensemble-of-figures symbol',reading='mathscr F',alternatives=['mathcal F'],confidence='medium',reason='A looped script F is visible; exact script/calligraphic font mapping is not resolved. The source does not have a plainly angular mathfrak form. First occurrence remains marked.'),
 dict(place='inclusion label spelling',reading='rellation',alternatives=['relation'],confidence='low',reason='Repeated tall loops after re cannot be safely segmented from the a on the crop. No spelling normalization.'),
 dict(place='inclusion label ending before figures',reading='de',alternatives=['des'],confidence='low',reason='The final horizontal run could contain s or be an extended e terminal. The grammar does not decide.'),
 dict(place='label of first equivalence, whole F≤G iff F sous figure de G formula',reading='déf',alternatives=['def'],confidence='low',reason='The cramped label is entangled with the descender/nearby line above. No safely isolated accent stroke decides it; the whole formula was cropped and read.'),
 dict(place='row (a), mark following existe',reading=')',alternatives=['}'],confidence='low',reason='The mark has a curled or crossed upper lobe and lower right-parenthesis curve. It may be a malformed or overwritten parenthesis or a brace. C doubt retained.'),
 dict(place='struck heading of first left marginal note',reading='Question',alternatives=[],confidence='low',reason='The initial Q and some low joins survive, but the thick horizontal stroke obscures interior letters. The rule for doubtful deleted words forbids removing the doubt.'),
 dict(place='row (b), Inf^≤(F,c/G), and recurring second argument in row (c)',reading='c',alternatives=['G'],confidence='low',reason='Small open curve, with no secure inward bar. G on this page can have a C-like body; exact case/letter is not decided. First recurrence in (b) remains marked; (c) uses preferred c.'),
 dict(place='row (b), stroke before overlined m',reading='(',alternatives=['et ('],confidence='low',reason='The tall curved stroke has a crossed or hooked lower end. It could be only a parenthesis or incorporate a compressed et. Retain C doubt.'),
 dict(place='row (b), F∨C/G',reading='C',alternatives=['G'],confidence='low',reason='The large final letter is C-shaped without a clear inward bar; other G forms can approach this outline. Whole formula read on scan004_b_text.png.'),
 dict(place='bottom-left marginal word',reading='mechisé',alternatives=['méchisé'],confidence='low',reason='m-like initial, h-like ascender, dotted i and final acute visible; exact word is uncertain. No paired quotation strokes. H rectiligne is not supported.'),
 dict(place='row (c) circled label',reading='c',alternatives=[],confidence='low',reason='The cramped inner strokes touch the surrounding circle, and the shape is not confidently separable. Retain C doubt.'),
 dict(place='short struck group between (c) and (d)',reading='G',alternatives=['CG'],confidence='low',reason='Crossing strokes obscure the group. Some ink could suggest an additional first character, but not every letter is plain; C doubt remains.'),
 dict(place='row (d) circled label',reading='d',alternatives=[],confidence='low',reason='Inner loop/stem are crowded against the left side of the enclosing circle. Retain C doubt.'),
 dict(place='row (c), closing paired quotation mark after fine',reading="''",alternatives=['no closing mark'],confidence='low',reason='The opening pair is clear; the alleged closing pair is not securely separable from nearby ink in the crop. This is a new uncertainty only; no unseen closing mark is asserted as certain.'),
]

inventory=[
 dict(element='manuscript page number',kind='handwritten number',position='top center [790,22,842,80]',first_words_or_objects='3'),
 dict(element='opening continuation',kind='handwritten prose, seven lines',position='upper block [240,83,1662,702]',first_words_or_objects='(et je suis resté muet'),
 dict(element='heading',kind='underlined handwritten heading with overwrite',position='[348,728,892,831]',first_words_or_objects='Données premières, doubtful correction'),
 dict(element='primitive data',kind='five handwritten lines grouped by left brace',position='[550,833,1650,1215]',first_words_or_objects='script F ensemble de figures; ≤; ll'),
 dict(element='axiom',kind='display with left label, preceded by avec',position='[272,1232,1127,1361]',first_words_or_objects='At 0, F≤G ⇒ F ll G'),
 dict(element='At 4 note',kind='slanted handwritten margin note',position='left [22,1267,278,1530]',first_words_or_objects='NB. Ce sera aussi contenu'),
 dict(element='axiom explanation',kind='two handwritten prose lines',position='[277,1353,1616,1553]',first_words_or_objects='— axiome si évident'),
 dict(element='operation (a)',kind='two-column definition row',position='[377,1515,1659,1815]',first_words_or_objects='circled a; F∨G ou F∪G; figure engendrée'),
 dict(element='first lower left note',kind='five baseline lines with one inserted heading line and deletion',position='[22,1689,612,1911]',first_words_or_objects='struck Question; inserted NB. : Si (F,G)'),
 dict(element='tilde identity note',kind='handwritten marginal formula',position='[24,1903,392,2004]',first_words_or_objects='NB tilde(F cap G)=tilde F cap tilde G'),
 dict(element='operation (b)',kind='two-column definition row with two formula lines and five prose lines',position='[382,1879,1659,2105]',first_words_or_objects='circled b; F wedge G ou F cap G'),
 dict(element='addition to operation (b)',kind='one inserted line with bent connector',position='[1300,1795,1659,1910]',first_words_or_objects='ou Inf pour ≤'),
 dict(element='bottom-left existence note',kind='three handwritten marginal lines',position='[21,2090,463,2252]',first_words_or_objects='NB Existe dans le cas ensembliste'),
 dict(element='operation (c)',kind='two-column definition row',position='[380,2086,1650,2221]',first_words_or_objects='circled doubtful c; F low-dot G; figure intersection fine'),
 dict(element='cancelled short group',kind='isolated deletion',position='[477,2168,706,2259]',first_words_or_objects='doubtful G|CG'),
 dict(element='operation (d)',kind='two-column definition row',position='[366,2209,1650,2343]',first_words_or_objects='circled doubtful d; empty figure with script F subscript'),
]
notation=[
 dict(form='GF, barred VI',reading='GF VI reference',place='upper paragraph, line 2 [1010,157,1233,241]',observation='G has a downward lower-right terminal. VI has horizontal bars above and below, preserved.'),
 dict(form='L with looped foot',reading='L | mathcal L',place='upper paragraph line 4 and both Fig expressions',observation='Font mapping remains doubtful. Same oblique stem/looped foot recurs; first occurrence marked.'),
 dict(form='mulomb(F)',reading='mulomb(F)',place='upper paragraph line 6 [730,505,1141,603]',observation='No t between l and o. The neighboring text calls it petite multiombre.'),
 dict(form='looped script F',reading='mathscr F | mathcal F',place='primitive-data first line, empty-figure subscript, and last prose line',observation='Upper swash and curled lower stem recur; first occurrence retains alphabet doubt. H’s Gothic rendering is not visually compelling.'),
 dict(form='≤ and ll',reading='inclusion and raffinement signs',place='primitive data, At 0, and operation table',observation='≤ has a separate lower stroke; ll has two distinct less-than signs. Both arrowheads and both shafts of each equivalence were checked.'),
 dict(form='c-shaped argument',reading='c | G',place='both Inf formulae',observation='Small open bowl lacks a secure inward bar. First instance remains doubtful; the second follows its preferred c reading.'),
 dict(form='overlined m',reading='abbreviation written as overlined m',place='row (b), [951,1795,1659,2105]',observation='Do not expand to même in the transcription.'),
 dict(form='=',reading='same/même abbreviated by equals sign',place='en = temps in row (b)',observation='Two parallel dark strokes are unmistakable; no replacement with en outre.'),
 dict(form='low dot',reading='F mathbin(ldotp) G',place='row (c), [380,2094,947,2209]',observation='Dot lies near the baseline, not centered on the capitals.'),
 dict(form='slashed oval with F subscript',reading='varnothing with script F subscript',place='row (d), [366,2220,563,2313]',observation='Oval with inclined crossing stroke longer below the oval. Retained varnothing after inspecting the entire local formula; no unsupported switch to phi made.'),
]
hand_log=[
 dict(habit='G often resembles open C',place='GF reference, the ≤/ll formulae, all four operation rows',observation='A short downward lower-right hook often supplies the G distinction. It is clear in GF and major display letters; very small Inf arguments and F∨C/G remain ambiguous. All occurrences on this page were checked, and the habit is not asserted to settle the doubtful ones.'),
 dict(habit='long low connecting runs compress words',place='resté muet; cela; qu’on a; l’avais; temps',observation='m/u/n/e can flatten into connected low strokes. Tall t, l, p and dotted i decide several words where H differs. This is a local habit, not a license to supply missing letters.'),
 dict(habit='script F ends in a curved lower hook',place='ensemble-of-figures symbol and final two F occurrences',observation='Curved lower stroke recurs even at small scale. Exact script/calligraphic classification remains uncertain; angular Gothic typography is not secure.'),
 dict(habit='paired upper quotation strokes',place='engendrée, réunion, somme, intersection fine',observation='Opening/closing signs on the first three terms are little vertical/oblique pairs, not guillemets. The last closing pair remains doubtful.'),
 dict(habit='curved insertion connector can resemble parenthesis',place='ou Inf pour ≤ above intersection row',observation='Continuous lower bracket and descending left end attach to intersection. H’s placement at (a) and opening parenthesis before existe misinterpret this connector.'),
]
notes=[
 dict(id='S004-N01',claim='No continuation from another page was supplied or inferred.',source='scan004 whole image and its two halves only',reasoning_if_any='H’s comments about another manuscript page are editorial evidence excluded from the text; the source begins (et.'),
 dict(id='S004-N02',claim='Heading deletion scope remains unresolved and requires the root editor’s crop adjudication.',source='out/crops/scan004_heading.png [348,728,892,831]',reasoning_if_any='The central cancellation is not plainly a separate struck pré. Keeping C’s uncertain encoding is a provisional preservation of its doubt, not an affirmation of its segmentation.'),
 dict(id='S004-N03',claim='No C doubt inside deleted text was resolved.',source='lieux_deleted, heading, margin_question, deleted_short crops',reasoning_if_any='In every such case some letters remain obscured by the strike. The possible ce was added as an alternative, not accepted as certain.'),
 dict(id='S004-N04',claim='The singular forms familles infinie and non vide are retained.',source='out/crops/scan004_b_text.png',reasoning_if_any='No final s is visible after infinie or vide. Grammatical agreement was not used to normalize them.'),
 dict(id='S004-N05',claim='The second argument written c may be a pen slip or a reduced G; the image does not settle it.',source='out/crops/scan004_b_formula.png and scan004_c_formula.png',reasoning_if_any='The mathematical role would allow G, but that cannot supply a missing stroke. The first occurrence remains doubtful and later recurrence follows the preferred c form.'),
 dict(id='S004-N06',claim='Marked-in-H convention for this review.',source='packets/scan004/H.tex',reasoning_if_any='True means H has an uncertainty wrapper or an editorial note explicitly covering this doubtful, cancelled, or inserted place. A mere formatting macro is not counted as uncertainty.'),
 dict(id='S004-N07',claim='Crop processing is fully recorded.',source='out/review/scan004_crop_manifest.json',reasoning_if_any='Each primary crop is 2600 px wide after LANCZOS resizing, autocontrast, and stated UnsharpMask. The At 4 crop alone was rotated −38 degrees before enhancement. All boxes refer to the original 1680×2361 whole image.'),
 dict(id='S004-N08',claim='No genuine diagram or pictorial drawing occurs on this leaf.',source='whole-image layout inspection',reasoning_if_any='The source has a braced data block, one implication display, and a two-column operation list; no unstated diagram elements need reconstruction.'),
]

audit=[
 dict(C_span=r'\deleted{\unsure{ou|de}}',decision='Retain deletion and doubt; add ce as an admissible alternative.',place='after lieux L',evidence='One sloping stroke crosses the small word only; L is not struck. Crop lieux_deleted. Letters beneath cancellation are not all plain.'),
 dict(C_span=r'\deleted{\unsure{pré}} before \unsure{premières}',decision='Retain C’s doubtful encoding provisionally; exact deletion scope not certified.',place='Données heading',evidence='Crossed tall strokes lie in the middle of a continuous word. No clean separate cancelled pré is demonstrable. Crop heading; root adjudication specifically requested.'),
 dict(C_span=r'\deleted{\unsure{Question}}',decision='Retain deletion and unresolved reading.',place='first lower-left marginal note',evidence='Horizontal strike extends from the initial Q through the baseline word, stopping before the colon. Interior letters remain covered. Crop margin_question.'),
 dict(C_span=r'\inserted{NB.}',decision='Retain replacement insertion.',place='above struck Question',evidence='NB. is visibly above the cancelled word. It replaces the heading; the baseline colon remains to its right. Crop margin_question.'),
 dict(C_span=r'\inserted{ou Inf pour $\leq$}',decision='Retain text and placement immediately after intersection in row (b).',place='above row (b)',evidence='The line beneath the addition turns down at its left end and ends in the gap after intersection. It does not terminate at row (a). Crop b_text.'),
 dict(C_span=r'\deleted{\unsure{G|CG}}',decision='Retain deletion and doubt.',place='short isolated group below F low-dot G',evidence='Multiple strokes cross the entire compact group. Curves survive, but no full letter sequence is unambiguous. Crop deleted_short.'),
]

# Explicit adjudication of every raw comparison row, including mixed, resynchronized stretches.
review_map={
70:('mixed: manuscript/scan marker syntax is ignored; H’s leading guillemet is a real addition',[1]),
71:('real words; C supported',[2,3]),
72:('C alphabet doubt resolved from crop, not macro-only',[4,5]),
73:('real word une supplied only by H',[6]),
74:('mixed alphabet, struck-word, and punctuation differences',[7,8,9]),
75:('real word difference cela/ceci',[10]),
76:('real phrase difference qu’on a/que c’est',[11]),
77:('real punctuation retained from C',[12]),
78:('real notation spelling mulomb/multomb',[13]),
79:('H editorial note; not source text',[]),
80:('real heading and deletion-state difference; unresolved C doubts retained',[14]),
81:('macro-only itemize syntax',[]),
82:('macro-only aligned syntax',[]),
83:('alphabet rendering differs, beyond list syntax',[15]),
84:('macro-only list bracket',[]),
85:('real relation spelling candidates',[16]),
86:('real de/des ending candidates',[17]),
87:('real punctuation after figures',[18]),
88:('uncertainty-only: first déf/def doubt retained after whole-formula inspection',[]),
89:('real absence/presence of hyphen',[19]),
90:('macro-only list markers',[]),
91:('real comma added after raffinement',[20]),
92:('real accent difference in second def label',[21]),
93:('mixed list/brace syntax and H editorial brace note; real At 0 underline extent',[22]),
94:('macro-only tag/makebox syntax',[]),
95:('mixed label placement and moved genuine margin note; all note words audited',[22,23]),
96:('real l’avais/le mets phrase',[24]),
97:('moved genuine marginal text plus H editorial location note; neither discarded as generic noise',[23]),
98:('macro-only array column specification',[]),
99:('mixed list syntax and real circled versus parenthesized label',[42]),
100:('real quote shape and underline omission',[25]),
101:('real closing quote shape',[25]),
102:('real opening quote shape',[25]),
103:('real closing quote shape',[25]),
104:('real opening quote shape',[25]),
105:('real closing quote shape',[25]),
106:('C parenthesis/brace doubt retained; actual following dash is present, already in both readable texts',[]),
107:('mixed array syntax; real insertion attachment and added semicolon',[26,27]),
108:('long resynchronization: substantive (b)–(d) text was independently collated, not excluded as syntax',[27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48]),
109:('real period after inserted NB',[29]),
110:('real abbreviation versus expansion',[30]),
111:('real abbreviation versus expansion',[31]),
112:('long resynchronization: genuine (b) text and final marginal note audited; array syntax only ignored',[32,33,34,35,36,37,38,39,40,41]),
113:('real uncertain marginal word plus H editorial note',[41]),
114:('long resynchronization/list syntax contains row (c) label and formula',[42,43,44]),
115:('resynchronization with H note, actual full formula independently checked',[43,44]),
116:('resynchronization; no omitted F or comma inferred from raw row',[43]),
117:('mixed real c/G formula difference and H editorial cancelled-word note',[43,46]),
118:('long resynchronization: real (c)/(d) text, deletion, script alphabet and parentheses all audited',[42,45,46,47,48]),
}
difference_review=[{'source_row':k,'classification':v[0],'change_ids':[f'S004-{n:03d}' for n in v[1]]} for k,v in sorted(review_map.items())]

sb_read={
'page_number':('handwritten number','3'),
'reste_muet':('real differing words','resté muet'),
'reference':('handwritten reference numeral; resolved C doubt','GF with barred VI'),
'comme_figure':('real differing word omission','comme figure; no une'),
'lieux_deleted':('deletion; whole uncertain notation; differing word','L | mathcal L; deleted ou|de|ce; no separate comma'),
'cela_quon_a':('real differing words','cela signifie qu’on a'),
'ensembliste_close':('differing punctuation','ensembliste),'),
'mulomb':('real differing word','mulomb(F)'),
'heading':('deletion; real differing word; unresolved lower-confidence scope','Données; doubtful heading and cancelled group'),
'figure_alphabet':('whole uncertain symbol/definition; alphabet difference','script F ensemble de figures'),
'relation':('real differing words','rellation|relation; de|des figures'),
'inclusion_formula':('whole formula with C doubt; hyphen difference','F≤G, label déf|def, equivalence, F sous figure de G'),
'raffinement_formula':('whole formula; differing accent','F ll G, label def, equivalence, F raffine G'),
'axiom':('handwritten axiom number; whole display','At 0; F≤G ⇒ F ll G'),
'margin_at4':('margin note; handwritten reference number; real differing words','NB. Ce sera aussi contenu dans At 4 plus bas'),
'axiome':('real differing words','je ne l’avais pas inclus'),
'a_formula':('circled label; whole formula','a; F∨G ou F∪G'),
'a_quotes':('quotation and underline differences','figure engendrée ou réunion ou somme'),
'a_exists':('uncertain closure and differing punctuation','existe )|}; aucun point-virgule final'),
'margin_question':('margin note; deletion; insertion; real differing words','deleted Question; inserted NB.; tjrs; néc.; Fig(L)'),
'margin_tilde':('margin note; whole formula','NB tilde(F cap G)=tilde F cap tilde G'),
'b_formula':('whole formula with C doubt; circled label','b; F wedge G ou F cap G (=Inf^≤(F,c|G))'),
'b_text':('insertion; whole doubtful F∨C/G formula; real differing words','ou Inf pour ≤ attached after intersection; overlined m; familles infinie (non vide); en = temps; F∨C|G'),
'margin_existe':('margin note; real differing word; lower-confidence departure from C','NB Existe dans le cas ensembliste Fig(L) et dans le cas mechisé|méchisé'),
'c_formula':('whole formula with recurring letter doubt; circled uncertain label','c; F low-dot G (=Inf^ll(F,c))'),
'c_text':('quotation doubt; differing underlines','figure intersection fine; closing quotes doubtful'),
'deleted_short':('deletion','deleted G|CG, retained doubt'),
'd_formula':('whole formula; uncertain circled label; alphabet difference','d; varnothing with script F subscript'),
'd_text':('differing punctuation; recurring script symbol','figure vide; plus petit élément de script F (pour ≤ et pour ll)'),
'opening_start':('real differing punctuation','(et; no preceding guillemet'),
}
second_boxes=[dict(box=f'scan004_{name}',kind=sb_read[name][0],x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=sb_read[name][1]) for name,b in boxes.items()]

check_events=[
 {'check':'Read only assigned packet instructions, preamble, notation file, C/H page texts, raw differences and images.json.','source':'packets/RULES.md; PREAMBLE.tex; NOTATION.md; packets/scan004/'},
 {'check':'Personally viewed the whole page once for layout, orientation, page number, blocks, margins and corrections.','source':'H156-01_156-7_scan004.jpg'},
 {'check':'Personally read the upper full-resolution half once, line by line, comparing every word and sign with both witnesses.','source':'H156-01_156-7_scan004_a.jpg'},
 {'check':'Personally read the lower full-resolution half once, line by line, including all margin text and source agreements.','source':'H156-01_156-7_scan004_b.jpg'},
 {'check':'Created and personally viewed 30 named primary crops, including the separately cropped opening. No OCR or text recognition was used.','source':'out/review/scan004_crop_manifest.json'},
 {'check':'Audited every C deleted and inserted span against visible crossing strokes and connector endpoints.','source':'deletion_insertion_audit'},
 {'check':'Read every arrow end, raised sign, Inf argument, tilde, barred numeral, abbreviation, circled marker and underlining extent.','source':'whole halves plus named formula/notation crops'},
 {'check':'Classified all 49 raw difference rows (70–118), retaining substantive differences inside long resynchronization stretches and excluding editorial prose.','source':'packets/scan004/differences.tsv'},
 {'check':'Counted independent physical lines/inscriptions per column and block using the convention recorded in lines_read.','source':'both halves and inventory'},
 {'check':'No other scan, peer output, external text, or TeX compilation was used.','source':'session workflow'},
]
result=dict(scan=4,lines_read={'count':53,'convention':'Count each independent handwritten baseline in each source block/column separately; simultaneous left formula and right explanatory text count independently. Include page number (1), opening prose (7), heading (1), braced data (5), avec (1), At 0 formula (1), axiom prose (2), slanted note (4), row-a formula (1) and prose (5), first lower note (6, including inserted NB), tilde note (1), row-b formula lines (2) and prose (5), its insertion (1), bottom-left note (3), row-c formula (1) and prose (2), isolated cancellation (1), row-d formula (1) and prose (2). A label written on a formula baseline is part of that line; arrow superscripts and accents are not separate lines.'},changes=changes,doubts=doubts,inventory=inventory,notation=notation,hand_log=hand_log,notes=notes,check_events=check_events,deletion_insertion_audit=audit,difference_review=difference_review,second_boxes=second_boxes)
(base/'out/review/scan004_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(f'Saved review with {len(changes)} differences, {len(doubts)} retained/new doubts, {len(difference_review)} raw-row reviews, and {len(second_boxes)} second-reading boxes.')
