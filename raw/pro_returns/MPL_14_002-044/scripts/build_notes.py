#!/usr/bin/env python3
"""Assemble reviewed research notes; never opens a frozen TeX file for writing."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / 'records'

def read(name):
    return (REC / name).read_text(encoding='utf-8')

def notes(name, prefix):
    text = read(name)
    pattern = re.compile(r'^#{2,3} (' + prefix + r'\d{1,2}[a-z]?) — (.+)$', re.M)
    matches = list(pattern.finditer(text))
    result = []
    for i, m in enumerate(matches):
        stop = matches[i+1].start() if i+1 < len(matches) else len(text)
        block = text[m.end():stop]
        end = re.search(r'^## (?!' + prefix + r'\d)', block, re.M)
        if end:
            block = block[:end.start()]
        block = block.replace('**Proposed note.** ', '').strip()
        result.append((m.group(1), m.group(2), block))
    return result

groups = {
    'B': notes('research_bridges_reused.md','B'),
    'M': notes('research_motives.md','M'),
    'A': notes('research_albanese.md','A'),
    'RT': notes('research_tate_concise.md','RT'),
    'R': notes('research_bridges_reused.md','R'),
    'H': notes('research_titles.md','H'),
}
expected = {'B':5,'M':34,'A':38,'RT':8,'R':8,'H':4}
assert {k:len(v) for k,v in groups.items()} == expected

mkinds = {
'M01':'reading question','M02':'unproved claim (proposed axioms)',
'M03':'self-flagged; own idea','M04':'reading question; own idea',
'M05':'unproved claim; own idea','M06':'self-flagged; own idea',
'M07':'self-flagged; own idea','M08':'reading question; own idea',
'M09':'self-flagged; unproved claim','M10':'own idea',
'M11':'unpursued implication; own idea','M12':'self-flagged',
'M13':'self-flagged','M14':'unproved claim; unpursued implication',
'M15':'unpursued implication; reading question','M16':'reading question; own idea',
'M17':'conjecture (expectation)','M18':'unproved claim; own idea',
'M19':'unproved claim; withdrawn in the same text (attempted proof on scan013)',
'M20':'withdrawn in the same text (the Q-to-R manoeuvre on scan015; comparison with scan013)',
'M21':'self-flagged; own idea','M22':'unproved claim; own idea','M23':'own idea',
'M24':'unpursued implication','M24a':'unpursued implication',
'M25':'own idea','M26':'own idea','M27':'own idea',
'M28':'unpursued implication','M28a':'unpursued implication',
'M29':'unpursued implication; own idea','M29a':'own idea',
'M30':'reading question; unpursued implication','M31':'reading question; unpursued implication',
}

def section(group):
    out = []
    for ident,title,body in groups[group]:
        if ident in mkinds:
            body = re.sub(r'\*\*Kind:\*\* .*?(?= \*\*Context)',
                          '**Kind:** ' + mkinds[ident] + '.', body, count=1)
        if group == 'A':
            kind = title.split(':',1)[0].lower()
            body = '**Kind:** ' + kind + '.\n\n' + body
        # Explicit filename keys are defined in the edition guide; retain source locators.
        out.append(f'<a id="{ident}"></a>\n\n### {ident} — {title}\n\n{body}\n')
    return '\n'.join(out)

HEADER = r'''# MPL_14_002-044 — Research notes

## Edition, locations, and evidence

This file contains **97 short research notes** on cote14, scans002–044, with the blank scans018,023,043 omitted. The 40 page files and combined transcription were frozen on **15 November 2026 at00:41:55UTC**, before the context was opened; the research has not altered those41 files. The notes record manuscript claims, questions, corrections and implications, together with explicitly labelled editorial calculations and primary-literature comparisons.

Every unqualified `scanNNN` means **cote14**, file `pages/MPL_14_002-044_14_scanNNN.tex`; line numbers locate the frozen TeX source, approximately locating the corresponding handwritten or typed passage. **T** or **CT** denotes the supplied `context/MPL_16+47+54+44_transcription.tex`, **N** or **CN** its `_notes.md`, and **R**, **RS**, or **Register** denotes `context/notes/RESULTS_STATE.md`. Full context filenames are fixed by these keys; every context cote/scan below belongs to that supplied earlier package, and those earlier readings and research claims remain unreviewed unless their source expressly records review.

All **WG2** entries have register status *question or plan item, war-game round2, unchecked*. **WG H9** has status *hunch, Believe, unchecked*. The **Hua 14-albanese-equivalence-ring** entry has status *conjecture, unsearched; reach beyond; intake pending*. Other statuses are stated at their point of use as the return's claims, including the limited referee qualification on LM7_PUSH E.67; no register status has been promoted by this edition.

Each numbered note has a body of one to four sentences, with its quotation, location, kind, context comparison and status in adjacent metadata. Mathematical test cases specify their actual maps and retain the manuscript's unverified hypotheses; none is proposed as a new general conjecture. The reproducible context-search ledgers are in `records/root_context_searches.md`, `records/research_motives_context_search.md`, `records/research_albanese_context_search.md`, and `records/research_tate_context_searches.md`; the corresponding note IDs locate each search. The source list at the end gives primary URLs and precise passages.

## Answers to the requested questions

| Requested question | Finding and exact comparison | Notes |
|---|---|---|
| Category of motives built from cote16's Lefschetz rings? | The fragment starts with an existing $M$ and its fourth structure. The correspondence construction $(X,p,m)$ and $g\circ f=p_{13*}(p_{12}^*f\cdot p_{23}^*g)$ supplies the mathematical bridge; cotes12–13 and the cited24-page *Motifs* witness were not supplied. | M01, M24, M24a |
| The Lefschetz $\mathfrak{sl}_2$ inside the motivic Galois group? | Naturality gives $gLg^{-1}=\chi_{\mathbb L}(g)L$, with the inverse character on lowering. The complete $\mathbf P^1$ calculation proves that a universal inclusion inducing these Lefschetz operators cannot hold; the Tate-character kernel commutes with them in the specified pure Nori realization. | M25, M27 |
| Grading as the weight cocharacter? | On the realization of a variety of dimension $d$, $d\rho(w)=h+dI$ and $\rho(w(t))=t^d\lambda_{\mathfrak{sl}_2}(t)$. The effective Tate object has $\varepsilon\circ w=t^2$, and its dual has $t^{-2}$. | M11, M26 |
| Draft A–D versus printed lettering? | Scan044 defines A on cycles modulo algebraic equivalence. The quotient $C^i_{\mathrm{alg}}\to A_H^i$ relates it to printed A; the inverse-operator content of cote16's draft $C_\ell$ matches printed B. The available occurrences do not define every draft B or D. | RT1–RT3 |
| Singular hypersurfaces from cote16 scan047? | Cote14's surviving Serre letter works with smooth $X$ and a smooth hyperplane section. No explicit singular-variety reformulation was found in the40 supplied pages. | RT8 |
| Exact sequence over $\mathbf Q$? | Cote14 supplies a Galois action on character/cocharacter data. The later Nori theorem gives $1\to G_N(\overline{\mathbf Q})\to G_N(\mathbf Q)\to\Gamma_{\mathbf Q}\to1$, through base change and Artin motives; its proof and the additional connectedness question are recorded separately. | M30 |
| A written period conjecture? | No statement was found in these supplied pages. The later comparison is the period point on $\operatorname{Isom}^{\otimes}(\omega_{\rm dR},\omega_B\otimes k)$ and its evaluation map; injectivity is the cited source's conjecture. | M31 |
| Which Nori/Ayoub statements are proved, and where do algebraic-cycle claims enter? | The inverse Hopf-algebra maps, pure-motive comparison, numerical quotient, and mixed Kummer extension specify the relevant results and limitations. The unresolved algebraicity of general Lefschetz inverses is kept visible through the cycle-action factorization. | M28–M29a |
| Motives over a base and six operations? | Scan011 proposes a connected base and a de Rham realization. The context's degree-one exact sequences supply a concrete comparison; these leaves do not construct the relative category or its six operations. | M14–M15, A38 |

The table is an index to the notes and their evidence; it does not replace their stated fields, coefficient conventions, or proof boundaries.

## The requested table: linear statement, non-linear statement

| Pair | Linear statement | Non-linear statement | Explicit map or calculation |
|---|---|---|---|
| Tate and anabelian Hom | Tate's finite-field Hom theorem, with $\ell$ invertible in the base field | Mochizuki's Hom theorem for hyperbolic curves over sub-$p$-adic fields | Functorial abelianization $(\Delta_X^{\rm prf})^{\rm ab,\ell}\to(\Delta_Y^{\rm prf})^{\rm ab,\ell}$ becomes $T_\ell J_X\to T_\ell J_Y$ for proper curves; the cited theorems retain their own base fields. **B01** |
| Semisimplicity and trivial centres | Tensor representations and the pro-reductive Tannaka group in the stated characteristic-zero setting | Injectivity of $\Delta\to\operatorname{Aut}(\Delta)$ for geometric hyperbolic-curve groups | $G_m$ acts by $t^n$ on its semisimple character spaces and has centre $G_m$; finite-cover abelianizations enter the verified centre-freeness argument. **B02** |
| Polarizations and real structures | $\psi^C(x,y)=\psi(x,Cy)$ and the associated compact real form | Components of $X(\mathbf R)$ and conjugacy classes of real sections | On the Jacobian Tate module, $e_\ell(cv,cw)=\chi_\ell(c)e_\ell(v,w)=-e_\ell(v,w)$. **B03** |
| Weights and cyclotomic normalizers | Cusp Tate modules of weight$-2$ and Jacobian Tate modules of weight$-1$ | Cyclotomic conjugation on procyclic inertia and its normalizer | The generalized-Jacobian abelianization sequence and $g\tau g^{-1}=\tau^{\chi(g)}$ specify the relation; open normalizer image alone leaves the character comparison to check. **B04–B05** |

'''

STANDING = r'''## Standing question I — Steps marked unverified, tentative, or postponed

This is a compact index into the notes. The exhaustive literal audit in `records/research_standing_register.md` gives **86 semantic/status entries**, **24 reused-typescript entries**, and all **155 deletion occurrences**, with exact TeX spans; its validation record checks the quotations and all40 page marks against the frozen files. An editorial reading doubt is marked as such in the transcription and is not automatically a doubt expressed by the author.

| Cote14 scan / TeX line | Author's short wording or written marker | Step, local continuation, and note |
|---|---|---|
|003:10,14,18–19|“À priori”; “d'autres axiomes”; “???”|Effectivity descent, additional axioms, and fixed-weight finiteness: M02–M03.|
|005:9–10|“sauf peut être”; unfinished insertion|Intersection and the graduation/effectivity reservation: M06.|
|007:15|“mais peut-être pas pr $W'$”|Larger automorphism invariance: M07.|
|009:4|“saturation que nous ne précisons pas ici”; “automatiquement satisfaite ?”|Undefined saturation and its automatic-satisfaction question: M09–M10.|
|011:9–11|“injective ?”; “dans Im I(G) ?”|Injectivity and single-cocharacter effectivity: M12–M13.|
|011:13–15|“intrinsèque”; “Regarder”; final “?”|Fibre-functor independence, torsor transport and the relative de Rham proposal: M14–M15.|
|011:17–19|“Regarder G commutatif !”; “sans doute”|Test groups and the anticipated Frobenius criterion: M16–M17.|
|013:14–20|“J'affirme”; deleted attempted proof|The compact-kernel assertion remains live; its displayed attempted proof is deleted: M19.|
|015:14|“??”; “Comment définir … intrinsèque ?”|Real-value positivity and intrinsic effectivity: M21–M22.|
|015:24; compare013:14|“ne peut pas”; “Fausse”|The Q-to-R move is denied; the uncertain compact-part wording does not identify a wholesale retraction of013: M20, M23.|
|024:8,14|“[projectif]”; marginal “?”|Projectivity and an unattached reservation: A04.|
|026:18|“sous réserve que”|Defined evaluations and simultaneous parameter choices: A06.|
|027:4–028:4|“à vérifier”; “Nous laissons ici les détails”|Moving representatives for pullback is expressly left unverified: A07.|
|028:8|“pr l'AQT”; “triviale”|An uncertain reference for pushforward and an abbreviated implication: A08.|
|029:2|“Ici il semble …”|Use of projectivity in the endpoint argument: A04.|
|029:9,11|“On ignore”; “Vrai pr tous les cycles???”; blank reference|Rational-equivalence question and an unfilled source citation: A10–A12.|
|030:4–5|“num. équiv. à0??”; deleted “À voir…”|Numerical strengthening remains a question; the cancelled wording remains uncertain: A14.|
|030:17–19|“On ignore”; “Il y a intérêt à transformer”|Four-point box and external-product proposal: A12–A13.|
|031:23 →034:2|“À réserver pr plus tard”; “Pour (i)”|The later page gives a divisibility argument for the postponed step: A16.|
|032:19,27,29 →033:2|uncertain “il faut vérifier”; “O.K.”; “on ne sait pas”|Local checks do not settle integral universal-cycle existence; multiplication by$n$ replaces it: A17–A19.|
|035:23,25|“Va être généralisé”; inserted saturation assertion|The generalization is stated, and the saturation scope has the explicit test A22.|
|036:13|“mais attention”; “Ces homs se composent”|Rational correspondence warning and asserted composition: A23–A24.|
|037:2–3|“?”; “Une question plus subtile”|Algebraicity of inverse isomorphisms: A25.|
|037:14,17,19|“il faut vérifier”; “Question de transposition”; “Cf plus bas”|Independence from the representative cycle remains a proof obligation: A26–A27.|
|038:17,20,22|“dém. pas faite”; “?” over implication; “réciproque”|Unfinished Theorem3.1 and its converse: A29, A34.|
|039:12|“on vérifie aisément”; “on est ramené au cas”|Curve-projector algebraicity is checked in A33; the middle-factor proof stops here: A29.|
|041:10,20,24|“conj de Tate vérifiée”; uncertain “Pr. Tits”; “Mumford”|Assumed degree-two statement, uncertain representation reference, and named external verification: RT5–RT7.|
|042:2,10|“b) est trivial”; “égalité des extrêmes…”|Compressed invariant-generation step: RT6.|
|044:6–10|“pas décisif”; “Conjecture A”; “Modulo vérification…”|Outstanding conjecture and unwritten reduction: RT1–RT4.|
|044:10|“n'est pas même démontré pour le moment !”; “N'est démontré que le théorème de Lefschetz ``faible''”|The author's dated 1965 report of the proof status of the cohomological statement; retained as a historical claim, with the comparison in RT2.|
|044:12|continuation sign|The letter stops during the Gysin discussion: RT4.|

Reused typescripts have several “clear”, “immediate”, cited-proof, and cut-off passages, indexed individually in R02–R05 and R08 and in the exhaustive register. Their printed statements are not attributed to Grothendieck solely from the fact that the leaves were reused in this folder.

## Standing question II — Title sheets, internal headings, and page counts

| Cote14 scan(s) | Visible title or identifying heading | Visible pagination / count finding |
|---|---|---|
|002|Deleted general title about motivic structures; live “Structure d'effectivité”|Manuscript mark1; no explicit total.|
|003|“Structure”|Mark2; short running heading.|
|011,013,015|“Questions”; “Cas d'un tore T sur Q”; “Détermination du groupe des caractères rationnels sur Q”|Marks10,12,14; internal headings.|
|017|“Équivalence d'Albanese et de Picard des cycles algébriques”|Mark16; cover.|
|024|“Théorie de l'équivalence d'Albanese des cycles”; §1 on its ring; uncertain marginal “Conjectures Weil, Critères d'Équivalences”|Mark23; no explicit total.|
|031,037,038|§2 on families; “Dualité”; §3 on the associated $\ell$-adic homomorphism|Marks30,36,37.|
|040|“Astuce de Tate / sur les cycles / décomposables”|Mark39; cover.|
|044|“27.8.65”; “Mon Cher Serre”|Mark43 and a continuation sign; only the first supplied letter page.|
|016,014,012,010,008,006,004|Reused English leaves, including “IV. The Brauer group of a ringed space.”|Internal II.9, III.4–III.7, IV and IV.2, with intervening typed leaves absent.|
|022,020|Reused French leaves, including “5. Chambres dans un espace affine.”|Typed“−14−”,“−15−”, both“n°391”; exact local join022→020.|

All40 retained scans have exactly one manuscript mark, with the explicit map $N\mapsto N-1$ for $N\in\{2,\ldots,44\}\setminus\{18,23,43\}$. No retained cover or heading writes an explicit total or page range for its text. The complete40-row census, uncertain marginal numeral, bibliographic page references, statement labels and deletion spans are in the standing register; H01–H04 give the context comparisons.

'''

REGISTER = r'''## Changes relative to the supplied results register

| Register entry and supplied status | What this package adds | Notes |
|---|---|---|
|WG2 §2.4 #3; WG2 §6. #9 — unchecked plans|Actual effectivity axioms and questions; exact correspondence, grading and Lefschetz maps; bounded conclusions on lettering, singular varieties, Galois sequence and periods.|M01–M31, RT1–RT4, RT8|
|WG2 §2.3 #2/#3; WG2 S28 (§1.7) — unchecked plans|The precise conversion between unit-step lowering and the $\mathfrak{sl}_2$ action, including denominators.|M25–M27|
|WG2 §2.3 #7 — unchecked plan|Primary checks on numerical semisimplicity, the pure Nori/André functor, and a nonsplit mixed extension; the cycle-class factorization remains explicit.|M28a–M29a|
|WG2 B16 (§1.2) — unchecked plan|The rational relative Chow-motive Lefschetz construction in the specified abelian-scheme setting.|M24a|
|WG2 §2.3 #12/#13; WG2 §2.4 #4 — unchecked plans|Definition and proposed operations on Albanese equivalence, exact maps to earlier questions, explicit gaps and scope tests, and later results with their hypotheses.|A01–A38|
|WG H9 — unchecked hunch|A direct diagonal pullback connects the new sign example to the old positivity divisor; no full height/intersection equivalence is inferred.|A01|
|WG2 §Lookups #3 — unchecked plan|Checked source and sign for the later threefold autoduality.|A36|
|Hua 14-albanese-equivalence-ring — unsearched conjecture; intake pending|Definition and stated operations confirmed as textual content; “shows” is qualified by scan028's explicit moving gap, and the truncated excerpt is not completed.|A37|
|LM1 A.8 — Refuted, return's claim|Adds the distinguished-character calculation $\varepsilon\circ\theta=\varepsilon^{-1}$ for $\varepsilon=\det$.|M16|
|LM7 C.1 — Known, return's claim; C.5 — Proved, return's claim; C.8 — Refuted, return's claim|Uses the generalized-Jacobian realization map, retains the prior exact-extension and specific-tower scope, and does not present either registered conclusion as newly proved.|B01, B04–B05|
|LM6 A.22; LM7 E.23; FLAGGED_149 B9 — Open, return's claims|Records possible realization methods and the missing character/fibre calculations; all three remain open in this package.|B04–B05|
|LM6 A.50 — Proved, return's claim|Retains the finite-cover character-descent lead without filling the register's truncated hypotheses.|B04|
|LM7_PUSH E.67 — Proved; limited referee confirmation recorded|No matching Gaussian-norm formula identified in these pages; no per-word fibre verification is claimed.|B05|
|MPL_7_061-072+8_001-078 scan061 (§66) — first-pass lead|The actual tensor-automorphism and torsor maps clarify the earlier fibre-functor requirements.|B02, M14|
|WG2 §1.1 #2/#3, §2.1 #5, §Summary #2 — unchecked plans|Actual titles, page-mark census, reused-text joins and the dated1965 letter replace catalogue-level guesses with located evidence.|H01–H04, R01, R06|

The supplied entries for MPL_142 §316 and MPL_147 §230 are bibliography leads, and MPL_149 RN100-02 concerns a good-reduction reference; no direct textual addition to those entries was identified here. The source files named by the register were not themselves supplied, so their truncated row statements have not been extended by conjecture.

'''

BIB = r'''## Verified primary references

The bracketed keys in the notes refer to this list; **Tate66** and **T66** name the same source, and **DM** denotes Deligne–Milne. Original publication dates and the particular corrected versions actually checked are recorded separately. Page/section references identify the evidence used, not an assertion that every statement in a cited work has been audited.

| Key | Primary reference | Passages used |
|---|---|---|
|G69|Grothendieck, A.(1969), *Standard conjectures on algebraic cycles*,193–199. [Primary text](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf)|§§2–3, cycle-class image and conjecture lettering.|
|K68|Kleiman, S.L.(1968), *Algebraic cycles and the Weil conjectures*,359–386. [University-hosted primary text](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf)|Introduction;§§1.2.1,1.4.7,2,2.9,3.6.|
|T66 / Tate66|Tate, J.(1966), *Endomorphisms of abelian varieties over finite fields*, Inventiones Mathematicae2,134–144. [Primary text](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf)|§1, Hom theorem and Mumford attribution; divisor-correspondence comparison.|
|C83|Clemens, H.(1983), *Homological equivalence, modulo algebraic equivalence, is not finitely generated*, Publications Mathématiques de l'IHÉS58,19–38. [Published text](https://www.numdam.org/article/PMIHES_1983__58__19_0.pdf)|§0, equation(0.1), Theorem(0.2), and meaning of generic onpp.19–20.|
|Milne01|Milne, J.S.(2001 submitted version,11February2001), *The Tate conjecture for certain abelian varieties over finite fields*. [Author text](https://www.jmilne.org/math/articles/2001aP.pdf)|§1; AppendixA.3 example,p.15;A.6.|
|Mochizuki99|Mochizuki, S.(1999), *The local pro-p anabelian geometry of curves*, Inventiones Mathematicae138,319–423. [Author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf)|TheoremA, full profinite and geometrically pro-p versions and notation; Corollary15.5.|
|Mochizuki03|Mochizuki, S.(2003), *The absolute anabelian geometry of hyperbolic curves*. [Author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf)|Lemma1.3.1 and Corollary1.3.2.|
|DM18 / Deligne–Milne|Deligne, P., & Milne, J.S.(1982; corrected author texts2012 and2018), *Tannakian Categories*. [2018 text](https://www.jmilne.org/math/xnotes/tc2018.pdf); [2012 text](https://www.jmilne.org/math/xnotes/tc2012.pdf)|Theorems2.11,3.2; Proposition2.23;4.22–4.24;§5.1;5.18–5.19.|
|Pal11|Pál, A.(2011), *The real section conjecture and Smith's fixed-point theorem for pro-spaces*, Journal of the London Mathematical Society83,353–367. [Author manuscript](https://arxiv.org/pdf/0905.1205)|Theorem1.3 and Example5.8, used for the stated proper real curves.|
|Stix12|Stix, J.(2012 author manuscript), *On cuspidal sections of algebraic fundamental groups*. [Author text](https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf)|(3.1); Proposition16; Definitions26,29; Theorem30; Corollary31.|
|Jannsen1992|Jannsen, U.(1992), *Motives, numerical equivalence, and semi-simplicity*, Inventiones Mathematicae107,447–452. [Repository primary text](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf)|Opening category construction; Theorem1; Corollaries1–2; Remark3.|
|Künnemann1993|Künnemann, K.(1993), *A Lefschetz decomposition for Chow motives of abelian schemes*, Inventiones Mathematicae113,85–102. [Digitized primary text](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0011.pdf)|Printedpp.85,94–97; equation(15), Proposition4.3, Theorems5.1–5.2; relevant printed pages visually read.|
|Choudhury–Gallauer2017|Choudhury, U., & Gallauer Alves de Souza, M.(2017), *An isomorphism of motivic Galois groups*. [Primary author text](https://arxiv.org/pdf/1410.6104)|Version3,18May2017;§2.2 and Theorem9.1.|
|Arapura2013|Arapura, D.(2013), *An abelian category of motivic sheaves*, Advances in Mathematics233,135–195. [Primary author text](https://arxiv.org/pdf/0801.0261)|Version4; Theorems6.3.3,6.3.5,6.4.1 and the latter proof's steps1–7.|
|HMS2025|Huber, A., & Müller-Stach, S.(2017; annotated edition1July2025), *Periods and Nori Motives*. [Corrected text](https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-errata/buch-errata.pdf); [author errata](https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-errata/buch.html)|Theorem9.1.16 and corrected§9.5, including2024–2025 corrections; Remark9.5.7; Theorems10.2.7–10.2.8,13.1.4; Definition13.1.9; Conjectures13.2.1,13.2.5.|
|Huber2018|Huber, A.(2018,29November), *Galois theory of periods*. [Author text](https://home.mathematik.uni-freiburg.de/arithgeom/preprints/huber-galois.pdf)|Conjecture3.3;§§4.4–4.5 and7.2.|
|Kahn2025|Kahn, B.(2025), *Galois descent for motivic theories*, Theory and Applications of Categories44(20),588–616, revised7July2025. [Author-hosted published text](https://webusers.imj-prg.fr/~bruno.kahn/preprints/stacks-TAC.pdf); [journal record](https://tac.mta.ca/tac/volumes/44/20/44-20abs.html)|§§5.8–5.10; Proposition10.1, Theorem10.2, Remark10.3.|
|M|Mumford, D.(1969), *Rational equivalence of0-cycles on surfaces*, Journal of Mathematics of Kyoto University9(2),195–204. [Author-hosted scan](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969e--0-cycles-Euclid.pdf)|Introduction and conclusion, especiallypp.196,203; actual PDF title checked despite erroneous search metadata.|
|K|Kahn, B.(2021), *On the universal regular homomorphism in codimension2*, Annales de l'Institut Fourier71(2),843–848. [Published text](https://www.numdam.org/item/10.5802/aif.3408.pdf)|Theorem0.1, bound argument, Lemma1.1 and Remark1.2.|
|ACV23|Achter, J.D., Casalaina-Martin, S., & Vial, C.(2023), *A functorial approach to regular homomorphisms*, Algebraic Geometry10(1),87–129. [Published text](https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf)|Definition4.2, Lemma4.7, Theorem6.1,§§8.1–8.2 and Proposition8.2.|
|V22|Voisin, C., *Geometric representability of1-cycles on rationally connected threefolds*. [Author manuscript](https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/1cycleRC.pdf)|Introduction and the family-induced Albanese map; “22” is a reference label, not a newly verified publication date.|
|V25|Voisin, C.(2025), *Varieties with representable CH0-group and a question of Colliot-Thélène*, arXiv2508.02331v2,15October2025. [Primary text](https://arxiv.org/html/2508.02331v2)|Definition1.1 and Theorem1.4.|
|ACV25|Achter, J.D., Casalaina-Martin, S., & Vial, C.(2025), *Decomposition of the diagonal, intermediate Jacobians, and universal codimension-2 cycles in positive characteristic*, Astérisque455. [Author text dated19March2025](https://www.math.uni-bielefeld.de/~vial/diagonal.pdf)|Theorems1,12.12; Conjecture5.1; Remark12.13.|
|O|Oda, T.(1969), *The first de Rham cohomology group and Dieudonné modules*, Annales scientifiques de l'ÉNS,4th series,2(1),63–135. [Published text](https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf)|Supplied primary source; Introduction, Theorem5.10, Corollaries5.11–5.12, printedp.131 visually checked.|
|Vitale96|Vitale, E.M.(1996), *The Brauer and Brauer-Taylor groups of a symmetric monoidal category*, Cahiers de Topologie et Géométrie Différentielle Catégoriques37,91–122. [Published record](https://www.numdam.org/item/CTGDC_1996__37_2_91_0/)|Bibliography entry1 attests B.Auslander's1966 title; the Auslander paper itself was not available for collation of these typescript leaves.|

## Verification scope

The primary transcription was made in one reading stream, with direct inspection of each whole page and both supplied halves, followed by the separate page audits recorded in `progress.log`; no manuscript OCR was used. Research reviewers worked only after the freeze from the frozen text, supplied context and primary literature. Every marked reading occurrence is enumerated in the doubts records, every inventory row is marked `yes`, and the frozen hashes are checked again at final packaging.

The supplied fragment ends before several promised arguments or later pages, and missing cotes have not been reconstructed. The exact reading uncertainties, unfinished proofs, source-qualified conjectures and limits of the context-register excerpts are retained at their locations. The LaTeX fragment passed structural checks for braces, math delimiters, environments, page order and inventory coverage; a full TeX compilation was unavailable because the installed engine lacked the required format/packages.
'''

parts=[HEADER,section('B'),'## Effectivity, correspondence rings, and motivic groups\n\n',section('M'),
       '## Albanese and Picard equivalence\n\n',section('A'),
       '## Tate classes and the letter to Serre\n\n',section('RT'),
       '## Reused typed leaves\n\n',section('R'),STANDING,section('H'),REGISTER,BIB]
output='\n'.join(parts)
assert len(re.findall(r'^### (?:B|M|A|RT|R|H)\d{1,2}[a-z]? —',output,re.M))==97
assert '**Proposed note.**' not in output
(ROOT/'MPL_14_002-044_notes.md').write_text(output,encoding='utf-8')
print(f'Assembled97 notes; {len(output.split())} whitespace-delimited words; {len(output.encode())} bytes')
