import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{44}',r'\mspage{\handwritten{- 44 -}}'),(r'\unsure{\varphi|\phi}',r'\varphi'),(r'\unsure{4}',r'\unsure{4|14}'),(r'\handwritten{\rho}>0',r'\handwritten{\rho>}0'),('et est $>0$','et est $\\handwritten{>}0$'),(r'\handwritten{\geq\rho}>0',r'\handwritten{\geq\rho>}0'),(r'\handwritten{\varepsilon}>0',r'\handwritten{\varepsilon>}0'),(r'$z_j-x_j$',r'$z_j-\handwritten{x}_j$'),(r'$|t-t\prime|',r'$|t-t\prime|')]
R=R[:-1]+[("$|t-t'|", "$\\handwritten{|}t-t'\\handwritten{|}"),("$|s-s'|", "$\\handwritten{|}s-s'\\handwritten{|}")]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','44','- 44 -','handwritten - 44 -','header: short dashes flank two open pen-drawn 4s.','high',True,True,'insertion or placement')
a('first coordinate difference','x_j-a_ij','unsure x/z_j-a_ij','x_j-a_ij','xj: the letter has crossed diagonals and four serif ends, rather than the parallel upper/lower strokes of z.','high',False,True,'misread symbol or index')
a('first deformation symbol','unsure varphi/phi','unsure varphi/phi','varphi','phi: the loop has a descending stem and no stem extending above its top, agreeing with the repeated loop form in the other occurrences on this sheet.','high',True,True,'misread symbol or index')
a('proposition reference','unsure 4','unsure 4/14','unsure 4/14','prop and reference_contrast: an open 4 is visible, with a faint preceding upright trace near the dot; show-through and pale ink prevent excluding 14.','low',True,False,'misread symbol or index')
a('handwritten formula completions','greater signs, absolute-value bars and second centre x not separately marked handwritten','these strokes marked handwritten','these strokes marked handwritten','greater, norms and series: the open chevrons and bars are irregular pen strokes; the x after z_j- has the same handwritten crossed form as the centres elsewhere, unlike the typed z.','high',True,False,'insertion or placement')
a('interpolation denominator','t_(alpha+1)-t','t_(alpha+1)-t','t_(alpha+1)-t retained literally','denominator: no subscript or other mark follows the final t. The numerator alone ends with t_alpha.','high')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 44 -','unnamed hand')
i('text','opening continuation','chacune des fonctions f_k … minimum rho … delta(x) >= rho > 0 …')
i('text','series and continuity','Par suite … chap.I, §1, prop.4/14 … continuité uniforme …')
i('display','continuity bound','|t-t prime| <= epsilon, |s-s prime| <= epsilon imply norm(phi(t,s)-phi(t prime,s prime)) <= rho/4')
i('text','partition choices','Soit (t_alpha) … soit de même (s_beta) … Désignons par gamma_beta …')
i('display','interpolation','gamma_beta(t)=phi(t_alpha,s_beta)+(t-t_alpha)/(t_(alpha+1)-t)(phi(t_(alpha+1),s_beta)-phi(t_alpha,s_beta)), bounds on t, alpha and beta')
i('text','endpoints and claim','on posera en outre gamma_0=gamma, gamma_q=gamma prime. Tout revient à prouver …')
i('display','split equality','integral_gamma_beta(sum f_k dx_k)= =integral_gamma_(beta+1)(sum f_k dx_k)')
i('text','last argument','Or, pour chaque indice alpha … Q_alpha,beta … fig.1 … existe dans Q_alphabeta')
commit(15,33,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole page then both halves inspected before C1/C2. Enlarged all prose and handwritten formulas, each differing or doubtful reading, and the literal denominator with its missing subscript. The two equals signs at the line break are retained. H absent; no collation rows. No context consulted.'))
