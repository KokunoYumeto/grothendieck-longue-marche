# Research notes: arithmetic appendix and exact coordinate checks

These items concern the **frozen** transcription; mathematical corrections below do not edit it. Detailed proofs and primary references are in *arithmetic_evidence.md*; exact computations are in *arithmetic_certificate.py* and *arithmetic_certificate_output.txt*. Context searches are recorded in *arithmetic_context_searches.tsv*.

**Register scope for each item.** The supplied *notes/RESULTS_STATE.md* has no directly matching numbered quadratic-normality result. A01–A09 supply local arithmetic background for the orientation toward **LM4_SUCCESSOR B.38** and **EXIT_TOWER E.24**; L90–L92 concern level-four coordinates relevant to **LM4_SUCCESSOR B.38**; none of these items proves or refutes those open register statements. A10 additionally bears on the boundary comparison represented by **LM6 F.43**. This is a scope mapping, not a claim that local calculations settle the global problems.

## A01 — The normality test requires the DVR hypothesis

**Cote/scan/place:** 64/155, heading and first normality assertion. **Kind:** unproved claim; reading question about the hypothesis. **Quote:** “$B$ normal ssi $a\notin\mathfrak m^2$” under $p\ne2$.

For a DVR $A$, the assertion is correct: valuation one gives a DVR, valuation at least two produces the missing integral element $S/\pi$, and a unit gives an étale normal algebra when two is invertible. The frozen hypothesis reads “anneau jauge,” with a doubt mark; it must not be silently replaced by either “DVR” or “regular local ring of arbitrary dimension.” **Context — restates and checks:** Hua's modernised reading of cote 64, §VI “Normalité de $B=A[S]/(S^2-a)$” (its p.154 = scan 155), already imposes dimension one and gives $\mathbb Q[[x,y,S]]/(S^2-xy)$ as a normal counterexample to the broader necessity; the evidence appendix verifies that lead. The primary background is the Stacks Project Authors (n.d., Tags 00P7, 031O, and 02JN).

## A02 — Residual inseparability and an intrinsic first-order obstruction

**Cote/scan/place:** 64/155, cases b)1°–2° and the marginal note. **Kind:** unproved claim. **Quote:** “ne dépend que de $a$, et pas du choix de $\alpha$.”

For any DVR of residual characteristic two, a unit with nonsquare residue gives a normal DVR with purely inseparable residue extension $k(\sqrt{\bar a})/k$, so this case is not étale. In the square-residue case, $b=\alpha^2-a$ defines an intrinsic class in $\mathfrak m/\mathfrak m^2$, since changing $\alpha$ by $m\in\mathfrak m$ changes $b$ by $2\alpha m+m^2$, and normality is equivalent to this class being nonzero. **Context — restates and checks:** Hua, cote 64 §VI, gives the same cases and independence calculation; the proof here makes explicit that no perfect-residue-field or henselian hypothesis is needed. This distinction is necessary for scan 156's passage from a normal order to a generically étale normalization (Stacks Project Authors, n.d., Tags 00P7 and 02GI).

## A03 — The ordinary-double-point conclusion needs $v(2)=1$

**Cote/scan/place:** 64/155, bottom marginal assertion; compare 64/157, quadratic scratch calculations. **Kind:** unproved claim; unrestricted statement refuted, refined as **A03.R**. **Quote:** “Ce dernier cas correspond à une … singularité quadratique ordinaire.”

For $a=\alpha^2-b$ a unit and $b\in\pi^2A$, the tangent quadratic is $X^2+\overline{2\alpha/\pi}XY+\overline{b/\pi^2}Y^2$, geometrically nondegenerate in residual characteristic two exactly when $v(2)=1$. The unrestricted claim fails for $A=\mathbb F_2[[\pi]],a=1+\pi^3$, which gives a cusp, and for the mixed-characteristic DVR $A=\mathbb Z_2[\sqrt2],a=5$, which has doubled tangent line $T^2=0$. **Context — adds a qualification:** Hua's cote 64 §VI checks normality without stating this additional ordinary-node hypothesis; it holds for the application's actual vertical ring $\mathbb Z[T]_{(2)}$ and is pertinent to scan 157's cross-term calculation. This restriction concerns singularity type, not the general DVR normality criterion (Stacks Project Authors, n.d., Tag 02DN).

## A04 — Codimension-one normality already gives global normality here

**Cote/scan/place:** 64/154, final paragraph. **Kind:** unpursued implication; own deduction. **Quote:** “$B$ est normal en codim $1$” and “un nb fini … pts non normaux.” **Confidence:** high, from the hypersurface property and Serre's criterion.

For $P=\varepsilon qQ$ in scan 155's squarefree primitive form, $B=\mathbb Z[T,S]/(S^2-P)$ is a hypersurface and hence $S_2$; if the stated height-one checks hold, $R_1+S_2$ makes it normal everywhere. Thus the finite exceptional nonnormal set allowed by scan 154 is empty for this model, although the weaker manuscript assertion is not contradicted. **Context — adds:** Hua's cote 64 §VI describes the codimension-one calculation without this global sharpening, and the supplied register contains no directly matching numbered arithmetic result. This applies to the given hypersurface, not to an arbitrary finite order over a regular surface (Stacks Project Authors, n.d., Tags 02JN and 031O).

## A05 — Test the full signed radicand

**Cote/scan/place:** 64/154, dyadic criterion and examples; 64/155, factorization (1); 64/156, $\varepsilon Q$. **Kind:** reading question; mathematical qualification. **Quote:** “$Q(t)$ est un carré mod $4$.”

With $P=\varepsilon qQ$, nonnormality at the vertical prime two is equivalent to $P$, not bare $Q$, being square modulo four. For example $Q=1$ is square modulo four, while $P=3$ and $P=-1$ give normal dyadic orders; this refutes a bare-$Q$ criterion **if** it is read as omitting the sign and content, with refined statement **A05.R**. **Context — clarifies:** Hua's cote 64 §VI uses $\varepsilon Q$ after reducing to $q=1$, and scan 156 itself writes that signed expression, while scan 154's examples also carry sign annotations. No alteration of the frozen $P(t)\mid Q(t)$ doubt or of its later $Q$ follows from this arithmetic qualification.

## A06 — An integral generator proves the deferred sufficiency

**Cote/scan/place:** 64/156, before the example. **Kind:** unproved claim; proof supplied. **Quote:** “Cette condition est aussi suffisante.”

If $P=r^2+4h$ with $r,h\in\mathbb Z[T]$, then $u=(S+r)/2$ satisfies $u^2-ru-h=0$, and this order is the full normalization for the squarefree radicands under discussion. Its discriminant is $P$, and on $D(P)$ its derivative $2u-r$ is invertible because $(2u-r)^2=P$, proving étaleness. **Context — adds a proof:** Hua's cote 64 §VI explicitly leaves the sufficiency unproved; the height-one checks together with $S_2$ establish it, and the displayed identity is verified by the certificate. Generic étaleness above every rational prime is equivalent to $q=1$ and $\varepsilon Q$ square modulo four, with at most one working sign for a fixed primitive $Q$ (Stacks Project Authors, n.d., Tags 02GI and 031O).

## A07 — Modulo two is weaker than the required modulo-four condition

**Cote/scan/place:** 64/156, displayed congruence for $Q(T)=T(T-\lambda)$. **Kind:** reading question; literal modulo-two equivalence refuted, refined as **A07.R**. **Quote:** “$\lambda\equiv0\ (4)$.”

The exact result is that $T(T-\lambda)$ is square modulo four precisely when $4\mid\lambda$, and only the positive sign can work. In contrast $T(T-\lambda)\equiv T^2\pmod2$ requires only $2\mid\lambda$, so $\lambda=2$ refutes its literal equivalence with $4\mid\lambda$. **Context — restates and checks:** Hua's cote 64 §VI already identifies the useful modulo-four congruence; the present proof establishes both necessity and sufficiency using the unique square-root reduction in $\mathbb F_2[T]$. The doubtful marker before “(2)” remains unchanged.

## A08 — The final infinity-chart radicand has the opposite sign

**Cote/scan/place:** 64/156, final displays and the $T'=1/T$ margin. **Kind:** reading question; literal cover claim refuted, refined as **A08.R**. **Quote:** “un revêtement étale” and “$T'=1/T$.”

For $\lambda=4m$ and $x=1/T$, the normalized finite étale model on the projective complement is $u^2-u+mx=0$, with discriminant $1-\lambda x$. The frozen radicand $\lambda x-1$ has the opposite sign, is congruent to $-1\pmod4$, and remains ramified at two after normalization; $\lambda=4,x=0$ gives $\mathbb Z[i]$ with a nonreduced characteristic-two fibre. **Context — adds a check absent from the unfinished treatment:** Hua's cote 64 §VI verifies the affine congruence and says the manuscript stops after changing coordinates, but does not check this last sign. The corrected model and overlap substitution $U=Tu$ are consequences of A06, not changes to the transcription (Stacks Project Authors, n.d., Tag 02GI).

## A09 — The completion formula can hold for noncomplete $A$

**Cote/scan/place:** 64/155, the display containing $\widehat B$. **Kind:** unproved claim; scope qualification. **Quote:** “$\widehat B\simeq A[[T]]/(T^2+2\alpha T+b)$.”

The displayed quotient is always the $T$-adic completion; when $b\ne0$, $B/(T)=A/(b)$ has finite length, so the $T$-adic and maximal-ideal-adic topologies coincide. Thus the formula is valid in the genuine quadratic-field case even for noncomplete $A$, since nonsquare $a$ forces $b\ne0$. **Context — adds an omitted check:** Hua's cote 64 §VI does not reproduce this completion step; in the unrestricted split example $A=\mathbb Z_{(2)},a=\alpha=1,b=0$, reduction modulo $T$ distinguishes the displayed quotient from the maximal-ideal completion, so that boundary case needs its topology specified. This qualification uses exactness of Noetherian completion and does not challenge the intended field-extension application (Stacks Project Authors, n.d., Tag 0BNH).

## A10 — The corrected cover splits at infinity

**Cote/scan/place:** 64/156, infinity-chart example. **Kind:** own idea; unpursued implication. **Quote:** “$T'=1/T$.” **Confidence:** high, by direct specialization of A08.R.

In the corrected model the infinity fibre is $u(u-1)=0$, two disjoint integral sections, and its characteristic-two equation $u^2+u+\bar m x=0$ is split for even $m$ and a connected Artin–Schreier affine-line double cover for odd $m$. **Context — adds and distinguishes:** Hua's cote 64 §VI leaves infinity unfinished, whereas *MPL_149_091-136_notes.md*, RN099-03 (scans 099–100), proposes a Tate-cusp degeneration with nontrivial unipotent inertia. The unramified fibre of this quadratic cover does not itself identify the announced modular degeneration or its tangential place. It supplies a boundary test for comparison with **LM6 F.43**, leaving **LM4_SUCCESSOR B.38** and **EXIT_TOWER E.24** unchanged.

## L90 — Two signs in the assembled fourth-division equations

**Cote/scan/place:** 64/118, (71), first bracket and first marginal display; compare 64/116, (61)–(65). **Kind:** unproved claim; literal identities refuted, refined as **L90.R**. **Quote:** “En mettant ensemble les équations pertinentes.”

With $r=\zeta_i,u=\zeta_\lambda,v=\zeta_\mu$, the principal radical is $(r-u)(r-v)=-(a_1r+2a_2-3uv)$, whereas the frozen bracket with $+3uv$ differs by $-6uv$, and the marginal fixed-point constant differs by $-4uv$. At $(r,u,v)=(1,2,3)$ the correct radical is $2$ and the literal bracket is $-34$. **Context — restates and independently checks:** Hua's cote 64 “Les involutions … et les points d'ordre 4,” footnote at its p.117 = scan 118, already flags both signs; the certificate verifies the identities symbolically. This agreement with Hua's arithmetic does not authorize altering the frozen expressions.

## L91 — The zero-root case has an undivided polynomial formula

**Cote/scan/place:** 64/116, margins around (62) and (65). **Kind:** reading question; verification of a self-flagged domain qualification. **Quote:** “Si $\zeta_i=0$.” **Confidence:** high, by the matrix identity in the evidence appendix.

The polynomial $(\zeta_i-\zeta_\lambda)(\zeta_i-\zeta_\mu)$ extends to $\zeta_i=0$ with value $\zeta_\lambda\zeta_\mu$, and the involution becomes $z\mapsto\zeta_\lambda\zeta_\mu/z$. Its undivided matrix squares to that radical times the identity, giving a check without evaluating $0/0$. **Context — restates and checks:** Hua's cote 64 “Les involutions …” supplies the factorization and the zero-root concern; the exact certificate verifies the extension and separates it from the sign-defective marginal alternative. Distinct roots and characteristic unequal to two remain the hypotheses of the elliptic-coordinate application.

## L92 — Basis signs are determined, but the pinning is unfinished

**Cote/scan/place:** 64/123 and 64/125–126, kernel vector and boxed basis formulas. **Kind:** reading question; unpursued implication. **Quote:** “$t$ correspond donc à.”

For $\Delta_0=(\zeta_1-\zeta_2)(\zeta_2-\zeta_3)(\zeta_3-\zeta_1)\ne0$, the preceding system forces $\Delta_0f_1=\sum_i(\zeta_j-\zeta_k)e_i$ and $-\Delta_0f_2=\sum_i\zeta_i(\zeta_j-\zeta_k)e_i$; all three equations and both kernel constraints were checked exactly. A minus before $\Delta_0f_1$ would contradict that system, but the frozen dot-or-minus doubt remains a reading question. **Context — restates and checks:** Hua's cote 64 “Vers l'épinglage de Legendre,” its pp.122–125, gives the formulas and connects the line to condition b). This does not settle condition c), explicitly deferred on scan 121, and therefore completes neither the canonical pinning nor a congruence-kernel claim.

## Primary-source URLs for review

APA entries appear in *arithmetic_evidence.md*.

- DVR/one-dimensional normality: https://stacks.math.columbia.edu/tag/00P7
- Cohen–Macaulay quotient: https://stacks.math.columbia.edu/tag/02JN
- Serre's criterion: https://stacks.math.columbia.edu/tag/031O
- Standard étale criterion: https://stacks.math.columbia.edu/tag/02GI
- Étale algebras over Dedekind rings: https://stacks.math.columbia.edu/tag/0AP2
- Ordinary double point in characteristic two: https://stacks.math.columbia.edu/tag/02DN
- Exact completion: https://stacks.math.columbia.edu/tag/0BNH
