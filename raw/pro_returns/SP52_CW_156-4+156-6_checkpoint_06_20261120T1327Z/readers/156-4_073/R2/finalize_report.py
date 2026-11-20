from pathlib import Path
import json,re
from datetime import datetime,timezone
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R2')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_073')
C=(packet/'C.tex').read_text();H=(packet/'H.tex').read_text()
r=json.loads((root/'report.json').read_text())
by={d['id']:d for d in r['differences']}
d=by['D21']
d['c']=C[C.index(r'\deleted{\deleted{\uline'):C.index('\n\n\\deleted{\\inserted')]
start=H.index(r'\struck{\ill{}} Soient')
d['h']=H[start:H.index(' Considérons les',start)]
d['reading']=r'R2-FIG-DRAFT: crossed heading and Soient $F,\deleted{A}G$ deux figures.'
d['scope_note']='The two witness strings quote the corresponding opening state excerpt only. The broad state comparison includes the following draft body through the C6 line; individual local readings and the final C7 line are accounted separately. No witness paragraph boundary is silently changed.'
d=by['D30']
d['location']='Lower a: first order chain on its own display line'
d['c']=r"\["+'\n'+r"\deleted{G\leq F'\preceq F}"+'\n'+r"\]"
d['h']=r"$G \leq F' \preccurlyeq F$"
d['reading']=r"\[G\leq F'\preceq F\] in R2-FIG-DRAFT"
d['scan_shows']='The first chain stands on its own centered line below condition a. Its symbols otherwise agree with both witnesses.'
d['bbox']=[675,700,1100,795]
d2=dict(d)
d2.update({'id':'D38','location':'Lower b: second order chain on its own display line','c':r'\['+'\n'+r"\deleted{G\preceq G'\leq F.}"+'\n'+r'\]','h':r"$G \preccurlyeq G' \leq F$.",'reading':r"\[G\preceq G'\leq F.\] in R2-FIG-DRAFT",'scan_shows':'The second chain stands separately below condition b and has its own final point. Its symbols otherwise agree.','bbox':[675,930,1120,1010]})
r['differences'].append(d2)
whole,a,b=r['image_views'];crops={i+1:c for i,c in enumerate(r['crops'])}
def ev(n):return {'source':crops[n]['source'],'bbox':crops[n]['bbox'],'crop':crops[n]['path']}
doubts={d['id']:d for d in r['c_doubts']}
doubts['C27']['evidence_loci']=[ev(1),ev(2),{'source':a,'bbox':[280,320,1675,650],'crop':None},ev(9),ev(13),{'source':b,'bbox':[675,700,1120,1010],'crop':None},ev(16)]
doubts['C28']['evidence_loci']=[{'source':a,'bbox':[280,320,460,450],'crop':None},{'source':a,'bbox':[1520,1140,1665,1255],'crop':None},ev(11),ev(17)]
# The same graphic references used in the doubts must exist in the fragment.
tex=(root/'reading.tex').read_text()
refs=['R2-FIG-PARENTHESIS','R2-MARK-BEFORE-C7','R2-FIG-DRAFT','R2-INSERTION-ENCLOSURE','R2-CLOSING-TICK','R2-DIAG-SQUARE']
assert all(x in tex for x in refs)
# Exact source snippets only; formula excerpts differ from surrounding prose only in scope.
for d in r['differences']:
 for key,w in [('c',C),('h',H)]:
  assert not d[key] or d[key] in w,(d['id'],key,d[key])
# Structural checks only, never TeX compilation.
clean='\n'.join(line.split('%')[0] for line in tex.splitlines())
stack=[]
for i,ch in enumerate(clean):
 if ch not in '{}':continue
 n=0;j=i-1
 while j>=0 and clean[j]=='\\':n+=1;j-=1
 if n%2:continue
 if ch=='{':stack.append(i)
 else:
  assert stack,('unmatched closing brace',i)
  stack.pop()
assert not stack,('unclosed braces',stack)
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 if m[1]=='begin':envs.append(m[2])
 else:
  assert envs and envs.pop()==m[2],('environment mismatch',m.group())
assert not envs
assert clean.count(r'\[')==clean.count(r'\]')==2
assert r'\scanpage{73}\mspage{72}' in tex and r'\cotefile' not in tex
assert len(r['crops'])==17 and len(json.loads((root/'inspection_log.json').read_text()))==20
for d in r['differences']:
 assert all(isinstance(d[k],bool) for k in ('change_c','change_h','math_consequential'))
 assert d['marked_in_h'] in ['yes','no']
 assert d['crop'] is None or Path(d['crop']).is_file()
 assert d['bbox_image'] in r['image_views']
 assert len(d['bbox'])==4
for x in r['inventory']:
 assert x['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion']
 assert x['sheet_kind']=='text' and x['hand']=='his hand' and x['transcribed']=='yes'
r['finished_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
r['structural_checks']={'braces_balanced':True,'environments_balanced':True,'display_pairs':2,'named_graphics_present':True,'witness_snippets_exact':True,'required_image_views':3,'successful_crop_views':17,'compilation_performed':False,'mathematical_validation_performed':False}
(root/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(root/'structural_check.txt').write_text('Fragment/report consistency checked without compiling. Braces and environments balanced; two display pairs; all six named graphic references present; every witness snippet is an exact substring of its supplied witness; 3 source views + 17 own crop views logged; all required booleans and inventory kinds valid. No mathematical validation performed.\n')
print(json.dumps({'reading_file':str(root/'reading.tex'),'report_file':str(root/'report.json'),'differences':len(r['differences']),'c_doubts':len(r['c_doubts']),'context_dispositions':len(r['context_dispositions']),'remaining_doubts':len(r['remaining_doubts']),'crops':len(r['crops']),'finished_utc':r['finished_utc'],'structural_checks':r['structural_checks']},indent=2))
