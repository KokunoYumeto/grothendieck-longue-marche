"""Required source-only structural/record audit; no rendering or image reads."""
from pathlib import Path
import json, re

base=Path(__file__).parent
tex=(base/'reading.tex').read_text()
report=json.loads((base/'report.json').read_text())
body='\n'.join(line.split('%',1)[0] for line in tex.splitlines())
depth=0
for pos,ch in enumerate(body):
    if ch in '{}':
        backslashes=0
        q=pos-1
        while q>=0 and body[q]=='\\':
            backslashes+=1
            q-=1
        if backslashes%2:
            continue
        depth+=1 if ch=='{' else -1
        assert depth>=0, ('unmatched closing brace',pos)
assert depth==0, ('brace depth',depth)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    if m.group(1)=='begin':
        stack.append(m.group(2))
    else:
        assert stack and stack.pop()==m.group(2), ('environment mismatch',m.group(0))
assert not stack
assert body.count('\\[')==body.count('\\]')==5
assert body.count('\\(')==body.count('\\)')==1
for display in re.findall(r'\\\[([\s\S]*?)\\\]',body):
    assert not re.search(r'\n\s*\n',display)
assert r'\cotefile' not in body
assert body.count(r'\scanpage{19}')==1
assert '% archive sheet number: 18' in tex
assert len(re.findall(r'\\draw\[',body))==11
allowed={'scanpage','operatorname','unsure','geqslant','figure','mathord','begin','end','coordinate','path','draw','cap','Sigma','underset','phantom','text','cdot','setminus','mathop','limits','alpha','in','deleted','widehat','left','right','subset','qquad','forall','pi','cup','bigcup','not'}
commands=set(re.findall(r'\\([A-Za-z]+)',body))
assert commands<=allowed, commands-allowed
for fragment in [r'\unsure{avec}',r'les ens.',r'\unsure{on a}',r'\deleted{\unsure{J|j}}K_0',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',r'\unsure{On a|\deleted{On}On a}',r'\unsure{dernier|deuxième}',r'\deleted{\unsure{somme|réunion}}',r'\unsure{à|:} sommer',r'$K_1$ cet ens.',r"\text{\unsure{l'une|l'un}}"]:
    assert fragment in tex,fragment
assert len(report['source_C_doubt_rows'])==12
assert [r['id'] for r in report['source_C_doubt_rows']]==[f'R{i:02}' for i in range(1,13)]
assert sum(r['status']=='resolved' for r in report['source_C_doubt_rows'])==3
assert sum(r['status']=='retained' for r in report['source_C_doubt_rows'])==9
ids={d['id'] for d in report['differences']}
for row in report['source_C_doubt_rows']:
    assert set(row['local_decision_ids'])<=ids
for d in report['differences']:
    assert d['H'] is not None
    if d['readers_crop']:
        assert (base/d['readers_crop']).is_file()
for c in report['crops']:
    assert (base/c['path']).is_file() and c['successful_deliveries']==1 and c['viewed']
assert len(report['image_ledger'])==17
assert len({x['path'] for x in report['image_ledger']})==17
assert all(x['successful_deliveries']==1 for x in report['image_ledger'])
assert report['counts']['diff_C']==sum(d['diff_C'] for d in report['differences'])==9
assert report['counts']['diff_H']==sum(d['diff_H'] for d in report['differences'])==14
assert report['S_page_scope']['id']=='SA01-K81-06'
result={'source_only':True,'braces':'balanced','environments':'balanced','display_pairs':5,'inline_math_pairs':1,'literal_draw_paths':11,'allowed_commands':'pass','crop_references':'exist','source_C_rows':'12/12, 3 resolved, 9 retained','image_ledger':'17 distinct delivered images; each once','reading_report_selected_fragments':'pass','compilation_or_rendering':False,'image_reads_in_audit':0}
(base/'source_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
