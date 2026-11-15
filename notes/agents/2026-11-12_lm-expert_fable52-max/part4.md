
---

## Closing lists

### (i) The findings and hunches this literature step was for

| Entry | Verdict | What changes |
|---|---|---|
| **F7** (sections: his corrected conjecture of 2:sc79 is the section conjecture with cuspidal sections; the "famille transcendante" is the standard packet; injectivity by Mordell–Weil; what 019 claims and does not cover) | **Confirmed, with four corrections.** | (1) Citations: letter to Faltings pp. 54, 56–58; Stix arXiv:0809.0017 Prop. 8, Thm 14, Thm 17; Esnault–Hai Conj. 2.2, Thm 5.1, Prop. 5.3, Thm 5.5, Thm 6.5, Cor. 6.9; Deligne 1989 §15.13–15.26. (2) The reason for injectivity is "no divisible elements in G(K)", not "G(K) of finite type" (false with a torus). (3) His claim that packets of distinct cusps are already distinct in the extension by π_ab is false in genus 0 (P^1 ∖ {0,1,∞}: the tangential classes at 0 and 1 coincide abelianized); true for g ≥ 1. (4) "Not covered by 019: affine curves" is too weak a description: the affine local statement with packets follows from Thm 1.1 by the neighbourhood argument (1.C); and over number fields 019 gives the equivalence "section conjecture for C ⇔ C(A_K)_•^{f-cov} = C(K)". |
| **H5** (his admissible sections are the non-cuspidal ones; axioms ①–⑥ of §32 equivalent to the section conjecture for all open subcurves; ⑤ (c) = affine case from the proper case) | **Confirmed in substance; one correction.** | Admissible = non-cuspidal: Stix Cor. 12 and Cor. 22 (after Nakamura), over fields that distinguish tori from abelian varieties. ⑤ from the proper case: the neighbourhood argument (Koenigsmann Lemma 1.7; Stix arXiv:1203.3236, 2.1.2 and Cor. 5; Bresciani arXiv:2108.13397). Not in the literature: the comparison with his axioms as he states them. Correction: his rigidity condition π^Γ = 1 holds for cuspidal sections too; the condition that excludes cusps is π^{Ker χ} = 1 (his own PS of 1983; 2:sc433 "peut-être même π^{Γ⁺} = 1"), and that one is conjectural for point sections. |
| **H7** (§33 is the real section conjecture; profinite version known; real cuspidal packets; fixed groups) | **Confirmed; one correction.** | §33's theorem with centralizers = Mochizuki 2003 Thm 3.6, Cor. 3.7; profinite: Mochizuki Cor. 3.13 (all hyperbolic real curves), Stix 2010 Thm 26 (proper), Bresciani–Vistoli (quasi-projective curves, semi-abelian torsors). Correction: over R the cuspidal sections are not extra classes; the packet at a real cusp has two elements, the classes of the adjacent components of U(R). Still to prove: the profinite fixed groups (1 for a line, Ẑ for an oval). |

### (ii) For the LM6 Parts (`PUSH_REDO\LM6_PARTS_redo_20261112.md`): concrete changes, each with its reason

Opening paragraph of the Parts.
1. Say what Theorem 1.1 of the 2026 paper rests on, so that "check the step you rely on" has a target: Mochizuki–
   Tsujimura's resolution of nonsingularities (RIMS-1974, Thm A, Prop. 2.4 (iv)), the lifting theorem of
   Amini–Baker–Brugallé–Rabinoff (Thm 7.7), Pop–Stix Thm 26, Koenigsmann Prop. 2.4 (2). Reason: these are the only
   external inputs of weight (1.A); the paper's own steps check out.
2. Add to the tools, as statements to be derived in a few lines and then used: (a) for finite k/Q_p and every
   hyperbolic U, every section is the section of a point of U(k) or cuspidal, and the packets are disjoint torsors
   under the profinite completion of k^× (1.C); (b) for proper C of genus ≥ 2 over a number field, the section
   conjecture for C is equivalent to C(A_K)_•^{f-cov} = C(K) (1.C, item 3). Reason: both follow from the paper plus
   the standard neighbourhood argument, and several asks below are otherwise spent on them.
3. Add the known limits: non-geometric sections exist for the geometrically pro-p quotient (Hoshi 2010;
   Hoshi–Tsujimura 2021) and for the geometrically metabelian and nilpotent-by-abelian quotients over p-adic fields
   (Saïdi, arXiv:1510.06864, arXiv:2109.14882); over elliptic curves over p-adic fields the section map is not
   surjective. Reason: any "pro-ℓ form" or "modulo a metabelian quotient" fallback must not assume geometricity.

Part B.
4. B (a): cite as tools Stix (Prop. 8, Thm 14, Thm 17), Esnault–Hai (Thm 6.5, Cor. 6.9), Deligne §15; and change
   "Prove his assertion of scan 79 ... already in the extension by π_ab" to "decide it": true for g ≥ 1, false for
   g = 0 (the classes of the tangential sections at 0 and at 1 of P^1 ∖ {0,1,∞} coincide in the extension by π_ab),
   and inside one packet the abelianized classes coincide when ν = 1. New target in its place: compute, for every
   (g, ν), the fibres of {packets and points} → {classes in the extension by π_ab}. Reason: item 2 of Part 2.
5. B (a), added target: characterize group-theoretically the K^×-subtorsor of tangential sections inside the packet.
   Reason: Stix lists exactly this as missing ("recognize tangential sections within cuspidal sections"); it is the
   one point of §9 that the literature read does not settle.
6. B (b): correct the wording. He excludes g = 0 with ν ≤ 1 (P^1 and the affine line), not ν = 2; G_m is included.
   And the proof cannot use "G(K) de type fini" (false when the torus is non-trivial): ask for the proof from
   "no non-trivial divisible element in G(K)" (Esnault–Hai Prop. 5.3; Stix Thm 45), with the proof of that property
   for semi-abelian G over K finitely generated over Q, and the list of fields where injectivity fails (R; a
   p-adically closed field that is not sub-p-adic: Koenigsmann Prop. 2.3 (1)).
7. B (c): the sentence on the "transcendental" sections has a definite answer to be proved, not decided: every member
   of a packet has image in the normalizer of the loop subgroup (Stix Cor. 12), so none is admissible, and his
   formulation of 2:sc79 coincides with the letter of 1983 (both use the whole packet, "Mächtigkeit des Kontinuums").
   Replace "say exactly how the two differ" by the three-way comparison that is open: (i) prove π^{Γ'} = 1 for every
   point section and every cuspidal section, Γ' open (so his condition (a) of 2:sc431–433 does not exclude cusps);
   (ii) prove that Ker χ fixes the loop subgroup of a cuspidal section; (iii) prove or refute the 1983 PS: for a point
   section, the fixed group of Ker χ in π is trivial. For (iii) a start to check: by Ribet's theorem (torsion of an
   abelian variety over K(μ_∞) is finite) the fixed group Z maps to zero in the abelianization of every open
   subgroup containing Z·s(Γ), for proper X, hence Z equals the closure of its commutator subgroup; what remains is
   to exclude a non-trivial perfect closed subgroup. Reason: items 1 and 6 of Part 2.
8. B (c), on ⑤: name the neighbourhood argument as the tool and ask for the equivalence with ⑤ a), b), c) written in
   his terms, then the list of which of ①–⑥ are now theorems (for Γ = G_k, k/Q_p finite, granted the 2026 theorem;
   over number fields for the curves with C(A_K)_•^{f-cov} = C(K)). Reason: item 6 of Part 2.
9. B (d): delete "Θ is no longer injective". For finite k/Q_p, Θ: k^× → H^1(k, Ẑ(1)) is injective with cokernel
   Ẑ/Z; it fails to be injective over R. The dichotomy "point or cuspidal" is tool 2 (a), so the asks that remain
   are: the tangential subtorsor and its closure in the packet (which packet members are limits of point sections
   s_x, x → y); complete curves of genus 0 and 1 over k (compute the section sets; for an elliptic curve the
   cokernel of E(k) → H^1(k, T E) is the Tate module of H^1(k, E)); which of ①–⑥ hold for Γ = G_k; and the same
   over finitely generated extensions of Q_p, where nothing is claimed. Reason: 1.C.
10. B (e): add as a tool Mochizuki–Tsujimura Thm F (ii) (for a dominant morphism of hyperbolic curves, a section
    upstairs arises from a rational point iff its image does), next to the Hom-form. Reason: it is the functoriality
    statement his relative version needs, and it is proved over p-adic fields.
11. B (f): add Steklov's Theorems B and C (hyperbolic DM-curves, in particular the moduli stack of elliptic curves:
    the section conjecture follows from the one for curves over finite extensions; injectivity over sub-p-adic
    fields). For (0,4) say that the local statement is now a consequence of tool 2 (a), so that the ask is the
    global one. Reason: item 7 of Part 2.

Part C.
12. C (a): the statement to prove is wrong as written. Over R: π_0(U(R)) → **all** classes of sections is bijective
    for every hyperbolic real curve, affine or proper (Mochizuki Cor. 3.13; Bresciani–Vistoli); a class is cuspidal
    at a real cusp y iff y lies in the closure of its component; the packet at y has two elements. Ask instead:
    derive these in his language (his §33 theorem is Mochizuki's Thm 3.6 / Cor. 3.7); prove what the classes recover
    of the position of the cusps (which cusps are real, on which oval, and their cyclic order up to reversal, from
    the pairs of cusps to which each class is cuspidal); prove the profinite fixed groups (1 for a line, Ẑ for an
    oval), which the literature read gives only in the discrete case. Reason: item 5 of Part 2.
13. C (c): "the six real cuspidal packets" should be "the three real packets (two classes each)"; the computation to
    demand is the three classes of involutions and the six identifications of tangential classes with them (the
    tangential class at 0 towards 1 and the one at 1 towards 0 are both the class of the interval (0,1), and so on).
    Reason: same.

Part D.
14. D (a): put the equivalence "section conjecture for C ⇔ C(A_K)_•^{f-cov} = C(K)" (given the 2026 theorem) into the
    diagram, with Stoll's Remark 8.9; and say that the set of classes of sections of the extension by π_ab is a torsor
    under H^1(K, T J), which contains the completion of J(K) with quotient the Tate module of H^1(K, J), so that the
    question "finite?" has the answer no in general and the ask is to compute it and its Selmer part.
15. D (b): the statement is Cor. 8.5 of the paper; the chain to check is Thm 1.1, Harari–Stix Thm 2.1, Stix
    arXiv:1203.3236 Cor. 5, Stoll Cor. 8.8 (all four statements verified against the sources here).
16. D (c): "every section is locally geometric, and what this gives globally" is Prop. 8.1 of the paper. Ask
    beyond it: finiteness of loc_v(Sec(C/K)) for K without CM subfield (Betts–Stix Thm A with Thm 1.1); rigidity
    (Porowski: a section is determined by its reductions on a set of places of strongly positive density); then
    prove or refute finiteness of Sec(C/K) itself, naming the missing statement (finite fibres of loc_v at one
    place). Reason: this is the present frontier of his "Mordell through splittings" (2:sc65).

Part E (Fermat; not redone by the predecessor) and LM7.
17. Steklov's theorem (all Selmer sections over Q of the affine Fermat curve of exponent ℓ ≥ 7 are cuspidal) with
    tool 2 (a) and the real case would give: every section of π_1(V_ℓ) → G_Q is cuspidal for ℓ ≥ 7. This is the
    section-conjecture form of Fermat's theorem that 2:sc65 points to. Ask Pro to check the chain (in particular that
    "Selmer" in Steklov's sense is what the 2026 theorem delivers at every place, 2 and ℓ included) and to treat ℓ = 5
    and ℓ = 3, where Steklov's method stops.

### (iii) Noticed in passing, outside this fork's task

- Mochizuki–Tsujimura, Thm G: with Σ = Primes, "the various p-adic versions of the Grothendieck–Teichmüller group
  that appear in the literature in fact coincide", and the metrized GT is commensurably terminal in GT. Bears on
  the LM3/LM3b reviews (GT), not on sections.
- Mochizuki 2003, Cor. 3.8: components of M_{g,r}(R) ↔ classes of involutions over complex conjugation in the
  extended mapping class group, with centralizers. This is the statement behind F11 (a) (the count of classes of
  anti-involutions is the number of components of the real moduli) and behind Cor. 1–2 of his §33; for LM4.
- 2:sc483 as written ("the L_i are the maximal subgroups of π whose normalizer in E has open image in Γ") needs
  "pro-cyclic and cyclotomically normalized" to be true (otherwise π itself qualifies); in that form it is
  Nakamura's theorem as stated by Stix (Thm 20, Cor. 21) for fields that distinguish tori from abelian varieties.
  Finite extensions of Q_p do not (a Tate curve has Z_ℓ(1) inside its Tate module), so the p-adic case of LM6 A (e)
  cannot be had by that route; this last remark is my reasoning, not a quotation.
- Yamaguchi, arXiv:2601.07112v4: centre-freeness and torsion-freeness of the maximal m-step solvable quotients
  (m ≥ 2) of geometric fundamental groups of hyperbolic curves; for F5.

### (iv) Not obtained

- Mochizuki, *The local pro-p anabelian geometry of curves* (Invent. Math. 138 (1999)), Thm 19.1: not fetched in this
  fork (statement taken from Koenigsmann's Remark 1.2 (2)).
- Hoshi, Publ. RIMS 46 (2010) 829–848: listed on the author's page with a link to the publisher only; statement taken
  from Hoshi–Tsujimura RIMS-1950.
- Pál 2011, Wickelgren 2014, Esnault–Wittenberg 2009 (real case): not fetched; their content as summarized by
  Bresciani–Vistoli.
- Tamagawa 1997 (Compositio 109), Prop. 2.8 (the original neighbourhood argument): not fetched; used through
  Koenigsmann and Stix.
- Betts–Stix (Annals 2025), Bresciani's toric paper (v5, Sept 2026) beyond its abstract, Pajwani 2025, the OpenAI
  "Selmer converse" paper: not read.
- Pop's note of 28 Sep 2025 on the t-birational section conjecture
  (`https://www2.math.upenn.edu/~pop/Research/files-Res/2025-09-28_t-BSC.pdf`): the server answered 403 to the
  download; not read.
- Stix's monograph (LNM 2054) is paywalled; not used.

### (v) Downloads

Twenty files, all under `Free or receipted\free\lm-expert-20261112\<short-name>\`, each with its text extraction
beside it; paths, sizes, SHA-256, titles and source URLs are in `LM_EXPERT\work\lit\downloads_B1.jsonl`. Hosts: arXiv
(11), kurims.kyoto-u.ac.jp author pages (4), IAS (1), MPIM preprint archive (1), authors' university pages (2:
Harari, Stoll), the Grothendieck Circle page of L. Schneps (1, the letter; editor's page, see item 1). They are not
yet entered in `CLAUDE_FREE_SHELF.json`.
