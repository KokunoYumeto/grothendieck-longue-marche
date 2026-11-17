# Actual continuous cohomology of the unfilled kernel and its ambient noncollapse

Conversation-level complete proof by DE, independently fully reviewed by CE and root. The finite-factor primary input was freshly read by root from the original-paper reproduction, with publisher metadata separately verified. Historical pre-node and B153 bytes remain unavailable; the full-N application is conditional on its exact factorization. No file, execution, archive, or formal promotion.

## Inputs and conventions

Use the already proved ACTUAL compact unfilled fold kernel U=bar(R) with its continuous pointed-coset presentation on X=Jhat/Shat. Its generators X_x satisfy X_base=1 and delta(X_x)=X_x^(-1). At finite levels X_N=Jhat/(Shat N), let U_N be the free profinite group on X_N minus the base. Then U=lim_N U_N with surjective folds.

Use the continuous nonabelian cocycle convention z delta(z)=1 and equivalence z~k^(-1)z delta(k). Equivalently one may use k z delta(k)^(-1), as k ranges over the group.

PRIMARY INPUT: Herfort, W., & Ribes, L. (1985). Torsion elements and centralizers in free products of profinite groups. Journal fuer die reine und angewandte Mathematik, 358, 155-161. https://doi.org/10.1515/crll.1985.358.155.
Theorem A' says that every finite-order element of a free profinite product of FINITELY MANY factors is conjugate into a factor (take their class of finite groups to be all finite groups). Root reread the full stated theorem and surrounding proof in the primary-paper reproduction at https://www.academia.edu/104225124/Torsion_elements_and_centralizers_in_free_products_of_profinite_groups, web reference turn1161view0, and publisher metadata at https://www.degruyterbrill.com/document/doi/10.1515/crll.1985.358.155/html, reference turn1160view0. No theorem about an unspecified infinite-factor product is assumed.

## 1. Finite levels and unique labels

The group E_N=U_N semidirect C2(tau) is exactly the free profinite product of copies of C2 indexed by X_N. The base generator is tau; the x-generator is t_x=X_x tau. The two inverse presentations follow from X_x=t_x tau and the equivalence of t_x²=1 with tau X_x tau=X_x^(-1).

For any cocycle z in U, z tau is an orientation-odd involution. Its image in E_N is nontrivial. The finite-factor torsion theorem conjugates it into one of the factors, hence to a t_x. The label is unique because the abelianization of E_N is the finite direct product (C2)^(X_N), in which the different t_x have distinct basis images. Folding maps preserve their labels, so the unique labels x_N form a compatible point x in X.

A finite-level conjugator can be chosen even. If w t_x w^(-1) is the prescribed involution and w is odd, replace w by w t_x; this keeps the conjugate and changes orientation. Thus the conjugator belongs to U_N.

## 2. Compactness supplies the actual global conjugator

For the compatible point x, define C_N to be the closed set of u in U such that pr_N(u t_x u^(-1))=pr_N(z tau). It is nonempty: an even finite-level conjugator lifts under the surjection U->U_N. A finer level gives a subset, and any finitely many levels have a common refinement. Compactness yields a member of the intersection of all C_N. The projections separate points, so one ACTUAL u conjugates t_x to z tau.

Different x cannot be U-conjugate, since they have distinct labels at some finite level. Therefore
H^1_cont(C2,bar(R)) = Jhat/Shat
as pointed sets, with x represented by the cocycle X_x and base Shat.

This is also a homeomorphism for the natural compact orbit topology. The cocycle set is closed in U. Its orbit relation is a compact image of U times that set, hence closed; the quotient is Hausdorff. The displayed continuous bijection from compact X to that quotient is a homeomorphism.

The analogous ordinary normal-form argument gives H^1(C2,R)=J/S. Its comparison with the compact result is the natural dense coset embedding. This does NOT identify Rhat with bar(R), whose noninjective comparison was proved separately.

## 3. Exact fixed-lift obstruction in the unfilled double

For g in Jhat,
delta(lambda_1(g))lambda_1(g)^(-1)=X_(g Shat).
A lift u lambda_1(g) is delta-fixed exactly when delta(u)X_(g Shat)=u. Such u exists exactly when the displayed cocycle has base class. The classification therefore says:
g has a delta-fixed lift in the actual unfilled completed double iff g belongs to Shat.
This recovers the original fixed-source restriction without substituting an abstract infinite-index completion.

## 4. Injection into the actual generic kernel

Let q_a be the exact FILLED one-family quotient, Kgen its ordinary kernel, and Ka=bar(Kgen)=ker(qahat). Equality with the completed kernel follows from the full-completion universal property for the quotient Ggen/Kgen. The established generic fixed-subgroup theorem says that the centralizer of tau in the actual generic orbifold completion is Shat times C2(tau). The one-family image of either lambda_i(Jhat) is the same embedded marked section sigmahat(Jhat).

Suppose X_g and X_h become equivalent by k in Ka:
k(X_g tau)k^(-1)=X_h tau.
Since X_g tau=lambda_2(g)tau lambda_2(g)^(-1), the even element
c=lambda_2(h)^(-1)k lambda_2(g)
centralizes tau, hence belongs to Shat. Apply qahat: k disappears, giving sigmahat(h^(-1)g) in sigmahat(Shat). Injectivity of the marked section implies h^(-1)g in Shat. Thus g Shat=h Shat.

Consequently H^1(C2,bar(R))->H^1(C2,Ka) is injective. The same proof applies to every closed delta-stable M with bar(R)<=M<=Ka. This includes bar(N_lambda). Its application to the COMPLETE nodal bar(N) is CONDITIONAL on the exact marked factorization q_a:Ggen->Gamma0->Gamma_a^0, hence N<=Kgen; the historical B139/B159 diagram must be rebound, and inclusion is not inferred from the term 'one-family filling'.

## 5. Actual split closure of P

Let P=q_a^(-1)(sigma(J)). The ordinary marked section gives P=Kgen semidirect lambda(J). The completed lambda embeds because its composite with qahat is the embedded sigmahat. Then
bar(P)=Ka semidirect lambdahat(Jhat)
as ACTUAL closed subgroups. Indeed the compact product is closed and contains P, while both factors belong to bar(P); their intersection is trivial after applying qahat. This proves the split closure without asserting P has its full abstract profinite topology.

The second section lambda_2=delta lambda_1 lies in this same group and also projects to sigmahat. Delta acts trivially on the quotient Jhat because sigmahat(Jhat) is fixed.

## 6. Exact image in the nonabelian cohomology sequence

Every class X_l coming from bar(R) maps to the basepoint of H^1(C2,bar(P)): take p=lambda_2(l)^(-1), so
p^(-1)delta(p)=lambda_2(l)lambda_1(l)^(-1)=X_l.

Conversely let z in Ka be a cocycle trivial in H^1(C2,bar(P)), so z=p^(-1)delta(p). The ACTUAL split closure permits p=lambda_2(l)^(-1) k with l in Jhat, k in Ka. Exact multiplication gives
z=k^(-1)lambda_2(l)lambda_1(l)^(-1)delta(k)
 =k^(-1)X_l delta(k).
Thus its Ka class comes from the class X_l in bar(R).

Combining both directions and injection:
Jhat/Shat = ker[H^1(C2,Ka)->H^1(C2,bar(P))].
Here 'kernel' is the inverse image of the distinguished point of a pointed set, not a group kernel. It is a homeomorphism onto that closed pointed subspace by the same compact/Hausdorff orbit argument.

This classifies precisely these ambient coboundary obstructions, not all of H^1(C2,Ka). It does not settle the remaining filled fixed-source generation or either original main problem.
