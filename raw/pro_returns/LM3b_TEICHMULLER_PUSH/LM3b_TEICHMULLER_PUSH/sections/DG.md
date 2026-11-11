# D. Loop structures, arithmetic subgroups, and sections

In D.1--D.5, $K$ is a number field and $U/K$ is a smooth geometrically connected affine hyperbolic curve of type $(g,n)$, $\Delta=\pi_1(U_{\overline K})$, and $\Pi=\pi_1(U)$. All subgroups are closed and all homomorphisms are continuous. The later category and centralizer statements allow proper hyperbolic curves as well. A *loop structure of type $(g,n)$* means the image, under an automorphism of $\Delta$, of its standard collection of $n$ conjugacy classes of peripheral procyclic subgroups. This hypothesis is substantially stronger than specifying one arbitrary procyclic subgroup. We write $\chi_K:G_K\to\widehat{\mathbb Z}^{\times}$ for the cyclotomic character. We inspected scans 479 and 483--488. The first assertion of scan 483 concerns a whole loop structure; the subsequent proposed normalizer test concerns individual subgroups. They require separate conclusions.

## D.1. Proved: the determinant of a peripheral automorphism

Let $F$ be either the free profinite group or the free pro-$\ell$ group of an affine hyperbolic type $(g,n)$, with $n\geq1$ and $2g+n>2$, and let $u\in\operatorname{Aut}(F)$ fix each peripheral conjugacy class. If $c_1,\ldots,c_n$ are peripheral generators, write
\[
 u(c_i)=v_i c_i^{\lambda_i}v_i^{-1}.
\]
For $n\geq2$ all $\lambda_i$ coincide; for $n=1$ put $\lambda=\lambda_1$. Then
\[
 \det(u\mid F^{\mathrm{ab}})=\lambda^{g+n-1}. \tag{D.1}
\]
This identity is integral, including at $\ell=2,3$.

**Proof.** We can check the identity over $R=\mathbb Z_\ell$ for every prime. Choose the surface presentation
\[
 \prod_{j=1}^{g}[a_j,b_j]\,c_1\cdots c_n=1.
\]
The classes of $c_1,\ldots,c_{n-1}$ freely generate a direct summand $W$ of $H=F^{\mathrm{ab}}$, and $[c_n]=-\sum_{i<n}[c_i]$. Applying $u$ proves the equality of the exponents when $n\geq2$. For $n=1$, the nonzero primitive class $\sum_j[a_j,b_j]$ in $\Gamma_2F/\Gamma_3F$ makes the exponent unambiguous.

Pass to the class-two quotient and further kill the commutators of the $c_i$ with all generators. Equivalently, in its central commutator module we quotient by $W\wedge H$. This quotient is preserved by $u$. The $c_i$ are now central, so their conjugating elements disappear. The defining surface relation gives
\[
 (\Lambda^2\bar u)(\omega)=\lambda\omega,
 \qquad \omega=\sum_{j=1}^{g}\bar a_j\wedge\bar b_j
 \quad\hbox{in }\Lambda^2(H/W).
\]
For $n=1$ the same argument uses the ordinary class-two quotient. If $M$ is the matrix on $H/W$ and $J$ the standard alternating matrix, this is $MJM^t=\lambda J$. The polynomial Pfaffian identity
$\operatorname{Pf}(MJM^t)=\det(M)\operatorname{Pf}(J)$ gives $\det M=\lambda^g$ over $R$, without dividing by $2$ or by $g!$. On $W$ the action is scalar $\lambda$. Multiplying the two determinants proves (D.1). The class-two free nilpotent quotient has commutator module $\Lambda^2H$: this follows from the integral collection formula on a free basis and passage to the inverse limit of the finite class-two quotients. In particular, for rank two it is $\mathbb Z_\ell$ at each prime and $\widehat{\mathbb Z}$ in the profinite case. No injectivity of the map from the full profinite group to its pronilpotent quotient is used. $\square$

## D.2. Proved: a useful strengthening of cyclotomic recognition

Let $z\ne1$ in $\Delta$, and let a subgroup $N\subseteq\Pi$ normalize $L=\overline{\langle z\rangle}$ with open image in $G_K$. Suppose there is a positive integer $d$ such that the conjugation character $\psi$ on $L$ satisfies, at every nontrivial pro-$\ell$ component of $L$,
\[
 \bigl(\psi_\ell\chi_{K,\ell}^{-1}\bigr)^d=1. \tag{D.2}
\]
Then $z$ belongs to a genuine cuspidal inertia subgroup. In particular, a maximal procyclic $L$ satisfying these conditions is a cuspidal inertia subgroup.

**Proof.** We use Nakamura (1994, Lemma 2.1.4 and the proof of Theorem 2.1.1), with its precise finite-cover test. If $z$ does not belong to the union $Z$ of the conjugates of cuspidal inertia, that lemma supplies an open subgroup $H\subseteq\Delta$ containing $z$ and a prime $\ell$ such that
\[
 z\notin\overline{[H,H]H^\ell\langle Z\cap H\rangle}. \tag{D.3}
\]
The finite étale geometric cover corresponding to $H$ descends to a number field after finite extension. We choose an arithmetic open subgroup with geometric intersection $H$. Intersecting it with $N$ preserves openness of the projected image. By (D.2), the continuous character $\psi_\ell\chi_{K,\ell}^{-1}$ takes values in the finite group $\mu_d(\mathbb Z_\ell)$. We further intersect with its kernel and descend once more. We need this finite extension only for the one prime selected in (D.3).

Let $Y$ be the resulting cover and let $H_{\ell}^{\mathrm{ab}}=H_1(Y_{\overline K},\mathbb Z_\ell)$. The image of $z$ is nonzero modulo the boundary part, by (D.3). Its cyclic span, however, is acted on cyclotomically. After making the boundary points rational, the boundary part has character $\chi_{K,\ell}$, whereas the quotient is the Tate module of the Jacobian. At a prime of good reduction away from $\ell$, the eigenvalues on the latter have complex absolute value $q^{1/2}$ and the cyclotomic eigenvalue has absolute value $q$. Thus no nonzero cyclotomic line occurs in the Jacobian quotient. This contradicts (D.3). The weight assertion is exactly the input used in Nakamura's proof. Maximality concludes the last assertion. A single extension killing all primewise twists is unnecessary. $\square$

There is a stronger single-prime formulation. It suffices that (D.2) hold for one nontrivial pro-$\ell$ component. Let $z_\ell$ generate that component of $L$ and intersect $N$ with the kernel of its finite twist. Its normalizer action on $\overline{\langle z_\ell\rangle}$ is then exactly cyclotomic, so Nakamura's Theorem 2.1.1, applied to the element $z_\ell$ in the *full* profinite group, puts it in actual inertia $I$. Since $L$ centralizes $z_\ell$, Boggi and Zalesskii (2019, Proposition 3.6) gives $L\subseteq I$. That proposition allows every nonzero profinite exponent, including an exponent supported at a single prime; this qualification is needed here. The geometric pro-$\ell$ version also follows: Nakamura's Theorem 2.1.1 and Lemma 2.1.4 are stated for every full class $\mathcal C$ of finite groups, so one takes $\mathcal C$ to be the finite $\ell$-groups, retains $n\geq1$ and $2g+n>2$, and uses the geometrically pro-$\ell$ arithmetic extension defined in his \S2.1. This does not deduce the pro-$\ell$ assertion merely by quotienting a full-profinite cover.

## D.3. Proved: uniqueness of the invariant loop structure for every affine hyperbolic type

The genuine cuspidal loop structure of $U$ is the unique loop structure of type $(g,n)$ on $\Delta$ invariant under $\rho_U(G_K)$. In particular, this settles the first half of LM3 D.23 at $(1,1)$ and for every affine hyperbolic curve over a number field, in the specified meaning of loop structure. It proves the first conjectural sentence beginning “Ce n'est pas la peine” in §34, folio 245, scan 483.

**Proof.** After finite extension, both the actual and the candidate sets of peripheral classes are individually fixed. Put $d=g+n-1>0$. For the actual Galois action,
\[
 \det\bigl(\rho_U(\sigma)\mid\Delta^{\mathrm{ab}}\bigr)
 =\chi_K(\sigma)^{g+n-1}.
\]
Indeed, the boundary module has rank $n-1$ and scalar action $\chi_K$; the Jacobian Tate module has a perfect alternating pairing with multiplier $\chi_K$, hence determinant $\chi_K^g$. On the other hand, D.1 applied to the candidate loop structure computes the very same determinant as $\lambda(\sigma)^d$. If $I$ is one chosen candidate subgroup, its arithmetic normalizer maps onto the restricted $G_K$: invariance of its conjugacy class lets us correct any lift of a Galois element by an element of $\Delta$. On this normalizer, D.1 gives $\psi^d=\chi_K^d$, including on its geometric kernel. D.2 therefore places a generator of $I$ in actual inertia. A candidate peripheral subgroup is maximal procyclic, since this is true of standard peripheral subgroups and is invariant under automorphisms; see Boggi and Zalesskii (2019, Proposition 3.6). Thus $I$ equals that actual inertia subgroup. The $n$ candidate conjugacy classes are distinct, so they exhaust the $n$ genuine classes. Finite base extension does not change the geometric inertia collection. $\square$

For $(1,1)$ one can shorten the argument. Here $\Gamma_2\Delta/\Gamma_3\Delta\simeq\widehat{\mathbb Z}$ and the candidate commutator has a unit coefficient. The action on this quotient is the determinant of $\widehat T E$, namely $\chi_K$. The normalizer exponent is therefore exactly cyclotomic before any finite twist is removed. This proof closes the specific missing step identified in LM3 D.23; the fact that the peripheral commutator has zero abelianization is not an obstruction in degree two.

## D.4. Open: the bare maximal-procyclic normalizer criterion

The statement that *every* maximal procyclic subgroup of $\Delta$ whose arithmetic normalizer has open image in $G_K$ is cuspidal is not proved by D.3. We retain this stronger statement, without its exponent hypothesis, as unresolved here; its smallest requested case is an elliptic curve minus its origin over a number field. Our attack is the following exact dichotomy, which validates the useful part of Lead 6 and identifies its missing step.

Choose a topological generator $z$ of the nontrivial procyclic group $L$, and a prime $\ell$ for which its pro-$\ell$ component is nontrivial. Since $L^\ell$ is a proper open subgroup of $L$, the subspace topology supplies an open normal subgroup $M\triangleleft\Delta$ with $M\cap L\subseteq L^\ell$. Set $H=M L$. The generator $z$ is nonzero modulo $\ell$ in the finite cyclic quotient $H/M=L/(M\cap L)$, and hence in $H^{\mathrm{ab}}\otimes\mathbb Z_\ell$. A finite extension of $K$ makes $H$ a geometric cover subgroup; intersecting $N$ with the corresponding arithmetic open subgroup preserves open arithmetic image and makes it normalize $H$. Thus its exponent occurs on the nonzero line generated by $z$ in that homology. The exact sequence is
\[
 0\longrightarrow\text{boundary Tate module}\longrightarrow
 H_1(Y_{\overline K},\mathbb Q_\ell)\longrightarrow V_\ell J_Y\longrightarrow0.
\]
If the resulting line lies in the boundary module after rationalizing the cusps, its character is cyclotomic. If it projects nontrivially to $V_\ell J_Y$, its Frobenius weight is one. Complex multiplication supplies examples of the latter *linear* phenomenon. It supplies no inverse-limit lifting theorem for a procyclic subgroup of the nonabelian fundamental group. D.1 excludes this possibility for a whole alternative surface loop structure; it does not apply to an arbitrary procyclic subgroup.

The strongest unconditional corrected recognition test used here is D.2, or equivalently Nakamura's original cyclotomic-normalizer test when that character is specified exactly. The remaining implication is explicitly:
\[
\begin{gathered}
 p(N_\Pi(L))\text{ open},\quad L\text{ maximal procyclic}
 \\
 \Longrightarrow\quad \text{$L$ has a potentially cyclotomic nontrivial prime component}.
\end{gathered}
\]
No complex-multiplication counterexample in the full $\Delta$ is constructed in this paper.

## D.5. Refuted: the corresponding criterion on the class-two pro-5 quotient

The analogue of D.4 becomes false after replacing $\Delta$ by its class-two pro-$5$ quotient. Take $E:y^2=x^3-x$ over $K=\mathbb Q(i)$ and $U=E\setminus\{O\}$. Since $5$ splits in $\mathbb Z[i]$, the module $T_5E$ is the direct sum of two primitive $G_K$-stable rank-one summands. Choose a free pro-$5$ basis $x,y$ whose abelianizations are bases of these summands, and write
\[
 N=\Delta^{(5)}/\Gamma_3\Delta^{(5)},\qquad c=[x,y].
\]
For any arithmetic lift of $\sigma$, the image of $x$ has the form $x^{\alpha(\sigma)}c^{t(\sigma)}$, where $\alpha(\sigma)\in\mathbb Z_5^{\times}$. Conjugating by a suitable power of $y$ cancels the central factor because $\alpha(\sigma)$ is a unit. Hence $\langle x\rangle\simeq\mathbb Z_5$ has arithmetic normalizer with full image in $G_K$. It is maximal procyclic by its primitive abelianization and cannot be peripheral: the genuine cusp is generated by $[x,y]$ and has zero abelianization.

The basis exists by lifting a $\mathbb Z_5$-basis to two elements of the free pro-$5$ group and using the Frattini criterion. The explicit Heisenberg calculation, including the required division by a unit, is checked in `code/dg_checks.py` modulo $5$, $25$, and $125$. This is a counterexample on a specified nilpotent quotient, not on the full pro-$5$ or profinite fundamental group. Beyond class two, compatible conjugators and compatible cyclic generators must be constructed; neither the CM decomposition nor this calculation supplies them.

## D.6. Known, with reduction: Pop's answer using birational localization

Put $U_0=\mathcal M_{0,4}=\mathbb P^1\setminus\{0,1,\infty\}$ and $X=\mathcal M_{0,5}\subset U_0^2$, with independent coordinates $s,t$. Let $\mathcal B$ be a cofinal system of nonempty opens of $X$ defined over $\mathbb Q$, closed under refinement enough that the rational functions $s,t,t-s$ define maps to $U_0$ on the relevant opens. Let $\mathcal V$ have these opens and $U_0$ as objects, inclusion maps, and these three restricted maps. Then restriction to $U_0$ identifies
\[
 \operatorname{Aut}\bigl(\pi_1((-)_{\overline{\mathbb Q}})|_{\mathcal V}\bigr)
 \simeq G_{\mathbb Q}
\]
with the arithmetic subgroup in $\operatorname{Out}(\widehat F_2)$, and hence in the standard $\widehat{\mathrm{GT}}$ and $\widehat{\mathrm{GT}}_0$ containers. Here automorphisms are compatible families of outer automorphisms; they fix the labelled objects and arrows of $\mathcal V$.

**Reduction.** Apply Pop (2018, Theorem 2.7(1)); in characteristic zero the valuation-tame fundamental groups in that theorem are the full geometric profinite groups. We check its Hypothesis (H), Definition/Remark 2.2. The dimension is two and $\overline{\mathbb Q}(s,t)=\overline{\mathbb Q}(s,t,t-s)$. For rigidity, a compatible birational automorphism acts on all three coordinates through the same automorphism $h$ of the tripod. After separating the field automorphism on constants, $h$ is one of the six Möbius functions
\[
 z,\quad1-z,\quad z^{-1},\quad(1-z)^{-1},\quad z/(z-1),\quad(z-1)/z.
\]
Compatibility with $t-s$ gives the rational identity $h(t-s)=h(t)-h(s)$. Of those six functions, only $h(z)=z$ satisfies it. This can also be seen by differentiating the identity in the two independent variables: $h'$ must be constant, and the only additive affine member of the six-element group is the identity. Thus the birational automorphism is the identity on $\mathbb Q(s,t)$ and only a field automorphism of the algebraic constants remains. This is precisely rigidity. The theorem gives the stated group, and its restriction to $U_0$ is the usual faithful arithmetic representation. Pop's Theorem 2.6(1) gives the analogous abelian-by-central pro-$\ell$ statement, with the scalar quotient required in his definition. $\square$

The objects added beyond the two moduli levels are infinitely many Zariski localizations, not merely the existing five forgetting maps. In particular $t-s$ is not everywhere a morphism $\mathcal M_{0,5}\to U_0$; one removes its $0,1,\infty$ fibres where necessary. The exact extra requirement in Grothendieck's language is *extendability to this localized functor*. This gives an algebraic characterization of the image asked for in §33 bis, folio 242 verso, scan 479, without asserting that every element of $\widehat{\mathrm{GT}}$ extends.

## D.7. Known, with reduction: the Hoshi–Mochizuki–Tsujimura characterization

Let $P_2=\pi_1(\operatorname{Conf}_2(U_{0,\overline{\mathbb Q}}))=\pi_1(\mathcal M_{0,5,\overline{\mathbb Q}})$. Under the standard identification of the genus-zero tower automorphism group with $\widehat{\mathrm{GT}}$, the $\widehat{\mathrm{GT}}$-conjugates of the arithmetic subgroup are exactly the inclusion-maximal closed subgroups satisfying the AA-property of Hoshi, Mochizuki, and Tsujimura (2025, Definition 5.12). This is their Theorem C(ii), equivalently Theorem 5.17(ii), transported to Grothendieck's normalizer quotient.

**Reduction and retained data.** Their Corollary 4.5 and Remark 4.5.1 reconstruct the relevant containers from the abstract profinite group $P_2$. A subgroup $B$ first has to satisfy the COF and RGC conditions of Definition 3.3: common dominating arithmetic Belyi diagrams must exist, and geometric dominations between such diagrams are unique. These diagrams include finite étale covers, open immersions, the associated second configuration groups, their fibre subgroups, and the appropriate cuspidal quotients. Theorem A constructs a set $Q_B$ with operations; the ArBC condition says these operations make it an algebraic closure of $\mathbb Q$. Definition 5.12 then quantifies over all normal open subgroups of the reconstructed groups and all finite sets of cusps. It imposes the specified Kummer nondegeneracy and restriction-injectivity conditions, a compatible family of function fields obtained from cusp-evaluation functions, and compatibility of the resulting geometric group identification with the second configuration group. Thus the AA condition is a predicate on rich group-theoretic data extracted using $P_2$, not the assertion that an automorphism of two isolated groups preserves five arrows.

Theorem 5.15(iv) places any such subgroup inside a $\widehat{\mathrm{GT}}$-conjugate of $G_{\mathbb Q}$. The arithmetic subgroup itself satisfies AA (Remark 5.12.1, or Theorem 6.8 for $K=\mathbb Q$). Theorem 5.17(ii) then gives the maximality characterization. This proves the exact translated assertion; a chosen arithmetic marking is still needed to select one subgroup from its conjugacy class. No claim that all of $\widehat{\mathrm{GT}}$ is AA is made. The refinement in Theorem C(i) uses QAA and conjugacy in the larger label-preserving outer automorphism group.

## D.8. Proved: the arithmetic subgroup is self-commensurating in the label-preserving container

Let $A\subseteq\operatorname{Out}(\widehat F_2)$ be the subgroup fixing each of the three genuine peripheral conjugacy classes, and use the standard arithmetic embedding $G_{\mathbb Q}\subseteq A$. Then
\[
 \operatorname{Comm}_{A}(G_{\mathbb Q})=G_{\mathbb Q}. \tag{D.4}
\]
In the full outer automorphism group the same argument gives $\operatorname{Comm}(G_{\mathbb Q})=G_{\mathbb Q}\mathfrak S_3$, with the standard commuting geometric $\mathfrak S_3$.

**Proof.** A commensurating element induces, by conjugation, an isomorphism between two open subgroups of $G_{\mathbb Q}$. These are absolute Galois groups of number fields. Uchida's isomorphism theorem (1979, main theorem, applied to algebraic closures) realizes the isomorphism by a field automorphism $\sigma\in G_{\mathbb Q}$. After multiplying by its inverse, our element centralizes $\rho(G_L)$ for one number field $L$. The full profinite Isom consequence of Mochizuki (1999, Theorem A = Theorem 16.5) identifies this centralizer with $\operatorname{Aut}_L(U_0)=\mathfrak S_3$: a commuting outer automorphism gives an isomorphism of the centre-free arithmetic extension over $G_L$, then the Isom theorem applies. The label-preserving subgroup intersects this $\mathfrak S_3$ trivially. This proves (D.4). Conversely arithmetic conjugation and the six geometric automorphisms visibly commensurate the arithmetic group. $\square$

Hoshi–Mochizuki–Tsujimura (2025, Theorem 6.8(ii)) gives the corresponding containment inside $\widehat{\mathrm{GT}}$ in the substantially wider TKND-AVKF setting. For number fields the proof above supplies the exact reduction requested here. The same argument proves that the centralizer of every open subgroup of either $\widehat{\mathrm{GT}}$ or $\widehat{\mathrm{GT}}_0$ in that container is trivial: intersect the open subgroup with $G_{\mathbb Q}$ and apply the label-preserving form of the centralizer calculation. This supplies the centralizer assertion used in the marginal insertion of \S34, scan 486, without identifying the whole container with $G_{\mathbb Q}$.

## D.9. Proved: a precisely typed geometric-section stabilizer equals the arithmetic image

For $m=4,5$ put $P_m=\pi_1(\mathcal M_{0,m,\overline{\mathbb Q}})$. For the standard outer $\widehat{\mathrm{GT}}$-action define its centre-free extension
\[
 E_m=\operatorname{Aut}(P_m)\mathbin{\times}_{\operatorname{Out}(P_m)}\widehat{\mathrm{GT}},
 \qquad1\to P_m\to E_m\xrightarrow{p}\widehat{\mathrm{GT}}\to1.
\]
Its pullback over $G_K\subseteq G_{\mathbb Q}$ is the arithmetic fundamental-group extension of $\mathcal M_{0,m,K}$. Let $\mathcal S_m$ be the set of $P_m$-conjugacy classes of section-image subgroups obtained from rational points and nonzero rational tangential base points, over all finite $K/\mathbb Q$. Let $\widehat{\mathrm{GT}}$ act on this ambient set of subgroup classes by conjugation by a lift in $E_m$; the result is independent of the lift modulo $P_m$-conjugacy. Then
\[
 \operatorname{Stab}_{\widehat{\mathrm{GT}}}(\mathcal S_4)
 =\operatorname{Stab}_{\widehat{\mathrm{GT}}}(\mathcal S_4,\mathcal S_5)
 =G_{\mathbb Q}. \tag{D.5}
\]
For $\widehat{\mathrm{GT}}_0$, form $E_4$ with that container; the same statement for $\mathcal S_4$ holds.

**Proof.** An arithmetic element transports a point, a tangent vector, and its field of definition by the corresponding field automorphism. It therefore preserves the designated family. Conversely take the section of the rational point $2\in U_0(\mathbb Q)$. Its image projects onto all of $G_{\mathbb Q}$. If $a$ preserves $\mathcal S_4$, the projection of its transported section image, namely $aG_{\mathbb Q}a^{-1}$, is an open subgroup of $G_{\mathbb Q}$. Thus $a$ commensurates $G_{\mathbb Q}$ and D.8 gives $a\in G_{\mathbb Q}$. The two containers are label-preserving, so this proof applies to both. For $m=5$, $(s,t)=(2,3)$ also gives a rational section; it is not needed for the converse. $\square$

This equality has an essential qualification. The data $\mathcal S_m$ already specify geometric sections with their arithmetic domains; it is not an arithmetic-free test on an arbitrary abstract $\widehat{\mathrm{GT}}$ element. Without a rule transporting the base $G_K$, “preserving sections” is not a defined action. If one asks instead for an intrinsic recognition of admissible complements without supplying their geometric/arithmetic marking, (D.5) does not solve that recognition problem. Pop's localized system and the AA predicate are genuine sufficient enrichments. In particular we do not assert that Grothendieck's empty list of extra conditions at $(1,1)$ in scan 487 recognizes all geometric complements; scan 488 itself warns that it might not.

## D.10. Known, with reduction: Kummer and Nakamura–Schneps data retained by the stabilizer

For $t\in U_0(K)$, abelianization of its geometric section relative to a tangential normalization gives the Kummer pair
\[
 (\kappa_K(t),\kappa_K(1-t))\in H^1(G_K,\widehat{\mathbb Z}(1))^2.
\]
For $\mathcal M_{0,5}$ the analogous classes come from the units $s,t,1-s,1-t,t-s$. A field automorphism transports these classes by $\kappa_K(a)\mapsto\kappa_{\sigma K}(\sigma a)$. This follows directly by applying $\sigma$ to compatible roots of $a$ in the Kummer cocycle. At a tangent vector one uses the leading nonzero coefficient of the function in the chosen local parameter; changing the path changes a cocycle by a coboundary. Consequently D.9 preserves these cohomology classes and all their functorial pullbacks. It does not canonically fix a cocycle representative after the paths and roots have been forgotten.

For the standard Drinfeld pair $(\lambda,f_\sigma)$, the Kummer class of $2$ is the class of the Nakamura–Schneps cocycle $\rho_2$. In the notation of Nakamura and Schneps (2000, equation (2.4) and Lemma 2.3), if
$f_\sigma\equiv A_\sigma(\bar x,\bar y)[x,y]\pmod{\widehat F_2''}$, then
\[
 \rho_2(\sigma)=-A_\sigma(-1,1).
\]
Their Theorem 1.1 and Theorem 2.1 impose, respectively, relations $(\mathrm{III}')$ and $(\mathrm{IV})$ on every arithmetic pair; Theorem 1.2 packages them as the refined subgroup $\mathrm I\Gamma\subseteq\widehat{\mathrm{GT}}$. Since the stabilizer in D.9 equals the arithmetic subgroup, every one of its elements satisfies these two relations. This inference uses the precise arithmetic marking in D.9; preservation of an unmarked set of point sections has not independently been shown to force the elliptic relation $(\mathrm{IV})$.

## D.11. Known, with reduction: centralizers for curves of the requested types

For every hyperbolic curve $U/K$ over a number field,
\[
 C_{\operatorname{Out}(\Delta_U)}(\rho_U(G_K))=\operatorname{Aut}_K(U). \tag{D.6}
\]
The proof is the centre-free extension construction followed by Mochizuki (1999, Theorem A/16.5), exactly as in D.8. Conversely functoriality sends every $K$-automorphism to the centralizer. The two constructions are inverse by the Isom theorem, so this is an equality of naturally identified groups, not just an injection.

For type $(0,4)$ or $(0,5)$, write $C$ for the genus-zero compactification and $D=C\setminus U$ for its reduced puncture divisor. The answer is $\operatorname{Aut}_K(C,D)$. When $C\simeq\mathbb P^1_K$, it is the subgroup of $\operatorname{PGL}_2(K)$ preserving $D$. A type $(0,4)$ compactification can be a nonsplit conic, so this qualification matters. For type $(0,5)$ the odd-degree divisor $D$ forces the conic to split: its degree-two canonical class and $D$ give a divisor class of degree one, whose Riemann--Roch space supplies a $K$-point. A generic rationally marked quadruple has the Klein four-group: the action of $\mathfrak S_4$ on its cross-ratio factors through $\mathfrak S_3$ with that kernel, and a generic cross-ratio has trivial stabilizer in the latter. A generic rationally marked quintuple has trivial group, since each nonidentity permutation imposes a proper algebraic equality among its cross-ratios.

For $(1,1)$ the unique missing point is $K$-rational and identifies the compactification with an elliptic curve $(E,O)$. Its answer is $\operatorname{Aut}_K(E,O)$. In a short Weierstrass equation $y^2=x^3+Ax+B$, an automorphism fixing $O$ has the form $(x,y)\mapsto(u^2x,u^3y)$, with $u\in K^{\times}$, $u^4A=A$ and $u^6B=B$. Consequently the group is $\mu_2(K)$ if $AB\ne0$, $\mu_4(K)$ if $B=0$, and $\mu_6(K)$ if $A=0$. These curve statements depend on the curve and must not be confused with the symmetric groups in the following moduli-space statement.

## D.12. Known, with reduction: Nakamura's moduli centralizers

For an odd prime $\ell$ and $m\geq4$, Nakamura (1994, Theorem A) gives
\[
 C_{\operatorname{Out}(\pi_1^{(\ell)}(\mathcal M_{0,m,\overline K}))}
       (\rho(G_K))
 \simeq\begin{cases}\mathfrak S_3,&m=4,\\\mathfrak S_m,&m\geq5.\end{cases}
\]
His Theorem B gives $C_{\operatorname{Out}(L_\ell(\Gamma_0^m))}(\rho^{\mathrm{Lie}}(G_K))=\mathfrak S_m$ for $m\geq5$, where $L_\ell(\Gamma_0^m)$ is the inverse limit of the $\mathbb Q_\ell$ Lie algebras associated to the nilpotent quotients of the pure sphere mapping class group, as defined in his \S4.2.2. In Grothendieck's notation these are arithmetic-compatible symmetries of the indicated geometric modular groups. To pass from Theorem A's arithmetic-automorphism formulation to the displayed centralizer, use the centre-freeness of the geometric group: an extension with centre-free kernel is the pullback of $\operatorname{Aut}(P)\to\operatorname{Out}(P)$ along its outer action. An automorphism over $G_K$, modulo conjugation by $P$, is therefore exactly a commuting outer automorphism of $P$. The six automorphisms of the tripod, or permutations of $m$ labels for $m\geq5$, are defined over $\mathbb Q$ and supply the full listed centralizer. The theorem has an odd-prime hypothesis; it is not silently extended to $\ell=2$ or to arbitrary elliptic pro-$\ell$ groups.

## D.13. Known, with reduction: the category statement in §34

Fix $K$ and let the objects be arithmetic fundamental-group extensions of hyperbolic curves over $K$, retaining the augmentation to $G_K$. The category with dominant morphisms is fully faithfully described by open continuous $G_K$-homomorphisms of these extensions, modulo inner automorphisms of the target geometric kernel. This is Mochizuki (1999, Theorem A/16.5), applied with source and target smooth curves. The comparison is covariant on fundamental groups, and both composition and identity are respected by functoriality; bijectivity on each Hom set gives a category equivalence onto the essential image.

To include constant morphisms one must additionally retain the *geometric* point sections of the target: a constant $K$-map is exactly a choice of a $K$-point, and its group map factors through $G_K$. Distinct geometric point sections are distinguished by the injectivity part of the section theorem (Mochizuki, Theorem C); replacing them by all abstract sections would require a section-surjectivity assertion and is not justified here. Tangential sections are retained as boundary data, not identified with interior constant maps. This supplies the precise category description supported by the cited theorems, while the arithmetic-free recognition of all admissible objects and splittings remains a separate problem. The exceptional nonhyperbolic types have nontrivial or trivial geometric kernels and do not satisfy this description; the real and nonorientable topological variants are not substitutes for the stated number-field algebraic category.

## D.14. Proved: an explicit essential-image construction from the arithmetic tripod

Allow the finite number field to vary inside $\overline{\mathbb Q}$. Starting from the arithmetic tripod extension $\Pi_0\to G_{\mathbb Q}$, take an open subgroup $E'\subseteq\Pi_0$ and then quotient by the closed normal subgroup generated by a Galois-stable collection of its geometric peripheral subgroups. Retain only hyperbolic resulting types. The resulting arithmetic extensions are exactly those of hyperbolic curves over number fields, up to isomorphism over their projected open subgroup of $G_{\mathbb Q}$. With the arrows of D.13 this is the essential-image description proposed immediately after scan 483, in §34, scan 484.

**Proof.** Write $p(E')=G_K$. Galois theory of finite étale covers identifies $E'$ with the arithmetic group of a geometrically connected finite étale cover $V\to U_{0,K}$. The normalization of $\mathbb P^1_K$ in $K(V)$ is its unique smooth proper compactification. A Galois-stable subset of its geometric boundary is a divisor defined over $K$; adjoining precisely those missing points gives a smooth curve $U/K$. The fundamental group of $U$ is the quotient of that of $V$ by the closed normal closure of the inertia subgroups at the filled points. Indeed a finite cover of $V$ extends étale across those points exactly when those local inertia groups act trivially. This proves one direction and types the quotient map explicitly.

Conversely, let $C/K$ be the smooth proper compactification of $U$. Choose any nonconstant $f\in K(C)$, and let $S\subseteq\mathbb P^1(\overline{\mathbb Q})$ contain its branch values and $f(C\setminus U)$. Enlarge $S$ to its finite union of $\mathbb Q$-conjugates. Belyi's proof of Theorem 4 (1980, pp. 255--256) constructs polynomial postcompositions in $\mathbb Q[t]$: the first sends $S$ and its own critical values into $\mathbb P^1(\mathbb Q)$, and the second sends that finite rational set and its critical values into $\{0,1,\infty\}$. The construction uses successive minimal polynomials of critical-value sets, whose degrees strictly decrease, followed by the rational polynomials proportional to $t^a(1-t)^b$ for rational $a/(a+b)\in(0,1)$. Thus the composite $b:C\to\mathbb P^1$ is defined over the original $K$, is branched only over $\{0,1,\infty\}$, and sends the boundary into that set. Removing $b^{-1}\{0,1,\infty\}$ gives a finite étale cover $V\to U_{0,K}$ with $V\subseteq U$. Its arithmetic group is an open $E'\subseteq\Pi_0$ projecting onto $G_K$, and filling the extra removed points recovers $U$. No enlargement of $K$ or additional descent datum is needed. $\square$

The insertion “morphismes les morphismes dominants” in the transcription at scan 484 is mathematically consequential: it matches precisely the open-Hom theorem used in D.13. Neither possible handwriting variant “extérieur/extérieure” changes this statement. The construction uses an identified arithmetic tripod, supplied for example by D.6 or the marked form of D.7; it does not identify every abstract action on a surface group as geometric.

# G. Independent verification of the requested steps of manuscripts 019 and 031

The labels below concern the exact propositions proved, with their external inputs specified. They do not constitute a certification of every statement in either manuscript. We read the supplied October 6 version of 019, the October 5 version of 031, and the relevant primary inputs. The separate September 24 exterior-sheet manuscript is not used in any proof below. No priority claim is made.

## G.1. Proved: division on a torically uniformized abelian variety

Let $\Omega$ be complete and algebraically closed of characteristic zero. Suppose an abelian variety has analytic uniformization $q:T^{\mathrm{an}}\to J^{\mathrm{an}}$ by a split torus, with discrete torsion-free lattice $\Lambda$, and $q$ is a topological covering and local analytic isomorphism. If $a:A\to T^{\mathrm{an}}$ is analytic and
\[
 B=A\mathbin{\times}_{q\circ a,J^{\mathrm{an}},[m]}J^{\mathrm{an}},
\]
then every torus character $\eta\circ a$ has an analytic $m$th root on the whole of $B$, for every positive integer $m$.

**Proof.** Write $b:B\to J^{\mathrm{an}}$ for the second projection. Locally lift $b$ to $t:B\to T^{\mathrm{an}}$. The quotient $t^m/a$ lies in the discrete group $\Lambda$ and is locally constant. Its image in $\Lambda/\Lambda^m$ is independent of the lift. Decompose $B$ into the finitely many clopen pieces determined by these classes. Fix a representative $\lambda$ on one piece. Adjust local lifts by locally constant periods until $t^m=\lambda a$. On an overlap two adjusted lifts differ by $\rho\in\Lambda$ with $\rho^m=1$; torsion-freeness gives $\rho=1$. They therefore glue on the entire piece. Choose an $m$th root of $\eta(\lambda)$ in $\Omega$. Dividing $\eta(t)$ by that root gives the desired function. The pieces are disjoint, so the functions assemble globally. No invertibility of $m$ in the residue field enters. $\square$

## G.2. Proved: manuscript 019, Proposition 5.2, including every inverse annulus

Let $k/\mathbb Q_p$ be finite, normalize $v(p)=1$, fix an odd prime $\ell\ne p$, and let $m\geq1$. Choose an integer $D>v_p(m)+1/(p-1)$ and $\alpha\in k^{\times}$ with $a=v(\alpha)>2D$. There is a smooth proper connected curve $Q/k$ and a finite map $Q\to\mathbb P^1_k$, all of whose ramification indices divide $\ell$, such that $T$ has an analytic $m$th root on the entire inverse image over $\Omega=\widehat{\overline k}$ of
\[
 A^{\circ}=\{D<v(T)<a-D\}.
\]

**Proof.** Consider the smooth projective normalization $Z$ of
\[
 y^\ell=\frac{T(T-1)}{T-\alpha}.
\]
The four valuations of the right side at $0,\alpha,1,\infty$ are $1,-1,1,-1$. The cover is connected and totally ramified there, and nowhere else; Riemann–Hurwitz gives $g(Z)=\ell-1$.

We give the needed stable model explicitly after a finite extension of constants. Blow up the model of the line at the ideal $(T,\alpha)$. The node chart has $TU=\alpha$, and the inner component has coordinate $S=T/\alpha$. The Kummer functions on the outer and inner components reduce respectively to $T-1$ and $-S/(S-1)$. Both normalized covers are rational, since each is cyclic of degree $\ell$ with precisely two total branch points. At the node the equation is
\[
 y^\ell=(T-1)/(1-U),
\]
a unit reducing to $-1$. As $\ell$ is invertible, adjoining its roots is étale there and splits into $\ell$ node charts after finite constant extension. At each branch section one takes an $\ell$th root of a simple parameter, so the normalized curve is smooth at that section. Away from nodes and branch sections it is étale. The special fibre therefore consists of two rational components joined by exactly $\ell$ nodes of thickness $a$. Since $\ell\geq3$, both components are stable. This verifies total degeneration and the exact metric graph, rather than assuming them from a schematic picture.

Over the open annulus $0<v(T)<a$, the Kummer function is
$-(1-T)/(1-\alpha/T)$. Both factors have convergent $\ell$th roots, so its inverse image is the disjoint union of $\ell$ annuli $A_j$, each with coordinate $T$. Let $J=\operatorname{Jac}(Z)$ and choose the Abel–Jacobi map using the $k$-rational point above $T=0$. Total degeneration gives the toric uniformization of G.1. For the exact input we use Baker and Rabinoff (2015, §4.1–§4.2 and §4.5.2); their Proposition 6.1 and Corollary 6.6 identify the tropical Abel–Jacobi map with integration on the metric graph. The graph has edges $e_1,\ldots,e_\ell$, all of length $a$, and character lattice $H_1(\Gamma,\mathbb Z)$.

The Berkovich annulus retracts to an interval and is locally path connected, so the Abel–Jacobi map on $A_j$ lifts along the topological covering $T^{\mathrm{an}}\to J^{\mathrm{an}}$; local analytic inverses make the lift analytic. For $j'\ne j$, the integral cycle $e_j-e_{j'}$ defines a torus character whose pullback $u_j$ has slope exactly one with respect to $s=v(T)$ on $A_j$. This follows by pairing the cycle with an oriented segment of $e_j$: the integral is its length. It is unaffected by the constant period ambiguity of the lift.

An analytic unit on an annulus over an algebraically closed field has a unique dominant Laurent monomial at every interior Gauss radius. A tie would give a zero, by the Newton polygon criterion on an annulus. Its exponent is constant and equals its slope. Consequently
\[
 u_j=c_jT(1+h_j),\qquad
 h_j=\sum_{r\ne0}b_{j,r}T^r,
\]
and dominance at all radii, followed by limits at the two endpoints, gives
$|b_{j,r}|\leq1$ and $|b_{j,-r}|\leq|\alpha|^r$ for $r>0$. Therefore
\[
 v(h_j)\geq\min(s,a-s)>D\quad\hbox{on the middle collar}.
\]
On each closed subannulus there is a strict uniform margin. Thus
$\exp(m^{-1}\log(1+h_j))$ converges locally uniformly and is an analytic $m$th root of $1+h_j$: its exponent has valuation greater than $D-v_p(m)>1/(p-1)$. This checks the wild case $p\mid m$ and $p=2$ directly.

Now take the single algebraic finite étale pullback
\[
 Z'=Z\mathbin{\times}_{i,J,[m]}J\longrightarrow Z.
\]
G.1 produces an $m$th root of $u_j$ on the *whole* inverse image of each $A_j$, not merely one component. Dividing by the root of $1+h_j$ and by an $m$th root of $c_j$ gives an $m$th root of $T$ above its middle collar. The $A_j$ are disjoint, so these functions define a root on the entire required inverse image. Any connected component $Q$ of $Z'$ is finite étale and surjective over connected $Z$, hence smooth proper and connected; its composite with $Z\to\mathbb P^1$ has only indices $1,\ell$. All algebraic maps and connected components in this last construction are taken over $k$; the analytic uniformization and roots are required only after base change to $\Omega$. This proves the stated proposition. $\square$

This removes the specific 019 verification obligation isolated in LM3 D.7. It does not by itself reprove the other geometric patching and valuation steps of that manuscript, and we do not relabel its full local section theorem on the strength of this one proposition.

## G.3. Proved: manuscript 031, Lemma 3.1 and its zero estimate

Let $E$ be a number field inside a finite extension $K/\mathbb Q_\ell$. Let $u_1,\ldots,u_m\in(E^{\times})^n$ have algebraic-integer coordinates which are $\ell$-adic units. Suppose that for every nonzero $a\in\mathbb Z^m$ the $n$ coordinates of $u^a=\prod_i u_i^{a_i}$ are multiplicatively independent modulo roots of unity. If $m>n(n-1)$, the vectors $\log u_i$ span $K^n$.

**Proof.** Every nontrivial $u^a$ generates a Zariski-dense cyclic subgroup of $\mathbb G_m^n$. Indeed, evaluate a Laurent polynomial along its powers: distinct monomials give distinct nonzero eigenvalues, so the Vandermonde matrix forces every coefficient to vanish. Suppose the logarithms have rank $r<n$. Rank zero contradicts the root-of-unity kernel of the local logarithm. After one common power, their coordinates are in the exponential convergence domain. Choose an $\mathcal O_K$-basis $b_1,\ldots,b_r$ of the module they generate; after a further common power we have $\eta=\ell^{1/(\ell-1)}\max|b_{tj}|_\ell<1$. Write $\log u_i=\sum_tz_{it}b_t$ with $z_{it}\in\mathcal O_K$. All these choices are fixed before the parameter $D$ tends to infinity.

For $\alpha\in\{0,\ldots,D\}^n$, the monomial evaluation is represented on the logarithmic parameter space by
\[
 f_\alpha(z)=\exp\left(\sum_{j,t}\alpha_jb_{tj}z_t\right)
 =\sum_\nu c_{\alpha,\nu}z^\nu,
 \qquad |c_{\alpha,\nu}|_\ell\leq\eta^{|\nu|}.
\]
Set $A=(D+1)^n$ and choose $S=O(D^{n/m})$ with $(S+1)^m>(nD)^n$. We first prove that the matrix $((u^a)^\alpha)$, with columns $a\in\{0,\ldots,nS\}^m$ and the indicated $A$ rows, has full row rank. Otherwise a nonzero polynomial $P$, of degree at most $D$ in each variable, vanishes on that grid. Set
\[
 Z_j=\{x\in\mathbb G_m^n:P(u^a x)=0\text{ for every }a\in\{0,\ldots,jS\}^m\},
 \quad0\leq j\leq n.
\]
The $Z_j$ are nested and nonempty because $1\in Z_n$, and $\dim Z_0\leq n-1$. Some adjacent pair therefore has the same dimension $d$. A $d$-dimensional irreducible component $V$ of $Z_{j+1}$ has the $(S+1)^m$ distinct translates $u^bV$ inside $Z_j$, for $b\in\{0,\ldots,S\}^m$. They are distinct because an equality would make $V$ invariant under a Zariski-dense cyclic subgroup, forcing $V=\mathbb G_m^n$. Each translate is a component of $Z_j$ by dimension. But equations of total degree at most $nD$ have at most $(nD)^n$ irreducible components. For completeness this affine Bézout bound follows by assigning a component $Y$ weight $(nD)^{\dim Y}\deg Y$: imposing a hypersurface never increases total weight, starting from weight $(nD)^n$ on affine space. Restriction to the torus does not increase the number of components. This contradiction proves full rank and supplies a nonzero algebraic-integer $A\times A$ minor $\Delta_D\in E$.

Expand this determinant using the $f_\alpha$. A nonzero term uses $A$ distinct monomials in $r$ variables. Their degree sum is at least $c_rA^{1+1/r}$ for large $A$, since the number of monomials of degree at most $t$ is $\binom{t+r}{r}$. Their values at the chosen $z(a)$ have norm at most one. The ultrametric inequality, first on truncations and then by convergence, gives
\[
 \log|\Delta_D|_\ell\leq-cA^{1+1/r}.
\]
At every archimedean embedding, the entries have logarithmic size $O(DS)$, so
$\log|\tau\Delta_D|\leq C ADS+A\log A$. At every finite place other than the chosen one, algebraic integrality makes the corresponding product-formula term nonpositive. Thus the product formula would imply
\[
 c'[D^{n+n/r}]\leq O(D^{n+1+n/m}+D^n\log D).
\]
This is impossible because
$n/r\geq n/(n-1)>1+n/m$. This proves both the rank lemma and the disputed zero estimate; neither Leopoldt's conjecture nor a conjectural rank is substituted. $\square$

## G.4. Proved: the finite-character separation used in Proposition 4.3

Use the notation of manuscript 031, §4: $P=\operatorname{Gal}(\mathbb Q^{\mathrm{sol}}/\mathbb Q)$; $U\triangleleft G_{\mathbb Q}$ is open; $N\triangleleft U$; $T=N_{G_{\mathbb Q}}(N)$; and $\beta:T\to P$ is the extension whose kernel on $U$ is $N$, with $A=\beta(U)$ open. Let $N_i\ne N$ be the other $G_{\mathbb Q}$-conjugates of $N$, and $H_i=\beta(N_i)$. For every odd $\ell$ and every finite quotient $R_0$ of $P$, there is a totally imaginary finite Galois $L/\mathbb Q$ inside $\mathbb Q^{\mathrm{sol}}$, dominating $R_0$, such that for every proper inclusion $D<C$ of a subgroup into a cyclic subgroup of $R=\operatorname{Gal}(L/\mathbb Q)$ there is
\[
 x\in X_\ell(L)^D,\qquad E_Cx=0,\qquad
 x\notin\sum_i X_\ell(L)^{H_i},
 \quad X_\ell(L)=\operatorname{Hom}_{\mathrm{cont}}(G_L,\mathbb Q_\ell).
\]

**Proof.** Each $H_i$ is nontrivial and normal in $A$. Nontriviality follows because an inclusion $tNt^{-1}\subseteq N$ would, on iteration until a power of $t$ lies in $U$, yield equality, contrary to $t\notin T$. Choose a quotient $R_1$ dominating $R_0$, detecting every $H_i$, with kernel inside $A$ and with field containing $\mathbb Q(i)$. Put $n_1=|R_1|$. Adjoin square roots of $m_1$ collections of conjugate elements with valuation one at one selected prime over a completely split rational prime and valuation zero at the other selected primes. Approximation supplies these elements, and disjoint valuation supports prove independence of their square classes. The resulting solvable extension has kernel
$V\simeq\mathbb F_2[R_1]^{m_1}$, whether or not its group extension splits. Every element of $R$ has order at most $2n_1$. Normality gives $(g_i-1)V\subseteq H_{i,R}$ for a nontrivial image $g_i\in R_1$; hence $|H_{i,R}|\geq2^{m_1n_1/2}$. Conjugation by $V$ gives the same lower bound for the conjugacy-class size of a complex conjugation $c\in R$.

The class-field description embeds $X_\ell(L)$ into the regular representation $\mathbb Q_\ell[R]$ and contains the signed representation $W=\operatorname{Ind}_{\langle c\rangle}^{R}\mathrm{sign}$. Here is why no Leopoldt assumption is hidden: the logarithmic image of global units is only a quotient of their algebraic unit representation; equivariant Dirichlet gives the latter as $\operatorname{Ind}_{\langle c\rangle}^{R}1-1$, so the complementary signed summand survives in the quotient and its dual. Put $\eta=2^{-m_1n_1/2}$. Then
\[
 \dim\sum_i X_\ell(L)^{H_i}\leq r\eta|R|.
\]
The character of $W$ is $|R|/2$ at the identity, $-|R|/(2|c^R|)$ on the conjugacy class of $c$, and zero elsewhere. For every subgroup $J$, its invariant dimension differs from $|R|/(2|J|)$ by at most $\eta|R|/2$. Consequently
\[
 \dim\ker(E_C:W^D\to W^C)
 \geq |R|(1/(4n_1)-\eta).
\]
Choose $m_1$ so that $(r+1)\eta<1/(4n_1)$. This kernel cannot lie in the sum of the $H_i$-invariant spaces and supplies the desired $x$. $\square$

## G.5. Proved: manuscript 031, Proposition 4.3

With the notation of G.4, for any finite quotient $R_0$ of $P$ and any $\gamma_0\in R_0$, one can enlarge to a quotient $R$ and choose a lift $\gamma$ so that infinitely many $\ell$-active source primes have target Frobenius $\gamma$ and source Frobenius image generating $\langle\gamma\rangle$.

**Proof.** We use Uchida (1981, §1 and Proposition 1), whose odd-prime local trichotomy gives an injective nontrivial pro-$\ell$ inertia image in a unique target prime, and cofinite target coverage for this fixed $\ell$. Choose $R$ using G.4. Take an open normal $U'\triangleleft G_{\mathbb Q}$ contained in $U\cap\beta^{-1}(P_L)$, and let $F'/\mathbb Q$ be its fixed field. Chebotarev and Uchida supply infinitely many active source primes $v'$ paired with target primes $w'$ in $L$ having Frobenius $\gamma$. Pass to a subset with distinct source rational primes, unramified in $F'$, and one fixed source Frobenius $\delta\in\operatorname{Gal}(F'/\mathbb Q)$. If $v=v'|_k$, where $T=G_k$, compatible prolongations retain $w'$: the decomposition group at $v'$ is contained in the one at $v$, and uniqueness in Uchida's theorem at the finite field $L$ identifies their target restrictions. Thus the image of $D_v$ in $R$ lies in $C=\langle\gamma\rangle$.

Put $H=T/U'$, and let $f=\min\{j>0:\delta^j\in H\}$. This is the residue degree of $v$ over its rational prime, by the orbit description on cosets; normality of $H$ is not required. Set $d=\beta(\delta^f)$ and $D=\langle d\rangle\subseteq C$. If $D<C$, choose $x$ by G.4 and pull it back to $y\in X_\ell(F')$. The pullback $j:X_\ell(L)\to X_\ell(F')$ is injective because the group image is open. Since $E_Cx=0$ and Frobenius evaluation at $w'$ is $C$-invariant, $x$ vanishes at $w'$, hence on its decomposition group, and $y$ vanishes at all selected $v'$.

The Frobenius-detection consequence of G.3 implies $E_{\langle\delta\rangle}y=0$. For clarity, that consequence follows by class-field reciprocity: a zero value at a degree-one prime annihilates the logarithm of a generator of a power of its ideal. Conjugate generators at distinct unramified rational primes have disjoint ideal supports, satisfying G.3. For prescribed Frobenius $\delta$, average first over $\langle\delta\rangle$, descend to its fixed field, and use the degree-one case. Thus no density assumption on the selected infinite set is used.

In the averaging sum, the powers with $f\mid j$ act trivially on $y$ because $x$ is $D$-invariant. Every other summand is fixed by some $N_i\ne N$. Therefore $y$ lies in the sum of the $N_i$-invariant subspaces of $X_\ell(F')$. The subspace $Y=j(X_\ell(L))$ is stable under the finite group $U/U'$. Characteristic-zero semisimplicity supplies a $U$-equivariant projection $X_\ell(F')\to Y$. Each $N_i$ is contained in $U$, so the projection carries its invariant space into $Y^{N_i}=j(X_\ell(L)^{H_i})$. Pulling back gives the forbidden inclusion $x\in\sum_iX_\ell(L)^{H_i}$. Thus $D=C$, proving the proposition. The proof needs only $U$-equivariance; it never assumes $T$ normal in $G_{\mathbb Q}$. $\square$

## G.6. Proved: manuscript 031, Proposition 5.3, with a bound independent of the auxiliary prime

In manuscript 031, §5, let $\beta_B:G_K\twoheadrightarrow P_B$ be the established surjection, with $B=\mathbb Q(i)$, and assume its cyclotomic discrepancy at the odd prime $\ell$ is the finite character $\epsilon=(\chi_\ell\circ\beta_B)\chi_{K,\ell}^{-1}$. Let $M_\ell$ be the primes of $B$ missed by the active-prime correspondence. Then
\[
 \#\{w\in M_\ell:w\nmid\ell\}\leq2[K:\mathbb Q],
 \qquad \#M_\ell\leq2[K:\mathbb Q]+2.
\]

**Proof.** Choose finitely many distinct missed primes $J$ away from $\ell$. For each choose $a_w$ whose principal ideal is a positive power of $w$. Their Kummer classes in $H^1(P_B,\mathbb Q_\ell(1))$ are independent by the valuations at the different $w$. Pullback along the surjection is injective by inflation. Let $K'/K$ be the cyclic extension killing $\epsilon$, with $\Delta=\operatorname{Gal}(K'/K)$. Restriction to $G_{K'}$ is injective because finite-group $H^1$ vanishes in characteristic zero. The resulting independent classes lie in the $\epsilon^{-1}$-eigenspace of $H^1(G_{K'},\mathbb Q_\ell(1))$.

They are unramified away from $\ell$. Indeed, ramification at $u\nmid\ell$ would detect a nonzero pro-$\ell$ inertia image at the underlying prime $v$ of $K$. Uchida's local theorem sends that Sylow inertia into inertia at an active target prime $t\notin J$. The original Kummer class is unramified at $t$ and its cocycle is zero on its inertia (the Tate coefficient is unramified there), contradicting its nonzero pullback at $u$.

For $S$ the archimedean places and the places above $\ell$, unramified Kummer theory identifies these classes with $\mathcal O_{K',S}^{\times}\otimes\mathbb Q_\ell$. One must use the completion correctly: at finite level, outside-$S$ divisors divisible by $\ell^a$ have an obstruction in $\mathrm{Cl}_S(K')[\ell^a]$, and the transition on these obstructions is multiplication by $\ell$. Their inverse limit is zero because the class group is finite. This proves the stated $S$-unit identification without asserting finite valuation support for an arbitrary completed multiplicative element.

Equivariant Dirichlet gives the character
\[
 [\mathcal O_{K',S}^{\times}\otimes\mathbb Q_\ell]
 =[\mathbb Q_\ell[S]]-[\mathbb Q_\ell].
\]
Each $\Delta$-orbit contributes at most one copy of the specified one-dimensional character $\epsilon^{-1}$, by Frobenius reciprocity from its stabilizer. The number of orbits is
\[
 r_1(K)+r_2(K)+\#\{v\mid\ell\}\leq2[K:\mathbb Q].
\]
Subtracting the trivial representation cannot increase the multiplicity. Hence $|J|$ has the asserted bound, independently of $[K':K]$ and $\ell$. Letting $J$ vary gives the first inequality; $B=\mathbb Q(i)$ has at most two primes above $\ell$, giving the second. This proves the requested uniform step. $\square$

## G.7. Proved: the immediate global consequences of the verified 031 steps

In the notation of G.4, the normalizer extension $\beta:G_k\to P$ is surjective. Put
\[
 m_0=[k:\mathbb Q]!,\qquad
 \mathcal L=\{\ell:\ell\text{ is odd prime and }\ell\equiv1\pmod{m_0}\}.
\]
For every $\ell\in\mathcal L$,
\[
 \log\chi_\ell\circ\beta=\log\chi_{k,\ell}.
 \tag{G.1}
\]
Equivalently, the discrepancy of the two $\ell$-adic cyclotomic characters is a finite character with values in $\mu_{\ell-1}$. This proves manuscript 031, Theorem 4.4, from the independently established inputs above, and supplies the exact hypothesis used in G.6.

**Proof.** First, the normalizer extension used in G.4 exists without a surjectivity assumption on the initial map. For an open $\alpha_0:G_F\to P$, choose $U\triangleleft G_{\mathbb Q}$ open inside $G_F$, and put $A=\alpha_0(U)$ and $N=\ker(\alpha_0|_U)$. Every $t\in T=N_{G_{\mathbb Q}}(N)$ induces an automorphism of $U/N=A$. Uchida (1979, main theorem) gives its unique implementing field automorphism of $\mathbb Q^{\mathrm{sol}}$. It fixes $\mathbb Q$, hence is an element $\beta(t)\in P$. Uniqueness proves multiplication and agreement with $\alpha_0$ on $U$; continuity follows from continuity on this open subgroup. Its image contains the open subgroup $A$. For any finite quotient $R_0$ of $P$ and any $\gamma_0\in R_0$, G.5 supplies a further quotient $R$ and a lift $\gamma$ such that $\langle\gamma\rangle$ is generated by a Frobenius image under $\beta$. Hence $\gamma$, and therefore $\gamma_0$, lies in the image. Compactness of $\beta(G_k)$ proves surjectivity.

We recall the precise tame-inertia identity needed next. For an active pair $(v,w)$ at $\ell$, let $b(g),a(g)\in\widehat{\mathbb Z}$ be the source and target residue exponents of $g\in D_v$ and $\beta(g)\in D_w$. Then
\[
 (Nv)^{b(g)}=(Nw)^{a(g)}\quad\text{in }\mathbb Z_\ell^{\times}.
 \tag{G.2}
\]
Choose a generator $\tau$ of a pro-$\ell$ Sylow of source inertia. The source tame relation makes $g\tau g^{-1}\tau^{-(Nv)^{b(g)}}$ belong to wild inertia, a pro-$p$ group with $p\ne\ell$. In the target tame quotient its image belongs to the pro-$\ell$ factor, because the two occurrences of $\tau$ do. It is therefore trivial. Uchida's odd-prime local result (1981, \S1, pp. 595--596) makes the target image of $\tau$ nontrivial in its torsion-free pro-$\ell$ tame inertia, so comparing the target conjugation relation gives (G.2). This uses no assertion that every part of source inertia is sent into target inertia.

Dirichlet's theorem makes $\mathcal L$ infinite. Fix $\ell\in\mathcal L$, and apply G.5 with $R_0=\operatorname{Gal}(\mathbb Q(\mu_\ell)/\mathbb Q)=\mathbb F_\ell^{\times}$ and a generator $\gamma_0$. It gives infinitely many active source primes $v$, over distinct rational primes $p\ne\ell$, such that the image of a Frobenius lift generates $\mathbb F_\ell^{\times}$. Put $Nv=p^f$. Relation (G.2) says that $p^f$ also generates $\mathbb F_\ell^{\times}$, so $\gcd(f,\ell-1)=1$. But $1\leq f\leq[k:\mathbb Q]$, and every prime divisor of an integer $f>1$ in that range divides $m_0$, hence $\ell-1$. Therefore $f=1$. Taking logarithms in (G.2) shows that $\log\chi_\ell\circ\beta-\log\chi_{k,\ell}$ vanishes at these infinitely many degree-one primes. The Frobenius-detection consequence of G.3, proved in G.5, makes this additive character zero. Finally, the kernel of the logarithm on $\mathbb Z_\ell^{\times}$ for odd $\ell$ is $\mu_{\ell-1}$, proving the last assertion. $\square$

**Scope of the manuscript audit.** The exact requested 019 and 031 propositions are proved in G.2, G.3, G.5, and G.6; no gap was found in them. G.7 records an additional implication with its proof. The full proper local section theorem and specified-completion inclusion of 019, Theorems 1.1--1.2, and the unrestricted open-Hom theorem of 031, Theorem 1.1, are claims of the supplied manuscripts, not automatically certified by this targeted audit. To turn the present text into a self-contained proof of those full claims one must also reproduce, respectively, 019's collar-to-global patching and descent chain, and 031's finite-partner argument, simultaneous Kummer separation, and compactness identification, followed by Hoshi (2025, Theorem 3.4). We read the final 031 reduction and the primary Hoshi theorem; for 019 we inspected the final use of Proposition 5.2 and its decomposition-group consequence. We do not call a step a mathematical gap merely because its independent proof is outside the designated obligations. In particular, this scope qualification is not a new row asserting that either full statement is false or mathematically open.

The independent computations in `code/dg_checks.py` verify the elementary Heisenberg counterexample, the six-function rigidity check, the strict exponent inequalities used in G.3, and the cyclic-character multiplicity bound used in G.6. The nonarchimedean analytic arguments and infinite Galois assertions are proved above, not certified by those finite checks.
