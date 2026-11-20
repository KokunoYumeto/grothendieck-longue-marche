from pathlib import Path
import json,csv
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work');out=root/'edition/reader_reports'
boxes=json.loads((out/'145_scan009_crop_boxes.json').read_text())
margin=r"\margin{\uline{NB} Ceci implique qu'il opère \unsure{triv\textsuperscript{t}} sur l'ens. des trois classes de conjugaison des ss-groupes de lacets --- ce qui précède s'applique.}"
tex=r'''\scanpage{9}
\mspage{3}
Mais comment vérifier que $(p;g)$ définissent non seulement un endomorphisme, mais un automorphisme ? Ça semble délicat\ldots

Dans le cas de $\tau$, on a $p=-1$, et $g=l_1$ :
\[
\tau\rho=\operatorname{int}(l_1)\rho\tau
\]
On veut exprimer la commutation de $u$ (comme autom ext \inserted{respectant la structure à lacets}) non seulement à $\rho$ i.e. $\unsure{\mathfrak S_3^+|\mathcal S_3^+}$,
\margin{\uline{NB} Ceci implique qu'il opère \unsure{triv\textsuperscript{t}} sur l'ens. des trois classes de conjugaison des ss-groupes de lacets --- ce qui précède s'applique.}
mais à $\unsure{\mathfrak S_3|\mathcal S_3}$ tout entier. Il suffit d'exprimer la commutation mod autom extérieurs à $\sigma_\infty$, i.e. d'écrire qu'il existe $h\in\pi$ (également unique) tel que
\[
u\sigma_\infty=\operatorname{int}(h)\deleted{\unsure{u}}\sigma_\infty u,
\]
et il suffira de l'exprimer pour les arguments $l_0$ et $l_1$. On trouve les conditions
\[
\underset{\substack{\Vert\\\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}}}{u\sigma_\infty(l_0)}=\operatorname{int}(h)\underbrace{\sigma_\infty(l_0^p)}_{l_1^p}
\qquad\text{i.e.}\quad\operatorname{int}(g^{-1}h)l_1^p=l_1^p\quad\text{i.e.}
\]
\[
g^{-1}h\in L_1\quad\text{i.e.}\quad h=gl_1^{q}\qquad q\in\hat{\mathbb Z}
\]
et
\[
u\underbrace{\sigma_\infty(l_1)}_{l_0}=\operatorname{int}(h)\sigma_\infty\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}\qquad\text{i.e.}
\]
\[
l_0^p=\operatorname{int}(h\sigma_\infty(g))l_0^p\qquad\text{soit}
\]
\[
l_0^p=\operatorname{int}(gl_1^q\sigma_\infty(g))l_0^p
\]
ce qui équivaut à
\[
\deleted{\operatorname{int}(\unsure{gl_1^q}\sigma_\infty g)L_1=L_0}
\]
i.e. la condition
\[
\exists_q\ \text{tel que}\quad gl_1^q\sigma_\infty(g)\in L_0
\]
\mspage{8}
'''
(out/'145_scan009.tex').write_text(tex,encoding='utf-8')
def crop(n):return f'crops/145_scan009_{n}.png'
def ch(i,place,C,H,final,ink,conf,kind,c,h,marked,n,cats,math=''):
 return dict(id=f's009-{i:02d}',place=place,C=C,H=H,final=final,ink=ink,confidence=conf,kind=kind,c_changed=c,h_changed=h,marked_in_H=marked,crop=crop(n),box=boxes[n],error_category=cats,math_consequence=math)
changes=[
 ch(1,'Opening pair of parameters',r'(p;g)',r'(p,g)',r'(p;g)','The separator has a detached upper dot and a separate curved descending lower stroke. It is a semicolon.','high','other',False,True,'no','pair_separator',[10]),
 ch(2,'Parenthesis comme autom ext and its interlinear insertion',r'(comme autom ext \inserted{\unsure{respectant} la structure à lacets})',r'\marginal{respectant la structure à lacets,}\struck{\ill{}} autom. ext.)',r'(comme autom ext \inserted{respectant la structure à lacets})','The initial c/o/m strokes are reinforced but the word comme is live; no cancellation runs across the whole word. Autom and ext have no following dots. The note reads respectant la structure à lacets; its long connector reaches the gap between ext and the closing parenthesis. The short curved end of that connector is not a comma after lacets.','high','insertion or placement',False,True,'yes','comme_and_respectant_insertion',[2,3,6,7,9]),
 ch(3,'Main prose: mod autom extérieurs','extérieurs',r'\uncertain{intérieurs}','extérieurs','The word begins with a small e-loop, a crossed x, then a tall t; the following accented e and low r/i/eurs sequence are visible. There is no initial i/n sequence. The unexpected extérieurs is preserved.','high','misread word',False,True,'yes','exterieurs',[2]),
 ch(4,'Oblique left-margin NB note and its anchor beside S_3^+',margin,r"\marginal{NB Ceci \uncertain{implique} qu'il \uncertain{existe} \ill{} \ill{} $\Gamma$ \ill{} très \ill{} \ill{} sous-groupe extérieur \ill{} \uncertain{qui} \ill{}}",margin,'After rotation, the seven note lines read NB Ceci implique / qu’il opère triv[t] / sur l’ens. des / trois classes de / conjugaison des / ss-groupes de lacets / — ce qui précède s’applique. The p-descender and accented e in opère are present; l’ens. is a Latin abbreviation, not Gamma; trois, classes, conjugaison, ss-groupes and lacets are legible. The triv[t] cluster remains doubtful. NB is singly underlined. The note begins opposite S_3^+, so its macro is anchored there rather than after tel que or at the page end.','medium','insertion or placement',True,True,'yes','margin_note',[2,3,5,6,8]),
 ch(5,'Cancelled character after int(h)',r'\deleted{\unsure{u}}',r'\struck{\ill{}}',r'\deleted{\unsure{u}}','A heavily blackened small character lies before the live sigma_infty. A low u-like curve is possible, but the crossing strokes obscure enough of its outline that C’s tentative u remains explicitly doubtful. No extra live factor is introduced.','low','misread symbol or index',False,True,'yes','commutation_struck_u',[1,5,7]),
 ch(6,'Word arguments','arguments',r'\textbf{arguments}','arguments','The apparent underline is continuous with the descending stem of g and turns left from its bottom. It extends only under the beginning of the word, with no independent emphasis stroke under arguments.','high','other',False,True,'no','arguments_emphasis',[10]),
 ch(7,'Annotations beneath u sigma_infty(l_0)',r'\underset{\substack{\Vert\\\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}}}{u\sigma_\infty(l_0)}',r'\underbrace{u\sigma_\infty(l_0)}_{\substack{\|\\u(l_1)\\\mathrm{int}(g)l_1^p}}',r'\underset{\substack{\Vert\\\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}}}{u\sigma_\infty(l_0)}','Two small upright strokes form the vertical equality below the main expression. Under those is u(l_1), with a separate bracket underneath it and int(g)l_1^p below that bracket. No brace lies directly beneath the upper main expression.','high','insertion or placement',False,True,'no','first_condition_and_parameter',[1,6],'Preserves the separate equality annotation and the scope of the lower bracket.'),
 ch(8,'Separation of h=gl_1^q and q in hat Z',r'h=gl_1^q,\qquad q\in\hat{\mathbb Z}',r'h=g\,l_1^q,\;q\in\hat{\mathbb Z}',r'h=gl_1^q\qquad q\in\hat{\mathbb Z}','The first formula ends in a superscript q with blank space to its right; q in hat Z occupies a separate lower line. There is no comma after the exponent. The p-like shape immediately before q is the connected upper loop of l, not an additional superscript p.','high','text not on the page',True,True,'no','first_condition_and_parameter',[1,9]),
 ch(9,'Left underbrace in the second calculation',r'u\underbrace{\sigma_\infty(l_1)}_{l_0}',r'\underbrace{u\sigma_\infty(l_1)}_{l_0}',r'u\underbrace{\sigma_\infty(l_1)}_{l_0}','The brace starts beneath sigma, to the right of the separate u, and ends beneath the closing parenthesis. Its l_0 label therefore applies to sigma_infty(l_1) alone.','high','insertion or placement',False,True,'no','second_condition_annotation',[1,6],'Attaches l_0 to sigma_infty(l_1), excluding the preceding u.'),
 ch(10,'Parentheses inside the cancelled bottom condition',r'\deleted{\operatorname{int}(gl_1^q\sigma_\infty(g))L_1=L_0}',r'\struck{\mathrm{int}(g\,l_1^q\,\sigma_\infty g)L_1=L_0}',r'\deleted{\operatorname{int}(\unsure{gl_1^q}\sigma_\infty g)L_1=L_0}','The final g follows sigma_infty directly, without an opening parenthesis, and is followed by one closing parenthesis terminating int’s argument. C adds an inner pair. The crossing line leaves a small entangled trace between the first g and l_1^q, so that initial group has a new uncertainty mark; it is not silently reconstructed.','medium','misread symbol or index',True,False,'no','cancelled_condition',[1,7,9]),
 ch(11,'Final existential quantifier',r'\exists_q',r'\exists\,q',r'\exists_q','The q stands small and low against the lower right of the existential sign, with its descender continuing below that sign’s baseline. It is subscripted rather than a full-sized baseline q.','high','misread symbol or index',False,True,'no','existential_condition',[1]),
 ch(12,'Lower-left manuscript number',r'\mspage{8}','',r'\mspage{8}','Two connected loops, upper narrow and lower rounded, form a clear handwritten 8.','high','omission',False,True,'no','manuscript_number_eight',[3]),
 ch(13,'End of abbreviation in mod autom','mod autom','mod autom.','mod autom','After the final low m-stroke, the paper is blank. The dark terminal at the end of m is connected to the letter and is not a separate period.','high','text not on the page',False,True,'no','mod_autom_punctuation',[9])
]
def dec(id,decision,reading,ink,n,confidence):
 return dict(id=id,decision=decision,reading=reading,ink=ink,crop=crop(n),box=boxes[n],confidence=confidence)
decisions=[
 dec('M0787','first','Ça','The large open C, its small detached cedilla below, and the connected round a are distinct. There is no cancellation of the word.','ca_semble','high'),
 dec('M0788','first','respectant','A compact re/s opening precedes the visible p-descender; the connected ectant continuation precedes the separate la. The insertion connector is below the words, not a cancellation through them.','comme_and_respectant_insertion','medium'),
 dec('M0789','undecided',r'\unsure{\mathfrak S_3^+|\mathcal S_3^+}','An ornate S, subscript 3 and high plus are visible. The letter’s outer loop and inner turn do not by themselves establish the intended typographic alphabet. The plus’s short arm and upright are both present.','s3_plus','medium'),
 dec('M0790','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The ornate S and lower 3 are clear; Fraktur versus calligraphic styling remains a transcription-alphabet question.','s3_entier','medium'),
 dec('M0791','undecided',r'\unsure{triv\textsuperscript{t}}','The note’s small contracted word has a tall initial t, low r/i-like traces and a compressed final/raised cluster. Its precise v and raised t are not fully separable in the interlocking ink, so the abbreviation remains doubtful.','margin_note','low')
]
unlisted=[dec('U009-01','undecided',r'\deleted{\unsure{u}}','The cancelled character is heavily blackened; a u-like lower curve is visible, but every stroke is not plain.','commutation_struck_u','low')]
doubts=[
 {'place':'rho i.e. S_3^+','reading':r'\unsure{\mathfrak S_3^+|\mathcal S_3^+}','alternatives':[r'\mathfrak S_3^+',r'\mathcal S_3^+'],'confidence':'medium','reason':'The ornate S is secure, as are 3 and +; typographic alphabet remains unsettled.'},
 {'place':'mais à S_3 tout entier','reading':r'\unsure{\mathfrak S_3|\mathcal S_3}','alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'Same local alphabet uncertainty; no uncertainty about the index 3.'},
 {'place':'NB margin, after opère','reading':r'\unsure{triv\textsuperscript{t}}','alternatives':[],'confidence':'low','reason':'Small interlocked abbreviation with raised terminal; the proposed expansion is not substituted for its written form.'},
 {'place':'Cancelled factor after int(h)','reading':r'\deleted{\unsure{u}}','alternatives':[],'confidence':'low','reason':'Dense crossing strokes do not permit every part of the character to be identified.'},
 {'place':'Beginning of int argument in cancelled bottom equation','reading':r'\unsure{gl_1^q}','alternatives':[],'confidence':'low','reason':'There is a small entangled trace between the first g and l_1^q under the cancellation; the retained grouped reading is provisional.'}
]
def inv(e,k,p,f,b):return dict(element=e,kind=k,position=p,first_words_or_objects=f,box=b,sheet_kind='text',hand='his hand',transcribed='yes')
inventory=[
 inv('N01','margin note','top centre','3',[845,25,900,85]),
 inv('T01','text','top prose question, three lines','Mais comment vérifier ...',[230,90,1585,370]),
 inv('T02','text','line introducing tau','Dans le cas de tau ...',[320,400,1545,480]),
 inv('F01','display','upper formula','tau rho = int(l_1) rho tau',[450,495,825,590]),
 inv('T03','text','main prose block between upper formula and commutation equation','On veut exprimer la commutation ...',[220,615,1655,1200]),
 inv('I01','insertion','interlinear, connected before closing parenthesis after autom ext','respectant la structure à lacets',[730,655,1290,760]),
 inv('M01','margin note','seven oblique lines along left margin beside S_3^+','NB Ceci implique ...',[18,755,465,1300]),
 inv('F02','display','main commutation equation','u sigma_infty = int(h) ...',[485,1205,1015,1315]),
 inv('D01','deletion','inside F02, after int(h)','uncertain u',[797,1220,848,1275]),
 inv('T04','text','two lines introducing calculations','et il suffira de l’exprimer ...',[210,1290,1575,1510]),
 inv('F03','display','first calculation, with vertical equality, two bracket annotations and right-hand consequences','u sigma_infty(l_0) ... g^-1 h in L_1 ... h=gl_1^q ...',[375,1495,1590,1735]),
 inv('T05','text','short linking word before second calculation','et',[215,1765,280,1810]),
 inv('F04','display','second calculation with two underbrace annotations','u sigma_infty(l_1) ...',[320,1760,1060,1925]),
 inv('F05','display','first resulting l_0^p formula','l_0^p=int(h sigma_infty(g))l_0^p',[380,1925,1060,2020]),
 inv('F06','display','second resulting l_0^p formula','l_0^p=int(g l_1^q sigma_infty(g))l_0^p',[530,2030,1110,2145]),
 inv('T06','text','right of F05','soit',[965,1925,1060,2000]),
 inv('T07','text','right of F06','ce qui équivaut à',[1170,2010,1640,2125]),
 inv('D02','deletion','cancelled equation near foot','int(g l_1^q sigma_infty g)L_1=L_0',[525,2140,1100,2268]),
 inv('T08','text','right of cancelled equation','i.e. la condition',[1170,2130,1645,2240]),
 inv('F07','display','last line','exists_sub_q tel que g l_1^q sigma_infty(g) in L_0',[295,2250,1075,2348]),
 inv('N02','margin note','lower left','8',[35,2270,85,2338])
]
second=[]
def sb(n,kind,coords,reading):second.append(dict(box=f'B{n:02d}',kind=kind,coords=coords,reading=reading))
sb(1,'handwritten top page number',[835,20,910,90],r'\mspage{3}')
sb(2,'C/H separator disagreement',boxes['pair_separator'],r'(p;g)')
sb(3,'resolved C doubt',boxes['ca_semble'],'Ça semble')
sb(4,'all numeric text and complete tau display',[310,395,1555,595],r'Dans le cas de $\tau$, on a $p=-1$, et $g=l_1$ : $\tau\rho=\operatorname{int}(l_1)\rho\tau$')
sb(5,'interlinear insertion, resolved C doubt and C/H live-versus-struck word disagreement',boxes['comme_and_respectant_insertion'],r'(comme autom ext \inserted{respectant la structure à lacets}) non seulement')
sb(6,'both S alphabet doubts, plus and handwritten indices',[315,780,935,930],r'$\unsure{\mathfrak S_3^+|\mathcal S_3^+}$, mais à $\unsure{\mathfrak S_3|\mathcal S_3}$')
sb(7,'C/H lexical disagreement',boxes['exterieurs'],'extérieurs à')
sb(8,'abbreviation punctuation disagreement',boxes['mod_autom_punctuation'],'mod autom')
sb(9,'complete marginal note; C doubt; C/H lexical disagreements',boxes['margin_note'],margin)
sb(10,'complete commutation display with struck C doubt',boxes['commutation_struck_u'],r'u\sigma_\infty=\operatorname{int}(h)\deleted{\unsure{u}}\sigma_\infty u,')
sb(11,'apparent underline versus g-descender',boxes['arguments_emphasis'],'les arguments')
sb(12,'all handwritten indices in calculation-introduction line',[200,1410,1110,1518],r'$l_0$ et $l_1$. On trouve les conditions')
sb(13,'complete first calculation and all annotations, indices and exponents; parameter line; punctuation disagreement',boxes['first_condition_and_parameter'],r'\underset{\substack{\Vert\\\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}}}{u\sigma_\infty(l_0)}=\operatorname{int}(h)\underbrace{\sigma_\infty(l_0^p)}_{l_1^p}\quad\text{i.e.}\quad\operatorname{int}(g^{-1}h)l_1^p=l_1^p\quad\text{i.e.}\quad g^{-1}h\in L_1\quad\text{i.e.}\quad h=gl_1^q\quad q\in\hat{\mathbb Z}')
sb(14,'complete second calculation and annotations; every index; disputed brace scope',boxes['second_condition_annotation'],r'u\underbrace{\sigma_\infty(l_1)}_{l_0}=\operatorname{int}(h)\sigma_\infty\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}\quad\text{i.e.}')
sb(15,'two complete resulting displays with every handwritten index and exponent',[380,1920,1645,2140],r'l_0^p=\operatorname{int}(h\sigma_\infty(g))l_0^p\quad\text{soit}\quad l_0^p=\operatorname{int}(gl_1^q\sigma_\infty(g))l_0^p\quad\text{ce qui équivaut à}')
sb(16,'complete struck condition, newly doubtful group, parentheses dispute, handwritten indices',boxes['cancelled_condition'],r'\deleted{\operatorname{int}(\unsure{gl_1^q}\sigma_\infty g)L_1=L_0}\quad\text{i.e. la condition}')
sb(17,'complete final condition; existential subscript and all handwritten indices',boxes['existential_condition'],r'\exists_q\ \text{tel que}\quad gl_1^q\sigma_\infty(g)\in L_0')
sb(18,'handwritten lower page number',boxes['manuscript_number_eight'],r'\mspage{8}')
notation=[
 {'observation':'The pair of parameters is written (p;g), with a true semicolon.','observed_places':['first line'],'qualification':'Only one parameter-pair occurrence on this page.'},
 {'observation':'The ornate S notation appears once with lower 3 and upper +, once with lower 3 alone.','observed_places':['main prose, S_3^+ and S_3'],'qualification':'Letter, index and plus are clear; typographic alphabet remains uncertain.'},
 {'observation':'The main calculation uses u, sigma_infty, int(h), and loop generators l_0,l_1, with powers p and q.','observed_places':['commutation display and all lower calculations'],'qualification':'The tiny cancelled factor remains uncertain; no algebraic result was verified.'},
 {'observation':'The first computation has a vertical equality below the left side, then u(l_1), then a bracket carrying int(g)l_1^p. The second left brace excludes u.','observed_places':['first and second lower calculations'],'qualification':'These are distinct annotation layouts and should not be mechanically regularized.'},
 {'observation':'q in hat Z is written below h=gl_1^q.','observed_places':['right-hand part of first calculation'],'qualification':'No separating comma is visible. The loop of l can resemble a raised p.'},
 {'observation':'The last quantifier is exists with a subscript q.','observed_places':['last displayed line'],'qualification':'Preserved as exists_q.'},
 {'observation':'The cancelled formula writes sigma_infty g without inner parentheses; the live formulas nearby write sigma_infty(g).','observed_places':['cancelled penultimate equation','live preceding and final equations'],'qualification':'The difference is kept as written.'}
]
hand=[
 {'habit':'A g descender may sweep left and resemble an underline.','places':['arguments'],'universal_on_page':'Observed distinctly at this word; not asserted for every g.','witness_misreadings':'H emphasizes arguments, but its apparent underline is the connected g-descender.'},
 {'habit':'A tall looped l can have a p-like upper loop.','places':['h=gl_1^q'],'universal_on_page':'Local form; compared with other l letters in the same crop.','witness_misreadings':'No witness error here. A possible extra p was considered and rejected from the continuous stroke.'},
 {'habit':'The main first letters of extérieurs are a small e followed by a crossed x and tall t.','places':['mod autom extérieurs'],'universal_on_page':'Only this word-instance examined.','witness_misreadings':'H suggests intérieurs, while the ink supports extérieurs.'},
 {'habit':'Reinforced writing does not necessarily denote cancellation.','places':['Ça','comme'],'universal_on_page':'Local observation; the genuinely cancelled u is much more heavily crossed.','witness_misreadings':'C doubts Ça; H treats the comme region as struck/illegible.'},
 {'habit':'The oblique margin uses contractions and compressed joins, but the g/p descenders and tall t/l strokes remain useful.','places':['NB note'],'universal_on_page':'One marginal note only.','witness_misreadings':'H misreads opère as existe and leaves much of l’ens., trois classes, conjugaison and ss-groupes de lacets unreadable.'}
]
abbreviations=[
 {'form':'autom','expansion':'automorphisme / automorphismes','place':'comme autom ext; mod autom extérieurs'},
 {'form':'ext','expansion':'extérieur','place':'comme autom ext'},
 {'form':'mod','expansion':'modulo','place':'mod autom extérieurs'},
 {'form':'i.e.','expansion':'id est','place':'main prose and several calculation links'},
 {'form':'NB','expansion':'nota bene','place':'left margin note'},
 {'form':r'triv\textsuperscript{t} (doubtful)','expansion':'trivialement','place':'left margin after opère'},
 {'form':"l'ens.",'expansion':"l'ensemble",'place':'left margin'},
 {'form':'ss-groupes','expansion':'sous-groupes','place':'left margin'},
 {'form':r'\operatorname{int}','expansion':'automorphisme intérieur','place':'all conjugation expressions'}
]
rows=list(csv.DictReader((root/'packets/145_scan009/differences.tsv').open(encoding='utf-8'),delimiter='\t'))
substantive={3:'s009-01',7:'s009-02',8:'s009-02',11:'s009-03',12:'s009-04',14:'s009-05',16:'s009-07',17:'s009-07',35:'s009-10',36:'s009-10',39:'s009-11',42:'s009-12'}
explain={1:'Scan marker versus editorial introduction to the author’s number; the source top 3 is retained as mspage{3}.',2:'H’s words de l’auteur are editorial.',4:'C’s ldots macro versus H’s ellipsis character; the same visible three dots.',9:'Tokenized alphabet alternative only; M0789 retains the uncertainty.',10:'Tokenized alphabet alternative only; M0790 retains the uncertainty.',20:'Display boundary difference only.',21:'Placement of display boundary relative to i.e.; no change of source text.',22:'TeX thin-space token and concatenation of g with following l only.',23:'H backslash-semicolon is spacing. Both witnesses’ separate literal comma after the exponent is removed under s009-08.',30:'TeX thin-space token and concatenation only.',33:'TeX thin-space token and concatenation only.',37:'Display boundary only.',38:'Display boundary only.',40:'TeX thin-space token and concatenation only.'}
coverage=[]
for i,row in enumerate(rows,1):
 if i in substantive:
  d={'row':i,'status':'substantive','change_id':substantive[i]}
  if i==11:d['explanation']='The lexical dispute is s009-03; H’s added period after preceding autom is independently covered by s009-13.'
  if i==14:d['explanation']='C’s tentative cancelled u versus H’s illegible cancellation is substantive; the comma tokens are H TeX thin spaces.'
  if i==36:d['explanation']='The redundant closing inner parenthesis in C is s009-10; H’s comma token is a TeX thin space.'
  if i==42:d['explanation']='Source lower number 8 is s009-12. H’s explanatory formula note is editorial; H’s appended marginal-note reading is collated under s009-04.'
  coverage.append(d)
 else:coverage.append({'row':i,'status':'macro/editorial','explanation':explain.get(i,'H TeX thin-space command only; no manuscript comma is asserted at this token.')})
report=dict(scan=9,reader='/root/reader_c',lines_read=34,
 layout='Upright handwritten page: 24 main/annotation rows, one interlinear prose-insertion row, seven oblique left-margin note rows, and two isolated handwritten page numbers (3 above, 8 below): 34 read rows/inscriptions. Main prose occupies the upper half, followed by calculations with underbraces and a vertical equality annotation. One prose insertion and two genuine cancellations. No diagram or drawing.',
 changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,notation=notation,hand=hand,abbreviations=abbreviations,
 notes=[
  'The page begins by asking how to verify that (p;g) defines an automorphism and not merely an endomorphism. The author writes “Ça semble délicat...” as an explicit statement of difficulty. He then records the tau example p=-1, g=l_1 and the displayed commutation formula. These are manuscript statements, not results verified by this reader.',
  'The author seeks to express commutation of u, viewed as an exterior automorphism respecting the structure à lacets, first with rho and then with the whole S_3. He explicitly writes “mod autom extérieurs”; the initial ex is visible and has not been corrected to H’s intérieurs. The left note says that the operation is trivial on the set of three conjugacy classes of the loop subgroups, although the contracted triv[t] itself remains uncertain.',
  'He introduces h through u sigma_infty=int(h) sigma_infty u and tests the relation on l_0 and l_1. The written calculations lead through g^-1 h in L_1 and h=gl_1^q, q in hat Z, to the final existential condition gl_1^q sigma_infty(g) in L_0. A preceding L_1=L_0 conjugation statement is cancelled. This describes the author’s chain of formulas; it is not an independent proof or check of its hypotheses.',
  'The two annotation layouts are deliberately kept distinct. In the first, a vertical equality leads to u(l_1), which itself has a lower bracket. In the second, the left underbrace covers sigma_infty(l_1) but excludes u. The apparent underline of arguments is a g-descender and does not receive an emphasis macro.',
  'The apparent extra p before the superscript q in h=gl_1^q was examined in the complete first-calculation crop and identified as the connected upper loop of l. No mathematical correction was used to decide this. In the cancelled last-but-one expression, the tiny interlocked trace after the first g is still uncertain, and the grouped reading gl_1^q remains marked.',
  'There is no date on the page. The top number is 3; the bottom-left number is 8. Both are preserved. The mathematical displays have no separate visible formula numbers.',
  'The whole-page image and each full-resolution half were viewed once. Fifteen distinct enlarged first-reading crops were made and viewed once each; the margin note crop was rotated 26 degrees clockwise. All supplied C deletions and the insertion were accounted for. No OCR, other page images, other reader reports, external research, mathematical proof check, or TeX compilation was used. The decisions array contains exactly the five MARKS IDs; the unindexed struck-u doubt is in unlisted_decisions.'
 ],check_events=[],diff_coverage=coverage)
(out/'145_scan009.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'scan':9,'crops':len(boxes),'changes':len(changes),'decisions':len(decisions),'unlisted_decisions':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(rows),'covered_rows':len(coverage)}))
