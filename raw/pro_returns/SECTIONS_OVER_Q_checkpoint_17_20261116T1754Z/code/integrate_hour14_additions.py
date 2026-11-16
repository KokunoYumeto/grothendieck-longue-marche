#!/usr/bin/env python3
"""Integrate only explicitly selected, completely audited hour-fourteen results."""
from pathlib import Path
import datetime, json, subprocess, sys

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
specs = {
 'A.178': {
  'file': 'metabelian_finite_support.tex',
  'before': 'two_inert_all_height_balanced_vanishing.tex',
  'heading': 'Finite support in one abelian-cover quotient and the full metabelian quotient',
  'detail': 'A.178 classifies every locally point/cusp-matching section with density-one finite proper support in the actual quotient E_X/H_3\u2032 and in the full geometric metabelian quotient, for every hyperbolic curve over a number field. Each is the image of a unique actual full point or cusp class. It also determines every rational Abel\u2013Jacobi fibre, including its complete injective cusp parameter.',
  'answers': 'A1; A5; A7; A10; A11; A15; L3; L7; L10; L12; L14; L15; L19',
  'depends_on': 'A.169 completed Kummer localization and nonsplit boundary recovery; Harari\u2013Stix Theorem2.1 and Remarks2.2(3) in the 2011 author version; Stoll Theorem8.2 and Proposition3.7 with 2017 errata; actual profinite surface and finite-cover maps',
  'notes': 'The original arithmetic section defines the actual characteristic abelian covers. Their genus and boundary formulas include the one-puncture case. Before a rational origin is available, the quotient section pulls back every finite commutative torsor to a global class; local evaluation agrees with its restrictions. Stoll8.2 then supplies a rational proper centre. The exact inverse-Selmer localization and nonsplit primitive inertia module recover the full affine point or cusp class. Reference injectivity on the single level-three cover fixes one full reference through every higher cover, and the compact conjugator intersection is exactly Pi double-prime. The closed Abel\u2013Jacobi immersion gives the rational compact-Kummer corollary. Root and both peers read the complete final proof and primary source passages, and independently reran the certificate. No arbitrary metabelian local geometricity or finite support is asserted.',
  'uses_local_theorem': 'no; locally matching quotient sections are the explicitly stated domain'
 },
 'A.180': {
  'file': 'two_inert_discrete_norm_fibre.tex',
  'before': None,
  'heading': 'The actual norm fibre through its full divisor classes and unit lattice',
  'detail': 'A.180 identifies the exact image of the actual infinite norm fibre: one stable integer valuation profile must satisfy the full ordinary principal-ideal tests and its actual norm-one-unit defect must vanish. It determines all completed valuation profiles by a single equation in the inverse cyclic three-class group, and constructs the exact connecting map from the completed-unit lattice quotients.',
  'answers': 'A5; A9; A15; L10; L14; L20',
  'depends_on': 'A.165 literal prime generators; A.166 actual and completed support identity; A.173 and A.176 evaluated class coordinates; A.177 changed-prime generation; A.179 cyclic three-class groups and completed norm family',
  'notes': 'The changed-prime divisors are killed by explicit powers of three in the full ordinary class group. Hence their integer combination cancels the distinguished two-prime exactly when both its prime-to-three component and the compatible cyclic three-class equation vanish. Actual generators of these principal fractional ideals can be given rational norm minus two by the odd-degree sign map. Their successive norm discrepancies lie in actual norm-one global units and define a choice-independent lim1 class; its vanishing is proved equivalent in both directions to an actual coherent family. Completed units are compact, and the proof gives the literal comparison through lim of completed units modulo the embedded unit lattices. Every two-prime primary class equals its residue degree times the distinguished one. Root and birational audits cover every map; the finite certificate is retained. The actual infinite family, the unevaluated prime-to-three classes and the unit defect remain unresolved.',
  'uses_local_theorem': 'no'
 },
 'A.181': {
  'file': 'two_inert_evaluated_norm_phantom.tex',
  'before': None,
  'after': 'two_inert_discrete_norm_fibre.tex',
  'heading': 'An evaluated nonzero continuous norm obstruction',
  'detail': 'A.181 evaluates a nonzero actual and completed derived-limit norm class in the fixed tower over Q(cuberoot(3)). The explicit unit B=(alpha^2-2)^3 is an actual field norm from every finite height, but has no infinite compatible actual or completed family. Its cohomology image in the specified one-variable pro-three metabelian quotient is nonzero while every local, root-torsor and finite-coefficient image is zero.',
  'answers': 'A5; A9; A15; L9; L10; L11; L14; L20',
  'depends_on': 'A.159 explicit degree-nine unit basis and tame characters; A.166 affine-prime support argument; A.173 and A.177 changed-prime class generation; Milne CFT III Theorem3.5; Oki Proposition6.4; actual Fox-specialized metabelian module and continuous cochain maps',
  'notes': 'The degree-twenty-seven S-unit norm obstruction has exact order three, and the all-height field norm assertion uses the full decomposition group at three in a literal Galois splitting field. Every infinite family over a unit is forced into global units by the uniformly growing residue-degree coefficients outside the totally ramified primes. The Milnor injection identifies the evaluated norm defect with the negative of the connecting cohomology class, with its sign fixed by an explicit cochain. The actual one-variable quotient, root-torsor modules and finite coefficient projections are constructed. A separate divisor correction proves every one-step global-unit field norm is a global-unit norm. Root and local peer audited the full proof and independently ran the retained finite certificate. No order is assigned to the derived-limit class, and no ordinary locally point-matching unit-equation pair is produced.',
  'uses_local_theorem': 'no'
 },
 'A.182': {
  'file': 'point3_fermat8_decomposition.tex',
  'before': None,
  'after': 'two_inert_evaluated_norm_phantom.tex',
  'heading': 'All twelve rational factors of the pointed Fermat-eight Jacobian',
  'detail': 'A.182 constructs a rational isogeny from the genus-twenty-one pointed Fermat-eight Jacobian to three elliptic curves and nine abelian surfaces. Every factor is rationally simple and has an explicit infinite-order rational point, giving rank at least twelve. Every nonzero rational abelian quotient has positive rank; the actual Weil-restriction adjunction then excludes every nonconstant map over any number field to an abelian variety with a finite group of points over that field.',
  'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
  'depends_on': 'Literal maps from 3u^8-2v^8=1; all twenty-one cotangent identities; exact good-reduction counts and divisor nonvanishing; Milne Abelian Varieties III Proposition6.1, III Theorem11.1, II Theorem1.1 and IV Theorem3.5',
  'notes': 'The certificate re-executes both companion surface certificates and checks all literal maps, nonzero differential scalars, torsion bounds and Frobenius irreducibility. Rational simplicity is deduced from the actual good-reduction Tate-module sequences; the quotient rank argument uses an inverse isogeny up to multiplication and does not assume pairwise nonisogenous factors. The field-extension conclusion is proved through the functorial Weil-restriction map and the pointed Jacobian universal property. Root and birational peer audited the complete source and independently executed the local certificate. No external rank computation is used. An upper rank bound, section classification and the remaining level-twenty-four factors stay unresolved.',
  'uses_local_theorem': 'no'
 },
 'A.183': {
  'file': 'two_inert_first_weight_vanishing.tex',
  'before': None,
  'after': 'point3_fermat8_decomposition.tex',
  'heading': 'A vanishing cup and an explicitly detected integral weight',
  'detail': 'A.183 evaluates the first-weight image of the A181 obstruction as the zero cup kappa(A) cup kappa(U^3), with its positive sign fixed. The same nonzero class survives in the explicit integral quotient D_A/T^14, although every finite coefficient image over the absolute Galois group is zero. Its least detecting quotient index lies between two and fourteen, and its nonzero image belongs to the specified coefficient-power lim1 subgroup.',
  'answers': 'A5; A9; A15; L10; L11; L14; L20',
  'depends_on': 'A.138 base three-class group; A.177 and A.179 S-three-class vanishing; A.181 evaluated unit norm and root-torsor obstruction; A.81 weight/coefficient Milnor maps; Milne ADT I Corollary4.15 and II Propositions2.1/2.9; Jannsen1988 exact inverse-limit and support maps',
  'notes': 'The exact Kummer sequence on O_F[1/3] and its Brauer invariant map give zero integral H2 in Tate weight two. The nine added residue-prime groups have exponent three, and restriction-corestriction of degree two transfers this to k. The finite-set norm cokernel contains U of exact order nine and embeds in H2 of the rank-eight augmentation kernel; its quotient maps to a torsion-free induced Tate group. Therefore the U-cube class survives modulo nine. Exact polynomial division gives T^14 in (9,L2). A direct normalized-cochain proof makes integral inflation injective, retaining the zero absolute finite-coefficient images. The integral weight inverse-limit map and the coefficient-power lim1 injection are written separately. Root and birational peer audited the full proof, primary passages and executed certificate. No least index within two through fourteen is assigned.',
  'uses_local_theorem': 'no'
 },
 'A.184': {
  'file': 'two_inert_secondary_unit_character.tex',
  'before': None,
  'after': 'two_inert_first_weight_vanishing.tex',
  'heading': 'An exact secondary unit-character equation at every height',
  'detail': 'A.184 determines every one-step global-unit norm image as the kernel of its two tame characters, proves those characters vanish on all relative norm-one global units, and constructs the resulting secondary homomorphism on that actual norm image. Its kernel is exactly the two-step global-unit norm image, with psi_n(u^3)=theta_n(u), both for actual units and their pro-three completions. The fixed U-cube obstruction consequently persists over every shifted base of the same tower.',
  'answers': 'A5; A9; A15; L10; L11; L14; L20',
  'depends_on': 'A.173 and A.177 actual class extension/norm maps; A.179 persistent anti-invariant cubic class characters; A.181 one-step global-unit support repair and full-decomposition norm argument; Hilbert90 and exact unit-lattice completion',
  'notes': 'The seven ramified-prime residues of the Hilbert90 divisor are compared with the actual relation jA_n=3A_(n+1). The pure involution fixes the linear residue branch and exchanges the other two with opposite exponents. The persistent two-by-two class-character matrix is invertible, forcing both quadratic-branch residues to be one. This proves preimage independence of the secondary homomorphism. Every local condition, actual Hasse norm map, support repair and degree-two norm transfer is retained. Flat completion preserves the exact finite unit lattices. Root and Legendre peer read the entire proof and independently executed the certificate. No stabilization of distant norm images, relative S-unit-kernel vanishing, or ordinary locally point-matching unit-equation pair is inferred.',
  'uses_local_theorem': 'no'
 }
}
selected = sys.argv[1:]
assert selected and all(k in specs for k in selected), selected
meta_path = w/'notes/register_metadata.json'
meta = json.loads(meta_path.read_text())
paper_path = w/'SECTIONS_OVER_Q_paper.tex'
paper = paper_path.read_text()
report_path = w/'SECTIONS_OVER_Q_report.md'
lines = report_path.read_text().splitlines()
assert lines[0] == 'INCOMPLETE'
for key in selected:
    spec = specs[key]
    source = w/'sections'/spec['file']
    assert ('{'+key+'}{Proved}') in source.read_text()
    include = '\\input{sections/'+spec['file']+'}'
    if include not in paper:
        anchor = ('\\input{sections/'+spec['before']+'}') if spec['before'] else ('\\input{sections/'+spec.get('after', 'two_inert_all_height_balanced_vanishing.tex')+'}')
        assert paper.count(anchor)==1
        paper = paper.replace(anchor, include+'\n'+anchor if spec['before'] else anchor+'\n'+include, 1)
    record = {k: spec[k] for k in ['answers','depends_on','notes','uses_local_theorem']}
    record['manuscript_passages'] = 'cote149; scans54\u201358 and126\u2013127; exact section and norm comparison maps'
    meta[key] = record
    answers = {a.strip() for a in spec['answers'].split(';')}
    for i,line in enumerate(lines[:55]):
        if not line.startswith('| '): continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells)==3 and cells[0] in answers:
            if key not in cells[1]: cells[1] += ', '+key
            if spec['detail'] not in cells[2]: cells[2] += ' '+spec['detail']
            lines[i] = '| '+' | '.join(cells)+' |'
    heading = '## Continued work: '+spec['heading']
    if heading not in lines:
        lines += ['',heading,'',stamp+': '+spec['detail'],'',spec['notes'],'']
    audit = stamp+' '+key+' integrated after complete saved-source audit and actual map checks. '+spec['detail']+'\n'
    for name in ['notes/hour14_root_audits.md','notes/root_progress.md']:
        with (w/name).open('a') as f: f.write('\n'+audit)
paper_path.write_text(paper)
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False)+'\n')
report_path.write_text('\n'.join(lines)+'\n')
proc = subprocess.run(['python',str(w/'code/build_register.py')],capture_output=True,text=True,check=True)
out = 'Integrated audited sections: '+', '.join(selected)+'\n'+proc.stdout
suffix = '_'.join(x.replace('.','') for x in selected)
(w/'code'/('integrate_hour14_'+suffix+'_output.txt')).write_text(out)
print(out,end='')
