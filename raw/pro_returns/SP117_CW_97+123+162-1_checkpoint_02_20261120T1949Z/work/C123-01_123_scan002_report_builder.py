import json
from pathlib import Path
R=Path('/workspace/scratch/d27bd2a88bca'); P='C123-01_123_scan002'
M={q['id']:q for q in json.load(open(R/'out/work'/f'{P}_crop_manifest.json'))}
changes=[]
def add(id,line,c,h,final,shows,boxid,confidence,kind,cc,ch,marked=False,consequential=False,certainty=False):
 q=M[boxid]
 changes.append(dict(id=id,line=line,c=c,h=h,final=final,scan_shows=shows,crop=q['crop'],box=q['box'],confidence=confidence,kind=kind,changed_C=cc,changed_H=ch,marked_in_H=marked,consequential=consequential,certainty_only=certainty))
add('b-c01','L01, title insertion',r'\unsure{irréductible|irreductible}','irréductible','irréductible','A small dark accent is visible over the e; the remaining cursive letters read irréductible. The word is circled with a leader after racines.','b01','high','other',True,False,False,False,True)
add('b-c02','M01, under title','th. 9.2.','Th. 9.2','th. 9.2.','The first abbreviation letter is a small t, with a crossbar; it is not an uppercase T. A point follows 2.','b02','high','misread word',False,True)
add('b-c03','L02, toute valeur propre de w est',r'\unsure{est}','est',r'\deleted{\unsure{di}}est','The first position contains the e crossbar plus a higher right ascender and top serif consistent with an underlying d. The second has an i-like dot and upright under the s. Current est is readable; the underlying di remains doubtful.','b03','medium','omission',True,True)
add('b-c04','L04-L05, il faut / et suffit','il faut et il suffit','il faut et suffit','il faut et suffit','The next typed line starts et suffit; no second il occurs. The typed insertion alors has a separate pen leader before les.','b04','high','text not on the page',True,False)
add('b-c05','M02, after correspondant','(qui est de dim 1)','(qui est de dim. 1)','(qui est de dim 1)','The inserted note reads qui est / de dim 1; there is no dark period between dim and 1. The first small circle is the matching insertion marker.','b05','high','other',False,True,True)
add('b-c06','L07, Corollaire label',r'\unsure{1|!}','1','1','The numeral has a sloping top lead and a continuous lower upright, not a separate dot.','b06','high','misread symbol or index',True,False,False,False,True)
add('b-c07','L08, mu isomorphic Z/hZ',r'\mu\simeq\underline{Z}/h\underline{Z}',r'\mu\simeq\mathbf{Z}/h\mathbf{Z}',r'\mu\simeq\underline{Z}/h\underline{Z}','Both typewritten Zs have separate straight underlines. They are not doubled capitals. The pen slash is thick and retraced; no distinct underlying character is secure.','b07','high','misread symbol or index',False,True)
add('b-c08','L10, displayed homomorphism',r'\unsure{\nu|\psi}/\mu\longrightarrow\operatorname{Aut}(\mu)\simeq(\underline{Z}/h\underline{Z})^*',r'\nu/\mu\longrightarrow\operatorname{Aut}(\mu)\simeq(\mathbf{Z}/h\mathbf{Z})^*',r'\unsure{\psi|\nu}/\mu\longrightarrow\operatorname{Aut}(\mu)\simeq(\underline{Z}/h\underline{Z})^*','The numerator has a deep shaft below its two upper branches, visually nearer psi than the unambiguous v-shaped nu in L09. Heavy retracing prevents resolution. Both typed Zs are underlined. The single right arrow and raised star are clear.','b08','medium','misread symbol or index',True,True,False,True)
add('b-c09','M03, right question',r'Quelle extension de $(\unsure{Z|\mathbb{Z}}/hZ)^*$ par $Z/hZ$ obtient-on ?',r'Quelle extension de $(\mathbf{Z}/h\mathbf{Z})^*$ par $\mathbf{Z}/h\mathbf{Z}$ obtient-on ?',r'Quelle extension de $(\unsure{Z|\mathbb{Z}}/hZ]^*$ par $Z/hZ$ obtient-on ?','The closing delimiter of the upper formula has a vertical side with horizontal head and foot, hence a square bracket; the opening sign curves like a parenthesis. The Z versus double-struck Z distinction remains open (first occurrence marked); it is not resolved by the mathematical meaning.','b09','medium','misread symbol or index',True,True,False,True)
add('b-c10','L11, est un isomorphisme',r'\unsure{un}','un',r'u\deleted{j}n','The n has a separate overprinted j: a dot above the right stem and a hooked descender below the baseline remain visible.','b10','high','omission',True,True)
add('b-c11','M04, left exchange note',r'\unsure{échanger|échange} avec cor.\unsure{3|?}',r'\uncertain{échanger avec cor. 3 ?}',r'\unsure{échanger|échange} avec cor.\unsure{3|?}','There is only one large terminal glyph after cor.; it can be a 3 or a question mark. The separate 3 followed by ? of H is not supported. The ending of échanger remains crowded and uncertain.','b11','medium','text not on the page',False,True,True)
add('b-c12','L13, Soit en effet',r'\unsure{en}','en',r'\deleted{\unsure{D|B}}en','The first letter position has a capital-height outer bowl and upper serif underneath a smaller e. D and B remain possible for the overprinted character.','b12','medium','omission',True,True)
add('b-c13','L13, effet',r'ef\inserted{f}et','effet',r'ef\inserted{\handwritten{f}}et','The second f rises above the typed word and has an irregular pen head and downstroke; it occupies the missing f position. H flattens the inserted letter into ordinary text. C already preserves the insertion.','b12','high','insertion or placement',False,True)
add('b-c14','L13, canceled phrase below le sous-espace',r'\deleted{\unsure{une droite}}',r'(omitted)',r'\deleted{\unsure{une droite}}','The line beneath le sous-espace contains a canceled two-word phrase compatible with une droite; x overtyping and a pen strike obscure several letters, so C’s doubt is retained. H omits the readable candidate entirely. The replacement above is typewritten, with a pen leader.','b12','medium','omission',False,True,False,True)
add('b-c15','L14, centralizer definition',r'z=\operatorname{Centr}(\mu)',r'\mathfrak{z}=\operatorname{Centr}(\mu)',r'\mathfrak{z}=\operatorname{Centr}(\mu)','A typed z has a long handwritten lower loop attached at the lower right, making the gothic centralizer sign. The following mu is handwritten in the typed parentheses.','b13','high','misread symbol or index',True,False,False,True)
add('b-c16','L15, homomorphism to Aut(D)',r'z\to\operatorname{Aut}(D)=\underline{C}^{*}',r'\mathfrak{z}\to\operatorname{Aut}(D)=\mathbf{C}^{*}',r'\mathfrak{z}\to\operatorname{Aut}(D)=\underline{C}^{*}','The z has the same appended descending loop; C is typed with a separate underline and a pen star above. Arrowhead is at right.','b14','high','misread symbol or index',True,True,False,True)
add('b-c17','L16, fini de C*',r'\underline{C}^{*}',r'\mathbf{C}^{*}',r'\underline{C}^{*}','The capital C is single typed, with a separate low horizontal underline; its raised star is handwritten.','b15','high','misread symbol or index',False,True)
add('b-c18','L18, retraction',r'z\to\mu',r'\mathfrak{z}\to\mu',r'\mathfrak{z}\to\mu','The typed z has a large descending curved pen tail, consistent with the other three centralizer signs.','b16','high','misread symbol or index',True,False,False,True)
add('b-c19','L19, et qômme D',r'\unsure{qômme|comme}','comme',r'\unsure{qômme|qomme}','The first letter has a closed bowl and descender, clearly q rather than c. Above the o is a small raised compound mark: circumflex is the first reading, but an accidental overprint cannot be excluded. The typed slip is retained.','b17','medium','misread word',False,True,False,False)
add('b-c20','L20, On a donc prouvé',r'\unsure{On|Bn}','On',r'\deleted{\unsure{B}}On','The capital contains both B-like middle construction and an O-shaped outside curve. The candidate underlying B is retained as doubtful under the readable On. The second letter is also thickly retraced, without a securely distinguishable earlier character.','b18','medium','omission',True,True)
add('b-c21','L20, centralizer equality',r'z=\mu',r'\mathfrak{z}=\mu',r'\mathfrak{z}=\mu','The z has a handwritten curled tail below the typed baseline, as at its three earlier occurrences.','b18','high','misread symbol or index',True,False,False,True)
add('b-c22','L23, second corollary heading','Corollaire','Corollaire',r'Coroll\deleted{b}a\deleted{\unsure{j|l}}ire','At the a position a tall b-shaped ascender survives under a; the next position has an overprinted vertical and a lower extension consistent with j, possibly l. Both witnesses silently give the clean heading. The second underlying letter remains doubtful.','b19','medium','omission',True,True)
add('b-c23','L29, third corollary starts',r'\deleted{\unsure{Considérons}} \deleted{Soit $D$ une}\inserted{Soit $D$ une}',r'\struck{Soit D une} \struck{Considérons}',r'\deleted{\unsure{Considérons}} \deleted{Soit $D$ une}\inserted{Soit $D$ une}','Three separate baselines are visible: Considérons at top is canceled, Soit D une at the base is canceled by x overtyping and a pen line, and a separate Soit D une between them is live. H omits the live middle insertion. The top canceled word remains doubtful where x strokes cover letters.','b22','high','omission',False,True,False,True)
add('b-c24','L29, V tensor C',r'V\unsure{\otimes|\mathbin{\text{\textcircled{x}}}}\underline{C}',r'V\otimes\mathbf{C}',r'V\otimes\underline{C}','The typewriter has put x and a rounded O on one position to form the tensor sign. It is not a plus sign. The C has a separate underline. The visible s in régulières belongs to the source, and is retained.','b23','high','misread symbol or index',True,True,False,False,True)

D=[
 dict(line='L02',reading=r'\deleted{\unsure{di}}est',alternatives=['underlying di','underlying first d secure; second i probable'],confidence='medium',reason='Overtype substrate partly merges with final e and s; the current word est is clear.'),
 dict(line='L08',reading=r'\mu\simeq\underline{Z}/h\underline{Z}',alternatives=['retraced slash','slash over an unidentifiable earlier mark'],confidence='medium',reason='The thick pen slash has a small thin loop to its upper left. No separate underlying character is entered because it is not secure.'),
 dict(line='L10',reading=r'\unsure{\psi|\nu}/\mu',alternatives=[r'\psi',r'\nu'],confidence='low',reason='Ink has two branches and a descender, unlike clear nu at L09. Mathematical reference favours nu, but does not erase the psi-shaped stroke. Whole formula boxed and cropped.'),
 dict(line='M03',reading=r'(\unsure{Z|\mathbb{Z}}/hZ]^*',alternatives=['Z','double-struck Z'],confidence='medium',reason='Some diagonal strokes seem doubled, especially on the bottom row, but cursive retracing can produce this. Marked once on the page under recurring-glyph convention.'),
 dict(line='M03',reading=r'(Z/hZ]^*',alternatives=['right square bracket','very angular right parenthesis'],confidence='medium',reason='Right boundary has horizontal head and foot. The mismatch with the opening round parenthesis is retained, not corrected.'),
 dict(line='M04',reading=r'\unsure{échanger|échange} avec cor.\unsure{3|?}',alternatives=['échanger','échange','3','?'],confidence='medium',reason='Slanted cursive ending and terminal glyph remain ambiguous; only one terminal glyph exists.'),
 dict(line='L13',reading=r'\deleted{\unsure{D|B}}en',alternatives=['D','B'],confidence='medium',reason='A capital-height outer bowl survives underneath e; the inner e can supply the apparent central bar of B.'),
 dict(line='L13',reading=r'\deleted{\unsure{une droite}}',alternatives=['une droite'],confidence='medium',reason='Several letters are covered by x overtyping and a pen stroke; no confidence upgrade from C.'),
 dict(line='L19',reading=r'\unsure{qômme|qomme}',alternatives=['qômme','qomme'],confidence='medium',reason='Initial q has an unequivocal descender. Raised mark over o may be a circumflex or an overprint; neither permits silently substituting comme.'),
 dict(line='L20',reading=r'\deleted{\unsure{B}}On',alternatives=['B under O','more than one earlier character'],confidence='medium',reason='Composite capital is very dark; readable B-like residue has been kept as a candidate, not made certain.'),
 dict(line='L23',reading=r'Coroll\deleted{b}a\deleted{\unsure{j|l}}ire',alternatives=['j underneath i','l underneath i'],confidence='medium',reason='The a position has a distinct b ascender; the neighboring overprint is less secure. Crop was tightened in place while unresolved, without retaining a duplicate crop.'),
 dict(line='L29',reading=r'\deleted{\unsure{Considérons}}',alternatives=['Considérons'],confidence='medium',reason='The word is compatible with all visible strokes, but some letters remain under typed x strokes; doubt retained.'),
]

# Each inventory row is an observed page element. y is only used to order rows.
I=[]
def inv(y,element,kind,position,first,hand='typewriting with handwritten annotations'):
 I.append((y,dict(scan=2,sheet_kind='typescript',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')))
inv(55,'title qualifier','insertion','above right of title','irréductible','handwriting')
inv(56,'oval and leader around title qualifier','drawing','above title, leader before (Kostant)','oval around irréductible','handwriting')
inv(126,'title','text','top, one typed line','Compléments sur transformation de Coxeter')
inv(152,'English bibliographic note','margin note','under title','The principal 3-dimensional subgroup .... th. 9.2.','handwriting')
inv(196,'statement a)','text','upper paragraph, L02-L06','a) Soit w in W. Alors toute valeur propre')
inv(199,'membership sign in a)','insertion','L02, between w and W',r'\in','handwriting')
inv(202,'overprint in est','deletion','L02, after de w',r'\deleted{\unsure{di}}')
inv(208,'right bracket on statement a)','drawing','right margin, L02-L06','right marginal bracket','handwriting')
inv(307,'inequality in statement a)','insertion','L04, before h',r'\leq','handwriting')
inv(338,'alors','insertion','above L05, inserted before les','alors','typewriting; pen leader')
inv(418,'dimension note','insertion','left margin, called after correspondant in L06','(qui est de dim 1)','handwriting')
inv(418,'dimension insertion marker','drawing','after correspondant in L06','small circle with rising leader','handwriting')
inv(442,'first corollary','text','L07-L12 with display L10','Corollaire 1: Soit mu le sous-groupe')
inv(442,'corollary number','insertion','L07, after underlined Corollaire','1','handwriting')
inv(444,'mu in corollary opening','insertion','L07, after Soit',r'\mu','handwriting')
inv(475,'rule beside first corollary','drawing','left margin L07-L12','vertical rule','handwriting')
inv(500,'cyclic group formula','insertion','L08, after donc',r'\mu\simeq\underline{Z}/h\underline{Z}','typewriting and handwriting')
inv(510,'mu after Alors','insertion','L08, after Alors',r'\mu','handwriting')
inv(515,'mu after donc de','insertion','L08, before et',r'\mu','handwriting')
inv(565,'nu and mu in normalizer clause','insertion','L09, after si and after de',r'\nu; \mu','handwriting')
inv(571,'extension question','margin note','right margin, beside display','Quelle extension de (Z/hZ]* par Z/hZ obtient-on ?','handwriting')
inv(628,'normalizer homomorphism','display','center, L10',r'\unsure{\psi|\nu}/\mu\longrightarrow\operatorname{Aut}(\mu)\simeq(\underline{Z}/h\underline{Z})^*','typewriting and handwriting')
inv(701,'overprint in un','deletion','L11, est un isomorphisme',r'u\deleted{j}n')
inv(759,'exchange note','margin note','left margin, below rule',r'\unsure{échanger|échange} avec cor.\unsure{3|?}','handwriting')
inv(769,'membership in conjugacy clause','insertion','L12, between w and W',r'\in','handwriting')
inv(781,'mu after mod','insertion','end L12',r'\mu','handwriting')
inv(820,'extra f in effet','insertion','L13, raised second f',r'ef\inserted{\handwritten{f}}et','handwriting')
inv(824,'replacement le sous-espace','insertion','above L13 canceled phrase','le sous-espace','typewriting; pen leader')
inv(831,'proof of first corollary','text','L13-L22','Soit en effet D')
inv(835,'overprint in en','deletion','L13, after Soit',r'\deleted{\unsure{D|B}}en')
inv(842,'canceled une droite','deletion','L13, beneath le sous-espace',r'\deleted{\unsure{une droite}}')
inv(912,'centralizer sign and mu','insertion','L14',r'\mathfrak{z}=\operatorname{Centr}(\mu)','typewritten z amended by pen; handwritten mu')
inv(969,'centralizer map and star','insertion','L15',r'\mathfrak{z}\to\operatorname{Aut}(D)=\underline{C}^{*}','typewriting and handwriting')
inv(1031,'raised star and mu','insertion','L16',r'\underline{C}^{*};\mu','handwriting')
inv(1171,'retraction','insertion','L18',r'\mathfrak{z}\to\mu','typewriting and handwriting')
inv(1235,'induit','deletion','L19, before centralise','induit','typewriting canceled with typed x strokes')
inv(1303,'overprint in On','deletion','L20',r'\deleted{\unsure{B}}On')
inv(1308,'centralizer equality','insertion','L20',r'\mathfrak{z}=\mu','typewriting and handwriting')
inv(1494,'second corollary','text','L23-L25','Corollaire. Soit c un élément de Coxeter')
inv(1495,'overprinted heading letters','deletion','L23, in Corollaire',r'Coroll\deleted{b}a\deleted{\unsure{j|l}}ire')
inv(1498,'lambda in statement','insertion','L23, after et',r'\lambda','handwriting')
inv(1512,'left rule beside second corollary','drawing','left margin L23-L25','vertical rule','handwriting')
inv(1625,'lambda repeated','insertion','L25, after que',r'\lambda','handwriting')
inv(1694,'proof of second corollary','text','L26-L28','La suffisance a déjà été énoncée')
inv(1757,'inequality in proof','insertion','L27, between h-prime and h',r'\leq','handwriting')
inv(1871,'canceled top start','deletion','L29, highest of three overlapping baselines',r'\deleted{\unsure{Considérons}}')
inv(1885,'live replacement start','insertion','L29, middle of three baselines','Soit D une','typewriting')
inv(1898,'third corollary begins','text','L29, final principal baseline','Corollaire. droite régulières dans V tensor C')
inv(1901,'canceled baseline start','deletion','L29, lowest of three overlapping baselines','Soit D une','typewriting canceled with typed x strokes and pen line')
inv(2062,'archive number','margin note','bottom left','1 (archive sheet number; comment only)','handwriting')

# Neutral IDs; bounding rectangles are in the 1672 by 2144 original image.
B=[]
def bx(id,kind,rect,reading):B.append(dict(box=id,kind=kind,x0=rect[0],y0=rect[1],x1=rect[2],y1=rect[3],reading=reading))
bx('b01','insertion',(1383,54,1627,168),r'\inserted{\handwritten{irréductible}}; oval with leader before (Kostant)')
bx('b02','margin note',(460,151,1463,196),'The principal 3-dimensional subgroup .... th. 9.2.')
bx('b03','deletion',(1164,195,1231,232),r'\deleted{\unsure{di}}est')
bx('b04','text',(220,308,1649,405),r'… donc d\'ordre $\handwritten{\leq}h$. Pour qu\'il y en ait une qui soit d\'ordre $h$, il faut et suffit que $w$ soit une transformation de Coxeter, et\inserted{alors} les éléments non nuls')
bx('b05','insertion',(30,411,181,490),r'\inserted{\handwritten{(qui est de dim $1$)}}')
bx('b06','insertion',(225,436,566,480),r'\uline{Corollaire}\handwritten{1}: Soit $\handwritten{\mu}$')
bx('b07','insertion',(401,495,561,552),r'$\handwritten{\mu\simeq}\underline{Z}\handwritten{/}h\underline{Z}$')
bx('b08','display',(618,618,1084,685),r'$\handwritten{\unsure{\psi|\nu}/\mu\longrightarrow}\operatorname{Aut}(\handwritten{\mu})\handwritten{\simeq}(\underline{Z}/h\underline{Z})^{\handwritten{*}}$')
bx('b09','margin note',(1313,563,1648,689),r'\margin{\handwritten{Quelle extension de $(\unsure{Z|\mathbb{Z}}/hZ]^*$ par $Z/hZ$ obtient-on ?}}')
bx('b10','deletion',(294,696,343,735),r'u\deleted{j}n')
bx('b11','margin note',(31,751,176,869),r'\margin{\handwritten{\unsure{échanger|échange} avec cor.\unsure{3|?}}}')
bx('b12','deletion',(327,816,954,874),r'Soit \deleted{\unsure{D|B}}en ef\inserted{\handwritten{f}}et $D$ \deleted{\unsure{une droite}}\inserted{le sous-espace} propre')
bx('b13','insertion',(1177,904,1411,958),r'$\handwritten{\mathfrak{z}}=\operatorname{Centr}(\handwritten{\mu})$')
bx('b14','insertion',(692,958,942,1015),r'$\handwritten{\mathfrak{z}\to}\operatorname{Aut}(D)=\underline{C}^{\handwritten{*}}$')
bx('b15','insertion',(363,1019,413,1071),r'$\underline{C}^{\handwritten{*}}$')
bx('b16','insertion',(416,1167,505,1211),r'$\handwritten{\mathfrak{z}\to\mu}$')
bx('b17','deletion',(548,1227,670,1269),r'\deleted{induit}')
bx('b18','text',(992,1229,1091,1268),r'\unsure{qômme|qomme}')
bx('b19','deletion',(731,1293,785,1339),r'\deleted{\unsure{B}}On')
bx('b20','insertion',(1045,1296,1168,1341),r'$\handwritten{\mathfrak{z}}=\handwritten{\mu}$')
bx('b21','deletion',(215,1485,422,1537),r'\uline{Coroll\deleted{b}a\deleted{\unsure{j|l}}ire}.')
bx('b22','insertion',(273,1618,316,1659),r'$\handwritten{\lambda}$')
bx('b23','insertion',(378,1744,478,1801),r'$h\prime\handwritten{\leq}h$')
bx('b24','deletion',(450,1866,683,1927),r'\deleted{\unsure{Considérons}} \deleted{Soit $D$ une}\inserted{Soit $D$ une}')
bx('b25','text',(655,1884,1130,1935),r'droite régulières dans $V\otimes\underline{C}$')
bx('b26','display',(718,746,884,803),r'$wcw^{-1}=c^h$')
bx('b27','margin note',(38,2054,67,2110),'% archive sheet number: 1')
bx('b28','insertion',(489,191,571,229),r'$w\handwritten{\in}W$')
bx('b29','insertion',(275,558,309,602),r'$\handwritten{\nu}$')
bx('b30','insertion',(752,564,793,607),r'$\handwritten{\mu}$')
bx('b31','insertion',(1497,506,1540,554),r'$\handwritten{\mu}$')
bx('b32','insertion',(1322,775,1363,815),r'$\handwritten{\mu}$')
bx('b33','insertion',(1046,1034,1089,1080),r'$\handwritten{\mu}$')
bx('b34','insertion',(695,505,739,552),r'$\handwritten{\mu}$')
bx('b35','insertion',(465,764,547,805),r'$w\handwritten{\in}W$')
bx('b36','drawing',(1608,195,1655,457),r'\figure{\begin{tikzpicture}\draw (-.16,.05)--(0,0)--(0,-2.05)--(-.16,-2.08);\end{tikzpicture}}')
bx('b37','drawing',(194,466,226,802),r'\figure{\begin{tikzpicture}\draw (0,0)--(0,-2.4);\end{tikzpicture}}')
bx('b38','drawing',(181,1498,217,1656),r'\figure{\begin{tikzpicture}\draw (.05,0)--(0,-.15)--(0,-1.05);\end{tikzpicture}}')
bx('b39','drawing',(871,406,902,447),'small circle below baseline after correspondant, with a rising diagonal leader')
bx('b40','insertion',(1024,1483,1066,1532),r'$\handwritten{\lambda}$')

notes=[
 'Main baseline numbering: L01 title; L02-L06 statement a); L07-L09 first corollary before display; L10 display; L11-L12 first-corollary continuation; L13-L22 its proof; L23-L25 next corollary; L26-L28 its proof; L29 final corollary fragment. There are 29 principal typed/display baselines, plus the separately inventoried marginal and interlinear writing.',
 'Whole image was inspected once for layout, then each provided half once line by line against both C and H; all 38 saved crops were displayed. One still-unresolved heading crop was tightened in place. No OCR, recognition library, web source, or TeX compilation was used.',
 'The sheet is upright. No author page number appears at the head. The lower-left 1 is treated as an archive sheet number, retained only in a comment.',
 'The English bibliographic note is source handwriting. No article was consulted. Its ellipsis is rendered as the visible sequence of dots rather than expanded text.',
 'The interlinear alors and le sous-espace are typed, with handwritten leaders. H’s editorial notes call them ink additions; this description was not imported as source wording.',
 'prop.30 is typewritten; the C handwritten wrapper on 30 was dropped as a non-substantive medium annotation change.',
 'c^h in wcw^{-1}=c^h is exactly typed. The following argument uses n and later c^n; this inconsistency caused a visual relook of the entire formula, not a correction.',
 'The handwritten centralizer notation is made by appending a lower loop/tail to a typed z, all four occurrences. It is transcribed as mathfrak z; the component-level handwriting history is described here rather than splitting one glyph into unrelated TeX characters.',
 'The visible typed slips qômme/qomme, régulière (in the earlier proof), and régulières (at bottom) are not normalized. No omitted article or agreement correction was supplied.',
 'Two canceled starts and one live inserted start occur at bottom. Their lexical sequence in the draft follows C’s arrangement, with both deletion states and the distinct live insertion retained; the inventory records their actual vertical placement.',
 'The oval, insertion leaders, and three marginal rules are annotation marks. The three rule/oval TikZ approximations from C are retained; locations are explicitly noted. No mathematical diagram or pictorial drawing is present.',
 'Some ordinary typewritten characters are overprinted rather than merely hard to read. Where an underlying character has not been securely identified, the proposed deletion is marked unsure. These new substrate readings require adjudication from their crops.',
 'No statement has been proved or disproved in this reading. All check events below are visual transcription checks only.'
]
checks=[
 dict(statement_id='C123-01_123_scan002:a',type='used and rechecked in this run',outcome='visual transcription check only: statement, h-bound, and two insertions were checked against ink; missing second il confirmed.'),
 dict(statement_id='C123-01_123_scan002:cor1',type='used and rechecked in this run',outcome='visual transcription check only: entire displayed homomorphism checked; numerator psi/nu remains doubtful; wcw^{-1}=c^h retained despite later n.'),
 dict(statement_id='C123-01_123_scan002:proof1',type='used and rechecked in this run',outcome='visual transcription check only: all four centralizer signs and all deleted/inserted spans checked; no mathematical proof claim.'),
 dict(statement_id='C123-01_123_scan002:cor2',type='used and rechecked in this run',outcome='visual transcription check only: two lambdas, h-prime exponents, inequality, and overprinted heading inspected; no proof claim.'),
 dict(statement_id='C123-01_123_scan002:cor3_fragment',type='used and rechecked in this run',outcome='visual transcription check only: three start baselines, final s, tensor sign, and page-end fragment inspected.')
]
notation=[
 'Typewritten Z and C with separate baseline underscores are rendered as underline{Z} and underline{C}; not bold and not mechanically doubled capitals.',
 'The centralizer glyph is a typed z augmented below by a handwritten loop or tail; render mathfrak{z} (four occurrences on this page).',
 'A star added by hand at upper right denotes the visible superscript *; no normalization to another notation.',
 'Tensor sign at bottom is mechanically formed by overtyping rounded O and x; rendered otimes and its keyed construction recorded here.',
 'Handwritten Z versus double-struck Z in the right marginal question remains ambiguous; candidates are Z and mathbb{Z}. Mark once at its first occurrence on this page, then use first candidate Z.',
 'Source abbreviations retained: dim (without period in the inserted note), th., cor., prop., mod, cqfd.'
]
handlog=[
 'Cote 123 scan 2: mu has a long left descender and a shallow central valley; visually confirmed in every handwritten mu on this page. Nu in the normalizer sentence is a plain v-shaped two-stroke glyph. The heavy numerator of the display is different enough that psi/nu is left open.',
 'Cote 123 scan 2: centralizer signs are not plain handwritten z: the z is typed and a broad lower loop is added by pen. This occurs at every one of the four centralizer signs. C read plain z at all four; H read mathfrak z.',
 'Cote 123 scan 2: a handwritten f in effet rises far above the baseline; it should not be silently merged with the typescript. No global u/f-to-n swap was securely found on this page.',
 'Cote 123 scan 2: retraced or overlapped typewriter characters can look like spelling errors without showing their layers. Distinct underlying candidates are preserved in est, un, en, On, and the second Corollaire heading; uncertain layers stay uncertain.',
 'Cote 123 scan 2: source 1 has a sloping head and continuous upright, confirmed in the inserted Corollaire 1 and dimensional note; C’s 1/! ambiguity in the heading is resolved. Terminal 3/? in the exchange note remains open.'
]
report=dict(page=P,line_count=29,changes=changes,doubts=D,inventory=[d for _,d in sorted(I,key=lambda a:a[0])],notes=notes,check_events=checks,notation=notation,hand_log=handlog,boxes=B)
path=R/'out/work'/f'{P}_report.json';path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(path, 'changes=',len(changes),'inventory=',len(I),'boxes=',len(B))
