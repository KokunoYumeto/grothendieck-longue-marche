#!/usr/bin/env python3
"""Integrate the audited actual unit-transfer and prime-generator statement."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/harmonic_infinite_primary_obstruction.tex}'
entry=r'\input{sections/constant_tower_prime_generator_agent.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
record={
 'answers':'A5; A9; A15; L9; L10; L14; L20',
 'depends_on':'A.138 class-three vanishing in the constant radical-cyclotomic tower; A.144 exact prime generator; actual cyclic unit ideal correction and quadratic norm transfer; exact completed divisor maps',
 'uses_local_theorem':'no; actual class fields, local norms and completed global units are used',
 'manuscript_passages':'cote149; scans56–58,126–127; compatibility under literal norm and divisor maps',
 'notes':'Actual unit norms in every pure cubic transition K_{n+1}/K_n of the constant radicand3 tower are surjective. The proof transfers a cyclic unit norm through adjoining mu3: a unit of norm epsilon² gives v²/epsilon of norm epsilon. Class-three vanishing transfers to every intermediate field by its Hilbert3 class field and total ramification at3. The degree-one q=511177 branch has coherent completed principal generators starting at gamma=-68+64alpha+alpha², with normq over Q. The scalarq in K1 and the A144 cofactor Uq/gamma³ fail to be norms already from K2 because two other unramified cubic branches have norm valuation3 and their valuation is1. The exact divisor maps prove the comparison. Full independent/root saved-source audits and finite certificate reruns passed, with266 Bezout and2660 exponent-inverse checks.'}
p=w/'notes/register_metadata.json';m=json.loads(p.read_text());m['A.147']=record;p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
detail='A.147 proves onto actual unit norms in the constant pure-three tower and coherent completed generators on one prime branch, with explicit divisor obstructions to transferring the scalarq or the changed-tower cofactor through that tower.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in {x.strip() for x in record['answers'].split(';')}:continue
    if 'A.147' not in cells[1]:cells[1]+=', A.147'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: actual unit transfer and the specified prime branch'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+detail,'',
    'The exact initial element is gamma, whose norm down to Q isq. At the other two q-branches the scalarq and Uq/gamma³ have valuation1 while the next local norm multiplies valuations by3. This proves that the coherent gamma-family has no automatic transfer to the changed-radicand problem. The full proof and executed certificate have independent and root audits.',''])
p.write_text('\n'.join(lines)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
old='The old-to-new radical identities'
extra=' V Theorem5.3 (global reciprocity, printed pp.178--179) and VIII Theorem3.1 (cyclic Hasse norm theorem, printed p.234) were reopened for A.147, with the exact principal-idele and local-to-global norm maps.'
needle='III Theorem 3.5 reopened for A.140: the actual norm group of a non-Galois local extension equals that of its maximal abelian subextension; the root-stabilizer inclusion and Artin diagram were checked on printed pages108--109.'
if 'were reopened for A.147' not in s:
    assert needle in s;s=s.replace(needle,needle+extra,1)
p.write_text(s)
audit=stamp+' A147 full root and independent audits PASS, with separate certificate reruns. Checked every intermediate class-group transfer including n=1; cyclic divisor-kernel and prime-to3 class order; actual epsilon^(4-3) norm transfer; exact q-adic degree-one branch; completed divisor exactness with its unit kernel; recursive gamma_n unit correction and normq; scalar/cofactor failure via the two literal residue-degree3 valuation maps. Milne V5.3 and VIII3.1 independently reopened. Missing mu control sequence corrected before integration.\\n'
for name in ['notes/hour10_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a') as f:f.write('\n'+audit.replace('\\n','\n'))
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A147.\n'+r.stdout
Path(__file__).with_name('integrate_a147_output.txt').write_text(out);print(out,end='')
