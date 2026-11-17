"""Write the exact normal-form statement with its literal audited input."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
path=root/'work_CE/next_symmetric_nodes/geometric_stabilizer_factored_chain.json'
data=json.loads(path.read_text())
original,transformed=data['circuits']
assert data['old_word']==[6,2,-6,-2] and data['node_index']==[8,0]
assert original['input_length']==124 and original['factored_term_count']==42
assert transformed['input_length']==119780 and transformed['factored_term_count']==33162
assert transformed['uncollected_expansion_cost']==67823551
assert data['original_117_coefficient_calibration']
assert all(c['full_compressed_boundary_verified'] for c in data['circuits'])
word=original['literal_F21_word']
rows=[]
for k in range(0,len(word),18):
    rows.append(','.join(map(str,word[k:k+18])))
literal=',\\\\\n &'.join(rows)
template=r'''% Complete actual root-path normal form and geometric stabilizer counterexample.
\statement{B.103}{Proved}{Exact integral root-path normal forms retain complete columns and exclude every unit multiple for an actual geometric head stabilizer}
\label{stmt:B103}
Use the discrete groups, actual paired bases and integral coefficient
ring $\Omega=\mathbb Z[G]$ of B.94 and B.98. For $a\in R_A$, let
$L_A(a)$ denote the oriented root path from $1$ to $a$ in $T_A$.
For a positive common $R_B$ generator $x$ and $b\in R_B$, write
$e_B(b,x)$ for the edge from $b$ to $bx$.
Then
\begin{equation}\label{eq:B103-basis}
 \mathcal C=\{L_A(a)\otimes e_B(b,x):
                   a\ne1,\ b\in R_B,\ x\text{ a positive basis generator}\}
\end{equation}
is a free abelian basis of the entire product-tree module
$P=C_1(T_A,\mathbb Z)\otimes C_1(T_B,\mathbb Z)$.
Its finite collected coefficient dictionaries are exact unique
normal forms. They retain the complete integral chains and all
$G$ coefficients.

For $g=(u,v,t)\in G$, the actual action on this basis is
\begin{equation}\label{eq:B103-action}
 \begin{aligned}
 g\bigl(L_A(a)\otimes e_B(b,x)\bigr)
  ={}&\bigl(L_A(u\tau_t(a))-L_A(u)\bigr)\\
     &\quad\otimes e_B\bigl(v\tau_{\beta(t)}(b),
                                      \tau_{\beta(t)}(x)\bigr).
 \end{aligned}
\end{equation}
Thus one $G$ monomial creates at most two terms per input term.
Every unit of $\Omega$ is of the form $\pm g$.

Let $c_{8,0}\in P$ be the actual node column of B.99. Let
$\psi_6,\psi_2$ be the literal positive geometric old operators
for $b_5,b_1$, respectively, in its six-lasso marking, and put
\[
 w=[b_5,b_1]=[6,2,-6,-2],\qquad
 \Psi=\psi_2^{-1}\circ\psi_6^{-1}\circ\psi_2\circ\psi_6.
\]
The composition convention means that the letters $6,2,-6,-2$
are applied successively to the based relator, exactly as in B.99.
This $w$ belongs to the complete selected head kernel and diagonal
row stabilizer. Nevertheless
\begin{equation}\label{eq:B103-no-unit}
                  \Psi(c_{8,0})\ne U c_{8,0}
                  \quad\text{for every }U\in\Omega^\times.
\end{equation}
Indeed their respective supports in \eqref{eq:B103-basis} have
$33\,162$ and $42$ terms, and $33\,162>2\cdot42$.
This is a full-chain counterexample. It asserts neither independence
of these two columns over $\Omega$ nor nonmembership in a whole
source-translated column span.

\begin{proof}
\emph{B.103.1. Integral basis and full coefficient recovery.}
The augmented cellular chain sequence of a tree is exact, so
\[
 \partial:C_1(T_A,\mathbb Z)\xrightarrow{\sim}
             I_{\mathbb Z[R_A]}.
\]
The elements $a-1$, for $a\ne1$, are a free abelian basis of this
augmentation ideal, and $\partial L_A(a)=a-1$.
This proves that the root paths form an integral basis. Tensoring
with the positive-edge basis of the other tree proves
\eqref{eq:B103-basis}, including uniqueness and finite support.
It is not an augmentation or a coefficient truncation.

For comparison with B.94, expand one root path into its signed
positive edges. A standard square at vertices $(u,v)$ with
$A$ generator $x_{(g,i)}$ and $B$ generator $x_{(h,j)}$ has the
actual normalized coefficient and row
\[
              (u,v,g)\in G,\qquad(i,j,\beta(g)^{-1}h).
\]
Consequently the root-path dictionary reconstructs every full
$\Omega$ coefficient by exact finite additions. Expansion is
available but unnecessary for equality in $P$.

\emph{B.103.2. Construction from a literal based relator.}
Schreier rewrite a word in the actual paired $F_{21}$ basis using
the retained splitting of B.94. At retained prefix $t$, an $A$
letter in slot $i$ becomes $x_{(t,i)}$, and a $B$ letter in slot
$j$ becomes $x_{(\beta(t),j)}$. Keep the reduced prefix vertices
$a\in R_A$ and $b\in R_B$.
At an $A$ letter, update $a$ and add no two-chain term.
At a signed $B$ letter $x^\epsilon$, set $b'=bx^\epsilon$ and
add
\begin{equation}\label{eq:B103-integration}
 \epsilon L_A(a)\otimes e_B(v,x),\qquad
 v=\begin{cases}b,&\epsilon=1,\\ b',&\epsilon=-1,\end{cases}
\end{equation}
then replace $b$ by $b'$.
The positive generator $x$ includes its full retained word and slot.
We apply this construction to words whose retained, $A$ and $B$
endpoints are all the identity.

Write $H(a,v)$ for the root $A$ path placed at the $B$ vertex $v$.
The full product boundary is
\begin{equation}\label{eq:B103-boundary}
 \begin{aligned}
 \partial\bigl(L_A(a)\otimes e_B(v,x)\bigr)
   ={}&H(a,v)-H(a,vx)\\
      &+e_B(a;v,x)-e_B(1;v,x).
 \end{aligned}
\end{equation}
Here the first argument of $e_B(a;v,x)$ specifies its $A$ vertex.
The first two terms telescope against precisely the actual $A$
edges of the input word: its consecutive root paths differ by
the actual traversed signed $A$ edge. The last two terms give
the actual $B$ edges minus their projection to the tree at $A=1$.
That projected chain is zero, because it is a closed path in a
tree. Thus \eqref{eq:B103-integration} has the full prescribed
boundary. The product of the trees is contractible and has no
three-cells, so its two-boundary is injective. This proves the
chain is the complete unique filling, not a partial integration.

Persistent reduced-word trees store each vertex by a parent,
a signed letter and its length. Appending an inverse last letter
returns the parent; other append operations create or reuse a
single node. A term records its two vertex identifiers, positive
$B$ generator and integer coefficient. Collection compares these
actual words, so this representation introduces no word equality
assumption. Its number of precollection terms is at most the
number of $B$ letters in the literal input.

\emph{B.103.3. The actual coefficient action and its units.}
The retained action is literally
\[
 \tau_t(x_{(g,i)})=x_{(tg,i)},
 \qquad \tau_{\beta(t)}(x_{(h,j)})=x_{(\beta(t)h,j)}.
\]
It permutes positive free generators. In particular the $B$ edge
in \eqref{eq:B103-action} is one edge, not a longer path.
The translated $A$ path runs from $u$ to $u\tau_t(a)$; in a tree
its chain is $L_A(u\tau_t(a))-L_A(u)$. This proves the action
formula and the support bound. The claim is for the actual $G$
action. An arbitrary old operator need not permute these edges.

B.98 proves a bi-order on $G$. For nonzero finite group-ring
elements $A,B$, the least support element of $AB$ is
$\min(A)\min(B)$, and the greatest is $\max(A)\max(B)$.
Each has a unique contributing pair and a nonzero integer
coefficient: strict order in either factor remains strict under
left and right multiplication. If $AB=1$, both extremes equal
$1$. Since inversion reverses the order,
\[
 \max(B)=\max(A)^{-1}\le\min(A)^{-1}=\min(B).
\]
Both supports are therefore singletons, and their integer
coefficients multiply to $1$. This proves
$\Omega^\times=\{\pm g:g\in G\}$ and establishes the claimed
support bound for every ring unit.

\emph{B.103.4. The complete actual geometric input.}
In the signed paired indices $p_1,\ldots,p_{21}$ of B.94, the
actual based relator for node $(8,0)$ is the following word of
length $124$; a negative integer denotes the inverse generator:
\begingroup\small
\[
 \begin{aligned}
 r_{8,0}=[&LITERAL_WORD]_{p}.
 \end{aligned}
\]
\endgroup
Applying the four displayed operators successively gives the
complete freely reduced word of length $119\,780$ retained in
the certificate below. B.99 proves that the actual old word $w$
has trivial retained action and both selected heads trivial.
Its membership in that head kernel is not inferred from any
column calculation.

The exact normal-form construction yields
\begin{center}
\begin{tabular}{lrr}
\toprule
 & original $r_{8,0}$ & transformed $\Psi(r_{8,0})$\\
\midrule
Paired word length & $124$ & $119\,780$\\
Deleted letters & $100$ & $92\,628$\\
Collected root-path terms & $42$ & $33\,162$\\
Uncollected standard rectangles & $173$ & $67\,823\,551$\\
\bottomrule
\end{tabular}
\end{center}
Both full boundaries satisfy \eqref{eq:B103-boundary}; all three
endpoints are the identity. Expanding only the small original
dictionary reproduces all $117$ already audited standard square
coefficients, including signs and retained labels.
The independent verifier reconstructs all four old substitutions,
every retained and $R$ word node, the entire transformed word,
both full telescoping boundaries and the complete collected
dictionary. Thus the support counts are exact integer counts,
not approximate ranks, cyclic word lengths or sampled rows.
Equation \eqref{eq:B103-no-unit} now follows from the proved
at-most-two-term action and $33\,162>84$.

\begingroup\raggedright
The complete input words, both normal forms and every reduction
node are in
\path{work_CE/next_symmetric_nodes/geometric_stabilizer_factored_chain.json}.
The producer is \path{work_CE/code/factored_product_tree_chain.py},
and the independent verifier is
\path{work_DE/next_marginal_source/verify_factored_product_tree_chain_independent.py}.
Both have their genuine outputs and input hashes. The complete
generic coefficient operations and composition checks are in
\path{work_CE/code/root_path_chain_operations.py}.\par
\endgroup
The earlier explicit square expansion was interrupted and is
retained with its incomplete status. The present finite normal
form supplies the complete chain without performing that expansion.
General $\Omega$ linear combinations may have arbitrarily many
monomials. Accordingly the support argument does not determine
whole source-orbit intersections or the image of $\kappa$.
\end{proof}
'''
text=template.replace('LITERAL_WORD',literal)
target=root/'sections/b_root_path_normal_form.tex'
target.write_text(text)
record={'source_certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'literal_word_length':len(word),'original_terms':42,'image_terms':33162,
        'signed_old_word':[6,2,-6,-2],'printed_word_matches_certificate':True,
        'tex_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(root/'records/B103_printed_input20.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
