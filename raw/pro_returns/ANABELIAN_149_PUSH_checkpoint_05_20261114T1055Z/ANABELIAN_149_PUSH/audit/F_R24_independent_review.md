# Independent review of R24: collar roots and completion

Reviewer: Part F agent. Scope requested by root: local manuscript §§5–6, with the required patching and completion interfaces in §§2–4. The supplied source is `background/literature/padic_section_conjecture_2026.pdf`; its extracted text is `tmp/pdf_text/padic_section_conjecture_2026.txt`.

## Result of this pass

No concrete flaw was found in Lemma5.1, Proposition5.2, or the §6 completion argument. The period-lattice gluing, integral slope, all-sheet requirement, horizontal ramification bound and fixed-copy field embedding were checked independently as described below. This is a review of these precise arguments, not an inference from the plausibility of the advertised section-conjecture conclusion. The overall R24 certification, including all separately cited localization and global descent inputs, remains with root.

## 1. Lemma5.1: the period obstruction is actually removed

Let q:T^an→J^an have free discrete kernel Λ, and pull multiplication by m back along q∘a. On a local lift t of the second projection b, the expression t^m/a takes values in the discrete kernel Λ. Its class in Λ/Λ^m is independent of the lift. This gives clopen subsets indexed by the finite quotient Λ/Λ^m.

On one subset choose a representative λ. The discrepancy (t^m/a)/λ is an m-th power of a period, so a locally constant correction changes t to a lift with t^m=λa. On overlaps two corrected lifts differ by ρ∈Λ with ρ^m=1. Freeness of Λ forces ρ=1, so the corrected lifts glue globally on that subset. Applying a character and dividing by a chosen m-th root of χ(λ) gives the desired m-th root of χ(a). Different subsets are disjoint, so there is no further compatibility condition.

This verifies the stronger assertion required later: the root exists on the entire pullback B, including every connected component. It does not merely produce one lifted sheet. Nothing in this argument requires m to be prime to the residue characteristic. The division morphism of the algebraic abelian variety is étale in characteristic zero even when p divides m.

## 2. The auxiliary curve and its skeleton

For y^ell=T(T−1)/(T−alpha), the four branch orders are 1,−1,1,−1, so the curve is connected of genus ell−1. In the blowup chart TU=alpha the Kummer expression is (T−1)/(1−U), a unit reducing to−1 at the node. After splitting its ell roots in the constant field, normalization has ell separate unramified node charts. The outer and inner component covers each have precisely two branch points and are rational. Thus the stable dual graph really is two rational vertices with ell parallel edges, each with the original thickness v(alpha). A thickness greater than one is compatible with a semistable curve model; regularity of the total space is not claimed or needed.

The inverse image of the open annulus |alpha|<|T|<1 is exactly ell copies of that annulus: both units 1−T and 1−alpha/T admit ell-th roots there because ell is a residue-field unit. This checks the all-sheet statement directly, independently of counting nodes. The branch above T=0 is rational over the original field, so the algebraic Abel–Jacobi map can indeed be chosen over that field.

I tested whether choosing a connected component of Z×_{J,[m]}J over k could leave a nongeometric connectedness problem. It does not affect the stated argument. Every geometric component is still finite étale of positive degree over the geometrically connected Z, hence surjective. The roots already exist on the full pullback and restrict to every such component. The later normalized connected pullbacks over kbar retain them.

## 3. The slope is one, without an extra period-matrix factor

The possible error here would have been identifying a character lattice with a dual lattice, thereby obtaining a rational slope or a multiple of ell. I reopened the cited Baker–Rabinoff primary source, arXiv:1308.3864v1, especially §4.5.2, §5.2, Proposition6.1 and Corollary6.6. Its conventions identify the character lattice with H1 of the skeleton, and its tropical Abel–Jacobi map uses integration with the edge-length pairing. The same source §4.1 explicitly supplies the topological covering and local analytic isomorphism needed in Lemma5.1.

For the cycle c_j=e_j−e_j′, the coefficient on the oriented edge e_j is exactly1. Evaluation of a lifted tropical Abel–Jacobi path against c_j therefore changes by the traversed edge length. Since that length coordinate is v(T), the derivative of v(χ_j∘b_ij) is1. Changing the lift adds a constant period and does not change the derivative. There is no inverse Gram matrix in this character evaluation.

The open Berkovich annulus retracts to its interval and is locally path connected. The topological lift to the torus is therefore available; local analytic inverses of q make it analytic. The fact that the annulus has nontrivial étale covers does not contradict its topological simple connectedness, and the proof does not confuse these two notions.

## 4. The quantitative trimming estimate suffices for p-power roots

Write the slope-one unit as cT(1+h), with h having no constant Laurent term. The unique dominant coefficient remains the degree-one coefficient on the entire annulus. For positive n, dominance at radii approaching the outer endpoint gives |h_n|≤1; at the inner endpoint it gives |h_{−n}|≤|alpha|^n. Thus at s=v(T),

    |h| ≤ p^{−min(s,a−s)}.

On the middle collar D<s<a−D this is strictly less than p^(−D), and on every closed subannulus it has a uniform strict margin. With D>v_p(m)+1/(p−1), the logarithm satisfies v(log(1+h))≥v(h), and v(m^(−1)log(1+h))>1/(p−1). Consequently the exponential converges locally uniformly and supplies a genuine analytic m-th root of1+h. The endpoint estimates do not require analytic continuation to either endpoint.

Division by this root and an m-th root of c converts the Lemma5.1 root of the character into a root of T on every inverse-image sheet. This was checked for arbitrary m, including p-powers and p=2.

## 5. Horizontal ramification remains bounded by ell

The ramification here is at closed points over kbar, with residue characteristic zero. A completed local extension is kbar((t^(1/e))); all roots of unity already lie in the residue field. Thus taking composita or Galois closures of extensions with e dividing ell cannot introduce an ell-squared index: all local factors remain in the same cyclic extension kbar((t^(1/ell))). Under a local pullback t=s^r a(s), the normalized index is e/gcd(e,r), and an upper étale cover contributes index1.

Accordingly every normalized pullback W_b in §6, their common compositum W, and the upper étale cover V all have the required horizontal indices. This does not impose a prime-to-p bound on vertical reduction ramification, and the argument never needs such a bound. The potentially large degree of the Jacobian multiplication cover is harmless: its map to Z is étale.

## 6. Patching is on the whole exterior and evaluates at the specified H-point

In Proposition3.2, the full inverse collar root splits every local factor Z^e−t into distinct linear factors. Although p may divide e, a nonzero constant zeta−zeta′ is still invertible in Omega, so the factors are comaximal as analytic functions. Their norms also place their roots inside the local disk charts from Lemma3.1. This gives an actual trivialization of the entire degree-d cover on the overlap. The finite open cover has disjoint branch-disk pieces, so the gluing needs no missing triple-overlap compatibility. The result is a finite étale algebra on a proper analytic curve and algebraizes by the cited GAGA input.

After proper base-extension invariance descends V_Omega→W_Omega, the composite V→X has field inside L_ell and hence H. An embedding kbar(V)→H, together with the fixed Omega→H, gives an H-valued point of V_Omega over exactly the original H-valued point of X_Omega. Its analytic image lies over xi in the exterior. Evaluating the exterior analytic map therefore gives an H-valued point of C_Omega. The support of its image on C is generic because its projection to X_kbar is the fixed generic point and C→X_kbar is finite. This is a field embedding kbar(C)→H over the specified K0, not an abstract unvalued embedding chosen independently of the completion.

This also handles the case where xi is an Omega-rational point whose projection to X_kbar is generic. The argument retains the entire H-valued point, so it does not incorrectly replace it by its underlying Berkovich point.

Finally, if F/K0 is normal and the embedding lands in H⊂E, every image of an element of F is a root in E of a polynomial already split in the chosen F. There are no new roots of that split polynomial in E. Hence the image is contained in the chosen F, and equality follows from the degree. The final containment F⊂H therefore concerns the specified copy. Taking the union over finite normal extensions is valid.

## 7. Additional interface check

I read the supplied RNS primary excerpt at Proposition2.4(iv), printed p.50, and the introduction's TheoremA scope. It does give a stable model mapping to an arbitrary compactified model after a finite extension, under the RNS hypothesis; the all-prime application to the proper genus≥2 source fits. The subsequent irrational-level compactness argument in Lemma4.3 only requires a model morphism, not a finite model morphism. Source vertices and smooth disk tubes have rational coordinate valuations, so the selected irrational level lies entirely in node tubes; compactness then supplies a whole collar. This interface also survived the check.

The direct web reader opened Baker–Rabinoff v1 and the exact passages above. Direct reads of the ABBR v3 and BPR v1 arXiv PDF URLs failed in this agent's tool call; I did not count those failed calls as independent primary reads. Root had already read their exact statements. I checked the supplied manuscript's use of them, while the independent primary confirmation in this pass is the Jacobian uniformization/comparison and the local RNS excerpt. No general p-adic section-conjecture theorem was imported as an input.
