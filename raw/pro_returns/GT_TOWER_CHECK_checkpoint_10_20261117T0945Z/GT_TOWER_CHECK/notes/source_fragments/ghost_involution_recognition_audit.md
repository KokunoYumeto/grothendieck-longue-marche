# Independent audit of A.4.54

Reviewed the complete source `root_involution_configuration_recognition.tex`
on 2026-11-17. Mathematical result: **PASS**. The remarks below concern
the actual normalized configuration spaces, the named involution, and
the displayed finite quotient maps.

## Fixed configurations and the ordinary kernel centralizer

For n=9,10,11,12, the number of fixed labels is k=n-8. After the
distinguished label is anchored at zero, each of the k-1 other fixed
labels is a distinct nonzero element of T[2]. The remaining four
labelled pairs have coordinates (u_j,-u_j). Their exact collision
conditions are u_j outside T[2] and u_i unequal to either sign of u_j.
The ordered assignments of the fixed labels number 1,3,6,6.

For a fixed assignment, the sign-forgetting map is a degree-16 cover
of the ordered four-point configuration space on the four-punctured
sphere. That base is connected. Moving one specified point around one
branch puncture, while holding the others fixed, changes precisely its
lift sign. These four independent monodromies prove connectedness of
the cover; no quotient of the ordered fixed-label assignments has been
taken. The fixed-component dimension is eight.

The normalized evaluation fibration gives the actual point-pushing
kernel K_n, with free ranks 2 through n. The universal cover of X_n is
contractible. The canonical lift of the involution is smooth and has
nonempty, connected, mod-two acyclic fixed set. Joining the chosen
lifted basepoint to its translate by an invariant deck transformation
inside that fixed set proves im(pi_1(X_n^{iota,0}) -> K_n)=C_Kn(iota).
Conversely a lifted fixed loop has invariant endpoint displacement.
This proves precisely the image statement; no injectivity claim for
the fixed-locus fundamental group is needed.

I independently opened the official primary PDF
<https://topology.nipissingu.ca/tp/reprints/v40/tp40023.pdf>, printed
pp.273-274. Proposition 3.2.1 supplies the chosen-point lifting
statement; Remark 3.2.4 supplies the fixed-loop image description when
the lifted fixed set is path connected; Theorem 3.3.1 and Proposition
3.3.2 give the acyclicity used here. The smooth finite-dimensional
configuration-cover action satisfies their hypotheses. No compactness
claim from the later dimension discussion in that source is used.

## Binary refinement and finite centralizer projection

In the free-group binary quotient, the cycle for the squared jth free
generator uses two distinct directed edges in the regular rose cover.
A deck vector outside its coordinate line moves it to disjoint edge
support. Since graph homology injects in edge chains, the homology
action is faithful. The center therefore maps trivially to the
elementary abelian deck group, giving the exact action-kernel
intersection used in the cohomology refinement.

The two-row LHS comparison remains valid at two with the possibly
nontrivial base action on H1 of the free kernel: the coefficient
restriction itself is zero. The positive q=0 restriction factors
through the selected subgroup of the base. Two successive such maps
kill the two-step filtered cohomology, with the stated Schreier bounds.
The coset-action argument makes each characteristic kappa subgroup
contained in the constructed subgroup and retains the zero maps.

The periodic six-division arrangement is invariant under minus the
label permutation and includes the forbidden diagonals. Its
barycentric complement retraction is equivariant and fixes the
selected vertices. The relative cochain complexes have degrees zero
through 2n-2. Thus 2n-1 actual zero-cohomology maps kill Tate
hypercohomology. For C2, the nonfixed cells are free orbits, and both
horizontal differentials vanish on fixed-cell cochains over F2.
Consequently the zero relative H0 map detects the entire bottom fixed
component. It does not require the fixed locus to be discrete.

A centralizing finite deck coset fixes its named fibre point. The
resulting bottom fixed-component path projects to an actual fixed
loop with that exact output displacement. This gives the forward
inclusion in ICR.6; actual commuting elements give the reverse.

## Ambient quotient and the moving origin

All base marks lie in T[6], so literal linear maps in Gamma(6) give
the stated homomorphic splitting. Its index is 144 n!, using the
independent compact-period and disc-label maps. The quotient of this
normal subgroup retains the actual K_n/V coordinate. Induction through
its I_n cosets has permutation image of order I_n and intersects K_n
in precisely V because V is characteristic there. This verifies both
the ambient order bound and its specified projection to Q.

The relative-homology correction is exact. For every fixed label j,
the compact component of iota(gamma_j)-gamma_j is -2p_j modulo two,
independent of the chosen path. The label matrix of an arbitrary g
sends e_j-e_0 to e_(tau j)-e_(tau 0), so commutation cancels the B
term and yields A p_j+p_(tau 0)=p_(tau j). The p_(tau 0) term cannot
be dropped; it is retained in ICR.19.

The actual affine map Az+p_(tau 0) then commutes with minus identity,
has integral period A, and gives the exact fixed-label assignment.
On the branch sphere, an isotopy fixing all four branch points can
move its four pair orbits to the required labelled orbits. Independent
branch loops prescribe all four lift signs. The identity-started lift
fixes T[2], commutes with the deck involution, and has compact period
identity. Hence its composition with the affine map supplies the
ordinary centralizer element with exactly the original period and
label permutation. The remaining factor is literally in K_n, where
ICR.6 applies. This verifies the full ambient equality ICR.15.

## Typesetting observation

The reviewed source has a missing leading backslash in `longrightarrow`
in ICR.10. Root was notified; no mathematical source was edited by this
audit.
