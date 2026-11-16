# The other two elliptic quotients of the harmonic genus-three curve

Let K=Q(sqrt(2)), lambda=1/sqrt(2), h=1/2, and let D be the smooth
proper completion of aW^4=T(T-1)(T-h), with the exact A139 coefficient a.
For either sign of lambda the actual involution is

sigma_lambda(T,W)=(lambda^2/T, lambda W/T).

Substitution proves that it preserves the curve and has order two.
The invariant functions

x=aW^2/T,  Y=aW(T+lambda)/T

satisfy

E_lambda: Y^2=x^3+a(3/2+2lambda)x.

Indeed, after dividing by a^2W^2/T^2, the target identity is
(T+lambda)^2=(T-1)(T-h)+(3/2+2lambda)T.
The inverse field equations are

u=x^2/a+3/2,  T^2-uT+lambda^2=0,
W=YT/[a(T+lambda)].

They give degree at most two, while the displayed nontrivial
involution fixes x,Y, so the degree is exactly two. These maps extend
uniquely over the smooth proper curves. Their target is nonsingular
because a(3/2+2lambda) is nonzero.

The boundary map is literal: T=0 and infinity go to O, and T=1,h
go to (0,0). At T=0, T is a unit times W^4, so x,Y have poles of
orders two and three. At infinity use w=W/T; T and W have orders
-4 and -3, giving the same pole orders. At T=1,h, both x,Y vanish.
The involution exchanges each pair, so all four boundary points
are unramified for these degree-two quotient maps.

Differentiation using 4aW^3 dW=F'(T)dT gives

q_lambda^*(dx/(2Y))=(T-lambda)dT/(4aW^3).

Together with the old W-to-minus-W quotient differential,
a nonzero constant times dT/W^2, the two new differentials span
dT/W^2, dT/W^3, T dT/W^3. At each finite branch point dT has order
three in W; at infinity the three differential orders are respectively
1,4,0. They are regular and linearly independent, hence form a basis
of the three-dimensional space of regular differentials.
The pushforwards on degree-zero divisor classes therefore give the
actual K-isogeny

Jac(D)_K -> E_K × E_lambda × E_{-lambda}.

The maps on Jacobians are the canonical divisor pushforwards;
subtracting the image of the chosen base point accounts for any
nonzero target origin image of the old quotient. The differential
calculation proves finite kernel and surjectivity.

Put epsilon=1+sqrt(2) and M=7·13·23·139·1119169.
The exact A143 constant is q0=M/(2·191^2), and a=573q0^2.
Scaling x by (2·191)^2 and Y by (2·191)^3 identifies E_lambda
with

E_b: Y^2=X^3+bX,  b=1146 epsilon^2 M^2.

The conjugate coefficient ratio is (sqrt(2)-1)^4.
Thus x -> (sqrt(2)-1)^2 x and Y -> (sqrt(2)-1)^3Y give an
actual K-isomorphism E_lambda -> E_{-lambda}.

## Executed arithmetic filters

The literal maps, inverse field equations, differentials and scalings
are checked in work/code/harmonic_prym_quotient_certificate.py and
its retained output.

The dyadic field has uniformizer pi=sqrt(2). A unit represented by
a+b*pi is determined modulo pi^5 by a modulo 8 and b modulo 4.
The square-unit residues are exactly (1,0) and (3,2).
Hensel's lemma proves that 1+pi^5 O is contained in the squares:
for f(X)=X^2-u at X=1, v_pi(f(1))>=5>2v_pi(2)=4.
Consequently the finite unit quotient gives all eight unit
squareclasses, and adjoining the valuation parity gives all sixteen
local squareclasses.

For a squareclass d, the two-isogeny quartic is
N^2=dU^4+(b/d)V^4. Normalize a field solution to a primitive integral
pair (U,V). The two literal charts U=1 and V=1 with U nonunit exhaust
all such pairs. Reducing them modulo pi^L gives necessary conditions.
The program work/code/harmonic_prym_dyadic_filter.py executes these
finite charts through L=13 and retains every surviving residue
witness in its data file. No local-solubility converse is inferred.
The dual coefficient -4b is locally and globally K-isomorphic to -b
by x=2X, y=2sqrt(2)Y; the x-squareclass is unchanged because 2 is
a square in K.

The independent odd-place code of /root/legendre_main is
work/code/harmonic_prym_odd_filter.py. It checks the exact positive
prime-generator factorization of b, both residue-field embeddings
at every split prime, and all primitive-quartic necessary conditions.
The first filters leave 64 classes for E_b and four for its dual.
The latter are exactly 1,1119169,-573,-573·1119169.
The resulting two-isogeny rank upper bound is six. Neither rank zero
nor finiteness of the Mordell-Weil group has been proved by these
filters. Further global descent is the outstanding arithmetic step
for using this separate factor as a finite target.

## Exact local sufficiency and the saved A150 proof

The precision-thirteen dyadic survivors are now proved locally
soluble. For the primitive quartic F=N²-dU⁴-(b/d)V⁴, either U is a
unit and v_pi(F_U)=4+delta<=5, or V is a unit and
v_pi(F_V)=6-delta<=6. The retained error depth13 is strictly greater
than twice the applicable derivative depth. Hensel therefore lifts
every retained witness. All odd supporting-prime tests are also
sufficient, and at every remaining odd prime the smooth genus-one
reduction has a finite-field point and lifts. Real conditions were
included in the global candidate list.

Thus the64/4 groups are the actual two-isogeny Selmer groups. Their
members are not thereby identified with global points. The exact
maps, complete local proof, Selmer orientations, and rank possibilities
{0,2,4,6} are saved in sections/harmonic_prym_selmer.tex (A150).
The consolidated code/harmonic_prym_selmer_certificate.py reruns
the prerequisite computations and checks all ten literal Hensel
inequalities and the complete squareclass spans.
