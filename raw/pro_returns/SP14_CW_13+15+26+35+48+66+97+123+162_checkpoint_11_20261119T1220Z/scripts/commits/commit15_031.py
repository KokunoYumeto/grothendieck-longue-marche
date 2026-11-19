import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{46}',r'\mspage{\handwritten{- 46 -}}')]
# The apostrophe is ordinary source punctuation, so replace its full short span.
R=R[:1]+[("\\uline{Alors, si l'expression différentielle}","\\uline{Alors}, \\uline{si l'expression différentielle}"),(r'\handwritten{\gamma}_o(t-',r'\handwritten{\gamma}_{\handwritten{\unsure{o|0|\circ}}}(t-'),(r'\handwritten{\gamma}^o$ défini',r'\handwritten{\gamma}^{\handwritten{\unsure{o|0|\circ}}}$ défini'),('un point est contractile\n','un point est contractile.\n'),(r'\handwritten{\alpha}$',r'\handwritten{\alpha}\unsure{)|))|}$'),('% The source leaves the space after I= blank. The right edge ends after alpha; no closing parentheses have been supplied.','% The source leaves the space after I= blank. At the right edge a faint arc may be one closing parenthesis; a second, or no intentional closing stroke, remains possible. Accents on DEFINITION and THEOREME are handwritten over the typed E letters.')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','46','- 46 -','handwritten - 46 -','header: both short dashes are present; the open 4 and looped 6 have pen-drawn contours.','medium',True,True,'insertion or placement')
a('corollary, Alors','Alors, si continuously underlined','Alors and si separately underlined','Alors, then si, comma outside the underline','Alors and corollary: the rule ends before the comma and resumes beneath si.','high',True)
a('first reversed route','gamma superscript unsure o/0/circle','same uncertainty','retained uncertainty o/0/circle','gamma and routes: the raised mark is a small unadorned closed round loop; its shape alone does not distinguish a letter o, zero or circular mark.','low')
a('route in translated parameter formula','gamma subscript o','gamma subscript unsure o/0','gamma subscript unsure o/0/circle','gamma_sub: the round loop lies below the baseline. It has the same undifferentiated circular form as the superscripts, and is not silently moved above.','low',True,True,'misread symbol or index')
a('repeated reversed route','gamma superscript o','gamma superscript o','gamma superscript unsure o/0/circle','routes: the repeated raised circle has no additional feature settling the same ambiguity; the uncertainty is carried consistently to this occurrence.','low',True,True,'misread symbol or index')
a('definition heading accent','unsure DÉFINITION/DÈFINITION','DÉFINITION, acute handwritten','retained unsure DÉFINITION/DÈFINITION; handwritten accent','def_accent: the short heavy mark above the E is almost vertical, with a blurred upper end. The direction is not securely distinguishable.','low',False,True,'misread word')
a('end of star-shaped example','no final period','final period','final period','last_point: a small coloured impression stands at the baseline beyond the e before the paper edge.','medium',True,False,'omission')
a('theorem heading accents','four acute/grave combinations','first acute; second grave/acute uncertain','four acute/grave combinations retained','th_accents: both short accents have nearly vertical stems and thickened upper ends. The first is no more securely acute than the second.','low',False,True,'misread word')
a('section number','unsure 3/2','3','unsure 3/2 retained','number: the upper and middle curvature favour 3, but the diagonal lower stroke and broad baseline can also belong to 2.','low',False,True,'misread symbol or index')
a('last formula, right edge','ends at alpha, no closing parentheses','uncertain one/two closing parentheses','uncertain one/two/no closing parentheses','edge, edge_full_contrast: a faint curved vertical trace follows alpha at the paper edge, but mottling and show-through prevent deciding its count or whether it is intentional text. No interval is supplied after the blank I=.','low',True,True,'misread symbol or index')
I=[]
def i(k,p,t,h='typewriter'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 46 -','unnamed hand')
i('text','corollary','COROLLAIRE.- Soient gamma et gamma prime … on a …','typewriter and unnamed hand')
i('display','corollary equality','integral_gamma(sum f_k dx_k)=integral_gamma_prime(sum f_k dx_k)','typewriter and unnamed hand')
i('text','proof of corollary','On peut supposer … gamma superscript circle … gamma subscript circle … aussitôt le corollaire.','typewriter and unnamed hand')
i('text','definition','DÉFINITION/DÈFINITION 5.- On dit qu’un domaine … en un point de A.','typewriter and unnamed hand')
i('insertion','definition heading','accent on first E','unnamed hand')
i('text','example','Par exemple, tout domaine étoilé … contractile.')
i('text','terminology','Une expression différentielle … dite fermée … On voit donc que :','typewriter and unnamed hand')
i('text','theorem','THÈORÈME and accent alternatives 2 (Cauchy).- … est nulle.')
i('insertion','theorem heading','accents on both E letters','unnamed hand')
i('text','indented question','On peut évidemment … continument différentiables ; est-ce que cela en vaut la peine ?','typewriter and unnamed hand')
i('text','section heading','3/2. Primitives d’une fonction holomorphe.','typewriter and unnamed hand')
i('text','last paragraph','Soit A subset K^n … route gamma définie dans I= [blank] …','typewriter and unnamed hand')
i('display','last line','integral_gamma dg=integral_gamma(sum f_k dx_k)=g(gamma(beta))-g(gamma(alpha [edge]','typewriter and unnamed hand')
commit(15,31,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole page then both halves personally read before both C runs. All prose, formula completions, underlines and C doubts enlarged. H absent, no H rows. No source gap has been completed from mathematics. No context consulted.'))
