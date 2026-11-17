# Independent complete review of B.106–B.107

Status: PASS, including the final angular collar and outer-source clarifications.
Reviewed by DE during the twenty-first hour. This is a review of the actual
source and its complete proof, not only of the displayed identities.

## Sources read

- `sections/b_free_swap_quotient.tex`, complete B.106 and B.107, including
  the final version with the angular-shrinking collar.
- `records/free_swap_quotient21.md` and
  `records/inner_critical_halfplane21.md`, both complete.
- `code/swap_quotient21.py` and the actual successful identity record;
  the preserved failed attempts are not counted as verification.
- `code/check_blaschke_collisions21.py` and
  `records/blaschke_collisions21.json`, complete.
- Herfort and Ribes (1985), Theorem B′ and the printed pp. 159–160 proof
  through Lemma 3, reopened independently at this use. The full-category
  free profinite product theorem applies; no prosolvable restriction is
  introduced. Existing bibliography key: `A_HR1985`.

## B.106: actual quotient, source, and completion

The invariant coordinates `(q,s)=(vw,v+w)` recover precisely the unordered
pair `{v,w}`. The removed diagonal makes the swap a free degree-two cover.
The projective `t` coordinate handles its poles correctly: the omitted
affine `s` point becomes `t=1`, the old `s=q+1` divisor becomes `t=-1`,
and the discriminant gives `q t^2=1`. At `t=infinity` the alternative
chart has `b^2=(q-1)/q`, so the coordinate formula has not added a branch.
The four A graphs and their literal F images are exactly `±T_u(q)`.
Thus both directions of the open-surface identification hold.

The collision factorizations account for all graph/old-boundary pairs.
Same-sign and old-boundary collisions lie over deleted fifth roots.
The remaining opposite-sign values are exactly the two displayed roots.
For equal indices they yield the four distinct outer `alpha_u` and the
four distinct inner `beta_u=1/conjugate(alpha_u)`. Both fixed sources
therefore have ten punctures. The selected source has the actual
connected unramified double cover `sqrt(1-q)`, with nontrivial monodromy
around the omitted point 1, and has rank 19.

The based two-coset proof is valid without source injectivity. The source
cover gives both `I_Q intersect Pi_Z=I_Z` and surjectivity of the source
onto the covering group. A fixed element in the other coset is moved into
the index-two subgroup by a fixed source element. The completed argument
uses only finite-index induced topology and compact images of the actual
completed source groups. It does not replace the completion of an
infinite-index image by its ambient closure.

## B.107: the complete inner critical region

The exact norm identity proves `|1/T_u(q)|<1` throughout the punctured
unit disk, including projective poles of `T_u`. The two branch punctures
also have modulus greater than 1. No inner critical fiber is deleted.
The inside piece is a product and contracts equivariantly to the selected
fixed section `t=0`.

The final explicit collar is safe. With `m<1` and
`delta=(1-m)/4`, every moving puncture has modulus at least `1/m`, and
`1/m>1+delta`. The condition

    |r-1| < delta(q) |sin(theta)|,  theta not in pi Z,

produces two components, exchanged by `t -> -t`. The angular shrink is
essential: it prevents a thickened annulus from reconnecting through
the deleted points `±1`. The inside plus collar remains equivariantly
star-shaped to zero. The Borel intersection has the homotopy type of
the base. The outside group need not be computed. The boundary section
`t=i` and projection to `q` supply an actual edge injection and
retraction. Thus the stated retracted amalgam is genuinely based.

The discrete centralizer follows from the ordinary reduced-word normal
form, since the cone involution is not in the edge group. The profinite
argument is also complete. Retraction-stable finite-index normal
subgroups are cofinal; each quotient has the displayed form
`(C2*K_N) semidirect D_N`. Its open free-product subgroup has full
profinite completion, and Herfort–Ribes B′ gives the cone centralizer.
Every finite quotient of the original amalgam factors through one such
quotient. The `D_N` system induces the full topology of C, because
`r^-1(L)` realizes every finite-index normal L in C. Compatible cone
centralizers therefore recover exactly `C-hat times C2`. Neither
residual finiteness of the unknown outside group nor a general proper
profinite amalgam theorem is assumed.

Over the inner source the square root `sqrt(1-q)` is single-valued.
Its inverse image consequently has two components. The proof uses the
component through the literal base point and only intersection with
the actual open index-two subgroup. It correctly avoids the global
surjective-source-monodromy converse. Projection to the base proves
source injection and full induced topology.

The final outer-mirror wording is correct: reciprocal conjugation gives
the other section `D_infinity` in Q, based there, and its lift is the
`F sigma` source. It does not prove the selected F-source equality in
the outer part of Z. No global amalgam across the q boundary has been
inferred from either regional result.

## Genuine independent algebra certificates

1. `verify_swap_blaschke_independent21.py`, adjacent `.out/.err`, and
   `swap_blaschke_independent_review21.json`: 26 exact identities PASS.
   The independent symbolic derivation includes the based V4 action,
   both coordinate inverses, all collision identities, the norm
   identity, the cover charts, and the half-plane affine formula.
   It imports no root producer.
2. `verify_quotient_collisions_independent21.py`, adjacent `.out/.err`,
   and `quotient_collisions_independent_review21.json`: PASS using a
   separate four-coordinate Fraction arithmetic implementation of
   `Q[x]/(x^4+x^3+x^2+x+1)`. Inverses use rational Gaussian
   elimination; signs use exact comparisons in `Q(sqrt(5))`.

The twenty root candidates have exactly two identifications:

    alpha_(1,4)=beta_(2,3),   beta_(1,4)=alpha_(2,3).

There are exactly 18 distinct additional base values: nine inner and
nine outer. Counting the two physical opposite-sign nodes for each
unequal pair and one for each equal pair gives 16 quotient nodes in
each region, 32 total. No value is zero or a fifth root, and none lies
on the unit circle. These counts remain supporting research data;
they are not an additional fixed-lifting theorem.

## Reference

Herfort, W., & Ribes, L. (1985). Torsion elements and centralizers in
free products of profinite groups. *Journal für die reine und angewandte
Mathematik, 358*, 155–161. https://doi.org/10.1515/crll.1985.358.155

The main global fixed-source and subsequent joint-source questions
remain Open. This review does not promote regional boundary maps to
injections after the actual critical fillings.
