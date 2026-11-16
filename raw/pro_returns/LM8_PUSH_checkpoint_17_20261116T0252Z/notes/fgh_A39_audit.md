# A.39 proof and source ledger

Full section: `sections/A_D4_fixed.tex`. Parent full independent proof audit and independent code rerun passed; the statement is integrated.

## Geometric inputs

* A.4 supplies the three dihedral genus-two equations, both reflection classes, Jacobian factors with j-invariants 1728 and one of 8000, 10976, 128, and exact order four for the cusp difference. Only its annihilation by four is used.
* The exact rational function `(z-(x^3-4cx))^2/(x^2-4c)` has divisor `4(Q_plus-Q_minus)`. Its apparent finite poles at `x^2=4c` cancel because the local uniformizer is z and numerator and denominator both have order two. Its orders at infinity are +4 and -4. All d=a+2c^2 are nonzero.
* At residue characteristic two, all elliptic factors acquire good supersingular reduction. The Jacobian is therefore potentially good of 2-rank zero; stable reduction has compact type. An unmarked stable compact-type genus-two fibre has no rational components.
* **Verified primary source:** Dupuy--Rabinoff, https://arxiv.org/pdf/1705.03034, Theorem 1.1 p.1 and Proposition 3.2 p.5, proof pp.5--6. The Abel map extends to the compact-type model and is a closed immersion when there are no rational special components. The 2-primary cusp divisor specializes to zero, so the cusp sections have exactly the same special point. The assertion applies also at a node. Source tool ref turn548view0.
* In a two-elliptic fibre, the hyperelliptic involution has proper H1 action -1, so it cannot exchange the components. On each supersingular component its unique geometric fixed point is the node. The common cusp specialization is therefore that node. It fixes both branches, hence the entire metric edge; the two exchanged cusps retract to the same interior point. On the inserted bridge, an involution fixing its two attachments is trivial in characteristic two. This proves collision at one smooth point of that bridge and the positive two-mark leaf edge.

## Actual action and unbounded algebra

* Betts--Dogra Definition 3.1.5 / Theorem 3.1.6 gives the based edge twists. The common leaf contributes `r ad(Omega)` to every handle; a separate elliptic arm adds `m_i ad(omega_i)`. Every displayed length is strictly positive. Smooth genus two has only the common leaf term.
* Handles have weight one, the selected cusp t has weight two. Packet comparison is through its actual punctured cusp disc and changes the first weighted derivation by `lambda ad(t)`. Equivalently, the inner discrepancy fixes t and hence its weight-two conjugator is a scalar multiple of t.
* For a smooth proper component, the first word of Omega is a1b1 with no self-overlap. The all-degree triangular Omega-bimodule basis reduces the first-core prefix to `lambda L_t+r R_Omega`, injective by t-count or right multiplication.
* For two components, the prefix operator is `K_i=N_B+lambda L_t+R_(r Omega+m_i omega_i)`. When lambda is nonzero, count t. When lambda is zero, use free generators Omega,omega_i,t: N_B and R_Omega preserve omega_i-count, while nonzero m_i R_omega_i raises it. This avoids the incorrect shortcut replacing N_B by a one-sided inner term.
* The remaining boundary algebra has kernel k<t,Omega> for lambda zero, k[t] otherwise. Taking primitives gives exactly L(t,Omega) or k t. This is an all-weight proof; finite matrices only check its conventions.
* A.38 applies to the unipotent closure of the actual derived-fixed subgroup. Both t and Omega carry chi, so its even weight 2m piece is scalar chi^m and odd pieces vanish. The criterion invokes Ribet only for actual finite-cover Jacobians and never lifts arbitrary rational Lie fixed elements.

## Executed support

`code/a_D4_fixed.py` and retained `.json` / `.out`: PASS.

The script checks the cusp function and hyperelliptic norm identities, the triangular basis through handle degree seven, and exact derivation identities. Modular ranks at 1000003 plus explicitly independent kernel vectors determine rational kernel dimensions through weight five for both geometric cases and packet scalars 0,1,-2. No integral saturation follows from these ranks or is claimed.

## Scope and non-claims

The result concerns actual full pro-prime fixed subgroups on all D4 first quotients, and combines with A.22 at prime two. It does not embed an odd-prime quotient through the proper unramified double map C4 to D4. It does not infer a nonzero primitive Collino class for the hyperelliptically conjugate cusps. In fact the displayed two-term hyperelliptic cycle has constant norm d^2; that limitation is irrelevant to the Tate-graded criterion.
