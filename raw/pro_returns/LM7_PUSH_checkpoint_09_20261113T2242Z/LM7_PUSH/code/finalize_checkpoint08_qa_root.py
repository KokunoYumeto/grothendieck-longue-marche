#!/usr/bin/env python3
"""Record completed visual review, exact image reuse, and checkpoint scope."""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

prior = json.loads((ROOT / 'research/checkpoint08_ninth_visual_qa.json').read_text())
qa = json.loads((ROOT / 'research/visual_qa.json').read_text())
assert qa['pdf_sha256'] == digest(ROOT / 'LM7_PUSH_paper.pdf')
assert qa['page_count'] == 448
names = list(prior['image_sha256'])
hashes = {n: digest(ROOT / 'build/renders' / n) for n in names}
changed = sorted(n for n in names if hashes[n] != prior['image_sha256'][n])
assert changed == ['contact_sheet_20.png', 'page_441.png', 'page_442.png', 'page_443.png']
qa['rendered_pages'] = prior['rendered_pages']
qa['inspected_contact_sheets'] = prior['inspected_contact_sheets']
qa['full_resolution_inspected_pages'] = prior['full_resolution_inspected_pages']
qa['freshly_inspected_contact_sheets'] = ['contact_sheet_20.png']
qa['freshly_inspected_full_resolution_pages'] = [441, 442, 443]
qa['prior_actual_inspection_record'] = 'research/checkpoint08_ninth_visual_qa.json'
qa['byte_identical_previous_images'] = [n for n in names if n not in changed]
qa['image_sha256'] = hashes
qa['visually_inspected'] = True
qa['approved_for_delivery'] = True
qa['inspection_notes'] = [
    'Root actually inspected the final contact sheet 20 and all three changed coverage pages at full resolution after the completed build and completed render process exits.',
    'Every other sampled image is byte-identical to an actually inspected ninth-build image. That record carries the explicit seventh-build image comparison for unchanged proof pages.',
    '367 sampled pages are covered by twenty contact sheets and seven additional full-resolution views; forty-one distinct pages have full-resolution inspection.',
    'The new E58 proof, updated D1/D2/E2/E3 statements, repaired D49 display, E54-E57 pages, coverage continuation rows and final bibliography are included.',
    'No clipping, overlapping formula tags, broken matrices, footer collision, or margin overflow is observed in the final images.',
    'The rejected seventh-build coverage images and premature tenth-build render remain explicitly preserved with their failure records.'
]
log = (ROOT / 'build/LM7_PUSH_paper.log').read_text()
assert not re.search(r'Warning|Overfull|undefined', log)
qa['current_log']['warnings'] = 0
assert qa['current_log']['overfull_boxes'] == 0
for name in ['research/visual_qa.json', 'research/checkpoint08_visual_qa.json']:
    path = ROOT / name
    if name.endswith('checkpoint08_visual_qa.json'):
        assert not path.exists()
    path.write_text(json.dumps(qa, indent=2) + '\n')

body_path = ROOT / 'research/report_body.md'
before = body_path.read_text()
after = before.replace('Checkpoint08 third compilation completed390 pages',
                       'Checkpoint08 third compilation completed391 pages')
assert before != after
repair = ROOT / 'research/checkpoint08_report_pagecount_correction.json'
assert not repair.exists()
repair.write_text(json.dumps({'reason': 'The final preserved third-build log records 391 pages; the preliminary report note said 390.',
                             'before': before, 'after_before_final_append': after}, indent=2) + '\n')
after += '''

## Checkpoint 08: accepted results and final verification

This checkpoint contains 203 numbered statements: 192 Proved, 7 Refuted,
3 Known and 1 Open, with all 29 lead and task rows. Parts A, B, C, D and F
and Tasks E.1--E.2 are complete. E.3 is the remaining open task. The full
weight-five special image has dimension 3 and the weight-nine gentle image
has dimension 2 for every prime at least 5. E.58 constructs a full gentle
element with CM bits (1,0), retains its exact peripheral frames, and proves
the failure of the original twelve-representative equivalence. The complete
proof reviews, source programs, outputs and isolated replays are retained.

The checkpoint-08 build history is preserved without deletion:

| Attempt | Recorded result |
|---|---|
| First | 367 pages; no overfull boxes or warnings. |
| Second | Failed at E.48 alignment and line-break syntax; its exact source and failure logs are retained. |
| Third | 391 pages; two filename overflows, 13.74924 and 10.26797 pt. The earlier preliminary report count of 390 is corrected from the final log, with its complete prior text preserved. |
| Fourth | 405 pages; no overfull boxes or warnings. |
| Fifth | 420 pages; one 14.47926-pt overflow in D.49.5, repaired by splitting its exact definition and group law. |
| Sixth | 444 pages; no overfull boxes, one legacy binomial warning and six bookmark warnings. |
| Seventh | 444 pages; clean log, but the actual rendered coverage rows collided with the footer on pages 437 and 438. This delivery candidate was rejected. |
| Eighth | 444 pages; bounded continuation rows preserve every character of the task text and repair the coverage collision. |
| Ninth | 448 pages; E.58 integrated, clean log. Full-resolution review found missing word/number spaces in the coverage text. |
| Tenth, confirmed | 448 pages; nine missing spaces inserted, with every non-whitespace source character unchanged. Zero overfull boxes, zero warnings, no undefined references or citations. |

One tenth-build snapshot was requested before process completion had been
observed. Its directory name does not certify a completed build; the timing
correction is stored inside that snapshot. A render launched during the
same interval showed blank final thumbnails and was rejected and preserved.
After the build returned success, the complete build was saved separately
as `build/checkpoint08_tenth_confirmed`, and the entire sample was rendered
again. Only that confirmed result supplies the final inspection below.

The final PDF is 448 pages and 3133961 bytes, with SHA-256
`cd48e108d98987071ac649aeb9fb3d6445ecdfff3e3c59a5f1f94805d1ad0005`.
Every active TeX source and the bibliography match the recorded build-input
hashes. The final register contains 86 active TeX sources and 57 bibliography
entries. Root inspected the distributed 367-page sample through twenty
contact sheets and seven additional page views; 41 distinct pages were
inspected at full resolution. Unchanged prior images are carried only after
literal PNG byte equality. The final three changed coverage pages and their
contact sheet were viewed again. The inspection records identify every
page, its exact image hash, and the previous actual-view record used.
No clipping, formula-tag overlap, broken matrix, footer collision or margin
overflow was observed in the final result.

The 3.A6 model construction and its isolated root replay are complete, but
the new central-kernel correction computation remains outside the accepted
statement register. The SL2(F3) Ferrari source and its whole finite correction
fibres are also under review. Their current programs, completed outputs,
failed or interrupted attempts and partial logs are retained as pending
work. The higher-genus relation comparison is active; no new full-GT
conclusion is certified from these unfinished routes. The pending-work
record is `research/checkpoint08_pending_outputs.json`.

Every earlier checkpoint archive, every preserved build attempt, all
superseded mathematical passages and recorded failed programs remain in
this archive. Regenerable successful render images and Python caches are
omitted; their generating programs, exact image hashes and actual inspection
records are retained. Rejected visual examples are retained explicitly.
This checkpoint preserves the completed results while E.3 continues.
'''
body_path.write_text(after)

pending = {
    'compiled_register_scope': '203 statements through E58; E3 only Open.',
    'SL2_F3': {'status': 'Complete 512-element correction enumeration above 24 retained G6 points reported; full generation checks and independent root audit pending.',
              'reserved_statement': 'E.59', 'prefix': 'code/a_cm_sl23'},
    'triple_A6': {'status': 'Complete finite cover/target models independently replayed by root. Rank79 source kernel replay reported complete; rank27 central coinvariant comparison and full CM correction fibres in progress.',
                 'reserved_statement': 'E.60', 'prefix': 'code/de_a6_triple'},
    'genus_one': {'status': 'Exact NS/BBR sewing relation and actual Ferrari projections under investigation; no full GT extension asserted.'},
    'partial_outputs': 'Files outside the accepted statement dependencies may be active or interrupted snapshots. Their presence is not a proof-status assertion.',
}
(ROOT / 'research/checkpoint08_pending_outputs.json').write_text(json.dumps(pending, indent=2) + '\n')
ledger_path = ROOT / 'research/root_searches_02.md'
ledger = ledger_path.read_text()
assert '\n138.' not in ledger
ledger += '''

138. Fresh primary-source check: Goto--Ishii, arXiv:2610.21052v1,
     https://arxiv.org/pdf/2610.21052, Introduction and Theorem 1.1
     (= Corollary 5.5), read directly (turn550view0, reopened turn559view1).
     Its formula evaluates elliptic Soule characters on local reciprocity
     images, for split primes p at least 5 and the stated positive index
     pairs. The checked source domain is the specified local Galois image.
     No full-GT comparison is inferred from that formula.

139. Nakamura--Tsunogai, Harmonic equations, RIMS1267 (2002),197--208,
     primary PDF 1267-18.pdf reopened (turn550view1). Theorems1--2 on
     printed199 state the harmonic/equianharmonic identities for G_Q.
     The full-GT accessory cocycles and the specified Galois equations
     retain their actual domains. This read supplies no proved transfer
     of those equations to every full-GT element.

140. Basualdo Bonatto--Robertson, arXiv:2606.01466v2 (8 October 2026),
     https://arxiv.org/pdf/2606.01466, primary PDF opened by root
     (turn559view0; exact proposition/theorem searches turn560view0--3).
     Proposition4.7 identifies the genus-zero object-fixing endomorphisms
     with the GT monoid. Definition4.8 imposes the two NS relations;
     Theorem4.9 maps that specified submonoid into the full modular-operad
     endomorphisms and proves compatibility with the genus-zero restriction.
     Its genus-one sewing verification invokes NS Claim8.3 relation6AS.
     The exact finite consequence of this relation is being investigated;
     no extension of the stated domain is used in the accepted manuscript.
'''
ledger_path.write_text(ledger)
before_inputs = json.loads((ROOT / 'build/source_input_manifest.json').read_text())
result = subprocess.run(['python3', 'code/assemble_register.py'], cwd=ROOT,
                        text=True, capture_output=True, check=True)
(ROOT / 'code/assemble_checkpoint08_final_qa.out').write_text(result.stdout)
assert all(digest(ROOT / name) == value for name, value in before_inputs['source_sha256'].items())
rows = list(csv.DictReader((ROOT / 'LM7_PUSH_results.csv').open()))
assert len(rows) == 203
assert [r['id'] for r in rows if r['status'] == 'Open'] == ['E.3']
assert len(qa['rendered_pages']) == 367
assert len(qa['full_resolution_inspected_pages']) == 41
print(json.dumps({'pdf_sha256': qa['pdf_sha256'], 'pages': 448,
                  'sample_pages': 367, 'full_resolution_pages': 41,
                  'status_counts': dict(collections.Counter(r['status'] for r in rows)),
                  'active_sources_unchanged_after_report_assembly': True}, indent=2))
