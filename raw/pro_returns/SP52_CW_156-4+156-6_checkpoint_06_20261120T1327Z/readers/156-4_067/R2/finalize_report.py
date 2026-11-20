from pathlib import Path
import json,re,datetime
P=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_067/R2')
r=json.loads((P/'report.json').read_text())
tex=(P/'reading.tex').read_text()
by={d['id']:d for d in r['differences']}
by['R2-D009']['reading']=r'''\draw (12.95,.64) .. controls (12.85,.24) and (13.75,.45) .. (14.15,.45) .. controls (14.5,.47) and (14.6,.22) .. (14.65,-.06); \draw (14.08,.45) .. controls (14.18,.31) and (14.15,.23) .. (14.16,.15);'''
by['R2-D016']['reading']=r'''\draw (14.62,-1.37) .. controls (14.75,-1.58) and (14.15,-1.52) .. (13.1,-1.5) .. controls (10.2,-1.42) and (5.25,-1.24) .. (5.2,-1.94);'''
by['R2-D027']['reading']=r'''\draw[->] (3.12,.16) -- (3.75,.26);'''
by['R2-D033']['reading']=r'''\draw[line width=.7pt] (10.3,-1.1) -- (11.12,-1.1) -- (11.12,-.83); \draw (8.75,-1.24) .. controls (9.5,-1.11) and (9.95,-1.1) .. (10.1,-1.4) .. controls (10.18,-1.66) and (12.5,-1.64) .. (13.8,-1.85); \draw (10.43,-1.13) .. controls (10.05,-1.1) and (10.03,-1.7) .. (10.5,-1.71) .. controls (11.9,-1.75) and (13.4,-1.67) .. (14.1,-2.12);'''
by['R2-D059']['reading']=r'''\draw (4.03,.46) .. controls (4.01,.29) and (3.65,.12) .. (3.53,-.03);'''
by['R2-D067']['c']=r'''\deleted{\unsure{\phi|\Phi}}\qquad\deleted{\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi),\quad M'=\mathcal F'\cap M,}'''
by['R2-D067']['h']=(Path('/workspace/scratch/6644f30583f9/page_packets/156-4_067/H.tex').read_text().split('\n\n')[1])
# The preceding index is the cancelled paragraph in the supplied H witness.
assert by['R2-D067']['h'].startswith('\\struck{Donc')
by['R2-D067']['reading']=by['R2-D067']['c']
by['R2-D068']['reading']=r'''\node[anchor=base west] (familylabel) at (10.3,-1.0) {$\mathcal F'$}; \node[anchor=base west] (stable) at (10.35,-1.51) {\uline{Stable par Sup.}};'''
r['notes']['summary']='One handwritten subject-note page, numbered 66. Top definitions are followed by a cancelled attempt, a live brace with two marginal notes, double-prime definitions, reduction to constructions in M, and saturated-part definitions with a final pair. The top insertion enclosure, top continuation curve, left-note arrow, right-note enclosure, and M-zero insertion leader are reproduced in TikZ. Draft agreement was not treated as evidence.'
# Structural scanning only; this script invokes no TeX engine.
code='\n'.join(line.split('%')[0] for line in tex.splitlines())
stack=[]
for i,ch in enumerate(code):
 if ch not in '{}':continue
 q=i-1;n=0
 while q>=0 and code[q]=='\\':n+=1;q-=1
 if n%2:continue
 if ch=='{':stack.append(i)
 else:
  assert stack,('extra closing brace',i)
  stack.pop()
assert not stack,('unclosed braces',stack)
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',code):
 if m[1]=='begin':envs.append(m[2])
 else:assert envs and envs.pop()==m[2],m.group()
assert not envs
assert len(re.findall(r'(?<!\\)\\\[',code))==len(re.findall(r'(?<!\\)\\\]',code))
assert '\\cotefile' not in code and '\\illegible' not in code
assert '\\scanpage{67}\\mspage{66}' in code
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
req={'id','location','c','h','reading','scan_shows','confidence','kind','marked_in_h','change_c','change_h','crop','bbox','math_consequential'}
for d in r['differences']:
 assert req<=d.keys(),d['id']
 assert d['kind'] in kinds,(d['id'],d['kind'])
 assert d['confidence'] in {'high','medium','low'}
 assert d['marked_in_h'] in {'yes','no'}
 assert isinstance(d['change_c'],bool) and isinstance(d['change_h'],bool)
 assert isinstance(d['math_consequential'],bool)
 assert '...' not in d['reading'] and '\\cdots' not in d['reading'],d['id']
for d in r['differences']+r['c_doubts']:
 assert d['bbox_image'] in r['image_views']
 assert isinstance(d['bbox'],list) and len(d['bbox'])==4
 assert d['crop'] is None or Path(d['crop']).is_file()
for d in r['c_doubts']:assert d['status'] in {'resolved','retained','revised'}
for i in r['inventory']:
 assert i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
 assert i['sheet_kind']=='text' and i['hand']=='his hand' and i['transcribed']=='yes'
for c in r['crops']:assert Path(c['path']).is_file()
assert len(r['crops'])==18
assert len(r['image_views'])==3
assert r['check_events']==[]
r['structural_check']='Passed: balanced unescaped braces, matching begin/end environments, paired display delimiters, correct page markers, allowed report categories and complete fields, valid crop paths and original-image bbox sources. No LaTeX compiler or rendering used.'
r['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(P/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
log=P/'inspection_log.md'
log.write_text(log.read_text()+'\nFinal structural/schema check: balanced braces, matched environments and display delimiters, page markers, inventory/category values, evidence bboxes and crop paths verified. No TeX engine invoked. Report records 68 differences, 34 C dispositions, 41 inventory elements and 22 remaining doubts.\n')
print(json.dumps(dict(differences=len(r['differences']),c_doubts=len(r['c_doubts']),inventory=len(r['inventory']),remaining_doubts=len(r['remaining_doubts']),crops=len(r['crops']),status='structural and schema checks passed')))
