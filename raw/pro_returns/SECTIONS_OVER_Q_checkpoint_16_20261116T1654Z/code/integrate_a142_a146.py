#!/usr/bin/env python3
"""Integrate the fully audited A142--A146, preserving unresolved item outcomes."""
from pathlib import Path
import datetime, json, subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
entries=[
 ('A.142','tripod_reciprocity_obstruction.tex'),
 ('A.143','harmonic_elliptic_positive_rank.tex'),
 ('A.144','successful_radicand_update_agent.tex'),
 ('A.145','uniform_harmonic_detector_family.tex'),
 ('A.146','harmonic_infinite_primary_obstruction.tex')]
p=w/'SECTIONS_OVER_Q_paper.tex';text=p.read_text()
anchor=r'\input{sections/harmonic_proper_finite_obstruction.tex}'
for key,name in entries:
    assert (w/'sections'/name).is_file()
    entry=r'\input{sections/'+name+'}'
    assert anchor in text
    if entry not in text:text=text.replace(anchor,anchor+'\n'+entry,1)
    anchor=entry
p.write_text(text)

p=w/'SECTIONS_OVER_Q_references.bib';text=p.read_text()
for name,key in [('legendre_elliptic_factor.bib','LegTunnell1983'),
                 ('legendre_infinite_primary.bib','LegMontgomeryVaughan1973')]:
    if '{'+key+',' not in text:text+='\n'+(w/'notes'/name).read_text()
old='V, Propositions 8.1 and 8.3 give the good-reduction Frobenius comparison.'
new=old+' Reopened for A.143: IV, Theorem 4.7(a) and Proposition 4.13, printed pp.122 and125, give the finite bounded-height set and its generation from representatives of E(Q)/2E(Q); here that quotient has been computed to have sixteen elements.'
if 'Reopened for A.143: IV' not in text:
    assert old in text;text=text.replace(old,new,1)
p.write_text(text)

data={
'A.142':{
 'answers':'A5; A8; A9; A12; A15; L2; L9; L10; L14; L17; L20',
 'depends_on':'A.134 actual quartic initialization and signed prime refinement; A.132 exact all-place comparison; A.90 mixed boundary stabilizers; exact prime4679 witness',
 'uses_local_theorem':'no; ordinary local points and full completed coordinates are constructed directly',
 'manuscript_passages':'cote149; scans56–58,126–127; lifting over a new puncture with fixed local centres',
 'notes':'Constructs an ordinary completed tripod pair with infinite integer support in both coordinates. Its new coordinate at b=-715208/36481 is a unit outside the fixed explicit finite set S0 but has quadratic reciprocity invariant1/2 only at4679. Thus the finite-coefficient restricted-product conditions all hold and the exact character orthogonality fails. All old and new local centres are fixed throughout cofinal coordinate refinements. The finite certificate checks611 retained centres,1833 fourth-power conditions, the three literal4679 roots and symbol, the boundary fields and216 mixed bounds. The proof, not a purported finite execution of infinitely many steps, supplies the construction. Full independent and root source audits/certificate reruns passed.'},
'A.143':{
 'answers':'A5; A7; A10; L7; L10; L15',
 'depends_on':'A.139 actual cyclic genus-three curve; explicit degree-two map and two-isogenies; complete elementary two-isogeny descent; Milne IV4.7(a)/4.13; Tunnell Theorems1/3; audited AP-D.25 Selmer integrality',
 'uses_local_theorem':'no; the full-section exclusion is stated in the Selmer range throughout',
 'manuscript_passages':'cote149; scans56–58; positive-rank elliptic images of full Selmer sections',
 'notes':'The actual order-four quotient Dbar→F factors through E:y²=x³-1146²x and F:v²=u³+573²u, with both maps and dual isogeny written explicitly. Exact squareclass descent gives rank2 for both and surjectivity E(Q)→F(Q); two independent rational points and their images are computed. The signed theta coefficient b(573)=0 is checked in three ways and Tunnell’s exact formula gives the central L-value zero, without exact analytic-rank or Sha claim. Every non-torsion completed F(Q) class with finite primary support has no full Selmer lift to D°. A positive-density set of primes forces its exact local elliptic image into the two boundary images, and audited density-one integrality forces a global cusp. Full source audit, original Tunnell scan comparison, and independent exact certificate reruns passed.'},
'A.144':{
 'answers':'A5; A9; A15; L9; L10; L14; L20',
 'depends_on':'A.138 exact unit cofactor; A.131 full tame stable norm formula; A.140 wild actual norm surjectivity; explicit full decomposition group; Oki Proposition6.4/Corollary6.5',
 'uses_local_theorem':'no; local class field theory and global norm-torus duality are used on actual fields',
 'manuscript_passages':'cote149; scans56–58,126–127; norm-family compatibility for a changed rational radicand',
 'notes':'For q=511177, gamma=-68+64alpha+alpha² has norm q in Q(alpha), alpha³=3. The specific beta=(1-alpha)(alpha²-2)q/gamma³ has norm-2 and is a norm from every finite level of the single tower with theta0=alpha q^8. Every local norm system has a compatible actual family; every finite global chain has a solution. The exact local image at q has independent tame/unramified vectors(1,1,1) and(0,2,1), yet all stable norm equations hold. The full local decomposition group at3 kills the finite global Hasse-norm obstruction. A compatible global infinite family and a completed ordinary pair are not obtained. Full independent/root source audits and exact arithmetic certificate reruns passed; root reopened Oki’s primary p35 and verified both general torus statements.'},
'A.145':{
 'answers':'A5; A8; A9; A12; A15; L2; L9; L10; L14; L17; L20',
 'depends_on':'A.139 all ordinary local sheets; A.141 proper corrected central class and order512 quotient; A.142 double-fibre unit invariant; A.90 exact nonunit-root refinement',
 'uses_local_theorem':'no; finite-quotient local hypotheses and full Selmer consequences are retained explicitly',
 'manuscript_passages':'cote149; scans56–58,126–127; finite/metabelian detection and lifting at a new puncture',
 'notes':'One fixed quotient of order512 and class6 excludes every section with the specified combined mod-eight character and ordinary centres at nine primes, allowing any ordinary or cuspidal local image elsewhere. Proper boundary values are computed explicitly at all four cusps. A binary tree of exact cofinal refinements constructs continuum many distinct ordinary completed pairs with this obstruction; common prefixes preserve every fixed coefficient quotient, making a continuous injection with compact image. The same prime at each pair of children records a permanent valuation0 versus n0; the nonunit root is absorbed by the exact rational valuation factor, and extra fresh primes preserve infinite support on all paths. All pairs retain A142’s restricted-product quadratic obstruction. The full metabelian/class6 conclusions apply through the actual maps with local matching. The finite q=1065217 node, all five Hensel lifts, splitting characters, unit differences and valuation gap were executed and independently audited.'},
'A.146':{
 'answers':'A5; A7; A10; L7; L10; L15',
 'depends_on':'A.143 exact rank-two factor and surjective isogeny; explicit good integral plane-quartic model; Montgomery–Vaughan Theorem2/(1.10); finite cyclotomic Chebotarev; audited AP-D.25 Selmer integrality',
 'uses_local_theorem':'no; full Selmer sections, functorial compact Kummer maps and actual reduction maps suffice',
 'manuscript_passages':'cote149; scans56–58; positive-rank completed multiples and local nonintegrality',
 'notes':'For every odd coefficient-prime set S with counting O(X^delta), delta<1/2, every non-torsion class in M2 × product_{ell in S}Mell × product_{odd ell outside S}ell Mell has no full Selmer lift to D°. The detecting primes have the proved positive Euler-product density, avoid ell|p+1 for ell in S and ell²|p+1 outside S, and are3 modulo8. Four explicit tail bounds justify the infinite sieve. The actual integral maps make reductions into the two elliptic boundary images force nonintegral tripod images. This includes sparse infinite support and explicit zR with z2=1 and zell=ell at every odd ell, all primary components nonzero. All remaining completed multiples are still unclassified. The certificate checks8 CRT patterns/161280 residues,5776 curve points at47 primes, and111648 E-points at82 detecting primes. Full independent/root proof audits, original Brun–Titchmarsh source checks and exact reruns passed.'}
}
p=w/'notes/register_metadata.json';meta=json.loads(p.read_text());meta.update(data);p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
details={
'A.142':'A.142 constructs fixed ordinary tripod data whose added coordinate is a unit outside one finite set but has a nonzero quadratic reciprocity sum.',
'A.143':'A.143 computes an actual rank-two elliptic quotient, central L-value zero, and excludes every non-torsion finite-primary completed class from full Selmer lifts to its punctured cover.',
'A.144':'A.144 gives one explicit changed radicand and representative passing every local compatible norm system and every finite global norm level; the global inverse family remains open.',
'A.145':'A.145 proves a uniform nine-place obstruction through one order512/class6 quotient and a continuous binary family of continuum many ordinary completed pairs it excludes.',
'A.146':'A.146 excludes an explicit infinite-primary subgroup, including completed multiples with every primary component nonzero, by exact integral reduction maps and a positive-density prime sieve.'
}
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3:continue
    for key,record in data.items():
        if cells[0] not in {z.strip() for z in record['answers'].split(';')}:continue
        if key not in cells[1]:cells[1]+=', '+key
        if details[key] not in cells[2]:cells[2]+=' '+details[key]
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: fixed-local reciprocity, positive-rank lifts, and exact norm updates'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+' '.join(details.values()),'',
    'The restricted-product example fixes the extra puncture b=-715208/36481. The exceptional prime4679 has an ordinary point on the initial quartic cover with unit roots, while its new-coordinate valuation is one and the fixed quadratic character is nonsplit. All other new-coordinate invariants are zero. Removing both fibres over c and1-c at each later mixed cover keeps the new coordinate a unit outside the original finite controlled set. Thus this example satisfies the restricted-product part of the exact global comparison and fails its character pairing.',
    'The rank-two calculation gives literal degree-two maps from the genus-three curve to E and from E to F, and the dual isogeny. The first squareclass descent has sixteen classes and the second is trivial; exact height finiteness and generation supply the finite-basis step. The two independent rational points, three computations of the relevant signed theta coefficient, and Tunnell’s opened central-value formula give the stated rank and L-value assertions. There is no assertion about the exact positive analytic rank or the Tate–Shafarevich group.',
    'For the infinite-primary extension, the good integral plane quartic and its maps have exactly four boundary points over the two elliptic target points, including after reduction. The prime set is defined by avoiding first-power divisors from a sufficiently sparse set and square divisors elsewhere. Its density follows from finite cyclotomic residue counts, the original Montgomery–Vaughan bound for small moduli, and explicit integer-counting tails for large moduli. At every such prime, the completed elliptic class reduces into the two boundary images. This forces nonintegrality of any local ordinary lift; the audited density-one integrality theorem in its Selmer scope then forces a global cusp and contradicts the non-torsion elliptic class. Profinite unit multiples remain among the concrete classes not decided by this argument.',
    'The uniform finite detector retains the original centres at only nine primes. All four proper boundary values are zero elsewhere, and the actual inertia-orbit comparison proves this for arbitrary cusp packets. The binary construction uses a fresh prime common to the two children, with a unit-root point on one child and a root of valuation one on the other. Its exact rational valuation factor handles the latter during refinement. The persistent tripod valuation separates the paths. Extra fresh coefficient primes maintain both infinite supports, including on the all-zero path. Prefix agreement fixes all coefficient classes at each prescribed exponent, proving continuity and a compact Cantor image in the Hausdorff exponent-completion space.',
    'For the changed norm tower, the exact representative has a two-dimensional local image at the new prime, with sheared tame and unramified vectors satisfying the full stable equations. The wild norms at3 are onto, and a local decomposition group equal to the full Galois closure group kills the finite global torus obstruction by the opened general duality statement. This proves every finite global chain and compatible local families. The proof does not produce a compatible global infinite family; that is the next retained obstruction.',
    'All five saved proofs have independent audits and executed finite certificates; root reruns and primary-source checks are recorded in notes/hour10_root_audits.md. Both principal A1 assertions remain open. No item outcome is promoted merely from a proved route or family.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+''' A142--A146 integrated after full proof audits. Root reran all exact certificates. A142: retained611 centres/1833 fourth conditions, exceptional4679 local roots and symbol,216 bound checks. A143: literal maps, duality/compositions, sixteen descent classes, all three F quartic exclusions, exact rank, signed theta/ternary/product coefficients and15 good-prime two-primary checks. Milne IV4.7(a)/4.13 supplies the exact finite-basis deduction; the original Tunnell scan was independently compared. A144: prime/norm/divisor identities, six cube roots, all three stable local symbols, and actual local/global field maps. Oki primary arXiv2508.10706v2, printed p35 Prop6.4/Cor6.5, reopened and visually inspected; its general torus statements have no prime-squared-degree restriction. A145: every proper cusp value, actual finite quotient/cusp transfer, signed nonunit-root CRT factor, binary scheduling/injection and cofinal completion. Both finite-node programs independently passed. A146: explicit smooth integral model and maps, all fibre multiplicities, exact density and four tails, all primary reduction maps including physical p, and Selmer transfer. Original Montgomery--Vaughan Theorem2/(1.10), printed p121, visually checked; root certificate independently passed8 CRT patterns/161280 residues,5776 D-points/47 primes,111648 E-points/82 primes. Global changed-tower compatibility and both A1 assertions remain open.
'''
for name in ['notes/hour10_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as f:f.write('\n'+audit)
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out='Integrated audited A142--A146.\n'+result.stdout
Path(__file__).with_name('integrate_a142_a146_output.txt').write_text(out);print(out,end='')
