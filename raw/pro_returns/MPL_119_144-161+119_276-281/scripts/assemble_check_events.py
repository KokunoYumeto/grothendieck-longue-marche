#!/usr/bin/env python3
"""Consolidate actual research events; never infer a proof from a note's presence.

The support ledgers use local F/T/R identifiers. This explicit map relates them
to the final N identifiers. Root-only events are separately authored records in
research/root_check_events.tsv. This script does not inspect images or edit TeX.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
HEADER = ['statement_id', 'date', 'who', 'type', 'outcome']
BACKGROUND = 'carried as background without fault found'

FINITE = {
    'F01':['N49'], 'F02':['N50'], 'F03':['N52'], 'F04':['N51'],
    'F05':['N53'], 'F06':['N54'], 'F07':['N47'], 'F08':['N48'],
    'F09':['N54'], 'F10':['N57'], 'F11':['N56'], 'F12':['N55'],
    'F13':['N40'], 'F14':['N38'], 'F15':['N46'], 'F16':['N43','N44'],
    'F17':['N78'], 'F18':['N79'], 'F19':['N45'], 'F20':['N61','N41'],
}
TOPOLOGY = {
    'T01':['N04','N05','N77'], 'T02':['N04'], 'T03':['N06'],
    'T04':['N04','N01'], 'T05':['N07'], 'T06':['N12'],
    'T07':['N11','N75'], 'T08':['N10','N13'], 'T09':['N14'],
    'T10':['N15'], 'T11':['N17','N18'], 'T12':['N16'], 'T13':['N19'],
    'T14':['N22'], 'T15':['N24'], 'T16':['N76','N24'],
    'T17':['N25','N23'], 'T18':['N26','N27'], 'T19':['N28'],
    'T20':['N29'], 'T21':['N30'], 'T22':['N31'],
    'T23':['N32','N33'], 'T24':['N34'],
    'TC1':['N15'], 'TC2':['N17'], 'TC3':['N29'], 'TC4':['N34'],
    'T20-unqualified':['N29-unqualified-implication'],
    'T24-Whitney-intrinsic':['N34-embedded-Whitney-invariance'],
}
REPORT = {
    'R01':'N63','R02':'N65','R02-HOURS':'N65','R03':'N64',
    'R03-SHARES':'N64','R04':'N69','R04-VETO':'N69',
    'R05':'N68','R05-COMMISSION':'N68','R06':'N70','R07':'N71',
    'R08':'N80','R09':'N67','R10':'N66','R11':'N72','R12':'N73',
    'WG2-Guide-2-ARCHIVE-ONLY':'WG2 §Guide #2',
    'CONTEXT250-DATE':'N62-context-date',
}

events = []
for source, mapping, worker in [
    ('finite_check_events.tsv', FINITE, 'finite_research'),
    ('topology_check_events.tsv', TOPOLOGY, 'topology_research'),
]:
    with (ROOT/'research'/source).open(newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            original = row['statement_id']
            ids = mapping.get(original, [original])
            if original.startswith('TOPOLOGY P'):
                ids = [original.removeprefix('TOPOLOGY ')]
            if original == 'Hua 119-foliation-quotient-topos-equivalence':
                ids = ['119-foliation-quotient-topos-equivalence']
            kind, outcome = row['type'], row['outcome']
            if original == 'MS119:159:A':
                kind = 'refuted, with refined statement N49R'
                outcome = outcome.replace('F02', 'N49R (proved in N50)')
            elif original == 'MS119:159:finalNB:c_alone':
                kind = 'refuted, with refined statement N51R'
            elif original == 'T20-unqualified':
                kind = 'refuted, with refined statement N29'
            elif original == 'T24-Whitney-intrinsic':
                kind = 'refuted, with refined statement N34'
            for statement in ids:
                events.append({
                    'statement_id': statement, 'date': row['date'],
                    'who': f'GPT-6 Astra Pro / effort inherited, not exposed / MPL119_20261118 / {worker}',
                    'type': kind,
                    'outcome': f'{outcome} [Support event {original}; research/{source}.]',
                })

report = (ROOT/'research/report_research.md').read_text()
report = report.split('## Check-event descriptions for the root to integrate', 1)[1]
for line in report.splitlines():
    if not line.startswith('| '):
        continue
    cells = [s.strip() for s in line.strip().strip('|').split('|')]
    if len(cells) != 3 or cells[0] in {'Statement ID','---'} or cells[0].startswith('-'):
        continue
    original, kind, outcome = cells
    events.append({
        'statement_id': REPORT.get(original, original), 'date':'2026-11-18',
        'who':'GPT-6 Astra Pro / effort inherited, not exposed / MPL119_20261118 / packaging_support',
        'type':kind, 'outcome':f'{outcome} [Support event {original}; research/report_research.md.]',
    })

with (ROOT/'research/root_check_events.tsv').open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    assert reader.fieldnames == HEADER
    events.extend(reader)

allowed = {
    'targeted proof check','independent re-proof','computation or formal certificate',
    'used and rechecked in this run',BACKGROUND,
}
for e in events:
    assert set(e) == set(HEADER)
    assert all(e[k].strip() for k in HEADER)
    assert e['type'] in allowed or e['type'].startswith('refuted, with refined statement ')

with (ROOT/'CHECK_EVENTS.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, HEADER, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)
print(f'Wrote {len(events)} actual events; source ledgers and ID mappings retained.')
