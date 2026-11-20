from pathlib import Path
from datetime import datetime,timezone
import json
out=Path('/workspace/scratch/ae626167fbca/SP47_CW_103_work/readers/scan003/B')
base='/workspace/scratch/ae626167fbca/source/SP47_CW_103_scans/'
crops=json.loads((out/'crop_log.json').read_text())
reads={
'b01_auto':r'au\deleted{\unsure{ot|tt}}to-équivalences; the two occupied cells contain both circular bodies and t crossbars, and the order of their impressions remains uncertain.',
'b02_bitorseurs':r'b\deleted{\unsure{t|l}}itorseurs; an extra upright/crossbar or foot lies beneath the live i, with t preferred to l but not secure.',
'b03_evidente':r'évident\deleted{\unsure{s|e}}e; a second rounded impression survives inside and to the right of the final e; s/e remain possible.',
'b04_un_mark':r'un\unsure{\'|.}; a black mark lies high after un, with an irregular taper. An apostrophe is stronger than a misplaced dot, but the shape is not decisive.',
'b05_les':r'\deleted{\rlap{xxx}\unsure{Les|les}}; upper stem, low foot and rounded following letters survive under the x cancellations; initial case remains unclear.',
'b06_de1':r'\deleted{\rlap{xxxx}de 1}; d ascender, e counter, blank third cell and numeral 1 top serif/stem are individually recoverable. C doubt removed.',
'b07_a':r'\deleted{\unsure{à|a}}à; overlapping a outlines and crossed strokes above them survive, but the accent belonging to the underlying impression cannot be isolated.',
'b08_f_cancel':r'\deleted{\rlap{$\mathrm{xxxxxxxxx}_{\mathrm{xxxxxx}}$}\unsure{1_C\quad 1_C}}; two 1 top strokes and two low C-like curves survive. Other x-covered positions yield no securely identifiable extra character.',
'b09_pen_cancel':r'\deleted{\handwritten{\unsure{(du pen}}}; left parenthesis, rising d and descending p are partly visible beneath the cancellation. The remaining short joins are compatible with du pen, not fully secure.',
'b10_pentagon':r'(axiome du pentagone), attached after d’associativité. A long hand connector runs below the addition, turns downward at the left attachment and upward at the right; it has no definite arrowhead.',
'b11_pi_index':r'\handwritten{\pi}_{\deleted{1}\handwritten{0}}; the old index has a typewriter 1 top serif and horizontal base, crossed/encircled by a handwritten closed oval 0.',
'b12_cochaine':r'2-coc\deleted{ah}haine; BOTH adjacent cells are composite a+h. Their clear bowls, cross strokes and tall h stems support the original ah transposition and final ha, rather than a correction of only one cell.',
'b13_correspondants':r'\deleted{p}co\deleted{\unsure{s|e|r}}rrespondants; first cell has definite p descender and bowl beneath c. First r has an additional low rounded body: s is preferred, e or a repeated r remain possible.',
'b14_Ostar':r'\underline{O}_{X}^{*}; O has its own short underline and low X. The raised star has x-like typewriter diagonals/serifs with a central horizontal strike; it is not a newly inferred handwritten star.'}
for c in crops:
 c['reading']=reads[c['id']]
 c['view_count']=1
 c['viewed_after_utc']='2026-11-20T09:15:59.529226Z'
 if c['id']=='b13_correspondants': c['reason']+=' The same crop also revealed a previously unrecorded overstrike in the first r.'
changes=[]
def change(place,c,h,reading,ink,confidence='high',kind='other',ac=False,ah=True,ids=(),marked=False):
 changes.append(dict(place=place,c=c,h=h,reading=reading,scan_shows=ink,confidence=confidence,kind=kind,marked_in_H=marked,against_c=ac,against_h=ah,crop_ids=list(ids)))
change('opening, quotation around champ','``champ\'\'','« champ »','``champ\'\'','Settled in half_a: each boundary has two short high straight typewriter strokes; there are no angle-shaped guillemets.',kind='misread symbol or index')
change('opening, auto-équivalences overwritten pair',r'au\deleted{\unsure{ot|tt}}to-équivalences','auto-équivalences',r'au\deleted{\unsure{ot|tt}}to-équivalences','Crop b01: both character cells contain an o-shaped enclosed body plus a tall t stem and crossbar. The live word is auto-, but old ot versus tt is not visually decidable. Retained C doubt.','low','omission',False,True,['b01_auto'])
change('opening, quotation around bitorseurs','``bitorseurs\'\'','« bitorseurs »','``bitorseurs\'\'','Settled in half_a and visible in b02: doubled upright strokes stand high at the two word boundaries, not angle-shaped quotation marks.',kind='misread symbol or index',ids=['b02_bitorseurs'])
change('opening, first i of bitorseurs',r'b\deleted{\unsure{t|l}}itorseurs','bitorseurs',r'b\deleted{\unsure{t|l}}itorseurs','Crop b02: the live i has its dot and baseline, with an additional high crossbar/upright and right foot beneath it; t and l cannot be separated completely. Retained C doubt.','low','omission',False,True,['b02_bitorseurs'])
change('opening, dash following sous F','F, - la composition','F, --- la composition','F, - la composition','Settled in half_a: the horizontal mark has the width of a typewriter hyphen, comparable with the internal hyphens in the paragraph.',kind='misread symbol or index')
change('opening, final e in évidente',r'évident\deleted{\unsure{s|e}}e','évidente',r'évident\deleted{\unsure{s|e}}e','Crop b03: a second rounded impression protrudes inside and to the right of the final e. Its original middle and lower strokes cannot be distinguished securely as s rather than e. Retained C doubt.','low','omission',False,True,['b03_evidente'])
change('opening, high mark after un',r'un\unsure{\'|.} faisceau','un faisceau',r'un\unsure{\'|.} faisceau','Crop b04: there is a separate high black impression immediately after n; it has an uneven tapered upper part. It is not an absent mark; apostrophe versus a misplaced dot remains unresolved. Retained C doubt.','low','omission',False,True,['b04_un_mark'])
change('opening, added quotation around inversibles',r'\handwritten{``}inversibles\handwritten{\'\'}',r'\add{«} inversibles \add{»}',r'\handwritten{``}inversibles\handwritten{\'\'}','Settled in half_a: two slanted pen strokes at each end of inversibles form high double quotes. Their addition state is represented in both witnesses, but H gives guillemets.',kind='misread symbol or index',marked=True)
change('Structure heading, extent of underline',r'\uline{Structure}.',r'\emph{Structure.}',r'\uline{Structure}.','Crop b05: the line runs beneath Structure and stops before the period; H’s emphasized span includes the period.',kind='other',ids=['b05_les'],marked=True)
change('Structure heading, cancelled opening word',r'\deleted{\rlap{xxx}\unsure{Les|les}}','omitted',r'\deleted{\rlap{xxx}\unsure{Les|les}}','Crop b05: three x-like cancellations overlie three letter cells. A tall left stem and low foot survive, but case cannot be separated securely from the cancellations. Retained C doubt.','medium','omission',False,True,['b05_les'])
change('c), between automorphisme and rho(X)',r'\deleted{\rlap{xxxx}\unsure{de 1}}','omitted',r'\deleted{\rlap{xxxx}de 1}','Crop b06: the d ascender and left bowl, the e loop, a blank occupied only by the cancellation, and the final numeral 1 top serif and stem all survive. The crop resolves the reading de 1.','high','omission',True,True,['b06_de1'])
change('choice of representatives, after pour deux',r'\deleted{\rlap{xxxxxx}objets}','omitted',r'\deleted{\rlap{xxxxxx}objets}','Settled in half_a and half_b overlap: all six letters of objets remain discernible under the row of x cancellations, immediately before a,b.',kind='omission')
phi_places=[
('first displayed choice isomorphism','a,b','half_a'),
('compte tenu clause, first isomorphism','a,b','half_b'),
('compte tenu clause, second isomorphism','ab,c','half_b'),
('compte tenu clause, third isomorphism','b,c','half_b'),
('compte tenu clause, fourth isomorphism','a,bc','half_b'),
('Les ... étant choisis','a,b','half_b'),
('last paragraph, système d’isomorphismes','a,b','half_b'),
('last paragraph, si on change phi',None,'half_b'),
('last paragraph, choix différents de phi',None,'half_b')]
for place,index,half in phi_places:
 suffix=('{'+index+'}') if index else ''
 sub=('_'+suffix) if index else ''
 change(place,r'\phi'+sub,r'\varphi'+sub,r'\phi'+sub,f'Settled in {half}: the pen sign is a small closed oval pierced by one long rising/slanting stroke, with no open curled bowl of varphi. '+('The stated lower indices and comma were separately checked.' if index else 'There is no subscript here.'),kind='misread symbol or index')
change('tensorisation à gauche, overwritten à',r'\deleted{\unsure{à|a}}à','à',r'\deleted{\unsure{à|a}}à','Crop b07: two displaced a-shaped bodies and crossing upper strokes survive; the final grave-marked à is clear but the underlying accent cannot be assigned to one impression. Retained C doubt.','low','omission',False,True,['b07_a'])
change('f(a,b,c) display, x-cancelled tail',r'\deleted{\rlap{$\mathrm{xxxxxxxxx}_{\mathrm{xxxxxx}}$}\unsure{1_C\quad 1_C}}','omitted',r'\deleted{\rlap{$\mathrm{xxxxxxxxx}_{\mathrm{xxxxxx}}$}\unsure{1_C\quad 1_C}}','Crop b08: two raised top-and-stem typewriter numeral outlines and two lower curved C-like outlines remain under two levels of x. The intervening covered cells disclose no reliable extra character. Retained C doubt, not a claim to recover the entire abandoned formula.','low','omission',False,True,['b08_f_cancel'])
change('f domain display, first product separator',r'\mathbin{\mathrm{x}}',r'\times',r'\mathbin{\mathrm{x}}','Settled in half_b, also visible along upper edge of b09: a baseline typewriter x with seriffed endpoints separates the first and second pi_0.',kind='misread symbol or index',ids=['b09_pen_cancel'])
change('f domain display, second product separator',r'\mathbin{\mathrm{x}}',r'\times',r'\mathbin{\mathrm{x}}','Settled in half_b, also visible along upper edge of b09: the second separator repeats the baseline typewriter x, between the second and third pi_0.',kind='misread symbol or index',ids=['b09_pen_cancel'])
change('last paragraph, cancelled interlinear trial before standard',r'\deleted{\handwritten{\unsure{(du pen}}}','omitted',r'\deleted{\handwritten{\unsure{(du pen}}}','Crop b09: the initial parenthesis, an ascender compatible with d and descender compatible with p remain; heavy horizontal pen cancellation prevents a secure full reading. Retained C doubt.','low','omission',False,True,['b09_pen_cancel'])
change('last paragraph, curving connector beneath pentagon insertion','insertion text/caret macro only','insertion text/add macro only','drawn curved connector, reproduced in TikZ','Crop b10: a continuous line goes from a downward-turning left hook after d’associativité beneath the added words to a short upturned right end. Neither witness reproduces its geometry; no arrowhead is inferred. The insertion wording and attachment are otherwise agreed.','high','drawing or diagram',True,True,['b10_pentagon'],True)
change('last paragraph, underlining of 3-cocycle',r'\handwritten{3}-\uline{cocycle}',r'\emph{3-cocycle}',r'\handwritten{3}-\uline{cocycle}','Settled in half_b: the underline begins below the c of cocycle and ends below its last letters; the preceding hand 3 and hyphen are outside the underline.',kind='other',marked=True)
change('last paragraph, corrected group index after du groupe',r'\handwritten{\pi}_{\deleted{1}0}',r'\pi_0',r'\handwritten{\pi}_{\deleted{1}\handwritten{0}}','Crop b11: the typewriter 1 has its top serif, vertical stem and baseline. A closed pen oval 0 is placed over it. C preserves the same reading and correction state; hand/type grouping is merely clarified.','high','omission',False,True,['b11_pi_index'])
change('last paragraph, second 2-cochaine, adjacent overwritten cells',r'2-coc\deleted{\unsure{a}}haine','2-cochaine',r'2-coc\deleted{ah}haine','Crop b12: each of TWO adjacent cells combines a tall h ascender with an a bowl and middle stroke. The pen/type density is not confined to the first cell. This supports ah corrected to ha: abandoned cocahine, live cochaine. The first a is now read without C’s doubt; the abandoned h in the second cell was omitted by C and H.','high','omission',True,True,['b12_cochaine'])
change('last paragraph, hyphen after f+dg','f+dg - donc','f + dg --- donc','f+dg - donc','Settled in half_b: the separator is a short single typewriter hyphen, matching the word hyphens, not a long dash.',kind='misread symbol or index')
change('last paragraph, first c of correspondants',r'\deleted{\unsure{p}}correspondants','correspondants',r'\deleted{p}correspondants','Crop b13: a clear low descender with baseline foot extends below the live c and joins the old rounded upper bowl. This identifies the abandoned p; C’s doubt is removed.','high','omission',True,True,['b13_correspondants'])
change('last paragraph, first r of correspondants','first r unmarked','first r unmarked',r'co\deleted{\unsure{s|e|r}}rrespondants','Crop b13: this cell has the live r top/shoulder and an extra rounded low right body. An underlying s is visually preferred; e or a second impression of r remains possible. This additional overstrike is unrecorded in both witnesses.','low','omission',True,True,['b13_correspondants'])
change('lower-left archive pencil numeral','% archive sheet number: 2','omitted','% archive sheet number: 2','Settled in half_b: a separate thin pencil 2 appears at the bottom-left corner. It is distinct from the upper penned manuscript page number.',kind='omission')

unresolved=[]
def doubt(place,reading,alts,confidence,evidence):
 unresolved.append(dict(place=place,reading=reading,alternatives=alts,confidence=confidence,evidence=evidence))
doubt('auto-équivalences overwritten pair','ot',['tt'],'low','b01: circular bodies and crossbars overlie both cells, obscuring the order of impressions.')
doubt('first i of bitorseurs','t',['l'],'low','b02: additional upper/foot strokes under i do not fully distinguish t from l.')
doubt('final e of évidente','s',['e'],'low','b03: additional rounded contours cannot be assigned securely to s or e.')
doubt('mark after un',"'",['.'],'low','b04: separate high tapered black impression; its irregular outline leaves a displaced dot possible.')
doubt('cancelled word after Structure','Les',['les'],'medium','b05: cancellations conceal the initial cap-height/foot distinction.')
doubt('underlying letter at à gauche','à',['a'],'low','b07: upper diagonal strokes cannot be assigned uniquely to the earlier or later impression.')
doubt('cancelled tail after f(a,b,c)',r'1_C\quad1_C',['other partly destroyed formula containing those two identity-like groups'],'low','b08: the two 1/C groups have surviving strokes, while no further letter/operator can be securely recovered through the x cancellations.')
doubt('cancelled interlinear trial before standard','(du pen',['partly unreadable short parenthetical trial'],'low','b09: only portions of the first curve, ascender, descender and small joins survive the heavy pen line.')
doubt('underlying first r of correspondants','s',['e','r'],'low','b13: extra lower rounded body is visible, but overlays obscure its exact letter identity.')

inventory=[]
def inv(element,kind,position,first,hand='typewriter'):
 inventory.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('manuscript page number','text','top centre','2','another unnamed hand')
inv('opening continuation paragraph','text','upper block','prenant pour A la "champ"; includes all F, P and underlined O expressions')
inv('auto-équivalences overstrike','deletion','upper block line 2','ot|tt under to')
inv('bitorseurs overstrike','deletion','upper block line 3','t|l under i')
inv('P addition and caret','insertion','after faisceaux','P','another unnamed hand')
inv('évidente overstrike','deletion','upper block line 6','s|e under final e')
inv('added opening and closing quotation marks','insertion','around inversibles','double high pen strokes','another unnamed hand')
inv('Structure heading and underline','text','below opening block','Structure.')
inv('cancelled Les/les','deletion','after Structure.','Les|les beneath three x')
inv('structure introductory sentence','text','heading line','Soit C une (Gr)-catégorie, on lui associe')
inv('item a','text','below heading','a) le groupe pi_0(C) des classes…','typewriter and another unnamed hand')
inv('item b','text','below a','b) le groupe pi_1(C) des automorphismes…','typewriter and another unnamed hand')
inv('item c introductory text','text','below b','c) une action de pi_0(C) sur pi_1(C)…','typewriter and another unnamed hand')
inv('cancelled de 1','deletion','after automorphisme','de 1 beneath xxxx')
inv('automorphism diagram','diagram','below item c','Aut(1_C), two parallel right arrows, Aut(X)','typewriter and another unnamed hand')
inv('maps and commutativity/representative-choice paragraph','text','after diagram','donnés par u maps-to… On prouve que… Ceci posé…','typewriter and another unnamed hand')
inv('cancelled objets','deletion','after pour deux','objets beneath xxxxxx')
inv('chosen isomorphism','display','after un isomorphisme','phi_{a,b}: L_a tensor L_b simeq L_ab','typewriter and another unnamed hand')
inv('three-element introduction','text','following chosen-isomorphism display','alors pour trois éléments a,b,c…','typewriter and another unnamed hand')
inv('associativity isomorphism','display','midpage','(L_a tensor L_b) tensor L_c simeq L_a tensor (L_b tensor L_c)','typewriter and another unnamed hand')
inv('four-isomorphism clause','text','below associativity display','compte tenu des isomorphismes phi_{a,b}, phi_{ab,c}, phi_{b,c}, phi_{a,bc}…','typewriter and another unnamed hand')
inv('L_abc self-isomorphism','display','below four-isomorphism clause','L_abc simeq L_abc','typewriter and another unnamed hand')
inv('left-tensorization clause','text','below self-isomorphism','ou encore comme la tensorisation à gauche…')
inv('à overstrike','deletion','tensorisation à gauche','underlying à|a')
inv('f(a,b,c) membership','display','below tensorization clause','f(a,b,c) in pi_1(C)','typewriter and another unnamed hand')
inv('cancelled display tail','deletion','right of pi_1(C)','two x rows over tentative 1_C and 1_C')
inv('functorial associativity paragraph','text','after membership display','Les phi_{a,b} étant choisis…; includes inline primed-L associativity','typewriter and another unnamed hand')
inv('cochain-domain display','display','above last paragraph','f: pi_0 x pi_0 x pi_0 right-arrow pi_1','typewriter and another unnamed hand')
inv('last paragraph','text','lower block','On vérifie alors que… jusqu’à classe de 3-cohomologie','typewriter and another unnamed hand')
inv('cancelled parenthetical trial','deletion','above standard','(du pen','another unnamed hand')
inv('pentagon phrase','insertion','interlinear, attached after d’associativité','(axiome du pentagone)','another unnamed hand')
inv('pentagon insertion connector','drawing','beneath addition, curving to attachment','long curved line with left downward and right upward ends','another unnamed hand')
inv('corrected group subscript','deletion','du groupe pi_0','typed 1 overwritten with hand 0','typewriter and another unnamed hand')
inv('cochaine adjacent overstrikes','deletion','second 2-cochaine','ah corrected to ha')
inv('correspondants initial overstrike','deletion','bottom text block','p corrected to c')
inv('correspondants first-r overstrike','deletion','bottom text block','s|e|r under first r')
inv('archive sheet number','text','bottom-left corner','2 (comment only)','another unnamed hand')

notation=[
 dict(place='opening paragraph, three structure-sheaf forms',sign='underlined O; X; star',ink='O is a plain round typewriter capital with one short underline beneath O only, X lower right; the first has a raised x-like star with central bar.',latex=r'\underline{O}_X^*; \underline{O}_X'),
 dict(place='a), b), c), and repeated groups through page',sign='pi_0 and pi_1',ink='Pen top bar joins two legs; the low numeral is 0 or 1 as written. The subscript correction in the last paragraph is recorded separately.',latex=r'\handwritten{\pi}_0; \handwritten{\pi}_1'),
 dict(place='c), after cancelled de 1',sign='rho',ink='Closed pen bowl attached to descending left stem; typed (X) follows.',latex=r'\handwritten{\rho}(X)'),
 dict(place='diagram',sign='parallel arrows',ink='Two distinct horizontal pen shafts, each with its own right-pointing head, without labels or starting bars.',latex=r'\arrow[r,shift left=.55ex]; \arrow[r,shift right=.55ex]'),
 dict(place='diagram and following text',sign='Aut; id_X; Ob',ink='Upright typewriter names, capital A and O, lower X after id; all occurrences inspected.',latex=r'\mathrm{Aut}; \mathrm{id}_X; \mathrm{Ob}'),
 dict(place='two maps following diagram',sign='maps-to',ink='Each pen sign has a short vertical starting bar, horizontal shaft and right head.',latex=r'\handwritten{\mapsto}'),
 dict(place='all tensor expressions',sign='tensor product',ink='Typewriter circle crossed internally; the several crowded O-cross-L combinations are separately legible as tensor signs and following L.',latex=r'\otimes'),
 dict(place='representative choice and associativity displays',sign='capital L and indices',ink='Plain typewriter capital L with separately lowered a, b, c, ab and abc; no overstruck alphabet or bold capital.',latex=r'L_a;L_b;L_c;L_{ab};L_{abc}'),
 dict(place='choice display and nine phi loci',sign='phi',ink='A narrow closed oval pierced by one slanting stroke; lower typed indices/commas checked at each locus. No varphi shape.',latex=r'\handwritten{\phi}_{a,b};\handwritten{\phi}_{ab,c};\handwritten{\phi}_{b,c};\handwritten{\phi}_{a,bc};\handwritten{\phi}'),
 dict(place='isomorphism and inline associativity formulas',sign='simeq',ink='One wavy upper pen stroke and one horizontal lower stroke, not an equals sign or arrow.',latex=r'\handwritten{\simeq}'),
 dict(place='inline functorial-associativity formula',sign='primes',ink='One high stroke after the first primed L, two after L double prime, repeated in the right member; not factorials or exclamation marks.',latex=r"(L\otimes L')\otimes L''\simeq L\otimes(L'\otimes L'')"),
 dict(place='final f-map display',sign='x and right arrow',ink='Two baseline typewriter x signs; one pen arrow with no vertical starting bar.',latex=r'\mathbin{\mathrm{x}};\handwritten{\longrightarrow}'),
 dict(place='last paragraph',sign='cohomological numerals',ink='Hand-drawn 3 with two lobes in 3-cocycle and 3-cohomologie; typed 2 in both cochaine occurrences.',latex=r'\handwritten{3};2'),
 dict(place='opening article and last paragraph orthography',sign='linguistic alerts',ink='The article is la before champ; both cochaine occurrences have no circumflex; fonctoriel visibly ends -iel. These are agreed readings, recorded here rather than as changes.',latex='la ``champ\'\'; cochaine; fonctoriel')]

notes=[
'Coverage: every text block and every inline and display formula on scan 003 was compared against both C and H, including all agreed words, endings, accents, punctuation, capitals, indices, primes, arrows, tensor signs, underlines and the paragraph ending. This is a visual coverage statement, not a mathematical proof check.',
'Only scan 003 inputs, its whole image, its supplied two halves and the 14 documented crops were inspected. Whole was opened once, then half_a once, then half_b once in that order. No whole half was enlarged again; each unresolved locus received one crop, and no crop was regenerated or viewed twice. Exact timestamps were not emitted by the image tool, so the recorded initial view interval is explicitly bounded rather than invented.',
'The sheet is a typescript continuation with pen-filled mathematical symbols, corrections, and additions. No author date or page total is written. The upper pen numeral reads 2; the lower-left pencil/archive numeral independently reads 2. Pen authorship is not assigned beyond an unnamed hand.',
'The opening paragraph describes the category of auto-equivalences of the champ of right F-torsors using bitorseurs, and then a description by invertible bi-Modules over an underlined O_X. Its la before champ, commutatif wording, quotation forms and high stray mark after un are retained without grammatical correction.',
'The Structure section states the construction of pi_0(C), pi_1(C) and an action, with two parallel maps from Aut(1_C) to Aut(X). The wording rho(X) de 1_C is retained exactly; no theoretical replacement by Aut(1_C) is made. The subsequent claim of commutativity is the page’s own assertion.',
'The page chooses representatives L_a and isomorphisms phi_{a,b}, identifies associativity with f(a,b,c) in pi_1(C), and states a relation with a 3-cocycle and changes f+dg under changes of 2-cochain. These assertions prompted checking the indices and signs in the images only; no proof or cohomology computation was performed.',
'C’s de 1 and initial p doubts are resolved by surviving strokes. The second cochaine has a double-cell transposition correction ah to ha, not just an old a under the h. A further overstrike in the first r of correspondants is recorded with uncertainty because its low rounded extra strokes are visible but the old letter is not secure.',
'The uncertain erased display tail preserves the two identity-like groups visible under x cancellations without inferring extra lost operators. The short cancelled parenthetical trial is not completed from the later live pentagon insertion.',
'The curving line under the pentagon addition is reproduced as a separate TikZ drawing after the paragraph with a placement comment, while the words themselves are inserted at their source attachment after d’associativité. The drawing is a connector without an inferred arrowhead.',
'H’s use of emphasis/addition/deletion-style macros was treated as a convention, not by itself a textual difference. Differences were recorded only where content, uncertainty, state, actual glyph shape, omission, underline extent, or reproduced geometry differed. Handwritten macro grouping alone is not counted as a witness error. Fully agreed expressions and the agreed grammatical/orthographic alerts are in notation/coverage rather than extra changes rows.',
'All math_checks are empty because this run performed transcription and visual structure verification only. In particular, the source words On prouve and On vérifie do not constitute checks performed by this reader.'
]
end=datetime.now(timezone.utc).isoformat()
report=dict(scan=3,reader='B',start_utc='2026-11-20T09:14:53Z',end_utc=end,model='GPT-6 Astra Pro',effort='not exposed',viewed=[dict(role=role,path=base+name,order=i,count=1,when_utc_interval=['2026-11-20T09:14:53Z','2026-11-20T09:15:59.529226Z']) for i,(role,name) in enumerate([('whole','H103-01_103_scan003.jpg'),('half_a','H103-01_103_scan003_a.jpg'),('half_b','H103-01_103_scan003_b.jpg')],1)],crops=crops,changes=changes,unresolved=unresolved,inventory=inventory,notation=notation,abbreviations=[dict(form='i.e.',expansion='id est'),dict(form='Aut',expansion='automorphismes'),dict(form='id',expansion='identité'),dict(form='Ob',expansion='objets'),dict(form='(Gr)',expansion='category prefix retained; not expanded by this page')],notes=notes,math_checks=[])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=str(out/'report.json'),changes=len(changes),against_c=sum(c['against_c'] for c in changes),against_h=sum(c['against_h'] for c in changes),unresolved=len(unresolved),crops=len(crops),inventory=len(inventory),end_utc=end),ensure_ascii=False))
