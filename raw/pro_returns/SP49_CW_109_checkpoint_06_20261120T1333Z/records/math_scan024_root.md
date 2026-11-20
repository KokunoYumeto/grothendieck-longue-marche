# Main-reader local checks: scan 024, cited p224 line 2

These checks were developed while the three readers independently inspected scan024, before their final reports. They use only the formula and question supplied for this page. They do not settle any ambiguous letter, index, cancellation or insertion in the scan. No external source was consulted.

## S024-Hom-presheaf-construction

The written formula has the form j_A(X)(a) = Hom(A/a, X), with the declared direction Cat to the presheaves on A. Under the ordinary small-category interpretation needed to make the displayed Hom a set of functors, this has the stated variance.

For an arrow u: a to a' in A, postcomposition gives u_*: A/a to A/a': it sends an object (b, v: b to a) to (b, uv: b to a') and leaves the underlying morphism in A unchanged. Precomposition with u_* sends a functor F: A/a' to X to F composed with u_*: A/a to X. Thus the displayed set-valued assignment is contravariant in a. Identities and composition follow directly from (v u)_* = v_* u_* and associativity of functor composition.

A functor G: X to Y acts by postcomposition, sending F to G F. This is covariant in X and commutes with the just-described precomposition in a. Consequently the displayed assignment defines a functor Cat to the presheaf category on A, subject to the ordinary size interpretation. No unmentioned size hypothesis is inserted into the transcription.

This is a bounded construction/variance check, not a proof of any absent surrounding statement on the cited page32 or224. It does not decide lowercase j versus uppercase J, or which old and live argument letters are visible.

## S024-slice-description-types

For a category B, the assignment x to B/x has x an object of B and outputs a category. On an arrow x to x' it acts by postcomposition B/x to B/x'. Its resulting type is B to Cat.

By contrast, substituting B for A in the preceding displayed construction gives j_B with type Cat to the presheaves on B; for a category X its value is the set-valued presheaf x to Hom(B/x, X). Therefore the bare category-valued assignment x to B/x is not the same typed construction as that displayed j_B. This explains a type-based reason for the writer's question, if the crowded inserted numerator and index are indeed B and the same convention is intended.

The original cited typescript is not present here, and the inserted numerator remains an ink question until adjudication. The check therefore does not claim a definitive correction of that absent typescript. It also does not justify restoring a question mark or changing the manuscript's wording.
