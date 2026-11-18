## D. Divided derivatives and characteristics 2 and 3

The mathematical interpretation checked in this section is explicit: \(A\) is a commutative \(\mathbb F_p\)-algebra, \(q=p\) for \(p>3\), \(q=4\) for \(p=2\), and \(q=9\) for \(p=3\); \(B=A[t]/(t^q-\alpha)\). For \(s\in B\), the conditions are that \(D^{(1)}s\) is a unit and \((D^{(2)}s)^2=D^{(1)}sD^{(3)}s\). The result checked is a fractional-linear expression with unit determinant and unit denominator, unique up to a common unit scalar, assuming \(\operatorname{Pic}(A)=0\); the zero-parameter case needs no Picard hypothesis, and D14 removes it for all parameters when p is odd. This is a stated mathematical interpretation of doubtful formulas, not a repair of the frozen transcription.

The complete elementary proof, including descent, is in **documentation/research_checks/integral_schwarzian_check.md**. The accompanying **integral_certificate.py** and **integral_certificate.txt** contain exact symbolic identities and finite-ring checks. Those finite examples support the proof but are not a substitute for its arbitrary-ring argument.

### D01 — The integral invariant is defined without dividing by 12

**File/location:** cote 93, scan 121, middle and lower displays; scan 122 opening. **Kind:** unproved claim.

“\(G(t,s)=12G_0(t,s)\)” has the integral interpretation \(G_0=((D^{(2)}s)^2-D^{(1)}sD^{(3)}s)/(D^{(1)}s)^2\,dt^2\), using only invertibility of the first derivative. Thus \(G_0\) exists even where 12 is zero, while \(G/12\) is only shorthand after inverting 12. The displayed notation \(D^{(n)}=(1/n!)d^n/dt^n\) must likewise be understood through Taylor coefficients, not literal division by \(n!\) in small characteristic.

**Context:** Restates and checks H-IX, pp. 120–121/scans 121–122, and bears directly on H-FIND; earlier P01 fixes the characteristic-zero normalization only.
**Context query:** facteur.*12|G_0|divis|Taylor
**Check:** computation or formal certificate || integral_certificate.txt verifies G=12G0 as a rational identity; the Hasse-coefficient definition itself is integral.

### D02 — A polynomial identity proves the refined cocycle

**File/location:** cote 93, scans 120–122, cocycle and “s'étendent à \(G_0\)”. **Kind:** own idea. **Confidence:** high, because the calculation is an identity over \(\mathbb Z\).

If \(a,b,c\) are the first three Taylor coefficients of \(s\), and \(A,B,C\) those of \(r\) relative to \(s\), then \(r_1=Aa\), \(r_2=Ab+Ba^2\), \(r_3=Ac+2Bab+Ca^3\). Expanding gives \(r_2^2-r_1r_3=A^2(b^2-ac)+a^4(B^2-AC)\), which proves the differential-valued cocycle after only the first derivatives are inverted. This checks the universal identity without cancelling 2, 3, or 12.

**Context:** Independently checks the identity reported in H-IX, pp. 120–121/scans 121–122, and H-FIND; Hua's named Lean artifacts were neither supplied nor rerun.
**Context query:** cocycle|N_comp|G0_comp|intégral
**Check:** computation or formal certificate || integral_certificate.py expands the universal Z-polynomial identity to zero; coordinate descent is a separate geometric step.

### D03 — Collapse of the ordinary torsor is not collapse of the refined one

**File/location:** cote 93, scan 121, “toutes les connexions… sont égales”. **Kind:** unpursued implication.

When \(12=0\), the coordinate sections \(c_t\) of the ordinary torsor coincide, so they define its canonical section by gluing. The refined \(G_0\) can still be nonzero, and the pushout by multiplication by 12 loses that information. This assertion concerns the two Schwarzian torsors and is not a p-curvature computation.

**Context:** Restates H-IX, p. 120/scan 121, and H-FIND; bears on earlier P05 and P06 precisely by limiting what may be inferred from a vanishing expression.
**Context query:** 12.*nul|canonique|Conn_0|courbure|nilpot
**Check:** targeted proof check || Pushout of a torsor by the zero endomorphism has a canonical section; the explicit nonzero refined invariants in D05 distinguish the torsors.

### D04 — The relevant constants are relative Frobenius constants

**File/location:** cote 93, scan 122, upper margin defining \(\mathcal O'_X\). **Kind:** unproved claim.

In \(A[t]\), the common kernel of \(D^{(1)},D^{(2)},D^{(3)}\) is \(A[t^p]\) for \(p>3\), \(A[t^4]\) for \(p=2\), and \(A[t^9]\) for \(p=3\). Comparing monomials proves this even when \(A\) has nilpotents, because every nonzero coefficient from \(\mathbb F_p\) is a unit in \(A\). Over an imperfect base, this is a relative constant algebra retaining all base coefficients, not necessarily the set of absolute pth or p-squared powers.

**Context:** Independently checks H-IXp, p. 121/scan 122, and H-FIND; the distinction complements the earlier package's cautions about relative and perfect-base constructions.
**Context query:** O'_X|Frobenius|constantes|p\\^2|parfait
**Check:** independent re-proof || Binomial coefficients detect the first one or two base-p digits; the coefficient argument works over arbitrary Fp-algebras.

### D05 — First-level constants are insufficient for the refined invariant

**File/location:** cote 93, scans 121–122, Frobenius action and the \(p>3\) qualification. **Kind:** own idea. **Confidence:** high, by direct Hasse differentiation; the examples are credited to Hua.

H-IXp's examples \(s=t+t^2\) in characteristic 2 and \(s=t+t^3\) in characteristic 3 give \(G_0=dt^2\) and \(-dt^2\), respectively, although the added terms are killed by \(D^{(1)}\). They show why the first-level Frobenius constants do not preserve \(G_0\) and why the first three Hasse derivatives must all be considered. In the finite models, taking \(q>3\) also makes those three operators well defined on \(A[t]/(t^q-\alpha)\).

**Context:** Rechecks and credits H-IXp, p. 121/scan 122, and H-FIND; does not contradict D03, which concerns the ordinary \(G\).
**Context query:** t.*t.*2|char_two|char_three|p\\^2
**Check:** computation or formal certificate || Hasse coefficients of t+t² and t+t³ give the stated constants; first-level invariance for G0 is refuted, refined statement D04.

### D06 — The derivative orders remain a reading question

**File/location:** cote 93, scan 122, definition of \(c_0\) and following equality. **Kind:** reading question.

The frozen reading marks doubtful 2/3 orders and includes an equality beginning with a squared third divided derivative, whereas scan 123 and H-IXp use \((D^{(2)}s)^2=D^{(1)}sD^{(3)}s\). The latter is the condition proved in D07–D10, because it is the numerator of the \(G_0\) defined on scan 121. Mathematical coherence therefore supplies a precise question for a future image reading, not permission to change the frozen orders.

**Context:** Differs from H-IXp, pp. 121–122/scans 122–123, at the doubtful derivative orders; explicitly limits which interpretation of H-FIND has been checked.
**Context query:** D.*3|D.*2|c_0|injectivit
**Check:** used and rechecked in this run || Compared the frozen formulas on 121–123 and the contextual modernization; retained the transcription and stated the proved interpretation separately.

### D07 — The local rigidity argument survives nilpotents

**File/location:** cote 93, scans 123–124, normalization and the least nonzero coefficient. **Kind:** own idea. **Confidence:** high, by an explicit linear coefficient argument.

For \(\alpha=0\), normalize by homographies to \(s=t\bmod t^3\), and let \(h t^d\) be the first remaining term. The coefficient of \(t^{d-3}\) in \((D^{(2)}s)^2-D^{(1)}sD^{(3)}s\) is \(-h\binom d3\), and \(\binom d3\) is a unit in all required ranges, forcing \(h=0\). The proof therefore does not make the invalid inference from \(h^2=0\) to \(h=0\), and it establishes local rigidity over nonreduced \(A\) without any Picard hypothesis.

**Context:** Independently checks the local conclusion of H-IXp, pp. 122–123/scans 123–124, and H-FIND; relates to earlier MPL_93_002-046 E12's warning about nilpotent test objects.
**Context query:** rigidity|nilpotent|binom|coefficient|E12
**Check:** independent re-proof || Complete coefficient induction in integral_schwarzian_check.md §3; finite-ring enumeration is supplementary, not the arbitrary-ring proof.

### D08 — The cancelled characteristic-3 branch is replaced

**File/location:** cote 93, scan 124, deleted calculation and surviving right-hand argument. **Kind:** withdrawn in the same text.

The long cancelled \(p=3\) branch is replaced by the digit/binomial argument ending “On gagne encore !”. For \(d=3,4,5,6,7,8\), the surviving coefficient \(\binom d3\) is \(1,1,1,2,2,2\) modulo 3, so the linear induction in D07 applies throughout. This validates the replacement step without rehabilitating the crossed-out argument.

**Context:** Agrees with H-IXp, p. 123/scan 124, and checks the precise small-prime step highlighted by H-FIND.
**Context query:** gagne|Lucas|binom|p=3|caractéristique.*3
**Check:** computation or formal certificate || integral_certificate.txt records the complete six-entry coefficient list modulo 3; the manuscript's surviving proof is the one used.

### D09 — Picard triviality does not imply determinant one

**File/location:** cote 93, scan 122, “avec \(ad-bc=1\)”. **Kind:** unproved claim.

The determinant-one conclusion is false even for \(A=\mathbb F_5\): Hua's counterexample \(s=2t\) in \(A[t]/t^5\) has vanishing refined Schwarzian and invertible derivative. Comparing \(2t(ct+d)=at+b\) gives \(b=c=0\), \(a=2d\), so the determinant is \(2d^2\), never 1 for a unit \(d\). The correct statement requires the determinant to be a unit; this correction is credited to Hua and independently checked here.

**Context:** Confirms H-IXp's explicit correction, p. 121/scan 122, and refines the statement underlying H-FIND; it is not a new discovery claimed by this run.
**Context query:** ad-bc|det_one|2t|déterminant
**Check:** computation or formal certificate || integral_certificate.py enumerates all 5⁴ matrices and finds four invertible solutions, none of determinant one; refined statement D10.

### D10 — Faithfully flat descent fills the general-parameter gap

**File/location:** cote 93, scan 123 opening, reduction to \(\alpha=0\). **Kind:** own idea. **Confidence:** high, by the local proof and descent of a rank-one module.

Pass to the faithfully flat algebra \(A'=A[u]/(u^q-\alpha)\), where \(z=t-u\) satisfies \(z^q=0\), and apply D07. The kernel \(K\) of \(A^4\to B,\ (a,b,c,d)\mapsto s(ct+d)-at-b\) becomes a free line over \(A'\), because every solution is a scalar multiple of the normalized matrix; by finite-projective descent [B7], \(K\) is an invertible \(A\)-module. If \(\operatorname{Pic}(A)=0\), a generator descends the matrix, and its determinant and denominator are units because they become units after faithful flat base change.

**Context:** Supplies a proof of the reduction left unchecked in H-IXp, pp. 122–123/scans 123–124, and strengthens the checked form of H-FIND without a novelty claim.
**Context query:** alpha|Pic\\(A\\)|réduction|descente
**Check:** independent re-proof || integral_schwarzian_check.md §4 proves the kernel becomes a free line and descends; Stacks tag058S was read for the finite-projective descent step.

### D11 — Matrix uniqueness means one common scalar

**File/location:** cote 93, scan 122, inserted “transformation diagonale”. **Kind:** unpursued implication.

After the root extension used in D10, coefficient comparison in \(1,z,z^2\) shows that all matrix solutions form a single free line, including noninvertible solutions. Its invertible generators differ by one common unit scalar, so arbitrary independent diagonal row or column changes are not the intended ambiguity. The Picard hypothesis trivializes that line; the proof establishes its sufficiency here, not its necessity in every possible formulation.

**Context:** Clarifies H-IXp, p. 121/scan 122, and the matrix issue in H-FIND; related but distinct from the literal quotient wording on scan 117, C03.
**Context query:** transformation.*diagon|scalaire|Pic\\(A\\)|PGL
**Check:** targeted proof check || The transformed relation c z²+(d-a)z-b=0 gives b=c=0 and d=a since q≥4; generators of a line differ by a unit.

### D12 — Modern small-characteristic literature does not settle priority

**File/location:** cote 93, scans 121–124, contextual comparison. **Kind:** own idea. **Confidence:** high for the checked distinction of constructions; no claim of novelty.

Hoshi's 2024 paper [B8, Definition 6.2 and Remark 6.4.2] uses a level-one invariant that collapses for \(p\le3\), while its §3 treats level-two projective structures in characteristic 2 through locally exact differentials. This supports Hua's distinction from the quadratic-differential-valued \(G_0\) on scan 121. It does not establish that the manuscript construction is new, that the two constructions are unrelated, or that all possible Cartier and p-curvature comparisons have been made.

**Context:** Checks the literature distinction made by H-IX, pp. 120–123/scans 121–124, and preserves H-FIND's candidate status; earlier P06/P09 remain limits on the proposed arithmetic connection.
**Context query:** Hoshi|Sugiyama|Yasuda|Wakabayashi|nouveau
**Check:** used and rechecked in this run || Read the cited primary-paper definitions and remark; no exhaustive novelty search or global equivalence theorem claimed.

### D13 — Deligne's normalization is a close characteristic-zero comparison

**File/location:** cote 93, scan 121, \(G_0\); scans 133–134, third jets. **Kind:** own idea. **Confidence:** high for the normalization comparison, not a dating or priority inference.

Deligne [B2, I, (5.9.2)] writes the projective difference as \(\theta(f)=(f'''/(6f')-(f''/(2f'))^2)\,dt^2\), so in these conventions \(\theta=-G_0=-G/12\) in characteristic zero. This gives a published comparison joining the third-jet construction and the divided-coefficient expression. It does not by itself establish the arbitrary-base or small-characteristic assertions of D04–D10, and it supplies no date for these physical manuscript sheets.

**Context:** Adds a precise comparison to H-IX and H-Xb, beyond H-FIND's candidate description; earlier P01 fixes the other normalization needed for the comparison.
**Context query:** Deligne|facteur.*12|jets|normalisation
**Check:** used and rechecked in this run || Read Deligne I5.9.2 and its statement that 6theta is the classical Schwarzian; direct substitution gives theta=-G0.

### D14 — In odd characteristic, the Picard hypothesis can be removed in this model

**File/location:** cote 93, scan 122, \(\operatorname{Pic}(A)=0\); scan 123, reduction to \(\alpha=0\). **Kind:** own idea. **Confidence:** high, by a determinant argument applied to the solution line already constructed.

The line \(K\) in D10 has \(K^{\otimes2}\simeq A\) because the determinant of a local generator is a unit, and its denominator gives \(K\otimes_A B\simeq B\). Since \(B\) is free of rank \(q\) over \(A\), taking determinants of the latter isomorphism gives \(K^{\otimes q}\simeq A\); when \(q\) is odd, these two trivializations force \(K\simeq A\). Thus the matrix conclusion of this specific truncated-algebra theorem holds without \(\operatorname{Pic}(A)=0\) for odd \(p\), while the argument gives no such removal for \(p=2\) and does not permit determinant-one normalization.

**Context:** Adds a refinement to H-IXp and H-FIND, whose stated sufficient hypothesis is Picard triviality; no supplied context asserts this refinement, and no novelty claim is made.
**Context query:** Pic\\(A\\)|déterminant|scalaire|p=2
**Check:** independent re-proof || Determinant trivializes K²; denominator and determinant of the rank-q A-module B trivialize K^q; coprime exponents 2 and q trivialize K.
