import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{10}',r'\mspage{\handwritten{- 10 -}}'),(r'\unsure{K|\mathbb{K}}','K'),(r'\unsure{E|\mathbb{E}}','E'),(r'\unsure{M|\mathbb{M}}','M'),(r'\uline{à valeurs \handwritten{/}dans}',r'\uline{à valeurs dans}'),(r'remarqu\unsure{er}','remarqu'),('Bornons-nous','% The right edge clips the first proof line after the visible letters remarqu.\nBornons-nous'),('de somme $s$,','de somme $S$,'),('existe.une',r'existe\handwritten{\unsure{.}}une')]
L=[]
def a(p,c,f,s,v='high',C=True,k='other'):
 L.append(dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable'))
a('original page number','10','handwritten - 10 -','header, upright: blue dashes and irregular pen numerals are present; the top of the zero is open.','medium',True,'omission')
a('proposition 6, first field','unsure K/blackboard K','K','K, upright: a single serifed typewriter upright and two arms; no added parallel stroke.',k='misread symbol or index')
a('proposition 6 bis, first Banach space','unsure E/blackboard E','E','E, upright: the hollow serifed type impression has one upright and three bars, without a second stem.',k='misread symbol or index')
a('proposition 6 bis, à valeurs … dans','handwritten slash','no slash','slash, upright: the diagonal is a dark-tipped tan fibre extending into a pale lower stalk; it is distinct from the blue writing.',k='text not on the page')
a('proof first line, right edge','remarqu plus uncertain er','remarqu; remainder clipped','edge, upright: the u reaches the physical right edge of the sheet; neither an e nor an r is visible beyond it. No completion supplied.',k='text not on the page')
a('proof, first sum','s','S','s_comparison, upright: the standalone typed S rises above and descends below the small s in somme; its cap-height curves are clear.',k='misread symbol or index')
a('proof, index set of second family','unsure M/blackboard M','M','M, upright: the double edges occur within the ordinary typewriter letter, with no extra handwritten vertical.',k='misread symbol or index')
a('proof, puisqu’il existe.une','certain point','uncertain point','dot, upright: a dense black round mark occurs at the baseline between the words. Its colour differs from the blue type, so punctuation versus foreign speck remains unsettled.','low',True,'other')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upright top centre','- 10 -','unnamed hand')
i('text','opening carried sentence','sa somme est une fonction holomorphe dans ce polycylindre.','typewriter and unnamed hand')
i('text','transition','De même, en vertu du cor. du th.2 :','typewriter')
i('text','proposition 6','Soit B … K^q … g_k … A … K^p … f(g1,…,gp) … holomorphe dans B')
i('text','explanatory paragraph','De façon imagée, toute fonction composée de fonctions holomorphes est holomorphe.')
i('text','proposition 6 bis','Soient E1,…,Er et F … application multilinéaire … [z1.z2…zr] … [f1.f2…fr] … valeurs dans F')
i('text','proof first line clipped right','Bornons-nous … r=2. Il suffit alors de remarqu','typewriter')
i('text','proof families and norm inequality','que si (x_lambda) … somme S … (y_mu) … somme t … [s.t] … existe [uncertain point] une constante k>0 … norm inequality')
i('text','proof conclusion','on appliquera cette remarque … f1 et f2 … point de A')
i('text','corollary','Soit f=(f1,…,fq) … A subset K^p … K^q … chacune des fonctions scalaires f_k … le soit')
commit(15,55,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both raw halves personally viewed, then whole and halves upright before C. All text/formula bands enlarged, plus every doubt, edge ending and suspected non-ink mark. No H text. The first typed sum is capital S while the later handwritten bracket contains a smaller s; this case difference is preserved. Underlining and product dots retained. No marginal notes, cancellations or insertions. No context consulted.'))
