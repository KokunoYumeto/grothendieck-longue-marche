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
