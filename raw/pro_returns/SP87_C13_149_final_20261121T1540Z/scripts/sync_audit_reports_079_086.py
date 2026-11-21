"""Copy only documented blind-audit deltas into normalized root reports.
The original readers' schemas differ from the root schema; never replace an
entire normalized report or its first-stage decisions with a reader report.
"""
from pathlib import Path
import json,copy
import aggregate
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
changed_places={79:['local_target','last_caution'],82:['P10_bien_plus','P13_cancelled_number'],83:['C083_11_meme','C083_13_deleted_phrase','C083_15_dans_le'],84:[],85:['P05_geometriques_quotes','P08_deleted_H1','accent in complete'],86:['C086_09_eta_subscript','C086_11_meme_short_form']}
# Identify exact audited rows by their saved second-crop references, avoiding
# any naming mismatch or changes to earlier root-only certainty rows.
for n in changed_places:
 rp=w/'review'/f'149_scan{n:03d}_reviewed.json';a=json.loads((w/'readers'/f'149_scan{n:03d}'/'report.json').read_text());r=json.loads(rp.read_text())
 for row in a['changes']:
  if not str(row.get('crop','')).startswith(f'second_149_scan{n:03d}_'):continue
  c=copy.deepcopy(row);c['crop']='crops/'+c['crop'];ix=next((i for i,x in enumerate(r['changes']) if x['place']==c['place']),None)
  if ix is None:r['changes'].append(c)
  else:r['changes'][ix]=c
 for row in a['marks']:
  if not str(row.get('crop','')).startswith(f'second_149_scan{n:03d}_'):continue
  c=copy.deepcopy(row);c['crop']='crops/'+c['crop'];ix=next(i for i,x in enumerate(r['marks']) if x['id']==c['id']);r['marks'][ix]=c
 # All differences to these uncertainty lists are the explicitly adjudicated
 # additions, except harmless list-to-string normalization of alternatives.
 r['unresolved']=copy.deepcopy(a['unresolved'])
 for u in r['unresolved']:
  if isinstance(u.get('alternatives'),list):u['alternatives']=' | '.join(u['alternatives'])
 if n==82:
  r['inventory'][2]['first_words_or_objects']=a['inventory'][2]['first_words_or_objects']
  r['hand_observations'].append(copy.deepcopy(a['hand_observations'][-1]))
 if n in [83,86]:r['hand_observations'][2]=copy.deepcopy(a['hand_observations'][2])
 if n==83:r['notation_additions'][0]=copy.deepcopy(a['notation_additions'][0])
 raw=a['notes'];flat=''.join(raw) if isinstance(raw,list) else raw
 start=flat.rfind('\n\nBlind')
 if start<0:raise ValueError((n,'audit notes absent'))
 tail=flat[start:]
 if tail.strip() not in r['notes']:r['notes']+=tail
 # Repair list += string artefact in working reader notes, retaining the
 # original first-stage list and one final audit paragraph as separate items.
 if isinstance(raw,list):
  idx=next((i for i,x in enumerate(raw) if x=='\n'),None)
  if idx is not None:a['notes']=raw[:idx]+[''.join(raw[idx:]).strip()];(w/'readers'/f'149_scan{n:03d}'/'report.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
 for h in r['hand_observations']:
  if isinstance(h.get('pages'),list):h['pages']=', '.join(f'{x:03d}' for x in h['pages'])
 rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(aggregate.rebuild())
with (w/'progress.log').open('a') as f:f.write('audit report reconciliation 2026-11-21 14:28 UTC: copied the explicit 079/082–086 blind-adjudication deltas into normalized root reports; preserved first/second TSVs and all first-stage root decisions.\n')
