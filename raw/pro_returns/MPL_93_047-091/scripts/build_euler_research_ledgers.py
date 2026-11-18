#!/usr/bin/env python3
"""Write only the Euler research event and context-search ledgers.

This script does not inspect images or modify the frozen transcription. Search
hits document targeted context lookups; they are not mathematical proof checks.
The event descriptions record actual post-freeze reasoning/source checks made
on 2026-11-18, not an automated claim that every cited theorem was reproved.
"""

import csv
import re
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
CONTEXT = PACKAGE.parent / "context"
RECORDS = PACKAGE / "records"
WHO = "GPT-6 Astra Pro; effort not exposed; run MPL_93_047-091/research_euler"
DATE = "2026-11-18"

QUERIES = {
    1: r"Euler|\\chi|orientation|topolog|S20",
    2: r"singuli|faisce|cohomolog|Alexander",
    3: r"compact|support|axiome",
    4: r"suite exacte|supp.*compact|ferm|additivit",
    5: r"Mayer|Vietoris|excision|ferm|r[eé]union",
    6: r"Mayer|Vietoris|finitude|dimension finie",
    7: r"dominat|domin[eé]|homotopi|r[eé]tract",
    8: r"point|vide|contractile|axiome",
    9: r"somme|disjoint|coproduit",
    10: r"Euclid|euclid|sph[eè]re|boule|h[eé]misph",
    11: r"coquille|corrig|chi_c|chi_!|Euler",
    12: r"filtration|cellule|ferm[eé]|poly[eè]dr",
    13: r"K[uü]nneth|produit|homolog",
    14: r"K[uü]nneth|produit|support",
    15: r"fibration|multiplicativ|restriction|poly[eè]dr",
    16: r"spectrale|E_2|r[eé]serve|prouver",
    17: r"localement constant|syst[eè]me local|filtration",
    18: r"triangul|filtration finie",
    19: r"recouvrement|intersection|psi_1|psi_2|g_2",
    20: r"homolog|syst[eè]me local|homotopi|recouvrement",
    21: r"t[eé]lescop|coefficients locaux|syst[eè]me local|fibration",
    22: r"homolog|dual|syst[eè]me local",
    23: r"coniqu|c[oô]niqu|C_.*infty|E_.*infty",
    24: r"discret|coniqu|c[oô]niqu|compactifi",
    25: r"triangul|dimension.*trois|dimension.*3|Mo[iï]se",
    26: r"triangul|dimension.*quatre|dimension.*4|Mo[iï]se",
    27: r"ANR|contractil|finitude|coniqu|c[oô]niqu",
    28: r"compactifi|infini|supp.*compact",
    29: r"c[oô]ne|c[oô]niqu|tronqu|v[eé]rifi|bord",
    30: r"r[eé]tract|homotopi|c[oô]ne|v[eé]rifi",
    31: r"structure locale|infini|Mayer|Vietoris|chi_c",
    32: r"sph[eè]re|Euclid|euclid|bord|infini",
    33: r"coquille|compl[eé]ment|ferm|corrig",
    34: r"r[eé]union|Mayer|Vietoris|ferm",
    35: r"homotopi|hom[eé]omorph|support",
    36: r"uniqu|poly[eè]dr|axiom|cellul",
    37: r"j.ignore|restriction|fibration|poly[eè]dr",
    38: r"j.ignore|caract[eé]ris|uniqu|axiom",
    39: r"ANR|West|fini.*CW|uniqu|homotopi",
    40: r"corps|caract[eé]ristique|Euler|cellul",
    41: r"FINMON|C2-CP2|cat[eé]gor|poly[eè]dr|nerf",
    42: r"S20|Weil|Galois|orientation|Cartier|Gauss",
    43: r"D.E.S.U.R|administr|recycl|r[eé]emploi|typed|dactylo",
    44: r"recherche|enseignement|tiers|typed|dactylo",
    45: r"1976|budget|D.E.S.U.R|recycl|r[eé]emploi",
    46: r"Th[eé]venet|Daru|Bayonne|couverture|nom|adrese|adresse",
    47: r"Postnikov|lacets|loop|k.invariant|Omega Y",
    48: r"Postnikov|H\^3|invariant|annul",
    49: r"Postnikov|Eilenberg|MacLane|cohomolog|lacets",
    50: r"Postnikov|suspension|lacets|loop",
    51: r"Postnikov|double|suspension|Arlettaz",
    52: r"quadrati|crois[eé]|Postnikov|lacets|Baues|Conduch",
    53: r"stable|suspension|Postnikov|lacets",
    54: r"naturel|scind|Postnikov|produit|Baues",
    55: r"complexe|graphe|dimension.*1|coniqu|c[oô]niqu",
    56: r"triangul|dimension.*2|coniqu|c[oô]niqu",
    57: r"triangul|dimension.*2|compact",
    58: r"triangul|dimension.*3|Mo[iï]se|coniqu|c[oô]niqu",
    59: r"triangul|dimension.*4|Mo[iï]se|coniqu|c[oô]niqu",
    60: r"compacts rel[eè]vent|compact|axiome|Premi[eè]res conclusions",
}

# Types are deliberately the prompt's factual check-event vocabulary.
EVENTS = {
    1: ("used and rechecked in this run", "Frozen title/sequence compared with Hua V and earlier O01; source-layer identification only, not a mathematical proof."),
    2: ("used and rechecked in this run", "Singular/sheaf correction compared with Hua's convention; no unrestricted comparison theorem certified."),
    3: ("targeted proof check", "For the stated relative-singular definition of compact supports, K=X is final and gives Hc=H on compact X."),
    4: ("targeted proof check", "Alternating-sum and two-out-of-three argument checked conditional on existence of the closed/open long exact sequence."),
    5: ("used and rechecked in this run", "Hatcher's usual Mayer-Vietoris hypotheses checked against the sheet's closed-cover wording; arbitrary closed-cover validity not established."),
    6: ("targeted proof check", "Finite-total-dimension subquotient argument checked conditional on the Mayer-Vietoris sequence."),
    7: ("targeted proof check", "Cohomology retract establishes domination finiteness; point dominated by circle checks that equality requires the subsequent equivalence hypothesis."),
    8: ("targeted proof check", "Empty and point chain complexes check normalization; deleted contractibility wording is not treated as a refuted theorem."),
    9: ("targeted proof check", "Two-component direct-sum calculation checked for ordinary and compact-support cohomology."),
    10: ("targeted proof check", "Finite sphere/ball/Euclidean alternating-sum calculation checked in the CW/excisive setting, including n=0."),
    11: ("used and rechecked in this run", "Frozen ordinary chi line compared with earlier values and Hua's chi-c correction; no transcription edit."),
    12: ("targeted proof check", "Induction checked for a finite closed filtration with the specified cell strata and valid compact-support exact sequences."),
    13: ("targeted proof check", "Field Kunneth and cohomology-dual finite-dimensional implication checked; Kunneth theorem used as background."),
    14: ("targeted proof check", "Product of finite cell sums checked; general compact-support Kunneth hypotheses left explicit and unproved."),
    15: ("used and rechecked in this run", "Broad scan060 statement compared with scan066 restriction and Hua; narrowed conical question kept separate from EC21."),
    16: ("used and rechecked in this run", "E2 finiteness flag and local-system reduction traced in frozen text; no unjustified spectral-sequence finiteness asserted."),
    17: ("targeted proof check", "Rank-b local system is trivial on each Euclidean cell; finite closed-filtration additivity gives the restricted compact-support formula."),
    18: ("used and rechecked in this run", "Deletion/insertion compared with finite-filtration argument and Hua; no mathematical truth value inferred merely from deletion."),
    19: ("carried as background without fault found", "Proposed cover criterion recorded as unproved; cover labels differ from Hua and are not resolved mathematically."),
    20: ("targeted proof check", "Finite CW cellular-chain rank argument checks the refined ordinary local-system statement; not the unrestricted statement."),
    21: ("independent re-proof", "Explicit locally compact projective-space telescope and sphere cover constructed; rational and sign-local-system cohomology computed, giving chi(X)=chi(Y)=1 with two-point fibre."),
    22: ("used and rechecked in this run", "Homology-index correction and dual local-system annotation compared with Hua; dimensions shorthand remains frozen."),
    23: ("used and rechecked in this run", "Unresolved C/E link convention compared with Hua's consistent C interpretation; modern deductions explicitly conditional."),
    24: ("targeted proof check", "Infinite discrete space has infinite-dimensional H0 and a non-locally-contractible one-point compactification; this checks a notational consistency obstruction."),
    25: ("used and rechecked in this run", "Cancelled compact triangulation clause compared with Hua's stronger summary; no general conical triangulation theorem claimed."),
    26: ("carried as background without fault found", "Manolescu's dimension-four E8 nontriangulability statement and dimension-three Moise distinction checked in author source; underlying triangulation proofs not reproved."),
    27: ("targeted proof check", "Conditional finite-chart/local-contractibility reduction checked; ANR criterion and West compact ANR theorem imported, not reproved."),
    28: ("targeted proof check", "Deleting the compactification point gives finiteness and chi-c=chi(hat X)-1 conditional on the valid support exact sequence."),
    29: ("carried as background without fault found", "Conical closure of the truncated core remains flagged; local half-interval product issue identified, not silently proved."),
    30: ("targeted proof check", "Explicit radial homotopy r -> (1-t)r+t max(r,1/2), glued to identity, checks retraction for a genuine cone chart."),
    31: ("targeted proof check", "Mayer-Vietoris algebra and end-link defect identity checked conditional on the compact core and excisive decomposition."),
    32: ("targeted proof check", "Euclidean parity and collared-manifold core/boundary Euler calculations check the end-link interpretation in those cases."),
    33: ("used and rechecked in this run", "Complement-letter alternatives compared with scan056 and Hua; retained as a reading question without editing frozen text."),
    34: ("targeted proof check", "Circle with both closed subsets one point refutes the summary formula if the covering condition is omitted; refined EC05 retains it."),
    35: ("targeted proof check", "R and point are homotopy equivalent with compact-support Euler numbers -1 and 1; ordinary and proper/homeomorphism invariances distinguished."),
    36: ("targeted proof check", "Finite polyhedral-pair cell induction and compact-core reduction check restricted uniqueness, not arbitrary infinite triangulations."),
    37: ("carried as background without fault found", "Author's final-class fibration question retained open; earlier telescope countermodel expressly outside this class."),
    38: ("used and rechecked in this run", "Marginal global-uniqueness question and main existence wording compared with Hua footnote; no manuscript claim of main-theorem uniqueness inferred."),
    39: ("targeted proof check", "Conditional ANR/finite-CW compact-core uniqueness reduction checked; exact manuscript-category coverage and imported ANR/West theorems not certified."),
    40: ("targeted proof check", "Finite cell counts give field-independent integer Euler characteristic in the controlled range; broad class membership is not asserted field-independent."),
    41: ("targeted proof check", "Finite simplicial face-poset nerve identifies barycentric subdivision; no FINMON minimal-arrow bound or solution inferred."),
    42: ("used and rechecked in this run", "Theme list compared with Hua, O01, E26, and README S20; no unproved arithmetic bridge asserted."),
    43: ("used and rechecked in this run", "Six frozen reused_typed entries, headings, internal numerals, and encoded additions checked; no image or handwriting authentication."),
    44: ("used and rechecked in this run", "Administrative questions attributed to the unidentified typescript rather than automatically to Grothendieck; no external personal research."),
    45: ("computation or formal certificate", "Exact Python arithmetic verifies all six budget totals including 275+79=354; not a certificate of hand or date."),
    46: ("used and rechecked in this run", "Cover/name/address layer and absent page total checked against frozen text; uncertain identities left unresolved."),
    47: ("used and rechecked in this run", "Question-marked loop/Postnikov sketch compared with Hua VI; no proof or conclusion attributed to the sheet."),
    48: ("used and rechecked in this run", "Placement of question-marked equality and Hua's class reading distinguished from ambient-group reading."),
    49: ("computation or formal certificate", "Normalized C2 cochains with C2 coefficients exhaustively checked, yielding H3=C2; product of Eilenberg-MacLane spaces supplies the independent ambient-group counterexample."),
    50: ("used and rechecked in this run", "Arlettaz Lemma7.4 checked for cohomology-suspension relation; no second delooping inferred from one."),
    51: ("targeted proof check", "Arlettaz Proposition7.5/Theorem7.6 deduction checked with its imported low-degree K(A,3) homology facts; not an independent re-proof of those facts."),
    52: ("computation or formal certificate", "Free reduced quadratic module checked algebraically; finite quotient, action, kernel/cokernel, cocycle and all normalized coboundaries exhaustively checked. Baues-Conduche realization theorem separately imported, not machine-proved."),
    53: ("targeted proof check", "Logical extra-delooping requirement checked against EC50-51; tower is not inferred from one loop structure."),
    54: ("carried as background without fault found", "Baues-Conduche natural-splitting distinction checked in author preprint; no new independent proof of their nonnaturality theorem."),
    55: ("targeted proof check", "Under the explicit compact recursive-cone convention, finite zero-dimensional links give finite-valence graph charts; no unrestricted E1 identification claimed."),
    56: ("targeted proof check", "Cone over a finite graph is a finite two-dimensional polyhedron, checking only the local claim under EC55's convention."),
    57: ("carried as background without fault found", "Retained compact two-dimensional triangulation assertion recorded separately; no independent global triangulation proof completed."),
    58: ("carried as background without fault found", "Local three-dimensional assertion depends on compact triangulated two-dimensional links; arbitrary singular-link generality not certified by a manifold theorem."),
    59: ("carried as background without fault found", "Local four-dimensional assertion and dependency on compact three-dimensional links separated from the global four-manifold counterexample."),
    60: ("used and rechecked in this run", "Frozen compact-comparison citation to (b) compared with axiom (a) and Hua's corrected cross-reference; no transcription change."),
}

EXTRA_EVENTS = [
    ("93/060(g):ordinary-unrestricted", "refuted, with the refined statement's id", "EC21 refutes ordinary multiplicativity under cohomological finiteness alone; refined finite-CW/local-system range EC20 and later distinct conical question EC37."),
    ("93/062:ordinary-local-system-unrestricted", "refuted, with the refined statement's id", "EC21 sign local system refutes the unrestricted ordinary lemma; refined finite-CW statement EC20."),
    ("93/066(c):without-cover-condition", "refuted, with the refined statement's id", "EC34 refutes only the formula read without X=X' union X''; refined covering/excision statement EC05."),
    ("93/083:ambient-H3-vanishing-reading", "refuted, with the refined statement's id", "EC49 refutes this possible reading of the question, not an asserted manuscript theorem; refined class/group distinction EC48."),
    ("93/083:single-loop-k1-vanishing-reading", "refuted, with the refined statement's id", "EC52 algebra plus imported realization refutes this possible question's unrestricted affirmative answer; refined positive double-loop statement EC51."),
    ("EUL-S1", "used and rechecked in this run", "Author-hosted Hatcher text checked for Mayer-Vietoris hypotheses, mapping telescope, and local coefficients; background theorems not independently reproved wholesale."),
    ("EUL-S2", "used and rechecked in this run", "West Corollary5.3 statement and metric-space convention checked; West proof not independently reproved."),
    ("EUL-S3", "used and rechecked in this run", "Manolescu author exposition checked at dimension3/4 distinction; original Moise full text not retrieved."),
    ("EUL-S4", "used and rechecked in this run", "Arlettaz author survey Lemma7.4, Proposition7.5 and Theorem7.6 checked; original 1990 DOI target inaccessible."),
    ("EUL-S5", "used and rechecked in this run", "Baues-Conduche author preprint §§4.5-4.7 reduced-quadratic realization/looping and Theorem1.9 scope checked; those classification theorems imported."),
    ("MPL_93_002-046 O01", "carried as background without fault found", "Used as a topological-theme context pointer only; earlier orientation claims not re-proved here."),
    ("MPL_93_002-046 E26", "carried as background without fault found", "Used as a Cartier/arithmetic-theme context pointer only; no earlier Cartier theorem checked here."),
    ("MPL_93_002-046 §3", "carried as background without fault found", "Used as earlier reused-sheet census/method context only; its identifications not independently authenticated here."),
    ("FINMON C2-CP2", "carried as background without fault found", "Finite-category minimization question used as a limited thematic link; no bound or solution supplied."),
]


def main():
    assert set(QUERIES) == set(EVENTS) == set(range(1, 61))
    context_files = [
        "README.md", "notes/RESULTS_STATE.md", "hua_project/README.md",
        "same_cote_93/MPL_93_002-046_notes.md", "hua_project/93.modern.tex",
    ]
    with (RECORDS / "research_euler_context_search.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["statement_id", "context_file", "query_regex", "matching_line_count", "matching_line_numbers", "interpretation"])
        for note_id, query in QUERIES.items():
            pattern = re.compile(query, re.IGNORECASE)
            for name in context_files:
                lines = (CONTEXT / name).read_text(encoding="utf-8").splitlines()
                hits = [str(i) for i, line in enumerate(lines, 1) if pattern.search(line)]
                writer.writerow([f"EC{note_id:02d}", "context/" + name, query, len(hits), ",".join(hits) or "none",
                    "Targeted lexical context search; hits are leads, not proof or identity of claims. Exact comparison and result-state match/non-match are in research_euler.md."])
    with (RECORDS / "research_euler_events.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["statement_id", "date", "who", "type", "outcome"])
        for note_id, (kind, outcome) in EVENTS.items():
            writer.writerow([f"EC{note_id:02d}", DATE, WHO, kind, outcome])
        for statement, kind, outcome in EXTRA_EVENTS:
            writer.writerow([statement, DATE, WHO, kind, outcome])
    print("Wrote 300 note-by-context-file lexical searches and 74 honest check-event rows.")
    print("Only research_euler_context_search.tsv and research_euler_events.tsv were written.")


if __name__ == "__main__":
    main()
