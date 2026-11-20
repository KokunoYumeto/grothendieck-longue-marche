"""Root decisions on independent audit096, including withdrawal of a phantom insertion."""
import json
import subprocess
import sys
from audit_support import load,replace_exact,commit,OUT

r,a,s=load(96)
ad=[]
for c in a['changes']+a['certainty_decisions']:
    s=replace_exact(s,c['before'],c['after'])
    ad.append({'id':c['id'],'decision':'certainty-only count revision' if c.get('certainty_only') else 'accepted',
        'reading':c['reading'],'evidence':c['scan_shows'],'crop':c['crop'],'confidence':c['confidence']})
c=a['changes'][0]
row=next(x for x in r['changes'] if x['id']=='096-23')
row.update(final='[absent from marginal text]',c_changed=True,h_changed=False,
    category='Text that is not on the page',kind='text not on the page',confidence='medium',
    scan_shows=c['scan_shows'],math_note=c['math_note'])
row['audit_history']='The first consolidation carried C’s candidate as an uncertain insertion, including uncertain existence. Complete second reading and root inspection find no independent inscription; the candidate is withdrawn and the existing comparison row revised.'
d=next(x for x in r['decisions'] if x['id']=='M0424')
d.update(decision='other',reading='[absent from marginal text]',what_the_ink_shows=c['scan_shows'],
         crop=c['crop'],confidence='medium',absence_label_only=True)
r['doubts']=[x for x in r['doubts'] if x['place']!='Upper margin proposed insertion after a)']
withdrawn=[x for x in r['inventory'] if x['element'].startswith('Possible small insertion')]
assert len(withdrawn)==1
r['audit_inventory_withdrawals']=withdrawn
r['inventory']=[x for x in r['inventory'] if x not in withdrawn]

c=a['certainty_decisions'][0]
d=next(x for x in r['decisions'] if x['id']=='M0428')
d.update(reading=c['reading'],what_the_ink_shows=c['scan_shows']+' '+c['reason'])
d=next(x for x in r['doubts'] if x['place']=='Middle margin parenthetical start')
d.update(reading=c['reading'],reason=c['reason'])
row=next(x for x in r['changes'] if x['id']=='096-30')
row['final']=row['final'].replace(r'\illegible{2}',r'\illegible{?}')
row['math_note']='The unreadable word count cannot be recovered; unknown extent is marked. No assertion or question has been supplied.'
r['certainty_decisions'].append({'scan':96,'place':c['place'],'reading':c['reading'],
    'confidence':'low','reason':c['reason'],'crop':c['crop']})

for c in a['changes'][1:]:
    number=c['id'][-2:]
    r['changes'].append({'id':f'096-A{number}','place':c['place'],'c':c['c'],'h':c['h'],
        'final':'groupoide' if number=='03' else c['after'],'c_changed':c['c_changed'],
        'h_changed':c['h_changed'],'category':'Words' if number=='03' else 'Text that is not on the page',
        'kind':'misread word' if number=='03' else 'text not on the page',
        'marked_in_H':number=='04','confidence':'medium','scan_shows':c['scan_shows'],
        'box':c['box'],'crop':c['crop'],'consequential':False,
        'math_note':'Local spelling only.' if number=='03' else 'Only C’s supplied terminal point is removed. H’s unrecovered G_m is already collated at 096-35; no new H difference.'})
row=next(x for x in r['changes'] if x['id']=='096-35')
assert row['final'].endswith('.');row['final']=row['final'][:-1]
for h in r['hand_log']:
    if h['habit'].startswith('Oblique marginal writing'):
        h['witness_errors']='C’s K est de t.f. and final de Gamma cannot be supported separately. The complete second reading and root inspection also exclude the proposed fixe x_0 insertion because no independent inscription can be identified.'
for h,errors in zip(a['hand_log_additions'],[
    'C supplies a fixed-point phrase that neither auditor nor main reader can identify independently of crossing body and marginal strokes. H’s ill does not establish that phrase.',
    'Both C and H supply a diaeresis; the single point supports groupoide at this occurrence.',
    'C supplies a terminal point after G_m; H has no independent point there. The rising border and adjacent body strokes are retained in their own elements.'
]):
    h=dict(h);h['witness_errors']=errors;r['hand_log'].append(h)
for i,note in enumerate(r['notes']):
    if note.startswith('The possible fixe'):
        r['notes'][i]='The complete second reading and root inspection withdraw the alleged fixe x_0 de point générique insertion: no independent sequence or attachment exists apart from intersecting established body and marginal text. Its old uncertain inventory entry is withdrawn. The unreadable extent after tentative N’est cannot be counted and is now illegible{?}.'
r['notes'].extend([
    'The final groupoid noun is literally groupoide: one compact point stands over i, with no separate second point. Both witnesses normalize it to a diaeresis. This local reading does not propagate to other occurrences.',
    'The terminal point after the last marginal G_m is unsupported. The m is beside the rising separator edge and other body strokes; no independent point can be identified. The caveat itself remains exactly as written.',
    'All 40 inherited comparison loci, 17 mark decisions and 16 original inventory entries were reviewed; after withdrawal of the phantom insertion there are 15 supported elements. Five inherited doubtful loci remain, including the middle unreadable run with unknown word count. No new mathematical check event.'
])
p=OUT/'documentation/root_view_ledger.json';ledger=json.loads(p.read_text())
crop='crops/scan096_audit_groupoide.jpg'
if crop not in ledger['96']['crops_seen']:ledger['96']['crops_seen'].append(crop)
p.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
p=OUT/'documentation/notation_audit_updates.json';overlay=json.loads(p.read_text())
x=next(x for x in overlay if x.get('sign','').startswith('connait;'))
x['sign']+='; groupoide / groupoïde';x['pages']='082, 085–086, 088, 093, 096'
x['evidence']+=' The final groupoid noun on 096 has one compact i point, transcribed groupoide; no diaeresis is supplied from conventional spelling.'
p.write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(96,r,a,s,
    'Complete independent second reading by reader_a. All 40 inherited comparison loci, 17 mark decisions and 16 original inventory elements were reviewed. Main reader independently reused upper-margin, upright-opening and middle-margin crops and inspected the new diacritic crop. The unsupported M0424 insertion and inventory item are withdrawn; one dotted-i spelling and one missing terminal point are corrected; the unreadable-word count is left unknown as a certainty-only change. Fifteen physical elements and five doubtful loci remain. No mathematical check event.',ad)
