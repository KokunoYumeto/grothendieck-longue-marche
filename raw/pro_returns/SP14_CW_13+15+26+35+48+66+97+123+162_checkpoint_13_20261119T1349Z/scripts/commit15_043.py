import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{24}',r'\mspage{- 24 -}'),(r'\unsure{\nu|v}',r'\nu'),('les équations (13)','les équations (15)'),(r'\ell}}<m+',r'\ell}}\handwritten{<}m+'),(r'$<t$',r'$\handwritten{<}t$'),(r'un\unsure{voisina-ge|voisinage}',r'un\unsure{voisina}\handwritten{-}ge'),(r'\unsure{somm bilité|sommabilité}','somm bilité'),(r'$C_i(n;',r'$G_i(n;'),(r'\unsure{\mathbb{H}|H}_i',r'H_i'),(r'\handwritten{\lambda}_1,..,\handwritten{\lambda}_q',r'\handwritten{\lambda}_1,\ldots,\handwritten{\lambda}_q')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other',cons=None):
 x=dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable')
 if cons:x['consequential']=cons
 L.append(x)
a('original page number','24','- 24 -','- 24 -','header: blue horizontal dashes appear on both sides.','high',True,False,'omission')
a('equation (16), first inner upper bound','r_j','unsure r_j/q_j','r_j','rj: an open shoulder and upright are visible; no closed oval of q is present.','high',False,True,'misread symbol or index')
a('equation (16), lambda','unsure lambda/Lambda','unsure lambda/Lambda','unsure lambda/Lambda','lambda: a tall right stroke and faint diagonal at the apex leave the branch point uncertain; the lower-case reading remains first.','low')
a('equation (16), final Greek letter','unsure nu/v','nu','nu','nu: the short left stroke and long hooked returning right stroke match the other handwritten nu forms in sum and exponents; they are not a straight two-legged v.','high',True,False,'misread symbol or index')
a('figure aux seconds membres de','(16)','(15)','(16)','ref1 and tag16: the last numeral has a curved upper hook and a closed lower bowl, matching the clear 6 in the top equation label.','medium',False,True,'misread symbol or index')
a('par récurrence, les équations','(13)','(15)','(15)','ref2: the last digit has a flat upper stroke, a faint short left upright and a lower bowl, rather than the two rounded lobes of 3.','medium',True,False,'misread symbol or index', 'The recursive determination cites equation (15), not (13).')
a('two strict degree inequalities','chevrons unmarked','handwritten chevrons','handwritten chevrons','exponents and recurrence: the broad uneven chevrons are drawn by pen between typewritten terms.','high',True,False,'insertion or placement')
a('de fa-çon','fa with handwritten hyphen then çon','façon','fa with handwritten hyphen then çon','facon_full: a clear rising blue stroke joins a to ç at mid-height.','high',False,True,'omission')
a('underlined summability condition','un followed without space by unsure voisina-ge/voisinage','unsure joined/spaced unvoisina-ge and un voisinage','un followed without space by unsure voisina, handwritten hyphen, ge','voisinage: n and v are adjacent without the normal typewriter word space. A rising blue hyphen after a is visible; damage obscures upper parts of the internal letters, so that word stem remains marked doubtful.','medium',True,True,'misread word')
a('solutions du système (12), domain','U in W','U unsure in/times W','U in W','in: a curved left outline and middle horizontal bar form an epsilon-shaped membership sign; there are no crossing diagonals.','high',False,True,'misread symbol or index')
a('Pour prouver la …','unsure somm bilité/sommabilité','somm bilité','somm bilité','sommabilite: a full blank typewriter space follows somm; no a is visible.','high',True,False,'misread word')
a('majorant coefficient','C_i','G_i','G_i','G: the rounded capital has an inward horizontal stroke and short right upright, distinguishing G from open C.','high',True,False,'misread symbol or index','The majorant coefficient is G_i.')
a('majorant coefficient, lambda ellipsis','two dots','three dots','three dots','ellipsis: three separate round impressions occur between the two commas.','high',True,False,'omission')
a('final coefficient alphabet','unsure blackboard H/plain H','H','H','H: both stems have the hollow typewriter impression seen in neighbouring typed capitals; no separate pen-drawn doubling is present.','medium',True,False,'misread symbol or index')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 24 -','typewriter')
i('display','equation (16), handwritten brace','m-1=n+double sum s_kj; mu_l=lambda/Lambda_l+double sum nu_kj; bounds')
i('text','between displays','On tire de ces conditions que','typewriter')
i('display','total-degree identity','m+sum mu_l=1+n+sum lambda_l+double sum(s_kj+sum nu_kjl)')
i('text','degree comparison and uniqueness','et par suite … (16) … caractéristique 0 … equations (15) … de fa-çon unique …')
i('text','summability requirement','En outre … pourvu qu’elles soient sommables dans unvoisina-ge de l’origine … K^(q+1) ; .')
i('text','substitution argument','En effet … voisina ge … U times W … soit contenue dans P … §1,th.2 … U in W.')
i('text','majorant construction opening','Pour prouver la somm bilité … G_i(n;r1,..,rp;lambda1,...,lambdaq) … H_i(m;mu1,...,muq) par les conditions')
commit(15,43,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves personally read before C1 and C2. Every display, formula-bearing prose band and disputed token enlarged. Contenue was separately checked and retained. The punctuation ; . and the literal domain U in W remain. No H text, cancellations or marginal notes. The opening brace is a handwritten completion. No context consulted.'))
