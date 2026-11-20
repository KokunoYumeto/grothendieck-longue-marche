from pathlib import Path
import json
from datetime import datetime, timezone

root=Path('/workspace/scratch/b9993b8b5640')
out=root/'out/readers/A57-02_57_scan077/R3'
a=str(root/'source/SP54_CW_57+63_scans/A57-02_57_scan077_a.jpg')
b=str(root/'source/SP54_CW_57+63_scans/A57-02_57_scan077_b.jpg')
w=str(root/'source/SP54_CW_57+63_scans/A57-02_57_scan077.jpg')
crop_data=[json.loads(p.read_text()) for p in sorted((out/'crops').glob('*.json'))]
cp={int(Path(x['file']).name.split('_')[0]):x['file'] for x in crop_data}
for x in crop_data:
    width=x['bbox'][2]-x['bbox'][0]
    height=x['bbox'][3]-x['bbox'][1]
    x['scale']=round(x['output_size'][0]/width,6) if x['rotation']==0 else None
    x['scale_note']='Output width divided by unrotated source box width.' if x['rotation']==0 else 'Rotation -12 degrees expands the box; output width is 3000 pixels after rotation. See output_size for the final scale.'
    x['viewed_once']=True

def ev(n, box=None):
    d=crop_data[n-1]
    return {'source':d['source'],'bbox':box or d['bbox'],'crop_file':d['file'],'basis':'single tight-crop inspection'}
def half_ev(source,box):
    return {'source':source,'bbox':box,'basis':'single supplied-half inspection; box supplied for adjudication'}

changes=[]
def ch(id,place,c,h,reading,dc,dh,kind,marked,confidence,shows,evidence,crop=None,consequence=None):
    changes.append({'id':id,'place':place,'c':c,'h':h,'reading':reading,'differs_c':dc,'differs_h':dh,'kind':kind,'h_marked':marked,'confidence':confidence,'scan_shows':shows,'evidence':evidence,'crop':cp[crop] if crop else None,'mathematical_consequence':consequence})

ch('R3-01','L05, cancelled words after datum means.',r'\deleted{\unsure{By a}}',r'\struck{By}',r'\deleted{By a}',True,True,'omission','no','medium','A capital B, a lower y with descender, a cancelled blank position and a final round-bodied a remain beneath typed x overstrikes. The a is retained; C doubt removed.',ev(1,[1503,493,1608,536]),1)
ch('R3-02','L09, punctuation after it',r'it\deleted{\unsure{:}}.',r'it.',r'it\deleted{\unsure{:}}.',False,True,'omission','no','medium','An x-shaped typed cancellation lies above the low full stop. A prior colon remains a tentative underlayer; its upper point is obscured.',ev(2,[593,779,670,823]),2)
ch('R3-03','L10, clipped final S after over',r'\unsure{S}',r'S',r'S',True,False,'other','no','medium','The right edge removes the rightmost portion, but the surviving upper and lower curved portions and lower serif support capital S.',ev(3,[1550,855,1685,916]),3)
ch('R3-04','L12, first raised mark on f',r'\unsure{f^{\bullet}|f^{\circ}|f\'}',r'f^{\cdot}',r'f^{\bullet}',True,False,'other','no','high','The raised mark is compact and filled, with no visible aperture or prime shaft. The H dot and the proposed bullet encode that same observed point.',ev(4,[883,1004,949,1048]),4)
ch('R3-05','L12, first Pic capital',r'\unsure{\mathbb{P}|P}\mathrm{ic}',r'\mathrm{Pic}',r'\unsure{\mathbb{P}|P}\mathrm{ic}',False,True,'misread symbol or index','no','medium','The first capital has displaced or doubled vertical/bowl strokes and a much heavier impression than the second P. Deliberate doubled alphabet and overlapping plain P remain alternatives.',ev(4,[947,1008,1010,1059]),4,'The alphabet remains undecided; no meaning is supplied from convention.')
ch('R3-06','L12, target Pic subscript',r'\text{\uuline{Pic}}_{X/S}',r'\underline{\underline{\mathrm{Pic}}}_{X\'/S}',r'\text{\uuline{Pic}}_{X/S}',False,True,'misread symbol or index','no','high','The lower string after the second Pic has X, slash and S. No separate raised prime appears between X and slash.',ev(4,[1121,1007,1257,1064]),4,'The written target subscript X/S is retained; no prime is supplied.')
ch('R3-07','L12, word space before full stop following second Pic',r'_{X/S}$. Assume:',r'_{X\'/S}$. Assume:',r'_{X/S}$ . Assume:',True,True,'other','no','high','A vacant typewriter position separates the target S from the following full stop. This row records the punctuation gap only; the target prime difference is R3-06.',ev(4,[1224,1010,1347,1064]),4)
ch('R3-08','L13, cancelled v in have correction',r'\deleted{v}',r'has',r'\deleted{v}',False,True,'omission','no','medium','The handwritten s occupies the old v position. Portions of the typed angled body remain under the hand stroke; the source layer is preserved before the s.',ev(4,[1302,1076,1389,1122]),4)
ch('R3-09','L13, cancelled final e in have correction',r'\deleted{e}',r'has',r'\deleted{e}',False,True,'omission','no','medium','A separate terminal typed body after the replacement s is overstruck. The underlying e is retained as the final cancelled letter of have.',ev(4,[1341,1076,1389,1122]),4)
ch('R3-10','L15, cancelled terminal letter of morphisme',r'morphism\deleted{\unsure{e}}',r'morphism',r'morphism\deleted{\unsure{e}}',False,True,'omission','no','medium','An additional last character carries crossing strokes after the final m. Residual curved strokes support e, with uncertainty retained.',ev(5,[282,232,472,273]),5)
ch('R3-11','L16, overwritten character beneath handwritten f_*',r'\deleted{\unsure{g}}\handwritten{f_{*}}',r'f_{*}',r'\deleted{\unsure{g}}\handwritten{f_{*}}',False,True,'omission','no','low','The tall handwritten loop and star cover a lower typed rounded body and descending remnant. Tentative g is preserved as the overwritten layer.',ev(6,[691,296,750,342]),6)
ch('R3-12','L16, two lines between the second and third sheaf terms',r'\handwritten{\unsure{\rightrightarrows|\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}}}',r'\rightrightarrows',r'\handwritten{\unsure{\rightrightarrows|\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}}}',False,True,'other','no','medium','Two horizontal hand strokes are clear. The upper right end has an angular head. The lower right end is a rounded dark swelling whose arrowhead remains unresolved.',ev(6,[829,304,899,344]),6,'A lower plain bar remains an explicit alternative to a lower arrow; exactness terminology did not settle the ink.')
ch('R3-13','L16, subscript on h',r'h_{\handwritten{\unsure{*|\uparrow}}}',r'h_{*}',r'h_{\handwritten{\unsure{*|\uparrow}}}',False,True,'other','no','low','A small multi-ray hand mark follows h below its body. Three principal rays are distinct; the star and upward-mark readings remain possible.',ev(6,[910,300,963,344]),6,'The subscript is left undecided from its strokes.')
ch('R3-14','L16–L17, underlined provided/replacement-of-S clause',r'\uline{provided we replace $S$ by a suitable non empty open set}',r'provided we replace $S$ by a suitable non empty open set',r'\uline{provided we replace $S$ by a suitable non empty open set}',False,True,'other','no','high','A hand underline begins beneath provided we and continues beneath the next-line replacement clause. H has plain inline text and a confident editorial note acknowledging the underlining; that note is not a doubt mark.',{'source':b,'bboxes':[[1412,299,1655,358],[282,368,1128,428]],'basis':'single supplied-half inspection; crop 08 also includes the beginning of the line'},None)
ch('R3-15','Left marginal query, initial glyph',r'\unsure{$\epsilon$|e|c|$\in$}',r'\uncertain{$S$}',r'\unsure{$\epsilon$|e|c|$\in$}',False,True,'misread symbol or index','yes','low','A small open curved form has upper/lower arcs and a short middle trace. The surviving curve supports epsilon/e/c/in alternatives; no definite capital S is established.',ev(7,[20,391,53,425]),7)
ch('R3-16','Left marginal query, word after initial glyph',r'not',r'\ill{}',r'not',False,True,r'readable ink left as \ill{}','yes','high','The strokes give n, a small rounded o and a taller crossed t.',ev(7,[56,389,112,426]),7)
ch('R3-17','Left marginal query, lower word',r'needed',r'\uncertain{needed}',r'needed',False,True,'other','yes','medium','The lower line gives needed, with the two taller d strokes and intervening e loops, followed by a question mark.',ev(7,[45,414,175,465]),7)
ch('R3-18','L17, cancelled final letter of homomorphisme',r'homomorphism\deleted{\unsure{e}}',r'homomorphism',r'homomorphism\deleted{\unsure{e}}',False,True,'omission','no','medium','There is a separate x-overprinted terminal body after m. Its remaining curved interior supports e, with doubt retained.',ev(8,[1217,366,1494,404]),8)
ch('R3-19','L18, final s of first quasi-affine morphisms',r'morphisms',r'morphism\struck{s}',r'morphism\deleted{s}',True,False,'deletion state','no','medium','The last curved letter has crossing diagonal impressions and a broadened top/bottom overprint. I read a typed x cancellation over the underlying s; the final s is preserved as deleted.',ev(9,[907,438,1116,479]),9,'The source cancellation is retained without grammatical or mathematical repair.')
ch('R3-20','L18, crowded e in specifically',r'sp\unsure{e}cifically',r'specifically',r'specifically',True,False,'other','no','medium','A small rounded e body with an internal horizontal trace is displaced toward and crowded against p; cifically follows. The e is readable in the enlarged ink.',ev(10,[1222,438,1480,483]),10)
ch('R3-21','L18, cancelled word before in',r'\deleted{the}',r'\struck{that}',r'\deleted{the}',False,True,'misread word','no','high','Three letter positions show tall t, tall h and round-bodied e under the cancellation. There is no fourth typed letter position in this cancelled word.',ev(10,[1494,434,1577,481]),10)
ch('R3-22','L19, raised mark on f before via',r'f^{\circ}',r'f^{\cdot}',r'f^{\circ}',False,True,'misread symbol or index','no','medium','The small round raised sign has a visible lighter centre enclosed by darker ink.',ev(11,[735,507,783,553]),11,'The locally open raised mark is retained; no identity with the filled marks is inferred.')
ch('R3-23','L19, attachment of via to the raised-f label',r'f^{\circ}$via',r'f^{\cdot}$ via',r'f^{\circ}$via',False,True,'other','no','high','The v follows the raised-mark position without an intervening empty typewriter cell. This row concerns the missing word gap; the raised shape is separately recorded in R3-22.',ev(11,[733,508,851,555]),11)
ch('R3-24','L20, cancelled phrase following u affine',r'\deleted{\unsure{as you know, both}}',r'\struck{\ill{}}',r'\deleted{\unsure{as you know,both|as you know, both}}',True,True,r'readable ink left as \ill{}','yes','low','The x overstrikes leave tentative as, the y descender in you, a tall k and know, comma, then the last ascenders of both. The surviving typewriter positions favor adjacency after the comma; a normal space there remains the explicit alternative. Several underlying bodies remain obscured.',ev(12,[833,583,1162,625]),12)
ch('R3-25','L21, first word of handwritten insertion before immersions',r'\inserted{\handwritten{\unsure{finite} direct sums of}}',r'\add{finite direct sums of}',r'\inserted{\handwritten{finite direct sums of}}',True,False,'other','no','medium','The hand reads f-i-n-i-t-e, with a compressed final loop attached to the preceding tall stroke; direct sums of follows. A bracket and downward stroke attach the insertion between by and immersions.',ev(13,[1199,601,1559,690]),13)
ch('R3-26','L22, handwritten numeral in Corollary heading',r'\uline{Corollary \handwritten{1}}',r'\emph{Corollary}',r'\uline{Corollary \handwritten{1}}',False,True,'omission','no','high','A thin handwritten 1 stands immediately after the underlined Corollary and before Without. Its short lower line is visible with the heading underline.',half_ev(b,[280,737,510,792]),None)
ch('R3-27','L23, index in the family X_i',r'X_{i}',r'X_1',r'X_{i}',False,True,'misread symbol or index','no','high','The lowered mark has a detached round dot above its short stem and a basal serif, supporting i.',ev(14,[966,807,1026,863]),14,'The written family index is i; no change to the source statement is inferred.')
ch('R3-28','L23, heavy X after finite over',r'\unsure{\mathbb{X}|X}',r'X',r'\unsure{\mathbb{X}|X}',False,True,'misread symbol or index','no','medium','Offset crossing strokes and enlarged serifs produce a doubled impression. A doubled alphabet and an overstruck plain X remain unresolved.',ev(14,[1254,804,1313,854]),14)
ch('R3-29','L24, raised mark on the Corollary f',r'f^{\circ}',r'f^{\cdot}',r'\unsure{f^{\circ}|f^{\bullet}}',True,True,'misread symbol or index','no','low','The compact round raised body has a small lighter core, much less distinct than the L19 aperture. The crop leaves an open ring and an uneven filled point as alternatives.',ev(15,[617,879,668,928]),15,'The raised glyph remains undecided; it is not regularized to the other f labels.')
ch('R3-30','L24, cancelled finite',r'\deleted{\unsure{finite|finit}}',r'\struck{finite}',r'\deleted{finite}',True,False,'other','no','medium','Six typed letter positions remain under the crossing overstrikes. After the tall t there is a separate final rounded e body.',ev(15,[1068,877,1204,931]),15)
ch('R3-31','L25, clipped final of',r'\unsure{of}',r'of',r'of',True,False,'other','no','medium','The lower round o is visible at the edge, and the next letter leaves a tall upper hook and crossbar of f before the black boundary. The final word is read from these surviving portions.',ev(16,[1629,950,1685,1013]),16)

# Correct Python raw-string quoting used to represent literal primes in exact witness fragments.
for row in changes:
    for field in ('c','h','reading'):
        row[field]=row[field].replace("\\'", "'")

c_doubts=[]
def doubt(place,c,reading,status,n,confidence,box=None):
    c_doubts.append({'place':place,'c':c,'reading':reading,'status':status,'evidence':ev(n,box),'crop':cp[n],'confidence':confidence})
doubt('L05, cancelled By a',r'\unsure{By a}',r'By a','resolved',1,'medium')
doubt('L09, cancelled punctuation',r'\unsure{:}',r'\unsure{:}','retained',2,'medium')
doubt('L10, final S',r'\unsure{S}',r'S','resolved',3,'medium')
doubt('L12, first f raised mark',"\\unsure{f^{\\bullet}|f^{\\circ}|f'}",r'f^{\bullet}','resolved',4,'high')
doubt('L12, first Pic capital',r'\unsure{\mathbb{P}|P}',r'\unsure{\mathbb{P}|P}','retained',4,'medium')
doubt('L15, final morphisme character',r'\unsure{e}',r'\unsure{e}','retained',5,'medium')
doubt('L16, overwritten g',r'\unsure{g}',r'\unsure{g}','retained',6,'low')
doubt('L16, parallel strokes',r'\unsure{\rightrightarrows|\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}}',r'\unsure{\rightrightarrows|\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}}','retained',6,'medium')
doubt('L16, h subscript',r'\unsure{*|\uparrow}',r'\unsure{*|\uparrow}','retained',6,'low')
doubt('L17 left margin, query initial',r'\unsure{$\epsilon$|e|c|$\in$}',r'\unsure{$\epsilon$|e|c|$\in$}','retained',7,'low')
doubt('L17, final homomorphisme character',r'\unsure{e}',r'\unsure{e}','retained',8,'medium')
doubt('L18, specifically e',r'\unsure{e}',r'e','resolved',10,'medium')
doubt('L20, cancelled phrase',r'\unsure{as you know, both}',r'\unsure{as you know,both|as you know, both}','revised',12,'low')
doubt('L21, handwritten finite',r'\unsure{finite}',r'finite','resolved',13,'medium')
doubt('L23, heavy X',r'\unsure{\mathbb{X}|X}',r'\unsure{\mathbb{X}|X}','retained',14,'medium')
doubt('L24, cancelled finite',r'\unsure{finite|finit}',r'finite','resolved',15,'medium')
doubt('L25, final of',r'\unsure{of}',r'of','resolved',16,'medium')

remaining=[]
def rem(place,reading,alternatives,confidence,reason,n):
    remaining.append({'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason,'crop':cp[n]})
rem('L09, cancelled punctuation',r'\deleted{\unsure{:}}.',[], 'medium','The low stop is visible; the crossed upper position does not reveal the original point independently.',2)
rem('L12, first Pic capital',r'\unsure{\mathbb{P}|P}',[r'\mathbb{P}',r'P'],'medium','Offset strokes do not decide deliberate doubling versus a plain overprinted P.',4)
rem('L15, cancelled morphisme ending',r'\deleted{\unsure{e}}',[r'e'],'medium','The x overprint obscures the underlying terminal body.',5)
rem('L16, overwritten letter',r'\deleted{\unsure{g}}',[r'g'],'low','Handwritten f_* overlaps the rounded body and lower remnant of the typed layer.',6)
rem('L16, lower parallel stroke',r'\unsure{\rightrightarrows|\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}}',[r'\rightrightarrows',r'\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}'],'medium','The lower right termination is rounded and thick; a separate angled head is unresolved.',6)
rem('L16, h subscript',r'\unsure{*|\uparrow}',[r'*',r'\uparrow'],'low','Only three principal rays separate clearly.',6)
rem('L17, marginal initial',r'\unsure{$\epsilon$|e|c|$\in$}',[r'\epsilon','e','c',r'\in'],'low','The tiny open curved body and middle trace do not settle the glyph.',7)
rem('L17, cancelled homomorphisme ending',r'\deleted{\unsure{e}}',[r'e'],'medium','The crossing typewriter impression obscures the terminal character.',8)
rem('L20, cancelled phrase',r'\deleted{\unsure{as you know,both|as you know, both}}',['as you know,both','as you know, both'],'low','Words are tentative under x overstrikes; the number of occupied cells favors no comma space, but the gap remains uncertain.',12)
rem('L23, heavy X',r'\unsure{\mathbb{X}|X}',[r'\mathbb{X}',r'X'],'medium','Offset crossing strokes leave alphabet intention undecided.',14)
rem('L24, Corollary f mark',r'\unsure{f^{\circ}|f^{\bullet}}',[r'f^{\circ}',r'f^{\bullet}'],'low','The pale central core is too small to decide aperture versus an uneven filled point.',15)

inventory=[]
def inv(element,kind,position,words,hand='typewriter'):
    inventory.append({'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('077-R3-01','text','L01, top continuation','the n.th power homomorphism')
inv('077-R3-02','text','L02–L09, opening paragraph','I tell you about this, namely (i)')
inv('077-R3-03','deletion','L05, after datum means.','By a under typed x overstrikes')
inv('077-R3-04','insertion','L08, above and/some','to, with a caret attachment','another unnamed hand')
inv('077-R3-05','deletion','L09, after it','tentative colon under an x; final low stop retained')
inv('077-R3-06','text','L10, heading','Theorem, with single underline')
inv('077-R3-07','text','L10–L21, theorem paragraph','Let S be an integral noetherian scheme')
inv('077-R3-08','insertion','L10, after second X','prime','another unnamed hand')
inv('077-R3-09','text','L11, morphism formula','f:X′→X')
inv('077-R3-10','insertion','L11, after source X in f formula','prime','another unnamed hand')
inv('077-R3-11','insertion','L11, between the two X terms','right arrow','another unnamed hand')
inv('077-R3-12','text','L12, Picard functor formula','f raised point: double-underlined Pic_X/S to double-underlined Pic_X/S, then space and full stop')
inv('077-R3-13','insertion','L12, between Picard names','right arrow','another unnamed hand')
inv('077-R3-14','deletion','L13, end of problems','s crossed by manuscript strokes','another unnamed hand')
inv('077-R3-15','deletion','L13, after A','and B beneath hand cancellation','another unnamed hand')
inv('077-R3-16','deletion','L13, have correction','typed v replaced by handwritten s')
inv('077-R3-17','insertion','L13, have correction','s over old v','another unnamed hand')
inv('077-R3-18','deletion','L13, end of have correction','typed e cancelled')
inv('077-R3-19','deletion','L15, morphisme before f_s','uncertain terminal e under x')
inv('077-R3-20','text','L15, generic-fiber map','f_s:X′_s→X_s')
inv('077-R3-21','insertion','L15, generic-fiber map','prime on source X','another unnamed hand')
inv('077-R3-22','insertion','L15, generic-fiber map','right arrow','another unnamed hand')
inv('077-R3-23','text','L16, inline exactness expression','O underlined with lower X_s, f_*(O underlined with lower X′_s), h with uncertain subscript and O underlined with lower X′′_s')
inv('077-R3-24','insertion','L16, after first sheaf term','right arrow','another unnamed hand')
inv('077-R3-25','deletion','L16, below handwritten f_*','uncertain typed g overwritten')
inv('077-R3-26','insertion','L16, before middle sheaf parentheses','f_*','another unnamed hand')
inv('077-R3-27','insertion','L16, middle sheaf subscript X','prime','another unnamed hand')
inv('077-R3-28','insertion','L16, before h','parallel hand strokes, lower arrowhead uncertain','another unnamed hand')
inv('077-R3-29','insertion','L16, lower right of h','star/upward-mark alternatives','another unnamed hand')
inv('077-R3-30','insertion','L16–L17, beneath replacement clause','single hand underline beneath provided we / replace S by a suitable non empty open set','another unnamed hand')
inv('077-R3-31','margin note','L17, left margin','uncertain initial glyph, not / needed?','another unnamed hand')
inv('077-R3-32','deletion','L17, end of homomorphisme','uncertain e under x')
inv('077-R3-33','text','L17, after homomorphisme','f with filled raised point, is')
inv('077-R3-34','deletion','L18, after representable by','a cancelled')
inv('077-R3-35','deletion','L18, final letter of first quasi-affine morphisms','s read as crossed by x')
inv('077-R3-36','text','L18, specifically','crowded displaced e against p')
inv('077-R3-37','deletion','L18, before in','the under typewriter cancellation')
inv('077-R3-38','text','L19, factorisation label','f with open raised ring attached to via')
inv('077-R3-39','text','L20, factorisation equality','f with filled raised point = vu with u affine')
inv('077-R3-40','deletion','L20, after affine','tentative as you know,both / as you know, both')
inv('077-R3-41','insertion','L20–L21, above by/immersions','finite direct sums of, under-bracket with curved ends and descending attachment before immersions','another unnamed hand')
inv('077-R3-42','text','L22, heading','Corollary, single underline')
inv('077-R3-43','insertion','L22, immediately after Corollary','1 with short lower stroke','another unnamed hand')
inv('077-R3-44','text','L22–L24, Corollary paragraph','Without assuming b), but instead in a)')
inv('077-R3-45','text','L23, family and covering scheme','X_i finite over heavy X')
inv('077-R3-46','text','L24, representability label','f with circle/bullet alternatives')
inv('077-R3-47','deletion','L24, before quasi-affine','finite under x overstrikes')
inv('077-R3-48','text','L25, final continuation','This follows from the theorem, using a suitable factorisation of')
inv('077-R3-49','margin note','lower left corner','archive pencil number 76, transcribed as comment','another unnamed hand')

notation=[]
def nt(sign,latex,place,shape,alternatives=[]):
    notation.append({'sign':sign,'latex':latex,'place':place,'visible_shape':shape,'alternatives':alternatives})
nt('first raised f point',r'f^{\bullet}','L12','Compact filled raised round/near-square point; no distinct prime shaft or aperture.')
nt('second raised f point',r'f^{\bullet}','L17','Compact filled raised point after the typed f.')
nt('third raised f ring',r'f^{\circ}','L19','Dark circular outline with lighter centre, immediately before via.')
nt('fourth raised f point',r'f^{\bullet}','L20','Filled raised point in f = vu, read in the supplied half.')
nt('Corollary raised f sign',r'\unsure{f^{\circ}|f^{\bullet}}','L24','Small rounded body with a weak pale central core.',[r'f^{\circ}',r'f^{\bullet}'])
nt('first Pic capital',r'\unsure{\mathbb{P}|P}\mathrm{ic}','L12','Heavy offset capital P strokes followed by lower ic; two underline rows.',[r'\mathbb{P}',r'P'])
nt('second Pic name and subscript',r'\text{\uuline{Pic}}_{X/S}','L12','Plain capital P and lower ic; two underline rows; lower X/S with no visible prime.')
nt('Pic source subscript',r'_{X/S}','L12','Capital X, slash and capital S beneath the first Pic.')
nt('family index',r'X_i','L23','Lowered i with separated dot, short upright and basal serif. H has 1.',[r'i'])
nt('heavy X',r'\unsure{\mathbb{X}|X}','L23','Offset superposed crossing strokes and enlarged serifs.',[r'\mathbb{X}',r'X'])
nt('generic-fiber labels',r'f_s:X\handwritten{\prime}_s\handwritten{\to}X_s','L15','Lower two-lobed s on f and both X terms; one slanted hand prime and right arrow.')
nt('structure sheaf terms',r'\underline O_{X_s},\ \underline O_{X\prime_s},\ \underline O_{X\prime\prime_s}','L16','Each capital O singly underlined; lower capital X with zero, one, and two primes respectively; each nested s sits lower.')
nt('first sequence arrow',r'\handwritten{\to}','L16','Hand-drawn horizontal shaft with two visible oblique head strokes at right.')
nt('overwritten map character',r'\deleted{\unsure{g}}\handwritten{f_*}','L16','Typed lower rounded body and descending remnant under taller hand loop and star.',[r'g'])
nt('parallel sequence strokes',r'\unsure{\rightrightarrows|\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}}','L16','Two horizontal strokes; clear upper angular head, rounded lower termination.',[r'\rightrightarrows',r'\substack{\longrightarrow\\[-0.7ex]\rule{1.4em}{0.4pt}}'])
nt('h subscript',r'h_{\unsure{*|\uparrow}}','L16','Small hand mark with three clear rays.',[r'*',r'\uparrow'])
nt('marginal initial',r'\unsure{\epsilon|e|c|\in}','L17 left margin','Small open curved form with short central trace.',[r'\epsilon','e','c',r'\in'])
nt('factorisation equality',r'f^{\bullet}=vu','L20','Typed equal sign has two short horizontal bars; lower-case v and u follow.')

report={
 'page':'A57-02_57_scan077','cote':'57','our_scan':'77','reader':'R3',
 'start_utc':'2026-11-20T11:32:16Z','end_utc':datetime.now(timezone.utc).isoformat(),
 'model':'GPT-6 Astra Pro','effort':'not exposed','run_identity':'/root/p57_077_r3',
 'images_viewed':[w,a,b],'crops':crop_data,
 'coverage':{'all_lines_read':True,'all_elements_included':True,'concise_block_list':['L01 top continuation','L02–L09 method/effectivity paragraph and two corrections','L10–L21 theorem, inline formulas, cancelled source layers and insertions','L16–L17 underlined clause and left marginal query','L22–L24 Corollary 1 and cancelled finite','L25 bottom continuation','lower-left archive number 76'],'main_typed_lines':25,'whole_views':1,'half_a_views':1,'half_b_views':1,'crop_views':16,'discarded_images':0},
 'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
 'notes':{
   'summary':'The page continues a statement about the n.th power homomorphism in the Picard prescheme, explains the interest in a method involving non flat descent and the absence of a good effectivity criterion, states a theorem and Corollary 1 about representability of Picard-functor homomorphisms, writes an exactness expression and a factorisation vu, and begins an explanatory continuation. The restriction to a suitable non empty open set is underlined and accompanied by a marginal query. This is a description of the page, without a claim of proof verification.',
   'reading_decisions':[],
   'author_checks':[{'quote':'I do not have any good effectivity criterion','place':'L04','description':'The page explicitly states the missing criterion.'},{'quote':'this is certainly true when X/S is projective','place':'L14','description':'An authorial assertion on the page, not a verification performed here.'},{'quote':r'\unsure{$\epsilon$|e|c|$\in$} not needed?','place':'L17 left margin','description':'The query initial remains uncertain; the question words are readable.'}],
   'titles_dates_pagination':{'headings':['Theorem, singly underlined','Corollary with manuscript 1, underlined'],'date':None,'signature':None,'authorial_pagination':None,'archive_sheet_number':'76','scan_marker':'77'},
   'authorship':'A typed letter continuation with manuscript additions; this page alone supplies no signature or named author. Manuscript hands are left unnamed.',
   'h_editorial_notes':'H has text on this page. Its note about and B and another page is excluded from the transcription, and no other page was consulted. Its note about the marginal question and underlining is descriptive, not an uncertainty mark.',
   'mathematical_scope':'Only written glyphs, nesting of indices, and formula order were inspected. No mathematical fact or theorem was used to choose a reading, and no proof check was performed. In particular, both written Pic subscripts remain X/S.',
   'spacing':'The space before the full stop after the Pic formula is entered explicitly. The f label remains attached to via. The comma spacing in the cancelled phrase remains an explicit alternative. The crowded e in specifically is recorded from the visible displaced impression.',
   'equivalent_encodings_excluded':['H page 76 and scanpage 77 follow the supplied mapping.','H emph and uline agree where the ink has a single underline.','H unwrapped handwritten glyph arguments and C handwritten wrappers add provenance only.','H f^{\\cdot} and f^{\\bullet} encode the same filled raised point where observed.'],
   'physical_features':'Fold lines, mottling, small detached ink specks and upper-right paper damage carry no readable independent text or drawn object.'
 },
 'notation':notation,
 'abbreviations':[{'abbreviation':'i.e.','proposed_expansion':'id est','place':'L16'},{'abbreviation':'n.th','proposed_expansion':'n-th','place':'L01'}],
 'check_events':[],
 'prior_flags':[{'place':'L11–L12','flag':'homomorphisme final e','result':'Retained as visible and agreed; no modernized spelling.'},{'place':'L12','flag':'both Pic subscripts X/S','result':'Confirmed in crop 04; target prime not supplied.'},{'place':'L19','flag':'raised f label immediately followed by via','result':'Confirmed in crop 11; attachment retained.'},{'place':'L23','flag':'X_i family index','result':'Confirmed from detached dot and short stem in crop 14.'}],
 'reader_workflow':{'inputs_read_in_required_order':True,'other_readers_consulted':False,'other_pages_viewed':False,'ocr_used':False,'web_used':False,'recropped_places':False,'all_c_doubts_count':17,'c_doubt_status_counts':{'resolved':7,'retained':9,'revised':1}}
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'crops':len(crop_data),'report':str(out/'report.json')},ensure_ascii=False))
