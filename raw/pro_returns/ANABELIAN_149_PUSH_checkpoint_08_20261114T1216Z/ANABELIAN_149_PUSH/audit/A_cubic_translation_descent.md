# A necessary base-point condition from all odd multiplication pullbacks

Status: further necessary-condition deduction, retained as an exploratory route. It concerns the exact-order-three symmetric branch family. A.29h now proves A1 for that entire family by a different two-branch construction, so this coset elimination is no longer needed for the A1 conclusion. The note does not classify every remaining finite packet or assert that the coset condition by itself is impossible.

Let E be ordinary in characteristic two, let d have exact order3, put D=〈d〉, and let h have divisor(d)+(−d)−2(O). Let B/E be the cubic root cover z³=h. Let δ generate its deck group and let

\[
 S=\{\pi(P):0\ne[P-\delta P]\text{ is 2-primary}\}\subset E(\overline{\mathbb F}_2).
\]

A.29d proves that S is finite. It is disjoint from D, because the cubic cover is totally ramified there. Define the D-invariant finite set

\[
 S_D=\{t\in E:t+D\subset S\}.
\]

Suppose two distinct points P,Q of B have equal geometrically prime-to-two section classes over a finite field extension. A.21 gives a common elliptic image t₀. The first translated refinement A.29b gives t₀∈S_D, by the same central-displacement argument used in A.29c. We claim the stronger necessary condition

\[
 t_0\in [N]S_D+D\quad\text{for every odd }N\ge1. \tag{1}
\]

## Construction proving(1)

Pull B back along [N]:E→E. The normalization C_N is connected: a ramified cyclic cubic extension of k(E) cannot intersect the unramified isogeny field in a nontrivial subextension. The map C_N→B is finite étale of degreeN², with odd Galois group E[N]. Its branch support over the new elliptic base is

\[
 H_N=[N]^{-1}D,
\]

a subgroup of order3N² containing D. Modulo3 the divisor of h∘[N] has residue1 at every point of H_N and zero elsewhere.

Partition H_N into its N² cosets a+D. For every coset adjoin the cubic roots of all three translated functions h(t−a−id), i=0,1,2. Each such cover is a translate of B. Its ramification index is3 at that coset and1 elsewhere, and therefore divides the ramification of C_N. Their common normalization V_N is étale over C_N. Over E it is an abelian 3-power Galois cover, and its composite with C_N→B has odd geometric Galois closure: translations by E[N] permute the finitely many cubic characters. Thus A.3 lifts the alleged collision to V_N after finite constants.

The images of those lifts on C_N and on E have the same elliptic coordinate t, by A.21. They map to t₀ under[N]. Since t₀∉D, the coordinate t lies outside H_N, so all covers here are unramified at the fibre in question.

For each coset a+D, its three cubic functions form the same Heisenberg block as A.29b. Their common quotient by diagonal inertia is an unramified genus-one cover E_{2,a}/E. The map V_N→E_{2,a} is Galois and ramified, because E_{2,a}/E is unramified while V_N/E has index3 along H_N. A.21 therefore forces equal images there. Consequently the three coordinate characters of the collision displacement are equal on that block.

Select one representative a for each coset. The function

\[
 h([N]t)\big/\prod_{a\in H_N/D} h(t-a)
\]

has divisor divisible by3. Its cubic root defines an unramified genus-one cover of E (or a split trivial cover, in which case select one component). A.21 again gives equal images of the lifted collision in this quotient. The character of C_N is thus the product of the selected block characters on the collision displacement.

That original character is nontrivial, since the images on B are distinct. Hence some block character is nontrivial. All three characters in that block are equal and nontrivial. Their images on the three translated B-covers are distinct deck pairs with 2-primary divisor differences. Therefore

\[
 t-a-id\in S\qquad(i=0,1,2),
\]

so t−a∈S_D. Multiplication by N gives t₀∈[N]S_D+D, because a∈H_N. This proves(1), including N divisible by3; no coprimality between N and3 was used.

## Consequence and exact limit

Every point of the finite set S_D is torsion. Choose an odd N annihilating the odd-primary component of every one of them. Then[N]S_D is contained in E[2^∞], so(1) implies

\[
 t_0\in E[2^\infty]+D.
\]

Equivalently, the image of t₀ in E/D is 2-primary. Combining with t₀∈S_D, a collision forces S to contain an entire D-coset whose image in E/D is 2-primary. This is stronger than nonemptiness of the original packet.

This does not yet prove that such a coset cannot occur. In particular the first possible elliptic two-primary coset is T+D, where T is the nonzero point of E[2]. Its member T corresponds to the known Weierstrass packet, whereas T±d would require non-Weierstrass packet points. Excluding all such translated two-primary cosets is a precise remaining geometric task. The argument does not infer a uniform exponent bound on arbitrary Jacobians in the multiplication tower.
