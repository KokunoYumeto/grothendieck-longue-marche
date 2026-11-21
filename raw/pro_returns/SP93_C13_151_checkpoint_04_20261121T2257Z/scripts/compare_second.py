"""Token-by-token comparison of prewritten first and blind second readings."""
from pathlib import Path
import argparse
import csv
import difflib
import json
import re

ROOT=Path('/workspace/scratch/d12e26a9cd50')
OUT=ROOT/'SP93_C13_151_work'

def read(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def tokens(text):
    # Whitespace and line wrapping are not manuscript tokens; every command,
    # letter sequence, numeral and punctuation/symbol is otherwise retained.
    return re.findall(r'\\[A-Za-z@]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+|[^\s]',text)

def compare(scan):
    name=f'151_scan{int(scan):03d}'
    first=read(OUT/'second'/f'{name}_first.tsv')
    second=read(OUT/'second'/f'{name}_second.tsv')
    if [r['box'] for r in first] != [r['box'] for r in second]:
        raise ValueError('Box IDs or order differ; repair the reading file before comparison.')
    rows=[]
    for a,b in zip(first,second):
        ta,tb=tokens(a['reading']),tokens(b['reading'])
        operations=[{'operation':tag,'first':ta[i:j],'second':tb[k:l]} for tag,i,j,k,l in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes() if tag!='equal']
        rows.append({'box':a['box'],'same_tokens':'yes' if not operations else 'no','first':a['reading'],'second':b['reading'],
            'token_changes':json.dumps(operations,ensure_ascii=False)})
    target=OUT/'second'/f'{name}_comparison.tsv'
    with target.open('w',newline='') as f:
        w=csv.DictWriter(f,['box','same_tokens','first','second','token_changes'],delimiter='\t');w.writeheader();w.writerows(rows)
    print(json.dumps({'scan':f'{int(scan):03d}','boxes':len(rows),'different_boxes':sum(r['same_tokens']=='no' for r in rows),'comparison':str(target)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('scans',nargs='+')
    for s in p.parse_args().scans:compare(s)
