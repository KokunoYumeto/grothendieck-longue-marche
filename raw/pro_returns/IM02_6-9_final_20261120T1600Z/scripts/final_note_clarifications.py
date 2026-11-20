#!/usr/bin/env python3
"""Record the prompt's stated authority for a supplied Michel Hua reading.

This does not alter any transcription, decision, or confidence. The earlier
reader wording is retained for audit, and the final note follows the prompt.
"""
import json
from review import D, now, rebuild

p = D / 'reviews' / '8_scan078.json'
report = json.loads(p.read_text())
row = next(r for r in report['rows'] if r['id'] == 'L752')
old = 'The source says Michel Hua’s project reads co-Lie; this is a reported project reading, not an explicit statement of a named manual scan check.'
new = 'The source attributes co-Lie to Michel Hua’s project. Following the prompt, the main reader treats that supplied reading with human-check authority; the visible joined coLie spelling supports it and does not contradict the reading.'
if old in row['note']:
    row['reader_note_before_authority_clarification'] = row['note']
    row['note'] = row['note'].replace(old, new)
    row.setdefault('events', []).append({
        'date': now(),
        'who': 'GPT-6 Astra Pro; effort not exposed; main reader; run IM02_6-9_20261120',
        'type': 'carried as background without fault found',
        'outcome': 'Cote 8, scan 078: clarified that the supplied Michel Hua reading has the human-check authority specified by the prompt. The accepted coLie reading and exact TeX replacement are unchanged. This records the supplied authority, not a new visual or mathematical check.',
    })
    p.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(rebuild())
