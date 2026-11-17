# The intermediate Q map has a real five-point model

This is a post-recovery structural reduction, not a proof that Q embeds. It applies only after deleting moving label 5. It must not be transferred to the full three-moving-point map without checking its additional collision incidences.

## Exact coordinate change

The six retained sphere points before choosing a cap are

\[
0,\;1,\;\zeta,\;\zeta^{-1},\;u\zeta^2,\;u\zeta^3.
\]

Choose the fixed pole 0 as the cap, invert the sphere coordinate, and multiply it by \(r\), with \(r=\zeta\). Put \(s=(u r^2)^{-1}\). The five finite points become, with fixed labels still tracked,

\[
\underbrace{1,r,r^2}_{\text{fixed}},
\qquad\underbrace{s,rs}_{\text{moving}}.
\]

Here the old fixed labels are: label6 at1, label2 at r, label4 at r². The moving labels are: label10 at s, label11 at rs. The old source puncture u=1 has already been filled; its s-value r^-2 is not a collision for r=ζ, since ζ has order five. The five finite remaining collision parameters are exactly

\[
0,\ r^{-1},\ 1,\ r,\ r^2.
\]

They are distinct if \(r\in\mathbb C^*\) is not a root of unity of order one, two or three. In these coordinates the intermediate source map is

\[
\mathbb C\setminus\{0,r^{-1},1,r,r^2\}
\longrightarrow\operatorname{Conf}_5(\mathbb C),
\qquad s\longmapsto(1,r,r^2,s,rs).
\]

Its finite-strand lift has zero pair-linking on every fixed pair. Thus the same central-factor splitting as in B65 identifies its kernel with the corresponding capped sphere kernel. Changing which fixed point is used as the cap changes the concrete lift and marking, not that kernel question.

## An explicit collision-free deformation to r=2

Use

\[
r(t)=(1-t)\zeta+2t,\qquad0\le t\le1.
\]

The real part is at least \(\cos(2\pi/5)=(\sqrt5-1)/4>0.3\). For t<1 its imaginary part is positive, while at t=1 it is2. Hence the segment misses0,1,−1 and both primitive cube roots of unity. Therefore all five collision parameters remain distinct throughout.

The constant source base point \(s_*=1/100\) avoids all these collision parameters. Indeed \(|r(t)|\ge0.3\) and \(|r(t)|\le2\), so the nonzero parameters have moduli at least0.09, whereas \(|s_*|=0.01\). The base configurations \((1,r(t),r(t)^2,s_*,r(t)s_*)\) are also distinct throughout. Isotopy extension for the finite moving set of source punctures, keeping s* fixed, trivializes the source bundle over the interval. The displayed root maps then give a homotopy of based maps, with base points transported along the specified target configuration path.

Consequently their induced fundamental-group homomorphisms are identified by based source and target isomorphisms. These isomorphisms also identify their full profinite completions. The original algebraic base point is connected to s* by a path in its punctured source; that only changes the simultaneous marking by the corresponding standard transport.

Thus the intermediate monodromy image and its kernel question can be studied in the real model

\[
s\longmapsto(1,2,4,s,2s),\qquad
s\in\mathbb C\setminus\{0,\tfrac12,1,2,4\}.
\]

The collision types are: a pair collision at0, a single moving--fixed collision at1/2, two disjoint moving--fixed collisions at1, two at2, and a single collision at4. This gives a short real wiring diagram for the same intermediate map. It does not automatically give a presentation of its image.

## A simpler free-fiber action

In the exact Q-stage action from the recovered certificate, change the rank-four free basis from (C,T,R,S) to (C,T,V,S), where

\[
V=T^{-1}RT,\qquad R=TVT^{-1}.
\]

Direct substitution in the already certified automorphisms gives:

- a fixes T,V and conjugates each of C,S by (TV)^-1;
- f fixes C,V and conjugates each of T,S by ST.

For example, the previous formula \(f(R)=[S,T]R[S,T]^{-1}\), together with \(f(T)=STS^{-1}\), gives \(f(V)=V\) after exact free reduction. This reveals two actual partial-conjugation actions. The e action still mixes C with the complementary generators, so the two partial-conjugation descriptions alone do not prove the full orbit-family independence.

## Limitation of the deformation

The original full six-root family has additional collisions whose equality uses \(\zeta^5=1\). Those collision parameters separate if ζ is replaced by an arbitrary positive real number. The above interval is therefore a legitimate constant-topology deformation of the two-moving intermediate family only. Neither the full theta5 kernel nor the actual residual centralizer is identified with a real-family kernel by this argument.
