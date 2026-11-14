# Independent review of the F.49 candidate

Reviewer: /root/topos. Candidate: audit/F_small_geometric_extension_candidate.md, all nine sections. Outcome: **PASS in the stated sufficient-class scope**, with one optional explicitness correction below. This is not an integration instruction or a solution of F.9.

## Arithmetic descent and the weaker divisible kernel

Section2 uses normality correctly. In \(L=Fk\), every descent field contains \(D\), so \(L/F\) is Galois. For a finite \(E/k\), its coefficients and a given infinitely divisible \(a\) fit in one finite Galois \(M/D\) with \(E\subset Mk\). The two automorphisms commute on both generating fields: \(\sigma\) fixes \(k\) and preserves \(M\); \(\tau\) fixes \(M\) and preserves \(k\) because \(k/D\) is normal. Since \(\mu_\infty\subset\bar{\mathbf Q}\subset k\), the radical-ratio argument indeed makes \(\sigma(a)/a\) infinitely divisible in the finitely generated field \(M\), where it is one.

The proof only needs \(D(E^\times)\subset k^\times\), not radical closedness of \(k\). This weaker conclusion is sufficient wherever the point-function argument uses the scalar ambiguity.

Optional explicitness correction in the finitely generated case: after the proper normal model puts \(a\) in the relative algebraic closure \(k_1\) of \(k\) in \(E\), each chosen root \(z_n\in E\) of \(a\) is algebraic over \(k_1\), hence is already in \(k_1\). Thus \(a\in D(k_1^\times)\), and the finite-extension assertion applies. This is a valid immediate consequence of relative algebraic closedness, but spelling it out avoids an apparent switch from \(D(E^\times)\cap k_1^\times\) to \(D(k_1^\times)\).

## Detection and the fixed norm field

The Hilbertian core's full arithmetic detection is correct. Specializing the entire connected composite \(Y\to X\to\mathbf P^1\), rather than just its geometric component, gives a point field of degree \(d|G|\); its intermediate point on \(X\) has degree \(d\) and its residual \(G\)-torsor is connected. Arbitrarily large degrees can be obtained from rational functions on the compactification, and the cover-preserving Bertini argument already proved in F.29 transfers the finite quotient to higher dimension.

The field in Section4 is fixed before varying the radical modulus. The actual point value lies in \(Mk\); a single finite \(S_0/D\subset k\) makes \(F'=MS_0\) contain that value and all its coefficients. The displayed \(\sigma\) preserves \(F'\), and \(Mk/F'\) is Galois. For \(\tau\in\operatorname{Gal}(Mk/F')\), the commuting argument proves \(\sigma(z)/z\in F'\). Norm to \(M\) is then legitimate and gives the integer \([F':M]\lambda_i\). The fact that a profinite integer with an ordinary nonzero integral multiple is ordinary is used correctly.

The chosen nonidentity \(\sigma\) fixes \(\bar{\mathbf Q}\), so it is a nontrivial geometric automorphism of the finite-type model. This is precisely the hypothesis of F.45's moved-divisor construction. The model can be enlarged by a finite constant Galois extension without changing \(Mk\), since those constants lie in \(k\). Nothing here uses a pro-formation quotient.

## Unit and point-function comparison

I checked the changed predicates against F.45–F.46. Normality \(G_L\triangleleft G_F\), full finite arithmetic detection, actual values over all finite extensions, and the integral norm-residue conclusion are all available. The finite arithmetic span and Jannsen step are still taken over a finitely generated \(\mathbf Q\)-field. Normalization at the rational point removes the arithmetic constant Kummer class; no Tate-Hom theorem over \(k\) is substituted.

After \(\xi=\kappa(h)\), the weaker divisible-kernel inclusion supplies exactly \(c_x\in k^\times\). In the nonconstant curve case, sufficiently high-degree points have \(h(x)\notin L\), so the inverse images of \(T-1\) and \(T-b\) used in the argument are nonempty. The pole-degree identity forces \(h_1=Ah+B\) with \(A,B\in k^\times\), and the translated-zero argument handles the remaining \(k\)-valued points.

In the constant case, choosing \(\beta\notin L\) in a finite extension is enough: \(\beta/h\notin k\) because \(h\in L^\times\) and \(k\subset L\). All point values remain in \(hk\subset L\). The pulled-back unit therefore takes values in the chosen finite base field at all closed points; unbounded-degree points force it to be constant. The two scalar relations then force the point function to equal \(h\). This is stable under the finite extensions used for the two-point curve comparison. CHW4.18(5) is applied only after actual geometric point equality, as required.

## Smallness and arbitrary subfields

The decisive smallness step is correct and explicitly avoids a false hereditary assertion. Since \(B/K_0\) is finitely generated and \(k/K_0\) algebraic, \(k\cap B\) is finite over \(K_0\). Thus \(\operatorname{Gal}(L/B)\) is an **open** subgroup of the small group \(\operatorname{Gal}(k/K_0)\).

For a cover of total degree \(D_0=d|G|\), only finitely many subfields of \(L/B\) have degree at most \(D_0\). Their normal closures lie in \(L\), so their compositum \(S/B\) is finite Galois. The descended connected \(G\)-cover has constant field \(M\) with \(M\cap L=B\), hence \(Y_B\times_B S\) is connected. A full-degree Hilbert specialization makes its \(Y_B\)-point field \(E\) linearly disjoint from \(S\). The field \(E\cap L\) has degree at most \(D_0\), so lies in \(S\), and is therefore \(B\). Because \(L/B\) is Galois, this intersection equality yields linear disjointness. Both point and torsor degrees survive. Applying this to a Galois closure of an arbitrary irreducible polynomial over \(L(T)\) proves the claimed Hilbertianity.

Section7 also uses a quotient, not an arbitrary closed subgroup. Regularity of \(F/R\) identifies the \(R\)-conjugates with the \(F\)-conjugates and puts \(N\subset L\). After adjoining \(\bar{\mathbf Q}\), it gives \(N\bar{\mathbf Q}\cap B=R\bar{\mathbf Q}\). Restriction from \(\operatorname{Gal}(L/B)\) is then surjective onto \(\operatorname{Gal}(N\bar{\mathbf Q}/R\bar{\mathbf Q})\). Quotients preserve smallness. The final extension \(N\bar{\mathbf Q}/k_0\) is algebraic because both \(R/A\) and \(\bar{\mathbf Q}/\mathbf Q\) are algebraic; F.32 applies.

## Alternating polynomial example

The identities in (49.15) are correct for all \(m\ge2\). Every finite critical point has exact ramification index3 and the critical values are distinct. The finite inertia generators, including their conjugates, generate the whole geometric group: quotienting them out would leave a characteristic-zero cover of \(\mathbf P^1\) branched only at infinity, which Riemann–Hurwitz excludes. A transitive group generated by single3-cycles is \(A_n\); the stated connected-support induction proves that fact, including the two-new-vertices step.

The pairwise nonisomorphic nonabelian simple groups give all finite product quotients by Goursat, and compactness gives the infinite product. For smallness, continuity of the coset action implies that killing every sufficiently large coordinate factor kills their whole product: the finite-support subgroup of that tail is dense. This is implicit in the written argument and may be made explicit.

The alternate-model strictness argument is valid. The finite compositum with \(\mathbf Q(t)\) gives an open subgroup of any proposed geometric normal-closure group, surjecting onto an open subgroup of the displayed product. Every further open subgroup still has unbounded alternating quotients, contrary to a proper hereditary formation.

The separate, simpler universal-tripod example is proved in audit/F_small_geometric_tripod_example.md. Either example proves strictness; no claim of priority or necessity is made.
