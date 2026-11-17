# Local section and Hom comparison: a checked inference from Raynaud

**Status:** checked literature inference for main note **N79**, supplementing N33–N35. The scalar comparison below follows from a published theorem of Michèle Raynaud and elementary local algebra. The reduction has been checked by the root reviewer and independently by the context reviewer; this records that mathematical check, not a claim of external refereeing or novelty.

**Manuscript and project credit:** the frozen text of cote 58, scan46, imposes depth at least two on both F′ and G′ outside Y′. The target-only formulation is the registered lead **Hua, findings register, `58-local-hom-comparison-depth-off-y`**, and is developed in Hua's AI-produced modernised reading of cote 58, “Une forme locale,” their pp.45–51 = our scans46–52. The proof below is a literature-based verification of that section/Hom comparison, not a replacement transcription or a verification of the manuscript's essential-image and effectivity claims.

## 1. Precise statement and conventions

Let (A,m) be a noetherian local ring which is a quotient of a regular noetherian ring. Let t∈m, and assume that A is separated and complete for the t-adic topology. Put

\[
S=\operatorname{Spec}A,\qquad s=\mathfrak m,\qquad
P=S\setminus\{s\},\qquad D=V(t)\cap P,\qquad
U=P\setminus D=D_S(t).
\]

Here s denotes the closed point; the notation S\{s} removes that point, not a subscheme with an unspecified thickening. Write \(\widehat P\) for the formal completion of P along the ideal tO_P, and \(\widehat K\) for completion of a coherent O_P-module K.

For u∈P corresponding to a prime p⊊m, define

\[
C(u)=\overline{\{u\}}^{\,P}=V(\mathfrak p)\cap P,
\qquad d(u)=\dim(A/\mathfrak p).
\]

All dimensions of C(u) are topological Krull dimensions **in the punctured scheme P**. Thus \(\dim C(u)=d(u)-1\), and u is closed in P exactly when d(u)=1. Depth means \(\operatorname{depth}_{\mathcal O_{P,u}}K_u\); the zero module has depth +∞.

**Section comparison.** If K is coherent on P and

\[
\operatorname{depth}K_q\ge2
\quad\text{for every point q closed in P with q\notin D},
\tag{A}
\]

then the canonical map

\[
\Gamma(P,K)\longrightarrow\Gamma(\widehat P,\widehat K)
\tag{1}
\]

is an isomorphism.

**Target-only Hom comparison.** If F and G are coherent on P and G satisfies (A), then

\[
\operatorname{Hom}_{P}(F,G)
\longrightarrow
\operatorname{Hom}_{\widehat P}(\widehat F,\widehat G)
\tag{2}
\]

is an isomorphism. No depth condition on F and no t-regularity condition on F, G, or K is imposed in these assertions. If the manuscript's phrase “closed points of P−D” is interpreted as closed in U itself, its assumption still includes every point quantified in (A), so the stated conclusion follows under that interpretation as well.

## 2. Published comparison input

Raynaud (1974, I.0, I.1.1, I.1.3, pp.31–32), specialized to n=2, gives (1) provided U is affine and every u∈U satisfies

\[
\operatorname{depth}K_u\ge
\begin{cases}
2-\dim C(u),& C(u)\cap D\ne\varnothing,\\
2,& C(u)\cap D=\varnothing.
\end{cases}
\tag{R}
\]

The local completeness assumption is already part of our setup, and U=D_S(t) is affine. We use only this H⁰ conclusion; the proof below verifies (R) from (A). The printed inequalities and closure convention on pp.31–32 were visually checked by both the literature reviewer and root.

## 3. Elementary geometric and depth facts

### 3.1 Dimension after removing the closed point

For a noetherian local domain B of finite dimension d≥1, the punctured spectrum has dimension d−1. Every chain in that punctured spectrum can be extended by the maximal ideal, giving the upper bound; a chain of maximal length d in Spec B ends at the maximal ideal, and deleting it gives the lower bound. Apply this with B=A/p to obtain the convention \(\dim C(u)=d(u)-1\) above. No catenarity assumption is needed for this fact.

### 3.2 A height-one prime avoiding a prescribed nonzero element

Let (B,n) be a noetherian local domain with dim B≥2, and let 0≠a∈n. The height-one primes containing a are exactly the minimal primes over (a): the principal ideal theorem gives height one, and two distinct primes of height one cannot strictly contain one another in a domain. There are finitely many of them. Prime avoidance gives b∈n outside their union; in particular b≠0. A minimal prime Q over (b) has height one, cannot contain a, and cannot be n, whose height is at least two.

When dim B=2, it follows that dim(B/Q)=1 and dim B_Q=1. Indeed, Q⊊n gives the lower bound dim(B/Q)≥1; a chain of length at least two above Q, preceded by (0)⊊Q, would contradict dim B=2. This is the specific dimension-two step; it does not require catenarity.

### 3.3 The depth-localization inequality

For a finite module M over a noetherian local ring R and a prime r⊂R,

\[
\operatorname{depth}M_r+\dim(R/\mathfrak r)
\ge\operatorname{depth}M.
\tag{3}
\]

This standard inequality is the only depth-propagation input. A complete elementary proof is given by the Stacks Project Authors (2026, Lemma 10.72.10, tag 0FCC); it proceeds by choosing an M-regular element in r when depth M>dim(R/r), and inducting after quotienting by that element. In the application below R=O_{P,q} and r=pO_{P,q}, so the dimension term will equal one.

## 4. Proof of the section comparison

Fix u∈U, corresponding to p⊊m. In B=A/p, the image a of t is nonzero because u∉D, and lies in the maximal ideal because t∈m.

**Case 1: C(u)∩D is empty.** Suppose d(u)≥2. A minimal prime of B over (a) has height one by the principal ideal theorem, hence is not the maximal ideal of B. Its inverse image in A therefore defines a point of P lying in both C(u) and V(t), a contradiction. Thus d(u)=1, so u is closed in P outside D and (A) gives depth K_u≥2. This is the second line of (R).

**Case 2: C(u)∩D is nonempty and dim C(u)≥2.** Then 2−dim C(u)≤0. Every nonzero finite module over a local ring has nonnegative depth, and the zero-module convention also satisfies this bound. Hence the first line of (R) is automatic.

**Case 3: C(u)∩D is nonempty and dim C(u)=1.** Now dim B=2. Use §3.2 with a=t mod p to choose a height-one prime Q⊊n of B avoiding a, and let q be its inverse image in A. Then t∉q and dim(A/q)=dim(B/Q)=1. Accordingly q is a point closed in P outside D, and (A) yields depth K_q≥2.

The point u is a generization of q. Apply (3) to the finite O_{P,q}-module K_q and the prime pO_{P,q}. Its localization is K_u, and

\[
\mathcal O_{P,q}/\mathfrak p\mathcal O_{P,q}
\simeq (A/\mathfrak p)_{\mathfrak q/\mathfrak p}
=B_Q,
\qquad \dim B_Q=1.
\]

Therefore depth K_u≥depth K_q−1≥1=2−dim C(u), as required. If K_u=0 this inequality holds by convention; if K_u≠0, K_q is also nonzero because the support of a coherent sheaf is closed under specialization.

These cases exhaust u∈U: if dim C(u)=0, then C(u)={u}, which is disjoint from D since u∈U. Thus (R) holds everywhere, and Raynaud's theorem gives (1).

## 5. Proof of the target-only Hom refinement

Set H=\(\mathcal Hom_{\mathcal O_P}(F,G)\). This is coherent because P is noetherian and F,G are coherent. At any point v∈P, a finite presentation of F_v gives an exact sequence

\[
0\longrightarrow H_v\longrightarrow G_v^{\oplus a}
\longrightarrow I\longrightarrow0,
\qquad I\subseteq G_v^{\oplus b}.
\]

If depth G_v≥1, any G_v-regular element is also regular on a nonzero submodule of G_v^{\oplus b}, so depth I≥1, with the zero-module convention covering I=0. The depth lemma consequently gives

\[
\operatorname{depth}H_v\ge
\min\{2,\operatorname{depth}G_v\}.
\tag{4}
\]

For depth G_v=0 the displayed lower bound is automatic; for depth G_v=1 the injection into G_v^{\oplus a} gives it directly; for depth G_v≥2 the exact sequence above gives depth H_v≥2. In particular H satisfies (A) whenever G does. The section comparison therefore applies to H.

It remains to identify its formal completion. On any affine open V=Spec R⊂P, write F|_V=\(\widetilde M\) and G|_V=\(\widetilde N\) for finite R-modules. The t-adic completion \(\widehat R\) is flat over the noetherian ring R (Stacks Project Authors, 2026, Lemma 10.97.2, tag 00MB). Taking the kernel associated with a finite presentation of M gives the canonical isomorphism

\[
\operatorname{Hom}_R(M,N)\otimes_R\widehat R
\simeq
\operatorname{Hom}_{\widehat R}
\bigl(M\otimes_R\widehat R,N\otimes_R\widehat R\bigr).
\]

These local isomorphisms are functorial and glue, yielding

\[
\widehat{\mathcal Hom_P(F,G)}
\simeq\mathcal Hom_{\widehat P}(\widehat F,\widehat G).
\]

Taking global sections of this identification and using (1) for H proves (2). In particular completion is fully faithful on the full subcategory of Coh(P) whose objects satisfy (A).

## 6. Exact scope of the conclusion

The comparison just proved verifies the section and Hom portion of the local lead under the stated complete-local hypotheses, including Hua's target-only refinement. It does **not** identify the essential image of completion, prove algebraization of an arbitrary formal coherent sheaf, validate unrestricted fullness of Coh(P)/C_Φ(P), or fill the manuscript's undefined conditions a), b), c′), T₁. The counterexample to unrestricted fullness in main note N39 is therefore unaffected.

Nothing here changes the frozen reading of scan46 or completes the manuscript's own interrupted dévissage at scan48. No update is made to the supplied historical RESULTS_STATE file; main note N79 records the checked literature inference alongside the original candidate/intake label. No claim of historical priority or mathematical novelty is made.

## References and verification limits

Raynaud, M. (1974). Théorèmes de Lefschetz en cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental. *Annales scientifiques de l'École Normale Supérieure, 4e série, 7*(1), 29–52. [https://doi.org/10.24033/asens.1260](https://doi.org/10.24033/asens.1260). [Primary PDF](https://www.numdam.org/article/ASENS_1974_4_7_1_29_0.pdf). Input: I.0, I.1.1, I.1.3, printed pp.31–32. The article describes its proofs as summaries of the essential arguments and refers to the longer work; this record checks the reduction to the cited theorem rather than reproducing that theorem's entire proof.

The Stacks Project Authors. (2026). *The Stacks Project*. Retrieved November 17, 2026. Specific locators: [Lemma 10.72.10, tag 0FCC](https://stacks.math.columbia.edu/tag/0FCC), for the depth-localization inequality; [Lemma 10.97.2, tag 00MB](https://stacks.math.columbia.edu/tag/00MB), for flatness of noetherian completion. These are auxiliary modern proof references.

Hua project. (n.d.). *Modernised reading of cote 58*, “Une forme locale,” their pp.45–51, and findings-register entry `58-local-hom-comparison-depth-off-y`. Supplied local files: `context_opened/hua_project/58.modern.tex`, its README, and `context_opened/notes/RESULTS_STATE.md`. AI-produced interpretation and diagnosis; not an independent diplomatic witness or a published proof.
