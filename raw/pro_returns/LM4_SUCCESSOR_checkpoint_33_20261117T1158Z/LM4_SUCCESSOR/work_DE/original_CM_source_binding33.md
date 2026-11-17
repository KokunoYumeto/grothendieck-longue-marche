# Complete original-source audit: E.61/E.65 and the actual CM signs

Saved after explicit checkpoint32 release on 2026-11-17. This
materializes the complete read-only DE audit while capture32 ran.
All32 bytes remain unchanged. All five sources were actually read
in bounded, untruncated chunks; no old certificate was executed.

## 1. Exact source bytes

The first two paths are relative to
/workspace/scratch/a50d05093ca1/recovered_inputs32/background/expanded/LM7_PUSH_checkpoint_09/.
The referee file is in the sibling background/expanded/referee/
directory, not under checkpoint09.

| Entire source | Lines | SHA-256 |
|---|---:|---|
| sections/E_cm_character_agent.tex | 327 | 45fb24828a71b3a2444f32b99625a594092732222065515f848bd49e022f15b9 |
| sections/E_genus_one_sewing_agent.tex | 267 | 6957b7565c585852ec94882e3558a738ba34678119b2f14a8fab7dea6ace8925 |
| background/expanded/referee/REFEREE_B_E61_E65.md | 252 | 0faa565d68df0bdf0d1370dd090529375ccfeb51b22135102a7efab187c06581 |
| work_A/outage32_original_r_frame_CRT_normalizer.md | 88 | c46c88b59fbeed5a6642ea1db138851039ab3806ac09fc50bf8ef339a12a120a |
| work_A/outage32_original_beta_frame.md | 78 | 36e387011d94c817e8e5efd5cc3936e00807d70365ea0e71e083059941049aeb |

This binds the definitions and the comparison below. It is not a
claim that every external theorem mentioned by the referee was
freshly reopened or reproved here.

## 2. Exact action and original frames

Let \(\alpha\) be the actual negative involution, \(c\) the retained
Galois complex conjugation, and \(\Sigma=\alpha c\). Then
\(f_\Sigma=\phi\). E.61.1 and E.65.1 use
\[
 \Sigma(s)=s\phi=\beta_s s\beta_s^{-1},\qquad
 \Sigma(r)=\phi^{-1}r=A_r rA_r^{-1},
 \quad A_r,\beta_s\in\widehat F,
\]
with \((\beta_s^{-1})^{\rm ab}=(\rho,\rho)\). These are exactly
the outage frames and composition order. The referee checks
conventions and uniqueness and supplies the omitted existence
argument for the pure r-frame. Signed coordinates apply to
multiplier-one \(\Sigma\); they are not confused with E.65's
projective coordinates for general multipliers.

## 3. Original signed correction

E.61.3 and E.65.2 specify
\[
 X=\begin{pmatrix}1&2\\0&1\end{pmatrix},\
 Y=\begin{pmatrix}1&0\\-2&1\end{pmatrix},\
 U_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\
 L_0=\begin{pmatrix}1&0\\-1&1\end{pmatrix},
\]
and, modulo twelve,
\[
 V=U_0^{8\rho},\qquad
 T=q_{12}(A_r)^{-1}V,\qquad
 W=q_{12}(\beta_s)^{-1}V.
\]
Thus the printed signed lift is explicit, rather than an arbitrary
representative of a projective class. Direct reduction gives
\[
 V_4=I,\qquad V_3=X^\nu,\qquad \nu=\rho\bmod3.
\]
This is the outage argument's canonical even-power lift. Its cube
is \(I\); the negative lift has cube \(-I\) and is not substituted.

## 4. Integral J and mod-three r-frame

The notation must distinguish
\[
 J=R_0=-U_0L_0=
 \begin{pmatrix}0&-1\\1&-1\end{pmatrix}\quad\text{over }\mathbb Z,
 \qquad C=J\bmod3=XYX^{-1}\bmod3.
\]
The integral word \(XYX^{-1}\) is NOT \(J\). The outage formula
\(C=XYX^{-1}\) is only a mod-three statement.

Conjugation by the ORIGINAL \(r\) cycles \(x,y,z\). Its matrix
on abelianization is
\(\left(\begin{smallmatrix}0&-1\\1&-1\end{smallmatrix}\right)\).
Since
\(\phi=rA_rr^{-1}A_r^{-1}\in\widehat F'\),
the determinant-three matrix \(\rho_{\rm cyc}-I\) kills
\((A_r)_{\rm ab}\). Multiplication by three is injective on
\(\widehat{\mathbb Z}\), so \(A_r\in\widehat F'\). This is
global; reduction first modulo three would be invalid.

The audited signed calculation gives
\[
 q_3(A_r)=\epsilon_A X^\nu C^{-\nu},\qquad
 T_3=\epsilon_A C^\nu,\qquad \epsilon_A\in\{1,-1\}.
\]
The EXACT E.65.3--4 line is
\(\ell=\mathbf F_3(1,-1)=\ker(C-I)\). Therefore
\[
 T_3|_\ell=\epsilon_A\,{\rm id}_\ell,\qquad
 (-1)^{\epsilon_3(T)}=\epsilon_A.
\]

## 5. Original Gaussian character

E.65 uses
\[
 S_{65}=U_0L_0U_0=
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The outage note uses
\(S_{\rm out}=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)
=S_{65}^{-1}\). These generate the SAME order-four group, and
inversion does not change exponent parity.

E.65.4 defines \(\epsilon_2(S_{65}^j)=j\bmod2\), so
\[
 W^2=(-1)^{\epsilon_2(W)}I.
\]
The exact beta-frame calculation gives
\[
 W_3=q_3(\beta_s)^{-1}X^\nu,\qquad W_3^2=\epsilon_u I.
\]
Consequently \((-1)^{\epsilon_2(W)}=\epsilon_u\).
Both corrected frames are \(I\) modulo four, as required by
the original global-sign normalization.

## 6. Actual CM parity and remaining full-GT criterion

Applying the printed E.65.4 definition yields
\[
 (-1)^{\delta(\Sigma)}=\epsilon_A\epsilon_u.
\]
E.65.5--6 makes \(\Delta\) vanish on Galois. Since the actual
retained \(c\) is Galois and \(\Sigma=\alpha c\),
\[
 \Delta(\alpha)=\delta(\Sigma),\qquad
 (-1)^{\Delta(\alpha)}=\epsilon_A\epsilon_u.
\]
For full-GT \(\alpha\), the new affine pentagon gives
\(dU_{11}=1\). The accepted signed normal form
\(q_3(u)=\epsilon_uY^{-\nu}X^\nu\) has top-left entry
\(\epsilon_u\). Hence \(\epsilon_u=d\bmod3\in\{1,-1\}\), and
\[
 \boxed{\Delta(\alpha)=0\quad\Longleftrightarrow\quad
        \epsilon_A=d\bmod3.}
\]
The right-hand equality remains OPEN. The signed congruence
vanishing of the hexagon determines the epsilon_u factor; it
does not through these identities determine epsilon_A.

## 7. Negative r-conjugator safeguard

The actual negative-alpha conjugator is
\[
 J_r=s\phi A_r=s\,\rho_{\rm cyc}(A_r),
\]
in the non-pure s-coset. The involution gives
\(\alpha(J_r)J_r=1\), NOT \(\alpha(A_r)=A_r^{-1}\).
Substituting the pure frame in that different norm problem could
falsely determine the remaining sign and is not permitted.

## 8. Verdict

PASS on the entire original-source binding and comparison.
Every source in Section 1, including all referee qualifications,
was read completely. No certificate was rerun. The named-character
identification gate is now closed, but the original CM parity
problem remains open.
