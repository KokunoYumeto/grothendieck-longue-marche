"""Main-reader decisions on the five independently proposed scan093 loci."""
import json
import subprocess
import sys
from audit_support import load,replace_exact,commit,OUT

r,a,s=load(93)
adjudications=[]
for i,c in enumerate(a['changes'],1):
    s=replace_exact(s,c['before'],c['after'])
    final=c['reading']
    if i==1:final=r'\inserted{$\unsure{\overline\Theta|\widetilde\Theta}$}'
    if i==3:
        prefix=c['before'][:-1]
        assert c['after'].startswith(prefix) and c['after'].endswith('=')
        final=c['after'][len(prefix):-1]
    if i==5:final='connexe'
    category={1:'Symbols and indices',2:'Text that is not on the page',3:'Drawings and diagrams',4:'Words',5:'Text that is not on the page'}[i]
    kind={1:'misread symbol or index',2:'text not on the page',3:'drawing or diagram',4:'misread word',5:'text not on the page'}[i]
    row={'id':f'093-A{i:02}','place':c['place'],'c':c['c'],'h':c['h'],
         'final':final,'c_changed':True,'h_changed':i!=5,'category':category,'kind':kind,
         'marked_in_H':False,'confidence':'medium','scan_shows':c['scan_shows'],
         'box':c['box'],'crop':c['crop'],'consequential':False,
         'math_note':c.get('math_note','Local spelling or punctuation; no mathematical assertion is changed.')}
    if i==2:row.update({'c':'i.e.','h':'i.e.'})
    if i==5:row['math_note']='The margin ending remains readable; only its unsupported terminal point is omitted. H’s unrecovered words are already collated at 093-27, so this punctuation omission adds no H difference.'
    r['changes'].append(row)
    adjudications.append({'id':c['id'],'decision':'accepted','reading':final,
        'evidence':c['scan_shows'],'crop':c['crop'],'confidence':'medium',
        **({'function':'unresolved; ordinary equality unchanged'} if i==3 else {})})

old=next(x for x in r['changes'] if x['id']=='093-20')
old['final']=old['final'].replace(r'\inserted{$\widetilde\Theta$}',r'\inserted{$\unsure{\overline\Theta|\widetilde\Theta}$}')
old['place']='Live preposition after the second inserted Theta'
old=next(x for x in r['changes'] if x['id']=='093-25')
old['place']='Verb after i.e'
old=next(x for x in r['changes'] if x['id']=='093-27')
old['final']=old['final'].replace('connexe.','connexe') if old['final'].endswith('connexe.') else old['final'].replace('connexe.}', 'connexe}')

for proposal,identifier,alternatives in [
    ('A093-01','D093-audit-second-Theta',[r'\widetilde\Theta']),
    ('A093-04','D093-audit-connait',['connaît'])
]:
    d=next(x for x in a['confirmed_doubts'] if x['id']==proposal)
    r['doubts'].append({'scan':93,'place':d['place'],'reading':d['reading'],
        'alternatives':alternatives,'confidence':'medium','reason':d['evidence']})
    r['decisions'].append({'id':identifier,'cote':'142','scan':93,'decision':'undecided',
        'reading':d['reading'],'what_the_ink_shows':d['evidence'],'crop':d['crop'],'confidence':'medium'})

for item in r['inventory']:
    if item['element']=='lifted action label':item['first_words_or_objects']='Theta with bar / flattened-tilde uncertainty'
    if item['element']=='closing paragraph':item['first_words_or_objects']='--- ... est connue quand on connai-t (diacritic uncertain)'
new=dict(a['new_inventory'][0]);new['transcribed']='yes'
pos=next(i for i,x in enumerate(r['inventory']) if x['element']=='equivariance formula and number')+1
r['inventory'].insert(pos,new)
for h,errors in zip(a['hand_log_additions'],[
    'Both C and H give a definite tilde at this second insertion. The flat stroke is now transcribed with bar first and tilde as the retained alternative.',
    'Both C and H supply a terminal point after this i.e; neither independent reader can identify it in the saved crop. The points in il f. et s. are separately confirmed.',
    'Both C and H give definite connaît. The compact hooked mark now retains plain i first and the circumflex alternative.'
]):
    h=dict(h);h['witness_errors']=errors;r['hand_log'].append(h)
for item in r['abbreviations']:
    if item['form']=='i.e.':item['form']='i.e'
r['notes'].extend([
    'The full second reading marks the second inserted Θ with bar/flattened-tilde uncertainty, independently of the first insertion’s tilde/prime ambiguity. The near-flat detached stroke is visually distinct from the nearby wave over C; no new mathematical object is inferred.',
    'The abbreviation before satisfaisant reads i.e with its internal point and no visible terminal point. The separate f. and s. points remain. No independent terminal point is found after the last connexe in the oblique margin, so none is supplied.',
    'Two tiny dark points stand high to the right of the left closing parenthesis of (46), above the ordinary equality. Their visible arrangement is reproduced in a small inline TikZ drawing. Their function remains unresolved between punctuation-like traces and incidental pen-points; neither a colon nor defining equality is asserted. The drawing has a separate inventory entry, not an invented word.',
    'The closing connai-t has a compact hooked i mark and retains plain i first with a circumflex alternative. Nine inherited text doubts and these two new text doubts remain. No new mathematical check event.'
])

p=OUT/'documentation/root_view_ledger.json';ledger=json.loads(p.read_text())
crop='crops/scan093_audit_connait.jpg'
if crop not in ledger['93']['crops_seen']:ledger['93']['crops_seen'].append(crop)
p.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')

p=OUT/'documentation/notation_audit_updates.json';overlay=json.loads(p.read_text())
accent=next(x for x in overlay if x.get('sign','').startswith('connait;'))
accent['pages']='082, 085–086, 088, 093'
accent['evidence']+=' The closing 093 form has a compact hooked point and retains plain i first with the circumflex alternative.'
abbr=next(x for x in overlay if x.get('sign','').startswith('ie.;'))
abbr['sign']='ie.; i.e.; i.e'
abbr['pages']='080, 086, 090, 093'
abbr['evidence']+=' The 093 occurrence instead has its internal point and no visible terminal point, transcribed i.e.'
overlay.append({'match_sign':r'\Theta,\Theta^n,\Theta^\nu;\quad\widetilde\Theta,\widetilde\Theta_0','fields':{
    'evidence':'Superscript n is written on 090–091; nu on 096. The first inserted lift mark on 093 retains tilde/prime uncertainty; the second inserted Θ on 093 has a nearly flat detached stroke and is transcribed with bar/flattened-tilde uncertainty. The connected upper cap on 094, prime/star on 095 and cancelled lift on 098 retain their individual doubts. No decoration is propagated into unclear ink.'}})
p.write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(93,r,a,s,
    'Complete independent second reading by reader_a. All 37 inherited comparison places, 30 original inventory elements and 15 old mark decisions were reviewed. The main reader inspected all five proposed loci on saved crops and accepted the local Theta-decoration doubt, i.e punctuation, neutral high-point drawing, connai-t doubt, and removal of the unsupported final marginal point. Nine inherited text doubts plus two new text doubts remain; the drawing’s function is separately unresolved in notes. One inventory element added. No mathematical check event.',
    adjudications)
