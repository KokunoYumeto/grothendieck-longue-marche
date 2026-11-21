from pathlib import Path
import csv,json,re,sys,hashlib
csv.field_size_limit(16 * 1024 * 1024)
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
        for i,char in enumerate(line):
            # A brace after a line-break command \\ is a real group opener;
            # only an odd run of preceding backslashes escapes it.
            n=0;j=i-1
            while j>=0 and line[j]=='\\':n+=1;j-=1
            if char=='%' and n%2==0:break
            if char in '{}' and n%2==0:
                bal+=1 if char=='{' else -1
                if bal<0:errors.append(p.name+': closing brace without opener');break
    if bal:errors.append(p.name+f': brace imbalance {bal}')
    environments=[]
    for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        if match[1]=='begin':environments.append(match[2])
        elif not environments or environments.pop()!=match[2]:
            errors.append(p.name+': unmatched environment '+match[0])
    if environments:errors.append(p.name+': unclosed environments '+str(environments))
    commands={m[1] for m in re.finditer(r'\\([A-Za-z]+|.)',s)}
    if commands.intersection({'uncertain','ill','struck','add','note'}):
        errors.append(p.name+': foreign witness macros remain')
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
        boxes_path=OUT/'second'/f'{p.stem}_boxes.tsv'
        second_path=OUT/'second'/f'{p.stem}_second.tsv'
        if boxes_path.exists() and second_path.exists():
            boxes=list(csv.DictReader(boxes_path.open(),delimiter='\t'))
            seconds=list(csv.DictReader(second_path.open(),delimiter='\t'))
            if [x['box'] for x in boxes]!=[x['box'] for x in seconds]:
                errors.append(p.stem+': independent reading does not cover boxes in order')
            for b in boxes:
                if not (OUT/'crops'/f"{p.stem}_second_{b['box']}.png").is_file():
                    errors.append(p.stem+': missing independent crop '+b['box'])
        audit=r.get('audit')
        if not audit:
            errors.append(p.stem+': independent audit not finalized')
        else:
            if audit.get('reader')==r.get('reader'):errors.append(p.stem+': first and second readers are identical')
            second_path=OUT/'second'/f'{p.stem}_second.tsv'
            if second_path.exists() and hashlib.sha256(second_path.read_bytes()).hexdigest()!=audit.get('second_reading_sha256'):
                errors.append(p.stem+': independent reading changed after adjudication')
            comparison_path=OUT/'second'/f'{p.stem}_comparison.json'
            adjudication_path=OUT/'second'/f'{p.stem}_adjudication.tsv'
            if comparison_path.exists() and adjudication_path.exists():
                comparison=json.loads(comparison_path.read_text())
                differing={x['box'] for x in comparison if not x['same_tokens']}
                adjudications=list(csv.DictReader(adjudication_path.open(),delimiter='\t'))
                if {x['box'] for x in adjudications}!=differing:errors.append(p.stem+': differing boxes not exactly adjudicated')
                if len(adjudications)!=len(differing):errors.append(p.stem+': duplicate adjudication rows')
                if any(x.get('main_reader_reviewed')!='yes' for x in adjudications):errors.append(p.stem+': unreviewed adjudication')
stats={'page_files':len(pages),'decisions':len(actual),'expected_decisions':len(expected),'crop_files':len(list((OUT/'crops').glob('*'))),'errors':errors,'warnings':warnings}
print(json.dumps(stats,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
