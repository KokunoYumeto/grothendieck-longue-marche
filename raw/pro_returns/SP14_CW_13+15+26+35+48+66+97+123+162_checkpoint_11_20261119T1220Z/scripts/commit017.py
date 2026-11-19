import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
(r'\unsure{\gamma|\mathscr{T}}',r'\unsure{\mathscr{J}|\mathcal{J}|\gamma}'),
(r'\gamma',r'\mathscr{J}'),
(r'\unsure{\mathscr{J}|\mathcal{J}|\mathscr{J}}',r'\unsure{\mathscr{J}|\mathcal{J}|\gamma}'),
(r'propert\deleted{\unsure{ies|y}}y',r'propert\deleted{ies}y'),
(r'\deleted{\unsure{\mathbb{Q}|\mathbb{R}}}\unsure{\mathbb{R}|\mathbb{Q}}',r'\deleted{\unsure{\mathbb{Q}|\mathbb{R}}}\mathbb{R}'),
(r'\unsure{riemanian|riemannian}',r'riemanian'),
(r'\unsure{homogeneous|homogenous}',r'homogeneous'),
(r'\unsure{univ.|univ-}',r'univ.'),
(r'\deleted{\unsure{is}}',r'\deleted{is}'),
(r'\deleted{\unsure{as|so}}',r'\deleted{as}'),
(r'\text{\unsure{élat.|élém.} \unsure{aut.|ant.}}',r'\text{int. aut.}'),
(r'),\unsure{.|{}}',r'),.'),
(r'\deleted{\unsure{picture|pictures}}',r'\deleted{picture}')]
L=[]
def a(p,c,h,f,s,k='other',v='high',C=False,H=True,m='no',q=None):
 d=dict(place=p,c=c,h=h,final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=H,marked_in_H=m)
 if q:d['consequential']=q
 L.append(d)
a('period-domain glyph throughout',r'\gamma; \unsure{\gamma|\mathscr T}',r'\mathcal J',r'\unsure{\mathscr J|\mathcal J|\gamma}, then \mathscr J','upper, Gamma, modular and side_full_rotated: two upper branches and descending loop agree with the earlier glyph; alphabet remains explicit uncertainty.','misread symbol or index','medium',True,False)
a('universal property',r'propert\deleted{\unsure{ies|y}}y','properties,',r'propert\deleted{ies}y','cancelled_top: terminal ies crossed by dark retracing, descending y retained; no comma after word.','deletion state (struck given live or live given struck)',C=True)
a('before representing',r'\deleted{\unsure{being}}',r'\struck{\ill{}}',r'\deleted{\unsure{being}}','cancelled_top: b-like beginning and descender survive oblique cancellation; interior still not secure.','readable ink left as \\ill{}','medium',m='yes')
a('functor specification',r'\inserted{F(X), X \deleted{\unsure{al|an}}complex analytic,}',r'F(X), X \struck{complex analytic}',r'\inserted{F(X), X \deleted{\unsure{al|an}}complex analytic,}','upper/cancelled_top: bracket attaches entire interlinear specification after functor; complex analytic is live, short cancelled prefix remains ambiguous.','deletion state (struck given live or live given struck)','medium',q='The inserted analytic parameter specification is live, not withdrawn.')
a('should define','should define',r'should \struck{\ill{}} define','should define','upper: line break between should and define; no intervening cancelled word.','text not on the page',m='yes')
a('multiplicative way','way for varying','way, for varying','way for varying','upper: no comma between way and for.','other')
a('Hodge-structure family',r'\inserted{\unsure{\mathscr V|V}}','V',r'\inserted{\unsure{\mathscr V|V}}','upper: looped V placed above the line between structure and over; script/plain distinction retained.','insertion or placement','medium')
a('group leaving V_0 fixed',r'G(\deleted{\unsure{Q|R}}\unsure{R|Q})','G(Q)',r'G(\deleted{\unsure{Q|R}}R)','Gamma: overwritten rounded base remains ambiguous; later right descending leg makes live R.','misread symbol or index','medium',True,True,q='The live field in the stabilizer sentence is R over an overwritten earlier character, not the clean Q of H.')
a('pair acted on',r'(\mathscr V,\gamma)',r'(V,\mathcal J)',r'(\mathscr V,\mathscr J)','Gamma: V has looped left stroke and curled upper right ending, matching the inserted family symbol.','misread symbol or index','medium')
a('side note spelling',r'\unsure{riemanian|riemannian}','riemannian','riemanian','side_full_rotated: riema- at line end and nian on the next line; only one n at the join.','abbreviation expanded or spelling modernised',C=True)
a('side note homogeneous',r'\unsure{homogeneous|homogenous}','homogeneous','homogeneous','side_full_rotated: small e before the final ous visible.','other',C=True,H=False)
a('side note covering',r'\unsure{univ.|univ-}','univ.','univ.','side_full_rotated: low dot after v; no hyphen.','other',C=True,H=False)
a('side note ending','freely','freely.','freely','side_full_rotated: writing reaches sheet edge; no final period visible.','other','medium')
a('after pair acted on','no additional sentence','J expects to carry algebraic (and usually,Z) structures.','no additional sentence','Gamma/modular: blank interparagraph space followed immediately by The modular varieties; this sentence is absent.','text not on the page')
a('modular-variety opening','The modular varieties I expect to carry algebraic structure... over Q (and morally,Z)','The modular varieties one gets from consideration of Hodge-structures over Q','The modular varieties I expect to carry algebraic structure... over Q (and morally,Z)','modular: I expect to carry algebraic and parenthetical and morally are plainly present.','misread word',q='H replaces an explicit expectation with different prose and loses the qualification morally.')
a('structure ending',r'structure\deleted{\unsure{s}}\unsure{{}|s}','structures (in invented preceding sentence)',r'structure\deleted{\unsure{s}}\unsure{{}|s}','structure: compact cancellation after e; possible surviving s cannot be separated securely from retracing.','deletion state (struck given live or live given struck)','low',False,True)
a('quotient emphasis',r'\boxed{J/\Gamma}','display J/Gamma',r'\boxed{\mathscr J/\Gamma}','modular: four sides of the handwritten box enclose the quotient.','drawing or diagram')
a('real-field exponent',r'G(R^{\unsure{0|\circ}})',r'G(R^\circ)',r'G(R^{\unsure{0|\circ}})','modular: small oval is inside the closing parenthesis, at upper right of R; zero/circle shape not separable.','misread symbol or index','medium')
a('after intersection',r'\deleted{\unsure{is}} is','is',r'\deleted{is} is','modular: small crossed is before separate live is.','omission',C=True)
a('for some matrix','for some matrix',r'for some \struck{\ill{}} matrix','for some matrix','lower: continuous unstruck for some matrix; no cancelled intervening word.','text not on the page',m='yes')
a('before giving',r'\deleted{\unsure{as|so}}',r'\struck{\ill{}}',r'\deleted{as}','lower: crossed a loop then s, not so; letters still discernible.','readable ink left as \\ill{}',C=True,m='yes')
a('Frobenius quotation','``Frobenius elements\'\'','guillemets','``Frobenius elements\'\'','lower/frobenius: paired short high strokes, not angular guillemets.','other')
a('Frobenius cancellation and membership',r'\deleted{\unsure{G(Q)|G}}\in\unsure{.|{}} I(Q)',r'\struck{\ill{}} I(Q)',r'\deleted{\unsure{G(Q)|G}}\in\unsure{.|{}} I(Q)','frobenius: cancelled G-like round stroke followed by dark diagonals; live epsilon-shaped membership stroke and possible dot before I; cancellation cannot be securely expanded.','omission','low',m='yes',q='The live membership sign before I(Q) and the overwritten expression are retained.')
a('definition of I',r'G/\text{\unsure{élat.|élém.} \unsure{aut.|ant.}}',r'G/\text{int. aut.}',r'G/\text{int. aut.}','frobenius: dotted i, compact n, tall crossed t, then aut. with u bowl and terminal t.','misread word',C=True,H=False)
a('punctuation after arithmetic condition',r'),\unsure{.|{}}','),','),.','frobenius: low comma after closing parenthesis, separate round dot to its right.','other','medium',True)
a('geometric condition','or geometric','or a geometric','or geometric','bottom: no a between or and geometric.','text not on the page')
a('inserted real-group restriction',r'\inserted{on G_R}',r'\add{(on G_R)}',r'\inserted{on G_R}','bottom: curved insertion bracket below the above-line on G_R; not a pair of text parentheses.','insertion or placement')
a('such as','such as:',r'much \ill{} :','such as:','bottom: s initial, tall h, separate as, two-dot colon.','readable ink left as \\ill{}',m='yes')
a('cancelled picture',r'\deleted{\unsure{picture|pictures}}',r'\struck{picture}',r'\deleted{picture}','bottom: e followed directly by comma after cancellation; no additional s.','other',C=True,H=False)
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','top','and assumes ... operates on (V,J).')
i('insertion','line 2','homothety')
i('deletion','universal property','ies')
i('deletion','before representing','being (uncertain)')
i('insertion','after functor','F(X), X ... complex analytic,')
i('deletion','within inserted specification','al/an')
i('insertion','after every V','as above')
i('insertion','after Hodge-structure','script V')
i('deletion','stabilizer field','overwritten Q/R before live R')
i('marginnote','left, rotated -90 degrees','Note that in general J ... if Gamma operates freely')
i('text','middle to bottom','The modular varieties ... if J/Gamma has')
i('deletion','structure ending','cancelled s, possible remaining s')
i('display','inside modular paragraph','boxed J/Gamma; Gamma subset G(Q) cap G(R^0)')
i('deletion','after intersection','is')
i('deletion','before giving','as')
i('deletion','Frobenius condition','G(Q)/G overwritten')
i('insertion','above geometric','on G_R')
i('deletion','general picture','picture')
i('insertion','above picture','description')
commit(13,17,dict(replace=R,changes=L,inventory=I,sheet_kind='letter',observations='Whole page and both supplied halves read; upper, Gamma, modular, lower, bottom, cancelled_top, structure, frobenius crops and full sideways note rotated upright inspected. All C doubts individually retained or resolved; no mathematical claim checked.'))
