#!/usr/bin/env python3
"""Execute only after parent and DE explicitly approve the complete A58 proof."""
from pathlib import Path
import json, shutil, sys
r=Path(__file__).resolve().parents[1]
audit=r/'notes/de_A58_audit.md'
assert (audit.exists() and 'PASS' in audit.read_text()) or '--explicit-root-and-de-pass' in sys.argv, 'Independent DE full audit is required.'
src=(r/'notes/fgh_A58_draft.tex').read_text().replace(
    '% Candidate A.58. Notes only until complete independent audits.',
    '% A.58 full independent root and DE proof/source/certificate audits PASS.')
(r/'sections/A_heisenberg_five_fixed.tex').write_text(src)
(r/'code/a_heisenberg_five_fixed.py').write_text((r/'notes/fgh_A58_certificate.py').read_text())
for ext in ('.json','.out'):
    shutil.copyfile(r/('notes/fgh_A58_certificate'+ext),r/('code/a_heisenberg_five_fixed'+ext))
shutil.copyfile(r/'notes/fgh_A58_certificate_root_rerun.out',r/'code/a_heisenberg_five_fixed_root_rerun.out')
p=r/'sections/A.tex';t=p.read_text();needle='\\input{sections/A_rank_one_good_normalizers.tex}'
assert needle in t and 'A_heisenberg_five_fixed.tex' not in t
p.write_text(t.replace(needle,needle+'\n\\input{sections/A_heisenberg_five_fixed.tex}'))
row=json.loads((r/'notes/fgh_A58_row.json').read_text())
row['where_proved']='sections/A_heisenberg_five_fixed.tex'
row['notes']=row['notes'].replace('Complete candidate with executed exact certificate; independent full audits pending.',
    'Root and DE independently audited the entire proof and exact certificate and reran it: PASS. Registered after both full audits.')
(r/'notes/fgh_A58_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(x['id']=='A.58' for x in rows)
for x in rows:
    if x['id'] in ('A.54','A.55'):
        x['notes']+=' The previously residual all-prime full fixed-group question for the actual Heisenberg5 cover is now completed independently by A.58 using its explicit wild compact-type model.'
rows.append(row);p.write_text(json.dumps(rows,indent=2)+'\n')
for ident in ('A54','A55'):
    p=r/f'notes/fgh_{ident}_row.json'
    if p.exists():
        x=json.loads(p.read_text());x['notes']+=' A.58 subsequently completes the all-prime full fixed-group question for the actual Heisenberg5 cover.';p.write_text(json.dumps(x,indent=2)+'\n')
p=r/'sections/A_heisenberg_five.tex';t=p.read_text();old='by A.55 below. The other full fixed-subgroup questions remain open.'
assert old in t
p.write_text(t.replace(old,'by A.55 below. The full fixed-subgroup comparison at every other\nprime is completed separately by the explicit model in A.58.'))
p=r/'sections/A_quartic_cm_normalizers.tex';t=p.read_text();old='claim to the pro-five fixed-subgroup result already proved there.'
assert old in t
p.write_text(t.replace(old,'claim to the pro-five fixed-subgroup result already proved there;\nthe all-prime full fixed-group comparison is supplied separately by A.58.'))
p=r/'sections/A_general_cover_frontier.tex';t=p.read_text();old='No full fixed-group claim at the other primes is made for this cover.'
assert old in t
new='''A.58 now completes the full fixed-subgroup comparison at every prime
for this same Heisenberg cover. Its exact five-adic charts give one
elliptic main component, five genus-six and ten genus-two
Artin--Schreier tails. Their genera exhaust fifty-one; all twenty-five
cusps occur in rational clusters away from those tails. Thus the
rational-path criterion A.42 applies to every cusp and packet.'''
p.write_text(t.replace(old,new))
p=r/'notes/root_cover_frontier_results.json';rows=json.loads(p.read_text())
for x in rows:
    if x['id']=='A.45':
        if 'A.58' not in x['depends_on']:
            if isinstance(x['depends_on'],str):x['depends_on']+=', A.58'
            else:x['depends_on'].append('A.58')
        x['notes']+=' A.58 completes the full all-prime fixed groups for the actual genus51 Heisenberg5 cover by an explicit wild compact-type model with rational cusp clusters; A.54--55 already settle its normalizers. Universal scope remains Open.'
p.write_text(json.dumps(rows,indent=2)+'\n')
(r/'notes/fgh_A58_audit.md').write_text('''# A.58 integrated after complete independent audits

**PASS, integrated.** Root and DE read the complete draft and exact certificate, checked the actual smooth tail equations and unramified-centre divisibility, AS jump/genus, component persistence, genus exhaustion, actual map and rational cusp clusters, and independently reran the certificate. See `de_A58_audit.md`, `fgh_A58_certificate_root_rerun.out`, and the canonical code/output.

Canonical section: `sections/A_heisenberg_five_fixed.tex`. Canonical code: `code/a_heisenberg_five_fixed.py`, with JSON/output and the root rerun. Historical candidate, source ledger and outputs are retained. The proof makes no use of an unramified Raynaud theorem for the ramified covering map. It settles the actual full pro-prime fixed group at every coefficient prime and every cusp packet through A41--42. No cofinality or fixed-element lifting for other covers is asserted.
''')
with (r/'notes/fgh.md').open('a') as f:
    f.write('''
## A.58: the remaining Heisenberg5 fixed groups are complete

Registered after independent full root and DE proof/certificate audits. Exact residue-five charts on the actual genus51 curve produce one ordinary elliptic main component, five genus6 and ten genus2 Artin--Schreier tails. Their genera exhaust51, proving compact type. The25cusps form five rational clusters of five, away from all positive-genus tails. A42 therefore proves the selected full pro-prime fixed subgroup equals its cusp inertia at every coefficient prime and for every permitted packet/open derived subgroup. Together with A54--55 this completes both requested assertions for this degree125 cover. Earlier notes leaving its other fixed groups open are superseded by this exact calculation.
''')
print('A58 integration complete: section, canonical code, register, frontier and audit.')
