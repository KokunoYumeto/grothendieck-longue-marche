"""Assemble the page-local first-reading records. No OCR or TeX compilation."""
from pathlib import Path
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan057'
BOXES = {
    'opening': [310,25,1603,188], 'torseurs': [320,289,1618,589],
    'first_formula_full': [319,575,923,745], 'contraction': [320,733,1620,831],
    'partial': [315,838,1565,1070], 'extension': [318,1070,1635,1300],
    'multiple': [313,1284,1668,1623], 'strengthening': [315,1625,1650,1850],
    'singular_full': [315,1815,1630,2185], 'final': [315,2150,1580,2340],
    'folio': [41,2244,135,2335],
}
record = dict(page=PAGE, reader='reader_b', lines_read=27, changes=[], decisions=[],
              implicit_decisions=[], doubts=[], inventory=[], notes=[], check_events=[],
              notation=[], abbreviations=[], second_boxes=[])

def crop(name):
    return f'crops/{PAGE}_{name}.png'

def change(place, c, h, final, dc, dh, kind, error, evidence, name,
           confidence='high', marked=False, consequential=False):
    record['changes'].append(dict(
        id=f'{PAGE}-{len(record["changes"])+1:02}', place=place, c=c, h=h,
        final=final, diff_c=dc, diff_h=dh, kind=kind, error_kind=error,
        evidence=evidence, crop=crop(name), box=BOXES[name], confidence=confidence,
        marked_in_h=marked, consequential=consequential))

change('Raised word attached after sur', r'\inserted{chacun}', r'\add{\uncertain{assez}}',
       r'\inserted{chacun}', False, True, 'misread word', 'Words',
       'The insertion begins with open c and a tall looped h, then the compressed a-c-u-n run. There is no initial a or terminal z. Its leader attaches between sur and des, not between nature and spéciale as in H.', 'torseurs', marked=True)
change('Article before torseurs', 'des torseurs', 'les torseurs', 'des torseurs', False, True,
       'misread word', 'Words', 'The first letter has the loop and ascender of d; e and a terminal s hook follow. The inserted chacun precedes this original des.', 'torseurs')
change('After R_a (a in A)', 'concernés', 'absent', 'concernés', False, True,
       'omission', 'Omissions', 'Between the closing parenthesis and sous, the complete word has the two c openings, flattened middle run, accented e and terminal s. It is not empty space.', 'torseurs')
change('After concernés sous', 'sous', 'sous les', 'sous', False, True,
       'text not on the page', 'Text that is not on the page',
       'Sous is the final word of the row. The following row begins with the quotient; no separate les is written after sous or before that formula.', 'torseurs')
change('Alphabet of the three live Z letters in the first formula unit', r'\mathbb Z', r'\mathbf{Z}', r'\mathbb Z', False, True,
       'misread symbol or index', 'Symbols and indices',
       'The quotient numerator and both Z letters in the parenthetical definition have paired diagonal strokes, not merely a thick single Z. The whole formula, including the crossed old quotient, was inspected.', 'first_formula_full')
change('Parentheses around the first quotient divisor', 'r(a)', '(r(a))', 'r(a)', False, True,
       'misread symbol or index', 'Symbols and indices',
       'After the slash there is r with its argument parentheses. No additional enclosing pair around r(a) is visible. The large following parenthesis encloses the Z_a definition.', 'first_formula_full')
change('Crossed old quotient after the first live quotient', r'\deleted{\unsure{\mathbb Z/r(a)}}', 'absent',
       r'\deleted{\unsure{\mathbb Z/r(a)}}', False, True, 'omission', 'Omissions',
       'A Z-like form, long slash and r(a)-like ending survive under several crossing strokes. The whole old quotient and the neighbouring live definition were read, but the overwritten letters and alphabet cannot be settled. H mentions an illegible overworked formula only in a note.', 'first_formula_full', 'low', True)
change('Name of the first operator-group operation', r'\unsure{contraction|restriction}', r'\emph{restriction}', 'contraction', False, True,
       'misread word', 'Words',
       'The word begins with an open c and low o-n connection, then the tall first t; the latter c-t-i-o-n run is visible. There is no initial r-e-s group. The blank strip below it contains no underline.', 'contraction', consequential=True)
change('Alphabet in the contraction source and target', r"$\mathbb Z_a/r(a)$ à $\mathbb Z_a/r'(a)$",
       r"$\mathbf{Z}_a/r(a)$ à $\mathbf{Z}_a/r'(a)$", r"$\mathbb Z_a/r(a)$ à $\mathbb Z_a/r'(a)$", False, True,
       'misread symbol or index', 'Symbols and indices',
       'Both Z letters have two separated diagonal strokes. Their a subscripts, the unprimed first r and singly primed second r are clear; the following divisibility relation also has a single prime.', 'partial')
change('First explanatory parenthesis, number of opération', '(opération de', '(opérations de', '(opération de', False, True,
       'misread word', 'Words', 'The last n finishes in a low hook before the gap leading to de. There is no separate final s.', 'partial')
change('Interlinear uniforme in the first explanatory parenthesis', r'\uline{gommage partiel} \inserted{\uline{uniforme}}',
       r'\emph{gommage partiel uniforme}', r'\uline{gommage partiel} \inserted{\uline{uniforme}}', False, True,
       'insertion or placement', 'Insertions put in the wrong place',
       'Uniforme is written above the main row and has its own underline. A curved leader brings it into the gap after partiel and before en a. Gommage and partiel remain on the original row.', 'partial')
change('After inserted uniforme', r'\unsure{en} $a$', r'(\ill{})', r'en $a$', False, True,
       r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'The short low word has an e loop followed by the flattened n and its terminal flick; the separate a follows. The large curve beside it connects to the interlinear insertion and is not an additional opening parenthesis. Only the outer closing parenthesis is present.', 'partial', marked=True)
change('Underline state of extension', "d'extension", r"d'\emph{extension}", "d'extension", False, True,
       'other', 'Other', 'The complete word extension is visible on the baseline, with blank paper underneath and no underline stroke.', 'extension')
change('Alphabet in the extension source and target', r"$\mathbb Z_a/r(a)$ à $\mathbb Z_a/r''(a)$",
       r"$\mathbf{Z}_a/r(a)$ à $\mathbf{Z}_a/r''(a)$", r"$\mathbb Z_a/r(a)$ à $\mathbb Z_a/r''(a)$", False, True,
       'misread symbol or index', 'Symbols and indices',
       'Both Z letters have doubled diagonals. The first r is unprimed; two small prime strokes occur over the target r. No exponent or additional divisor parentheses are supplied.', 'extension')
change('Whole multiplier identity with raised addition', r"$r''(a)$ \inserted{$=d(a)r(a)$}",
       r"$r''(a) = d(a)\,r(a)$", r"$r''(a)$ \inserted{$=\unsure{d_a|d(a)}r(a)$}", True, True,
       'misread symbol or index', 'Symbols and indices',
       'The complete formula has r with two primes on the main row and the equals/product addition above it. The a is visibly lowered beneath d; a nearby curved stroke may be an opening parenthesis, so d_a is first but d(a) remains possible. The following r(a) is clear. H also describes the interlinear placement in its note.', 'extension', 'medium', False, True)
change('Underline scope in the second explanatory parenthesis', r'\uline{surmarquage uniforme en $a$}',
       r'\emph{surmarquage uniforme}', r'\uline{surmarquage uniforme} en $a$', True, False,
       'other', 'Other',
       'The long underline ends directly below the end of uniforme. It does not continue beneath en or a. H has the correct underline extent; its missing following text is recorded separately.', 'multiple')
change('Text following underlined surmarquage uniforme', r'en $a$', r'\ill{}', r'en $a$', False, True,
       r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'A low e-n run and a distinct small a stand after uniforme and before the comma. The comma follows a, rather than preceding this group as H places it.', 'multiple', marked=True)
change('Cancelled earlier closing parenthesis', r'\deleted{)}', 'absent', r'\deleted{)}', False, True,
       'omission', 'Omissions',
       'After the comma a large closing parenthesis remains visible, crossed by a separate diagonal/looping stroke at its upper part. The live phrase de multiplicateur continues to its right.', 'multiple', marked=True)
change('Multiplier wording across the line break', 'multiplicateur', r'multiplic.\ par', 'multiplicateur', False, True,
       'misread word', 'Words',
       'The long word reaches the right margin and continues as teur at the start of the following row. That continuation has the tall t followed by e-u-r, not p-a-r. There is no separate par word.', 'multiple')
change('Interlinear word after On se rend compte', r'\inserted{ici}', r'\ill{}', r'\inserted{ici}', False, True,
       r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'Above the gap after compte are a short dotted i, open c and final dotted i. The V-shaped attachment stroke points into that gap before que, establishing the insertion state.', 'multiple', marked=True)
change('Emphasis on partiel in the last statement', r'\uuline{partiel}', r'\emph{partiel}', r'\uuline{partiel}', False, True,
       'other', 'Other', 'Two separate, nearly parallel horizontal strokes lie beneath partiel. The lower one is shorter but distinct, so a single underline does not reproduce the emphasis.', 'strengthening')
change('Singular surmarquage in the last statement', 'le surmarquage uniforme', 'les surmarquages uniformes', 'le surmarquage uniforme', False, True,
       'misread word', 'Words',
       'Le ends after its low e stroke. Surmarquage ends in e without an added s, and uniforme likewise ends before the dash without a separate s. The full words and their ends are visible in the extended boundary crop.', 'singular_full')
change('Singular future phrase at graph level', 'sera défini', 'seront définis', 'sera défini', False, True,
       'misread word', 'Words',
       'The first word has the short s-e-r-a sequence, without the additional o-n-t run. Défini ends after the dotted i; no final s is written.', 'singular_full')
change('First word of the final parenthesis', 'sauf', 'autre', 'sauf', False, True,
       'misread word', 'Words', 'The opening s is followed by the low a-u run and a tall descending f. The ending is not the t-r-e sequence of autre.', 'final')
change('After bien sûr in the final parenthesis', 'bien sûr les', 'bien sûr que les', 'bien sûr les', False, True,
       'text not on the page', 'Text that is not on the page',
       'Sûr ends the row; the following row begins directly with les. No intervening que is written in either place.', 'final')
change('Final noun before d(a)', 'multiplicateurs', 'multiplications', 'multiplicateurs', False, True,
       'misread word', 'Words',
       'After the common multiplica- beginning, the tall t and low e-u-r-s ending are visible. The final run is not the t-i-o-n-s ending of multiplications.', 'final')
change('Lower-left handwritten folio', r'\mspage{56}', 'absent', r'\mspage{56}', False, True,
       'omission', 'Omissions', 'The first digit has a top bar, left turn and lower 5 bowl; the second has a long upper stroke closing into the lower bowl of 6.', 'folio')

def decision(target, identifier, choice, reading, evidence, name, confidence):
    record[target].append(dict(id=identifier, decision=choice, reading=reading,
        evidence=evidence, crop=crop(name), box=BOXES[name], confidence=confidence))

decision('decisions','M0743','first','par',
         'The long p descender is followed by one small a connection and a short r finish; there is no separate o-u sequence.', 'opening','high')
decision('decisions','M0744','first','contraction',
         'The initial open c and low o-n connection are followed by the first tall t; the latter c-t-i-o-n run is visible. No initial r-e-s group or underline is present.', 'contraction','high')
decision('decisions','M0745','first','en',
         'The short low e loop and flattened n are visible beside the curved insertion leader, before the separate a. The leader does not erase the letters.', 'partial','high')
decision('implicit_decisions','I057-01','undecided',r'\deleted{\unsure{\mathbb Z/r(a)}}',
         'The entire old quotient is under several crossing strokes. Its Z-like initial and r(a)-like ending remain plausible, but the intervening strokes and alphabet are not fully recoverable.', 'first_formula_full','low')
decision('implicit_decisions','I057-02','undecided',r"$r''(a)$ \inserted{$=\unsure{d_a|d(a)}r(a)$}",
         'The whole equation was inspected. The a lies below d, but an adjacent curved stroke could be a parenthesis. The page-local evidence does not settle subscript versus function notation.', 'extension','medium')
decision('implicit_decisions','I057-03','first','renforcement',
         'H marks this word doubtful. The initial r-e-n, tall crossed f and the following o-r-c-e-m-e-n-t run are legible in the enlarged crop.', 'strengthening','high')
decision('implicit_decisions','I057-04','first','pas',
         'H marks this word doubtful. The descending p and short a-s continuation appear after the comma and before un.', 'strengthening','high')
record['doubts'] = [
    dict(place='Cancelled quotient after the first live group', reading=r'\deleted{\unsure{\mathbb Z/r(a)}}',
         alternatives='Z/r(a); exact strokes and alphabet under crossing unresolved', confidence='low',
         reason='Several heavy cancellation and replacement strokes obscure the original quotient; not every character is plain.'),
    dict(place='Whole inserted multiplier identity', reading=r"$r''(a)$ \inserted{$=\unsure{d_a|d(a)}r(a)$}",
         alternatives=r'd_a | d(a)', confidence='medium',
         reason='The a is lowered below d, while a nearby curved stroke may belong to an opening parenthesis. Later clear d(a) occurrences do not override this local ambiguity.'),
]

inventory = [
    ('text','Top centre','13','his hand'),
    ('text','Main text, first five rows','On va peut-être se borner par la suite','his hand'),
    ('insertion','Above sur des','chacun','his hand'),
    ('text','First formula unit',r'$\mathbb Z_a/r(a)$; $(\mathbb Z_a=\mathbb Z\wedge_{\{\pm1\}}\omega(a))$','his hand'),
    ('deletion','After first live quotient',r'\unsure{\mathbb Z/r(a)}','his hand'),
    ('text','First operation and explanatory parenthesis','par une opération de contraction','his hand'),
    ('insertion','Above partiel / en a',r'\uline{uniforme}','his hand'),
    ('text','Second operation and explanatory parenthesis',"ou d'extension des groupes d'opérateurs",'his hand'),
    ('insertion','Above r-double-prime in the second operation',r'$=\unsure{d_a|d(a)}r(a)$','his hand'),
    ('deletion','After en a and comma in second parenthesis',')','his hand'),
    ('text','Remainder of second parenthesis','de multiplicateur d(a)','his hand'),
    ('insertion','Above gap between compte and que','ici','his hand'),
    ('text','Last statement through final parenthesis','On se rend compte ... le gommage partiel','his hand'),
    ('text','Lower-left corner','56; lighter folio annotation, attribution provisional','another hand'),
]
for i,(kind,position,words,hand) in enumerate(inventory,1):
    record['inventory'].append(dict(element=f'E{i:02}',sheet_kind='text',hand=hand,
        kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))

notes = [
 ('N01','The source proposes limiting later discussion to special erasing or added-marking operations. It describes their action separately on each concerned R_a torsor and writes the cyclic operator group and the twisted-integer definition of Z_a. The overwritten earlier quotient remains doubtful.'),
 ('N02','For partial uniform erasing, the source writes contraction from Z_a/r(a) to Z_a/r-prime(a), with r-prime(a) dividing r(a). For uniform added marking it writes extension to Z_a/r-double-prime(a), a multiple of r(a). The raised multiplier notation remains d_a versus d(a) uncertain; no mathematical expectation chooses the reading.'),
 ('N03','The last statement calls partial erasing a strengthening of structure, and says uniform added marking is defined combinatorially without supplementary structural data except the multipliers. The source uses singular le surmarquage uniforme and sera défini. This note records the claim without extending it to all cases.'),
 ('N04','The raised words chacun, uniforme and ici have visible attachment strokes. The source has no underlining beneath contraction or extension. Surmarquage uniforme is underlined, en a following it is not, and the final partiel has two underline strokes. The crossed closing parenthesis before de multiplicateur remains part of the diplomatic text.'),
 ('N05','Targeted mathematical check supplied by the main reader: for positive integers r-prime dividing r, let d=r/r-prime. The map [k] -> [d k] embeds Z/r-prime into Z/r. A Z/r torsor has d cosets of this subgroup, hence d possible retained uniform sub-torsors. Conversely, extension of a Z/r-prime torsor T by (T x Z/r)/(Z/r-prime), using that inclusion, is functorial and requires no choice beyond d. This checks the finite cyclic torsor distinction behind the final statement. It does not check the global surface construction or the r=0 case, and it is not evidence for the words contraction or the local d_a/d(a) notation.'),
 ('N06','H\'s doubtful renforcement and pas are legible in the strengthening crop. The old crossed quotient is not resolved. The tiny a under the inserted d is visibly lower than d; the possible adjacent parenthesis prevents a secure decision between subscript and argument notation.'),
 ('N07','The handwritten top number 13 and lower-left folio 56 are transcribed. The lighter footer annotation is provisionally attributed to another hand, without a firm authorship claim. Scan 57 is an editorial locator, not source ink. No independent diagram or pictorial drawing is present.'),
 ('N08','The original image was viewed once for layout and both prepared halves once line by line, including agreed readings. Eleven evidence places were cropped and directly inspected. The first_formula and singular crops initially clipped boundary strokes; fuller versions were made solely to complete those unresolved boundaries, and both versions are retained. The record cites first_formula_full and singular_full. The count of 27 comprises 21 main text rows, four separate interlinear addition rows and two handwritten number positions. No OCR, web source or TeX compilation was used.'),
]
for suffix,text in notes:
    record['notes'].append(dict(id=f'{PAGE}-{suffix}',text=text))
for suffix in ['N01','N02','N03']:
    record['check_events'].append(dict(statement_id=f'{PAGE}-{suffix}',
        type='carried as background without fault found',
        outcome='The statement and its notation were read against the assigned ink. This first-reader event is a transcription check, not an independent proof; the separate main-reader finite cyclic check is recorded at N05.'))
record['check_events'].append(dict(statement_id=f'{PAGE}-N05',type='targeted proof check',who='main reader',
    outcome='The main reader checked the finite cyclic case for positive r-prime dividing r: multiplication by d gives the subgroup inclusion, its torsor has d cosets, and contracted-product extension is functorial. This supports the choice-versus-extension distinction only within that scope; the surface construction and r=0 were not checked.'))

record['notation'] = [
 dict(sign=r'\mathbb Z',meaning_or_form='Z with two separated diagonal strokes, sometimes heavily retraced.',
      places='Seven live occurrences: three in the initial quotient/definition, two in the contraction pair, and two in the extension pair.',
      universality='All seven live Z letters were checked. The crossed earlier Z-like letter remains uncertain and is not used to extend the pattern.',
      witness_errors=r'H uses \mathbf{Z}; the doubled handwritten alphabet is retained as \mathbb Z.'),
 dict(sign=r'\pm1',meaning_or_form='Plus/minus with an upright joining the two bars, followed by the digit 1 inside braces below the wedge.',
      places='Definition of Z_a',universality='One occurrence on this page.',witness_errors='Neither witness changes this subscript; the full definition was checked beside the crossed quotient.'),
 dict(sign=r"r'(a), r''(a)",meaning_or_form='One prime for the contraction divisor and two for the extension divisor.',
      places='Both source/target comparisons and their following conditions.',universality='Each relevant prime count was inspected separately.',witness_errors='Both witnesses preserve the prime counts; they were not inferred from the argument.'),
 dict(sign=r'\unsure{d_a|d(a)}',meaning_or_form='Small a placed below d, with a nearby curved stroke that may be a parenthesis.',
      places='Raised multiplier identity above the second operation.',universality='This ambiguity is local. The later two d(a) occurrences have ordinary argument parentheses and are not rewritten as subscripts.',
      witness_errors='Both drafts confidently give d(a) at the raised identity. The local lower placement requires retained uncertainty.'),
 dict(sign='Flattened final n',meaning_or_form='A long low connection ending in a short downward flick.',
      places='Inserted chacun, opération, and the short en beside the leader.',universality='Checked at these three page-local disputed readings.',
      witness_errors='H misreads chacun as assez, pluralizes opération and leaves en a illegible.'),
 dict(sign='Curved insertion leader',meaning_or_form='A nonletter curve connecting a raised word to a gap on the main row.',
      places='chacun; uniforme; ici (angular V-shaped version).',universality='Three visibly attached word insertions.',
      witness_errors='H attaches the first raised word after nature, misses the insertion state of uniforme, and leaves ici illegible. The curve by en a is not a nested parenthesis.'),
]
record['abbreviations'] = []

def second(kind, box, reading):
    x0,y0,x1,y1=box
    record['second_boxes'].append(dict(box=f'B{len(record["second_boxes"])+1:02}',kind=kind,
        x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))

second('handwritten number',BOXES['opening'],r'\mspage{13}'+'\n'+'On va peut-être se borner par la suite')
second('insertion',BOXES['torseurs'],r'repères, ou de surmarquage, de nature spéciale, qui se traduisent, sur \inserted{chacun} des torseurs $R_a$ $(a\in A)$ concernés sous')
second('doubtful formula',BOXES['first_formula_full'],r'$\mathbb Z_a/r(a)\deleted{\unsure{\mathbb Z/r(a)}}$ $(\mathbb Z_a=\mathbb Z\mathbin{\wedge}_{\{\pm1\}}\omega(a))$,')
second('different words',BOXES['contraction'],r"de contraction des groupes d'opérateurs")
second('insertion',BOXES['partial'],r"de $\mathbb Z_a/r(a)$ à $\mathbb Z_a/r'(a)$, où $r'(a)\mid r(a)$ (opération de \uline{gommage partiel} \inserted{\uline{uniforme}} en $a$)")
second('doubtful formula',BOXES['extension'],r"ou d'extension des groupes d'opérateurs de $\mathbb Z_a/r(a)$ à $\mathbb Z_a/r''(a)$, où $r''(a)$ \inserted{$=\unsure{d_a|d(a)}r(a)$} est")
second('struck passage',BOXES['multiple'],r'un multiple de $r(a)$ (opération de \uline{surmarquage uniforme} en $a$, \deleted{)} de multiplicateur $d(a)$). On se rend compte \inserted{ici} que')
second('different words',BOXES['strengthening'],r'le gommage \uuline{partiel} est en fait un renforcement de structure, pas un')
second('different words',BOXES['singular_full'],r'affaiblissement, et inversement pour le surmarquage uniforme --- qui, au niveau combinatoire, sera défini sans donnée')
second('different words',BOXES['final'],r'de structure supplémentaire (sauf bien sûr les multiplicateurs $d(a)$).')
second('handwritten number',BOXES['folio'],r'\mspage{56}')

(ROOT/'proposed'/f'{PAGE}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,changes=len(record['changes']),decisions=len(record['decisions']),
                     implicit_decisions=len(record['implicit_decisions']),doubts=len(record['doubts']),
                     inventory=len(record['inventory']),second_boxes=len(record['second_boxes']))))
