from workflow import *
n=358
boxes=dict(K_form=(727,197,924,281),ticks=(1506,971,1565,1012),cancel_g=(497,1204,916,1474))
cp=lambda k:f'scan 358 {k} {boxes[k]}'
choices=[]
for j in range(10):
 choices.append(('K','Short upright with flattened upper arm and detached curved lower arm; the same form is confirmed in all ten occurrences. Its role in NK(Z,i)=Z[i] and the preceding normalization notation supports K rather than a change to kappa.',cp('K_form') if j==0 else 'page','medium'))
t,ds=resolve(n,choices)
t=repl(t,r'''\overset{\text{''}}{\otimes}''',r'\overset{\Vert}{\otimes}')
t=t.replace(r'\unsure{g|\mathfrak g}',r'g')
# Reproduce the actual crossed-out multi-line diagram in TikZ: the diagonal strokes are its deletion.
a0=t.index(r'\deleted{\diagram{')
b0=t.index(r'\mspage{359}')
t=t[:a0]+r'''% Deleted block: the two large diagonal strokes cross the entire parenthesized diagram.
\figure{\begin{tikzpicture}
\node(a) at (0,1) {$\operatorname{Inv}^G(Sg^*)$};
\node(b) at (0,0) {$H^*(G,L\operatorname{Sym}g^*)$};
\node(c) at (4,.65) {$H^*(BG)$};
\node at (-2,.5) {$\Bigg($};\node at (5.2,.65) {$\Bigg)$};
\draw[double,->](1.8,.45)--(2.8,.6);
\draw(-1.2,2.1) .. controls (0,1.8) and (3.7,-.5) .. (4.6,-.55);
\draw(-.5,-.9)--(4.5,2.35);
\end{tikzpicture}}
''' +t[b0:]
cc=[]
def a(place,c,h,f,ink,kind='other',dc=False,dh=True,k=None,conf='high',cons=False):
 cc.append(change(place,c,h,f,ink,kind,dc,dh,conf,cp(k) if k else 'page','no',cons))
a('first target closing','no closing parenthesis','closed K(Z,i+j)','no closing parenthesis','The ink ends after j; no closing curve follows.','text not on the page')
a('first diagram arrangement','triangle, one upper target','linearized with target repeated','triangle, one upper target','The product maps down to the tensor, and the oblique f arrow rises to the single upper target.','drawing or diagram')
a('integer alphabet throughout','plain Z','blackboard Z','plain Z','Crossed single-stroke Z forms occur; no doubled diagonal is written.','misread symbol or index',conf='medium')
a('second diagram source parenthesis','one missing outer close; isolated dot','both parentheses closed; dot omitted','one missing outer close; isolated dot','Only one closing curve follows j. A small isolated ink dot stands to the right of the source.','text not on the page')
a('E.Z. arrow label','E.Z.','E-Z','E.Z.','Low stops follow both capitals; there is no hyphen.','abbreviation expanded or spelling modernised')
a('vertical relation over tensor','two apostrophe marks','baseline equality','paired vertical equality strokes','The two short strokes are written between the two rows, above the lower tensor, rather than as baseline punctuation.','misread symbol or index',dc=True,k='ticks',conf='medium',cons=True)
a('cancelled g alphabet, both occurrences','g or fraktur g','fraktur g','ordinary g','Both letters have a small upper loop and long descending return; no distinct fraktur construction is present.','misread symbol or index',k='cancel_g',conf='medium')
a('cancelled block layout','two left rows, outer parentheses around diagram','comma-separated left pair, arrow outside pair parentheses','two left rows, arrow and target all inside large parentheses','The large right parenthesis lies beyond H*(BG), and the two left formulas are vertically stacked.','insertion or placement')
a('large cancellation geometry','generic deletion wrapper','cross described in note','two long crossing diagonal strokes across entire block','Two large diagonals extend beyond the parenthesized formulas; the double implication remains visible underneath.','drawing or diagram',dc=True,conf='high')
items=[inv('diagram','top','K(Z,i) times K(Z,j), tensor below, oblique f'),inv('text','below top triangle','Il suffit de construire Nf'),inv('diagram','middle','N of tensor through E.Z. to NK tensor NK and NK(Z,i+j)'),inv('text','right of second source','isolated dot'),inv('display','under middle tensor','vertical equality; Z[i] tensor Z[j]'),inv('diagram','lower ink block','Inv^G(Sg*) and H*(G,L Sym g*) imply H*(BG)'),inv('deletion','across lower ink block','two large diagonal cancellation strokes'),inv('text','foot','359')]
notes="This short continuation constructs the product K(Z,i) times K(Z,j) to K(Z,i+j) by passing through a tensor product and says Il suffit de construire Nf. The next diagram applies an E.Z. map to normalized complexes and identifies their tensor with Z[i] tensor Z[j]. The K-shaped glyph has a flattened arm and may resemble kappa in isolation; all ten occurrences match, and the displayed NK(Z,i)=Z[i] role supports reading the same K throughout. This use of notation is recorded rather than relying on witness agreement. The top target lacks its closing parenthesis, and the normalized-tensor source lacks one outer close. The paired vertical relation is not quotation punctuation. Conditional on the displayed normalization identifications, the tensor of free rank-one complexes concentrated in degrees i and j is free rank one in degree i+j, with zero differential; this checks the final complex-level target only, not the existence or coherence of the simplicial product. A separate parenthesized block with invariant polynomials, derived symmetric powers and H*(BG) is crossed out in its entirety; no claim about it is proved. Almost the entire lower half is blank apart from faint reverse impressions and foot359. No date."
# Syntax only: delimit control words before the following letters.
t = t.replace('\\timesK', '\\times K').replace('\\otimesK', '\\otimes K')
commit(n,t,ds,cc,items,notes,hand=['Short K has a flattened upper arm and a separately drawn curved lower arm. All ten examples on this page are read consistently as K, at medium confidence, using their normalization role.','Paired upright strokes between displayed rows function as a vertical relation, not textual quotation marks.','Both g letters in the crossed-out block have the same ordinary loop and long descender.'],notation=[('K(Z,i)','Ten repeated short K forms; NK identified with Z[i].'),('vertical equality','Paired upright strokes over the lower tensor.'),('Z','Single crossed handwritten Z, not an imposed blackboard alphabet.'),('g*','Ordinary looped g with raised star in both cancelled formulas.')],abbr=[('E.Z.','Eilenberg-Zilber'),('Inv','invariants'),('Sym','symétrique')],checks=[check('358.tensor-of-concentrated-complexes','Under the displayed identifications, Z[i] tensor Z[j] has its sole nonzero group Z in degree i+j and zero differential. This validates only the last target, not the full simplicial construction.','targeted proof check')])
