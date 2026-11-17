#!/usr/bin/env python3
"""Build a research-only comparison; never write frozen transcription files."""
from pathlib import Path
import json
import re
import subprocess

ROOT=Path('/workspace/scratch/cb96d9ba0f27')
CONTEXT=ROOT/'context'
OUT=ROOT/'deliverable/work_records'
PREFIX='MPL_108+112+113+114+115'

supplied={}
for number,line in enumerate((CONTEXT/'DOSSIER_STATEMENTS_WITH_STATUS.md').read_text().splitlines(),1):
    if line.startswith('| RESIDUE '):
        fields=line.strip('|').split(' | ')
        fields=[v.strip() for v in fields]
        assert len(fields)==4,(number,len(fields))
        supplied[fields[0]]={'id':fields[0], 'supplied_statement':fields[1],
                             'supplied_status':fields[2], 'supplied_source_locator':fields[3],
                             'dossier_line':number, 'review_status':'No separate review of this row is supplied.'}

entries={}
def add(short,relation,note,states,context_locator,terms,quotes=()):
    key='RESIDUE '+short
    assert key in supplied and key not in entries
    entries[key]={**supplied[key], 'relation':relation, 'note':note,
                  'results_state_links':states, 'context_locator':context_locator,
                  'search_terms':terms,
                  'manuscript_evidence':[{'cote':c,'scan':n,'quote':q} for c,n,q in quotes]}

XVI='companion/chunks/DER_XVI.tex, §§1–3 (especially ms.1–27); supplied RESIDUE row.'
FIB='companion/chunks/DER_XIIc-b.tex, ms.240–241, with DER_XIIc-a.tex, ms.215–218; supplied RESIDUE row.'
COEF='companion/chunks/DER_I-b.tex, ms.99–100; DER_XVI.tex, §4; supplied RESIDUE row.'
TOTAL='companion/chunks/DER_XIIb-a.tex, ms.88–89, Definition 1 and the preceding terminology warning; supplied RESIDUE row.'
KAN='DOSSIER_STATEMENTS_WITH_STATUS.md, BISITE F.10–F.12, F.19 and the exact RESIDUE I row.'
HIGH='DOSSIER_STATEMENTS_WITH_STATUS.md, BISITE C.10, F.18 and the exact RESIDUE J row.'

add('B.1','absent','No component-dependent class W-dagger or separation of absolute from relative Theorem A is stated in this package; the supplied counterexample has no manuscript counterpart here.', ['GALOIS B.3','REVLOC F.1'],XVI,r'component-dependent|relative Theorem A|Loc.*3 bis')
add('B.2','absent','The quotient of the homotopy category by maps factoring through the circle, and its classification of invertible images, do not occur on these pages.', ['GALOIS B.3'],XVI,r'factoring through|homotopy retract|quotient.*homotopy')
add('B.3','absent','No circle-degree localizer or counterexample showing that saturation fails to imply relative Theorem A appears here; this remains a later research-return claim in the supplied context.', ['GALOIS B.3','REVLOC F.1'],XVI,r'W_.*circ|strong saturation|absolute axiom')
add('B.4','absent','The ten-object/six-object finite certificate and its degree-two homology detection are absent; no scan is assigned to that later construction.', ['GALOIS B.3','REVLOC F.1'],XVI,r'ten-object|six-object|multiplication by.*2')
add('B.5','precursor','108/005 asks whether the presheaf/category comparison induces equivalences after localization by homotopisms; it does not prove homotopy invariance for all literal localizers, the adjunction assertion, or the initial-object consequence of this row.', ['GALOIS B.1','GALOIS B.3'],XVI,r'homotopisme|Rappel 1.2|initial object',[(108,5,r'localisés par les \uline{homotopismes}')])
add('B.6','absent','Invariance of the localizer under opposition, W = W-op, is not asserted here. The package’s separate questions about duality of asphericity structures cannot be substituted for that statement.', ['GALOIS B.1'],XVI,r'W=W|Rappel 1|opposition|automorphisme')
add('B.7','absent','Neither of XVI Proposition 1.3’s two abstract equivalences, with the distinction between absolute and relative Theorem A, is formulated in this package.', ['GALOIS B.1','GALOIS B.3'],XVI,r'Proposition.*1.3|weak equivalence|strong equivalence')
add('B.8','precursor','108/003 explicitly asks about exactness of the canonical localization functors, and 108/005 asks about the comparison i_A(X×Y) to i_A(X)×i_A(Y); neither passage asserts the later product-closure theorem or gives the counterexample under the literal axioms.', ['GALOIS B.3'],XVI,r'Rappel.*2.3|Proposition.*2.4|finite products',[(108,3,r'Exactness properties of $(Hot_{\underline W})$'),(108,5,r'i_A(X\times Y)\unsure{\mathbin{-}|\longrightarrow}i_A(X)\times i_A(Y)')])
add('B.9','absent','The comparison with Cisinski’s and Maltsiniotis’s later definitions and their saturation terminology has no form in these manuscript pages.', ['GALOIS B.1','GALOIS B.3'],XVI,r'6.1.12|1.1.2|weak fundamental localizer')
add('B.10','precursor','The exactness and base-change questions in 108/003–004 supply an earlier problem list, but no statement-by-statement audit of XVI or XV §9 and no conclusion about their Mayer–Vietoris implications appears here.', ['RESIDUE I.7','GALOIS B.3'],XVI,r'Mayer|historical audit|Loc.*4',[(108,3,r'Exactness properties of $(Hot_{\underline W})$'),(108,4,r'chgt. de base transforme équiv. faibles en équiv. faibles')])
add('B.11','absent','There is no distinction here between full decomposition and its forward part, and no counterexample to the parenthesis in XVI Corollary 2.2. The occurrence of “Loc 4)” in 114/004 belongs to the historical hypotheses of its different Proposition 4, not to a proof of this correction.', ['GALOIS B.3'],XVI,r'Corollary.*2.2|Corollaire.*2.2|decomposition|Loc.*4 a')
add('B.12','precursor','108/003 asks about exactness of localization, but does not state these decomposition equivalences or prove preservation of finite products and coproducts under the specified hypotheses.', ['GALOIS B.3'],XVI,r'Lemma.*2.5|Lemme.*2.5|Proposition.*9.4|finite localization',[(108,3,r'Exactness properties of $(Hot_{\underline W})$')])
add('B.13','absent','The two adjunctions of π₀ with the discrete-set functor on Hot_W, and their consequences for arbitrary small sets, are not given here; the ordinary adjunctions in cote 115 involve different categories and functors.', ['GALOIS B.1'],XVI,r'discrete.set|discrets|pi_0|2.14')
add('B.14','absent','No version of XVI Proposition 3.1’s elementary cube implications is stated. The phrase “Cubical games” elsewhere in the package is a question heading, not this axiom calculation.', ['GALOIS B.3'],XVI,r'Proposition.*3.1|cube implications|Mayer')
add('B.15','precursor','108/003’s question about exactness leaves room for the later issue, but supplies neither an arbitrary-arrow-class counterexample nor the repair requiring identities.', ['GALOIS B.3'],XVI,r'arbitrary.arrow|identities|Lemme.*2.5',[(108,3,r'Exactness properties of $(Hot_{\underline W})$')])
add('B.16','absent','Near bijections of infinite component sets and the resulting weak localizer W_nb are absent from the frozen package.', ['GALOIS B.3','REVLOC F.1'],XVI,r'near bijection|near.bijective|W_.*nb')
add('B.17','absent','The failures of the listed nontriviality equivalences, and their repair by relative Theorem A, are not stated or exemplified on these pages.', ['GALOIS B.3','REVLOC F.1'],XVI,r'nontriviality|Proposition.*2.7|9.13')

add('C.1','precursor','108/004 describes fibrations through preservation of weak equivalences by base change and separately asks to add the displayed pullback condition to Quillen’s axioms. It gives no factorization hypothesis or proof of W∩Fib_W = W^u or of invariance between intrinsic fibrations.', ['GALOIS B.14'],FIB,r'intrinsic fibration|universellement|weak after arbitrary',[(108,4,r'chgt. de base transforme équiv. faibles en équiv. faibles'),(108,4,r'$f$ fib, $g\in\underline W\implies g\prime\in\underline W')])
# The second displayed quote above is normalized below to the exact frozen token.
entries['RESIDUE C.1']['manuscript_evidence'][1]['quote']=r"$f$ fib, $g\in\underline W\implies g'\in\underline W$ dans axiomatique de Quillen."
add('C.2','absent','Equivalence of all intermediate intrinsic-fibrant subcategories after ordinary and infinity localization, under factorization alone, is not established here.', ['GALOIS B.14'],FIB,r'intermediate|factorisation gauche|factorization alone')
add('C.3','absent','The five-object, sixteen-arrow counterexample separating the fibre axioms and intrinsic factorization is absent.', ['GALOIS B.14'],FIB,r'five objects|sixteen arrows|five-object|B062')
add('C.4','absent','There is no exhaustive-search bound for finite categories with pullbacks, nor the warning that bounding objects leaves arrows unbounded.', ['GALOIS B.14'],FIB,r'object bound|arrow bound|finite categor.*pullback')
add('C.5','absent','No strictly functorial perfect-path replacement R_S with weak coaugmentation is constructed here.', ['BISITE B.21','RESIDUE A.8'],FIB,r'perfect path|perfect.*replacement|coaugmented')
add('C.6','absent','The localization theorem for all intermediate subcategories between perfect objects and Cat/S is absent; questions about contractor/presheaf comparisons do not supply its relative assertion.', ['BISITE B.21','RESIDUE A.8'],FIB,r'intermediate perfect|Parf|F_0,S')
add('C.7','precursor','108/004 places change of base and the local tests for fibrations on the agenda, but no intrinsic-factorization theorem, derived reindexing construction, or the two relative homotopy-fibre identities of XII ms.241 are written here.', ['GALOIS B.14'],FIB,r'240|241|derived reindexing|homotopy.fibre',[(108,4,r'Caractérisation des \deleted{\unsure{équiv}}\unsure{SQ|W}-fibrations dans $Cat$')])
add('C.8','absent','The minimum-size counterexample problem for axioms (a),(b),(c) in a category with pullbacks does not occur in this package.', ['GALOIS B.14'],FIB,r'minimum problem|five objects|unbounded.arrow')

add('D.1','precursor','108/004 states that testing preservation of weak equivalences on inclusions of terminal objects suffices and asks whether all Δ₀→Δₙ tests suffice. This is a recognizable local-test precursor, without the truncation τ≤n, the homotopy-pullback equivalence, or the smooth/proper reductions of the later row.', ['GALOIS B.14','GALOIS B.7'],COEF,r'terminal object|objet final|intrinsic|tau_',[(108,4,r'il suffit que ce soit OK pour les inclusions $e_Y\longrightarrow Y$, $e_Y$ objet final de $Y$.'),(108,4,r'Est-il suffisant que l\prime on le suppose')])
entries['RESIDUE D.1']['manuscript_evidence'][1]['quote']=r'Est-il suffisant que l’on le suppose' # removed if typography differs; first quote suffices
entries['RESIDUE D.1']['manuscript_evidence']=entries['RESIDUE D.1']['manuscript_evidence'][:1]
add('D.2','absent','No classification of truncated intrinsic fibrations by connecting homomorphisms, including the degree-zero monodromy clause, is given here.', ['GALOIS B.7','GALOIS B.14'],COEF,r'connecting homomorphism|monodromy action|boundary.*pi')
add('D.3','absent','The two explicit component-and-arrow-lifting conditions characterizing Fib_W0 do not appear; the package’s general fibration questions do not specify them.', ['GALOIS B.7','GALOIS B.14'],COEF,r'prescribed component|lift.*component|Fib_.*W_0')
add('D.4','absent','No counterexample to describing intrinsic fibrations by a right lifting property is present.', ['GALOIS B.7','GALOIS B.14'],COEF,r'right lifting|lifting property|relèvement')
add('D.5','precursor','112/003 explicitly introduces a locally constant derived target and a “syst. de coeff tordus”, then asks for a localization equivalence. It does not identify the associated class of functors by π₀, π₁ and homology of universal covers, or prove the integral, rational, set or groupoid cases in this row.', ['GALOIS G.6','GALOIS E.11','RESIDUE I.7'],COEF,r'locally constant|universal covers|coefficients|coeff',[(112,3,r'\uline{syst. de coeff tordus}'),(112,3,r'\uline{est-ce une équivalence de catégories}')])
add('D.6','absent','The rational local-coefficient criterion involving only the degree-two boundary, and the rejection of stronger higher-boundary tests, are absent.', ['GALOIS B.14','GALOIS G.6'],COEF,r'rational local coefficients|degree.two boundary|higher rational')
add('D.7','absent','These pages supply no general intrinsic-fibre criterion for rational or mod-p locally constant coefficients and do not close this recorded gap.', ['GALOIS B.14','GALOIS G.6'],COEF,r'remaining coefficient|mod-.p|rational|coefficient')
add('D.8','absent','The mod-p intrinsic covering with finite p-group monodromy, including EC_p→BC_p, has no counterpart here.', ['RESIDUE D.9','GALOIS B.7'],COEF,r'mod-.p|finite.*p.group|monodromy|EC_p')
add('D.9','absent','No classification of intrinsic homology coverings for arbitrary spectra is stated or proved; the ordinary and additive coefficient calculations here do not settle the registered open problem.', ['RESIDUE D.9'],COEF,r'arbitrary nonzero spectra|homology classification|monodromy')
add('D.10','absent','The named finite examples and the forty-eight-entry smooth/proper/intrinsic table of BISITE B.15 are not reproduced or computed here.', ['GALOIS B.7','RESIDUE D.9'],COEF,r'BISITE B.15|all 48|Intrinsic|Proper, both')
add('D.11','precursor','Question 12 on 108/004 explicitly proposes stability of weak equivalences under pullback along a fibration in Quillen’s axioms. It supplies no classification of axioms (7a),(7b),(7c),(7F) across the six coefficient localizers in the later table.', ['GALOIS B.7','GALOIS B.14'],COEF,r'fibration.axiom|7a|7b|7c|7F',[(108,4,r"$f$ fib, $g\in\underline W\implies g'\in\underline W$ dans axiomatique de Quillen.")])
add('D.12','absent','There is no theorem identifying integral/rational intrinsic categorical coverings with trivial-monodromy products; the mod-p contrast is absent as well.', ['RESIDUE D.9','GALOIS B.7'],COEF,r'trivial monodromy|integral and rational|discrete.*opfibration')

add('F.1','different','114/004’s Proposition 4 tests products of representables and refers to section 65 A, definition 1, p.170; RESIDUE F.1 explicitly uses totality under every ordinary final image in XII ms.88–89. The covariant-action criterion and its comparison of integral acyclicity with weak contractibility are not supplied by this differently quantified manuscript proposition.', ['TOTASPH D.7','RESIDUE F.5','POLES H.2'],TOTAL,r'ordinary final images|total asphericity|earlier test.category|quantifier',[(114,4,r'the product $a\mathbin{\mathrm{x}}b$'),(114,4,r'in $\widehat A$ is 0-connected.')])
add('F.2','absent','No augmentation-one integral combination equalizing an original parallel pair is constructed here. The product-of-representables condition in the earlier totality discussion must not be silently replaced by this affine equalization assertion.', ['TOTASPH D.7','RESIDUE F.5'],TOTAL,r'augmentation one|original parallel|affine|common successors')
add('F.3','absent','The classifications for unbounded injective ordinals, finite sets and injections, injective self-maps of N, and free categories are absent. The undeciphered variants of Δ and cubical categories in the problem lists do not identify the specific A_S examples in the supplied return.', ['RESIDUE F.3','PRETOT A.12','TOTASPH C.10'],TOTAL,r'Delta_.*inj|unbounded|injective|free category')
add('F.4','absent','No final-image-totality theorem with a weakly terminal object, finite-object consequence, or universal Cat-colimit implication is stated in these pages.', ['RESIDUE F.7','TOTASPH D.7'],TOTAL,r'weakly terminal|finitely many objects|filtered')
add('F.5','different','The tempting apparent answer from 114/004 concerns product/diagonal totality, not the final-image totality quantified in RESIDUE F.5. Nothing in the frozen package addresses arbitrary parallel arrows of Aff_Z(A), so it neither proves nor refutes the recorded converse from totality to exact abelian colimits.', ['RESIDUE F.5','TOTASPH D.7','TOTEX D.20'],TOTAL,r'Aff_.*mathbb Z|exact connected converse|parallel pair|final image',[(114,4,r'(ii) $A$ is totally $\underline W$-asphericx (cf. section 65 A), def.1 p.170)).')])
add('F.6','different','The independence-of-localizer claim in 114/004 concerns categories tested through products of representables. It does not compare totally W_Z- and W_infinity-aspherical presheaves under all outgoing Kan extensions, and contains no composition theorem for Dwyer sieves; the registered open item remains untouched.', ['RESIDUE F.6','TOTASPH F.27'],TOTAL,r'total.*presheav|dwy|composition|restricted.action',[(114,4,r'Let $A$ be any small category, $\underline W$ a basic'),(114,4,r'localizer satisfying Loc 4)')])
add('F.7','absent','The universal ordinary-Cat-colimit comparison for a countable shape, its implication toward filteredness, and the B(N^(n+1)) obstruction are absent; the additive colimit universal properties of cote 113 concern a different target category.', ['RESIDUE F.7','PATHS A.8'],TOTAL,r'Universal Cat.colimit|countable category|categorical colimit|Grothendieck construction')

add('I.1','absent','No diagonal-stable classification of W_infinity-smooth maps as discrete fibrations occurs. General kernel correspondences do not impose or prove that lifting criterion.', ['BISITE F.18'],KAN,r'diagonal.stable|strict diagonal|discrete fibration')
add('I.2','absent','The assertion that universally ambidextrous discrete fibrations with unpointed-space coefficients are exactly isomorphisms is absent. The dual adjunction of presheaf and copresheaf transforms is not an equality of left and right Kan extensions along one map.', ['RESIDUE I.7','GALOIS G.6'],KAN,r'ambidextr|unpointed spaces|left and right Kan')
add('I.3','precursor','115/004 gives an ordinary set-valued kernel, its two contravariant transforms and their Hom adjunction; 115/006 organizes equivalent presentations, and 115/010 gives contraction/left-Kan exchange identities. These are relevant one-categorical ingredients, but the pages do not construct a lax symmetric monoidal infinity-correspondence functor, specify smooth right legs, or verify coherent composition of b_!a^*.', ['STRATA B.2','BISITE F.18','RESIDUE I.7'],KAN,r'correspondence|coherence|symmetric monoidal|kernel|b_!a',[(115,6,r'Toutes les flèches du diagramme sont des équivalences de catégories'),(115,10,r'\langle\Phi_*,f^{\circ *}(\Psi^*)\rangle_A&\simeq\langle f_!(\Phi_*),\Psi^*\rangle_B')])
add('I.4','absent','The suitable-decomposition cancellation counterexample and the replacement by a span universal property are absent. Uniqueness of the ordinary adjoints in cote 115 does not by itself certify the infinity-categorical extension demanded by I.3.', ['RESIDUE I.7','BISITE F.18'],KAN,r'suitable.decomposition|cancellation|unfurling|A.5.10')
add('I.5','precursor','115/008 explicitly exchanges the two duality transforms upon replacing A by its opposite, and 115/015 exchanges coefficient-valued sheaves and cosheaves. This is ordinary variance duality, not a proper-leg correspondence theorem or a statement f^! = f^*: on 115/004, a superscript ! on Hom is expressly the limit-preserving condition.', ['STRATA 0.1','BISITE D.13','RESIDUE I.7'],KAN,r'opposition|proper right legs|trivial twist|cohomologically etale',[(115,8,r'\varphi_{A^\circ}&=\psi_A'),(115,15,r'\mathcal F(\mathcal X,M)^\circ\simeq\mathcal F^\vee(\mathcal X,M^\circ)'),(115,4,r'formée des foncteurs commutant aux $\varprojlim$.')])
add('I.6','absent','The pointed-space ambidexterity classification by unions of connected components is absent; questions about pointed homotopy types do not provide the coefficient-sensitive Kan comparison.', ['RESIDUE I.7','GALOIS G.6'],KAN,r'pointed.space|unions of connected components|ambidextr')
add('I.7','precursor','112/003 asks whether localization of smooth abelian presheaves gives a locally constant derived category, with explicit twisted coefficients, while 113/013 develops a conditional derived tensor calculation. Neither page classifies reversible accessible localizers between integral homology and W_0, constructs D↦D′ on every bare derivator, or gives the proposed obstruction by agreement on finite posets.', ['RESIDUE I.7','GALOIS G.6','GALOIS E.11'],r'companion/chunks/DER_VIII-X.tex, chapter X ms.1–5; dossier RESIDUE I.7 and I.9.',r'reversible|accessible|higher.coefficient|bare.derivator|locally constant',[(112,3,r'\uline{est-ce une équivalence de catégories}'),(112,3,r'\uline{syst. de coeff tordus}'),(113,13,r'peut se calculer indifféremment par résolutions projectives')])
add('I.8','absent','There is no finite-discrete-bifibration classification for spectra or D(k), and no equality of exceptional and ordinary inverse images or assertion of a trivial dualizing twist. The additive dualities and projective resolutions in cote 113 do not constitute this map classification.', ['RESIDUE I.7','GALOIS G.6'],KAN,r'finite discrete bifibration|spectra|dualizing twist|ambidextr')
add('I.9','absent','No second-stage coefficient tower for spectra or D(F_p), loop criterion, or integral π₁/π₂ plus mod-p homology-of-2-connected-cover test appears. The supplied row credits independent checks of GALOIS E.8/E.10 in its source locator, but that is not a review certificate for this entire row or a manuscript proof.', ['RESIDUE I.7','GALOIS E.11','GALOIS G.6'],r'Dossier RESIDUE I.9; companion/chunks/DER_VIII-X.tex, chapter X ms.1–5.',r'second stages|second.stage|loop condition|finite iteration')
add('J.1','absent','The Street-nerve comparison for fine localizations of strict 2-categories over an ordinary base is absent; ordinary functor-category equivalences in cote 115 do not supply it.', ['BISITE C.10','BISITE F.18'],HIGH,r'Street|locally discrete|strict.*2.category|fine class')
add('J.2','absent','No walking-2-cell example, relative strictification, or straightening theorem for a general strict 2-categorical base occurs, so the supplied open recognition problem receives no new proof here.', ['BISITE C.10','BISITE F.18'],HIGH,r'walking.*cell|lax triangle|strictification|straightening')
add('J.3','absent','There is no lax-comma Der 4 base-change theorem or four-variance higher-cell table. Ordinary opposition and sheaf/cosheaf duality in cote 115 do not verify the missing recognition and lax-comma compatibility in this open row.', ['BISITE C.10','BISITE F.18'],HIGH,r'lax.comma|four.variance|cell duality|Der.*4')

assert set(entries)==set(supplied),(set(supplied)-set(entries),set(entries)-set(supplied))

hua=[
 {'id':'108-delta-op-not-test','supplied_status':'conjecture (unsearched) | reach: beyond',
  'relation':'supports the negative answer; differs in literal wording and scope',
  'source':'Hua, modernised reading of cote 108, subsection “Une réponse, la seule de la liste (6)”; RESULTS_STATE finding of the same ID.',
  'note':'Hua’s finding is supported as an unanswered negative assertion on 108/003: the frozen reading asks about both a test category and “wtc” and answers with the underlined English “no”. The modernised reading instead renders “ou non ? non”, dropping the explicit weak-test alternative; neither this line nor its neighbours supply a proof. This checks the manuscript attribution only, not the finding’s mathematical status.',
  'quotes':[(108,3,r'Is the category $\Delta^\circ$ a test category, or wtc? \uline{no}')],
  'state':['Hua 108-delta-op-not-test','BISITE C.1'], 'terms':r'Delta.*circ|test category|wtc|delta-op-not-test'},
 {'id':'112-linearization-beyond-the-simplex','supplied_status':'conjecture (unsearched) | reach: imprecise',
  'relation':'supported programme; several material reading differences',
  'source':'Hua, modernised reading of cote 112, “Lisse”, “Négligeable”, and “Les trois questions”.',
  'note':'The programme beyond Δ is explicit in 112/003, including the Δ_/X question, Ext comparisons and realization of a homotopical truncation; this adds a readable third question to Hua’s subsection (3), which leaves it illegible. The frozen smoothness condition says “est un quasi-iso”, where Hua deliberately chooses “isomorphisme”, and negligibility says “quasi-nul”, where his reading leaves the condition blank. The twisted-coefficient comparison bears on GALOIS G.6/E.11 and RESIDUE I.7, but is a question in this folder, not their functorial higher-coefficient construction.',
  'quotes':[(112,3,r'est un quasi-iso.'),(112,3,r'``quasi-nul\prime\prime'),(112,3,r'OK pour $A=\Delta$, mais est-ce OK pour $A=\Delta_{/X}$')],
  'state':['Hua 112-linearization-beyond-the-simplex','GALOIS G.6','GALOIS E.11','RESIDUE I.7'], 'terms':r'Lisse|Dold|quasi.iso|linearization-beyond'},
 {'id':'114-total-asphericity-independent-of-localizer','supplied_status':'refuted by them | Lean card: the reading dropped a hypothes…',
  'relation':'literal assertion supported with its hypothesis; no completed proof here',
  'source':'Hua, modernised reading of cote 114, “La proposition” and “La démonstration, et ce qu’elle suppose”.',
  'note':'114/004 does state the three-way equivalence in Proposition 4, expressly assuming “a basic localizer satisfying Loc 4)”; its proof ends at “namely”, and 114/005–006 turn to a different faithfulness/generation problem. Hua’s modernised main proposition omits that hypothesis, while its corrective footnote acknowledges the omission and the finding register labels the earlier unrestricted reading refuted. The supplied manuscript supports neither removal of Loc 4) nor completion of the missing implication, and its product-of-representables notion is different from the final-image totality in RESIDUE F and TOTASPH D.7. Hua’s separate cubical counterexample must be assessed under the printed hypothesis, as in the main notes’ primary-source check; it is not disposed of merely by restoring Loc 4).',
  'quotes':[(114,4,r'a basic'),(114,4,r'localizer satisfying Loc 4)'),(114,4,r'namely')],
  'state':['Hua 114-total-asphericity-independent-of-localizer','TOTASPH D.7','RESIDUE F.5','RESIDUE F.6'], 'terms':r'Loc.*4|total.asphericity.independent|cubes|diagonal'},
 {'id':'115-wheel-eleven-curryings','supplied_status':'literature: Settled as mathematics: every node of the wheel…',
  'relation':'supported, with counting and variance qualifications',
  'source':'Hua, modernised reading of cote 115, “Noyaux entre topos de préfaisceaux”, especially its wheel discussion.',
  'note':'115/006 labels “6 Cas” and “4 Cas” and states that every arrow of the diagram is an equivalence, supporting Hua’s eleven distinct presentations when the central kernel category is included. As Hua correctly notes, the drawing repeats both inner curryings, giving thirteen written placements rather than thirteen distinct categories. This is an ordinary set-valued variance diagram; it does not establish the higher coherence or smooth/proper base-change results of RESIDUE I.3/I.5.',
  'quotes':[(115,6,r'(6\text{ Cas})'),(115,6,r'(4\text{ Cas})'),(115,6,r'Toutes les flèches du diagramme sont des équivalences de catégories')],
  'state':['Hua 115-wheel-eleven-curryings','BISITE F.18','RESIDUE I.7'], 'terms':r'onze|wheel-eleven|curry|cohérence|coherence'},
 {'id':'115-isbell-reflexivity-left-open','supplied_status':'literature: Settled: reflexive objects strictly exceed the…',
  'relation':'question supported; finding attaches the negative expectation to the wrong question',
  'source':'Hua, modernised reading of cote 115, “La dualité”, and the findings-register wording reproduced in RESULTS_STATE.',
  'note':'115/008 separately asks whether the adjunction morphisms are isomorphisms only on representables, then whether they are always weak equivalences, with “sans doute pas” on the latter sentence. Thus the register’s assertion that the manuscript answers the representability/reflexivity question “sans doute pas” is not supported by the frozen source; Hua’s longer modernised quotation preserves the two questions more accurately. The third question, whether the duality functors turn weak equivalences into isomorphisms, must also remain separate from ordinary reflexivity.',
  'quotes':[(115,8,r'Iso (si et) seulement si $\Phi$ resp. $\Psi$ est représentable ?'),(115,8,r'\unsure{Est-ce|Est-on} tjrs une équivalence faible (sans doute pas).'),(115,8,r'Les foncteurs $\varphi_A$ et $\psi_A$ transforment-ils équiv. faibles en isom ?')],
  'state':['Hua 115-isbell-reflexivity-left-open','RESIDUE I.7'], 'terms':r'reflexiv|réflexiv|sans doute|Isbell'},
 {'id':'115-isbell-envelope-self-dual','supplied_status':'literature: Settled: this is the Isbell envelope, and the K…',
  'relation':'triple construction and opposition supported; Karoubi interpretation is qualified',
  'source':'Hua, modernised reading of cote 115, “L’enveloppe”.',
  'note':'115/011 defines paired triples and 115/012 writes the canonical opposition equivalence, supporting Hua’s identification of an Isbell-envelope construction and the two embeddings. The further assertion that Kar(A) sits inside the reflexive part is Hua’s modern interpretation: 115/014 has an uncertain bar/tilde-A label below Kar(A), and another diagram writes A = Â ∩ A^{vee,op} with the intersection mark uncertain, so neither its labels nor an equality of completions should be silently regularized. A concrete reading difference also remains at 115/011: frozen H^x(·) is written Hom_B(a,x), whereas Hua supplies Hom_B(x,-); the frozen transcription is unchanged.',
  'quotes':[(115,11,r'la catégorie des triples $(H_*,H^*,\alpha)$'),(115,12,r'$\widetilde{A^\circ}\simeq\widetilde A^\circ$ canonique'),(115,11,r'H^x(\cdot)=\mathrm{Hom}_B(a,x)')],
  'state':['Hua 115-isbell-envelope-self-dual','STRATA B.2','RESIDUE I.7'], 'terms':r'Kar|enveloppe|auto.duale|Isbell'},
 {'id':'115-isbell-duality-derived-from-kernels','supplied_status':'conjecture (unsearched) | Lean card: holds',
  'relation':'supported as a textual specialization, not a priority claim',
  'source':'Hua, modernised reading of cote 115, “Noyaux entre topos de préfaisceaux” and “La dualité”.',
  'note':'The margin of 115/004 explicitly takes B = A-op and the canonical H_A, and 115/008 then writes the two adjoint transforms, their units and representable values; this supports Hua’s kernel-specialization reading. No occurrence of the name Isbell was found in the frozen package, which supports only the local absence of attribution, not independent discovery or priority. “Derived” in this finding’s title means obtained from kernels; these are ordinary Hom/pairing formulas, not the derived six-functor or ambidexterity assertions of RESIDUE I.',
  'quotes':[(115,4,r'Cas $B=A^\circ$, d\prime où élément canonique'),(115,8,r'paires de foncteurs adjoints')],
  'state':['Hua 115-isbell-duality-derived-from-kernels','RESIDUE I.7','BISITE F.18'], 'terms':r'kernel|noyau|Isbell|H_A'}
]
hua[1]['quotes'][1]=(112,3,r'``quasi-nul\prime\prime')
# Use a plain literal substring rather than normalizing manuscript quotation marks.
hua[1]['quotes'][1]=(112,3,'quasi-nul')
hua[-1]['quotes'][0]=(115,4,"Cas $B=A^\\circ$, d'où élément canonique")

def search_context(pattern):
    run=subprocess.run(['rg','-n','-i','-m','2','--glob','*.tex','--glob','*.md',pattern,str(CONTEXT)],capture_output=True,text=True)
    assert run.returncode in (0,1),run.stderr
    matches=[]
    for line in run.stdout.splitlines()[:18]:
        fields=line.split(':',2)
        if len(fields)==3:
            matches.append({'file':str(Path(fields[0]).relative_to(CONTEXT)),
                            'line':int(fields[1]),'excerpt':fields[2][:450]})
    return {'pattern':pattern,'matches':matches,'matching_output_lines':len(run.stdout.splitlines())}

def verify_quote(c,n,q):
    text=(ROOT/'deliverable/pages'/f'{PREFIX}_{c}_scan{n:03d}.tex').read_text()
    if q not in text:
        raise AssertionError((c,n,q))

for row in entries.values():
    for e in row['manuscript_evidence']:
        verify_quote(e['cote'],e['scan'],e['quote'])
    row['context_search']=search_context(row['search_terms'])
for row in hua:
    for c,n,q in row['quotes']:verify_quote(c,n,q)
    row['context_search']=search_context(row['terms'])
for c,n,q in [
    (108,6,r'alors il est cat. test, \uline{sauf} si $A\simeq\Delta_0$'),
    (108,6,r"même s'il est de la forme $\widehat A$"),
    (114,6,r"Contr'exemple: $M$ cat. discrète de cardinal $\geq2$, !"),
    (114,6,r'supposons $G=\{\operatorname{id}_a\}$'),
]: verify_quote(c,n,q)

def esc(value):
    return str(value).replace('|',r'\|').replace('\n',' ')

def evidence(row):
    return '; '.join(f"{e['cote']}/{e['scan']:03d}: `{e['quote']}`" for e in row['manuscript_evidence']) or '—'

lines=[
'# Research draft: exhaustive RESIDUE comparison and Hua findings audit',
'',
'This research-only draft was prepared after the root froze the forty page fragments and combined transcription. It reads the supplied context and the frozen text, not the scans; no transcription file was changed. All manuscript quotations below are literal substrings of the frozen page files and were checked mechanically.',
'',
'## Status and coverage',
'',
'All **56 RESIDUE rows actually supplied** in `DOSSIER_STATEMENTS_WITH_STATUS.md` are covered: B.1–B.17, C.1–C.8, D.1–D.12, F.1–F.7, I.1–I.9 and J.1–J.3. The full RESIDUE research register reportedly contains additional rows, but they were not supplied in this dossier and are not invented here. The exact supplied statement, status and original locator for every row are retained in the companion JSON.',
'',
'“Present” would mean that the specific statement appears; “precursor” marks a related question or ordinary construction without the later theorem; “different” marks a material mismatch of hypotheses, definition or scope; “absent” means that no form of the specific statement was found in these forty pages. An absent row has no purported manuscript scan or quotation. The status column reproduces the return’s claim, not an endorsement: no separate referee verdict for these RESIDUE rows is supplied. RESULTS_STATE links are relevant cross-references, not claims that that file contains an exact entry for every row.',
'',
'The register source is `derivateurs_companion_20261109/pro_returns_20261110/8_RESIDUE/RESIDUE/RESIDUE_results.csv`, as identified by `notes/RESULTS_STATE.md`; that external path itself was not accessed. Context searches were made for each row’s objects or terminology and are retained individually in the JSON.',
'',
'## Two boundaries that govern the comparison',
'',
'**Totality has two meanings.** 114/004 invokes products of representables and cites section 65 A, definition 1, p.170. RESIDUE F.1 expressly invokes the all-final-images definition of *Les Dérivateurs* XII ms.88–89; `companion/chunks/DER_XIIb-a.tex` explicitly warns that this differs from the earlier product/diagonal terminology. Therefore the earlier Proposition 4 cannot settle RESIDUE F.5/F.6 or TOTASPH D.7/F.27 merely by sharing the word “total”.',
'',
'**Cote 115’s duality is ordinary and variance-sensitive.** 115/004 defines Hom-subscript-! by preservation of inductive limits and Hom-superscript-! by preservation of projective limits. The kernel transforms are contravariant in the tested presheaf, and 115/010’s two formulas concern contraction against pullback/left Kan extension; they do not assert universal f_! ≅ f_*, exceptional f^! = f^*, a smooth/proper Beck–Chevalley theorem, or the higher coherence of a symmetric monoidal span functor. The additive derived tensor discussion in 113/013 has its own projective-flatness hypotheses and also does not imply those claims.',
'',
'## One row per supplied RESIDUE statement',
'',
'| Exact ID | Supplied claim status | Original source locator | Relation | Manuscript evidence | Comparison (1–4 sentences) | Context / RESULTS_STATE links |',
'|---|---|---|---|---|---|---|'
]
for row in entries.values():
    locator=row['supplied_source_locator'] or '— (blank in supplied dossier)'
    context=row['context_locator']+' State: '+', '.join(row['results_state_links'])+'.'
    lines.append('| '+' | '.join(esc(v) for v in [row['id'],row['supplied_status'],locator,row['relation'],evidence(row),row['note'],context])+' |')

lines += ['', '## Michel Hua’s seven supplied findings', '',
'Credit for the findings and modernised readings belongs to **Michel Hua’s project**. Their recorded literature or Lean statuses are reproduced as supplied; neither the cited literature nor Lean files are included as proof certificates in this task, and this audit checks their relation to the frozen manuscript. Hua’s page numbers are one less than the archive scan numbers used below.', '']
for row in hua:
    lines += ['### Hua, findings register, '+row['id'],'',
              '**Supplied status:** '+row['supplied_status']+'. **Relation:** '+row['relation']+'.', '',
              row['note'],'',
              '**Frozen evidence:** '+'; '.join(f'{c}/{n:03d}: `{q}`' for c,n,q in row['quotes'])+'.','',
              '**Context:** '+row['source']+' **Bears on:** '+', '.join(row['state'])+'.','']

lines += ['## Additional comparison notes for the root to merge', '',
"**Hua-108-mobile (reading question; 108/006).** Hua’s modernised cote 108, “Le feuillet mobile”, reads the contractor conclusion as an equivalence with A ≅ Δ₀ and paraphrases the preceding claim as excluding presheaf topoi; the frozen page instead reads `alors il est cat. test, \\uline{sauf} si $A\\simeq\\Delta_0$` and `même s'il est de la forme $\\widehat A$`. These reverse the force of the modernization’s paraphrase, so the context must not be used to repair the frozen text. Bears on RESULTS_STATE’s Hua orientation and BISITE C.1; context search: `contracteur|feuillet mobile|Delta_0`.", '',
'**Hua-115-product (reading/claim comparison; 115/004).** Hua’s “Noyaux entre topos de préfaisceaux” repeats the manuscript’s unrestricted assertion that the external product is fully faithful. The root’s separate BISITE comparison supplies the elementary counterexample and should be cross-referenced here once, without treating Hua’s modernized statement as independent verification.', '',
"**Hua-114-discrete (own check of a modernised claim; 114/006).** Hua’s modernised cote 114, “La partie asphérique peut être ponctuelle sans rien engendrer”, concludes that the functor out of the discrete M is not faithful. That conclusion is false: every Hom set in a discrete category has at most one element, so every functor out of it is faithful (and automatically reflects isomorphisms of its source arrows). The frozen page says only `Contr'exemple: $M$ cat. discrète de cardinal $\\geq2$, !`, leaving the precise target of the example to be interpreted; it does not justify Hua’s added non-faithfulness claim. Confidence: high, by the definition of faithfulness; context: the named Hua subsection, distinct from the presheaf-restriction counterexample in his preceding subsection.", '',
'**Hua-114-monoid (reading question; 114/006).** The frozen text says “supposons $G=\\{\\operatorname{id}_a\\}$”, whereas Hua’s explanatory footnote reads a deduction that G is necessarily trivial. His proposed diagonal-action argument invokes a group although End(a) is introduced only as a monoid, so it cannot be imported without an additional hypothesis or proof. This is a context-induced reading question, not a change to the frozen source; it bears on the Hua total-asphericity finding and its distinction from RESIDUE F.', '',
'## Limits and open comparison work', '',
'This draft does not adjudicate the truth of every supplied research-return claim, and no unreviewed claim is promoted to an established result. Its absences are bounded by the frozen forty-page package. In particular it supplies no solution to the bare-derivator or accessible-localizer questions in RESIDUE I.7, no identification of ordinary Isbell duality with derived ambidexterity, and no translation of product/diagonal totality into the all-final-images notion.', '',
'The Hua comparisons preserve unresolved readings: 112’s exponent b/flat, 115’s one/double tilde and bar/tilde distinction, and 115/011’s H^x variance. All are research questions only; the frozen transcription stays unchanged.', '']

out={'scope':'Research-only comparison with frozen transcription; no image rereading or transcription changes.',
     'coverage_ids':list(entries), 'coverage_count':len(entries),
     'hua_coverage_ids':[r['id'] for r in hua], 'hua_coverage_count':len(hua),
     'rows':list(entries.values()), 'hua_findings':hua}
(OUT/'research_residue_hua.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(OUT/'research_residue_hua.md').write_text('\n'.join(lines))
(OUT/'research_residue_hua_coverage.txt').write_text('\n'.join(list(entries)+['Hua '+r['id'] for r in hua])+'\n')
print(json.dumps({'residue_rows':len(entries),'hua_findings':len(hua),'quote_checks':'passed',
                  'relations':{k:sum(r['relation']==k for r in entries.values()) for k in ('present','precursor','different','absent')}},indent=2))
