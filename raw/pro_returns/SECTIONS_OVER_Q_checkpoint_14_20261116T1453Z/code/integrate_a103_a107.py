#!/usr/bin/env python3
"""Integrate the five independently audited seventh-hour statements."""
from pathlib import Path
import datetime
import json

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
files=[
 ('A.103','norm_permitted_unit_obstruction.tex'),
 ('A.104','legendre_simultaneous_fibre.tex'),
 ('A.105','norm_deeper_root_refinement.tex'),
 ('A.106','norm_deeper_unit_obstruction.tex'),
 ('A.107','harmonic_tripod_bridge.tex'),
]
p=w/'SECTIONS_OVER_Q_paper.tex'
source=p.read_text()
anchor=r'\input{sections/legendre_bad_place_fibre.tex}'
assert anchor in source
for ident,name in files:
    entry='\\input{sections/'+name+'}'
    if entry not in source:
        source=source.replace(anchor,anchor+'\n'+entry)
    anchor=entry
p.write_text(source)

records={
 'A.103': {
  'answers':'A5; A9; L10; L20',
  'depends_on':'A.98; A.101; explicit tame cubic norm criterion and q=22441 certificate',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58,126–127; actual norm transition in the one-variable quotient',
  'notes':'The specified cubic-field representative has no next norm preimage for any rational Q and q-unit R, even though q satisfies B24 and prior-representative radical splitting. Its canonical2 divisor is preserved. The underlying rational pair retains its explicit compatible norm family.'
 },
 'A.104': {
  'answers':'A7; A15; L14; L15',
  'depends_on':'A.16; A.49; A.56; A.63; A.78; continuous connecting cocycles and exact integral centralizers',
  'uses_local_theorem':'no; full local types are tested directly in the specified quotient',
  'manuscript_passages':'cote149; scans48,54–58; relative-sign comparison in the actual congruence-plus-abelian extension',
  'notes':'Exactly four geometric section classes have both projection classes equal to a rational point. Restriction to Q3 is a bijection on these fibres, and only the zero class is locally point/cusp. At good3 the order8192 quotient excludes every point/cusp source for the other three classes. At bad3 an explicit order2^(3N−2) quotient distinguishes the four classes, N=5+v2(−v3(j)/2). This classifies the simultaneous two-projection fibre, with no classification of the H-only fibre.'
 },
 'A.105': {
  'answers':'A5; A9; L10; L20',
  'depends_on':'A.95; A.100; A.101; Kedlaya4.3.7 equation4.3.1 and Galois norm limitation',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58,126–127; stronger permitted prime conditions for the norm tower',
  'notes':'For ray moduli excluding2 and3, proves the exact intersections with deeper pure roots and all prior representative/boundary radicals, together with the full simultaneous arithmetic abelianization and CRT compatibility. The local relative cubic norm at the coefficient-place3 is onto. Individual post-repair unit equations remain.'
 },
 'A.106': {
  'answers':'A5; A9; L10; L20',
  'depends_on':'A.103 tame norm formula; explicit norm-one incidence map in the degree54 splitting field; exact polynomial certificate',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58,126–127; exact failure of an allocated-prime norm transition',
  'notes':'Explicit degree9 representatives, defined by unique integer interpolation polynomials, retain norm−2 and the canonical2 divisor. At q=321193 all deeper L3, B72 and prior conjugate radical conditions hold. For the post-repair representative, all nine local norm equations hold exactly when Q is a local cube, for every rational R and every e prime3. Thus allocating q at exact depth2 fails for this representative. Exact norm-fibre map included; no obstruction to the underlying rational pair is claimed.'
 },
 'A.107': {
  'answers':'A12; A14; A15; L12; L14',
  'depends_on':'A.76; A.93; A.97; SGA1 finite etale cover comparison and the actual harmonic morphism',
  'uses_local_theorem':'no; works with the stated Selmer fibres',
  'manuscript_passages':'cote149; scans54–58; prompt harmonic map t=4T(1−T)',
  'notes':'Proves the exact degree2 cover, completed Kummer/deck maps, bijection of full Selmer fibres with real condition retained, and an actual finite tripod quotient of order2^136 receiving the old rank3 quotient. Third-derived and lower-central quotient maps are explicit. No obstructed harmonic arithmetic tuple has been found.'
 }
}
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta.update(records)
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
lines=report.splitlines()
additions={
 'A5':('A.103, A.105, A.106','The actual norm transition now has two explicit representative obstructions; stronger permitted-prime splitting is proved, while the coupled unit repair remains open.'),
 'A7':('A.104','The simultaneous full-H and full-Kummer projection fibre over any point has exactly four classes, and three fail locally at3; the full H-only recognition scope remains open.'),
 'A9':('A.103, A.105, A.106','The deeper-root/ray-field intersections and both explicit representative obstructions locate the remaining norm-unit repair in an actual transition map.'),
 'A12':('A.107','The harmonic degree2 map has an exact Selmer-fibre bijection and finite quotient comparison; an obstructed harmonic tuple remains unconstructed.'),
 'A14':('A.107','The harmonic map is treated on its actual four-punctured source, with one global deck ambiguity and the exact full Selmer-fibre map.'),
 'A15':('A.104, A.107','The four relative-sign classes in the specified simultaneous projection fibre are classified and detected at3, and the harmonic finite-quotient comparison is explicit. The general countersign and derived-limit questions remain open.'),
 'L10':('A.103, A.105, A.106','The norm-tower comparison includes stronger split-prime control and fully specified failures for individual transition representatives.'),
 'L12':('A.107','The harmonic cover comparison retains the full profinite groups and real Selmer condition.'),
 'L14':('A.104, A.107','Exact relative-sign and harmonic-cover comparisons are proved in the named quotients.'),
 'L15':('A.104','The simultaneous H-plus-Kummer fibre is now classified; this result retains its exact quotient and does not settle the H-only fibre.'),
 'L20':('A.103, A.105, A.106','The actual norm transition and its auxiliary-prime unit constraints are explicit; a coherent infinite preimage is still unresolved.'),
}
for i,line in enumerate(lines[:55]):
    for item,(ids,detail) in additions.items():
        if line.startswith('| '+item+' |'):
            parts=line.split(' | ')
            if ids not in parts[1]: parts[1]+=', '+ids
            line=' | '.join(parts)
            if detail not in line: line=line[:-2]+' '+detail+' |'
            lines[i]=line
report='\n'.join(lines)+'\n'
heading='## Exact relative signs and stronger norm-prime tests'
if heading not in report:
    report+='\n'+heading+'\n\n'+stamp+': A.103–A.107 are integrated after full independent audits. A.104 identifies exactly four global and four Q3-local geometric section classes in the simultaneous full-congruence/full-abelian projection fibre of every rational point. The connecting map from the four invariant relative signs is injective, and the actual centralizer image is zero at3. Only the zero class has a local point or cusp source. For good reduction at3, the finite geometric quotient has order8192 and excludes every such source for the other classes; an explicit depth-dependent finite quotient distinguishes the four classes at bad3 as well. All j=1728 parameters are included.\n\nA.105 proves that deeper A-root splitting can coexist with the full boundary, prior-representative radical, and ideal-class generation conditions, with the ray modulus away2 and3. It also proves surjectivity of the local relative cubic norm at3. A.103 and A.106 show why representative-unit control still matters: at22441 a specified cubic-field representative fails every permitted next norm map, while at321193 a fully specified degree9 post-repair representative forces every successful update Q to be a local cube, even after every deeper splitting condition holds. Both examples retain the canonical two-adic divisor and give their actual completed norm-fibre maps. The rational pair(3,−2) retains its explicit compatible family.\n\nA.107 proves the exact harmonic degree2 comparison between full Selmer fibres, including its unique global deck choice after fixing the old coordinates and the real condition. Its finite tripod quotient has order2^136 and is an actual arithmetic quotient. The necessary harmonic arithmetic obstruction has not been constructed; the unsuccessful searches and intermediate-cover calculations remain documented as research in progress. Both principal assertions A1 remain open.\n'
p.write_text(report)

audit=stamp+' root audits A103–A107: A103 full tame norm and exact coefficient map passed; A104 exact continuous cocycle kernel, integral centralizer at3, full finite good3 disc/trace exclusion and finite bad3 Tate centralizers passed; A105 local total ramification, both field intersections, literal combined group and Galois norm-index argument passed; A106 all polynomial and embedding formulas, actual norm identities, arbitrary R valuation and complete local cube criterion passed, independently audited by birational_main; A107 Selmer-fibre lifting/deck proof, real transfer, characteristic subgroup and exact finite quotient maps passed, with independent birational audit. Local_preprint independently passed A103,A104,A105 and authored A107. All cited finite certificates were executed and their outputs retained.\n'
for name in ['notes/hour7_root_audits.md','notes/root_progress.md']:
    with (w/name).open('a') as f: f.write('\n'+audit)

sources='\n'+stamp+' seventh-hour source checks: root opened Kedlaya, Notes on class field theory, Theorem4.1.7 at https://kskedlaya.org/cft/sec_localrecip.html and Remark4.3.7/equation4.3.1 plus Remark4.3.8 at https://kskedlaya.org/cft/sec_tatethm.html. A105 uses the Galois norm-index identity and an explicit scalar-cube argument for its S3 closure. The non-Galois reduction sentence claiming preservation of the maximal abelian subfield under Galois closure is not used: the actual cubic field here has no abelian intermediate field, whereas its S3 closure has the quadratic cyclotomic subfield. The theorem itself is not refuted by this observation. Searches with both engines covered Legendre monodromy abelianization/congruence-kernel section signs, and pure-radical tower/ray-class/norm-coherence compatibility. No theorem resolving the infinite norm compatibility was imported; no novelty or priority claim is made.\n'
with (w/'notes/root_source_continuation.md').open('a') as f:f.write(sources)

output='Integrated A103–A107 with exact scopes and independent audits; both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a103_a107_output.txt').write_text(output)
print(output,end='')
