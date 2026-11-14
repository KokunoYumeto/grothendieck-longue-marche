\subsection{The complete first inert-prime stratum and the first lower factor at fifty-three}

\begin{statement}{E.116}{Proved}{Pure norm coordinates for $v_3(\ell+1)=1$, and exact class and norm maps at $53$}
Let $\ell$ be a rational prime congruent to $2$ or $5$ modulo nine,
and fix compatible positive roots $\alpha_m=\ell^{1/3^m}$.
Put $F_m=\mathbb Q(\alpha_m)$, $M_m=\mathbb Q(\zeta_3,\alpha_m)$,
and let S denote the primes over three and $\ell$.
All completions below mean completion for multiplication by powers of three.
Then
\[
 \operatorname{Cl}(M_m)\{3\}=\operatorname{Cl}(F_m)\{3\}=0,
 \qquad
 N:\widehat{\mathcal O_{F_{m+1}}^\times}_3
       \twoheadrightarrow\widehat{\mathcal O_{F_m}^\times}_3,
 \qquad \ker N\simeq\mathbb Z_3^{3^m}.
 \tag{E116.1}
\]
These are the actual field norms and ideal norm/extension maps.
For the complex ordinary units the precise quotient is
\[
 \mathcal O_{M_m}^\times/N\mathcal O_{M_{m+1}}^\times
       \xrightarrow{\sim}C_3,
 \qquad u\longmapsto(\alpha_m,u)_{\mathfrak l,3},
 \tag{E116.2}
\]
where $\mathfrak l$ is the unique prime over $\ell$ and
the symbol uses arithmetic local reciprocity. Complex
conjugation acts on this quotient by inversion. Its
restriction to the included $\zeta_3$ is nonzero.

Let
\[
 \begin{gathered}
 P_0(\ell)=\{p\ne3,\ell:v_3(\operatorname{ord}_{\mathbb F_p^\times}\ell)=0\},
 \mathcal R(P)=\{(a_p)\in\prod_{p\in P}\mathbb Z_3:
                       a_p\longrightarrow0\},\\
 \mathcal U_{\ell,0}=\varprojlim_{m,N}
              \widehat{\mathcal O_{F_m}^\times}_3,
 \qquad
 \mathcal X_{\ell,0}=\varprojlim_{m,N}\widehat{F_m^\times}_3.
 \end{gathered}
 \tag{E116.3}
\]
There are actual, choice-specified continuous inverse maps
\[
 \begin{gathered}
 \mathcal U_{\ell,0}\simeq\prod_{m\ge0}\mathbb Z_3^{3^m},\qquad
 \mathcal X_{\ell,0}\simeq
       \mathcal U_{\ell,0}\times\mathbb Z_3^2\times\mathcal R(P_0(\ell)),\\
 (u,B,e,v)\longmapsto u\,a_3^B a_\ell^e\prod_{p\in P_0(\ell)}a_p^{v_p},
 \qquad N_{F_0/\mathbb Q}(x_0)=3^B\ell^e\prod_p p^{v_p}.
 \end{gathered}
 \tag{E116.4}
\]
Each $a_p$ is a norm-coherent completed principal generator
of the specified prime chain and has initial value $p$;
$a_3,a_\ell$ have initial values $3,\ell$.
The inverse reads those valuations and divides by the displayed
product. The unit coordinates and their inverse are the
literal matrix recursion (E116.13).

This evaluates every factor of E.46 for the first class
$3^k u\kappa_3(\ell)$, $k\ge0$, $u\in\mathbb Z_3^\times$.
In particular every second toric coordinate
\[
  \beta=B_3\kappa_3(3)+B_\ell\kappa_3(\ell)
                 +\sum_{j=0}^{k+1}\sum_{p\in P_j(\ell)}v_p\kappa_3(p)
 \tag{E116.5}
\]
has the full global $H$-section fibre
\[
 \mathcal U_{\ell,0}\times\prod_{j=1}^{k+1}\mathcal U_{\ell,j}.
 \tag{E116.6}
\]
These are exactly the possible second toric coordinates.
Here the sets $P_j$ and the fully evaluated complex factors
$\mathcal U_{\ell,j}$ are those of E.114; the exponent family
in (E116.5) is restricted. Equations (E116.14)--(E116.15)
give the actual inverse for this fibre and both directions
of its comparison to E.55. The second toric coordinate is
the scaled augmentation $\operatorname{aug}(v)/3$, as in E.46.

The first inert prime beyond the already evaluated $17$
with $v_3(\ell+1)>1$ is $53$, for which this valuation is three.
Here write $a=53^{1/3}$, $b=53^{1/9}$,
$F=\mathbb Q(a)$, $L=\mathbb Q(b)$,
$M=\mathbb Q(\zeta_3,a)$ and $E=\mathbb Q(\zeta_3,b)$.
The following is the complete first pure norm transition:
\[
 \begin{gathered}
 \operatorname{Cl}(F)=0,\quad
 \operatorname{Cl}(L)\simeq C_3^2,\quad
 \operatorname{Cl}_S(L)=0,\quad
 \operatorname{Cl}_S(E)\{3\}\simeq C_3,\\
 \sigma(b)=\zeta_3b:\quad\sigma=1
       \text{ on }\operatorname{Cl}_S(E)\{3\},
 \qquad c=-1\text{ on that group}.
 \end{gathered}
 \tag{E116.7}
\]
All class norms to $M$ and $F$, and all class extensions
from those lower fields, are the zero maps, since their
three-primary class groups vanish. The prime-coordinate
map in (E116.23) specifies the nonzero upper classes.

The certified lower S-unit basis, with torsion $\{\pm1\}$
removed by multiplication completion, is
\[
 \begin{gathered}
 e=-344340+4517a+23202a^2,\\
 p_A=(46-16a+a^2)/3,\qquad
 p_B=(-272+125a-14a^2)/3,\qquad a.
 \end{gathered}
 \tag{E116.8}
\]
The elements $p_A,p_B$ generate the two three-primes of
$F$, of ramification indices one and two respectively.
The eight literal upper S-units $U_1,\ldots,U_8$ of
(E116.22) are a basis of $\widehat{\mathcal O_{L,S}^\times}_3$.
The full norm map in these bases is
\[
 R=\begin{pmatrix}
 1&0&0&0&-1&-1&-1&0\\
 0&0&0&0&3&3&0&0\\
 0&0&0&0&0&0&3&0\\
 0&0&0&0&0&0&0&1
 \end{pmatrix}.
 \tag{E116.9}
\]
Thus its image is exactly
$\{e^x p_A^{3y}p_B^{3z}a^w:x,y,z,w\in\mathbb Z_3\}$.
The fibre over such an element has the actual inverse
\[
 \begin{gathered}
 (r_2,r_3,r_4,r_6)\longmapsto
 U_1^{x+y+z}U_2^{r_2}U_3^{r_3}U_4^{r_4}
 U_5^{y-r_6}U_6^{r_6}U_7^zU_8^w,\\
 (n_i)_{i=1}^8\longmapsto(x,y,z,w;r_2,r_3,r_4,r_6),\\
 x=n_1-n_5-n_6-n_7,\quad y=n_5+n_6,\quad z=n_7,\quad w=n_8,\\
 r_2=n_2,\quad r_3=n_3,\quad r_4=n_4,\quad r_6=n_6.
 \end{gathered}
 \tag{E116.10}
\]
The ordinary unit norm is onto, with kernel
$\mathbb Z_3^3$ on $U_2,U_3,U_4$.

The exact complex comparison retains one further obstruction.
Label the three primes of $M$ by the embeddings
$a=b_0\zeta_3^i$ into $\mathbb Q_3(\zeta_3)$, where
$b_0^3=53$ and $b_0\equiv-1\pmod9$.
For a completed S-unit $v$ put $v_i=v_{Q_i}(v)$.
Then
\[
 \begin{aligned}
 v\in N\widehat{E^\times}_3
       &\quad\Longleftrightarrow\quad v_0+v_1+v_2\equiv0\pmod3,\\
 v\in N\widehat{\mathcal O_{E,S}^\times}_3
       &\quad\Longleftrightarrow\quad
             v_0\equiv v_1+v_2\equiv0\pmod3.
 \end{aligned}
 \tag{E116.11}
\]
The quotient of these two norm images is $C_3$, with
generator the ratio of the literal principal generators
of $Q_0$ and $Q_1$. Equations (E116.18)--(E116.21) prove
both directions by the actual Hilbert90 and quadratic
norm maps. This result evaluates this first lower layer
at $53$; its higher lower positional factors remain the
actual norm systems specified in E.46 and E.114.
The manuscript anchor is \S51.16, scans172--178,
folios733v--736v, equations(371)--(379), and Part E(c),(d).
\end{statement}

\begin{proof}
\emph{The two actual ramified places when $v_3(\ell+1)=1$.}
Put $K=\mathbb Q(\zeta_3)$ and $\lambda=1-\zeta_3$.
At the unique prime over $\ell$, $X^{3^m}-\ell$ is Eisenstein.
At three write $X=Y-1$. The constant term of
$(Y-1)^{3^m}-\ell$ has $\lambda$-valuation two, and
every intermediate coefficient is divisible by three.
If $t=\alpha_m+1$, reduction gives $v_\lambda(t)>0$;
every intermediate term has valuation strictly greater
than two. Therefore $3^m v_\lambda(t)=2$.
Since $\gcd(2,3^m)=1$, the completion has the full degree
$3^m$ and is totally ramified. This also proves uniqueness
of the three-prime at every stage. Away from three and
$\ell$ the derivative $3^m X^{3^m-1}$ is a unit at every
root, so these are all the ramified primes.
Each $M_{m+1}/M_m$ is consequently cyclic cubic with
exactly two ramified finite places and no infinite ramification.

The residue field at $\ell$ is always $\mathbb F_{\ell^2}$.
The norm of a unit in this totally ramified cubic reduces
to its cube. Since $v_3(\ell^2-1)=1$, the included
$\zeta_3$ is not such a cube.
For an ordinary global unit, all unramified local symbols
are zero. Global reciprocity says that the two remaining
symbols add to zero. Thus the field-unit norm index is
at most three; the displayed $\zeta_3$ shows it is exactly
three. This is an assertion about field norms by the
cyclic Hasse norm theorem, whose actual map is
$M_m^\times/NM_{m+1}^\times\hookrightarrow
\bigoplus_v(M_m)_v^\times/N(M_{m+1})_v^\times$
\cite[VIII,Theorem3.1 and proof]{E_MilneCFT}.

The ambiguous class formula now gives
\[
 |\operatorname{Cl}(M_{m+1})\{3\}^{\sigma}|
       =|\operatorname{Cl}(M_m)\{3\}|\,3^{2-1}/3.
 \tag{E116.12}
\]
The base $K$ has class number one. A nonzero finite
three-group with an action of a group of order three has
nonzero invariants: on its nonzero subgroup killed by
three, $\sigma-1$ is nilpotent. Induction in (E116.12)
therefore gives the asserted vanishing of the entire
three-class group. The strongly ambiguous formula, with
this zero upper three-class group, gives the actual
ordinary-unit norm index three as well. These are the
two precise formulae of \cite[Theorem1, Proposition1 and
the full ideal/Herbrand proof]{E_LemmermeyerAmbiguous}.
The local character consequently gives the exact quotient
(E116.2), not merely a necessary test.

For the quadratic inclusion $j:F_m\hookrightarrow M_m$
and norm $n$, one has $nj=2$ and $jn=1+c$ on completed
units and on three-primary ideal classes. Thus $j$ identifies
the completed pure units with the $c$-fixed subgroup;
the inverse is $n/2$. On (E116.2), $c$ inverts the nonzero
class of $\zeta_3$ and hence acts as minus one.
Taking fixed groups is exact because two is invertible.
The fixed quotient is zero, proving the pure-unit norm
surjectivity. The same pair of actual maps proves
$\operatorname{Cl}(F_m)\{3\}=0$.
The unit rank of $F_m$, of signature
$(1,(3^m-1)/2)$, is $(3^m-1)/2$; its roots of unity are
$\{\pm1\}$. This proves the kernel rank in (E116.1).

\emph{Literal infinite coordinates and their topology.}
Choose actual fundamental units at every finite pure level.
Their relative norm exponent matrix $N_m$ has a right inverse
$R_m$ over $\mathbb Z_3$, obtained from a unit minor in its
Smith reduction; let $K_m$ be the resulting basis of its
kernel. These are actual field-norm matrices. They give
\[
 z_0=0,\qquad z_{m+1}=R_m z_m+K_m t_m,
 \qquad
 t_m=K_m^{-1}(z_{m+1}-R_mz_m),
 \quad t_m\in\mathbb Z_3^{3^m}.
 \tag{E116.13}
\]
Here $K_m^{-1}$ means its coordinate inverse on the displayed
kernel, supplied by the same invertible Smith matrix.
Both formulas are continuous at every finite level and
are mutually inverse. This proves the first homeomorphism
in (E116.4), including its choice dependence: another
pair $(R_m,K_m)$ changes coordinates by these same forward
and inverse matrix formulas.

For any prime chain with residue degree one, its ideal is
principal in the multiplication completion because its
class has order prime to three. Choose a principal power
of that order and raise its generator to the inverse
order in $\mathbb Z_3$.
Inductively, the norm of a chosen next generator divided
by the chosen lower generator is an ordinary completed
unit. Surjectivity in (E116.1) supplies an ordinary unit
preimage; division by that preimage makes the generators
norm coherent. Begin with $3$, $\ell$, or $p$ in $F_0$.
This is the construction of every $a_p$ in (E116.4).

Outside S, the compatible positions of roots of
$X^{3^m}-\ell$ form $\mathbb Z_3$, and actual Frobenius
acts as $x\mapsto p x+b_p$ with its Kummer translation.
It has an integral fixed point precisely when the
three-primary order of $\ell\bmod p$ is one. The explicit
compatible residue roots in that case are
$\ell^{3^{-m}\bmod d}$, $d=\operatorname{ord}_p(\ell)$.
This gives the unique surviving degree-one chain.
Every other orbit has unbounded three-part in its residue
degree; the ideal norm multiplies its compatible valuation
by these degrees, so a $\mathbb Z_3$-valued coherent
valuation on such a chain is zero. This proves the
divisor coordinate $\mathcal R(P_0(\ell))$.
At three and $\ell$ the unique chains have residue degree
one and give the two displayed scalar coordinates.

At each finite field, the completed principal-divisor
sequence is exact: the three-primary class group is zero,
and the finite-rank unit kernel is compact. Equivalently,
take actual principal powers of class orders prime to
three as above. Thus the only kernel after all valuations
have been removed is the ordinary unit system (E116.13).
For a restricted exponent family $v$, the product
$\prod a_p^{v_p}$ converges in every multiplication
quotient: modulo $3^n$ all but finitely many exponents
are divisible by $3^n$, uniformly in the chosen generators.
The same observation proves continuity of the product
and its inverse for the prodiscrete restricted topology.
This proves all of (E116.4); no compactness is asserted
for the infinite restricted divisor module.

For completeness the total-norm coupling to E.46 is as
follows. Set $u=1$ initially, since the actual arithmetic
automorphism $\Phi_u(a,v(T))=(ua,v(T^u))$ and its inverse
transport to every three-adic unit $u$.
At a cofinal positional level the factors are exactly
$F_m$ and $L^\ell_{m,j}$, $1\le j\le k+1$.
Choose $y_0\in\mathcal U_{\ell,0}$ and
$y_j\in\mathcal U_{\ell,j}$ arbitrarily. In E.114's
fixed splitting form
\[
 \begin{gathered}
 x_j=y_j s_j(3v|_{P_j}),\qquad
 A_3=\sum_{j=1}^{k+1}\nu_3(x_j),\qquad
 A_\ell=\sum_{j=1}^{k+1}\nu_\ell(x_j),\\
 x_0=y_0 a_3^{\,3B_3-A_3}a_\ell^{\,3B_\ell-A_\ell}
              \prod_{p\in P_0}a_p^{3v_p}.
 \end{gathered}
 \tag{E116.14}
\]
Here $\nu$ applied to $x_j$ includes the initial valuations
of its splitting factors, exactly as in (E114.8).
Their total rational norm is literally
\[
 N(x_0)\prod_jN(x_j)
       =\left(3^{B_3}\ell^{B_\ell}
                    \prod_{j,p}p^{v_p}\right)^3.
 \tag{E116.15}
\]
E.46's inverse Kummer--Shapiro cochain map now gives the
actual global $H$ section. Conversely, E.46 sends such
a section to its unique factor tuple; the disjoint prime
sets force each divisor coordinate to be $3v_p$.
Remove the specified splitting factors to recover every
$y_j$, and (E116.15) forces the two exponents of $x_0$.
This proves (E116.6) and its topology.
The exact comparison with E.55 is the composition of
this construction with E.46's evaluation-at-a-root
Shapiro map and E.55's evaluation on its actual inertia,
Frobenius and complementary generator, followed by the
finite orbit projection and its displayed odd gauge.
In the other direction use E.55's constructed cocycle,
E.46's inverse norm tuple, then (E116.14) in reverse.
Thus the comparison retains the actual arithmetic roots,
the scaled augmentation and every inverse; it does not
identify the two displayed products by their abstract ranks.

\emph{The three-place labels and local characters at $53$.}
The least inert primes are $2$, $5$, $11$, $17$, $23$,
$29$, $41$, $47$, and $53$.
Those before $53$, apart from the already settled $17$,
have $v_3(\ell+1)=1$; $53+1=2\cdot27$.
The retained default-flag-zero certifications prove
$\operatorname{Cl}(F)=\operatorname{Cl}(M)=0$.
They also give the basis $\zeta_3,u_1,u_2$ of its
completed ordinary unit group, with the last two columns
in the basis $(1,a,a^2,\zeta_3,\zeta_3a,\zeta_3a^2)$:
\[
 \begin{pmatrix}
 -344627/3&344627/3\\
 178976/3&91747/3\\
 -23222/3&24425/3\\
 327656/3&-327656/3\\
 91747/3&-87229/3\\
 -47647/3&-23222/3
 \end{pmatrix}.
 \tag{E116.16}
\]
The unique rational three-adic cube root $b_0$ of $53$
satisfies $b_0\equiv-1\pmod9$ and is itself a cube in
$\mathbb Q_3$: the cube map sends $1+3\mathbb Z_3$
onto $1+9\mathbb Z_3$, as its convergent logarithm shows.
Thus the completion of $E/M$ at $Q_0$ splits; at $Q_1,Q_2$
it is respectively the Kummer extension for $\zeta_3$
and $\zeta_3^2$, namely the cyclotomic cubic
$\mathbb Q_3(\zeta_9)/\mathbb Q_3(\zeta_3)$.
At $53$ it is totally ramified and tame. These are the
only three ramified finite places.

Here are all local character columns, including their
actual principal S-divisor inputs. Principal generators
$q_i$ of $Q_i$, in analytic order $i=0,1,2$, have columns
\[
 \begin{pmatrix}
 -174&-1505&18526/3\\
 -1063/3&1063/3&-3288\\
 320/3&37/3&1313/3\\
 1331&-1331&37052/3\\
 -1202/3&-139/3&-1644\\
 37/3&320/3&-1313/3
 \end{pmatrix}.
 \tag{E116.17}
\]
Their complete ideals are the indicated single primes,
and their absolute norms are three. The literal quadratic
norms are $N_{M/F}(q_0)=p_A$ and
$N_{M/F}(q_1)=N_{M/F}(q_2)=p_B$, with positive sign.
The analytic-to-PARI
prime order is $(1,3,2)$, checked by the literal local
valuations of these columns. On the ordered S-unit basis
$(\zeta_3,u_1,u_2,q_0,q_1,q_2,a)$ the four character rows are
\[
 \begin{array}{c|rrrrrrr}
       &\zeta_3&u_1&u_2&q_0&q_1&q_2&a\\ \hline
 Q_0&0&0&0&0&0&0&0\\
 Q_1&0&0&0&1&1&1&0\\
 Q_2&0&0&0&2&2&2&0\\
 53 &0&0&0&0&0&0&0
 \end{array}
 \tag{E116.18}
\]
The normalization can be checked without a wild-symbol
black box. In the embedding $a=b_0\zeta_3^i$, write
$u=x+y\zeta_3$ and divide its quadratic norm
$x^2-xy+y^2$ by its exact power of three. If its unit
part is $n_i(u)$ modulo nine, the arithmetic Artin
character is
$i(n_i(u)^{-1}-1)/3\pmod3$.
This follows from the actual Artin norm square and the
action of a rational unit $n$ on $\zeta_9$ by $n^{-1}$.
The norm square is the restriction/corestriction
compatibility of the cup-product isomorphism
\cite[III,Theorem3.1 and its proof]{E_MilneCFT}.
At $53$ the character for a unit is
$-\log_{\zeta_3}(\overline u^{(53^2-1)/3})$ in
$\mathbb F_{53}[\zeta_3]$; for the literal uniformizer
$a$ it is zero by alternation. These formulas give
(E116.18) exactly. Their column sums are zero, as
required by global reciprocity.

\emph{The completed Hilbert90 maps and the conjugation sign.}
For this paragraph use $U_T=\mathcal O_{T,S}^\times$ and
$\sigma(b)=\zeta_3b$. Since all ramification is in S,
an invariant divisor outside S is exactly an extended
base divisor. Hilbert90 for elements consequently gives
\[
 H^1(\langle\sigma\rangle,U_E)
       \simeq\ker(\operatorname{Cl}_S(M)
                          \xrightarrow{j}\operatorname{Cl}_S(E))=0.
 \tag{E116.19}
\]
Explicitly, a norm-one S-unit $z=x^{\sigma-1}$ has
invariant outside-S divisor $\operatorname{div}x=jD$;
its image is $[D]$. Changing $x$ by a base element
changes $D$ by a principal divisor. In the reverse
direction a principal extension $jD=(x)$ maps to
$x^{\sigma-1}$. These maps are inverse modulo the
displayed coboundaries.
The S-unit Herbrand quotient is the product of local
degrees divided by three, hence $1\cdot3\cdot3\cdot3/3=9$.
The proof of this formula identifies the logarithmic
unit lattice with the augmentation kernel of the actual
permutation lattice on S-places
\cite[VII,Proposition3.1 and complete proof]{E_MilneCFT}.
Together with (E116.19) it gives
$C=U_M/NU_E\simeq C_3^2$.

The same ideal Hilbert90 maps as in
\cite[Proposition1 and proof]{E_LemmermeyerAmbiguous}, now
on divisors outside S, give the exact sequence
\[
 \begin{gathered}
 0\longrightarrow\operatorname{Cl}_S(E)^{\sigma}\{3\}
  \xrightarrow{\nu} C
  \longrightarrow U_M/(U_M\cap NE^\times)\longrightarrow0,\\
 \nu([D])=Nx\pmod{NU_E},\qquad
                  (\sigma-1)D=\operatorname{div}_{\notin S}(x),\\
 \nu(c[D])=(c\nu([D]))^{-1}.
 \end{gathered}
 \tag{E116.20}
\]
For surjectivity onto the kernel, take $u=Nx$ an S-unit;
the outside-S divisor of $x$ has norm zero, so its
coefficients on each finite permutation orbit are a
$\sigma-1$ difference. The resulting divisor $D$ is
ambiguous. The kernel consists of extended base divisor
classes, which vanish because $\operatorname{Cl}_S(M)=0$.
Changing $x$ by a norm-one element uses element Hilbert90,
and changing the divisor primitive changes only an
extended base divisor; these checks prove well-definedness
and both inverse directions.
For the last formula apply $c\sigma c=\sigma^{-1}$:
one can take $(\sigma c x)^{-1}$ as the element for
$cD$, whose norm is $(cNx)^{-1}$. This is the sign
needed in the following descent.

All these quotient groups are killed by three and finite.
They are unchanged by completion: $U_M^3\subset NU_E$,
the free parts are finitely generated, and tensoring the
finite-rank kernel/image lattices with $\mathbb Z_3$ is
exact. For the field norm image, the exact local cyclic
characters in (E116.18), together with Hasse's theorem,
give a finite-index subgroup containing $U_M^3$;
its completion is precisely the kernel of the same
continuous characters. For the norm preimage direction,
choose actual field preimages of a finite generating set
of this finite-index S-unit subgroup. Products of their
three-adic powers lift its free completed coordinates;
choose an ordinary representative for its finite torsion
coordinate. Their norms are the prescribed element.
Thus this comparison proves the
completed assertions as well as the ordinary ones.

\emph{The certified upper bound and the independent lower bound.}
The degree-nine calculation first produces candidate
ideal generators $g_1,g_2$ with presentation $C_3^2$.
The separately executed \texttt{bnfcertify(B,1)} returns
one. Its precise assertion is that the actual class
group is a quotient of that presentation; it does not
certify the unit index. The official PARI documentation
states exactly this distinction, and its source performs
the prime-generation test before the flag-one return
\cite[\texttt{bnfcertify}, flag1]{E_PARICertifiedUnits}.
The four actual primes of $L$ over S, ordered by their
ramification indices $(1,2,6,9)$ over $\mathbb Q$, have
the following verified ideal relations in those generators:
$P_0\mapsto(0,1)$, $P_1\mapsto(0,1)$,
$P_2\mapsto(2,1)$, $P_{53}\mapsto(0,0)$.
The program verifies the full principal multiplier for
each relation by equality of ideal Hermite matrices.
These columns span $C_3^2$, so the actual
$\operatorname{Cl}_S(L)$ is zero, irrespective of whether
the initial ordinary presentation has a kernel.

Quadratic norm and extension now give
$\operatorname{Cl}_S(E)\{3\}^{c}=0$:
for a fixed class $z$, $jNz=(1+c)z=2z$, whereas
$Nz$ lies in the zero lower S-class group.
On (E116.18)'s image $C_3$, natural conjugation is
minus the interchange of the two nonzero rows, hence
acts as plus one. The left group of (E116.20) has order
three and is $c$-minus, since it has no fixed part.
The last identity of (E116.20) therefore makes its
image in the natural unit quotient $c$-plus.
Exactness and the projector $(1+c)/2$ show that all of
$C\simeq C_3^2$ is $c$-plus.
The actual unit inclusions and norms identify the fixed
groups by $j$ and $N/2$. Their commuting square with
the vertical cubic norms yields
\[
 \widehat U_F/N\widehat U_L
       \xrightarrow{\ j\ } C^+=C\simeq C_3^2,
 \qquad
 C\longrightarrow\widehat U_F/N\widehat U_L,
              \ [v]\longmapsto[N_{M/F}(v)^{1/2}].
 \tag{E116.21}
\]
These maps are mutually inverse. In particular the pure
S-unit norm image has index exactly nine, proved
independently of an exact upper class-number calculation.

For clarity the entire complex S-class group is now
determined too. Since its $c$-fixed part is zero, $c=-1$
on that finite three-group. The literal relation
$c\sigma c=\sigma^{-1}$ then gives
$\sigma=\sigma^{-1}$. Its order divides three, so
$\sigma=1$. Its invariant subgroup in (E116.20) is the
whole group, proving (E116.7)'s $C_3$ and both actions.

\begin{samepage}
\emph{Literal norm elements, saturation and inverse fibres.}
Here are the promised eight upper elements. A row lists
the coefficients of $1,b,\ldots,b^8$; denominators are
displayed as a common row denominator.\par
\end{samepage}
\[
 \begin{gathered}
 \begin{array}{c|r|rrrrr}
  &\text{den.}&1&b&b^2&b^3&b^4\\ \hline
 U_1&3&-898&2629&2975&1843&581\\
 U_2&3&-1858&-594&277&427&327\\
 U_3&1&30527&-13589&3794&1035&-2821\\
 U_4&3&-7978252&7819787&-6152925&4202572&-2534822\\
 U_5&9&1357&881&562&362&235\\
 U_6&3&-26493&-17045&-10965&-7053&-4537\\
 U_7&3&60&-57&44&-27&15\\
 U_8&1&0&1&0&0&0
 \end{array}\\[.7em]
 \begin{array}{c|r|rrrr}
  &\text{den.}&b^5&b^6&b^7&b^8\\ \hline
 U_1&3&-191&-427&-341&-160\\
 U_2&3&170&8&-57&-53\\
 U_3&1&2983&-2439&1714&-1063\\
 U_4&3&1325340&-553420&120572&83223\\
 U_5&9&149&97&62&40\\
 U_6&3&-2919&-1878&-1208&-777\\
 U_7&3&-8&3&0&-1\\
 U_8&1&0&0&0&0
 \end{array}
 \end{gathered}
 \tag{E116.22}
\]
Every element's complete ideal has been checked to have
support in S. The first four ideals are the unit ideal.
Their relative norms, computed by the literal resultant
$\operatorname{Res}_X(X^3-a,U_i(X))$, are
$e,-1,-1,-1,e^{-1}p_A^3,-e^{-1}p_A^3,
-e^{-1}p_B^3,a$, respectively.
This proves (E116.9) on these actual elements, with all
signs retained before completion. Its image has index
nine, equal to the independent bound (E116.21), so it
is the entire completed norm image.

Their upper S-divisor columns are zero for $i\le4$ and
$(3,0,0,0)$, $(2,1,0,0)$, $(0,0,3,0)$,
$(0,0,0,1)$ for $i=5,6,7,8$.
The actual norm on these divisor coordinates is
$(n_0,n_1,n_2,n_{53})\mapsto(n_0+n_1,n_2,n_{53})$:
the first two primes lie over $p_A$, the third over
$p_B$, and every relative residue degree is one.
Thus any principal S-divisor must satisfy
$n_0+n_1\equiv n_2\equiv0\pmod3$ by the just proved
full norm image. The displayed columns span exactly
this index-nine sublattice. The subgroup of ordinary
classes generated by S therefore has order nine.
The certified upper bound is also nine, which forces
the entire class group and its exact coordinate map
\[
 \begin{gathered}
 \operatorname{Cl}(L)\xleftarrow{\sim}(\mathbb Z/3)^2,
 \qquad (x,y)\longmapsto x[P_0]+y[P_2],\\
 (n_0,n_1,n_2,n_{53})\longmapsto(n_0+n_1,n_2),\\
 (x,y)\longmapsto(2y,x+y)
          \text{ in the original }(g_1,g_2)\text{ coordinates},\\
 (A,B)\longmapsto(B-2A,2A)\pmod3
          \text{ is the inverse coordinate change}.
 \end{gathered}
 \tag{E116.23}
\]
This gives the independent lower bound promised above;
the unfinished default-flag-zero certification is not
used at any point.

The four ordinary units are independently three-saturated.
At the actual degree-one residue maps
$(p,b\bmod p)=(13,1),(13,3),(13,9),(61,23)$,
use $\zeta_3\bmod p=3,3,3,47$, respectively.
The cubic residue characters of $U_1,U_2,U_3,U_4$ form
\[
 J=\begin{pmatrix}2&2&2&2\\1&1&2&2\\2&0&2&2\\2&1&1&0\end{pmatrix},
 \qquad\det J=-4,
 \qquad J^{-1}\pmod3=
 \begin{pmatrix}2&2&2&0\\2&0&1&0\\0&2&1&1\\1&2&2&2\end{pmatrix}.
 \tag{E116.24}
\]
Consequently no nonzero product of these units with
exponents modulo three is a cube in $L$.
The ordinary unit rank is four and $L$ has no
three-primary roots of unity. The generated rank-four
lattice is therefore three-saturated and gives the
entire completed ordinary unit group.
Together with the exact principal S-divisor lattice
this proves that all eight elements form the claimed
completed S-unit basis. Direct multiplication of
(E116.9) with the source exponents in (E116.10) proves
the inverse and every fibre; the certificate also
retains full integral Smith matrices and their inverses.
For the ordinary norm, $NU_1=e$ and the other three
norms are $-1$, proving its full image and kernel.

Finally the inverse of (E116.21) reads the pure three
valuations of $N_{M/F}(v)^{1/2}$ as
$v_0/2$ and $(v_1+v_2)/2$.
The first formula uses the ramified quadratic prime
above the degree-one three-place; the second uses the
two conjugate primes above the other place, all with
relative residue degree one. Hence (E116.9) gives
exactly the second criterion of (E116.11), while
(E116.18) and Hasse give the first.
Their nonzero quotient class is represented by
$q_0/q_1$ from (E116.17). This specifies its actual
field, valuation vector, local zero character and
nonzero S-unit obstruction.

The executable record keeps the failed 180-second
default-flag-zero run and its actual exit124 separately.
The successful flag-one bound, all element/ideal
equalities, the independent saturation matrix,
the complete norm Smith identities, the local prime
permutation and every inverse above are retained and
rebuildable. None of these calculations assigns a
class group or a stabilization to a later lower factor
at $53$.
\end{proof}
