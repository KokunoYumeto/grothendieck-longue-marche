# Research notes: pinned maps, moduli, and the small catalogue

**Run:** MPL_138_090-133/maps_moduli_research. **Author:** GPT-6 Astra Pro; inherited effort unspecified. **Scope:** frozen TeX for scans 98–103 and 114–120 only, with supplied context consulted after the freeze. No scan image was read for this research and no transcription was edited.

Source locations below are local line numbers in pages/MPL_138_090-133_138_scanNNN.tex. “Hua” means **Hua, modernised reading of cote 138**, supplied as context/hua_project/138.modern.tex; its section titles are cited, and its already-existing findings are credited to that project. RESULTS_STATE claims retain their supplied status unless a specific check is recorded here. The full searches and the longer arguments are in maps_moduli_context_search.md and maps_moduli_checks.md; actual events are in maps_moduli_check_events.tsv.

## MM01 — Pinning labels cells with degrees, not incident flags

**Source:** scan 98, lines 6–11, 34–48; “une pré-carte”; “C0 … → Fac(C)”; “Ce foncteur est conservatif,” with the uncertain marginal “fidèle … pour iso.”  
**Kind:** definition-sensitive implication / reading question.  
**Context:** Hua §13.I, “Précartes, et la catégorie des cartes co-épinglées,” lines 1508–1521; RESULTS_STATE: no direct entry on this definition.

The specified data are the three degree-labelled sets S,A,F and an isomorphism to them, without a labelled dart, tangent direction or flag. Conservativity reflects isomorphisms and does not imply faithfulness; MM02 checks the latter independently using the actual cell labels. The margin must therefore remain a reading question rather than supplying an additional rigidity hypothesis.

## MM02 — The unrestricted rigidity claim is false

**Source:** scan 99, line 3, “la catégorie des cartes … orientées C0-épinglées est rigide”; scan 100, line 20, “catégorie est rigide,” margin “vérifier.”  
**Kind:** unproved claim, refuted by a targeted check of an existing context counterexample.  
**Context:** Hua §13.I, lines 1525–1533, already gives the one-vertex, two-edge, one-face torus half-turn; RESULTS_STATE: no direct entry, and **LM4 C.12** is a different, still-open infinite-operator comparison.

For r=(1234), σ=(13)(24), ρ_f=r, the map is connected of genus one and the nonidentity r² fixes each vertex, edge and face individually while preserving orientation. **Refinement MM02R:** the pinned automorphism group is the kernel of Aut(C)→Aut(Fac(C)), which in this example is C2, not 1. This verifies Hua's counterexample against the precise precarte definition; proof and exact permutations are in checks P1–P2 and maps_moduli_certificate.json.

## MM03 — The counting formula needs orbit sizes

**Source:** scan 99, lines 7–11, “classes d'iso … multiplié par le cardinal du groupe des autom. de C0”; displayed product of factorials.  
**Kind:** unproved count, refuted as an ordinary unweighted count and refined.  
**Context:** Hua §13.I, lines 1534–1546, already identifies the omitted automorphism denominator and the cubic-star test; RESULTS_STATE: no direct entry.

With K_C=ker(Aut(C)→Aut(Fac(C))), **MM03R** is the ordinary count Σ_[C] |Aut(C0)|·|K_C|/|Aut(C)|, whereas Σ_[C]|Aut(C0)|/|Aut(C)| is the groupoid mass. For the cubic star the ordinary count is 6/3=2, not 6; for the torus it is 2·2/4=1, with residual automorphism group C2. The factorial product for |Aut(C0)| is correct; the distinction is which quotient and weighting are being counted (checks P3).

## MM04 — Genus-zero geometric rigidity does survive

**Source:** scan 99, line 3, “orientées … est rigide,” tested on the spherical cases later catalogued.  
**Kind:** targeted proof check of Hua's qualification.  
**Context:** Hua §13.I, lines 1525–1533; RESULTS_STATE: no direct entry.

Over C, a pinned genus-zero cover has an automorphism of P1 fixing at least one labelled point in each of the disjoint fibres above 0,1,∞, hence fixing three distinct points and therefore equal to the identity. This proves the genus-zero qualification made by Hua without using the footnote's ordinary-edge inequality V+F≥3, which needs care because q=1 folded edges are allowed. It proves geometric rigidity, not the complete relative representability statement (checks P4).

## MM05 — Explicit étale-local failure of the raw moduli functor

**Source:** scan 100, lines 11–17, reduced-fibre identifications; line 21, “un foncteur … qui est représentable.”  
**Kind:** own idea, explicit counterexample to the stated fine functor; confidence high because the field and ramification calculations are exact and independently checked.  
**Context:** Hua §13.II–III, “Le schéma de modules, et l'action de Galois,” lines 1554–1574, already warns of nonrepresentability; LM_140-2_text.tex, scan 547, line 15778, and LM_140-3_text.tex, scans 180–181, lines 7891–7898, discuss the C2-gerbe and quadratic-twist ambiguity; supplied LM_140-3_notes.md, note C3 for scans 180–181, already relates the Legendre curve to y²=x³−x; RESULTS_STATE: no direct entry.

Take the two covers E_d: d y²=x³−x, f=x², d=1,2, and pin the points over 0, the ordered pair (1,0),(−1,0) over 1, and O over ∞. They have passport (4)|(2,2)|(4), become isomorphic as pinned covers over Q(√2), but are not isomorphic over Q because the labels force x↦x and 2 is not a square in Q(x). **MM05R:** the raw isomorphism-class presheaf is not étale-separated, so it cannot be represented by a scheme; this explicit descent obstruction sharpens the context's automorphism warning without confusing it with a coarse geometric-class space (checks P5).

## MM06 — Relabelling stabilizers see an effective quotient

**Source:** scan 101, line 8, “Le stabilisateur … correspond … aux autom du … rev.” and “si f est galoisien … au groupe de Galois de f.”  
**Kind:** unproved claim, false without a faithful pinning action; refined.  
**Context:** Hua §13.II–III, lines 1575–1577, repeats the stabilizer identification; LM_140-2_text.tex, scans 547–548, lines 15787–15795, distinguishes a group from its effective quotient; RESULTS_STATE: no direct entry.

For geometric isomorphism classes, **MM06R** is Stab_γ([C,u])≅Aut(C)/K_C, with K_C as in MM03. In the regular torus example Aut(C)=C4, but the relabelling stabilizer is C2. Thus identifying this stabilizer with the full deck group requires precisely the faithful pinning condition that fails in MM02; relative sections may require additional descent hypotheses (checks P3).

## MM07 — The prime bound has a valid source, with a narrower conclusion

**Source:** scan 100, line 21, “fini … Z[1/δ!]”; scan 101, line 3, “non ramifié en les p>δ.”  
**Kind:** unproved arithmetic claim; numerical implication and reference scope checked.  
**Context:** Hua §13.II–III, lines 1565–1574, gives the monodromy-order explanation and cites Fulton; RESULTS_STATE: no direct entry; **EXIT_TOWER E.24** remains open and is not solved by this prime bound.

For a faithful degree-δ monodromy action, G⊂S_δ implies |G| divides δ!, so p>δ is prime to |G|. SGA 1, Exposé XIII, Corollary 2.9 and Lemma 2.11 supply the relevant prime-to-characteristic specialization and inertia framework for the smooth pair (P1,{0,1,∞}); they support the finite geometric-class formulation, while the raw fine functor remains refuted by MM05. No proof of every asserted property of M_C0 over all of Z is claimed, and Fulton's cited paper was checked bibliographically rather than used as a theorem for this exact functor (checks P6 and primary-reference list).

## MM08 — Group-type strata should first be read on geometric classes

**Source:** scans 101, line 10, and 102, line 3, “groupe de Galois … de type α” and “sous-schéma ouvert et fermé.”  
**Kind:** conditional implication, with the representability premise separated.  
**Context:** Hua §13.II–III, lines 1579–1582; RESULTS_STATE: no direct entry; **EXIT_TOWER E.24** is related only through finite Galois actions.

On a finite Γ_Q-set of geometric cover classes, the locus with a fixed abstract geometric Galois-closure group is Γ_Q-stable, since conjugating coefficients transports the cover and its automorphisms. Such a subset corresponds to an open-and-closed finite étale Q-subscheme by the finite-Galois-set equivalence. This validates the formal characteristic-zero partition once that class space is supplied, but does not prove the stated all-base representability of the original presheaf or local constancy for arbitrary families (checks P6).

## MM09 — The core-free criterion is exact in the connected case

**Source:** scan 102, line 5, “∩ conjugués de H={e}” and “E=G/H”; divisibility by p(s),q(s),r(s),δ.  
**Kind:** targeted proof check, with the necessary transitivity hypothesis stated.  
**Context:** Hua §13.II–III, lines 1582–1589; RESULTS_STATE **WG H5** is an unchecked hunch about finite Nielsen classes, not a proof of this criterion or its arithmetic consequences.

A transitive G-set is G/H and its action kernel is core_G(H), so core-freeness is precisely faithfulness; conversely a generating triple with ρ_sρ_fσ=1 and σ²=1 gives the desired map when its three cycle partitions match C0. Then δ=[G:H] and every listed cycle length divides |G|, giving the stated necessary divisibilities. The G/H formulation and degree divisibility require connectedness/transitivity; disconnected covers need several orbits, and these pages do not themselves spell out that hypothesis (checks P7).

## MM10 — Does the cover fail to determine its generator-marked group?

**Source:** scan 102, line 5, “la classe d'isom. de G muni de ρ_s,ρ_f,σ … n'est pas déterminée … X→P1_C.”  
**Kind:** reading question / apparently incompatible claim under the usual fixed-target interpretation.  
**Context:** Hua §13.II–III, lines 1589–1596, already flags this sentence as unreconstructed; RESULTS_STATE: no direct entry; **WG H5** concerns generating pairs modulo inner automorphisms but does not resolve this reading.

A fixed complex cover determines f^(-1)([0,1]) with its complex orientation and hence its oriented map type. Choosing standard target loops and a fibre labelling determines the monodromy generators up to simultaneous conjugacy; actual named elements in a separately chosen abstract group involve further choices. This distinguishes a choice-dependent presentation from the map's isomorphism class, so the manuscript's parenthetical identification appears problematic, but no alternative reading is imposed (checks P7).

## MM11 — The finite Galois-set conclusion has an independent formal meaning

**Source:** scan 103, lines 3–6, “M(Qbar)≃M(C)” and the knowledge of the Γ-set determines the Q-scheme, with Γ “commutant” with γ.  
**Kind:** targeted proof check of a conditional formal conclusion.  
**Context:** Hua §13.II–III, lines 1598–1610; RESULTS_STATE **EXIT_TOWER E.24** remains an open arithmetic-image problem, while **MPL_147_003-047 N075** warns that boundary compatibility is stronger than isolated group actions.

For a finite étale Q-algebra R, every homomorphism R→C lands in Qbar, and its finite continuous Γ_Q-set of geometric points determines R by Galois descent. The constant label permutations γ commute with Γ_Q, so this finite action makes sense even when the original raw fine functor is replaced by a suitable geometric-class space. It does not determine the full arithmetic image in a tower, supply boundary compatibilities, or recover an integral model without the extra unramified condition (checks P6; Stacks Project, tag 03QR).

## MM12 — Complex conjugation: possibility, not a universal nontriviality claim

**Source:** scan 103, line 8, “peut ne pas être triviale”; line 10, action of γ×Γ in elementary spherical cases.  
**Kind:** reading comparison and targeted example.  
**Context:** Hua §13.II–III, lines 1607–1614, correctly relates conjugation to mirrors, but its footnote quotes “ne peut pas être triviale”; RESULTS_STATE **LM4 D.12** remains open beyond these finite examples.

The frozen wording asserts that the action can be nontrivial, not that it must always be nontrivial, so Hua's quoted wording and corrective footnote should not override it. The degree-five chiral pair in MM14 supplies an explicit case in which complex conjugation exchanges two oriented classes after quotienting by the pins. This is a finite dessin test, not a classification of torsion in the full profinite groups (checks P8).

## MM13 — The catalogue's group labels include reversing symmetries

**Source:** scan 115, lines 5–7, “Z2” with type (1,1,1); lines 28–34, “S3” for (3;1,1,1;3) and “Z2” for (3;2,1;2,1).  
**Kind:** targeted check of Hua's interpretation.  
**Context:** Hua §14, “Cartes sphériques en bas degrés,” lines 1693–1702; RESULTS_STATE: no direct entry.

The degree-one map has trivial monodromy, so its Z2 label cannot denote monodromy. The cubic star has monodromy C3 and full combinatorial symmetry S3, whereas the cubic loop-tail has monodromy S3 and full combinatorial symmetry C2, exactly matching the catalogue labels. These diagnostic computations support Hua's interpretation as finite combinatorial automorphisms including orientation reversal, with isotopies forgotten; no claim is made that every group label on scans 114–120 has been verified (checks P8 and certificate).

## MM14 — The degree-five “rigide” map is chiral

**Source:** scan 116, lines 28–30, group “1” and passport (4,1)|(2,2,1)|(4,1); scan 118, line 10, boxed “rigide.”  
**Kind:** own targeted computation; confidence high for the passport, moderate for identifying every figure solely from the frozen TeX.
**Context:** Hua §14, lines 1707–1713, notes “rigide” without a class-by-class check; RESULTS_STATE **LM4 D.12** is only a broader open comparison.

Exhaustive permutation enumeration for this one passport gives exactly two oriented classes, exchanged by reflection, each with trivial full automorphism group and monodromy order 20. Thus the stated group 1 and the live degree-five rigidity mark are consistent with chirality, not with trivial monodromy. Hua's mention of a first degree-four “rigide” needs its cancellation status retained: frozen scan 114 places that doubtful word inside the deleted block at lines 74–80 (checks P8–P9).

## MM15 — A repeated passport can encode distinct maps

**Source:** scan 117, line 7, the repeated (6)|(2,2,1,1)|(3,2,1), grouped under “!”.  
**Kind:** own targeted computation; confidence high for the finite classification, cautious about the author's intention.
**Context:** Hua §14, lines 1710–1713, notes the repeated type but does not verify the catalogue; RESULTS_STATE: no direct entry.

This passport has three oriented classes: one reflexible map and one chiral pair, all with monodromy S6 and trivial oriented automorphism group. Consequently it has two classes when orientation is forgotten, so two occurrences of the passport need not be a copying error. The separate arithmetic calculation and the already-known example in Gareth A. Jones, “Regular dessins with a given automorphism group,” Example 7.7, printed page 12, corroborate this triple for the dual passport; identifying each particular drawing or explaining the exclamation mark remains outside this check (checks P8; arithmetic_research.md AR13–AR14; https://arxiv.org/pdf/1309.5219).

## MM16 — Both “impossible” annotations have a short proof

**Source:** scan 118, line 18, four vertices with degrees (2,1,1,1), “impossible”; scan 120, lines 17–18, five vertices with degrees (2,1,1,1,1), “impossible.”  
**Kind:** targeted proof check of an existing context observation.
**Context:** Hua §14, lines 1704–1706, already gives the spanning-tree bound; RESULTS_STATE: no direct entry.

A connected map with V vertices needs at least V−1 complete edges joining vertices, hence at least 2(V−1) darts; q=1 half edges do not connect two different vertices. The two cases would require respectively 5≥6 and 6≥8, which are false. This confirms the annotations without enumerating the remaining catalogue (checks P9).

## MM17 — A degree-six heading is numerically inconsistent as frozen

**Source:** scan 120, line 3, “1 sommet d’ordre 3, 1 d’ordre 2, 1 d’ordre 2,” against the (3,2,1) marginal passports at line 5.  
**Kind:** reading question supported by an arithmetic inconsistency.
**Context:** Hua §14, lines 1693–1695 and 1711–1713, describes the degree-at-most-six catalogue and cautions about overwritten types; RESULTS_STATE: no direct entry.

The heading's stated degrees sum to 7, whereas the marginal list sums to 6. The degree condition therefore identifies a local incompatibility, but it does not by itself license changing the final 2 to 1 in a diplomatic transcription. The frozen reading is preserved (checks P9).

## Check summary and limits

The exact computation record is maps_moduli_certificate.json, reproducible with check_maps_moduli.py; all 44 frozen source hashes matched before and after that run. The concrete fine-moduli obstruction was also reviewed by the arithmetic agent. The all-characteristic relative moduli theorem, a full catalogue enumeration, the global Galois image and the cited open RESULTS_STATE entries remain unproved here.
