#!/usr/bin/env python3
"""Integrate the audited bad-place quotient and good-place recognition."""
from pathlib import Path
import datetime
import json
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/norm_canonical_two_wreath_agent.tex}'
entry=r'\input{sections/legendre_bad_place_fibre.tex}'
if entry not in s:
    assert anchor in s
    s=s.replace(anchor,anchor+'\n'+entry)
p.write_text(s)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.102']={
    'answers':'A7; A15; L14; L15',
    'depends_on':'A.14; A.16; A.37; A.49; A.56; A.63; A.74; A.78; A.94; exact Tate nomes, pro-{2,3} disc maps and coefficient23-to-residue47 comparison',
    'uses_local_theorem':'no for the explicitly stated quotient construction and Selmer recognition range',
    'manuscript_passages':'cote149; scans54–58; L14 and L15 exact congruence-plus-abelian comparisons',
    'notes':'Constructs an actual section of E_U/(ker(Pi→H) intersect Gamma2Pi) over the point254 congruence section. It simultaneously matches point254 at2,11 and full cusp sections at127,23, but fails all point/cusp classes at the good prime47 already at abelian exponent46. The same forced coefficient23 residues, together with the nonsquare obstruction at11, recognize every Selmer section realizing254 under arbitrary labeled integral comparison. No full lift of the constructed quotient section is asserted.'
}
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
extra='A.102 constructs an actual full-congruence-plus-abelian quotient section matching every bad place of E254 but obstructed at the good prime47. Transporting the forced coefficient23 data to residue47 also recognizes every Selmer realization of254 under arbitrary labeled integral comparison.'
for i,line in enumerate(lines[:55]):
    if line.startswith(('| A7 |','| A15 |','| L14 |','| L15 |')):
        cols=line.split(' | ')
        if 'A.102' not in cols[1]:cols[1]+=', A.102'
        line=' | '.join(cols)
        if extra not in line:line=line[:-2]+' '+extra+' |'
        lines[i]=line
s='\n'.join(lines)+'\n'
heading='## A good-place obstruction after all bad-place comparisons'
if heading not in s:
    s+='\n'+heading+'\n\n'+stamp+': A.102 constructs a literal continuous section in the fibre product of the full Legendre congruence quotient and full geometric abelianization. Its two modified primary coordinates are23 and127. The two- and three-primary common factor stays equal to point254. The proof extends the actual punctured-disc comparison to finite groups of order2^a3^b, then assembles a single geometric conjugator in the fibre product. At2 and11 it matches point254; at127 it matches cusp0; at23 it matches cusp1. All integral Tate comparisons preserve the Weil pairing. At the good prime47 its two unit residues are33 and33; exponent46 already excludes every ordinary point and cusp packet.\n\nFor an actual Selmer section realizing254, the dyadic multiplier restriction forces the same square condition. A cusp at11 would force alpha_11=10 modulo11, a nonsquare, so11 is ordinary and its completed exponent is1. The remaining nonpoint configuration then requires both cusp labels at127 and23. Its coefficient23 data force exponents31 and27 modulo46, giving the same contradiction at47. Thus the good-place calculation proves unrestricted labeled recognition for254. The quotient example and the recognition conclusion retain their separate exact source groups and local hypotheses.\n'
p.write_text(s)
audit=stamp+' root A102 audit: checked every normalized logarithm residue and square root, the two full Tate unit equalities and twists, global relative cocycle in the actual H×_(H_ab)T quotient, product decomposition and its point-induced action. The A49 finite-constant descent and tame normalization proof applies to every geometric2,3-group at23 and127, giving simultaneous common-factor conjugacy. Independent higher factors then assemble one geometric conjugator. Checked all four bad places, exponent46 residues and exclusion of nonintegral ordinary points as well as cusps. The recognition addition uses the nonsquare10 at11, A37 two-label requirement, A16 parity/sign maps and the same coefficient23 residue comparison. Independent local_preprint audit passed.\n'
for name in ['notes/hour6_root_audits.md','notes/root_progress.md']:
    with (w/name).open('a') as f:f.write('\n'+audit)
output='A102 integrated: actual quotient matching all bad places, good47 obstruction, and arbitrary-labeled Selmer recognition of254.\n'
Path(__file__).with_name('integrate_a102_output.txt').write_text(output)
print(output,end='')
