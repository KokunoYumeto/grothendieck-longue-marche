from pathlib import Path
import csv,json,re,sys,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'result'
ORDER=(OUT/'page_order.txt').read_text().splitlines()
final='--final' in sys.argv
errors=[];warnings=[];stats={}
expected=list(csv.DictReader((ROOT/'source/SP83_C13_148+149_texts/MARKS.tsv').open(),delimiter='\t'))
actual=list(csv.DictReader((OUT/'decisions.tsv').open(),delimiter='\t'))
ids=[r['id'] for r in actual]
if len(set(ids))!=len(ids):errors.append('Duplicate mark decisions')
if final and ids!=[r['id'] for r in expected]:errors.append('decisions.tsv does not exactly cover MARKS.tsv in order')
pages=list((OUT/'pages').glob('*.tex'))
if final and {p.stem for p in pages}!=set(ORDER):errors.append('Final page set incomplete')
for p in pages:
    s=p.read_text();bal=0
    for line in s.splitlines():
        line=re.split(r'(?<!\\)%',line)[0]
        for m in re.finditer(r'(?<!\\)[{}]',line):
            bal+=1 if m[0]=='{' else -1
            if bal<0:errors.append(p.name+': closing brace without opener');break
    if bal:errors.append(p.name+f': brace imbalance {bal}')
    if len(re.findall(r'\\scanpage\{',s))!=1:errors.append(p.name+': unexpected scanpage count')
    r=json.loads((OUT/'records'/f'{p.stem}.json').read_text())
    reviewed=set(r.get('main_reader_crops',[]))
    for c in r.get('changes',[])+r.get('decisions',[]):
        crop=c.get('crop')
        mandatory=bool(c.get('diff_c') or c.get('diff_h') or c.get('decision') in ['first','alternative','other'])
        if mandatory and (not crop or crop=='page'):errors.append(p.stem+': no crop for '+c.get('id',c.get('place','')))
        if crop and crop!='page':
            if not (OUT/crop).exists():errors.append(p.stem+': crop missing '+crop)
            if mandatory and crop not in reviewed:warnings.append(p.stem+': main-reader crop not registered '+crop)
    if final:
        for suffix in ['boxes.tsv','first.tsv','second.tsv','comparison.json','adjudication.tsv']:
            if not (OUT/'second'/f'{p.stem}_{suffix}').exists():errors.append(p.stem+': missing independent audit '+suffix)
stats={'page_files':len(pages),'decisions':len(actual),'expected_decisions':len(expected),'crop_files':len(list((OUT/'crops').glob('*'))),'errors':errors,'warnings':warnings}
print(json.dumps(stats,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
