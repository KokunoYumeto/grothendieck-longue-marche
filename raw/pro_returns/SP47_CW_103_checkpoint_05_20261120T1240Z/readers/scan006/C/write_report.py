from pathlib import Path
import json
from datetime import datetime,timezone
root=Path('/workspace/scratch/ae626167fbca/SP47_CW_103_work/readers/scan006/C')
viewlog=json.loads((root/'view_log.json').read_text())
crops=json.loads((root/'crop_manifest.json').read_text())
cv={v['id']:v for v in viewlog['crop_viewed']}
readings={
'c01_page_number':'No decipherable numeral is first reading. There is a shallow dark blot with faint detached traces above; a 5 is possible but cannot be established from its strokes. The sequence of other pages was not used to choose a digit.',
'c02_FX_overwrite':'An upper closed rounded bowl remains to the right of the stem, with the F bars also present. Read the cancelled underletter as P, then live F(X); the C P|F doubt is resolved in favour of P, with medium confidence.',
'c03_de_overwrite':'Live de is clear. Extra vertical and top strokes inside/left of the d and thickened e support an overwritten le, but a displaced second de impression is also possible. Read deleted le|de, then live de.',
'c04_K_corrections':'Both lower digits are cancelled: a closed lower 0 under the first K and a footed lower 1 under the second. Live upper 0 and 1 are visible. At the second upper 1, the preceding line’s pi_1 subscript meets the numeral. Primary reading: no separately identifiable cancelled upper numeral; alternatives remain an earlier cancelled 0 or 1. This is a visual overlap assessment, not an inference from the intended degree.',
'c05_somme_punctuation':'Comma. The mark has a broad head at the upper right and a narrowing extension toward the lower left, below the parenthesis. The following capital Cela did not determine this reading.',
'c06_netant_overwrite':'Live hand ét before typed ant is clear. Several old curved and upright type impressions remain; est is plausible, but the complete old word cannot be separated confidently. Retain deleted unsure est.',
'c07_two_high_marks':'Two distinct high impressions survive after à: a small left wedge/curl and a rounder right dot. Diaeresis is the first reading, with paired quotation strokes still possible. Retain the C doubt rather than omit the marks.',
'c08_developpements':'The corrected letter has the high ascender of b and an additional mid-height n-like shoulder/serif. Read the old b cancelled beneath live n, as C does; H omits that underletter.',
'c09_bottom_overwrite':'Live autre is overtyped within the cancelled paragraph. An earlier d-like ascender and further crowded lower letters remain under it. The complete older word is not secure; retain deleted unsure dans inside the globally deleted paragraph.',
'c10_inversib_break':'A dark, approximately round mark survives after b at mid-height; no extended horizontal shaft is visible, and the right edge is not clipping the mark. A weak line-end hyphen is possible, but the visible remnant is dot-shaped. Preserve dot|hyphen uncertainty at the source break before next-line le.'
}
for c in crops:
 c['reading']=readings[c['id']]
 c['viewed_utc']=cv[c['id']]['opened_utc']
changes=[]
def change(place,c,h,reading,shows,confidence,kind,ac,ah,ids=()):
 changes.append({'place':place,'c':c,'h':h,'reading':reading,'scan_shows':shows,'confidence':confidence,'kind':kind,'marked_in_H':False,'against_c':ac,'against_h':ah,'crop_ids':list(ids)})
change('Upper centre, putative manuscript page number',r'\mspage{\unsure{5}}',r'\page{5} (page metadata; also credits the clearly written archive 5)',r'\mspage{\unsure{\phantom{5}|5}}','The crop shows a shallow dark shape and detached faint traces, without a complete distinguishable numeral. No readable number is primary; 5 remains possible. No H omission is charged for the archive number.','low','other',True,False,['c01_page_number'])
change('Opening explanation, F(X)',r'\deleted{\unsure{P|F}}F(X)','F(X)',r'\deleted{P}F(X)','The upper-right old impression forms a closed rounded P-like bowl. Live F bars and its stem remain visible. This is an overtyped ordinary capital, not a doubled alphabet.','medium','omission',True,True,['c02_FX_overwrite'])
change('Opening explanation, line end inversib / next-line le','inversible','inversible',r'inversib\unsure{\textperiodcentered|-}le','After the b there is a compact dark mid-height dot-like mark. There is space to its right and no evident extended horizontal hyphen shaft. The next source line starts le. A damaged or weak line-break hyphen remains an alternative.','low','misread symbol or index',True,True,['c10_inversib_break'])
change('First quoted expression, catégorie de Picard enveloppante',"``catégorie de Picard enveloppante''",'« catégorie de Picard enveloppante »',"``catégorie de Picard enveloppante''",'Half a settled this difference: both quotation boundaries have paired high straight typewriter strokes, not angle-shaped guillemets. No reader crop was needed; the main reader still needs its adjudication crop.','high','other',False,True)
change('Les invariants pi_0 et pi_1, before de cette',r'\deleted{\unsure{le}}de','de',r'\deleted{\unsure{le|de}}de','Extra internal vertical/top strokes accompany the live d, and e is also overstruck. Underlying le is plausible; a displaced prior de cannot be excluded. The former word remains uncertain, with an added alternative to C.','low','omission',True,True,['c03_de_overwrite'])
change('Méritent la notation, first K(C)',r'K^{0}_{\deleted{0}}(C)','K^0(C)',r'K^{0}_{\deleted{0}}(C)','The first K has a cancelled low closed 0 plus a separate live raised 0. Its plain K stem is not double-struck. Half a already established the low cancellation; the same strokes are included as context in c04.','high','omission',False,True,['c04_K_corrections'])
change('Méritent la notation, second K(C)',r'K^{\deleted{\unsure{0|1}}1}_{\deleted{1}}(C)','K^1(C)',r'K^{\unsure{1|\deleted{0}1|\deleted{1}1}}_{\deleted{1}}(C)','A low footed 1 is cancelled and a live raised 1 is clear. The crowded strokes above are also in contact with the preceding line’s pi_1 subscript. No independent old upper numeral is primary; an overtyped upper 0 or 1 is retained as an alternative, rather than inferred from the mathematical expectation.','medium','omission',True,True,['c04_K_corrections'])
change('Munie de la l’opération somme, cancelled la',r'de \deleted{\rlap{xx}la} l’opération','de l’opération',r'de \deleted{\rlap{xx}la} l’opération','Half a settled this difference: readable l and a remain beneath two crossing typewriter cancellation impressions before the live l’opération. H leaves out the cancelled word.','high','omission',False,True)
change('After somme), before Cela',r')\unsure{.|,} Cela','). Cela',r'), Cela','A broad comma head and downward-left tail are visible below and to the right of the parenthesis. The final reading preserves the following capital Cela.','high','misread symbol or index',True,True,['c05_somme_punctuation'])
change('Quoted expression catégorie stabilisée',"``catégorie stabilisée''",'« catégorie stabilisée »',"``catégorie stabilisée''",'Half a settled this difference: the source uses pairs of high straight quotation strokes on both sides. H replaces them with guillemets.','high','other',False,True)
change('After l’anneau A), n’étant correction',r"n'\deleted{\unsure{est}}\handwritten{ét}ant","n'étant",r"n'\deleted{\unsure{est}}\handwritten{ét}ant",'Live pen ét is superposed on several older typewriter impressions before ant. The underlying curved and upright strokes allow est but do not resolve all three letters. C’s exact doubt is retained; H omits the underlayer.','low','omission',False,True,['c06_netant_overwrite'])
change('After H_1(K_bullet)=K^1, before puisqu’une','-','---','-','Half b settled this difference: a single short horizontal typewriter hyphen occupies the separation before puisque. It is not an em-length drawn stroke.','high','other',False,True)
change('Final live paragraph, first occurrence of interprétation','interprétation','interpétation','interprétation','Half b settled this difference: the typed r after p and before é is present. The complete word is interprétation. No crop was needed to decide it in this reading.','high','misread word',False,True)
change('Final paragraph, after est à and before chercher',r"à\unsure{\textasciidieresis|''} chercher",'à chercher',r"à\unsure{\textasciidieresis|''} chercher",'Two high marks lie between the accented à and chercher. Their small dot/wedge outlines leave diaeresis versus quotation strokes unresolved. They are not the grave accent of à, which is separately visible to the left.','low','omission',False,True,['c07_two_high_marks'])
change('Quoted homotopiques, spanning source line break',"``homotopiques''",'« homotopiques »',"``homotopiques''",'Half b settled this difference: paired high straight strokes occur before homotopi- and after ques. The line-break hyphen was joined, while the quotation form was preserved.','high','other',False,True)
change('Final live line, développements',r'développeme\deleted{b}nts','développements',r'développeme\deleted{b}nts','The letter before ts retains a b ascender and an additional n-like shoulder at x-height. This is an ordinary overwritten letter, not a new spelling silently supplied. Read old b cancelled beneath live n.','medium','omission',False,True,['c08_developpements'])
change('Cancelled final paragraph, after Comme',r'\deleted{Comme \deleted{\unsure{dans}}autre direction ...}',r'\struck{Comme autre direction ...}',r'\deleted{Comme \deleted{\unsure{dans}}autre direction ...}','The whole paragraph is cancelled. Under live autre, the initial old d-like ascender and crowded residual lower shapes survive, but the word dans is not fully separable. C’s doubt is retained. H accurately records the global cancellation but omits the older overwritten word.','low','omission',False,True,['c09_bottom_overwrite'])
unresolved=[
{'place':'Upper-centre putative page number','reading':r'\mspage{\unsure{\phantom{5}|5}}','alternatives':['no decipherable numeral','5'],'confidence':'low','evidence':'c01: dark shallow blot and detached faint traces. A complete 5 cannot be established. Page sequence was not used as ink evidence.'},
{'place':'Opening inversib / le line break','reading':r'inversib\unsure{\textperiodcentered|-}le','alternatives':['mid-height dot-like mark','weak or damaged line-break hyphen'],'confidence':'low','evidence':'c10: round dark remnant at mid-height with no surviving extended shaft; margin does not clip it. Next source line begins le.'},
{'place':'Underlying word before live de cette','reading':r'\deleted{\unsure{le|de}}de','alternatives':['le','displaced prior de'],'confidence':'low','evidence':'c03: internal vertical strokes and top impression inside live d, plus thickened e. The underlayer is not cleanly separated.'},
{'place':'Second K(C), possible older upper digit','reading':r'K^{\unsure{1|\deleted{0}1|\deleted{1}1}}_{\deleted{1}}(C)','alternatives':['live upper 1 with no identifiable cancelled upper numeral','cancelled upper 0 beneath live 1','cancelled upper 1 beneath live 1'],'confidence':'medium','evidence':'c04: the preceding line’s low pi_1 numeral meets the raised K degree. The final high 1 and cancelled low 1 are clear; any independent older upper glyph is not.'},
{'place':'Underlying type in n’étant','reading':r"n'\deleted{\unsure{est}}\handwritten{ét}ant",'alternatives':['est','older letters not fully recoverable'],'confidence':'low','evidence':'c06: curved lower impressions and old uprights are obscured by hand ét and adjacent ant.'},
{'place':'Two high marks between à and chercher','reading':r"à\unsure{\textasciidieresis|''} chercher",'alternatives':['diaeresis-like paired dots','paired quotation strokes'],'confidence':'low','evidence':'c07: two distinct compact high impressions, separate from the à grave accent. Neither reading can be fully established.'},
{'place':'Earlier word under autre in cancelled block','reading':r'\deleted{\unsure{dans}}autre','alternatives':['dans','underword not fully recoverable'],'confidence':'low','evidence':'c09: d-like initial ascender and crowded residual shapes survive, but the long cancellation and overtyping prevent a secure whole-word reading.'}
]
inventory=[]
def item(element,kind,position,first,hand='typewriter'):
 inventory.append({'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
item('Putative manuscript number / indistinct upper-centre mark','text','top centre','no decipherable numeral | 5','unnamed hand, if the faint trace is writing; attribution not established')
item('Opening Hom formula','display','upper centre',r'\underline{Hom}_{\otimes AUC}(S^{-1}C,G) to \underline{Hom}^{S}_{\otimes AUC}(C,G)')
item('Display rightward arrow','insertion','between the two Hom terms','plain rightward arrow','unnamed hand (pen)')
item('First Hom underline','insertion','under first Hom','single line beneath Hom only','unnamed hand (pen)')
item('Second Hom underline','insertion','under second Hom','single line beneath Hom only','unnamed hand (pen)')
item('Opening explanatory parenthesis and assertion','text','below display',"(où l’exposant S dans le deuxième membre ...")
item('Inline F:C to G arrow','insertion','opening explanation','C to G','unnamed hand (pen)')
item('Membership sign','insertion','opening explanation, X before Ob S','X in Ob S','unnamed hand (pen)')
item('Old P under F(X)','deletion','opening explanation','P')
item('Live F over P','insertion','opening explanation','F(X)')
item('Small line-end dot/hyphen remnant','text','after inversib, before next-line le','mid-height mark')
item('Isomorphisme underline','insertion','end of opening explanation','isomorphisme','unnamed hand (pen)')
item('De catégories underline','insertion','end of opening explanation','de catégories','unnamed hand (pen)')
item('Long main prose paragraph with all inline formulas','text','from Nous to invariants seraient K^0 et K^1',"Nous n’explicitons pas ici la construction")
item('Cancelled et with x-mask','deletion','after pas à pas,','et beneath xx')
item('Typed interlinear avec','insertion','above cancelled et, before la vérification','avec')
item('Avec attachment hook','insertion','at cancelled et / la vérification','hook attaching interlinear avec','unnamed hand (pen)')
item('Pi in first invariant','insertion','Les invariants, before low 0','pi_0','unnamed hand (pen)')
item('Pi in second invariant','insertion','Les invariants, before low 1','pi_1','unnamed hand (pen)')
item('Overwritten le or de','deletion','before cette catégorie enveloppante','le | de')
item('Live de replacement','insertion','before cette catégorie enveloppante','de')
item('First K old low 0','deletion','méritent la notation, first K(C)','cancelled subscript 0')
item('First K live high 0','insertion','méritent la notation, first K(C)','raised 0')
item('Second K old low 1','deletion','méritent la notation, second K(C)','cancelled subscript 1')
item('Second K live high 1 and uncertainty about older upper impression','insertion','méritent la notation, second K(C)','high 1; possible older cancelled 0 or 1 encoded as alternatives')
item('Inserted operation phrase','insertion','after un anneau A,','avec l’opération de somme,')
item('Operation-phrase insertion connector','insertion','below inserted phrase, attached after A,','curved insertion hook and connecting line','unnamed hand (pen)')
item('Cancelled la with x-mask','deletion','munie de, before l’opération somme','la beneath xx')
item('Comma after somme)','text','right end of munie ... line','),')
item('Added opening parenthesis','insertion','before de la catégorie additive C','(','unnamed hand (pen)')
item('Added closing parenthesis','insertion','after de la catégorie additive C',')','unnamed hand (pen)')
item('Older type under ét','deletion','after l’anneau A), n’','est, uncertain')
item('Hand replacement ét','insertion','after n’ and before ant','ét','unnamed hand (pen)')
item('First stricte underline','insertion','catégorie de Picard stricte, ces considérations','stricte','unnamed hand (pen)')
item('Inline H/K equalities','text','complexe de chaines satisfaisant','H_0(K_bullet)=K^0, H_1(K_bullet)=K^1')
item('Second stricte underline','insertion','Picard stricte canonique','stricte','unnamed hand (pen)')
item('Final live prose paragraph and all inline formulas','text','lower body',"On peut difficilement échapper à la question d’une interprétation")
item('Two high marks after à','text','final paragraph, before chercher','diaeresis-like marks | double quote','typewriter or unidentified mark layer; origin not secure')
item('Pi in final homotopiques formula','insertion','after homotopiques, before low i','pi_i','unnamed hand (pen)')
item('Old b in développements','deletion','last live line','b')
item('Live n over b','insertion','last live line','n')
item('Interrupted live ending','text','last live line, right edge','obligerai-')
item('Final cancelled prose block, all three lines','text','bottom body','Comme autre direction de recherche ouverte ... néces-')
item('Cancellation of final paragraph','deletion','across final three-line block','enclosing and looping/sloping strokes','unnamed hand (pen)')
item('Earlier word under autre','deletion','cancelled paragraph, after Comme','dans, uncertain')
item('Overtyped autre','insertion','cancelled paragraph, after Comme','autre')
item('Archive sheet number','text','bottom left','5','unnamed hand (pencil-like line)')
notation=[]
def notation_item(place,sign,ink,latex):
 notation.append({'place':place,'sign':sign,'ink':ink,'latex':latex})
notation_item('Opening display, both terms','underlined Hom with lower tensor AUC','Each Hom has a plain serif H with one identifiable letter impression and one underline under the name. Tensor and AUC stand low; only the second term has raised S.',r'\underline{\mathrm{Hom}}_{\otimes\mathrm{AUC}}; \underline{\mathrm{Hom}}_{\otimes\mathrm{AUC}}^S')
notation_item('Display and main prose','S inverse exponent','Both S^{-1}C expressions show a raised minus and raised 1, followed by baseline C.',r'S^{-1}C')
notation_item('Opening display and F:C to G','rightward arrows','Each hand arrow has a horizontal shaft and a head at the right, with no start bar.',r'\handwritten{\longrightarrow}')
notation_item('Every tensor occurrence','circled cross','All seven signs were checked: two Hom subscripts, the initial foncteurs prefix, two final live category prefixes, and two cancelled category prefixes. The outline is round with interior crossing strokes.',r'\otimes')
notation_item('Opening explanation','membership and Ob','The sign after X has an open curved body and a middle stroke. Ob is upright, followed by S.',r'X\handwritten{\in}\mathrm{Ob}\ S')
notation_item('F(X)','overtyped ordinary F/P','The composite includes a closed P-like upper bowl and live F bars. No special bold or blackboard alphabet is indicated.',r'\deleted{P}F(X)')
notation_item('Les invariants and final homotopiques expression','pi and indices','All three pi signs have a pen top bridge and descending legs. The 0 and 1 in the main paragraph and the dotted i in the final paragraph are low-right.',r'\handwritten{\pi}_0,\ \handwritten{\pi}_1,\ \handwritten{\pi}_i')
notation_item('First K pair','former low degrees and live high degrees','Both lower digits are cancelled. The first live upper degree is a closed 0; the second is a footed 1. Its encounter with the preceding line’s pi_1 creates the reported upper-layer uncertainty.',r'K^0_{\deleted{0}}(C),\ K^{\unsure{1|\deleted{0}1|\deleted{1}1}}_{\deleted{1}}(C)')
notation_item('All later invariant K expressions','raised degrees','The projective-module K pair, the Cela pair, the equality right sides, and the final main-paragraph pair all have high 0 and 1. Both final-paragraph i marks are high and dotted.',r'K^0(A),K^1(A);\ K^0,K^1;\ K^i')
notation_item('Complexe de chaines satisfaisant','H low indices and K low dots','H_0 and H_1 have low 0 and 1. In both parenthesized complexes, the solid dot lies low-right of K. The equals signs each have two horizontal strokes.',r'H_0(K_\bullet)=K^0,\ H_1(K_\bullet)=K^1')
notation_item('All capital mathematical letters','ordinary alphabet','C, G, S, F, X, A, K and H keep typewriter serifs and ordinary single-letter identities. Local overtyping is preserved separately; no bold or double-struck alphabet is supplied.',r'C,G,S,F,X,A,K,H')
notation_item('AUC and AU occurrences','letter order','Both Hom subscripts and the three live prose AUC occurrences have A then U then C. The cancelled final block has AU without C.',r'\mathrm{AUC};\ \mathrm{AU}')
notation_item('Final live paragraph','n category prefixes','n is a baseline mathematical letter. In the second parenthesis it follows a tensor sign and a hyphen. Nothing is promoted to an exponent.',r'n\text{-catégories};\ \otimes\text{-}n\text{-catégorie}')
notation_item('Opening assertion and two stricte occurrences','underlining','The assertion has one line under isomorphisme and a separate line under de catégories. Each later stricte has one underline. No double underline is present.',r'\uline{isomorphisme}\ \uline{de catégories};\ \uline{stricte}')
notation_item('Three quoted expressions','paired high quotation strokes','The source encloses catégorie de Picard enveloppante, catégorie stabilisée, and homotopiques with pairs of high typewriter strokes.',"``...''")
notation_item('De la catégorie additive C','hand-added parentheses','Two larger pen curves surround the existing typewritten phrase. The following comma remains outside the closing curve.',r'\handwritten{(}de la catégorie additive $C$\handwritten{)},')
notation_item('Signalons seulement que, cette','comma','A low comma occurs after que before cette. Both witnesses preserve it; the unusual syntax was not repaired.','que, cette')
notation_item('Complexe de chaines','absence of circumflex','The i has its ordinary dot; no circumflex is visible above it.','chaines')
notation_item('Before puisqu’une','short dash','A single short horizontal typewriter mark separates the formula from puisque.','-')
notation_item('Final paragraph, est à chercher','two raised marks','A separate pair of high dot/wedge shapes follows the grave-accented à; their exact identity remains open.',r"à\unsure{\textasciidieresis|''}")
notation_item('Last live line and cancelled final line','unfinished words at page end','The source visible endings are obligerai- and néces-. No completion from another page was supplied.','obligerai-; néces-')
notation_item('Top and bottom metadata','page marks','The upper-centre trace does not supply a certain numeral. The lower-left archive numeral is a clearly shaped 5.',r'\mspage{\unsure{\phantom{5}|5}}; % archive sheet number: 5')
notes=[
'The brief v05, source_paths.json, notation_snapshot.md, PREAMBLE.tex, C_alerts.md, and both assigned witnesses were read. Only scan006 images and this reader’s own crops were opened. No other reader material, records directory, other scan, external source, OCR, text recognition, or PDF text layer was used. There was no delegation.',
'Coverage: the whole page was opened once for layout, then supplied half_a once and half_b once in that order. Every text block, including all three lines of the cancelled bottom paragraph, every word and ending, accent, abbreviation, punctuation sign, and every inline and displayed mathematical expression was compared visually against both C and H, including agreements. This is a coverage statement, not a mathematical proof check.',
'Ten unresolved loci were identified after the halves. One tight crop was made for each, enlarged to 3000 pixels across with PIL LANCZOS, autocontrasted, sharpened, and viewed once. No whole half was enlarged again and no locus was recropped. Crop c04 includes the first K and the preceding line’s pi_1 as context for the second K upper-layer doubt. All crop view times are actual tool-invocation timestamps.',
'The start_utc field records the first instrumented timestamp at packet intake, immediately after the brief was read. Whole, half, and crop opening times were captured as those view calls were made. The end time is the actual report-writing time; no durations of mathematical activity are invented.',
'The page states that the displayed map between the two underlined Hom expressions is an isomorphisme de catégories and explains the raised S by an invertibility condition. It expressly does not give the construction and calls the compatibility verification long and tedious. Reading those claims was not counted as checking them.',
'The main paragraph names the enveloping Picard category when S contains all objects and calls its invariants K^0 and K^1. It gives the finite projective module example and describes the extension to any additive C with the tentative words sans doute. These are reported as statements on the page, not as results independently established in this run.',
'The text says the stabilized category is practically never stricte and says this makes a canonical complex satisfying the two written homology equalities seem peu probable. It invokes the théorie de Deligne in explaining that concern. No theorem about this connection was checked here.',
'The final live paragraph asks about geometric interpretations of higher K^i and uses Il y a tout lieu de croire for an interpretation through n-catégories de Picard. The cancelled block starts a distinct research direction about a tensor-category of fractions in the AU setting. The live text ends at obligerai-; the cancelled block ends at néces-. No continuation beyond this scan was inspected or supplied.',
'Ink and expectation were kept separate. In particular, the comma after somme) was read from its head and tail, despite Cela following; the unaccented chaines and comma in que, cette were retained; the extra marks after à were not removed for syntax. The K upper-layer decision is about overlapping strokes, not about which K degree would make mathematical sense.',
'C doubts: the P|F underletter was resolved to P, and .|, after somme) was resolved to comma. The top trace was revised to no decipherable numeral first, with 5 possible; le gained a displaced-de alternative; the second K gained no independent cancelled upper numeral as first alternative. The exact C doubts est, diaeresis|quotation strokes, and dans were retained. An additional line-end dot|hyphen doubt was recorded after inversib.',
'The upper number is not established by consulting the page sequence. The separate archive 5 is clear and is credited to H’s page metadata; no archive-number omission difference is manufactured. There is no visible title, date, signature, or written total page count on this sheet.',
'Hand identification is conservative. Pen corrections, carets, parentheses, pi signs, arrows, underlines and deletion strokes are assigned only to an unnamed hand. The typewritten interlinear avec and avec l’opération de somme, remain typewriter material, although their attachment hooks are hand drawn. Ordinary insertion hooks are represented by inserted at the textual attachment, not by detached drawings.',
'The H emph spans encode the same source underlining, and its add/struck macro names are not counted as differences by themselves. None of the listed loci is explicitly marked doubtful by H, so every marked_in_H flag is false. Its note correctly records that the bottom paragraph is globally cancelled; the omitted older word beneath autre is a separate layer.',
'Differences settled by the halves without a reader crop are expressly identified in changes: the three quotation forms, cancelled la, short dash, and interprétation. The main reader must still make and inspect its own adjudication crop for those differences. Agreed notation is recorded separately instead of creating no-change rows.',
'No mathematical proof, independent re-proof, computation, formal certificate, or previously used theorem check was performed. All formula inspections in this run were visual transcription comparisons, including alphabet, level, indices, exponents, equality signs, tensor signs, arrows and correction layers. Accordingly math_checks is empty.'
]
report={
'scan':6,'reader':'C','start_utc':viewlog['start_utc'],'end_utc':datetime.now(timezone.utc).isoformat(),'model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':viewlog['viewed'],'crops':crops,'changes':changes,'unresolved':unresolved,'inventory':inventory,'notation':notation,
'abbreviations':[
{'form':'Hom','expansion':'Not expanded in prose on this page; retained as the upright name in both underlined expressions.'},
{'form':'Ob','expansion':'objets (contextual expansion; the abbreviation itself is retained).'},
{'form':'AUC','expansion':'Not spelled out on this page; letter order A-U-C is preserved.'},
{'form':'AU','expansion':'Not spelled out on this page; A-U without C is preserved in the cancelled paragraph.'},
{'form':'(Ab)','expansion':'Not spelled out on this page; the parentheses and capitals/lowercase are preserved.'}
],
'notes':notes,'math_checks':[]
}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(root/'report.json'),'reading':str(root/'reading.tex'),'changes':len(changes),'against_c':sum(x['against_c'] for x in changes),'against_h':sum(x['against_h'] for x in changes),'unresolved':len(unresolved),'crops':len(crops),'inventory':len(inventory),'notation':len(notation),'math_checks':0,'end_utc':report['end_utc']},ensure_ascii=False))
