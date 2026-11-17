#!/usr/bin/env python3
"""Assemble research notes without opening or modifying frozen transcription files."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WORKING = ROOT / 'working'
catalog = json.loads((WORKING / 'context_catalog.json').read_text())
comparisons = {}
for line in (WORKING / 'comparisons_dss.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    row = line.split(' || ')
    assert len(row) == 5, row
    identifier, topic, scans, kind, note = row
    assert identifier not in comparisons, identifier
    comparisons[identifier] = dict(topic=topic, scans=scans, kind=kind, note=note)
assert set(comparisons) == {r['id'] for r in catalog['dossier_statements']}
assert len(comparisons) == 255

def cell(text):
    return text.replace('|', r'\|').replace('\n', ' ')

parts = [(WORKING / name).read_text().rstrip() for name in
         ('notes_core.md', 'notes_apparatus.md', 'notes_new_results.md')]
table = [
    '## Individual comparison with all 255 dossier statements',
    '',
    'Every selected DSS row has its own entry below, in the source order: STRATA 10, PATHS 76, BISITE 113 and RESIDUE 56. The status and earlier manuscript locator are copied from the supplied dossier; a blank locator is explicitly marked rather than reconstructed. The short topic is an index label, not a replacement statement; the exact statements, original rows and status cells are preserved in `working/context_catalog.json`.',
    '',
    'The second column cites the line of `context/DOSSIER_STATEMENTS_WITH_STATUS.md` and its own earlier-manuscript locator; those older locators do not refer to a supplied Montpellier scan. The third column identifies evidence in the present package, or says **none** for no occurrence of that particular statement. Each last-column comparison is one note, with its kind in the third column; N/Q references lead to the source quotations and fuller analysis above.',
    ''
]
previous = None
for entry in catalog['dossier_statements']:
    identifier = entry['id']
    part = identifier.split()[0] + ' ' + identifier.split()[1].split('.')[0]
    if part != previous:
        table.extend([
            '### ' + part,
            '',
            '| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |',
            '|---|---|---|---|'
        ])
        previous = part
    comp = comparisons[identifier]
    locator = entry['manuscript_locator_exact'] or '(no manuscript locator supplied)'
    source = f"{entry['status_exact']}; DSS:{entry['source_line']}; {locator}"
    same = entry.get('state_same_id_entries', [])
    if same:
        source += '; same-ID RS:' + ','.join(str(s['source_line']) for s in same)
    scans = comp['scans'] if comp['scans'] != 'none' else '**none**'
    table.append('| ' + ' | '.join(map(cell, [
        f"**{identifier}** — {comp['topic']}", source,
        scans + '; ' + comp['kind'], comp['note']])) + ' |')
    # Separating group tables from their following heading is mandatory Markdown.
    nxt = catalog['dossier_statements'].index(entry) + 1
    if nxt == len(catalog['dossier_statements']) or (
        catalog['dossier_statements'][nxt]['id'].split()[0] + ' ' +
        catalog['dossier_statements'][nxt]['id'].split()[1].split('.')[0]
    ) != part:
        table.append('')
parts.append('\n'.join(table).rstrip())
parts.append((WORKING / 'notes_state_impact.md').read_text().rstrip())
parts.append(r'''## Source key and limits of the reference check

The relevant supplied files are `context/README.md`, `context/notes/RESULTS_STATE.md`, `context/NEW_RESULTS.md`, `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, both files under `context/hua_project/`, `context/PURSUING_STACKS_CONTENTS.md`, and `context/ps_chapters_VI_VII/ps6.tex` / `ps7.tex`. The cited companion files are under **`context/companion/chunks/`**: `DER_II-a.tex`, `DER_XIIb-a.tex` and `DER_XVI.tex`; their manuscript-page markers are locators in the supplied companion's transcription, not new visual verification of those older manuscripts.

The two externally checked primary references, followed from Hua's leads, are:

1. A. Grothendieck and J.-L. Verdier, **SGA 4 I, Exposé IV, exercise 9.5.10(a–c)**, original pp. 470–471; [checked primary PDF](https://www.normalesup.org/~forgogozo/SGA4/04/04.pdf), retypeset p. 96 (PDF index 95). Relevant notes: N10–N11 and R01.
2. N. Gurski, N. Johnson and A. M. Osorno, **Extending homotopy theories across adjunctions**, [arXiv:1508.00054, v3](https://arxiv.org/pdf/1508.00054.pdf), pp. 3–4, Definitions 1.3–1.4/1.9, Lemma 1.7 and Theorem 1.11(c). Relevant notes: N26 and R10.

The compact check record is `working/primary_references.md`; its conclusions are qualified in the notes above. Other bibliographical assertions in NR, RS and Hua are attributed to those supplied files rather than presented as independently verified literature results.

`working/context_search_log.json` records the context queries associated with the notes and comparisons, including zero-match searches. A keyword match is a discovery aid, not proof that an earlier result is correct or that a manuscript contains it; the positive comparisons rest on the frozen readings and the located contextual statements. The first-pass `working/observations.md` is a process record superseded by the audited transcription and these notes wherever they differ.

This return establishes neither a whole-archive priority date nor the contents of the missing cote 118. The 34-page diplomatic reading, its 131 doubt records, and the bounded historical comparisons are the completed work; the mathematical conjectures and contextual research claims retain the qualifications stated in their individual entries.
'''.rstrip())

output = '\n\n'.join(parts) + '\n'
output = re.sub(r'^(#{1,6} [^\n]+)\n(?=\S)', r'\1\n\n', output, flags=re.M)
target = ROOT / 'MPL_116+117_notes.md'
target.write_text(output)
assert len(re.findall(r'^### NR(?:0[1-9]|1[0-2]|K[123]) —', output, re.M)) == 15
assert all(f'**{r["id"]}** —' in output for r in catalog['dossier_statements'])
print(f'Wrote {target.name}: {len(output.split())} words, {len(output.splitlines())} lines; 255 DSS and 15 NR comparisons.')
