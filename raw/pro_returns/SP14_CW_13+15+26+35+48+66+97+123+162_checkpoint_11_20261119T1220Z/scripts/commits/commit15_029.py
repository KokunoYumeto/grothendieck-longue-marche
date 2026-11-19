import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{47}',r'\mspage{\handwritten{- 47 -}}'),(r'\uline{il existe une route a-chevée linéaire par morceaux, contenue dans}',r'\uline{il existe une route a-chevée linéaire par morceaux}, \uline{contenue dans}'),('fermé. Or,','fermé. \\handwritten{O}r,'),(r'\unsure{a|z}=','a='),('du th.1.','du th.\\unsure{1|2}.')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','47','- 47 -','handwritten - 47 -','header: short strokes flank the two figures; the 4 and sloping 7 have irregular pen strokes, unlike the regular type impressions below.','medium',True,True,'insertion or placement')
a('lemma, underline boundary','morceaux, contenue in continuous underline','rule interrupted around comma','morceaux and contenue separately underlined; comma outside','lemma_rule and lemma: the rule beneath morceaux stops before the comma, with a new run under contenue.','high',True)
a('proof, Or','typed Or','handwritten O, typed r','handwritten O, typed r','Or: an irregular oval stands above and left of the regularly impressed typewriter r.','high',True,False,'insertion or placement')
a('closure of B','overline B','handwritten bar over typed B','overline B; bar handwritten, B typed','barB: the thick irregular horizontal line is separate from the serifed typewriter capital B. Rendering of the bar is unchanged; its origin is recorded in the inventory.','high',False,False)
a('inserted equality at foot','unsure a/z =','a=','inserted a=','a_insert: the inserted letter has a closed bowl and a right-hand downstroke; it is not an open zigzag z. The two equality strokes follow it above the line.','high',True,False,'misread symbol or index')
a('last theorem reference','th.1','th. unsure 1/2','th. unsure 1/2','th: a vertical stroke with a bottom foot favours 1, but additional curved and diagonal impressions prevent a secure exclusion of 2.','low',True,False,'misread symbol or index')
I=[]
def i(k,p,t,h='typewriter'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 47 -','unnamed hand')
i('text','opening continuation','en particulier integral_gamma dg=0 … circuit dans A.','typewriter and unnamed hand')
i('text','proposition','PROPOSITION 2.- Soit A subset K^n … dg=sum f_k dx_k.','typewriter and unnamed hand')
i('text','bridge','Nous utiliserons le lemme suivant :')
i('text','lemma','Lemme 1.- Quels que soient … a-chevée … extrémités a et b.','typewriter and unnamed hand')
i('text','proof, first part','Il suffit de prouver que l’ensemble B … donc S subset C … C est ouvert et fermé.','typewriter and unnamed hand')
i('insertion','initial of Or','O','unnamed hand')
i('insertion','above typed B in closure condition','overbar','unnamed hand')
i('text','proof, second part','Ce lemme étant démontré … On a integral_gamma = integral_gamma_prime.','typewriter and unnamed hand')
i('text','proof, last part','En effet … intervals [b,c], [c,d], [b,d] … circuit … th.1/2.','typewriter and unnamed hand')
i('insertion','last line, above equality','a=','unnamed hand')
commit(15,29,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves personally inspected before the two C runs; all text and all handwritten completions checked in enlarged blocks. H has no text and receives no collation rows. The source’s d’origine A, switch from B to C, a-chevée and juxta-position are retained literally. No context consulted.'))
