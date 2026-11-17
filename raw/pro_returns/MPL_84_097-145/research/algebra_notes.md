# Algebra research notes: cote 84, scans 097–122

## Status and conventions

These notes were written from the frozen transcription, after the context was opened; no image was inspected and no transcription was changed for this research. Source paths below are relative to `MPL_84_097-145/`; the scan number is the archive scan, and line numbers are approximate lines of that individual frozen TeX file. The supplied `context/same_cote_84/MPL_84_146-193_notes.md` is abbreviated **C84** in the metadata, always with its item and scan reference; it and its entries in `context/notes/RESULTS_STATE.md` are earlier research claims/leads, not automatically reviewed results.

**RS-product** means **Hua, findings register, `84-product-quadratic-algebras-formula`**; **RS-χ** means **Hua, findings register, `84-chi-trivialised-extension-product`**; **RS-later** means the supplied register ID **`MPL_84_146-193 §2`**. “No direct RS entry” means that the supplied register does not state the particular claim, not that the wider literature was searched. Each A-item has a corresponding, actually executed context search in `algebra_context_searches.md`; proofs and reproducible calculations are in `algebra_derivations.md`, `algebra_checks.json`, and `relative_norm_checks.json`.

The allowed kind describes the source passage or the new research contribution, not an automatic verdict on its truth. Author-marked pending steps, including those later discharged, are separately registered in `algebra_unverified_steps.md`. No LM2/GT/congruence implication is inferred from the occurrence of norms, involutions, or \(\mathbf F_2\).

### A01 — The extension duality includes a checked minus sign

**Source:** `pages/MPL_84_097-145_84_scan097.tex`, scan 097, approximately lines 3–45. **Kind:** self-flagged. **Brief exact quotation:** `"g","?"`; `Attention au \unsure{signe}`; `dès que $\unsure{\varphi}$ est iso`.  
**Context:** C84, E160.2 (scan 160), L174.2 (scan 174), on perfect duality and determinant twists. **Relation:** adds. **RESULTS_STATE:** RS-later; no direct entry for this sign check.

The map \(g:E\to\mathcal A\otimes L\) induces \(-\mathrm{id}_L\) on the submodule and the identity on the quotient, and the two elementary evaluations end in “c'est OK” and “mais c'est aussi OK.” The ensuing correspondence between \(Q\) and \(N\) is explicitly conditional on the displayed isomorphism, whose symbol is transcription-doubtful; it should not be promoted to an unconditional identification of every extension with an algebra. Compared with the later duality leads, this supplies an earlier, author-checked sign convention rather than a new general duality theorem.

### A02 — The discriminant identity is asserted for a bare rank-two form

**Source:** `pages/MPL_84_097-145_84_scan098.tex`, scan 098, approximately lines 7–19. **Kind:** unproved claim. **Brief exact quotation:** `Q_N(\varphi_N(x))=-N(x)\delta_N`; `sans autre donnée`.  
**Context:** C84, no exact match for `Q_N` or `\delta_N`; compare L182.3 (scan 182) only for the distinct distinction between abstract and induced pairings. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The boxed formula is expressly claimed for any locally free rank-two module with a quadratic form, without additional algebra data. Its local \(Q\)-to-\(N\) comparison follows the minus sign on \(L\), but the minus sign in the displayed local norm is itself marked `\unsure{-}` and must remain a reading uncertainty. The statement therefore calls for reconstructing the meanings of \(Q_N,\varphi_N,\delta_N\) before checking it in that generality; the later product-discriminant formula is a different assertion and does not supply that proof.

### A03 — The first tensor-transpose attempt is withdrawn and restarted

**Source:** `pages/MPL_84_097-145_84_scan099.tex`, scan 099, approximately lines 12–41; compare scans 100–102. **Kind:** withdrawn in same text. **Brief exact quotation:** `\alpha\circ\mathrm{inc}=2\beta`; `Je pense à l'hom`.  
**Context:** C84, L172.5 (scan 172), the factorization of \(1+\sigma_1\otimes\sigma_2\). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

The lower construction, including its question-marked arrows and the proposed operator \(\xi\mapsto\xi+\bar\xi\), lies inside a deletion. The same operator is developed again without that deletion on scans 100–102, so the cancellation records an abandoned derivation rather than rejection of the trace construction. The later C84 factorization is a useful comparison for the surviving operator, but cannot make the cancelled arrows into live assertions.

### A04 — A module transpose is claimed before quadratic algebra structure

**Source:** `pages/MPL_84_097-145_84_scan100.tex`, scan 100, approximately lines 16–32. **Kind:** unproved claim. **Brief exact quotation:** `un sens sans utiliser les structures de rev.`; `$\chi=2$`.  
**Context:** C84, E160.2 (scan 160), L174.2 (scan 174), and E170.2 (scan 170). **Relation:** adds. **RESULTS_STATE:** RS-χ.

The author claims that \(i_A:\mathcal A\to\mathcal A_1\otimes\mathcal A_2\) can be obtained as the transpose of the extension product without the covering forms or the specialization \(\chi=2\). This is a statement about the underlying dualized module construction; its use as an algebra homomorphism requires the later quadratic structure and compatibility checks. C84's perfect-pairing and coherence cautions apply precisely here: the existence of a linear transpose does not by itself establish the full categorical claim in RS-χ.

### A05 — The reduced-trace pushout has a concrete compatibility condition

**Source:** `pages/MPL_84_097-145_84_scan101.tex`, scan 101, approximately lines 4–32. **Kind:** unpursued implication. **Brief exact quotation:** `Trace réduite`; `soient égaux`.  
**Context:** C84, L180.1 (scan 180), on the rank-three boundary and rank-two pushout; E170.1 (scan 170), on exactness hypotheses. **Relation:** restates. **RESULTS_STATE:** RS-product, RS-χ.

The construction pushes the extension by \(\mathcal A_1\otimes_0\mathcal A_2\) out along the trace that restricts to the two input traces. Defining \(i_A\) then requires its proposed scalar map and tensor map to agree on this boundary, which is exactly the compatibility verified for \(1+\sigma_1\otimes\sigma_2\) on scan 102. The extension pushout alone is not yet a proof of a multiplication or of categorical coherence.

### A06 — Scan 102 gives a conditional invariant-ring identification

**Source:** `pages/MPL_84_097-145_84_scan102.tex`, scan 102, approximately lines 23–36. **Kind:** unproved claim. **Brief exact quotation:** `l'une des deux structures $E_1,E_2$ est étale`; `est univ injectif`.  
**Context:** C84, L172.3–L172.5 (scan 172), L192.1 (scan 192). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

The NB assumes that at every characteristic-two point at least one input is étale, and under that hypothesis identifies the abstract product with the diagonal-involution invariants in the tensor algebra. In monic local coordinates the condition gives the covering by \(D(2),D(b_1),D(b_2)\); the invariant coefficient equations in `algebra_derivations.md` §2 prove equality of image and invariants on this cover, including after base change. This is stronger than the kernel calculation quoted in C84 L172.4 and is compatible with its exceptional cases, rather than a blanket claim of injectivity.

### A07 — The relative norm must lift through a possibly noninjective map

**Source:** `pages/MPL_84_097-145_84_scan103.tex`, scan 103, approximately lines 14–40. **Kind:** self-flagged. **Brief exact quotation:** `serait, essentiellement, $z\bar z$`; `On devrait avoir`.  
**Context:** C84, L172.4–L172.5 (scan 172), and L190.2 (scan 190). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

The desired \(A\)-valued relative norm is stronger data than the tensor element \(z\bar z\), because a value in the image of \(A\to A_1\otimes A_2\) need not have a unique lift. The author therefore specifies its polarization through the already constructed relative trace and its four diagonal values \(1,c_1,c_2,c_1c_2\). C84 L190.2 gives the ordinary norm on a rank-two algebra, whereas the present problem is a quadratic map from the rank-four tensor algebra to its abstract rank-two product.

### A08 — The doubt about injectivity is outside the NB's hypothesis

**Source:** `pages/MPL_84_097-145_84_scan104.tex`, scan 104, approximately lines 2–4; scan 105, line 21. **Kind:** self-flagged. **Brief exact quotation:** `on ne sait pas si`; `seulement`; `ni d'ailleurs surjectif`.  
**Context:** C84, L172.4 (scan 172), L192.1 (scan 192), R06 (scans 172/192). **Relation:** restates. **RESULTS_STATE:** RS-product, RS-later.

The author now declines to assume either injectivity or surjectivity onto the fixed algebra, which does not withdraw scan 102's conditional statement. The later lead's coefficient map \((a,d)\mapsto(a,db_2,db_1,2d)\) explains why an abstract quadratic algebra can survive when its tensor realization has a kernel. Any proof that cancels this map must therefore supply a hypothesis or instead prove equality in the abstract algebra.

### A09 — Hua's local formula matches the frozen signs on scan 104

**Source:** `pages/MPL_84_097-145_84_scan104.tex`, scan 104, approximately lines 11–30. **Kind:** reading question. **Brief exact quotation:** `b=b_1b_2`; `c=b_1^2c_2+b_2^2c_1-4c_1c_2`.  
**Context:** C84, L172.1–L172.2 (scan 172), R05 (scan 172), R10 (claim audit). **Relation:** restates. **RESULTS_STATE:** RS-product; RS-later.

For the frozen convention \(U_i^2+b_iU_i+c_i=0\), scan 104 gives \(U^2+b_1b_2U+c=0\) and \(U\mapsto2U_1U_2+b_1U_2+b_2U_1\), exactly the coefficients and generator map asserted in RS-product. There is no sign contradiction here, and the discriminant product follows algebraically from these displayed coefficients; the alternate generator shift reported by C84 R05 must not be substituted into the transcription. These local equations support that component of Hua's claim, while global commutativity/coherence and identification with a published construction remain separate claims with the supplied context's stated limitations.

### A10 — The relative trace factorization contains an essential factor two

**Source:** `pages/MPL_84_097-145_84_scan105.tex`, scan 105, approximately lines 17–29. **Kind:** unpursued implication. **Brief exact quotation:** `i\bigl(\operatorname{Tr}_{A_1\otimes A_2/A}(\xi)\bigr)=\xi+\bar\xi`; `=2\eta`.  
**Context:** C84, L172.5 (scan 172). **Relation:** restates. **RESULTS_STATE:** RS-product, RS-later.

The two equations \(i\operatorname{Tr}=1+\sigma_1\otimes\sigma_2\) and \(\operatorname{Tr}i=2\mathrm{id}_A\) agree with the later lead, including the trace-basis values \((2,-b_1,-b_2,U+b_1b_2)\). Consequently the tensor operator squares to twice itself, and is a projector only after division by two is available. In particular, the identities alone neither split \(i\) over an arbitrary base nor imply its injectivity in characteristic two.

### A11 — The norm uniqueness assertion needs both values and polarization

**Source:** `pages/MPL_84_097-145_84_scan105.tex`, scan 105, approximately lines 36–39; `pages/MPL_84_097-145_84_scan106.tex`, scan 106, lines 2–25. **Kind:** unproved claim. **Brief exact quotation:** `une application quadratique unique`; `\varphi_N(\xi,\eta)=\operatorname{Tr}_{A_1\otimes A_2/A}(\xi\bar\eta)`.  
**Context:** C84, L172.5 (scan 172), L190.2 (scan 190), with no relative rank-four-to-rank-two norm formula located. **Relation:** adds. **RESULTS_STATE:** RS-product.

For actual quadratic \(A_1,A_2\), the pure-tensor norm condition supplies the four diagonal values on a local tensor basis and the trace condition supplies its six mixed coefficients, so uniqueness does not require dividing by two. Existence still requires those coefficients to satisfy the claimed identities in the abstract target, rather than merely after applying \(i\). A12 supplies this local verification, including the scalar and multiplicative identities that turn the form into an \(A\)-quadratic relative norm.

### A12 — A universal local relative norm completes the missing coefficients

**Source:** `pages/MPL_84_097-145_84_scan103.tex`, scan 103, lines 25–40; scans 105–107, norm proposition. **Kind:** own idea. **Brief exact quotation:** `les éléments de la base $1,U_1,U_2,U_1\otimes U_2$`.  
**Context:** C84, L172.1/L172.5 (scan 172), L190.2 (scan 190): the product relation and trace are present, but not this relative form. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later. **Confidence:** high for the local identities, from exact universal monic reduction.

For \(B=R[u,v]/(u^2+b_1u+c_1,v^2+b_2v+c_2)\) and \(A=R[t]/(t^2+b_1b_2t+C)\), \(C=b_1^2c_2+b_2^2c_1-4c_1c_2\), the norm on the ordered basis \((1,u,v,uv)\) has diagonal coefficients \((1,c_1,c_2,c_1c_2)\) and mixed coefficients \((-b_1,-b_2,t+b_1b_2,-t,-b_2c_1,-b_1c_2)\) in the order \(01,02,03,12,13,23\). The full polynomial in `algebra_derivations.md` §1 satisfies the pure-tensor condition, the required polarization, \(iN(\xi)=\xi\bar\xi\), multiplicativity, \(N(i(a))=a^2\), norm transitivity, and \(A\)-linearity of the relative trace. The seven checks in `research_relative_norm.py` reduce by monic relations over an integer polynomial ring without inverting a parameter; they establish these local algebraic identities and do not claim a new literature result or full categorical coherence.

### A13 — Norm transitivity does not require cancelling the product embedding

**Source:** `pages/MPL_84_097-145_84_scan106.tex`, scan 106, approximately lines 26–53; `pages/MPL_84_097-145_84_scan107.tex`, scan 107, lines 2–12. **Kind:** self-flagged. **Brief exact quotation:** `Prouvons p.ex. la première`; `N\bar N=N_{A/O}(N)\qquad\text{OK}`.  
**Context:** C84, L172.4–L172.5 (scan 172), L190.2 (scan 190). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

The proposed proof groups the four conjugates into the two relative norms and ends with “OK,” but writes \(N(\xi)=\xi\bar\xi\) while suppressing the map \(i\). For actual rank-two input algebras, the final comparison is between scalars in \(R\), and \(R\to B\) is injective because \(B\) is locally free of rank four; this can justify the scalar equality without assuming \(A\to B\) injective. The abstract local norm calculation in A12 verifies the same transitivity directly, so the source's suppressed map need not be repaired in the transcript or used as an illicit cancellation.

### A14 — The new axioms allow nonflat and nonfaithful scalar maps

**Source:** `pages/MPL_84_097-145_84_scan107.tex`, scan 107, approximately lines 16–32; scan 108, lines 6–9. **Kind:** unpursued implication. **Brief exact quotation:** `ni même plat`; `soit injective`.  
**Context:** C84, L172.4 (scan 172), on a noninjective map between free algebras, which is a different situation; no “quasi-quadratique” axiomatization located. **Relation:** differs. **RESULTS_STATE:** RS-product concerns actual quadratic algebras; no direct entry for the enlarged axioms.

Here \(k\to A\) itself may be noninjective and \(A\) need not be flat over \(k\), so the definition must not be silently replaced by the usual locally free rank-two notion. Nevertheless the displayed axioms already force every \(\lambda\in\ker(k\to A)\) to satisfy \(2\lambda=0\) and \(\lambda^2=0\), by applying \(t\) and \(n\) to \(\lambda1_A=0\). This elementary consequence locates the possible nonfaithfulness in two-torsion and is consistent with the \(\mathbf Z/4\) example in A20.

### A15 — Norm invariance is proved after its separate axiom is withdrawn

**Source:** `pages/MPL_84_097-145_84_scan108.tex`, scan 108, approximately lines 48–69. **Kind:** withdrawn in same text. **Brief exact quotation:** `\deleted{\unsure{3^\circ)}}`; `donc on a bien $n(\bar x)=n(x)$`.  
**Context:** C84, E148.4 (scan 148), on the distinction between conjugation identities and multiplicativity; no matching derivation of norm invariance located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The cancelled label does not cancel the conclusion: the author derives \(n(\bar x)=n(x)\) from \(\bar x=t(x)1-x\), the quadratic translation formula, and \(n(1)=1\). The two \(t(x)^2\) terms cancel in the target \(k\), so this proof does not need injectivity of \(k\to A\) or multiplicativity of \(n\). This completed check should be distinguished from the genuinely missing multiplicativity condition in the later recap.

### A16 — When two is invertible the form reconstructs multiplication

**Source:** `pages/MPL_84_097-145_84_scan108.tex`, scan 108, approximately lines 33–46; scan 109, lines 18–32. **Kind:** unpursued implication. **Brief exact quotation:** `Au facteur $2$ près`; `la structure d'algèbre de $A$ est connue`.  
**Context:** C84, E148.4 (scan 148), L172.5 (scan 172), for distinct warnings about multiplicativity and division by two. **Relation:** adds. **RESULTS_STATE:** no direct entry for this reconstruction.

Combining multiplicativity of the conjugation with the subsequently imposed polarization identity gives \(2xy=t(x)y+t(y)x-\alpha(\varphi_n(x,y))\), whose right side is known from the pointed module, \(t\), and \(n\). Thus the multiplication is determined by those data when two is invertible, while the displayed equation cannot recover an arbitrary two-torsion contribution otherwise. In the same invertible-two case \(t(\lambda1)=2\lambda\) forces \(\alpha\) injective, explaining why the nonfaithful phenomenon in A20 cannot occur there.

### A17 — The polarization identity is an extra requirement without faithfulness

**Source:** `pages/MPL_84_097-145_84_scan109.tex`, scan 109, approximately lines 6–32. **Kind:** unpursued implication. **Brief exact quotation:** `sans supposer $\alpha$ injectif`.  
**Context:** C84, E148.4 (scan 148), L172.4 (scan 172); no exact quasi-quadratic polarization axiom located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

Polarizing \(\alpha(n(x))=x\bar x\) yields only \(\alpha(\varphi_n(y,z))=\alpha(t(y\bar z))\). Scan 109 explicitly adds equality in \(k\) itself when \(\alpha\) cannot be cancelled, rather than treating the equality after \(\alpha\) as sufficient. This is the same distinction between an abstract value and its possibly nonfaithful image that motivated the relative norm construction, although the two maps and object classes are different.

### A18 — The transitivity condition is optional and concerns forms

**Source:** `pages/MPL_84_097-145_84_scan109.tex`, scan 109, approximately lines 34–42; scan 110, lines 35–42. **Kind:** reading question. **Brief exact quotation:** `Une formule facultative`; `identité de $(2n)$-formes`.  
**Context:** C84, L190.2 (scan 190), on an ordinary quadratic norm; no matching optional tower axiom located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The trace and norm tower identities apply when \(k\) is locally free of rank \(n\) over \(k_0\) and \(A\) is locally free of rank \(2n\) over \(k_0\), while \(k\to A\) may still be noninjective. The author explicitly describes the norm equation as an identity of degree-\(2n\) forms, so verification only on a small base's points would not replace the stated form identity. Scan 110 makes this condition optional and defines the basic notion using only conditions \(1^\circ\)–\(5^\circ\).

### A19 — The five-axiom recap omits the earlier multiplicativity condition

**Source:** `pages/MPL_84_097-145_84_scan108.tex`, scan 108, lines 4–9 and 46; `pages/MPL_84_097-145_84_scan110.tex`, scan 110, lines 9–42. **Kind:** reading question. **Brief exact quotation:** `n(xy)=n(x)n(y)`; `satisfaisant $1^\circ$ à $5^\circ$`.  
**Context:** C84, E148.4 (scan 148), a related but different multiplicativity warning; exact searches for “quasi-quadratique” and this five-axiom issue are negative. **Relation:** adds. **RESULTS_STATE:** RS-product concerns actual quadratic algebras and does not settle this axiom question.

Condition (b) on scan 108 requires \(n\) to be multiplicative, but the five numbered conditions used to define “quasi-quadratique” on scan 110 do not repeat it. The margin on scan 108 explains why multiplicativity follows when \(\alpha\) is injective; A20 proves that it is not redundant for the explicitly allowed noninjective maps. Hence the displayed five axioms strictly weaken the earlier list containing (b), without deciding whether the author intended a weaker definition or an abbreviated recap.

### A20 — A finite counterexample separates the two axiom lists

**Source:** `pages/MPL_84_097-145_84_scan110.tex`, scan 110, approximately lines 9–42; compare scan 108, line 6. **Kind:** own idea. **Brief exact quotation:** `algèbre \uline{quasi-quadratique}`.  
**Context:** C84, no matching weak-axiom example; E148.4 (scan 148) concerns a different implication. **Relation:** adds. **RESULTS_STATE:** no direct entry; RS-product is about actual quadratic algebras. **Confidence:** high, from the coefficient proof and exhaustive finite check.

Let \(k=\mathbf Z/4\), \(A=\mathbf F_2[e,f]/(e^2,f^2)\), and for \(x=a+be+cf+d\,ef\) with binary coefficients set \(t(x)=2a\) and \(n(x)=a+2d\), using the reduction scalar map. Then \(\bar x=x\), the polarization is \(2aa'\), and all five displayed axioms hold, whereas \(n(ef)=2\ne n(e)n(f)=0\). Multiplicativity fails even on units: \(n((1+e)(1+f))=3\) while \(n(1+e)n(1+f)=1\). The proof in `algebra_derivations.md` §3 extends the construction to quadratic laws under every \(k\)-algebra base change, and `research_algebra_checks.py` checks all four scalars, sixteen algebra elements, and 256 ordered pairs, finding 96 multiplicativity failures.

### A21 — The three intermediate algebras are part of an enlarged formal setup

**Source:** `pages/MPL_84_097-145_84_scan111.tex`, scan 111, approximately lines 4–32. **Kind:** unpursued implication. **Brief exact quotation:** `sans forcément supposer $k\mathrel{-\!\!-\!\!-}A_i$ injectif`; `pas néc. inj.`.  
**Context:** C84, no exact “biquadratique” or three-intermediate-algebra setup located; L172.4 (scan 172) concerns a different noninjective realization map. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The data comprise three quasi-quadratic \(A_i/k\), three maps \(A_i\to A\), and quasi-quadratic structures \(A/A_i\), with neither kind of scalar map assumed injective. This does not assert that \(A\) has rank four over \(k\), or even that the images of the \(A_i\) generate it. The subsequent compatibility axioms must consequently be read as imposed structure, not as automatic properties of an ordinary biquadratic field or étale extension.

### A22 — The cancelled involution condition returns as a live axiom

**Source:** `pages/MPL_84_097-145_84_scan111.tex`, scan 111, approximately lines 33–44; scan 114, lines 4–21. **Kind:** withdrawn in same text. **Brief exact quotation:** `\sigma_1\sigma_2\sigma_3=\operatorname{id}`; `On veut la condition`.  
**Context:** C84, no matching three-involution compatibility located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The bottom of scan 111 crosses out the initial statement that the three involutions commute with product one. Scan 114 restores \(\sigma_1\sigma_2\sigma_3=1\) as condition \(3^\circ\) and derives pairwise commutation, so the cancellation is a reordering of the axiomatization. Its automatic validity on the subalgebra generated by the \(A_i\) does not suffice on all of \(A\) unless that subalgebra is the whole algebra.

### A23 — Six compatibility squares do not assert tensor-product isomorphisms

**Source:** `pages/MPL_84_097-145_84_scan112.tex`, scan 112, approximately lines 2–29. **Kind:** unpursued implication. **Brief exact quotation:** `un des 6 diagrammes`; `s'annule au moins sur le noyau`.  
**Context:** C84, E170.1 (scan 170), on exactness limitations; no matching six-square system located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

For each ordered pair of distinct indices, the author asks the trace and norm to behave as under quadratic base change, while explicitly withholding quadraticity, generation, and injectivity of the tensor map. The trace requirement is therefore a factorization condition: \(t_i\otimes\mathrm{id}_{A_j}\) must annihilate the kernel of \(A_i\otimes_kA_j\to A\). It determines \(T_j\) on the subalgebra generated by those two images, but does not determine a trace on any additional elements of \(A\).

### A24 — The bilinear verification on scan 113 is marked complete

**Source:** `pages/MPL_84_097-145_84_scan113.tex`, scan 113, approximately lines 2–29; scan 114, line 2. **Kind:** self-flagged. **Brief exact quotation:** `Il reste à vérifier`; `O.K.`.  
**Context:** C84, no matching relative-norm base-change verification located; compare L190.2 (scan 190) only for ordinary norm coordinates. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The indicated argument compares the quadratic maps on pure tensors and then compares their polar forms using \(\alpha_1(\bar y)=\sigma_2(\alpha_1(y))\) and trace compatibility. The author marks this remaining bilinear check “O.K.” and next observes that norm compatibility also implies trace compatibility by comparing \(a\) and \(1+a\). This is a discharged author-marked proof obligation, while the two literal formula problems in A25 remain separate reading questions.

### A25 — Two literal entries in the norm argument have incompatible types

**Source:** `pages/MPL_84_097-145_84_scan113.tex`, scan 113, approximately lines 8–16. **Kind:** reading question. **Brief exact quotation:** `t_1(x_1)`; `par chgt. de base $k\longrightarrow A_1$`.  
**Context:** C84, L190.2 (scan 190), explicitly distinguishes trace and norm formulas; no matching discussion of scan 113 located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The frozen pure-tensor value is \(t_1(x_1)x_2^2\), although the preceding norm compatibility and quadratic homogeneity would yield \(n_1(x_1)x_2^2\). The prose also names base change \(k\to A_1\) where the displayed target and preceding margin name \(A_2\). These are mathematical type checks on the frozen reading, not authorization to change the symbols or a claim that the image has been reread.

### A26 — Common absolute trace is assumed when the base map is nonfaithful

**Source:** `pages/MPL_84_097-145_84_scan114.tex`, scan 114, approximately lines 23–45. **Kind:** self-flagged. **Brief exact quotation:** `du moins si $k\mathbin{-}A$ injectif`; `on la suppose \unsure{vérifiée} en tous cas`.  
**Context:** C84, L172.4 (scan 172), on the danger of cancelling a noninjective map; no common-trace axiom located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The cyclic expansions of \(\sigma_1\sigma_2\sigma_3=1\) identify the images of \(t_iT_i(x)\) in \(A\). Equality of those values in \(k\) follows under injectivity of \(k\to A\), but the margin explicitly assumes it in the remaining cases. The common trace \(T_{A/k}\) and the identity \(2x=T_1(x)+T_2(x)+T_3(x)-T_{A/k}(x)\) therefore use that extra scalar-level requirement.

### A27 — The norm argument proves a scalar equality only under faithfulness

**Source:** `pages/MPL_84_097-145_84_scan115.tex`, scan 115, approximately lines 2–48. **Kind:** self-flagged. **Brief exact quotation:** `On s'attend à trouver` [deleted]; `si $k\mathbin{-}A$ est \uline{injectif}`; `O.K.`.  
**Context:** C84, E148.4 (scan 148), L172.4 (scan 172), for separate multiplicativity and faithfulness distinctions. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The cancelled expectation is replaced by a four-conjugate argument, with the permutation display giving \(x_i=\sigma_i(x)\) for that calculation even though the preceding frozen line retains `T_i|\sigma_i` uncertainty. Each \(n_i(N_i(x))\) has the same image \(x_0x_1x_2x_3\) in \(A\), and the author explicitly restricts equality in \(k\) to the case \(k\to A\) injective. Under that qualification the common scalar norm gives \(N_1(x)N_2(x)N_3(x)=x^2N_{A/k}(x)\); the page does not prove automatic scalar equality for every nonfaithful setup.

### A28 — The acting group is the even subgroup, and the action may be trivial

**Source:** `pages/MPL_84_097-145_84_scan116.tex`, scan 116, approximately lines 6–30; scan 117, lines 2–8. **Kind:** unpursued implication. **Brief exact quotation:** `Il n'y a pas en général d'opération de ce groupe sur $A$`; `soit pair`.  
**Context:** C84, no matching three-factor parity action; R09 records the absence of a demonstrated LM2 bridge. **Relation:** adds. **RESULTS_STATE:** no direct entry for this action; `MPL_84_146-193 R09` supplies only the context caution.

The tensor product carries \(\mathbf F_2^3\), but an automorphism fixing two generating intermediate algebras cannot simultaneously induce a nontrivial involution on the third image, explaining why the whole action need not descend. The subgroup \(\Gamma=\ker(\mathbf F_2^3\to\mathbf F_2)\), with nonzero elements \(011,101,110\), does act through the compatible relative involutions \(\sigma_{A/A_i}\). This is a homomorphism from a four-element group, not an assertion of faithful action, as the characteristic-two example A32 demonstrates.

### A29 — The three-factor exceptional locus is precisely qualified

**Source:** `pages/MPL_84_097-145_84_scan117.tex`, scan 117, approximately lines 12–26. **Kind:** unproved claim. **Brief exact quotation:** `deux au moins des $A_i$ soient non étales`; `est un \uline{iso}`.  
**Context:** C84, L172.3 (scan 172), L192.1 (scan 192), concerning the two-factor characteristic-two exception. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

For actual quadratic inputs, the author claims that the contracted triple product maps isomorphically to \((A_1\otimes A_2\otimes A_3)^\Gamma\) away from characteristic-two points where at least two factors are nonétale. This allows characteristic-two points with two étale inputs and should not be paraphrased as requiring all three inputs étale or excluding characteristic two altogether. It is a three-factor invariant-ring assertion beyond the later lead's two-factor kernel calculation; A30 supplies a proof on the stated open locus.

### A30 — The stated open locus admits a direct invariant calculation

**Source:** `pages/MPL_84_097-145_84_scan117.tex`, scan 117, approximately lines 22–26. **Kind:** own idea. **Brief exact quotation:** `invariants sous $\unsure{\gamma|\Gamma}$`.  
**Context:** C84, L172.1–L172.5 (scan 172), L192.1 (scan 192), provide the two-factor formula/trace leads but no triple invariant proof. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later. **Confidence:** high for the asserted sufficient locus, from the two explicit local calculations.

When two is invertible, putting \(v_i=2u_i+b_i\) gives invariant basis \(1,v_1v_2v_3\), and the iterated product generator maps to \((v_1v_2v_3-b_1b_2b_3)/2\). When two inputs are étale, a faithfully flat splitting makes the tensor algebra four copies of the third algebra, on which \(\Gamma\) permutes the four factors transitively with the prescribed conjugations, so the invariants and the contracted product both identify with that third algebra. The coefficient calculation and descent of this finite kernel computation are written out in `algebra_derivations.md` §2, proving sufficiency on \(D(2)\cup D(\delta_1\delta_2)\cup D(\delta_2\delta_3)\cup D(\delta_3\delta_1)\) without asserting necessity at every remaining point.

### A31 — Scalar image is the goal; the fixed-ring equality is sufficient

**Source:** `pages/MPL_84_097-145_84_scan118.tex`, scan 118, approximately lines 6–21. **Kind:** conjecture. **Brief exact quotation:** `j'ai envie de \unsure{prouver}`; `à valeurs dans $k.1_A$`.  
**Context:** C84, no matching constant-section problem or three-factor fixed-ring criterion located; L192.1 (scan 192) is only a related degeneration warning. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The proposed constant map is a factorization through a section of the contracted triple cover, and the author now assumes \(k\to A\) injective so that scalar image of the algebra map is equivalent to that section. The equality \(A^\Gamma=k.1_A\) is introduced as a sufficient condition, with an explicit warning that it can fail in characteristic two. It is stronger than the desired statement about the particular image \(f(B)\), so failure of the fixed-ring equality alone does not refute the section claim.

### A32 — A characteristic-two model separates scalar image from fixed ring

**Source:** `pages/MPL_84_097-145_84_scan118.tex`, scan 118, approximately lines 17–21; compare scan 117. **Kind:** own idea. **Brief exact quotation:** `pas tjrs vérifiée`; `à cause de la car. 2`.  
**Context:** C84, L192.1/R06 (scans 172/192), distinguish an abstract product from a collapsed tensor realization; no example for the present fixed-ring question located. **Relation:** adds. **RESULTS_STATE:** RS-product is related only through the actual quadratic product. **Confidence:** high, from explicit bases and relative trace/norm formulas.

Take \(k=\mathbf F_2\), \(A=k[e,f]/(e^2,f^2)\), and \(A_1,A_2,A_3\) generated respectively by \(e,f,e+f\); each pair tensor map is an isomorphism and \(A\) is genuinely quadratic over each \(A_i\). All relative traces vanish and all relative norms are \(x\mapsto x^2\), so every relative involution is the identity and \(A^\Gamma=A\ne k\). Nevertheless the contracted triple algebra is \(k[t]/(t^2)\) with \(t\mapsto0\), giving scalar image and a section. Section 4 of `algebra_derivations.md` and the finite basis checks thus realize the distinction in A31 without weakening the input algebras to arbitrary quasi-quadratic objects.

### A33 — The invertible-two case is discharged by the factor four

**Source:** `pages/MPL_84_097-145_84_scan119.tex`, scan 119, approximately lines 2–16. **Kind:** self-flagged. **Brief exact quotation:** `a=\frac14T_{A/k}(a)\in k\qquad\text{O.K.}`.  
**Context:** C84, no matching three-involution averaging argument; L172.5 (scan 172) contains a different factor-two projector. **Relation:** adds. **RESULTS_STATE:** no direct entry.

For \(a\in A^\Gamma\), each \(T_i(a)=2a\), while the common-trace identity gives \(T_1(a)+T_2(a)+T_3(a)=2a+T_{A/k}(a)\); therefore \(4a=T_{A/k}(a)\). If two is invertible, this forces \(a\) to be scalar and establishes the sufficient fixed-ring condition used on scan 118. The proof depends on the common trace already imposed in the nonfaithful setup and is not an averaging argument over the full eight-element tensor group.

### A34 — The étale proposition needs generation and the inserted fixed-ring condition

**Source:** `pages/MPL_84_097-145_84_scan119.tex`, scan 119, approximately lines 20–30; scan 120, lines 2–8; scan 121, lines 2–6. **Kind:** unproved claim. **Brief exact quotation:** `enfin $A^{\unsure{\gamma|\Gamma}}=k.1_A$`; `par twist`.  
**Context:** C84, no matching three-cover twisting proposition; E170.1 (scan 170) is a general exactness caution, not its proof. **Relation:** adds. **RESULTS_STATE:** no direct entry.

The proposition assumes all three inputs étale, injectivity of \(k\to A\), generation by the three images, and the inserted equality \(A^\Gamma=k\). After splitting the covers, the section cuts out one parity fibre \(J\) of four points, and the author aims to show that the closed \(\Gamma\)-stable subscheme \(\operatorname{Spec}A\subset J_X\) is all of \(J_X\), yielding all three pair-product isomorphisms and the twisted description. The original application supplies closedness explicitly on scan 119; the lemma's target and formulation nevertheless require the checks in A35–A36.

### A35 — The frozen target of lemma 120 makes its injectivity condition vacuous

**Source:** `pages/MPL_84_097-145_84_scan120.tex`, scan 120, approximately lines 10–18; scan 121, lines 2–6. **Kind:** reading question. **Brief exact quotation:** `k\longrightarrow\Gamma(\unsure{X_J},\mathcal O_{\unsure{X_J}})`; `(\simeq k^J)`.  
**Context:** C84, no matching transitive-subschema lemma or \(X_J\) target located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

Under the frozen first reading, condition (b) targets the ambient \(X_J\), so it is automatic for nonempty \(J\) and cannot force a stable proper closed subscheme to equal \(X_J\): take \(J\) a singleton, \(k=\mathbf Z\), and \(\mathcal X=\operatorname{Spec}\mathbf F_2\). The subsequent ideal proof instead needs injectivity of \(k\to\Gamma(\mathcal X,\mathcal O_{\mathcal X})\), whose kernel is the intersection of the component ideals. This diagnoses a target-level problem in the frozen reading, including its own `\unsure{X_J}` notation, and does not claim a visual correction.

### A36 — Even with the target repaired, the lemma requires a closed subscheme

**Source:** `pages/MPL_84_097-145_84_scan120.tex`, scan 120, approximately lines 10–18; compare scan 119, line 21. **Kind:** own idea. **Brief exact quotation:** `un sous-schéma`; `un sous-schéma fermé de $X$ donc à un idéal`.  
**Context:** C84, no matching closed-subscheme/transitive-action lemma located. **Relation:** adds. **RESULTS_STATE:** no direct entry. **Confidence:** high, from the explicit open-immersion counterexample and the component-ideal proof.

With \(J\) a singleton and \(k=\mathbf Z\), the proper open subscheme \(D(2)=\operatorname{Spec}\mathbf Z[1/2]\) is stable and has injective scalar map, so “subscheme” alone still does not imply equality even if condition (b) targets \(\mathcal X\). For a closed subscheme, transitivity makes all component ideals equal and scalar injectivity kills their intersection, proving the intended conclusion. Thus adding closedness repairs the argument used in scan 119, where generation had already supplied a closed immersion; this gap in the standalone lemma does not by itself refute the étale proposition.

### A37 — The nonétale fibre construction is a stated program

**Source:** `pages/MPL_84_097-145_84_scan121.tex`, scan 121, approximately lines 9–22. **Kind:** conjecture. **Brief exact quotation:** `J'ai envie de vérifier`; `sans condition étale`; `Ceci doit généraliser`.  
**Context:** C84, L192.1/R06 (scans 172/192), on realization failure; no matching three-cover fibre construction located. **Relation:** adds. **RESULTS_STATE:** RS-product does not settle this further construction.

The author proposes that a section \(\varepsilon\) of any contracted triple quadratic cover should endow \(\pi^{-1}(\varepsilon)\) with the corresponding biquadratic structure relative to the three inputs. This extends the previous étale classification and the canonical two-factor example, but is introduced as something to verify, not as a completed theorem. The next page's nonflatness warning explains why a proof must work with the enlarged quasi-quadratic notion rather than silently infer a finite locally free degree-four cover.

### A38 — The universal map is finite but need not have flat degree four

**Source:** `pages/MPL_84_097-145_84_scan122.tex`, scan 122, approximately lines 2–30. **Kind:** self-flagged. **Brief exact quotation:** `n'est pas même fini loc. libre, ni même plat`; `4(!)`; `pas univ. inj.`.  
**Context:** C84, E170.1 (scan 170), L172.4 (scan 172), L192.1 (scan 192), for distinct flatness and realization issues. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

The universal base is the contracted triple cover and the total space is the full threefold fibre product, with the maps toward its three base-changed inputs. Although the tensor algebra is finite over this base, the author explicitly denies a general flatness claim and annotates the expected degrees by exclamation marks. The labels \(4(!)\) and \(2(!)\) must therefore not be reported as established locally free ranks over that new base.

### A39 — Three dual-number inputs give an explicit nonflat universal map

**Source:** `pages/MPL_84_097-145_84_scan122.tex`, scan 122, approximately lines 25–31. **Kind:** own idea. **Brief exact quotation:** `ni même plat (mais il est bien surjectif)`.  
**Context:** C84, L192.1/R06 (scans 172/192), the two-factor collapse lead; no three-factor nonflat example located. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later. **Confidence:** high, from the explicit module action and tensor test.

For three copies of \(k[z]/(z^2)\) over \(k=\mathbf F_2\), the contracted algebra is \(B_0=k[t]/(t^2)\) and the full tensor algebra is \(B=k[e,f,g]/(e^2,f^2,g^2)\), with \(t\mapsto0\). The map on spectra is finite and surjective, but tensoring the injection \((t)\hookrightarrow B_0\) with \(B\) gives the zero map from \((t)\otimes_{B_0}B\simeq B\ne0\), proving nonflatness. Its fibre at \(t=0\) has \(k\)-dimension eight, demonstrating why the indicated degree four is not a constant flat rank. The derivation and finite-algebra check illustrate the author's warning and do not disprove the weaker quasi-quadratic program of A37.

### A40 — The final relative trace and norm are still to be constructed

**Source:** `pages/MPL_84_097-145_84_scan122.tex`, scan 122, approximately lines 27–32. **Kind:** self-flagged. **Brief exact quotation:** `N_1\unsure{?}`; `$\operatorname{Tr}_1$ doit être $B_0$-linéaire, $N_1$ $B_0$-quadratique\ldots`.  
**Context:** C84, L172.5 (scan 172) and L190.2 (scan 190), the trace and ordinary norm leads, with no construction for this \(B\to B_1\) setting. **Relation:** adds. **RESULTS_STATE:** no direct entry for this pending relative structure.

The diagram asks for maps \(B\to B_1=A_1\otimes B_0\), while the final sentence only begins to demand \(B_0\)-linearity and \(B_0\)-quadraticity. A completed quasi-quadratic structure on \(B/B_1\) would in particular require the corresponding \(B_1\)-linearity/homogeneity and the five defining axioms, together with the compatibilities of the three intermediate structures. The question-marked norm label and unfinished sentence leave that construction open in this interval; nonflatness alone cannot settle it because flatness was explicitly excluded from the definition.

