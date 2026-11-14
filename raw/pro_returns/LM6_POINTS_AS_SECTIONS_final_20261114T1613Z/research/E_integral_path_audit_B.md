# Independent audit of E.39 and final main-route assessment

**Auditor:** Part B/C contributor.  **Date:** 14 November 2026, five-hour reassessment.

**Verdict:** the complete statement and proof of E.39 pass this review. The comparison has the stated finite cohomology kernels. The available compact and unit cohomology classes do not specify an integral lift through this comparison. The actual integral tangential path lift has not been computed. E.39 correctly leaves open whether further use of the automorphism identities constrains that lift.

## Material read

I read `sections/E_integral_path_comparison.tex` in full, including its assertion for both absolute Galois groups and their quotients unramified away from three and infinity. I reopened the actual cusp coordinates and Galois matrices (E18.8)–(E18.9) in `sections/E_extra.tex`, and the geometric path construction, unit definitions, and Kummer comparison (E36.3)–(E36.8) in `sections/E_kummer_values.tex`. I also inspected the complete program `code/root/integral_path_comparison.py` and its executed output `code/root/integral_path_comparison_output.json`. This review uses the exact maps in those files; it does not substitute an arbitrary rational splitting for the integral lattice.

## 1. The unit rows are the actual geometric maps

Write $V=\mathbb Z_3^2\oplus\mathbb Z_3^8$ in the integral basis of E.18. The eight boundary coordinates correspond, in order, to

\[
A_0,A_1,A_2,B_0,B_1,B_2,C_1,C_2.
\]

The normalized tangent-line unit $f_d=L_d/L_O$ has divisor $3(d-O)$. Its geometric Kummer map therefore restricts to $3e_d^*$ on the boundary lattice. The actual equivariant Tate map $j_{0*}$ has columns $\binom{3I_2}{U}$. Its rational image is the compact summand. At a good Frobenius, its compact eigenvalues have absolute value $\sqrt q$, whereas the target $\mathbb Q_3(1)$ has eigenvalue $q$. Equivariance therefore makes a unit map vanish on that summand. Writing its first two coefficients as $r_d$, this gives

\[
3r_d+3U_d=0,
\qquad \ell_d=(-U_d,3e_d^*).
\]

Thus the matrix in E39.1 is the actual compact-and-unit comparison

\[
j(a,b)=(a,-Ua+3b),
\]

not only an integral matrix with the same rationalization. The normalized equations in E.36 are permuted by complex conjugation; scalar normalizations would not change their geometric Kummer maps in any event. The target action is the compact action together with the cyclotomic action times the stated cusp permutation.

## 2. Exact coefficient quotient and its Galois action

The explicit quotient map is

\[
q:T_3E\oplus\mathbb Z_3(1)^8\longrightarrow\mathbb F_3^8,
\qquad q(x,y)=y+Ux\pmod3.
\]

It is surjective. The condition $q(x,y)=0$ is equivalent to $y=-Ux+3b$ for an integral $b$, so its kernel is precisely the image of $j$. This proves the short exact sequence without relying on a numerical Smith calculation. The Smith factors $1,1,3,3,3,3,3,3,3,3$ in the certificate agree.

Over $K=\mathbb Q(\zeta_3)$, the boundary coordinates are individually fixed apart from the cyclotomic action, and $\chi_3\equiv1\pmod3$. The divided block $U(A_E-\chi_3 I)/3$ in E18.9 is integral, giving

\[
UA_E\equiv\chi_3U\pmod3.
\]

Consequently $q(g(x,y))=q(x,y)$ over $G_K$. For complex conjugation the same calculation uses $UC_E\equiv C_TU\pmod3$, and its quotient action is $C_T=-P_c$. The two permutation-fixed coordinates $A_0,B_0$ contribute no invariants in characteristic three. Each transposed pair contributes one anti-diagonal invariant. Hence

\[
Q^{G_K}=\mathbb F_3^8,
\qquad
Q^{G_{\mathbb Q}}=
\langle e_{A_1}-e_{A_2},e_{B_1}-e_{B_2},e_{C_1}-e_{C_2}\rangle
\simeq\mathbb F_3^3.
\]

## 3. The cohomology kernels are genuine torsion classes

The middle coefficient module has no invariants for either absolute group or either stated unramified quotient. This can already be checked at a prime over seven: the compact Frobenius eigenvalues are $1+3\zeta_3$ and its conjugate, neither equal to one, while the toric eigenvalue is seven. All these representations factor through the stated unramified quotients.

The continuous long exact sequence therefore injects $Q^G$ into $H^1(G,V)$, with image exactly $\ker H^1(G,j)$. A finite quotient of these coefficient modules admits a continuous set-theoretic section, which supplies the usual continuous-cochain exact sequence used here. It follows that every nonempty fibre of $H^1(j)$ has exactly $3^8$ elements over $K$ and $3^3$ over $\mathbb Q$, for both types of Galois group.

For a boundary vector $t_d$, its rational lift $t_d/3\in V\otimes\mathbb Q_3$ maps under $j$ to the integral target vector $(0,e_d)$. Thus

\[
b_d(g)=g(t_d/3)-t_d/3
      =\frac{\chi_3(g)-1}{3}t_d \quad(g\in G_K)
\]

is exactly the connecting cocycle. It is integral because $\mu_3\subset K$. Its compact image is zero; its unit image is the target coboundary $g(e_d)-e_d$. At both free generators $\tau,\tau'$, the value is $2t_d$, since their cyclotomic values are seven. Multiplication by three gives the coboundary of $t_d$. Injectivity of the connecting map proves that each nonzero quotient vector gives a nonzero class of exact order three.

The three anti-diagonal lifts are fixed by $C_T$ integrally. Their connecting cocycles vanish at complex conjugation. Therefore normalizing a path cocycle to have value zero at $c$ leaves the stated $\mathbb F_3^3$ ambiguity over $\mathbb Q$.

## 4. Exact remaining path comparison

For each automorphism $a$, the geometric construction in E.36 supplies one actual integral abelianized path class. Its compact image is the Kummer class of $aO-O\in E[3]$, and all eight unit images are known leading-coefficient Kummer classes. E.39 proves the size and explicit connecting cocycles of the cohomological fibre containing that actual class. It does not assert that every element of the fibre is the class of the specified geometric path.

Separately choosing representatives of the compact Kummer class and the eight unit Kummer classes, then solving the displayed matrix equation, selects a lift only after further choices. Changing those representatives can introduce the nonzero connecting classes above. The existing Frobenius matrices and the numerical Kummer values do not identify those choices with the divisions and roots transported by the common geometric path.

The remaining comparison is to compute, for the actual tangent transported by each $a$, the correlated compact division points and compatible unit roots, or another exact geometric datum that determines the same element of the finite comparison fibre. Such a computation has not been completed. The identities $(a-1)[\eta]=[\alpha_a,w]$, together with compatibility among automorphisms, may impose additional constraints; this audit makes no assertion that they cannot do so. No executed calculation presently selects the actual path classes or extracts an additional integral torsion coordinate of $\eta$ from that system. The rational average and the proved detector calculations remain valid.

## 5. Final assessment of the three remaining main routes

| Main item | Established advance | Exact point at which the attempted route stops |
|---|---|---|
| Nonisotrivial relative section realization over finitely generated p-adic fields | B.38–B.40 preserve the original generic section through the actual fundamental-group pullback and prove unramification; B.41 completes the isotrivial case, with the stipulated local theorem as recorded input. | Realizing the resulting point-theoretic relative group section as an algebraic section of a nonisotrivial family is unproved. The inspected dominant/open Hom theorem does not apply to that image, and the inspected relative theorem invokes the generic section conjecture at the missing step. B.42's Tate cover disproves the attempted inference from points on all closed fibres to a point on the generic finite cover. No completed full étale-topos comparison or replacement realization construction is available. |
| Genus-three free reflection and the nonorientable genus-four centralizer | C.18 gives the exact comparison with automorphisms of the profinite orientation-double-cover extension. C.17 settles the procongruence centralizers for the five genus-three types with ovals. | Density of the discrete $\operatorname{Mod}(N_4)$ in the group identified in C.18 is unproved; the corresponding full-completion kernel and extra involution classes also remain. C.19 excludes the proposed finite-index discrete hyperelliptic route. The inspected homological-congruence and profinite-orbit results do not supply the required simultaneous centralizer approximation. No finite calculation currently closes this global density step. |
| Cubic three-adic Ross edge and residual integral path data | E.35 identifies the elliptic projection with the exact compact edge of the Ross symbol. E.36 evaluates the rational nonelliptic coordinates. E.37–E.38 provide integral and continuous-cohomology detector results. E.39 now computes the exact information lost by compact and unit path comparisons. | The elliptic Ross regulator at the ramified bad prime three has not been evaluated or proved nonzero. The opened regulator comparison theorems have the precise excluded-prime or curve hypotheses recorded in `E_ross_ramified_audit.md`; the all-prime Iwasawa input does not itself identify this Ross class. The final integral automorphism attempt reaches the finite correlated-root/path comparison described above, with no actual integral path class yet computed. |

These are records of the inspected proofs and attempted calculations, not claims that no future theorem or calculation can relate the remaining objects. At this reassessment there is no completed executable step that resolves one of these three remaining main items. Expansion stops here; these three items remain incomplete.
