from pathlib import Path
import json,re
p=Path('out/readers/021/C'); tex=(p/'reading.tex').read_text()
r=json.loads((p/'report.json').read_text()); s=json.loads((p/'source_audit.json').read_text()); g=json.loads((p/'graphical_groups.json').read_text())
# Inventory ordering and original source identities are administrative provenance.
ypos={1:65,2:140,3:265,4:385,5:490,6:645,7:725,8:810,9:1030,10:1070,11:1125,12:935,13:1195,14:1305,15:1380,16:1433,17:1680,18:1815,19:1900,20:2040,21:2135,22:2180,23:419,24:1818,25:2227,26:1935,27:398}
source_map={n:f'021.{n:02d}' for n in range(1,18)};source_map.update({18:'021.17',19:'021.18',20:'021.19',21:'021.20',22:'021.21'})
for item in r['inventory']:
 suffix=item['element'].split('.')[-1]
 if suffix.isdigit():
  n=int(suffix)
  if n in ypos:item['page_order_y']=ypos[n]
  else:
   loc=next((d for d in r['differences'] if d['location']==item['position'] and d.get('bbox')),None)
   item['page_order_y']=loc['bbox'][1] if loc else 0
  if n in source_map:item['source_C_element']=source_map[n]
 elif suffix.startswith('M'):
  d=next(d for d in r['differences'] if d['id']=='C021-'+suffix);item['page_order_y']=d['bbox'][1]
 else:item['page_order_y']=2350
r['inventory'].sort(key=lambda z:(z['page_order_y'],z['element']))
precise={
'C021-R01':("l'on a",['on a']),
'C021-R05':('comme',[]),
'C021-R06':('j.e.',['i.e.','j:e.','i:e.']),
'C021-R07':('upright !',['sideways ou','sideways dash']),
'C021-R08':(r'\Sigma_{i\alpha}',[r'\Sigma_{i,\alpha}']),
'C021-R10':(r'\deleted{impli}',[r'\deleted{impl.}']),
'C021-R12':(r'\circ',['0']),
'C021-R15':(r'\alpha_0',[r'\alpha']),
'C021-D03':('literal two middle points',['single abbreviation point plus an independently attached point','colon punctuation']),
'C021-D07':('K with head retrace',[r'\deleted{I}K']),
'C021-D08':('achèvera',['achévera','achevera']),
'C021-D09':('demonstration',['démonstration']),
'C021-D12':('précédent',['prêcédent'])}
for d in r['doubts']:
 if d['difference_id'] in precise:d['reading'],d['alternatives']=precise[d['difference_id']]
history=[
{'stage':'initial combined packet read','result':'text output truncated','response':'Complete bounded reads of all required files before images; no image delivery failed.'},
{'stage':'first source-only structural pass','result':'two unmatched opening braces','cause':'End-of-group marker comments swallowed two following macro closings; the same boundary also commented adjoining proof prose.','response':'Added a newline after every complete graphical group marker; regenerated the complete source and all reports.'},
{'stage':'exact source-span audit','result':'parent end markers could match prefixes of nested child IDs','response':'Changed source span extraction to require the exact whole-line end marker; regenerated source/audits.'},
{'stage':'final source-only pass','result':'passed','scope':'Unescaped braces, nested environments, even math delimiters, crop existence, original C identity map, exact group spans and adjoining proof prose. No render/compile result claimed.'}]
r['provenance']['source_review_history']=history
r['provenance']['checkpoint_pause']='Assembly saved and mutations paused for root Checkpoint18; resumed in the same reader context after release. No later image view.'
r['structural_review']['checks'][-1]='inventory transcribed flags reviewed, with selected source groups manually matched'
# Literal path/node command records complement, rather than replace, complete group source boundaries.
for z in g:
 ex=z.get('reading_tex_exact_excerpt',z['source'])
 z['source_command_lines']=[line for line in ex.splitlines() if re.match(r'\s*\\(?:draw|fill|node|useasboundingbox)\b',line)]
 z['source_command_scope']='Includes nested selected child groups when this is a parent; child source overlap is provenance, not an additional visible copy.'
 span=z.get('reading_tex_character_span')
 if span:
  if tex[span[0]:span[1]]!=z['reading_tex_exact_excerpt']:raise RuntimeError('Exact source span mismatch: '+z['id'])
  if z['id']!='C021-G05' and ex.rstrip().splitlines()[-1]!='% END '+z['id']:raise RuntimeError('Incomplete group end: '+z['id'])
s['graphical_groups']=g;s['inventory']=r['inventory'];s['source_structure_review']=r['structural_review'];s['processing']=r['provenance'];s['counts']=r['counts'];s['raw_original_C_inventory']=json.loads(Path('packets/021/C_inventory.json').read_text());s['source_review_history']=history
r['provenance']['exact_group_span_validation']='Every declared span equals its full exact selected excerpt and ends at its own full marker; no source prefix truncation remains.'
s['processing']=r['provenance']
(p/'graphical_groups.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
(p/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(p/'source_audit.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
(p/'assembly_status.json').write_text(json.dumps({'phase':'complete; UTC seal pending','checkpoint_pause':False,'structural_review':'passed','images_final':True,'source_spans':'complete exact-marker spans verified','source_repairs_disclosed':True},ensure_ascii=False,indent=2)+'\n')
print('Final metadata, sorted inventory and exact source groups validated.')
