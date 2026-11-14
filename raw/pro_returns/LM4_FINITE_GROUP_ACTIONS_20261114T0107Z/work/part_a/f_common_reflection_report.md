# F.12: actual common-reflection equalizer

## Main proved result

The new fragment is f_common_reflection.tex, with metadata in f_common_reflection_results.json. It retains the full residual centralizer question as Open but gives an exact smaller fixed-intersection problem with all maps based and explicit.

The F.11 map has six normalized difference characters whose pullbacks are nonzero constant multiples of \(t,t-1,\ldots,t-\zeta^4\). Hence the induced map on the full abelianizations is split injective. Every element of its kernel lies in the closed commutator subgroup of the specified \(\widehat F_6\).

The residual A5 centralizer consequently lies in the index-two source \(Y\to X_5\), \(s\mapsto s^2\). The source is \(Y=\mathbf P^1-\{0,\infty,\pm\mu_5\}\), of rank eleven.

The common involution is \(\tau=(15)(34)\), acting on the original family by \(z\mapsto s^2/z\). Its quotient is the exact map

\[
Q_s(z)=\left(\frac{z-s}{z+s}\right)^2.
\]

It labels the two branch points by0 and infinity and the original pole-pair by1. The other five coordinates are

\[
v_{j+1}(s)=\left(\frac{\zeta^j-s}{\zeta^j+s}\right)^2.
\]

This map of full profinite fundamental groups is injective. It is the composite of the source inclusion from F.11 and the actual completed normalizer quotient from F.7.4–5. The only quotient kernel is the named deck involution, which has nontrivial permutation on the original punctures and is therefore absent from the pure subgroup.

## Exact second action and both directions of the reduction

Take \(\beta=(13)(45)\). It commutes with \(\tau\), and the chosen D10 and beta generate A5. On the six tau-orbits its permutation is \((0\,2)(1\,3)(4\,5)\), while it exchanges the two branch points. The actual Möbius matrix is checked over the same quartic field as F.11. In the branch coordinate it is \(V\mapsto v_2(s_0)/V\).

Thus its based action on normalized moduli is

\[
R(v_1,\ldots,v_5)=(v_2/v_3,v_2,v_2/v_1,v_2/v_5,v_2/v_4).
\]

The residual A5 centralizer is exactly the equalizer of the completed source map and its composition with R. One direction uses the actual forgetting constraints to enter the double-cover source. The other direction uses injective descent in the common tau-centralizer: equality downstairs proves actual beta commutation upstairs, and D10 together with beta is A5. No equality of unrelated closures or unspecified basepoint conjugation is used.

## Integral consequences and the explicit old word

Vanishing of the source abelianization downstairs leaves anti-invariant classes

\[
\sum_{j=0}^4 a_j(e_j^+-e_j^-).
\]

The twenty ordinary target winding characters restrict to

\[
L_{j+1}=4a_j,\qquad M_{j+1}=2a_j,\qquad
N_{i+1,j+1}=2(a_i+a_j).
\]

Their complete fixed-value system is exactly

\[
a_0-a_1+a_2=0,\qquad -a_1+a_3+a_4=0.
\]

The three integral kernel vectors are \((-1,0,1,0,0)\), \((1,1,0,1,0)\), and \((1,1,0,0,1)\). They also form a basis over the full profinite integers. This is the kernel of these winding equations; the actual residual group's image is only proved to be contained in it.

The exact F.11 kernel word lifts to \(e_1^- -e_1^+\). Its winding defect for \(L_1-R^*L_1\) is4. The full power \(w^u\) has defect \(4u\) in the full \(\widehat{\mathbb Z}\), proving that no nonzero power is in the residual equalizer. This supplies a specific low-dimensional detector in place of the general Magnus construction for this word.

## Executed certificate and remaining implication

code/c5_common_reflection_f12.py was executed successfully. The complete output records the actual beta matrix and branch action, all six character pullback roots, the twenty-by-twelve divisor matrix, the integral involution matrix, the exact two-row restriction, its three kernel vectors, and the defect4.

The unreduced source-cohomology map has rank10; its beta-difference has rank6, with nonzero Smith diagonal \(1,1,1,1,2,10\). These exploratory rank data are retained but are not used to infer the full fixed intersection.

The precise unproved implication is now whether the two specified injected maps from \(\widehat{\pi_1(Y)}\) to \(\widehat{P\Gamma}_{0,8}\) have trivial equalizer. The homology constraints do not settle it. The staged proof makes no pro-p replacement and constructs no nontrivial residual centralizer element.

No new bibliography key is required. The full topology and quotient maps are the independently audited inputs of F.7, while the explicit coordinates and the integer calculation are proved in this fragment.
