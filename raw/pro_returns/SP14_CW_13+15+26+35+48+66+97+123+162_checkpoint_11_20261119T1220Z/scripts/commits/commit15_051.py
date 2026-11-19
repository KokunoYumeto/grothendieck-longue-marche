import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{13}',r'\mspage{\handwritten{- 13 -}}'),(r'\unsure{M|\mathbb{M}}','M'),(r'\unsure{E|\mathbb{E}}','E'),(r'\unsure{K|\mathbb{K}}','K'),(r'\unsure{\smile}',r'\smile')]
L=[]
def a(p,c,f,s,v='high',C=True,k='other'):
 L.append(dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable'))
a('original page number','13','handwritten - 13 -','header, rotated 180 degrees: two short strokes flank 13; the numeral strokes have the irregular connected form of pen writing.',k='omission')
a('bound constant','unsure M/blackboard M','M','M and bounds, upright: the serifed type impression has hollow areas within the thick strokes; no separate added vertical line.',k='misread symbol or index')
a('mark beneath supremum index k','unsure smile-shaped arc','smile-shaped arc','smile, upright: a continuous blue line descends from the left, curves across the base, then rises right. Its shape is clear; no mathematical meaning is assigned to it.',k='misread symbol or index')
a('product space','unsure E/blackboard E','E','E and proof, upright: one serifed upright and three horizontal bars form the typed E, without an extra stem.',k='misread symbol or index')
a('point a belongs to K','unsure K/blackboard K','K','K and zero, upright: the letter has one typed upright and diagonal arms; no additional pen line supports a double-stroke alphabet.',k='misread symbol or index')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upright top centre','- 13 -','unnamed hand')
i('display','upright opening two lines','f(u1+w1,..,up+wp)=f(u1,..,up)+sum D_k f(0,..,0)w_k+sum f_k(…)w_k+ +sum b(…)u1^n1..up^np w1^m1 :..wp^mp')
i('text','below opening display','où les séries entières … sum m_k>=2 … |u_k|=|w_k|=r … M … t=sup_k |w_k|')
i('drawing','beneath supremum index k','shallow upward-facing arc, rendered by smile','unnamed hand')
i('display','middle two-line estimate','sum ||b(…)|| |u1^n1 … up^np w1^m1..wp^mp| <= <= Mt^2 sum (1/2)^(sum n_k)(t/r)^((sum m_k)-2)')
i('text','after estimate','Comme la série … formule (6) … continuité des séries entières.')
i('text','corollary','Toute fonction holomorphe dans A est indéfiniment différentiable dans A.')
i('text','corollary proof before display','En effet, la prop.8 … sa différentielle est l’application')
i('display','differential application','(u1,…,up) -> sum D_k f .u_k')
i('text','proof after display','qu’on peut identifier … espace produit E^p … prop.7 … indéfiniment différentiable')
i('text','last paragraph','Pour p=1 … a in K … zéro d’ordre h … Si K est de caractéristique 0, il est')
commit(15,51,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole image and both supplied halves viewed, then the whole and overlapping halves rotated 180 degrees before reading C. All text/formula bands and every doubt enlarged upright. No H text. The colon after w1^m1, duplicated plus and inequality at line breaks, arc under k, and page-ending incomplete sentence are retained. No cancellations or marginal notes. No context consulted.'))
