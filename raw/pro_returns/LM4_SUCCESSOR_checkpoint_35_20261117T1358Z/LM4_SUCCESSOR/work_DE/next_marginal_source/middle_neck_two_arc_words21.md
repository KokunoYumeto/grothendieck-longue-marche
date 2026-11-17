# Exact based words for the first mixed neck's two vanishing arcs

Research only, checkpoint21. This uses CE's actual radial-arc proof
and its exact physical ordering, together with an independent planar
cut calculation. The words are in a newly specified geometric basis
of the natural K; they are not silently identified with an earlier
21-strand marking.

## 1. Actual geometry retained

For k=1 use `Q=x+i(c_1+c_2)/2`. CE proves that the actual A2/B1
vanishing arc is the radial segment through

    x+i(c_1-c_2)/2.

The other three selected punctures stay on the opposite side of
this segment for `x>0`; the `x<0` picture is its reflection. In the
boundary fiber their increasing imaginary order is

    A2, A4, A3, upper branch, B1.

The disjoint rational bounds are respectively `(0.95,0.96)`,
`(1.53,1.55)`, `(2.12,2.14)`, `(2.16,2.17)`, `(2.75,2.76)`.
See CE's genuine `first_mixed_neck_arc.json` and its producer.
Thus the actual inner arc goes to the right of the three middle
punctures in Z, and the actual outer arc goes to their left.

## 2. One explicit based geometric free basis

Rotate by `z=-i Z`. This preserves orientation and makes the five
punctures real in the displayed order. The inner arc is below the
real axis and the outer arc is above it. An increasing homeomorphism
of the real axis, extended preserving its two half-planes, moves the
five points to 1,2,3,4,5 without changing either arc class.

Use far basepoint 6 and downward cuts from these five points.
The positive meridian `x_j` crosses the j-th downward cut once
from left to right. The common connector goes from 6 to `6+i`,
then to `1/2+i`, then to `p=1/2`. All its cut crossings vanish.
In the actual Z half-plane this is a connector from the chosen high
imaginary basepoint, with all paths staying away from the retained
boundary point Z=0. The model point p is positive, not zero.

The first meridian is `a=x_1`. For the outer/upper arc, run from p
above the intermediate punctures to a small positive loop at 5.
This gives `b_out=x_5`. For the inner/lower arc, run from p below
all four initial points before making the same small positive loop
at 5. The prefix cut word is `x_1 x_2 x_3 x_4`; hence

    b_in=(x_1 x_2 x_3 x_4) x_5 (x_1 x_2 x_3 x_4)^-1.

These two whiskered pairs are the boundaries of thin neighborhoods
of the respective arc trees. All small loops are counterclockwise.
No independent conjugation of one peripheral is discarded.

## 3. The two actual relations and their normalization

In this single based K marking the actual node relations are the
normal closures of

    r_out=[x_1,x_5],
    r_in=[x_1,(x_1 x_2 x_3 x_4) x_5 (x_1 x_2 x_3 x_4)^-1].

Conjugating the entire second relator by `x_1^-1` gives

    x_1^-1 r_in x_1 = [x_1, P x_5 P^-1],
    P=x_2 x_3 x_4.

This normalization preserves its actual normal-closure relation;
it is not an assertion that the two commutators are the same word.
Equivalently, after choosing the inner pair as `(a,b)`, the outer
relation involves the conjugate by `P^-1`. Both conventions encode
the same two-sided incidence with the three middle punctures.

The common regular-neck transport followed by the chosen quadrant
paths determines the displayed arc classes. Further choices of the
single common connector conjugate both relations together. The
normalization above records the extra `x_1` conjugation explicitly.

## 4. Genuine exact certificate and limit

`check_middle_neck_arc_words21.py` uses Fraction coordinates for all
segments, checks that no segment or endpoint hits a puncture or an
unhandled cut, verifies the positive square areas, and reads every
crossing with the calibrated downward-cut sign rule. Its actual
stdout/stderr and `middle_neck_arc_words21.json` retain the complete
paths, all events, raw meridians, raw commutators, and the literal
free reduction giving the normalized inner word. The run passes.

This establishes the two short based relation words. It does not
identify the full regional kernels with their normal closures,
compute the pushout across all necks, or prove a global centralizer
or fixed-source theorem.
