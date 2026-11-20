"""Serialization helper for explicit human-readable main-reader adjudications.

It makes no reading decisions. Every differing box must have its own supplied
decision and ink evidence; retaining the first reading requires an explicit
use_first flag. Only complete_audit.py applies the resulting adjudication.
"""
from pathlib import Path
import csv,json
E=Path(__file__).resolve().parents[1]

def read_rows(path):
    with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))

def write_adjudication(scan,reader,choices,page_edits=None,report_replace=None,report_append=None):
    stem=f'145_scan{scan:03d}'
    rows=read_rows(E/'second'/(stem+'_comparison.tsv'))
    assert set(choices)=={r['box'] for r in rows},'Every differing box needs its own explicit root decision'
    out=[]
    for row in rows:
        c=dict(choices[row['box']])
        assert c.get('adjudication') and c.get('ink')
        if c.pop('use_first',False):
            assert 'final' not in c and not c.get('changed',False)
            c['final']=row['first'];c['changed']=False
        else:
            assert 'final' in c and isinstance(c.get('changed'),bool)
        c['box']=row['box']
        c.setdefault('crop',f'crops/second_{stem}_{row["box"]}.png')
        assert (E/c['crop']).is_file(),c['crop']
        out.append(c)
    doc={'reader':reader,'main_reader_viewed_all_differing_crops':True,'differences':out,
         'page_edits':page_edits or [],'report_replace':report_replace or {},'report_append':report_append or {}}
    target=E/'second'/(stem+'_adjudication.json')
    assert not target.exists(),'Do not overwrite an adjudication record'
    target.write_text(json.dumps(doc,ensure_ascii=False,indent=2))
    return target
