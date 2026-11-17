# Exact central coordinates and the actual modular quotient

New checkpoint33 research addendum. The complete central-refinement proof work_A/actual_congruence_central_refinement33.md remains unchanged at SHA-256 dae57e05b503c3c726cc899da193feb9d96a4e40cf459eec553a82efb50e4813. All formal sources remain frozen. This note retains its actual full-GT hypotheses and original marking.

## 1. An exact model of the first central quotient

Use \(F,C,N,N_1,F^{(2)},\pi_2\) from the preceding proof. To distinguish the pro-two kernel from the relative-central series, write
\[
M_2=\ker(F^{(2)}\to C_{(2)}),\qquad
M_{2,1}=\overline{[M_2,F^{(2)}]}.
\]
Then
\[
\boxed{N_1=N\cap F'\cap\pi_2^{-1}(M_{2,1}).}          \tag{1}
\]
One inclusion is commutator functoriality: \(N_1\subseteq N\cap F'\), and the continuous map \(\pi_2\) sends it into \(M_{2,1}\). Conversely take \(h\) in the intersection on the right. The preceding proof's exact character comparison says that every continuous \(F\)-invariant character of \(N\) is
\[
\chi=\chi_2\circ\pi_2|_N+\lambda|_N,
\]
where \(\chi_2\) is \(F^{(2)}\)-invariant on \(M_2\) and \(\lambda\) is a character of \(F\). The first summand kills \(h\) because \(\pi_2(h)\in M_{2,1}\); the second kills it because \(h\in F'\). Character separation of \(N/N_1\) proves the reverse inclusion.

Thus the natural map
\[
F/N_1\longrightarrow
C\times F_{\rm ab}\times\bigl(F^{(2)}/M_{2,1}\bigr)    \tag{2}
\]
is a continuous injection. Its source is compact and its target Hausdorff, so it is a topological embedding onto its actual closed image. This is not an assertion of surjectivity onto the whole product, nor an identification of a discrete kernel's abstract completion. Surjectivity of \(N\to M_2\) is not needed.

## 2. The full signed kernel has the actual geometric symmetries

Retain the original modular group
\[
B=C_2(s)\amalg C_3(r),\qquad
F=\ker(B\to S_3),\qquad \delta=sr,
\]
with \(x=\delta^{-2}\), \(y=sxs\), \(z=(xy)^{-1}\).
Let \(\iota=\operatorname{Ad}(s)|_F\) swap \(x,y\), and
\(\rho=\operatorname{Ad}(r)|_F\) cycle \(x,y,z\). The actual integral matrix
\[
R_0=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\qquad R_0^3=I,
\]
satisfies
\[
\operatorname{Ad}(R_0):X\mapsto Y\mapsto -Z\mapsto X,
\qquad Z=(XY)^{-1}.
\]
Therefore, for every \(g\in F\),
\[
q(\rho(g))=\operatorname{Ad}(R_0)(q(g))\,
                (-I)^{\operatorname{exp}_y(g)}.      \tag{3}
\]
This follows on the two free generators and hence on all of \(F\); the exponent on the right is read modulo two.

Modulo four, the original \(X_4=I+2E_{12}\) and \(Y_4=I-2E_{21}\) are independent commuting involutions. Explicitly
\[
q_4(g)=I+2(\operatorname{exp}_x(g)E_{12}
                      -\operatorname{exp}_y(g)E_{21}).
\]
Consequently every \(n\in N=\ker q\) has both exponent sums even. Its sign in (3) is one, giving \(\rho(N)\subseteq N\). Since \(\rho^3=1\), this is equality. The swap \(\iota\) is implemented under \(q\) by the integral matrix
\[
S_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
so \(\iota(N)=N\) as well. Inner conjugation by \(F\) already preserves \(N\). Hence \(N\) is a closed normal subgroup of \(B\). Every
\(N_{r+1}=\overline{[N_r,F]}\), and \(N_\infty\), is likewise stable under these actual geometric symmetries.

**Exact distinction and superseded warning.** The subgroup \(\ker(q_3)\) on all \(F\) is not \(\rho\)-stable: \(y^3\) has image one under \(q_3\), whereas its cyclic image \(z^3\) maps to \(-I\). During review that example was momentarily used to warn against \(\rho\)-stability of the full \(N\). That warning is superseded by (3) and the modulo-four calculation: \(y^3\notin N\). DE's derived-kernel construction for \(\ker(q_3|F')\) is unaffected. The result here proves the actual geometric \(S_3\)-stability, not characteristicity under every automorphism of \(F\).

## 3. A genuine normalized automorphism on the central modular quotient

Let
\[
B_1=B/N_1,\qquad E_1=F/N_1\triangleleft B_1.
\]
This is a well-defined profinite quotient by §2. Its quotient by \(E_1\) is the original \(S_3\).

For the actual canonical word put \(v=u^{-1}s=su\). Duality gives \(v^2=1\). The previously proved exact marked identity is
\[
H_d=u\,\bigl((v\delta^d)^3\bigr)^{-1}u^{-1}.          \tag{4}
\]
It is the literal ordered identity of the original three-cycle/hexagon proof, not a new conjugacy choice. The central-refinement theorem gives \(H_d\in N_1\); hence \((v\delta^d)^3=1\) in \(B_1\).

The universal property of the full free profinite product therefore defines an actual continuous homomorphism
\[
\Psi:B\to B_1,\qquad
s\mapsto v,\quad r\mapsto v\delta^d,
\quad\text{so }\delta\mapsto\delta^d.                \tag{5}
\]
Since \(u\in F\) and \(d\) is odd, this map induces the identity on the original \(S_3\) quotient: the images of \(s\) and \(\delta\) there are transpositions. On the actual \(F\), (5) gives
\[
x\mapsto x^d,\qquad y\mapsto u^{-1}y^du,
\]
which is exactly \(\psi_d\). This map preserves \(N_1\), so (5) descends to an endomorphism \(\Psi_1\) of \(B_1\). Its restriction to \(E_1\) is the already proved automorphism \(\psi_d\), and its quotient map on \(S_3\) is the identity. The kernel is therefore trivial: an element of the kernel first lies in \(E_1\), where injectivity applies. Surjectivity follows by first matching a coset in \(S_3\), then correcting in \(E_1\). Thus
\[
\boxed{\Psi_1\in\operatorname{Aut}(B_1).}             \tag{6}
\]

Retain the genuine original extensions of \(\alpha\) and complex conjugation \(c_B\) to \(B\):
\[
\alpha(\delta)=\delta^{-1},\quad\alpha(s)=s\phi,
\qquad c_B(\delta)=\delta^{-1},\quad c_B(s)=s.
\]
Both preserve \(N_1\); on \(F\), this is the already proved \(\alpha\)- and \(c\)-stability. The canonical norm and the two-cycle identity give \(\alpha(v)=v\). Hence, on the generators \(s,\delta\) of \(B\),
\[
\alpha\Psi=\Psi c_B.
\]
After descent and (6), this becomes the exact conjugacy
\[
\boxed{\alpha|_{B_1}=\Psi_1c_B\Psi_1^{-1}.}           \tag{7}
\]
No unproved full homomorphism \(B\to B\) has been introduced: the target is specifically \(B/N_1\), where the cubic relation was proved first. No claim is made that \(N_1\) is pro-two, that it is characteristic under all automorphisms, or that an arbitrary relative-lifting theorem applies. For higher \(N_r\), the previous note proves automorphy and intertwining on \(F/N_r\), but does not prove the cubic relation needed to extend those maps to \(B/N_r\).

## 4. Provenance and limits

Equation (1) is a direct consequence of the fully proved character comparison, with no new external theorem. Equation (3) uses the original integral cyclic matrix from A.103 and the literal signed modulo-four marking. Equation (4) is the established original marked three-cycle identity, and has the same \(u,d,k\) as A.103 and the central-refinement theorem.

CE independently checked (1)--(3) in conversation before this source save; the whole saved proof and (5)--(7) are being sent for complete review. The parent independently accepted the full-versus-mod3 kernel correction before save. No finite target, mathematical producer, private build or render was used.

The new conclusion is the actual normalized modular automorphism and involution conjugacy on the first central congruence quotient. It does not decide full Main A, the actual full hexagon, the remaining CM sign, or surjectivity on \(N_\infty\).

