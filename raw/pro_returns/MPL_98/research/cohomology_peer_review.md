# Independent review of the Čech comparison and real-conic calculation

**Reviewer:** ChatGPT, GPT-6 Astra Pro; inherited effort setting not exposed; run **MPL98**, agent `norm_research`. **Date:** November 18, 2026. **Target:** `research/cohomology_research.md`, principally COH06–COH07 and their completed Appendices C–D. The author confirmed completion of the mathematical memo before the final review of those appendices. The reviewer read the research memorandum only, together with the primary references listed below; no manuscript image or transcription was inspected. This is a mathematical check, not a novelty or archival-priority assessment.

## Verdict

**The real-conic calculation and the displayed conditional low-degree exact sequence are correct.** The necessary qualifications are now explicit in the reviewed COH06–COH07: the counterexample concerns one fixed non-field cover; the injection criterion is the vanishing of a specific differential; the field setting satisfies the required Picard vanishing; and the conic does not obstruct the usual colimit comparison after arbitrary refinements. No correction to the conic calculation or to the final term `E_4^{4,0}` is needed.

## PR-COH01: the exact criterion for the initial injection

Use a convergent first-quadrant cohomological spectral sequence with

\[
d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1}.
\]

The only differential that can enter `(2,0)` is `d_2:E_2^{0,1}→E_2^{2,0}`; there is no outgoing differential there. Consequently

\[
E_\infty^{2,0}=E_2^{2,0}/\operatorname{im}(d_2),
\qquad
F^2H^2\simeq E_\infty^{2,0}.
\]

The edge map `E_2^{2,0}→H^2` has kernel exactly `im(d_2)`. Thus:

- **Necessary and sufficient:** that particular `d_2` is zero.
- **Sufficient:** `E_2^{0,1}=0`.
- For a single-cover Čech spectral sequence, **sufficient:** `H^1(T,A)=0`.
- For `A=G_m`, **sufficient:** `Pic(T)=0`.

Vanishing of the entire `q=1` row is stronger than needed for this initial injection. Stacks, Tag 0CJZ, proof of Lemma 21.11.1, explicitly uses the corresponding covering-family criterion `H^1(U_i,A)=0`. Tags 03AZ and 079Z provide the spectral sequences; Tag 03P8 identifies first `G_m` cohomology with Picard groups.

## PR-COH02: the extended sequence and its endpoint

Under `E_2^{p,1}=0` for all `p`, the filtration calculation gives

\[
\begin{aligned}
E_\infty^{2,0}&=E_2^{2,0},\\
E_\infty^{0,2}&=\ker(d_3:E_2^{0,2}\to E_2^{3,0}),\\
E_\infty^{3,0}&=\operatorname{coker}(d_3:E_2^{0,2}\to E_2^{3,0}),\\
E_\infty^{1,2}&=\ker(d_3:E_2^{1,2}\to E_2^{4,0}),\\
E_4^{4,0}&=\operatorname{coker}(d_3:E_2^{1,2}\to E_2^{4,0}).
\end{aligned}
\]

Because no differential enters column zero, `E_∞^{0,3}` is canonically a subgroup of `E_2^{0,3}`. Therefore

\[
H^{3\prime}=F^1H^3
=\ker\bigl(H^3\longrightarrow E_2^{0,3}\bigr).
\]

Also `F^2H^3/F^3H^3=E_∞^{2,1}=0`. Combining the resulting two filtration extensions yields exactly the sequence in COH06:

\[
0\to E_2^{2,0}\to H^2\to E_2^{0,2}
\xrightarrow{d_3}E_2^{3,0}\to H^{3\prime}
\to E_2^{1,2}\xrightarrow{d_3}E_2^{4,0}
\to E_4^{4,0}\to0.
\]

The final `E_4^{4,0}` is correct. A subsequent `d_4:E_4^{0,3}→E_4^{4,0}` can still change it, and even the stable term `E_∞^{4,0}` is only `F^4H^4`, not all of `H^4`. Thus silently replacing this endpoint by `H^4` would require additional assumptions. The identity-cover example correctly shows that full row vanishing is sufficient rather than necessary. Appendix C's sharper sufficiency claim also checks: only the `q=1` entries for `p=0,1,2,3` need vanish for this displayed portion.

## PR-COH03: independently checked real-conic obstruction

Let

\[
S:\ x^2+y^2+z^2=0\subset\mathbf P^2_{\mathbf R},
\qquad T=S_{\mathbf C}.
\]

The map `T→S` is the base change of the finite étale `C_2`-torsor `Spec(C)→Spec(R)`. The parametrization

\[
\phi([u:v])=[u^2-v^2:i(u^2+v^2):2uv]
\]

is the Veronese parametrization followed by an invertible linear change of coordinates, hence identifies `T` with `P^1_C`. Substitution directly gives `x^2+y^2+z^2=0`. Writing

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad j([u:v])=[-\bar v:\bar u],
\]

one obtains `φ(J bar(w))=−bar(φ(w))`; the minus sign disappears projectively. Thus *j* is exactly the real descent involution, not an unrelated involution of the split projective line.

The tautological bundle `O(−1)` has a semilinear lift `τ(w)=J bar(w)` covering *j*. Since `J bar(J)=J^2=−I`, its square is multiplication by `−1`. The dual bundle `O(1)` has the same scalar obstruction. Every other lift differs by an automorphism of that line bundle, hence by `c∈C^×`; its square changes by the factor `c bar(c)>0`. Therefore no lift satisfies the descent cocycle condition.

This yields the normalized two-cocycle with value `−1` on `(σ,σ)`. Indeed, for the conjugation action of `C_2` on `C^×`, the normalized two-cocycle condition says that its sole possibly nontrivial value is real, while a normalized coboundary changes that value by `c bar(c)`. Hence

\[
H^2(C_2,C^\times)=\mathbf R^\times/N(\mathbf C^\times)
\simeq\mathbf Z/2,
\qquad d_2([\mathcal O(1)])=[-1]\ne0.
\]

The Čech nerve has `T^{p+1}_S≅\coprod_{C_2^p}T`, and `Γ(T,O_T^×)=C^×`; its degree-zero row is exactly this group-cochain complex. By PR-COH01, the fixed-cover edge map

\[
\check H^2(T/S,G_m)\longrightarrow H^2(S,G_m)
\]

has nonzero kernel. In fact it is zero on the entire source `Z/2`, since the displayed transgression is surjective. Differential sign conventions cannot change the conclusion: this nonzero class has order two. No computation of the whole Brauer group of *S* is needed.

Badr, Bars, and Lorenzo García (2018), Theorem 4.1, p. 1199, corroborates the Picard-to-Brauer obstruction, but explicitly recalls it as Lichtenbaum's theorem by reference to another work. It should be cited as a stated comparison, not as their original proof of this explicit example.

## PR-COH04: fixed cover versus all refinements

The conic example does **not** disprove injectivity of the degree-two Čech comparison after taking the usual colimit over all covers and refinements in the full étale or fppf site.

Independently, suppose a fixed-cover class `c∈E_2^{2,0}` maps to zero in derived cohomology. By PR-COH01, `c=d_2(a)` for `a∈E_2^{0,1}`. This *a* is represented by compatible first-cohomology classes on the cover's members. Refine each member to trivialize its corresponding torsor. Under the induced refinement map, *a* becomes zero; naturality gives `c↦d_2(0)=0`. Thus the kernel vanishes in that colimit.

For the conic one can explicitly refine `P^1_C` by its two affine charts, where `O(1)` is trivial. This argument uses arbitrary admissible refinements, including open refinements of the finite étale cover. A limit restricted only to finite Galois covers is a different construction and should not be substituted without explanation.

## PR-COH05: the field setting is compatible with the injection

If `T=Spec(L)` is a field, then `Pic(T)=0`, already proving the initial injection whenever that map is a cover in the selected site. For a finite extension `L/k`, every finite tensor power `L⊗_k⋯⊗_kL` is a finite-dimensional *k*-algebra and therefore Artinian. It is a finite product of local rings; an invertible module is free of rank one on each factor and hence free globally. Its Picard group is zero, including in the inseparable/nonreduced case. Consequently the full `q=1` nerve row vanishes and COH06 applies.

For an algebraic extension of arbitrary degree, each finite tensor power is the filtered colimit of the tensor powers of finite subextensions. An invertible module, its inverse, and their multiplication isomorphism descend to some finite stage by finite presentation. Picard vanishing follows from the finite-stage result. The topology caveat is essential: an infinite algebraic field extension is an fpqc cover, but is not automatically a cover of finite presentation in the étale or fppf site. This algebraic verification supports the possible field context described by the other agents; it does not decide what the manuscript asserts.

## References inspected for this review

- Badr, E., Bars, F., & Lorenzo García, E. (2018). The Picard group of Brauer–Severi varieties. *Open Mathematics, 16*, 1196–1203. https://doi.org/10.1515/math-2018-0101 . Author-hosted paper: https://mat.uab.cat/~francesc/Brauer.pdf . Theorem 4.1, p. 1199.
- The Stacks Project Authors. (n.d.). *Lemma 21.10.6* (Tag 03AZ). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/03AZ . Čech-to-cohomology spectral sequence.
- The Stacks Project Authors. (n.d.). *Lemma 21.13.2* (Tag 079Z). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/079Z . Epimorphisms of sheaves and the nerve spectral sequence.
- The Stacks Project Authors. (n.d.). *Second cohomology and gerbes* (Tag 0CJZ). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/0CJZ . Proof of Lemma 21.11.1 explicitly states the `H^1(U_i,A)=0` criterion for fixed-cover degree-two injectivity.
- The Stacks Project Authors. (n.d.). *Theorem 59.24.1* (Tag 03P8). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/03P8 . First multiplicative-group cohomology and Picard groups.
- The Stacks Project Authors. (n.d.). *Lemma 10.78.7* (Tag 02M9). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/02M9 . Constant-rank finite locally free modules over semilocal rings are free.
- The Stacks Project Authors. (n.d.). *Lemma 32.10.3* (Tag 0B8W). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/0B8W . Descent of invertible modules through inverse limits of quasi-compact quasi-separated schemes with affine transition maps.

**Review boundary:** This memo certifies the displayed mathematical arguments in its stated scope; it does not certify other COH sections, unseen formal code, a novelty claim, or a reading of the manuscript. It makes no edits to the author agent's memo.
