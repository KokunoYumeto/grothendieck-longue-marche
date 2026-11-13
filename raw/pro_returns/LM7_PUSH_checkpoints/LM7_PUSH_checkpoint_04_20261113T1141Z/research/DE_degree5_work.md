# Degree5 continuation plan and exact kernel presentation

Completed E21 is in sections/E_ferrari_degree4_agent.tex. Root has been told
to input it after E20. All degree4 computations are finished. Target joint
order344373768, E18 kernel dimension12; pureS4 quotient8264970432. Source
kernel overG6 dimension7, Fprime6, Nprime3, gamma3N zero. Norm rank4,
pentagon5, every retained E17 point has an affine line (3 points). All24
literal choices generate source and target and preserve full twists.

For degree5, use de_ferrari_truncated_model.FerrariTruncated(5), keeping the
mod9 factor. The top kernel over the exact degree4 target is elementary
abelian, with96 ambient coordinates per evaluation (32 unit degree5 and
64 automorphism degree5). Source core has36 evaluations as before.
Do not use kernel_vector over E18 atdegree5: that kernel is class2,
not abelian; top_kernel_vector/top_kernel_element are implemented.

Exact next source-kernel presentation: let Jprime=K6 intersectFprime.
It is normally generated inN by all4656 [ni,nj] and95 products
prod ni^(6 ai) for the integral ker(Fab) basis. Its degree4 image is
F3^6 with actual basis words bi saved in de_ferrari_degree4_module.json.
The kernel over degree4 is normally generated inN by:
1. each original generator g times prod bi^(-coeff_i(g));
2. all bi^3 and all [bi,bj];
3. every nk bi nk^-1 times prod bj^(-coeff_j(Ad nk bi)).
These relations put every original generator and every N-conjugate
in the commuting exponent3 span of the selected six bi. The quotient
therefore has order at most3^6 and maps onto the actual image3^6, proving
that this is the complete kernel, not a sample. Evaluate these5354
relations in the degree5 top layer and close their span underN. Retain
literal words for an actual basis. Repeat with K6 normal generators
(4656 commutators plus97 sixth powers), the seven saved full-image basis
words, to get the complete source kernel without Fprime. Verify s/r
stability and the full Fprime basis abelianization.

For each old E21 point, retain all three old affine solutions z=z0+tK.
Their exact lifted Sbase=beta s beta^-1 * old_k need not have square1
atdegree5. Rbase=Sbase^-1*t. The inverse is essential before the top correction: the provisional Sbase can have a nonzero square. For a top correction k the full linear norms
are (1+AdS)k= -Sbase^2 and (1+AdR+AdR^2)k=Rbase^3. The final word is
s*x^g*Sbase*k*x^-g; k is an actual Fprime word, so the integral gauge
is unchanged. Pentagon residuals are in the top layer; their correction
map is exactly affine. Evaluate all old t values, retaining all system
matrices and at least one direct literal witness per CM fibre.

Source generation follows from Frattini without expensive repeated
5354-relation calculations: N-image is a finite3-group times its G6
2-primary abelian component, by the exact coprime product comparison.
The new kernel is inside the image of Nprime N6, hence inside the
Frattini subgroup of the3-Sylow. Every solution already induces the
verified G6 automorphism and therefore generates the source quotient.

For full four-strand generation atdegree5, the joint kernel overE18 is
class2 exponent3. Its raw coordinates have group law v*w=v+w+C(v,w),
with bilinear cross terms only atdegree5. Log(v)=v-(1/2)C(v,v) gives
actual first-kind coordinates, and the bracket is the group commutator.
Compute its full Lie span from the Schreier relators overE18 (648 vertices,
3 generators) and their pairwise brackets; this gives target order and
its commutator/Frattini subspace. For each corrected triple, project its
Schreier generators to the resulting Frattini quotient and check full
rank. This avoids enumerating the huge degree4 target. Exact full twists
and all braid relations should again be checked.

## Correction recorded before E22 was stated

The first degree5 solver used Rbase=Sbase*t even though Sbase could have
a top-layer square. An independent gentle-only product check exposed
this. Its four positive witnesses had passed full direct equations and
remain actual positives, but all twenty initial negative conclusions
were withdrawn. Both solvers now define Rbase=Sbase^-1*t and assert
Sbase*Rbase=t before forming any norm equations. The full72-case rerun
replaces the preliminary lift/control/generation outputs. No E22
statement was written before this correction.
