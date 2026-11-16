#!/usr/bin/env python3
"""Integrate exact Prym rank/Sha arithmetic and the two-level norm certificate."""
from pathlib import Path
import datetime,json,subprocess,re
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
records={
 'A.154':{
  'file':'harmonic_prym_rank_zero.tex',
  'answers':'A5; A10; A15; L7; L10; L14',
  'depends_on':'A.150 actual Prym morphisms and exact isogeny Selmer groups; A.152 dyadic Kummer injection; six literal conics and complete tangent-symbol matrix; Fisher Theorem3.1 with exact cubic invariant square; Cassels dual-isogeny adjointness; finite Kummer exact sequences and compatible continuous coboundaries',
  'uses_local_theorem':'no; full Selmer localizations are part of the stated domain',
  'manuscript_passages':'cote149; scans56–58; explicit rigid elliptic target and actual full-section comparison',
  'notes':'E_b/Q(sqrt2) has rank0 and exactly{O,(0,0)} rational points. Its full2-Selmer group has dimension3 and Sha[2∞]=Sha[2]=C2², with nondegenerate pairing and zero T2Sha. A rank4 tangent-symbol pairing on six isogeny classes gives the independent upper bound8; a separately certified full two-cover pairing is nonzero, with exactly three negative local symbols. All exceptional local points, omitted-prime support, primitive Bezout identities, literal covariant maps, T0 translation, and real places are checked. No software Selmer-group order or analytic rank is used. Every full Selmer section on the harmonic curve overQ orK has dyadic cuspidal localization, via finite Kummer sequences and the actual proper Prym morphism. Ordinary points in odd formal neighborhoods have zero2-adic Kummer class, so the stated scope does not infer all-place cuspidality. Root and independent saved-source/map/arithmetic audits passed.',
  'detail':'A.154 proves rank0, full2-Selmer order8, and Sha[2∞]=C2² for the complementary Prym factor; every full Selmer section on the harmonic cover has cuspidal localization at two.'},
 'A.156':{
  'file':'two_inert_norm2_generator_agent.tex',
  'answers':'A5; A9; A15; L10; L14; L20',
  'depends_on':'A.155 actual distinguished class; explicit degree9 Eisenstein field; exact table-first multiplication arithmetic, integer characteristic polynomial, Bareiss determinant and relative norm; unique degree-one prime over2',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58 and126–127; actual target norm family and compatible field maps',
  'notes':'For a=3*649^24, a literal integral element gamma in K2=Q(t), t^9=3*649^6, has relative norm alpha-1 in K1=Q(alpha), alpha³=3. Thus beta2=-gamma extends the fixed seed beta1=1-alpha with norm-2 overQ. Its principal ideal is the unique norm-two prime, so the actual e2 of A.155 vanishes. All36 base10^40 blocks and signs are reconstructed directly from TeX by an independent certificate; integer Newton identities, Bareiss determinant, characteristic divisibilities, annihilation, and relative norm are verified. The class-group presentation was used solely to discover the element. No full compatible tower is inferred.',
  'detail':'A.156 gives a literal integral degree-nine norm-two generator, proves e_2=0, and extends the fixed first seed1−cuberoot3 by one exact relative norm.'}
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
for ident,anchor in [('A.154',r'\input{sections/two_prime_finite_support_persistence_agent.tex}'),('A.156',r'\input{sections/balanced_class_norm_criterion_agent.tex}')]:
 entry=r'\input{sections/'+records[ident]['file']+'}'
 assert anchor in s
 if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
p=w/'notes/register_metadata.json';metadata=json.loads(p.read_text())
for ident,rec in records.items():metadata[ident]={k:v for k,v in rec.items() if k not in {'file','detail'}}
p.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
fragment=(w/'notes/harmonic_prym_second_descent_references.bib').read_text()
for entry in re.split(r'(?=@\w+\{)',fragment):
 if not entry.strip():continue
 key=re.search(r'@\w+\{([^,]+),',entry).group(1)
 if re.search(r'@\w+\{'+re.escape(key)+',',s):continue
 if key=='AgentFisherBinaryQuartics2022':
  entry=entry.replace('f35e7d09-f88e-4058-959d-b8153d7708cf','bf57c387-4c32-41bc-a226-cf470e228523')
  entry=entry.replace('Verified:', 'verified:')
  entry=entry.replace('Theorem 3.1 and Remark 3.2 were also checked for the separate full-pairing certificate.', 'The root independently reopened Theorem3.1, Remarks3.2--3.3, Lemmas2.1,5.1,6.1,6.3, Proposition7.2, Corollary7.3, Theorem8.2 and the full final proof for A.154, checking the exact invariant, normalization, cyclic-algebra and local-product maps.')
 if key=='AgentCasselsIsogenies1965':
  entry=entry.replace('Verified:', 'verified:')
  entry=entry.replace('without assuming finiteness of the Tate--Shafarevich groups.', 'without assuming finiteness of the Tate--Shafarevich groups. The root visually reopened the original printed pp.181,187--188 and followed the torsor map (2.5), pulled-back functions (2.7), compatible local points (2.8), and equality (2.9).')
 s+='\n'+entry.strip()+'\n'
p.write_text(s)
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=3:continue
 for ident,rec in records.items():
  if cells[0] in {x.strip() for x in rec['answers'].split(';')}:
   if ident not in cells[1]:cells[1]+=', '+ident
   if rec['detail'] not in cells[2]:cells[2]+=' '+rec['detail']
 lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: exact Prym rank and a literal norm extension'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+records['A.154']['detail']+' '+records['A.156']['detail'],'',
 'The Prym calculation has two independent arithmetic parts. Six literal conic points produce tangent functions with divisor twice the specified rational kernel point. Their complete local Hilbert matrix has rank4. The actual two-isogeny sequence has a kernel of order2, and Cassels dual-isogeny adjointness puts the full2-Selmer image in the matrix radical of dimension2, giving order at most8. A separate Fisher pairing on full two-covers has negative symbols exactly at(41,17),(139,inert), and(38709401,15703973); every other finite and both real symbols equal1. Primitive integral Bezout identities, full component-denominator support, direct dyadic Hensel witnesses, and all omitted places are certified.',
 'The nonzero full pairing and the rational torsion Kummer class force full2-Selmer dimension3 and rank0. The induced pairing on the two-dimensional Sha[2] is nondegenerate. Bilinearity makes twice every Sha[4] class orthogonal to Sha[2], hence zero; all higher2-power orders are thereby excluded. Thus Sha[2∞]=C2² and T2Sha=0 without a finiteness hypothesis. Every full Selmer section maps through the actual proper Prym morphism to a continuous2-adic Kummer class of one of the two global torsion points. Exact dyadic injectivity gives the stated boundary fibres. The proof explicitly constructs ordinary odd-place points in the Kummer kernel, retaining the precise localization scope.',
 'For the two-prime norm tower, the degree-nine search produced an algebraic number whose monic integral characteristic polynomial, exact multiplication determinant2, and relative norm alpha−1 are verified using only rational and integer arithmetic. An independent program reads all36 base10^40 blocks directly from the manuscript, computes the characteristic polynomial by Newton identities and determinant by fraction-free Bareiss, and checks annihilation and the relative norm. The unique degree-one prime over2 is therefore principal, proving the actual target class e2=0. The resulting beta2 maps exactly to the specified beta1=1−alpha. No class-group completeness or coherent infinite family is claimed.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A154/A156 root audits PASS. A154: exact isogeny tangent divisor/Jacobian maps, local kernel and dual adjointness, rank4 matrix, all full quartic invariants/maps/ELS, complete Fisher product and support, rank/Sha deduction, continuous Kummer and dyadic section comparisons checked. Cassels printed187–188 visually reviewed. A156: all field embeddings, scalar unit correction, integrality/norm and prime identification checked; independent TeX-table-first certificate rerun PASS. All active statements retain their exact scope.\n'
for name in ['notes/hour11_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A154 and A156.\n'+r.stdout
Path(__file__).with_name('integrate_a154_a156_output.txt').write_text(out);print(out,end='')
