#!/usr/bin/env python3
"""Record completed root proof review, actual replays and final typing delta.

This records an already performed mathematical review. Hash checks and exact
comparisons below verify its scope; they do not infer that a proof was read.
"""
from pathlib import Path
import argparse
import hashlib
import json

P = argparse.ArgumentParser()
P.add_argument('--peer-sha256', required=True)
args = P.parse_args()
R = Path(__file__).resolve().parent.parent
A = R / 'research_e119_continuation'
HERE = Path(__file__).resolve().parent
OLD = A / 'audit/pre_final_typing/full_tree'
PEER = R / 'd_e121_audit'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
enc = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + '\n'
manifest_name = 'ledger/e_fiftythree_normalizer_manifest.json'
proof_name = 'sections/E_fiftythree_normalizer.tex'
old_manifest_sha = '0586bacfa58c080ddc4549c1eb845714978a50a56d8ac00f18b33aba80c78eb4'
new_manifest_sha = 'de04c68da8e09240a36074cd7dfb3d943d0759811cf6e842fe871b1e24625b1d'
old_proof_sha = '346bf38b90b23c80adb719ec24f158ea42bb0f1ef05b30ad342bd2a864f935b0'
new_proof_sha = '435bef02e897562e6651305bfee3da289e54235899c113027b1799a2e5a2fae0'
assert sha(A / manifest_name) == new_manifest_sha
assert sha(OLD / manifest_name) == old_manifest_sha
old_manifest, new_manifest = read(OLD / manifest_name), read(A / manifest_name)
assert len(old_manifest['files']) == 128 and len(new_manifest['files']) == 264
for folder, manifest in [(OLD, old_manifest), (A, new_manifest)]:
    for rel, entry in manifest['files'].items():
        p = folder / rel
        assert sha(p) == entry['sha256'], str(p)
        assert p.stat().st_size == entry['bytes'], str(p)
assert sha(OLD / proof_name) == old_proof_sha
assert sha(A / proof_name) == new_proof_sha
assert len((OLD / proof_name).read_text().splitlines()) == 555
assert len((A / proof_name).read_text().splitlines()) == 573
delta = read(A / 'audit/e121_final_typing.json')
assert delta['after_proof_sha256'] == new_proof_sha
assert sha(A / 'audit/e121_final_typing.diff') == delta['exact_diff_sha256']
unchanged = {}
for rel, entry in old_manifest['files'].items():
    p = Path(rel)
    if p.parts[0] in ('code', 'inputs') and p.name not in {
        'e53_normalizer_layout.py', 'e53_normalizer_layout.out',
        'e53_normalizer_layout.json', 'e53_normalizer_freeze.py',
        'e53_normalizer_freeze.out', 'e53_normalizer_freeze.err',
    }:
        assert sha(A / rel) == entry['sha256'], rel
        unchanged[rel] = entry['sha256']
for rel, expected in delta['unchanged_mathematical_files'].items():
    assert sha(A / rel) == sha(OLD / rel) == expected

replay = read(HERE / 'replay.json')
assert sha(HERE / 'replay.json') == '4f511f832d00f026a3b5c436d8db723c52f9f69202ba5b2f194c8400ccfb9bc6'
assert replay['status'] == 'PASS_ROOT_FIVE_STAGE_REPLAY'
assert replay['manifest_sha256'] == old_manifest_sha
assert replay['proof_sha256'] == old_proof_sha
assert len(replay['stages']) == 5 and all(x['exit_code'] == 0 for x in replay['stages'])
assert replay['python_exit_code'] == replay['binary_comparison_exit_code'] == 0
assert replay['excluded_fields'] == replay['excluded_binary_components'] == []
sources = {}
for rel, expected in replay['mathematical_source_hashes'].items():
    assert sha(A / rel) == expected
    sources[rel] = {'sha256': expected, 'lines': len((A / rel).read_text().splitlines())}
for rel, data in replay['text_outputs'].items():
    assert data['byte_identical']
    assert sha(A / rel) == sha(HERE / 'fresh' / rel) == data['sha256']
for rel, data in replay['binary_objects'].items():
    assert data['whole_decoded_GEN_identical'] and not data['raw_bytes_identical']
    assert sha(A / rel) == data['author_sha256']
    assert sha(HERE / 'fresh' / rel) == data['root_sha256']
assert sha(HERE / 'independent_maps.json') == 'daca2437a8f7f2e69d709280227e2e1ea6b02c05631a562be6bdc2486aa1f5bb'
finite = read(HERE / 'independent_maps.json')
assert finite['status'] == 'PASS_INDEPENDENT_FULL_FINITE_MAPS'
assert (HERE / 'independent_maps.json').read_bytes() == (HERE / 'independent_maps.out').read_bytes()

assert sha(PEER / 'audit.json') == args.peer_sha256
peer = read(PEER / 'audit.json')
assert peer['status'] == 'PASS_FULL_PROOF_SOURCE_AND_INDEPENDENT_MARKED_MAP_IDEAL_CHECKS'
assert sha(PEER / 'manifest.json') == 'f8c4de728ed465162bc9c93e5eb31fcf42cc0a700925c17cc1920c713807c530'
for rel, entry in read(PEER / 'manifest.json')['files'].items():
    assert sha(PEER / rel) == entry['sha256'], rel
    assert (PEER / rel).stat().st_size == entry['bytes'], rel
peer_hashes = {str(p.relative_to(PEER)): sha(p) for p in [
    PEER / 'audit.json', PEER / 'audit.md',
    PEER / 'code/d_e121_maps.py', PEER / 'code/d_e121_maps.out',
    PEER / 'code/d_e121_maps.json', PEER / 'code/d_e121_ideals.gp',
    PEER / 'code/d_e121_ideals.out', PEER / 'code/d_e121_ideals.json',
    PEER / 'code/d_e121_factor_sizes.gp',
    PEER / 'code/d_e121_factor_sizes.out',
]}
assert read(PEER / 'code/d_e121_maps.json')['status'] == 'PASS'
assert (PEER / 'code/d_e121_maps.json').read_bytes() == (PEER / 'code/d_e121_maps.out').read_bytes()
assert '"status":"PASS"' in (PEER / 'code/d_e121_ideals.out').read_text()

report = '''# Root E.121 proof and execution review

**PASS for the final frozen proof.** The root read the complete original
555-line proof, all six mathematical sources, and both final proof-only
amendments. The final proof has573 lines. Every original freeze file is
preserved, and the264-file final manifest has been verified exactly.

The full B2 class group follows from the actual normalizer action, the
ideal trace identity and the explicit finite nilpotence bound. The
horizontal unramified S-split class-field sequence, positive connecting
commutator and both norm/extension compositions determine the full L2
group and its marked basis ambiguity. The actual cyclic-nine and
normal-closure comparisons retain their full projection kernels and
positive Artin signs. The outside-S ideal/Hilbert90 construction proves
the unit-norm defect map in both directions, including its canonical
three-primary projection. All three completed norm kernel types use
the literal root-of-unity maps and finite-rank unit completion.

The two final amendments make the actual morphisms explicit. The
vertical extension sends b to3a for any actual norm lift a. The full
kernel is3A and9A=0, proving that choice independence. For every
completed unit kernel K, a basis of K/mu3 and chosen lifts give the
continuous product isomorphism from mu3 plus Z3^r; quotient coordinates
and division give its inverse. Basis and lift changes are specified.
The root checked both paragraphs. All mathematical sources, arithmetic
outputs and complete PARI objects remain byte-identical to the old
freeze; no arithmetic rerun is attributed to this text amendment.

Against the original128-file freeze, the root freshly ran all five new
GP stages and the exact Python checker from copied mathematical sources
and nine immutable E119 inputs. All seven complete text outputs agree
byte for byte. All seven whole decoded PARI GEN objects agree exactly,
with no excluded component. Their raw binary serialization bytes differ;
both hashes and the full object equality checks are retained. All
mathematical stages returned0. The binary-comparison stderr contains
only the retained PARI stack-allocation messages. Earlier E119 BNF
certifications were already reviewed and were not repeated here.

The root also wrote and executed an independent finite-map verifier
without importing author code or outputs. It exhausts the243 upper B
classes,81 upper L classes, both nine-element lower groups, all nine
displayed maps, every norm/extension square, trace, basis shear, positive
connecting class, unit defect quotient and compositum subgroup. Its
polynomial calculation verifies the stated nilpotence relation.

The separate peer independently checked the three full rational genus
coordinate maps, all finite ideal maps, and all26244 products in a
different coordinate model of the162-element normal-closure group.
Its own GP program checks12 actual S-prime images,14 full principal
ideal identities,732 embedded HNF columns, all seven literal S-units,
21 tame characters and seven wild characters. The root read its entire
243-line Python program and117-line GP program, diagnostic and full
outputs, and final audit. These peer executions are separately credited;
they are not described as additional root executions.

Primary-source review uses the complete Milne class-field, reciprocity,
unit-Herbrand and cyclic Hasse-norm passages already read for E119,
together with Lemmermeyer's full ideal/Hilbert90 proof. Root additionally
read the official PARI nfgaloisapply, idealprimedec and bnfisprincipal
contracts, including transformed-ideal HNF comparison and factored
principal generators. Milne's adjacent omitted proof is not claimed
as read or used. No upper BNF completeness claim enters this result.

The result evaluates this complete next positional53 transition.
Later positional norm systems and the full intrinsic section set in
original E.23 remain active through their stated exact comparison maps.
The author layout evidence is retained separately; the integrated paper
will receive its own complete visual review.
'''
(HERE / 'audit.md').write_text(report)
record = {
    'statement': 'E.121', 'status': 'PASS_ROOT_FULL_PROOF_SOURCES_REPLAY_AND_TYPING_DELTA',
    'proof_sha256': new_proof_sha, 'proof_lines_read': 573,
    'proof_read_scope': 'Complete original555 lines and both exact final morphism paragraphs.',
    'manifest_sha256': new_manifest_sha, 'final_frozen_files_checked': 264,
    'original_freeze_checked': {'manifest_sha256': old_manifest_sha, 'proof_sha256': old_proof_sha, 'files': 128},
    'mathematical_sources_read': sources,
    'mathematical_review': [
        'Actual lower trivial g-action and jN trace imply M contained in (3,T)M; T^9 in3R gives explicit (3,T)^(9e) annihilation and full B2 projection-kernel zero.',
        'The unramified S-split horizontal class-field sequence and positive E4-AH E4 class give the full L2 extension, order81, exponent9 and basis with sigma(a)=a+3u.',
        'All ideal norm/extension squares, trace identities and the three a-to-a+3ku coordinate transports preserve the stated matrices.',
        'The cyclic-nine genus, literal compositum fields, actual fixed subgroups and local Artin character identify the precise full quotient maps.',
        'The outside-S ideal/Hilbert90 map has both inverse directions and canonical three-primary projection; jN=3 eliminates the prime-to-three invariant quotient.',
        'Actual root norms and finite-rank completion give literal mu3 torsion and free ranks18,6,22; chosen quotient lifts give the full continuous kernel isomorphism and inverse.',
    ],
    'final_typing_delta': delta,
    'unchanged_original_code_and_input_files': unchanged,
    'root_replay': {
        'replay_json_sha256': sha(HERE / 'replay.json'),
        'freeze_at_execution': old_manifest_sha,
        'complete_GP_stages': 5, 'complete_Python_checker': 1,
        'complete_text_byte_equal': 7, 'complete_decoded_GEN_equal': 7,
        'raw_binary_byte_equal': 0, 'excluded_fields_or_components': [],
        'binary_comparison_stderr': (HERE / 'compare_binary.err').read_text(),
        'scope': replay['scope'],
    },
    'independent_root_maps': {
        'source_sha256': sha(HERE / 'independent_maps.py'),
        'stdout_json_sha256': sha(HERE / 'independent_maps.json'),
        'scope': finite['scope'], 'author_code_or_output_imported': False,
    },
    'peer_review': {
        'status': 'PASS', 'hashes_verified': peer_hashes,
        'root_read_scope': 'Complete final audit, complete243-line Python and117-line GP sources, diagnostic source and all their outputs; peer programs not rerun by root.',
        'final_peer_manifest_sha256': sha(PEER / 'manifest.json'),
    },
    'primary_source_scope': [
        'Milne CFT4.03 III2.7/3.1 cup-product Res/Cor proof; V3.3,3.6,Example3.9; V5.2 full product proof,5.3,5.5; VII3.1 full unit-lattice proof and7.1-3; VIII3.1 full cyclic Hasse-norm proof.',
        'Lemmermeyer1309.1071 all six pages, Theorem1, Proposition1 and full ideal/Hilbert90 argument; the actual outside-S map is proved in the paper.',
        'Official PARI nfgaloisapply read at turn1070view0/1 and local2.19.0 usersch3.tex22836-22880; idealprimedec21785-21827; bnfisprincipal20713-20784.',
    ],
    'omitted_proof_not_used': 'Milne III Lemma3.2 prints Proof. To be added; no read-proof or independent-use claim is made.',
    'unresolved_original_scope': 'Original E.23 later positional inverse norm systems, higher/intrinsic section comparisons and unrestricted section set remain active.',
    'layout_scope': 'Author seven-page render retained; integrated root visual review follows separately.',
    'audit_report_sha256': sha(HERE / 'audit.md'),
}
(HERE / 'audit.json').write_text(enc(record))
print(enc({'status': record['status'], 'audit_sha256': sha(HERE / 'audit.json'),
           'report_sha256': sha(HERE / 'audit.md'), 'final_files': 264,
           'unchanged_original_code_and_input_files': len(unchanged)}), end='')
