"""Build the C/F result and reading ledgers from the actual TeX fragments."""
from pathlib import Path
import json
import re

work = Path(__file__).resolve().parents[1]
out = work / "sections"
passages = {
 "C1": "149; section3; manuscript32,34–35,41; scans65,70–72,83",
 "C2": "149; section3; manuscript36–38; scans74–78",
 "C3": "149; section3; manuscript37–39,44; scans75–79,90",
 "C4": "149; section3; manuscript31,36,39; scans64,73,79",
 "C5": "149; section3; manuscript32,34–36,41; scans65,70–73,83–84",
 "C6": "149; section3; manuscript39–41; scans79–82",
 "C7": "149; section3; manuscript40–42; scans80–82,85",
 "C8": "149; section3; manuscript42; scan85",
 "C9": "149; section3; manuscript46–47; scans93–95",
 "F9.1": "149; section2; manuscript25; scan52",
 "F9.2": "149; section2; manuscript25; scan52",
 "F9.3": "149; section2; manuscript25; scan52",
 "F9.4": "149; section2; manuscript25; scan52",
 "F9.5": "149; section2; manuscript25; scan52",
 "F17.1": "149; section3; manuscript49–51; scans100–103",
 "F17.2": "149; section3; manuscript49–51; scans100–103",
 "F17.3": "149; section3; manuscript49–51; scans100–103",
 "F17.4": "149; section3; manuscript50–51; scans101–103",
 "F17.5": "149; section3; manuscript50–51; scans101,103",
 "F17.6": "149; section3; manuscript49–51; scans100–103; suppliedR4,H2",
 "F17.7": "149; section3; manuscript50–51; scans101–103; readercorrectionofe",
 "F17.8": "149; section3; manuscript50–51; scans101–103; suppliedH2b",
 "ZCF1": "149; section2; manuscript20–22; scans41–46",
 "ZCF2": "149; section2; manuscript21; scans43–44",
 "ZCF3": "149; section2; manuscript23; scan47",
 "ZCF4": "149; section2; manuscript24–25; scans49–50",
 "ZCF5": "149; sections2–3; manuscript23–31; scans48–49,53–63",
 "ZCF6": "149; sections2–3; manuscript22–34,51; scans45,48–49,51,56–57,59–63,66–69,104",
 "ZCF7": "149; section3; manuscript30–31; scans62–63",
 "ZCF8": "149; section3; manuscript30; scan62",
 "ZCF9": "149; section3; manuscript33–34; scans68–69",
 "ZCF10": "149; section3; manuscript32,36,45–49; scans65,73,91–99",
 "ZCF11": "149; section3; manuscript50–51; scans101–104",
 "ZCF12": "149; section3; manuscript29–33; scans58–59,62–63,66–67",
}
notes = {
 "C1": "Smooth characteristic-zero base; type(0,0) excluded with explicit counterexample; genus-zero extension uses a removed cusp, not extension of an arbitrary map to P1.",
 "C2": "Retains the full arithmetic quotient. Geometric pro-prime-to-p quotient only in mixed/residue characteristic p. Includes (0,2),(1,0), with A1 pole counterexample.",
 "C3": "Nonabelian Kummer formula includes one cusp; scan90 full injectivity requires residue characteristic zero, otherwise quotient wild inertia; index is prime-to-p part of mu.",
 "C4": "Centre-free fibre removes the pi2 obstruction. Gm and elliptic factors require K(pi,1) base or trait. O(-1)^times over P1 refutes unrestricted exactness.",
 "C6": "Positive Kummer inertia gives +c1(normal), -c1(conormal). The requested moving-q example has colliding boundary and trivial normal line, so cannot distinguish sign.",
 "C7": "Pic finite generation has arithmetic finite-type normal hypotheses. Continuous H2 comparison includes the derived-limit check. Surjective normalizer map need not split.",
 "C8": "Ordinary units, without a circumflex, act on actual frames. Full splitting classes form completed-unit torsor.",
 "F9.1": "Relative 2-isomorphism must have the identity base component. Carlson–Stix Lemma5.4 needs reduced source, not reduced fibres.",
 "F9.2": "Pinned maps over fields; chivalrous maps for the stated relative theorem. Arbitrary topos maps are not covered.",
 "F9.4": "Finite-field counterexample checks every possible natural 2-isomorphism, not just the canonical Frobenius one.",
 "F17.2": "Explicit genus2 compact-type model, separating twist trivial on class2 but nontrivial on full group.",
 "F17.3": "Four colliding marked points; abelian inertia trivial, outer class2 twist nontrivial for every prime.",
 "F17.4": "Five cyclotomically normalized loops, but any curve with geometric group free rank3 has at most4 cusps. Checked by second agent against Nakamura2.1.1.",
 "F17.5": "Ramified quadratic twist; every residue splitting yields an actual quadratic twist over Q. Refutes e⇒a even with every-splitting quantifier.",
 "F17.6": "Full logarithmic comparison proved over a henselian DVR with residue field finitely generated over Q. Every stable node is injected and essentially cyclotomically normalized after fixing node and branches. Proper and affine stable-bad residue actions are nongeometric after every finite residue extension; graph quotient and tree cusp-rank arguments include the one-cusp case.",
 "F17.7": "For every chosen residue splitting, e is equivalent to potential good marked reduction. The potentially-good special fibre descends to k itself via the actual finite Galois action extended to the stable model and explicit projective descent. The full action comparison uses Q=Gal(K1/K)×_{Gal(k1/k)}G_k and q∘s(g)=(alpha(g),g), retaining the infinite arithmetic action. Finite-residue-extension and no-extension formulations agree in this range.",
 "F17.8": "Literal invariance under all of G_k is false: the two nodes of y2=(x2+1)^2(x2-2)+t over Q[[t]] are exchanged. Their groups are distinct by commensurable terminality. Discriminant and node jets checked exactly.",
 "ZCF4": "Fully specified trilinear surface inside (y2=x5-x)^3. Eight Groebner ideals, eighteen slice determinants,216 branch triples checked exactly.",
 "ZCF6": "Open assertions retained exactly: smallest U03/Q and Q(t)/Q section-existence cases, compatible cuspidalization, and abstract B-prime actions without open function stabilizers. The continuous B-prime family is reduced to B with its G_k^circ clause at the same base field by ZCF12; no obsolete invariant-level gap is retained. No conjecture is used as a theorem hypothesis.",
 "ZCF9": "Artin neighborhood source opened; extra finite-etale-to-punctured-P1 refinement proved by high-degree jets, simple distinct branch values, and spreading at the prescribed point.",
 "ZCF12": "Pointwise topology on the discrete union of finite-level function fields. Finite orbits of generators give a stable finite covering field and a normalized open deck subgroup. Finite Galois cover descent preserves the actual open curve and boundary; effective marked projective descent gives a quotient over k itself and an actual continuous section. The cofinal covering comparison gives an equivariant bijection of completed geometric pro-points. Thus continuous B-prime and B with the G_k^circ clause of scan61, quantified over all curves, are equivalent at fixed k. Plain B has the same comparison over finitely generated Q-fields by the checked uniqueness theorem.",
}
results = []
for name in ["C_agent.tex", "F_agent.tex", "CF_Z_agent.tex"]:
    text = (out/name).read_text()
    matches = list(re.finditer(r"\\begin\{result\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}", text))
    for i,m in enumerate(matches):
        block = text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]
        cites = sorted({k for x in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", block) for k in x.split(',')})
        ident,status,title=m.groups()
        deps = sorted(set(re.findall(r"\b(?:C[1-9]|F9\.[1-5]|F17\.[1-8]|ZCF\d+|A[1-9]|B\d+|F8a|F10[a-c])\b",block))-{ident})
        results.append({
            "id":ident,"statement":title,"status":status,
            "where_proved":f"sections/{name}; result {ident} and its following proof",
            "depends_on": "; ".join(deps+cites),
            "manuscript_passages":passages.get(ident,""),
            "depends_on_doubtful_reading":"See CF_readings.json for linked scans; no silent palaeographic resolution.",
            "notes":notes.get(ident,"All maps and hypotheses are stated in the TeX result and proof."),
        })
(out/"CF_results.json").write_text(json.dumps(results,indent=2,ensure_ascii=False)+"\n")

reading_rows = [
 (41,"k,k'→Q; same image; direction of field map", "The constants embed in a common algebraic closure Qbar. A map G_L→G_M from M→L is contravariant. The literal k→Q is impossible for a nontrivial number field.","Mathematical correction; scan not supplied for image check."),
 (47,"V|U → U|V; H1 index; types|topos", "The two constant maps2,3 into U03 refute homology-only determination in either source/target lettering. Arithmetic topos determination is a separate precisely compared map.","Independent of the doubtful alternatives."),
 (52,"topoi over X_et in the first sentence, then over S_et", "The relative statement is over S_et; the image appears to write X_et at first, an internal notational slip. The proof keeps the base 2-cell fixed.","Image inspected; mathematical necessity strong, palaeographic reading not declared settled."),
 (52,"structure à Qcts|Dcts", "Image appears to abbreviate structure à lacets as à lcts. The birational Isom theorem proves the conclusion with or without requiring peripheral preservation.","Image inspected; tentative palaeographic support only."),
 (63,"arbitrary semilinear action; no normalized profinite deck group; continuity clause", "For pointwise convergence on the discrete field of rational functions, every generator has finite orbit. ZCF12 constructs a Galois-stable finite quotient and descends it over k, proving continuous B-prime equivalent to B with its G_k^circ clause at fixed k. Abstract actions without open function stabilizers retain the extra unresolved scope.","Exact mathematical topology and reduction; no continuity word is silently inserted into the transcription."),
 (79,"pi2(S)→pi1(fibre); marginal centre-free extension and quotient", "Both centrality and centrelessness are needed for unconditional fibre injection. For type(0,2) the O(-1)^times example gives nonzero boundary; C4 states the exact range.","Image inspected, including margin; no change to the stated doubt."),
 (81,"conormal (ou normal, le diable sait)", "With positive Kummer inertia the class is +c1(normal)=-c1(conormal). The author genuinely writes both alternatives; the mathematical proof fixes a convention, not handwriting.","Image inspected; mathematical determination exact."),
 (85,"possible circumflex on first G_m(S)", "The algebraic frame torsor is under ordinary G_m(S); the full splitting torsor is under its completion. A hat on the former is mathematically false.","Image inspected; circumflex palaeography remains uncertain."),
 (90,"a) injectif; d) ne provient pas; index mu", "The image supports the negative descent condition. Full injectivity and index mu are correct in residue characteristic0; geometrically prime-to-p version uses G_K/Pwild and mu_pprime.","Image inspected; the correction concerns hypotheses, not a silently altered word."),
 (91,"facteur trivial kummérien T", "T is Zhat(1), with conjugation by the cyclotomic character. Trivial cannot mean trivial arithmetic action over a number field.","Mathematical interpretation; no palaeographic decision."),
 (93,"I≈E_Ktilde but following field has double tilde; hensélisé(strict)", "I=G_Frac(Ash); N=G_Frac(Ah). Distinct single and double tildes are needed for the residue exact sequence.","Mathematical correction exact; no final palaeographic choice."),
 (93,"(20|29); U versus X in fibre notation", "The displayed local decomposition extension is typed in ZCF.3; notation for the open curve is retained separately from its compactification.","No proof depends on choosing a manuscript equation number."),
 (95,"conormal N_D,S^{vee|*}; mu|n multiplicity", "The leading term is f_D^*(I_q/I_q²)→(I_D/I_D²)^{tensor mu}; dual notation is immaterial once this actual map is fixed.","Exact mathematical map, without resolving the glyph."),
 (102,"scindage de31; induces T→pi; T_l|Z_l", "The scan does say31, consistent with a genuine action. Its restriction yields an inner action, hence a map T→pi via pi≈Inn(pi), not literal inclusion of s(T) into pi. A Tate twist of Z_l does not affect inertia triviality in residue characteristic0.","Image inspected; exact map supplied in ZCF11."),
 (103,"c)=|⇒d)", "The unconditional comparison is c⇒d through the characteristic homological quotient. F17.2–4 refute the asserted return to good reduction and the implication to e.","No palaeographic conclusion; both quotient maps explicitly written."),
]
readings=[]
for scan,place,support,strength in reading_rows:
 readings.append({"file":"MPL_149_001-090_transcription.tex" if scan<=90 else "MPL_149_091-136_transcription.tex","scan":scan,"the_unsure_or_illegible_place":place,"what_the_mathematics_supports":support,"how_strongly":strength})
(out/"CF_readings.json").write_text(json.dumps(readings,indent=2,ensure_ascii=False)+"\n")

coverage=[
 ("F9",[52],"1-fidèle; peut-être pleinement fidèle; S de car.0?","True after exact target/base restrictions; unrestricted fullness false","F9.1–F9.5","Carlson–Stix5.4,A/B/D/E; CHW0.1; Tsujimura4.10"),
 ("F11",[65,70,71,72,83],"section rationnelle ... section régulière; codimension≥2","Proved with stated smooth-pair and arithmetic-base hypotheses","C1,C5","Bierstone–Milman1.10; purity0BMB"),
 ("F12",[74,75,76,77,78,79,90],"Théorème(?); mu.id_T; nu=1; a–e","Proved; prime-to-p domain/index corrected","C2,C3","SGA1XIII2.12,4.3,5.1–5.2"),
 ("F13",[79],"on suppose une telle suite exacte; extension ... quotient","Proved for hyperbolic fibres; centre-bearing exceptions require added hypothesis","C4","HSS5.6,8.2,proof8.3"),
 ("F14",[80,81,82],"normalisateur surjecte; conormal(ou normal); Pic fini; H2","Proved with normal sign and arithmetic/K(pi,1) scope; surjective⇒split false","C6,C7","Stix6.4,10.3; GJRW6.1; Jannsen0.2"),
 ("F15",[85],"G_m(S) sans éléments infiniment divisibles; torsors","Proved; algebraic torsor has no completion hat","C8","MilneANT5.1; explicit Kummer cocycles"),
 ("F16",[93,94,95],"D pure codim1; mu multiplicité; specialization","Proved on specified regular-and-invertible locus","C9","C1–C3; leading-term conormal map"),
 ("F17",[100,101,102,103],"a⇔b; d⇒a; ces conditions impliquent e","a⇔b proved; c,d⇒a and c,d⇒e false; e⇒a false; e⇔potentially-good proved in the stated residue-field range","F17.1–F17.8","Tamagawa5.3; Nakamura2.1.1; Hoshi3.9; Illusie7.6; MochizukiComb1.2,Ex2.5; Knudsen2.7"),
 ("Z41",[41,42,43],"tout hom compatible provient d'un plongement","False without open image; corrected open statement proved","ZCF1","Mochizuki17.1"),
 ("Z43",[43],"centralisateur ... reconstitue l'hom d'extensions","Proved with exact equivariance convention","ZCF2","Closed-graph construction; A9"),
 ("Z44a",[44],"a⇒b⇒c; b équivaut image géométrique ouverte","Open-Hom equivalence proved; stated centralizer necessity retained","ZCF1,ZCF2","Mochizuki17.1; field image and coset comparisons"),
 ("Z44b",[44,45],"toute section ... centralisateur non trivial; sans doute faux","False for full Galois centralizer; t-adic section counterexample","ZCF2","Prior return B7; F8a; cyclotomic character"),
 ("Z45c",[45],"pi_K^{Gamma-circ} nontrivial for every section","Open; smallest Q(t)/Q instance and exact obstruction recorded","ZCF6(2)","Prior return B7 checked"),
 ("Z46",[46],"G_K inverse limit of elementary models; model filtration","Limit proved; extra model filtration unnecessary for open Hom","ZCF1,A8","Finite-cover spreading; Mochizuki17.1"),
 ("Z47",[47],"hom connu par H1 géométrique","False: constants2 and3; arithmetic Kummer replacement proved","ZCF3","B2/B5; valuation of3/2"),
 ("Z48a",[48,49],"Conjecture fondamentale a⇒b","Proved via actual point maps and open-subgroup intersections","ZCF5","Prior A6,A7,AE1; F8a; C4"),
 ("Z48b",[48,49],"Conjecture fondamentale b⇒a","Open; smallest U03/Q zero-centralizer section","ZCF6(1)","Pinned-topos forgetting map explicitly located"),
 ("Z49",[49,50],"dominant maps correspond to open homs, higher-dimensional models","False; explicit smooth ample surface in C cubed","ZCF4","SGA2XII3.5; symbolic checks; Mochizuki17.1 Remark"),
 ("Z51",[51,52],"reconstruct schemes by gluing for arbitrary K","Field and relative topoi theorems proved in F9; arbitrary fields false; group-action existence programme unresolved","F9.1–F9.4,ZCF6","CHW/CS; algebraically closed and finite-field counterexamples"),
 ("Z53",[53,54],"sections point/cusp; commutative-group injection","Proved in exact range; type(0,2) exception","B2,F10a–F10c,ZCF5","Stix; prior return; Kummer"),
 ("Z55",[55,56],"pi^{Gamma-circ}=L_i; précisions conjecturales","Proved with noncuspidal versus cuspidal cases, not point exhaustion","ZCF5","Prior A6,A7,AE1 checked"),
 ("Z56",[56,57,59,60,61],"Conjecture A/B existence of point or cusp/fixed pro-point","Open for number fields; uniqueness and centralizers proved","ZCF6(1),ZCF5","Prior D0b; precise smallest test"),
 ("Z57",[57,58],"pass to function field / lift sections","Open compatible cuspidalization; known images of valuative packets proved","ZCF6(3)","C2–C3; finite-cover quotient kernels"),
 ("Z58",[58],"recover actual lifted cusps from inertia subgroups","Proved by Pi/I→conjugates and self-normalizer","ZCF5","A4/F10a; StixCor12"),
 ("Z59",[59],"continuity of section/action","Proved with explicit pointwise function-field topology; every such action descends to an arithmetic finite quotient","ZCF12,ZCF6(4)","Finite covering fields, finite generator orbits, and effective descent"),
 ("Z62a",[62,63],"all statements over cyclotomic fields","False; explicit genus4 no-point curve with section","ZCF7","Prior D5 checked, reproduced mechanism"),
 ("Z62b",[62],"same Poincare pro-cover iff common finite etale cover","Proved as scheme statement, with exact descent maps","ZCF8","Stacks32.6.1; proper descent and ramification indices"),
 ("Z62c",[62],"canonical completion extends every semilinear automorphism","Proved by finite-level descent and DVR extension","ZCF12","ZCF8; proper curve extension"),
 ("Z63",[63],"B-prime action not normalizing any deck group","Impossible under open function stabilizers: a normalized open deck subgroup and quotient over k are constructed. Continuous B-prime is equivalent to B with its G_k^circ clause; abstract actions remain open","ZCF12,ZCF6(4)","Prior D11 checked and strengthened by finite orbit compositum and projective descent"),
 ("Z64",[64],"generic-fibre pi1 square Cartesian","Proved with exact hyperbolic sequence","C4","HSS5.6 and centrelessness"),
 ("Z65",[65],"generic rational cusp extends to boundary section","Proved over normal base","ZCF10(1)","Finite birational component of etale boundary"),
 ("Z66",[66],"Gamma action on germs; admissible germs are points","Equivariant injection proved; exhaustion open","ZCF12,ZCF6(1)","Typed conjugation action; B5"),
 ("Z67",[67],"forage de trous reconstructs new groups from admissible germs","Geometric quotient kernels proved; abstract cuspidalization/exhaustion open","ZCF6(3)","Purity for curve punctures; exact lifting problem"),
 ("Z68",[68,69],"special factors enough for basis at every smooth point","Proved in characteristic zero with finite-etale genus-zero factor refinement","ZCF9","PSVProp1 plus explicit jet/branch construction"),
 ("Z71",[71,72,83,84],"purity kills codimension2 ambiguity; inertia generates kernel","Proved with geometric Hartogs step supplied separately","C1,C5","Purity0BMB; resolution"),
 ("Z73",[73],"local and generic fundamental-group maps surjective","Proved by connected-cover restriction","ZCF10","Normal-integral finite covers"),
 ("Z79",[79],"centre-free extension gives quotient even with pi2","Hyperbolic sequence iso proved; general type(0,2) counterexample","C4","HSS; O(-1) punctured line"),
 ("Z80",[80],"normalizer surjects, hence splitting?","Surjectivity proved; splitting inference false","C6,C7","Diagonal in C×C, normal degree-2 mod3"),
 ("Z82",[82],"inverse limit Kummer exactness; TatePic vanishes","Proved with Mittag-Leffler and arithmetic Pic finite generation","C7","GJRW6.1; Jannsen0.2"),
 ("Z86",[86,87,88,89,90],"failure of descent/extension; injectivity and index mu","Proved with prime-to-p qualification","C2,C3,C5","Nonabelian Kummer and coset index"),
 ("Z91",[91],"facteur trivial kummérien","Tate-module interpretation proved; trivial arithmetic action false","ZCF10","Conjugation g tau g^-1=tau^chi(g)"),
 ("Z92a",[91,92],"closed points suffice to know rational section","Proved on common domain, reduced Jacobson base","ZCF10(2)","Closed equalizer and density"),
 ("Z92b",[92,93],"henselian decomposition/inertia and local extension criterion","Proved with single/double strict fields distinguished","ZCF10(3)","Henselization, C1,C2,C4"),
 ("Z95",[95,96],"specialization where conormal coefficient is a unit; other points requested","Unit-locus statement proved; unrestricted geometric-subset characterization belongs to open lifting problem","C9,ZCF6","Explicit normal power map and Kummer change"),
 ("Z98",[96,97,98,99],"compose sections with valuative sections; first/second species","Proved at good-reduction places","ZCF10,C2,C3,C9","Actual henselian base change and normal-coordinate map"),
 ("Z102a",[102],"any(or one) splitting of31 induces T→pi","Proved via pi≈Inn(pi), not literal containment","ZCF11","Centre-free action comparison"),
 ("Z102b",[102],"p-divisible groups should detect good reduction of curve","Jacobian-only version false by compact type; nonabelian replacement proved","ZCF11,F17.1,F17.2","Explicit genus2 stable model"),
 ("Z102f",[102],"pas trop loufoque, à définir","Undefined predicate; no theorem asserted from it","ZCF6","Exact missing definition noted"),
 ("Z103",[101,103],"bad reduction produces nongeometric residue actions","False without stable-bad restriction; all stable-bad cases proved; e⇔potentially-good proved","F17.4–F17.7","Full log comparison and graph filtration; explicit quadratic twist"),
 ("ZH2a",[100,101,102,103],"essentially cyclotomic procyclic groups are peripheral","Proved over fields finitely generated over Q, including proper curves","F17.6,ZCF5","Stix20,21; PriorAE1"),
 ("ZH2b",[100,101,102,103],"each vanishing cycle preserved cyclotomically; affine count","Proved after finite extension fixing node and branches; literal whole-group invariance refuted","F17.6,F17.8","Hoshi3.9; Illusie7.6; MochizukiComb1.2,Ex2.5; HoshiMochizuki2.10,2.11"),
 ("ZR4",[100,101,102,103],"stable bad reduction cannot yield a smooth residue curve","Proved for proper and affine curves, including isomorphic CM components; Tate-lattice Torelli shortcut remains invalid","F17.6,F17.7","Full log comparison; graph quotient and toric Hom-rank; explicit effective descent"),
 ("Z104",[104],"nongeometric genuine actions above already geometric outer action","Open smallest U03/Q section case; no false reduction to F17.4","ZCF6(1),ZCF11","Exact image of point/cusp section maps"),
]
cov=[]
for ident,scans,words,verdict,statements,source in coverage:
 cov.append({"id":ident,"scans":scans,"manuscript_pages":sorted({(n-1)//2 for n in scans}),"words":words,"verdict":verdict,"statements":statements,"source_opened":source})
(out/"CF_coverage.json").write_text(json.dumps(cov,indent=2,ensure_ascii=False)+"\n")

report=['INCOMPLETE','', '# C/F contribution and complete sweep inventory for scans41–104','',
'This contribution closes the assigned named rows F9 and F11–F17 with exact scopes and counterexamples. It does not claim that the whole requested project is complete: the sweep necessarily includes the unresolved section-existence and unrestricted-action statements ZCF6. No open assertion is used as a theorem hypothesis.','',
'All scans41–104 of cote149 were read in both transcription files. Images52,79,81,85,90,102 were inspected where the mathematics depends on a reading. The report and reading ledger retain palaeographic uncertainty rather than silently correcting it.','',
'| Row | Scans | Words / assertion | Verdict | Results | Opened source |','|---|---|---|---|---|---|']
for r in cov:
 report.append('| '+ ' | '.join([r['id'],','.join(map(str,r['scans'])),r['words'],r['verdict'],r['statements'],r['source_opened']]).replace('\n',' ')+' |')
report += ['', '## Corrections to supplied notes and prior claims','',
'- R2: the centralizer theorem separates cuspidal and noncuspidal sections. Replacing noncuspidal by point-theoretic would assume the missing section-conjecture surjectivity. The checked prior return repairs the proof by unique lifted cusps and characteristic finite-cover comparisons.',
'- R3: root supplies F8a; our necessity proof uses its actual arithmetic centralizer map.',
'- H1: the invariant subgroup is the product of those prime components on which the cyclotomic character is trivial. A nonzero invariant component does not force the full character to be trivial. See ZCF5 and the prior return AE4.',
'- R4(ii): an integral Tate-module symplectic isomorphism does not by itself supply an isomorphism of principally polarized abelian varieties. The proposed Torelli shortcut is not validated. F17.6 proves the stable-bad conclusion by the full logarithmic comparison, including the genus2 fibre with two isomorphic CM elliptic components; F17.2 gives their explicit isomorphism.',
'- H2(a): the precise essentially cyclotomic normalizer statement follows from Stix20/Nakamura, including proper curves. H2(b) is now proved in F17.6 over henselian DVRs with residue field finitely generated over Q: Hoshi3.9 and Illusie7.6 supply the full comparison; MochizukiComb Example2.5 and Hoshi–Mochizuki2.11 supply the graph kernel and node injection. The statement for a particular node requires a finite extension fixing it and its branches. The literal full-Galois invariance is false by F17.8. All stable-bad proper and affine cases and the affine maximal-procyclic counting criterion are settled in this range.',
'- The requested moving-cusp sign test P1 minus{0,infinity,t^mu u} is not a smooth marked family over the trait: its boundary collides. It checks the local multiplicity, but its normal line is trivial and cannot detect the global Chern sign. C6 gives the gluing computation and O(-1) sign test.',
'- The reader’s e⇒a suggestion is false even when every residue splitting is allowed: F17.5 computes the resulting actual quadratic twist. Homological c,d⇒e is also false, by F17.4. The corrected e⇔potentially-good statement is proved in F17.7; the explicit finite Galois action on the good model and its projective descent show that finite residue extension can be removed in this precise range.',
'- The finite-field fullness counterexample checks all natural automorphisms of the identity topos by restriction to closed points of every degree. It does not rely solely on a preferred Frobenius 2-cell.',
'- The reader’s continuity reduction is correct for the explicit topology of pointwise convergence on the discrete rational-function field. The finite-generator proof in the prior return D11 was checked directly. ZCF12 strengthens it: all generator orbits are finite, their compositum gives a deck group normalized by the whole Galois group, and finite Galois projective descent gives a quotient over k itself. Thus continuous B-prime is equivalent to B with its G_k^circ clause of scan61 at fixed k, each quantified over all hyperbolic curves. The comparison is an equivariant bijection of completed geometric pro-points. Over finitely generated Q-fields the checked uniqueness theorem also gives the plain B formulation. The earlier draft’s invariant-level gap is withdrawn. Fixed-point existence remains open, and abstract actions without open function stabilizers retain the extra unresolved scope.',
'', '## Computations actually run','',
'`CF_checks.py` verifies the genus2 discriminant, the elliptic component discriminants, the four-puncture class-two action and its failure to be inner, the five peripheral homology lines, the quadratic twist substitution, the Legendre j difference, Kummer multiplicity/index examples, and the finite-field root-count inequality. `CF_hyperplane.py` verifies all eight affine singularity ideals, eighteen branch-slice determinants, and216 full branch triples for the explicit surface in ZCF4. `CF_h2_checks.py` verifies the conjugate-node sextic discriminant and node jets, all153 thickness/modulus pairs used as finite checks of the node map, the CM-component isomorphism, and smoothness of both components modulo5. All three scripts and their JSON outputs are saved.','',
'## Precise remaining work','',
'ZCF6 gives each exact unsolved statement, its smallest instance, all routes tried, and their failure points. The strongest proved reductions are: zero cyclotomic centralizer iff noncuspidal; at most one fixed pro-point; a birational section with nonzero centralizer iff a unique rational place; full pinned-topos maps from a field are actual points; and every semilinear action with open function stabilizers is an ordinary section action for a finite hyperbolic quotient over the same base field. The unconstructed maps are the pinned-topos lift of an arbitrary noncuspidal section and compatible lifts through all puncturing quotients. Continuous B-prime has no additional finite-level obstruction. Its existence assertion remains that of B with its G_k^circ clause; without the open-stabilizer hypothesis the finite generator orbit construction can fail, and the abstract-action problem remains explicit.','',
'## Deliverable fragments','',
'C_agent.tex; F_agent.tex; CF_Z_agent.tex; CF_results.json; CF_readings.json; CF_coverage.json; CF_refs.bib; CF_sources.md; this CF_report.md; code/CF_checks.py and output; code/CF_hyperplane.py and output; code/CF_h2_checks.py and output; code/CF_make_ledgers.py. Root is responsible for final assembly, compilation, ZIP and upload.']
(out/"CF_report.md").write_text('\n'.join(report)+'\n')
for name in ["CF_results.json", "CF_readings.json", "CF_coverage.json", "CF_report.md"]:
    (work/name).write_text((out/name).read_text())
print(f"Wrote {len(results)} result rows, {len(readings)} readings, {len(cov)} coverage rows.")
