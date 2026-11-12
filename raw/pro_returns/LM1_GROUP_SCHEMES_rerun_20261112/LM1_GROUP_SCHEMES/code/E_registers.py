"""Build and audit the Part E statement, reading, and task registers."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
tex=(ROOT/'sections/E.tex').read_text()
heads=re.findall(r'\\begin\{statement\}\{(E\.\d+)\}\{([^}]+)\}\{([^}]+)\}',tex)
assert len(heads)==25 and len({h[0] for h in heads})==25

# id: (assertion, dependencies, manuscript locus, reading dependence, notes)
items={
1:('The manuscript Ga-valued definition implies exponent p in characteristic p; quasi-unipotence there is finite order.',
 'None','50.1; 650bis; 140-4:5--6','Definition, not an unsettled word.',
 'Witt elements of order p^2 test conventional unipotence, not the source definition.'),
2:('For any Q-algebra and closed linear group scheme, every fibrewise-unipotent section is uniquely exp(t log g).',
 'E.1','50.1; 650bis verso; 140-4:6','Q-algebra distinguished from characteristic zero, scan13.',
 'Cayley--Hamilton and Vandermonde proof works over nonreduced Q-algebras; no claim for arbitrary non-linear targets.'),
3:('Over a torsion-free Z-algebra, a nilpotent g-I in a closed linear group extends uniquely iff every (log g)^i/i! is integral.',
 'E.2','50.1; 651 verso--652; 140-4:8--9','No; exact interpretation of equation10.',
 'Necessary and sufficient coefficient criterion; factorization through the closed subgroup proved.'),
4:('Integrality of exp(X) and exp(-X) does not imply integral divided powers; a rank-three counterexample is minimal.',
 'E.3','50.1; 652; 140-4:9','Actual exponential hypothesis includes the linear term omitted from equation11.',
 'X=J3-J3^2/2; both exponential matrices and inverses checked exactly.'),
5:('The literal signed implication (X^2/2 plus or minus X^3/6 integral) is false in rank four; adding X integral makes it true.',
 'None','50.1--2; 652--652 verso; 140-4:9--10','Dropped linear term; denominator1/2 versus1/6 in12bis.',
 'Finite grid finds the displayed counterexample after168 candidates; local proof on D(2),D(3) gives the correction.'),
6:('A rank-five section over Z is genuinely fibrewise Ga-valued and has no Ga extension; the local rank bound r<=p^2 is sharp.',
 'E.2; E.3','50.1--2; 650bis--654; 140-4:6--13','Does not use the omitted-linear-term reading.',
 'Weights1,2,3,2; logarithm integral but fourth divided power is E15/2. General first obstructed degree p^2.'),
7:('W2 has elements of order p^2; the smooth group law x+y+p*C_p(x,y) over Z/p^2 has a fibrewise Ga-valued section that has no Ga lift.',
 'E.1','50.1; 650bis verso; 140-4:6','Source definition separated from conventional usage.',
 'Proof for every prime and every polynomial degree; finite exact tests p2,3,5 and1024 Z/4 polynomials degree<=6.'),
8:('Binomial polynomials characterize integer-valued polynomials; integer-tuple vanishing over any ring is killed by a further integer dilation.',
 'None','50.1--2; 652--654; 140-4:9--13','Scan13 A|K and 3!|6! alternatives tested; characteristic0 versus Q-algebra corrected.',
 'Newton differences and tensor Vandermonde proof;72 specified degree<=12 matrix cases, not an exhaustive search over all rational matrices.'),
9:('For an affine finite-type target and schematically dense D(n), a Ga homomorphism extends after dilation by a power of n; the scheme version needs exactly extension of its value at0.',
 'None','50.2; 654 verso--655 verso; 140-4:14--16','Scan12 lambda^n corrected to n*lambda; scan14 finite type|finite presentation and n>=1|n>=0.',
 'Finite algebra-generator denominator argument; uniqueness proves the group law and gluing.'),
10:('For every ring and every closed linear finite-presentation group scheme, fibrewise quasi-unipotence is equivalent to a positive power lying on a Ga subgroup.',
 'E.2; E.8','50.2; 652 verso--655 verso; 140-4:10--16','Theoreme(!) read literally, with explicit added linearity hypothesis.',
 'Constructible compactness, uniform nilpotence, integral binomial dilation and finite-equation torsion killing.'),
11:('The full source theorem for arbitrary separated locally finitely presented group schemes, and the Q-algebra statement without linearity, remain unproved here.',
 'E.2--E.10','50.1--2; 650bis verso--655 verso; 140-4:6,10--16','Both affine S|S0 target readings retained in the later universal theorem.',
 'Exact residual, proved cases, executed computations, and first base-dimension-zero unproved tests Q[eps]/eps^2 and Z/4 recorded; no literature-open assertion.'),
12:('For a finitely generated virtually abelian group, a normal lattice yields an explicit smooth integral affine-space cocycle model and exact fppf extension.',
 'None','50.3--4; 656--660; 140-4:17--25','Source metabelian means virtually abelian; disconnected-point sheafification is essential.',
 'Coordinate ring product_H Z[x1,...,xr]; polynomial group law, inverse, change of section, and pushout universal property proved.'),
13:('The full envelope has coordinate colimit product_{Gamma/nM}Z[x]; kernel Z+(x)Q[x]; every Fp fibre is the proconstant full profinite completion.',
 'E.12','50.4; 659--662; 140-4:23--29','Scan29 nA=0 and characteristic0 remarks corrected.',
 'Finite-stage smooth r-dimensional fibres distinguished from reduced dimension-zero proconstant limit fibres.'),
14:('Restriction from the envelope bijects with fibrewise quasi-unipotent representations into closed linear finite-presentation targets over every ring.',
 'E.8; E.10; E.12; E.13','50.5; 662 verso--663 verso; 140-4:30--32','Scan31 inverse limit in58 corrected to direct limit; scan32 affine S|S0 not silently chosen.',
 'Explicit polynomial one-parameter maps centralize all lattice images; finite polynomial identities give existence and uniqueness after refinement.'),
15:('Pi0 is a normal free group of rank2 and index12 in SL2Z; S=SL2Z/[Pi0,Pi0] has lattice Z^2, quotient Dic3, and abelianization C12.',
 'C.2','51.1; 664--664 verso; 140-4:33--34','Deleted completion hats and the surviving word profinis typed separately.',
 'Exact matrices, finite quotient SL2(Z/4)/V4, amalgam tree, and lattice-action matrices.'),
16:('The finite-stage modular envelope is product_12 Z[x,y] with an explicit integral cocycle; all fibres are smooth dimension2, including2,3.',
 'E.12; E.15','51.1; 664--665; 140-4:33--35','Discrete versus completed lattice distinguished.',
 'All144 cocycle values and1728 associativity triples checked; finite quotient orders and point counts attached.'),
17:('E_Gamma(Z)=Gamma, E_Gamma(Zp)=hatGamma, E_Gamma(Zhat)=product_p hatGamma; the finite-stage Delta subgroup of Zhat-points is hatGamma.',
 'E.12; E.13','50.4; 662; 140-4:29; 51.1; 665; 140-4:35','The Delta superscript in35(13) is essential.',
 'Full Zhat-point functor is not the diagonal component subgroup; proof includes topology and the p-divisibility kernel.'),
18:('Lead3 identification with full pro-algebraic, Malcev, integral Hall/Lazard or divided-power hulls is false; canonical maps and separating examples are given.',
 'E.3; E.13; E.14; E.15','50.4--5; 659--663; 140-4:23--32','Virtually abelian source meaning is essential.',
 'P_Q(Gamma)->E_Gamma,Q->U_Q(Gamma); Z character2^n, divided-power coordinate distinction, finite relative quotient map, and nonfinite reductive example Ga x Gm with no compatible maps either way.'),
19:('Relative completion of SL2Z over its order12 quotient, with its unipotent kernel abelianized, is the rational finite-stage S model; GL2Z/order24 is analogous.',
 'E.12; E.15; E.16','51.1; 664--665; 140-4:33--35','Discrete/profinite distinction and orientation action included.',
 'Direct universal-property proof from Hain Section1; full envelope is different because its profinite component group is infinite.'),
20:('The full comparison of named M_rho,sigma/N_rho,sigma functors with signed automorphism functors and the Fermat relative-completion targets remains partly settled.',
 'E.15--E.19; E.24; E.25','51.2; 665 verso--668; 140-4:36--41; After BISITE Fermat relative-completion follow-up','Local conjugators, sign retention, quotient conventions and the distinct deck-quotient comparison specified as residual.',
 'Generic no-sign functor and integral fine parameters computed; genuine infinitesimal and sign obstructions proved. First remaining named signed comparison over the field F2. Separately, free F_2=<x,y> maps to (Z/2)^2 by x->(1,0),y->(0,1); no named-scheme comparison of its relative completion or abelian-kernel quotient is proved. Targets (Z/n)^2 and S3 x Zhat^* retained explicitly.'),
21:('The BISITE free-group endomorphism induces automorphisms of every nilpotent quotient, every pro-p completion and the rational unipotent completion, but changes the S3 covering.',
 'None','After BISITE follow-up; source scope50.4; 660; 140-4:25','No historical motivation is inferred.',
 'Independent graded-commutator, Frattini and Hopfian proof; exact permutation action goes from orbit3 to orbits2+1.'),
22:('The modular envelope retains the three-letter S3 covering through its finite quotient; modern metabelian and manuscript virtually abelian scopes differ.',
 'E.13; E.15; E.18; E.21','50.4--51.1; 660--665; 140-4:25,33--35','Terminology correction only.',
 'Modulo2 kills Pi0, so S3 is retained; free metabelian F2/F2-double-prime is not virtually abelian, proved via Z wreath Z.'),
23:('For B S, fibrewise rationalization keeps discrete S, schematization is B P_Q(S), and the integral envelope represents the strictly smaller quasi-unipotent representation theory.',
 'E.12; E.14--E.18','After BISITE / GALOIS C.13--C.14; source50.5; 663; 140-4:31--32','No doubtful reading needed.',
 'RWZ Theorems3/16 and Toen Corollary3.3.7 used with a full algebraic-goodness reduction; induced12-dimensional character has eigenvalue2.'),
24:('The scan41 fine parameter scheme is an open A^3 over Z in each sign pair; the actual rational no-sign automorphism group is Ga semidirect Gm.',
 'E.12; E.15; E.16','51.2; 667--668; 140-4:39--41','All coherent +/- alternatives in31 and the middle -|= in32 tested; fixed convention from38(21),39(28).',
 'Smith invariants(1,3) become(1,1) after nu-prime is included; exact counts p<=13,n4,8,9; generic action and composition checked.'),
25:('Over Fp[eps]/eps^2 a nonidentity automorphism fixes all discrete S elements and the loop line; overQ the same automorphism can have opposite-sign rho conjugators.',
 'E.12; E.15; E.16; E.24','51.2; 665 verso--666; 140-4:36--37','Formula16 generator determination and formula18 sign well-definedness refuted in the stated model.',
 'T(v)=v+eps(v^[p]-v), inverse with minus; polynomial tests p2,3,5. Correct generator-determination statement proved under A-linearity on M.')}

results=[]
for ident,status,title in heads:
    a,deps,locus,reading,note=items[int(ident.split('.')[1])]
    results.append({'id':ident,'statement':a,'status':status,
       'where_proved':'sections/E.tex, '+ident,'depends_on':deps,
       'manuscript_passages (section; folio; scan)':locus,
       'depends_on_doubtful_reading (scan, alternatives)':reading,'notes':note})

readings=[]
def reading(package,scan,place,support,strength):
    readings.append({'package':package,'scan':'140-4:'+scan,
       'the \\unsure or \\illegible place':place,
       'what the mathematics supports':support,'how strongly':strength})
p1='LM_C4-001-019';p2='LM_C4-020-038';p3='LM_C4-039-057'
reading(p1,'5--6','Definition of unipotent through phi(1), contrasted with the requested Witt-vector examples.',
 'An actual Ga value has exponent p. Order-p^2 Witt elements refute conventional matrix-unipotence, not this stronger source definition; E.1,E.7.',
 'Conclusive mathematical distinction; scan5 and6 photographs inspected.')
reading(p1,'9','n=3 idem; omission of +/-X when passing from (9) to (11).',
 'The actual exponential statement fails in rank3; the literal dropped-linear-term statement is different and fails in rank4; E.4,E.5.',
 'Exact rational counterexamples and photographed formulas; no claim of final editorial intention.')
reading(p1,'10','X0 integral but not in2M4(A), X=X0/2^nu in (11bis).',
 'The rank4 example has X0=2X integral and not divisible2, with nu=1, so it satisfies this normalization.',
 'Exact matrix verification; photograph inspected.')
reading(p1,'10','1/2 versus1/6 coefficient multiplying X0^3 in (12bis).',
 'At residue characteristic2 these integrality conditions differ by the unit3 and are equivalent; that equivalence must not be asserted at3.',
 'Conclusive in the explicitly localized ring; paleographic alternative remains recorded.')
reading(p1,'12,14--15','phi_U^n: lambda maps to phi_U(lambda^n), compared with formula22 m*lambda and T maps to mT.',
 'Precomposition must be multiplication by n, not exponentiation of the additive variable; the latter is not additive in characteristic0. E.9.',
 'Map types, displayed formula22 and photographs12,14,15 give strong mathematical evidence.')
reading(p1,'13','Equation20 initial X in M5(A|K), concluding X in M5(A).',
 'A reading is tautological. K reading is false for X=E12/2, X^2=0; both signed higher combinations vanish. E.8 and executed code.',
 'Both literal alternatives decided mathematically; photograph inspected; no final transcription chosen.')
reading(p1,'13','Cubic denominator3! in checked text versus6! in first pass.',
 '3! obeys the exponential addition identity;6! gives t^2*u*E14 coefficient -119/240 on J4. E.8.',
 'Polynomial calculation conclusive for exponential meaning; photograph supports3!.')
reading(p1,'13','car.0 i.e. Q-algebra; logarithm margin saying arbitrary characteristic-zero ring.',
 'Q-algebra is sufficient. Characteristic0 alone is insufficient; Z and the rank5 example separate them. E.2,E.6,E.8.',
 'Mathematical correction conclusive; photograph inspected.')
reading(p1,'14','n>=1|n>=0 and finite presentation|finite type in the dilation proposition.',
 'Finite type suffices. With schematically dense D(n), n=0 forces the empty base, so the substantive version has n>=1. E.9.',
 'Both alternatives analyzed; photo inspected; no forced editorial choice for finite-type wording.')
reading(p1,'15','The coefficient bound i>=1|i>1 near the substitution argument.',
 'Every positive degree including i=1 needs denominator clearing; the constant term cannot be changed by dilation. E.9.',
 'Exact polynomial proof supports >=1; photo inspected.')
reading(p1,'16','Reference p.662|652 prime after the corollary.',
 'The theorem being discussed starts on652 verso, scans10--11;662 belongs to the later envelope construction.',
 'Strong structural cross-reference evidence; photograph inspected, not a final paleographic ruling.')
reading(p2,'25','The word metabelien as defined by the finite-index abelian-lattice construction.',
 'Here it means finitely generated virtually abelian, not modern derived-length2. E.12 and E.22 separate the categories.',
 'Definition explicit in checked transcription. No photograph of scan25 was supplied; this limitation is recorded.')
reading(p2,'29','nA (=|approximately equal)0; all residue characteristics divide n.',
 'Annihilation implies zero kernel points. Divisibility of residue characteristics does not imply nA=0 for that same n (Z/4,n=2); positivity of all residues does imply some integer annihilator. E.13.',
 'Proof and smallest elementary counterexample; photograph inspected.')
reading(p2,'29','If A has characteristic0 then E^1(A)=A.',
 'Correct for Q-algebras; false for A=Z, where coherent division sequences are all zero. E.13.',
 'Exact point-functor computation; photograph inspected.')
reading(p2,'31','Inverse-limit arrow under Hom in equation58.',
 'The correct object is colim_i Hom(G_i,G) for a finitely presented target; generator-and-relation proof supplied in E.14.',
 'Conclusive categorical correction; the photographed arrow points left.')
reading(p2,'32','G affine over S|S0 in the universal property.',
 'The proof covers closed linear finite-presentation targets over arbitrary rings. Neither broader affine reading is silently substituted; E.11 records missing linearization.',
 'Scope explicitly conditional for both readings; photo inspected.')
reading(p2,'33','Deleted hats on G0 and Z-lattice versus the surviving word profinis.',
 'Uncapped groups give the discrete extension; retaining hats gives its profinite completion. The two typed assertions are distinct. E.15,E.17.',
 'Strong internal typing evidence; photograph inspected; deletion interpretation not declared final.')
reading(p2,'34','Z|Zhat for points and for M tensor Z|Zhat, equation6.',
 'Lattice generators lie in M(Z) and map into M(Zhat); the discrete lattice is not its completion. E.17.',
 'Conclusive point-functor distinction; photo inspected.')
reading(p2,'35','Delta superscript in the comparison with G-hat, equation13.',
 'The finite-stage equality uses the common-component Delta subgroup; full Zhat-points permit independent local components. E.17.',
 'Exact product-ring proof and visible Delta; essential, not decorative notation.')
reading(p2,'36','Formula16: an automorphism is determined by its rho and sigma images; condition15(c) preserves the loop subgroup.',
 'False over Fp[eps]/eps^2: T(v)=v+eps(v^[p]-v) fixes all discrete elements and the loop line. A-linearity on the normal vector subgroup is a sufficient correction. E.25.',
 'Polynomial counterexample checked p2,3,5; photo36 and independent review of condition15(c).')
reading(p2,'37','Formula18: epsilon3(u) is well-defined from the orientation of a rho-conjugator.',
 'False overQ in this model: identity admits both1 and(-1/3,1/3)*tau as rho conjugators. Remembering that sign adds data. E.25.',
 'Exact rational vector/matrix check; photo37 inspected.')
reading(p3,'39','The displayed expansion of eta loses the inverse on sigma(beta0); zeta|xi letter.',
 'The typed formula is beta0-sigma(beta0) additively, as confirmed by27 and28. Changing the letter zeta to xi is harmless when its role is fixed. E.24.',
 'Conjugation identity and adjacent formulas support the inverse; photograph inspected.')
reading(p3,'40--41','Failure of epimorphism of the alpha,beta coefficient map at3 versus smoothness of the enlarged fine parameter scheme.',
 'The2x4 map has maximal-minor gcd3; adjoining nu-prime with coefficient2 makes gcd1. The fine scheme is an open A3 even at2,3. E.24.',
 'Explicit integral parametrization, minors and finite counts; both photographs inspected.')
reading(p3,'41','nu=2nu-prime +/-nu2 and zeta=(I-R)alpha +/-nu3 lambda1 in31.',
 'All four coherent choices tested. Source21 fixes +nu2; source28 and tau-conjugation give -nu3. Opposite nu3 sign makes that component empty at3, whereas tau has mu=-1 there. E.24.',
 'All alternatives computed p2,3,5; exact group identity supports convention; no final handwriting decision.')
reading(p3,'41','Middle -|= in32 and the corresponding +/-nu3 right side.',
 'The subtraction form follows31. Reading a chain of equalities fails for alpha=beta=e0 and nu=nu2=nu3=0: both sides before subtraction are(1,-1), not0.',
 'Explicit exact counterexample and inspected photograph; the equality-chain alternative is not equivalent.')

coverage=[
 {'task':'item5','outcome':'partly settled','statements':'E.1--E.14',
  'details':'Exact integrality assertions refuted and corrected; Q-linear, torsion-free integral, and all-ring positive-power theorems proved; envelope constructed with universal property for closed linear targets. E.11 records non-linear generality, executed tests, and first uncovered base-dimension-zero instances.'},
 {'task':'Lead3','outcome':'refuted','statements':'E.3--E.8; E.12--E.19',
  'details':'The source is virtually abelian, not arbitrary modern metabelian. Full pro-algebraic/Malcev and divided-power identifications fail. Correct maps, coordinate ring, universal property in its proved scope, rank1 separating examples and finite/nonfinite relative-completion comparisons supplied.'},
 {'task':'E.a','outcome':'partly settled','statements':'E.1--E.3; E.6; E.7; E.11',
  'details':'Q-algebra closed-linear theorem and exact torsion-free divided-power criterion proved; all-prime smooth Z/p^2 counterexamples and genuine integral rank5 example proved and computed. Remaining arbitrary non-linear targets specified in E.11.'},
 {'task':'E.b','outcome':'refuted','statements':'E.4--E.8',
  'details':'Actual and dropped-linear-term signed readings have exact rank3 and4 counterexamples.72 degree<=12 cases at2,3,5, rank5 genuine section, A|K and3!|6! alternatives, binomial-basis calculations executed. Added-integral-X rank4 theorem and sharp p^2 bound proved.'},
 {'task':'E.c','outcome':'partly settled','statements':'E.8--E.11',
  'details':'Positive-power theorem holds for every ring and closed linear finite-presentation target; affine dilation lemma proved under schematic density. Original arbitrary separated-lfp scope stays precise in E.11, with proved cases, computations and first uncovered base-dimension-zero tests.'},
 {'task':'E.d','outcome':'partly settled','statements':'E.12--E.14; E.18; E.19; E.11',
  'details':'Full integral envelope and linear-target universal property constructed. Maps to/from full pro-algebraic, Malcev, rank1 Hall/Lazard, divided-power and Hain finite/reductive relative examples proved; false identifications separated. Unrestricted target universality and unspecified general integral Hall/Lazard functors are not claimed.'},
 {'task':'E.e','outcome':'partly settled','statements':'E.15--E.20; E.24; E.25',
  'details':'Coordinate rings, all fibres, Zhat-points, discrete injection, order12/24 relative abelian-kernel completion computed. Fine signed parameter scheme and rational no-sign automorphism group proved. Integral generator-determination and sign-recovery assertions refuted. E.20 retains both the named signed comparison over the field F2 and the separate Fermat deck-quotient comparison beginning with free F_2 -> (Z/2)^2.'},
 {'task':'E.f','outcome':'proved','statements':'E.21; E.22',
  'details':'Independent proof for every nilpotent quotient, pro-p and rational unipotent completion; S3 permutation counterexample executed; modular envelope retains its S3 quotient. No claim that this establishes the author historical motivation.'},
 {'task':'E.g','outcome':'proved','statements':'E.18; E.23',
  'details':'RWZ/Toen theorems verified and reduced to B S; algebraic goodness proved through the finite-index lattice. Explicit induced12-dimensional representation separates full pro-algebraic from quasi-unipotent envelope on S itself.'},
 {'task':'AfterBISITE.Stallings','outcome':'proved','statements':'E.21; E.22',
  'details':'Mathematical lead proved independently; nilpotent/pro-p approximations miss the change in the S3 covering, while the modular envelope retains that quotient. Modern metabelian scope distinguished.'},
 {'task':'AfterBISITE.TwoRationalTheories','outcome':'proved','statements':'E.23',
  'details':'Discrete S, full P_Q(S), and the quasi-unipotent integral envelope compared on the requested example with exact maps and separating representation.'},
 {'task':'AfterBISITE.FermatRelativeCompletion','outcome':'partly settled','statements':'E.19; E.20; E.24; E.25',
  'details':'Proved case: order12/24 modular relative abelian-kernel completion is the finite stage; fine automorphism parameters, a generic identification and two counterexamples are supplied. General targets (Z/n)^2 and S3 x Zhat^* remain uncomputed. The first nontrivial finite deck test is q2: free F_2=<x,y> -> (Z/2)^2, x->(1,0), y->(0,1); comparison of its rational relative completion or abelian-kernel quotient with specified M/N, including the map, image and kernel, is absent. For S3 x Zhat^*, the tower source, continuous quotient map and proconstant or compatible finite-quotient completion category must be fixed. This is only the group-scheme half; no general tower identification is claimed.'}
]

for name,obj in [('E_results.json',results),('E_readings.json',readings),('E_coverage.json',coverage)]:
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print('Part E statement register:',len(results),'rows;',dict(Counter(x['status'] for x in results)))
print('Part E readings:',len(readings),'rows; no alternative silently declared final.')
print('Part E coverage:',len(coverage),'rows;',dict(Counter(x['outcome'] for x in coverage)))
print('Statement identifiers, statuses, and manuscript loci audited against sections/E.tex: PASS')
