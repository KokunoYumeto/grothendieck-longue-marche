from save_page import save
tex=r'''
\scanpage{40}

On en conclut un isom canonique
\diagram{\boxed{\begin{tikzcd}[column sep=large]
H^1(X,A) & \operatorname{Ext}^1(A',\underline{\operatorname{Pic}}_X) \arrow[l,"\sim"']
\end{tikzcd}}}

\margin{Cet isomorphisme reste-t-il valable pour $X$ singulier ??? Il est possible qu'on ait besoin de $H^i(X,G_m)=0$ pour $i\unsure{\geq|>}2$, \unsure{vrai seulement si} $X$ non sing. ??}

($A$, variété abélienne), qui se compare à la formule de dualité
\[
\boxed{H^1(X,G)\simeq\operatorname{Hom}(D(G),\underline{\operatorname{Pic}}_X)}
\]
pour $G$ commutatif affine.

Remarque, On a des hom canoniques
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\operatorname{Ext}^1(\underline{\operatorname{Alb}}_X,A) \arrow[r] \arrow[d,"\unsure{\wr}"] & H^1(X,A)\\
\operatorname{Ext}^1(A',\underline{\operatorname{Alb}}_X') \arrow[d,"\unsure{\wr}"] &\\
\operatorname{Ext}^1(A',\underline{\operatorname{Pic}}^{\unsure{\tau|0}}) &
\end{tikzcd}}

dont on constate que c'est des \uline{isomorphismes} \uline{\unsure{donc|tous}}, qui définissent sur les \unsure{deux} groupes en question l'isomorphisme envisagé plus haut.
\margin{39}
'''
e=[('text','top line','On en conclut un isom canonique'),('diagram','upper boxed isomorphism','H^1(X,A) <-sim Ext^1(A prime,underline Pic_X)'),('margin note','left upper and middle','Cet isomorphisme reste-t-il valable pour X singulier ???'),('text','middle two lines','(A, variété abélienne), qui se compare à la formule de dualité'),('display','middle boxed formula','H^1(X,G) ~= Hom(D(G),underline Pic_X)'),('text','below second box','pour G commutatif affine'),('text','lower section opening','Remarque, On a des hom canoniques'),('diagram','lower comparison','Ext^1(Alb_X,A) -> H^1(X,A); down to Ext^1(A prime,Alb_X prime) and Ext^1(A prime,Pic^tau)'),('text','lower three-line conclusion','dont on constate que c’est des isomorphismes ...'),('margin note','bottom left','39')]
d=[{'line':'left margin inequality','reading':'i>=2','alternatives':'i>2; small lower stroke uncertain','confidence':'medium'},{'line':'left margin after inequality','reading':'vrai seulement si','alternatives':'compressed faded strokes near ink blot','confidence':'medium'},{'line':'diagram vertical labels','reading':'wr-like isomorphism marks','alternatives':'first curl clear, second overinked','confidence':'medium'},{'line':'diagram last Pic exponent','reading':'tau','alternatives':'0; hooked shape has top horizontal bar','confidence':'medium'},{'line':'final paragraph underlined connective','reading':'donc','alternatives':'tous; ending runs into underline','confidence':'low'},{'line':'final paragraph before groupes','reading':'deux','alternatives':'short word compressed; possible trois','confidence':'low'}]
save(40,tex,e,d,'Concludes canonical isomorphism H^1(X,A)←Ext^1(A prime,Pic_X), compares affine commutative G formula H^1(X,G)≈Hom(DG,Pic_X), and gives Albanese-duality maps. Critical marginal self-flag: “Cet isomorphisme reste-t-il valable pour X singulier ??? Il est possible qu’on ait besoin de H^i(X,G_m)=0 pour i [>= or >] 2, vrai seulement si X non sing. ??” Must not state singular extension as established. Pic exponent in the last diagram looks tau, not round zero; revisit all related Pic exponents in 039 at notation audit. Concluding isomorphism assertions carry no separate proof here. Pencil 39.')
