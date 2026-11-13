# Independent audit of E.53

The full proof in `sections/E_symplectic_integral_common_root.tex` passes the geometry agent's independent read. The fixed source certificate was replayed in an isolated output directory in 4.551 seconds. Every mathematical JSON field agrees, and every protected original hash is unchanged. The independent wrapper and its records are `code/bc_symplectic_integral_gl_comparison_audit.py`, `.out`, and `.json`.

## Exact signed map

The actual modular matrices on the pure free generators, with the unique sign giving both diagonal entries one modulo four, are

\[
x\longmapsto E_{12}(2),\qquad y\longmapsto E_{21}(-2).
\]

Their component away from two is precisely \(P\theta P^{-1}\), with \(P\) the coordinate swap used in E.50. Their component modulo four is determined by the two literal exponent sums. The new certificate checks this identity on all 97 actual generators of \(N\) and all five actual Schreier generators of \(K_2\). On \(F'\), the four-component is the identity, so the existing signed map \(G_L\to Q_{20}\) forces the exact, rather than projective, equation \(\theta\equiv I\pmod5\) for every correcting word in \(\ker\rho_L\).

The induced map

\[
G_m/Q_m\longrightarrow A_{2m}\times_{A_2}Q_{4m}
\]

has the stated common kernel, and the displayed orders prove surjectivity. Its generator maps commute with reduction. This is an isomorphism of the specified source images.

## Local normal subgroups and the central additive factor

For \(p\ge5\), the first nonzero congruence layer of an open normal subgroup of \(\operatorname{SL}_2(\mathbf Z_p)\) is the full adjoint module. The interpolation argument at \(0,1,-1\) proves stability under \(e,f,h\), and the distinct \(h\)-weights \(0,2,-2\) give irreducibility. The explicit \(p\)-th power formula moves each basis vector to every later layer. Successive approximation proves containment of the whole congruence subgroup. An element above \(-I\) differs from \(-I\) by a principal-congruence element whose square is trivial in a finite \(p\)-group; hence that difference is trivial. These steps give exactly the principal congruence subgroups, their products with \(\{\pm I\}\), and the whole group.

A closed normal subgroup surjecting modulo \(p\) is the whole group: its quotient is pro-\(p\) and topologically perfect, so each finite quotient is both a \(p\)-group and perfect and is trivial. This is the precise closed-subgroup extension of the open-subgroup step.

The centre of every finite local quotient has exponent at most two. In the projective quotient, a central element first has scalar reduction modulo \(p\); its commutators with elementary matrices cannot be the negative sign, and hence are the identity. Commutation with both elementary generators then forces the representative to be scalar. In a finite quotient of the product of the local groups, the factor images commute; every factor in a central product is central in its own image. The centre of that quotient again has exponent at most two.

The common quotient of \(C_R\) with the perfect group \(C_L\) is finite and perfect. Its image from the additive factor is central, while its entire group is an image of \(\operatorname{SL}_2(R)\). The centre result and the prime-to-six additive order force the additive image to be trivial. Thus the correcting image contains all of \(V_3(R)\).

## The exact five-adic level

The complete signed source has exact orders 30 on both \(x,y\); the used relations \(x^{60}=y^{60}=1\) are consequently valid. The independently expanded matrix identity is

\[
[E_{21}(t),E_{12}(1)]
=\begin{pmatrix}1-t&t\\-t^2&t^2+t+1\end{pmatrix}.
\]

At \(t=120\), its reduction modulo 25 is \(\left(\begin{smallmatrix}6&20\\0&21\end{smallmatrix}\right)\). The three saved conjugate Lie vectors have determinant 3 in their three coordinates, so they span \(\mathfrak{sl}_2(\mathbf F_5)\). The actual word is \([x^{60},c]\), where \(c\in R_{\mathrm{nil}}\) has the specified elementary matrix image. Normality places this word in both required kernels. Powers and closedness give all of \(\Gamma_5(1)\); the signed comparison above gives the reverse containment modulo five. The already proved seven-adic surjection and the order exclusion at primes at least eleven give the remaining full factors.

## Whole-source quotient and retained maps

After quotienting by the exact correcting subgroup, the remaining kernel of the map to \(\mathcal J_5\) injects into the even exponent coordinates. The two actual source words \(x^{60},y^{60}\) give \((30,0),(0,30)\). Their closed spans are \(5R^2\), since \(30R=5R\). This proves the entire kernel equality, including its abelian part, and hence the maximum common quotient. It does not rely only on matching quotient orders.

The complete \(D_{23}\) image is a solvable group supported at two and three. Every finite solvable quotient of the correcting image is supported at primes at least five. Goursat therefore gives the unchanged correcting image after imposing the actual \(D_{23}\) kernel. The additional level-five and level-seven maps factor through \(\rho_R\), so imposing their kernels gives exactly the displayed intersection in E.53.5. This retains the stated full source cosets. Membership in the closed lower-central residual kills each nilpotent quotient at its actual nilpotency class and then every inverse limit of such quotients.

The existing choice in E.43.11 already has \(\chi(\sigma)=1\), with the required Kummer value. Consequently it also satisfies the uniform multiplier-one requirement for the integral tower. No additional Galois selection assertion is required here.

## Preserved wrapper attempt

The first independent wrapper reproduced the full root certificate and passed the mathematical JSON comparison, then rejected an unexpanded symbolic matrix expression under SymPy's structural equality. Exact simplification gives the zero difference. That wrapper and the explanation are preserved in `research/audit_geometry_integral_gl_comparison/first_wrapper_attempt/`. The corrected wrapper uses exact simplification. No root certificate or frozen result was changed.
