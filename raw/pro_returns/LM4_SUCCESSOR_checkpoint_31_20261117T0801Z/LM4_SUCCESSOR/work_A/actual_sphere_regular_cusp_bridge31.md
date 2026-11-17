# The same marked negative cusp gives the original regular frame

Cycle31 research. This is a direct continuation of
`actual_sphere_cabling_correction31.md`. It changes neither that proof
nor any frozen formal source. The original full-GT hypothesis is retained
for the actual four-strand embedding.

## 1. Keep the literal original rank-two copy

Use the free factor \(\widehat F(A,S)\le\widehat N\) from the cabling
proof. For this section only write
\[
 \alpha_*=\gamma|_{\widehat F(A,S)},\quad
 \varphi=\varphi_\alpha(A,S),\quad u=u_\alpha(A,S).
\]
Thus
\[
 \alpha_*(A)=A^{-1},\quad
 \alpha_*(S)=\varphi^{-1}S^{-1}\varphi,\quad
 \alpha_*(u)=\varphi^{-1}u.
\]
This is the original canonical system under \(x\mapsto A,y\mapsto S\).
Let \(\iota_*\) swap \(A,S\), put
\[
 v_*=\operatorname{Inn}(u^{-1})\iota_*,
 \qquad \tau_*=\alpha_*v_*,
 \qquad L=SA,\qquad z_*=(AS)^{-1}.
\]
All these actual automorphisms and their commuting-involution
identities are the original A85/A86 data transported through the
literal free-factor isomorphism.

The preceding proof supplies the unique transporter \(t\in\widehat
F(A,S)\) with
\[
 \alpha_*(L)=t^{-1}L^{-1}t,\qquad
 t_{\rm ab}=-A,
\]
normalized to have zero \(L\)-coordinate in the basis \((L,A)\).
The four-strand correction was exactly \(h_0=t p\), with
\(p=\varphi_\alpha(bc,f)\in(\widehat N)'\).
The letters \(t,h_0\) in this paragraph are the negative-cusp
transporters; they are not the regular-frame scalar of A86.

## 2. A full regular transporter for the same positive boundary

Directly from the displayed definitions,
\[
 \tau_*(A)=u^{-1}S^{-1}u,\qquad
 v_*(L)=u^{-1}A L A^{-1}u.
\]
Apply \(\alpha_*\) to the second equality, retaining the order of every
factor. It gives
\[
 \tau_*(L)
 =u^{-1}\varphi A^{-1}t^{-1}L^{-1}tA\varphi^{-1}u
 =k^{-1}L^{-1}k,
 \qquad
                         k=tA\varphi^{-1}u.             \tag{1}
\]
Because \(t_{\rm ab}=-A\) and \(\varphi,u\) are commutator words, \(k\)
has zero abelianization. This is an exact full-word formula, not only
a homology comparison.

Let \(h_{\rm reg}\) be A86's unique element of the closed commutator
subgroup with
\[
             \tau_*(z_*)=h_{\rm reg}^{-1}z_*^{-1}h_{\rm reg}.
\]
The basepoint identity is \(L=A^{-1}z_*^{-1}A\). Applying \(\tau_*\)
shows that \(A^{-1}h_{\rm reg}\tau_*(A)\) is a transporter for \(L\);
its abelianization is \(-L\). Multiplying it on the left by \(L\)
preserves the transport equation and makes its abelianization zero.
The primitive centralizer of \(L\) implies uniqueness of the
zero-abelianization transporter. Comparing with (1) therefore proves
\[
 k=S h_{\rm reg}\tau_*(A)
   =S h_{\rm reg}u^{-1}S^{-1}u.
\]
Solving this exact equality gives the desired original-marking bridge:
\[
             \boxed{h_{\rm reg}=S^{-1}tA\varphi^{-1}S u.} \tag{2}
\]

For example the standard reflection has \(\varphi=u=1,t=A^{-1}\),
and (2) gives \(h_{\rm reg}=1\), in agreement with its literal
negative-swap regular involution. This is a check of the order and
normalization, not a finite-target argument.

## 3. Put the actual regular norm back into the four-strand correction

A86 gives the unique actual full \(q_*\in\widehat F(A,S)\) with
\[
 h_{\rm reg}=q_*\tau_*(q_*)^{-1},\qquad
 (q_*)_{\rm ab}=(\xi,-\xi)
\]
in the \((A,S)\)-basis. The scalar \(\xi\) is precisely A86's regular
frame scalar transported by the indicated isomorphism.
Equation (2) and \(h_0=t p\) give, in the original sphere kernel,
\[
 h_0=
 S\,q_*\tau_*(q_*)^{-1}\,
 u^{-1}S^{-1}\varphi A^{-1}\,p.                         \tag{3}
\]
Thus the regular frame is now tied to the same full correction as the
actual four-strand action. No conjugator or based cabling factor has
been removed.

In the free basis \((L,A,C)\) of the kernel, the same element has
\[
                   (q_*)_{\rm ab}=(-\xi,2\xi,0).        \tag{4}
\]
Indeed \(S=LA^{-1}\). This keeps the distinction between the two
coordinate systems explicit.

## 4. What this does and does not force

The odd \(A\)-coordinate of the negative correction \(h_0\) does not
obstruct the regular frame: it is cancelled in (1), and (2) is an
actual zero-abelianization regular transporter. In (3) the entire
regular norm is a commutator word, so abelianizing that identity
recovers \((h_0)_{\rm ab}=-A\) independently of \(\xi\). It cannot
by itself identify \(\xi\) with the canonical dihedral exponent.

The existing actual unit comparison is still
\[
 a_{\rm reg}=1-4\xi,\qquad d_\alpha=2k_\alpha+1,
\]
where \(u_\alpha\) has dihedral image \(T^{k_\alpha}\).
The required equality is still \(\xi=-k_\alpha/2\), followed by the
full nonlinear \(\Omega_\alpha=1\) condition. These symbols refer to
the original canonical data, not to a freely chosen solution.

The relative pro-two sphere quotients from the preceding notes retain
only the dyadic image of (4). Their full retained \(P\) and the actual
same correction remain essential, but their kernel action factors
through the pro-two base as already proved. Equations (2)--(3) supply
the previously missing based comparison; they do not create an odd
coefficient consequence from that factorization. Any further argument
must use additional actual marked data, not simply identify the
negative and regular reflections or their section classes.

No producer, finite-head census, new external theorem, or private
render was used.
