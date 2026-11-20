from pathlib import Path
import json
from datetime import datetime, timezone
base=Path('/workspace/scratch/b9993b8b5640/out/readers/A57-02_57_scan076/R2')
inp=Path('/workspace/scratch/b9993b8b5640/work/inputs/A57-02_57_scan076')
page=json.loads((inp/'page.json').read_text())
a=page['half_a']; b=page['half_b']; whole=page['whole']
c=(inp/'C.tex').read_text()
(base/'reading.tex').write_text(c)
cp={i:str(base/'crops'/name) for i,name in enumerate(['01_cancelled_morphism.png','02_cancelled_mumford.png','03_overtyped_to.png','04_raised_f.png','05_cancelled_m.png'],1)}
def ev(source, bbox): return {'source':source,'bbox':bbox,'coordinates':'source pixels [left, top, right, bottom]'}
def change(id,place,c,h,reading,kind,confidence,scan_shows,evidence,crop=None,h_marked='no',mathematical_consequence=None):
 return dict(id=id,place=place,c=c,h=h,reading=reading,differs_c=(c!=reading),differs_h=True,kind=kind,h_marked=h_marked,confidence=confidence,scan_shows=scan_shows,evidence=evidence,crop=crop,mathematical_consequence=mathematical_consequence)
d1=r'\deleted{\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}}'
d2=r"\deleted{\unsure{and Mumford's}}"
d3=r'\deleted{\unsure{h}}to'
d4=r"\unsure{f^{\bullet}|f^{\circ}|f'}"
changes=[
 change('R2-01','L06, cancelled phrase after simple',d1,r'\struck{morphism (namely that}',d1,'misread word','low','Typed x overstrikes cross the lower phrase. The initial morphism and following parenthesis are recoverable, with no full character cell between them. Residual strokes support with, then an X/Y-shaped capital and an abbreviated ending read prjt; the capital and ending remain obscured. The upper live line reads projective morphism.',ev(a,[528,505,963,560]),cp[1]),
 change('R2-02','L14, proofsbeing','proofsbeing','proofs being','proofsbeing','other','high','The final s of proofs is followed by b at the next ordinary typewriter character position, with no intervening blank cell.',ev(a,[909,1083,1139,1128])),
 change('R2-03','L15, cancelled and Mumford\'s',d2,r"\struck{and Mumford's}",d2,'other','low','The proposed words remain plausible from a/n/d, the capital and following stem sequence, and final s; x-overprints and a pen stroke obscure parts of the name and apostrophe. H gives a confident reading; the proposed transcription retains the uncertainty.',ev(b,[1307,169,1589,207]),cp[2]),
 change('R2-04','L15, boundary between (i) and cancelled words',r"uses (i)\deleted{\unsure{and Mumford's}}",r"uses (i) \struck{and Mumford's}",r"uses (i)\deleted{\unsure{and Mumford's}}",'other','high','The first crossed character follows the closing parenthesis at the next typed position; there is no blank character cell. This row concerns the boundary spacing only; the cancelled wording and certainty are recorded in R2-03.',ev(b,[1244,170,1358,210]),cp[2]),
 change('R2-05','L16, overtyped first letter in to reduce',d3,'to',d3,'omission','low','The first live t has superposed lower vertical/shoulder strokes consistent with an underlying h. The composite is followed by an ordinary o. The underlying character remains uncertain; the live word is to. The earlier layer is preserved before the live t.',ev(b,[264,233,310,269]),cp[3]),
 change('R2-06','L18, X,Y boundary',r'$X,Y$',r'$X$, $Y$',r'$X,Y$','other','high','X, comma, and Y occupy consecutive typewriter positions; no blank cell follows the comma.',ev(b,[514,373,584,412])),
 change('R2-07','L18 interlinear surjective',r'\inserted{\uline{surjective}}',r'\add{surjective}',r'\inserted{\uline{surjective}}','omission','high','The interlinear typed word surjective has a single straight underline. A separate hand-drawn attachment bracket points down before S-morphis.',ev(b,[1286,332,1540,403])),
 change('R2-08','L19, cancelled line-opening m comma',r'\deleted{m,}',r'\struck{\ill{}}',r'\deleted{m,}','readable ink left as \\ill{}','medium','Under the oblique cancellation strokes, the lower multi-stem body and base of m and a following descending comma remain recoverable. The cancellation strokes are independently visible. The replacement m comma is handwritten at the right end of the preceding line.',ev(b,[261,442,322,484]),cp[5],h_marked='yes'),
 change('R2-09','L20, raised mark on the Picard-map f',d4,r'f^{\cdot}',d4,'misread symbol or index','medium','A compact raised rounded spot follows f. It has a dark body and a slight lower-right taper; the reproduction leaves a tiny internal pale feature unresolved. A filled dot is the leading reading, with circle and prime retained. No mathematical meaning was used to select among them.',ev(b,[470,510,538,550]),cp[4],mathematical_consequence='The superscript mark on the map label remains uncertain; the source and target are read directly as Pic with Y/S and Pic with X/S.'),
 change('R2-10','L22, final is space period','is .','is.','is .','other','high','A visible blank typewriter cell separates is from the full stop.',ev(b,[880,658,968,702]))
]
c_doubts=[
 {'place':'L06, cancelled phrase after simple','c':r'\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}','reading':r'\unsure{morphism(with $X$ prjt|morphism(with $Y$ prjt}','status':'retained','evidence':ev(a,[528,505,963,560]),'crop':cp[1],'confidence':'low'},
 {'place':"L15, cancelled and Mumford's",'c':r"\unsure{and Mumford's}",'reading':r"\unsure{and Mumford's}",'status':'retained','evidence':ev(b,[1307,169,1589,207]),'crop':cp[2],'confidence':'low'},
 {'place':'L16, underlying h at to reduce','c':r'\unsure{h}','reading':r'\unsure{h}','status':'retained','evidence':ev(b,[264,233,310,269]),'crop':cp[3],'confidence':'low'},
 {'place':'L20, raised f mark','c':d4,'reading':d4,'status':'retained','evidence':ev(b,[470,510,538,550]),'crop':cp[4],'confidence':'medium'}
]
remaining=[
 {'place':'L06, cancelled phrase','reading':r'morphism(with $X$ prjt','alternatives':[r'morphism(with $Y$ prjt'],'confidence':'low','reason':'Full-width typed crossing marks merge with the underlying letters; the capital and trailing abbreviation remain uncertain. H\'s reading morphism (namely that was examined but is not adopted.','crop':cp[1]},
 {'place':'L15, cancelled words','reading':"and Mumford's",'alternatives':[],'confidence':'low','reason':'Some of the name and apostrophe are obscured by typed crossing marks and pen; no distinct alternative word sequence is supported enough to transcribe.','crop':cp[2]},
 {'place':'L16, cancelled underlying letter','reading':'h','alternatives':[],'confidence':'low','reason':'The composite t contains lower shoulder/stem remnants, but the underlying letter is only partly separable. The reading is preserved as a deleted uncertain h before live to.','crop':cp[3]},
 {'place':'L20, raised f mark','reading':r'f^{\bullet}','alternatives':[r'f^{\circ}',"f'"],'confidence':'medium','reason':'Rounded raised spot with a dark centre, slight terminal taper, and an unresolved pale internal feature.','crop':cp[4]}
]
items=[]
def inv(element,kind,position,first,hand='typewriter'):
 items.append(dict(sheet_kind='letter',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('076-R2-01','text','L01, top right','July 18, 1962','another unnamed hand')
inv('076-R2-02','text','L02, salutation','My dear Murre,')
inv('076-R2-03','text','L03–L17, opening paragraph','I recently had some thought')
inv('076-R2-04','deletion','L06, lower typed line after simple',r'morphism(with X/Y prjt')
inv('076-R2-05','insertion','above L06 deletion','projective morphism')
inv('076-R2-06','text','L07, inline formula',r'\underline{\mathrm{Pic}}^{P}_{X/S}')
inv('076-R2-07','deletion','L08, after where','the fibers')
inv('076-R2-08','insertion','between L08 and L09, bracket attached after fibers,','(at least if these are normal).','typewriter; attachment by another unnamed hand')
inv('076-R2-09','deletion','L15, directly after (i)',"and Mumford's",'typewriter; cancellation includes another unnamed hand')
inv('076-R2-10','deletion','L16, first t over a possible h','h beneath live t')
inv('076-R2-11','text','L18–L22, statement (i)','(i) Let X,Y be proper')
inv('076-R2-12','insertion','L18, between X and Y in f label',r'\to','another unnamed hand')
inv('076-R2-13','insertion','above L18, before S-morphis','surjective, single underline and attachment bracket','typewriter; attachment by another unnamed hand')
inv('076-R2-14','insertion','L18, right margin after S-morphis','m,','another unnamed hand')
inv('076-R2-15','deletion','L19, before assume','m,','typewriter; cancellation by another unnamed hand')
inv('076-R2-16','text','L20, inline Picard-map formula',r'f raised mark: \underline{\mathrm{Pic}}_{Y/S} to \underline{\mathrm{Pic}}_{X/S}')
inv('076-R2-17','insertion','L20, Picard-map arrow',r'\to','another unnamed hand')
inv('076-R2-18','text','L21–L22, inline Picard expressions',r'\underline{\mathrm{Pic}}_{Y/S}; \underline{\mathrm{Pic}}_{X/S}')
inv('076-R2-19','text','L23–L26, statement (ii)','(ii) The same conclusion holds')
inv('076-R2-20','insertion','L23, canonical immersion arrow',r'X\to Y','another unnamed hand')
inv('076-R2-21','insertion','L25, relation before 3',r'\geqslant','another unnamed hand')
inv('076-R2-22','text','L26, invertible sheaf letter',r'\underline{L}')
inv('076-R2-23','text','L27, bottom paragraph fragment','A connected result is that for any X/S proper, and integer n')
inv('076-R2-24','insertion','L27, relation between n and 0',r'\ne','another unnamed hand')
inv('076-R2-25','margin note','bottom left, pencil archive number','75','another unnamed hand')
crops=[]
for i in range(1,6):
 r=json.loads(Path(cp[i]).with_suffix('.json').read_text())
 r['scale']=r['output_size'][0]/(r['bbox'][2]-r['bbox'][0])
 r['viewed_once']=True
 crops.append(r)
notation=[
 {'sign':'Pic pieces','latex':r'\underline{\mathrm{Pic}}^{P}_{X/S}','place':'L07','visible_shape':'Capital P with lower ic and one underline; raised capital P; lower X/S.','alternatives':[]},
 {'sign':'raised f mark','latex':d4,'place':'L20','visible_shape':'Compact raised round dark spot, slight lower-right taper, unresolved tiny pale internal feature.','alternatives':[r'f^{\bullet}',r'f^{\circ}',"f'"]},
 {'sign':'Pic map and subset indices','latex':r'\underline{\mathrm{Pic}}_{Y/S}; \underline{\mathrm{Pic}}_{X/S}','place':'L20–L22','visible_shape':'Singly underlined capital P plus lowercase ic; lowered Y/S at source and subset, lowered X/S at target and image.','alternatives':[]},
 {'sign':'right arrows','latex':r'\handwritten{\to}','place':'L18, L20, L23','visible_shape':'Hand-drawn horizontal strokes ending in right-facing arrowheads.','alternatives':[]},
 {'sign':'dimension relation','latex':r'\handwritten{\geqslant}3','place':'L25','visible_shape':'Right-facing angle with a separate lower oblique stroke; typed 3 follows.','alternatives':[]},
 {'sign':'invertible sheaf','latex':r'\underline{L}','place':'L26','visible_shape':'Single-struck serifed capital L with one underline.','alternatives':[]},
 {'sign':'nonzero integer relation','latex':r'n\handwritten{\ne}0','place':'L27','visible_shape':'Two short horizontal strokes crossed by an oblique stroke between typed n and 0.','alternatives':[]},
 {'sign':'year initial','latex':'1962','place':'L01','visible_shape':'Handwritten numeral 1 followed by 962.','alternatives':[]},
 {'sign':'typed capitals X, Y, S, M, P','latex':'X, Y, S, M, P','place':'throughout','visible_shape':'Ordinary serifed typewriter capitals. No alphabet change is inferred from the heavy impressions.','alternatives':[]}
]
report={
 'page':page['page'],'cote':page['cote'],'our_scan':page['our_scan'],'reader':'R2 (/root/p57_076_r2)',
 'start_utc':'2026-11-20T11:17:48Z','end_utc':datetime.now(timezone.utc).isoformat(),
 'model':'GPT-6 Astra Pro (developer-exposed identity)','effort':'not exposed in task metadata',
 'images_viewed':[whole,a,b],'crops':crops,
 'coverage':{'all_lines_read':True,'all_elements_included':True,'blocks':['L01 handwritten date','L02 salutation','L03–L17 opening paragraph, including all corrections and inline formula','L18–L22 statement (i), handwritten completions, arrows and crossed m comma','L23–L26 statement (ii), arrow, dimension relation and underlined L','L27 bottom continuation fragment and handwritten nonzero sign','bottom-left archive number 75'], 'image_view_counts':{'whole':1,'half_a':1,'half_b':1}, 'crop_view_count':5},
 'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':items,
 'notes':{
  'summary':'The letter to Murre, dated July 18, 1962, reports improved finiteness results for Picard preschemes, describes a result attributed to Mumford and the author\'s claimed further reduction, then states items (i) and (ii). A final connected-result sentence ends at the page boundary after the nonzero integer condition. These are descriptions of the page\'s assertions; their proofs were not checked.',
  'reading_decisions':[],
  'author_checks':[],
  'titles_dates_pagination':{'date':'July 18, 1962','salutation':'My dear Murre,','authored_page_number':None,'archive_number':'75, pencil at bottom left','our_scan':'76','c':r'\scanpage{76} ... % archive sheet number: 75','h':r'\page{75}','treatment':'H page 75 corresponds to our scan 76 under the supplied page metadata. The visible pencil 75 is retained as an archive comment, with no mspage. This encoding correspondence is excluded from textual change counts.','evidence':ev(b,[25,1097,70,1131])},
  'authorship':'No named authorship is established from this page alone. The body is typed; the date, correction/attachment marks, mathematical arrows and relations, right-margin m comma, and pencil archive number are handwritten.',
  'mathematical_check_scope':'No proof, numerical computation or formal verification was performed. The mathematical letters, indices and relations were inspected directly from ink. No mathematical fact was used to choose a reading.',
  'visual_delivery':'Exactly one view of each supplied image and each of five crops; no output image was discarded. The largest image-result batch contained three images.',
  'nontext_physical_marks':'The top-left staple/rust trace and paper folds carry no transcribed writing. There are no independent drawings, diagrams, displays, signature or closing on this page.'
 },
 'notation':notation,
 'abbreviations':[{'abbreviation':'prjt','proposed_expansion':'projective (tentative; cancelled abbreviated text itself remains uncertain)','place':'L06'},{'abbreviation':'i.e.','proposed_expansion':'that is','place':'L21'},{'abbreviation':'iff','proposed_expansion':'if and only if','place':'L22'}],
 'check_events':[],
 'prior_flags':[
  {'place':'L03','reading':'some thought','decision':'Confirmed singular thought from the half; no C uncertainty macro here.'},
  {'place':'L07','reading':r'\underline{\mathrm{Pic}}^{P}_{X/S}','decision':'Capital P, raised P and lower X/S each inspected.'},
  {'place':'L14','reading':'proofsbeing','decision':'Confirmed attached spelling; H inserts a space.'},
  {'place':'L17','reading':'developped','decision':'Both p letters are visible; retained.'},
  {'place':'L20','reading':'the f','decision':'The typed article is the; no extra letter added.'},
  {'place':'L22','reading':'is .','decision':'Confirmed visible blank before full stop.'},
  {'place':'L25–L27','reading':r'\geqslant3; \underline{L}; n\ne0','decision':'All glyphs read directly; no mathematical correction.'}
 ],
 'spacing_audit':[
  {'place':'L06','result':'Attached morphism( belongs to the uncertain cancelled phrase and is included in R2-01; no duplicate spacing row.'},
  {'place':'L09 insertion','result':'The normality parenthesis is interlinear and attached by a bracket after fibers,. The witnesses\' linearizing blanks around add/inserted do not yield a further visible baseline difference.'},
  {'place':'L14','result':'proofsbeing attached; R2-02.'},
  {'place':'L15','result':'No blank cell between (i) and the first crossed character; R2-04.'},
  {'place':'L18','result':'X,Y has consecutive cells; R2-06.'},
  {'place':'L20','result':'the, f label, colon, both Pic terms, and following is are separated as visibly typed/drawn; no additional spacing difference identified.'},
  {'place':'L22','result':'Visible blank before period; R2-10.'}
 ]
}
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
obs='''# Independent reading R2 — A57-02_57_scan076

Start UTC: 2026-11-20T11:17:48Z. Model identity exposed: GPT-6 Astra Pro. Effort setting: not exposed. Run: /root/p57_076_r2.

## Image discipline

Whole viewed once for layout; half_a and half_b each viewed once at supplied resolution, in that order. Five unresolved places received one tight enlarged crop each, all viewed once. Crops used the supplied Pillow helper, autocontrast, LANCZOS enlargement and unsharp mask; rotation 0 degrees because the local typed baselines were sufficiently level. The report records source boxes, output sizes and scales. No OCR, web, other pages or other reader material was used. No image delivery was lost.

## Ordered coverage

Line IDs count the date and salutation, then each principal typed baseline. Interlinear insertions are attached to their receiving line.

| Line | Direct reading coverage |
|---|---|
| L01 | Hand date: July 18, 1962; no final punctuation added. |
| L02 | My dear Murre, including comma. |
| L03 | I recently had some thought … finiteness conditions for Picard; singular thought. |
| L04 | preschemes, and substantially improved … results stated in the. |
| L05 | last section … last Bourbaki talk. The main result stated there. |
| L06 | for a simple; cancelled phrase; upper typed projective morphism; with connected geometric fibers. Crop 01 retains the cancelled-phrase doubt. |
| L07 | namely parenthesis and pieces formula; capital Pic, raised P, lower X/S; finite type over S; has been. |
| L08 | extended by Mumford … where; cancelled the fibers; instead of f simple. |
| L09 | we assume only f flat … integral geometric fibers, Using his. The typed interlinear normality parenthesis and pen attachment after fibers, are included. |
| L10 | result (the proof of which is quite simple and beautiful), I could. |
| L11 | get rid … normality assumption, and even (as in theorem 4.1. of. |
| L12 | my talk) restrict … two first non trivial. |
| L13 | coefficients … Hilbert polynomials. The key results for the; also present in half_b overlap. |
| L14 | reduction … following (the proofsbeing very technical, and rather; attached proofsbeing. |
| L15 | different for (i) and (ii), except that (ii) uses (i); immediately following cancelled words. Crop 02 retains uncertain and Mumford's and confirms no blank after (i). |
| L16 | to reduce … normal case; moreover (ii) uses Mumford's result. Crop 03 shows the composite first t; uncertain deleted h retained. |
| L17 | and the equivalence criteria as developped in my last Seminar):; both p letters. |
| L18 | (i) Let X,Y … S noetherian, let f:X to Y be a S-morphis; direct arrow, underlined interlinear surjective with attachment, and right-margin handwritten m comma. |
| L19 | crossed m comma before assume for simplicity … Picard preschemes. Crop 05 supports m comma under independent cancellation strokes. |
| L20 | exist, the f with raised mark; Pic Y/S to Pic X/S; is of finite type (and in fact affine. Crop 04 preserves mark alternatives and confirms both subscripts/underlines/arrow. |
| L21 | if S is the spectrum of a field), i.e. a subset M of Pic Y/S is quasi-. |
| L22 | compact iff its image in Pic X/S is .; lexical quasi-compact retained and final blank before period preserved. |
| L23 | (ii) The same conclusion holds … canonical immersion X to Y,; hand right arrow. |
| L24 | if Y/S is projective … fibers all components of which are of. |
| L25 | dimension greater-than-or-equal 3, and if X is the sub-scheme of zeros of a section; oblique lower relation stroke inspected. |
| L26 | over Y of an invertible sheaf underlined L ample with respect to S. |
| L27 | A connected result is that for any X/S proper, and integer n not-equal 0,; final comma and hand relation preserved. |
| Margin | Pencil 75 at bottom left; archive comment. No authored page number, signature, closing, separate diagram, drawing or display. |

## Decisions and limits

The complete proposed reading retains C's text. All four actual C uncertainty macros remain, each after its designated crop. The cancelled initial phrase favors C's proposed morphism(with X/Y prjt over H's morphism (namely that, but the obscured capital and ending remain open. The name in the second cancellation, the overtyped h, and the raised f mark also remain uncertain. The crossed line-opening m comma is legible enough to transcribe at medium confidence.

The report records ten H comparison rows, including retained uncertainty versus H's confident readings, attached proofsbeing, adjacency after (i), X,Y spacing, surjective underlining, the omitted underlying h, the readable cancelled m comma, and is space period. Pagination is explicitly collated in notes: H page 75 corresponds to scan 76; the visible pencil 75 is an archive number.

No mathematical statement was proved, refuted, computed or used to decide a glyph; check_events is empty. The summary attributes the mathematical claims to the page.
'''
(base/'observations.md').write_text(obs)
print(json.dumps({'reading':str(base/'reading.tex'),'observations':str(base/'observations.md'),'report':str(base/'report.json'),'changes':len(changes),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),'crops':len(crops),'all_lines_read':report['coverage']['all_lines_read']},indent=2))
