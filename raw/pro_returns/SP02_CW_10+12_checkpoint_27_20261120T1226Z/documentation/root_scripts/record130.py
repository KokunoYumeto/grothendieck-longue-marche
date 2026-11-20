from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,130);ch=r.change
mono=r'\unsure{\(\mathbb m\)|\rlap{a}m|\rlap{u}m}onoïde'
duale=r'd\unsure{\rlap{a}u|u|a}ale'
MX=r'\unsure{\rlap{\(M\)}X|\mathbb M|\mathbb X}'
mx=r'\rlap{\(M\)}X'
le=r"l\unsure{\rlap{'}e|é|e}"
cat=r'\unsure{\rlap{c}C|\(\mathbb C\)|C|c}atégorie'
label=r'\rlap{\(x\)}-'
firstlabel=r'\unsure{'+label+r'|*}'
iso=r'iso\unsure{\rlap{m}M|M|m}.'
guide=r'\handwritten{\begin{tikzpicture}[x=.2cm,y=.2cm,baseline=-.1ex]\draw (0,-.5) .. controls (.2,.1) and (1,.2) .. (1.5,.8);\end{tikzpicture}}'
rule=r'\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.03) .. controls (3,.09) and (6,-.02) .. (8,0) .. controls (11,.03) and (13,.01) .. (15,.06);\end{tikzpicture}}'
r.edit('un monoïde fini','un '+mono+' fini')
r.edit(r'\unsure{duale|daale}',duale)
r.edit(r'\unsure{\mathbb{M}|\mathbb{X}}',MX)
r.edit(r'\unsure{lé|le}',le)
r.edit(r"X_{g'}\otimes Y_{g''}",r"X_{g'}\unsure{\otimes|\Omega} Y_{g''}")
r.edit(r'\mathbb{M}',mx,count=2)
r.edit(r'\unsure{Catégorie|catégorie}',cat)
r.edit(r'$\handwritten{\psi}$',r'$\handwritten{\unsure{\psi|\mu}}$')
r.edit(r'$\vee$',r'$\handwritten{\vee}$')
r.edit(r'\['+'\n'+r"\deleted{M}\handwritten{L}_{gg'}",r'\['+'\n'+r'('+firstlabel+r')\qquad '+r"\deleted{M}\handwritten{L}_{gg'}")
r.edit('\n'+r'\tag*{(*)}','')
r.edit(r'\unsure{(**)|(*+)}',r'\unsure{(*+)|(**)}')
r.edit(r'\inserted{\handwritten{\unsure{(*+)|(**)}}}',r'\inserted{\handwritten{\unsure{(*+)|(**)}}}'+guide)
r.edit('qui rendre',r'qui rend\deleted{r}e')
r.edit('isomorphismes (*)',r'isomorphismes $('+label+r')$',count=2)
r.edit(r'\deleted{\unsure{ceux-ci}}',r'\deleted{ceux-ci}')
r.edit(r'\deleted{\unsure{conditio}}',r'\deleted{conditio}')
r.edit(r'\unsure{isoM.|isom.}',iso)
r.edit(r'\deleted{\unsure{sinon $N$|sinon $M$}}',r'\deleted{sinon $M$}')
r.edit(r'p^{\handwritten{2}}',r'p^2')
r.edit(r'isomorphismes $*$',r'isomorphismes $'+label+'$')
r.edit('% bottom margin, below a handwritten separating rule','% bottom margin, below a handwritten separating rule\n'+rule)
# C uncertainties and differences from H, decided from root-only enlarged ink views.
ch('top ambiguous capital',r'\unsure{\mathbb E|\mathbb F|E|F}','F',r'\unsure{\mathbb E|\mathbb F|E|F}','An upright, protruding middle bar and low rightward trace coexist with dense overlapping ink. Neither E/F nor single/double construction is secure; C alternatives remain. Ordinary F-prime and the E of Exemple were separately enlarged as comparators.','topF; Fprime; Exemple','misread symbol or index','low',False,True,False,True)
for place,crop in [('opening dash','topdash'),('dash before Le foncteur','maindash')]:
 ch(place,'short typewriter hyphen','em dash','short typewriter hyphen','The ink is a single short horizontal strike of one typewriter cell width.',crop,'other')
ch('base-field subscript',r'k_x','k',r'k_x','A small x has its crossing below the k baseline; it is a separate lower index.','kx','omission','high',False,True,False,True)
ch('vraie final addition',r'vrai\handwritten{e}','vraie',r'vrai\handwritten{e}','The final e is written by hand between the typed i and closing parenthesis, rather than being an original typed character.','vraie','insertion or placement')
ch('section12 heading and paragraph','12. underlined Exemples instructifs. Soit G ...','separate subsection followed by new paragraph','12. underlined Exemples instructifs. Soit G ...','The underline stops before the period, and Soit G follows on the same typed line without a new paragraph.','heading; SoitG','insertion or placement')
ch('monoïde first cell','m','m',mono,'The initial cell has two upper arches together with extra lower enclosed contours and a middle horizontal trace. Double m is favored over unlike a/m or u/m overlap; weight alone is not the evidence. The diaeresis has two dots.','monoide; mono_initial','misread word','medium',True,True)
ch('canceled a before application',r"l\deleted{a}'application","l'application",r"l\deleted{a}'application",'A typed a bowl remains under the x strike before the live apostrophe.','lapp','deletion state')
ch('multiplication source',r'GxG',r'G\times G',r'GxG','The central glyph is a typewriter x with serifed diagonal ends; the following arrow is a hand stroke.','GxG','misread symbol or index','high',False,True,False,True)
ch('duale second cell',r'\unsure{duale|daale}','duale',duale,'The second cell combines a lower u-like cup with an a-like closed upper/bowl contour. The raw overlap is favored, while single u or a remains possible.','duale','misread word','medium',True,True)
for word,crop in [('duale','duale'),('famille de Dirac','dirac')]:
 ch('quotation marks around '+word,'double quotation marks','guillemets','double quotation marks','Paired short upright quotation strokes occur on both sides, rather than angular guillemets.',crop,'other')
ch('category C','C','underlined C','C','The typed C is an open curved body without a separate lower rule.','C','misread symbol or index','high',False,True,False,True)
ch('canceled est',r'G\deleted{est} peut','G peut',r'G\deleted{est} peut','The e, s and t remain visible beneath the cancellation between G and peut.','Gcancel','deletion state')
ch('family symbol first occurrence',r'\unsure{\mathbb M|\mathbb X}','X',MX,'The cell combines two M-like outer uprights and middle structure with X-like crossing diagonals. It is retained as unlike-letter overlap first, with double-letter alternatives. Both later Dirac-family cells were separately enlarged and have the same construction.','fam; units','misread symbol or index','medium',True,True,False,True)
ch('family lower index',r'g\ G',r'g\in G',r'g\ G','There is a blank interval between the lower g and G; no membership sign is visible.','fam','text not on the page','high',False,True,False,True)
ch('live article before canceled phrase',r'\unsure{lé|le}',r"\struck{l'application diagonale}",le+r'\deleted{application diagonale}','A live l precedes an e-like body with an upper apostrophe-like stroke. The following application diagonale is canceled, but this article is not crossed through.','lecancel','deletion state','medium',True,True)
ch('product phrase order',r'canceled application diagonale, produit, inserted tens.',r'produit, inserted tens., canceled application diagonale',r'canceled application diagonale, produit, inserted tens.','The canceled phrase stands before produit; tens. is typed interline above the end of produit.','lecancel; tens','insertion or placement')
ch('convolution formula placement','inline','display','inline','The Z formula follows défini par on the same typed baseline and ends before the next sentence.','XYZ; sum','insertion or placement')
ch('seven typed tensor-like signs',r'\otimes',r'\otimes',r'first \unsure{\otimes|\Omega}; six later \otimes','Every typed sign was enlarged. Their rounded upper outline, internal crossing and flat lower foot permit an Omega-like alternative. Only the first occurrence carries the doubt; the hand signs below were inspected separately.','sum; catsymbols; Lformula; Uformula; display; tensor1; tensor2','misread symbol or index','medium',True,True,False,True)
ch('two Dirac family symbols',r'\mathbb M_g; \mathbb M_e',r'X_g; X_e',mx+r'_g; '+mx+r'_e','Both cells show the same M uprights and X diagonals as the first family symbol. They use the first chosen form without repeating the doubt.','units; fam','misread symbol or index','medium',True,True,False,True)
ch('unit element after inequality',r'\mathbb e','e',r'\mathbb e','Two vertically offset e contours and middle-bar traces are visible in the cell after the hand inequality. The subscript e at the next family symbol is single.','units','misread symbol or index','high',False,True,False,True)
ch('inserted Catégorie first cell',r'\unsure{Catégorie|catégorie}','catégorie',cat,'The cell has a tall C-shaped outer curve and a shorter inner c-like curve. Mixed-case overlap is favored; double capital C and either single case remain alternatives. The acute accent on é is visible at the edge.','Cat; cat_initial; catsymbols','misread word','medium',True,True)
ch('extent of On a une insertion','entire On a une ... un groupe. inserted','only un groupe inserted','entire On a une ... un groupe. inserted','The whole passage is interlinear, beginning at the end of the previous line and continuing above the following paragraph.','Cat; catsymbols; psi; Gcomm; vee; Gend; ungroupe','insertion or placement')
ch('three symmetry signs',r'\psi',r'\psi',r'first \handwritten{\unsure{\psi|\mu}}; two later psi','The first sign combines a cup-shaped body and a descending oblique stroke. Psi is favored, but a mu-like construction remains possible. Both later signs in the phi/psi pairs were separately enlarged and follow the first reading.','psi; phipsi1; phipsi2','misread symbol or index','medium',True,True,False,True)
ch('duality sign baseline and hand',r'\vee',r'{}^\vee',r'\handwritten{\vee}','The V-shaped hand stroke stands at the sentence baseline after un, not as an exponent.','vee','misread symbol or index','high',True,True,False,True)
ch('Un L paragraph','new paragraph','continuous with group insertion','new paragraph','Un L starts an indented main-text line below the inserted un groupe ending.','ungroupe; UnL','insertion or placement')
ch('tensor in U formula',r'\otimes_k',r'\widehat\otimes_k',r'\otimes_k','There is no independent hat above this operator; the upper ink is its own rounded contour.','Uformula','text not on the page','high',False,True,False,True)
ch('family parameter M to L',r'\deleted M\handwritten L_g',r'M_g',r'\deleted M\handwritten L_g','A hand L replaces the typed M in the indexed family. The membership sign is separately inserted by hand.','family2','deletion state','high',False,True,False,True)
ch('four typed reference marks','asterisks','asterisks',r'first '+firstlabel+r'; later '+label,'All four marks combine a typed x with a horizontal middle stroke. No additional upright makes a plus. The first carries an asterisk alternative; later instances retain the same constructed form.','displaylabel; inlineaster1_full; inlineaster2_full; aster','misread symbol or index','medium',True,True,False,True)
ch('display reference position','right tag','left label','left label','The parenthesized mark lies in the left text margin, well to the left of the displayed formula.','displaylabel; display','insertion or placement','high',True,False)
ch('three display M to L corrections',r'\deleted M\handwritten L',r'M',r'\deleted M\handwritten L','Each of the three indexed symbols has a typed M with a distinct hand L correction. The hand isomorphism sign, indices gg-prime/g/g-prime and final period are visible.','display','deletion state','high',False,True,False,True)
ch('margin M to L correction',r'\deleted M\handwritten L_g',r'M_g',r'\deleted M\handwritten L_g','After rotating the marginal sentence, a typed M and hand L replacement are distinct before the lower g. The text reads rang ... 0 ou 1.','margin; margin_rot','deletion state','high',False,True,False,True)
ch('unit reference sign',r'\unsure{(**)|(*+)}','(**)',r'\unsure{(*+)|(**)}','The first hand sign is star-shaped; the second has four principal arms and looks plus-like, though a reduced asterisk cannot be excluded. The first candidate is reversed from C.','insertlabel','misread symbol or index','medium',True,True,False,True)
ch('unit reference attachment','before unit formula','after unit formula','before unit formula','The inserted parenthesized sign stands above the gap preceding the unit isomorphism, with its curved guide descending into that gap.','insertlabel; unitiso','insertion or placement')
ch('unit reference guide','omitted','omitted','curved rising guide drawn','A thin curved stroke links the parenthesized hand label to the preceding gap; no arrowhead is discernible.','insertlabel','drawing or diagram','high',True,True)
ch('unit isomorphism M to L',r'\deleted M\handwritten L_e',r'M_e',r'\deleted M\handwritten L_e','A separate hand L replaces the typed M before subscript e. The following isomorphism sign is hand drawn.','unitiso','deletion state','high',False,True,False,True)
ch('rendre canceled penultimate r','rendre','rende',r'rend\deleted r e','The second r, immediately before the final e, is visibly crossed by an x strike. It must remain as a deletion, not live and not omitted.','rendre','deletion state','high',True,True)
ch('canceled ceux-ci',r'\deleted{\unsure{ceux-ci}}',r'\struck{\ill{}}',r'\deleted{ceux-ci}','The c/e/u/x, hyphen and c/i contours remain legible under cancellation. C doubt is resolved.','ceux',r'readable ink left as \ill{}','high',True,True,True)
ch('canceled right-edge fragment',r'\deleted{\unsure{conditio}}',r'\struck{condition}',r'\deleted{conditio}','The eight visible cells spell conditio. The image ends before any n; none is supplied. The following live line begins conditions. C doubt is resolved to the visible fragment.','cond; conditions','misread word','high',True,True)
ch('mais non fidèle emphasis','underlined','italic','underlined','Separate horizontal rules occur beneath mais non and the next-line fidèle; the grave accent on è is visible.','under; fidele','other')
ch('isomorphism abbreviation',r'\unsure{isoM.|isom.}','isom.',iso,'The final letter cell has two tall M uprights with a lower m-like arch construction overlapping them. The period follows the cell. A simple M or m remains an alternative.','isoM','misread word','medium',True,True)
ch('canceled sinon M',r'\unsure{sinon N|sinon M}','sinon M','sinon M','The final capital has two outer uprights and a central V, identifying M rather than N. The word sinon is readable beneath the cancellation. C doubt resolved.','sinon','misread symbol or index','high',True,False)
for place,crop,sub in [('invertible component','Lg','g'),('idempotent example unit','Mek','e'),('idempotent example p','Mp0','p')]:
 ch(place+' M to L',r'\deleted M\handwritten L_'+sub,'M_'+sub,r'\deleted M\handwritten L_'+sub,'A hand L replaces the typed M; the lower index and the following value are separately legible.',crop,'deletion state','high',False,True,False,True)
ch('p squared numeral',r'p^{\handwritten2}',r'p^2',r'p^2','The raised 2 has the same shaped upper hook, diagonal middle and flat foot as the typed 2 in the section12 heading. Its ink and edge texture are typed, not a hand addition.','p2; p2_close; two_header','insertion or placement','high',True,False)
ch('final reference parentheses','bare mark','parenthesized mark','bare '+label,'No parentheses flank the final reference mark between isomorphismes and the comma.','aster','text not on the page')
ch('final unit subscript',r'1_x','1',r'1_x','A small x sits below-right of the typed1.','oneX','omission','high',False,True,False,True)
ch('bottom separating rule','comment only','omitted','long gently irregular rule drawn','The hand line spans almost the full sheet width above the question and separates it from the typed paragraph.','rule; bottom','drawing or diagram','high',True,True)
ch('Question underline','underlined','italic','underlined','A separate short hand rule lies below Question.','bottom1','other')
ch('bottom satisfaisant tous','satisfaisant tous','satisfaisant à tous','satisfaisant tous','The final n/t strokes of satisfaisant are followed directly by tous. No separate a body and grave accent occur between the words.','bottom3; satisfaisant_tous','text not on the page')
ch('bottom final punctuation','?!','??','?!','The first sign has a long upper question-hook; the second is a narrow curved vertical with its own lower dot and no comparable upper question-hook.','bottom6_full; punct_close','misread symbol or index')
for a,b,c,d,e in [
 ('opening capital',r'\mathbb E',r'\mathbb F; E; F','low','C alternatives retained; overlapping bars prevent a secure alphabet or letter choice.'),
 ('monoïde initial cell',r'\mathbb m',r'\rlap{a}m; \rlap{u}m','medium','Extra enclosed contours and middle bar are not explained by darkness alone.'),
 ('duale second cell',r'\rlap{a}u','u; a','medium','Both bowl and cup contours are present.'),
 ('family symbols',mx,r'\mathbb M; \mathbb X','medium','First qualified; two later cells use the first reading.'),
 ('article before canceled application',r"l\rlap{'}e",'lé; le','medium','Apostrophe-like upright above e may instead be an accent.'),
 ('seven typed tensor signs',r'\otimes',r'\Omega','medium','First occurrence qualified; six recurrences inspected independently.'),
 ('Catégorie initial cell',r'\rlap{c}C',r'\mathbb C; C; c','medium','Tall outer and shorter inner open curves overlap.'),
 ('three symmetry signs',r'\psi',r'\mu','medium','Cup with descending oblique stroke; later two use first candidate.'),
 ('four typed formula reference marks',label,'*','medium','Crossing x plus horizontal stroke; first qualified only.'),
 ('unit reference label','(*+)','(**)','medium','Second hand glyph has four main arms but a reduced star remains possible.'),
 ('isoM abbreviation final cell',r'\rlap{m}M','M; m','medium','Tall M uprights coexist with lower arches.')]:r.doubt(a,b,c,d,e)
r.notation('seven typed tensor-like signs',r'first \unsure{\otimes|\Omega}; six later \otimes','10:130 sum; category insertion; L formula; U formula; display; two a) occurrences','uncertain')
r.notation('two handwritten tensor signs',r'\otimes','10:130 bottom question before foncteur and catégories')
r.notation('family overprint',MX+' then '+mx,'10:130 first indexed family and both Dirac unit components','uncertain')
r.notation('double-struck unit element',r'\mathbb e','10:130 g not-e; compared with ordinary subscript e')
r.notation('typed reference construction',firstlabel+' then '+label,'10:130 left display label; two middle prose references; final bare reference','uncertain')
r.notation('hand unit reference',r'\unsure{(*+)|(**)}','10:130 before L_e isomorphism','uncertain')
r.notation('hand symmetry signs',r'first \unsure{\psi|\mu}; later psi','10:130 group insertion and two phi/psi pairs','uncertain')
r.notation('hand phi signs',r'\phi','10:130 category insertion and two phi/psi pairs; closed circular body crossed by oblique stem')
r.notation('hand duality sign',r'\vee','10:130 baseline before si G est un groupe')
r.notation('M to L replacements',r'\deleted M\handwritten L','10:130 family; display three; margin; unit; lower invertible component; example e and p')
r.notation('typed p exponent',r'p^2','10:130 idempotent example; compared with section12 numeral')
r.notation('ordinary typed capitals',r"A,C,F',G,L,M,U,X,Y,Z",'10:130 each occurrence enlarged individually; weight alone not classified as double striking')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:130 '+c) for a,b,c in [('tens.','tensoriel','above produit'),('loc.','localement','a) paragraph'),('iso[m/M overlap].','isomorphe (tentative expansion)','a) paragraph'),('néc.','nécessairement','bottom question')]]
o={}
def ov(i,s,**kw):o[f'130-E{i:03d}']=dict(first_words_or_objects=s,**kw)
ov(3,'12. Exemples instructifs. Soit G un '+mono+' fini')
ov(8,'application diagonale');ov(12,'On a une '+cat+' avec tensor, phi,1 ... un groupe.')
ov(14,r'\unsure{\psi|\mu}');ov(21,'left constructed label; three M-to-L replacements, isomorphism, tensor')
for i in (32,33):ov(i,r'\unsure{(*+)|(**)}')
ov(37,'ceux-ci');ov(38,'conditio');ov(41,'sinon M');ov(44,'2',hand='typewriter',kind='text')
r.r['inventory_overrides']=o
extras=[('monoïde initial overprint','text','first paragraph','typewriter'),('duale a/u overprint','text','first paragraph','typewriter'),('M/X family symbol','text','first indexed family','typewriter'),('M/X symbol twice in unit sentence','text','Dirac unit sentence','typewriter'),('live e with apostrophe-like upper stroke','text','before canceled application diagonale','typewriter'),('Catégorie C/c overlap','text','interlinear insertion','typewriter'),('hand vee','insertion','before si G est un groupe','unnamed hand'),('constructed left display reference','text','left of display','typewriter'),('constructed reference twice in prose','text','triviaux and satisfont clauses','typewriter'),('constructed bare final reference','text','last typed paragraph','typewriter'),('unit label curved insertion guide','drawing','before unit isomorphism','unnamed hand'),('canceled penultimate r of rendre','deletion','unit-compatibility sentence','typewriter'),('isoM final m/M overlap','text','a) abbreviation','typewriter'),('long hand separating rule','drawing','above bottom question','unnamed hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:130',sheet_kind='typescript',hand=h,element=f'130-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops130.json').read_text())
r.r['inspection_note']='Root alone viewed the whole image, both halves, C/H, all10 C doubts and all51 C inventory items, then all95 enlarged crop recipes. Mis-targeted inline and bottom crops were retained as evidence and followed by corrected full-target crops, all actually viewed. The marginal sentence and slanted bottom question were rotated upright. Every mathematical sign, differing/doubtful locus, deletion, insertion and marginal note was enlarged; agreed prose was checked line by line, with both halves reread. All10 C doubts have explicit decisions. Archive129 remains only an archive comment. The two short typewriter dashes were additionally enlarged and viewed before finalization. No OCR, parallel transcription, context access or mathematical checking occurred.'
r.save('work/record130.json')
