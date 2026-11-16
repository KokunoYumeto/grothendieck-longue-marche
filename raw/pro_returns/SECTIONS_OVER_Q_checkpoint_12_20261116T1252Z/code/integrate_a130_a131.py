#!/usr/bin/env python3
"""Integrate audited finite cyclic repair and stable allocated-prime norms."""
from pathlib import Path
import datetime,json,subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/relative_precision_forms_agent.tex}'
assert anchor in s
for source in ['relative_cyclic_precision_agent.tex','stable_local_norm_agent.tex']:
 text=(w/'sections'/source).read_text()
 assert r'\!left(' not in text
 entry='\\input{sections/'+source+'}'
 if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
 anchor=entry
p.write_text(s)

p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.130']={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.115; A.117; A.122; A.129; Milne ADT I4.10(b),4.15; proved odd-prime-power extension of Schmidt–Wingberg Theorem13',
 'uses_local_theorem':'no; explicit finite-module duality and norm-torus Kummer maps',
 'manuscript_passages':'cote149; scans56–58,126–127; finite relative norm repair at arbitrary coefficient precision',
 'notes':'Identifies exactly the old-local image of relative classes at every precision3^r with cyclic or inertia-generated new images at split permitted primes. The full reciprocity conditions are exactly the included mod-three quadratic forms of A129. The complete odd-power scalar proof retains the Hilbert signs, an actual Chebotarev cancellation, bounded-character extension in a fibre product and underlying cyclic-summand induction. Finite abelian double-annihilator duality supplies the required corestriction input; old classes remain at full3^r precision and local torus prescriptions give actual global norm-one elements. Root and local_preprint full audits and all retained finite certificates passed. No cross-precision norm-chain compatibility or stable branch condition is inferred.'
}
meta['A.131']={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'actual tame field norms, residue norm and scalar principal-unit power maps; compact fixed-valuation norm fibres; A.106 allocated-prime coordinates',
 'uses_local_theorem':'no; explicit local multiplicative groups and field norms',
 'manuscript_passages':'cote149; scans56–58,126–127; full local norm-tower condition at allocated coefficient primes',
 'notes':'Computes the norm image from every tame pure3-power field and its exact compatible inverse-limit image, stabilizing at3^v3(q−1), for both ordinary and completed local multiplicative groups. It retains every root-branch unit character in the norm-chain update. Relative block sums give exact moment conditions; a scalar-shifted cyclic graph satisfying the full equations forces every inertia valuation divisible by3. This proves why primitive inertia from finite cyclic repair does not automatically solve the stated stable branch equations. Root and local_preprint full audits passed; root executed the residue, transition, block and551880 primitive-inertia systems. No restriction is asserted for an unspecified lower representative.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
items={'A5','A9','A15','L10','L14','L20'}
detail=('A.130 extends the exact cyclic auxiliary repair image to every finite three-power precision, with all old classes retained and inertia-generated new images. A.131 computes the full stable local norm condition and an actual compatible local family; its root-branch term forces primitive cyclic graphs to fail for the stated relative norm-one target. The global chain still requires a repair satisfying these retained branch equations.')
changed=0
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[z.strip() for z in line.strip().strip('|').split('|')]
 if len(cells)!=3 or cells[0] not in items:continue
 for identifier in ['A.130','A.131']:
  if identifier not in cells[1]:cells[1]+=', '+identifier
 if detail not in cells[2]:cells[2]+=' '+detail
 lines[i]='| '+' | '.join(cells)+' |'
 changed+=1
heading='## Finite cyclic repair and full stable local norm equations'
if heading not in lines:
 lines.extend(['',heading,'',stamp+': '+detail,
 'The odd-prime-power extension of the opened Schmidt–Wingberg argument is proved in full: its scalar construction uses the inverse of two, precise local Hilbert products and a repeated finite vector. The induction uses an explicit extension of bounded characters from a fibre-product kernel. Transported corestriction distributions have as their full annihilator the bilinear forms already computed in A.129. Their quadratic sums are precisely the finite image obstruction. This produces actual torus points for local Kummer prescriptions at each fixed precision.',
 'At an allocated prime q≠3, a uniformizer with its exact norm and the residue-unit map compute all norm groups. Compactness is used only for closed fixed-valuation fibres in finite local fields, where it supplies genuine compatible families. The stable equations contain the branch difference κ3^(s−n)i. Summing in each relative block gives its moment constraint. Substituting a scalar-shifted cyclic graph into those full equations forces every inertia coordinate divisible by three, including in stable precision three. This comparison records the remaining local shape required by a global construction.',''])
p.write_text('\n'.join(lines)+'\n')

audits=[
 'A130 root and local_preprint full audits passed: scalar odd-power Chebotarev functional, both Hilbert-product signs, bounded-character extension, cyclic-summand induction with nonstable arithmetic summands, actual corestriction and inertia order; full cocycle-field product, transported affine duality, finite double-annihilator and actual torus realization. Root independently reran the certificate:five exact annihilator modules,368 full finite-ring affine systems and1092 bounded fibre-product characters, all passed. The A130.3 display typo was fixed before integration.',
 'A131 root audit passed the original source and the complete primitive-inertia append: exact tame degrees and uniformizers including negative valuations; full unit norm image; compact norm-fibre finite-intersection argument; completed local quotient; all branch characters and block moments; scalar-shifted graph inverse expansion and zero-coefficient case. Local independently passed the original proof and was sent the append. Root reran7980 residue norm cosets,31920 transition identities,1890 stable intersections,4401 block moments,110 branch-depth tests and551880 graph systems, all passed.'
]
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
 p=w/name
 s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
 for audit in audits:
  if audit not in s:s+='\n'+stamp+' '+audit+'\n'
 p.write_text(s)
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out=f'Integrated A130 and A131 in numerical order; updated {changed} outcome rows.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a130_a131_output.txt').write_text(out)
print(out,end='')
