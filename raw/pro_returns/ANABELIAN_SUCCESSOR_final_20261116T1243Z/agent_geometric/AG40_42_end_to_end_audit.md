# AG40–AG42: complete separation-chain audit

Date: 2026-11-16. Status: all three claims integrated and independently approved. The parent owns the main A1 statement and its consequences.

## Exact final labels and retained sources

- AG.40, label `clm:AGcuspidalcriterion`, equations AG.40.1–7: `cuspidal_conditional_separation_draft.tex` (the historical filename is retained). This proves that an actual cusp-compatible maximal cuspidally pro-r isomorphism over the identity full proper geometric prime-to-p group forces equality of the punctures.
- AG.41, label `clm:AGfixedrconfiguration`, equations AG.41.1–14: `fixed_prime_configuration_exactness.tex`. This proves fixed-r relative configuration fiber exactness, cofinal finite-quotient detection, prime-to-p specialization, and the arithmetic pullback over the actual point section.
- AG.42, label `clm:AGcuspidaltransport`, equations AG.42.1–6: `cuspidal_boundary_transport.tex`. This proves the arithmetic diagonal boundary sequence, the actual puncture-intersection identification, and the construction of the cusp-compatible isomorphism from geometrically conjugate proper point sections. It then applies AG.40 to prove equality of those points, over every finite extension of the constant field.

All three occur once in `geometric_section.tex`. `AG40_claim_delta.csv` and `AG41_AG42_claim_delta.csv` record current scope. The original authoring drafts in agent_F and the independent cusp-module proof in agent_criteria are retained rather than overwritten.

## AG41 finite-cover audit

The discrete fibration has free fiber and aspherical compact base. After a proper finite Galois cover C′→C, the total cover is C′×C′ minus the disjoint deck graphs. The compact family is constant and its punctures are individually labeled. Thus mod-r monodromy is a finite r-group of shears, without a section assumption. The elementary finite Frattini automorphism argument makes the closure of the full action on the free pro-r fiber a pro-r group. Center-freeness of that fiber makes its inner action faithful, proving injection into the pro-r completion of the total group.

For an arbitrary finite quotient of the relative fiber, the proper quotient supplies the cover C′. The remaining fiber image is an r-group. A finite r-quotient of the total cover dominates it on the fiber. Its normal core in the original configuration group has r-group kernel and proper prime-to-p quotient A×A. Consequently it factors through the actual global cuspidally pro-r quotient. No arbitrary finite quotient is assumed to extend identically; domination of its kernel is sufficient and explicitly proved. Right exactness gives the remaining exact sequence. This avoids the invalid full prime-to-p fiber assertion excluded by AG39.

The geometric specialization uses the smooth proper pairs (C,P) and (C×C,diagonal), not a direct characteristic-p Hodge argument. Their prime-to-p comparisons are functorial for the fiber map and identify the characteristic relative quotients. The arithmetic comparison is an isomorphism on geometric kernels and the identity on the full constant-field Galois quotient.

## AG42 boundary audit

The root stacks of the smooth diagonal and their reduced boundary root gerbes explicitly encode tame boundary covers. A geometrically prime-to-p finite cover has tame boundary inertia; taking a root order divisible by its inertia order gives a unique finite étale extension on each whole Kummer chart. Uniqueness gives descent and compatibility. The resulting boundary homomorphism is to the tame fundamental group, then to the geometrically prime-to-p quotient; it is not asserted to encode wildly ramified covers.

For each root gerbe, quotienting its fundamental group by the stabilizer image gives the full base group. The compatible transitions are surjective. Passing to the inverse limit therefore gives exactly the inertia image as kernel. Right exactness is then applied to geometric groups, while the full G_k quotient is retained. There is no extra image of the discarded geometric base kernel. The global relative quotient makes inertia pro-r. Its full Z_r(1) survives because the fiber injects and the puncture commutator word maps to an infinite central element in the pro-r Heisenberg group.

The transverse fiber meets the diagonal with multiplicity one, so the puncture inertia is the same oriented inertia. Its actual decomposition subgroup maps isomorphically on this inertia and on the actual proper point section. It is therefore the full intersection with the diagonal boundary group. A diagonal lift of a geometric proper conjugator transports both fiber and cusp; a geometric element in the target fiber corrects the remaining inner proper action. This produces exactly the isomorphism required by AG40.

## AG40 adversarial downstream audit

The core lemma AG.39.15 applies to every open subgroup, not merely normal or r-group-index opens. It preserves the full compactified pro-r group and arithmetic Frobenius. The transported cusp decomposition groups preserve missing-point counts, so all visible open covers have the same rational-point counts. Finite-set compactness over nonnormal open neighborhoods of a point section identifies an actual target section. The universal-cover wording now explicitly refers to the pro-cover defined by G_Q.

Outside the known finite exceptional set, the identity proper quotient forces the point label to be unchanged. The direct Kummer cycle-class construction gives both one-cusp central extensions with degree-one class; hence the kernel multiplier is one. Their difference cocycle has residues (+1,−1). Subtracting its p^e multiple from the Kummer class of a function with divisor p^e(P−Q) leaves a proper H¹ class, hence a constant. The proper section self-normalizer removes the projected conjugator, making evaluation of the difference cocycle a coboundary. A nontrivial r-power root of unity in a finite residue field has nonzero full r-adic Kummer class. This supplies the final contradiction.

## Exact primary inputs freshly checked

1. SGA1 XIII Proposition 5.2, printed pp.428–429, attached primary TeX `background/literature/SGA1/src_arXiv_math_0206203/smf_doc-math_3_01.tex`, statement beginning at line25272. It assumes a regular local scheme and normal-crossing divisor, with a cover tame relative to that divisor. It explicitly concludes unique extension over the entire Kummer chart. Its proof includes purity, citing SGA2 XIV1.11. The use here has a smooth surface and one smooth divisor, and all inertia orders are prime to the characteristic. Root, F, and this agent independently read the statement and proof.
2. SGA1 XIII Corollary2.9 and Section2.10 were already independently checked for the proper-pair prime-to-p specialization used in AG39; AG41 uses that same exact statement and functorial diagram.
3. Kochloukova–Zalesskii, arXiv1107.2331, primary author PDF https://arxiv.org/pdf/1107.2331 , Theorem5.1 proof Case I, printedp7, and Corollary5.3, printedp8. Freshly opened here as turn594view0 and turn595view1. The free finite-rank pro-r case explicitly has procyclic centralizers of nontrivial elements and therefore trivial center in rank at least two. The existing verified bibliography key is FF_KochloukovaZalesskii2011.
4. The elementary finite Frattini automorphism bound is proved in full, by its free action on ordered generating tuples lifting a fixed Frattini basis. No unverified general automorphism theorem is substituted.

## Independent review record and source-scope corrections

Root, criteria, and this agent independently read and approved AG41 and the entire boundary proof. F independently re-audited every downstream step of AG40 after the geometric proof was complete and reported approval. Root authorized integration and the unconditional point-equality consequence. The audit corrections were: specify the tame target of the boundary map; explicitly retain G_k during geometric completion; identify the universal G_Q-cover in the point-recognition argument; and preserve the arithmetic-to-geometric conjugator adjustment.

The earlier source-convention discrepancy concerning full prime-to-p configuration exactness remains recorded in `cuspidal_green_research.md`. Neither that assertion nor an exceptional-coordinate application of the separatedness-dependent literature comparison is an input to this proof. AG39 and AG41 are compatible: the full prime-to-p fiber can fail to inject, while its one-prime relative cuspidal quotient injects.

No numerical experiment is presented as proof of these infinite group statements. The argument is by finite-quotient cofinality and exact tame descent. All prior finite program certificates remain preserved for the separate computational claims.

Root additionally requested the direct geometric orientation check in AG40. It is now included: the punctured surface relation makes the cusp a central generator after geometric centralization; the Heisenberg specialization gives infinite r-adic order, and the relator has degree one. This complements, rather than replaces, the arithmetic Kummer cycle-class construction and introduces no configuration exactness assumption.
