#!/usr/bin/env python3
"""Freeze E.94's proof, actual outputs, exact maps and remaining scope."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
LED = ROOT / "ledger"
LED.mkdir(exist_ok=True)

def write(name, value):
    (LED / name).write_text(json.dumps(value, indent=2) + "\n")

tex = ROOT / "sections/E_mu27_comparison.tex"
body = tex.read_text()
assert len(re.findall(r"(?<!\\)\\\[", body)) == len(re.findall(r"(?<!\\)\\\]", body)) == 20
assert len(re.findall(r"\\tag\{E94\.\d+\}", body)) == 20
assert body.count(r"\begin{statement}{E.94}{Proved}") == 1
assert not any(ord(c) < 32 and c not in "\n\t" for c in body)
certificate = json.loads((ROOT / "code/e_mu27_comparison.json").read_text())
summary = certificate["summary"]
assert summary["status"] == "PASS"
assert summary["structured_records"] == 91
assert summary["exact_Smith_systems"] == 10
assert summary["ordinary_coordinate_cases"] == 2187
assert summary["normalizer_group_cases"] == 243
assert summary["relative_ordinary_orders"] == [9,9,9,3]
assert summary["relative_S_orders"] == [9,3]

write("e_mu27_comparison_results.json", [{
    "id": "E.94",
    "status": "Proved",
    "statement": "For the actual degree486 field E=B3(mu27), evaluate its maximal ordinary and S-split three-genus fields over F=B1, their relative quotients A=C9^3+C3 and A_S=C9+C3, and all displayed local, prime, norm, extension and normalizer maps. The actual ordinary norm A to E91's A9 is onto with kernel C3^2; genuine ideal extension factors through A9 and satisfies JN=NJ=3. The actual S-genus norm to Cl_S(B3)=C3 is -x modulo3. G acts as identity and H as [[1,3],[2,1]] on A_S. Thus the actual Cl_S(E) deck coinvariants have a noncyclic quotient, proving failure of cyclicity over the cubic deck group ring.",
    "where_proved": "sections/E_mu27_comparison.tex, E94.1--20 and full proof; code/e_mu27_local.gp, e_mu27_genus.gp, e_mu27_export.gp, e_mu27_comparison.py and their retained actual outputs and complete certificates.",
    "depends_on": ["E.69","E.72","E.76","E.79","E.86","E.88","E.91","E_MilneCFT","E_PARICertifiedUnits"],
    "manuscript_passages": ["LM section51.16, folios733v--736v, scans172--178, through the actual positional norm and prime-class maps of E46,E69,E72,E88."],
    "depends_on_doubtful_reading": False,
    "notes": "The full class groups of E and the eventual exponent h are not evaluated. The E91 residual transvection is killed by the actual genus extension map, so this comparison does not decide its value. Author six-stage fresh rebuild session77324 exited0. All initial failed programs and their actual outputs are retained."
}])
write("e_mu27_comparison_coverage.json", {
    "statement": "E.94",
    "addresses": [{
        "task": "Part E(c),(d), Item2/Lead3 via the actual positional norm quotient H",
        "status": "Proved arithmetic refinement",
        "exact_maps": "E/B3 local ideal norm and extension; normalizer restriction; maximal ordinary and S-genus Artin quotients; the exact S-prime removal map; norm and genuine extension to the old ninth-genus quotient; the coherent prime73 S-class norm."
    }],
    "remaining": [
        "The full ordinary and S-class groups of E, beyond the evaluated maximal abelian-over-F genus quotients.",
        "The actual value of E91's transvection in W and its original prime-order consequence.",
        "The exact eventual exponent h and a coherent minimal-valuation three-unit.",
        "The intrinsic higher-quotient lifting questions retained in E23."
    ]
})
write("e_mu27_comparison_source_evidence.json", {
    "statement": "E.94",
    "sources": [{
        "key": "E_MilneCFT",
        "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
        "opened_passages": [
            "III Theorem3.1: the proved local Tate-pairing construction and restriction/corestriction compatibility, retained in E76/E79 and freshly checked by root with E91.",
            "III Theorem3.4: actual local Artin map and finite norm-kernel identification.",
            "V Proposition3.3, Theorem3.6 and Example3.9, printed pp157--159/PDF pp165--167: actual norm/Frobenius square, class-field existence, and the modulus1 Hilbert class field. Opened in turn790view0.",
            "V Proposition5.2 and its complete proof, printed p178/PDF186; Theorem5.3, printed pp178--179/PDF186--187; the reciprocal cyclotomic map and Summary5.10, printed pp181--182/PDF189--190. Opened in turn799view0.",
            "VIII Theorem7.4 and its complete Chebotarev proof through line16289, printed pp259--260/PDF267--268. Opened in turn790view1."
        ],
        "usage": "The local characters are actual Artin characters with the arithmetic-Frobenius/inverse-unit sign fixed. The finite ray quotient is identified with its maximal field through full local norm subgroups. Ordinary and S-class norm surjectivity is proved by the actual Hilbert-class-field intersection and Frobenius map.",
        "source_precision": "III Lemma3.2 has an unfinished printed proof. No assertion that its printed proof is complete is made; the compatibility used here follows from the proved Tate-pairing restriction/corestriction construction in III Theorem3.1. V Theorem5.3's proof is in ChapterVII, previously read with the class-field argument."
    },{
        "key": "E_PARICertifiedUnits",
        "source": "Official PARI2.19.0 manual, research_e52/vendor/pari-2.19.0/doc/usersch3.tex",
        "usage": "bnfcertify with default flag0 and return value1, actual ideal ray coordinates and Galois matrices, residue-field computations, exact integral HNF/Smith transformations."
    }],
    "internal_primary_arithmetic": [
        "E76 certified degree18 B1, exact local ninth-power norm characters and original ninth-genus ray quotient.",
        "E86 actual all-level S-class norm bases and literal g/h automorphisms.",
        "E91 actual old A9 coordinates, six prime columns, exact residual W and normalizer restriction."
    ],
    "certificate": "code/e_mu27_comparison.json, all91 structured export records and the complete exact transformation/inverse matrices.",
    "independent_audit": "Requested from root and a_structure after this freeze; no independent PASS is asserted yet."
})
write("e_mu27_comparison_computation_status.json", {
    "author_rebuild": {
        "session_id": 77324, "exit_code": 0, "stages": 6,
        "command": "python research_e94/code/e_mu27_comparison.py --gp research_e52/vendor/pari-2.19.0/gp",
        "output": "code/e_mu27_comparison.out",
        "summary": summary
    },
    "retained_attempts": [
        {"source": "code/e_mu27_local_nonunit_attempt.gp", "output": "code/e_mu27_local_nonunit_attempt.out", "outcome": "Stopped at the explicit check that a constructed norm was not a unit at a wild prime. No norm-kernel conclusion was drawn."},
        {"source": "code/e_mu27_local_rank_attempt.gp", "output": "code/e_mu27_local_rank_attempt.out", "outcome": "The first unit-norm spanning family had insufficient modulo-three rank. The corrected actual norms of Y and 1+(1-Y)^k have the proved full rank."},
        {"source": "code/e_mu27_genus_basis_attempt.gp", "output": "code/e_mu27_genus_basis_attempt.out", "outcome": "Stopped at the original-genus restriction check because the ray bases were different. The final computation constructs the exact basis map by evaluating actual ideals."},
        {"source": "code/e_mu27_comparison_inclusion_attempt.py", "output": "code/e_mu27_comparison_inclusion_attempt.out", "outcome": "A verifier assertion used the reversed lattice inclusion. The correct integral matrix is H_S inverse times H, and the full fresh reconstruction verifies it."},
        {"source": "code/e_mu27_comparison_json_attempt.py", "output": "code/e_mu27_comparison_json_attempt.out", "outcome": "The mathematical checks completed, then JSON rejected SymPy Integer. The final exporter explicitly converts exact integers and the entire fresh reconstruction passes."},
        {"source": "code/e_mu27_freeze_count_attempt.py", "output": "code/e_mu27_freeze_count_attempt.out", "outcome": "The first metadata lint counted the array row-spacing command as a display opening. The corrected lexer excludes an already escaped backslash. The theorem had all20 opening and closing display delimiters."},
        {"source": "code/e_mu27_small_coordinates.py", "output": "code/e_mu27_small_coordinates.out", "outcome": "Successful exact extraction of the displayed small group matrices from the complete retained certificate."}
    ],
    "existing_long_BNF_sessions": [
        {"session_id": 24024, "source": "research_prime17/first_layers.gp", "created_utc": "2026-11-13 05:59:47.616539 UTC", "last_poll_utc": "2026-11-13 14:40:54 UTC", "status_at_last_actual_poll": "Running, no new output."},
        {"session_id": 40565, "source": "research_prime17/layer2_reduced.gp", "created_utc": "2026-11-13 06:54:11.574697 UTC", "last_poll_utc": "2026-11-13 14:40:54 UTC", "status_at_last_actual_poll": "Running, no new output."}
    ],
    "no_duplicate_BNF_started": True
})
(LED / "e_mu27_comparison_refs.bib").write_text(
    "% E94 uses existing verified keys E_MilneCFT and E_PARICertifiedUnits.\n"
    "% verified: precise opened passages and proof usage are in e_mu27_comparison_source_evidence.json.\n"
    "% No duplicate bibliography keys are introduced.\n"
)
(LED / "e_mu27_comparison_report.md").write_text("""# E.94: the actual mu27 comparison

The next cyclotomic base change E=B3(mu27), of degree486 over Q,
has an explicitly evaluated maximal ordinary genus quotient
C9^3 plus C3 and S-genus quotient C9 plus C3. These are actual
quotients of the corresponding upper class groups; no full upper
class group is assigned from the calculation.

The proof gives every field inclusion and restriction. E/B3 is
totally ramified at each prime over3 and unramified inert at each
prime over17. The actual norm and extension coefficients are therefore
(1,1,1,3,3,3) and (3,3,3,1,1,1), respectively.
The ordinary and S-class norms are onto, proved by the Hilbert
class field intersection and actual Frobenius maps.

The actual automorphisms G,H have orders27,9 and satisfy
HGH^-1=G^4. G does not preserve B3: its exact conjugate of the
cubic deck generator is G^-9 H^3. The original g2,h2 are the
restrictions of G^3,H. Their actions on the new genus quotients,
including every coordinate inverse, are retained.

The two local norm characters at each wild prime have joint
quotient C9 plus C3. A literal eleven-column norm family proves the
entire new cyclotomic unit-norm kernel. Its index is justified by
local class field theory. The original insufficient norm family
and its actual failure output are retained. The arithmetic sign of
the cyclotomic character is fixed by the inverse-unit Artin action,
including the exact values on beta1 and 1+beta1.

The ordinary genus norm onto E91's A9 has kernel C3^2. The actual
ideal extension kills E91's residual transvection, so it factors
through A9. Both compositions are multiplication by3. The six
prime columns independently verify all residue and ramification
coefficients. This explicit map explains why the new genus
calculation does not decide that old transvection or the exponent h.

On the new relative S-genus group, G is identity and H has matrix
[[1,3],[2,1]], with row moduli9,3. The actual norm to the original
coherent prime73 C3 is -x modulo3. The upper deck coinvariants thus
surject onto C9 plus C3. A cyclic module over the cubic deck group
ring would have cyclic coinvariants, so this actual quotient proves
that the former cyclic-module premise fails for this base change.

## Exact reconstruction

    python research_e94/code/e_mu27_comparison.py --gp research_e52/vendor/pari-2.19.0/gp

The portable driver also works in the final flat code directory.
It uses the three already retained E76 dependencies
e_basechange_field.gp, e_basechange_ninth_norms.gp and
e_basechange_ninth_genus.gp, then the three owned local/genus/export
stages. It starts only the certified degree18 B1 calculation.
The six-stage author reconstruction77324 exited0.

All91 structured records, ten full Smith systems with integral
inverse maps, 2187 relative ordinary coordinates,27 relative S
coordinates,243 normalizer elements and the actual prime maps pass.
The actual local/genus BIN objects and certified B1 BNF are retained.
Five failed attempts and their literal stdout are included; no
missing successful output has been invented.

## Remaining arithmetic

The full upper ordinary/S-class groups, the old residual
transvection, and the limiting exponent h remain unevaluated.
E94 supplies an exact field and class-map comparison and an evaluated
noncyclic quotient. It does not infer principality or nonprincipality
from an unsuccessful element search, nor a stabilization assertion
from a finite level.

The two original expensive L2 BNF jobs were actually polled at
14:40 UTC and remained running without new output. No duplicate
BNF computation was started.
""")
dependencies = {}
for name in ["e_basechange_field.gp","e_basechange_ninth_norms.gp","e_basechange_ninth_genus.gp"]:
    choices = [ROOT / "code" / name, ROOT.parent / "research_e76/code" / name]
    p = next(p for p in choices if p.exists())
    dependencies[name] = {
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "bytes": p.stat().st_size,
        "purpose": "Exact E76 dependency for the six-stage portable rebuild."
    }
write("e_mu27_comparison_dependencies.json", dependencies)
manifest = {}
for p in sorted(ROOT.rglob("*")):
    if not p.is_file() or p.name in {"e_mu27_comparison_manifest.json","e_mu27_freeze.out"}:
        continue
    manifest[str(p.relative_to(ROOT))] = {
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "bytes": p.stat().st_size
    }
write("e_mu27_comparison_manifest.json", manifest)
print("PASS: E94 full proof, six-stage reconstruction, exact maps, retained attempts and scope.")
for p in [tex, ROOT/"code/e_mu27_comparison.py", ROOT/"code/e_mu27_comparison.json", LED/"e_mu27_comparison_manifest.json"]:
    print(p.name, hashlib.sha256(p.read_bytes()).hexdigest())
