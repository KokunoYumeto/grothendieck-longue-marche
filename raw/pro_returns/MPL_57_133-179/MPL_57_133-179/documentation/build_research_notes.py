#!/usr/bin/env python3
"""Assemble post-freeze research notes; never reads or writes scan images or TeX."""
from pathlib import Path
import json, re, subprocess, csv

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
notes = []

def add(section, ident, title, where, kind, quote, rs, search, comparison, sentences, confidence=None, event='documentary'):
    assert 1 <= len(sentences) <= 4, (ident, len(sentences))
    notes.append(dict(section=section, id=ident, title=title, where=where, kind=kind,
                      quote=quote, rs=rs, search=search, comparison=comparison,
                      sentences=sentences, confidence=confidence, event=event))

BROAD = ['WG2 §1.1 #3']
CARRY = ['WG2 §2.4 #4', 'WG2 §1.1 #3']

add('Picard kernels, descent, and curve obstructions', 'P01', 'Representability is admitted in the affine-kernel argument',
    '57:133 L5–22; 135 L6–22', 'unproved claim',
    '« admettre que tous les ... Pic ... sont représentables »; « on peut sans doute s’en passer ! »',
    BROAD, ['noyau', 'représentables', 'Stein', 'Seshadri'],
    'HUA, “Le noyau pour un morphisme surjectif (pages 132 et 134)”, L1707–1728, restates the reduction; CT 44:2 Th. 1 and CN D08 concern a different Albanese-to-cycle quotient.',
    [r'The proposed proof reduces through the reduced subschemes and Stein factorization, but assumes representability for every intermediate Picard object and invokes a finite-surjective descent result under an uncertain attribution.',
     r'The final monomorphism argument is itself qualified by the margin on non-finite-type groups, so this selection does not supply a finished proof independent of representability.',
     r'Hua’s modernization is a useful map of the intended reduction; its stronger reformulation is not substituted for the frozen theorem or used to settle the separate cote 44 kernel construction.'])

add('Picard kernels, descent, and curve obstructions', 'P02', 'The non-quasi-compact monomorphism warning has a concrete model',
    '57:135 L18–20', 'own idea', '« un mono n’est donc pas ... affine [ex. Z → G] »',
    BROAD, ['monomorphisme', 'type fini', 'quasi-affine', 'noyau'],
    'HUA, “Le noyau pour un morphisme surjectif”, L1707–1728, stops at the monomorphism step without reproducing the nonfinite-type warning; CT 44:2’s kernel has a different meaning.',
    [r'Over a characteristic-zero field, the map from the constant scheme \(\mathbf Z_k=\coprod_{n\in\mathbf Z}\operatorname{Spec}k\) to \(\mathbf G_a\), taking \(n\) to its image in \(k\), is a monomorphism: different integers remain distinct after every base change.',
     r'It is not affine, because its inverse image of the affine target is the non-quasi-compact scheme \(\mathbf Z_k\).',
     r'This verifies the manuscript’s objection to the unrestricted inference from monomorphism to affine morphism, without refuting the Picard-kernel theorem itself.'],
    'high: the diagonal/fibre-product test and failure of quasi-compactness give an explicit example', 'proof')

add('Picard kernels, descent, and curve obstructions', 'P03', 'The rigidifying tensor factor needs an inverse',
    '57:138 L16–20; compare 175 L7–11', 'own idea',
    r'« savoir \(L\otimes\varphi^*(g^*(L))\) »', BROAD,
    ['rigidifié', 'inverse', 'L^{-1}', 'Leray'],
    'HUA, “Pic relatif et suite de Leray (pages 137 à 139)”, L1739–1743, explicitly adds the inverse and notes its absence in the page; CT 47:3 supplies the related rigidified-kernel context.',
    [r'The frozen expression has no inverse, so with \(X=\Sigma=S=\mathbf P^1_k\), \(\varphi=g=\mathrm{id}\), and \(L=\mathcal O(1)\), it gives \(\mathcal O(2)\), which cannot be rigidified along the identity section.',
     r'The corrected construction is \(L\otimes\varphi^*(g^*L)^{-1}\), whose restriction to \(g\) is canonically trivial.',
     r'This independently checks the correction credited to Hua and the inverse appearing at 57:175; it is a research correction only, and the frozen insertion at 57:138 remains unchanged.'],
    'high: restriction to the section and the degree-two example test the exact displayed formula', 'proof')

add('Picard kernels, descent, and curve obstructions', 'P04', 'The Stein-factor version and the later descent version share a mechanism',
    '57:138 L3–22; 140 L3–25; 175 L16–177 L7', 'unpursued implication',
    '« le théorème de descente connu et le raisonnement connu »', BROAD,
    ['Stein', 'descente', 'localement', 'section'],
    'HUA, “Pic relatif et suite de Leray”, L1730–1749, and “Le foncteur de Picard”, L1970–1990, restate the two versions; CT 47:3 uses rigidified line bundles.',
    [r'The earlier block uses the finite Stein factor \(\Sigma\) to identify the ambiguity in a line bundle with pullback from \(\Sigma\), whereas the later block assumes the universal equality \(f_*\mathcal O_X=\mathcal O_S\).',
     r'Both arguments use a local section to rigidify and then descend uniquely, but their quotient groups have different bases until \(\Sigma=S\) has been justified.',
     r'This is an internal parallel rather than a reason to replace \(\operatorname{Pic}(\Sigma)\) by \(\operatorname{Pic}(S)\) in the earlier sheets.'])

add('Picard kernels, descent, and curve obstructions', 'P05', 'A possible proof of the Kummer comparison must compare cocycles',
    '57:142 L27–40; 144 L17–32', 'own idea', '« ξ_n=δ_n(η) »; « à vérifier ...... »',
    CARRY + ['LM7 E.23', 'LM6 E.21'], ['Kummer', 'torseur', 'compatibilité', 'ξ_n'],
    'HUA, “Une obstruction pour une courbe épointée”, L1753–1783, preserves the unfinished identity; CT 16:21 has a Kummer sequence, while CT 47:7–8 is the distinct Fourier comparison.',
    [r'A useful next check is to choose local degree-one line bundles on the pinched curve, lift their transition translations through multiplication by \(n\), and compare the resulting Čech two-cocycle with the transgression of the fibrewise compact-support fundamental class.',
     r'That comparison must retain the convention for the connecting map and the trace generator, since an equality of target groups alone does not determine a sign or the actual class.',
     r'This is a proposed method, not a completed verification; the abelian-layer connection to LM7 E.23 and LM6 E.21 leaves their full section-class problems open.'],
    'medium: the two constructions have the right obstruction degree, but their cocycle identification and sign have not been proved here', 'proposal')

add('Picard kernels, descent, and curve obstructions', 'P06', 'Passing from finite Kummer classes to a Tate-module class needs a cohomology convention',
    '57:142 L33–40', 'unproved claim', '« on trouve ... ξ(ℓ)∈H²(S,T_ℓ(E)) »',
    BROAD + ['LM7 E.23', 'LM6 E.21'], ['Tate', 'lim', 'Kummer', 'T_\\ell'],
    'CT 16:21 and CN’s Kummer discussion distinguish finite torsion from inverse-limit data; SN D09 and C09 are first-pass cautions; Jannsen (1988), Proposition 1.6, supplies the continuous-cohomology comparison.',
    [r'The page passes from the finite-level classes to a class with Tate-module coefficients without specifying whether cohomology is continuous or is defined directly by an inverse limit.',
     r'A completion of the argument should check transition compatibility and the relevant derived-limit term, rather than identify \(H^2(S,\varprojlim E[\ell^\nu])\) with \(\varprojlim H^2(S,E[\ell^\nu])\) without hypotheses.',
     r'This is a qualification of the stated passage, not a claim that the class cannot be defined or that the registered section problems are solved.'])

add('Picard kernels, descent, and curve obstructions', 'P07', 'One and two punctures provide control cases for the torus',
    '57:142 L42–46; 145 L9–33', 'own idea', '« G_m^I/G_m »; « par diagonale »',
    BROAD + ['MPL_57_271-315 C04'], ['unités', 'diagonale', 'pinching', 'généralisé'],
    'SN C04 and I03, reporting 57:304, isolate the same unit quotient and are leads only; HUA, “Une obstruction pour une courbe épointée”, restates the present torus sequence.',
    [r'For one marked section the diagonal quotient is trivial, while for two labelled disjoint sections the ratio \((u,v)\mapsto u/v\) identifies it with \(\mathbf G_m\).',
     r'Accordingly the split two-section case gives \(H^1(S,T)\simeq\operatorname{Pic}(S)\), and the identification depends on the order or ratio convention.',
     r'This checks a concrete unit contribution and adds a control case to the pinching mechanism reported in SN C04, without independently checking that earlier package’s source pages.'],
    'high: the kernel and cokernel of the diagonal map are computed directly', 'proof')

add('Picard kernels, descent, and curve obstructions', 'P08', 'The last vanishing statement retains the preceding splitting assumptions',
    '57:145 L3–33', 'unproved claim', '« Si p. ex. Pic(S)=0, on trouve η=0 »',
    BROAD + ['MPL_57_271-315 C04'], ['Pic(S)', 'section', 'Br', 'torseur'],
    'HUA, “Une obstruction pour une courbe épointée”, L1778–1783, condenses this chain; SN C04 and README’s B11 lead also warn about the unit term.',
    [r'The conclusion follows along the page’s chain after the image of \(\eta\) in \(H^1(S,J)\) is zero and the boundary is a disjoint union of sections, so the relevant torus cohomology is the displayed quotient of copies of \(\operatorname{Pic}(S)\).',
     r'It should not be extracted as a theorem that \(\operatorname{Pic}(S)=0\) alone kills \(\eta\) for arbitrary finite étale \(Y\) or arbitrary \(\operatorname{Pic}^1_{X/S}\).',
     r'The final assertion about the \(\xi_n\) still uses the comparison explicitly left unverified on the preceding page.'])

add('Picard kernels, descent, and curve obstructions', 'P09', 'Vanishing is not a converse section criterion',
    '57:142 L40; 145 L25–33', 'own idea', '« Cet élément est nul si U a une section sur S »',
    BROAD + ['LM7 E.23', 'LM6 E.21'], ['section', 'obstruction', 'Kummer', 'courbe épointée'],
    'HUA, “Une obstruction pour une courbe épointée”, follows the same one-way assertion; RS LM7 E.23 and LM6 E.21 remain open classification problems.',
    [r'Take \(S=\operatorname{Spec}\mathbf F_2\), \(X=\mathbf P^1\), and \(Y=\{0,1,\infty\}\): the boundary consists of three sections and \(\operatorname{Pic}(S)=0\), but \(U(S)=\varnothing\).',
     r'Thus even under the manuscript’s vanishing conclusions, the converse implication from a vanishing class to an actual section of \(U\) cannot be inferred.',
     r'This finite example tests the logical converse only and does not verify the manuscript’s comparison of the two obstruction constructions.'],
    'high: the three rational points exhaust the projective line over the two-element field', 'proof')

add('Picard kernels, descent, and curve obstructions', 'P10', 'The arithmetic bridge is semiabelian and retains the unit term',
    '57:142 L42–46; 144 L7–15; 145 L9–16', 'unpursued implication', '« extension de J ... par T »',
    BROAD + ['ANABELIAN_149_PUSH A.1', 'SECTIONS_OVER_Q A.198', 'MPL_57_271-315 C04'],
    ['semiabelian', 'généralisé', 'norm-one', 'B11', 'unités'],
    'README’s B11 correction, RS ANABELIAN_149_PUSH A.1 and SECTIONS_OVER_Q A.198, and SN C04/I03 give the related arithmetic leads; none is reproved here.',
    [r'The current source explicitly exhibits the toric part of a generalized Jacobian and the quotient of boundary units, providing a geometric mechanism relevant to the registered Kummer-kernel and norm-one-frame results.',
     r'The README’s warning against treating all rational points of a semiabelian variety as a finitely generated Mordell–Weil group remains essential when transferring the construction to arithmetic.',
     r'The two registered results are carried at their stated “Proved (the return’s claim)” status, while the present sheets add the pinching/torsor context and no new proof of those results.'])

add('Picard kernels, descent, and curve obstructions', 'P11', 'Three obstruction constructions require explicit comparison',
    '57:144 L17–32; 145 L9–16; 174 L5–14; 179 L5', 'unpursued implication',
    '« H²(S,{}_nE) »; « Br′(S) »; « H²(S,G_m) »',
    BROAD + ['CYCLOTOMIC_KERNEL C1', 'LM6 F.43'], ['Kummer', 'Brauer', 'normal lines', 'H^2'],
    'CT 16:21 and 47:3 provide Kummer/rigidification comparators; RS CYCLOTOMIC_KERNEL C1 is an H¹ splitting torsor and LM6 F.43 concerns normal-line torus data.',
    [r'The transgression/Kummer class lies in \(H^2(S,E[n])\), the failure to lift a torus class through the boundary-unit sequence lands in a Brauer-type \(H^2(S,\mathbf G_m)\), and realizing a relative Picard class as a line bundle has its own \(\mathbf G_m\)-obstruction.',
     r'The normal-line and cusp-Kummer entries suggest comparisons of their input torsors, but the pages do not identify these constructions or their classes; the two Brauer-type constructions may have the same target group on the same site.',
     r'In particular the H¹ torsor in CYCLOTOMIC_KERNEL C1 is not the H² class on this sheet, and no nonabelian conclusion is extracted from the similarity of their Kummer vocabulary.'])

add('Singular curves and dimension calculations', 'C01', 'Normalization separates toric rank from the additive contribution',
    '57:147 L3–32; 149 L3–21; 151 L27–38', 'unpursued implication',
    '« branches formelles ... diminué de 1 »; « g=...+ρ+σ »',
    BROAD + ['MPL_57_271-315 C04'], ['normalisée', 'branches', 'rang torique', 'multiplicative'],
    'HUA, “Le Picard d’une courbe réduite (pages 146 à 150)”, L1785–1833, writes the same decomposition in changed notation; SN C04 gives another pinching lead at 57:304.',
    [r'With editorial notation \(d_P=\operatorname{length}(\nu_*\mathcal O_{\widetilde C}/\mathcal O_C)_P\) and \(r_P\) the number of branches, the source’s live calculation separates \(\dim G=\sum d_P-c_0+1\), toric rank \(\sum(r_P-1)-c_0+1\), and unipotent dimension \(\sum(d_P-r_P+1)\).',
     r'The incidence graph must include normalization branches, including self-identifications on a component, as the warning at 57:149 already recognizes.',
     r'These formulas explain the mechanism relevant to the earlier pinching lead; the editorial letters avoid silently equating the manuscript’s changing \(\mu,\mu^{\prime},\delta\) conventions.'])

add('Singular curves and dimension calculations', 'C02', 'A node, a cusp, and a triple point test different invariants',
    '57:149 L6–23; 151 L23–25; 155 L5–17', 'own idea',
    '« multiplicatifs »; « n’a pas de composante additive »', BROAD,
    ['triédraux', 'axes', 'additive', 'courbe réduite'],
    'HUA, “Le Picard d’une courbe réduite”, L1822–1833, interprets the singularities using coordinate axes; SN C04 is a related unit-quotient lead.',
    [r'In characteristic zero, an ordinary node has \((d,r)=(1,2)\), a cusp has \((1,1)\), and an ordinary planar triple point has \((3,3)\), so their additive dimensions are respectively \(0,1,1\).',
     r'The planar triple point therefore differs from three coordinate axes in three-space, whose normalization quotient has length two and no additive contribution.',
     r'This guards the meaning of “multiplicatif”: merely counting distinct tangent directions in a plane is not enough to obtain the coordinate-axis gluing used in Hua’s explanation.'],
    'high: node/cusp normalization quotients and the triple-point normalization quotient give the displayed lengths', 'proof')

add('Singular curves and dimension calculations', 'C03', 'A tree condition alone does not make the Picard identity component proper',
    '57:151 L16–25; 155 L3–17', 'own idea', '« on ne peut avoir de cycles »; « Pic^0 ... est abélien »',
    BROAD + ['MPL_57_271-315 C04'], ['arbre', 'abélien', 'additive', 'normalisée'],
    'HUA, “Le Picard d’une courbe réduite”, L1822–1833, combines vanishing additive part with the tree condition; SN C04 accounts for the affine unit contribution.',
    [r'A rational cuspidal curve has a single normalization component and no combinatorial cycle, yet its one-dimensional additive contribution prevents \(\operatorname{Pic}^0\) from being an abelian variety.',
     r'For the reduced connected curves under discussion, the intended criterion must kill both the toric graph contribution and all additive singularity contributions.',
     r'This supports the combined reading in Hua’s account while preserving the source’s changed words and its unresolved \(\mu\)-notation at 57:155.'],
    'high: the cusp has normalization defect one and one branch, so the source’s decomposition supplies the counterexample', 'proof')

add('Singular curves and dimension calculations', 'C04', '“Additive” does not automatically mean a vector group in positive characteristic',
    '57:149 L9, L20–23; 151 L38', 'unproved claim', '« partie additive »',
    BROAD + ['ANABELIAN_149_PUSH A.1'], ['additive', 'unipotent', 'caractéristique', 'courbe réduite'],
    'HUA, “Le Picard d’une courbe réduite”, uses the same dimension split; RS ANABELIAN_149_PUSH A.1 is explicitly semiabelian and therefore excludes this unipotent contribution.',
    [r'The dimension count determines the size of the unipotent contribution, but does not identify its group law with a product of copies of \(\mathbf G_a\) in arbitrary characteristic.',
     r'Any arithmetic use of the registered semiabelian Kummer statement therefore first has to establish that the present singularity contribution is toric, not merely affine.',
     r'This is a scope boundary, and no general classification of the unipotent factors is claimed here.'])

add('Singular curves and dimension calculations', 'C05', 'A stable-graph dimension specialization can be checked without a moduli theorem',
    '57:153 L20–31; 155 L31–39', 'own idea', '« 3g_i−3+ν_i »; « 3g−2ρ−2c_0+c_1+λ−1 »',
    BROAD + ['EXIT_TOWER A.5'], ['stable', 'graphe', 'lambda', '3g'],
    'HUA, “Courbes stables (pages 152 et 154)”, L1835–1852, gives the interpretation; RS EXIT_TOWER A.5 is a separate claimed statement about strata and their factors.',
    [r'For a connected unmarked nodal graph, with \(\nu_i\) counting node preimages and \(\rho=c_1-c_0+1\), the last displayed expression simplifies to \(3g-3-c_1+\lambda\), and under stable-vertex hypotheses \(\lambda=0\), giving \(3g-3-c_1\).',
     r'This checks only the arithmetic under the stated graph conventions; the drawings and uncertain inequalities do not prove that a particular moduli stratum is smooth or a product without an automorphism quotient.',
     r'The connection to EXIT_TOWER A.5 is the component-and-marking bookkeeping, with that entry retained at its own claimed status.'],
    'high for the polynomial substitution; medium for assigning every uncertain drawing to a specific moduli stratum', 'proof')

add('Singular curves and dimension calculations', 'C06', 'The graph calculation does not determine higher section classes',
    '57:149 L13–18; 151 L30–38; 153 L49–51', 'unpursued implication',
    '« H¹_ℓ(C) »; « ρ: nbr des cycles combinatoires »',
    BROAD + ['LM7 E.23', 'LM6 E.21', 'ANABELIAN_149_PUSH B.5'],
    ['metabelian', 'class-two', 'vanishing', 'Picard', 'graphe'],
    'RS LM7 E.23 and LM6 E.21 are open section classifications; ANABELIAN_149_PUSH B.5 is a claimed degeneration/multitwist bridge, and CT 16:21 concerns abelian Kummer data.',
    [r'The source supplies a degree-one and graph contribution to the Jacobian of a singular curve, which is useful input for an abelianized degeneration calculation.',
     r'It supplies neither the noncommuting extension data of the full metabelian quotient nor the fibres of the section maps requested by LM7 E.23 and LM6 E.21.',
     r'The degeneration bridge in ANABELIAN_149_PUSH B.5 is cited without rederivation, and its thickness or inertia data should not be reconstructed from the graph-rank formula alone.'])

add('Projective classes and divisor deformation', 'D01', 'Projective trivialization forgets the scalar and can leave Brauer twisting',
    '57:158 L9–44; 160 L5–41', 'unpursued implication',
    '« bases de E modulo O_S^* »; « fibré de Brauer-Severi »', BROAD,
    ['Brauer', 'trivialisation projective', 'PGL', 'GP(N)'],
    'HUA, “Plongements projectifs et foncteur de Picard (pages 156 à 163)”, L1858–1895, recasts the same quotient; CT 47:3 gives a different rigidified line-bundle classification.',
    [r'The first equivalence keeps both a projective map and an isomorphism of its pulled-back \(\mathcal O(1)\) with \(L\), whereas the later equivalence forgets the scalar ambiguity and then allows a projective bundle twisted over the base.',
     r'This explains why a relative line-bundle class need not come with a globally chosen vector bundle of sections and a frame.',
     r'The Brauer–Severi object here is also distinct from the \(P_\xi=\operatorname{Alb}(S)/N(\xi)\) of cote 44, despite the shared subscript notation.'])

add('Projective classes and divisor deformation', 'D02', 'Freeness of a frame action is different from triviality of Aut(X)',
    '57:160 L45–50; 162 L3–10', 'own idea', '« sans pts fixes (= Aut_S(X) trivial) »',
    BROAD, ['Aut', 'sans points fixes', 'quotient', 'morphismes projectifs'],
    'HUA, “Plongements projectifs et foncteur de Picard (pages 156 à 163)”, L1885–1895, interprets a quotient by projective changes of frame; no exact CT/SN counterpart of this parenthesis was found.',
    [r'If the parenthesis is taken literally as a statement about all automorphisms of \(X\), set \(X=\mathbf P^1_k\), \(L=\mathcal O(1)\), and \(j=\mathrm{id}\): its stabilizer under postcomposition by \(\operatorname{PGL}_2\) is trivial, but \(\operatorname{Aut}_k(X)=\operatorname{PGL}_2\) is not.',
     r'The sensible condition is trivial automorphisms of the specified framed datum, or a trivial stabilizer for that action, and the precise datum must be stated.',
     r'This is a conditional check of the frozen parenthesis, whose surrounding wording is uncertain; it does not change the transcription or refute a correctly formulated free-action quotient.'],
    'high for the projective-line example; medium for what the compressed manuscript parenthesis intended', 'proof')

add('Projective classes and divisor deformation', 'D03', 'The quotient needs its representability theorem and topology',
    '57:160 L45–50; 162 L8–16', 'unproved claim', '« existe, c’est un espace »',
    BROAD, ['quotient', 'espace', 'représentable', 'Hom'],
    'HUA, “Plongements projectifs et foncteur de Picard (pages 156 à 163)”, L1885–1895, identifies the intended quotient interpretation; SN P05–P06, reporting 57:276–277, are later unreviewed quotient-existence questions.',
    [r'The source classifies principal bundles with an equivariant map into the special-morphism space and then announces the quotient as an “espace”.',
     r'A modern formulation should specify the flat sheaf quotient, the representing Hom scheme and its special locus, and the theorem that promotes the free quotient to an algebraic space.',
     r'The classification sketch is valuable input to that theorem, while the indefinite word “espace” and the nearby margin do not supply all its hypotheses.'])

add('Projective classes and divisor deformation', 'D04', 'The divisor tangent sequence comes from a specific short exact sequence',
    '57:164 L20–34', 'own idea', '« 0 ... O_X ... L ... L|Y ... 0 »',
    BROAD + ['MPL_57_271-315 D07'], ['tangent', 'Div', 'H^2', 'suite exacte'],
    'HUA, “Diviseurs et Picard : la suite tangente (page 163)”, L1897–1910, modernizes the same sequence; CT 54:3 and SN D07 discuss different tangent/Hodge extensions.',
    [r'For an effective Cartier divisor \(Y\), with \(L=\mathcal O_X(Y)\), the identity \(\mathcal I_Y\otimes L\simeq\mathcal O_X\) gives \(0\to\mathcal O_X\to L\to L|_Y\to0\), hence the connecting map \(H^0(Y,L|_Y)\to H^1(X,\mathcal O_X)\) and the next map \(H^1(Y,L|_Y)\to H^2(X,\mathcal O_X)\).',
     r'The first is the natural candidate for the differential of the divisor-to-Picard map, with kernel given by sections of \(L\) modulo sections of \(\mathcal O_X\).',
     r'This checks the formal cohomology degrees and explains the reading question in R04; it does not prove relative representability or a canonical splitting of the tangent sequence.'],
    'high for the long exact sequence; the geometric tangent interpretation requires the usual Cartier/deformation hypotheses', 'proof')

add('Projective classes and divisor deformation', 'D05', 'Universal vanishing is stronger than one fibre’s tangent count',
    '57:164 L25–34', 'unproved claim', '« son annulation universelle implique ... est lisse »',
    BROAD + ['MPL_57_271-315 D07'], ['annulation', 'lisse', 'obstruction', 'tangent'],
    'HUA, “Diviseurs et Picard : la suite tangente”, L1897–1910, offers an obstruction interpretation; SN E07/R04 and CT 54:3–7 are only comparison leads.',
    [r'The margin’s word “universelle” asks for a base-change-stable vanishing condition, not merely a numerical equality of tangent dimensions at one point.',
     r'A proof of the relative smoothness conclusion must identify the actual obstruction group for the functor, check that it vanishes under arbitrary infinitesimal base changes, and supply the relevant finiteness or representability conditions.',
     r'The frozen margins leave some labels uncertain, so neither Hua’s reconstruction nor the familiar deformation pattern settles which individual group the pointer was intended to select.'])

add('Pseudo-morphisms and normality', 'N01', 'Separatedness is what makes the maximal-domain construction unique',
    '57:166 L19–23; 167 L7', 'own idea', '« Y séparé sur S »; « un domaine (plus grand) de définition »',
    BROAD, ['séparé', 'pseudo-morphisme', 'domaine', 'rational'],
    'HUA, “Pseudo-morphismes et diviseurs (pages 165 à 170)”, L1914–1925, retains separatedness explicitly; no exact CT/SN proof of this construction was found.',
    [r'The two maps from \(\mathbf A^1\) into the affine line with doubled origin, selecting its two charts, agree on the punctured line and differ at the origin.',
     r'This shows why the previously written separatedness hypothesis must stay in force when representatives of a pseudo-morphism are glued into a unique map on their union.',
     r'For a separated target the equalizer is closed and schematic density forces equality, which supplies the gluing mechanism that the bracket on 57:166 begins.'],
    'high: the doubled-origin maps test uniqueness directly and the diagonal argument explains the retained hypothesis', 'proof')

add('Pseudo-morphisms and normality', 'N02', 'The quasi-coherence proposition is withdrawn, without a supplied verdict',
    '57:167 L9–13', 'withdrawn in the same text', '« Prop. 0.1 Ce faisceau est quasi-cohérent » [deleted]',
    BROAD, ['pseudo-fonctions', 'quasi-cohérent', 'meromorphic', 'embedded'],
    'HUA, “Pseudo-morphismes et diviseurs”, L1914–1925, omits this cancelled proposition; Stacks 0EMH and 0EMF give sufficient hypotheses for the usual meromorphic-function sheaf.',
    [r'The assertion and its attempted affine reduction are cancelled on this same sheet; cancellation alone does not determine whether the author found a false statement, changed definitions, or deferred the proof.',
     r'For the usual meromorphic-function sheaf, local noetherianity with no embedded points is a sufficient quasi-coherence hypothesis, whereas no such hypothesis appears in this current pseudo-function block.',
     r'The needed comparison is between the exact pseudo-function definition here and the usual localization sheaf before importing that theorem; Hua’s omission supplies no verdict.'])

add('Pseudo-morphisms and normality', 'N03', 'Codimension-one regularity is insufficient for the first normality relaxation',
    '57:169 L20–26; 170 L3–7', 'own idea', '« Les résultats précédents valent ... si ... singuliers ... dim ≤ n−2 »',
    BROAD + ['SECTIONS_OVER_Q B.15'], ['normal', 'singulier', 'S_2', 'pseudo-morphismes'],
    'HUA, “Pseudo-morphismes et diviseurs”, L1927–1941, already flags the missing S₂ condition using a two-point pinching example; Stacks 031S supplies the precise normality criterion.',
    [r'Let \(A=k+(x,y)^2\subset k[x,y]\), \(\mathfrak m=(x,y)^2\), and \(X=\operatorname{Spec}A\): this is a two-dimensional affine domain whose finite normalization is \(k[x,y]\), and \(A_{x^2}=k[x,y]_{x^2}\), \(A_{y^2}=k[x,y]_{y^2}\) show it is regular outside the closed origin.',
     r'The rational function \(x=x^3/x^2\) is regular at every height-one point and has no negative divisorial order, but \(x\notin A_{\mathfrak m}\), since multiplying it by an element with nonzero constant term produces a nonzero linear term.',
     r'Thus its undefined locus is the codimension-two origin, refuting the first NB’s unrestricted extension of the preceding regular-function criterion and pole-locus assertion.',
     r'The refined statement N04 keeps normality, or the noetherian R₁+S₂ condition, and the explicit ring checks Hua’s warning independently; a weaker intended statement allowing a codimension-two exception is not excluded.'],
    'high: generators, normalization, the punctured open cover, and the failed localization membership are checked explicitly in research_counterexamples_review.md', 'proof')

add('Pseudo-morphisms and normality', 'N04', 'The two normality relaxations have different corrected statements',
    '57:169 L20–26; 170 L7–19; 171 L5–7', 'own idea', '« anneau de valuation »; « le th. se généralise aussi »',
    BROAD + ['SECTIONS_OVER_Q B.15'], ['normal', 'valuation', 'Main Th', 'complete'],
    'HUA, “Pseudo-morphismes et diviseurs”, L1943–1954, distinguishes the two arguments; Stacks 031S and 0BX7 give the normality and local-extension statements.',
    [r'For the regular-function assertion, retaining noetherian normality restores the height-one intersection argument; replacing it by regularity in codimension one alone loses the S₂ condition.',
     r'For a rational map from an integral variety to a proper variety, R₁ is enough to extend at each codimension-one point, because its local ring is a DVR and the proper valuative criterion supplies a map that extends to a neighbourhood.',
     r'This validates the scope of the second NB through proof (b), without importing the stronger normal-target conclusion of proof (a) into the weakened hypotheses.',
     r'It concerns ordinary rational maps and does not settle the open birational section assertions indexed by SECTIONS_OVER_Q B.15.'],
    'high: the distinct uses of normality and the DVR extension are tracked separately', 'proof')

add('Pseudo-morphisms and normality', 'N05', '“Premiers minimaux” needs its local historical meaning kept visible',
    '57:169 L18–26', 'reading question', '« idéaux premiers non nuls minimaux »; « premiers minimaux »',
    BROAD, ['premiers minimaux', 'hauteur', 'normal', 'diviseur'],
    'HUA, “Pseudo-morphismes et diviseurs”, L1927–1933, silently explains these as primes of height one; no corresponding wording was found in CT.',
    [r'The first occurrence explicitly says minimal nonzero prime ideals, while the final parenthesis shortens this to “premiers minimaux”.',
     r'In a domain, taking the latter in the modern unrestricted sense would include only the zero prime and give the fraction field, so the proof needs the former, height-one interpretation.',
     r'Hua’s explanation clarifies the mathematical intention but does not authorize changing the frozen words.'])

add('The three Picard functors', 'Q01', 'The page distinguishes three functors before discussing representability',
    '57:173 L6–23; 178 L5–15; 179 L3–9', 'unpursued implication',
    '« Prépic »; « Prépic′ »; « enveloppe exacte »', BROAD,
    ['Prépic', 'enveloppe', 'sheaf', 'représentable'],
    'HUA, “Le foncteur de Picard (pages 172 à 182)”, L1956–2013, restates the chain; SN P04–P05, reporting 57:276–277, concerns later quotient formulations.',
    [r'The unprimed functor takes a base change to its absolute Picard group, the primed functor records relative classes after open-cover descent, and the final Picard functor enforces the specified flat descent.',
     r'The distinction explains why the kernel of the first comparison can contain line bundles from the base and why the second comparison can have a Brauer obstruction.',
     r'Neither quotienting by the base nor sheafifying is by itself a proof of the representability postponed at 57:179.'])

add('The three Picard functors', 'Q02', 'The requested cohomological formulation is the low-degree Leray sequence',
    '57:174 L3–14; 175 L7–14', 'own idea', '« donner une formulation cohomologique des raisonnements »',
    BROAD, ['Leray', 'cohomologique', 'rigidifié', 'H^2'],
    'HUA, “Le foncteur de Picard”, L1966–1983, puts the Leray sequence beside rigidification; CT 47:3 uses the same removal of scalar automorphisms.',
    [r'Under \(f_*\mathcal O_X^*=\mathcal O_S^*\), the low-degree sequence is \(0\to\operatorname{Pic}(S)\to\operatorname{Pic}(X)\to H^0(S,R^1f_*\mathbf G_m)\to H^2(S,\mathbf G_m)\to H^2(X,\mathbf G_m)\), on the site being used.',
     r'A section makes the last pullback injective, so the obstruction vanishes and the relative classes lift; rigidifying these lifts kills their scalar automorphisms, making their descent isomorphisms unique.',
     r'This supplies a precise formulation of the requested mechanism, while the separate flat sheafification and its Brauer example require retaining the correct site.'],
    'high: the exact-sequence argument and the section’s retraction are explicit; no new representability theorem is claimed', 'proof')

add('The three Picard functors', 'Q03', 'The universal H⁰ condition is substantive',
    '57:175 L16; 176 L12–23; 177 L7; 179 L3', 'unproved claim',
    '« reste vraie par tte extension de la base »', BROAD,
    ['universel', 'coh. plat', 'changement de base', 'H^0'],
    'HUA, “Le foncteur de Picard”, L1981–1991, repeats the universal qualification; SN P09 reports a similar qualification for a later product formula at 57:283.',
    [r'The descent proof needs compatibility of the direct image with flat base change to recognize whether a bundle comes from the base, and the functorial corollary strengthens this to every base change.',
     r'Connected fibres or the equality of one group of global sections do not by themselves state that universal hypothesis.',
     r'The added local-section assumption in 57:177 is also part of the corollary, not an optional explanation of why descent might work.'])

add('The three Picard functors', 'Q04', 'The Brauer–Severi example distinguishes a sheaf class from a line bundle',
    '57:179 L3–5; compare 174 L5–14', 'unpursued implication',
    '« variété de ... Séveri-Brauer non triviale sur un corps »', BROAD,
    ['Brauer', 'H^2', 'Picard', 'surjectif'],
    'HUA, “Le foncteur de Picard”, L2005–2010, explains the same example; CT 47:3’s rigidified Poincaré bundle represents an additional choice with a section.',
    [r'The geometric hyperplane class of a non-split Brauer–Severi variety is invariant and exists in the relative flat Picard sheaf, although an actual line bundle of geometric degree one would split the corresponding Brauer class.',
     r'This makes the failure of \(\beta\) to be surjective concrete and separates representability of the sheaf from existence of a universal line bundle realizing every class.',
     r'The obstruction’s vanishing is not inferred from a tangent-space computation or from the quotient description alone.'])

add('The three Picard functors', 'Q05', 'The absolute Picard functor already fails separatedness for open-cover descent',
    '57:178 L12–15; 179 L9', 'own idea', '« n’est pas représentable ... sauf dans des cas ... triviaux »',
    BROAD, ['non représentable', 'Pic abs', 'recouvrements', 'Prépic'],
    'HUA, “Le foncteur de Picard”, L1993–2013, preserves the nonrepresentability warning; SN P04 concerns later distinctions between quotient functors.',
    [r'For \(X=S=\operatorname{Spec}k\), the unprimed functor on \(T\) is \(\operatorname{Pic}(T)\); the nontrivial class of \(\mathcal O(1)\) on \(\mathbf P^1\) and the trivial class have identical restrictions to its two standard affine opens.',
     r'Thus this functor fails the separatedness part of the Zariski sheaf condition and cannot be represented by a scheme.',
     r'The example verifies the mechanism behind the warning, while leaving the manuscript’s broad phrase about exceptional “trivial” cases unclassified.'],
    'high: the two restrictions and nonzero degree are explicit', 'proof')

add('The three Picard functors', 'Q06', 'The topology caveat is part of the definition being drafted',
    '57:178 L5–7', 'reading question', '« Il y a un ennui »; « morphismes de localisation fidèlement plats »',
    BROAD, ['localisation', 'quasi-compact', 'topologie', 'enveloppe'],
    'HUA, “Le foncteur de Picard”, L1998–2005, explains this as a covering-family issue; CT 47’s base-change formulas do not resolve this foundational choice.',
    [r'The author notices that formulating descent only with a single faithfully flat quasi-compact map does not directly encode his preceding discussion of arbitrary open coverings.',
     r'A modern reconstruction should specify a site and its covering families before identifying the two sheafifications, rather than silently replace his cancelled alternatives with a standard acronym.',
     r'This is a definitional repair under discussion on the page, not a completed comparison theorem for all non-quasi-compact bases.'])

add('Reused leaves and their independent mathematical content', 'U01', 'The Koszul homotopy supports the marginal annihilator assertion',
    '57:134 L25–43', 'own idea', '« formule d’homotopie »; « les f_i annulent les H »',
    BROAD, ['Koszul', 'homotopie', 'exterieure', 'Cech'],
    'HUA’s introductory editorial policy L85–94 identifies and omits this reused Koszul exposé; CT 47:7–8 and CN F8 use a different Koszul calculation at the unit.',
    [r'Taking \(g\) to be the \(i\)-th standard vector in the displayed identity gives a homotopy from multiplication by \(f_i\) to zero, so \(f_i\) annihilates the Koszul cohomology.',
     r'If \(\sum g_if_i=1\), the same formula contracts the complex and gives the proposition’s vanishing.',
     r'This verifies the local homotopy mechanism on the reused leaf, but does not identify the induced Fourier comparison map in cote 47.'],
    'high: direct substitution in the displayed homotopy identity', 'proof')

add('Reused leaves and their independent mathematical content', 'U02', 'The promised support invariance is a separate omitted argument',
    '57:134 L14–23', 'unproved claim', '« on verra ... seulement de la topologie ... qu’il definit »',
    BROAD, ['Koszul', 'topologie', 'cohomologie', 'Cech'],
    'HUA’s L85–94 omission policy gives no proof of this reused leaf; CN F8’s local Koszul calculation is a different problem.',
    [r'The page defines a direct limit of Koszul complexes and promises independence of the chosen generators, and even dependence only on the corresponding adic topology.',
     r'The stable Koszul/Čech construction works for arbitrary rings and finitely generated ideals; an identification with the derived I-power-torsion functor on modules needs its own hypotheses, as distinguished in Stacks 0952.',
     r'The missing inequality/arrows and parenthesis in this typescript remain transcription issues and are not filled from that familiar interpretation.'])

add('Reused leaves and their independent mathematical content', 'U03', 'Cohen–Macaulay does not mean free unless it is maximal over the regular ring',
    '57:136 L3', 'own idea', '« si l’anneau local est régulier, Cohen Mac sur lui signifie libre »',
    BROAD, ['Cohen', 'codim', 'profondeur', 'completion'],
    'HUA omits the reused commutative-algebra leaf; CT 44:3/CN D07 concern a separate completion issue; SGA 1, Exposé I §9 identifies cohomological codimension with depth, and Stacks 00NT states the maximal-CM result.',
    [r'For the regular local ring \(A=k[[t]]\), the finite module \(M=k\) has \(\dim_A M=\operatorname{depth}_A M=0\), so it is Cohen–Macaulay in the definition just written, but it is not free because \(tM=0\).',
     r'The valid correction U04 requires maximal Cohen–Macaulay, meaning depth equal to \(\dim A\), rather than only equal to \(\dim M\).',
     r'The historical meaning of “codim coh” is checked against SGA 1, and this is a counterexample to the unqualified sentence, not an amendment to its frozen reading.',
     r'An omitted full-dimension or full-support assumption would materially change the claim, but is not supplied by the visible finite-module definition.'],
    'high: the residue-field module supplies the dimension, depth, and torsion checks explicitly', 'proof')

add('Reused leaves and their independent mathematical content', 'U04', 'The corrected regular-local statement and completion proposition have different hypotheses',
    '57:136 L3–15', 'unpursued implication', '« M ... de type fini »; « M qu f sur A »',
    BROAD, ['Cohen', 'complété', 'quasi-finie', 'platitude'],
    'Stacks 00NT supplies the maximal-CM correction; CT 44:3/CN D07 treats another completed-module assertion and does not prove this leaf’s flatness criterion.',
    [r'A finite maximal Cohen–Macaulay module over a regular local ring is free, as in Stacks 00NT; this is the refinement of the sentence tested in U03.',
     r'The separate flatness proposition uses a finite \(B\)-module and completion for the maximal ideal of \(B\), while the later corollary adds a quasi-finiteness condition over \(A\) before concluding freeness over the completed base.',
     r'The proof sketch invokes an earlier proposition and a Tor/completion comparison absent from this selection, so those hypotheses should not be erased by appealing to the corrected CM sentence.'])

add('Reused leaves and their independent mathematical content', 'U05', 'The surface degree argument checks its leading coefficient, not a Néron–Tate pairing',
    '57:156 L6–18; 148 L4–20', 'own idea', '« mah²−bh ≤ ah²−b*h+const. »',
    BROAD + ['WG H9'], ['Néron', 'intersection', 'surface', 'quadratic'],
    'CT 44:4 Th. 5 and CN D12 concern a height/intersection identity; HUA’s policy L85–94 omits these reused surface pages.',
    [r'Assuming the two displayed linear-system estimates, division by \(h^2\) and passage to arbitrarily large \(h\) give \(ma\leq a\), so \(a>0\) and the positive integer degree force \(m=1\).',
     r'This checks the last numerical step while leaving the earlier geometric and analytic inputs at their source status.',
     r'The calculation supplies no Néron–Tate height, generic-pencil pairing, or normalization for WG H9.'],
    'high for the leading-coefficient deduction; no independent verification of the cited surface theorems', 'proof')

add('Reused leaves and their independent mathematical content', 'U06', 'The printed finiteness leaf explains why a local equality spreads',
    '57:154 L10–19; compare 171 L7', 'unpursued implication', '« de type fini »; « les restrictions ... à D(g) sont identiques »',
    BROAD + ['SECTIONS_OVER_Q B.15'], ['type fini', 'voisinage', 'localité', 'valuation'],
    'CT 54:4,6/CN D06 is another reused finite-presentation context; HUA largely omits these printed EGA sheets.',
    [r'The proof uses finitely many algebra generators to choose one common denominator, thereby extending equality at a local ring to equality on a neighbourhood.',
     r'This is useful background for the local-to-open step in the rational-map argument at 57:171, but the leaf is an independent printed algebraic statement and supplies no theorem on arithmetic sections.'])

add('Reused leaves and their independent mathematical content', 'U07', 'Formal completion and later reuse do not by themselves prove an algebraization claim',
    '57:159 L3–15; 165 L4–8', 'unproved claim', '« B est un anneau ... adique »; « complété séparé »',
    BROAD, ['complété', 'adique', 'algébrisation', 'hensélien'],
    'CT 44:3/CN D07 and SN P02/C09 concern distinct completion or algebraization issues; HUA’s introductory policy omits most reused printed text.',
    [r'The printed leaves concern an adic algebra presentation and the continuous extension of a topological module action, respectively.',
     r'They identify algebraic completion mechanisms but contain no passage from a formal Picard object to an algebraized family in the analytic/local questions reported by SN P02.',
     r'Their cited earlier lemmas and the ambiguous product-versus-list of generators at 57:159 are dependencies to check before reusing the printed proof in a new setting.'])

add('Reused leaves and their independent mathematical content', 'U08', 'The continuous-functions example retains compactness and topology assumptions',
    '57:161 L23', 'unproved claim', '« espace compact infini Y »; « Y n’est pas un espace noethérien »',
    BROAD, ['fonctions continues', 'compact', 'noethérien', 'spectre'],
    'HUA omits this reused spectral-topology paragraph; no matching example was found in CT or SN, so its connection to WG2 is dossier identification only.',
    [r'The printed example embeds the compact space into the maximal spectrum of its continuous-function ring and uses its non-noetherian topology to detect a non-noetherian spectrum.',
     r'A reconstruction should state the Hausdorff convention and the coefficient field of “fonctions continues numériques” before applying the usual maximal-ideal description.',
     r'This printed example contributes no evidence for the Picard representability assertions on the neighbouring handwritten leaves.'])

add('Reading questions after the freeze', 'R01', 'The affine-kernel modernization is not an independent reading',
    '57:133 L5–12; 135 L10, L18–22', 'reading question',
    '« un sous-groupe d’un groupe affine »; « alg.-affine »; « Sorb. chev. » [uncertain]',
    BROAD, ['Seshadri', 'quasi-affine', 'noyau', 'Sorb'],
    'HUA, “Le noyau pour un morphisme surjectif”, L1707–1728, changes the theorem’s phrasing, calls the first corollary quasi-affine, and supplies “Seshadri”.',
    [r'The frozen theorem says a subgroup of an affine group, the first corollary says “alg.-affine”, and the finite-descent attribution remains \(\backslash\mathrm{unsure}\{\mathrm{Sorb.\ chev.}\}\).',
     r'Hua instead describes an extension, refers in a footnote to “quasi-affine”, and resolves the attribution as Seshadri, so these are interpretive differences requiring a future return to the ink rather than replacements of the current readings.',
     r'His mathematical reconstruction is credited in P01, but it is not a second source witness for these exact words.'])

add('Reading questions after the freeze', 'R02', 'The μ conventions change inside the curve block',
    '57:147 L30–54; 149 L3–23; 155 L5–17', 'reading question',
    '« μ_α=1+δ_α »; « μ′_α ... diminué de 1 »; « les μ_α=0 »',
    BROAD, ['mu', 'delta', 'branches', 'courbe réduite'],
    'HUA, “Le Picard d’une courbe réduite”, L1791–1833, replaces the manuscript’s μ by normalization-defect δ and describes μ=1+δ as in a cancelled passage.',
    [r'The frozen file places \(\mu_\alpha=1+\delta_\alpha\) before the outer deletion at 57:147 L37, while Hua includes it in the barred passage, and 57:149 subsequently defines \(\mu^{\prime}_\alpha\) as branches minus one.',
     r'The unprimed \(\mu_\alpha=0\) at 57:155 should therefore remain a reading/notation question rather than be silently rewritten as vanishing additive part.',
     r'The independent notation in C01 permits a mathematical comparison without asserting that all these manuscript symbols were used consistently.'])

add('Reading questions after the freeze', 'R03', 'The change from double to multiple points is source evidence',
    '57:151 L23–25; 155 L5–8', 'reading question',
    '« pts [doubles deleted] multiples “multiplicatifs” »',
    BROAD, ['multiples', 'doubles ordinaires', 'axes', 'Picard'],
    'HUA’s curve subsection footnote L1828–1833 says both archive pages 150 and 154 formulate the condition with ordinary double points.',
    [r'The frozen 57:151 records “doubles” deleted and “multiples” inserted, whereas 57:155 still contains “pts doubles”.',
     r'This is a real difference between the current diplomatic record and the modernized footnote, and it matters when comparing a node with coordinate-axis singularities of higher valency.',
     r'The source states of both pages are retained, with no post-context correction.'])

add('Reading questions after the freeze', 'R04', 'The last cohomology degree stays doubtful even though the long exact sequence is clear',
    '57:164 L31–34', 'reading question', '« H_f^{1|2} O_X » [explicit doubt]',
    BROAD + ['MPL_57_271-315 D07'], ['tangent', 'H^2', 'Div', 'obstructions'],
    'HUA, “Diviseurs et Picard : la suite tangente”, L1907–1910, reports an ink reading of H¹ and corrects it to H²; CT 54:3/SN D07 are different tangent-sequence comparators.',
    [r'The frozen transcription has \(\backslash\mathrm{unsure}\{1|2\}\), while Hua presents a confident reading of 1 and then a mathematical correction to 2.',
     r'D04 checks why 2 is the expected cohomological degree, but that argument cannot decide the superscript actually written or the partly illegible smoothness pointers.',
     r'The two levels of uncertainty remain separate.'])

add('Reading questions after the freeze', 'R05', 'A missing prime changes the literal rigidification assertion',
    '57:174 L19; 177 L3; compare 173 L6–23', 'reading question',
    '« tout élémᵗ de Prépic(X/S) »; « élts de Prépic(X/S) »', BROAD,
    ['Prépic', 'rigidifié', 'Pic abs', 'section'],
    'HUA, “Le foncteur de Picard”, L1976–1983, states the conclusion for Pic′, while CT 47:3 uses explicitly rigidified objects.',
    [r'The frozen occurrences are unprimed, but the surrounding gluing proof and Hua’s formulation concern relative classes after quotienting by base bundles.',
     r'With \(X=S=\mathbf P^1\) and the identity section, the absolute class \(\mathcal O(1)\) has no rigidified representative in that same absolute isomorphism class, although its relative class does.',
     r'This provides a mathematical reason to ask whether a prime was omitted or shorthand was being used, while the source remains unprimed in the frozen transcription.'])

add('Reading questions after the freeze', 'R06', 'The adjunction criterion is stronger than the literal “il faut” wording',
    '57:176 L13–23', 'reading question', '« il faut que »; « f^*f_*(E)−E »',
    BROAD, ['image inverse', 'loc. libre', 'descente', 'adjunction'],
    'HUA, “Le foncteur de Picard”, L1986–1990, reformulates the passage as an if-and-only-if criterion after flat base change.',
    [r'The frozen statement says “il faut que” and its displayed adjunction connector has no arrowhead, while Hua supplies the equivalence used by the surrounding proof.',
     r'The intended sufficiency would descend local freeness of \(f_*E\) and invertibility of the counit under the stated base-change hypotheses, but that reconstruction is not a license to add “et il suffit” or an arrow to the source.',
     r'The uncertain marginal quasi-compact/quasi-separated condition must also stay explicit.'])

add('Reading questions after the freeze', 'R07', 'The projective quotient paragraph has unresolved objects and indices',
    '57:158 L5–25; 160 L7–19, L33–50; 162 L3–16', 'reading question',
    '« P_S^N » with E of rank N; « P principaux sur X »; « P|S−J/GP(N) »',
    BROAD, ['rang', 'projectif', 'principal', 'GP(N)'],
    'HUA, “Plongements projectifs et foncteur de Picard (pages 156 à 163)”, L1859–1895, regularizes the projective dimensions and torsor bases in its interpretation.',
    [r'The frozen rank/projective-dimension convention, the written base of the principal bundle, and the final uncertain source \(\mathcal P|S\) cannot all be resolved by the standard PGL-torsor template.',
     r'The interpretation in D01–D03 should therefore be read as a reconstruction of the classification problem, not a claim that every object or index on these difficult pages has been deciphered.',
     r'The source uncertainties and the uncertain \(\mathcal J|\mathcal I\) letters are preserved.'])

add('Reading questions after the freeze', 'R08', 'The finite algebra generators may form a list rather than a product',
    '57:159 L5, L8–10', 'reading question', '« c_i a_j » in the generation argument',
    BROAD, ['c_i', 'adique', 'générateurs', 'completion'],
    'HUA omits most of this reused printed EGA proof; CT 44:3/CN D07 is a separate completion argument and supplies no source reading here.',
    [r'The printed argument and marginal addition suggest checking whether the visible juxtaposition of the lifted algebra generators and ideal generators was intended as a list, while the frozen transcription preserves the printed separation as read.',
     r'A list and a family of products have different generation properties, so a later use of the argument should return to the source and its cited previous proposition.',
     r'No correction is inferred solely from what the completed-algebra proof would need.'])

add('Reading questions after the freeze', 'R09', 'The contour around the ν calculation may not be a deletion',
    '57:151 L8–15', 'reading question', '« Soit ν_α le nbr ... » [encoded as deleted]',
    BROAD, ['nu', 'branches', 'cycles', 'courbe réduite'],
    'HUA’s curve subsection L1803–1833 supplies a cleaned-up graph calculation, not a description of this contour’s physical function.',
    [r'The frozen diplomatic file encodes the opening \(\nu_\alpha\) calculation as a deleted block, but the audit records that the long contour might instead isolate the calculation.',
     r'The modernization cannot decide this page-state question, and its mathematical agreement with part of the calculation would not prove that the lines are live.',
     r'The doubt is repeated here because it affects the distinction between a rejected trial and an unfinished continuation, without changing the frozen file.'])

def sf(ident, title, where, quote, search, comparison, sentences):
    add('Standing question: steps the manuscript itself marks as unverified', ident, title, where,
        'self-flagged: a step he himself marks as unverified', quote, BROAD, search, comparison, sentences)

sf('SF01', 'Question beside the affine-kernel theorem', '57:133 L5–6', '« ? »',
   ['noyau', 'interrogation', 'affine'], 'HUA, “Le noyau pour un morphisme surjectif”, L1713–1717, notices this authorial question; P01 gives the proof dependencies.',
   ['The isolated question mark qualifies the opening theorem or its formulation, and the sheet does not specify a narrower target for it.', 'It is retained as an authorial flag rather than resolved by the theorem’s later modern formulation.'])

sf('SF02', 'Representability assumed to simplify the proof', '57:133 L14; 135 L22',
   '« On va pour simplifier admettre ... représentables »', ['admettre', 'représentables', 'noyau'],
   'HUA’s affine-kernel subsection restates the proof; CT 44:2’s programme does not remove this assumption.',
   ['Representability of the intermediate Picard objects is an admitted input, explicitly recalled on the next handwritten leaf.', 'The present selection does not include the suggested proof avoiding it.'])

sf('SF03', 'Base-field extension and the reduced comparison remain queried', '57:133 L16–22',
   '« (extension? ) » [first word doubtful]; diagram arrow « ? »', ['algébriquement clos', 'réduit', 'noyau'],
   'HUA’s affine-kernel subsection L1719–1725 presents these as proof steps; the current doubts file preserves their source marks.',
   ['The algebraically closed base-field reduction and the reduced Picard comparison are accompanied by separate question marks.', 'The uncertain word before the first question mark is an editorial reading doubt, while the question marks themselves are the source’s unfinished-step evidence.'])

sf('SF04', 'Dispensing with the admitted Picard schemes is an expectation', '57:135 L22',
   '« on peut sans doute s’en passer ! »', ['sans doute', 'Picard', 'représentable'],
   'HUA’s affine-kernel subsection does not supply this alternative proof; P01 separates the expectation from the argument actually given.',
   ['The author expects representability of the intermediate objects can be avoided.', 'No replacement proof is written in this selection, so this remains an expectation under the dossier entry WG2 §1.1 #3.'])

sf('SF05', 'Generator/topology invariance promised for later', '57:134 L21',
   '« on verra en effet ulterieurement »', ['Koszul', 'topologie', 'Cech'],
   'HUA’s introductory omission policy excludes the full reused Koszul text; U02 identifies the missing comparison argument.',
   ['The reused typescript postpones the independence of the limiting cohomology from the generators and its dependence only on the indicated adic topology.', 'This is a promise in that separate text, not a proof supplied by the neighbouring Picard notes.'])

sf('SF06', 'A special Cohen–Macaulay lemma is still to be drafted', '57:136 L3',
   '« il faudrait sans doute un lemme spécial »; « peut-être ... l’équidimensionnalité »',
   ['Cohen', 'codim', 'équidimensionnalité'], 'HUA omits this reused leaf; U03–U04 distinguish its literal freeness claim from a valid corrected statement.',
   ['The author requests a separate lemma and possibly an equidimensionality addition, while also revising the form of an earlier corollary.', 'The earlier numbered material is outside this selection, so the requested lemma cannot be treated as already supplied here.'])

sf('SF07', 'Kummer/transgression comparison expressly left open', '57:144 L21–32',
   '« à vérifier ...... »', ['Kummer', 'vérifier', 'torseur'],
   'HUA, “Une obstruction pour une courbe épointée”, L1774–1778, preserves the flag; CT 47:8 has a separate compatibility gap, discussed in FW01–FW02.',
   [r'The unfinished step is \(\xi_n=\delta_n(\eta)\), comparing the spectral-sequence class with the boundary of the degree-one Picard torsor.', 'The following vanishing deductions should therefore retain their dependence on that comparison.'])

sf('SF08', 'The “inutile?” annotation is itself an uncertain reading', '57:158 L5–8',
   r'« inutile? » [the whole word is under \unsure]', ['très ample', 'spécial', 'projectif'],
   'HUA, “Plongements projectifs et foncteur de Picard (pages 156 à 163)”, L1859–1895, reorganizes the conditions, without settling this exact annotation.',
   ['A marginal note possibly asks whether part of the initial very-ample/frame setup is unnecessary.', 'Because the word and its precise target are uncertain, this is a tentative self-flag and cannot be reported as a definite withdrawal of a named hypothesis.'])

sf('SF09', 'The elementary Picard argument still needs reformulation', '57:173 L23, L32–37; 175 L12–14',
   '« mettre ce ... sous forme d’une suite exacte plutôt »; « donner une formulation cohomologique »',
   ['Leray', 'cohomologique', 'expliciter', 'rigidifié'],
   'HUA, “Le foncteur de Picard”, L1966–1983, juxtaposes Leray and rigidification; Q02 gives a proposed precise formulation.',
   ['These are authorial requests to improve the proof’s formulation and introduce its lemmas, not assertions that the result has been disproved.', 'The unambiguous final question asks for the cohomological explanation of the gluing reasoning.'])

sf('SF10', 'A problem with the covering convention is noticed', '57:178 L7',
   '« Il y a un ennui »; « Il faut donc dire au lieu de ... »',
   ['recouvrement', 'localisation', 'quasi-compact'],
   'HUA, “Le foncteur de Picard”, L1998–2005, offers a modern topology interpretation; Q06 retains the exact drafting issue.',
   ['The author explicitly revises the type of covering morphism used in the descent definition.', 'His successive cancellations show a definition being adjusted and do not themselves prove the equivalence of the resulting sheafifications.'])

sf('SF11', 'The Brauer obstruction is promised', '57:179 L5',
   '« On verra qu’il y a une obstruction ... H²(S,G_m) »',
   ['obstruction', 'Brauer', 'H^2'],
   'HUA, “Le foncteur de Picard”, L2005–2010, explains the same example; CT 47:3 is a related but different rigidified-kernel construction.',
   ['The page gives a Brauer–Severi example and announces a later cohomological obstruction to surjectivity.', 'The earlier Leray discussion supplies a nearby mechanism, but this sentence still refers forward to the flat Picard comparison and its chosen topology.'])

sf('SF12', 'General representability is deferred', '57:179 L9',
   '« des cas généraux importants qui seront étudiés par la suite »',
   ['représentable', 'Picard', 'suite'],
   'HUA, “Le foncteur de Picard”, L2009–2013, summarizes representability in important cases but omits the explicit promise of later study; SN P05–P06 gives later first-pass representability leads.',
   ['The final Picard sheaf is announced to be representable in important general cases.', 'The selection stops before the promised representability argument and cannot be cited as having proved that theorem.'])

sf('SF13', 'An analytic function-field proof is deferred to an appendix', '57:150 L4',
   '“A proof of this fact ... will be given in Appendix below.”',
   ['Appendix', 'meromorphic', 'surface'],
   'HUA’s introductory policy omits these reused surface sheets; CT 44:4/CN D12 concerns a different intersection problem.',
   ['The reused English text promises a proof that the meromorphic function field is finite over the field generated by two algebraically independent functions.', 'The appendix is not part of these four leaves, so the promise and its cited Chow input remain external dependencies.'])

def title(ident, name, where, quote, search, comparison, sentences):
    add('Standing question: title sheets, internal headings, dates, and page counts', ident,
        name, where, 'unpursued implication', quote, CARRY, search, comparison, sentences)

title('T01', 'Curve Picard cover', '57:141 L3', '« Picard des schémas en courbes » [en doubtful]',
      ['Picard des schémas', 'courbes'], 'HUA calls the block “Le Picard des schémas en courbes (pages 140 à 154)”; SN §9 is only a comparison for recording local titles.',
      ['This is a local title sheet for the curve material, with no written page count.', 'Hua’s page 140 corresponds to current scan 141; neither number is an authorial total.'])

title('T02', 'Picard and divisors cover', '57:157 L4–5', '« Foncteurs|Foncteur de Picard, Diviseurs ... »',
      ['Foncteur de Picard', 'Diviseurs'], 'HUA introduces a Picard/divisor block for archive pages 156–163; SN §9 records different covers in the later selection.',
      ['The local cover names the Picard functor(s) and divisors, with the singular/plural reading still open.', 'No number of pages or authorial range is written on it.'])

title('T03', 'Pseudomorphisms heading', '57:166 L3–4', '« A K »; « Pseudomorphismes »',
      ['AK', 'Pseudomorphismes'], 'HUA, “Pseudo-morphismes et diviseurs”, L1914–1916, also leaves AK unexplained.',
      ['This is an internal heading on a mathematical sheet rather than a separate counted cover.', 'The initials or letters “A K” remain unexplained, and no page total is present.'])

title('T04', 'Picard functor heading', '57:173 L3–4', '« Le foncteur de Picard »',
      ['Le foncteur de Picard', 'classes de diviseurs'], 'HUA’s corresponding section is numbered archive pages 172–182 and extends beyond the present selection.',
      ['The heading starts the elementary functor discussion and is accompanied by a marginal description of its subject.', 'The present batch ends at scan 179, so the larger Hua section range does not supply an authorial page count for this batch.'])

title('T05', 'Reused chapter title and contents', '57:163 L3–27',
      '« Nouveau fascicule »; « Chapitre Premier / LE LANGAGE DES SCHÉMAS / Sommaire »',
      ['Nouveau fascicule', 'LANGAGE DES SCHÉMAS', 'Sommaire'], 'HUA’s introduction identifies reused EGA sheets but generally omits their printed contents; CT/SN provide other reuse examples, not this title’s count.',
      ['The printed title and the numbered contents list ten sections, from affine schemes to formal schemes.', 'Ten is a section count, and the references to Chapter III and §§1–8 or §10 are internal cross-references, not a count of pages in this manuscript packet.'])

title('T06', 'The four English surface leaves have their own printed sequence',
      '57:152 L3; 150 L3; 156 L3; 148 L3', 'printed “39”, “40”, “41”, “42”',
      ['surface', 'Chow', 'Kodaira'], 'HUA’s introductory policy L85–94 recognizes a reused compact-surface typescript; JAC05 compares its subject with the different cote 44 height programme.',
      ['Their source order is scan 152 (39), 150 (40), 156 (41), 148 (42), which differs from their archive scan order.', 'These are printed page labels on reused text, not authorial handwritten numbering of the Picard notes or a four-page count written by the author.'])

title('T07', 'Topological-module printed leaf', '57:165 L3–4',
      'printed “− 34 −”; “n° 297”',
      ['Complété', 'module topologique', '297'], 'HUA omits most of the reused printed text; CT 44:3/CN D07 is an unrelated completion comparison.',
      ['The leaf carries its own printed page label 34 and the separate printed number 297.', 'Neither number belongs in an authorial manuscript-page macro or determines the extent of this Picard packet.'])

title('T08', 'Other printed and typed local headings',
      '57:134 L42; 154 L11; 159 L12; 161 L17',
      '« 2. Cohomologie de Cech d’un recouvrement ouvert »; « 6.5 »; « 7.6 »; « (1.1.5) »',
      ['Cech', '6.5', '7.6', '1.1.5'], 'HUA’s introductory policy recognizes these reused EGA/Koszul materials; no matching packet-length statement was found in CT or SN.',
      ['These are section or proposition numbers in independent reused texts, not page-count statements for the handwritten block.', 'The full wording remains in the transcription and the inventory classifies the reused sheets separately.'])

title('T09', 'The Benjamin letter dates itself, not its neighbours', '57:143 L12–16',
      '“Massy November 21, 1966”; “Huit exposés ...”',
      ['Benjamin', '1966', 'Huit exposés', 'Bourbaki'], 'CT 44:8 has the dated 12.8.1964 letter; HUA omits this reused correspondence, so the chronology limitation here is an editorial conclusion from the dated objects actually present.',
      ['The letter concerns the front matter and copyright arrangements for the named book and also mentions letters of July 8 and November 10.', 'Its date is secure documentary information about this reused letter, but it does not date the adjoining Picard handwriting or prove an earlier/later relationship to all seven cote 44 theorems.'])

title('T10', 'No explicit manuscript page total is present in this selection',
      '57:133–179, all 43 kept scans; covers 141 and 157',
      'covers have titles without a “pages” total', ['pages', 'page count', 'titre', 'Sommaire'],
      'SN §9 gives the same recording distinction for another selection; HUA’s ranges and its whole-cote coverage are editorial organization, not counts written on these sheets.',
      ['No explicit authorial total such as “19 pages” or authorial “Pages 1–67” range was identified in these 43 scans.', 'The archival foliation recorded in TeX comments, the scan numbers, and the task’s 43-page selection count are separate from handwritten authorial numbering; no secure authorial page number was encoded with \\mspage in this batch.', 'This negative finding is limited to the supplied selection and cannot establish the extent or chronology of every text inside cote 57.'])

add('Singular curves and dimension calculations', 'C07', 'The exact sequence carries extension data beyond the dimensions',
    '57:147 L5–13, L20–29; 151 L27–38', 'unpursued implication',
    '« partie linéaire »; « g=...+ρ+σ »',
    BROAD + ['MPL_57_271-315 C04', 'MPL_57_271-315 D07'], ['extension', 'normalisée', 'scind', 'dualité'],
    'HUA, “Le Picard d’une courbe réduite”, L1785–1820, rewrites the same sequence; SN C04/I03 concerns pinching and SN D07 warns about a different, Hodge-theoretic extension.',
    [r'The normalization calculation gives a group extension with an affine kernel, and its dimension formula does not give a canonical product decomposition of the entire \(\operatorname{Pic}^0\).',
     r'A subsequent use should retain the extension class when relating the component Jacobians to the toric or unipotent contribution.',
     r'This is the same logical distinction between extension data and splitting data emphasized in the earlier D07 lead, although that lead concerns a different extension and is not a proof about this one.'])

add('Projective classes and divisor deformation', 'D06', 'A cohomological tangent dimension is not the dimension of a reduced Picard variety',
    '57:164 L25–34', 'unpursued implication', '« H¹_f(O_X) » below “Tangent ... Pic/S”',
    BROAD + ['WG2 §2.3 #12', 'MPL_57_271-315 J03', 'MPL_57_271-315 D07'],
    ['Igusa', 'non-réduit', 'tangent', 'Hodge'],
    'SN E01/E06/E07 reports Igusa and infinitesimal Picard phenomena at 57:284–286,294,297; CT 54:3 and SN D07 compare Hodge/tangent extensions, all retained at their supplied status.',
    [r'The diagram labels a tangent term, while the following terms and margins keep obstructions and smoothness hypotheses visible.',
     r'The later package’s reported nonreduced Picard examples explain why this cohomological dimension should not automatically be substituted for the dimension of the reduced identity component.',
     r'Neither that substitution nor the displayed tangent sequence proves the higher-cycle Betti bound in WG2 §2.3 #12, and no Oda theorem has been independently checked for this comparison.'])

add('Pseudo-morphisms and normality', 'N06', 'A known birational fundamental-group link requires regularity and purity',
    '57:170 L9–19; 171 L5–7', 'unpursued implication', '« Y une variété complète »; « anneau de valuation »',
    BROAD + ['SECTIONS_OVER_Q B.15'], ['birational', 'fondamental', 'purity', 'valuation'],
    'CT 16:19 supplies only broad cohomological background; RS SECTIONS_OVER_Q B.15 is an open birational-section entry; SGA 1, Exposé X, Corollaries 3.3–3.4, gives the established geometric comparison.',
    [r'For regular proper varieties, combining codimension-two indeterminacy with purity of finite étale covers leads to the birational invariance of the étale fundamental group stated in SGA 1, Exposé X, Corollary 3.4.',
     r'This is a known comparison suggested by the current valuative proof, and regularity in the purity step must not be weakened merely because the map-extension step only needs R₁.',
     r'The group invariance does not classify arithmetic sections or settle SECTIONS_OVER_Q B.15.'])

add('Reading questions after the freeze', 'R10', 'The Néron–Severi subscript should not silently become “modulo torsion”',
    '57:133 L12', 'reading question', '« Nér Sév_0 » [name doubtful]',
    BROAD + ['MPL_57_271-315 E08'], ['Néron', 'torsion', 'Nér', 'NérSev'],
    'HUA, “Le noyau pour un morphisme surjectif”, L1711–1717, interprets the statement modulo torsion while retaining uncertainty about the subscript; SN E08 separates torsion questions from rank questions.',
    [r'The frozen notation has a subscript 0, while Hua gives a torsion-quotient interpretation that is not defined on the present sheet.',
     r'The nearby assertion about abelian parts explicitly retains a perfect-field qualification, so a reconstructed statement should state both its component convention and its base-field assumptions.',
     r'The current injectivity line does not answer the later torsion-continuity questions indexed by MPL_57_271-315 E08.'])

add('Reading questions after the freeze', 'R11', 'The quotient formula clarifies a literal isomorphism slip',
    '57:138 L7–14', 'reading question', '« le dernier hom est un isom »; « Pic(X)/Pic(Σ) »',
    BROAD, ['Leray', 'surjectif', 'isom', 'Pic relatif'],
    'HUA, “Pic relatif et suite de Leray”, L1735–1739, says the last arrow is surjective and identifies the quotient; CT 47:3 uses relative rather than absolute classes.',
    [r'The page calls the last arrow an isomorphism but immediately gives the quotient formula, and Hua changes that adjective to surjective.',
     r'For \(X=\Sigma=S=\mathbf P^1_k\) with identity maps, the arrow \(\operatorname{Pic}(X)\to\operatorname{Pic}^{\prime}(X/S)\) is \(\mathbf Z\to0\), while the quotient by \(\operatorname{Pic}(\Sigma)\) is indeed zero.',
     r'This checks the mismatch in the literal assertion and motivates the reading question without changing the frozen word “isom”.'])

add('Standing question: steps the manuscript itself marks as unverified', 'SF14', 'An annotated proof challenges its generating condition; hand attribution is uncertain',
    '57:159 L8–10', 'reading question', '« définition insuffisante » [uncertain]; « il faut aussi ... engendrent JB/J²B ! »',
    BROAD, ['définition insuffisante', 'engendrent', 'crayon', 'adique'],
    'HUA’s projective section footnote, L1892–1895, says the pencil annotations on these printed EGA leaves are not securely attributed.',
    [r'The margin challenges a generating condition and emphasizes the degree-one part of the associated-graded argument.',
     r'It is included as a flagged step in the annotated source, but the evidence does not justify attributing this particular hand to Grothendieck with certainty.',
     r'R08 records the separate product/list reading question, and neither annotation is treated as a completed replacement proof.'])

def main():
    (ROOT/'documentation'/'root_research_items.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(notes)} root research items staged')

if __name__ == '__main__':
    main()
