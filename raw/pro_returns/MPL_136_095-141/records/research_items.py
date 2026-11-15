"""Research-note registry: authored only after the transcription freeze."""
ITEMS=[]

def add(id, scans, kind, quote, body, context, ids, query, confidence=None):
    ITEMS.append(dict(id=id,scans=scans,kind=kind,quote=quote,body=body,
                      context=context,results_ids=ids,query=query,confidence=confidence))

W='WG2 §2.4 #5'
H='WG H6'

add('N01','096','unproved claim',r'on sait que',
r'The free divided-power/exterior presentation $\mathrm{DR}(\Phi,T)=\Gamma^*(\Phi)\otimes\bigwedge^*\Psi$ is asserted to be a special de Rham algebra with a canonical map to $A^{**}$. A proof needs the precise differential, the distinguished element, the PD ideal, and the relevant flatness hypotheses; the displayed presentation alone does not prove a cohomology comparison.',
'C3',W,r'Gamma|divided powers|universal polynomial')

add('N02','096','unproved claim',r'Cela ... implique aisément',
r'The canonical square is used to claim an equivalence after passing to the stated derived categories. One must specify which maps are inverted and why the canonical comparison maps become invertible, rather than infer an equivalence merely from the existence of natural arrows.',
'C8',W,r'equivalence|uniqueness|De.Rham')

add('N03','098','unproved claim',r'On sait que cette dernière est équivalente à la cat. ponctuelle',
r'The category of flat-quotient extensions is invoked as having point-like localization, without its proof appearing in this package. This is a claim about the groupoid obtained by localization and should not be promoted to a statement about all higher homotopies of the nerve.',
'C8',W,r'groupoid|contractib|uniqueness|point')

add('N04','098; 100; 102; 104','conjecture / conditional claim',r'Supposons que ceci implique que les $\Gamma_k^i\Phi$ ... sont uni. flasques',
r'The universally flasque version of the point-category proposition is explicitly conditional on positive divided powers preserving universal flasqueness for the specified flat modules. Scan 100 marks the proposed justification as false as written, so subsequent uses in 102 and the conditional arrow in 104 do not discharge this hypothesis.',
'C6',W,r'flasque|flabby|divided powers|acyclic')

add('N05','100, referring back to 098','withdrawn in the same text / self-flagged',r'faux tel quel, à arranger',
r'The margin retracts the displayed implication from flasque plus flat to homotopic to zero, which was intended to justify the condition used on 098. The nearby insertion appears to replace flatness by projectivity, but neither a corrected theorem nor its proof is supplied here.',
'C5',W,r'false|divided.power|projectiv|homotop')

add('N06','100','own idea',r'non, projectif',
r'A useful repair test is to distinguish acyclicity, degreewise flatness, and an actual contracting homotopy before applying a nonlinear functor such as $\Gamma^i$. For a prime $p$, the short exact complex $0\to\bigoplus_{n\ge0}\mathbf Z\xrightarrow{e_n\mapsto e_n-p e_{n+1}}\bigoplus_{n\ge0}\mathbf Z\to\mathbf Z[1/p]\to0$ is acyclic with flat terms but is not contractible, since the quotient is not projective and the sequence cannot split. This is not asserted to be a counterexample to every historical meaning of “flasque” on these sheets.',
'C6',W,r'acyclic|flat|projective|divided.power','high; explicit nonsplit exact complex, with historical scope left open')

add('N07','100; 102; 105','unpursued implication',r'$i_{0*}(M)\simeq\Phi_*\otimes_{\mathbf Z}M$',
r'The evaluation/right-adjoint calculation supplies the natural map $A_*\to i_{0*}i_0^*A_*$ used in the standard-model zigzag, including the handwritten diagram on the reused sheet 105. This identifies a concrete universal construction in the package; it does not identify a new de Rham topos.',
'C3',W,r'adjoint|universal|De.Rham')

add('N08','102','expectation',r'qui semble ... économique de toutes',
r'The standard model is described as apparently the most economical, and a three-stage zigzag is drawn. “Economical” has no supplied minimality criterion, so a universal minimal-object claim would require an additional definition and proof.',
'C8',W,r'universal|uniqueness|minimal|De.Rham')

add('N09','102; 104; 106','unpursued implication',r'ayant plus de morphismes',
r'The primed categories enlarge the allowed morphisms to completed differential PD maps preserving $T$, rather than merely repeat the unprimed category. Any uniqueness conclusion must therefore be rechecked after this enlargement: it may introduce automorphisms even when objects remain connected by the standard zigzags.',
'C8',W,r'groupoid|automorphism|uniqueness|completion')

add('N10','104; 106','reading question',r'groupoïdes ... ponctuels; deux groupes, que nous nous proposons de déterminer',
r'The doubtful adjective on 104 cannot safely be interpreted as asserting trivial isotropy, because 106 immediately proposes determining the two groups associated with the connected groupoids. The context encourages keeping equivalence, connectedness, and uniqueness distinct, but does not decide whether the written adjective is “ponctuels” or “pointés”; the frozen reading remains unchanged.',
'C8',W,r'groupoid|uniqueness|axiomati')

add('N11','106','question / unfinished computation',r'que nous nous proposons de déterminer',
r'The two automorphism groups of the primed localizations are explicitly left as targets of computation, in the case $X=S_s$. The component formulas for $v(p,q)$ begin that calculation, but no completed description of both groups appears before the text changes topic.',
'C8',W,r'group|automorphism|uniqueness')

add('N12','106','reading question',r'$(p+q)\neq(1,0)$',
r'The first reading in the condition on $\bar v(p,q)$ is a scalar sum compared with an ordered pair, while the preceding condition uses the pair $(p,q)$. Replacing the sum by the pair would repair the type mismatch, but that is a mathematical proposal rather than a post-freeze correction; no supplied context passage resolves the ink.',
'C0',W,r'pair|bigrad|De.Rham')

add('N13','108','reading question',r'$\beta^*(\xi_0)=1|\beta^*(\xi_0)=0$',
r'The endpoint condition and the later simplex identities are too faded to support a reliable theorem about universal morphisms. The competing endpoint values already occur in the doubt marker; neither the familiar interval model nor a contextual universal construction licenses choosing the mathematically convenient value.',
'C3',W,r'polynomial|universal|simplex|completion')

add('N14','109','unproved claim — reused English sheet',r'precisely determines the nilpotent quotient',
r'The donor sheet asserts that $\Lambda_{1,n}$ determines $\pi_1/C_n$ over $Q$ or $R$. It is evidence of rational/real minimal-model material in the physical bundle, not evidence that the integral PD lecture proves the same classification; its precise bibliographic provenance is not established here.',
'C4',H,r'nilpotent|rational|fundamental group|polynomial cochains')

add('N15','109','unproved claim — reused English sheet',r'a tower of spaces and maps',
r'The model is related, through a cited but absent Appendix H, to a tower of principal fibrations with rational-vector-space homotopy fibres. The sheet calls this a rational homotopy type for arbitrary spaces, so the relation to modern nilpotent or completion hypotheses requires care rather than importing a simply connected theorem without qualification.',
'C8',H,r'Cartan.Serre|tower|nilpoten|rational')

add('N16','109','self-flagged open point — reused English sheet',r'not yet completely understood except in a philosophical way',
r'The significance of the higher-dimensional model for general non-simply connected spaces is expressly unresolved on the sheet. This is a useful boundary for comparisons to schematization, but it cannot be assigned to Grothendieck as the author of this English passage without independent provenance.',
'C8',H,r'non.simply|fundamental group|schematization')

add('N17','111','unproved claim / reading question',r'transforment ... $\lim$ ... en ... $\lim$, donc qui sont représentables',
r'The direction of the underlined limit symbols is not drawn, although the functor has contravariant variance. Representability is compatible with sending colimits of semisimplicial sets to limits, degree by degree in the underlying set-valued functors; a stronger literal assertion about arbitrary limits should not be substituted for the unspecified notation.',
'C2',W,r'representab|functor|semi.simplicial|limit')

add('N18','111; 113','unproved claim',r'cohomologie de De Rham associée',
r'The generalized theory has two gradings, a differential, an augmentation, and divided powers, while its admissibility is expressed only after applying $\tau_\infty$. The package does not supply the earlier definition of this extraction functor, so one cannot replace it by ordinary cohomology of the ungraded complex or by evaluation at $T=1$.',
'C6',W,r'bigrad|cohomology|De.Rham|divided powers')

add('N19','113','unproved claim',r'dans l\'image essentielle de $\mathrm{Mod}(k)$',
r'The desired decomposition into $H_C^*(X)$ and the auxiliary coefficient algebra is part of the admissibility discussion, with canonicity itself qualified in the writing. A proof of a multiplicative integral comparison must identify this descent/extraction and show that the product recovered there is the ordinary cup product.',
'C6',W,r'module structure|linearization|cohomology|divided powers')

add('N20','113','unpursued implication',r'comme un faisceau ... sur le topos $(\mathrm{Ss})$',
r'The actual sheaf construction visible here regards the structured semisimplicial object as a sheaf on the presheaf topos of semisimplicial sets and compares ordinary with derived global sections. This is concrete evidence for a sheaf-theoretic treatment of de Rham data, but it does not define a separately named “topos de De Rham” or an associated-sheaf functor on a specified new site.',
'C10',W,r'topos|sheaf|sections|faisceaut')

add('N21','115','self-flagged expectation',r'On ... voudrait que ces deux flèches soient des isomorphismes',
r'The two derived comparison arrows are desired isomorphisms after $\tau_\infty$, not a theorem proved on this page. The change from “demande” to “voudrait” is material evidence that the comparison is being formulated as a goal.',
'C10',W,r'weak equivalence|sections|cohomology|spectral sequence')

add('N22','115','withdrawn in the same text',r'\deleted{signifie}\inserted{implique}',
r'The author weakens a claimed equivalence to an implication when relating negligible kernels/cokernels to the horizontal comparison. The research argument must preserve this one-way logical relation; the unqualified converse is not licensed by the final wording.',
'C10',W,r'implies|equivalence|sections|cohomology')

add('N23','117','unproved claim',r'l\'augmentation est un quasi-iso',
r'The phrase is then spelled out by eventual vanishing in the first grading for each fixed positive exterior degree, and eventual identification of the degree-zero kernel with $S_k^i$. These are asymptotic conditions involving $\lambda(p)$, rather than an assertion that each fixed-weight complex is an ordinary resolution in all degrees.',
'C6',W,r'graded|cohomology|resolution|divided powers')

add('N24','117','conjecture / self-flagged expectation',r'On suspecte qu\'il faut pouvoir prendre $\lambda$ indépendant de $n$',
r'Uniformity in the simplex dimension is explicitly suspected, not proved. Establishing it would turn the objectwise simplex comparison into a condition usable uniformly on arbitrary $X$, and requires a bound that does not deteriorate with $n$.',
'C10',W,r'cohomology|spectral sequence|semi.simplicial|uniform')

add('N25','119','unproved claim / proof sketch',r'chaque $C_*^{i*}$ est une résolution ... jusqu\'au degré $p$',
r'The horizontal comparison is justified only by a truncated-resolution observation followed by an ellipsis. A proof must state the bounded range, explain how the uniform weight bound controls hypercohomology in that range, and justify passage through $\tau_\infty$.',
'C10',W,r'resolution|cohomology|spectral sequence|sections')

add('N26','119','unproved claim',r'est conséquence de la condition suivante',
r'The divergence $\pi(i)\to\infty$ is proposed as a sufficient condition for the vertical ordinary-to-derived-sections comparison. The page gives no complete spectral-sequence or acyclicity argument, so its force should be recorded as a stated criterion awaiting that verification.',
'C10',W,r'acyclic|sections|higher cohomology|spectral sequence')

add('N27','119','conjecture / self-flagged',r'et sans doute équivalente',
r'The converse to the quasi-flasqueness criterion is conjectural even in the wording. Necessity would require deriving degreewise flasqueness information from the stabilized global comparison, a separate issue from proving sufficiency.',
'C10',W,r'equivalent|sections|cohomology|flasque')

add('N28','119','reading question / proposed weakening',r'On peut ... affaiblir (4)',
r'The sloping margin proposes weakening condition (4), but the decisive dimension phrase is partly illegible. No definite replacement condition is extracted from it, and the supplied PS sheaf-cohomology discussion is a comparison rather than a source for filling the missing words.',
'C10',W,r'dimension|cohomology|sheaves|sections')

add('N29','119','unproved claim',r'on a déjà l\'existence',
r'The parenthesis claims existence of an admissible theory, with the local reading itself marked doubtful. Earlier scans are absent from the supplied context, so this package does not permit checking which construction and which hypotheses establish that existence.',
'C0',W,r'existence|first 45|package 49|De.Rham')

add('N30','119; 121','conjecture',r'On aimerait prouver un th. d\'unicité',
r'The uniqueness theorem is a stated aim and is then unpacked into localization and common-refinement conditions on 121. This is an open comparison problem within the manuscript, not a supplied theorem of canonical equivalence among all generalized theories.',
'C8',W,r'uniqueness|axiomati|different approaches')

add('N31','119','expectation / proposed method',r'on oublie d\'abord la structure p.d.',
r'The suggested first step is to forget divided powers while attempting uniqueness. Even if that weaker comparison succeeded, recovering a comparison preserving the PD structure would be an additional problem, especially for products after weight extraction.',
'C6',W,r'forget|divided powers|binomial')

add('N32','121','unproved claim',r'les hom. ... sont déjà des ``quasi-iso''',
r'Every allowed morphism is asserted to be a $\tau_\infty$ quasi-isomorphism. A proof must use both the quasi-resolution and quasi-flasque hypotheses, and cannot simply equate an arbitrary structured morphism with an ordinary quasi-isomorphism.',
'C10',W,r'weak equivalence|sections|quasi|resolution')

add('N33','121','conjecture / self-flagged',r'connexe et simplement connexe ?',
r'The groupoid generated by the admissible theories is conjectured to have one connected component and trivial automorphism group. This addresses uniqueness at the level of a groupoid localization, not by itself a contractible space of all higher coherent choices.',
'C8',W,r'uniqueness|groupoid|homotopy types')

add('N34','121','conjecture / self-flagged',r'Conj.? a)',
r'Two admissible theories are conjectured to admit a third with maps to both. The drawn common-refinement condition is a concrete test for constructing the desired comparison; the unheaded lower stroke has not been silently promoted to a directed arrow in the transcription.',
'C8',W,r'uniqueness|axiomati|comparison|cofilter')

add('N35','121','conjecture / self-flagged',r'qui ``égalise''',
r'Two parallel morphisms are conjectured to become equal after precomposition from another admissible theory. Together with nonemptiness and common refinements this would give a cofiltered-style sufficient condition, stronger than merely asserting connectedness of the localized groupoid.',
'C8',W,r'equaliz|filter|uniqueness|groupoid')

add('N36','121','self-flagged alternative',r'calcul de fractions à droite ???',
r'The margin explicitly doubts the chosen direction of the calculus of fractions and proposes the opposite direction. Any proof plan based on left fractions must therefore remain provisional and should explain which pushout or pullback constructions preserve admissibility.',
'C8',W,r'fractions|localization|uniqueness|adjoint')

add('N37','123','unproved claim',r'en vertu des axiomes sont en fait',
r'The coalgebra-side PD operations are asserted to land in the homogeneous symmetric power $\operatorname{Sym}^i_k(S^+)$. Verifying this requires specifying the polynomial-law/PD axioms and their homogeneity, especially over a general base ring rather than only a field.',
'C7',W,r'analyzer|polynomial|axioms|divided.power')

add('N38','123; 125','unproved claim',r'dans la cat des ... schémas affines',
r'The functor of structured PD differential algebras is claimed to be affine representable, and 125 begins the explicit representation. This is representability of an entire functor of coefficient algebras, so the proof should use the representing module and Yoneda, not an unjustified identification with a finite-dimensional linear dual.',
'C2',W,r'affine|representab|symmetric|functor')

add('N39','125','unproved claim',r'$\sum X_i-t,\sum dX_i$',
r'Eliminating the last coordinate gives the displayed completed PD-polynomial/exterior presentation with $n$ independent variables. A proof must specify the PD quotient and its completion so that substitution of $t-\sum_{i<n}X_i$ is legitimate and compatible with the differential.',
'C3',W,r'completion|divided powers|polynomial')

add('N40','125','reading question / possible missing hypothesis',r"$S^{k'}/(S^{k'})^+\unsure{\leftarrow}\bar S^{k'}$",
r'The written arrow and quotient comparison should not be silently replaced by a surjective restriction map. For arbitrary modules, $\operatorname{Hom}_k(S,k^{\prime})\to\operatorname{Hom}_k(\bar S,k^{\prime})$ need not be surjective; the coalgebra hypotheses or a suitable sheaf interpretation would have to supply any stronger exactness used here.',
'C2',W,r'sheaf|affine|exact|module')

add('N41','125; 127','unpursued implication',r'$S\otimes_k k[Y_0,\ldots,Y_{n-1}]\otimes_k\Lambda^*(y_0,\ldots,y_{n-1})$',
r'The explicit representing module explains why completed PD series on the cochain side correspond to an ordinary polynomial module on the chain side. This is a useful route to proving the duality claims degree by degree without assuming all modules are finite or reflexive.',
'C3',W,r'completion|dual|polynomial|divided powers')

add('N42','127','unproved claim',r'coalgèbre ... codifférentielle',
r'The representing objects are asserted to carry compatible coalgebra, codifferential and co-PD structures. Verification requires dualizing each natural operation and checking its identities, including the codifferential degree $-1$, rather than merely identifying the underlying modules.',
'C7',W,r'coalgebra|analyzer|operations|axioms')

add('N43','127','unproved claim',r'$\frac12$\inserted{co}simplicial',
r'The insertion changes the variance on the coalgebra side to cosimplicial, while the cochain functor remains contravariant. The face and degeneracy identities and their compatibility with all added structures are asserted rather than checked on these leaves.',
'C2',W,r'cosimplicial|semi.simplicial|functor')

add('N44','127; 129','unpursued implication',r'$\varinjlim_{\sigma\text{ ds }\Delta/X}A^{\dim\sigma}$',
r'The chain construction is the extension from standard simplices by the category-of-simplices colimit, and the displayed Hom–limit calculation explains the cochain representation. This yields functoriality at the ordinary categorical level; homotopy invariance and a comparison with singular chains remain additional assertions.',
'C11',W,r'colimit|homotopy colimit|integrator|simplex')

add('N45','129','withdrawn in the same text / explicit qualification',r'pas néc injectif p. ex. si $X=\varnothing$',
r'The author replaces the earlier-looking inclusion picture by a structural map $\bar S\to C_*^{\mathrm{DR}}(X,-)$ and explicitly observes that it need not be injective. The empty-set value is zero, so the quotient/augmentation data must be formulated with a cokernel and not with an assumed subobject for every $X$.',
'C2',W,r'empty|initial|coalgebra|augmentation')

add('N46','129','unproved claim',r'aux $\varinjlim$ quelconques (non seult filtrantes)',
r'Commutation with arbitrary colimits of $X$ is asserted in the margin and is suggested by the extension-from-simplices formula. This concerns ordinary colimits: the context register’s PATHS A.5 warns against replacing an ordinary colimit comparison by a homotopy-colimit statement without hypotheses, but its particular claimed counterexample is not reproved or imported as a theorem about these coalgebras.',
'C11',W+'; PATHS A.5',r'colimit|PATHS A\.5|homotopy colimit')

add('N47','129','unproved claim',r'comme foncteur en $(S,S^+,\gamma_*,t)$, il commute aux $\varinjlim$ quelc.',
r'The same arbitrary-colimit assertion is made in the category of coefficient data, where the PD/co-PD structures and the distinguished functional also vary. A proof must specify colimits in that structured category and verify that the polynomial/exterior representation carries the required universal property there.',
'C7',W,r'colimit|analyzer|operations|universal')

add('N48','129; 135','unproved claim',r'Commutation à l\'extension de l\'anneau de base',
r'Base-ring extension is announced as a heading and later expressed by an integral tensor formula. The natural linear base-change statement must be separated from a derived base-change assertion about cohomology or from extension of scalars for homotopy types, which is the different issue discussed in PS §124.',
'C9',W+'; WG H6',r'ground.ring|base.ring|module structure|extension')

add('N49','131','unproved claim',r'La diff. ... respecte le degré total',
r'The second grading is transported from the coefficient coalgebra, and compatibility of the differential and divided powers with both degrees is asserted. This compatibility is essential to the later extraction argument and needs checking on generators, the PD relations, and the quotient relation $\sum X_i=t$.',
'C6',W,r'graded|differential|divided powers')

add('N50','131; 133','unpursued implication',r'$S_k=k[u]$; $t(u^n)=1$ si $n=1$',
r'The specific polynomial coalgebra and coefficient-extraction functional provide an integral universal coefficient datum, whose dual is completed divided-power series in $T$. This is stronger evidence for an integral algebraic construction than an analogy with rational minimal models, but it leaves the eventual cohomology/product comparison to be proved.',
'C3',W,r'divided powers|completion|universal polynomial|integral')

add('N51','133','unproved claim',r'avec toutes les structures',
r'The identification with the Hom-valued functor is asserted to recover all structures, including the bigrading. Proving this requires naturality in every coefficient algebra and compatibility of the representing maps for multiplication, differential and PD operations; an isomorphism of underlying groups alone is insufficient.',
'C7',W,r'operations|analyzer|structure|functor')

add('N52','135','unproved claim',r'$C_*^{DRpd}(X,k)\simeq C_*^{DRpd}(X)\otimes_{\mathbf Z}k$',
r'The displayed formula defines a family over arbitrary coefficient rings from an integral chain object. It does not by itself imply that tensoring cohomology with $k$ computes the new cohomology, since derived tensor effects require their own flatness or homological argument.',
'C9',W,r'ground.ring|module|tensor|extension')

add('N53','135','reading question',r'$\operatorname{Hom}(C_*^{DRpd}(X,k))$',
r'The first displayed cochain Hom has only one visible argument in the frozen text, while the later formula with an abelian group $M$ has both source and target. A target such as $k$ is mathematically plausible but is not supplied by the ink or by the context, and has therefore not been inserted.',
'C0',W,r'Hom|cochains|De.Rham')

add('N54','135','unproved claim',r'une ... de structures multiplicatives',
r'The conclusion promises multiplicative structures on the functors in arbitrary abelian-group coefficients $M$. Such a statement should specify external pairings with targets involving $M\otimes N$, or extra multiplication on the coefficients, since a general abelian group has no canonical internal product.',
'C7',W,r'multiplicative|tensor|operations|coefficients')

add('N55','137, cancelled upper draft','withdrawn by cancellation / unproved claim',r'ce qui est évident, car; Comme les $\sigma^*$ commutent',
r'The upper argument about inverse-image functors and limits is cancelled as a block, including its diagrams. Its cancellation records abandonment of this draft argument, not evidence that every statement inside it is false; the surviving Stokes discussion below should not be made dependent on it.',
'C10',W,r'limits|inverse.image|sheaves|sections')

add('N56','137','unproved claim',r"c'est l'identité si $n=0$",
r'The proposed dual Stokes homomorphisms are required to restrict to the identity in dimension zero. Constructing them in all dimensions still needs a compatible normalization, and the explicit coefficient calculation only begins on 139–141.',
'C6',W,r'De.Rham|integrat|identity|cochains')

add('N57','137','self-flagged calculation / reading question',r'Stokes; $d\kappa_n=\partial_{ss}\kappa_{n-1}$',
r'The square, the marginal degree labels, and the cancelled alternative formula show active checking of variance and degree conventions. A valid chain map requires the exterior differential and semisimplicial boundary signs to match; the supplied PS uses “integration” for homotopy colimits and supplies no Stokes sign convention for this calculation.',
'C11',W,r'Stokes|integrat|differential|boundary')

add('N58','137','unproved claim',r'$C_*^{\mathrm{sing}}(X,k[u])\longrightarrow C_*^{DRpd}(X,k)$',
r'A natural comparison from singular chains with the additional coefficient algebra is displayed. Its existence is not a proof of a quasi-isomorphism, and the coefficient $k[u]$ itself warns against identifying the entire target with ordinary $k$-chains before applying the intended grading or extraction.',
'C6',W,r'cochains|De.Rham|linearization|integral')

add('N59','139','unproved claim',r"l'image est ... l'intersection des noyaux des ... op. diff.",
r'The image of $k[Z_0,\ldots,Z_n]\to k[U,Y_0,\ldots,Y_n]$, $Z_i\mapsto U+Y_i$, is described using all divided differential operators associated with $\sum\partial_{Y_i}-\partial_U$. Over rings with torsion, the phrase “all” matters: the kernel of the first ordinary derivation alone can contain extra $p$th powers, so it cannot replace the displayed family.',
'C3',W,r'polynomial|divided powers|differential|torsion')

add('N60','139','unproved claim',r"l'image est le noyau de $i_X$",
r'The dual of the exterior quotient is identified with the exterior algebra on the kernel of the sum-of-coordinates functional. The contraction characterization is compatible with a split rank-one quotient, but proving the claimed canonical top-degree identification requires fixing the determinant convention and the orientation used by Stokes.',
'C3',W,r'dual|exterior|canonical|polynomial')

add('N61','139','reading question',r"$[y_0,\ldots,y_n]^{!|'}$",
r'The frozen readings explicitly distinguish the uncertain exclamation-like and prime-like superscripts on the zero-sum submodule. The later exact sequence uses a prime-like mark, but neither its algebraic role nor the absence of matching notation in the context resolves each individual stroke.',
'C0',W,r'zero.sum|coordinates|exterior|De.Rham')

add('N62','139','reading question',r'On a un isom can',
r'If the displayed ambient module really has basis $y_0,\ldots,y_n$, it has rank $n+1$, and its zero-sum kernel has rank $n$. The determinant sequence would then compare $\bigwedge^n K$ with $\bigwedge^{n+1}V$, so the visible exponents raise an indexing question; this conditional algebraic check does not alter the frozen exponents.',
'C0',W,r'exterior|rank|determinant|De.Rham')

add('N63','141','unproved claim',r'un entier canonique',
r'The normalized simplex integral is asserted to define an integer coefficient $\gamma_{i_0,\ldots,i_{n-1}}$. The integral formula permits a direct proof under the usual positive orientation, but the page itself does not complete that proof before developing its recurrence; our separate calculation is recorded in O05.',
'C6',W,r'integral|De.Rham|divided powers|coefficient')

add('N64','141','self-flagged question',r'$\frac1{n!}\gamma_{0,0,\ldots,0}\overset?=\frac1{n!}$',
r'The question mark explicitly leaves the zero-index normalization open at this stage of the calculation. It is a question about the simplex volume/normalization, not evidence for a global integral cohomology comparison.',
'C6',W,r'integral|normaliz|De.Rham|coefficient')

add('N65','141','withdrawn in the same text / reading question',r'\deleted{$(-1)^{i_{n-1}+1}$}',
r'The outer sign survives in an intermediate line and is cancelled in the final recurrence, while other sign corrections occur earlier in the Stokes expansion. With the final inner sign written as $(-1)^{\sum\ell_\alpha}$, the deleted prefactor would change the answer when $i_{n-1}+1$ is odd; an inner sign written instead as $(-1)^\lambda$ would compensate for it, so the two conventions must not be conflated.',
'C11',W,r'Stokes|sign|integrat|boundary')

add('N66','141','insertion / reading question',r'$C_{\lambda,n-1+\sum_0^{n-2}(\ell_\alpha+i_\alpha)}$',
r'The inserted factor is indispensable in the final candidate recurrence if $C_{a,b}$ means $\binom{a+b}{a}$. The package does not explicitly define that notation here, and the earlier placement of a similar insertion inside a still unevaluated $\kappa_{n-1}$ expression should be checked separately from the mathematically coherent final recurrence; no formula has been rewritten.',
'C6',W,r'binomial|divided powers|integral|coefficient')

add('R01','095; 105; 101, reused typescript, §13.2','unpursued implication',r'il est déterminé à isomorphisme unique près',
r'The formal-rigidity lemma has its proof distributed across these physically out-of-order sheets: its statement is on 095, the Nakayama argument on 105, and the conclusion on 101. It is therefore not an unproved lemma within the surviving material, but its hypotheses on the constant period lattice and spanning property provide a separate rigidity mechanism that should not be transferred to generalized de Rham theories.',
'C3','No directly relevant RESULTS_STATE item',r'formal|completion|uniqueness|rigid')

add('R02','097, reused typescript, §12.4','unpursued implication',r'sans ambiguïté de signe; défini positif',
r'The sign ambiguity in each branch functional disappears after taking its tensor square, and positivity follows from the displayed embedding into the standard integral quadratic lattice. This is an explicit integral pairing in the donor text, but the sheet does not relate it to PD cochains or to the planning register’s integral Lefschetz-ring lead.',
'C0',W,r'Lefschetz|pairing|positiv|integral')

add('R03','099, reused typescript, §13.1','self-flagged admitted construction',r"Nous admettrons ici la définition de l'homomorphisme exponentiel",
r'The exponential homomorphism is admitted, with only a construction sketch using characteristic-zero formal groups and multiplicative continuation. Establishing the quoted étaleness, image, and base-change properties requires the omitted analytic-group argument; this admission belongs to the reused SGA material.',
'C3','No directly relevant RESULTS_STATE item',r'exponential|formal group|characteristic zero')

add('R04','101, reused typescript, Corollary 13.2.2','reading question',r'les conditions a), b), c) de 13.2.2',
r'The corollary refers to its own number for conditions actually displayed in Lemma 13.2.1 on 095. This is an internal reference question already visible without external correction; the frozen text preserves the self-reference.',
'C0','No directly relevant RESULTS_STATE item',r'13\.2\.2|13\.2\.1|Raynaud')

add('R05','101, reused typescript, §13.3','unproved claim / proof sketch',r'évidemment le plus grand sous-groupe constant',
r'The construction of the fixed period subgroup uses shrinking around the base point and a finite-generation argument. Its maximality is asserted without a separate proof here, and any proposed analogy with a universal de Rham object must first specify whether it is a local analytic or a categorical universal property.',
'C3','No directly relevant RESULTS_STATE item',r'constant|universal|formal|completion')

add('R06','103, reused typescript, §12.10','unproved claim by reference to absent argument',r'La démonstration donnée dans 12.8 nous fournit un résultat plus général',
r'The weighted monodromy pairing $\sum d_\lambda\varphi_{x_\lambda}\otimes\varphi_{x_\lambda}$ is deduced from a proof and multiplicities in §12.8 that are not included here. It extends the unweighted pairing of 097, but its derivation and hypotheses cannot be checked from this package alone.',
'C0',W,r'monodrom|Lefschetz|pairing|integral')

add('R07','103, reused typescript, Remark 12.9','unproved claim / example',r'une ou deux composantes irréductibles',
r'The donor text relates the one-node degeneration to the ranks one and zero of the character module, with good reduction of the generic Jacobian in the latter case. This is a concrete abelian-variety example physically present in the package, but it is not presented as an example of the PD lecture.',
'C0','No directly relevant RESULTS_STATE item',r'Jacobian|jacobien|abelian|abélien|Lefschetz')

add('R08','107, reused typescript, §13.1.4','unproved claim',r'une équivalence de catégories, compatible aux changements de base',
r'The equivalence between smooth connected relative analytic groups and vector bundles with an étale lattice is stated following the exponential sequence. It belongs to analytic uniformization; no comparison functor to the integral semisimplicial de Rham construction is supplied.',
'C2','No directly relevant RESULTS_STATE item',r'analytic|étale|equivalence|group schemes')

add('R09','107, reused typescript, §13.1.5','unproved claim / example',r'Lorsque $A$ est un groupe ``abéloïde''',
r'The rank-$2\dim$ locally constant lattice and complex structure describe the donor text’s abeloid families. Their presence answers the literal question about abelian objects among the sheets, but does not establish that Grothendieck selected them as examples for this lecture.',
'C0','No directly relevant RESULTS_STATE item',r'abélo|abeloid|abelian variet|complex structure')

add('R10','112, reused typescript, §10.2','unproved claim',r'compatible, en un sens évident',
r'Compatibility of the monodromy pairing with pullback of biextensions is asserted without the diagram chase. Its verification needs the variance of the character modules and the induced morphism of Néron models, rather than only a symmetric bilinear formula.',
'C0','No directly relevant RESULTS_STATE item',r'biextension|monodrom|Néron|character')

add('R11','112; 114; 116, reused typescript, §10.2','unproved claim',r'on a alors la relation de symétrie',
r'The symmetry identity is reformulated using dual abelian schemes, polarizations, and general biextensions. The text points to an earlier antisymmetry result and leaves the formal checks to the reader, so the displayed agreement of signs is a target for verification in the donor argument, not part of the manuscript’s Stokes calculation.',
'C0','No directly relevant RESULTS_STATE item',r'biextension|symmetr|monodrom|duality')

add('R12','114, reused typescript, §10.2','unpursued implication / qualification',r'pas nécessairement une polarisation',
r'The symmetry statement extends to arbitrary Néron–Severi classes, while recovering the original pairing symmetry from it requires a nondegenerate class. This distinction prevents turning a statement about a chosen bilinear form into an equivalence without the isogeny hypothesis.',
'C0','No directly relevant RESULTS_STATE item',r'Néron|polariz|polarisa|symmetr')

add('R13','116, reused typescript, introduction to §10','self-flagged verification left to reader',r'le détail ... des vérifications étant laissé au lecteur',
r'The formal properties, especially transport of structure and symmetry, are explicitly not checked in detail in these sheets. This standing qualification applies to the claims on 112–116 and should be preserved even though the author regards them as routine.',
'C0','No directly relevant RESULTS_STATE item',r'monodrom|verification|symmetr')

add('R14','114; 116; 124; 138, reused typescript, references to §10.4','self-flagged deferred proof',r'qui sera traité (par voie transcendante) au par. 12',
r'The deeper integrality/positivity theorem is announced, invoked, and deferred to a Jacobian reduction and a transcendental calculation. The donor sheets include relevant fragments on 097 and 103 but neither the statement of §10.4 nor the full reduction, so the whole theorem is not certified by this package.',
'C0',W,r'integral|Lefschetz|positiv|monodrom')

add('R15','116, reused typescript, §10.2','reading question',r"le schéma dual $(A'_K)'$ de $A_K$",
r'The phrase names the bidual expression while saying “of $A_K$”; the next clause identifies it canonically with $A_K$. Reading the phrase as referring instead to the dual of $A^{\prime}_K$ would restore the expected sequence, but the frozen text is left literal.',
'C0','No directly relevant RESULTS_STATE item',r'bidual|duality|dual|abelian')

add('R16','124, reused typescript, §9.7','unproved claim by deferred reference',r"n'en dépend pas; est indépendant de $\ell$",
r'Independence from the semistable extension and from the prime, together with rationality of the normalized pairing, is referred to the absent theorem 10.4. The factor $1/e(S^{\prime}/S)$ is part of the construction and cannot be discarded when discussing integrality.',
'C0',W,r'monodrom|integral|independen|Lefschetz')

add('R17','124, reused typescript, §9.7','question / self-flagged',r"On peut se demander s'il est à valeurs dans $\mathbb Z_K$",
r'This is an explicit integrality question for the monodromy pairing after passage from potentially semistable reduction. It concerns an arithmetic pairing on character modules, whereas the planning register’s PD-cochain thread concerns a different integral structure; a bridge between them is not supplied.',
'C0',W,r'integral|Lefschetz|monodrom|divisib')

add('R18','124, reused typescript, §9.7','unproved claim / example',r"C'est le cas du moins si $A_K$ est une courbe elliptique",
r'The elliptic case is claimed by appeal to Néron’s results, with the rank-one pairing identified as a rational number. The cited source and the preceding definitions of the lattice are absent, so this asserted special-case resolution is recorded without independently certifying its derivation.',
'C0','No directly relevant RESULTS_STATE item',r'elliptic|elliptique|Néron|monodrom')

add('R19','124, reused typescript, §9.7','reading question',r'égal à $v(j)$',
r'The valuation formula is preserved exactly. Before combining it with the positivity statements elsewhere on the donor sheets, one must check both the valuation convention and the chosen identification of the two rank-one character lattices; the expected sign is not a reason to insert a minus sign.',
'C0','No directly relevant RESULTS_STATE item',r'valuation|elliptic|positiv|monodrom')

add('R20','126, reused typescript, §9.6','self-flagged conditional claim',r'sous réserve de la validité du théorème de TATE',
r'The recovery of the filtration and extensions from the sole Barsotti–Tate pro-group is conditional on Tate’s theorem, with characteristic zero singled out as available. The conditional formulation is part of the historical text and should not be silently updated using later literature.',
'C0','No directly relevant RESULTS_STATE item',r'Tate|Barsotti|characteristic|filtration')

add('R21','126, reused typescript, §9.6','reading question',r'$X_\eta/X_\eta^2\simeq F_\eta=D(F^{\prime}_\eta)$',
r'The quotient is labelled $F_\eta$, whereas the neighbouring construction on 128 defines $E=D(F^{\prime})$ and distinguishes extensions by $P$ from extensions by $R$. This gives an internal candidate $E_\eta$ for the disputed label, but no substitution is made in the frozen transcription.',
'C0','No directly relevant RESULTS_STATE item',r'Barsotti|panach|Cartier|9\.6')

add('R22','128, reused typescript, §9.5.8','self-flagged verification left to reader',r"La vérification de l'identité des deux définitions est alors laissée au lecteur",
r'The comparison between the extension-based pairing and the inertia-action pairing is explicitly omitted after a reduction to finite coefficients. It is the missing compatibility needed to use the new definition uniformly for all primes while recovering the earlier one for $\ell\ne p$.',
'C0','No directly relevant RESULTS_STATE item',r'inertia|inertie|monodrom|Barsotti')

add('R23','130, reused typescript, Remark 9.5.6.4(a)','conjecture / self-flagged expectation',r'devrait être valable sans restriction sur $K$',
r'The characteristic restriction is expected to disappear because the invoked Tate theorem is expected to hold without it. This is an expressly prospective statement on the donor sheet, not a new conjecture about the PD construction.',
'C0','No directly relevant RESULTS_STATE item',r'Tate|characteristic|expect|conjectur')

add('R24','130, reused typescript, Remark 9.5.6.4(b)','unproved claim / alternative proof sketch',r'On peut donner une autre démonstration du critère de bonne réduction',
r'The proposed alternative proof combines the mixed-extension criterion, vanishing monodromy, and the absent statement 11.6.2(a). The latter implication is essential to conclude vanishing of the toric part, so the sketch is not a self-contained proof in this package.',
'C0','No directly relevant RESULTS_STATE item',r'good reduction|bonne réduction|Tate|monodrom')

add('R25','132, reused typescript, §9.5.6.3','self-flagged extension left to reader',r'Nous laissons au lecteur le soin d\'étendre cet énoncé',
r'The suggested extension replaces the trait by a connected regular noetherian scheme of dimension one. A proof must glue the local extension and vanishing-pairing conditions and check the global uniqueness, rather than merely repeat the henselian-local argument.',
'C0','No directly relevant RESULTS_STATE item',r'regular|dimension one|Barsotti|étale')

add('R26','134, reused typescript, §9.5','self-flagged verification left to reader',r'les homomorphismes (9.5.4) définissent un homomorphisme de systèmes projectifs',
r'Compatibility of the finite-level pairings with transition morphisms is explicitly left to the reader. This is what makes the $\ell$-adic pairing well defined, and it must be checked with the Cartier-dual transition conventions rather than inferred from existence at each level.',
'C0','No directly relevant RESULTS_STATE item',r'projective|Cartier|transition|pairing')

add('R27','134; 132; 130, reused typescript, Proposition 9.5.6','unpursued implication',r'qui ne sera pas utilisé dans la suite',
r'The proposition on extending mixed Barsotti–Tate extensions is explicitly marked unused in the subsequent development. Its proof is nevertheless partly present on 132–130, so it should be catalogued as an unused method with referenced hypotheses, rather than as a wholly unproved assertion.',
'C0','No directly relevant RESULTS_STATE item',r'Barsotti|extension|faithful|Tate')

add('R28','136, reused typescript, end of §9.4','unproved claim by reference to missing construction',r'la conclusion est vraie par construction',
r'The proof reduces extension from the generic point to the strictly local case using uniqueness and étale locality. The construction just before 9.4.6 is absent, so the final reduction is visible but its base case cannot be audited from the included sheets.',
'C0','No directly relevant RESULTS_STATE item',r'étale|extension|local|Barsotti')

add('R29','138, reused typescript, Theorem 11.5','unproved claim',r'alors on a un isomorphisme canonique',
r'The theorem identifies the component-group contribution with the cokernel of the monodromy map for semistable reduction. No proof of the theorem is included on this sheet; the claimed perfect pairing of component groups is then a consequence of it and the previously stated symmetry.',
'C0','No directly relevant RESULTS_STATE item',r'component group|monodrom|cokernel|duality')

add('R30','138, reused typescript, Remark 11.5.2(a)','unpursued implication / proof-dependency warning',r"y compris dans le cas $\ell=p$; nous n'utilisons pas ici le théorème ... 10.4",
r'The separating property at the residue characteristic is singled out as nontrivial and logically independent of the deeper integrality theorem. Keeping this dependency separate avoids a circular proof if the donor fragments are reconstructed in mathematical order.',
'C0','No directly relevant RESULTS_STATE item',r'characteristic|monodrom|integral|duality')

add('R31','140, reused typescript, §11.3','unproved claim by external reference',r'Il est bien connu que ces accouplements sont des dualités parfaites',
r'The finite-module dualities are invoked through SGA 5, I, §5, rather than proved. The needed cohomological dimension, dualizing module, and finiteness assumptions belong to that cited argument and are not supplied by the displayed pairing alone.',
'C0','No directly relevant RESULTS_STATE item',r'perfect|duality|inertia|cohomological dimension')

add('R32','140, reused typescript, §11.3','unproved claim',r'par passage à la limite un accouplement parfait',
r'Two successive limit arguments are asserted to preserve perfectness. A reconstruction must identify the direct and inverse systems and their topologies, because perfect finite pairings do not alone specify the meaning of perfectness after either limit.',
'C0','No directly relevant RESULTS_STATE item',r'limit|perfect|duality|finite')

add('R33','140, reused typescript, formula 11.3.13','reading question',r'$H^0(I,U\otimes\mathbb Q_\ell)\times H^1(I,U^{\prime}\otimes\mathbb Q_\ell)\longrightarrow D_\ell$',
r'The target remains $D_\ell$ in the frozen line although the next words call the factors finite-dimensional $\mathbb Q_\ell$-vector spaces. The definition of $D_\ell$ and the limit transition maps must be recovered before replacing that target or interpreting the assertion as a bilinear perfect pairing over $\mathbb Q_\ell$.',
'C0','No directly relevant RESULTS_STATE item',r'D_ell|duality|rational|limit')

add('O01','111–117; 131–135','own idea — obstruction test',r'structure ... de puissances divisées',
r'An ordinary integral cochain algebra with $\gamma_2$ defined on every positive even cocycle, satisfying $z^2=2\gamma_2(z)$ and $d\gamma_2(z)=z\,dz$, cannot recover the cup-product ring of $\mathbf{CP}^2$: choosing $[z]=x\in H^2$ would make the primitive class $x^2\in H^4\cong\mathbf Z$ divisible by two. This uses one chosen cocycle and does not assume that PD operations descend to cohomology (Stacks Project, tags 09PG, 09PJ; Hatcher, 2002, Theorem 3.12, revised online numbering 3.19). The manuscript’s extra weight, coefficient algebra, restricted PD domain, or $\tau_\infty$ could avoid these hypotheses, so this is a test of the strong unqualified interpretation, not a disproof of the historical construction.',
'C6',W,r'divided powers|cohomology|commutative algebra|binomial','high; the stated identities force a contradiction in a rank-one integral cohomology group')

add('O02','131; 133; 135; 137','own idea — point diagnostic',r'$S_k=k[u]$; $C_*^{\mathrm{sing}}(X,k[u])$',
r'If the represented zero-simplex is sent to $A^0=S=k[u]$ concentrated in exterior chain degree zero and $u$ remains a separate weight, then the unprocessed object has $H_0=k[u]$, whereas ordinary $k$-chains on that simplex have $H_0=k$. This forces an explicit coefficient or extraction convention before claiming an ordinary integral comparison; it does not determine what the missing definition of $\tau_\infty$ does. The diagnosis changes if $u$ has positive total chain degree, and a represented zero-simplex must not be confused with the terminal semisimplicial presheaf.',
'C6',W,r'linearization|module structure|De.Rham|cohomology','high under the three stated grading and evaluation hypotheses; no claim about an undefined realization')

add('O03','113; 117; 135; 141','own idea — elementary product recovery',r'structures multiplicatives',
r'The elementary identity $\gamma_r\gamma_s=\binom{r+s}{r}\gamma_{r+s}$ explains how weight-sensitive products can determine an ordinary integral product without any individual coefficient being one. If the pairs $(2,2),(2,3),(3,4)$ lie in the comparison range and their transported products satisfy $P_{r,s}=\binom{r+s}{r}\mu$ for one product $\mu$, then $\mu=P_{2,2}+3P_{2,3}-P_{3,4}$ because $6+3\cdot10-35=1$. For a family containing all sufficiently large independent weight pairs, choosing, for each prime $\ell$, large distinct powers $r=\ell^N$ and $s=\ell^{N+1}$ makes $\binom{r+s}{r}\not\equiv0\pmod\ell$, since $(1+z)^{r+s}\equiv(1+z^r)(1+z^s)\pmod\ell$; hence the family of coefficients has gcd one.',
'C7',W,r'binomial|divided powers|operations|integral','high; explicit Bézout identity and elementary polynomial proof, illustrating rather than claiming novelty for the published recovery principle')

add('O04','111; 117; 131','own idea — separate weight from cochain degree',r'algèbres bigraduées',
r'If multiplication adds weights, a fixed-weight complex is generally not a subalgebra: $A^{*,r}\otimes A^{*,s}\to A^{*,r+s}$. Consequently an additive comparison in each weight cannot, by itself, be described as an isomorphism of ordinary rings; the comparison must include the coefficient pairings or a proved extraction that handles them.',
'C6',W,r'graded|divided powers|cohomology|binomial','high; follows directly from the two degrees and the type of the multiplication map')

add('O05','141','own idea — verification of the displayed normalization',r'$\gamma_{i_0\ldots i_{n-1}}$',
r'For nonnegative integral indices and the positively oriented standard simplex, the beta-integral calculation gives $\int_{\sum x_a\le1,\,x_a\ge0}\prod x_a^{i_a}\,dx=\prod i_a!/(n+\sum i_a)!$, so the normalization written on 141 yields $\gamma_i=1$. Thus it resolves the zero-index question and integrality under those conventions; it does not establish the global cohomology comparison. A self-contained induction by slicing the simplex, including the dimension-zero convention, is in `records/pd_diagnostics.md` (compare NIST DLMF, §5.14).',
'C11',W,r'Stokes|integrat|coefficient|De.Rham','high under the explicit orientation and index conventions; the factorials cancel by the exact simplex integral')

add('O06','141','own idea — verification of the final recurrence',r'On peut aussi calculer par ... récurrence sur $n$',
r'Assuming $C_{a,b}=\binom{a+b}{a}$, set $r=n-1$, $A=\sum_{a<r}i_a$, $m=i_{n-1}+1$, and $L=\sum_{a<r}\ell_a$: the final inserted-factor recurrence with lower-dimensional coefficients one is the coefficient of $z^m$ in $(1+z)^{A+r+m}\prod_{a<r}(1+z)^{-i_a-1}=(1+z)^m$, hence equals one. Omitting $C_{\lambda,r+A+L}$ fails already at $n=2,i=(0,0)$, where the resulting sum is zero. The dimension-one edge case and 1,364 exact small-index checks agree with this proof, while the intermediate sign and insertion placements remain reading questions rather than repaired manuscript text.',
'C11',W,r'Stokes|binomial|integrat|divided powers','high for the explicitly normalized recurrence; the manuscript’s earlier definition of C and orientation are not supplied')

add('O07','139','own idea — why all divided differential operators matter',r"l'intersection des noyaux",
r'Under the change of variables $Z_i=U+Y_i$, simultaneous translation $Y_i\mapsto Y_i+h$, $U\mapsto U-h$ fixes every $Z_i$. Requiring every positive coefficient of this translation to vanish is equivalent, over any coefficient ring, to independence of $U$ in the coordinates $(U,Z_i)$, whereas the first derivative alone also kills $U^p$ in characteristic $p$. This supplies a direct algebraic route to the image characterization if the manuscript’s operators are precisely these Hasse coefficients.',
'C3',W,r'polynomial|divided powers|characteristic|differential','high conditional on the Hasse-operator interpretation; the coordinate change and coefficient argument are explicit')

add('O08','119; 121','own idea — level of uniqueness',r'connexe et simplement connexe ?',
r'The ordinary groupoid completion records only $\pi_0$ and $\pi_1$ of the original category’s nerve; its equivalence to the terminal groupoid does not force that original nerve to be weakly contractible. To obtain a contractible moduli space of de Rham theories, one would need a model for the full coherent space of comparisons and a proof that its higher homotopy groups vanish; common refinements and equalization as a cofiltered-category argument might provide such a stronger route only after their hypotheses are established.',
'C8',W,r'uniqueness|contractib|groupoid|axiomati','high for the distinction; the proposed higher-coherent repair is a method to investigate, not a theorem about these categories')

add('O09','109; 111–121, comparison to the planning register','own idea — diagnostic for an incomplete hunch',r'foncteurs de De Rham',
r'If the displayed fragment of WG H6 were interpreted as saying that equivalence on finite-dimensional local systems alone detects characteristic-zero schematic equivalence, $S^2\to *$ would be a counterexample: both have the same local systems but different rational higher homotopy. This tests only the truncated criterion printed in the supplied register, not the unseen full hunch, which could include higher cohomology with local coefficients. It motivates keeping the cohomological and higher-homotopical information of the de Rham construction in any comparison.',
'C8',H,r'WG H6|local systems|schematization|higher homotopy','high for the stated elementary example; low for applicability to the unavailable full hunch')

add('O10','123–133, compared with PS §119','own idea — divided powers versus binomial operations',r'$S_k=k[u]$',
r'The integer-valued polynomial $x(x-1)/2$ and the divided-power expression $x^2/2$ already differ on integral inputs, so the binomial and PD constructions cannot be identified merely by replacing operation names. A useful bridge would have to specify the relevant algebra or coalgebra, filtration, and comparison map, retaining the completed dual where it occurs.',
'C6',W+'; '+H,r'binomial|integer values|integral coefficients|divided powers','high for the arithmetic distinction; the proposed bridge remains a research problem')

add('O11','125; 127; 133; 139','own idea — finite support and completed duals',r'$\widehat\Gamma$; $k\{\{T\}\}$',
r'The dual of a direct sum of finite free weight pieces is a product, so formal PD series and finite PD polynomials are different objects before any grading restriction. A comparison with a published finite-weight model should first be made weight by weight, where the duality can be finite, and only then extended to sums or products with an explicit continuity convention.',
'C3',W,r'completion|product|homogeneous|divided powers','high for the direct-sum/product duality; convergence and exactness of the proposed extension are not established')

add('O12','127; 129','own idea — universal extension versus homotopy invariance',r'commutant aux ... inductives',
r'Extending a simplex assignment by an ordinary colimit gives a categorical universal construction, but does not automatically make that extension invariant under weak equivalences of semisimplicial sets. One should prove the needed acyclicity/extension property or compare with a derived colimit; the register’s PATHS A.5 is only an unreviewed warning about a different Cat-valued ordinary-colimit problem and is not imported as a theorem here.',
'C11','PATHS A.5; '+W,r'PATHS A.5|homotopy colimits|integration|colimit','high as a distinction between universal and derived properties; no counterexample to the full manuscript construction is asserted')

add('L01','111–117; 123; 125; 131; 133; 135; 137, historical comparison','own idea — literature comparison',r'Complexes de données de De Rham à p.d.',
r'Cartan (1976, §7, pp. 269–271) attributes his account to Grothendieck’s IHÉS lecture of 12 December 1975: his weighted model has $H^n(Gr^{*,r}(X))\cong H^n(X;\mathbf Z)$ for $r\ge n$ and zero for $r<n$, while identifying coefficient generators with one turns the weight-$(r,s)$ product into $\binom{r+s}{r}$ times cup product. He recovers the ordinary product from the whole family because those integers are collectively coprime. This is a close published parallel, but its coefficient algebra $\Gamma_{\mathbf Z}(t)$, finite weights, and precise model must be matched to the manuscript’s dual, completed, and extracted objects before transferring its theorem.',
'C6',W,r'Cartan|De.Rham|divided powers|integral','high for the published statement, directly checked on the printed pages; a literal identification with the manuscript is not proved')

add('L02','113; 135; 141, multiplicative comparison','own idea — literature comparison',r'structures multiplicatives',
r'Cenkl and Porter (1982, Proposition 1, p. 10) compare forms with cochains valued in the weight module $\Gamma_q$, in degrees $p<q$, using cup product followed by $\Gamma_q\otimes\Gamma_r\to\Gamma_{q+r}$. Their integration map is not strictly multiplicative on cochains; Theorem 1 gives higher-homotopy multiplicativity. This supplies a concrete target for the manuscript’s product claim while retaining both the coefficient pairing and the level of coherence.',
'C7',W,r'multiplicative|cochains|divided powers|operations','high for the stated comparison; no unconstructed chain map to the present manuscript is claimed')

add('L03','117; 119; 141, range of comparison','own idea — literature comparison',r'quasi-iso',
r'Garvín et al. (1998, Theorem 4.2, p. 176) extend a Miller-type divided-power theorem to arbitrary simplicial sets over any commutative coefficient ring with unit, with the explicit range $p<q$. Their normalized map $q!\int$ is defined integrally on basis forms, so the notation is not an instruction to divide in the coefficient ring. This strict endpoint is kept separate from Cartan’s inclusive $r\ge n$ statement; matching the constructions and conventions is still required.',
'C6',W,r'Cartan|cochains|integral|De.Rham','high for the printed inequalities; their relationship to the manuscript’s uniform bound is not established')

add('L04','117; 129; 131; 135, alternative integral approximation','own idea — literature comparison',r"Commutation à l'extension de l'anneau de base.",
r'Cenkl and Porter’s cubical theorem (1984, §4, Theorems 4.1–4.2) uses a simplicial complex of finite type and coefficient rings $Q_q=\mathbf Z[1/2,\ldots,1/q]$, $q\ge1$, with products landing over $Q_{q_1+q_2}$. It provides a filtered comparison with cup products after these localizations, not an unchanged integral coefficient theorem for the entire filtered object.',
'C9',W,r'ground.ring|integral|cohomology|De.Rham','high for the explicit coefficient restriction; this is a different comparison model')

add('L05','109; 117; 131; 135, tame comparison','own idea — literature comparison',r'$k[u]$',
r'Dwyer’s tame theory, as described by Scheerer and Tanré (1991, §0, pp. 376–377), uses $r\ge3$ and an increasing system of degree-dependent subrings $R_j\subset\mathbf Q$, $j\ge0$ in which the integers $k$ with $2k-3\le j$ are invertible. It compares localized homotopy groups $\pi_{r+k}\otimes R_k$ with differential graded Lie algebra homology $H_{r-1+k}\otimes R_k$, so it is not a theorem about unrestricted integral PD cochains. The original Dwyer article was not retrieved, and the precise statement here is sourced to this directly checked primary exposition.',
'C8',W+'; '+H,r'rational|localiz|homotopy|Lie','high for the stated limitation of the cited framework; it does not identify a tame range for this manuscript')

add('L06','109; 111–121; 135, integral homotopy benchmark','own idea — literature comparison',r'cohomologie de De Rham associée',
r'Mandell (2006, Main Theorem and Theorem 0.1) classifies finite-type nilpotent spaces by integral singular cochains as $E_\infty$ algebras; the cochain functor on homotopy categories is faithful but not full. This benchmark is stronger than recovering the cohomology ring and uses specified coherent operations, so the manuscript’s product and PD data alone do not establish its conclusion.',
'C8',H+'; '+W,r'homotopy type|nilpotent|cohomology|schematization','high for the theorem’s hypotheses and categorical distinction; an E-infinity comparison for the manuscript is absent')

add('L07','109; 111–121, prime-by-prime benchmark','own idea — literature comparison',r'nilpotent quotient',
r'Mandell (2001, Main Theorem) gives a fully faithful description on homotopy categories for connected $p$-complete nilpotent spaces of finite $p$-type using $E_\infty$ algebras over $\overline{\mathbf F}_p$. The algebraic closure and the completeness and finiteness assumptions are part of this statement; it cannot be substituted for the integral theorem or for the donor sheet’s unrestricted rational-language claims.',
'C8',H,r'nilpotent|completion|prime|schematization','high for the exact coefficient and space restrictions; no integral conclusion is inferred')

add('L08','109; 123–133, numerical-model comparison','own idea — literature comparison',r'$S_k=k[u]$',
r'Ekedahl (2002, Theorem 2.9 and Lemma 2.8) models connected nilpotent spaces with finitely generated homology in each degree using numerical maps, namely rational polynomials taking integral values on integral inputs. Numerical cochains recover cohomology and the mapping comparison between these special models is up to numerical homotopy (based maps in Lemma 2.8), while minimal models need not be strictly isomorphic. This offers a precise later alternative to ordinary integral polynomial maps, not an identification with the completed PD dual on these scans.',
'C4',H+'; '+W,r'polynomial|integer values|integral coefficients|nilpotent','high for the distinction of algebraic structures and the cited result; the historical comparison map remains open')

add('L09','111–133, integral schematization comparison','own idea — literature comparison',r'foncteurs de De Rham généralisés',
r'Toën (2020, Theorem 0.1) treats simply connected spaces of finite type: integral affinization has homotopy sheaves $\pi_i(X)\otimes\mathbb H$, where $\mathbb H$ is the Hilbert additive group, and the map to its integral points has a functorial retraction. The resulting faithfulness and recovery do not assert full faithfulness, and the fpqc affine-stack construction is not thereby identified with a “topos de De Rham.”',
'C2',H+'; WG2 §Week #3',r'fpqc|schematization|topos|integral','high for the theorem and its restrictions; the historical site identification is unsupported')

add('L10','123–135, binomial refinement','own idea — literature comparison',r'structures multiplicatives',
r'Horel (2024, Theorems 5.4 and 6.1) obtains a fully faithful model for connected nilpotent finite-type spaces using cosimplicial binomial rings localized at quasi-isomorphisms; for connected finite-type spaces more generally the derived unit is integral Bousfield–Kan completion. The binomial condition and its derived category are not interchangeable with a PD ideal, so this result supplies a modern comparison target without completing the manuscript’s uniqueness argument.',
'C6',H+'; '+W,r'binomial|nilpotent|schematization|divided powers','high for the exact modern statement; any map from the manuscript’s model still needs construction')

add('L11','111–135, qualification of strict-commutativity claims','own idea — literature comparison',r'structures multiplicatives',
r'Richter and Sagave (2020, Theorems 1.1–1.2) construct a strictly commutative model in diagrams of chain complexes indexed by finite sets and injections, with Day-convolution multiplication, whose homotopy colimit recovers singular cochains as an $E_\infty$ algebra. The diagram structure carries extra information, so O01 must remain an obstruction under its explicit ordinary-PD hypotheses, not a blanket prohibition on all strictly commutative presentations of integral cochains.',
'C7',W,r'commutative|operations|cochains|homotopy colimit','high for the structural distinction; no comparison of diagram categories is asserted')

add('L12','096–106; 111–135, comparison with the later withdrawal','own idea — contextual distinction',r'faux tel quel, à arranger',
r'The manuscript’s local withdrawal of the flasque-flat argument and PS §119’s rejection of a derived-$\Gamma$ computation are different claims. In PS the rejected expectation concerns Eilenberg–Mac Lane homology and schematic/discrete comparison, while the same section subsequently still distinguishes PD de Rham linearization from a possible binomial approach. Their coexistence prevents treating either correction as a blanket repudiation of every integral de Rham model.',
'C5',W+'; '+H,r'definitely false|divided powers|De.Rham|Illusie','high for the distinction of the explicitly named propositions; neither source supplies the missing lecture comparison proof')

add('L13','129; 135; 137, comparison with PS base-ring criticism','own idea — contextual distinction',r'$C_*^{DRpd}(X)\otimes_{\mathbf Z}k$',
r'The manuscript’s scalar-extension formula applies to a constructed integral chain object, whereas PS §124 criticizes a procedure that first forgets the module structure of an arbitrary chain complex before applying the de Rham construction to its underlying semisimplicial set. Thus the later criticism neither contradicts the displayed tensor formula nor establishes derived base change for it; comparing the two requires preserving the input category and the forgotten structure.',
'C9',W+'; '+H,r'module structure|ground.ring|De.Rham|forget','high for the difference between the two stated constructions; a stronger equivalence is not claimed')

add('N67','113','withdrawn in the same text / reformulation',r'On veut de plus que ... l\'augmentation',
r'The direct augmentation requirement is cancelled and replaced by a sheaf-theoretic diagram involving derived sections. This is a reformulation in progress, so one should not silently combine the deleted requirement with the later comparison conditions as if both belonged to a finalized axiom system.',
'C10',W,r'augmentation|sections|sheaf|cohomology')

add('N68','111','withdrawn in the same text / weakening',r'\deleted{doivent}\inserted{peuvent}',
r'The modal correction weakens “must” to “can” in the passage from representable functors to structured semisimplicial objects. It does not settle the unspecified limit directions, and its significance should remain local to that interpretation rather than be read as an existence theorem for every desired theory.',
'C2',W,r'representab|functor|semi.simplicial|topos')

add('R34','132, reused typescript, proof of §9.5.6','reading question',r'se prolonge en un groupe de Barsotti-Tate $X_\eta$ sur $S$',
r'The extension over $S$ retains the subscript $\eta$ in this sentence, while the following displayed extension morphism uses $X$. A subscript-free $X$ is the natural candidate in the argument, but the literal notation is retained and the question is recorded only here.',
'C0','No directly relevant RESULTS_STATE item',r'Barsotti|generic|extension|9\.5\.6')

add('L14','111–121; 135, functorial commutative-cochain benchmark','own idea — literature comparison',r'On s\'intéresse aux foncteurs',
r'Cenkl (1989, §5, Theorem 2) studies a natural cochain theory with unit-compatible commutative multiplication, acyclicity on models, and a comparison inducing cohomology isomorphisms in every degree for every simplicial set; his theorem forces each $a^2$ in the coefficient ring to be divisible by two and excludes $\mathbf Z$. These specific hypotheses give a distinct functorial obstruction independent of a PD structure, alongside O01, but they must be matched before being applied to a weighted or extracted theory.',
'C7',W,r'commutative|cochains|unit|De.Rham','high for the theorem’s specified framework; no claim that every weighted manuscript object satisfies its hypotheses')

add('L15','109; 111–121, rational comparison','own idea — literature comparison',r'tensored by $Q$ or $R$',
r'Sullivan (1977, §§7–8 and 10) provides the rational polynomial-forms and minimal-model comparison, with nilpotence and finite-type hypotheses in the homotopy classification. It is a useful mechanism to compare with the donor sheet’s tower language, but cannot establish an integral theorem or supply the unverified provenance of N27.',
'C4',H,r'rational|polynomial|nilpotent|cochains','high for the coefficient and hypothesis distinction; the donor’s authorship remains unverified')

add('R35','124; 126, reused typescript, bibliography/version question','reading question',r'NERON [19]; TATE [33]',
r'The publisher’s bibliography for the 1972 chapter lists Néron’s models paper as item 20 and Tate’s p-divisible-groups paper as item 36, while these sheets use 19 and 33 (Grothendieck & Raynaud, 1972, publisher chapter record). This supports distinguishing the identifiable SGA text family from a fully collated published version; draft-stage bibliography or other version differences require checking against the complete original chapter. No citation number or wording in the frozen donor transcription has been updated.',
'C0','No directly relevant RESULTS_STATE item',r'Néron|Tate|Raynaud|monodrom')

add('N69','109, reused English sheet','unproved claim / construction by absent reference',r'a purely algebraic computational construction',
r'The donor describes building the minimal model by adjoining generators to obtain successive cohomology isomorphisms and injections, referring to a construction in the missing preceding text. Its potentially infinite stages require their own convergence and minimality arguments; the brief algorithm here does not prove the tower interpretation or identify an integral PD analogue.',
'C4',H,r'minimal|polynomial|rational|cochains')
