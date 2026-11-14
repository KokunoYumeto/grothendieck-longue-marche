# Independent audit of C.74

**Result: PASS.** I read the full current proof, metadata and producer,
reread the spiral estimate in C.72 and the filled-hull comparison in C.70,
and reran the producer. All **41 exact checks** pass. Captured output is
`work/part_a/c74_audit_stdout.txt`. The statement's final wording is
"coordinate centralizer homotopy"; no mathematical correction is needed.

## Loop and full centralizer

The displayed spiral map and inverse are actual inverse plane/interior-disk
coordinates. The C.72 estimate applies to a point-dependent displacement
as well as to a constant translation, provided its norm has the stated
uniform bound. Each of the three paths, its inverse, and the scaled-amplitude
contraction has a common bound. The forward and inverse families therefore
extend jointly over the original circle, fixing it pointwise.

The first two loop paths generate every real horizontal and vertical
translation. Thus the generated group is transitive. An arbitrary interior
homeomorphism commuting with both translation groups is a translation by
its value at the origin. Commutation with the third path forces
psi(t+b)=psi(t); evaluating at zero gives b=0 because the bump has its
unique maximum at zero. This proves the full centralizer equality, including
the exclusion of orientation-reversing candidates. Evaluation, compact-open
continuity and bounded translation parameters prove its exact topology,
closedness, freeness and properness.

## Actual section change and midpoint

The two principal coordinates have precisely the stated section-change
map H(s,t)=(s-t^3,t) and inverse. Both give the same labelled horizontal
operator action. Conjugating the original vertical path through this map
gives the displayed cubic shear. Its coordinate interpolation has vertical
coordinate t+ra and first-coordinate coefficient one, so it is a jointly
continuous family of interior homeomorphisms, with continuous inverses.
The other two loop segments and the joins have the same property.

The exact expansion back in the original plane is
(w+3r(1-r)a^2t+r(1-r^2)a^3,t+ra). The midpoint and its given inverse check
in both orders. This compares the actual maps under the specified morphism;
it does not assume a section change has any boundary extension.

## Original boundary and compact-word obstruction

For each original boundary point, the two exponential-radius sequences
have exactly the required limiting spiral angle. The horizontal image has
bounded displacement. The vertical image factors exactly as
(S_n+1/2)(3/4,1), giving angular difference
log(5/4)-arctan(3/4). The integral inequalities give a value strictly between
-pi/2 and -23/100, so the two limits are distinct without approximation.
This proves failure of continuity at every original boundary point.

For any compact P in the actual boundary-fixed disk group and finite N,
the product family P^N is compact. Joint evaluation continuity gives uniform
convergence of its images of the vertical sequence to the original boundary
point. C.70's filled hull lies in the Euclidean convex hull; hence those
filled hulls converge into arbitrarily small convex balls at that same
point. The explicit midpoint images have the different limit, contradicting
the proposed inclusion. This is the asserted quantification over every
compact P and every finite word length N, without any unproved size estimate
on the candidate map.

The original amplitude-scaled contraction is still valid and commutes with
the same actual R-action. The result therefore establishes the precise
failure of the specified coordinate interpolation and its proposed compact
filled-word bound. It does not assert a nonzero centralizer fundamental
group or a failure of every possible boundary-relative contraction.

No new external source theorem is required for this elementary explicit
construction. Its cited C.72 estimate and C.70 convex-hull argument were
read and checked in their accepted source files.
