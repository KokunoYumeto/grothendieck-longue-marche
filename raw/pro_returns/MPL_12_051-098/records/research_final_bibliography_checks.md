# Final arithmetic bibliography checks

Narrow primary-source audit for the parent, 2026-11-17. Only the five requested citation questions were checked; no main notes, frozen transcription, doubts, inventory, or checkpoint files were changed. Printed page numbers and PDF page numbers are distinguished below; retrieval IDs are supplied so the parent can reopen sources for final citations.

## 1. Milne, ADT II.2.1: the curve residue sequence

**Primary:** J. S. Milne, *Arithmetic Duality Theorems*, second edition (2006), Chapter II, Proposition 2.1, printed pp.163–164; Remark 2.2(a), p.165. These are PDF pages171–173 in the current 347-page file.

**URL:** https://www.jmilne.org/math/Books/ADTnot.pdf

**Inspected:** the section's global-field and curve conventions, the proposition, its displayed sequence, and Remark 2.2(a). Retrieval: `turn178710157view2` (lines7317–7419); earlier `turn775252917view1`.

In the function-field case, X is the connected smooth complete curve over the full constant field of K, and U is a nonempty open subset; S consists of the omitted places. The proposition gives

\[
0\longrightarrow H^2(U,\mathbf G_m)
\longrightarrow\bigoplus_{v\in S}\operatorname{Br}(K_v)
\xrightarrow{\sum\operatorname{inv}_v}\mathbf Q/\mathbf Z
\longrightarrow H^3(U,\mathbf G_m)\longrightarrow0.
\]

For a nonempty finite S the sum map is surjective, and each local invariant identifies its summand with Q/Z; S counts closed points, which need not be rational.

**Wording for N044:** “For a smooth proper geometrically connected curve over a finite field with r≥1 closed points removed, ADT II.2.1 and Remark II.2.2(a) give Br(U)≅(Q/Z)^{r−1}; in particular one puncture still gives Br(U)=0.”

## 2. Kato–Trihan: one finite primary component implies full BSD

**Primary:** K. Kato and F. Trihan, *On the conjectures of Birch and Swinnerton-Dyer in characteristic p>0*, *Inventiones mathematicae* 153 (2003),537–592, introduction theorem, printed p.537.

**Publisher / DOI:** https://doi.org/10.1007/s00222-003-0299-2

**Author-uploaded full text inspected:** https://www.researchgate.net/publication/227273997_On_the_conjectures_of_Birch_and_Swinnerton-Dyer_in_characteristic_p0

**Inspected:** introduction theorem and the following paragraph identifying the full conjectures by §§1.3.1,1.4.1,1.8.1. Retrieval: `turn318824728view1` (lines61–85); fuller text `turn618209735view1`; publisher metadata `turn348528139view0`.

K is a function field in one variable over a finite field and A is an abelian variety over K. The hypothesis is finiteness of Sha(A/K)(ℓ) for **some prime ℓ**, without excluding ℓ=p; the conclusion is the full BSD conjecture, not merely its rank equality. This theorem does not establish the finiteness hypothesis for every A.

**Wording for N040:** “For an abelian variety over a global function field of characteristic p>0, Kato–Trihan's theorem proves the full BSD conjecture if one ℓ-primary component of Sha is finite, with ℓ=p allowed.”

## 3. Milne's local duality: distinguish the 1970 theorem from the 1972 completion

### 1970 paper

**Primary:** J. S. Milne, *Weil–Châtelet groups over local fields*, *Annales scientifiques de l'École Normale Supérieure*, série4,3 (1970),273–284. Theorem(a), printed p.274 / PDF page3; notation on p.273 / PDF page2.

**URL:** https://www.numdam.org/item/ASENS_1970_4_3_3_273_0.pdf

**Inspected:** opening scope statement, topology conventions, Theorem(a), and its interpretation as H¹(K,A)→A∨(K)*. Retrieval: `turn178710157view0`; `turn653972606view0` (lines15–71); screenshot requested for printed p.274 as `turn300172045view1`.

The theorem gives nondegeneracy of the degree0/degree1 pairing, with a possible exception on the p-primary part in characteristic p when A is not isogenous to a product of elliptic curves and abelian varieties with potential good reduction. Cohomology is taken in the flat topology; for the smooth abelian variety itself it agrees with étale/Galois cohomology. Thus **the 1970 paper alone should not be cited as the unrestricted theorem for arbitrary reduction**.

### 1972 addendum

**Primary:** J. S. Milne, *Weil–Châtelet groups over local fields: addendum*, *Annales scientifiques de l'École Normale Supérieure*, série4,5 (1972),261–264. Unnumbered theorem, printed p.261 / PDF page2.

**URL:** https://www.numdam.org/article/ASENS_1972_4_5_2_261_0.pdf

**DOI:** https://doi.org/10.24033/asens.1227

**Inspected:** complete theorem and the opening reduction of its proof. Retrieval: `turn178710157view1` (lines16–29); screenshot requested as `turn300172045view2`.

This supplies the unrestricted theorem for an abelian variety over a local field with finite residue field, including the characteristic-p primary part. In degree1 it gives the Pontryagin duality between H¹(K,A) and A∨(K).

**Wording for N042 / bibliography:** “The Tate–Milne local pairing identifies H¹(K_x,A) with the Pontryagin dual of A∨(K_x); Milne's 1970 Theorem(a) covers the good-reduction situation of scan082, and the 1972 addendum supplies the general local-field theorem.”

**Why 1970 suffices for this leaf:** A is an abelian scheme on the smooth curve C, so its generic fibre has good reduction at x. This is an inference from the manuscript's hypothesis, not a weakening of Milne's theorem.

## 4. Oda Corollary5.11: perfect-field and group-scheme scope

**Primary:** T. Oda, *The first de Rham cohomology group and Dieudonné modules*, *Annales scientifiques de l'École Normale Supérieure*, série4,2 (1969),63–135. Corollary5.11, printed p.131 / PDF page70.

**URL:** https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf

**DOI:** https://doi.org/10.24033/asens.1175

**Inspected:** the corollary, both exact sequences, and its perfect-field hypothesis; the supplied PDF page was also rendered and visually inspected during the arithmetic research. Retrieval: `turn178710157view3` (lines2450–2465); `turn741419338view1`.

For an abelian variety A over a **perfect field of characteristic p**, Oda gives a canonical isomorphism M(A[p])≅H¹_dR(A), using his contravariant Dieudonné-module conventions. It identifies the submodule VM(A[p]) with the Hodge subspace H⁰(A,Ω¹), retaining F and V rather than only geometric p-torsion points.

**Wording for N063:** “Over a perfect field of characteristic p, Oda's Corollary5.11 identifies the Dieudonné module of A[p] with H¹_dR(A), compatibly with the Hodge sequence; it is not a theorem of Sha finiteness or a replacement for flat p-primary cohomology.”

The perfect-field qualification cannot be omitted when comparing with K_x≅F_{q^d}((t)), which is imperfect. The corollary is not a statement for an arbitrary base scheme.

## 5. Weil II lower weights and smooth finite-field high-degree vanishing

**Primary:** P. Deligne, *La conjecture de Weil II*, *Publications Mathématiques de l'IHÉS* 52 (1980),137–252. Corollary3.3.5 and its duality proof, printed p.206 / PDF page70.

**Author/institutional URL:** https://publications.ias.edu/sites/default/files/Number40.pdf

**DOI / archive:** https://doi.org/10.1007/BF02684780 ; https://www.numdam.org/item/PMIHES_1980__52__137_0/

**Inspected:** Corollary3.3.5, its lower-bound inequality, and the following duality argument. Retrieval: `turn318824728view2` (lines2433–2438); `turn490511336view0`; screenshot requested for printed p.206 as `turn300172045view0`.

For a smooth finite-type base and a lisse sheaf of weights ≥n, the corollary puts ordinary geometric H^j in weights ≥n+j. Applied to Qℓ(1), it gives weights ≥j−2, with ℓ≠p.

**Wording suitable beside N045:** “For smooth separated finite-type X/Fq and ℓ≠p, Weil II, Corollary3.3.5 gives weights ≥i−3 and ≥i−2 on H^{i−1}(X̄,Qℓ(1)) and H^i(X̄,Qℓ(1)); when i≥4 neither has Frobenius eigenvalue1, so the Hochschild–Serre sequence implies H^i(X,Qℓ(1))=0.”

The last implication is the explicit editorial deduction from the theorem and Hochschild–Serre, and uses no disputed upper weight bound for variable coefficients. It does not apply to the singular D or D×P¹ counterexamples.

## Audit outcome

All five requested comparisons have direct primary support with the scopes above. The material citation adjustment is to distinguish Milne1970's reduction hypothesis from the unrestricted Milne1972 addendum; the scan082 application itself satisfies the former. No new mathematical investigation, source-image transcription, upload, or checkpoint was undertaken.
