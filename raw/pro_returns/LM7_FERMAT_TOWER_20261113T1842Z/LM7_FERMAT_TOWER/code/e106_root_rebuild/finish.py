"""Verify the refreshed frozen metadata and record the completed root audit."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / "research_e106"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
encode = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + "\n"

manifest_path = AUTHOR / "ledger/e_next_ordinary_manifest.json"
assert sha(manifest_path) == "173ea6ea1dfd39822b77ca2b777c4425ead419e8b2b1afa950289d8f645ec309"
manifest = read(manifest_path)
assert manifest["statement"] == "E.106"
assert len(manifest["files"]) == 36
checked = []
for row in manifest["files"]:
    p = AUTHOR / row["path"]
    assert p.stat().st_size == row["bytes"], row["path"]
    assert sha(p) == row["sha256"], row["path"]
    checked.append(row)

fresh = read(HERE / "comparison.json")
assert fresh["status"] == "PASS" and fresh["exit_code"] == 0
assert fresh["excluded_fields"] == []
for relative, digest in fresh["frozen_input_and_source_sha256"].items():
    assert sha(AUTHOR / relative) == digest, relative
    assert sha(HERE / relative) == digest, relative
for row in fresh["comparisons"]:
    assert row["entire_file_byte_identical"]
    assert (AUTHOR / row["path"]).read_bytes() == (HERE / row["path"]).read_bytes()

history = AUTHOR / "code/history"
assert sha(history / "e106_initial_prime_driver.out") == "885fdb263e4ad2b9d63eb01c085d526e056cb931be3f1525a13c911f32c90fbb"
assert (history / "e106_initial_prime_driver_arithmetic.out").read_bytes() == (history / "e106_initial_prime_driver_replay_arithmetic.out").read_bytes()
assert (history / "e106_initial_prime_driver_replay_arithmetic.out").read_bytes() == (AUTHOR / "code/e_next_prime_maps.out").read_bytes()
original = AUTHOR / "ledger/e106_original_author_freeze"
assert sha(original / "e_next_ordinary_manifest.json") == "572f4d16495de53b4cd506c4c9813e34706eac9039e13a71402f79e7e6e2349b"

proof_checks = [
    "The local norm/inclusion square fixes Gal(B3/B1)'s generator by its action on beta3, identifies Gal(B3/B2) with its third power, and divides the actual ninth-character matrix by three only after its restriction to E101's complete ordinary-unit norm lattice.",
    "The literal E94 row weights are retained. The six cubic characters have rank4, and the full 19683-residue calculation supplies both finite coordinate inverses and all243 preimages of every image.",
    "The ordinary FIELD-norm index81 is used in the ambiguous-class formula. E91's trivial vertical action then identifies the entire three-class group order243. Surjectivity of the actual ninth-genus quotient of that same order proves its isomorphism and W=0.",
    "The prime-above-three class is followed through actual ideal norms; the horizontal norm and extension maps yield Cl(L3){3}=C9+C3, q3=3a3, and capitulation kernel<3a3>. The unramified capitulation formula then proves the ordinary horizontal unit norm is onto.",
    "The two literal prime ideals over7 and73 are recomputed in the certified B1 field. Their Frobenii determine the claimed horizontal class coordinates, with all243 upper and81 lower coordinates checked.",
    "The six S-prime class columns and the displayed principal S-divisor lattice have exact mutually inverse coordinate maps. Earlier actual principal powers establish full principality and remove any dependence on only a three-saturated lattice.",
    "The vertical ordinary-unit obstruction is computed after the field-norm test using the exact strongly ambiguous class subgroup. The quotient and completed norm kernels follow with their actual torsion and free ranks.",
    "The result determines the finite projection exponent a3=1. It asserts no value for the eventual all-level exponent h and makes no deduction about later transvections from equality of adjacent finite class groups."
]
sources = [
    {
        "key": "E_MilneCFT",
        "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
        "root_read_scope": "III Proposition2.7 and the proved restriction/corestriction cup-product compatibility preceding Theorem3.1; III section4 Steps1--4 and Theorem4.4 with proof, printed pp.111--114; VII Proposition3.1 and its entire lattice/Herbrand proof through Lemmas3.2--3.5, printed pp.208--209; VIII Theorem3.1 and full Hasse-norm proof.",
        "fresh_remaining_passages": ["turn868view0", "turn868view1", "turn871view0"],
        "precision": "III Lemma3.2's missing printed proof and III3.3's proof warning are not counted as complete proofs. The local square uses the preceding proved cup-product compatibility."
    },
    {
        "key": "E_LemmermeyerAmbiguous",
        "url": "https://arxiv.org/pdf/1309.1071",
        "root_read_scope": "Theorem1, Proposition1, Lemma1 and the complete ideal/index derivation through section3.",
        "root_opened_references": ["turn862view1", "turn863view0", "turn863view4", "turn864view3"],
        "precision": "The unit Herbrand input is separately checked in Milne VII3.1. The Proposition1 surjectivity paragraph's Am_st/Am notation slip is addressed by the proof's explicit orbitwise Hilbert90 map."
    }
]
result = {
    "status": "PASS",
    "statement": "E.106",
    "complete_proof_read": True,
    "complete_final_Python_and_GP_sources_read": True,
    "proof_lines": 420,
    "proof_sha256": fresh["proof_sha256"],
    "author_manifest_sha256": sha(manifest_path),
    "checked_manifest_files": checked,
    "complete_fresh_rebuild": fresh,
    "proof_audit": proof_checks,
    "primary_source_checks": sources,
    "historical_output_provenance": "The unchanged exploratory wrapper's newly executed isolated stdout is explicitly a fresh replay. Its complete GP arithmetic stream agrees byte for byte with the retained original stream and final GP result. The pre-refresh author freeze source, manifest, status and stdout remain retained separately.",
    "mathematical_source_changes_required": [],
    "peer_review": "No separate peer review result has been received at this root audit; none is asserted.",
    "remaining_original_scope": "E.23 remains active: later ordinary layers and eventual h, unrestricted global ramification, and other-primary/mixed section problems remain outside this result."
}
(HERE / "audit.json").write_text(encode(result))
report = """# E106 complete root audit

**PASS.** The root auditor read the complete 420-line mathematical proof, the
complete final Python and GP programs, and the accompanying dependency and
source records. No mathematical correction was required.

The fresh copied reconstruction returned exit0. Its full Python stdout, JSON,
and GP stdout agree byte for byte with the frozen author files, with no excluded
fields. All six complete inputs and both mathematical sources were hashed before
and after execution. PARI recertified the retained B1 field and recomputed the
literal prime7/73 Frobenii. The root execution is `rebuild.py`, its actual stdout
is `rebuild.out`, and the complete comparison is `comparison.json`.

## Mathematical argument checked

"""
report += "\n".join(str(i + 1) + ". " + check for i, check in enumerate(proof_checks)) + "\n\n"
report += """## Primary-source checks

Milne's local cup-product compatibility, Hilbert-symbol definition and norm
criterion, complete unit Herbrand quotient proof, and complete cyclic Hasse norm
proof were read in the primary course notes. Lemmermeyer's ambiguous and strongly
ambiguous ideal-class arguments were read through their complete ideal/index
derivation. The exact sections and source limitations are recorded in `audit.json`.
The omitted printed local lemma proof and the notation slip in the ambiguous-class
article are recorded explicitly; the written E106 argument supplies the required
maps through the proved cup-product and orbitwise Hilbert90 constructions.

## Frozen metadata and historical stdout

The refreshed 36-file manifest was checked in full. It changes historical-output
provenance only: the mathematical proof, final programs, inputs and final outputs
retain their audited hashes. The unchanged exploratory wrapper was actually rerun
in an isolated copy. Its new stdout is labelled as a fresh replay, and its complete
arithmetic stream is byte-identical to the retained stream. The preceding author
freeze and manifest remain available. This audit's `finish.py` performs and records
these metadata checks; its actual stdout is `finish.out`.

No separate peer result is asserted. The eventual all-level exponent h and the
unrestricted portions of E.23 remain active.
"""
(HERE / "README.md").write_text(report)
print(encode({"status": "PASS", "statement": "E.106", "manifest_files": len(checked),
              "proof_sha256": fresh["proof_sha256"], "fresh_full_output_comparisons": len(fresh["comparisons"]),
              "excluded_fields": [], "audit_sha256": sha(HERE / "audit.json")}))
