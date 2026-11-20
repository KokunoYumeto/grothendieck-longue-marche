from pathlib import Path
import json
from datetime import datetime,timezone
R=Path('out'); d=json.loads((R/'checks/scan006_record_draft.json').read_text())
assert len(d['decisions'])==68 and len(d['doubts'])==17
assert all(x.get('root_decided') for x in d['decisions'])
assert not any('pending' in x['evidence'].lower() for x in d['decisions'])
keep={7,13,16,17,21,22,23,25,29,33,41,43,48,49,50,51,52,53,54}
for x in d['decisions']:
 n=int(x['id'].split('-')[1].rstrip('bcd'))
 if x.get('mathematical_consequence'):
  x['mathematical_context']=x['mathematical_consequence']
  if n not in keep:x.pop('mathematical_consequence')
 if n in {14,15,17,21,22} and not x['diff_H']:x['kind']='other'
 if n==61:
  x['mathematical_context']=x['mathematical_context'].replace('no new computation event is added.','the manual monomial comparison is recorded as 006-factor-correspondences.')
d['notes']=d['notes'].replace('the unequal basis indices','the basis indices')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
proof='''\n## 006-factor-correspondences — manual monomial comparison\n\nRecorded: NOW. The inclusion of R0 = Q[P0,P1,Q0,Q0^{-1},Q1] into the coefficient ring used above fixes each named generator. Its defining inverse relation is the same Q0 Q0^{-1}=1. Represent a Laurent monomial by (coefficient, exponent of P0, exponent of P1, exponent of Q0, exponent of Q1); multiplication multiplies coefficients and adds each exponent.\n\nThe products Q1 P0 and P0 Q1 both give (1,1,0,0,1). The products 2(P1 Q1)Q0^{-2} and (2P1)(Q1 Q0^{-2}) both give (2,0,1,-2,1). This is the explicit correspondence for the factor order and shared-numerator placement considered at 006-01 and 006-61. It records a manual use and recheck of multiplication in the already specified coefficient ring, without claiming a further run of the coefficient-check script. The transcription keeps the physical factor order and fraction placement.\n'''.replace('NOW',now)
with (R/'checks/scan006_algebra.md').open('a') as f:f.write(proof)
d['check_events'].append({'statement_id':'006-factor-correspondences','date':now,'who':'GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root','type':'used and rechecked in this run','outcome':'Manual Laurent-monomial comparison: Q1P0 and P0Q1 both have tuple (1,1,0,0,1); 2(P1Q1)Q0^{-2} and (2P1)(Q1Q0^{-2}) both have tuple (2,0,1,-2,1), in coordinates (coefficient,P0,P1,Q0,Q1). The generator-fixing inclusion and multiplication rule are specified in checks/scan006_algebra.md. Literal ink order and numerator placement remain unchanged.'})
d['notes']+='\n\nA later manual monomial comparison records the explicit correspondence for Q′P/PQ′ and the two placements of P′ in the shared-numerator expression (event 006-factor-correspondences). It gives identical coefficient/exponent tuples in the specified Laurent coefficient ring; the diplomatic factor order and placement remain as written.'
d['workflow_note']+=' A fifth event records root’s subsequent manual Laurent-monomial comparison; the four earlier computations remain unchanged.'
d['main_adjudicated']=True;d['main_approved_utc']=now
(R/'records/scan006.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=R/'legibility_note.md';s=p.read_text().replace('scans 002–005 have been decided','scans 002–006 have been decided');s+='\nScan006 has two opposed writing layers and long crossing strokes. Crowded exponents, primes and overwritten signs remain its weakest readings. Full crop bounds resolved two predecessor letters; the raised-2 cancellation state and one prose comma remain explicit doubts. Extra fraction-rule strokes are drawn.\n';p.write_text(s)
with (R/'checks/scan006_main_decisions.md').open('a') as f:f.write('\nRecord approved '+now+'. Final audit: 68 decisions; 16 C differences; 52 H differences; 11 original C doubts resolved,14 retained,3 new qualifications;35 inventory elements;4 executed coefficient computations plus1 subsequent manual monomial comparison.\n')
print({'approved':now,'decisions':68,'events':len(d['check_events'])})
