import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{\handwritten{31}}',r'\mspage{- \handwritten{31} -}'),(r'\uline{1}.',r'\uline{\handwritten{1}}.'),('analytique .d\'une',"analytique \\unsure{.|}d'une"),(r'Dans ce \handwritten{\S} ;',r'Dans ce \handwritten{\S}\unsure{,|;}'),(r'\uline{deux polycylindres ouverts, de centres}',r'\uline{deux polycylindres ouverts}, \uline{de centres}'),(r'\unsure{g|y|z}','g'),(r'\uline{sommable dans}\unsure{-} Q',r'\uline{sommable dans} Q'),(r'\handwritten{g}(\deleted{\handwritten{g}}\inserted{\handwritten{x}})=',r'\handwritten{g(}\deleted{\handwritten{g}}\inserted{\handwritten{x}}\handwritten{)}\handwritten{=}'),(r'\handwritten{\rho}>0',r'\handwritten{\rho>}0'),(r'\handwritten{\rho}<t<\handwritten{\rho}',r'\handwritten{\rho<}t\handwritten{<\rho}'),(r'\handwritten{\alpha}>0',r'\handwritten{\alpha>}0')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','31','- 31 -','- 31 -','header: a short horizontal blue dash is visible on each side of the handwritten figures.','high',True,False,'omission')
a('section number','1 not marked handwritten','1 marked handwritten','handwritten 1','number: the numeral has one thick pen stroke and an angled top, unlike the serifed typewriter numerals.','high',True,False,'insertion or placement')
a('title before d’une','dot','uncertain dot','uncertain dot or absence','title_dot: the small black point lies near the baseline but differs in colour from the blue typed letters; it may be a speck.','low',True,True)
a('punctuation after section sign','semicolon','uncertain semicolon/comma','uncertain comma/semicolon','section_punct: the lower curved blue impression is clear; the upper point is black and offset to its right. Comma is the visually stronger reading, but semicolon remains possible.','low',True,True)
a('proposition, underline after ouverts','continuous underline including comma','separate runs','separate underlines, comma outside','rule: the line stops before the comma and resumes beneath de centres.','high',True)
a('cancelled argument of g','unsure g/y/z','unsure g/z','cancelled g','old_g: despite the diagonal cancellation strokes, a rounded upper bowl and a separate descending loop remain visible, matching the live g to its left. The replacement x is above.','high',True,True,'misread symbol or index')
a('after sommable dans','uncertain dash','no dash','no dash','dash: the small horizontal trace is tan paper material; the blue underline ends below the final s.','high',True,False,'text not on the page')
a('handwritten punctuation and inequalities','g parentheses/equality and final strict inequalities left outside handwritten spans','these marked handwritten','these marked handwritten','old_g, proof1 and proof2: the g parentheses, its first equals sign and the strict chevrons have pen contours rather than typewriter impressions; the second equals at the following line is preserved.','high',True,False,'insertion or placement')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 31 -')
i('text','chapter heading','CHAPITRE II (Etat 1)','typewriter')
i('text','chapter title',"FONCTIONS HOLOMORPHES D’UNE VARIABLE COMPLEXE.",'typewriter')
i('text','section heading','§1. Le principe du prolongement analytique.')
i('text','subsection heading','1. Prolongement analytique [possible dot]d’une fonction holomorphe.')
i('text','notation paragraph','Dans ce § … K désignera … E un espace normé complet …')
i('text','proposition','PROPOSITION 1.- Dans l’espace K^p … f and g series … equality on U implies equality on P cap Q.')
i('display','first series','f(x)=sum c_(n1 n2..np)(x1-a1)^n1 … (xp-ap)^np')
i('deletion','argument of second series','g','unnamed hand')
i('insertion','above cancelled argument','x','unnamed hand')
i('display','second series','g(x)= =sum d_(n1 n2..np)(x1-b1)^n1 … (xp-bp)^np')
i('text','proof','Soit en effet x un point de U … segment … h(t) … rho … zéros isolés … mais cela est')
i('display','line restriction','h(t)=f(x+t(y-x))-g(x+t(y-x))')
i('display','zero interval and endpoint','0<=t<=1, h(s)=0 for 0<=s<=t, rho>0, rho in A, rho=1; later rho<t<rho+alpha, alpha>0')
commit(15,37,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole image, then both halves personally read before C1 and C2. All titles, prose and mathematical completions were enlarged, including the cancelled argument. Two equals signs at the line break and absence of punctuation between nuls and on a are retained. No H text. No context consulted.'))
