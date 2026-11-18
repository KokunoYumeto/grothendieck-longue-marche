from pathlib import Path
import json

root = Path('/workspace/scratch/5cac7c575bd7')
out = root / 'work/configuration'
registry = json.loads((root/'work/notes/statement_registry.json').read_text())
who = 'GPT-6 Astra Pro; Pro mode; separate effort setting not exposed'
common = {
    'status': 'Proved',
    'check_date': '2026-11-18',
    'checker': who,
    'depends_on_doubtful_reading': 'None',
    'source_cotes': [{'cote': '149', 'scans': '35–36'}],
    'priority_claim': False,
}

new = {
 'A.61': {
   'working_id': 'A.61',
   'statement': 'For every pointed genus2 curve in characteristic different from3,19, the pro7 arithmetic action on the canonical first mod3 then mod19 deck group is trivial. Its nontrivial19-character orbit of lengthd has cohomology multiplicity2d, and pro7 order at most7^(1+floor(log7(2d))). Hence b2(7)<=3; a7^2 factor requires orbit length>=9 and a7^3 factor length>=27. On the A60 example1<=b2(7)<=3. Every cyclic3 then abelian19-power then arbitrarypro3 pointed tower has v7<=1. No actual49 or universal A12 classification is asserted.',
   'depends_on': ['A.4', 'A.59', 'A.60'],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'Proper smooth geometrically connected genus2 curve over finite k, rational point, p different from3,19. Canonical covers use full geometric mod-prime groups and descend pointed to the same k. Smaller-tower clause requires a geometric cyclic3 first cover, an abelian19-power cover of arbitrary rank/exponent, then a cover with3-group geometric Galois closure; all pointed over k.',
   'where_proved': 'configuration/A61_first_alternation_obstruction.tex',
   'notes': 'A4 proper prime-to-p comparison is used solely for the geometric deck formula H1=2trivial+2regular, derived inline from genus2 cellular chains; no Frobenius is lifted. A59 supplies tower/full induced topology; A60 supplies the elementary pro3 Frattini kernel and particular lower bound. Actual pro7 deck triviality, crossed-homomorphism19-kernel, explicit H2 averaging, splitting field with residueF3^18, little-group representation dimensions, multiplicity-space eigenvalue-order bound, and geometric core for cyclic3/abelian19/pro3 extension are proved inline. Complete root and finite_checks readings both PASS on2026-11-18. Same model family; no priority claim. This is a restricted arithmetic obstruction and finite-stage upper bound, not qualifying movement of the universal A12 gate.',
 },
 'A.60': {
   'working_id': 'A.60',
   'statement': 'For the pointed cyclic-19 Lang cover D of the genus-two F8 curve from A50, actual Frobenius on mod-3 cohomology has prime-to-3 order 56, whereas the base has order 4. Thus omitted v7 increases from 0 to 1 and v2 from 2 to 3. The second canonical alternating 3/19 level dominates D. Every further pointed pro-3 cover of D still has v7=1, and A56 gives the sharp bound 1 on the entire normal-3 by abelian-19 class. No unboundedness or A12 classification is asserted.',
   'depends_on': ['A.50', 'A.56', 'A.59'],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'The explicit smooth proper F8 curve y^2+x(x+1)y=x^5+1, rational point (0,1), and pointed constant cyclic-19 Lang cover proved in A50; Sigma={3,19}, coefficient prime3, omitted prime7 (also valuation2 computed). Further-cover assertion requires pointed geometrically connected finite etale covers over the same F8 with 3-group geometric Galois closure. A56 sharpness concerns only normal 3-group by abelian 19-group deck groups.',
   'where_proved': 'configuration/A60_frobenius_order_jump.tex',
   'notes': 'No new external theorem input: A50 supplies the actual geometric cover, point counts, and exact character polynomial 1+(3+S)T+8T^2; A59 supplies canonical-level and rational trace/congruence comparisons; A56 supplies its explicit restricted-class bound. Cyclotomic cubic, norm polynomial, irreducibility and exact root order modulo3 are proved by displayed finite identities. Finite pro-3 Frattini automorphism kernel is proved inline. Independent finite_checks certificate code/a50_cover19_order_jump.py/.json/.out was written before reading the author calculation, and A50 was reread to confirm the geometric premise. Complete finite_checks proof reading PASS, followed by targeted final A60.12 bound reading PASS, and complete root proof reading PASS on2026-11-18. Same model family; no priority claim; actual finite arithmetic progress, not universal A12 gate movement.',
 },
 'A.59': {
   'working_id': 'A.59',
   'statement': 'For a proper genus>=2 curve over a finite field with rational point and Sigma={r,s}, r invertible and s possibly the characteristic, the characteristic tower obtained by alternating full mod-r and mod-s geometric abelianization kernels is cofinal. Its pointed covers descend to the same field, and the omitted-t Frobenius orders on mod-r cohomology form a nondecreasing sequence whose supremum equals the all-cover order supremum. Each finite-stage order is determined exactly by the irreducible factors modulo r of the actual point-count Weil polynomial. No bound, unboundedness, or stopping criterion is asserted.',
   'depends_on': [],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'C proper smooth geometrically connected of genus>=2 over finite k with O rational; distinct r,s with r different from the characteristic, while s may equal it; omitted t outside {r,s}. Covers use the full geometric mod-prime quotient with its arithmetic action, not a rational class-field quotient. At s=p use the etale p-quotient only.',
   'where_proved': 'configuration/A59_alternating_tower.tex',
   'notes': 'External CF_Burnside1904 TheoremIII p392, primary five-page paper and proof opened in full; MilneJac Proposition9.1, Corollary9.6 and Theorem11.1. Cofinality, full induced Sigma topology, pointed descent, rational trace splitting, pro-r congruence argument and eigenvalue-order formula proved inline. A54/A57 identify the already-defined all-cover supremum and its arithmetic-kernel interpretation; they are contextual references, not premises of this independent tower/cohomology proof. A58 is mentioned only to separate arbitrary automorphisms from arithmetic realization. Complete second readings by root and finite_checks both PASS on2026-11-18; all readers are from the same model family. No priority claim and no universal A12 gate movement.',
 },
 'A.58': {
   'working_id': 'A.58',
   'statement': 'For every fixed pair of primes r,s and omitted prime t, two-generated finite {r,s}-groups of derived length at most three have IA automorphisms of arbitrarily high t-power order, also of that exact order in Out. They have elementary-abelian normal r-subgroup and metabelian s-quotient, and are geometric quotients of every genus>=2 curve when r,s differ from the characteristic. No lift of those automorphisms to the full surface group or realization by Frobenius is asserted.',
   'depends_on': ['A.4'],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'Distinct fixed r,s and t outside {r,s}; arbitrary prescribed exponent b>=1. The finite-group proof has no geometric premise. The geometric quotient corollary assumes genus>=2 and p outside {r,s}, and uses only the proper-curve comparison already proved in A4. The arbitrary automorphism is not claimed to be actual Frobenius.',
   'where_proved': 'configuration/A58_abstract_automorphism_obstruction.tex',
   'notes': 'All finite group and matrix assertions proved inline: S=(C_s)^d semidirect C_d, d=s^n; full matrix coefficient algebra; cyclic W=V^(d-1); two explicit generators; multiplicity IA group; extension-field matrix of exact t^b order; unchanged Out order. A4 is a direct dependency solely of the final characteristic-p geometric realization clause, not of the group construction. Independent finite_checks small certificate: code/two_prime_ia_small.py/.json/.out at r2,s3,F4,d3, group order331776 and IA order5; no full group enumeration claimed. Complete second readings by root and finite_checks both PASS on2026-11-18, all same model family. No priority claim; group-only obstruction does not change the universal A12 gate.',
 },
 'A.57': {
   'working_id': 'A.57',
   'statement': 'For every fixed ell different from p, every proper smooth genus>=2 curve over an algebraically closed characteristic-p field has a connected etale cyclic ell-power cover of positive p-rank. Consequently for every Sigma containing an invertible prime, including p-retained sets with base p-rank zero, the retained-p part of the finite-field outer arithmetic kernel is zero and the entire A54 all-cover kernel criterion and bounded-order collision consequence remain valid.',
   'depends_on': ['A.54'],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'Geometric cover statement: algebraically closed characteristic p, proper smooth genus>=2, any fixed ell!=p. Arithmetic statement: finite ground field, arbitrary Sigma containing r!=p; all G_k-stable pointed normal Sigma levels, after finite constants for a rational base point. Positive p-rank on one character orbit only; no claim that the whole primitive factor is ordinary.',
   'where_proved': 'configuration/A57_retained_p_detection.tex',
   'notes': 'External CF_Raynaud1982 Theorem4.1.1 and exact tensorized Frobenius sequence; complete source proof in4.2 opened. CF_Tamagawa2003 Lemma3.9(ii),(iii),Corollary3.10 and Remark3.11 supply the precise correction to Raynaud4.3.5/4.3.1; the already-written hyperplane proof satisfies it and no original numerical threshold is used. Uniform torsion intersection bound for all N, p-orbit length at ell2, same absolute-Frobenius bundle, Kummer cohomology orbit, and Artin–Schreier fixed-vector argument are explicit. Arithmetic orbit core is abelian-r and retains positive p-rank; outer-trivial p-factor acts through finite deck group on positive-rank Tp, contradicting faithful Zp action. A54 proof steps are checked individually for p-retained scope. Full author rereading plus complete independent second readings by root and finite_checks PASS completed2026-11-18, all same model family; cyclic r-power wording corrected. No priority claim; omitted-prime orders and full point classification remain unresolved.',
 },
 'A.56': {
   'working_id': 'A.56',
   'statement': 'For Sigma={r,s}, allowing either retained prime to equal p, every omitted-prime t-part of Frobenius on H1(D,F_r) is uniformly bounded as D ranges over pointed normal covers whose geometric deck group is an r-group by an abelian s-group. An explicit bound uses the base mod-s Frobenius order, a uniform cyclotomic residue-degree ratio, and bounded isotypic multiplicities. Consequently this restricted tower cannot establish the all-cover unboundedness criterion of A54.',
   'depends_on': [],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'C proper smooth geometrically connected genus>=2 over finite k with rational base point; r,s distinct and either may equal p; t omitted; only deck groups with normal r-Sylow and abelian s-quotient. At r=p use p-rank<=genus and the enlarged explicit M; at s=p the base etale Tate rank is f_C, possibly zero. All intermediate covers and base points descend to k. No assertion for arbitrary two-prime covers or the full exceptional image.',
   'where_proved': 'configuration/A56_restricted_tower_bound.tex',
   'notes': 'External CF_Milne2013 Theorem14.9 and MilneJac Proposition9.1/Corollary9.6. Explicit c_(r,s), including s=2, and e_t(r), including t=2, proved inline. Quotient genera and mod-r invariants bound every simple multiplicity without lifting or Chevalley–Weil. Killing bounded deck action gives field-linearity, then the pro-r Frattini automorphism kernel and normal-core topology extend the bound through arbitrary r-covers. A54/A57 supply interpretation only, not proof dependencies. Retained-p extension has a complete Artin–Schreier shortest-relation proof of the p-rank bound, modified multiplicity M, rank-zero convention, and pro-p finite-generation argument. Complete revised-proof readings by root and finite_checks both PASS on2026-11-18; same model family. No priority claim; side obstruction only.',
 },
 'A.55': {
   'working_id': 'A.55',
   'statement': 'For every finite prime set Sigma, allowing p, and every positive-genus smooth proper curve C over a finite field, the action of G_k on the product of the complementary Tate modules of J_C is injective. Thus no finite Sigma is J_C-large in the exact sense of Saidi–Tamagawa Definition2.6. This excludes every finite two-prime set from the large-set emptiness hypothesis but does not classify its exceptional image.',
   'depends_on': ['A.53'],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'C smooth proper geometrically connected of positive genus over Fq; Sigma finite, including empty or characteristic-containing sets. At p use the etale Tate module of geometric torsion. A53 primary-growth calculation is valid in every positive dimension; its curve point-count part is not used.',
   'where_proved': 'configuration/A55_finite_sigma_not_large.tex',
   'notes': 'External LA_ST2017 Definition2.6 and CF_MilneAV1986 Theorem19.1(b),(c). A hypothetical nonzero closed kernel contains t^b Z_t. Along degrees t^a the entire complementary-primary rational torsion stabilizes, contradicting A53 polynomial retained-primary growth and the exponential Weil lower bound. No assumption t in Sigma. Full author rereading and complete root second reading PASS completed2026-11-18; same model family. No priority claim; A12 remains open.',
 },
 'A.54': {
   'working_id': 'A.54',
   'statement': 'For nonempty Sigma excluding p, choose a rational base point and fixed r in Sigma. On all G_k-stable pointed proper Sigma covers D_N, let B_t be the supremum of v_t(order Frobenius on H1(D_Nbar,F_r)) for each omitted prime t. Then ker outer Frobenius action is exactly the product of t^(B_t)Z_t over omitted t, with infinity meaning zero. Any finite B_t gives a central arithmetic subgroup and infinitely many actual collisions, at every closed point of degree t^a with a>B_t. Outer faithfulness is not asserted to imply point separation.',
   'depends_on': [],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'C proper smooth geometrically connected genus>=2 over finite k of characteristic p; nonempty Sigma excludes p; r in Sigma fixed; a rational point O after finite constant extension if needed. D_N range over every G_k-stable normal open level of Delta^Sigma. At omitted t, t differs from r. The full retained-prime kernel formula is not claimed when p is retained with p-rank zero.',
   'where_proved': 'configuration/A54_frobenius_gate.tex',
   'notes': 'External MilneJac Proposition9.1, Corollary9.6, Theorem11.1; CF_Milne2013 Theorem14.9. Cofinality, induced Sigma topology, deck representation faithfulness via quotient genus and Q_r invariants, all-cover detection of based action, congruence pro-r kernel, and central arithmetic collisions proved inline. No centrelessness or finite-Frattini assumption. Original proof, fresh targeted author rereading, and full root second reading PASS completed2026-11-18; same model family. No priority claim; A28 remains Open.',
 },
 'A.53': {
   'working_id': 'A.53',
   'statement': 'For every finite prime set Sigma, allowing the characteristic prime, M_n=#J_C(F_(q^n))_Sigma is at most c n^(2g). For each P in C(F_(q^n)), the number of Q with [Q-P]_Sigma=0 differs from (q^n+1)/M_n by at most 2(g-1+1/M_n)q^(n/2). Hence every geometric point has infinitely many complementary-primary torsion partners, so B_C^Sigma is all C(kbar). This is an abelian candidate obstruction and does not prove full section collisions.',
   'depends_on': [],
   'answers_item': ['A12'],
   'hypotheses_and_where_they_hold': 'C smooth proper geometrically connected of genusg>=2 over Fq; Sigma finite, including empty and characteristic-containing sets; all n>=1; P rational over the individual F_(q^n). At p use the etale Tate module of rank f_J, not crystalline nonunit factors. A fixed geometric P is handled along multiples of its definition degree.',
   'where_proved': 'configuration/A53_finite_sigma_density.tex',
   'notes': 'External MilneJac Proposition9.1, including characteristic-prime proof in9.4–9.5 and subsequent Witt-vector paragraph; Theorem11.1 Weil bound. Lang isogeny, all-n primary determinant estimate, geometric-series valuation at2, exact Frobenius displacement, and proper-field obstruction are proved inline. No internal theorem dependency; A28 is a status boundary, not premise. Original derivation and root targeted second reading completed2026-11-18; no priority claim. Does not change A12/OpenA28.',
 },
 'A.45': {
   'working_id': 'A.DC1',
   'statement': 'For a product of smooth proper curves over an algebraically closed field, with a nonempty finite union of disjoint labelled graph sections removed and base genus at least one, every finite r-group fibre torsor extends after a finite étale base cover with r-group Galois closure; hence the fibre pro-r group injects into the total pro-r group.',
   'depends_on': [],
   'answers_item': ['G1(ii)', 'A4', 'A9', 'A10', 'A12', 'S4'],
   'hypotheses_and_where_they_hold': 'r is invertible in the algebraically closed ground field; C0 and S are smooth proper connected curves; g(S)>=1; m>=1 disjoint labelled sections in C0×S. In configuration applications S=Cprime is finite étale over a genus>=2 curve, so g(S)>=2, and m=|A|>=1. No requirement r∤m and no restriction on the characteristic part of the proper deck group.',
   'where_proved': 'configuration/direct_characteristic_p.tex; claim A.DC1',
   'notes': 'External keys CF_Milne2013 (12.7,14.1–14.2,14.9–14.10,16.7,17.10), CF_MilneAV1986 (8.2,8.4). Open-family base change is derived by localization; nonabelian torsor extension is proved by central induction. Neither Stix nor SGA XIII4.3–4.4 nor excluded specialization is used. Checked only in this writing; parent subsequently performed a targeted second reading.',
 },
 'A.46': {
   'working_id': 'A.DC2',
   'statement': 'For a product of smooth proper curves minus disjoint labelled sections, every connected finite tame Galois cover has normal geometric fibre image, and its quotient by that image comes from a finite étale base cover. Thus the tame configuration sequence is exact at its middle and right terms.',
   'depends_on': [],
   'answers_item': ['G1(ii)', 'A4', 'A9', 'A10', 'A12', 'S4'],
   'hypotheses_and_where_they_hold': 'The pair is smooth over an algebraically closed field with disjoint relative boundary sections; the finite total cover is tame along the boundary. Every finite relative cuspidally pro-r quotient is tame because r is invertible and diagonal inertia maps into its r-group cuspidal kernel.',
   'where_proved': 'configuration/direct_characteristic_p.tex; claim A.DC2',
   'notes': 'External key CF_SGA1: XIII5.2–5.3 gives local Kummer charts, X1.2 gives finite étale Stein factor. Source-proof chain checked through X3.6 and CF_SGA2 XIV1.11/X3.4. The commuting-action proof of normality is written here. A45 is used only to share notation, not as a theorem dependency. Checked only in this writing; parent subsequently performed a targeted second reading.',
 },
 'A.47': {
   'working_id': 'A.DC3',
   'statement': 'For a smooth proper curve of positive genus over an algebraically closed field and r invertible, actual tame r-adic inertia at one deleted point injects into the punctured pro-r group, and hence into every relative cuspidally pro-r quotient with r retained.',
   'depends_on': [],
   'answers_item': ['G1(ii)', 'A5', 'A12', 'S4'],
   'hypotheses_and_where_they_hold': 'C smooth proper connected, g(C)>=1, algebraically closed ground field, r different from its characteristic, P a geometric point. All configuration fibres have genus>=2.',
   'where_proved': 'configuration/direct_characteristic_p.tex; claim A.DC3',
   'notes': 'External keys CF_Milne2013 14.1–14.2 and CF_MilneAV1986 8.2/8.4; Kummer tower after a proper cyclic r-cover, with r-group conjugate compositum, detects unbounded inertia. No surface presentation. Checked only in this writing; parent subsequently performed a targeted second reading.',
 },
 'A.48': {
   'working_id': 'A.DC4',
   'statement': 'For a proper hyperbolic curve over a finite field and arbitrary retained Σ with r≠p, the relative configuration quotient has a common actual diagonal boundary extension by Z_r(1); its arithmetic fibres and cusps are the actual punctured groups and cusp groups, and geometrically conjugate proper sections yield cusp-preserving transport over the identity proper arithmetic group.',
   'depends_on': ['A.45', 'A.46', 'A.47'],
   'answers_item': ['G1(ii)', 'A5', 'A12', 'A14', 'S4'],
   'hypotheses_and_where_they_hold': 'C/k smooth proper geometrically connected, g>=2, k finite of characteristic p; Σ arbitrary with r in Σ and r!=p; whole G_k retained; compared punctures k-rational. After any finite constant extension the same hypotheses hold.',
   'where_proved': 'configuration/direct_characteristic_p.tex; claim A.DC4',
   'notes': 'External CF_SGA1 XIII5.2 plus finite étale descent. Root-stack wording is a derived chart-descent formulation, not a quotation from SGA. Finite stabilizer injectivity is not presumed. Completion right exactness is proved directly. The geometric fibre input is derived here by repeating the finite-core argument from A45,A46; there is no A13 dependency. A47 gives full actual inertia. Checked in this writing; parent subsequently performed a targeted second reading.',
 },
 'A.15': {
   'working_id': 'A.CR2 replacement',
   'statement': 'For arbitrary Σ containing r≠p, every open geometric level of the relative cuspidally pro-r quotient recovers the full geometric pro-r group of its actual compactification after killing its cusp inertia. The comparison respects arithmetic actions; cusp-preserving isomorphisms therefore preserve compactified Frobenius polynomials and all open-cover point counts.',
   'depends_on': ['A.14'],
   'answers_item': ['G1(i)', 'G1(iii)', 'A1', 'A3', 'A6', 'A12', 'K2'],
   'hypotheses_and_where_they_hold': 'Finite ground field k of characteristic p, C smooth proper geometrically connected, P rational, r in Σ and r!=p, Σ otherwise arbitrary. At an arithmetic level work over its actual finite field of constants. Every relative cover is tame at the cusp although proper deck groups may have p-parts.',
   'where_proved': 'configuration/A15_general.tex',
   'notes': 'External WeilCurves: Deligne1974 formula1.5.1 and Theorem1.6, opened in this writing. Full induced Σ topology is proved by explicit cores; A14 kills N in every finite r quotient, with no condition on open index. Boundary counts are recovered from actual decomposition double cosets and arithmetic indices. Also checked in this writing; replacement broadens the old p-prime statement to the range required by A49.',
 },
 'A.35': {
   'working_id': 'A.LIT2 replacement',
   'statement': registry['A.35']['source']['statement'],
   'depends_on': ['A.45', 'A.46'],
   'answers_item': ['A10', 'G1(iii)', 'A12', 'A14', 'S4'],
   'hypotheses_and_where_they_hold': 'Perfect k; smooth proper geometrically connected C of genus>=2; Σdagger comprises retained primes invertible in k and is nonempty; actual tame boundary convention with cuspidal kernel completed pro-Σdagger; proper Σ may contain characteristic p. Rational-point arithmetic assertions retain all G_k; finite closed marked sets split after a finite separable extension.',
   'where_proved': 'configuration/A35_repaired.tex',
   'notes': 'External keys CF_Milne2013 14.1–14.2,14.9–14.10; CF_MilneAV1986 8.2/8.4; CF_SGA1 XIII5.2. Uniform relative finite-core proof repeats A13 argument from A45–46 and works in characteristic0 as well. Primitive central inertia over arbitrary perfect fields is proved within A35, not imported from finite-field A42. Boundary right exactness and diagonal lifts prove second proper factor adds no coinvariant relation. Also checked in this writing.',
 },
}
for v in new.values():
    for key,value in common.items(): v.setdefault(key,value)

carried_deps = {
 'A.2': [], 'A.3': ['A.2'], 'A.4': ['A.3'],
 'A.5': ['A.3','A.4'], 'A.6': ['A.4'], 'A.7': ['A.4'],
 'A.8': ['A.3'], 'A.9': ['A.8'],
 'A.10': ['A.2','A.3','A.4','A.8','A.9'],
 'A.11': ['A.2','A.3','A.4'], 'A.12': ['A.7'],
 'A.13': ['A.45','A.46','A.48'],
}
dep_notes = {
 'A.2':'No internal theorem dependency. Magnus and finite-r automorphism arguments are supplied. S1 blind proof and line comparison completed.',
 'A.3':'Bellingeri Section2.1 supplies discrete fibre sequence; finite core/right exactness are in proof.',
 'A.4':'External CF_SGA1 III7.3–7.4, XIII2.9–2.11. This is retained as the separate specialization theorem, not used in the direct main-theorem route.',
 'A.5':'The assembled proof retains its original standalone topological argument: A3 gives retained fibre inertia and A4 gives characteristic-p specialization and the arithmetic setting. Thus actual direct deps are A3,A4. A48 supplies an independent stronger alternative, but is not silently substituted as this proof. External CF_SGA1 XIII5.2 gives local Kummer comparison.',
 'A.6':'A4 only for transfer of the finite complex test to characteristic2. External Bellingeri Theorem1.2 and actual finite certificate.',
 'A.7':'A4 only for characteristic2 specialization. Bellingeri Theorem1.2 and Schreier certificate supply the discrete obstruction.',
 'A.8':'As written it explicitly refers to the finite-quotient right-exactness argument in A3. This edge may be deleted if that already-stated universal-property argument is treated inline and the shorthand cross-reference is removed; no relative left-injectivity theorem is used.',
 'A.9':'Uses the normal-core topology argument supplied in A8, not its conclusion about passing to proper curve covers. All topological point-push and symplectic calculations are written in A9.',
 'A.10':'A3 is needed for the final relative-repair assertion in the statement. External CF_MT2008 Proposition2.2 only for total formation. A4 transfers the full-fibre classification only for p excluded.',
 'A.11':'This is the inherited simultaneously-liftable variant. The stronger direct constant-family proof follows from A45,A46 with the common-cover/core calculation repeated in A35; use those deps if replacing A11 by that stronger proof.',
 'A.12':'Uses A7 normalizer obstruction; A9 is mentioned only as the general mechanism corroborated by the finite test, not as a premise. External Bellingeri and actual finite certificate.',
 'A.13':'Preserve the full inherited statement. Geometric exactness, domination and the labelled constant-family variant use A45,A46 plus finite-core algebra written out. The boundary/arithmetic clause uses A48, whose proof independently derives its own geometric input from A45,A46 and A47, so there is no cycle. No A2,A3,A4,A5,Stix dependency in the replacement. A46 repairs omitted open-family middle exactness.',
}
carried = {}
for sid,deps in carried_deps.items():
    src=registry[sid]['source']
    carried[sid]={
      'depends_on':deps,
      'answers_item':src.get('answers (item or check item)','').split(';')+['G1(iii)'],
      'source_cotes':[{'cote':'149','scans':'35–36'}],
      'notes':dep_notes[sid],
      'check_date':'2026-11-18',
      'checker':who,
      'check_record':'Also checked in this writing; statement-specific outcome in configuration/CHECK_EVENTS.tsv. A2,A3 additionally have immutable blind proof and line-by-line comparison.',
    }

literature_metadata_file = out / 'literature_metadata.json'
if literature_metadata_file.exists():
    literature_metadata = json.loads(literature_metadata_file.read_text())
    carried.update(literature_metadata['corrected_carried_dependencies'])
else:
    literature_metadata = {}

payload={
 'new_and_replacement_statements':new,
 'corrected_carried_dependencies':carried,
 'assembly_instructions':[
   'Replace A15 with A15_general.tex and A35 with A35_repaired.tex.',
   'Map A.DC1–A.DC4 to A45–A48.',
   'Use the entire repaired A13 proof paragraph from direct_characteristic_p.tex, preserving the full inherited statement, including its boundary and arithmetic clause.',
   'The graph is acyclic: A48 derives geometric exactness directly from A45,A46 and uses A47 for inertia; A13 uses A45,A46 for its geometric clauses and A48 for its boundary/arithmetic clause.',
   'source_dependency_audit.tex is an unnumbered audit; its algebraic assertions are source statements or details of numbered A45–48/A35 proofs, not new result numbers.',
 ],
}
payload['assembly_instructions'].extend(literature_metadata.get('assembly_instructions', []))
payload['verified_reference_keys'] = literature_metadata.get('verified_reference_keys', {})
B_source_metadata_file = out / 'B_source_metadata.json'
if B_source_metadata_file.exists():
    B_source_metadata = json.loads(B_source_metadata_file.read_text())
    payload['verified_reference_keys'].update(B_source_metadata.get('verified_reference_keys', {}))
    payload['assembly_instructions'].extend(B_source_metadata.get('assembly_instructions', []))
A12_source_metadata_file = out / 'A12_source_metadata.json'
if A12_source_metadata_file.exists():
    A12_source_metadata = json.loads(A12_source_metadata_file.read_text())
    payload['verified_reference_keys'].update(A12_source_metadata.get('verified_reference_keys', {}))
    payload['assembly_instructions'].extend(A12_source_metadata.get('assembly_instructions', []))
(out/'configuration_metadata.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print('Wrote configuration_metadata.json:',len(new),'new/replacement rows;',len(carried),'corrected dependency rows.')
