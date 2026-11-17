# Finite-field research memo: cote 15, scans 003–014

## Scope and evidential status

Research began only after the transcription was frozen. This memo uses the frozen page files, the supplied context, and independently checked published sources; it neither inspects manuscript images nor proposes changes to the transcript. README and the complete notes/RESULTS_STATE.md were read first. Earlier research returns are treated as first-pass leads, including their assertions labelled “Proved”; none is promoted to a reviewed result here.

Every witness filename below is inside MPL_12_150-168+15_002-033/pages/. Every note body is one to four sentences, independently usable with its metadata. Mathematical reconstructions of ambiguous domains, coefficient fields, or categories are reading questions, not alternative transcriptions.

For the mathematical calculations, “the intended rigid Weil group” means
\[
W(p)=\{\alpha\in\overline{\mathbb Q}^{\,*}:\ 
|\sigma\alpha|=p^{w/2}\text{ for every }\sigma,\ w\in\mathbb Z,\ 
p^N\alpha\text{ is integral for some }N\ge0\}.
\]
This is an explicitly declared comparison model, not a replacement for the algebraic-integer/positive-weight wording of scan 005. Write \(\mu_\infty\) for the roots of unity and \(W_0(p)=\ker(w)\).

## Suggested notes

### FF01 — The finite-field identification retains a conjectural input

**Kind:** scope of a conditional assertion; later-result comparison.  
**Witness:** MPL_12_150-168+15_002-033_15_scan003.tex, scan 003; compare scan 013.  
**Brief frozen quote:** “en vertu des conj. de Tate et de Tate-Honda”.  
**Context search and relation:** Tate | semi-simple | conjecture → context/MPL_16+47+54+44_transcription.tex, cote 16/049, and context/same_cote_15/MPL_15_087-138_notes.md, FR08 at 15/100: **adds** a finite-field character-group description to the semisimple-motive programme, while **restating** its need for realization input.  
**RESULTS_STATE:** WG2 §2.4 #3 and WG2 §2.3 #7, both unchecked questions/plans; MPL_15_087-138 §125, first-pass lead. No status change.  
**Confidence:** high; the manuscript names the conjectures, and the primary sources distinguish their scopes.

The classification of simple abelian varieties up to isogeny by weight-one Weil numbers is the Honda–Tate theorem, not by itself a classification of the tensor category of all motives (Honda, 1968, Main Theorem, p. 83; Tate, 1971, Theorem 1, p. 96). In Milne’s later treatment, §2 explicitly assumes the pole-order form of the Tate conjecture, Conjecture 1.14, before identifying the all-motives category and its Frobenius centralizers (Milne, 1994/2019, pp. 10–11). Thus the new sheet supplies a conditional description of the category, its band, and realizations; the abelian-variety theorem does not remove every hypothesis in that description.

### FF02 — Why the crystalline realization uses the discrete group \(\mathbb Z\)

**Kind:** unpursued implication; independent elementary check.  
**Witness:** MPL_12_150-168+15_002-033_15_scan003.tex, scan 003, opening paragraph.  
**Brief frozen quote:** “ici on ne peut remplacer \(\mathbf Z\) par \(\widehat{\mathbf Z}\) !”.  
**Context search and relation:** cristalline | Dieudonné | Frobenius → context/MPL_16+47+54+44_transcription.tex, cote 54/005–007; context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, A16 at 15/211: **adds** a rational Frobenius-representation distinction to the integral \(F,V\) questions, rather than identifying the two settings.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high; compactness gives an explicit obstruction.

Over \(\mathbb F_p\), \(W(\mathbb F_p)[1/p]=\mathbb Q_p\) and Witt Frobenius on the coefficients is the identity, so an isocrystal is a finite-dimensional \(\mathbb Q_p\)-space with an invertible linear operator; over a general perfect field the operator is semilinear (Milne, 1994/2019, §1, p. 11). The one-dimensional operator \(F=p\) defines a representation of the discrete group \(\mathbb Z\), but cannot be the value at \(1\) of a continuous representation of compact \(\widehat{\mathbb Z}\), since its powers have unbounded \(p\)-adic valuations. This verifies the warning and also explains why the phrase “sur \(Q_p\)” belongs specifically to the prime-field case.

### FF03 — The literal effective set is a monoid, not a subgroup

**Kind:** reading question; explicit counterexample to the literal group assertion.  
**Witness:** MPL_12_150-168+15_002-033_15_scan005.tex, scan 005.  
**Brief frozen quote:** “le sous groupe”; “entiers algébriques”; \(\nu\in\mathbf Z^+\).  
**Context search and relation:** rigidité | entier | sous groupe | FR02 | FR08b → context/same_cote_15/MPL_15_087-138_notes.md, FR02 at 15/090 and FR08b at 15/100: **restates** the dual-closure issue and **adds** an immediate test for this exact definition; compare context/MPL_16+47+54+44_transcription.tex, 16/049.  
**RESULTS_STATE:** WG2 §2.4 #3 and §2.3 #7, unchecked plans.  
**Confidence:** high; \(p\) and \(p^{-1}\) settle the literal claim.

The displayed conditions include \(p\), whereas its inverse \(p^{-1}\) is not an algebraic integer and has negative weight, so the displayed set is not a subgroup. Passing to its group completion, equivalently allowing a power of \(p\) to clear denominators and allowing all integral weights, gives the comparison group \(W(p)\) declared above. This is the expected distinction between effective objects and the rigid category with Tate inverses, but it remains a reading/category question because the frozen text itself says “sous groupe”.

### FF04 — The roots-of-unity quotient is a protorus construction

**Kind:** structural clarification and finite-type qualification.  
**Witness:** MPL_12_150-168+15_002-033_15_scan005.tex and MPL_12_150-168+15_002-033_15_scan013.tex, scans 005 and 013.  
**Brief frozen quote:** \(G^0=D(\Gamma/\text{racines de }1)\); \(D(\text{racines de }1)\).  
**Context search and relation:** protorus | torsion | racines | type fini → context/same_cote_15/MPL_15_087-138_notes.md, FR10 at 15/102 and FR11 at 15/104; context/MPL_16+47+54+44_transcription.tex, 16/021: **adds** the full component sequence to the finite root and Tate inverse-limit comparisons.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high, conditional on the rigid group interpretation FF03; finite-type terminology is not inferred from the handwriting.

Cartier duality sends \(\mu_\infty\), with its cyclotomic Galois action, to the proconstant group \(\widehat{\mathbb Z}\), giving \(1\to D(W(p)/\mu_\infty)\to D(W(p))\to\widehat{\mathbb Z}\to1\). Torsion-free characters yield a connected group of multiplicative type, hence a protorus; a torus of finite type additionally requires a finitely generated character lattice. Here the whole band cannot be finite type, since its character group contains roots of unity of arbitrarily large order, while the weight-zero part contains \(u=(1+\sqrt{1-p^4})/p^2\) and all its root classes: this \(p\)-unit is not torsion because its trace \(2/p^2\) is not integral. Finite-rank Galois-stable lattices therefore describe torus quotients, not the whole object without qualification.

### FF05 — The weight and Tate maps give the square relation exactly

**Kind:** unpursued implication; convention check.  
**Witness:** MPL_12_150-168+15_002-033_15_scan007.tex, MPL_12_150-168+15_002-033_15_scan013.tex, and MPL_12_150-168+15_002-033_15_scan014.tex, scans 007, 013, 014.  
**Brief frozen quote:** \(\epsilon i(\lambda)=\lambda^2\); \(i^*\epsilon^*=2\operatorname{Id}\).  
**Context search and relation:** epsilon | poids | FR22 → context/same_cote_15/MPL_15_087-138_notes.md, FR01 at 15/088–090 and FR22 at 15/090,100,102; context/MPL_16+47+54+44_transcription.tex, 16/021: **restates** the weight-two normalization and **adds** the explicit dual diagram.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_195-228+18_002-017 B04, first-pass lead only.  
**Confidence:** high; direct character–cocharacter pairing.

Since \(\epsilon^*(1)=p\) and the displayed weight of \(p\) is two, duality gives \(i^*\epsilon^*(1)=2\), hence \(\epsilon\circ i=[2]\). Thus \(i\) is not a section of \(\epsilon\); its restriction to \(\mu_2\) is instead what supplies the component splitting of the kernel. This is the positive-weight-two convention of the Lefschetz object; comparison with a notation \(Q(1)\) using negative cohomological weight must explicitly track dualization and Frobenius inversion.

### FF06 — The \(\mu_2\) factor is correct, but the written section has the wrong target if read literally

**Kind:** reading question with explicit character calculation.  
**Witness:** MPL_12_150-168+15_002-033_15_scan005.tex, scan 005; compare scans 013–014.  
**Brief frozen quote:** \(i|\mu_2:\mu_2\longrightarrow H^0\); \(H\simeq H^0\times\mu_2\).  
**Context search and relation:** splitting | mu_2 | T05 → context/same_cote_15/MPL_15_087-138_notes.md, T05 at 15/117–119: **adds** a different kernel/section type check to the later projection-versus-square discrepancy.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high for the mathematical type check; no new ink judgment is asserted.

In the rigid Weil group, \(\alpha\mapsto(\alpha p^{-w(\alpha)/2},w(\alpha))\) identifies \(W(p)/\mu_\infty\) with \(W_0(p)/\mu_\infty\oplus\mathbb Z\), because the ambiguity in \(\sqrt p\) is torsion. Quotienting by the character \(p\) therefore leaves \(W_0(p)/\mu_\infty\oplus\mathbb Z/2\), giving \(H\simeq H^0\times\mu_2\) with the nonzero torsion character represented by \(\sqrt p\). The element \(i(-1)\) evaluates to \(-1\) on that character, so the section \(\mu_2\to H\) has nontrivial image in \(H/H^0\) and cannot factor through \(H^0\). The literal target \(H^0\) is retained as a reading question.

### FF07 — The rational Frobenius is evaluation on the eigenvalue group

**Kind:** unpursued implication; exact construction.  
**Witness:** MPL_12_150-168+15_002-033_15_scan013.tex, scan 013.  
**Brief frozen quote:** “canonique, défini par \(\Gamma\subset\overline Q^*\)”.  
**Context search and relation:** Frobenius | engendré | FR01 → context/same_cote_15/MPL_15_087-138_notes.md, FR01 at 15/088–090: **restates** its evaluation construction in the reverse direction, with the new page explicitly designating the rational point.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high; Galois equivariance and injectivity are explicit.

A rational point of \(D(\Gamma)\) is a Galois-equivariant homomorphism \(\Gamma\to\overline{\mathbb Q}^{\,*}\), so the actual inclusion defines the stated rational Frobenius. Evaluation at this point is injective on characters; consequently no nontrivial character is trivial on all its powers, and those powers are Zariski dense in the diagonalizable group, interpreted through every finite quotient. This explains the precise connection between the eigenvalue group and the Zariski-generating Frobenius discussed on 15/088–090, without inferring rational neutralization of the gerbe.

### FF08 — “red” cannot simply discard Jordan blocks by reducedness

**Kind:** reading question; explicit representation counterexample.  
**Witness:** MPL_12_150-168+15_002-033_15_scan013.tex, scan 013, algebraic-envelope diagram.  
**Brief frozen quote:** “enveloppe algébrique de \(\mathbf Z\)”; \(D(\overline Q_p^*)\).  
**Context search and relation:** unipotent | isocrystal | réductif | red → no matching semisimplification statement in the supplied context; nearest realization questions are context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, A16 at 15/211 and context/MPL_16+47+54+44_transcription.tex, 54/007: **adds** a distinction those passages do not make.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan.  
**Confidence:** high; the Jordan block is a complete test.

The invertible operator \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\) is an isocrystal over \(\mathbb F_p\), hence an object of the full representation category of \(\mathbb Z\), but it is not a representation of a group of multiplicative type in characteristic zero. The displayed \(D(\overline Q_p^*)\) therefore describes the semisimple representation part, so the subscript “red” requires a reductive-quotient or semisimplification reading, not merely the reduced scheme underlying the full envelope. The geometric realization can land in this part under the stipulated semisimplicity hypotheses; that does not make every \(\mathbb F_p\)-isocrystal semisimple.

### FF09 — The Artin–Tate quotient and the topology of its first cohomology

**Kind:** unpursued implication with a topological qualification.  
**Witness:** MPL_12_150-168+15_002-033_15_scan009.tex, scan 009; compare 014.  
**Brief frozen quote:** “extension qui splitte”; \(H^1(Q_p,G/H)\xrightarrow{\sim}H^1(Q_p,\widehat{\mathbf Z})\).  
**Context search and relation:** Artin | proconstant | Hilbert | splitting → context/same_cote_15/MPL_15_087-138_notes.md, T21 at 15/137 and the Artin construction T28 at 15/135–137; context/MPL_16+47+54+44_transcription.tex, 16/021: **adds** a specified finite-field quotient to the later general Artin–Tate construction.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high; direct duality and Hilbert 90.

The characters trivial on \(H=\ker(\epsilon|G^0)\) are precisely \(\mu_\infty\cdot p^{\mathbb Z}\), a direct product, so duality supplies \(G/H\simeq\widehat{\mathbb Z}\times G_m\). Hilbert 90 then removes the \(G_m\) factor from \(H^1\). The remaining group must use continuous homomorphisms to the profinite topology on \(\widehat{\mathbb Z}\), or the corresponding proconstant torsor formalism: if \(\widehat{\mathbb Z}\) were treated as a discrete torsion-free module, continuous homomorphisms from the profinite absolute Galois group would all vanish.

### FF10 — A nonzero \(H\)-gerbe class is compatible with a \(Q_p\)-valued fibre functor

**Kind:** unpursued implication; gerbe/torsor distinction.  
**Witness:** MPL_12_150-168+15_002-033_15_scan007.tex and MPL_12_150-168+15_002-033_15_scan009.tex, scans 007–009.  
**Brief frozen quote:** \(\xi_p=\partial(\eta_p)\); “du general nonsense” with the frozen uncertainty on its opening words.  
**Context search and relation:** gerbe | torseur | A13 → context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, A13 at 15/207–209, and context/MPL_16+47+54+44_transcription.tex, 54/003: **adds** an explicit boundary-class calculation and **differs** from the latter’s universal vector-extension torsor.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high; the lifting-gerbe construction identifies the boundary.

The \(H\)-gerbe records fibre functors equipped with the prescribed restriction \(F_0\), and its obstruction is the boundary of the \(G/H\)-torsor comparing that restriction with \(T_p\); this is the lifting-gerbe statement formalized in Milne (2003, Lemma 4.4, pp. 29–30). Exactness sends \(\partial(\eta_p)\) to zero in \(H^2(\mathbb Q_p,G)\), so a nonzero \(H\)-class does not contradict the already given \(Q_p\)-valued fibre functor \(T_p\). The bare \(H^2\)-class describes the banded gerbe up to equivalence, whereas the chosen local splittings are additional data, already acknowledged by the relative-cohomology notation on scan 007.

### FF11 — A finite étale test identifies the unramified torsor

**Kind:** own calculation; Frobenius-convention qualification.  
**Witness:** MPL_12_150-168+15_002-033_15_scan009.tex, scan 009.  
**Brief frozen quote:** “l'isom \(\operatorname{Gal}(\widetilde Q_p/Q_p)\simeq\widehat{\mathbf Z}\) donné par Frobenius”.  
**Context search and relation:** Frobenius | cyclotomique | arithmetic | geometric → context/same_cote_15/MPL_15_087-138_notes.md, FR22 at 15/090,100,102; context/MPL_16+47+54+44_transcription.tex, 16/021: **adds** the unramified Artin fibre torsor and **restates** the need to specify Frobenius orientation.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high for the finite étale algebra test; the sign depends on the order of the isomorphism torsor and the Frobenius convention.

For \(X=\operatorname{Spec}\mathbb F_{p^n}\), the canonical Artin fibre is the split algebra \(\mathbb Q_p^n\), whereas degree-zero crystalline cohomology is the unramified degree-\(n\) field \(W(\mathbb F_{p^n})[1/p]\). Their tensor-isomorphism torsor therefore detects the unramified cyclic quotient of \(\operatorname{Gal}(\overline{\mathbb Q}_p/\mathbb Q_p)\), and the compatible family over \(n\) gives the written profinite character. Specifying whether Frobenius means \(x\mapsto x^p\) or its inverse, and whether the isomorphisms run from \(F_0\) to \(T_p\) or conversely, is necessary to fix its sign.

### FF12 — Compactness verifies the real finite-torus term, not global uniqueness by itself

**Kind:** own cohomology calculation; scope limit.  
**Witness:** MPL_12_150-168+15_002-033_15_scan011.tex, scan 011, opening paragraph; compare scan 014.  
**Brief frozen quote:** “la composante à l'infini est de tte façon nulle”.  
**Context search and relation:** compact | cohomologie | T04 → context/same_cote_15/MPL_15_087-138_notes.md, T04 at 15/117–119: **restates** the same real norm calculation, but **adds** its use in a global determination argument.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high; the finite cyclic calculation and the finite-group Mittag–Leffler argument cover the real protorus term.

For \(S=\operatorname{Res}_{\mathbb C/\mathbb R}^{1}G_m\), complex conjugation acts on \(S(\mathbb C)=\mathbb C^*\) as \(z\mapsto1/\bar z\), and the cyclic norm \(z/\bar z\) surjects onto \(S^1\), giving \(H^2(\mathbb R,S)=0\). Products prove the same assertion for every compact real torus of finite type. For a countable inverse system of such tori, the groups \(H^1(\mathbb R,S^d)=(\mathbb Z/2)^d\) are finite and hence satisfy Mittag–Leffler, so the \(\varprojlim{}^1H^1\) term vanishes and Milne’s protorus cohomology sequence extends this real vanishing (2003, Proposition 2.8). This still does not prove injectivity of the global-to-local map.

### FF13 — Real non-neutrality has an explicit obstruction over \(\mathbb F_p\) itself

**Kind:** own verification using a primary theorem.  
**Witness:** MPL_12_150-168+15_002-033_15_scan011.tex, scan 011.  
**Brief frozen quote:** “n'a pas de foncteur fibre sur \(R\)”.  
**Context search and relation:** non neutre | quaternion | foncteur fibre | T06 → context/same_cote_15/MPL_15_087-138_notes.md, T01 at 15/117 and T06 at 15/119; context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, A12 at 15/207: **adds** a concrete finite abelian subcategory witnessing the obstruction left unspecified in A12.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124 and MPL_15_195-228+18_002-017 B03, first-pass leads.  
**Confidence:** high; the division-algebra dimensions give a contradiction.

Honda–Tate gives a simple abelian surface over \(\mathbb F_p\) with Frobenius \(\sqrt p\), whose endomorphism algebra becomes \(\mathbb H\times\mathbb H\) over \(\mathbb R\), where \(\mathbb H\) is Hamilton’s quaternion division algebra (Tate, 1971, p. 97, example (a), odd exponent case). A real fibre functor would realize its degree-one motive on a four-dimensional real space, with both central components of that algebra acting nontrivially; equivalently, preservation of the characteristic polynomial \((T^2-p)^2\) forces both real embeddings of \(\mathbb Q(\sqrt p)\) to occur. Each nonzero \(\mathbb H\)-module has real dimension at least four, so the two summands would require dimension at least eight. This supplies an obstruction over the exact ground field of the sheet, without silently replacing \(\mathbb F_p\) by \(\mathbb F_{p^2}\).

### FF14 — The \(\mu_2\) component is the quaternion Brauer class ramified at \(p\) and infinity

**Kind:** unpursued implication; exact local-invariant computation.  
**Witness:** MPL_12_150-168+15_002-033_15_scan009.tex and MPL_12_150-168+15_002-033_15_scan011.tex, scans 009 and 011.  
**Brief frozen quote:** \(\sum\operatorname{inv}_p=0\); “l'unique élément non nul”.  
**Context search and relation:** invariant | Brauer | réciprocité → context/MPL_16+47+54+44_transcription.tex, 16/021, and context/same_cote_15/MPL_15_087-138_notes.md, T04 at 15/117–119: **adds** a global Brauer calculation; the older Brauer group concerns a variety, not this coefficient-field gerbe.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high, after accepting the stated non-neutral real class and finite-place splittings.

Kummer theory identifies \(H^2(\mathbb Q,\mu_2)\) with \(\operatorname{Br}(\mathbb Q)[2]\), and the local invariants of the displayed component are \(0\) at finite \(\ell\ne p\) and \(1/2\) at infinity. The global Brauer exact sequence therefore forces invariant \(1/2\) at \(p\), uniquely specifying the quaternion class ramified exactly at \(\{p,\infty\}\) (Milne, 2020, VIII, Theorem 4.2 and Example 4.4(b), p. 241). This determines the \(\mu_2\) component only; the \(H^0\) component needs the additional local-global argument FF22.

### FF15 — The \(p\)-adic endomorphism ring is a Frobenius centralizer

**Kind:** reading question; explicit algebraic dimension test.  
**Witness:** MPL_12_150-168+15_002-033_15_scan013.tex, scan 013.  
**Brief frozen quote:** \(A\otimes_QQ_p\simeq\operatorname{End}(T_p(M))\).  
**Context search and relation:** End | Tate-Honda | B01 → context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, B01 at 15/213,215,227, and context/same_cote_15/MPL_15_087-138_notes.md, FR21 at 15/088–090: **restates** the importance of the precise Hom target and **adds** its crystalline version.  
**RESULTS_STATE:** MPL_15_195-228+18_002-017 B01, first-pass lead; WG2 §2.4 #3, unchecked plan.  
**Confidence:** high; the target category is essential to the cited theorem.

For an abelian variety the right-hand side must mean endomorphisms in the rational Dieudonné/isocrystal category, hence commuting with Frobenius, rather than every linear map on the underlying vector space (Tate, 1971, §2, pp. 98–99). For example, the Weil polynomial \(T^2-T+2\) gives a simple elliptic isogeny class over \(\mathbb F_2\) with endomorphism algebra \(\mathbb Q(\sqrt{-7})\), so its scalar extension has dimension two over \(\mathbb Q_2\), whereas all linear endomorphisms of its two-dimensional crystalline realization have dimension four. This explicitly contradicts the unrestricted linear-End reading, while agreeing with the Frobenius-centralizer reading; Tate’s 1966 Main Theorem likewise has Galois-equivariant Hom as its target.

### FF16 — Splitting is over the local centre, with a specific \(p\)-adic invariant

**Kind:** later theorem comparison; exact hypothesis and normalization.  
**Witness:** MPL_12_150-168+15_002-033_15_scan013.tex, scan 013, final block.  
**Brief frozen quote:** “centre ... engendré par”; “splitte sur \(Q_\ell\)”.  
**Context search and relation:** centre | endomorphism | splitte | invariant → context/MPL_16+47+54+44_transcription.tex, 16/049, and context/same_cote_15/MPL_15_087-138_notes.md, FR08 at 15/100: **adds** the endomorphism-algebra arithmetic to the semisimplicity and eigenvalue programme.  
**RESULTS_STATE:** WG2 §2.3 #7 and §2.4 #3, unchecked plans; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high for the abelian theorem; the all-motives extension retains FF01’s hypotheses.

For simple \(A/\mathbb F_q\), put \(F=\mathbb Q(\pi_A)\) and \(D=\operatorname{End}^0(A)\); the precise theorem says that \(D\) is central division over \(F\), splits at every finite \(v\nmid p\), has invariant \(1/2\) at real \(v\), and has \(\operatorname{inv}_v(D)=\frac{\operatorname{ord}_v(\pi_A)}{\operatorname{ord}_v(q)}[F_v:\mathbb Q_p]\pmod{\mathbb Z}\) for \(v\mid p\) (Tate, 1971, Theorem 1(ii), p. 96). Thus \(D\otimes_{\mathbb Q}\mathbb Q_\ell\) is a product of matrix algebras over the completions \(F_v\), not necessarily a matrix algebra over \(\mathbb Q_\ell\) itself. The inserted simplicity assumption and the incomplete line about invariants should therefore be retained when comparing the sheet with this theorem. For a contravariant degree-one motive the algebra is the opposite of \(D\), which negates its invariants; correspondingly, Milne’s motivic formula has the minus sign (1994/2019, Theorem 2.16, p. 18), so this variance convention must be fixed before transferring the formula to \(A_M\).

### FF17 — A weight-zero valuation gives a genuine denominator obstruction

**Kind:** reading question; own explicit counterexample.  
**Witness:** MPL_12_150-168+15_002-033_15_scan014.tex, scan 014; compare scan 013’s rational valuation target.  
**Brief frozen quote:** “valuation ... normalisée par \(v_p(p)=1\)”; \(M\to\unsure{\mathbf Z|\mathbf Z^+}\).  
**Context search and relation:** valuation | entière | denominator | T10 | T11 → context/same_cote_15/MPL_15_087-138_notes.md, T10–T11 at 15/121 and CM02 at 15/100,110: **restates** its explicit integrality warning and **adds** an example of weight zero, rather than only \(\sqrt{-3}\) of nonzero weight.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high; exact Gaussian-integer factorization.

Take \(p=5\), \(u=(3+4i)/5=(2+i)/(2-i)\), and \(\beta^n=u\) for \(n>1\). Every complex conjugate of \(\beta\) has absolute value one, it is a unit away from \(5\), and at a prime above \(2+i\) the normalization \(v_5(5)=1\) gives \(v_5(\beta)=1/n\). Thus the written integral target cannot describe normalized valuation on the whole intended weight-zero character group; scan 013’s target \(\mathbb Q\) has the correct type for this example. The finite-lattice or ramification rescaling needed for a genuine cocharacter is additional data, not a reason to replace the frozen target.

### FF18 — The idelic diagram requires finite torus lattices before taking limits

**Kind:** reading question; own type check.  
**Witness:** MPL_12_150-168+15_002-033_15_scan014.tex, scan 014, opening diagram.  
**Brief frozen quote:** \(H^2(\mathbf Q,H)=\varinjlim H^2(G,K^*\otimes\check M)\).  
**Context search and relation:** cocharacter | lattice | CM02b | limite | idèle → context/same_cote_15/MPL_15_087-138_notes.md, CM02b at 15/110–114 and T10 at 15/121; context/MPL_16+47+54+44_transcription.tex, 16/021: **differs** from those finite-lattice and Tate-module limits and **adds** a necessary scope check for the whole protorus.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124 and §125, first-pass leads.  
**Confidence:** high for the type obstruction; the diagram’s unstated finite-level quantifiers remain a reading question.

Root extraction makes \(W_0(p)/\mu_\infty\) uniquely divisible: choices of an \(n\)-th root differ only by roots of unity. Consequently its integral dual \(\operatorname{Hom}(W_0(p)/\mu_\infty,\mathbb Z)\) is zero, so the expression \(K^*\otimes\check M\) cannot encode the whole nontrivial protorus if \(\check M\) means that full integral dual. Likewise an integral cocharacter lattice does not encode the \(\mu_2\) component. The displayed idelic/Tate-cohomology calculation therefore needs finite-rank torus quotients and a separately justified inverse-limit passage; it cannot be applied unchanged to the whole \(H\).

### FF19 — Oda proves a degree-one, \(p\)-torsion comparison

**Kind:** primary-source scope check.  
**Witness:** MPL_12_150-168+15_002-033_15_scan003.tex and MPL_12_150-168+15_002-033_15_scan013.tex, scans 003, 013.  
**Brief frozen quote:** “cohomologie cristalline”; “\(F\)-cristaux”.  
**Context search and relation:** Oda | p-torsion | Corollary | D05 → context/MPL_16+47+54+44_transcription.tex, 54/003,005,007; context/MPL_16+47+54+44_notes.md, D05; context/same_cote_15/MPL_15_087-138_notes.md, FR23 at 15/106,110–112; context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, P04 at 18/005: **restates** the independently verified comparison and **differs** from the all-motives rational realization proposed here.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §125, first-pass lead.  
**Confidence:** high; supplied PDF text and published page image checked, printed p. 131, PDF page 70.

Oda’s Corollary 5.11 identifies the Dieudonné module of \(A[p]\) with \(H^1_{\mathrm{dR}}(A)\) for an abelian variety over a perfect field of characteristic \(p\), compatibly with the specified submodule and the Hodge exact sequence (Oda, 1969, p. 131). It directly addresses the \(p\)-kernel/extension question in context 54/007. It does not alone construct the rational crystalline fibre functor on all motives, identify its essential image, or prove the \(p\)-adic fullness assertion on scan 013; integral \(p\)-torsion, rational isocrystals, and arbitrary cohomological degree must remain distinct.

### FF20 — The odd character extends over \(\mathbb R\), not over \(\mathbb Q\)

**Kind:** reading question; independent coefficient-field test.  
**Witness:** MPL_12_150-168+15_002-033_15_scan011.tex, scan 011.  
**Brief frozen quote:** “de degré \(1\), rang \(1\) (qui se prolonge à \(G\))”.  
**Context search and relation:** caractère | degré | rang | Frobenius → context/same_cote_15/MPL_15_087-138_notes.md, FR01 at 15/088–090 and T01–T03 at 15/117: **adds** the coefficient-field qualification to the odd-line argument and **restates** the need for its motivic structure.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high; rational Weil numbers give an exact obstruction.

The class of \(\sqrt p\) in \(W(p)/\mu_\infty\) is Galois invariant and defines a rational character of \(G^0\) of weight one. It extends to \(G_{\mathbb R}\) through the real representative \(\sqrt p\), but a rational character of \(G\) would require a rational Weil number; such a number is \(\pm p^n\) and has even weight. Thus the parenthetical extension is consistent in the surrounding real-neutrality argument after scalar extension to \(\mathbb R\), whereas an unqualified extension over \(\mathbb Q\) would be false.

### FF21 — Fixing the Artin fibre and fixing its Tate extension give different bands

**Kind:** reading question; exact kernel comparison.  
**Witness:** MPL_12_150-168+15_002-033_15_scan003.tex, scan 003; compare 007.  
**Brief frozen quote:** \(F^0(Q(1))=Q\); \(H=\operatorname{Ker}(G^0\to G_m)\).  
**Context search and relation:** Niv | Artin–Tate | effective weight-zero | F_0 → context/same_cote_15/MPL_15_087-138_notes.md, T01 at 15/117 and T18–T21 at 15/135–137: **adds** an earlier domain/framing issue and **restates** the later separation of finite-image and Tate subcategories.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead.  
**Confidence:** high for the kernel comparison; the intended extension of \(F^0\)’s domain remains interpretative.

Prescribing the canonical fibre functor on Artin motives alone reduces the band from \(G\) to \(G^0\); also prescribing the Tate fibre and its identification reduces it further to \(\ker(\epsilon|G^0)=H\). Thus the formula \(F^0(Q(1))=Q\) must extend the preceding weight-zero domain or add a Tate framing for the displayed \(H\)-gerbe to follow. The same distinction explains why the full comparison torsor has group \(G/H\), while its restriction to the Artin subcategory has only the quotient \(\widehat{\mathbb Z}\).

### FF22 — Later protorus cohomology can justify the intended local-global conclusion

**Kind:** later-result comparison; hypothesis-sensitive verification, not a claim that the page contains the proof.  
**Witness:** MPL_12_150-168+15_002-033_15_scan009.tex, MPL_12_150-168+15_002-033_15_scan011.tex, and MPL_12_150-168+15_002-033_15_scan014.tex, scans 009, 011, 014.  
**Brief frozen quote:** “connues quand on connaît leurs composantes en ttes places”; “Donc ici on ... connaît \(\xi\)”.  
**Context search and relation:** local-global | lim¹ | protorus | Hasse principle | idèle → no matching global protorus proof in the supplied context; context/same_cote_15/MPL_15_087-138_notes.md, T04 at 15/117–119, supplies only the compact real finite-torus computation: the new pages **add** a global determination claim.  
**RESULTS_STATE:** WG2 §2.4 #3, unchecked plan; MPL_15_087-138 §124, first-pass lead. These entries are not upgraded by this comparison.  
**Confidence:** high for the cited cohomology statements; application to the manuscript depends on the declared rigid Weil-group model and the distinction FF18.

For a strict countable inverse system of tori, Milne’s Proposition 2.8 includes a \(\varprojlim{}^1H^1\) term in \(H^2\); his Propositions 3.5(b), 3.10 and 4.3 prove the requisite local-global uniqueness for the specific Weil-number protorus (Milne, 2003, pp. 17, 24–25, 29). The intended character group \(W(p)/\mu_\infty\) identifies with the Weil-number germ group by \(\alpha\mapsto[(\alpha,1)]\): the kernel consists of roots of unity, and a representative over \(\mathbb F_{p^n}\) lifts by taking an \(n\)-th root. Its weight-zero part is a direct factor, so this gives the appropriate later route to the \(H^0\) uniqueness used on scans 009–011. The conclusion is therefore defensible for that identified band, but it is not a consequence of compactness alone and the missing inverse-limit justification must not be silently supplied as manuscript text.

## Bibliography and exact checked locators

**Honda, T. (1968).** Isogeny classes of abelian varieties over finite fields. *Journal of the Mathematical Society of Japan, 20*(1–2), 83–95. https://doi.org/10.2969/jmsj/02010083  
Checked primary PDF: https://www.jstage.jst.go.jp/article/jmath1948/20/1-2/20_1-2_83/_pdf/-char/en  
Main Theorem, p. 83; definition of type \((A_0)\), p. 83; §1, Proposition 4 and Theorem 1, pp. 85–86. The first publisher PDF route timed out; the publisher’s actual download link succeeded.

**Tate, J. (1966).** Endomorphisms of abelian varieties over finite fields. *Inventiones Mathematicae, 2*, 134–144.  
Checked primary PDF: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf  
§1, map (1) and Main Theorem, p. 134; rational map (2), Lemmas 1 and 3, p. 135; centralizer Lemma 4, p. 136. This paper’s displayed Tate module uses \(\ell\ne\operatorname{char}k\).

**Tate, J. (1971).** Classes d’isogénie des variétés abéliennes sur un corps fini (d’après T. Honda). *Séminaire Bourbaki, 1968/69*, Exposé 352, 95–110.  
Checked primary PDF: https://www.numdam.org/article/SB_1968-1969__11__95_0.pdf  
The talk is dated November 1968; Numdam records publication in 1971. Theorem 1(i–ii), p. 96; real Weil-number examples, p. 97; §2, the Tate/Dieudonné fully faithful realization, pp. 98–99. The local formula on p. 96 was checked visually, not inferred from damaged formula extraction.

**Oda, T. (1969).** The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l’École Normale Supérieure, Fourth Series, 2*(1), 63–135. https://doi.org/10.24033/asens.1175  
Supplied source: context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf.  
Published counterpart checked: https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf  
Corollary 5.11 and following remark, printed p. 131 / PDF page 70; compare Corollary 5.12 on the same page for the weaker general smooth-proper statement. The module in 5.11 is that of the \(p\)-torsion group scheme, not the full rational isocrystal.

**Milne, J. S. (1994/2019).** Motives over finite fields. In U. Jannsen, S. Kleiman, & J.-P. Serre (Eds.), *Motives* (Proceedings of Symposia in Pure Mathematics, Vol. 55, Part 1, pp. 401–459). American Mathematical Society. Author’s corrected manuscript, November 2, 2019.  
Checked PDF: https://jmilne.org/math/xnotes/Seattle1.pdf  
Version record: https://jmilne.org/math/xnotes/Seattle1.html  
Locators use the corrected manuscript’s own printed pagination: Conjecture 1.14 and Proposition 1.15, p. 10; isocrystal definition and Proposition 1.17, p. 11; §2 standing assumption, p. 11; Proposition 2.4 and Definition 2.5, p. 13; Proposition 2.6, pp. 13–14; Proposition 2.10, pp. 15–16; Theorem 2.16, p. 18 (negative valuation sign checked visually); Proposition 2.22, p. 21; Remark 2.29, p. 24; Proposition 2.42, p. 27. The HTML record confirms that the corrected manuscript retains the original numbering.

**Milne, J. S. (2003).** *Gerbes and abelian motives* (Version 1.1, February 21, 2003).  
Checked primary PDF: https://www.jmilne.org/math/articles/2003b.pdf  
Proposition 2.8, p. 17; Remark 2.17, p. 20; Weil-number protorus, §3, p. 23; Proposition 3.5, p. 24; Lemmas 3.7–3.9 and Proposition 3.10, p. 25; Proposition 4.3 and Lemma 4.4, pp. 29–30; Theorem 6.3, pp. 36–37. The introduction, p. 3, explicitly identifies the inverse-limit cohomology issue in earlier literature.

**Primary-source definition caveat:** On p. 23 of this 2003 version the displayed definition of Weil numbers visibly omits the \(p\)-integrality condition. At \(p=2\), \((3+4i)/5\) satisfies its printed archimedean condition but has nonzero valuations at \(5\), so it would defeat the subsequent \(p\)-adic divisor description. The comparison in FF22 uses the explicit \(p\)-integral definition in Milne’s corrected 1994 manuscript, Definition 2.5, and does not silently treat the abbreviated 2003 definition as sufficient.

**Milne, J. S. (2020).** *Class field theory* (Version 4.03).  
Checked author PDF: https://www.jmilne.org/math/CourseNotes/CFT.pdf  
Chapter IV, §4, real and local Brauer groups, pp. 139–141; Chapter VIII, Theorem 4.2 and Example 4.4(b), p. 241, for the global Brauer exact sequence and the quaternion ramification description.

## Research handoff priorities

The most consequential literal-formula/domain questions are FF03 (monoid versus group), FF06 (the section’s target), FF15 (the End category), FF17 (integral versus rational valuation), FF18 (finite lattice versus whole protorus), FF20 (the coefficient field of a character extension), and FF21 (Artin versus Artin–Tate framing). FF13 gives an independently checkable real obstruction; FF14 computes the precise \(\mu_2\) class; FF22 prevents the opposite error of declaring the intended local-global conclusion false merely because its proof is abbreviated. No remark here changes the frozen readings, deletes cancellations, upgrades a register entry, or supplies a proof to an unfinished manuscript sentence.
