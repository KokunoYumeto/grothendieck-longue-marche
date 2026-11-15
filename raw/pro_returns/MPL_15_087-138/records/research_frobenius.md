# Candidate research notes: Frobenius, CM fields, and the two requested bridges

Prepared after the transcription freeze and authorized context opening. These are candidate notes for the primary reader, who owns the final synthesis. No image was consulted and no frozen page was changed. README.md and notes/RESULTS_STATE.md were read completely; the register's own status qualifications remain in force. In the references below, CT means context/MPL_16+47+54+44_transcription.tex, and CN means context/MPL_16+47+54+44_notes.md; both are supplied first-pass material.

## Notes on the current manuscript

### FR01 — Evaluation at Frobenius is the exact character map

**Location / kind:** cote 15, scans 088 line 7 and 090 lines 3–12; unpursued implication, with an explicit calculation. **Quote:** “engendré (au sens de Zariski) par f”. **Context / register:** search “M(q)”, “Frobenius”, “semi-simple”; CT 16/049 supplies the semisimple-motive programme, while these pages add the character evaluation and a designated generator; bears on WG2 §2.4 #3 and WG2 §2.3 #7.

The map in the first equivalence table is \(X^*(T_{\overline{\mathbb Q}})\to\overline{\mathbb Q}^{\,*}\), \(\chi\mapsto\chi(f)\), and its compatibility with Galois follows from \(f\in T(\mathbb Q)\). Its kernel is zero because \(\chi(f)=1\) puts the Zariski closure of the powers of \(f\), hence the written \(T\), inside \(\ker\chi\). The grading is the actual homomorphism \(j^*:M\to\mathbb Z\), and the written relation \(\varepsilon j(t)=t^\alpha\) is \(j^*(\varepsilon)=\alpha\); this is the concrete correspondence between the group, eigenvalue, and grading columns.

### FR02 — The listed closure operations need the surrounding rigidity

**Location / kind:** cote 15, scan 090 line 6; own idea, confidence high because the tensor category and its embedding are explicit. **Quote:** “stable par \(\otimes\), \(\oplus\), sous objet”. **Context / register:** search “catégorie”, “modules”, “semi-simple”; CT 16/018 and 16/049 discuss modules and the motivic category; this checks the operational content of the new table, bearing on WG2 §2.4 #3.

Finite direct sums of the one-dimensional \(\mathbb Q[X]\)-modules with \(X\) acting as \(2^n\), \(n\in\mathbb N\), form a full semisimple subcategory closed under every operation listed on the page, but the dual of the eigenvalue-\(2\) object has eigenvalue \(2^{-1}\) and is absent. The exact tensor embedding into finite \(\mathbb Z\)-graded vector spaces, with \(f\) acting by \(2^n\) in degree \(n\), is induced by \(\mathbb N\hookrightarrow\mathbb Z\); adjoining duals implements this group completion. The motivic setting of scan 088 supplies the relevant rigidity, so this example records an implicit requirement of the table rather than proposing a transcription change.

### FR03 — The deleted rank-two counterexample does not satisfy the displayed weight equation

**Location / kind:** cote 15, scans 090 lines 20–28 and 092 lines 19–22; withdrawn argument / own calculation, confidence high. **Quote:** deleted “sous-groupes libres de \(Q^*\) de rang \(\geq2\)”. **Context / register:** search “positive”, “semi-simple”, “index”; CT 16/049 connects positivity with semisimplicity, but has no version of this character calculation; bears on WG2 §2.4 #3.

For the concrete rank-two group \(M=\langle2,3\rangle\), the displayed equation \(|m|=q^{j^*(m)/\alpha}\) gives \(2^{j^*(3)}=3^{j^*(2)}\), and the 2- and 3-adic valuations force both exponents to vanish, contradicting the two positive absolute values. Thus this group does not instantiate conditions b) and c) of scan 090. The counterexample paragraph is cancelled and marked with a marginal question mark on scan 092; both its cancellation and the attempted reverse implication on 090 should remain visible in the notes.

### FR04 — The norm-one divisor argument has a concrete finite-index obstruction

**Location / kind:** cote 15, scans 096 lines 3–10, 098 lines 5–7, and 114 line 3; unpursued implication / own calculation, confidence high. **Quote:** “d'indice fini”. **Context / register:** searches “norm-one”, “class group”, “M(q)” found no counterpart to this construction in CT; CT 16/049 is the neighbouring motive programme, and this adds arithmetic integral-lattice data; bears on WG2 §2.4 #3.

The written construction is \(x=y/\sigma y=y^2/Ny\), so its divisor is \(2h(\mathfrak p-\sigma\mathfrak p)\) and its norm is exactly one; the proposition's existential positive multiplier therefore survives the factor \(2\). The later lattice map is \(u\mapsto(v_{\mathfrak p}(u))_{\mathfrak p\mid p}\), with target the anti-invariant divisor lattice. FR14 below supplies an actual index-three image, explaining why the passage from “finite index” to equality is a substantive issue on 112–114.

### FR05 — The literal \(K\) in the eigenvalue sentence on 098

**Location / kind:** cote 15, scan 098 line 3; reading question with a concrete test. **Quote:** “les \(\lambda\in K\) entiers”. **Context / register:** search “norme”, “M(q)”, “CM”; no corresponding CM arithmetic appears in CT, while the present scan adds the valuation model to the programme of CT 16/049; bears on WG2 §2.4 #3.

The same sentence declares \(K\) totally real and \(L/K\) quadratic totally imaginary, so its literal \(\lambda\in K\) gives \(\lambda\bar\lambda=\lambda^2\). For \(K=\mathbb Q\), \(L=\mathbb Q(i)\), \(q=25\), the integer \(3+4i\) has norm \(25\), and \((3+4i)/5=(2+i)/(2-i)\) supplies a nontrivial norm-one 5-unit in \(L\), whereas the rational solutions of \(\lambda^2=25\) are just \(\pm5\). This tests the precise letter against the objects used later in the paragraph; the frozen \(K\) is retained.

### FR06 — Two explicit exponent normalizations on 100

**Location / kind:** cote 15, scan 100 lines 15–17; reading question / own calculation, confidence high for the calculation, not an additional ink judgment. **Quote:** `\lambda^{\unsure{2}}=q^{i/2}u`. **Context / register:** search “weight”, “poids”, “Tate”; CT 16/021 provides the Tate sheaf, and the current page adds a numerical weight formula; bears on MPL_14_002-044 B04 and §3, both supplied register leads.

The frozen first reading of the superscript as \(2\), together with the written absolute-unit property, gives \(|\lambda|=q^{i/4}\), while the inserted box gives \(|\lambda_\alpha|=q^{i/2}\). The explicit values \(q=4\), \(i=1\), \(u=1\), and \(\lambda=\sqrt2\) satisfy the former equation and not the box's absolute value \(2\). This isolates the exponent reading without silently replacing either formula.

### FR07 — The change-of-base weight sentence omits a denominator in its present reading

**Location / kind:** cote 15, scan 100 line 33; reading question / own calculation, confidence high. **Quote:** “le poids \(i\) … est égal à \(mi'\)”. **Context / register:** CT 16/021 and register MPL_14_002-044 B04; the present page supplies a numerical base-extension comparison absent from that CT passage.

The two absolute-value equations with \(q=p^n\) and \(q'=p^m\) give \(ni=mi'\), by taking real logarithms base \(p\). For \(\lambda=\sqrt p\), \(q'=p\), and \(q=p^2\), they give \(i'=1\) and \(i=1/2\), so even the asserted availability of an integral weight for every \(q\) needs examination. The source's \(mi'\) and its surrounding quantifiers remain unchanged.

### FR08 — The strong eigenvalue conjecture has a later explicit realization construction

**Location / kind:** cote 15, scan 100 lines 39–41; manuscript conjecture and later-result comparison. **Quote:** “Conjecture forte … suffisantes”. **Context / register:** CT 16/049 gives the semisimple-motive programme; CN S17 discusses finite-field Frobenius projectors at CT 16/046–048; this adds an existence construction to WG2 §2.3 #7 and §2.4 #3, while preserving FR06–FR07.

For the boxed absolute-value formulation of positive integral weight \(i\), choose \(\beta^i=\lambda\): integrality follows from the monic equation \(T^i-\lambda\), and every conjugate of \(\beta\) has modulus \(q^{1/2}\). Honda–Tate supplies \(A/\mathbb F_q\) with eigenvalue \(\beta\) for the Frobenius endomorphism \(\pi\) on \(V_\ell A\), \(\ell\ne p\) [HT, Theorem 1(i), p.96]. On \(H^1_{\mathrm{et}}(A_{\overline{\mathbb F}_q},\mathbb Q_\ell)=\operatorname{Hom}(V_\ell A,\mathbb Q_\ell)\), geometric Frobenius acts by \(\varphi\mapsto\varphi\circ\pi\), and the external-product Künneth map \(H^1(A)^{\otimes i}\hookrightarrow H^i(A^i)\) sends an eigenvector tensor over \(\overline{\mathbb Q}_\ell\) to an eigenvector of eigenvalue \(\beta^i=\lambda\). This supplies eigenvalue occurrence, while identification of the manuscript's motivic group also involves the realization map \(\operatorname{Hom}_{\mathrm{mot}}(M,N)\otimes\mathbb Q_\ell\to\operatorname{Hom}_{\mathrm{Frob}}(H_\ell M,H_\ell N)\), its fullness, the gerbe class, and scan 088's stipulated Zariski-generating tensor automorphism, none of which is proved by this eigenvector construction.

### FR08b — Zero and negative weights have elementary tests

**Location / kind:** cote 15, scan 100 lines 11–17 and 39; own calculation, confidence high from norms and bounded integer polynomials. **Quote:** “\(i\in Z\)”. **Context / register:** the same CT 16/049, CN S17, and WG2 §2.3 #7 / §2.4 #3 relations as FR08; this completes the weight range of its numerical test.

A nonzero algebraic integer of degree \(d\) with all conjugate moduli \(q^{i/2}\), \(i<0\), would have a nonzero integer norm of absolute value \(q^{id/2}<1\), a contradiction. At weight zero the monic polynomials \(\prod_\sigma(T-\sigma(\lambda)^n)\) have integer coefficients bounded by the binomial coefficients in degree \(d\), so only finitely many polynomials, and hence finitely many values \(\lambda^n\), occur; thus \(\lambda\) is a root of unity. For its order \(r\), the finite étale, smooth projective \(\mathbb F_q\)-scheme \(\operatorname{Spec}\mathbb F_{q^r}\) has Frobenius acting as an \(r\)-cycle on \(H^0\), whose eigenvalues include \(\lambda\).

### FR09 — The “geometric” expectation has the advertised CM antecedent

**Location / kind:** cote 15, scan 106 lines 3–15; conjecture / self-flagged expectation. **Quote:** “Résulte probablement … Taniyama–Shimura”. **Context / register:** CT 54/005–007 provides the \(p\)-kernel and \(F,V\) comparison; the present page adds CM eigenvalue existence, bearing on WG2 §2.4 #3 and the register's abelian-motive leads MPL_14_087-132 M10.

The written weak conjecture permits a positive power and records \(D(M_0\otimes\mathbb Q)\times G_m\) as its proposed group. Tate's later proof uses CM reduction to realize a power, followed by restriction of scalars to recover the prescribed Weil number [HT, §3, Lemmas 1–3, pp.100–101; §4, pp.102–105]. This is a precise later realization of the method named in the margin; the literal \(p\), \(q\), and \(f_{q^m}\) normalizations remain reading questions.

### FR10 — The finite-field transition has an exact dual sequence

**Location / kind:** cote 15, scan 102 lines 12–27; unpursued implication. **Quote:** “élévation à la puissance \(m\)”. **Context / register:** search “Tate”, “torsion”, “Galois”; CT 16/021 records Tate inverse limits and torsion, and current 102 adds an explicit motivic base-extension morphism; bears on MPL_14_002-044 B04 and WG2 §2.4 #3.

The written map \(P_m:M(q)\to M(q^m)\), \(\lambda\mapsto\lambda^m\), has kernel \(\mu_m\), while its cokernel \(C_m\) is annihilated by \(m\) through the displayed subgroup inclusions. Cartier duality gives the exact sequence \(1\to D(C_m)\to G(q^m)\to G(q)\to D(\mu_m)\to1\), with \(D(\mu_m)\) the constant \(\mathbb Z/m\mathbb Z\) group. The arrow sends the designated Frobenius to \(f_q^m\); this records both the finite component quotient and the possible kernel without silently dropping the latter.

### FR11 — A cancelled saturation question precedes the geometric conjecture

**Location / kind:** cote 15, scan 104 lines 11–26; withdrawn question / self-flagged unresolved step. **Quote:** “Trouve-t-on … tout entier?” and “\(m\) convenable??”. **Context / register:** search “torsion”, “divisible”, “Tate”; CT 16/021 relates rationalization and torsion, whereas this page asks a saturation question for the actual eigenvalue group; bears on WG2 §2.4 #3.

The root-taking description \(\lambda\mapsto\lambda^{1/n}\bmod U\) and the ensuing surjectivity question occur inside one cancelled block. The live margin asserts a rationalized weight-zero group, and scan 106 then labels the geometric realization a weak conjecture. These textual states should be recorded together rather than treating the cancelled saturation calculation as a completed proof.

### FR12 — The total-reality subgroup criterion is corrected by the later explicit fixed-field construction

**Location / kind:** cote 15, scan 108 line 3 and scan 128 line 14; reading question / exact comparison. **Quote:** “\(H\) ne contient aucun conjugué de \(\tau\)”. **Context / register:** search “conjugaison”, “Galois”, “CM”; no matching CM fixed-field construction occurs in CT; adds to WG2 §2.4 #3 and the weights/normalizers lead MPL_14_002-044 B04.

For a finite subfield \(K=\overline{\mathbb Q}^{\,H}\), the real embeddings are exactly \(\{gH:g^{-1}\tau g\in H\}\), since \(\tau(gx)=gx\) for every \(x\in K\) is the displayed membership condition. In particular \(K=\mathbb Q\), \(H=G_{\mathbb Q}\) is totally real and contains \(\tau\), directly testing the “ne … aucun” wording. Scan 128 instead identifies the maximal totally real field with the fixed field of the closed normal subgroup generated by all conjugates of \(\tau\); this later construction supplies the matching exact subgroup map.

### FR13 — The quadratic polynomial and its marginal trace have opposite signs

**Location / kind:** cote 15, scan 108 lines 5–7; reading question / own calculation, confidence high. **Quote:** “\(x^2+ax+b=0\)” and “\(a=x+{}^\sigma x\)”. **Context / register:** CT has no matching CM quadratic construction under the searches above; the later current scan 131 supplies a direct internal comparison, bearing on WG2 §2.4 #3.

The expansion \((T-x)(T-\sigma x)=T^2-(x+\sigma x)T+x\sigma x\) gives the exact coefficient comparison. Scan 131 writes \(\lambda^2-a\lambda+Q=0\) with \(a=\lambda+\bar\lambda\), so the later page exhibits the minus sign associated with the same trace expression. Neither occurrence in 108 is altered.

### FR14 — An explicit answer to “demander à Serre?”

**Location / kind:** cote 15, scans 098, 112, and 114; own calculation, confidence high from norms and ideal factorization. **Quote:** “\(\operatorname{Pic}(A)\) … non \(2\)-groupe”. **Context / register:** searches “class group”, “norm-one”, “CM” in CT and CN provide no corresponding example; this adds a concrete obstruction to WG2 §2.4 #3.

Put \(L=\mathbb Q(\sqrt{-23})\), \(\omega=(1+\sqrt{-23})/2\), \(\mathcal O_L=\mathbb Z[\omega]\), and \(\mathfrak p=(2,\omega+1)\); the norm formula is \(N(a+b\omega)=(a+b/2)^2+23b^2/4\), which never equals \(2\), so \(\mathfrak p\) is nonprincipal. The integer \(\alpha=1+\omega\) has norm \(8\), lies in \(\mathfrak p\) but not \(\bar{\mathfrak p}\), and therefore \((\alpha)=\mathfrak p^3\), proving that \([\mathfrak p]\) has order three and conjugation acts nontrivially by inversion. The norm-one 2-unit divisor map consequently has image \(3\mathbb Z(\mathfrak p-\bar{\mathfrak p})\), generated by \(\alpha/\bar\alpha\), so its cokernel is explicitly \(\mathbb Z/3\mathbb Z\). LMFDB independently lists the full class group as \(C_3\) [NF23]; the calculation only needs the exhibited order-three class.

### FR15 — The inserted \(f_0\) needs a character-value check

**Location / kind:** cote 15, scan 112 line 22, compared with 090 line 12 and 094 line 36; reading question / own calculation, confidence high. **Quote:** “\(f_0=f\,j(p^{1/2})\)”. **Context / register:** CT 16/021 contains the Tate object; these pages add the pair \((j,\varepsilon)\), bearing on MPL_14_002-044 B04 and WG2 §2.4 #3.

The written equations \(\varepsilon(f)=q\) and \(\varepsilon j(t)=t^2\) give \(\varepsilon(f\,j(p^{1/2}))=qp\). Thus the displayed product has the computed character value \(qp\), whereas its stated weight-zero role calls for character value \(1\). This is an exact type/value check on the frozen insertion, with no substituted inverse or square root in the transcription.

### FR16 — The lifting statement concerns a point torsor as well as a lattice

**Location / kind:** cote 15, scan 112 line 22; unproved claim / concrete scope check. **Quote:** “ne se relève … que si \(\varphi\) est un isom”. **Context / register:** CT 16/049 discusses algebraic inverse maps, while the current page adds rational lifting across an isogeny; bears on WG2 §2.4 #3.

For the written isogeny, the actual obstruction attached to \(f_0\) is the fibre torsor \(\varphi^{-1}(f_0)\) under \(\ker\varphi\), or its class in \(H^1(\mathbb Q,\ker\varphi)\). The explicit non-isomorphic isogeny \([2]:G_m\to G_m\) has the rational lift \(2\mapsto4\), so the asserted necessity uses more than the mere isogeny property. FR14 supplies the class-group obstruction in the manuscript's valuation construction; a proof of the written necessity must identify the designated Frobenius evaluation point with that obstruction, rather than infer it from the nonzero lattice cokernel alone.

### FR17 — The cancelled fixed-field norm assertion already fails over \(\mathbb Q(i)\)

**Location / kind:** cote 15, scan 132 line 13; withdrawn claim / own calculation, confidence high. **Quote:** “\(L\) est engendré par un \(\lambda\) tel que \(\lambda\bar\lambda=Q\)”. **Context / register:** CT contains no matching fixed-field norm claim under the CM/norm searches; the current withdrawal adds a specific arithmetic issue to WG2 §2.4 #3.

Take the prescribed field \(L=\mathbb Q(i)\) and the scalar \(Q=3\). A rational solution of \(N(a+bi)=3\) would give a primitive integer solution \(x^2+y^2=3z^2\); reduction modulo \(3\) forces \(3\mid x,y\), and then \(3\mid z\), a contradiction. This directly tests the first clause of the cancelled assertion, before any integrality requirement.

### FR18 — The cancelled integrality assertion fails even when the prescribed norm is attained

**Location / kind:** cote 15, scan 132 line 13; withdrawn claim / own calculation, confidence high. **Quote:** “Si \(Q\in Z\), on peut … \(\lambda\) entier”. **Context / register:** FR14's context search applies; this supplies a second exact test of the same withdrawn statement, bearing on WG2 §2.4 #3.

In \(L=\mathbb Q(\sqrt{-23})\), the element \((3+\sqrt{-23})/4\) generates \(L\) and has norm \(2\). The norm formula of FR14 gives no algebraic integer of norm \(2\): \(b\ne0\) contributes at least \(23/4>2\), and \(b=0\) would require \(a^2=2\). Thus the cancelled integrality clause has a concrete failure with its preceding norm and generation clauses satisfied.

### FR19 — The replacement and root-taking argument preserve integrality in the enlarged field

**Location / kind:** cote 15, scan 132 lines 15–17 and scan 133 line 2; unpursued implication / own calculation, confidence high from monic equations and an explicit field inclusion. **Quote:** “contenant \(K\)” and “\(\lambda'=\lambda^{1/i}\)”. **Context / register:** CT has no counterpart under the CM/norm searches; this identifies exactly what the live replacement changes, bearing on WG2 §2.4 #3.

For the manuscript's integral scalar \(Q>1\) and integral generator \(a\), the chosen positive \(i\) gives an integral \(\lambda\) from \(T^2-aT+Q^i\), and \(\lambda'\) is integral by \(T^i-\lambda\) and transitivity of integrality; the identity \(a=\lambda+Q^i/\lambda\) gives the actual inclusions \(K=\mathbb Q(a)\subset\mathbb Q(\lambda)\subset\mathbb Q(\lambda')\). Concretely, \(\alpha=(3+\sqrt{-23})/2\) satisfies \(\alpha^2-3\alpha+8=0\), and \(\pi^3=\alpha\) gives the monic equation \(\pi^6-3\pi^3+8=0\), with every conjugate of \(\pi\) of modulus \(\sqrt2\). The exact inclusion \(\mathbb Q(\sqrt{-23})=\mathbb Q(\pi^3)\subset\mathbb Q(\pi)\) is strict by FR18's norm-two obstruction; in fact the degree is six because a cubic root in the quadratic field would itself be an integer of norm two. This proves the advertised root-integrality step while locating precisely the field enlargement that the cancelled prescribed-\(L\) assertion did not permit.

### FR19b — The enlarged field and its conjugation are explicit

**Location / kind:** cote 15, scan 132, live remark and proof; scan 133, entire continuation; own calculation, confidence high from the displayed polynomial and conjugation identities. **Quote:** “contenant \(K\)”; “purement imaginaire”. **Context / register:** searches for CM, norme, conjugaison and corps in CT/CN give no parallel field-generation proof; adds to the open CM-field setting of **LM6 A.22** and **WG2 §2.4 #3**, without constructing the procyclic subgroup of A.22.

For the source's rational scalar \(Q>1\), take its integral generator \(a\) of the totally real field \(K\), and its positive integer \(i\) satisfying \(4Q^i-\sigma(a)^2>0\) at every embedding; the roots of \(T^2-aT+Q^i\) are nonreal and have squared modulus \(Q^i\) at every embedding. The identity \(a=\lambda+Q^i/\lambda\) proves \(K\subset\mathbb Q(\lambda)=K(\lambda)\), and \(\lambda=(\lambda')^i\) gives \(K\subset\mathbb Q(\lambda')\). Every conjugate of \(\lambda'\) is nonreal, has squared modulus \(Q\), and satisfies \(\overline{\lambda'}=Q/\lambda'\) and \(\sigma(\overline{\lambda'})=Q/\sigma(\lambda')=\overline{\sigma(\lambda')}\), so conjugation preserves \(\mathbb Q(\lambda')\) and its fixed field is totally real. The extension over that fixed field has degree two, which verifies the claimed CM field enlargement; the source's extra integral-\(Q\) assertion is the monic-equation calculation in FR19.

### FR20 — A sign remains in the “real, trivial case” margin

**Location / kind:** cote 15, scan 094 line 45; reading question / own calculation, confidence high. **Quote:** “\(\lambda=(q^{1/2})^i\)”. **Context / register:** CT 16/021 and register MPL_14_002-044 B04 supply the nearest Tate/weight comparison; this is an additional scalar check on the current weight formulation.

The value \(\lambda=-2\), \(q=4\), \(i=1\) satisfies the written norm and conjugate-absolute-value conditions, while the margin's displayed expression equals \(2\). The equation immediately preceding it, \(\lambda^2=q^i\), retains both square roots. The sign issue stays in the research notes.

### FR20b — The cancelled quartic example fails the rational common-norm premise

**Location / kind:** cote 15, scan 094, cancelled lower margin; scan 131, opening proposition; own calculation / withdrawn in the same text, confidence high by the four roots of the polynomial. **Quote:** “\(\lambda=p^{1/4}\)”; “\(\lambda_\alpha\bar\lambda_\alpha=Q\)”. **Context / register:** the norm and conjugation searches in CT/CN have no matching example; this adds the exact premise check to **MPL_14_002-044 §3**, **§108**, and **WG2 §2.4 #3**.

For a rational prime \(p\), the four conjugates of \(p^{1/4}\) are \(\pm p^{1/4},\pm i p^{1/4}\), and all their squared moduli equal \(\sqrt p\). This common value is irrational, so the example does not satisfy the rational-common-norm premise subsequently stated on scan 131; relative to \(q=p\), the equation \(q^{i/2}=p^{1/4}\) gives the nonintegral weight \(i=1/2\). The example and its cancellation are therefore recorded with the exact failed premise, without altering either textual state.

## Requested linear/non-linear comparison: explicit morphisms

### FR21 — Tate Hom and anabelian Hom meet through Abel–Jacobi and geometric abelianization

**Location / kind:** cote 15, 088 line 7 and 090 lines 3–10; requested bridge / unpursued implication. **Quote:** “catégorie des vectoriels … avec endomorphisme”. **Context / register:** CT 44/008 identifies Picard/Albanese endpoints and a Tate-module realization; CT 16/021 identifies the Tate sheaf; bears on MPL_14_002-044 §3 and MPL_14_087-132 §81, whose full source files are not supplied.

Tate's finite-field map is \(\mathbb Z_\ell\otimes\operatorname{Hom}_k(A,B)\to\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)\), and his Main Theorem makes it bijective [T66, §1, p.134]. Mochizuki's anabelian map is \(f\mapsto[\pi_1(f)]\) from dominant morphisms of hyperbolic curves over a sub-\(p\)-adic field to continuous open homomorphisms over \(G_K\), modulo geometric inner conjugation [M, Theorem A, p.3; Theorem 16.5]. For smooth proper curves the explicit connecting operation is restriction to geometric groups, abelianization, and passage to the pro-\(\ell\) quotient, identified by Abel–Jacobi with \(T_\ell J_C\); choosing geometric basepoints \(x,f(x)\) makes the Abel–Jacobi square commute, so on a curve morphism the resulting map is \(T_\ell(f_*:J_X\to J_Y)\) [JV, Proposition 9.1, p.30; Corollary 9.6, p.32]. Geometric inner conjugation disappears on this abelian quotient, and the field specifications of both cited bijectivity results remain attached to their respective maps.

### FR22 — Weights and cyclotomic normalizers share an exact one-dimensional representation

**Location / kind:** cote 15, 090 lines 10–23, 100 line 33, and 102 lines 12–25; requested bridge / own calculation, confidence high for the explicit Kummer action. **Quote:** “\(j^*:M\longrightarrow Z\)”. **Context / register:** CT 16/021 explicitly writes \(\mathbb Z_\ell[1]=\varprojlim\mu_{\ell^\nu}\); bears on MPL_14_002-044 B04, LM6 A.50 (register claim), and the open LM6 A.22 without claiming to settle it.

On the Kummer cover \(t=s^{\ell^n}\), inertia acts by \(\tau_\zeta(s)=\zeta s\), and a coefficient-Galois lift gives \(\sigma\tau_\zeta\sigma^{-1}=\tau_{\sigma\zeta}=\tau_\zeta^{\chi_\ell(\sigma)}\). Passing to the inverse limit gives the explicit normalizer representation on \(\mathbb Z_\ell(1)\); arithmetic Frobenius has \(\chi_\ell(\mathrm{Frob}_q)=q\), and inversion gives \(q^{-1}\) for geometric Frobenius. On the dual \(\mathbb Q_\ell(-1)=\operatorname{Hom}(\mathbb Q_\ell(1),\mathbb Q_\ell)\), geometric Frobenius acts by \(q\), which realizes the positive-weight-two character \(\varepsilon\) with \(\varepsilon j(t)=t^2\); this duality and inversion give the precise correspondence of conventions. Base extension sends Frobenius to its \(m\)-th power and \(q\) to \(q^m\), matching \(f_{q^m}\mapsto f_q^m\); the separate subgroup-existence question LM6 A.22 retains its open register status.

### FR23 — The supplied Oda theorem completes a particular \(p\)-linear comparison already present in the context

**Location / kind:** current cote 15, 106 line 15 and 110–112; contextual link, using a supplied primary source. **Quote:** “théorie des multiplications complexes”. **Context / register:** CT 54/003, 54/005, and especially 54/007 ask for the extension determined by \(A[p]\); CN D05 is a first-pass lead, here checked against Oda; bears on WG2 §2.4 #4 and the abelian-motive lead MPL_14_087-132 M10.

Oda's supplied paper, Corollary 5.11 on printed p.131, gives a canonical Dieudonné-module isomorphism \(M(A[p])\simeq H^1_{\mathrm{dR}}(A)\) over a perfect field of characteristic \(p\), carrying its stated submodule to \(H^0(A,\Omega_A^1)\) and its exact sequence to the Hodge sequence. This verifies the specific comparison sought in CT 54/007, while the current finite-field pages add the norm and valuation data used in a CM/Frobenius existence programme. Oda's immediately following remark attributes the conjecture to Grothendieck's 1966 de Rham paper, bibliography item [15]; it does not identify this particular handwritten sheet as the cited source.

## Context-search ledger and source limits

- CT searches for the exact arithmetic vocabulary “Taniyama”, “Shimura”, “M(q)”, standalone “CM”, “class group”, and “norm-one” returned no corresponding arithmetic construction. CN has nearby discussions of cohomological and divisor structures, but no construction matching the explicit norm-one 2-unit example above.
- CT and CN searches for “cyclotom”, “normalisateur/normalizer”, and “anabél/anabelian” returned no occurrence. The requested bridges are explicit comparisons added in these notes, keyed to the planning/register entries rather than attributed to an absent statement in the context.
- The actual shared objects were checked at CT 16/021 (Tate inverse limit and Kummer sequence), 16/049 (semisimple motive programme and algebraic inverse maps), 54/003–007 (dual abelian varieties, de Rham extension, \(p\)-kernel, \(F,V\)), and 44/008 (Picard/Albanese and Tate-module realization).
- CN D05's Oda comparison was checked directly against the supplied paper, printed p.131 / PDF page 70. No claim from an earlier run was used as a substitute for that primary text.
- Register entries LM6 A.50 and LM6 A.22 are supplied as summaries with stated run statuses; their full return proofs are not in this context archive. Nothing here re-proves A.50 or claims a solution of A.22.

## Verified primary references

- **[HT]** John Tate, “Classes d'isogénie des variétés abéliennes sur un corps fini (d'après T. Honda)”, Bourbaki exposé 352, talk November 1968, volume published 1971, pp.95–110. Checked Theorem 1(i), printed p.96; §3, Lemmas 1–3, pp.100–101; §4, pp.102–105. https://www.numdam.org/article/SB_1968-1969__11__95_0.pdf
- **[T66]** John Tate, “Endomorphisms of Abelian Varieties over Finite Fields”, Inventiones mathematicae 2 (1966), pp.134–144. Checked §1, displayed map (1) and Main Theorem, p.134; rationalized map (2), Lemma 1, p.135. https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf
- **[M]** Shinichi Mochizuki, “The Local Pro-p Anabelian Geometry of Curves”, author-hosted version. Checked Introduction, Theorem A, PDF p.3, including sub-\(p\)-adic base, open morphisms, and the quotient by geometric inner automorphisms; the text identifies this as Theorem 16.5. https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf
- **[JV]** J. S. Milne, “Jacobian Varieties”, author version dated 12 June 2021 of the 1986 article, §9, “Obtaining coverings of a curve from its Jacobian”: Proposition 9.1, p.30, and Corollary 9.6, p.32. The Abel–Jacobi comparison and its cohomological consequence are the only facts used here. https://jmilne.org/math/xnotes/JVs.pdf
- **[NF23]** LMFDB number-field record 2.0.23.1, checked defining polynomial \(x^2-x+6\), integral basis, and class group \(C_3\). The norm and ideal-order calculations in FR14 and FR18 are given independently. https://www.lmfdb.org/NumberField/2.0.23.1
- **[Oda]** Tadao Oda, “The first de Rham cohomology group and Dieudonné modules”, Annales scientifiques de l'École Normale Supérieure, série 4, 2 (1969), pp.63–135, supplied PDF; checked Corollary 5.11 and its remark, printed p.131 / PDF page 70, and bibliography [15]. Publisher record: https://www.numdam.org/articles/10.24033/asens.1175/

Web retrieval references for the primary reader's own reopening: HT turn22view0 / turn25view0; T66 turn22view1; M turn22view2 / turn24view0; JV turn35view0 and turn34search6; NF23 turn22view3; Oda publisher record turn32search4. These retrieval identifiers are audit aids, not substitutes for the URLs and locations above.
