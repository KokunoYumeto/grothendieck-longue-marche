# E.110 — The complete fixed-seventeen H section set

Every three-primary class group in the pure radical tower vanishes.
This provides a coherent lift of every compatible pure divisor and,
combined with E107, evaluates the entire H section set with first
Kummer class kappa3(17), including every second toric fiber.
The exact arithmetic automorphism (a,v(T)) -> (r*a,v(T^r)) gives
the same complete evaluation for every unit r in Z3.

## Arithmetic input and all-level proof

The three literal M1 units have four local characters

    2 2 2
    2 2 0
    2 0 2
    0 2 2

at the three labeled places over3 and the place over17.
The first three rows have determinant -8, so the image is the
entire product-one hyperplane. The local norm of alpha_d to
alpha1 and the exact Kummer projection formula preserve those
characters at every height, with no degree multiplier.

There are four totally ramified places at each vertical step.
Chevalley's formula therefore gives unchanged ambiguous
three-class order. The initial M1 three-class group is zero
by a separate one-ramified-prime argument, and the finite
three-group fixed-point lemma proves that the full groups
remain zero. Extension and norm with composite2 give the
pure F_d assertion.

The same exact ambiguous/strongly-ambiguous sequence gives
ordinary-unit norm cokernels C3^3 over M and C3 over F.
The proof retains their actual local maps. In particular it
does not replace the genuine first pure unit norm row
(0,3,0,0) by a surjective map; the next wild character row
is (0,2,0,0).

## Entire pure positional factor

Every completed divisor is principal because the finite class
group has order prime to3. Compatible completed divisors lift
coherently by the finite intersection property applied to
compact ordinary-unit torsors.

The surviving divisor coordinates are the two three-prime
chains, the seventeen chain, and one degree-one chain at
each prime p with v3(ord_p17)=0. Their exact rational norm is

    (B,C,e,t) -> 3^(B+C) 17^e product p^t_p.

The infinite prime exponents form the restricted, prodiscrete
multiplication completion. The unit kernel is compact and
has a specified topological isomorphism with a countably
infinite product of Z3: choose a Pruefer basis of its actual
character direct limit under transposed unit norm matrices.
Finite character equations give the forward map and unique
inverse. Its infinite rank follows unconditionally from
Kato1.1(1) and the exact rank computation in Section3.2,
through restriction to the actual pure norm chain.

## Full second toric image and inverse

The allowed prime support is precisely {3,17} together with
the primes whose 17-residue order has three-part at most3.
For an arbitrary target with coefficients B3,B17,r_p, put

    t_L=3*r|P1, t_F=3*r|P0,
    e=3*B17-2*b,
    C=3*B3-3*z+sum ell_p*r_p-B.

Here b,z,B are arbitrary Z3 parameters. The section is the
actual positional pair

    x_L=beta^b e_L^z k_L s_L*(t_L),
    x_F=k_F s_F(B,C,e,t_F).

Its total norm is exactly the cube of the target. Every section
has exactly these coordinates, by the actual complex coordinate
inverse and pure divisor inverse. Thus every fiber is
Z3^3 times the complete pure unit product times the complete
complex base-zero unit product.

For kappa3(7), E107 gives ell7=8. The concrete pure correction
a1^8 has norm3^8 and the complex factor s_L*(3[7]) has norm
7^3/3^8. Their combination gives the exact requested toric
coordinate, including the phase excluded in the pure=1 locus.

## Certificate and scope

The portable full rebuild is:

    python code/e_pure_tower.py --gp /absolute/path/to/gp

It executes the small degree6 certified GP calculation and
retains the full binary object. The self-contained Python
then verifies the literal units, four local characters,
all27 image inverses and mixed-unit products,792 compatible
prime-root transitions, and531441 full toric inverse checks.
The historical failed exports and their actual outputs are
retained with their precise causes. No expensive upper BNF
was restarted.

The entire H set at the stated first classes is evaluated.
The actual image from intrinsic metabelian or marked-depth
sections remains a further lifting problem through E38's
quotient maps. Nonunit multiples of kappa17 and first
classes outside the proved families are not included in this
theorem.

## Integrated audit and current scope

E.110 proves all pure-tower three-class groups zero and evaluates every coherent pure divisor and its unit kernel through exact norm-character maps. Combining the pure and complex factors gives the complete actual H section space over kappa3(17) and every unit multiple, with second toric support at3,17 and primes satisfying v3(ord_p17)<=1, and every explicit inverse fibre. Other first classes and the intrinsic metabelian/marked source image remain active.

Full root review and recorded fresh executions passed. E108, E109 and E110 also have received independent proof reviews. D59 includes its exact numerical amendment. The full-paper layout is verified in the following build.
