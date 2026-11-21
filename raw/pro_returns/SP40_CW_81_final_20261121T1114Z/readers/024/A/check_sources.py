from pathlib import Path
import re,json,hashlib
from datetime import datetime,timezone
root=Path('out/readers/024/A')
s=(root/'reading.tex').read_text();r=json.loads((root/'report.json').read_text());m=json.loads((root/'source_map.json').read_text());v=json.loads((root/'view_audit.json').read_text());md=(root/'reading.md').read_text()
clean='\n'.join(x.split('%',1)[0] for x in s.splitlines())
stack=[];bad=[]
for i,c in enumerate(clean):
 if c=='{' and (i==0 or clean[i-1]!='\\'):stack.append(i)
 if c=='}' and (i==0 or clean[i-1]!='\\'):
  if stack:stack.pop()
  else:bad.append(i)
assert not stack and not bad,(stack,bad)
envs=[]
for x in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 a,n=x.groups()
 if a=='begin':envs.append(n)
 else:assert envs.pop()==n
assert not envs
assert clean.count('\\[')==clean.count('\\]')==1
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
# Flag actual empty physical lines inside math delimiters.
math=False;display=False;blank=[]
for ln,line in enumerate(s.splitlines(),1):
 if not line.strip() and (math or display):blank.append(ln)
 line=line.split('%',1)[0]
 for q in re.finditer(r'\\\[|\\\]|(?<!\\)\$',line):
  if q.group()=='\\[':display=True
  elif q.group()=='\\]':display=False
  else:math=not math
assert not blank,blank
assert not math and not display
allowed={'scanpage','unsure','Pi','bigcup','in','setminus','begin','path','draw','fill','end','deleted','node','phantom','inserted','uline','forall','rlap','overset','text','Longleftrightarrow','overline','cap','ne','varnothing','figure','small','subset','Sigma','circ'}
macros=set(re.findall(r'\\([A-Za-z]+)',clean));assert not(macros-allowed),macros-allowed
h=hashlib.sha256(s.encode()).hexdigest();assert m['source_sha256']==h==r['provenance']['reading_tex_sha256']
for z in m['groups']+m['units']:
 p=z['source_span'];assert s[p['char_start']:p['char_end_exclusive']]==p['exact_tex']
 assert s.encode()[p['utf8_byte_start']:p['utf8_byte_end_exclusive']].decode()==p['exact_tex']
for z in m['literal_components']:
 p=z['source_span'];assert s[p['char_start']:p['char_end_exclusive']]==p['exact_tex']
for d in r['differences']:
 assert d['id'] in md,d['id']
 if d['readers_crop']:assert (root/d['readers_crop']).exists()
 for g in d['source_groups']:assert g in {x['id'] for x in m['groups']}
assert len(r['source_doubt_rows'])==18
assert {x['id'] for x in r['source_doubt_rows']}=={f'C024-R{i:02}' for i in range(1,19)}
assert r['counts']['C_rows_resolved']==2 and r['counts']['C_rows_retained']==16
assert all(x['transcribed']=='yes' for x in r['inventory'])
assert all(x['source_refs'] for x in r['inventory'])
assert len(v['events'])==29
assert len({x['path'] for x in v['events']})==29
assert all(x['result']=='successful_delivery' for x in v['events'])
assert v['view_counts']=={'whole_successful':1,'half_a_successful':1,'half_b_successful':1,'local_crops_successful':26,'failed_unseen_deliveries':0,'reopens':0}
assert r['check_events']==[]
assert any(x['id']=='D47' and x['marked_in_H'] for x in r['differences'])
assert sum(x['marked_in_H'] for x in r['differences'])==1
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(x['kind'] in kinds for x in r['differences']),[(x['id'],x['kind']) for x in r['differences'] if x['kind'] not in kinds]
# Literal witness quotation check: do not rewrite mathematical source syntax.
cw=Path('packets/024/C.tex').read_text();hw=Path('packets/024/H.tex').read_text()
for d in r['differences']:
 for w,t in [('C',cw),('H',hw)]:
  if d[w] is not None:assert d[w] in t,(d['id'],w,d[w])
result={'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'brace_balance':'pass','environment_balance':'pass','display_delimiters':'one matched pair','inline_math_delimiters':'even and no unmatched running state','blank_physical_lines_inside_math':blank,'macro_allowlist':'pass','source_span_checks':'all unit, group and literal component excerpts match exact current source','literal_witness_quotes':'all non-null C/H quotations are exact substrings of their supplied source files','check_history':'Initial source checker allowlist omitted standard circ; checker corrected without a transcription change.','report_reading_hash_consistency':'pass','doubt_row_coverage':'18 of 18; 2 resolved, 16 retained','crop_references':'all exist','view_audit':'29 unique successful deliveries; no failure and no reopen','inventory_coverage':'49 rows yes, each with exact source references','check_events':'empty; no mathematical check performed','compile_render':'neither performed'}
r['source_checks']=result
r['provenance']['view_audit_sha256']=hashlib.sha256((root/'view_audit.json').read_bytes()).hexdigest()
r['provenance']['reading_md_sha256']=hashlib.sha256((root/'reading.md').read_bytes()).hexdigest()
r['provenance']['crop_hashes']=[{'path':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(root.glob('*.png'))]
r['confirmed_source_choices']=[
 {'reading':'second Considérons la','evidence':'crop04, separate rising accent at e','source_unit':'P1'},
 {'reading':'Cette relation fait de','evidence':'half a and crop09; apparent endpoint point is final letter return, no added punctuation','source_unit':'P2'},
 {'reading':'first exactement','evidence':'half b, physical full-scan region [339,1467,679,1556]','source_unit':'P4'},
 {'reading':'caractérisé','evidence':'half b; both local acute positions read as rising strokes','source_unit':'P4'},
 {'reading':'l’ens de ces deux U_s.','evidence':'half b; no abbreviation point after ens, endpoint period after U_s','source_unit':'P4'},
 {'reading':'final U_s-minus subset Sigma_i-minus','evidence':'crop24; independent distinct i dot and firm minus, joined head','source_unit':'P5'},
 {'reading':'final barred U_s-minus cap E_i notempty','evidence':'crop22; existing bar, clear index dot, clear minus, visible gap from pour descender','source_unit':'P5'}]
(root/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,indent=2));print('Source components:',len(m['literal_components']),'wrappers:',len(m['uncertainty_and_state_wrappers']))
