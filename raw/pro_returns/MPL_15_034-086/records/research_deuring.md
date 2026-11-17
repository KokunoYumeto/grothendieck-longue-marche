# Research draft: Deuring gerbes and crystalline orientations (scans 034–056)

Research only, after the transcription freeze of 2026-11-17 20:48:04 UTC. No page or combined-transcription file was changed. `context/README.md`, the complete `context/notes/RESULTS_STATE.md` (RS), and `context/hua_project/README.md` were read before using their material. References to Hua below mean **Hua, modernised reading of cote 15**, `context/hua_project/15.modern.tex`; his page number is the present scan number minus one, and his mathematical repairs are credited rather than imported into the frozen text. CT = `context/MPL_16+47+54+44_transcription.tex`; CN = the matching notes file. The two same-cote note filenames are given in full on first use. All their observations are first-pass leads, not independently certified results.

## D01 — Norm rigidification and reduction of the band

**Witness:** 15/034, “gerbe de groupe $\mu_n$”. **Kind:** unproved claim / literature comparison. **Context:** Hua, subsection “« Cat. de Deuring sur A » : foncteurs admissibles, normes, ramification”, pp. 33–35 (= scans 034–036), restates the intended reduction; `context/same_cote_15/MPL_15_087-138_notes.md`, T18–T18b, scans 135–137, adds the analogous gerbe of a fibre functor together with a specified Tate trivialization. **RS:** MPL_15_087-138 §124 and S15 [first-pass leads]; WG2 §2.4 #3 [unchecked plan], unchanged.

The reduction from a multiplicative-group band to $\mu_n$ requires the determinant/norm trivialization as part of the object, so its automorphisms are precisely the scalars with $\lambda^n=1$. The general lifting-gerbe construction has a precise later analogue in Deligne–Milne, Proposition 5.8, but that proposition does not identify the present order-module category with every $\mu_n$-gerbe over an arbitrary ring [DM12]. In particular, the rank/weight words marked uncertain in scan 034 remain a reading question; Hua explicitly modernizes those words and cannot settle the ink.

## D02 — The right endpoint of the ramification sequence has a norm obstruction

**Witness:** 15/036, “$\operatorname{Ram}(C/A)$”. **Kind:** own idea, making a supplied warning explicit. **Context:** Hua, same subsection, pp. 33–35 (= scans 034–036), already flags unrestricted surjectivity; this adds its obstruction map, while CT 16/049 has only the broader category programme. **RS:** WG2 §2.4 #3 [unchecked plan]; no settled gerbe result in RS; no status change.

If a ramification class is represented by a bimodule $P$, replacing $P$ by $L\otimes_A P$ changes its reduced norm by $L^{\otimes n}$, hence defines $\delta([P])=[N(P)]\in\operatorname{Pic}(A)/n\operatorname{Pic}(A)$. A norm-trivialized representative exists exactly when this class vanishes, so the displayed surjection onto all of $\operatorname{Ram}(C/A)$ needs that additional condition; it is automatic for the subsequently used $\mathbb Z$, $\mathbb Z[1/p]$, and $\mathbb Z_p$. **Confidence: high**, conditional on the written norm transformation law, because the obstruction is the elementary line-bundle equation $N(P)\otimes L^{\otimes n}\simeq A$; this does not assert a counterexample within the later principal-ideal bases.

## D03 — The explicitly unfinished identification of the two Picard actions

**Witness:** 15/036, “À vérifier!!”. **Kind:** self-flagged. **Context:** Hua, same subsection, p. 35 (= scan 036), restates the equivalence-category torsor but does not supply the requested coherence verification; same-cote notes T18, scan 135, separately warn that an isomorphism class does not specify an isomorphism. **RS:** MPL_15_087-138 §124 [first-pass lead]; WG2 §2.4 #3 [unchecked plan], unchanged.

Choosing an equivalence between the two categories transports autoequivalences by conjugation, but independence of that choice as a Picard equivalence requires the commutativity constraints and their coherence. The margin therefore records a genuine unfinished step, not merely a request to compute the two abstract groups of isomorphism classes. The prose $\pi_1$ and displayed $\pi_0$ on scan 036 remain distinct frozen readings; contextual expectations justify a note, not a transcription correction.

## D04 — The canonical norm object is a hypothesis at this point

**Witness:** 15/038, “Supposons qu'on ait pu associer”. **Kind:** unproved claim / conditional construction. **Context:** Hua, same subsection, p. 37 (= scan 038), invokes his earlier p. 21, outside this packet, and states the canonical object affirmatively; the present witness differs by explicitly supposing it. **RS:** WG2 §2.4 #3 [unchecked plan]; RS orientation says no existing proved Deuring result, unchanged.

All subsequent independence from the representative category uses the specified lift $c:\operatorname{Eq}(C)\to\operatorname{Eq}(C,T)$, not merely existence of some object of $V(C)$. Hua's reference to an earlier construction is a useful lead, but the earlier source scan is not included here and cannot turn this conditional sentence into a proof within the supplied packet. Checking the functorial and composition laws for $c$ is the concrete missing obligation.

## D05 — The local quaternion class explains the real obstruction

**Witness:** 15/040, “ramifié exactement”; 052, “elle est non triviale”. **Kind:** unpursued implication / source comparison. **Context:** Hua, same subsection p. 39 (= scan 040), identifies $B_{p,\infty}$; `context/same_cote_15/MPL_15_195-228+18_002-017_notes.md`, A12, scan 207, asks for a real-neutralization obstruction without constructing one there. **RS:** MPL_15_087-138 §124 [first-pass lead]; claims #964 [open follow-up about archimedean places], unchanged.

Deuring's classification gives a maximal endomorphism order in the definite rational quaternion algebra $B_{p,\infty}$, whose two nonzero local Brauer invariants are $1/2$ at $p$ and $\infty$ and whose invariants vanish elsewhere [Deu; Voi42]. Thus this packet supplies a concrete real quaternion obstruction absent from the later general question, but no conclusion about arbitrary motivic categories follows. The frozen alternative “$2|p$” in scan 040 must remain marked; the mathematics provides only a context-induced future reading question.

## D06 — Why the ramified local extension splits

**Witness:** 15/040, “engendré par $(\mathfrak m,p)$”. **Kind:** own idea / independently checked supplied calculation. **Context:** Hua, same subsection p. 39 (= scan 040), already gives this calculation; the present item restates and verifies it, without claiming novelty. **RS:** no settled Deuring result; WG2 §2.4 #3 [unchecked plan], unchanged.

For the maximal order in the local quaternion division algebra, $\mathfrak m^2=pO$ and $N(\mathfrak m)=p\mathbb Z_p$; identifying $pO$ with $O$ by multiplication by $p^{-1}$ sends the squared norm trivialization to the identity because $\operatorname{Nrd}(p)=p^2$. Hence $(\mathfrak m,p)$ has order two and splits the displayed extension, whereas the unit square classes are only its kernel. **Confidence: high**, because both powers and the scalar reduced norm are explicit; the resulting abstract group is $\mathbb Q_p^*/\mathbb Q_p^{*2}$, not $H^1(\mathbb Z_p,\mu_2)$ alone.

## D07 — The prime two changes both the size and the topology

**Witness:** 15/040, “si $p\ne2$”; 042, deleted “ét”. **Kind:** own idea / explicit boundary calculation. **Context:** Hua, same subsection p. 39 (= scan 040), retains the odd-prime qualification but does not compute the dyadic case; CT 54/005–007 concerns characteristic-$p$ Cartier duality and differs from this flat Kummer issue. **RS:** WG2 §2.4 #3 [unchecked plan]; same-cote P04, 18/005 [first-pass lead], unchanged.

Over $\mathbb Z_2$, the unit square classes have representatives $1,3,5,7$ modulo 8, so $\mathbb Z_2^*/\mathbb Z_2^{*2}\simeq(\mathbb Z/2)^2$ and the whole split local group has order 8. The identification with Kummer cohomology is valid in the fppf topology even when 2 is not invertible, whereas the usual étale Kummer exact sequence requires invertibility [Kum]. **Confidence: high**, by odd squares modulo 8 and successive square-root lifting; the deleted topology label is therefore mathematically consequential without authorizing restoration of any replacement.

## D08 — The written adèle ring and the quotient can be made explicit

**Witness:** 15/042, “$\Gamma=\Gamma'/f(\pm1)$”; 046, “$\mathbb A=\prod_\ell\mathbb Z_\ell$”. **Kind:** own idea / terminology clarification. **Context:** Hua, subsection “Le torseur adélique et l'élément de Deuring”, pp. 41–45 (= scans 042–046), already distinguishes the written ring from the full adèle ring; this adds the coordinate quotient map. **RS:** MPL_15_087-138 §125 [negative first-pass search, not a theorem]; LM6 A.22 [Open, return's claim], unchanged.

With the real factor included as specified, the written ring is $\widehat{\mathbb Z}\times\mathbb R$, and the unit-square formula should be read on that ring rather than silently enlarged to rational adèles. In coordinates $(u,v,e,w)$, with $e\in\mathbb Z/2$, the quotient by $(p,1,1,p)$ is explicitly $(u,v,e,w)\mapsto(u p^{-e},v,w)$ because $p$ is a real square. **Confidence: high**, by direct kernel computation, which verifies the group-level splitting without providing a distinguished point of its torsor.

## D09 — Frobenius triviality at the level of classes leaves gerbe coherence to prove

**Witness:** 15/044, “$f$ opère trivialement”; “Ceci suggère”. **Kind:** unproved claim / unpursued implication. **Context:** Hua, same subsection pp. 43–45 (= scans 044–046), restates the class-level descent and the subsequent suggestion; same-cote A13, scans 207–209, also distinguishes the gerbe of points from individual isomorphism torsors. **RS:** claims #964 [open follow-up]; WG2 §2.4 #3 [unchecked plan], unchanged.

The quotient kills precisely the translation computed in scan 042, so the stated Frobenius action on $\mathcal T$ is trivial once that action formula is granted. It does not by itself produce coherent descent isomorphisms for the underlying gerbe or eliminate its 2-automorphisms: these are the additional data investigated on scan 046–048. The wording marks the transition from a class-set calculation to a gerbe construction as a suggestion, not a completed descent theorem.

## D10 — The cyclotomic quotient is concretely a product, not the advertised field

**Witness:** 15/046, “par les polynômes cyclotomiques”. **Kind:** own idea / explicit check of a supplied objection. **Context:** Hua, same subsection p. 45 (= scan 046), already says that the quotient is generally not a field; this adds a minimal factorization and distinguishes field selection from compatible transition maps. **RS:** no matching settled result; WG2 §2.4 #3 [unchecked plan], unchanged.

For $p=2,n=3$, $\Phi_7(T)=(T^3+T+1)(T^3+T^2+1)$ over $\mathbb F_2$, with two coprime irreducible cubics, so the written quotient is $\mathbb F_8\times\mathbb F_8$. Selecting one irreducible factor and compatible embeddings along a divisibility-indexed tower would be additional choices, absent from the displayed formula. **Confidence: high**, because the factorization and irreducibility (no roots in $\mathbb F_2$) are direct calculations; this refutes that proposed formula, not existence of an algebraic closure.

## D11 — Residual 2-automorphisms obstruct literal uniqueness

**Witness:** 15/048, “$\pi_2=\mathbb Z/2\mathbb Z$”. **Kind:** unpursued implication. **Context:** Hua, same subsection p. 47 (= scan 048), restates the 2-categorical description; same-cote T18, scan 135, likewise records cancelled canonicity, while A13, scans 207–209, separates groupoids from sets. **RS:** MPL_15_087-138 §124 [first-pass lead]; claims #964 [open follow-up], unchanged.

The stipulated vanishing of $\pi_0$ and $\pi_1$ makes objects and equivalences unique at the preceding levels, but the nonzero $\pi_2$ retains exactly two 2-isomorphisms. It cannot justify uniqueness of every comparison without the persistent sign qualification. Deligne–Milne's appendix explicitly distinguishes a neutral gerbe from its choice of global object [DM12], which is the relevant logical distinction here.

## D12 — A canonical torsor is not a chosen Deuring element

**Witness:** 15/048, deleted “point ... can.”; 050, “l'élément de Deuring”. **Kind:** withdrawn in the same text / unproved claim. **Context:** Hua, same subsection pp. 47–49 (= scans 048–050), correctly distinguishes a chosen torsor element from the geometric assertion; same-cote T22, scan 137, records another explicit choice of arithmetic trivialization. **RS:** MPL_15_087-138 §124 [first-pass lead]; LM6 A.22 [Open, return's claim], unchanged.

Scan 048 cancels the assertion of a canonical point while retaining the canonical torsor, and 050 separately asserts that supersingular elliptic curves furnish $\xi_p$. The source therefore does not derive the point formally from the square-class group or the categorical quotient. Scans 054–056 reformulate its characterization but do not compute its value.

## D13 — The neutral comparison gerbe and the nonneutral real gerbe are different

**Witness:** 15/050, “Cette gerbe est triviale”; 052, “elle est non triviale”. **Kind:** reading question / resolved distinction. **Context:** Hua, same subsection pp. 49–51 (= scans 050–052), treats the same two objects but reports an uncertain earlier reading on p. 51; the frozen 052 directly supports nontriviality and thus differs from that palaeographic warning. **RS:** MPL_15_087-138 §124 [first-pass lead]; same-cote A12–A13, scans 207–209 [first-pass leads]; no status change.

The former is the gerbe $\mathfrak G(\xi)$ of comparisons with the fixed local models, whereas the latter is $h(\xi_p)_{\mathbb R}$ itself. Two nonneutral $\mu_2$-gerbes with the same class can admit an equivalence, so a neutral comparison gerbe is compatible with a nonzero quaternion class of each operand. Neither assertion supplies a preferred equivalence or removes the real sign.

## D14 — The two real signs occur at different categorical levels

**Witness:** 15/052, “mais il reste l'ambiguïté des signes”. **Kind:** unpursued implication. **Context:** Hua, same subsection pp. 39,49–51 (= scans 040,050–052), restates the ambiguity; same-cote T04 and T06, scans 117–119, already distinguish $H^1$, $H^2$, and the quaternionic odd object, while T27 gives the semilinear descent formula. **RS:** MPL_18_018-062 RH19 [first-pass lead]; claims #964 [open follow-up], unchanged.

Classes of equivalences with the chosen real model form an $H^1(\mathbb R,\mu_2)=\{\pm1\}$-torsor, while a fixed equivalence still has the automorphisms $H^0(\mathbb R,\mu_2)=\{\pm1\}$. The Brauer obstruction itself lies one degree higher in $H^2$, so identifying either sign set with that obstruction would conflate distinct data. This adds a precise bookkeeping rule to the later polarization/real-structure comparison, without rederiving the supplied compact-torus calculation.

## D15 — What Oda actually proves

**Witness:** 15/054, “F-cristal ... de rang $2$”. **Kind:** unpursued implication / precise literature boundary. **Context:** CT 54/003,005,007 and CN D03–D05; same-cote P04, 18/005 and 011, and FR23 in the 087–138 notes, already cite the same result; this restates its verified scope for the present determinant problem. **RS:** MPL_15_195-228+18_002-017 P01 [conjectural-realization first-pass lead]; WG2 §2.4 #3 [unchecked plan], unchanged.

Oda, Corollary 5.11, printed p. 131, canonically identifies the contravariant Dieudonné module $M(E[p])$ with $H^1_{\mathrm{dR}}(E)$ over a perfect field of characteristic $p$, carrying $VM=\ker F$ onto $H^0(E,\Omega^1)$ and matching the Hodge exact sequence [Oda]. This precise theorem was checked on the printed page, not inferred from its title. It does not alone construct the full integral rank-two crystalline determinant normalization or prove its Morita compatibility on scan 054.

## D16 — A geometric route to the determinant orientation, with its remaining comparison

**Witness:** 15/054, “$\operatorname{Isom}(\bigwedge^2 M,T_p)/\mathbb Z_p^{*2}$”. **Kind:** own idea / construction route. **Context:** CT 54/005's exterior-algebra and duality paragraph and CN D02–D05 supply the antecedent; Hua, subsection “« Détermination de $\xi_p$ ? »”, pp. 53–55 (= scans 054–056), restates the determinant target but gives no value. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 P01 [first-pass conjectural programme], unchanged.

Oda, Propositions 3.22–3.24, pp. 99–101, constructs the full Witt-module duality and the Frobenius/Verschiebung-compatible Riemann form associated with a polarization, supplying a stronger candidate input than Corollary 5.11 alone [Oda]. In the cohomological convention where the Tate line has $F=p\sigma$, the rank-two model $Fe_1=e_2$, $Fe_2=-pe_1$ gives $F(e_1\wedge e_2)=p(e_1\wedge e_2)$, an explicit check of the determinant's Tate slope. **Confidence: high** for the matrix calculation and the cited pairing construction, **medium** for its identification with this particular $\xi_p$, because variance, the chosen Tate-line convention, and the global norm/Morita comparison must still be matched.

## D17 — Frobenius descent does not automatically extend to the maximal quadratic order

**Witness:** 15/056, “l'anneau des entiers”; “$F^2+p=0$”. **Kind:** own idea / explicit boundary test. **Context:** Hua, same subsection p. 55 (= scan 056), already flags the distinction from $\mathbb Z[\sqrt{-p}]$; this adds an actual trace-zero example, while CT 54/007 concerns Frobenius kernels and has no order-extension assertion. **RS:** MPL_15_195-228+18_002-017 P01 [first-pass lead]; WG2 §2.4 #3 [unchecked plan], unchanged.

For odd $p\equiv3\pmod4$, the maximal order is $\mathbb Z[(1+\sqrt{-p})/2]$, so the equation alone initially gives the smaller order $\mathbb Z[F]$. For $E/\mathbb F_7:y^2=x^3+x$, direct counting gives $\#E(\mathbb F_7)=8$ and trace zero, but only one nonzero 2-torsion point is rational; consequently $(1+F)/2$ is not an endomorphism, since its existence would force $1+F$ to kill all of $E[2]$. **Confidence: high** for this obstruction to extension of the specified Frobenius embedding: it is an explicit kernel test, not a denial that some unrelated maximal-order embedding might exist. The source's asserted equivalence therefore needs an integrality qualification if $R$ retains its written maximal-order meaning.

## D18 — Invertible-module twists and determinant orientations require the specified order

**Witness:** 15/056, “module inversible $P_0$ sur $R$”. **Kind:** unpursued implication / reading question. **Context:** Hua, same subsection p. 55 (= scan 056), modernizes $R$ to the order generated by the Frobenius root, which differs from the frozen maximal-order wording; same-cote FR04, scan 098, separately warns that norm and ideal-class images can have finite index. **RS:** MPL_15_087-138 FR01/FR08 [first-pass Frobenius/eigenvalue leads, not proofs of this twist classification]; LM6 A.22 [Open, return's claim], unchanged.

Replacing the maximal order by $\mathbb Z[\sqrt{-p}]$ changes the category of invertible modules and the conductor-two local condition, so those two formulations cannot be interchanged without proof. The line $\det_{\mathbb Z}P_0$ is free, but making its isomorphism with $\mathbb Z$ functorial needs an orientation convention; the chosen root can supply one through the complex orientation of the quadratic algebra, which should be stated and checked against the norm convention on scan 054. This identifies concrete comparison data still missing from the unfinished determination of $\xi_p$, rather than declaring that an orientation cannot exist.

## Primary references

- **[Oda]** Tadao Oda, *The first de Rham cohomology group and Dieudonné modules*, Annales scientifiques de l’École Normale Supérieure, series 4, 2 (1969), 63–135, DOI 10.24033/asens.1175. [Primary article](https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf). Corollary 5.11, printed p. 131; Propositions 3.22–3.24, printed pp. 99–101.
- **[Deu]** Max Deuring, *Die Typen der Multiplikatorenringe elliptischer Funktionenkörper*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 14 (1941), 197–272. [Primary article](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1941.Deuring.pdf). Introduction §§2–3, pp. 198–200; §2, nos. 4–10, pp. 212–218.
- **[Voi42]** John Voight, *Quaternion Algebras*, chapter 42, “Supersingular elliptic curves”. [Author edition](https://jvoight.github.io/quat-book.pdf); [publisher chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42). Modern corroborating exposition of the Deuring correspondence and its local quaternion algebra.
- **[Kum]** The Stacks Project, [Lemma 59.28.3, Tag 040N](https://stacks.math.columbia.edu/tag/040N), and [Section 59.28, Tag 03PK](https://stacks.math.columbia.edu/tag/03PK). The fppf Kummer sequence and the distinct étale invertibility hypothesis.
- **[DM12]** P. Deligne and J. S. Milne, *Tannakian Categories* (1982), [corrected author edition dated 15 August 2012](https://www.jmilne.org/math/xnotes/tc2012.pdf). Proposition 5.8 and Appendix, “Gerbes”; original proposition numbering is retained.
