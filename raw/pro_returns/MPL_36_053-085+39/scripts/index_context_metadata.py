#!/usr/bin/env python3
"""Index supplied context metadata after freeze; never access cited originals."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

WORK=Path(__file__).resolve().parent.parent
CONTEXT=WORK.parent/'context'

def main():
    results=(CONTEXT/'notes'/'RESULTS_STATE.md').read_text()
    readme=(CONTEXT/'README.md').read_text()
    source_paths=re.findall(r'^- `([^`]+)`$',results,re.M)
    source_map={Path(path).name:path for path in source_paths}
    entries=[];section=None
    for line_number,line in enumerate(results.splitlines(),1):
        if line.startswith('## '):section=line[3:]
        match=re.match(r'^- \*\*(.+?)\*\*(.*)$',line)
        if not match:continue
        entry_id,tail=match.groups()
        status_match=re.search(r'\[([^\]]+)\]',tail)
        run_state=tail.startswith(': ')
        status=(tail[2:].split(';',1)[0] if run_state else status_match[1] if status_match else None)
        source_match=re.search(r'\(([^()]+\.(?:csv|md))\)\s*$',tail)
        source_filename=source_match[1] if source_match else None
        where_match=re.search(r'\bWhere:\s*(.*?)(?=\s*\([^()]+\.(?:csv|md)\)\s*$)',tail)
        where_raw=where_match[1].strip() if where_match else None
        supplied=[]
        if where_raw:
            for locator in re.findall(r'\b(?:folios|scans)\s+[^;]+',where_raw):
                supplied.append({'kind':'folio' if locator.startswith('folios') else 'scan','raw':locator})
            if entry_id=='LM4 D.12':
                supplied.append({'kind':'unlabeled scan/folio locator sequence','raw':where_raw,
                                 'note':'Retained without assigning unlabeled number ranges to sections, folios, or scans.'})
        if entry_id=='MPL_33_002-049 §2':
            supplied.append({'kind':'scan','raw':'Scans **002…','truncated':True})
        if entry_id=='MPL_91_099-143 §68':
            supplied.append({'kind':'source-scan evidence column','raw':'Title sheet 124; thickness conditions 126 and 128',
                             'note':'The source excerpt labels the column Evidence in the retained scans; no fuller source was supplied.'})
        if entry_id=='WG2 §2.1 #2':
            supplied.extend([{'kind':'manuscript page','raw':'ms. pp. 1–16, nos 1–8'},
                             {'kind':'scan','raw':'scans 3–18'}])
        hua_match=re.search(r'^ \((cote \d+, their pp\. .*?; our scans .*?)\)',tail)
        hua_refs=None
        if hua_match:
            hua_refs=hua_match[1]
            supplied.append({'kind':'Hua page / supplied scan correspondence','raw':hua_refs})
        intake_match=re.search(r'Our intake:\s*(.*)$',tail)
        entry={
            'id':entry_id,
            'context_file':'notes/RESULTS_STATE.md',
            'context_line':line_number,
            'section':section,
            'status_exact':status,
            'source_filename':source_filename,
            'source_path_as_supplied':source_map.get(source_filename),
            'source_attribution':"Hua, findings register" if hua_match else None,
            'source_scan_folio_references':supplied or None,
            'where_exact':where_raw,
            'intake_exact':intake_match[1] if intake_match else None,
            'run_state_exact':tail[2:tail.rfind(' (')].strip() if run_state else None,
            'truncation':{
                'entry_contains_ellipsis':('…' in tail),
                'status_truncated':bool(status and '…' in status),
                'locator_truncated':any('…' in item['raw'] for item in supplied),
                'referenced_original_not_supplied_or_opened':True,
            },
        }
        entries.append(entry)
    planning=re.search(r'Drafts around SGA 4, 5 and 7.*?\(S19\)\.',readme,re.S)
    assert planning
    result={
        'created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scope':'Mechanical index of supplied context metadata only. No cited originals, scans, or frozen transcription files accessed by this script.',
        'entry_count':len(entries),
        'entries':entries,
        'readme_plan':{
            'id':'S19',
            'context_file':'README.md',
            'source_filename':'README.md',
            'status_exact':None,
            'status_note':'No bracketed status is supplied for S19 in the README; it is described as a planning task.',
            'plan_exact':planning[0],
            'source_scan_folio_references':[
                {'kind':'package scope','cote':36,'raw':'scans 53-85'},
                {'kind':'package scope','cote':39,'raw':'scans 2-20'},
            ],
            'truncated':False,
        },
        'limitations':[
            'Ellipses and truncated statuses are preserved; omitted words have not been reconstructed.',
            'No scan or folio reference is inferred from a filename range or an entry section number.',
            'Source file paths are copied from the supplied source list only; referenced originals were not opened.',
            'The scan/folio field is null when no such locator is supplied.',
            'Unlabeled locator sequences remain unclassified.',
        ],
    }
    path=WORK/'qa'/'context_index.json'
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':str(path),'entry_count':len(entries),'ids':[entry['id'] for entry in entries],
                      'status_truncated':[entry['id'] for entry in entries if entry['truncation']['status_truncated']],
                      'locator_truncated':[entry['id'] for entry in entries if entry['truncation']['locator_truncated']],
                      'readme_plan':'S19'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
