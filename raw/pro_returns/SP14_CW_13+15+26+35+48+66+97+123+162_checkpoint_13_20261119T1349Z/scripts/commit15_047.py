import sys,re
sys.path.insert(0,'out/scripts');from work import commit,W,row
r=row(15,47)
c2=(W/r['codex_file_run2']).read_text()
fig=c2[c2.index(r'\margin{\figure'):c2.index('% block: middle; lines')].rstrip()
original=(W/r['codex_file']).read_text()
oldfig=original[original.index(r'\margin{\handwritten{\figure'):original.index('Lorsque')].rstrip()
R=[(r'\mspage{22}',r'\mspage{- 22 -}'),
 (r'a_1,..,a_p',r'a_1,\ldots,a_p'),
 (oldfig,'% The brown marginal outline is visible; whether it is ink or adhering material is uncertain.\n'+fig),
 (r'\unsure{\mathbb{R}|R}',r'\unsure{R|\mathbb{R}}'),
 (r'chap.I,\S\,2',r'chap.I,\handwritten{\S}\,2'),
 (r'chap.IV,\S\,2',r'chap.IV,\handwritten{\S}\,2'),
 (r'\handwritten{|x-1|<\frac{1}{2}}',r'\handwritten{|}x-1\handwritten{|<\frac{1}{2}}'),
 (r'\uline{3}.',r'\handwritten{\uline{3}}.'),
 (r'\margin{\handwritten{\unsure{-}}}',r''),
 (r'\uline{et un système et un seul de} $p$',r'\uline{et un système et un seul de} $\uline{p}$'),
 (r'\uline{holomorphes dans} $U\handwritten{\times}W$ \uline{telles',r'\uline{holomorphes dans} $U\handwritten{\times}W$\handwritten{,} \uline{telles'),
 (r'\handwritten{\to}(u_i(x;z_1,..,z_q))',r'\handwritten{\to}(u_i(x;z_1,\ldots,z_q))')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','22','- 22 -','- 22 -','header: blue horizontal dashes flank both digits.','high',True,False,'omission')
a('corollary, initial function','only u handwritten','entire u(z1,..,zp) handwritten','only u handwritten','u_typed and corollary: the u is a broad blue pen stroke; parentheses, z letters, indices and two dots have the regular dark typewriter impressions.','high',False,True,'other')
a('corollary, point a','only a handwritten; two dots','entire point handwritten; three dots','only a handwritten; three dots','a_dots and corollary: three round dots occur between the commas; the equals sign, parentheses and indexed a letters are typed.','high',True,True,'misread symbol or index')
a('corollary, differential','unsure d.u(a)/du(a)','d.u(a)','unsure d.u(a)/du(a)','d_dot: a dark round spot appears after the d below its upper curve, but its colour and boundary do not securely distinguish a pen stop from a puncture or paper defect.','low',False,True,'misread symbol or index')
a('left margin beside Lorsque','angular small outline','filled irregular pointing outline','filled irregular pointing outline; material uncertain','mark: the right side forms a thick vertical lobe with two internal pale divisions; a narrow projection points left and a short lower hook returns right. The scan does not settle whether the brown material is drawn ink.','medium',True,False,'drawing or diagram')
a('real-field symbol after K=','unsure blackboard R/R','unsure R/blackboard R','unsure R/blackboard R','R: the main stem is broad, but a separate parallel stem is not secure; retain both alphabets with plain R first.','low',True,False,'misread symbol or index')
a('two bibliographical section signs','unmarked as hand','handwritten section signs','handwritten section signs','real and complex: both section signs have continuous blue loops distinct from the typed chapter numerals.','high',True,False,'other')
a('complex-field symbol after K=','blackboard C','unsure C/blackboard C','blackboard C','C: an inner curved stroke runs parallel to the main left curve and supports the double-stroke alphabet.','high',False,True,'misread symbol or index')
a('disc inequality','entire formula handwritten','x-1 typed, surrounding symbols handwritten','x-1 typed, surrounding symbols handwritten','disc: the x, short minus and upright 1 have the dark serif impressions of the typewriter; the two bars, inequality and fraction are blue pen.','high',True,False,'other')
a('section numeral 3','underlined 3, unmarked as hand','handwritten underlined 3','handwritten underlined 3','section3: the connected angled upper stroke and rounded lower return are blue pen, with a blue rule below.','high',True,False,'other')
a('left margin beside theorem','unsure dash','absent','absent','dash: the apparent dash is a tan fleck continuous in colour with the paper; no dark or blue ink stroke is visible.','high',True,False,'text not on the page')
a('et un système et un seul de p','p outside underline','p outside underline','p underlined','p_rule: the blue line continues beneath the p descender into the underline below fonctions.','high',True,True,'omission')
a('first U times W before telles','no comma','no comma','handwritten comma','comma and theorem2: a faint blue head and short descending tail lie just after W, above the start of the next underline.','medium',True,True,'omission')
a('last mapping, argument inside u_i','two dots','three dots','three dots','last_dots: three separate round typed points occur between the two commas; the outer mapping argument has only two.','high',True,False,'misread symbol or index')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 22 -','typewriter')
i('text','corollary, first six lines','COROLLAIRE.- Soit u(z1,..,zp) … différentielle d.u(a)/du(a) … réciproque holomorphe')
i('drawing','left margin beside Lorsque','irregular brown pointing outline; material uncertain','unnamed hand or adhering material, uncertain')
i('text','middle, real-field paragraph','Lorsque K=R … A tout entier … Fonct.var.réelle … Top.gén.')
i('text','middle, complex-field paragraph','Mais lorsque K=blackboard C … exemple u(x)=x^n … |x-1|<1/2 … x^n=1')
i('text','below example','Il faudrait faire ici également le théorème de dépendance … jacobien identiquement nul.','typewriter and unnamed hand')
i('text','section heading','3. Intégration des équations différentielles.')
i('text','theorem 2, lower third','Soit K … caractéristique 0 … f_i(x;…;…) … U times V times W subset A … système unique … conditions')
commit(15,47,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole page and both halves personally read before C1/C2, then all text and formula-bearing bands enlarged, with separate close views for disagreements and doubts. No H text. No cancellation or insertion. The deferred dependency theorem is transcribed without filling it in. The brown marginal shape is reproduced but its physical origin remains uncertain. Context unopened.'))
