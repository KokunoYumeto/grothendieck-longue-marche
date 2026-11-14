# Independent E.118 audit

**PASS.** The complete corrected proof and both mathematical sources were read. A fresh reconstruction used only the two source files; no binary arithmetic input was supplied.

Reviewed proof SHA256: `142d07c7f19d79b5044ae37208f226031595c97b1060c023bf9da3b734f1a0f2`.

## Proof checks

- Read the complete corrected theorem/proof, complete GP source and complete Python source.
- Exact degree32 compositum, point coordinates and inverse field maps; all32 actual embeddings and residual matrices.
- Monic integer unit equations with unit constant term, literal inverse, and tau_b(u)=w^5 u^3.
- The conjugate unit character and the negative second coordinate in H agree with the actual determinant character.
- Left-coset corestriction gives a cocycle; 3*32=1 mod5 makes its restriction H; changing representatives adds g v-v.
- The norm-to-degree8 map proves injectivity of the nonfifth class, and the distinct tau_a characters prove independence.
- The resulting actual Kummer field is normal, unramified away2,5 and has degree800 overQ; kernel equality is read through rho and H.
- E112 finite H1 reduction is onto and each integral H1 is free rank1; all integral generator choices are (1+5z)h.
- The specified degree-one prime, two fifth residue logarithms and alternating Weil-pairing sign give h1(F3121)=(3,1).
- The independently enumerated3200 points and actual25-element torsion span imply F-1=5D with D invertible, hence exact local order5.
- The toric fifth-power condition, primitive inertia and E115 exact mixed criterion give precisely5Z5^3, both directions, with all central fibres retained.
- Corrected tensor extension and its literal inverse are distinguished from the image of the integral inclusion; the actual finite-support rational correcting cochain gives the full rational slice.
- All six copied source/output files are byte-identical after a fresh no-input GP/Python reconstruction; no elapsed or other field excluded.
- A separately written finite group program verifies25600 corestriction terms,800 representative-change formulas and640000 cocycle identities.

## Exact correction

The initial statement described the inclusion of the integral slice as surjective after scalar extension. The corrected text proves the tensor map `(5R^3) tensor_R Q5 -> Q5^3`, its inverse on the basis, and separately constructs the actual rational section through E115’s correcting cochain. This resolves the typing issue; no other proof correction was requested.

## Fresh arithmetic replay

The full no-input GP/Python replay completed with exit0. Both source files, GP stdout/stderr, Python stdout and the full JSON are byte-identical to the author files, with zero excluded fields. The additional independent program checks all640000 cocycle identities in the actual residual semidirect group of order800.

## Scope

This is a complete proof/source audit plus a fresh arithmetic replay. E112’s exact finite reduction and E115’s actual coefficient/local boundary maps were reread. It does not claim a new independent reopening of every primary source cited by those earlier statements. All audit programs and their actual outputs are retained under `code/`.
