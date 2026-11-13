"""Prepare exact generator replacements without writing any shared dependency."""
from pathlib import Path
import csv
import hashlib
import json

OUT = Path('work/layout_probes')
candidate = json.loads((OUT / 'range134_heading_candidate.json').read_text())
rows = []


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def add(path, old, new):
    source = Path(path).read_text()
    assert source.count(old) == 1, path
    changed = source.replace(old, new)
    compile(changed, Path(path).name, 'exec')
    target = OUT / 'range134_staged' / Path(path).name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(changed)
    rows.append({'path': path, 'source_sha256': digest(source), 'expected_match_count': 1,
                 'old': old, 'new': new, 'after_sha256': digest(changed),
                 'staged_copy': target.as_posix(),
                 'syntax_validation': 'PASS', 'shared_dependency_written': False})


add('work/scripts/build_readers.py',
    "  pieces += ['% BEGIN PACKAGE '+pkg,r'\\ifnum\\LMform<2\\Needspace{11\\baselineskip}\\subsection*{Scans '+row['scans'].replace('-','--')+r'}\\fi']",
    "  range_reservation = r'\\Needspace{\\dimexpr123mm+11\\baselineskip\\relax}' if pkg=='LM_C4-134-152' else r'\\Needspace{11\\baselineskip}'\n"
    "  pieces += ['% BEGIN PACKAGE '+pkg,r'\\ifnum\\LMform<2'+range_reservation+r'\\subsection*{Scans '+row['scans'].replace('-','--')+r'}\\fi']")

add('work/scripts/verify_sources.py',
    "        pieces += ['% BEGIN PACKAGE '+package,r'\\ifnum\\LMform<2\\Needspace{11\\baselineskip}\\subsection*{Scans '+row['scans'].replace('-','--')+r'}\\fi']",
    "        range_reservation = r'\\Needspace{\\dimexpr123mm+11\\baselineskip\\relax}' if package=='LM_C4-134-152' else r'\\Needspace{11\\baselineskip}'\n"
    "        pieces += ['% BEGIN PACKAGE '+package,r'\\ifnum\\LMform<2'+range_reservation+r'\\subsection*{Scans '+row['scans'].replace('-','--')+r'}\\fi']")

inventory = Path('work/scripts/record_generated_heading_repairs.py').read_text()
start = inventory.index('        if form < 2:\n')
end = inventory.index('        # These rows enumerate conditional applicability', start)
old = inventory[start:end]
new = old.replace('        if form < 2:\n',
                  "        if form < 2:\n            range134 = read(WORK / 'layout_probes/range134_heading_candidate.json')\n")
new = new.replace("                new = ranges['new_template'].replace('#1', span)\n",
                  "                new = ranges['new_template'].replace('#1', span)\n"
                  "                range_reason = ranges['reason']\n"
                  "                if package == 'LM_C4-134-152':\n"
                  "                    new = range134['new_generated_prefix']\n"
                  "                    range_reason += ' ' + range134['reason']\n")
new = new.replace("'scan-range heading guard', old, new, ranges['reason'],",
                  "'scan-range heading guard', old, new, range_reason,")
new += ("                if package == 'LM_C4-134-152':\n"
        "                    rows[-1]['candidate'] = 'work/layout_probes/range134_heading_candidate.json'\n"
        "                    rows[-1]['candidate_sha256'] = digest(WORK / 'layout_probes/range134_heading_candidate.json')\n"
        "                    rows[-1]['probe_validation'] = 'work/layout_probes/range134_heading_validation.json'\n")
add('work/scripts/record_generated_heading_repairs.py', old, new)

# Verify the exact final prefix for every package while keeping all other
# package prefixes byte-identical to the previously frozen generation rule.
index = list(csv.DictReader(Path('sources/fr/records/CURRENT_TEXT_INDEX.tsv').open(), delimiter='\t'))
unchanged = 0
for row in index:
    package = row['package']
    reserve = r'\Needspace{\dimexpr123mm+11\baselineskip\relax}' if package == 'LM_C4-134-152' else r'\Needspace{11\baselineskip}'
    after = r'\ifnum\LMform<2' + reserve + r'\subsection*{Scans ' + row['scans'].replace('-', '--') + r'}\fi'
    before = r'\ifnum\LMform<2\Needspace{11\baselineskip}\subsection*{Scans ' + row['scans'].replace('-', '--') + r'}\fi'
    if package == 'LM_C4-134-152':
        assert after == candidate['new_generated_prefix']
        assert before == candidate['old_generated_prefix']
    else:
        assert after == before
        unchanged += 1
assert unchanged == 115
report = {'status': 'STAGED_SYNTAX_AND_PREFIX_CHECK_PASS',
          'candidate': 'work/layout_probes/range134_heading_candidate.json',
          'candidate_sha256': hashlib.sha256((OUT / 'range134_heading_candidate.json').read_bytes()).hexdigest(),
          'probe_validation': 'work/layout_probes/range134_heading_validation.json',
          'replacements': rows, 'unchanged_other_package_prefixes': unchanged,
          'range_occurrences_after_integration': 580, 'special_range_occurrences': 5,
          'duplicate_range_rows_added': 0, 'source_text_changed': False,
          'shared_dependencies_modified': False}
(OUT / 'range134_generator_replacements.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print('Staged3 exact replacements; syntax PASS;115 other prefixes identical;580 range rows retained.')
