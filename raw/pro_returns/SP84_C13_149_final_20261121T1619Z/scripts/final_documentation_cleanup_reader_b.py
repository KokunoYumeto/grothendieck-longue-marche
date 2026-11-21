"""One-use root-approved final documentation and019c16 accounting cleanup.

No page, frozen reading, adjudication or notation decision is modified.  Only
the introductions of existing aggregate Markdown are synchronized here; the
complete aggregate rebuild remains a separate final root step.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import copy
import csv
import hashlib
import importlib.util
import json

R = Path(__file__).resolve().parents[1]
LOG = R / 'documentation/final_documentation_cleanup_reader_b.json'
assert not LOG.exists()
files = ['README.md', 'scripts/assemble.py', 'notation_current.md',
         'SP84_C13_149_notes.md', 'reviews/149_scan013.json',
         'reviews/149_scan019.json', 'reviews/149_scan021.json']
before = {p: (R / p).read_text() for p in files}
protected = {}
for n in (13, 19, 21):
    for p in [R / f'pages/149_scan{n:03d}.tex'] + list((R / 'second').glob(f'149_scan{n:03d}_*')):
        if p.is_file(): protected[str(p.relative_to(R))] = hashlib.sha256(p.read_bytes()).hexdigest()
reports = {n: json.loads(before[f'reviews/149_scan{n:03d}.json']) for n in (13, 19, 21)}
original_reports = copy.deepcopy(reports)

# Existing source/adjudication evidence settles accounting, not a new reading.
r = reports[19]
i = next(i for i, x in enumerate(r['changes']) if x['id'] == 'c16')
c16 = r['changes'][i]
assert c16['against_C'] is False and c16['confidence'] == 'high'
with (R / 'second/149_scan019_adjudications.tsv').open() as stream:
    adjud = next(x for x in csv.DictReader(stream, delimiter='\t') if x['box'] == 'b16')
assert r'\unsure{si}' in adjud['final_reading']
assert r'\unsure{si}' not in c16['C'] and r'\unsure{si}' in c16['final']
c16.update(against_C=True, confidence='low', crop=adjud['crop'],
           box=list(ast.literal_eval(adjud['pixel_box'])),
           evidence=('Root’s recorded b16 adjudication: ' + adjud['evidence'] +
                     ' This single insertion place accounts for two witness departures: C omits the favored but uncertain si, while H does not mark the raised phrase as an insertion. Confidence is low for the compound reading because si remains tentative. The current flags and confidence supersede the first-draft accounting; the source page and frozen adjudication are unchanged.'))

reports[13]['notes'][2] += (' The parenthesis written as \\unsure{sauf|s.f.} erreur is the author’s own qualification of the assertion that the relations are equalities; its exact wording remains uncertain. It is not an editorial reservation added to the source.')
reports[21]['notes'][0] += (' The inserted sauf erreur before the proposed strengthening is the author’s own qualification, separately from the later parenthesized sauf erreur accompanying the injectivity claim. Both are retained as source statements, not added editorial caveats.')

readme = before['README.md']
old = '**Work in progress.** The statements below describe the intended completed edition. The exact pages already finalized and audited are recorded in progress.log; unfinished reader proposals remain in reviews/.'
new = 'The authoritative current transcription is in `pages/`. Completion times, independent-audit status, checkpoints and any recorded final freeze are documented in `progress.log` and the per-page JSON records. Historical drafts are retained separately as evidence of the reading process.'
assert old in readme
readme = readme.replace(old, new, 1)
readme = readme.replace('The final reading follows visible ink', 'The adopted reading follows visible ink', 1)
old = '- `reviews/`: per-page proposed readings and structured evidence, including main-reader approval records.'
new = '- `reviews/*.json`: current structured readings, decisions, doubts, metadata and accounting, together with identified historical first-pass evidence and approval/audit records.\n- `reviews/*.tex`: archived first-reader proposals; these are historical working texts and are not the current transcription or either supplied witness.'
assert old in readme
readme = readme.replace(old, new, 1)
old = 'The provisional `notation_current.md`, `legibility_note.md`, and `feedback_addendum.md` support the assembled reports. They are retained as documentation. The full-size halves are reproducible and are excluded, as are the original attachments and previous checkpoint ZIPs.'
new = ('## Current text and historical records\n\n'
       '`pages/149_scanNNN.tex` is the authority for the adopted page text. The combined transcription is generated from those page files in ascending scan order. Current report fields such as final readings, decisions, doubts, notes, inventory and witness-accounting flags are synchronized with the adopted text. Fields that preserve the first-pass audit targets, and the separate first/second TSVs, retain their original historical readings; adjudications and correction logs explain subsequent changes.\n\n'
       'The archived `reviews/*.tex` proposals may differ from both the current pages and the supplied C/H comparison drafts. They must not be substituted for `pages/` or treated as a new witness. `documentation/first_reader_working_files/` preserves earlier scripts and coordinate metadata for provenance; these are historical working files, not a recipe to overwrite frozen readings. The supplied source scans and witness texts remain outside this edition archive and are identified by `source_manifest.json`.\n\n'
       '`notation_current.md`, `legibility_note.md`, and `feedback_addendum.md` support the assembled reports. Cross-page notation review is documented separately in `documentation/notation_review.md`; repeated forms do not by themselves remove a local doubt. The full-size halves are reproducible and are excluded, as are original attachments and previous checkpoint ZIPs.')
assert old in readme
readme = readme.replace(old, new, 1)

assembly = before['scripts/assemble.py']
old_line = next(line for line in assembly.splitlines(keepends=True) if line.startswith('    notation_intro='))
assert 'in progress' in old_line
helper = '''def notation_introduction(reports):
    """Describe actual audit status without claiming a pending audit is done."""
    expected=set(range(5,28))
    done={r['scan'] for r in reports if r.get('audited')}
    pending=sorted(expected-done)
    status=('All 23 pages have completed the independent image-only audit. '
            if not pending else
            'Independent audits remain pending for scans '+', '.join(f'{n:03d}' for n in pending)+'. ')
    return ('# Notation table\\n\\nThis table records notation from the current authoritative page reports. '
            +status+'The actual completion records are preserved in progress.log. '
            'Cross-page comparison outcomes are documented in documentation/notation_review.md. '
            'Differences of handwriting, distinct alphabets and local uncertainty are not silently regularized. '
            'A literal headless shaft remains a dash. Abbreviations, quotation marks and small raised strokes were read locally.\\n\\n')

'''
assert 'def notation_introduction(' not in assembly
assembly = assembly.replace('def build():\n', helper + 'def build():\n', 1)
assembly = assembly.replace(old_line, '    notation_intro=notation_introduction(reports)\n', 1)
watermark = 'The supplied method identifies EXTRA STRONG as a possible paper watermark; no such pale or reversed paper marks were treated as manuscript text in this run. A positive watermark reading was not established from these scans.'
old = 'No external texts were consulted.\\n\']'
new = 'No external texts were consulted.\\n\\n' + watermark + '\\n\']'
assert assembly.count(old) == 1
assembly = assembly.replace(old, new, 1)
ast.parse(assembly)

# Only intro strings are changed in these existing generated Markdown files.
# Their tables/page sections will be rebuilt by root after the remaining audits.
(R / 'scripts/assemble.py').write_text(assembly)
spec = importlib.util.spec_from_file_location('assemble_documentation_only', R / 'scripts/assemble.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
current_reports = [json.loads(p.read_text()) for p in sorted((R / 'reviews').glob('149_scan*.json'))]
notation = before['notation_current.md']
table_start = notation.index('| scan | written form |')
notation = module.notation_introduction(current_reports) + notation[table_start:]
notes = before['SP84_C13_149_notes.md']
needle = 'No external texts were consulted.\n'
assert notes.count(needle) == 1 and 'EXTRA STRONG' not in notes
notes = notes.replace(needle, needle + '\n' + watermark + '\n', 1)

(R / 'README.md').write_text(readme)
(R / 'notation_current.md').write_text(notation)
(R / 'SP84_C13_149_notes.md').write_text(notes)
for n, report in reports.items():
    expected = copy.deepcopy(original_reports[n])
    if n == 19:
        expected['changes'][i] = report['changes'][i]
    else:
        expected['notes'] = report['notes']
    assert expected == report
    (R / f'reviews/149_scan{n:03d}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert all(hashlib.sha256((R / p).read_bytes()).hexdigest() == h for p, h in protected.items())

# Text-only role check: only current pages form the combined transcription;
# proposal .tex files remain an explicitly archived distinct set.
role_check = []
for n in range(5, 28):
    page = R / f'pages/149_scan{n:03d}.tex'
    proposal = R / f'reviews/149_scan{n:03d}.tex'
    assert page.is_file() and proposal.is_file()
    role_check.append(dict(scan=n, current_page=str(page.relative_to(R)),
                           archived_proposal=str(proposal.relative_to(R)),
                           same_text=page.read_text() == proposal.read_text()))
edits = [dict(file=p, before=before[p], after=(R / p).read_text()) for p in files if before[p] != (R / p).read_text()]
log = dict(completed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           authorization='Root approved README and actual-status intros, authorial qualifications, exact candid watermark sentence, and019c16 current accounting from its existing adjudication.',
           edits=edits, archived_text_role_check=role_check,
           protected_hashes=protected, protected_files_unchanged=True,
           historical_draft_values_preserved_in_log=True,
           current_count_delta=dict(places=0, against_C=1, against_H=0, high=-1, medium=0, low=1),
           audit_counts_unchanged=True, no_page_or_notation_decision_change=True,
           aggregate_tables_and_page_sections_not_rebuilt=True)
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
md = ('# Final documentation cleanup — reader B\n\n' + log['completed_utc'] + '\n\n'
      'README now distinguishes authoritative pages, current structured report fields, archived proposal TeX and frozen historical comparison evidence. The notation introduction reports actual audit completion dynamically; no pending audit is claimed complete. The notes name the possible EXTRA STRONG watermark candidly without a positive image identification. Source qualifications on013 and021 are identified as authorial.\n\n'
      '019/c16 remains one insertion place. Its current C flag is true for tentative si omitted by C, its H flag remains true for insertion placement, and its compound confidence is low. The exact prior draft fields and current fields are in the JSON log. This changes C by+1, high by−1 and low by+1, with places and H unchanged. No page, frozen input, adjudication, audit changed count or notation decision changed.\n\n'
      'The text-only role check found all23 current page fragments and23 archived proposal fragments; the JSON records whether each pair has identical text. Aggregate tables and page sections were not rebuilt.\n')
LOG.with_suffix('.md').write_text(md)
print(json.dumps({'files_modified': [x['file'] for x in edits],
                  'protected_files_unchanged': True,
                  'archive_pairs_checked': len(role_check),
                  'archive_pairs_different': sum(not x['same_text'] for x in role_check),
                  'count_delta': log['current_count_delta']}))
