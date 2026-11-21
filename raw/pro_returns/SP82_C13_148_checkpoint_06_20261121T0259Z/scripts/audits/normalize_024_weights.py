#!/usr/bin/env python3
"""Normalize scan024's embedded graphic weights, without changing readings.

Run once after its recorded audit. Coordinate radii, labels, geometry, confidence,
choices, first/second readings and audit/count fields remain unchanged.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re

B=Path(__file__).resolve().parents[2]
page=B/'pages/148_scan024.tex'
rp=B/'reviews/148_scan024.json'
ap=B/'second/148_scan024_adjudications.json'
tp=B/'second/148_scan024_adjudication.tsv'
log=B/'reviews/148_scan024_weight_normalization.json'
assert not log.exists(), 'Non-idempotent: normalization already logged.'
protected=[B/f'second/148_scan024_{s}.tsv' for s in ['first','second','comparison','token_differences']]
digest=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
before={q.name:digest(q) for q in protected}
page_before=digest(page)
t=page.read_text();p=json.loads(rp.read_text());es=json.loads(ap.read_text())
with tp.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
unchanged_columns=[{k:v for k,v in r.items() if k!='final'} for r in rows]
audit_counts={k:p['second_audit'][k] for k in ['boxes','differences','changed']}
change_counts=(len(p['changes']),sum(r['against_c'] for r in p['changes']),sum(r['against_h'] for r in p['changes']))
with (B/'second/148_scan024_second.tsv').open() as f:
    second={r['box']:r['reading'] for r in csv.DictReader(f,delimiter='\t')}
scopes=re.findall(r'\\begin\{scope\}[^\n]*\n.*?\\end\{scope\}',t,re.S)
assert len(scopes)==15 and all(r'\pgflinewidth' not in s.split('\n')[0] for s in scopes)
updates=[]
for k,tr in p['blind_graphic_transforms'].items():
    x0,y0,x1,y1=tr['native_box']
    yshift=y1 if k=='S24-diamond_formulas' else y0
    prefix=f'\\begin{{scope}}[shift={{({x0},{yshift})}}'
    found=[s for s in scopes if s.startswith(prefix)];assert len(found)==1,k
    old=found[0];head=old.split('\n',1)[0]
    numerator,denominator=re.search(r'xscale=\{([0-9]+)/([0-9]+)\}',head).groups()
    native_scale=int(numerator)/int(denominator)
    base=float(re.search(r'\[x=([0-9.]+)cm',second[k]).group(1))
    ratio=.007*native_scale/base
    def pt(m):return f'{float(m.group(1))*ratio:.6f}'.rstrip('0').rstrip('.')+'pt'
    new=re.sub(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt',pt,old)
    newhead=head[:-1]+f',line width={ratio:.8f}\\pgflinewidth]'
    new=new.replace(head,newhead,1)
    t=t.replace(old,new,1)
    n_changes=n_json=n_tsv=n_audit=0
    for r in p['changes']:
        n_changes+=old in r['final'];r['final']=r['final'].replace(old,new)
    for e in es:
        if 'final' in e:
            n_json+=old in e['final'];e['final']=e['final'].replace(old,new)
    for r in rows:
        n_tsv+=old in r['final'];r['final']=r['final'].replace(old,new)
    for r in p['second_audit']['changes']:
        n_audit+=old in r['final'];r['final']=r['final'].replace(old,new)
    assert n_changes and n_json==1 and n_tsv==1 and n_audit==1,(k,n_changes,n_json,n_tsv,n_audit)
    tr.update(source_base_x_cm=base,target_base_x_cm=.007,physical_size_ratio=ratio)
    updates.append(dict(box=k,native_coordinate_scale=native_scale,source_base_x_cm=base,
        physical_size_ratio=ratio,updated_changes_final_values=n_changes))
assert [ {k:v for k,v in r.items() if k!='final'} for r in rows]==unchanged_columns
assert {k:p['second_audit'][k] for k in audit_counts}==audit_counts
assert (len(p['changes']),sum(r['against_c'] for r in p['changes']),sum(r['against_h'] for r in p['changes']))==change_counts
assert t.count(r'\pgflinewidth')==15
page.write_text(t);rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
ap.write_text(json.dumps(es,ensure_ascii=False,indent=2)+'\n')
with tp.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
after={q.name:digest(q) for q in protected};assert before==after
log.write_text(json.dumps(dict(utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    purpose='Mechanical physical stroke normalization only; no new ink reading or audit decision.',
    formula='(.007 cm * local native coordinate scale) / blind second base x unit',
    scaled='Explicit pt stroke widths, radii and dash intervals; inherited default width.',
    unchanged='Coordinate-unit radii, geometry, labels, readings, confidence, choices, change and audit counts.',
    audit_counts=audit_counts,change_counts=dict(rows=change_counts[0],against_c=change_counts[1],against_h=change_counts[2]),
    protected_sha256=after,page_sha256_before=page_before,page_sha256_after=digest(page),scopes=updates),
    ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scopes=len(updates),protected_hashes_unchanged=before==after,audit_counts=audit_counts,change_counts=change_counts)))
