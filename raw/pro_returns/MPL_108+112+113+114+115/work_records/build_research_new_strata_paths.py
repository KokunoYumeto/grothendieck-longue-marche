from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path('/workspace/scratch/cb96d9ba0f27')
OUT = ROOT / 'deliverable/work_records'
TRANSCRIPT = ROOT / 'deliverable/MPL_108+112+113+114+115_transcription.tex'
FROZEN_SHA = '38a275c286614227ad83cc1e02a51927099b21f7d7c625296ced18f2a52f60fc'
assert hashlib.sha256(TRANSCRIPT.read_bytes()).hexdigest() == FROZEN_SHA

def rows(path, prefix):
    result = []
    for n, line in enumerate((ROOT/path).read_text().splitlines(), 1):
        if re.match(prefix, line):
            cols = line[2:-2].split(' | ')
            result.append((n, cols))
    return result

ANCHORS = {
    'model': ('108', 3, r'$(Cat)$ a model category?', 'item 3; archive foliation 2'),
    'pointed': ('108', 3, '10) Pointed homotopy types and group objects', 'item 10; archive foliation 2'),
    'cubical': ('108', 3, r'b) Cubical games\ldots', 'item 6(b); archive foliation 2'),
    'integral': ('108', 3, r'notion of $\int.$ of homotopy types, as a $\varinjlim$ --- and dual notion.', 'item 8; archive foliation 2'),
    'fibration': ('108', 4, 'tel que le chgt. de base transforme équiv. faibles en équiv. faibles', 'item 11; archive foliation 3'),
    'pullback': ('108', 4, r'$f$ fib, $g\in\underline W\implies g\prime\in\underline W$', 'item 12; archive foliation 3'),
    'homs': ('108', 4, r'\uline{\unsure{Homs}} in $(Hot)$ and diagram variants\ldots', 'item 14; archive foliation 3'),
    'connected': ('108', 4, r'Is a \deleted{tot} 0-connected topos also totally $\infty$-connected?', 'item 13; archive foliation 3'),
    'homotopisms': ('108', 5, r'pour les localisés par les \uline{homotopismes} ?', 'item 16; archive foliation 4'),
    'finiteproducts': ('108', 6, r'une cat $A$ avec \deleted{objet fi-} produits finis', 'archive foliation 5'),
    'mu': ('113', 3, r'ne fasse pas sortir des $MU$-fibrés semi-simpliciaux, il suffit que', 'cancelled paragraph; archive foliation 2'),
    'derived': ('113', 13, 'peut se calculer indifféremment par résolutions projectives', 'archive foliation 12'),
    'psproduct': ('114', 4, r'in $\widehat A$ is 0-connected.', 'draft Proposition 4(iii), printed PS draft numbered 350; archive foliation 3'),
    'faithful': ('114', 5, r'$f^*: \widehat B\longrightarrow\widehat A$ conservatif et fidèle', 'author p.1; archive foliation 4'),
    'pairing': ('115', 10, r'\langle\Phi_*,f^{\circ *}(\Psi^*)\rangle_A&\simeq\langle f_!(\Phi_*),\Psi^*\rangle_B', 'author circled p.4; archive foliation 9'),
}
# Keep the diplomatic apostrophe, rather than silently changing it to a prime macro.
ANCHORS['pullback'] = ('108', 4, "$f$ fib, $g\\in\\underline W\\implies g'\\in\\underline W$ dans axiomatique de Quillen.", 'item 12; archive foliation 3')

for key, (cote, scan, quote, loc) in ANCHORS.items():
    p = ROOT / f'deliverable/pages/MPL_108+112+113+114+115_{cote}_scan{scan:03}.tex'
    assert quote in p.read_text(), (key, 'quote not literal')

I = ['context/companion/chunks/DER_I-a.tex']
VI = ['context/companion/chunks/DER_VI-c.tex']
VIIA = ['context/companion/chunks/DER_VII-a.tex']
VIIB = ['context/companion/chunks/DER_VII-b.tex']
VIIC = ['context/companion/chunks/DER_VII-c.tex']
IX = ['context/companion/chunks/DER_VIII-X.tex']
V = ['context/companion/chunks/DER_III-V.tex']
II = ['context/companion/chunks/DER_II-a.tex']
XII = ['context/companion/chunks/DER_XIIb-a.tex']
XIIAPP = ['context/companion/chunks/DER_XIIapp.tex']
XVI = ['context/companion/chunks/DER_XVI.tex']

M = {}
def add(id, title, relation, anchors, note, files, terms, states=()):
    assert id not in M
    M[id] = dict(title=title, relation=relation, anchor_keys=anchors.split() if anchors else [],
                 note=note, companion_search_files=files, search_terms=terms, state_refs=list(states))

# NEW_RESULTS: the exact source statement, author credit and checked-by column are
# copied from the supplied table when assembling the output, not rewritten here.
add('NEW_RESULTS #1', 'Finite monoids: finiteness, dimension, bounded homology', 'absent', '',
    'No finite-monoid classifying-space theorem or bounded-homology argument is stated in the frozen pages; the finite-product example in cote 108 does not assume that the category is finite. The later finite-model programme in RESULTS_STATE is a research cross-reference, not a theorem of this dossier.', V+XIIAPP,
    ['finite monoid', 'monoid', 'type fini'], ['CATHOT G.17', 'FINMON'])
add('NEW_RESULTS #2', 'Miller theorem under a cohomological bound', 'absent', '',
    'No map from a finite-group classifying space, cohomological-bound variant of Miller, or residual-finiteness argument occurs in these pages. This is supplied as a proof tool for NEW_RESULTS #1, not as a manuscript proposition.', V,
    ['Miller', 'cohomological', 'finite group'], ['CATHOT G.17'])
add('NEW_RESULTS #3', 'Kan–Thurston without small quotients; invariant ind-objects', 'absent', '',
    'The package gives no Kan–Thurston construction, cardinal bound, or groupoid-completion theorem for invariant ind-objects. RESULTS_STATE retains an older open CATHOT E.17 entry while the supplied NEW_RESULTS and PATHS D.K3–D.K4 record later positive claims; those layers are not a new proof in these pages.', V+VIIC+IX,
    ['Thurston', 'ind-objet', 'groupo'], ['CATHOT E.17', 'PATHS'])
add('NEW_RESULTS #4', 'Uncountably many maps into the two-sphere', 'absent', '',
    'There is no sphere-retraction hypothesis, uncountability assertion, or computation of maps into S² in the package. The later S2COUNT headline in RESULTS_STATE is related research history and does not supply a missing manuscript statement here.', V,
    ['uncount', 'non dénombr', 'sphère'], ['S2COUNT'])
add('NEW_RESULTS #5', 'At least 34 arrows for posets of type RP²', 'absent', '',
    'Neither an RP² poset nor an arrow-count lower bound is present. The older size interval in CATHOT G.17 and the newer bound in the supplied result are separate register versions, not evidence on a scan.', XIIAPP,
    ['projectif', 'RP', 'poset'], ['CATHOT G.17'])
add('NEW_RESULTS #6', 'Small-category census: 4, 5, 7 arrows', 'absent', '',
    'The scanned dossier contains no enumeration of categories or proof of these minima or uniqueness clauses. The manuscript source for Grothendieck’s sphere models is the supplied later XII appendix, not any cote in this package.', XIIAPP,
    ['sphère', 'flèches', 'mono'], ['CATHOT G.17', 'FINMON'])
add('NEW_RESULTS #7', 'Reversible localizer not detected by spectra', 'absent', '',
    'No reversible localizer, stable closure, or RP∞/RP² separation is defined here, and the strong W(7) is absent. The POLES F.14 open classification entry and the newer supplied construction must retain their own dates and review levels.', XII+XVI,
    ['revers', 'révers', 'spectr'], ['POLES F.14', 'REVLOC'])
add('NEW_RESULTS #8', 'Strong W(7): failure of XII Theorem 2 for W∞', 'different', 'pullback',
    'The quoted item concerns preservation of a weak equivalence by a Cartesian pullback along a fibration; it is not the reverse implication in a sieve-cover gluing square or cube. Strong W(7 bis)/W(7) and the assertion for W∞ are located only in the supplied later XII text at manuscript pages 75–78, so no 1983 version of the claimed counterexample is present.', XII,
    ['W(7', 'Axiome du cube', 'Théorème 2'], ['TOTASPH A.9', 'POLES B.2'])
add('NEW_RESULTS #9', 'Homology localizers fail Loc(7 F)', 'precursor', 'fibration',
    'Item 11 poses the general problem of characterizing categorical weak-equivalence-preserving fibrations and reducing the tests. It contains no trefoil example or failure result for integral or field homology localizers; the supplied later locator is XVI manuscript page 105.', XVI,
    ['7 F', '7F', 'homolog'], ['GALOIS B.7'])
add('NEW_RESULTS #10', 'Totality of fixed-origin paths forces totality of a simply connected base', 'absent', '',
    'No fixed-origin categorical path functor or implication of this form is stated in the package. The cancelled semisimplicial MU-fibré integration is too different to identify with this theorem.', XII,
    ['simplement connexe', 'origine', 'totalement'], ['TOTASPH D.7', 'PATHS'])
add('NEW_RESULTS #11', 'Δinj refutes total W∞-aspherical ⇒ filtered', 'different', 'psproduct',
    'Proposition 4 is about the Pursuing Stacks product/diagonal sense of total asphericity, under Loc 4, and does not assert filteredness. The later universal outgoing-functor definition and the question at II manuscript pages 36/36ter are different context; RESULTS_STATE TOTASPH C.10 and PRETOT A.12 record the supplied Δinj counterexample, without its appearing on these scans.', II+XII,
    ['filtr', '36ter', 'Isbell'], ['TOTASPH C.10', 'PRETOT A.12', 'TOTASPH A.7', 'TOTEX2 D.4'])
add('NEW_RESULTS #12', 'RP² is not the classifying space of a finite monoid', 'absent', '',
    'The package neither discusses the cited 2026 conjecture nor gives a finite-monoid obstruction for RP². Preserve the supplied record of the original return and the later Miller/Atiyah checks rather than attributing their argument to the manuscript.', V+XIIAPP,
    ['Miller', 'Atiyah', 'monoid'], ['CATHOT G.17'])

add('STRATA D.1', 'Exceptional adjunction chains and support images', 'precursor', 'pairing',
    'Cote 115 gives an ordinary presheaf/copresheaf pairing adjunction, which is a genuine categorical precursor to exchange formulas. It does not define an open/closed decomposition, exceptional support images, or the asserted four-term pointed-derivator adjunction chains.', I,
    ['j_!', 'i^!', 'recollement'], ['STRATA', 'STRATA 0.1'])
add('STRATA D.2', 'Support fibre/cofiber sequences and stable recollement', 'absent', '',
    'No support subcategory, coherent open–closed fibre/cofiber square, or stable triangulated recollement is constructed in the package. The ordinary correspondence calculus in cote 115 supplies no stability or pointed-derivator hypothesis.', I,
    ['cocart', 'recollement', 'triangle'], ['STRATA', 'STRATA 0.1'])
add('STRATA D.3', 'Exact lifting-poset criterion for properness and smoothness', 'precursor', 'fibration',
    'The manuscript asks for a characterization of weak-equivalence-preserving fibrations in Cat. It does not formulate incoming/outgoing exact lifting posets or an if-and-only-if criterion for finite-poset maps.', I,
    ['lisse', 'propre', 'fibre'], ['STRATA', 'GALOIS B.7'])
add('STRATA D.4', 'Strict-pullback base change under properness/smoothness', 'precursor', 'pullback pairing',
    'The manuscript separately proposes a Quillen pullback-preservation condition and writes an ordinary pairing adjunction. Neither passage asserts the derived Beck–Chevalley theorem for a strict square with a proper or smooth side, nor its detection by space-valued coefficients.', I+VI,
    ['changement de base', 'propre', 'lisse'], ['STRATA', 'BISITE A.19', 'GALOIS D.2'])
add('STRATA D.5', 'Failed topological criteria for categorical properness/smoothness', 'absent', '',
    'There is no finite-poset map compared with a topological proper map, homotopy-fibre comparison, or stratified local product. Thus the refuted criteria and their witnesses have no scan attribution in this dossier.', I+VI,
    ['topologique', 'propre', 'fibre'], ['STRATA'])
add('STRATA D.6', 'Diamond map: smooth/proper but not an opfibration or bundle', 'absent', '',
    'The four-object diamond over [1] does not occur, and no example distinguishes Grothendieck lifting from categorical smoothness/properness. The later VI comparison remains the supplied source.', VI,
    ['fibr', 'localement trivial', 'opposé'], ['STRATA'])
add('STRATA D.7', 'Poset inclusions and product projections', 'absent', '',
    'No proper-cosieve/smooth-sieve classification or product-projection theorem for posets is stated. Cote 115’s ordinary product projections in a presheaf pairing do not identify their categorical properness or smoothness.', I,
    ['cribl', 'cocribl', 'projection'], ['STRATA', 'STRATA 0.1'])
add('STRATA D.8', 'Finite-poset coefficient dictionary and geometric interpretation', 'absent', '',
    'The dossier gives ordinary presheaf and copresheaf duality but no stratification of |NP|, constructible coefficient dictionary, or allowed class of monotone maps. RESULTS_STATE STRATA A.4 and BISITE G.10 are later supplied claims about the relevant dictionary.', I+XII,
    ['constructib', 'stratif', 'topologique'], ['STRATA', 'STRATA A.4', 'BISITE G.10'])
add('STRATA D.9', 'Variance of smooth fibre inclusion and closure order', 'absent', '',
    'Neither the fibre-inclusion target y\\X nor the downset-topology closure convention is asserted here. Ordinary opposite categories in cote 115 do not settle these slice and geometric-variance choices; retain the corrected later locators and RESULTS_STATE STRATA 0.1.', I+XII,
    ['adhér', 'fibre', 'lisse'], ['STRATA', 'STRATA 0.1', 'TOTEX2 D.4'])
add('STRATA G.2', 'Universal homotopy-colimit/strict-colimit criterion for totality', 'different', 'psproduct',
    'The frozen proposition tests products of representables and explicitly invokes Loc 4; it gives neither simplicial diagrams nor a universal ordinary-colimit comparison. The companion explicitly distinguishes this Pursuing Stacks sense from the universal final-image totality defined at XII manuscript pages 88–89, which is the sense relevant to the supplied row.', XII+II,
    ['différente', 'totale', '88'], ['STRATA', 'POLES H.2', 'TOTASPH A.2', 'TOTEX2 D.4'])

add('PATHS A.P1', 'Components of full paths give localized Hom', 'precursor', 'homs mu',
    'The agenda asks about Homs in Hot and the cancelled MU-fibré page draws strings of arrows. Neither defines the full path category with a marking nor identifies its components, naturality, or composition with localized Hom.', VIIB,
    ['localis', 'composantes', 'chemins'], ['PATHS'])
add('PATHS A.P2', 'Sequential/all-type comparison by a fibred roof', 'precursor', 'mu',
    'The cancelled integration paragraph is a precursor to organizing diagram categories by total constructions. It has no type preorder, cofinal sequence, two-legged comparison roof, or assertion that both legs are weak equivalences.', VIIB,
    ['cofinal', 'fibr', 'intégr'], ['PATHS', 'CATHOT E.26'])
add('PATHS A.1', 'Fibred/opfibred Grothendieck span and direction', 'precursor', 'mu',
    'The cancelled page discusses an integral of semisimplicial MU-fibrés under explicit submersion conditions. It does not give the later span C ← C_u → C∞ or a direct comparison, so its arrows must not be used to settle that direction issue.', VIIB,
    ['cofibr', 'fibr', 'limite inductive'], ['PATHS', 'CATHOT E.26'])
add('PATHS A.2', 'Filtered Cat-colimits agree with total categories', 'precursor', 'integral mu',
    'Integration as a colimit is an explicit question, and the cancelled MU-fibré paragraph adds special closure hypotheses. No statement quantifies over all filtered indexing categories and all Cat-valued diagrams; the filtered colimits in cote 113 scan004 concern abelian-category exactness instead.', VIIB,
    ['filtr', 'limite inductive', 'intégr'], ['PATHS', 'TOTASPH A.7'])
add('PATHS A.3', 'Universal total-category equivalence iff all u/t are contractible', 'precursor', 'mu',
    'The cancelled semisimplicial passage assumes asphericity of I as one sufficient input. It does not state a universal base-change criterion in terms of every comma category u/t, and its specific submersion hypotheses cannot be dropped.', VIIB,
    ['asphér', 'fibr', 'cofinal'], ['PATHS', 'GALOIS B.3'])
add('PATHS A.4', 'Preorder cofinality and parallel homotopies are insufficient', 'absent', '',
    'No failure witness for the asserted total/sequential comparison or corresponding preorder-cofinality claim occurs. The cancelled MU-fibré passage supplies neither the rejected assertion nor its counterexample.', VIIB,
    ['cofinal', 'homotop', 'suite'], ['PATHS', 'CATHOT E.26'])
add('PATHS A.5', 'Δinj totality does not ensure all Cat-colimits are correct', 'different', 'psproduct',
    'The manuscript’s product criterion uses the earlier Pursuing Stacks sense of totality, not the later universal final-image condition. No Δinj diagram of monoids, homology-in-every-degree computation, or circle-valued Cat-colimit is present.', VIIB+II+XII,
    ['inject', 'filtr', 'totalement'], ['PATHS', 'TOTASPH C.10', 'PRETOT A.12'])
add('PATHS A.6', 'Δinj: exact abelian colimits, total, not filtered', 'different', 'psproduct',
    'No Δinj counterexample or abelian-colimit theorem appears, and the identical word “total” in Proposition 4 has the different product/diagonal meaning. The relevant supplied status is TOTASPH C.10/PRETOT A.12, not a result proved in cote 114.', II+XII,
    ['Isbell', 'filtr', 'inject'], ['PATHS', 'TOTASPH C.10', 'PRETOT A.12'])
add('PATHS A.7', 'Strict inclusion of universally correct Cat-colimit shapes', 'absent', '',
    'The package gives no classes of universally correct Cat-colimit shapes and no strict inclusion between them. RESULTS_STATE’s later totality/exactness programme and older open TOTASPH D.7 are contextual status layers, not a classification supplied by these pages.', VIIB+II+XII,
    ['filtr', 'totalement', 'limite inductive'], ['PATHS', 'TOTASPH D.7', 'TOTASPH A.7', 'RESIDUE F.3'])
add('PATHS A.8', 'Open intrinsic classification of Cat-colimit shapes', 'absent', '',
    'No intrinsic classification is attempted here, and the dossier supplies no answer to the specified open target. RESULTS_STATE RESIDUE F.3 provides later claimed special cases only; it is not a general resolution of PATHS A.8.', VIIB+XII,
    ['filtr', 'limite inductive', 'totalement'], ['PATHS', 'RESIDUE F.3'])
add('PATHS A.9', 'Subdivision weak equivalence without Cat-hot inverse', 'precursor', 'homotopisms',
    'The manuscript explicitly asks for equivalences after localization by homotopisms, so the distinction from nerve weak equivalence is relevant. It gives no six-face circle poset, reverse-map enumeration, or degree-zero obstruction.', VIIC+V,
    ['homotopismes', 'homotopie', 'subdiv'], ['PATHS', 'POLES D.5'])

add('PATHS B.1', 'Full/weak-vertical path diagrams and strict concatenation', 'precursor', 'mu',
    'The arrow strings and submersion diagrams are a limited combinatorial precursor. They define neither all path types with a marked subcategory nor the full/weak-vertical inclusion or strict concatenation law.', VIIA+VIIB,
    ['chemins', 'composition', 'types'], ['PATHS'])
add('PATHS B.2', 'Restricted all-type nerve and hammocks', 'absent', '',
    'No weak-vertical hammock, reduction to a mapping simplicial set, or composition-compatible nerve comparison occurs. The supplied row’s “Known” status is retained as its own return claim.', VIIA+VIIB,
    ['hammock', 'hammac', 'localisation simpliciale'], ['PATHS'])
add('PATHS B.3', 'The inclusion J need not be an isomorphism', 'absent', '',
    'The package never defines this J, saturated path markings, or a counterexample to categorical isomorphism. Nothing here upgrades a possible weak equivalence to a literal isomorphism.', VIIB,
    ['satur', 'chemins', 'isomorphisme'], ['PATHS'])
add('PATHS B.4', 'Identity/all-arrow markings as sufficient cases', 'absent', '',
    'No theorem about the path comparison when only isomorphisms are marked or all arrows are marked is stated. The ordinary categorical Yoneda identities in cote 115 do not concern this J.', VIIB,
    ['isomorphismes', 'chemins', 'discr'], ['PATHS'])
add('PATHS B.5', 'Homotopy fraction calculi on the restricted side', 'absent', '',
    'There is no homotopy calculus of fractions or argument forcing vertical arrows to be marked by two-out-of-three. The dashed and doubled arrows in the MU-fibré page do not specify that calculus.', VIIB,
    ['fractions', 'localis', 'vertical'], ['PATHS'])
add('PATHS B.6', 'Full-path comparison makes J split monic in Hot', 'absent', '',
    'No map from full paths to localization mapping spaces or factorization through a hammock comparison is constructed. Consequently the split-monomorphism conclusion has no scan source here.', VIIB,
    ['chemins', 'localis', 'composition'], ['PATHS'])
add('PATHS B.7', 'Identity padding of a backward square', 'absent', '',
    'No identity-padding or grid-sweep theorem is present. Commutative squares on the MU-fibré page are not identified with arbitrary backward marked-path squares.', VIIB,
    ['identit', 'carré', 'chemins'], ['PATHS'])
add('PATHS B.8', 'Open unrestricted-vertical comparison', 'absent', '',
    'The package neither formulates nor settles whether the full/weak-vertical J is always a weak equivalence. The supplied Open status remains untouched, including its listed marking/model-category variants.', VIIB+IX,
    ['vertical', 'hammock', 'localis'], ['PATHS'])
add('PATHS B.9', '132 bounded finite comparisons', 'absent', '',
    'There is no bounded computational search or comparison of H0 and H1 over F2 in the manuscript. The numerical report belongs solely to the supplied return.', VIIB,
    ['homolog', 'chemins', 'fini'], ['PATHS'])

add('PATHS C.P1', 'Contractible endpoint-preserving type-map categories', 'absent', '',
    'No category of endpoint-preserving maps between path types or its categorical contraction is defined. The manuscript’s semisimplicial submersion conditions do not state this enriched-composition lemma.', VIIB,
    ['extrémit', 'contract', 'type'], ['PATHS'])
add('PATHS C.P2', 'Descent to a reachability preorder and cofinal sequences', 'absent', '',
    'No reachability preorder of types, coherent descent, or homotopy-final sequence is specified. A general integration notation cannot supply these particular index categories or their finality proofs.', VIIB+VIIC,
    ['préord', 'cofinal', 'types'], ['PATHS', 'CATHOT E.26'])
add('PATHS C.P3', 'Three CATHOT E.26 comparisons for arbitrary wide markings', 'absent', '',
    'The three specified all-type comparisons are not present. RESULTS_STATE retains the older open CATHOT E.26 entry, whereas this supplied PATHS row claims a later resolution; keep both provenance layers without re-proving either.', VIIB+VIIC+V,
    ['cofinal', 'types', 'homotop'], ['PATHS', 'CATHOT E.26'])
add('PATHS C.P4', 'Mixed-sign padding and block-independent Hot composition', 'absent', '',
    'No mixed-sign block, padding comparison, or canonical associative/unital composition obtained from it occurs. The question about Homs in Hot is too general to constitute this particular operation.', VIIC+IX,
    ['composition', 'types', 'signes'], ['PATHS', 'FINMON F:C22-types'])
add('PATHS C.P5', 'Four-object crown refutes Cat-hot invertibility of qL', 'absent', '',
    'The four-object crown and the map qL are absent. No claim here about categorical homotopisms furnishes that concrete noninvertibility witness.', VIIC+V,
    ['homotopie', 'chemins', 'équivalence'], ['PATHS'])
add('PATHS C.1', 'Strict Cat-enrichment and a Segal model', 'precursor', 'homs mu',
    'The dossier asks for Hom and diagram variants and draws composable strings, which are plausible programme-level precursors. It does not construct the all-type Cat-enrichment, product-preserving Kan replacement, or Segal model.', IX,
    ['enrich', 'composition', 'Segal'], ['PATHS'])
add('PATHS C.2', 'Weak-vertical hammocks model simplicial localization', 'absent', '',
    'No hammock or simplicial-localization comparison occurs. In particular there is no textual basis for replacing arbitrary vertical arrows by weak ones.', IX,
    ['hammock', 'hammac', 'simplicial'], ['PATHS'])
add('PATHS C.3', 'Pointed composition: Cartesian obstruction and smash unit', 'precursor', 'pointed',
    'The manuscript asks about pointed homotopy types and group objects. It gives no absorbing-zero condition or argument distinguishing Cartesian from smash composition and the S0 unit.', IX,
    ['pointé', 'zéro', 'composition'], ['PATHS'])
add('PATHS C.4', 'Pointed simplicial models with strict zero and smash units', 'precursor', 'pointed model',
    'Pointed homotopy types and model-category structure are questions in the agenda. The package does not construct cofibrant-fibrant mapping spaces, strict zeros, or their composition and units.', IX,
    ['pointé', 'fibrant', 'composition'], ['PATHS'])
add('PATHS C.5', 'Quillen fundamental groupoid versus derived mapping complexes', 'absent', '',
    'The name Quillen and derived-category notation elsewhere do not state this mapping-space groupoid comparison. No chosen vertices, basepoint paths, or induced π1 isomorphisms are provided.', IX,
    ['Quillen', 'groupo', 'fondamental'], ['PATHS'])
add('PATHS C.6', 'Loop/suspension mapping-space formulas', 'precursor', 'pointed',
    'The pointed-group-object and Dold–Puppe questions are a broad precursor to loop-space structures. There is no mapping-space formula under pullback/pushout hypotheses or derivator adjunction with the asserted exactness.', IX,
    ['suspension', 'lacet', 'adjoint'], ['PATHS'])
add('PATHS C.7', 'π1 representability does not force loop formulas', 'absent', '',
    'No representability test for all π1 mapping functors or counterexample separating it from loop formulas occurs. The ordinary representability questions in cote 115 concern presheaf/copresheaf duality instead.', IX,
    ['représent', 'lacet', 'suspension'], ['PATHS'])
add('PATHS C.8', 'Truncated derived Hom with tensor composition', 'precursor', 'derived',
    'Cote 113 constructs derived contractions using projective resolutions and records flatness/exactness hypotheses. It does not define the truncated derived Hom enrichment in D≤0(k), its units, tensor composition, or the mapping-space homotopy-group identifications.', IX+['context/ps_chapters_VI_VII/ps7.tex'],
    ['Hom', 'dériv', 'tensor'], ['PATHS', 'GALOIS G.6'])
add('PATHS C.9', 'Open general additive relative-category proposal', 'precursor', 'derived',
    'The explicit projective and k-flat hypotheses in cote 113 show the narrower setting of its derived pairing construction. They neither prove the unspecified general additional axioms of IX nor show that finite-sum closure of a saturated weak class suffices.', IX+['context/ps_chapters_VI_VII/ps7.tex'],
    ['additif', 'satur', 'dériv'], ['PATHS', 'GALOIS G.6', 'GALOIS E.11'])
add('PATHS C.10', 'Open pointed and pointed-ind stabilized paths', 'precursor', 'pointed',
    'The pointed-type question does not define pointed ind-categories or stabilized full paths. No resolution of the supplied open refinements can be extracted from it.', IX,
    ['pointé', 'ind-', 'chemins'], ['PATHS', 'CATHOT E.17'])

add('PATHS D.1', 'Typed and size-bounded IX tests', 'precursor', 'homs',
    'The brief Hom/diagram agenda is earlier and substantially weaker than the typed IX tests. It specifies neither a universe bound nor the two representability directions or readings of homotopy.', IX,
    ['représent', 'univers', 'homotop'], ['PATHS', 'PATHS D.22'])
add('PATHS D.2', 'Five-arrow pointed rectification example', 'absent', '',
    'No five-arrow pointed category with identity weak equivalences or rectification/enhancement claim appears. The counterexample to Lead 3 is confined to the supplied return.', IX,
    ['pointé', 'rectif', 'cinq'], ['PATHS'])
add('PATHS D.3', 'Finite category with finite products is a preorder', 'different', 'finiteproducts',
    'The displayed example assumes finite products, not a finite underlying category, and is intended to remain nonterminal despite having a zero object. It therefore does not contradict or prove the finite-category proposition and must not be reported as its example.', IX,
    ['produits finis', 'fini', 'préord'], ['PATHS'])
add('PATHS D.4', 'Rectifiability implies constant-diagram mapping formula', 'absent', '',
    'No rectifiability hypothesis on a specified shape class or formula [BA, MapL(a,b)] for localized constant-diagram Homs is stated. Ordinary presheaf Hom identities in cote 115 are not this derived assertion.', IX,
    ['constant', 'rectif', 'Hom'], ['PATHS', 'PATHS D.22'])
add('PATHS D.5', 'Six-object suspension-poset failure of restriction surjectivity', 'absent', '',
    'Neither this suspension poset nor the parallel-arrow target and nonsurjective restriction is present. No counterexample scan can be assigned.', VIIC+IX,
    ['suspension', 'surject', 'Hom'], ['PATHS'])
add('PATHS D.6', 'Loop identities imply representability; finite tests are weaker', 'absent', '',
    'There is no hierarchy of IX tests (a), (b), (c) or implication among them in this dossier. The pointed-type agenda alone does not provide either the positive implication or the finite-poset limitation.', IX,
    ['représent', 'suspension', 'lacet'], ['PATHS', 'PATHS D.22'])
add('PATHS D.7', 'Derivable/ABC/Quillen rectification ranges', 'precursor', 'model',
    'The manuscript asks whether Cat and presheaf categories are model categories. It gives no finite derivable or ABC axioms and no theorem rectifying finite direct/inverse or all small diagram shapes.', IX,
    ['rectif', 'Quillen', 'dérivable'], ['PATHS'])
add('PATHS D.8', 'Finite intrinsic-cofibration axioms imply rectification', 'absent', '',
    'The initial-object, pushout, and intrinsic-cofibration package is not formulated here. The pullback condition for fibrations in cote 108 is not a proof of its dual finite rectification theorem.', ['context/companion/chunks/DER_XIIc-a.tex', 'context/companion/chunks/DER_XIIc-b.tex']+IX,
    ['cofibr', 'somme amalgamée', 'initial'], ['PATHS', 'POLES H.5'])
add('PATHS D.9', 'Diamond and finite-set failures of stronger cofibration axioms', 'absent', '',
    'No diamond-lattice cofibrancy calculation or finite-set example separating CF5/CF6 from finite axioms occurs. The manuscript’s finite-product examples address test categories instead.', ['context/companion/chunks/DER_XIIc-b.tex']+IX,
    ['cofibr', 'fini', 'initial'], ['PATHS'])
add('PATHS D.10', 'Cubical rectification does not imply finite-poset rectification', 'precursor', 'cubical',
    '“Cubical games” is only an agenda item. No rectification test, six-element circle poset, or degree-two obstruction is supplied.', IX,
    ['cube', 'cubiq', 'rectif'], ['PATHS', 'PATHS D.22'])
add('PATHS D.11', 'Finite simplicial sets fail rectification at BZ', 'absent', '',
    'No finite-automorphism/Nielsen-monodromy example or BK-fibrant opposite is present. The separate “no” about Δ opposite being a test category has no stated connection to this counterexample.', IX,
    ['simplicial', 'rectif', 'automorph'], ['PATHS'])
add('PATHS D.12', 'Contractible fence rectifies but is not BK-fibrant', 'absent', '',
    'No nine-vertex fence, Ex² nerve, or unfillable inner horn is considered. The package does not address the converse BK question.', IX,
    ['fibr', 'nerf', 'contract'], ['PATHS'])
add('PATHS D.13', 'Relative-poset presentations need not rectify', 'absent', '',
    'The finite circle and countable signed-face orbit posets presenting BZ and BC2 do not appear. Neither relative-poset localization nor its rectification failure is established here.', VIIC+IX,
    ['localis', 'rectif', 'ordonné'], ['PATHS'])
add('PATHS D.14', 'Kaledin v3 shape and scope audit', 'absent', '',
    'No Kaledin text or its Pos, Pos+, and Pos+− shape classes occurs in these historical pages. This is a modern bibliographic/scope claim in the supplied return, not manuscript evidence.', IX,
    ['Kaledin', 'posets', 'univers'], ['PATHS'])
add('PATHS D.15', 'Kaledin enhancement iff coherent localization comparisons', 'absent', '',
    'There is no Kaledin enhancement or comparison to coherent L(M,W)-diagram categories. The ordinary functor-category equivalences in cote 115 do not give this criterion.', IX,
    ['Kaledin', 'cohérent', 'localis'], ['PATHS'])
add('PATHS D.16', 'Circle fails countable additivity; finite IX example does not', 'absent', '',
    'The bounded-winding argument for countable discrete shapes is absent. Neither example nor enhancement-axiom conclusion can be attached to these scans.', IX,
    ['additiv', 'dénombr', 'chemins'], ['PATHS'])
add('PATHS D.17', 'Later Cof0–Cof4 and quillenisable rectification results', 'precursor', 'model',
    'The model-category question is an early programme item. It contains no later Cof0–Cof4 axioms, quillenisable classes, filtered-colimit upgrade, or rectification/Kan-extension theorem.', ['context/companion/chunks/DER_XIII-a.tex', 'context/companion/chunks/DER_XVII-a.tex', 'context/companion/chunks/DER_XIX.tex'],
    ['Cof', 'quill', 'filtr'], ['PATHS'])
add('PATHS D.18', 'Accessible Cat localizers, Thomason models, and rectification', 'precursor', 'model fibration',
    'Cote 108 juxtaposes the Cat model-category problem and the stronger weak-equivalence-preserving fibration question. It neither defines accessibility nor constructs a Thomason model or proves the all-shape rectification and properness qualifications.', XVI+IX,
    ['accessib', 'Thomason', 'quill'], ['PATHS', 'GALOIS B.4', 'GALOIS B.7'])
add('PATHS D.19', 'Locally constant fully faithful restriction fails two-out-of-three', 'different', 'faithful',
    'Cote 114 tests faithfulness/conservativity of ordinary presheaf restriction and then adds a generator condition. It does not assert full faithfulness on locally constant coefficients or exhibit e → BC2 → e, so the supplied saturation counterexample is neither proved nor contradicted by that passage.', ['context/companion/chunks/DER_I-b.tex']+IX,
    ['localement constant', 'pleinement fidèle', 'satur'], ['PATHS', 'GALOIS D.2', 'BISITE A.19'])
add('PATHS D.20', 'Modern references; coherent arrows differ from arrows in Ho', 'absent', '',
    'The Arlin and Fuentes-Keuthan-Kedziorek-Rovelli reference audit is modern context. No coherent-arrow example with Z morphisms versus one or strict/pseudonatural comparison is stated in the package.', IX,
    ['Arlin', 'pseudonat', 'cohérent'], ['PATHS'])
add('PATHS D.21', 'Mapping-space upgrade from every Kaledin shape', 'absent', '',
    'No equivalence R(A×J) or comparison L(M^A) → Fun(NA,L(M)) appears. Ordinary currying in cote 115 does not establish localization commuting with a diagram category.', IX,
    ['Kaledin', 'localis', 'Hom'], ['PATHS'])
add('PATHS D.22', 'Exact remaining recognition and rectification questions', 'absent', '',
    'The package supplies no resolution of any of the listed finite/cardinal recognition, BK, no-initial-object, IX-test, or nonaccessible-localizer targets. Cite the exact open ID PATHS D.22 in RESULTS_STATE, without treating broad agenda questions as solutions.', IX+XVI,
    ['rectif', 'fibr', 'localisateur'], ['PATHS', 'PATHS D.22', 'GALOIS B.13'])
add('PATHS D.23', 'Homology localizers lack enough intrinsic fibrations', 'precursor', 'fibration',
    'The fibration-characterization question is relevant to this later obstruction. The pages give no nonzero-spectrum homology localizer, free-group nullity, or nonsurjective identity-homology endomorphism.', XVI,
    ['homolog', 'fibr', 'spectr'], ['PATHS', 'GALOIS B.7'])
add('PATHS D.K1', 'Acyclic maps are Hot epimorphisms with double-pushout criterion', 'absent', '',
    'No acyclic-map epimorphism theorem or double-pushout codiagonal occurs. This cannot be supplied by the manuscript’s separate Cartesian pullback proposal.', V,
    ['acycl', 'épimorph', 'somme amalgamée'], ['PATHS', 'CATHOT E.17'])
add('PATHS D.K2', 'Embedding groups in large simple acyclic groups', 'absent', '',
    'The package has no simple-acyclic-group embedding or prescribed cardinality construction. Pointed group objects in an agenda question are not such a result.', V,
    ['acycl', 'cardinal', 'simple'], ['PATHS', 'CATHOT E.17'])
add('PATHS D.K3', 'Cardinality-controlled Kan–Thurston', 'absent', '',
    'No acyclic BG presentation or perfect-kernel small-quotient property is constructed. The later positive claim is also recorded under NEW_RESULTS #3, whose independent proof routes and review qualifications must remain distinct.', V,
    ['Thurston', 'acycl', 'cardinal'], ['PATHS', 'CATHOT E.17'])
add('PATHS D.K4', 'Invariant ind-objects reduce to groupoids with the same index', 'absent', '',
    'No filtered ind-presentation, W1 inversion, or same-index groupoid-completion ind-isomorphism is stated. The supplied PATHS claim and NEW_RESULTS #3 are later developments relative to the older open CATHOT E.17 record.', V+VIIC,
    ['ind-', 'groupo', 'invariant'], ['PATHS', 'CATHOT E.17'])
add('PATHS D.K5', 'All-small constant-Hom invariance forces a one-type', 'absent', '',
    'The package does not quantify a constant-to-constant localization Hom functor over all small shapes. No factorization through Π1 or represented-space one-type conclusion is present.', V+IX,
    ['constant', 'invariant', 'groupo'], ['PATHS', 'CATHOT E.17'])

add('PATHS E.1', 'All-arrow endpoints and path spaces', 'absent', '',
    'No all-type endpoint fibre, even translation, or constant-tail comparison is defined. The general homotopy integration agenda is insufficient to identify the checked CATHOT theorem here.', VIIC,
    ['extrémit', 'origine', 'chemins'], ['PATHS'])
add('PATHS E.2', 'Strict categorical loop monoid with A∞ realization', 'precursor', 'pointed',
    'The group-object question is a thematic precursor to categorical loop models. It supplies no all-type construction, strict monoidal product, or comparison with loop-space A∞ multiplication.', VIIC+IX,
    ['lacet', 'monoïd', 'composition'], ['PATHS'])
add('PATHS E.3', 'All-type endpoints smooth, not necessarily proper or fibrations', 'absent', '',
    'No all-type endpoint functor or [1] lifting counterexample occurs. The term “subm” on the MU-fibré page is used in a different construction and cannot be identified with this smoothness theorem.', VIIC,
    ['lisse', 'propre', 'chemins'], ['PATHS'])
add('PATHS E.4', 'Eventual endpoints smooth and proper, without strict lifting', 'absent', '',
    'There is no eventual alternating path construction or filtered-union lifting argument. Consequently the distinction between smooth/proper and strict Grothendieck lifting is not proved on a scan here.', VIIC,
    ['filtr', 'lisse', 'fibr'], ['PATHS'])
add('PATHS E.5', 'Natural mapping-path factorization', 'precursor', 'fibration pullback',
    'Cote 108 asks about categorical fibrations and pullback preservation of weak equivalences. It gives no natural mapping-path factorization or identification of strict and homotopy fibres.', ['context/companion/chunks/DER_XIIc-a.tex'],
    ['chemins', 'factoris', 'fibre'], ['PATHS', 'GALOIS B.7'])
add('PATHS E.6', 'Rectangular-band monoid defeats strict path lifting', 'absent', '',
    'The five-element rectangular-band monoid and its eventual/all-type endpoint maps are absent. No calculation of their failed fibration or opfibration lifting occurs.', VIIC+VI,
    ['monoïd', 'fibr', 'chemins'], ['PATHS', 'RESIDUE A.8', 'BISITE B.21'])
add('PATHS E.7', 'Interval pushout-products are weak but not intrinsic cofibrations', 'absent', '',
    'No interval pushout-product or intrinsic-cofibration obstruction appears. The supplied return is not a consequence stated in the dossier’s model-category question.', ['context/companion/chunks/DER_XIIc-b.tex']+XII,
    ['cofibr', 'intervalle', 'produit'], ['PATHS', 'POLES H.5'])
add('PATHS E.8', 'Interval cotensors: constant-section equivalence but wrong exact fibres', 'absent', '',
    'The package gives no finite-interval cotensor or endpoint-fibre calculation. Ordinary duality of presheaves/copresheaves in cote 115 is not this homotopy-theoretic dual interval assertion.', VIIC,
    ['intervalle', 'constant', 'fibre'], ['PATHS'])
add('PATHS E.9', 'W∞ smooth/proper need not preserve a larger localizer', 'precursor', 'pullback',
    'The agenda’s preservation condition names a selected W and is not a theorem simultaneously for all localizers. It contains no larger-localizer counterexample, so the return’s qualification remains additional information.', XVI+VIIC,
    ['localisateur', 'fibr', 'changement de base'], ['PATHS', 'GALOIS B.7'])
add('PATHS E.10', 'Marked components do not determine a sufficient exit stratification', 'absent', '',
    'No stratification by components of a marked subcategory or general exit-path localization claim is made. The correspondence kernel of cote 115 does not by itself specify strata or exit links.', XII+IX,
    ['stratif', 'composantes', 'localis'], ['PATHS', 'STRATA B.2', 'STRATA F.3'])
add('PATHS E.11', 'Open alternative strict bifibration over the rectangular-band monoid', 'absent', '',
    'The package gives neither the monoid nor an alternative strict bifibration, so it does not settle this open existence problem. RESULTS_STATE RESIDUE A.8 and BISITE B.21 preserve the same unresolved target.', VI,
    ['bifibr', 'monoïd', 'adjoint'], ['PATHS', 'RESIDUE A.8', 'BISITE B.21'])
add('PATHS E.12', 'Contractible fixed-origin paths need not be filtered or total', 'different', 'psproduct',
    'No fixed-origin all-type path category occurs, and totality in the quoted Proposition 4 is the earlier product/diagonal notion. The later universal-totality/path assertion and its simply connected finality clause therefore cannot be read into this proposition.', XII+VIIC,
    ['origine', 'simplement connexe', 'filtr'], ['PATHS', 'TOTASPH C.10', 'POLES H.2'])
add('PATHS E.13', 'Finite set-valued tests do not faithfully detect all maps', 'absent', '',
    'No finitary symmetric-group shift or finite restricted-Yoneda counterexample is given. The finite-condition agenda and ordinary Yoneda discussions in the dossier do not supply the specified failure of faithfulness in Hot.', VIIC+V,
    ['fidèle', 'fini', 'symétr'], ['PATHS', 'S2COUNT'])

records = []
for ln, c in rows('context/NEW_RESULTS.md', r'^\| \d+ \|'):
    num, statement, proof, author, checked, bears = c
    id = 'NEW_RESULTS #' + num
    rec = dict(id=id, table='NEW_RESULTS', source_file='context/NEW_RESULTS.md', source_line=ln,
               supplied_statement=statement, original_source_locator=proof,
               supplied_author_credit=author, supplied_review_status=checked,
               supplied_manuscript_locator=bears)
    rec.update(M[id])
    records.append(rec)
for ln, c in rows('context/DOSSIER_STATEMENTS_WITH_STATUS.md', r'^\| (?:STRATA|PATHS) '):
    id, statement, status, loc = c
    rec = dict(id=id, table=id.split()[0], source_file='context/DOSSIER_STATEMENTS_WITH_STATUS.md', source_line=ln,
               supplied_statement=statement, original_source_locator=loc,
               supplied_review_status=status,
               supplied_review_caveat='Every row is the return’s claim; none of these returns has had a review at full effort, per the dossier header.')
    rec.update(M[id])
    records.append(rec)

assert len(records) == 98, len(records)
assert set(M) == {r['id'] for r in records}
assert len({r['id'] for r in records}) == 98

def anchor_record(key):
    cote, scan, quote, loc = ANCHORS[key]
    return dict(key=key, cote=cote, scan=scan,
                page_file=f'deliverable/pages/MPL_108+112+113+114+115_{cote}_scan{scan:03}.tex',
                location=loc, quote_diplomatic_tex=quote, deletion_warning=('cancelled passage' if key=='mu' else None))

def keyword_hits(path, terms, max_hits=3):
    lines = (ROOT/path).read_text().splitlines()
    hits = []
    last_msp = None
    # Actual searches are scoped to these supplied context files; Hua material is
    # deliberately not searched or used, so no borrowed modernized reading enters.
    for n, line in enumerate(lines, 1):
        m = re.search(r'\\msp\{([^}]+)\}', line)
        if m:
            last_msp = m.group(1)
        matched = [t for t in terms if t.casefold() in line.casefold()]
        if matched:
            hits.append(dict(file=path, line=n, nearest_preceding_manuscript_marker=last_msp,
                             matched_terms=matched, text=line[:950]))
            if len(hits) >= max_hits:
                break
    return hits

for rec in records:
    rec['manuscript_evidence'] = [anchor_record(k) for k in rec['anchor_keys']]
    rec['context_searches'] = [dict(file=p, terms=rec['search_terms'], hits=keyword_hits(p, rec['search_terms']))
                               for p in rec['companion_search_files']]
    rec['state_reference_scope'] = ('Supplied register IDs are cross-references with their own status, not independent validation or a manuscript attribution.')

chronology = [
    dict(id='CHRONO W7', kind='reading question', answer='Absent from the frozen 40-scan package',
         note='No strong W(7), W(7 bis), sieve-cover biconditional, or reverse cube-gluing axiom is stated in these five cotes. Item 12 of cote 108 scan004 is a Cartesian pullback-preservation proposal for a fibration, and item 1 of scan003 is a Čech-asphericity question; neither supplies reverse gluing. In the supplied later companion, DER_XIIb-a.tex places W(7 bis) at XII manuscript pages 75–76, W(7) at 76–77, and Theorem 2 claiming it for W∞ at 78; NEW_RESULTS #8 records the checked counterexample claim. This establishes no occurrence in the package and only the displayed later locators, not the first occurrence anywhere in the archive.',
         context_files=['context/companion/chunks/DER_XIIb-a.tex'],
         state_refs=['TOTASPH A.9', 'POLES B.2'], manuscript_evidence=[anchor_record('pullback')]),
    dict(id='CHRONO TOTAL-FILTERED', kind='reading question', answer='Absent from the frozen 40-scan package',
         note='There is no assertion that a totally aspherical category is filtered; the only filtered-colimit wording in the frozen transcript is part of the ordinary abelian-category hypotheses in cote 113 scan004. The earliest related agenda question in scan order is 108 scan004 item 13, followed by 114 scan003 and the product criterion on 114 scan004, and none mentions filteredness. In supplied DER_II-a.tex the question already appears at manuscript page 36 (“cela implique-t-il que $X$ soit filtrante ?”), before the displayed conjecture at 36ter; the intervening attempted Δ opposite example is withdrawn. Cite NEW_RESULTS #11, TOTASPH C.10 and PRETOT A.12 for the supplied later Δinj counterexample, without treating either its proof or any historical first occurrence as established by these scans.',
         context_files=['context/companion/chunks/DER_II-a.tex', 'context/companion/chunks/DER_XIIb-a.tex'],
         state_refs=['TOTASPH C.10', 'PRETOT A.12', 'TOTASPH A.7', 'TOTEX2 D.4'], manuscript_evidence=[anchor_record('connected'), anchor_record('psproduct')]),
    dict(id='DEFINITION TOTALITY', kind='reading question', answer='The two meanings must be separated',
         note='Cote 114 scan004 is a printed PS draft numbered 350, with its own Proposition 4, the explicit hypothesis that W satisfies Loc 4, and a criterion in terms of 0-connected products of representables; its statement is not identified with the retained book text. In contrast, the supplied DER_XIIb-a.tex defines totality at XII manuscript pages 88–89 by all outgoing functors and ordinary left Kan extensions/final images, and its editorial note says “Cette notion est différente de la notion de totale asphéricité de Pursuing Stacks”. Thus STRATA G.2, PATHS A.5–A.7, and NEW_RESULTS #11 cannot be called present merely because the earlier page uses the same adjective. RESULTS_STATE’s older open TOTASPH D.7/RESIDUE F.5, later totality/exactness programme and TOTEX2 completion headline are different status layers; the selected TOTEX2 D.4 is a variance correction, not a supplied proof of the exactness classification.',
         context_files=['context/companion/chunks/DER_XIIb-a.tex', 'context/notes/RESULTS_STATE.md'],
         state_refs=['POLES H.2', 'TOTASPH A.2', 'TOTASPH D.7', 'TOTEX2 D.4'], manuscript_evidence=[anchor_record('psproduct')]),
]

known = [
    dict(id='NEW_RESULTS known-after-all 1', title='Isbell–Mitchell 1973, Theorem 3',
         supplied_notice='Isbell–Mitchell 1973, Theorem 3 (aff Δ filtered; item 11)',
         relation='absent', note='The notice credits the affine filteredness input used for NEW_RESULTS #11; neither it nor Δinj appears in these scans. The passage at 114 scan004 uses the earlier product notion of totality, so this known result must not be projected back onto it.',
         original_source_locator='context/NEW_RESULTS.md, final known-after-all notice; Isbell–Mitchell 1973, Theorem 3',
         context_files=II, state_refs=['TOTASPH C.10', 'PRETOT A.12']),
    dict(id='NEW_RESULTS known-after-all 2', title='Uniqueness in Nielsen realization',
         supplied_notice='uniqueness in Nielsen realization (Harvey 1971; found again by the La Longue Marche expert)',
         relation='absent', note='No Nielsen realization or its uniqueness problem occurs in the frozen dossier. Preserve Harvey 1971 as the supplied notice’s bibliographic credit; the notice is not independently verified in this comparison.',
         original_source_locator='context/NEW_RESULTS.md, final known-after-all notice; Harvey 1971',
         context_files=IX, state_refs=[]),
    dict(id='NEW_RESULTS known-after-all 3', title='Special localizers and accessibility',
         supplied_notice='“localiseur spécial” = accessible fundamental localizer follows from Cisinski, Astérisque 308, Cor. 4.2.22',
         relation='precursor', note='The only relevant programme-level precursor is the Cat model-category question in cote 108 scan003; the phrase localiseur spécial and an accessibility characterization are absent. Keep the exact Cisinski locator as supplied bibliographic credit rather than a theorem of the dossier.',
         original_source_locator='context/NEW_RESULTS.md, final known-after-all notice; Cisinski, Astérisque 308, Cor. 4.2.22',
         context_files=XVI, state_refs=['GALOIS B.4'], manuscript_evidence=[anchor_record('model')]),
]
for k in known:
    k['supplied_review_status'] = 'Supplied known-after-all notice; not independently verified in this comparison.'

meta = dict(
    scope='Research-only comparison after freeze; no scans opened and no page or combined transcription modified by this task.',
    required_context_read=['context/README.md (entire)', 'context/notes/RESULTS_STATE.md (entire)'],
    freeze_utc='2026-11-17 19:31:09 UTC', context_opened_utc='2026-11-17 19:31:17 UTC',
    transcription=str(TRANSCRIPT.relative_to(ROOT)), frozen_sha256=FROZEN_SHA,
    covered_ids=[r['id'] for r in records], counts=dict(NEW_RESULTS=12, STRATA=10, PATHS=76, numbered_total=98, known_after_all_notices=3),
    relation_definitions=dict(present='The supplied exact claim is explicitly stated here; not a proof verdict.',
                             precursor='Only a narrower or programme-level idea is actually present; the row’s theorem remains absent.',
                             absent='No statement or specific construction corresponding to the exact supplied row was found.',
                             different='A tempting verbal/formal resemblance has different hypotheses, variance, construction or meaning.'),
    no_hua_use='No hua_project modernized reading was used or searched by this task. No claim of independent priority is made.',
    status_boundary='Dossier statuses and NEW_RESULTS review/credit columns are copied literally. Register headlines and older selected open rows are not silently reconciled. No settled claim is re-proved.',
    evidence_boundary='The frozen transcription is the only source of quotes from these five cotes; braces, deletion and uncertainty macros are retained. Absent rows receive no scan or invented quotation.',
    source_boundary='Companion files are supplied context, not independently verified manuscript readings; keyword hit markers are locators for comparison only. External return proof paths cited by the source tables are generally not included in this package.',
)

payload = dict(metadata=meta, chronology=chronology, results=records, known_after_all=known)
(OUT/'research_new_strata_paths.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
(OUT/'research_new_strata_paths_covered_ids.json').write_text(json.dumps(meta['covered_ids'], ensure_ascii=False, indent=2)+'\n')

def mdcell(x):
    return str(x).replace('|', '&#124;').replace('\n', ' ')

def manuscript_md(rec):
    result=[]
    for a in rec.get('manuscript_evidence', []):
        warn = '; cancelled' if a.get('deletion_warning') else ''
        result.append(f"cote {a['cote']} scan{a['scan']:03} ({a['location']}{warn}): `{a['quote_diplomatic_tex']}`")
    return '; '.join(result)

parts = [
    '# Research draft: NEW_RESULTS, STRATA, PATHS — all exact IDs',
    '',
    '**Kind:** reading-question audit. **Coverage:** 12 numbered NEW_RESULTS results, all 10 STRATA and all 76 PATHS rows (98 exact IDs), plus the three known-after-all notices. The accompanying JSON preserves every full source statement, original locator, literal supplied status/review and credit, and per-ID context search records.',
    '',
    '## Method and status boundary',
    '',
    'The transcription was frozen at 2026-11-17 19:31:09 UTC; context opened at 19:31:17 UTC. This task read `context/README.md` and `context/notes/RESULTS_STATE.md` in full before drafting, and used the frozen combined transcription and its page files only as text. It did not open scans, audit readings, or edit the transcription. The combined SHA-256 remained `'+FROZEN_SHA+'`.',
    '',
    'Every STRATA/PATHS status below remains **the return’s claim**, as required by the header of `context/DOSSIER_STATEMENTS_WITH_STATUS.md`; the supplied header says those returns have no full-effort review. The distinct NEW_RESULTS review history is retained separately. “Precursor” does not mean the exact modern result is proved or stated: it marks only the narrower idea quoted from the page. “Different” flags a tempting but invalid identification. An absent row has no manuscript scan or quotation assigned to it.',
    '',
    'Source paths in the “original source” column are copied from the supplied tables and are not claims that those external return files are present in this package. The comparison-text column names the actual supplied companion file(s) searched; exact manuscript-page locators remain those of the source table. `RESULTS_STATE` IDs are cited as contextual cross-references with their own dates/status, never promoted to a manuscript proof. No Hua modernized reading was used; no outside literature was independently checked for these comparisons.',
    '',
    '## Earliest-occurrence questions and the two meanings of totality',
    '',
]
for c in chronology:
    parts.extend([f"### {c['id']} — {c['answer']}", '', c['note'], '',
                  '**Frozen-page evidence:** '+manuscript_md(c), '',
                  '**Supplied context:** '+', '.join('`'+f+'`' for f in c['context_files'])+'; `RESULTS_STATE` '+', '.join(c['state_refs'])+'.', ''])

parts += ['## NEW_RESULTS: every numbered result', '',
          '| Exact ID and claim | Supplied review/credit | Original proof and manuscript locator | Comparison with the frozen package |',
          '|---|---|---|---|']
for r in records:
    if r['table'] != 'NEW_RESULTS': continue
    credit = r['supplied_review_status']+' **Credit:** '+r['supplied_author_credit']
    source = r['original_source_locator']+' **Bears on:** '+r['supplied_manuscript_locator']
    compare = '**'+r['relation']+'.** '+r['note']
    if r['manuscript_evidence']: compare += ' **Page:** '+manuscript_md(r)+'.'
    compare += ' **Context searched:** '+', '.join('`'+p+'`' for p in r['companion_search_files'])+'.'
    if r['state_refs']: compare += ' **RESULTS_STATE:** '+', '.join(r['state_refs'])+'.'
    parts.append('| '+ ' | '.join(map(mdcell,[r['id']+' — '+r['title'], credit, source, compare]))+' |')

parts += ['', '### Known-after-all notices', '',
          '| Exact notice ID | Supplied source and status | Comparison |', '|---|---|---|']
for k in known:
    compare = '**'+k['relation']+'.** '+k['note']
    if k.get('manuscript_evidence'): compare += ' **Page:** '+manuscript_md(k)+'.'
    if k['state_refs']: compare += ' **RESULTS_STATE:** '+', '.join(k['state_refs'])+'.'
    parts.append('| '+' | '.join(map(mdcell,[k['id']+' — '+k['title'], k['original_source_locator']+'; '+k['supplied_review_status'], compare]))+' |')

for group in ['STRATA','PATHS']:
    parts += ['', '## '+group+': every supplied row', '',
              '| Exact ID and claim | Supplied status | Original source locator | Comparison with frozen pages and supplied context |',
              '|---|---|---|---|']
    for r in records:
        if r['table'] != group: continue
        compare='**'+r['relation']+'.** '+r['note']
        if r['manuscript_evidence']: compare+=' **Page:** '+manuscript_md(r)+'.'
        compare += ' **Context searched:** '+', '.join('`'+p+'`' for p in r['companion_search_files'])+'.'
        if r['state_refs']: compare += ' **RESULTS_STATE:** '+', '.join(r['state_refs'])+'.'
        parts.append('| '+' | '.join(map(mdcell,[r['id']+' — '+r['title'], r['supplied_review_status'], r['original_source_locator'], compare]))+' |')

parts += ['', '## Gaps and limits', '',
          '- The exact source statements and review/author columns are fully preserved in `research_new_strata_paths.json`; the Markdown claim labels are compact summaries. Coverage is independently listed in `research_new_strata_paths_covered_ids.json`.',
          '- These pages contain programme questions and several cancelled constructions. A real precursor is not evidence for all later hypotheses, a universal quantifier, coherence, variance, a counterexample, or a computational count.',
          '- Cote 114 scan004 is a printed PS draft numbered 350, whose Proposition 4 must be distinguished from the retained book text. The supplied `ps7.tex` begins the much later Abelianization II chapter (printed p.555); it is not a textual witness for this draft leaf. The exact manuscript source here remains the frozen scan004 transcription; the parent research task separately checks the retained text.',
          '- The only exact filtered-colimit wording in this package is cote 113 scan004’s abelian-category hypothesis. Neither strong W(7) nor total-aspherical ⇒ filtered has an occurrence here. The later companion locators are not a claim of historical first occurrence across the entire archive.',
          '- Source-version tensions are preserved: CATHOT E.17/E.26 and TOTASPH D.7 may remain in an older open-items selection while later returns/headlines state additional results. The underlying later full proof returns are not part of the supplied files, so aggregate counts are not used to certify a particular theorem.',
          '- The no-match judgments are based on the complete frozen text plus per-ID thematic searches in the supplied companion context. A keyword hit is recorded with its preceding manuscript-page marker in JSON, but is not itself promoted to a mathematical correspondence.',
          '']
(OUT/'research_new_strata_paths.md').write_text('\n'.join(parts))
assert hashlib.sha256(TRANSCRIPT.read_bytes()).hexdigest() == FROZEN_SHA
print(json.dumps({'covered':len(records),'counts':meta['counts'],'relations':{k:sum(r['relation']==k for r in records) for k in ['present','precursor','absent','different']},'files':['research_new_strata_paths.md','research_new_strata_paths.json','research_new_strata_paths_covered_ids.json'],'sha256_unchanged':True},ensure_ascii=False))
