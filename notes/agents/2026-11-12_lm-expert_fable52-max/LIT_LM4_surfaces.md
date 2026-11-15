# Literature for the surface-topology findings behind LM4 (F1, F2, F9, F10, F11)

Author: Claude Fable 5.2, effort max (fork A of the LM expert successor). Written 12 Nov 2026, 13:10–13:28 UTC (clock read).
Scope: the classical theorems named in `FINDINGS.md` (F1, F2, F9, F10, F11) and in the N-remarks of
`GROTHENDIECK_NOTES.md` on §§12, 15, 17, 18, 19, 24, 28, 31, 33. Every statement under "Quoted" was read by me in the
copy named; "from memory" marks what I could not read in a freely accessible copy. Local copies are under
`C:\Users\user\Documents\Free or receipted\free\lm-expert-20261112\<folder>\`; the download log is
`LM_EXPERT\work\lit\downloads_A.jsonl` (21 files: path, bytes, SHA-256, title, URL). Scans are cited as cote:scan.
The files are not yet entered in `free\CLAUDE_FREE_SHELF.json`.

Not obtained (paywalled, or the host refuses automated access; nothing was bypassed): Kerckhoff, Ann. of Math. 117
(1983); Birman–Hilden, Ann. of Math. 97 (1973); MacLachlan–Harvey, Proc. LMS 30 (1975); Hamstrom, Illinois J. Math. 10
(1966) and Earle–Eells, Earle–Schatz, Wolpert in J. Differential Geom. (Project Euclid answers with a bot check);
Birman–Lubotzky–McCarthy, Duke 50 (1983); Stallings, Ann. of Math. 88 (1968); Bieri–Eckmann, JPAA 13 (1978);
Zieschang, LNM 875; Zieschang–Vogt–Coldewey, LNM 835; Macbeath, Canad. J. Math. 19 (1967) (HTTP 403); Farb–Margalit,
*A Primer on Mapping Class Groups* (no copy on an author's or publisher's free page found); Herfort–Ribes, J. reine
angew. Math. 358 (1985) (not tried here). For each, the statement below is taken from a free text that quotes it, and
is marked. URLs tried without success: `https://projecteuclid.org/journalArticle/Download?urlId=10.4310%2Fjdg%2F1214428816`
(bot check); `https://cms.math.ca/cjm/v19/cjm1967v19.1192-1205.pdf` (403);
`https://www.intlpress.com/site/pub/files/_fulltext/journals/jdg/1969/0003/0001/JDG-1969-0003-0001-a003.pdf` and the
1987 analogue (404, guessed paths). JSTOR, Wiley, Duke and Springer items were not requested.

---

## 1. Kerékjártó–Brouwer–Eilenberg: periodic homeomorphisms of the disc, the plane, the sphere

**Source read.** A. Constantin, B. Kolev, *The theorem of Kerékjártó on periodic homeomorphisms of the disc and the
sphere*, Enseign. Math. (2) 40 (1994) 193–204; arXiv:math/0303256v1 (`constantin-kolev-kerekjarto\`). B. Kolev, *Note
sur les sous-groupes compacts d'homéomorphismes de la sphère*, Enseign. Math. 52 (2006); arXiv:math/0304106v3
(`kolev-compact-subgroups-sphere\`; text layer unusable, page 1 read as an image).

**Quoted (Constantin–Kolev).**
- Lemma 2.5: "Let f : S → S be a periodic homeomorphism of an arbitrary 2-dimensional topological manifold S and let
  x ∈ Fix(f), a fixed point of f. Then for any neighbourhood N of x, there exists a topological disc Δ_x such that:
  (1) Δ_x ⊂ N, (2) Δ_x is a neighbourhood of x, (3) f(Δ_x) = Δ_x."
- Theorem 3.1: "Let f : D² → D² be a periodic homeomorphism. Then there exists r ∈ O(2) and a homeomorphism
  h : D² → D² such that f = h r h⁻¹." Proposition 3.2: a periodic homeomorphism of D² that is the identity on ∂D² is
  the identity.
- Theorem 4.1: "Let f : S² → S² be a periodic homeomorphism. Then there exists r ∈ O(3) and a homeomorphism
  h : S² → S² such that f = h r h⁻¹."
- Corollary 4.2: "Let f : R² → R² be a periodic homeomorphism. Then f is topologically conjugate to a finite order
  rotation around the origin or to the reflection about the x-axis."
- Remark 3.4 (annulus) and Remark 4.3 (positive genus: Kerékjártó and Nielsen, "a periodic homeomorphism of a
  Riemannian surface of positive genus is conjugate to a conformal isometry") are stated without proof.
- History (their introduction): Kerékjártó 1919 (sketch, with a gap), Brouwer 1919, complete proof Eilenberg 1934.

**Quoted (Kolev, résumé).** "tout sous-groupe compact d'homéomorphismes de la sphère est topologiquement conjugué à un
sous-groupe fermé du groupe orthogonal O(3)."

**Hypotheses.** Topological category, no smoothness; orientation-reversing maps included; single periodic maps in
Constantin–Kolev, arbitrary compact (so finite) groups in Kolev, for S² only.

**Bears on.**
- 2:sc146–147, the lemma he leaves ("Soit u un homéomorphisme d'ordre fini de C, commutant à z ↦ z+1, et laissant
  invariant l'origine. Alors u = id ... On doit pouvoir terminer par la suite spectrale d'Adams"). As written, with no
  orientation hypothesis, it is false: u(z) = z̄ has order 2, commutes with z ↦ z+1 and fixes 0. In his context
  (Γ = Γ⁰, orientation preserved) it follows from Corollary 4.2: u is conjugate to a rotation of finite order, which
  has one fixed point unless it is the identity, and u fixes every point of Z ⊂ C.
- 2:sc148 (margin) and the admitted lemma of 2:sc440 (an involutive anti-automorphism of D is conjugate to z ↦ z̄, so
  D^τ ≅ R): Corollary 4.2 for the plane, Theorem 3.1 for the closed disc; locally at a fixed point of an
  anti-involution of any surface: Lemma 2.5 followed by Theorem 3.1.
- "Lemme fondamental", parts (a), (b) (2:sc141–148: a finite Γ acting faithfully on D ≅ R² with Γ⁰ ≠ 1 has one fixed
  point, Γ⁰ is cyclic, Γ dihedral if Γ ≠ Γ⁰, and the action is conjugate to the standard one): extend the action to
  S² = R² ∪ {∞}; by Kolev's theorem it is conjugate to a finite subgroup of O(3) fixing a point p, that is, to a
  finite subgroup of O(2) acting linearly on S² ∖ {p} ≅ R². This gives the whole lemma for topological actions, with
  no induction on the order.
- F1 step (i) and the N-remark on §15.

**Verdict.** Confirms the N-remark on §15 and F1's first cited fact. One correction to F1 step (i): local linearity
is needed for the stabilizer *groups* (cyclic or dihedral), not only for single periodic maps; Constantin–Kolev's
Lemma 2.5 and Theorem 3.1 give the cyclic case, the group case is Kolev's theorem (apply the proof of Lemma 2.5 to
the finite group to get an invariant disc, then Kolev on its one-point-compactified interior). His lemma of
2:sc146–147 needs the words "preserving the orientation".

## 2. Nielsen realization

**Source read.** S. P. Kerckhoff, *The Nielsen realization problem* (research announcement), Bull. AMS (N.S.) 2 (1980)
452–454 (`kerckhoff-1980-announcement\`, AMS open archive). D. Gabai, *Convergence groups are Fuchsian groups*
(announcement), Bull. AMS (N.S.) 25 (1991) 395–402 (`gabai-1991-announcement\`). H. Zieschang, *On extensions of
fundamental groups of surfaces and related groups*, Bull. AMS 77 (1971) 1116–1119 (`zieschang-1971-extensions\`).
Primary not obtained: Kerckhoff, Ann. of Math. 117 (1983) 235–265.

**Quoted (Kerckhoff 1980).** M_g "a closed, oriented 2-manifold of genus g" (the scan reads "g > 2"; the sense is
g ≥ 2). "THEOREM 1. Every finite subgroup of π₀ Diff M_g can be realized as a group of isometries of some hyperbolic
structure on M_g." Footnote 2 to "mapping class group": "We make no restriction to the orientation-preserving case,
however." "THEOREM 2. Every finite subgroup of Mod_g acting on T_g has a fixed point." "Theorems 1 and 2 were known
for G cyclic (Nielsen [4]), solvable (Fenchel [1]), and in many other special cases (see Zieschang [6]). Kravetz [2]
gave a proof of Theorem 2, but it was based on the false belief that T_g, equipped with Teichmüller's metric, has
negative curvature (see Masur [3])." Closing remarks: "the methods used here work for a general Teichmüller space,
when the hyperbolic manifold is allowed to have geodesic boundary or cone-like singularities and ... the theorems
were stated for closed surfaces only to avoid the details involved in defining these structures and their modular
groups. The nonorientable case can be handled by passing to the oriented double cover." "the Nielsen Problem is
equivalent to describing when a finite extension of a surface group is again a surface group (in the generalized
sense of a surface with cone-like singularities, etc.)".

**Quoted (Gabai 1991).** "Theorem 1. G is a convergence group if and only if G is conjugate in Homeo(S¹) to the
restriction of a Fuchsian group." (Footnote: Casson announced a proof by different methods.) The abstract: "This
completes the proof of the Seifert fiber space conjecture and gives a new proof of the Nielsen realization problem."

**History, from a free survey** (K. Mann, B. Tshishiku, *Realization problems for diffeomorphism groups*,
arXiv:1802.00490, `mann-tshishiku-realization\`), for closed surfaces only: the problem "was answered positively for
finite, cyclic groups by Nielsen ... Fenchel [Fen48] gave a positive answer for finite solvable groups, and the
general result for finite groups is due to Kerckhoff [Ker83], with alternate proofs by Tromba, Gabai and Wolpert".

**Hypotheses.** Kerckhoff's announced theorem: closed oriented surfaces of genus ≥ 2, finite subgroups of the full
group π₀ Diff (orientation-reversing classes allowed), realization by isometries, hence by diffeomorphisms and by
homeomorphisms. Punctured surfaces are not named in the announcement (it names geodesic boundary and cone points).

**Bears on.** 2:sc101–102 (his "problème ouvert sur lequel les gens sèchent", existence half); 2:sc195–196 (he admits
realizability of cyclic actions, "sauf erreur ce résultat est bien connu (même pour les groupes résolubles...)");
F2, 3-fidelity.

**Verdict.** Confirms F2's "3-fidelity = Kerckhoff" for ν = 0, orientation-reversing elements included. Confirms his
recollection: cyclic (Nielsen, Acta Math. 75) and solvable (Fenchel 1948), for closed surfaces. For ν > 0 the
statement is still from memory in this line: the 1983 paper was not obtained and the announcement does not name
punctures. Two routes that do not need it: (a) a finite G in the extended mapping class group of a
punctured hyperbolic surface gives an extension E of G by a Fuchsian group of finite coarea; E acts on the circle as
a convergence group, so by Gabai's Theorem 1 it is Fuchsian (the step "E acts on the circle" uses Nielsen's boundary
extension of type-preserving automorphisms: from memory); (b) section 7 below for the torsion-free case. Date note:
his text is of 1981; the general case had been announced in May 1980 and published in 1983, and Zieschang's 1971
footnote (section 7) records that Kravetz's earlier proof had collapsed, which is the state he describes.

## 3. Teichmüller's uniqueness theorem; is F1 in the literature?

**Source read.** L. Bers, *Finite dimensional Teichmüller spaces and generalizations*, Bull. AMS (N.S.) 5 (1981)
131–172, §3 (`bers-1981-finite-dim-teichmuller\`). W. J. Harvey, *On branch loci in Teichmüller space*, Trans. AMS
153 (1971) 387–399 (`harvey-1971-branch-loci\`). Margalit–Winarski (section 4) for the method of MacLachlan–Harvey.

**Quoted (Bers §3).** "(A) Given two marked Riemann surfaces of type (p, n) ... we want to find an extremal map in the
homotopy class ..., that is a map f : S₁ → S₂ homotopic to [the given one] and with the smallest possible dilatation
... The existence of an extremal map follows easily from general compactness properties of quasiconformal maps.
Teichmüller discovered that the extremal map is unique and of a very special form". "(D) Teichmüller's theorem
asserts that (α) every Teichmüller map is the unique extremal in its homotopy class and (β) that every extremal map
is either conformal or a Teichmüller map. Teichmüller first proved, in his famous 1939 paper [114], statement (α); in
1943 he derived (β) from (α) by a continuity argument [115] ... Ahlfors' paper [6] ... contained a new proof of (β).
Later a modernized version of Teichmüller's own proof was given by the author [17]". Type (p, n) = genus p with n
punctures (his §1), excluding the sphere with ≤ 2 punctures and the torus.

**Quoted (Harvey 1971).** Setting: Fuchsian groups "with compact quotient spaces". "Lemma 1. The map î is a real
analytic homeomorphism onto the image set I, which is a closed subset of T(K)" (attributed to Greenberg).
"Theorem 2. F(⟨γ⟩) = î(T(Γ))." "The theorem extends immediately to a description of the fixed point set of any finite
subgroup H ⊂ M_g (and indeed to the fixed point set in T(K) of any finite subgroup of M(K) for an arbitrary group K,
provided that the set is nonempty)." "Corollary 3. Let H ⊂ M(K) be any finite group. Then there exists a group Γ of
Fuchsian type and an injection K → Γ such that (i) 1 → K → Γ → H' → 1 is exact with H' anti-isomorphic to H;
(ii) F(H) = î(T(Γ))."

**Check of F1's proof against these.** (ii) Teichmüller's theorem with punctures: Bers (α)+(β) for type (p, n); the
conformal case is unique because a hyperbolic surface of finite type has no conformal automorphism homotopic to the
identity other than the identity. (iii) h_g = ρ₂(g)⁻¹ h ρ₁(g) is orientation preserving, quasiconformal with the same
maximal dilatation (conformal and anti-conformal maps do not change it) and homotopic to ρ₂(g)⁻¹ρ₁(g) ≃ id; so
h_g = h. No anti-conformal version of the theorem is needed. (i) needs local linearity of the stabilizer groups
(section 1) so that X/ρ_i(G) is a compact surface with boundary, cone points and corners; a conformal structure on it
pulls back to an invariant one on the compact X, hence of finite type on S = X ∖ P. With that amendment the proof is
complete.

**Is F1 new?** No. For closed surfaces and orientation-preserving G it is contained in Harvey's Theorem 2 and
Corollary 3: the fixed set of H is the image of one Teichmüller space T(Γ), Γ the extension of H by K, so any two
invariant structures are σ₁∘i, σ₂∘i for the same abstract (Γ, i), and the isomorphism σ₂σ₁⁻¹ of cocompact Fuchsian
groups is induced by a homeomorphism (Harvey: "an extended Nielsen theorem due to Zieschang [14]"; from memory also
Macbeath 1967). F1's argument by Teichmüller's uniqueness is the method of MacLachlan–Harvey 1975 as described in
Margalit–Winarski ("Their approach ... is framed in terms of Teichmüller theory"; "The key point in the proof is that
σ is injective ... Teichmüller geodesics in Teich(X°) map to Teichmüller geodesics in Teich(S) of the same length").
The sentence "two actions with the same outer action are conjugate by a homeomorphism isotopic to the identity" I
did not find verbatim in any text read here; with punctures, orientation-reversing elements and topological (not
smooth) actions together, F1 as written is a clean statement of a classical fact, to be presented as such.

**Verdict.** Confirms F1 (second and third cited facts), with the amendment to step (i). Corrects its status: a
classical consequence of Harvey 1971 / MacLachlan–Harvey 1975, not a new result; the prompt should ask GPT-6 Astra
(effort Pro) for the proof in his generality (punctures, anti-involutions, no smoothness), not for a novelty check.

## 4. The Birman–Hilden property

**Source read.** J. Birman, H. Hilden, *Isotopies of homeomorphisms of Riemann surfaces and a theorem about Artin's
braid group* (announcement), Bull. AMS 78 (1972) 1002–1004 (`birman-hilden-1972-announcement\`). D. Margalit,
R. Winarski, *Braids groups and mapping class groups: the Birman–Hilden theory*, arXiv:1703.03448
(`margalit-winarski-birman-hilden\`). Primaries not obtained: Birman–Hilden, Ann. of Math. 97 (1973);
MacLachlan–Harvey, Proc. LMS 30 (1975).

**Quoted (Birman–Hilden 1972).** "Let X̃, X be orientable surfaces. Let (p, X̃, X) be a regular covering space,
possibly branched, with finitely many branch points and a finite group of covering transformations. We require also
that every covering transformation leave the branch points fixed." "THEOREM 1. Let g : X̃ → X̃ be a fiber-preserving
homeomorphism which is isotopic to the identity map. If the covering is branched, assume X̃ is not the closed sphere
or torus. Then g is fiber-isotopic to the identity." "THEOREM 2 ... its projection ḡ to X is also isotopic to the
identity map; however, the isotopy may move branch points."

**Quoted (Margalit–Winarski).** "Let p : S → X be a covering map of surfaces, possibly branched, possibly with
boundary." "whenever a fiber-preserving homeomorphism is homotopic to the identity, it is homotopic to the identity
through fiber-preserving homeomorphisms" (the Birman–Hilden property). "we will say that a surface is hyperbolic if
its Euler characteristic is negative." "Theorem 2.1 (Birman–Hilden). Let p : S → X be a finite-sheeted regular
branched covering map where S is a hyperbolic surface. Assume that p is either unbranched or is solvable. Then p has
the Birman–Hilden property." "Theorem 2.2 (MacLachlan–Harvey). Let p : S → X be a finite-sheeted regular branched
covering map where S is a hyperbolic surface. Then p has the Birman–Hilden property." "Theorem 2.3 (Winarski) ...
fully ramified." Counterexample without hyperbolicity: the torus over the sphere with four marked points.
"Proposition 3.1. Let p : S → X be a finite-sheeted branched covering map where S is a hyperbolic surface without
boundary. Then the following are equivalent: p has the Birman–Hilden property; the natural map LMod(X) → SMod(S)/D is
injective; the natural map SMod(S) → LMod(X) is well defined; SMod(S)/D ≅ LMod(X)."

**Hypotheses.** Orientation-preserving deck groups; S hyperbolic (χ < 0), boundary allowed; punctures are not
discussed in the statements (the 1972 announcement says only "orientable surfaces"). The Teichmüller-theoretic proof
uses only Teichmüller's theorem for the quotient with its branch points removed, which holds for type (p, n)
(section 3), so it covers punctured S; deck groups with reflections are covered by the argument of F1 (section 3),
not by the statements quoted (from memory: Macbeath–Singerman 1975 treat NEC groups).

**What it gives.**
- "(A⁰)^u connected" (F2, 1-fidelity; 2:sc279–280). Let f ∈ A⁰ commute with Γ. It is fiber preserving for
  U → U/Γ and isotopic to the identity, so by the property there is an isotopy f_t through fiber-preserving
  homeomorphisms, f₀ = id. For each deck transformation d, t ↦ f_t d f_t⁻¹ is a continuous path in the finite deck
  group, so it is constant: every f_t commutes with Γ, and the path lies in (A⁰)^Γ. Hence (A⁰)^u is path connected.
- "H⁰(Γ, π₁(Mon(S^!, U))) = 1" (2:sc285–286). B/B⁰ ≅ π₁(Mon(S^!, U)) is the kernel of Mod(V) → Mod(U),
  V = U ∖ S^!. Let φ be a Γ-invariant class in it. By F1 for V (two realizations f Γ f⁻¹ and Γ of the same finite
  subgroup of Mod(V)) φ has a representative F commuting with Γ; extended to U it lies in (A⁰)^Γ, so by the previous
  item it is joined to the identity by Γ-equivariant homeomorphisms F_t of U. Each F_t permutes the discrete set S^! of
  points with non-trivial stabilizer, hence fixes it pointwise; so F is isotopic to the identity in V and φ = 1.
  This needs U hyperbolic and uses F1 and the Birman–Hilden property; it proves the relation of the title of §24.
  (π₀(Aut(U)^{0Γ}) = 1 is the previous item.)

**Verdict.** Confirms F2's 1-fidelity for orientation-preserving Γ and S hyperbolic, with the derivations above.
Corrects two points of wording in F2: the primary theorem for arbitrary finite regular covers is MacLachlan–Harvey
1975 (Birman–Hilden 1972/73 need the cover unbranched, or solvable, or every deck transformation fixing every branch
point); and for Γ with orientation-reversing elements the cited statements do not apply as stated (the proof does).

## 5. Contractibility of identity components (his "théorème bien connu", 2:sc215)

**Source read.** C. J. Earle, J. Eells, *The diffeomorphism group of a compact Riemann surface*, Bull. AMS 73 (1967)
557–559 (`earle-eells-1967-announcement\`). T. Yagasaki, *Homotopy types of homeomorphism groups of noncompact
2-manifolds*, Topology Appl. 108 (2000); arXiv:math/0010223 (`yagasaki-homeo-noncompact-surfaces\`), which quotes
Hamstrom and Scott. Primaries not obtained: Hamstrom, Illinois J. Math. 10 (1966) 563–573; Earle–Eells, J. Diff.
Geom. 3 (1969); Earle–Schatz, J. Diff. Geom. 4 (1970); Scott, Topology 9 (1970).

**Quoted (Earle–Eells 1967).** X "a compact oriented surface X without boundary", D(X) the orientation-preserving
C^∞ diffeomorphisms, D₀(X; x₁, ..., x_n) those homotopic to the identity fixing the x_i. "THEOREM 1. Let g denote the
genus of X. (a) If g = 0, then D₀(X; x₁, x₂, x₃) is contractible. Furthermore, D(X) is homeomorphic to
G × D₀(X; x₁, x₂, x₃), where G is the group of conformal automorphisms of the Riemann sphere. (b) If g = 1, then
D₀(X; x₁) is contractible. Furthermore, D₀(X) is homeomorphic to G × D₀(X; x₁), where now G is the identity
component of the group of conformal automorphisms of the torus. (c) If g ≥ 2, then D₀(X) is contractible."
"COROLLARY. In all cases D₀(X) is the identity component of D(X)." And: "Our results confirm a conjecture of
Grothendieck [7, p. 7-09], relating the homotopy of D(X) and T(X)" ([7] = Séminaire Cartan 1960/61, exposé 7).

**Quoted (Yagasaki).** H_X(M) = homeomorphisms of M that are the identity on X, compact-open topology. "Lemma 2.1.
([4], [12, §3]) Suppose N is a compact connected PL 2-manifold and Y is a compact subpolyhedron of N. (i) If
(N, Y) ≠ (D², ∅), (D², 0), (S¹ × [0,1], ∅), (M, ∅), (S², ∅), (S², 1pt), (S², 2pts), (T², ∅), (K², ∅), (P², ∅),
(P², 1pt), then H_Y(N)₀ ≃ ∗. (ii) If A is a nonempty compact subset of ∂N, then H_{Y∪A}(N)₀ ≃ ∗. (iii) If
(N, Y) = (D², ∅), (D², 0), (S¹ × [0,1], ∅), (M, ∅), (S², 1pt), (S², 2pts), (P², 1pt), (K², ∅), then H_Y(N)₀ ≃ S¹."
([4] = Hamstrom 1966, [12] = Scott 1970; M the Möbius band.) "Theorem 1.1. Suppose M is a noncompact connected
(separable) PL 2-manifold and X is a compact subpolyhedron of M. Then (i) H_X(M)₀ ≃ S¹ if (M, X) ≅ (R², ∅),
(R², 1pt), (S¹ × R¹, ∅), (S¹ × [0,1), ∅) or (P² ∖ 1pt, ∅), (ii) H_X(M)₀ ≃ ∗ in all other cases."

**Bears on.** 2:sc215: for N = X_g and Y = S_{g,ν} (ν points), Lemma 2.1 gives A⁰_{g,ν} contractible exactly when
(g, ν) is not (0,0), (0,1), (0,2), (1,0), that is 2g + ν ≥ 3; S¹ for (0,1), (0,2); the two remaining cases are
SO(3) (Earle–Eells (a) with Smale) and the torus (Earle–Eells (b)). This is his equivalence (a) ⇔ (c) ⇔ (d) with his
exceptions. Same answer for Aut(U_{g,ν}) with the compact-open topology (Theorem 1.1). F2, 0-fidelity: the identity
component of Homeo(U)^Γ is the identity component of the homeomorphism group of the quotient surface with its branch
points and punctures marked (mirror boundary if Γ has reflections); an orbifold whose underlying pair is in the
exceptional list of Lemma 2.1 (a disc with ≤ 1 cone point, an annulus, a Möbius band, a sphere with ≤ 2 cone
points, a torus, a Klein bottle, a projective plane with ≤ 1 cone point, none with corner points) has orbifold Euler
characteristic ≥ 0, so for U hyperbolic the component is contractible. Also 2:sc304 ("(SA_{g,ν})⁰ est ∞-connexe":
Lemma 2.1 (ii)).

**Verdict.** Confirms the N-remark on §19 and F2's 0-fidelity, for homeomorphisms, with punctures and with mirror
boundary. Correction of attribution: for homeomorphisms the theorem is Hamstrom 1966 (and Scott 1970), read here only
through Yagasaki's Lemma 2.1; Earle–Eells is the diffeomorphism statement for closed surfaces with marked points and
credits Grothendieck's conjecture; Earle–Schatz was not obtained.

## 6. Dehn–Nielsen–Baer with punctures; the Birman exact sequence (2:sc186–189, 2:sc219–221)

**Not obtained** from a free copy: Zieschang–Vogt–Coldewey (LNM 835); Farb–Margalit, Theorems 4.6, 8.1, 8.8;
Birman, Comm. Pure Appl. Math. 22 (1969).

**Quoted from a free text that cites them** (R. Coulon, A. Sisto, H. Wilton, *Power quotients of surface groups and
mapping class groups*, arXiv:2507.13701v2, `power-quotients-2507.13701\`): "the Dehn–Nielsen–Baer theorem identifies
the outer automorphism group of the surface group with the extended mapping class group MCG^±(S) [31, Theorem 8.1]";
"Theorem 6.2 (Birman). Let S be closed, connected, orientable surface of genus at least two. There is an exact
sequence 1 → π₁(S) → MCG^±(S_*) → MCG^±(S) → 1" ([31] = Farb–Margalit; "the famous Birman exact sequence [31, Theorem
4.6]. We only state the case when S is closed"), with "the natural homomorphism MCG^±(S_*) → Aut(π₁(S))". Harvey 1971
(section 3): "A similar interpretation is possible for any G of Fuchsian type using an extended Nielsen theorem due
to Zieschang [14]."

**From memory (to be confirmed on the book).** Farb–Margalit Theorem 8.8: for S = S_{g,p} hyperbolic, the natural map
Mod^±(S) → Out^⋆(π₁(S)) is an isomorphism, Out^⋆ the outer automorphisms preserving the set of conjugacy classes of
the loops around the punctures. Theorem 4.6: for χ(S) < 0 (punctures and boundary allowed) and x an interior point,
1 → π₁(S, x) → Mod(S, x) → Mod(S) → 1 is exact.

**Bears on.** 2:sc221 ("Théorème bien connu": Γ_{g,ν} ≅ Autext_lac(Π_{g,ν}), Γ'_{g,ν+1} ≅ Aut_lac(Π_{g,ν})) and
2:sc186–189 (Autext(π', i) → Aut(π) an isomorphism when π' of type (g, ν+1) and π of type (g, ν) are both
anabelian). Excluded types: exactly χ(U_{g,ν}) ≥ 0, i.e. (0,0), (0,1), (0,2), (1,0); his list "g ≥ 2, ou g ≥ 1,
ν ≥ 2, ou g = 0, ν ≥ 4" (ν counted on π') is the condition χ(U_{g,ν−1}) < 0 and is right. When only π is abelian:
(1,1) → (1,0) is still an isomorphism (Autext_lac(F₂) = Out(F₂) ≅ GL(2,Z) = Aut(Z²), Nielsen); the case (0,3) → (0,2)
depends on his special definition of the loop group of type (0,2) (2:sc229–230) and was not examined here.

**Verdict.** Closed case confirmed through a free text; the punctured statements remain from memory (no free
legitimate copy of the two books). The N-remarks on §18 and §19 stand as stated, marked "primary not obtained".

## 7. Torsion-free finite extensions of surface and free groups (his (III), 2:sc292–293; 2:sc353)

**Source read.** B. Eckmann, H. Müller, *Poincaré duality groups of dimension two*, Comment. Math. Helv. 55 (1980)
510–520 (`eckmann-mueller-1980-pd2\`, GDZ scan, pp. 510–512 read as images). B. Eckmann, P. Linnell, *Poincaré duality
groups of dimension two, II*, Comment. Math. Helv. 58 (1983) 111–114 (`eckmann-linnell-1983-pd2-ii\`, p. 111).
B. Eckmann, H. Müller, *Plane motion groups and virtual Poincaré duality of dimension two*, Invent. Math. 69 (1982)
293–310 (`eckmann-mueller-1982-plane-motion\`, p. 293). Zieschang 1971 and Kerckhoff 1980 (section 2).

**Quoted.**
- Zieschang 1971: "a conjecture of A. Karrass and D. Solitar raised at the American Mathematical Society meeting in
  Urbana, October 1970: A finite torsionfree extension of the fundamental group of a closed surface is isomorphic to
  the fundamental group of a closed surface." "THEOREM 1. Let 𝔊 be a group without torsion, 𝔉 a subgroup of finite
  index isomorphic to the fundamental group of a closed 'non-euclidean' orientable surface ... Then 𝔊 is isomorphic
  to the fundamental group of a closed noneuclidean surface." Footnote 1: "ADDED IN PROOF. Recently it was found out
  that the theorem about negative curvature of the Teichmüller space in [1] is not true. Therefore [1, Theorem 5.2]
  is not known to be valid and the Theorems 1, 1' and 5 of this article are still open. In the special cases of
  finite extensions by solvable groups the theorems will follow from the fixed point theorem of P. A. Smith".
  "THEOREM 3. A torsionfree finite extension 𝔊 of Z is isomorphic to Z; a torsionfree finite extension of Z² is
  isomorphic to Z² or to the Klein bottle group".
- Eckmann–Müller 1980: "THEOREM 1. Let G be a PD²-group with β₁(G) > 0. Then G is a surface group." "COROLLARY 2. Let G
  be a torsion-free group containing a surface group G₁ as subgroup of finite index. Then G itself is a surface
  group." (1.5: this "concerns the 'Nielsen conjecture' for surface groups".) "THEOREM 2. All PD²-pairs of groups are
  geometric", a geometric pair being "G the fundamental group of a closed surface with m+1 discs removed (m ≥ 0, and
  m ≥ 1 if the surface is the sphere) together with the family of infinite cyclic subgroups generated by the circles
  bounding the discs".
- Eckmann–Linnell 1983: "THEOREM 1. The first Betti number β₁ of a PD²-group is positive." "THEOREM 2. A group G is a
  PD²-group if and only if it is isomorphic to a surface group."
- Eckmann–Müller 1982: "(A) Let G be a virtual PD²-group with β₁(G) > 0. Then G contains a finite normal subgroup K
  such that G/K is (isomorphic to) a plane motion group."

**Bears on.** His (III): "a torsion-free extension of a finite group by a loop group is a loop group", with the
classes of the centralizers of the L_i as loop classes. Case ν = 0: Eckmann–Müller Corollary 2 (1980), independent
of Nielsen realization; surfaces "of genus ≥ 1", orientable or not, so the extension may be a non-orientable surface
group when the finite group reverses the orientation. Case ν ≥ 1: the group is free (Stallings 1968; from memory,
primary not obtained), and the loop structure is given by Eckmann–Müller Theorem 2 once (E; centralizers of the L_i
up to E-conjugacy) is known to be a PD²-pair, which follows from the finite-index theorem for pairs (Bieri–Eckmann
1978; from memory, not obtained). In 1981, when he wrote, the closed case had just been proved (1980) and the
route through realization was conditional (Zieschang's footnote), which matches his "comme si on savait déjà".

**Verdict.** Confirms the N-remark on §28 and the first half of HUNCHES H3 (III) for ν = 0 by a quoted theorem;
for ν ≥ 1 it rests on two statements still from memory (Stallings; Bieri–Eckmann for pairs). The profinite analogue
(LM4 Part D (d)) is not covered by any of these.

## 8. Torsion in profinite completions of Fuchsian groups (§31, 2:sc393; F9)

**Source read.** M. Bridson, M. Conder, A. Reid, *Determining Fuchsian groups by their finite quotients*, Israel J.
Math. 214 (2016); arXiv:1401.3645 (`bridson-conder-reid\`). A. Minasyan, P. Zalesskii, *Virtually compact special
hyperbolic groups are conjugacy separable*, Comment. Math. Helv. 91 (2016); arXiv:1504.00613
(`minasyan-zalesskii-vcsh-conjugacy\`). A. Minasyan, *Hereditary conjugacy separability of right angled Artin groups
and its applications*, Groups Geom. Dyn. 6 (2012); arXiv:0905.1282 (`minasyan-hcs-raag\`).

**Quoted (Bridson–Conder–Reid).** cf(Γ) = "the set of conjugacy classes of maximal finite subgroups". "Theorem 5.1. If Γ
is a finitely-generated Fuchsian group, then the natural inclusion Γ → Γ̂ induces a bijection cf(Γ) → cf(Γ̂). More
precisely, every finite subgroup of Γ̂ is conjugate to a subgroup of Γ, and if two maximal finite subgroups of Γ are
conjugate in Γ̂ then they are already conjugate in Γ." (Injectivity is from conjugacy separability of Fuchsian
groups; surjectivity from "Theorem 2.18. Let G = G₁ ∐_H G₂ be any profinite amalgamated free product. If K is a finite
subgroup of G, then K is conjugate to a subgroup of G₁ or G₂.") "Corollary 5.2. Let Γ be a finitely generated
Fuchsian group. Then Γ̂ does not contain a non-trivial finite normal subgroup." "Corollary 5.3. If Γ is a torsion-free
Fuchsian group, then Γ̂ is torsion-free." Also "Theorem 2.13. Lattices in PSL(2, R) and PSL(2, C) are good." Fuchsian
= discrete in PSL(2,R), cocompact or not ("If the Fuchsian group is not cocompact, then it is a free product of
cyclic groups").

**Quoted (Minasyan–Zalesskii; Minasyan).** "Theorem 1.1. Any virtually compact special hyperbolic group is
hereditarily conjugacy separable." "Corollary 3.5. Suppose that G is a finitely generated residually finite
cohomologically good group with vcd(G) < ∞. Then G has finitely many conjugacy classes of subgroups of prime power
order, and the natural inclusion of G in Ĝ induces a bijection between the conjugacy classes of elements (or
subgroups) of prime order in G and in Ĝ." Minasyan, Proposition 3.2: "the following are equivalent: (a) G is
hereditarily conjugacy separable; (b) G is conjugacy separable and satisfies CC", where for residually finite G
(his (3.2), Corollary 12.2) CC is: "C_Ĝ(g) = \overline{C_G(g)} in Ĝ, for every g ∈ G".

**What follows for §31** (G = G⁺ finite in 𝒯(π₀), realized; E the extension, a Fuchsian group of finite coarea;
Ê = π̂₀·E).
- (a) Splittings. Surjective: a finite K ⊂ Ê mapping isomorphically to G is x K₀ x⁻¹ with K₀ ⊂ E (Theorem 5.1);
  write x = p e with p ∈ π̂₀, e ∈ E; then K = p (e K₀ e⁻¹) p⁻¹, and conjugation by p does not change the projection to
  G, so the section of K is π̂₀-conjugate to a section into E. Injective: sections s₁, s₂ into E that are
  π̂₀-conjugate have images that are maximal finite subgroups of E (π₀ is torsion-free, so every finite subgroup of E
  injects into G) and are conjugate in Ê, hence by some e ∈ E (Theorem 5.1); then e' = s₂(ē)⁻¹ e lies in π₀ and
  e' s₁ e'⁻¹ = s₂. So his map of 2:sc393 (a) is bijective, also for partial splittings.
- (b) π̂₀^G = 1 for G ≠ 1 acting through a splitting. Not in Bridson–Conder–Reid. It follows from the centralizer
  condition: for 1 ≠ k ∈ E of finite order, C_Ê(k) is the closure of C_E(k), a finite cyclic group, and π̂₀ is
  torsion-free (Corollary 5.3), so C_{π̂₀}(k) = 1. The centralizer condition holds for cocompact E by
  Minasyan–Zalesskii Theorem 1.1 with Minasyan Proposition 3.2 (a cocompact Fuchsian group is virtually a surface
  group; that surface groups are compact special is used from memory). For E not cocompact (ν > 0), E is a free
  product of cyclic groups and the statement is the theorem on normalizers of finite subgroups in free profinite
  products (Herfort–Ribes 1985: from memory, not read here).
- Orientation-reversing G: E is then not Fuchsian in the sense of Theorem 5.1. For anti-involutions (order 2)
  Corollary 3.5 of Minasyan–Zalesskii applies (E is good, vcd 2) and gives the bijection of classes of elements of
  order 2, hence of classes of splittings over Z/2 by the argument of (a): the profinite form of his theorem of
  2:sc440–445 (b). For dihedral subgroups no statement was found in the texts read.

**Verdict.** Confirms F9 (a) for orientation-preserving G, with the derivation above (the "right count" is the
bijection cf(Γ) → cf(Γ̂)). Corrects F9 (b): it does not come from Bridson–Conder–Reid; it comes from the centralizer
condition, read for the cocompact case and from memory for the free case. Open in this line: finite dihedral
subgroups in completions of groups with reflections; everything for finite subgroups of Autext_lac(π̂) that do not
stabilize a discretization (HUNCHES H4 (b)).

## 9. Abelian subgroups of mapping class groups (2:sc470; F11 (b))

**Primary not obtained** (Birman–Lubotzky–McCarthy, Duke Math. J. 50 (1983) 1107–1120). **Quoted from a free text**
(J. Behrstock, Y. Minsky, *Dimension and rank for mapping class groups*, Ann. of Math. 167 (2008); arXiv:math/0512352,
`behrstock-minsky-rank\`): "[BLM] showed that the maximal rank of an abelian subgroup of a mapping class group of a
surface with negative Euler characteristic is 3g − 3 + p where g is the genus and p the number of boundary
components"; "this rank is realized by any subgroup generated by Dehn twists on a maximal set of disjoint essential
simple closed curves."

**Bears on.** His H = ⟨ρ_j⟩ ≅ Z^g, generated by the Dehn twists about the g core circles of the tubes T_j (a cut
system). For g ≥ 2, g < 3g − 3, and the g circles extend to a pants decomposition, so H lies properly in a free
abelian subgroup of rank 3g − 3: H is not maximal among free abelian subgroups. For g = 1 it is (rank 1, and the
twist has no root in SL(2,Z)).

**Verdict.** Confirms F11 (b); the statement of the rank is read through Behrstock–Minsky, "primary not obtained".

## 10. Anti-involutions: the Weichold–Klein classification (2:sc437–440; F11 (a))

**Source read.** B. Gross, J. Harris, *Real algebraic curves*, Ann. Sci. ENS (4) 14 (1981) 157–182, §3 (Numdam;
`gross-harris-real-curves\`).

**Quoted.** "let n(X) denote the number of ... connected components of X(R). The real locus X(R) of a curve X of genus
g consists of n(X) disjoint circles. The complement of the real locus in the complex locus has either one or two
connected components [7]. Put a(X) = 0 if X(R) divides the complex locus, and a(X) = 1 if X(C) − X(R) remains
connected." "The quotient of X(C) by complex conjugation is a connected 2-manifold M with n(X) boundary components.
M has Euler characteristic (1 − g) and is orientable if and only if a(X) = 0." "PROPOSITION 3.1. (1) 0 ≤ n(X) ≤ g+1.
(2) If n(X) = 0 then a(X) = 1. If n(X) = g+1 then a(X) = 0. (3) If a(X) = 0 then n(X) ≡ g+1 (mod 2). Klein proved
that all pairs (n(X), a(X)) which are permitted by Proposition 3.1 actually occur for some real curve X of genus g
([7], [8])." (References to Klein, Weichold 1883.)

**Count.** The quotient M is determined up to homeomorphism by χ = 1 − g, n and orientability, so the conjugacy
classes of anti-involutions of X_g are the admissible pairs: a = 1 (quotient non-orientable): n = 0, ..., g, that is
g+1 classes (his first statement, 2:sc439); a = 0 (quotient orientable): 1 ≤ n ≤ g+1, n ≡ g+1 (mod 2), that is
⌊(g+2)/2⌋ classes (his marginal correction, g = 2γ + μ − 1). Total g + 1 + ⌊(g+2)/2⌋ = ⌊(3g+4)/2⌋ (2, 3, 5, 6, 8 for
g = 0, ..., 4).

**Verdict.** Confirms F11 (a) as stated. His hope of 2:sc440 (classes distinct in A_g stay distinct in 𝒯_g) follows
from F1: conjugate classes are realized by involutions with the same outer action up to a homeomorphism, which are
then conjugate.

## 11. Rotation data and geometric isomorphisms (2:sc155–160; F10)

**Not obtained:** Zieschang–Vogt–Coldewey; Macbeath 1967; Harvey, Quart. J. Math. 17 (1966); Nielsen 1937.

**Source read.** Harvey 1971 (section 3), §3: "If T : S → S is a conformal self-mapping of order n which fixes a point
P, then in local coordinates z near P we must have T(z) = εz where ε is a primitive nth root of unity. Thus T is
locally a rotation at P through angle 2πν/n where (ν, n) = 1." "Theorem 7. The rotation angles of the automorphism
group ⟨t⟩ are determined by the homomorphism φ", φ : Γ → Z_n the epimorphism with kernel the surface group, under the
normalization "the element x_i ∈ Γ is a counterclockwise rotation about z_i through angle 2π/m_i" (closed surfaces).

**Bears on.** His μ_E and his question whether it is intrinsic in E. Harvey's Theorem 7 is the formula he asks for:
μ is read from the extension once the elliptic generators are known as counterclockwise rotations, that is, once the
orientation and the loop structure of the drilled group are given (his margin of 2:sc159). Invariance under
isomorphisms of extensions that respect π, its loop structure and T: such an isomorphism is induced on π by an
orientation-preserving homeomorphism (section 6, punctured case from memory), the two actions are then conjugate by
F1, and a conjugating homeomorphism carries fixed points to fixed points and keeps rotation numbers (section 1:
local conjugacy to a rotation). Orientation reversal inverts them.

**Verdict.** F10 confirmed as a corollary of F1 with sections 1 and 6; its citation "Zieschang–Vogt–Coldewey" stays
from memory and is not needed. His abelian counterexample (2:sc157–159) is unaffected.

---

## Table

| Finding | Result | What changed |
|---|---|---|
| F1 | confirmed, proof complete after one amendment | step (i) needs local linearity of the finite stabilizer groups (Kolev), not only of periodic maps; Teichmüller's theorem with punctures read in Bers 1981 §3; status corrected: a classical fact (Harvey 1971 Thm 2, Cor. 3; MacLachlan–Harvey 1975), not new |
| F2, 3-fidelity | confirmed for ν = 0 (Kerckhoff 1980, any orientation behaviour) | for ν > 0 still from memory: the 1983 paper was not obtained, the announcement names boundary and cone points only |
| F2, 2-fidelity | = F1 | — |
| F2, 1-fidelity | confirmed for orientation-preserving Γ | primary is MacLachlan–Harvey (not obtained; read through Margalit–Winarski Thm 2.2); Birman–Hilden's own theorem has extra hypotheses; reflections not covered by the quoted statements; derivations of "(A⁰)^u connected" and of H⁰(Γ, π₁(Mon)) = 1 written in section 4 |
| F2, 0-fidelity | confirmed | the homeomorphism theorem is Hamstrom/Scott (through Yagasaki Lemma 2.1), not Earle–Eells; exceptional quotient pairs excluded by an Euler characteristic count |
| F9 (a) | confirmed for G = G⁺ | Bridson–Conder–Reid Thm 5.1 plus the short argument of section 8 |
| F9 (b) | corrected | not in Bridson–Conder–Reid; follows from the centralizer condition (Minasyan–Zalesskii Thm 1.1 with Minasyan Prop. 3.2 for cocompact E; Herfort–Ribes from memory for free E) |
| F10 | confirmed as a corollary of F1 | Harvey 1971 Thm 7 gives the formula; Zieschang–Vogt–Coldewey not obtained and not needed |
| F11 (a) | confirmed | Gross–Harris Prop. 3.1 and Klein; count ⌊(3g+4)/2⌋ = (g+1) + ⌊(g+2)/2⌋ |
| F11 (b) | confirmed | rank 3g − 3 + p read through Behrstock–Minsky; primary not obtained |
| his (III), N on §28 | ν = 0 confirmed (Eckmann–Müller 1980 Cor. 2; Eckmann–Linnell 1983) | ν ≥ 1: Eckmann–Müller Thm 2 read; Stallings and the finite-index theorem for pairs from memory |
| N on §15, 2:sc146–148, 2:sc440 | confirmed | his lemma of 2:sc146–147 is false without "orientation preserving" (u = z̄) |
| N on §18–19 (Dehn–Nielsen–Baer, Birman) | closed case confirmed through a free text | punctured statements from memory (Farb–Margalit 4.6, 8.8) |
