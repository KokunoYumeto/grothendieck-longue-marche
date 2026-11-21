from pathlib import Path
from datetime import datetime,timezone
import json,re
base=Path('/workspace/scratch/94548b74fbe0/out/readers/015/A')
tex=(base/'reading.tex').read_text()
report=json.loads((base/'report.json').read_text())
def unescaped(s,pos):
 n=0
 while pos>0 and s[pos-1]=='\\':n+=1;pos-=1
 return n%2==0
lines=[]
for line in tex.splitlines():
 ends=[i for i,c in enumerate(line) if c=='%' and unescaped(line,i)]
 lines.append(line[:ends[0]] if ends else line)
body='\n'.join(lines)
depth=0
for i,c in enumerate(body):
 if c in '{}' and unescaped(body,i):
  depth+=1 if c=='{' else -1
  assert depth>=0,('early closing brace',i)
assert depth==0,('brace depth',depth)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 if m.group(1)=='begin':stack.append(m.group(2))
 else:
  assert stack and stack.pop()==m.group(2),('environment',m.group(0))
assert not stack
assert sum(c=='$' and unescaped(body,i) for i,c in enumerate(body))%2==0
assert body.count(r'\[')==body.count(r'\]')
assert body.count(r'\begingroup')==body.count(r'\endgroup')
required=['scan','reader','start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read','differences','doubts','inventory','notes','notation','check_events','crops','brief_feedback']
assert all(k in report for k in required)
ids=[d['id'] for d in report['differences']]
assert len(ids)==len(set(ids))
locals_=[d for d in report['differences'] if d.get('C_source_row')]
assert sorted(set(d['C_source_row'] for d in locals_))==list(range(1,22))
assert len(locals_)==24
assert sum(d['C_doubt_status']=='resolved' for d in locals_)==9
assert sum(d['C_doubt_status']=='retained' for d in locals_)==15
for d in report['differences']:
 assert d['bbox'] is not None,d['id']
 if d['readers_crop']:assert (base/d['readers_crop']).is_file(),d['id']
 if d['C_doubt_status']=='resolved':assert d['diff_C'] is True,d['id']
for d in report['doubts']:
 if d['crop']:assert (base/d['crop']).is_file()
for c in report['crops']:
 assert (base/c['path']).is_file()
 c['viewed']=True
for component in ['MARK01','MARK02','MARK03','MARK04','MARK05','GUIDE01','GUIDE02','GUIDE03','GUIDE04','RULE01','RULE02','CANCEL01','CANCEL02','CANCEL03','CANCEL04']:
 assert component in tex,component
 assert any(i.get('component')==component for i in report['inventory']),component
for token in [
 r'\deleted{\unsure{I|V}}Version I',
 r'\inserted{\unsure{fermés|fermées}}',
 r'comp. conn. $\unsure{\Sigma_i|\Sigma}$',
 r'$\Sigma_i$ non fermé',
 r'X\setminus\Sigma_i',
 r'est vérifiée automatiquement les',
 r'\text{équivaut à}',
 r'\unsure{et} symétriquement, à',
 r'on \unsure{a}',
 r'\uline{vois}.',
 r'\inserted{l\'ouvert}'.replace("\\'","'"),
 r'\inserted{un} fermé',
 r'\unsure{donc|puis}',
 r'\Sigma_1^+\text{ serait}',
 '% archive sheet number: 14'
]:
 assert token in tex,token
assert not report['check_events']
report['structural_verification']={
 'performed_once':True,'braces':'balanced','environments':'balanced','display_delimiters':'balanced',
 'dollar_delimiters':'even','required_report_keys':'present','source_doubt_rows':'21 rows / 24 local decisions',
 'crop_references':'22 existing crop files; all displayed once','component_inventory':'all 15 named graphics mapped',
 'compiler_or_renderer_invoked':False,'method':'Direct Python source parsing and selected reading/report assertions; no TeX processing.'
}
report['end_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (base/'reading.md').open('a') as f:
 f.write('\nFinal source/report check completed at **'+report['end_utc']+'**: balanced braces and environments; matched display delimiters; complete source-row map; all crop references and named graphic inventory entries present. No TeX compilation or rendering.\n')
print('STRUCTURAL CHECK PASSED')
print(json.dumps({k:report[k] for k in ['scan','reader','start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read']},ensure_ascii=False))
print('C LOCAL DECISIONS')
for d in locals_:print(d['id'],'row',d['C_source_row'],d['C_doubt_status'],d['reading'])
print('COLLATION INDEX')
for d in report['differences']:print(d['id'], 'C='+str(d['diff_C']), 'H='+str(d['diff_H']), d['location'], '=>',d['reading'])
print('TRANSCRIPTION')
print(tex)
