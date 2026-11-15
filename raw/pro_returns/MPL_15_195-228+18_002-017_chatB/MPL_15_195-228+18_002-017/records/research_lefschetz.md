# Lefschetz correspondence rings, motivic groups, and the singular-hypersurface question

Research memo for the frozen package `MPL_15_195-228+18_002-017`; prepared after the transcription freeze at **2026-11-15 14:05:01 UTC**. This memo changes no transcription. The calculations below are editorial calculations on explicitly defined objects, and are not reconstructions of doubtful manuscript formulas.

## Evidence and status conventions

**C** means `context_sources/MPL_16+47+54+44_transcription.tex`, always followed by cote and scan; its supplied transcription is a first-pass return. **N** means `context_sources/MPL_16+47+54+44_notes.md`, whose notes are earlier editorial claims. **R** means `context_sources/notes/RESULTS_STATE.md`; its returned-package notes are explicitly marked **first pass; a lead**, and the WG2 entries are **question or plan item; unchecked**. These statuses remain attached to the entries below. Reading a register excerpt has not verified the absent original return.

The context directory contains exactly six files: `README.md`, `notes/RESULTS_STATE.md`, the C transcription, its `_doubts.md` and `_notes.md` companions, and `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`. Neither the full cote 14 returns listed by R nor cotes 12–13 are supplied. The present memo uses the frozen current-page text of 15/213, 15/227, and 18/011; no source images were reopened.

## Concise answers

| Requested question | Answer supported by this dossier |
|---|---|
| Is the category of motives in cotes 12–13 built from the Lefschetz correspondence rings of cote 16? | The historical construction in 12–13 cannot be inspected here. C 16/3–18 supplies a graded ring with projectors and Lefschetz operators; current 15/227 already speaks of multiplicative functors from motives. The precise mathematical passage through correspondence composition, corners, projectors, and Tate twists is given in §2 below. R’s cote 14 excerpts report an existing category and a fourth, effectivity structure, but the full return is absent. |
| Is the Lefschetz sl₂ inside the motivic Galois group, and does its Cartan give the same grading? | The concrete comparison is $H=D-nI$, hence $h(s)=s^{-n}w(s)$ on an $n$-dimensional variety’s total cohomology. On the projective-line Tate category, $G=\mathbb G_m$, $\rho(t)=\operatorname{diag}(1,t)$, while the Lefschetz matrices generate a noncommutative sl₂; the exact conjugation and cocharacter relations are calculated in §3. Current 18/011 places $j'$ in $B'/U'$, with a lift and a centralizer, and does not supply an SL₂ subgroup morphism. |
| What is the draft’s A–D lettering? | The secure operator identification is draft $C_\ell$ with the algebraic-Lefschetz-inverse content of published $B$. Draft $A$ has critical-degree and algebraic-class evidence consistent with published $A$, but its complete standalone definition is absent here. Draft $B$ and $D$ occur in implications and known/unknown lists without standalone definitions; §4 records every relevant occurrence and does not assign them by a guessed permutation. |
| Does cote 14 carry out the singular-hypersurface programme of 16/47? | The available evidence does not establish that. C 16/47 explicitly requests a reformulation for singular varieties. R contains no match for `singul\|hypersurf`; its available cote 14 summaries discuss effectivity, gradings, correspondences, and later comparison theorems. The complete cote 14 texts are absent. |

## 1. Atomic note candidates

Each note body below contains at most four sentences. Metadata and the supplementary calculations are separate, so a main notes file can retain the short note and link to the relevant calculation.

### RL01 — The present pages use a category; the ring-to-category map is explicit

**Kind:** unpursued implication. **Current file/scan:** `pages/MPL_15_195-228+18_002-017_15_scan227.tex`, cote 15, scan 227. **Short source quote:** “foncteurs multiplicatifs de Motifs”. **Context:** C, cote 16, scans 3–4 and 15–18; N, S5–S6. **Relation:** adds a current-page anchor to the earlier ring/category question. **Register:** WG2 §2.4 #3 and WG2 §6. #9 — unchecked plans; MPL_14_002-044 M01 and §2, MPL_14_087-132 M01 — first-pass leads.

The current question already uses a category of motives and its multiplicative functors, while C 16/16–17 explicitly requires both $L$ and the projectors $\pi_i$ in its ring homomorphism. The correspondence construction in §2 gives the maps $f\mapsto qfp$, composition by pullback–intersection–pushforward, and degree $2r\mapsto\operatorname{Hom}(h(X),h(X)(r))$, thereby displaying the mathematical connection. The absent cotes 12–13 and full cote 14 returns prevent a conclusion here about the historical construction in those files.

### RL02 — A projective-line calculation tests the proposed subgroup inclusion

**Kind:** own calculation, verifying an earlier lead. **Current files/scans:** `pages/MPL_15_195-228+18_002-017_15_scan213.tex`, cote 15, scan 213; `pages/MPL_15_195-228+18_002-017_18_scan011.tex`, cote 18, scan 11. **Short source quotes:** $G(X,\xi)=\underline{\operatorname{Aut}}(\xi)$; $j':G_m\to B'/U'$. **Context:** C, cote 16, scans 14–18 and 48–49. **Relation:** verifies the register’s test and connects it to the newly supplied automorphism/cocharacter page. **Register:** MPL_14_087-132 M04 — first-pass own-idea lead; WG2 §2.4 #3 — unchecked plan. **Confidence:** high, by the displayed matrices in §3.

For the Tate category generated by $h(\mathbf P^1)=\mathbf1\oplus\mathbf Q(-1)$, tensor automorphisms act as $\rho(t)=\operatorname{diag}(1,t)$, whereas the Lefschetz matrices satisfy $[E,F]=\operatorname{diag}(-1,1)$. Every Lie algebra homomorphism from sl₂ into the one-dimensional abelian Lie algebra of this $\mathbb G_m$ vanishes, as follows directly from the three sl₂ bracket identities. The surviving relation is explicit: $\rho(t)E\rho(t)^{-1}=tE$ and $\rho(t)F\rho(t)^{-1}=t^{-1}F$, so the motivic torus acts on the Lefschetz operator algebra by the Tate character and its inverse.

### RL03 — Three cocharacters can be compared without suppressing the scalar

**Kind:** own calculation. **Current file/scan:** `pages/MPL_15_195-228+18_002-017_18_scan011.tex`, cote 18, scan 11. **Short source quotes:** $(\varepsilon|B'/U')\circ j'=\mathrm{id}$; $L'=\operatorname{Centr}(j'_0)$. **Context:** C, cote 16, scans 3, 14, and 16–18. **Relation:** adds the current Levi/cocharacter datum to the grading question. **Register:** WG2 §2.4 #3 — unchecked plan; MPL_14_002-044 B04 — first-pass lead. **Confidence:** high for the explicit Tate calculation, without assigning an unproved general interpretation to the draft $j'$.

In the Tate example of §3, the cocharacter recording the Hodge index is $j(t)=\operatorname{diag}(1,t)$, the cohomological-weight cocharacter is $w(s)=j(s^2)$, and the centered Lefschetz cocharacter is $h(s)=s^{-1}j(s^2)$. The scalar $s^{-1}$ acts on the tensor-unit summand, which gives a direct check of the group-valued claim. Current 18/011 specifies a cocharacter in the Levi quotient and a lift $j'_0$, so its comparison with a Lefschetz Cartan requires these exponent and scalar data.

### RL04 — The integral model has an explicit factor of two

**Kind:** own calculation, checking an earlier claim. **Context file/scans:** C, cote 16, scan 14, and scans 16–17. **Short source quotes:** “sur $\mathbb Z$ !”; “Il faut donc se donner en même temps $L$ et les $\pi_i$”. **Prior notes:** N, R1–R3 and S2–S5. **Relation:** verifies the factorial test and supplies the exact operator conversion; it does not settle the integral order requested by the plan. **Register:** WG2 §2.3 #3, WG2 S28 (§1.7), WG2 §6. #9 — unchecked plans. **Confidence:** high, by direct exterior multiplication and matrix calculation.

For $\xi=e_1\wedge f_1+e_2\wedge f_2$, $\xi^2=2e_1\wedge f_1\wedge e_2\wedge f_2$, so the written integral exterior model sends the degree-zero generator to twice a top-degree generator. On the concrete string $v_j=L^jp$ of length $m+1$, the unit-step lowering $U$ and the sl₂ lowering $F$ are related by $Fv_j=j(m-j+1)Uv_j$. The calculations in §3 and §6 make this comparison before interpreting the matrix-ring description; the full integral-order computation for $n\leq4$ remains outside the verified results of this memo.

### RL05 — Preserve the draft letters and compare their operator content

**Kind:** reading question. **Context file/scans:** C, cote 16, scans 42 and 44–49; N, S1 and S12. **Short source quote:** “$D_\ell(X)$ implies ... the coefficients of the characteristic polynomial are rational numbers” (16/48, with the supplied uncertainty between $\ell$ and $\chi$ retained in C). **Relation:** repeats the prior caution and strengthens it by a complete local occurrence audit. **Register:** WG2 §2.4 #3 — unchecked plan.

Draft $C_\ell$ is identified operationally by algebraic complementary-degree inverses, matching published $B$, and draft $A$ is discussed through algebraic classes and critical-degree Lefschetz maps. The supplied occurrences of draft $B$ and $D$ provide implications but no standalone definitions, as documented exhaustively in §4. Grothendieck’s published $A$ includes the cohomological isomorphism as well as its restriction to algebraic classes, whereas Kleiman states the cohomological Lefschetz property before defining $A(X,L)$; the comparison therefore records the source formulation as well as its letter [G69, §§2–3; K68, §2].

### RL06 — The singular programme is visible; its cote 14 continuation is not supplied

**Kind:** unpursued implication / evidence limit. **Context file/scan:** C, cote 16, scan 47. **Short source quote:** “see how to reformulate for singular varieties the standard conjectures”. **Prior notes:** N, 16:47:4–6. **Relation:** records the programme and the exact limit of the supplied cote 14 register excerpts. **Register:** WG2 §2.4 #3 — unchecked plan; MPL_14_002-044 M01, §2, §107 and MPL_14_087-132 M01 — first-pass leads.

The letter rejects its proposed smooth-hypersurface reduction after reporting Serre’s fundamental-group objection, then explicitly asks for a singular reformulation. The supplied register’s cote 14 summaries report effectivity and correspondence/grading material, and the full-text register search `singul|hypersurf` has no hit. Since the named cote 14 return files are absent, the present evidence does not determine whether those pages execute the programme; N 16:47:6’s suggested resolutions and intersection-cohomology comparison remains an earlier editorial idea.

### RL07 — Numerical semisimplicity is connected by a specific quotient map

**Kind:** unpursued implication. **Context file/scan:** C, cote 16, scan 49. **Short source quote:** “the category of motives which is semi-simple !”. **Prior notes:** N, S15–S16. **Relation:** verifies the numerical theorem and states the actual comparison morphism. **Register:** WG2 §2.3 #7 — unchecked plan; MPL_14_087-132 M09 — first-pass lead.

Jannsen proves semisimplicity and abelianness for pure numerical motives with characteristic-zero coefficient field [J92, Theorem 1]. The relation to the manuscript’s cohomological correspondence classes is the surjection $A^d_{\rm hom}(X\times X)\to A^d_{\rm num}(X\times X)$, sending a cycle’s homological class to its numerical class. Section 5 identifies its kernel explicitly and supplies a concrete algebra quotient demonstrating why target semisimplicity alone gives no calculation of that kernel.

### RL08 — The abelian bridge has an explicit group morphism in correspondences

**Kind:** unpursued implication, primary-source verification. **Context file/scans:** C, cote 16, scans 15–18; the bridge to cote 47, scans 3–11, is the one named in R. **Short source quote:** “anneau ... de correspondances Lefschetzien” (16/18). **Relation:** verifies a later rational correspondence realization of the planned bridge. **Register:** WG2 B16 (§1.2) — unchecked plan; MPL_14_002-044 M24a and MPL_14_087-132 M10 — first-pass leads.

Künnemann constructs Lefschetz decompositions for rational Chow motives of abelian schemes over a smooth quasiprojective base [Ku93, introduction]. Beauville gives $\varphi:\mathrm{SL}_2\to\operatorname{Corr}^{*}(A)$, with raising operator $\Delta_*\theta$ and Cartan $\sum_i(i-g)\pi_i$, and then acts by correspondences on Chow groups [B08, Theorem 3.3]. The formulas in §3 give the exact morphism and its centered grading, establishing the correspondence bridge named by the register without transporting it to an integral order.

## 2. The ring/category relationship as actual maps

The point of departure in C 16/3–4 is a family of orthogonal idempotents, summing to one, inside an endomorphism ring. The formula

\[
\mathcal E^{(\nu)}=\bigoplus_i\pi_{i+\nu}\mathcal E\pi_i,
\qquad u\longmapsto\sum_i\pi_{i+\nu}u\pi_i
\]

gives its homogeneous part. C 16/16 makes the images of the projectors part of its proposed homomorphism from the universal operator ring; 16/17 rejects uniqueness from $L$ alone; 16/18 gives the correspondence-ring name. These are precise statements in the supplied first-pass text, including its editorial alterations; they should not be silently strengthened into a construction of every motivic structure.

Here is the comparison in the concrete rational Chow category, with the triple convention written in [J92, pp.447–448]. For smooth projective $X,Y$ and $d_X=\dim X$, set

\[
\operatorname{Corr}^{r}(X,Y)=\mathrm{CH}^{d_X+r}(X\times Y)_{\mathbf Q}.
\]

For $f\in\operatorname{Corr}^{r}(X,Y)$, $g\in\operatorname{Corr}^{s}(Y,Z)$, the composition is

\[
g\circ f=(p_{XZ})_*\bigl(p_{XY}^*f\cdot p_{YZ}^*g\bigr)
\in\operatorname{Corr}^{r+s}(X,Z).
\]

The idempotent-completed category has objects $(X,p,m)$ and

\[
\operatorname{Hom}\bigl((X,p,m),(Y,q,n)\bigr)
=q\,\mathrm{CH}^{d_X-m+n}(X\times Y)_{\mathbf Q}\,p.
\]

In particular, the total correspondence ring is related to the category by

\[
\operatorname{Corr}^{r}(X,X)
=\operatorname{Hom}(h(X),h(X)(r)).
\]

An algebraic cycle $z$ acts on cohomology by the concrete formula

\[
z_*(a)=(p_2)_*\bigl(p_1^*a\cup\operatorname{cl}(z)\bigr),
\qquad H^i(X)\longrightarrow H^{i+2r}(X)(r).
\]

Composition of cycles is carried to composition of these maps. Choosing a basis of the realized Tate line permits writing their direct sum as ordinary matrices; the preceding formula retains the twist that the matrix notation suppresses. Thus an operator of cohomological degree (2r) is represented by a morphism to the $r$-th Tate twist, and an idempotent $p$ is represented by the summand ($X,p,0$).

The off-diagonal blocks are also explicit. In the additive category, put $M=h(X)\oplus h(Y)$ and let $e_X,e_Y$ be its two projectors; then the identification

\[
\operatorname{Hom}(h(X),h(Y))\longrightarrow e_Y\operatorname{End}(M)e_X,
\quad f\longmapsto
\begin{pmatrix}0&0\\f&0\end{pmatrix}
\]

has inverse given by restriction to the $X$-summand followed by projection to the $Y$-summand. This is the precise way a family of correspondence rings and its corner maps encodes morphisms between objects. None of these explicit maps establishes the textual history of the absent cotes 12–13.

The available cote 14 register excerpts are narrower evidence. R’s **MPL_14_002-044 M01** cites “Structure d’effectivité” on 14/002–003 and describes an already existing $M$; **§2** and **§107** summarize its correspondence/grading comparison; **MPL_14_087-132 M01** points to the notation on 14/117. All four are first-pass leads. Current 15/227 adds a visible question about multiplicative functors and places, rather than supplying the missing construction pages.

## 3. Operator normalizations, group morphisms, and the Tate test

### 3.1 A concrete string calculation

Fix the vector space with basis $v_0,\ldots,v_m$, and define actual matrices by

\[
Ev_j=v_{j+1},\quad Uv_j=v_{j-1},\quad
Fv_j=j(m-j+1)v_{j-1},\quad Hv_j=(2j-m)v_j,
\]

where the values outside the basis range are zero. Direct calculation gives

\[
(EF-FE)v_j=
\bigl[j(m-j+1)-(j+1)(m-j)\bigr]v_j
=(2j-m)v_j,
\]

and hence $[E,F]=H$, $[H,E]=2E$, $[H,F]=-2F$, including both endpoints. The exact conversion is $F=U\,a(J)$, with $Jv_j=jv_j$ and $a(J)=J(m+1-J)$. Writing the conversion this way records every scalar.

For a Lefschetz string beginning in degree $i$ in total cohomology of dimension $n$, put $m=n-i$ and $Dv_j=(i+2j)v_j$. Then

\[
H=D-nI,\qquad
w(s)v_j=s^{i+2j}v_j,\qquad
h(s)v_j=s^{2j-m}v_j=s^{-n}w(s)v_j.
\]

This calculation supplies the precise comparison between centered Lefschetz weights and cohomological weights. N R2 and S3 already proposed the corresponding normalization issue; this memo verifies the displayed conversion rather than relying on their status.

For the integral exterior model of C 16/14, let $L$ be wedge multiplication by $\xi=e_1\wedge f_1+e_2\wedge f_2$. Its square on $1$ is $2\,\mathrm{vol}$. The contraction operator $\iota_{f_1^*}\iota_{e_1^*}+\iota_{f_2^*}\iota_{e_2^*}$, with each $e_a\wedge f_a$ contracting to $1$, sends $\xi$ to $2$; the unit-step matrix sends $L1$ to $1$. These are exact values of the two operators, and rational rescaling on each string is the comparison map above. No modification to C’s doubtful formula (6.5) follows from this editorial calculation.

### 3.2 A primary-source correspondence morphism

For a polarized abelian variety $A$ of positive dimension $g$, write $\theta$ for its symmetric polarization class, $d=\theta^g/g!$, $\delta(x,y)=y-x$, and $\pi_i$ for its rational Chow–Künneth projectors. Beauville’s Theorem 3.3 constructs [B08]

\[
\varphi:\mathrm{SL}_{2,\mathbf Q}\longrightarrow
\operatorname{Corr}^{*}(A),\qquad
\operatorname{Corr}(A)=\mathrm{CH}^{*}(A\times A)_{\mathbf Q},
\]

with the correspondence-composition multiplication. Its differential is

\[
d\varphi(e)=\Delta_*\theta,\qquad
d\varphi(f)=\frac{\delta^*(\theta^{g-1})}{d(g-1)!},\qquad
d\varphi(h)=\sum_i(i-g)\pi_i.
\]

Its torus is exactly

\[
\varphi\!\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix}
=t^{-g}\sum_i t^i\pi_i.
\]

The further map $z\mapsto[z_*:a\mapsto(p_2)_*(z\cdot p_1^*a)]$ is the ring action on Chow groups. These formulas verify a later relationship between the rational Lefschetz ring, the centered grading, and Fourier correspondences. Künnemann’s introduction gives the abelian-scheme Chow-motive setting and its motivic Lefschetz isomorphism [Ku93]; this supports R’s B16/M24a/M10 bridge at rational coefficients. This memo makes no claim to have computed the integral order in WG2 S28.

### 3.3 The complete projective-line calculation

Work over $\mathbf C$ with rational Chow motives and their Betti realization. In $\mathrm{CH}^1(\mathbf P^1\times\mathbf P^1)$, the diagonal has class $[\{p\}\times\mathbf P^1]+[\mathbf P^1\times\{p\}]$; the two correspondence projectors give

\[
M=h(\mathbf P^1)=\mathbf1\oplus T,\qquad T=\mathbf Q(-1).
\]

For integer $a,b$, the correspondence formula on $\operatorname{Spec}\mathbf C$ gives

\[
\operatorname{Hom}(T^a,T^b)=
\begin{cases}\mathbf Q&a=b,\\0&a\ne b.\end{cases}
\]

The rigid additive category generated by $T$ is therefore the category of finite-dimensional, finitely supported $\mathbf Z$-graded rational vector spaces, with the degree-$a$ line sent to $T^a$. A tensor automorphism of its forgetful fiber functor is determined by a scalar $t\in R^\times$ on $T\otimes R$; tensor compatibility gives $t^a$ on $T^a$, and the unit has scalar $1$. This constructs the isomorphism of group functors $G\simeq\mathbb G_m$, not just its rational points.

On the basis $e_0,e_2$ of $H^0\oplus H^2$, the two actions are

\[
\rho(t)=\begin{pmatrix}1&0\\0&t\end{pmatrix},\quad
E=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
F=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
H=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]

The displayed $E,F,H$ satisfy the three brackets above, while the differential of $\rho$ has image $\{\operatorname{diag}(0,a):a\in\mathbf Q\}$. For a Lie homomorphism $u:\mathfrak{sl}_2\to\operatorname{Lie}(\mathbb G_m)$, the abelian target gives $u(H)=u([E,F])=0$, $2u(E)=u([H,E])=0$, and $-2u(F)=u([H,F])=0$. Thus this concrete Lefschetz action cannot be the differential of a subgroup inclusion into the Tate motivic group. This directly verifies the two-dimensional test named, but only excerpted, in R’s **MPL_14_087-132 M04**.

The relationship is retained by conjugation:

\[
\rho(t)E\rho(t)^{-1}=tE,
\qquad\rho(t)F\rho(t)^{-1}=t^{-1}F,
\qquad\rho(t)H\rho(t)^{-1}=H.
\]

Equivalently, the raising correspondence is a morphism $M\to M(1)$; the twist has character $t^{-1}$, so the tensor-naturality equation is

\[
(t^{-1}\rho(t))E=E\rho(t).
\]

This is the explicit map relating the graded correspondence to tensor automorphisms. The cocharacters, with the convention that $T$ has Hodge index $1$ and cohomological weight $2$, are

\[
j(t)=\operatorname{diag}(1,t),\qquad
w(s)=j(s^2)=\operatorname{diag}(1,s^2),\qquad
h(s)=s^{-1}w(s)=\operatorname{diag}(s^{-1},s).
\]

The first coordinate of $h(s)$ checks its action on the unit. In this example $B'=L'=G=\mathbb G_m$, $U'=1$, and the Tate character $\varepsilon$ is the identity, giving $\varepsilon j=\mathrm{id}$. This is a concrete comparison with the formulas on current 18/011, not an assertion that the page assigns these exponents in every motive.

## 4. Exhaustive local lettering audit

The full relevant passages C 16/42–49 were read after the freeze, including 16/43, whose $A,B$ are commutative rings in an EGA correction. Searches covered the entire C file for `conj` and `Conject`, followed by an audit of the four letters in the relevant passages and all isolated $B,D$ occurrences in 16/42–50; N S1 and S12 were read. Uppercase paragraph labels A), B), C) on 16/33 and the rings (A,B) on 16/43 do not provide definitions of the conjecture labels: their actual text is respectively a list of operator identities and a finite ring map (B=k[T_1,\ldots,T_r]\to A).

| Draft letter | Complete relevant occurrence evidence | Supported comparison |
|---|---|---|
| $A$ | 16/42: critical $A^0(X\times Y)$; 16/44: $A+\mathrm{index}\Rightarrow B$, characteristic-zero equivalence with $B$, and equality of dimensions of the algebraic-class spaces $C^i,C^{n-i}$; 16/45–47: critical-degree restrictions and low-dimensional list. | Algebraic-class Lefschetz content is visible. A complete standalone definition, including whether the full cohomological isomorphism is incorporated, is absent from these passages. |
| $B$ | 16/44: $A+\mathrm{index}\Rightarrow B$, and $A$ equivalent to $B$ in characteristic zero; 16/45 continues the equality under the index assertion; 16/46 lists $A,B$ among the positive-characteristic questions. | No standalone definition is supplied; no published-letter assignment is made. |
| $C$ | 16/42 and 45–46: algebraicity of the natural inverse to hyperplane restriction and of complementary-degree inverses; 16/48–49: the $u,v,w=uv$ inverse construction; 16/44 also uses $C(X)$ for a vector space of algebraic cycle classes. | The conjectural operator content matches published $B$, by the same algebraic inverse maps. The cycle-space notation on 16/44 is identified by its dimension and grading, not by the letter alone. |
| $D$ | 16/44: range $A_\ell$ through $D_\ell$; 16/46: $C(X)$ “or only $D(X)$” in the threefold list; 16/48: $D_\ell(X)$ in condition $a$, $C_\ell\Rightarrow D_\ell$, and $D_\ell\Rightarrow$ rational characteristic polynomials. | No standalone definition is supplied. The listed implications do not determine a unique definition. |

For comparison, the published dictionary verified in the primary texts is:

| Published source and label | Content relevant to the comparison |
|---|---|
| Grothendieck 1969, §3, $A(X)$ | $L^{n-i}:H^i\to H^{2n-i}$ is an isomorphism, together with its induced isomorphism on algebraic classes in even degrees. |
| Kleiman 1968, §2, $A(X,L)$ | After the cohomological Lefschetz property is stated as the setting, $L^{n-2p}:A^p\to A^{n-p}$ is bijective. |
| Grothendieck §3 / Kleiman §2, $B$ | Algebraicity of lowering; Kleiman §2.3 gives the same condition through algebraic inverses to $L^{n-i}$. |
| Grothendieck §2 / Kleiman §2, $C$ | Algebraic Künneth components of the diagonal; Grothendieck additionally writes a parenthetical common-cycle requirement across $\ell$. |
| Kleiman §3.6, $D$ | Equality of homological and numerical equivalence. |
| Grothendieck §4, $Hdg$ / Kleiman §3, $I$ | Positivity of the signed primitive intersection form on algebraic classes. |

The operator map in the draft’s Cayley–Hamilton argument is explicit: $u:H^{2n-i}\to H^i$, $v=L^{n-i}:H^i\to H^{2n-i}$, $w=uv$, and the constructed inverse is $w^{-1}u=v^{-1}$ (C 16/48–49). This exact common inverse is the basis of the draft-$C$/published-$B$ comparison. The uncertainty between the source subscripts $\ell$ and $\chi$, and the written dates 4.1.67 on 16/44 and 6.1.1966 on 16/48, remain unchanged.

## 5. Semisimplicity and singular varieties: what is and is not established here

### 5.1 The numerical comparison

Jannsen’s Theorem 1 proves that the category of pure motives for numerical equivalence is semisimple abelian, for characteristic-zero coefficients [J92]. The concrete comparison on correspondences is

\[
q_X:A^d_{\rm hom}(X\times X)\twoheadrightarrow
A^d_{\rm num}(X\times X),\qquad[z]_{\rm hom}\mapsto[z]_{\rm num}.
\]

This is well defined because a homologically zero cycle has zero intersection degree with every complementary cycle: the cycle-class map carries the intersection to the zero top-degree class. Its kernel is exactly the classes of numerically trivial cycles modulo homological equivalence. Thus there is a specific morphism relating the manuscript’s ring and the numerical ring.

For a direct algebraic check of what quotient semisimplicity alone says, the quotient

\[
\mathbf Q[\epsilon]/(\epsilon^2)\longrightarrow\mathbf Q,
\qquad a+b\epsilon\longmapsto a
\]

has semisimple target and nonzero nilpotent kernel $\mathbf Q\epsilon$. In its two-dimensional regular representation, multiplication by $\epsilon$ is $\begin{pmatrix}0&0\\1&0\end{pmatrix}$. This is a calculation about that explicit algebra, not an identification of it with a motivic correspondence ring. R’s M09 and N S15–S16 already flag the comparison; the present memo verifies the numerical theorem and writes the quotient and its exact kernel without asserting a new geometric vanishing result.

### 5.2 The singular-hypersurface programme

C 16/47 reports a proposed chain: birational equivalence to a smooth $X'$, specialization of a smooth $X''$, and birational equivalence of $X''$ to a smooth hypersurface. The author reports Serre’s objection that the resulting $X$ would have to be simply connected and then asks for work with singular hypersurfaces and a singular reformulation of the standard conjectures. This memo records the objection as the letter’s statement; it does not supply unrecorded family, dimension, characteristic, or fundamental-group hypotheses.

The supplied R excerpts from cote 14 supply “Structure d’effectivité” (MPL_14_002-044 M01), a ring/category comparison (its §2 and §107; MPL_14_087-132 M01), numerical semisimplicity (M09), the abelian case (M10 and M24a), and Nori/motivated-cycle leads (M23 and M28a). No displayed excerpt identifies a singular standard-conjecture construction. The exact negative search `singul|hypersurf` in R reinforces this evidence limit, but it says nothing about the unsupplied full files. N 16:47:6’s resolutions/intersection-cohomology suggestion is explicitly an earlier own idea; this memo neither promotes it into manuscript text nor states a new singular theorem.

## 6. Supplementary matrix-ring verification

This calculation verifies the string-algebra model used in the unchecked WG2 §2.3 #2 and gives an explicit morphism between the two operator algebras discussed in N S3. Its scope is this completely specified representation. It does not identify the manuscript’s integral exterior-algebra order with the model or supply the full proof of every manuscript formula requested by WG2 §6. #9.

Let $V_n=\bigoplus_{m=0}^n\bigoplus_{j=0}^m\mathbf Qv_{m,j}$, and let $E,U,F,H$ act on each summand by §3.1. Set $e=1-EU$. The integral polynomial

\[
e_m=eU^mE^me-eU^{m+1}E^{m+1}e
\]

projects onto $\mathbf Qv_{m,0}$: its first term selects string bottoms of length at least $m+1$, and its second selects the strictly longer strings. Thus

\[
E_m^{ba}=E^be_mU^a
\]

sends $v_{m,a}$ to $v_{m,b}$ and every other basis vector to zero. This proves by the displayed map that

\[
\mathbf Q[E,U]\simeq\prod_{m=0}^n\operatorname{Mat}_{m+1}(\mathbf Q).
\]

For the conversion to the sl₂ algebra, the element $C=H^2+2H+4FE$ acts on the $m$-th string by $m(m+2)$. Define

\[
q_m(C)=\prod_{r\ne m}\frac{C-r(r+2)}{m(m+2)-r(r+2)},
\quad
p_{m,j}=q_m(C)\prod_{0\leq k\leq m,\ k\ne j}
\frac{H-(2k-m)}{2(j-k)}.
\]

Here $p_{m,j}$ is the projector onto the basis line $v_{m,j}$, so

\[
U=\sum_{m=0}^n\sum_{j=1}^m
\frac{1}{j(m-j+1)}Fp_{m,j}.
\]

Conversely $F=\sum_{m,j}j(m-j+1)Up_{m,j}$, using the already explicit matrix units in $\mathbf Q[E,U]$. Consequently $\mathbf Q[E,F]=\mathbf Q[E,U]$, and the image of $U(\mathfrak{sl}_2)$ in this representation is exactly the displayed product. This is the explicit rational morphism; its denominators and the exterior calculation $\xi^2=2\mathrm{vol}$ are retained.

The identities, projectors, Casimir eigenvalues, and conversion for $n=0,1,2,3,4$ were also checked with exact rational matrices. The representation dimensions were $1,3,6,10,15$, and the algebra ranks were $1,5,14,30,55$. This finite check supports the direct basis proof above; it is not the integral-order computation requested by WG2 §6. #9.

## 7. Search and verification log

### Local searches

| Search | Files searched | Results and limit |
|---|---|---|
| `lefschet` (case insensitive) | C | Hits at 16/15, 18, 22, 25, 47, 50 and 44/4; these are lexical hits, not the full operator discussion, which also uses $L,\Lambda,\pi_i$. |
| `motif\|motiv` | C | 16/48–49. |
| `sl_2\|sl2\|sl₂\|mathfrak\{sl\}` | C | No match. The sl₂ identification is an editorial mathematical comparison, not a literal phrase recovered from C. |
| `singul\|hypersurf` | C | 16/42, 47 and 44/6, 8, 9. The singular-standard-conjecture programme is the explicit paragraph on 16/47. |
| `singul\|hypersurf` | R | No match. This is a result about the supplied register excerpts, not absent full cote 14 files. |
| `singul\|hypersurf`; `sl_2\|sl2\|sl₂\|mathfrak\{sl\}` | README | The standing research questions on lines 25 and 24 respectively. |
| `conj\|Conject`, isolated A/B/C/D, then every B/D occurrence in 16/42–50 | C | The occurrence table in §4 records all relevant conjecture uses; 16/43 is the EGA ring-map passage, and the other false positive `N.B.` provides no conjecture definition. |
| `Lefschetz\|lefschetzien\|singulier\|singular\|hypersurface\|sl_2\|mathfrak\{sl\}` | Frozen current combined text and individual page files | The lexical Lefschetz hit is 15/202’s “principe de Lefschetz” in the Lie-algebra editorial page; no literal sl₂ or singular-hypersurface programme was found by these terms. The substantive cocharacter page 18/011 was read directly. |
| `MPL_14\|WG2\|M04\|M09\|M10\|B16\|S28` | R | IDs and statuses used above; listed return paths were not treated as available files. |
| S1–S6, S12–S16; R1–R3; 16:47:1–6 | N | Prior claims checked against the C passages and, for the listed modern results, primary sources. |

### Primary-source browsing

Grothendieck’s original PDF at the Grothendieck Circle initially yielded no readable text through the browser connector. The same article’s Mainz-hosted PDF supplied readable §§2–4. Kleiman’s hosted original paper supplied §§1.4, 2, and 3.6; Jannsen’s author-repository PDF supplied the construction and Theorem 1. Künnemann’s primary Göttingen PDF opening exposed wrapper metadata; the search index supplied the paper’s introduction and a Theorem 5.1 excerpt, so only the introduction’s scope and displayed Lefschetz statement are used here. Beauville’s arXiv v1 was readable, and §1 plus Theorem 3.3 and its proof were checked directly. Nonprimary search hits were not used to substantiate technical claims.

## 8. Primary bibliography and retrieval references

- **[G69]** Grothendieck, A. (1969). *Standard conjectures on algebraic cycles*. In *Algebraic Geometry (International Colloquium, Tata Institute, Bombay, 1968)*, pp.193–199. Oxford University Press. Checked §§2–4. [Primary PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1968.Grothendieck.StandardConjs.pdf). Original alternative: [Grothendieck Circle](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf). Retrieval refs: `turn15view0`, `turn25view0`, `turn26view0`.
- **[K68]** Kleiman, S. L. (1968). *Algebraic cycles and the Weil conjectures*, pp.359–386. Checked §1.4, §2, and §3.6. [Primary PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf). Retrieval refs: `turn6view1`, `turn25view1`.
- **[J92]** Jannsen, U. (1992). Motives, numerical equivalence, and semi-simplicity. *Inventiones Mathematicae, 107*, 447–452. Checked pp.447–449, especially Theorem 1. [Author-repository PDF](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf). [DOI](https://doi.org/10.1007/BF01231898). Retrieval ref: `turn6view2`.
- **[Ku93]** Künnemann, K. (1993). A Lefschetz decomposition for Chow motives of abelian schemes. *Inventiones Mathematicae, 113*, 85–102. Scope and the displayed motivic Lefschetz isomorphism checked in the introduction through the primary PDF’s indexed text, with the retrieval limitation stated above. [Primary PDF](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0011.pdf). [DOI](https://doi.org/10.1007/BF01244303). Retrieval refs: `turn7search12`, `turn27search7`; wrapper-only open: `turn9view0`.
- **[B08]** Beauville, A. (2008). *The action of SL₂ on abelian varieties*. arXiv:0805.1541v1, 11 May 2008. Checked §1 and Theorem 3.3 with its torus formula. [Primary PDF](https://arxiv.org/pdf/0805.1541). Retrieval ref: `turn28view0`.

The retrieval references are an internal handoff aid; the bibliography URLs and section references are the portable citations. A parent agent should open a retrieved source itself before using its web citation token in a final chat response.
