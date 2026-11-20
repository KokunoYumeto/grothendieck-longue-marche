#!/usr/bin/env python3
"""Merge disjoint, actually inspected ID subsets of one current page. No inference."""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path
import sys


def parse_time(s):
    try:
        return dt.datetime.strptime(s,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return dt.datetime.fromisoformat(s.replace('Z','+00:00'))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scan',type=int)
    parser.add_argument('parts',type=Path,nargs='+')
    parser.add_argument('--workspace',type=Path,default=Path.cwd())
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    base=args.workspace.resolve()
    with (base/'source/DM01_1_001-160_texts/MARKS.tsv').open(newline='',encoding='utf-8') as f:
        ids=[r['id'] for r in csv.DictReader(f,delimiter='\t') if int(r['scan'])==args.scan]
    if not ids:
        raise ValueError('No marks for requested scan')
    seen={}; readers={}; starts=[];finishes=[];views=[];errors=[];patterns=[];notes=[];paths=[];intervals=[]
    for path in args.parts:
        path=path.resolve()
        data=json.loads(path.read_text(encoding='utf-8'))
        if int(data['scan'])!=args.scan:
            raise ValueError(f'{path}: wrong page')
        reader=data.get('reader') or data.get('who')
        if not reader:
            raise ValueError(f'{path}: missing reader')
        rows=data['rows']
        these=[r['id'] for r in rows]
        if these != [i for i in ids if i in set(these)]:
            raise ValueError(f'{path}: subset is duplicated or out of original order')
        for row in rows:
            ident=row['id']
            if ident not in ids or ident in seen:
                raise ValueError(f'{path}: unknown or overlapping ID {ident}')
            seen[ident]=row;readers[ident]=reader
        start=data.get('started_utc') or data.get('reader_started_utc')
        finish=data.get('finished_utc') or data.get('reader_finished_utc')
        if not start or not finish or parse_time(start)>parse_time(finish):
            raise ValueError(f'{path}: missing/inconsistent actual reading interval')
        starts.append(start);finishes.append(finish)
        intervals.append({'reader':reader,'started_utc':start,'finished_utc':finish,'marks':len(rows)})
        for view in data.get('views',[]):
            views.append({**view,'reader':reader})
        for error in data.get('other_errors',[]):
            if error not in errors:errors.append(error)
        for pattern in data.get('patterns',[]):
            patterns.append({**pattern,'reader':reader})
        notes.append({'reader':reader,'notes':data.get('notes','')})
        paths.append(str(path.relative_to(base)) if path.is_relative_to(base) else str(path))
    if set(seen)!=set(ids):
        raise ValueError('Missing IDs: '+','.join(i for i in ids if i not in seen))
    result={'scan':args.scan,'reader':'Coordinator assembly; actual visual readers are recorded per mark in row_readers',
            'row_readers':readers,'started_utc':min(starts,key=parse_time),'finished_utc':max(finishes,key=parse_time),
            'reader_intervals':intervals,'rows':[seen[i] for i in ids],'views':views,'other_errors':errors,
            'patterns':patterns,'notes':notes,'source_submission_paths':paths}
    output=args.output or base/f'work/scan{args.scan:03}.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(output),'scan':args.scan,'marks':len(ids),'readers':len(args.parts)},ensure_ascii=False))

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError) as exc:
        print('ERROR: '+str(exc),file=sys.stderr);sys.exit(1)
