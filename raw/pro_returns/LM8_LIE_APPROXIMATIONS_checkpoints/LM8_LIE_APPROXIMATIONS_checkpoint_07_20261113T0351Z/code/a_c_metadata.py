#!/usr/bin/env python3
"""Regenerate the Part A/C claim, coverage, and reading ledgers from the paper."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"

def put_json(name, value):
    (SECTIONS / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n")

def readings(name, rows):
    with (SECTIONS/name).open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cote", "scan", "folio", "equation", "reading", "resolution", "used_by", "doubtful"])
        w.writerows(rows)

def main():
    # Keep a late-added result in numerical order.
    p = SECTIONS/"A.tex"
    a = p.read_text()
    if a.index(r"\begin{statement}{A.15}") < a.index(r"\begin{statement}{A.2}"):
        start = a.index(r"\begin{statement}{A.15}")
        end = a.index(r"\begin{statement}{A.2}")
        block = a[start:end].strip()
        a = a[:start]+a[end:]
        p.write_text(a.rstrip()+"\n\n"+block+"\n")

    summaries = {
      "A.1": "The discrete L structure is the filtered colimit of invariant hyperbolic peripheral structures on normal finite-index subgroups; transition maps are injective. PiL is not independently defined in the supplied body.",
      "A.2": "Germ-only LT axioms do not determine a defining subgroup up to commensurability: the two closed surface factors in P_2,0 x P_2,0 are a counterexample, also profinitely.",
      "A.3": "Every discrete hyperbolic L-group is the orbifold path extension of a finite, possibly ineffective and orientation-reversing, surface action.",
      "A.4": "The centralizer of the defining hyperbolic surface group is the finite ineffective kernel and is isomorphic to the kernel of the finite outer action. It vanishes exactly when all finite-index subgroup centralizers vanish.",
      "A.5": "Every finite extension of Z or Z^2 with specified linear action has an affine realization; the faithful-action centralizer criterion fails for torus translations.",
      "A.6": "Marked realizations are Aut_L torsors and outer-marked realizations are Out_L torsors; conformal realizations are orbit spaces. Three signatures are computed.",
      "A.7": "C2*C4, with one cusp, refutes the proposed characterization of PSL2(Z) by trivial oriented outer L-group and trivial centralizers of every finite-index subgroup.",
      "A.8": "For C2*C3 with its cusp structure, Out_L^+=1, Out_L=C2, and Aut_L=PGL2(Z); its six epimorphisms to S3 form one conjugation orbit and have characteristic kernel F2.",
      "A.9": "For P hyperbolic and A finite abelian, Out_L(P x A)=Hom(P^ab,A) semidirect (Out_L(P) x Aut(A)); ineffective groups retain gerbe automorphisms absent from the effective coarse orbifold.",
      "A.10": "Exact finite enumeration: all 24 groups of order <=12, all 42 admissible faithful closed genus-two group/signature rows, 17 realizable rows, 126 ineffective rows; 4368 small signatures, 4258 hyperbolic and 66 bad.",
      "A.11": "A finite extension of a specified profinite surface completion is the completion of its discrete finite-action extension when its outer action lifts to the discrete peripheral outer group; this factorization is necessary for a realization preserving that discretization.",
      "A.12": "Unrestricted profinite finite-action realization is not established: an arbitrary finite peripheral outer action must be shown to preserve a discrete surface lattice up to conjugacy, or a counterexample must be found.",
      "A.13": "The profinite L definition uses invariant completed loop structures on normal open subgroups, rank-one Zhat orientation modules and continuous germs; peripheral recovery makes transition maps injective. LT additionally retains a defining commensurability class.",
      "A.14": "The finite ineffective-kernel centralizer criterion and Aut/Out marking torsor assertions remain valid for profinite hyperbolic L extensions.",
      "A.15": "Out_L,cts of the completed modular orbifold group surjects onto Zhat units by its rational arithmetic action, so the discrete conclusion Out_L=C2 does not extend literally.",
      "A.16": "The mixed-prime involution x->x^lambda,y->y of Fhat2, lambda_2=-1 and lambda_odd=1, has a semidirect extension that is not the completion of any finitely generated discrete group. It fails both standard peripheral structures, so is not an A.12 counterexample.",
      "A.17": "Every finite subgroup of the geometric closure for S_1,1 is conjugate to a discrete subgroup and realizable; its effective image has one of nine abstract types. The same holds for finite solvable subgroups of orientation-preserving geometric closures for every hyperbolic surface of genus<=2.",
      "A.18": "Geometric realization forces global orientation signs and integral homology characters. Tripod realization would imply every finite subgroup of GT is trivial or C2 and multiplier-one torsion is absent. The checked recent theorems concern mapping class completions or pro-p groups and do not establish full peripheral realization."
    }
    adeps = {
      1: [], 2: ["A.1"], 3: ["A.1", "Kerckhoff1983", "BeringQingWigglesworth2024"],
      4: ["A.3"], 5: [], 6: ["A.3"], 7: ["A.4", "A.6", "code/a_small_actions.py"],
      8: ["A.4", "A.6", "code/a_small_actions.py"], 9: ["A.1"],
      10: ["A.3", "code/a_small_actions.py"], 11: ["A.3"],
      12: ["A.11", "A.13", "A.14"], 13: ["A.1", "A.2", "BoggiZalesskii2019"],
      14: ["A.11"], 15: ["A.8", "A.13", "C.1"],
      16: ["code/a_profinite_obstructions.py"],
      17: ["A.3", "A.11", "BuxErshovRapinchuk2011", "ZalesskiiMelnikov1989", "Boggi2026Symmetric", "code/a_profinite_obstructions.py"],
      18: ["A.13", "A.16", "A.17", "BoggiZalesskii2025", "HerfortZalesskii2013", "LochakNakamuraSchneps2026", "Schneps1997Survey"]
    }
    anotes = {
      1: "The damaged exceptional-type list is explicitly repaired to 2g-2+n>0; original scans 179-182 are absent. Orientation is a line without chosen generator; + fixes a generator.",
      2: "Closed genus-two factors have empty peripheral lists and trivial intersection. The literal existence axiom is refuted; the corrected definition includes the class as datum.",
      3: "Full reduction to Nielsen realization includes an explicit center-free pullback construction and equality of extension classes; no splitting is assumed.",
      4: "All finite-index subgroups, not merely the center. P_2,0 x S3 shows center-freeness alone insufficient.",
      5: "Exceptional nonhyperbolic types are not silently included in A.3/A.4. Averaging solves the real-valued extension cocycle.",
      6: "Examples (0;2,3;1), (0;2,4;1), and once-punctured torus, including the C4-fixed marked parameter i. Markings and unmarked conformal moduli are distinguished.",
      7: "Index-four kernel in C2*C4 is the once-punctured-torus group; finite action group C4 is within the requested bound.",
      8: "All six finite pairs and their S3 conjugacy orbit are enumerated, not sampled.",
      9: "Explicit product-gerbe theorem, including the (C2)^4 gauge subgroup for a genus-two surface. No replacement by a coarse space.",
      10: "Existence of generating vectors is exhaustive in the stated boxes; Hurwitz/Nielsen orbits are not counted. Genus<=2 with unbounded punctures is an infinite request. Orientation-reversing enumeration is not performed; realization theorem includes it.",
      11: "Center-freeness is independently proved from faithful regular-quotient actions on finite-cover homology. LM3 is not used as proof authority.",
      12: "Audit-unresolved, not a literature-wide openness claim. Further attack A.16-A.18 proves realization for geometric closures (all finite groups in S_1,1, solvable finite groups in oriented genus<=2), refutes blanket bare-free-profinite realization, and identifies a GT torsion implication. Missing: conjugacy of arbitrary peripheral finite subgroups into geometric closure, or a genuinely peripheral counterexample. LM4 not supplied.",
      13: "Primary Proposition 3.6 was opened and checked, including the algebraically-simple hypothesis; only integer nonzero powers needed for open germs.",
      14: "Independent proof that centralizers of open subgroups of the geometric completion vanish. No unproved profinite unique-roots assertion is used.",
      15: "Uses the arithmetic action on [(P1-{0,1,infinity})/S3] and local Kummer inertia; no faithfulness theorem for the whole Galois action is needed. Finite-subgroup question remains A.12.",
      16: "Explicit independent proof by prime-dependent free rank of abelianization. Exhaustive 48-element metabelian quotient certifies failure of the standard torus commutator condition; tripod exclusion survives all profinite markings. Not claimed to exclude every possible torus peripheral structure. Each pro-prime action separately geometric.",
      17: "Asada outer congruence form verified in Bux-Ershov-Rapinchuk Main Theorem. Zalesskii-Melnikov Theorem3.10 hypotheses A/B explicitly checked. Exact 10 and16 subgroup enumerations of D8,D12, not conjugacy counts. Boggi2026 Theorem5.1(i) used only for finite solvable subgroups and orientation-preserving mappings.",
      18: "Necessary conditions and logical implication proved, not claimed sufficient. GT injectivity into pure peripheral Out proved using normalizers. Source audit separates torsion in mapping class completions from torsion inside GT. Schneps1997 question cited historically, not as current openness certification."
    }
    apass = {
      1: ["C4 §52.1, folios 737-738, scans 179-181; scan 4 table heading"],
      2: ["C4 §52.1, folios 742-743, scans 190-191"],
      3: ["C4 §52.1, folios 738-739, scans 182-183"],
      4: ["C4 §52.1, folio 739, scans 183-184"],
      5: ["C4 §52.1, folio 737, scans 179-180"],
      6: ["C4 §52.1, folios 739-741, scans 183-188"],
      7: ["C4 §52.1, folios 740-741, scans 185-188"],
      8: ["C4 §52.1, folios 740-741, scans 185-188"],
      9: ["C4 §52.1, folios 739,741,743, scans 183-184,187-192"],
      10: ["C4 §52.1, folio 739, scan 183; program requested by Part A(b)"],
      11: ["C4 §52.2, folio 744, scan 193; comparison requested with LM3 B.8-B.11"],
      12: ["C4 §52.2, folio 744, scan 193; Part A(e)"],
      13: ["C4 §52.1-2, folios 741-744, scans 188-193"],
      14: ["C4 §52.1-2, folios 739-740,744, scans 183-186,193"],
      15: ["C4 §52.1-2, folios 741,744-745, scans 188,193-195"],
      16: ["C4 §52.2, folio744, scan193; PartA(e) finite-action extension"],
      17: ["C4 §52.1-2, folios739,744, scans183,193; PartA(e)"],
      18: ["C4 §52.1-2, folios741,744, scans188,193; PartA(e)"]
    }

    csummaries = {
      1: "Finite curve quotient, finite etale scheme cover, injectivity of all inertia maps into etale pi1, and an ordinary analytic universal cover are equivalent for a smooth separated DM curve over Qbar.",
      2: "For effective orbifold curves the only exceptions are P1 with one cone point or two unequal cone orders; each football has pi1=C_gcd(m,n) and explicitly noninjective inertia in the bad cases.",
      3: "For arbitrary DM curves the extra exceptions are spherical gerbes whose weighted-projective universal cover is not P(1,1); the exact cases are listed by effective orbifold signature and cyclic kernel of generic inertia. P(n,n) is a bad gerbe for n>1.",
      4: "Existence of a finite etale curve cover over an algebraic closure descends to every characteristic-zero field after changing the cover and finite group. In particular existence descends from Qbar to Q.",
      5: "For a smooth integral-base DM stack with relative normal-crossings boundary meeting every residue characteristic, every finite etale cover of the complement extends uniquely over the boundary.",
      6: "pi1^et(M_1,1 over Z)=1. Nontrivial inertia therefore prevents every finite etale scheme atlas and every quotient presentation [C/G] with G constant finite.",
      7: "Over Z[1/3], M_1,1=[Y(3)/GL2(F3)] with group order48; fixed Weil-pairing geometric components have group SL2(F3) of order24.",
      8: "The labelled schemes M_0,4 over Z and M_0,5 over Z both have trivial etale fundamental group.",
      9: "The quotient stacks [M_0,4/S4] and [M_0,5/S5] over Z have etale fundamental groups S4 and S5. The four-point action has kernel V4, and its effective S3 quotient is a different stack. M_0,5 has dimension2.",
      10: "Exact checks cover all144 ordered football pairs in the box1..12, all24 cross-ratio permutations, all120 five-point boundary permutations, GL2(F3), and the integral Weierstrass algebraic ingredients."
    }
    cdeps = {1: ["BehrendNoohi2006"], 2: ["C.1", "BehrendNoohi2006"],
             3: ["C.1", "C.2", "BehrendNoohi2006"], 4: ["C.1"],
             5: ["SGA1"], 6: ["C.5", "SGA1", "Milne2020ANT"],
             7: ["Bruin2007"], 8: ["C.5", "Milne2020ANT"],
             9: ["C.8", "code/c_stack_checks.py"], 10: ["code/c_stack_checks.py"]}
    cnotes = {
      1: "Behrend-Noohi Theorems4.2,4.4,1.1; Remark4.3; Proposition7.2; Corollary7.7. Scheme frame-torsor construction and comparison spelled out.",
      2: "Complete family-wise counterexample proof, not a representative-only example; effective hypothesis explicit.",
      3: "Behrend-Noohi Propositions7.4-7.6, Corollary7.7. Source misprint k corrected to d using its proof; final subgroup-generator slip repaired by a kernel of pi1(surface)->C_n. No statement depends on these slips.",
      4: "No field-of-moduli obstruction to existence: descend to finite L, compose the etale atlas, then take a frame torsor/Galois closure. Geometric connectedness of the cover is not asserted.",
      5: "SGA1 XIII Proposition5.5 checked in original primary PDF; generic tameness forces every boundary ramification index prime to every p, hence1. X Theorem3.1 purity checked.",
      6: "Full integral Weierstrass atlas W=A5-V(c4,Delta), connected coordinate-change group, purity, and Minkowski argument. Includes primes2 and3; not inferred from a Z[1/6] presentation.",
      7: "Bruin section4 explicit full-level3 construction and Theorem7.1 opened. Small-prime failure of this level cover is separated from C.6.",
      8: "Explicit P1 and three-point blowup compactifications with relative SNC boundary. All-finite-prime arithmetic argument uses boundary sections; M04 need not have an integral point itself.",
      9: "Constant finite groups are etale even when p divides their order; quotient atlas remains a torsor. Ineffective V4 is retained. Dimension corrects the curve wording for M05.",
      10: "All stated finite boxes exhausted; symbolic tangent determinant=-1 proves every residue characteristic at once. pi1 claims depend on proofs, not finite testing."
    }

    pattern = r"\\begin\{statement\}\{([AC]\.\d+)\}\{([^}]+)\}\{([^\n]*)\}\n(.*?)\\end\{statement\}"
    for part in ["A", "C"]:
        tex = (SECTIONS/f"{part}.tex").read_text()
        data = []
        for sid, status, title, body in re.findall(pattern, tex, re.S):
            num = int(sid.split(".")[1])
            data.append({"id": sid,
                         "statement": summaries[sid] if part == "A" else csummaries[num],
                         "status": status,
                         "where_proved": f"sections/{part}.tex, Statement {sid}",
                         "depends_on": adeps[num] if part == "A" else cdeps[num],
                         "manuscript_passages": apass[num] if part == "A" else
                             ["C4 §52.2, folios 744-746, scans 193-197"],
                         "depends_on_doubtful_reading": part == "A" and num == 1,
                         "notes": anotes[num] if part == "A" else cnotes[num]})
        assert len(data) == (18 if part == "A" else 10), (part, len(data))
        put_json(f"{part}_results.json", data)

    put_json("A_coverage.json", [
      {"task":"item1", "requested":"Discrete/profinite L-groups from finite surface actions, nonuniqueness and centralizers", "status":"partial", "results":["A.1","A.2","A.3","A.4","A.6","A.11","A.12","A.13","A.14","A.15","A.16","A.17","A.18"], "remaining":["Unrestricted profinite finite-action realization A.12"]},
      {"task":"A(a)", "requested":"Definitions L, PiL, TL discrete and profinite", "status":"complete_with_reading_correction", "results":["A.1","A.2","A.13"], "remaining":[]},
      {"task":"A(b).theorem", "requested":"Every discrete L-group arises from a finite surface action", "status":"proved_in_hyperbolic_definition", "results":["A.3","A.5"], "remaining":[]},
      {"task":"A(b).program", "requested":"Small orbifold signatures and finite extensions of surfaces of genus<=2 by groups of order<=12", "status":"complete_for_declared_finite_boxes", "results":["A.7","A.8","A.10"], "remaining":["Unbounded punctures do not define a finite enumeration; nonorientable quotient signatures and Hurwitz orbit counts are outside the stated program box"], "program":"code/a_small_actions.py", "outputs":["code/a_small_actions.json","code/a_small_actions.out","code/a_small_signatures.csv"]},
      {"task":"A(c)", "requested":"Exact nonuniqueness torsor or orbit description and three examples", "status":"proved", "results":["A.6","A.9"], "remaining":[]},
      {"task":"A(d)", "requested":"Centralizers scans185-186 and Teichmueller groups scans187-188", "status":"refuted_characterization_and_proved_replacements", "results":["A.3","A.4","A.7","A.8","A.9"], "remaining":[]},
      {"task":"A(e)", "requested":"Profinite counterparts using LM3 B8-B11 and LM4 if present", "status":"partial_with_stronger_realization_theorems", "results":["A.11","A.12","A.13","A.14","A.15","A.16","A.17","A.18"], "remaining":["Put arbitrary finite peripheral subgroup into geometric closure up to peripheral conjugacy, or construct a genuinely peripheral counterexample", "LM4 package not supplied; LM3 does not imply arbitrary invariant-lattice existence"], "program":"code/a_profinite_obstructions.py", "outputs":["code/a_profinite_obstructions.json","code/a_profinite_obstructions.out"]}
    ])
    put_json("C_coverage.json", [
      {"task":"item2", "requested":"Modular multiplicities as finite curve quotients over Qbar,Q,Z", "status":"refuted_and_classified", "results":["C.1","C.2","C.3","C.4","C.6","C.9"], "remaining":[]},
      {"task":"C.question", "requested":"State manuscript question exactly", "status":"complete", "results":["C.1","C.6"], "remaining":[], "location":"sections/C.tex opening paragraph; §52.2 folios744-746 scans193-197"},
      {"task":"C.Qbar", "requested":"Classification with theorem numbers, exceptions, counterexample proof for each", "status":"complete", "results":["C.1","C.2","C.3"], "remaining":[]},
      {"task":"C.Q", "requested":"Descent of geometric finite quotient to Q", "status":"proved", "results":["C.4"], "remaining":[]},
      {"task":"C.Z.M11", "requested":"Compute etale pi1 overZ and infer presentation consequence", "status":"proved_and_refuted", "results":["C.5","C.6","C.7"], "remaining":[]},
      {"task":"C.Z.M04_M05", "requested":"Genus-zero examples with symmetric groups", "status":"proved_with_dimension_correction", "results":["C.8","C.9","C.10"], "remaining":[], "program":"code/c_stack_checks.py", "outputs":["code/c_stack_checks.json","code/c_stack_checks.out"]}
    ])
    readings("A_readings.csv", [
      ["140-4","4","table","heading","PiL heading versus LT/TL in body","Scan4 image inspected; no independent third definition in supplied body; do not invent PiL axioms","A.1","yes"],
      ["140-4","179-180","737","definition","Exceptional anabelian type list damaged; (0,1) associated to Z","Images absent; checked transcript read; use explicit mathematical convention 2g-2+n>0 and mark the correction","A.1; A.5","yes"],
      ["140-4","181","738","(1)-(3)","Invariant normal-finite-index colimit; transition maps injective","Checked transcript; proof reproduced, no image claimed","A.1","no"],
      ["140-4","183-184","739","finite actions","Every L-group seems to arise from finite surface action; faithful iff finite-index centralizers trivial","Scan183 image inspected; scan184 checked transcript. Ineffective actions explicitly retained","A.3; A.4","no"],
      ["140-4","185-186","740","characterization","Direct L-autos inner and center/centralizer conditions might characterize modular group","Both scan images inspected. Characterization refuted by C2*C4; modular assertions separately proved","A.7; A.8","no"],
      ["140-4","187","741","Teichmueller group","Out_L(Pi), or Out_L(Pi^+) as preferred alternative","Checked transcript read; alternatives recorded, no equivalence silently assumed","A.6; A.8; A.9","no"],
      ["140-4","188","741","(5)","Orientation module T rank1; finite set of outer germs; natural/sharp superscript","Image inspected; mathematical germ content clear; decorative superscript left immaterial","A.1; A.13","no"],
      ["140-4","189-191","742-743","LT axiom","Remove finite-index condition but require normality and all germs to factor; uniqueness up to commensurability asserted","Images absent; checked transcript read. Empty-peripheral product counterexample refutes literal uniqueness","A.2","no"],
      ["140-4","193","744","(8)","Profinite extension of germ definitions called essentially evident","Image inspected; completed definition and peripheral-recovery theorem explicitly supplied. Further finite-action attack separates geometric closure from full peripheral outer group and pro-p from full profinite","A.11; A.12; A.13; A.14; A.16; A.17; A.18","no"],
      ["140-4","195","745","(12)","Arithmetic exact sequence makes a TL-group","Checked transcript; used with geometric kernel specified; no reconstruction from germs alone","A.2; A.15","no"]
    ])
    readings("C_readings.csv", [
      ["140-4","193","744","(9)","Connected finite-type separated smooth multiplicity of relative dimension1 proposed as (U,G)","Image inspected; read as DM stack quotient, no effectiveness assumed","C.1; C.2; C.3","no"],
      ["140-4","194","744","intrinsic reformulation","Finite etale cover which is a scheme; characteristic0 imposed thereafter","Image inspected; finite scheme atlas equivalence proved by frame torsor","C.1; C.4","no"],
      ["140-4","194","744","(10)-(11)","Pi1(U|M,G;a) letter doubtful in transcription","Image inspected; U is mathematically required in quotient path extension. No proof depends on deciphering that letter","C.1","yes"],
      ["140-4","195","745","(12)","Arithmetic kernel carries invariant L-structure","Checked transcript; valid after finite curve cover, excluding the classified bad stacks","C.1; C.3; C.4","no"],
      ["140-4","196-197","745-746","modular discussion;(13)","Modular multiplicities over Q and evenZ, categories versus2-categories, universal curve extension","Checked transcript; integral claim tested independently, not inferred by base change fromQ","C.5; C.6; C.7; C.8; C.9","no"]
    ])
    print("Regenerated A/C results, coverage and readings; A has18 statements, C has10.")

if __name__ == "__main__":
    main()
