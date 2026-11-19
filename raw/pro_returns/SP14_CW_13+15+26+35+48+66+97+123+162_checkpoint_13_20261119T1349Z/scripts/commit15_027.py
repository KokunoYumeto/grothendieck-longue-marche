import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\mspage{\handwritten{48}}',r'\mspage{\handwritten{- 48 -}}'),(r'\unsure{même}',r'\unsure{nulle|même}'),(r'\unsure{P|p}','p')]
L=[]
def a(p,c1,c2,f,s,v='high',C=False,C2=False,k='other'):
 L.append(dict(place=p,c='C1: '+c1+'; C2: '+c2,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_c2=C2,against_h=False,marked_in_H='not applicable'))
a('original page number','48','- 48 -','- 48 -','header: a short horizontal dash stands on each side of the handwritten 48.','high',True)
a('first u/g equality, handwriting boundary','only u,z0,g,z0 marked handwritten','whole u(z0)=g(z0) marked handwritten','only handwritten letters and point symbols marked; typed delimiters/equality retained','top: the u, g and z marks have the variable pen strokes of the completions; the parentheses and equals have the regular pale typewriter impressions.','medium',False,True,'insertion or placement')
a('interval, handwriting boundary','0,1 typed; membership and brackets handwritten','whole membership and [0,1] handwritten','0,1 typed; membership and brackets handwritten','route: 0 and serif 1 have the uniform typed shapes and spacing; the enclosing brackets and membership sign have irregular pen strokes.','high',False,True,'insertion or placement')
a('cancelled word after est','unsure même','unsure nulle','unsure nulle/même, cancelled','old_word: about five typewriter positions and two taller middle strokes favour nulle; cancellation and a fold partly obscure the letters, so the alternative remains explicit.','low',True,True,'misread word')
a('first local-function index','unsure P/p','P','p','index: the bowl occupies the upper half of a lower-case p with a descending stem and bottom serif; compare the taller capital P elsewhere in the same paragraph.','high',True,True,'misread symbol or index')
a('underline after first local function','définie dans underlined; P outside','définie dans P underlined','définie dans underlined; P outside','defined: the underline stops after dans, leaving a clear gap before the typed P.','high',False,True)
a('local equality, handwriting boundary','u and x handwritten, Q/P and delimiters typed','whole u_Q(x)=u_P(x) handwritten','u and x handwritten, Q/P and delimiters typed','compatibility: the dark handwritten u and x contrast with the regular pale serif Q/P, parentheses and equals.','high',False,True,'insertion or placement')
a('last emphasis','enfin and si separately underlined','enfin, si continuously underlined','enfin and si separately underlined','finally: the first rule ends before the comma, and another begins beneath si; the intervening gap is clear.','high',False,True)
I=[]
def i(k,p,t,h='typewriter'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 48 -','unnamed hand')
i('text','first paragraph','L’élément … ce qui démontre la proposition.')
i('text','handwritten completions of first paragraph','integrals with gamma and sigma, sums indexed k, f, a, z, z0, g, u, membership signs','unnamed hand')
i('display','linear route','t→z0+t(z-z0), t in [0,1]','typewriter and unnamed hand')
i('display','primitive comparison','u(z)-u(z0)=integral_sigma(sum_k f_k dx_k)=g(z)-g(z0), g(z)=u(z)','typewriter and unnamed hand')
i('text','second paragraph','En particulier, si n=1 … A est connexe.')
i('text','handwritten completions in second paragraph','f, g, g1, g2 and inclusion in A subset K','unnamed hand')
i('deletion','fold at right in second paragraph','uncertain nulle/même')
i('text','third paragraph','Une variante de la démonstration du th.1 et de la prop.2 …')
i('text','underlined principle, first part','Etant donné un domaine A subset K^n … une fonction holomorphe u_p définie dans P')
i('text','underlined principle, compatibility clauses','on suppose que pour tout … on suppose en outre que si … enfin, si')
i('text','handwritten completions in principle','Phi, inclusion/membership/intersection signs, z, x and u','unnamed hand')
i('display','first compatibility equality','u_Q(x)=u_P(x)','typewriter and unnamed hand')
i('display','overlap condition','u_P(x)=u_Q(x), P cap Q','typewriter and unnamed hand')
commit(15,27,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole page then both halves personally inspected before both independent C runs. H has no text, so no H collation rows. Every paragraph, handwritten formula completion, index, underline and cancelled word was inspected in enlarged crops. The author of the typewritten analysis text and the completion hand is not identified from the scan. No context consulted.'))
