#!/usr/bin/env python3
"""Integrate the fully checked local Prym Kummer comparison."""
from pathlib import Path
import json,datetime,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/two_inert_prime_class_limit_agent.tex}'
entry=r'\input{sections/harmonic_prym_dyadic_injection.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
rec={
 'answers':'A5; A10; A15; L7; L10; L14',
 'depends_on':'A.150 literal Prym morphisms; exact dyadic unit squares and duplication formula; continuous division-point Kummer cocycle; exact proper boundary fibres; independent finite-reduction counts',
 'uses_local_theorem':'no; the ordinary localization at two is specified in the domain of the section map',
 'manuscript_passages':'cote149; scans56–58; actual elliptic quotient and local section comparisons',
 'notes':'For E_b over K2=Q2(sqrt2), every nonzero [2^n] image has v_sqrt2(x)<=2-4n. The literal valuation table covers all points, including the exact valuation-one unit residues. Thus the continuous local2-adic Kummer map is injective. Local and global torsion are exactly{O,(0,0)}; independent reductions at17 and41 have orders10 and52. Under the actual degree-two Prym map, the preimage of those two torsion Kummer classes is exactly the four boundary points. Restriction to K, compactification, the proper morphism and the Tate-module quotient therefore send every full D-open section ordinary at2 outside the global torsion Kummer classes. No global consequence is inferred from a single cuspidal localization, and no rank or full Selmer computation is assumed. Root proof and independent full saved-source audit/certificate rerun passed.'}
p=w/'notes/register_metadata.json';m=json.loads(p.read_text());m['A.152']=rec;p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
detail='A.152 proves exact dyadic Prym Kummer injectivity, local and global torsion of order2, and the boundary-fibre exclusion for every full section ordinary at two.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in {x.strip() for x in rec['answers'].split(';')}:continue
    if 'A.152' not in cells[1]:cells[1]+=', A.152'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: the exact dyadic Prym comparison'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+detail,'',
    'Writing pi=sqrt2 gives b=pi²*573*(epsilon*M)². The tangent duplication formula yields exact x-valuation changes. In the only tied case v_pi(x)=1, the two unit-square residues modulo pi^5 give right-side valuations5 and6; only the even case is possible, and its doubled x-valuation is-2. All later doublings subtract4. Thus every nonzero point in [2^n]E(K2) has valuation at most2-4n, proving the intersection of all doubling images is the origin. The actual compatible division-point cocycle then gives injectivity in continuous cohomology.',
    'Odd torsion lies in that intersection; higher2-power torsion would make(0,0) a double, which the first bound excludes. Hence local torsion, and its global subgroup under the field inclusion, are exactly{O,(0,0)}. Complete reductions at17 and41 provide an independent count check. The proper quotient has the two boundary pairs as its exact fibres over these torsion points. All arithmetic fundamental-group and decomposition-group maps are displayed, giving the stated exclusion for a full section ordinary at two. No rank assumption or Tate–Shafarevich finiteness is used.',''])
p.write_text('\n'.join(lines)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
needle='A.150 supplies its particular two-isogeny and covering maps explicitly.'
extra=' II Corollary4.2(b) and Remark4.3, printed pp.64--65, were reopened for A.152: good-reduction injection on torsion prime to the residue characteristic, applied at the split primes17 and41. The dyadic injection is instead proved by its explicit duplication valuation table.'
if 'were reopened for A.152' not in s:
    assert needle in s;s=s.replace(needle,needle+extra,1)
p.write_text(s)
audit=stamp+' A152 complete root proof and independent saved-source audit PASS. Exact duplication formula and every valuation case checked, including nonzero x in the inverse-image intersection and both possible unit-square residues. All finite calculations independently rerun. The direct local torsion argument and field inclusion were checked separately from finite-reduction bounds. Every restriction, compactification, proper quotient and Tate-module comparison is explicit; no implication from one local cusp is asserted. Milne EC2021 II4.2(b)/Remark4.3 reopened for the independent good-reduction check.\n'
for name in ['notes/hour11_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A152.\n'+r.stdout
Path(__file__).with_name('integrate_a152_output.txt').write_text(out);print(out,end='')
