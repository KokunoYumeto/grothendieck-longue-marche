#!/usr/bin/env python3
"""Build a research catalog from frozen text; never modifies transcription."""
from pathlib import Path
from collections import Counter
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / 'context'
OUT = ROOT / 'research'
OUT.mkdir(exist_ok=True)
ITEMS = []
HUA_Q = 'Hua, findings register, 84-product-quadratic-algebras-formula'
HUA_E = 'Hua, findings register, 84-chi-trivialised-extension-product'
RS_SAME = 'MPL_84_146-193 §2'

def add(ident, scans, title, parameters, entries, counts, status, recipe, refs, relation, queries, *, family='math', rs=None, anchors=None, check='literal'):
    ITEMS.append(dict(id=ident, scans=scans, title=title, parameters=parameters,
        entries=entries, counts=counts, status=status, recomputation_recipe=recipe,
        context_references=refs, context_relation=relation, context_queries=queries,
        layer=family, results_state_ids=rs or [], source_anchors=anchors or [], check=check))

add('EN097.1',[97], 'Three-row verification array for the restriction of g',
    'u in L; x in E; psi(u)=0',
    [r'g(x)(u)=psi(x)u',r'psi(x)u-psi(u)x'],
    'Listed: 2 expression rows and 1 equality-mark row; array shape 3×1. No finite set of x or u is counted.',
    'Live verification; the nearby sign warnings remain manuscript warnings.',
    'Substitute psi(u)=0; count the three source array rows without treating the equality sign as an object.',
    ['§9.2 T180b/T184c (scans180,184); R04 (scan160)'],
    'Earlier notes register boundary pairings, but not this restriction array; this is preceding sign-sensitive evidence for the same duality problem.',
    ['boundary pairing','sign','duality','psi'],rs=[HUA_E],anchors=[r'g(x)(u)=',r'\begin{array}{c}'])
add('EN098.1',[98], 'Extension/algebra splitting comparison and the two quadratic forms',
    'E=L⊕O x0; A⊗L=L⊕O; b in L and c in L^2',
    ['E: L and O x0','A⊗L: L and O','Q(u+lambda x0)=u²+lambda<u,b>+lambda²c','N(v+lambda1)=lambda²-lambda<v,b>+<v²,c> (signs doubtful in source)'],
    'Listed: 2 decomposition rows with 2 summands each; 2 corresponding form formulas. Counts are layout counts, not authorial cardinality claims.',
    'Live; source marks the norm signs and several letters uncertain.',
    'Read the 2×2 summand correspondence; substitute u=-v under the stated sign convention only after the relevant pairing is fixed.',
    ['§9.2 T176b/T190b (scans176,190); R08 (scans160,192)'],
    'Adds the earlier explicit Q/N comparison to later reported dual-basis tables; those tables do not settle its uncertain signs.',
    ['dual-basis','binary quadratic','pairing','norm'],rs=[HUA_Q,HUA_E],anchors=[r'\underline E={}',r'Q(',r'N('])
add('EN099.1',[99], 'Two composites in the cancelled construction of i',
    'i:E→E1⊗E2; product * and injection inj',
    ['alpha=i∘*','beta=i∘inj','alpha∘inc=2 beta'],
    'Author says “les deux composés”: 2 composites; 1 compatibility relation.',
    'Entire proposal is cancelled; not two additional live axioms.',
    'Enumerate the two named composites and retain the one relation as a constraint, not a third composite.',
    ['E166.1–E166.3 / §9.1 T166.1–T166.2 (scan166)'],
    'The earlier notes later describe four comparison blocks and two nonautomatic squares; this is a cancelled precursor, not the same four-block count.',
    ['composites','comparison','F_{11}','two squares'],rs=[HUA_E],anchors=['les deux composés'])
add('EN099.2',[99], 'Cancelled two-row kernel label and paired involutions',
    'Two input extensions; sigma1, sigma2 and their tensor product',
    [r'L1⊗E2 ⊕ E1⊗L2',r'E1*_0E2','sigma1','sigma2'],
    'Listed: inner array 2×1; 2 input involutions and 1 indicated tensor involution.',
    'Cancelled diagram and prose; projection and kernel notation remain doubtful.',
    'Count both array labels and both factor involutions; do not assert an isomorphism between doubtful labels from their juxtaposition.',
    ['§9.1 T160.2 (scan160); §9.2 T186a (scan186)'],
    'Precedes later mixed-factor and symmetrizer computations; the cancelled status distinguishes it from the later reported formulas.',
    ['mixed tensor','symmetrization','involution'],rs=[HUA_E],anchors=[r'\begin{array}{c}L_1', 'inv. canoniques'])
add('EN100.1',[100], 'Two-level tensor/product correspondence',
    'Two chi-trivialized torsors; Li invertible; L=L1⊗L2',
    ['E1⊗E2 → E1 * E2 (product sign uncertain)','(A1⊗L1)⊗(A2⊗L2) and A⊗L'],
    'Listed: 2 comparison rows, each with tensor-side and product-side entries; 2 input torsors explicitly named.',
    'Live comparison; no claim of a finite classification.',
    'Count the two rows and two inputs; the transpose maps are structural maps, not extra members of a counted set.',
    ['§9.2 T184a/T184b (scan184); §9.1 T160.1 (scan160)'],
    'Restates the tensor-versus-product distinction that the earlier notes later record for dual presentations.',
    ['product algebra','product module','dual sequence','two input'],rs=[HUA_E],anchors=['deux torseurs',r'E_1\otimes E_2 \arrow'])
add('EN101.1',[101], 'Two trace restrictions and two universal-property maps',
    'A1 amalgamated with A2 over O; A1⊗A2; target A1⊗A2',
    ['Tr_A1 on first component','Tr_A2 on second component','O→A1⊗A2','A1⊗A2→A1⊗A2'],
    'Authorial “deux composantes”; 2 trace restrictions. The separate map specification has 2 maps with 1 agreement condition.',
    'Live construction; one arrow direction and the amalgam symbol are uncertain.',
    'Check agreement of the two maps on the amalgamated kernel; enumerate maps separately from their common compatibility condition.',
    ['§9.2 T188c (scan188); L172.1 (scan172)'],
    'Adds an earlier universal-property formulation to the later notes’ two trace restrictions.',
    ['trace restrictions','universal property','amalgamated'],rs=[HUA_Q,HUA_E],anchors=['deux composantes','séparément'])
add('EN102.1',[102,105], 'Paired conjugation formulas on the quadratic factors',
    'i=1,2; xi in Ai; units ei; the source has different written unit conventions',
    ['x1↦Tr1(x1)-x1','x2↦Tr2(x2)e2-x2','bar(x1⊗x2)=bar x1⊗bar x2'],
    'Listed: 2 factor formulas and 1 induced tensor rule; scan105 repeats the 2 factor formulas.',
    'Live corrected formulas; cancelled predecessors remain in scan102.',
    'In monic coordinates substitute Ui↦-bi-Ui and form the tensor conjugation; retain the source’s unit typography.',
    ['§9.2 T186a/T192a (scans186,192); L172.1'],
    'Provides the general conjugation input for the later notes’ specialized four-image table.',
    ['conjugation','symmetrization','quadratic equations'],rs=[HUA_Q],anchors=['sur $\\mathcal A_1','les involutions canoniques'],check='quadratic_basis')
add('EN103.1',[103,104], 'Four-element tensor basis: trace and norm values',
    'Ai=O[Ui]/(Ui²+biUi+ci); ordered basis (1,U1,U2,U1U2)',
    ['trace: (2,-b1,-b2,U+b1b2)','norm: (1,c1,c2,c1c2)','i(U)=2U1U2+b1U2+b2U1'],
    'Listed basis size 4; 4 trace images across the prose/formulas and 4 norm values. No claim that the tensor realization is always injective.',
    'Trace values are given; norm construction is introduced as a desired universal construction. Some surrounding prose/signs are doubtful.',
    'Reduce products in the monic rank-four tensor algebra; compute z+bar z and z bar z on the four basis vectors.',
    ['§9.2 T186a (scan186), T192a/T192e (scan192); L172.1–L172.3'],
    'Adds the general b1,b2 basis table to the later notes’ b1=b2=0 specialization; the tensor-realization warning agrees in scope.',
    ['ordered basis','four image','b1=b2=0','monic'],rs=[HUA_Q,RS_SAME],anchors=['base $1,U_1,U_2','N(1)=','images de $1'],check='quadratic_basis')
add('EN103.2',[103], 'Five-row norm comparison array',
    'Pure tensor x1⊗x2 and conjugations on the two factors',
    ['N_A(x1⊗x2)=N1(x1)N(x2)','(x1⊗x2)(bar x1⊗bar x2)','(x1 bar x1)⊗(x2 bar x2)'],
    'Array shape 5×1: 3 expression rows and 2 equality-mark rows. The literal second factor is N(x2), not silently N2(x2).',
    'Introduced by “On devrait avoir”; proposed comparison, not a completed existence proof.',
    'Count rows; check the pure-tensor norm identity in the declared monic model, explicitly separating that model from the literal subscript.',
    ['L172.1; §9.2 T186b (scan186)'],
    'Related later norm computations do not erase this page’s desideratum or its written notation.',
    ['norm','pure tensor','quadratic products'],rs=[HUA_Q],anchors=[r'N_{\mathcal A}(x_1'],check='quadratic_basis')
add('EN104.1',[104], 'Two quadratic input presentations and their product presentation',
    'b1,b2,c1,c2 over O; bases (1,U1),(1,U2)',
    ['A1=O[U1]/(U1²+b1U1+c1)','A2=O[U2]/(U2²+b2U2+c2)','A1⊗A2 with both relations','A=O[U]/(U²+bU+c)'],
    '2 input bases of 2 elements; 2 input relations; tensor basis rank 4 and product basis rank 2 are derived from the monic presentations.',
    'Live local presentations. The rank-four algebra here is commutative, not a central rank-four Azumaya algebra.',
    'Enumerate the tensor basis by the Cartesian product of the two basis lists; reduce using the two monic relations.',
    ['§9.2 T192a/T192b/T192e; R02 (scans172,192)'],
    'Restates the local presentations appearing later and reinforces the earlier notes’ distinction from B12’s Azumaya algebra.',
    ['quadratic equations','rank four','commutative','Azumaya'],rs=[HUA_Q,RS_SAME],anchors=['Choisissons les bases'],check='quadratic_basis')
add('EN104.2',[104], 'Two product-coefficient formulas',
    'Four scalar parameters b1,b2,c1,c2; output b,c',
    ['b=b1b2','c=b1²c2+b2²c1-4c1c2'],
    'Listed: 2 output coefficients from 4 input coefficients.',
    'Live explicit local formula.',
    'Substitute U=2U1U2+b1U2+b2U1 and reduce U²+bU+c by the two input relations.',
    ['L172.1; §9.2 T172a; R05 (scans172,192)'],
    'Same local formula as the earlier notes’ checked claim; this package supplies an earlier occurrence, not a new theorem.',
    ['b=b₁b₂','c=b₁²c₂','product coefficients'],rs=[HUA_Q,RS_SAME],anchors=['b&=b_1b_2'],check='quadratic_basis')
add('EN105.1',[105,106], 'Two-part proposition with a two-condition norm characterization',
    'Two quadratic O-algebras and their product A',
    ['1) canonical relative trace','2) unique quadratic relative norm','2a) norm on pure tensors','2b) polar form = relative trace of xi bar eta'],
    'Numbered proposition: 2 main parts; norm part: 2 labelled conditions a,b. These are 2+2 hierarchical slots, not 4 independent axioms.',
    'Authorial proposition and characterization; verification continues on106–107.',
    'Parse labels 1),2),a),b); the monic model checks the four basis values and polarization, not arbitrary-base existence by counting alone.',
    ['L172.1; §9.2 T188c and T192a'],
    'Adds an explicit trace/norm characterization to the later local product account; no matching proposition list occurs in the earlier notes.',
    ['relative trace','norm','quadratic-algebra product'],rs=[HUA_Q],anchors=['1)','2)','text{a)}','text{b)}'])
add('EN106.1',[106,107], 'Four conjugates and two complementary norm pairs',
    'xi0=xi, xii=sigmai(xi), sigma3=sigma1 sigma2',
    ['xi0','xi1','xi2','xi3','pairing {0,3} and {1,2}'],
    'Listed: 4 indexed conjugates; grouping marks select 2 pairs. Product has 4 factors.',
    'Norm-transitivity calculation; source writes xi in A and an equality is emphatically marked on107.',
    'Use four formal commuting variables; verify (x0x3)(x1x2)=x0x1x2x3 and the induced conjugate pairing.',
    ['§9.2 T186a (scan186); R02'],
    'No matching four-conjugate action table was found in the earlier notes; related four-dimensional basis computations concern a different enumeration.',
    ['four conjugates','sigma_3','four image','norm'],rs=[HUA_Q],anchors=['xi=\\xi_0','N_{A_1\\otimes A_2/O}(\\xi)='],check='four_conjugates')
add('EN106.2',[106], 'Two invariance rows and two transitivity identities',
    'Relative N,Tr for A1⊗A2/A/O; sigma1,sigma2,sigma3',
    ['N(sigma1 xi)=N(sigma2 xi)=bar N(xi)','N(bar xi)=N(xi)','N_A/O(N_relative xi)=N_tensor/O(xi)','Tr_A/O(Tr_relative xi)=Tr_tensor/O(xi)'],
    '2 displayed invariance rows; 2 separately displayed composition identities.',
    'Live claims; one identity-map index is explicitly doubtful.',
    'Check invariance and norm pairing in the four-conjugate model; do not identify a doubtful A1/A2 subscript from the count.',
    ['L172.1; §9.2 T190a'],
    'Extends the earlier notes’ local coefficient/trace-norm calculations by stating these structural identities explicitly.',
    ['trace and norm','norm','involution'],rs=[HUA_Q],anchors=['N(\\sigma_1','N_{A/O}','Tr}_{A/O}'],check='four_conjugates')
add('EN107.1',[107], 'Two-row trace/norm data table',
    'A arbitrary k-algebra; alpha:k→A need not be injective; no flatness assumption',
    ['t_A/k=t:A→k, trace relative','n_A/k=n:A→k, norme relative'],
    '2 written rows, each with map and name; array declares 3 columns but uses 2 populated columns.',
    'Definition-stage data; neither finite rank nor injectivity assumed.',
    'Count the two map rows; do not infer rank2 from the names.',
    ['R02; E148.4 (scan148)'],
    'Adds a deliberately weaker axiomatic setting than the later notes’ genuine rank-two local algebras.',
    ['trace-like','trace scalar','quadratic algebra'],rs=[HUA_Q],anchors=['trace relative','norme relative'])
add('EN107.2',[107,108,109], 'Draft quasi-quadratic axioms and nested numbered conditions',
    'alpha,t,n,sigma on A/k; optional tower k0→k→A',
    ['a) t linear, n quadratic, t(x)=phi_n(x,1)','b) n(1)=1 and n multiplicative','c|b) sigma=tau-id and nested conditions','1° sigma multiplicative','2° alpha n(x)=x bar x','cancelled 3° n(bar x)=n(x), then derived','3° polarization/additivity without alpha injective','4° optional trace and norm transitivity'],
    '3 draft lettered slots (third label doubtful); 4 live nested numbered slots1–4; 1 struck earlier “3°” label. Optional4 contains 2 identities.',
    'Draft hierarchy, including cancellation; replaced by the organized recap on110.',
    'Count labels by status and level, not all displayed identities as independent axioms.',
    ['E148.4 (scan148); §9.2 T190a'],
    'No equivalent numbered quasi-quadratic axiom system is in the earlier notes; it adds the missing general framework rather than a new finite algebra count.',
    ['quasi-quadratique','quasi-quadratic','trace-like','axiom'],rs=[HUA_Q],anchors=[r'\textcircled{a}',r'\textcircled{b}',r'3^\circ',r'4^\circ'])
add('EN109.1',[109,110], 'Optional two-row compatibility with the base ring',
    'rank(k/k0)=n, rank(A/k0)=2n; k→A not assumed injective',
    ['Tr_k/k0(t(x))=Tr_A/k0(x)','N_k/k0(n(x))=N_A/k0(x)'],
    '2 formulas; parameters n and 2n are ranks, not numbers of solutions.',
    'Explicitly facultative; repeated as item6 of the recap.',
    'Count the linear identity and degree2n-form identity separately; only evaluate under an actual finite locally free model.',
    ['L172.1; R02'],
    'Earlier notes provide local norm computations but no matching optional two-row axiom.',
    ['locally free','trace','norm'],rs=[HUA_Q],anchors=['formule facultative','Tr}_{k/k_0}'])
add('EN110.1',[110], 'Six-item recap defining quasi-quadratic algebras',
    'A/k; alpha,t,n; optional k0 and rank parameter n',
    ['1 t linear, t(1)=2','2 conjugation is algebra automorphism','3 quadratic homogeneity and additivity','4 n(1)=1','5 alpha n(x)=x bar x','6 optional trace/norm tower compatibility'],
    '6 numbered items; author defines the structure using1–5 (5 mandatory), with1 optional item; items3 and6 each contain2 formulas.',
    'Live recap; qualifications about injectivity and redundancy remain in margins.',
    'Enumerate labels1…6 and distinguish the mandatory subset1…5 from optional6.',
    ['E148.4 (scan148); R02'],
    'No matching six-item system was located in the earlier notes; the recap supplies context for their later trace-like operators.',
    ['quasi-quadratique','quasi-quadratic','trace-like','1°'],rs=[HUA_Q],anchors=['Récapitulons','satisfaisant $1^'])
add('EN111.1',[111], 'Four labelled input-data groups',
    'Base k; A1,A2,A3,A; index i=1,2,3',
    ['a base ring k','b four k-algebras A1,A2,A3,A','c quasi-quadratic structures on each Ai/k','d maps alpha_i:Ai→A and quasi-quadratic structures A/Ai'],
    '4 lettered data groups; 3 factor algebras plus1 ambient algebra; 3 alpha maps; 3 pairs(t_i,n_i) and3 pairs(T_i,N_i).',
    'Live; noninjectivity allowed.',
    'Enumerate the three indices; count 6 map pairs (12 maps) across the two levels, not twelve independent algebras.',
    ['R02 (scans172,192); §9.2 T172c'],
    'Adds a three-factor biquadratic setup to the earlier notes’ two-factor product calculations; no matching a–d list there.',
    ['biquadratic','biquadratique','three','two input'],rs=[HUA_Q],anchors=['Données','a) anneau','d) Des Hom'])
add('EN111.2',[111], 'Cancelled two-target trace/norm diagram, followed by the three-target diagram',
    'A→Ai; target labels include a cancelled A3 replaced by doubtful A2',
    ['cancelled draft: targets A1 and corrected A2, map pairs(T1,N1),(T2,N2)','live diagram: targets A1,A2,A3 with(Ti,Ni)'],
    'Cancelled diagram: 2 target slots and4 map arrows; live diagram: 3 target slots and6 arrows.',
    'One cancelled draft and one live replacement; target correction is not a fourth live algebra.',
    'Count arrows within each diagram separately and preserve deletion status.',
    ['§9.2 T188a (scan188)'],
    'Earlier notes also distinguish trial from live data, but their three-to-two reduction is a different object; no direct counterpart was found.',
    ['trial','cancelled','three','biquadratic'],rs=[HUA_Q],anchors=[r'\deleted{\diagram',r'"T_3"'])
add('EN111.3',[111,114], 'Three pair-product relations for commuting involutions',
    'sigma1,sigma2,sigma3; each squares to identity',
    ['sigma1 sigma2=sigma3','sigma2 sigma3=sigma1 (scan111 second index doubtful)','sigma3 sigma1=sigma2','sigma1 sigma2 sigma3=1'],
    '3 displayed pair-product relations and1 triple-product relation; a 4-element Klein group is a derived model, not a written four-element list here.',
    'Cancelled on111; live formulation and argument on114.',
    'Enumerate the four even-parity vectors in F2^3 and verify the three products.',
    ['R02/R09 (scans172,192)'],
    'No matching V4 relation list was located in the earlier notes or a relevant settled RS row; shared involution vocabulary does not link it to GT involution problems.',
    ['sigma_1','biquadratic','Klein','F_2'],rs=[HUA_Q],anchors=['sigma_1\\sigma_2','sigma_1\\sigma_2\\sigma_3'],check='binary_group')
add('EN112.1',[112], 'Six ordered-pair base-change diagrams',
    'Ordered distinct indices i,j in{1,2,3}',
    ['(1,2)','(1,3)','(2,1)','(2,3)','(3,1)','(3,2)'],
    'Author explicitly says6 diagrams; only the(1,2) representative is drawn. The full ordered-pair list is editorial expansion of3×2=6.',
    'Six cases claimed as a pattern; not six individually drawn diagrams.',
    'Enumerate permutations(range(1,4),2), keeping order.',
    ['R02; §9.2 T172c'],
    'No same six-case enumeration in the earlier notes; this adds the three-subalgebra compatibility pattern.',
    ['six','6 diagrammes','biquadratic','base change'],rs=[HUA_Q],anchors=['6 diagrammes'],check='ordered_pairs')
add('EN112.2',[112,113,114], 'Trace and norm compatibility conditions for each ordered pair',
    'i≠j; Ti,Ni and ti,ni; alpha_i',
    ['1° Tj(alpha_i(a))=ti(a)','2° Nj(alpha_i(a))=ni(a)'],
    '2 numbered compatibility types; expanding over the6 ordered pairs gives12 formal instances (derived). Scan114 says the norm condition implies the trace condition.',
    'Conditions, with a subsequent dependence claim; 12 is not a count of independent axioms.',
    'Cross the six ordered pairs with{trace,norm}; preserve the claimed implication as a qualification.',
    ['§9.2 T188c; E148.4'],
    'Extends later two-factor trace restrictions to six ordered base-change cases; the earlier notes do not contain this enumeration.',
    ['trace restrictions','base change','norm'],rs=[HUA_Q],anchors=['textcircled{1°}','textcircled{2°}','implique celle sur $T_2$'],check='ordered_pairs')
add('EN113.1',[113], 'Two-row comparison identities in the polarization check',
    'x′=alpha1(x), y′=alpha1(y); T2 and sigma2',
    ['alpha1(bar y)=sigma2(alpha1(y))','t1(x bar y)=T2(alpha1(x bar y))','phi_n(x,y)=T2(x′sigma2(y′))','ditto phi_N2(x′,y′)'],
    '2 rows in the braced intermediate comparison;2 rows in the concluding aligned comparison.',
    'Written proof check ends O.K.; n/n1 and some symbols remain reading doubts.',
    'Count both two-row comparisons; verify only after fixing the domains and the doubtful notation.',
    ['§9.2 T180b/T182a (scans180,182)'],
    'Related boundary-pairing comparisons occur later, but not this exact polarization array.',
    ['polar','pairing','boundary'],rs=[HUA_Q],anchors=['alpha_1(\\bar y)','varphi_{\\unsure'])
add('EN114.1',[114], 'Three cyclic trace expressions and their common composite',
    'T1,T2,T3 and t1,t2,t3',
    ['2x=T1x+T2x+T3x-t2T2x','same with-t3T3x','same with-t1T1x','t1Tr1(x)=t2Tr2(x)=t3Tr3(x)'],
    '3 cyclic forms;3 composites in the common-value equality. The manuscript writes Tr_i in the latter line.',
    'Equality of base scalars is qualified when k→A is not injective and then separately assumed.',
    'Use Ti(x0)=x0+xi and total trace=sum xj to verify the displayed formal pattern, without cancelling a noninjective base map.',
    ['E148.4; R02'],
    'Adds the three-way trace system; no direct counterpart in the earlier notes.',
    ['trace scalar','biquadratic','injective'],rs=[HUA_Q],anchors=['t_1\\operatorname{Tr}_1','2x=T_1'],check='four_conjugates')
add('EN115.1',[115], 'Four conjugates and the three-row involution pairing table',
    'x0=x and xi=Ti|sigmai(x); indices0,1,2,3',
    ['sigma1: x0↔x1; x2↔x3','sigma2: x0↔x2; x1→|↔x3','sigma3: x0↔x3; x1←x2'],
    '3 rows×2 pair cells=6 pairs;4 distinct x labels,12 pair incidences. Including row labels, the array is3×3.',
    'Literal arrow directions and Ti|sigmai readings remain uncertain/asymmetric; the abstract involution completion is editorial.',
    'Enumerate double transpositions(01)(23),(02)(13),(03)(12); verify they give all3 perfect matchings of4 labels and all6 unordered pairs once.',
    ['R02/R09'],
    'No matching permutation table occurs in the earlier notes; their rank-four tensor algebra is related but does not supply missing arrowheads here.',
    ['four','sigma_3','biquadratic','Klein'],rs=[HUA_Q],anchors=['On a alors',r'\begin{array}{c@'],check='four_conjugates')
add('EN115.2',[115], 'Three relative norms and three equal base norms',
    'Ni(x)=x0xi in the four-conjugate model; i=1,2,3',
    ['N1(x)=x0x1','N2(x)=x0x2','N3(x)=x0x3','ni(Ni(x))=x0x1x2x3 for each i'],
    '3 relative factors and3 base-norm composites; the total norm is a4-factor product.',
    'Initial expectation is cancelled; the following verification is live and equality in k is qualified by injectivity.',
    'Multiply the three pairs to get x0² times the fourfold product; use complementary pairs for each base norm.',
    ['L172.1; §9.2 T186b'],
    'No same three-norm enumeration in the earlier notes; this adds a structural norm relation rather than another local coefficient table.',
    ['norm','injective','biquadratic'],rs=[HUA_Q],anchors=['N_1(x)N_2(x)N_3(x)','n_2(N_2'],check='four_conjugates')
add('EN116.1',[116,117], 'Even-parity subgroup of F2^3 and its three nonzero elements',
    'Binary triples; parity map sum:F2^3→F2',
    ['(0,1,1)','(1,0,1)','(1,1,0)','(0,0,1) is explicitly deleted'],
    'Author says3 nonzero elements; identity(0,0,0) is implicit. Derived: ambient8, even subgroup4;1 deleted odd triple is not a live member.',
    'Live group enumeration with one rejected candidate; group-letter gamma/Gamma remains a reading doubt.',
    'Generate all8 binary triples, retain even parity, and remove the identity to recover the3 live entries.',
    ['R02/R09'],
    'No same F2^3 kernel enumeration was located in earlier notes; no connection to the unrelated GT/CM parity register follows.',
    ['F_2^3','even','parity','biquadratic'],rs=[HUA_Q],anchors=['trois éléments non nuls'],check='binary_group')
add('EN116.2',[116,117], 'Three tensor involutions and their three induced actions',
    'i=1,2,3; tensor of three factors; even vectors from EN116.1',
    ['tau1=id⊗sigma2⊗sigma3','tau2=sigma1⊗id⊗sigma3','tau3=sigma1⊗sigma2⊗id','tau_i acts on A by sigma_A/Ai'],
    '3 explicit tensor automorphisms and3 indexed induced actions; full F2^3 action on A is expressly rejected in general.',
    'Distinguishes the4-element subgroup action from the unavailable8-element action.',
    'Map each even nonzero triple to its tensor-factor flips and compare indexwise with the3 declared actions.',
    ['R02/R09'],
    'A new action distinction relative to the earlier notes’ two-factor product; no asserted descent of all8 symmetries.',
    ['tensor','automorphism','biquadratic','parity'],rs=[HUA_Q],anchors=['déf}}{=}\\tau_1','tau_i\\quad'],check='binary_group')
add('EN117.1',[117], 'Excluded characteristic-two non-etale patterns',
    'Three input quadratic algebras; at a characteristic2 point record whether each is non-etale',
    ['exclude points where at least2 of the3 inputs are non-etale'],
    'Authorial threshold≥2; editorial binary encoding gives4 forbidden patterns and4 remaining patterns among8.',
    'Conditional locus statement; the bit model counts status patterns, not actual points or algebras.',
    'Generate all triples of0/1 flags; count those of Hamming weight≥2.',
    ['L172.3–L172.6; R06 (scans172,192)'],
    'Extends the earlier notes’ two-factor degeneration warning to an explicit three-input exclusion; does not prove the asserted invariant-algebra isomorphism.',
    ['nonreduced','characteristic two','exceptional','non-étale'],rs=[HUA_Q,RS_SAME],anchors=['deux au moins'],check='binary_group')
add('EN119.1',[119,120,121], 'Three two-point sets, parity fiber J, and the three pair projections',
    'I1,I2,I3 of size2; chosen epsilon in their contracted product',
    ['J={(a1,a2,a3):a1∧a2∧a3=epsilon}','J→I1×I2','J→I2×I3','J→I3×I1'],
    'Literal:3 sets of2 elements and3 displayed pair maps. Derived in the split binary model:8 triples, each epsilon-fiber4,3 pair-target sets each4.',
    'Etale proposition with injective k→A, generation, and A^Gamma=k; finite-set verification does not remove these hypotheses.',
    'Enumerate both parity fibers; test all3 pair projections for bijectivity and the even subgroup action for transitivity/freeness.',
    ['R02/R09; §9.2 T172b'],
    'No same transitive-J enumeration occurs in earlier notes; related degeneration cautions prevent extending the etale count into a flatness theorem.',
    ['transitive','J','biquadratic','étale'],rs=[HUA_Q],anchors=['3 ens. à deux élts','J=\\{'],check='binary_group')
add('EN120.1',[120,121], 'Two hypotheses of the transitive-component lemma',
    'Group Gamma acts transitively on arbitrary J; closed subscheme Xcal⊂X_J',
    ['a) Gamma stability','b) written injectivity into Gamma(X_J,O_X_J)≃k^J'],
    '2 labelled hypotheses; no fixed finite value of |J| in the lemma.',
    'Literal target in b is X_J in the frozen reading; the proof uses component ideals. A corrected target must remain a research question, not a transcription change.',
    'For finite J the intended ideal argument tests constant ideals and their intersection; counting hypotheses alone does not repair the target issue.',
    ['R02/R09'],
    'No counterpart lemma found in earlier notes; no RS open item is claimed settled.',
    ['transitive','component','ideal','k^J'],rs=[],anchors=['a) $\\mathcal X','b) le composé'])
add('EN121.1',[121,122], 'Three maps from a biquadratic object to its three quadratic quotients',
    'X1,X2,X3=X1∧X2; later base change to Xcal0',
    ['projection to X1','projection to X2','product map to X3'],
    '3 target maps;122 repeats3 base-changed covers and3 arms.',
    '121 proposes extension beyond the etale setting;122 immediately records a nonflatness obstacle.',
    'Count the3 maps; in the split etale model identify them with the3 quotient maps of a4-point torsor.',
    ['R02/R06; §9.2 T172b'],
    'Adds a three-quotient organization; later notes warn about degenerating realizations but do not supply this three-arm diagram.',
    ['quotient','etale','degeneration','tensor realization'],rs=[HUA_Q],anchors=['X_3=X_1\\wedge X_2','revêts'],check='binary_group')
add('EN122.1',[122], 'Universal rank/degree-labelled diagram',
    'B=A1⊗A2⊗A3; B0=A1∧A2∧A3; B1=A1⊗B0',
    ['O→B:8','O→B0:2','B0→B:4(!), with not-universally-injective remark','B0→B1:2','B1↔B:2(!)'],
    '5 displayed numerical edge labels:8,2,4(!),2,2(!). In the etale model the derived absolute ranks are B8,B02,B14.',
    'The source explicitly says the morphism is not generally finite locally free or even flat; ! labels are not unqualified rank assertions.',
    'Check8=2×4 and8=4×2 only in the split etale model. Report the general relative-rank test as unsupported, not passed.',
    ['L172.3–L172.6; R06; §9.2 T172b'],
    'Provides a new three-factor diagram and an explicit nonflatness warning consistent with later realization warnings; neither rank4 algebra is thereby Azumaya.',
    ['not','flat','tensor realization','rank four'],rs=[HUA_Q,RS_SAME],anchors=['4(!)','2(!)','pas même fini'],check='binary_group')
add('EN124.1',[124], 'Two proposed splitting-compatibility conditions and two mixed tensor inputs',
    'Morphism of extensions(alpha,beta,gamma); two factors i=1,2',
    ['alpha pi=pi′ beta','beta varpi=varpi′ gamma','mixed inputs E1⊗L2 and L1⊗E2'],
    '2 condition formulas with a question-marked equivalence;2 mixed source summands.',
    'Explicit question; several maps and equality signs remain reading doubts.',
    'Compose both extension squares; count the two mixed tensor summands without treating the questioned equivalence as proved.',
    ['E170.3; §9.1 T160.2/T170.1'],
    'Precedes the later notes’ splitting identities and mixed-factor restrictions; adds the explicit question about equivalence of the two compatibilities.',
    ['splitting identities','mixed tensor','compatibility'],rs=[HUA_E],anchors=['Longleftrightarrow','E_1\\otimes L_2,'])
add('EN125.1',[125], 'Two named races in the cultural argument',
    'Reused typescript; two unnamed antagonistic superpowers',
    ['course à l’espace','course aux armements, nucléaires notamment'],
    '2 explicit named acts/races;2 superpowers asserted, not identified by name on this leaf.',
    'Authorial cultural interpretation, not an empirical conclusion of the catalog.',
    'Count only the two named items; do not infer a list of states.',
    ['T173.1; T179.1/T181.1 (scans173,179,181)'],
    'The earlier notes discuss cultural yin–yang valuation, but no matching two-race list was found.',
    ['space','armements','culture','yang'],family='reused_typed',rs=[],anchors=['course à l’espace','course à l\'espace','course aux armements'])
add('EN125.2',[125,135,137], 'Two aspects and their paired names',
    'Author’s self-description; no biological or psychological taxonomy is endorsed',
    ['l’homme / la femme','yang / yin'],
    'Literal “deux aspects ou faces”;2 paired naming schemes for the same two aspects, not4 distinct aspects.',
    'Authorial conceptual classification;135/137 discuss dominance and qualify his own classification.',
    'Preserve the two alias pairs and count the underlying aspects once.',
    ['T173.1; T175.1; §9.3 (scans173,175,177,183)'],
    'Supplies an earlier two-pole self-description, not extra entries in the later fourteen-pair action–inaction list.',
    ['yin','yang','fourteen','pairs'],family='reused_typed',rs=[],anchors=['deux\\quad a s p e c t s'])
add('EN126.1',[126,128], 'Four translations in the comparison square and two product constructions',
    'chi,gamma with gamma chi=2; b,b′,U; E1∨E2 and E1∧E2',
    ['top T_U','left T_-gamma b','right T_-gamma b′','bottom T_-U','E1∨E2≃E1∧E2; same for primed inputs'],
    '4 labelled square edges;2 parallel product-isomorphism formulas (unprimed and primed).',
    'Commutativity asserted; b′ sign is uncertain on126;128 requires gamma chi=2.',
    'With b′=b+chi U compute square defect(2-gamma chi)U; the opposite source reading is a separate branch, not silently repaired.',
    ['E170.4–E170.5; R11; §10.3'],
    'Adds earlier explicit square/coordinate data to the later notes’ conditional sign/gluing obstruction; the same scalar condition is not a new result here.',
    ['gluing defect','gamma','delta','coordinate'],rs=[HUA_E],anchors=['T_{-\\gamma b}','gamma\\chi=2'],check='transition')
add('EN126.2',[126], 'Four-corner extension comparison under endpoint changes',
    'For each i, Li/Li′ and Mi/Mi′; extensions Ei,Ei′,Ei″,Ei‴',
    ['Ei','Ei′','Ei″','Ei‴ (label doubtful)'],
    '4 extension slots in the grid;2 subobject labels and2 quotient labels. This is a structural grid, not4 isomorphism classes.',
    'Naturality construction with a doubtful fourth extension label.',
    'Enumerate the four corners of the two endpoint changes; leave map-direction questions to the frozen diagram.',
    ['§9.1 T168.1/T170.2 (scans168,170)'],
    'Earlier notes later compare two product constructions; this grid adds morphism/naturality bookkeeping rather than proving canonicity.',
    ['four horizontal','naturality','canonical comparison'],rs=[HUA_E],anchors=[r'E^{\prime\prime\prime}_i'])
add('EN127.1',[127,133,139,143,145], 'Three periods in the author’s self-history',
    'First childhood years; rupture1933 and subsequent change; third period beginning July1976/age48 in127',
    ['first: first five childhood years','second: repression/egotistical mechanisms after childhood rupture','third: maturity/return toward childhood; beginning described in127 and145'],
    'Author explicitly says3 periods. The first lasts5 years as reported; boundaries and descriptions are distributed over the listed leaves, not a numeric partition supplied in one table.',
    'Retrospective self-report;133’s2–3-year interval and143’s correction of a meditation sequence are not extra periods.',
    'Count named periods1–3; preserve stated dates/ages as parameters rather than calculating a new chronology from them.',
    ['T151.2/T151.4; T171.4 (scans151,171)'],
    'Current leaves supply the three-period framework; earlier notes distinguish July1976 self-acceptance from the later discovery of meditation and describe the continuation.',
    ['July 1976','juillet 1976','childhood','meditation'],family='reused_typed',rs=[],anchors=['trois périodes','trois grandes périodes','troisième période'],check='typed')
add('EN127.2',[127], 'Seven explicitly named yang-valued traits in an open list',
    'Author’s description of both parents; list ends with ellipsis',
    ['volonté','intelligence','contrôle de soi','ascendant sur autrui','intransigeance','Konsequenz','idéalisme'],
    '7 displayed entries, counted editorially; source does not state7 or claim the list exhaustive.',
    'Authorial classification; open list, so7 is a lower bound on named examples, not a complete taxonomy.',
    'Count the seven comma/parenthetical-separated main trait names, excluding explanatory glosses.',
    ['T147.3; T153.2; T175.1'],
    'Earlier notes discuss goal-directedness, paternal identification and later collected pairs; no identical seven-trait list found.',
    ['goal-directed','Konsequenz','father','yang'],family='reused_typed',rs=[],anchors=['volonté, intelligence'],check='typed')
add('EN127.3',[127,131,139], 'Family of four and the three nearest people',
    'Author, mother, father, older sister',
    ['mother','father','older sister','self'],
    '4 family members listed/explicitly counted on139;131 explicitly calls the other3 the nearest beings. These are overlapping counts, not4+3 distinct persons.',
    'Authorial family self-report; relationships are explicit in the supplied text.',
    'Count the four named roles; remove self to obtain the three others.',
    ['T153.2/T153.4 (scan153)'],
    'Adds explicit current family/closest-person counts to the earlier notes’ parental chronology and identification discussion.',
    ['family','father','parents','1933'],family='reused_typed',rs=[],anchors=['formée de mes parents','trois êtres les plus proches','tous les quatre'],check='typed')
add('EN127.4',[127], 'Two referenced sections',
    'Internal titles and section numbers36,37',
    ['Désir et méditation —36','L’émerveillement —37'],
    'Source explicitly says2 sections;2 titles and2 numbers.',
    'Bibliographic/internal enumeration, not two supplied sections.',
    'Count the two references; do not pretend the referenced section texts were supplied.',
    ['§8.3; T151.2/T171.4'],
    'No same two-section list in the earlier notes; related meditation discussion does not supply the absent sections.',
    ['Désir','émerveillement','meditation'],family='reused_typed',rs=[],anchors=['les deux sections'],check='typed')
add('EN128.1',[128], 'Comparison of two splitting conventions',
    'Tilded and untilded b_i,U_i,U,b,T; i=1,2; gamma chi=2',
    ['tilde b_i=-b_i','tilde U_i=-U_i','tilde U=U','tilde b=tilde b1 tilde b2=b1b2','later comparison uses tilde b=-b','tilde T described as inverse/opposite translation'],
    '2 conventions;2 indexed sign reversals and their product data. Listed sign statements are not a consistent table unless endpoint conventions are specified.',
    'Live sign-comparison calculation with literal tension between tilde b=+b and later -b; do not normalize the source.',
    'Check the two-factor sign product; treat the later -b as a separate endpoint convention needing interpretation, not a failed count.',
    ['E170.4–E170.5; R11'],
    'Adds source-level evidence for the later notes’ opposite-cocycle/sign-twist caution.',
    ['opposite','sign twist','splitting changes'],rs=[HUA_E],anchors=['widetilde b_i','widetilde U_i','widetilde b='],check='transition')
add('EN129.1',[129], 'Two fundamental questions in algebraic geometry',
    'Reused note dated3 October; author’s assessment',
    ['validity of the standard conjectures on algebraic cycles','resolution of singularities'],
    'Author explicitly says2 questions; Weil conjectures mentioned earlier are not a third member of this two-question list.',
    'Authorial research assessment and uncertainty about standard conjectures; no new resolution is claimed.',
    'Count the two named questions in the final comparison.',
    ['T169.5 (scan169); R09 as scope caution'],
    'Earlier notes mention current mathematical investment but contain no identical two-question enumeration; no supplied RS theorem resolves either question.',
    ['standard conjectures','singularities','mathematical investment'],family='reused_typed',rs=[],anchors=['deux questions les plus fondamentales'],check='typed')
add('EN130.1',[130,132], 'Paired splitting changes and the product change parameter',
    'p=(p1,p2), p′=(p1′,p2′); U1,U2; b_i=pi_i-chi p_i',
    ['p_i′=p_i-U_i','b1′=b1+chi U1','b2′=b2+chi U2','U=b1⊗U2+U1⊗b2+chi U1⊗U2'],
    '2 input changes and2 coefficient changes; one product parameter with3 written terms. This is a coordinate table, not a finite group count.',
    'Live; the terminal transformation formula and its coefficient need separate sign/normalization review.',
    'Expand(b1+chi U1)(b2+chi U2)-b1b2 and factor chi; no division by chi is needed.',
    ['E146.1/E146.3; §9.1 T146.3; R11'],
    'Same local coefficient identity as the earlier notes, with an earlier explicit tuple presentation; does not by itself prove global coherence.',
    ['coordinate change','b1','splitting','aσ+τb'],rs=[HUA_E],anchors=['p=(p_1,p_2)','b_1\\otimes U_2'],check='transition')
add('EN132.1',[132], 'Three-stage transition table and its repeated local coordinate models',
    'p,p′,p″; b_i,b_i′,b_i″; U_i,U_i′,U_i″; two factors',
    ['stage0: b_i','stage1: b_i′=b_i+chi U_i','stage2: b_i″=b_i′-chi U_i′ in upper table','later row literally writes b1″=b1′+chi U1′ but b2″=b2+chi U2′, with unprimed b2','3 copies of M⊕L and3 Hom labels'],
    'Upper array2×3:3 coefficient cells,2 downward arrows,1 blank cell. Three stages/models are explicitly displayed; factor index has2 values.',
    'Literal plus/minus conflict and a missing prime in the second-factor base across written rows; uncertain index2|3 elsewhere. Counts remain3 stages despite these reading/formula issues.',
    'Count the3 stage columns and retain both incompatible sign versions; do not report a single corrected transition table.',
    ['E146.1/E146.3; E170.5; §9.1 T146.3'],
    'Adds a three-stage descent test to the later notes’ two-stage coordinate table and gluing condition; the earlier notes cannot disambiguate this frozen source.',
    ['coordinate change','splitting changes','gluing defect'],rs=[HUA_E],anchors=['begin{array}{ccc}','b\'\'_i=b\'_i-'],check='transition')
add('EN132.2',[132], 'Three transition parameters and the cocycle test',
    'U for first step, U′ for second, U″ for composite; U_i″=U_i+U_i′',
    ['U=b1 U2+U1 b2+chi U1U2','U′=b1′U2′+U1′b2′+chi U1′U2′','U″=b1 U2″+U1″b2+chi U1″U2″','claimed U″=U+U′'],
    '3 displayed parameter formulas and1 labelled claim1°; some subsidiary indices/expansion terms are doubtful.',
    'Cocycle verification is attempted; only a declared consistent plus-sign branch is script-checked.',
    'Substitute b_i′=b_i+chi U_i and U_i″=U_i+U_i′; expand U″-U-U′. Also record the nonzero residual for a mixed sign branch.',
    ['R11; E170.5'],
    'The local-model composition law is already claimed checked in earlier R11; this page adds manuscript evidence of the same intended cocycle test, with unresolved literal signs.',
    ['composition','coordinate','gluing'],rs=[HUA_E],anchors=['U\'\'&=','U\'\'=U+U\''],check='transition')
add('EN134.1',[134], 'Two Hom maps and three sign reversals',
    'Ui:Mi→Li; alternate convention p_i′=p_i-U_i′',
    ['U1:M1→L1','U2:M2→L2|L1','U1′=-U1','U2′=-U2','U′=-U'],
    '2 map rows;3 sign-reversal rows. Product-coefficient signs are calculated nearby, not additional finite objects.',
    'Live sign investigation marked “signe étrange”; target/index and other signs remain uncertain.',
    'Count map and reversal rows separately; substitute negated variables only under an explicitly fixed product-sign convention.',
    ['E146.3; E170.4–E170.5'],
    'Adds the author’s earlier sign warning and coordinate-convention changes to the later sign-obstruction lead.',
    ['sign','opposite','coordinate'],rs=[HUA_E],anchors=['U_1:M_1','U\'_1&=-U_1'],check='transition')
add('EN134.2',[134,136], 'Two corresponding extension rows in the Hom! duality comparison',
    '0→H→E→O→0 and Hom!(E,H); subobject map -id, quotient map id',
    ['original extension row','Hom! extension row','endpoint actions -id on H and +id on O'],
    '2 compared extension rows and2 endpoint actions; scan136 repeats the comparison with L.',
    'Live comparison; source uses exclamation exponent, not prime, in Hom!.',
    'Count rows and endpoint actions; verify the bilinear formula restricts with the written negative sign on the subobject.',
    ['§9.2 T174c/T184b; R04'],
    'Earlier notes later register dual/original extension pairs; current pages supply the explicit endpoint sign and Hom! notation.',
    ['dual sequence','dual extension','sign','Hom'],rs=[HUA_E],anchors=['operatorname{Hom}^{!}'])
add('EN136.1',[136,138,140], 'Two generator strata for the product pairing',
    'f_i:E_i→L_i with restriction scalar lambda_i; tensor stratum and L1⊗L2 stratum',
    ['(f1*f2)(x1*x2)=lambda1 pi1(x1)⊗f2(x2)+f1(x1)⊗lambda2 pi2(x2)-chi f1(x1)⊗f2(x2)','(f1*f2)(u1⊗u2)=lambda1lambda2 u1⊗u2'],
    '2 prescribed input strata; formulas recur on136,138,140. The first has3 terms, not3 distinct input cases.',
    'Construction and boundary checks; source has several sign/index doubts and a cancelled erroneous coefficient on140.',
    'Evaluate separately on tensor generators and line–line generators; use f_i|Li=lambda_i to test the mixed boundary.',
    ['§9.1 T160.2; §9.2 T180b/T184c/T184d; L186.1'],
    'Precedes the later notes’ multi-block pairing specification and boundary checks; the two-stratum prescription alone is not a proof of all quotient compatibilities.',
    ['boundary','pairing','tensor/scalar','four blocks'],rs=[HUA_E],anchors=['f_1*f_2)(u_1','f_1*f_2\\,(u_1'])
add('EN136.2',[136], 'Four input-type cases and the four-term shifted-product expansion',
    'For each factor choose general f_i or U_i factoring through the quotient M_i and valued in L_i; alternatively x_i or u_i',
    ['f1*f2','f1*U2','U1*f2','U1*U2=-chi U1⊗U2','(x1+u1)*(x2+u2): original, first mixed, second mixed, line–line term'],
    '4 input-type combinations from2×2; shifted product explicitly has4 terms. The bracketed morphisms in mixed cases carry primes in the frozen text.',
    'Live formulas, one cancelled start, and “signe étrange!”; no exclamation exponent is substituted for the bracket primes.',
    'Enumerate the2×2 type choices; expand bilinearly, recording the different sign conventions of the two displayed products.',
    ['§9.2 T186c; §9.1 T160.2'],
    'Matches the later notes’ four-term lift-change structure while adding explicit mixed f/U formulas and sign warnings.',
    ['four displayed terms','mixed','change of lifts'],rs=[HUA_E],anchors=['(f_1*U_2)','(U_1*U_2)','+u_1)*'],check='binary_choices')
add('EN138.1',[138], 'Two-row specialization to pi1*pi2',
    'Tensor generators versus line–line generators; chi arbitrary in the writing',
    ['(pi1*pi2)(x1*x2)=chi pi1(x1)⊗pi2(x2)','(pi1*pi2)(u1⊗u2)=chi²u1⊗u2'],
    '2 listed evaluations; followed by a formula written with1/chi.',
    'Formal specialization; division by chi requires interpretation/hypotheses not supplied by the two-row count.',
    'Substitute f_i=pi_i, lambda_i=chi in EN136.1; keep division separate from the integral coefficient check.',
    ['E156.1/E156.2; E170.3'],
    'Adds a concrete specialization to the later notes’ warnings against cancelling or dividing by chi.',
    ['divide','division','chi','scalar'],rs=[HUA_E],anchors=['pi_1*\\pi_2)(x_1','pi_1*\\pi_2)(u_1'])
add('EN138.2',[138], 'Two-by-two object/map table and three adjacent formal expressions',
    'Li,Mi and maps pi,qi for i=1,2',
    ['row1: Li,pi','row2: Mi,qi','1+p1q1','1+p2q2','1+(p1p2)(q1q2)'],
    'Array2×2=4 populated cells;3 adjacent expressions compare factor1,factor2,product.',
    'Fragmentary notation; no completed group law or classification follows from the layout.',
    'Count source cells and expressions; type-check maps before any algebraic evaluation.',
    ['§9.1 T146.4; §9.2 T182b'],
    'Related terminology and parallel-factor tables occur later, but no exact counterpart of these three fragmentary expressions was found.',
    ['terminology','parallel notation','factor'],rs=[HUA_E],anchors=['begin{array}{cc}','1+\\underbrace'])
add('EN139.1',[139], 'Paired parental death dates',
    'Reused footnote; author’s family chronology',
    ['father: Auschwitz1942','mother:1957'],
    '2 people and2 reported dates; not independent historical verification.',
    'Authorial historical self-report.',
    'Count the two named date assignments; do not merge them with the four-person family count.',
    ['T153.4 (scan153)'],
    'Earlier notes report the father’s1942 disappearance and family chronology; current footnote adds the explicit1957 maternal date.',
    ['1942','1957','family chronology'],family='reused_typed',rs=[],anchors=['Mon père est mort'],check='typed')
add('EN140.1',[140], 'Paired complementary splittings and two special input classes',
    'i=1,2; qi(mi)=xi-pi(xi); product p,q',
    ['q1(m1)=x1-p1(x1)','q2(m2)=x2-p2(x2)','general product x1*x2','line inputs u1⊗u2'],
    '2 factor identities and2 input classes; the intervening expansion is a derivation, not a separate enumeration of solutions.',
    'Live boundary calculation with cancelled coefficient attempts.',
    'Substitute the two complementary splittings and test the line–line specialization without retaining cancelled expressions as axioms.',
    ['§9.1 T160.2/T164.1; §9.2 T186c'],
    'Precedes later complementary-operator and mixed-boundary tables, with the same need to preserve cancellation history.',
    ['complementary','mixed tensor','boundary'],rs=[HUA_E],anchors=['q(m_1)|q_1(m_1)','u_1*u_2='])
add('EN141.1',[141], 'Three subjects of private lessons',
    'Reused account of the former pastor’s livelihood',
    ['latin','grec','mathématiques'],
    '3 explicitly named subjects, counted editorially; the source does not state a numerical total.',
    'Historical self-report; this is not an exhaustive curriculum claim.',
    'Count the three names following “leçons particulières”.',
    ['T153.4 (scan153); §8.2 printed-page chronology'],
    'No matching subject list in the earlier notes; only the surrounding family chronology is related.',
    ['latin','grec','lessons','family chronology'],family='reused_typed',rs=[],anchors=['leçons particulières de latin'],check='typed')
add('EN142.1',[142], 'Two prescribed composites for F11',
    'F11:E1⊗E2→E1⊗E2; kernel inclusion mu and quotient map nu',
    ['1° F11∘mu is prescribed through pi and L1⊗L2','2° nu∘F11 is prescribed through psi1⊗psi2 and omega','pi∘(alpha1⊗alpha2)=chi id','(psi1⊗psi2)∘omega=chi id'],
    '2 numbered F11 constraints;2 marginal boundary identities. The phrase “deux autres carrés” is contextual, not two further constraints written here.',
    'Conditional construction: existence of F11 with the required squares gives an extension isomorphism; not claimed solved merely by enumeration.',
    'List the two composites, then test candidate maps against both; do not replace existence by a count of equations.',
    ['E154.2; E166.1–E166.3; §9.1 T166.1/T166.2'],
    'Direct earlier occurrence of the same two nonautomatic comparison squares that the later notes identify around F11; adds explicit boundary prescriptions.',
    ['F_{11}','two compatibilities','two squares','four block'],rs=[HUA_E],anchors=['1°) Connu','2°) $\\nu'])
add('EN142.2',[142], 'Scalar specialization and two endpoint actions of the involution',
    'chi,gamma with gamma chi=2; special chi2,gamma1; L1 and M1',
    ['chi=2,gamma=1','sigma|L1=-id','sigma on M1=+id','bar(x1⊗x2)=bar x1⊗bar x2'],
    '1 explicit scalar pair;2 endpoint actions;2 factor conjugations induce1 tensor conjugation.',
    'Specialization and comparison ansatz, not an all-chi involution claim.',
    'For chi2 use P²=2P and sigma=I-P to check sigma²=I and the two stated endpoint eigenvalues.',
    ['E148.1; E150.2; §9.1 T150.1/T152.1/T156.1'],
    'Restates earlier-in-the-manuscript the same scalar restriction and endpoint sign pattern later noted for the ansatz.',
    ['gamma','scalar condition','-1,+1','involution'],rs=[HUA_E],anchors=['gamma\\chi=2','-\\mathrm{id}_{L_1}'],check='transition')
add('EN143.1',[143], 'Three initials in a quoted relational sequence',
    'Author’s quotation; identities deliberately not inferred',
    ['M.','J.','S.'],
    '3 listed initials in the sequence “M., puis de J., puis de S.”; count is editorial, not an author-stated3.',
    'Quoted autobiographical interpretation; names and factual judgments are not reconstructed.',
    'Count the three displayed initials only.',
    ['T151.2; T157.1; T165.4'],
    'Earlier notes discuss the meditation and relationships but do not supply an identical three-initial list; current page480 also fills a pagination gap.',
    ['meditation','lovers','relationships'],family='reused_typed',rs=[],anchors=['M., puis de J., puis de S.'],check='typed')
add('EN144.1',[144], 'Two operator/domain rows and two induced value rules',
    'fi preserves Li; f_i^! denotes its restriction in the frozen reading',
    ['f1⊗f2 on E1⊗E2','f1^!⊗f2^! on L1⊗L2','f(x1*x2)=f1(x1)*f2(x2)','f(u1⊗u2)=f1^!(u1)⊗f2^!(u2)'],
    'First table2×3=6 populated cells including the “sur/---” column;2 substantive operator/domain rows and2 following value rules.',
    'Exploratory compatibility calculation; f! versus u! is doubtful in one definition, but exclamation/prime distinctions are frozen.',
    'Count the two strata; test preservation on mixed tensors separately rather than assuming the two displayed rules descend.',
    ['L174.1–L174.3; §9.2 T174a/T174b; §9.1 T160.2'],
    'Provides earlier explicit operator/stratum tables for the later endomorphism-restriction discussion.',
    ['restriction','endomorphism','two numbered conditions','mixed tensor'],rs=[HUA_E],anchors=['f_1\\otimes f_2&','f(x_1*x_2)'])
add('EN144.2',[144], 'Two-column map/scalar family and its repeated small table',
    'f1:E1→L1, f2:E2→L2; associated lambda1,lambda2',
    ['factor1: E1→L1 by f1; lambda1','factor2: E2→L2 by f2; lambda2','small array rows(f1,f2) and(lambda1,lambda2)'],
    '2 indexed factor columns; explicit small array2×2=4 data cells; preceding diagram has3 node rows×2 columns plus2 arrow labels.',
    'Fragmentary example with cancelled trials; no scalar classification or equation-solution count asserted.',
    'Count the repeated pair table separately from the preceding diagram; retain doubtful surrounding coefficients as reading issues.',
    ['§9.2 T182b/T190c; E148.3'],
    'Related parallel-factor tables appear later; these fragments add the particular f/lambda pairing but not a completed endomorphism-sheaf definition.',
    ['parallel notation','coefficient extraction','endomorphism'],rs=[HUA_E],anchors=['f_1&f_2','lambda_1&\\lambda_2'])
add('EN145.1',[145], 'Two declared repressive forces, one explicitly developed here',
    'Reused typescript; author’s retrospective classification',
    ['explicit here: repression of traits called feminine, in favor of virile values','second force is declared but not named in this enumeration on145'],
    'Author explicitly says2 forces;1 is developed on this leaf. Do not invent a second listed entry from context.',
    'Incomplete local enumeration; earlier discussion of buried childhood is related but not a second numbered item here.',
    'Record declared2 versus explicitly developed1; keep the missing member unresolved within this leaf.',
    ['T153.1 (scan153)'],
    'Earlier notes explicitly describe burial of the past plus promotion of virile traits, and qualify that these are not all life forces; this supplies a continuation lead, not replacement text.',
    ['two repressive','burial of the past','l’une de ces deux'],family='reused_typed',rs=[],anchors=['deux grandes forces','L\'un de ces mécanismes'],check='typed')
add('EN145.2',[145], 'Four raised children and a fifth/last child',
    'Author’s footnote; membership not identified by name',
    ['4 whom he helped raise','fifth and last raised by the child’s mother'],
    'Literal4 and “cinquième et dernier”; derived partition4+1=5 children. This is not the distinct4-person childhood family.',
    'Authorial self-report; no additional personal identities inferred.',
    'Add4+1 and keep the two family contexts separate.',
    ['T153.4; §9.4 (different4+1 arts list on189)'],
    'No same children enumeration found in earlier notes; its4+1 arts count is explicitly unrelated despite identical arithmetic.',
    ['children','cinquième','quatre','family'],family='reused_typed',rs=[],anchors=['aux quatre parmi eux','cinquième et dernier'],check='typed')
add('EN-P01',list(range(97,123))+list(range(124,146)), 'Supplied scan and handwritten-number coverage',
    'Archive scans97…145, omitted blank123; handwritten numbers96…144 except122',
    ['49 scan positions minus1 omitted blank =48 supplied pages','37 mathematical/cancelled mathematical faces and11 reused typed faces','handwritten-number set96…144 except122'],
    'Derived corpus counts48=49-1 and37+11; the numbers on individual leaves are literal, but48 is not an authorial total-page statement.',
    'Current frozen file inventory; omitted blank comes from the attachment instructions.',
    'Enumerate expected scan IDs and mspage numbers; classify the11 typed leaves by their printed400-series numbers.',
    ['§8.1/§8.2/§9.4 (scans146–193)'],
    'Extends the later notes’ archival-count method; does not merge handwritten and printed pagination systems.',
    ['pagination','pencil','typed leaves'],family='archival',rs=[RS_SAME],check='pagination')
add('EN-P02',[125,127,129,131,133,135,137,139,141,143,145], 'Current reused-typescript printed-page set',
    'Printed pages465…474 plus480; scan order differs from page order',
    ['125→465','127→466','129→467','131→468','133→469','135→470','137→471','139→472','141→473','143→480','145→474'],
    '11 supplied typed leaves;10 consecutive pages465–474 plus1 page480. Derived, not an authorial11-page title count.',
    'Current frozen transcription metadata; no date for the mathematical writing is inferred.',
    'Extract mspage values≥400 from these files and compare the mapping exactly.',
    ['§8.2 (scan-to-page table); §9.4'],
    'Current143 supplies page480, which the earlier notes list as absent from their own packet.',
    ['480','475 bis','printed pagination'],family='archival',rs=[RS_SAME],check='pagination')
add('EN-J01',[143], 'Joint reported printed-page coverage across the two packets',
    'Current11 typed leaves; earlier notes’24 typed leaves(475–500 excluding480,481,485 plus475bis)',
    ['current set:465–474 and480','earlier reported set:475–500 except480,481,485, plus475bis','union:465–500 except481,485, plus475bis'],
    'Derived union11+24=35 leaves;34 ordinary numbered pages plus475bis. Sets are disjoint as reported.',
    'Joint count is conditional on unreviewed earlier-note pagination; earlier scans were not inspected by this cataloger.',
    'Parse the earlier §8.2 mapping, union it with current printed labels, check35 and missing ordinary labels481,485.',
    ['§8.2/§9.4 (earlier24-leaf table)'],
    'Adds current page480 to fill one reported gap; does not claim a continuous manuscript or infer why481/485 are absent.',
    ['480','481','485','475 bis'],family='archival',rs=[RS_SAME],check='pagination')

def source_location(item):
    result = []
    for scan in item['scans']:
        path=ROOT/'pages'/f'MPL_84_097-145_84_scan{scan:03}.tex'
        text=path.read_text()
        hits=[]
        for n,line in enumerate(text.splitlines(),1):
            if any(anchor in line for anchor in item['source_anchors']): hits.append(n)
        result.append({'file':path.name,'scan':scan,'anchor_lines':hits})
    return result

def escape(s):
    return str(s).replace('|','\\|').replace('\n',' ')

for item in ITEMS:
    item['sources']=source_location(item)
    item['context_status']='Earlier same-cote notes are first-pass/unreviewed leads. RS statuses remain exactly those of the supplied register; no result is upgraded here.'

metadata={'catalog_scope':'Every explicit finite list, labelled condition system, table/comparison array, selected symbolic cases, typed explicit enumeration, and archival count found in the 48 frozen page texts. Ordinary derivation lines and unnumbered rhetorical contrasts are not automatically sets. No images or OCR used by this cataloger.',
    'count_convention':'Author-stated numerals, counted written entries/layout cells, and independently derived model totals are distinguished in each counts field. Reading uncertainty is separate from cardinality.',
    'source_status':'The transcription was frozen by root before this research. It is not modified by these files.',
    'context_file':'context/same_cote_84/MPL_84_146-193_notes.md',
    'negative_independent_pages':{118:'Factorization/invariant-subalgebra argument; no independent table or enumerated list.',133:'Continues the family/period narrative catalogued under EN127.1/EN127.3; no new independent table/list.',135:'Continues the two-aspect discussion in EN125.2; no new explicit finite list.',137:'Continues the same discussion and explicitly declines a review of all signs; examples in prose are not a complete enumeration.'}}
(OUT/'enumerations.json').write_text(json.dumps({'metadata':metadata,'items':ITEMS},ensure_ascii=False,indent=2)+'\n')
columns=['id','scans','layer','title','parameters','entries','counts','status','recomputation_recipe','context_references','context_relation','results_state_ids','check']
with (OUT/'enumerations.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader()
    for item in ITEMS:
        row={k:item[k] for k in columns}
        for k in ['scans','entries','context_references','results_state_ids']:row[k]='; '.join(map(str,row[k]))
        w.writerow(row)

lines=['# Tables and enumerations: cote84, scans097–145','','## Scope and counting rules','',metadata['catalog_scope'],'',metadata['count_convention'],'',
    'The rank-four tensor algebra in the quadratic calculations is commutative. Neither that rank nor the finite four-point model establishes the rank-four central Azumaya algebra required by the planning bridge B12. No regular-polyhedron/congruence-level enumeration is found here; the unrelated LM2 claims are not advanced by these counts.','',
    'Context shorthand below refers throughout to `context/same_cote_84/MPL_84_146-193_notes.md`. Those earlier notes are first-pass leads, including their reported calculations and pagination. The cited Hua entries in `context/notes/RESULTS_STATE.md` are AI-produced claims, not reviewed results.','',
    'Machine-readable entries, exact source basenames/anchor lines, and search terms are in `enumerations.json`; the flat companion is `enumerations.csv`. Run `python3 scripts/recompute_enumerations.py` for the declared finite models and symbolic checks; its output distinguishes verified models from unproved manuscript assertions.','']
for layer,title in [('math','Mathematical tables and enumerations'),('reused_typed','Explicit lists in the reused typescript'),('archival','Archival and cross-packet counts')]:
    lines+=['## '+title,'','| ID / scans | What and parameters | Entries / counts | Status and recomputation |','|---|---|---|---|']
    for it in ITEMS:
        if it['layer']!=layer:continue
        lines.append('| '+escape(it['id']+' / '+','.join(map(str,it['scans'])))+' | '+escape(it['title']+' — '+it['parameters'])+' | '+escape('; '.join(it['entries'])+'; '+it['counts'])+' | '+escape(it['status']+' Recipe: '+it['recomputation_recipe'])+' |')
    lines.append('')
lines+=['## Per-item context comparisons and register links','']
for it in ITEMS:
    src='; '.join(s['file']+((': lines '+','.join(map(str,s['anchor_lines']))) if s['anchor_lines'] else '') for s in it['sources'])
    lines += ['### '+it['id'],'',f"Source: {src}. Context: {'; '.join(it['context_references'])}. {it['context_relation']} Results-register relation: "+('; '.join(it['results_state_ids']) if it['results_state_ids'] else 'no subject-matched mathematical result ID; the typed or new structural enumeration does not settle an unrelated register item.')+'.','']
lines += ['## Per-page coverage and negative findings','','Archival counts EN-P01 apply to every supplied page and are omitted from the table below so they do not disguise a page with no substantive enumeration.','', '| Scan | Relevant catalog IDs | Coverage qualification |','|---:|---|---|']
for scan in [*range(97,123),*range(124,146)]:
    ids=[it['id'] for it in ITEMS if scan in it['scans'] and it['layer']!='archival']
    qual=metadata['negative_independent_pages'].get(scan,'Enumerations/tables listed above; ordinary equation derivations are not separately counted.')
    lines.append(f"| {scan} | {', '.join(ids) or 'None'} | {escape(qual)} |")
lines+=['','## Important limits','','- A table cell count does not certify a map, prove independence of axioms, or enumerate isomorphism classes.','- EN115.1 retains the literal asymmetric/uncertain arrows; its completed permutation action is explicitly an editorial model.','- EN122.1 keeps the labels4(!) and2(!) tentative because the same page denies general flatness.','- EN132.1 records both written signs; the cocycle check uses the declared consistent branch and reports the other branch separately.','- Typed lists are the author’s claims or self-reports. Counts do not establish their psychological or historical interpretation.','- EN-J01 uses only the earlier notes’ reported mapping, not a new examination of earlier scans.','']
(OUT/'enumerations.md').write_text('\n'.join(lines)+'\n')

search_files=[CONTEXT/'same_cote_84/MPL_84_146-193_notes.md',CONTEXT/'notes/RESULTS_STATE.md',CONTEXT/'README.md',CONTEXT/'LM2_CONGRUENCE_ROWS.md']
searchlog=['# Context searches for every enumeration item','','Searches operate on the supplied text files only. Case-insensitive literal terms are logged separately, including zero-hit searches; lexical matches are not automatically substantive links. Selected relevant references and their relation are recorded after each item. Earlier note claims remain unreviewed leads.','']
for it in ITEMS:
    searchlog+=['## '+it['id'],'','Queries: '+', '.join('`'+q+'`' for q in it['context_queries'])+'.','']
    for file in search_files:
        source_lines=file.read_text().splitlines()
        searchlog.append('### '+str(file.relative_to(CONTEXT)))
        searchlog.append('')
        for query in it['context_queries']:
            hits=[(i+1,line) for i,line in enumerate(source_lines) if query.casefold() in line.casefold()]
            searchlog.append(f'- `{query}`: {len(hits)} matching lines.')
            for number,line in hits[:3]:searchlog.append(f'  - Line {number}: '+line[:220].replace('\n',' '))
        searchlog.append('')
    searchlog+=['Selected comparison: '+'; '.join(it['context_references'])+'. '+it['context_relation'], 'Register IDs: '+('; '.join(it['results_state_ids']) or 'none substantively matched')+'.','']
(OUT/'enumeration_context_searches.md').write_text('\n'.join(searchlog)+'\n')
print(f'Wrote {len(ITEMS)} catalog items; layers '+str(dict(Counter(it['layer'] for it in ITEMS))))
print('Source pages untouched; no image access, combining, freezing, archiving, or uploads.')
