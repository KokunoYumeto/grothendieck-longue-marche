#!/usr/bin/env python3
"""Rebuild the result ledger from the actual numbered statements.

Dependencies and scope notes are explicit audit data, not inferred proofs.
Unknown statement identifiers stop the update so a new result cannot be
silently given a generic dependency or task assignment.
"""
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
META={}
def add(ids,deps,answers,checks='',notes=''):
    for ident in ids.split(','):
        META[ident]=(deps,answers,checks,notes)

add('P.1','Opened primary sources listed in Part P','Task P.1',
    'EXIT_TOWER E.39–E.44 and E.49: scope compared',
    'Full/procongruence comparison maps and exact published theorem scopes are stated; no priority claim.')
add('A.1.1','Boggi–Zalesskii Theorem A(iii)=4.3(iii); goodness and virtual cohomological hypotheses checked','Task A.1; Lead 1; Lead 2',
    'Boggi–Zalesskii application in EXIT_TOWER E.44: confirmed',
    'Finite prime-power subgroup theorem used directly; the arbitrary closure-intersection step is not imported.')
add('A.1.2','A.1.1; finite-prime normalizer induction; genus-zero Birman sequences','Task A.1; Lead 2',
    'LM4_SUCCESSOR B.30/B.39: independently reproved',
    'Normalizer density plus the finite conjugation map proves the simultaneous centralizer equality for solvable subgroups.')
add('A.1','A.1.1; A.1.2; actual ten-point sphere quotient and two marked forgetful maps; Harbater–Schneps; HMM','Task A.1; Lead 1; Lead 2',
    'EXIT_TOWER E.44: repaired',
    'Full induced topologies, the two subgroup classes, and each source/target parameter are retained.')
add('A.2','Refereed R1; relative finite class-sum lifting; coprime complement lifting','Task A.2; Lead 6',
    'EXIT_TOWER E.46: confirmed on every dependency used by E.49; E.47: no unused global claim imported',
    'The noncanonical witness can be chosen as the refereed Phi0 with beta=1, signed A=5I, rho=0 and Delta=1.')
add('A.6.1','A.1; Hatcher–Lochak–Schneps moves; explicit B4 identities; E98 pentagon calculation','Task A.6; Task A.3; Lead 1',
    'EXIT_TOWER ordinary tower extension: checked and expanded',
    'The mixed six-move relation is the named conjugate of the actual five-point pentagon; full completions are used.')
add('A.3','A.1; A.2; A.6.1; finite-prime centralizer theorem; explicit determinant and label repairs','Task A.3; Task A.7; Lead 1',
    'EXIT_TOWER E.49: repaired',
    'The nine torsion-point labels and the common permutation of three nonzero branch labels are treated separately; exact R1 signs retained.')
add('A.7','A.3; R1 arithmetic vanishing and nonzero witness','Task A.7; Lead 1; Lead 6',
    'LM7_PUSH E.3 and DELTA_ON_GT A.84: decided',
    'Delta vanishes on full profinite GT for every multiplier. B.2.1–B.2.3 also prove strictness of GT inside ker Delta.')
add('A.4','A.4.1--A.4.48; A.4.50--A.4.51; executed finite-source, quaternion surface, joint normalizer, braid, capped630-factor, finite centralizer and fusion, ordinary-image census and explicit finite five-point coefficient comparison','Task A.4; Lead 1',
    'DELTA_ON_GT finite-shadow problem: remains unresolved',
    'The full common finite level and complete pentagon-shadow/parity census have not been obtained.')
add('A.4.1','A.7; compactness of GT0; continuity of the pentagon evaluation','Task A.4; Lead 1',
    'Infinite-only alternative: excluded for the actual compact system',
    'Proves existence of a finite separating level; does not identify or enumerate that level.')
add('A.4.2','R1; Bass–Serre relation module; finite homology computation; arithmetic inertia bound','Task A.4; Lead 1',
    'DELTA_ON_GT A.110: independently reconstructed',
    'Explicit characteristic source detector at every multiplier, with the stated enormous modulus and characteristic-core bound.')
add('A.4.3','Exact five-point presentation; actual 768-sheeted cover; Fourier chain complex; 114-dimensional homology action','Task A.4; Lead 1',
    'DELTA_ON_GT A.112 cubic centralizer ambiguity: excluded in an explicit finite quotient',
    'All twelve fixed residues are tested by exact affine linear elimination; only identity lifts, and the centralizer has order 3^40. The two-frame comparison remains open.')
add('A.4.4','Exact B4/Z4 presentation; Ferrari free kernel; Reidemeister–Schreier basis; faithful Artin representation','Task A.4; Lead 1',
    'Quartic modular embedding and peripheral word: computed exactly',
    'The marked embedding is an isomorphism onto the specified preimage; its sixth peripheral power has the displayed commutator orientation. A.4.5 gives the exact normal/mirror-core transport of the geometric marking.')
add('A.4.5','A.4.4; actual CM pullback; free-product normal forms; explicit braid mirror and normal-core maps','Task A.4; Lead 1',
    'Geometric marking transport on a common finite refinement: proved',
    'The actual inner marking and mirror are retained; a 48-factor diagonal injection gives the bound 24|R|^48. This does not complete the finite pentagon exclusion.')
add('A.4.6','Actual 576-sheeted Bass–Serre covering graph; exact homology action; all 18 affine centralizer fibres; signed modular projection; ordinary folding','Task A.4; Lead 1',
    'Final CM centralizer stabilization: effective finite quotient and complete residue census proved',
    'The projective homology cover has rank97; rank(r-1)=63, and only three of18 residues lift. An explicit invariant functional compresses the detecting module to96. The signed centralizer image is exactly C6, yielding a five-point quotient of order192*3^96. The finite nine-point naturality comparison remains open.')
add('A.4.7','Actual Bass–Serre covering graph; elementary abelian homology quotient; fixed-vertex boundary coefficients; cyclic lift to Z/p²','Task A.4; Lead 1',
    'Cyclic centralizer, normalizer and torsion-recognition steps: one explicit finite refinement proved',
    'For a specified quotient faithful on the finite factors, the homology cover has exactly the stated centralizer and normalizer images in that quotient. Every order-p element with nontrivial lower image is recognized there by a vertex-factor class. The three E.256 groups have explicit index bounds. Full rank-two translation-subgroup recognition remains open.')
add('A.5','A.5.1; A.5.2; A.7','Task A.5',
    'DELTA_ON_GT A.103: both vanishing assertions proved',
    'The harmonic square gives the first defect; the signed CM sum gives the second.')
add('A.5.1','A.1 first quotient square; exact harmonic re-marking; integral Schreier abelianization; R1 frame','Task A.5; Task B.1',
    'Harmonic primitive relation GF1: proved in the stated normalization',
    'No arithmetic coefficient convention is silently substituted for the frame-defined rho.')
add('A.5.2','A.5.1; A.7; exact affine F4 quotient and half-character computation','Task A.5',
    'DELTA_ON_GT A.103 individual defects: proved',
    'The kappa_d definition is used only on H5; its general-H replacement is explicitly named.')
add('A.5.3','Enriquez Theorem 8.1 and equation (50); actual finite-index Schreier subgroup and opening map','Task A.5; Task B.1; Task B.4',
    'Full profinite Kummer distribution: derived with the precise marking',
    'Every normalized Kummer descendant fixes full GT; positive and negative Schreier choices give the same actual map, and c_MN=c_M+c_N.')
add('A.6','A.1; A.6.1; full multitwist injection; Birman and finite categorical comparisons; BBR strictification','Task A.6; Lead 1',
    'EXIT_TOWER E.42/E.43 and missing E.29/E.32/E.33/E.35/E.38: repaired',
    'All endpoint groups use full profinite completion, including genus at least three; no inverse to the congruence quotient is presumed.')
add('A.8','A.1–A.7','Lead 1','Four referee points: proof comparisons repaired; finite census open',
    'The lead remains open as a complete task because its independent finite enumeration is still missing.')
add('A.9','A.1.1; A.1.2; A.1','Lead 2','Solvable centralizer assertion: proved',
    'The actual E.44 prime-power instance follows directly from the checked finite-prime theorem.')

add('B.1','B.1.1; B.1.2; B.1.3; B.1.7; B.1.8; B.2.5; A.5','Task B.1',
    'Literal §47 subgroup comparisons: partly refuted; one inclusion remains open',
    'The two marked descent operators are specified; an unproved remaining inclusion is kept open.')
add('B.1.1','Marked C2*C3 presentation; actual swap/inversion automorphisms','Task B.1',
    'DELTA_ON_GT descent conventions: independently checked',
    'Gives the exact conjugation relation between D_P and D_L.')
add('B.1.2','B.1.1; explicit rational degree-six cover; tangential arithmetic functoriality; degree-sixteen splitting field','Task B.1',
    'Literal GT subset C_P, C_P=GT and C_P=ker Delta: refuted',
    'The explicit actual Galois commutator is checked in the finite degree-sixteen Galois group; C_P intersect G_Q={1,c}.')
add('B.1.3','R1 relative lifting; explicit core word; compact finite-source lifting; B.1.1','Task B.1; Task B.2',
    'DELTA_ON_GT A.94/A.109 kernel construction: independently reconstructed',
    'An actual full kernel element has Delta=1; its nontrivial square has Delta=0 and belongs to neither fixed subgroup.')
add('B.1.7','A.1.1; actual cyclic sphere cover and universal-curve extension; HMM Corollary 2.8; A.5.3','Task B.1; Task B.4; Lead 5',
    'Genus-zero cyclic prime-power quotient parameter: determined',
    'The completed centralizer quotient has the original full GT parameter. The multiplier correction, named orbit representatives, and cover/opening square are explicit.')
add('B.1.8','B.1.7; A.5.1; exact equianharmonic quotient q_E; arithmetic multiplier stripping','Task B.1; Task B.2',
    'Physical and literal modular descent on full GT: determined',
    'D_L is the identity on GT and D_P(F)=cFc. The inner comparison is the explicit pure element x^(rho-t), so every Delta composed with a descent iterate vanishes on GT.')
add('B.2','B.2.1--B.2.31; A.7','Task B.2',
    'All quadratic annihilators determined as a countable-dimensional vector space; further finite-image census remains open',
    'Actual finite images through class ten over F11 and every finite coordinate set in a countably generated binary shift quotient are determined. The full annihilator has dimension aleph0 with an exact selected-basis isomorphism. Countably many explicit prime-indexed families and their descent iterates are jointly independent, and the full quotient V/D*V has dimension aleph0, excluding every finite set of descent generators. The common five-point census and explicit comparison at further mixed characteristic quotients remain unresolved.')
add('B.2.1','R1 full relative lifting; integral special derivation; exact sphere-Lie pentagon certificate','Task B.2; Task A.7',
    'Strict GT subset ker Delta: proved',
    'The weight-nine certificate is lifted to a genuine full gentle element before squaring to parity zero.')
add('B.2.2','B.2.1 lifting method; exact low-weight matrices; arithmetic beta-series formula; explicit Soulé Kummer residues','Task B.2; Task B.4',
    'Actual images in the named characteristic quotients: computed',
    'First separation occurs at class eight in this sequence. G_Q and GT images coincide through class ten; ker Delta and GT0 images coincide.')
add('B.2.3','B.2.2; integral weight-seven Lie polynomial; S4 group-algebra pentagon evaluation','Task B.2; Task A.7',
    'Smaller separating witness: checked',
    'Pentagon image is 160((34)-(12)); its reduction modulo eleven is nonzero and survives squaring.')
add('B.2.4','Finite Frattini automorphism kernels; actual pro-ell completion maps; arithmetic cyclotomic surjectivity','Task B.2; Task B.4',
    'Quadratic arithmetic annihilators detected by all odd-prime pronilpotent actions: proved zero',
    'The compact image and its exact scalar quotient are specified; additional annihilators require a different finite detection map.')
add('B.2.5','B.1.3; B.1.8; A.7; exact evaluation and restriction maps','Task B.1; Task B.2',
    'Descent on the full continuous quadratic annihilator: structural constraints proved',
    'Delta is independent of the image of D_P pullback; every descent iterate restricts to Delta on C_P. Nonvanishing of the first pullback is proved in B.2.8; the full image and later relations remain open.')
add('B.2.6','Marked finite source D; transfer and Hopf formula; actual central extension relations; exact GAP cohomology','Task B.2; Task B.1',
    'Canonical finite central obstruction and positive frame fibres: determined',
    'The finite stem kernel is H2(D,Z); o=a^3 b^2 is the exact cusp-fixed obstruction and f^c=f_tilde ab its unique correction. Prescribed pure residue conjugators are retained.')
add('B.2.7','B.2.6; refereed R1 D.50.5–D.50.16 with arbitrary normal kernel; compactness; exact inner normalization','Task B.2; Task B.1',
    'Finite canonical central-cover lift and full positive lift: equal images proved',
    'Every auxiliary central source factors through B/[B,K]. Exact epimorphism counts and compactness give an actual automorphism of the full profinite source, with prescribed two frame residues.')
add('B.2.8','B.2.5–B.2.7; exact full Schur-cover certificate; B.1.3; B.1.8; A.7','Task B.2; Task B.1',
    'Delta generates all quadratic annihilators: refuted by an actual full profinite element',
    'The full kernel is C2^3 x C3 and the cover has order 9393093476352. Candidate fourteen lifts to g with (Delta(g),Delta(D_P(g)))=(1,1); together with k it proves independence and failure of D_P preservation of ker Delta.')
add('B.3','R1 torsion classification; Lochak–Schneps Proposition 4(ii); LM4_SUCCESSOR A.39/A.42/A.81','Task B.3; Lead 4',
    'Direct E.44 application to GT involutions: exact missing realization identified',
    'No nonconjugate full GT involution or universal full GT conjugator has been produced.')
add('B.4','A.1; A.3; B.1; B.2.2; Part C','Task B.4; Lead 5',
    'Universal prime-power quotient and all-frame assertions: unresolved',
    'The checked named quotient comparisons and tested finite arithmetic images do not settle the universal assertion.')
add('B.4.1','B.1.7; classification of finite p-subgroups of PGL2(C); actual two-stage normalizer quotient map; HMM rigidity','Task B.4; Lead 5',
    'All genus-zero prime-power quotients with the stated branch markings: proved compatible with full GT',
    'The dihedral quotient is the composite u=z^N, w=u+u^(-1); characteristic rotation and Klein-four choices are accounted for. The universal higher-genus and all-frame assertions remain open.')
add('B.4.2','A.1; A.6.1; completed Birman–Hilden central quotient; HMM Corollary2.8; exact adjacent-twist subgroup and forgetful map','Task B.4; Lead 5',
    'The genus-two hyperelliptic quotient has exactly the original GT parameter',
    'The C2 kernel is the full profinite center. An exact test of15 pair vectors pins the label permutation to S3xS3; after its actual braid correction, forgetting complementary labels detects the same full GT parameter. Both the inner lift and the completion maps are retained.')
add('B.4.3','B.1.7; B.4.2; A.6.1 labelled sewing; actual two-stage quadratic cover and choice subgroups; exact Sp4(F3) detector','Task B.4',
    'The outer monodromy invariant of the degree-four two-step origami is constant on all full GT',
    'Both cyclic lifts retain the required names and their covariance witnesses compose inside the actual mixed domain. The remaining C2 discrepancy is a homomorphism and vanishes on both generators by the unipotent versus negative-unipotent trace test modulo3. This decides the specified outer invariant; the more tightly pinned tangential relation is not inferred from it.')
add('B.5','Exact 542-object/1620-arrow reconstruction; free-by-free five-point presentation; all 1080 relators','Task B.5',
    'EXIT_TOWER B.25: specified realization confirmed',
    'The actual pins and path choices are stated; original manuscript path identification is a separately recorded source-audit issue.')
add('B.5.1','B.5; exact change of generators and spanning-tree transport','Task B.5',
    'DELTA_ON_GT B.33: relation transport for specified path conventions proved',
    'The incidence graph alone does not fix the missing loop words; the required comparison is an explicit substitution.')
add('B.6','B.3','Lead 4','All-involution conjugacy assertion: open',
    'The E.44 finite-subgroup input has no constructed peripheral five-point realization for an arbitrary GT involution.')
add('B.7','B.4','Lead 5','Universal quotient/frame assertion: open',
    'No invariant separating G_Q from full profinite GT has been proved here.')

add('C.1','C.1.1–C.1.19','Task C.1; Lead 3','SECTIONS_OVER_Q limit assertion: open',
    'Every fixed ordinary pair has compatible compact lifting fibres; finite support from all-depth lifting remains undecided.')
add('C.1.18','Weibel IV.2.5, VI.4.3.1–2, VI.5.3; exact coefficient transition maps; tame K2 sequence','Task C.1; Task C.2',
    'Continuous global weight-two first cohomology: determined exactly',
    'H1(GQ,Zhat(2)) is Z/24, generated by (chi^2-1)/24; eight classes at two, three at three, zero at larger primes.')
add('C.1.19','C.1.12; C.1.18; vanishing of global weight-one invariants','Task C.1; Task C.2',
    'Full geometric-conjugacy fibre of class-two sections: determined exactly',
    'Every ordinary pair has precisely 24 pronilpotent class-two section classes; pro-ell fibre is singleton for ell>=5.')
add('C.1.20','C.1.11; C.1.15; C.1.18; original A.44 local invariant; exact integral primitive comparison; coefficient-five restricted-ramification cohomology','Task C.1; Task C.2; Task C.3',
    'A finite coefficient-five class-two prefix is fixed before the second prime choice',
    'Rational placeholders fix the integral local primitives modulo5 at q0,r0. Every continuation with the displayed principal-unit tails has the same actual H5 semidirect C4 quotient of order500, up to central conjugacy. Its maximal abelian subfield is Q(mu5).')
add('C.1.1','Actual local ordinary equalities; prime valuations and completed Kummer maps','Task C.1; Lead 3',
    'SECTIONS_OVER_Q A.32: confirmed',
    'Finite support of either coordinate or their ratio already gives the rational-point reconstruction.')
add('C.1.2','C.1.1; ordinary local valuation patterns','Task C.1; Task C.2',
    'Fixed finite-ramification reduction: limitation proved',
    'An infinite-support ordinary pair has unbounded ramification support at every coefficient prime.')
add('C.1.3','Tame inertia weights; finite ramification outside ell; finite-coefficient global cohomology','Task C.1',
    'Higher-weight cocycle compactness: proved',
    'Applies to weights at least two; the abelian coordinate is fixed separately.')
add('C.1.4','Integral Hall collection and actual free nilpotent pro-ell quotients','Task C.1; Task C.2',
    'Integral nilpotent model: checked',
    'All coefficient primes, including two and three, are retained.')
add('C.1.5','C.1.3; noetherian closed submodules; finite polynomial family','Task C.1',
    'Primitive-family compactness: proved',
    'The finite polynomial parameters and actual integral cochains are retained.')
add('C.1.6','C.1.3; C.1.4; C.1.5','Task C.1',
    'Fixed-abelian-cocycle section fibres: compactness proved',
    'This compactness concerns one specified pair, with the exact forgetful maps.')
add('C.1.7','C.1.6; compact inverse-limit finite intersection argument','Task C.1; Lead 3',
    'All-depth compatibility for one fixed pair: proved',
    'Nonempty lifts at every integral nilpotent class yield one compatible pronilpotent section for that same pair.')
add('C.1.8','Integral Milnor sequence; Poitou–Tate duality; K22(Z) at 691; local duality','Task C.1',
    'Vanishing of arbitrary integral localization kernels: refuted',
    'A Z/691 class is nonzero globally, locally zero everywhere, and zero in every finite coefficient reduction.')
add('C.1.9','C.1.8; continuous two-cocycle extension construction','Task C.1',
    'Finite coefficient splitting implies continuous splitting: refuted',
    'The displayed profinite extension is genuine; no unsupported identification with a curve-fundamental-group quotient is made.')
add('C.1.10','Milnor exact sequence; finite-coefficient local-global injectivity; explicit residue tower','Task C.1',
    'Integral localization kernel: computed',
    'At ell=3 and weight two it contains an uncountable product/c0 quotient.')
add('C.1.11','Ordinary tame symbols; K2(Z); explicit local primitive; finite residue surjectivity; compact primitive fibres','Task C.1; Task C.2',
    'Ordinary continuous cup obstruction: proved zero',
    'Includes ell=2 and the real place, with a compatible integral primitive.')
add('C.1.12','C.1.11; explicit integral class-two section coordinates','Task C.1; Task C.2',
    'Every ordinary completed pair: unrestricted global class-two lift proved',
    'Local matching is a separate restriction of the actual section space; the C.2.2 obstruction applies there.')
add('C.1.13','Coefficient-compatible supports triangle; derived inverse limit; real-place H3 comparison; K4(Z)=0','Task C.1; Task C.2',
    'SECTIONS_OVER_Q A.65.8 and A.46.2 strict localization: repaired',
    'The image dR is literal, not its closure; in weight three the global obstruction is exactly the stated c0/dc0 quotient.')
add('C.1.14','C.1.13; actual tame cocycle extension; Frobenius-inertia relator','Task C.1; Task C.2',
    'Strict residue cochain comparison: proved',
    'The q inverse factor and the subcomplex on which the formula is defined are explicit.')
add('C.1.15','C.1.13; C.1.14; exact Hall cochains; symbolic residue verification','Task C.1; Task C.2',
    'SECTIONS_OVER_Q A.43.1/A.46.5–6 class-three residue formulas: confirmed with exact comparison',
    'Two divided residue families must be integral and tend to zero; the test concerns a specified actual class-two section.')
add('C.1.16','Integral cyclic-word sums; finite ell-group augmentation ideals; compact conjugator fibres','Task C.1; Task C.2',
    'Rational Magnus-to-pro-ell conjugacy comparison: proved',
    'The rational formal conjugator is never evaluated in an integral finite group algebra.')
add('C.1.17','C.1.16; Frobenius weights; rational Hall corrections; integral peripheral centralizer','Task C.1; Task C.2',
    'All-depth local boundary matching: proved',
    'At q distinct from ell with nonzero ordinary valuation, the abelian section fibre is the singleton local point-section class.')
add('C.2','C.2.1–C.2.8; C.1.12; C.1.15; C.1.17','Task C.2',
    'Universal first-exclusion reading of SECTIONS_OVER_Q: unresolved',
    'The fixed-level witnesses vary with the level; absence of every all-depth ghost has not been proved.')
add('C.2.1','Exact factorial exponents in supplied A.65 construction','Task C.2',
    'SECTIONS_OVER_Q A.65 limiting family: checked',
    'The displayed sequence converges to the rational pair (3,-2); this fact does not decide every possible family.')
add('C.2.2','Explicit modified A.44 pair; genus-two cover; exact two-descent; finite residue check at 1129','Task C.2; Task C.3',
    'SECTIONS_OVER_Q A.207/A.209 local-matching exclusion: reconstructed',
    'First local-matching exclusion is class two for the specified witness; unrestricted class-two global lifting follows from C.1.12.')
add('C.2.3','Actual displayed A.196 coordinates; exact local finite ring computation','Task C.2',
    'SECTIONS_OVER_Q A.196 application to ordinary pairs over Q: refuted',
    'The displayed pair is over Q(cuberoot(3)) and already fails its required ordinary/cuspidal local test.')
add('C.2.4','C.1.15; valuation-zero Kummer coordinates at 1129; unramified pro-ell action; local duality','Task C.2',
    'Using the 1129 local-matching failure as an unrestricted class-three obstruction: excluded',
    'Every global class-two section of this witness has zero local class-three obstruction there; full local lifts exist for ell distinct from 1129.')
add('C.2.5','C.1.12; C.1.15; C.1.18; explicit point-three Heisenberg cover; Kummer intersections; Chebotarev; A.44 recursion','Task C.2; Task C.3',
    'Modified factorial ordinary ghosts: first unrestricted integral obstruction determined',
    'Exponents 5(j+4)! yield a recursively specified ordinary pair for which every integral class-two section has a nonzero class-three obstruction at q0 in coefficient prime five, detected modulo 25. The explicit smaller-modulus prime is a separate verification example.')
add('C.2.6','C.2.5 cover argument; explicit H3 arithmetic descent; C.1.18; K2(Z) at three; A.44 original recursion','Task C.2; Task C.3',
    'An original-exponent A.44 prime choice: first unrestricted integral failure is class three',
    'The exact prime test kills all three global central choices modulo three; the nonzero obstruction is detected modulo nine. This determines the selected recursive family, not every A.44 prime choice.')
add('C.2.7','C.1.20; C.3.5; C.3.10; exact Heisenberg/radical/cyclotomic fibre products; C.1.15 residue formula; original A.44 recursion','Task C.2; Task C.3',
    'An original family passing every compact elliptic test first fails integral lifting at class three',
    'At the second support prime q1, exponent120 and a nonzero central coefficient-five Frobenius give valuation-one obstruction modulo25 for every integral class-two lift. The family has full affine-cover abelian quotient sections and retains all original factorial exponents.')
add('C.2.8','C.1.20; C.2.7; C.3.10; original A.44 local invariant and CRT recursion; exact coefficient-prime Heisenberg fibre products; C.1.15; C.3.11','Task C.2; Task C.3',
    'Every finite original A.44 prefix admits a continuation first excluded at unrestricted integral class three',
    'The same prefix-surjectivity holds in the entire compact-test-passing subspace. Choose a new coefficient prime ell, retain original factorial exponents, freeze every old integral local primitive, and impose a nonzero central Frobenius at q_(ell-4). The exact residue is nonzero modulo ell squared. All constructed compact-passing pairs have abelian cover sections and no metabelian cover lifts. Density does not assert universal exclusion.')
add('A.4.8','Literal degree-nine torus cover and Schreier basis; integral deck matrices; actual pointpush generators; complete finite linear census modulo three and nine','Task A.4; Lead 1',
    'Translation centralizer residues: exact finite homological stabilization to the geometric image',
    'All81 pure homological centralizer residues modulo three are tested. Exactly27 lift symplectically modulo nine, and they equal the actual level-three normalizer image. The upstairs forgetting lattice3Lambda and the degree-nine covering inclusion are typed separately. The larger centralizer has order3^7; no full conjugacy or common pentagon census is inferred.')
add('C.3','Exact fixed-finite-quotient A.72 construction; common finite refinements; C.2.2','Task C.3; Lead 6',
    'One fixed finite quotient excludes every A.72 ghost: refuted; full target question open',
    'No uniform full cover/configuration/modular target, or theorem excluding all such targets, has been obtained.')
add('C.3.1','C.2.6; C.1.17; actual pointed H3 cover; exact cubic and isogeny maps; Milne II.1.5–1.8','Task C.3; Task C.2; Lead 6',
    'An explicit open elliptic cover target excludes the selected original-factorial examples',
    'The pointed degree-27 cover is y^2=x^3+9 minus 27 boundary points, with its exact map to U. The two other mod-three section classes fail at two; a fixed-coset obstruction excludes the remaining cover at q0. Compactification kills inertia that survives pushforward, so no unsupported compact-target conclusion is drawn.')
add('C.3.2','C.3.1 explicit dual three-isogenies; exact Kummer torsor; local calculation at two; Kronecker–Weber; Mordell–Weil','Task C.3; Task C.2',
    'The elliptic target: both three-isogeny Selmer groups and all three-primary Sha determined',
    'Sel_phi=0, Sel_psi=<6,12>; both three-primary Sha groups vanish; Eprime(Q) has rank one and its three-completion is Z3 P0 plus C3 T.')
add('C.3.3','C.3.2; exact inverse Kummer sequence; Milne ADT I.3.3–3.5 and I.6.26(b)','Task C.3; Task C.1',
    'Absolute continuous H1(GQ,T3 Eprime): determined',
    'Every compatible Weil–Chatelet tower vanishes at all primes away from three; global reciprocity and the finite-index closure of P0 also kill it at three. No fixed ramification set is imposed.')
add('C.3.4','C.3.1–C.3.3; C.1.17; exact translated isogeny; reduction at every actual support prime','Task C.3; Task C.2',
    'All original A.44 outputs: universal necessary support-prime point-order tests proved',
    'A full pro-three section requires (-2,1) to have order prime to three at every q_j and (3,-6) at every r_j. The quantified containment retains the pointed open-cover map.')
add('C.3.5','C.3.4; exact A.44 cyclotomic/radical fields; cube-class intersection; Chebotarev; CM endomorphism and explicit isogeny Kummer map','Task C.3; Task C.2',
    'Original-factorial outputs satisfying every compact elliptic test: constructed',
    'Add noncubic 3 at q_j and noncubic 2 at r_j, retaining every original recursive condition. The finite elliptic three-primary group is C3 and the required points have prime-to-three order. No all-depth section is asserted.')
add('C.3.6','C.3.1; C.3.2; actual local isogeny fibre and three-primary torsion at two','Task C.3; Task C.2',
    'Compact local fibre at two: all three classes realized',
    'Every original A.44 ordinary local point lifts to three points of Y(Q2), whose compact Kummer classes fill Eprime(Q2)^completion3. No further compact coefficient restriction is imposed there.')
add('C.3.7','C.3.1–C.3.3; generalized Picard exact sequence; semiabelian Albanese comparison; Shapiro and Kummer theory; exact boundary norm characters','Task C.3; Task C.2; Lead 6',
    'The full affine-cover geometric abelianization: exact three-adic coordinate image determined',
    'The actual quotient pi1(Y)/[K,K] has kernel TJac(Eprime,D) and rational splitting. Its three-adic coordinate image is the displayed completed norm formula. At every coefficient prime, the block-constant torus map constructs quotient sections for all pairs (3C^27,-2D^27), including scaled ordinary infinite-support pairs; no full section through the retained commutator kernel is asserted.')
add('C.3.8','C.3.1; C.3.7; exact Heisenberg arithmetic coset actions; central-extension relator calculation; Macedo–Newton Theorems 2.1–2.3 and Definition 2.5','Task C.3; Task C.2',
    'Boundary-field Hasse norm and weak-approximation obstructions: zero',
    'Each degree-nine boundary field has normal-closure group H3 semidirect C2 and stabilizer S3. H3(G,Z)=0 and the sign restriction is surjective, giving H2(G,X)=0 for its norm-one character module. The full normalized bar calculation was independently rerun.')
add('C.3.9','C.3.5; C.3.7; C.3.8; original A.44 Hensel and CRT estimates; translated multiplication-by-three boundary fibres; local norms at every place','Task C.3; Task C.2; Lead 6',
    'Original unscaled factorial ghosts surviving the full affine-cover abelian quotient: constructed',
    'Retaining the original exponents, choose both prime sequences congruent to one modulo27 with the stated noncube conditions. Actual global norm preimages give convergent toric cocycles at three, and the block-constant map treats every other coefficient prime. Their product is a full profinite section of the displayed quotient with proper class zero. The retained commutator-kernel lifting problem remains open.')
add('C.3.10','C.3.4; C.3.5; C.3.8; C.3.9; exact local boundary Galois action; Milne ADT Corollary I.2.4','Task C.3; Task C.2; Lead 6',
    'Every original A.44 output passing the compact elliptic tests survives the full affine-cover abelian quotient',
    'At three each boundary algebra is a degree-nine field with full decomposition group H3 semidirect C2. Its norm-one character lattice has H1 zero, so local torus duality proves actual norm surjectivity. The Hasse norm argument and convergent products apply to every compact-passing original output without additional congruences. The nonabelian lifting problem remains open.')
add('C.3.11','C.2.7; C.3.10; exact inclusion of the second derived subgroup of the cover kernel into Gamma4 of the original geometric group','Task C.3; Task C.2; Lead 6',
    'All affine-cover abelian sections above the selected family fail to lift through its metabelian cover quotient',
    'The actual arithmetic map pi1(Y)/Ksecondderived -> pi1(U)/Gamma4 preserves both Kummer coordinates. The latter section fibre is empty while the former abelian fibre is nonempty. This excludes every choice of abelian section above this one specified original family.')
add('C.4','C.1; C.1.1; C.1.7','Lead 3','All-depth survival implies finite support: open',
    'The exact compatible-section meaning is fixed; the further arithmetic implication remains unresolved.')
add('C.5','A.2; A.3; C.2.2; C.3','Lead 6','Uniform rigid-target analogy: partly settled, open overall',
    'The exact GT witness obstruction is proved; a uniform section-ghost exclusion has not been proved.')

add('B.2.9','B.2.7; B.2.8 normalization; R1 finite normal-kernel epimorphism counts; canonical source central covers; actual six-conjugate pants source; compactness','Task B.2; Task B.1',
    'The full descent image: exact finite canonical-cover descriptions proved',
    'For every characteristic target Q, both the actual gentle image and the actual descent image are images of explicit finite framed automorphism groups. Their inverse-image intersection equals D_P(H); the full image is G_Q D_P(H). The raw target frame freedoms obey a=l=−u modulo3. Equality of both finite images at all levels, and surjectivity of D_P, remain unresolved.')
add('A.4.9','A.4.8 literal surface basis; characteristic Zassenhaus quotient; integral commutator collection at three; exact tensor matrices; 244 actual geometric IA words; explicit reflection','Task A.4; Lead 1',
    'The nine-point degree-three peripheral lift: complete actual geometric image in the class-two quotient',
    'The characteristic group has order3^395 and retains ten cubic power directions. Killing the peripheral third-layer span gives order3^91. A rank26 obstruction on the117-dimensional peripheral outer IA space has kernel equal to the91-dimensional span of actual mapping-class words. Both signs are realized explicitly. The entire finite image has order48 times3^107 and removes all six earlier relative conjugacy directions. The common pentagon source comparison remains to be constructed.')
add('B.2.10','B.2.9 actual six-conjugate source maps; exact kernel-image table; spherical triangle presentations; Goursat comparison; central transfer and iterated relative commutators','Task B.2; Task B.1',
    'Simultaneous six-word membership and commutator-word membership reduce to fixed finite quotients',
    'The joint image in B^6 contains L3^6 and its derived subgroup contains L4^6, for the explicitly defined open iterated relative commutators. This proves exact inverse-image formulas for both word images independently of every later finite target. Positive framed automorphism lifting is a separate remaining condition.')
add('B.2.11','B.2.10; exact marked central product of SL2(F3) and Dic3; complete H2 spaces at two and three and their source restrictions; canonical central-cover transfer','Task B.2; Task B.1',
    'The fixed six-word membership quotient and its full marked canonical cover: exactly determined',
    'All five relative-commutator quotients equal the marked group of order144, whose next canonical central kernel is zero. The actual six-coordinate image has order1990656, derived order13824 and abelianizationC12 squared. Complete PC presentations, cohomology cocycles, source restriction vectors and actual generators are retained. This still proves word membership rather than the remaining positive automorphism lift.')
add('C.1.21','C.1.15; C.1.18; original factorial exponents; literal integral Kummer sums; exact tame relations and division by p−1 before reduction','Task C.1; Task C.2',
    'Finite determination of every fixed class-two coefficient quotient for original A.44 outputs',
    'For ell>=5 and exponentN, an explicit finite prefix using D=N+max v_ell(p−1) fixes the coefficient-ell^N class-two section class of every continuation. Its proof compares actual continuous cocycles and their local integral primitives, then kills the unramified central difference by the checked weight-two cohomology.')
add('C.2.9','C.1.21; C.2.8; C.1.19; exact Hall reduction through class three for ell>=5; C.3.10; C.3.11','Task C.2; Task C.3',
    'Finite local class-three failures form an open dense subset of original A.44 outputs and of the compact-passing subspace',
    'Every finite legal prefix has a finite extension forcing class-three exclusion for every ordinary continuation. The proof retains geometric conjugacy invariance of the finite obstruction through the actual central extension. The residual set is closed with empty interior; its emptiness and all higher lifting conditions remain unresolved.')
add('C.2.10','Exact restricted power series; coefficient valuations; contraction on each p-adic shell; integral exponential and logarithm','Task C.2; Task C.1',
    'SECTIONS A.66 missing coefficient-prime image lemma: reconstructed',
    'For the literal exponent C n product_(r=2)^d(z^r−1), an explicitly specified input shell maps bijectively to the stated full multiplicative coset. Exact exponent valuations and congruence preservation are proved, including the dyadic shell. Finite certificates check32 exact local permutations and2867 valuations; the proof treats every allowed parameter.')
add('C.2.11','C.2.10; three actual radical fields; exact maximal abelian subfields; triangular CRT; Chebotarev fibre products; finite-field Jacobi bounds; completed Kummer limits','Task C.2; Task C.1; Task C.3',
    'SECTIONS A.66 ordinary variable-exponent construction: reconstructed with full arithmetic proof',
    'The three disjoint prime sequences have the literal stated tame-denominator exponents and satisfy all ordinary local conditions. Every fresh-prime gcd equals the previous factorial, all simultaneous CRT/radical classes are compatible, and the pair is a prescribed C-th power perturbation of point3 with infinite support. The arithmetic certificate checks705 finite-field image cases; no enormous complete prime search is represented as executed.')
add('C.2.12','C.2.11; C.1.4; C.1.13; C.1.14; actual Magnus congruence quotient; Weibel IV1.18/6.9 and VI8.2/9.11; exact tame Hall ideal bounds; integral Bockstein correction','Task C.2; Task C.1; Task C.3; Lead 3; Lead 6',
    'SECTIONS A.65 fixed-depth ordinary infinite-support section construction: certified with the missing arithmetic input reconstructed',
    'For each fixed nilpotent classR and coefficient modulusN, an ordinary infinite-support pair has an actual full profinite classR section agreeing with point3 in the specified finite Magnus quotient. The proof retains all coefficient primes, the dyadic real term, the literal strict-localization convergence condition and the finite congruence at every induction step. The pair and section may depend onR,N; no one fixed all-depth pair is asserted.')

add('B.2.12','B.2.10--B.2.11; exact order144 target; exhaustive normalized positive-frame census; actual joint derived subgroup membership','Task B.2; Task B.1',
    'Every normalized full target has a simultaneous six-word preimage in the full source commutator subgroup',
    'All24 normalized target frame triples are enumerated. Exactly one of the two allowed harmonic exponents passes for each triple. The exact full joint-image equality then produces an actual profinite commutator word with all six prescribed evaluations. Full source cycle relations and positive automorphism lifting remain to be established.')

add('B.2.13','B.2.10--B.2.12; exact six-coordinate Schreier action; exhaustive finite positive-frame census; explicit conjugator recursion on freely permuted factors','Task B.2; Task B.1',
    'Every normalized target has an actual positive automorphism lift to the universal six-coordinate source quotient',
    'The proposed source generator images satisfy both cycles literally. The induced action on the pure subgroup is the restriction of six target automorphisms; finite index proves surjectivity. All24 finite positive frames lift by explicit coordinate equations in the direct-product kernel. The canonical central-cover lifting problems required for a full source automorphism remain unresolved.')

add('A.4.10','A.4.6; literal Artin action and pure inner maps; two regular homology covers; characteristic permutation core; exact multiplication-by-two and multiplication-by-three covering square','Task A.4; Lead 1(2)',
    'The decisive signed modular centralizer detector is realized by an explicit characteristic surface quotient with a common two-/three-division cover',
    'The finite quotient of the four-punctured torus and the characteristic once-punctured-torus quotient have literal modular-image surjections onto D+. Every nonpure residue, pure inner kernel and signed central residue is checked. The common six-division square retains the exact based covering maps and all subgroup indices. The remaining geometric straightening and complete five-point shadow census are unresolved.')
add('B.2.14','B.2.9; B.2.13; exact commutator-kernel comparison; cofinal characteristic quotients; compact positive framed automorphism space','Task B.2; Task B.1',
    'The central-cover image criterion extends to the actual infinite universal quotient',
    'The full positive source image equals the image from U^c, retaining both prescribed U-frame values. The exact map to every finite canonical cover is proved, then compactness gives one full lift. No surjectivity onto all positive automorphisms of U is asserted.')
add('B.2.15','B.2.10--B.2.14; exact S3 and A4 pair-common quotients; signed tensor coinvariants; finite-presentation homology; transfer; explicit completion comparison','Task B.2; Task B.1',
    'The actual central kernel over U is finite and annihilated by 2^14 times3^6',
    'The two exceptional matching lines have stabilizer eigenvalue minus one, so the discrete rational second homology vanishes. Integral transfer supplies the annihilator, and the actual profinite kernel is a quotient of the resulting finite discrete kernel. Root independently reconstructed both permutation representations and signed tensor calculations.')
add('B.2.16','B.2.13--B.2.15; exact central cusp defect; continuous explicit positive frames; source commutator normalization','Task B.2; Task B.1',
    'The physical descent image is an open subgroup of finite index',
    'Positive U-frames lift to an actual automorphism of U^c whose cusp error is a specified element of the finite central kernel. The error vanishes on an open identity neighborhood. The exact central-cover criterion supplies full source lifts there, proving openness of D_P(H) and of the full descent image. The index remains uncomputed.')
add('B.2.17','B.2.14--B.2.15; free factor sections; central bilinear commutators; exact free class-two exponent2m quotient; actual characteristic core','Task B.2; Task B.1',
    'An explicit finite canonical source cover retains the whole central cusp kernel',
    'The map from U^c to R_*^c is injective on M. The target has order2^4579 times3^1952 and the induced source order2^27464 times3^11706; the characteristic refinement is specified literally. These groups were not enumerated, and the complete positive-frame census remains open.')
add('C.2.13','C.2.11--C.2.12; C.1.17; C.1.20; exact marked Heisenberg cover; compatible radical/cyclotomic fibre product; fixed-pair compactness','Task C.2; Task C.3; Task C.1; Lead 3; Lead 6',
    'Selected fixed-depth ghosts have finite first failures arbitrarily far out and share one degree125 cover exclusion',
    'For every R,N, the fixed-depth construction admits a selected pair surviving classR but failing some later finite integral class. The same tangentially marked H5 cover splits at the ordinary local point and has nonzero central point-three Frobenius, proving full pro-five exclusion. The point-three twist is one fixed geometric degree125 target for this selected family. All outputs of A.65 are not classified.')
add('C.2.14','C.1.4; exact class-three Hall and BCH laws; ordered group-algebra basis; terminating weighted collection','Task C.2; Task C.1',
    'The augmentation ideal of the five-coordinate class-three exponent-M group has an explicit nilpotence bound',
    'For p>=5 and M=p^a, the group has orderM^5 and its Fp augmentation ideal satisfies I^(1+10(M−1))=0. The five ordered variables have weights1,1,2,3,3, and the proof gives exact collection identities and a terminating weight-preserving procedure.')
add('C.2.15','C.2.14; C.1.16--C.1.17; actual tangential Frobenius action; integral cyclic-word sums; exact finite class-three centralizer','Task C.2; Task C.1; Task C.3',
    'A specified nonzero central local Frobenius is excluded at class10(p^(v_p(m)+1)−1)',
    'Rational conjugation is used only to compare integral cyclic-word coefficients. These are evaluated in the finite group algebra to obtain actual conjugacy; the finite centralizer then contradicts the central Frobenius value. No rational conjugator is evaluated in the finite group algebra. Complete finite coordinate certificates for k=0,1 were independently rerun.')
add('C.2.16','C.2.12--C.2.15; exact first-stage exponent valuation and coefficient-prime shell','Task C.2; Task C.3; Lead 3; Lead 6',
    'The selected A.65 first empty integral class has an explicit two-sided bound',
    'For every prescribed R the selected pair has R<r<=10(5^(v5(m)+1)−1), with v5(m)=v5(C)+d v5(J!)+v5(d!). This supplies a concrete finite upper bound while retaining survival throughR; the exact least class and the universal classification remain unresolved.')

add('A.4.11','A.4.10; exact permutation cores; faithful integral deck homology modulo three; intrinsic finite inner-action extension; actual characteristic lower quotient', 'Task A.4; Lead 1(2)',
    'Every normalizer of the specified finite nine-point deck subgroup descends to the decisive characteristic surface quotient',
    'The deck subgroup is faithful in the finite outer action. Its full inner-action preimage intrinsically recovers P0, and the actual characteristic kernel yields the required surface quotient. The residual upper extension cocycle is written explicitly and dies in P0. A geometric conjugator of a transported deck subgroup is still required for the complete finite comparison.')
add('B.2.18','B.2.10--B.2.11; B.2.16; exact six-coordinate cusp action; primitive cusp centralizer; complete72-tuple finite membership census', 'Task B.2; Task B.1',
    'The actual universal cusp centralizer and its additional central defect are determined',
    'The pure centralizer is exactly the source procyclic x-group, the full centralizer is the source procyclic tau-group, and its central correction map is trivial. All12 passing finite residues were independently rerun and checked against the exact congruences.')
add('B.2.19','B.2.12--B.2.18; actual exponent-change inner morphism; exact source composition law; finite central cusp defects and compact frame space', 'Task B.2; Task B.1',
    'The complete descent image is the kernel of one finite continuous crossed obstruction map',
    'The coefficient group is M modulo the two torsion-centralizer correction images. Its actual H-action and crossed map have exact kernel D_P(H), so the index equals the finite affine orbit cardinality. The coefficient action, full reduced group and orbit are not yet computed; neither triviality nor normality is asserted.')

add('B.2.20','B.2.11--B.2.13; B.2.15--B.2.19; complete marked central-extension cohomology and higher-layer constraints; actual torsion-centralizer lifting recursion', 'Task B.2; Task B.1',
    'The full finite base central kernel is C2 times C3 and its reduced torsion correction quotient is trivial',
    'Both first central layers and all further central source-compatible layers are tested. The pure s and r correction images have orders2 and3, and all24 normalized finite targets lift positively. The full central kernel and both pure torsion centralizers map onto their finite-base counterparts. The remaining reduced group is exactly M0/(M0 intersect S); no vanishing of that remaining group is asserted.')

add('A.4.12','Characteristic quaternion quotient; literal rank9 Schreier action; exact class-two exponent3 group law; actual restriction/deck quotient; complete9216-element base and36864-edge kernel calculation', 'Task A.4; Lead 1(2)',
    'The decisive complete CM centralizer residue census is realized on an explicit characteristic surface quotient of order32 times3^45',
    'The detected actual modular image has order1152 times3^8. All36 signed commuting residues are tested, and exactly the six literal CM powers survive, each with81 lifts. Independent root reproduction and exhaustive236196-vector verification agree. The actual rank73 common cover with the three-division surface and every subgroup order are retained; finite geometric fusion remains open.')

add('A.4.13','A.4.11--A.4.12; actual permutation cores; intrinsic common quaternion epimorphism kernel; verbal class-two exponent3 subgroup; abelian-mod12 intersection', 'Task A.4; Lead 1(2)',
    'The finite three-division normalizer reconstruction uses the explicit input order32 times3^45',
    'All quotient maps, faithful deck inclusion and bounds are retained. The quaternion quotient kernel is intrinsic and characteristic inside P0, so every finite deck normalizer descends to this particular surface detector. The outstanding comparison is finite geometric fusion of transported deck subgroups, not the extension reconstruction.')

add('B.2.21','B.2.15; B.2.19--B.2.20; actual integral Bass--Serre module; exact Shapiro first homology; all signed pair coinvariants; full spectral filtration and integral universal coefficients', 'Task B.2; Task B.1',
    'The remaining finite obstruction has at most four generators at2 and a cyclic3-primary part, with index bound2^56 times3^6',
    'The 144-edge integral graph action, both marked PC presentations, exact dual first-cohomology constraints and exceptional tensor actions are reconstructed. Spectral differentials are retained through upper bounds. The actual C6 subgroup inside the torsion-correction image splits off, yielding the generator and orbit-index bounds; no uncomputed term is asserted to survive.')

add('C.2.17','C.2.11 radical calculation; exact boundary-field conductor intersection; pointed finite-cover fibre product; SGA1 XIII2.9--2.12; Deligne WeilI1.5.1 and1.6; Hensel continuation and actual component transitions', 'Task C.2; Task C.3; Lead 6',
    'SECTIONS A.72 is independently reconstructed with the full joint finite quotient, abelian pair and local conjugacies',
    'The exact continuous section has the point-three component in every prescribed one finite quotient. The proof constructs the designated connected cover, all old- and new-prime local points, the actual transition morphisms and one compact-limit conjugator at each place. Root read the complete reconstruction and opened the exact primary specialization and trace-formula passages.')
add('C.2.18','C.2.17; C.1.12; C.1.15; C.1.21; tangential generic Heisenberg quotient and exact cyclotomic descent; actual first-stage Galois fibre product', 'Task C.2; Task C.3; Task C.1; Lead 3; Lead 6',
    'For every prescribed finite geometric quotient, selected A.72 pairs retain all joint local tests but first fail at integral class3',
    'Choose p outside the fixed cover constants and N0 with exact p-valuation1. The initial rational point makes all first CRT roots1 and forces q=1 modulo p^6, while compatible nonzero central Heisenberg Frobenius fixes every integral class-two reduction. The exact weight-three residue has valuation1 and obstructs every integral lift. The complete fixed finite test still has a locally matching section; universal exclusion of every A.72 output is not asserted.')

add('A.4.14','A.4.12; exact seven-dimensional period kernel and its21-dimensional wedge; all36864 projected Schreier rows; complete36-residue centralizer census; literal rank73 homology quotient', 'Task A.4; Lead 1(2)',
    'A characteristic quotient of order32 times3^24 retains exactly the needed parity coupling and is an actual quotient of the rank73 homology cover',
    'The detected modular image has elementary kernel C3^4. Exactly18 commuting residues lift, each with9 solutions; their two literal CM exponents modulo4 and3 have equal parity. The actual killed subspace and quotient map are retained. This is a parity detector, with no claim that all surviving full exponents coincide.')
add('A.4.16','A.4.15 actual matrices; exact full radical parameterization and opposite word; Taylor11.24,11.46,11.51; complete reflection factorizations', 'Task A.4; Lead 1(2)',
    'The two explicitly generated opposite orthogonal radicals yield the exact actual SO-minus18 image overF3',
    'A coordinate orbit argument supplies every singular-line radical. The opened primary generation theorem gives Omega; the actual nonsquare-spinor generator gives SO. Every source word, all360 determinant checks and all reflection products were independently reproduced. No enumeration of the whole classical group is claimed.')
add('A.4.17','A.4.15--A.4.16; actual C3^2 norm rank2; local group-algebra socle; exact Hermitian form and unit-norm reflection', 'Task A.4; Lead 1(2)',
    'An explicit determinant-minus-one orthogonal centralizer corrects fusion to the actual special orthogonal image',
    'The actual module is proved free of rank2 overF3[C3^2]. The retained Hermitian reflection centralizes both translations and has two nine-dimensional eigenspaces. Right composition preserves the exact induced map on H while correcting determinant. The assertion concerns this specific representation; the joint lower quotient and frame comparison remain to be established.')
add('B.2.22','B.2.15; B.2.20--B.2.21; exact normal coprime cores and all-degree module averaging; full total-degree-two LHS differential comparison; torsion-centralizer lifting', 'Task B.2; Task B.1',
    'Two explicit smaller finite source quotients detect all remaining elementary reduced central classes',
    'The source orders are2^80 times3^6 and2^14 times3^30. Their maps inject (M/S)/p into the respective finite canonical kernel modulo p and the actual torsion-correction images. The proof checks every relevant spectral differential and the actual completion map. Finite-source classes are not asserted to survive in the full reduced group.')

add('A.4.15','A.4.8--A.4.9; A.4.12; exact rank73 Schreier words and all360 quaternion-kernel words; A.4.16--A.4.17; literal translation matrices', 'Task A.4; Lead 1(2)',
    'The actual geometric image on the specified faithful quaternion multiplicity space is SO-minus18 overF3',
    'All free-word substitutions, invariant form, complete opposite radical words and reflection factors are retained and independently replayed. The original C3^2 deck action is a free rank2 group-algebra module. This assertion retains the separate signed-period factor and every remaining homology summand; the full joint comparison remains open.')
add('A.4.18','A.4.12; A.4.14--A.4.15; exact peripheral normal ideal; complete36864-row compact census; actual14-by73 source map; intrinsic augmentation-square kernel', 'Task A.4; Lead 1(2)',
    'A common characteristic source of order288 times3^36 maps onto the compact parity detector of order32 times3^14',
    'The actual36 boundary loops vanish, the rank12 target factors through faithful quaternion homology, and the multiplicity kernel is exactly the square of the labelled translation augmentation ideal. The signed ordinary period factor is joined explicitly. Exactly18 CM residues survive and all opposite-parity residues fail. The full joint geometric normalizer comparison and common pentagon-shadow census remain open.')
add('B.2.23','B.2.20--B.2.22; exact reduced ternary PC presentation and both marked cocycles; explicit restriction to the actual24-dimensional elementary kernel; full LHS filtration comparison', 'Task B.2; Task B.1',
    'The entire three-primary reduced central obstruction vanishes, with remaining affine orbit bounded by2^56',
    'The finite H2 dimension3 and restriction rank1 identify the two-dimensional first filtration step. The comparison proves H2 of the actual infinite source overF3 has dimension2. Its cyclic three-primary central kernel is forced to be the already split C3 torsion-correction subgroup. The remaining reduced kernel is a finite two-group with at most4 generators and exponent dividing2^14; the index bound is a cardinality bound only.')

add('A.4.19','A.4.18; exact normal three-subgroup and order32 complement; Sylow conjugacy; explicit split extension maps', 'Task A.4; Lead 1(2)',
    'The faithful and compact marked extensions split with an exact outer kernel',
    'The proof constructs the actual complements by normalizers, proves their unique conjugacy by the three-subgroup, extends every compatible module/base pair, and identifies the order18 inner kernel while retaining the signed period coordinate.')
add('A.4.20','A.4.15--A.4.17; actual free rank2 F3[C3^2] module; hermitian reflections; exact reflection spinor formula', 'Task A.4; Lead 1(2)',
    'Both determinant and spinor can be corrected in the actual labelled translation centralizer',
    'Two explicit hermitian reflections realize the two determinant-minus-one spinor classes. Their actual ordinary-reflection decompositions and product are independently replayed. The correction preserves the labelled deck conjugation exactly.')
add('A.4.21','A.4.18--A.4.20; complete ordinary four-generator image; actual96 source words and36864 Schreier edges; self-adjoint first-order equations; exact period-spinor graph', 'Task A.4; Lead 1(2)',
    'The complete ordinary first-order joint normalizer equals the actual geometric image of order384 times3^6',
    'The upper bound retains the ordinary signed period, quaternion residue, deck labels and spinor. The actual source census attains it. Every bridge from rank73 words to the eighteen- and six-dimensional matrices was independently reconstructed.')
add('A.4.22','A.4.19--A.4.21; explicit actual normalizer-to-outer map and its order18 inner kernel', 'Task A.4; Lead 1(2)',
    'The detected compact image is exactly the actual ordinary outer modular image',
    'The Gamma(2) outer image has order192 times3^4 and the full modular image has order1152 times3^4. The comparison surjection is an isomorphism by these exact orders, so the complete18-residue parity census applies to the actual outer image.')
add('A.4.23','A.4.15--A.4.16; exact expanded pure radical words; pure nonsquare-spinor cube; explicit perfectness proof; full joint solvable lower image', 'Task A.4; Lead 1(2)',
    'Every perfect orthogonal correction has an actual pure geometric lift trivial on the full retained lower comparison',
    'All32 pure radical words and the nonsquare cube are checked from the original nine-label permutations. The actual joint lower image has derived length at most5. Taking the fifth derived subgroup of the finite joint image gives every Omega correction with all three lower coordinates simultaneously trivial.')
add('B.2.24','B.2.19--B.2.23; exact binary pair coinvariants and torsion diagonals; full first-filtration isomorphism; complete finite H2 and marked restriction/centralizer rows', 'Task B.2; Task B.1',
    'The entire reduced central obstruction vanishes and the literal descent is surjective',
    'The exact4608 source quotient detects the remaining first-filtration classes. Its complete H2 has dimension5; the marked four-dimensional space is killed jointly by the rank2 pair restriction and rank3 torsion correction. The full comparison gives M/S=1, D_P(H)=H and D_P(GT0)=GT0. All source matrices and the full cohomology calculation were independently rerun.')
add('B.2.25','A.7; B.1.3; B.1.8; B.2.24; explicit triangular witnesses; compactness; countable finite-action basis', 'Task B.2; Task B.1',
    'The full quadratic annihilator has dimension aleph0 and an explicit infinite independent descent family',
    'The actual map Xi=(Delta composed with D_P^n) is onto the countable binary product already on H, kills GT and intertwines descent with the left shift. Every finite prefix has its complete actual images computed. A selected full basis gives the exact isomorphism of all annihilators with the countable direct sum and of the maximal elementary quotient with the countable product. Both gentle groups have topological generator number aleph0. B.2.27 subsequently proves that this particular descent family does not span; fixed-subgroup parity remains unresolved.')
add('A.4.24','A.4.9; A.4.18--A.4.23; exact class-two fibre product; all148 actual IA words and19 cube corrections; intrinsic quaternion kernel; complete31104-case label/period census', 'Task A.4; Lead 1(2)',
    'A specified finite peripheral input has exactly the actual pure geometric image at the retained lower output',
    'The three-group input has order3^396 and output order3^65; their actual common faithful products are proved surjective and have characteristic factors with exact product Aut/Out maps. The pure positive output image has order24 times3^126. Modulo-nine deck equations force the precise label/period relation nu=J C_mod3 J. The characteristic refinement and every translated projection are retained. This does not yet give the common five-point census.')

add('A.4.25','A.4.18--A.4.24; actual36 peripheral words and rank38 compact intersection form; intrinsic finite relative kernels; characteristic dyadic compact quotient; exact faithful/base extension morphisms', 'Task A.4; Lead 1(2)',
    'Finite geometric fusion and the exact ordinary descent square are proved on the specified transport domain',
    'The characteristic input degree bound is128 times3^1172. Its actual genus19 cover quotient has order3^776 and recovers the multiplicity form exactly as2F. Pure geometric corrections simultaneously match the lower quotient and signed periods and centralize the labelled translation group. The normalizer descent is a well-defined surjection onto Jc, and the corrected transport acts through the exact commuting square. Its membership in the transport domain must still be forced by a common finite pentagon level.')

add('A.4.26','A.1; A.6.1; exact two-boundary double-cover geometry and independent collar adaptations; all12 faithful Artin identities; complete mixed-subgroup Schreier presentation and induced finite wreath map', 'Task A.4; Task A.1; Task A.3; Lead 1(2)',
    'One explicit pure conjugation identifies the three local quilt images with the genuine braid formulas at every finite target',
    'The gauge is a^(8c)V^(-4c), for every multiplier. Every local evaluation and coefficient quotient is specified. An actual induced B3 map into Q wreath S3 of order at most6|Q|^3 recovers the mixed evaluation without a square root. The additional finite same-parameter test is exactly ABR.4; forcing it from the common finite pentagon level remains unproved, and it is not inserted as an extra shadow axiom.')

add('B.1.9','B.1.3; B.1.8; B.2.7--B.2.9; B.2.24--B.2.25; actual joint source canonical cover; faithful characteristic outer actions; compactness', 'Task B.1; Task B.2',
    'The fixed-subgroup parity is the intersection of exact finite joint-image equalizer tests',
    'The ordinary action and its descendant are retained in one actual canonical source cover. Its positive framed group has exactly the full joint gentle image. The multiplier-one and full fixed parity images are the respective nested finite intersections; the full case keeps the actual arithmetic commutator gamma c gamma^-1 c. A pro-prime character-coboundary attempt is excluded by the actual kernel witness. Computed shift examples certify the precise limitation of abstract surjectivity. The remaining finite equalizer sets have not all been computed.')

add('A.4.27','A.4.15; A.4.26; literal local surface substitutions; all72 quaternion Schreier matrices; complete signed and mixed finite group enumerations; explicit Heisenberg coordinates and split complement', 'Task A.4; Lead 1(2)',
    'The actual signed local image has order93312 and its mixed subgroup is an explicit Heisenberg extension of order432',
    'All432 matrices, all generator edges, all729 Heisenberg products, the actual order16 complement and the cusp interchange are enumerated. The precise mixed equation reduces to k1-k2=2c in F3. The exact commutator comparison excludes the proposed full-target class-two factorization. Local conjugation agreement does not yet identify the full global finite pentagon action.')

add('A.4.28','A.4.26--A.4.27; exact mixed-braid abelianization and central generator; actual signed local432 image; complete independent matrix, multiplication, cyclic-join and central-coset censuses', 'Task A.4; Lead 1(2)',
    'The local same-parameter test is exactly detected by an actual finite coloured four-point orbifold quotient',
    'Adding the u-character modulo twice the central order and then killing the resulting central generator preserves the entire zero-character defect. The actual orders are432,1296,216, and the symmetric two-color join648. The Heisenberg27 derived subgroup injects into the capped216 target. Every element, map and generator transition is retained. Deriving this finite equation from a common finite pentagon shadow remains unresolved.')

add('A.4.29','Actual pure sphere abelianization; Endo--Kamada Theorem3.2; exact crossing-mod4 extension; complete Coxeter and H-section linear systems; actual pure correction words', 'Task A.4; Lead 1(2)',
    'The full binary pure ten-point quotient and its marked H-fusion corrections are computed exactly',
    'The module has dimension35. The complete H-section system has128 cohomology classes; the colored permutation centralizer has64 two-element orbits, with the exact flip-parity stabilizer. Every automorphism fixing module and labels is an inner pure correction times mirror. All cocycles,30 solution directions and affine fusion equations were independently replayed. This is the specified binary quotient, not the complete common pentagon level.')
add('A.4.30','A.4.28--A.4.29; exact free nilpotent Hall coordinates; complete peripheral tangent and cubic-kernel ranks; actual pair twists and84 degree-three commutators', 'Task A.4; Lead 1(2)',
    'The entire pure peripheral outer image at the specified class-three ternary quotient is geometric',
    'The source has order3^294 and the actual pure peripheral image has order3^119. All84 cubic commutators and their Magnus coordinates were independently replayed. The literal map to the capped target retains a nonnilpotent image, giving the exact nonfactorization obstruction for a nilpotent pure source. The full pure four-point cap image has order108 and abelianization C4; the centralizer-only source image has order54 and abelianization C2.')
add('A.4.31','A.4.29; saturated integral sphere relation lattice with explicit determinant-minus-one minor; crossing-mod8 cocycle; actual258-letter pure correction; geometric reflection', 'Task A.4; Lead 1(2)',
    'All four odd multiplier actions on the actual quaternary sphere quotient have marked geometric fusion corrections',
    'The correction at multiplier5 fixes every element over the named H permutations, independently of section. Its full modulo4 system has23 unit pivots and one residual two-pivot. The exact relation witnesses, literal braid word, all colored cocycles and all multiplier-unit sphere relations were independently rerun. Reduction to the binary quotient commutes with each standard action.')
add('A.4.32','A.4.26--A.4.31; actual216 cap multiplication table; complete5670-edge induced map; all38 sphere presentation relations; all45 pair-twist words; exact630-character census and module projectors', 'Task A.4; Lead 1(2)',
    'One actual finite ten-point quotient simultaneously retains all630 colored four-point maps with its complete joint image proved',
    'The pure image is the exact fibre product of630 order108 groups over C4^35, with kernel the full product of630 Heisenberg27 groups. Its full image has order10! times2^70 times3^1890 and quotient E4. Every coordinate, relation and character was independently replayed. The proof recovers all central coordinates by literal Heisenberg commutators; it does not infer the image from an order comparison.')
add('A.4.33','A.4.7; actual one-point Birman sequence and half-turn orbifold group; characteristic free kernels; binary graph-homology centralizer detector; faithful ternary deck action and integral torsion argument', 'Task A.4; Lead 1(2)',
    'An explicit finite free-group refinement kills the entire point-pushing centralizer fibre at any specified lower quotient',
    'The construction uses kappa_s(F), its binary homology cover and the next ternary homology cover; the latter removes the inner-action kernel. The actual finite image in Q0 times Aut(W) has an explicit size bound. The two order-two vertex types are separated by the same finite graph edge-chain calculation.')
add('A.4.34','A.1 actual fixed-pair forgetful isomorphisms; A.4.29 binary sphere quotient; A.4.33 twice per pair; exact induced ordered-to-unordered quotient; recursive quotient by the actual pair-pushing image', 'Task A.4; Lead 1(2)',
    'A specified finite refinement recognizes the image of the actual simultaneous ten-point Klein-four centralizer',
    'The isolated-transposition square obstruction handles each unordered fixed pair. The three-step recursion retains both named involutions and lifts the lower ordinary centralizer through the actual fixed-pair isomorphism. It gives equality of finite centralizer images at every specified lower quotient, including A.4.32, with explicit constructions and size bounds. The accompanying A.4.35 gives finite H-fusion; the complete pentagon census remains unresolved.')
add('A.4.35','A.4.7; A.4.33--A.4.34; actual fixed-vertex half-twist switch; exact quotient-by-fibre maps; free-group mod4 torsion obstruction; complete simultaneous conjugacy recursion', 'Task A.4; Lead 1(2)',
    'A specified finite refinement fuses every labelled Klein-four lift to the named geometric group at the retained output',
    'The proof first recognizes both one-point vertex lifts, retains their actual pair interchange, and compares the second generator inside the finite centralizer fibre. The four-point base is checked by the free-group map to C4. The final corrector is pure times an optional C0 flip killed by the relevant forgetting maps. All source maps and explicit recursive finite bounds are supplied; no complete pentagon-shadow enumeration is asserted.')
add('A.4.36','A.4.31--A.4.32; actual stereographic marking and ambient half-turn paths; exact rational quadratic crossing isolation; complete actual source word and finite quotient replay', 'Task A.4; Lead 1(2)',
    'Literal90- and86-letter braid words identify the actual marked geometric Klein four group in the630-state quotient',
    'The26-letter marking and38/34 rotation crossings are printed. Every one of90 pair-polynomial records is checked by exact Sturm and Vieta counts, rational interval derivative and height signs, and adjacency. Isotopy extension identifies the source mapping classes before finite reduction. All source permutations, squares, commutator, and actual E4 section coordinates were independently rerun.')
add('B.1.10','B.1.9; B.2.8 actual signed frames; B.2.24--B.2.25; exact retained-frame homomorphism and full descent kernel', 'Task B.1; Task B.2',
    'Both parities survive the signed-frame equalizer and the remaining fixed-point equation is typed exactly in the full shift kernel',
    'The actual odd witness has the same signed frames before and after descent, proving that frame equality alone does not settle fixed parity. On the shift kernel N, descent is onto and the odd fixed fibre is exactly the stated nonlinear equation a0=n(Dn)^-1. The physical fixed subgroup splits over its multiplier-one part by the arithmetic group. Every finite frame check was independently replayed.')
add('B.2.26','A.5.1--A.5.2; R1 signed-frame conjugation; exact full crossed harmonic cocycle; B.2.7--B.2.8; complete PC39 centralizers and literal source-A4 marking', 'Task B.2; Task B.1',
    'The harmonic defect extends to a full quadratic annihilator independent of Delta',
    'The full character eta is conjugation invariant, zero on GT and G_Q, and has actual witnesses for both independent bit coordinates. Its finite source calculation retains the original A4 quotient as an additional marked factor. Both full centralizers and the saved odd source frame were independently enumerated; no finite identity is used to infer an infinite descent-kernel assertion.')
add('B.2.27','B.2.14--B.2.15; B.2.20--B.2.24 discrete central-kernel comparisons; B.2.26; exact Brunnian source word; actual V4 semidirect extension; full integral H2 splitting and quaternion commutator', 'Task B.2; Task B.1',
    'An actual full descent-kernel witness proves that the iterates of Delta do not span all quadratic annihilators',
    'The specified word lies in every one of the six coordinate kernels and maps to the named source double transposition. The enlarged source has the exact additional C2 Schur summand; its marked frame obstruction vanishes, giving a full positive lift. After exact normalization the actual descent is identity and eta is one. Multiplication by the earlier kernel witness gives Delta zero and eta one, annihilated by every Delta pullback. All A4 and quaternion maps were independently checked.')
add('B.2.28','B.2.24--B.2.27; two actual descent-kernel bit witnesses; recursive preimages with exact coordinate corrections; compactness; harmonic covariance on the physical fixed group', 'Task B.2; Task B.1',
    'Two jointly independent character families give a surjective paired binary shift quotient and an additional constraint on the physical fixed subgroup',
    'The map (D,Delta,eta) is onto H times F2^2. Every finite prefix of the two character families has its full actual image, and compactness gives the countable product. Their span contains an explicit free F2[t]-module of rank2. On the physical fixed subgroup every eta-iterate vanishes and every Delta-iterate equals Delta; the remaining Delta parity decision stays open.')
add('A.4.37','A.4.26; A.4.34--A.4.36; actual characteristic pure braid kernels; exact central cap detecting zero-abelian words; Fresse Theorem6.2.4; finite genuine gentle pair composition; complete Artin word replay', 'Task A.4; Lead 1(2)',
    'One specified characteristic five-point level supplies invertible finite braid and sphere actions at every retained arity up to ten',
    'The quotient Gamma05/kappa_C, C=(m!)^((m!)^45), forces every inserted pentagon in the named finite pure braid targets. The actual join/cap preserves each zero-abelian defect. Defining S_m coordinates prove descent to the universal kernels, and finite genuine gentle-pair order proves invertibility. Both sphere relators and deletion maps are retained, with a nested-level construction for the centralizer/fusion refinements. The full genuine shadow image and its demanded census remain uncomputed.')
add('B.2.29','B.2.14; B.2.27 actual Brunnian kernel word; exact integral matrix with gcds128 and2; Conrad Theorems3.3--3.5; integral five-term and product H2 maps; Q/Z character detection', 'Task B.2; Task B.1',
    'An independent actual perfect source factor gives a full positive descent-kernel lift with a prescribed new frame',
    'For every finite retained R and prime p at least5 not dividing its order, the joined source is exactly U_R times PSL2(Fp). The canonical centralizer lift follows from the actual integral Kunneth splitting and all Q/Z-valued central classes, without a Schur-multiplier or completion-kernel assumption. The literal commutator identity transfers to the full central cover. Normalization changes descent by Inn(s^t) with t divisible by6, hence leaves it trivial.')
add('B.2.30','R1 full signed congruence covariance; B.2.24--B.2.29; exact cyclic Cartan characters; actual ascending-prime source cores; full normalization cancellation; compactness and exact image of D*', 'Task B.2; Task B.1',
    'Countably many prime-indexed character families are jointly independent under descent and the full character module needs infinitely many descent generators',
    'The signed Cartan character at each odd prime gives a full harmonic defect vanishing on GT and on the physical fixed subgroup. Ascending primes congruent3 or5 modulo8 give actual triangular kernel witnesses retaining all prior signed factors. The explicit map from the countable direct sum of F2[t] is injective; dim(V/D*V)=aleph0. The corresponding map onto the binary product indexed by N^2 is onto already on H, with every finite image computed. Integral source and full finite Cartan tables were independently rerun.')

add('A.4.38','A.1 actual ordinary centralizer descent; A.4.31--A.4.32; A.4.36 marked Klein four; exact two-quartet source paths; complete174-orbit centralizer and8192-edge ordinary-image census', 'Task A.4; Lead 1(2)',
    'The ordinary centralizer image has exact index2^13 times3^208 in the centralizer of the same marked subgroup in the specified ten-point quotient',
    'The actual ordinary image has order2^14 times3^302 and the full finite centralizer has order2^27 times3^510. The two source motions generate N/H by their nested Jordan-loop descent. Every signed crossing, finite image, stabilizer, source Schreier word and Heisenberg bracket was independently replayed. The stronger recognition refinement projects to the ordinary image and remains compatible with this proper inclusion at its lower output.')
add('A.4.39','A.4.28; A.4.34--A.4.37; actual C2*Z graph homology refinements; retained abelian coefficient quotients; all-multiplier mixed normalization; two1260-coset induced quartet maps and exact finite centralizer/fusion square', 'Task A.4; Lead 1(2)',
    'A bounded specified characteristic five-point quotient forces the exact elliptic coefficient relation at every prescribed finite mixed-braid target',
    'Two explicit homology layers force the cusp-centralizer images and recover t=-4c modulo2e from actual retained abelian coordinates. The centralizer-then-fusion construction gives the finite outer S-square with both independent target conjugators retained. The zero-character cap restores the braid center and forces TA.2. All216 cone-retaining S4 quotient graphs and the literal source marking words were independently checked. The final finite genus-one/CM comparison and complete genuine-source shadow census remain outstanding.')
add('B.2.31','R1 E.65.8, E.65.14--E.65.15; B.1.7--B.1.8; B.2.30; signed braid center; exact split and nonsplit Cartan commutators', 'Task B.2; Task B.1',
    'Every prime harmonic character has an explicit full signed-frame formula and a precise multiplier restriction on the literal fixed subgroup',
    'The exact signed frame W_p is a representation on the whole gentle group. W_p(g)W_p(Dg)^-1 lies in the norm-one Cartan, and its quadratic bit plus the displayed cyclotomic correction is the full annihilator. On C_P the value is exactly the corrected local quadratic-residue bit of the multiplier; on C_L it is zero. The complete normalizer checks at nine primes and all4096/16384 products in the p=3/5 pair groups were independently rerun. The Delta fixed-subgroup decision remains open.')


add('A.4.40','A.4.26; A.4.37; A.4.39; A.6.1 local quilt identities; exact Birman kernel; faithful mod3 graph homology; finite actual gentle records', 'Task A.4; Lead 1(2)',
    'One bounded finite five-point input gives the actual genus-one mapping-class and punctured-surface actions, including the full ordinary compact forgetting factor',
    'The90-generator bound retains every required stabilizer map. Literal local weights descend through the universal pure kernels; their actual finite record proves invertibility. A characteristic graph-homology cover kills projected centers, so the actual Birman image yields Aut(Q), not just its inner quotient. The full j0 factor is preserved. Identification with d on the larger finite normalizer is refuted by A.4.42 and requires a further recognition refinement.')
add('A.4.41','B.2.7--B.2.9 full canonical-cover image equality; B.2.27 pants-kernel word; exact six source-deck maps; source abelianization C_N^2; compactness of the actual gentle source', 'Task A.4; Lead 1(2)',
    'Every specified finite family of odd-derived or exponent-four odd-normal targets admits a genuine parity-one gentle survivor, with literal normalized signed frames',
    'The auxiliary cubic frame is a suitable odd power of [[x4,y4],z4]^2. Its signed image is5I on all six decks and its tested coordinates are1. Its full canonical-cover lift commutes with r by the coprime2/3 identity. Normalization retains the identity f-record and Delta1. Compactness gives one genuine survivor for each entire directed family, also with D_P=1 and harmonic parameter0. The cap216 source is computed exactly: degree3954, order2^8*3^15, pure abelianization C12^2. Relative pro3 refinements over the stated exponent4 bases cannot settle the requested exclusion.')
add('A.4.42','A.4.19--A.4.25 actual compatible-pair and perfect-image calculations; retained nine-coset ordinary forgetting map; exact Hermitian reflection and six Cayley lifts', 'Task A.4; Lead 1(2)',
    'The equality of finite CM descent and ordinary forgetting is false on the joined finite centralizer; its exact discrepancy image is the full C3^4 signed-period kernel',
    'An explicit order3 isometry k centralizes the actual deck matrices, has nonscalar first-order quotient and lies in Omega. The actual sixth-derived joint source realizes k with all lower and nine ordinary-forgetting values1. Six exact Cayley lifts realize all first-order symmetric parameters; quotienting the actual two scalar inner rows yields all81 classes. The retained period comparison gives the reverse inclusion. Every additional finite solvable family still leaves the full discrepancy image. The actual swap a<->b aligns the forgetting target, and the integral3J comparison proves equality on the ordinary geometric normalizer. The full joint image is exactly the fibre product over SL2(Z/12), of order1152*3^8. This identifies the necessary next recognition step.')


add('A.4.43','B.1.3; B.2.7--B.2.9; A.4.41; literal rank10 Schreier basis and exponent4 class2 coordinates; exact signed source map', 'Task A.4; Lead 1(2)',
    'The reversed-prime class-two source admits a genuine parity-one identity record, and one existing actual element survives the entire specified nilpotent-kernel family',
    'The actual source has order54*2^65, pure abelianization C12^2 and generator orders12. The296-letter product of the three r-conjugates of [[x4,y4],z4]^2 is an r-centralizing involution with all six signed values5I. Its full canonical-cover lift commutes with r by the coprime2/3 identity and gives a normalized full gentle element with f=1 in the whole source. Fresh root and independent auditor replays check all45 commutator coordinates and exact signed32-element image. The already constructed k in R_nil(Fprime F^3) proves simultaneous survival whenever the inserted subgroup image is nilpotent.')


add('A.4.44','A.4.7 exact graph centralizer and torsion recognition; literal C3*C3 Schreier rewriting; exact affine torus action and finite graph chains', 'Task A.4; Lead 1(2)',
    'The actual cubic orbifold over the nine-point translation cover has a simultaneous finite cone and cusp detector',
    'The exact source is C3*C3 with index3 free torus subgroup and index27 nine-point surface group. Its marked CM element is the cusp c, with c^3=[x,y], while the two finite factors have unmarked fixed triples. The relative graph quotient over every retained finite input D has order|D|*3^(1+|D|/3) and centralizer projections exactly the three named cyclic subgroups. The entire first layer of order3^13 was replayed: all27 residues, rank6 centralizer equations, kernel fibres dimension4, and exactly12 nonidentity order3-lift residues. Ambient H-normalizer recognition remains a further step.')


add('A.4.45','Actual six-relator five-point presentation; fifth insertion; original signed modular marking; A.4.6--A.4.7; full finite vertex-module centralizer census', 'Task A.4; Lead 1(2)',
    'A literal split five-point retraction retains the complete ternary modular centralizer detector and excludes the earlier identity pair with cubic frame5I',
    'The five generator words give pi iota=id, with exact signed relation q192=(-I)^epsilon theta12 pi. The pure signed image has order96 and excludes-I modulo4, so its kernel equals the original B-normal projective kernel. Every relative abelian exponent-m quotient retains this split map. In the ternary modular source all six pure r-centralizer residues are tested in the actual192-dimensional vertex module with96-dimensional kernel; correction rank62 leaves onlyI. Every failed residue has an explicit dual obstruction. Other harmonic frames on identity pair records and general nonidentity pair records remain to be examined.')


add('A.4.46','Actual normalized configuration homeomorphism; eight free forgetful fibrations; Edmonds2012 printed273--274 Smith theorem and lifting proposition', 'Task A.4; Lead 1(2)',
    'The ordinary nine-label translation action has48 fixed grids and a unique fixed lift, giving a trivial configuration-kernel centralizer',
    'The map sends each configuration to its differences from label0. Its fixed equations give exactly Hom_inj(C3^2,T[3]); the universal cover is contractible by the actual rank2..9 tower. Smith acyclicity and discreteness give the unique fixed point. The parameter a corresponds to T_-a/3 and is compared with the other convention by a->-a.')
add('A.4.47','A.4.46; A.4.7 graph homology; two-row LHS restriction maps; explicit bounded cellular Tate complexes; A.4.24 label-period certificate; A.4.42 aligned ordinary normalizer', 'Task A.4; Lead 1(2)',
    'An explicit characteristic finite configuration refinement recognizes the canonical translation normalizer and centralizer at the old joint output',
    'Two actual restrictions kill positive cohomology in each free-extension step.289 characteristic covers and two cyclic Tate comparisons kill the unwanted projected deck centralizer. The subgroup K0 semidirect Gamma(3) has index24*9!, and its induced finite map retains K0/V exactly. Removing the actual affine source representative proves both normalizer-image equalities and the ordinary forgetting comparison. The extra induced period map identifies exactly the finite configuration semidirect subgroup; competing-complement fusion requires the further marking proof.')
add('A.4.48','A.4.45 exact fifth retraction; actual eight-map rank97 source; B.2.7--B.2.9 full canonical image equality; B.2.26 harmonic frame; natural integral H2 comparison for an odd kernel', 'Task A.4; Lead 1(2)',
    'The actual ternary five-point level admits a genuine full parity-one identity parameter with cubic frame1 and a lifted harmonic frame',
    'The common source has order1728*3^97, kernel3^98 overQ576, named generator orders18 and pure abelianization C18^2. Sylow conjugacy and the actual H2 isomorphism on2-primary central kernels lift the harmonic frame through the full canonical cover. Normalization preserves every source coordinate. The exact signed base frame is [[9,4],[8,9]] modulo12 and the shear is1; hence Delta1. Every one of the eight insertions and the full target pentagon is identity.')
add('A.4.50','A.4.48 canonical-cover comparison; B.2.8 andB.2.26 original full source; exact abelian C_n^2 join; compactness; executed cap216 and source-order certificates', 'Task A.4; Lead 1(2)',
    'One genuine normalized parity-one parameter is identity in every finite odd-kernel refinement of the original full source',
    'The added abelian kernel has odd exponentm and order dividingm^2 for n=12m. The same full canonical lift and exact normalization work for every finite intersection; closedness gives the simultaneous element. The concrete joint ternary/cap/Schreier source has generator order36 and pure abelianization C36^2. Both cap IV evaluations and all eight ternary five-point insertions are identity for the same actual parameter.')
add('A.4.51','A.4.45 literal split retraction for m=6; full binary s-vertex module rank97; all eight base source fibres; ternary r-centralizer gate; original signed covariance', 'Task A.4; Lead 1(2)',
    'Every actual multiplier-one parameter in the identity fibre at the specified mixed modulus-six five-point quotient has Delta0',
    'The binary vertex source is exactly B/(Kprime K^2), of order576*2^97. Its correction space has rank45 and all eight pure s-centralizer residues are tested; only identity lifts, with explicit dual obstructions for every failed residue. The same fifth insertion retains both binary and ternary modular sources, forcing both signed frames and the shear to1. The other finite parameter fibres remain to be enumerated.')

pat=re.compile(r'\\begin\{result\}\{([^}]+)\}\{([^}]+)\}\{')
rows=[]
for p in sorted(ROOT.glob('part_*.tex')):
    source=p.read_text()
    for m in pat.finditer(source):
        ident,status=m.group(1,2);start=m.end();depth=1;j=start
        while depth:
            if source[j]=='{' and source[j-1]!='\\':depth+=1
            elif source[j]=='}' and source[j-1]!='\\':depth-=1
            j+=1
        title=source[start:j-1]
        end=source.index(r'\end{result}',j)
        body=re.sub(r'(?m)^\s*%.*$','',source[j:end]).strip()
        statement=re.sub(r'\s+',' ',title+'. '+body).strip()
        deps,answers,checks,notes=META[ident]
        rows.append({'id':ident,'statement':statement,'status':status,
                     'where_proved':p.name+'; statement '+ident,
                     'depends_on':deps,'answers':answers,'checks':checks,'notes':notes})
assert len({r['id'] for r in rows})==len(rows)
def key(r):
    part,*nums=r['id'].split('.')
    return ('PABC'.index(part),*[int(n) for n in nums])
rows.sort(key=key)
with (ROOT/'GT_TOWER_CHECK_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['id','statement','status','where_proved','depends_on','answers','checks','notes'])
    writer.writeheader();writer.writerows(rows)
print('Ledger rows:',len(rows))
print('Statuses:',{s:sum(r['status']==s for r in rows) for s in sorted({r['status'] for r in rows})})
print('Every numbered statement has explicit dependencies, task/lead mapping, audit checks and scope notes.')
