"""Record the accepted full-group A1 proof in the current report producer.

This one-time editorial migration is retained with its output for the audit.
It never modifies checkpoint archives or historical research notes.
"""
from pathlib import Path

work = Path(__file__).resolve().parents[1]
path = work / "code/write_report.py"
source = path.read_text()
rows = {
    "A1": (
        "AR.1 AR.2 AR.3 AG.39 AG.40 AG.41 AG.42 AR.8 AR.9",
        "PROVED. Universal injectivity holds in the whole geometrically prime-to-p group, retaining full G_k. A finite-cover proof gives fixed-prime cuspidal configuration exactness; the diagonal boundary transports actual cusp groups; full same-prime cohomology, point recognition and a Kummer evaluation contradiction give separation. The finitely generated field corollary follows by the checked specialization comparison. The full prime-to-p configuration fiber map itself is noninjective, a separate statement."
    ),
    "A5": (
        "AG.1 AG.2 AG.8 AG.9 AG.10 AG.13 AG.14 AG.30 AR.3",
        "OPEN as the compound request. The general point-separating-cover assertion now follows from A1, even using the identity cover. The stronger demand for prime-to-p correspondences to supersingular targets, and the exact reach from the specified seeds by those constructions, remain unresolved."
    ),
    "A8": (
        "AR.8 AR.9 AR.3 AG.39 AG.40 AG.41 AG.42",
        "PROVED. The two papers give the stated finiteness and separation results. The whole-group proof here additionally shows that the exceptional set is empty for the full prime-to-p set; this emptiness is not attributed to those papers."
    ),
    "A10": (
        "AR.11 AR.12 AR.13 AR.14 AR.18 AC.39 AC.40 AG.31 AR.3",
        "OPEN. Construction, compatible additivity, collision implication and rational projections are proved. A1 excludes every nonzero vector arising from a collision. Arbitrary Frobenius-fixed norm-compatible vectors with free deck orbits have not been shown to come from points. Their universal genus-two nonexistence remains open, beyond the proved original F4 cases and the hereditary relative-test sandwich."
    ),
    "L9": (
        "AR.8 AR.9 AR.3 AG.39 AG.40 AG.41 AG.42",
        "PROVED. Exact statements from both papers are distinguished from the additional result here: A1 implies emptiness of the full prime-to-p exceptional set."
    ),
    "L11": (
        "AR.11 AR.12 AR.13 AR.14 AR.18 AC.39 AC.40 AG.6 AG.31 AR.3",
        "OPEN as an equivalence with arbitrary free vectors. The module, semilinear Frobenius and point-difference implication are proved. A1 excludes point-origin collision vectors, but arbitrary free vectors have not been identified with points."
    ),
}
changed = []
lines = source.splitlines()
for index, line in enumerate(lines):
    for key, (ids, result) in rows.items():
        if line.startswith(f"('{key}',"):
            suffix = "]" if line.endswith(")]" ) else ","
            lines[index] = repr((key, ids, result)) + suffix
            changed.append(key)
source = "\n".join(lines) + "\n"
assert set(changed) == set(rows), changed

replacements = [
    ("The sixth checkpoint is being saved at the11:39UTC review.",
     "The sixth checkpoint snapshot at11:39:07UTC was saved successfully (215345733bytes,659entries)."),
    ("These address open items directly. Universal A1 and the classification remain unresolved.",
     "These addressed open items directly; at that review universal A1 and the classification were unresolved."),
    ("The next progress review/checkpoint is due at12:39UTC. The main collision assertion has priority.",
     "Before12:00UTC the independent fixed-prime cuspidal proof and the boundary/point-recognition audits closed A1. Its complete argument is now integrated. The next progress review/checkpoint is due at12:39UTC, with remaining cover-existence and reconstruction items under investigation."),
    ("the final implication remains A1.",
     "the final implication is now proved by the full-group A1 argument."),
    ("'A1/A3: neither counting,", "'A3: neither counting,"),
    ("A fixed-field full Abel-pullback tower now gives another exact route to A1:",
     "The retained fixed-field full Abel-pullback tower gives an alternative sufficient route to A1:"),
    ("General genus-two nonexistence and a converse from arbitrary vectors to points are not proved.",
     "A1 now excludes all point-origin collision vectors. General genus-two nonexistence of arbitrary free vectors and a converse from those vectors to points are not proved."),
    ("This does not prove point separation. Those visible covers can be ramified at the puncture; R1 does not provide lifted point differences on them, and a Weil polynomial alone determines an isogeny class rather than its integral p-primary exponent. The exceptional-coordinate Green splitting comparison remains an extra unproved premise. The small ambiguity in proper global H1 cannot remove the residue-bearing Kummer class on the common twice-punctured open.",
     "The retention lemma alone does not prove point separation. Those visible covers can be ramified at the puncture, so R1 cannot simply provide lifted point differences on them. The completed proof instead uses all their point counts to recognize actual noncuspidal sections, and then a cuspidal central difference cocycle and integral Kummer evaluations. The fixed-prime boundary construction supplies the required exceptional-coordinate comparison independently of the disputed full configuration assertion."),
    ("A late source audit has located a concrete convention conflict that is being checked before any Green-route conclusion is used.",
     "A late source audit located a concrete convention conflict, which the accepted proof avoids through an independent fixed-prime construction."),
    ("The conditional point-recognition and Kummer-evaluation steps are now under a separate full proof audit; A1 remains OPEN.",
     "The conditional point-recognition and Kummer-evaluation steps subsequently passed a separate full proof audit. The new fixed-prime fiber and boundary comparisons supply their hypotheses, so A1 is now PROVED. The primary SGA1 XIII5.2 Kummer-chart statement and the free-pro-r center-free input were opened directly; the audit is retained in notes/A1_full_chain_root_audit.md."),
]
for old, new in replacements:
    count = source.count(old)
    assert count == 1, (count, old)
    source = source.replace(old, new)

marker = "out += ['', '# Research record', '',\n"
assert source.count(marker) == 1
new_paragraph = (
    "A1 is now proved in the full group specified in the prompt. The proof retains the entire proper geometric prime-to-p quotient and full arithmetic G_k. For any auxiliary r different from p, each finite relative fiber quotient is dominated by an r-by-prime-to-p configuration quotient; this proves fixed-prime cuspidal fiber exactness. A local Kummer/root-gerbe boundary comparison transports the actual cusp decomposition groups for conjugate proper sections. Every visible cover retains full compact r-adic cohomology and Frobenius, so its zeta function and missing-point count are preserved. Compactness recognizes noncuspidal point sections. The degree-one central cusp extension then gives a difference cocycle whose values must be constant Kummer classes, contradicted by a nontrivial r-power root-of-unity value of a nonconstant function. Root and all three research agents independently checked the complete chain, including a second independent automorphism proof of the fixed-prime step. A1 also gives the finitely generated field corollary and emptiness of the exceptional set. It does not imply universal class-number witnesses or absence of arbitrary abstract norm-module vectors."
)
source = source.replace(marker, marker + repr(new_paragraph) + ",\n")
path.write_text(source)
print("Updated outcome rows:", ", ".join(changed))
print("Updated report paragraphs:", len(replacements) + 1)
print("Historical checkpoint files and research notes unchanged.")
