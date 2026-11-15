# Research bridges and the Oda comparison

Research memorandum for the responsible reader. Prepared after the reported transcription freeze and context opening at 2026-11-15 14:05:01 UTC. The manuscript anchors below refer to the frozen page fragments; no source JPEG was opened and no transcription was changed in this research pass.

## Source and status conventions

`P15/NNN` means `pages/MPL_15_195-228+18_002-017_15_scanNNN.tex`; `P18/NNN` means the corresponding cote 18 file. `C16/49`, for example, means cote 16, scan 49 in the supplied `context_sources/MPL_16+47+54+44_transcription.tex`. References to earlier notes identify `context_sources/MPL_16+47+54+44_notes.md`; they remain leads unless the cited publication was checked independently here.

`context_sources/README.md` and `context_sources/notes/RESULTS_STATE.md` were read before this research. The register describes LM6 A.50 as **Proved (the return's claim)** and LM6 A.22 as **Open (the return's claim)**; both supplied statements are truncated. LM7 C.1 is **Known (the return's claim)**, C.5 **Proved (the return's claim)**, and C.8 **Refuted (the return's claim)**. The complete LM6 and LM7 return files named by that register are absent from the supplied context. Their omitted hypotheses and conclusions have not been reconstructed.

The full Oda extraction is outside the deliverable tree at `/workspace/scratch/ac0509dac04e/research_tmp/oda1969.txt`; its PDF renders are in the same directory. Embedded PDF text was extracted without OCR. Oda's printed pp. 89, 123–126, 131–132 were inspected as rendered pages; the references below use printed pagination. Search evidence is in `records/research_bridges_context_searches.json` and `records/research_bridges_oda_searches.json`.

## The requested comparison table

The labels in the first column organize explicit maps and calculations. They do not impose a disjoint classification of mathematical subjects.

| Requested pair | Linear construction | Nonlinear construction and connecting map | Concrete comparison / source scope |
|---|---|---|---|
| Tate / anabelian Hom | $f\mapsto T_\ell f$, from abelian-variety Hom to Galois-equivariant Tate-module Hom. | A curve map induces an outer arithmetic fundamental-group map; geometric abelianization carries it to $T_\ell\operatorname{Alb}(f)$. | Tate's finite-field Main Theorem and Faltings's number-field Satz 4 supply the linear Hom comparison. Mochizuki's Theorem A supplies dominant-curve/open-outer-Hom reconstruction over sub-$p$-adic fields. The genus-two calculation in §S1 tracks the effect of abelianization. |
| Semisimplicity / trivial centres | For connected affine groups in characteristic zero, Deligne–Milne Proposition 2.23 relates semisimplicity of representations to pro-reductivity; a tensor grading is a central cocharacter. | Conjugation $G\to\operatorname{Aut}(G)$ has kernel (Z(G)). For a geometric hyperbolic group $\Delta$, Mochizuki's Lemma 1.3.1 gives slimness, and Corollary 1.3.2 recovers the arithmetic extension from its outer action. | In $G=\mathbf G_m$, the direct sum of character spaces proves semisimplicity and the conjugation map is constant. Mochizuki's proof uses the Tate modules of generalized Jacobians of finite covers; see B03. |
| Polarizations / real structures | A Riemann form $Q$ and Weil operator $C$ give (Q(x,Cy)); conjugation by $C$ produces a Cartan involution on the appropriate polarization group. | With the Betti–de Rham comparison fixed, $c_{\mathrm{dR}}=F_\infty c_B$. The square elliptic torus makes both operations explicit. | §S2 gives $C^2=-I$, $c^2=I$, $cCc^{-1}=-C$, $c^tJc=-J$, and $\operatorname{Int}(C)(g)=(g^t)^{-1}$. The multiplier $-1$ is also $\chi_\ell(c)$ in the Weil pairing. |
| Weights / cyclotomic normalizers | For a marked curve, $0\to T_\ell T\to T_\ell J_D\to T_\ell J\to0$, with toric weight $-2$ and abelian weight $-1$. | Kummer covers at a cusp give $\sigma\tau\sigma^{-1}=\tau^{\chi_\ell(\sigma)}$, through the actual conjugation character $N(I_\ell)\to\operatorname{Aut}(I_\ell)$. | §S3 gives the realization and duality maps and cites the registered marked-curve and extension results; §S4 calculates cusp inertia that vanishes in first abelianization and survives in lower-central degree two. LM6 A.50/A.22 retain their supplied statuses. |

## Note candidates

Each indented candidate has at most four sentences. Longer computations follow in the support sections.

### B01 — Hom comparison through geometric abelianization

**Kind / comparison:** unpursued implication; exact functorial bridge with a concrete image test. **Source:** P15/215, opening; also P15/213 and P15/227. **Short quote:** “Caractériser … l'image ??”.

> For smooth proper hyperbolic curves over a number field, the map from curve morphisms to outer fundamental-group homomorphisms passes, by geometric abelianization, to the Tate-module map of the induced Albanese homomorphism. Faltings's Satz 4 and Mochizuki's Theorem A establish the respective Hom reconstructions in their stated settings. For the genus-two curve $y^2=x^5-x$, the Jacobian endomorphism $[2]$ acts as $2I$ on $T_\ell J$, whereas Riemann–Hurwitz forces every nonconstant self-map of the curve to have degree one; §S1 gives the resulting exact image calculation.

**Context search:** `Tate|fidèle|Hom|correspondance` finds C44/8, Tate module of $J^i$ as a quotient of a submodule of $H^{2i-1}(X,\mathbf Z_\ell(i))$, and C16/49, inverses of correspondence maps. **Register:** LM7 C.1, Known (return claim), provides the later curve/1-motive realization lead; `WG2 §2.4 #3`, unchecked plan, asks how these motive stages meet. **Sources:** [T66], [F83], [M-Hom]. **Confidence:** high for the stated comparison maps and genus-two calculation; the frozen page's general motive category is not assigned extra axioms here.

### B02 — Semisimplicity, the centre, and the weight cocharacter

**Kind / comparison:** own idea; explicit representation and conjugation calculations. **Source:** P15/195, middle paragraph. **Short quote:** “semi-simples … sans doute”.

> For $G=\mathbf G_m$, every finite rational representation is the direct sum $V=\bigoplus_n V_n$ of its character spaces, while $Z(G)=G$ and $G\to\operatorname{Aut}(G)$ by conjugation is constant. This example computes semisimplicity and the central kernel in one group. Deligne–Milne's Proposition 2.23 and Definition 5.1 further relate semisimple representations to pro-reductivity, and tensor gradings to central cocharacters, respectively.

**Context search:** `semi.simple|centre|graduation` finds C16/49's proposed semisimple category of motives and C16/5's central projectors in the degree-zero correspondence ring. **Register:** `WG2 §2.3 #7` and `WG2 §2.4 #3`, unchecked plans; LM7 C.5, Proved (return claim), supplies an extension-class lead for B06. **Source:** [DM82/22], Proposition 2.23, Definition 5.1. **Confidence:** high, because the character decomposition and conjugation map are explicit; the centre of the degree-zero correspondence ring is connected only through its stated representation, not silently identified with a Tannaka-group centre.

### B03 — Trivial centralizers proved through linear realizations of covers

**Kind / comparison:** unpursued implication; a source-proved nonlinear conclusion using linear realizations. **Source:** P15/195, semisimplicity paragraph; P15/213, reconstruction discussion. **Short quote:** “semi-simples”.

> Mochizuki's slimness proof takes sufficiently small normal open $H\subset\Delta$ whose covering curve has genus at least two and uses $H^{\mathrm{ab}}$, the profinite Tate module of its generalized Jacobian. Trivial conjugation on these modules forces the deck transformation to be trivial at every such level. Thus his exact sequence $1\to\Delta\to\operatorname{Aut}(\Delta)\to\operatorname{Out}(\Delta)\to1$ has a directly exhibited linear bridge.

**Context search:** `semi.simple|centre|Tate|Jacob` finds C16/49 and C44/8; no hyperbolic-group centre theorem occurs in the first Book II transcription. **Register:** LM6 A.50, Proved (return claim), is a finite-cover character-descent lead at LM scan 483, folio 245; its truncated conclusion is retained as unavailable. **Source:** [M-Abs], Lemma 1.3.1 and Corollary 1.3.2, pp. 15–16. **Confidence:** high for this cited proof mechanism; no semisimplicity premise has been added to it.

### B04 — The two conjugations and real Frobenius

**Kind / comparison:** own calculation validating a specific comparison identity. **Source:** P15/203, the two margin checks; P15/205, $f_\infty$; P15/215, real-point realization. **Short quote:** “à vérifier”.

> For a smooth proper variety over $\mathbf R$, transport coefficient conjugation on de Rham cohomology across the integration comparison $I$, and call it $c_{\mathrm{dR}}$ on complexified Betti cohomology. Naturality of integration gives $c_{\mathrm{dR}}=F_\infty c_B$, hence $c_Bc_{\mathrm{dR}}=c_{\mathrm{dR}}c_B=F_\infty$. Section S2 proves the relation by periods and fixes which conjugation is semilinear.

**Context search:** `conjugu|réel|real|Betti|de.?Rham|Cartier|orthogon` finds the de Rham/Hodge sequences C54/3 and C54/5; no matching pair of real conjugations is stated in those earlier pages. **Register:** LM7 C.1, Known (return claim), has Betti/de Rham realizations as a related comparison lead; it gives no separate real-conjugation statement in the supplied row. **Source:** the integration calculation in S2; [DK02], §5.1, as a checked lecture-note comparison. **Confidence:** high, from the explicit period identity and $F_\infty^2=1$; this fixes an explanatory convention without changing any uncertain manuscript symbol.

### B05 — Polarization and real structures on one explicit elliptic torus

**Kind / comparison:** own idea; matrix calculation connecting the two operations. **Source:** P15/203 and P15/227, polarized-motive moduli. **Short quote:** “motifs polarisés”.

> On $E(\mathbf C)=\mathbf C/(\mathbf Z+i\mathbf Z)$, the matrices $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, $C=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, and $c=\operatorname{diag}(1,-1)$ give $JC=I$, $cCc^{-1}=-C$, and $c^tJc=-J$. Thus the positive form $u^tJCv$, geometric conjugation, and its multiplier are computed on the same lattice. On $SL_2(\mathbf R)$, $\operatorname{Int}(C)(g)=(g^t)^{-1}$, with fixed group $SO_2$, while $\operatorname{Int}(C)\circ\text{coefficient conjugation}$ on $SL_2(\mathbf C)$ fixes $SU_2$.

**Context search:** `polari|positiv|dualité|duaux|Poincaré` finds C54/3, C54/5 and C44/8–9; earlier notes D02 and D13 are pairing/positivity leads. **Register:** LM7 C.1, Known (return claim), for Cartier-dual realizations; `WG2 §2.3 #12`, unchecked plan, for the polarization programme. **Source:** direct S2 calculation; [Mil94], Lemma 1.5 and Proposition 1.6, pp. 7–8, for the stated polarization/Cartan bridge. **Confidence:** high, because all matrices and fixed groups are exhibited; for a general Mumford–Tate group the cited proposition uses the quotient by the weight torus.

### B06 — Apply the registered generalized-Jacobian results to the current twist convention

**Kind / comparison:** source-linked application of registered results; explicit realization and duality maps. **Source:** P18/009, heading and twist formulas. **Short quote:** “Twist de Tate sur structures de Hodge mixtes”.

> LM7 C.1 records the Picard 1-motive/generalized-Jacobian duality, C.8 reports the rank-two toric and three-nonzero-two-torsion example, and C.5 reports the extension-order and splitting-degree result; these entries are cited at their stated return statuses. The contribution of current P18/009 is its concrete twist convention, which can be tracked through the homological torus/abelian weights $-2,-1$ and the cohomological dual weights $2,1$ in §S3. For the sequence maps $i:V_\ell T\to V_\ell J_D$ and $p:V_\ell J_D\to V_\ell J$, the dual arrows are explicitly $p^\vee(\varphi)=\varphi\circ p$ and $i^\vee(\psi)=\psi\circ i$, and the Cartier pairing takes values in $\mathbf Q_\ell(1)$.

**Context search:** “Tate|extension|Pic|dual” finds C44/8 and C54/3,5,7; the first Book II pages do not state the marked-point example. **Register:** LM7 C.1, Known (return's claim), §51.13–14, folios719–724, scans143–153; C.5, Proved (return's claim), Part C(b), Lead3, comparison with §51.14; C.8, Refuted (return's claim), §51.13–14, folios719–724, scans143–153. The unavailable LM7 source has not been independently checked. **Sources:** [D74], §§10.1.4–10.1.5, 10.2.10–10.2.11, 10.3.4–10.3.8, for realization and duality constructions. **Confidence:** high for the explicit dual arrows and realization comparison, because they are the stated duality constructions with their variance and Tate target displayed; register-only for the reported example, extension order, splitting degree, and tower conclusion.

### B07 — The cyclotomic character from actual conjugation

**Kind / comparison:** own calculation; explicit local-to-representation bridge. **Source:** P18/009, Tate twist; also P15/195, weight discussion. **Short quote:** “Twist de Tate”.

> For the Kummer tower $t^{1/\ell^n}$ at a rational cusp, write $\tau(t^{1/\ell^n})=\zeta_{\ell^n}t^{1/\ell^n}$. Conjugating this formula by an arithmetic lift of $\sigma$ gives $\sigma\tau\sigma^{-1}=\tau^{\chi_\ell(\sigma)}$, so the cusp-normalizer character on $I_\ell\simeq\mathbf Z_\ell(1)$ is explicitly cyclotomic. For two or more rational marked points, this is the character on each rank-one toric factor in S3.

**Context search:** `normalisateur|normalizer|cyclotom` has no hit in the first Book II transcription; `poids` there leads to the reused Lie typescript C44/7, whereas the relevant procyclic-normalizer statements occur in `notes/RESULTS_STATE.md`. **Register:** LM6 A.50, Proved (return claim), truncated after “Fix a prime”; LM6 A.22, Open (return claim), truncated in its deeper-kernel clause. **Sources:** direct Kummer calculation; [M-Abs], Lemma 1.3.7, p. 18, for geometric cusp inertia's commensurable terminality. **Confidence:** high for an actual cusp Kummer tower; no converse recognizing every normalized procyclic subgroup is inferred from the truncated register.

### B08 — A cusp visible in lower-central degree two

**Kind / comparison:** own idea; exact calculation of an abelianization kernel. **Source:** P18/009, mixed weights. **Short quote:** “structures de Hodge mixtes”.

> For $U=E\setminus\{0\}$ over $\mathbf Q$, the geometric fundamental group is generated by $a,b$ and the peripheral element is $[a,b]^{-1}$, hence its image in first abelianization is zero. In the pro-$\ell$ lower-central quotient of degree two, its class is the nonzero generator of $\bigwedge^2 T_\ell E\simeq\mathbf Z_\ell(1)$, and arithmetic conjugation acts by the determinant $\chi_\ell$. This gives a specific place where the cyclotomic character is recovered after passing beyond first homology.

**Context search:** `Tate|poids|normalisateur|cyclotom|commut|jacob|Betti` finds the C44/8 Tate-module discussion, but no once-punctured elliptic commutator calculation; the LM6 lead is confined to the results register. **Register:** LM6 A.22, Open (return claim), concerns a procyclic subgroup in a deeper common kernel; its complete group $R$ and the following truncated subgroup are unavailable, so the calculation is attached only as a comparison of the abelianization map. **Sources:** the group calculation in S4, the Weil pairing, and the cusp calculation B07. **Confidence:** high for this presentation and its degree-two bracket; no solution of LM6 A.22 is claimed.

### O01 — Oda identifies the Hodge subspace of $H^1$

**Kind / comparison:** unpursued implication; published reconstruction with exact operators. **Source:** P15/195, two filtrations; P15/211, $F,V$; P18/005, filtered crystalline realization. **Short quote:** “avec structure supplémentaire ((F,V))”.

> Oda's Corollary 5.11, for an abelian variety $X$ over a perfect field $k$ of characteristic $p$, gives a canonical contravariant Dieudonné-module isomorphism $M(X[p])\simeq H^1_{\mathrm{dR}}(X/k)$. Under it the Hodge subspace is $H^0(X,\Omega^1)=\operatorname{im}V=\ker F$, and Oda identifies the accompanying exact sequence with the Hodge sequence. His printed remark attributes this comparison conjecture to Grothendieck's 1966 de Rham paper.

**Context search:** `Dieudonn|de Rham|Froben|Versch|p^A|extension` finds C54/3,5,7, especially C54/7's final question whether the extension can be recovered from $p^A$; earlier note D05 cites exactly this corollary. **Register:** LM7 C.1, Known (return claim), is a related realization/duality lead; it supplies no new Oda theorem. **Source:** [O69], Definition 5.8, p. 124; Corollary 5.11 and its displayed sequences, p. 131; its bibliography [15], p. 134. **Confidence:** high: the corollary and both operator equalities were inspected in the rendered PDF, with Oda's contravariant convention retained.

### O02 — The two scalar operations in the Witt-vector question

**Kind / comparison:** own deduction from exact published functors. **Source:** P15/211, characteristic-$p$ line; P18/005, local $p$-divisible groups. **Short quotes:** “corps des fractions?” (preceded by an uncertain reading); “mod isogénie”.

> Set $D=M(X[p^\infty])$, a free $W(k)$-module of rank $2\dim X$ by Oda's Proposition 3.18. Exactness applied to multiplication by $p$ gives $D/pD\simeq M(X[p])\simeq H^1_{\mathrm{dR}}(X/k)$, while the map $D\hookrightarrow D[1/p]$ realizes the passage to isogenies. The identity $FV=p$ becomes $V=pF^{-1}$ on $D[1/p]$, explicitly relating the manuscript's two scalar choices and its additional operators.

**Context search:** `Dieudonn|Froben|Versch|extension` finds C54/5,7 and notes D03–D05; `isogén|Witt|fractions` adds no earlier statement of this exact three-term comparison. **Register:** LM7 C.1, Known (return claim), comparison lead only. **Source:** [O69], Corollary 3.16, Definition 3.17 and Proposition 3.18, pp. 88–89, combined with Corollary 5.11, p. 131. **Confidence:** high, because the kernel sequence and the two scalar maps are displayed in S5; this deduction concerns the characteristic-$p$ fibre specified in Oda's theorem.

### O03 — The general Picard comparison has an explicitly described image

**Kind / comparison:** unpursued implication; exact image formula fixing the comparison's scope. **Source:** P15/195, Hodge–de Rham filtration; P18/005, “pseudo-motifs”. **Short quote:** “pseudo-motifs”.

> Oda's Corollary 5.12 gives, for smooth proper $X/k$ with a $k$-point over a perfect characteristic-$p$ field, a canonical injection $D M({}_p\operatorname{Pic}_{X/k})\hookrightarrow H^1_{\mathrm{dR}}(X/k)$ with image $\bigcap_n\ker(d\circ V^n)$. Here the $D$ before $M$ is Oda's module duality, and the iterated Cartier maps have the successive domains defined before Definition 5.8. Theorem 5.10 constructs this map; the abelian-variety isomorphism O01 is its specified full-image case.

**Context search:** `Pic|Cartier|de Rham|extension` finds C54/3,5,7 and notes D01–D05; Oda's common-kernel formula does not occur in those earlier manuscript pages. **Register:** LM7 C.1, Known (return claim), for Picard 1-motives; no extra implication for its Fermat tower is drawn from this formula. **Source:** [O69], pp. 123–126, Theorem 5.10; Corollary 5.12, p. 131. **Confidence:** high for the source statement and image formula; S5 retains the domains rather than treating every $V^n$ as an unrestricted endomorphism of arbitrary de Rham cohomology.

### O04 — A local Tate-curve calculation for the filtered-crystal programme

**Kind / comparison:** own idea using a verified published example; explicit local realization test. **Source:** P18/005, local descriptions 5′–6′. **Short quote:** “cristal filtré”.

> For the Tate elliptic curve $E_p/\mathbf Q_p$, the representation $V_p(E_p)$ is the extension $0\to\mathbf Q_p(1)\to V_p(E_p)\to\mathbf Q_p\to0$ supplied by the Kummer class of $p$. With $\log_p p=0$, its contravariant filtered semistable module has a basis $e_1,e_2$ with $\varphi e_1=e_1$, $\varphi e_2=pe_2$, $Ne_2=e_1$, $Ne_1=0$, and $\operatorname{Fil}^1=\mathbf Q_p e_2$. The exact relation $D_{\mathrm{cris}}^*=\ker(N:D_{\mathrm{st}}^*\to D_{\mathrm{st}}^*)$ has dimensions one inside two in this example, which supplies a concrete monodromy calculation beside the page's filtered-crystal entry.

**Context search:** `cristal|p.divisible|isogén|Froben|Cartier|Tate|monodrom|extension|T_\{` finds C54/5,7 and C44/8; no local Tate-curve or monodromy calculation occurs in the first Book II transcription. **Register:** LM7 C.1 and C.5, Known/Proved (return claims), provide realization and extension leads only. **Sources:** [BC09], pp. 124–126, Example 9.2.1 p. 136 and Example 9.2.9 pp. 142–143; [F94], §5.1.6, p. 156. **Confidence:** high for the fixed curve and displayed module; the example retains semistable monodromy and does not specify a missing hypothesis for the manuscript's broad local programme.

## Supporting calculations and source scopes

### S1. Hom maps and the genus-two image calculation

Let $K$ be a number field and $X,Y/K$ smooth proper geometrically connected curves with rational basepoints. The covariant Albanese maps give the commutative chain

\[
f:X\longrightarrow Y\quad\mapsto\quad
\pi_1(f)\quad\mapsto\quad
\pi_1(\overline X)^{\mathrm{ab},\ell}\longrightarrow
\pi_1(\overline Y)^{\mathrm{ab},\ell}
\quad=\quad T_\ell\operatorname{Alb}(f):T_\ell J_X\longrightarrow T_\ell J_Y.
\]

Changing basepoints changes the fundamental-group homomorphism by inner conjugation; abelianization removes that conjugation. Using $f^*:J_Y\to J_X$ instead would require reversing the variance, so the displayed comparison uses $\operatorname{Alb}(f)$.

The source scopes are precise: [T66], Main Theorem, p. 134, treats abelian varieties over a finite field, with $\ell$ different from its characteristic. [F83], Satz 3–4, p. 360, treats abelian varieties over a number field: rational Tate-module semisimplicity and the integral endomorphism comparison; the Hom comparison follows by taking the off-diagonal block of $\operatorname{End}(A\times B)$. [M-Hom], Theorem A, author PDF p. 3, uses a sub-$p$-adic field $K$, a smooth pro-variety $X$, and a hyperbolic pro-curve $Y$: dominant $K$-morphisms correspond to open augmentation-compatible group homomorphisms, modulo inner conjugation by the geometric target group, for the profinite and geometric pro-$p$ versions stated there.

Now fix $X/\mathbf Q:y^2=x^5-x$ with its smooth projective completion and its rational point at infinity. The polynomial has five distinct roots; together with infinity these give six branch points of the degree-two map to $\mathbf P^1$, so $g(X)=2$. For a nonconstant self-map, Riemann–Hurwitz is

\[
2=2\deg(f)+\sum_x(e_x-1).
\]

Thus $\deg(f)=1$ and $f$ is an automorphism; its Albanese map has an inverse. In contrast, $[2]:J_X\to J_X$ has degree $2^{2g}=16$. Equivalently, for the canonical principal polarization $\lambda$, an induced curve automorphism has $f_*^\vee\lambda f_*=\lambda$, whereas $[2]^\vee\lambda[2]=4\lambda$. The actual Tate-module homomorphism $2I$ therefore exists and is Galois equivariant; these calculations identify why it is outside this curve-morphism image.

### S2. Period conjugations and the polarization matrices

Write the integration comparison in real bases as $I(w)=Pw$. Geometric complex conjugation has a real Betti matrix $R$; for a differential defined over $\mathbf R$,

\[
\int_{c\gamma}\omega=\overline{\int_\gamma\omega},
\qquad RP=\overline P,\qquad R^2=I.
\]

Consequently $R\overline P=P$. Coefficient conjugation on Betti cohomology sends $z\mapsto\bar z$, while the transported de Rham conjugation is $Pw\mapsto P\bar w$; hence $c_{\mathrm{dR}}=R c_B$. This proves the product identity in B04, including commutativity of the two semilinear involutions. [DK02] §5.1 records the same infinite-Frobenius factorization, but its introduction explicitly describes the text as Kedlaya's transcription of Deligne's lectures; the calculation above is supplied independently.

For the square elliptic torus, take the lattice basis $1,i$ and $Q(u,v)=u^tJv$. Direct multiplication gives

\[
JC=I,\quad C^2=-I,\quad c^2=I,\quad
c^tJc=-J,\quad cCc^{-1}=-C,
\qquad Q(u,Cv)=u^tv.
\]

For $g\in SL_2$, $g^tJg=J$ yields $CgC^{-1}=(g^t)^{-1}$. Its real fixed group is ${g:g^tg=I,\det g=1}=SO_2$; the semilinear involution $g\mapsto C\bar gC^{-1}=(\bar g^t)^{-1}$ fixes $SU_2$. The Galois-equivariant Weil pairing $T_\ell E\times T_\ell E\to\mathbf Z_\ell(1)$ gives $e_\ell(cx,cy)=\chi_\ell(c)e_\ell(x,y)=-e_\ell(x,y)$, agreeing with the computed multiplier.

[Mil94], Lemma 1.5, relates a $C$-polarization on a faithful real representation to the Cartan involution $\operatorname{Int}(C)$. Proposition 1.6 applies this to a polarizable rational Hodge structure, with $C=h(i)$, on $(G/w_h(\mathbf G_m))_{\mathbf R}$; retaining that quotient avoids silently imposing a compactness assertion on the weight torus.

### S3. Marked curves, integral weights, and explicit dual arrows

For the current Hodge comparison, work over a characteristic-zero field $K$ with a fixed embedding into $\mathbf C$. Fix a smooth proper curve $C/K$ with $r>0$ rational marked points $D$, $J=\operatorname{Pic}^0(C)$, and generalized Jacobian $J_D$. Rigidifications of a trivial line bundle at the marked points, modulo a common scalar, give the exact torus

\[
T=(\mathbf G_m^D)/\mathbf G_m,\qquad
X^*(T)=\ker(\mathbf Z^D\xrightarrow{\sum}\mathbf Z)=\operatorname{Div}^0_D,
\qquad T\simeq\mathbf G_m^{r-1}.
\]

With overbars denoting base change to an algebraic closure of $K$, and $\ell$ invertible in $K$, the realization sequence and its cohomological dual are

\[
0\to\mathbf Z_\ell(1)^{r-1}\xrightarrow{i}T_\ell J_D\xrightarrow{p}T_\ell J\to0,
\]
\[
0\to H^1(\overline C,\mathbf Q_\ell)\xrightarrow{p^\vee}
H^1(\overline{C\setminus D},\mathbf Q_\ell)
\xrightarrow{i^\vee}\operatorname{Div}^0_D\otimes\mathbf Q_\ell(-1)\to0.
\]

Here $V_\ell=T_\ell\otimes\mathbf Q_\ell$, and the cohomological identification is
$H^1(\overline{C\setminus D},\mathbf Q_\ell)
=\operatorname{Hom}(V_\ell J_D,\mathbf Q_\ell)$.
Thus $p^\vee(\varphi)=\varphi\circ p$ and $i^\vee(\psi)=\psi\circ i$; the toric dual is
$\operatorname{Hom}(V_\ell T,\mathbf Q_\ell)
=X^*(T)\otimes\mathbf Q_\ell(-1)$.
In the mixed-Hodge homological convention, with the matching weight filtration on the étale realization, the toric and abelian pieces have weights $-2,-1$; after the displayed duality their cohomological weights are $2,1$, respectively. This is the explicit weight and variance comparison with the Tate twist on current P18/009.

Deligne's 1-motive $M=[\operatorname{Div}^0_D\to J]$ has Cartier dual $M^\vee=[0\to J_D]$ through the Poincaré biextension and the canonical Jacobian polarization. Its pairing is
\[
T_\ell M\times T_\ell M^\vee\longrightarrow\mathbf Z_\ell(1),\qquad
y\longmapsto\bigl(x\longmapsto\langle x,y\rangle\bigr),
\]
identifying $T_\ell M^\vee$ with
$\operatorname{Hom}(T_\ell M,\mathbf Z_\ell(1))$.
These are the realization and duality constructions specified in [D74] and reported by LM7 C.1 [Known, return's claim].

For the marked elliptic example and its splitting calculation, cite LM7 C.8 [Refuted, return's claim] for the reported rank-two toric tower and elliptic generalized Jacobian with three nonzero two-torsion marked points, and LM7 C.5 [Proved, return's claim] for its reported extension-order, pullback-splitting and degree results. The present comparison adds the current page's twist/weight realization; it makes no independent proof claim about the unavailable LM7 source and does not repeat the reported extension-order or degree derivation.

### S4. Kummer conjugation and the punctured elliptic bracket

Choose compatible roots $t_n^{\ell^n}=t$ and $\zeta_{\ell^{n+1}}^\ell=\zeta_{\ell^n}$. An inertia generator sends $t_n\mapsto\zeta_{\ell^n}t_n$; an arithmetic lift fixing the chosen $t_n$ sends $\zeta_{\ell^n}\mapsto\zeta_{\ell^n}^{\chi_\ell(\sigma)}$. Evaluating the conjugate on $t_n$ proves the formula in B07 at every level and hence in the inverse limit. A different lift has the same conjugation action because $I_\ell$ is abelian.

For a once-punctured elliptic curve, the topological presentation is

\[
\pi_1(U(\mathbf C))=\langle a,b,\tau\mid[a,b]\tau=1\rangle.
\]

Eliminating $\tau$ gives the free group on $a,b$, and its maximal pro-$\ell$ quotient is free pro-$\ell$ on the same generators. Its second lower-central graded piece is generated by the alternating bracket $[a,b]$, identified with $a\wedge b$ in $\bigwedge^2(T_\ell E)$. An automorphism with matrix $M$ on first abelianization acts there by $\det M$; the Weil pairing gives $\det M=\chi_\ell(\sigma)$ for arithmetic action. Thus the peripheral element has zero first image but a nonzero cyclotomic image in degree two. This calculation concerns those specified quotients; the full common kernel $R$ in LM6 A.22 remains outside the supplied statement.

### S5. Oda's exact comparison and passage to isogenies

Oda's Dieudonné ring has generators $W(k),F,V$, with

\[
FV=VF=p,\qquad F\lambda=\lambda^\sigma F,
\qquad \lambda V=V\lambda^\sigma.
\]

Corollary 3.16 is the finite-group contravariant equivalence, Definition 3.17 takes the inverse limit on the module side, and Proposition 3.18 makes the module of a $p$-divisible group free over $W(k)$. Apply exactness to

\[
0\to X[p]\to X[p^\infty]\xrightarrow{p}X[p^\infty]\to0
\]

to obtain

\[
0\to D\xrightarrow{p}D\to M(X[p])\to0,
\qquad
D/pD\xrightarrow[\text{Oda 5.11}]{\sim}H^1_{\mathrm{dR}}(X/k).
\]

The associated Hodge sequence is

\[
0\to \operatorname{im}(V:D/pD\to D/pD)=\ker(F:D/pD\to D/pD)
\to D/pD\to H^1(X,\mathcal O_X)\to0,
\]

where the first term is identified with $H^0(X,\Omega^1_{X/k})$. More invariantly, the image $V(D/pD)$ is meant in the displayed first term; $pD\subset VD$ follows from $VF=p$. Definition 5.8 also gives $\operatorname{im}F=\ker V$ in the abelian/proper-curve cases treated there. The separate map $D\hookrightarrow D\otimes_{W(k)}W(k)[1/p]$ is injective because $D$ is free; on its target $F$ is invertible with $F^{-1}=p^{-1}V$.

For general smooth proper $X$, Oda defines Cartier iteration on successive domains. Theorem 5.10 and Corollary 5.12 identify the Picard-module image with the intersection of those domains expressed as $\bigcap_n\ker(dV^n)$. On p. 123 he illustrates the need to retain the domains with

\[
\omega=x^{p^n}\frac{dy}{y},\quad
V^j\omega=x^{p^{n-j}}\frac{dy}{y},\quad
dV^n\omega=\frac{dx\wedge dy}{y}\ne0.
\]

For $j<n$, the derivative is zero in characteristic $p$. This displayed computation supplies a concrete check on repeated Cartier operations; it is not asserted to be a global regular form on an arbitrary proper $X$.

For the local Tate-curve example O04, [BC09] uses the contravariant convention $D^*_{\mathrm{st}}(V)=\operatorname{Hom}_{G_K}(V,B_{\mathrm{st}})$. The Kummer class yields a matrix $\left(\begin{smallmatrix}\chi_p&\eta_p\\0&1\end{smallmatrix}\right)$; its period construction gives the two basis vectors used in O04. The calculation $N\varphi(e_2)=pe_1=p\varphi N(e_2)$ verifies $N\varphi=p\varphi N$, while $\ker N=\mathbf Q_p e_1$ has dimension one. Fontaine's §5.1.6 supplies the exact crystalline-kernel identification. This is the precise map for the fixed example, with the logarithm choice stated.

## Primary references checked

Publication references and checked author versions are separated where necessary. Titles, statement numbers and printed/page labels are given so the responsible reader can reopen the passages.

| Key | Reference and checked locator | Link |
|---|---|---|
| T66 | John Tate, *Endomorphisms of Abelian Varieties over Finite Fields*, Inventiones Mathematicae **2** (1966), 134–144. Main Theorem p. 134; product reduction Lemma 3 p. 135. | https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf |
| F83 | Gerd Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Inventiones Mathematicae **73** (1983), 349–366. Satz 3 and Satz 4 p. 360. | https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf |
| M-Hom | Shinichi Mochizuki, *The Local Pro-p Anabelian Geometry of Curves*. Theorem A, author PDF p. 3. | https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf |
| M-Abs | Shinichi Mochizuki, *The Absolute Anabelian Geometry of Hyperbolic Curves*. Definition 0.1 and Remark 0.1.3 pp. 3–4; Lemma 1.3.1 and Corollary 1.3.2 pp. 15–16; Lemma 1.3.7 p. 18. | https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf |
| DM82/22 | Pierre Deligne and James S. Milne, *Tannakian Categories* (1982); Milne's corrected 2022 text, with original numbering retained. Proposition 2.23 p. 26; Definition 5.1 p. 51. | https://www.jmilne.org/math/xnotes/tc2022.pdf |
| Mil94 | James S. Milne, *Shimura Varieties and Motives* (1994 publication; checked author final draft dated 1992/1993). Lemma 1.5 p. 7 and Proposition 1.6 pp. 7–8. | https://www.jmilne.org/math/articles/1994bP.pdf |
| D74 | Pierre Deligne, *Théorie de Hodge III*, Publications Mathématiques de l'IHÉS **44** (1974), 5–77. §§10.1.4–10.1.5 pp. 56–57; §§10.2.10–10.2.11 pp. 66–67; §§10.3.4–10.3.8 pp. 70–71. DOI 10.1007/BF02685881. | https://www.numdam.org/item/PMIHES_1974__44__5_0.pdf |
| O69 | Tadao Oda, *The first de Rham cohomology group and Dieudonné modules*, Annales scientifiques de l'École Normale Supérieure, série 4, **2** (1969), 63–135. Corollary 3.16–Proposition 3.18 pp. 88–89; Definition 5.8 p. 124; Theorem 5.10 p. 126; Corollaries 5.11–5.12 p. 131. DOI 10.24033/asens.1175. | https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf |
| F94 | Jean-Marc Fontaine, *Exposé III : Représentations p-adiques semi-stables*, Astérisque **223** (1994), 113–184. §5.1.6 p. 156 gives $D_{\mathrm{cris}}=\ker N$ in $D_{\mathrm{st}}$. | https://www.numdam.org/item/AST_1994__223__113_0.pdf |
| BC09 | Olivier Brinon and Brian Conrad, *CMI Summer School Notes on p-adic Hodge Theory*, author notes dated 24 June 2009. pp. 124–126, Example 9.2.1 p. 136, Example 9.2.9 pp. 142–143. This is checked author exposition, used together with Fontaine's original construction. | https://virtualmath1.stanford.edu/~conrad/papers/notes.pdf |
| DK02 | Pierre Deligne, lectures; Kiran Kedlaya, notes, *Periods for the Fundamental Group*, Arizona Winter School 2002. §5.1, “The infinite Frobenius.” Recorder's qualifications appear on p. 1. | https://swc-math.github.io/notes/files/02DeligneKedlayaCN.pdf |
| Deu41 | Max Deuring, *Die Typen der Multiplikatorenringe elliptischer Funktionenkörper*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **14** (1941), 197–272. Introduction no. 2 pp. 198–199; §2 no. 10 p. 218; characteristic-three example p. 234. DOI 10.1007/BF02940746. Located at the responsible reader's request for the separate P15/207 real-realization calculation. | https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1941.Deuring.pdf |
