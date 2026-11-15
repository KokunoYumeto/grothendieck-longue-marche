# Research memo: reused algebra sheets, cote 60 scans036–070

Prepared after the transcription freeze; no scan image was opened by this research agent and no frozen page, combined transcription, or doubts file was edited. The page quotations below refer to the frozen transcription and remain subject to its explicit reading doubts. The typed sheets are reused source material: an exercise request is not evidence that Grothendieck was personally conjecturing its statement at the time he wrote the L-function notes.

## Context and register scope

`context/MPL_16+47+54+44_transcription.tex` is abbreviated **CT**, and `context/MPL_16+47+54+44_notes.md` **CN**. Searches are preserved in `records/algebra_context_search.json`; CT contains no match for reflexive/réflexif or pseudo-nul, but **CT cote16 scan052** is a direct and important match for Fitting ideals, differents, annihilator bounds, monogenicity and ramification. **CT cote16 scans054–056** discusses étale algebras and flat descent, **CT cote54 scans004–006** generic flatness, and **CT cote44 scan003** contains a cancelled discussion of completion and flatness. These are textual comparisons, not assertions that the first-pass contextual readings have been reviewed.

No supplied settled/open RESULTS_STATE entry directly settles the commutative-algebra statements below. In particular **LM7 E.23** concerns section classes and **LM7_PUSH D.44** modular descent, so neither should be cited as evidence for a Fitting, reflexivity or monogenicity theorem. The applicable planning entry **WG2 §2.4 #3** bears only on scope: these sheets supply commutative algebra, not a construction of a category of motives from Lefschetz correspondence rings. The first-pass lead **MPL_15_195-228+18_002-017 R01** makes a comparable distinction for reused Lie-theory material; it is a methodological parallel, not a proof of anything here. The notes below therefore record “no direct result ID” where appropriate instead of forcing a false mathematical connection.

## Draft research items

### A01 — Hensel factorization lacks a necessary hypothesis in the frozen wording

**Witness:** `MPL_60_036-070_60_scan038.tex`, line10 (exercise15), with the Hensel hint at line12. **Kind:** reading question; own idea (counterexample). **Quote:** “on ait \(\overline P=\overline Q.\overline R\)” and “appliquer ensuite le lemme de Hensel”. **Context search:** `Hensel|complet|étale|résiduel`; CT16/054–056. **Relation:** adds a limitation to the context’s lifting programme, rather than contradicting a fully stated context theorem. **RESULTS_STATE:** no direct result ID; WG2 §2.4 #3 only for scope.

As written in the frozen transcription, take \(A=\mathbb Z_p\), \(K=\mathbb Q_p\), one variable, \(P=X^2-p\), \(Q=R=X\), and \(s=1\): all displayed assumptions hold, including splitting into linear factors over \(K'=\mathbb Q_p(\sqrt p)\), but the demanded degree-one factorization over \(A\) would give an element of \(K\) of valuation \(1/2\). The ordinary factorization form of Hensel’s lemma requires coprime reduced factors (Stacks Project Authors, 2026, Tag04GG, Lemma10.153.3(3)–(6)), absent from this frozen wording. This is a reason to seek an omitted condition or an antecedent convention in the underlying typed source, not to add one to the transcription. **Confidence: high**, because the example checks every displayed hypothesis and the valuation obstruction is immediate.

### A02 — Quotient Fitting inclusion runs in the opposite direction

**Witness:** `MPL_60_036-070_60_scan064.tex`, lines8,22–24 (10a,f). **Kind:** reading question; own idea (counterexample). **Quote:** “\(\underline d_k(M/N)\subset\underline d_k(M)\)”. **Context search:** `Fitting|Filting|Ann`; CT16/052, nos.1–2; CN16:52:1 and R14. **Relation:** adds an explicit higher-ideal definition to the context and contradicts the quotient inclusion as transcribed; it does not contradict the context’s annihilator bound. **RESULTS_STATE:** no direct result ID.

The definition \(d_k(M)=c_{n-k}(R)\) identifies \(d_k\) with the usual \(\operatorname{Fitt}_k\), for which a surjection \(M\twoheadrightarrow M/N\) gives \(d_k(M)\subseteq d_k(M/N)\) (Stacks Project Authors, 2026, Tag07ZA(5)). For a nonzero nonunit \(a\) in a domain, \(M=A\), \(N=aA\), \(k=0\) yields \(d_0(M)=0\) and \(d_0(M/N)=(a)\), directly refuting the displayed reverse inclusion. The following convolution inclusion in line24 is a separate statement and should not be rejected merely because the preceding inclusion is reversed. **Confidence: high**, from the one-generator presentations.

### A03 — Fitting ideals give a precise answer to the earlier annihilator outline

**Witness:** `MPL_60_036-070_60_scan064.tex`, lines6–20 (10a–e). **Kind:** unpursued implication. **Quote:** “\(\underline d_0(M)\subset\underline a\)” and “\(\underline a^{r-k}\subset\underline d_k(M)\)”. **Context search:** `Fitting|Filting|Ann`; CT16/052, no.1; CN16:52:1 and R14. **Relation:** restates the earlier bound at \(k=0\), and adds the whole determinantal sequence and direct-sum convolution. **RESULTS_STATE:** no direct result ID.

With \(r\) a number of generators and \(\mathfrak a=\operatorname{Ann}(M)\), the new exercise specializes to \(\mathfrak a^r\subseteq d_0(M)\subseteq\mathfrak a\), making the earlier “une de ses puissances” explicit. The zeroth-ideal convention also clarifies the older phrase “premier idéal de Filting” without resolving the context’s separate use of \(A^p\to A^q\) for a \(B\)-module. The presentation-independent construction, direct-sum formula and annihilator inclusion agree with Stacks Tags07Z8 and07ZA; none of this proves the broader finite-presentation conjecture about differentials in CN16:52:2.

### A04 — Local generator bounds do not produce a global generator

**Witness:** `MPL_60_036-070_60_scan064.tex`, line12 (10c). **Kind:** own idea (explicit exercise example). **Quote:** “donner un exemple où \(r_0<r\)”. **Context search:** `Dedekind|Fitting|annulateur`; CT16/052. **Relation:** adds a global obstruction not addressed in the earlier Fitting outline. **RESULTS_STATE:** no direct result ID.

In \(A=\mathbb Z[\sqrt{-5}]\), take the invertible ideal \(I=(2,1+\sqrt{-5})\); locally it has rank one, so \(d_1(I)=A\), whereas its norm is2 and no element has norm2, hence \(I\) is not principal and needs two generators. Thus \(r_0=1<2=r\), distinguishing local Fitting information from the global ideal class (compare Stacks Tags07ZA and0AUW). **Confidence: high**, because nonprincipality reduces to \(a^2+5b^2=2\), which has no integer solution.

### A05 — A free submodule can have a torsion-free, nonreflexive quotient

**Witness:** `MPL_60_036-070_60_scan046.tex`, line6; `MPL_60_036-070_60_scan064.tex`, line4. **Kind:** unpursued implication. **Quote:** “n’est pas nécessairement ... réflexif” and “le noyau ... libre monogène”. **Context search:** `réflex|reflex|pseudo-nul` has no CT match; the nearest flatness discussion is CT54/004–006. **Relation:** supplies the concrete example promised on046; differs from the context’s flatness questions. **RESULTS_STATE:** no direct result ID.

For \(A=k[X,Y]\), the kernel of \((a,b)\mapsto aX+bY\) is \(A(-Y,X)\), while the quotient is \((X,Y)\). Its dual is \(A\), hence its double dual is \(A\), and the natural inclusion \((X,Y)\hookrightarrow A\) is not onto. This gives a local codimension-two defect at the origin, consistent with the characterization of reflexive modules by their height-one localizations (Stacks Project Authors, 2026, Tag0AVB), and makes precise what the reduction theorem does not preserve.

### A06 — The reflexivity exercise needs a nonzero source module

**Witness:** `MPL_60_036-070_60_scan068.tex`, lines7–11 (*2). **Kind:** reading question; own idea (counterexample). **Quote:** “On suppose que \(E\) est sans torsion” and “Montrer alors que \(F\) est réflexif”. **Context search:** `réflex|reflex|Hom|Ext`; no corresponding reflexivity assertion in CT. **Relation:** adds a missing-hypothesis test; no direct context theorem is contradicted. **RESULTS_STATE:** no direct result ID.

The literal hypotheses allow \(E=0\), in which case \(\operatorname{Hom}(E,F)=0\) is reflexive and \(\operatorname{Ext}^1(E,F)=0\) for every \(F\), including \(F=A/(a)\) for a nonzero nonunit \(a\), which is not reflexive. A condition \(E\ne0\), equivalently positive rank under the stated domain and torsion-freeness hypotheses, removes this immediate obstruction and makes the indicated associated-prime argument viable. **Confidence: high**, since the zero-module test is independent of any modern comparison; it does not authorize inserting \(E\ne0\) in the frozen text.

### A07 — A bounded family of reflexive lattices has a finite intersection witness

**Witness:** `MPL_60_036-070_60_scan068.tex`, line5 (exercise1). **Kind:** own idea. **Quote:** “une famille quelconque ... contenant toutes un même réseau \(N\)”. **Context search:** `réflex|réseau|intersection`; no matching lattice theorem in CT; CT16/014–015’s integral correspondence algebra is a different use of a lattice. **Relation:** adds a finite-generation consequence to the current exercise; differs from the integral Lefschetz setting. **RESULTS_STATE:** WG2 §6. #9 only as a distinction, not as a claim to settle its integral-operator problem.

Inside the dual vector space, \(S=\sum_\lambda M_\lambda^*\) lies in the finite module \(N^*\), so noetherianity makes \(S\) equal to a sum of finitely many \(M_\lambda^*\). Dualizing yields \(\bigcap_\lambda M_\lambda=S^*\), and therefore the intersection already equals the intersection of a finite subfamily. The common full lattice is essential: \(\bigcap_{n\ge0}X^n k[X]=0\) has no such lower lattice and no finite intersection witness. **Confidence: high**, from duality and noetherian finite generation.

### A08 — The Veronese example measures the exact torsion lost under extension

**Witness:** `MPL_60_036-070_60_scan066.tex`, lines4–8 (exercise6). **Kind:** own idea (explicit computation). **Quote:** “un module de torsion \(\ne0\)” and “n’est pas injective”. **Context search:** `plat|changement d’anneau|torsion`; CT16/056 and CT54/004–006. **Relation:** adds a finite nonflat example to the context’s descent discussion; realizes the warning on current052. **RESULTS_STATE:** no direct result ID.

Writing \(A=k[u,v,w]/(uw-v^2)\), \(u=X^2,v=XY,w=Y^2\), the ideal \(\mathfrak p=(u,v)\) has syzygies \((-v,u)\) and \((-w,v)\), so \(\mathfrak p\otimes_A B\cong B^2/(X,Y)(-Y,X)\). Its map to \(\mathfrak pB=X(X,Y)\) has kernel \(B(-Y,X)/(X,Y)(-Y,X)\cong B/(X,Y)\), while \((\mathfrak pB)^{**}=XB\). Thus both the torsion kernel and the failure of divisoriality are concentrated in codimension two and invisible to height-one divisor calculations. **Confidence: high**, from the displayed presentation; no restriction on the characteristic of \(k\) is needed.

### A09 — Flat extension preserves reflexivity; finite extension alone does not

**Witness:** `MPL_60_036-070_60_scan052.tex`, line7; `MPL_60_036-070_60_scan066.tex`, lines4–8. **Kind:** unpursued implication. **Quote:** “Il en est toutefois ainsi lorsque \(B\) est un \(A\)-module plat”. **Context search:** `plat|changement d’anneau`; CT16/056 and CT54/004–006. **Relation:** adds a specific module property to the context’s general flatness programme. **RESULTS_STATE:** no direct result ID.

The remark separates the flat case from merely finite normal extensions, and066 gives an explicit failure of the latter. The modern preservation statement is precisely Stacks Tag0EB9, Lemma15.24.7, for a flat map of noetherian domains and a finite reflexive module. It should not be confused with the different assertion on058 that restriction of scalars along the given finite normal extension detects reflexivity.

### A10 — Restriction of scalars uses the height-one intersection, not tensor exactness

**Witness:** `MPL_60_036-070_60_scan058.tex`, lines6–12; `MPL_60_036-070_60_scan056.tex`, lines4–8. **Kind:** unpursued implication. **Quote:** “\((R_{[A]})_{\underline p}=\bigcap_{\underline P\mid\underline p}R_{\underline P}\)”. **Context search:** `réflex|intersection|plat`; no direct CT reflexivity theorem. **Relation:** differs from CT16/056’s flat descent and adds a separate finite-normal-extension mechanism. **RESULTS_STATE:** no direct result ID.

The proof works by expressing a torsion-free module as the intersection of its height-one lattices and regrouping the primes above each \(\mathfrak p\), not by claiming that \(B\) is globally flat over \(A\). Stacks Tags0AVB–0AVC supply the modern intersection criterion, while Tag0BM4 confirms the special case that the finite integral closure itself is reflexive over the normal base. The missing opening hypotheses of the reused source must be kept in view before extending the statement to arbitrary finite ring maps.

### A11 — Base change is exact only after ignoring higher-codimension defects

**Witness:** `MPL_60_036-070_60_scan056.tex`, lines10–31; `MPL_60_036-070_60_scan054.tex`, lines4–18; `MPL_60_036-070_60_scan052.tex`, line5. **Kind:** unpursued implication. **Quote:** “le noyau ... est pseudo-nul”. **Context search:** `pseudo-nul|plat|changement`; CT16/056 is the nearest base-change passage, with no pseudo-null theorem. **Relation:** adds a weaker form of exactness than flatness; differs from faithfully flat descent. **RESULTS_STATE:** no direct result ID.

At each height-one prime of a normal noetherian domain the local ring is a DVR, and the finite torsion-free extension module is free there, so tensoring preserves injections at those primes. Consequently the defect can survive in codimension at least two, exactly as the \(B/(X,Y)\) kernel on066 shows, while the divisor and first-class formulas remain valid. The proof on054 refers to “lemme4” where the immediately relevant injectivity-defect statement is labelled “LEMME5” on056; this is an internal-reference question, not grounds to renumber the transcription. The local freeness step agrees with Stacks Tag0AUW.

### A12 — Ramification and residue degree act in opposite divisor directions

**Witness:** `MPL_60_036-070_60_scan054.tex`, line14; `MPL_60_036-070_60_scan060.tex`, line8; `MPL_60_036-070_60_scan052.tex`, lines9–16. **Kind:** unpursued implication. **Quote:** “\(\sum_{\underline P\mid\underline p}e_{\underline P/\underline p}.\underline P\)” and “sa longueur ... \(f_{\underline P/\underline p}\)”. **Context search:** `ramification|différente|trace`; CT16/052, nos.3–5. **Relation:** adds explicit divisor pullback/norm formulas to the different-and-trace outline, but does not prove the context’s different-transitivity equality. **RESULTS_STATE:** no direct result ID.

The typed pages distinguish pullback, weighted by ramification indices \(e\), from norm/restriction, weighted by residue degrees \(f\), and052 records the corresponding transitivity orders. This is useful when checking whether later formulas confuse a residue-field degree with a ramification index. These are divisor-group statements; they are not the local Euler characteristics denoted by a visually similar \(\chi\) in the handwritten L-function pages.

### A13 — Hom–tensor reflexivity is a projectivity test

**Witness:** `MPL_60_036-070_60_scan066.tex`, lines10–14 (exercise7). **Kind:** unproved claim (exercise); unpursued implication. **Quote:** “\(E^*\otimes_A E\longrightarrow\operatorname{End}_A(E)\)” and “soit ... réflexif”. **Context search:** `End|Hom|libre`; CT16/003–015 concerns graded endomorphism rings, a different setting. **Relation:** differs from the correspondence-ring programme; adds a finite-module test. **RESULTS_STATE:** WG2 §2.4 #3 only to prevent conflation with motivic rigidity.

The evaluation map is an isomorphism in height one because \(E\) is free over the corresponding DVRs, hence is a pseudo-isomorphism. If its source is reflexive, comparing it to the reflexive hull of \(\operatorname{End}(E)\) makes evaluation surjective, so the identity endomorphism is a finite sum of rank-one maps and supplies a dual basis proving projectivity. This is a module-theoretic analogue of dualizability, but the page alone supplies no tensor-category or motivic-fibre-functor construction.

### A14 — The Tor and Ext terms are essential for the divisor identities

**Witness:** `MPL_60_036-070_60_scan066.tex`, lines16–35 (*8). **Kind:** unpursued implication. **Quote:** “se ramener au cas où \(A\) est principal” and the three \(\chi\)-identities. **Context search:** `Tor|Ext|groupe de Grothendieck`; CT16/035 introduces a Grothendieck group, while CT16/037–041 discusses derived Hom. **Relation:** adds a codimension-one Euler-characteristic calculation; does not identify the divisor class with the context’s categorical Grothendieck group. **RESULTS_STATE:** no direct result ID.

Over a DVR, test \(M_1=A/(\pi^a)\) and \(M_2=A^r\oplus A/(\pi^b)\): the tensor and first-Tor lengths are \(ar+\min(a,b)\) and \(\min(a,b)\), giving \(ar\), while the Hom/Ext length differences in the two orders are respectively \(-ar\) and \(+ar\). These computations check the signs in066 and show why simply discarding \(\operatorname{Tor}_1\) or \(\operatorname{Ext}^1\) would fail. Higher Tor/Ext disappear after height-one localization because a DVR has length-one finite free resolutions for its finite torsion modules; this is the content needed for the pseudo-null assertions, not global vanishing in higher dimension.

### A15 — A concrete cyclotomic realization of the finite-field monogenicity obstruction

**Witness:** `MPL_60_036-070_60_scan062.tex`, line4 (exercise7d). **Kind:** own idea (construction). **Quote:** “partir d’une extension cyclotomique de \(Q\)”. **Context search:** `monog|étale`; CT16/052 and054; CN R6 and R7. **Relation:** adds an arithmetic realization of the already noted \(\mathbb F_2^3\) obstruction, rather than presenting that obstruction as new. **RESULTS_STATE:** no direct result ID; CN R6/R7 remain first-pass leads.

Let \(A=\mathbb Z_{(2)}\) and let \(L\) be the unique cubic subfield of \(\mathbb Q(\zeta_{31})\). Since2 has order5 modulo31, its Frobenius lies in the subgroup of order10 fixing \(L\), so2 splits completely in \(L\) and the integral closure \(B\) has \(B/2B\cong\mathbb F_2^3\) (Milne,2020, §8.16 and Example8.18, pp.142–143). A monogenic \(B=A[x]\) would give a monogenic residue algebra, impossible because one element with three coordinates in \(\mathbb F_2\) cannot separate all three factors. **Confidence: high**, from the order calculation and residue-algebra obstruction; this respects the noncomplete DVR hypothesis rather than incorrectly claiming such a split algebra is a DVR over the complete base.

### A16 — Cyclic differentials and a monogenic algebra are different requirements

**Witness:** `MPL_60_036-070_60_scan062.tex`, lines4–6 (7d and8a). **Kind:** unpursued implication. **Quote:** “\(B\) ne soit ... \(A[x]\)” and “\(\Omega_A(B)\) ... engendré par \(\mathrm dx\)”. **Context search:** `monog|différente|Omega_A`; CT16/052, nos.2–4; CN R7,R14,R16. **Relation:** adds the distinction needed to assess the earlier monogenicity outline. **RESULTS_STATE:** no direct result ID.

The juxtaposition separates global monogenicity of \(B\) from cyclicity of its differential module, even when the same notation \(x\) is used for a generator. In the preceding unramified cyclotomic example, \(B\) is not monogenic while \(\Omega_{B/A}=0\), so a generator of differentials cannot be promoted to a generator of the algebra. The Kähler different remains the zeroth Fitting ideal of \(\Omega_{B/A}\) (Stacks Project Authors,2026, Tag0BVW), and the exercise8a is therefore relevant to its presentation without settling every trace-comparison hypothesis in CT16/052.

### A17 — A separable extension with a non-simple purely inseparable residue extension

**Witness:** `MPL_60_036-070_60_scan062.tex`, line8 (8b). **Kind:** own idea (construction); reading question for “corps des fractions \(K\) de \(L\)”. **Quote:** “radicielle non monogène” and “\(\Omega_A(B)\) n’est pas monogène”. **Context search:** `monog|différente|résiduel`; CT16/052, CN R14–R16. **Relation:** adds an explicit two-generator differential example to the context. **RESULTS_STATE:** no direct result ID.

Take \(k=\mathbb F_p(s,t)\), \(A=k[[\pi]]\), and \(B=A[\alpha,\beta]/(\alpha^p-\pi\alpha-s,\,\beta^p-\pi\beta-t)\); its reduction modulo \(\pi\) is the field \(k(s^{1/p},t^{1/p})\) of degree \(p^2\), so this finite free local \(A\)-algebra has principal maximal ideal \((\pi)\) and is a DVR. Its fraction-field extension is separable, since both defining polynomials have nonzero derivative \(-\pi\), whereas its residue extension has exponent one and degree \(p^2\), hence cannot be simple. The differential presentation gives \(\Omega_{B/A}\cong(B/\pi B)^2\), which is not cyclic, and its zeroth Fitting ideal is \((\pi^2)\), agreeing with the Jacobian formula in Stacks Tag0BVZ. **Confidence: high**, from the finite free presentation and explicit differential matrix; the anomalous phrase “\(K\) de \(L\)” is left untouched.

### A18 — Pseudo-null need not mean zero outside the Dedekind case

**Witness:** `MPL_60_036-070_60_scan046.tex`, lines10–24; `MPL_60_036-070_60_scan068.tex`, line21. **Kind:** own idea (example). **Quote:** “Tout ... pseudo-nul est nul” and “donner un exemple où il n’est pas nul”. **Context search:** `pseudo-nul|torsion|Dedekind`; CT16/052 only matches the different setting, not pseudo-null modules. **Relation:** adds a dimensional distinction absent from the supplied context. **RESULTS_STATE:** no direct result ID.

For \(A=k[x,y]\), \(M=A/(x-y)\), \(\mathfrak a=(x)\), \(\mathfrak b=(y)\), the quotient in068 is \(xk[x]/x^2k[x]\cong k\), supported at the codimension-two maximal ideal \((x,y)\), hence nonzero and pseudo-null. Over a Dedekind domain there are no such positive-codimension-two supports, explaining046’s collapse of pseudo-isomorphisms to isomorphisms and its equivalence of finite torsion-free, reflexive and projective modules (compare Stacks Tag0AUW). **Confidence: high**, by the direct quotient calculation.

### A19 — Torsion components need not split over a higher-dimensional normal ring

**Witness:** `MPL_60_036-070_60_scan068.tex`, lines15–19 (4a,b). **Kind:** unpursued implication. **Quote:** “n’est pas somme directe”. **Context search:** `torsion|somme directe`; CT16/021’s cohomological torsion discussion concerns another category. **Relation:** differs from the context’s cohomological torsion and adds an explicit module warning. **RESULTS_STATE:** no direct result ID.

The quotient \(A/(XY)\) retains the intersection point of its two components: the natural map to \(A/(X)\oplus A/(Y)\) has cokernel \(A/(X,Y)\), so the tempting direct-sum decomposition loses a codimension-two term. This explains why height-one or divisor data can suggest a split form while the module itself remains glued. The exercise4a asks for an analogous failure of splitting off the torsion submodule, and neither failure contradicts the one-dimensional Dedekind decomposition results.

### A20 — Generic unit-ideal certificates require the vertical checks

**Witness:** `MPL_60_036-070_60_scan070.tex`, line4 (exercise26). **Kind:** unpursued implication. **Quote:** “pour tout élément extrémal \(p\) ... divisant \(d\)”. **Context search:** `contenu|idéal|annulateur`; CT16/052’s “Lien avec le contenu” is the nearest textual match. **Relation:** adds an explicit denominator-localization test, without proving the context’s Fitting assertions. **RESULTS_STATE:** no direct result ID.

After clearing denominators in \(\sum v_if_i=1\), the ideal \(I=(f_i)\) contains \(d\); any maximal ideal containing \(I\) must therefore contain some prime factor \(p\mid d\). The additional condition \(I+(p)=B\) excludes each such maximal ideal and proves \(I=B\), showing precisely why generic solvability alone does not suffice. The gcd normalization organizes the certificate but should not be confused with a general claim that checking arbitrary codimension-one localizations detects every ideal.

### A21 — Factoriality is neither automatic under completion nor geometric base change

**Witness:** `MPL_60_036-070_60_scan040.tex`, lines8–16; `MPL_60_036-070_60_scan042.tex`, lines4–6; `MPL_60_036-070_60_scan044.tex`, lines4–6. **Kind:** unpursued implication. **Quote:** “dont le complété ... non factoriel” and “mais ... n’est pas factoriel”. **Context search:** `factoriel|complété|plat`; CT44/003 has the cancelled completion-flatness discussion. **Relation:** differs from flatness and adds a warning against inferring factoriality from that property. **RESULTS_STATE:** no direct result ID.

The reused exercises exhibit both directions of change under \(\mathbb Q\subset\mathbb Q(i)\): the circle algebra on044 becomes factorial, while the conic algebra on042 ceases to be factorial. Separately040 asks for a factorial local noetherian ring with a nonfactorial completion, so even a flat completion map cannot itself justify preservation of factoriality. These are explicit commutative-algebra constructions, not evidence for a conjectural motivic descent principle.

### A22 — Infinite ideal-class groups from the characteristic-two construction

**Witness:** `MPL_60_036-070_60_scan036.tex`, lines11–15 (25). **Kind:** own idea (specialization, conditional on the exercise). **Quote:** “un espace vectoriel sur \(k\) de dimension \(N(i,j)\)” and “groupe des classes d’idéaux ... infini”. **Context search:** `Dedekind|torsion|classes`; CT16/052 concerns differents, not this class-group construction. **Relation:** adds a characteristic-two class-group example, with no direct corresponding context theorem. **RESULTS_STATE:** no direct result ID.

At \(i=j=2\), the displayed lattice-point condition selects only \((a,b)=(1,1)\), so \(N(2,2)=1\). If \(k\) is infinite of characteristic two, the asserted embedding therefore produces an infinite elementary2-torsion subgroup of the class group, which survives the indicated localization to the Dedekind ring \(A'\). **Confidence: high for the lattice-point calculation and conditional implication**; proving the claimed embedding still requires the earlier exercises23–24 and resolving the role of \(L,L'\), whose notation is not fully introduced in this excerpt.

### A23 — The formal power series ring appears as a completed cyclic group algebra

**Witness:** `MPL_60_036-070_60_scan038.tex`, line8 (exercise14). **Kind:** unpursued implication. **Quote:** “l’algèbre ... du groupe \(G_n=Z/p^nZ\)” and “\(\varprojlim A_n\)”. **Context search:** `complété|groupe|limite`; CT44/003 has completion but not this cyclic inverse limit. **Relation:** adds a distinct completion construction. **RESULTS_STATE:** no direct result ID.

The substitution \(g=1-T\) identifies the finite quotients with the cyclic group algebras, and the inverse-limit assertion is the completed-group-algebra pattern for \(\mathbb Z_p\). To justify surjectivity, one needs completeness of \(A[[T]]\), closedness of the ideals \((\gamma_n)\), and the fact that \(\gamma_n\) tend to zero in the maximal-ideal topology; the assertion is not a consequence of the intersection being zero alone. This is a formal algebraic parallel to later uses of completed group rings, without a claim of historical influence on the handwritten L-function argument.

### A24 — The intersection counterexample and the tensor counterexample use the same ring

**Witness:** `MPL_60_036-070_60_scan040.tex`, line22 (exercise11); `MPL_60_036-070_60_scan066.tex`, lines4–8. **Kind:** own idea (cross-page identification). **Quote:** “\(A\cap L\) n’est pas factoriel” and “\(k[X^2,XY,Y^2]\)”. **Context search:** `factoriel|torsion|plat`; no corresponding CT ring example. **Relation:** adds an internal link between the current reused sheets; differs from CT54/004–006’s generic-flatness programme. **RESULTS_STATE:** no direct result ID.

For a field \(k\), \(k[X,Y]\cap k(X^2,Y/X)=k[X^2,XY,Y^2]\): splitting a polynomial into its even- and odd-total-degree parts and using the basis \(1,X\) of \(k(X,Y)\) over \(k(X^2,Y/X)\) proves the equality in every characteristic. Its irreducible degree-two elements satisfy \((XY)^2=X^2Y^2\), giving the nonunique factorization requested on040. Thus066’s failure of flatness and reflexive scalar extension occurs over the same normal, nonfactorial ring already constructed on040. **Confidence: high**, from the explicit field basis and grading argument; this identifies the algebra, not a historical borrowing between the sheets.

## Exact primary references and retrieval record

All sources below were opened in the web tool; root should open the relevant URLs itself before citing a subagent retrieval in the final response. Retrieval date: November15,2026. No retrieved source was used to alter the transcription.

| Reference | Exact content used | Tool retrieval reference |
|---|---|---|
| Stacks Project Authors. (2026). *Lemma10.153.3: Characterizations of henselian local rings* (Tag04GG). https://stacks.math.columbia.edu/tag/04GG | Parts(3)–(6) require gcd1 for reduced factorization lifting. | turn25view0 |
| Stacks Project Authors. (2026). *Lemma15.8.2: Fitting ideals* (Tag07Z8). https://stacks.math.columbia.edu/tag/07Z8 | Presentation-independent minors definition. | turn32view0 |
| Stacks Project Authors. (2026). *Lemma15.8.4* (Tag07ZA). https://stacks.math.columbia.edu/tag/07ZA | Direct sums, arbitrary scalar extension, surjection inclusion, annihilator inclusion, cyclic quotient ideal. | turn3view0; turn2search1 |
| Stacks Project Authors. (2026). *Lemma15.22.11: Torsion-free modules* (Tag0AUW). https://stacks.math.columbia.edu/tag/0AUW | Over a Dedekind domain, finite torsion-free modules are finite locally free; over a PID they are free. | turn20view2 |
| Stacks Project Authors. (2026). *Section15.24: Reflexive modules* (Tag0AUY). https://stacks.math.columbia.edu/tag/0AUY | Lemma15.24.7 flat base change; Lemma15.24.8 reflexivity of Hom into a reflexive module; related finite-module facts. | turn3view2 |
| Stacks Project Authors. (2026). *Lemma15.24.7* (Tag0EB9). https://stacks.math.columbia.edu/tag/0EB9 | Flat base change preserves finite reflexive modules over noetherian domains. | turn32view1 |
| Stacks Project Authors. (2026). *Lemma15.24.18* (Tag0AVB). https://stacks.math.columbia.edu/tag/0AVB | Reflexive iff torsion-free and S2 iff height-one intersection, for finite modules over normal noetherian domains. | turn17view3 |
| Stacks Project Authors. (2026). *Lemma15.24.19* (Tag0AVC). https://stacks.math.columbia.edu/tag/0AVC | Reflexive hull is intersection of torsion-free height-one localizations. | turn3view1 |
| Stacks Project Authors. (2026). *Lemma15.24.20* (Tag0BM4). https://stacks.math.columbia.edu/tag/0BM4 | Finite integral closure in a finite field extension is reflexive over the normal noetherian base. | turn17view2 |
| Stacks Project Authors. (2026). *Definition49.7.1* (Tag0BVW). https://stacks.math.columbia.edu/tag/0BVW | Kähler different equals zeroth Fitting ideal of the differential module. | turn17view0 |
| Stacks Project Authors. (2026). *Lemma49.7.4* (Tag0BVZ). https://stacks.math.columbia.edu/tag/0BVZ | Square polynomial presentation gives the Jacobian determinant for the Kähler different. | turn17view1 |
| Milne, J. S. (2020). *Algebraic number theory* (Version3.08). https://www.jmilne.org/math/CourseNotes/ANTc.pdf | §8.16 and Example8.18, printed pp.142–143: Frobenius restriction and cyclotomic Frobenius. Version/date confirmed on title page and official landing page. | turn20view1; turn21view0; turn22view0; landing page turn20view0 |

## Checks and cautions for synthesis

- A01, A02 and A06 give three independent literal-statement counterexamples; classify them as research questions/counterexamples, not transcription corrections.
- A15 adds the cubic-field realization to CN R6/R7, which already contains the elementary finite-field obstruction. Do not present that older obstruction as a newly discovered result.
- A17 has \(B\) a genuine complete DVR; A15 has \(A\) a noncomplete DVR and \(B\) a semilocal integral closure. Conflating these settings would invalidate the example.
- A08's torsion is exactly \(k\), so it concretely illustrates the pseudo-null correction in A11 rather than merely giving another nonflatness warning.
- The “lemme4” references on054, the apparent extra prime on \(a_k\) on064, the field-name wording on062, and the overloaded \(L\) on036 are reading questions only. The frozen text must remain unchanged.
- Routine “Montrer que” exercises are unfinished proofs in the reused source, but not necessarily author-marked doubts; the standing self-flagged section should not inflate them into Grothendieck’s personal conjectures.
