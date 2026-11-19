import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{29}',r'\mspage{- 29 -}'),(r'&&&1\handwritten{\leq}j\handwritten{\leq}q)',r'&&&1\handwritten{\leq}j\handwritten{\leq}q'),(r'2^\circ',r'2^{\handwritten{\circ}}'),(r'$|t|<2$',r'$\handwritten{|}t\handwritten{|<}2$')]
# Replace the second sums of each display only; their lower handwritten index is ambiguous.
R += [(r'&=\frac{\handwritten{\partial}U_{ij}}{\handwritten{\partial}x_k}(\handwritten{x};\handwritten{u}(\handwritten{x}))+\handwritten{\sum_{h=1}^q}',r'&=\frac{\handwritten{\partial}U_{ij}}{\handwritten{\partial}x_k}(\handwritten{x};\handwritten{u}(\handwritten{x}))+\handwritten{\sum_{\unsure{k|h}=1}^q}'),(r'&=\frac{\handwritten{\partial}U_{kj}}{\handwritten{\partial}x_i}(\handwritten{x}_0;\handwritten{y}_0)+\handwritten{\sum_{h=1}^q}',r'&=\frac{\handwritten{\partial}U_{kj}}{\handwritten{\partial}x_i}(\handwritten{x}_0;\handwritten{y}_0)+\handwritten{\sum_{\unsure{k|h}=1}^q}')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','29','- 29 -','- 29 -','header: both blue horizontal dashes are visible beside the typewritten numeral.','high',True,False,'omission')
a('first numerator, u_j','u_j','unsure u/n','u_j','first_u: a left downstroke turns across the baseline and the right stroke rises separately, leaving the bowl open above; it is u.','high',False,True,'misread symbol or index')
a('first display, second summation index','h','unsure k/h','unsure k/h','sum_top and chain: the narrow looped upright has a short branching stroke to its right; k is stronger, but the joining strokes could form h.','low',True,False,'misread symbol or index')
a('first display, final closing parenthesis',')','none','none','edge: the q meets the cut right paper edge and no closing parenthesis survives.','high',True,False,'text not on the page')
a('Ecriva-nt, internal hyphen','handwritten hyphen','unmarked hyphen','handwritten hyphen','Ecriva: the sloping curved join between a and n is a pen stroke, unlike the level typewriter hyphens.','high',False,True,'insertion or placement')
a('mixed-derivative identity, second summation index','h','unsure k/h','unsure k/h','sum_middle: a tall loop and rightward branching strokes suggest k, but the right stroke is blurred enough to leave h possible.','low',True,False,'misread symbol or index')
a('mixed-derivative identity, final U index','jh','ih','jh','Uwide and Uih: the first subscript has a dot above a stem with a left-curving descender below the baseline; it is j, not i.','high',False,True,'misread symbol or index')
a('sufficiency label and holomorphy bound','superscript circle and absolute bars/chevron not marked handwritten','marked handwritten','handwritten circle and bars/chevron','order and solution: the oval and the tall bars/chevron have uneven pen contours; the typed t and 2 remain outside those spans.','high',True,False,'insertion or placement')
a('last numerator index','unsure n/h','h','unsure n/h','last_index: the short arched letter favours n; the faint upper left trace does not securely exclude an ascender of h.','low',False,True,'misread symbol or index')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 29 -','typewriter')
i('display','top, two equations and three bounds','mixed derivative chain rule; second sum index k/h; final bound at cut edge')
i('text','upper paragraph','Ecriva-nt que les expressions ainsi obtenues … tenant compte de (23) il vient')
i('display','middle, two lines','equality at (x0;y0), repeated equals; second sum index k/h; final U_jh')
i('text','below identity','Mais comme par hypothèse … on obtient bien (24).')
i('text','sufficiency heading','2° Les conditions sont suffisantes. Considérons …')
i('display','equation (25)',"y′=underlined U(x0+t(x-x0);y).(x-x0)")
i('text','construction paragraph','où U est la matrice … voisina ge … solution t une seule … v(0;x0,x,y0)=y0 …')
i('display','equation (26)','dv_j/dt=sum_i U_ij(…)(x_i-x_i0), bounds')
i('text','above final calculation','On déduit de là que','typewriter')
i('display','bottom, three lines','d/dt partial v_j/partial x_k … plus t sum_i … plus sum_i,h … partial v_(n/h)/partial x_k, bounds')
commit(15,39,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves read before both C runs; no H text. Each mathematical block and disputed index enlarged. Typed spacing voisina ge, solution t une seule, doubled equals and doubled plus at line breaks retained literally. Fraction bars are handwritten completions of the typescript; ordinary frac syntax represents them. No marginal additions or cancellations. No context consulted.'))
