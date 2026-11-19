import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{27}',r'\mspage{- 27 -}'),(r'\uline{En outre, il existe un voisinage}',r'\uline{En outre}, \uline{il existe un voisinage}'),(r'\uline{tel que, pour tout}',r'\uline{tel que}, \uline{pour tout}'),('tel que pour tout','tel que, pour tout'),(r'M|x-x_0|',r'M\handwritten{|}x-x_0\handwritten{|}'),(r'\unsure{-.|-} ',''),(r'\handwritten{w\in}',r'\handwritten{\unsure{w|W}\in}'),(r'\handwritten{w}',r'\handwritten{\unsure{w|W}}')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','27','- 27 -','- 27 -','header: short blue horizontal dashes flank the numeral.','high',True,False,'omission')
a('statement, two underline breaks','continuous across commas after En outre and tel que','separate runs','separate runs','top and underlines: each underline stops before the comma and restarts under the next word.','high',True,False,'insertion or placement')
a('proof, tel que before pour tout','tel que pour tout','tel que pour tout','tel que, pour tout','comma: a blue curved comma stands at the baseline after que, matching the other typed commas.','high',True,True,'omission')
a('proof, internal hyphen in pa-rt','handwritten hyphen','hyphen unmarked','handwritten hyphen','part: a rising curved pen stroke joins the typed a and r; it is not a level typewriter dash.','high',False,True,'insertion or placement')
a('norm estimate, absolute-value bars','bars unmarked','handwritten bars','handwritten bars','proof2: both bars around x-x0 are tall uneven pen strokes, unlike the adjacent typed x and M.','high',True,False,'insertion or placement')
for p,crop,c2 in [('after D’ailleurs, si','w1','unsure W/w'),('argument in y0=u(x0,x,…)','w2','W'),('argument in s→u(s,x,…)','w3','W'),('final y=…','w4','W')]:
 a(p,'w',c2,'unsure w/W',crop+': the doubled valley and turned entry/exit suggest cursive w, but the variable height and angular middle strokes do not securely distinguish it from capital W.','low',True,True,'misread symbol or index')
a('after au point x0,','uncertain dash-dot/dash','nothing after comma','nothing after comma','punct: the comma is blue; the following short tan mark and separate black speck are paper material, not blue punctuation.','high',True,False,'text not on the page')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 27 -','typewriter')
i('display','equation (20)','D u(x,x0,y0)=f(x,u(x,x0,y0))')
i('text','below (20)','(D dériva tion par rapport à x, f=(f_i)), et la condition')
i('display','equation (21)','u(x0,x0,y0)=y0.')
i('text','underlined statement','En outre … V1 subset V … une seule ra-cine y=u(x,x0,y0).')
i('text','proof, first part','Posons en effet … y-y0=z … z′=f(x0+t,y0+z) … th.2 …')
i('text','proof, neighbourhood and bound','D’autre pa-rt … tel que, pour tout … U times C … th. des accroissements finis')
i('display','norm estimate in continuing line','norm(u-y0)=norm(u-u(x0,x0,y0))<=M abs(x-x0)')
i('text','proof, last part','quels que soient … uniqueness of s→u … four w/W … et achève la démonstration.')
commit(15,41,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves personally viewed, then both C runs. All mathematical expressions enlarged with prose in four bands; punctuation and all four disputed w/W forms separately enlarged. Literal dériva tion, ra-cine, pa-rt, and U times C retained. No H text, marginal additions or cancellations. No context consulted.'))
