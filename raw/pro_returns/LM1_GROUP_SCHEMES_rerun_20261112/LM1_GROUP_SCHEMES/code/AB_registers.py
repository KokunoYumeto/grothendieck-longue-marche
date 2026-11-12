"""Generate the A/B statement, reading and task-coverage registries.

This is metadata assembly, not an additional mathematical calculation.
Run from any directory; paths are resolved relative to this file.
"""
from pathlib import Path
import json

BASE=Path(__file__).resolve().parents[1]
COLS=['id','statement','status','where_proved','depends_on',
      'manuscript_passages (section; folio; scan)',
      'depends_on_doubtful_reading (scan, alternatives)','notes']
ROWS=[]
def add(i,claim,status,deps,passages,reading,notes,section=None):
    ROWS.append(dict(zip(COLS,[i,claim,status,
        f'sections/{section or i[0]}.tex, statement {i} and its proof',
        deps,passages,reading,notes])))

add('A.1','The modular dictionary gives the stated centralizers, signed normalizer, solution schemes, ambient groups and final equal-determinant group.',
    'Proved','B.1; B.2; B.4; B.6',
    '48.II–XII; folios 433–543, with dual pagination; C3 scans264–273,323–330,368–419,473–480',
    'C3:264 cd|d; 266 B+D−C|C+D−B; 328 last matrix entry; 479 (13)–(14) coordinate order',
    'Definitions are fixed before the later proofs. Universal polynomial identities executed in AB_identities.py; no claim that every earlier overwritten notation is unchanged.')
add('A.2','Regular-unipotent lifts differ exactly by 1+tau with 2tau=tau²=0; uniqueness on all base changes holds exactly where 2 is invertible.',
    'Proved','None','48.VI–VII; folios462,480–481; C3 scans323,358–360',
    'C3:358–360 finite ambiguity mu2 prime versus mu2','The ambiguity is nonflat Spec Z[tau]/(2tau,tau²); Z/4 gives a smallest-cardinality counterexample, executed exactly.')
add('A.3','Specified regular-unipotent lifts and transverse lines give a unique inner pinning; the projective stabilizer is [I+tau r] with 2tau=tau²=0.',
    'Proved','A.2','48.VI–VII,XI; folios462,480–481,508; C3 scans323,358–360,413',
    'C3:323 qualification on the base; 358 uniqueness claim',
    'Proof covers the stated free-module bases and descends to vector-bundle/Azumaya algebra identifications; projective infinitesimal ambiguity checked over Z/4.')
add('A.4','Normalized modular triples form one GL2 orbit and SL2 orbits indexed by R×/(R×)² over Z, all fields, Z/4, Z/8 and Z/9.',
    'Proved','A.3','48.VI–VII; folios462–470,480–481; C3 scans323–339,358–360',
    'No further doubtful reading after normalization',
    'Full finite enumeration and orbit representatives retained; normalized lift conditions, including transversality, are explicit.')
add('A.5','Individual commutator maps are centralizer torsors onto the regular trace locus; integral special-linear images are exactly Y22>0.',
    'Proved','A.1','48.II–III,VIII; folios433–436,485–486; C3 scans264–273,368–370',
    'C3:264 c²+cd+d² versus c²+d+d²',
    'General point obstructions are Picard and determinant norm classes. Over Z Euclidean Gaussian/Eisenstein orders remove the former; all missed points are parametrized by Y22<0.')
add('A.6','The printed trace ordering, determinant-free transpose formula, and full signed centrality assertion are false; explicit corrected formulas hold.',
    'Refuted','A.1','48.II,VI,X–XII; folios434,464,501,511,542; C3 scans266,328,401,419,480',
    'C3:266 B+D−C; 328 −w(w²+2v)+v+w²; 480 omitted determinant',
    'All polynomial alternatives tested; b=2I refutes the missing determinant. The centrality claim was already withdrawn/corrected at scan419 and is identified as such.')
add('A.7','Projective modular-pair orbits in characteristic 2 are norm classes N(K×)/k×²; other fields and requested rings have the stated GL2/SL2 orbit classification.',
    'Proved','A.3; A.4; A.5','48.VI–VII; folios462–470,480; C3 scans323–339,358',
    'Projective hypotheses are explicitly distinguished from specified lifts',
    'An imperfect-field example over F2(t) is proved by a nonsquare derivative certificate; fppf normalization descent and finite projective orbits are checked.')
add('A.8','Unrestricted uniqueness among all GL2 group-scheme isomorphisms fails because theta(g)=det(g)^−1 g fixes SL2 pointwise.',
    'Refuted','A.3','48.VI–VII,XI; folios462,480,508; C3 scans323,358,413',
    'Scope of identification: algebra-induced inner maps versus arbitrary group isomorphisms',
    'Universal multiplicativity and involutivity checks executed; correct uniqueness is the inner/algebra-induced assertion A.3.')
add('A.9','General dictionaries and formal constructions are established in their typed categories; the remaining normalized and restricted-conjugator comparisons are source-indexed separately.',
    'Open','B.8; B.9; B.11; B.12; B.13; B.15; B.16; B.17; B.18; D.7',
    '49.II–VI; folios553–650 with dual pagination; C3 scans501–696',
    'C3:509 rho exponent; 510 alpha,beta versus zeta,eta; 511 second SZ_rho; 530–535 changed loop and sign conventions',
    'Proved formal constructions and finite tests; B.8.5 is only the automatic-automorphism question. B.15 treats quotient functoriality; B.16 and B.18 retain the distinct geometric-image, normalized-section, natural-subgroup and bisection assertions. B.17 corrects the antidiagonal domain. Integral realization and D.7 are further separate comparisons.')
add('B.1','The fixed modular solution space is Ga×Gm, and both unsigned and signed simultaneous parametrizations are isomorphisms over Z.',
    'Proved','A.1','48.II–III,VIII; folios435–436,485–486; C3 scans268–273,368–371',
    'C3:370 surjectivity question; 371 inclusion of the signed normalizer',
    'Explicit polynomial inverse; no missed points on any ring. Separate complete small-ring enumeration verifies the inverse, not only a dimension count.')
add('B.2','The final M has the displayed coordinate algebra, a monic integral Groebner basis, and is Z-flat of relative dimension 6.',
    'Proved','A.1; B.1; B.3','Earlier calculation and 48.IX–XII; folios365,497–501,542; C3 scans151,393,399,479',
    'C3:151 dimension3 changed to4; 393 4+3=7 and quotient dimension6',
    'Integral monic/product-criterion certificate and independent QQ,F2,F3 Groebner bases executed. Dimensions4,6,7,9,10 refer to distinct named schemes.')
add('B.3','M is smooth precisely over Z[1/2], with Jacobian ideal (4); its F3 fibre has four smooth components and its F2 fibre has one component of generic nilpotent length4.',
    'Proved','B.2','48.IX–XII and 51; folios497–501,542; C3 scans393,399–400,479; C4 scan41',
    'The final M and the separate scan41 fine parameter scheme are distinguished',
    'Unsigned M0 is smooth over all Z; the F2 reduction and the nilradical are explicit. E.24 treats the different scan41 scheme.')
add('B.4','The componentwise group law gives all displayed modular and ambient split/fppf exact sequences, with exact pointwise qualifications.',
    'Proved','A.1; B.1; B.2','48.IX–XII; folios487–511,539–542; C3 scans373–419,473–479',
    'C3:479 coordinate order and signs; 393 ambient groups',
    'Sections proved by matrix formulas; root adjunction proves remaining fppf surjections. Z and F3 give explicit failures of pointwise surjectivity.')
add('B.5','M(0),M[0], the full root-subgroup normalizer and the two three-element section cycles have the stated descriptions.',
    'Proved','B.4','48.XI–XII; folios508–511,541; C3 scans413–419,476–478',
    'C3:418 normalizer correction; 477–478 unchosen M(−j)',
    '(I,I,−I) is a strict-normalizer witness. The incomplete M(−j) choice is not declared canonical.')
add('B.6','The centres and central kernels are explicit; J0→H0 is a mu2 cover, and (J0×SL2)/mu2=M0.',
    'Proved','B.4','48.X–XI; folios501–502,511; C3 scans400–402,419',
    'C3:400 proposed unqualified J0 identification',
    'Fppf root descent proves the cover; F3 counts48 versus24 separate it from an isomorphism. Full signed centre computed functorially at2 as well.')
add('B.7','All requested M point counts and all individual commutator image complements over F2,F3,Z/4 are exactly those displayed.',
    'Proved','A.5; B.1; B.4','48.II–III,VIII–XII; folios433–436,485–486,501,542; C3 scans264–273,368–370,399,479',
    'Uses the corrected norm and trace equations',
    'Independent norm-count and matrix-enumeration methods agree. Counts for p≤13 and n=4,8,9, along with unsigned and determinant-one variants, are saved.')
add('B.8','General matrix equalizers are representable and signed universal data define continuous endomorphisms; automorphism realization B.8.5 and a suitable integral realization remain unresolved.',
    'Open','B.1; B.11; B.12; B.13; C.2; D.7','49.I–VI; folios553–587; C3 scans501–559',
    'Realization hypothesis (37) and scan503(10)(b) are retained',
    'Proved modular case, formal quotients, all signed finite models and PSL2F13 counterexample; exact remaining surjectivity B.8.5 is separate from D.7. A constant pro-group scheme cannot realize an infinite-order integral unipotent generator.')
add('B.9','A genuine global-sign quotient representation has a canonical profinite central pullback; quotienting by the group scheme mu2 has an additional infinite adelic kernel.',
    'Proved','None','48.XII;49.III; folios548,565–566; C3 scans492,524–526',
    'Global diagonal signs versus mu2(hatZ); placement of completion symbols at524–526',
    'The additional kernel is (product_p {±1})/diagonal{±1}. Identification with a named geometric extension requires its specified comparison map.')
add('B.10','Lead2 incorrectly identifies the final M with a preliminary pair scheme and its GL2 centralizers with norm-one groups.',
    'Refuted','A.1; B.1; B.2; B.3; B.4','48.II–XII; folios433–543; C3 scans264–480',
    'Normalization changes are explicitly distinguished',
    'Dimension4 precursor versus dimension6 final M and dimension2 versus dimension1 centralizers prove the correction.')
add('B.11','For general discrete/profinite C the unsigned construction and all displayed fibre-product exact sequences are valid; its pair parametrization is conditional on realization.',
    'Proved','None','49.II; folios554–560, parallel502–513; C3 scans503–514',
    'C3:509 rho^+1|rho^−1;510 inserted zeta,eta versus alpha,beta;511 second SZ_rho',
    'Kernel C→G is L0∩Z(C), not automatically trivial. Exact S3/S4 automorphism and count calculations attached.',section='B_general')
add('B.12','Automatic realization of generating pairs with separately conjugate entries satisfying a unit loop equation is false in PSL2(F13).',
    'Refuted','B.11','49.I–II; folios553–554; C3 scans501,503',
    'No reading dependence: directly satisfies the original numerical condition',
    'Complete matrices, conjugators, orders, generation and failed relation [sigma,rho]^7=1 are executed; the unit exponent is correctly lifted to hatZ×.',section='B_general')

READCOLS=['package','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly']
READ=[]
def read(p,s,q,a,e='Exact algebraic implication; mathematical evidence, not final palaeographic settlement'):
    READ.append(dict(zip(READCOLS,[p,s,q,a,e])))
read('LM_C3-150-168','151','Relative dimension3 with marginal correction4',
     'The special precursor has dimension4; the later final M has dimension6. Both are computed from independent explicit coordinate models.')
read('LM_C3-264-282','264',r'c²+\unsure{cd|d}+d²',
     'The determinant is c²+cd+d²; the alternative differs by cd−d in the universal ring.')
read('LM_C3-264-282','266','Trace condition B+D−C=1 versus C+D−B=1',
     'For the displayed r, tr(Yr)=C+D−B. Universal difference for the other order is 2(C−B). Ink and scan151 were visually checked; this is a formula correction.')
read('LM_C3-321-339','323','Qualification sans quelques restrictions sur S; tau with 2tau=0,tau²=0',
     'Exactly the ambiguity of unipotent lifts and the projective stabilizer; it disappears on all base changes precisely when 2 is invertible.')
read('LM_C3-321-339','327–330','General normalized v|nu and lower-right entry of rho² sigma at328',
     'With R=[[0,1],[v,w]], S=[[0,−1],[−v,1−w]], the entry is −w(w²+2v)+v+w². All other entries and powers are checked universally; glyph v versus nu is not decided.')
read('LM_C3-340-358 / LM_C3-359-377','358–360','Uniqueness and ambiguity mu2 prime',
     'The actual ambiguity is nonflat Spec Z[tau]/(2tau,tau²), not all mu2. The Z/4 example is of minimal ring cardinality.')
read('LM_C3-359-377','368–371','Surjectivity of (2), then signed (10)',
     'Both maps are scheme isomorphisms for the fixed modular matrices. Individual commutator maps instead require the regular locus and have norm obstructions on points.')
read('LM_C3-378-396','393','4+3=7, quotient dimension6; ambient10 and9',
     'All four dimensions are correct for their respective schemes. The overwritten precursor dimension is4; universal product/quotient coordinates prove the counts.')
read('LM_C3-397-415','399–400','(13)–(14) det f=det y=epsilon prime det x; identification J0≈H0',
     'The determinant chain defines final M. J0→H0 is instead a central mu2 cover; F3 has48 versus24 points.')
read('LM_C3-397-415 / LM_C3-416-434','401,418–419','ST_sigma centrality; M[0] asserted as normalizer',
     'ST_sigma is central in M0 but inverted by the full sign action; the normalizer of L0 has the whole upper triangular U-coordinate. Both qualifications are already corrected by the author at418–419.')
read('LM_C3-473-491','477–478','Labels M(−j), M(−bar j), M(1/2)',
     'M(−bar j)=M(r) is the partial section U=a and M(1/2)=M(s) is U=b. The extra M(−j) choice is not fixed by the text; no canonical choice is inferred.')
read('LM_C3-473-491','479–480','Final signs; sigma(b)=transpose inverse and bb^t=epsilon I',
     'The correct GL2 identities include det(b): sigma(b)=det(b)b^−t and bb^t=epsilon det(b)I. The displayed versions hold after det(b)=1, not on all N_sigma prime.')
read('LM_C3-492-510','509',r'alpha(rho)rho^{\unsure{+1|−1}}',
     'Exponent−1 is required by the commutator definition. Both alternatives are tested over the universal matrix coordinate ring.')
read('LM_C3-492-510','510','(38) inserted (zeta,eta) with zeta=ua^−1,eta=ub^−1',
     'These are alpha,beta; zeta,eta are their commutators. The formal inverse parametrization proves the types.')
read('LM_C3-511-529','511','(44) duplicated SZ_rho in the sigma line',
     'The second group is SZ_sigma=Cent_C(sigma), as forced by the kernel map and the later fibre-product exact sequences.')
read('LM_C3-492-510 / LM_C3-511-529','492,524–526','GL2(hatZ)/±1 versus (GL2/mu2)(hatZ); completion symbol placements',
     'Global ±1 and schematic mu2 give different adelic quotients. The extra scalar kernel is infinite; profinite completion and congruence completion remain separate.')

COVER=[]
def cov(task,outcome,ids,details):
    COVER.append(dict(task=task,outcome=outcome,statements=ids,details=details))
cov('item1','proved','A.2; A.3; A.5; A.7; B.1–B.7; E.24',
    'Explicit schemes, integral and finite-field Groebner bases, dimensions/flatness/smooth loci, exact lift ambiguity and all requested modular parametrization images; the different scan41 fine scheme is treated in E.24.')
cov('Lead2','refuted','B.1–B.4; B.10','Final scheme, precursor and norm-one factors are distinguished with explicit equations, inverse maps and dimension proofs.')
cov('A.a','partly settled','A.1; A.9; B.11; B.13; B.15–B.18',
    'Modular and formal dictionaries, quotient descent and finite models are established. B.16 and B.18 specify the remaining named geometric/normalized and restricted-conjugator comparisons at scans573–650 and651–690; these are distinct from B.8.5 and integral realization.')
cov('A.b','partly settled','A.1; A.6; A.9; B.11–B.18',
    'Universal matrix identities, used algebraic reading alternatives, quotient descent, central twists and restricted finite models are checked. The exact unverified global image/section and natural-comparison formulas are indexed in B.16/B.18; no exhaustive verification of them is claimed.')
cov('A.c','proved','A.2; A.3; A.8','Precise existence/uniqueness theorem for inner pinning, arbitrary-base descent, infinitesimal projective stabilizer, and counterexample to unrestricted group-isomorphism uniqueness.')
cov('A.d','proved','A.4; A.7','Complete normalized and projective classifications over every requested base, including imperfect fields; finite triples and GL2/SL2 projective orbits exhaustively enumerated.')
cov('B.a','proved','A.1; B.1; B.2; B.4','Full affine coordinate rings and functors of points, including both ambient groups and preliminary solution spaces.')
cov('B.b','proved','B.2; B.3; E.24','Integral monic Groebner certificate, QQ/F2/F3 computations, every fibre component and nilradical, smooth locus and unsigned/fine-parameter distinctions.')
cov('B.c','partly settled','A.3; B.4–B.6; B.8; B.11; B.13; B.15–B.18',
    'Modular and general formal exact sequences, quotient descent, central-twist kernel and corrected restricted antidiagonal are proved. The actual normalized sections and later natural-subgroup exact sequences are separately retained in B.16/B.18, with executed finite cases.')
cov('B.d','proved','A.2; A.3','Exact ring-of-sections criterion, universal base-change criterion and smallest-cardinality Z/4 counterexample proved and executed.')
cov('B.e','proved','A.5; B.1; B.7','Combined maps are isomorphisms over all rings; all missed individual points over finite requested rings listed; infinite integral complements specified exactly.')
cov('B.f','proved','B.4; B.7','All p≤13 and n=4,8,9 counts computed twice and compared with exact formulas; unsigned and determinant-one companion counts retained.')
cov('B.g','partly settled','A.9; B.8; B.9; B.11–B.18; D.7',
    'Unsigned/signed formal constructions, congruence descent, global-sign pullback and finite tests are proved. Automatic realization (B.8.5), named geometric/normalized comparisons (B.16), restricted-conjugator comparisons (B.18), integral realization and D.7 are explicitly distinct residuals.')

for name,data in [('AB_results.json',ROWS),('AB_readings.json',READ),('AB_coverage.json',COVER)]:
    (BASE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(ROWS)} A/B statement rows, {len(READ)} readings and {len(COVER)} coverage rows.')
