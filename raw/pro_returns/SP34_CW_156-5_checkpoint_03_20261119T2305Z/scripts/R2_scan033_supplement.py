from pathlib import Path
from datetime import datetime,timezone
import json
b=Path('/workspace/scratch/4770596940a0');out=b/'out/readers/R2';p=out/'scan033.json';r=json.loads(p.read_text());now=datetime.now(timezone.utc).isoformat()
ids=['left_faint_focused','left_faint_context','left_faint_rotated'];allc=json.loads((out/'crops033.json').read_text());cs=[c for c in allc if c['id'] in ids]
entry={'id':'D44','place':'Right of long left rule beside Je dis; source x180–285,y620–765','C':'Omitted','H':'Omitted','reading':'Three pale graphic remnants: short upper diagonal rising right, small broken curved trace below it, longer broken lower diagonal also rising right; no secure lexical or symbolic identification.','ink':'Upper short stroke approximately x255–270,y660–672; small curved/dotted remnant around x253–257,y679–687; lower broken stroke approximately x214–245,y709–724. They are substantially paler than the adjacent live writing. Enlarged and rotated views do not establish whether these are erased writing, another faint writing layer, or other marks. No definite insertion/deletion function is assigned.','confidence':0.94,'confidence_scope':'Presence and approximate shapes, not identity or state.','kind':'omitted drawing; state uncertain','crop':ids,'against_C':True,'against_H':True,'marked_in_H':False}
if not any(d['id']=='D44' for d in r['differences']):r['differences'].append(entry)
r['crops']=allc
for c in cs:
 if not any(v.get('crop_id')==c['id'] for v in r['images_viewed']):r['images_viewed'].append({'path':c['path'],'crop_id':c['id'],'phase':'focused supplement'})
if not any(x.get('id')=='I55' for x in r['inventory']):r['inventory'].append({'id':'I55','kind':'drawing','position':'Right of left separator and left of Je dis, x180–285,y620–765','first_words_or_objects':'two pale diagonals and a small intervening curved remnant','state':'identity, writing layer and deletion status uncertain','crop':ids,'notes':'Preserved graphically without introducing a word or a mathematical relation.'})
r['remaining_doubts'].append({'difference_id':'D44','issue':'Identity and state of pale margin remnants; no secure linguistic/symbolic reading.'})
r.setdefault('supplements',[]).append({'id':'R2.scan033.left_faint_marks','start_utc':'2026-11-19T22:47:24.249116+00:00','end_utc':now,'request':'Parent requested independent examination of x180–285,y620–765 without supplying a reading.','result':entry['reading'],'state':'Undetermined. No confident cancellation or insertion attachment.','crops':ids,'mathematical_check_events_added':0,'changes':'D44 and I55 appended; three crops added; TikZ traces inserted left of Je dis in complete proposed TEX. Earlier judgments and C doubt decisions unchanged.'})
r['last_supplement_utc']=now
r['counts']['differences_and_reviews']=len(r['differences']);r['counts']['inventory_items']=len(r['inventory']);r['counts']['crops_viewed']=len(allc)
r['visual_checks'].append('Supplement: exact requested left-margin rectangle, larger context and clockwise 35-degree view all emitted and inspected; no mathematical check claimed.')
r['independence']['image_reading']+=' Focused supplement then viewed three additional crops; total 43. No other reports or later pages consulted.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
tp=out/'scan033.tex';s=tp.read_text();before=out/'scan033.pre_left_faint.tex'
if not before.exists():before.write_text(s)
snippet=r'''% Focused supplement: pale remnants beside Je dis; no word, mathematical sign,
% or deletion/insertion function is assigned to these marks.
\llap{\begin{tikzpicture}[x=1cm,y=1cm,baseline=0cm]
\draw[black!40,line width=.35pt] (.42,.44)--(.66,.64);
\draw[black!24,line width=.3pt] (.40,.31)..controls(.49,.25)and(.47,.21)..(.44,.16);
\draw[black!20,line width=.35pt,dash pattern=on 2pt off 1pt] (-.22,-.43)--(.12,-.24);
\draw[black!31,line width=.4pt] (.13,-.24)--(.28,-.17);
\end{tikzpicture}\hspace{.35em}}
'''
(out/'scan033_supplement_left_faint.tex').write_text(snippet)
if '% Focused supplement: pale remnants beside Je dis' not in s:
 s=s.replace('Je dis que $A',snippet+'Je dis que $A',1);tp.write_text(s)
# Validate the appended structural syntax without compilation.
body='\n'.join(l.split('%',1)[0] for l in s.splitlines());bal=0
for i,ch in enumerate(body):
 if ch in '{}':
  n=0;j=i-1
  while j>=0 and body[j]=='\\':n+=1;j-=1
  if n%2==0:bal+=1 if ch=='{' else -1;assert bal>=0
assert bal==0 and body.count('$')%2==0
assert body.count('\\begin{tikzpicture}')==body.count('\\end{tikzpicture}')
r['syntax_checks'].append({'type':'supplement structural syntax check','outcome':'Balanced braces/dollars and paired TikZ environments after adding left-margin traces; no compilation.'})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'supplement_end_utc':now,'counts':r['counts']},ensure_ascii=False))
