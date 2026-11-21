"""One-use implementation of the three final checklist fixes approved by root.

No page text, meaningful reading, frozen input, adjudication, or count changes.
The archived012 builder is preserved byte for byte; its active duplicate is
guarded before any import or executable historical statement.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import subprocess
import sys

R = Path(__file__).resolve().parents[1]
LOG = R / 'documentation/checklist_metadata_fixes_reader_b.json'
assert not LOG.exists()
reports = {n: json.loads((R / f'reviews/149_scan{n:03d}.json').read_text()) for n in (16, 22, 25)}
original = copy.deepcopy(reports)
active = R / 'scripts/write_reader_c_scan012.py'
archive = R / 'documentation/first_reader_working_files/write_reader_c_scan012.py'
original_builder = active.read_bytes()
assert original_builder == archive.read_bytes()
protected = {}
for n in (12, 16, 22, 25):
    for p in [R / f'pages/149_scan{n:03d}.tex'] + list((R / 'second').glob(f'149_scan{n:03d}_*')):
        if p.is_file(): protected[str(p.relative_to(R))] = hashlib.sha256(p.read_bytes()).hexdigest()
for p in (archive, R / 'reviews/149_scan012.json', R / 'reviews/149_scan012.tex'):
    protected[str(p.relative_to(R))] = hashlib.sha256(p.read_bytes()).hexdigest()

assert not any('dc.' in x['form'] for x in reports[16]['abbreviations'])
reports[16]['abbreviations'].append(dict(
    form='dc. (uncertain alternative)', expansion='donc (tentative)',
    place=r'Main paragraph, Il en \unsure{sera|dc.} en particulier; sera remains the favored reading'))
assert reports[22]['abbreviations'][0]['form'] == 't.f.'
reports[22]['abbreviations'][0] = dict(
    form=r'\unsure{t.f.|v.f.}',
    expansion='type fini if t.f. is written; v.f. remains unexpanded',
    place='opening theorem; the abbreviated form remains uncertain')
c02 = next(x for x in reports[25]['changes'] if x['id'] == 'c02')
assert c02['final'] == "``ext. d'une V.A. par un tore''"
assert not any(x['written'] == 'paired raised short quotation strokes' for x in reports[25]['notation'])
reports[25]['notation'].append(dict(
    written='paired raised short quotation strokes', rendering=c02['final'],
    meaning='double quotation marks around the stated generalized-Jacobian type',
    evidence=('Existing approved c02 evidence: ' + c02['evidence'] +
              ' The retained independent-audit b05 decision also identifies paired raised short ticks at both ends. '
              'Evidence: crops/149_scan025_c02.png and crops/149_scan025_second_b05.png, original rectangle (280,340,1630,550). No new scan inspection was made for this notation entry.')))

readme_path = R / 'README.md'
before_readme = readme_path.read_text()
anchor = 'Fields that preserve the first-pass audit targets, and the separate first/second TSVs, retain their original historical readings; adjudications and correction logs explain subsequent changes.'
assert before_readme.count(anchor) == 1
sentence = (' Adjudication final-reading strings and changed-box counts describe the audit-time decisions. '
            'Later documented presentation amendments can update current page/report rendering without changing those historical strings or counts; the amendment logs identify their exact scope.')
after_readme = before_readme.replace(anchor, anchor + sentence, 1)
pointer = (' The active duplicate `scripts/write_reader_c_scan012.py` is deliberately disabled before its historical body can run or be imported; '
           'its byte-original source is preserved at `documentation/first_reader_working_files/write_reader_c_scan012.py`.')
anchor2 = 'these are historical working files, not a recipe to overwrite frozen readings.'
assert after_readme.count(anchor2) == 1
after_readme = after_readme.replace(anchor2, anchor2 + pointer, 1)

guard = (
    '# Historical first-reader builder: deliberately disabled in the current edition.\n'
    '# The byte-original source is preserved at\n'
    '# documentation/first_reader_working_files/write_reader_c_scan012.py.\n'
    '# This guard precedes every original import and write; direct use and import both stop.\n'
    'raise RuntimeError("Historical scan012 builder disabled: do not rerun over the edition. "\n'
    '                   "See documentation/first_reader_working_files/write_reader_c_scan012.py "\n'
    '                   "for the byte-original historical source.")\n\n'
).encode()
active.write_bytes(guard + original_builder)
for n, r in reports.items():
    expected = copy.deepcopy(original[n])
    field = 'notation' if n == 25 else 'abbreviations'
    expected[field] = r[field]
    assert r == expected
    (R / f'reviews/149_scan{n:03d}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
readme_path.write_text(after_readme)

# Meaningful guard checks: the previous script would overwrite012 immediately.
direct = subprocess.run([sys.executable, '-B', str(active)], capture_output=True, text=True)
assert direct.returncode != 0 and 'Historical scan012 builder disabled' in direct.stderr
import_code = ('import importlib.util; '
               f's=importlib.util.spec_from_file_location("historical012", {str(active)!r}); '
               'm=importlib.util.module_from_spec(s); s.loader.exec_module(m)')
imported = subprocess.run([sys.executable, '-B', '-c', import_code], capture_output=True, text=True)
assert imported.returncode != 0 and 'Historical scan012 builder disabled' in imported.stderr
assert all(hashlib.sha256((R / p).read_bytes()).hexdigest() == h for p, h in protected.items())
assert active.read_bytes()[len(guard):] == archive.read_bytes() == original_builder

edits = []
for n in reports:
    field = 'notation' if n == 25 else 'abbreviations'
    edits.append(dict(file=f'reviews/149_scan{n:03d}.json', field=field,
                      before=original[n][field], after=reports[n][field]))
log = dict(completed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           authorization='Root approved exactly the remaining abbreviation alternatives, one025 quotation notation entry, the012 active-builder guard, and a README presentation-amendment sentence.',
           metadata_edits=edits,
           readme=dict(before=before_readme, after=after_readme),
           active_builder=dict(file=str(active.relative_to(R)), prefix_added=guard.decode(),
                               original_body_preserved=True,
                               before_sha256=hashlib.sha256(original_builder).hexdigest(),
                               after_sha256=hashlib.sha256(active.read_bytes()).hexdigest()),
           archived_original=dict(file=str(archive.relative_to(R)),
                                  sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), unchanged=True),
           guard_checks=dict(direct_execution='blocked before historical body', import_execution='blocked before historical body',
                             original012_proposal_and_report_unchanged=True),
           protected_hashes=protected, protected_files_unchanged=True,
           meaningful_readings_pages_counts_and_audits_unchanged=True,
           no_new_image_reading=True, no_assembly=True)
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
LOG.with_suffix('.md').write_text(
    '# Final checklist metadata fixes — reader B\n\n' + log['completed_utc'] + '\n\n'
    'Applied the three root-approved minimal fixes:016 dc. is listed as an uncertain alternative with tentative donc;022 records the complete t.f./v.f. form with conditional type fini and no expansion for v.f.;025 has one paired-quotation-stroke notation entry grounded in already approved c02/b05 evidence.\n\n'
    'The active012 builder now raises before any original statement can execute, both directly and on import. Both guard checks passed, and012’s proposal/report were unchanged. The original body remains intact after the guard, and the separate archived file is byte-original. README points to that archive and distinguishes later documented presentation amendments from audit-time final strings and counts.\n\n'
    'Exact prior and current metadata, README text, guard prefix, hashes and verification results are in the JSON log. No page, meaningful reading, confidence/count, frozen comparison file or adjudication changed. No image work or aggregate assembly was performed.\n')
print(json.dumps({'metadata_reports': [16, 22, 25], 'guard_checks':2,
                  'archived_original_unchanged':True,
                  'protected_files_unchanged':True, 'no_assembly':True}))
