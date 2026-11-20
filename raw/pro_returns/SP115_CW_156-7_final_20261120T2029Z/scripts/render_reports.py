#!/usr/bin/env python3
"""Render the adjudicator's per-page data. This script makes no reading choices."""
from pathlib import Path
import collections
import csv
import html
import json

R = Path(__file__).resolve().parents[1]
S = 'SP115_CW_156-7'
pages = [json.loads(p.read_text()) for p in sorted((R/'review').glob('scan*_final.json'))]


def code(s):
    return '<code>' + html.escape(str(s)).replace('|', '&#124;').replace('\n', '<br>') + '</code>'


def prose(s):
    return str(s).replace('|', '&#124;').replace('\n', '<br>')


def evidence(c):
    s = c.get('scan_shows', '')
    if c.get('crop'):
        s += ' Crop: ' + c['crop'] + '; original box ' + str(c.get('box', 'see manifest')) + '.'
    return s


def count(d, k):
    return sum(bool(c.get(k)) for c in d.get('changes', []))


changes = [f'# {S} — changes and adjudications', '',
           'The final reading is determined from the supplied ink. Each row is one adjudicated place; a row may differ from both witnesses. Macro syntax alone is excluded. Doubt decisions are retained as evidence but distinguished from substantive text/state differences. Added uncertainty alone belongs in the doubts file.', '',
           '## Counts', '',
           '| Scan | Recorded places | Differences from C | Differences from H | High | Medium | Low |',
           '|---:|---:|---:|---:|---:|---:|---:|']
totals = collections.Counter()
for d in pages:
    conf = collections.Counter(c.get('confidence', 'medium') for c in d.get('changes', []))
    vals = [len(d.get('changes', [])), count(d, 'against_C'), count(d, 'against_H'), conf['high'], conf['medium'], conf['low']]
    for k,v in zip(['rows','C','H','high','medium','low'],vals): totals[k] += v
    changes.append('| ' + ' | '.join(map(str, [d['scan']] + vals)) + ' |')
changes.append('| **Total** | ' + ' | '.join(str(totals[k]) for k in ['rows','C','H','high','medium','low']) + ' |')
changes += ['', '### Confidence of differences by witness', '', '| Scan | C high | C medium | C low | H high | H medium | H low |', '|---:|---:|---:|---:|---:|---:|---:|']
cc_total=collections.Counter()
for d in pages:
    vals=[sum(bool(c.get(w)) and c.get('confidence')==q for c in d['changes']) for w in ['against_C','against_H'] for q in ['high','medium','low']]
    for i,v in enumerate(vals):cc_total[i]+=v
    changes.append('| '+' | '.join(map(str,[d['scan']]+vals))+' |')
changes.append('| **Total** | '+' | '.join(str(cc_total[i]) for i in range(6))+' |')
changes += ['', 'Counts in the C/H columns are the explicitly adjudicated differences recorded in the corresponding Boolean fields of the per-page final records. Resolutions that leave the same primary letters and source state can be recorded without counting as a substantive difference. Confidence describes the final ink decision, not the mathematical truth of the statement.', '',
            '## Consequential corrections', '']
for d in pages:
    for c in d.get('changes', []):
        if c.get('consequential'):
            changes.append(f"- Scan {d['scan']:03d}, {c['id']}, {c['place']}: {code(c['final'])}. {prose(c.get('consequence', c.get('scan_shows','')))}")
for d in pages:
    changes += ['', f"## Scan {d['scan']:03d} — manuscript page {d['scan']-1}", '',
                '| ID / place | Witness C | Witness H | Final reading | What the scan shows | Confidence |',
                '|---|---|---|---|---|---|']
    for c in d.get('changes', []):
        changes.append('| ' + ' | '.join([prose(c['id']+' — '+c['place']), code(c.get('C','')), code(c.get('H','')), code(c['final']), prose(evidence(c)), c['confidence']]) + ' |')
    changes += ['', '### Remaining uncertainties', '']
    if not d.get('doubts'):
        changes.append('None remaining in the adjudicated page.')
    for x in d.get('doubts', []):
        changes.append(f"- {prose(x['place'])}: {code(x['reading'])}; alternatives {code(x.get('alternatives',''))}; {x['confidence']}. {prose(x.get('reason',''))}")
    if d.get('S_decisions'):
        changes += ['', '### Witness S', '']
        for x in d['S_decisions']:
            changes.append(f"- {prose(x['id'])}: {prose(x['decision'])}. {prose(x['evidence'])}")
    if d.get('audit_changes'):
        changes += ['', '### Changes following the blind second reading', '',
                    '| Box / place | First reading | Blind reading | Final decision | Evidence |',
                    '|---|---|---|---|---|']
        for a in d['audit_changes']:
            changes.append('| ' + ' | '.join([prose(a['box']), code(a['first']), code(a['second']), code(a['final']), prose(a['evidence'])]) + ' |')
(R/(S+'_changes.md')).write_text('\n'.join(changes)+'\n')

columns = ['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
with (R/(S+'_collation.tsv')).open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=columns, delimiter='\t'); w.writeheader()
    for d in pages:
        for c in d.get('changes', []):
            if c.get('against_H'):
                w.writerow(dict(folder='H156-01',their_page=d['scan']-1,our_scan=d['scan'],line=c['place'],
                                their_reading=c.get('H',''),codex_reading=c.get('C',''),final_reading=c['final'],
                                scan_shows=evidence(c),kind=c['kind'],marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))

columns = ['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
with (R/(S+'_inventory.csv')).open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=columns); w.writeheader()
    for d in pages:
        for e in d.get('inventory', []):
            row = {k:e.get(k,'') for k in columns}
            row.update(scan=d['scan'],sheet_kind=e.get('sheet_kind','text'),hand=e.get('hand','his hand'),transcribed='yes')
            w.writerow(row)

meta = {'pages': [d['scan'] for d in pages], 'totals': dict(totals),
        'remaining_doubt_entries': sum(len(d.get('doubts', [])) for d in pages),
        'inventory_elements': sum(len(d.get('inventory', [])) for d in pages)}
(R/'review/report_counts.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(meta,ensure_ascii=False,indent=2))
