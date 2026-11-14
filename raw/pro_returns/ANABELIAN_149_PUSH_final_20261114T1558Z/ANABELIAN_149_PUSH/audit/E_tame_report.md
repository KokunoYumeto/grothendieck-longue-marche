# E1 repaired tame-category extension

Status: proofs E.10--E.12 independently reviewed and accepted by root after checking BR6.23--6.26, SGA1 IX.4.12 and Noohi10.4--10.5. The result rows in E_tame_results.json are Proved. Under root's express direction, E_tame_extension.tex is now input in E.tex and the former E.U1 statement has been removed as superseded. Root handles the central coverage and result assembly.

| Literal or repaired request | Outcome represented in the extension |
|---|---|
| Full moduli étale paths in characteristic p with field-extension invariance | Remains refuted by E.1, under the faithful marking convention of (Z.2). |
| Specialization of the entire characteristic-zero category to prime-to-p-closure covering arrows | Remains refuted by E.2, by the proper genus-two degree-p cover. |
| Category with boundary-tame paths retaining interior p-monodromy | Proved in E.10--E.11. |
| Specialization from the characteristic-zero restricted-arrow category | Proved in E.12; full characteristic-zero markings remain present. |

The construction uses the prime-to-p root stacks of the proper stable moduli compactification. It keeps all original stack inertia and finite interior p-monodromy; it does not replace the moduli fundamental group by its maximal prime-to-p quotient. Proper-DM finite-étale field comparison and formal specialization are proved from EHKV Theorem 2.7 and SGA1 descent on a finite scheme cover and its Čech nerve. This explicitly supplies the stack extension rather than citing a scheme-only theorem for it.

The crucial additional point is that actual curve automorphisms inject into the boundary-tame group. Order all punctures, and in positive genus impose full Jacobi level at an odd ell different from p. Jacobian faithfulness and torsion-freeness of the principal ell-adic congruence subgroup detect the automorphisms. The prime-to-p semistable monodromy formula of B.5/C.2 makes each boundary generator an ell-transvection and kills wild inertia. Therefore the level cover is boundary tame, although its full finite monodromy group can have p-torsion.

For a cover with prime-to-p Galois-closure group G, Bertin--Romagny's stable Hurwitz compactification has local discriminant parameters tau_i=t_i^{e_i}, e_i dividing |G|. Normalize after adjoining roots of the target boundary with index divisible by every e_i. The local normalization branches have identical deformation rings to the base. Relative automorphisms preserving one branch extend over that deformation and form its generic smooth-cover deck group; the extra ghost automorphisms permute branches. This gives a finite étale gerbe over a finite étale cover of the target root stack. Its source map is logarithmic on boundary parameters.

An arbitrary finite gerbe need not have injective fibre inertia. The proof does not assume otherwise: take the gerbe exact sequence through the cofinal root system, then use the faithful source-moduli level to inject the deck group. Compactness gives exactness and surjectivity in the limit. It follows that a target path lifts uniquely up to the deck group, which is exactly the ambiguity in the closed-coset Hom formula. Chain Hurwitz stacks and the common prime-to-p Galois closure prove associativity.

Specialization uses one good marked R-model per type, R=W(k). A permitted generic cover extends after finite base extension, by the fixed-curve comparison E.3 and uniqueness of stable models. The corresponding root-stack specialization sends full generic paths to boundary-tame special paths and commutes with the normalized Hurwitz source, target and composition maps. It preserves type and cover components, and gives surjections on automorphism groups and on each closed-coset Hom component. It need not be faithful. The source restriction excludes the degree-p obstruction of E.2.

Files: `sections/E_tame_extension.tex`, `audit/E_tame_results.json`, full proof note `audit/F_E1_tame_construction.md`. Source details are in `sources/F_sources.md`; new bibliography keys are F_EHKV2001, F_Noohi2004, F_TalpoVistoli2018. Existing BC_DM, BC_Knudsen, BC_HMTopics and E_BR2007/E_SGA1 are reused.
