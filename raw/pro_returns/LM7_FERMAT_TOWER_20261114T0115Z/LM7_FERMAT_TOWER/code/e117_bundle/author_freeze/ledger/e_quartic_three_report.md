# E.117: the actual three-primary quartic class-two image

## Result and scope

E.117 proves the complete image and every fibre of the actual intrinsic quartic class-two section map with integral three-adic coefficients, and its rational three-adic counterpart. It uses the fixed E.103 abelian coordinates and the actual E.105 four-coset origin. All changes of coordinates carry the based arithmetic action and the affine filling map with them.

For the finite base (S=\{2,3,\infty\}\), every abelian input lifts. The displayed coordinates identify the section space with

\[
\mathbb Z_3^{13}\times\bigl(\mathbb Z_3^{78}\oplus(\mathbb Z/3)^{10}\bigr).
\]

For the unrestricted arithmetic source, the image is precisely the intersection of the 55 peripheral cup conditions of E.108 with the integral restricted-support condition on

\[
c_p=v_p\wedge j_r(F_{E,p}-1)^{-1}h(F_p).
\]

The support denominator is the actual image of the support differential, without taking a closure. The proof gives both directions, a compatible global primitive, the inverse coordinate maps, and the full change under geometric conjugacy. Every nonempty central fibre has the stated coordinates

\[
\mathbb Z_3^{66}\oplus(\mathbb Z/3)^{10}
\oplus\mathcal R_{\mathrm{all}}(\mathbb Z_3)^6
\oplus\mathcal R_{p\equiv1\ (4)}(\mathbb Z_3)^3
\oplus\mathcal R_{p\equiv3\ (4),\ p\ne3}(\mathbb Z_3)^3.
\]

Here each restricted product consists of coefficient families tending to zero. Rationalization uses the literal compact-cochain scalar-extension map and a common denominator bound. The theorem also proves unbounded local mixed orders by actual compatible finite translation and Kummer extensions, and constructs separately liftable toric and compact inputs whose sums fail the class-two test.

The statement concerns this exact intrinsic class-two quotient. Higher intrinsic quotients, other odd coefficient primes, and the original E.23 questions beyond the displayed maps remain under investigation. The proof makes no assertion that the three-adic Ceresa class is nonzero based on a five-adic shadow.

## Arithmetic and integral maps

The two full three-division fields are constructed with explicit radical maps for (y^2=x^3+x) and (y^2=x^3+4x). Each has degree 16, certified class number one, and a full decomposition group at both 2 and 3. The certificate records all sixteen actual automorphisms in both fields, all nine torsion points, the inverse field maps, and the normalized flex-tangent Weil-pairing calculation. The pairing is the displayed primitive cube root squared in both fields.

Restriction and corestriction of degree 16, the exact Kummer sequence, the two fixed Brauer places, and the literal residual twists prove finite-base (H^0=H^2=0) for all five rank-two coefficient lattices. Their (H^1) is evaluated as one free three-adic coordinate with explicit compatible finite-cocycle choices. The unrestricted pure-CM factor adds exactly the displayed inert-prime residue coordinates.

The polarization coordinate change is Φ/2 and Ψ/2, and it is compared explicitly with the original Φ and Ψ/4 coordinates. The selected first elliptic factor supplies an integral section of the compact wedge quotient. The proof does not divide its total contraction by three. A retained 20 by 20 unit minor for the Johnson map and a 6 by 6 unit minor for the inner map prove saturation. The pure-CM selector has eight nonzero entries, all equal to (\pm1/4). The actual integral Harris–Pulte/Johnson comparison, its factor two, its inner correction, and the full affine filling morphism are preserved in the resulting cochain identity.

## Executed verification

The author executed the complete program with the actual PARI source:

```bash
python research_e117/code/a_quartic_three.py --gp research_e52/vendor/pari-2.19.0/gp
```

A second execution used copied owned sources and all three copied, hash-checked inputs in an isolated replay tree. The complete Python stdout, complete JSON, complete GP textual output, and copied sources are byte-identical. No timing or other fields were excluded. The PARI serialization bytes differ; the retained verifier compares the complete deserialized objects, including every component of both full BNF objects, and proves exact equality. The comparison is recorded in `e_quartic_three_replay.json`.

The finite certificate includes two unconditional default-flag class-group certifications; the two full automorphism and local-decomposition calculations; 512 residual cocycle equations; the exact Johnson, inner, polarization, and pure-CM maps with inverses; 586 inert-projector checks; 4,997 tensor-valuation checks; 4,997 bounded-coboundary inverse checks; 48 scalar-extension tests; and the symbolic ordered-cup tame-word identity. The infinite cohomology, topology, source descent, support sufficiency, and Chebotarev statements are proved in the text, rather than inferred from those finite samples.

All earlier failed API, serialization, and layout attempts remain in the history directories with their actual outputs. The unsupported number-field pairing call was replaced by the proved literal tangent-function formula; no equation was weakened to obtain a passing run.

## Source and peer review

The source-evidence ledger records the exact opened primary passages: SGA1 XIII 2.9–2.12 and full specialization proof; Milne's finite arithmetic cohomology and duality; Jannsen's continuous-cohomology comparison; the integral Hain–Matsumoto and BLLS action comparisons; Milne's Chebotarev proof; and the official meaning of default `bnfcertify`.

B independently checked E117.11–29, the normalized pairing sign, the exact residual twists, finite-base cohomology, coordinate counts, and the integral selector. That focused audit is retained at `bc_e117_focus/audit.md` and `audit.json`; it makes no full unrestricted-support or fresh-program claim. The only later source amendment explicitly defines (H=C=T_3J_C), as requested by root. The preceding source is preserved and the exact diff is recorded. Root's complete proof and independent replay review is pending at this author freeze.

## Presentation and freeze

The standalone source compiled through three LuaLaTeX passes and BibTeX with exit zero and no overfull or undefined-reference warnings. All twelve rendered pages were actually inspected at 110 dpi. The theorem, equations, field table, selectors, support maps, and bibliography are visible without clipping or overlap. Exact page and PDF hashes are retained in the visual ledger.

The author manifest identifies the authoritative theorem, both executable arithmetic sources, all outputs and inputs, source evidence, actual replay comparisons, preserved histories, and rendered verification. Root owns integration into the main manuscript and the subsequent checkpoint.
