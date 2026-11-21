"""Explicit occurrence-level accounting decisions; never change page readings."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import assemble
B=Path(__file__).resolve().parents[1]
choices=[
('054','P05','C','C lists 1 and 2; the final lists 2 and 1 and keeps both unresolved. Reordering these alternatives supplies no resolved correction.'),
('055','P04','H','The H pt reading corresponds to the pt alternative inside the same cancelled group; deleted and struck are the two witness wrappers for that recorded cancellation.'),
('055','P09a','C','The C voudra candidate remains an explicit final alternative; adding raisonne has not resolved the word.'),
('055','P11','H','The H de reading remains an explicit final alternative beside des.'),
('057','P07','H',r'The H Centr alternative remains explicitly present. At this indexed occurrence, operatorname{Centr} and mathrm{Centr} render the same five letters, and the H raised o maps to the recorded small raised round Gamma mark.'),
('057','P16','H',r'The H to arrow remains the longrightarrow alternative between the same E_L and E_K. Both encode a single rightward connector at this coordinate; the uncertain head is not resolved.'),
('057','P18','C','The C comma remains the final comma alternative; the choice between period and comma is unresolved. H still omits the independently written punctuation mark.'),
('059','P02a','H','The H cancelled K remains an explicit final alternative at the same crossed group; the source state remains unresolved.'),
('059','P08a','C',r'The C cancelled widetilde U_i remains a full explicit final alternative. The additional index and decoration candidates broaden the unresolved reading. H still records only an illegible crossed group.'),
('061','P04','H','The H de reading remains an explicit final alternative beside des.'),
('062','P07','H','Substituting a for the local e/a slot gives exactly the H définissant reading; substituting e gives C définissent. Neither is excluded.')]
dest=B/'uncertainty_accounting.json';assert not dest.exists();log=[];hashes={}
for n,cid,witness,reason in choices:
 page='149_scan'+n;rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert r.get('audit')
 p=B/'pages'/f'{page}.tex';h=hashlib.sha256(p.read_bytes()).hexdigest();hashes[page]=h
 x=next(x for x in r['changes'] if x['id']==cid);before=dict(x);assert x['against_'+witness];x['against_'+witness]=False
 x['accounting_note']=reason
 if not (x['against_C'] or x['against_H']):
  r['changes'].remove(x);r.setdefault('nonmaterial_observations',[]).append(x);action='moved to uncounted observations'
 else:action='excluded only against '+witness
 log.append(dict(page=page,id=cid,witness=witness,action=action,reason=reason,row_before=before,row_after=x))
 rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');assert hashlib.sha256(p.read_bytes()).hexdigest()==h
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
dest.write_text(json.dumps(dict(utc=stamp,purpose='Exclude unresolved alternatives and certainty-only changes from material witness-correction counts, preserving all evidence.',records=log,unchanged_page_hashes=hashes),ensure_ascii=False,indent=2)+'\n')
with (B/'progress.log').open('a') as f:f.write(f'uncertainty accounting reconciled {stamp}: 11 explicit witness-count decisions on audited pages; page text and frozen audit inputs unchanged.\n')
print(json.dumps(assemble.build()))
