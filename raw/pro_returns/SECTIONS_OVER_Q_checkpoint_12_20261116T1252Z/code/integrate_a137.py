#!/usr/bin/env python3
"""Integrate the fully audited finite obstruction on an actual completed tripod pair."""
from pathlib import Path
import datetime
import json
import subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/tripod_escaping_support.tex}'
entry=r'\input{sections/harmonic_tripod_finite_obstruction.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.137']={
 'answers':'A5; A7; A8; A9; A12; A15; L2; L9; L10; L14; L17; L20',
 'depends_on':'A.93 etale/group comparison; A.107 exact harmonic cover; A.134 completed harmonic obstruction; nonsplit central-extension descent; proved two-progression fourth-power detection; exact path-chain representation and executed lower-central/augmentation computations',
 'uses_local_theorem':'no; the assertion is for actual Selmer sections and explicitly prescribed finite quotient local images',
 'manuscript_passages':'cote149; scans56–58,126–127; completed tripod Kummer data, finite geometric quotients and actual section lifting',
 'notes':'The explicit harmonic completed triple maps to an infinite-support ordinary tripod pair with no full Selmer section. The obstruction already occurs in the actual finite geometric quotient Pi/K of order2^136, with K=cl(H²[H,H]), H=ker(Lambdaab/4), and Lambda the harmonic index-two subgroup. Its Kummer character B modulo8 and local ordinary point images force the whole old quartic torsor by a proved p≡5,3mod8 detection lemma. A central Brauer extension descends through K without an arithmetic splitting of the quartic cover; exact point and real-cusp pullbacks give the invariant-sum contradiction. The quotient has exact nilpotency class17, proved by its128-vertex/256-edge model, complete lower-central computation and a separate augmentation-ideal/196606-letter-word audit. Thus the actual third-derived and class17 quotients also exclude the specified locally matching pair. This is not a claim of the earliest obstruction for that pair or of a universal bound for all ghosts. Root, local_preprint and birational_main full audits passed.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
items={'A5','A7','A8','A9','A12','A15','L2','L9','L10','L14','L17','L20'}
detail=('A.137 maps the explicit completed harmonic triple to an ordinary infinite-support tripod pair and excludes every full Selmer section with that pair. Its actual finite detecting quotient has order2^136 and exact nilpotency class17; the third-derived and class17 quotient maps retain the obstruction. The proof includes the nonsplit Brauer-class descent and the finite Kummer argument forcing the harmonic quartic cover.')
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in items:continue
    if 'A.137' not in cells[1]:cells[1]+=', A.137'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## A completed tripod pair excluded by a class-seventeen finite quotient'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+detail,
    'The new pair is A=−4A0A1, B=4Ah² from A134, with finite centres4T_p(1−T_p) and real centre−77763/36481. The finite condition B modulo8 equals4a_h² forces a global choice of harmonic sheet modulo four. At primes3 and5 modulo8, that choice forces the actual local harmonic centre. A separate rational fourth-power detection proof, through Q(zeta8) and its Q(i) fixed field, then forces the full old quartic torsor. This supplies an actual lift to its arithmetic cover subgroup.',
    'The quartic cover has no rational point, so its arithmetic group is retained as an extension. Every central F2 extension splits on its free geometric subgroup H. Conjugation discrepancies are characters of H and vanish on K=cl(H²[H,H]); quotienting the chosen lift of K gives an exact central extension over the finite geometric quotient. The original extension is its literal fibre-product pullback. Local fixed sheets give actual points, and the proper Brauer lift gives evaluation at real boundary points for cuspidal images. The resulting rational Brauer class would have invariant sum1/2, contradicting reciprocity.',
    'The quotient is computed through the actual graph of P=(C4×C4) semidirect C8, with128 vertices and256 directed edges. Its path cycles have dimension129 and give exactly Pi/K. The complete lower-central dimensions from Gamma4 through Gamma18 are124,121,115,107,97,85,71,55,41,29,19,11,5,2,0. A literal weight17 commutator is the sum of all128 x-edges. A second implementation computes I(P)^17=0 and independently expands and traces the same196606-letter word. The exact class17 identifies a detecting quotient; no claim is made that this is the first obstruction of the pair or a common obstruction level for every ghost.',
    'The literature search opened the primary mod-p relation-module constructions of Yamin and Dietrich–Hulpke, with their exact theorem numbers and the comparison map recorded in the paper and source audit. The full new result has three independent proof reviews. Both A1 assertions remain open.',''])
p.write_text('\n'.join(lines)+'\n')
audit=('A137 full saved-source audits passed root, local_preprint and birational_main: nonsplit central-extension descent and literal fibre product; quotient-level mod-eight Kummer maps; global sign/deck choice; exact fourth-power detection through Q(zeta8), sigma5 and Q(i); fixed-sheet forcing of the full quartic arithmetic subgroup; finite-point and real-cuspidal cohomology pullbacks; full completed-pair and derived quotient consequences. All three also checked the actual graph identification and exact class17 refinement. Root reran the full lower-central certificate and independent augmentation audit; the latter gives I17=0 and independently traces the196606-letter deepest word. The source now includes both upper-bound proofs, the two exact finite outputs and their complete bases/provenance. The integer character parameter is identical to A134.')
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
    p=w/name
    s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
    if audit not in s:p.write_text(s+'\n'+stamp+' '+audit+'\n')
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out='Integrated A137 with its exact class17 quotient and independent augmentation proof.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a137_output.txt').write_text(out)
print(out,end='')
