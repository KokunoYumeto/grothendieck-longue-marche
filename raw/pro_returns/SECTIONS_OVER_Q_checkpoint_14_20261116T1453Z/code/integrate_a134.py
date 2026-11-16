#!/usr/bin/env python3
"""Integrate the audited explicit harmonic twist and its completed coordinates."""
from pathlib import Path
import datetime
import json
import subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/harmonic_escaping_support.tex}'
entry=r'\input{sections/harmonic_twist_completed_obstruction.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.134']={
 'answers':'A5; A8; A9; A12; A15; L2; L9; L10; L14; L17; L20',
 'depends_on':'A.90 exact mixed-exponent refinement; A.96 common quartic field; A.128 arbitrary-twist constancy; explicit finite local certificates, tame good reduction and Hasse–Weil bound',
 'uses_local_theorem':'no; actual covers, ordinary local points, finite character fields and Brauer reciprocity',
 'manuscript_passages':'cote149; scans56–58,126–127; harmonic completed Kummer data and rational puncture lifting',
 'notes':'Gives the exact locally soluble genus33 harmonic quartic with R=529/382, Q=155564491 and coefficients(R,R−1,(R−1/2)Q²). At c=−338/191 its full common field has degree16 and its character d=18512174429 has constant invariant1/2 at2 and zero at every other place. Thus no rational point or everywhere soluble quadratic augmentation exists. An explicit negative first coefficient refinement uses the exactly cancelling dyadic and real root symbols; subsequent mixed refinements give a specified ordinary completed harmonic triple with each coordinate infinitely supported and no new global squareclass. Root and local_preprint full audits and independent certificate reruns passed:611 centres,1833 fourth-power tests,3040 root-symbol conditions, exact fields, finite group,295 prototypes and complete large-prime bound. All infinite construction choices are effectively specified; only the finite starting certificate is claimed executed.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
report=report.replace('the arbitrary-twist sum and compatible new coefficients remain open.',
    'A.134 supplies an explicit nonzero arbitrary-twist sum and completed harmonic old coordinates; A.132–A.133 identify the exact fixed-centre completion issue.')
lines=report.splitlines()
items={'A5','A8','A9','A12','A15','L2','L9','L10','L14','L17','L20'}
detail=('A.134 gives an explicit everywhere locally soluble harmonic quartic with a nonzero constant Brauer sum and constructs actual completed old coordinates on it. The exact signed initial root-symbol cancellation starts the cofinal mixed refinements; the new puncture−338/191 has no global squareclass even for the completed triple.')
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in items:continue
    if 'A.134' not in cells[1]:cells[1]+=', A.134'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## An explicit nonzero harmonic obstruction and completed old data'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+detail,
    'The repaired prime is1119169 and the square twist factor is155564491. The proper curve has genus33 and64 geometric old boundary points. Its actual new-boundary common field is Q(i,sqrt6,sqrt299,sqrt18512174429), of degree16. The last character has invariant1/2 at2 and zero at every other place. The certificate independently verifies611 rational local centres and all1833 fourth-power criteria; the explicit good-reduction charts and strict Hasse–Weil inequality supply every remaining prime. The root expression for the character is written in every residue factor, and all other common characters have zero global sum.',
    'The completed construction requires more than local solubility. Its initial coordinate-zero root has two dyadic symbols1/2, cancelled by taking that root negative at the real place. The exact signed principal-idele calculation produces a negative rational refinement multiplier. Its new roots are principal squares at every controlled finite place and positive at the real place, establishing the pointwise invariant. The other initial root symbols have been checked individually. The actual mixed-power cover maps then give cofinal completed coefficients, fixed ordinary local centres and infinite support in each coordinate. The same proper Brauer class excludes a new squareclass for the fixed completed centres.',
    'The finite numerical search, independent standard-library certificate and separate root-symbol audit are retained with their actual outputs. The source also proves an infinite prime-repair family through the actual order32 splitting field and its degree8 abelianization. The finite computation is not used as a substitute for the all-place or completed proofs.',''])
p.write_text('\n'.join(lines)+'\n')
audit=('A134 root and local_preprint full saved-source audits passed: exact degree16 common field and root formula in every factor; connected genus33 cover and good-reduction charts; all611 finite centres and the strict large-good-prime bound; full support, dyadic invariant and all outside-support cases; actual order32 repair splitting group and degree8 abelianization;295 nonsquare prototypes and the explicit local reciprocity at each fresh repair prime; all initial boundary symbols, signed valuation factor d0 and negative first refinement; every later mixed-cover invariant, cofinal map, retained centre and infinite-support valuation. Root independently reran both retained certificates, including1833 exact fourth-power tests and3040 unramified root-symbol tests; all passed. Effective finite choices and the executed scope are explicit.')
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
    p=w/name
    s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
    if audit not in s:p.write_text(s+'\n'+stamp+' '+audit+'\n')
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out='Integrated A134 in numerical order.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a134_output.txt').write_text(out)
print(out,end='')
