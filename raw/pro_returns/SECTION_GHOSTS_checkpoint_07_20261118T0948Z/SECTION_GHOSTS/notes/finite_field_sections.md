# Fixed-prime finite-field section comparison: research and E.150

Date: 18 November 2026. Author: literature agent. Parent owns assembly and saving.

## Established finding

Hoshi (2009), *Absolute Anabelian Cuspidalizations of Configuration Spaces of Proper Hyperbolic Curves over Finite Fields*, Publications of the Research Institute for Mathematical Sciences 45(3), 661–744, DOI 10.2977/PRIMS/1249478963, Remark 10(i), printed pp.742–743, records Tamagawa's counterexample to injectivity of rational-point sections in a fixed full geometric pro-l quotient of a proper hyperbolic curve over a finite field. This is an actual full pro-l counterexample, not just an abelian countermodel. Its mechanism is the prime-to-l arithmetic factor that centralizes the geometric pro-l group after suitable finite base change.

E.150 independently proves the corresponding assertion for the tripod using its unit tangential splitting. For K=F_q, e=ord(q mod3), and L=F_{q^d}, gcd(d,3e)=1 implies that the action images of G_K and G_L on the same free pro3 group F coincide. The image Gamma is procyclic with a pro3 subgroup of index e: the based Frattini action is the scalar q, and the IA automorphism kernel is pro3. Choose a in G_L with the same action as Frobenius sigma. Then tau(a) and tau(sigma) differ by an element central in F semidirect G_K. Their conjugations agree, so two points in one Gal(L/K)-orbit have sections conjugate inside Pi_L. Crucially, h=tau(a)s_x(a)^{-1} lies in F and gives the same conjugation, because s_x(G_L) is abelian. This proves the required *geometric* conjugacy of full sections.

Two explicit fields and point orbits:

1. K=F25, L=F5[alpha]/(alpha^4+2)=F625. The quartic is irreducible, alpha^25=-alpha, and alpha,-alpha are distinct interior points with equal pro3 section classes.
2. K=F5, L=F5[beta]/(beta^5-beta-1)=F3125. The Artin–Schreier polynomial is irreducible; beta^{5^j}=beta+j. Its five distinct interior roots have equal pro3 section classes. Here #L is -1 modulo3.

The independent finite script `code/check_finite_field_sections.py` proves the two polynomial irreducibility certificates by exact finite polynomial arithmetic and checks the stated Frobenius orbits. Its JSON records PASS. The script does not certify the infinite group argument; that proof is written in full in E.150.

## Exact limitations

- The geometric quotient F is held fixed under base change. These are failures of injection in full geometric pro3, not merely some finite nilpotent layer.
- The fields in these examples have non-prime cardinality. No prime-field example is claimed.
- Galois preserves the boundary, so the orbit argument never changes an interior point into a tangential cusp. It neither proves nor disproves the point-versus-tangent separation required by E.135.
- Distinct points inducing the same section are compatible with Hoshi's Frobenius-preserving isomorphism theorems: preserving the set of point-section classes is weaker than injectively indexing the classes by points.
- These examples provide no locally ordinary completed pair over Q and resolve no main global question.

## Primary sources opened and exact locators

### Hoshi 2009 — used in E.150

- Published primary PDF: https://www.kurims.kyoto-u.ac.jp/~prims/pdf/45-3/45-3-19.pdf . Open ref `turn111146638view0`; exact Remark10 text refs `turn598887429view0` and `turn598887429view1`.
- Publisher metadata: https://ems.press/journals/prims/articles/3938 . Open ref `turn720027641view0`. It verifies author, title, volume45, issue3, pages661–744, 30September2009 and DOI.
- Remark10(i), pp742–743: explicit interior/interior counterexample for proper hyperbolic curves, using almost-pro-l outer automorphism group and a prime-to-l extension with new points.
- Theorem0.1, pp662–663: Frobenius-preserving isomorphism of proper-curve geometric pro-l groups reconstructs configuration groups.
- Proposition2.5(ii) and proof, pp696–697: such isomorphisms preserve point-section classes; no claim of pointwise injectivity.

### Mochizuki cuspidalization — scope check only

Primary author LaTex version: https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(LaTeX%20version).pdf . Open ref `turn300428320view0`, later exact opens `turn878236346view1`, `turn878236346view2`, `turn878236346view3`.

- Definition1.5, printed p31, defines Sigma-separated using injectivity of decomposition groups after every finite cover.
- Remark10, p32, explicitly distinguishes quasi-point-theoreticity from pointwise separation. It does not assert arbitrary singleton-Sigma separation.
- Theorem3.1, pp80–81, reconstructs maximal cuspidally pro-l extensions from a Frobenius-preserving isomorphism of proper-curve groups that already matches the chosen decomposition groups. This is not a criterion separating one point section from one tangential section.
- Corollary3.1, p85, explicitly assumes all characteristic-invertible primes and Sigma-separatedness.
- Original published pagination differs; only this author version's printed locators are used in this research log. No new formal bibliography/theorem use is needed for the scope check unless parent decides to include it.

### Stix Chapter15 and erratum — access limitation

- Existing `LitStix2013` entry remains metadata-only; the relevant chapter is Sections over Finite Fields, pp197–205, with §15.4 pp204–205.
- Publisher chapter PDF https://link.springer.com/content/pdf/10.1007/978-3-642-30674-7_15.pdf was inaccessible (`turn428179847view0`). An author-path guess was inaccessible (`turn428179847view1`); it is not treated as a valid source URL.
- The SciSpace PDF https://scispace.com/pdf/rational-points-and-arithmetic-of-fundamental-groups-34z8wqgcxg.pdf was opened (`turn483958550view1`) but consists of only20 preliminary pages, not Chapter15.
- A search-indexed full-book mirror at nzdr.ru timed out via web open (`turn878236346view0`); direct urllib request returned404. No unobserved theorem from it is used.
- Author erratum https://www.math.uni-frankfurt.de/~stix/research/preprints/STIX-Evidence%20for%20SC-Erratum.pdf opened (`turn483958550view0`), dated4December2017,3pages. It corrects §15.2's counts of curves filling their Jacobians and states that only two genus2 curves overF2 remain. This is a correction to the Jacobian counting argument, not a fixed-pro3 point/cusp separation theorem.

## Search log and discarded directions

Primary searches included: finite fields pro-l section injectivity; finite fields pro-ell Kummer map; finite fields cuspidal section injective; finite field section map injective; finite field tangential section point; pro-l point-theoretic; finite field pro-l separated Tamagawa. The last led to Hoshi2009 Remark10 and the explicit counterexample.

No proof uses machine-generated survey pages returned by broad searches. Bibliographic aggregators were used only to locate originals. No statement is inferred from a table of contents.

The stronger point/cusp question remains under active investigation. Whole cusp decomposition-group separation is insufficient, because an interior Galois section could in principle be a Frobenius complement inside a larger cusp decomposition group without equality or commensurability of the whole groups. An applicable theorem would need to exclude that containment, with singleton coefficient set {3}, not merely distinguish the full groups.

## Exact containment check after E.150

Primary Saidi–Tamagawa2009 PDF https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/publRIMS.pdf independently reopened (`turn532967915view0`, exact `turn135951463view0` and `turn135951463view1`). Proposition1.8(ii), printed pp144–145, excludes commensurability of the *whole* cusp and interior decomposition groups; its proof uses their different geometric inertia intersections. It does not exclude containment of an interior decomposition group as a complement in a cusp decomposition group. Lemma1.7, p144, controls the commensurator of a subgroup mapping injectively onto an open arithmetic subgroup. Cofiniteness of Sigma first enters Proposition1.8(vi), to make the exceptional set finite; it is absent from the earlier commensurability assertion. Corollary1.12(ii), pp148–149, controls the normalizer of cusp inertia, not normalizers of its Frobenius complements.

An elementary consistency check explains why the quasi-section lemma supplies no contradiction: in Z3(1) semidirect G_Fq, a Frobenius complement Z has geometric centralizer zero, since q^m-1 acts injectively on Z3 for every positive m. Thus Z may satisfy the lemma while lying in the larger cusp group. Whether such a complement is also the decomposition group of an interior point is additional geometry.

The exact no-containment assertion does occur in Mochizuki, *Galois Sections in Absolute Anabelian Geometry*, Theorem1.3(iv), author p6, primary https://www.kurims.kyoto-u.ac.jp/~motizuki/Galois%20Sections.pdf (`turn532967915view1`, exact `turn135951463view2`). But §0, author p2, and the opening of §1, p4, restrict the fields to finite extensions of Q_p, and the fundamental groups are full profinite. The proof first passes to a cover with hyperbolic proper compactification, then invokes point determination there. It is not a theorem for a singleton-prime geometric quotient over a finite field. In particular, E.150 disallows importing an unrestricted fixed-pro3 proper-point injection as a substitute.

The author publications page https://www.math.uni-frankfurt.de/~stix/publikationen.html was opened (`turn586480657view0`). Its Habilitationsschrift entry links the Springer book and erratum, with no accessible full thesis PDF in that entry. Chapter15 remains unread; no claim is based on its unseen text.
