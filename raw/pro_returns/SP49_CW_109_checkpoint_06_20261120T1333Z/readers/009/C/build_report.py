from pathlib import Path
import json
BASE=Path('/workspace/scratch/6d55c8c3e5a7/work/readers/009/C')
SRC='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-01_109_scan009'
A=SRC+'_a.jpg'; B=SRC+'_b.jpg'; W=SRC+'.jpg'
plan=json.loads((BASE/'open_after_halves.json').read_text())
locations={x['id']:x for x in plan}
def loc(crop=None,source=None,bbox=None):
    if crop:
        q=locations[crop]
        return dict(crop='crops/'+crop+'.jpg',source=q['source'],bbox=q['bbox'])
    return dict(crop=None,source=source,bbox=bbox)
changes=[]
def ch(id,place,c,h,reading,dc,dh,kind,evidence,confidence='high',marked=False,crop=None,source=None,bbox=None):
    changes.append(dict(id=id,place=place,c=c,h=h,reading=reading,diff_c=dc,diff_h=dh,kind=kind,marked_in_H=marked,confidence=confidence,evidence=evidence,**loc(crop,source,bbox)))
ch('heading','upper right heading',r'\uline{Terminology}','',r'\uline{Terminology}',False,True,'omission','The word Terminology and a single underline are plainly present. H describes a handwritten underlined title in its note but does not give the title itself.',marked=True,source=A,bbox=[1390,15,1653,90])
ch('first-structure','first entry, after ternary',r'\unsure{structure}','structure','structure',True,False,'other','The crop separates the two t ascenders and compressed ending; the final r/e strokes complete structure. There is no remaining competing word supported by these strokes.',crop='01_structure')
ch('fibre','standard type entry, parenthesis','fibre','fiber','fibre',False,True,'misread word','After the tall b the low r joins the terminal e; the e is not placed before r.',crop='02_fibre')
ch('stacks-cancellation','before n-C-stacks',r'\deleted{\unsure{an|en|n}}',r'\struck{\ill{}}',r'\deleted{\unsure{an|en|n}}',False,True,'readable ink left as \\ill{}','The crossed cluster retains a low terminal n-like arch and a possible initial loop. It supports the listed tentative letters, but cancellation prevents choosing among them. This is a tentative recovery, not a resolved word.',confidence='low',marked=True,crop='03_stacks_deletion')
ch('coherator-capital','Coherator entry','Coherator','coherator','Coherator',False,True,'misread word','The initial open C rises above the following o and is the same capital treatment seen in Cat.',source=A,bbox=[119,273,353,332])
ch('coherator-reference','reference column beside Coherator','13',r'13 \qquad 25','13',False,True,'insertion or placement','The second 13 belongs to Coherator. The 25 is lower in the reference column and belongs to the next Hot-equivalence entry.',source=A,bbox=[1150,235,1260,357])
ch('site-structure','Hot-equivalence entry, last word',r'\unsure{structure|structures}','structure','structure',True,False,'other','The terminal joined wave is the compressed u/r/e ending; no additional s follows it. The crop supports singular structure.',confidence='medium',crop='04_site_structure')
ch('hot-reference','reference beside Hot-equivalence','25',r'26, \emph{39}','25',False,True,'insertion or placement','The 25 stands at the height of Hot-equivalence. A lower leader from test category runs to 26, 39; those numbers do not label Hot-equivalence.',source=A,bbox=[1147,312,1370,421])
ch('test-entries','interlinear test category and following test-topology',r'test category(!) \hrulefill & 26, \uline{39} \\ test-topology & 27',r'test category (!) / test-topology \quad 27',r'test category(!) \hrulefill & 26, \uline{39} \\ test-topology & 27',False,True,'insertion or placement','The raised test category(!) has its own leader to 26 and underlined 39. The next test-topology entry has 27. No slash is drawn between these entries. H notices the raised placement in a note but merges the reference assignment.',marked=True,source=A,bbox=[133,370,1370,492])
ch('canceled-41','above functor, after first modelizer line',r'\deleted{\unsure{41|4}}',r'\struck{\ill{}}',r'\deleted{\uline{41}}',True,True,'readable ink left as \\ill{}','A 4-shaped open angular body is followed by a separate right upright, supporting 41. A heavy horizontal underline remains below the number, and diagonal strokes cancel the cluster. The number is above functor, not ordinary text following modelizing.',confidence='medium',marked=True,crop='05_canceled_reference')
ch('modelizer-brace','right of the two modelizer lines',r'\right\}', '',r'\right\}',False,True,'omission','A right brace joins modelizer/model-preserving and (or modelizing) functor to the reference group 28 with its arrows.',source=A,bbox=[1120,450,1172,568])
ch('basic-quote','start of basic modelizer entry',r"\unsure{'basic|basic}",'basic',"'basic",True,True,'other','A short detached upright precedes the b. It is sufficiently separate from the ascender to retain as a genuine single quote; no closing quote is visible.',source=A,bbox=[104,617,263,681])
ch('elementary-punctuation','after elementary modelizer',r'(\unsure{!|;|!,})','(!)',r'(\unsure{!|;|!,})',False,True,'other','There is a tall upper stroke and a lower dark dot with a long down-left tail. The primary ! agrees with H, but the tail also permits a semicolon or an added comma; H does not mark that uncertainty.',confidence='low',crop='06_elementary_punctuation')
ch('raised-29','reference to basic/elementary modelizer',r'$29^{\unsure{7|+}}$','29*','$29^7$',True,True,'misread symbol or index','The raised sign has a distinct top horizontal, a descending stem, and a small cross-stroke midway down. Those are the strokes of a crossed 7, not a plus or asterisk.',crop='07_raised_29')
ch('basic-group','grouping of basic and elementary modelizer',r'\left.\begin{array}{l}\text{basic modelizer (Cat)}\\\text{elementary modelizer(!)}\end{array}\right)', 'basic modelizer (Cat) / elementary modelizer (!)',r'\left.\begin{array}{l}\text{basic modelizer (Cat)}\\\text{elementary modelizer(!)}\end{array}\right)',False,True,'insertion or placement','A tall right parenthesis joins the two lines to the one reference 29 with raised 7. There is no slash between them. Quote and punctuation decisions are separate loci.',source=A,bbox=[819,590,895,760])
ch('strict-capital','Strict test. category entry',r'\uline{Strict}',r'\emph{strict}',r'\uline{Strict}',False,True,'misread word','The initial S is a full-height capital. H emph is accepted as encoding the visible single underline; the discrepancy is capitalization only.',source=A,bbox=[125,752,303,838])
ch('test-period','word test in Strict test. category',r'\unsure{test.|test}','test','test.',True,True,'other','The half shows a distinct small dot just to the right of the final t; it is retained as the written full stop.',source=A,bbox=[333,746,455,813])
ch('strict-cancellation','after Strict test. category',r'\deleted{\unsure{(!)|!|4.}}',r'\struck{\ill{}}',r'\deleted{\unsure{(!)|!|4.}}',False,True,'readable ink left as \\ill{}','A left curved stroke, an upright, and a lower dot survive diagonal hatching. They allow parenthesized exclamation, exclamation, or a 4-like form plus dot; the cancellation prevents a secure choice.',confidence='low',marked=True,crop='08_strict_deletion')
ch('simplices-cubes','standard simplices and indented cubes',r'standard simplices\quad\textemdash\ \textemdash\ \hrulefill \\ cubes','standard simplices / cubes',r'standard simplices\quad\textemdash\ \textemdash\ \hrulefill \\ cubes',False,True,'drawing or diagram','After simplices are two short horizontal dashes and a longer thin leader. Cubes is on the following indented line. No slash separates the words.',source=A,bbox=[130,827,1140,961])
ch('canceled-square-drawings','two small drawings below cubes','TikZ drawing of two squares, inner strokes and cancellation strokes',r'\struck{$\square$, $\square$}','TikZ drawing of two squares, inner strokes and cancellation strokes',False,True,'drawing or diagram','The ink contains two distinct rough square forms separated by a comma, with internal vertical strokes and different diagonal/looping cancellation strokes. C already reproduces those strokes and is retained. H reduces these to two square glyphs, although its note correctly calls them canceled.',marked=True,crop='09_square_drawings')
ch('canceled-34','reference at right of the square drawings',r'\deleted{34}','34',r'\deleted{34}',False,True,'deletion state (struck given live or live given struck)','A heavy near-horizontal stroke cuts through 34. It is not the live 34 written one row higher beside cubes.',source=A,bbox=[1146,935,1246,1003])
ch('map-insertion','aspheric entry, above the end of its parenthesis',r'\inserted{map of objects}','map of objects',r'\inserted{map of objects}',False,True,'insertion or placement','Map of objects is written above the line. The curved line underneath it returns to the comma before the existing closing parenthesis and acts as an insertion connector. The added phrase is not underlined.',crop='10_aspheric_insertion')
ch('aspheric-group','grouping of aspheric and locally aspheric lines',r'\right) & 35','aspheric ... 35; locally aspheric ...',r'\right) & 35',False,True,'insertion or placement','A tall curved rule at the right joins the aspheric line and locally aspheric line to 35. H splits them and leaves the latter line without the grouping mark.',source=A,bbox=[1067,1015,1242,1194])
ch('aspheric-underline','locally aspheric entry',r'locally \uline{aspheric topos, tot.\ asph.\ topos}',r'locally aspheric topos, tot.\ asph.\ topos',r'locally \uline{aspheric topos, tot.\ asph.\ topos}',False,True,'omission','The long thin underline begins beneath aspheric, continues beneath topos and tot. asph. topos, and curves downward to the right. Locally is not included in it.',source=A,bbox=[360,1091,1231,1215])
ch('weak-heading','Weak equivalence entry',r'\uline{Weak equivalence}','weak equivalence',r'\uline{Weak equivalence}',False,True,'other','Weak begins with a capital W, and a heavy single underline sits below the two words. H has neither the capitalization nor an underline encoding here.',source=B,bbox=[100,96,553,225])
ch('weak-connector','between X and Y in weak equivalence',r'X\mathrel{\unsure{-|\to}}Y',r'X \to Y',r'X\mathrel{\unsure{-|\to}}Y',False,True,'other','The stroke is horizontal and ends in a small downward thickened tip. A complete two-sided arrowhead is not visible. Dash remains first, with a minimally drawn right arrow still possible; H presents an arrow without doubt.',confidence='medium',crop='11_weak_formula')
ch('weak-abbreviation','immediately after Y',r'\unsure{m};','map','m;',True,True,'abbreviation expanded or spelling modernised','The crop shows a small low m-shaped wave followed by a dot and a separate tailed lower stroke, hence m;. There is no a/p sequence or p descender such as the one in the added map of objects phrase.',confidence='medium',crop='11_weak_formula')
ch('weak-closing-parenthesis','end of weak equivalence phrase','of topos','of topos)','of topos',False,True,'text not on the page','The phrase ends with topos and blank space; the initial left parenthesis before f is unmatched. The right parenthesis in H has no visible counterpart.',crop='11_weak_formula')
ch('strict-reference-stop','reference beside [strict] elementary modelizer','39.','39','39.',False,True,'omission','The crop shows a discrete ink dot just to the right of the body of 9, above its long descender. It is positioned as a full stop.',crop='13_strict_reference')
ch('local-accent','local test catégory entry',r'\unsure{catégory|category}','category','catégory',True,True,'misread word','A detached rising stroke with a small return at its top is plainly present above the e/g join. It is read as an acute accent on e; the English spelling is not normalized.',confidence='medium',crop='12_local_accent')
ch('local-group','local test catégory and local el. modelizer',r'\left.\begin{array}{l}\text{local test catégory}\\\text{local el. modelizer}\end{array}\right) & 39','local test category / local el. modelizer 39',r'\left.\begin{array}{l}\text{local test catégory}\\\text{local el. modelizer}\end{array}\right) & 39',False,True,'insertion or placement','The lines are joined by a right parenthesis before 39. No slash is present between the two terms.',source=B,bbox=[850,388,1007,529])

doubts=[]
def doubt(place,c,reading,resolved,evidence,confidence='high',crop=None,source=None,bbox=None):
    doubts.append(dict(place=place,c=c,reading=reading,resolved=resolved,confidence=confidence,evidence=evidence,**loc(crop,source,bbox)))
doubt('first entry, after ternary',r'\unsure{structure}','structure',True,'Compressed but continuous structure ending, with no competing surviving word.',crop='01_structure')
doubt('stacks entry, canceled text before n-C',r'\deleted{\unsure{an|en|n}}',r'\deleted{\unsure{an|en|n}}',False,'Dense crossing leaves a possible first loop and final n-like arch. The initial letter cannot be separated securely from cancellation.',confidence='low',crop='03_stacks_deletion')
doubt('Hot-equivalence, after site',r'\unsure{structure|structures}','structure',True,'The final wave is the r/e ending; no further terminal s is distinguishable.',confidence='medium',crop='04_site_structure')
doubt('canceled reference above functor',r'\deleted{\unsure{41|4}}',r'\deleted{\uline{41}}',True,'The open angular 4 is followed by a distinct right upright, and a horizontal underline remains below the canceled number.',confidence='medium',crop='05_canceled_reference')
doubt('before basic modelizer',r"\unsure{'basic|basic}","'basic",True,'A separate short upright appears before b; retain the single quote and do not supply a closing mate.',source=A,bbox=[104,617,263,681])
doubt('punctuation after elementary modelizer',r'\unsure{!|;|!,}',r'\unsure{!|;|!,}',False,'The upper stroke is long, favoring !, but the lower dot has a substantial comma-like tail. All three supplied alternatives remain possible.',confidence='low',crop='06_elementary_punctuation')
doubt('raised sign following 29',r'29^{\unsure{7|+}}','29^7',True,'Separate top horizontal plus descending stem and middle cross-stroke decide a crossed 7.',crop='07_raised_29')
doubt('Strict entry, word test',r'\unsure{test.|test}','test.',True,'A distinct dot is adjacent to the end of t in the half; this was settled before crops.',source=A,bbox=[333,746,455,813])
doubt('Strict entry, canceled final punctuation',r'\deleted{\unsure{(!)|!|4.}}',r'\deleted{\unsure{(!)|!|4.}}',False,'The left curve and lower dot survive, but the intervening strokes are dominated by cancellation. Parenthesized ! is first without excluding ! or 4.',confidence='low',crop='08_strict_deletion')
doubt('Weak equivalence, X to Y connector',r'\mathrel{\unsure{-|\to}}',r'\mathrel{\unsure{-|\to}}',False,'Only a horizontal line and a short downturned thickened right end are visible; this does not securely distinguish dash from a one-barb arrow.',confidence='medium',crop='11_weak_formula')
doubt('Weak equivalence, immediately after Y',r'\unsure{m};','m;',True,'A compressed low m is followed by a discrete two-part semicolon. No p descender is present, so H map cannot stand as written.',confidence='medium',crop='11_weak_formula')
doubt('local test catégory',r'\unsure{catégory|category}','catégory',True,'The raised mark is separate from the word and rises to the right, supporting the acute accent. It is not erased or crossed.',confidence='medium',crop='12_local_accent')

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('01','text','upper right','Terminology, single underline')
inv('02','text','top line, left through middle; reference 4. at right','primary, secondary, ternary... structure')
inv('02a','insertion','above the beginning of 02, connected down before primary','primitive,')
inv('03','text','second entry; reference 5.','standard type (iterated fibre products of)')
inv('04','text','third entry; reference 13.','n-stacks, infinity-stacks, n-underlined-C-stacks')
inv('04a','deletion','inside 04 before n-C-stacks','an/en/n, canceled')
inv('05','text','below stacks; reference 13','Coherator')
inv('06','text','below Coherator; reference 25','Hot-equivalence of site structure')
inv('07','text','raised/interlinear entry between 06 and 08, indented; references 26, underlined 39','test category(!), horizontal leader')
inv('08','text','next line at main left margin; reference 27','test-topology')
inv('09','text','modelizer group, first line','modelizer !/ model-preserving')
inv('09a','text','modelizer group, second indented line','(or modelizing) functor !')
inv('09b','deletion','above functor at end of the first line','underlined 41, heavily canceled')
inv('09c','drawing','right of the two modelizer lines','right brace grouping the two lines')
inv('09d','diagram','reference column beside modelizer brace','28 with separate up-right and down-right arrows to underlined 41 and underlined 42')
inv('10','text','next two-line group, first line',"'basic modelizer (Cat)")
inv('11','text','second line of 10 group','elementary modelizer(!/;/!,)')
inv('11a','drawing','right of 10 and 11','tall right parenthesis; reference 29 with raised crossed 7')
inv('12','text','following line; references 33, 39','underlined Strict test. category')
inv('12a','deletion','after category in 12','canceled (!)/!/4.')
inv('13','text','next entry, first line','standard simplices, two short dashes and a long leader')
inv('14','text','indented line below 13; reference 34','cubes')
inv('15a','drawing','below cubes, left of a comma','first roughly square outline, inner vertical stroke')
inv('15b','deletion','on first square','diagonal cancellation strokes through the square; drawn directly in TikZ')
inv('15c','text','between the two square drawings','comma')
inv('15d','drawing','right of the comma','second roughly square outline with inner vertical stroke')
inv('15e','deletion','on and above second square','large looping and diagonal cancellation strokes; drawn directly in TikZ')
inv('15f','deletion','reference column beside the square drawings','34 crossed through')
inv('16','text','below square drawings, first line of aspheric group','aspheric (topos, object of topos, ...)')
inv('16a','insertion','above the end of 16, returning by a curved pointer to the comma','map of objects')
inv('17','text','second line of aspheric group','locally aspheric topos, tot. asph. topos; underline begins after locally')
inv('17a','drawing','right of 16 and 17','curved grouping rule with shared reference 35')
inv('18','text','following line; reference is a question mark','underlined Weak equivalence (f:X—Y m; of topos, without a closing parenthesis')
inv('19','text','next entry; reference 37','homotopy interval')
inv('20','text','below homotopy interval; reference 39.','[strict] elementary modelizer')
inv('21','text','penultimate group, first line','local test catégory')
inv('22','text','penultimate group, second line','local el. modelizer')
inv('22a','drawing','right of 21 and 22','right parenthesis joining the two lines to 39')
inv('23','text','last terminology entry; reference 39','[locally] modelizing topos')
inv('24','margin note','bottom left corner, separate from text','archive sheet number 8; retained only as a LaTeX comment','another unnamed hand (archive pencil)')

report=dict(
 scan=9,reader='C',model='GPT-6 Astra Pro',effort='not exposed',viewed=[W,A,B],
 layout='A single handwritten terminology index. The underlined heading is at the upper right. Terms occupy the left and middle, with a loose column of page references at the right. The upper entries are crowded: primitive is added over primary, and test category occupies an interline with its own leader and references. Modelizer spans two lines joined by a brace; its reference 28 forks by arrows to separately underlined 41 and 42. A right parenthesis groups the basic/elementary terms, and further curved grouping rules join the two aspheric lines and the two local-modelizer lines. Two small square drawings below cubes are canceled, as is their reference 34. Map of objects is an addition above the aspheric entry with a curved insertion pointer. Single underlines mark Terminology, 39 by test category, 41 and 42 in the fork, Strict, the phrase after locally in the aspheric entry, and Weak equivalence. The canceled reference above functor also retains an underline. Text is in one principal ink hand; the pencilled archive 8 is separate at bottom left. No internal page number, date, letterhead, additional margin prose, or stated page count is visible. Much of the lower sheet is blank with scattered isolated specks.',
 changes=changes,c_doubts=doubts,
 remaining_doubts=[
  dict(place='canceled text before n-C-stacks',reading=r'\deleted{\unsure{an|en|n}}',alternatives='an | en | n',confidence='low',reason='Overlapping cancellation hides the initial loop and interior strokes.'),
  dict(place='after elementary modelizer',reading=r'(\unsure{!|;|!,})',alternatives='! | ; | !,',confidence='low',reason='Long upper stroke favors an exclamation mark, but the tailed lower dot does not settle the punctuation.'),
  dict(place='canceled mark after Strict test. category',reading=r'\deleted{\unsure{(!)|!|4.}}',alternatives='(!) | ! | 4.',confidence='low',reason='The surviving curve, upright and dot admit more than one underlying reading.'),
  dict(place='connector between X and Y',reading=r'\mathrel{\unsure{-|\to}}',alternatives='dash | right arrow',confidence='medium',reason='A downturned thickened endpoint could be a terminal pen stroke or a minimal arrow barb.'),
 ],
 inventory=inventory,
 notes=[
  'This is an English working terminology list, retaining its written forms and marks, including the single opening quote before basic, the full stop in test., and the acute accent in catégory. No spellings or punctuation have been regularized.',
  'References are: 4., 5., 13., 13, 25, 26 with underlined 39, 27, 28 branching to underlined 41 and 42, 29 with raised 7, 33 and 39, 34, canceled 34, 35, ?, 37, 39., 39, 39. They function as index references; this page gives no definitions or claims about those pages.',
  'The test category entry is separately legible in the space above test-topology and has its own reference leader. Its visual interline position is recorded in the inventory; no caret instructs that it replace the still-live test-topology entry.',
  'The curve after map of objects is treated as an insertion connector into the existing aspheric parenthesis, not as an additional literal closing parenthesis or underline. The original closing parenthesis remains after the insertion in the reading.',
  'The weak-equivalence phrase has an opening parenthesis and no closing mate. The abbreviation m; is retained as ink, without expanding it to map. The nearby right-column question mark is the entry reference, not an added sentence-ending guess.',
  'Both canceled square drawings are reproduced in TikZ with their actual cancellation strokes; a further automatic strike would add a nonoriginal line, so the existing drawing reconstruction is retained and its deletion state is recorded explicitly in comments and separate inventory rows.',
  'The two tiny isolated marks above/below the final topos are not at the end of its textual baseline and resemble the scattered page specks. The inspected crop crops/14_final_topos.jpg therefore supplies no added terminal full stop. This differs from the discrete period beside reference 39., inspected in crops/13_strict_reference.jpg.',
  'The whole page and each supplied half were viewed once. Fourteen unresolved loci were then cropped once each with scripts/crop.py; the plan and crop log are retained in this reader directory. No whole half was reopened or enlarged, and no OCR, extraction, external source, other page or other reader was used.',
  'Inventory coverage includes every text entry, all named additions and deletions, the reference fork, grouping rules, the two separately canceled drawings and their separating comma, and the archive number comment. No additional live prose or marginal annotation was found.',
  'No substantive mathematical assertion is stated on this terminology page. The source/target connector was examined as an ink and parsing problem, not as a theorem, so no proof or mathematical check event is claimed.'
 ],
 math_checks=[],
 notation=[
  dict(sign=r'n, \infty, \underline{C}',location='stacks entry',reading=r'$n$-stacks, $\infty$-stacks, $n$-$\underline{C}$-stacks',evidence='Low arched n, a horizontal infinity loop, and an open capital C with a separate low underline; no double stroke on C.'),
  dict(sign='C and H capitals',location='Coherator, Hot-equivalence, Cat',reading='Coherator; Hot-equivalence; (Cat)',evidence='Initial capital strokes are larger than the following lowercase letters; the C and H are single-stroked, not blackboard or script capitals.'),
  dict(sign=r'29^7',location='basic/elementary reference',reading='raised crossed 7',evidence='Top horizontal, descending stem and middle cross-stroke in crop 07; not an asterisk or plus.'),
  dict(sign=r'28 \to \underline{41},\ \underline{42}',location='modelizer reference group',reading='one upper-right arrow and one lower-right arrow leave 28',evidence='Separate oblique shafts and dark arrowheads end near the two underlined numbers; both paths are reproduced in tikz-cd.'),
  dict(sign=r'\unsure{-|\to}',location='Weak equivalence, between X and Y',reading='dash first, right arrow possible',evidence='One horizontal stroke and a thickened downturned tip remain ambiguous after crop 11.'),
  dict(sign='m;',location='Weak equivalence, after Y',reading='literal m followed by semicolon',evidence='A low m-shaped wave precedes a separate dot and tailed lower punctuation stroke; no p descender.'),
  dict(sign=') and }',location='right-hand grouping of terminology lines',reading='brace at modelizer; right parentheses/curved rules at 29, 35 and local 39',evidence='Their distinct curly versus single curved profiles are visible in the half images.'),
  dict(sign='[strict], [locally]',location='lower terminology entries',reading='literal square brackets',evidence='Straight upright brackets with horizontal terminal strokes surround each qualifying word.'),
 ],
 abbreviations=[
  dict(form='tot.',expansion='probably totally; listed only, not expanded in reading',place='locally aspheric entry'),
  dict(form='asph.',expansion='probably aspheric; listed only, not expanded in reading',place='locally aspheric entry'),
  dict(form='el.',expansion='probably elementary; listed only, not expanded in reading',place='local el. modelizer'),
  dict(form='m;',expansion='possibly map or morphism; punctuation and expansion are not normalized',place='Weak equivalence after Y'),
  dict(form='Cat',expansion='category notation; no expansion asserted by this page',place='basic modelizer (Cat)'),
 ],
 brief_feedback='The brief referred to a permitted H change-kind list without including it. The parent supplied the exact allowed values during this run, and those values are used here. There was no substantive reading communication with any other reader. The brief does not distinguish meaningful uncertainty-only collation updates from certain changes, so such rows are labeled other and explain when the primary reading agrees with H. C contains 12 distinct explicit doubt loci; repeated context notes on test. and catégory are treated as the same loci, and the missing weak-equivalence closing delimiter is covered separately in changes and notes.'
)

# Use exact witness snippets for the multiline layout and drawing loci.
c_text=Path('/workspace/scratch/6d55c8c3e5a7/work/inputs/009/C.tex').read_text()
h_text=Path('/workspace/scratch/6d55c8c3e5a7/work/inputs/009/H.tex').read_text()
r_text=(BASE/'reading.tex').read_text()
def between(text,start,end,include_end=False):
    a=text.index(start); b=text.index(end,a)
    return text[a:b+(len(end) if include_end else 0)]
rows={x['id']:x for x in changes}
rows['test-entries']['c']=between(c_text,r'\hspace{1.5em}',r'$\left.\begin{array}')
rows['test-entries']['reading']=between(r_text,r'\hspace{1.5em}',r'$\left.\begin{array}')
rows['test-entries']['h']=between(h_text,'test category (!) / test-topology',r'\note{')
rows['basic-group']['c']=between(c_text,r'$\left.\begin{array}{@{}l@{}}'+'\n'+r"\text{\unsure{'basic|basic}",r'\uline{Strict}')
rows['basic-group']['reading']=between(r_text,r'$\left.\begin{array}{@{}l@{}}'+'\n'+r"\text{'basic",r'\uline{Strict}')
rows['basic-group']['h']=between(h_text,'basic modelizer (Cat)',r'\item \emph{strict}').strip()
rows['simplices-cubes']['c']=between(c_text,'standard simplices',r'\begin{minipage}{.4\linewidth}')
rows['simplices-cubes']['reading']=between(r_text,'standard simplices','% Both drawings')
rows['simplices-cubes']['h']=between(h_text,'standard simplices',r'\item \struck{$\square$').strip()
rows['canceled-square-drawings']['c']=between(c_text,r'\figure{\begin{tikzpicture}',r'\end{tikzpicture}}',True)
rows['canceled-square-drawings']['reading']=between(r_text,r'\figure{\begin{tikzpicture}',r'\end{tikzpicture}}',True)
rows['aspheric-group']['c']=between(c_text,r'$\left.\begin{array}{@{}l@{}}'+'\n'+r'\text{aspheric',r'\uline{Weak equivalence}')
rows['aspheric-group']['reading']=between(r_text,r'$\left.\begin{array}{@{}l@{}}'+'\n'+r'\text{aspheric','% The visible opening')
rows['aspheric-group']['h']=between(h_text,'aspheric (topos',r'\item weak equivalence').strip()
rows['local-group']['c']=between(c_text,r'$\left.\begin{array}{@{}l@{}}'+'\n'+r'\text{local test',r'{}[locally]')
rows['local-group']['reading']=between(r_text,r'$\left.\begin{array}{@{}l@{}}'+'\n'+r'\text{local test',r'{}[locally]')
rows['local-group']['h']=between(h_text,'local test category',r'\item $[$locally').strip()

(BASE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'diff_c':sum(x['diff_c'] for x in changes),'diff_h':sum(x['diff_h'] for x in changes),'c_doubts':len(doubts),'resolved_c_doubts':sum(x['resolved'] for x in doubts),'remaining_doubts':len(report['remaining_doubts']),'inventory':len(inventory)},indent=2))
