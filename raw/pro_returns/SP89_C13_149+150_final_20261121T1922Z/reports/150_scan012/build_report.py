from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/8759b8008681')
PAGE = '150_scan012'
OUT = ROOT / 'work/reports' / PAGE
C = (ROOT / 'packets' / PAGE / 'C.tex').read_text()
H = (ROOT / 'packets' / PAGE / 'H.tex').read_text()
D = (OUT / 'draft.tex').read_text()
BOX = json.loads((OUT / 'crop_boxes.json').read_text())

def between(s, first, last):
    start = s.index(first)
    end = s.index(last, start) + len(last)
    return s[start:end]

def macro(s, start):
    i = s.index(start)
    j = s.index('{', i)
    n = 1
    k = j + 1
    while n:
        n += (s[k] == '{') - (s[k] == '}')
        k += 1
    return s[i:k]

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

nb_c = macro(C, r'\margin{\uline{NB}')
nb_h = macro(H, r'\marginal{\emph{NB}')
nb_d = macro(D, r'\margin{\uline{NB}')
hom_c = macro(C, r'\margin{donc')
hom_h = macro(H, r'\marginal{donc')
hom_d = macro(D, r'\margin{donc')
star_c = macro(C, r'\margin{$^{*}$')
star_h = macro(H, r'\marginal{* Cela')
star_d = macro(D, r'\margin{\uline{$^{*}$}')
diagram_c = between(C, r'\begin{tikzcd}', r'\end{tikzcd}')
diagram_h = between(H, r'\begin{tikzcd}', r'\end{tikzcd}')
diagram_d = between(D, r'\begin{tikzcd}', r'\end{tikzcd}')
situation_d = between(D, r'Y\mathrel{\tikz', r'\dot T,')[:-1]
situation_full_d = between(D, r'aussi que la situation', r'\mathbf{I}\times T-T)$')
tail_d = between(D, r'\deleted{\unsure{son intersection}}', r'\mathbf{I}\times\dot T$}}')

R = {
    'page': PAGE, 'reader': 'reader_b', 'line_count': len(D.splitlines()),
    'changes': [], 'decisions': [], 'inventory': [], 'audit_boxes': [],
    'doubts': [], 'notes': [], 'check_events': [], 'notation': [],
    'abbreviations': [], 'hand': [], 'diff_coverage': [],
    'deletion_insertion_review': []
}

def change(id, p, place, c, h, final, evidence, confidence='high',
           kind='misread symbol or index', against_c=True, against_h=True,
           marked_in_h=False, consequential=False, error_category='1'):
    R['changes'].append(dict(id=id, place=place, c=c, h=h, final=final,
        evidence=evidence, crop=f'crops/{PAGE}_{p}.png', box=BOX[p],
        confidence=confidence, kind=kind, against_c=against_c,
        against_h=against_h, marked_in_h=marked_in_h,
        consequential=consequential, error_category=error_category))

change('P00a','P00','Upper-left author folio',r'\mspage{1}',r'« 1) »',r'\mspage{1)}',
       'The upright 1 is followed by a separate large right parenthesis, curved under the digit. C drops that closing stroke; H quotes it correctly.',
       against_h=False,kind='omission',error_category='3')
change('P00b','P00','Circled Roman I beneath the author folio',r'\textcircled{I}',r'(I)',r'\textcircled{I}',
       'One Roman I, with detached roof and foot, is enclosed by an oval; it is not a pair of ordinary parentheses. H explicitly substitutes (I) in its note.',
       against_c=False,kind='other',error_category='10')
change('P01','P01','Title and its replacement word',
       between(C,'Espaces stratifiés',r'\inserted{coniques})'),
       r'Espaces stratifiés (étude par voisinages \struck{tubulaires} coniques)',
       between(D,'Espaces stratifiés',r'\inserted{coniques})'),
       'The title is written across the top. Tubulaires has a cancellation line; coniques is written underneath as its replacement, ending before the closing parenthesis. The dark pale-edged stain above is substrate, not a letter. H carries the title inside editorial prose and does not encode the insertion.',
       kind='insertion or placement',against_c=False,error_category='6')
change('P02','P02','Opening definition: underlining of voisinage and cancelled tubulaire',
       r'\uline{voisinage \deleted{tubulaire}}',r'\emph{voisinage} \struck{tubulaire}',
       r'\uline{voisinage \deleted{tubulaire}}',
       'A continuous lower horizontal stroke runs under voisinage and the crossed tubulaire. The replacement conique has a separate underline. The clipped final e of conique is newly doubted, not completed.',
       kind='other',against_c=False,error_category='10')
change('P03a','P03','Inserted parenthetical absolu',
       r'\inserted{(\uline{``absolu\'\'})}',
       r'(« \uncertain{absolu} »)',r'\inserted{(``\uline{absolu}\'\')}',
       'The letters a-b-s-o-l-u are separable, including the tall b and l and final u. Both quote signs consist of two short ticks rather than guillemets. The independent underline spans the word only, and both parentheses are visible. This also resolves H\'s lexical doubt.',
       kind='other',marked_in_h=True,error_category='10')
change('P03b','P03','Inserted ou cône sur Y phrase',
       r'\inserted{(ou ``cône sur $Y$\'\')}',r'(ou « cône sur $Y$ »)',
       r'\inserted{(ou ``cône sur $Y$\'\')}',
       'Two paired short quotation ticks surround cône sur Y. Its leader curves left over the following live line and attaches the raised parenthesis after the struck Y; it does not cancel that live line.',
       kind='insertion or placement',against_c=False,error_category='6')
change('P03c','P03','Live est un espace following the insertion',
       'est un espace topologique',r'\struck{est un espace} est un espace topologique',
       'est un espace topologique',
       'There is one sequence est un espace. The long stroke above it continues from the parenthetical insertion leader; no second word bodies or independent strike are present. H duplicates the words as a cancelled copy.',
       kind='text not on the page',against_c=False,error_category='9')
change('P04','P04','First space T and crossed low-right token',
       r'$\bar T\deleted{\unsure{_Y}}$',r'$T$ \struck{\ill{}}',
       r'$T\deleted{\unsure{_Y}}$',
       'The live T has one detached roof and a hooked upright; there is no second horizontal stroke for a bar. A small cancelled low-right form remains compatible with Y, but the crossing hides its independent legs. Keep the C candidate doubtful against H\'s unreadable token.',
       confidence='medium',marked_in_h=True,consequential=True)
change('P06a','P06','Punctuation after contenant Y',r'contenant $Y$',r'contenant $Y$,',r'contenant $Y$,',
       'A separate dark curved comma lies below and right of Y at approximately x1565–1585, y374–391. It was outside the bottom edge of P04 and is complete in P06.',
       kind='omission',against_h=False,error_category='3')
change('P05','P05','Quoted underlined tube',r'(le ``\uline{\unsure{tube}}\'\'),',r'(le « \emph{tube} »),',r'(le ``\uline{tube}\'\'),',
       'The initial t has a tall stem, u is low, b has its own ascender and closed lower body, and the final e is distinct. This resolves C M0307. The underline covers only tube; the two quotation ticks on each side, closing parenthesis and comma remain separate.',
       kind='misread word',error_category='2')
change('P06b','P06','Cancelled word after dot T and before le bord',
       r'$\dot T$'+'\n'+r'(le ``bord\'\' du tube\'\')',
       r'$\dot T$ (le « bord du tube »)',
       r'$\dot T$'+'\n'+r'\deleted{\illegible{1}} (le ``bord\'\' du tube\'\')',
       'Below/right of the dotted T and before the opening parenthesis, a short textual group has several low humps and a final upright under a distinct heavy cancellation. Not every letter can be recovered; muni would exceed the evidence. Both witnesses omit this cancelled word.',
       confidence='low',kind='omission',error_category='3')
change('P06c','P06','Closing quotation after bord',r'(le ``bord\'\'',r'(le « bord',r'(le ``bord\'\'',
       'Two short high closing ticks occur immediately after bord. They are independent of the following line, so the quotation is not regularized into H\'s single pair around bord du tube.',
       kind='other',against_c=False,error_category='10')
change('P07','P07','Extra closing quotation after du tube',r'du tube\'\')',r'du tube »)',r'du tube\'\')',
       'The next line ends tube, two further high closing ticks, then a separate right parenthesis. There is no new opening quotation on this line. Preserve the unmatched additional pair.',
       kind='other',against_c=False,error_category='10')
change('P08a','P08','Interval monoid and the overworked following mark',
       r'$I=[0,1]$',r'$\mathbf{I}=[0,1]$',r'$\mathbf{I}=[0,1]\,\unsure{}$',
       'The I has a broad filled vertical body and distinct top/bottom serifs. After the closing bracket a small dark overworked glyph has a tiny counter and a short low return. Its identity and whether it was cancelled cannot be settled; both witnesses omit that present ink. The empty unsure is the established convention for unreadable mathematical ink, not an absent token.',
       confidence='medium',kind='omission',consequential=True,error_category='3')
change('P08b','P08','Action on T, notée',r'sur $\bar T$, notée',r'sur $T$, notée',r'sur $T$, notée',
       'The roof and hooked descending stem make a single T. There is no independent upper bar; the comma and accent in notée remain visible.',against_h=False,consequential=True)
change('P09','P09','Whole numbered action formula (1)',
       between(C,r'(1)\qquad',r'\qquad I\times\bar T\longrightarrow\bar T'),
       between(H,r'(1)\qquad',r'\qquad \mathbf{I}\times T\longrightarrow T'),
       between(D,r'(1)\qquad',r'\qquad \mathbf{I}\times T\longrightarrow T'),
       'The label is (1); the first arrow has a left mapping bar and right head. The second has a rounded/retraced right head. Its I is broad with serifs, while each T has just one roof. The small unanchored speck above the shaft has no secure glyph attachment and is not transcribed.',against_h=False,consequential=True)
change('P10a','P10','Axiom b): crossed token before the live T',
       r'b)&0.\deleted{\unsure{\bar T}}\bar T\subset Y',r'b) $0.\,T\subset Y$ \struck{\ill{}}',
       r'b)&0.\deleted{\unsure{T|\bar T}}T\subset Y',
       'The crossed body lies between 0. and the live T, not after Y. The live T has one roof; the old body remains T-like but its crossing prevents deciding whether an extra bar belonged to it. The y descender from a) above is not itself a deletion. The relation is a curved subset without an equality bar.',
       confidence='medium',kind='insertion or placement',marked_in_h=True,consequential=True,error_category='6')
change('P10b','P11','Brace grouping a) and b) with the right margin note',
       r'\end{array}',r'à droite de a) b), réunis par une accolade.',r'\end{array}\right\}',
       'A single continuous right brace stands alongside the two axiom lines, with upper/lower returns and the central inward angle. It links a), b) to the right marginal deduction; no extra condition is enclosed.',
       kind='drawing or diagram',against_h=False,error_category='4')
change('P11','P11','Complete right marginal homotopy statement',hom_c,hom_h,hom_d,
       'The live words after (pour lambda=1) are sur une, followed by the underlined rétraction, then de T sur Y. There are no additional word bodies for H\'s à l’application ... de T; those arise from adjoining main-text d’applications. Rétraction has a dotted i and compressed on-like continuation on the same lower baseline, without a separate raised suffix or abbreviation stop. Pts is abbreviated; au cours has distinct low au and the initial c of cours. Every T has one roof and the lambda/id subscripts are T. The margin continues to homotopie without a secure terminal stop.',
       confidence='medium',kind='misread word',marked_in_h=True,consequential=True,error_category='2')
change('P12a','P12','NB: weak form of b)',r'La condition b) \unsure{sous sa forme faible}',
       r'La condition b) \uncertain{peut se} formuler \uncertain{plus faiblement}',
       r'La condition b) sous \unsure{sa|la} forme faible',
       'Sous has the initial low s and terminal s, forme has the f ascender and m humps, and faible ends with a tall l and final e. The intervening article has no secure independent l ascender: sa remains preferred, la is retained as a local alternative. This is not H\'s peut se formuler plus faiblement.',
       confidence='medium',kind='misread word',against_c=False,marked_in_h=True,error_category='2')
change('P12b','P12','NB: plus la condition c) and its parenthesis',
       'plus la condition c)\n'+r'(\unsure{à qui celle-ci donne un sens})',
       r'alors la condition c) (qui \struck{\ill{}} donne \ill{})',
       'plus la condition c)\n(à qui celle-ci donne un sens)',
       'Plus begins with a descending p and tall l; the parenthesis has à, a q descender in qui, two tall l strokes in celle, the hyphen-ci, then donne un sens. The retracing in celle-ci is not an independently cancelled word. All words of C M0309 are retained and its doubt is resolved from these strokes.',
       confidence='medium',kind='misread word',marked_in_h=True,error_category='2')
change('P12c','P12','NB: final suffisent : entraînent',
       'suffisent :\n'+r'\unsure{entraînent}',r'\ill{} \ill{} \ill{} :',
       'suffisent :\nentraînent',
       'Suffisent has two tall f stems and a final t; two separate dots form the colon. Entraînent has the initial en, crossed t, following r, raised accent and ending n-t. This resolves M0310. The upright parenthesized token below/right is separately assigned to the diagram, not repeated as an object of entraînent.',
       confidence='medium',kind=r'readable ink left as \ill{}',marked_in_h=True,error_category='5')
change('P27a','P27','Delete duplicated marginal (b). after entraînent',r'(b).','(nothing)','(nothing)',
       'In the unrotated attachment crop the only parenthesized token is upright in the main formula-number column near x246–289,y1085–1120. The NB baseline runs diagonally and ends with entraînent. C duplicates this token as marginal (b) and main (2), and adds a stop not supported by separate ink. The separate axiom b) above belongs only to the main axiom line.',
       confidence='medium',kind='text not on the page',against_h=False,error_category='9')
change('P27b','P27','One formula-number token at the left of the square',r'(2)\qquad','(nothing)',r'\unsure{(2)|(b)}\qquad',
       'The single pair of parentheses surrounds a compressed curved middle sign. Its upright orientation and alignment with the other left formula numbers favor (2), but the shape also admits (b); both are retained once at the diagram\'s physical numbering position. H omits a number there. Added uncertainty alone is not counted against C.',
       confidence='medium',kind='omission',against_c=False,error_category='3')
change('P13','P13','Cancelled application before diagramme',r'Le \deleted{application}',r'Le \struck{applicat\ldots}',r'Le \deleted{application}',
       'The strike crosses the full word application. After the tall t the i dot, rounded o and final n remain visible; there are no independent ellipsis dots. Diagramme is live. The source\'s Le is retained without grammatical correction.',
       kind='misread word',against_c=False,error_category='2')
change('P14a','P14','Entire square: objects, shafts, arrowheads and labels',diagram_c,diagram_h,diagram_d,
       'Counted twice: four objects, four square shafts, six arrowheads and one right lower hook. The top shaft has one righthead near its first third and a second at T; the bottom shaft has one righthead; the left shaft has both upper and lower heads; the right shaft has an upper head and a bottom hook, labelled inc without a stop. The extra top head is drawn as two short angular strokes on the existing shaft, with no added object or shaft. I is locally bold serif; the overworked top-right T has one roof. The top x remains overtraced and doubtful. H\'s note acknowledges the two-ended left connector, but its drawn square normalizes it to an upward hook and omits the extra top head.',
       confidence='medium',kind='drawing or diagram',consequential=True,error_category='4')
change('P14b','P14','Cancelled label on the top shaft',r'\deleted{\unsure{g}}',r'un $f$ \uncertain{biffé}',r'\deleted{\unsure{g|f}}',
       'A loop and long descending stroke favor g under the strike, but the crossing obscures the top joining strokes and f remains possible. This is an unresolved C/H letter disagreement, not a clean resolution. Cancellation itself is visible.',
       confidence='low',kind='misread symbol or index',against_c=False,marked_in_h=True)
change('P15a','P15','Star note: first complete bijection formula',
       r'$]0,1]\times\dot T\xrightarrow[\sim]{\mathrm{bij.}}\bar T\setminus Y$',
       r'$\mathbf{I}_{]0,1]}\times\dot T\to T\setminus Y$',
       r'$\mathbf{I}_{]0,1]}\times\dot T\xrightarrow{\substack{\mathrm{bij.}\\\sim}}T\setminus Y$',
       'A heavy serif I stands before a lower ]0,1] interval, so the source is I with that subscript, not the interval alone. The arrow is rightward; bij. and a separate wave are stacked above its shaft. T has one roof. This formula follows Cela signifie que in the starred note, not H\'s NB reconstruction.',
       confidence='medium',kind='insertion or placement',consequential=True,error_category='6')
change('P15b','P15','Star note: revised openness sentence and unfinished ending',
       between(C,'et qu\'une partie de',r'\unsure{dans $Y$ et ses images dans $I\times\dot T$}.}'),
       star_h,
       between(D,'et qu\'une partie de',r'\unsure{dans $Y$ et ses images dans $\mathbf{I}\times\dot T$}}'),
       'The live opening reads et qu’une partie de T est ouverte ssi: partie has a p descender and t stem, ouverte has its tall t, and ssi has two low s forms and a dotted i. The crossed lower string still only supports doubtful son intersection; its proposed replacement, raised ses images, is likewise not secure letter by letter. A short et-like group remains before dans Y and is retained as doubtful, not deleted to repair syntax. The next small groups read dans Y et ses images dans I×dot T only with continuing uncertainty. H divides this source between two marginal reconstructions and supplies quotient; that word is not supported here. There is no final predicate or independent terminal stop, so neither is supplied.',
       confidence='low',kind='misread word',marked_in_h=True,consequential=True,error_category='2')
change('P15c','P15','Short underline under the starred marginal call',r'\margin{$^{*}$',r'\marginal{* Cela',r'\margin{\uline{$^{*}$}',
       'A short separate horizontal stroke lies immediately below the marginal star. It belongs to the call sign, not the first word Cela or the neighbouring main formula number.',
       kind='other',error_category='10')
change('P16','P16','End of c): cocartésien and identifie T',
       r'est \uline{cocartésien}$^{*}$, i.e. identifie $\bar T$ au cône de l\'application',
       r'est \emph{cocartésien}*, i.e. identifie $T$ au cône de l\'application',
       r'est \uline{cocartésien}$^{*}$, i.e. identifie $T$ au cône de l\'application',
       'Cocartésien has its own underline, followed by a raised star and comma. The T is overworked, with one roof and a thick hooked stem; there is no second bar. The abbreviated i.e. is retained. H\'s emphasis and plain star express the same call; the material letter correction is against C.',against_h=False,consequential=True)
change('P17a','P17','Whole formula (3), including the compressed argument of f',
       r'(3)\qquad f:\dot T\longrightarrow Y\qquad f(x)=0.x',
       r'f:\dot T\longrightarrow Y\qquad f(x)=0.x',
       r'(3)\qquad f:\dot T\longrightarrow Y\qquad f(\unsure{a|x})=0.x',
       'The left label (3) is visible and not part of a margin note. Inside f( ), the tiny letter has a closed counter and right return, favoring a; unlike the clear crossed x after 0., it does not show four separate arms. Compressed x remains possible, so a|x is explicit. The map\'s right arrowhead and both parentheses are clear. This preferred reading differs from both witnesses.',
       confidence='medium',consequential=True)
change('P17b','P17','Whole formula (4)',r'(4)\qquad \bar T\simeq C(f)',r'(4)\qquad T\simeq\mathcal{C}(f)',r'(4)\qquad T\simeq C(f)',
       'The number is 4, not an inserted mark. The single roof belongs to T. The relation has a wave above one straight bar. C is the same open curled capital form as the other C(f) occurrences, without an additional alphabetic decoration.',consequential=True)
change('P18','P18','Inline span from Y through T to dot T',
       r'$Y\hookrightarrow\deleted{\unsure{T}}\bar T'+'\n'+r'\hookleftarrow\dot T$',
       r'$Y\hookrightarrow T\hookleftarrow\dot T$',
       r'$Y\hookrightarrow\deleted{\unsure{T}}T'+'\n'+r'\hookleftarrow\dot T$',
       'Both outer hook tails and both central arrowheads are distinct. A crossed T-like form stands before the live T; its body remains obscured enough to keep the doubt, and H omits it. The live T has one roof; the separate point over the right T is a dot, not a bar.',
       confidence='medium',kind='omission',consequential=True,error_category='3')
change('P19','P19','Cancelled phrase after applications canoniques',
       r'\deleted{\unsure{du cône $f$}}',r'\struck{\ill{}}',r'\deleted{\unsure{du cône $f$}}',
       'The initial looped d and low u are partially separable. A heavy long strike masks the middle, and two descending/looped forms survive near the end; not every letter of cône f can be isolated. Keep C\'s candidate explicitly doubtful against H\'s unreadable passage.',
       confidence='low',kind='other',against_c=False,marked_in_h=True,error_category='7')
change('P20','P20','Canonical source/target formula at the right edge',
       r'$\operatorname{but}(f)\hookrightarrow C(f)\hookleftarrow'+'\n'+r'\operatorname{source}(f)$',
       r'\uncertain{but} $Y\hookrightarrow\mathcal{C}(f)\hookleftarrow$ source,',
       r'$\operatorname{but}(f)\hookrightarrow C(f)\hookleftarrow'+'\n'+r'\operatorname{source}\unsure{(}f\unsure{)}$',
       'But has separate b/u/t bodies and is followed by an f with its long looped descender inside visible parentheses; it is not but Y. Both hooks and inward heads are clear. C(f) uses the same plain curled C. At the physical right edge source and the f stem/crossbar are visible, but surrounding parentheses cannot both be traced completely; those punctuation positions alone remain unsure. H\'s extra comma is not supported by a separate visible terminal mark.',
       confidence='medium',against_c=False,marked_in_h=True,consequential=True)
change('P21','P21','Coordination et l’op. triviale',r'et l\'op. triviale',r'et de l\'op. triviale',r'et l\'op. triviale',
       'The connected et ends in a tall crossed t, immediately followed by the l apostrophe and abbreviated op. No d ascender or separate e body occurs between them. The stop after op is visible.',
       kind='text not on the page',against_c=False,error_category='9')
change('P28','P28','Middle action paragraph: each I/T and repeated C(f)',
       between(C,'et l\'opération de $I$',r'de $I$ sur $Y$.'),
       between(H,'et l\'opération de $\mathbf{I}$',r'de $\mathbf{I}$ sur $Y$.'),
       between(D,'et l\'opération de $\mathbf{I}$',r'de $\mathbf{I}$ sur $Y$.'),
       'This previously uncropped paragraph was checked locally rather than by global font replacement. All five interval I occurrences have heavy vertical bodies and upper/lower serifs (the first roof is at the crop edge and was visible in the half). The ordinary T has one roof; the dotted T has its own separate point. C(f) repeats the plain curled C. The op. coordination was separately inspected in P21; no new words are supplied.',
       consequential=True)
change('P22a','P22','Les axiomes ... signifient aussi',r'signifient'+'\n'+'aussi',r'signifient donc','signifient'+'\n'+'aussi',
       'The word has a low a/u opening followed by two small s bodies and a dotted final i. There is no tall initial d or final c for donc.',
       kind='misread word',against_c=False,error_category='2')
change('P22b','P22','First member of the situation: literal hooked shafts',
       r'\unsure{Y\hookrightarrow\bar T\hookleftarrow\dot T}',r'Y\to T\hookleftarrow\dot T',situation_d,
       'There are three objects and two shafts. The left shaft has a small outer left hook, and the right shaft a curved outer right hook. Neither shaft has a securely separable head at the central T. The draft draws only those visible hooked shafts, without silently asserting inclusions. Intended inclusion directions remain a diagnostic alternative in doubts. Each T has one roof.',
       confidence='medium',kind='drawing or diagram',consequential=True,error_category='4')
change('P22c','P22','Second member of the situation: headless action shaft',
       r'\unsure{I\times\bar T-\bar T}',r'\mathbf{I}\times T\to T',r'\mathbf{I}\times T-T',
       'The I has a broad stem and top/bottom serifs; each T has one roof. Between the T forms is one straight horizontal stroke with no paired angular head. The literal headless shaft resolves M0315; it does not decide the semantic intent of a suppressed map arrow.',consequential=True)
change('P23a','P23','Punctuation after isomorphe',r'est isomorphe à',r'est isomorphe :',r'est isomorphe :',
       'Two distinct dark vertically stacked dots follow the final e; there is no a body with an accent. The source colon is retained, even though à would repair the syntax.',
       kind='other',against_h=False,error_category='10')
change('P23b','P23','Final f formula in the isomorphism sentence',
       r'celle d\'un $C(f)$ avec $f:\dot T\longrightarrow Y$.',
       r'celle d\'un $\mathcal{C}(f)$ avec $f:\dot T\to Y$.',
       r'celle d\'un $C(f)$ avec $f:\dot T-Y$.',
       'The short stroke between dot T and Y has a straight squared/right return, not two angular head branches. Its literal shaft is retained without a map head. The colon after f, separate point above T, plain curled C(f), and terminal period after Y are visible.',consequential=True)
change('P24a','P24','Opening Notons',r'Notons',r'\emph{Notons}',r'Notons',
       'No independent stroke lies under the word. The nearby horizontal below/left is the upper serif of the I on the next line and continues into its upright; it is not an underline of Notons.',
       kind='other',against_c=False,error_category='10')
change('P24b','P24','connu quand on connaît',r'\unsure{connu quand on connaît}',r'connu quand on connaît',r'connu quand on connaît',
       'Connu has the low c/o followed by two n humps; quand has a descending q and the tall terminal d; on is a separate short group; connaît repeats the con- opening and finishes with an accented i/t ending. The words are sufficiently separable to resolve C M0316.',
       kind='misread word',against_h=False,error_category='2')
change('P24c','P24','de I sur T before the cancelled phrase',r'de $I$ sur $\bar T$,',r'de $\mathbf{I}$ sur $T$,',r'de $\mathbf{I}$ sur $T$,',
       'The I under Notons has a dark broad upright and separate upper/lower serifs. The following T has one roof only. The comma is a separate downward curved stroke after T.',against_h=False,consequential=True)
change('P24d','P24','Cancelled comme on before en posant',r'\deleted{\unsure{comme on}}',r'\struck{\ill{}}',r'\deleted{\unsure{comme on}}',
       'An initial open c and rounded o survive before low m-like joining humps; the second short group remains partly hidden by the strike and descending loops from neighbouring text. Comme on is retained only as an uncertain candidate, not a resolved clean word sequence.',
       confidence='low',kind='other',against_c=False,marked_in_h=True,error_category='7')
change('P25a','P25','First part of formula (5)',
       r'(5)\qquad \mathring T=\bar T\setminus\dot T',
       r'(5)\qquad \overset{\circ}{T}=T\setminus\dot T',
       r'(5)\qquad \mathring T=T\setminus\dot T',
       'The label is 5. An open ring lies above the first T and a filled point above the last. The middle T has one roof, without an independent bar. The two macros for the ring are equivalent and are not themselves counted as a change.',against_h=False,consequential=True)
change('P25b','P25','Parenthetic l’intérieur du tube',r"(l'\uline{intérieur} du tube)",r'(\emph{intérieur} du tube)',r"(l'\uline{intérieur} du tube)",
       'After the opening parenthesis an independent l and apostrophe precede intérieur. The long lower stroke spans the word intérieur, rather than the whole parenthesis. Both parentheses are visible.',
       kind='omission',against_c=False,error_category='3')
change('P25c','P25','Final notons que and union formula',
       r'\text{et notons que }\mathring T=\bigcup_{\lambda\in[0,1[}\lambda\bar T',
       r'et notant que $\overset{\circ}{T}=\bigcup_{\lambda\in[0,1[}\lambda T$',
       r'\text{et notons que }\mathring T=\bigcup_{\lambda\in[0,1[}\lambda T',
       'Notons has an o-shaped middle body and a low final s after n, not the a-n-t of notant; que is on the short lower continuation. The large union has lambda membership in [0,1[, with the final bracket open. The last T has one roof. There is no secure terminal stop after that T.',
       kind='misread word',consequential=True,error_category='2')
change('P26','P26','Thin lower-left foliation',r'\margin{11}','(nothing)',r'\margin{11}',
       'Two thin long uprights each have a short oblique approach stroke, giving 11. Their weight and small size differ from the author\'s upper 1); hand attribution remains uncertain, but both digits are clear.',
       kind='omission',against_c=False,error_category='3')

def decision(id, p, decision, reading, evidence, confidence):
    R['decisions'].append(dict(id=id,cote='150',scan='12',decision=decision,
        reading=reading,evidence=evidence,crop=f'crops/{PAGE}_{p}.png',
        box=BOX[p],confidence=confidence))

decision('M0307','P05','first','tube','Separate t/u/b/e bodies, including both tall ascenders and final e; word-only underline does not obscure the letters.','high')
decision('M0308','P12','undecided',r'sous \unsure{sa|la} forme faible','Sous, forme and faible are legible; the article is compressed and lacks a secure l ascender. The original broad doubt is narrowed, not fully resolved.','medium')
decision('M0309','P12','first','à qui celle-ci donne un sens','The q descender, twin l ascenders, hyphen-ci and final un sens can be read separately; no independent cancelled group occurs inside.','medium')
decision('M0310','P12','first','entraînent','Initial en, crossed t, r, raised accent and final n-t support the whole word; the nearby upright number is not its object.','medium')
decision('M0311','P14','undecided',r'\unsure{x}','The top label argument is heavily retraced, with crossing arms but no clean isolated glyph. Keep x doubtful; no separate deletion is asserted.','low')
decision('M0312','P15','undecided',r'\unsure{ses images}','Raised replacement sits over the struck group, but its low joining strokes are crowded and every letter cannot be isolated.','low')
decision('M0313','P15','undecided',r'\unsure{dans $Y$ et ses images dans $\mathbf{I}\times\dot T$}','The Y and I×dot T are locatable, and the surrounding low words fit the proposed sequence, but the slanted revision makes exact joins and scope insecure. A separate doubtful et before this group is retained.','low')
decision('M0314','P22','other',situation_d,'The source has three objects and two outwardly hooked shafts, but no secure independent heads at the central T. Literal geometry replaces asserted inclusions; semantic direction remains unresolved.','medium')
decision('M0315','P22','first',r'\mathbf{I}\times T-T','The connector is one horizontal stroke with no angular head; I is locally bold and both Ts have a single roof. The first candidate\'s headless form is retained with these independently checked glyph corrections.','high')
decision('M0316','P24','first','connu quand on connaît','Separate c/o/n/n/u, q descender and terminal d, short on, then repeated con- and accented ending are visible.','high')

def inv(kind, position, content, hand='his hand'):
    R['inventory'].append(dict(scan=PAGE,sheet_kind='text',hand=hand,
        element=f'E{len(R["inventory"])+1:02d}',kind=kind,position=position,
        first_words_or_objects=content,transcribed='yes'))

inv('text','Upper left, P00',r'\mspage{1)}; \textcircled{I}')
inv('text','Across the top, P01','Espaces stratifiés (étude par voisinages ... coniques)')
inv('deletion','Title, P01',r'\deleted{tubulaires}')
inv('insertion','Under title cancellation, P01',r'\inserted{coniques}')
inv('text','First paragraph opening, native upper half; P02–P09',r'\textcircled{1} Soit Y un espace topologique ...')
inv('deletion','Opening definition, P02',r'\deleted{tubulaire}')
inv('insertion','Opening definition at right edge, P02',r'\inserted{\uline{\unsure{conique}}}')
inv('insertion','Raised parenthetic definition, P03',r'\inserted{(``\uline{absolu}\'\')}')
inv('deletion','After live de, P03',r'\deleted{$Y$}')
inv('insertion','After crossed Y, P03',r'\inserted{(ou ``cône sur $Y$\'\')}')
inv('deletion','Low-right of first T, P04',r'\deleted{\unsure{_Y}}')
inv('deletion','After dot T, before le bord, P06',r'\deleted{\illegible{1}}')
inv('text','After interval [0,1], P08',r'\unsure{}; present overworked mark, cancellation state unresolved')
inv('display','Action formula, P09',r'(1) (\lambda,t)\mapsto\lambda t; \mathbf I\times T\to T')
inv('display','Conditions a), b), P10, with right brace visible in P11',r'a) \lambda y=y\quad\forall y\in Y; b)0.\deleted{\unsure{T|\bar T}}T\subset Y')
inv('deletion','Between 0. and live T in b), P10',r'\deleted{\unsure{T|\bar T}}')
inv('margin note','Right of a), b), P11',hom_d)
inv('margin note','Slanted left of c), P12; attachment P27',nb_d)
inv('deletion','After c) Le, P13',r'\deleted{application}')
inv('diagram','Square, P14, number in P27',r'\unsure{(2)|(b)}; four objects/four shafts/six heads/one hook; '+diagram_d)
inv('deletion','Label on top square shaft, P14',r'\deleted{\unsure{g|f}}')
inv('text','Below the square, P16',r'est \uline{cocartésien}$^{*}$, i.e. identifie T au cône de l’application')
inv('display','Between square and (4), P17',r'(3) f:\dot T\to Y,\quad f(\unsure{a|x})=0.x')
inv('margin note','Slanted lower left, starred note P15',star_d)
inv('deletion','Inside starred note, P15',r'\deleted{\unsure{son intersection}}')
inv('insertion','Above that cancellation, P15',r'\inserted{\unsure{ses images}}')
inv('display','Middle of page, P17',r'(4) T\simeq C(f)')
inv('text','Identification and canonical maps, P18–P20','Dans cette identification ... applications canoniques ... but(f) ... source(f)')
inv('deletion','Before live T in identification, P18',r'\deleted{\unsure{T}}')
inv('deletion','After applications canoniques, P19',r'\deleted{\unsure{du cône $f$}}')
inv('text','Middle action paragraph, P28 and P21','et l’opération de I sur T ... et l’op. triviale de I sur Y')
inv('text','Lower situation paragraph, P22–P23',situation_full_d+' est isomorphe : celle d’un C(f) avec f:dot T—Y.')
inv('text','Last paragraph opening, P24','Notons que dot T est connu quand on connaît l’opération de I sur T, ... en posant')
inv('deletion','Before en posant, P24',r'\deleted{\unsure{comme on}}')
inv('display','Last display and its parenthesis, P25',between(D,r'(5)\qquad',r'\bigcup_{\lambda\in[0,1[}\lambda T'))
inv('margin note','Small lower-left foliation, P26',r'\margin{11}','uncertain hand')

def audit(id, kind, xyxy, reading):
    R['audit_boxes'].append(dict(box=id,kind=kind,xyxy=xyxy,reading=reading))

audit('B00','handwritten number; margin note',BOX['P00'],r'1)\quad\textcircled{I}')
audit('B01','insertion; struck passage',BOX['P01'],between(D,'Espaces stratifiés',r'\inserted{coniques})'))
audit('B02','insertion; struck passage; less than high confidence departure',BOX['P02'],r'\uline{voisinage \deleted{tubulaire}} \inserted{\uline{\unsure{conique}}}')
audit('B03','insertion; struck passage; C/H different words',BOX['P03'],r'\inserted{(``\uline{absolu}\'\')} de \deleted{$Y$} \inserted{(ou ``cône sur $Y$\'\')} est un espace topologique')
audit('B04','doubtful formula; struck passage; less than high confidence departure',BOX['P04'],r'$T\deleted{\unsure{_Y}}$ contenant $Y$')
audit('B05','C/H different words',BOX['P05'],r'(le ``\uline{tube}\'\'),')
audit('B06','struck passage; less than high confidence departure',BOX['P06'],r'Y,\quad \dot T\quad\deleted{\illegible{1}}\quad(le ``bord\'\'')
audit('B07','C/H different words',BOX['P07'],r'du tube\'\')')
audit('B08','doubtful formula; handwritten number; less than high confidence departure',BOX['P08'],r'$\mathbf I=[0,1]\,\unsure{}$ (pour la multiplication) sur $T$, notée')
audit('B09','handwritten number',BOX['P09'],between(D,r'(1)\qquad',r'\qquad \mathbf{I}\times T\longrightarrow T'))
audit('B10','struck passage; doubtful formula; handwritten number; less than high confidence departure',BOX['P10'],between(D,r'a)&',r'T\subset Y'))
audit('B11','margin note; handwritten number; C/H different words; less than high confidence departure',BOX['P11'],hom_d)
audit('B12','margin note; handwritten number; C/H different words; less than high confidence departure',BOX['P12'],nb_d)
audit('B13','struck passage; C/H different words',BOX['P13'],r'c) Le \deleted{application} diagramme d’applications')
audit('B14','doubtful formula; struck passage; handwritten number; less than high confidence departure',BOX['P14'],diagram_d)
audit('B15','margin note; insertion; struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',BOX['P15'],star_d)
audit('B16','C/H different words',BOX['P16'],r'est \uline{cocartésien}$^{*}$, i.e. identifie $T$ au cône de l’application')
audit('B17','doubtful formula; handwritten number; less than high confidence departure',BOX['P17'],r'(3)\qquad f:\dot T\longrightarrow Y\qquad f(\unsure{a|x})=0.x\qquad (4)\qquad T\simeq C(f)')
audit('B18','struck passage; doubtful formula; less than high confidence departure',BOX['P18'],r'$Y\hookrightarrow\deleted{\unsure{T}}T\hookleftarrow\dot T$ correspondent')
audit('B19','struck passage; less than high confidence departure',BOX['P19'],r'\deleted{\unsure{du cône $f$}}')
audit('B20','doubtful formula; C/H different words; less than high confidence departure',BOX['P20'],r'$\operatorname{but}(f)\hookrightarrow C(f)\hookleftarrow\operatorname{source}\unsure{(}f\unsure{)}$')
audit('B21','C/H different words',BOX['P21'],r'et l’op. triviale')
audit('B22','doubtful formula; C/H different words; less than high confidence departure',BOX['P22'],situation_full_d)
audit('B23','doubtful formula; C/H different words',BOX['P23'],r'est isomorphe : celle d’un $C(f)$ avec $f:\dot T-Y$.')
audit('B24','struck passage; C/H different words; less than high confidence departure',BOX['P24'],r'Notons que $\dot T$ est connu quand on connaît l’opération de $\mathbf I$ sur $T$, \deleted{\unsure{comme on}} en posant')
audit('B25','handwritten number; C/H different words',BOX['P25'],between(D,r'(5)\qquad',r'\bigcup_{\lambda\in[0,1[}\lambda T'))
audit('B26','margin note; handwritten number',BOX['P26'],'11')
audit('B27','handwritten number; less than high confidence departure',[238,1072,300,1128],r'\unsure{(2)|(b)}')
audit('B28','C/H different words',BOX['P28'],between(D,'et l\'opération de $\mathbf{I}$',r'de $\mathbf{I}$ sur $Y$.'))
audit('B29','handwritten number',[197,183,292,274],r'\textcircled{1}')

def doubt(place,reading,alternatives,reason,confidence='low'):
    R['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))

doubt('P02 replacement at physical right edge',r'\unsure{conique}','conique, final e not secure','The final letter meets the clipped paper/image edge. Retaining the candidate does not claim a fully visible e.','medium')
doubt('P04 crossed low-right token',r'\deleted{\unsure{_Y}}','Y-like subscript; unreadable cancelled glyph','Crossing and low placement obscure the independent branches; no resolution of the old candidate.')
doubt('P06 new cancelled textual word',r'\deleted{\illegible{1}}','No recoverable full word; muni is only an unsupported possible outline','Several low humps and a last upright survive, but the strike covers the complete letter sequence.')
doubt('P08 mark after interval',r'\unsure{}','Unreadable present mathematical mark, possibly cancelled; e-like or arrow-like outline not adopted','The small filled cluster and low return lack enough independent strokes to fix identity or chronology. An adjacent draft comment records uncertain state.')
doubt('P10 crossed T in b)',r'\deleted{\unsure{T|\bar T}}','T | barred T','The crossing itself could account for the apparent upper horizontal; the underlying roof cannot be separated from it.','medium')
doubt('P11 rétraction ending','rétraction','Compressed baseline on; raised/abbreviated ending was considered but not favored','The dotted i is followed by a short low continuation turning down, rather than a separately raised suffix or independent stop.','medium')
doubt('P12 article after sous',r'\unsure{sa|la}','sa | la','No secure tall l separates the possibilities; the low compact body favors sa.','medium')
doubt('P27 formula-number shape and attachment',r'\unsure{(2)|(b)}','(2) | (b), once at the diagram','Upright orientation and formula-number column favor 2; the central curved stroke remains compressed. The glyph is not duplicated after the slanted NB.','medium')
doubt('P14 top label argument',r'\unsure{x}','x; no stable alternative letter','Overtracing and a crossing stroke prevent isolating one clean x; no separate cancelled copy is asserted.')
doubt('P14 cancelled top label',r'\deleted{\unsure{g|f}}','g | f','Loop plus descender favor g, but the strike masks joins. The C/H disagreement remains unresolved.')
doubt('P15 cancelled lower phrase',r'\deleted{\unsure{son intersection}}','son intersection; no fully legible alternative','A heavy stroke hides the interior letters, so the conventional expected wording is not used as proof.')
doubt('P15 raised replacement',r'\inserted{\unsure{ses images}}','ses images','The raised low bodies overlap the cramped revision and cannot all be separated.')
doubt('P15 short group before dans Y',r'\unsure{et}','et; uncertain attachment within the revision','A short e-like loop and t-like upright survive below the strike; deleting them for grammar would lose visible ink.')
doubt('P15 final slanted clause',r'\unsure{dans $Y$ et ses images dans $\mathbf{I}\times\dot T$}','Proposed clause; some word joins and revision attachment remain insecure','The clear Y and product anchor the reading, but small slanted text is crowded. No final predicate or terminal stop is visible.')
doubt('P17 argument in f(a|x)',r'f(\unsure{a|x})=0.x','a | x','Closed counter and right return favor a; the RHS x is distinctly crossed. The expected f(x) is not silently imposed.','medium')
doubt('P18 cancelled T before live T',r'\deleted{\unsure{T}}','T-like token','Crossing hides a complete independent roof/stem, so the original doubt remains.')
doubt('P19 cancelled phrase',r'\deleted{\unsure{du cône $f$}}','du cône f; no fully recoverable alternative','The opening d/u and final loops survive, but the strike prevents reading every letter of the proposed phrase.')
doubt('P20 source at physical right edge',r'\operatorname{source}\unsure{(}f\unsure{)}','Parentheses around the visible f are insecure','The source letters and f stem/crossbar are visible; the punctuation falls at the clipped edge and is not completed as certain.','medium')
doubt('P22 first pair of situation shafts',situation_d,r'Intended Y\hookrightarrow T\hookleftarrow\dot T','The outward hooks are visible, but neither central arrowhead can be isolated. The draft records unheaded geometry; intended inclusions belong only to the diagnosis.','medium')
doubt('P22 second situation shaft',r'\mathbf I\times T-T',r'Intended action map \mathbf I\times T\to T','No arrowhead is visible in the written short shaft. Its map interpretation does not authorize drawing a missing head.','medium')
doubt('P23 f shaft',r'f:\dot T-Y',r'Intended f:\dot T\to Y','The source has a short unheaded horizontal; f and its source/target supply mathematical context, not an unseen angular head.','medium')
doubt('P24 cancelled comme on',r'\deleted{\unsure{comme on}}','comme on','Crossing masks the low middle joins and the second group, so not all letters can be independently recovered.')

R['notes'] = [
 {'id':'N01','text':'Source report: the title replaces “tubulaires” by “coniques”. The page defines a “voisinage conique” (also “cône sur Y”) using a space T containing Y, a closed part dot T, and an action of the multiplicative interval monoid I=[0,1]. The source axioms a), b), c), the starred pushout explanation, the canonical-map identifications and the final interior formula are transcribed. This description by itself is not a proof check. No outside source was used.'},
 {'id':'N02','text':'Main-reader targeted deduction, communicated by root and retained as a check: a) and b), together with the continuous unital I-action, imply a strong deformation retraction of T onto Y. Let r(t)=0t and H(s,t)=(1-s)t. Then H(0,t)=t, H(1,t)=r(t) is in Y by b), and H(s,y)=y by a). In particular r(y)=y. This explains the right marginal “sur une rétraction” without adding words to it.'},
 {'id':'N03','text':'Main-reader targeted deduction: the weaker condition 0.dot T subset Y, together with a) and the cocartesian square c), implies b). In the pushout every point has a representative y in Y or lambda b with b in dot T. For y, 0y=y by a); for lambda b, the action law gives 0(lambda b)=(0 lambda)b=0b in Y. This verifies the intended marginal implication. The written NB nonetheless ends at “entraînent”: the parenthesized token is kept once at the diagram position as (2)|(b), not supplied as the verb’s missing object.'},
 {'id':'N04','text':'Main-reader targeted deduction: the pushout identifies the whole copy {0}×dot T with its image in Y and makes no other identifications between Y and (0,1]×dot T. Thus the latter points and Y form the disjoint representative description. The source star-note bijection from I_{]0,1]}×dot T to T minus Y is consistent with that quotient description. It does not establish that this bijection is a homeomorphism, and the transcription does not add such a statement.'},
 {'id':'N05','text':'Main-reader targeted deduction for the final equation: using the representative description, the union of lambda T for 0≤lambda<1 is Y union ((0,1)×dot T), hence T minus dot T. One inclusion follows because multiplying a representative with positive parameter by lambda<1 yields parameter below 1. Conversely, a parameter mu<1 is mu times a parameter-1 representative, and Y is fixed. This verifies the equation defining the interior and explains how the action determines the boundary as its complement.'},
 {'id':'N06','text':'Main-reader targeted quotient-topology check: a subset of the pushout is open exactly when its inverse images in Y and I×dot T are open. The visible starred sentence says “et qu’une partie de T est ouverte ssi” followed by a cramped cancelled/replaced phrase and the proposed clause “dans Y et ses images dans I×dot T”, but no final predicate is visible. “Open” is the needed mathematical predicate of the inverse images; it is recorded only here as an explanatory correction, not added to the diplomatic text. The extra et-like group before dans Y stays doubtful and live.'},
 {'id':'N07','text':'Possible author slip / unresolved letter in (3): the argument of f looks like a closed a rather than the crossed x used on the right of 0.x. Both witnesses print f(x)=0.x. The diplomatic text retains f(a|x)=0.x with a preferred. Mathematical consistency would favor using x on both sides, but the check does not settle the letter against the ink.'},
 {'id':'N08','text':'Notation and geometry are kept literal. The T forms have single roofs; bold serif I was checked locally, including all five occurrences in the middle action paragraph P28. The main square has four objects, four shafts, six heads and one hook, counted twice. Later situation connectors have outer hooks but no secure central heads; their intended inclusion/map interpretations do not supply those heads. The colon after “isomorphe”, the unmatched extra closing quotation after tube, the source Le before the cancelled application, and the incomplete marginal endings are preserved.'},
 {'id':'N09','text':'Reading record: the assigned original was viewed once, both supplied native halves once, and each saved first-pass crop P00–P26 once. P27 was authorized specifically for the still-open original-orientation attachment of the number/NB ending. Only the still-open rétraction ending was then consulted in saved P11; no new crop of a decided place was made. P28 is the first crop of the previously uncropped action paragraph, to check local I weight. There were no OCR, recognition libraries, outside research, compilation, other-page images, or other-page reports. Root independently reviewed all 29 crops.'},
 {'id':'N10','text':'The faint narrow lower-left 11 is retained separately from the large author folio 1). Its hand is not attributed with certainty from line weight alone. Punctuation at the physically clipped right edge is explicitly uncertain. Pale substrate/stain marks were not transcribed as text.'}
]
R['check_events'] = [
 {'statement_id':PAGE+'.N01','type':'carried as background without fault found','outcome':'Source contents were read visually against C/H; reporting them is not an independent theorem verification.'},
 {'statement_id':PAGE+'.N02','type':'targeted proof check','outcome':'Root explicitly checked H(s,t)=(1-s)t, both endpoints, and fixed Y under a), b); reader B integrated that supplied main-reader deduction.'},
 {'statement_id':PAGE+'.N03','type':'targeted proof check','outcome':'Root explicitly checked the y and lambda b representative cases to derive full b) from weak b), a), c). This is separate from the unresolved physical attachment of the nearby parenthesized token.'},
 {'statement_id':PAGE+'.N04','type':'targeted proof check','outcome':'Root checked the pushout representative description Y disjoint union (0,1]×dot T and its set-level bijection.'},
 {'statement_id':PAGE+'.N05','type':'targeted proof check','outcome':'Root checked the union for lambda<1 in the pushout representative description and its equality to T minus dot T.'},
 {'statement_id':PAGE+'.N06','type':'targeted proof check','outcome':'Root checked the quotient-openness criterion, found the missing predicate in the visible incomplete sentence, and required the correction to remain in notes only.'},
 {'statement_id':PAGE+'.N07','type':'carried as background without fault found','outcome':'No mathematical argument resolves the compressed a/x letter. The possible source slip remains explicitly doubtful.'}
]
R['notation'] = [
 {'form':r'T','meaning':'Ambient conical-neighbourhood space','evidence':'Opening definition and repeated single-roof T forms; P04, P08–P09, P14, P16–P18, P22–P25, P28.'},
 {'form':r'\dot T','meaning':'Specified closed part called the bord (with literal uneven quotation marks)','evidence':'Definition before le bord in P06 and repetitions throughout the page.'},
 {'form':r'\mathbf I=[0,1]','meaning':'Multiplicative interval monoid','evidence':'Explicit definition in P08; broad serif I locally verified in every subsequent occurrence, including P28.'},
 {'form':r'\mathbf I_{]0,1]}','meaning':'Positive-parameter interval notation in the starred bijection','evidence':'P15 has a heavy I followed by the lower written interval ]0,1].'},
 {'form':r'\lambda_T,\operatorname{id}_T','meaning':'Action endomorphism at lambda and identity of T','evidence':'Right margin P11 has lowered T in both labels.'},
 {'form':r'C(f)','meaning':'The source’s cone construction attached to f; no replacement terminology imposed','evidence':'Formula (4), canonical-map formula and repeated prose C(f).'},
 {'form':r'\mathring T=T\setminus\dot T','meaning':'Interior of the tube, in the author’s terminology','evidence':'Explicit formula (5) and underlined intérieur in P25.'},
 {'form':r'\unsure{}','meaning':'Present unreadable mathematical mark with unresolved cancellation state, not a blank','evidence':'P08 small overworked mark immediately after [0,1]; adjacent draft comment identifies it.'}
]
R['abbreviations'] = [
 {'form':'pts','expansion':'points'}, {'form':'ssi','expansion':'si et seulement si'},
 {'form':'i.e.','expansion':'id est'}, {'form':'bij.','expansion':'bijective / bijection (arrow label)'},
 {'form':'inc','expansion':'inclusion; source has no stop'}, {'form':'op.','expansion':'opération'},
 {'form':'NB','expansion':'nota bene'}, {'form':'id','expansion':'identité'}
]
R['hand'] = [
 {'habit':'A detached horizontal roof and hooked upright form T; the roof is not an additional overbar.','places':'150_scan012 P04, P08–P11, P14, P16–P18, P22–P25, P28.','consistency':'All checked live T occurrences have one roof. Crossed prior T forms remain doubtful because their strike can mimic a second bar.','witness_errors':'C repeatedly prints barred T; H generally prints plain T.'},
 {'habit':'The interval I has broad filled or multiply retraced stem plus top/bottom serifs.','places':'150_scan012 P08–P09, P14–P15, P22, P24, P28.','consistency':'Verified locally on this page; no rule is imposed on another page or another I from context alone.','witness_errors':'C mostly gives plain I; H bold I matches this page’s local weight.'},
 {'habit':'Small compressed a can resemble x, but a closed counter differs from the clear crossed x nearby.','places':'150_scan012 P17, f argument versus RHS 0.x.','consistency':'One unresolved occurrence; not generalized as a systematic substitution.','witness_errors':'Both witnesses choose x; the preferred a-like reading is retained with x as alternative.'},
 {'habit':'Continuous insertion leaders may run above or around live words without cancelling them.','places':'150_scan012 P03 and the slanted marginal-note attachments P12/P27.','consistency':'Leader paths were tracked separately from lexical content; neighbouring main labels are not duplicated into a margin.','witness_errors':'H invents a struck est un espace; C duplicates a parenthesized token as NB (b) and diagram (2).'},
 {'habit':'Quotation marks are paired short ticks; repeats can remain unmatched.','places':'150_scan012 P03, P05–P07.','consistency':'Paired ticks remain distinct from parentheses and underlines.','witness_errors':'H regularizes them to guillemets and merges the two closing pairs around bord/du tube.'},
 {'habit':'Arrow shafts and heads are not always complete; an extra head can be present on a continuous shaft.','places':'150_scan012 P14, P22–P23.','consistency':'Heads and hooks counted separately twice; explicit inline hooks P18/P20 remain distinct from headless later shafts.','witness_errors':'Both witnesses miss the extra top head; C normalizes left up/down geometry and later inclusion heads; H also adds map heads to short shafts.'}
]

coverage = {
1:'P00a author folio 1); P01 title. H editorial framing is not source text.',
2:'P00a retains 1); editorial discussion of other leaves is excluded.',
3:'P00b retains the physically circled Roman I, once; H explanatory words excluded.',
4:'Circled source paragraph 1 retained once (audit B29); H editorial parenthesis normalization and duplicate labels are excluded.',
5:'P03a: paired ticks, word-only absolu underline, actual insertion and resolved H lexical doubt.',
6:'P03b: paired opening ticks and raised insertion, not guillemets.',
7:'P03b: paired closing ticks; source parenthesis retained.',
8:'P03c: one live est un espace; H extra struck duplicate rejected as insertion-leader confusion.',
9:'P04: low-right cancelled Y candidate remains unresolved, explicitly collated against H unreadable token.',
10:'P06a adds the separate visible comma after Y.',
11:'P05: straight opening pair, not guillemet.',
12:'P05: straight closing pair; tube doubt resolved from letters.',
13:'P06c: independent closing pair immediately after bord.',
14:'P07: additional closing pair after du tube retained literally.',
15:'Array/environment syntax alone is not a change; source grouping brace is separately restored in P10b.',
16:'P10a: crossed T candidate occurs between 0. and live T; exact bar remains doubtful.',
17:'Array closure is macro syntax; cancelled-token placement is covered by P10a.',
18:'P11: sur une rétraction; H extra à l’application ... de T is not present.',
19:'P11 right note and P12 left NB are separately transcribed in source order; H attachment comment is editorial.',
20:'P12a: sous sa|la forme faible and the literal weak condition retained.',
21:'P12b/P12c: plus la condition c), full parenthesis, suffisent : entraînent; P27a removes duplicated (b).',
22:'P13: full cancelled application, no ellipsis.',
23:'P27b: sole number is (2)|(b) at diagram position, not duplicated into NB.',
24:'P14b: cancelled g|f remains unresolved; preferred g differs from H.',
25:'P14a: literal up/down left arrow and additional top head; P14b cancelled label. H note is not copied as source prose.',
26:'P16 raised call star retained; baseline versus superscript encoding is otherwise representational. P15c restores the separate underline under the marginal star.',
27:'P17a retains visible (3) with the whole formula; H omits the formula number there.',
28:'P15a–c: complete starred note in its actual place; I_{]0,1]}, labels above arrow, revised prose with uncertainties and no supplied ending.',
29:'P18: crossed T before live T retained; H omission explicitly collated.',
30:'P19: cancelled du cône f candidate stays uncertain against H illegible passage.',
31:'P20: but(f), not but Y; both hooks and C(f) checked.',
32:'P20: visible source/f retained, edge parentheses doubtful; no secure added comma.',
33:'P21: et l’op. triviale, no added de.',
34:'P22a: aussi, not donc.',
35:'P22b: two outwardly hooked but headless shafts; intended inclusion directions remain notes/doubts.',
36:'P22c: literal headless straight shaft, not an arrowhead.',
37:'P23a: two separate dots give colon, not à.',
38:'H moves and conflates the two slanted notes. P12/P27 retain NB ending at entraînent and one diagram number; P15 restores the separate starred note, with incomplete ending. H editorial notes and duplicate (3) labels are not source words.',
39:'P24d: cancelled comme on remains uncertain and is explicitly collated against H illegible token.',
40:'Ring notation mathring versus overset circ is macro-only; P25a changes only the unsupported bar on T.',
41:'Display boundaries are macro layout only; the parenthesis and continuation remain source content.',
42:'P25b retains the written l apostrophe before intérieur.',
43:'P25c: notons, not notant.',
44:'Second ring notation is macro-only; P25c preserves the full indexed union and corrects the unsupported T bar.',
45:'P26 retains thin lower-left 11; attribution remains uncertain.'
}
R['diff_coverage'] = [dict(row=i,disposition=coverage[i]) for i in range(1,46)]

def rev(text,scope,evidence):
    R['deletion_insertion_review'].append(dict(text=text,scope_attachment=scope,evidence=evidence))
rev(r'\deleted{tubulaires}\inserted{coniques}','Title replacement, below the crossed plural adjective, before the closing parenthesis.','P01: separate strike and lower replacement baseline.')
rev(r'\deleted{tubulaire}\inserted{\uline{\unsure{conique}}}','Singular replacement in the opening definition; underline continues under old word and is separate under the replacement.','P02: old crossing and lower underline separated; final e meets the physical edge.')
rev(r'\inserted{(``\uline{absolu}\'\')}','Raised parenthesis attaches to voisinage conique.','P03: complete parentheses, paired ticks and a word-only underline.')
rev(r'de \deleted{$Y$}\inserted{(ou ``cône sur $Y$\'\')}','de is live; Y alone is cancelled; the raised parenthesis follows it.','P03: leader continues over one live est un espace and does not cross a second copy.')
rev(r'\deleted{\unsure{_Y}}','Small low-right old token attached to the first T.','P04: crossing masks complete branches; candidate and subscript placement remain uncertain.')
rev(r'\deleted{\illegible{1}}','Cancelled textual word after dot T, before (le bord).','P06: distinct line across low letter bodies; full word cannot be recovered.')
rev(r'\unsure{} after [0,1]','Present small mathematical glyph; live/cancelled chronology unresolved.','P08: overworked counter and low return, no separable independent cancellation line.')
rev(r'\deleted{\unsure{T|\bar T}}','Old token immediately after 0., before the live T in b).','P10: crossed body precedes live single-roof T; descender from preceding y is not cancellation.')
rev(r'\deleted{application}','Only application, between live Le and live diagramme.','P13: strike crosses through final ion; there are no separate ellipsis dots.')
rev(r'\deleted{\unsure{g|f}}','Top square label beneath the mapping annotation.','P14: loop/descender under independent strike; doubtful letter remains, not a new arrow.')
rev(r'\deleted{\unsure{son intersection}}\inserted{\unsure{ses images}}','Starred-note local revision after ssi; short et-like group remains live before dans Y.','P15: raised replacement, crossed lower body and cramped continuation have distinct vertical positions; their exact letters remain doubtful.')
rev(r'\deleted{\unsure{T}}','Old inline T after the left hook-arrow and before live T.','P18: crossed glyph is separate from the next single-roof live T.')
rev(r'\deleted{\unsure{du cône $f$}}','Cancelled phrase after applications canoniques and before but(f).','P19: heavy line spans phrase, partial d/u and final loops remain; no certain expansion.')
rev(r'\deleted{\unsure{comme on}}','Cancelled words after the comma and before live en posant.','P24: strike lies through low word bodies; en posant remains live.')
rev('Single parenthesized (2)|(b)','Diagram number once, not the last object of NB; main axiom b) likewise remains separate.','P27 original orientation shows two distinct main labels at their own positions; no extra duplicate in the slanted NB.')

marks = list(csv.DictReader((ROOT/'packets'/PAGE/'marks.tsv').open(),delimiter='\t'))
assert [x['id'] for x in marks] == [x['id'] for x in R['decisions']]
assert len(R['diff_coverage']) == 45
assert len(BOX) == 29

# Raw literals use escaped Python quote delimiters in a few French/quotation
# snippets; source apostrophes are literal characters, never TeX accent escapes.
def source_quotes(value):
    if isinstance(value, str):
        return value.replace("\\'", "'")
    if isinstance(value, list):
        return [source_quotes(v) for v in value]
    if isinstance(value, dict):
        return {k: source_quotes(v) for k,v in value.items()}
    return value

R = source_quotes(R)

# Read-only structural checks: exact source excerpts, valid crop paths, and no lost original mark.
bad = []
for row in R['changes']:
    for key,source in [('c',C),('h',H)]:
        if row[key] != '(nothing)' and norm(row[key]) not in norm(source):
            bad.append((row['id'],key,row[key]))
    assert (ROOT/'work'/row['crop']).exists(), row['crop']
for row in R['audit_boxes']:
    x0,y0,x1,y1=row['xyxy']; assert 0<=x0<x1<=1685 and 0<=y0<y1<=2361
if bad:
    print('SOURCE EXCERPTS NEED CORRECTION:')
    for item in bad: print(item)
    raise SystemExit(1)

(OUT/'report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':PAGE,'crops':len(BOX),'changes':len(R['changes']),
    'marks':len(R['decisions']),'inventory':len(R['inventory']),
    'audit_boxes':len(R['audit_boxes']),'doubts':len(R['doubts']),
    'diff_rows':len(R['diff_coverage']),'draft_lines':R['line_count']},ensure_ascii=False))
