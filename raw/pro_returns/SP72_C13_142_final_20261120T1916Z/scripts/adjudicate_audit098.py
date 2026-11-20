"""Root consolidation of plain-i spelling and uncertain shared-t-bar state."""
import json,subprocess,sys
from audit_support import load,replace_exact,commit,OUT
r,a,s=load(98)
ad=[]
for c in a['changes']:
    s=replace_exact(s,c['before'],c['after'])
    ad.append({'id':c['id'],'decision':'accepted','reading':c['final'],
        'evidence':c['scan_shows'],'crop':c['crop'],'confidence':c['confidence']})
c=a['changes'][0]
r['changes'].append({'id':'098-A01','place':c['place'],'c':c['c'],'h':c['h'],
    'final':c['final'],'c_changed':True,'h_changed':True,'category':'Words','kind':'misread word',
    'marked_in_H':False,'confidence':'high','scan_shows':c['scan_shows'],
    'box':c['box'],'crop':c['crop'],'consequential':False,'math_note':c['math_note']})
c=a['changes'][1]
reading=r'\unsure{pourtant|\deleted{pourtant}}'
row=next(x for x in r['changes'] if x['id']=='098-36')
row.update(place='Live/deleted state of pourtant',final=reading,c_changed=True,h_changed=False,
    scan_shows=c['scan_shows'],math_note=c['math_note'])
row['audit_history']='First consolidation treated the long upper line as cancellation across the right letters. Full second reading and root inspection identify a possible shared t-crossbar instead; live text is now preferred and deletion retained explicitly as an alternative.'
d=next(x for x in r['decisions'] if x['id']=='C098-D07')
d.update(decision='undecided',reading=reading,what_the_ink_shows=c['scan_shows'],confidence='medium')
r['certainty_decisions']=[x for x in r['certainty_decisions'] if not x['place'].startswith('C098-D07')]
r['doubts'].append({'scan':98,'decision_id':'C098-D07','place':'Final pourtant: shared t-crossbar or cancellation',
    'reading':reading,'alternatives':['pourtant',r'\deleted{pourtant}'],'confidence':'medium',
    'reason':c['scan_shows'],'crop':c['crop']})
item=next(x for x in r['inventory'] if x['element']=='Final paragraph cancellation')
item.update(element='Final pourtant with uncertain cancellation state',kind='text',
    first_words_or_objects='pourtant (live preferred; deleted alternative explicit)')
for h in r['hand_log']:
    if h['scope']=='Final pourtant.':
        h['habit']='A long stroke joining two t stems may be their common crossbar rather than a cancellation.'
        h['witness_errors']='C and the first consolidation treat pourtant as cancelled. The full second reading and root inspection favor H’s live word, while retaining deletion as an explicit alternative because the bar’s function is not fully settled.'
r['hand_log'].append(a['hand_log_additions'][0])
r['notes'].extend([
    'The complete second reading corrects connaît to connait in quand on connait ses valeurs. The first focused crop shows a compact vertical oval i point with no two-sided roof; the main reader independently inspected it. Both witnesses supplied the circumflex.',
    'At pourtant, the first consolidation treated the long line above the right-hand letters as a strike. Auditor and main reader independently reused the crop and found that the line joins the two t stems at crossbar height, above the low a/n bodies. Live pourtant is now preferred, with deletion retained as an explicit alternative. The original deletion-only certainty is withdrawn and the inventory entry is text with uncertain cancellation.',
    'All 34 inherited comparison loci, 18 decisions, eight old certainty entries and 22 inventory elements were reviewed. The 11 inherited doubts remain and the newly reopened state of pourtant brings the total to 12. No missing element or mathematical check event.'
])
p=OUT/'documentation/root_view_ledger.json';j=json.loads(p.read_text())
crop='crops/scan098_audit_connait.jpg'
if crop not in j['98']['crops_seen']:j['98']['crops_seen'].append(crop)
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=OUT/'documentation/notation_audit_updates.json';j=json.loads(p.read_text())
x=next(x for x in j if x.get('sign','').startswith('connait;'))
x['pages']='082, 085–086, 088, 093, 096, 098'
x['evidence']+=' The 098 connait has a compact vertical oval point and is transcribed without a circumflex.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(98,r,a,s,
    'Complete independent second reading by reader_c. All 34 inherited comparison loci, 18 decisions, eight old certainty entries and 22 inventory elements were reviewed. Main reader inspected the new connait crop and reused the existing pourtant crop, accepting a plain-i spelling correction and revising 098-36 to live-first with explicit deletion-state uncertainty. The latter reverses its C/H flags without adding a second place. Eleven old doubts plus this state doubt remain; no missing element or new mathematical check event.',ad)
