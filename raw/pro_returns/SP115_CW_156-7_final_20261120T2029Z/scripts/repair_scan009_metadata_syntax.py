from pathlib import Path
import csv, io, json, hashlib, datetime
R=Path('/workspace/scratch/ddf8babdc42e/out')
P=R/'pages/H156-01_156-7_scan009.tex'
D=R/'second/H156-01_156-7_scan009_decisions.json'
A=R/'second/H156-01_156-7_scan009_adjudication.tsv'
J=R/'review/scan009_final.json'
S=R/'scripts/decide_blind009.py'
old=r'\LongrightarrowZ';new=r'\Longrightarrow Z'
page=P.read_text();dec=json.loads(D.read_text());data=json.loads(J.read_text())
assert page.count(old)==1
page=page.replace(old,new,1)
assert dec['boxes']['B007']['final'].count(old)==1
dec['boxes']['B007']['final']=dec['boxes']['B007']['final'].replace(old,new,1)
key=r'\unsure{Z^{+}\leq L|Z+\leq L|Z\leq L}'
patch=next(x for x in dec['patches'] if x['old']==key)
assert patch['new']==r'Z^{+}\leq L'
patch['new']=r' Z^{+}\leq L'
audit_entry=next(x for x in data['audit_changes'] if x['box']=='B007')
assert audit_entry['final'].count(old)==1
audit_entry['final']=audit_entry['final'].replace(old,new,1)
for rows in (data['changes'],dec['new_changes']):
 for id in ('009-87','009-88'):
  row=next(x for x in rows if x['id']==id)
  assert row['kind']=='omitted text'
  row['kind']='omission'
ab=A.read_bytes()
assert ab.count(old.encode())==1
ab_new=ab.replace(old.encode(),new.encode(),1)
before_rows=list(csv.DictReader(io.StringIO(ab.decode()),delimiter='\t'))
after_rows=list(csv.DictReader(io.StringIO(ab_new.decode()),delimiter='\t'))
for b,a in zip(before_rows,after_rows):
 if b['box']=='B007':
  assert a['final']==b['final'].replace(old,new,1)
  assert all(a[k]==b[k] for k in b if k!='final')
 else:assert a==b
s=S.read_text()
old_line="patch(r'"+key+"',r'Z^{+}\\leq L')"
new_line="patch(r'"+key+"',r' Z^{+}\\leq L')"
assert s.count(old_line)==1
s=s.replace(old_line,new_line,1)
for id in ('009-87','009-88'):
 lines=s.splitlines(keepends=True)
 idx=next(i for i,line in enumerate(lines) if "'"+id+"'" in line and "'omitted text'" in line)
 assert lines[idx].count("'omitted text'")==1
 lines[idx]=lines[idx].replace("'omitted text'","'omission'",1)
 s=''.join(lines)
initial=(R/'second/H156-01_156-7_scan009_initial.tex').read_text()
expected=initial
for p in dec['patches']:
 assert expected.count(p['old'])==p.get('count',1),(p['old'],expected.count(p['old']),p.get('count'))
 expected=expected.replace(p['old'],p['new'])
assert expected==page,'Page does not equal frozen initial plus current recorded patches'
P.write_text(page);D.write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n');J.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');A.write_bytes(ab_new);S.write_text(s)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (P,D,A,J,S)}
report={'completed_utc':now,'authorization':'Root exact non-ink schema correction and exact TeX separator repair','repairs':[{'old':old,'new':new,'locations':['current page','adjudication B007.final','decisions.boxes.B007.final','review.audit_changes B007.final']},{'old':r'Z^{+}\leq L','new':r' Z^{+}\leq L','locations':['decisions replacement for the old Z-plus uncertainty','same literal replacement argument in decide_blind009.py']},{'old':'omitted text','new':'omission','ids':['009-87','009-88'],'locations':['review changes kinds','decisions new_changes kinds','script literal tuples']}],'page_equals_frozen_initial_plus_recorded_patches':True,'apply_script_rerun':False,'K_changed':False,'after_hashes_at_repair':hashes}
(R/'review/scan009_syntax_schema_repair.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (R/'progress.log').open('a') as f:f.write('scan009 exact syntax/schema repair '+now+': Longrightarrow-Z separator synchronized in current page, B007 audit final and decision override; recorded Z-plus patch/script replacement now begins with a space; 009-87/88 kinds omitted text -> omission in final JSON/decisions/script. No apply rerun, no K change. Page equals frozen initial plus recorded patch sequence. Page SHA256 '+hashes[str(P.relative_to(R))]+'. Full repair record review/scan009_syntax_schema_repair.json\n')
print(json.dumps({'page_sha256':hashes[str(P.relative_to(R))],'page_matches_patches':True,'K_changed':False,'report':'out/review/scan009_syntax_schema_repair.json'},indent=2))
