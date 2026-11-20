import json
from pathlib import Path

ROOT = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
packet = json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan018.json').read_text())
candidate = (ROOT / 'reviews/143_scan018_readerA.tex').read_text()
boxes = {
    'tuple': [495,165,1475,275],
    'first-isom': [260,440,1125,572],
    'isom-diagram': [265,835,1040,1155],
    'replacement': [290,1145,735,1265],
    'margin': [1000,685,1650,1190],
    'prose-isom': [1180,1235,1535,1333],
    'unique-iso': [655,1310,1235,1450],
    'lower-cancellations': [320,2030,1645,2275],
    'final-pi': [1000,2225,1350,2337],
    'body-point': [900,1210,1205,1335],
    'body-ending': [235,1410,1540,1585],
}
changes = []
def add(place,C,H,final,against_C,against_H,kind,ink,confidence='high',crop='page',marked=False,consequential=False):
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=against_C,against_H=against_H,
                        kind=kind,ink=ink,confidence=confidence,
                        crop='page' if crop=='page' else f'crops/143_scan018_A_{crop}.png',
                        box=None if crop=='page' else boxes[crop],
                        marked_in_H=marked,consequential=consequential))
def alphabet(place,C,H,final,crop='page'):
    add(place,C,H,final,True,False,'misread symbol or index',
        'The large set letter has an angular upper sweep, an inward middle turn and a broad rounded lower bowl, the recurring ornate 3-shaped capital. Every occurrence at this place was inspected. Provisional alphabet encoding follows the main reader; it does not claim a separate mathematical object.',
        'medium',crop,False,False)
def extension(place,crop='page'):
    add(place,r'\mathcal E',r'\Sigma',r'\unsure{\mathcal E|\Sigma}',False,False,'other',
        'The rounded, doubled-curvature capital admits a cursive E or a rounded Sigma. This page does not settle the shared letter identification. Both witness readings remain in the candidate, so no correction against either is claimed here.',
        'medium',crop,False,True)

add('heading: after alpha',r'\uline{Définition de $\alpha$}',r'\emph{Définition de $\alpha$}.',
    r'\uline{Définition de $\alpha$}',False,True,'text not on the page',
    'The underline finishes below the heading. The space before On va définir contains no separate full stop.')
extension('defining tuple: first input','tuple')
alphabet('defining tuple: set input',r'Z',r'\mathfrak{Z}',r'\mathfrak Z','tuple')
add('defining tuple: between set input and suspension points',r'Z,\ldots',r'\mathfrak{Z}\ldots',
    r'\mathfrak Z\ldots',True,False,'text not on the page',
    'The points after the set letter have no separate downward-hooked comma like the comma following pi. Alphabet encoding is recorded separately.',
    'medium','tuple')
add('defining tuple: last output',r'\mathcal G,a',r'G, \sim',
    r'\mathcal G,\unsure{a|\sim}',False,False,'other',
    'After the last comma there is a short, low, wavy graph. No securely closed a-loop is visible, but the graph also is not an unambiguous mathematical tilde. The two readings remain open.',
    'low','tuple',False,True)
alphabet('first brace line: object set',r'Z/\pi',r'\mathfrak{Z}/\pi',r'\mathfrak Z/\pi')
alphabet('second brace line: both fibre arguments',r"(Z_j,Z_{j'})",r"(\mathfrak{Z}_j, \mathfrak{Z}_{j'})",
         r"(\mathfrak Z_j,\mathfrak Z_{j'})",'first-isom')
add('right edge of brace definition',r'\bigg|','[no witness]',r'\bigg|',False,True,'drawing or diagram',
    'A separate vertical rule stands to the right of the three definition lines, before the words d’où groupoïde.')
alphabet('canceled preliminary object formula',r'\widetilde\Pi_j=Z_j',r'\widetilde{\Pi}_j = \mathfrak{Z}_j',
         r'\widetilde\Pi_j=\mathfrak Z_j')
alphabet('replacement object declaration',r'\operatorname{Ob}\widetilde\Pi=Z',r'\mathrm{Ob}\,\widetilde{\Pi} ='+ '\n'+r'\mathfrak{Z}',
         r'\operatorname{Ob}\widetilde\Pi=\mathfrak Z')
alphabet('projection diagram: universal quantifier set',r'\forall z,z'+r"'\in Z",r'\forall z, z'+r"' \in \mathfrak{Z}",
         r'\forall z,z'+r"'\in\mathfrak Z",'isom-diagram')
add('projection diagram: end of discrete-category parenthesis',r'(\widetilde\Pi\text{ cat. discrète})',
    r'(\widetilde{\Pi} \text{ cat.\ discrète\ldots})',r'(\widetilde\Pi\text{ cat. discrète}\ldots)',
    True,False,'omission','Several short continuation marks follow discrète before the closing parenthesis. They are retained as suspension points.','medium','isom-diagram')
alphabet('projection diagram: lower RHS fibre arguments',r"(Z_j,Z_{j'})",r"(\mathfrak{Z}_j, \mathfrak{Z}_{j'})",
         r"(\mathfrak Z_j,\mathfrak Z_{j'})",'isom-diagram')
add('canceled parenthesis beneath the projection diagram',
    r"\deleted{(\unsure{où} $j,j'$ \unsure{les} \illegible{1})}",
    'une ligne biffée\nne se lit pas',
    r"\deleted{(\unsure{où} $j,j'$ \unsure{les} \unsure{images}\unsure{)}}",
    True,True,r'readable ink left as \ill{}',
    'The opening parenthesis and two j-graphs with the second prime survive the strike. Short strokes may be où and les; the last word shows a low sequence with a descender compatible with g and an ending like es, permitting only a tentative images. The final hook is not a secure independent closing parenthesis.',
    'low','replacement',True)
add('replacement parenthesis: signs over the two z letters',
    r"j=\dot z$, $j'=\dot z'",
    r"j = \bar z,\ j' = \bar z'",
    r"j=\dot z$, $j'=\dot z'",
    False,True,'misread symbol or index',
    'Both marks are compact round dark points above the z bodies, not extended horizontal bars. The second prime is a separate stroke.',
    'high','replacement',False,True)
add('right marginal note: left separator rule','[no witness]',
    'à droite, séparé par un trait vertical',r'\draw (0,0.20)--(0,-2.95);',
    True,False,'drawing or diagram',
    'A thin vertical rule separates the note from the central diagram. It is reproduced as a drawn stroke, not as editorial prose.',
    'high','margin')
add('right marginal note: leftward double-shaft pointer',r'\Longleftarrow','[no witness]',r'\Longleftarrow',
    False,True,'drawing or diagram',
    'The note has a leftward pointer made of two nearly horizontal strokes and a left-facing head, crossing the separator around the middle of the note.',
    'high','margin')
add('right marginal note: before foncteur',r'foncteur',r'\uncertain{un}'+'\n'+r'foncteur',r'foncteur',
    False,True,'text not on the page',
    'After par, the following main-line word begins with the tall f of foncteur. No separate un is visible between them.',
    'medium','margin',True)
add('right marginal note: interlinear qualification of foncteur',r'\inserted{\unsure{contr.}}',
    r'\struck{\ill{}}',r'\inserted{\unsure{contr.}}',False,True,'insertion or placement',
    'The small interlinear graph has an initial c, compressed middle strokes and a tall crossed stroke followed by a short terminal mark. A thin curved guide leads toward foncteur; it is an insertion, not a deleted main-line word. The precise abbreviation remains contr. with doubt.',
    'medium','margin',True)
add('right marginal note: curved attachment guide','[no witness]',r'\struck{\ill{}}',
    r'\draw[thin] (0.94,-0.64) .. controls (0.75,-0.66) and (0.57,-0.74) .. (0.45,-0.83);',
    True,True,'drawing or diagram',
    'A light curved attachment stroke runs from the little interlinear qualification toward foncteur, crossing the tall f region. The guide is distinct from the heavier letter strokes.',
    'medium','margin',True)
add('right marginal functor: after Ens',r'\operatorname{Ens}',r'\mathrm{Ens}$,',r'\operatorname{Ens}',
    False,True,'text not on the page',
    'Ens ends the functor line. The next line starts F(j); no dark comma intervenes after Ens.',
    'medium','margin')
alphabet('right marginal functor: object value',r'F(j)=Z_j',r'F(j) = \mathfrak{Z}_j',r'F(j)=\mathfrak Z_j','margin')
add('right marginal functor: after the object-value suspension points',r'$F(j)=Z_j,\ldots$',
    r'$F(j) = \mathfrak{Z}_j$, …,',r'$F(j)=\mathfrak Z_j,\ldots$',
    False,True,'text not on the page',
    'A comma precedes the short suspension marks. No additional comma follows them before the next lower formula.',
    'medium','margin')
add('right marginal equivalence: placement of /F',r'\widetilde\Pi\simeq\Pi/F',
    r'\widetilde{\Pi} \simeq \Pi_{/F}',r'\widetilde\Pi\simeq\Pi_{/F}',
    True,False,'misread symbol or index',
    'The slash and F are smaller and placed below the capital Pi’s main baseline. Their position is a subscript at the lower right.',
    'medium','margin',False,True)
add('body projection explanation: short form after inserted pi-',r'\inserted{$\pi$-}iso',r'isom.',
    r'\inserted{$\pi$-}isom',True,True,'misread word',
    'The i and s are followed by a short o-shaped stroke and then a separate low wavy m-like stroke. No detached period is visible after it. This revises my initial iso reading after main drew attention to the additional stroke. The pi- prefix is inserted above with an attachment curve.',
    'medium','unique-iso')
alphabet('body fibre map: source set',r'Z_j',r'\mathfrak{Z}_j',r'\mathfrak Z_j','unique-iso')
alphabet('body fibre map: target set',r"Z_{j'}",r"\mathfrak{Z}_{j'}",r"\mathfrak Z_{j'}",'unique-iso')
add('body fibre map: connecting stroke',r"Z_j\mathbin{-}Z_{j'}",
    r"\mathfrak{Z}_j \to \mathfrak{Z}_{j'}",r"\mathfrak Z_j\mathbin{-}\mathfrak Z_{j'}",
    False,True,'misread symbol or index',
    'The connector is a single near-horizontal shaft ending in a rounded thickening. Neither endpoint has an angled barb or raised triangular arrowhead. Alphabet changes are separate rows.',
    'high','unique-iso',False,True)
add('body projection explanation: suspension points after z prime',
    r"transformant $z$ en $z'\ldots.$",r"transformant $z$ en $z'$…",
    r"transformant $z$ en $z'\ldots.$",False,True,'omission',
    'Four distinct dark marks follow z prime: the first three compact points and a fourth short horizontal point. The four-point continuation in C is retained.',
    'high','body-ending')
add('lower paragraph opening: after Pour l’instant',r"Pour l'instant on",r"Pour l'instant, on",
    r"Pour l'instant on",False,True,'text not on the page',
    'The space after instant leads directly to on, with no independent comma stroke.')
extension('lower paragraph: after utilisé')
extension('lower paragraph: after l’op. de')
alphabet('lower paragraph: set on which the operation was unused',r'Z',r'\mathfrak{Z}',r'\mathfrak Z')
extension('lower paragraph: quotient group numerator')
extension('lower paragraph: action on tilde Pi')
extension('lower paragraph: Comme ... opère')
alphabet('lower paragraph: set in the Ens equality',r'Z',r'\mathfrak{Z}',r'\mathfrak Z')
add('lower paragraph: right side of the object-set equality',r'\operatorname{Ens}(\widetilde\Pi)',
    r'\mathrm{Ob}(\widetilde{\Pi})',r'\operatorname{Ens}(\widetilde\Pi)',False,True,'misread word',
    'The operator starts with an E-shaped graph and continues with the joined short n and s strokes; it is not the rounded O followed by a tall b used by Ob earlier on the page.',
    'high','page',False,True)
add('lower paragraph: between il opère and sur tilde Pi',r'\unsure{en fait}',r'\struck{\ill{}}',
    'en fait',False,True,'deletion state',
    'The short en is followed by the tall looped/descending f and the joined remainder of fait. The f descends below the baseline; there is no independent horizontal cancellation crossing the two words.',
    'medium','lower-cancellations',True,True)
add('lower paragraph: canceled opérant librement',r'\deleted{\unsure{opérant librement}}',
    r'\struck{\ill{}}',r'\deleted{\unsure{opérant librement}}',
    False,True,r'readable ink left as \ill{}',
    'The cancellation crosses a word beginning with an o-like loop and descending p at the right end of one line, then the continuation on the next line with tall strokes compatible with librement. Several middle letters remain obscured, so C’s phrase is retained only as a doubtful recovery.',
    'low','lower-cancellations',True)
add('lower paragraph: canceled article before pi',r'\deleted{le}',r'\struck{\ill{}}',r'\deleted{le}',
    False,True,r'readable ink left as \ill{}',
    'A tall loop of l and a small joined e remain under the thick horizontal strike immediately before the separate pi.',
    'high','lower-cancellations',True)
add('lower paragraph: abbreviation after par',r'$\Pi$-auto---',r'\uncertain{$\Pi$-automorphismes}',
    r'$\Pi$-auto---',False,True,'abbreviation expanded or spelling modernised',
    'After the capital Pi and its hyphen, the source has auto followed by a long continuation dash. The letters morphismes are not present.',
    'high','lower-cancellations',True)
add('last line: target after sur',r'\unsure{\pi|\Pi}',r'\Pi',r'\pi',
    False,True,'misread symbol or index',
    'The right leg curves sharply inward toward the left stem, matching the lowercase pi immediately before opère above. The capital Pi in Pi-auto has two more clearly separated upright legs. The source’s lowercase graph is preserved without repairing the assertion.',
    'medium','final-pi',False,True)
add('bottom-left pencil pagination',r'\mspage{17}','[no witness]',r'\mspage{17}',
    False,True,'omission',
    'A faint pencil 1 followed by the angled 7 is present at the bottom left. No evidence on this sheet identifies the person who wrote it.')

decisions = []
def decide(id,decision,reading,ink,crop,confidence):
    decisions.append(dict(id=id,decision=decision,reading=reading,ink=ink,
                          crop=f'crops/143_scan018_A_{crop}.png',box=boxes[crop],confidence=confidence))
decide('M0691','first',r'\operatorname{Isom}',
       'The serifed capital I and closely joined curled s form a compact outline that can resemble H. The following o and m are present; the same I+s construction occurs on the left of the equality.',
       'first-isom','high')
decide('M0692','first',r'\operatorname{Isom}',
       'The RHS starts with the same small serifed I joined to a curved s as the left-hand Isom. It is not a single H followed directly by om.',
       'isom-diagram','high')
decide('M0693','first','si',
       'A curved s is followed by a short i with a separate dot. There is no round initial o or accented u.',
       'replacement','high')
decide('M0694','undecided',r'\unsure{contr.}',
       'Initial c, compressed middle strokes and a tall crossed stroke with a terminal short mark support contr.; the minute joining strokes do not securely establish every letter. Its insertion attachment is clearer than its full spelling.',
       'margin','medium')
decide('M0695','first',r'\operatorname{Isom}',
       'A serifed I is joined closely to the s, creating a broad double-curved outline. It continues into compressed om, matching the two formula occurrences.',
       'prose-isom','high')
decide('M0696','first','en fait',
       'The phrase has en followed by the tall descending f and the joined small letters of fait. The long f stroke is part of the letter, not a cancellation of the phrase.',
       'lower-cancellations','medium')
decide('M0697','first',r'\pi',
       'The top stroke feeds an inward-curving right leg that approaches the left stem, like the preceding lowercase pi before opère. This differs from the separated vertical legs of Pi-auto. No mathematical correction to capital Pi is made.',
       'final-pi','medium')

inventory = []
def inv(n,kind,position,words,hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=f'E{n:02d}',kind=kind,
                          position=position,first_words_or_objects=words,transcribed='yes'))
inv(1,'margin note','top right','9','unnamed hand (pencil)')
inv(2,'text','top line','underlined Définition de alpha; On va définir')
inv(3,'display','below heading','alpha(input tuple) = output tuple')
inv(4,'display','upper quarter, three-line brace','Ob Pi; Isom(j,j prime); composition des flèches évidente')
inv(5,'drawing','right of the three-line brace','vertical rule before d’où groupoïde Pi')
inv(6,'deletion','below the first definition','tilde Pi subscript j = ornate Z subscript j')
inv(7,'display','same line as canceled formula, to its right','Ob tilde Pi = ornate Z')
inv(8,'diagram','central upper half','Isom(z,z prime)={pt}; for all z,z prime; downward arrow; lower Isom equality; cat. discrète with continuation points')
inv(9,'deletion','beneath central diagram','canceled parenthesis: doubtful où; j,j prime; doubtful les images and closing parenthesis')
inv(10,'insertion','above canceled parenthesis, beneath lower diagram row','si j=dot z, j prime=dot z prime')
inv(11,'margin note','right of central diagram','tilde Pi cat. underlined discrète sur Pi définie par foncteur')
inv(12,'drawing','left edge of the right marginal note','vertical separating rule')
inv(13,'drawing','middle of marginal rule','double-shaft leftward pointer')
inv(14,'insertion','above foncteur in right note','doubtful contr.')
inv(15,'drawing','between contr. and foncteur','thin curved attachment guide')
inv(16,'diagram','middle of right note','F: Pi circle to Ens, rightward arrow')
inv(17,'display','below functor arrow in right note','F(j)=ornate Z subscript j, suspension points')
inv(18,'display','bottom of right note','tilde Pi approximately Pi subscript /F')
inv(19,'text','middle to lower half','down arrow transforme l’unique pt de Isom(z,z prime) ... transformant z en z prime, four suspension marks')
inv(20,'insertion','above isom in projection explanation','pi- prefix with attachment curve')
inv(21,'text','lower half','Pour l’instant ... de façon compatible.')
inv(22,'text','bottom paragraph','Comme ... Ens(tilde Pi) ... en fait ... passage au quotient.')
inv(23,'deletion','end of the cat. discrète associée line and start of next line','doubtful opérant librement')
inv(24,'deletion','before pi opère','le')
inv(25,'margin note','bottom left','17','unnamed hand (pencil)')

remaining = []
def doubt(place,reading,alternatives,confidence,reason):
    remaining.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
for place in ['defining tuple first input','after utilisé','after l’op. de','quotient numerator','before sur tilde Pi','after Comme']:
    doubt('action-group letter: '+place,r'\unsure{\mathcal E|\Sigma}',r'\mathcal E or \Sigma','medium',
          'The rounded capital still fits both graphic identifications; this page supplies no independent decisive contrast. Shared uncertainty retained at this exact occurrence.')
doubt('defining tuple final output',r'\unsure{a|\sim}',r'a or \sim','low',
      'A low wavy graph lacks a secure a-loop. Mathematical expectations have not been used to choose. Crop: 143_scan018_A_tuple.png.')
doubt('canceled old parenthesis, initial word',r'\unsure{où}','où; the struck letters are not fully recoverable','low',
      'The cancellation obscures the rounded joining strokes. Crop: 143_scan018_A_replacement.png.')
doubt('canceled old parenthesis, word after j,j prime',r'\unsure{les}','les; incomplete visible letter sequence','low',
      'The short word lies directly beneath the heavy strike. Crop: 143_scan018_A_replacement.png.')
doubt('canceled old parenthesis, final noun',r'\unsure{images}','images; partly unreadable word','low',
      'A possible g descender and es-like ending support only a tentative recovery. Crop: 143_scan018_A_replacement.png.')
doubt('canceled old parenthesis, closing punctuation',r'\unsure{)}','closing parenthesis or terminal remnant of canceled writing','low',
      'There is a short hooked terminal stroke but no securely independent full closing parenthesis. Crop: 143_scan018_A_replacement.png.')
doubt('marginal insertion above foncteur',r'\unsure{contr.}','contr.; exact middle letters uncertain','medium',
      'The word is an insertion, but its minute central joins remain indistinct. Crop: 143_scan018_A_margin.png.')
doubt('lower canceled phrase across the line break',r'\unsure{opérant librement}','opérant librement; several crossed middle letters unrecoverable','low',
      'The visible initial loops and tall strokes support C’s reading without making the entire phrase secure. Crop: 143_scan018_A_lower-cancellations.png.')

certainty = [
    dict(place='M0691 first definition RHS',C=r'\unsure{\operatorname{Isom}|\operatorname{Hom}}',final=r'\operatorname{Isom}',ink='Serifed I plus joined s, confirmed against the left-hand occurrence.'),
    dict(place='M0692 projection diagram RHS',C=r'\unsure{\operatorname{Isom}|\operatorname{Hom}}',final=r'\operatorname{Isom}',ink='Compact I+s construction followed by om.'),
    dict(place='M0693 inserted parenthesis',C=r'\unsure{si|où}',final='si',ink='Curved s and separately dotted i.'),
    dict(place='M0695 prose Isom',C=r'\unsure{\operatorname{Isom}|\operatorname{Hom}}',final=r'\operatorname{Isom}',ink='Joined I+s outline matches both formula occurrences.'),
    dict(place='M0696 lower paragraph',C=r'\unsure{en fait}',final='en fait',ink='Visible en and tall f with the following small letters; no independent cancellation stroke.'),
    dict(place='M0697 final target',C=r'\unsure{\pi|\Pi}',final=r'\pi',ink='Inward-curved right leg matches the preceding lowercase pi rather than the separated capital Pi legs.'),
]
notation = [
    dict(form=r'\mathfrak Z',meaning='The set with a pi action used in the construction.',evidence='Provisional encoding of each ornate 3-shaped capital, confirmed occurrence by occurrence; alphabet choice is medium-confidence and not a mathematical correction.'),
    dict(form=r'\unsure{\mathcal E|\Sigma}',meaning='The action/extension group whose quotient by pi is the G of the page.',evidence='Same rounded capital at all six occurrences; unresolved graphic identification carried from the shared notation.'),
    dict(form=r'\Pi,\widetilde\Pi,p',meaning='The two categories/groupoids and the displayed projection in the stated construction.',evidence='Defining tuple, object declarations and central downward arrow.'),
    dict(form=r'j=\dot z,\ j'+"'"+r'=\dot z'+"'",meaning='The page’s labels for the images of z and z prime.',evidence='Both overmarks in the inserted parenthesis are round dots, not bars.'),
    dict(form=r'F:\Pi^\circ\longrightarrow\operatorname{Ens}',meaning='Functor used in the right marginal account.',evidence='The source arrow has a rightward head and the Pi bears a small circle.'),
    dict(form=r'\Pi_{/F}',meaning='The category in the marginal equivalence with tilde Pi.',evidence='The slash and F sit low at the right of the capital Pi.'),
    dict(form=r'\mathbin{-}',meaning='Literal shaft between the two fibres in the projection explanation.',evidence='The connector has no visible arrowhead; no arrow is supplied.'),
]
abbreviations = [
    dict(form='Ob',expansion='objets'),
    dict(form='Isom',expansion='isomorphismes'),
    dict(form='pt',expansion='point'),
    dict(form='cat.',expansion='catégorie'),
    dict(form='isom',expansion='isomorphisme'),
    dict(form='op.',expansion='opération'),
    dict(form='auto---',expansion='automorphismes (expansion only here, not supplied in the transcription)'),
    dict(form='contr. [doubtful]',expansion='contravariant [the source abbreviation itself remains doubtful]'),
]
hand_log = [
    dict(habit='Ornate capital set letter resembles a large 3 with a high angular entry and broad lower bowl.',places='143_scan018: tuple; object quotient; two fibre arguments in each Isom expression; canceled preliminary formula; replacement object declaration; universal quantifier; F(j); both fibres in the body map; both lower prose set references.',scope='All capital-set occurrences on this page inspected; provisional mathfrak Z encoding only.',misreadings='C uses plain Z; H’s mathfrak Z is retained as a provisional alphabet match.'),
    dict(habit='Serifed I closely joined to s resembles an H-like or double-curved initial.',places='143_scan018: first definition RHS, lower central diagram RHS and prose Isom.',scope='All three marked Isom/Hom loci compared with neighboring unabbreviated Isom graphs.',misreadings='C doubts Isom/Hom at all three; Isom selected.'),
    dict(habit='Lowercase pi has an inward-curved right leg that can approach or meet its left stem.',places='143_scan018: pi before opère and final target after sur; compared with capital Pi in Pi-auto.',scope='The final disputed graph is matched only to these within-page exemplars.',misreadings='H uses capital Pi at the final target; lowercase pi is selected at medium confidence, without repairing the statement.'),
    dict(habit='A tall descending f can resemble a cancellation when it crosses space below the word.',places='143_scan018: live en fait in the bottom paragraph.',scope='Specific phrase only.',misreadings='H represents en fait as struck illegible text; the phrase is live.'),
    dict(habit='Compact round overmarks are distinct from the adjacent primes.',places='143_scan018: inserted j=dot z, j prime=dot z prime.',scope='Both overmarks inspected in the single crop.',misreadings='H changes both dots to bars.'),
    dict(habit='Rounded action-group capital remains graphically compatible with both cursive E and Sigma.',places='143_scan018: tuple and five lower prose/formula occurrences.',scope='All six occurrences inspected; no page-local resolution.',misreadings='C E and H Sigma remain alternative identifications.'),
    dict(habit='Short forms and continuation strokes remain literal.',places='143_scan018: isom; Pi-auto---; four points after z prime; pt in the body.',scope='These exact loci checked. Reader A judges the body t foot close to the p-bowl baseline and retains pt. Main sees a raised t and will record that positional ambiguity in adjudication.',misreadings='C’s iso omits the separate low m-like stroke; H’s period after isom is not separately visible. H expands auto--- and reduces the final four points to an ellipsis.'),
    dict(habit='Pencil pagination is recorded without identifying the writer.',places='143_scan018: 9 at top right and 17 at bottom left.',scope='Both pencil numerals present on this sheet; no independent identifying evidence.',misreadings='H’s editorial attribution de l’auteur is not adopted as source evidence.'),
]
notes = [
    dict(id='143_scan018-N1',text='The page states a definition of alpha by constructing Pi, tilde Pi and p from the action data. It defines the objects of Pi as the orbit set, writes the Isom sets in terms of the fibres and describes composition as evident. The canceled preliminary formula and the replacement object declaration are retained. This is an account of what the manuscript says, not a proof of the construction.'),
    dict(id='143_scan018-N2',text='The central diagram and the following prose describe the projection of the unique point of Isom(z,z prime) to a pi-isomorphism carrying z to z prime. The right margin calls tilde Pi discrete over Pi, supplies a functor F and writes an equivalence with Pi subscript /F. The uncertain insertion contr. and the canceled old parenthesis remain visibly marked. No mathematical proof was performed.'),
    dict(id='143_scan018-N3',text='The lower paragraph says that the action-group letter had not yet been used, then describes compatible actions on Pi and tilde Pi and a quotient passage. Its literal final target is read as lowercase pi from the graph, although the preceding sentences discuss capital Pi. This potential source slip is not silently repaired, and no claim about the mathematical validity of the sentence is made.'),
    dict(id='143_scan018-N4',text='Graphic decisions follow the ink: dots over z in the replacement, Ens rather than Ob in the lower equality, a bare shaft between fibres, four suspension points after z prime, and unexpanded isom and Pi-auto---. The tuple’s last entry a versus tilde remains unresolved. After main highlighted the extra low stroke, isom replaces Reader A’s initial iso; no detached period is supplied. Reader A retains baseline pt as its positional judgment; main sees a raised t and will record this ambiguity explicitly in adjudication.'),
    dict(id='143_scan018-N5',text='Both pencil page numerals are transcribed, with the hand unnamed. H’s page attribution, margin descriptions, quotation marks around descriptions and report of an unreadable line are editorial matter rather than extra manuscript words. The source graphic features they describe are reconstructed.'),
    dict(id='143_scan018-N6',text='Main subsequently reported an isolated dark point after the first Z/pi quotient and before (soit J), near original coordinates x647,y360. Reader A did not securely register that point in the original/half reading and has not inspected the main-created crop. No punctuation is supplied on that report alone; this is left for main’s direct adjudication.'),
]
check_events = [
    dict(statement_id='143_scan018-N1',type='carried as background without fault found',outcome='Only transcription and within-page comparison of letter forms were performed. The definition and composition assertion were not proved or independently rechecked mathematically.'),
    dict(statement_id='143_scan018-N2',type='carried as background without fault found',outcome='Objects, strokes, indices and insertion/deletion states were visually checked. The fibre-isomorphism assertion and marginal equivalence were not proved.'),
    dict(statement_id='143_scan018-N3',type='carried as background without fault found',outcome='The action statements were transcribed without a mathematical proof check. The final lowercase pi is an ink-based choice, not a conclusion that the quotient-action assertion is valid.'),
]

raw_actions = [
    'Scan/page metadata syntax only; original and both pencil numbers inspected.',
    'H attribution de l’auteur is editorial; both pencil numerals have unnamed hand in the inventory.',
    'Heading has no full stop; changes row heading.',
    'Tuple action-group identification remains E|Sigma; changes row tuple first input.',
    'No separate comma after set input; changes row tuple punctuation.',
    'Raw tokenization suppresses H tilde; actual witnesses inspected and final tuple entry left a|tilde.',
    'H thin-space macro after Ob is not a source comma; formatting-only.',
    'M0691 settled Isom; decisions and certainty resolutions.',
    'Right vertical separator preserved; drawing row.',
    'Display delimiter syntax only.',
    'H thin-space macro after Ob is not source punctuation; formatting-only.',
    'Display/environment syntax only.',
    'Diagram environment syntax only; all objects and arrow visually inspected.',
    'Downward arrow is in both representations; no substantive direction difference.',
    'Environment syntax only; actual continuation points after discrète separately restored.',
    'M0692 settled Isom; decisions and certainty resolutions.',
    'Canceled parenthesis inspected and tentatively recovered with doubts; deletion row.',
    'M0693 settled si; the independently wrong bars in H are corrected to dots.',
    'H margin-location description replaced by source graphic; separator and pointer inventoried and reproduced.',
    'No separate un before foncteur; changes row.',
    'Interlinear contr. remains doubtful but insertion state and guide retained; changes rows and M0694.',
    'Functor arrow macro difference only; visible right arrowhead confirmed.',
    'No comma after Ens; punctuation row.',
    'C already has suspension points despite raw tokenizer; no extra comma after them, punctuation row.',
    'Low /F is a subscript; changes row.',
    'H editorial quotation and unreadable-line report excluded; actual canceled line retained with doubts.',
    'M0695 settled Isom; decisions and certainty resolutions.',
    'H editorial interline description maps to the same inserted pi-; source insertion retained.',
    'The extra low m-like stroke supports isom, revising C iso; no detached period is supplied. Main alerted Reader A to that stroke after inspecting the existing crop.',
    'Bare connecting shaft retained; H arrowhead unsupported.',
    'Four suspension marks confirmed; C retained and H third-point ellipsis incomplete.',
    'No comma after Pour l’instant; changes row.',
    'Action-group occurrence after utilisé remains E|Sigma.',
    'Action-group occurrence after l’op. de remains E|Sigma.',
    'Action-group occurrence in quotient numerator remains E|Sigma.',
    'Action-group occurrence before action on tilde Pi remains E|Sigma.',
    'Action-group occurrence after Comme remains E|Sigma.',
    'Ens selected from letters; H Ob rejected.',
    'Live en fait selected; H strike rejected, M0696 and changes row.',
    'Canceled opérant librement tentatively recovered, with doubt retained.',
    'Canceled le is readable and retained.',
    'Literal Pi-auto--- retained without expansion.',
    'M0697 chooses lowercase pi from within-page stroke comparison; H Pi not imposed.',
    'Bottom pencil 17 retained; omission row.',
]
assert len(raw_actions)==len(packet['differences']), (len(raw_actions),len(packet['differences']))
report = dict(
    key='143_scan018',reader='A',stage='first',
    image_views=['original','half1','half2']+[f'crops/143_scan018_A_{k}.png' for k in boxes],
    changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining,
    certainty_resolutions=certainty,notation=notation,abbreviations=abbreviations,
    hand_log=hand_log,notes=notes,check_events=check_events,
    unresolved_for_main=[
        'Six action-group capitals remain E|Sigma: defining tuple; after utilisé; after l’op. de; quotient numerator; action on tilde Pi; after Comme. Representative crop: crops/143_scan018_A_tuple.png; all occurrences inspected in halves.',
        'Tuple final output a|tilde: crops/143_scan018_A_tuple.png.',
        'Canceled old parenthesis: doubtful où, les, images and closing parenthesis: crops/143_scan018_A_replacement.png.',
        'Marginal contr. spelling remains doubtful although insertion status is supported: crops/143_scan018_A_margin.png.',
        'Canceled opérant librement remains a tentative recovery: crops/143_scan018_A_lower-cancellations.png.',
        'Body pt versus p with superscript t: crops/143_scan018_A_body-point.png. Candidate retains Reader A’s baseline-t judgment; main judges raised t and has undertaken to record this positional ambiguity during adjudication.',
        'Main reported an isolated point after the first Z/pi and before (soit J), around x647,y360. Reader A did not securely identify it in the original/half view and has not inspected main’s new crop; punctuation versus stray ink is for main.',
    ],
    raw_difference_disposition='All '+str(len(raw_actions))+' packet differences inspected against the image, not just the marks. Pure markup, math spacing and editorial descriptions do not constitute extra source text. All additional alphabet, dot, arrow and deletion-state findings are recorded separately. For unresolved C/H symbol conflicts, against_C and against_H are both false because neither witness is conclusively rejected. Alphabet-only rows have medium confidence and consequential false. Detailed packet-order disposition:\n'+'\n'.join(f'{i+1}. {x}' for i,x in enumerate(raw_actions)),
)
assert [d['id'] for d in decisions]==[m['id'] for m in packet['marks']]
for n,row in enumerate(changes,1):
    for field,witness in [('C','witness_C'),('H','witness_H')]:
        if row[field]!='[no witness]' and row[field] not in packet[witness]:
            raise ValueError(f'Change {n} {field} is not exact: {row[field]!r}')
    if row['final'] not in candidate:
        raise ValueError(f'Change {n} final is not exact: {row["final"]!r}')
    if row['crop']!='page' and not (ROOT/row['crop']).exists():
        raise ValueError(row['crop'])
path=ROOT/'reviews/143_scan018_readerA.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {path}: {len(changes)} changes, {len(decisions)} original marks, {len(inventory)} inventory elements, {len(remaining)} remaining-doubt records.')
