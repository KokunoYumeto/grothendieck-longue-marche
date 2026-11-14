# Root review of F.48: henselian Abhyankar valuations

**Date:** 14 November2026. **Verdict:** PASS for the exact seven-section
candidate `audit/F_Abhyankar_valuation_obstruction_candidate.md`.
Root read every section and the complete independent review
`audit/F_Abhyankar_finite_field_review.md`. The statement is a necessary
obstruction for F.9; it supplies no converse or transcendence-defect claim.

## Exact valuation and closure calculation

Rational independence of the positive basis values gives a unique
least-valued monomial in every polynomial. This proves multiplicativity,
algebraic independence, the value lattice, and the residue field F of the
rational base. The immediate henselization therefore has the same lattice
and residue field. Algebraic constants have valuation zero by the minimal-
polynomial least-term argument.

For a finite constant field F', dividing a linear combination by a coefficient
of least value and reducing proves the formula v(sum e_i h_i)=min v(h_i).
Thus the claimed degree, unchanged value group and exact residue F' are all
justified before a linear-disjointness assertion is used. The n^r radical
monomials have distinct value classes modulo the old lattice; their linear
independence matches the elementary degree upper bound. Every element is
expressed in that basis, so the value group is exactly (1/n)Gamma_0 and the
residue field is exactly F'. In a value-zero expansion only the zero exponent
class can be the least-valued term.

The union of these finite radical/constant fields is an algebraic extension
of a henselian field and hence henselian. Its value group is divisible and
its residue field is the algebraic closure of F. Equicharacteristic zero is
used precisely in the cited algebraic-closedness criterion. This identifies
the entire algebraic closure, with no multivariate Puiseux or completeness
assumption. The asserted split Galois group and its continuity follow on
these actual finite field bases.

## Automorphism, compatible roots and centralization

Substitution t1 -> t1+t1^2 preserves the value of every monomial and hence
of every polynomial and fraction, for an arbitrary order on the free lattice.
The unique positive-valued root r1 of X^2+X-t1 has the same value as t1 and
ratio r1/t1 of residue one, so it supplies a second valuation-preserving
embedding. Henselization universality extends both embeddings. Their two
composites agree with the identity on the rational base by uniqueness of
the positive-valued simple root; the same universal property then makes
them identity maps of the henselization. Thus this is an automorphism,
not merely a self-embedding.

The roots beta_n of 1+t1 are uniquely selected by residue one. Uniqueness
gives every divisibility compatibility. The established n^r field basis
makes the maps on radical generators well-defined, and surjectivity follows
because the images contain the base, constants and every radical generator.
For arbitrary g in G_H, commutation holds on H, algebraic constants and all
parameter roots; g fixes beta_n because it belongs to H. These generators
exhaust the closure. The proof therefore centralizes all of G_H, including
all inertia factors, without applying an abstract automorphism termwise to
an infinite formal series.

F.40 gives the relative closed-point-preserving full-topos counterexample.
Values at 1,2,t1 exclude an algebraic monomial. F.32's contrapositive then
excludes every algebraic extension, with the correct direction of inference.

## Intrinsic Abhyankar reduction and source check

The coefficient field is supplied by the complete F.47 argument. Choose a
positive rational basis in the actual value group and elements realizing
it. Unique least monomials give a rational-function subfield with the
prescribed monomial valuation. The exact Abhyankar equality makes the
ambient K algebraic over it. Henselization universality embeds its
henselization into K, and K remains algebraic over the embedded field.
All hypotheses needed for the negative conclusion have therefore been
checked. Rational rank and order rank are correctly kept distinct.

Root independently reopened the primary author PDF of Aschenbrenner,
van den Dries, and van der Hoeven (2017),
https://www.math.ucla.edu/~matthias/pdf/mt.pdf. In addition to the
coefficient-field and universal-property passages opened for F.47,
we read Proposition3.3.11(ii), printedp119 (`turn875view0`),
Corollary3.3.22, printedp124 (`turn875view1`), and the complete
henselization universal-property proof through Corollary3.3.26,
printedp125 (`turn875view2`). They have exactly the arbitrary-rank,
equicharacteristic-zero hypotheses used here.

**Integration approved.** The counterexample construction and the full
finite-transcendence Abhyankar obstruction are valid in the candidate's
stated scope. No new numerical computation is needed for the all-degree
Hensel uniqueness or valuation-independence proofs.

## Integrated-source readback

Root subsequently read the entire integrated
`sections/F_Abhyankar_valuation_obstruction_extension.tex`, including all
fifteen equation tags and the intrinsic final reduction. It preserves the
reviewed statement and proofs, including the no-transcendence-defect
limitation. The static record identifies its SHA256 as
`3baaf0fcffad6c5326355a0c66ed2bbc05227011673f3eaa76ec0675d01a9c89`.
The mathematical readback passes; the combined build and visual QA remain
separate later tasks.
