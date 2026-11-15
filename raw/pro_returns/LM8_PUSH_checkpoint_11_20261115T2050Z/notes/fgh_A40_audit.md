# A.40: all genus-one covers

Status: parent full independent proof/source audit and independent code rerun passed; the parent is integrating the section and row.

## New unbounded algebra

For a proper curve with potentially good reduction, separating its cusps creates a single positive-genus component and attached rational marked trees. Select two distinct cusps P,Q colliding on the good model, root at P, and eliminate Q from the peripheral relation. Write B=k<Omega,t_j, j!=Q>. The actual tree derivation has D(v)=[W,v] for every handle and D(t_j)=[W_j,t_j]. All W and W_j are boundary-linear. Packet changes add lambda ad(t_P).

The Omega coefficients are r=sum m_e E_e(1-Q_e) and c_j=sum m_e j_e(E_e-Q_e). Here r is the strictly positive distance from the P,Q,genus branching point to the genus vertex. Other cusps can be on other trees or on the genus component; then c_j may equal r. Some c_j may be negative. Neither is an obstruction.

The first-core prefix operator is K=D_B+R_W. Its part raising the Omega count is D_c+rR_Omega, with D_c(t_j)=c_j[Omega,t_j]. On a fixed ordered cusp word i_1...i_n, insertion exponents identify its vector space with k[Z_0,...,Z_n]. The operator is multiplication by c_i1 Z0 + sum(c_next-c_prev) Z_h +(r-c_last) Z_n. Its coefficients sum to r, so it is nonzero. This proves injectivity at all degrees, independent of lambda and the signs of c_j. The kernel of the complete derivation is therefore contained in the primitive boundary algebra L(t_j,Omega). All its generators are Tate of weight two, which is exactly the hypothesis of A.38.

The proof does not infer a nonabelian injection from a finite covering map. It uses the actual derived-fixed subgroup and its unipotent closure, not arbitrary rational fixed elements.

## Collision for arbitrary isogeny degree

Let phi:E'→E have degree N. For each p|N, some p-primary kernel point must specialize to zero at some place above p.

* At p=2 or p=3 modulo4, E is potentially supersingular. An isogenous good reduction is supersingular too, so every p-primary kernel point specializes to zero.
* At split p=pi*pi_bar, suppose the p-primary kernel specialized injectively at every place above both CM primes. Prime-to-p torsion also specializes injectively, hence the entire kernel stays distinct and the special isogeny is separable of degree N. The ordinary special [N] map has inseparable degree equal to the p-part p^n. The dual special isogeny consequently has separable degree N/p^n, with no p-primary geometric kernel points. Its generic p-primary kernel T, of order p^n, thus specializes to zero at both CM primes.
* On the target E, endomorphisms [pi] and [pi_bar] extend to the good model. At the pi-prime the first has degree p and zero differential, hence purely inseparable reduction; the second is separable. The formal p^n-torsion is exactly E[pi^n]. The conjugate place gives E[pi_bar^n]. Their intersection is zero by Bezout in Z[i], contradicting |T|=p^n. This proof uses maximal CM only on the fixed target E, so it allows nonmaximal orders on E'.

Translation by any selected cusp turns the zero-specializing kernel point into a second cusp colliding with it. For coefficient prime ell, choose p!=ell dividing N and apply the marked-tree criterion. If no such p exists, the cover has ell-group Galois group and A.22 applies. Degree one is R1.

## Primary source checks

Betts--Dogra's actual based edge formula has already been independently opened in the A.35–A.39 audits. The new coefficient calculation uses its downstream boundary class with the complete relation before eliminating Q.

Silverman AEC primary book reopened at https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf. Relevant exact references: Theorem III.6.1 (dual isogeny), Corollary III.6.4 (p-power torsion/separable degree), Theorem V.3.1 (ordinary/supersingular), Theorem V.4.1(a), printed p148, Example V.4.5, printed p152 (j1728 supersingularity), and Proposition VII.3.1(b) (prime-to-p torsion specialization). Web refs turn583view0, turn584view0–2, turn589view0–1. The degree of the special isogeny equals the generic degree by constancy of the degree of its pulled-back degree-one line bundle; no unproved equality of a generic point count and a special scheme length is used.

## Executed certificate

`code/a_isogeny_fixed.py`, `.json`, `.out`: PASS.

The code checks the positive coefficient identity on every labelled tree with a genus leaf through six vertices; an explicit stable marked tree with c_j values 0,0,3,-3,-7,5 and r=5; the exact slot formula on every boundary word through length four; prefix injectivity through boundary degree three for lambda=0,1,-2,5,-5; and Hasse coefficients at odd primes below100. The example deliberately includes a cusp on the genus component with c_j=r, confirming that the telescope, rather than a strict-gap hypothesis, is the correct proof.

## Normalizers

Every genus-one compactification map is unramified by Riemann–Hurwitz and becomes an isogeny after choosing an origin. A.11 detects any noncuspidal normalized procyclic subgroup in proper H1. The actual arithmetic map to U preserves an open arithmetic normalizer image, and the proper rational H1 isogeny map is an isomorphism even when ell divides the degree. R2 then forces the nonzero image to be cuspidal, contrary to its nonzero proper homology. This step applies to all genus-one covers independently of the collision argument.
