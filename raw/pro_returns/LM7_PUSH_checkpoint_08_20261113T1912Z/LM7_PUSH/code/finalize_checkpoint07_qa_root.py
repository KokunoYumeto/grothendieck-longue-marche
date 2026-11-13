#!/usr/bin/env python3
"""Record the actual root inspection of the clean fifth checkpoint-07 PDF."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / 'research/visual_qa.json'
qa = json.loads(path.read_text())
assert qa['pdf_sha256'] == sha256((ROOT / 'LM7_PUSH_paper.pdf').read_bytes()).hexdigest()
assert qa['page_count'] == 354 and len(qa['rendered_pages']) == 267
assert len(qa['contact_sheets']) == 15
log = (ROOT / 'build/LM7_PUSH_paper.log').read_text()
assert not any(word in log for word in ('Overfull', 'Warning', 'undefined'))
inspected = [124, 125, 188, 191, 193, 197, 199, 201, 203,
             314, 315, 316, 317, 318, 349, 354]
names = [row['file'] for row in qa['contact_sheets']]
names += [f'page_{page:03d}.png' for page in qa['rendered_pages']]
qa['visually_inspected'] = True
qa['inspected_contact_sheets'] = [row['file'] for row in qa['contact_sheets']]
qa['full_resolution_inspected_pages'] = inspected
qa['image_sha256'] = {name: sha256((ROOT / 'build/renders' / name).read_bytes()).hexdigest()
                      for name in names}
qa['inspection_basis'] = {'reader': 'root', 'build': 'checkpoint07_fifth_complete',
                          'all_contact_sheets_actually_viewed': True,
                          'full_resolution_pages_actually_viewed': inspected}
qa['inspection_notes'] = [
    'Root inspected all 267 rendered sample pages in all fifteen contact sheets.',
    'Sixteen listed pages were also inspected at full resolution, covering the exact Kummer sign and inversion comparison, D40--D43 proof displays, the E50 residual and signed comparison, its repaired filename paragraph, the open-task table and the final bibliography page.',
    'No clipped text, overlapping equation tags, broken matrices, footer collisions or margin overflow was observed.',
    'The exact fifth complete build has zero overfull boxes, zero warnings and no undefined references or citations; its active-source input manifest is verified.',
]
path.write_text(json.dumps(qa, indent=2) + '\n')
(ROOT / 'research/checkpoint07_visual_qa.json').write_text(json.dumps(qa, indent=2) + '\n')
report = ROOT / 'research/report_body.md'
body = report.read_text()
assert 'Checkpoint 07 preserves' not in body
body += '''

Checkpoint 07 preserves the completed Parts A, B, C and F and adds the
accepted results D.40--D.43 and E.50. Its verified 354-page PDF contains
185 numbered statements: 171 Proved, 7 Refuted, 3 Known and 4 Open, with
all 29 lead and task rows. D.1, D.2, E.2 and E.3 remain unresolved.
The exact double-cover and generator-inversion maps in D.5 correct the
earlier Kummer-sign sentence: in the displayed positive-root convention,
c2(f_sigma) = kappa2(sigma), whereas the retained negative distribution
coordinate is -c2. The finite distribution equations and the arithmetic
matrices remain unchanged; their dependencies are recorded in
`research/BC_kummer_two_sign_audit.md` and the prior passages are preserved.

The first checkpoint-07 build completed cleanly before the final new
integrations. The second pass failed at a two-column alignment inside a
single-alignment environment; the third failed at a proof-opening paragraph
command. Both exact sources and failure logs are preserved. The fourth pass
completed with one 20.49881-pt filename overflow. The fifth complete build
repairs that line and has zero overfull boxes, zero warnings, no undefined
references or citations, and verified active-source input hashes.

Root inspected all 267 sampled pages in fifteen contact sheets and sixteen
pages at full resolution. These include the revised D.5 sign proof, the new
coprime-cover arguments, the prime-five signed modular and residual maps,
the repaired filename paragraph, the remaining-question table and the
bibliography. No clipping, tag overlap, broken matrix, footer collision or
margin overflow was observed. The exact page lists and image hashes are
retained in `research/checkpoint07_visual_qa.json`. The current PDF SHA-256 is
`d01782f3bd1c0cb9f2d20815c45bd1c26555e9885ff90bbfc023da2db4069a2a`.

The D.44 full pro-ell pair comparison, E.48 full A6 source and E.51
prime-seven source and targets are retained as separate drafts outside
this checkpoint's compiled register. Their proof reviews and certificate
manifests are retained. Root's complete E.48 and E.51 certificate replays
are in progress at the snapshot; their partial logs are explicitly
unfinished and do not certify completion. The new joint A6/double-cover
and cyclic outer-five chief investigations also continue separately.
All earlier checkpoint archives, all five checkpoint-07 build snapshots,
superseded passages, failed attempts and executed certificate outputs are
preserved. This archive records active work; the unresolved tasks continue.
'''
report.write_text(body)
with (ROOT / 'research/root_searches_02.md').open('a') as stream:
    stream.write('''

112. Root inspected the fifth complete checkpoint-07 PDF: all 267 sampled
     pages in fifteen contact sheets and sixteen listed pages at full
     resolution. The D5 correction, D40--43 displays, E50 signed/residual
     maps and repaired prefix, open-task table and bibliography are clean.
     Zero overfull boxes, warnings or undefined references/citations remain.
     The exact current PDF hash and image hashes are recorded in
     research/checkpoint07_visual_qa.json.

113. Root began isolated complete replays from the frozen E48 and E51
     manifests. E48's full source chain already passed all 865049 final
     Schreier checks and every original-word DAG value. E51's model,
     compressed source, subgroup, projective comparison, residual and signed
     common-source computations all compare exactly; the final target
     replay is still running. Full completion is recorded only by the
     corresponding audit JSON with all_passed=true. D44's new centerless
     pullback, full pro-ell pair and invariant leading-term construction
     passed root and geometry proof reviews; its explicit peripheral
     permutation justification was added with the prior fragment preserved.
''')
(ROOT / 'research/checkpoint07_pending_outputs.json').write_text(json.dumps({
    'scope': 'Unfinished work at checkpoint preparation; no completion inferred.',
    'compiled_register_excludes': ['D.44', 'E.48', 'E.51'],
    'active_root_audits': ['code/audit_a6_full_chains_root.out',
                           'code/audit_symplectic_five_p7_root.out'],
    'separate_active_agent_work': ['de_a6_gl_*', 'D45 cyclic outer-five chief'],
    'completion_rule': 'Use only the corresponding final audit JSON with all_passed=true.'
}, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'page_count': qa['page_count'],
                  'rendered_pages': len(qa['rendered_pages']),
                  'contact_sheets': len(qa['contact_sheets']),
                  'full_resolution_pages': len(inspected),
                  'pdf_sha256': qa['pdf_sha256']}, indent=2))
