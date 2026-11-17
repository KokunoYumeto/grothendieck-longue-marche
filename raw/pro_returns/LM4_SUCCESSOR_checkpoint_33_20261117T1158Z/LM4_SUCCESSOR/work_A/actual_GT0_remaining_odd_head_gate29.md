# The remaining odd cyclic heads after the actual dyadic comparison

Checkpoint29 separate research. This records a precise further reduction of the actual coefficient gate; it supplies no missing odd-head identity and no nonlinear cusp conclusion. The reviewed A87/A88 and hexagon-defect note remain unchanged.

Retain the actual units a=a_reg and d=d_alpha and the exact full-ring identity Theta_u D_a=1. Now assume alpha is a full-GT involution, so the complete proof in `actual_GT0_hexagon_Alexander_defect29.md` gives a_2=d_2. This extra hypothesis is essential to the reduction below.

For every odd positive integer n, write Lambda_n=F2[C_n] and denote projection by a subscript n. Then

\[
(\Theta_uD_d)_n=1\quad\Longleftrightarrow\quad a\equiv d\pmod n.       \tag{1}
\]

Here the D-function is the image of the actual full continuous geometric sum; it is not defined by dividing by T-1 in the finite ring.

To prove (1), Theta_n is a unit because Theta_n D_(a,n)=1. Thus the left condition is D_(d,n)=D_(a,n), which implies T^d=T^a after multiplication by T-1, and hence a=d modulo n by the group basis.

Conversely suppose a=d modulo n. Multiplication by T-1 kills D_(d,n)+D_(a,n). A vector fixed by the cyclic left translation has constant coefficients on the single regular orbit, so this difference is c(1+T+...+T^(n-1)) for c in F2. Both a and d are full units and therefore odd, so the augmentation of their D-difference is zero. The augmentation of the displayed norm vector is n modulo2=1. Hence c=0, proving the converse. No residual-finiteness assertion or character-field choice is needed for this finite ring argument.

It follows that, under this full-GT hypothesis,

\[
\boxed{\quad a_{\rm reg}=d_\alpha
\iff (\Theta_uD_{d_\alpha})_n=1
       \text{ for every odd }n.\quad}                         \tag{2}
\]

Indeed equality at every odd n gives equality of all odd-primary components. The already proved dyadic equality gives the remaining component of Zhat. Conversely full equality gives every displayed projection. Once these exponent components agree, the full A88 ring identity follows; mixed even-times-odd heads require no additional comparison.

Equivalently, using the actual complete hexagon class R_d from the preceding note, (2) asks for

\[
\overline{R_{d,n}}=T^dR_{d,n}\qquad\text{for every odd }n.       \tag{3}
\]

Over an algebraic closure of F2, these odd cyclic rings are semisimple. Their nontrivial characters express the same test as

\[
\Theta_u(\zeta)=\frac{\zeta-1}{\zeta^d-1}
\qquad(\zeta\ne1\text{ of odd order}).                        \tag{4}
\]

The denominator is nonzero since d is a unit modulo that order; the trivial-character equation is already augmentation1. Formula (4) is only an optional character restatement of the proved elementary (1), not a new analytic interpolation assumption.

A42's prescribed pro-p hexagons for odd p do not by themselves verify (3). A quotient of the mod-two cyclic-cover kernel with an odd cyclic retained head is a relative finite quotient; it need not factor through the maximal pro-p quotient of F. In particular a pro-p kernel, p odd, has no nontrivial mod-two abelian quotient, so the pro-two module argument cannot simply be repeated with its head replaced by Z_p. The actual relative marking is still required.

No individual n was enumerated. No all-odd-head identity has been proved. For an arbitrary GT0 involution the dyadic hypothesis needed for (2) is not supplied; the unconditional statement remains the full-head criterion and weighted symmetry of the preceding note. Even proving (2) would leave the full nonlinear Xi_d/Omega_alpha equation and the required original-marking R2 input separate.
