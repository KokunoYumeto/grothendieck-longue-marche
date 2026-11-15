# Round 1 talk: the shape-map agent

Claude Fable 5.2 (effort medium, no sub-agents), 13 November 2026. Reread before writing: Revision 3 of
`braindump_board\SHAPE_MAP_REVISION_20261113.md`, `KNOWLEDGE_HANDOFF_SHAPE_MAP.md`, the card's "Framing of the global
shape". Read new: `pro_intake_20261113\IMPLICATIONS.md` and `NEXT_PROMPT_ITEMS.md` in full, `AGENDA.md`.

**Grounds.** I read reports and registers of the returns, and one proof (LM7 E.32). Everything from the returns is
"claimed". "Mine" marks a step of my own, checked by nobody. The build-on note asked of me is folded into this talk.

## 1. The central statement as it stands

**Statement (the card's).** In every framework of the map, the failure of the passage from finite stages to the limit
is a first-derived class, invisible to the underived object and to sizes, and absorbed by the derived or
one-dimension-up object.

**What Revision 3 and the intake add.**

- **One duality joins the colimit side and the limit side (intake I1).** For M: A → Ab,
  lim^i over A^op of Hom(M, R/Z) is Hom(T_i(M), R/Z). So exactness of colim_A is the vanishing of lim¹ on diagrams of
  compact abelian groups. My Revision 3 had this as speculation 6 ("framework 1 is dual to framework 2"); the intake
  proved it and computed the instance lim¹ = F_p over C_δ^op. Speculation 6 is settled.
- **The obstruction has two coordinates: the index and the coefficients.**

  | | compact coefficients | non-compact coefficients |
  |---|---|---|
  | directed index | no class (LM8 F.15, first half) | lim¹ = closure(im d)/im d; the gap closes (F.15 counterexample, F.21, LM7 E.32, LM7_PUSH A.1–A.4) |
  | non-directed index | a class with uniform gap and closed range: lim¹ = F_p, T₁ = R (TOTEX2 A.24, dual) | not yet met in the returns |

- **Three regimes, not one (intake I5, P5).** My closing-gap form B2 covers the right-hand column. It does not cover
  the lower left: there nothing closes, and the class is a full cokernel. I accept this limit on B2.
- **A correction to my Revision 3, from the card.** I wrote that the class of LM7_PUSH being invisible to
  cardinalities made the second half of the D+1 statement wrong "if the determinant is a size". That reading was
  the wrong one. A determinant line is a class that no size sees. So "non-zero and invisible to cardinalities"
  (LM7_PUSH: two lattices with identical cardinalities and different derived limits) is the profile the D+1 statement
  predicts. I withdraw the sentence.
- **Two proved instances of the absorbing object.** The Tate complex Cone(C_* → C^*) with B(M)^∨ ≃ B(M^∨)[−1]
  (my Revision 2, A2; mine). The pairing T_i(M) × lim^i(M^∨) → R/Z (intake I1). Both are a duality between a class and
  a class of the dual object, in the derived object.

## 2. What kills the class: the build-on

Revision 3's column "what kills it" was per framework. With the two coordinates it reads:

- **Directed index:** compact coefficients kill it. For non-compact coefficients, bounded Smith valuations kill it
  (LM7_PUSH), and so does a fixed finite set of primes (LM8 F.20).
- **Non-directed index, compact coefficients (claimed, TOTEX2):** an exact index (filtered; Δ_inj; ordered graphs,
  A.8); the Ramsey property (A.6, A.13); quasi-filtered with a uniform bound on the fibres (A.15, A.20). Totality
  does not (A.24).
- **A known fact that supports N5 (from memory, not opened):** over N, the lim¹ of a tower of countable groups is
  zero or uncountable (Gray). So a finite class such as F_p cannot occur over N for countable groups. A finite
  non-zero lim¹ is a signature of a non-directed index.

**A computation that splits floor question 1 (mine, unchecked).** Let FI be the category of finite sets and
injections. Its Fraïssé limit is a countable set, with group S_∞, which is amenable and not extremely amenable.
- *FI is exact over Q.* The one-object category BS_n is final in the full subcategory on sets of size ≤ n (every set
  injects into [n], and the injections form one S_n-orbit). So colim over FI of M is the directed colimit over n of
  the coinvariants (M_n)_{S_n}. Coinvariants of finite groups are exact over Q, and directed colimits are exact.
- *FI is not exact over F₂.* Let P be the FI-module of F₂-combinations of ordered pairs of distinct elements, U the
  same for unordered pairs, and K the kernel of P → U. K is spanned by the elements (a,b) + (b,a) and is isomorphic
  to U. The colimits of K and of P are both F₂, and the map between them sends the generator to
  [(a,b)] + [(b,a)] = 2[(a,b)] = 0. So colim is not injective on K → P, and T₁(U) ≠ 0 over F₂.
- *FI is not total* (sketch): the category of elements of the functor of unordered pairs has the homotopy type of
  BC₂.
- Consequences, if this stands. N2 as written ("exact iff G amenable", for a class with canonical amalgamation) can
  hold only rationally: FI has canonical amalgamation and an amenable group and is not exact over Z. It agrees with
  TOTEX2 A.2 (exact over Z iff over Q and every F_p): the two halves have different criteria. It also ties
  Revision 3's framework 5 (integral against rational) to framework 1: the F₂-class comes from the finite groups in
  the index and dies over Q.

## 3. Floor question 1: what plays Mittag-Leffler's role for a non-directed index?

My answer is three statements, by the kind of object whose limit must be non-empty. For G = Aut(M):

| What must have a point | Fixed-point property of G | Status |
|---|---|---|
| every diagram of non-empty compact Hausdorff spaces | on every compact G-space: extreme amenability, the Ramsey property | claimed, TOTEX2 A.13 (with Kechris–Pestov–Todorcevic, not opened) |
| every diagram of torsors under compact abelian groups: this is lim¹ = 0, hence exactness (I1) | on compact principal homogeneous spaces under compact abelian groups | the statement to prove; it sits between the other two |
| every diagram of compact convex sets | on compact convex G-spaces: amenability, the convex Ramsey property (Moore; from memory) | the candidate of N2 and P1 |

- So Mittag-Leffler's role is played by a fixed-point property, and which one depends on the coefficients.
- Over Q or R, torsors under vector groups are convex, and amenability is the right candidate. FI supports it.
- Over F_p, convexity is not available. The FI example shows what else is needed: the stabilizer of a 2-element set
  is an open subgroup of S_∞ with a quotient of order 2, and that quotient is the class. Candidate statement: colim_A
  is exact over F_p only if no open subgroup of G has a continuous quotient of order p; with convex Ramsey this may be
  sufficient. In C_δ the order makes every object rigid, so this second condition holds trivially and the failure is
  the first one, in every characteristic at once (T₁ = R for every R).
- TOTEX2 A.18 (probability combinations of the three arrows stay at distance ≥ 1) reads to me as the failure of
  convex Ramsey for C_δ. If so, Aut(M_δ) is not amenable and C_δ is consistent with the rational statement. I have
  not read A.18's proof; see question 1 below.

## 4. Floor question 2: the section statements

- **LM7 E.23: I do not think the mixed-prime kernel carries it.** E.23 concerns pro-3 quotients of one group: a
  compact tower over a directed index. By LM8 F.15 such towers have no lim¹, and the section set of the limit is the
  limit of the section sets. What remains there is obstruction at finite depth, of the kind LM7_PUSH exhibits at 17
  (a class-three lift and no class-four lift; A.6, B.4). The lim¹ classes of E.32 and F.21 belong to integral H² with
  unrestricted ramification, a non-compact module, and not to the section set. This is a statement about the route
  "E.23's residue is a limit phenomenon": checked against F.15 as claimed, not against LM7's proofs.
- **The full profinite statements are where the kernel enters.** For P¹ minus three points over Q, and for LM8 A.12
  and G.20, write N for the kernel of Π → ∏_ℓ Π^(ℓ). The precise form the card's framing asks for: the sections with
  a given image modulo N form, when non-empty, a set governed by the non-abelian H¹(G_Q, N) twisted by the section.
  That is a first-derived class, and by construction no pro-ℓ quotient sees it. Statement to prove or correct: for a
  point or cusp section of P¹ minus three points this twisted H¹ is trivial. LM8 A.22 (order 75) and LM4 D.29, D.30
  are the first places to compute it. The intake calls G.20 "an H⁰-type failure over a discrete set of primes"; I
  read the same fact one degree up, as the torsor of lifts. Which reading is right is a question for round 2.
- **LM4 against LM7_PUSH's CM shadows.** LM7_PUSH E.2 says the 24 CM pairs survive "every relative kernel of order
  prime to six", with full profinite survival open. So the untested quotients are those involving 2 and 3 together
  with another prime, which is the mixed-prime situation. I have not seen LM4's counterexample itself (it was not
  in the part of the report I read), so I can say only that it bears on the right place.

## 5. Floor question 4: framework by framework

| Framework | The first-derived class | Invisible to | Absorbed by | Verdict on the central statement |
|---|---|---|---|---|
| Derived colimit (TOTEX2) | T₁(Q_R) ≅ R; dually lim¹ = F_p | set-valued functors (totality holds); the underived colimit | the homotopy colimit | confirms; sharpens: uniform gap, closed range |
| Derived limit of a tower (E.32, F.21, F.15, LM7_PUSH) | lim¹ = closure(im d)/im d | every finite level, every place, cardinalities, finite base change, finite computation | the derived limit; Milnor's telescope | confirms, including "invisible to sizes" |
| Integral against rational (LM8 F.22, the congruence of the fake shadow) | torsion: 5³ classes; a denominator 24 | the rationalization | the derived tensor product (Bockstein) | confirms |
| Pro-p against profinite (LM8 A.22, G.20; LM4) | proposed: H¹(G_Q, N) twisted, N the kernel to the product over primes | every maximal pro-p quotient | the full profinite group | needs its precise form; proposal in section 4 |
| The Galois part against the full topos (LM8 E.10–E.11; TOTEX2 A.33) | the intake finds no class: the limit topos is empty by a covering argument | — | the pro-object: take coverings stage by stage, the limit afterwards (I2) | the absorbing object is there; the class is to be found. My proposal: it is the cone i^*Rj_*, the punctured neighbourhood, as in the Tate complex at ∞ |
| The archimedean place (LM7 E.18, E.25; Connes–Consani) | Ĥ^*(C₂, M), the Tate complex | finite places | the cone, with shift [−1] (mine, Revision 2, A2) | confirms |
| Weil positivity, λ → ∞ (Andrews–Connes–La Gatta) | not identified: Hypothesis LA is a bound on a closing gap ε_λ against δ₄(λ) | each finite window | — | needs another form, or the class is to be found |
| Navier–Stokes force budget | not identified. Route checked: Proj¹ of the restriction spectrum of smooth forces vanishes (restrictions are onto), so the class is not there | — | — | open. Proposal: by the duality of I1 the condition "all derivatives bounded in the limit" should be read on the inductive side, as acyclicity of an inductive spectrum of bounded sets |
| Sum of squares after descent (zeta workbench) | route checked: H¹ of the finite deck group on certificates vanishes by averaging; Ψ₂^♯ is negative off the image of the cover | — | — | open in another form |

## 6. Three questions

1. **To the Dérivateurs expert.** (a) Is TOTEX2 A.18 exactly the negation of the convex Ramsey property for the age
   of C_δ, so that Aut(M_δ) is not amenable? (b) Does the FI example of section 2 stand against A.2, A.15 and A.20:
   exact over Q, T₁ ≠ 0 over F₂ on the module of unordered pairs, and not total? If it does, should N2 be split into a
   rational statement (amenability) and a statement over F_p (no open subgroup with a quotient of order p)?
2. **To the LM7 reviewer.** From the proofs you read: at each nilpotency class of the pro-3 tower of E.23, is the
   section set compact, so that the sections of the limit are the limit of the sections and E.23's residue is
   obstruction at finite depth only, as at 17 in LM7_PUSH? And is "prime to six" in LM7_PUSH E.2 the exact boundary of
   what was tested for the CM shadows?
3. **To the EXIT_ONE_TYPE reviewer.** Is LM8 E.11's covering germ BZ the fundamental groupoid of the normal link that
   your P1a1 computes as a homotopy fibre? In exodromy terms, is "the limit of the punctured neighbourhoods" the
   object i^*Rj_*, that is, the cone of j_! → Rj_*? And for the henselian étale case, which hypothesis (coherence of
   the topoi and of the transition maps, intake I2) makes the limit topos equal to the classifying topos of Ẑ(1)?
