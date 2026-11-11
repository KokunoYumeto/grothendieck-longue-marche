# Conventions and scope

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).** Prepared on 11 November 2026 from the attached manuscript, prior response, review, and primary sources. We claim no priority. “Proved” means that the exact assertion has a proof in this paper, using the cited external theorems where specified. “Known” means that we derive the requested formulation from a named theorem. “Refuted” applies to the assertion expressly negated, in the completion specified. “Open” means that the exact obligation remains unresolved in this work; the text distinguishes a recognized open problem from an incomplete comparison in this audit.

We fix the principal manuscript notation before making any comparison. New auxiliary letters in a proof are declared there and do not claim a manuscript counterpart. An unadorned surface group in an assertion about profinite automorphisms is fully profinite; a pro-prime group always carries the superscript or the explicit qualification “pro-$\ell$.” The bracket grading in the computations is the ordinary lower-central grading.

| Our notation | Grothendieck's notation; introducing scan | Meaning |
|:---|:---|:---|
| $(g,n)$ | $(g,\nu)$; 204–205 | Genus and number of punctures; hyperbolic means $2g-2+n>0$. |
| $\Pi_{g,n}$, $\widehat\pi_{g,n}$ | $\Pi_{g,\nu}$, $\widehat\Pi_{g,\nu}$; 221, 328 | Discrete surface group and full profinite completion, with peripheral classes. |
| $\Gamma_{g,n}$, $P\Gamma_{g,n}$ | $\mathcal T^+$, $\mathcal T^{!+}$; 226, 323, 328 | Orientation-preserving mapping class group, respectively its pure subgroup. |
| $O_{g,n}$ | $\widehat{\widehat{\mathcal T}}$; 321–324 | Continuous loop-preserving outer automorphisms, with a common peripheral unit multiplier. The double hat is not iterated completion. |
| $\Sigma_{g,n}$ | $\widehat{\mathcal T}^{+}=\Sigma$; 323–324 | Geometric image, the closure of the orientation-preserving mapping class action; it need not be its abstract profinite completion. |
| $\Gamma^{\mathrm{norm}}_{g,n}$ | $\mathcal N_\Sigma/\Sigma=\Gamma_\Sigma$; 324–326 | The normalizer quotient of §26. |
| $\Gamma^{\mathrm{arith}}_{g,n}$ | $N_{g,\nu}/\Sigma$; 370–371 | The arithmetic-image quotient of §29. |
| $G_K$, $\chi_K$ or $\lambda$ | $\mathbb I\Gamma_K$, $\chi$; 327, 323 | Absolute Galois group and cyclotomic character, or the ambient peripheral multiplier. |
| $\mathcal M_{g,[n]}$ | $M_{g,\nu}$; 326–329 | The moduli **stack** with an unordered puncture divisor; $\mathcal M_{g,n}$ retains labels. |
| $f_i$, $\theta_i$ | The filling maps (1)–(2); 348–349, 367–368 | Outer filling and its genuine target action after selecting filled-cusp inertia. |
| $\mathfrak s_r$, $V_n$, $W_n$, $C_n$ | No corresponding fixed symbol | Special outer derivations, the two equation spaces of F, and the exit category of H. |

All homomorphisms of profinite groups are continuous; all subgroup closures, kernels, and quotient topologies are understood. A morphism “outer” to a group $H$ is taken modulo conjugation by $H$, unless a smaller conjugating group is named. Geometric base-point changes induce that stated inner ambiguity. We distinguish a mapping class group's full completion from its image in the automorphism group of a completed surface group. The latter is the procongruence group.

# What the numbered results settle

The full profinite filling sequence marked “??” fails at $(0,4)\to(0,3)$: B.5 constructs an element of its kernel outside point-pushing. The map is nevertheless onto, by B.4. B.6 identifies the exact replacement on the normalizer of the point-pushing subgroup. This also refutes full profinite normality of the geometric subgroup at $(0,4)$, by A.6. These conclusions do not depend on lifting an arbitrary pro-prime automorphism to a free profinite group.

The finite pro-$2$ covering certificate C.5 refutes the requested normalizer-times-geometric factorization for the degree-two tripod cover; C.10 transfers the obstruction to the characteristic Klein-four cover. D.3 proves uniqueness of a whole Galois-invariant loop structure for every affine hyperbolic type over a number field. H.8 proves the first strict-category versus profinite-stratified comparison, at $\overline{\mathcal M}_{0,4}$. The full profinite tripod normality and GT strictness questions, the unrestricted elliptic inertia comparison, and genus-three congruence are kept separate from these results.

The following table is a guide to the earlier open rows, not an additional set of unnumbered theorems.

| Earlier row | Conclusion in this paper | Numbered results |
|:---|:---|:---|
| LM3 B.7: normality | Counterexamples in all three requested pro-prime types and in the full profinite four-puncture case; exact remaining tripod lifting problem. | A.1–A.16 |
| LM3 C.8: filling | Full profinite sequence false in the middle; surjectivity and repaired normalizer sequence proved; the all-degree kernel presentation remains open. | B.1–B.11 |
| LM3 B.14: coverings | Geometric descent/injectivity established for the test covers; both pro-$2$ surjectivity claims refuted; remaining comparisons isolated. | C.1–C.10 |
| LM3 D.23: loops | Whole invariant loop structures unique; bare maximal-procyclic criterion remains stronger. | D.1–D.5 |
| LM3 D.23: admissible splittings | Localized-tower and AA characterizations derived; equality for an explicitly arithmetically marked section family. | D.6–D.14 |
| LM3 E.14, F.16: elliptic types | Precise automatic-inertia and clutching-coherence obligations; open-arrow 2-group and boundary modification group computed; modular-topos comparison derived. | E.1–E.9 |
| LM3 E.8: Galois and GT | Pro-$\ell$ two-relation strictness for $\ell\geq5$; full profinite comparison remains unresolved; abelian and characteristic class-two finite families settled. | F.1–F.13 |
| LM3 B.3: congruence | Exact centralizer criterion and an explicit finite representation beyond base homology; no genus-three solution. | H.1–H.5 |
| LM3 F.18: higher completion | Affirmative comparison at $n=4$; a precise chain-comparison condition for larger $n$. | H.6–H.9 |
| LM3 D.7, D.13, E.26: manuscripts | Requested steps of 019, 031, and 008 rederived; independent direct pentagon calculation and all-weight upper-bound reduction. | G.1–G.11; F.2 |

The primary-source theorem numbers below refer to the actual versions opened. A bibliography entry marked **verified** means that the source was opened and the cited locus inspected; it is not a claim that every theorem in that source was independently reproved. In particular, the 2026 manuscripts retain their manuscript status. We verify the obligations named in G and do not certify every assertion of 019 or 031.

# Manuscript loci and exceptional types

We use section, manuscript folio, and scan together. Where the transcription also supplies a running number at the bottom of a verso, the folio reference follows the surrounding recto/verso sequence; the scan is the unambiguous locator. The folio alternative on scan 328 is retained. Statements about the new computational leads, or about the 2026 manuscripts, are auxiliary to the indicated passage and have no verbatim 1981 counterpart. The result register records that distinction. The reading register separates mathematical support for an alternative from a palaeographic decision.

The quoted sentence “Ce n'est pas la peine” is treated as the conjectural sentence about a whole loop structure, followed by a distinct proposed test for individual subgroups. We also retain the question marks on the filling sequence and the subsequent correction on scans 367–370. A withdrawn assertion is not restored as a theorem.

The nonhyperbolic types excluded from the principal assertions must be treated separately. For $(0,0)$ and $(0,1)$ the geometric group is trivial; its outer automorphisms cannot detect arithmetic. For $(0,2)$ it is $\widehat{\mathbb Z}$, and for $(1,0)$ it is $\widehat{\mathbb Z}^{\,2}$. Their nontrivial centers invalidate the center-free extension arguments in B and D. These elementary identifications follow from the sphere, punctured sphere, cylinder, and torus presentations. Thus none of the hyperbolic recognition statements is extended to them by deleting a hypothesis.

The profinite surface groups of the hyperbolic types used below are center-free, including the tripod and once-punctured torus. Mapping class groups may still have centers, especially the order-two elliptic center; E treats that distinction explicitly. The integral lifting and determinant proofs include primes two and three. Coprime fixed-point lifting in F.3 explicitly excludes them. All surfaces in the mapping class arguments are oriented, and orientation-reversing maps are included only where the extended geometric group is specified. Real arithmetic, when used as a subgroup generated by complex conjugation, is not replaced by the finite-index number-field Galois group in the recognition arguments; nonorientable surfaces and real section problems are not claimed as consequences.



\clearpage
\tableofcontents
\clearpage

# A. Normality, integral lifting, and the orbit of a geometric subgroup

We use the ordinary closed lower central series $\gamma_1F=F$, $\gamma_{m+1}F=\overline{[F,\gamma_mF]}$. It is not the Zassenhaus filtration. For a prime $\ell$, write $F_r^{(\ell)}$ for the free pro-$\ell$ group on $x_1,\ldots,x_r$, put $P=x_1\cdots x_r$, and distinguish the conjugacy classes of $\langle x_1\rangle,\ldots,\langle x_r\rangle,\langle P\rangle$. A special automorphism preserves the conjugacy class of each displayed generator, with exponent one. We write $\mathfrak s_r$ for its graded outer derivation algebra over a characteristic-zero field. The filtration degree of $D(x_i)=[a_i,x_i]$ is $\deg a_i$, not $\deg D(x_i)$. The geometric subgroup is always the image of the orientation-preserving mapping class group in the indicated outer automorphism group.

## A.1. Proved — Integral lifting of special derivations (Lead 1)

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


Every homogeneous special derivation over $\mathbb Z_\ell$ of positive degree is the leading term of a special automorphism of $F_r^{(\ell)}$. This holds also for $\ell=2,3$. If the derivation induces zero on the quotient killing $x_1$, it can be lifted to an automorphism inducing the identity on that quotient. If its normalized conjugators all belong to the Lie ideal $(x_1)$, the lift can moreover be chosen in the kernel of the genuine based filling map $\theta_1$.

*Proof.* The canonical graded Lie algebra of $F_r^{(\ell)}$ is the free $\mathbb Z_\ell$-Lie algebra $L$ on the classes of the $x_i$ (Koch, Kukkuk, & Labute, 1998, Theorem 2.1). The surjection

$$
\delta_m:\bigoplus_{i=0}^r L_{m-1}\longrightarrow L_m,
\qquad (b_i)\longmapsto\sum_{i=1}^r[b_i,x_i]-[b_0,x_1+\cdots+x_r]
$$

is integral: already the terms with $i\geq1$ span $L_m$. To see this without a dimension argument, apply Jacobi repeatedly to write every bracket word as a sum of left-associated bracket words; each ends in a generator. Thus no division by a weight or by a prime is involved.

Let $D(x_i)=[a_i,x_i]$ and $D(S)=[a_0,S]$, where $S=\sum x_i$ and all $a_i$ have degree $n$. Lift $a_i$ to $A_i\in\gamma_nF$. The error between $\prod A_ix_iA_i^{-1}$ and $A_0PA_0^{-1}$ belongs to $\gamma_{n+2}F$. Suppose it belongs to $\gamma_mF$. Multiplying the $A_i$ by elements $B_i\in\gamma_{m-1}F$ changes its degree-$m$ class by $\delta_m(b_i)$, up to the harmless common choice of sign for the error. Surjectivity allows us to kill that class. Proceed inductively.

The corrections converge in the actual pro-$\ell$ group. Indeed, in every finite continuous quotient of $F$, which is a finite $\ell$-group, sufficiently long commutators vanish. Consequently $\gamma_mF$ is eventually contained in every prescribed open normal subgroup. The convergent conjugators give an exact equality of the two products, not just an equality in a rational Lie algebra. The map sending $x_i$ to the resulting conjugates is a continuous endomorphism inducing the identity on $F/\Phi(F)$. The pro-$\ell$ Burnside basis theorem makes it surjective, and a surjective endomorphism of a finitely generated profinite group is injective. Its leading term is unchanged.

For the relative assertion put $N=\overline{\langle x_1\rangle}^{\rm normal}$ and $I=(x_1)\subset L$. The retraction killing $x_1$ shows that the graded subgroup of $N$ is exactly $I$. Jacobi gives

$$
 I_m=[L_{m-1},x_1]+\sum_{i\ne1}[I_{m-1},x_i].
$$

Thus corrections can be taken with $B_0,B_i\in N$ for $i\ne1$, and $B_1$ unrestricted. A derivation whose filled outer class is zero can first be changed by an inner derivation so that its filled genuine derivation is zero. In degree at least two, the centralizer of a free generator in $L$ then forces the corresponding conjugators $a_i$ for $i\ne1$, and $a_0$, to lie in $I$. Degree one is handled by subtracting the scalar multiples of the individual generators, which do not change the derivation. The corrected automorphism therefore induces the identity after filling.

For the strengthened assertion, normalize $a_0=0$ by subtracting an inner derivation and suppose all $a_i\in I$. In fact

$$
 I_m=\sum_{i=1}^r[I_{m-1},x_i].
$$

For a proof, $I$ is the adjoint module generated by $x_1$; the universal enveloping algebra of the free Lie algebra is the tensor algebra on its generators. Its degree-$m$ part is therefore spanned by iterated adjoints of $m-1$ generators applied to $x_1$. We may keep $A_0=1$ and all the $A_i$ in $N$ throughout the correction. The resulting automorphism fixes $P$, induces the identity on $F/N$, and its conjugator at $x_1$ belongs to $N$. Conjugating it to fix $x_1$ therefore changes nothing on $F/N$. This is precisely membership in $\ker\theta_1$. All arguments are integral. $\square$

The lifting just proved concerns conjugacy-preserving automorphisms of a free pro-$\ell$ group. It does not assert that an arbitrary such automorphism is induced from the free profinite group. The difference is essential in A.4.

## A.2. Proved — The complete $S_3$ character through weight 12

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


For $n\geq2$, the rational $S_3$-module of special outer derivations of the tripod has character

$$
 [\mathfrak s_{2,n}]=[V\otimes L_n(V)]-[L_{n+1}(V)],
$$

where $V$ is the two-dimensional standard representation. The dimension is $2\ell_n(2)-\ell_{n+1}(2)$, where

$$
 \ell_n(r)=\frac1n\sum_{d\mid n}\mu(d)r^{n/d}.
$$

The degree-one outer space is zero. In the following table, the final column is the multiplicity of the two-dimensional standard representation, not its contribution to total dimension.

| Degree | Total dimension | Trivial | Sign | Standard multiplicity |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 |
| 3 | 1 | 1 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 |
| 5 | 3 | 1 | 0 | 1 |
| 6 | 0 | 0 | 0 | 0 |
| 7 | 6 | 2 | 0 | 2 |
| 8 | 4 | 1 | 1 | 1 |
| 9 | 13 | 4 | 1 | 4 |
| 10 | 12 | 2 | 2 | 4 |
| 11 | 37 | 9 | 4 | 12 |
| 12 | 40 | 7 | 7 | 13 |

*Proof and computation.* The three peripheral conjugators form $\mathbb Q^3\otimes L_n(V)$. The special relation maps this module surjectively onto $L_{n+1}(V)$. For $n\geq2$, individual generator centralizers contribute no kernel; quotienting by inner derivations subtracts $L_n(V)$. Since $\mathbb Q^3-\mathbb Q=V$ in the representation ring, the stated formula follows. In degree one the three scalar generator-centralizer directions must also be subtracted; the result is zero.

We evaluate the free-Lie character by the exact Witt character formula

$$
 \operatorname{tr}(g\mid L_n(V))
 =\frac1n\sum_{d\mid n}\mu(d)\operatorname{tr}(g^d\mid V)^{n/d}.
$$

The traces of the identity, a transposition, and a three-cycle on $V$ are $2,0,-1$. Taking inner products with the three character rows of $S_3$ gives the table. The program `code/ab_lie.py` independently constructs Lyndon words and bracket expansions; it uses the displayed exact integer character formula for this table and exact rational matrices for the filling and normalizer tables below. Its complete machine-readable output is `code/ab_lie_results.json`. No review program is imported. $\square$

## A.3. Refuted — Pro-$\ell$ normality of the geometric tripod group (Lead 2)

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


For every prime $\ell$, the geometric $S_3$ is not normal in $O_{0,3}^{(\ell)}=\operatorname{Out}_{\rm lac}(F_2^{(\ell)})$. Consequently $N_O(S_3)\ne O$ and there is more than one strict geometric subgroup. This answers the pro-$\ell$ versions of §26, folios 163–165, scans 322–326.

*Proof.* The degree-five space of A.2 contains a standard summand. Choose an integral special derivation with non-invariant outer class; clearing denominators in a rational basis suffices, and a nonzero integral class remains nonzero over every $\mathbb Z_\ell$. One explicit choice, checked by `code/ab_weight5_witness.py`, is

$$
 a_x=[x,[x,[[x,y],y]]]-2[[x,[x,y]],[x,y]],\qquad
 a_y=[x,[x,[x,[x,y]]]],
$$

with $D(x)=[a_x,x]$ and $D(y)=[a_y,y]$. Its sum is zero and transposition changes the derivation. The complete integral coordinates are also recorded in `code/ab_weight5_witness.json`. By A.1 it lifts to a special automorphism $a$. If $a$ centralized $S_3$ in the outer group, its leading class would be invariant, a contradiction. The special subgroup is the kernel of the cusp-permutation and multiplier maps, hence is normal in $O$, and its intersection with the geometric $S_3$ is trivial because the latter acts faithfully on cusp labels. If $S_3$ were normal in $O$, its commutator with a label-preserving element would lie in this trivial intersection. This proves nonnormality. We did not average an integral lattice by $1/6$, so the proof includes $\ell=2,3$. $\square$

## A.4. Open — The remaining profinite tripod lifting problem

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


We do not decide whether $S_3\triangleleft\operatorname{Out}_{\rm lac}(\widehat F_2)$, or whether the image of its label-preserving subgroup in $\operatorname{Out}(F_2^{(\ell)})$ centralizes $S_3$ for every $\ell$. The exact missing assertion is the realization, by a special automorphism of $\widehat F_2$, of a pro-$\ell$ outer class having a non-invariant degree-five leading term.

*Attack and obstruction.* The quotient to the maximal pronilpotent group gives

$$
 \widehat F_2\twoheadrightarrow\prod_\ell F_2^{(\ell)}.
$$

A.1 constructs special automorphisms on the factors. Lifting their conjugators to $\widehat F_2$ preserves the first two peripheral classes, but the product relation may still have an error in the kernel of the displayed quotient. Repeating the lower-central correction only kills its image in every nilpotent quotient; it does not kill this remaining error in nonnilpotent finite quotients. Projectivity of a free profinite group lifts homomorphisms, not the simultaneous peripheral equations together with invertibility. Thus it does not supply the missing special automorphism. The smallest unclosed instance remains the tripod itself, already the degree-five non-invariant class at one prime. By contrast, the four-puncture profinite normality assertion is refuted in A.6.

## A.5. Proved — Four-puncture normalizer calculations through degree six

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


Put $x=x_1,y=x_2,z=x_3$. Let $\mathfrak p$ be the Lie subalgebra generated by

$$
 u=([y,x],[x,y],0),\qquad v=([z,x],0,[x,z]),
$$

where a tuple lists a derivation's values on $x,y,z$. It is the graded point-pushing Lie algebra, freely generated by $u,v$. Its normalizer inside $\mathfrak s_3$ has the following homogeneous dimensions.

| Degree | $\mathfrak s_3$ | $\mathfrak p$ | $N_{\mathfrak s_3}(\mathfrak p)$ | Normalizer modulo $\mathfrak p$ |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 |
| 2 | 1 | 1 | 1 | 0 |
| 3 | 6 | 2 | 3 | 1 |
| 4 | 6 | 3 | 3 | 0 |
| 5 | 28 | 6 | 7 | 1 |
| 6 | 36 | 9 | 9 | 0 |

*Proof and certification.* Subtracting an inner derivation gives the gauge $D(x+y+z)=0$. In degree at least two it is unique because the centralizer of $x+y+z$ has only degree one. We solve

$$
 \sum_{i=1}^3[a_i,x_i]=0
$$

in the Lyndon basis, and use the induced derivations as columns. Degree one additionally quotients by $\operatorname{ad}(x+y+z)$. The two generator brackets $[D,u]$ and $[D,v]$ must belong to $\mathfrak p_{n+1}$; these conditions are necessary and sufficient because $\mathfrak p$ is generated by $u,v$ and the derivation identity then handles every bracket word. The program forms these two exact matrices, eliminates their components in $\mathfrak p_{n+1}$, and computes the joint rational nullspace. All ranks are exact.

Freeness of $\mathfrak p$ can also be checked conceptually: the graded based filling map sends it isomorphically onto the inner derivations of the free Lie algebra $L(y,z)$. The free Lie algebra is center-free, so this is an injection in every degree.

The last column is canonically $\mathfrak{grt}_1$ through degree six, not only equal in dimension. Here is the needed comparison. The infinitesimal parenthesized braid action justified in F.10 preserves the configuration exact sequence

$$
 0\longrightarrow L_3\longrightarrow
 \mathfrak t_4/Z(\mathfrak t_4)\longrightarrow
 \mathfrak t_3/Z(\mathfrak t_3)\simeq L_2\longrightarrow0.
$$

Its restriction to $L_3$ preserves the peripheral classes and distinguished diagonal cusp. If $d$ is the induced derivation of the middle Lie algebra and $q\in L_2$, the derivation identity gives, in outer derivations of the fiber,

$$
 [d|_{L_3},\rho(q)]=\rho(\bar d(q)),
$$

where $\rho$ is point-pushing and $\bar d$ is the induced quotient derivation. Hence fiber restriction lies in $N_{\mathfrak s_3}(\mathfrak p)$. Changing a base-point representative by an inner derivation of the middle algebra changes fiber restriction by point-pushing, so it defines a canonical Lie homomorphism

$$
 \mathfrak{grt}_1\longrightarrow N_{\mathfrak s_3}(\mathfrak p)/\mathfrak p.
$$

This map is injective. If the fiber restriction belongs to point-pushing modulo inner fiber derivations, subtract the corresponding inner derivation of the middle algebra. The resulting derivation vanishes on $L_3$. For every middle element $e$ and fiber element $f$, the derivation identity then gives $[d(e),f]=0$. The centralizer of $L_3$ in the middle algebra is zero: projecting such a centralizing element to $L_2$ would give an inner point-pushing action, contrary to the already proved faithful outer monodromy; the remaining element lies in the center of the free Lie algebra $L_3$, which is zero. Thus the middle derivation vanishes, and so does its action on the quotient tripod. F.1 identifies that action with the original defining polynomial of $\mathfrak{grt}_1$, up to the fixed harmless sign convention. The original element is therefore zero.

The dimensions in F.2 are $0,0,1,0,1,0$ in degrees one through six. The injective canonical map and our exact normalizer dimensions make it an isomorphism in those degrees, compatible with all brackets whose total degree stays in this range. No equality in uncomputed degrees is inferred. $\square$

## A.6. Refuted — The geometric four-puncture subgroup is normal, in either completion

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


The subgroup $\Sigma_{0,4}$ is not normal in the full profinite group $O_{0,4}$; likewise its pro-$\ell$ image is not normal for any $\ell$.

*Proof.* For the pro-$\ell$ assertion the explicit derivation in B.3 lies in $\ker\theta_x$ and its bracket with $v$ is nonzero. If its lift normalized the geometric subgroup, it would normalize the point-pushing subgroup, which is the intersection of the geometric cusp stabilizer with the filling kernel. Since $\theta_x$ is injective on point-pushing, a normalizing element in $\ker\theta_x$ would centralize point-pushing. The nonzero leading bracket contradicts this.

For the full profinite assertion use the element $b$ of B.5. It preserves every cusp label, fills to the identity, and does not belong to the geometric subgroup. If it normalized $\Sigma_{0,4}$, it would normalize its stabilizer of the distinguished cusp, and then the subgroup $K=\Sigma_{0,4,x}\cap\ker f_x$ of point-pushing. By B.6 the kernel of filling on this normalizer is exactly $K$. This would force $b\in K$, contradicting B.5. $\square$

## A.7. Proved — The elliptic ambient calculation

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


For the positive-degree outer derivations of $L(a,b)$ preserving the conjugacy class of $\omega=[a,b]$, the dimensions are

$$
 e_n=2\ell_{n+1}(2)-\ell_{n+2}(2)-\delta_{n,2}.
$$

For degrees $1$ through $12$ they are

$$
 0,0,0,3,0,6,4,13,12,37,40,99.
$$

*Proof.* After subtracting an inner derivation, the condition is $D(\omega)=0$. The linear map

$$
 L_{n+1}^{\oplus2}\longrightarrow L_{n+2},\qquad
 (u,v)\longmapsto[u,b]+[a,v]
$$

is onto because brackets with $a,b$ span $L_{n+2}$. Its kernel has dimension $2\ell_{n+1}-\ell_{n+2}$. An inner derivation preserving $\omega$ comes from its free-Lie centralizer, the line spanned by $\omega$; hence precisely one further dimension is removed in degree two. The formula is evaluated independently in `code/ab_kernel.py`. $\square$

## A.8. Known — The elliptic geometric Lie image through degree twelve, with independently computed consequences

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


Fix a rational symplectic basis $a,b$ of first homology and use the weight-graded monodromy representation of the relative completion of $SL_2(\mathbb Z)$. Its image is $\mathfrak{sl}_2\ltimes\mathfrak u$, where the positive outer image $\mathfrak u$ is the Lie algebra generated by the $SL_2$-orbits of the boundary-preserving derivations $\epsilon_{2m}$, $m\geq2$. Its dimensions are

| Degree | Ambient outer derivations | Geometric positive image $\mathfrak u_n$ |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 0 | 0 |
| 3 | 0 | 0 |
| 4 | 3 | 3 |
| 5 | 0 | 0 |
| 6 | 6 | 5 |
| 7 | 4 | 0 |
| 8 | 13 | 10 |
| 9 | 12 | 0 |
| 10 | 37 | 24 |
| 11 | 40 | 0 |
| 12 | 99 | 50 |

*Reduction and computation.* Hain and Matsumoto (2020), Theorem 10.7, identify the relative-completion monodromy image with their geometric elliptic motivic group. Proposition 20.1 and Corollary 20.2 give its generators, and Theorem 22.3 and Corollary 23.3 identify their derivation images as nonzero rational multiples of $\epsilon_{2m}$. Section 22 identifies the weight-graded fundamental Lie algebra with $L(a,b)$; its $W$-weight $-j$ is bracket length $j$. Thus $\epsilon_{2m}$ has the ordinary derivation degree $2m$ used here. This comparison uses $W$, not the different relative weight filtration $M$. The tangent-vector generator $\epsilon_2=\operatorname{ad}[a,b]$ is inner and disappears from the outer image, as explained in their Remark 22.2.

For complete reproducibility put $B_j=\operatorname{ad}_a^j(b)$. In the normalization of their equation (22.3),

$$
 \epsilon_{2m}(a)=-B_{2m},\qquad
 \epsilon_{2m}(b)=[B_{2m-1},b]
 -\sum_{\substack{j+k=2m-1\\j>k>0}}(-1)^j[B_j,B_k].
$$

The code checks directly that each derivation kills $[a,b]$. Bracketing repeatedly with the degree-zero lowering derivation $a\mapsto b$, $b\mapsto0$ produces its $2m-1$ independent $SL_2$-orbit vectors. In degree $n$, we take the span of this orbit, when present, and all brackets of the already computed lower-degree geometric spaces. Exact rational elimination in the integral Lyndon basis gives the displayed dimensions. This recursion is complete because the cited generators generate the image; it does not assume a conjectural presentation of their relations. The program is `code/ab_elliptic.py`; the formulas, exact outputs, and an additional independent degree-fourteen computation are retained with the code.

In particular, the first geometric space is all of the degree-four ambient $\operatorname{Sym}^2$ representation. In degree six the geometric space is $\operatorname{Sym}^4$, and the ambient space has one additional trivial representation. All odd geometric degrees vanish. These assertions concern the actual graded relative-completion image; the pro-$\ell$ group normality question is separately decided in A.14. $\square$

## A.9. Proved — The pro-$\ell$ orbit space is a profinite homogeneous space, and is a Cantor space in the three computed types

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


For a closed geometric subgroup $\Sigma\subset O$, the set of its conjugates is canonically $O/N_O(\Sigma)$ with its compact quotient topology. For the pro-$\ell$ types $(0,3)$, $(0,4)$, and $(1,1)$ this space is infinite, metrizable, and has no isolated points; hence it is homeomorphic to a Cantor space. It contains a closed copy of $\mathbb Z_\ell$.

*Proof.* The normalizer is closed, so the quotient of the profinite group is compact and zero-dimensional. The automorphism group of a finitely generated pro-$\ell$ group is metrizable: characteristic open subgroups of finite index form a countable cofinal family. In the tripod case choose the lift $a$ in A.3. The powers $a^t$, $t\in\mathbb Z_\ell$, exist in the pro-$\ell$ special subgroup; their leading classes are $tD$. If two powers determine the same conjugate of $S_3$, their quotient normalizes $S_3$, hence centralizes it because it preserves labels. Its non-invariant leading class forces $t=s$. This gives a continuous injection of $\mathbb Z_\ell$ into the quotient, therefore a closed embedding. For four punctures use the lift in B.3 and the nonzero bracket with $v$; the same argument applies to $(t-s)E$. For the once-punctured torus, A.14 shows that every normalizing element centralizes the characteristic involution $c$; its degree-seven witness and the nonzero difference $2(t-s)D$ therefore give the same closed embedding. A compact homogeneous space having one isolated point has every point isolated and is finite. Our quotients are infinite, so have no isolated points. The usual characterization of compact metrizable perfect zero-dimensional spaces finishes the proof. The coset space has no asserted canonical group law. $\square$

## A.10. Proved — Corrections to scans 322–326

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


The following statements replace the normality guesses of §26, folios 163–165, while preserving its valid orbit constructions.

1. The unoriented map of scan 322 is $O/H$ to the conjugates of $H$, with fibers $N_O(H)/H$. Its oriented strict counterpart is the map from $O/\Sigma$ to strict geometric subgroups, with image the conjugacy orbit and fibers $N_O(\Sigma)/\Sigma$. Injectivity is equivalent to $N_O(\Sigma)=\Sigma$, whereas uniqueness of the strict subgroup is equivalent to $N_O(\Sigma)=O$. These are different assertions. The withdrawn self-normalizer speculation on scan 322 is not reinstated.
2. The multiplier and cusp-permutation maps on scan 323 are homomorphisms. For the extended geometric subgroup $H$, the orientation-preserving subgroup is $\Sigma=\ker(\chi|_H)$, and $\Sigma\subset H\subset N_O(\Sigma)$ as on scan 324. The assertions that $\Sigma$ is invariant or unique are false for all three pro-$\ell$ types by A.3, A.6, and A.14, and, by A.6, for the full profinite four-puncture sphere. The full profinite tripod remains A.4.
3. With $\Sigma$ chosen, $\Gamma_\Sigma=N_O(\Sigma)/\Sigma$ is well-defined. Geometric extended groups $H$ with orientation subgroup $\Sigma$ determine a single conjugacy class of involutions in $\Gamma_\Sigma$, as on scan 325. This is an injection into the involutions, not an assertion that every involution is geometric: $H$ is the full inverse image of its order-two quotient, and conjugating two such $H$ necessarily normalizes their common $\Sigma$.
4. Formula (17) on scan 326 is the orbit formula $\operatorname{Isom}_{\rm lac}^{\rm out}(\widehat\Pi,\pi)/N\simeq\{\text{strict geometric subgroups}\}$. It does not require $N=O$.

The proofs are the orbit–stabilizer identity and the stated kernel properties, with A.3, A.6, and A.14 supplying the counterexamples in the three pro-$\ell$ types. The alternatives “injective / bijective / injection” on scan 322 must therefore be interpreted relative to the explicitly described image; the mathematics supports injectivity onto that image as the self-normalizer condition, not surjectivity onto all closed subgroups. We inspected the scan, but do not declare the handwriting settled.

## A.11. Proved — Equivariant lifting away from $2,3$

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


Let $S$ be the special outer automorphism group of $F_2^{(\ell)}$, with its degree filtration $S_n$. If $\ell\nmid6$, every $S_3$-invariant class in $S_n/S_{n+1}$ lifts to $C_{S_n}(S_3)$.

*Proof.* The kernel of the action of $\operatorname{Aut}(F)$ on $F/\Phi(F)$ is pro-$\ell$: on each finite characteristic $\ell$-group quotient its analogous kernel is an $\ell$-group, and these quotients detect automorphisms. The special outer group is a closed quotient of a subgroup of this kernel and is also pro-$\ell$. If a finite group $A$ of order prime to $\ell$ acts on a pro-$\ell$ group $P$ and $N$ is closed, normal, and $A$-stable, then $C_P(A)\to C_{P/N}(A)$ is onto. In a finite $\ell$-group this follows by the standard conjugacy-of-complements argument in $N\rtimes A$; equivalently, one inducts through an $A$-stable central series and kills each abelian cocycle by averaging, since $|A|$ is invertible on a finite $\ell$-group. Compactness over the finite $A$-stable quotients gives the pro-$\ell$ assertion. Apply it with $P=S_n$, $N=S_{n+1}$, and $A=S_3$. This argument is deliberately not asserted at $\ell=2,3$. $\square$

## A.12. Proved — Integral lifting with the elliptic boundary fixed exactly

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


Let $F=F_2^{(\ell)}$ have free generators $a,b$, and put $w=[a,b]$. Every integral homogeneous derivation $D$ of $L_{\mathbb Z_\ell}(a,b)$ of positive degree $n$ satisfying $D([a,b])=0$ is the leading term of an automorphism $\alpha$ of $F$ satisfying $\alpha(w)=w$ and acting trivially on $F^{\rm ab}$.

*Proof.* Choose $U,V\in\gamma_{n+1}F$ lifting $D(a),D(b)$ and start with $a'=Ua$, $b'=Vb$. The class of $[a',b']w^{-1}$ in $\gamma_{n+2}F/\gamma_{n+3}F$ is $[D(a),b]+[a,D(b)]=0$. Thus the initial error lies in $\gamma_{n+3}F$. If the current error lies in $\gamma_mF$, multiply $a',b'$ by corrections in $\gamma_{m-1}F$. Their contribution to its degree-$m$ class is

$$
 (u,v)\longmapsto [u,b]+[a,v],\qquad L_{m-1}^{\oplus2}\longrightarrow L_m.
$$

This map is surjective over $\mathbb Z$: brackets with the two generators span the free Lie algebra in every degree. Choose corrections killing the error and continue. The corrections converge in the actual pro-$\ell$ group by the finite-$\ell$-quotient argument of A.1. They produce the exact identity $[a',b']=w$. Their degrees are greater than $n+1$, so the prescribed leading term is unchanged. The resulting endomorphism is an automorphism by the pro-$\ell$ Burnside basis theorem and finite generation. It acts identically on the integral abelianization. No logarithm, exponential, denominator, or odd-prime hypothesis occurs. $\square$

## A.13. Proved — The outer IA group of a free pro-$\ell$ group is torsion-free

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


For $F=F_r^{(\ell)}$, $r\geq2$, the kernel of $\operatorname{Out}(F)\to GL_r(\mathbb Z_\ell)$ has no nontrivial finite-order elements. This includes $\ell=2$.

*Proof.* Put $\mathcal A_n=\ker(\operatorname{Aut}F\to\operatorname{Aut}(F/\gamma_{n+1}F))$ and let $\mathcal O_n$ be its image in $\operatorname{Out}F$. Taking the leading change of the free generators embeds $\mathcal A_n/\mathcal A_{n+1}$ in $\operatorname{Hom}_{\mathbb Z_\ell}(H,L_{n+1})$, where $H=F^{\rm ab}$. In fact every homomorphism lifts by choosing images of the free generators, but injectivity is enough here.

We have $\mathcal A_n\cap\operatorname{Inn}F=\operatorname{ad}(\gamma_nF)$. Indeed, if a conjugating element first has nonzero degree $k<n$, its leading class would have to commute with every free generator. The center of the free Lie algebra is zero, so this is impossible. It follows that

$$
 \mathcal O_n/\mathcal O_{n+1}\hookrightarrow
 \operatorname{Hom}(H,L_{n+1})/\operatorname{ad}L_n.
$$

The denominator is saturated over $\mathbb Z_\ell$. To check this, suppose $\operatorname{ad}(A)$ is divisible by $\ell$ in the homomorphism module. Reducing modulo $\ell$ shows that $\bar A$ commutes with every generator of the ordinary free Lie algebra over $\mathbb F_\ell$. Embedding this Lie algebra in the free associative algebra shows $\bar A=0$: an element commuting with all free generators is scalar, and a positive-degree Lie element cannot be scalar. Therefore $A=\ell B$. Repeating this argument proves saturation. The displayed quotient, and hence every outer graded piece, is a torsion-free $\mathbb Z_\ell$-module.

Finally, $\bigcap_n\mathcal O_n=1$. For an outer class in every $\mathcal O_n$, choose a representative $\beta$. The sets of $g\in F$ for which $\operatorname{ad}(g)^{-1}\beta$ induces the identity modulo $\gamma_{n+1}F$ are nonempty nested closed subsets of the compact group $F$. Their intersection is nonempty. Since $\bigcap_n\gamma_nF=1$, a conjugator in that intersection makes $\beta$ the identity on $F$. Thus the outer class was trivial. Every nontrivial IA outer class consequently has a first nonzero outer graded term. If its order were a positive integer $m$, its $m$th power would have leading term $mD$, which is nonzero in a torsion-free $\mathbb Z_\ell$-module. This contradiction proves the assertion. $\square$

## A.14. Refuted — Pro-$\ell$ normality of the geometric once-punctured-torus subgroup

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


For every prime $\ell$, including $2$, the geometric subgroup $\Sigma_{1,1}^{(\ell)}\subset O_{1,1}^{(\ell)}$ is not normal.

*Proof.* Let $c$ be the geometric elliptic involution. The discrete mapping class group of the once-punctured torus is $SL_2(\mathbb Z)$, and $c$ is its central element $-I$. It is represented on the free group by $a\mapsto a^{-1}$, $b\mapsto b^{-1}$; its action sends $[a,b]$ to a conjugate of $[a,b]$, and its outer order is two. Thus $c$ remains a central involution in the closure $\Sigma=\Sigma_{1,1}^{(\ell)}$.

This is the unique nontrivial central involution of $\Sigma$. The continuous homology map sends $\Sigma$ onto $SL_2(\mathbb Z_\ell)$, because the elementary integral unipotent matrices are dense in their $\ell$-adic counterparts. The center of $SL_2(\mathbb Z_\ell)$ is $\{I,-I\}$: commuting with both elementary unipotent subgroups forces a matrix to be scalar, and determinant one then forces its scalar to square to one. A central involution $z$ of $\Sigma$ therefore maps to $I$ or $-I$. In the first case A.13 gives $z=1$. In the second case $zc$ is an IA element and $(zc)^2=1$, so A.13 gives $z=c$. This proves uniqueness. Consequently every automorphism of $\Sigma$, and in particular conjugation by every element of its normalizer in $O$, fixes $c$.

Here is a fully integral counterexample to that necessary centralizing condition. Write $r_0=[a,b]$ and $r_{j+1}=[r_j,b]$. Define a degree-seven derivation by

$$
\begin{aligned}
 D(a)&=-2[a,[r_0,r_3]]-3[a,[r_1,r_2]]
       +2[r_0,[r_0,r_2]]+[[r_0,r_1],r_1],\\
 D(b)&=2[r_0,r_4]+5[r_1,r_3].
\end{aligned}
$$

It satisfies $[D(a),b]+[a,D(b)]=0$. Applying the derivation $u\mapsto[u,b]$ to the first line cancels the terms containing $[a,\cdot]$ against the second line; the remaining expression is

$$
 -[r_0,[r_1,r_2]]+[r_1,[r_0,r_2]]+[[r_0,r_1],r_2]=0
$$

by Jacobi. Its outer class is nonzero. An exact independent matrix certificate in `code/ab_elliptic.py` computes rank $18$ for the degree-seven inner derivations and rank $19$ after adjoining $D$; its integral Lyndon coordinates, with a coefficient equal to one, are in `code/ab_elliptic_results.json`. Equivalently, an inner derivation killing $[a,b]$ must come from the line generated by $[a,b]$, and that line has degree two, not seven.

By A.12 choose an IA automorphism $\alpha$ fixing the entire boundary word $[a,b]$ and having leading term $D$. On degree-$n$ derivations, conjugation by $c$, whose linear action is $-I$, acts as $(-1)^n$. Hence $c\alpha c^{-1}$ has leading term $-D$. Were $\alpha$ to normalize $\Sigma$, the characteristic property of $c$ would force $c\alpha c^{-1}=\alpha$ in the outer group. Their first difference would be $2D=0$, contradicting A.13's saturated graded module. In particular, $2D\ne0$ over $\mathbb Z_2$; reduction modulo two alone would have missed the obstruction. Therefore $\alpha\notin N_O(\Sigma)$ and $\Sigma$ is not normal. $\square$

## A.15. Proved — The elliptic normalizer quotient through ordinary degree twelve

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


Let $\mathfrak e_+$ be the positive outer boundary-preserving derivation algebra of A.7, and let $\mathfrak g=\mathfrak{sl}_2\ltimes\mathfrak u$ be the full geometric Lie image of A.8. Define

$$
 N^+_{\mathfrak e}(\mathfrak g)=
 \{D\in\mathfrak e_+:[D,\mathfrak g]\subseteq\mathfrak g\}.
$$

This is the normalizer of the full relative geometric Lie algebra, including its degree-zero $\mathfrak{sl}_2$; it is not defined by normalizing only $\mathfrak u$. We have

| Degree | Geometric $\mathfrak u_n$ | $N^+_{\mathfrak e}(\mathfrak g)_n$ | Normalizer quotient |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 |
| 4 | 3 | 3 | 0 |
| 5 | 0 | 0 | 0 |
| 6 | 5 | 6 | 1 |
| 7 | 0 | 0 | 0 |
| 8 | 10 | 10 | 0 |
| 9 | 0 | 0 | 0 |
| 10 | 24 | 25 | 1 |
| 11 | 0 | 0 | 0 |
| 12 | 50 | 50 | 0 |

After doubling the usual weights of $\mathfrak{grt}_1$, the quotient is isomorphic to $\mathfrak{grt}_1$ throughout this range: its weight-three and weight-five generators occur in elliptic degrees six and ten. With the rational fiber functor and splittings fixed, the comparison is induced by their common arithmetic mixed-Tate Lie subalgebra, not by an equality of dimensions alone.

*Proof.* Normalizing $\mathfrak{sl}_2$ modulo $\mathfrak u$ gives an injection

$$
 \bigl(N^+_{\mathfrak e}(\mathfrak g)/\mathfrak u\bigr)_n
 \hookrightarrow(\mathfrak e_n/\mathfrak u_n)^{\mathfrak{sl}_2}.
$$

Finite-dimensional rational $\mathfrak{sl}_2$-modules are semisimple. Therefore the dimension on the right is the difference of the multiplicities of the trivial module in $\mathfrak e_n$ and $\mathfrak u_n$. The Witt character formula, or simply the multidegrees of the Lyndon words, computes the ambient character as

$$
 [H\otimes L_{n+1}(H)]-[L_{n+2}(H)]-\delta_{n,2}[\mathbb Q].
$$

Our independently generated geometric basis consists of homogeneous weight vectors. Counting these weights and taking the difference between the multiplicities of weights zero and two computes its trivial multiplicity. The resulting upper bounds in degrees one through twelve are zero except in degree six, where the bound is one, and degree ten, where it is three. The full decompositions are in `code/ab_elliptic_normalizer_results.json`. In particular, no odd-degree normalizer class survives; this also follows from the central element $-I$ of $SL_2$.

The degree-ten upper bound requires one additional equation. Its three invariant ambient derivations are constructed by taking the simultaneous kernels of the raising and lowering operators. Any one normalizing $\mathfrak g$ must satisfy $[D,\epsilon_4]\in\mathfrak u_{14}$. The same complete geometric recursion gives $\dim\mathfrak u_{14}=109$. Adjoining the three brackets to an exact basis of that space raises the rank to $111$. Thus this necessary normalizer equation has rank two on the invariant three-dimensional space, and the degree-ten quotient has dimension at most one. These are exact rational ranks, not ranks modulo a prime. `code/ab_elliptic_normalizer.py` constructs the whole matrix and records the result.

For the matching lower bounds, Hain and Matsumoto (2020), Remark 29.3, give an injective map from the arithmetic mixed-Tate Lie algebra $\mathfrak k$ to the geometric normalizer quotient. Their Proposition 29.1 places the class of $\sigma_{2m+1}$ in $W$-degree $-(4m+2)$, modulo geometric derivations. It therefore supplies nonzero classes in ordinary degrees six and ten. Passing from the tangent-base-point action to outer derivations kills only the degree-two line $\mathbb Q\operatorname{ad}[a,b]$, so it does not kill either class. The representative is intrinsically defined modulo the geometric image, so the splitting ambiguity does not affect this quotient. Together with the upper bounds, this proves the table.

For the comparison with $\mathfrak{grt}_1$, use the arithmetic free Lie subalgebra and faithful tripod action in F.2. Through ordinary weights at most six, $\mathfrak k\to\mathfrak{grt}_1$ is an isomorphism: the independent pentagon bounds equal the free arithmetic dimensions. Its elliptic normalizer map is also an isomorphism after doubling weights by the table just proved. These two maps give the asserted comparison. The only possible bracket of the two positive degrees with total at most twelve is the bracket of the degree-six line with itself, which is zero. Thus the comparison respects every bracket in the claimed range. No all-weight elliptic normalizer equality is inferred. $\square$

## A.16. Open — The remaining elliptic profinite and all-degree normalizer questions

*Manuscript connection: §26; folios 163–165; scans 322–326.*

\nopagebreak[4]


We do not decide normality of $\Sigma_{1,1}$ in the full profinite $O_{1,1}$, nor whether the full graded quotient $N^+_{\mathfrak e}(\mathfrak g)/\mathfrak u$ is $\mathfrak{grt}_1$ with doubled weights.

*Attack and exact remaining obligations.* The explicit degree-seven derivation in A.14 lifts with exact boundary relation in every free pro-$\ell$ group by A.12. Extending that construction to $\widehat F_2$ requires solving $[a',b']=[a,b]$ simultaneously in nonnilpotent finite quotients while retaining an automorphism and the prescribed odd leading class at some prime. Ordinary lower-central correction cannot supply that step. Thus the pro-$\ell$ proof does not settle full profinite normality. Even a successful boundary-preserving profinite lift would require the corresponding characteristic-central-involution argument for the full geometric closure, or a directly verified failure to normalize it; we do not assume that extra transfer.

For the Lie normalizer, A.15 supplies a complete computation through degree twelve and rules out every odd degree in all weights. The first even degree not closed by our normalizer test is fourteen. Our geometric calculation already gives $\dim\mathfrak u_{14}=109$, and the arithmetic $\sigma_7$ gives a nonzero quotient class there. What remains is to impose the bracket conditions against all geometric generators on the remaining invariant ambient classes, and to show in every degree that the resulting quotient has no further classes. The finite test against $\epsilon_4$ closed degree ten; we do not promote it to a sufficient all-degree criterion. The verified source comparison and the exact calculations replace the earlier degree-four uncertainty, while leaving these stronger obligations explicit.

# B. Filling: a profinite counterexample and the exact repaired sequence

We distinguish $f_x:O_{0,4,x}\to O_{0,3}$, which is an outer filling map, from $\theta_x:O_{0,4,x}\to\operatorname{Aut}_{\rm lac}(\pi_{0,3})$, which becomes genuine after choosing the inertia subgroup at the filled cusp. Its base-point ambiguity is conjugation by an inner automorphism of the target. The construction and the restriction of $\theta_x$ to point-pushing are LM3 C.7; we use that proved statement without repeating its proof.

## B.1. Proved — Filling is surjective in every graded degree

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


In the rational graded special outer algebras, filling $x$ induces a surjective homomorphism $\mathfrak s_3\to\mathfrak s_2$. It is split as a graded Lie homomorphism by extending the unique sum-preserving representative in every positive nonzero target degree and setting $D(x)=0$. Through degree six the dimensions are as follows.

| Degree | Source | Image | Kernel | Point-pushing | Kernel modulo point-pushing as vector spaces |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 0 | 2 | 2 | 0 |
| 2 | 1 | 0 | 1 | 1 | 0 |
| 3 | 6 | 1 | 5 | 2 | 3 |
| 4 | 6 | 0 | 6 | 3 | 3 |
| 5 | 28 | 3 | 25 | 6 | 19 |
| 6 | 36 | 0 | 36 | 9 | 27 |

The last column is a vector-space quotient in each degree; point-pushing is not an ideal in the full source algebra.

*Proof.* For $n\geq2$ the gauge $D(S)=0$ removes inner ambiguity, and

$$
 \dim\mathfrak s_{r,n}=r\ell_n(r)-\ell_{n+1}(r).
$$

In degree one the dimension is $(r+1)(r-2)/2$. The target is zero in degrees one and two, so no degree-one gauge ambiguity affects the proposed section. In all higher degrees, a target derivation killing $y+z$ extends by $D(x)=0$ and kills $x+y+z$. Extension commutes with brackets, proving the split surjection. The dimensions follow from this formula and the Witt dimensions of the free point-pushing algebra. `code/ab_lie.py` also computes each image and point-pushing rank by an independent exact matrix calculation, rather than subtracting the announced dimensions. $\square$

## B.2. Proved — The first required ideal generators of the filling kernel

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


Let $\mathfrak k=\ker(\mathfrak s_3\to\mathfrak s_2)$. It is an ideal, and the dimensions of its minimal homogeneous generators *as an ideal of $\mathfrak s_3$* through degree six are

$$
 \dim\bigl(\mathfrak k/[\mathfrak s_3,\mathfrak k]\bigr)_n
 =2,0,3,0,13,0.
$$

In particular, point-pushing alone does not generate the kernel as an ideal, and adding the three degree-three generators still does not suffice: thirteen further generators are necessary in degree five.

*Proof and computation.* For each $n$, the program `code/ab_kernel.py` computes an exact basis of the filling kernel and forms every bracket $[\mathfrak s_{3,i},\mathfrak k_{n-i}]$, $1\leq i<n$. Their exact ranks are $0,1,2,6,12,36$. Subtraction from the kernel dimensions in B.1 gives the displayed sequence. An all-degree exact description is the kernel of the explicit tuple map

$$
 (a_x,a_y,a_z):\ [a_x,x]+[a_y,y]+[a_z,z]=0
 \quad\longmapsto\quad
 ([\bar a_y,y],[\bar a_z,z]),
$$

with the degree-one residual inner line removed and bars denoting $x=0$. This gives a finite linear algorithm in every prescribed degree. A closed minimal generating set in all degrees is not obtained; the first uncomputed indecomposable degree is seven. $\square$

## B.3. Refuted — The pro-$\ell$ filling sequence is exact in the middle (Lead 3)

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


For every prime $\ell$, the kernel of $f_x:O_{0,4,x}^{(\ell)}\to O_{0,3}^{(\ell)}$ strictly contains point-pushing. The genuine map $\theta_x$ is not injective. An integral degree-three witness is

$$
 E(x)=[[y,[x,y]],x],\qquad
 E(y)=-[[x,[x,y]],y],\qquad E(z)=0.
$$

*Proof.* Jacobi gives $E(x+y+z)=0$. Filling $x$ gives zero, whereas filling $z$ gives a nonzero special outer derivation of the rank-two free Lie algebra. Geometric pure four-puncture automorphisms become pure geometric tripod automorphisms under *either* filling, and the latter group is trivial. Thus $E$ is not point-pushing. More strongly, both conjugators in the displayed formula belong to $(x)$. The strengthened assertion of A.1 supplies a special group automorphism with this leading term in $\ker\theta_x$. It is nontrivial because its leading outer class is nonzero.

The supplied code checks the Jacobi identity by expansion, checks both fillings, and verifies that adjoining $E$ raises the degree-three point-pushing rank from two to three. For $u,v$ of A.5 it also checks

$$
 [E,u]=0,\qquad [E,v](z)=[E(x),z]\ne0,
$$

and that adjoining $[E,v]$ raises the degree-four point-pushing rank from three to four. These checks are exact over $\mathbb Z$; nonvanishing over $\mathbb Z_\ell$ holds also at $2,3$. $\square$

## B.4. Proved — Full profinite and pro-$\ell$ surjectivity of filling

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


The maps

$$
 f_x:O_{0,4,x}\twoheadrightarrow O_{0,3},\qquad
 \theta_x:O_{0,4,x}\twoheadrightarrow\operatorname{Aut}_{\rm lac}(\widehat F_2)
$$

are onto. The same assertions hold for every maximal pro-$\ell$ quotient. The corresponding outer surjectivity holds for all genus-zero fillings with hyperbolic target.

*Proof.* Begin with a label-preserving exponent-one outer automorphism $\beta$ of the target $\widehat F(y,z)$. It carries $yz$ to a conjugate of itself. Conjugate a representative so that it fixes $yz$ exactly. Extend this representative to $\widehat F(x,y,z)$ by $x\mapsto x$. Its inverse extends in the same manner, so this is an automorphism of the free profinite group, not merely an endomorphism. It preserves the three generator classes and fixes $xyz$. Hence it is a special preimage of $\beta$.

For a general loop-preserving outer automorphism of the tripod, abelianization forces the three peripheral exponents to be one common unit $\lambda\in\widehat{\mathbb Z}^{\times}$. Its cusp permutation lifts by a geometric mapping class fixing the extra puncture. Choose a rational four-puncture curve whose filling gives the rational tripod; its Galois action realizes every multiplier, since the cyclotomic character of $G_{\mathbb Q}$ is onto. Remove these two factors from the desired automorphism and apply the special construction. The same argument works with $\mathbb Z_\ell^{\times}$ and pro-$\ell$ free products, and with any finite number of rational punctures.

Finally $\theta_x$ has the same outer image as $f_x$. Its restriction to point-pushing is the isomorphism $\pi_{0,3}\simeq\operatorname{Inn}(\pi_{0,3})$, since the target is center-free. Thus point-pushing adjusts any inner discrepancy, proving genuine surjectivity. $\square$

## B.5. Refuted — The unrestricted full profinite filling sequence

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


The full profinite sequence marked “??” in §33 bis, folio 202, scan 399, is not exact in the middle already for $(0,4)\to(0,3)$. There are two distinct oriented prediscretizations with the same image under filling. The map $\theta_x$ in §30, folio 176, scan 348, is onto but not injective.

*Proof: an actual profinite counterexample.* Let $\beta\ne1$ be a special outer automorphism of $\widehat F(x,y)$. Such an element exists arithmetically. Put $L=\mathbb Q(\sqrt[3]{2},\zeta_3)$, whose Galois group over $\mathbb Q$ is $S_3$. Its largest abelian subextension is $\mathbb Q(\zeta_3)$, so $G_{\mathbb Q}^{1}=\ker\chi=\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q^{\rm ab})$ maps onto $A_3=\operatorname{Gal}(L/\mathbb Q(\zeta_3))$. Choose an element mapping to a nonidentity three-cycle. The faithful tripod action (Belyi; LM3 D.16) gives a nonidentity outer automorphism $\beta$. It is special because the cusps are rational and its cyclotomic exponent is one.

Choose a genuine representative $b$ of $\beta$ fixing $xy$ exactly, by conjugating its product conjugator away. Extend it to the free profinite group

$$
 F=\widehat F(x,y,z)=\widehat F(x,y)\amalg\widehat{\mathbb Z}(z)
$$

by fixing $z$. The inverse extends too. This extension preserves the conjugacy classes of $x,y,z$ and fixes $xyz=(xy)z$, so it belongs to $O_{0,4}$ and fixes every cusp label.

On filling $x$, the conjugate of $y$ becomes exactly $y$: the image of its conjugator lies in the procyclic group generated by $y$. The generator $z$ remains fixed. Thus $f_x(b)=1$. On filling $z$, its outer class is precisely $\beta\ne1$. Every element of the pure geometric subgroup $\widehat P_{0,4}$ fills $z$ into $\widehat P_{0,3}=1$. Therefore $b\notin\widehat P_{0,4}$, in particular $b$ is not point-pushing. This is a group-level counterexample in the full profinite topology; it does not require lifting a pro-$\ell$ automorphism to $\widehat F$.

The cosets $\Sigma_{0,4,x}$ and $b\Sigma_{0,4,x}$ are distinct and have the same filled image. Also $\theta_x(b)$ is inner because $f_x(b)=1$. Choose the unique point-pushing element $k$ with $\theta_x(k)=\theta_x(b)$. Then $bk^{-1}\ne1$ and $\theta_x(bk^{-1})=1$. This proves the final assertion. The finite $S_3$ field computation used to select $\beta$ is LM3 B.5; the new free-product and filling deductions are the proof here. $\square$

## B.6. Known — The exact point-pushing normalizer sequence for the tripod

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


Let $K\simeq\widehat F_2$ be the point-pushing subgroup of $O_{0,4,x}$, and define

$$
 O'=N_{O_{0,4,x}}(K).
$$

Then filling gives an exact sequence

$$
 1\longrightarrow K\longrightarrow O'
 \longrightarrow\widehat{GT}\times S_3\longrightarrow1,
$$

where the last group is viewed through its faithful natural action on the target tripod. Equivalently, $\theta_x$ identifies $O'$ with the inverse image of $\widehat{GT}\times S_3$ in $\operatorname{Aut}_{\rm lac}(\widehat F_2)$. The same proof works for the pro-$\ell$ versions, with $GT^{\{\ell\}}$ as defined by Hoshi, Minamide, and Mochizuki (2022, Definition 2.7).

*Proof of the reduction from the cited theorems.* Let $T=\mathbb P^1\setminus\{0,1,\infty\}$ and $E=\pi_1(T_2)=\pi_1(M_{0,5})$, where $T_2$ is its ordered two-point configuration space. Its projection to the first point gives

$$
 1\longrightarrow F\longrightarrow E\longrightarrow\pi_1(T)\longrightarrow1,
 \qquad F\simeq\widehat F_3.
$$

The outer monodromy embeds the quotient as $K$. Since $F$ is center-free, $E$ is canonically the pullback of $\operatorname{Aut}(F)\to\operatorname{Out}(F)$ over $K$. An outer automorphism $\alpha$ of $F$ normalizing $K$ therefore conjugates this pullback to itself. Choosing a genuine representative changes the resulting automorphism of $E$ only by an inner automorphism from $F$. Conversely, an automorphism of $E$ preserving $F$ restricts to an outer automorphism normalizing $K$. Its extension by the pullback construction is the original automorphism: both have the same conjugation action on $F$, and $E$ embeds in $\operatorname{Aut}(F)$. Thus the homomorphism from the normalizer to the indicated outer automorphism group of $E$ is onto. Its kernel is exactly $K$: its extension is inner precisely when its restriction to $F$ is the point-pushing outer action of an element of $E/F$. This proves

$$
 1\longrightarrow K\longrightarrow N_{O_{0,4,x}}(K)
 \longrightarrow\operatorname{Out}(E;F,I_{\rm diag})\longrightarrow1.
$$

Here $I_{\rm diag}$ is the distinguished fiber cusp where the two moving points collide. This notation also imposes the peripheral condition inherited from $O_{0,4,x}$.

Hoshi, Minamide, and Mochizuki (2022, Corollaries 2.6(i), 2.8(i), and Definition 2.7) identify

$$
 \operatorname{Out}(E)=\widehat{GT}\times S_5
$$

and identify the five generalized fiber subgroups intrinsically. Preserving $F$ fixes the forgotten moving label. Preserving its distinguished diagonal cusp fixes the other moving label as well. The remaining permutation group is precisely $S_3$ on the three original tripod labels. The $GT$ factor preserves all these data. Thus the last group in the previous exact sequence is $\widehat{GT}\times S_3$.

For its induced action on the base, Hoshi and Mochizuki (2011, Theorem 6.1, the case $n=1$) says that the FC-admissible outer automorphism of $\pi_1(T_2)$ is determined by its restriction to $\pi_1(T)$. It supplies injectivity, not surjectivity onto every automorphism of the surface group. The $S_3$ factor acts faithfully on the three cusp labels, and the $GT$ factor is FC-admissible. Hence the induced base action is faithful. Filling therefore has kernel exactly $K$ on $O'$, and its image is the asserted subgroup. The final assertion about $\theta_x$ follows by the same inner-adjustment argument as B.4, now with trivial kernel. All source and target groups here are profinite and every map is continuous. $\square$

## B.7. Proved — The general FC-admissible repair supplied by cuspidalization

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


For a hyperbolic curve with center-free geometric fundamental group, let $E$ be the two-point configuration group, $F$ a fiber group, and $K$ its point-pushing outer monodromy. Let $O'_{\rm FC}$ be the subgroup of $N_{O_{g,\nu+1,i}}(K)$ whose induced outer automorphism of $E$ is FC-admissible. If $J$ is its image in $O_{g,\nu}$, then

$$
 1\longrightarrow\pi_{g,\nu}\longrightarrow O'_{\rm FC}
 \longrightarrow J\longrightarrow1
$$

is exact. The same assertion holds with all primes or one prime in the characteristic-zero configuration theorem.

*Proof.* The pullback argument in B.6 identifies the quotient of $O'_{\rm FC}$ by point-pushing with the corresponding FC-admissible outer automorphism group of $E$. Hoshi and Mochizuki (2011, Theorem 6.1) makes restriction from configuration level two to level one injective. Thus the kernel is exactly point-pushing. Surjectivity onto $J$ is its definition, so there is no unproved assertion that $J=O_{g,\nu}$. In genus zero over the tripod, B.6 computes $J=\widehat{GT}\times S_3$. $\square$

## B.8. Open — Removing the FC condition in general type

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


For general $(g,\nu)$, the equality of the bare normalizer of one point-pushing subgroup with $O'_{\rm FC}$ is not established here. The exact remaining implication is: an outer automorphism of the fiber preserving its peripheral classes and normalizing monodromy must preserve every configuration fiber subgroup and the cuspidal data required in the definition of FC-admissibility. Extending to the one fixed group extension is formally enough to normalize point-pushing; it is not by itself the full FC condition. The tripod case is settled by the intrinsic five-fiber reconstruction used in B.6. The first further hyperbolic types requiring a separate verification include $(0,4)$ as the base and $(1,1)$ as the base. This is a limitation of the general reduction, not a qualification of B.6.

## B.9. Refuted — Unrestricted prediscretization bijectivity; proved restricted replacement

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


The map

$$
 O_{0,4,x}/\Sigma_{0,4,x}\longrightarrow O_{0,3}/\Sigma_{0,3}
$$

is surjective but not injective in the full profinite and in every pro-$\ell$ case. For the restricted source $O'$ of B.6, it instead induces a bijection

$$
 O'/\Sigma_{0,4,x}\ \xrightarrow{\sim}\
 (\widehat{GT}\times S_3)/S_3\simeq\widehat{GT}.
$$

*Proof.* Surjectivity follows from B.4 and geometric filling. The two distinct cosets in B.5, or the witness in B.3, prove failure of injectivity. For the restricted statement, both the restricted group and its geometric subgroup have the same filling kernel $K$, and their images are $\widehat{GT}\times S_3$ and $S_3$. The coset bijection follows directly: two representatives have images differing by an element of $S_3$ exactly when they differ by an element of $\Sigma_{0,4,x}$. This is a bijection of compact quotient spaces. $\square$

## B.10. Proved — The exact structure of the unrestricted filling kernel

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


Let $Q=\ker\theta_x$. In the full profinite and every pro-$\ell$ case,

$$
 \ker f_x=Q\rtimes K,\qquad
 1\longrightarrow Q\longrightarrow O_{0,4,x}
 \xrightarrow{\theta_x}\operatorname{Aut}_{\rm lac}(\pi_{0,3})\longrightarrow1.
$$

Here $Q\ne1$. For the pro-$\ell$ lower-central graded spaces, its first six rational dimensions are $0,0,3,3,19,27$.

*Proof.* The second sequence is exact by definition and B.4. On $\ker f_x$, the map $\theta_x$ lands in $\operatorname{Inn}(\pi_{0,3})$. Its restriction to $K$ is an isomorphism onto this group, so it splits this restriction and gives the semidirect product. Nontriviality is B.3 or B.5. The filtration is strict on the point-pushing section: an element of degree at least $n$ gives a based inner automorphism of degree at least $n$, and conversely center-freeness of the free graded Lie algebra detects the degree of the pushing element. Normalizing an outer automorphism of degree at least $n$ at the filled cusp uses a conjugator in $\gamma_nF$, so $\theta_x$ respects this filtration. Thus the semidirect decomposition is strict, and the graded dimensions follow by subtracting the point-pushing dimensions from the kernel dimensions in B.1; equivalently, one imposes the additional vanishing of the conjugator of the filled cusp after passage to the quotient. A.1 supplies the corresponding integral lifts. This semidirect product does not say that $K$ is normal in $\ker f_x$; $Q$ is the normal factor. $\square$

The statements above concern hyperbolic targets. They do not use center-freeness for $(0,0),(0,1),(0,2)$ or $(1,0)$, where that hypothesis either has no content or fails. In particular, filling the tripod to a twice-punctured sphere has procyclic target and is not covered by the point-pushing identification with its inner automorphism group. The counterexamples have multiplier one, so adjoining orientation-reversing geometric automorphisms does not remove them. No inference about arithmetic faithfulness over a real closed field is made from the number-field construction.


## B.11. Open — An all-degree minimal presentation of the filling Lie kernel

*Manuscript connection: §30; folio 176; scan 348; §33 bis; folio 202; scan 399.*

\nopagebreak[4]


Determine a minimal homogeneous generating set and defining relations for

$$
 \mathfrak k=\ker(\mathfrak s_3\longrightarrow\mathfrak s_2)
$$

as a Lie algebra and as an ideal of $\mathfrak s_3$, in every degree. The all-degree split surjection in B.1 and the group-kernel decomposition in B.10 do not supply this presentation.

*Attack and strongest proved partial.* B.2 gives an exact finite linear algorithm for $\mathfrak k_n$ in each specified degree: impose the special tuple equation, set the filled generator equal to zero, and remove the residual inner ambiguity. We then form every bracket $[\mathfrak s_{3,i},\mathfrak k_{n-i}]$ to calculate the minimal generators as an ambient ideal. The exact counts through degree six are $2,0,3,0,13,0$. Therefore the point-pushing degree-one generators require three further degree-three generators and thirteen further degree-five generators; the first three additional generators alone cannot generate the ideal. The first uncomputed ideal-indecomposable degree is seven. To complete the requested presentation one must compute these indecomposables in every degree, provide actual homogeneous representatives, and determine the relations among their iterated brackets. The finite matrices give a terminating calculation in any fixed degree, but we have not proved a uniform generating formula, stabilization theorem, or complete family of relations. No finite-range computation is presented as an all-degree presentation.


# C. Finite coverings

Throughout this part, all automorphisms of profinite groups are continuous. A peripheral structure means the full collection of conjugacy classes of maximal cusp inertia subgroups, with one common orientation multiplier. We write $\Gamma(S)$ for the orientation-preserving mapping class group with punctures permitted to permute, and $P\Gamma(S)$ for its pure subgroup. Its geometric closure in the appropriate outer automorphism group is denoted by $\Sigma(S)$. We use the established LM3 statements B.9, B.12, B.13 and E.7, without repeating their proofs. The new comparisons below concern §28, folios 179–183, scans 355–363; scans 355 and 356 were inspected, whereas scan 363 is available only in the supplied transcription.

## C.1. Refuted — Characteristicness of the index-two test covering

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


Let $G=\widehat F(x,y)$ be the tripod group, with peripheral classes $x,y,(xy)^{-1}$. The subgroup
$$
 V_2=\ker(G\longrightarrow C_2),\qquad x\longmapsto1,\quad y\longmapsto0,
$$
which corresponds to $z\mapsto z^2$, is normal but is not characteristic under loop-preserving automorphisms. The restriction homomorphism must therefore have source $\operatorname{Aut}_{\rm lac}(G;V_2)$, the open stabilizer of $V_2$. In contrast,
$$
 V_4=\ker(G\longrightarrow G^{\rm ab}/2G^{\rm ab})
$$
is characteristic. Its rank is five and its punctured-sphere type is $(0,6)$.

**Proof.** Interchanging the peripheral classes of $x$ and $y$ carries $V_2$ to the distinct kernel of $x\mapsto0,y\mapsto1$. This interchange is induced by an orientation-preserving homeomorphism of the tripod. The assertion about $V_4$ follows from functoriality of abelianization. Schreier's formula gives ranks $1+2(2-1)=3$ and $1+4(2-1)=5$. There are respectively four and six cusps, because the ramification indices above the three omitted points are $(2,1,2)$ and $(2,2,2)$; the Euler-characteristic formula then gives genus zero. All three nonzero maps $H_1(G,\mathbf F_2)\to C_2$ lie in one geometric $S_3$ orbit. Thus the stabilizer correction loses no cosets in the non-strict prediscretization comparison: every loop-preserving automorphism can first be adjusted by a geometric automorphism to stabilize $V_2$. This explains why Grothendieck expressly says “sans supposer $\pi'$ caract.” in the index-two example of scan 363. The characteristic hypothesis in the prompt cannot be imposed on that particular cover. $\square$

## C.2. Proved — The correctly typed deck-normalizer theorem

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


Let $V$ be an open normal subgroup of a center-free profinite surface group $G$, and suppose $C_G(V)=1$. Put $D=G/V$, viewed as a subgroup of $\operatorname{Out}(V)$ by conjugation. Then restriction gives an isomorphism
$$
 \operatorname{Aut}(G;V)\xrightarrow{\sim}
 \{a\in\operatorname{Aut}(V):[a]\in N_{\operatorname{Out}(V)}(D)\},
$$
and, after passing to outer automorphisms, an isomorphism
$$
 \operatorname{Out}(G;V)\xrightarrow{\sim}
 N_{\operatorname{Out}(V)}(D)/D.                         \tag{C.1}
$$
The same statements hold with loop-preserving automorphisms for the two covers in C.1, with the induced peripheral structures. Thus the prompt's normalizer modulo $D$ describes the **outer source**, not the image of a homomorphism with target $\operatorname{Aut}(V)$.

**Proof.** Conjugation identifies $G$ with a subgroup of $\operatorname{Aut}(V)$, by the centralizer hypothesis. This subgroup is exactly the inverse image of $D$ under $\operatorname{Aut}(V)\to\operatorname{Out}(V)$: both contain $\operatorname{Inn}(V)$ and have quotient $D$. An automorphism $a$ of $V$ normalizes this inverse image precisely when its outer class normalizes $D$. Conjugation by $a$ then defines the unique extension to $G$. Uniqueness also follows directly: if an automorphism of $G$ is the identity on $V$, then $g^{-1}\alpha(g)$ centralizes $V$ for every $g\in G$. The construction and its inverse are continuous. Quotienting by $\operatorname{Inn}(G)$ gives (C.1), because its restriction maps onto $D$ modulo $\operatorname{Inn}(V)$.

For the peripheral assertion, the inertia subgroups upstairs are the nontrivial intersections of conjugates of downstairs inertia with $V$. Downstairs inertia is recovered as the normalizer in $G$ of each such intersection. Boggi and Zalesskii (2019, Proposition 3.6) prove the required self-normalizer statement even for nonzero profinite powers of an algebraically simple element. Hence a peripheral automorphism upstairs which extends necessarily permutes the recovered downstairs inertia; the common exponent agrees under restriction. The same argument works for free pro-$2$ groups. $\square$

## C.3. Known — Coset injectivity holds for both test coverings

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


For $V_2$ use $A=\operatorname{Aut}_{\rm lac}(G;V_2)$ and let $B$ be the closure in $A$ of the corresponding discrete orientation-preserving stabilizer. For $V_4$ use the full loop-preserving group and its geometric closure. Let $A'=\operatorname{Aut}_{\rm lac}(V)$ and $B'$ be its geometric closure, including inner automorphisms. Then, for both test coverings,
$$
                         f^{-1}(B')=B.                 \tag{C.2}
$$
Consequently the restriction map on the oriented prediscretization coset spaces is injective.

The same injectivity statement holds for both free pro-$2$ test coverings, with geometric closure taken in the pro-$2$ outer automorphism group. More generally, the finite-$p$-subgroup normalizer equality used below holds in the genus-zero geometric pro-$p$ closure.

**Proof and reduction to the cited theorem.** The substantive external input is Boggi and Zalesskii (2025, Theorem A(iii), equivalently Theorem 4.3 in the version read): in the profinite completion of a residually finite, good group of finite virtual cohomological type, the normalizer of a finite $p$-subgroup is the closure of its discrete normalizer. Apply this with $p=2$ to the genus-zero mapping class group of the upstairs surface and the deck subgroup $D=C_2$ or $C_2^2$. The needed goodness follows inductively from the pure genus-zero Birman extensions by finitely generated free groups; these groups and their finite extensions have finite virtual cohomological type. This genus-zero application is also included in the source's discussion preceding §6.1. Genus-zero congruence identifies this completion with $\Sigma(V)$, so
$$
 N_{\Sigma(V)}(D)=\overline{N_{\Gamma(V)}(D)}.           \tag{C.3}
$$
The discrete normalizer descends to the discrete geometric stabilizer downstairs. To see this without assuming a choice of equivariant representatives, apply the discrete version of the proof of C.2. The extension preserves the oriented peripheral classes, so Dehn–Nielsen–Baer identifies it with a geometric mapping class downstairs. Conversely every liftable geometric mapping class lifts to this normalizer. Thus (C.1) identifies $N_{\Gamma(V)}(D)/D$ with the geometric stabilizer downstairs. Taking closures and using (C.3) proves that an element of $A$ whose restriction is in $B'$ already lies in $B$. The reverse inclusion follows by continuity of restriction. Finally apply LM3 B.13 to obtain coset injectivity.

For the pro-$p$ assertion, we check the completion issue explicitly. Put $G=\Gamma_{0,n}$ with labels allowed to permute, $P=P\Gamma_{0,n}$, and let $R$ be its geometric closure in $\operatorname{Out}(F_{n-1}^{(p)})$. Boggi (2020, Corollary 5.4(ii)) identifies the closure of $P$ with its full pro-$p$ completion $P^{(p)}$; his notation $\Gamma(S)$ is pure throughout that paper. The label action on the cusp classes is faithful, so
$$
 1\to P^{(p)}\to R\to S_n\to1
$$
is exact. The map $G\to R$ is injective because $P$ is residually $p$ and the label action detects every nonpure element.

The maps $P\to P^{(p)}$ induce cohomology isomorphisms for every finite continuous $\mathbf F_p[P^{(p)}]$-module. Here is the required goodness argument rather than an appeal to full profinite goodness. Induct on the number of punctures using the free Birman extensions, whose completed pro-$p$ sequences are exact by Boggi's Corollary 4.7 and Corollary 5.4(ii). A finitely generated free group and its free pro-$p$ completion have the same cohomology for these coefficients: both have cohomological dimension one, and a crossed homomorphism to a finite $p$-module extends continuously, since its graph lies in a finite $p$-group extension. The Lyndon–Hochschild–Serre comparison then proves the induction; the kernel cohomology modules are finite and carry the continuous quotient action supplied by the completed extension. A second comparison across the common finite quotient $S_n$ proves
$$
 H^i(R,M)\xrightarrow{\sim}H^i(G,M)
$$
for every finite continuous $\mathbf F_p[R]$-module $M$ and every $i$. The pure groups have finite classifying complexes and $G$ is virtually of that type, hence of type $\mathrm{FP}_{\infty}$. Group cohomology therefore commutes with filtered unions of these finite modules. Continuous profinite cohomology does also; every discrete $\mathbf F_p[R]$-module is the union of its finite-dimensional $R$-stable submodules. Thus the comparison holds for all discrete modules required by Boggi–Zalesskii (2025, Theorem A, or Theorem 4.3), not only finite ones. The same finite-type argument verifies finite virtual $p$-cohomological type.

That theorem applies to this arbitrary dense embedding $G\hookrightarrow R$, and gives $N_R(H)=\overline{N_G(H)}$ for every finite $p$-subgroup $H\subset G$. Taking $p=2$ and the relevant deck subgroup gives the pro-$2$ analogue of (C.3). Discrete descent and continuity now prove the asserted pro-$2$ injectivity, and also show that every geometric pro-$2$ normalizer of a deck subgroup descends geometrically. $\square$

The normalizer theorem is not a statement that every outer automorphism upstairs can be adjusted geometrically to normalize the deck group. That is the separate surjectivity condition below.

## C.4. Proved — A degree-three obstruction in the rational graded comparison

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


Let $\mathfrak o_r$ be the graded Lie algebra of special outer derivations of the free Lie algebra on $r$ generators over a characteristic-zero field. For the index-two cover, the degree-three deck-fixed subspace and geometric subspace satisfy
$$
 \dim\mathfrak o_{3,3}=6,\quad
 \dim\mathfrak o_{3,3}^{C_2}=4,\quad
 \dim\mathfrak p_{0,4,3}=2,\quad
 \dim(\mathfrak o_{3,3}^{C_2}+\mathfrak p_{0,4,3})=5.
                                                               \tag{C.4}
$$
For the degree-four cover,
$$
 \dim\mathfrak o_{5,3}=50,\qquad
 \dim\mathfrak o_{5,3}^{C_2^2}=17,\qquad
 \dim\mathfrak p_{0,6,3}=30,
                                                               \tag{C.5}
$$
so the corresponding sum has codimension at least three. These are statements about graded vector spaces; they do not assert a factorization theorem or its negation for the full pro-$2$ automorphism groups.

**Proof and computation.** Let $W$ be the standard $r$-dimensional representation of the permutation group on the $r+1$ punctures. In degree $n\geq2$, the exact special-derivation complex, after quotienting inner derivations, gives the virtual character
$$
 [\mathfrak o_{r,n}]=[W\otimes L_n(W)]-[L_{n+1}(W)].   \tag{C.6}
$$
The character of a free Lie power is
$$
 \operatorname{tr}(g\mid L_n(W))=
 \frac1n\sum_{d\mid n}\mu(d)\operatorname{tr}(g^d\mid W)^{n/d}.
$$
For the index-two cover, the deck involution fixes two punctures and interchanges the other two. For the degree-four cover, each nonidentity deck element fixes two punctures and interchanges the other four in two pairs. Thus the trace on $W$ is one in both cases; its even powers have trace $r$. Equations (C.6) and character averaging give (C.4)–(C.5), except for the sum rank in (C.4), which was independently checked by rational matrices in `ceh_checks.py`, using the independent Lyndon implementation of Part A. The deck action on the six-dimensional degree-three space has matrix
$$
 \begin{pmatrix}
0&0&1&0&0&0\\0&1&0&0&0&0\\1&0&0&0&0&0\\
0&0&0&0&-1&0\\0&0&0&-1&0&0\\0&0&0&0&0&1
\end{pmatrix}.
$$
Adjoining the two point-pushing columns to its four-dimensional fixed subspace gives rank five. The pure sphere Lie dimensions used here are $\sum_{j=2}^{r-1}\dim L_n(\mathbf Q^j)$, obtained from the iterated free Birman extensions. The other computed values are:

| Upstairs type | Degree | Special outer | Deck-fixed | Geometric |
|---|---:|---:|---:|---:|
| $(0,4)$ | 2 | 1 | 0 | 1 |
| $(0,4)$ | 3 | 6 | 4 | 2 |
| $(0,4)$ | 4 | 6 | 2 | 3 |
| $(0,6)$ | 2 | 10 | 1 | 10 |
| $(0,6)$ | 3 | 50 | 17 | 30 |
| $(0,6)$ | 4 | 126 | 27 | 81 |

All ranks are exact over $\mathbf Q$. $\square$

## C.5. Refuted — Surjectivity for the index-two pro-$2$ cover

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


For the index-two covering in C.1, after replacing both geometric fundamental groups by their free pro-$2$ completions, the coset map is **not surjective**. In particular,
$$
 \operatorname{Out}_{\rm lac}(V_2^{(2)})
 \ne N_{\operatorname{Out}_{\rm lac}(V_2^{(2)})}(D)\,
       \Sigma(V_2^{(2)}),\qquad D=C_2.                 \tag{C.7}
$$
This conclusion follows from an actual finite characteristic $2$-group quotient and a special automorphism of the full free pro-$2$ group. It does not use rational averaging or a comparison of dimensions alone.

**The group, deck action, and lift.** Write the downstairs group as $F^{(2)}(a,b)$, with $a\mapsto1,b\mapsto0$ in $C_2$, and use the Schreier basis
$$
 x=aba^{-1},\qquad y=a^2,\qquad z=b
$$
of $V_2^{(2)}$. Its four peripheral classes have generators $x,y,z,P^{-1}$, where $P=xyz=(ab)^2$. Conjugation by $a$ induces the deck representative
$$
 \delta(x)=yzy^{-1},\quad\delta(y)=y,\quad\delta(z)=x,
 \qquad\delta^2=\operatorname{Inn}(y),\quad
 \delta(P)=x^{-1}Px.                                  \tag{C.8}
$$
Let
$$
 R=\mathbf F_2\langle X,Y,Z\rangle/(\text{words of length }\ge5),
 \qquad J=(X,Y,Z),
$$
and let $Q$ be the image of $V_2^{(2)}$ under $x\mapsto1+X$, $y\mapsto1+Y$, $z\mapsto1+Z$. The group $1+J$ has order $2^{120}$, so $Q$ is a finite $2$-group. Its kernel is fully characteristic: substitution of $X,Y,Z$ by arbitrary elements of $J$ preserves the ideal of words of length at least five. This argument also proves that every endomorphism under consideration induces the asserted endomorphism of $Q$; no identification with a differently indexed filtration is needed. Ordinary fifth commutators map to $1$ in $Q$.

Take the integral special derivation whose conjugators are
$$
 a_x=[[X,Y],Y],\qquad a_y=[X,[X,Y]],\qquad a_z=0.
$$
Jacobi gives $[a_x,X]+[a_y,Y]=0$. By A.1 this lifts to an actual special automorphism $\alpha$ of $V_2^{(2)}$ fixing $P$. Begin the lift with the group commutators $A_x=[[x,y],y]$, $A_y=[x,[x,y]]$, $A_z=1$. All subsequent corrections change generator images only in $\gamma_5$, so they disappear in $Q$. Hence the induced automorphism is exactly
$$
 \alpha(X)=X+h,\qquad\alpha(Y)=Y+h,\qquad\alpha(Z)=Z,
 \qquad h=X^2Y^2+Y^2X^2.                              \tag{C.9}
$$
It is an involution on this finite quotient. The finite candidate is therefore realized in the required infinite pro-$2$ automorphism group.

**The full geometric comparison.** The pure four-puncture geometric group is generated, modulo inner automorphisms, by the two adjacent pair twists
$$
 t_1:(x,y,z)\longmapsto
 ((xy)x(xy)^{-1},(xy)y(xy)^{-1},z),
$$
$$
 t_2:(x,y,z)\longmapsto
 (x,(yz)y(yz)^{-1},(yz)z(yz)^{-1}).                    \tag{C.10}
$$
These are the usual squares of the adjacent Artin generators; the pure three-strand braid group modulo its central full twist is generated by their outer classes. Thus their finite image gives the entire pure geometric image relevant here. Exact closure under these two generators in $\operatorname{Aut}(Q)$ has order $128$; its conjugation orbit of $\delta$ has $64$ elements.

It suffices to compare this pure image. The permutation of the four cusp labels induced by $\delta$ is $(xz)$. If $\alpha D\alpha^{-1}=\sigma D\sigma^{-1}$ for a geometric $\sigma$, then the label permutation of $\sigma$ centralizes $(xz)$. This centralizer is generated by $(xz)$ and $(y\infty)$. Both have geometric representatives commuting with $D$: in the original cover coordinate $w$ these are $w\mapsto-w$ and $w\mapsto1/w$. Multiplying $\sigma$ by a suitable such representative makes it pure without changing its deck conjugate. This accounts for every geometric label permutation.

**The finite certificate.** For each of the $64$ geometric deck conjugates $\beta=t\delta t^{-1}$, the program tests the necessary condition for inner equality
$$
 c\,\beta(x_i)=(\alpha\delta\alpha^{-1})(x_i)c
 \quad(i=1,2,3),\qquad
 c=1+\sum_{1\le |w|\le3}c_w w.                       \tag{C.11}
$$
There are $39$ unknowns $c_w\in\mathbf F_2$. Every group conjugator belongs to $1+J$; its degree-four terms commute with all generator images modulo $J^5$ and can be omitted. Therefore inconsistency even for arbitrary units of the displayed form rules out every inner group conjugator.

All $64$ systems are inconsistent. The C++ search records an explicit sum of coefficient equations giving $0=1$ for each system. An independent Python program reconstructs the automorphisms from group commutators using sets of literal words, verifies the whole geometric orbit and its closure, and checks each recorded sum by addition only. It does not reuse the C++ Gaussian elimination. To make the certificate interpretable, write $\rho_i(w)$ for the coefficient equation of the word $w$ in the $i$th equation of (C.11). The $64$ certificates use just the following five patterns; the sum of the listed equations has zero left side and right side one.

| Equations added | Number of geometric deck conjugates |
|---|---:|
| $\rho_x(XZ),\rho_y(XY)$ | 32 |
| $\rho_x(XXZ),\rho_y(XXY)$ | 16 |
| $\rho_x(XZ),\rho_x(XYZ),\rho_y(XYY)$ | 8 |
| $\rho_x(XXZ),\rho_x(XXYZ),\rho_y(XXYY)$ | 4 |
| $\rho_x(XXZZ),\rho_y(XXZY)$ | 4 |

For example, for $\beta=\delta$ the three equations in the fourth row are $c_{XX}=0$, $c_{XX}+c_{XXY}=0$, and $c_{XXY}=1$, an immediate contradiction. The file `ceh_pro2_certificates.json` specifies a twist word and the applicable certificate for every orbit element. The search also tested all $64$ sums of the six integral special degree-three basis vectors supplied in Part A; exactly $32$ have no intertwiner to any geometric deck conjugate. Only the explicit witness (C.9) is needed for the theorem.

If $\alpha$ belonged to $\Sigma N(D)$, its conjugate of $D$ would be geometrically conjugate to $D$, contrary to (C.11). Inversion gives failure of $N(D)\Sigma$ as well; the finite image of $\alpha^{-1}$ is the same involution. By C.2 this is precisely the failure of covering coset surjectivity. This proves (C.7). The reproducible programs are `ceh_pro2_cover.cpp` and `ceh_pro2_verify.py`; their exact outputs and all dual certificates accompany the paper. $\square$

## C.6. Proved — Arithmetic-image quotients are unchanged over the field of definition

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


Let $Y\to X$ be a finite étale cover of affine hyperbolic curves defined over a number field $K$, and use compatible geometric base points, allowing inner ambiguity. Write $\Gamma^{\rm arith}_{X,K}$ and $\Gamma^{\rm arith}_{Y,K}$ for the §29 arithmetic-image quotients with arithmetic group $G_K$. Under the geometric/arithmetic intersection theorem used in LM3 C.5 and E.2, restriction identifies both quotients with $G_K$, and the comparison is the identity of $G_K$.

**Proof.** In the downstairs arithmetic-image group, first take the stabilizer of the chosen geometric covering. Its geometric subgroup is the liftable subgroup of $\Sigma_X$, and its quotient still maps onto $G_K$: the cover defined over $K$ supplies the compatible $G_K$ action. Restriction carries this geometric subgroup into $\Sigma_Y$ and the arithmetic action to that of $Y$. We do not restrict every element of the full geometric mapping class group unless it stabilizes the cover. The exact sequences
$$
1\to\pi_1(X_{\overline K})\to\pi_1(X)\to G_K\to1,
\qquad
1\to\pi_1(Y_{\overline K})\to\pi_1(Y)\to G_K\to1
$$
form a commutative diagram induced by the cover. Conjugation gives the compatible outer actions, and hence the compatible arithmetic-image groups. Hoshi–Mochizuki (2011, Corollary 6.4), with the reduction already proved in LM3 C.5, says that quotienting those images by their geometric parts loses no element of $G_K$. Thus the map on the quotients is precisely the common map to $G_K$ in the diagram, namely its identity. Changing compatible base points changes representatives by geometric inner automorphisms and disappears in the quotient. If the cover is defined only over $K$, one must restrict the downstairs arithmetic group to the corresponding open subgroup $G_K\subset G_{\mathbf Q}$; there is no assertion that $G_{\mathbf Q}$ stabilizes that chosen covering. Both test covers admit models over $\mathbf Q$, so they give the full $G_{\mathbf Q}$ comparison. This proves the arithmetic-image version of scan 355, formula (6), and scan 356. $\square$

## C.7. Open — The §26 comparison requires an additional normalizer assertion

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


For the two tripod covers, the already established §26 groups are $\widehat{\mathrm{GT}}_0$ downstairs and $\widehat{\mathrm{GT}}$ upstairs. Restriction from the stabilizer of the covering is defined at the level of loop-preserving automorphisms by C.2. To descend it to the normalizer quotients, one must prove that a downstairs automorphism normalizing $\Sigma(G)$ restricts to an automorphism normalizing **all** of $\Sigma(V)$, rather than merely its subgroup $N_{\Sigma(V)}(D)$. C.3 proves the intersection condition but does not prove this enlargement. The smallest undecided assertion is exactly this implication for $D=C_2$ and $V=V_2$. It is the distinction Grothendieck himself isolates at scan 362. Thus no map $\widehat{\mathrm{GT}}_0\to\widehat{\mathrm{GT}}$ is manufactured by citing the separate identifications of its putative source and target.

## C.8. Proved — Two corrections to the readings at scans 361–363

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


In the normalizer expression at scan 361, the deck group $D$ acts on the upstairs group, so the ambient outer automorphism group must be the one belonging to $\pi'_0$. The alternative downstairs symbol cannot type the displayed normalizer. At scan 363, for $\nu\geq1$, the dimension of mod-two homology is $2g+\nu-1$, so the sign in $2g\unsure{+|-}\nu-1$ is supported as plus. These are mathematical constraints on the transcription, not claims of palaeographic certainty. At $(0,3)$ the minus alternative would give exponent $-4$ and cannot represent the displayed finite elementary abelian deck group; the plus alternative gives the required exponent two. Formula (C.1) also explains why a quotient by deck transformations appears only after passing to outer automorphisms.

## C.9. Open — The exact remaining covering cases

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


For the full profinite groups, covering surjectivity remains undecided here for both $V_2$ and $V_4$. In the notation of C.3, the exact assertion is $A'=f(A)B'$, equivalently $\operatorname{Out}_{\rm lac}(V)=N(D)\Sigma(V)$. The negative pro-$2$ answers are C.5 and C.10. A.1 does not lift the automorphism of C.5 from the free pro-$2$ group to the free profinite group, so those answers do not settle the full profinite cases. An exact remaining route is to realize a full profinite special automorphism whose pro-$2$ image has the finite obstruction (C.9), or to construct another obstruction directly in full finite quotients. We have supplied neither such realization nor a full profinite factorization theorem.

## C.10. Refuted — Surjectivity for the degree-four pro-$2$ cover

*Manuscript connection: §28;179–183;355–363.*

\nopagebreak[4]


For the characteristic degree-four cover $W=V_4^{(2)}$ of the tripod, with deck group $D_4=C_2^2$, one likewise has
$$
 \operatorname{Out}_{\rm lac}(W)\ne
 N_{\operatorname{Out}_{\rm lac}(W)}(D_4)\Sigma(W).
                                                               \tag{C.12}
$$
This is a transfer of the concrete certificate in C.5, using the pro-$2$ geometric-normalizer descent proved in C.3. No direct enumeration in rank five is claimed.

**Proof.** Use the intermediate tower
$$
 W\subset V=V_2^{(2)}\subset G=F_2^{(2)},\qquad
 E=V/W\subset D_4=G/W.
$$
The automorphism $\alpha$ of C.5 acts trivially on abelianization, so preserves $W$, which is the kernel in $V$ of the mod-two character $x\mapsto1$, $y\mapsto0$, $z\mapsto1$. Let $\alpha_W$ denote its restricted outer class. It normalizes $E$ by C.2.

Suppose that $\alpha_W=n\sigma$ with $n\in N(D_4)$ and $\sigma\in\Sigma(W)$. Then
$$
 \sigma E\sigma^{-1}=n^{-1}En=:E',
$$
where $E'$ is another order-two subgroup of $D_4$. The geometric normalizer of $D_4$ acts transitively on its three order-two subgroups: every downstairs tripod permutation lifts because this cover is characteristic, and its action on $D_4=H_1(G,\mathbf F_2)$ is the full $\mathrm{GL}_2(\mathbf F_2)=S_3$. Choose $t\in N_{\Sigma(W)}(D_4)$ with $tEt^{-1}=E'$. The factors
$$
 n'=nt,\qquad \sigma'=t^{-1}\sigma
$$
both normalize $E$; moreover $n'$ still normalizes $D_4$. The quotient isomorphism of C.2 for $W\subset V$ now descends $n'$ to an outer automorphism of $V$ normalizing $D_4/E$, while C.3 descends $\sigma'$ to an element of $\Sigma(V)$. Their product is the outer class of $\alpha$. Since $D_4/E$ is exactly the index-two deck group of C.5, this is the factorization ruled out there. The contradiction proves (C.12). $\square$



# D. Loop structures, arithmetic subgroups, and sections

In D.1--D.5, $K$ is a number field and $U/K$ is a smooth geometrically connected affine hyperbolic curve of type $(g,n)$, $\Delta=\pi_1(U_{\overline K})$, and $\Pi=\pi_1(U)$. All subgroups are closed and all homomorphisms are continuous. The later category and centralizer statements allow proper hyperbolic curves as well. A *loop structure of type $(g,n)$* means the image, under an automorphism of $\Delta$, of its standard collection of $n$ conjugacy classes of peripheral procyclic subgroups. This hypothesis is substantially stronger than specifying one arbitrary procyclic subgroup. We write $\chi_K:G_K\to\widehat{\mathbb Z}^{\times}$ for the cyclotomic character. We inspected scans 479 and 483--488. The first assertion of scan 483 concerns a whole loop structure; the subsequent proposed normalizer test concerns individual subgroups. They require separate conclusions.

## D.1. Proved — the determinant of a peripheral automorphism

*Manuscript connection: 34;245;483.*

\nopagebreak[4]


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

## D.2. Proved — a useful strengthening of cyclotomic recognition

*Manuscript connection: 34;245;483.*

\nopagebreak[4]


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

There is a stronger single-prime formulation. It suffices that (D.2) hold for one nontrivial pro-$\ell$ component. Let $z_\ell$ generate that component of $L$ and intersect $N$ with the kernel of its finite twist. Its normalizer action on $\overline{\langle z_\ell\rangle}$ is then exactly cyclotomic, so Nakamura's Theorem 2.1.1, applied to the element $z_\ell$ in the *full* profinite group, puts it in actual inertia $I$. Since $L$ centralizes $z_\ell$, Boggi and Zalesskii (2019, Proposition 3.6) gives $L\subseteq I$. That proposition allows every nonzero profinite exponent, including an exponent supported at a single prime; this qualification is needed here. The geometric pro-$\ell$ version also follows: Nakamura's Theorem 2.1.1 and Lemma 2.1.4 are stated for every full class $\mathcal C$ of finite groups, so one takes $\mathcal C$ to be the finite $\ell$-groups, retains $n\geq1$ and $2g+n>2$, and uses the geometrically pro-$\ell$ arithmetic extension defined in his §2.1. This does not deduce the pro-$\ell$ assertion merely by quotienting a full-profinite cover.

## D.3. Proved — uniqueness of the invariant loop structure for every affine hyperbolic type

*Manuscript connection: 34;245;483.*

\nopagebreak[4]


The genuine cuspidal loop structure of $U$ is the unique loop structure of type $(g,n)$ on $\Delta$ invariant under $\rho_U(G_K)$. In particular, this settles the first half of LM3 D.23 at $(1,1)$ and for every affine hyperbolic curve over a number field, in the specified meaning of loop structure. It proves the first conjectural sentence beginning “Ce n'est pas la peine” in §34, folio 245, scan 483.

**Proof.** After finite extension, both the actual and the candidate sets of peripheral classes are individually fixed. Put $d=g+n-1>0$. For the actual Galois action,
\[
 \det\bigl(\rho_U(\sigma)\mid\Delta^{\mathrm{ab}}\bigr)
 =\chi_K(\sigma)^{g+n-1}.
\]
Indeed, the boundary module has rank $n-1$ and scalar action $\chi_K$; the Jacobian Tate module has a perfect alternating pairing with multiplier $\chi_K$, hence determinant $\chi_K^g$. On the other hand, D.1 applied to the candidate loop structure computes the very same determinant as $\lambda(\sigma)^d$. If $I$ is one chosen candidate subgroup, its arithmetic normalizer maps onto the restricted $G_K$: invariance of its conjugacy class lets us correct any lift of a Galois element by an element of $\Delta$. On this normalizer, D.1 gives $\psi^d=\chi_K^d$, including on its geometric kernel. D.2 therefore places a generator of $I$ in actual inertia. A candidate peripheral subgroup is maximal procyclic, since this is true of standard peripheral subgroups and is invariant under automorphisms; see Boggi and Zalesskii (2019, Proposition 3.6). Thus $I$ equals that actual inertia subgroup. The $n$ candidate conjugacy classes are distinct, so they exhaust the $n$ genuine classes. Finite base extension does not change the geometric inertia collection. $\square$

For $(1,1)$ one can shorten the argument. Here $\Gamma_2\Delta/\Gamma_3\Delta\simeq\widehat{\mathbb Z}$ and the candidate commutator has a unit coefficient. The action on this quotient is the determinant of $\widehat T E$, namely $\chi_K$. The normalizer exponent is therefore exactly cyclotomic before any finite twist is removed. This proof closes the specific missing step identified in LM3 D.23; the fact that the peripheral commutator has zero abelianization is not an obstruction in degree two.

## D.4. Open — the bare maximal-procyclic normalizer criterion

*Manuscript connection: 34;245;483.*

\nopagebreak[4]


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

## D.5. Refuted — the corresponding criterion on the class-two pro-5 quotient

*Manuscript connection: 34;245;483.*

\nopagebreak[4]


The analogue of D.4 becomes false after replacing $\Delta$ by its class-two pro-$5$ quotient. Take $E:y^2=x^3-x$ over $K=\mathbb Q(i)$ and $U=E\setminus\{O\}$. Since $5$ splits in $\mathbb Z[i]$, the module $T_5E$ is the direct sum of two primitive $G_K$-stable rank-one summands. Choose a free pro-$5$ basis $x,y$ whose abelianizations are bases of these summands, and write
\[
 N=\Delta^{(5)}/\Gamma_3\Delta^{(5)},\qquad c=[x,y].
\]
For any arithmetic lift of $\sigma$, the image of $x$ has the form $x^{\alpha(\sigma)}c^{t(\sigma)}$, where $\alpha(\sigma)\in\mathbb Z_5^{\times}$. Conjugating by a suitable power of $y$ cancels the central factor because $\alpha(\sigma)$ is a unit. Hence $\langle x\rangle\simeq\mathbb Z_5$ has arithmetic normalizer with full image in $G_K$. It is maximal procyclic by its primitive abelianization and cannot be peripheral: the genuine cusp is generated by $[x,y]$ and has zero abelianization.

The basis exists by lifting a $\mathbb Z_5$-basis to two elements of the free pro-$5$ group and using the Frattini criterion. The explicit Heisenberg calculation, including the required division by a unit, is checked in `code/dg_checks.py` modulo $5$, $25$, and $125$. This is a counterexample on a specified nilpotent quotient, not on the full pro-$5$ or profinite fundamental group. Beyond class two, compatible conjugators and compatible cyclic generators must be constructed; neither the CM decomposition nor this calculation supplies them.

## D.6. Known — Pop's answer using birational localization

*Manuscript connection: 33bis;242verso;479.*

\nopagebreak[4]


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

## D.7. Known — the Hoshi–Mochizuki–Tsujimura characterization

*Manuscript connection: 33bis;242verso;479.*

\nopagebreak[4]


Let $P_2=\pi_1(\operatorname{Conf}_2(U_{0,\overline{\mathbb Q}}))=\pi_1(\mathcal M_{0,5,\overline{\mathbb Q}})$. Under the standard identification of the genus-zero tower automorphism group with $\widehat{\mathrm{GT}}$, the $\widehat{\mathrm{GT}}$-conjugates of the arithmetic subgroup are exactly the inclusion-maximal closed subgroups satisfying the AA-property of Hoshi, Mochizuki, and Tsujimura (2025, Definition 5.12). This is their Theorem C(ii), equivalently Theorem 5.17(ii), transported to Grothendieck's normalizer quotient.

**Reduction and retained data.** Their Corollary 4.5 and Remark 4.5.1 reconstruct the relevant containers from the abstract profinite group $P_2$. A subgroup $B$ first has to satisfy the COF and RGC conditions of Definition 3.3: common dominating arithmetic Belyi diagrams must exist, and geometric dominations between such diagrams are unique. These diagrams include finite étale covers, open immersions, the associated second configuration groups, their fibre subgroups, and the appropriate cuspidal quotients. Theorem A constructs a set $Q_B$ with operations; the ArBC condition says these operations make it an algebraic closure of $\mathbb Q$. Definition 5.12 then quantifies over all normal open subgroups of the reconstructed groups and all finite sets of cusps. It imposes the specified Kummer nondegeneracy and restriction-injectivity conditions, a compatible family of function fields obtained from cusp-evaluation functions, and compatibility of the resulting geometric group identification with the second configuration group. Thus the AA condition is a predicate on rich group-theoretic data extracted using $P_2$, not the assertion that an automorphism of two isolated groups preserves five arrows.

Theorem 5.15(iv) places any such subgroup inside a $\widehat{\mathrm{GT}}$-conjugate of $G_{\mathbb Q}$. The arithmetic subgroup itself satisfies AA (Remark 5.12.1, or Theorem 6.8 for $K=\mathbb Q$). Theorem 5.17(ii) then gives the maximality characterization. This proves the exact translated assertion; a chosen arithmetic marking is still needed to select one subgroup from its conjugacy class. No claim that all of $\widehat{\mathrm{GT}}$ is AA is made. The refinement in Theorem C(i) uses QAA and conjugacy in the larger label-preserving outer automorphism group.

## D.8. Proved — the arithmetic subgroup is self-commensurating in the label-preserving container

*Manuscript connection: 34;245/246 verso (folio uncertain);486.*

\nopagebreak[4]


Let $A\subseteq\operatorname{Out}(\widehat F_2)$ be the subgroup fixing each of the three genuine peripheral conjugacy classes, and use the standard arithmetic embedding $G_{\mathbb Q}\subseteq A$. Then
\[
 \operatorname{Comm}_{A}(G_{\mathbb Q})=G_{\mathbb Q}. \tag{D.4}
\]
In the full outer automorphism group the same argument gives $\operatorname{Comm}(G_{\mathbb Q})=G_{\mathbb Q}\mathfrak S_3$, with the standard commuting geometric $\mathfrak S_3$.

**Proof.** A commensurating element induces, by conjugation, an isomorphism between two open subgroups of $G_{\mathbb Q}$. These are absolute Galois groups of number fields. Uchida's isomorphism theorem (1979, main theorem, applied to algebraic closures) realizes the isomorphism by a field automorphism $\sigma\in G_{\mathbb Q}$. After multiplying by its inverse, our element centralizes $\rho(G_L)$ for one number field $L$. The full profinite Isom consequence of Mochizuki (1999, Theorem A = Theorem 16.5) identifies this centralizer with $\operatorname{Aut}_L(U_0)=\mathfrak S_3$: a commuting outer automorphism gives an isomorphism of the centre-free arithmetic extension over $G_L$, then the Isom theorem applies. The label-preserving subgroup intersects this $\mathfrak S_3$ trivially. This proves (D.4). Conversely arithmetic conjugation and the six geometric automorphisms visibly commensurate the arithmetic group. $\square$

Hoshi–Mochizuki–Tsujimura (2025, Theorem 6.8(ii)) gives the corresponding containment inside $\widehat{\mathrm{GT}}$ in the substantially wider TKND-AVKF setting. For number fields the proof above supplies the exact reduction requested here. The same argument proves that the centralizer of every open subgroup of either $\widehat{\mathrm{GT}}$ or $\widehat{\mathrm{GT}}_0$ in that container is trivial: intersect the open subgroup with $G_{\mathbb Q}$ and apply the label-preserving form of the centralizer calculation. This supplies the centralizer assertion used in the marginal insertion of §34, scan 486, without identifying the whole container with $G_{\mathbb Q}$.

## D.9. Proved — a precisely typed geometric-section stabilizer equals the arithmetic image

*Manuscript connection: 33bis-35;242verso and247;479,487-488.*

\nopagebreak[4]


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

## D.10. Known — Kummer and Nakamura–Schneps data retained by the stabilizer

*Manuscript connection: 35;247;487-488.*

\nopagebreak[4]


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

## D.11. Known — centralizers for curves of the requested types

*Manuscript connection: 34;245/246 (folio uncertain);485-486.*

\nopagebreak[4]


For every hyperbolic curve $U/K$ over a number field,
\[
 C_{\operatorname{Out}(\Delta_U)}(\rho_U(G_K))=\operatorname{Aut}_K(U). \tag{D.6}
\]
The proof is the centre-free extension construction followed by Mochizuki (1999, Theorem A/16.5), exactly as in D.8. Conversely functoriality sends every $K$-automorphism to the centralizer. The two constructions are inverse by the Isom theorem, so this is an equality of naturally identified groups, not just an injection.

For type $(0,4)$ or $(0,5)$, write $C$ for the genus-zero compactification and $D=C\setminus U$ for its reduced puncture divisor. The answer is $\operatorname{Aut}_K(C,D)$. When $C\simeq\mathbb P^1_K$, it is the subgroup of $\operatorname{PGL}_2(K)$ preserving $D$. A type $(0,4)$ compactification can be a nonsplit conic, so this qualification matters. For type $(0,5)$ the odd-degree divisor $D$ forces the conic to split: its degree-two canonical class and $D$ give a divisor class of degree one, whose Riemann--Roch space supplies a $K$-point. A generic rationally marked quadruple has the Klein four-group: the action of $\mathfrak S_4$ on its cross-ratio factors through $\mathfrak S_3$ with that kernel, and a generic cross-ratio has trivial stabilizer in the latter. A generic rationally marked quintuple has trivial group, since each nonidentity permutation imposes a proper algebraic equality among its cross-ratios.

For $(1,1)$ the unique missing point is $K$-rational and identifies the compactification with an elliptic curve $(E,O)$. Its answer is $\operatorname{Aut}_K(E,O)$. In a short Weierstrass equation $y^2=x^3+Ax+B$, an automorphism fixing $O$ has the form $(x,y)\mapsto(u^2x,u^3y)$, with $u\in K^{\times}$, $u^4A=A$ and $u^6B=B$. Consequently the group is $\mu_2(K)$ if $AB\ne0$, $\mu_4(K)$ if $B=0$, and $\mu_6(K)$ if $A=0$. These curve statements depend on the curve and must not be confused with the symmetric groups in the following moduli-space statement.

## D.12. Known — Nakamura's moduli centralizers

*Manuscript connection: 34-35;245/246 (uncertain) and247;485-488.*

\nopagebreak[4]


For an odd prime $\ell$ and $m\geq4$, Nakamura (1994, Theorem A) gives
\[
 C_{\operatorname{Out}(\pi_1^{(\ell)}(\mathcal M_{0,m,\overline K}))}
       (\rho(G_K))
 \simeq\begin{cases}\mathfrak S_3,&m=4,\\\mathfrak S_m,&m\geq5.\end{cases}
\]
His Theorem B gives $C_{\operatorname{Out}(L_\ell(\Gamma_0^m))}(\rho^{\mathrm{Lie}}(G_K))=\mathfrak S_m$ for $m\geq5$, where $L_\ell(\Gamma_0^m)$ is the inverse limit of the $\mathbb Q_\ell$ Lie algebras associated to the nilpotent quotients of the pure sphere mapping class group, as defined in his §4.2.2. In Grothendieck's notation these are arithmetic-compatible symmetries of the indicated geometric modular groups. To pass from Theorem A's arithmetic-automorphism formulation to the displayed centralizer, use the centre-freeness of the geometric group: an extension with centre-free kernel is the pullback of $\operatorname{Aut}(P)\to\operatorname{Out}(P)$ along its outer action. An automorphism over $G_K$, modulo conjugation by $P$, is therefore exactly a commuting outer automorphism of $P$. The six automorphisms of the tripod, or permutations of $m$ labels for $m\geq5$, are defined over $\mathbb Q$ and supply the full listed centralizer. The theorem has an odd-prime hypothesis; it is not silently extended to $\ell=2$ or to arbitrary elliptic pro-$\ell$ groups.

## D.13. Known — the category statement in §34

*Manuscript connection: 34;245verso;484.*

\nopagebreak[4]


Fix $K$ and let the objects be arithmetic fundamental-group extensions of hyperbolic curves over $K$, retaining the augmentation to $G_K$. The category with dominant morphisms is fully faithfully described by open continuous $G_K$-homomorphisms of these extensions, modulo inner automorphisms of the target geometric kernel. This is Mochizuki (1999, Theorem A/16.5), applied with source and target smooth curves. The comparison is covariant on fundamental groups, and both composition and identity are respected by functoriality; bijectivity on each Hom set gives a category equivalence onto the essential image.

To include constant morphisms one must additionally retain the *geometric* point sections of the target: a constant $K$-map is exactly a choice of a $K$-point, and its group map factors through $G_K$. Distinct geometric point sections are distinguished by the injectivity part of the section theorem (Mochizuki, Theorem C); replacing them by all abstract sections would require a section-surjectivity assertion and is not justified here. Tangential sections are retained as boundary data, not identified with interior constant maps. This supplies the precise category description supported by the cited theorems, while the arithmetic-free recognition of all admissible objects and splittings remains a separate problem. The exceptional nonhyperbolic types have nontrivial or trivial geometric kernels and do not satisfy this description; the real and nonorientable topological variants are not substitutes for the stated number-field algebraic category.

## D.14. Proved — an explicit essential-image construction from the arithmetic tripod

*Manuscript connection: 34;245verso;484.*

\nopagebreak[4]


Allow the finite number field to vary inside $\overline{\mathbb Q}$. Starting from the arithmetic tripod extension $\Pi_0\to G_{\mathbb Q}$, take an open subgroup $E'\subseteq\Pi_0$ and then quotient by the closed normal subgroup generated by a Galois-stable collection of its geometric peripheral subgroups. Retain only hyperbolic resulting types. The resulting arithmetic extensions are exactly those of hyperbolic curves over number fields, up to isomorphism over their projected open subgroup of $G_{\mathbb Q}$. With the arrows of D.13 this is the essential-image description proposed immediately after scan 483, in §34, scan 484.

**Proof.** Write $p(E')=G_K$. Galois theory of finite étale covers identifies $E'$ with the arithmetic group of a geometrically connected finite étale cover $V\to U_{0,K}$. The normalization of $\mathbb P^1_K$ in $K(V)$ is its unique smooth proper compactification. A Galois-stable subset of its geometric boundary is a divisor defined over $K$; adjoining precisely those missing points gives a smooth curve $U/K$. The fundamental group of $U$ is the quotient of that of $V$ by the closed normal closure of the inertia subgroups at the filled points. Indeed a finite cover of $V$ extends étale across those points exactly when those local inertia groups act trivially. This proves one direction and types the quotient map explicitly.

Conversely, let $C/K$ be the smooth proper compactification of $U$. Choose any nonconstant $f\in K(C)$, and let $S\subseteq\mathbb P^1(\overline{\mathbb Q})$ contain its branch values and $f(C\setminus U)$. Enlarge $S$ to its finite union of $\mathbb Q$-conjugates. Belyi's proof of Theorem 4 (1980, pp. 255--256) constructs polynomial postcompositions in $\mathbb Q[t]$: the first sends $S$ and its own critical values into $\mathbb P^1(\mathbb Q)$, and the second sends that finite rational set and its critical values into $\{0,1,\infty\}$. The construction uses successive minimal polynomials of critical-value sets, whose degrees strictly decrease, followed by the rational polynomials proportional to $t^a(1-t)^b$ for rational $a/(a+b)\in(0,1)$. Thus the composite $b:C\to\mathbb P^1$ is defined over the original $K$, is branched only over $\{0,1,\infty\}$, and sends the boundary into that set. Removing $b^{-1}\{0,1,\infty\}$ gives a finite étale cover $V\to U_{0,K}$ with $V\subseteq U$. Its arithmetic group is an open $E'\subseteq\Pi_0$ projecting onto $G_K$, and filling the extra removed points recovers $U$. No enlargement of $K$ or additional descent datum is needed. $\square$

The insertion “morphismes les morphismes dominants” in the transcription at scan 484 is mathematically consequential: it matches precisely the open-Hom theorem used in D.13. Neither possible handwriting variant “extérieur/extérieure” changes this statement. The construction uses an identified arithmetic tripod, supplied for example by D.6 or the marked form of D.7; it does not identify every abstract action on a surface group as geometric.



# E. Elliptic types, coherence, and the whole outer tower

This part concerns the proposed type-independence in §§30–33 bis, notably folios 188–202, scans 371, 376, 395–400, and the modular constructions of §26, folios 165–166 (the latter reading is doubtful), scans 326–329. We keep the distinction between a natural automorphism of an outer group-valued functor and a coherent automorphism of boundary categories with specified paths and clutching data.

## E.1. Proved — The exact remaining $(1,2)$ inertia condition

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


Put $E=\widehat{P\Gamma}_{1,3}$ and let $A\subset\operatorname{Out}(E)$ be the subgroup of LM3 E.11: it preserves the universal-curve fibre $\widehat\pi_{1,2}$, its two cusp classes with one exponent, and normalizes the transposition of the two original marks. Let $A^I$ be the subgroup which in addition preserves the conjugacy class of a nonseparating twist subgroup. Then
$$
 A^I/S_2\cong\widehat{\mathrm{GT}}.                    \tag{E.1}
$$
Consequently the requested equality $\Gamma^{\rm norm}_{1,2}=\widehat{\mathrm{GT}}$ is equivalent to $A=A^I$ under the known normalizer reduction and the known tower inclusion.

**Proof.** Genus-one congruence lets us replace $E$ by its procongruence completion. Boggi (2026, Theorem 3.12) turns preservation of nonseparating twist inertia into preservation of all twist inertia; his Theorem A(ii), applied to $(1,3)$, identifies the resulting outer group with $S_3\times\widehat{\mathrm{GT}}$. The condition of preserving the chosen fibre singles out the stabilizer of the third label, namely $S_2$, in the permutation factor. Normalizing the transposition imposes no further condition inside that stabilizer, and the GT factor commutes with it. Quotienting gives (E.1). Conversely the GT action in Boggi's Theorem 6.7 is compatible with the relevant forgetting maps and preserves all peripheral twist subgroups, hence gives the known inclusion into $A/S_2$. Thus equality can fail only through an element of $A$ outside the inertia-preserving subgroup. $\square$

The equality $A=A^I$ is the separate open assertion E.9. The proved identification (E.1) does not establish that automatic-inertia assertion.

## E.2. Proved — The automorphism 2-group of the open elliptic forgetting arrow

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


Consider the diagram of one-object profinite groupoids
$$
 B G_2\xrightarrow{Bq}B G_1,
\qquad
G_2=\widehat{P\Gamma}_{1,2},\quad G_1=\widehat{P\Gamma}_{1,1},
$$
where $q$ forgets the second mark. Automorphisms mean invertible pseudonatural transformations, modulo modifications. Its automorphism 2-group has
$$
 \pi_0\cong\widehat{\mathrm{GT}},\qquad \pi_1=1.       \tag{E.2}
$$

**Proof.** For a general epimorphism $q:G_2\to G_1$, a pseudonatural automorphism is represented by automorphisms $\phi_2,\phi_1$ and $h\in G_1$ with $\phi_1q=\operatorname{Inn}(h)q\phi_2$, up to the corresponding inner modifications. Choose a lift of $h$ in $G_2$; modification by it makes the compatibility strict. We obtain
$$
 \pi_0\cong\operatorname{Out}(G_2;\ker q),\qquad
 \pi_1\cong Z(G_2),
$$
the second isomorphism sending a central modification $z_2$ to $(z_2,q(z_2))$.

Now $G_2$ is the profinite central quotient of $B_4$. Minamide–Nakamura (2022, Theorem 4.3 and Corollary C) identify its outer automorphism group with GT. Their Proposition 3.2(iii) makes the orbifold fibre $C_2\amalg C_2\amalg C_2$ characteristic. Inside that fibre, the genuine punctured-elliptic fibre is the unique index-two subgroup in which all three involution classes map nontrivially to the quotient: its kernel is free of rank two. This description is invariant under automorphisms, so $\ker q$ is characteristic. Finally $Z(G_2)=1$ by genus-one congruence and Boggi (2020, Theorem 4.4), while $Z(G_1)=C_2$. Hence (E.2). The center at the target creates nonunique representatives of a compatibility isomorphism, but not a surviving $\pi_1$ of this arrow diagram. $\square$

## E.3. Proved — The center does not create a $\pi_1$ for the elliptic boundary pair

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


Use the completed stable-curve transporter categories of LM3 F.15 for $(1,1)$ and $(1,2)$, together with a forgetting functor. The automorphism 2-group of this decorated pair has trivial $\pi_1$. This remains true after adjoining the other forgetting map, relabellings, and the boundary clutching functors.

**Proof.** A natural automorphism of the identity on a transporter category has an open-stratum component in the center of its open group. Once that component is specified, naturality with the smoothing arrow from any stratum to the open stratum determines its component there: postcomposition embeds the transporter Hom-set into the open Hom-set. This is the same transporter argument as LM3 F.12, and does not require trivial centers. For $(1,2)$ the open center is trivial, so the whole natural automorphism is the identity. Compatibility with forgetting then forces the open component at $(1,1)$ to be the identity, because $q$ is onto. The transporter argument forces all its boundary components to be the identity as well. Adding more compatibility requirements takes a subgroup of this already trivial modification group. $\square$

For clarity about $\pi_0$, two *unrelated* forgetting arrows with the same target center $C_2$ would produce two compatibility signs, modulo a common target modification, and hence one residual $C_2$. Coherent relabelling of the two source marks identifies the two signs and kills that residual choice. The finite computation in `ceh_checks.py` verifies these two orbit counts, two and one. This computation explains why the precise morphisms and their relations must be retained; it does not settle every clutching coherence equation.

## E.4. Open — The elliptic boundary and orbifold normalizer comparisons

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


What remains after E.2–E.3 is the following exact assertion. For every $F\in\widehat{\mathrm{GT}}$, its automorphism of $G_2$ must extend to the two transporter categories with induced automorphisms on all normalization factors, with compatibility isomorphisms for forgetting and clutching satisfying their relations; and every such system inducing the identity on $G_2$ must be coherently isomorphic to the identity system. The first step, extension to each individual boundary category, follows once the twist-incidence data are preserved. The remaining step is comparison of the induced genus-zero action at the nonseparating boundary with the prescribed action on its four-point normalization, including the branch-exchange involution, and coherence with the rational-tail boundary carrying $G_1$.

Our attack removes the proposed $\pi_1=C_2$ obstruction and computes the open-arrow 2-group, but does not supply a complete presentation of these remaining clutching relations. In particular, the outer-tower theorem E.7 below cannot by itself be upgraded to a theorem about this finer 2-group. Under the explicitly named **boundary coherence hypothesis** consisting of the preceding existence and uniqueness assertion, one obtains $\pi_0=\widehat{\mathrm{GT}}$ and $\pi_1=1$. Without it, only the latter equality and (E.2) have been proved here.

There is a second, distinct comparison required by Part E(c). In the notation of E.5, put $n_3=1$, $n_4=2$ and
$$
 \widetilde N_r=\{\phi\in\mathcal A_r:
 [\phi]\in N_{O_{0,r+1}}(\Sigma_{0,r+1})\},
 \qquad r\in\{3,4\}.
$$
The quotient and restriction construction gives a genuine homomorphism $\rho_r:\mathcal A_r\to\operatorname{Aut}_{\rm lac}(K_r)$. What remains to prove is the **full geometric-normalizer comparison**
$$
 [\rho_r(\widetilde N_r)]\subseteq
 N_{O_{1,n_r}}(\Sigma_{1,n_r}),
$$
together with descent through the geometric equivalence relations and independence of the choices used to stabilize the distinguished infinity and to lift through the deck quotient. After those steps, the induced comparison of the §26 normalizer quotients must be shown to retain the same GT pair $(\lambda,f)$ under the standard genus-zero and elliptic identifications. Normalization of the deck subgroup, proved in E.5, does not establish normalization of the full elliptic geometric subgroup. Nor does an abstract isomorphism of both quotients with GT establish that their specified comparison is the identity.

For $(1,2)$ the identification of the target quotient with GT is additionally conditional on the automatic-inertia assertion E.9. For $(1,1)$ that identification is already known from LM3 E.10; thus the orbifold comparison between $(0,4)$ and $(1,1)$ is the smallest remaining comparison in this audit. The analogous same-pair comparison for the elliptic filling $(1,2)\to(1,1)$ also remains conditional on E.9 and on construction of its normalizer comparison. The ordinary genus-zero filling is covered by the known comparison recalled in E.5. These residual assertions, rather than the formal descent maps alone, are the unresolved part of E(c).

## E.5. Proved — The orbifold quotient and parity-kernel restriction maps

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


There is no ordinary degree-two étale covering of punctured surfaces $(1,1)\to(0,4)$ or $(1,2)\to(0,5)$. The corresponding elliptic quotients have cone points. For $(1,1)$ the quotient has one cusp and three cone points of order two; its orbifold Euler characteristic is $-1/2$. For two punctures exchanged by the elliptic involution, the quotient has one cusp and four cone points of order two, of orbifold Euler characteristic $-1$. Deleting the cone points produces the four- or five-punctured sphere but also changes the upstairs surface.

For $r=3,4$, the correctly typed group construction is
$$
 F_r=\widehat F(x_1,\ldots,x_r),\qquad
 P=x_1\cdots x_r,\qquad
 J_r=\overline{\langle\!\langle x_1^2,\ldots,x_r^2\rangle\!\rangle},
$$
$$
 q_r:F_r\twoheadrightarrow
 Q_r=F_r/J_r=\underbrace{C_2\amalg\cdots\amalg C_2}_{r\text{ factors}},
 \qquad c_i=q_r(x_i),\quad c=c_1\cdots c_r,
$$
where $\amalg$ denotes the profinite free product. Define
$$
 \epsilon_r:Q_r\twoheadrightarrow C_2,\quad
 \epsilon_r(c_i)=1,\qquad K_r=\ker\epsilon_r.
$$
Then $K_3\cong\widehat\pi_{1,1}$ and $K_4\cong\widehat\pi_{1,2}$, with their induced oriented peripheral structures. Let $\mathcal A_r$ be the subgroup of $\operatorname{Aut}_{\rm lac}(F_r)$ preserving the distinguished infinity class $[\langle P^{-1}\rangle]$. There are continuous homomorphisms
$$
 \mathcal A_r\xrightarrow{q_*}\operatorname{Aut}(Q_r;K_r)
 \xrightarrow{\operatorname{res}_{K_r}}\operatorname{Aut}(K_r),
 \qquad
 \rho_r=\operatorname{res}_{K_r}\circ q_*,
$$
and $\rho_r(\mathcal A_r)\subseteq\operatorname{Aut}_{\rm lac}(K_r)$ with the same orientation multiplier. These are quotient followed by restriction maps, not restriction along an inclusion of the ordinary punctured-sphere group into the elliptic group.

**Proof.** The Euler characteristics of $(1,1),(0,4)$ are $-1,-2$, and those of $(1,2),(0,5)$ are $-2,-3$. They cannot satisfy $\chi(\text{upstairs})=2\chi(\text{downstairs})$. On an elliptic curve, the involution has four fixed points. In the one-puncture case the removed origin accounts for one of them, leaving three order-two cone points. In the exchanged-puncture case no fixed point is removed and the two punctures give one cusp downstairs. Applying the orbifold formula gives the values stated.

The discrete orbifold group is the free product of $r$ copies of $C_2$. Its parity kernel is a torsion-free subgroup of index two, free on the Schreier generators $c_1c_i$ for $2\leq i\leq r$. Finite-index subgroups carry the topology induced by the full profinite topology, so completion identifies this kernel with $K_r$. Its Euler characteristic is $2(1-r/2)=2-r$. When $r=3$, $c$ has odd parity, so the cusp lifts once and its inertia in $K_3$ is generated by $c^2$. When $r=4$, $c$ has even parity, so the cusp lifts twice, with inertia classes generated by $c$ and $c_1cc_1^{-1}$. The formula $2-2g-n=2-r$ now gives $(g,n)=(1,1)$ and $(1,2)$, respectively.

For $\phi\in\mathcal A_r$, there are $\sigma\in S_r$, $v_0,\ldots,v_r\in F_r$ and a common $\lambda\in\widehat{\mathbf Z}^{\times}$ such that
$$
 \phi(x_i)=v_i x_{\sigma(i)}^{\lambda}v_i^{-1},\qquad
 \phi(P)=v_0P^{\lambda}v_0^{-1}.
$$
Every $\phi(x_i^2)$ belongs to $J_r$; applying the same argument to $\phi^{-1}$ gives $\phi(J_r)=J_r$. Hence $\phi$ descends uniquely to an automorphism $\bar\phi$ of $Q_r$. Since $\lambda$ is odd modulo two, each $\bar\phi(c_i)$ is conjugate to $c_{\sigma(i)}$, and $\epsilon_r\bar\phi=\epsilon_r$. Thus $\bar\phi$ preserves $K_r$ and can be restricted to it. These constructions commute with composition and are continuous.

Write $u=q_r(v_0)$. For $r=3$ the image of $c^2$ is $u(c^2)^{\lambda}u^{-1}$. If $u$ has odd parity, replace this conjugator by $uc$, which has even parity and gives the same conjugate. This is therefore conjugacy in $K_3$, with exponent $\lambda$. For $r=4$, conjugation by an even $u$ preserves the first cusp class, while an odd $u$ takes it to the second. The image of the second generator $c_1cc_1^{-1}$ has conjugator $\bar\phi(c_1)u$, of the opposite parity. Thus the two cusp classes are permuted, again with their common exponent $\lambda$. This proves the asserted loop preservation.

There is also a precise outer form. Let $\delta_r$ be the outer involution of $K_r$ induced by conjugation by $c_1$, and put $D_r=\langle\delta_r\rangle$. It is nontrivial: on the Schreier generators it sends $c_1c_i$ to $(c_1c_i)^{-1}$, hence acts as $-1$ on their abelianization. Because $\bar\phi(c_1)$ has odd parity, the outer class of $\rho_r(\phi)$ normalizes $D_r$. Replacing $\phi$ by $\operatorname{Inn}(g)\phi$ changes this outer class by conjugation by $q_r(g)$, which is trivial or $\delta_r$ according to its parity. Consequently the well-defined outer homomorphism has target
$$
 \mathcal A_r/\operatorname{Inn}(F_r)
 \longrightarrow
 N_{\operatorname{Out}_{\rm lac}(K_r)}(D_r)/D_r.
$$
This proves quotient and restriction descent, including the necessary deck ambiguity. It does not supply the full geometric-normalizer comparison isolated in E.4. $\square$

For the ordinary genus-zero filling $(0,5)\to(0,4)$, the known normalizer identifications of LM3 E.7 identify the comparison with the identity of GT: the standard braid action restricts with the same pair $(\lambda,f)$, and faithfulness at the detecting level forces this identification. The same formal argument applies to $(1,2)\to(1,1)$ **if** E.9's automatic-inertia assertion and the asserted normalizer comparison map have first been proved. Separate abstract identifications of four groups with GT do not prove that a specified covering induces that map.

## E.6. Known — What the refined quilt theorems actually give

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


Let $\mathcal G_{\rm NS}$ be the subgroup of GT defined by Nakamura–Schneps (2000, Definition 1.1), imposing $(\mathrm{III}')$ and $(\mathrm{IV})$ with their Kummer cocycle $\rho_2$. Their Theorem 1.2 gives $G_{\mathbf Q}\subset\mathcal G_{\rm NS}$. Theorems 1.3–1.4 give genuine actions after a quilt is fixed, independent outer actions after forgetting it, and compatibility for inclusions of unions of pants. Hatcher–Lochak–Schneps (2000, Theorems A–C, respectively Lemma 7, Theorem 4 and Theorem 5 of §3) give the analogous action of their subgroup $\Lambda\subset\widehat{\mathrm{GT}}^1$ defined by relation $(R)$.

**Reduction to Grothendieck's formulation.** Replace each surface by its profinite mapping class group and each pants inclusion by the induced continuous homomorphism. Theorem 1.4 supplies a commutative square for every such arrow with the selected quilt restrictions. The change-of-quilt formula in Nakamura–Schneps §10, equations (10.1)–(10.4), says precisely that replacing those choices changes the action by a specified inner automorphism. Quotienting by these inner automorphisms therefore gives a natural transformation of the outer tower. Its restriction to any detecting genus-zero component has the original parameter $(\lambda,f)$, so every comparison in this restricted tower is the identity on $\mathcal G_{\rm NS}$. In the Hatcher–Lochak–Schneps formulation the same argument uses Theorem C, with $\lambda=1$ and the extra relation $(R)$.

This proves compatibility for the arrows actually present in those theorems. Their hypotheses do not include arbitrary finite covering maps. For the explicit genuine elliptic/quilt formulas, relation $(\mathrm{IV})$ and the $\rho_2$ correction remain part of the theorem being used; replacing $\mathcal G_{\rm NS}$ by all of GT in those formulas requires a separate proof of those relations or a comparison with a different action. In particular the Hatcher–Lochak–Schneps subgroup does not contain all of $G_{\mathbf Q}$: its arithmetic subgroup fixes all roots of unity and all roots of two. This restriction is stated on page 3 of the supplied paper. $\square$

## E.7. Known — Derivation of the whole procongruence outer-tower statement

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


Let $\mathcal S$ be Boggi's category of oriented hyperbolic surfaces with boundary and embeddings which may fill punctures, and let
$$
 \check{\mathfrak T}^{\rm out}(S)=\check{P\Gamma}(S,\partial S)
$$
with continuous homomorphisms modulo target inner automorphisms. Then
$$
 \operatorname{Aut}(\check{\mathfrak T}^{\rm out})\cong
 \widehat{\mathrm{GT}}.                                \tag{E.3}
$$
There is a faithful compatible action of GT on the corresponding full profinite outer tower. Equality of its automorphism group with GT follows if the congruence subgroup property holds for every component.

**Proof of the reduction, using Boggi (2026, Theorem 6.23 and Corollary 6.24).** We spell out why this is a statement in the manuscript's terms. Filling a boundary circle by a punctured disc kills exactly its procyclic twist subgroup. A natural automorphism of the tower preserves that kernel. Every interior simple closed curve is a boundary circle of an embedded subsurface, so naturality also preserves every interior twist-inertia subgroup. This is the argument of Boggi's Lemma 6.25; it makes inertia intrinsic to the full tower even though it need not be intrinsic to a single group. His Theorem 6.1 then identifies each sufficiently large component's permissible outer automorphisms with a permutation factor times GT. The individual boundary-filling maps distinguish the labelled boundary circles, eliminating the permutation factor. The restriction maps retain the same GT parameter, and the construction in Theorem 6.7 supplies its converse action. This proves (E.3), with the precise source category and outer ambiguity stated.

There is a natural quotient transformation $\widehat{\mathfrak T}^{\rm out}\to\check{\mathfrak T}^{\rm out}$. If all congruence kernels vanish, it is objectwise an isomorphism and therefore identifies the two automorphism groups. Without that assumption, Corollary 6.24 gives an injection of GT into the full profinite tower automorphism group, but not surjectivity; the latter is Boggi's Conjecture 6.21. Neither equation (E.3) nor that injection computes the normalizer quotient attached to an isolated arbitrary type without the automatic-inertia condition. $\square$

## E.8. Known — The modular-topos exact sequence and its correction

*Manuscript connection: §§26,30–33 bis;165–166/168,188–202;326–329,371,376,395–400.*

\nopagebreak[4]


For the stack of unordered marked hyperbolic curves $\mathcal M_{g,[n]}/\mathbf Q$, with geometric base point, the étale fundamental group fits in
$$
1\to\widehat\Gamma_{g,n}\to
 \pi_1^{\rm et}(\mathcal M_{g,[n]})\to G_{\mathbf Q}\to1. \tag{E.4}
$$
Passing through universal geometric monodromy replaces the left term by its procongruence image $\Sigma_{g,n}$, with congruence kernel as the discarded kernel. The arithmetic-image quotient of §29 is $G_{\mathbf Q}$, as in LM3 E.2. For $(0,3)$, the stack is $BS_3$, and (E.4) is the split sequence with middle group $S_3\times G_{\mathbf Q}$.

**Reduction.** Boggi (2026, §7.1, equation (29)) states (E.4) for the moduli stack, and §2.8 identifies the relevant relative groups with geometric étale groups of the logarithmic formal boundary objects. The map to the geometric fibre's outer automorphism group is the universal monodromy map. Its geometric kernel is exactly the definition of the congruence kernel. The intersection theorem of Hoshi–Mochizuki used in LM3 C.5 ensures that killing this geometric kernel introduces no extra arithmetic kernel after quotienting the image by $\Sigma$. At $(0,3)$ there is one geometric isomorphism class with automorphism group $S_3$, defined over $\mathbf Q$, giving the displayed product. This proves the stack-based exact sequence of scans 326–329. The coarse moduli space is a point and would lose $S_3$; it cannot replace the stack. Nor does (E.4) identify the arithmetic image with the entire normalizer in $\operatorname{Out}_{\rm lac}$: that additional assertion is precisely the §26 conjecture, not a formal consequence of the exact sequence. At scan 328 the folio alternative $166|168$ has no mathematical consequence, and we do not select one as a reading. $\square$

## E.9. Open — Automatic nonseparating inertia for the elliptic normalizer

*Manuscript connection: §§30–33 bis;188–202;371,376,395–400.*

\nopagebreak[4]


With $E$, $A$, and $A^I$ as in E.1, the precise remaining assertion is
$$
 A=A^I,
 \quad\text{equivalently}\quad
 a(I_\gamma)\text{ is conjugate in }E\text{ to }I_\gamma
 \text{ for every }a\in A,
$$
where $I_\gamma=\overline{\langle\tau_\gamma\rangle}$ is the subgroup of a nonseparating Dehn twist. The condition is independent of the representative of the outer automorphism. Under the normalizer reduction in E.1, this is exactly the unresolved implication needed for $\Gamma^{\rm norm}_{1,2}\cong\widehat{\mathrm{GT}}$.

**Attack and remaining obligation.** Boggi–Funar (2023, Theorem 4.11 and Corollary 4.12) and Boggi (2026, Theorem 2.8) identify centralizers of already recognized multitwists with curve stabilizers. These theorems do not characterize all nonseparating twists among arbitrary elements solely by the isomorphism type of their centralizers. Boggi's 2026 introduction explicitly retains automatic inertia in positive genus as unresolved. The precise converse still required here is an intrinsic recognition of $I_\gamma$ among subgroups of $E$ using the specified universal-curve fibre, its two cusp classes with their common exponent, and the transposition. An automorphism carrying the centralizer of $I_\gamma$ to an isomorphic centralizer does not supply that converse. The smallest unresolved case is this very group $\widehat{P\Gamma}_{1,3}$ with those decorations. We have neither proved the restricted recognition assertion nor constructed an element of $A\setminus A^I$.



# F. The pentagon, finite images, and abelianization

Throughout this part, weight means the ordinary bracket length in the free Lie algebra, not the motivic weight, which is its negative double in the conventions of Hain and Matsumoto. We use $W_n$ for the rational solutions of antisymmetry, the three-cycle equation, and the pentagon in $\mathfrak t_4$. We write $V_n$ for antisymmetry, three-cycle, and cabling, without the pentagon. These are different equation spaces. The relevant manuscript statements are §26, folios 162–165, scans 323–326; §29, scans 370–371; and §§34–35, scans 479, 487–488, 496–505.

## F.1. Proved — The exact invariant special-derivation equation space

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


For every field of characteristic zero and every $n\geq2$, there is a natural vector-space isomorphism
$$
V_n\simeq(\operatorname{OutSDer}_n(F_2))^{\mathfrak S_3},
$$
where $V_n$ is the space of degree-$n$ Lie polynomials $\psi$ satisfying
$$
\psi(x,y)+\psi(y,x)=0,\qquad
\psi(x,y)+\psi(y,z)+\psi(z,x)=0,
$$
$$
[x,\psi(x,y)]-[x+y,\psi(z,y)]=0,\qquad z=-x-y.
$$
The last equation must be retained when comparing with special derivations. The first two homogeneous equations alone are not this invariant space.

**Proof.** Every special outer derivation has a representative with $D(x+y)=0$, obtained by subtracting its inner part at the third puncture. For $n\geq2$ this representative is unique: a degree-$n$ Lie element commuting with the degree-one element $x+y$ is zero. Its tangential coefficients $a_x,a_y$ are also unique, because the centralizer of $x$ or $y$ in a free Lie algebra consists of its scalar multiples. Set
$$
a_x=\psi(z,x),\quad a_y=\psi(z,y),\quad
D(x)=[a_x,x],\quad D(y)=[a_y,y].
$$
Antisymmetry and the three-cycle equation give $a_x=a_y-\psi(x,y)$. Consequently
$$
D(x+y)=[\psi(z,y),x+y]-[\psi(x,y),x]=0
$$
by cabling. Interchanging $x,y$ interchanges the two coefficients. Under the cycle $(x,y,z)\mapsto(y,z,x)$ the triple of tangential coefficients $(a_x,a_y,0)$ becomes $(0,\psi(x,y),\psi(x,z))$. Subtracting the common inner coefficient $\psi(x,z)$ recovers $(a_x,a_y,0)$. Thus the outer derivation is invariant.

Conversely, normalize an invariant derivation by $a_z=0$ and define $\psi(X,Y)=a_y(-X-Y,Y)$. Transposition invariance gives $a_x=\psi(z,x)$. Cycle invariance, followed by the unique normalization at $z$, gives $\psi(z,x)=-\psi(x,z)$ and $\psi(z,y)=\psi(x,y)-\psi(x,z)$. These are antisymmetry and the three-cycle equation after invertible linear substitutions. The equation $D(x+y)=0$ is cabling. This proves surjectivity as well as injectivity. In weight one the residual inner derivation must be divided out; the outer invariant space is zero. $\square$

For clarity, the weight-four polynomial
$$
[x,[x,[x,y]]]-4[x,[[x,y],y]]+[[[x,y],y],y]
$$
satisfies the first two homogeneous equations but fails cabling. Its coefficients are produced by the exact nullspace calculation. Thus simply retaining the lowest homogeneous parts of (I) and (II), while dropping the loop-preserving and nonlinear lifting requirements, gives the wrong tangent space. This refutes that particular shortcut in Lead 4, not its correctly formulated invariant-space comparison.

## F.2. Proved — Direct pentagon bounds and exact dimensions through weight twelve

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


Our independent calculation gives the following table. The middle column is the exact rational dimension before imposing the pentagon, with cabling retained. The rank column is computed in the actual infinitesimal braid algebra, modulo the prime $65521$; it provides a rigorous upper bound on the rational kernel dimension. The final column is the exact rational dimension, obtained by matching this bound with the independently known motivic lower bound.

| Weight $n$ | $\dim V_n$ | Pentagon rank on $V_n$, modulo $65521$ | $\dim W_n$ |
|---:|---:|---:|---:|
| 1 | 1 before the outer quotient | 1 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 1 | 0 | 1 |
| 4 | 0 | 0 | 0 |
| 5 | 1 | 0 | 1 |
| 6 | 0 | 0 | 0 |
| 7 | 2 | 1 | 1 |
| 8 | 1 | 0 | 1 |
| 9 | 4 | 3 | 1 |
| 10 | 2 | 1 | 1 |
| 11 | 9 | 7 | 2 |
| 12 | 7 | 5 | 2 |

**Proof and computational certificate.** The program `fg_prepare.py` constructs the Lyndon basis, expands every bracket in the free associative algebra over $\mathbb Z$, and solves the three displayed equations over $\mathbb Q$. It stores integral multiples of a rational basis of $V_n$. Independence of their reductions modulo $65521$ is checked separately in `fg_certify.py`; this check matters, because an arbitrary integral rescaling could otherwise lose rank modulo the chosen prime.

For the pentagon we use the faithful decomposition
$$
\mathfrak t_4/Z(\mathfrak t_4)
 =L(u,v,w)\rtimes L(a,b),
$$
with $u=t_{14},v=t_{24},w=t_{34},a=t_{12},b=t_{23}$ and
$$
t_{13}=-a-b-u-v-w.
$$
The derivations of the free fibre are
$$
D_a(u)=[u,v],\quad D_a(v)=[v,u],\quad D_a(w)=0,
$$
$$
D_b(u)=0,\quad D_b(v)=[v,w],\quad D_b(w)=[w,v].
$$
The braid relations verify this semidirect presentation; conversely it recovers all generators and defining relations, with the single central generator restored separately. For weight at least two the centre has no component, so this model loses no equation. The five pentagon substitutions are evaluated in this model, not in a commuting or metabelian quotient. `fg_pentagon.cpp` calculates their free-fibre component using exact modular word arithmetic. Their base component cancels identically. It records pivot word indices and ranks. In weight one, the direct pentagon defect is $-\alpha t_{12}-\beta t_{34}$, which forces zero; weight two is killed by the three-cycle equation.

Cabling is a rational consequence of the three defining equations (Drinfeld, 1990, Proposition 5.7; Bar-Natan, 1998, Theorem 5). Using it first is therefore an exact elimination of redundant unknowns in the rational problem. We do not assert that adding it preserves the solution space over every finite field. If $K_n$ is the saturated rational kernel of the remaining pentagon matrix in the integral candidate lattice, its reduction injects into the modular kernel. The listed ranks therefore give the asserted rational upper bounds. Brown's Theorem 1.1 and its introductory deduction of the faithful mixed Tate action supply a free Lie subalgebra on one generator in each odd weight at least three. The Witt product formula gives its dimensions $1,0,1,0,1,1,1,1,2,2$ in weights $3$ through $12$. They match the upper bounds. No all-weight claim is inferred from this finite calculation. $\square$

## F.3. Proved — Strictness in the coprime pro-prime cases

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


For every prime $\ell\geq5$, the group of special, label-preserving outer automorphisms of the free pro-$\ell$ tripod group centralizing its geometric $\mathfrak S_3$ is strictly larger than its subgroup satisfying the pentagon. Under the usual normalizer interpretation of the pro-$\ell$ pair equations, this is
$$
\mathrm{GT}_{\ell}^{1}\subsetneq\mathrm{GT}_{0,\ell}^{1}.
$$
Here the superscript denotes multiplier one; these groups are distinct from the full profinite groups.

**Proof.** The positive filtration subgroup of special outer automorphisms is pro-$\ell$: it is contained in the quotient of the kernel of the action on the Frattini quotient of a finitely generated free pro-$\ell$ group. The integral lifting theorem in A realizes every integral special outer derivation. The coprime fixed-point lifting lemma proved there applies to the geometric $\mathfrak S_3$, since $6$ is a unit in $\mathbb Z_\ell$. Thus every invariant integral leading term lifts to an actual automorphism centralizing $\mathfrak S_3$.

In weight seven the invariant lattice has rank two, while the rational pentagon solution space has dimension one by F.2. Choose an integral invariant element outside that rational line and lift it. If its lift satisfied the group pentagon, the first nonzero homogeneous term of that relation would satisfy the Lie pentagon. This contradicts our choice. The normal form identifying this centralizer with the two-relation pair group is the same explicit normal-form calculation used in LM3 E.4–E.7: normalize the image of one inertia generator, then compare with the transposition and three-cycle. Its relations are group relations before passing to leading terms. $\square$

## F.4. Open — The small primes and the full profinite strictness question

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


We do not prove $\widehat{\mathrm{GT}}\ne\widehat{\mathrm{GT}}_0$. Nor do we prove pro-$2$ or pro-$3$ strictness by F.3. The exact unresolved assertions are: (i) that some invariant weight-seven integral derivation outside the pentagon line lifts to an actual fixed point when $\ell=2$ or $3$; (ii) that some such pro-prime witness lies in the image of the full profinite two-relation group. The first obstruction is nonabelian fixed-point lifting for a group of order divisible by $\ell$; the second is the image of the full profinite automorphism group in its pronilpotent realization. Neither is removed by the integral special-automorphism lifting in A, which does not impose the finite symmetry simultaneously.

This is an attack beyond a dimension comparison: we have identified the correct homogeneous invariant space, evaluated its pentagon map, and integrated the witness at every prime at least five. What remains is an exact lifting problem, already in the tripod. Consequently the prompt's proposed refutation of the §26 arithmetic conjecture at $(0,3)$ remains unproved here. No non-Galois full profinite GT element is asserted.

## F.5. Proved — All two-generated abelian finite images through order five hundred

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


For every finite two-generated abelian group $Q\simeq C_a\times C_b$, with $a\mid b$, the image of $\widehat{\mathrm{GT}}$ in $\operatorname{Aut}(Q)$, for any chosen quotient of the free group, is precisely
$$
\{q\mapsto \lambda q:\lambda\in(\mathbb Z/b)^\times\}.
$$
Every element of this image is realized by $G_{\mathbb Q}$. The program enumerates all **792 isomorphism types** with $ab\leq500$, including the trivial group, and records every scalar residue. This is an exhaustive abelian-family computation, not an enumeration of nonabelian quotients of order at most five hundred.

**Proof.** In a GT pair, $f$ belongs to the closed commutator subgroup, so it disappears in every abelian quotient. Both generators are raised to the same multiplier $\lambda$. A scalar is invertible precisely when its residue is a unit modulo the exponent $b$. Conversely the cyclotomic character maps onto $(\mathbb Z/b)^\times$, by the action on $\mathbb Q(\zeta_b)$, and $G_{\mathbb Q}$ embeds in $\widehat{\mathrm{GT}}$. This proves both inclusions and arithmetic realization, with no search for an unknown extension required.

For actual abelian GT-shadow objects, rather than just their actions on $F_2$-quotients, Dolgushev, Le, and Lorenz (2024), Theorem B.2 and Remark B.3, give the pairs $(m,1)$ with $\gcd(2m+1,N_{\rm ord})=1$. We reproduce the arithmetic realization: choose a cyclotomic multiplier congruent to $2m+1$ modulo $2N_{\rm ord}$. Then $(\lambda-1)/2\equiv m\pmod {N_{\rm ord}}$. This also distinguishes the two half-parameter choices when $N_{\rm ord}$ is even. `fh_finite.py` enumerates these for $N_{\rm ord}\leq22$, corresponding to the homocyclic $F_2$-quotients of order at most $22^2$.

The unmarked Fermat/Kummer cover can have field of moduli $\mathbb Q$ even though its deck marking requires roots of unity. Accordingly the arithmetic certificate is the cyclotomic action on the **marked** cover; its unmarked field of moduli alone would not certify all automorphisms of $Q$. $\square$

## F.6. Open — Nonabelian shadows and finite arithmetic exhaustion

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


For every nonabelian characteristic finite quotient $Q$ of $\widehat F_2$, determine whether every restriction of a genuine element of $\widehat{\mathrm{GT}}$ is the restriction of a Galois element. F.13 proves this for nilpotency class at most two, including an explicit quaternion dessin, but does not settle arbitrary $Q$. Moreover a solution of finitely many shadow equations need not lift to a genuine GT element; compatible lifting through the braid-tower quotients is an additional condition (Dolgushev et al., 2024, Theorem 3.8).

The settled families are the abelian quotients, including their even-level shadow half-parameters, and all characteristic quotients of nilpotency class at most two. In the latter family the commutator part of a GT pair acts trivially by conjugation. The first nilpotency class not covered by this reduction is three; there the conjugation by that part can be nontrivial. A concrete next test is the characteristic free class-three exponent-five quotient of order $5^5$, with its genuine GT image and its arithmetic image compared. This specifies a next finite instance, not a claim of minimality by group order. Nonnilpotent quotients are also untreated. We attach a complete quaternion computation, but no exhaustive nonabelian enumeration through order five hundred, and report no unrealized genuine shadow.

## F.7. Proved — Integral scalar coinvariants, including the prime two

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


For $w>0$ define $J_{\ell,w}=(u^w-1:u\in\mathbb Z_\ell^\times)\subset\mathbb Z_\ell$. Then
$$
\mathbb Z_\ell/J_{\ell,w}=
\begin{cases}
0,&\ell>2,\ (\ell-1)\nmid w,\\
\mathbb Z/\ell^{1+v_\ell(w)},&\ell>2,\ (\ell-1)\mid w,\\
\mathbb Z/2,&\ell=2,\ w\text{ odd},\\
\mathbb Z/2^{2+v_2(w)},&\ell=2,\ w\text{ even}.
\end{cases}
$$
Thus Lead 5's proposed nonvanishing in the integral scalar model is correct. In the odd generating weights $3,5,7,9,11$ the model has no odd-prime coinvariants but has a nonzero $\mathbb F_2$ quotient in every weight.

**Proof.** For odd $\ell$, a Teichmüller unit detects the failure of divisibility by $\ell-1$. When that divisibility holds, every unit has $u^w\equiv1\pmod\ell$, and the minimum valuation is $1+v_\ell(w)$, attained by $u=1+\ell$, by the binomial expansion. For $\ell=2$, $u=-1$ gives valuation one for odd $w$. For even $w$, factor $u^w-1$ successively by squaring; every odd $u$ gives valuation at least $2+v_2(w)$, attained by $u=3$. These arguments are valid for every prime, without replacing $\mathbb Z_2^\times$ by $1+4\mathbb Z_2$. The code verifies the predicted ideal in a sufficiently high finite residue ring for $w\leq12$ and $\ell=2,3,5,7,11,13$. $\square$

## F.8. Refuted — Automatic extension of a character from scalar coinvariants

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


For arbitrary group extensions, a nonzero conjugation-invariant character of the kernel need not extend to the whole group. This general inference is refuted below; no nonextending character inside the actual GT group is asserted. For a finite abelian coefficient group $A$ with trivial action, the obstruction in the actual cyclotomic extension is the transgression
$$
H^1(K,A)^{\mathbb Z_\ell^\times}\longrightarrow
H^2(\mathbb Z_\ell^\times,A)
$$
for the actual extension $1\to K\to\mathrm{GT}_\ell\to\mathbb Z_\ell^\times\to1$, whenever the displayed quotient is used. The kernel of transgression is the image of restriction from $H^1(\mathrm{GT}_\ell,A)$.

**Proof and counterexample.** In $1\to C_2\to Q_8\to C_2^2\to1$, the central kernel has a nonzero invariant character to $C_2$. Every homomorphism $Q_8\to C_2$ kills that kernel, since $-1=[i,j]$. Thus its nonzero character does not extend. The program constructs the multiplication table, checks associativity, enumerates all four homomorphisms to $C_2$, and verifies their trivial restrictions. The five-term cohomology sequence gives the stated obstruction for the actual cyclotomic extension as well, without asserting that its transgression is nonzero.

There is a useful distinction between primes. For odd $\ell$ and $\ell$-primary $A$, one has $H^2(\mathbb Z_\ell^\times,A)=0$, so every **actual** invariant kernel character does extend. Indeed, $\mathbb Z_\ell^\times\cong\mu_{\ell-1}\times\mathbb Z_\ell$; averaging kills higher cohomology of the first factor. For the second, the description $H^2(C_{\ell^m},A)=A/\ell^m A$ identifies inflation to $C_{\ell^{m+1}}$ with multiplication by $\ell$. Its direct limit is zero for finite $\ell$-primary $A$. At two, the torsion factor $C_2\subset\mathbb Z_2^\times$ means that this vanishing need not hold. Thus in the odd-prime case the unproved step is already the construction of an actual invariant kernel character from the graded coinvariants; at two, extension can require an additional argument. This vanishing concerns only the displayed $\mathbb Z_\ell^\times$ quotient; it does not apply automatically to the full profinite quotient $\widehat{\mathbb Z}^{\times}$, whose kernel is a different group. F.7 establishes neither such actual character nor an extra full profinite GT character. $\square$

## F.9. Known — The precise rational abelianization statement

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


In the category of affine pro-algebraic groups over a characteristic-zero field $k$, the scalar character induces
$$
\mathrm{GRT}^{\rm ab}\simeq\mathbb G_m.
$$
After the all-weight result verified in G, write $\mathfrak{grt}_{1,\mathrm{gr}}$ for the graded direct sum and $\widehat{\mathfrak{grt}}_1$ for its degree completion. Their graded and continuous Lie abelianizations, respectively, and the multiplier-one group abelianization are
$$
\begin{gathered}
\mathfrak{grt}_{1,\mathrm{gr}}^{\rm ab}=\bigoplus_{j\geq1} k\sigma_{2j+1},\qquad
(\widehat{\mathfrak{grt}}_1)^{\rm ab,cont}=\prod_{j\geq1} k\sigma_{2j+1},\\
\mathrm{GRT}_1^{\rm ab}=\prod_{j\geq1}\mathbb G_a(2j+1).
\end{gathered}
$$
An associator transports this statement to $\mathrm{GT}(k)$ in its pro-algebraic interpretation. The isomorphism with the graded form depends on that associator.

**Reduction to the cited results.** Hain and Matsumoto (2003), Theorem 7.3, compute the free graded Lie algebra of the weighted completion of $G_{\mathbb Q,\{\ell\}}$, initially including weight one. Their Theorem 8.4 identifies the rationalized graded image of the outer action; Lemma 8.5 kills weight one. Remark 8.6, using Ihara's nonvanishing of the Soulé classes, identifies its abelianization as the sum of odd Tate lines of weight at least three. Brown (2012), Theorem 1.1 and the deduction of faithfulness in its introduction, provide the free motivic lower bound. G supplies the matching upper bound for the entire equation algebra. This proves the multiplier-one formula, rather than merely identifying an arithmetic subalgebra.

For the full group, every positive-weight vector $v$ is a commutator with the torus in the abelian quotient: a scalar $2$ acts by $2^w$, and $2^w-1$ is invertible in $k$. Apply this successively to each finite weight quotient and take closed commutators before the inverse limit. The remaining quotient is $\mathbb G_m$. In fact this full-group argument needs positivity of the weights, not freeness. It is the exact rational analogue of the cyclotomic abelianization on scans 323–329. Division by $2^w-1$ is exactly the operation that fails in the integral calculation F.7. $\square$

## F.10. Known — Which Lie tower has automorphism group GT

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


Let $\mathrm{PaB}_k^{\rm un}$ be the parenthesized braid groupoid with unipotent completion on its pure braid groups, retaining permutation data, units, cabling, juxtaposition, and strand removal. Its structure-preserving automorphism group, allowing the braiding multiplier, is $\mathrm{GT}(k)$. Fixing the multiplier gives the corresponding kernel. An associator identifies it with the parenthesized infinitesimal-braid model and its graded automorphism group.

**Reduction.** Bar-Natan (1998), §2.1, Claim 2.6, §3, and Proposition 5.3, express the category by a braiding and one reassociation arrow. An automorphism is determined by their images: the former supplies the scalar and the latter the group-like series. The two hexagons and pentagon are precisely the relations required for these images to extend to a functor. Preservation of units and strand removal supplies the normalizations; invertibility supplies an automorphism. His Definition 2.4 fixes the braiding and therefore describes the multiplier-one group. Allowing chord scaling by $k^\times$, and transporting it across an associator, restores the scalar factor of the full GT group. His Theorem 4 provides that associator comparison; Theorem 5 removes the redundant infinitesimal cabling constraint in characteristic zero. This derives the automorphism assertion from a presentation, rather than from an equality of dimensions.

The strict boundary exit category of the manuscript also has noninvertible smoothing arrows. It is not the parenthesized braid **groupoid**. Thus this theorem proves the stated operadic Lie approximation. An unqualified assertion for an unspecified termwise completion of all exit-category Hom-sets would require an extra comparison and is not silently included. Neither version implies equality of full profinite groups: rational unipotent realization forgets finite torsion and does not provide finite-quotient arithmetic exhaustion. $\square$

## F.11. Proved — The finite-quotient counterpart of the upper bound, in the settled family

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


The exact full profinite counterpart is: for every open normal $V\triangleleft\widehat{\mathrm{GT}}$, the map $G_{\mathbb Q}\to\widehat{\mathrm{GT}}/V$ is onto. LM3 E.22 proves its equivalence with $G_{\mathbb Q}=\widehat{\mathrm{GT}}$ by compactness. F.5 proves this statement for every finite quotient obtained from a cyclotomic scalar action on an abelian quotient of $F_2$, with arbitrary modulus, not merely those in the table.

**Proof of the additional assertion.** Such a quotient is a quotient of $(\mathbb Z/m)^\times$. The field $\mathbb Q(\zeta_m)$ supplies the required surjection, and composing a surjection with any quotient remains surjective. This is a finite-exhaustion proof for a cofiltered family, but that family is not cofinal in all finite GT quotients. The missing cofinality cannot be supplied by rational dimension estimates. $\square$

## F.12. Open — The full profinite abelianization

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


Determine the kernel of $\lambda^{\rm ab}:\widehat{\mathrm{GT}}^{\rm ab}\to\widehat{\mathbb Z}^{\times}$. Our computations determine scalar coinvariants of individual integral graded lines and all abelian images of $F_2$ in the stated range. They do not determine the abelianization of the full GT group. The remaining tasks include the integral lattices in its actual filtration, construction of actual invariant kernel characters, extension transgressions where these are not forced to vanish as in F.8, and compatibility among all primes and nonabelian finite quotients. The first unresolved case in this attack is construction and extension of an actual degree-three $2$-primary kernel character across the cyclotomic extension. No absence or existence of an extra full profinite character is claimed.

## F.13. Proved — Class-two finite images and an explicit nonabelian quaternion dessin

*Manuscript connection: §26; folios 163-166 (328 folio doubtful); scans 323-329; §27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation.*

\nopagebreak[4]


Fix the standard based embedding of $\widehat{\mathrm{GT}}$ in $\operatorname{Aut}(\widehat F_2)$, with ordered generators $x,y$. Let $N$ be an open characteristic subgroup and let $Q=\widehat F_2/N$ have nilpotency class at most two. Then the images of $G_{\mathbb Q}$ and $\widehat{\mathrm{GT}}$ in $\operatorname{Aut}(Q)$ are equal. Their common image factors through the cyclotomic multiplier modulo the exponent of $Q$.

In particular, for the characteristic quaternion quotient $x\mapsto i$, $y\mapsto j$ of order eight, that genuine automorphism image has order two:
$$
\{1,\ (i\mapsto i^{-1},\ j\mapsto j^{-1})\}.
$$
Its outer image is trivial. An explicit geometrically regular dessin defined over $\mathbb Q$ and realizing the quotient is the smooth projective model of
$$
C:\quad Y^2=X^5-X,\qquad
t=\frac{(X^2+1)^2}{4X^2}:C\longrightarrow\mathbb P^1_{\mathbb Q}.
$$
The map has degree eight and ramification profiles $(4,4)$ over each of $0,1,\infty$.

**Proof.** Write a genuine GT automorphism as
$$
x\longmapsto x^\lambda,\qquad
y\longmapsto f^{-1}y^\lambda f,
\qquad f\in[\widehat F_2,\widehat F_2].
$$
Since $[Q,Q]\subseteq Z(Q)$, its induced automorphism sends the two chosen generator images to their $\lambda$-powers. These two values determine the entire homomorphism. If $e$ is the exponent of $Q$, they depend only on $\lambda\bmod e$. Choose $\sigma\in G_{\mathbb Q}$ with $\chi(\sigma)\equiv\lambda\pmod e$, using cyclotomic surjectivity. Its GT image induces exactly the same automorphism on $Q$. Characteristicness of $N$ ensures that both genuine automorphisms descend. This proves equality of the images. The description is by **powers of the chosen generators**; it does not identify the automorphism with the usually nonmultiplicative map $q\mapsto q^\lambda$ on all of a nonabelian group.

For $Q_8$, every ordered generating pair consists of two noncentral elements from distinct cyclic subgroups of order four. There are $6\cdot4=24$ such pairs. Each satisfies $u^2=v^2=-1$ and $vu=u^{-1}v$, so there is a unique automorphism sending $(i,j)$ to $(u,v)$. Consequently every epimorphism $\widehat F_2\to Q_8$ has the same kernel. That kernel is characteristic, since precomposition by an automorphism gives another epimorphism. The preceding image formula now gives the two displayed maps according to $\lambda\bmod4$. Both occur because $\chi\bmod4$ is onto. Simultaneous inversion of $i,j$ is conjugation by $ij$, which proves the outer assertion.

To verify the dessin directly, over $\mathbb Q(\sqrt{-1})$ put
$$
a(X,Y)=(-X,\sqrt{-1}Y),\qquad
b(X,Y)=(X^{-1},\sqrt{-1}Y/X^3),\qquad h(X,Y)=(X,-Y).
$$
These preserve the curve and $t$, and satisfy $a^2=b^2=h$, $h^2=1$, and $ab=hba$. They generate eight distinct deck transformations. The rational function of $X$ has degree four, while the hyperelliptic map has degree two, so these account for the full deck group. The polynomial $X^5-X$ is square-free; hence the curve has genus two. The identities
$$
t=\frac{(X^2+1)^2}{4X^2},\qquad
t-1=\frac{(X^2-1)^2}{4X^2}
$$
give order-two zeros on the $X$-line at $\pm\sqrt{-1}$ and $\pm1$, and order-two poles at $0,\infty$. Each is a branch point of the hyperelliptic map, so the composite has ramification index four there. Riemann--Hurwitz gives total ramification $18=2\cdot2-2+2\cdot8$, excluding any other branch point. Thus this is a geometrically Galois three-point cover defined over $\mathbb Q$, with geometric deck group $Q_8$ and displayed deck marking over $\mathbb Q(\sqrt{-1})$. Choose its identification with the ordered free-group quotient as above. Coefficient conjugation on the displayed deck formulas sends both $a,b$ to their inverses; its fixed deck subgroup is $\langle ab\rangle\simeq C_4$. In particular we do not assert that $\mathbb Q(C)/\mathbb Q(t)$ is $Q_8$-Galois over $\mathbb Q$. The arithmetic realization of the genuine quotient image is the cyclotomic argument already proved, not an inference from the unmarked field of moduli alone.

The independent program `quaternion_shadow.py` checks all $512$ associativity triples, all $24$ generating-pair automorphisms, the central commutator subgroup, both GT restrictions, all $64$ deck-composition identities, preservation of the curve and Belyi function, and coefficient conjugation. Its JSON and text output are included. This settles a genuine nonabelian quotient and the stated class-two family; it does not enumerate all nonabelian quotients of order at most five hundred. $\square$


# G. Independent verification of the requested steps of manuscripts 019 and 031

The labels below concern the exact propositions proved, with their external inputs specified. They do not constitute a certification of every statement in either manuscript. We read the supplied October 6 version of 019, the October 5 version of 031, and the relevant primary inputs. The separate September 24 exterior-sheet manuscript is not used in any proof below. No priority claim is made.

## G.1. Proved — division on a torically uniformized abelian variety

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


Let $\Omega$ be complete and algebraically closed of characteristic zero. Suppose an abelian variety has analytic uniformization $q:T^{\mathrm{an}}\to J^{\mathrm{an}}$ by a split torus, with discrete torsion-free lattice $\Lambda$, and $q$ is a topological covering and local analytic isomorphism. If $a:A\to T^{\mathrm{an}}$ is analytic and
\[
 B=A\mathbin{\times}_{q\circ a,J^{\mathrm{an}},[m]}J^{\mathrm{an}},
\]
then every torus character $\eta\circ a$ has an analytic $m$th root on the whole of $B$, for every positive integer $m$.

**Proof.** Write $b:B\to J^{\mathrm{an}}$ for the second projection. Locally lift $b$ to $t:B\to T^{\mathrm{an}}$. The quotient $t^m/a$ lies in the discrete group $\Lambda$ and is locally constant. Its image in $\Lambda/\Lambda^m$ is independent of the lift. Decompose $B$ into the finitely many clopen pieces determined by these classes. Fix a representative $\lambda$ on one piece. Adjust local lifts by locally constant periods until $t^m=\lambda a$. On an overlap two adjusted lifts differ by $\rho\in\Lambda$ with $\rho^m=1$; torsion-freeness gives $\rho=1$. They therefore glue on the entire piece. Choose an $m$th root of $\eta(\lambda)$ in $\Omega$. Dividing $\eta(t)$ by that root gives the desired function. The pieces are disjoint, so the functions assemble globally. No invertibility of $m$ in the residue field enters. $\square$

## G.2. Proved — manuscript 019, Proposition 5.2, including every inverse annulus

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


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

## G.3. Proved — manuscript 031, Lemma 3.1 and its zero estimate

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


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

## G.4. Proved — the finite-character separation used in Proposition 4.3

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


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

## G.5. Proved — manuscript 031, Proposition 4.3

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


With the notation of G.4, for any finite quotient $R_0$ of $P$ and any $\gamma_0\in R_0$, one can enlarge to a quotient $R$ and choose a lift $\gamma$ so that infinitely many $\ell$-active source primes have target Frobenius $\gamma$ and source Frobenius image generating $\langle\gamma\rangle$.

**Proof.** We use Uchida (1981, §1 and Proposition 1), whose odd-prime local trichotomy gives an injective nontrivial pro-$\ell$ inertia image in a unique target prime, and cofinite target coverage for this fixed $\ell$. Choose $R$ using G.4. Take an open normal $U'\triangleleft G_{\mathbb Q}$ contained in $U\cap\beta^{-1}(P_L)$, and let $F'/\mathbb Q$ be its fixed field. Chebotarev and Uchida supply infinitely many active source primes $v'$ paired with target primes $w'$ in $L$ having Frobenius $\gamma$. Pass to a subset with distinct source rational primes, unramified in $F'$, and one fixed source Frobenius $\delta\in\operatorname{Gal}(F'/\mathbb Q)$. If $v=v'|_k$, where $T=G_k$, compatible prolongations retain $w'$: the decomposition group at $v'$ is contained in the one at $v$, and uniqueness in Uchida's theorem at the finite field $L$ identifies their target restrictions. Thus the image of $D_v$ in $R$ lies in $C=\langle\gamma\rangle$.

Put $H=T/U'$, and let $f=\min\{j>0:\delta^j\in H\}$. This is the residue degree of $v$ over its rational prime, by the orbit description on cosets; normality of $H$ is not required. Set $d=\beta(\delta^f)$ and $D=\langle d\rangle\subseteq C$. If $D<C$, choose $x$ by G.4 and pull it back to $y\in X_\ell(F')$. The pullback $j:X_\ell(L)\to X_\ell(F')$ is injective because the group image is open. Since $E_Cx=0$ and Frobenius evaluation at $w'$ is $C$-invariant, $x$ vanishes at $w'$, hence on its decomposition group, and $y$ vanishes at all selected $v'$.

The Frobenius-detection consequence of G.3 implies $E_{\langle\delta\rangle}y=0$. For clarity, that consequence follows by class-field reciprocity: a zero value at a degree-one prime annihilates the logarithm of a generator of a power of its ideal. Conjugate generators at distinct unramified rational primes have disjoint ideal supports, satisfying G.3. For prescribed Frobenius $\delta$, average first over $\langle\delta\rangle$, descend to its fixed field, and use the degree-one case. Thus no density assumption on the selected infinite set is used.

In the averaging sum, the powers with $f\mid j$ act trivially on $y$ because $x$ is $D$-invariant. Every other summand is fixed by some $N_i\ne N$. Therefore $y$ lies in the sum of the $N_i$-invariant subspaces of $X_\ell(F')$. The subspace $Y=j(X_\ell(L))$ is stable under the finite group $U/U'$. Characteristic-zero semisimplicity supplies a $U$-equivariant projection $X_\ell(F')\to Y$. Each $N_i$ is contained in $U$, so the projection carries its invariant space into $Y^{N_i}=j(X_\ell(L)^{H_i})$. Pulling back gives the forbidden inclusion $x\in\sum_iX_\ell(L)^{H_i}$. Thus $D=C$, proving the proposition. The proof needs only $U$-equivariance; it never assumes $T$ normal in $G_{\mathbb Q}$. $\square$

## G.6. Proved — manuscript 031, Proposition 5.3, with a bound independent of the auxiliary prime

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


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

## G.7. Proved — the immediate global consequences of the verified 031 steps

*Manuscript connection: Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart.*

\nopagebreak[4]


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
Choose a generator $\tau$ of a pro-$\ell$ Sylow of source inertia. The source tame relation makes $g\tau g^{-1}\tau^{-(Nv)^{b(g)}}$ belong to wild inertia, a pro-$p$ group with $p\ne\ell$. In the target tame quotient its image belongs to the pro-$\ell$ factor, because the two occurrences of $\tau$ do. It is therefore trivial. Uchida's odd-prime local result (1981, §1, pp. 595--596) makes the target image of $\tau$ nontrivial in its torsion-free pro-$\ell$ tame inertia, so comparing the target conjugation relation gives (G.2). This uses no assertion that every part of source inertia is sent into target inertia.

Dirichlet's theorem makes $\mathcal L$ infinite. Fix $\ell\in\mathcal L$, and apply G.5 with $R_0=\operatorname{Gal}(\mathbb Q(\mu_\ell)/\mathbb Q)=\mathbb F_\ell^{\times}$ and a generator $\gamma_0$. It gives infinitely many active source primes $v$, over distinct rational primes $p\ne\ell$, such that the image of a Frobenius lift generates $\mathbb F_\ell^{\times}$. Put $Nv=p^f$. Relation (G.2) says that $p^f$ also generates $\mathbb F_\ell^{\times}$, so $\gcd(f,\ell-1)=1$. But $1\leq f\leq[k:\mathbb Q]$, and every prime divisor of an integer $f>1$ in that range divides $m_0$, hence $\ell-1$. Therefore $f=1$. Taking logarithms in (G.2) shows that $\log\chi_\ell\circ\beta-\log\chi_{k,\ell}$ vanishes at these infinitely many degree-one primes. The Frobenius-detection consequence of G.3, proved in G.5, makes this additive character zero. Finally, the kernel of the logarithm on $\mathbb Z_\ell^{\times}$ for odd $\ell$ is $\mu_{\ell-1}$, proving the last assertion. $\square$

**Scope of the manuscript audit.** The exact requested 019 and 031 propositions are proved in G.2, G.3, G.5, and G.6; no gap was found in them. G.7 records an additional implication with its proof. The full proper local section theorem and specified-completion inclusion of 019, Theorems 1.1--1.2, and the unrestricted open-Hom theorem of 031, Theorem 1.1, are claims of the supplied manuscripts, not automatically certified by this targeted audit. To turn the present text into a self-contained proof of those full claims one must also reproduce, respectively, 019's collar-to-global patching and descent chain, and 031's finite-partner argument, simultaneous Kummer separation, and compactness identification, followed by Hoshi (2025, Theorem 3.4). We read the final 031 reduction and the primary Hoshi theorem; for 019 we inspected the final use of Proposition 5.2 and its decomposition-group consequence. We do not call a step a mathematical gap merely because its independent proof is outside the designated obligations. In particular, this scope qualification is not a new row asserting that either full statement is false or mathematically open.

The independent computations in `code/dg_checks.py` verify the elementary Heisenberg counterexample, the six-function rigidity check, the strict exponent inequalities used in G.3, and the cyclic-character multiplicity bound used in G.6. The nonarchimedean analytic arguments and infinite Galois assertions are proved above, not certified by those finite checks.



We now treat the two outstanding steps of the September 23 manuscript 008 and the independent upper-bound route in the attached October 28 version of Willwacher. We distinguish an independent rederivation of a lemma from an independent discovery of its method. The coordinates $A=x^2$, $B=y$, $C=[x,y]$ and the characteristic-two strategy are taken from these sources. No novelty or priority is claimed.

## G.8. Proved — The filtered transfer in manuscript 008, Proposition 3.2

*Manuscript connection: Auxiliary audit of manuscript 008; connection to §§26-27, folios 163-172 verso, scans 323-341, and LM3 E.26; no verbatim counterpart of the modern proposition in 1981.*

\nopagebreak[4]


Let $\bar\psi$ be the reduction of an integral rational GT solution of weight $n>2$. Express it in the ordinary free Lie algebra on $A=x^2,C=[x,y],B=y$ over $\mathbb F_2$, and suppose its lowest $B$-count is $r$. Let $\chi(A,C,B)$ be its component of that count, with arguments in the displayed order, and write $n=2m+r$, with $m>0$. In the integral type-$B_3$ arrangement algebra reduced modulo two, use $a_i$ for coordinate hyperplanes, $u_{ij}$ for the minus hyperplane, and $v_{ij}$ for the sum of the minus and plus generators. Then
$$
\begin{split}
0\equiv{}&\chi(a_1,v_{12}+v_{13},u_{12}+u_{13})
 +\chi(a_2+v_{12},v_{23},u_{23})\\
&+\chi(a_1+a_2+v_{12},v_{13}+v_{23},u_{13}+u_{23})
 +\chi(a_1,v_{12},u_{12})
\end{split}
$$
modulo the span of words of **length $m+r$** having fewer than $r$ letters of type $u$. This is exactly the stated filtered transfer, including its length qualification.

**Proof.** We give the finite rewriting argument without assuming linear independence in the target. In the source $U(\mathfrak t_4(\mathbb F_2))$, relabel strands $0,1,2,3$ and put $X_i=t_{0i}$, $u_{ij}=t_{ij}$, $a_i=X_i^2$, $v_{ij}=[X_i,u_{ij}]=[X_i,X_j]$. For a newest strand $d$, write $X=X_d$, $H=X^2$, $U_i=u_{id}$, $V_i=[X,U_i]$. The base derivations are
$$
\delta_i(X)=V_i,\quad\delta_i(U_i)=V_i,\quad\delta_i(U_k)=0\ (k\ne i),
$$
$$
\epsilon_{ij}(X)=0,\quad
\epsilon_{ij}(U_i)=\epsilon_{ij}(U_j)=[U_i,U_j],
$$
with the other $U_k$ killed. Acting twice by $\delta_i$ gives the action of $a_i$; commuting $\delta_i$ with $\epsilon_{ij}$ gives that of $v_{ij}$. The Leibniz rule therefore gives every source base–fibre commutator, with no hypothesis about unbounded words.

The count-preserving terms are the following; exchanging $i,j$ gives the other incident entries, and nonincident entries vanish at this count:

| Base letter | $H$ | $U_i$ | $V_i$ |
|---|---|---|---|
| $a_i$ | $[H,V_i]$ | $[H+V_i,U_i]$ | $[H,V_i]$ |
| $u_{ij}$ | $0$ | $[U_i,U_j]$ | $[U_i,V_j]+[V_i,U_j]$ |
| $v_{ij}$ | $0$ | $[U_i,V_j]$ | $[V_i,V_j]$ |

For example, putting $R_i=[H,U_i]$, the exact source identities are
$$
[a_i,H]=[H,V_i]+[R_i,U_i],\qquad
[a_i,V_i]=[H,V_i]+[[V_i,U_i],U_i].
$$
The extra terms have two additional $U$ letters. The remaining source corrections are obtained from the same two derivations and likewise add two $U$ letters. On the target side, the four-hyperplane flat $z_i=z_d=0$ gives the $a_i$ row, and the signed three-hyperplane flats give the $u,v$ rows. The sole additional incident target term is $[V_i,V_j]$ in $[u_{ij},V_i]$; it has one fewer $U$ than the input. Nonincident pairs meet in a two-hyperplane flat and commute. Thus source rewriting never decreases count, target rewriting never increases it, and their count-preserving tables agree exactly.

Order each word by replacing a base letter immediately followed by a fibre letter with the swapped product plus their commutator. This terminates: the lexicographic pair consisting of the number of base letters and the number of base-before-fibre inversions decreases on every branch. Repeat with the next lower strand. Source ordered words are independent: the free-fibre decomposition of the braid algebra gives an iterated tensor product of free associative fibre algebras; in each restricted fibre the leading words $XX,XU_i,U_i$ form a prefix code. Thus all products in the restricted fibre alphabet are independent, even when their lengths differ.

In these source coordinates the five substitutions of the reduced pentagon have triples
$$
\begin{gathered}
(a_1,v_{12}+v_{13},u_{12}+u_{13}),\\
(a_2+v_{12}+u_{12}^2,v_{23}+[u_{12},u_{23}],u_{23}),\\
(u_{12}^2,[u_{12},u_{23}],u_{23}),\\
(a_1+a_2+v_{12},v_{13}+v_{23},u_{13}+u_{23}),\quad
(a_1,v_{12},u_{12}).
\end{gathered}
$$
The exact count-$r$ component is the displayed four-term polynomial. The discarded component has larger count: either an extra $u^2$ or commutator adds two, or the entirely $u$-valued third term has count $n>r$. Ordering cannot lower it back to $r$. Source independence forces every ordered count-$r$ coefficient of the four-term expression to be zero. Original weight and count determine symbolic length by $n=2\,\text{length}-\text{count}$; these zero coefficients all have length $m+r$.

Apply the target ordering to just this polynomial. The branches retaining count $r$ use the identical table and have the identical zero coefficient vector. The discarded branches have lower count and the same symbolic length, because target commutators are quadratic. This proves the asserted congruence. No homomorphism from the source algebra to the target algebra, and no target PBW independence, has been assumed. $\square$

## G.9. Proved — The deletion and residual-kernel induction of manuscript 008, §4

*Manuscript connection: Auxiliary audit of manuscript 008; connection to §§26-27, folios 163-172 verso, scans 323-341, and LM3 E.26; no verbatim counterpart of the modern proposition in 1981.*

\nopagebreak[4]


For each weight $n>2$ and count $r$, the projection
$$
\operatorname{gr}^r_F\bar L_n\longrightarrow L_{\mathbb F_2}(C,B),
\qquad \chi\longmapsto\chi(0,C,B)
$$
is injective. Here $\bar L_n$ is the reduction of the saturated lattice of rational solutions, not an unspecified full mod-two solution space.

**Proof.** We first justify the deletion representation in every length. Use the letters $0,e,p$ with endpoints $0,w$, where
$$
e=1,\quad p=(z_2-z_3)/(z_2+z_3),\quad
w=(z_2-z_1)/(z_2+z_1).
$$
For a hyperplane $H$ let its deletion at position $j$ have coefficient
$$
\nu_H(P_j,P_{j+1})-\nu_H(P_{j-1},P_j),
$$
with $\nu_H(P,P)=0$. The matrix-valued logarithmic one-form of these operators is flat. Indeed, two nonadjacent deletions cancel in pairs; for adjacent deletions their commutator coefficient is the sum of the logarithmic triangle identities for their two neighboring triples. For distinct $I,J,K$ that identity follows by differentiating $(I-J)+(J-K)+(K-I)=0$ and putting the three wedge products over a common denominator. For repeated letters one logarithmic form is zero and the other two agree. Taking residues successively at a hyperplane and a codimension-two flat gives the arrangement relation. All entries are integers, so the result reduces modulo two without identifying the plus and minus hyperplanes or dividing by two.

The factorization of $p,w,1-p,1-w,p-w$ gives the edge table

| Edge | $a,v$ functional | $u$ functional |
|---|---|---|
| $0p$ | $0$ | $u_{23}^*$ |
| $0w$ | $0$ | $u_{12}^*$ |
| $0e$ | $0$ | $0$ |
| $ep$ | $a_3^*-v_{23}^*$ | $0$ |
| $ew$ | $a_1^*-v_{12}^*$ | $0$ |
| $pw$ | $a_2^*+v_{13}^*-v_{12}^*-v_{23}^*$ | $u_{13}^*$ |

In particular an $a$ or $v$ operation cannot delete a zero. A word with $r$ zeros annihilates every remainder in G.8, and in a successful test of a count-$r$ word every $u$ operation must delete a zero.

Suppose $\chi(0,C,B)=0$ and let $h>0$ be its least nonzero $A$-count. Test G.8 on a word having $h$ letters $e$, $m-h$ letters $p$, and $r$ zeros. Every $A$ operation must remove an $e$, so minimality forces exactly the $A$-count-$h$ component to contribute. The third term of G.8 has zero $A$ operation. The first term cannot remove a $p$. In the fourth term, every successful deletion is at the right endpoint; its value is precisely the associative coefficient of the word obtained by $e\mapsto A,p\mapsto C,0\mapsto B$.

In the second term, an $e$ preceding a nonempty block of $p$'s and zeros cannot be removed while that block remains. The final remaining letter of the block has boundaries $e,e$ or $e,w$. Its deletion weight is $1+1=0$ if it is $p$, and $0+0=0$ if it is zero. Hence no complete deletion sequence exists. We conclude that every coefficient of the least-$A$ component with an $A$ before a non-$A$ vanishes. Reversal fixes homogeneous Lie polynomials in characteristic two; it also kills the remaining words ending in $A^h$. If $h<m$ a non-$A$ exists, a contradiction. Therefore a possible kernel element is an ordinary Lie polynomial $P(A,B)$ with $m$ letters $A$ and $r$ letters $B$.

The case $r=0$ vanishes except in weight two. For $r\geq1$, the reduced cabling identity and the substitution $x\mapsto x+y$ give, in the lowest count,
$$
D\bigl(P(A+C,B)+P(A,B)\bigr)=0,
\qquad D(A)=D(C)=0,\quad D(B)=C.
$$
Terms of larger original count cannot contribute, since the outer commutator lowers count by at most one. Looking at a word with two $C$ positions says that the coefficients of $P$ agree under exchanging any $A$ position with any $B$ position. All coefficients at this multidegree are consequently one value $\lambda$. If $m\geq2$, a word with three $C$ positions has coefficient $3\lambda=\lambda$, forcing zero. This is the key integral-characteristic-two induction, not a dimension estimate.

If $m=1$, the component has original $(x,y)$-bidegree $(2,r)$. Symmetry forces a nonzero component of bidegree $(r,2)$, whose $B$-count is at most two. Thus $r\leq2$. When $r=2$, the ordinary Lie component is spanned by $ABB+BBA$, whose three coefficients are $(1,0,1)$ and cannot all equal a nonzero $\lambda$. When $r=1$, the swapped bidegree forces a nonzero $[C,B]$ term which survives $A=0$, contrary to the kernel assumption. These cases exhaust the induction and prove injectivity. $\square$

## G.10. Known, with complete reduction — The all-weight upper bound via Willwacher's reconstruction

*Manuscript connection: Auxiliary audit of manuscript 008; connection to §§26-27, folios 163-172 verso, scans 323-341, and LM3 E.26; no verbatim counterpart of the modern proposition in 1981.*

\nopagebreak[4]


Over $\mathbb Q$, the full equation Lie algebra $\mathfrak{grt}_1$ is free on one generator in every odd weight at least three. The upper-bound argument below rederives Willwacher (2026, Theorems 1.1 and 2.2, Proposition 3.2); the lower bound is Brown's established faithful motivic action. This removes the conditional use of the all-weight upper bound in LM3 E.20, E.24, and E.26.

**Proof of the upper bound.** The integral free Lie and infinitesimal-braid targets are torsion-free. Intersect the rational solution space, with the rationally implied cabling equation included, with the free $\mathbb Z_{(2)}$ lattice. This intersection is saturated: if $2a$ is a solution, the rational linear equations imply that $a$ is one. Its mod-two reduction therefore injects into the four-equation mod-two space and has dimension equal to the rational dimension.

The map
$$
\iota:\mathbb F_2\langle A,B,C\rangle\longrightarrow
\mathbb F_2\langle x,y\rangle,
\quad (A,B,C)\mapsto(x^2,y,[x,y])
$$
is injective, since the leading words $xx,y,xy$ form a prefix code. It identifies the ordinary Lie ideal generated by $B,C$ with the ideal generated by $y$: Lazard elimination generates the latter by $\operatorname{ad}_x^j y$, whose even and odd members are respectively $\iota(\operatorname{ad}_A^iB)$ and $\iota(\operatorname{ad}_A^iC)$. Thus a solution of weight $n\geq3$ has a unique ordinary Lie preimage $P(A,B,C)$.

Put $R=\mathbb F_2\langle A,B,C\rangle$ and $M=R\otimes\mathbb F_2[\varepsilon,\eta]/(\varepsilon^2,\eta^2)$. On $R$ define derivations
$$
E(A)=E(C)=[A,B],\quad E(B)=0,
$$
$$
T(A)=0,\quad T(B)=[C,B],\quad T(C)=[A,B^2],
$$
and let $G=L_A+L_C+T$, where $L_r$ denotes left multiplication. Define
$$
\begin{aligned}
\rho(t_{12})&=\varepsilon,&
\rho(t_{23})&=L_A\partial_\varepsilon,\\
\rho(t_{13})&=\varepsilon+\eta+L_A(\partial_\varepsilon+\partial_\eta),&
\rho(t_{34})&=L_B+L_C\partial_\eta,\\
\rho(t_{24})&=E+G(\partial_\varepsilon+\partial_\eta)
 +L_{[A,B]}\partial_\varepsilon\partial_\eta.
\end{aligned}
$$
Set $\rho(t_{14})$ equal to the sum of the other five operators. This is a representation of $\mathfrak t_4$. To verify it in all word lengths, use $[D,L_f]=L_{D(f)}$ and
$$
[E,L_A]=[E,L_C]=L_{[A,B]},\quad [E,L_B]=[T,L_A]=0,
$$
$$
[L_A,G]=L_{[A,C]},\quad[G,L_B]=L_{[A,B]},\quad
[G,L_C]+[L_{[A,B]},L_B]=L_{[A,C]}.
$$
The final equality is $[A,B^2]=[[A,B],B]$ in characteristic two. Expanding in the four-dimensional $\varepsilon,\eta$ operator algebra gives the two independent three-strand relations on $123$, the relations $[t_{12},t_{34}]=[t_{13},t_{24}]=0$, and the equality of the three commutators on $234$. The zero total sum then gives the remaining relations on $124,134$ and the final disjoint pair. Each identity used here is an equality of multiplication operators or of derivations checked on the three free generators, so the verification holds on all $R$, not merely on truncated words. Independently, `g_operator.py` checks all 15 braid-relator forms on 484 basis inputs, giving 7,260 vanishing checks.

Let $f(B,C)=P(0,B,C)$. Restrict the five pentagon pairs $(u,v)$ to $R\subset M$. Their triples $(\rho(u^2),\rho(v),\rho([u,v]))$ are

| Pair | Triple on $R$ |
|---|---|
| $(t_{12},t_{23}+t_{24})$ | $(0,E,L_C+T)$ |
| $(t_{13}+t_{23},t_{34})$ | $(L_A,L_B,L_C)$ |
| $(t_{23},t_{34})$ | $(0,L_B,0)$ |
| $(t_{12}+t_{13},t_{24}+t_{34})$ | $(L_A,E+L_B,L_A+T)$ |
| $(t_{12},t_{23})$ | $(0,0,L_A)$ |

The third and fifth contributions vanish in weight at least three. In the fourth, $L_A$ commutes with the other two arguments, so every ordinary Lie term containing $A$ vanishes; the remaining central $L_A$ also disappears. Applying the resulting operator equality to $1$ gives
$$
P(A,B,C)=f(E,L_C+T)(1)+f(E+L_B,T)(1).             \tag{G.3}
$$
This is an explicit left inverse to projection $P\mapsto f$, proving its injectivity.

It remains to bound its image. On $\mathbb F_2\langle B,C\rangle$ let $\partial(B)=C,\partial(C)=0$, and define
$$
\theta(A)=L_{B^2},\quad\theta(B)=\partial,\quad\theta(C)=L_C,
\quad Q(r)=\theta(r)(1).
$$
Let $d(B)=B^2+C,d(C)=[B,C]$. Checking on $A,B,C$ gives $\theta T=0$ and $\theta(E(r))=[d,\theta(r)]$; hence $QT=0,QE=dQ$, and $QL_r=\theta(r)Q$. Apply $Q$ to (G.3):
$$
Q(P)=f(d,L_C)(1).
$$
The second reconstruction term becomes $f(d+\partial,0)(1)=0$, since $f$ has no linear term. Antisymmetry of $\psi$, evaluated at $x=\partial,y=L_B$, gives $\theta(P)=L_f$, since $\partial^2=0$ and $[\partial,L_B]=L_C$. Therefore
$$
f=f(d,L_C)(1).
$$
Now $d^2=0$, as is checked on $B,C$, so the ideal generated by $L_C$ in $\operatorname{Lie}(d,L_C)$ is generated by $L_C$ and $[d,L_C]=L_{[B,C]}$. Hence $f\in\operatorname{Lie}(C,[B,C])$.

Lazard elimination identifies this last algebra with
$$
\mathbb F_2 C\ltimes
\operatorname{Lie}_{\mathbb F_2}(g_1,g_2,\ldots),
\qquad g_j=\operatorname{ad}_C^jB,\quad\mathrm{wt}(g_j)=2j+1.
$$
Its dimensions in weights at least three are precisely those of the free Lie algebra on one generator in every odd weight at least three. The injective projection, followed by saturated reduction, proves this upper bound for $\mathfrak{grt}_1(\mathbb Q)$. Brown supplies the matching free subalgebra, so equality in each weight proves that its inclusion is an isomorphism; taking products proves the completed assertion. $\square$

## G.11. Proved — Dependency and independence of the two upper-bound arguments

*Manuscript connection: Auxiliary audit of manuscript 008; connection to §§26-27, folios 163-172 verso, scans 323-341, and LM3 E.26; no verbatim counterpart of the modern proposition in 1981.*

\nopagebreak[4]


The proof of G.10 uses neither G.8's comparison with the type-$B_3$ arrangement nor G.9's deletion induction. Its replacement for their injectivity step is the explicit formula (G.3), and its replacement for the later shift/Vandermonde image argument is the operator identity $f=f(d,L_C)(1)$. Both arguments use the same characteristic-two coordinate embedding, the integral reduction of rational solutions, and ordinary rather than restricted Lie algebras. Thus these are different proofs of the crucial upper-bound mechanism, with shared preparatory ideas.

The lower bound used here is Brown's theorem; we have not used Willwacher's additional §4.4 or manuscript 008's internal lower-bound construction to justify it. F.2 is a third, bounded check of the equations through weight twelve, independent of the two all-weight image arguments. Its agreement is evidence for the implementation and an exact theorem in that range; it is not what proves G.10. The designated audit verdicts for 008 Proposition 3.2 and §4 are **proved here** by G.8–G.9, and the all-weight upper bound is **rederived from the read source** in G.10. No gap was found in those specified steps.


# H. Congruence and higher categorical completion


## H.1. Proved — A centralizer exactly measuring the closed genus-three kernel

*Manuscript connection: Auxiliary congruence problem attached to §26; folio 162; scan 320; LM3 B.3.*

\nopagebreak[4]


Let $P=\widehat\pi_{3,0}$ and let
$$
1\to P\to E=\widehat{P\Gamma}_{3,1}\xrightarrow{q}
\widehat\Gamma_{3,0}\to1
$$
be the profinite Birman sequence. The restriction of $q$ gives an isomorphism
$$
 C_E(P)\xrightarrow{\sim}C_{3,0},
\qquad
C_{3,0}=\ker(\widehat\Gamma_{3,0}\to\operatorname{Out}(P)).
                                                               \tag{H.1}
$$
In particular, genus-three congruence is equivalent to $C_E(P)=1$.

**Proof.** Conjugation on $P$ gives a homomorphism $E\to\operatorname{Aut}(P)$ and, after quotienting $P$, the usual outer monodromy of the closed genus-three surface. Thus an element of $C_E(P)$ maps into $C_{3,0}$. The restriction is injective because $C_E(P)\cap P=Z(P)=1$. If $c\in C_{3,0}$, choose $e\in E$ above it. Its action on $P$ is inner, say by $p\in P$. Then $p^{-1}e$ centralizes $P$ and maps to $c$. This proves surjectivity and the asserted equivalence. All maps are continuous; compactness makes the bijection a profinite isomorphism. The procongruence Birman sequence in Boggi (2020, Corollary 4.7, with Proposition 2.4(ii)) identifies this kernel with the one after adding or removing further punctures, as already proved in LM3 C.4. $\square$

## H.2. Proved — What centrality and torsion-freeness would require

*Manuscript connection: Auxiliary congruence problem attached to §26; folio 162; scan 320; LM3 B.3.*

\nopagebreak[4]


Boggi's procongruence center theorem does not establish that $C_{3,0}$ is central or torsion-free in the full profinite completion. What it does imply is
$$
 Z(\widehat\Gamma_{3,0})\subseteq C_{3,0},
$$
because $Z(\check\Gamma_{3,0})=1$ by Boggi (2020, Theorem 4.4). Likewise, the full kernel lies in the centralizer (H.1), not necessarily in the center of $E$.

**Proof and conditional sharpening.** The image of a central element under a surjection is central, giving the inclusion. A centralizer of a normal subgroup need not centralize the whole ambient group; the implication that would prove centrality is missing. If a torsion-free finite-index congruence subgroup $\Gamma_{3,0}[3]$ is good and its completion has finite cohomological dimension at every prime, then $C_{3,0}$ is torsion-free: it is contained in that completion, and a nontrivial finite cyclic subgroup of order $p$ would force infinite $p$-cohomological dimension. The point is that torsion-freeness of the discrete level group alone is insufficient to deduce torsion-freeness of its completion. We do not prove the additional completion hypothesis here. Thus centrality and torsion-freeness of the full genus-three kernel are retained as unresolved assertions in this audit, rather than imported from the procongruence center formulas. $\square$

## H.3. Proved — Finite-cover homology representations are congruence representations

*Manuscript connection: Auxiliary congruence problem attached to §26; folio 162; scan 320; LM3 B.3.*

\nopagebreak[4]


Let $\pi=\pi_1(S_3)$ and let $K\triangleleft\pi$ be characteristic of finite index. For $m\geq2$, put $L=[K,K]K^m$. Then $L$ is characteristic and of finite index in $\pi$, and the action of $\Gamma_3$ on the cover and on $H_1(K,\mathbf Z/m)$, with its unavoidable deck ambiguity, factors through
$$
                       \Gamma_3\longrightarrow\operatorname{Out}(\pi/L).
                                                               \tag{H.2}
$$
Every finite quotient obtained this way is therefore a congruence quotient. The same conclusion holds for a finite orbit of noncharacteristic covers after replacing their subgroups by a characteristic finite-index core.

**Proof.** Characteristicity of $L$ follows by applying every automorphism of $\pi$ to the characteristic subgroup $K$, its commutators and its $m$th powers. The quotient $K/L$ is the finite module $H_1(K,\mathbf Z/m)$, and $\pi/L$ remembers both this module and the deck quotient $\pi/K$. Thus an automorphism of $\pi$ trivial modulo $L$ is trivial on the indicated data. Changing a based representative by an inner automorphism acts by a deck transformation on the module, exactly the ambiguity named in the statement. For finitely many covers, there are only finitely many subgroups of each given index in the finitely generated group $\pi$; intersect their full automorphism orbits to obtain a characteristic finite-index subgroup $K$. Its subgroup $[K,K]K^m$ lies in the corresponding subgroup $[V,V]V^m$ for each cover subgroup $V$, giving the asserted factorization. $\square$

## H.4. Proved — An explicit finite congruence representation beyond base homology

*Manuscript connection: Auxiliary congruence problem attached to §26; folio 162; scan 320; LM3 B.3.*

\nopagebreak[4]


Take $K=\ker(\pi_3\to H_1(S_3,\mathbf F_2))$ and $L=[K,K]K^3$. Then
$$
                       |\pi_3/L|=64\cdot3^{258}.        \tag{H.3}
$$
The congruence representation $\Gamma_3\to\operatorname{Out}(\pi_3/L)$ does not factor through the action on $H_1(S_3,\mathbf Z)$: a separating Dehn twist has nontrivial image.

**Proof and reproducible certificate.** Write
$$
\pi_3=\langle a_1,b_1,a_2,b_2,a_3,b_3\mid
[a_1,b_1][a_2,b_2][a_3,b_3]=1\rangle.
$$
The degree-64 characteristic cover has genus $1+64(3-1)=129$, whence $\dim H_1(K,\mathbf F_3)=258$, proving (H.3). To detect a twist, it suffices to use the double cover with monodromy $a_1\mapsto1,a_2\mapsto1$ and the other four generators mapping to zero. It has genus five. The twist about the curve $c=[a_1,b_1]$ is represented by conjugating $a_1,b_1$ by $c$ and fixing the other four generators. It fixes the defining surface relation and acts trivially on base homology.

The program `ceh_checks.py` computes signed lifted edge paths, equivalently evaluated Fox derivatives, over $\mathbf F_3$. For the cellular complex of the double cover it obtains
$$
(\dim C_0,\dim C_1,\dim C_2)=(2,12,2),\quad
\operatorname{rank}d_1=\operatorname{rank}d_2=1,
$$
and therefore $\dim H_1=10$. The induced operator $T$ satisfies
$$
\operatorname{rank}_{H_1}(T-1)=1,\qquad (T-1)^2=0,
\qquad T^3=1,\quad T\ne1.
$$
The complete $12\times12$ chain matrix is in `ceh_checks.json`; the program checks the chain-map identities and all displayed ranks by exact elimination modulo three. This homology action factors through $\pi_3/L$, since $K$ is contained in the double-cover subgroup. An inner automorphism of $\pi_3/L$ acts on the latter cover's abelianization through its deck group of order two. The nontrivial operator $T$ has order three, so it cannot arise from an inner automorphism. Thus the separating twist survives (H.2). Since it is in the Torelli group, (H.2) does not factor through the ordinary symplectic representation. $\square$

## H.5. Open — Genus-three kernel triviality, centrality, and torsion-freeness

*Manuscript connection: Auxiliary congruence problem attached to §26; folio 162; scan 320; LM3 B.3.*

\nopagebreak[4]


The three residual assertions, for $C=C_{3,0}$, are
$$
 C=1,\qquad
 C\subseteq Z(\widehat\Gamma_{3,0}),\qquad
 C\text{ has no nontrivial element of finite order}.
$$
We have not proved or refuted any of these three assertions in this audit. Triviality would imply the other two. H.2 proves a center inclusion in the opposite direction and a conditional torsion-freeness criterion, but neither settles the corresponding residual assertion. For centrality the remaining implication is that the centralizer identified in H.1 centralizes the entire one-point mapping class group; for torsion-freeness it is the required control of finite subgroups in the full profinite completion, or the additional finite-cohomological-dimension hypothesis stated in H.2.

The finite quotients in H.3–H.4 are congruence by an explicit characteristic subgroup, and the calculation demonstrates information beyond the base symplectic quotient. It cannot detect a nontrivial $C_{3,0}$, because every quotient used factors through the very action defining congruence. No quantum representation quotient was constructed here. The smallest remaining structural assertion is $C_{\widehat\Gamma_{3,1}}(\widehat\pi_{3,0})=1$ in (H.1). A finite quotient witnessing failure would require a finite quotient of $\Gamma_3$ which does not factor through any characteristic finite quotient of $\pi_3$; calculations on homology of finite covers alone cannot provide one. Conversely, proving that all such cover-homology quotients are congruence, as we have done, supplies no cofinality statement among all finite quotients of $\Gamma_3$. This is the exact obstruction left after our attack.



The issue in LM3 F.18 is not the finite-set exodromy equivalence already proved there. It is comparison with finite homotopy types. We give that comparison at $\overline{\mathcal M}_{0,4}\simeq\mathbb P^1$, stratified by its three boundary points. We use the finite-object skeleton of the exit category, with arrows from a boundary point toward the open stratum. The comparison is in profinite stratified homotopy theory; an ordinary nerve of a finite category need not itself be a truncated finite homotopy type.

## H.6. Proved — A cofinal family of strict finite quotient categories

*Manuscript connection: §26; folios 165-166 (328 folio doubtful); scans 326-329; §29; folios 187 verso-188; scans 370-371; auxiliary higher-completion comparison attached to LM3 F.18.*

\nopagebreak[4]


Let $G=F(x,y)$ be the discrete free group, let $c_1=x,c_2=y,c_3=(xy)^{-1}$, and let $I_i=\langle c_i\rangle$. The four-object exit category $C$ has objects $u,p_1,p_2,p_3$, with
$$
\operatorname{Aut}(u)=G,\quad\operatorname{Aut}(p_i)=1,
\quad\operatorname{Hom}(p_i,u)=G/I_i,
$$
and no other nonidentity morphisms. For each finite-index normal $N\triangleleft G$, define $C_N$ by replacing $G$ with $Q_N=G/N$ and $I_i$ with its image $I_{i,N}$. Then $(C_N)_N$ is cofinal in the strict finite-category quotient completion of $C$.

**Proof.** This description of $C$ is the $n=4$ specialization of the transporter model in Jansen (2023, Construction 3.18 and Theorem 6.7), already used in LM3 F.1. A finite congruence on $C$ has a finite group quotient of $G=\operatorname{Aut}(u)$; call its kernel $N$. Its action on each quotient of $G/I_i$ is well-defined. If $g'I_i=gnI_i$ modulo $NI_i$, with $n\in N$, then composition by $n$ is the identity in that quotient, so the two arrows have the same image. Thus $C_N\to C/R$ is defined on every Hom-set and respects composition. This proves cofinality. It also explains why an arbitrary larger stabilizer of a quotient arrow does not introduce an extra completion: refining by the group kernel restores the displayed coset system. $\square$

## H.7. Proved — Finite-coefficient cohomology of the strict nerve

*Manuscript connection: §26; folios 165-166 (328 folio doubtful); scans 326-329; §29; folios 187 verso-188; scans 370-371; auxiliary higher-completion comparison attached to LM3 F.18.*

\nopagebreak[4]


For every finite abelian group $A$ with constant coefficients,
$$
\varinjlim_N H^q(NC_N;A)=
\begin{cases}A,&q=0,2,\\0,&q\ne0,2.
\end{cases}
$$
The degree-two class agrees, under the natural comparison, with the orientation class of $\mathbb P^1(\mathbb C)\simeq S^2$.

**Proof.** The groupoid of arrows $p_i\to u$, under target automorphisms, is the action groupoid of $Q_N$ on $Q_N/I_{i,N}$, and hence has classifying space $BI_{i,N}$. The realization of $NC_N$ is the homotopy pushout of the three diagrams
$$
BQ_N\longleftarrow BI_{i,N}\longrightarrow *.
$$
One can verify this without a nerve-realization interchange theorem: a nonconstant simplex has exactly one initial $p_i$ and then a string of target-group arrows. These are the mapping-cylinder simplices of the displayed action groupoid, and their faces give precisely the homotopy pushout.

Free groups and infinite cyclic groups are good for finite coefficients. In this case goodness follows directly from their one-dimensional free resolutions: the completed augmentation sequence for $\widehat F_2$ has two free profinite generators in degree one and no higher terms, and the procyclic analogue has one. Finite quotient cochains, taken in filtered colimit, compute their continuous cohomology. The topology induced on each $I_i$ is its full profinite topology: each $c_i$ is primitive in $F_2$ and admits a retraction to $\mathbb Z$; reduction of that retraction modulo any $m$ supplies the required finite-index intersections. Therefore
$$
\varinjlim_N H^q(Q_N;A)=H^q(\widehat F_2;A),\qquad
\varinjlim_N H^q(I_{i,N};A)=H^q(\widehat{\mathbb Z};A).
$$
The homotopy-pushout cochain triangle is compatible with $N$. Filtered colimits are exact on abelian groups. In degree zero its restriction map is
$$
A\oplus A^3\longrightarrow A^3,\quad
(a,b_1,b_2,b_3)\mapsto(a-b_1,a-b_2,a-b_3),
$$
which is onto and has diagonal kernel $A$. In degree one it is
$$
A^2\longrightarrow A^3,\quad(s,t)\mapsto(s,t,-s-t).
$$
This is injective; its cokernel is $A$, identified by the sum of the three coordinates. Higher group cohomology vanishes in the colimit. These facts prove the formula. The sum map is the boundary orientation relation of the three-punctured sphere, so its cokernel generator is the sphere's fundamental cohomology class. `fh_finite.py` checks the finite cochain kernel and cokernel for $A=\mathbb Z/m$, $2\leq m\leq39$; the proof applies to every finite $A$. No claim is made that the higher cohomology vanishes at each individual finite stage. $\square$

## H.8. Proved — The full profinite stratified comparison for four points

*Manuscript connection: §26; folios 165-166 (328 folio doubtful); scans 326-329; §29; folios 187 verso-188; scans 370-371; auxiliary higher-completion comparison attached to LM3 F.18.*

\nopagebreak[4]


The nerve of the strict finite-category completion in H.6 represents the profinite stratified homotopy type of $(\mathbb P^1,\{0,1,\infty\})$. In particular, LM3 F.18 has an affirmative answer at $n=4$, with the same strict quotient system that was used for finite-set coefficients.

**Proof.** We supply the higher comparison rather than deducing it solely from H.7's constant cohomology. Let $P$ be the poset with the three boundary strata below the open stratum. It has rank one. Its spatial décollage consists of the four stratum groupoids and the three arrow groupoids; there are no chains of length two with three distinct strata. For the original exit category these spaces are
$$
BG,\quad *,*,*,\quad BI_1,BI_2,BI_3,
$$
with the evident inclusion maps. For the strict quotient system they are
$$
(BQ_N)_N,\quad *,*,*,\quad(BI_{1,N})_N,(BI_{2,N})_N,(BI_{3,N})_N.
$$
The same free-group and cyclic-group goodness argument works for all finite local systems, not only the constant ones in H.7. Together with the identical profinite fundamental groups, it identifies the profinite completions of $BG,BI_i$ with these group-quotient systems. Equivalently, obstruction theory into a finite Postnikov tower is computed by these finite local-system cohomology groups, so the comparison is an equivalence when tested on every $\pi$-finite space. It is compatible with each inclusion $I_i\hookrightarrow G$.

Barwick, Glasman, and Haine (2020), Theorem 2.7.4, reconstruct stratified spaces from their spatial décollages. Their Example 2.6.4 makes the Segal condition vacuous in rank at most one, and Construction 2.8.8 with equation (2.8.9) gives the profinite décollage equivalence. Therefore the objectwise profinite completion just verified is already a profinite stratified space with the universal completion property: there are no higher chains whose homotopy fibre products would require an additional comparison. This proves the desired equivalence of stratified pro-objects. Theorem 10.4.3 is the corresponding topos-theoretic form under its bounded coherent constructible hypotheses. Their Corollary 12.6.7 identifies this with the stratified étale homotopy type over $\mathbb C$. Proposition 10.5.1 identifies its unstratified realization with the profinite completion of the homotopy pushout, namely the sphere. Thus no step interchanges arbitrary completion and an infinite homotopy limit. $\square$

## H.9. Open — What must be added beyond four points

*Manuscript connection: §26; folios 165-166 (328 folio doubtful); scans 326-329; §29; folios 187 verso-188; scans 370-371; auxiliary higher-completion comparison attached to LM3 F.18.*

\nopagebreak[4]


For all $n$, the desired comparison is the equivalence between the nerve of the strict finite-category quotient system of $C_n$ and the profinite stratified completion of $NC_n$. H.8 does not prove it once there are chains of three distinct strata. The first additional case is $n=5$.

Here is a precise sufficient condition, and the point at which our argument stops. For every chain $\tau$ in the stable-tree poset, form the groupoid of lifts of $\tau$ to $C_n$, with natural isomorphisms as arrows. Require that the groupoids obtained from the strict finite quotients form its full profinite homotopy completion, compatibly with chain restriction. In particular one must establish goodness of the stabilizer groups with the topology induced from the finite categorical quotients, and that these quotients compute the iterated homotopy fibre products for consecutive chains. Under this condition the décollage comparison is objectwise an equivalence, hence a stratified equivalence by the décollage reconstruction theorem. This proves the sufficiency of the named condition.

At $n=4$ the only nontrivial chain stabilizers are cyclic and the required topology is supplied by a retraction. At $n=5$ the two-step gluing compatibility is a new assertion; comparing only the stratum groups and finite sets does not prove it. We have computed the complete rank-one cohomology and higher comparison, but do not supply an all-$n$ chain-stabilizer and fibre-product proof. This is the exact remaining comparison, not a claimed counterexample for $n\geq5$.


# References

Baker, M., & Rabinoff, J. (2015). The skeleton of the Jacobian, the Jacobian of the skeleton, and lifting meromorphic functions from tropical to algebraic curves. *International Mathematics Research Notices*, *2015*(16), 7436-7472. <https://doi.org/10.1093/imrn/rnu168>.

*Source check:* verified: primary author preprint opened. Sections 4.1–4.2 and 4.5.2, Proposition 6.1 and Corollary 6.6 checked for toric uniformization, its covering property, and compatibility of the analytic and tropical Abel–Jacobi maps. Used in the independent proof of 019 Proposition 5.2.

Bar-Natan, D. (1998). On associators and the Grothendieck–Teichmüller group, I. *Selecta Mathematica. New Series*, *4*(2), 183-212. <https://doi.org/10.1007/s000290050029>.

*Source check:* Verified: primary full paper opened; Definition 2.4, Claim 2.6, Theorems 4 and 5, and Proposition 5.3 checked. Definition 2.4 fixes the braiding and therefore describes the multiplier-one version; the scalar extension is stated separately.

Barwick, C., Glasman, S., & Haine, P. J. (2020). *Exodromy*. arXiv:1807.03281, book draft of 21 August 2020. <https://www.maths.ed.ac.uk/~cbarwick/papers/exodromy_book.pdf>.

*Source check:* Verified: attached primary LaTeX source and public PDF opened. Example 2.6.4, Theorem 2.7.4, Construction 2.8.8 and equation 2.8.9, Theorem 10.4.3, Proposition 10.5.1 and Corollary 12.6.7 checked. Rank-one reduction written in H.8; no unrestricted interchange of completion with homotopy limits.

Belyi, G. V. (1980). On Galois extensions of a maximal cyclotomic field. *Mathematics of the USSR-Izvestiya*, *14*(2), 247-256. <https://doi.org/10.1070/IM1980v014n02ABEH001106>.

*Source check:* verified: attached primary English translation opened. Theorem 4 and its proof, pp. 255–256, checked, including rational polynomial postcompositions and the permitted inclusion of a prescribed finite set of algebraic values. Russian original published in 1979.

Boggi, M. (2020). Congruence topologies on the mapping class group. *Journal of Algebra*. <https://doi.org/10.1016/j.jalgebra.2019.11.004>.

*Source check:* Verified: supplied primary PDF opened; Theorem 1.4, Proposition 2.4, Theorem 4.4, Corollary 4.7 and Corollary 5.4(ii), and the stated scope for full versus procongruence completions checked. The supplied text is dated 12 July 2021 despite its older arXiv identifier.

Boggi, M. (2026). *Automorphisms of profinite mapping class groups*. <https://arxiv.org/abs/2011.15075>.

*Source check:* Verified: supplied version 6 of 22 April 2026 opened. Definitions in section 2.8, Theorems A, 2.8, 3.12, 6.1, 6.23, Lemma 6.25, Corollary 6.24 and equation (29) checked. The automatic-inertia caveat on page 3 is retained. No full independent audit of the preprint’s main proof is claimed.

Boggi, M., & Funar, L. (2023). Automorphisms of the procongruence curve and pants complexes. *Journal of Topology*, *16*, 936-989. <https://doi.org/10.1112/topo.12306>.

*Source check:* Verified: supplied primary PDF opened; Theorems 4.11 and 4.14, Corollary 4.12 and the center versus procongruence distinction checked.

Boggi, M., & Zalesskii, P. (2019). A restricted Magnus property for profinite surface groups. *Transactions of the American Mathematical Society*, *371*(1), 729-753. <https://doi.org/10.1090/tran/7311>.

*Source check:* verified: attached primary preprint opened. Definition 1.3 and Proposition 3.6 checked. Its normalizer assertion applies to every nonzero profinite exponent, including exponents supported at one prime, and to peripheral algebraically simple elements.

Boggi, M., & Zalesskii, P. (2025). Finite subgroups of the profinite completion of good groups. *Bulletin of the London Mathematical Society*, *57*(1), 236-255. <https://doi.org/10.1112/blms.13193>.

*Source check:* Verified: primary version 2 of 28 October 2024 opened; Theorem A(iii), Theorem 4.3 and the applications in section 6 checked. Used to descend geometric deck normalizers for the two genus-zero test coverings. The arbitrary-dense-embedding formulation and its all-discrete-module hypothesis were also checked for the pro-2 application.

Brown, F. (2012). Mixed Tate motives over $\mathbb Z$. *Annals of Mathematics*, *175*(2), 949-976. <https://doi.org/10.4007/annals.2012.175.2.10>.

*Source check:* Verified: attached primary paper opened. Theorem 1.1 and the introductory deduction of faithfulness of the mixed Tate action checked. Used as the established free motivic lower bound, independently of either 2026 upper-bound argument.

Dolgushev, V. A., Le, K. Q., & Lorenz, A. A. (2024). What are GT-shadows?. *Algebraic and Geometric Topology*, *24*, 2721-2777. <https://doi.org/10.2140/agt.2024.24.2721>.

*Source check:* Verified: attached full primary paper opened; Theorem 3.8, Theorem B.2 and Remark B.3 checked. The arithmetic half-parameter is treated modulo twice the shadow order when necessary. The computed family is explicitly abelian.

Drinfeld, V. G. (1990). On quasitriangular quasi-Hopf algebras and on a group that is closely connected with $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$. *Algebra i Analiz*, *2*(4), 149-181.

*Source check:* Verified: supplied primary Russian paper opened; Proposition 5.7 is also checked through its explicit citation and reformulation in Bar-Natan Theorem 5 and Willwacher section 1. The rational cabling consequence is not asserted integrally in all characteristics.

Grothendieck, A. (1981). *La longue marche a travers la theorie de galois*. Unpublished manuscript, cote 140-2; attached scans and provisional AI-assisted transcription packages.

*Source check:* Verified: the cited selected scans and corresponding transcription passages opened. The mathematics does not settle palaeographic alternatives. Section, folio and scan locators appear in the statements and result register.

Hain, R., & Matsumoto, M. (2003). Weighted completion of Galois groups and Galois actions on the fundamental group of $\mathbb P^1-\{0,1,\infty\}$. *Compositio Mathematica*, *139*(2), 119-167. <https://doi.org/10.1023/B:COMP.0000005077.42732.93>.

*Source check:* Verified: attached primary preprint opened. Theorem 7.3, Theorem 8.4, Lemma 8.5 and Remark 8.6 checked for the precise arithmetic image, weight-one removal and odd Tate abelianization. Arithmetic image is not substituted for all of GRT without the separate upper bound.

Hain, R., & Matsumoto, M. (2020). Universal mixed elliptic motives. *Journal of the Institute of Mathematics of Jussieu*, *19*(3), 663-766. <https://doi.org/10.1017/S1474748018000130>.

*Source check:* Verified: primary arXiv version 4, December 2017, opened in full, with Theorem 10.7, Proposition 20.1, Corollary 20.2, Remark 22.2, Theorem 22.3, Corollary 23.3, Proposition 29.1 and Remark 29.3 checked. Published metadata independently checked at Cambridge Core. Online publication 2018; issue publication 2020. The numbering used here is the verified arXiv version.

Hatcher, A., Lochak, P., & Schneps, L. (2000). On the teichmüller tower of mapping class groups. *Journal für die reine und angewandte Mathematik*, *521*, 1-24. <https://webusers.imj-prg.fr/~pierre.lochak/textes/crelle.pdf>.

*Source check:* Verified: supplied primary PDF rendered and visually read at pages 3–6 after text extraction failed; Theorems A–C and the arithmetic subgroup fixing roots of unity and of two checked.

Hoshi, Y. (2025). Homomorphisms of global solvably closed Galois groups compatible with cyclotomic characters. *Tohoku Mathematical Journal*, *77*(1), 17-32. <https://doi.org/10.2748/tmj.20230414>.

*Source check:* verified: primary revised author preprint opened at the stated URL. Theorem 3.4 checked in full: cyclotomic compatibility in the full profinite unit group is equivalent to existence of the equivariant field embedding. It is an input to the full manuscript 031 claim, not silently substituted for logarithmic compatibility.

Hoshi, Y., & Mochizuki, S. (2011). On the combinatorial anabelian geometry of nodally nondegenerate outer representations. *Hiroshima Mathematical Journal*, *41*(3), 275-342. <https://doi.org/10.32917/hmj/1323700038>.

*Source check:* Verified: attached primary full text opened; Theorem 6.1, manuscript pp. 61–63, read including its hypotheses, exact injectivity and surjectivity ranges, and proof reduction.

Hoshi, Y., Minamide, A., & Mochizuki, S. (2022). Group-theoreticity of numerical invariants and distinguished subgroups of configuration space groups. *Kodai Mathematical Journal*, *45*(3), 295-348. <https://doi.org/10.2996/kmj45301>.

*Source check:* Verified: attached primary full text opened; Corollaries 2.6(i) and 2.8(i), Definition 2.7 and their proofs read. The theorem covers both all primes and a singleton, and identifies generalized fiber subgroups intrinsically.

Hoshi, Y., Mochizuki, S., & Tsujimura, S. (2025). Combinatorial construction of the absolute Galois group of the field of rational numbers. *Journal of Mathematical Sciences, the University of Tokyo*, *32*(1), 1-125. <https://www.kurims.kyoto-u.ac.jp/~motizuki/Combinatorial%20absolute%20Galois%20groups.pdf>.

*Source check:* verified: supplied primary text dated March 14, 2025 opened. Theorems A–C, Definitions 3.3 and 5.12, Theorems 4.4, 5.15, 5.17 and 6.8, Corollary 4.5 and Remark 4.5.1 checked for the precise enriched data and conjugacy qualification. No independent reproof of the full source claimed.

Jansen, M. Ø. (2023). *Moduli stack of stable curves from a stratified homotopy viewpoint*. arXiv:2308.09551v2. <https://doi.org/10.48550/arXiv.2308.09551>.

*Source check:* Verified: primary arXiv version 2 opened; Construction 3.18 and Theorems 6.6–6.7 checked for the transporter category and its exit variance. Used only for the explicit first-level model and the source of the all-n question.

Koch, H., Kukkuk, S., & Labute, J. (1998). Nilpotent local class field theory. *Acta Arithmetica*, *83*(1), 45-64. <https://doi.org/10.4064/aa-83-1-45-64>.

*Source check:* Verified: primary full paper opened; Theorem 2.1 and its proof, pp. 48–49, checked. This lower-central theorem is over Z-p and includes p=2; the later restriction p greater than 2 in the paper is not a hypothesis of Theorem 2.1.

Minamide, A., & Nakamura, H. (2022). The automorphism groups of the profinite braid groups. *American Journal of Mathematics*, *144*(5), 1159-1176.

*Source check:* Verified: supplied primary PDF opened; Proposition 3.2 including its orbifold-fibre proof, Theorem 4.3 and Corollary C checked.

Mochizuki, S. (1999). The local pro-p anabelian geometry of curves. *Inventiones Mathematicae*, *138*, 319-423.

*Source check:* verified: attached primary author text opened. Theorem A, identified there with Theorem 16.5 and its following remark, checked for both full profinite and geometrically pro-p open Hom. Theorem C, identified with Theorem 19.1, checked for injectivity of the point-to-section map.

Nakamura, H. (1994). Galois rigidity of pure sphere braid groups and profinite calculus. *Journal of Mathematical Sciences, the University of Tokyo*, *1*, 71-136. <https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf>.

*Source check:* verified: attached primary text opened. Theorems A and B, including their odd-prime hypotheses; Theorem 2.1.1; Lemmas 2.1.2 and 2.1.4 and the complete weight argument on pp. 94–97 checked. Theorem 2.1.1 is stated for every full class of finite groups, including all finite groups and all finite l-groups.

Nakamura, H., & Schneps, L. (2000). On a subgroup of the Grothendieck–Teichmüller group acting on the tower of profinite Teichmüller modular groups. *Inventiones Mathematicae*, *141*, 503-560. <https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf>.

*Source check:* verified: attached primary text opened. Theorems 1.1, 1.2 and 2.1, Lemma 2.3, equation 2.4 and Proposition 5.3 checked for relations III-prime and IV and the Kummer cocycle of 2.

OpenAI (2026a). *LM3 TEICHMULLER TOWER: Supplied prior response*. Attached AI-produced research response by GPT-6 Astra, with paper, result and reading registers.

*Source check:* Verified: supplied paper and selected cited statements opened. Used for previously reviewed reductions as permitted by the task, not as authority for the twelve open rows or the new leads.

OpenAI (2026b). *Open homomorphisms of global solvably closed Galois groups*. Attached unrefereed preprint, October 5, 2026, proof pack 031.

*Source check:* verified as a source: attached October 5, 2026 primary manuscript opened. Lemma 3.1 and Propositions 4.3 and 5.3 independently proved, with finite-character amplification and the consequence Theorem 4.4. Sections 1–6 read. The full theorem is not automatically certified by the targeted audit. Unrefereed manuscript.

OpenAI (2026c). *The Deligne–Drinfeld conjecture*.

*Source check:* Verified as a source: attached September 23, 2026 manuscript 008 opened. Proposition 3.2 and the induction of section 4 independently rederived in G.8–G.9; other all-weight steps are not inferred from finite dimensions. Unrefereed manuscript.

OpenAI (2026d). *The p-adic section conjecture*. Attached unrefereed preprint, October 6, 2026, proof pack 019.

*Source check:* verified as a source: attached October 6, 2026 primary manuscript opened. Proposition 5.2 independently proved in this audit, including the model, character slope and a root on every inverse component. This does not certify the remaining collar-to-global proof or the complete local section theorem. Unrefereed manuscript.

Pop, F. (2018). *Finite tripod variants of I/OM on Ihara’s question/Oda–Matsumoto conjecture*.

*Source check:* verified: attached author manuscript dated December 24, 2018 opened. Definition/Remark 2.2, Hypothesis H, Theorems 2.6 and 2.7 and the birational tripod example checked. The reduction uses all required open localizations and the restricted maps s, t and t-s; the difference is not a global forgetting map.

Uchida, K. (1979). Isomorphisms of Galois groups of solvably closed Galois extensions. *Tohoku Mathematical Journal*, *31*(3), 359-362. <https://www.jstage.jst.go.jp/article/tmj1949/31/3/31_3_359/_pdf/-char/en>.

*Source check:* verified: all four pages of the primary journal paper opened. Main theorem and Lemma 3 checked. Used for the prescribed Galois-group isomorphism, uniqueness, centralizers and the normalizer extension.

Uchida, K. (1981). Homomorphisms of Galois groups of solvably closed Galois extensions. *Journal of the Mathematical Society of Japan*, *33*(4), 595-604. <https://doi.org/10.2969/jmsj/03340595>.

*Source check:* verified: primary journal paper opened. Section 1, pp. 595–597, the odd-prime local trichotomy and Proposition 1 checked for open maps and cofinite target coverage at a fixed prime; Proposition 2 checked for uniqueness. No uniform bound in the auxiliary prime is attributed to this source.

Willwacher, T. (2026). *The Deligne–Drinfeld conjecture after OpenAI*. <https://arxiv.org/html/2610.15592v4>.

*Source check:* Verified: attached and public arXiv version 4, dated October 28, 2026, opened. Theorems 1.1 and 2.2, Proposition 3.2 and sections 3.1–3.3 rederived in G.10. Its optional section 4.4 lower-bound proof is not needed: Brown supplies the lower bound. Unrefereed preprint.
