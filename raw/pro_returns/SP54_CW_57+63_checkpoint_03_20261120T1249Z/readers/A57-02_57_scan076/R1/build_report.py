from pathlib import Path
from datetime import datetime, timezone
import json
root=Path('/workspace/scratch/b9993b8b5640')
base=root/'out/readers/A57-02_57_scan076/R1'
src=root/'source/SP54_CW_57+63_scans'
A=str(src/'A57-02_57_scan076_a.jpg'); B=str(src/'A57-02_57_scan076_b.jpg'); W=str(src/'A57-02_57_scan076.jpg')
cp=lambda n:str(base/'crops'/f'{n}.png')
ev=lambda s,box:{'source':s,'bbox':box,'coordinates':'source pixels, left top right bottom'}
changes=[
 dict(id='R1-01',place='Opening paragraph, cancelled phrase after simple',c=r'\deleted{\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}}',h=r'\struck{morphism (namely that}',reading=r'\deleted{\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}}',differs_c=False,differs_h=True,kind='misread word',h_marked='no',confidence='low',scan_shows='The typed x row crosses a recoverable morphism and parenthesis; the remaining crowded stems support with, a capital X/Y and the tentative ending prjt. They do not permit removal of the C alternatives. The parenthesis follows the word closely. H gives a different cancelled phrase confidently.',evidence=ev(W,[526,524,968,566]),crop=cp('cancelled_morphism'),mathematical_consequence=None),
 dict(id='R1-02',place='Opening paragraph, the proofsbeing',c='the proofsbeing',h='the proofs being',reading='the proofsbeing',differs_c=False,differs_h=True,kind='other',h_marked='no',confidence='high',scan_shows='The terminal s of proofs is followed at the ordinary adjacent-character pitch by b of being; there is no blank character cell.',evidence=ev(A,[832,1085,1138,1130]),crop=None,mathematical_consequence=None),
 dict(id='R1-03',place='Opening paragraph, cancelled and Mumford\'s',c=r"\deleted{\unsure{and Mumford's}}",h=r"\struck{and Mumford's}",reading=r"\deleted{and Mumford's}",differs_c=True,differs_h=False,kind='misread word',h_marked='no',confidence='medium',scan_shows='Residual lower bowls and stems give and; the capital M, u/m shoulders, tall f, o/r/d remnants and final apostrophe-s remain recoverable through the typed x row and pen crossing. Cancellation is clear.',evidence=ev(B,[1306,171,1589,211]),crop=cp('cancelled_mumford'),mathematical_consequence=None),
 dict(id='R1-04',place='Opening paragraph, boundary after uses (i)',c=r"(i)\deleted{\unsure{and Mumford's}}",h=r"(i) \struck{and Mumford's}",reading=r"(i)\deleted{and Mumford's}",differs_c=False,differs_h=True,kind='other',h_marked='no',confidence='high',scan_shows='The first overprinted character is adjacent to the closing parenthesis, without an intervening blank typewriter cell. This row concerns only the boundary space; the uncertainty decision is R1-03.',evidence=ev(B,[1244,166,1378,214]),crop=cp('cancelled_mumford'),mathematical_consequence=None),
 dict(id='R1-05',place='Opening paragraph, initial overtype in to reduce',c=r'\deleted{\unsure{h}}to',h='to',reading=r'\unsure{\deleted{h}t|\deleted{t}h}o',differs_c=True,differs_h=True,kind='deletion state',h_marked='no',confidence='medium',scan_shows='The first position has the tall stem, shoulder and right descender-to-baseline of h together with the crossbar/body of t; two superposed character bodies are visible. The image does not fix which impression was typed last. The first alternative follows C\'s cancelled-h/live-t order, the second preserves the reverse assignment. H omits the underlying character.',evidence=ev(B,[262,234,309,265]),crop=cp('overtyped_to'),mathematical_consequence=None),
 dict(id='R1-06',place='Statement (i), X,Y after Let',c='$X,Y$',h='$X$, $Y$',reading='$X,Y$',differs_c=False,differs_h=True,kind='other',h_marked='no',confidence='high',scan_shows='X, comma and Y occupy consecutive typewriter positions; there is no additional space after the comma.',evidence=ev(B,[510,371,590,417]),crop=cp('deleted_continuation'),mathematical_consequence=None),
 dict(id='R1-07',place='Statement (i), inserted surjective',c=r'\inserted{\uline{surjective}}',h=r'\add{surjective}',reading=r'\inserted{\uline{surjective}}',differs_c=False,differs_h=True,kind='omission',h_marked='no',confidence='high',scan_shows='A straight underline directly under surjective is distinct from the wider curved insertion bracket and its downward attachment before S-morphis. H does not encode the underline.',evidence=ev(B,[1290,332,1510,377]),crop=None,mathematical_consequence=None),
 dict(id='R1-08',place='Statement (i), crossed beginning of continuation line before assume',c=r'\deleted{m,}',h=r'\struck{\ill{}}',reading=r'\deleted{m,}',differs_c=False,differs_h=True,kind=r'readable ink left as \ill{}',h_marked='yes',confidence='high',scan_shows='The typed m has its baseline and two shoulders below several oblique pen cancellation strokes; the comma remains visible to its right. The handwritten replacement m, is at the end of S-morphis on the preceding line.',evidence=ev(B,[261,443,326,478]),crop=cp('deleted_continuation'),mathematical_consequence=None),
 dict(id='R1-09',place='Statement (i), raised mark on f',c=r"\unsure{f^{\bullet}|f^{\circ}|f'}",h=r'f^{\cdot}',reading=r'f^{\bullet}',differs_c=True,differs_h=False,kind='misread symbol or index',h_marked='no',confidence='high',scan_shows='The mark is a compact filled round spot raised at the upper right of f. It lacks a clearly open ring and an extended oblique prime shaft. H\'s cdot and the proposed bullet represent this same raised filled point; no separate H glyph difference is counted.',evidence=ev(B,[474,509,515,548]),crop=cp('raised_f_mark'),mathematical_consequence='The raised point is preserved; no change to the map source, target or asserted property.'),
 dict(id='R1-10',place='Statement (i), final is .',c='is .',h='is.',reading='is .',differs_c=False,differs_h=True,kind='other',h_marked='no',confidence='high',scan_shows='A blank typewriter cell separates the s of is and the full stop.',evidence=ev(B,[880,651,967,699]),crop=None,mathematical_consequence=None)
]
c_doubts=[
 dict(place='Cancelled phrase after simple',c=r'\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}',reading=r'\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}',status='retained',evidence=ev(W,[526,524,968,566]),crop=cp('cancelled_morphism'),confidence='low'),
 dict(place="Cancelled and Mumford's",c=r"\unsure{and Mumford's}",reading="and Mumford's",status='resolved',evidence=ev(B,[1306,171,1589,211]),crop=cp('cancelled_mumford'),confidence='medium'),
 dict(place='Underlying h at to reduce',c=r'\unsure{h}',reading=r'\unsure{\deleted{h}t|\deleted{t}h}o',status='revised',evidence=ev(B,[262,234,309,265]),crop=cp('overtyped_to'),confidence='medium'),
 dict(place='Raised f mark in statement (i)',c=r"\unsure{f^{\bullet}|f^{\circ}|f'}",reading=r'f^{\bullet}',status='resolved',evidence=ev(B,[474,509,515,548]),crop=cp('raised_f_mark'),confidence='high')
]
inv=[]
def item(element,kind,pos,words,hand='typewriter'):
 inv.append(dict(sheet_kind='letter',hand=hand,element=element,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
item('076-R1-01','text','top right','July 18, 1962','another unnamed hand')
item('076-R1-02','text','salutation','My dear Murre,')
item('076-R1-03','text','opening paragraph B01–B15','I recently had some thought on finiteness conditions')
item('076-R1-04','insertion','above B04 cancelled phrase','projective morphism')
item('076-R1-05','deletion','B04 after simple','morphism(with X/Y prjt; x-overprinted')
item('076-R1-06','text','B05 inline formula','Pic with underline, upper P and lower X/S')
item('076-R1-07','deletion','B06 after where','the fibers; typed x cancellation')
item('076-R1-08','insertion','above B07, attached between fibers, and Using','(at least if these are normal).; handwritten curved attachment bracket')
item('076-R1-09','deletion','B13 immediately after uses (i)',"and Mumford's; typed x and handwritten crossing")
item('076-R1-10','deletion','B14 first character','superposed h and t; both layer assignments retained')
item('076-R1-11','text','statement (i), I01–I05','Let X,Y be proper over S noetherian')
item('076-R1-12','text','I01 f:X to Y','right arrow','another unnamed hand')
item('076-R1-13','insertion','above I01, attached before S-morphis','surjective, singly underlined; curved handwritten insertion bracket')
item('076-R1-14','insertion','right end of I01 after S-morphis','m,','another unnamed hand')
item('076-R1-15','deletion','I02 before assume','m,; handwritten slashes cross typed letters')
item('076-R1-16','text','I03 map label','f with raised filled round point; Pic Y/S and Pic X/S singly underlined')
item('076-R1-17','text','I03 between Pic terms','right arrow','another unnamed hand')
item('076-R1-18','text','statement (ii), II01–II04','The same conclusion holds for a canonical immersion')
item('076-R1-19','text','II01 X to Y','right arrow','another unnamed hand')
item('076-R1-20','text','II03 dimension relation','greater-than angle and lower oblique stroke, followed by typed 3','another unnamed hand')
item('076-R1-21','text','II04 invertible sheaf','single-underlined capital L')
item('076-R1-22','text','bottom sentence E01','A connected result is that for any X/S proper, and integer')
item('076-R1-23','text','E01 between n and 0','not-equal sign','another unnamed hand')
item('076-R1-24','margin note','bottom left','75; pencil archive sheet number','another unnamed hand')
notation=[
 dict(sign='Pic pieces',latex=r'\underline{\mathrm{Pic}}^P_{X/S}',place='B05',visible_shape='Capital P, lowercase ic, one underline; raised capital P; lowered X/S.',alternatives=[]),
 dict(sign='f raised point',latex=r'f^{\bullet}',place='I03',visible_shape='Compact filled round raised point without a prime shaft or open centre.',alternatives=[]),
 dict(sign='Pic source and target',latex=r'\underline{\mathrm{Pic}}_{Y/S}\handwritten{\to}\underline{\mathrm{Pic}}_{X/S}',place='I03; repeated subscripts in I04–I05',visible_shape='Single underline under each Pic; Y/S on the left, X/S on the right. Hand-drawn horizontal arrow with right-facing head.',alternatives=[]),
 dict(sign='dimension relation',latex=r'\handwritten{\geqslant}3',place='II03',visible_shape='Right-facing angle with separate oblique lower stroke parallel to the lower arm, then typed 3.',alternatives=[]),
 dict(sign='sheaf letter',latex=r'\underline L',place='II04',visible_shape='Capital L with serifed upright and foot; one independent underline.',alternatives=[]),
 dict(sign='integer inequality',latex=r'n\handwritten{\ne}0',place='E01',visible_shape='Two short horizontal strokes crossed by a slanting stroke between typed n and 0.',alternatives=[]),
 dict(sign='date year initial',latex='1962',place='date',visible_shape='Handwritten numeral 1 before 962.',alternatives=[]),
 dict(sign='cancelled capital after with',latex=r'\unsure{X|Y}',place='B04 cancelled phrase',visible_shape='Lower portion of a crossed capital obscured by typed x cancellation.',alternatives=['X','Y'])
]
blocks=[
 'Date, salutation and archive pencil number',
 'Opening paragraph B01–B15, including three insertions/deletions above lines and two cancellations at B13–B14',
 'Statement (i), I01–I05, including surjective insertion, handwritten word ending, cancelled continuation and all inline formulas',
 'Statement (ii), II01–II04, including handwritten arrow and inequality, underlined sheaf L',
 'Unfinished connected-result sentence E01, ending with n not equal to 0 and comma'
]
end=datetime.now(timezone.utc).isoformat()
report=dict(page='A57-02_57_scan076',cote='57',our_scan='76',reader='R1',start_utc='2026-11-20T11:17:40+00:00',end_utc=end,model='GPT-6 Astra Pro (exposed agent identity)',effort='not exposed',images_viewed=[W,A,B],crops=[],coverage=dict(all_lines_read=True,all_elements_included=True,blocks=blocks),changes=changes,c_doubts=c_doubts,remaining_doubts=[
 dict(place='B04 cancelled phrase',reading=r'morphism(with $X$ prjt',alternatives=[r'morphism(with $Y$ prjt'],confidence='low',reason='Typed x overprint obscures the capital and portions of the abbreviation; the full C uncertainty remains.',crop=cp('cancelled_morphism')),
 dict(place='B14 first character',reading=r'\deleted{h}t',alternatives=[r'\deleted{t}h'],confidence='medium',reason='Both h and t bodies can be read, but their application order and live-layer assignment are not visually fixed.',crop=cp('overtyped_to'))
],inventory=inv,notes=dict(summary='The letter reports improvements concerning finiteness of Picard preschemes, discusses a result attributed to Mumford and the reduction involving normality and Hilbert-polynomial coefficients, and records two numbered assertions. It begins a further connected-result sentence at the foot of the page. These are statements read from the page, not results proved in this run.',reading_decisions=[],author_checks=[{'place':'B08','quote':'the proof of which is quite simple and beautiful'},{'place':'B12–B13','quote':'the proofsbeing very technical, and rather different for (i) and (ii)'},{'place':'B13–B15','quote':"except that (ii) uses (i) ... to reduce to the normal case; moreover (ii) uses Mumford's result and the equivalence criteria as developped in my last Seminar"}],titles_dates_pagination=[{'place':'top right','text':'July 18, 1962','form':'handwritten'},{'place':'salutation','text':'My dear Murre,','form':'typed'},{'place':'bottom left','text':'75','form':'pencil archive sheet number; encoded as comment'},{'place':'page','text':'No visible author/typescript page number','form':'No mspage macro added'}]),notation=notation,abbreviations=[dict(abbreviation='prjt',proposed_expansion='projective (tentative, confined to cancelled phrase)',place='B04'),dict(abbreviation='i.e.',proposed_expansion='id est',place='I04'),dict(abbreviation='iff',proposed_expansion='if and only if',place='I05')],check_events=[])
for file in sorted((base/'crops').glob('*.json')):
 data=json.loads(file.read_text()); width=data['bbox'][2]-data['bbox'][0]
 report['crops'].append({k:data[k] for k in ['file','source','bbox','rotation','purpose','output_size','method']}|{'scale_x':data['output_size'][0]/width,'viewed_once':True})
report['image_delivery_events']=[dict(file=cp('overtyped_to'),event='Third image was explicitly discarded by output limit in a three-image result; that discarded delivery was not viewed or counted. The existing image was resent alone and viewed once. No replacement crop was made.')]
report['pagination_collation']=dict(c=r'\scanpage{76}; % archive sheet number: 75',h=r'\page{75}',reading=r'\scanpage{76}; % archive sheet number: 75',decision='H page 75 maps to scan 76 by the supplied page mapping. This equivalent wrapper is excluded from change counts. The separate visible pencil 75 is inventoried; no authored page number is present.')
report['equivalent_encoding_notes']=[r'H \add{July 18, 1962} and the reading \handwritten{July 18, 1962} carry the same visible date.',r'H \add / \struck and reading \inserted / \deleted map to the same insertion and cancellation states except where a row explicitly records a different layer assignment.',r'H \colon and C colon, H \neq and C \ne, and H f^{\cdot} and the proposed f^{\bullet} map to the visible colon, crossed-equals sign, and raised filled point respectively; no independent symbol changes are counted for those spellings.',r'H unwrapped hand-drawn arrows and C \handwritten wrappers have identical arrow arguments; provenance wrappers do not count as textual differences.']
report['prior_flags']=[dict(place='B01',flag='some thought / some thoughts',decision='Confirmed singular some thought from visible final t and following space.'),dict(place='B12',flag='proofsbeing / proofs being',decision='Confirmed attached proofsbeing.'),dict(place='B15',flag='developped / developed',decision='Confirmed double p in developped.'),dict(place='I03',flag='the f / then f',decision='Confirmed the f; no n between e and f.'),dict(place='I05',flag='is . / is.',decision='Confirmed one blank typewriter position before the full stop.')]
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
observations='''# R1 observations — A57-02_57_scan076

Start: 2026-11-20 11:17:40 UTC. Exposed identity: GPT-6 Astra Pro. Effort setting: not exposed.

## Inspection record

The whole was viewed once for layout. Half A and half B were each viewed once at supplied resolution. Every line, including C/H agreement, was read visually. No OCR, web, other pages or other readers were consulted. The half overlap was encountered in the two prescribed views; neither half was reopened. Half B begins at whole-image y = 993.

## Ordered coverage

- D: handwritten July 18, 1962; numeral 1 in the year.
- S: My dear Murre, with comma.
- B01: I recently … Picard; singular thought.
- B02: preschemes, … in the; every word read.
- B03: last section … there; Bourbaki and full stop read.
- B04: for a simple … with connected geometric fibers; typed projective morphism inserted above crossed morphism phrase. Cancelled phrase retained with X/Y uncertainty after crop.
- B05: (namely that … has been; capital Pic, one underline, upper P, lower X/S, closing parenthesis all read.
- B06: extended … f simple; crossed the fibers recoverable on half A.
- B07: we assume … Using his; f flat and integral geometric fibers read. Typed insertion (at least if these are normal). has its own curved hand attachment between fibers, and Using.
- B08: result (the proof … I could; punctuation and beautiful read.
- B09: get rid … 4.1. of; normality and both points in 4.1. read.
- B10: my talk) … non trivial; no lexical hyphen in non trivial.
- B11: coefficients … for the; Hilbert polynomials and full stop read.
- B12: reduction … rather; proofsbeing is attached.
- B13: different … uses (i), followed immediately by crossed and Mumford's; the three roman labels and boundary space checked. The crop supports removal of the word-reading doubt.
- B14: overtyped first character before o reduce … result; separate h and t impressions retained with both live/cancelled assignments.
- B15: and the equivalence … Seminar):; developped has two p's, colon after parenthesis.
- I01: (i) Let X,Y … S-morphis; no space after the comma in X,Y. Right arrow X to Y. Singly underlined surjective inserted before S-morphis. Handwritten m, completes the word at the far right.
- I02: crossed m, then assume … preschemes; crop confirms readable m and comma under oblique pen strokes.
- I03: exist, the f with raised filled point : Pic Y/S to Pic X/S … affine; the without n. Every Pic letter, underline, subscript and arrow read; point resolved from crop.
- I04: if S … quasi-; spectrum of a field), i.e., M, and lower Y/S read.
- I05: compact iff … is .; quasi-compact retains lexical hyphen, lower X/S, and blank before the full stop.
- II01: (ii) The same conclusion … X to Y,; hand arrow and final comma read.
- II02: if Y/S … are of; every word read.
- II03: dimension greater-than-or-equal 3, … section; lower stroke is slanted. sub-scheme retains its lexical hyphen.
- II04: over Y … S.; capital L singly underlined, final point.
- E01: A connected result … integer n not-equal 0,; inequality has two bars and transverse stroke, sentence continues beyond this page.
- Archive margin: pencil 75 at bottom left. No visible authored/typescript pagination, heading, signature, independent diagram, drawing or separate marginal prose.

## Unresolved-place crop record

Five distinct places were cropped once with the supplied helper: cancelled morphism phrase, cancelled and Mumford's, the h/t overtype, the crossed m, continuation, and the raised f mark. Each crop uses autocontrast, LANCZOS enlargement to 3000 pixels wide, and sharpening; no rotation was needed for these near-horizontal lines. Exact source boxes, output dimensions and scale factors are in report.json and crop sidecars.

A three-image result explicitly discarded the third image, overtyped_to.png. That unseen delivery was not counted. The same existing file was sent alone and inspected once. No crop was remade or reopened.

## Collation decisions

All four C uncertainty macros have decisions. The cancelled morphism phrase remains uncertain. The cancelled and Mumford's and filled raised f mark are resolved. The h/t uncertainty is revised to retain both layer orders. H differences include the cancelled phrase, proofsbeing, the absent gap before crossed and Mumford's, the h/t layer, X,Y spacing, surjective's underline, readable crossed m, and is . spacing. H page 75 maps to scan 76; the archive pencil 75 is separately inventoried. Equivalent wrappers are documented rather than counted as changes.

## Mathematical checking

I read the formulas, indices and assertions from the ink. I did not prove, disprove, calculate or independently recheck a mathematical assertion, and I did not use a theorem to choose letters. check_events is therefore empty. The summary in report.json attributes the mathematical material to this page.
'''
(base/'observations.md').write_text(observations)
print(json.dumps({'files':[str(base/n) for n in ['reading.tex','observations.md','report.json']],'changes':len(changes),'c_doubts':len(c_doubts),'crops':len(report['crops']),'remaining_doubts':len(report['remaining_doubts']),'end_utc':end}))
