# Deuring-category research memorandum: cote 15, scans 016–032

## Scope, provenance, and status discipline

This memorandum was prepared only after the parent agent froze the transcription. I read the frozen text, context/README.md, the complete context/notes/RESULTS_STATE.md, and the relevant supplied context notes; I did not view any manuscript images or alter any transcription, doubts, inventory, or progress record. All current witnesses below refer to the files MPL_12_150-168+15_002-033/pages/MPL_12_150-168+15_002-033_15_scanNNN.tex, with NNN supplied by the scan number; line numbers are local to those frozen files. Mathematical objections below do not resolve handwriting.

The metadata label “own calculation” means an explicit argument developed in this audit, not a claim that the result is historically new. “Contradicts” below always identifies the precise displayed mathematical assertion contradicted, and never licenses a transcriptional emendation. Primary-source comparisons are retrospective mathematical comparisons, not evidence of the manuscript’s date or the author’s historical access to a later publication.

Exact relevant register statuses, retained throughout:

- **WG2 §2.4 #3**: “question or plan item of the war game (round 2; unchecked).” It asks how motives are built from Lefschetz correspondence rings; a Deuring construction supplies a specific categorical model, not an answer to that whole historical question.
- **WG2 §2.3 #12**: “question or plan item of the war game (round 2; unchecked).”
- **MPL_15_087-138 §3** and **MPL_15_087-138 §124**: “observation (research note of a returned package, first pass; a lead).”
- **MPL_15_195-228+18_002-017 M01**: “The category is used, not constructed f… (research note of a returned package, first pass; a lead).”
- **MPL_15_195-228+18_002-017 B03**: “Polarization and real-section reconstru… (research note of a returned package, first pass; a lead).”
- **LM1 A.8**: “Refuted (the return’s claim).”
- **SECTIONS_OVER_Q A.198**: “Proved (the return’s claim).”

The latter two are supplied return claims, not independently referee-approved results. No supplied settled register entry specifically proves the Deuring classification, the local autoequivalence assertion, or the universal norm construction.

## Integrable notes

### D01 — Rank one is relative to O, and preadditivity does not supply direct sums

**Kind:** definitional clarification / own calculation.  
**Witness:** 15/016:L4–16; 15/026:L7–12.  
**Brief quotation:** “loc. sur Spec A libre de rang 1 sur O”.  
**Context search and relation:** Searches “Deuring | bimodule | rang 1 | category of motives” found no earlier Deuring definition in context/MPL_16+47+54+44_transcription.tex or its notes; this **adds** an explicit category to that file’s cote 16/049 semisimplicity programme and **differs** from the already-used motivic category at context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, M01, 15/219 and 18/011.  
**Register:** WG2 §2.4 #3 [unchecked plan, exact status above]; MPL_15_195-228+18_002-017 M01 [first-pass lead, exact status above].  
**Confidence/reason:** high; follows directly from the marginal definition and endomorphism rings.

The intended objects are right O-modules locally isomorphic to O over Spec A, rather than arbitrary finitely generated projective O-modules or modules of A-rank one. Thus, for O=M_d(A), an object has A-rank d², although its image under a splitting representation has rank d. The category is preadditive because its Hom sets are A-modules; it need not contain direct sums of its objects, since O⊕O has O-rank two.

### D02 — The change of base object preserves the order because it is locally a change of presentation

**Kind:** completion of the written proof sketch / own calculation.  
**Witness:** 15/016:L18–25 and 15/017, opening continuation.  
**Brief quotation:** “pour un des objets … tt autre”; “résulte du fait”.  
**Context search and relation:** “commutant | ordre maximal | semi-simple” gives no parallel proof in the supplied context; this **adds** a specific module-theoretic argument to context/MPL_16+47+54+44_notes.md, 16:49:4, whose question concerns semisimplicity of correspondence algebras.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no matching settled Deuring entry.  
**Confidence/reason:** high; Zariski-local trivializations of P make the claims explicit.

For P locally free of rank one over O, O′=End_O(P) is locally isomorphic to O as an A-algebra, so maximality and the Azumaya property, when separately assumed, pass to O′. The maps Q↦Q⊗_{O′}P and P′↦Hom_O(P,P′) are inverse equivalences on the relevant rank-one module categories, with the usual evaluation and composition maps checked after trivializing P. This supplies the omitted local argument without treating maximality as a consequence of rank-one projectivity alone.

### D03 — The live product ideal has an ambient-algebra and a handedness problem

**Kind:** reading question separated from a mathematical variance check.  
**Witness:** 15/017, displayed O.O′ and preceding bimodule convention.  
**Brief quotation:** “O: drt, O′: g”; “O.O′ … ⊂ K”.  
**Context search and relation:** “bimodule | commutant | ordre” yields no corresponding construction in the supplied context; this **adds** a local textual audit beyond context/MPL_16+47+54+44_notes.md, cote 16/049.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no direct settled entry.  
**Confidence/reason:** high for the algebraic mismatch, no judgment about the ink.

For noncommutative E, the product O.O′ lies naturally in E and contains O, so the frozen inclusion in K cannot express its intended ambient algebra unless E=K. In addition, O.O′ is naturally a left O, right O′ bimodule, whereas the preceding convention asks for left O′, right O; the reversed product or an inverse connecting bimodule has the requested variance. These are two mathematical checks on the literal formula, not proposed replacements for its frozen readings.

### D04 — Rank-one equivalence retains the algebra type, not merely the Brauer class

**Kind:** own counterexample.  
**Witness:** 15/017, generic-isomorphism assertion; 15/018, first paragraph.  
**Brief quotation:** “classes d’isomorphie”; “i.e. … groupe de Brauer”.  
**Context search and relation:** “Brauer | Azumaya | Br′” locates context/MPL_16+47+54+44_notes.md, 16:21:3 and 16:21:6, which already distinguish kinds of Brauer group; the present observation **adds** an independent distinction between algebra isomorphism and Brauer equivalence.  
**Register:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 §124 [first-pass lead]; neither settles this assertion.  
**Confidence/reason:** high; explicit endomorphism-ring obstruction.

Take the Dedekind local ring A=Z_3 and the maximal Azumaya orders O=A and O′=M_2(A). Both have Brauer class zero, but every locally free rank-one object over either order is globally free because A is local, so its endomorphism ring is respectively A or M_2(A), preventing an A-linear equivalence of the two rank-one categories. Thus the preceding generic algebra isomorphism/type classification cannot be replaced by Brauer classes without changing the equivalence relation; the modern Brauer relation is Morita-type stabilization (Stacks Project, §59.62, Tag 0A2J).

### D05 — Maximal orders in a generic central simple algebra need not be Azumaya over A

**Kind:** mathematical objection / explicit example.  
**Witness:** 15/016:L10; 15/018, first paragraph; compare 15/020:L9.  
**Brief quotation:** “ordre maximal”; “algèbres d’Azumaya … sur A”.  
**Context search and relation:** “Azumaya | Brauer | ordre maximal” finds context/MPL_16+47+54+44_notes.md, cote 16/021, but no ramified-order comparison; this **differs** from the cohomological Brauer discussion there and **adds** the necessary integral distinction.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no settled Deuring entry.  
**Confidence/reason:** high; the ramified quaternion order in Construction A below has a visibly nonsimple special fibre.

For A=Z_3, the quaternion division algebra D=(Q_3(i)/Q_3,3) has maximal order O=Z_3[i]⊕Z_3[i]Π with Π²=3 and Πi=−iΠ. The nonzero two-sided ideal generated by Π in O/3O has square zero, so this fibre is not central simple and O is not Azumaya over A, even though D is central simple over K. This supplies a counterexample to identifying the maximal-order setting of scan 016 with Azumaya algebras over A in scan 018; see Voight (2021), Theorem 13.1.6 and Proposition 13.3.4.

### D06 — The homotopy indices change between scans 019 and 030

**Kind:** reading question / notation comparison.  
**Witness:** 15/019:L4–18; 15/030:L11–13.  
**Brief quotation:** “π_[deleted 0]1”; “π_0(End(C))”; “π_1=A*”.  
**Context search and relation:** “Gr-catégorie | Brandt | π_0 | π_1” found no matching categorical-group convention in the supplied context; this **adds** an indexing audit to the gerbe comparisons at context/same_cote_15/MPL_15_087-138_notes.md, T15–T18, scans 123–135.  
**Register:** MPL_15_087-138 §124 [first-pass lead].  
**Confidence/reason:** high for the comparison, without declaring the author’s convention uniform.

For a monoidal groupoid of autoequivalences, the conventional invariants are π_0, the group of isomorphism classes of objects, and π_1=Aut(id), the automorphisms of its tensor unit. Scan 019’s displayed indices and End(id) versus centre units therefore need comparison with scan 030, where π_1=A* agrees with that convention; the endomorphism ring of the identity is Z(O), whereas its automorphism group is Z(O)*. The H³ invariant is the associator class with coefficients in the latter group and with its specified π_0-action (Baez & Lauda, 2004, Theorem 43 and Corollary 44).

### D07 — Trivial action on the centre requires the central A-linear hypothesis

**Kind:** scope clarification / own counterexample to an unrestricted extension.  
**Witness:** 15/019:L10–18; compare broader 15/026 and 15/030:L5–11.  
**Brief quotation:** “l’opération … triviale”; “σ(λ)x=xλ”.  
**Context search and relation:** “centre | centralité | gerbe | conjugaison” locates context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, P14, 18/011, where section and centrality are separated; this **adds** a different, categorical-centre test, rather than restating that group-theoretic question.  
**Register:** MPL_15_087-138 §124 [first-pass lead]; the register’s group centralizer questions are not resolved here.  
**Confidence/reason:** high; explicit conjugation bimodule.

If Z(O)=A and all bimodules and equivalences are A-linear, their action on the centre is indeed trivial. The assertion does not extend automatically to the general A-algebras admitted later: for A=R and O=C, the rank-one bimodule with one action twisted by complex conjugation acts nontrivially on Z(O)=C. Thus the coefficient action in the H³ classification must be retained when the central hypothesis is dropped, as in the general classification of Baez and Lauda (2004, §8.3).

### D08 — A noncanonical inverse presentation is different from failure of biequivalence

**Kind:** conceptual clarification.  
**Witness:** 15/019, last paragraph; 15/020:L2–7.  
**Brief quotation:** “2-équivalence”; “pas de 2-foncteur naturel en sens inverse”.  
**Context search and relation:** “gerbe | foncteur fibre | can.” locates context/same_cote_15/MPL_15_087-138_notes.md, T18, scan 135, where a cancelled canonicity claim accompanies an explicit choice; this **restates** the need to distinguish an equivalence from a preferred presentation, in a different construction.  
**Register:** MPL_15_087-138 §124 [first-pass lead].  
**Confidence/reason:** high; base-object choices account for the issue.

The forward construction O↦P_1(O) loses a distinguished base object, so recovering a ring presentation requires choosing X and writing End(X). A biequivalence can have a pseudoinverse with coherent choices without providing a natural strict reverse 2-functor independent of such choices. The handwritten complaint is therefore naturally read as a canonicity/coherence issue, not as a contradiction of the preceding 2-equivalence.

### D09 — The revision on scan 020 strengthens the hypothesis, but the following “i.e.” does not characterize it

**Kind:** withdrawn hypothesis / mathematical objection.  
**Witness:** 15/020:L9.  
**Brief quotation:** cancelled “ordres maximaux … sur K”; inserted “alg. d’Azumaya”; “i.e.”.  
**Context search and relation:** “Azumaya | centre | Ban” found no matching revision in the supplied context; this **adds** the integral hypothesis needed for the gerbe construction beyond the Brauer discussion at context/MPL_16+47+54+44_notes.md, 16:21:3.  
**Register:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 §124 [first-pass lead].  
**Confidence/reason:** high; Construction A has centre A but is not Azumaya.

Replacing maximal orders in a generic Azumaya algebra by Azumaya algebras over A removes precisely the ramification problem of D05. However, A≅End(id_C), or centre equal to A, is necessary but insufficient: the ramified quaternion order in Construction A has centre A and is not Azumaya. Both the material change of hypothesis and the insufficiency of the displayed “i.e.” should be retained as distinct observations.

### D10 — Splitting modules give the G_m-band and explain independence from X

**Kind:** completion of a construction / own verification.  
**Witness:** 15/020:L10–20.  
**Brief quotation:** “banalisations”; “lien G_m”; “ne dépend pas du choix de X”.  
**Context search and relation:** “gerbe | Giraud | foncteur fibre” locates context/same_cote_15/MPL_15_087-138_notes.md, T18–T18b, scan 135, and context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, A13, scans 207–209; this **adds** a concrete Azumaya splitting gerbe to those fibre-functor comparisons.  
**Register:** MPL_15_087-138 §124 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].  
**Confidence/reason:** high under the inserted Azumaya hypothesis; checked after a splitting cover.

For an Azumaya algebra O of degree d, use pairs (V, O⊗_A𝒪_T≅End(V)), with V locally free of rank d over the structure sheaf 𝒪_T, as the objects of its splitting gerbe. An automorphism compatible with the O⊗_A𝒪_T-action is multiplication by a unit of the structure sheaf 𝒪_T, giving the band G_m. Replacing X by P⊗_O X sends V to P⊗_O V and identifies the same scalar automorphisms, explaining the asserted independence from X without a preferred trivialization.

### D11 — Scan 021 mixes algebra rank, splitting rank, and scalar weight

**Kind:** reading question with a split-case mathematical test.  
**Witness:** 15/021:L2–15 and L25; compare 15/023:L12–14.  
**Brief quotation:** “de degré 1”; “n(x) … rg de _A O”; “Azumaya de rang n(x)”.  
**Context search and relation:** “rang | degré | Tate” locates context/same_cote_15/MPL_15_087-138_notes.md, T06, scan 119, which expressly distinguishes “de degré 1, rang 2”; this **differs** from the rank/degree identification now written and supplies a nearby terminological comparison.  
**Register:** MPL_15_087-138 §3 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].  
**Confidence/reason:** high; O=M_2(A) gives an immediate test.

For O=M_2(A), the algebra has A-rank four, its splitting module has rank two, and scalar λ on that splitting module has weight one. In the modern consistent notation d=degree(O), the image of C in representations consists of weight-one bundles of rank d, while rank_A(O)=d². The class is annihilated by d (Stacks Project, Lemma 59.62.2), so the frozen n(x) must not be silently interpreted simultaneously as these different ranks.

### D12 — The reduced-norm determinant identity can be checked by transition functions

**Kind:** own construction / verification.  
**Witness:** 15/021:L17–21; 15/022, multiplicativity display.  
**Brief quotation:** “det X′≃det(X) Nrd(P)”; “compatible … ass.”.  
**Context search and relation:** “déterminant | determinant | Tate | norme” locates context/same_cote_15/MPL_15_087-138_notes.md, L15, scan 135, and its Proof D; this **adds** a norm-line construction, whereas L15 tests preservation of a specified determinant character.  
**Register:** LM1 A.8 [“Refuted (the return’s claim)”], only as a distinct determinant comparison; WG2 §2.4 #3 [unchecked plan].  
**Confidence/reason:** high; local transition-function calculation.

Trivialize P locally as a right O-module, with transition units u_ij∈O*, and define Nrd(P) as the line whose transitions are Nrd(u_ij). After splitting O=End(V), the determinant transitions of P⊗_O V are det(u_ij) times those of V, giving the written determinant identity. Multiplicativity of reduced norm supplies the tensor-composition isomorphisms, and the ordinary associativity of multiplication supplies their coherence.

### D13 — For normal A, replacing the Azumaya open by its ring of functions can lose the excluded locus

**Kind:** own counterexample to an inference.  
**Witness:** 15/021:L24–25, continuing to 15/022:L3.  
**Brief quotation:** “A normal”; “C⊗_A Γ(U) se récupère”.  
**Context search and relation:** “normal | Γ(U) | Azumaya | extension” found no matching assertion in the supplied context; this **adds** a locality obstruction to the construction, beyond context/MPL_16+47+54+44_notes.md, cote 16/049.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no settled entry on this reconstruction.  
**Confidence/reason:** high; explicit finite torsion-free algebra and endomorphism comparison, expanded in Construction C.

Let A=k[x,y], I=(x,y), and O=End_A(A⊕I)=((A,A),(I,A)), a finite torsion-free algebra with generic fibre M_2(k(x,y)). Its Azumaya locus is U=A²−{0}, and Γ(U,O_U)=A, but O is not locally free at the origin: it has generic rank four and five minimal generators there. Consequently scalar extension to Γ(U) leaves O unchanged, whereas its splitting gerbe over U sees M_2(O_U); the displayed recovery requires an affineness assumption or a formulation using restriction as a category over U.

### D14 — The norm-one condition is necessary for an isomorphism-invariant trivialization

**Kind:** own verification with a scope restriction.  
**Witness:** 15/022:L10–28.  
**Brief quotation:** “N_red:O′*→A* … dans 1”; “Pic(A)=0”; “Φ∩A*={1}”.  
**Context search and relation:** “norm-one | norme | trivialisation” locates context/notes/RESULTS_STATE.md, SECTIONS_OVER_Q A.198, but only as an abbreviated claim without its proof; this **adds** a directly verifiable automorphism obstruction, not a proof of that separate generalized-Jacobian result. Nearest supplied scan comparison: context/same_cote_15/MPL_15_087-138_notes.md, T18, 15/135, on specified trivializations.  
**Register:** SECTIONS_OVER_Q A.198 [“Proved (the return’s claim)”]; MPL_15_087-138 §124 [first-pass lead].  
**Confidence/reason:** high on the groupoid of isomorphisms; D29 records the full-category obstruction.

If an automorphism u of P acts on Nrd(P) by Nrd(u), naturality of a trivialization with respect to that automorphism forces Nrd(u)=1. Under Pic(A)=0 and K*=ΦA* with Φ∩A*={1}, a principal norm ideal has a unique generator in Φ, because any two such generators differ by a unit in Φ∩A*. This gives the proposed multiplicative choice on invertible objects and their isomorphisms, but does not make reduced norms of arbitrary noninvertible morphisms equal to one.

### D15 — The definite quaternion case verifies the positivity argument

**Kind:** literature comparison / explicit consequence.  
**Witness:** 15/022:L23–31; 15/023:L12.  
**Brief quotation:** “A=Z”; “pas décomposé sur R”.  
**Context search and relation:** “positivité | norme | polarisation” locates context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, B03, scans 203, 215, 217; this **adds** a reduced-norm positivity argument, not the construction of a polarization in that broader Tannakian problem.  
**Register:** MPL_15_195-228+18_002-017 B03 [first-pass lead]; WG2 §2.3 #12 [unchecked plan].  
**Confidence/reason:** high for the definite quaternion example actually used on scan 023.

For a quaternion algebra over Q ramified at infinity, Hasse–Schilling gives Nrd(E*)=Q_{>0} (Voight, 2021, Main Theorem 14.7.4). Since Z*={±1}, the two conditions on Φ hold and each rational fractional ideal has a unique positive generator; norms of integral units are therefore one. This verifies the announced mechanism in the supersingular quaternion case, while keeping its functoriality restriction from D14.

### D16 — The supersingular example realizes the rank-one category, with a variance convention to retain

**Kind:** primary-source comparison / identification.  
**Witness:** 15/023:L5–14.  
**Brief quotation:** “D’après Deuring”; “degré 4 (corps de quaternions)”.  
**Context search and relation:** “supersingulier | Deuring | quaternion | Hasse” gives no matching category in the supplied context; this **adds** an explicit geometric realization beyond context/MPL_16+47+54+44_transcription.tex, cote 54/003–007, whose subject is p-kernels and Dieudonné-type structure.  
**Register:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 §3 [first-pass lead].  
**Confidence/reason:** high; precise modern theorem and its stated variance.

For a supersingular elliptic curve E_0 over an algebraically closed field of characteristic p, End(E_0) is a maximal order in B_{p,∞}, and E↦Hom(E_0,E) gives the covariant right-module version of Deuring’s correspondence. Voight (2021), Theorems 42.1.9 and 42.3.2 and Remark 42.3.3, provides exact statements; adjoining zero maps yields the preadditive formulation relevant here. The quaternion algebra has dimension four and degree two in modern terminology, so “degré 4” on this sheet should be annotated as a convention issue, not normalized.

### D17 — An invertible representation is a line; its scalar weight may be two

**Kind:** reading question with a mathematical incompatibility.  
**Witness:** 15/023:L14; compare 15/021:L17 and 15/022:L31.  
**Brief quotation:** “représentation inversible, T … de rang 2”.  
**Context search and relation:** “rang 2 | degré 1 | Tate” locates context/same_cote_15/MPL_15_087-138_notes.md, T06, scan 119, and T18, scan 135; this **differs** from their explicit separation of rank and degree and **adds** a determinant test.  
**Register:** MPL_15_087-138 §3 and §124 [first-pass leads].  
**Confidence/reason:** high for the mathematical incompatibility; no claim about the correct handwritten word.

An invertible object in the usual tensor category of locally free representations has rank one, since its rank multiplied by the rank of its inverse is one. For the rank-two weight-one splitting representation V, det(V) has rank one and weight two, because λ acts by λ². Thus “inversible … de rang 2” is inconsistent with literal vector-bundle rank, while weight/degree two fits the surrounding determinant construction; this is a research annotation only.

### D18 — A weight-d line reduces the band by taking its trivialization gerbe

**Kind:** own construction.  
**Witness:** 15/022:L31–15/023:L3 and L14.  
**Brief quotation:** “réduit à μ_n”.  
**Context search and relation:** “gerbe | Tate | restriction | munis d’un isom” locates context/same_cote_15/MPL_15_087-138_notes.md, T18–T18b, scan 135; this **restates** the principle of reducing a band by specified fibre data and **adds** its finite μ_d version.  
**Register:** MPL_15_087-138 §124 [first-pass lead].  
**Confidence/reason:** high; scalar automorphisms compute the kernel directly.

Given a G_m-gerbe and an invertible representation T of weight d, form pairs (ω,t), where ω is an object and t:ω(T)≅O is a chosen trivialization. Scalar λ preserves t exactly when λ^d=1, so the resulting gerbe is banded by μ_d, with local existence ensured in the fppf topology. This construction needs the line and its weight, not a rank-d invertible representation.

### D19 — The Tate determinant supplies an isomorphism of root gerbes, not a preferred square root

**Kind:** explanatory construction / scope clarification.  
**Witness:** 15/023, Tate-module paragraph and L31; 15/024, opening and margin.  
**Brief quotation:** “gerbe des racines carrées de A′(1)”; “pas … choisir une origine”.  
**Context search and relation:** “Tate | μ | Kummer” locates context/MPL_16+47+54+44_notes.md, 16:21:2, and context/same_cote_15/MPL_15_087-138_notes.md, T18, 15/135; this **adds** the square-root-gerbe construction and **restates** the need to distinguish a fibre isomorphism from a canonical choice.  
**Register:** MPL_15_087-138 §124 [first-pass lead].  
**Confidence/reason:** high; rank-two determinant and torsor definitions.

The Weil pairing associated with the elliptic curve’s canonical principal polarization gives det T_ℓ(E)≅Z_ℓ(1), explaining the determinant/Tate line in the comparison. An equivalence with the gerbe of square roots of that line does not choose an object of the gerbe or a distinguished trivialization: those choices vary by μ_2-torsors. This supports the sheet’s explicit warning that its torsor has no specified origin.

### D20 — The Kummer calculation is fppf when the prime two remains in the base

**Kind:** topology qualification / literature comparison.  
**Witness:** 15/024, H¹ displays; compare 15/023:L14.  
**Brief quotation:** “H^1(Z[1/p],μ_2)”; “Z_2*/Z_2*2”.  
**Context search and relation:** “Kummer | μ_2 | Tate” locates context/MPL_16+47+54+44_notes.md, 16:21:2–3; this **adds** the characteristic-two topology qualification to that earlier Tate/Kummer discussion.  
**Register:** MPL_15_087-138 §124 [first-pass lead]; no settled local-global calculation in the register.  
**Confidence/reason:** high; exact Kummer sequence with its explicit topology hypotheses.

If p is odd, Spec Z[1/p] still contains the prime two, so the squaring sequence with kernel μ_2 is exact for fppf sheaves but not generally for étale sheaves. Because Pic(Z[1/p])=0, it gives H¹_fppf(Z[1/p],μ_2)=Z[1/p]*/Z[1/p]*²≅(Z/2)², generated by p and −1. The relevant precise references are Stacks Project, Lemmas 59.28.1, 59.28.3, and 59.28.5, Tags 03PK, 040N, and 040Q.

### D21 — The single-factor quotient is not justified by the two-factor restriction map

**Kind:** reading question plus explicit counterexample to the displayed group size.  
**Witness:** 15/024, quotient Π/ρ(Z/2) and subsequent definition of ρ.  
**Brief quotation:** “Π/ρ(Z/2Z)”; inserted “×Z/2Z”.  
**Context search and relation:** “torseur | μ_2 | restrictions” locates context/same_cote_15/MPL_15_087-138_notes.md, T13, scan 123, where residual parity requires explicit data; this **adds** a different integral two-torsion calculation.  
**Register:** MPL_15_087-138 §3 and §124 [first-pass leads].  
**Confidence/reason:** high; p=3 gives an elementary calculation with no density theorem.

The written source of ρ has two generators, so quotienting by its image normally requires ρ((Z/2)²), not the single factor displayed earlier. For p=3, the images of p and −1 in Z_2*/Z_2*² are the classes of 3 and 7 modulo eight, and their product is 5, so the two images are independent. Thus no automatic collapse to one factor is available even in this simplest permitted case; an additional rigidification would have to be stated.

### D22 — A dyadic square class needs two coordinates

**Kind:** mathematical objection to a compressed formula, distinct from a reading doubt.  
**Witness:** 15/024, local factors and piecewise formula for ρ.  
**Brief quotation:** “Z/2Z×Z/2Z si ℓ=2”; “0 … 1 sinon”.  
**Context search and relation:** “carré | modulo 2 | μ_2” locates context/same_cote_15/MPL_15_087-138_notes.md, T13, scan 123; this **adds** a concrete instance in which a binary square/nonsquare test loses information.  
**Register:** MPL_15_087-138 §3 [first-pass lead].  
**Confidence/reason:** high; multiplication of odd residues modulo eight.

At odd ℓ, a unit square class has a single binary coordinate, but at ℓ=2 the four classes are represented by 1,3,5,7 modulo eight. Consequently “0 if square, 1 otherwise” cannot specify an element of the displayed dyadic group: for p=3 it assigns the same “1” to the distinct classes 3 and −1=7. The formula can record only whether a class is trivial unless a two-coordinate convention is added.

### D23 — The proposed real and crystalline rigidifications remain a construction claim

**Kind:** unproved claim / evidence limit.  
**Witness:** 15/024, final margin.  
**Brief quotation:** “éliminer ce groupe … polarisation … cristalline”.  
**Context search and relation:** “polarisation | réelle | cristalline | μ_2” locates context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, B03, 15/203, 215, 217, and context/same_cote_15/MPL_15_087-138_notes.md, T01–T09, 15/117–123; this **adds** a specific proposed two-torsion rigidification and does not establish those broader polarization claims.  
**Register:** MPL_15_195-228+18_002-017 B03 [first-pass lead]; WG2 §2.3 #12 [unchecked plan].  
**Confidence/reason:** high concerning what is and is not supplied on the sheet.

The margin proposes that real polarization and p-adic crystalline data remove the two residual global μ_2 freedoms, but gives neither the comparison maps nor their kernels. A proof would need to show how the classes of −1 and p act on those additional structures and why their simultaneous stabilizer is trivial. The supplied real-fibre discussions and Dieudonné context do not by themselves furnish that compatibility.

### D24 — The admissible-functor construction explains the formal base change, not preservation of maximality

**Kind:** construction clarification / own verification.  
**Witness:** 15/026, definition of admissibility; 15/028:L3–20.  
**Brief quotation:** “commute … P⊗_O X”; “Hom ad”; “O⊗_A A′→O′”.  
**Context search and relation:** “changement de base | foncteur | extension” finds no corresponding rank-one-module universal property in the supplied context; this **adds** a categorical base-change construction beyond context/MPL_16+47+54+44_notes.md, cote 16/049, and **differs** from the realization functors at context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, M01, 15/219 and 18/011.  
**Register:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 M01 [first-pass lead].  
**Confidence/reason:** high, with the manuscript’s tensor-existence and admissibility hypotheses.

After choosing X with O=End(X), the candidate base-changed category is P_1(O⊗_A A′), and an admissible functor is reconstructed by P↦P⊗_O X′ from X′ and its O-action. This explains the stated universal property and why an isomorphism on the displayed endomorphism algebras gives an equivalence of Deuring presentations. It does not establish that O⊗_A A′ remains a maximal order, which is a separate assertion tested on scan 030.

### D25 — Residue-changing finite étale base change really can destroy maximality

**Kind:** own verifying example.  
**Witness:** 15/030:L9.  
**Brief quotation:** “mais pas localisations étales !!”.  
**Context search and relation:** “étale | maximal | extension résiduelle” gives no corresponding order example in the supplied context; this **adds** a concrete justification to the warning, beyond context/MPL_16+47+54+44_notes.md, cote 16/049.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no matching settled entry.  
**Confidence/reason:** high; an explicit matrix embedding computes the base-changed order.

Use the order O of D05 and the finite étale extension B=Z_3[i] of A=Z_3. Under a↦diag(a,σ(a)) and Π↦((0,3),(1,0)), the algebra D⊗_K Q_3(i) splits, while O⊗_A B becomes the proper order ((B,3B),(B,B)) inside M_2(B). This verifies the warning for an étale extension that changes the residue field, and does not contradict the separately stated residue-preserving cases.

### D26 — A local ramified maximal order has a nontrivial invertible bimodule

**Kind:** own counterexample to the local π_0 claim.  
**Witness:** 15/030:L13.  
**Brief quotation:** “π_0=1”; “tt bimodule … est trivial”.  
**Context search and relation:** “bimodule | Brandt | Deuring | maximal” gives no matching local theorem in the supplied context; this **contradicts** the current displayed assertion under its own hypotheses and **adds** a distinct obstruction to the broad category programme at context/MPL_16+47+54+44_notes.md, 16:49:4.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no settled register claim is contradicted.  
**Confidence/reason:** high; full division, maximality, invertibility, and non-isomorphism checks are in Construction A.

For A=Z_3 and D=(Q_3(i)/Q_3,3), let O be its maximal order and J=ΠO=OΠ its radical. Then J is free of rank one on either side, J²=3O, and J is invertible as an O-bimodule, but a bimodule isomorphism O→J would send 1 to a central x∈Q_3 with valuation 1/2, which is impossible. Hence the group of isomorphism classes of autoequivalences contains an element of order two, even though A is local and D is central simple with centre K.

### D27 — Generic innerness does not imply innerness by an integral unit

**Kind:** explanation of the counterexample / scope of a valid replacement.  
**Witness:** 15/030:L13; compare 15/020:L9.  
**Brief quotation:** “E … de centre K”; “Mais il reste … A*”.  
**Context search and relation:** “automorphisme intérieur | centre | conjugaison” finds no matching integral argument in the supplied context; this **adds** the mechanism underlying D26, and **differs** from the group-automorphism ambiguity at context/same_cote_15/MPL_15_087-138_notes.md, L15, 15/135.  
**Register:** WG2 §2.4 #3 [unchecked plan]; LM1 A.8 [“Refuted (the return’s claim)”] is a separate issue.  
**Confidence/reason:** high; residue action separates the two innerness notions.

Conjugation by Π is inner over D but acts on O/J≅F_9 by its nontrivial Frobenius automorphism, whereas conjugation by a unit of O acts trivially on this commutative residue field. The failure is therefore integral and ramified, not a failure of generic central simplicity. Under the stronger hypothesis that O is Azumaya over local A, the appropriate A-linear invertible bimodules come from central invertible A-modules, and Pic(A)=0 removes this obstruction; that is a different hypothesis from the one actually written on scan 030.

### D28 — The universal norm category has an explicit model once a base object is chosen

**Kind:** own conditional construction of the requested universal object.  
**Witness:** 15/032:L2–18.  
**Brief quotation:** “Montrer … D universelle”; “V_A(C)”; “X fixé”.  
**Context search and relation:** “foncteur norme | universelle | déterminant” yields no equivalent universal norm category in the supplied context; this **adds** a construction beyond context/MPL_16+47+54+44_notes.md, cote 16/049. A distinct commutative norm comparison is Ferrand (1998), Theorem 3.2.3 and Proposition 3.3, not an identification of the two universality problems.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no settled universal-norm entry.  
**Confidence/reason:** high in the central Azumaya/maximal-order setting once the coherent reduced-norm line functor is specified; Construction D gives the precise hypotheses and maps.

Fix X and identify C≃P_1(O); the reduced-norm line functor N:P_1(O)→P_1(A), on all module maps, gives a model V_A(C)≃P_1(A). An admissible A-linear functor P_1(A)→D is determined by T_0=F(A) and sends L to L⊗_A T_0, exactly yielding the formula written on the sheet. Changing X changes this presentation by tensoring with its norm line, so a canonical presentation or section requires the additional coherent trivialization, rather than merely the existence of a base object.

### D29 — A constant norm object need not give a constant norm functor

**Kind:** mathematical objection / necessary distinction of morphism categories.  
**Witness:** 15/032:L4, L23–31 and L37; compare 15/022, functorial trivializations.  
**Brief quotation:** “pas additif!”; “isom fonctoriel”; uncertain “c^te v.l.”.  
**Context search and relation:** “fonctoriel | trivialisation | can.” locates context/same_cote_15/MPL_15_087-138_notes.md, T18, 15/135, on choice-sensitive trivializations; this **adds** a morphism-level obstruction.  
**Register:** MPL_15_087-138 §124 [first-pass lead]; SECTIONS_OVER_Q A.198 [“Proved (the return’s claim)”] is only a distinct norm-one-frame comparison.  
**Confidence/reason:** high; zero and multiplication by two give direct tests.

On the full preadditive category, reduced norm sends the zero endomorphism to zero, and in the quaternion example sends multiplication by two to four. Therefore Nrd(P) cannot be naturally isomorphic to the literally constant functor A that sends every morphism to the identity. The proposed trivializations can be natural on the invertible core, or can identify all norm objects with one line while retaining reduced-norm scalars on morphisms; these alternatives should be distinguished before interpreting the uncertain marginal abbreviation or the last canonical-object assertion.

### D30 — The independence margin is tentative, and its possible scopes must remain distinct

**Kind:** self-flagged / own examples for one precise reading.  
**Witness:** 15/016:L16, L20–21; compare 15/017, inserted unrestricted definition.  
**Brief quotation:** “a) est disjointe de b) et c)”; “vraisemblᵗ”; uncertain “indépendamment|indépendantes”.  
**Context search and relation:** “Deuring | indépendant | projectif | ordre maximal” finds no equivalent independence question in the supplied context; this **adds** a self-marked axiom question beyond context/MPL_16+47+54+44_notes.md, cote 16/049.  
**Register:** WG2 §2.4 #3 [unchecked plan]; no settled independence entry.  
**Confidence/reason:** high for the examples; the precise intended grammatical scope remains a reading doubt.

The margin tentatively separates the arithmetic order condition (a) from the rank-one presentation conditions (b,c), but its uncertain last word does not determine whether the author also meant independence between (b) and (c). For any A, the category P_1(A[ε]/ε²) satisfies the categorical presentation conditions while its generic algebra is not Azumaya, showing that they do not force (a). Conversely, take the one-object A-preadditive category with endomorphism ring A=Z[√−5]: condition (a) holds, but the nonprincipal invertible ideal (2,1+√−5) has no tensor object in that category, since such an object would require that ideal’s dual to be isomorphic to A. These examples separate (a) from the joint presentation conditions; they neither decide the uncertain handwriting nor establish an independence of (b) and (c), whose displayed functor already presupposes existence of the tensor objects.

## Explicit constructions supporting the notes

### Construction A — Ramified quaternion counterexample to 15/030

**Status:** own calculation, high confidence. The local order structure is also covered by Voight (2021), Proposition 13.3.4 and Theorem 13.1.6. The contradiction uses only a particular complete DVR, so questions about arbitrary Dedekind rings cannot remove it.

Let
\[
 A=\mathbf Z_3,\quad K=\mathbf Q_3,\quad
 L=K(i),\ i^2=-1,\quad B=A[i],
\]
and let σ(i)=−i. Since t²+1 is irreducible and separable over F_3, B/A is the unramified quadratic finite étale extension, with residue F_9. Define
\[
 D=L\oplus L\Pi,\qquad
 \Pi^2=3,\qquad \Pi a=\sigma(a)\Pi.
\]
Its centre is K. For x=a+bΠ,
\[
 \operatorname{Nrd}(x)=N_{L/K}(a)-3N_{L/K}(b).
\]
If both terms are nonzero, their 3-adic valuations are respectively 2v_L(a) and 1+2v_L(b), of different parity; hence they cannot cancel. If exactly one term is nonzero, it is nonzero. Thus every nonzero x has nonzero norm and is invertible by the standard conjugation formula, proving D is a central division quaternion algebra.

Define
\[
 w(x)=\frac12v_3(\operatorname{Nrd}x)
     =\min\{v_L(a),v_L(b)+\tfrac12\}.
\]
Multiplicativity of Nrd and the explicit minimum give the valuation identities. Its valuation ring and maximal ideal are
\[
 O=B\oplus B\Pi,\qquad
 J=3B\oplus B\Pi=\Pi O=O\Pi.
\]
The valuation ring is the unique maximal A-order: every element of an A-order is integral over A, and a monic relation for an element of negative valuation is impossible because its highest power has strictly smaller valuation than every other term. Hence every A-order lies in O; O itself is finite free of A-rank four.

Multiplication identifies J⊗_O J with J²=3O, and the central map 3O→O, 3a↦a, is a bimodule isomorphism. In particular J is invertible, with inverse Π^−1O, and is free of rank one as both a left and a right O-module.

Suppose f:O→J were an O-bimodule isomorphism. Then x=f(1) commutes with every element of O, hence with D=O⊗_A K, so x∈K. Surjectivity gives xO=J. The least finite valuation occurring in xO is w(x), while that occurring in J is 1/2, forcing w(x)=1/2. This contradicts w(K*)=Z. Equivalently, the norm valuation v_3(Nrd(x)) of a central nonzero x is 2v_3(x), which is even, whereas a generator of J has norm valuation one.

The endofunctor P↦P⊗_O J of P_1(O) is therefore an autoequivalence whose square is naturally isomorphic to the identity but which is not itself naturally isomorphic to the identity. Evaluation at O turns any hypothetical natural isomorphism into the forbidden bimodule isomorphism. Thus π_0 contains C_2.

The residue explanation is equally concrete: conjugation by Π induces a↦a³ on B/3B=F_9, while inner conjugation by any O-unit induces the identity on O/J. This identifies the precise gap between generic inner automorphisms and integral inner automorphisms.

### Construction B — The same example verifies the étale warning and the centre/Azumaya distinction

**Status:** own calculation, high confidence.

The quotient J/3O is a nonzero square-zero two-sided ideal of O/3O. Hence the special fibre is not central simple, although Z(O)=A, proving that centre=A does not imply Azumaya.

Over B, represent
\[
 a\longmapsto
 \begin{pmatrix}a&0\\0&\sigma(a)\end{pmatrix},
 \qquad
 \Pi\longmapsto
 \begin{pmatrix}0&3\\1&0\end{pmatrix}.
\]
Since B⊗_A B≅B×B, scalar extension of B supplies all diagonal matrices, and multiplication by Π supplies the remaining off-diagonal entries. Therefore
\[
 O\otimes_A B\simeq
 \left\{
 \begin{pmatrix}u&3v\\w&z\end{pmatrix}:u,v,w,z\in B
 \right\}
 \subsetneq M_2(B).
\]
This is an order in the split algebra M_2(L), properly contained in the order M_2(B), so it is not maximal. The extension is finite étale but changes the residue field from F_3 to F_9.

### Construction C — The Azumaya open and its global functions are different bases

**Status:** own calculation, high confidence.

Let A=k[x,y], I=(x,y), and M=A⊕I. Every A-linear map I→A is multiplication by an element of A: if f(x)=u and f(y)=v, the relation yu=xv and unique factorization imply u=xc and v=yc for c∈A. Hence Hom_A(I,A)=A and End_A(I)=A, so
\[
 O=\operatorname{End}_A(M)=
 \begin{pmatrix} A&A\\ I&A\end{pmatrix}
\]
as an A-module and algebra. Its A-module rank is four and O⊗_A K=M_2(K).

At every prime other than m=(x,y), the ideal I becomes the unit ideal, so O becomes M_2(A_p). At m, however,
\[
 \dim_k(O/mO)=3+\dim_k(I/mI)=3+2=5,
\]
whereas a locally free rank-four algebra would have a four-dimensional fibre. Thus the Azumaya locus is U=Spec(A)−{m}. Since A is a normal domain and the removed point has codimension two, Γ(U,O_U)=A; here it can also be checked directly as A_x∩A_y=A inside K.

On U, M|_U=O_U² and O|_U=M_2(O_U), so the splitting gerbe is neutral there. The object obtained by restricting the regular O-module has endomorphism ring Γ(U,O|_U)=M_2(A), whereas scalar extension of the original category to Γ(U,O_U)=A leaves its endomorphism ring O unchanged. This proves that the literal reconstruction by the ring of global functions is not automatic under the normal, finite, torsion-free hypotheses of scan 021.

### Construction D — A precise conditional model of V_A(C), including noninvertible maps

**Status:** own construction, high confidence under the stated central hypotheses. This gives a concrete route to the manuscript’s “Montrer”, rather than asserting a theorem for all finite semisimple algebras, arbitrary centres, or arbitrary target categories without further definitions.

Assume A is a domain, O is central Azumaya over A, or a finite maximal order in a central simple K-algebra for which the reduced norm takes O into A, and C=P_1(O). The latter integrality holds for an order over an integrally closed A: elements of O are integral, and reduced characteristic-polynomial coefficients lie in K and are integral over A.

For P∈P_1(O), choose local right-module trivializations. Their transition units define an invertible A-module N(P) by the reduced norm character O*→A*. If f:P→Q is any right O-module map, local trivializations identify it with left multiplication by a local element a∈O; define N(f) locally as multiplication by Nrd(a). Changing trivializations multiplies by the corresponding norm transitions, so these maps glue. Multiplicativity gives N(gf)=N(g)N(f), N(id)=id, and N(0)=0. This functor is generally not additive; for O=M_d(A), it is the determinant law.

Let P_1(A) denote invertible A-modules with all A-linear maps. For an A-preadditive target D in which L⊗_A T exists for invertible L, an admissible A-linear functor F:P_1(A)→D is determined by T=F(A), with
\[
 F(L)=L\otimes_A T,\qquad
 F(h)=h\otimes_A\operatorname{id}_T.
\]
The resulting N-followed-by-F is
\[
 \nu(P)=N(P)\otimes_A T.
\]
With norm structures and compatible natural transformations included, evaluation at the fixed base object O identifies the category of these norm functors with D. This is the universal property for this restricted target 2-category; therefore P_1(A) supplies a chosen-base-object model there. The manuscript's margin requires only tensoring by norm lines, which may be weaker than tensoring by every invertible A-module, so this argument does not settle its most general proposed target category.

For an intrinsic presentation, put
\[
 \mathcal N(Y,Z)
 =\operatorname{Nrd}_{\operatorname{End}(Y)/A}
       \bigl(\operatorname{Hom}_C(Y,Z)\bigr).
\]
Each is a line, because Hom_C(Y,Z) is locally rank one over End(Y). Reduced-norm composition gives coherent isomorphisms
\[
 \mathcal N(Z,W)\otimes_A\mathcal N(Y,Z)
 \simeq\mathcal N(Y,W).
\]
Form an A-preadditive category with objects (Y,L), where Y∈C and L is an invertible A-module, and
\[
 \operatorname{Hom}\bigl((Y,L),(Z,M)\bigr)
 =\mathcal N(Y,Z)\otimes_A\operatorname{Hom}_A(L,M).
\]
Use the displayed norm-composition maps for composition and send f:Y→Z to its reduced-norm section in \(\mathcal N(Y,Z)\). Fixing X identifies (Y,L) with N(Hom_C(X,Y))⊗L in P_1(A), proving the claimed presentation equivalence and its dependence on X. This construction retains the nonadditive norm action on morphisms and does not assert that the resulting norm functor is literally constant.

In a definite quaternion category, coherent positive generators can trivialize these lines on isomorphisms, but a nonzero isogeny still acts by its degree and the zero map acts by zero. This explains simultaneously the desired canonical object and the obstruction to the strongest possible reading of “constant”. No proof is supplied here for arbitrary semisimple centres or for the manuscript's general base-change compatibility claim.

## Source register and exact locators

Only brief source-specific statements are attributed above; the longer displayed counterexamples and constructions are independently worked calculations.

1. Baez, J. C., & Lauda, A. D. (2004). Higher-dimensional algebra V: 2-groups. *Theory and Applications of Categories, 12*, 423–491. **§8.3, Theorem 43 and Corollary 44** give the group, coefficient group, action, and H³ class; Proposition 45 discusses strictification. Author preprint, exact text verified: https://arxiv.org/pdf/math/0307200 . Web retrieval IDs available to the parent: turn22view0, turn31view2. The source supports the modern comparison, not a historical identification with this manuscript.

2. Ferrand, D. (1998). Un foncteur norme. *Bulletin de la Société Mathématique de France, 126*(1), 1–49. https://doi.org/10.24033/bsmf.2319 . Exact primary PDF: https://www.numdam.org/article/BSMF_1998__126_1_1_0.pdf . **Theorem 3.2.3, pp. 19–20**, gives a universal norm functor for a finite locally free commutative algebra; **Proposition 3.3, p. 22**, treats invertible modules. This is a comparison for norm functoriality, not a theorem identifying Ferrand’s functor with the manuscript’s noncommutative reduced-norm category. Retrieval IDs: turn22view1, turn41view0.

3. The Stacks Project Authors. (2026). *The Brauer group of a scheme* (Section 59.62, Tag 0A2J). https://stacks.math.columbia.edu/tag/0A2J . Opening definitions separate Azumaya algebras from their Brauer equivalence classes; **Lemma 59.62.1** treats endomorphism-algebra isomorphisms and line twists; **Lemma 59.62.2** states the degree annihilation bound for an Azumaya algebra of rank d². Retrieval ID: turn15view1.

4. The Stacks Project Authors. (2026). *Kummer theory* (Section 59.28, Tag 03PK). https://stacks.math.columbia.edu/tag/03PK . **Lemma 59.28.1** requires n invertible for the étale statement; **Lemma 59.28.3**, https://stacks.math.columbia.edu/tag/040N , gives the general fppf statement; **Lemma 59.28.5**, https://stacks.math.columbia.edu/tag/040Q , identifies H¹ with line bundles equipped with a trivialization of their nth tensor power. Retrieval IDs: turn21search3, turn21search4, turn21search5.

5. Voight, J. (2021). *Quaternion algebras* (Graduate Texts in Mathematics, Vol. 288). Springer. https://doi.org/10.1007/978-3-030-56694-4 .
   - **Chapter 13, Theorem 13.1.6; Proposition 13.3.4; Theorem 13.3.11; Corollary 13.3.14**: local division algebra, unique maximal valuation order, radical and residue field, and matrix realization. Exact publisher full text: https://link.springer.com/chapter/10.1007/978-3-030-56694-4_13 . Retrieval IDs: turn15view2, turn27view1.
   - **Chapter 14, Main Theorem 14.7.4**: Hasse–Schilling reduced-norm image for quaternion algebras. https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14 . Retrieval IDs: turn31view1, turn41view5.
   - **Chapter 42, Theorems 42.1.9 and 42.3.2, Remark 42.3.3, Corollary 42.3.7**: supersingular endomorphism order and the category equivalence, with its variance. https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42 . Retrieval IDs: turn31view0, turn41view2, turn41view4.
   The author’s full PDF was too large for the web parser; the exact publisher chapter texts were opened and checked instead.

## Bounded search report

The complete supplied research register was read with its status warnings. Searches of the supplied context text files for “Deuring”, “Brandt”, “bimodule”, “Azumaya”, “norme réduite”, and “Nrd” found no earlier directly matching Deuring construction; “Azumaya” chiefly located the Brauer/Brauer-prime distinction at cote 16/021. Targeted searches for “gerbe”, “Giraud”, “foncteur fibre”, “Tate”, “determinant”, “norm-one”, “centre”, “μ_2”, “Kummer”, and “polarisation” found the specific scan comparisons cited above. A separate text search of context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf for “Deuring | supersingular | quaternion | Azumaya | gerbe | reduced norm” found a Deuring bibliography entry, but no matching categorical construction under those terms; that bounded search does not exclude an implicit relationship elsewhere in the paper.

The supplied context supports comparisons with cote 16/021 (Tate and Kummer), 16/049 (motive/semisimplicity programme), 54/003–007 (p-kernel/Dieudonné structures), cote 15/117–135 (real fibre functors, gerbes, ranks, Tate reduction), and cote 15/203–219 plus 18/011 (polarized and realized categories). These are bounded conceptual links; none supplies an already settled proof of scan 030 or the full unqualified universality on scan 032. No claim concerning Galois reconstruction, period conjectures, or a general category of motives is resolved by the calculations here.

