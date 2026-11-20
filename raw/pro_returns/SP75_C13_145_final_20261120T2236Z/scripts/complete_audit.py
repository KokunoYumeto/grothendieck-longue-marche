"""Apply explicit root adjudications after every differing second-reading crop was inspected."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,subprocess,sys,re
E=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]);stem=f'145_scan{scan:03d}';D=E/'second'
def read(p):
 with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
boxes=read(D/(stem+'_boxes.tsv'));comparison=read(D/(stem+'_comparison.tsv'))
a=json.loads((D/(stem+'_adjudication.json')).read_text())
assert a['main_reader_viewed_all_differing_crops'] is True
assert [x['box'] for x in a['differences']]==[x['box'] for x in comparison]
coords={b['box']:[int(b[k]) for k in ['x0','y0','x1','y1']] for b in boxes}
for x,c in zip(a['differences'],comparison):
 assert x['adjudication'] and x['adjudication']!='PENDING' and x['ink'] and x['final']
 assert isinstance(x['changed'],bool) and (E/x['crop']).is_file()
 x.update(first=c['first'],second=c['second'],coords=coords[x['box']])
 c.update(adjudication=x['adjudication'],final=x['final'],ink=x['ink'])
page=E/'pages'/(stem+'.tex');text=page.read_text()
for e in a.get('page_edits',[]):
 assert text.count(e['old'])==e.get('count',1),(e['old'],text.count(e['old']))
 text=text.replace(e['old'],e['new'])
assert len(re.findall(r'(?<!\\)\$',text))%2==0,'Unpaired inline math delimiter after adjudication edits'
rpath=E/'reader_reports'/(stem+'_reviewed.json');r=json.loads(rpath.read_text())
assert 'audit' not in r,'Refusing to repeat a completed audit'
assert a['reader'].split('/')[-1]!=r['reader'].split('/')[-1],'The blind second reader must differ from the first reader'
assert not (a['reader'].split('/')[-1]=='reader_b' and scan in [25,26,27]),'Reader excluded by accidental difference-list exposure'
assigned=json.loads((D/(stem+'_audit_assignment.json')).read_text())
assert assigned['reader'].split('/')[-1]==a['reader'].split('/')[-1]
for k,v in a.get('report_replace',{}).items():r[k]=v
for k,v in a.get('report_append',{}).items():r.setdefault(k,[]).extend(v)
r['audit']={'reader':a['reader'],'boxes_read':len(boxes),'differences':a['differences']}
page.write_text(text);rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2))
with (D/(stem+'_comparison.tsv')).open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['box','kind','first','second','differing_token_spans','adjudication','final','ink'],delimiter='\t');w.writeheader();w.writerows(comparison)
subprocess.run([sys.executable,str(E/'scripts/build_edition.py')],check=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (E/'progress.log').open('a') as f:f.write(f"scan {scan:03d} audited {now}: {len(boxes)} boxes read, {len(comparison)} differences, {sum(x['changed'] for x in a['differences'])} changed\n")
print(stem+' audited '+now)
