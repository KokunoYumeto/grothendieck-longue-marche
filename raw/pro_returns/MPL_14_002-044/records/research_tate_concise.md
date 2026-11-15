# Tate and Serre-letter notes for the final edition

T means `context/MPL_16+47+54+44_transcription.tex`, N means `context/MPL_16+47+54+44_notes.md`, and R means `context/notes/RESULTS_STATE.md`. The RT-numbered searches and longer calculations are retained in `records/research_tate_context_searches.md` and `records/research_tate_letter.md`.

## RT1 — The exact quotient between the two cycle formulations

**Location:** `pages/MPL_14_002-044_14_scan044.tex`, lines6–8. **Kind:** unpursued implication. **Quote:** “mod équivalence algébrique, tensorisé par $\underline{\mathbb Q}$”. **Context:** T, cote16 scans044–045, dimension and critical-degree comparisons; N, S1. **Delta:** adds an explicit quotient to the provisional lettering dictionary. **R:** WG2 §2.4 #3 [unchecked planning item]. **Search:** RT1.

The letter's group $C^i_{\mathrm{alg}}(X)$ maps to the published rational cycle-class image $A_H^i(X)$ by $q_i([z]_{\mathrm{alg}})=\mathrm{cl}_H(z)$, with exact sequence $0\to\operatorname{Griff}_H^i(X)_{\mathbb Q}\to C^i_{\mathrm{alg}}(X)\xrightarrow{q_i}A_H^i(X)\to0$ [G69, §2; K68, §1.2.1]. Algebraic equivalence maps to zero because the class of a family restricts identically at all points of a connected parameter space, and the kernel is therefore precisely homological equivalence modulo algebraic equivalence. Multiplicativity gives $q_{n-i}(\xi^{n-2i}z)=\mathrm{cl}_H(\xi)^{n-2i}\cup q_i(z)$, the exact map relating the letter's formulation to published A; it retains the rational image rather than replacing it by its entire $\mathbb Q_\ell$-span.

## RT2 — A quintic threefold tests the letter's written A

**Location:** `pages/MPL_14_002-044_14_scan044.tex`, lines6–10. **Kind:** own idea. **Quote:** “Le premier cas qui échappe pour le moment est $i=1,n=3$”. **Context:** T, cote44 scan006, Theorem7; cote16 scan046, uncertain $\tau$ annotation; N, D14. **Delta:** applies the earlier Clemens lead directly to the written multiplication map, without identifying the context's uncertain $\tau$. **R:** WG2 §2.4 #3 and §2.1 #5 [unchecked planning items]; no matching settled result entry. **Search:** RT2. **Confidence:** high, from the displayed map, its intersection with the kernel, and the identified primary result.

For a very general smooth quintic threefold $V\subset\mathbf P^4_{\mathbf C}$, weak Lefschetz and the divisor cycle-class map give $C^1_{\mathrm{alg}}(V)=\mathbb QH$, so the letter's map is $aH\mapsto aH^2$. Clemens's equation(0.1) and Theorem(0.2) give nonzero elements of $\operatorname{Griff}^2(V)_{\mathbb Q}\subset C^2_{\mathrm{alg}}(V)$ [C83, pp.19–20]. The image $\mathbb QH^2$ meets that kernel only at zero, since $q_2(aH^2)=0$ gives $5a=\int_VaH^3=0$, proving failure of surjectivity for the exact algebraic-equivalence formulation written here. Passing through $q_2$ removes precisely these obstructing kernel classes, which explains the relationship to the published statement without altering the transcription.

## RT3 — Draft lettering and the printed operator dictionary

**Location:** `pages/MPL_14_002-044_14_scan044.tex`, lines6–12. **Kind:** reading question. **Quote:** “les deux conjectures-clef”; “Conjecture A”. **Context:** T, cote16 scans044–045 and048–049; N, S1. **Delta:** adds an explicit earlier A and checks the inverse-operator part of the earlier dictionary. **R:** WG2 §2.4 #3 [unchecked planning item]. **Search:** RT3.

The surviving letter defines A but ends before a second conjecture, while cote16's draft $C_\ell$ is expressed through algebraic inverse Lefschetz maps, the operator content called B in the printed account [G69, §§2–3; K68, §§2 and3.6]. A correspondence acts by $z_*(a)=p_{2*}(p_1^*a\cup\mathrm{cl}(z))$, and the draft's maps $v=L^{n-i}$ and $u$ give $v^{-1}=(uv)^{-1}u$, with both composites the identity. Its characteristic-polynomial construction writes $(uv)^{-1}$ as a rational polynomial in $uv$, as checked explicitly in the retained evidence record. These operator identities justify the printed dictionary below and the draft-$C_\ell$/printed-B comparison, while the supplied occurrences do not furnish standalone definitions for every draft B and D.

| Printed letter | Content in the checked published sources | Supplied manuscript comparison |
|---|---|---|
| A | Hyperplane multiplication on the rational space of algebraic cohomology classes; G69 also lists cohomological hard Lefschetz under A | Scan044 uses $C^i_{\mathrm{alg}}$; RT1 gives the quotient map and RT2 its kernel obstruction. |
| B | Algebraicity of the Lefschetz inverse/lowering operator | Cote16 scans045,048–049 give this operator content under draft $C_\ell$. |
| C | Algebraicity of Künneth projectors | The printed definition is explicit; occurrences of draft D alone do not establish a complete letter identification. |
| D | Equality of homological and numerical equivalence | K68 §3.6 is explicit; relations asserted for draft B are insufficient to recover its full definition. |

## RT4 — The reduction is explicitly unwritten, and its continuation is missing

**Location:** `pages/MPL_14_002-044_14_scan044.tex`, lines8–12. **Kind:** self-flagged. **Quote:** “Modulo vérification que je n'ai pas écrite en détail”. **Context:** T, cote16 scans045–047; N, 16:47:3. **Delta:** adds an explicitly qualified earlier witness to the context's strong-to-weak Lefschetz programme. **R:** WG2 §2.4 #3 and §6 #9 [unchecked planning items]. **Search:** RT4.

The author proposes reducing A to surjectivity in odd dimension $n=2i+1$, with an explicit reservation that the verification has not been written out. The later maps for a smooth hyperplane inclusion $j:Y\hookrightarrow X$ are restriction $j^*$ and Gysin $j_*$, related by $j_*j^*=L_X$ [K68, §1.4.7]. The surviving sheet ends during the Gysin sentence and carries a continuation sign, so the rest of that argument and the promised second conjecture are absent from the supplied letter fragment. The cohomological identity alone does not resolve the algebraic-equivalence kernel exhibited in RT1–RT2.

## RT5 — The elliptic-power example and the named Mumford verification

**Location:** `pages/MPL_14_002-044_14_scan041.tex`, line24; scan042, line2. **Kind:** unpursued implication. **Quote:** “a été vérifié pr Mumford”; “produit de deux courbes elliptiques”. **Context:** T, cote16 scan019; cote47 scans007,009; those Mumford occurrences concern other constructions. **Delta:** adds the specific finite-field attribution; no matching earlier assertion was found. **R:** no matching result entry. **Search:** RT5.

Tate's 1966 §1 expressly credits Mumford with deriving the elliptic-pair case from Deuring, closely matching the attribution and reduction in these pages [T66, p.134]. The comparison is the map $\operatorname{Hom}_{\mathbf F_q}(A,B)\otimes\mathbf Z_\ell\to\operatorname{Hom}_{G_{\mathbf F_q}}(T_\ell A,T_\ell B)$, $f\mapsto T_\ell f$, for $\ell\ne\operatorname{char}\mathbf F_q$. For divisors on $C\times C$, the intervening map sends $\mathcal L$ to $x\mapsto[\mathcal L|_{\{x\}\times C}\otimes(\mathcal L|_{\{0\}\times C})^{-1}]\in C^\vee$, followed by its Tate-module action. Milne's Appendix A.3 example verifies divisor generation of Tate classes for all powers of such an elliptic curve [Milne01, p.15].

## RT6 — The two inclusions and the unverified general equality

**Location:** `pages/MPL_14_002-044_14_scan041.tex`, lines10–22; scan042, lines4–10. **Kind:** unproved claim. **Quote:** “à priori on a les inclusions”; “l'hypothèse implique l'égalité des extrêmes”. **Context:** T, cote44 scan008, Tate-module paragraph; N, D10. **Delta:** adds a divisor-generation assertion not supplied by that earlier realization paragraph. **R:** no matching settled entry proves the displayed general equality. **Search:** RT6.

The decomposable classes are reached by the cup-product map $\operatorname{Sym}^i_{\mathbf Q_\ell}(H^2(A,\mathbf Q_\ell(1))^{\mathrm{alg}})\to H^{2i}(A,\mathbf Q_\ell(i))$, $d_1\cdots d_i\mapsto d_1\cup\cdots\cup d_i$. The text writes the two inclusions and asserts equality of the outer terms from its hypotheses, leaving the uncertain general condition b) without a full invariant-theoretic verification. For a finite-field model, geometric Tate classes are $\bigcup_{r\ge1}\ker(F^r-1)$ on the twisted cohomology, and [Milne01, §1 and AppendixA.3] verifies the divisor-generation example used in RT5. The passage's $\mathfrak g$-invariants retain their literal notation because the supplied text does not define the precise monodromy group identifying them with that union.

## RT7 — A precise test of the Frobenius wording

**Location:** `pages/MPL_14_002-044_14_scan041.tex`, lines4–8 and16–22. **Kind:** reading question; own idea for the explicit test. **Quote:** “$\varepsilon q^{-1/2}$, $\varepsilon$ une racine de l'unité”; `\unsure{Pr. Tits}`. **Context:** T, cote54 scans005,007; N, D03 andS17; the context has no matching convention for the uncertain “pseudoalgébrique”. **Delta:** adds a convention question and an explicit numerical test. **R:** no matching entry. **Search:** RT7. **Confidence:** high for the calculation; the author's intended convention and Tits reference remain unresolved.

The exact duality change is $F\mapsto(F^{-1})^{\mathsf t}$, sending an eigenvalue $\alpha$ to $\alpha^{-1}$, while scalar extension is $V_\ell(A)\to V_\ell(A)\otimes_{\mathbf Q_\ell}K$, $v\mapsto v\otimes1$ [T66, §1]. For $E/\mathbf F_5:y^2=x^3+x+1$, the affine point counts $2,0,2,2,2$ and the point at infinity give nine points, so $\alpha=(-3+\sqrt{-11})/2$ is a Frobenius eigenvalue and $\beta=\alpha/\sqrt5$ satisfies $(\beta+\beta^{-1})^2=9/5$. A root of unity and its inverse have algebraic-integer sum, whose square cannot be the rational noninteger $9/5$, proving that $\alpha^{-1}$ has absolute value $5^{-1/2}$ without the written root-of-unity form. This exact obstruction explains why the exponent, root-of-unity requirement, omitted tensor factor, and alternative two-piece formulation must be interpreted separately, while leaving all frozen readings and the unverified Tits attribution intact.

## RT8 — The singular programme has no explicit continuation in these supplied pages

**Location:** `pages/MPL_14_002-044_14_scan044.tex`, lines6 and10–12; bounded search of all40 frozen page files. **Kind:** reading question. **Quote:** “variété projective lisse connexe”; “section hyperplane lisse”. **Context:** T, cote16 scan047, “work also with singular ones”; N, 16:47:4–6; `context/README.md`, singular-hypersurface question. **Delta:** supplies a smooth formulation and no explicit singular-variety reformulation in the retained text. **R:** WG2 §2.4 #3 [unchecked planning item]; no separate settled singular-programme entry. **Search:** RT8 andRT8-F.

Cote16 scan047 proposes singular hypersurfaces and a reformulation of the standard conjectures for singular varieties after reporting Serre's objection to the preceding smooth reduction. The supplied letter uses a smooth projective variety, a smooth hyperplane section, and the maps $j^*,j_*$ in RT4. A search of all40 frozen pages for singularity, hypersurface, resolution, birational, and specialization vocabulary found no explicit continuation of that programme, and the review of the actual arguments supplies no such construction. This documentary conclusion is limited to the supplied pages and does not assign a verdict to unavailable cotes12,13,15 or18.
