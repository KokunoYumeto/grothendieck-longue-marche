#!/usr/bin/env python3
"""Generate the separate A.25--A.26 source ledgers without shared assembly."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT/"sections"
passage = "C4 §52.2, folio744, scan193; PartA(e) unrestricted profinite finite-action realization"
rows = [
    {
        "id": "A.25",
        "statement": "The complete integral Hall-coordinate class-five lifting family above the fixed A.23 pair and all20 A.24 parameters is affine Z5^90. Its1428x428 system has rank338 over Q and F5. Projection to class4 has affine image dimension2 and fibres dimension88; the zero-parameter class4 particular point does not extend. Every solution gives an outer order-two peripheral automorphism with the prescribed A.22 metabelian images and exact conjugator norms.",
        "status": "Proved",
        "where_proved": "sections/A_allclass.tex, Statement A.25",
        "depends_on": ["A.22", "A.23", "A.24", "A_CasalsHall2018", "code/a_metabelian_lift_class5.py", "code/a_class5_verify.py"],
        "manuscript_passages": [passage],
        "depends_on_doubtful_reading": False,
        "notes": "Uses actual Hall group coordinates at class=p, not the bare integral BCH lattice. All294 Hall leading terms and logarithms are checked. The saturated second-derived lattice has rank252, certified by308 actual commutators. All20 previous parameters are retained and every one of the90 integral kernel vectors is saved and independently verified. Complete central derivative formulas are proved; four declared basis indices for each conjugator are additional group-evaluation cross-checks, not exhaustive column sampling. Counts5^(90n),5^(2n),5^(88n) refer to residue solutions of parameter equations, not naive Hall-coordinate group quotients. No full free profinite lift is asserted.",
    },
    {
        "id": "A.26",
        "statement": "The specified A.22 metabelian involution lifts to an actual outer order-two pure peripheral automorphism of Q=Fhat2/ker(K→K^(5)), where K is the index-three subgroup sending both tripod generators to1 in C3. Derived conjugators have the exact specified metabelian residues and norm one. The entire A.22 action on M=Fhat2/Fhat2'' also lifts to Fhat2/(Fhat2''∩ker(K→K^(5)))≅M×_(Q/Q'')Q. This is an all-class relative lift, without prescribing the particular A.23 pair.",
        "status": "Proved",
        "where_proved": "sections/A_allclass.tex, Statement A.26",
        "depends_on": ["A.19", "A.22", "A_ChenDeligne2017", "A_HajirMaire2016", "A_PutmanSymplectic"],
        "manuscript_passages": [passage],
        "depends_on_doubtful_reading": False,
        "notes": "The pure genus1/three-boundary homology image is proved by handle twists and four explicit boundary shears. Schur–Zassenhaus is applied inside the closed subgroup fixing one boundary element and each other oriented boundary conjugacy class, with a pro5 congruence kernel; complements are conjugated to preserve the actual C3 deck action. Primitive-cube centralizers plus the prescribed deck coset, rather than unrestricted root uniqueness, give peripheral conjugators. Exact norm normalization puts them in Q'. A specialized profinite Magnus representation proves the relative Alexander module is free of rankone; its two domain factors force the signs +1 and−1 and identify both A.22 residues. The all-class lift is not claimed to extend the fixed A.23 pair or to lift to the full free profinite group.",
    },
]
(OUT/"A_allclass_results.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False)+"\n")
coverage = [
    {
        "task": "A(e).specified_class5_lift",
        "requested": "Continue the A.22/A.23 lifting problem to class5 using integral group coordinates and all20 preceding class4 parameters",
        "status": "proved_complete_affine_family",
        "results": ["A.25"],
        "remaining": ["All-class extension of the specifically fixed A.23 conjugator pair is not claimed by A.26"],
        "programs": ["code/a_metabelian_lift_class5.py", "code/a_class5_verify.py"],
        "outputs": ["code/a_metabelian_lift_class5.json", "code/a_metabelian_lift_class5_system.json", "code/a_metabelian_lift_class5.out", "code/a_class5_verify.json", "code/a_class5_verify.out"],
        "exhaustiveness": "Complete integral affine system, all90 kernel vectors, all20 original parameters, and complete projection; eight explicitly declared exact-evaluation cross-checks supplement proved central derivative formulas.",
    },
    {
        "task": "A(e).allclass_relative_lift",
        "requested": "Find an all-class equivariant realization preserving every oriented boundary, or a finite obstruction to the specified A.22 metabelian action",
        "status": "proved_relative_pro5_and_full_metabelian_fibre_product_lift",
        "results": ["A.26"],
        "remaining": ["A.12: compatibility with the remaining finite quotients of Fhat2, beyond the all-class relative-pro5/full-metabelian fibre product", "Whether the specified A.22 action itself lifts to an order-two pure peripheral automorphism of Fhat2"],
        "source_scope": "Hajir–Maire §2 and Theorem2.5 give the pro5-kernel and coprime complement inputs; the boundary radical and specialized Alexander statements are proved here. Putman Theorem0.1 is cited only for comparison with the closed-surface result.",
        "specific_earlier_pair_prescribed": False,
        "full_free_profinite_lift_asserted": False,
    },
]
(OUT/"A_allclass_coverage.json").write_text(json.dumps(coverage, indent=2, ensure_ascii=False)+"\n")
with (OUT/"A_allclass_readings.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["cote", "scan", "folio", "equation", "reading", "resolution", "used_by", "doubtful"])
    w.writerow(["140-4", "193", "744", "(8)", "Profinite extension of the L definitions and finite-action realization context", "Previously image-checked passage. A.25 gives the complete integral class-five test; A.26 proves an all-class relative-pro5 and full-metabelian fibre-product lift. No new manuscript decipherment or unrestricted full-profinite realization claim.", "A.25; A.26", "no"])

bib = r'''@misc{A_CasalsHall2018,
  author = {Casals-Ruiz, Montserrat and Kazachkov, Ilya and Remeslennikov, Vladimir},
  title = {Pro-{Hall} $R$-groups and groups discriminated by the free pro-$p$ group},
  year = {2018},
  eprint = {1803.00478v1},
  archivePrefix = {arXiv},
  primaryClass = {math.GR},
  url = {https://arxiv.org/pdf/1803.00478},
  note = {Opened primary author preprint, 13 November 2026. Section 4, displayed Hall normal form and Remark 4.1, printed page 7, identify finite-class free Hall Zp groups with free nilpotent pro-p groups. A.25 separately proves the integral coordinate comparison and does not infer naive coordinatewise finite group quotients at class p}
}
@article{A_HajirMaire2016,
  author = {Hajir, Farshid and Maire, Christian},
  title = {Prime decomposition and the {Iwasawa} mu-invariant},
  journal = {Mathematical Proceedings of the Cambridge Philosophical Society},
  year = {2019},
  volume = {166},
  number = {3},
  pages = {599--617},
  doi = {10.1017/S0305004118000191},
  eprint = {1601.04195v1},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/pdf/1601.04195},
  note = {Exact numbering follows the opened 16 January 2016 author preprint: Section 2, before Definition 2.1, states that the mod-p Frattini congruence kernel is pro-p; Theorem 2.5 gives profinite Schur--Zassenhaus and conjugacy by that kernel. Lemma 2.12 and Proposition 2.13 corroborate the coprime automorphism-lifting argument. Accessed 13 November 2026; no unseen theorem number from Ribes--Zalesskii is attributed}
}
@misc{A_PutmanSymplectic,
  author = {Putman, Andrew},
  title = {The symplectic representation of the mapping class group is surjective},
  year = {n.d.},
  url = {https://academicweb.nd.edu/~andyp/notes/SymplecticSurjective.pdf},
  note = {Author's four-page note opened 13 November 2026. Theorem 0.1 is the closed-surface surjectivity theorem, with proof. A.26 explicitly proves its own boundary-radical extension by twists and does not attribute that stronger statement to this theorem}
}
'''
(OUT/"A_allclass_refs.bib").write_text(bib)
report = '''# A.25–A.26: class five and the all-class relative lift

The specified metabelian involution now survives the entire relative pro-5 completion of the index-three subgroup of the free profinite tripod group. A separate exact calculation also extends the previously fixed class-two conjugators through class five, with the complete earlier parameter family retained. These are different conclusions: the all-class theorem prescribes the A.22 metabelian action, but does not prescribe which A.23 nonmetabelian pair it extends.

## Complete integral class-five calculation

The open class-five kernel is free nilpotent pro-5 on four generators. Its lower-central ranks are 4, 6, 20, 60, and 204, for a total of 294 coordinates. At class five one cannot simply treat the free integral Lie lattice as a BCH group, because the rational formulas can have denominators divisible by 5. The calculation instead uses actual recursively bracketed Hall group words and their ordered 5-adic power coordinates inside a rational truncated Magnus algebra.

Every Hall generator's leading Lyndon bracket is checked, and all 294 individual Hall logarithms are integral at 5. Actual group collection lifts the class-four particular pair. Each of the twenty class-four parameters is retained as an actual weight-four group correction, with its necessary degree-five commutator correction in logarithmic coordinates. There are also 204 central coordinates for each of the two conjugators. This describes every class-five pair above the earlier family.

The second-derived lattice is checked integrally, not merely over the rational numbers. Its rank is 252. The code constructs 308 actual group commutators in the second-derived subgroup; their logarithms span that lattice modulo 5. The matching rational and modular ranks, together with the explicit integral basis, prove saturation. Since the derived subgroup of the open kernel has nilpotency class at most two, its integral logarithm is controlled using only the invertible denominator 2.

The full seven-residual system has 1,428 rows and 428 columns. Twenty columns represent every preceding parameter and 408 are the new central coordinates. The residuals are affine by weight: a quadratic occurrence of two old corrections would first appear in degree seven. Every old-parameter column is evaluated by the full group formulas. All central derivatives are derived explicitly in the proof and calculated on all 204 basis elements for each conjugator. Four declared basis indices for each side are also checked by full group evaluation; these eight checks are identified as cross-checks, not as an exhaustive second evaluation of all columns.

The rational and mod-5 ranks are 338, with an integral particular solution and ninety integral nullspace vectors. The independent verifier reads the saved sparse matrix and hash, checks all ninety exact kernel equations, checks the identity minor on the free coordinates, and recomputes the rank modulo 5. The solution space is therefore exactly an affine Z5-space of dimension 90.

Projection to the entire class-four parameter space has affine image dimension 2 and fibres dimension 88. The image basis has a unit identity minor on coordinates 0 and 3. All twenty offset coordinates and both image vectors are displayed in the section, while the certificate also saves the eighteen equivalent affine constraints. The class-four point with all twenty parameters zero fails those constraints. This is another explicit instance where retaining the previous family changes the outcome.

Modulo 5^n the integral parameter equations have 5^(90n) solutions, 5^(2n) extending class-four parameter points, and 5^(88n) points per fibre. These count residues of parameter equations. They do not assert that naive Hall-coordinate reduction modulo 5^n is a group quotient at class five. Every integral solution itself gives an exact order-two peripheral automorphism, and the same finite order-75 witness proves outerness.

## All-class relative theorem

Write F=Fhat2, K=ker(F→C3), N=K^(5), R=ker(K→N), and Q=F/R. The group N is free pro-5 of rank four, and Q=N⋊C3. Its three peripheral cubes are primitive elements corresponding to the three boundary components of a genus-one cover. The proof works in the closed automorphism subgroup that fixes the first cube exactly and preserves each of the other two oriented conjugacy classes separately.

The required mod-5 homology involution is in this subgroup's image. This is proved by two handle twists and four boundary shears, each shear given by the explicit difference of twists about a handle curve and its band sum with one boundary component. Those shears generate every homomorphism from proper homology to the boundary radical. This proves the needed boundary statement directly; Putman's closed-surface symplectic theorem is cited only for comparison.

The congruence kernel is pro-5. Schur–Zassenhaus gives a complement over the order-six subgroup generated by the involution and the deck transformation. Conjugacy of complements aligns its order-three subgroup with the actual given deck action. Its order-two element therefore extends to Q fixing the split deck generator. The exact source is Hajir and Maire's 2016 author preprint, Section 2 and Theorem 2.5, subsequently published in 2019.

Primitivity identifies the centralizers of the three boundary cubes. Equality of cubes is used together with the specified nontrivial C3 coset; the proof does not claim unrestricted uniqueness of cube roots in the semidirect product. This produces individual peripheral conjugators. Each is then adjusted by a half-power of the appropriate boundary cube, simultaneously giving exact norm one and zero abelianization without changing the involution.

The relative Alexander module is proved to be free of rank one over Z5[[Z5²×C3]]. A cyclic surjection is made injective by a specialized profinite Magnus representation: the commutator vector has zero annihilator. The coefficient ring has two domain factors, the trivial C3 character and the irreducible nontrivial character over Z5[ζ3]. The involution multiplier has square one. Augmentation forces sign +1 on the trivial factor; the prescribed proper-homology action forces sign −1 on the nontrivial factor. The conjugator and third-peripheral equations then determine precisely the A.22 residues. This avoids any assumption that completion automatically preserves a discrete Alexander calculation.

Finally, the normal-subgroup pullback lemma identifies F/(F''∩R) with the fibre product (F/F'')×_(Q/Q'')Q. The all-class relative action and the full A.22 metabelian action agree on the common quotient, so they act componentwise on this fibre product. Their conjugators agree there as well and satisfy the exact norms. Thus the entire specified metabelian action has an all-class nonmetabelian lift, not only a lift after discarding its other metabelian factors.

## Exact residual and scope

The relative group and the fibre product are prosolvable, whereas the full free profinite group also has nonabelian simple finite quotients. No automorphism of the full free profinite group has been constructed. The remaining concrete A.12 question is compatibility of the specified A.22 involution with the other finite quotients, beyond this relative-pro5/full-metabelian fibre product. Increasing nilpotency class inside this particular open pro-5 kernel alone cannot supply an obstruction to the A.22 action, because A.26 provides a compatible all-class lift. Extending the specifically selected A.23 pair through all classes is a separate question; A.25 establishes that pair's survival through class five.

## Reproduction and files

Run `python code/a_metabelian_lift_class5.py` for the exact group and linear construction, then `python code/a_class5_verify.py` for the independent saved-certificate checks. The first recorded construction took approximately 665 seconds. The sparse system and complete particular solution, all ninety kernel vectors, actual Hall coordinates, all prior-parameter corrections, exact hash, and transcript are retained. The verifier saves the entire projection and all affine image equations.

The manuscript supplement is `sections/A_allclass.tex`; its separate result, coverage, source-reading, bibliography, and report files have the same stem. The data are `code/a_metabelian_lift_class5.json`, `code/a_metabelian_lift_class5_system.json`, `code/a_metabelian_lift_class5.out`, `code/a_class5_verify.json`, and `code/a_class5_verify.out`. No randomized search, sampled solution count, or numerical rank inference is used.
'''
(OUT/"A_allclass_report.md").write_text(report)
print("Wrote separate A.25–A.26 results, coverage, readings, bibliography, and report.")
