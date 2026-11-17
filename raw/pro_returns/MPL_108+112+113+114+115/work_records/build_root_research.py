"""Post-freeze research only. Never writes a transcription file."""
from pathlib import Path
import json, re, subprocess

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable/work_records'
rows=[]
def add(id,title,cote,scans,kind,quote,note,context,query):
    rows.append(dict(id=id,title=title,cote=cote,scans=scans,kind=kind,quote=quote,note=note,context=context,query=query))

add('R10801','Čech asphericity and the unidentified L5',108,[3],'conjecture',
    r'\v{C}ech type asphericity condition (implied by L 5)?)',
    'Item 1 asks whether the Čech-type condition follows from L5; it neither states L5 nor gives the implication. The later localizer axiom labels must therefore not be substituted for this label without a source identification.',
    'PURSUING_STACKS_CONTENTS.md §§35,60,64–65; RESULTS_STATE REVLOC F.1 (run claim); relation: precursor, not a proof of relative Theorem A.',
    'Cech|Čech|Verdier|L.?5|REVLOC.*F.1')
add('R10802','Saturation of the two weak-equivalence classes',108,[3],'unproved claim',
    r'$\underline W$, $W_A$ saturated',
    'The word “saturated” is recorded without a proof or the meaning of saturation, while only the item number is deleted. This is an agenda assertion, not evidence that every proposed class satisfies all fundamental-localizer axioms.',
    'PURSUING_STACKS_CONTENTS.md §41; companion/chunks/DER_XIIb-a.tex, localizer discussion; RESULTS_STATE REVLOC F.1; relation: earlier programme.',
    'satur|REVLOC.*F.1')
add('R10803','Homotopy and Dold–Puppe sequences in Cat',108,[3],'conjecture',
    'Dold-Puppe sequences.',
    'The listed “Homotopy properties” and Dold–Puppe sequences are questions about the categorical modelizer, with the preceding qualifier cancelled. They anticipate the integration and abelianization discussion, but no sequence, convergence statement, or comparison morphism is supplied.',
    'ps_chapters_VI_VII/ps7.tex §134, ms557–560, and §135; RESULTS_STATE GALOIS G.6 and RESIDUE I.7 are related open leads, not consequences.',
    'Dold|Puppe|GALOIS.*G.6|RESIDUE.*I.7')
add('R10804','A model structure on Cat',108,[3],'conjecture',
    'a model category?',
    'The explicit question about Cat is separate from the Dold–Puppe agenda. The supplied contents point to the retained PS discussion of Thomason, so this records an undated question witness alongside that discussion rather than a new model-structure result.',
    'PURSUING_STACKS_CONTENTS.md §87, “Comments on Thomason’s paper on closed model structure”; relation: question later addressed in the named discussion.',
    'Thomason|model category|model structure')
add('R10805','Which presheaf categories have the intended model structure?',108,[3],'conjecture',
    'a (closed) model category?',
    'The question asks “When”, leaving both hypotheses on A and the intended weak equivalences open. Ara §4.6 supplies a modern sufficient hypothesis for the canonical weak equivalences when A is a local test category; that result should not be read back as a statement on this sheet.',
    'PURSUING_STACKS_CONTENTS.md §§29,31,39,65; primary [Ara] §§4.4–4.6; relation: question with a later sufficient answer.',
    'local.test|closed.model|canonical.model|test categor')
add('R10806','Exactness of the localized homotopy category',108,[3],'conjecture',
    'Exactness properties',
    'The exactness of Hot_W and of the two displayed canonical functors is only listed, and two arrowheads remain uncertain in the frozen reading. No preservation of a particular finite limit, Kan extension, or base-change square follows from this agenda entry.',
    'DOSSIER_STATEMENTS_WITH_STATUS.md BISITE E.1–E.14 and F; ps_chapters_VI_VII/ps7.tex §136; relation: precursor only.',
    'exact|Hot|Kan|BISITE.*E.')
add('R10807','The negative answer for the opposite simplex category',108,[3],'unproved claim',
    r'Is the category $\Delta^\circ$ a test category, or wtc?',
    'Item 6c answers both alternatives by the underlined English “no”, with no proof. This confirms the substance of Hua’s finding while retaining the actual language and the explicit weak-test alternative.',
    'RESULTS_STATE, Hua findings register 108-delta-op-not-test (conjecture, unsearched); hua_project/108.modern.tex p2; relation: confirms and sharpens wording.',
    '108-delta|Delta|Δ|weak test')
add('R10808','Why Δ opposite is neither weak nor local test',108,[3],'own idea',
    r'\uline{no}',
    'Verification of the lead credited to Hua: if a small category A has an initial object 0, the category of elements A/X of any presheaf decomposes by X(0), each component having initial object (0,x), so all its represented homotopy types are discrete. Consequently A cannot be weak test, and each slice A/a again has an initial object, so A is not local test either; apply this to A=Δᵒᵖ, whose initial object is [0], to exclude test and strict test as well. Confidence: high, because this is a direct category-of-elements argument with the weak/local definitions, not a claim of novelty.',
    'Hua findings register 108-delta-op-not-test; primary [Ara] §§4.4–4.5 for definitions; relation: elementary verification of the open lead.',
    '108-delta|weak.test|local.test|initial object')
add('R10809','Other shapes and cubical games',108,[3],'conjecture',
    'Cubical games',
    'Items 6a–b list Δ_f and three O-shaped symbols, then cubical games, without saying that each is a test category. The O symbols and their decorations remain diplomatic readings; assigning them specific modern cubical categories would be an interpretation.',
    'PURSUING_STACKS_CONTENTS.md §§22,34,43,98; hua_project/108.modern.tex p2 and 114.modern.tex p2; relation: related examples, with an unresolved identification.',
    'cub|cube|Simplexf|Delta|Delta_f')
add('R10810','Cohomology invariants and axiomatized Dold–Puppe',108,[3],'conjecture',
    'Dold Puppe axiomatized?',
    'Item 7 asks for an axiomatization and singles out the O-shaped category after an uncertain cohomology heading. The inserted “comm.” does not justify replacing the live heading by a fully cancelled one or identifying the category from the theory alone.',
    'ps_chapters_VI_VII/ps7.tex §§134–135; hua_project/108.modern.tex p2; RESULTS_STATE RESIDUE I.7; relation: precursor and reading difference.',
    'Dold|Puppe|cohomolog|commut')
add('R10811','Integration as a direct limit and its dual',108,[3],'conjecture',
    r'as a $\varinjlim$',
    'The note explicitly proposes integration of homotopy types as a direct limit, together with a dual notion and an internal structure on Hot. Hua’s modernized inverse-limit wording differs from the frozen symbol, so it is a reading question rather than a correction to make.',
    'hua_project/108.modern.tex p2; PURSUING_STACKS_CONTENTS.md §69; ps_chapters_VI_VII/ps7.tex §136, ms566–568; relation: precursor, with direct/inverse-limit difference.',
    'integration|intégr|varprojlim|varinjlim')
add('R10812','Topological spaces and geometric realization',108,[3],'conjecture',
    'Geom. realization',
    'Item 9 asks for test functors into topological spaces and marks geometric realization in the margin. No choice of topology, realization functor, or preservation theorem is stated, so this remains a separate modelizer problem.',
    'PURSUING_STACKS_CONTENTS.md §§27,59; relation: matching programme topic.',
    'geometric realization|topological spaces|Spaces|réalisation')
add('R10813','Group objects and pointed connected types',108,[3],'conjecture',
    'modelizer for pointed 0-connected homotopy types',
    'Item 10 asks whether group objects in a modelizer model pointed connected homotopy types, and itself questions whether strictness is needed. The later schematic and Dold–Puppe discussions are relevant, but the question is not a theorem for an arbitrary M.',
    'PURSUING_STACKS_CONTENTS.md §71; ps_chapters_VI_VII/ps6.tex §§121–126; RESULTS_STATE RESIDUE I.7 and GALOIS G.6 only as neighbouring coefficient questions.',
    'pointed|group objects|Dold|Puppe|strict')
add('R10814','Base-change fibrations: the proposed test family',108,[4],'unproved claim',
    'il suffit que ce soit OK',
    'Item 11 defines the intended fibrations by preservation of all weak equivalences under pullback and asserts that final-object inclusions suffice. The assertion needs a factorization or localizer-generation argument; the sheet does not supply one.',
    'companion/chunks/DER_XIIb-a.tex, smooth/proper and base-change discussions; DOSSIER BISITE E and RESIDUE D; relation: precursor, not strong W(7).',
    'fibr|changement de base|base.change|final object')
add('R10815','Do simplex-point inclusions suffice?',108,[4],'conjecture',
    'Est-il suffisant',
    'The second part of item 11 asks whether it suffices to test every Δ₀→Δₙ→X, with “tout” inserted. This is a narrower generating-family question than the preceding assertion, and is not answered on the remaining leaves.',
    'PURSUING_STACKS_CONTENTS.md §§70,72–74; DOSSIER BISITE E; relation: more specific unproved precursor.',
    'simplex|Simplex|fibr|base.change')
add('R10816','The pullback axiom for a Quillen structure',108,[4],'conjecture',
    'dans axiomatique de Quillen.',
    'Item 12 proposes the implication “f fib, g∈W ⇒ g′∈W” in the Cartesian square. This is the right-properness pattern for the chosen fibrations, not an unrestricted assertion that all pullbacks preserve W.',
    'DOSSIER BISITE F.2 and RESIDUE C.1; ps_chapters_VI_VII/ps7.tex §§136–137; relation: ordinary precursor, with a fibration hypothesis.',
    'Quillen|proper|pullback|fibration')
add('R10817','Connectedness versus total asphericity of a topos',108,[4],'conjecture',
    '0-connected topos also totally',
    'Item13 first asks whether a 0-connected topos is totally infinity-connected, with “tot” deleted before the first condition. It is the first related question in this package’s physical order, not the later all-outgoing-functors definition of total asphericity and not a filteredness assertion.',
    '114 scan003–004; companion/chunks/DER_XIIb-a.tex ms88–89 explicitly distinguishes the later notion; RESULTS_STATE TOTASPH D.7, RESIDUE F.5; relation: different notion.',
    'totale|totally|0.connected|TOTASPH.*D.7|RESIDUE.*F.5')
add('R10818','Internal Homs and diagram categories',108,[4],'conjecture',
    'and diagram variants',
    'Item 14 requests Homs in Hot and diagram variants but gives no enrichment, mapping-object construction, or coherence data. The later derivator questions make the direction intelligible without supplying the omitted construction on this page.',
    'DOSSIER BISITE F.17–F.18 and RESIDUE I.1; RESULTS_STATE BISITE F.18; relation: precursor only.',
    'internal.Hom|mapping|diagram|BISITE.*F.18')
add('R10819','A relative topos defined by a stack',108,[4],'conjecture',
    r'un \uline{champ} sur $B$',
    'The first item numbered 15 proposes a relative topos defined by a stack on B; the abbreviation before it remains uncertain. This is a programme for relative coefficients, not a stated correspondence-composition or gluing theorem.',
    'PURSUING_STACKS_CONTENTS.md §§16,69–70; DOSSIER BISITE A–B and STRATA; relation: general precursor.',
    'champ|relative.topos|stack|topos')
add('R10820','Cointegration and a relative homotopy spectral sequence',108,[5],'conjecture',
    'Suite spectrale',
    'The second item numbered 15 asks for a spectral sequence relating homotopy sheaves of Rf_*ξ to Rⁱf_*Πⱼξ. It states neither indexing conventions nor convergence hypotheses, and the leftward arrow must not be converted into a completed spectral-sequence theorem.',
    'ps_chapters_VI_VII/ps7.tex §§136–138; companion/chunks/DER_XIIb-a.tex, integration/cointegration; DOSSIER RESIDUE I; relation: precursor with missing hypotheses.',
    'spectral|cointegr|cointégr|homotopy.sheav')
add('R10821','Contractors and localization by homotopisms',108,[5],'conjecture',
    r'localisés par les \uline{homotopismes}',
    'Item 16 asks whether i_A and j_A become mutually inverse after inverting homotopisms. This is stronger or at least differently specified than merely passing to the usual weak-homotopy localization, so a theorem about test categories alone does not answer the wording.',
    'PURSUING_STACKS_CONTENTS.md §§48–55,95; primary [PS] §95 Proposition3; relation: contractor link, with localization classes to distinguish.',
    'homotopism|contractor|contracteur|j_A')
add('R10822','Contractibility detected by categories of elements',108,[5],'conjecture',
    'Est-il vrai que $X$',
    'The first subsidiary question compares contractibility of a presheaf X with that of A/X. The intended interval homotopy structure must be fixed before replacing “contractible” by weakly contractible.',
    'PURSUING_STACKS_CONTENTS.md §§49–55,79,95; relation: question about contractibility, not a restatement of a localizer equivalence.',
    'contractib|category of elements|homotop')
add('R10823','Contractibility detected by the right adjoint',108,[5],'conjecture',
    r'\forall C',
    'The next question compares contractibility of C with that of its j_A-image, with a visible insertion identifying the notation. Neither direction is proved here, and it should remain distinct from the preceding question about i_A.',
    'PURSUING_STACKS_CONTENTS.md §§36–39,95; relation: adjoint companion to R10822.',
    'j_A|nerve|contractib')
add('R10824','The product comparison and its variants',108,[5],'conjecture',
    'un homotopisme ?',
    'The product comparison i_A(X×Y)→i_A(X)×i_A(Y) is asked to be a homotopism, followed by uncertain “cohomotopes|commutatives” variants. The adjective is a reading issue, while the distinction between a homotopism and a weak equivalence is a mathematical issue.',
    'PURSUING_STACKS_CONTENTS.md §§39–40,74; primary [Ara] §4.5; relation: product question stronger than the weak-equivalence definition alone.',
    'product|homotopism|strict.test|cohomot')
add('R10825','The final Dold–Puppe/Whitehead reminder',108,[5],'conjecture',
    '17 Dold-Puppe, Whitehead etc',
    'Item 17 is only a reminder, with no proposition to extract. Its natural continuation is the abelianization programme of cotes112–113 and PS VII, but it cannot by itself establish a homology-detection theorem.',
    'ps_chapters_VI_VII/ps7.tex §§134–135; RESULTS_STATE RESIDUE I.7; relation: programme link.',
    'Whitehead|Dold|Puppe')
add('R10826','Total asphericity does not suffice for a modelizing topos',108,[6],'unproved claim',
    r"même s'il est de la forme $\widehat A$",
    'The final leaf explicitly denies that total asphericity, possibly qualified here by the uncertain word “strict”, suffices for being modelizing, even for a presheaf topos different from Ens. Its proposed finite-product category has a zero object, connecting it to the initial-object obstruction in R10808; this is not a statement about the later TOTASPH definition.',
    'hua_project/108.modern.tex, “Le feuillet mobile”; [PS] §95; RESULTS_STATE TOTASPH A.7/D.7 and RESIDUE F.5; relation: different notion and a reversed paraphrase in Hua.',
    'feuillet mobile|zero|initial|totally|TOTASPH')
add('R10827','The cancelled algebraic example',108,[6],'withdrawn in the same text',
    'Prendre',
    'The proposed category of rings on the final leaf is struck through and partly unreadable. It is evidence of an attempted example, not a valid counterexample that may be completed from the expected algebra.',
    'hua_project/108.modern.tex, final leaf; relation: cancellation preserved, candidate unresolved.',
    'anneaux|rings|feuillet|contracteur')
add('R10828','The nontrivial-contractor conclusion',108,[6],'unproved claim',
    r'\uline{sauf} si $A\simeq\Delta_0$',
    'The live conclusion says a contractor is test except when equivalent to Δ₀. The retained PS §95 Proposition3 supplies the matching nontrivial-contractor theorem, whereas Hua’s final paraphrase reverses the exception; no proof needs to be reconstructed here.',
    '[PS] §95 Proposition3, ms346–347; hua_project/108.modern.tex final section; relation: matching retained PS theorem, different Hua wording.',
    'contractor|contracteur|sauf|Delta_0')

add('R11201','Smoothness is a quasi-isomorphism condition',112,[3],'reading question',
    'est un quasi-iso.',
    'The definition makes the two integration values quasi-isomorphic along each arrow of A. Hua’s modernization writes an isomorphism; this can be compatible only after specifying a derived category, and must not replace the literal quasi-isomorphism wording.',
    'hua_project/112.modern.tex, “Lisse”; ps_chapters_VI_VII/ps7.tex §134; Hua findings register 112-linearization-beyond-the-simplex; relation: reading/level distinction.',
    'lisse|quasi-iso|isomorphisme|112-linearization')
add('R11202','Negligibility and the coefficient variance',112,[3],'unproved claim',
    'quasi-nul',
    'Negligibility is explicitly defined by pointwise quasi-null integration, while the margin calls the resulting object a system of twisted coefficients. The displayed B-based target is retained despite the A-based starting data; identifying B or the b/flat superscript is necessary before treating the construction as a fully specified functor.',
    'hua_project/112.modern.tex, negligibility and twisted coefficients; RESULTS_STATE GALOIS G.6 and RESIDUE I.7; relation: adds readable definition, unresolved variance.',
    'négligeable|neglig|tordus|GALOIS.*G.6|RESIDUE.*I.7')
add('R11203','The proposed localization equivalence',112,[3],'conjecture',
    'est-ce une équivalence de catégories',
    'Question1 asks whether the localization of smooth abelian presheaves gives the displayed locally constant derived category. Neither the weak-equivalence class W_q nor the A/B comparison is fully fixed on this sheet, so this remains a precise research direction with unresolved input conventions.',
    'Hua findings register 112-linearization-beyond-the-simplex; ps_chapters_VI_VII/ps7.tex §134, ms557–560; RESULTS_STATE GALOIS G.6; relation: manuscript form of the lead.',
    '112-linearization|localement constant|locally constant|GALOIS.*G.6')
add('R11204','The simplex case and the slice question',112,[3],'self-flagged',
    r'OK pour $A=\Delta$, mais est-ce OK',
    'The margin accepts the simplex case and explicitly asks about Δ/X. That qualification prevents extending the claimed comparison automatically to slices merely because the simplex case is familiar.',
    'ps_chapters_VI_VII/ps7.tex §134; Hua findings register 112-linearization-beyond-the-simplex; relation: explicit unresolved extension.',
    'Simplex|Delta|slice|112-linearization')
add('R11205','An external route for the Dold–Kan comparison',112,[3,4],'own idea',
    r'$A=\Delta_{/X}$',
    'The Whitehead test-category hypotheses in Hubert’s thesis offer a route to testing the requested extension beyond Δ: the thesis constructs homology model structures and derived Dold–Kan equivalences for the stated classes. Confidence: medium as a route, because its abstract does not by itself identify the sheet’s twisted-coefficient target, W_q, or the literal A/B comparison, so it is not being cited as an answer to Question1.',
    'Primary [Hubert], abstract and stated scope; ps_chapters_VI_VII/ps7.tex §134; relation: later method to compare, not closure of GALOIS G.6.',
    'Whitehead|Dold|Kan|GALOIS.*G.6')
add('R11206','The aspherical-base simplification',112,[3],'unproved claim',
    'est asphérique',
    'The diagram identifies the locally constant derived target with D(Ab) in the aspherical case. Establishing the exact statement requires its boundedness, coefficient variance, and meaning of “locally constant”; the sheet supplies no argument checking these choices.',
    'ps_chapters_VI_VII/ps7.tex §§134–135; RESULTS_STATE GALOIS G.6; relation: special-case claim, not a higher-coefficient derivator construction.',
    'asph|locally constant|loc.const|GALOIS.*G.6')
add('R11207','The uncertain total-asphericity margin',112,[3],'reading question',
    r'\uline{NB} Si $A$ est tot. asph.',
    'The angled margin about all “pt” and quasi-isomorphisms remains low confidence in the frozen transcription. It cannot be promoted to a theorem on all points or all presheaves from the surrounding mathematics, and it supplies no filteredness assertion.',
    'hua_project/112.modern.tex; RESULTS_STATE TOTASPH D.7 and RESIDUE F.5; relation: uncertain wording, no usable solution.',
    'tot.*asph|quasi.iso|TOTASPH.*D.7')
add('R11208','The Ext comparison',112,[3],'conjecture',
    r'pour }i>0',
    'Question2 asks for the displayed comparison on positive Ext groups, with a further simplification in the aspherical case. The arrow is written, but an isomorphism is not proved and the A/B coefficient rings remain part of the question.',
    'hua_project/112.modern.tex, second question; ps_chapters_VI_VII/ps7.tex §§134–135; relation: same unresolved comparison, with literal variance retained.',
    'Ext|Whitehead|112-linearization')
add('R11209','Removing smoothness in the Ext question',112,[3],'conjecture',
    'même sans supposer',
    'The bracket asks whether the Ext comparison still holds without smoothness. This is a separate strengthening and is not implied merely by an equivalence on the smooth subcategory.',
    'hua_project/112.modern.tex, second question; RESULTS_STATE GALOIS G.6; relation: explicit stronger question.',
    'sans supposer|lisse|Ext|GALOIS.*G.6')
add('R11210','Replacing objects by complexes',112,[3],'conjecture',
    'et peut-on y remplacer',
    'An insertion extends Question2 from objects to complexes. Any answer needs resolution or derived-functor hypotheses, particularly if the intended complexes are not bounded in the direction later indicated on scan004.',
    'ps_chapters_VI_VII/ps7.tex §§134–135; hua_project/112.modern.tex; relation: explicit extension of the Ext question.',
    'complex|résolution|resolution|Ext')
add('R11211','Realizing a homotopical truncation',112,[3],'conjecture',
    'au tronqué',
    'Question3 seeks L→L′ whose linearization realizes a homotopical truncation, with the cutoff sign still ≤|<. The prior vanishing assumption is deleted before the new formulation, so it must not be retained as a live hypothesis; Hua’s unreadable-third-question report is materially less informative than this frozen reading.',
    'hua_project/112.modern.tex, third question; ps_chapters_VI_VII/ps6.tex §§112–113,122,126; relation: recovered formulation and a Postnikov link.',
    'tronqu|Postnikov|112-linearization')
add('R11212','Bounded and bounded-above linearization',112,[4],'unproved claim',
    r'\uline{équiv. cat.}',
    'The loose A/B/C programme asserts quasi-inverse equivalences of bounded-above locally constant derived categories and writes homology preservation by φ. These claims need the missing relation between A and B and must not be read as equivalences for arbitrary pairs of small categories.',
    'hua_project/112.modern.tex, following sheet; ps_chapters_VI_VII/ps7.tex §134; RESULTS_STATE GALOIS G.6, RESIDUE I.7; relation: expanded programme with missing hypotheses.',
    'bounded|born|D_.*lc|GALOIS.*G.6|RESIDUE.*I.7')
add('R11213','Smooth, cosmooth, and cohomological terminology',112,[4],'unpursued implication',
    r'c\text{-lisse}',
    'The isolated c-lisse/c-propre box and the lisse/colisse pair suggest that the linearization programme is being compared with cohomological smoothness and properness. The diagrams do not define a six-operation formalism or identify which later notion is intended.',
    'ps_chapters_VI_VII/ps7.tex §§136–138, especially ms571–573; DOSSIER BISITE E–F and RESIDUE I; relation: terminology precursor only.',
    'cohomologically|smooth|proper|colisse|c-lisse')
add('R11214','The loose free-coefficient calculation',112,[5],'unproved claim',
    r'F*k^{(b_\beta^\circ)}\simeq F(b_\beta)',
    'The reused sheet combines representable/free-coefficient expressions, Hom pairings, and a derived-category comparison without a connected proof. These may provide a calculation to reconstruct once the uncertain indices are resolved, but they do not close the three questions on scan003.',
    'hua_project/112.modern.tex p4; PURSUING_STACKS_CONTENTS.md §§99–108; ps_chapters_VI_VII/ps7.tex §§134–135; relation: exploratory calculation.',
    'integrator|Add|Hom|linearization')

add('R11301','The cancelled MU-fibration integration criterion',113,[3],'withdrawn in the same text',
    'subm',
    'The crossed draft proposes three hypotheses involving an aspherical indexing category, boundary submersions, and transition maps factored as a submersion followed by a monomorphism. It is a cancelled working criterion for semi-simplicial MU-fibrations, not a proof of the later path-localization or coherent-gluing results.',
    'DOSSIER PATHS A–C and E; companion/chunks/DER_XIIb-a.tex, integration discussion; relation: limited precursor, cancellation retained.',
    'MU|submersion|semi.simplic|intégration|PATHS')
add('R11302','The additive presheaf category and scalar structure',113,[4],'unproved claim',
    'ne dépend pas du choix',
    'The initial definition identifies additive Ab-valued functors with k-linear Ab_k-valued functors and says the resulting category does not depend on the chosen k-additive structure. The underlying additive category and the k-enrichment should be distinguished when using that independence assertion.',
    'hua_project/113.modern.tex, opening additive-topos section; PURSUING_STACKS_CONTENTS.md §§104–107; relation: foundational assertion for this calculation.',
    'k-add|additive|Ab_k|indépend')
add('R11303','Karoubi completion and ultraprojectives',113,[4],'unproved claim',
    r'\operatorname{UlProj}',
    'The page identifies Kar(P) with the ultraprojectives of the additive presheaf category and states that passing from P to Kar(P) leaves that category unchanged. This is the small-projective core of the argument and must be kept distinct from the later phrase “assez de projectifs”.',
    'hua_project/113.modern.tex, additive topoi; hua_project/115.modern.tex p13; RESULTS_STATE Hua 115-isbell-envelope-self-dual; relation: additive Morita precursor, not reflexivity equality.',
    'UlProj|ultraproject|Kar|Morita')
add('R11304','The recognition claim is too broad for ordinary projectives',113,[4],'unproved claim',
    'a assez de projectifs.',
    'The criterion says “assez de projectifs”, then permits P=UlProj, but ordinary projectives do not suffice: published Grothendieck-category counterexamples have enough projectives without a small family of compact projective generators. Saorín–Šťovíček §5 explicitly includes the many-object module-category setting, and Bazzoni et al. Corollary4.5/Theorem6.3 provide the original tilting-heart construction, with the many-object bridge checked in the secondary review. Thus the assertion is false under the ordinary meaning of projective; a small generating family of compact/ultraprojective objects is the additional condition, while any strengthened meaning of the manuscript word remains an editorial interpretation.',
    'hua_project/113.modern.tex, recognition discussion; PURSUING_STACKS_CONTENTS.md §§104–107; primary [Saorin-Stovicek] §5 and [Bazzoni] Cor4.5, Proposition6.2, Theorem6.3; relation: known counterexample to the literal generality.',
    'assez de projectifs|ultraproject|Grothendieck|génératrice')
add('R11305','Three adjoints and the ambiguous 2-categorical diagram',113,[4],'unproved claim',
    'admet adjoint à droite',
    'The proposed morphisms have a colimit-preserving f_! whose right adjoint f* also preserves colimits and has a further right adjoint. The 2-essential-surjectivity and doubtful “3-fid.” label are not proved, and should not be normalized into a standard Morita 2-equivalence without specifying its morphisms.',
    'hua_project/113.modern.tex, morphisms of additive topoi; DOSSIER BISITE B and RESIDUE I; relation: ordinary adjoint programme, not ambidexterity.',
    'adjoint|Morita|2-essential|2-ess|3-fid')
add('R11306','Density and the two free-completion properties',113,[4],'unproved claim',
    r'\varinjlim_{P/L}',
    'The density display and the two Hom equivalences assert additive free cocompletion and its opposite limit version under the indicated completeness assumptions on M. These support later curryings, but they are not a general preservation theorem for an arbitrary exact square.',
    'hua_project/113.modern.tex, universal properties; hua_project/115.modern.tex p5; DOSSIER BISITE E.1–E.14; relation: ordinary universal-property precursor.',
    'cocompletion|cocompl|Yoneda|universel|universal')
add('R11307','The two module actions and opposite variance',113,[6],'unproved claim',
    'les deux types de lim',
    'The page couples the Hom action and the convolution action, then interchanges them by taking opposites when M has both types of limits. This is an ordinary additive duality statement, and its vee/circle signs should not be treated as interchangeable.',
    'hua_project/113.modern.tex, Hom and convolution; PURSUING_STACKS_CONTENTS.md §§105–107; DOSSIER RESIDUE I; relation: ordinary pairing, not exceptional duality.',
    'convolution|coend|oppos|dualité|dual')
add('R11308','The finite-family tensor construction',113,[6],'unproved claim',
    'de façon 2-universelle',
    'The manuscript specifies the bilinear universal property, then constructs P⊗_kQ by finite formal sums and a matrix Hom formula. A complete proof needs composition and the universal functor on finite sums; the sheet gives the ingredients and the smallness claim rather than checking every coherence.',
    'hua_project/113.modern.tex, tensor product; PURSUING_STACKS_CONTENTS.md §109; relation: explicit construction, no later higher coherence theorem.',
    'bilin|Bil|tensor|tenseur|2-univers')
add('R11309','The Yoneda realization of the tensor product',113,[6,8],'unproved claim',
    'pl. fid !',
    'The full-faithfulness assertion at the end of scan006 is continued on scan008 by the finite-sum subcategory of bilinear representables. Its scope is P⊗Q on those generators, not the much larger tensor product of all presheaves asserted later.',
    'hua_project/113.modern.tex, tensor construction and later curryfication warning; relation: a valid scope distinction essential for R11313.',
    'Yoneda|pleinement|fully faithful|curry')
add('R11310','Coefficient categories and the dual additive topos',113,[8],'unproved claim',
    'Application 1',
    'Application1 identifies P-valued coefficients in Q-presheaves with presheaves on P⊗Q and gives the opposite/dual counterpart. The displayed currying calculation is evidence for this specific assertion, with the uncertain “alg.” qualifier still unresolved.',
    'hua_project/113.modern.tex, Application1; PURSUING_STACKS_CONTENTS.md §§104–107; relation: direct ordinary currying calculation.',
    'Application 1|dual|curry|algébrique')
add('R11311','The cocontinuous bilinear universal property',113,[8,10],'unproved claim',
    'Appl. 2',
    'Application2 is followed by an iterated-Hom proof on scan010, so it should not be listed as wholly abandoned. What remains to check is the stated completeness/colimit hypotheses and enrichment conventions; it is the completed presheaf category that represents separately cocontinuous bilinear functors.',
    'hua_project/113.modern.tex, Application2; PURSUING_STACKS_CONTENTS.md §§106–107; relation: assertion with a proof sketch in the package.',
    'Bil|cocont|Application 2|tensor')
add('R11312','The dual universal property',113,[10],'unproved claim',
    'Dualement',
    'The dual formula is asserted immediately after the proof of Application2. It requires taking the appropriate opposite categories and projective-limit hypotheses, not replacing lower exclamation marks by primes.',
    'hua_project/113.modern.tex, dual version of Application2; PURSUING_STACKS_CONTENTS.md §§105–107; relation: asserted dual of the preceding calculation.',
    'Dualement|limit|Hom|variance')
add('R11313','The full-faithfulness claim for arbitrary coefficients',113,[10],'self-flagged',
    'pl. fid ?',
    'Application3 asserts full faithfulness of P-presheaves⊗M→Hom(Pᵒᵖ,M), but its attempted proof itself marks the decisive arrow “pl. fid ?”. Hua’s modernization gives the finite-rank obstruction, so this claim must not be treated as proved by the diagram.',
    'hua_project/113.modern.tex, “La curryfication”; relation: confirmed self-flag and previously supplied counterexample lead.',
    'curryfication|rang fini|finite.rank|pl. fid')
add('R11314','A concrete check of the finite-rank obstruction',113,[10,12],'own idea',
    'pl. fidèle',
    'Check of the counterexample credited to Hua’s project: over a field, take the additive finite-free generator category and an infinite-dimensional vector space E; the comparison on the pairs (k,E) and (E,k) contains E⊗E*→End(E), whose image consists of finite-rank maps and misses the identity. Confidence: high, because this elementary Hom calculation disproves fullness under the unqualified infinite-dimensional reading; it is a verification of the supplied lead, not a new counterexample claim.',
    'hua_project/113.modern.tex, “La curryfication”; relation: verifies its obstruction to scans010/012, without changing text.',
    'curryfication|dimension infinie|rang fini|finite.rank')
add('R11315','The universe enlargement is explicitly flagged',113,[10],'self-flagged',
    'Attention, il faut passer à un univers plus gros',
    'The universe warning is part of the proposed full-faithfulness argument, not a licence to ignore size. Enlarging the universe addresses formation of the functor category but does not remove the finite-rank obstruction.',
    'hua_project/113.modern.tex, “La curryfication”; relation: explicit size caveat plus independent mathematical obstruction.',
    'univers|universe|curryfication')
add('R11316','The repeated presheaf tensor claim is not a retraction',113,[12],'unproved claim',
    r'\text{\uline{pl. fid}}',
    'The special case with M=Q-presheaves repeats full faithfulness even though one marginal occurrence is cancelled. The page does not clearly retract the main assertion, and agreement on representables plus generation does not alone prove full faithfulness on the uncompleted tensor product.',
    'hua_project/113.modern.tex, curryfication; relation: repetition of R11313 with a cancelled marginal label, not a settled correction.',
    'curryfication|représent|representable|génér')
add('R11317','The contraction formula marked for verification',113,[12],'self-flagged',
    'à vérifier',
    'The boxed formula (L⊗x)*L′≃(L*L′)⊗x is explicitly marked “à vérifier”, with a proposed reduction to representables. The proof needs the separate colimit preservation of both expressions in the two presheaf variables; the handwritten reduction is a method, not an omitted completed proof.',
    'hua_project/113.modern.tex, contraction formula; PURSUING_STACKS_CONTENTS.md §106; DOSSIER BISITE F.4/F.7 and RESIDUE I.3; relation: ordinary projection-pattern precursor.',
    'contraction|projection|coend|cofin|à vérifier')
add('R11318','The Hom–tensor adjunction chain',113,[12],'unproved claim',
    'Si $L=a',
    'The boxed Hom identifications are checked on a representable in the margin and then used for the projectivity corollary. Their extension to all L needs the same density and completeness assumptions as the earlier universal properties, which should remain visible in any modern proof.',
    'hua_project/113.modern.tex, adjunction and projectivity; PURSUING_STACKS_CONTENTS.md §§106–107; relation: foundational calculation, not a derived exchange isomorphism.',
    'Hom|tensor|adjunction|projectiv')
add('R11319','The projectivity corollary',113,[12],'unproved claim',
    r'\uline{Cor.}',
    'The corollary asserts that projective L and projective x give projective L⊗x. In an additive cocomplete M, epimorphisms are exactly maps with zero cokernel, so epimorphisms in the additive functor category are pointwise; projectivity of x then gives a pointwise surjection after applying Hom_M(x,−), and projectivity of L completes the lifting through the displayed Hom adjunction. This is an own elementary verification with high confidence from that lifting argument: no abelian hypothesis is needed for this particular corollary, although the subsequent Tor and derived discussion requires its separately stated exactness hypotheses.',
    'hua_project/113.modern.tex, projectives; scan013; relation: the ordinary projectivity claim is verified under the preceding additive cocomplete hypotheses, separately from the later derived claims.',
    'projectif|projectiv|abelian|abélienne')
add('R11320','Enough projectives and the stronger Tor question',113,[12,13],'conjecture',
    r'\uuline{Question}',
    'The final question asks both for enough projectives in the coefficient category and for their Tor-acyclicity. Scan013 gives separate sufficient conditions, so the continuation should be read as a conditional development rather than an unconditional answer to both parts.',
    'hua_project/113.modern.tex, last two pages; RESULTS_STATE TOTASPH D.7/F.27 and RESIDUE F.5/F.6; relation: coefficient-flatness method, not the total-asphericity implication.',
    'Tor|flat|plat|TOTASPH.*D.7|TOTASPH.*F.27')
add('R11321','Projective generators built from representables',113,[13],'unproved claim',
    'tout objet $F$ est quotient',
    'Part(a) constructs a projective epimorphism as a sum of a⊗x_a with x_a projective. This is a concrete route to enough projectives under the abelian and coproduct hypotheses, but it does not assert that those projectives are automatically k-flat.',
    'hua_project/113.modern.tex, last page; companion totality/flatness discussions; relation: separate sufficient construction.',
    'projectif|projectiv|somme|coproduct')
add('R11322','The flatness hypothesis for the balanced derived pairing',113,[13],'unproved claim',
    'transforme mono en mono',
    'Part(b) requires u↦u⊗x to be exact for every projective x, then claims the projective convolution functor is exact and either resolution computes the derived pairing. It is this additional hypothesis, not enough projectives alone, that bears on the later flatness questions.',
    'RESULTS_STATE TOTASPH F.27 and RESIDUE F.6; DOSSIER RESIDUE F.6; hua_project/113.modern.tex last page; relation: useful algebraic criterion, no dwyerienne-composition proof.',
    'TOTASPH.*F.27|RESIDUE.*F.6|flat|plat|exact')
add('R11323','Small sums of monomorphisms are explicitly required',113,[13],'reading question',
    'Une petite somme de mono est mono',
    'Condition(b) of the final list is readable and explicitly supplies the exactness of small sums of monomorphisms. Hua’s suggestion that this condition had to be supplied or was unreadable should therefore be revised at the commentary level, while the frozen text remains unchanged.',
    'hua_project/113.modern.tex, final hypotheses; relation: material reading difference supporting the proof conditions.',
    'somme|mono|AB4|exact')
add('R11324','Quasi-isomorphism invariance after resolving the first variable',113,[13],'unproved claim',
    'un quasi-isom',
    'The upper paragraph asserts quasi-isomorphism invariance in the second variable after resolving the first. The displayed complexes carry no explicit boundedness condition here, and the assertion is not accompanied by a totalization or convergence argument.',
    'hua_project/113.modern.tex, final page; ps_chapters_VI_VII/ps7.tex §§134–135; relation: missing scope for the derived construction, not a new theorem.',
    'quasi.iso|résolution|resolution|flat|multiplication')

add('R11401','Morphisms of asphericity structures',114,[2],'conjecture',
    'Morphisms of asph. structures? Inverse images?',
    'Agenda item1 asks for morphisms of asphericity structures, and the closing list postpones it. The later draft on scans005–006 explores the associated adjoint difficulties without supplying a finished definition.',
    'PURSUING_STACKS_CONTENTS.md §§84–86,88–90; DOSSIER BISITE E–F; relation: explicit postponed programme.',
    'asphericity structures|morphisms|inverse images|asphéricité')
add('R11402','Contractors and their morphisms',114,[2],'conjecture',
    'morphisms of such',
    'Item2 puts contractors and their morphisms in the proposed partIV work. The retained PS contents distinguish contractors from their morphisms, so the agenda is an organization of questions, not a proof that all relevant functors preserve contractibility.',
    'PURSUING_STACKS_CONTENTS.md §§95,97; [PS] §95 Proposition3; relation: programme treated in the matching named sections.',
    'contractor|contracteur|bimorphism')
add('R11403','Induced structures on slices',114,[2],'conjecture',
    'Induced structures',
    'Item3 asks for induced structures on M/a and assigns the topic to partIV, with VI marked in the margin. The page gives no stability hypothesis or slice theorem.',
    'PURSUING_STACKS_CONTENTS.md §§75–79; DOSSIER BISITE E.1; relation: slice precursor only.',
    'slice|localization|induced|localisation')
add('R11404','The lack of duality',114,[2],'conjecture',
    r'Lack of \deleted{auto}duality',
    'Item4 explicitly deletes “auto” while leaving the lack of duality as a topic to be revisited. Cote115’s ordinary dual adjunctions and PS VII’s six-operation perplexities are related responses, but neither turns this line into a derived self-duality theorem.',
    'ps_chapters_VI_VII/ps7.tex §136; DOSSIER BISITE G and RESIDUE I; relation: motivating mismatch.',
    'duality|dualité|auto|six operations')
add('R11405','Canonical modelizers from an equivalence structure',114,[2],'conjecture',
    'give rise to a can. modelizer?',
    'Item5 asks when an equivalence structure produces a canonical modelizer, with one intervening word doubtful. No existence criterion is stated on the agenda.',
    'PURSUING_STACKS_CONTENTS.md §§50,56,78,80,88; relation: repeated programme question.',
    'canonical modelizer|canoni|equivalence structure')
add('R11406','Existence of test functors',114,[2],'conjecture',
    'Existence theorems for test functors',
    'Item6 requests existence theorems and attaches V? and VII in the margin. It does not claim every asphericity structure has such a functor.',
    'PURSUING_STACKS_CONTENTS.md §§46–47,78–79,90; relation: explicitly deferred existence problem.',
    'test functor|foncteur.test|existence')
add('R11407','Finiteness conditions',114,[2],'conjecture',
    'Finiteness conditions in an elementary modelizer?',
    'Item7 asks for finiteness conditions and the closing note says it may not be treated at all. The general question is too broad to identify it with one of the later finite-category, finite-space, or finite-height classification results.',
    'PURSUING_STACKS_CONTENTS.md §91; DOSSIER PATHS E and RESIDUE B; relation: thematic precursor, not a matching classification.',
    'finite|finiteness|finitude|PATHS.*E.')
add('R11408','Boundary operators and cohomology',114,[2],'conjecture',
    'Computation of cohomology by boundary operator?',
    'Item8 asks whether boundary operators compute cohomology and is also among the topics that may be omitted. Cotes112–113 provide coefficient machinery, while PS §§93,99–103 are the directly matching later topics.',
    'PURSUING_STACKS_CONTENTS.md §§91,93,99–103; ps_chapters_VI_VII/ps7.tex §§134–135; relation: abelianization programme.',
    'boundary|operator|bord|abelianizator|integrator')
add('R11409','The infinite simplex and submodelizers',114,[2,3],'conjecture',
    'submodelizers of (Cat)',
    'Item9 groups Δ with a superscript f, an infinite simplex, finite subsimplices, and submodelizers of Cat; scan003 adds further candidate shapes. The programme allocations IV/V/VI/VII are section plans, not evidence of a numbered manuscript page count or a proven test property.',
    'PURSUING_STACKS_CONTENTS.md §§42–43,91,98; relation: matches the weak-test-category programme, not later totality/filteredness.',
    'Simplexf|submodelizer|infinite simplex|Delta')
add('R11410','The finite-subset candidate',114,[3],'conjecture',
    'weak test category?',
    'The P_f(I) question is explicit, but its P alphabet and the convention on empty subsets remain unspecified on the leaf. A close contextual match is PS §43, manuscript page78, which takes the finite nonempty subsets of an infinite set and asks exactly whether this ordered category J is weak test. That passage rules out local test by its one-object singleton slices, but leaves the weak-test question there open; filteredness alone is not its answer. The matching object and question support a probable identification, with medium confidence because the leaf itself omits these conventions.',
    'hua_project/114.modern.tex p2; PURSUING_STACKS_CONTENTS.md §§22,34,43; primary [PS] §43, ms78, PDF index120; relation: close textual candidate, with the omitted conventions kept explicit.',
    'P_f|finite subset|parties finies|weak test')
add('R11411','Ordered sets and the page74 reference',114,[3],'conjecture',
    'Cf p 74',
    'The margin asks about an asphericity or contractibility structure on Ord and points to page74 without naming the source. PS §42, original manuscript page74, gives a submodelizer criterion for Cat and immediately asks how to apply it to Ord through an ordered test category, making it a strong candidate for the reference. Confidence in this identification is medium, based on the matching page number and adjacent subject matter; it is a research connection, not an expansion of the frozen marginal text.',
    'PURSUING_STACKS_CONTENTS.md §§22,42; primary [PS] §42, ms74–75, PDF indices116–117; ps_chapters_VI_VII/ps7.tex §137; relation: probable source identification, not a certain attribution.',
    'Ord|ordered sets|ordonn|p.74|page.74')
add('R11412','Total zero-connectedness implies total asphericity?',114,[3,4],'conjecture',
    'total 0-connectedness',
    'Scan003 asks the implication explicitly; scan004’s Proposition4 claims the stronger equivalence for a localizer satisfying Loc4. The proof runs off the supplied page, and the statement concerns products of representables rather than the later total-final-image condition.',
    '108 scan004 item13; RESULTS_STATE Hua 114-total-asphericity-independent-of-localizer, TOTASPH D.7, RESIDUE F.5; companion/chunks/DER_XIIb-a.tex ms88–89; relation: precise but different notion.',
    'total.*connect|totale|Loc 4|TOTASPH.*D.7')
add('R11413','The exact Loc4 hypothesis',114,[4],'reading question',
    'localizer satisfying Loc 4)',
    'The printed proposition explicitly includes Loc4, and the last line calls W₀ the coarsest localizer satisfying it. In PS §81 this axiom means W-equivalences induce bijections on π₀, so the all-functors localizer used in one of Hua’s objections fails the stated hypothesis.',
    '[PS] §81, ms260–261; hua_project/114.modern.tex, first objection and later correction; relation: corrects the hypothesis of that objection, not every objection.',
    'Loc 4|W_0|all functors|tous les foncteurs')
add('R11414','The ordinary cube obstruction survives Loc4',114,[4],'own idea',
    'The following conditions are equivalent:',
    'Verification of Hua’s separate cubical lead: in the ordinary cube category with faces and degeneracies, every element of a product of representables connects to a vertex pair, and edge paths connect all vertex pairs, so condition(iii) holds. Cisinski Remark8.4.33 records that the product of two representable one-cubes is not even simply connected, contradicting condition(i), while W=W₀ does satisfy the PS Loc4 condition. Confidence: high under that explicit cube convention; this checks the literal draft proposition and does not concern later TOTASPH totality.',
    'hua_project/114.modern.tex, cubical objection; primary [Cisinski] Remark8.4.33 and [PS] §81; relation: checks a previously supplied counterexample lead.',
    'cub|Loc 4|0-connected|114-total')
add('R11415','A draft differs from the retained PS Proposition4',114,[4],'own idea',
    'So I\'ll have to clarify the points a) and b)',
    'The retained PS §95 Proposition4 at manuscript page350 is a different statement about a contractibility structure and i:A→M, with strict total asphericity and sections, while the supplied page continues into the arbitrary-A totality proposition. The opening of PS §96 describes putting failed pages aside as scratch paper, which supports treating this as a draft witness rather than filling its missing proof from the retained Proposition4. Confidence: medium for that historical identification, high for the textual difference; no exact date of this physical sheet is inferred.',
    'Primary [PS] §§95–96, ms349–351; hua_project/114.modern.tex; relation: distinct textual witness, not a same-package retraction.',
    'Proposition 4|scratch|contractor|clarify')
add('R11416','Asphericity does not imply ordinary faithful restriction',114,[5],'unproved claim',
    'conservatif et fidèle',
    'The NB asserts that an aspherical f gives a conservative faithful restriction functor. Hua’s two-object-chain example correctly obstructs this literal ordinary-category reading: selecting the initial object is aspherical but evaluation there loses the other presheaf component.',
    'hua_project/114.modern.tex, “Le NB, et pourquoi il ne tient pas”; RESULTS_STATE REVLOC F.1 is a different localizer issue; relation: checked elementary obstruction to this claim.',
    'dominant|conservatif|fidèle|REVLOC.*F.1')
add('R11417','Dominance detects the empty presheaf',114,[5],'unproved claim',
    r'$A_{/b}\ne\varnothing$ OK',
    'The margin’s condition is dominance, and the attempted argument concerns reflection of the initial presheaf. That property is weaker than ordinary faithfulness/conservativity; the neighbouring cancellations do not provide a proof of the stronger NB.',
    'hua_project/114.modern.tex, “Ce que la dominance caractérise exactement”; relation: same weaker criterion, not a six-operation base-change result.',
    'dominance|dominant|initial|empty|vide')
add('R11418','The missing localizer hypothesis is explicitly flagged',114,[5],'self-flagged',
    'hypothèse sur',
    'The margin says a small hypothesis on W is needed, but does not name it. It should be recorded as an unresolved qualification, not automatically identified with Loc4 merely because that axiom appears on the preceding reused sheet.',
    'RESULTS_STATE REVLOC F.1; hua_project/114.modern.tex p4; relation: explicit missing hypothesis, with no supplied identification.',
    'hypothèse|localizer|Loc 4|REVLOC.*F.1')
add('R11419','Generation by aspherical objects',114,[5,6],'unproved claim',
    r'est \uline{générateur}',
    'The argument replaces the initial expectation with a generating hypothesis on M_as and then assumes it on scan006. Faithfulness is a separating-family condition, whereas detecting isomorphisms needs the corresponding stronger property; the manuscript’s intended sense of “engendre” should be specified before claiming either.',
    'hua_project/114.modern.tex, “Le bon critère”; PURSUING_STACKS_CONTENTS.md §90; relation: stated repair with a terminology distinction.',
    'générat|generat|separat|conserv')
add('R11420','The empty aspherical part',114,[5],'conjecture',
    r'Peut-on avoir $M_{\mathrm{as}}=\varnothing$',
    'The empty case is tested and marked OK using A=∅ and its one-object presheaf category. This is an exploratory example in the chosen asphericity setup, not a contradiction from the existence of an initial or final object alone.',
    'hua_project/114.modern.tex, “La partie asphérique peut être vide”; relation: same proposed degenerate example.',
    'asphérique peut être vide|varnothing|empty|asph')
add('R11421','The singleton part and the discrete-category warning',114,[5,6],'reading question',
    'supposons $G=',
    'Scan006 assumes End(a) is trivial, while Hua’s footnote turns this into a necessity and then argues with a group despite End(a) being a monoid in general. Moreover, a functor from a discrete category is always faithful and reflects isomorphisms of its source arrows, so Hua’s explicit claim that the displayed discrete M makes i* non-faithful cannot be the conclusion of that example.',
    'hua_project/114.modern.tex, singleton counterexample; relation: two interpretive errors, with the manuscript’s exact target of “Contr’exemple” still to determine.',
    'End|monoïde|discrète|discrete|nécessairement')
add('R11422','The adjoint-existence argument is cancelled and unverified',114,[6],'self-flagged',
    'à vérifier des conditions',
    'The cancelled lower draft asks which representability/admissibility conditions ensure a left adjoint to a limit-preserving f*. It is explicitly unfinished, and the word is “admissibilité” in the frozen reading, not the modernizing replacement “accessibilité”.',
    'hua_project/114.modern.tex, final section; PURSUING_STACKS_CONTENTS.md §§84–85; relation: explicit unverified adjoint hypotheses and reading difference.',
    'admissib|accessib|representab|représentab|adjoint')
add('R11423','Does the left adjoint preserve aspherical objects?',114,[6],'withdrawn in the same text',
    'Mais va-t-on supposer',
    'The same cancelled draft asks whether f_! should carry M_as to M′_as, then specializes to an aspherical functor and begins the case B punctual. The question is recorded again in the PS §84 title, but this sheet stops before completing the example or giving a general answer.',
    'PURSUING_STACKS_CONTENTS.md §§84–85; hua_project/114.modern.tex final section; DOSSIER BISITE E–F; relation: cancelled precursor to a named later perplexity.',
    'f_!|perplexity|aspheric|asphérique')

add('R10829','The converse connectedness question',108,[4],'conjecture',
    'and conversely',
    'The inserted converse is a distinct question in item13. The terminology and deletion at the start of the sentence prevent treating it as a formal tautology without identifying the intended connectedness structures.',
    '114 scans003–004; companion/chunks/DER_XIIb-a.tex ms88–89; RESULTS_STATE TOTASPH D.7; relation: earlier, differently defined question.',
    'connected|connex|totale|TOTASPH.*D.7')
add('R10830','Products of connected objects',108,[4],'conjecture',
    'Is it enough that product of two',
    'Item13 separately asks whether closure of 0-connected objects under binary products suffices. The insertions “0-” and the preceding converse should remain visible when relating this to the product-of-representables condition of 114/004.',
    '114 scan004 Proposition4(iii); hua_project/108.modern.tex p3 and 114.modern.tex; relation: related product criterion, not identical quantified objects.',
    'product|produit|0-connected|total')
add('R10831','Products of W-aspherical objects',108,[4],'conjecture',
    r'$\underline W$-aspheric objects',
    'The parenthetical version replaces connected objects by W-aspherical objects and explicitly inserts the numeral2. It is another sufficiency question, not an asserted equivalence for all localizers.',
    '114 scan004; PURSUING_STACKS_CONTENTS.md §§60,65; RESULTS_STATE TOTASPH D.7/RESIDUE F.5 use a different later totality; relation: related but distinct question.',
    'W-asph|W.*asph|produit|product')
add('R11215','The truncation question retracts an extra hypothesis',112,[3],'withdrawn in the same text',
    r'\deleted{et $H_i',
    'Question3 crosses out the preliminary homology-vanishing condition before inserting a new request for L′ and L→L′. This is a change of the problem on the same sheet, not a proof that the earlier hypothesis is unnecessary in a solution.',
    'hua_project/112.modern.tex, third question; ps_chapters_VI_VII/ps6.tex, Postnikov discussions; relation: retained drafting history.',
    'tronqu|Postnikov|H_i|112-linearization')
add('R11325','The unfinished multiplication with flat generators',113,[13],'conjecture',
    'une multiplication',
    'A sentence begins with a multiplication on Q-presheaves for which the objects of Q are flat and then stops. No monoidal axiom, derived product, or compatibility conclusion is supplied after that hypothesis.',
    'hua_project/113.modern.tex, last page; PURSUING_STACKS_CONTENTS.md §109; relation: unfinished extension of the tensor programme.',
    'multiplication|flat|plat|coalgebra')
add('R11326','A scope check for unbounded derived tensor products',113,[13],'own idea',
    'résolutions proj.',
    'A modern treatment should first settle boundedness and totalization, then use K-flat or K-projective replacements if unbounded complexes are intended. Confidence: medium as a proposed proof requirement, because the sheet does not specify its complex conventions and may have intended a bounded situation; no failure of its bounded calculation is being claimed.',
    'hua_project/113.modern.tex, final page; ps_chapters_VI_VII/ps7.tex §§134–135; primary [Spaltenstein] §5 and [Stacks] tag06Y7; relation: additional scope question, not a new theorem.',
    'complex|bounded|born|résolution|resolution')
add('R11424','Inverse images of asphericity structures',114,[2],'conjecture',
    'Inverse images?',
    'The second question in agenda item1 asks independently for inverse images. It anticipates a variance problem but supplies no formula or closure argument for the pulled-back structure.',
    'PURSUING_STACKS_CONTENTS.md §§84–86; DOSSIER BISITE E.1 and F.1; relation: programme only.',
    'inverse image|image inverse|asphericity')
add('R11425','The clarification promised before the draft Proposition4',114,[4],'self-flagged',
    "So I'll have to clarify the points a) and b)",
    'The author explicitly says points(a) and(b) of the preceding remark require clarification, then starts a new totality argument. The referenced remark is not wholly present in the supplied sheet, so the missing clarification cannot be reconstructed from the later retained version without marking a textual difference.',
    '[PS] §§95–96, ms349–351; hua_project/114.modern.tex p3; relation: explicit unfinished step and a different retained text.',
    'clarif|remark 2|Proposition 4|contractor')

def write():
    rows.sort(key=lambda r:(r['cote'],min(r['scans']),r['id']))
    for r in rows:
        p=subprocess.run(['rg','-n','-i','-m','4','--glob','*.md','--glob','*.tex',r['query'],str(ROOT/'context')],text=True,capture_output=True)
        r['context_search_hits']=p.stdout.splitlines()[:24]
        r['context_search_exit']=p.returncode
    (OUT/'research_root.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    chunks=['## Page-specific research notes: cotes 108, 112, 113 and 114\n']
    for r in rows:
        loc=f"{r['cote']} scan"+('s ' if len(r['scans'])>1 else ' ')+', '.join(f'{s:03}' for s in r['scans'])
        chunks += [f"### {r['id']} — {r['title']}\n",f"**Location:** {loc}. **Kind:** {r['kind']}.\n",f"**Manuscript cue:** `{r['quote']}`\n",r['note']+'\n',f"**Context/status:** {r['context']}\n"]
    (OUT/'research_root.md').write_text('\n'.join(chunks))
    print(f'Wrote {len(rows)} root notes with individual context searches.')
if __name__=='__main__': write()
