# Fresh positive-marginal reconstruction and its exact transport

Research computation, 16 November2026. The original attached LM4 F23/F24
code files were not present in the recovered inputs. The present program
reconstructs only the positive signed marginal, from the actual formulas
and based paths printed in the attached paper. No old stdout or code is
claimed to have been recovered.

## Actual family and source

Let zeta=exp(2*pi*i/5). In the finite-label order used here the eight
points are

    0, 1, v_1(s), v_zeta(s), v_zeta2(s), v_zeta3(s), v_zeta4(s), a(s),
    v_u(s)=((u-s)/(u+s))^2,       a(s)=(zeta-s)/(zeta+s).

The ninth sphere label is infinity. The source is Y_+=P1 minus
0,infinity,plus/minus mu5 and the eight roots of

    s^2=A_j=zeta^j(2*zeta-zeta^j),       j=0,2,3,4.

Its finite-puncture meridian basis has rank19. The basepoint is2+2i.
The nineteen centers and square lassos are exactly the positive subset
of the attached F23.14 tables; their source half-side is h=1e-4.
Each lasso follows the straight whisker from2+2i to the northeast
corner of its square, traverses the square counterclockwise, and
returns along the reverse whisker. The exact rational distance checks
verify that the whiskers form an embedded star and avoid every other
square. Each square contains its one named actual source puncture.
The eleven old lassos survive the filling of the eight new punctures.

To return to the original attached basepoint s0, use the actual F20.4a
path with vertices

    s0, 3*s0, 3*s0+6i, 6+6i, 2+2i,
    s0=i*(theta^2-2)*zeta, theta=2*sin(2*pi/5).

The attached proof verifies that this path avoids all old and both
signed new collisions. Its image under the displayed labelled family,
and the same literal forgettings of that path, provide the common
based transport. No unrelated target conjugator is introduced.

## Rational coefficient deformation

For a fresh rational-Sturm certificate, replace the five roots zeta^j
by the following rational complex constants:

    1,
    (309016994375 +951056516295*i)/10^12,
    (-809016994375+587785252292*i)/10^12,
    (-809016994375-587785252292*i)/10^12,
    (309016994375 -951056516295*i)/10^12.

The program constructs exact rational enclosures of sqrt(5) and
sqrt(10+/-2*sqrt(5)), and checks that each displayed constant has
complex error less than1e-12 from its specified root. Interpolate each
coefficient linearly. Denote the varying coefficients by z_j and the
coefficient in a(s) by z_1.

The entire finite collision set along this interpolation is explicit:

* zeros/poles of a or v_j, and collisions with1: s=0 or s=+/-z_j;
* v_i=v_j, i!=j: s=0 or s^2=z_i*z_j;
* a=v_j, j!=1: s=0 or s^2=z_j*(2*z_1-z_j);
* a=v_1: s=0 or s=z_1.

All coefficient-product errors along the interpolation are less than
1e-10. The program checks the old-root disks directly and checks each
quadratic root disk by Rouche: for a printed center c and its squared
root V,

    |c|>1/2,  |c^2-V|<1e-5,
    (h/2)^2+1e-5<h/2.

The residual check includes the1e-10 interpolation slack. On the
circle |s-c|=h/2 the linear term2*c*(s-c) dominates the constant and
quadratic errors, so each indicated disk contains one root throughout
the deformation. For a pair product z_i*z_j use the old disk with
index3*(i+j) modulo5, and its negative. Thus every critical point stays
inside its original square. The fixed source loops avoid all these
squares except their own boundary, so the coefficient deformation
induces a collision-free homotopy of every specified target loop.

Several deformed pair polynomials can have different roots in the same
old disk. We do not assume that all their roots are globally separated.
Only the distinct roots in each individual squarefree numerator
factorization below need the stated separation.

## Projection perturbation

Set P0=1+371*i/1000 and, in the finite-label order above, add

    epsilon_j=j^2/(10^14*P0),       0<=j<=7.

This removes coincident projection events without changing the braid.
Here is an explicit uniform estimate. Every source path has |s|<3,
every coefficient has |z_j|<2, and every path point has distance at
least rho=h/3 from every critical root. Distinct source disks have
centers more than0.11 apart; the distinct roots within each individual
squarefree factorization are consequently separated by at least
sigma=0.1. Every denominator factor has modulus less than5.

The relevant numerators, up to nonzero signs, are

    v_j:                 (s-z_j)^2;
    v_i-v_j:             4*s*(z_i-z_j)*(s^2-z_i*z_j);
    a-v_j, j!=1:         2*s*(s^2-z_j*(2*z_1-z_j));
    a-v_1:               2*s*(z_1-s);
    a:                   z_1-s;
    a-1:                 -2*s;
    v_j-1:               -4*z_j*s.

For a product of three distinct critical factors, at most one can have
modulus less than sigma/2. Its product is at least
rho*(sigma/2)^2. Also |z_i-z_j|>0.1 and |z_j|>0.9.
The resulting pair-difference lower bounds, all checked as exact
rational inequalities, have minimum greater than1e-11. The maximum
change of any pair difference under the offset interpolation is less
than49*1e-14. Thus the full offset interpolation is collision-free.

The coefficient homotopy followed by the offset homotopy gives an
explicit labelled path between the original and computed target
basepoints. All old-point forgettings and the one-point fiber maps use
these same homotopies. This is the exact based comparison for the
computed monodromy, rather than a claim that the rational coefficients
still form a cyclic regular pentagon.

## Exact crossing computation and scope

After these proved deformations, every coordinate is rational over Q(i).
The existing rational-Sturm engine is used with eight strands. For each
source segment it checks every denominator and collision numerator,
isolates every real projected crossing, checks a simple root and
nonzero height, verifies adjacency, and checks the final projection
order. It retains all exact polynomials and isolating intervals.
Return whiskers use the literal inverse words.

The geometry checks and braid words are freshly executed data. The
positive_marginal_words.json file is the small word-only record;
positive_marginal_braids.json also retains all crossing certificates.
Their presence is not a claim of source surjectivity. The next step is
to extract the actual F7 fiber words and the eleven based actions, then
test a precise subgroup/peripheral/finite-cover mechanism. Normal
generation, an abelian rank, or a finite list of successful finite
images is not substituted for the full marginal equality.
