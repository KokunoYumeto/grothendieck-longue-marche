import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{23}',r'\mspage{- 23 -}'),(r'\unsure{g|e|c}',r'g'),(r'\unsure{\lambda|\Lambda}',r'\lambda'),(r'\unsure{\nu|v}',r'\nu'),(r'\sum_{n,(r_j),(\lambda_\ell)}}g_i',r'\sum_{n,(r_j),(\lambda_\ell)}}\unsure{g|G}_i'),('satisfaisant aux conditions',r'satisfaisa\handwritten{-}nt aux conditions')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','23','- 23 -','- 23 -','header: horizontal blue dashes flank the numeral.','high',True,False,'omission')
a('equation (14), coefficient','unsure g/e/c','g','g','g1: the typed letter has a small upper bowl and a separate lower loop, distinguishing g from e or c.','high',True,False,'misread symbol or index')
a('equation (14), first lambda','unsure lambda/Lambda','unsure lambda/Lambda','lambda','lambda: the right stroke extends well above the point where the left diagonal joins it, giving a lower-case lambda with an ascender.','high',True,True,'misread symbol or index')
a('sommables dans un …','polydylindre','polycylindre','polydylindre','polydylindre: the letter after poly has a closed bowl and a full tall right ascender; it is the typed d.','high',False,True,'misread word')
a('equation (15), coefficient','g_i','unsure G/g_i','unsure g/G_i','g2: the upper lobe and lower rounded part favour g, but the very faint link between them does not securely exclude capital G.','low',True,True,'misread symbol or index')
a('equation (15), first nu','unsure nu/v','nu','nu','nu: the right stroke rises and hooks back left while the left stroke is short, matching the other nu forms; it is not a straight v.','high',True,False,'misread symbol or index')
a('last word before aux conditions','satisfaisant','satisfaisant','satisfaisa-nt with handwritten internal hyphen','sa_nt: a rising blue joining stroke lies between a and n in the last line; the line-break hyphen after satisfai is separate and only wraps the word.','high',True,True,'omission')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 23 -','typewriter')
i('display','equation (12)','D u_i(x;z1,..,zq)=f_i(x;u1(…),..,up(…);z1,..,zq)','typewriter')
i('text','below (12)','(D dérivation par rapport à x, 1<=i<=p) et')
i('display','equation (13)','u_i(a;z1,..,zq)=b_i; bounds; pour tout (z1,..,zq) in W')
i('text','translation paragraph','Par translation … a=b_j=c_k=0 … B times P times Q … subsets of K, K^p, K^q')
i('display','equation (14), two lines','f_i= sum g_i(n;r1,..,rp;lambda1,..,lambdaq) . . x^n y1^r1 … zq^lambdaq .')
i('text','existence introduction','Pour établir l’existence … sans terme indépendant de x','typewriter')
i('display','candidate solution series','u_i(x;z1,..,zq)=sum h_i(m;mu1,..,muq)x^m z1^mu1 … zq^muq')
i('text','substitution and coefficient comparison','sommables dans un polydylindre … (14), (12) … mêmes coefficients …')
i('display','equation (15), right handwritten brace','h_i(0;…)=0; m h_i(m;…)=sum (g/G)_i(…) . . double product h_i(s_kj;nu_kj1,…,nu_kjq)')
i('text','bottom summation conditions','pour tout entier m>0 … mu_l>=0 … systèmes … satisfaisa-nt aux conditions')
commit(15,45,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves personally read before C1/C2, then all formula-bearing blocks and disputed characters enlarged. The final product factor is literally h_i; no expected-index correction made. The large closing brace is handwritten. The duplicated multiplication dots at line breaks are retained. No H text, marginal notes or cancellations. No context consulted.'))
