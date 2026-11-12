#!/usr/bin/env python3
"""Build Part D's statement, reading, and task registers from explicit metadata."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parent.parent

titles={
1:"Explicit semidirect-product descriptions of M(Z), M(Z_p), and M(Q_p)",
2:"All local norm images, norm-one groups, determinant valuations, and sign restrictions",
3:"Product and restricted-product descriptions of integral and finite adelic points",
4:"Conditional typed congruence comparison and global-sign obstruction to openness",
5:"Exhaustive finite I/II equations at moduli 2, 3, 4, 6, 12",
6:"Nontrivial modular congruence kernel through the simple quotient SL2(F8)",
7:"Actual Galois, GT, and GT0 comparisons, images, and invisible loop solutions remain unresolved",
8:"Eight geometric central extensions of V4 by C2; manuscript class D8 and nonnormal complements",
9:"Central extensions of M_C, M(0)_C, and M[0]_C by mu2 form F2^5",
10:"No integral central extension of mu2^2 by mu2 has the dihedral generic fibre",
11:"Arithmetic descent and the integral mu2-extension group at 2 remain unresolved",
12:"The manuscript cup product (-3,3) is split; explicit full D8 Galois lift",
13:"The distinct symbol (-1,-3) has order 2; scan631 C4 is a finite group",
14:"No constant Dic3 lift of an S3 character with imaginary sign Q(sqrt(-3))",
15:"Full constant Dic3 lifting criterion and its class-field-theoretic solution over Q",
16:"Explicit constant and arithmetic-twisted full lifts with complete local ramification",
17:"Exact modular generation and indices for all n, enumerated through 48",
18:"Motivic specialization for elliptic torsion and unipotent fundamental groups",
19:"Arbitrary integral discrete monodromy is insufficient and arithmetic descent is not unique",
20:"Necessary and sufficient equivariant datum for arithmetic descent; H1 of the centralizer"
}
statuses={i:"Proved" for i in titles}
statuses.update({7:"Open",11:"Open",12:"Refuted",14:"Refuted",18:"Known",19:"Refuted"})
deps={
1:"A.1; B.1",2:"D.1",3:"D.1; D.2",4:"D.2; D.3; B.9",
5:"explicit finite quotient and relations (I),(II)",6:"discrete modular presentation; D.17 elementary generation",
7:"D.4; D.5; D.6",8:"scan602 square rule; D_finite.py",9:"D.8; A.1; Kummer sequence",
10:"Hopf-algebra character calculation",11:"D.8; D.9; D.10",
12:"D.8",13:"D.12; local Hilbert-symbol formulas",
14:"D.8; D_finite.py",15:"D.13; D.14; Milne I.4.16",
16:"D.12; D.14; D.15",17:"elementary matrix identities",
18:"Hain-Matsumoto A.6, 8.2-8.4; MEM Definition6.1, Theorem6.9, Corollary6.10",
19:"D.18; discrete modular presentation",20:"D.18; D.19"
}
passages={
1:"48; 542-543; 479-481",2:"48; 542-543; 479-481",3:"49; 576; 546",
4:"48; 543; 481-482; 49; 628 verso (lower651); 652",
5:"38-47 comparison; 49; 606; 605 (loop generators)",
6:"38-47 comparison and After LM3 task D.b",
7:"38-47 comparison; 48; 543; 481; After LM3 task D.b",
8:"49; 602-608; 596-610, especially602(90),609(111)",
9:"49; 608-609; 610; 48; 542-543; 479-481",
10:"49; 602-608; 596-610; distinction constant C2 versus mu2 at2",
11:"49; 608-609; 610; task D.c integral classification",
12:"49; 609; 610-611(115)",
13:"49; 619; 631; compare609;611",
14:"49; 606,618-620; 605,629,631,634",
15:"49; 619-620; 631-634",
16:"49; 606,618-620; 605,629-634",
17:"49.VI; 628 verso (lower651); 652",
18:"48; 547; 489",19:"48; 547; 489",20:"48; 547; 489"
}
doubts={
4:"481 target modulo Sigma; no unchosen central section is assumed",
8:"603 E'|E'' in automorphism group; 609 order4|8 and first quotient factor",
10:"none: depends on whether the intended group scheme is constant or mu2, stated explicitly",
12:"610 H^2; 611 mu2 and H^2 for quadratic characters; the quadratic fields themselves are legible",
13:"631 Pi0|Pi; C4 is visibly a group in a displayed extension",
14:"631 Pi0|Pi; 634 constant versus arithmetic-twisted target is a mathematical distinction",
16:"631 Pi0|Pi; 634 constant versus arithmetic-twisted target",
17:"652 G^+|G^*, peut etre|pas alors; interpretations are treated separately",
19:"489 generiquement reductifs: either reading is insufficient"
}
notes={
1:"H_R multiplication and conjugation action given explicitly. Integral group C6 x (SL2Z semidirect D8).",
2:"Includes ramified primes2,3; explicit noncanonical norm-one decompositions. Norm enumerations modulo4,8,16,9,27,25,49 executed.",
3:"Affine finite presentation and finitely many denominators prove equality as topological groups.",
4:"Actual bare-source comparisons are NOT claimed constructed. Global-sign-compatible images cannot be open in full signed M(Zhat); explicit extra point at5.",
5:"Finite necessary equation solutions, NOT asserted actual finite images of GT0, GT, or G_Q. Simultaneous commutator-word evaluation and automorphism consistency both tested.",
6:"Proof uses an exact 504-element group enumeration and its conjugacy classes. Does not produce a GT0 element.",
7:"Partial triple: nonopenness proof, five finite computations, exact n3/lambda1 lift instance and SL2F8 invisible-solution obstruction.",
8:"Geometric finite classification complete; program16 cocycles/2 coboundaries. The two complements are nonnormal but their intersection is normal.",
9:"Kummer/UFD proof; explicit component section and invariant character action. Integral/arithmetic classification is not claimed.",
10:"Every extension with exact integral kernel/quotient mu2,mu2^2 is commutative, by connectedness and internal Hom.",
11:"First unresolved map Ext_cen(M[0]_Z2,mu2) to Ext_cen(M[0]_Q2,mu2); flat torsors on nonreduced special fibre not classified.",
12:"Explicit matrices split quaternion; full field Q(3^(1/4),i) has D8 and ramification exactly2,3. The claimed nonzero class is false.",
13:"Hilbert symbols at3 and infinity are negative; at2 positive. Nonzero class is Bockstein for constant C4 lifting of chi_-3.",
14:"Finite group verified as SL2Z4/V4; unique involution and complex conjugation forbid constant lift, independently of surjectivity.",
15:"General obstruction (a,-1); overQ squarefree sign d>0 with all odd prime divisors1mod4. Full-image condition and all lift choices proved.",
16:"K5=split(x3-12x-14).Q(zeta5), degree12, ramification2,3,5. K=Q(cuberoot2,fourthroot3,i), degree24 and full Dic3 overQi, ramification2,3. All local degrees proved; programs verify exact finite certificates.",
17:"SL2 index1, GL2 indexphi(n)/2 for n>2. Closure in GL2(Zhat) has infinite index; G+ terminology must distinguish tau.",
18:"Known results are reduced explicitly: base change of torsion sheaf, Weil pairing, specialization of pro-MEM, Kummer basis checking Hain-Matsumoto hypothesis.",
19:"Explicit rank2 integral monodromy with non-quasiunipotent cusp; six exact quadratic-twist point counts.",
20:"Semidirect-product proof and explicit centralizer cocycle; states full extra motivic and integral data required."
}
rows=[]
for i,title in titles.items():
 rows.append(dict(id=f"D.{i}",statement=title,status=statuses[i],
  where_proved=f"sections/D.tex, D.{i}"+(" (partial results and exact obstruction)" if i in (7,11) else " and its proof"),
  depends_on=deps[i],manuscript_passages=passages[i],
  depends_on_doubtful_reading=doubts.get(i,"none"),notes=notes[i]))

readings=[
dict(package="LM_C3-473-491",scan="481",
 **{"the \\unsure or \\illegible place":"(24)-(25), target divided by Sigma",
 "what the mathematics supports":"The written comparison initially lands modulo central global signs. An unquotiented comparison needs a pullback extension and a section; D.4 leaves its existence on the bare groups open.",
 "how strongly":"Exact target typing; no palaeographic emendation claimed."}),
dict(package="LM_C3-587-605",scan="602",
 **{"the \\unsure or \\illegible place":"epsilon2(unsure{u}) epsilon3(unsure{u})=1, and square criterion(90)",
 "what the mathematics supports":"With quotient coordinates (epsilon3,epsilon2), the square is u(u+v); it is zero exactly on the two lines epsilon3=1 or epsilon2 epsilon3=1.",
 "how strongly":"Exact finite enumeration and cocycle proof; supports the indicated quotient-sign interpretation."}),
dict(package="LM_C3-587-605",scan="603",
 **{"the \\unsure or \\illegible place":"Aut(unsure{E'|E''}) is C2",
 "what the mathematics supports":"E'' is cyclic of order4 and has automorphism group C2. E' is V4, with automorphism group S3, so E'' is mathematically required in this sentence.",
 "how strongly":"Decisive group-order evidence; reading remains editorial."}),
dict(package="LM_C3-606-624",scan="609",
 **{"the \\unsure or \\illegible place":"x.u serait d'ordre unsure{4|8}",
 "what the mathematics supports":"Under the hypothetical commuting product C2 x C4, x.u has order4, not8.",
 "how strongly":"Decisive calculation for the stated hypothesis."}),
dict(package="LM_C3-606-624",scan="609",
 **{"the \\unsure or \\illegible place":"E'' maps to unsure{mu x {1}}; E''/2E'' versus E''/E''[2]",
 "what the mathematics supports":"The first factor is correct for ordering (epsilon3,epsilon2), since E'' is epsilon2=1. For C4, 2E''=E''[2], so the two quotient readings are mathematically indistinguishable.",
 "how strongly":"Strong on the factor; no discrimination between quotient readings."}),
dict(package="LM_C3-606-624",scan="610",
 **{"the \\unsure or \\illegible place":"kernel mu of unsure{E_ab|E} -> mu x mu",
 "what the mathematics supports":"The map E_ab -> V4 is an isomorphism; its kernel is trivial. The nontrivial central kernel belongs to E -> V4, so E is required.",
 "how strongly":"Decisive order and abelianization computation."}),
dict(package="LM_C3-606-624",scan="611",
 **{"the \\unsure or \\illegible place":"xi',xi'' in H^2(Q,unsure{mu2}); fields Q(sqrt(-3)), Q(sqrt3); nonzero and nonsplit overQi",
 "what the mathematics supports":"Quadratic characters are in H^1. Their cup is (-3,3)=0, with an explicit M2Q splitting. The named fields were read visually; the nonvanishing assertion is false, not a justified reason to change a sign in the transcription.",
 "how strongly":"Decisive algebra and local checks; no silent emendation of the legible fields."}),
dict(package="LM_C3-625-643",scan="631",
 **{"the \\unsure or \\illegible place":"SL2(Z)/unsure{Pi0|Pi}; E''=Z/4Z; canoniquement",
 "what the mathematics supports":"The quotient by Pi0, realized modulo4 by the displayed normal V4, has sigma of order4. The C4 is a finite group, while its Galois obstruction has Brauer order2. A generator choice is needed for an abstract identification with Z/4.",
 "how strongly":"Exact finite quotient and order test; distinguishes group order from cohomology exponent."}),
dict(package="LM_C3-625-643",scan="634",
 **{"the \\unsure or \\illegible place":"ordinary lift G_Q -> tilde G3; contextual choice between constant and arithmetic-twisted target",
 "what the mathematics supports":"The constant interpretation with signQsqrt(-3) is impossible; retaining determinant action gives a full twisted lift and a genuine full lift overQi. This is a mathematical correction, not a claim to settle lexical unsure{delectable}.",
 "how strongly":"Complete complex-conjugation obstruction and explicit degree24 Galois construction."}),
dict(package="LM_C3-644-662",scan="652",
 **{"the \\unsure or \\illegible place":"unsure{G^+|G^*}; unsure{peut etre|pas alors}; integral adelic generation",
 "what the mathematics supports":"rho,sigma generate all SL2 congruence quotients. Adding tau gives determinant±1 in GL2, with indexphi(n)/2 and infinite adelic index. These facts do not select a glyph but forbid a universal finite-index claim.",
 "how strongly":"Proof for all n and exact enumerations1..48; interpretation-dependent, no glyph chosen."}),
dict(package="LM_C3-473-491",scan="489",
 **{"the \\unsure or \\illegible place":"representations into integral points of unsure{generiquement} reductive group schemes",
 "what the mathematics supports":"The qualifier does not suffice: the explicit counterexample already has target GL2/Z. Arithmetic equivariance and compatible realizations are extra data.",
 "how strongly":"Complete counterexample and formal descent criterion; neither lexical alternative repairs the assertion."})
]

def cov(task,outcome,ids,proved,computations,undecided="None in the stated corrected scope."):
 return dict(task=task,outcome=outcome,statement_ids=ids,proved_cases=proved,
  executed_computations=computations,exact_smallest_undecided_instance=undecided)
coverage=[
cov("D.a","proved","D.1-D.3",
 "Final modular M overZ, all Zp/Qp, Zhat and Af; full group laws, local norm kernels, valuation/sign restrictions.",
 "D_gt.py/.out: norms modulo4,8,16,9,27,25,49."),
cov("D.b","partly settled","D.4-D.7",
 "Conditional lifted comparison; global-sign nonopenness and explicit extra point; modular congruence kernel maps nontrivially to SL2F8.",
 "D_gt.py/.out: finite I/II at2,3,4,6,12 and full SL2F8 enumeration.",
 "n3, lambda=1, fxy=[[1,1],[1,2]]: lift simultaneously to a profinite GT0 pair, then GT or G_Q. Separately construct a loop solution trivial in all congruence coordinates but nontrivial in SL2F8. Bare-source comparison/lift and image/kernel remain to be identified."),
cov("D.c","partly settled","D.8-D.11",
 "All eight geometric V4 extensions; full H2 of M_C,M(0)_C,M[0]_C equalsF2^5; prescribed class nonsplit and complements nonnormal; no literal mu2^2/mu2 dihedral model at2.",
 "D_finite.py/.out: exhaustive cocycles; D_components.py/.out: explicit component section and invariant characters.",
 "Kernel and image of Ext_cen(M[0]_Z2,mu2) -> Ext_cen(M[0]_Q2,mu2), including flat torsors on the nonreduced fibre; arithmetic descent of all geometric classes."),
cov("D.d","refuted","D.12-D.13",
 "Literal c=(-3,3)=0, order1; distinct(-1,-3) ramifies3,infinity, order2; C4 onscan631 is an inverse-image group.",
 "D_finite.py/.out: explicit matrix algebra splitting; D_number_fields.py/.out: Hilbert symbols."),
cov("D.e","refuted","D.14-D.16",
 "Constant imaginary-sign lift impossible; exact classfield criterion proved. Full constant sign√5 example and full twisted sign√-3 example with ramification proved.",
 "D_finite.py/.out: Dic3 quotient; D_number_fields.py/.out: cubic/index/characters; D_arithmetic.py/.out: order24 quotient and local Eisenstein certificates."),
cov("D.f","proved","D.17",
 "SL2 index1 for alln; GL2 indexphi(n)/2 for n>2 and index1 for n=1,2, determinant quotient; full adelic finite-index guess refuted.",
 "D_finite.py/.out: exact generated matrix groups for every1<=n<=48."),
cov("D.g","proved","D.18-D.20",
 "Explicit MEM realization definition, torsion and pro-unipotent specialization, proof of Hain-Matsumoto reductions, counterexample to arbitrary discrete input and exact arithmetic descent criterion.",
 "D_motives.py/.out: monodromy matrices, six twist point counts, free Lie ranks1..6."),
cov("item3","proved","D.1-D.3; D.18-D.20",
 "Adelic points computed; motivic construction proved in the stated compatible-realization sense for the two requested geometric families; arbitrary integral-input formulation refuted.",
 "D_gt.py/.out norms; D_motives.py/.out."),
cov("item4","partly settled","D.8-D.17",
 "Geometric extensions, complements, Brauer class, corrected classfield exercise, all requested modular indices.",
 "D_finite.py/.out; D_components.py/.out; D_number_fields.py/.out; D_arithmetic.py/.out.",
 "D.11: integral mu2-extension classification for M[0] overZ2 and arithmetic descent; no claim of full integral H2."),
cov("Lead4","refuted","D.8-D.13; D.16",
 "The written extension is a finite D8 inflation; literal cup(-3,3) iszero. The proposed(-1,-3) is a different nonzero order2 class; retained arithmetic determinant twisting gives the corrected full lift.",
 "D_finite.py/.out; D_number_fields.py/.out; D_arithmetic.py/.out.")
]
paper=(root/"sections/D.tex").read_text()
heads=re.findall(r"\\begin\{statement\}\{(D\.\d+)\}\{([^}]+)\}",paper)
assert len(heads)==20 and set(heads)=={(r["id"],r["status"]) for r in rows}
for name,data in [("D_results.json",rows),("D_readings.json",readings),("D_coverage.json",coverage)]:
 (root/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
from collections import Counter
print(json.dumps(dict(statements=len(rows),statuses=dict(Counter(r["status"] for r in rows)),
 readings=len(readings),coverage_rows=len(coverage),
 outcomes=dict(Counter(r["outcome"] for r in coverage))),indent=2))
