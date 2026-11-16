# Full-group A1 proof: root audit, 16 November 2026

The root read the full finite-cover fixed-r configuration proof, the
root-gerbe boundary comparison, and the conditional cuspidal separation
proof. All three research agents independently audited the finite-cover
and boundary arguments. The topos agent then made an additional adversarial
pass through every downstream step of the conditional separation proof.
The chain is accepted in this return as a proof, with no claim of priority.

## Exact quotient and finite-cover proof

The proper geometric quotient remains the entire prime-to-p surface group
Delta. Only the kernel relative to the proper quotient is replaced by its
maximal pro-r quotient, for one r distinct from p. The arithmetic quotient
remains the full G_k. Neither the full pro-p-prime configuration injection
nor a full pro-r replacement of the proper curve is used.

For each finite fiber quotient Q, its cuspidal image R is an r-group and
A=Q/R is a finite proper prime-to-p quotient. Pull back the configuration
space along C' times C', where C' is the A-cover of C. The punctures are
individually labeled deck graphs and the compact family is a product.
Its mod-r monodromy is an r-group of shears. The pro-r congruence kernel
in the automorphism group of the finitely generated free fiber is pro-r;
its faithful inner action proves fiber injection into the pro-r total
group. Compact subgroup topology gives finite quotient domination.
Normal cores through the A-squared cover yield r-by-prime-to-p total
quotients whose entire cuspidal image is an r-group. They therefore factor
through the specified relative quotient. All finite fiber quotients are
detected, giving injection in the whole group.

The center-free input was opened directly in Kochloukova--Zalesskii,
arXiv:1107.2331, Corollary 5.3, with the definition of their class including
free pro-r groups. Root retrieval: turn591view0 and turn592view1.
The proof of the finite automorphism-kernel assertion is included explicitly.

## Boundary and arithmetic transport

The primary attached SGA1 text, XIII Proposition 5.2, printed pages428--429,
was read at source lines25272 onward in smf_doc-math_3_01.tex. Its hypotheses
are a regular local scheme, a normal-crossing divisor, and a cover tamely
ramified along that divisor. The Kummer substitution using inertia orders
gives a unique finite etale extension on the whole chart. Thus the root
stack construction glues. Its target is the tame fundamental group and
hence the required geometrically prime-to-p quotient; it is not asserted
to capture arbitrary wild covers.

The gerbe boundary sequence is right exact with kernel the image of
inertia. Right exactness after geometric prime-to-p completion removes
the discarded geometric base kernel, while G_k is unchanged. Its image
in the cuspidal configuration quotient therefore has kernel a quotient
of Z_r(1). The actual puncture inertia is full Z_r: its product-of-
commutators word maps to an infinite-order central element in the pro-r
Heisenberg group. Fixed-r fiber injection and transverse multiplicity one
identify this with the global diagonal inertia. Comparing inertia and
the arithmetic point group identifies the actual cusp decomposition group
with the intersection with the diagonal boundary group.

A geometric conjugator gamma between the proper point sections lifts to
a geometric element d of the diagonal boundary. Conjugation by d transports
the two fibers and their cusps, inducing Inn(gamma) on the first proper
coordinate. An element e of the geometric target fiber projecting to
gamma^{-1} corrects this to identity. The resulting isomorphism has exactly
the hypotheses of the conditional separation criterion.

## Downstream checks

1. The same-prime retention lemma applies to every visible open subgroup,
   not only opens with r-group Galois closure. A normal-core construction
   makes the cuspidal image r-by-r and shows that every finite r-quotient
   kills the original discarded kernel. Compactification hence retains
   the complete compact r-adic H1 and the exact Frobenius Weil polynomial.
2. For all arithmetic opens containing the transported point section,
   source rational points force nonempty target rational-point sets.
   Their finite intersection property follows from subgroup intersections.
   A compatible point in the universal target quotient cover gives an
   actual target point section contained in the transported section;
   equality follows because both map isomorphically to G_k. Nonnormal
   opens and finite extensions of constants are included.
3. The finite exceptional set from Saidi--Tamagawa is used only to label
   the transported proper point at all but finitely many geometric points.
   No emptiness assumption or exceptional-coordinate reconstruction theorem
   is used. The central quotient has full Z_r(1) kernel and degree-one
   class. Its isomorphism multiplier is one. The difference cocycle has
   residues(+1,-1), and subtracting it from the function Kummer class
   gives a proper H1 class, hence a constant by Frobenius weights.
4. The self-normalizer of a rational proper point section permits removal
   of the conjugator's proper projection. Evaluation of the difference
   cocycle is consequently a coboundary. A nontrivial r-power root of unity
   in any finite residue field has a nonzero integral r-adic Kummer class,
   even if its first mod-r Kummer class vanishes. Surjectivity of a nonconstant
   function supplies such an evaluation outside the finite excluded set.

These checks prove universal A1 and its finitely generated field corollary.
They do not prove a universal relative-class-number witness, a supersingular
correspondence theorem, or a converse from arbitrary norm-module vectors
to rational points.

## Search and source conflict

Additional primary-source discovery searches used the phrases
"cuspidally pro" "injectivity" "finite", "prime-to-p" "point"
"injectivity" "finite fields", and "configuration" "cuspidal"
"exactness" fundamental group. These supplemented the earlier search
record. No priority is asserted. The disputed full configuration assertion
in the Mochizuki author versions and the scope of the Saidi--Tamagawa
cuspidal comparison are documented separately in source_conflict_review.md.
They are not inputs to this proof.
