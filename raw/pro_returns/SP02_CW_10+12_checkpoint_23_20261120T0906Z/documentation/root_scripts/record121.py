from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,121);ch=r.change
r.edit(r'\scanpage{121}',r'\scanpage{121}'+'\n'+r'\mspage{120}')
r.edit('% archive sheet number: 120','')
guide=r'\handwritten{\begin{tikzpicture}[x=.55cm,y=.55cm,baseline=-.2ex]\draw (0,-.23) .. controls (.04,-.04) and (.14,.05) .. (.38,.05)--(1.8,.06) .. controls (2,.07) and (2.12,.2) .. (2.12,.42);\end{tikzpicture}}'
for s in ['(continues)','(associative, unitaire)','topologique','bilinaire']:
 r.edit('\\inserted{'+s+'}','\\inserted{'+s+guide+'}')
r.edit(r"d'un foncteur $\otimes$",r"d'un foncteur $\unsure{\otimes|\Omega}$")
r.edit(r'F(Y)$)',r'F(Y)$\handwritten{)}')
une=r'\unsure{\rlap{\begin{tikzpicture}[x=1em,y=1em,baseline=0pt]\draw[line width=1pt] (.7,.73)--(1.03,.73);\draw[line width=1pt] (.85,.72)--(.85,.95);\fill (1.15,.72)--(1.29,.72)--(1.28,.99)--(1.22,.91)--(1.14,.94)--cycle;\end{tikzpicture}}Une|Une}'
r.edit('Une donnée supplémentaire',une+' donnée supplémentaire')
r.edit(r'\unsure{\epsilon|\varepsilon}',r'\unsure{\epsilon|e}')
r.edit('si elle existe.',r'si elle existe.\handwritten{\llap{\raisebox{-.65ex}{,}}}')
cguide=r'\handwritten{\begin{tikzpicture}[x=.55cm,y=.55cm,baseline=-.2ex]\draw (-.15,-.3) .. controls (.02,.06) and (.16,.1) .. (.45,.08)--(2.45,.02);\draw (2.5,.03) .. controls (2.58,-.18) and (2.62,-.24) .. (2.78,-.24);\end{tikzpicture}}'
r.edit(r'\unsure{et que ce soit}}}}',r'\unsure{et que ce soit}}}'+cguide+'}')
sep=r'\unsure{\rlap{\handwritten{\begin{tikzpicture}[x=1em,y=1em,baseline=0pt]\draw[line width=.6pt] (.48,.9) .. controls (.24,.55) and (.28,.15) .. (.22,-.18);\draw[line width=.6pt] (.22,-.18) .. controls (.37,.15) and (.64,.35) .. (.82,.53);\end{tikzpicture}}}x|\deleted{x}\handwritten{/}}'
r.edit(r'\handwritten{\unsure{,|/}}',sep)
r.edit('transformé',r'tra\rlap{e}nsformé')
cg=r'\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,-.35) .. controls (.02,-.04) and (.08,.1) .. (.3,.14)--(.7,.16) .. controls (.88,.18) and (.94,.32) .. (.95,.58);\end{tikzpicture}'
r.edit(r'\inserted{\handwritten{$c$}}',r'\inserted{\handwritten{$c$'+cg+'}}')
r.edit('les multiplications',r'les mu\rlap{\handwritten{l}}t\rlap{\handwritten{t}}liplications')
r.edit(r'supplémentaires a) \deleted{b)}',r'supplémentaires a)\deleted{, b)}')
r.edit('il faut imposer compatibilité',r'il faut \unsure{imposer|supposer} compatibilité')
r.edit(r'\unsure{augm.|augm}','augm')
r.edit(r'Relations entre\\loi $X^\vee$',r'relations entre\\loi $\check{X}$')
r.edit(r'$(\underline{C},\otimes)$',r'$(\underline{C},\unsure{\omega|\otimes})$')
un=r'U\unsure{\rlap{\begin{tikzpicture}[x=1em,y=1em,baseline=0pt]\draw[line width=.4pt] (.05,-.05) .. controls (-.07,-.13) and (.07,-.25) .. (.2,-.08)--(.35,.04);\draw[line width=.4pt] (.2,-.08)--(.16,-.28);\draw[line width=.4pt] (.36,.01)--(.42,-.2);\end{tikzpicture}}n|n}'
r.edit('7) Un exemple.',r'7) '+un+' exemple.')
r.edit(r'gradué\unsure{ss|s}',r'gradué\deleted{\unsure{s}}s')
r.edit(r'donnée\deleted{\unsure{di}}',r'donnée\deleted{s di}')
ch('opening C','plain C','underlined C','plain C','The first C has one open curved body and no detached lower bar.','header','misread symbol or index','high',False,True,False,True)
ch('C in F arrow','plain C','underlined C','plain C','The C before the handwritten right arrow is unbarred; Modf has one M body, without a repeated outline.','F','misread symbol or index','high',False,True,False,True)
ch('C before identifies','plain C','underlined C','plain C','No horizontal underline is visible beneath this third C.','C-third','misread symbol or index','high',False,True,False,True)
ch('canceled d\'un',"deleted d'un",'deleted ill',"deleted d'un",'The d ascender, apostrophe and u/n bodies remain readable beneath the typed crosses.','dun','readable ink left as \\ill{}','high',False,True,True)
for place,crop in [('(continues)','continues'),('(associative, unitaire)','assoc'),('topologique','dual'),('bilinaire','bilinaire')]:
 ch('guide for '+place,'omitted','omitted','curved local insertion guide','A thin line joins the insertion point to the added text, running below it and turning upward at its right end. The drawing is placed beside its own insertion.',''+crop,'drawing or diagram','high',True,True)
ch('first and recurring typed tensor','otimes','otimes',r'first \unsure{\otimes|\Omega}; later first-candidate tokens','The nine recurring typed signs have an arched top, internal crossed strokes and lower feet. The first occurrence remains qualified and eight later instances use its first candidate; the handwritten signs in the lower note are judged separately.','tensor1; equality; Uhat; avecun; tensorpair; tensorfonct; tensorlast','misread symbol or index','medium',True,True,False,True)
ch('inserted bilinaire','bilinaire','bilinéaire','bilinaire','The inserted type reads b-i-l-i-n-a-i-r-e, with no e after n and no acute accent.','bilinaire','abbreviation expanded or spelling modernised')
ch('canceled c\'est',"deleted c'est",'deleted ill',"deleted c'est",'The c/e/s/t cells and raised apostrophe survive the x cancellation.','cest','readable ink left as \\ill{}','high',False,True,True)
ch('égalité emphasis','underlined','italic','underlined égalité','A separate continuous lower line underlies the upright typed word.','equality','other')
ch('outer closing parenthesis after equality','ordinary )','ordinary )','handwritten )','Beyond the typed closing parenthesis of F(Y), a thinner hand curve supplies the outer closing mark; its ends are visible at the paper edge.','formula-close','insertion or placement','high',True,True)
ch('équivaut emphasis','underlined','italic','underlined équivaut','A horizontal line runs under the upright typed word.','equiv','other')
ch('Une upper traces','plain Une','plain Une','qualified Une with upper strokes drawn','Above the U/n junction are a short vertical stroke with a horizontal foot and a separate dark upright rectangular trace. These do not settle an additional letter sequence.','Une','drawing or diagram','low',True,True)
ch('first b replacement','canceled typed b) and inserted hand b)','canceled b) only','canceled typed b) and inserted hand b)','A separate blue hand b) stands above and to the right of the crossed typed b).','abc','omission')
ch('compatible emphasis','underlined','italic','underlined compatible','The upright typed word has a separate horizontal underline.','compatible','other')
ch('canceled note opening',r'\unsure{pour b)}','pour b)',r'\unsure{pour b)} retained','The p descender, low intervening curves, tall b and closing curve survive, but the crossing line hides parts of the middle letters.','cancel-left; cancel-all','misread word','low',False,True,False)
ch('canceled note next word',r'\unsure{il}',"c'est une",r'\unsure{il} retained','A narrow upright and dot are visible under the cancellation. The longer H sequence cannot be read securely there.','cancel-left; cancel-middle','misread word','low',False,True,False)
ch('canceled unreadable group',r'\illegible{4}',r'\ill{}',r'\illegible{4} retained','The thick cancellation physically covers the central letters; four remains an approximate character count rather than a reconstruction.','cancel-middle','other','low',False,False,True)
ch('canceled que soit une',r'\unsure{que soit une}','ill',r'\unsure{que soit une} retained','The q descender and several low curves/uprights remain, but the joined group is crossed too densely for an unqualified reading.','cancel-middle; cancel-right','readable ink left as \\ill{}','low',False,True,True)
ch('first epsilon in canceled note',r'\unsure{\epsilon|\varepsilon}','e',r'\unsure{\epsilon|e}','Two open rounded lobes favor epsilon, but the cancellation obscures the middle, leaving Latin e possible. The C alternatives were glyph variants of the same Greek letter.','cancel-middle','misread symbol or index','low',True,True,False,True)
ch('canceled parenthesis hom. de k-alg',r'\unsure{hom. de $k$-alg}',"morph. d'alg.",r'\unsure{hom. de $k$-alg} retained','A tall h, low om loops and remnants of de and k-alg can be followed, but not securely throughout; the H morph. sequence is unsupported.','cancel-right; cancel-lower','misread word','low',False,True,False)
ch('canceled tail et que ce soit',r'\unsure{et que ce soit}','ill',r'\unsure{et que ce soit} retained','Low joined letter remnants remain under the lower crossing line, with no basis for removing the doubt.','cancel-lower','readable ink left as \\ill{}','low',False,True,True)
ch('punctuation after existe','period','period','period with lower handwritten comma-tail','A black baseline point has a separate smooth blue comma-tail below it, left of the insertion guide. Both visible layers are reproduced without normalizing the compound to a typed semicolon.','exists-punct','omission','high',True,True)
ch('guide of canceled insertion','omitted','omitted','curved insertion guide drawn','The long thin line rises from between existe and Elle, passes under the canceled note and ends with a detached short down-hook.','cancel-guide; cancel-all','drawing or diagram','high',True,True)
ch('punctuation after unitaire','no comma','comma','no comma','No comma body is visible on the paper after the final e before the following resp.; the edge is clipped and no missing ink is supplied.','unitaire-end','text not on the page')
ch('dash after situation','short -','em dash','short -','One short typewriter dash follows the point.','dash','other')
ch('first C prime in Si on a',r'\mathbb{C}\prime','underlined C prime',r'\mathbb{C}\prime','Offset curved contours and displaced terminal strokes show a repeated C body; the prime is a short raised stroke, not an exclamation.','Cpp','misread symbol or index','medium',False,True,False,True)
ch('canceled avec un tensor comma','readable canceled phrase','deleted ill','readable canceled phrase','The cells avec un, the crossed-arch operator and comma remain visible beneath the x row.','avecun','readable ink left as \\ill{}','high',False,True,True)
ch('G source C','plain C','underlined C','plain C','There is no lower bar under the source C in the G arrow expression.','G','misread symbol or index','high',False,True,False,True)
ch('G target C prime','plain C prime','underlined C prime','plain C prime','The target C has no separate underline; its raised mark is a prime.','G','misread symbol or index','high',False,True,False,True)
ch('C in Si C et',r'\mathbb{C}','underlined C',r'\mathbb{C}','Two offset C contours/terminal strokes are visible, rather than a separate lower bar.','Cdouble','misread symbol or index','medium',False,True,False,True)
ch('next C prime','plain C prime','underlined C prime','plain C prime','This C prime has one ordinary C body with no detached underline.','Cprime','misread symbol or index','high',False,True,False,True)
ch('pair of typed tensor signs','two with qualified hand comma/slash','one sign','two typed signs with central typed x and qualified hand crossing strokes','Between the two crossed-arch signs is a typed x with upper/lower serifs. Blue strokes cross its cell and rise toward the second sign; their cancellation status is uncertain and is retained graphically.','tensorpair; tensor-x','misread symbol or index','low',True,True,False,True)
ch('transformé overlapped n cell','transformé','transformé',r'tra\rlap{e}nsformé','The n arch and stems coexist with a rounded e body and crossbar in the same cell. Both bodies are kept without assigning revision order.','ctransform; transform-n','misread word','high',True,True)
ch('c insertion after caractériser','inserted c; typed alors','alors inserted; c omitted','inserted hand c; typed alors','The small blue c sits above the interval after caractériser; alors is ordinary baseline type. The curved guide begins at that interval.','cinsert; le','insertion or placement','high',False,True,False,True)
ch('guide for c','omitted','omitted','local curved guide drawn','A thin curved line rises from between caractériser and alors to the handwritten c.','cinsert','drawing or diagram','high',True,True)
ch('multiplications corrected cells','multiplications','multiplications',r'mu\rlap{\handwritten{l}}t\rlap{\handwritten{t}}liplications','The third typed cell has a t crossbar and foot, under a blue looped l; the next typed l has a blue t stem/bar across it. The two original type cells and the hand corrections are both retained.','multi; multi-over','insertion or placement','high',True,True)
ch('last enumeration comma','a) canceled b)','a), canceled b)','a) with comma and b) canceled','The blue strike passes through the comma after a) as well as the following b). The comma is neither omitted nor left live.','a-final; bfinal','deletion state','high',True,True)
ch('small note verb','imposer','supposer',r'\unsure{imposer|supposer}','The initial compressed strokes and following p descender do not distinguish the two readings securely. The rest of the verb remains legible.','smallnote; small1','misread word','low',True,True)
ch('small note compatibilité','compatibilité','compatible','compatibilité','The final letters form té with an acute mark after the long compatibility stem.','small1; small2','misread word')
ch('small note first aux','aux','avec','aux','The short three-letter group ends in crossed x strokes, with no intervening ve cells.','small2','misread word')
ch('small note abbreviation',r'\unsure{augm.|augm}','augment.','augm','The group ends after m; the blank interval before de contains no point. No ent letters are written.','small2','abbreviation expanded or spelling modernised','high',True,True)
ch('small note second aux','aux','avec','aux','The short group before unités has u and crossed x strokes.','small3','misread word')
ch('small note unités','unités','unité','unités','A final short s follows the accented e. The following A,A prime have a visible comma and raised prime.','small3','misread word')
ch('Dire note de plus exiger','de plus exiger','ill la cond.','de plus exiger','The separate words de plus and the e-x-i-g-e-r strokes can be followed in the rotated enlargement; no la cond. is written.','dire2; dire3; direformula','readable ink left as \\ill{}','high',False,True,True)
ch('Dire note last clause','qualified three alternatives','ill les morphismes','qualified C alternatives retained','A q descender and low joined middle/final traces overlap the neighboring line. They do not settle any complete clause; the uncertainty is retained rather than completing it from the formula.','diretail; direformula','misread word','low',False,True,True,True)
ch('Dire note hand operator after C','otimes','otimes',r'\unsure{\omega|\otimes}','This operator has open upper lobes joined at the bottom and an internal diagonal, unlike the clear circled cross in Delta(g). The omega-like form is the first qualified reading.','dire-C; direformula','misread symbol or index','low',True,True,False,True)
ch('Dire note vertical rule','drawn vertical rule','not drawn','drawn vertical rule','The blue rule stands at the left of the note, with a slight lower bend.','dire-line; dire','drawing or diagram')
ch('Relations initial case','Relations','relations','relations','The initial r is a small lower-case stroke, not a capital R.','relations-upright','misread word','high',True,False)
ch('Relations mark on X',r'X^\vee',r'\check{X}',r'\check{X}','The two short strokes forming a check sit centered directly above X, not to its upper right.','relations-upright','misread symbol or index','high',True,False,False,True)
ch('Relations antipodisme','antipodisme sur U resp. A','antipo with supplied de; données par U resp. A','antipodisme sur U resp. A','The word continues from antipo- into disme on the next line; the following word reads sur. The line-end division is joined under the stated convention.','relations; relations-upright','misread word','high',False,True,True,True)
ch('Relations surrounding drawing','irregular balloon and right leader','not drawn','irregular balloon and right leader','A long uneven curve surrounds the slanted note and meets a short horizontal leader on the right.','relations','drawing or diagram')
ch('Un exemple emphasis','plain type','italic','plain type','The heading is upright type without underline or other emphasis mark.','title7','other')
ch('Un lower traces','plain Un','plain Un','qualified n with lower strokes drawn','Below the n are a small loop, an ascending diagonal and two downward legs. These are retained without asserting a second repeated n.','Un; Un-lower','drawing or diagram','low',True,True)
ch('example category C','plain C','underlined C','plain C','The C in pour C has no separate lower bar.','title7','misread symbol or index','high',False,True,False,True)
ch('gradués ending',r'gradué\unsure{ss|s}','gradués',r'gradué\deleted{\unsure{s}}s','Two cells follow é: the first has an underlying curved letter crossed by x, and the second is a clear live s. Cancellation is clear; the first underlying s remains qualified.','gradues; gradues-end','deletion state','medium',True,True)
ch('first k in example',r'\mathbb{k}','k',r'\mathbb{k}','Two displaced upright/arm contours are visible in the typewritten k.','k1','misread symbol or index','high',False,True,False,True)
ch('k subscript s in example',r'\mathbb{k}_s','k subscript s',r'\mathbb{k}_s','The k has repeated offset contours; the lower small subscript is s.','ks','misread symbol or index','high',False,True,False,True)
ch('donnée canceled ending',r'donnée\deleted{\unsure{di}}','données',r'donnée\deleted{s di}','A canceled s follows donnée, then the crossed d ascender/oval and dotted i. The di reading is settled, and the canceled s is restored.','donneedel','deletion state','high',True,True)
ch('hand commutativity sign',r'\unsure{\mu|\psi}','psi',r'\unsure{\mu|\psi} retained','Two joined low legs and a long through-stroke remain compatible with mu or psi.','mu','misread symbol or index','medium',False,True,False,True)
ch('estnun','estnun','est un','estnun','Six successive cells read e-s-t-n-u-n; the first n is faint but has an arch and stems. It is not a word space.','estnun','abbreviation expanded or spelling modernised')
ch('folio','comment120','administrative page120','mspage120','Three pencil figures at lower left read120.','folio','insertion or placement','high',True,True)
for args in [
 ('first recurring typed tensor',r'\otimes',r'\Omega','medium','Crossed arch with lower feet; later typed instances take the first candidate.'),
 ('Une upper traces','Une with upper strokes drawn','unidentified additional typed traces','low','An upper T-like mark and separate block do not settle extra letters.'),
 ('canceled note opening','pour b)','','low','Cancellation obscures middle letters.'),
 ('canceled note next word','il',"c'est une",'low','Only a narrow upright/dot and adjoining covered remnants are visible.'),
 ('canceled group','approximately four illegible characters','','low','Physically covered by the thick strike.'),
 ('canceled note middle','que soit une','','low','Several descenders/uprights survive; joined letters remain covered.'),
 ('first epsilon in canceled note',r'\epsilon','e','low','Two lobes favor epsilon, but the middle is covered.'),
 ('canceled algebra parenthesis','hom. de k-alg',"morph. d'alg.",'low','Partial ascenders/loops survive under the line.'),
 ('canceled note tail','et que ce soit','','low','Low traces overlap the cancellation.'),
 ('separator of typed tensors','typed x with hand crossing strokes drawn','canceled x; slash-like hand stroke','low','The typed x is clear; the role of the blue crossing strokes is unresolved.'),
 ('small note verb','imposer','supposer','low','The compressed initial cluster does not distinguish the readings.'),
 ('Dire note operator after C',r'\omega',r'\otimes','low','Open upper lobes and a lower join differ from the other hand circled cross.'),
 ('Dire note final clause','qui implique unitaire','qui sont les morphismes; qui implique un morphisme','low','The joined clause overlaps the next line; no alternative is settled.'),
 ('Un lower traces','n with lower strokes drawn','unidentified overlapping or corrective marks','low','The separate lower loop and legs do not settle a second n.'),
 ('gradués canceled ending','s beneath cancellation','','medium','Cancellation is certain, but the curved underlying letter is partially obscured.'),
 ('hand commutativity sign',r'\mu',r'\psi','medium','Joined legs and through-stroke remain ambiguous.')]:r.doubt(*args)
r.notation('typed tensor sign','crossed arch with lower feet; first tensor/Omega qualified, eight later first-candidate tokens','10/121','unresolved')
r.notation('hand tensor and omega-like forms','clear circled cross in Delta(g); separate open omega-like operator after C qualified omega/tensor','10/121','partly unresolved')
r.notation('epsilon in canceled note','first epsilon/e qualified; later epsilon first candidate; lower note epsilon has clear open lobes','10/121','partly unresolved')
r.notation('repeated type','two middle C forms and two example k forms have offset repeated contours, rendered mathbb','10/121')
r.notation('physical overlaps','e/n in transformé; handwritten l/t over typed t/l in multiplications; unidentified upper Une and lower Un traces drawn','10/121','partly unresolved')
r.notation('hand commutor','mu/psi qualified','10/121','unresolved')
r.notation('dual-operation mark','centered check above X in rotated Relations note','10/121')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/121') for a,b in [('sss','si et seulement si'),('hom.','homomorphisme(s)'),('top','topologique(s)'),('resp.','respectivement'),('augm','augmentations'),('endom.','endomorphismes')]]
r.r['inventory_overrides']={
 '006':{'first_words_or_objects':'(continues) with local curved guide'},
 '007':{'first_words_or_objects':'(associative, unitaire) with local curved guide'},
 '008':{'first_words_or_objects':'topologique with local curved guide'},
 '009':{'first_words_or_objects':'bilinaire with local curved guide'},
 '016':{'first_words_or_objects':'canceled hand note pour b) ... epsilon/e ...; doubts retained and insertion guide drawn'},
 '017':{'first_words_or_objects':'same canceled handwritten note; Greek epsilon/Latin e qualified'},
 '018':{'first_words_or_objects':'same full handwritten note crossed by long lines'},
 '026':{'first_words_or_objects':'typed x between two tensor signs, with qualified handwritten crossing strokes'},
 '028':{'first_words_or_objects':'c inserted after caractériser, with curved guide'},
 '029':{'first_words_or_objects':'hand c and insertion guide; alors remains baseline type'},
 '032':{'first_words_or_objects':'comma and b) canceled after final a)'},
 '033':{'first_words_or_objects':'pour b) il faut qualified imposer/supposer compatibilité aux augm de U resp. aux unités de A,A prime'},
 '034':{'first_words_or_objects':'same small note; augm without point, unités plural'},
 '038':{'first_words_or_objects':'relations entre loi check-X et antipodisme sur U resp. A'},
 '040':{'first_words_or_objects':'Dire que les endom. ... clear first circled cross, qualified omega/tensor after C, qualified final clause'},
 '041':{'first_words_or_objects':'7) Un with lower traces; example with gradué canceled-s s; doubled k and k_s; donnée canceled s di; estnun'},
 '042':{'first_words_or_objects':'s di, all canceled after donnée; di readable'}}
extras=[('guide-continues','after canceled d\'un','curved guide for (continues)','drawing','his hand'),('guide-assoc','after k','curved guide for (associative, unitaire)','drawing','his hand'),('guide-top','after dual','curved guide for topologique','drawing','his hand'),('guide-bil','after first tensor sign','curved guide for bilinaire','drawing','his hand'),('formula-close','right edge of equality line','hand outer closing parenthesis','insertion','his hand'),('Une-traces','above Une','qualified upper T-like and block traces','drawing','typewriter'),('existe-comma','below point after existe','lower handwritten comma-tail','insertion','his hand'),('cancel-guide','under canceled long note','long curved insertion guide with right hook','drawing','his hand'),('c-guide','after caractériser','curved insertion guide for c','drawing','his hand'),('multi-correction','third and fourth cells of multiplications','hand l/t over typed t/l','insertion','his hand'),('Un-traces','below n in Un exemple','qualified lower loop and legs','drawing','unnamed hand'),('gradues-delete','after gradué','canceled qualified s before live s','deletion','typewriter'),('folio','lower left','120','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:121',sheet_kind='typescript',hand=hand,element='121-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops121.json').read_text())
r.r['inspection_note']='Root viewed whole121 then both halves, C/H, all13 C uncertainty fields and44 C inventory elements. All89 crops were viewed, including upright rotations of the canceled and lower/slanted notes. The initially truncated le/cinsert/Udiag/Adiag images were repeated successfully. Original margin-type and epsilon crops were supplemented by correctly framed full/epsilon-correct crops. A later optional Une/cancel-left redo was output-truncated; both had already been viewed and were then viewed individually again. Every agreed word, symbol, prime, index, underline, deletion and insertion was checked in ink. No OCR, parallel transcription, context, compilation or mathematical checking. No122 image opened before finalization.'
r.save('work/record121.json')
