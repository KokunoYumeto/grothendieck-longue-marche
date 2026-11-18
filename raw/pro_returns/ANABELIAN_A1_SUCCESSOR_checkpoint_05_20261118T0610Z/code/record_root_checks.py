"""Record actual proof readings, separately from source and numerical checks.

This is bookkeeping, not a mathematical verifier. Entries are deliberately
specific about scope; a source opening or a rerun is never inferred from a
proof reading.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "notes/statement_registry.json"
reg = json.loads(REGISTRY.read_text())
events = []
who = "GPT-6 Astra (OpenAI, ChatGPT Pro mode), root; separate effort setting not exposed"

def checked(ids, outcome, typ="targeted proof check"):
    for ident in ids.split():
        if ident in reg:
            reg[ident]["review_state"] = "proof_checked"
            reg[ident]["check_record"] = "Also checked in this writing, 18 November 2026: " + who + ". " + outcome
        events.append([ident, "2026-11-18", who, typ, outcome])

checked("A.14 A.15", "Read the full finite-core argument for the same-prime topology and the integral Frobenius/cusp-count comparison. No mixed-prime full-fibre injection is used.")
checked("A.16", "Opened supplied Saidi--Tamagawa source, Proposition 1.8(vi), definitions, and finite support argument; cofinite hypothesis retained. Known result, not independently reproved.")
checked("A.17 A.18 A.22", "Checked the self-normalizer proof, both compactness steps in point recognition, and commensurability-to-finite-constant-extension equivalence. Opened ST2009 Lemma 1.7 and Proposition 1.8(iii).")
checked("A.19 A.20 A.21", "Rebuilt the central extension, residue cocycle, same-label evaluation and two separate endgames. Dependency correction uses A.42--A.44 and A.49; support-field proof uses B.68, not A.16 or Boxall.")
checked("A.23 A.24 A.25 A.26 A.27 A.28 A.29", "Read prime-set proofs and their limits, including the degree-two-pencil bound, singleton Frobenius kernel, and Frattini obstruction. Finite data are checked in separate computation events. A.28 remains Open.")
checked("A.30 A.31 A.32 A.33", "Read Kummer-kernel proof, cover criterion in both directions with uniqueness/descent, specialization and all hyperbolic types. Corrected the finite-generation wording for tori; nonreduced modulus excluded from the semiabelian kernel statement.")
checked("B.1 B.2 B.3 B.4 B.5", "Read relative class-number proof, simultaneous-character formula in all genera, corrected pair bound and first-field fixed-prime reduction. Universal existence B.5 remains Open; no A.1 is used in the odd-degree pair exclusion.")
checked("B.6 B.7 B.8 B.9 B.10 B.11 B.12", "Read inverse norm/Tate-module identification, Frobenius cokernel, full-section construction, every-normal-quotient compactness criterion and examples. B.12 remains Open; nonzero fixed vectors alone do not give all-level free vectors.")
checked("B.13 B.14 B.15 B.16 B.17 B.18", "Read abelian primitive-packet decomposition including nonconstant Frobenius and p-divisible orbit lengths; solvable induction with all normal quotient idempotents; nonabelian finite-module limitation. Numerical checks are separate events.")
checked("B.19 B.20 B.21 B.22 B.23 B.24", "Read isolating-cover arguments, both F4 examples, scalar-Frobenius Lang cover, conductor reduction and explicit primitive-zero obstruction. Degree-one-allowed B.24 remains Open. Certificate reruns are recorded separately.")
checked("B.25 B.26 B.27", "Read normalized Cartier formula, rigidification at the marked point, both exact certificate interpretations, and the involution/Frobenius all-extension lower bound proving least prime 191.")
checked("B.28 B.29", "Read unpointed twist count and the prescribed-point obstruction. This invalidates the proposed contraposition but is not a formal logical independence theorem for A.1 and universal B.1.")
checked("B.30 B.31 B.32 B.33 B.34", "Read quartic isogeny pullbacks, all differential bases and Cartier formulas, characteristic polynomials and exact minimality arguments. B.32 remains Open; B.34 first-field minimum is degree 3 with prime 13, distinct from least-prime cubic witness over degree 8.")
checked("B.35 B.36 B.37 B.38", "Read the complete torsion-placement and domination proofs: disjoint branch loci, normal generation, constant-field p-primary control, tame cancellation, and the finite-wreath-product proof of prime-to-p Galois-closure order. Opened Poonen Theorem1.7 and Lemma2.1; the stronger order condition is proved locally.")
checked("B.39 B.40 B.41 B.42", "Read complete proofs: cyclic13 Frobenius factor and geometric non-supersingularity; theta-divisor exclusion and characteristic-two reflection Prym; ramification gcd obstruction; Hermitian/Fermat supersingular pullback. Finite certificates are separate events; the g=2,3 restriction in B40 is essential.")
checked("B.106 B.107 B.109 B.110", "Full targeted second reading of arithmetic Kummer inputs, uniform norm constants, generic-projection graph argument and removal of all exceptional values; exact CHW Proposition3.6, Corollary2.32 and Theorem4.18 and Rousseau printed11-01/02 theorem read. Scope is p>=5 nilpotent union and every finite extension, not all B8 fields.")
checked("C.1 C.2 C.3 C.4", "Read scope of field extensions, semiabelian Kummer collision versus full sections, independence limits, and virtual-puncture limitations. C.3 wording is corrected to avoid asserting formal independence not proved by its example.")
checked("A.42 A.43 A.44 A.49 B.68", "Full proof written and checked in this writing; no claim of a blind or different-model-family check.")
checked("A.1", "Checked the complete direct characteristic-p chain A.45–A.48, A.13, A.14–A.15, A.49, B.68, A.42–A.43, A.20–A.21, including full arithmetic quotient and whole-geometric-subgroup conjugacy.")
checked("A.15 A.35", "Read the complete replacement proofs for arbitrary retained prime sets and arbitrary perfect fields, respectively, including the normal-core topology, primitive orientation class and tame-boundary restriction.")
checked("A.45 A.46 A.47 A.48", "Read all four direct characteristic-p proofs: localization/Leray and central induction, tame Stein factor, algebraic inertia survival, and root-gerbe arithmetic transport. No characteristic-zero comparison used.")
checked("B.111 B.112 B.113 B.114 B.115 B.116 B.117", "Full second reading of finite-cover detection, normalizer character descent, arithmetic weight exclusion, CM coefficient-field proof and explicit 2-isogeny, weighted elliptic Magnus filtration, strictly smaller residual subgroup, square-torus based conjugation, and fixed-point-free pro-odd argument. The individual candidate is not assumed stable under complex conjugation; B.118 remains Open.")
checked("B.83 B.84", "Full second reading of the complete F8 branch-orbit proof and degree-seven supersingular-factor list; independent verification scope remains separately recorded. Checked the uniform four-branch proof: integral orbit idempotents, denominator multiplicity, duality, signature endpoint, opposite pairs, all regular differential valuations and symbolic Cartier identities. Universal B5 remains Open.")
checked("B.62 B.63 B.64 B.65 B.66", "Read complete ordinary pro-category proofs, including compact choices of comparisons descending after one refinement, slice coherence, simultaneous whole-Kummer comparison, completion saturation, fixed-field reconstruction, unique functor isomorphisms and h-descent. Opened CHW Proposition5.22, Proposition6.22 and Claim6.23, TheoremA.8, CorollaryA.9, Proposition4.8 and Stacks Tags0EYL,01ZM,0CUF with exact hypotheses.")
checked("B.45 B.53 B.56 B.57 B.58 B.59 B.60 B.61", "Read complete proofs: ordinary pro-form consequence, solvable strict-local closure via exact tame/wild sequence, metabelian stable Kummer kernel and complementary-unit intersection, nilpotent Kummer theorem including p2/p3 exceptions, rational residues, affine similarity and polynomial point maps. B56 nontriviality is now proved directly by odd-prime affine groups and the p2 dihedral splitting field, without wild freeness. B57 reconstruction scope updated by B106–110.")
checked("B.43 B.44 B.46 B.47 B.48 B.49 B.50 B.51 B.54 B.55", "Full targeted reading of ordinary finite-transcendence pro-reconstruction, all formal-arc avoidance cases, the henselian centralizer example, stable marked logarithmic diagrams and uniqueness, full finite-cover-to-small-site gluing, and arbitrary rank-one logarithmic approximation. Configuration reader separately opened all exact primary inputs. Inverse-image orientation is made explicit; the fixed log point retains the entire arithmetic Galois group.")
checked("B.52 B.67", "Read full remaining-quantifier statements and every recorded attempted reduction. They remain Open. B52 now removes p>=5 nilpotent unions via B106–110; B67 must not infer a supersingular target from a nonordinary cover or a bounded cyclic-seven exclusion.")
checked("A.50 A.51 A.52", "Full root second reading of S2–S3 and S6 proof texts: genus and marked divisor computation, connected cyclic19 Lang quotient and all nine character norms; braid presentation, class2 exponent5 core, augmentation filtration and independent collection certificate; four independently implemented finite controls and the integral rank82 basis comparison. This is a proof reading, separate from the precisely scoped computational events.")
checked("A.53", "Full root second reading: uniform primary-torsion bound by matrix geometric series, including the etale p-adic module and mod4 at2; connected Lang quotient pullback; exact rational fibre displacement; uniform Weil estimate and proper-subfield degree obstruction. This proves abundance of abelian candidates only, not compatibility of full point-section collisions.")
checked("A.54 A.55", "Full root second reading: cofinal pointed covers and full induced pro-Sigma topology; faithful deck action on rational cohomology, including r dividing the deck order; all-cover detection of based action; exact omitted-prime outer kernel and actual bounded-order collisions; retained-prime faithfulness; exact ST2017 large-set definition and full complementary-torsion stabilization contradicted by Weil growth. Neither statement decides the universal two-prime case.")
checked("B.85 B.86", "Full root second reading: characteristic-two local different and Raynaud theta line bundle; Frobenius character-orbit criterion; exact ordinary cubic and two-rank-one quintic loci; connectedness and etaleness of explicit Kummer covers; normalized split fibres; reflection isogeny and explicit maps; exact smooth-model zeta and class-number identities. Numerical verifier scope is recorded separately. Universal B4 and B5 remain Open.")
checked("A.56", "Full root second reading: elementary multiplicative-order valuations including2; abelian-s character multiplicities from invariant cohomology and quotient genera; bounded field-linear omitted-prime action; finite-r Frattini automorphism kernel; full induced pro-r topology through all subsequent r-covers. Scope is r-group by abelian-s-group deck groups, not all two-prime covers.")
checked("B.87", "Full root second reading: regular nodal smoothing; exponent-M cover with complete bipartite graph and all M^4 character bundles; proper henselian torsor extension; normalization exact sequence and Frobenius invertibility; ordinary smoothing and finite-field specialization. Finite degree avoidance is not an all-prime counterexample.")
checked("B.88", "Full root second reading: all Q-lifts have nonzero3-primary Abel class by norm/pullback and free odd-deck hyperelliptic contradiction; connected3-primary Lang pullback; exact Frobenius fibre criterion; degree3^7 and genus2188; explicit geometric Galois lift; full pro3 section separation at P,Q. Deck group is not asserted constant over F16.")
checked("B.89", "Full root second reading: ordinary elliptic existence in every characteristic; stable compact-type genus-g smoothing; connected maximal exponent-M torsor and exact graph genus; exhaustion of all geometric characters; rationalization of full geometric p-torsion before choosing the pointing; prime-to-p norm idempotents and uniqueness of each pointed split twist over every extension. Divisibility by p^((ell-1)(g-1)) is proved. This excludes bounded witness primes depending only on p,g but leaves unrestricted B1 open.")
checked("B.124 B.125", "Complete proof written by root and reread: central transgression for all curve types; goodness and exact full completion by centralizer/H2 effacement; full topology on every fg abelian subgroup; local comparison along labelled strata; exact finite Smith divisibility test and recursive relation lattice. Arithmetic-notes reader completed a targeted full second reading; requested character-embedding and stratum-comparison joins incorporated.")
checked("B.125", "Executed n3_lattice_certificate.py: 23863 exact comparisons across23 cases, comparing brute-force relation spans with Smith tests and checking line-bundle, blow-up and recursive cyclic examples. Computation does not verify the topology theorem.", "computation or formal certificate")
checked("B.126", "Full root second reading: normalized norm-class invariance under G_F; arbitrary-point transport over common finite extensions; both Gaussian grids, including nonfixed translated origin; monic modulus interpolation and Laurent coefficient contradiction; finite open-cover and exceptional-fibre patching. This proves uniform actual-point equivariance, not descent of the topos morphism.")
checked("B.127", "Full root second reading: finite scalar restriction/corestriction; unit decomposition and vanishing inverse-limit correction; nonidentity g in I'' and a non-root-of-unity moved ratio; one finite Galois local field for all samples; trivial conjugation on J/H and coefficient module; injective local restriction, convergent dilation identity, multivariable coefficients and divisor residues. Actual evaluation detects all rational p-Kummer classes on the stated principal affine opens, giving exact cohomological equivariance. Actual lifting remains open.")
checked("B.128", "Full root second reading: finitely many actual base values included in one Galois number field; stability of Bp under the local decomposition group; natural Kummer transport with the full Qp(1) action; arbitrary-point common-field comparison into W; independent I' two-grid argument; finite affine-space patching; B127 cohomological consequence and henselization fixed field. Gives equivariance under one open local absolute Galois group, without inferring topos descent or actual Kummer lifting.")
checked("B.129", "Full root second reading: universal projective extension and proper-affine finiteness; finite flatness from regular local parameters; finite principal cover of the branch/grid complement; one normalized field before point choices; two incidence-dimension arguments for avoidance and reducedness at all fibre points; rational projection fixed by sigma; norm-root multiset contradiction. Gives one local Galois group for every smooth geometrically integral affine source, not descent of the morphism of topoi.")
checked("B.130", "Complete root proof written and read; finite-checks reader checked the complete argument independently. Primitive part for a cyclic prime-power cover is the top prime-degree relative factor; geometric p-rank zero survives all forms and pointings; rationalize chosen point and group over one finite extension; Frobenius-power restriction and norm idempotent obstruct every all-level free vector. Applies to complete B85/B86 genus-two families; excludes degree-one covers.")
checked("A.57", "Full root second reading: Raynaud's same absolute-Frobenius theta bundle; uniform torsion intersection by proper hyperplane cuts; full multiplication-p orbit avoidance for every fixed ell, including2; positive stable cohomology; arithmetic abelian-r core and norm/pullback; faithful retained-p Tate action and finite inner-deck contradiction. Extends A54 to retained characteristic primes without deciding arbitrary omitted-prime order unboundedness. Finite-checks reader separately completed a full reading.")
checked("A.58", "Full root second reading: coefficient algebra over F_r is the full F-matrix algebra; explicit two-generator recovery and full cyclic multiplicity module; commutator equality gives IA action; extension-field multiplier gives exact t-power order also in Out; surface quotient realization uses A4 only for its final geometric clause. Arbitrary automorphisms are not identified with compatible arithmetic Frobenius actions. Independent finite certificate separately recorded.")
checked("B.119 B.120 B.121 B.122 B.123", "Full root second reading of local wild/derived centralizers and all-prime torsion-freeness; global valuation-and-power descent; stable metabelian Kummer kernel; affine collineation and finite-root-of-unity rigidity; uniform Gaussian-grid norm descent; finite-class nilpotent cohomology induction and its three-input reconstruction application. The finite number field must contain the tested a or b before its local Kummer class is formed; this is now explicit. General metabelian morphism reconstruction remains Open. Opened Iwasawa1955 Theorem2(ii), KZ2011 Theorem5.1 CaseI, Kuhlmann Chapter9 Theorem9.44.")

checked("A.56", "Full root reading of expanded retained-characteristic scope: Artin-Schreier fixed-vector independence and p-rank bound; rank-f_C characteristic Tate module; coefficient-field linearity; pro-p Frattini finite generation and full induced topology. Finite-checks reader independently passed the entire revised proof.")
checked("A.59", "Full root second reading: Burnside1904 TheoremIII p392 actually read; alternating characteristic homology subgroups cofinal by finite solvable image; correct normal-core argument; pointed descent over fixed field including characteristic-etale factor; rational trace injection and pro-r congruence compare omitted-prime orders; polynomial-factor formula including inverse Frobenius convention. No classification conclusion inferred.")
checked("B.131 B.132 B.133", "Full root second reading: exact opened JTWY Corollary6.13 and CHW3.6/4.13/A9; affine-chart continuity and finite algebraic subfields; scalar-log error from inflation and N-surjectivity; primitive integral Kummer class construction; primitive-output dilation with identical scalar error; analytic inverse construction; four-centre mixed derivative and q>=3 block separation; finite interpolation to algebraic coefficients; divisor residues, arithmetic-class normalization, two-grid global equality, pole exclusion and E-descent. Only principal affine-space opens are proved here.")
checked("B.135", "Complete root proof written and read; finite-checks full second reading PASS. Minimal-relation differential independence, trivial class forced by monicity, 2d-centre root-count argument, analytic constant field and sharpness all checked. Exact logarithmic derivatives are required.")
checked("B.134", "Full root second reading: the chosen CM differential 2+i is a unit at5; the proper etale model is finite over the nondiscrete strictly henselian valuation ring; Gaussian coprimality gives cyclic5-power kernels; compatible model covers give a surjective geometric character; properness and strict henselianity split every evaluated torsor over every finite extension, with compatible lifts. Restriction to an affine open remains nonzero. Finite-checks reader separately passed the whole proof. This refutes general point-evaluation detection, not reconstruction.")
checked("B.136", "Full root reading of every paragraph: normalized norm Kummer signs, constant-gcd analytic ratio interpolation, scalar Weil-restriction blocks, extended algebraic derivations and divisor cocycle, constant-root exclusion, analytic-open lcm specialization and q-1>d, B135 exact derivatives, integral residues and global constant-factor removal, generic graph degree, transverse-curve continuity and CHW reconstruction. Finite-checks and configuration readers also completed full readings with PASS; no general evaluation-faithfulness premise is used.")
checked("B.137 B.138", "Complete root proof written and reread. Finite-checks and arithmetic-notes readers completed full independent readings of the signed-grid lemma and whole norm transfer. The uniform all-prime extension uses an odd ell not dividing p(p-1), a central tame pro-ell element with cyclotomic value1, and the explicit nonzero class of1-p^(1/ell). Arithmetic-notes reader reread the saved final all-prime clauses and passed. All finite algebraic extensions, henselization/completion distinctions, normalized per-projection norm equivariance, cyclic local quotients, scalar errors and field-independent B136 argument are explicit; this route uses no Baker-Brumer theorem.")

checked("A.60", "Full root reading: cyclotomic period identity and exact resultant; explicit modular remainders, irreducibility and order56; semisimple order versus possible3-primary Jordan blocks; canonical N2 domination; full pro3 topology and Frattini automorphism kernel; sharp A56 bound B=1 with exact constants. No all-cover unboundedness is inferred.")
checked("B.139 B.140", "Full root reading: finite local closure of a finitely generated subfield of Qpbar, henselian relative closure and finite-extension/completion equivalence; stable finite-derived Kummer kernel via inflation-restriction unipotence and finite vector orbit; strict derived quotients using balanced unitriangular commutators; relative tame two-grid criterion; every norm-proof input over Omega; compatible finite-slice infinite algebraic base change and descent; positive transcendence-degree examples and negative infinite derived union. Root independently opened and read Temkin1.9.5(ii),1.9.7,1.9.8 and all of Stacks09EJ. Later B142–144 are not premises of this reading.")
checked("B.141", "Full root reading of initial general criterion: Lang connectivity, genus-two Riemann-Roch character polynomial including canonical coefficient, separable hyperelliptic pencil in characteristic2, inverse-character identity and even-order p-Frobenius pairing, unique potential bad twist, number of pointed covers, and norm-character persistence under every extension degree prime toell. The subsequently added explicit family and numerical certificate are not covered by this initial reading.")

checked("A.61", "Full root reading: based arithmetic pro7 actions on the first two pro-prime groups and their deck extension; crossed homomorphisms; explicit splitting by H2 averaging; actual deck Chevalley-Weil multiplicity2d via the rechecked geometric A4 comparison; splitting field and residueF3^18; exact eigenvalue7-exponent bounds and orbit thresholds; arbitrary exponent cyclic3-then-abelian19-then-pro3 normal-core argument. The Frobenius return matrices are not computed and A12 remains Open.")
checked("B.141", "Full root reading of final explicit congruence-family addition and all code. Degree-two elliptic norm of canonical class, order3 and non-3-divisibility at every p>=5 congruent2 or5mod9, exact F5 character table, two polynomial norms, independent F25 sixth-power count, and Jacobian orders checked. Also executed the complete finite certificate with all PASS; this separate reading does not infer the infinite family from computation.")
checked("B.141", "Executed finite_checks/code/b141_canonical_example.py independently after reading it: all checks PASS, C counts6/46, baseJ36, elliptic norm obstruction, occupancy[1,1,4], relative polynomial[1,-3,4,-15,25], relative class number12 and coverJ432. Output already retained in the same program's .out; this event is a rerun, not a second independent implementation.", "computation or formal certificate")
checked("B.142 B.143", "Full root reading of all425 lines: one-sided stable Kummer kernel via B/H abelian normal quotient, finite-orbit unipotence, local root-of-unity bound, nonzero class and two-grid rigidity, all norm-proof input transport. Every nontrivial normal local subgroup is nonabelian; B=Nprime is nonzero and not assumed pro-p; least derived index makes H proper while Bprime makes H nonzero. Exact nontrivial core in an open local group and algebraic descent, without replacement by normal closure, checked.")
checked("B.144", "Full root reading including final joins: open inertia cyclotomic image, explicit wild procyclic Zp at2 and oddp, henselian/residue/transcendence claims, exact inverse-image mate c^-1 and relative structural cell, actual point map a to c(a), exclusion of relative2-isomorphism and UH-localization, finite-etale slice transfer proving slimness necessary, all finite extensions negative and every-open normal core trivial. Asayama comparison is statement-only literature, not a henselian premise.")
checked("B.145", "Full root reading of the initial general proof and genus3 example: RR reduced degree at mostg-1, exact affine twist action ut-a, every primitive index, norm persistence, smooth quartic in characteristic3, elliptic norm and explicit order7 eigencharacter, full degree2 effective-divisor coefficient count, reciprocal polynomial, and exact integer norm. The later all-twist/field-first-minimum extension is not included in this initial event.")

checked("B.145", "Full root reading of the final all-twist addition and complete expanded program: all seven integer norms independently represented by resultants and multiplication determinants, exact quadratic-period identity eta squared=-1, unit-root orders4 and28, all constant-extension divisibility tests, and field-first minimum(degree3,prime7) for every original F3 marking. The full universal B6 census remains Open.")
checked("B.145", "Executed the full expanded finite_checks/code/b145_quartic_example.py on18November2026 at05:43UTC after reading every line: all finite-field, point, character, degree-two divisor, integer norm, seven-twist and exact eigenvalue-order assertions PASS. This is a root rerun of the author's program, not a separately written implementation.", "computation or formal certificate")
checked("B.146", "Full root reading of every paragraph: arbitrary complete mixed-characteristic DVR with finitely generated residue, perfect-core constants via proper normal model, induced p-power topology on deep units, injective additive Kummer map without a surjectivity claim, exact finite-root Kummer kernel, finite-extension compatibility and relative algebraic completion equivalence. The local inertia image is I_L0 by the bounded ramification intersection argument; strict derived quotients are transferred through that surjection, without general wild freeness.")
checked("B.147", "Full root reading of all527 proof lines after B146: arbitrary-DVR tame/wild sequence without perfect residue; stable derived and nilpotent kernels; nonzero class and two-grid rigidity; split fibre before cyclic quotient choice; deep-unit normalized differences and exact scalar error; finite analytic-open density without Baire or compactness; every norm, interpolation, graph, pole-exclusion and algebraic-descent join. Gauss residue-transcendence families are strictly additional by the exact F.K.Schmidt rank-one argument. Root separately opened and read the entire Stacks0BUA statement and proof on18November2026. No all-proper-normal-subgroup result is asserted over these general bases.")

# Explicitly repaired direct dependencies. These are not transitive closures.
deps = {
    "A.1": "A.13;A.14;A.15;A.20;A.21;A.42;A.43;A.45;A.46;A.47;A.48;A.49;B.68",
    "A.13": "A.45;A.46;A.48",
    "A.18": "A.15;A.16",
    "A.19": "A.16;A.42;A.43;A.44;A.49",
    "A.20": "A.42;A.43;A.49",
    "A.21": "A.20;A.49;B.68",
    "A.23": "A.20;A.21;A.22;A.48;A.49;B.68",
    "A.24": "B.68",
    "A.25": "B.68",
    "A.30": "B.68",
    "A.31": "A.1;A.30;B.68",
    "A.32": "A.1",
    "A.33": "A.1;A.30;A.32;B.68",
    "B.2": "",
    "B.3": "B.2",
    "B.7": "B.6;A.1;A.17;B.68",
    "B.9": "",
    "B.11": "",
    "B.13": "",
    "B.14": "B.13",
    "B.15": "B.13",
    "B.16": "B.15",
    "B.17": "B.8;B.15",
    "B.18": "B.13",
    "B.22": "B.23",
    "B.23": "",
    "B.25": "",
    "B.26": "B.23;B.25",
    "B.27": "B.23;B.26",
    "B.28": "B.25",
    "B.29": "B.28",
    "B.30": "B.4",
    "B.31": "B.4;B.30",
    "B.32": "B.4;B.30;B.31;B.80;B.81",
    "B.33": "B.30",
    "B.34": "B.4;B.33",
    "B.35": "",
    "B.36": "B.35",
    "B.37": "",
    "B.38": "B.36",
    "B.39": "B.2",
    "B.40": "",
    "B.41": "",
    "B.42": "",
    "B.43": "",
    "B.44": "",
    "B.45": "B.62;B.63;B.64;B.65;B.66",
    "B.46": "",
    "B.47": "B.46",
    "B.48": "",
    "B.49": "B.48",
    "B.50": "B.47;B.49",
    "B.51": "B.49",
    "B.52": "B.49;B.51;B.53;B.54;B.55;B.57;B.106;B.110",
    "B.53": "",
    "B.54": "",
    "B.55": "B.48;B.49;B.54",
    "B.56": "B.53",
    "B.57": "B.53;B.56",
    "B.58": "B.57",
    "B.59": "B.57;B.58",
    "B.60": "B.58",
    "B.61": "B.57;B.59;B.60",
    "B.62": "",
    "B.63": "B.62",
    "B.64": "",
    "B.65": "B.62;B.63;B.64",
    "B.66": "B.62;B.65",
    "B.67": "B.35;B.36;B.37;B.38;B.40;B.41;B.42;B.82;B.83;B.84",
    "C.1": "A.1;A.30;A.31;A.33",
    "C.2": "A.1;A.24;A.25;A.30;B.68",
}
for key, value in deps.items():
    reg[key]["depends_on"] = value

REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n")
out = ROOT / "notes/ROOT_CHECK_EVENTS.tsv"
with out.open("w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["statement_id", "date", "who", "type", "outcome"])
    writer.writerows(events)
print(json.dumps({"events": len(events), "proof_checked_original": sum(v["review_state"] == "proof_checked" for v in reg.values())}))
