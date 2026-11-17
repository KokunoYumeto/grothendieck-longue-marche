#!/usr/bin/env python3
"""Consolidate actual research events, preserving their original timestamps.

This is record assembly, not a mathematical test, transcription audit, or
permission to upgrade another run's result. Supplemental IDs are retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

ROOT=Path(__file__).resolve().parents[1]
SUP=ROOT/'research_support'
FIELDS=['statement_id','date','who','type','outcome']
ALLOWED={
 'targeted proof check','independent re-proof','computation or formal certificate',
 'used and rechecked in this run','carried as background without fault found',
 "refuted, with refined statement's id",
}
INPUTS=[
 ('root_note_events.tsv','root'),
 ('boundary_levels_checks.tsv','boundary_levels'),
 ('octahedral_CHECK_EVENTS.tsv','octahedral_checks'),
 ('s20_check_events.tsv','mechanical_support'),
 ('root_proof_review.tsv','mechanical_support'),
 ('final_metadata_audit.tsv','mechanical_support'),
]

def main():
    rows=[]
    included=[]
    for name,agent in INPUTS:
        path=SUP/name
        if not path.exists():
            if name=='final_metadata_audit.tsv':
                continue
            raise RuntimeError(f'Missing required event source: {name}')
        with path.open(encoding='utf-8',newline='') as f:
            reader=csv.DictReader(f,delimiter='\t')
            assert reader.fieldnames==FIELDS, (name,reader.fieldnames)
            loaded=list(reader)
        for row in loaded:
            assert set(row)==set(FIELDS) and all(row.values()),(name,row)
            assert row['type'] in ALLOWED,(name,row['type'])
            # Add known run routing without inventing an unexposed effort level.
            if 'effort' not in row['who'].lower():
                row['who']+='; effort not exposed'
            if 'MPL_64_040-077' not in row['who']:
                row['who']+=f'; run MPL_64_040-077/{agent}'
            rows.append(row)
        included.append(dict(file=name,events=len(loaded)))
    extra=SUP/'root_extra_events.json'
    if extra.exists():
        for row in json.loads(extra.read_text()):
            assert set(row)==set(FIELDS) and all(row.values()),row
            assert row['type'] in ALLOWED,row
            rows.append(row)
        included.append(dict(file=extra.name,events=len(json.loads(extra.read_text()))))
    # Keep events from different reviews even if they concern the same claim.
    # Only exact accidental copies are removed.
    unique=[]
    seen=set()
    for row in rows:
        key=tuple(row[x] for x in FIELDS)
        if key not in seen:
            unique.append(row);seen.add(key)
    unique.sort(key=lambda r:(r['date'],r['statement_id'],r['type']))
    with (ROOT/'CHECK_EVENTS.tsv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,FIELDS,delimiter='\t')
        writer.writeheader();writer.writerows(unique)
    note_ids={n['id'] for n in json.loads((SUP/'research_note_metadata.json').read_text())}
    logged={r['statement_id'] for r in unique}
    assert note_ids<=logged,sorted(note_ids-logged)
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    report={'assembled_utc':stamp,'sources':included,'events':len(unique),'distinct_statement_ids':len(logged),'main_notes_covered':len(note_ids),'scope':'event consolidation only; not a new proof or source audit'}
    (SUP/'check_event_assembly.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
    main()
