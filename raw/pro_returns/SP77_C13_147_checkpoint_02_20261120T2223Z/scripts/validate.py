"""Integrity checks only; this is not a substitute for visual reading."""
from pathlib import Path
from PIL import Image
import csv,json,re,sys,hashlib
W=Path(__file__).resolve().parents[1];I=W.parent/'inputs';full='--complete' in sys.argv
scans=[24,26,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,50,52,53]
errors=[];summary=[]
for n in scans:
    p=W/'pages'/f'147_scan{n:03d}.tex'
    if not p.exists():
        if full:errors.append(f'missing page {n}')
        continue
    r=json.loads((W/'records'/p.with_suffix('.json').name).read_text());t=p.read_text()
    if not r.get('main_review'):errors.append(f'{n}: no main visual review')
    if not all(r['coverage'].get(k) for k in ['whole_viewed','all_tokens_read','all_deletions_insertions_checked']):errors.append(f'{n}: incomplete first-reading coverage')
    if f'\\scanpage{{{n}}}' not in t:errors.append(f'{n}: scan marker')
    braces=0
    for token in re.findall(r'\\[{}]|[{}]',re.sub(r'(?m)(?<!\\)%.*$','',t)):
        braces+=1 if token=='{' else -1 if token=='}' else 0
        if braces<0:errors.append(f'{n}: closing brace precedes opener');break
    if braces:errors.append(f'{n}: unbalanced braces {braces}')
    dims=Image.open(I/f'SP77_C13_147_scans/147_scan{n:03d}.jpg').size
    for c in r['changes']:
        if not (c['diff_C'] or c['diff_H']):errors.append(f'{n}: redundant change {c["id"]}')
        if c['confidence'] not in ['high','medium','low']:errors.append(f'{n}: bad confidence')
        if not (W/c['crop']).is_file():errors.append(f'{n}: missing crop {c["crop"]}')
        if len(c['box'])!=4:errors.append(f'{n}: invalid box')
    ids=[]
    for b in r['boxes']:
        ids.append(b['box']);a,c,d,e=[b[k] for k in ['x0','y0','x1','y1']]
        if not (0<=a<d<=dims[0] and 0<=c<e<=dims[1]):errors.append(f'{n}: outside image {b["box"]}')
    if len(ids)!=len(set(ids)):errors.append(f'{n}: duplicate box')
    if any(e['transcribed']!='yes' for e in r['inventory']):errors.append(f'{n}: incomplete inventory')
    with (W/'second'/f'147_scan{n:03d}_first.tsv').open() as f:first=list(csv.DictReader(f,delimiter='\t'))
    if [x['box'] for x in first]!=ids:errors.append(f'{n}: first-reading box order mismatch')
    if full:
        for suffix in ['_second.tsv','_comparison.tsv','_reconciliation.tsv']:
            if not (W/'second'/f'147_scan{n:03d}{suffix}').exists():errors.append(f'{n}: missing {suffix}')
        if not r.get('audit'):errors.append(f'{n}: missing audit decision')
        elif r['audit']['reader']==r['reader']:errors.append(f'{n}: same first/second reader')
        base=W/'second'/f'147_scan{n:03d}'
        meta_path=Path(str(base)+'_comparison_metadata.json')
        reader_path=Path(str(base)+'_second_reader.json')
        if not meta_path.exists() or not reader_path.exists():
            errors.append(f'{n}: missing independent-reading provenance')
        else:
            cm=json.loads(meta_path.read_text());rm=json.loads(reader_path.read_text())
            if rm.get('no_previous_reading') is not True:errors.append(f'{n}: blind-reader independence not recorded')
            if rm.get('reader','').split('/')[-1]==r['reader'].split('/')[-1]:errors.append(f'{n}: same reader identity')
            for suffix,key in [('_first.tsv','first_sha256'),('_second.tsv','second_sha256')]:
                fp=Path(str(base)+suffix)
                if fp.exists() and hashlib.sha256(fp.read_bytes()).hexdigest()!=cm[key]:errors.append(f'{n}: {suffix} changed after comparison')
            if r.get('audit') and r['audit']['second_sha256']!=cm['second_sha256']:errors.append(f'{n}: second-reading audit hash mismatch')
            for crop in rm.get('crop_files',[]):
                if not (W/crop).exists():errors.append(f'{n}: missing blind crop {crop}')
            if len(rm.get('crop_files',[]))!=len(ids):errors.append(f'{n}: independent crop count differs from box count')
    summary.append({'scan':n,'changes':len(r['changes']),'crops':len(r['crop_files']),'boxes':len(ids),'doubts':len(r['doubts'])})
with (I/'SP77_C13_147_texts/MARKS.tsv').open() as f:expected=[x['id'] for x in csv.DictReader(f,delimiter='\t') if full or (W/'pages'/f'147_scan{int(x["scan"]):03d}.tex').exists()]
with (W/'decisions.tsv').open() as f:got=[x['id'] for x in csv.DictReader(f,delimiter='\t')]
if expected!=got:errors.append('decisions do not exactly match supplied MARKS order')
print(json.dumps({'complete_required':full,'pages':len(summary),'summary':summary,'errors':errors},ensure_ascii=False))
if errors:sys.exit(1)
