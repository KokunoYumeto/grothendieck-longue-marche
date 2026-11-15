# Operational comparison of the A–D letters

**The strongest verified comparison is draft C with printed B in Kleiman's 1968 paper, through the actual inverse Lefschetz maps.** Draft A has an operational match with the algebraic-class clause of printed A; a full four-letter permutation has not been verified because standalone definitions of the draft's B and D remain unlocated in the searched witnesses.

Here CT means the supplied MPL_16+47+54+44_transcription.tex; CT16/048 means cote 16, scan 048. Its first-pass readings and the doubts recorded in MPL_16+47+54+44_doubts.md remain evidence with that status, including the uncertain ℓ/χ subscript and the overwritten Cayley–Hamilton display. K68's §2 works with a fixed Weil cohomology and varieties satisfying its strong Lefschetz condition; the comparisons below retain that printed setting and the manuscript's indicated polarizations.

## Statement-to-statement table

| Draft letter and witness | Printed statement reached by the comparison | Extent verified |
|---|---|---|
| **A:** CT16/044 discusses the dimensions of algebraic-class spaces \(C^i\) and \(C^{n-i}\); CT16/045 uses the critical maps on \(X\times X\) and \(X\times Y\). | G69, p. 196, A(b) requires \(L^{n-2p}:C_\ell^p(X)\to C_\ell^{n-p}(X)\), \(2p\le n\), to be isomorphisms; A(a) also states the full cohomological Lefschetz isomorphisms. | The algebraic-class operation is identified; the full printed A(a)+(b) must remain explicit. |
| **B:** CT16/044 writes “\(A+\mathrm{index}\) implies \(B\)”; CT16/045 attaches the index qualification to its A/B comparison, with a local A/Q reading doubt. | K68, Corollary 3.9, connects printed A and D under the stated strong Lefschetz and index conditions; printed D concerns equality of homological and numerical equivalence. | These are parallel source relations. The draft B definition needed for an isolated B↔D entry has not been located. |
| **C:** CT16/048–049 constructs \((L_X^{n-i})^{-1}\) from an algebraic opposite-direction isomorphism and rational characteristic-polynomial coefficients, for every \(i<n\). | K68, Proposition 2.3, characterizes printed B by algebraicity of the inverse maps, for every \(i\le n\). | The exact map comparison is verified below; \(i=n\) contributes the identity. |
| **D:** CT16/048 places D in a conjunction with algebraic isomorphisms \(H^{2n-i}(X)\to H^i(X)\) for every \(i<n\), and compares this with rationality for every algebraic endomorphism together with those isomorphisms. | K68, Theorem 2.9, has the corresponding conjunction with printed C, whose content is algebraicity of the Künneth projectors. | The bundled criteria have been located and compared. CT16/040's use of D(Y) with primitive-projector notation remains relevant; a standalone draft D↔printed C definition is unverified. |

Sources: [G69, pp. 195–196](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf); [K68, §§2.3, 2.9, 3.6, 3.9](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf). G69's C also specifies representatives independent of ℓ; that clause remains part of that printed statement.

## Exact inverse-map calculation for draft C and printed B

CT16/048 names

\[
u:H^{2n-i}(X)\longrightarrow H^i(X),\qquad
v=L_X^{n-i}:H^i(X)\longrightarrow H^{2n-i}(X),\qquad
w=uv.
\]

The source describes \(u\) and \(v\) as algebraic isomorphisms and invokes rational characteristic-polynomial coefficients to obtain algebraic \(w^{-1}\); CT16/049 then gives the literal identity “\(w^{-1}u=v^{-1}\).” Its map-level verification is

\[
(w^{-1}u)v=w^{-1}(uv)=1,\qquad
w^{-1}u=(w^{-1}u)(vv^{-1})=((w^{-1}u)v)v^{-1}=v^{-1}.
\]

Thus the map constructed there is exactly the inverse appearing in K68, Proposition 2.3, with the same source, target and polarization. At the additional printed index \(i=n\), \(L^0=1\), and its inverse is represented by the diagonal: \(p_{2*}([\Delta_X]\cdot p_1^*a)=a\). This comparison reports the source's criterion and verifies its displayed maps; it does not supply missing definitions for B or D.

## Exact rescaling of the lowering operator

K68, p. 367, equations 1.4.2.1–1.4.2.2, were checked visually. For \(a\in P^i(X)\), \(0\le i\le n\), set \(m=n-i\); both operators kill \(a\), and on the same primitive string,

\[
\Lambda(L^ja)=L^{j-1}a,\qquad
{}^c\Lambda(L^ja)=j(m-j+1)L^{j-1}a
\quad(1\le j\le m).
\]

Define the degree-zero rescaling map \(D\) by

\[
D|_{P^i}=1,\qquad
D|_{L^jP^i}=j(m-j+1)\,1\quad(1\le j\le m).
\]

Its nonzero rational factors make \(D\) invertible, and evaluation on each summand proves

\[
{}^c\Lambda=\Lambda D,\qquad
\Lambda={}^c\Lambda D^{-1},\qquad
\Lambda^mL^ma=a,\qquad
({}^c\Lambda)^mL^ma=(m!)^2a.
\]

**Editorial calculation; confidence high:** direct evaluation on every displayed primitive-string summand proves the four identities, including the order of composition with D. This is the explicit coefficient conversion underlying K68's introductory scalar-modification remark. CT16/013, (6.14), records \((\Lambda^{n-i}L^{n-i}-1)\pi_i=0\); CT16/010's dotted definition (6.5) remains unfilled. The table consequently uses K68's inverse-map criterion; its Proposition 2.3 also records both lowering operators' algebraicity. [K68, pp. 367–370](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf).

## Quantifiers and the contribution of cote 11

CT16/046 expressly says that the polarizations on products and hyperplane sections come from \(X\), and writes “\(A(k)=C(k)\)” in terms of critical-degree A for “every T.” G69, p. 196, separately records \(B(X)\Rightarrow A(X)\) and \(A(X\times X)\Rightarrow B(X)\); the self-product and universal quantifiers remain in the comparison.

The frozen cote 11 text adds the correspondence construction \( \operatorname{Hom}_{V^A}(X,Y)=A(X\times Y)\) on scan 003 and the Poincaré/bivariant formalism on scans 027 and 034. Its searched text contains no labeled standard-conjecture list: the sole search match for “conject” concerns Tits on scan 016, while the underlined A on 027 introduces the Poincaré-algebra category. Thus the present packet contributes the formalism used in the comparison; the letter evidence comes from the cited cote 16 witnesses.

The related ledger entries **WG2 §2.4 #3**, **WG2 §2.3 #2**, and **WG2 §2.2 #4** each retain the exact status **question or plan item of the war game (round 2; unchecked)**. The earlier notes' S1 supplies a first-pass lead, and the present map calculations do not promote its unresolved B/D dictionary entries.
