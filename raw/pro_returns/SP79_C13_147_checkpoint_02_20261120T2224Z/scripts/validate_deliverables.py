"""Structural validation of the supplied-data transcription apparatus; no TeX build."""
from pathlib import Path
from collections import Counter
import csv,json,re,sys,hashlib
from build_reports import ROOT,ORDER,PREFIX
final='--final' in sys.argv
errors=[];warnings=[]
def readtab(p,delimiter='\t'):
    with p.open() as f:return list(csv.DictReader(f,delimiter=delimiter))
reports=[]
for n in ORDER:
    stem=f'147_scan{n:03d}';p=ROOT/'pages'/f'{stem}.tex';rp=ROOT/'adjudicated'/f'{stem}.json'
    if not p.exists() or not rp.exists():
        if final:errors.append(f'{stem}: missing final page or adjudication report')
        continue
    r=json.loads(rp.read_text());reports.append(r);s=p.read_text()
    if not r.get('main_reader_reviewed'):errors.append(f'{stem}: lacks main-reader approval')
    if f'\\scanpage{{{n}}}' not in s:errors.append(f'{stem}: incorrect scan marker')
    if re.search(r'\\(?:uncertain|struck|ill|note|documentclass|usepackage)\b',s):errors.append(f'{stem}: foreign witness or preamble macro')
    depth=0
    for line in s.splitlines():
        line=re.split(r'(?<!\\)%',line)[0]
        for match in re.finditer(r'(?<!\\)[{}]',line):
            depth+=1 if match.group()=='{' else -1
            if depth<0:errors.append(f'{stem}: unmatched closing brace');break
    if depth:errors.append(f'{stem}: unbalanced braces {depth}')
    envs=[]
    for action,env in re.findall(r'\\(begin|end)\{([^}]+)\}',s):
        if action=='begin':envs.append(env)
        elif not envs or envs.pop()!=env:errors.append(f'{stem}: mismatched environment {env}')
    if envs:errors.append(f'{stem}: unclosed environments {envs}')
    for c in r.get('changes',[])+r.get('decisions',[]):
        if c.get('crop') and c['crop']!='page' and not (ROOT/c['crop']).exists():errors.append(f'{stem}: missing crop {c["crop"]}')
        if c.get('confidence') not in ('high','medium','low'):errors.append(f'{stem}: invalid confidence')
    for d in r.get('decisions',[]):
        if d['decision'] not in ('first','alternative','other','undecided'):errors.append(f'{stem}: invalid decision {d["id"]}')
        if d['decision']!='undecided' and (not d.get('crop') or d['crop']=='page'):errors.append(f'{stem}: resolved mark without crop {d["id"]}')
    for i in r.get('inventory',[]):
        if i.get('transcribed')!='yes':errors.append(f'{stem}: untranscribed inventory element')
        if i.get('kind') not in ('text','display','diagram','drawing','margin note','insertion','deletion'):errors.append(f'{stem}: invalid inventory kind {i.get("kind")}')
    if r.get('sheet_kind','text') not in ('text','reused_typed','typescript','letter','list','cancelled_draft','cover'):errors.append(f'{stem}: invalid sheet kind')
    allowed_collation=('misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other')
    for c in r.get('changes',[]):
        if c.get('against_H') and c.get('kind') not in allowed_collation:errors.append(f'{stem}: invalid collation kind {c.get("kind")}')
    if final:
        for suffix in ('boxes.tsv','first.tsv','second.tsv','comparison.json','token_adjudication.tsv'):
            if not (ROOT/'second'/f'{stem}_{suffix}').exists():errors.append(f'{stem}: missing {suffix}')
        if not r.get('audit_completed'):errors.append(f'{stem}: blind audit not adjudicated')
        if not r.get('second_reader'):errors.append(f'{stem}: missing second-reader identity')
        if r.get('second_reader')==r.get('reader'):errors.append(f'{stem}: same first and second reader')
        comparison=ROOT/'second'/f'{stem}_comparison.json'
        if comparison.exists():
            cmp=json.loads(comparison.read_text())
            expected_boxes={x['box'] for x in cmp['items']}
            actual_boxes=[x['box'] for x in r.get('audit_decisions',[])]
            if set(actual_boxes)!=expected_boxes or len(actual_boxes)!=len(set(actual_boxes)):
                errors.append(f'{stem}: adjudication rows do not cover every differing blind box exactly once')
            for a in r.get('audit_decisions',[]):
                if not a.get('ink'):errors.append(f'{stem}: blind adjudication lacks visual evidence {a["box"]}')
                if not a.get('crop') or not (ROOT/a['crop']).exists():errors.append(f'{stem}: blind adjudication lacks crop {a["box"]}')
                item=next((x for x in cmp['items'] if x['box']==a['box']),None)
                covered=[i for v in a.get('token_resolutions',[]) for i in v.get('operations',[])]
                if item and sorted(covered)!=list(range(len(item['token_differences']))):
                    errors.append(f'{stem}: incomplete token-operation adjudication {a["box"]}')
if final:
    commitment=ROOT/'second/FIRST_READING_SHA256.tsv'
    if not commitment.exists():errors.append('missing pre-blind commitment')
    else:
        for row in readtab(commitment):
            if hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()!=row['sha256']:
                errors.append(f'pre-blind committed file changed: {row["path"]}')
ds=readtab(ROOT/'decisions.tsv')
if len({d['id'] for d in ds})!=len(ds):errors.append('duplicate decisions')
source=ROOT.parents[1]/'source/SP79_C13_147_texts/MARKS.tsv'
with source.open() as f:marks=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
expected=[m['id'] for m in marks if int(m['scan']) in {r['scan'] for r in reports}]
if [d['id'] for d in ds]!=expected:errors.append('decisions IDs/order differ from supplied MARKS.tsv')
actual=(ROOT/f'{PREFIX}_transcription.tex').read_text()
expected_combined='\\cotefile{147}\n\n'+'\n\n'.join((ROOT/'pages'/f'147_scan{r["scan"]:03d}.tex').read_text().rstrip() for r in reports)+'\n'
if actual!=expected_combined:errors.append('combined fragment differs from page files')
res={'status':'pass' if not errors else 'fail','mode':'final' if final else 'in progress','pages':len(reports),'decisions':len(ds),'errors':errors,'warnings':warnings,'latex_compiled':False,'ocr_used':False}
(ROOT/'VALIDATION.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res,ensure_ascii=False))
if errors:sys.exit(1)
