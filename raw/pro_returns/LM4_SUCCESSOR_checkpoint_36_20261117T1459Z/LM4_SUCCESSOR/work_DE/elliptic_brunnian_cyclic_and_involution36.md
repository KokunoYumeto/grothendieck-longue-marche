# The entire elliptic joint-kernel cyclic obstruction and its actual involution action

Checkpoint36 research, separate from the frozen formal cutoff A120–A125. All completions and closed subgroups below are the actual ones. This note does not identify a completion of an abstract infinite-index subgroup. It uses the complete A121, A122, A124 and A125 proofs and the exact based deletion table in `work_A/actual_elliptic_based_forgetting36.md`. No extracted primary forgetting table is imported.

## 1. Actual groups, conventions and the joint quotient

Let G be the full completion of the actual reduced three-strand elliptic braid group, and P its pure subgroup. Write P′ for its closed derived subgroup. In the retained marking put

\[
 K=[Y,X]=\sigma\tau^2\sigma,\quad C=\sigma\tau,\quad
 L=C^{-1},\quad\Pi_0=LY,\quad
 \rho=\operatorname{Ad}(C),\quad \rho_0=\operatorname{Ad}(\Pi_0).
\]

The base cubic has exact order three. Let E be the full free profinite group on X,Y and E′ its closed derived subgroup. The actual two-strand half-twist induces

\[
 j(X)=X^{-1}K^{-1}=YX^{-1}Y^{-1},\quad j(Y)=KY^{-1},\quad
 j(K)=K,\quad j^2=\operatorname{Ad}(K).
\]

Define the involution

\[
 \theta=\operatorname{Ad}(Y^{-1})j.
\]

Thus theta sends X to X inverse and Y to X Y inverse X inverse. In the actual free basis (X,YX inverse), it inverts both generators. The literal identities are

\[
 \theta^2=1,\qquad j\theta=\operatorname{Ad}(Y),\qquad
 j^{-1}\operatorname{Ad}(Y)=\theta.
\tag{1}
\]

The three based deletion maps are the exact maps pi3, pi1=pi3 rho inverse and pi2=j inverse pi3 rho. The previous whole-generator proof gives

\[
 \pi_1\rho=\pi_3,\qquad \pi_2\rho=j\pi_1,\qquad
 \pi_3\rho=j\pi_2.
\tag{2}
\]

It also proves the **entire** continuous surjection

\[
 q=(\pi_1,\pi_2,\pi_3):P'\longrightarrow Q=(E')^3.
\tag{3}
\]

For clarity, its surjectivity uses the three actual pair meridians: their images are (K,1,1), (1,K,1), and (1,1,K). Each meridian lies in P′; conjugation by the whole pure group gives the full closed normal closure of K in its indicated E coordinate. That closure is E′. Compactness makes these images closed, so all three independent coordinates occur.

Define the actual closed joint kernel

\[
 \mathcal B=\ker(q:P'\to Q).
\tag{4}
\]

This is the full kernel retained in the argument; it is not replaced by selected meridian relators or a finite family of words.

## 2. Exact cyclic action and the complete cohomology space

Because rho0=rho inverse followed by Ad(Y), equations (1)–(2) give the action induced on Q:

\[
 R(t_1,t_2,t_3)=(\theta(t_2),\theta(t_3),t_1).
\tag{5}
\]

Indeed pi1(Y)=1 and pi2(Y)=pi3(Y)=Y. The first two coordinates of rho inverse Ad(Y) are therefore j inverse Ad(Y), and the third is the first coordinate unchanged. In particular R cubed is the identity, and B is rho0-stable. Its fixed subgroup is exactly

\[
 Q^R=\{\iota(t)=(t,\theta(t),t):t\in E'\}\cong E'.
\tag{6}
\]

A125 proves at this actual scope

\[
 (P')^{\rho_0}=1,\qquad H^1(C_3,P';\rho_0)=\{*\}.
\tag{7}
\]

Here a C3 cocycle is an element z with z rho0(z) rho0 squared(z)=1; equivalent cocycles differ by z becoming n inverse z rho0(n). For t in E′, choose any g in P′ with q(g)=iota(t). Then g inverse rho0(g) lies in B. Define

\[
 \partial(t)=[g^{-1}\rho_0(g)]\in H^1(C_3,\mathcal B;\rho_0).
\tag{8}
\]

The map is independent of the lift. Replacing g by gn, n in B, changes the cocycle by n inverse z rho0(n).

It is onto: a B-valued cocycle is a P′-coboundary by (7), say g inverse rho0(g); its quotient image forces q(g) to be R-fixed and hence of the form (6). It is one-to-one: if the two cocycles are B-equivalent, one may replace the first lift by its product with an element of B so that the cocycles become equal. Equality of g1 inverse rho0(g1) and g2 inverse rho0(g2) makes g2 g1 inverse rho0-fixed. By (7), g1=g2 and their quotient parameters agree.

The topology does not require a continuous choice of g. The compact space

\[
 \{(t,g)\in E'\times P':q(g)=\iota(t)\}
\]

maps continuously onto E′ and to the cocycle-orbit space. The latter map is constant on the fibers of the former, so it descends continuously. Continuous cocycles form a closed compact set, and their orbit equivalence relation under the compact coefficient group is closed. Thus their orbit space is compact Hausdorff. The continuous bijection (8) is consequently a homeomorphism:

\[
 \boxed{H^1(C_3,\mathcal B;\rho_0)\cong E'}
\tag{9}
\]

as pointed compact spaces, with t=1 corresponding to the neutral class. This is not a claim that the pointed cohomology set has its usual group structure; the parameterization transports one if desired, but no such operation is used.

## 3. Based half-braid actions and the actual involution

Now fix the original negative full-GT involution, its original parameter phi and its canonical norm word u. Let Theta be its actual elliptic involution on G, and T its actual restriction to the two-strand pure group E. Put

\[
 \Phi=\phi(X,K),\quad F_b=\phi(\sigma^2,\tau^2).
\]

The complete actual section formulas are

\[
 \begin{aligned}
 T(X)&=\Phi X^{-1}\Phi^{-1},&
 T(Y)&=K^{-1}j(\Phi)Y\Phi^{-1},& T(K)&=K^{-1},\\
 \Theta(\sigma)&=F_b\sigma^{-1}F_b^{-1},&
 \Theta(\tau)&=\tau^{-1}.&&
 \end{aligned}
\tag{10}
\]

The two-strand formulas themselves imply, by substitution on X,Y,

\[
 Tj=j^{-1}T.
\tag{11}
\]

For example, Tj(X) and j inverse T(X) both equal
K inverse j(Phi) (YX Y inverse) j(Phi) inverse K. For Y both equal
K inverse Phi Y inverse j(Phi) inverse K. Thus no unbased naturality or extracted forgetting table is needed for (11).

Here is a complete convenient verification that all three based deletions commute with Theta. On joint tuples the two actual half-braid conjugations act as

\[
 \operatorname{Ad}(\sigma):(t_1,t_2,t_3)\mapsto(t_2,t_1,j(t_3)),
\qquad
 \operatorname{Ad}(\tau):(t_1,t_2,t_3)\mapsto(j(t_1),t_3,t_2).
\tag{12}
\]

For the first formula use the generating set X,Y,X2,Y2,a= sigma squared,b= tau squared. Its first four conjugates are respectively X2 a inverse, a Y2, a X, Y a inverse; a is fixed and b maps to A13. The whole deletion table proves every coordinate. The second formula follows by composing the inverse first action with (2). In particular the full joint kernel of the pure group is stable under both half-braids; its intersection B with P′ is normal in G.

The word Fb has all three deletion images one. Its conjugates therefore do also. For Theta(X2), use Theta(X2)=Ad(Theta sigma)(Theta X) times Theta(a). Formula (12) makes its tuple

\[
 (T(X),1,j^{-1}(T(X))K^{-1})=(T(X),1,T(X)^{-1}),
\]

where the equality follows from (11) applied to j(X)=X inverse K inverse. Similarly Theta(Y2) has tuple

\[
 (T(Y),1,j(T(Y))K)=(T(Y),1,T(Y)^{-1}),
\]

using j inverse(Y)=Y inverse K and (11). The X,Y rows follow directly from (10), and a,b have the three original images with each K replaced by K inverse. These six checks prove on the entire group

\[
 \pi_i\Theta=T\pi_i\quad(i=1,2,3).
\tag{13}
\]

Consequently B is Theta-stable as well. In this proof one may first use the full joint kernel on P to justify discarding the half-braid conjugates of Fb, and then restrict to its intersection B with P′; no circular stability assumption is made.

## 4. The corrected involution on the entire cyclic cohomology space

Let h1 be the uniquely normalized actual derived transporter

\[
 \Theta(\Pi_0)=h_1\Pi_0h_1^{-1},\qquad
 h_1\in P',\qquad\Theta(h_1)h_1=1.
\tag{14}
\]

Its existence, uniqueness, derived membership and norm are A124–A125. Define

\[
 \Theta_0=\operatorname{Ad}(h_1^{-1})\Theta.
\tag{15}
\]

This is an involution, it preserves B, and it commutes with rho0. Indeed it fixes Pi0, and its square is the inner action of h1 inverse Theta(h1 inverse)=1. It therefore acts on both sides of (9).

Write e=pi1(h1). Below we verify pi3(h1)=e. Equivariance of the boundary map follows from applying Theta0 to an arbitrary lift in (8). Its action on the parameter t is exactly

\[
 t\longmapsto e^{-1}T(t)e.
\tag{16}
\]

This is an actual corrected reflection, not the simultaneous inversion theta. In particular T has abelianization diag(-1,1), whereas theta has abelianization minus the identity. They cannot be interchanged in a cohomology calculation.

## 5. Base parameter and the original canonical common word

Set beta2=Ad(Phi inverse)T. The original canonical norm gives

\[
 U=u(X,K),\qquad T(U)=U\Phi^{-1}.
\tag{17}
\]

Applying T again gives T(Phi)=Phi inverse. Thus beta2 is an involution. The exact identity

\[
 \Phi^{-1}T(Y^{-1})K^{-1}=Y^{-1}j(\Phi^{-1})
\]

and (11) show that

\[
 \beta_2\theta=\theta\beta_2.
\tag{18}
\]

To determine the three images of h1, left-multiply (14) by C. Modulo the full joint kernel, C Theta(L) equals K: this follows at once from (10), since every image of Fb is one and C tau sigma= sigma tau squared sigma=K. Consequently the three images of C Theta(Pi0) are

\[
 (1,K T(Y),K T(Y))=(1,j(\Phi)Y\Phi^{-1},j(\Phi)Y\Phi^{-1}).
\]

Apply the same two based equations that gave the common-word description of p_w in the earlier note. There is a unique b0 in E′ such that

\[
 q(h_1)=(\Phi b_0,\Phi\theta(b_0),\Phi b_0).
\tag{19}
\]

The parameter is derived because h1 is derived and Phi is a commutator-word evaluation. Equation (13) and the actual norm in (14) give

\[
 \beta_2(b_0)b_0=1.
\tag{20}
\]

The norm in the second coordinate follows from the same equation by (18). Formula (16) can therefore also be written as Ad(b0 inverse) beta2. It is an involution because of (20).

For the actual canonical w=u, let p_u be the unique derived cubic transporter. The completely proved based-forgetting result is

\[
 q(p_u)=(U a_u,U\theta(a_u),U a_u),\qquad a_u\in E'.
\tag{21}
\]

The actual transporter of Theta(Pi_u) from Pi_u is

\[
 h_u=\Theta(p_u)h_1p_u^{-1}.
\tag{22}
\]

Substituting (17)–(21), in their displayed order, gives

\[
 \begin{aligned}
 t_u&=\beta_2(a_u)b_0a_u^{-1},\\
 q(h_u)&=(U t_u U^{-1},U\theta(t_u)U^{-1},U t_u U^{-1}).
 \end{aligned}
\tag{23}
\]

The middle coordinate uses precisely (18). The norm beta2(tu)tu=1 is automatic from (20), for **every** possible a_u in E′. Explicitly,

\[
 \beta_2(t_u)t_u
 =a_u b_0^{-1}\beta_2(a_u)^{-1}
          \beta_2(a_u)b_0a_u^{-1}=1.
\tag{24}
\]

Thus the actual norm does not supply the missing equation a_u theta(a_u)=1. Even if that different equation were proved, triviality of H1 for theta would supply a coboundary, not the equality a_u=1. The unique original p_u and its full joint-kernel coordinate remain indispensable.

## 6. An actual original Brunnian cyclic cocycle, with its exact parameter

The canonical norm also puts a further **specified** difference in B. Write

\[
 B_u=u(\sigma^2,\tau^2),\qquad
 W=j(U)YU^{-1},\qquad \Pi_u=LWB_u.
\]

Both Bu and Fb are in B. On their pair, (10) and the original norm give

\[
 \Theta(B_u)=B_uF_b^{-1}.
\tag{25}
\]

Equations (11) and (17), or the exact two-pair norm computation in A122, give

\[
 \Theta(W)=K^{-1}W.
\tag{26}
\]

For example Theta(j(U))=j inverse(U Phi inverse), and
j inverse(Phi)=K inverse j(Phi)K; substitution in Theta(W) cancels the Phi factors in the printed order and yields (26).

The pure element D=C Theta(L) K inverse lies in B. Here it lies in P′ as well: the abelian class of C Theta(L) equals that of K, since the Fb contributions vanish and the unreplaced braid factors have the same pure word K. More directly, D is a product of conjugates of Fb, each in B. Therefore

\[
 c_u=\Theta(\Pi_u)\Pi_u^{-1}\in\mathcal B.
\tag{27}
\]

Indeed Theta(Pi_u)=L D W Bu Fb inverse; multiplying by Pi_u inverse expresses the difference as a product of G-conjugates of D and Fb. The normality in (12) is used here. Since both Pi_u and Theta(Pi_u) have cube one, c_u is a C3-cocycle for rho_u=Ad(Pi_u).

Conjugate by the **actual** p_u inverse and put

\[
 z_u=p_u^{-1}c_up_u\in\mathcal B.
\tag{28}
\]

This is a rho0-cocycle. Its class under (9) is exactly

\[
 \boxed{[z_u]=\partial\bigl(b_0^{-1}\beta_2(a_u^{-1})a_u\bigr).}
\tag{29}
\]

To check the order, set g=p_u inverse h_u p_u. Equation (22) and the defining transporter equality give z_u=g rho0(g) inverse. Thus (8) applies to the lift g inverse. Formulas (21)–(23) yield

\[
 q(g)=\iota\bigl(a_u^{-1}\beta_2(a_u)b_0\bigr),
\]

whose inverse parameter is exactly the one in (29). This proves the formula without choosing any new transporter.

In particular the following are equivalent:

\[
 [z_u]=*,\qquad t_u=1,\qquad h_u\in\mathcal B.
\tag{30}
\]

The last condition means that the unique pure transporter from Pi_u to Theta(Pi_u) belongs to the full joint kernel. It is not the assertion that its C2 class in H1(C2,P′;Theta) is trivial, and no such implication is claimed.

## 7. Precise limitation

The full C3 obstruction space (9), the corrected C2 action (16), and the original cocycle (27)–(29) are exact at their stated actual markings. They do not evaluate b0 or a_u, do not impose a simultaneous-inversion cocycle equation on a_u, and do not identify the actual coherent CM class with a deletion quotient. The joint-kernel part of the unique original transporter has not been dropped. Boundary-power, full hexagon, original coherent-class and CM conclusions remain open.

All new arguments here are symbolic and topological. No mathematical producer, finite target census, new primary theorem or PDF change has been used.
