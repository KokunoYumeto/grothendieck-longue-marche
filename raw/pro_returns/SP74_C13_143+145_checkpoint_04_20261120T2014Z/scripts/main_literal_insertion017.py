"""Final convention correction: do not print an expanded phrase for two unread graphs."""
from pathlib import Path
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[1];key='143_scan017'
rp=R/'reviews'/f'{key}_accepted.json';r=json.loads(rp.read_text());pp=R/'pages'/f'{key}.tex';t=pp.read_text()
before=r'\inserted{\unsure{non vide|$\ne\varnothing$}}'
graphic=r'''\unsure{\begin{tikzpicture}[baseline=-.35ex,x=.5cm,y=.5cm,line cap=round]
\draw[line width=.35pt] (.07,.49) .. controls (.16,.46) and (.27,.39) .. (.27,.28)
  .. controls (.27,.13) and (.08,.11) .. (.09,.24)
  .. controls (.10,.34) and (.20,.39) .. (.25,.32);
\draw[line width=.45pt] (.46,.36)--(.68,.34);
\end{tikzpicture}}'''
after=r'\inserted{'+graphic+'}'
assert t.count(before)==1 and r.get('audited_at')
reason='Main convention review of the existing groupoid-insertion crop confirms only a tiny loop with an upper entry and a separate short bar. The surrounding long S-like stroke is the attachment guide, not additional letters. Neither the full words non vide nor the complete signs ne-empty-set can be independently read from these surviving two graphs. The visible inscription is therefore drawn under a doubt mark; possible interpretations remain in the doubts record rather than being expanded into the transcription.'
row=dict(place='M0690: literal content of the tiny raised inscription before connexe',C=r'\inserted{\unsure{non vide|$\ne\varnothing$}}',H=r'\marginal{interligne : « \uncertain{non vide} »}',final=after,against_C=True,against_H=True,kind='other',ink=reason,confidence='low',crop='crops/143_scan017_readerC_groupoid-insertion.png',box=[733,1408,1224,1549],marked_in_H=True,consequential=False)
r['changes'].append(row)
for d in r['decisions']:
 if d['id']=='M0690':d.update(decision='undecided',reading=graphic,ink=reason,confidence='low')
found=0
for d in r['remaining_doubts']:
 if 'non vide' in d.get('reading',''):
  d.update(reading=graphic,alternatives='Visible tiny loop and short bar; interpretation as non vide or ne-empty-set remains unestablished.',reason=reason,confidence='low');found+=1
assert found==1
for c in r['changes'][:-1]:
 if before in c.get('final',''):c['final']=c['final'].replace(before,after);c['ink']+=' Later main convention review draws the tiny inscription literally; this row concerns its guide and placement, not recovery of the words.'
for i in r['inventory']:
 if i['element']=='E10':i['first_words_or_objects']='tiny loop and separate short bar, drawn under a doubt mark before connexe'
r['notes'].append(dict(id=key+'-main-literal-N1',text=reason+' This is not a mathematical correction of the groupoid condition. The different reader had independently described the same limited surviving strokes.'))
r['hand_log'].append(dict(habit='A tiny interlinear inscription must not be expanded into several words when only two graphs are readable.',places='143_scan017 insertion before connexe, M0690.',scope='The loop and short bar are separate from the long attachment guide; no additional letter sequence is established.',misreadings='Both draft witnesses propose non vide. The final fragment preserves the drawn graphs with uncertainty rather than printing that expansion.'))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r['check_events'].append(dict(statement_id=key+'-main-literal-N1',date=now[:10],who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='used and rechecked in this run',outcome='Physical inscription and guide were independently inspected in the existing crop. Only the two readable graphs are reproduced; their semantic interpretation remains unresolved. No groupoid proposition was proved.'))
record=dict(time=now,before=before,after=after,reason=reason,crop=row['crop'],box=row['box'])
r.setdefault('post_audit_main_corrections',[]).append(record)
pp.write_text(t.replace(before,after));rp.write_text(json.dumps(r,ensure_ascii=False,indent=2))
(R/'reviews'/f'{key}_main_literal_insertion_supplement.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
with (R/'progress.log').open('a') as f:f.write(f'scan 017 main literal-inscription convention supplement {now} cote 143; existing crop used, no recrop\n')
print('017 tiny inscription preserved literally; M0690 remains undecided')
