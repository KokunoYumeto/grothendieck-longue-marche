"""Reconcile administrative classification labels without changing readings.

Root audit scripts retain the labels used when each decision was made. This
one-time, idempotent finalization maps their descriptive shorthand to the exact
controlled vocabularies requested for the collation and error-sheet counts.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

ROOT=Path(__file__).resolve().parents[1]
kind_aliases={
    'punctuation':'misread symbol or index',
    'number':'misread symbol or index',
    'letter':'misread symbol or index',
    'symbol':'misread symbol or index',
    'index':'misread symbol or index',
    'diagram':'drawing or diagram',
    'word':'misread word',
}
category_aliases={
    'supplied punctuation':'Text that is not on the page',
    'ambiguous numeral':'Symbols and indices',
    'ambiguous overtrace':'Symbols and indices',
    'compressed ending':'Words',
    'full head supplied for terminal cap':'Drawings and diagrams',
    'terminal letter not separable':'Words',
    'letter sequence':'Words',
    'compressed short word':'Words',
    'retraced digit':'Symbols and indices',
    'prime overlaps parenthesis':'Symbols and indices',
    'point versus comma':'Symbols and indices',
    'comma substituted for literal point':'Symbols and indices',
    'brace extent':'Drawings and diagrams',
    'cancellation obscures lower bar':'Struck text',
    'alphabet':'Symbols and indices',
    'continuation shapes':'Symbols and indices',
    'omitted comma':'Omissions',
    'elongated terminal mark':'Symbols and indices',
    'normalized continuation and supplied comma':'Symbols and indices',
    'continuation shape and punctuation':'Symbols and indices',
    'two detached marks':'Symbols and indices',
}
changes=[]
for path in sorted((ROOT/'review').glob('*_reviewed.json')):
    data=json.loads(path.read_text())
    changed=False
    for i,row in enumerate(data['rows']):
        for key,mapping in [('kind',kind_aliases),('error_category',category_aliases)]:
            old=row.get(key)
            if old in mapping:
                if key=='error_category': row.setdefault('error_detail',old)
                row[key]=mapping[old]
                changes.append(f'{path.name} rows[{i}].{key}: {old} -> {row[key]}')
                changed=True
    for event in data.get('check_events',[]):
        if event['statement_id']=='R129-continuation-shapes; N129-13' and 'first-pass continuation review;' in event.get('who',''):
            event['who']=event['who'].replace('first-pass continuation review;','first-pass continuation review run;')
            changes.append(f'{path.name} continuation event provenance: explicitly label the already identified run')
            changed=True
    if changed:
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
if changes:
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'review/administrative_audit_corrections.md').open('a') as f:
        f.write('\n## Final controlled-vocabulary reconciliation — '+now+'\n\n')
        f.write('No reading, evidence, witness quotation, confidence, decision or audit count changed. Descriptive category detail is retained in `error_detail`; the required ten-category totals now include these rows. The continuation event already identified its model, effort and review; its provenance now explicitly names that review as a run.\n\n')
        for line in changes:f.write('- '+line+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'administrative classification reconciliation {now}: {len(changes)} metadata fields; transcription bytes unchanged\n')
print(json.dumps({'metadata_fields_changed':len(changes)}))
