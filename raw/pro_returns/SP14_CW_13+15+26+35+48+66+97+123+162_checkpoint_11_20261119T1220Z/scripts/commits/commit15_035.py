import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{42}',r'\mspage{\handwritten{- 42 -}}'),(r'\unsure{\varphi|\phi}',r'\varphi'),(r'\handwritten{\unsure{\textasciigrave|\textbackslash}}',''),('un sens, puisque','un sens; puisque'),(r'\unsure{2|Z}','2'),('linéaire. par morceaux','linéaire par morceaux'),(r"nouveaux chemins $\handwritten{\gamma}'_1$, $\handwritten{\gamma}'_2$",r"nouveaux chemins $\handwritten{\gamma}'_1$\unsure{,|} $\handwritten{\gamma}'_2$")]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','42','- 42 =','handwritten - 42 -','header: a single blue dash is present on each side. The extra short mark above the right dash is tan paper material, not a second blue line.','high',True,True,'misread symbol or index')
a('first deformation symbol','unsure varphi/phi','unsure varphi/phi','varphi','phi: the rounded loop has a descending stem and no ascender; it matches the other varphi forms in the paragraph.','high',True,True,'misread symbol or index')
a('before I times J_1','uncertain grave/backslash','no mark','no textual mark','stray: the slanting mark is ochre-brown like the paper fibres, unlike all nearby blue typed and handwritten strokes.','high',True,False,'text not on the page')
a('parenthesis after sens','sens,','sens;','sens;','sens: a distinct upper dot sits above the lower comma-shaped impression.','high',True,False,'misread word')
a('ambient real space','blackboard R','unsure blackboard/plain R','blackboard R','R: the left stem is doubled with two separate parallel strokes, unlike the single strokes of the typed capitals.','high',False,True,'misread symbol or index')
a('pair of new paths in remark','gamma_1 prime, gamma_2 prime','gamma_1 prime gamma_2 prime','uncertain comma between the paths','pair: a faint short blue curved trace lies in the narrow gap, but its relation to the neighbouring pen strokes is not secure enough to choose comma or absence.','low',True,True)
a('large left-margin mark','unsure 2/Z','unsure 2/Z','2','margin, already upright: the upper stroke turns into a rounded right-hand curve before descending diagonally to the long lower foot, supporting 2.','high',True,True,'misread symbol or index')
a('proposition, after linéaire','linéaire. par','linéaire par','linéaire par','linear: the apparent point is a dark slanting speck with a tan halo just above the blue rule; it does not have the blue impression of the typewritten punctuation.','medium',True,False,'text not on the page')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 42 -','unnamed hand')
i('text','opening continuation','convenable s→s+a … function patched over J_1 union J_2 … relation d’équivalence …')
i('text','example','Exemple.- On dit qu’un domaine A subset blackboard R^n … étoilé …')
i('display','example deformation','varphi(t,s)=a+(1-s)(gamma(t)-a), 0<=s<=1')
i('text','remark','Remarque.- Si gamma est une juxta-position … il ne s’ensuit nullement …')
i('margin note','left beside remark, second half','2','unnamed hand')
i('text','proposition','PROPOSITION 1.- Tout chemin achevé … mêmes extrémités.')
i('text','proof start','En effet, soit gamma un chemin a chevé … distance rho … complement A … >0.')
commit(15,35,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole image and both halves read before the two C runs, all paragraphs and formula completions enlarged. The margin mark was already upright and was separately enlarged. Literal capital A in par rapport à A, juxta-position and a chevé retained. H absent. No context consulted.'))
