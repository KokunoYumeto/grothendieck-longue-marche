from pathlib import Path
from datetime import datetime, timezone
import json,re
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/B')
s=(R/'reading.tex').read_text()
p=json.loads((R/'report.json').read_text())
c='\n'.join(re.split(r'(?<!\\)%',ln,1)[0] for ln in s.splitlines())
errors=[]; stack=[]
for i,ch in enumerate(c):
 if ch in '{}':
  slashes=0;j=i-1
  while j>=0 and c[j]=='\\':slashes+=1;j-=1
  if slashes%2:continue
  if ch=='{':stack.append(i)
  elif stack:stack.pop()
  else:errors.append('extra closing brace at '+str(i))
if stack:errors.append('unclosed braces: '+str(stack))
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',c):
 if m[1]=='begin':envs.append(m[2])
 elif not envs or envs.pop()!=m[2]:errors.append('environment mismatch: '+m.group(0))
if envs:errors.append('unclosed environments: '+str(envs))
if c.count('$')%2:errors.append('odd dollar delimiter count')
allowed={'begin','deleted','draw','end','figure','fill','fontsize','linewidth','mathord','mathrm','node','overline','phantom','resizebox','rlap','scanpage','selectfont','underline','unsure','useasboundingbox'}
macros=set(re.findall(r'\\([A-Za-z]+)',c))
if macros-allowed:errors.append('unlisted macros: '+str(macros-allowed))
# File and schema checks, without compiling or rendering.
required={'id','location','C','H','reading','evidence','confidence','kind','diff_C','diff_H','C_doubt_status','readers_crop','bbox','mathematical_consequence'}
kindset={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for d in p['differences']:
 if required-set(d):errors.append('missing difference fields: '+d['id'])
 if d['kind'] not in kindset:errors.append('invalid kind: '+d['id'])
 if d['confidence'] not in ['high','medium','low']:errors.append('invalid confidence: '+d['id'])
 if d['H'] is not None or d['diff_H']:errors.append('H invariant failed: '+d['id'])
 if d['readers_crop'] and not (R/d['readers_crop']).is_file():errors.append('missing crop: '+d['readers_crop'])
for d in p['doubts']:
 if d['crop'] and not (R/d['crop']).is_file():errors.append('missing doubt crop: '+d['crop'])
 if d['id'].startswith('G-') and d['id'] not in s:errors.append('missing drawn doubt: '+d['id'])
for d in p['inventory']:
 if d['kind'] not in ['text','display','diagram','drawing','margin note','insertion','deletion']:errors.append('invalid inventory kind: '+d['element'])
 if d['element'].startswith('G-') and d['element'] not in s:errors.append('missing inventory path: '+d['element'])
for c0 in p['crops']:
 if not (R/c0['path']).is_file() or not c0['viewed']:errors.append('crop availability/view record: '+c0['path'])
 if c0['bbox'][2]>2365 or c0['bbox'][3]>1688:errors.append('crop outside source: '+c0['path'])
if len(p['C_doubt_source_map'])!=13 or sum(len(x['local_decisions']) for x in p['C_doubt_source_map'])!=14:errors.append('source row map incomplete')
if p['check_events']:errors.append('check_events must remain empty')
# Reading/report synchronization on every changed textual reading and key notation.
for q in ['Méditation','Vers un plus long Voyage',r'\rlap{A}\phantom{\deleted{A}}',r'\unsure{C|Ca}',r'\unsure{\mathrm{iii}|\mathrm{iv}}',r'\rlap{(i)}\phantom{\deleted{(i)}}',r'\unsure{(i)|\deleted{(i)}}',r'\unsure{(|\deleted{(}}','Die Eltern','(Les parents)','Das Kind',"(L'enfant)",'Der Baumeister','Le Bâtisseur','Bild und Wahrheit','(Image et Réalité)','Der Wolf','(Le Loup)','Spiel- und Sucht','(Jeu - et Fringale)',"Le ``Maître''",r'1976\mathord{*}',r'\overline{\underline{\mathrm{VI}}}',r'\overline{\underline{\mathrm{IX}}}','% archive sheet number: 12']:
 if q not in s:errors.append('reading/report anchor absent: '+q)
for q in ['(upper-question)','(lower-question)']:
 if q not in s:errors.append('question anchor missing: '+q)
for i in range(1,11):
 if 'G-edge-%02d'%i not in s:errors.append('edge component missing: '+str(i))
# Older visible forms immediately precede their replacements in each local source sequence.
if not s.index('(old-sub-A)')<s.index('(live-sub1)')<s.index('(old-sub-C-left)')<s.index('(live-sub3)')<s.index('(old-sub-D)')<s.index('(live-sub4)'):errors.append('predecessor/replacement source order')
# Graphic bounding boxes use a baseline anchor so editorial doubt superscripts cannot move their paths.
if 'anchor=north west] at' in s:errors.append('unadjusted uncertain graphic anchor')
res={'performed':True,'time_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'checks':['balanced braces','matched tikzpicture environments','paired math delimiters','allowed macro set','all difference schema fields and vocabulary','H-null invariants','13 source doubt rows / 14 local decisions','25 existing crop references with honest viewed records','inventory-path references','text reading/report anchor synchronization','ten right-edge component IDs','predecessor/replacement source order','baseline-anchored uncertain graphics'],'errors':errors,'compiler_or_renderer_used':False,'render_validation_claimed':False,'mathematical_check_performed':False}
p['structural_validation']=res
p['end_utc']=res['time_utc']
p['notes']['drawing_conventions']+=' Small qualified graphics are anchored by their baseline and explicit bounding box; their editorial doubt marker does not set the path origin. Radius values use explicit centimeter dimensions matching the full-scan coordinate scale.'
p['brief_feedback'].append('The connected marginal arrow/brace group is drawn at its page position within the table figure; the inventory retains margin note for its content. This keeps the connections and pale returns visible without moving them into a separate margin box.')
(R/'report.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
(R/'structural_validation.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
md=(R/'reading.md').read_text()
md+='\nFinal structural pass: **'+('passed' if not errors else 'errors listed in structural_validation.json')+'** at '+p['end_utc']+'. The brace, environment, macro, source-row, crop-file and reading/report checks are recorded in `structural_validation.json`. This was a source-only check.\n'
(R/'reading.md').write_text(md)
print(json.dumps({'errors':errors,'end_utc':p['end_utc'],'differences_and_retained_rows':len(p['differences']),'C_changes_including_graphic_components':sum(x['diff_C'] for x in p['differences']),'C_doubt_rows':len(p['C_doubt_source_map']),'local_doubt_decisions':sum(len(x['local_decisions']) for x in p['C_doubt_source_map']),'crops':len(p['crops']),'inventory':len(p['inventory']),'remaining_local_doubts':len(p['doubts'])},ensure_ascii=False))
if errors:raise SystemExit(1)
