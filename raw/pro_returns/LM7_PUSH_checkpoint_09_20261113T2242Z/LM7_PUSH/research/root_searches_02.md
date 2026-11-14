# Exact source scopes and further approaches after checkpoint 02

This file records approaches investigated in the active continuation. A source
is used only for the precise map or statement below. Unresolved comparisons
remain on the task ledger.

## Full profinite special image and configuration spaces

1. Nakamura, *Galois rigidity of pure sphere braid groups and profinite
   calculus*, primary PDF opened at
   https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf.
   Theorem 2.1.1 concerns the arithmetic action with its stated global-field
   hypotheses. Those hypotheses supply no constructed comparison to the
   local cyclotomic fixed-group action required in F.4.

2. Mochizuki, *On combinatorial cuspidalization of hyperbolic curves*, primary
   PDF opened at
   https://www.kurims.kyoto-u.ac.jp/~motizuki/Combinatorial%20Cuspidalization.pdf.
   Theorem 4.1 and Corollary 4.2 give injectivity for the full profinite
   configuration-space forgetful map, and bijectivity in the stated stable
   range. The surjectivity assertions in Corollaries 5.1 and 5.3 use the
   discrete groups in Section 5. The map needed for D.1 is the first full
   profinite lifting step from the three-punctured curve to its configuration
   space; no surjectivity assertion for that map was extracted from this
   paper. Consequently no peripheral lifting theorem has been claimed here.

3. Collas, *Anabelian perspectives in Galois--Teichmüller theory*,
   arXiv:2603.02848v2, dated 6 November 2026, opened at
   https://arxiv.org/pdf/2603.02848.
   Section 3 discusses the intrinsic GT description at M(0,5). It supplies
   no verified surjection from the full special automorphism group at
   M(0,4) to that group. Section 4.3.2 gives leads to the p-adic
   reconstruction papers; those references were sent to the geometry
   investigation. Section 4.3.3 describes the GT and arithmetic comparison
   but supplies no proof of D.1, D.2, or the CM equality in E.3.

4. A search found the author-hosted Pop line/hyperplane paper at
   https://www2.math.upenn.edu/~pop/Research/files-Res/2025-09-29_2104.10504v2.pdf.
   The attempted open returned HTTP 403. No theorem from that inaccessible
   text has been used.

5. The attached Dolgushev--Guynee source arXiv:2401.06870 was reread at its
   isolated-object and Main Line constructions. Isolated objects form the
   specified cofinal subsystem and recover the gentle group as an inverse
   limit. That definition does not assert surjectivity of all reduction
   maps. The dihedral subsystem has its proved maps, but its factorization
   maps do not form the full cofinal family needed in D and E.

6. Searches for the weight-five S3 action and metabelian special image
   produced no source settling the exact full profinite image. D.21 instead
   proves its symmetry restriction by the explicit conjugation and inner
   correction maps. D.22 records the exact Smith-rank formula and explicit
   stable lattices showing what a single reduction can establish.

## Generalized Jacobian torsion test, F.30

7. Mattuck, *Abelian Varieties over P-Adic Ground Fields*, Theorem 7,
   printed page 114 (PDF page 24), independently opened at
   https://people.dm.unipi.it/lombardo/NonAbelianChabauty/Mat55.pdf.
   The theorem supplies the finite-index local analytic subgroup for the
   abelian-variety part over a finite local field. F.30 explicitly adds the
   torus valuation lattice and proves the semiabelian point-group statement.

8. Creutz, *Generalized Jacobians and explicit descents*,
   arXiv:1601.06445v3, independently opened at
   https://arxiv.org/pdf/1601.06445.
   Section 2.1, equation (2.2), is the torus extension of the Jacobian;
   Section 2.3, Lemma 2.5, gives the divisor quotient with functions equal
   to one on the reduced modulus. F.30 constructs the actual Abel morphism
   and pullbacks of multiplication-by-5^n covers. Its restriction injection
   is proved directly from the finite-dimensional commutative algebra of
   the abelian cyclotomic quotient. No point-injectivity assertion for a
   unipotent completion has been inferred from these statements.

## Integral two-adic lifting audit, E.15

9. The explicit logarithmic coordinates on the even-abelian subgroup give
   bracket 12 times the exterior product. The involution norm is the
   integral unipotent transform of (1+M_S)Z. The order-three norm is the
   integral embedding of its fixed projection displayed in E.15.5.
   These maps, together with the exact H A_S matrix relation, supply the
   primitive comparison for the compressed derivative. The full tangent
   program is independently rerun with its output retained.

10. The first gluing paragraph asserted that normalized component words
    lay in N and that the identity could be taken at the other primes.
    The recorded gauges have residues 0, 2, and 4 modulo six, so the
    normalized words can have nontrivial Q-coordinate. This was flagged
    before accepting E.15. The correction glues the ungauged actions over
    Q first and applies one adelic cusp gauge afterward, with every
    component's actual Q-coordinate and abelianization accounted for.

## Full fixed groups, F.21 and F.32

11. Mochizuki--Tsujimura, *Resolution of Nonsingularities,
    Point-theoreticity, and Metric-admissibility for p-adic Hyperbolic
    Curves*, author-hosted revision dated 30 March 2024, independently
    opened at
    https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf.
    The root reader checked Definition 2.2(i)--(v), Proposition
    2.3(v)--(vi), Proposition 2.4(vii) and its proof, and Theorem 2.17.
    Proposition 2.4(vii) applies to nonproper hyperbolic curves for
    uniqueness of a fixed primitive valuation. Openness of the cyclotomic
    image is imposed only for the additional existence conclusion.
    Theorem 2.17 supplies RNS for every curve used here, with Sigma all
    primes. F.32 verifies the exact closed-subgroup hypothesis by the
    tame quotient Delta -> Z_3. Its explicit valuation R, primitive-ideal
    argument, recovery R[1/5]=B, and finite-center stabilizers were
    independently audited by the root and profinite-images readers.
    F.21 then gives all three full groups and the fixed-lift fibres.

## Further exact comparisons

12. E.16 was read in full. The proof of perfection for the simultaneous
    joint image uses simple targets; no assertion that arbitrary joint
    perfect images remain perfect is used. The exact subdirect-product
    argument, commutator-image surjectivity, and compatibility of the
    identity perfect-factor action were checked. The root reran
    de_solvable_barrier.py: the triple commutator is I+2E14 over F_5,
    giving the explicit solvable quotient outside this family.

13. A.36 was independently rerun and audited by the arithmetic reader.
    Its coordinate morphism, local torsion lifting, both Miller norm
    identities, Frobenius descent, and tangential constants were accepted.
    The finite-field and characteristic-zero comparison remains explicit;
    the statement supplies covers, not an unevaluated central cochain.

## Complete finite Ferrari pentagon, E.17

14. The root reader checked the six literal substitutions, the rank-97
    kernel factorization, the full joint quotient of order 5184, the
    exact cusp-gauge identity, and the affine two-dimensional reduction.
    The proof of the logarithm's additivity now includes the common
    invariant flag and the vanishing of all triple products in the
    three-dimensional unipotent representation. Direct checks of the
    three braid relations and of the unchanged full modulo-two
    generation matrix were added at every retained literal word.
    The independent root rerun of de_ferrari_fibres.py exited zero;
    code/de_ferrari_fibres_root_check.out preserves its output.
    Each of the 24 full CM fibres has a positive witness. No exclusion
    has been inferred from the randomized witness search.

## Further source-image approaches being checked

15. Willwacher, *The Deligne--Drinfeld conjecture after OpenAI*,
    arXiv:2610.15592v4, dated 28 October 2026, was opened at
    https://arxiv.org/html/2610.15592v4, including Theorem 2.2,
    Lemma 3.1, and Proposition 3.2. The reconstruction in Proposition
    3.2 uses the pentagon explicitly. No map from the full gentle
    profinite source into that pentagon solution space has been
    established by this check; its rational conclusion is therefore
    not used as an upper bound for Tasks D.1 or D.2.

16. Markarian, *A remark on the AI proof of Deligne--Drinfeld conjecture*,
    arXiv:2611.01745v1, dated 1 November 2026, was opened at
    https://arxiv.org/html/2611.01745v1. Its index-two subgroup,
    Schreier map, and filling map are explicit. Its source group
    satisfies the pentagon, and the restricted tangent inverse uses
    the mixed pentagon. This supplies no verified surjectivity from
    the full gentle profinite source needed in D.2.

17. The RIMS 1997 index identifies Ihara's beta--gamma preprint as
    RIMS-1177, but provides no download. The 1999 index identifies
    Part II as RIMS-1224 and links a compressed PostScript source.
    The web reader cannot open that content type. Direct retrieval
    succeeded; the initial Ghostscript conversion failed because its
    default temporary directory was unwritable. A second converter
    using a workspace temporary directory succeeded. Both programs
    and both outputs are retained. The root read the resulting primary
    text, including Proposition 1, Proposition 2, Proposition 3, and
    the discussion of the kernel of D on page 11. The first page
    explicitly states that the beta--gamma factorization in Part I
    uses the five-cycle relation. Part II's Kummer comparison gives
    the logarithmic derivative of the multiplication identity; its
    stated kernel ambiguity remains. The CERN metadata record was
    blocked by a JavaScript bot check. Part I remains unopened.

18. Otsubo, *Homology of the Fermat Tower and Universal Measures for
    Jacobi Sums*, Canad. Math. Bull. 59 (2016), 624--640, was opened
    at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008439500022232.
    Theorem 1.1 supplies the free cyclic completed group-ring module;
    Theorem 1.2 specifies the Frobenius interpolation for the actual
    Galois action. The latter formula has not been transferred to the
    larger full special source.

19. Furusho, *Geometric and arithmetic subgroups of the
    Grothendieck--Teichmueller group*, Math. Res. Lett. 10 (2003),
    97--108, was opened at
    https://www.math.nagoya-u.ac.jp/~furusho/paper/GTA-mrl.pdf.
    The root checked Definition 2.1, the exact relation (IV),
    Theorem 3.1 and its proof, Lemmas 3.2--3.3, and Theorem 3.4.
    The duplication argument includes the harmonic relation (IV).
    Enriquez's already checked Kummer compatibility supplies K2 on
    full GT. Rereading the introduction and Section 8 of
    arXiv:2602.12462v1 confirms that its full-GT mapping-class action
    does not establish that additional Lego relation. This source
    chain therefore retains a precise missing hypothesis.

Downloaded third-party primary texts are local reading inputs. Their
filenames and hashes are recorded in primary_reading_cache.json;
they are not reproduced in the deliverable. The download, conversion,
and cache-staging programs and all their diagnostic outputs are retained.

## Further arithmetic and Ferrari audits

20. A.37 constructs the actual order-81 extension from three conjugate
    cubic radicals over K(cuberoot(17)). The exact norm, Kummer
    independence, ramification, residue Frobenius, group law, and all
    729 normalized generator triples are checked in a_wreath17_root.py.
    The arithmetic reader independently verified the coefficient two
    of [t,[t,m]], the vanishing of all other tested degree-three
    directions, and the precise order-27 quotient that forgets it.

21. The root reader audited E.18's literal Ferrari generators, central
    coordinate change, Heisenberg multiplication, and joint pure
    quotient. The complete images of the rank-97 kernel are explicitly
    additive elementary abelian groups; the stacked parameter map has
    exactly the old kernel. The 216-value comparison and the direct
    generation checks at all 24 saved words were independently rerun.
    The two root_check.out files preserve the successful executions.

22. Schneps's 2005 Arizona Winter School notes were opened at
    https://swc-math.github.io/notes/files/05SchnepsNotes.pdf.
    Sections I.3 and I.6 supply the exact Ihara composition convention
    and actual Galois cycle relations used in A.38. The root rerun of
    a_ihara_frobenius_conjugacy.py verifies every 55-by-55 matrix
    conjugation in the nine-point parameter family. Its source basis
    morphism and the transport of other Frobenius words are retained
    in the statement, rather than inferred from the finite orbit alone.

23. The complete proof and both programs for B.15 were independently
    checked and rerun. The radical noncube proof, three-sheet valuation
    calculation at each auxiliary point, exact Miller cancellation,
    tangent coefficient, deck commutator and coefficientwise Puiseux
    Frobenius transport all check. The root also audited B.16's exact
    metabelian quotient, Schreier/Kummer dual coordinates, negative-Y
    factor, binomial rows, tangent ratio nine and negative phase sign.
    Its independent rerun passes.

24. E.19's induced six-coset core, integral rank-95 zero-abelianization
    lattice, rank-three complete correction image, all 27 affine
    evaluations per fibre, literal gauge and hexagons, and both
    generation arguments were audited. The full independent rerun
    exited zero, with 24 simultaneous lifts; its output is retained
    as de_ferrari_mod9_lift_root_check.out.

25. E.20 was independently read by both the geometry and profinite
    readers. The combined kernel's inclusion in N-prime is proved
    using all primary abelian coordinates; it supplies the actual
    full F-abelianization map after gluing. The same gauge gives one
    F-prime preimage for the entire compatible family. The statement
    was refined to name precisely the characteristic class-two levels
    of E.15, rather than arbitrary noncharacteristic quotients.
    The U4(F3) program was independently rerun. Its map is from N;
    the characteristic source kernel, not an asserted extension of
    that particular map, gives the required B quotient.

26. The full-source search was continued with queries on relative
    peripheral embedding problems, the geometric S3 normalizer,
    and metabelian beta functions. Harbater--Schneps was reopened
    at its definitions, Main Theorem, and Section 1.2: symmetry is
    an explicit hypothesis of the checked identification. No map
    proving that hypothesis for the whole source in D.1 was obtained.
    Lochak--Schneps, Open problems in Grothendieck--Teichmueller
    theory, was opened at
    https://webusers.imj-prg.fr/~pierre.lochak/textes/farb.pdf;
    its precise quotient/completion maps were checked, without
    assuming surjectivity of the comparison needed here.

27. The publisher record for Ayoub, Anabelian presentation of the
    motivic Galois group in characteristic zero, gives publication
    on 27 October 2026. The publisher HTML exceeded the web reader's
    size limit. The author's primary PDF was then opened at
    https://user.math.uzh.ch/ayoub/PDF-Files/Anabel.pdf.
    Its introduction, Theorem 8, and the displayed functorial maps
    were read. The source is an automorphism group of the entire
    specified sheaf functor. Extending the one-group source action
    in D.1 or D.2 to that functor remains an unproved comparison;
    no dimension bound is inferred from this source.

28. The mixed norm-zeta search for beta^3=51 is retained in
    a_norm_zeta_51_root.py with its exact bounded failure. A dual
    cyclic-algebra construction, using eta^3=zeta and a norm-17
    element, then produced an exact norm-zeta element with
    denominator six. The prime-two valuation obstructs using that
    element as an S={3,17} detector. The subsequent small cyclic-
    basis search for a denominator supported only at three failed
    in its recorded box; the larger exact search is retained too.
    None of these bounded failures is a nonexistence assertion.

29. B.17 and B.18 were independently rerun, with preserved root-check
    outputs. The exact cyclic-nine symbols and full order-243 arithmetic
    image pass. The proof of the finite image, its commutator table,
    D4 kernel, Frobenius value and cusp-column comparison was read.
    The separate a_ihara_manuscript_root.py verifies every one of the
    55 printed coordinates of A.38 against its saved certificate.

30. E.21's complete source-core calculation, integral abelianization
    kernel, degree-four additive-kernel proof, and Schreier generation
    argument were read. Both de_ferrari_degree4_lift.py and
    de_ferrari_degree4_generation.py were independently rerun and pass.
    The four-strand target order is 344373768, with kernel dimension12
    over the E.18 quotient. All24 corrected triples generate it and
    preserve the two full twists. The proof retains the fact that this
    three-strand core kills gamma3(N).

31. A.39 was audited from the integral lattice onward: the exact
    Frobenius/coboundary comparison, rank21 evaluation, saturated rank24
    kernel, equivariant class-three lifts, actual transported word,
    all global corrections, enlarged local conjugator family, and
    descent to section classes. The root rerun matches all68 maps and
    all27 cases. The geometry reader independently uses a truncated
    noncommutative Magnus evaluator in bc_gluing_audit.py; it agrees
    entry by entry. Its common local-conjugator image has rank6, and
    the resulting map has rank24 in every case. The rank restriction
    to R/3 proves the stated conservative lower bound3.

32. The exact class-four normalization and tame-relation argument of
    A.40 were checked by both independent readers. With the displayed
    order of the two local lifts, the integral right side is
    minus17[z,eO], becoming plus[z,eO] modulo3. The ordinary Hall--Lyndon
    embedding, followed by the elementary free-associative centralizer
    argument, proves injectivity of this bracket. The exclusions apply
    to class-two targets themselves, despite their class-three lifts.
    A.41's completed Fox module, tame injectivity, local normalization,
    absence of a residual conjugacy quotient, and compact finite-system
    criterion were also read. Its arithmetic operator remains explicitly
    unevaluated beyond the certified finite obstructions.

33. The norm-zeta search was enlarged to all small dual presentations:
    29 exact norm-three elements and12 exact norm-seventeen elements
    in the coefficient box of radius2 give123 distinct norm51
    presentations. All44772 cyclic bases in their radius1 boxes
    failed the denominator-three test. The integer-pair implementation
    and output are retained in a_norm_zeta_51_variants_root.py and
    its matching output; the larger radius3 run has its own output.

34. Further primary-source checks on the profinite lifting problem:
    Lochak's Automorphism groups of profinite complexes of curves and
    the Grothendieck--Teichmueller group was opened at
    https://webusers.imj-prg.fr/~pierre.lochak/textes/gt.pdf.
    Theorem4.5 gives the stated automorphism comparison for n>4,
    and Theorem4.6 the braid comparison for n>3. The extension map
    from the source on three strands required here is still to be
    constructed; no bound is transferred across that missing map.
    Boschheidgen--Klopsch--Thillaisundaram, Generating pairs of
    projective special linear groups that fail to lift, was opened
    at https://onlinelibrary.wiley.com/doi/10.1002/mana.201900354,
    through Theorem1.1 and its stated source groups. Those discrete
    generating-pair examples were not asserted to be profinite
    peripheral counterexamples. Searches also retrieved the primary
    abstract of Bell--Wibmer, arXiv2610.38919; both attempted full-text
    arXiv routes failed. No theorem from that unopened text is used.

35. The larger norm-zeta radius-three search completed with 7,235,352
    attempts and no denominator-three witness among the 123 retained
    dual presentations. The separate unramified auxiliary-prime test
    also completed at radius three for p=2: the same number of attempts
    produced 5,445 denominator candidates and no accepted witness.
    The radius-one search allowing all inert auxiliary denominator
    primes had 2,531 candidates and no witness. Each run has a separate
    output and JSON file. These bounded failures make no nonexistence
    claim about S-units, ideal classes, or the desired arithmetic cover.

36. B.19 and B.20 were read and independently rerun. The root checked
    the integral Frobenius matrix, both Smith computations, all21
    displayed nonzero wedge coordinates, and all9 terms of the final
    obstruction functional against the saved arrays. The exact
    rank16 stable lattice puts the selected cocycle in the integral
    Frobenius kernel without evaluating an unknown word coefficient.
    All68 word maps and the full local-conjugator family are retained.

37. A.42 and A.43 were independently audited by the root and geometry
    readers. The affine Fox relation has the three actual generator
    terms and its exact residual-conjugator quotient. For A.43 we
    checked the Frattini exponent and abelian-image bounds, the
    marked zero-abelian-inertia result, all inherited ramification
    constraints, the graph-field bound, the literal target, and the
    compact orbit comparison through J_n^c. Milne's primary ANT
    version3.08, Theorems8.42--8.43, printed pp.151--152, was reopened
    at https://www.jmilne.org/math/CourseNotes/ANT.pdf. Its proof
    bounds a primitive integral element's conjugates, giving the
    generous polynomial bound2(B+1) used here. Milne's AV version2.00,
    ChapterIII Proposition9.1, Corollary9.6 and Proposition9.7,
    printed pp.113--115, was reopened at
    https://www.jmilne.org/math/CourseNotes/AV.pdf. The based
    generalized-Jacobian pullback in A.43 supplies its own boundary
    inertia comparison and exact auxiliary-basepoint translation.

38. The corrected E.22 proof, complete normal presentation, inverse
    companion identity, class-two BCH kernel, multiplier scope and
    exact factorization comparison were read. The root sequential
    rerun of kernel, lift, control and generation took245.227seconds
    and passed all four programs. The output files and a manifest
    of hashes are retained in code/audit_degree5_root.json. Every
    protected failed-initial artifact is unchanged. The overwritten
    original stdout and the explicitly labelled reproduction are
    separately disclosed in the report; no lost bytes are represented
    as an original output.

39. Further searches for peripheral profinite lifting found a displayed
    surjection to a group denoted GT_ell in Martin Gonzalez's 2018
    thesis. The primary theses.fr PDF timed out, and the supervisor's
    Montpellier-hosted copy returned502 on two attempts. The defining
    scope of that group has therefore not been verified and no
    surjectivity is used. Searches also returned Pop's I/OM survey
    (Topology and its Applications313,107993); both author-PDF routes
    returned403. The publisher-indexed text describes actual
    birational and line/hyperplane functors with their additional
    morphisms. No extension from the full three-puncture peripheral
    source to those functors has been constructed. An AI-generated
    problem listing that echoed the task was ignored as evidence.

40. A.44 was read in full and its exact inherited kernels were compared
    with the attached LM7 E.25. The marked normal closure is evaluated
    by the actual free-product retraction to a rank9 free factor.
    Its class-two kernel is the completed group-ring module and its
    completed exterior square, with integral coefficient1/2. The
    lower-central equality is proved in both directions; the free-Lie
    elimination maps identify the actual graded arithmetic quotient.
    The root rerun of a_marked_layers.py independently enumerates
    ordinary Lyndon words through degree5 and confirms the first
    ranks10,45,330,2466,19827. The layer formulas retain the full
    restricted residue image and its nonzero first derived limit.

41. Minamide--Tsujimura, Strong indecomposability of the outer
    automorphism groups of nonabelian free profinite groups,
    Journal of Group Theory28(6)(2025),1453--1476,
    DOI10.1515/jgth-2024-0153, was opened in the primary publisher
    text. Theorem1.1 cites surjectivity of the unrestricted
    pro-prime outer projection. Lemma3.4 proves injectivity into
    the product of prime-to-p outer groups, and Lemma3.8 constructs
    the specified virtual action on an actual open subgroup. None
    of these checked maps supplies the required peripheral-preserving
    lift. Wilkes, arXiv1711.02953v2, was opened at Theorem3.3 and
    Theorem5.1: its basis classification is for pro-p duality pairs,
    and its final theorem gives the stated congruence separability.
    A relative embedding-problem calculation is now being pursued
    with the full profinite pair; no unconstructed transfer from the
    pro-p classification is used.

42. Wilkes, Relative extensions and cohomology of profinite groups,
    JPAA 229(1)(2025), 107846, DOI 10.1016/j.jpaa.2024.107846,
    was opened at https://arxiv.org/pdf/2209.06492 and in the
    publisher metadata. Definition 4.1, Theorem 5.5, Definition 6.1
    and Proposition 6.3 give the finite-kernel relative extension
    comparison. D.23 constructs its map for the actual full profinite
    three-peripheral pair, evaluates it as A_G, and retains the
    additional base-centralizer quotient. Section 6's projective-pair
    results retain their stated hypotheses; they have not supplied
    automatic solvability of this three-peripheral problem.

43. A further search for the full-to-pro-prime transfer opened Horel's
    author PDF at https://geoffroy.horel.org/GT%20p%20torsion.pdf,
    Automorphisms of the little disks operad with torsion coefficients,
    and the author publication page dating the revision to 7 August
    2019. Theorem 5.1 and Propositions 5.2--5.3 identify the pro-p
    endomorphism monoid through the completed parenthesized-braid
    operad. Theorems 5.5 and 5.7 compare that model with its
    materialization and Bousfield--Kan completion. Applying the
    pro-p quotient functor gives an actual map from full profinite
    operadic automorphisms to this target. A lift along that map
    for the required extra graded directions is still to be
    constructed; the checked isomorphisms have pro-p models as
    their source, so they do not supply that lift.

44. Minamide's primary journal PDF, Indecomposability of various
    profinite groups arising from hyperbolic curves, Math. J.
    Okayama Univ. 60(2018), 175--208, was opened at
    https://www.math.okayama-u.ac.jp/mjou/mjou60/_10_Minamide.pdf.
    Definition 6.2, printed p.205, defines GT_l using the image of
    the two-point configuration-space outer group in the pro-l
    curve outer group, intersected with the S3 centralizer.
    Corollary 6.3 proves its stated indecomposability, with the
    Galois inclusions checked on p.206. The full and pro-l
    configuration quotient maps were kept explicitly; no section
    or surjectivity of the comparison between them was obtained.

45. The root read all of D.23 and D.24. The exact product-variation
    map has image [E,A]; varying base conjugators gives the three
    centralizer homomorphisms into A_G. The weak-solution count,
    complement bijection, relative cohomology sign, universal
    central p-cover and Schur comparison were checked directly.
    The independent a_peripheral_count_root_check.out reproduces
    all sixteen enumerations. The separate PSL2(F11) search replay
    a_peripheral_spin_p11_root_check.out/.json gives the exact
    generating orders 435600 and 871200 and product obstruction
    (-I,1). The canonical odd-order matrices and all conjugators
    agree with D.24. The perfectness proof and both explicit
    mixed-product lifts show the precise scope on pro-l shadows.

46. The root read the complete E.23 proof and replayed the exact
    model, full kernel, lift, generation and whole-plane programs.
    They passed in 4.606, 103.513, 404.036, 57.108 and 145.843
    seconds, respectively. All 216 points satisfy the full literal
    relations and generate the target. The original agent stdout
    and programs were hash-protected and remain unchanged. The
    sequential audit manifest is code/audit_degree6_root.json.
    The normal-presentation comparison, inverse companion, source
    Frattini quotient, class-two kernel logarithm and affine
    Schreier matrices were each audited at their stated source
    and target groups. No cofinality of the Ferrari truncations
    is claimed.

47. The complete E.24 proof was checked against its actual binary
    algebra and ternary quotient maps. Seven root replays passed:
    model, lower degrees, complete correction module, lift,
    generation, independent collection audit and joint control.
    Their times were 0.298, 12.282, 43.041, 132.669, 1.568,
    0.974 and 15.138 seconds. Every original program, certificate
    and stdout file is hash-protected and unchanged. The first
    isolated replay omitted de_source and stopped on a missing
    input before the lower-degree calculation; it remains in
    audit_binary_root.py/.out/.json. The corrected replay and
    all copied inputs and new outputs remain separately recorded.

48. The root checked E.25's induced cyclic-cover maps, shift-zero
    normal closure, faithful permutation model and exact joint
    coefficient table. The complete five-cover replay passed in
    12.456 seconds. E.26's integer filling and deck maps, cyclic
    translation argument and nonfactorization word were checked;
    its independent replay passed in 0.510 seconds. The original
    certificates are unchanged. The negative-square source words
    make the printed r-conjugation identities literal; their
    simultaneous inversion has the explicitly printed inner
    correction. Discrete lattices and their completions are now
    typed separately in the statement.

49. A search for relative peripheral embedding and cover methods
    opened Kumar's published paper, Ann. Inst. Fourier67(2017),
    2623--2649, https://www.numdam.org/article/AIF_2017__67_6_2623_0.pdf,
    and arXiv:1409.1345. Definition1.1, Proposition1.2 and
    Remark1.3 retain the restriction to an effective open
    subgroup and the available-branch condition. No descent
    preserving the three prescribed original peripheral classes
    was obtained from those maps. The attempted Harbater
    v6Baall.pdf and isj00coradd.pdf primary opens returned403;
    their search-indexed introductions identify the p-dominating
    hypothesis, but no theorem from an unopened full text is used.
    For our pair with trivial F_p coefficients the actual boundary
    map F_p^2 -> F_p^3 is (a,b) -> (a,b,-a-b), with one-dimensional
    cokernel. D.26 then proves the precise covering obstruction
    directly, including every based local power map.

50. D.25's Clifford cover, all five generating triples, ten literal
    inequivalence relators, complete simplicity certificate and
    power obstruction were audited. The root degree-eight replay
    produces the same JSON byte-for-byte, SHA256
    f3a8c964e4312f1882a8b421aa40aac912bcc20ac2064a30b7e182cb7b505193.
    Its four nontrivial order-five powers remain obstructed by
    C2. This refutes the proposed unit-power removal argument;
    the central obstruction had not been proved to be a
    homomorphism on the peripheral automorphism group.

51. D.26 gives the exact weak-lift count on every open subgroup
    for the D.24 example. The relative H2 restriction is
    multiplication by the subgroup index; all local conjugacy
    choices reduce to the unique odd-order lifts. The independent
    arithmetic reader checked the complete proof and reran all
    twenty-four explicit connected covers of indices1--9. Both
    outputs and all central corrections are retained. In
    particular odd prime-power covers preserve this fixed
    nonzero obstruction; even-index covers have the stated
    2^(2g) weak lifts.

52. E.27's two complete S3 programs passed root replay in2.276
    and7.894 seconds. The free Ferrari image108 is nonnilpotent,
    while its actual thirty-six-coordinate source factor is
    B/(F-prime F^3), of order54. All six pure pairs commute and
    have exponent three, which proves their F-prime values are
    identity. The binary lower-central replay also passed in
    8.352 seconds, giving the exact ranks6,0. These are actual
    quotient-map comparisons, not an inference from the free
    kernel's group name.

53. The root read all of E.28 and replayed both finite and
    integral boundary programs, passing in0.617 and1.647 seconds.
    The primitive rank-six image, both Smith calculations,
    literal corrected words, all ten action substitutions,
    the exact Z[1/3] correction matrix and the gamma5 words
    were checked. The initial final paragraph assumed an
    automorphism of the fixed Ferrari quotient, which E.24 had
    not established. Root and the profinite reader independently
    caught it. The retained passage is
    E28_joint_generation_withdrawn.tex. The replacement uses
    gamma5 of the joint image and its rank97 nilpotent Frattini
    quotient to prove a surjective shadow directly. All432
    multiplier-one points thereby extend jointly through the
    complete two-adic boundary tower.

54. The root checked D.27's25 coordinate maps, its300 kernel
    witnesses, the central product and all conjugator maps in
    the fibre product over C5. The complete independent replay
    passed in1.060 seconds. The explicit nonidentity order-five
    pro-five automorphism is given by literal commutator words
    in a degree-four augmentation algebra; its exponential and
    logarithm use only units in F5. The projection to E0 proves
    the obstructed branch, and (X3^(-r),h) is the required
    actual fibre-product conjugator for the admitted branch.
    No full cofinal lifting assertion follows from this family.

55. The primary Collas genus-zero paper was opened at
    https://www.numdam.org/article/JTNB_2012__24_3_605_0.pdf,
    TheoremB, Theorem3.10 and its proof, printed pp.616--620.
    The exact based braid action and its permutation map were
    checked. E.30 derives the finite periodic-involution
    conjugacy test through B4/<z4> = Stab(5) in Gamma_0,[5].
    The unique fixed marked point forces the theorem's
    conjugator into that index-five subgroup. This gives an
    actual quotient map to T/<q(z4)> and does not assume
    invariance of ker(q) under a finite shadow. The genus-one
    author PDF was also opened at
    https://collas.perso.math.cnrs.fr/documents/Collas-Genus1_gt_action.pdf:
    Definition1.1 explicitly uses relations III-prime and IV
    for its source I-Gamma. That source has not been substituted
    for full GT. The finite conjugacy test is the next active
    binary refinement, alongside the A5 generating-pair target.

56. The later E.28 lineage audit found that E.24 uses the E.17
    replacement origins, while the first boundary calculation used
    the original E.1 G6 words. Their equality in G6 had not been
    proved. The exact withdrawn paragraph is retained at the start
    of research/BCF4_agent.md. The replacement reconstructs every
    one of the432 multiplier-one words, rewrites it integrally in
    H, and proves the needed difference lies in the primitive
    derived boundary image modulo two. All corrected action
    matrices have rank ten modulo two. Independent root replays
    passed: literal family reconstruction67.121s, restricted deep
    correction test65.092s, and the mod-two comparison0.528s.
    The deep six-column ternary correction fails for all432 words;
    its exact norm Smith factors are3,9,9,9,9,0. That failure
    concerns only those six words. The complete18-dimensional
    commutator-kernel presentation then passed root replay in
    55.139s, retaining6668 normal relators and the actual B-action
    closure. Its boundary lattice has rank eight and index144;
    all432 complete-kernel ternary corrections exist and have
    invertible action modulo three. All protected originals are
    unchanged. The full replay is audit_boundary_torsion_root.

57. E.32's complete binary conjugacy computation passed all root
    replays: the degree-two exhaustive control0.712s, full degree-six
    test39.635s, and independent literal conjugators5.166s.
    Every one of96 branch/line inputs passes with central exponent
    zero; the other three translates fail. The nine ternary
    parameters have identity binary correction, so the positive
    assertion covers all864 joint points. The independent program
    reconstructs all forty collected basis words and verifies the
    two literal conjugators of lengths344 and0 without invoking
    the conjugacy solver. E.30's proof was augmented with the exact
    B4 -> B5 -> Gamma_0,[5] diagram, with
    z5=(sigma1 sigma2 sigma3 sigma4)^5 and
    y5=sigma4 sigma3 sigma2 sigma1^2 sigma2 sigma3 sigma4.
    Collas Section3.1 and Lemma3.12 were reopened in the primary
    PDF and provide both the quotient presentation and the literal
    power formulas proving equivariance of these maps.

58. The root read every step of D.28: the finite-cover genus,
    surface counts, core restriction, normalizer/outer-automorphism
    extension, subgroup count, monotonic rational bound, exact
    Shapiro cocycle, labelled cycle products, simple subdirect
    generation and the coupled fibre-product application.
    The independent finite program enumerates all3600 A5
    commutators, all59 subgroups and all120 automorphisms. It
    reproduces the JSON byte-for-byte, SHA256
    3ae406acffc220dd924610709a2d05b499d0a5e214053d66feedeff2b7d6dee6.
    The uniform discarded fraction is
    38122819/33750000000 < 1/500. Original code, JSON and stdout
    are unchanged; code/audit_wreath_root.json records the audit.
    The result applies to the stated transitive five-group actions
    of degree at least25 with fixed-point-free peripherals. The
    all-degree count comparison is the next active approach.

59. The root audited all of E.31, including the exact equality
    (K6 intersect F-prime)/N-prime =6ker(phi), the normal
    presentation with6668 relators, primitive source-word
    preimages, and both inclusions in the completed joint
    three-adic image. The literal preimage replay passed in
    17.508s and produced byte-identical JSON, SHA256
    ba512ea9c44af789f286a6e92d84e4968125f7e529001007d6675d110b3a1d17.
    The Smith factors(1^6,12,12), norm factors(1^4,3,0^3),
    and homogeneous embedding(1,4,12) give finite kernel size
    3^(3n-1) and prove that every finite correction image lifts.
    The prime-supported continuous powers and the actual
    lower-central/Frattini and coprime-H comparisons establish
    one generating word through the full boundary tower at
    every modulus, with all Ferrari evaluations retained.

60. The root found a printed convention mismatch between the
    introductory braid action in Collas2012 and the action
    in Nakamura--Schneps2000, Section1(1.1). No identification
    between those f-coordinates had been proved. Both earlier
    torsion proof files are preserved under
    research/torsion_action_convention_preserved/ with the
    exact reason. The repaired E.30 and E.34 use NS(1.1)
    for the actual equivariant capping action and Collas
    Theorem3.3/Corollary3.2 solely for the action-independent
    classification of torsion. These primary passages were
    reopened. The Ferrari sixth evaluation agrees literally
    with NS: Omega3=sigma1^2 y3, the first factor commutes
    with y3 and sigma3^2, and its exponent in f is zero.
    For E.34, the six-move positive braid certificate proves
    epsilon^3=z4. The geometric map t->1/t inverts the
    order-three rotation and exchanges the two poles; the
    unwanted conjugator location would force8lambda=0 in
    Z/12. The geometry reader independently audited both
    the original pole argument and the convention repair.

61. D.29 and D.30 were read with the exact centerless pullback,
    twisted S5 wreath coordinates, intermediate embeddings,
    parity characters, boundary power maps and literal surface
    counts retained. The root replay of a_peripheral_a5_invariance
    passed. Both D.30 programs passed in 0.440s and 0.260s, with
    byte-identical JSON and stdout. Their JSON hashes are
    13a2e31c5c55003c47debe5506311b0e5490c40665bda55bde731377d3f953d8
    and 002bff223a17c7d54d477568dc29d56edce091c4ddb5a90efc91c1b86612f699.
    All six relevant F20 subgroups, the class-algebra annihilator,
    the actual finite-base sections and the subtraction of maps
    factoring through the base are retained. The geometry reader
    independently checked the count comparison. D.30 completes
    the mixed-base case previously left open at the end of D.29;
    the earlier text now points explicitly to that proof.

62. The root replayed all seven A5 Ferrari programs, including
    the 6840-to-1980 permutation compression, complete source,
    corrections, comparison and solvable quotient. The longest
    replays were 351.477s and 456.780s. All passed, and originals
    were protected by hashes. The proof identifies the actual
    perfect group C, the source quotient of order216, the common
    quotient in the joint target and the signed modular image of
    the actual Galois cocycle. Its final scope retains all further
    solvable boundary component maps and equations; joint
    generation with every such boundary factor is not inferred
    from the perfect/solvable comparison. The common quotient
    of order25 in that further source comparison is retained.

63. All five E.33 programs passed the protected root replay.
    They recover the complete normal-presentation image,
    abelian dimension6, central dimension45, central norm rank35
    and 3^11 corrections over every one of432 source points.
    The integral zero-abelianization relator adjustment is part
    of the replay. Its fourth powers preserve the actual binary
    Ferrari images while realizing every ternary central value,
    and preserve every boundary abelian modulus literally.
    The complete thirteen-program audit, including D.29 and
    E.29, is code/audit_new_refinements_root.json.

64. The E.35 conjugacy solver, complete torsion test and independent
    literal-word checker passed root replay, together with all
    five exponent-four/CRT programs for E.36. This eight-program
    audit finished in177.611s. All216 ternary points pass the
    complete order-three test; the45 literal words are checked
    separately from the conjugacy algorithm. The exponent-four
    model retains every square and Hall carry, and every one of
    the432 source points has2^10 corrections. The actual
    exponent-twelve comparison gives2^10*3^11=181398528 images.
    See code/audit_torsion_class_four_root.json.

65. E.37 was read in full, including the exact integral source
    lattice, both inclusions in its three-adic completion,
    the unimodular Smith transformations, the nonzero-Smith
    divisibility conditions, all zero rows and the cubic identity
    reducing them to F=t3-t2+3Q=0. The literal source-word
    realization and prime-supported joint correction were
    checked. The integral model, norm and tower programs passed
    in0.697s,2.524s and0.584s. Finite fibres have3^(10n+1)
    elements, while precisely3^(10n-1) lift further. The saved
    exponent-three nonlifting correction has zero abelian vector
    and Y36=1; any exponent-nine lift forces Y36=0 modulo3.
    This excludes that correction at fixed multiplier1, with
    every one of the24 CM fibres still containing a full
    Z3^10 family. The exact statement makes no whole-fibre
    exclusion from this single nonlifting point.

66. The two D.31 A6 programs passed protected replay in1.878s
    and0.889s. The full1440-element automorphism group, its
    four-element outer quotient, every labelled choice and the
    entire ordinary union are retained. The D.32 proof then
    gives an ordinary obstruction using fifteen actual Nielsen
    orbits. The root and geometry readers independently checked
    the simple subdirect-product map, all105 source-kernel
    witnesses, every base-centralizer image and the graph-lift
    exhaustion. Root replays of the Nielsen and ordinary
    programs passed in0.512s and4.613s with byte-identical JSON.
    The new ordinary fibre has2160 weak lifts and0 proper lifts;
    the original has3240 weak and1080 proper lifts. Products
    with finite five-groups have the displayed actual maximal
    pro-five quotient and retain both blocked and admitted
    branches above the same prescribed shadow. D.33 was then
    checked directly: the cumulative centralizer correction
    makes every odd-order multiplier-one base conjugator
    outer-trivial for a single A6 kernel, and the displayed
    pullback map supplies a generating lift of the same order.

67. The publisher's primary HTML and PDF for Marco Boggi,
    A congruence subgroup property for symmetric mapping class
    groups, Sao Paulo Journal of Mathematical Sciences20,
    article35(2026), DOI10.1007/s40863-026-00558-y, were opened
    at Theorem C(i) and Theorem5.1(i). The genus-zero case gives
    the required bijection on conjugacy classes of finite
    solvable subgroups of the full mapping class group and its
    profinite completion. The surface hypotheses and the use
    of cyclic subgroups are explicit in E.39. The proof uses
    the actual NS(1.1) capping action, the finite-index core
    comparison, the marked-pole location, the explicit pole
    exchange and the exact exponent-sum map. It proves full
    profinite braid conjugacy for delta_n and epsilon_n for
    every n>=3, with the central discrepancy killed in Zhat.
    Both geometry and profinite readers independently checked
    the argument. The discrete periodic-braid corollary now
    explicitly lifts its rotation conjugator and absorbs the
    remaining full twist as a power of the same periodic braid.

68. E.40 applies the full-target order-four test. The binary
    nonidentity-S3 solver agrees with exhaustive enumeration
    of all1536 degree-two target elements. All96 binary inputs
    pass in40.087s; their two periodic values admit precisely
    central translates0 and2 modulo4, with four literal
    conjugators of lengths0 through11088. All216 ternary inputs
    pass in15.795s; fifteen periodic values each admit exactly
    translate0 modulo9, with fifteen conjugators of lengths6
    through131. An independent evaluator, importing neither
    conjugacy solver, reconstructs all source words and checks
    all19 literal conjugators in13.913s. The multiplier73
    comparison retains delta^73=delta*z4^2 on the binary side
    and period36 on the ternary side. The actual product
    target supplies all864 joint comparisons.

69. A repeated-build source defect was discovered and preserved.
    Recursive TEXINPUTS search selected a saved draft within
    build/; the second checkpoint-05 pass consequently compiled
    a stale first-pass source. Its files, PDF, recorder context
    and exact reason are retained in
    build/checkpoint05_second_stale_source/. The repaired
    builder uses root:build: without recursive search, an
    absolute main source and the recorder. It recursively
    resolves both InputIfFileExists and input, including
    extensionless filenames, verifies every actual TeX input
    against the active manifest and verifies unchanged hashes
    before publishing. The third pass failed at a paragraph
    in E.35; the fourth compiled but rejected legitimate nested
    inputs; the fifth failed while resolving an extensionless
    input. All are preserved separately. The sixth pass
    compiled the active159-statement source to261 pages with
    zero overfull boxes, zero warnings, no undefined references
    or citations, and the verified source-input manifest.
    That exact successful snapshot is preserved before further
    integration. It has not been released as the final05 PDF.

70. A further higher-genus search located the author page and
    abstract of Basualdo Bonatto--Robertson, arXiv2606.01466v2,
    dated8October2026. Full arXiv PDF/HTML retrieval was disabled;
    no uninspected theorem is used. The primary24-page LNS
    text arXiv2602.12462 was reopened, including its introductory
    explanation of the additional compatibility condition.
    Neither search supplied a proved comparison turning the
    present full-GT action into every proposed higher-genus
    cutting action. The exact E.39 result instead rests on the
    opened genus-zero finite-subgroup theorem and NS's actual
    braid action.

71. All six E.41 programs passed protected independent replay.
    The integral source took34.143s, all432 integral word values
    66.317s, and the complete central norm0.745s. The complete
    P8 fibre enumeration took12.665s, actual central-word
    preimages1.500s and the exact tower certificate0.737s.
    Every mathematical JSON entry and every NPZ array agrees.
    All originals remained unchanged. The root read the exact
    Hall/doubled-log map, finite coefficient ambiguity, central
    source lattice, complete mod4 detector, its coverage by
    all432*32 reference values, Hensel parameter maps, finite
    counts and the literal P8 nonlifting word. For n>=3 there
    are2^(10n-9) finite images and exactly2^(10n-10) images
    lifting to the next and every level. The P8 word retains
    (u,v)=(0,4) mod8, giving F=4 mod8, and fails at P16 with
    multiplier fixed at1. Every CM fibre retains a Z2^10
    family. The geometry and profinite readers independently
    checked the proof and its parity/source comparisons.

72. D.34 and D.35 were checked directly, without importing a
    source-image conclusion from the finite base. D.34 uses
    the actual centerless pullback and a prime-by-prime CRT
    construction of one common outer conjugator when epsilon(D)
    is cyclic; the full Out(A) need not be abelian. D.35 uses
    the characteristic maximal-two quotient of a two-generated
    finite group. The Frattini action and the free action on
    generating tuples prove that this quotient has no order-five
    automorphism. The resulting equality epsilon*alpha=epsilon
    precedes the explicit fifth-root centralizer adjustment.
    These give actual ordinary peripheral automorphism lifts,
    with D.35 retaining the original order and fixing the
    kernel pointwise. All three peripheral conjugacies are
    checked through the displayed pullback maps.

73. The six E.38 source/model/modular programs passed the root
    mathematical replay: model1.471s, Nielsen9.993s,
    full source171.547s, all97 N-generators159.459s,
    signed modular comparison1.231s and maximal solvable
    quotient47.610s. Every mathematical JSON entry agrees.
    The initial final guard nevertheless rejected two byte
    comparisons. The terminal perfect subgroup was returned
    with a different four-element generating list, and a
    separately running exploratory replay stdout changed
    during the broad prefix hash guard. That failed guard
    and all outputs remain in audit_sl2_source_root.*.
    The resolution program checks both terminal subgroup
    inclusions inside the very same Sym(251), with their
    order18553505148634694418432000000000000. The actual
    a,b,c permutations and the complete96-element quotient
    Cayley table are identical. All mathematical programs
    and certificates remained unchanged; only the concurrent
    exploratory stdout is explicitly excluded from that
    historical guard. The exact permutation comparison
    passed in6.699s, recorded separately in
    audit_sl2_source_resolution_root.*.

74. The complete E.38 derived replay passed independently in
    332.792s. It reconstructs all16 N-prime,22 N-double-prime
    and3 F-prime chosen generators as literal source
    expressions and checks their actual component and base
    permutation arrays. The root adds a syntactic membership
    proof against the actual input words: every chosen word
    is a main-word commutator or an iterated main-word
    conjugate of such a commutator. Complete Schreier
    rewriting, every original module commutator, all
    conjugation residuals and their entire normal closure
    are recomputed. Both inclusions of each kernel span
    agree with the original certificates. The actual ranks
    are41,41,42, and quotient orders75,8,576,43200.
    Only the search for the small generating sets is
    replaced by their verified literal descriptions.
    Exhaustive small-group controls passed in0.536s and
    the independent module-coinvariant calculation in5.855s.
    The latter retains the seven directions supplied by
    actual second-derived relations. All original
    mathematical artifacts remained unchanged.

75. E.42 was audited by the root and profinite readers.
    The exact inclusions Fhat-prime subset H and K6 subset H
    are retained. The map f -> f^(e2+e3) preserves every
    actual finite two/three-primary Ferrari evaluation and
    the prescribed H-adic images, while giving identity in
    the full pro-p completion of H for every p>=5. At each
    finite stage, the actual H image is the full product
    of its two/three-primary factor and the other p-group
    factors. Applying the same coprime-order quotient
    proof to the corrected image establishes generation.
    Characteristic finite quotients are proved cofinal
    using finite generation of H. This proves only the
    displayed boundary family, with the explicit maps.

76. The new E.43 comparison program passed independent root
    replay in0.177s and a separate geometry replay. Every
    mathematical JSON entry and NPZ array agrees. The old
    literal x,y source permutations have order15; the
    elementary-two cover and signed modular order6 give
    exact new order30. The proved abelianization order900
    makes ordinary free abelianization mod30 the actual
    quotient map. Together with signed q3 it gives the
    full7200-element F image; the ten actual Fermat
    Schreier words give the800-element H image
    Q8 times C10^2. Its actual Sylow projections are
    h^5 and h^16, its class is2 and exponent20.
    Therefore the literal B map to G_L/C factors through
    P20. The root and geometry readers checked the whole
    proof, including the P20 -> P4 times_(B/H) P5 CRT map,
    the explicit onto map from H's prosolvable residual
    to C, the nested compact N-derived fibres, and the
    maximal-common-quotient generation argument. This
    completes the joint source comparison with every
    prescribed E.42 boundary family, retaining all its
    p>=5 identity shadows and the SL2(F5) pentagon.

77. Two further failed typesetting passes were retained before
    repair. The seventh pass found five unbraced widehat
    applications to the mathbb macro in the new E.39 source,
    and a50.77733pt filename-list overflow in D.31. The eighth
    reached the coverage table and rejected an unescaped
    text caret; it also found a143.97688pt filename-list
    overflow in E.41. Explicit accent braces, a text-caret
    escape and shared-prefix filename lists repaired those
    problems. The ninth pass compiled the170-statement
    manuscript through D.35 and E.42 to289 pages, with
    zero overfull boxes, zero warnings, no undefined
    references or citations and a verified input manifest.
    Its exact source, PDF and logs are preserved before
    integration of E.43. The register now follows the
    same actual include graph as the builder, keeping
    unintegrated research drafts outside the numbered
    manuscript register.

78. The tenth build integrated E.43 and compiled the exact active
    171-statement manuscript to292 pages:157 Proved,7 Refuted,
    3 Known and4 Open, with all29 coverage rows. Its final
    log has zero overfull boxes, zero warnings and no
    undefined citations or references. All active source
    hashes still agree with the recorder manifest; the PDF
    contains the final E43.14 residual surjection. Its SHA256
    is e44c5e8657912fb6699af4fc429f2cfc32375fb52f1a93eb2505e2a784cf6984.
    The root actually viewed contact sheets07--12 and28
    full-resolution pages. The geometry reader actually
    viewed contact sheets01--06 and16 full-resolution pages,
    including the additional B.6 display page103. Together
    these cover204 sample pages and44 full-resolution pages.
    No clipping, tag overlap, broken matrices, footer
    collisions or margin overflow was found. The truncated
    initial four-image tool output was not counted as
    inspection; all four images were viewed again individually.
    The final record is research/checkpoint05_visual_qa.json,
    created by finalize_checkpoint05_audit.py only after
    inspection. The exact before/after overflow counts from
    every preserved checkpoint05 log are retained there.
    Mathematical scope remains through D.35 and E.43;
    subsequent exploratory work does not enter this register.

## Work after the immutable fifth checkpoint

79. Checkpoint05 was packed, CRC checked and saved under a new name.
    It contains2296 files and172527839 bytes, with SHA256
    e4b6b4c7604d50ad367c44fb23136d92724709119a763bcb9d54e2254f1e6d01.
    Its exact frozen source tree, active history copy, upload record,
    and Library identifier libfile_9eb9225f4af88191b07d146cf163eb79
    are retained. The archive and its four predecessors remain unchanged.
    Work continued beyond D35/E43 immediately after that snapshot.

80. The root reopened the primary Marin rigidity paper at
    https://www.lamfa.u-picardie.fr/marin/arts/gtrig.pdf,
    including Section4, Lemmas4.1--4.3; the Numdam publisher
    record verifies the2008 publication in17(4),765--780,
    DOI10.5802/afst.1202. The previously checked NTYIII
    Proposition4.4/Theorem4.16 comparison remains Galois-scoped.
    These reads supplied no proved transfer of its matrix Kummer
    specialization to the entire gentle or full special source.
    Enriquez, arXivmath/0609440, introduction and Section1,
    was opened; its additional relations construct subtorsors,
    and no full profinite comparison was used from it.
    Lochak--Nakamura--Schneps2004 was opened at
    https://www.math.okayama-u.ac.jp/mjou/mjou46/_09_Lochak-Nakamura-Schneps.pdf.
    Theorem1 gives the order-five conjugacy formulation;
    TheoremsA/B give the specific Galois conjugator and
    pentaharmonic equation. The source explicitly leaves
    their extension to the whole GT group unresolved.
    The new Hurwitz test below instead uses the actual NS
    action and E39's proved periodic-braid conjugacy.
    Source screenshots returned as placeholders were not
    counted as visually inspected PDF pages.

81. E44 passed the independent root replay of all three new
    class-three programs. The first guard stopped at the norms
    JSON because two earlier input hashes differed; both inputs
    had independently recorded elapsed times. The retained
    resolution verifies every declared hash against its own
    actual input file, proves equality of all mathematical
    inputs, and reproduces every mathematical output and NPZ
    array. Every original artifact stayed unchanged.
    A separate reader reconstructed the associative tensor
    collector, all nine rank103 affine matrices, all45
    actual integral H-prime relators, and the nonlifting
    tower point's obstruction functional, in2.576s.
    Both proof readers checked the Magnus quotient and
    complete220-dimensional cube span, the actual central
    gluing words, and the simultaneous E43 factorization.
    All432 fibres survive; four independent extra congruences
    cut the full E37 reduction family and the explicit
    Y37=1 tower point fails to lift.

82. D36 passed a new isolated replay from exactly ten minimal
    files. The complete module,452-subgroup classification,
    surface Tietze maps, both corrected boundary-count patterns,
    and five actual source/conjugator certificates regenerate
    seven identical authoritative JSON files in9.376s.
    Original artifacts remained unchanged. The root and
    geometry readers independently checked the full ordinary
    centralizer union, exact kernel normalizers/transporters,
    lexicographic finite-family selection, product generation,
    split weak lifts, and all four nonidentity-power obstructions.
    The based module-path term is retained throughout;
    incomplete-framing outputs are preserved and excluded.
    The pro-five comparison explicitly retains an admitted
    branch over the same prescribed five-group shadow, so
    the finite obstruction alone does not supply D1's bound.

83. E45's complete lower A6 kernel and exceptional-outer models
    passed root replay. All129600 pairs,124 automorphism orbits,
    53 epikernels, all36 induced coordinates, and every
    compression intertwiner agree. The original strict
    NPZ guard stopped in63.597s at two noncanonical derived
    generating lists. That failed audit remains unchanged.
    The resolution proves both literal subgroup inclusions
    for all eight differing derived generating lists in the
    identical faithful representations. Their orders are
    2972345018094330659559356497920000000000 and
    102128997161149427406540367434971936194560000000000.
    It runs only the unrun outer correction and final
    comparison steps, and finishes in222.537s. Every
    mathematical JSON and every literal array agrees;
    all original inputs and outputs remain unchanged.
    The exact source quotients are B/(F-prime F^30)
    and B/(F-prime F^6), with their ordinary free
    exponent-sum maps. Both four-strand derived groups
    are perfect of index two. All864 finite points and
    the stated full boundary families survive.

84. The root's new five-point Hurwitz quotient starts with
    the11820 product-one involution tuples in A5. Exactly
    11520 generate A5, giving96 free Aut(A5) orbits.
    A word in the four pure squares, raised to410,
    is the three-cycle(17,26,43);72 explicit pure
    conjugates have connected supports covering96 points.
    The root proves the support-extension induction to A96;
    the geometry reader independently reconstructs all
    tuple data, transporters and recorded word conjugates.
    The initially interrupted generic order attempt is
    preserved. The reverse sphere word proves that the
    first three braid generators already have image A96.

    The complete eight-evaluation/six-coset source compresses
    faithfully from4608 to1074 points, has order
    2^18 3^20 5^15 7^2, and has perfect N-prime image C.
    All144 modular Schreier words prove the actual
    quotient G/P=PSL2(Z/6), and q3 identifies F-prime/C
    with V4. The exact old word reconstruction verifies
    all864 indexed matrices. The maximal solvable quotient
    has order5400, with F image A4 times over C3 (Z/15)^2
    and H image V4 times C5^2, abelian of exponent ten.
    This gives the literal P20 comparison, residual
    R_H surjection, and full E42/E44 boundary gluing.
    The common four-strand target is T23 times A96;
    E39(n=5) proves the full target order-five conjugacy.
    The profinite reader independently checked all these
    maps, including the separate B4 and B5 surjections.

    The full isolated five-program replay passes in58.727s,
    with every mathematical record, literal array and
    subgroup comparison checked and originals unchanged.
    Before integration, the root corrected one reversed
    conjugation in the E46.14 draft display against the
    actual NS(1.1) convention. Both exact lines and the
    unchanged evaluation-map comparison are retained in
    E46_braid_orientation_correction.md.

85. A fresh primary-source search reopened LNS2026,
    https://arxiv.org/pdf/2602.12462, Theorem1.1,
    Theorem2.1(2.1), and the introduction's precise
    compatibility statement. The full81-page v2 PDF of
    Basualdo Bonatto--Robertson, arXiv2606.01466,
    is now retrievable, unlike the earlier search70.
    The root opened its introduction and Theorem4.9
    on printedp41, with its proof setup and Corollary6.13.
    Its actual homomorphism starts at the Nakamura--Schneps
    subgroup and restricts to the genus-zero action along
    that subgroup's inclusion in GT. This specific map
    supplies no surjection from full GT to its additional
    genus-one compatibility data. No additional relation
    is imposed on the present full group from this source.
    Primary retrieval references are turn439view0/1 and
    turn440view0/1. The source date is October12,2026,
    with arXiv v2 posted October8,2026.

86. D36 and E44--E46 are now integrated into the actual
    manuscript include graph. Their proof fragments and
    mathematical certificates were independently checked
    before registration. The active register has175
    statements, with161 Proved,7 Refuted,3 Known and4 Open,
    and retains all29 task rows. The exact preceding four
    coverage rows are preserved. The full integral
    three-adic class-three investigation, the full inner/free
    A6 source, and the characteristic finite-five bridge
    remain separate active work until their comparisons
    and proofs are completed.

87. The first checkpoint06 build stopped at an immediate
    paragraph command at the start of E46's proof. Its
    exact source, incomplete PDF and logs are preserved
    in build/checkpoint06_first_failure. The same attempt
    exposed filename overflows of63.24359pt in D36 and
    35.40152pt in E45. A proof-opening sentence and
    common-prefix filename paragraphs correct these.
    The second build completes with311pages, zero
    overfull boxes, no warnings and no undefined
    references or citations. Its exact recorder inputs
    are verified and saved in checkpoint06_second_complete.
    This build has not been visually approved; subsequent
    mathematical additions require a fresh build and QA.

88. The actual joint A5-Ferrari/Hurwitz source has the
    A5 source order2^38 3^26 5^21 7^2. Its projection
    onto that source is therefore an isomorphism. The
    resulting onto map sends rho_A(b) to rho_5(b), and
    composes with the actual SL2(F5) source projection.
    This gives the same corrected word in the Hurwitz
    factor, including every retained E43/E44 boundary
    family. The exact independent replay takes57.817s;
    every mathematical JSON, source array, strong generator
    and base agrees, with unchanged originals.
    The target common quotient is proved trivial using
    an eleven-cycle and its literal three-cycle commutator.
    The complete four-strand target is consequently
    (T23 times over S_L T_L) times A96. These are
    E46.26 and E46.27, with both projection maps specified.

89. D37 supplies the actual fully invariant Magnus target
    P_n of order5^(17n+2), its complete ordinary
    three-parameter special outer family, and the exact
    source S3 action including inner corrections. The
    root and profinite readers independently verify
    the all-precision proof. In the draft D37.13,
    rho_n(w(g,h)) incorrectly applied rho_n to an
    element already in P_n; its corrected left side
    is w(g,h). The exact right side remains
    Phi_{g,h}(rho_n(w)). The root's isolated standalone
    replay takes2.049s, reproduces the entire n=1,2
    JSON byte for byte, and preserves all originals.
    D37 is integrated; the full-source lifting problem
    above these particular characteristic targets remains.

90. A new root calculation constructs the literal chain
    transvections of B5 over F3 and F5. The alternating
    matrix, all vector permutations and every Artin
    relation are checked. The exact full images have
    orders51840 and9360000, equal to the corresponding
    symplectic-basis counts. Both periodic powers give
    minus identity, with actual element orders10 and8.
    The eight pentagon/NS evaluations, with all six B/F
    cosets retained, give source orders46656 and9000000.
    Their compressed actions have explicit B-set
    intertwiners. No CM-survival assertion is made
    from these target and source constructions alone;
    the source fibres and five-strand relations are
    the next calculation.

91. E47's entire integral class-three calculation passes
    root proof review and isolated eight-program replay
    in55.690s. Every mathematical JSON entry and every
    NPZ array agrees; all31 authoritative originals
    stay unchanged. The actual Hall lattice, all450
    central source words, four rational conditions,
    two residue tests, unit chart minor and exact
    central right inverse give Z3^70 correction images.
    The word fibres are their actual joint-kernel cosets.
    The fixed exact lower fibre has21 finite central
    directions; an actual higher lower-coordinate change
    supplies the22nd. Two finite lower equations give
    the exact3^25 image in E44. The Y41=1 witness has
    explicit finite central coordinates and norm zero,
    but obstruction values(2,2), independent of higher
    digit changes. All432 sources and all stated common
    boundary/SL2/Hurwitz families survive. The draft's
    weight-three logarithm sentence is corrected to
    scaled T coordinates12 times the Lyndon basis;
    both sentences remain in the audit note.

92. D38's exact elementwise conjugators on P1 and its
    full odd-base A6 chief comparison pass root review.
    The isolated two-program replay takes4.444s and
    reproduces both JSON files byte for byte. The
   3125 Magnus cases include1200 nonzero restricted
    fifth-power terms. All16 unit powers modulo60
    are verified on all360 A6 elements, with the actual
    odd-S6 automorphism located in the saved Aut(A6)
    table. The outer averaging gauge, every cover
    boundary map, kernel normalizer, Mobius count and
    coupled odd pullback retain their literal maps.

93. D39 determines every generating lift through the
    first universal coprime Frattini cover. The actual
    Cayley-chain splitting and boundary norm formula
    give peripheral automorphisms. Every source lift
    factors through this same finite cover, so the
    parameterization includes every generating branch.
    Root and geometry independently read its full proof.
    The two isolated replays take3.482s, with byte-identical
    JSONs and unchanged originals. All28 cases pass;
    whole-fibre enumeration in orders48 and54 verifies
    both fixed-conjugator counts and the complete
    ordinary centralizer union.

94. E49's prime-three five-strand calculation passes
    a separate matrix/source audit in2.915s. Exhaustive
    matrix enumeration gives all51840 target elements.
    All3840 induced coordinates,104 compression
    intertwiners,81 kernel elements,576 disjoint cosets
    and1152 closure edges certify the source order46656.
    All97 cubes and9409 commutations prove the literal
    factorization throughG6. The1944-edge E18 map is
    an isomorphism onto the first B4 image of order648.
    All864 values retain their exact source words.
    Three explicit symplectic matrices simultaneously
    conjugate the original four braid generators to
    the changed ones. Their literal braid words and
    all96 identities are checked. The additional root
    all-units certificate verifies the printed row table,
    the exponent-three normalizer, all96 delta conjugators
    for the four unit powers modulo ten, and all24
    epsilon conjugators. This proves the entire stated
    multiplier range lambda=1 modulo72. D39 andE49
    are integrated; E48 remains a separate ongoing
    full A6 computation with new three-primary layers.

95. For the next equivariant pairing step, the root opens
    the primary author PDF of Broto--Moeller--Oliver,
    Equivalences between fusion systems of finite groups
    of Lie type, at
    https://www.math.univ-paris13.fr/~bobol/bmo1-jams.pdf.
    LemmaA.1(b), printedpp15--17, states the exact
    uniqueness of invariant symplectic forms for a finite
    odd-order group of order prime to the finite-field
    characteristic, on a self-dual module with zero
    invariants. Its characteristic-two argument is
    explicit. Root retrieval references turn449view0/1.
    The new compact cover module has zero invariants
    by the actual split boundary and graph sequences.
    The all-precision pairing and subsequent relative
    pro-p automorphism construction remain under
    investigation; no full peripheral lift is inferred
    solely from the pairing statement.


96. Checkpoint-06 typesetting preserves all seven passes. The fourth failed
    at an unbraced accent; the fifth completed with two overflows, 72.9224
    and 11.25229 pt, in E47.11 and E47.22. Both displays were split. The
    sixth and seventh complete logs have zero overfull boxes, zero warnings,
    no undefined references or citations and verified active-source hashes.
    The seventh pass corrects only coverage-table typography and spacing.
    Earlier passages and the earlier clean PDF remain preserved.

97. Root visually inspected all 242 sampled pages in fourteen contact sheets
    and thirty-two full-resolution pages, including every formerly overflowing
    display and distributed samples. The exact seventh-build render changes
    only pages 326 and 327 and contact sheet 14; these were inspected again,
    with every other image hash unchanged. No clipping or overlap remains.
    The final PDF has 331 pages and SHA256
    560a3619cf5f208b96503470ffd15ed60992f199e63342bd6a85ee4c48335619.

98. Root reopened Broto--Moeller--Oliver Lemma A.1 and its complete proof in
    the author PDF, retrieval turn451view1, printed pages 15--17. The DOI
    resolver failed; the publisher issue result turn452search0 and the
    author's published-PDF search result turn452search4 agree on JAMS 25
    (2012), 1--20, DOI 10.1090/S0894-0347-2011-00713-3. Opening the latter
    PDF timed out (turn453view0). D40's complete integral pairing proof has
    been read by root and independently by geometry; root program replay
    and integration remain pending at checkpoint06.

99. The D41 relative pro-p draft now supplies an exact integral homology
    image and full literal-fibre description. It awaits root audit. E50's
    prime-five residual certificate identifies the actual SL2(F5) factor
    and elementary abelian five-kernels; its common source with the old
    double cover remains under computation. E48's new metabelian source
    has full affine generating fibres over all 864 old points, whereas
    only 288 admit zero module value. The common-source generation and
    remaining perfect-residual comparison are not yet integrated. These
    are ongoing calculations, not answers to the full-source tasks.


100. D40 and D41 pass root full-proof review and isolated program replay.
     D40 reproduces its entire JSON byte for byte in 0.643s over the four
     actual covers, with all sixteen finite-field and integral corrections.
     D41's initial finite gate used all vector transvections; root required
     the exact elementary list in the proof. The original artifacts are
     preserved as a_relative_prop_all_vectors_superseded.*, and the new
     eight-generator/two-generator runs give orders 720 and 24. The root
     isolated replay is byte-identical in 0.279s. The proof also retains the
     explicit four-factor diagonal SL2 identity. Both statements are now
     integrated; all four full-source tasks remain unresolved.

101. Checkpoint06 is frozen, CRC-verified and saved under a new identity.
     It contains 3987 files and 409074505 bytes; SHA256 is
     6ea5d7a87a572b9eeabc7b7aabf2d374e3173f6163173619bcb1384dd5996ce5.
     The five earlier archives are unchanged. The local transfer helper
     failed before a service write because its Codex auth file was absent;
     the runtime-authenticated prepared upload then transferred the exact
     workspace bytes and finalized its returned opaque session. The
     preserved metadata and history copy identify the same saved archive.

102. For the even-base intersection problem, root searched Barge--Marche
     and opened the primary author PDF at
     https://webusers.imj-prg.fr/~julien.marche/papiers/Symplectic_Chevalley_Weil.pdf
     (turn459view0, ten pages). Its Theorem1 directly gives a primitive
     integral invariant Lagrangian for a free finite-group surface action.
     The manuscript's rational Witt comparison and the field hypothesis
     in Section2 were also read. The publisher URL failed. D42 is reserved
     for the ongoing actual boundary-gluing and finite-field cancellation
     argument; no even-base extension has yet been registered as proved.


103. D42 passes three complete independent proof readings. Root reopened
     Barge--Marché's primary author PDF (turn471view0): Theorem1 gives
     the integral primitive invariant Lagrangian on p1. The proof checks
     the actual alpha-twisted free-action double, the Mayer--Vietoris neck
     lattice including its integral index, its orthogonal quotient, and
     finite-field Witt cancellation on identical semisimple modules.
     Root's isolated Q8 replay is byte-identical in0.368s, with all eight
     boundary maps through729 and15625 and original inputs unchanged.
     D42 is integrated. The exact characteristic two-then-p quotient
     maps retain P_n; compatibility as the intermediate stage varies
     is the next explicit comparison under investigation.

104. The first checkpoint07 build, incorporating D40 andD41, completes
     with zero overfull boxes and no undefined citations or references.
     Its exact inputs and logs are preserved in checkpoint07_first_complete.
     D42 and the current E50 continuation postdate that preserved build.
     E50's four source certificates independently replay in dependency
     order with all mathematical JSON records and NPZ arrays identical.
     The replay verifies every declared input hash against its own files.
     The initial replay-driver input discovery failed before any certificate
     executed because it treated an overlong text literal as a filename.
     The failed driver/output remain preserved; the correction accepts
     only explicit bounded filename literals. The target replay is ongoing.


105. The previously inaccessible Gonzalez thesis is now opened in the
     supervisor-hosted primary PDF (turn463view0), Definition2.6.10 and
     Remark2.6.13 on printedpp90--91. The displayed pro-l comparison
     concerns the group with the pentagon retained. Marin's author PDF
     (turn468view0) and published primary text (turn480view0), Section3.3
     on printedp773, were opened and give the same equations and arrow.
     Fresse's cited primary book, Theorem11.1.7 and Chapter12, is also
     opened (turn470view0 and turn471view2). Its operadic comparison has
     the full pentagon in its source and target. The explicit projection
     of a profinite pair to its pro-l pair retains that equation, so its
     leading metabelian output lies in the proved D3 line. No lift of the
     extra peripheral or gentle directions is inferred from that arrow,
     and its displayed surjectivity is not used as an additional theorem.

106. E50 passes both complete isolated replays: source242.635s and
     target204.890s. Every mathematical JSON record and every NPZ array
     is literally equal; each input hash is checked against its own
     original or replay location. Two readers check the exact signed
     common quotient and residual correction, and the added target proof
     has a second full reading. The new H-image and its generation are
     proved explicitly without finite-kernel invariance. The full common
     quotient has order72000 and kernel125; both three-bit signs and all
     25965 source/73496 target relations are retained. E50 is integrated.
     The full A6 order64 solvable layer and prime-seven source remain
     active computations, outside this accepted statement register.


107. D43 passes root and geometry independent complete proof readings.
     Both audit the residual equality through actual finite source maps,
     the exact characteristic transition kernels and automorphism descent,
     the compact inverse fibre without surjectivity of its transitions,
     and the nested exact-conjugator sets. Whole-quotient Hopficity proves
     all-source factorization without finite generation of the kernel.
     The two-then-p application retains precisely the original P_n quotient.
     D43 is integrated; the four outstanding task rows remain open.

108. The second checkpoint07 build fails during LuaLaTeX pass1 in
     D.42.17: split was used for two aligned equation pairs. The complete
     attempt and its source snapshot are preserved as checkpoint07_second_failure.
     No new PDF was produced. The repair changes only that environment
     to aligned; the exact prior source passage is separately preserved.


109. The third checkpoint07 build reaches E50 and stops at its second
     paragraph heading with Improper prevdepth. The complete attempted
     build and source snapshot are preserved as checkpoint07_third_failure;
     no new PDF was produced. The proof now starts with ordinary prose
     before its first paragraph heading, the same repair used in E46.

110. The double-cover Kummer sign is checked from the literal map and
     reopened primary text. Root opened NS newGT.pdf (turn491view0,
     turn492view2, turn494view2), Section2 positive-root definition,
     equation2.1 and its convention paragraph, equation2.4 and Lemma2.3.
     c2([x,y])=-1, x acts by -1 and y by1, so c2(f_sigma)=+kappa2.
     The exact simultaneous-inversion automorphism commutes with delta2
     on its free basis and reverses the sign. D5's earlier arithmetic
     sentence was wrong in the stated NS convention; the former passages
     are preserved. E25 keeps its exact negative coefficient labels.
     E29/E38 use NS Theorem2.5 directly, and the dependent E43/E46/E47/E50
     arguments retain that actual Galois choice. No certificate changes.
     Enriquez's Theorem8.1 and Remark8.6 were reopened (turn493view0,
     turn494view0, turn495view0), confirming the literal delta_N/c_N
     distribution maps used in every finite test.


111. The fourth checkpoint07 build completes with one20.49881pt
     certificate-prefix overflow in E50 and no undefined references
     or citations. It is preserved in checkpoint07_fourth_overflow.
     An optional line break inside the literal prefix repairs the line.
     The fifth complete build has zero overfull boxes and verified
     actual inputs. Its snapshot is checkpoint07_fifth_complete.
     The render script now covers the complete revised D5 span and
     all new D/E statement spans, with its former program preserved.


112. Root inspected the fifth complete checkpoint-07 PDF: all 267 sampled
     pages in fifteen contact sheets and sixteen listed pages at full
     resolution. The D5 correction, D40--43 displays, E50 signed/residual
     maps and repaired prefix, open-task table and bibliography are clean.
     Zero overfull boxes, warnings or undefined references/citations remain.
     The exact current PDF hash and image hashes are recorded in
     research/checkpoint07_visual_qa.json.

113. Root began isolated complete replays from the frozen E48 and E51
     manifests. E48's full source chain already passed all 865049 final
     Schreier checks and every original-word DAG value. E51's model,
     compressed source, subgroup, projective comparison, residual and signed
     common-source computations all compare exactly; the final target
     replay is still running. Full completion is recorded only by the
     corresponding audit JSON with all_passed=true. D44's new centerless
     pullback, full pro-ell pair and invariant leading-term construction
     passed root and geometry proof reviews; its explicit peripheral
     permutation justification was added with the prior fragment preserved.


114. Checkpoint07 exceeds the prepared single-file limit of536870912 bytes;
     the rejected preparation wrote no file. The exact894790136-byte ZIP
     is saved as two parts and a checksummed reassembly script. Their joined
     SHA256 equals5f6d77e47dd8a29eddae51a18214927fdb917ce02af244d2d0e8740af590d3c8.
     All three uploads succeed and their returned metadata are applied.
     The full original ZIP is preserved unchanged in history. Exact native
     identifiers and the failure/partition record are retained.

115. D44 passes root's literal certificate replay and the complete proof
     reviews. The infinite pro-ell comparison explicitly retains the three
     peripheral labels, centerless pullback, positive cusp, unique pair and
     invariant integral leading term. E51 passes the entire nine-program
     root replay in945.743s, including its109340-relator final target and
     all literal prime-five/prime-seven joint maps. Both are integrated;
     the four remaining global tasks stay open.

116. The new integral symplectic probe verifies all4656 N matrices and240
     K2 matrices over Q, with explicit standard intertwiners and mutually
     annihilating additive radicals. Its global radical has rank5; all
     denominators are supported at2,3. The independent geometry audit
     verifies the full elementary SL2 maps as well. Root is proving the
     uniform congruence closures and exact residual maps before integration.


117. D45 is fully read by root; White's exact author PDF Section3 and
     Lemma3.2 are opened. Both isolated programs reproduce all JSON bytes
     and all arrays in8.075s. D46 is fully read and its two model/centralizer
     cases reproduce every mathematical output and literal array in26.956s.
     Both complete finite-base and return-source proofs also pass a second reader.

118. E48 root validation completes all11 full stabilizer chains in680.367s
     and all22 remaining quotient/module/fibre steps in870.501s. All267
     authoritative source artifacts remain unchanged. The complete proof
     and the exact common-source generation are accepted; a replay-guide
     filename typo is corrected with the original passage preserved.

119. E52 identifies the exact integral source at every modulus prime to6,
     including parity detection, SL2 times rank5 N image, rank3 F-derived
     image, the actual A_(2m) quotient and full lower-central inverse-limit
     residual. Independent audits reproduce the complete residual certificate,
     all20 K2 conjugation comparisons and both uncompressed p5/p7 source maps.
     The whole closure proof passes a second reader. The uniform simultaneous
     fibre/common-source comparison remains an active next step.


120. D47 complete root proof and literal isolated replay PASS; a second
     reader checks every composite phase, nonsplit carry and full fibre.
     D48 complete root proof/code read and all four precision replays PASS
     in47.429s. A second independent proof reader checks every integral
     centralizer, source-core, generation and inverse-limit comparison.

121. E53 exact uniform common-source proof and isolated independent replay
     PASS. The centre/normal-subgroup proof, signed canonical comparison,
     first-layer determinant3 and full abelian kernel are checked. The
     closed full-mod-p case is made explicit. The rejected exact-order60
     probe and the audit's unsimplified symbolic comparison are preserved.
     D47,D48,E53 are integrated with unchanged open task statuses.


122. Root opened Steinberg's original Yale notes at the University of Utah,
     https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf.
     Section 7 Theorem 10 and Corollary 2(b), including the finite-field
     exceptions, prove the exact universal SL2(F5) to PSL2(F5) central cover
     used in E54. The F5 rank-one case satisfies every displayed restriction.
     The actual PSL2(F5) to A5 permutation identification is retained separately.
     PDF pages at indices84,88,89 were opened as screenshots after the text read.

123. Primary research for general outer-character detectors found Turaev's
     Sections of fiber bundles over surfaces, arXiv:0904.2692v1 (2009).
     Root opened its full PDF and read Theorems1.1,1.2 and Sections2.1--2.4.
     The relative statement assumes positive genus and a q-free boundary
     family; it does not supply the genus-zero chief step. The arXiv PDF
     open for0804.1489 failed with DisabledError. Publisher copies were
     located but not yet opened. The active proof route derives the exact
     all-genus finite group-algebra count and finite scalar covers directly,
     retaining proper subgroup images for an explicit Mobius inversion.
     No general chief theorem is registered from this active route yet.

124. E55 complete root and independent proof reads PASS. The exact CRT
     common source, inverse-limit residual correction, one actual Galois
     word, generation and both complete word fibres are all checked.
     E56 complete root and two independent proof reads PASS; root's isolated
     exact replay PASS in3.082s, with every mathematical JSON value equal
     and every original unchanged. E55 and E56 are integrated, retaining
     all four unresolved global task statuses.

125. The first E54 root chain driver stopped before running a saved chain:
     it chose a preparation log instead of the complete _order.out record.
     The exact driver, traceback and isolated directory are preserved in
     E54_root_chain_initial_log_failure.json. The corrected driver accepts
     only a final PASS record with every exact chain field and checks all
     available complete records for equality. Its new full replay is active.
     The separate E54 quotient replay proceeds independently and protects
     all417 frozen source artifacts.


126. Root completed the D49 proof and both new program reads. The final
     explicit fine-cycle origin choice is checked against the actual j_C
     injection. Both isolated programs reproduce every JSON byte and every
     log byte, with all protected originals unchanged. A second complete
     proof reader passes the full refinement and whole-source application.
     D49 is integrated, while D1 and D2 remain unresolved.

127. Public searches for prosolvable/prosoluble peripheral automorphism
     lifting and pro-p-to-prosolvable Grothendieck--Teichmuller comparison
     found no theorem resolving the exact remaining map. Primary papers
     on prosoluble free products, unrestricted outer automorphisms, and
     prosolvable surface rigidity appeared; their search abstracts do not
     prove the required peripheral lifting assertion. None is used as a
     theorem in the manuscript from this search. The direct finite
     scalar-cover proof continues independently.


128. E54 full root proof and all new Python/C++ collector reads PASS.
     All8 complete chains PASS174.520s; all20 remaining program/comparison
     steps PASS. The initial preparation-log selection failure and strict
     derived-generator-list comparison failure are preserved. The latter
     is resolved by explicit mutual signed-word identity maps on the same
     ambient permutation points; every other array remains literal. The
     continuation retains the failed directory unchanged. All417 frozen
     originals are unchanged. E54 is accepted and integrated; the verified
     Steinberg bibliographic entry is merged with its exact original
     fragment preserved.

129. E57 complete root proof read passes the exact residual ranks9/6,
     power120 congruence correction, direct I fibre product preserving the
     whole E55 word, common sources and target generation. One sentence
     making the onto abelian/derived-coordinate comparison explicit was
     requested before its final manifest. Its independent peer read and
     isolated certificate replay remain to be completed.

130. The general finite character-count argument is now being checked
     for arbitrary normal kernels. Its central scalar detectors allow
     the joint-image argument to use [E,A]=A. The finite lower-central
     residual and actual nilpotent detector quotients are the active
     next step toward the full D1/D2 source comparison. No global task
     status is changed before that complete proof and audit.


131. E57 is accepted after the complete root and geometry proof reads,
     all three new Python reads, and all four isolated certificate
     replays. Mathematical JSON and every NPZ array agree literally;
     the complete536-point chain checks219684 final relations. The
     exact full-word correction, common quotient and target products
     are retained. The frozen source SHA is cf54237143936a0825f2a9f97a
     6096366599a6139dc2bdcc1366acfd4bf017f5. Root runtime10.229s.

132. D50's final residual comparison and actual aligned row breaks
     were read and accepted by root and geometry, SHA b27a2116165d03c9
     75e4022125e92fcbf3e599f25d217b350f32a8ec26ef3ff9. Its independent
     finite scalar-cover program is fully read and replayed literally:
     420 Q8 phase cases,848 noncentral-kernel cases,1088 proper-subgroup
     counts,136 ordinary Mobius counts,3672 boundary transports,
     331776 pair-group products, and the nonfaithful32-point pullback.
     All original hashes are unchanged; root runtime0.239s. The four
     normalized free-Lie source witnesses also pass isolated literal
     replay, with exact rescalings2,3/2,-1,3 and common denominator2;
     root runtime0.387s. D51/D52 are being written before global
     task statuses are changed.

133. Turaev, Sections of fiber bundles over surfaces, arXiv0904.2692,
     was reopened at the primary PDF. Lemma2.1 constructs the scalar
     cocycle; Section2.3 constructs the relative boundary class; the
     positive-genus restriction is explicit in Section2.4. Theorem1.2
     supplies the comparison count in its stated scope. D50 proves
     its required pants count directly, including every proper J,
     without extending that theorem past its boundary hypotheses.
     Searches for a ready-made full peripheral pronilpotent lifting
     result supplied no exact theorem used here. Reopened Marin and
     Nakamura--Tsunogai--Yasuda sources retain their already recorded
     GT/Galois scopes; no CM transfer is inferred from the reread.


134. D51 and D52 complete root proof reads PASS; geometry's complete
     independent reads PASS. The literal D51 basis, integral realization,
     characteristic full/pro-ell square and upper bound give dimension3.
     D52's two exact S3 inner corrections, normalized centralizer and
     filtration argument, pair/derivation sign, literal full modular lift,
     independent gamma line and degree-nine pentagon map give dimension2.
     The reviewed D52 draft is preserved before its two TeX-only repairs.

135. The final witness exporter adds only a direct cyclic-sum assertion
     and its two result fields. The original exporter and its output are
     preserved at their previously audited hashes. A fresh root replay
     checks every final identity, every old vector/map unchanged, and
     all42 printed integral D52 coefficients. PASS0.551s. D50--D52 are
     accepted and integrated; Tasks D1/D2 and PartD are complete. All
     previous open passages and coverage rows are preserved verbatim.
     E2/E3 remain the two active global tasks.


136. Root opened the full primary Herfort--Ribes1985 article, Section4,
     printed page159, TheoremB-prime and its proof (turn547view0).
     Applied to the actual C2 and C3 factors, it gives the pure-frame
     uniqueness used in E58; no centralizer assertion is inferred
     solely from a finite quotient.

137. Root read every line of E58 and its standard-library certificate.
     The complete relative source lift, actual local fibre product,
     pro-two centralizer lift, exact full cusp normalization and
     positive E1 signs all pass. Arithmetic's independent full review
     also passes. Root's isolated replay passes in0.206s, reproduces
     every mathematical JSON field, and preserves all9 protected
     files. E58 is integrated and E2 is proved. The exact E9 exclusion
     together with E58 refutes the earlier twelve-representative
     equivalence. E3 is the remaining global task.


138. Fresh primary-source check: Goto--Ishii, arXiv:2610.21052v1,
     https://arxiv.org/pdf/2610.21052, Introduction and Theorem 1.1
     (= Corollary 5.5), read directly (turn550view0, reopened turn559view1).
     Its formula evaluates elliptic Soule characters on local reciprocity
     images, for split primes p at least 5 and the stated positive index
     pairs. The checked source domain is the specified local Galois image.
     No full-GT comparison is inferred from that formula.

139. Nakamura--Tsunogai, Harmonic equations, RIMS1267 (2002),197--208,
     primary PDF 1267-18.pdf reopened (turn550view1). Theorems1--2 on
     printed199 state the harmonic/equianharmonic identities for G_Q.
     The full-GT accessory cocycles and the specified Galois equations
     retain their actual domains. This read supplies no proved transfer
     of those equations to every full-GT element.

140. Basualdo Bonatto--Robertson, arXiv:2606.01466v2 (8 October 2026),
     https://arxiv.org/pdf/2606.01466, primary PDF opened by root
     (turn559view0; exact proposition/theorem searches turn560view0--3).
     Proposition4.7 identifies the genus-zero object-fixing endomorphisms
     with the GT monoid. Definition4.8 imposes the two NS relations;
     Theorem4.9 maps that specified submonoid into the full modular-operad
     endomorphisms and proves compatibility with the genus-zero restriction.
     Its genus-one sewing verification invokes NS Claim8.3 relation6AS.
     The exact finite consequence of this relation is being investigated;
     no extension of the stated domain is used in the accepted manuscript.


141. Root opened Collas, arXiv:2603.02848v2, primary PDF, Introduction,
     contents and Theorem1.1 (turn565view0). Its full Section4 was not
     read in that visit. This lead supplies no asserted full-GT CM result.

142. Root opened Hoshi--Mochizuki--Tsujimura, JMS Univ Tokyo32(2025),
     pp.1--125, https://www.ms.u-tokyo.ac.jp/journal/32-1-1.pdf,
     Introduction TheoremsA--C and the COF/RGC/ArBC/QAA/AA hypotheses
     (turn565view1). The stated Belyi/Kummer compatibility data are retained;
     no assertion that every full-GT element satisfies them is used.

143. Root opened Boggi, arXiv:2011.15075v6 (22April2026), primary HTML
     and53-page PDF (turn587view0/1). Theorem6.7 and Corollary6.24 are
     read with the actual full profinite targets. Sections2.1/2.8 allow
     the annular-complement pants embedding, whose two boundary twists
     have the same image. The actual capping map in Proposition6.9
     retains one Weierstrass point. Lemma6.16's based uniqueness has
     the explicit identity/inner-twist alternatives. These particular
     proof issues, exact naturality conjugators and possible repair
     maps are preserved in DE_Boggi_v6_morphisms.md; no falsity of the
     global theorem is inferred. Geometry is checking the repair.

144. Root reopened NS newGT.pdf, Definition5.1 and proof of Claim8.3,
     relation(R-prime), author-PDF pp.17,33--34 (turn595view0/1).
     The actual h=beta-inverse and rho convention agrees exactly.
     The four A3 homomorphisms carry full braid central powers with
     coefficients2,-2,2,-2. RelationIV's subgroup domain is retained.
     Shpilrain's primary braids.pdf was opened at the Artin formula,
     TheoremA and its proof, pp.1--4 (turn592view1,turn595view2).
     The representation(k=1) is exactly the certificate convention.

145. E59 root complete proof/program read and isolated replay PASS,
     322.028seconds. Every mathematical JSON and NPZ array agrees;
     all144 generation certificates fully replayed,691 protected
     originals unchanged. All512 corrections over each24 retained
     G6 points give4 gentle and2 pentagon values, with complete
     actual source/target generation and positive CM gauges.

146. E61 root complete proof/program read and isolated replay PASS,
     2.854seconds. JSON and stdout are byte-identical; all7 protected
     originals unchanged. The signed cubic and exact rho comparison,
     everymod3 frame,16 braid identities,24 framed words, fourcentral
     carries and the affine sewing formula all pass. E59/E61 are
     integrated; the sole unresolved task remains E3.

147. Root reopened Lochak--Nakamura--Schneps, arXiv:2602.12462v1,
     https://arxiv.org/pdf/2602.12462 (turn600view0). Theorem1.1
     gives the stated full-GT actions on the unpunctured and one-puncture
     groups. The Introduction and Section8 retain the additional
     compatibility problem for cutting/sewing and the two-puncture
     construction. No compatibility absent from that statement is used.

148. Root opened Boggi--Funar, Automorphisms of procongruence curve
     and pants complexes, primary author PDF
     https://www-fourier.univ-grenoble-alpes.fr/~funar/bf_final.pdf
     (turn605view1,turn606view2,turn612view1). Theorem4.14 on printed
     pp.22--23 explicitly takes an open subgroup. Its proof uses the
     resulting finite-index images. This supplies the exact hypothesis
     check in the audit of Boggi v6 Lemma6.16; no conclusion about the
     truth value of the global tower theorem is inferred from that issue.

149. Root opened Endo--Kamada, Counting Dirac braid relators and
     hyperelliptic Lefschetz fibrations, arXiv:1508.07687v2,
     https://arxiv.org/pdf/1508.07687 (turn606view0,turn608view1,
     turn612view0). The version-specific PDF URL first returned a
     DisabledError; the unversioned URL returned the visibly dated
     v2 PDF of5October2016. Theorems3.1--3.3, printed p.6, give the
     exact sphere braid, marked-sphere and hyperelliptic presentations.
     The central involution and its actual quotient map are retained
     on printed p.7. These data support the explicit hyperelliptic
     descent currently being checked, without a CM compatibility claim.

150. Root reopened NTY III's complete author-uploaded PDF
     (turn605view2), with Definition(1.1), printed p.432,
     Notation3.9 and Lemma3.10, printed p.441, Lemma4.6,
     printed p.443, and Proposition4.13, printed p.445
     (turn606view3/4,turn612view2). The g and h parameters are
     distinct defined factors. The actual Mordell triangle subgroup,
     its Ferrari kernel and the central Kummer path factor are retained.
     Proposition4.13 and Theorem4.16 have the stated Galois domain.
     The new exceptional B3 inclusion is being compared with the
     literal full-GT braid action without changing that domain.

151. Root complete proof/program read of frozen E62 PASS. All new
     mathematical programs and the replay driver were read, including
     the complete class-two multiplication and both central norm
     equations. The4-to2 strict projection to the GL-only final values
     is proved using the actual block map. The full isolated replay
     is running in research/root_E62_replay; no replay success is
     claimed in this entry before its final comparison completes.

152. Root complete isolated replay of the frozen3.A6 source PASS:
     all873463 lifted source relations,720615 C relations,10 original
     C links and every saved word replay. All11 mathematical JSON,
     7 NPZ and6 exact binary outputs agree. The final wrapper initially
     compared discovery-history stdout fields with replay-history fields
     and stopped; both original logs remain unchanged. The separate
     audit_a6_triple_source_compare_root.py checks the exact differing
     scan counts and selected-index lists, both literal original
     generators in the identical complete certificates, and all final
     mathematical fields. All121 protected original files are unchanged.
     Batch command time1354.643seconds; comparison1.841seconds.


153. E62 full isolated root replay PASS,651.328seconds. All1011 complete
     certificates, including960 generation and40 coordinate certificates,
     were replayed. Every mathematical JSON field and NPZ array agrees,
     and all4183 protected files are unchanged. Root's complete proof
     and all-new-program reads and the independent profinite_images
     review pass. The actual common source, full class-two fibres,
     complete G6 comparison and strict4-to2 GL final projection are
     integrated. E3 remains the sole Open task.

154. Root full read of the exact hyperelliptic/Mordell note and its
     faithful Artin program passed. The isolated replay reproduced
     all45 braid comparisons and every integral genus-two matrix check
     byte-for-byte, with all four protected originals unchanged.
     The separate quartic note, its213-line program and the complete
     E64 fragment were then read in full. The isolated quartic replay
     passed in1.562seconds, with all14 braid equations, the exact
     free-by-cyclic map, both CM tables and every saved covariance
     reproduced byte-for-byte. All five original hashes were unchanged.
     The two orbifold discrepancy characters remain explicitly
     unevaluated on full GT.

155. Root reopened Marin's complete primary author PDF,13June2007,
     https://www.lamfa.u-picardie.fr/marin/arts/gtrig.pdf
     (turn623view0,turn624view0), Section4, printed pp.7--8,
     Lemmas4.1--4.3 and the displayed braid equations. They give the
     exact normalized intertwiner used in E65. In the abelian branch
     the displayed system gives v=lambda; the proof's printed v=1
     is a typo. The nonabelian branch and our explicit covariance
     matrix are unchanged by that correction. Root's complete E65
     proof and finite-program reads pass, including arbitrary-
     multiplier conjugation, signed transport, compact continuity,
     and the explicit F -> F sigma^-1 -> (F sigma^-1)^3 comparison
     to the retained matrix fibre. Its full-GT character is not
     assigned a value by this reduction.

156. Root opened Margalit--Winarski's complete author research PDF,
     https://margalit.droppages.net/papers/bh.pdf (turn625view0).
     Section4 gives the genus-two hyperelliptic presentation and deck
     map. Section6, printed p.9, explicitly gives the two-boundary
     torus group B4 x Z, with the extra factor the single-boundary
     twist. E64 retains that factor, both boundary images, and the
     three-chain relation in the actual sewing map; it uses the
     separately checked profinite stabilizer sequence for completion.


157. E60 complete isolated root continuation replay PASS,346.65seconds.
     The full signed base has1159255 checked relations; all79 new
     signed words give the complete previous kernel by an invertible
     transition. All60 normal-form queries and all six target chains
     pass, with3144734 final target relations. All11 mathematical JSON,
     seven NPZ and four byte outputs agree, and all340 protected
     originals remain unchanged. Full source, bridge, compactness and
     target proof/program reads pass independently. E60 is integrated.

158. E65 isolated root replay PASS,0.038363seconds. Every mathematical
     JSON field is identical and all nine protected originals remain
     unchanged. E64's final seven-page standalone layout also passes,
     with no source edits after root's proof and both-program replays.
     E60,E64,E65 and three opened E64 references are integrated with
     complete prior active passages preserved in the named checkpoint09
     acceptance record. E3 remains Open, now with the exact restricted
     quadratic character and its actual matrix-fibre comparison.

159. The first checkpoint09 integrated build completes with477 pages,
     zero overfull boxes and no undefined references or citations.
     The exact build and sources are preserved in checkpoint09_first_confirmed.
     Root rendered408 sampled pages, verified333 PNGs byte-identical
     to the prior approved sample, and actually viewed all seven new
     contact panels plus fourteen individual pages at full resolution.
     The new proofs, E3 table continuations and bibliography have no
     observed clipping, equation-tag collision or margin overflow.
     The approved PDF SHA256 is c9d4ced12ecdfaf52de6b535f4cdc008fdcad4c54833e6e1a72cec945a324cbb.

160. Root read the entire K3 source proof, all three new programs and
     the isolated replay driver. Root execution PASS7.600413seconds:
     every mathematical JSON field, every NPZ array and all five
     complete word-DAG/Schreier certificates agree; all64 protected
     originals are unchanged. The actual full eighteen-coordinate
     correction image has order2^27*3 and derived order2^27.
     Its abelianization C3 proves direct-product independence from
     E62's binary correction on the identical N_B-prime source.
     No equation is assigned to an additional based coordinate.

161. Root read the entire new orbifold-sign note and program.
     Isolated execution PASS0.973416seconds, with byte-identical JSON
     and stdout and all six originals unchanged. The actual Mordell
     order54 quotient forces positive original-orbifold sign. The
     actual Gaussian order36 quotient gives its parity as v2 squared
     for the literal f(x,y) translation. Two printed N_B-prime words
     retain the old G6 source and independently generate both Gaussian
     translations while killing the Mordell coordinate. The discrepancy
     characters retain their stated full-GT domain and remain unevaluated.

162. Root searched both engines for profinite GT abelianization and
     quadratic characters. Opened the editor-hosted complete primary
     book https://www.math.uchicago.edu/~farb/papers/mcgbook.pdf
     (turn635view0, turn636view0), Lochak--Schneps Question1.2,
     printedp178/PDFp185. The cyclotomic abelianization assertion is
     posed there as a question. Reopened the primary Harbater--Schneps
     author PDF https://webusers.imj-prg.fr/~leila.schneps/HS.pdf
     (turn635view1, turn636view1), Section3.2 Question1, printedp31,
     which poses the same derived-subgroup question through its exact
     Out-sharp-five isomorphism. Neither passage is used as a theorem.
     Opened Collas's full author PDF
     https://collas.perso.math.cnrs.fr/documents/Collas-Genus1_gt_action.pdf
     (turn635view2), Definition1.1 and TheoremsA/B: the source is I-Gamma
     with the additional III-prime and IV equations. The search gives
     no usable vanishing result for the particular Delta under study;
     no global nonexistence of such a result is claimed.


163. The 2.A6 target's five complete derived chains pass a fresh complete
     replay, with3091439 final relations and indices1,2,6,96,96.
     Independent DAG substitutions and the specified S_L map give exact
     quotient orders96,48,16,1,1. The terminal group is perfect and is
     the entire kernel of this quotient. Profinite peer read of the full
     target proof and five programs passes. The initial incorrect kernel
     docstring and the failed registration-ID lookup are separately
     preserved with their exact fixes. Source integration awaits its
     final common-quotient proof.

164. E66 root isolated replay PASS20.301921seconds: four complete
     certificates, all mathematical JSON/NPZ values and288 same-word
     witnesses agree, with76 original files unchanged. Root and geometry
     full proof/program reads pass. The E17 origin correction is explicit.

165. E67 root isolated replay PASS285.135576seconds: all four programs,
     mathematical JSON values and every exported NPZ array agree. Both
     actual origin lists and all correction words are retained. Regenerated
     timing-dependent provenance hashes are separately checked. Root and
     arithmetic full proof/program reads pass;20 originals are unchanged.

166. Exact binary-overlap probes are retained under
     e_a6_double_binary_overlap_probe_root and e_a6_double_E62_word_probe_root.
     The stable ternary six-space acts trivially on the old binary six-space;
     its commutator rank is0, while the new central binary pairing has rank3.
     Of125 named old-J-identity N words, only11 have E62 values in its
     N-prime image. None of the six chosen module lifts has such a value;
     all15 pair commutators do. Thus these particular literal N words cannot
     be substituted for unspecified deep N-prime preimages. The full binary
     comparison remains active; no whole-fibre inference uses this probe.


167. E68 full root and geometry proof/program reads PASS. Root isolated
     replay PASS23.535915seconds: all four complete certificates, all
     mathematical JSON/NPZ values and1152 literal common words agree;
     all88 originals remain unchanged. The exact common quotient is
     trivial, giving the full E66-by-E67 product on the same N_B-prime.
     The actual E17 origin maps and full kernel-coset fibres are retained.

168. Root and profinite prove the exact joint2.A6/3.A6 target over the
     actual old signed-A6 target. The triple relative kernel maps onto
     ASL2(F3), with kernel3^105; the affine abelianization has order3.
     It has no nontrivial two-group quotient, while the double relative
     kernel is elementary abelian2^151. Goursat gives the full fibre
     product, order2^5573^2715^1177^8 11^3 13^2. The specified solvable
     quotient remains order20736, with a perfect kernel proved by its
     two- and three-primary abelianization bounds. Actual T23, uniform
     and Hurwitz arrows are retained. New target fragment tagsE63.36--38
     and the exact order certificate pass peer read.

169. Additional primary-source scope check: Nakamura--Tsunogai,
     Harmonic equations in the Grothendieck--Teichmuller group,
     RIMS Kokyuroku1267(2002),197--208, opened at
     https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1267-18.pdf.
     Theorems1--2 and their corollary explicitly concern the Galois image;
     the opening discussion leaves their full-GT subgroup comparison
     undecided. Section5 records the full-GT cyclic Kummer cocycles and
     a further hypothesis for comparison with the accessory cocycle.
     These formulas are retained as source comparisons, not used as a
     full-GT vanishing theorem. Chinburg's ICTS January2024 slides,
     https://www.icts.res.in/sites/default/files/seminar%20doc%20files/Ted%20Chinburg%2004.01.2024.pdf,
     slides20--23 were opened as well: the modular-family representation
     extension carries explicit subgroup-stabilization and linear-lift
     conditions. It does not assign the remaining character here.


170. E63 full source proof, both root target fragments and every new
     mathematical program/collector/replay pass root and arithmetic read.
     Complete isolated root replay PASS1633.604seconds: all four new full
     presentation calculations, all literal words and all mathematical
     JSON/NPZ values agree;665 original files are unchanged and
     226 exact routed input hashes are explicitly validated.
     The signed common quotient is the actual9331200000-element group;
     the full relative correction kernel is125-dimensional, with the
     perfect122-dimensional bridge and all three stable characters retained.
     The exact source and target scopes are integrated as E63. E3 is open.

171. Root's enlarged A6/A5/E62 actual base is a15774-point permutation
     action. All1279851 final Schreier relations pass;407
     strong words and13526 DAG nodes are retained. The subsequent full
     signed/binary collector and independent literal replay determine
     the exact additional common source. Earlier finite probes retain
     only their literal N-word values, with no unsupported N-prime claim.

172. E69 complete root and arithmetic proof/program reads PASS. Root
     isolated replay PASS12.548128seconds: all four mathematical outputs,
     every array value, shape and dtype, and all3456 actual common words
     agree;34 protected originals remain unchanged. The Gaussian central
     quotient has correction image M times Heis3 cubed and its actual
     E67 projection is precisely its abelianization. The same-map Goursat
     argument gives the full E66 product, with all three central lifts
     over each old combination and exact word-kernel fibres. E3 remains
     open.


173. E70 complete root proof/four-program and independent profinite proof
     reads PASS. Root isolated replay PASS49.265512seconds: all70
     protected originals unchanged, every mathematical field and array
     exact, all six complete Schreier inputs/binaries byte-identical and
     independently replayed. The complete Gaussian pro-three source,
     all12 abelian characters, full E66/Mordell product and compatible
     lifts of every3456 E69 frame are proved through their actual maps.

174. E71 complete root and geometry proof/nine-program reads PASS.
     Root complete isolated replay PASS538.340874seconds; all six
     complete certificates and18432 full-source words agree, with
     131 originals protected. The actual
     full K6-intersect-F-prime domain is obtained through6ker(e), retaining
     its index12 exponent image. The extra quotient is C4 via c2/6 mod4.
     All1152 retained values admit all16 coefficient lifts; the finite
     simultaneous stabilizer is trivial and full word fibres are given.

175. E72 full root proof/program read and isolated replay
     PASS0.800947seconds, with16 originals unchanged. The two
     explicit integral basis maps identify every genus-three homology
     evaluation with the three retained genus-two evaluations, including
     their exact scalar characters and all90 induced transition maps.
     Thus this homology enlargement has the stated old source kernel.
     The nonlinear Wajnryb source is retained as a separate next route.


176. E73 complete root and geometry proof/four-program reads PASS.
     Root isolated replay PASS 27.431729 seconds, all 73 originals
     unchanged, every mathematical output and array exact, all six full
     H-certificate inputs/binaries byte-identical and independently replayed.
     The enlarged source evaluates all 1279851 relations and has binary
     relative rank 163. Its old-J/E62 identity kernel is the retained
     122-dimensional bridge kernel. The exact N-prime descent gives the
     graph of six explicit masks over C62, with independent V6. The full
     I image is V6 times the order-2^15 H-residual intersection, proved
     by nested compact fibres and a matching full-H upper comparison.
     Each fixed J2 value has an entire 64-element E62 coset. Individual
     prescribed pentagon targets remain to be evaluated in these cosets.
