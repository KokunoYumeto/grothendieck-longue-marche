from pathlib import Path
import json

P=Path(__file__).parent
items=[]
HVI='`context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074)'
HVG='`context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084)'
HIX='`context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied)'
HX='`context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied)'
R='`context/notes/RESULTS_STATE.md`'
PRE='`context/same_cote_93/MPL_93_002-046_notes.md`'
NONE=f'{R}: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead'
HUA=f'{R}: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled'

def add(title,scan,quote,kind,comment,ctx=None,confidence='High for the stated check; it uses the displayed formula or an explicit local argument.',event='targeted proof check',outcome=None):
    sid=f'SC{len(items)+1:02}'
    if ctx is None: ctx=(HVI if int(scan.split('–')[0])<=74 else HVG)+'; '+NONE
    items.append(dict(id=sid,title=title,scan=scan,quote=quote,kind=kind,comment=comment,context=ctx,confidence=confidence,event=event,outcome=outcome or title))

add('Existence of the analytic projective invariant','072',r'Il existe un morphisme','unproved claim',
    r'The displayed formula on 073 supplies this existence assertion: its coordinate compatibility follows from the chain identity in C1, and its analytic local properties from C3. The theorem is announced here without a proof; checking this example does not establish the subsequent uniqueness statement.',HVI+f'; {PRE}, P01 (scan 036); {R}: **MPL_93_002-046 P01**',outcome='Verified the announced existence for the displayed invariant using C1–C3; uniqueness separate.')
add('The proposed denominator restriction','072',r'On doit pouvoir montrer que','self-flagged / unproved claim',
    r'In a universal polynomial jet algebra over a field, a reduced denominator whose zero set is contained in the union of the two first-derivative divisors is a unit times a product of their powers. Applying that algebraic fact to the stated analytic condition requires a jet-realization argument and care about coefficients varying on U; no proof of that passage is supplied here, so the bracketed claim remains conditional.',event='carried as background without fault found',confidence='Medium: the algebraic lemma is straightforward, but the analytic-to-universal hypothesis is not proved here.',outcome='Conditional algebraic interpretation recorded; full denominator assertion not promoted.')
add('The additive cocycle equation','072',r'G(f,g)+G(g,h)=G(f,h)','unproved claim',
    r'For the formula on 073 the equality is literal cancellation of the middle Q-term, with no characteristic restriction for G₀. This is distinct from the coordinate-composition identity needed to make those differences quadratic differentials; C1 verifies both.',event='computation or formal certificate',outcome='Exact three-jet computation plus telescoping verifies displayed cocycle.')
add('Invariance under the three generators','072',r'G(f,1/g)=G(f,g)','unproved claim',
    r'Translation, nonzero scaling and inversion are constant homographies, and their integral Q vanishes by C1. The unit and nonvanishing conditions in the page are essential domains of definition, not cosmetic exceptions.',event='computation or formal certificate',outcome='Verified integral homography jets and chain identity; domains retained.')
add('Rigidity from equality of the two-jet','072',r'coïncident à l’ordre $2$','unproved claim',
    r'In the complex analytic setting the local Schwarzian equation gives a unique solution with prescribed value, first derivative and second derivative, and analytic continuation gives the stated connected-domain equality. This is the C3 local ODE argument; it must not be transferred unchanged to positive characteristic.',HVI+f'; {PRE}, P01/P04 (scan 036); {R}: **MPL_93_002-046 P01**; no settled positive-characteristic rigidity entry')
add('Uniqueness up to a nowhere-zero function','072',r'G’=\varphi G','unproved claim',
    r'The asserted classification concerns all admissible nonlinear rational differential operators, not only two copies of the displayed formula. Our computations do not prove that classification; the distinction matters because arbitrary additive differential operations would preserve a cocycle but can destroy rigidity or local surjectivity.',event='carried as background without fault found',confidence='Medium: the claim is plausible in the full analytic hypotheses; classification was not re-proved.',outcome='Full operator classification remains unverified in this run.')
add('Descent from affine to projective coordinates','072',r'c) implique que $G$ se descend','unproved claim',
    r'Two affine charts of the projective line differ by the allowed constant homographies, so C1 allows G to glue on projective étale coordinates and descend in both arguments. The uncertain handwritten group abbreviation is not resolved by this mathematical identification; PGL₂ is the group used in the check.')
add('Opposite torsor-difference conventions','072–073',r'G(f,g)=c(f)-c(g)','reading question',
    r'The margin on 072 uses c(f)−c(g), while the principal equation on 073 uses c(g)−c(f). Either convention can define a torsor after changing the sign of its action, but using them together without that adjustment reverses later differences; both readings remain frozen.',outcome='Compared the two displayed signs; recorded convention conflict, no transcription correction.')
add('The quotient map is claimed to be injective','072',r'est mono','unproved claim',
    r'Equality of projective connections first gives a constant Möbius transformation locally; after matching the two-jet, condition d) kills the remaining transformation. This supplies the analytic quotient-level injectivity for the displayed invariant, rather than injectivity of the map on raw coordinates.',HVI+f'; {PRE}, P03 (scan 036); {R}: no matching settled quotient theorem')
add('Local surjectivity of the Schwarzian equation','072',r'est un épi','unproved claim',
    r'C3 solves the prescribed analytic Schwarzian equation locally by a ratio of two independent solutions of a linear second-order ODE. The word “épi” is a sheaf-local assertion; it neither gives a global single-valued solution on every open set nor algebraic étale-local surjectivity in every characteristic.',HVI+f'; {PRE}, P04 (scan 036); {R}: no matching settled surjectivity theorem')
add('Functoriality reduces the scalar ambiguity','072',r'c\in\mathbb C^{*}','unproved claim',
    r'If the fixed-curve uniqueness assertion has first been established, a scalar natural for every étale coordinate chart restricts from one scalar on the affine line and is invariant under translations, hence is constant. This verifies the reduction from an already existing φ to a constant, not the missing classification of operators.',outcome='Conditional naturality argument checked; depends on SC06.')
add('The margin says e) may be omitted','072',r'il suffit de supposer d)','self-flagged / unproved claim',
    r'For the displayed nonzero Schwarzian, e) follows from the analytic ODE, but the margin purports to deduce it for every operator in the classification. That stronger redundancy depends on the unproved uniqueness argument and has not been independently established here.',event='carried as background without fault found',confidence='Medium: true for the explicit invariant, classification-dependent for all operators.',outcome='Recorded marginal strengthening; no general proof claimed.')
add('Universal constant coefficients in the jet expression','073',r'des coefficients $\in\mathbb C$','unproved claim',
    r'Compatibility with all charts and translations accounts for independence of the base point, but uniqueness of a rational jet presentation is needed to conclude the exact universal coefficient statement. The sentence is read in the variable-X context of II; a single fixed curve with arbitrary holomorphic coefficients would not justify it.',event='carried as background without fault found',confidence='Medium: contextual naturality explains the intended statement but no full presentation theorem was checked.')
add('Normalization relative to the classical Schwarzian','073',r"-2\frac{g'''}{g'}+3\left(\frac{g''}{g'}\right)^2",'unpursued implication',
    r'This is −2 times the classical Schwarzian, agreeing with the earlier scan 036 and P01. C2 rechecks the normalization so that comparisons with ODEs, exponentials and the later factor 12 use the same sign.',HVI+f'; {PRE}, P01/P04 (scan 036); {R}: **MPL_93_002-046 P01**',event='used and rechecked in this run')
add('The canonical torsor and quotient isomorphism','073',r'ce dernier morphisme est un iso','unproved claim',
    r'Transition differences from C1 glue local affine spaces of quadratic differentials into a torsor, and the analytic local injectivity and surjectivity in SC09–SC10 identify the orbit sheaf with it. “Canonical” does not supply a canonical global point; a projective connection is a choice of section.',HVI+f'; {PRE}, P01/P03 (scan 036); {R}: **MPL_93_002-046 P01**, no matching settled global torsor construction')
add('Divided derivatives in the relative problem','073',r'il faut maintenant remplacer','unproved claim',
    r'Hasse derivatives are the coefficients of the Taylor expansion, so their definitions use no factorial inverses. C1 verifies the necessary third-order composition identities on an étale coordinate chart over an arbitrary commutative base; writing D⁽ⁿ⁾ as (1/n!)dⁿ is only a characteristic-zero mnemonic.',HVI+'; '+HIX+'; '+HUA,event='independent re-proof')
add('Integral coefficients are asserted by naturality','073',r'les coefficients doivent être dans $\mathbb Z$','unproved claim',
    r'The particular formula has integral coefficients in the localized universal Hasse-jet algebra, as C1 shows directly. The stronger claim that every natural operator admits exactly the stated integral presentation belongs to the proposed classification and is not proved merely by that example.',HVI+'; '+HUA,event='carried as background without fault found',confidence='High for the explicit formula; medium for the unproved general representation statement.')
add('The integral cocycle exists over every base','073',r'On trouve encore l’existence','unproved claim',
    r'C1 proves an integral polynomial identity before any localization and proves the corresponding Q identity where the first jets are units. Thus the stated G₀ formula is a coordinate-independent quadratic-differential cocycle in characteristics 2 and 3 as well; this verifies the formula-level part of Hua’s candidate, not every universal property attached to it.',HVI+'; '+HIX+'; '+HUA,event='independent re-proof')
add('The uniqueness up to sign is a separate claim','073',r'unicité au signe près','unproved claim',
    r'The observation that the units of ℤ are ±1 explains the asserted normalization only after uniqueness up to a universal unit has been proved. C1–C2 establish existence and normalization, not this classification of all natural operators.',HVI+'; '+HUA,event='carried as background without fault found',confidence='Medium: a logical dependency is identified; the general classification remains unverified.')
add('The classical invariant vanishes in characteristics 2 and 3','073',r'identiquement nulle en car. $2$ et $3$','unproved claim',
    r'This follows from the integral identity G=12G₀, not from replacing integer denominators by illegal inverses. In characteristic 2 the ordinary second derivative vanishes, and in characteristic 3 the ordinary third derivative vanishes while the remaining coefficient is 3.',HVI+'; '+HIX+'; '+HUA,event='computation or formal certificate')
add('Meaning of the notation G divided by 12','073',r'prendre $\frac1{12}G(f,g)$','unproved claim',
    r"C2 verifies G=12G₀ over the integers after substituting f''=2D⁽²⁾f and f'''=6D⁽³⁾f. Over a base where 12 is not invertible, the displayed Hasse formula defines G₀ independently; division by the already zero G cannot recover it.",HVI+'; '+HIX+'; '+HUA,event='computation or formal certificate')
add('Nonvanishing in small characteristics','073',r'non identiquement','unproved claim / marginal nonvanishing condition',
    r'The margin’s nonzero condition is realized by G₀(t,t+t²)=dt² in characteristic 2 and G₀(t,t+t³)=−dt² in characteristic 3, where the first derivatives are 1. These examples are checked in C2 and C9 and also explain why ordinary derivatives lose information.',HVI+'; '+HIX+'; '+HUA,event='computation or formal certificate')
add('The squared-coordinate normalization test is wrong as printed','073',r'\frac1{2t}dt^2','own idea / reading question',
    r'Direct Hasse differentiation gives G₀(t,t²)=dt²/(4t²), whereas the final frozen text gives dt²/(2t). Hua’s modernised reading makes the same mathematical correction, but it is a research correction to the value, not evidence for replacing the frozen glyphs.',HVI+' (footnote on the two tests); '+HUA,event='refuted, with refined statement’s id',outcome='Refuted printed test; refined value established in SC23 and C2/C9.')
add('Why the t-squared test excludes characteristic 2','073',r'$t^2$ n’est jamais un uniformisant','unproved claim / restriction on the normalization test',
    r'The author correctly notices that D⁽¹⁾(t²)=2t cannot be a unit where 2 is noninvertible. The test must be restricted to the locus where 2t is a unit; it cannot normalize a nonzero invariant on a characteristic-2 fiber.',HVI+' (test-value footnote); '+HUA)
add('The cubed-coordinate test and its limitation','073',r'=\frac23\frac1{t^2}dt^2','unproved claim',
    r'The value is correct where 3t² is invertible, as C2 verifies. It has a meaning in characteristic 2 but becomes zero there, so its role is a characteristic-zero sign check rather than a witness to characteristic-2 nonvanishing.',HVI+' (test-value footnote); '+HUA,event='computation or formal certificate')
add('The two signs coincide modulo 2','073',r'les deux choix possibles sur $\mathbb Z$ coïncident','unproved claim / clarification of the characteristic-two sign choice',
    r'The author’s bracket correctly observes that −G₀=G₀ on a characteristic-2 base. This removes a sign choice there and does not prove uniqueness among all possible characteristic-2 operators.',HVI+'; '+HUA)
add('Can quadratic differentials be eliminated from the formulation?','073',r's’il n’y aurait pas moyen d’éliminer ce rôle','conjecture / question',
    r'The proposed universal recipient asks for more than rewriting the known formula: it asks that every admissible coherent-valued invariant factor through ω². A precise answer needs the hypotheses on the target and on local surjectivity stated explicitly; the page announces the result without such a proof.',event='carried as background without fault found',confidence='Medium: the question and its missing hypotheses are explicit.')
add('Why an induced map u is not automatically an isomorphism','073',r'$u$ est même un iso','own idea / unproved claim',
    r'If e) is omitted, the map G′=(G,0) into ω²⊕𝒪 satisfies the evident rationality, cocycle, invariance and rigidity conditions, but the inclusion u is not an isomorphism. Thus the stated conclusion needs a surjectivity condition or a minimal/universal-target hypothesis; this counterexample does not refute the version retaining all relevant axioms.',HVI+'; '+NONE,event='targeted proof check',outcome='Verified direct-sum counterexample to weakened universal-target claim; full-hypothesis claim not refuted.')
add('Functorial coherent recipients','074',r'$\mathcal F_X\simeq\underline\omega_{X/\mathbb C}^{\otimes2}$','unproved claim',
    r'The opening continuation extends the same universal-recipient assertion to a family of coherent sheaves natural in X and then to the relative setting. No new proof is supplied, and the distinction in SC28 between a recipient and a minimal surjective recipient remains necessary.',event='carried as background without fault found',confidence='Medium: extension is explicit but its classification is not verified.')
add('Changing the acting group of a torsor by a unit','074',r'can. (semi)-isomorphes','unproved claim',
    r'For a unit φ, contracting a torsor along multiplication by φ produces a canonically φ-semilinear torsor isomorphism, and its transition differences become φG. This checks the displayed square without identifying points of different torsors by an unstated choice of origin.')
add('The factor-12 torsor and the word finest','074',r'un multiple $12$ième','unproved claim',
    r'Contracted change of group along 12·id makes the transition cocycle 12G₀, so the “multiple” description is valid even where 12 is not a unit. In that situation it is not a torsor isomorphism, and “le plus fin” should be read as the exhibited integral refinement rather than an independently proved optimality theorem.',HVI+'; '+HIX+'; '+HUA)
add('Uniqueness in a fixed positive characteristic','074',r'cela caractérise $G_0(f,g)$','unproved claim',
    r'The proposed replacement of d) by mere nonvanishing is a substantially stronger classification assertion and is not proved by the integral formula. Its exact functoriality and differential-order hypotheses matter, especially in the presence of additive Frobenius operations.',HVI+'; '+HUA,event='carried as background without fault found',confidence='Low for the full classification: the author immediately marks it doubtful.')
add('The explicit faux-question margin must remain visible','074',r'faux?','self-flagged',
    r'The margin contains an uncertain qualification ending “d’ordre ≤3”; its uncertainty cannot be resolved by a modern classification theorem. Hua’s VI abbreviates this nearly unreadable end, while the frozen transcription preserves the author’s doubt, so an unqualified uniqueness claim would overstate these pages.',HVI+' (final nearly-illegible-page footnote); '+HUA,event='used and rechecked in this run',confidence='High that a doubt and order restriction are present; low for the uncertain connecting words.')
add('Base units and universal nonvanishing','074',r'l’indétermination est dans','unproved claim',
    r'The change from an absolute field scalar to a global base unit is consistent with a functorial invariant that can be multiplied by a scalar pulled back from the base. Nonzero and invertible are different on a general base: multiplication by a nonzero nonunit may vanish on a fiber, so the exact nonvanishing hypothesis is decisive.',HVI+'; '+HUA,event='carried as background without fault found',confidence='Medium: scalar multiplication is checked; the full classification remains open here.')
add('The fiberwise condition on a nonintegral base','074',r'sur chaque $k(s)$','unproved claim / added fiberwise qualification',
    r'If the only ambiguity is a base scalar, being nonzero in every residue field makes that scalar a unit, including on a nonreduced base. This explains the added fiberwise requirement but does not rule out extra natural operators with nilpotent coefficients.',HVI+'; '+HUA)

add('The real and finite-regularity extensions','075',r'analytique réel, ou le $C^{\infty}$, ou $C^3$','unproved claim',
    r'The Schwarzian formula and its chain identity make sense for locally invertible real C³ maps, but their output has only continuous coefficients in general. Thus the C³ version requires matching the regularity of the target and the local ODE; it is not literally the same holomorphic sheaf statement, and later even-root constructions also need a sign restriction over the reals.',event='carried as background without fault found',confidence='Medium: the formula-level extension is clear; the exact category has not been specified.')
add('Exactness of the analytic derivative sequence','075',r's’annule exactement sur les fonctions loc. constantes','unproved claim',
    r'A holomorphic one-form has a primitive on a sufficiently small disc, and two primitives differ by a constant on each connected component. This checks local analytic surjectivity and the kernel; it does not assert surjectivity on global sections or in positive characteristic.')
add('The translation cocycle and its invariance','075',r'A(f,g)=dg-df','unproved claim',
    r'The additive cocycle law follows by cancellation, and adding a constant to g leaves dg unchanged. Both are literal first-derivative identities, with the analytic kernel statement in SC37 supplying the orbit interpretation.')
add('Translation rigidity with an initial value','075',r'g(x)=h(x)','unproved claim',
    r'Equality A(f,g)=A(f,h) gives d(g−h)=0, and the common initial value removes the locally constant difference. This is a zeroth-order initial condition because the translation group has one parameter; no second-order rigidity is needed here.')
add('The instruction to replace all functions by étale ones','075',r'prendre $\mathcal E_X$ plutôt!','self-flagged / withdrawn step',
    r'The marginal change removes functions whose derivative vanishes, but it simultaneously changes the image of d. The next page explicitly replaces the target by the bases of ω and switches from a difference to a ratio, so the earlier target cannot simply be retained.',event='used and rechecked in this run',outcome='Tracked author’s change of domain and its target repair on 076.')
add('The asserted étale-to-all-forms epimorphism fails','075',r'\mathcal E_X\longrightarrow\underline\omega_X\quad\text{épi}','own idea / withdrawn step',
    r'For fixed étale f, the target value −df would force dg=0 and is therefore never reached by an étale g, even locally. C4 gives this direct counterexample, and scan 076 repairs the statement by taking ratios of nonzero forms.',event='refuted, with refined statement’s id',outcome='Refuted the stated étale-to-all-forms map; refined nonzero-form ratio is SC43–SC44.')
add('The translation torsor is said to be trivial','075',r'sinon, il est trivial','unproved claim',
    r'For all analytic functions modulo constants, differentiation identifies the quotient with the vector sheaf ω, whose zero section gives a canonical origin. After restriction to étale coordinates the recipient becomes ω*, an 𝒪*-torsor which need not have a global frame; the triviality remark belongs to the preceding additive construction.')
add('The corrected multiplicative difference of bases','076',r'A’(f,g)=\frac{dg}{df}','unproved claim',
    r'For étale f and g the ratio is a unit and obeys the multiplicative cocycle A′(f,g)A′(g,h)=A′(f,h). Local integration shows that every unit multiple of df is realized locally, which is exactly the correction missing from the map in SC41.')
add('The bases of a line bundle form an 𝒪-star torsor','076',r'faisceau des bases','unproved claim',
    r'Any two frames differ by a unique invertible function, so ω* is a torsor under 𝒪*; a frame exists locally by the definition of an invertible sheaf. This is a change in both the target and the acting group from the additive ω-torsor discussed on 075.')
add('Frames modulo constants and line-bundle connections','076',r'L^*/\mathbb C^*\simeq','unproved claim',
    r'A connection on a line bundle over a small analytic disc has a nonzero horizontal solution of its first-order equation; two horizontal frames differ by a constant. Hence the displayed quotient is an isomorphism of analytic sheaves, while global horizontal frames may be obstructed by monodromy and the assertion is not automatically valid algebraically.')
add('The logarithmic difference has a convention-sensitive sign','076',r'D_g-D_f','reading question / own idea',
    r'With the stated convention that D_f makes f horizontal, C4 gives D_g−D_f=−d log(g/f), whereas the page uses the positive sign. The positive expression remains a valid cocycle, but equating it to that connection difference needs the opposite convention; Hua VI repeats the equality without resolving this issue.',HVG+' (item b, line-bundle connections); '+NONE,event='targeted proof check',outcome='Checked sign under explicit horizontality convention; no glyphs changed.')
add('The logarithmic derivative quotient','076',r'g\longmapsto\frac{dg}{g}','unproved claim',
    r'Locally, any holomorphic one-form a(t)dt is d log(exp∫a(t)dt), and the kernel consists of nonzero constants. This proves the analytic sheaf quotient claimed for the trivial line bundle, but not a global quotient of sections or a characteristic-p analogue.')
add('The preliminary additive logarithmic cocycle','077',r'B’(f,g)=\dfrac{dg}{g}-\dfrac{df}{f}','unproved claim',
    r'On nonzero functions this is an additive cocycle by cancellation and equals d log(g/f). Its use of all nonzero functions differs from the later restriction to nonvanishing étale coordinates, where d log g must also be a basis.')
add('The inverse-differential invariant','077',r'g\longrightarrow\frac{g}{dg}','unproved claim',
    r'An étale g has invertible dg, so g/dg is a well-defined vector field and is invariant under multiplication of g by a nonzero constant. Differences of these vector fields satisfy the additive cocycle, even when g itself vanishes.')
add('The nonzero-value hypothesis in multiplicative rigidity','077',r'un pt qui n’est pas un zéro','unproved claim / nonzero-value qualification',
    r'If g/dg=h/dh and g,h are nonzero near the chosen point, equality of logarithmic derivatives implies g=ch, and the common nonzero value forces c=1. The author’s nonzero hypothesis is needed: g=t and h=2t have equal g/dg and agree at their zero without being equal.')
add('The author rejects the inverse-vector surjectivity','077',r'ne peut être id. nul','withdrawn in the same text',
    r'If g/dg were identically zero while dg were invertible, then g would be identically zero, contradicting étaleness. Thus the proposed epimorphism onto all vector fields fails exactly as the author observes; this is an explicit internal retraction, not merely a later objection.',event='used and rechecked in this run',outcome='Author’s failed-e counterexample checked and retained as a retraction.')
add('Restriction to the nonvanishing étale locus','077',r'il faut se borner à','self-flagged / withdrawn step',
    r'On E* the logarithmic derivative is a basis, and every such analytic one-form is locally d log g for a nonzero étale g. This gives the revised torsor of bases and the multiplicative ratio, rather than restoring the rejected surjectivity onto all vector fields.')
add('The ratio has f over g rather than g over f','077',r'\frac{dg}{df}\frac{g}{f}','own idea / reading question',
    r'The left-hand ratio (dg/g)/(df/f) equals (dg/df)(f/g), as direct cancellation shows. C4 and C9 test f=t,g=t² and obtain 2 on the left but 2t² from the printed product; the later table on 082 uses the correct unsimplified ratio.',HVG+' (multiplicative invariant and table); '+NONE,event='refuted, with refined statement’s id',outcome='Printed product refuted; corrected identity in SC53 and C4, later confirmation SC97.')
add('Homogeneity is proposed as a condition of success','077',r'semble condition de succès','conjecture',
    r'The failed action of G_m on the whole affine line has a special orbit at zero, whereas its restriction to G_m is transitive, matching the author’s examples. This motivates the conjecture but does not prove that transitivity is necessary or sufficient for such a differential-invariant classification.',event='carried as background without fault found',confidence='Medium as an explanation of these examples; low for a general criterion.')
add('The affine action supplies horizontal differentials','077–078',r'f\longrightarrow D_{df}','unproved claim',
    r'Replacing f by af+b multiplies df by a constant and preserves the connection which makes it horizontal. This checks that the proposed construction is affine-invariant, provided the horizontality convention is kept explicit.')
add('The two quotient stages give the affine connection sheaf','078',r'\operatorname{Aff}(1,\mathbb C)\backslash\mathcal E_X','unproved claim',
    r'The two local analytic arguments are successive integration of a nonzero one-form and finding a horizontal frame for a line connection. They identify the affine orbit sheaf with Conn(ω); the statement concerns sheaves and need not yield one global affine coordinate.')
add('The affine logarithmic coefficient is correct as an invariant','078',r"\frac{g''}{g'}-\frac{f''}{f'}",'unproved claim / reading question',
    r'Differentiating log(g′/f′) gives the displayed one-form and its additive cocycle law. The calculation verifies the invariant itself; its identification with D_dg−D_df retains the sign issue identified in SC46.',event='used and rechecked in this run')
add('The question mark after the affine group of G-m','078',r'opérant sur $G_m$. ?','self-flagged / question',
    r'The indicated transformations z↦cz and z↦c/z form G_m⋊(ℤ/2) over ℂ, so they do act on G_m as written. This answers the elementary action question, while the analogy with an affine group is terminology rather than a new classification proof.')
add('The squared logarithmic differential quotient','078',r'\omega\mapsto\omega^2','unproved claim',
    r'Locally over ℂ, equality of squares of nonzero one-forms gives a constant sign, so equality of (d log f)² identifies f and g up to g=cf or g=c/f. Conversely a local square root of a nonzero quadratic differential, followed by logarithmic integration, proves surjectivity onto ω²*; these arguments use characteristic zero.')
add('Taking a root of an n-differential','080',r'\omega^{1/n}','unproved claim',
    r'For n≠0 over ℂ, a nowhere-zero coefficient admits a local analytic n-th root, unique up to a locally constant n-th root of unity. This is a local construction; when n is not invertible on a positive-characteristic base the same argument does not apply.')
add('The primitive ambiguity gives a well-defined projective point','080',r'donc $c_{\int\omega^{1/n}}$ bien défini','unproved claim',
    r'Two root choices differ by ε with εⁿ=1, and two primitives then differ by εf+b. These are constant affine transformations, so projective invariance proves that the resulting c_n is independent of both choices.')
add('Checking the c-n coefficient','080',r'\frac{2n+1}{n^2}','unproved claim',
    r'C5 derives the formula from λ=−f′/(nf) and 2λ′+λ², giving exactly (2n+1)/n². The independent symbolic check confirms the coefficient without deciding any other uncertain symbol on the page.',HVG+' (formula and coefficient footnote); '+NONE,event='computation or formal certificate')
add('The wrong function appears in the second G-m-n term','080',r"\frac{2m+1}{m^2}\left(\frac{g'}g\right)^2",'own idea / reading question',
    r'Because the second term is c_m(fdtᵐ), its logarithmic square must use f′/f. The test m=1,n=2,f=t,g=t² gives the correct difference 0 but the printed expression −9dt²/t²; Hua VI flags the same error, and C5/C9 independently verify it.',HVG+' (final coefficient footnote); '+NONE,event='refuted, with refined statement’s id',outcome='Printed G_m,n equality refuted; refined difference c_n−c_m in SC63/C5.')
add('The mixed-weight cocycle','080',r'G_{m,n}(\omega_m,\omega’_n)+G_{n,r}','unproved claim',
    r'With the definition G_m,n=c_n−c_m in a common projective-connection torsor, the mixed-weight cocycle is cancellation of c_n. It is valid for the defined difference, independent of the erroneous expanded second term identified in SC63.')
add('Compatibility with tensor powers','080',r'G_{m,nr}(\omega_m,\omega_n^r)','unproved claim',
    r'C5 proves c_nr(ω_nʳ)=c_n(ω_n) by substitution, so the asserted G identity follows. This also follows geometrically because the local root differentials differ only by constants, but the formula-level calculation is independently recorded.',event='computation or formal certificate')
add('The inserted power repairs the type of ds','080',r'G_{m,n}(\omega_m,(ds)^n)','withdrawn in the same text',
    r'The earlier line supplies ds where an n-differential is expected, and the insertion replaces it by (ds)ⁿ. The repaired identity then follows because a root is ds and its primitive is s; the incomplete line remains part of the author’s revision history.',event='used and rechecked in this run')
add('Recovery of the ordinary Schwarzian difference','080',r'G_{m,n}((dt)^m,(ds)^n)=G_{0,0}(t,s)','unproved claim',
    r'The first root differential has primitive t and the second has primitive s, so the difference is c_s−c_t=G(t,s). This also specifies what the page’s index 0 means: a coordinate input, not substitution n=0 into a formula containing 1/n.')
add('The cancelled denominator in c-prime','080',r'c’_n(\omega)=n^2','self-flagged / withdrawn step',
    r'The margin first cancels a 12, while the subsequent rescaling lines again use c_n/12. Since c_n is a torsor point, scalar multiplication must mean contracted change of group, and the inconsistent intermediate notation does not by itself define an integral normalized section.',HVG+' (final footnote explicitly declines to draw a conclusion); '+HUA,event='carried as background without fault found',confidence='Low for the author’s final intended normalization; high that the intermediate changes need preservation.')
add('The rescaled difference has reversed order and a target issue','080',r'\alpha^2c’_m(\omega_m)-\beta^2c’_n(\omega’_n)','reading question / own idea',
    r'On the displayed normalization this equals −(δ²/12)G_m,n, rather than its positive multiple, because the order is reversed. Moreover the difference of two points of a common torsor belongs to its acting sheaf, not canonically to the torsor itself; the displayed membership in a power of T therefore needs interpretation.',HVG+' (rescaling footnote); '+NONE,event='targeted proof check')
add('Invariance with parameters pulled back from the base','080',r'a\in\Gamma(S,\mathcal O_S^*)','unproved claim',
    r'The parameters a and b have zero relative Hasse derivatives, so the integral homography calculation C1 proves the displayed three invariances over the base. Allowing arbitrary functions on X in those parameters would change the assertion and is not justified.')
add('Equal differentials imply equal projective data in characteristic zero','080',r'df=dg\Longrightarrow G(f,g)=0','unproved claim',
    r'Locally analytically, equal differentials give g=f+b, so projective invariance applies. In characteristic 2 or 3 equal ordinary differentials do not force G₀ to agree: C2’s t+t² and t+t³ give explicit failures, so the distinction between G and G₀ must be retained.',HVG+'; '+HIX+'; '+HUA,event='targeted proof check')
add('Equal squared logarithmic differentials','080',r'\left(\frac{df}{f}\right)^2=\left(\frac{dg}{g}\right)^2','unproved claim',
    r'On the connected complex analytic nonzero étale locus, the two logarithmic differentials differ by a constant sign, hence f=cg or f=c/g. Both transformations are homographies and give G(f,g)=0; this is the same local argument as SC59.')
add('The question about a constant multiple of a logarithmic differential','080',r'\frac{df}{f}=c\frac{dg}{g}\qquad ?','conjecture / question',
    r'For a constant c and local choices of logarithm, integration gives f=Cgᶜ, with a multiplicative constant C that the last line suppresses. Such a power is generally not a homography: f=t²,g=t gives G(g,f)=3dt²/t² in characteristic zero, so the preceding vanishing implication does not extend to every c.',event='targeted proof check',outcome='Local integration checked; general Schwarzian-vanishing extension disproved by power test.')
add('The unfinished product at the foot of 080','080',r'(df-dg)','reading question',
    r'The product of a first-differential difference and a squared-logarithmic-differential difference is written without a proposed equality or target. It cannot be promoted into an additional vanishing criterion merely because each adjacent factor occurs in a valid preceding implication.',HVG+' (draft page, no interpretation supplied); '+NONE,event='carried as background without fault found',confidence='Low: there is no complete asserted relation to check.')

add('The first uniformization diagram is only partially specified','081',r'\mathbb R\text{-an}','reading question / unproved claim',
    r'The first row labels correspondences among D_X, U(x), B(x), V(x) and a doubtful D′_X as real-analytic or canonical, but these objects and the precise arrows are not defined on this sheet. Hua’s later discussion of homogeneous domains is a possible contextual lead, not enough to certify these particular maps or fill their uncertain directions.',HVG+' (draft page 80 expressly not reconstructed); '+HX+f'; {PRE}, P03/P09 (scan 036 and cross-cote comparison); {R}: no settled diagram identification; S20 only',event='carried as background without fault found',confidence='Low: definitions and several arrow directions are missing.')
add('The question between Sigma and the hatted tangent object','081',r'\widehat T_X','self-flagged / question',
    r'The paired arrows between Σ(x) and the hatted T-object carry an explicit question mark and a real-analytic label. Without identifying the hatted object and the intended map, one cannot infer an isomorphism from the two-way drawing; this remains an author-unverified diagram question.',HVG+' (draft not reconstructed); '+HX+'; '+NONE,event='carried as background without fault found',confidence='Low: the relevant objects are not fixed by the sheet.')
add('The questioned downward map from U to D','081',r'\mathbb R\text{-anal.}\;?','self-flagged / question',
    r'The arrow U(x)→D_X asks whether the map is real analytic. The available context does not specify a construction or agreed analytic structures for these exact objects, so this arrow remains unverified.',HVG+' (draft not reconstructed); '+HX+'; '+NONE,event='carried as background without fault found',confidence='Low: the map is not defined on the supplied sheet.')
add('The questioned downward map from B to the hatted T-object','081',r'?\;\mathbb R\text{-anal.}','self-flagged / question',
    r'The middle downward arrow B(x)→the hatted T-object has its own question mark about real analyticity. The path-class description of B later on the page gives no analytic formula for this arrow, so its status cannot be inferred from the neighboring maps.',HVG+' (draft not reconstructed); '+HX+'; '+NONE,event='carried as background without fault found',confidence='Low: neither the target identification nor an analytic map is fixed.')
add('The questioned downward map from V to D-prime','081',r'?\;\mathbb R\text{-anal.}','self-flagged / question',
    r'The right-hand downward arrow V(x)→D′_X separately asks about real analyticity. A hoped-for conjugate symmetry with the U-arrow would still require a definition of V and D′; the draft and Hua’s summary do not supply that definition.',HVG+' (draft not reconstructed); '+HX+'; '+NONE,event='carried as background without fault found',confidence='Low: the claimed conjugate interpretation is not established.')
add('The unfinished product of universal covers','081',r'\widetilde X_{(x)}','reading question',
    r'The product involving X, its conjugate, and a fundamental-group action stops at an equals sign and is followed by disconnected covering-space labels. It suggests an associated or diagonal quotient, but the action and equivalence relation needed to identify that object are not fully given here.',HVG+' (draft not reconstructed); '+HX+f'; {PRE}, P03; {R}: no matching settled construction',event='carried as background without fault found',confidence='Low: this is an incomplete formula, not a theorem with settled notation.')
add('The path-class construction of B','081',r'(c\lambda,\xi)\simeq(c,\lambda\xi)','unproved claim / reading question',
    r'If the fundamental group acts on the indicated fiber, this is the usual equivalence relation for transporting that fiber along paths and forms an associated local-system bundle. The text does not specify the required action or a compatible analytic structure, so the construction explains the set-theoretic pattern but proves none of the real-analytic arrows.',HVG+' (draft not reconstructed); '+HX+f'; {PRE}, P03; {R}: no settled B(x) identification',confidence='Medium for the associated-bundle pattern; low for the intended analytic realization.')
add('The proposed rank-two splitting on the draft','081',r'=\Omega^{-1}\oplus\Omega^0','unproved claim / reading question',
    r'The visible right-hand side gives a clear split rank-two bundle for the following matrix calculations, but the symbol on the left is uncertain. The subsequent algebra can be checked conditionally with E=Ω⁻¹⊕𝒪 without identifying that E with every hatted or Lie-algebra object earlier in the draft.',HVG+' (draft matrices) and VII (later rank-two constructions); '+NONE,confidence='High for the conditional split-bundle calculation; low for the uncertain left-hand identification.')
add('The endomorphism matrix and its differential twist','081',r'\check E\otimes E','unproved claim',
    r'For E=Ω⁻¹⊕𝒪, Hom of each ordered pair of summands gives the matrix (𝒪,Ω⁻¹;Ω,𝒪), and tensoring with Ω gives (Ω,𝒪;Ω²,Ω). This verifies both displayed matrices from the stated splitting, with no need to reconstruct the earlier diagrams.')
add('The trace-zero submatrix and the cancelled numerical matrix','081',r'\Omega^2&-\Omega^1','unproved claim / withdrawn step',
    r'Trace zero replaces the two diagonal Ω entries by a single entry and its negative, leaving Ω⊕𝒪⊕Ω² as the associated bundle. The earlier numerical matrix is crossed out and does not establish degrees or dimensions; in characteristic 2 trace-zero matrices contain the scalars, so this complex-analytic notation cannot bypass the later characteristic-2 issue.',HVG+' (draft matrices) and VII (trace/Lie discussion); '+f'{R}: no settled identification for this cancelled matrix',confidence='High for the trace calculation; low for interpreting the crossed-out numerical entries.')
add('A conditional interpretation of the genus counts','081',r'3g-3','own idea',
    r'If Ω is the canonical bundle of a compact genus-g curve with g≥2, then h⁰(Ω²)=3g−3, h⁰(Ω)=g and h⁰(𝒪)=1, summing to 4g−2 for the trace-zero differential-twisted matrix. This explains the displayed numbers consistently, but the draft does not itself state compactness, the genus range, or that these are the spaces being counted.',HVG+' (explicitly lists g+1, 3g−3, 4g−2 without reconstruction); '+NONE,confidence='Medium: Riemann–Roch fits all numbers, but their intended interpretation is not specified.',outcome='Conditional dimension interpretation only; no corrected transcription or unconditional genus claim.')
add('The isolated Omega and omega identification','081',r'\Omega^1=\omega^{\otimes2}','reading question',
    r'This isolated equality sits beside incomplete reciprocal-function calculations and is not reconciled with the Ω-powers used in the matrix block. It could use another convention for Ω, but treating it as a global identification would change all the line-bundle weights; no such convention is established on this sheet.',HVG+' (draft not reconstructed); '+NONE,event='carried as background without fault found',confidence='Low: the local notation is not explained.')
add('Inverting f plus its reciprocal','081',r'f^2-fh+1=','self-flagged / unfinished step',
    r'The intended equation has roots governed by h²−4, and h being nonzero alone does not make its roots étale: h=2 forces f=1. Conversely the map f↦f+1/f has critical points f=±1 and can take the value 0, so neither the image nor its local inverse is described just by “h sans zéro”.',HVG+' (draft not reconstructed); '+NONE,event='targeted proof check',outcome='Checked quadratic/discriminant and two simple failures of the stated nonzero condition.')
add('The reciprocal-logarithmic ODE is locally solvable','081',r'g=c\exp\int\frac1\varphi','unproved claim',
    r'For a nonzero holomorphic coefficient φ, the local equation g′/g=1/φ is solved by this exponential with c≠0 and gives a nonzero étale g. The integration constant is necessary, and possible global periods prevent interpreting the formula as an unconditional global solution.',HVG+' (draft not reconstructed, compare item b logarithmic integration); '+NONE)
add('The diagonal cancellation strokes on the draft','081',r'f+\frac1f=','withdrawn in the same text / reading question',
    r'The frozen page records long diagonal cancellation strokes crossing the working, alongside incomplete formulas and question marks. Their precise scope is not stated by the text, so this sheet is treated as draft exploration rather than a sequence of final theorems; no entire mathematical claim is silently deleted on that basis.',HVG+' (calls pages 79–80 drafts and notes the two strokes); '+NONE,event='used and rechecked in this run',confidence='High that cancellation strokes were recorded in the frozen audit; low for their exact intended scope.')

add('The powered additive ratio in the table','082',r'A_n(f,g)=\left(\frac{dg}{df}\right)^n','unproved claim',
    r'This is an 𝒪*-valued multiplicative cocycle obtained by taking a power of the ratio of bases. Despite the heading “écart additif”, its displayed operation is a ratio, so its cocycle law is multiplicative rather than the additive law of G.')
add('The affine sign conflict is repeated in the table','082',r'D_{dg}-D_{df}','reading question',
    r'The table again equates this difference with the positive logarithmic derivative of dg/df. The direct horizontal-frame computation in C4 gives the negative sign, whereas the β_n arrow later on this same page uses the compatible negative coefficient; the internal convention issue is therefore still present.',HVG+' (table and β_n footnote); '+NONE,event='used and rechecked in this run')
add('The missing star in the first powered quotient target','082',r'\underline\omega_X^n','reading question / own idea',
    r'The image (df)ⁿ of an étale coordinate is a nowhere-zero n-differential, so the quotient target is ωⁿ* for n≠0, as written in the repeated diagram below. The first target without a star cannot literally include zero while also being described as an 𝒪*-torsor.',HVG+' (table displays ω^{n*}); '+NONE,event='targeted proof check')
add('A possible group-level meaning of the exceptional n-equals-zero arrow','082',r'(n=0)','own idea / reading question',
    r'If μ₀ denotes the kernel of the power-zero map G_m→G_m, then μ₀=G_m and μ₀⋊G_a is the affine group, which gives a coherent possible indexing convention for this arrow. This interpretation does not define β₀ by substituting into 1/n or identify (df)⁰ with a connection; the draft supplies no limiting construction.',HVG+' (β_n formula explicitly n≠0); '+NONE,event='targeted proof check',confidence='High for the elementary kernel identity; medium for identifying the author’s intended convention.',outcome='Checked power-zero kernel μ₀=G_m and affine semidirect product; retained β₀/limiting-construction caveat.')
add('Forgetting an affine coordinate gives a projective one','082',r'D\mapsto c_D','unproved claim',
    r'Constant affine transformations form a subgroup of the constant projective transformations, so the map of orbit sheaves exists locally in the analytic setting. With the identifications on 078 and 073 it gives γ:Conn(ω)→Conn_proj(X), whose nonlinear formula is checked below.')
add('The boxed variation formula','082',r'c_{D+\omega_1}=c_D+2D\omega_1+\omega_1^2','unproved claim',
    r'C5 checks the formula by writing D=D_dt+λdt and ω₁=hdt: the difference of 2λ′+λ² is 2(h′+λh)+h². The term Dω₁ is the induced covariant derivative, so replacing it by an ordinary derivative in a nonhorizontal frame would lose the cross term.',HVG+' (boxed formula and ensuing computation); '+NONE,event='independent re-proof')
add('The exponential respects the sign-affine action','082',r'\exp(\pm f+a)','unproved claim',
    r'The elementary exponential identity gives exp(±f+a)=exp(a)(exp f)^±1. Consequently exponentiation connects the sign-and-translation quotient of additive coordinates with the inversion-and-scaling quotient of nonzero coordinates, locally over ℂ.')
add('The later multiplicative ratios correct the earlier expansion','082',r'\operatorname{Ecmu}_1(f,g)=\frac{dg/g}{df/f}','unpursued implication',
    r'The table retains the correct unsimplified logarithmic ratio and its square, avoiding the inverted f/g factor on 077. C4’s counterexample therefore concerns the earlier expanded product, not these later formulas.',HVG+' (table); '+NONE,event='used and rechecked in this run')
add('The first projective coefficient needs a quadratic differential factor','082',r'\frac{d^3g/df^3}{dg/df}','reading question / own idea',
    r'The first line is a coefficient computed in coordinate f and needs multiplication by (df)² to equal the second line, which is a quadratic differential written in t. The same tensor type favors ω² over the uncertain ω¹/ω² exponent at the end, but mathematical typing is recorded only as a research observation.',HVG+' (projective entry of the table); '+f'{PRE}, P01; {R}: **MPL_93_002-046 P01**, no settled reading of this exponent',event='targeted proof check')
add('The questioned vertical identity between the two omega-star targets','082',r'\mathrm{id}','self-flagged / question',
    r'The direct calculation d log(exp f)=df shows that the map induced by exponentiation is the identity on ω* under the two displayed quotient identifications. This answers the diagram’s question locally in the complex analytic category, without requiring a globally chosen logarithm.',HVG+' (quotient diagram); '+NONE,event='targeted proof check')
add('The power arrows alpha-n and alpha-prime-two','082',r'\alpha_n(\omega_1)=\omega_1^n','unproved claim',
    r'The arrows are equivariant for 𝒪*→𝒪*, φ↦φⁿ, and locally surjective over ℂ by root extraction on nowhere-zero coefficients. The n=2 identification in the diagram is compatible with the exponential sign-action identity in SC96; it is not a characteristic-2 root-extraction statement.')
add('The minus sign in beta-n and Hua’s differing reading','082',r'\varphi\mapsto-\frac1n\frac{d\varphi}{\varphi}','reading question / unproved claim',
    r'The group arrow has an explicit minus sign, and the frozen β_n formula lists minus as its first uncertain reading; C4–C5 show that this is the sign making f^{1/n}dt horizontal. Hua’s footnote reports a plus reading for that formula and corrects it mathematically, so its report must not override the newly frozen alternatives.',HVG+' (β_n sign footnote); '+NONE,event='computation or formal certificate')
add('The local formula for gamma','082',r'c_{pr}(t)+(2f’+f^2)dt^2','unproved claim',
    r'Using D_dt as the horizontal reference connection gives γ(D_dt+fdt)=c_t+(2f′+f²)dt². This is the λ=f specialization of C5 and is compatible with the boxed variation formula.',HVG+' (γ and c_n calculation); '+NONE,event='computation or formal certificate')
add('The general gamma-beta coefficient and the final n-one specialization','082',r'(2n+1)','reading question / inserted coefficient correction and n-one specialization',
    r'C5 verifies the inserted coefficient 2n+1 and the denominator n². The last line dropping n is correct only for n=1, as the nearby γβ₁ margin indicates; interpreting that line as another equality for arbitrary n would be false.',HVG+' (c_n coefficient footnote); '+NONE,event='computation or formal certificate')
add('Recovering the Schwarzian from gamma-beta-one-d','082',r'\gamma\beta_1d(f)','unproved claim',
    r'Substitution of the coefficient f′ for a one-form df gives precisely −2f‴/f′+3(f″/f′)². This independently checks the canceled n² denominator and links the diagram back to the normalization on 073 and the earlier scan 036.',HVG+'; '+f'{PRE}, P01 (scan 036); {R}: **MPL_93_002-046 P01**',event='computation or formal certificate')
add('The delta formula has coefficients minus one and five-fourths','082',r'\frac54','reading question / unproved claim',
    r'For ω₂=fdt², C5 gives δ(ω₂)=c_t+[f−f″/f+(5/4)(f′/f)²]dt². This verifies the first alternative for the doubtful f″ coefficient and the stated 5/4, while leaving the uncertain c_pr argument in the diplomatic transcription unchanged.',HVG+' (coefficient footnote); '+NONE,event='computation or formal certificate')
add('Delta after squaring and the exponential correction','082',r'\delta\alpha’_2(\omega_1)','unproved claim',
    r'Applying the power-compatibility identity gives δ(ω₁²)=γβ₁(ω₁)+ω₁² and the final coefficient f²−2f″/f+3(f′/f)². For ω₁=du this is also G(t,eᵘ)−G(t,u)=(du)², rechecking the earlier P02 correction rather than supplying any p-curvature conclusion.',HVG+'; '+f'{PRE}, P02/P05/P06 (scan 036); {R}: **MPL_93_002-046 P05**, **P06** are background bounds',event='used and rechecked in this run')
add('The final squared logarithmic ratio is algebraically correct','084',r'E(f,g)=\left(\frac{dg}{g}\right)^2','unproved claim',
    r'Dividing the two squares gives (dg/df)²/(g/f)² exactly, with all denominators units on E*. This is consistent with the table on 082 and corrects the direction of the unsquared product written on 077.',HVG+' (item d refers to manuscript p.83); '+NONE,event='used and rechecked in this run')
add('The blanket claim of axioms a through e needs the adapted meanings','084',r'On a\quad a) b) c) d) e)','unproved claim',
    r'The orbit and local-surjectivity arguments in SC59 establish the intended quotient by scaling and inversion, and E satisfies the multiplicative identity E(f,g)E(g,h)=E(f,h). The earlier additive b) cannot be copied literally into this 𝒪*-valued construction, and a rigidity initial condition must also remove the inversion ambiguity.',HVG+' (item d and table); '+NONE,event='targeted proof check')
add('The deleted translation-quotient fragment','084',r'\mathcal E_X/G_a(\mathbb C)','withdrawn in the same text / reading question',
    r'The final fragment is deleted and has no completed assertion after the quotient. It does not retract the separately justified translation quotient on 078, nor does it define an additional target for E.',HVG+' (end of other-groups section); '+NONE,event='carried as background without fault found',confidence='High that it is a deleted incomplete fragment; no definite mathematical assertion to test.')

add('What scans 072–074 actually establish about Hua’s candidate','072–074',r'G_0(f,g)','reading question / context comparison',
    r'The supplied scans explicitly propose the Hasse-derivative formula, the factor 12, arbitrary-base compatibility and a characteristic-p uniqueness question; they do not state a p-versus-p² homography theorem. Hua’s modernised reading places that theorem in its later IX, pp.121–123, so the two parts of the findings-register claim require different textual attributions.',HVI+'; '+HIX+'; '+HUA,event='used and rechecked in this run',confidence='High: this is a direct comparison of the frozen pages and the labelled context subsections.')
add('The relative constants for the first three Hasse derivatives','073–074',r'D_t^{(3)}','own idea / check of a contextual lead',
    r'C6 independently proves that on A[t] the common kernel is A[tᵖ] for p>3, A[t⁴] for p=2, and A[t⁹] for p=3, for every 𝔽_p-algebra A. These are relative Frobenius subrings with arbitrary coefficients from A, not necessarily literal powers of elements when A is imperfect; this checks Hua’s later local claim without attributing it to the supplied pages.',HIX+'; '+HUA,event='independent re-proof',confidence='High: direct coefficient proof, including nilpotent coefficients, reviewed by the root agent.')
add('Why level p alone loses invariance in characteristics 2 and 3','073–074',r'identiquement nulle en car. $2$ et $3$','own idea / check of a contextual lead',
    r'The coordinates t+t² in characteristic 2 and t+t³ in characteristic 3 differ from t by a relative p-th-power translation, yet their G₀-values are 1 and −1. Thus level-p constants are too large for the proposed G₀-invariance in these characteristics; this is an explicit necessity test for the later level-p² refinement, not by itself a proof of all its rigidity claims.',HIX+' (examples in the injectivity footnote); '+HUA,event='computation or formal certificate',confidence='High: exact Hasse computations, also exercised in the finite-ring script.')
add('Rigidity over an arbitrary coefficient ring in the nilpotent model','073–074',r'G_0(f,g)','own idea / independent check of a contextual lead',
    r'C7 proves that Q(s)=0 with unit first derivative forces a homography in A[t]/tᵠ for q=p>3, q=4 in characteristic 2, and q=9 in characteristic 3, without a Picard hypothesis. The proof uses a two-jet normalization and the unit binomial coefficients binom(d,3); C9’s exhaustive finite-field tests are only supplementary diagnostics.',HIX+' (Hua’s reported α=0 Lean verification, not rerun); '+HUA,event='independent re-proof',confidence='High: a complete arbitrary-ring coefficient proof was checked and separately reviewed by the root agent.')
add('A new descent argument fills the arbitrary-alpha step for the monic model','073–074',r'G_0(f,g)','own idea / refinement of a contextual lead',
    r'C8 supplies the missing written argument for B=A[t]/(tᵠ−α) with Pic(A)=0: a finite faithfully flat root extension reduces to C7, and the rank-one kernel of matrix relations descends to an invertible module which the Picard hypothesis trivializes. Determinant and denominator units then descend, giving a homography over A; the root agent independently reviewed this proof for the stated monic model, without promoting it to an unrestricted global theorem.',HIX+' (explicitly leaves the α≠0 descent unchecked); '+HUA,event='independent re-proof',confidence='High for the stated monic model: the complete kernel/descent proof was independently reviewed; global generalizations were not checked.',outcome='Proved monic-model arbitrary-α statement with Pic(A)=0; supporting C8, root targeted review accepted.')
add('Determinant one is stronger than projective linearity','073–074',r'G_0(f,g)','own idea / check of a contextual correction',
    r'Hua removes a determinant-one assertion from its report of later pages: over 𝔽₅[t]/t⁵, s=2t has Q=0 and unit derivative, but a representing homography has determinant 2d² and cannot have determinant 1. This elementary comparison confirms the need for a unit determinant in C7–C8; it does not establish what the unsupplied original glyphs say.',HIX+' (determinant-one counterexample footnote); '+HUA,event='targeted proof check',confidence='High for the counterexample: 2 is a nonsquare in 𝔽₅ and coefficient comparison forces the matrix shape.')
add('The limited comparison with Hoshi’s published invariants','073–074',r'G_0(f,g)','own idea / literature comparison',
    r'Hoshi’s 2024 paper §3 places the characteristic-2 level-two Sugiyama–Yasuda invariant in the sheaf of locally exact differentials, while §6 discusses the classical Schwarzian variant and its small-characteristic degeneracy. Those constructions cannot be identified with this ω²-valued integral G₀ solely from a shared level label; this comparison neither establishes nor refutes a priority claim.',HIX+' (literature footnote); '+HUA,event='targeted proof check',confidence='High for the cited definitions and target distinction; no novelty claim.',outcome='Read primary Hoshi §§3,6; checked targets and characteristic restrictions, no asserted priority.')
add('The limited comparison with Frobenius-Ehresmann structures','073–074',r'G_0(f,g)','own idea / literature comparison',
    r'Wakabayashi’s 2021 paper develops Frobenius–Ehresmann structures and their relation with flat Cartan geometry over an algebraically closed field of odd characteristic, in its stated smooth and locally noetherian setting. That framework supplies context for higher levels, but it does not directly verify the integral third-jet calculation or our characteristic-2 assertion; a precise functorial identification would still be needed.',HIX+' (literature footnote); '+HUA,event='targeted proof check',confidence='High for the source’s stated scope; low for any unstated equivalence with this G₀.',outcome='Read primary Wakabayashi introduction and §1.7; retained only scoped comparison.')
add('No p-curvature or Picard-Fuchs conclusion follows from this cluster alone','072–084',r'\operatorname{Conn\,proj}(X)','own idea / context comparison',
    r'These pages support a projective-connection and differential-invariant strand of S20, but this cluster specifies neither a Picard–Fuchs family nor a p-curvature computation. Earlier P05 and P06 are carried as background limits on such an inference, while P07–P09 describe additional comparison data that would be required; the present jet and descent checks do not re-prove or supersede those results.',f'{PRE}, P05/P06/P07/P08/P09 (scan 036 and scans 023,038–046); `context/README.md`, S20; {R}: **MPL_93_002-046 P05**, **P06**, **P07**, **P08**, **P09**, S20',event='carried as background without fault found',confidence='High for the evidentiary limit; no claim to resolve the larger programme.')

# Attach primary URLs only where a sourced fact, rather than our own computation,
# is being used. No source supplies the new C8 argument as a whole.
byid={i['id']:i for i in items}
quote_overrides={
 'SC04':r'G(f,1/g)',
 'SC05':"coïncident à l'ordre $2$",
 'SC06':r"G'=\varphi G",
 'SC11':r'c\in\mathbb{C}^{*}',
 'SC13':r'des coefficients $\in\mathbb{C}$',
 'SC17':'les coefficients doivent être dans',
 'SC18':"On trouve encore l'existence",
 'SC24':"$t^2$ n'est jamais un uniformisant",
 'SC25':r'+\frac23\frac1{t^2}dt^2',
 'SC26':r'possibles sur $\mathbb{Z}$ coïncident',
 'SC27':"s'il n'y aurait pas moyen d'éliminer ce rôle",
 'SC28':r'même un \uline{iso}!',
 'SC29':r'$\mathcal{F}_X\simeq\underline{\omega}_{X/\mathbb{C}}^{\otimes2}$',
 'SC32':'cela caractérise',
 'SC34':"l'indétermination est dans",
 'SC35':"n'est pas identiquement nul.",
 'SC37':"s'annule exactement sur les fonctions loc. constantes",
 'SC40':r'$\mathcal{E}_X$ plutôt!',
 'SC41':r'\mathcal{E}_X\longrightarrow\underline{\omega}_X\quad\text{épi}',
 'SC43':r"A'(f,g)=\frac{dg}{df}",
 'SC48':r"B'(f,g)=\dfrac{dg}{g}-\dfrac{df}{f}",
 'SC50':"un pt qui n'est pas un zéro",
 'SC54':'ce qui semble',
 'SC56':r'\operatorname{Aff}(1,\mathbb C)\backslash \mathcal E_X',
 'SC58':r'opérant sur $G_m$.',
 'SC64':r"G_{m,p}(\omega_m,\omega''_p)",
 'SC68':r"c'_n(\omega)=n^2",
 'SC69':r"\alpha^2c'_m(\omega_m)-\beta^2c'_n(\omega'_n)",
 'SC70':r'\Gamma(S,\mathcal O_S^*)',
 'SC102':r"c_{pr}(t)+(2f'+f^2)dt^2",
 'SC106':r"\delta\alpha'_2(\omega_1)",
}
for sid,quote in quote_overrides.items(): byid[sid]['quote']=quote
for i in items:
    parts=i['kind'].split(' / ')
    i['kind']=parts[0].replace('withdrawn in the same text','withdrawn in same text')
    i['state']='; '.join(parts[1:]) if len(parts)>1 else ''
    i['context_relation']='Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated.'
for n in [14,104]:
    byid[f'SC{n:02}']['context_relation']='Restates earlier P01 and Hua VI’s normalization, with an independent formula check.'
for n in [16,18,20,21,22,25]:
    byid[f'SC{n:02}']['context_relation']='Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate.'
for n in [6,12,13,17,19,27,28,29,32,34,35]:
    byid[f'SC{n:02}']['context_relation']='Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument.'
byid['SC23']['context_relation']='Restates and independently checks Hua VI’s mathematical correction; differs from the final printed test in the frozen page.'
byid['SC33']['context_relation']='Differs from Hua VI’s abbreviated ending by retaining the explicit faux-question and order-at-most-three qualification.'
byid['SC46']['context_relation']='Contradicts the sign identification repeated in Hua VI under the explicitly stated horizontal-frame convention.'
byid['SC53']['context_relation']='Adds an explicit counterexample to the expanded ratio; agrees with Hua VI’s later unsimplified ratio.'
byid['SC63']['context_relation']='Restates Hua VI’s correction of the second logarithmic-square term and independently tests it.'
byid['SC68']['context_relation']='Restates Hua VI’s decision to leave the draft torsor rescaling unresolved and records the cancellation explicitly.'
byid['SC71']['context_relation']='Adds the small-characteristic limitation to Hua VI’s analytic implication, using the independently checked examples reported in Hua IX.'
for n in range(75,90):
    byid[f'SC{n:02}']['context_relation']='Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead.'
byid['SC101']['context_relation']='Differs from Hua VI’s report of the doubtful written sign, while independently agreeing with its required mathematical minus sign.'
byid['SC106']['context_relation']='Restates and rechecks earlier P02’s exponential correction, while retaining the P05/P06 limits on p-curvature inferences.'
byid['SC110']['context_relation']='Refines Hua’s findings-register attribution by separating the supplied formula pages from its later p-versus-p² claim.'
byid['SC111']['context_relation']='Restates Hua IX’s local kernel claim and adds an independent arbitrary-coefficient-ring proof plus the relative-versus-literal-power qualification.'
byid['SC112']['context_relation']='Restates and independently checks Hua IX’s two counterexamples to level-p invariance.'
byid['SC113']['context_relation']='Restates Hua IX’s nilpotent-model result and adds an independent written proof; its reported Lean certificate was not executed.'
byid['SC114']['context_relation']='Adds the monic-model arbitrary-α descent proof which Hua IX explicitly leaves unchecked; it refines that candidate within the stated Picard hypothesis.'
byid['SC115']['context_relation']='Restates and independently checks Hua IX’s determinant-one counterexample, without making a new claim about unsupplied manuscript glyphs.'
byid['SC116']['context_relation']='Rechecks Hua IX’s Hoshi comparison against the primary definitions; adds no priority claim.'
byid['SC117']['context_relation']='Rechecks Hua IX’s Wakabayashi comparison within the primary source’s stated scope; adds no claimed equivalence of invariants.'
byid['SC118']['context_relation']='Restates P05/P06’s evidentiary caution and qualifies the S20 planning hypothesis using this cluster’s actual contents.'
byid['SC85']['source']='Stacks Project, Riemann–Roch and duality, Lemma 53.5.2: https://stacks.math.columbia.edu/tag/0B5B (conditional application, not an identification of the draft notation).'
byid['SC114']['source']='Stacks Project, Proposition 10.83.3 (finite projective descent): https://stacks.math.columbia.edu/tag/058Q; the remaining matrix-kernel argument is our C8.'
byid['SC116']['source']='Y. Hoshi, A note on Schwarzian derivatives and Sugiyama–Yasuda locally exact differentials, Osaka Journal of Mathematics 61 (2024), §§3,6: https://ir.library.osaka-u.ac.jp/repo/ouka/all/97634/ojm61_03_313.pdf.'
byid['SC117']['source']='Y. Wakabayashi, Frobenius–Ehresmann structures and Cartan geometries in positive characteristic (2021), introduction and §1.7: https://arxiv.org/pdf/2109.02826.'

header=r'''# Research notes: Schwarzian and other one-dimensional differential invariants

**Coverage:** cote 93, frozen scans 072–078, 080–082 and 084; research notes SC01–SC118. Scan 079 is absent from the supplied sequence, and the unrelated homotopy page 083 is handled separately. These notes were written only after the root recorded its freeze at 10:49:51 UTC on 18 November 2026 and opened the context at 10:49:56; this research agent used the frozen text and did not inspect the scan images or edit transcription files.

**Main findings.** The formula in scan 073 is an integral quadratic-differential cocycle, as independently checked by a universal three-jet identity, and its relation to the earlier normalization is G=12G₀. The printed squared-coordinate test is wrong; the correct coefficient is 1/(4t²). The author’s failed surjectivity experiments on 075 and 077, the doubt on 074, the draft diagrams on 081, and the uncertain or revised coefficients on 080/082 are preserved as separate issues rather than absorbed into a polished theorem.

**Hua comparison.** Hua’s findings-register candidate combines two different textual locations: the integral formula is present in 072–074, while the p-versus-p² homography discussion is reported in later unsupplied pages. Our checks prove the monic local model with q=p for p>3 and q=p² for p=2,3, including a new written descent argument for arbitrary α under Pic(A)=0; the root independently reviewed that argument. This does not prove all global sheaf statements or the proposed classifications of differential operators, and it does not establish priority.

**Context discipline.** `context/notes/RESULTS_STATE.md` was read before using the earlier-package notes and Hua’s modernised reading, and all matches below name the relevant files and their local sections/scan locations. The Hua material is credited to his AI-produced project as a lead; P05/P06 are carried as background rather than re-derived, and S20 remains a planning hypothesis. “No matching settled entry” means no matching result in the supplied context, not that the statement is unknown in the literature.

**Supporting records.** Detailed independent arguments are in `research_schwarzian_proofs.md` (C1–C11), the executable exact checks in `schwarzian_checks.py`, and their actual output in `schwarzian_checks_output.json`. The event ledger records what was checked, used, left as background, or refuted; it does not turn a finite enumeration or a cited AI report into a general proof. Each main commentary below is one to four sentences, excluding its metadata.

## Statement-level notes

'''

chunks=[header]
for i in items:
    chunks.append(f"### {i['id']} — {i['title']}\n\n")
    chunks.append(f"**File/location:** cote 93, scan {i['scan']}. **Short quote:** “{i['quote']}”. **Kind:** {i['kind']}.\n\n")
    if i['state']: chunks.append(f"**Additional state:** {i['state']}.\n\n")
    chunks.append(f"{i['comment']}\n\n")
    chunks.append(f"**Confidence:** {i['confidence']}\n\n")
    chunks.append(f"**Context comparison:** {i['context_relation']} {i['context']}.\n\n")
    if i.get('source'): chunks.append(f"**Primary source:** {i['source']}\n\n")

chunks.append('''## Separate author-unverified and withdrawn list

“Author-unverified” here means that the supplied pages explicitly question, withdraw or announce the item without a proof; it does not claim knowledge of what the author may have checked elsewhere. Independent checks in this run are identified in the individual notes and do not erase the manuscript’s provisional status.

### Explicit doubts, questions, proposed repairs and cancellations

''')
explicit=[2,8,12,27,33,40,41,51,52,54,58,66,68,69,73,74,75,76,77,78,79,80,81,84,86,87,89,91,92,93,98,99,101,105,109]
for n in explicit:
    i=byid[f'SC{n:02}']
    chunks.append(f"- **{i['id']}**, scan {i['scan']}: {i['title']}.\n")
chunks.append('''
Qualifications and coefficient revisions without an explicit nonverification mark are recorded separately as SC22, SC24, SC26, SC35, SC50 and SC103; they are not classified as self-flagged steps.

### Announced claims without a proof on the supplied sheet

''')
for scan in ['072','073','074','075','076','077','078','080','081','082','084']:
    group=[i for i in items if i['scan']==scan and 'unproved claim' in i['kind'] and int(i['id'][2:])<=109]
    if group: chunks.append(f"- **Scan {scan}:** "+', '.join(i['id'] for i in group)+'.\n')
chunks.append('''
### Context-only extensions requiring a separate provenance label

- **SC110–SC115:** the later p/p² discussion, kernel calculation, monic-model rigidity, arbitrary-α descent and determinant normalization are comparisons with Hua’s report of later unsupplied pages. They are not explicit claims of scans 072–074.
- **SC06, SC12, SC13, SC17, SC19, SC27–SC29, SC32–SC35:** the full classifications and universal-recipient assertions remain unproved in this run even though the displayed invariant and several consequences were checked.
- **SC75–SC81, SC86, SC93:** the questioned or incomplete diagrams still lack enough definitions for a theorem-level interpretation; each explicit real-analytic question has its own note.
- **SC116–SC118:** the literature comparisons and S20 boundary do not assert novelty, a Picard–Fuchs realization, or zero/nilpotent p-curvature.

## Primary-source register and actual reading scope

1. **Dumas**, *Complex Projective Structures* (2009), §§3.1–3.2, https://arxiv.org/pdf/0902.1951. Read the Schwarzian chain rule, projective-coordinate classification and local second-order ODE construction; these give a conventional reference for C3. Our normalization and the integral computations are independently displayed in C1–C5.
2. **Hoshi**, *A note on Schwarzian derivatives and Sugiyama–Yasuda locally exact differentials* (2024), §§3 and 6, https://ir.library.osaka-u.ac.jp/repo/ouka/all/97634/ojm61_03_313.pdf. Read the definitions/targets and the characteristic restrictions used in SC116; no claim to have identified all historical predecessors.
3. **Wakabayashi**, *Frobenius–Ehresmann structures and Cartan geometries in positive characteristic* (2021), introduction and §1.7, https://arxiv.org/pdf/2109.02826. Read the odd-characteristic setup and the structural comparison used in SC117, not a proof of the integral G₀ formula.
4. **Stacks Project**, Proposition 10.83.3, https://stacks.math.columbia.edu/tag/058Q. Read the finite-projective-descent statement and its proof; this is the one external descent input of C8, which the root also opened and checked.
5. **Stacks Project**, Lemma 53.5.2, https://stacks.math.columbia.edu/tag/0B5B. Read Riemann–Roch/duality for the conditional genus-count inference in SC85. The manuscript’s intended identification remains uncertain.

No extended quotations from these primary sources were used. The per-source discussion is deliberately limited; long calculations above belong to our independent proofs or to the user-supplied manuscript/context. A preliminary Ovsienko–Tabachnikov overview and Stacks module-descent page were also consulted but are not needed as cited inputs here. Hua’s reported Lean checks were not run, and no proof-assistant certification is claimed for this run.
''')

import re
def link_urls(s):
    return re.sub(r'(?<!\()https?://[^\s<>]+',lambda m:'[source]('+m.group(0).rstrip('.,;')+')'+m.group(0)[len(m.group(0).rstrip('.,;')):],s)
P.joinpath('research_schwarzian.md').write_text(link_urls(''.join(chunks)),encoding='utf-8')
P.joinpath('research_schwarzian_statements.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')

ledger=['statement_id\tdate\twho\ttype\toutcome\n']
for i in items:
    typ='refuted' if i['event'].startswith('refuted') else i['event']
    outcome=i['outcome']
    if outcome==i['title']:
        first=re.split(r'(?<=[.!?])\s+',i['comment'])[0]
        if typ=='carried as background without fault found':
            outcome='Unverified background/reading after context comparison: '+first+' No general proof is claimed.'
        elif typ=='computation or formal certificate':
            outcome='Exact computation performed; '+first
        elif typ=='independent re-proof':
            outcome='Independent written argument checked; '+first
        elif typ=='used and rechecked in this run':
            outcome='Compared or reused and rechecked in this run; '+first
        else:
            outcome='Targeted argument or text comparison checked; '+first
    if typ=='carried as background without fault found' and 'not' not in outcome.lower():
        outcome+='; recorded as unverified background, not promoted to a proof.'
    ledger.append('\t'.join([i['id'],'2026-11-18','ChatGPT research agent /root/research_schwarzian',typ,outcome.replace('\t',' ').replace('\n',' ')])+'\n')
for sid,outcome in [
 ('SC18','Root independently reviewed C1 integral jet identity; accepted for stated formula-level arbitrary-base cocycle.'),
 ('SC93','Root relayed BT peer review identifying μ₀ as the kernel of the power-zero map; research agent checked this elementary group identity and retained the draft-interpretation caveat.'),
 ('SC111','Root independently reviewed C6 relative Hasse-kernel proof; accepted for the stated polynomial model.'),
 ('SC113','Root independently reviewed C7; accepted arbitrary-ring nilpotent-model rigidity at q=p>3,4,9.'),
 ('SC114','Root independently reviewed C8 in full; accepted kernel base change, singular-matrix uniqueness, rank-one descent and unit conditions for the monic model with Pic(A)=0; no global generalization.')]:
    ledger.append('\t'.join([sid,'2026-11-18','ChatGPT root agent /root','targeted proof check',outcome])+'\n')
P.joinpath('research_schwarzian_events.tsv').write_text(''.join(ledger),encoding='utf-8')

# Each statement received the full-context reading recorded above. These actual
# batched rg queries supplement that reading and make the term checks reproducible.
import subprocess,re
contextfiles=['context/notes/RESULTS_STATE.md','context/same_cote_93/MPL_93_002-046_notes.md','context/hua_project/93.modern.tex','context/README.md']
patterns={
 '072':'dénominateur|Schwarz|schwarz|torseur|rigidité|surjectif|projectif',
 '073':'Hasse|divisées|G_0|12|universel|caractéristique|signe',
 '074':'unicité|non-nullité|intègre|torseur|caractéristique',
 '075':'Translations|translations|surjectif|étales|homogène',
 '076':r'Homothéties|horizontale|L\^\*|Conn|logarith',
 '077':'homogène|mauvais|multiplicatif|G_m|homoth',
 '078':'affine|Aff|automorphisme|G_m|df/f',
 '080':r'c_n|2n\+1|différentielle|79|puissance|12',
 '081':'brouillon|revêtement|4g|80|homogène|End|check',
 '082':r'beta|gamma|delta|81|5/4|5\}\{4|2n\+1',
 '084':'83|invariant.*E|G_m|logarith',
}
querylog=['statement_id\tfiles_searched\tregex\tmatching_lines\tfirst_locations\n']
for i in items:
    first=i['scan'].split('–')[0]
    pattern=patterns[first]
    if int(i['id'][2:])>=110:
        pattern=r'93-integral-schwarzian-level-p2|injectivité|rigidity|Descente|Pic\(A\)|p-curvature|P05|P06|S20|Hoshi|Wakabayashi'
    r=subprocess.run(['rg','-n','-i','-e',pattern,*contextfiles],cwd=P.parents[1],text=True,capture_output=True)
    assert r.returncode in (0,1),r.stderr
    lines=r.stdout.splitlines()
    locations=[]
    for line in lines[:6]:
        m=re.match(r'([^:]+):(\d+):',line)
        if m: locations.append(':'.join(m.groups()))
    querylog.append('\t'.join([i['id'],';'.join(contextfiles),pattern,str(len(lines)),';'.join(locations)])+'\n')
P.joinpath('research_schwarzian_context_queries.tsv').write_text(''.join(querylog),encoding='utf-8')
print(f'Wrote {len(items)} notes, {len(ledger)-1} check events, and {len(querylog)-1} context query records.')
