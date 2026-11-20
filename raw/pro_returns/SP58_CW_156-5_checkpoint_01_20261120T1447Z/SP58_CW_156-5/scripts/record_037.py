from records import commit,OUT
tex=(OUT.parents[1]/'source/SP58_CW_156-5_witnesses/codex/J156-5-05/pages/J156-5-05_156-5_scan037.tex').read_text()
for a,b in [(r'\unsure{commutatifs|commutatif}','commutatifs'),(r'\unsure{qui en}','qui en'),(r'\unsure{préord}','préord'),(r'\unsure{satisfont|satisfait}','satisfont'),(r'\unsure{ultr.}','ultr.'),(r'\unsure{A}','A'),(r"\unsure{S|S'}",r"S'")]:
 assert a in tex,a
 tex=tex.replace(a,b)
ch=[]
def add(place,c,h,f,e,k='misread word',conf='high',ac=False,ah=True,hm=False,con=''):ch.append((place,c,h,f,e,k,conf,ac,ah,hm,con))
add('opening word','aussitôt','immédiat','aussitôt','Upper half, first word: reduced au-ss-i sequence and circumflex before terminal t. No initial im-mé. ')
add('square first object','+J′ / J′','J′','+J′ / J′','037 square_start crop (560,375,685,480): distinct vertical crosses the left cap of J; whether an extra + or an old start remains uncertain.','omission','low')
add('below square cancellation','qui en, doubtful','ill.','qui en','037 under_square crop (270,600,1650,770): long q descender and separate en under a single cancellation.','readable ink left as \\ill{}','medium',False,True,True)
add('below square insertion','d’ens ordonnés (ou préord)','d’ens. ordonnés; (on prend)','d’ens ordonnés (ou préord)','Same under_square crop: ou before the abbreviated préord, all on the raised replacement baseline.','insertion or placement')
add('first topology prefix','ultr.','ultra-','ultr.','Upper half: a dot after ultr, followed by a space before topologies.','expansion or normalisation')
add('préordonnées emphasis','double underline on pré','no emphasis','double underline on pré','Upper half interlinear insertion: two short underlines under the prefix.','omission')
add('sans prendre la peine','tjrs d’expliciter laborieusement','des types d’explicitation laborieuse','tjrs d’expliciter laborieusement','Lower half opening lines: tjrs has a long j descender; expliciter ends in -ter, and laborieusement has its long -ment ending.')
add('ensembles d’indices','d’indices in baseline','d’indices inserted','d’indices in baseline','Whole and lower half: same baseline and pen size as ensembles; the separate insertion underneath is de L for figure.','insertion or placement')
add('after Une “figure”','inserted de L','omitted','inserted de L','Lower half, y1320–1370: de L above the continuation with a placement line.','omission')
add('ambient letter','L','calligraphic L','L','Lower half, y1590: plain angular L, matching the inserted de L.','misread symbol or index')
add('second topology prefix','ultr.','ultra-','ultr.','Lower half, y1540–1600: compact ultr followed by a period; no a or hyphen.','expansion or normalisation')
add('after voisinages','inserted [ouverts, si on veut], comma doubtful','omitted here; [ou autrement dit] later','inserted [ouverts, si on veut], comma doubtful','037 neighbourhood crop (535,1880,970,1955): bracketed ouverts ... si on veut, placement line immediately after voisinages.','insertion or placement','medium')
add('second equivalent condition','ou encore que tt pt','on présume que tout pt','ou encore que tt pt','Lower half: ou encore followed directly by que; tt is two short t strokes.','misread word')
add('néc. ouvert parenthesis','néc. ouvert).','nécess. ouvert)).','néc. ouvert).','Lower half: three-letter néc abbreviation and one closing parenthesis. Outer topologie parenthesis remains unclosed in the ink.','expansion or normalisation')
add('Si ... sont comme','ça','ci-dessus','ça','Lower half, y2150: short ç with cedilla and a; no long ci-dessus sequence.','misread word')
add('induisent la = topologie','= (for même)','même','= (for même)','Lower half, y2200: two horizontal parallel strokes, not the word même.','expansion or normalisation')
add('closedness insertion, first S','S / S′','S','S′','037 closed crop (980,2210,1555,2285): a distinct raised curved prime lies immediately above/right of the first S, just as at the second S′.','misread symbol or index','high',True,True,False,'The insertion says closed in S′ (pour T), then S′ (pour T′). The first prime is retained despite the expected unprimed S.')
add('closedness clause state','inserted','baseline','inserted','Whole/bottom half: small raised writing above et alors, with placement after S∩S′.','insertion or placement')
add('final clause','et alors y a une unique','et alors il y a une unique','et alors y a une unique','Bottom baseline: no il before y a.','text not on the page')
inv=[('text','top centre','36'),('text','opening','aussitôt que K est objet final'),('diagram','upper','J′ I′ / J I'),('deletion','under square','qui en'),('insertion','under square','d’ens ordonnés (ou préord)'),('text','after square','qui satisfont la condition précédente'),('margin note','left, dated paragraph','18 Juin'),('text','dated paragraph','Dans toutes ces questions'),('insertion','after ultr. topologies','i.e. top. préordonnées'),('insertion','after figure','de L'),('deletion','in pair (S,T)','A'),('insertion','after voisinages','[ouverts, si on veut]'),('insertion','foot after S∩S′','qui est fermé dans S′ (pour T) et dans S′ (pour T′)')]
notes='''### 037-N1 — Statements and date

Continuation: K is asserted to be a final object among the displayed commutative squares of ordered or preordered sets satisfying the preceding condition. The author tentatively writes “Ça devrait impliquer (b,c,d)⇔a)”. This is a proposed consequence, not a completed proof. The explicit underlined date is 18 Juin; the page gives no year. Manuscript pagination 36.

### 037-N2 — Change of viewpoint

The dated passage represents a figure of L by a subset S and an “ultr.” topology T, defined by closure under arbitrary unions of closed sets, equivalently arbitrary intersections of open sets or smallest neighbourhoods. The definition of compatibility requires equal induced topologies on S∩S′ and a closedness insertion. The first ambient S in that insertion visibly has a prime, although followed by T, and is preserved. The pair-membership and cartesian-square issues on the preceding page do not justify altering this ink. The first large topologie parenthesis is not visibly closed; no editorial parenthesis is supplied.

### 037-N3 — Scope of checking

No new proof check on this sheet. The finality assertion and the proposed equivalence have been transcribed and identified, not certified. The neighbourhood definitions are recorded without an additional theorem claim.'''
doubts=r'''| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| square first object | +J′ | J′ with a crossed start | low |
| inserted bracket after voisinages | ouverts, si on veut | ouverts si on veut | medium |

C’s ten listed doubt places were all examined. Resolved: commutatifs; deleted qui en; préord; satisfont; both ultr. prefixes; deleted A. The first S in the closedness insertion is resolved to S′ by a visible detached prime, not by its expected mathematical role. The comma within the bracket remains open.'''
hand='''The short cross at the left of the square’s J′ may be a surplus plus or an earlier start; its interpretation remains open. The dotted ultr. abbreviation appears twice and should not be expanded to ultra-. Double underlining applies only to pré in préordonnées. The footnote-like inserted closedness clause uses a clear short raised prime at both S occurrences, even where the first is paired with T. The sign = again abbreviates même.'''
commit(37,tex,ch,inv,notes,doubts,hand,notation='A figure is a pair (S,T); T is the topology, not the earlier subset T in the ordered-set diagrams. L is a plain angular capital. The prime on the first S of the final insertion is an apparent manuscript slip.',abbr='ultr. = ultra (truncated prefix); tjrs = toujours; tt = tout; pt = point; néc. = nécessairement; top. = topologie; préord = préordonnés.')
