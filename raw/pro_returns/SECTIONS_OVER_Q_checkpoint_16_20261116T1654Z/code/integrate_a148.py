#!/usr/bin/env python3
"""Integrate the audited finite scalar exclusion on the actual elliptic cover."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1];stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/constant_tower_prime_generator_agent.tex}'
entry=r'\input{sections/harmonic_unit_scalar_obstruction.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
record={
 'answers':'A5; A7; A10; L7; L10; L15',
 'depends_on':'A.143 two explicit independent elliptic points and actual quotient map; A.146 integral plane-quartic model and boundary fibres; exact finite group arithmetic and common-residue propagation',
 'uses_local_theorem':'no; the assertion retains full Selmer lifts and uses their actual local point/cusp reductions',
 'manuscript_passages':'cote149; scans56–58; positive-rank profinite multiples and actual punctured-curve lifts',
 'notes':'All profinite unit multiples of each of the two explicit rank-two points R_P and R_Q are excluded. The actual proper image at17 gives allowed R_P scalars{0,5} modulo10, and the image at5 gives only0 modulo2 for R_Q; two further exact rows at257/769 force40|z and10|z. Exhaustive good-prime image computation through3000 gives846 constraints. Literal residue maps and four monotone propagation rounds prove the stronger displayed D_P and D_Q divisibilities and six explicit small-primary domains. Every finite deletion is retained. A cofinite-primary scalar surviving all these finite constraints but outside A146’s subgroups is explicitly given, so no finite-to-infinite or sufficiency inference is made. Full root/local saved-source audits and independent reruns of enumeration, direct certificates and propagation passed.'}
p=w/'notes/register_metadata.json';m=json.loads(p.read_text());m['A.148']=record;p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
detail='A.148 excludes all profinite unit multiples on both explicit rank-two elliptic lines by actual local images, and846 finite residue constraints prove stronger necessary scalar divisibilities with every deletion retained.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in {x.strip() for x in record['answers'].split(';')}:continue
    if 'A.148' not in cells[1]:cells[1]+=', A.148'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: exact scalar residues on the rank-two elliptic lines'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+detail,'',
    'The smallest obstructions occur at17 for R_P and5 for R_Q. The proof enumerates the complete proper plane quartic at those primes, including all four boundary points, and computes its actual elliptic image. At every tested prime the two preimages under the two-isogeny give the same square test, with the exact square ratio written out. This justifies each scalar residue condition without selecting one sheet arbitrarily.',
    'The larger calculation compares residues through the actual reduction maps modulo the primary divisors of each finite orbit order. Every deletion preserves the residue of every possible lift. Four rounds give the displayed large necessary divisors. The proof also exhibits an explicit completed scalar with zero components on every tested coefficient prime and unit components elsewhere; it passes the finite congruences and remains outside the A146 divisibility subgroups. Thus the combined finite calculation still leaves an exact infinite lifting problem. All three programs and their outputs/data are retained and independently rerun.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A148 full root/local saved-source audits PASS. Checked the actual integral proper image including all cusp sources, local Kummer comparison, the exact square ratio between the two phi sheets, all four finite orbits and point-image tables, every necessary-residue operation and finite termination. Root independently reran complete846-row enumeration, four-row detector and full four-round propagation. D_P,D_Q and all six small-primary domains agree. The cofinite-primary survivor is retained as a limit on the finite conclusion.\n'
for name in ['notes/hour10_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A148.\n'+r.stdout
Path(__file__).with_name('integrate_a148_output.txt').write_text(out);print(out,end='')
