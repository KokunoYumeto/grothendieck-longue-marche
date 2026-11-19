#!/usr/bin/env python3
"""Add only mechanically unique text anchors and explicit existing scan refs.

No images are opened. No page text, decisions or ink-review ledgers are edited.
Without --apply this prints a proposal summary. On apply, only blocks[].position
and the three explicitly authorized crop fields can change in page records.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import runpy
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]
SOURCE=OUT.parent/'source/SP31_CW_156-3_scans'


def proposal(record: dict,tex: str,work: dict) -> tuple[dict,list[dict],list[str]]:
    updated=json.loads(json.dumps(record,ensure_ascii=False))
    scan=record['scan'];changes=[];unresolved=[]
    projected,offsets=work['inventory_projection'](tex)
    for index,block in enumerate(updated['blocks'],1):
        kind,position,words=block
        if position=='paper background':continue
        if 'tex line ' in position and 'mechanical text match' not in position:continue
        row=[scan,'text','his hand',f'{scan:03}-B{index:02}',kind,position,words,'yes']
        anchor,basis=work['inventory_anchor'](tex,row,projected,offsets)
        if anchor is None:
            unresolved.append(row[3]);continue
        line=tex.count('\n',0,anchor)+1;column=anchor-tex.rfind('\n',0,anchor)
        suffix=f'tex line {line}, column {column} (mechanical text match)'
        if 'mechanical text match' in position:
            new_position=re.sub(r'tex line \d+, column \d+ \(mechanical text match\)',suffix,position)
        else:new_position=position+'; '+suffix
        if new_position!=position:
            block[1]=new_position
            changes.append({'scan':scan,'element':row[3],'field':'block position','before':position,'after':new_position,'basis':basis})
    crop_specs={7:(11,'whole / lower half',['','_b']),8:(10,'whole / halves',['','_a','_b']),9:(11,'whole / halves',['','_a','_b'])}
    if scan in crop_specs:
        index,old,suffixes=crop_specs[scan]
        if len(updated['rows'])>=index and updated['rows'][index-1].get('crop')==old:
            base=f"{record['folder']}_156-3_scan{scan:03}"
            paths=[SOURCE/(base+suffix+'.jpg') for suffix in suffixes]
            if all(path.is_file() for path in paths):
                new='; '.join('SP31_CW_156-3_scans/'+path.name for path in paths)
                updated['rows'][index-1]['crop']=new
                changes.append({'scan':scan,'element':f'{scan:03}-{index:02}','field':'crop reference','before':old,'after':new,'basis':'exact existing supplied whole/half JPEG filenames; no new enlargement or image inspection'})
    # Assert that no other record field was changed, including all decisions.
    original_rest={k:v for k,v in record.items() if k not in {'blocks','rows'}}
    updated_rest={k:v for k,v in updated.items() if k not in {'blocks','rows'}}
    assert original_rest==updated_rest
    for a,b in zip(record['blocks'],updated['blocks']):assert a[0]==b[0] and a[2]==b[2]
    for index,(a,b) in enumerate(zip(record['rows'],updated['rows']),1):
        assert {k:v for k,v in a.items() if k!='crop'}=={k:v for k,v in b.items() if k!='crop'}
        if a.get('crop')!=b.get('crop'):assert (scan,index) in {(7,11),(8,10),(9,11)}
    return updated,changes,unresolved


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    work=runpy.run_path(str(OUT/'scripts/work.py'))
    all_changes=[];all_unresolved=[];files_changed=[]
    for path in sorted((OUT/'records').glob('[0-9][0-9][0-9].json')):
        for attempt in range(5):
            raw=path.read_bytes();record=json.loads(raw)
            page=OUT/'pages'/record['filename'];page_bytes=page.read_bytes()
            updated,changes,unresolved=proposal(record,page_bytes.decode('utf-8'),work)
            if path.read_bytes()!=raw or page.read_bytes()!=page_bytes:continue
            if args.apply and changes:
                temp=path.with_name(path.name+'.anchor-tmp')
                temp.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
                if path.read_bytes()!=raw or page.read_bytes()!=page_bytes:
                    temp.unlink();continue
                os.replace(temp,path);files_changed.append(path.name)
            all_changes.extend(changes);all_unresolved.extend(unresolved)
            break
        else:raise RuntimeError('Repeated concurrent changes prevented safe update: '+path.name)
    if args.apply and all_changes:
        report=OUT/'audit/inventory_anchor_edits.tsv'
        report.parent.mkdir(parents=True,exist_ok=True)
        exists=report.exists()
        with report.open('a',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=['scan','element','field','before','after','basis'],delimiter='\t',lineterminator='\n')
            if not exists:writer.writeheader()
            writer.writerows(all_changes)
    print(json.dumps({'applied':args.apply,'changed_record_files':files_changed,
                      'text_anchors_added_or_refreshed':sum(c['field']=='block position' for c in all_changes),
                      'crop_references_resolved':[c['element'] for c in all_changes if c['field']=='crop reference'],
                      'unresolved_manual_blocks':all_unresolved},ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':raise SystemExit(main())
