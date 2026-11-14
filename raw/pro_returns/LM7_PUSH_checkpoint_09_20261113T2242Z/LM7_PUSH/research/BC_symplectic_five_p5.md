# E50: the exact prime-five five-strand comparison

## Completed result and scope

The complete induced source of the eight literal Sp4(F5) evaluations has order9,000,000. All six B/F cosets are retained. Its lower-central residual on the rank-ten Fermat subgroup H is C=SL2(F5)×(C5)^3, with the displayed isomorphism obtained by extracting the actual third pentagon coordinate and transposing its stable two-plane matrix. This residual admits corrections preserving every nilpotent H boundary factor used in E41, E47 and E42.

The actual common quotient with the old Ferrari double-cover source G_L is

    J=A10 ×_{A2} Q20,
    A_m=B/(F′F^m),
    Q20=SL2(Z/20)/{±I},
    |A10|=600, |A2|=24, |Q20|=2880, |J|=72000.

The maps are printed in sections/E_symplectic_five_p5_agent.tex. A10→A2 reduces the six actual Schreier exponent-sum vectors modulo2. Q20→A2 is projective reduction modulo4, matched on every value and generator edge. The new source kernel is the actual subgroup Q=(C5)^3.

For every one of the432 multiplier-one E24 points and every full E41/E47 boundary fibre, the same profinite commutator word can retain the complete G_L comparison and satisfy all new five-strand tests. The selected Galois element is exactly the E43 element with cyclotomic character1 in the full profinite unit group; consequently all new order5, order10 and order8 powers have the required multiplier-one values. The correction is in the closed lower-central residual of H, kills D23 and G_L, and has any prescribed value in Q. It therefore preserves the entire indicated infinite boundary system at once.

The actual common source for an old finite stage G_old retaining P20 is

    (G_old ×_S G_L) ×_J G_sp.

Both the original and corrected maps are onto this specified fibre product. The proof does not presume invariance of a finite source kernel under a shadow map. On the new factor, onto H follows from agreement with the actual Galois map; alternatively its F image has abelianization(C10)^2 and hence no nontrivial quotient of the exponent-three group F/H. The new source itself does not retain B/H.

The exact joint B4 target is

    (T23 ×_{S_L} T_L) × T_sp^(4) × A96,

where |T_sp^(4)|=15000. The two retained B5 targets have actual joint image Sp4(F5)×A96. Their corrected maps are onto, because the new symplectic and retained Hurwitz/SL2 values all agree with the same actual Galois word.

## Exact finite certificates and replay order

All files have prefix `code/bc_symplectic_five_p5_`. Each script has `.out`, `.json` and `.npz` outputs. No original root or earlier checkpoint file is rewritten by these programs.

1. `residual.py` —5.569seconds. Reconstructs all97 N words and all ten H words, checks all subgroup containments, and proves [H,C]=C. The third pentagon projection identifies L=N′=C′ with all120 matrices of SL2(F5). Its exact kernel splits N=L×(C5)^5 and C=L×(C5)^3. It constructs the actual A10 map, and the source/A10 joint order remains9,000,000.
2. `modular.py` —47.027seconds. Computes conjugation on the actual L. The selected SL2 lifts of s,r square and cube to−I. Change of basis[[0,1],[1,0]] identifies their projective map with the ordinary modular quotient. The full joint source with the old Ferrari A5 source has exactly the old order, proving its actual quotient map to PSL2(F5).
3. `signed.py` —179.426seconds. Reconstructs the Ferrari Source read-only with load_data(), avoiding the legacy runpy initializer. Replays the complete25965-relator lifted presentation with width2055: the2052 old ambient coordinates plus all three binary Q20 coordinates. The kernel rank remains44, and its projection to the old44-space is an isomorphism. The saved3×44 matrix is the exact signed map, including the scalar9I.
4. `common.py` —0.640seconds. Builds both maps to A2, checks all2880 Q20 matrices and5760 small-action edges, enumerates all72000 matching pairs, and certifies that their joint source with G_sp still has order9,000,000. It also records the normal-closure orders of every SL2(F5) element:1,2, then118 occurrences of120.
5. `target.py` —208.223seconds. Pairs all three literal Ferrari braid generators with the first three new transvections. The complete73496-relator lifted presentation has binary kernel rank55. The actual joint target order is |T_L|·15000, proving the direct product with its original maps.
6. `target_perfect.py` —0.350seconds. Enumerates all15000 four-by-four matrix values. The two adjacent commutators generate1250 elements; adding the conjugate U1[U1,U2]U1^{-1} gives all15000. This is the literal perfectness certificate for the new B4 factor.

The first four source scripts take about four minutes; all six take about seven and a half minutes. Scripts1–4 are the parent’s initial replay dependency sequence. Script5 is independent of their outputs; script6 reads script5’s final target metadata. The complete immutable program/output hashes are in `research/E50_source_authoritative_manifest.json`.

Primary upstream inputs are the root’s `e_symplectic_five_p5_{model,source,subgroups}_root` arrays and metadata, the read-only `de_ferrari_a6_source_data.py` reconstruction, the literal H basis in `de_fermat_schreier.py`, and the frozen Ferrari A5/SL2 source and target certificates. Each new output records its exact input hashes. Elapsed-time-only JSON changes during an isolated replay change provenance hashes; compare those against the replay’s own inputs rather than the original elapsed-time values.

## Preserved failed one-bit attempt

The first signed comparison incorrectly treated q4 as a quotient of the old A5 base. Its literal x,y values have order15, while the nontrivial q4 values have order2; this already rules out that claimed map. The complete Schreier replay then found the Q20 discrepancy[[9,10],[10,9]] and stopped at an assertion before producing any comparison certificate.

The correct base is q5×q2. Its kernel in Q20 is elementary abelian of rank3. Choose the representative equal to I modulo5, and write its modulo4 value as

    I+2[[a,b],[c,a]].

All three coordinates must be retained. The corrected run includes them in the actual lifted group law and conjugation action. The failed script, its complete output and an explanation are preserved in `research/bc_symplectic_five_p5_attempts/signed_one_bit_failed.py`, `.out`, and `signed_one_bit_failure.md`. No theorem or final result uses the failed one-bit assertion.

## Proof checks and limits

The parent and profinite_images independently read the source/common-quotient and residual-generation proof and accepted it before the isolated source replay. Their audits explicitly checked the H-surjectivity restriction, the compact nested-fibre passage, and the use of actual maps rather than finite kernel invariance.

This result retains the specified multiplier-one family and the entire stated boundary towers. It does not identify the full Grothendieck–Teichmüller image or establish that these finite and relative factors form a cofinal family. Those remain the exact E2/E3 questions.
