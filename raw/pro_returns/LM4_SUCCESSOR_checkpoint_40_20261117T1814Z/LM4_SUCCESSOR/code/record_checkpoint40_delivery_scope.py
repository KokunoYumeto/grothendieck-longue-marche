"""Record exact superseded derivatives without removing any local file."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parents[1]
FIRST = ROOT.parent / '.checkpoint39_stage_ie3483cd'
SECOND = ROOT.parent / '.checkpoint39_stage_revision_9gl459jj'
FINAL_PDF = 'LM4_SUCCESSOR_paper.pdf'
CSV_PATH = 'records/checkpoint40_approved_derivative_omissions.csv'


def binding(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_39.zip').exists()
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_40.zip').exists()
    prior = json.loads((FIRST / 'snapshot.json').read_text())
    original = {r['path']: r for r in prior['logical_rows_before_generated']}
    images = sorted((ROOT / 'records/pdf_qa/checkpoint39_final').glob('*.png'))
    failed = ROOT / 'records/pdf_qa/checkpoint39_before_path_wrap/LM4_SUCCESSOR_paper.pdf'
    assert len(images) == 58 and sum(p.stat().st_size for p in images) == 15018260
    assert failed.stat().st_size == 5035739
    omitted = {p.relative_to(ROOT).as_posix() for p in images + [failed]}
    assert len(omitted) == 59 and FINAL_PDF not in omitted
    counts = []
    for rel in ['records/checkpoint_version_retention.csv', 'records/checkpoint39_frozen38_entry_map.csv']:
        count = 0
        with (ROOT / rel).open(newline='') as f:
            for row in csv.DictReader(f):
                for key in ['retained_path', 'original_path']:
                    path = row[key]
                    if path.startswith('LM4_SUCCESSOR/'):
                        path = path[len('LM4_SUCCESSOR/'):]
                    assert path not in omitted, (rel, key, path)
                assert not row.get('omission_reason')
                count += 1
        counts.append(count)
    assert counts == [196804, 12502]
    rows = []
    for p in images + [failed]:
        rel = p.relative_to(ROOT).as_posix()
        actual = binding(p)
        assert actual == {k: original[rel][k] for k in ['bytes', 'sha256']}
        is_image = p.suffix == '.png'
        rows.append({'path': rel, **actual,
                     'reason': ('Regenerable page/contact preview; the final vector PDF supersedes this delivery copy. Its render manifest and completed visual-review evidence remain.' if is_image else 'Superseded failed-layout PDF with four overflowing provenance paths; the final corrected PDF contains the same mathematics. Failed source, diffs and build logs remain.'),
                     'superseded_by': FINAL_PDF,
                     'regeneration_recipe': ('code/render_checkpoint39_pdf.py; records/pdf_qa/checkpoint39_final/render_manifest.json; render into a fresh output directory using the retained final PDF.' if is_image else 'For the failed layout, use retained before_path_wrap source copies and build logs. Rebuilding need not reproduce PDF timestamps or metadata byte-for-byte.')})
    with (ROOT / CSV_PATH).open('x', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['path','bytes','sha256','reason','superseded_by','regeneration_recipe'])
        w.writeheader(); w.writerows(rows)
    for source, target in [('checkpoint39_revision_prepare.out','checkpoint39_second_prepare_run.out'),
                           ('checkpoint39_revision_prepare.err','checkpoint39_second_prepare_run.err')]:
        with (ROOT / 'records' / target).open('xb') as f:
            f.write((ROOT.parent / source).read_bytes())
    second = json.loads((SECOND / 'sealed-plan.json').read_text())
    assert second['result'] == 'FAIL_EXACT_CAP' and second['layout']['exact_zip_bytes'] == 548237023
    record = {'result':'PASS_EXACT_APPROVED_CURRENT_DERIVATIVES_ONLY',
              'recorded_at':datetime.now(timezone.utc).isoformat(),
              'approved_omissions':59, 'omitted_bytes':sum(r['bytes'] for r in rows),
              'historical_identity_rows_checked':counts, 'historical_omissions':0,
              'omissions_csv':{'path':CSV_PATH, **binding(ROOT / CSV_PATH)},
              'final_pdf':{'path':FINAL_PDF, **binding(ROOT / FINAL_PDF)},
              'second_prepare':{'session_id':90963,'initial_chunk':'852b4c','completion_chunk':'5e4aee',
                                'actual_exit_code':1,'complete_outer_outputs_read':'3c3414',
                                'exact_bytes':548237023,'plan':binding(SECOND / 'sealed-plan.json')},
              'checkpoint39_zip_created':False, 'local_files_deleted':0,
              'checkpoint40_open_not_before':'2026-11-17T19:49:30+00:00',
              'checkpoint40_open_before':'2026-11-17T20:49:30+00:00',
              'archive_cap_bytes':536870912, 'future_success_claimed':False}
    with (ROOT / 'records/checkpoint40_delivery_scope.json').open('x') as f:
        json.dump(record,f,indent=2); f.write('\n')
    text = 'INCOMPLETE\n\n# Final delivery report addendum\n\n'
    text += 'This file and LM4_SUCCESSOR_report.md together form the final report. The research remains incomplete: both main problems and the original coherent-class/CM-parity question remain open. The paper remains the reviewed 762-page, 401-statement version.\n\n'
    text += '| Register | Proved | Refuted | Open | Known | Total |\n|---|---:|---:|---:|---:|---:|\n| Numbered statements | 357 | 19 | 19 | 6 | 401 |\n| Original task/lead rows | 15 | 3 | 30 | 1 | 49 |\n\n'
    text += '## Preparation outcomes\n\nThe two checkpoint 39 preparations actually ended with exit 1 at their size gates: 547,320,902 bytes and 548,237,023 bytes, against the unchanged 536,870,912-byte limit. Neither opened a ZIP. Their streams, complete outputs, source reviews and failed plans are preserved. The final archive is assigned checkpoint 40 in the next hourly slot; the expired checkpoint 39 opening guard is not changed. Mathematical exploration remains stopped.\n\n'
    text += '## Explicit derivative omissions and replacements\n\nOnly the following 59 newly generated checkpoint 39 diagnostic files are omitted from the final archive. None occurs as an original or retained path in any of the 196,804 verified historical identities or 12,502 recovered frozen-checkpoint 38 identities. Historical omissions remain zero. The current final PDF, all mathematical sources, all code, the render manifest, visual-review records, and failed-layout source/diffs/logs remain included. Local copies and the failed preparation streams are not deleted.\n\n'
    text += 'The 58 PNG page/contact previews are superseded for delivery by LM4_SUCCESSOR_paper.pdf. The retained render program and manifest document their regeneration and the actual inspection. Regeneration on a different renderer version is not claimed to be byte-identical. The failed-layout PDF is superseded by the corrected final PDF; its failed sources and complete build evidence remain. Exact sizes, SHA-256 hashes and per-file regeneration notes are in records/checkpoint40_approved_derivative_omissions.csv.\n\n'
    text += '| Omitted path | Bytes | Superseding file | Reason |\n|---|---:|---|---|\n'
    for row in rows:
        reason = 'Regenerable preview; render/review evidence retained.' if row['path'].endswith('.png') else 'Failed provenance-path layout; corrected PDF and failed source/logs retained.'
        text += f"| {row['path']} | {row['bytes']} | {FINAL_PDF} | {reason} |\n"
    text += '\n## Restoration and evidence timing\n\nThe current final manifest and packaging record use checkpoint_40 names. Earlier checkpoint_39 and checkpoint_38 records are historical evidence. The unchanged three TAR extraction commands restore the logical files; open LM4_SUCCESSOR/LM4_SUCCESSOR_paper.pdf afterward. Preparation, the exclusive ZIP opening, closed-archive verification and saving remain separate gates. Postseal observations cannot be inserted retroactively into the sealed archive; the final response reports their actual outcomes.\n'
    with (ROOT / 'LM4_SUCCESSOR_final_delivery_report.md').open('x') as f:
        f.write(text)
    print(json.dumps(record,indent=2))


if __name__ == '__main__':
    main()
