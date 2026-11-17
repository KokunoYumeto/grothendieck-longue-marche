from record_page import record
record(6,r'''
\scanpage{6}
% archive foliation: 5
Prouvons $\Longleftarrow$, i.e. \deleted{Soit $x\in\overline C(j)$}, $R(x)\ne\varnothing$, $\forall y\in R(x)$, on a $y\in G(j)$, prouvons $x\in G(j)$.

Stratégie $\Sigma$ avec :
\[
z\in C(j),\quad\Sigma(z)=\begin{cases}R(z)\text{ si }z\notin G(j)\\ R(z)\cap G(j)\text{ si }z\in G(j)\end{cases}
\]
 a) \uline{\unsure{Bien une} stratégie}, \deleted{i.e. $R(z)\ne\varnothing\Longrightarrow\Sigma(z)\ne\varnothing$.}\inserted{par $1^\circ$. et $2^\circ)$, $\Longrightarrow$}

\deleted{En effet, il n'y a de question que si $z\in G(j)$ et alors $R(z)\cap G(j)\ne\varnothing$ par a)}

 b) Elle est $x$-gagnante. En effet soit $(x_0=x,x_1=y,x_2,\ldots,x_n,\ldots)$ une partie partant de $x$, comp. avec $\Sigma$, admettons qu'elle est finie.
\margin{On suppose qu'il n'y a \unsure{de} partie infinie}

Prouvons au préalable \unsure{en prouvant} que $x_i\in G(j)\quad\forall i\geq1$ \deleted{\unsure{les distinguons}} \inserted{OK} pour $i=1$ par hyp.

Supposons que \deleted{\unsure{c'est pour}} l'on ait $x_i\in G(j)$, prouvons $x_{i+1}\in G(j)$. En effet, si $x_i\in\overline C(j)$, cela provient de la partie déjà prouvée de $2^\circ$.
Si $x_i\in C(j)$, cela provient de la définition de $\Sigma$, car $\Sigma(x_i)=R(x_i)\cap G(j)$ donc $x_{i+1}\in\Sigma(x_i)$ \deleted{\unsure{donc x}} est $\in G(j)$. O.K.

\uline{Corollaire} \deleted{\unsure{Pour tte une stratégie}}\deleted{Il existe une stratégie $\Sigma$ telle}\deleted{\unsure{soit} $\Gamma\subset G(j)$.}
\inserted{Soit $j\in J$, $\Gamma\subset G(j)$ stable (dans $G(j)$) par succession.}
Il existe une \deleted{\unsure{que}} stratégie $\Sigma$ gagnante pour tous les $x\in\Gamma$.

 b) Parmi celles-ci il y en a une plus grande
''',[
('text','top','Prouvons left implication i.e. ...'),('deletion','top','Soit x in Cbar(j)'),('display','top','R(x) nonempty; forall y in R(x) y in G(j)'),('text','upper','Stratégie Sigma avec'),('display','upper cases','z in C(j), Sigma(z)=R(z) / R(z) cap G(j)'),('text','middle a','Bien une stratégie'),('deletion','middle a','i.e. R(z) nonempty implies Sigma(z) nonempty'),('insertion','middle a','par 1 degrees et 2 degrees right implication'),('deletion','middle crossed paragraph','En effet il n’y a de question que si z in G(j) ...'),('text','middle b','Elle est x-gagnante; soit tuple une partie'),('margin note','left','On suppose qu’il n’y a de partie infinie'),('text','middle-lower','Prouvons au préalable ... x_i in G(j) forall i>=1'),('deletion','middle-lower','les distinguons'),('insertion','middle-lower','OK'),('text','lower','Supposons que l’on ait x_i in G(j)'),('deletion','lower','c’est pour'),('text','lower','Si x_i in C(j), cela provient de la définition'),('display','lower','Sigma(x_i)=R(x_i) cap G(j); x_(i+1) in Sigma(x_i)'),('deletion','lower','donc x'),('text','bottom','Corollaire; Il existe une stratégie ...'),('deletion','bottom corollary','Pour tte une stratégie; Il existe une stratégie Sigma telle; soit Gamma subset G(j); que'),('insertion','bottom corollary','Soit j in J, Gamma subset G(j) stable ... par succession'),('text','bottom line','b) Parmi celles-ci il y en a une plus grande')
],'''The proof constructs the relation of all successors that stay within G(j). It explicitly says “admettons qu’elle est finie,” alongside a marginal global exclusion of infinite plays. This is a self-flagged step/hypothesis and matters for the maximal-strategy claim. The corollary starts a simultaneous winning-strategy statement on a successor-stable subset Gamma of G(j), with a greatest strategy asserted; its continuation must be read before assessing it.''')
