import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{12}',r'\mspage{\handwritten{- 12 -}}'),(r'coeffici\handwritten{\`}{e}nts','coefficients'),(r'\unsure{K|\mathbb{K}}','K'),(r"$\unsure{'} étant",'$ étant'),('la série de terme général,','la série de terme général'),(r'\handwritten{\beta}>0',r'\handwritten{\beta>}0'),(r'\handwritten{\varepsilon}>0',r'\handwritten{\varepsilon>}0')]
L=[]
def a(p,c,f,s,v='high',C=True,k='other'):
 L.append(dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable'))
a('original page number','12','handwritten - 12 -','header, upright: blue dashes flank the two irregular pen numerals.',k='omission')
a('first coefficient','unsure c/C','unsure c/C','c and top, upright: a rounded open curve with an inward top terminal is clear, but its height does not securely distinguish lower from upper case.','low',False,'misread symbol or index')
a('first occurrence of coefficients','coefficiènts, added handwritten grave','coefficients','accent, upright: the diagonal above e is a tan pointed fibre with a dark edge, unlike the blue letter; no separate blue grave stroke.',k='text not on the page')
a('En outre, on a, dans K','unsure K/blackboard K','K','K, upright: the regular serifed typewriter K has one upright and no added parallel stem.',k='misread symbol or index')
a('two strict inequalities beta>0 and epsilon>0','greater signs unmarked as hand','greater signs handwritten','series and prop, upright: both open angles have continuous blue strokes and irregular widths, unlike the typed zeroes beside them.',k='other')
a('first série de terme général','général,','général','general_comma, upright: a tan elongated fleck occupies the apparent comma position; it contains no blue ink.',k='text not on the page')
a('proof, after f(z1,..,zp)','uncertain apostrophe','no apostrophe','prime, upright: the small mark beside the parenthesis is brown and isolated; the parenthesis itself is blue.','high',True,'text not on the page')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upright top centre','- 12 -','unnamed hand')
i('text','opening paragraph','En effet … c/C_k;… … coefficients b … n_k b= c … doubled not-equal at line break … b_00..0=c … façon unique')
i('text','bound paragraph','En outre … dans K … |1/n|<=n^beta … dans blackboard R … terme général')
i('display','weighted general term','((n1+1)(n2+1)..(np+1))^beta ||a_n1n2..np|| r1^n1 r2^n2 … rp^np')
i('text','between general terms','converge en même temps que la série de terme général','typewriter')
i('display','unweighted general term','||a_n1..np|| r1^n1 r2^n2 … rp^np .')
i('text','proposition 8','Soit f(z1,..,zp) … A … point a … epsilon>0 … P_o … tout couple de points …')
i('display','equation (6)','||f(u)-f(v)-sum D_k f(a)(u_k-v_k)|| <= epsilon.sup |u_k-v_k|')
i('text','proof first part','On peut se ramener au cas où a est l’origine … série entière … Q … th.2 … polynome u_k+w_k')
i('text','proof final part','est substituable … P assez petit … P times P … 2p variables … théorème d’associativité … on peut donc écrire')
commit(15,53,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole image and supplied halves personally viewed, then upright whole and overlapping halves before C. All text/formula bands, doubts and possible extra marks enlarged. H has no text. Double-stroke R has parallel pen lines and is retained. P_o has a round small o; the final a_p in (6) has a left descender and right bowl. Literal polynome and duplicated not-equal at line break retained. No cancellations, margin notes or insertion. No context consulted.'))
