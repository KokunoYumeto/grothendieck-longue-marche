# Universal primitive-cover existence: exact remaining obstacle

Status, 14 November 2026: research audit after the accepted A.C2.26 integration. Universal A1 remains A.30 Unresolved. This note establishes no failure of A1 or of the sufficient cover criterion, and adds no numbered theorem or finite-field census.

## 1. The existence assertion actually needed

For a fixed genus-two curve C over an algebraic closure of a finite field of characteristic two, let Theta be its Raynaud theta curve in J. A.C2.19 supplies A1 if there are an odd n>1 and a point L of exact order n such that

    every orbit of multiplication by 2 on (Z/n)^* contains i with iL in Theta.

Equivalently, the primitive conductor-n factor of the connected cyclic cover has two-rank zero. Lower-conductor factors may survive. Write E(C) for this existence assertion. The audit has not established E(C) for an arbitrary C. E(C) is sufficient for A1; no converse from A1 to E(C) is claimed.

A.C2.25 verifies E(C) for the former remaining F4 classes by 1,296 separate exact theta relations at conductor 7*31*2503*4519. The whole proof of that finite assertion is already integrated and independently verified. Its arithmetic group order, actual exponent, rank-two seven-primary subgroup, exact theta generator and complete orbit coverage were proved separately. None follows from the group order alone.

## 2. What the direct character-sum approach does and does not yield

Take a finite extension F_Q over which the theta embedding and all points under consideration are defined. Put A=J(F_Q), N=|A|, and c=|C(F_Q)|. Translating an Abel embedding to the Raynaud origin changes a character sum by a unit scalar. For every nontrivial additive character chi of A, the Lang-torsor estimate is

    |sum_(P in C(F_Q)) chi(P-B)| <= 2 sqrt(Q).

Katz proves the general (2g-2)sqrt(Q) estimate in Proposition9.1.3, with the complete geometric argument: the Abel map induces the required abelianized fundamental-group isomorphism, its pulled-back nontrivial Lang character has H0=H2=0, and H1 has dimension2g-2. This is an actual opened primary statement, not an assumed square-root bound for discrete logarithms.

For an additive subgroup H of index I, character orthogonality consequently gives

    ||Theta(F_Q) intersect (a+H)| - c/I| <= 2sqrt(Q)(I-1)/I.

This can prove that theta meets every additive coset of a sufficiently large subgroup. A primitive doubling orbit O={2^j L} is not an additive coset. For s=|O|, the exact Fourier expansion followed by this same bound and Cauchy–Schwarz gives only

    ||Theta(F_Q) intersect O| - cs/N|
      <= (2sqrt(Q)/N) sum_(chi != 1) |sum_(x in O) chi(x)|
      <= 2sqrt(Q*(N-1)/N * s*(1-s/N)).

The second inequality is just Parseval: the sum of the squared inner absolute values over nontrivial characters is Ns-s^2. It makes no independence assumption about theta and O. Thus it is rigorous, but far too weak to establish positivity in the large-conductor example itself.

For that already proved example, Q=262144, N=68725982332, c=262171 and s=1570005. The expected orbit intersection cs/N is approximately5.989; the resulting error bound is approximately1.283 million. In contrast, the full cyclic subgroup has index28; its expected intersection is c/28, approximately9363, while the additive-coset error is less than988. The standard theorem can therefore certify many theta points in the subgroup without locating a point in every primitive doubling orbit. Exact numerical values are saved in A_universal_primitive_existence_statistics.json.

This diagnoses the failed inference, not a proof that no better estimate exists. A new estimate must control the correlation with multiplicative orbits in the scalar-index group. Treating chi(log_L(P)) as an ordinary Artin character on C is unjustified. Enlarging the constant field while keeping a fixed finite subgroup and orbit does not repair the argument: their geometric theta intersection is unchanged.

## 3. Arithmetic Frobenius is useful only after the subgroup is controlled

If a cyclic subgroup H=<L> is Frobenius stable and pi(L)=aL, then theta membership is stable under multiplying indices by a. Symmetry also supplies -1. Thus a theta point whose indices generate all cosets under <2,-1,a> can give full coverage more efficiently. This is a valid finite certificate reduction.

It is not automatic that H is Frobenius stable, that pi acts by a specified scalar on it, or that <2,-1,a>=(Z/n)^*. Even the accepted example has a rank-two seven-primary group, for which different cyclic directions must be distinguished. The earlier complete73 analysis demonstrates a precise failure of this shortcut: the arithmetic scalar expands the covered subgroup only to index two, leaving positive primitive rank. No order or scalar claim is inferred solely from a point count.

A general proof along this route must construct a theta point and its cyclic subgroup with enough arithmetic scalar orbits, or must obtain direct theta hits in the remaining cosets. Prime-to-two torsion density alone asserts neither conclusion. A.C2.14 also prevents restricting the search to any fixed finite set of odd prime divisors uniformly over all curves.

## 4. Rechecked existence literature has a weaker conclusion

The already audited Raynaud solvable-cover theorem supplies nonordinariness, not zero stable support of an entire isotypic factor. The exact multiplicity-versus-support gap remains in A_nonabelian_Raynaud_gap.md. A.C2.23 shows that taking a cyclic primitive-zero stage inside an abelian total cover cannot evade the original existence question: such a stage already descends to a cyclic primitive-zero quotient of the original curve.

The following primary sources were opened again during this focused attempt.

* Hoshi (2022), Theorem2.7, authorpp9–10: in odd characteristic it constructs a cyclic cover with positive p-rank; for(p,n)=(2,3) or(3,2) and a nonordinary base it constructs a new-ordinary cover. Remark2.7.1 records the genus-two/characteristic-two cubic new-ordinariness result. These are not primitive-zero existence statements.
* Ozman and Pries (2019), author§8, pp18–19: Proposition8.1 is the theta criterion for new ordinariness, and Theorem8.2 records ordinary and nonordinary existence results. §9.4 asks a weaker fixed-prime nonordinary-Prym question. The previously identified discrepancy between its infinite-prime summary and the displayed Pop–Saidi coprime-order construction remains; it is not used to force prime order or complete primitive-orbit coverage.
* Achter and Casalaina-Martin (2024), TheoremA and Theorem5.12: these develop the characteristic-two Prym construction and classify when its induced polarization is a multiple of a principal polarization. The opened statements do not supply E(C).

These readings do not prove that E(C) is absent from the literature. They establish only that none of these actual opened statements fills the specific missing implication.

## 5. Precise next step and present limit

The next substantive mathematical step is to prove, for a fixed arbitrary genus-two curve C/Fbar2, the existence of one odd cyclic subgroup H for which every primitive doubling orbit intersects Theta. A quantitative version could construct H and prove a positive lower bound for the minimum orbit intersection, not merely an average over H or over all subgroups. A geometrically different route must force a complete stable representation block to disappear in a genuinely nonabelian total cover, with the transfer argument required by A.C2.20 or another proved criterion.

Neither step has been achieved in this audit. A possible arithmetic weakening involving rational two-torsion in primitive factors would require a new controlled-field endgame and uniform Frobenius control; it is not used or promoted here. No further bounded census or peripheral variance theorem was added. The integrated positive scope is unchanged: every genus-two curve overF4 is covered by A.C2.26, while general characteristic-two genus-two curves and universal A1 remain unresolved.

## References and exact openings

Katz, N. M. (2002). *Twisted L-functions and monodromy*. Princeton University Press. Author PDF https://web.math.princeton.edu/~nmk/twistedLfctnov052001.pdf . Proposition9.1.3, printedp185/PDFindex190, and its complete proof; preceding Lang-torsor discussion, printedp184. Opened turn860view0, turn861view0–1 and turn867view0.

Hoshi, Y. (2022). A note on torsion points on ample divisors on abelian varieties. *Mathematical Journal of Okayama University,64*,1–11. Primary journal PDF https://www.math.okayama-u.ac.jp/mjou/mjou64/_01_hoshi.pdf . Theorem2.7 and Remark2.7.1, pp9–10. Opened turn852view0, turn859view0 and turn867view1.

Ozman, E., & Pries, R. (2019). Ordinary and almost ordinary Prym varieties. *Asian Journal of Mathematics,23*(3),455–478. Primary author PDF https://arxiv.org/pdf/1502.05959 . Proposition8.1, Theorem8.2 and§9.4, authorpp18,20. Opened turn852view1, turn859view2, turn861view4 and turn867view2. The manuscript's earlier source audit retains the Pop–Saidi qualification.

Achter, J. D., & Casalaina-Martin, S. (2024, December18). *Putting the P back in Prym* [Preprint]. Author PDF https://www.math.colostate.edu/~achter/math/prym1224.pdf . TheoremA, authorpp2–3; the stated classification is proved as Theorems5.12 and6.4. Opened turn852view2. No assertion about its later publication status is needed.

No source quotation is reproduced. The Fourier expansion and its concrete comparison above are calculations of this audit; they are not attributed as a new theorem of the cited authors.
