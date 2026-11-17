# The full profinite elliptic section and a pentagon-only marked cubic

Checkpoint35 research continuation, intended for subsequent independent review. No frozen formal source is changed. This note distinguishes the published full profinite section, a consequence whose proof needs only the pentagon, and the still missing comparison to the original CM frame.

## 1. Primary source, completion, and convention

Primary reference: Enriquez, B. (2014). Elliptic associators. *Selecta Mathematica, 20*(2), 491–584. https://doi.org/10.1007/s00029-013-0137-3. The complete proof used here was read in the author's arXiv version 1003.1012v3 (26 July 2012), https://arxiv.org/pdf/1003.1012, §2.6, Proposition 2.20, printed pp.14–18 (PDF indices13–17).

Proposition 2.20 gives a section of the elliptic-to-usual GT semigroup map in the full profinite category, as well as the other categories named there. If K=[Y,X], its formulas are

\[
 g_+(X,Y)=f(X,K)X^\lambda f(X,K)^{-1},
 \qquad
 g_-(X,Y)=K^m f(YX^{-1}Y^{-1},K)Yf(X,K)^{-1},
 \quad m=(\lambda-1)/2.                                      \tag{1}
\]

The section sends the identity to the identity, so it sends units to units: applying its multiplication law to a unit and its inverse proves this directly. Thus an actual full-GT involution has an elliptic involution. The induced two-generator abelianization is diag(lambda,1).

The paper uses the commutator [a,b]=aba^{-1}b^{-1}, as does the present project. Its braid-coordinate convention fixes the second free generator and conjugates the first. Interchanging the two free generators and using the original duality identifies this with the project's convention x↦x^lambda, y↦f^{-1}y^lambda f. We retain the original word f and do not replace it by an arbitrary normalized conjugator. The semigroup convention in the paper's endomorphism factor is opposite composition; no conclusion here depends on silently reversing that convention.

The assertion about the full profinite section is a primary theorem, not an inference from its prounipotent analogue. Its existence does not say that the particular GT0 lift Gamma of A118 belongs to full GT, or that the pair (d,u) already satisfies the missing hexagon.

## 2. The exact reduced elliptic braid group

Write sigma=sigma_1, tau=sigma_2, X=X_1^+, Y=X_1^-. We use the full profinite completion of the discrete reduced elliptic braid group B_{1,3}. Its marked presentation is the n=3 case of §1.2, equation (7) of the primary source:

\[
\begin{gathered}
 \sigma\tau\sigma=\tau\sigma\tau,\qquad [X,\tau]=[Y,\tau]=1,\\
 (\sigma X)^2=(X\sigma)^2,\qquad
 (\sigma^{-1}Y)^2=(Y\sigma^{-1})^2,\qquad
 [Y,X_2^{-1}]=\sigma^2,\\
 X_2=\sigma X\sigma,\quad X_3=\tau X_2\tau,\quad XX_2X_3=1,\\
 Y_2=\sigma^{-1}Y\sigma^{-1},\quad
 Y_3=\tau^{-1}Y_2\tau^{-1},\quad YY_2Y_3=1.
\end{gathered}                                                \tag{2}
\]

In particular the same-sign X_i commute, as do the Y_i. Put

\[
 K=[Y,X]=\sigma\tau^2\sigma,
 \qquad L=\tau^{-1}\sigma^{-1},\qquad
 K_2=\tau\sigma^2\tau.                                      \tag{3}
\]

These are the marked identities used below; the displayed K is not a new peripheral generator of the original free rank-two group.

The primary type-B braid map is

\[
 (B_4/Z(B_4))\times_{S_4}S_3\longrightarrow B_{1,3},
 \qquad \sigma_0^2\mapsto X,\quad
 \sigma_1\mapsto\sigma,\quad\sigma_2\mapsto\tau.             \tag{4}
\]

It is induced by the stated multiplicative-torus configuration map in Proposition 2.20, proof part1. We need only this homomorphism, not injectivity or a completion recognition theorem. Every displayed discrete homomorphism gives a continuous homomorphism on full profinite completions by the universal property.

## 3. A statement requiring only the actual pentagon

Let w be a profinite commutator word in two free generators satisfying the original four-strand pentagon. No hexagon, scalar multiplier, canonical norm, or assumed automorphism associated to w is needed for the following conclusion:

\[
 \boxed{\mathcal P_w^3=1,\qquad
 \mathcal P_w=
 L\,w(YX^{-1}Y^{-1},K)\,Y\,w(X,K)^{-1}\,w(\sigma^2,\tau^2)}
 \quad\text{in }\widehat B_{1,3}.                          \tag{5}
\]

This is the negative elliptic cubic of (1), with the adjacent powers K^{-m}K^m cancelled. Its proof below isolates exactly which input is used.

### 3.1 The original pentagon, with every argument fixed

In B_4 with Artin generators sigma_0,sigma_1,sigma_2, put a=sigma_0^2, c=sigma_1^2, f_br=sigma_2^2 and use the standard pure generators (a,b,c,d_br,e,f_br)=(A12,A13,A23,A14,A24,A34) of A94/A118. The exact products are

\[
 ce=\sigma_1\sigma_2^2\sigma_1,\quad
 bc=\sigma_1\sigma_0^2\sigma_1,\quad
 ab=\sigma_0\sigma_1^2\sigma_0,\quad
 ef_{\rm br}=\sigma_2\sigma_1^2\sigma_2.                     \tag{6}
\]

Thus the project's literal pentagon w(a,ce)w(bc,f_br)=w(c,f_br)w(ab,ef_br)w(a,c) is the same ordered braid identity used in (4). In the middle factor, sigma_1^2 commutes with both arguments and

\[
 (\sigma_1\sigma_0^2)^2
       =(\sigma_0\sigma_1^2\sigma_0)\sigma_1^2.
\]

A commutator word is unchanged by such a common commuting decoration. Applying (4), using X_2X=X_3^{-1}, gives precisely

\[
 w(\sigma^2,\tau^2)\,w(X_3^{-1},K_2)\,w(X,\sigma^2)
       =w(X,K)\,w(X_2,\tau^2).                             \tag{7}
\]

This step uses the original pentagon, not an equation assigned to a new residual word. The decoration identity holds for profinite commutator words by continuity, or directly by the universal map from the two-generator free profinite group and its abelianization.

### 3.2 Ordered conjugation to a three-factor norm

Relations (2) give

\[
 L(YX^{-1}Y^{-1})L^{-1}=X_3^{-1},\qquad LKL^{-1}=K_2.
\]

Consequently the word in (5) is conjugate, by two cyclic rotations of its factors, to

\[
 Y\,w(X,K)^{-1}w(\sigma^2,\tau^2)w(X_3^{-1},K_2)L.
\]

Using (7), this is

\[
 T_w=Y A_w L,\qquad
 A_w=w(X_2,\tau^2)w(X,\sigma^2)^{-1}.                       \tag{8}
\]

For clarity, the conjugation order is exact. If E=w(X_3^{-1},K_2), then P_w=E L Y w(X,K)^{-1}w(sigma^2,tau^2). Conjugate by E^{-1}, then by L^{-1}; the result is (8).

Set B=tau sigma and C=sigma tau. The literal identities

\[
 LY=Y_3B,\qquad BLY=Y_2C,\qquad CL=1
\]

give the direct expansion

\[
 T_w^3=Y A_wY_3\,\operatorname{Ad}(B)(A_w)
                     Y_2\,\operatorname{Ad}(C)(A_w).        \tag{9}
\]

No cyclic exponent or central full twist has been dropped in (9).

### 3.3 Complete cancellation using only the marked braid relations

Define the following four actual evaluations:

\[
\begin{aligned}
 B_w&=w(X_2\sigma^{-2},\tau^2),\\
 D_w&=w(\tau\sigma^2\tau^{-1}X,\sigma^2),\\
 E_w&=w(X_3\tau^{-1}\sigma^{-2}\tau^{-1},\tau\sigma^2\tau^{-1}),\\
 F_w&=w(X_3\tau^{-1}\sigma^{-2}\tau,\tau\sigma^2\tau^{-1}).
\end{aligned}                                                \tag{10}
\]

The required argument transformations from (2) are

\[
\begin{gathered}
 YX_2=(X_2\sigma^{-2})Y,\quad [Y,\tau^2]=1,\quad
 XY_3=Y_3(\tau\sigma^2\tau^{-1}X),\quad[\sigma^2,Y_3]=1,
 \quad YY_3=Y_2^{-1},\\
 \operatorname{Ad}(B)(X_2)=\tau\sigma^2\tau^{-1}X,
 \quad\operatorname{Ad}(B)(\tau^2)=\sigma^2,\\
 \operatorname{Ad}(B)(X)=X_3\tau^{-1}\sigma^{-2}\tau^{-1},
 \quad\operatorname{Ad}(B)(\sigma^2)=\tau\sigma^2\tau^{-1},\\
 \operatorname{Ad}(C)(X_2)=X_3\tau^{-1}\sigma^{-2}\tau,
 \quad\operatorname{Ad}(C)(\tau^2)=\tau\sigma^2\tau^{-1},\\
 \operatorname{Ad}(C)(X)=X_2\sigma^{-2},
 \quad\operatorname{Ad}(C)(\sigma^2)=\tau^2.
\end{gathered}                                                \tag{11}
\]

Substituting these transformations, in their printed order, yields

\[
 YA_wY_3=B_wY_2^{-1}D_w^{-1},\qquad
 \operatorname{Ad}(B)(A_w)=D_wE_w^{-1},\qquad
 \operatorname{Ad}(C)(A_w)=F_wB_w^{-1}.                       \tag{12}
\]

Finally the remaining two argument identities are

\[
\begin{gathered}
 Y_2^{-1}(X_3\tau^{-1}\sigma^{-2}\tau^{-1})Y_2
          =X_3\tau^{-1}\sigma^{-2}\tau,\\
 [Y_2,\tau\sigma^2\tau^{-1}]=1.
\end{gathered}
\]

Hence Y_2^{-1}E_wY_2=F_w. Equations (9) and (12) give

\[
 T_w^3=B_wY_2^{-1}E_w^{-1}Y_2F_wB_w^{-1}=1.
\]

Since P_w is conjugate to T_w, (5) follows. This is a complete symbolic argument in the actual marked group. There is no finite target search or numerical producer. All transformations are literal discrete braid identities, and the evaluations of the profinite word extend them continuously.

## 4. Actual canonical and normalized residual specializations

For the original negative involution alpha in full GT, A37 proves that its unique canonical u in F' satisfies the full pentagon. It therefore satisfies (5). This conclusion is not asserted for an arbitrary negative GT0 involution: A37's full-GT hypothesis remains in force.

For any m in Zhat, define the candidate g_-[w,m] by the second formula of (1). Then

\[
 \bigl(LK^{-m}g_-[w,m](X,Y)w(\sigma^2,\tau^2)\bigr)^3=1
\]

is exactly (5), because the adjacent K powers cancel. In particular m=k=(d-1)/2 is allowed for the actual canonical d. This does not assert the other defining elliptic relations for (d,u,g_+,g_-). The published verification of the positive cubic uses the usual GT braid action, and its commutator-relation proof explicitly uses the hexagon. Neither verification may be applied to (d,u) by assuming the result under investigation.

There is also an exact transported version after A118. Write Gamma=(d,f), U'=Gamma^{-1}(f^{-1}u), so u=f Gamma(U'). For every pair (p,q) in any profinite target define

\[
 \mathcal U_{p,q}
   =f(p,q)\,U'\bigl(p^d,f(p,q)^{-1}q^df(p,q)\bigr).
                                                               \tag{13}
\]

The original free-generator formula for Gamma gives U_{p,q}=u(p,q). Therefore the exact residual constraint is

\[
 \boxed{\left(
 L\,\mathcal U_{YX^{-1}Y^{-1},K}\,Y\,
       \mathcal U_{X,K}^{-1}\mathcal U_{\sigma^2,\tau^2}
 \right)^3=1.}                                                \tag{14}
\]

Formula (14) uses only pairwise evaluations. It does not need an elliptic braid action of Gamma, and does not assume that Gamma extends from GT0 to full GT. Removing the f factors or replacing the three U evaluations by an ordinary pentagon/cubic for U' would change the proven constraint. Although U' belongs to the actual residual R in its original free group, its images under the three new pair maps are not declared trivial or assigned to a newly identified kernel.

## 5. Literal comparison with the original CM sewing condition

The complete original LM7_PUSH E61 source was reread at this use. Its specified multiplier-one sewing word is R_rho(f) in B4, with the four E-factors and both frame powers retained. Its actual affine map eta_m has

\[
 \eta_m(R_\rho(f))=((-B-8\rho A,A-1)^t,I)
 \quad\text{when }f(U^2,L^2)=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
\]

The signed modulus-twelve calculation makes this image one for every normalized full gentle multiplier-one pair, including the extra CM branch. Reusing that same projection cannot decide the original parity. The full type-B sewing equation (IV), in that source's notation,

\[
 f(u,v^2)=v^{4\rho}f(u^2,v)u^{4\rho}(uv)^{-4\rho},
\]

is applied there only on the stated Nakamura–Schneps subgroup. The full profinite elliptic section is a different theorem and supplies no automatic identification of its chosen Tate-coordinate frame with that sewing frame.

A simple marking check blocks the most literal attempted substitution. The K in (1) is a commutator. In the original B3 sewing source u=tau_1 and v=tau_2^2, the exponent-sum character sends v to2 and its central full twist z_3 to6. A homomorphism cannot send K to v z_3^b or v^2 z_3^b for any b in Zhat: their exponent sums would be 2+6b or 4+6b, neither zero modulo3. This excludes only those specified identifications, not a differently based higher-strand comparison.

The remaining concrete task is to construct and verify a based comparison from the elliptic element P_u (or (14)) to the ORIGINAL coherent r-frame/CM comparison, preserving all central powers and the actual negative frame. No such comparison, vanishing of H_d, value of the coherent class, or CM-parity conclusion is proved here. The full elliptic section for alpha alone also does not classify its negative elliptic involution up to the required normalized conjugation.

## 6. Exact read and verification record

Fresh primary reads: §1.2 and its complete B_{1,n} presentation; §2.1–§2.2 definitions and Lemma2.1/Proposition2.2 with their displayed proof; the full statement and all five proof parts of Proposition2.20, including its final explicit extension to the full profinite category. The proof was read across bounded primary PDF outputs, not inferred from an abstract or a truncated combined output. The arXiv printed pages are3–8 and14–18; the proposition itself is printed14–18. This is not a claim to have read the entire67-page paper or its later arithmetic sections.

Primary retrieval references at this use: turn1211view0 (PDF), turn1214view0, turn1215view0 and turn1216view0 (complete proposition across overlapping bounded reads), turn1218view0, turn1219view0–1 and turn1220view0 (definitions/presentation). The paper's commutator convention is explicitly printed in footnote3, p.3.

Fresh internal source reads: the entire A37 statement/proof and scope paragraph; A94's exact original generator and pentagon displays and Artin-marking explanation; the entire original LM7_PUSH E61 source at recovered_inputs32/background/expanded/LM7_PUSH_checkpoint_09/sections/E_genus_one_sewing_agent.tex. The earlier attempted combined E64/referee output was truncated and is not counted as a complete new read. No full E65 reread or new E64 geometric dependency audit is claimed in this note.

The full profinite section is the cited primary result. Equations (5)–(14) are the explicit hypothesis audit and ordered specialization proved above. Their mathematical verification is symbolic; no program, output, file rendering, finite census or new formal promotion is claimed.
