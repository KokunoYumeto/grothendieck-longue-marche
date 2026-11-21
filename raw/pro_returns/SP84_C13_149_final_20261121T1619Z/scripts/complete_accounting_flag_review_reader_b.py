"""One-use favored-reading flag corrections from exact existing witness text.

No readings, evidence, historical rows, frozen inputs or audit changed counts
are changed.  A differing alternate reading does not by itself change the
adopted/favored reading against a witness.  Other witness flags remain intact.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

R = Path(__file__).resolve().parents[1]
DEST = R / 'documentation/accounting_flags_followup_reader_b.json'
assert not DEST.exists()
corrections = [
    (16, 'c13', 'against_C', 'C writes un peu affiné,; final favors affiné with différent as an alternative. The surrounding peu and comma are unchanged context.'),
    (17, 'c01', 'against_C', 'C already has deleted tentative ain. Adding un/une alternatives retains ain first; de and the following article/underline are unchanged context.'),
    (17, 'c04', 'against_C', 'C already has deleted tentative compatible. The final adds correspond as an alternative while retaining compatible first.'),
    (18, 'c02', 'against_C', 'C already has the Gamma superscript a/infinity. Adding can leaves a as the favored raised form; H still omits the cluster.'),
    (19, 'c04', 'against_C', 'C already writes ce topos, (le. The final adds en as an alternative to ce, retaining ce and the same comma/parenthesis context.'),
    (19, 'c19', 'against_C', 'C already has deleted tentative comme. Adding connexe/connexes retains comme first.'),
    (19, 'c20', 'against_C', 'C already writes pi_K not-equal pi_1(K), including the following comma. The final favors not-equal while allowing equality/simeq.'),
    (18, 'c08', 'against_H', 'H already has un-underlined pro-galoisiens. The final favors the same dash; the point alternative is uncertainty only. C still differs by underlining.'),
    (19, 'c01', 'against_H', 'H has deleted une. The outer and inner favored final alternatives still give deleted une; other letters and live-state alternatives do not alter that favored reading. C still gives live une.'),
]
reports = {n: json.loads((R / f'reviews/149_scan{n:03d}.json').read_text()) for n in (16, 17, 18, 19)}
before = copy.deepcopy(reports)
protected = {}
for n in reports:
    files = [R / f'pages/149_scan{n:03d}.tex'] + list((R / 'second').glob(f'149_scan{n:03d}_*'))
    for p in files:
        if p.is_file(): protected[str(p.relative_to(R))] = hashlib.sha256(p.read_bytes()).hexdigest()
edits = []
for n, cid, key, reason in corrections:
    index = next(i for i, x in enumerate(reports[n]['changes']) if x['id'] == cid)
    item = reports[n]['changes'][index]
    assert item[key] is True
    item[key] = False
    assert item['against_C'] or item['against_H'], 'These places still differ from the other witness.'
    edits.append(dict(scan=n, id=cid, path=['changes', index, key], before=True, after=False,
                      reason=reason, C=item['C'], H=item['H'], final=item['final']))
for n, report in reports.items():
    expected = copy.deepcopy(before[n])
    for item in edits:
        if item['scan'] == n:
            _, index, key = item['path']
            expected['changes'][index][key] = False
    assert report == expected
    (R / f'reviews/149_scan{n:03d}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert all(hashlib.sha256((R / p).read_bytes()).hexdigest() == h for p, h in protected.items())
log = dict(completed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           authorization='Root requested exact favored-reading accounting across all audits, preserving historical rows and audit changed counts.',
           edits=edits, counts_delta=dict(places=0, against_C=-7, against_H=-2, high=0, medium=0, low=0),
           protected_hashes=protected, protected_files_unchanged=True,
           historical_rows_and_audit_counts_unchanged=True,
           all_other_report_fields_unchanged=True,
           substantive_case_left_for_root='019c16 contains tentative inserted si, absent from C but not counted against it; root must choose a separate low-confidence omission row or broadened compound accounting.',
           excluded_candidates=['015c07 keeps C=true: current defini differs from accented C défini.',
                                '023c04 keeps C=true: the new low placement is a substantive placement correction.',
                                'Underline, insertion, deletion and punctuation departures remain substantive even when their letters agree.'])
DEST.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
md = ['# Follow-up favored-reading accounting\n', log['completed_utc'] + '\n',
      'Nine flags corrected from exact current/adjudicated readings and supplied witness text. No source reading, confidence, historical row, audit changed count or frozen file changed. These places still count against the other witness. Delta: C −7, H −2; places and confidence totals unchanged.\n']
for item in edits:
    md.append(f"## {item['scan']:03d}/{item['id']}\n\n`{'.'.join(map(str,item['path']))}`: `true` → `false`.\n\n{item['reason']}\n")
md.append('## Root judgment retained\n\n' + log['substantive_case_left_for_root'] + '\n')
DEST.with_suffix('.md').write_text('\n'.join(md))
print(json.dumps({'flag_edits': len(edits), 'delta': log['counts_delta'], 'protected_files_unchanged': True}))
