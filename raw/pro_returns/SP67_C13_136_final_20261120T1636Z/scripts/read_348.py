from workflow import *
n=348
boxes=dict(augmentation=(38,302,403,466),complex=(477,296,1110,368),bilin_trial=(486,524,662,571),conditions=(242,797,981,883),nulle=(777,1071,1126,1143),donc_trial=(290,1070,400,1121),si_deux=(1303,1111,1632,1194),deleted_sections=(486,1510,1635,1598),square=(300,1645,1217,1891),derivative_margin=(1218,1697,1656,1817),cancel_paragraph=(326,1885,1609,2041),NB_intro=(337,2014,1597,2112),NB_hom=(341,2095,1620,2202),NB_wish=(348,2177,1621,2259),NB_end=(347,2247,1634,2325))
cp=lambda k:f'scan 348 {k} {boxes[k]}'
def c(r,e,k=None,conf='high'):return (r,e,cp(k) if k else 'page',conf)
choices=[c('Topos','Capital T, followed by opos.'),c(r'\mathcal X','Two crossing curves; not the cap and stem of T.'),c("ou, il suffit qu'il y ait une augmentation",'Three slanted marginal lines; suffit, ait and augmentation can be followed through the pale strokes.','augmentation','medium'),c(r'\unsure{\cdots|0}','Several faint traces precede the first connector; neither a definite closed zero nor a single dash is secure.','complex','low'),c('-','A single short continuation stroke after the last arrow.','complex'),c('aux conditions','The first group ends in x; the next begins con-, not rel-.','conditions','medium'),c('Donc','Capital D followed by onc; no apostrophe.'),c('nulle','Two tall l strokes and a final small e.','nulle','medium'),c('si deux','Dotted short i followed by a looped d and eux.','si_deux','medium'),c('bilin.','Short form ending in a dot, not the expanded adjective.'),c(r'Z^i\times Z^j','Two Z forms with a cross between them above the cancelled source.','square','medium'),c('rendant le carré suivant commutatif','The pale line above the square has the successive word groups; commutatif ends with an upright f.','square','medium'),c(r'd(x^i\circ z^j)=dx^i\circ z^j','Initial d and parenthesis; both occurrences of x have raised i; small circles between x and z.','derivative_margin','medium')]
t,ds=resolve(n,choices)
t=repl(t,r'\deleted{\unsure{bilin.}}',r'\deleted{bilin.}')
t=repl(t,r'\deleted{\unsure{donc}}',r'\deleted{donc}')
t=repl(t,r'''\deleted{\diagram{\begin{tikzcd}
C^{i-1}\times Z^j\arrow[r,"h_{ij}"] & C^{i+j-1}
\end{tikzcd}}}
\inserted{$Z^i\times Z^j$}''',r'''\diagram{\begin{tikzcd}
\inserted{Z^i\times Z^j} & \\
\deleted{C^{i-1}\times Z^j}\arrow[r,"h_{ij}"] & C^{i+j-1}
\end{tikzcd}}''')
t=repl(t,r'\unsure{B^i|Z^i}',r'B^i')
t=repl(t,r'''\arrow[r,"h_{ij}"']''',r'''\arrow[r,"\unsure{h_{ij}|b_{ij}}"']''')
# The square has a very faint, open-topped enclosing stroke. Its three sides
# are kept separately from the arrows, without manufacturing a top edge.
old=r'''\diagram{\begin{tikzcd}
B^i\times Z^j\arrow[r] & Z^{i+j}\\
C^{i-1}\times Z^j\arrow[u,"d\times\mathrm{id}"]\arrow[r,"\unsure{h_{ij}|b_{ij}}"'] & C^{i+j-1}\arrow[u,"d"']
\end{tikzcd}}'''
new=r'''\figure{\begin{tikzpicture}
\node (q) {\begin{tikzcd}
B^i\times Z^j\arrow[r] & Z^{i+j}\\
C^{i-1}\times Z^j\arrow[u,"d\times\mathrm{id}"]\arrow[r,"\unsure{h_{ij}|b_{ij}}"'] & C^{i+j-1}\arrow[u,"d"']
\end{tikzcd}};
\draw[thin] ([xshift=-2pt]q.west) -- ([xshift=-2pt,yshift=-2pt]q.south west) -- ([xshift=3pt,yshift=-2pt]q.south east) -- ([xshift=3pt,yshift=8pt]q.north east);
\end{tikzpicture}}'''
t=repl(t,old,new)
cc=[]
def a(place,c,h,f,ink,kind='other',dc=False,dh=True,k=None,conf='high',cons=False,marked='no'):
 cc.append(change(place,c,h,f,ink,kind,dc,dh,conf,cp(k) if k else 'page',marked,cons))
a('heading fraction','1/2-Algèbre différentielle','k-Algèbres différentielles','1/2-Algèbre différentielle','A stacked 1 and 2 separated by a fraction bar; both nouns are singular.','misread symbol or index',cons=True)
a('base-ring qualification','commutatif','ill','commutatif','Parenthesized word with crossed t and final f.','readable ink left as \\ill{}',marked='yes')
a('augmentation margin','ou, il suffit qu’il y ait une augmentation','ill augmentation','ou, il suffit qu’il y ait une augmentation','Full three-line slanted note is present.','readable ink left as \\ill{}',k='augmentation',conf='medium',marked='yes')
a('complex initial object','unsure 0 or dash','ellipsis','unsure ellipsis or 0','Several pale traces precede the connector; the outline does not securely settle zero.','misread symbol or index',dc=True,k='complex',conf='low')
a('complex final continuation','unsure dash or ellipsis','ellipsis','dash','Only one short continuation stroke is visible.','misread symbol or index',k='complex')
a('unit-section explanation','la section unité de k correspond à une section T de C0','ill correspond à une section T de C0','la section unité de k correspond à une section T de C0','The entire parenthesis is present, including the unit-section phrase.','readable ink left as \\ill{}',marked='yes')
a('cancelled adjective','deleted unsure bilin.','omitted','deleted bilin.','Tall b and short ilin under a cancellation stroke.','omission',k='bilin_trial',conf='medium')
a('conditions introduction','les relations or aux conditions','aux conditions','aux conditions','The first group has a final x; following group begins con-.','misread word',dc=True,dh=False,k='conditions',conf='medium')
a('condition 1 values','y prennent valeurs','y prennent leurs valeurs','y prennent valeurs','No word intervenes between prennent and valeurs.','text not on the page')
a('condition 1 explanation','Donc la notation ... elle a un sens si dx ou dy est nulle','ill la notation ... dx circ dy ill','Donc la notation ... elle a un sens si dx underlined ou dy est nulle','The word ou has its own underline; it is not a composition circle. The feminine ending of nulle remains as written.','readable ink left as \\ill{}',k='nulle',conf='medium',cons=True,marked='yes')
a('cancelled restart after 1','deleted unsure donc','omitted','deleted donc','Looped d and following short onc are crossed out.','omission',k='donc_trial',conf='medium')
a('associativity qualification','si deux','ill','si deux','Small dotted i followed by the four-letter group deux.','readable ink left as \\ill{}',k='si_deux',conf='medium',marked='yes')
a('third degree in associativity','C^h','C^k','C^h','Raised h has one shoulder and no lower diagonal arm.','misread symbol or index',cons=True)
a('associativity remaining prose','de; sont des cocycles','ill; ill des cocycles','de; sont des cocycles','Both short words are visible around the displayed degree list.','readable ink left as \\ill{}',marked='yes')
a('condition 3 parity','i underlined impair','ill condition on i','i underlined impair','The word impair and its separate underline are visible.','readable ink left as \\ill{}',cons=True,marked='yes')
a('cancelled section trial','si unsure xi/ui ... zj/xj ...','omitted','cancelled trial retained with doubts','A pale crossed line lies between conditions 3 and 4; its short words and indices remain doubtful.','omission',k='deleted_sections',conf='low')
a('condition 4 map name','h_ij bilin.','ill / bilinéaires','h_ij bilin.','Tall initial h, lower ij, and abbreviated bilin. with a dot.','abbreviation expanded or spelling modernised',cons=True,marked='yes')
a('preliminary map deletion extent','entire map deleted','entire map deleted','only source deleted; replacement above it','The strike crosses C^{i-1} times Z^j; arrow and target have no strike through them.','deletion state',dc=True,k='square',conf='medium')
a('preliminary map label','h_ij','a_ij','h_ij','The label above the arrow begins with an ascender and shoulder.','misread symbol or index',k='square',conf='medium')
a('replacement over preliminary source','inserted Zi times Zj','omitted','inserted Zi times Zj','Both raised-index Z factors are written above the cancelled source.','insertion or placement',k='square',conf='medium')
a('square introduction','rendant le carré suivant commutatif','ill','rendant le carré suivant commutatif','Pale sentence immediately above the square.','readable ink left as \\ill{}',k='square',conf='medium',marked='yes')
a('square top left','unsure Bi or Zi','Zi','Bi','Vertical stroke with two right-hand lobes; distinct from the following angular Z.','misread symbol or index',k='square',conf='medium',cons=True,marked='yes')
a('square lower arrow label','h_ij','b_ij','unsure h_ij or b_ij','Faint ascender and lower ij survive, but the loop/shoulder is not secure.','misread symbol or index',dc=True,k='square',conf='low',cons=True,marked='yes')
a('square enclosing stroke','omitted','omitted','thin open-topped outline','Thin left, bottom and right strokes surround the square; no complete top edge is supplied.','drawing or diagram',dc=True,k='square',conf='low')
a('right margin derivative','d(xi circ zj)=dxi circ zj','ill','d(xi circ zj)=dxi circ zj','Two i superscripts and the small composition circles remain visible.','readable ink left as \\ill{}',k='derivative_margin',conf='medium',marked='yes')
a('cancelled paragraph after square','donc ... h_ij formula ...','only fragment d(x^(i)) times Zj=d(ill)','cancelled paragraph retained with its doubts','A full cancelled paragraph contains the condition, equality and section qualification; its final words are physically too pale.','omission',k='cancel_paragraph',conf='low',marked='yes')
a('NB deletion state','deleted','partly live','deleted','Long oblique cancellation strokes cross the NB paragraph as well as the preceding draft.','deletion state',k='NB_intro')
a('NB Hom domain','C^{i-1} tensor_k Zj','ill tensor Zj','C^{i-1} tensor_k Zj','C with raised i-1 and small lower k on tensor are visible.','readable ink left as \\ill{}',k='NB_hom',conf='medium',marked='yes')
a('NB prose and last lines','indétermination ... celle-ci ... voulue; on peut ... donnés, et pour des ...','ill','same, remaining doubts retained','Recoverable word groups are preserved; intervening near-erased stretches cannot be resolved by enhancement.','omission',k='NB_end',conf='low',marked='yes')
items=[]
for kind,pos,first in [('text','top','1/2-Algèbre différentielle'),('text','top','Anneau de base; résolution'),('margin note','upper left','ou, il suffit'),('diagram','upper','complex and k augmentation'),('text','upper','la section unité'),('deletion','above Accouplements','bilin.'),('text','upper middle','Accouplements notés'),('display','upper middle','two partial products'),('text','middle','satisfaisant aux conditions'),('text','middle','condition 1 and explanation'),('deletion','after 1','donc'),('text','middle','condition 2 associativity'),('display','middle','unit identity'),('display','lower middle','condition 3 two equations'),('deletion','between 3 and 4','section trial'),('text','lower','condition 4'),('diagram','lower','preliminary map'),('deletion','preliminary map source','Ci-1 times Zj'),('insertion','above source','Zi times Zj'),('text','lower','rendant le carré suivant commutatif'),('diagram','lower','square with Bi'),('drawing','around square','open-topped outline'),('margin note','right of square','d(xi circ zj)'),('deletion','below square','donc paragraph and equality'),('deletion','foot','NB indétermination'),('display','within NB','Hom_k'),('text','foot','349')]:items.append(inv(kind,pos,first))
notes="This upright, very pale sheet defines a 1/2-Algèbre différentielle on a topos with two partial products, one factor a cocycle, and compatibility, associativity and graded-commutativity conditions. It then asks for auxiliary bilinear maps related to a boundary square. The heading really has 1/2, not k; the prose says dx underlined ou dy and retains the feminine nulle. In the square the upper source visibly begins B^i, compatible with the image of d, although the earlier source revision says Z^i. These are preserved as distinct written forms. The lower map label remains h/b, so the mathematics has not been used to force it. The cancelled NB gives a Hom group for the indeterminacy of possible lifts: conditional on two maps having the same d-composite, their difference has image in ker d=Z^{i+j-1}; this is the elementary explanation of that Hom target, not a proof that the required maps exist. The faint cancelled prose is the least secure area; no completion has been supplied for physically unreadable spans. Manuscript foot 349; no date."
commit(n,t,ds,cc,items,notes,hand=['A pale composition circle can resemble the word ou; here the separate underline and letter sequence settle ou.','B has two faint right lobes; Z has angular upper and lower strokes. Both occur side by side in the square.','Cancellation through a source does not automatically cancel the untouched arrow and target; the preliminary map is retained in that state.'],notation=[('1/2-Algèbre','Stacked fraction in the heading, singular noun.'),('B^i, Z^i','Both retained; not normalized into a single source symbol.'),('h_ij / b_ij','Lower square label left uncertain; upper preliminary label h is clearer.')],abbr=[('bilin.','bilinéaire'),('NB','nota bene')],checks=[check('348.lift-indeterminacy','Conditional check: d(h-hprime)=0 implies image of h-hprime is in Z^{i+j-1}; hence the indicated Hom target describes differences of lifts. No existence claim checked.','targeted proof check')],unresolved=['Cancelled section trial between conditions 3 and 4 (low).','Lower square label h_ij or b_ij (low).','Faint open-topped enclosing stroke around square (low).','Cancelled donc paragraph and its last three words (low).','Cancelled NB prose, including est dans, celle-ci, voulue, exiger pour les and donnés (low).'])
