import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{9}',r'\mspage{\handwritten{- 9 -}}'),(r'$2^{\mathrm{o}}$',r'$\handwritten{2^{\mathrm{o}}}$'),(r'\uline{4}.',r'\uline{\handwritten{4}}.'),(r'\unsure{K|\mathbb{K}}','K'),(r'\unsure{E|\mathbb{E}}','E')]
L=[]
def a(p,c,f,s,v='high',C=True,k='other'):
 L.append(dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable'))
a('original page number','9','handwritten - 9 -','header, upright: two blue pen dashes flank a looped 9 whose curved descending stroke is continuous.',k='omission')
a('opening continuation, second alternative','2 raised o without handwriting mark','handwritten 2 raised o','ordinal, upright: both the irregular curved numeral and its elevated round loop are in pen, unlike the neighbouring type impressions.')
a('opening continuation, substituted series','unsure gamma/y','unsure gamma/y retained','gamma, upright: two upper arms meet a short descending stroke; the left arm has a small hook. This is compatible with gamma but does not securely exclude y.','low',False)
a('section heading','4 without handwriting mark','handwritten 4','section4, upright: a sloping pen stroke, irregular crossbar and long descending upright form the numeral.')
a('proposition 4, first coefficient','unsure c/C','unsure c/C retained','c and prop4a, upright: the open rounded pen letter has no case-specific feature; neighbouring handwritten letters do not settle its height.','low',False)
a('definition 2, field','unsure K/blackboard K','K','K, upright: a single serifed typewriter upright and two diagonal arms, without an added second stem.',k='misread symbol or index')
a('definition 2, target space','unsure E/blackboard E','E','E, upright: the serifed typewriter impression has one upright and three horizontal arms; no extra upright is present.',k='misread symbol or index')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upright top centre','- 9 -','unnamed hand')
i('text','opening continuation','des séries entières g_k … deuxième substitution … gamma/y_j … u1,…,uq')
i('text','section heading','4. La notion de fonction holomorphe')
i('text','proposition introduction','Le th.2 entraîne en particulier la proposition suivante :','typewriter')
i('text','proposition 4','f(z1,…,zp) … c/C coefficients … P … |z_k|<r_k … polynomes a_k+u_k … f(a1+u1,…,ap+up)')
i('text','proof','En effet … h_k(|u1|,…,|up|)==|a_k|+|u_k|<r_k par hypothèse')
i('text','reformulation','En d’autres termes … centre (a1,…,ap) … série entière … z_k-a_k')
i('text','definition 2','A … K^p … application f de A dans E … fonction holomorphe … série entière absolument sommable')
i('text','transition','La prop.4 montre donc que :','typewriter')
i('text','proposition 5 opening','Si une série entière … z_k … sommable … centre 0,')
commit(15,57,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both raw halves personally viewed, then the whole and halves upright before C. All prose and mathematical bands enlarged; every C doubt and the handwritten header and section numeral separately enlarged. Gamma/y and c/C remain unresolved. The two equals signs across the proof line break, polynomes without accent, punctuation and underlining are retained as visible. No marginal writing, deletion or insertion. H absent; no context consulted.'))
