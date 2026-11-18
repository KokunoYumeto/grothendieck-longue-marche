#!/usr/bin/env python3
"""Rebuild the post-freeze research notes and per-item context-search ledger.

Only generated research files are written. Frozen transcription files are read
for locator validation, never changed. The attached context must be available
at ../../context to rerun the searches; it is deliberately excluded from ZIPs.
"""
from pathlib import Path
import csv
import re
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / 'context'
NOTES = []

def add(id, section, title, kind, ms, quote, body, context, query,
        check='used and rechecked in this run', outcome=None, results=()):
    NOTES.append(dict(id=id, section=section, title=title, kind=kind, ms=ms,
                      quote=quote, body=body, context=context, query=query,
                      check=check, outcome=outcome, results=results))

add('N001','A. What the dossier does and does not establish','The uniformization part of the planning guess is supported','unpursued implication',
'002:L3-5;018:L12-26;023:L2-6',
r'Connexions projectives canoniques et uniformisation des courbes algébriques',
r'''The dossier develops pointed projective bundles, projective connections, monodromy, and the uniformizing representations of compact complex curves, so the uniformization part of the planning guess is supported by substantial content, not only by its title. It also develops a separate formal normalization problem on scans 25–34; the Hodge-theoretic pages do not visibly complete the proposed bridge between those two parts.''',
'Adds direct manuscript evidence to context/README.md, “The guess” (S20), and agrees with Hua, modernised reading of cote 159, hua_project/159.modern.tex, §§“Les stations” and “Ce qui ne s’articule pas”, while retaining the unfinished bridge as unfinished.',
r'uniformisation|Les stations|ne s.articule|S20',results=('S20',))

add('N002','A. What the dossier does and does not establish','Projective structures and scalar differential equations','own idea',
'018:L26-35;020:L3-19;021:L3-15',r'connexions projectives',
r'''Confidence: high for the modern comparison, low for any exact identification of the manuscript’s scalar normalization, because no complete Schwarzian equation is written here and scan 20 has incompatible signs. Beilinson–Drinfeld, Opers, §§2.6–2.7, identify a projective structure with a transverse section of a flat projective-line bundle and with a normalized second-order operator whose solution ratio gives projective coordinates [L1]; this supplies a precise comparison to attempt, not a missing manuscript formula.''',
'Bears on RESULTS_STATE.md entry MPL_93_002-046 P01 (“Identifying the normalization of the Schwarzian”) and P09; differs from treating the title-level comparison in context/README.md as an already identified equation, and supplements Hua, hua_project/159.modern.tex, §“Le calcul en coordonnées, et la formule encadrée”.',
r'Schwarz|P01|P09|formule encadr',results=('MPL_93_002-046 P01','MPL_93_002-046 P09'))

add('N003','A. What the dossier does and does not establish','There is no single characteristic assumption for all the pages','reading question',
'009:L3-7;013:L10-14;015:L13-18;021:L13-15;022:L23;026:L2-9;029:L40-45;034:L7-9',r'sans condit. de dim ni de car. ?',
r'''The opening question is deliberately unrestricted, scan 13 marks characteristic different from two, the moduli calculation is placed in characteristic zero, the automorphism argument uses invertibility of two, and the formal normalization propositions explicitly use characteristic zero. The density proposition still carries “de car nulle ?”, so neither an all-characteristic theorem nor a uniform blanket hypothesis should be read into the whole dossier.''',
'Refines context/README.md, “The guess”, and Hua, hua_project/159.modern.tex, §§“Conventions, valables pour tout le dossier”, “Le théorème de rigidité”, and “La densité de Zariski, et où la situer”, by listing the actual locations and the surviving authorial question.',
r'caract.ristique|car nulle|car\.\}|Conventions|rigidit',results=('S20',))

add('N004','A. What the dossier does and does not establish','No p-curvature calculation has been located','reading question',
'009:L7-36;011:L3-14;012:L10-26;029:L21-45;034:L7-9',r'stratification',
r'''No explicit p-curvature, Frobenius, or Cartier calculation was read on these 32 supplied pages; that is a bounded negative finding, subject to the marked illegible words and uncertain readings. The changes from connection to stratification and the denominators in the formal recurrence provide reasons for a future characteristic-p comparison, but do not themselves constitute one.''',
'Does not confirm the p-curvature part of context/README.md, “The guess” (S20), and respects the evidentiary limit in RESULTS_STATE.md, MPL_93_002-046 P09; Hua, hua_project/159.modern.tex, §“Ce qui ne s’articule pas”, likewise does not supply a manuscript p-curvature computation.',
r'courbure|Cartier|Frobenius|P09|stratification',results=('S20','MPL_93_002-046 P09'))

add('N005','A. What the dossier does and does not establish','Cotes 93 and 64 are a proposed comparison, not a manuscript cross-reference','reading question',
'002:L3-5;011:L3-14;012:L10-26;018:L16-26',r'connexion',
r'''No explicit citation to cote 93 or cote 64 was located in the supplied leaves, and the actual pages of those cotes are not part of this context attachment. The available RESULTS_STATE.md gives only labels or truncated summaries for P01, P09, and C35, so their underlying arguments and the normalization in cote 93 cannot be checked from those summaries.''',
'Limits the proposed cluster in context/README.md, “The guess”, and RESULTS_STATE.md, “What other packages’ research notes say about these cotes”, entries MPL_93_002-046 P01, P09, and C35; the precise comparison remains to be made from the sources rather than inferred from their titles.',
r'\b93\b|\b64\b|P01|P09|C35',results=('MPL_93_002-046 P01','MPL_93_002-046 P09','MPL_93_002-046 C35'))

add('N006','A. What the dossier does and does not establish','The suggested tower and icosahedral links do not receive a solution here','reading question',
'018:L3-24;022:L18-24;023:L2-6',r'Zariski-dense',
r'''The monodromy here concerns unbranched projective structures on smooth projective curves of genus at least two; it neither gives Schwarz’s finite-monodromy list nor compares the absolute Galois group with GT or GT0. Its characteristic-zero density conclusion actually excludes finite projective monodromy in that setting, so a passage to punctured, branched, or orbifold curves would be needed before applying the suggested finite-group comparison.''',
'Does not settle the conditional leads in RESULTS_STATE.md, “Orientation for this package”, namely FERMAT_SUCCESSOR C.20, LM4 F.7, or LM1 D.7; those remain the prior runs’ open claims, not results of this transcription.',
r'FERMAT_SUCCESSOR C\.20|LM4 F\.7|LM1 D\.7|Schwarz|icosa',results=('FERMAT_SUCCESSOR C.20','LM4 F.7','LM1 D.7'))

add('N007','B. Pointed projective bundles and stratifications','The extension dictionary fixes the object being recovered','unpursued implication',
'002:L7-23;003:L3-7;008:L3-24',r'équivalence de catégories',
r'''A pointed Brauer–Severi bundle is encoded by an extension 0→Ω→E→O→0, with the quotient line normalized to O; a first-order projective identification then identifies Ω with Ω¹ of the base curve or variety. This distinction between the pointed bundle and the additional connection is essential when interpreting the subsequent word “canonique”.''',
'Restates the dictionary in Hua, modernised reading of cote 159, hua_project/159.modern.tex, §“Trois descriptions d’un même objet”, and adds its role in limiting the question on scan 9.',
r'Trois descriptions|extension|Brauer|canonique')

add('N008','B. Pointed projective bundles and stratifications','Automorphisms of a nonsplit extension have an obstruction','own idea',
'002:L13-23;019:L13-15',r'\lambda c=c',
r'''Confidence: high, because an automorphism of Ω extends to the extension precisely when it preserves its class in Ext¹(O,Ω); the kernel of the resulting map on extension automorphisms is Hom(O,Ω). Thus a full semidirect-product description by Aut(Ω) and Γ(Ω) is valid in the split model but need not describe the global automorphism group of an arbitrary extension.''',
'Qualifies Hua, hua_project/159.modern.tex, §“Trois descriptions d’un même objet”, using the manuscript’s own class-preservation argument in §“Les automorphismes du couple (P,σ)” (our scan 19); this is a context correction, not a transcription change.',
r'Aut|semi.direct|classe|lambda|automorphismes du couple',check='targeted proof check',outcome='Checked extension-class obstruction; no claim that all Aut(Ω) lifts globally.')

add('N009','B. Pointed projective bundles and stratifications','The fractional action controls the later coefficients','unpursued implication',
'004:L33-47;005:L3-24',r'\frac{\omega}{1+a}',
r'''The action on the formal coordinate is fractional linear, and its homogeneous degree-n part is multiplied by (1+a)^(-n). Expanding only through degree n+1 yields the coefficient −n used on scan 7, so later missing-looking integers should be checked against this earlier explicit action rather than normalized silently.''',
'Restates Hua, hua_project/159.modern.tex, §§“Le complété formel le long de la section, et l’action de Ω” and “La conséquence graduée”, and supplies a cross-check relevant to the distinct associated-graded issue on scans 28 and 33.',
r'compl.t. formel|cons.quence gradu|1\+a|n v_n',check='targeted proof check',outcome='Expanded (1+a)^(-n) to first order; checked the coefficient -n.')

add('N010','B. Pointed projective bundles and stratifications','The tautological line has a different action from the algebra','unpursued implication',
'005:L26-48;006:L20-55',r'u_{a*}^{\widehat L}(g)=(a+1)u_{a*}(g)',
r'''The extra factor 1+a is forced by compatibility with the quotient E⊗Ŝ→L̂, so the weight on a homogeneous degree-n element of L̂ is 1−n. Keeping this action separate from the algebra action prevents losing the twist when comparing jet extensions or constructing a second-order operator.''',
'Restates Hua, hua_project/159.modern.tex, §“Le complété formel le long de la section, et l’action de Ω”, and adds a concrete normalization constraint for RESULTS_STATE.md entry MPL_93_002-046 P01, whose source formula is not supplied.',
r'tautologique|1-n|1\+a|P01|compl.t. formel',check='targeted proof check',outcome='Checked equivariance of the quotient using the displayed fractional action.',results=('MPL_93_002-046 P01',))

add('N011','B. Pointed projective bundles and stratifications','Successive jet extensions remember a multiple of the torsor','unpursued implication',
'007:L10-36',r'-nv_n',
r'''The extension Jⁿ/Jⁿ⁺² is the pushout of the Ω-torsor along −n times multiplication, with its sign tied to the stated action convention. In positive characteristic the scalar n can vanish, so one such graded extension can lose information even though the whole formal action remains nontrivial.''',
'Restates Hua, hua_project/159.modern.tex, §“La conséquence graduée”, and adds an elementary characteristic-p warning relevant to the unrestricted question in §“Les deux données, et l’identification qu’elles forcent”.',
r'cons.quence gradu|v_n|caract.ristique|deux donn',check='targeted proof check',outcome='Checked first-order expansion and vanishing of the scalar n in characteristic dividing n.')

add('N012','B. Pointed projective bundles and stratifications','Why r+1 appears, and why rank one is separate','own idea',
'008:L25-29;009:L3',r'r+1 inv.',
r'''Confidence: high: the canonical contraction C:V*⊗Sym²V→V sends λ⊗vw to λ(v)w+λ(w)v, and for m(a)(v)=av it gives C(m(a))=(r+1)a. This proves the displayed sufficient splitting condition, while in rank one m itself is an isomorphism even when two is not invertible; research_checks/basic_report.md §B1 and its certificate record the check.''',
'Supplies the contraction behind Hua, hua_project/159.modern.tex, §“Les deux données, et l’identification qu’elles forcent”; it does not settle the next all-characteristic question.',
r'r\+1|trace|contraction|dimension|deux donn',check='independent re-proof',outcome='Proved C∘m=(r+1)id, with a separate rank-one argument; finite-rank certificate accompanies general proof.')

add('N013','B. Pointed projective bundles and stratifications','The unanswered canonical-object question is about the torsor','self-flagged: a step he himself marks as unverified',
'009:L3-7',r'est-il vrai ... $\mathcal{T}$ est can. déterminé par $X/S$, sans condit. de dim ni de car. ?',
r'''The explicit question asks whether the underlying torsor T is canonically determined when an infinite projective connection is already given, without the stated dimension or characteristic restrictions. It does not ask whether X carries a unique entire projective connection, and the later torsor of quadratic differentials would contradict that stronger interpretation rather than answer the actual question.''',
'Differs from Hua, hua_project/159.modern.tex, §§“Les deux données, et l’identification qu’elles forcent” and “Ce qui ne s’articule pas”, where the object of canonicity is broadened to the projective connection itself; no all-characteristic resolution of the narrower question is established here.',
r'canoniquement|canonique|sans restriction|dimension|caract.ristique')

add('N014','B. Pointed projective bundles and stratifications','The manuscript deliberately replaces connections by stratifications','withdrawn in the same text',
'009:L7;010:L17-25',r'\deleted{connexion} \inserted{stratification}',
r'''The replacements on scan 9, continued on scan 10, matter: the transported structure on principal parts does not preserve the augmentation, and integrability is phrased as extension to the whole projective bundle after forgetting the marked section. In characteristic p an ordinary integrable connection alone does not recover all the higher stratification data, as the explicit comparison in N070 demonstrates.''',
'Adds the manuscript’s revision history to Hua, hua_project/159.modern.tex, §“Intégrabilité, et l’écriture en coordonnées”, and restricts the p-curvature speculation in context/README.md; the higher-stratification comparison in N070 is our calculation, not manuscript content.',
r'stratification|int.grabilit|courbure|Cartier',results=('S20',))

add('N015','B. Pointed projective bundles and stratifications','The scalar-ring notation on scans 9–10 remains a reading question','reading question',
'009:L11-16;009:L34-36;010:L6-19',r'\mathcal{O}_S[[\delta f_1,\ldots,\delta f_r]]',
r'''The frozen transcription has O_S in several local power-series expressions, whereas a principal-parts algebra on X normally has O_X as its scalar sheaf. This makes O_X a mathematically motivated alternative for future image review, but the context cannot authorize replacing the visible subscript after the freeze.''',
'Differs from the normalized O_X conventions in Hua, hua_project/159.modern.tex, §§“Conventions, valables pour tout le dossier” and “Intégrabilité, et l’écriture en coordonnées”; the supplied interpretation is recorded as the source of the alternative, not as evidence that the ink was O_X.',
r'cal O._X|mathcal.O._X|coordonn|Conventions')

add('N016','B. Pointed projective bundles and stratifications','The coordinate test for integrability stops before its criterion','unproved claim',
'009:L9-38;010:L3-25',r'Posant',
r'''The formal coordinate transformations F_i and Φ_i transport the canonical structure, but scan 10 ends after “Posant” before an explicit coefficient criterion for descent to the projective bundle is supplied. A continuation would need to identify which transported formal automorphisms are projective-linear and then check the cocycle condition, especially if higher-dimensional or positive-characteristic conclusions are intended.''',
'Agrees with the incompleteness noticed in Hua, hua_project/159.modern.tex, §§“Intégrabilité, et l’écriture en coordonnées” and “Les reprises, et leur ordre”; the later rank-one formal theorem is a different, more restricted problem.',
r'Posant|interromp|inachev|Int.grabilit|reprises')

add('N017','B. Pointed projective bundles and stratifications','The cut-off symmetric-algebra formula is not a completed claim','reading question',
'003:L9-12;004:L26-31',r'\operatorname{Sym}^n(',
r'''Scan 3 ends inside a symmetric-algebra expression; the next leaf restarts the setup and later gives the completed symmetric algebra in the split case. The second passage helps identify the topic but does not supply the missing ink of the earlier unfinished expression.''',
'Differs in documentary scope from the completed exposition in Hua, hua_project/159.modern.tex, §§“Les reprises, et leur ordre” and “Le complété formel le long de la section, et l’action de Ω”; no completion has been inserted in the transcription.',
r'Sym|reprises|compl.t. formel')

add('N018','C. The Hodge-theoretic interlude','The symplectic extension is a distinct source of torsors','unpursued implication',
'011:L12-48',r'l’orthogonal de $\Omega$ est $\Omega$',
r'''The de Rham extension has an alternating perfect pairing with Ω as its own orthogonal, and a choice of splitting leaves an alternating form on the quotient. This is a torsor problem over the base of a family of curves, so its relation to the pointed projective bundle on an individual curve needs an actual construction rather than an identification from repeated use of Ω.''',
'Restates Hua, hua_project/159.modern.tex, §“La cohomologie de de Rham d’une famille de courbes”, while retaining the distinction between the Hodge bundle Ω and the relative differential line ω emphasized by the manuscript’s notation.',
r'cohomologie de de Rham|altern.e|orthogonal|Hodge')

add('N019','C. The Hodge-theoretic interlude','Isotropic splittings exist locally even in characteristic two','own idea',
'011:L40-48;012:L3-8',r'formes symétriques sur $\check\Omega$',
r'''Confidence: high: after choosing a local splitting, the obstruction matrix is alternating, and a strict triangular matrix u cancels it through u−uᵗ without division by two. The remaining freedom is a symmetric matrix, giving the stated Γ²Ω-torsor locally; this does not assert a global splitting, and the general argument plus finite-field checks are in basic_report.md §B2.''',
'Checks and sharpens Hua, hua_project/159.modern.tex, §“La cohomologie de de Rham d’une famille de courbes”; characteristic-two restrictions in the subsequent multiplication map should not be imported into this local symplectic splitting argument.',
r'splittings|sym.triques|caract.ristique|cohomologie de de Rham',check='independent re-proof',outcome='Proved local surjectivity of u→u-uᵗ and symmetric kernel over arbitrary characteristic; finite cases exhaustively checked.')

add('N020','C. The Hodge-theoretic interlude','Γ² and Sym² have different integral meanings','own idea',
'012:L3-5;013:L9-14',r'\Gamma^2\Omega',
r'''Confidence: high: for finite free V, Γ²V identifies with symmetric invariant tensors, while Sym²V is the quotient by permutation relations; the natural map sends an off-diagonal invariant to twice its product and a diagonal invariant to its square. Thus that map is invertible after inverting two and kills the off-diagonal generators in characteristic two, which explains a genuine condition on the arrow written on scan 13 without changing Γ² to Sym².''',
'Builds on Hua’s explicit Γ²-versus-Sym² distinction in hua_project/159.modern.tex, §“La cohomologie de de Rham d’une famille de courbes”, and clarifies which multiplication arrow carries the characteristic qualification in §“Le compte des quadriques”; basic_report.md §B2 gives the calculation.',
r'Gamma|Sym|quadriques|sym.trique',check='independent re-proof',outcome='Checked invariant-to-coinvariant map on its basis, including the factor 2.')

add('N021','C. The Hodge-theoretic interlude','The Kodaira–Spencer arrow has tangent source and symmetric target','reading question',
'012:L14-26',r'\mathcal{T}_{S/T}\longrightarrow\Gamma^2\check\Omega',
r'''The frozen reading is T_{S/T}→Γ²Ω̌, obtained from Ω→Ω̌⊗Ω¹_{S/T}, and the text explicitly discusses principally polarized abelian varieties. Landesman’s algebraic proof of infinitesimal Torelli identifies the dual map with multiplication of canonical differentials [L3, Theorem 4.3], supporting this variance without supplying evidence for a different handwritten glyph.''',
'Contradicts the specific variance warning in Hua, hua_project/159.modern.tex, §“Gauss–Manin, et ce que la page 11 ne livre pas”, which reads a cotangent source and an exterior-square target; the present first-pass image reading already had T and Γ² before that context was opened.',
r'variance|Lambda|Gamma|Gauss.Manin|cotangent')

add('N022','C. The Hodge-theoretic interlude','The nonhyperelliptic condition is explicitly on the page','reading question',
'012:L22-26;013:L10-14',r'Épi (cas non hyperelliptique) (car.\ne2)',
r'''The surjectivity arrow is expressly qualified by the nonhyperelliptic case and characteristic different from two; the condition was not supplied by this research commentary. Max Noether’s multiplication theorem supplies the relevant ordinary symmetric-square surjectivity [L4, introduction and theorem], with the extra factor-two issue of N020 for the invariant-square map actually drawn.''',
'Contradicts Hua, hua_project/159.modern.tex, §“Le compte des quadriques”, insofar as it says the manuscript does not state the nonhyperelliptic hypothesis; this is a documentary correction to the modernized reading.',
r'hyperellipt|quadriques|Noether')

add('N023','C. The Hodge-theoretic interlude','The numerical count requires the surjectivity hypothesis','unpursued implication',
'013:L10-14',r'\frac12(g-2)(g-3)',
r'''The displayed subtraction is correct, and for a nonhyperelliptic curve in the stated setting it computes the kernel dimension of multiplication on quadratic canonical forms. Genus two is a useful boundary case: it is hyperelliptic but ordinary Sym² multiplication is an isomorphism, while for hyperelliptic genus g≥3 its image has dimension 2g−1, so the same subtraction is not the kernel dimension.''',
'Refines Hua, hua_project/159.modern.tex, §“Le compte des quadriques”, using the actually present hypotheses and the standard hyperelliptic monomial calculation; basic_report.md §B4 checks the arithmetic, and [L3, §4] supplies the tangent-map identification.',
r'quadriques|g-2|g-3|hyperellipt',check='targeted proof check',outcome='Checked arithmetic and hyperelliptic products x^i dx/y times x^j dx/y, with exponents 0 through 2g-2.')

add('N024','C. The Hodge-theoretic interlude','A possible Gauss–Manin bridge still needs a rank-two construction','own idea',
'012:L28-35;013:L16-67',r'(\mathcal{DR})_X',
r'''Confidence: medium as a research direction, because the kernel of evaluation Ω_X→ω_X and its symplectic orthogonal suggest a rank-two quotient of the pulled-back de Rham bundle. To obtain a projective connection one must specify the quotient and twists, show that the needed connection descends or choose a replacement, and establish transversality; none of those requirements follows merely from the displayed inclusion chain.''',
'Adds an explicit list of missing maps to Hua, hua_project/159.modern.tex, §§“Gauss–Manin, et ce que la page 11 ne livre pas” and “Ce qui ne s’articule pas”, and bears on the comparison requested in RESULTS_STATE.md, MPL_93_002-046 P09.',
r'Gauss.Manin|orthogonal|rang deux|P09|ne s.articule',results=('MPL_93_002-046 P09',))

add('N025','C. The Hodge-theoretic interlude','The final vanishing fragment needs its actual degree hypothesis','reading question',
'013:L50-67',r'R^1f_*(M\otimes\omega^n)=0',
r'''The short condition following the vanishing formula and the later graded-algebra scratchwork remain uncertain readings, so no exact uniform vanishing theorem is extracted from them. For a line bundle M on a smooth proper curve, Serre duality instead supplies the concrete sufficient condition deg(M)+n(2g−2)>2g−2, and a family statement also needs the appropriate fiberwise and base-change hypotheses.''',
'Adds a bounded interpretation to Hua, hua_project/159.modern.tex, §§“Le compte des quadriques” and “Les reprises, et leur ordre”, which do not settle the ambiguous final scratchwork; the sufficient condition is an independent comparison, not a proposed transcription correction.',
r'vanish|annul|R\^1|quadriques|reprises',check='targeted proof check',outcome='Applied Serre duality and negative-degree vanishing only to the explicitly specified line-bundle comparison, not to uncertain manuscript notation.')

add('N026','D. Flat bundles, projective structures, and monodromy','The dimension issue is a change of moduli problem','reading question',
'015:L7-18;016:L41-49;017:L3-16;018:L26-35',r'fibrés projectifs analytiques à connexion plate',
r'''Scans 15–17 discuss flat projective bundles without a chosen transverse section; scan 18 separately introduces projective connections with a nonstationary section. For fixed X the first deformation problem has dimension 6g−6 at a point with vanishing infinitesimal centralizer, whereas the projective-structure space has dimension 3g−3; over the moduli of curves these become 9g−9 and 6g−6 respectively on the appropriate smooth loci.''',
'Contradicts the proposed dimension repair in Hua, modernised reading of cote 159, hua_project/159.modern.tex, §“L’anomalie de la page 15, et ce que la cohérence demande”: the written relative dimension 6g−6 is consistent with the flat-bundle problem actually defined, and should not be changed to the oper-fiber dimension.',
r'anomalie|6g-6|3g-3|relative|non.stationnaire',check='targeted proof check',outcome='Separated the two definitions and checked dimensions using the manuscript Euler characteristic and Riemann–Roch for K².')

add('N027','D. Flat bundles, projective structures, and monodromy','Dimension-zero automorphisms need not be trivial','unproved claim',
'015:L14-34;016:L36-47',r'\operatorname{Aut}^{\unsure{\xi|\zeta}}(P)=1',
r'''The claimed passage from dimension zero to the trivial automorphism group fails for the flat-bundle problem: the subgroup V₄ generated by z↦−z and z↦1/z in PGL₂(C) has centralizer V₄. A surface group of genus at least two surjects onto V₄, so the associated flat bundle has no infinitesimal automorphisms but has nontrivial finite ones; the explicit centralizer calculation is checked in monodromy_report.md.''',
'Rechecks and credits the same counterexample already given by Hua, hua_project/159.modern.tex, §“L’espace, et le critère de non-dégénérescence”; this is confirmation of a supplied objection, not a new discovery.',
r'Klein|V_4|dimension.*z.ro|d.g.n.rescence',check='refuted, with refined statement id: N028',outcome='Refuted Aut=1 from zero-dimensionality by V4; correct local consequence is absence of infinitesimal automorphisms.')

add('N028','D. Flat bundles, projective structures, and monodromy','The exclusion of additive and multiplicative reductions controls only the identity component','unpursued implication',
'015:L14-34;016:L7-9',r'G_m\subset GP(1)',
r'''The centralizer argument can force the Lie algebra of automorphisms to vanish, but it must retain a separate condition excluding finite centralizers if a rigid set-valued moduli functor is intended. V₄ is not contained in an additive or multiplicative one-dimensional subgroup, so it passes the stated exclusions while violating the stronger conclusion.''',
'Restates the distinction in Hua, hua_project/159.modern.tex, §§“L’espace, et le critère de non-dégénérescence” and “Le calcul de dimension”, with the finite subgroup checked explicitly rather than silently strengthening the manuscript’s hypotheses.',
r'centralisateur|Klein|non.d.g.n|dimension',check='targeted proof check',outcome='Checked V4 passes the two subgroup exclusions and has zero-dimensional but nontrivial centralizer.')

add('N029','D. Flat bundles, projective structures, and monodromy','The 6g−6 calculation survives the finite-automorphism objection','unpursued implication',
'016:L4-43',r'\dim H^1_{DR}(X,\unsure{\mathfrak g})=2\dim H^0_{DR}(X,\unsure{\mathfrak g})+(6g-6)',
r'''For the rank-three adjoint local system on a compact complex curve, Euler characteristic is 3(2−2g) and the invariant pairing gives h²=h⁰, hence h¹=2h⁰+6g−6. Thus H⁰=0 gives the displayed tangent dimension and H²=0, even when a finite stabilizer remains; this is a calculation for the deformation complex, not proof of a smooth coarse scheme at a quotient singularity.''',
'Checks and restates Hua, hua_project/159.modern.tex, §“Le calcul de dimension”, while preventing its use to justify the stronger representability assertion challenged in the preceding subsection.',
r'6g-6|Euler|dualit|calcul de dimension',check='independent re-proof',outcome='Reproved adjoint Euler-characteristic dimension under the explicit complex/characteristic-zero smooth-proper hypotheses.')

add('N030','D. Flat bundles, projective structures, and monodromy','Representability is explicitly left for further proof','self-flagged: a step he himself marks as unverified',
'016:L47-49',r'Sans doute peut-on prouver la représentabilité relative',
r'''The exclamation “donc un foncteur représentable !” is followed by a qualified expectation allowing Artin algebraic spaces, so representability should not be reported as proved on this page. Even after correcting the stabilizer hypothesis, a proof needs an algebraicity theorem and the relevant descent and finiteness conditions; infinitesimal smoothness and objectwise rigidity alone are not that theorem.''',
'Agrees with the caution in Hua, hua_project/159.modern.tex, §§“Le calcul de dimension” and “L’espace, et le critère de non-dégénérescence”, and preserves the explicit qualification instead of treating it as a concluded result.',
r'repr.sentabilit|Artin|rigide|formellement lisse')

add('N031','D. Flat bundles, projective structures, and monodromy','The quotient notation needs a choice of moduli category','unproved claim',
'017:L5-18',r'\underline{\operatorname{Hom}}_{\operatorname{gr}}(\pi,H)',
r'''A finite presentation of the surface group gives an affine representation variety by the product-of-commutators equation, but trivial centralizer does not force an orbit to be closed in the full affine representation variety, as required for a direct identification with points of its reductive GIT quotient. A representation Zariski-dense in an upper-triangular Borel gives an example: its diagonal limit leaves the trivial-centralizer locus, so its orbit can be closed in that smaller locus while nonclosed in the full variety; basic_report.md §B5 makes the distinction explicit.''',
'Adds a quotient qualification to Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; it does not invalidate the standard analytic Riemann–Hilbert comparison in its proper category.',
r'quotient|Hom|caract.res|tableau analytique',check='targeted proof check',outcome='Checked upper-triangular nonclosed-orbit example; trivial centralizer does not imply GIT stability.')

add('N032','D. Flat bundles, projective structures, and monodromy','The Riemann–Hilbert algebraicity doubt has mathematical substance','self-flagged: a step he himself marks as unverified',
'017:L16-17',r'n’est pas ... sans doute ... algébrique !',
r'''The marked expectation concerns the comparison from de Rham bundles to representations, not the elementary algebraicity of the representation variety. On the fixed-curve oper locus, algebraic dimension 3g−3 together with Zariski density of a Bers slice in the 6g−6 Betti component obstructs algebraicity of that comparison; the argument and its scope are given in monodromy_report.md using Dumas–Kent [L6].''',
'Supports the direction of Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, while adding an actual obstruction and distinguishing it from the separate mapping-class-action expectation.',
r'Riemann|alg.brique|monodromie|tableau analytique',check='targeted proof check',outcome='Checked dimension obstruction using the stated Zariski-density theorem; no claim that every possible restricted comparison is nonalgebraic.')

add('N033','D. Flat bundles, projective structures, and monodromy','The transported outer action is a separate unresolved question','self-flagged: a step he himself marks as unverified',
'018:L3-10',r'sans doute cette opération n’est pas algébrique',
r'''On the Betti representation variety, precomposing by a fixed automorphism of π is algebraic because it replaces each generator matrix by a finite word in the old matrices and their inverses. Transporting this action through a nonalgebraic Riemann–Hilbert map does not automatically prove the resulting de Rham action nonalgebraic, so the manuscript’s expectation is left unresolved in that generality.''',
'Refines Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, by separating the checked word-map statement from the unproved transported-action claim; it does not settle RESULTS_STATE.md entry LM1 D.7 on Galois/GT comparisons.',
r'Out|automorphismes ext.rieurs|alg.brique|LM1 D\.7',check='targeted proof check',outcome='Proved Betti word-map algebraicity; recorded transported de Rham nonalgebraicity as not proved.',results=('LM1 D.7',))

add('N034','D. Flat bundles, projective structures, and monodromy','Canonical Fuchsian uniformization is real analytic','reading question',
'018:L12-24',r'morphisme analytique injectif',
r'''The natural uniformizing representation depends real analytically on Teichmüller space and lands in a totally real Fuchsian locus; it is not a nonconstant holomorphic map into the complex character variety. The word “analytique” therefore needs this distinction, whereas a holomorphic Bers section requires an additional choice and is a different construction [L7, §2].''',
'Qualifies Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, where the analytic category is not separated at this point; no word in the frozen text is changed.',
r'analytique|Teichm|uniformis|Bers',check='targeted proof check',outcome='Checked real-analytic/nonholomorphic distinction for the canonical Fuchsian section.')

add('N035','D. Flat bundles, projective structures, and monodromy','The manuscript suspects nonconstructibility, not constructibility','self-flagged: a step he himself marks as unverified',
'018:L24',r'On suspecte ... pas un sous-ens. constructible',
r'''The sentence retains the negation and the tentative verb despite a rewritten subjunctive or conditional phrase. Its nonconstructibility expectation is supported for the Fuchsian locus: a positive-dimensional complex constructible set contains a positive-dimensional complex analytic piece, which cannot lie in this totally real locus; the same local argument survives an analytic Riemann–Hilbert identification.''',
'Contradicts the positive constructibility/algebraicity reading in Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; monodromy_report.md gives the targeted proof and [L7] supplies the geometric input.',
r'constructible|suppose|suspect|alg.brique',check='targeted proof check',outcome='Checked negative reading against frozen text and proved nonconstructibility from total reality and positive dimension.')

add('N036','D. Flat bundles, projective structures, and monodromy','The invariant domain is not unique without an orientation choice','unproved claim',
'018:L24',r'il sera unique',
r'''A cocompact torsion-free Fuchsian subgroup preserves both the upper and lower half-planes, acts freely on both, and has compact quotient on both. Thus the literal uniqueness assertion requires a chosen oriented component or compatible complex marking; the two domains provide a direct counterexample otherwise.''',
'Corrects the unqualified uniqueness repeated in Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; the two-component geometry is also explicit in [L7, §2].',
r'unique|domaine|homog.ne|tableau analytique',check='refuted, with refined statement id: N036.orientation',outcome='Refuted bare uniqueness by the two half-planes; refined statement requires a chosen oriented component.')

add('N037','D. Flat bundles, projective structures, and monodromy','The fixed-curve projective-connection space is an affine torsor','unpursued implication',
'018:L26-35;027:L6-12',r'C’est un torseur sur le vectoriel de dim finie',
r'''For fixed X, differences of projective connections are quadratic differentials, so the space is a torsor under H⁰(X,K²), of dimension 3g−3 for g≥2 by Riemann–Roch and H¹(K²)=H⁰(K⁻¹)*=0. A torsor supplies no preferred origin, which is why “canonical underlying bundle” does not imply “canonical chosen connection”.''',
'Restates Hua, hua_project/159.modern.tex, §§“Le tableau analytique : monodromie, Teichmüller, uniformisation” and “L’énoncé final”, and bears on RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; [L1, §3.1] provides the modern comparison.',
r'torseur|quadratique|3g-3|159-formal-rigidity',check='targeted proof check',outcome='Checked Riemann–Roch dimension and distinguished affine torsor from chosen origin.',results=('159-formal-rigidity-quadratic-torsor',))

add('N038','D. Flat bundles, projective structures, and monodromy','The manuscript asserts and argues fixed-X injectivity','reading question',
'018:L33-40;019:L3-20;021:L13-16',r'En fait c’est un ... mono',
r'''Scan 18 asserts that the forgetful map is a monomorphism, and scans 19–21 pursue an automorphism argument concluding that distinct projective connections are not isomorphic when two is invertible. Over a compact complex curve of genus at least two, pointwise injectivity can be independently proved by uniqueness of the negative section, and Gallo–Kapovich–Marden give the fixed-X proper-embedding statement [L5, §11.4]; the scheme-theoretic family-level word “mono” requires that stronger functorial argument as well.''',
'Contradicts the historical description “without answering” in RESULTS_STATE.md, Hua finding 159-monodromy-injectivity-question, and Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; it does not claim every intermediate handwritten computation is sound.',
r'injectiv|sans r.ponse|159-monodromy-injectivity|mono',check='targeted proof check',outcome='Verified an assertion and subsequent argument are present; independently checked fixed-X pointwise injectivity, without claiming a complete scheme-level proof from the page.',results=('159-monodromy-injectivity-question',))

add('N039','D. Flat bundles, projective structures, and monodromy','Injectivity is not a statement about varying complex structures','unpursued implication',
'018:L26-35',r'sur $X$',
r'''Fixing X is essential: holonomy on the full space of marked projective structures over Teichmüller space has nontrivial fibers, with grafting providing distinct structures with the same holonomy [L8, introduction and §2.4]. That phenomenon does not refute the fixed-X statement checked in N038.''',
'Adds the scope distinction needed when using Hua, findings register, 159-monodromy-injectivity-question, in RESULTS_STATE.md, and Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”.',
r'fix.e|injectiv|Teichm|159-monodromy-injectivity',results=('159-monodromy-injectivity-question',))

add('N040','D. Flat bundles, projective structures, and monodromy','The negative section gives an independent injectivity argument','own idea',
'019:L3-15;021:L13-16',r'anti-ample',
r'''Confidence: high under the smooth compact complex genus-at-least-two hypotheses: a transverse section of a flat projective bundle has normal bundle T_X and self-intersection 2−2g. In a ruled surface, if S is negative and S′≡S+dF is a distinct section, then 0≤S·S′=S²+d and hence (S′)²=S²+2d≥−S²>0; therefore the negative section is unique and a flat-bundle isomorphism preserves the oper section, proving fixed-X pointwise injectivity without relying on the disputed coordinate signs.''',
'Independently checks the geometric mechanism behind Hua, hua_project/159.modern.tex, §“Les automorphismes du couple (P,σ)”, and refines the treatment of finding 159-monodromy-injectivity-question in RESULTS_STATE.md; monodromy_report.md gives the equivalent quotient-line degree proof.',
r'anti.ample|n.gati|automorphismes du couple|159-monodromy-injectivity',check='independent re-proof',outcome='Reproved uniqueness of a negative section on a ruled surface and fixed-X pointwise injectivity.',results=('159-monodromy-injectivity-question',))

add('N041','D. Flat bundles, projective structures, and monodromy','The local question is revised from two connections to one','withdrawn in the same text',
'019:L5-10;019:L20;021:L13-16',r'\deleted{deux}\inserted{une}',
r'''Scan 19 cancels an earlier uniqueness sentence and a moduli diagram, then edits a comparison of c and c′ into a question about an automorphism of one connection. Scan 21 nevertheless states both consequences—distinct connections are not isomorphic and one connection has no automorphisms—so the local revision should not be described as abandonment of injectivity.''',
'Adds the sequence of revisions to Hua, hua_project/159.modern.tex, §§“Les automorphismes du couple (P,σ)” and “Le calcul en coordonnées, et la formule encadrée”, and further qualifies RESULTS_STATE.md finding 159-monodromy-injectivity-question.',
r'automorphismes du couple|injectiv|connexions distinctes|formule encadr',results=('159-monodromy-injectivity-question',))

add('N042','D. Flat bundles, projective structures, and monodromy','The scan 20 formulas have a literal sign conflict','reading question',
'020:L12-19;020:L24;020:L51-58',r'c_{D_t}(1)=1',
r'''The generator formula gives c_D(1)=1, whereas substitution λ=ν=0, μ=1 into the subsequent general formula gives −1; the bracket [−ω,1] also receives inconsistent displayed values later on the page. These are concrete consistency problems in characteristic different from two, so no exact Schwarzian normalization should be extracted from that calculation before resolving the convention or reading; basic_report.md §B3 records the substitution.''',
'Adds a literal consistency check to Hua, hua_project/159.modern.tex, §“Le calcul en coordonnées, et la formule encadrée”, and bears directly on RESULTS_STATE.md entry MPL_93_002-046 P01; the frozen signs are retained.',
r'formule encadr|D_t|Schwarz|P01',check='computation or formal certificate',outcome='Substitution gives +1 and -1 for the same generator; no correction selected.',results=('MPL_93_002-046 P01',))

add('N043','D. Flat bundles, projective structures, and monodromy','The factor two tests preservation of the normalized form','unpursued implication',
'020:L41-46;021:L3-15',r'2\omega=0',
r'''In the explicit convention ∂_x+(1+bt+ct²)∂_t, the change z=t/(1+at) produces the linear coefficient b−2a and quadratic coefficient a²−ab+c−a′. Thus preserving a prescribed zero linear coefficient forces 2a=0; this independently checks the kind of obstruction used on scan 21 without validating all of scan 20’s signs or replacing the operator on ω by exterior differentiation.''',
'Differs from Hua, hua_project/159.modern.tex, §“Le calcul en coordonnées, et la formule encadrée”, insofar as it reads a dω=0 condition and suggests a translation action of H⁰(K) on the normalized projective-connection torsor; basic_report.md §B3 gives the declared convention and symbolic certificate.',
r'd\\omega|d_\\omega|2\\omega|formule encadr|translations',check='computation or formal certificate',outcome='Symbolically verified the stated Möbius change formula and its linear coefficient -2a; normalization explicitly declared.')

add('N044','D. Flat bundles, projective structures, and monodromy','No automorphisms is a conclusion for opers under the stated hypotheses','unpursued implication',
'019:L13-20;021:L13-16',r'a fortiori $2\omega=0$',
r'''Once the underlying pointed bundle has the nonzero extension class used on scan 19, its residual automorphisms are parametrized by one-forms, and scan 21’s 2ω obstruction eliminates them when two is invertible. This oper rigidity does not retrospectively eliminate the finite centralizers of arbitrary flat bundles on scans 15–16.''',
'Separates the two moduli problems inside Hua, hua_project/159.modern.tex, §§“Les automorphismes du couple (P,σ)” and “L’anomalie de la page 15, et ce que la cohérence demande”; the distinction is also needed for RESULTS_STATE.md finding 159-monodromy-injectivity-question.',
r'pas d.automorphismes|automorphismes du couple|anomalie|159-monodromy-injectivity',check='targeted proof check',outcome='Checked rigidity mechanism with nonzero extension and invertible 2; did not extend it to all flat bundles.',results=('159-monodromy-injectivity-question',))

add('N045','D. Flat bundles, projective structures, and monodromy','The horizontal-section question is answered later on the same leaf','self-flagged: a step he himself marks as unverified',
'021:L18-34;022:L3-18',r'question : y en a-t-il ... horizontales ?; Non',
r'''The marginal question is followed by “Non” and a degree argument continuing on scan 22, so it is not an unanswered conjecture in the finished sequence of leaves. In a determinant-normalized rank-two oper, the oper line has degree g−1 while a horizontal line has degree zero; its map to the negative-degree quotient vanishes, forcing it into the oper line, and the two saturated line subbundles then coincide, contradicting transversality.''',
'Restates and checks Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, and the mechanism behind RESULTS_STATE.md finding 159-no-reduction-monodromy-dense, with characteristic-zero degree-zero input made explicit.',
r'horizontale|degr.s|159-no-reduction-monodromy-dense|g-1',check='independent re-proof',outcome='Reproved the horizontal-line contradiction in characteristic zero; the question is answered in manuscript scans21–22.',results=('159-no-reduction-monodromy-dense',))

add('N046','D. Flat bundles, projective structures, and monodromy','A Borel reduction is excluded by the horizontal-line argument','unpursued implication',
'022:L3-18',r'un groupe de Borel',
r'''A horizontal Borel reduction of a flat PGL₂ bundle gives a horizontal point in each projective fiber and hence the forbidden horizontal section. This establishes the Borel exclusion under the smooth-projective, genus-at-least-two, characteristic-zero hypotheses used in the degree argument.''',
'Checks and restates Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, and RESULTS_STATE.md finding 159-no-reduction-monodromy-dense; it is the first exclusion, not by itself the full density theorem.',
r'Borel|degr.s|159-no-reduction-monodromy-dense',check='targeted proof check',outcome='Checked equivalence of a horizontal Borel reduction and a horizontal section in the projective-line bundle.',results=('159-no-reduction-monodromy-dense',))

add('N047','D. Flat bundles, projective structures, and monodromy','The torus-normalizer step uses an étale double cover','unpursued implication',
'022:L18-24',r'normalisateur d’un tore',
r'''A reduction to the torus normalizer becomes a torus reduction after an étale cover of degree at most two, and a torus reduction supplies fixed projective points. The pulled-back curve still has genus at least two by the étale Riemann–Hurwitz formula, so the horizontal-section contradiction applies there as well.''',
'Checks and restates Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, and the corresponding part of RESULTS_STATE.md finding 159-no-reduction-monodromy-dense.',
r'normalisateur|.tale|159-no-reduction-monodromy-dense',check='independent re-proof',outcome='Checked passage through N(T)/T of order2 and preservation of genus≥2 on finite étale covers.',results=('159-no-reduction-monodromy-dense',))

add('N048','D. Flat bundles, projective structures, and monodromy','The finite algebraic subgroups require one more argument','unproved claim',
'022:L23-24;023:L2-6',r'sous-groupe ... distinct de $H$',
r'''Excluding a Borel and a torus normalizer does not on its own exclude the finite tetrahedral, octahedral, or icosahedral groups. If monodromy were finite, its kernel would define a finite étale cover on which the flat projective bundle is trivial and therefore has horizontal sections, again contradicting N045; this completes the characteristic-zero complex density proof.''',
'Credits and rechecks the same completion in Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, paragraph “Une lacune, et comment la combler”, rather than claiming it as new; it refines the compressed implication in RESULTS_STATE.md finding 159-no-reduction-monodromy-dense.',
r'fini|icosa|densit.|159-no-reduction-monodromy-dense',check='independent re-proof',outcome='Supplied finite-cover exclusion and checked the remaining proper algebraic subgroup cases of PGL2(C).',results=('159-no-reduction-monodromy-dense',))

add('N049','D. Flat bundles, projective structures, and monodromy','The density conclusion is sound with its characteristic-zero scope','self-flagged: a step he himself marks as unverified',
'022:L23-24;023:L2-6',r'de car nulle ?; Zariski-dense',
r'''Over C, the completed degree and finite-cover argument proves Zariski density for the monodromy of an unbranched projective structure on a compact curve of genus at least two. The author’s characteristic question should nevertheless remain visible, and a proposed extension to positive characteristic needs a different proof and a precise choice between a connection and a stratification. Irreducibility, Zariski density, and Kleinian nonelementarity are different conditions for arbitrary representations; monodromy_report.md §MC13 gives counterexamples to conflating them.''',
'Supports the characteristic-zero conclusion, with the finite-subgroup completion credited to Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, paragraph “Une lacune, et comment la combler”, and rechecks RESULTS_STATE.md finding 159-no-reduction-monodromy-dense without promoting an unrestricted variant.',
r'caract.ristique|densit.|159-no-reduction-monodromy-dense',check='targeted proof check',outcome='Validated complex characteristic-zero density under stated hypotheses; no positive-characteristic theorem claimed.',results=('159-no-reduction-monodromy-dense',))

add('N050','D. Flat bundles, projective structures, and monodromy','The degree-zero step fails for ordinary connections in characteristic p','own idea',
'022:L3-16;022:L23',r'\deg L=g-1',
r'''Confidence: high for the obstruction to this proof: in characteristic p, a Frobenius pullback F*L has a canonical flat connection and degree p·deg(L), which need not be zero as an integer. Thus the rank-one flat-connection input used on scan 22 cannot simply be carried into characteristic p; this observation neither constructs a counterexample to every stronger stratified statement nor computes a p-curvature for the manuscript’s object.''',
'Adds a concrete limit to Hua, hua_project/159.modern.tex, §“La densité de Zariski, et où la situer”, and to S20 in context/README.md; Katz [L2, §5, Cartier descent] supplies the standard Frobenius-pullback comparison.',
r'Frobenius|Cartier|caract.ristique|courbure|degr.',check='targeted proof check',outcome='Checked degree of Frobenius pullback and its canonical zero-p-curvature connection; limited conclusion to failure of the degree argument.',results=('S20','159-no-reduction-monodromy-dense'))

add('N051','E. Formal normalization and its hypotheses','The inserted symbol isomorphism is part of the theorem','unproved claim',
'026:L2-8;034:L4-9',r'est un iso',
r'''The formal theorem is stated in characteristic zero and has an inserted isomorphism J/J²→Ω¹_{X/S}; that hypothesis must accompany the existence claim. With the formal line coordinate and this unit symbol, elimination of higher coefficients is possible recursively, whereas injectivity of the symbol alone supports uniqueness but not the same existence statement.''',
'Refines Hua, modernised reading of cote 159, hua_project/159.modern.tex, §§“Le cadre, tel que les pages 32 et 33 le posent” and “Le théorème de rigidité”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; formal_report.md checks the distinction.',
r'symbole|isomorphisme|tr.s r.guli|159-formal-rigidity',check='targeted proof check',outcome='Checked unit-symbol hypothesis for recursive existence and regular-symbol hypothesis for uniqueness.',results=('159-formal-rigidity-quadratic-torsor',))

add('N052','E. Formal normalization and its hypotheses','Rank-one conormal alone does not imply a formal disk','own idea',
'026:L2-8;033:L4-24',r'$\mathcal J/\mathcal J^2$ ... inversible',
r'''Confidence: high: the complete augmented dual-number algebra has one-dimensional J/J² but is not a power-series algebra, so that condition alone is insufficient. In the locally free differential-line setting over a Q-algebra, the extra connection with regular symbol repairs the gap: a lowest-order relation in R[[t]] differentiates to a nonzero relation of one lower order, impossible by minimality; formal_report.md gives the precise separated-complete argument. In characteristic p, even unit symbol allows the truncated algebra F_p[x,t]/(t^p) with C=(∂_x+∂_t)dx, so the characteristic restriction matters already for the formal-disk presentation.''',
'Adds a missing justification to Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”, and refines the hypotheses behind RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor rather than rejecting its unit-symbol case.',
r'compl.te|Sym|J/J|159-formal-rigidity',check='independent re-proof',outcome='Gave dual-number counterexample to conormal-only claim; proved formal-disk conclusion with regular symbol, Q-algebra, completeness and local differential-line assumptions.',results=('159-formal-rigidity-quadratic-torsor',))

add('N053','E. Formal normalization and its hypotheses','The second neighborhood reconstructs the extension','unpursued implication',
'025:L13-17;026:L20-23',r'E=\Omega^{-1}\otimes\mathcal J/\mathcal J^3',
r'''Once multiplication identifies J²/J³ with Ω², twisting 0→J²/J³→J/J³→J/J²→0 by Ω⁻¹ produces 0→Ω→E→O→0. This explicitly recovers the pointed projective-line bundle from order two, while recovering a compatible connection is a separate higher-order problem.''',
'Checks and restates Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”, and the underlying-bundle portion of RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor.',
r'ordre deux|ordre 2|Omega|159-formal-rigidity',check='targeted proof check',outcome='Checked exact-sequence twist under the associated-graded identification.',results=('159-formal-rigidity-quadratic-torsor',))

add('N054','E. Formal normalization and its hypotheses','A prescribed third jet and an arbitrary target connection are not independent','reading question',
'026:L24-28;027:L2',r'pour ... tte $c$',
r'''Here “order 3” is explicitly reduction modulo J⁴, and prescribing the cubic jet determines the compatible target quadratic coefficient rather than leaving it arbitrary. For C=(∂_x+∂_t)dx and u₃=id modulo t⁴, any extension preserves the coefficient of t², so it cannot intertwine C with (∂_x+(1+t²)∂_t)dx; thus the literal “for every c” continuation on scan 27 needs compatibility with u₃ or a different quantifier.''',
'Adds a quantifier correction to Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”, and qualifies RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; the corrected statement produces one compatible projective connection from each prescribed third jet, as checked in formal_report.md.',
r'ordre trois|ordre 3|u_3|rigidit|159-formal-rigidity',check='refuted, with refined statement id: N054.compatible_target',outcome='Refuted independent choice of arbitrary c and fixed u3; target lower coefficients must satisfy jet compatibility.',results=('159-formal-rigidity-quadratic-torsor',))

add('N055','E. Formal normalization and its hypotheses','Rigidity is a consequence of the first nonzero coefficient','unpursued implication',
'027:L6-17;029:L21-45;034:L23',r'la cat. des solutions est rigide',
r'''For a regular symbol over a Q-algebra, a nonidentity tangent-to-identity conjugacy has a first nonzero coefficient b_m, whose contribution to the transported connection begins with m·a₀·b_m in degree m−1. Since m is invertible and a₀ is a non-zero-divisor, it cannot stabilize the connection; this supplies the needed concrete freeness rather than deriving it from the abstract group-action lemma.''',
'Checks the rigidity conclusion in Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor, while distinguishing it from the faulty general freeness implication in §“La structure du groupe G”.',
r'rigide|libre|n\+1|structure du groupe|159-formal-rigidity',check='independent re-proof',outcome='Proved first-nonzero-coefficient obstruction to a stabilizer under regular symbol and Q-algebra assumptions.',results=('159-formal-rigidity-quadratic-torsor',))

add('N056','E. Formal normalization and its hypotheses','The inserted word “pseudo” preserves a global existence issue','unpursued implication',
'027:L8-12;034:L28-34',r'\inserted{pseudo} torseur',
r'''The difference between two lifts of a fixed second jet to a third jet is Hom(Ω,Ω³)=Ω², so the set of global lifts, if nonempty, is acted on simply transitively by Γ(X,Ω²). The inserted “pseudo” therefore matters: local lifts and a difference sheaf do not alone establish a global lift, and no preferred zero is supplied.''',
'Qualifies the unqualified torsor wording in Hua, hua_project/159.modern.tex, §§“Le théorème de rigidité” and “L’énoncé final”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; sufficient global lifting hypotheses are isolated in N066.',
r'pseudo|torseur|Gamma|159-formal-rigidity',check='targeted proof check',outcome='Checked difference sheaf Ω² and retained nonemptiness as a separate global condition.',results=('159-formal-rigidity-quadratic-torsor',))

add('N057','E. Formal normalization and its hypotheses','The recurrence explains exactly where characteristic zero is used','unpursued implication',
'029:L21-45;031:L20-44',r'(n+1)\alpha_n=0',
r'''Writing h(t)=t+b_m t^m+⋯, the first change in a connection with constant term a₀ occurs in degree m−1 and has coefficient m a₀ b_m; derivative terms in b_m occur later. A unit a₀ and invertible positive integers therefore let one kill each higher term uniquely, while the cubic coefficient changes the quadratic term by 3a₀b₃ in the convention fixed in formal_report.md. These divisions require a Q-algebra, not merely a ring whose additive characteristic is zero: over Z[x] even the first correction can require the unavailable coefficient −1/4.''',
'Checks Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”, and the local mechanism for RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; it does not assume every long expansion on scans 29 and 31 is correct.',
r'n\+1|alpha|changement de param.tre|159-formal-rigidity',check='computation or formal certificate',outcome='Verified finite Taylor coefficients and supplied the general leading-order proof; convention recorded in formal_report.md.',results=('159-formal-rigidity-quadratic-torsor',))

add('N058','E. Formal normalization and its hypotheses','Positive characteristic has explicit resonant automorphisms','own idea',
'029:L29-45;034:L9-23',r'car. nulle',
r'''Confidence: high: over F_p[x], the nonidentity formal automorphism h(t)=t+t^p commutes with ∂_x+∂_t and, for p≥5, is the identity modulo t⁴. It is therefore a nontrivial stabilizer in the very group used for the characteristic-zero uniqueness statement; higher p-powers cover the small primes, so a characteristic-p extension needs extra structure or a different quotient. The example even has zero p-curvature, because the two commuting partial derivations have zero p-th iterates, as checked in formal_report.md using the definition in [L2, (5.0.4)].''',
'Adds a concrete resonance to Hua, hua_project/159.modern.tex, §§“Le calcul du changement de paramètre” and “L’énoncé final”, and explains a limit of RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor and of the S20 p-curvature guess.',
r'caract.ristique|n\+1|courbure|159-formal-rigidity',check='computation or formal certificate',outcome='Checked h′=1 and base-constant coefficients in characteristic p; nontrivial stabilizer survives fixed third jet.',results=('159-formal-rigidity-quadratic-torsor','S20'))

add('N059','E. Formal normalization and its hypotheses','Reciprocal series and compositional inverses must be separated','reading question',
'029:L3-18;031:L46-48',r'u^{-1}',
r'''For the admissible element h(t)=t+t³ of G, its compositional inverse begins t−t³+3t⁵, whereas t/(1+t²) begins t−t³+t⁵. The reciprocal expression becomes correct only with its denominator evaluated at the inverse variable, so the literal same-variable inverse substitution in the scratch calculations cannot be used as an exact identity, even though the leading-coefficient induction can remain valid.''',
'Adds a formal-series qualification to Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”, which discusses the multiplicative factor and denominators without separating its reciprocal from automorphism inversion; formal_report.md and formal_group_certificate.json keep this separate from the valid leading-order argument.',
r'inverse|changement de param.tre|alpha|d.nominateur',check='computation or formal certificate',outcome='Compared quintic coefficients for admissible h=t+t³: inverse coefficient3 versus reciprocal coefficient1; evaluated-variable repair stated, frozen formulas unchanged.')

add('N060','E. Formal normalization and its hypotheses','The associated-graded derivation has an integer coefficient','reading question',
'028:L33-40;033:L35-45',r'\lambda\omega^i',
r'''For a derivation C with C(t)≡a₀dx modulo t, Leibniz gives C(t^i)≡i a₀t^(i−1)dx modulo t^i. Thus a formula without i on ordinary symmetric powers is false already for i=2 over Q; divided powers would have a different basis and cannot be silently substituted for the written Sym-algebra.''',
'Corrects the corresponding degree-lowering formula repeated by Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”; the literal omission in the frozen text is retained and the simple derivation example is certified in formal_report.md.',
r'lin.arit.|Sym|gradu.|lambda|cadre',check='computation or formal certificate',outcome='Checked C(t²)=2t C(t), refuting an i-independent formula on ordinary symmetric powers.')

add('N061','E. Formal normalization and its hypotheses','The graded operator is a derivation, not a Sym-linear map','reading question',
'033:L37-45;034:L3-4',r'\operatorname{Sym}(\Omega)-linéaire',
r'''The degree-lowering associated-graded operator satisfies the Leibniz rule, and for C(t)=dx one has C(t·t)=2t dx while t C(t)=t dx. Its degree-one component determines it as a derivation, which is a valid replacement for the stated Sym(Ω)-linearity but not the same assertion.''',
'Corrects the manuscript’s linearity claim and the related i-independent multiplication description in Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”; formal_report.md distinguishes this algebraic error from the less certain coefficient glyphs.',
r'Sym.*lin|lin.arit.|gradu.|cadre',check='refuted, with refined statement id: N061.derivation',outcome='Refuted Sym-linearity by C(t²)=2t dx; correct description is the graded derivation determined by the symbol.')

add('N062','E. Formal normalization and its hypotheses','G(c) is defined as a subset, and need not be a subgroup','reading question',
'030:L11-21;032:L10-12;034:L28-34',r'un sous-ensemble $G(c)$',
r'''The manuscript’s word is “sous-ensemble”, and an element taking c into the preferred slice need not have its inverse take c into that slice. In the concrete formal model, h′=1+h² takes ∂_t to the quadratic vector field (1+t²)∂_t, while its inverse introduces a nonzero t⁴ coefficient, giving an explicit failure of inverse closure.''',
'Contradicts the subgroup terminology in Hua, hua_project/159.modern.tex, §“La structure du groupe G”, and refines its use in §“L’énoncé final”; formal_report.md gives both a finite-group example and the formal-series certificate.',
r'sous.groupe|sous.ensemble|structure du groupe|G\(c\)',check='computation or formal certificate',outcome='Verified inverse-closure failure for the formal slice transporter; G(c) is a set of coset representatives, not automatically a subgroup.')

add('N063','E. Formal normalization and its hypotheses','The coset-transversal assertion is valid without a subgroup claim','unpursued implication',
'030:L21-42;032:L6-33',r'G_0\times C_0\arrow[r,"\sim"] & C',
r'''If H×C₀→C is bijective and c∈C₀, every left coset of H in G has exactly one representative g with gc∈C₀: normalize gc by the unique H-coordinate. This proves G(c)≈H\G as sets and the factorization G=H·G(c), without requiring G(c) to be closed under multiplication.''',
'Checks the valid part of Hua, hua_project/159.modern.tex, §“La structure du groupe G”, while removing its extra subgroup language; this part of the manuscript’s abstract argument survives the later stabilizer objection.',
r'G_0|coset|classes|structure du groupe',check='independent re-proof',outcome='Proved unique left-coset representative by the H×C0 normal form.')

add('N064','E. Formal normalization and its hypotheses','The abstract freeness question has a counterexample','self-flagged: a step he himself marks as unverified',
'032:L6-9;032:L34',r'gc=c\Longrightarrow g=1\ ?',
r'''The stated normal-form hypothesis does not imply that the full G-action is free: take G=H×K acting on C=H through the first factor and C₀={1}, with K nontrivial. Then H×C₀→C is bijective but K fixes every point; concrete formal freeness therefore needs the coefficient argument of N055.''',
'Answers negatively the manuscript’s explicit question and corrects the inference in Hua, hua_project/159.modern.tex, §“La structure du groupe G”; formal_report.md includes a finite certificate.',
r'libre|gc|structure du groupe|stabilis',check='refuted, with refined statement id: N064.formal_freeness_N055',outcome='Refuted abstract freeness implication by product-group action; concrete regular formal action repaired independently in N055.')

add('N065','E. Formal normalization and its hypotheses','The orbit intersection is generally a double-coset space','unproved claim',
'032:L38-42',r'O\cap C_0\simeq{}_{G_0}\backslash G',
r'''For c∈O∩C₀, the correct set is H\G/Stab_G(c), since the orbit is G/Stab_G(c) and C₀ supplies representatives for its H-orbits. The displayed single-coset version follows when the full action is free, which is false abstractly but can be established in the concrete characteristic-zero regular-symbol setting.''',
'Corrects the abstract orbit corollary endorsed by Hua, hua_project/159.modern.tex, §“La structure du groupe G”, without automatically rejecting the concrete formal consequence after N055 supplies its missing hypothesis.',
r'orbite|stabilis|structure du groupe|G_0',check='refuted, with refined statement id: N065.double_coset',outcome=r'Derived H\G/Stab(c); single-coset formula needs a separate freeness hypothesis.')

add('N066','E. Formal normalization and its hypotheses','Global jet quotients need a lifting argument','own idea',
'027:L8-12;034:L28-34',r'\Gamma(X,\Omega^{\otimes2})',
r'''Confidence: high about the distinction: a sheaf quotient G/G₀≈Ω² does not alone identify Γ(G)/Γ(G₀) with Γ(Ω²), since a global section of the quotient may have a lifting obstruction. Surjectivity does hold for a globally split completed symmetric algebra by the explicit lift t↦t+qt³, and, over a Q-base, for the completion of a pointed projective-line bundle with a given global very regular projective connection, local conjugacies with the prescribed cubic jet glue uniquely; formal_report.md supplies these sufficient hypotheses.''',
'Qualifies Hua, hua_project/159.modern.tex, §§“La structure du groupe G” and “L’énoncé final”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor, while respecting the manuscript’s “pseudo” on scan 27.',
r'Gamma|global|pseudo|159-formal-rigidity',check='targeted proof check',outcome='Distinguished sheaf from global quotient; checked explicit split lift and uniqueness-based gluing under a given very regular global connection.',results=('159-formal-rigidity-quadratic-torsor',))

add('N067','E. Formal normalization and its hypotheses','Regularity alone does not give normalization existence','own idea',
'034:L4-23',r'régulière ... très régulière',
r'''Confidence: high under the standard non-zero-divisor meaning of a regular section: over R=Q[x], the connection C(t)=(x+t³)dx has regular nonunit symbol x. Any change h=t+b₄t⁴+⋯ modifies the cubic coefficient to 1+4xb₄, which cannot vanish with b₄∈R, so uniqueness under regularity must be separated from existence under the stronger unit-symbol condition.''',
'Corrects the conflation of regular and very regular in Hua, hua_project/159.modern.tex, §§“Le cadre, tel que les pages 32 et 33 le posent” and “L’énoncé final”; the manuscript’s own revised wording may be aiming at exactly this distinction, and formal_report.md gives the counterexample.',
r'tr.s r.guli|r.guli.re|bijective|injective',check='computation or formal certificate',outcome='Checked divisibility obstruction 1+4xb4=0 in Q[x]; regularity gives uniqueness, unit symbol gives recursive existence.')

add('N068','E. Formal normalization and its hypotheses','The theorem reconstructs a compatible connection, not a distinguished universal one','reading question',
'026:L10-28;027:L6-12',r'muni d’une connexion $c$',
r'''The target consists of a pointed projective bundle together with a connection whose completion is identified with the given formal connection; the text does not select one connection on every curve independently of that input. The third-jet ambiguity and the quadratic-differential pseudo-torsor are evidence of the remaining choice, not an assertion of a canonical origin.''',
'Qualifies “with its canonical connection” in RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor and the wording of Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”; the underlying bundle can be canonical without the same being true of an independently chosen connection.',
r'canonique|159-formal-rigidity|connexion|rigidit',results=('159-formal-rigidity-quadratic-torsor',))

add('N069','E. Formal normalization and its hypotheses','The coefficient glyph and indices remain unresolved readings','reading question',
'028:L3-29;031:L3-54;033:L18-45;034:L3-4',r'\varpi_0|\bar\omega_0',
r'''Several coefficient signs resemble a modified omega or varpi, while some powers and subscripts in the dense calculation on scan 31 are genuinely uncertain. Hua’s normalized coefficient notation helps state a mathematical model, but it cannot decide those shapes or authorize replacing the first reading in the frozen doubt alternatives.''',
'Differs in documentary certainty from Hua, hua_project/159.modern.tex, §§“Le calcul du changement de paramètre” and “Le cadre, tel que les pages 32 et 33 le posent”; these are explicit post-context reading questions, not newly settled readings.',
r'varpi|omega_0|changement de param.tre|cadre')

add('N070','E. Formal normalization and its hypotheses','A concrete characteristic-p follow-up would compare higher stratification data','own idea',
'009:L7;029:L29-45;034:L7-9',r'\inserted{stratification}',
r'''Confidence: high for the local test and medium for a global classification, because the full ordinary principal-parts translation stratification Δx=x+ε, Δt=t+ε detects h(t)=t+t^q, q=p^r≥4, invisible to the ordinary connection: Δ(h(t))−h(Δt)=ε^q, with h fixing x and ε. Thus this family of resonant automorphisms does not preserve that full stratification, as verified in basic_report.md §B6; no claim about divided-power stratifications follows from this calculation. Whether the extra data restore an appropriate global normalization theorem, and how they compare with the actual equations in cote 93, remain questions rather than conclusions of these leaves.''',
'Adds a specific test to context/README.md, S20, and RESULTS_STATE.md entries MPL_93_002-046 P01 and P09, rather than asserting a p-curvature result from the title; Katz [L2, §5] provides the external language for that future test.',
r'stratification|Cartier|Frobenius|P01|P09|S20',check='computation or formal certificate',outcome='Checked Δh(t)-hΔ(t)=ε^q, q=p^r≥4, for ordinary full principal-parts translation; no PD or global rigidity claim.',results=('S20','MPL_93_002-046 P01','MPL_93_002-046 P09'))

add('N071','F. Additional authorial questions and their local disposition','The two questions on scan 5 are answered by the following calculation','self-flagged: a step he himself marks as unverified',
'005:L25-48;006:L20-46',r'Quel est l’hom canon. épi; Quel est l’autom.',
r'''The first question is answered by π(ω⊗f,g)=ωf+g on scan 5, and the second by u^L_a(g)=(1+a)u_a(g) on scan 6. They are working questions resolved in this sequence, not open conjectures; N010 checks the compatibility condition that motivates them.''',
'Restates the completed calculation in Hua, modernised reading of cote 159, hua_project/159.modern.tex, §“Le complété formel le long de la section, et l’action de Ω”, and adds the exact local question-and-answer locations.',
r'compl.t. formel|tautologique|quotient|1\+a')

add('N072','F. Additional authorial questions and their local disposition','“Vérifions” is followed by an explicit check and “OK !”','self-flagged: a step he himself marks as unverified',
'006:L38-46',r'Vérifions ... en général par acquit de conscience; OK !',
r'''This verification cue is followed immediately by the compatibility calculation and “OK !”, so it should be indexed as a self-check completed by the author rather than as an unresolved warning. A sign inside the written calculation still has a frozen doubt alternative, which remains a reading issue independent of the mathematical check in N010.''',
'Adds documentary detail to Hua, hua_project/159.modern.tex, §“Le complété formel le long de la section, et l’action de Ω”, whose normalized presentation does not preserve the same distinction between a completed check and an uncertain glyph.',
r'compl.t. formel|v.rifi|1\+a')

add('N073','F. Additional authorial questions and their local disposition','The finite-type qualification is a separate question','self-flagged: a step he himself marks as unverified',
'017:L5-18',r'de t.f. ?',
r'''The finite-type parenthesis concerns the algebraic moduli object behind the analytic flat-bundle space, not the dimension of the oper fiber. A finite presentation makes the representation variety finite type, but identifying the desired de Rham quotient and its representability needs the additional moduli work already flagged on scan 16.''',
'Adds the precise question to Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, and keeps it separate from the dimension conflation in §“L’anomalie de la page 15, et ce que la cohérence demande”.',
r'type fini|t\.f\.|repr.sent|tableau analytique|anomalie')

add('N074','F. Additional authorial questions and their local disposition','The formal search is initially conditional on existence','self-flagged: a step he himself marks as unverified',
'025:L11-28;026:L2-28;027:L8-12',r's’il y en a; Quels sont les autres ?',
r'''The insertion “s’il y en a” and the following classification question precede a heavily revised existence sentence and the characteristic-zero theorem on the next leaf. The later local normalization proof addresses existence with unit symbol and a prescribed compatible third jet, while the global lifting pseudo-torsor of N056 retains a separate nonemptiness issue.''',
'Adds the successive qualifications to Hua, hua_project/159.modern.tex, §§“Le théorème de rigidité” and “L’énoncé final”, and refines RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor rather than reading unconditional existence into the first question.',
r'existence|pseudo|rigidit|159-formal-rigidity',results=('159-formal-rigidity-quadratic-torsor',))

add('N075','F. Additional authorial questions and their local disposition','The coefficient question is followed by the characteristic-zero induction','self-flagged: a step he himself marks as unverified',
'029:L20-45',r'\alpha_n=?',
r'''The inserted question asks for the next coordinate-change coefficient, and the following calculation isolates (n+1)α_n before the characteristic-zero proposition. The coefficient mechanism is checked in N057, while N058 explains why the same induction does not provide uniqueness in characteristic p.''',
'Restates Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”, with the question’s actual disposition and its denominator restriction made explicit.',
r'alpha|n\+1|changement de param.tre')

add('N076','F. Additional authorial questions and their local disposition','The mark on scan 31 is not a secure authorial question mark','reading question',
'031:L54',r'\unsure{!|?}',
r'''The mark attached to the arrows is transcribed with exclamation mark as the first reading and question mark as the alternative. It is therefore included among possible verification flags, but no mathematical statement is designated self-doubted on the strength of that uncertain punctuation alone.''',
'Adds a bounded reading issue to Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”; the supplied modernization does not resolve the shape, and the transcription remains frozen.',
r'changement de param.tre|calcul|page 30')

add('N077','F. Additional authorial questions and their local disposition','The cancelled question about knowing C precedes the coefficient decomposition','withdrawn in the same text',
'033:L16-31',r'\deleted{\unsure{Comment peut-on connaître $C$}}',
r'''The question is both cancelled and uncertain, and the following lines describe C through its coefficients after choosing a local splitting. The decomposition identifies the degree-one coefficient as connection-like rather than O-linear; that valid distinction is checked in formal_report.md §FC-B1, separately from the erroneous Sym-linearity discussed in N061.''',
'Adds the deletion state to Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”, while retaining its valid distinction between the linear coefficient and the other coefficient maps.',
r'coefficient|lin.aire|cadre|splitting')

add('N078','F. Additional authorial questions and their local disposition','The cancelled jet-extension question is taken up on the next page','withdrawn in the same text',
'006:L55;007:L10-36',r'Comment calculer les extensions successives',
r'''The question at the bottom of scan 6 is cancelled, but scan 7 calculates precisely the successive extension Jⁿ/Jⁿ⁺² through the −n v_n pushout. This is a resumption in the next leaf, not evidence that the problem was left untouched.''',
'Restates the mathematical development in Hua, hua_project/159.modern.tex, §“La conséquence graduée”, and adds the cancelled-question and resumed-answer locations.',
r'cons.quence gradu|extensions successives|v_n')

add('N079','G. Standing question: title sheets and page counts','The first scan is an institutional cover','reading question',
'001:L1-13',r'IMAG; INSTITUT MONTPELLIERAIN; ALEXANDER GROTHENDIECK',
r'''Scan 1 is a printed institutional cover with its graphic, rather than an authorial mathematical title or a handwritten page count. It is included in the transcription and inventory, so the 32 supplied scans comprise this cover and 31 mathematical leaves.''',
'Adds the cover omitted from the mathematical page sequence used by Hua, hua_project/159.modern.tex, opening folder/page metadata; context/README.md identifies the dossier but supplies no additional authorial count.',
r'pages|folder|cote 159|dossier entier')

add('N080','G. Standing question: title sheets and page counts','The authorial title includes “canoniques”','reading question',
'002:L3-5',r'Connexions projectives canoniques et uniformisation des courbes algébriques.',
r'''The first mathematical leaf has this title and the section heading “1. Connexions projectives”. Its word “canoniques” belongs to the transcription, while whether the pages construct a canonical chosen connection must be judged from the narrower questions and torsors discussed in N013 and N068.''',
'Adds the full handwritten title to context/README.md’s shorter catalogue title and Hua, hua_project/159.modern.tex, §“Ce que le contenu montre, et ce qu’il ne date pas”, without turning a title into a proved existence statement.',
r'canonique|foldertitle|date pas|titre')

add('N081','G. Standing question: title sheets and page counts','The archive’s foliation is not an authorial page count','reading question',
'002:L2;013:L2;015:L2;023:L7;025:L29;034:L35',r'% archive foliation: 1',
r'''No authorial statement such as “32 pages” or “Pages 1–33” was located on these leaves, and the later pencil numbers are recorded only as archive-foliation comments. The supplied scan sequence is 1–13, 15–23, and 25–34: scans 14 and 24 were omitted as blank by the input package, so 34 PDF positions must not be reported as 34 supplied handwritten pages.''',
'Differs from treating Hua, hua_project/159.modern.tex, opening pages{1}{33}, as an authorial count; its mathematical page n corresponds to our scan n+1, and the actual omissions are specified in the supplied task rather than by a manuscript count.',
r'pages|1.33|33|foliation|dossier entier')

add('N082','G. Standing question: title sheets and page counts','No date is supplied by the handwritten title','reading question',
'001:L1-13;002:L3-5;034:L28-35',r'Connexions projectives canoniques',
r'''No authorial date was located in the supplied cover or mathematical leaves. An archival grouping near dated neighboring material cannot by itself date these notes, and no chronological claim about priority is drawn from the mathematical parallels in this report.''',
'Retains “s.d.” in context/README.md and agrees with the caution in Hua, hua_project/159.modern.tex, §“Ce que le contenu montre, et ce qu’il ne date pas”, while declining to turn its “Dérivateurs” folder association into a date for the handwriting.',
r'dating|1990|1991|date pas|s\.d\.')

INTRO = r'''# MPL 159 — Research notes after the frozen transcription

## Scope, evidence, and the planning questions

These notes concern cote 159, the 32 supplied scans numbered 1–13, 15–23, and
25–34. The root agent personally read and transcribed the images in one
sequential stream, completed a second image audit of all 32 pages, checked
recurring notation, and froze the 32 page fragments plus their exact combined
transcription at **2026-11-18 01:04:49 UTC**. The context was first opened at
**01:04:50 UTC**; no contextual or mathematical conclusion below changes a
frozen `.tex` file.

The source references below name the **scan number**, not the archive pencil
foliation. `L` numbers are physical lines in the named frozen page `.tex`
file, not claims about original manuscript line breaks. Brief quotations
omit intervening material where shown by an ellipsis; macro-bearing quotations
retain the editorial uncertainty or cancellation. All full readings, including
their doubt alternatives, remain in the transcription and doubts register.

| Planning question | Finding | Notes |
|---|---|---|
| Does the folder concern uniformization by projective connections? | Yes: it treats projective structures, transverse sections, uniformizing representations, and monodromy. | N001, N026–N049 |
| Does it write the specific Schwarzian equation needed for comparison? | No complete scalar normalization has been identified; the coordinate calculation has a sign conflict. | N002, N042–N043 |
| In which characteristic? | Mixed scope: general initial definitions and a question, explicit exclusions of characteristic two, a complex analytic section, and characteristic-zero formal theorems. | N003, N014, N049–N058 |
| Does it compute p-curvature? | No explicit p-curvature/Frobenius/Cartier calculation was located; characteristic-p counterexamples below are our comparisons, not manuscript content. | N004, N050, N058, N070 |
| Does he cite cotes 93 or 64? | No such citation was located in the supplied pages, subject to the recorded legibility limits. | N005 |
| Is the proposed 159–93–64 cluster established? | There is a substantive projective-connection/Gauss–Manin comparison to attempt, but no completed identification, and the actual 93/64 source pages are absent here. | N002, N005, N024, N070 |

The table is an index to the individually checked notes, not an additional
set of unlogged claims. The strongest changes to the supplied interpretation
concern the **object of the canonical-torsor question**, **flat bundles versus
opers**, **the injectivity assertion actually followed by an argument**, and
**the hypotheses and stabilizers in formal normalization**.

### Context and attribution

The authorized context files were read after the freeze, including the whole
`context/notes/RESULTS_STATE.md` and `context/hua_project/159.modern.tex`.
**Hua, modernised reading of cote 159** means the AI-produced interpretation
credited to Michel Hua’s project in `context/hua_project/README.md`; it is
neither our transcription nor our result. Its page n is generally our scan
n+1; the cover and blank omissions explain the different counts.

Each note has an actual `rg` query recorded as `[Qnnn]` in
`context_searches.tsv`, with query, matching files/lines, retained match locations,
and the comparison cited in the note. Subsection names identify the location
inside Hua’s file. RESULTS_STATE entries are connected by their supplied IDs;
their statuses are reports of earlier runs, not independent proof certificates.
The source files behind the truncated MPL_93 entries and the tower-result
register were not supplied, so no claim of reading or rechecking them is made.

The main event ledger uses the requested check categories and separates
documentary comparisons, targeted proof checks, independent proofs, exact
computations, and unproved background. Merely transcribing a statement was
not counted as a mathematical check. Delegated agents worked only after the
freeze on the mathematical checks in `research_checks/`; all image reading
and transcription decisions remained with the root agent. The model was
GPT-6 Astra Pro; a distinct numerical effort setting was not exposed, and
the event ledger records that fact instead of inventing one.
'''

FLAGS = r'''## Standing question: what the manuscript itself marks for checking

This index covers the explicit interrogatives, uncertainty phrases, and
verification cues found during the image reading and rechecked against the
frozen text. A working question that receives an answer is still listed;
an uncertain punctuation mark is not promoted to a secure question.

| Scan / TeX line | His words or sign, briefly | Disposition and note |
|---|---|---|
| 005 L25 | “Quel est l’hom canon. épi” | Answered later on the same leaf; N071. |
| 005 L48 | “Quel est l’autom.” … “de la situation ?” | Answered on scan 006; N071. |
| 006 L38–46 | “Vérifions” … “par acquit de conscience”; “OK !” | Author performs the check; N072. |
| 006 L55 | Deleted “Comment calculer les extensions successives” | Resumed and calculated on scan 007; N078. |
| 009 L5 | “est-il vrai” … “sans condit. de dim ni de car. ?” | Unrestricted canonical-torsor question remains open here; N013. |
| 016 L12 | “conditions jamais vérifiées si g=0 — et pour cause !” | A genus-zero exclusion, not a request to verify a step; see N029 and the supplementary event. |
| 016 L49 | “Sans doute peut-on prouver la représentabilité relative” | Representability expectation, with Artin-space qualification; N030. |
| 017 L5 | “de t.f. ?” | Finiteness qualification retained; N073. |
| 017 L16–17 | “Il est immédiat”; inserted “sans doute”; marginal “?” | Representation-variety construction is elementary, RH algebraicity is doubted; N031–N032. |
| 018 L9–10 | “sans doute cette opération n’est pas algébrique”; marginal “?” | Transported outer action is not settled by the RH argument; N033. |
| 018 L24 | “On suspecte” … “pas un sous-ens. constructible” | Negative expectation checked for the Fuchsian locus; N035. |
| 019 L20 | “Peut-on avoir” … “?” with “deux” changed to “une” | Both related conclusions appear on scan 021; N041. |
| 021 L18, L32 | “question : y en a-t-il … horizontales ?”; “Non” | Answer continues on scan 022; N045. |
| 022 L23 | “de car nulle ?” | Characteristic-zero degree argument checked; N049–N050. |
| 025 L11, L26 | “s’il y en a”; “Quels sont les autres ?” | Later normalization theorem and global lifting caveat; N074. |
| 029 L22 | “α_n=?” | Leading-coefficient induction follows; N075. |
| 030 L11 | “quand hĉ est-il de la forme ĉ′ ?” | Defines the subset G(c), followed by factorization; N062–N063. |
| 031 L54 | `\unsure{!|?}` | Possible flag only; N076. |
| 032 L34 | “gc=c ⇒ g=1 ?” | False for the abstract hypotheses; concrete formal freeness checked separately; N064–N065. |
| 033 L16 | Deleted, unsure “Comment peut-on connaître C” | Followed by coefficient decomposition; N077. |

No secure occurrence of “à vérifier”, “sauf erreur”, “je présume”, “admis”,
or “il faudrait vérifier” was located. This is a bounded reading observation,
not a claim that the six physically unreadable word groups contain none of
those words. The candidate-search documentation is
`diagnostics/self_flag_candidates.tsv`; it deliberately distinguishes deleted
questions, completed checks, and uncertain punctuation.
'''

BIBLIO = r'''## Primary literature consulted after the freeze

The following references supply comparisons in the research notes, not
transcription readings. The listed statements and sections were checked;
this does not claim independent verification of every theorem in each paper.
Longer independent arguments and exact computation scopes are in
`research_checks/basic_report.md`, `formal_report.md`, and `monodromy_report.md`.

| ID | Primary source and location used | Scope of use |
|---|---|---|
| L1 | A. Beilinson and V. Drinfeld, *Opers*, §§2.6–2.7, 3.1–3.3, [author-submitted text](https://arxiv.org/html/math/0501398v1) | Projective structures, second-order operators, and quadratic-differential torsors. |
| L2 | N. M. Katz, *Nilpotent connections and the monodromy theorem*, Publ. Math. IHÉS 39 (1970), 175–232, §5, especially (5.0.4), Theorem 5.1 and Proposition 5.2, [author-hosted published PDF](https://web.math.princeton.edu/~nmk/old/nilpconn.pdf) | Definition of p-curvature and Cartier descent; specific counterexamples here are independently checked. |
| L3 | A. Landesman, *The infinitesimal Torelli problem*, Theorem 4.3, [author-submitted PDF](https://arxiv.org/pdf/1911.02187) | Tangent-map duality with multiplication of canonical differentials. |
| L4 | E. M. Gagliardi and R. V. Martins, *Max Noether Theorem for Singular Curves*, introduction and main theorem, [author-submitted PDF](https://arxiv.org/pdf/2202.09349) | The smooth nonhyperelliptic multiplication theorem, stated within its extension to integral curves. |
| L5 | D. Gallo, M. Kapovich, and A. Marden, *The monodromy groups of Schwarzian equations on closed Riemann surfaces*, Annals of Mathematics 151 (2000), 625–704, §11.4, [author-hosted published PDF](https://www.math.ucdavis.edu/~kapovich/EPR/GaKaMa.pdf) | Fixed-X holonomy embedding/properness; the independent proof here is only pointwise injectivity. |
| L6 | D. Dumas and R. P. Kent IV, *Bers slices are Zariski dense*, Theorem A and §5, [author-submitted PDF](https://arxiv.org/pdf/0807.4509) | Density used for the separate RH dimension obstruction; its main proof is not independently reproduced. |
| L7 | C. T. McMullen, *The moduli space of Riemann surfaces is Kähler hyperbolic*, §2, [author-hosted preprint](https://people.math.harvard.edu/~ctm/papers/home/text/papers/kahler/kahler.pdf) | Fuchsian real analyticity, total reality, and the two half-planes. |
| L8 | S. Baba and S. Gupta, *Holonomy map fibers of CP¹-structures in moduli space*, introduction and §2.4, [author-submitted PDF](https://arxiv.org/pdf/1402.5445) | Holonomy-preserving grafting and the varying-X distinction. |

## Verification and remaining limits

The exact algebra certificates test the stated examples and finite jets;
the reports separately give the all-orders arguments where those are claimed.
No proof assistant certification or numerical evidence is substituted for a
general proof. In particular, the notes do **not** settle the all-characteristic
canonical-torsor question, the general transported mapping-class-action
algebraicity question, arbitrary-base scheme monomorphism, or nonemptiness of
every global third-jet lifting pseudo-torsor.

The 441 doubt occurrences in the frozen transcription are indexed separately;
research context has not been used to erase them. The six `\illegible` groups
are words, not stand-ins for mathematical symbols. The final hash check and
structural validation are recorded in `progress.log`; the supplied environment
lacked the base LaTeX format and required packages, so no successful PDF
compilation is claimed. No supplied scans, attached context sources, or older
checkpoint ZIPs are included in the final package.
'''

def source_text(ms):
    parts=[]
    for item in ms.split(';'):
        scan, spec=item.split(':')
        path=ROOT/'pages'/f'MPL_159_159_scan{int(scan):03d}.tex'
        lines=path.read_text(encoding='utf-8').splitlines()
        nums=[int(n) for n in re.findall(r'\d+',spec)]
        if not nums or min(nums)<1 or max(nums)>len(lines):
            raise ValueError(f'Bad source locator {item}: page has {len(lines)} lines')
        parts.append(f'159.pdf scan {int(scan):03d}, `{path.relative_to(ROOT)}` {spec}')
    return '; '.join(parts)

def run_query(n):
    proc=subprocess.run(['rg','-n','-i','--no-heading','-e',n['query'],str(CONTEXT)],
                        capture_output=True,text=True,check=False)
    if proc.returncode not in (0,1):
        raise RuntimeError(f"{n['id']} query failed: {proc.stderr}")
    hits=proc.stdout.splitlines()
    byfile={}
    for hit in hits:
        rel=hit.replace(str(CONTEXT)+'/', 'context/',1)
        file=rel.split(':',1)[0]
        byfile.setdefault(file,[]).append(rel)
    kept=[]
    for file, values in byfile.items():
        selected=values if len(values)<=16 else values[:8]+values[-8:]
        line_numbers=[v.split(':',2)[1] for v in selected]
        kept.append(file+':'+','.join(line_numbers))
    return {'query_id': 'Q'+n['id'][1:], 'note_id':n['id'],
            'searched_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'pattern':n['query'], 'match_count':len(hits),
            'matching_files':'; '.join(byfile),
            'retained_match_locations':' || '.join(kept) if kept else 'No literal rg match; see explicit comparison and scope in note.',
            'comparison':n['context']}

def event(statement_id, event_type, outcome, who=None):
    return {'statement_id':statement_id,'date':'2026-11-18',
            'who':who or 'GPT-6 Astra Pro; effort not exposed; MPL_159 root',
            'type':event_type,'outcome':outcome}

def build_events():
    events=[]
    used_results={}
    for n in NOTES:
        outcome=n['outcome'] or ('Documentary/context comparison checked; no proof of an unproved or uncertain manuscript claim is implied. '+n['title'])
        events.append(event(n['id'],n['check'],outcome))
        for place in n['ms'].split(';'):
            events.append(event('M159.'+place.replace(':','.')+'/'+n['id'],n['check'],
                f"Used for {n['id']}: {outcome}"))
        events.append(event('CONTEXT/'+n['id'],'used and rechecked in this run',
            f"Q{n['id'][1:]}: "+n['context']))
        for result_id in n['results']:
            used_results.setdefault(result_id,[]).append(n['id'])
    for result_id, ids in used_results.items():
        if result_id=='159-monodromy-injectivity-question':
            et='refuted, with refined statement id: N038'
            outcome='Historical description “without answering” is contradicted by scans18–21; fixed-X pointwise injectivity independently checked. '
        elif result_id=='159-no-reduction-monodromy-dense':
            et='targeted proof check'
            outcome='Characteristic-zero complex density checked with the finite-cover completion credited to Hua; no positive-characteristic extension claimed. '
        elif result_id=='159-formal-rigidity-quadratic-torsor':
            et='targeted proof check'
            outcome='Local unit-symbol normalization checked; retain compatibility of target with third jet and global pseudo-torsor nonemptiness caveat; canonical chosen connection not established. '
        else:
            et='carried as background without fault found'
            outcome='Used only as the supplied planning lead, open-status label, or truncated research-note summary; underlying source/proof not supplied or rechecked, and no status upgrade claimed. '
        events.append(event(result_id,et,outcome+'Connected notes: '+', '.join(ids)))

    formal=ROOT/'research_checks'/'CHECK_EVENTS_formal_proposed.tsv'
    repairs={
      '159-formal-action-orbit-unqualified':'N065.double_coset',
      '159-formal-action-slice-subgroup':'N062',
      '159-formal-graded-symbol-linearity':'N061.derivation',
      '159-formal-bare-power-series-presentation':'N052',
      '159-formal-characteristic-p-presentation':'159-formal-regular-power-series-presentation',
      '159-formal-regular-symbol-surjectivity':'N051',
      '159-formal-characteristic-zero-ring-sufficiency':'159-formal-unit-symbol-normalization',
      '159-formal-characteristic-p-rigidity':'N055',
      '159-formal-reciprocal-inverse':'N059',
      '159-formal-normal-form-slice-subgroup':'N062',
      '159-formal-target-connection-compatibility':'N054.compatible_target'}
    computations={'159-formal-finite-certificate','159-formal-coordinate-change-exact',
                  '159-formal-zero-p-curvature-resonance'}
    with formal.open(encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            old=row['type']
            if old=='refuted':
                typ='refuted, with refined statement id: '+repairs[row['statement_id']]
            elif old=='used': typ='used and rechecked in this run'
            elif row['statement_id'] in computations: typ='computation or formal certificate'
            else: typ='independent re-proof'
            outcome=row['outcome']
            if row['statement_id'] in {'159-formal-projective-global-quotient','159-formal-fixed-projective-model-descent'}:
                outcome += ' This connection-based gluing statement is over a Q-base.'
            events.append(event(row['statement_id'],typ,outcome,
                'GPT-6 Astra Pro; effort not exposed; MPL_159 formal_checks'))
    mono=ROOT/'research_checks'/'monodromy_check_events.tsv'
    mono_repairs={'MC01':'N038','MC04':'N026','MC08':'N036.orientation',
                  'MC13':'MC13.distinct_predicates'}
    with mono.open(encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            check_type=row['check_type']
            if row['statement_id'] in mono_repairs:
                check_type='refuted, with refined statement id: '+mono_repairs[row['statement_id']]
            events.append(event(row['statement_id'],check_type,
                row['outcome']+' | Evidence: '+row['evidence']+' | Limits: '+row['limits'],
                'GPT-6 Astra Pro; effort not exposed; MPL_159 monodromy_checks'))
    for i in range(1,9):
        events.append(event(f'L{i}','used and rechecked in this run',
            'Primary source opened after freeze and listed statement/section compared; no claim to independently prove all results in this source. See literature register and research reports.'))
    events.extend([
        event('M159.016.L12','targeted proof check','Genus-zero flat bundles over C are trivial because the sphere is simply connected, so the specified nondegeneracy conditions fail; this is an exclusion, not an authorial unresolved check.'),
        event('M159.flags.package','used and rechecked in this run','Explicit questions, uncertainty phrases, deleted questions, and completed checks indexed against frozen text and the completed image reading; no secure à vérifier/sauf erreur/je présume/admis/il faudrait vérifier located, subject to marked unreadable words.'),
        event('N036.orientation','targeted proof check','Two halfplanes refute unconditional domain uniqueness; choosing the side compatible with the oriented marked uniformization removes that specific ambiguity, without classifying all homogeneous domains.'),
        event('N054.compatible_target','independent re-proof','Prescribed cubic coefficient b3 forces target quadratic coefficient a2+3a0b3; higher terms cannot change it.'),
        event('N061.derivation','independent re-proof','The graded operator is the degree-minus-one derivation determined by its degree-one symbol, with factor i on t^i.'),
        event('N064.formal_freeness_N055','independent re-proof','Abstract freeness fails; the regular-symbol Q-algebra formal action is free by the first-nonzero-coefficient calculation.'),
        event('N065.double_coset','independent re-proof','Orbit intersection is H\\G/Stab(c); derive from the orbit G/Stab(c) and the H-normal form.'),
        event('MC13.distinct_predicates','independent re-proof','Irreducibility, complex Zariski density, and Kleinian nonelementarity are distinct predicates: finite A4 gives the first separation, and a dense subgroup of PSU2 gives the second; see monodromy_report.md MC13.'),
        event('BASIC.CERTIFICATE','computation or formal certificate','basic_checks.py assertions passed: finite-field alternating splitting maps, invariant-square coefficients, declared Möbius-gauge convention, literal sign conflict, dimension identity, and ordinary full-stratification test.'),
        event('N070.ordinary_stratification_test','computation or formal certificate','Over F_p[x][[t]], Δx=x+ε, Δt=t+ε, h(t)=t+t^q and h fixes x,ε; (Δ∘h-h∘Δ)(t)=ε^q for q=p^r≥4. Ordinary principal parts detect this family at order q; no PD or global-rigidity conclusion.')])
    return events

def main():
    assert [n['id'] for n in NOTES]==[f'N{i:03d}' for i in range(1,83)]
    chunks=[INTRO]
    queries=[]
    last_section=None
    for n in NOTES:
        if n['section']!=last_section:
            chunks.append('\n## '+n['section']+'\n')
            last_section=n['section']
        body=n['body']
        if 'own idea' in n['kind'] and not re.search(r'reason|because|since|based on',body,re.I):
            body=re.sub(r'^(Confidence:.*?):',r'\1; reason:',body,count=1)
        chunks.append(f"\n### {n['id']} — {n['title']}\n\n**Kind:** {n['kind']} · **Source:** {source_text(n['ms'])} · **Quote:** `{n['quote']}`\n\n{body}\n\n**Context comparison:** {n['context']} [Q{n['id'][1:]}]\n")
        queries.append(run_query(n))
    chunks.extend(['\n'+FLAGS,'\n'+BIBLIO])
    (ROOT/'MPL_159_notes.md').write_text('\n'.join(chunks).strip()+'\n',encoding='utf-8')
    with (ROOT/'context_searches.tsv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(queries[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(queries)
    events=build_events()
    with (ROOT/'CHECK_EVENTS.tsv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(events)
    print(f"Wrote {len(NOTES)} notes, {len(queries)} actual context queries, and {len(events)} check events.")
    print('Queries without literal hits: '+', '.join(q['query_id'] for q in queries if not q['match_count']))

if __name__=='__main__':
    main()
