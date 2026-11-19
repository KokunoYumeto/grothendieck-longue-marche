import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{21}',r'\mspage{- 21 -}'),(r'\unsure{M|\mathbb{M}}','M'),(r'\unsure{K|\mathbb{K}}','K'),(r'\unsure{\leq|=}','='),(r'\unsure{w|v}','w'),('§',r'\handwritten{\S}')]
L=[]
def a(p,c,f,s,v='high',C=True,k='other'):
 L.append(dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable'))
a('original page number','21','- 21 -','header: two horizontal blue dashes flank 21.',k='omission')
a('equation (9), numerator','unsure M/blackboard M','M','M and top: the double edges belong to the hollow typewriter impression and recur in the other M letters; no additional handwritten stem.',k='misread symbol or index')
a('uniqueness paragraph, first field','unsure K/blackboard K','K','K and unique: a single serifed stem and two diagonal arms form the typed K, without a parallel added stroke.',k='misread symbol or index')
a('on a nécessairement, relation','unsure <=/=','=','rel: two parallel horizontal impressions; the tan diagonal above the upper stroke is paper colour and is disconnected from it.',k='misread symbol or index')
a('after da ns','unsure handwritten dot','unsure handwritten dot','dot: a dark round mark is present at the baseline after s, near several dark fragments below the line. Its status as punctuation rather than a paper fragment remains uncertain.','low',False)
a('last display, second variable inside absolute bars','unsure w/v','w','w and end: two lower lobes and the central descending stroke support w; the right half is faint.','medium',True,'misread symbol or index')
a('three reference section signs','unmarked as hand','handwritten section signs','reference, unique and end: each section sign consists of a continuous pen loop, unlike the separate typed serif impressions beside it.',k='other')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 21 -','typewriter')
i('text','opening three lines','Tout revient donc à prouver … q séries entières … équations','typewriter')
i('display','equation (9)','v_k=M/((1-mu sum t_j)(1-mu sum v_i))-M-Mmu sum v_i; bounds')
i('text','after (9)','Or, on déduit aussitôt … (9) … v1=v sa tisfaisant à')
i('deletion','after aussitôt','que','typewriter, cancelled by unnamed hand')
i('insertion','above cancelled que','de','unnamed hand')
i('display','equation (10)','(1-q mu v)(1+qMmu)v=M/(1-mu sum t_j)-M(1-q mu v)')
i('text','before radical formula','et réciproquement ; or, la fonction v(t1,..,tp) … donnée par','typewriter')
i('display','radical solution','v(t1,..,tp)=1/(2qmu(1+qMmu)) [1-sqrt(…)]')
i('text','binomial-series paragraph','Comme la fonction (1-w)^(1/2) … sum binomial(1/2,n) v^n … centre (0,…,0)')
i('text','uniqueness introduction','Reste à montrer … w_i … fonctions continues … relations')
i('display','equation (11)','w_i=h_i0+sum h_i;n1..nq w1^n1 … wq^nq; bounds')
i('text','after (11)','dans un voisinage … u_i=w_i da ns [uncertain dot] un voisinage … prop.8 … (5) et (11)')
i('display','little-o relation','u_i-w_i=underlined o(sup |u_k-w_k|); bounds')
i('text','last paragraph','dans un voisinage de 0 … Fonct.var.réelle, chap.V, section 2 … complètement démontré.')
commit(15,49,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole page, both halves, then C personally read; H has no text. All text and formula bands enlarged, with close views for every C doubt and the cancellation/insertion. Literal sa tisfaisant, da ns and the v^n in the series of (1-w)^(1/2) retained. The underlined little o is visible. Dark fragments below the uniqueness paragraph are not additional readable writing. No context consulted.'))
