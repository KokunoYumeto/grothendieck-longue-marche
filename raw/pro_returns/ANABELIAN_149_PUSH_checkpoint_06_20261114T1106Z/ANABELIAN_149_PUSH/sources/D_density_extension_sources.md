# D.25 primary-source record

The bibliography keys below already occur in the assembled bibliography; this extension adds no duplicate BibTeX entries.

- **Opened: Stix, J. (2015).** *On the birational section conjecture with local conditions*, arXiv:1203.3236v3, <https://arxiv.org/pdf/1203.3236>. Exact passages: Definition 8 (asymptotic integrality), Theorem 10 and its proof (pp. 9–11), Lemmas 17–19 (explicit Legendre monodromy and the three distinct modulo-2 cusp lines), equation (5.1) and the surrounding local calculation in the proof of Theorem 20 (pp. 15–16), and Corollary 5 with its finite-support proof. The complete corresponding supplied TeX source was opened and read. Bibliography key: `D_Stix2015`.
- **Opened: Mochizuki (2003), real section theorem.** Corollary 3.13, as already recorded and independently checked for D.22. Bibliography key: `D_Mochizuki2003Real`. Only the real connected-component assertion is used; no equality of a real point with a boundary point is claimed.
- **Internal proved inputs:** D.6/D.19 for finite-local point-or-cusp sections; D.22 for the corrected finite-place formulation of the Stoll finite-support argument. These dependencies are explicit rather than attributed to Stix's original hypotheses.

## Exact scope of the new argument

Stix's general Theorem 20 assumes birational liftability. D.25 does not invoke that theorem without its hypothesis. It uses only its geometric pro-2 local specialization calculation for the identity map of the three-punctured line, where no additional puncture or lift is needed. The three cusps are already distinguished modulo 2. An independent compatible Kummer argument over Q then excludes its exceptional triangular case for a noncuspidal section.

The finite étale cover extension is proved directly from decomposition-group intersection, finite normalization over Z[1/S], and the boundary identity d_base=e*d_cover. No arbitrary branched cover or twisted modular curve is included.

## Reproducible computations

`code/D_legendre_density_certificate.py` was executed successfully. Its output `audit/D_legendre_density_certificate.json` verifies the exact matrix identity, the three primitive fixed vectors and their distinct reductions, and representative eighth-power residues. The all-odd-prime eighth-power assertion is proved in the manuscript by the four congruence classes modulo 8 and Hensel's lemma; the finite computation is not substituted for that proof.

## D.26 source and proof update

The number-field strengthening uses the same opened Stix statements with their original number-field scope. The compatible Kummer lemma is proved in full from Chebotarev, elementary cyclotomic group structure, inflation–restriction, and the unit/divisor sequence; no Grunwald–Wang assertion is imported. Root independently reviewed the complete candidate `audit/D_number_field_density_candidate.md` before integration.
