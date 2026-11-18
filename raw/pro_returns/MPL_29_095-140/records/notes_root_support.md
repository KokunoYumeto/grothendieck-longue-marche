# Root research support, after transcription freeze

This file records research work only. The 31 page files and the combined transcription were frozen at 2026-11-18 06:04:22 UTC; none of the context-based comparisons below changes them. Root has read the context READMEs and RESULTS_STATE and has delegated only text-based context research, never image transcription or visual auditing.

## R1. The two-branch drawing does not specify its punctures

Witness: cote 29, scan107, the circled `Z=Spec` completed local ring and the diagram with `Pi_1(Z)=hat Z^2`; the source ends by requiring a `th. de descente` and `hom. canoniques`. Kind: reading question / unproved claim. Context searches: `deux branches`, `complétions`, `descente`, `Z`, `hat`; compare Hua, modernised reading of cote 29, “Le π₁ local le long de deux branches” (Hua p.106 = scan107), “Deux complétions d’un croisement normal” (Hua pp.41–42 = scans042–043), and “La traduction simpliciale” / “Le van Kampen” (Hua pp.180–185 = scans181–186, outside supplied images).

The displayed completed local ring and the fundamental group need separate interpretation: for the model A=C[[x,y]], Spec A is strictly henselian and has no nontrivial connected finite étale cover, whereas removing the two coordinate divisors is a different space. The familiar two-generator tame inertia calculation belongs to the latter kind of punctured neighborhood, so it must not be silently assigned to the unpunctured Spec in the drawing. Hua repeats the diagram and adds descent connections but does not resolve that notational ambiguity. No current RESULTS_STATE entry settles these specific canonical maps.

Check performed: a complete local ring with algebraically closed residue field is strictly henselian; for a finite étale A-algebra B, idempotents lift from B/(x,y)B, which is a finite product of C, and each resulting local finite étale factor has rank one and hence equals A. Thus every connected finite étale cover of Spec A is trivial. This is a targeted check of the unpunctured model only; it is not a proof of the intended formal patching theorem or of every group in the sketch.

## R2. Root gerbe and divisor root stack have different stabilizers

Witness: scan101, the Kummer algebra `T_i^{n_i}-a_i` and the Chern-class proof target; scan103, normal-bundle class. Kind: own idea, high confidence in the distinction by an explicit local quotient; the proposed application to the archival construction is a comparison, not an established identification.

Context searches: `gerbe`, `racines`, `Chern`, `diviseurs`, `section`; compare Hua, modernised reading of cote 29, “Le programme kummérien : la classe, une deuxième fois” (Hua p.100 = scan101) and “Exemple 2 : des diviseurs, et la gerbe” / “Ce que ces exemples sont, aujourd’hui” (Hua pp.199–200 = scans200–201, outside supplied images). Relation: context adds the modern root-stack interpretation; distinguish the gerbe of roots of the line bundle from the stack of roots of the line bundle together with its defining section. Relevant register: Hua, findings register, 29-formal-tame-pi1-self-intersection.

Explicit check: let n>1 be invertible in k, X=Spec k[x], and D=(x). The divisor root stack is the quotient [Spec k[z]/mu_n], with x=z^n and scalar action on z; for z nonzero its stabilizer is trivial, while at z=0 its stabilizer is mu_n. The line bundle O_X(D) is trivial, and its nth-root gerbe is Bmu_n over all of X, with stabilizer mu_n everywhere. Consequently these two stacks are not isomorphic over X, although the line-bundle gerbe supplies the Kummer obstruction used in comparing their constructions. No priority claim is made.

External verification consulted: Stacks Project, Tag 04V8, “Taking roots of line bundles”, https://stacks.math.columbia.edu/tag/04V8 (accessed 2026-11-18), for the divisor root stack's stabilizer description. The actual comparison above is a direct local calculation, not an inference from a historical attribution.

## R3. Kummer coefficients require a specified topology

Witness: scan101, arbitrary integers `n_i>=1` and the cohomology class in H^2(X,mu_n); scan098, primes invertible on arithmetic bases. Kind: unpursued implication. Context searches: `Kummer`, `inversible`, `caractéristiques`, `boitent`; compare Hua, modernised reading of cote29, “Le programme kummérien” (p.100 = scan101), “Le cas kummérien” (pp.19–20 = scans020–021), and “Le boitement, avoué” (p.200 = scan201, outside supplied images).

For arbitrary positive n, the Kummer exact sequence is valid on the fppf site; on the étale site the standard Kummer statement applies when n is invertible on the base. The source's general Kummer programme and its tame specializations should therefore retain distinct coefficient and topology hypotheses. This adds an explicit formulation issue to Hua's later discussion of residue-characteristic restrictions; it does not prove the archival Chern comparison.

Proof rechecked from Stacks Project, Tag 03PK, Lemmas 59.28.1 and 59.28.3, https://stacks.math.columbia.edu/tag/03PK (accessed 2026-11-18): for a unit a in A, A[T]/(T^n-a) is finite free of positive rank, hence faithfully flat; if n is invertible, T and the derivative nT^{n-1} are units, giving an étale cover. This is a used-and-rechecked background fact, with no claim to a new result.

## R4. Finite coefficient pro-representability is not a finite homotopy model

Witness: scan105, `exact à g., donc proreprésentable`. Kind: own idea, high confidence about the logical distinction because the test categories and representability demands differ; no new theorem follows.

Context searches: `pro-représent`, `pi_{2}`, `finite categories`, `S2COUNT`, `C2-CP2`; compare Hua, modernised reading of cote29, “pi_2” (p.104 = scan105), “Quand un foncteur est pro-représentable” (pp.181–185 = scans182–186), and RESULTS_STATE entries FINMON C2-CP2 and S2COUNT. The source proposes representing H^2 on finite abelian coefficient groups by a pro-group; those register entries concern finite categories or monoids realizing homotopy types or testing maps to S^2. This is a methodological comparison only: it neither settles FINMON C2-CP2 nor contradicts S2COUNT, whose underlying proof and certificate are not supplied here.

## R5. Date and literature comparison has a clear evidence boundary

Witness: scans126,129,130, letter fragments with author pages2,5,6 and final `Bien à toi`; scan124 title sheet. Kind: reading question about provenance / unpursued comparison. Context searches: `Serre`, `18 août 1959`, `Nori`, `1976`, `1983`, `multiplodoque`.

Hua, modernised reading of cote29, “Lettre à Serre, 18 août 1959” (Hua pp.124–129 = scans125–130) supplies the correspondent and date; the date-bearing opening scan125 is excluded from this image package. The supplied fragments directly witness the infinitesimal-group discussion, abelian-variety computation and programme, but not the date or addressee on their own. Publication metadata independently verifies Nori's articles in 1976, 1982 and 1983; this establishes a bibliographic comparison, not a claim of influence, priority, or equivalence under identical hypotheses. Relevant register: Hua, findings register, 29-fundamental-group-scheme-via-torsors; its literature-status label remains that project's claim.

Primary bibliographic pages consulted 2026-11-18:

- Madhav V. Nori, “On the representations of the fundamental group”, Compositio Mathematica 33 (1976),29–41: https://www.numdam.org/item/CM_1976__33_1_29_0/ .
- Madhav V. Nori, “The fundamental group-scheme”, Proceedings of the Indian Academy of Sciences (Mathematical Sciences)91 (1982),73–122: https://doi.org/10.1007/BF02967978 ; publisher https://link.springer.com/article/10.1007/BF02967978 .
- Madhav V. Nori, “The fundamental group-scheme of an abelian variety”, Mathematische Annalen263 (1983),263–266: https://doi.org/10.1007/BF01457128 ; publisher https://link.springer.com/article/10.1007/BF01457128 .

Only the bibliographic metadata is used here; the complete 1982 and1983 proofs were not inspected. No mathematical CHECK_EVENTS row is created merely for verifying publication metadata.

## R6. Literature supports keeping field groups separate from arbitrary base groups

Witness: scans126 and137–140, the restricted exact-functor setup versus arbitrary admissible S-groups and their morphisms. Kind: unpursued implication / literature comparison. Context searches: `exact`, `foncteur`, `admissibles`, `noyaux`, `minimal`; compare Hua, modernised reading of cote29, “Le dispositif” (pp.124–126 = scans125–127) and “La proposition4, démontrée deux fois” (pp.138–140 = scans139–141).

Marco Antei, “On the bumpy fundamental group scheme”, arXiv:1511.07331v1, §2.2 and §3, explicitly distinguishes the category of finite k-group torsors from the relative-base setting and points out that the fibre product of finite flat groups over a base can fail to be flat. This is consistent with the flatness obstruction exposed in the present cusp example; it does not by itself prove that example, complete the later archival proof, or settle LM1 E.11. The paper was inspected as a historical mathematical source, not as evidence of the current state of every relative fundamental-group question.

Source: https://arxiv.org/pdf/1511.07331 , §2.2 (printed pp.4–5), §3 (printed pp.5–6), accessed2026-11-18. This source is not copied into the deliverable. Its detailed theorems are not carried as proved results in this run; the comparison uses only its stated distinction and warning, while the algebraic example is proved separately.

## Root review of ancillary checks

The following mathematical arguments have been examined directly by root, rather than accepted just because an agent reported them:

- Inertia C1: the F4((u))/F2((t)) automorphisms satisfy sigma r sigma^{-1}=r^2; separable Eisenstein cubic plus degree-two constants yields the tame S3 quotient, so unrestricted arithmetic centrality fails.
- Inertia C2: changing Heisenberg lifts by the central kernel leaves their nontrivial commutator unchanged; this is only a diagnostic against the inference from pi_2=0, not a geometric refutation.
- Inertia C3: the prime-to-p Tate cokernel is finite for nonzero degree, while the zero endomorphism has the whole Tate group as cokernel; the check is conditional on the archival homotopy exact sequence.
- Inertia C4: both order-four subgroups of Q8 are normal but do not commute; no geometric realization claim is made.
- Inertia C5: a finite spectrum preserved by q-th power is permuted, every nonzero eigenvalue is torsion, and Cayley–Hamilton gives a common unipotent power in every characteristic.
- Inertia C6: the two short exact coefficient sequences through the image of a map, with H^1 vanishing for each finite constant coefficient, give preservation of kernels in H^2; products are additive. No right exactness or comparison theorem is included.
- Torsor U-uniqueness: the preimage of the identity of a finite étale quotient is clopen and contains all geometric points of a geometrically injective group with a unit section; thus either proposed infinitesimal kernel lies in the other, without reducedness of the base.
- Torsor cusp: A=k[t^p,t^{p+1}], x=t^p, y=t^{p+1}; the pointed alpha_p torsor z^p=x has no A-section, finite flat proper subgroup ranks are forced to1, and [x] pushes it to w^p=y^p, pointed-trivial. Its equalizer normalization A[z]/(z^p-x,xz-y)=k[z] has generic rank1 and special fibre lengthp, so is not flat.

These are scoped, written proof checks, not machine certificates, literature novelty determinations, or alterations of transcription readings.

## R7. Removing reducedness breaks pointed rigidity

Witness: scan126, provisional condition (vi) and rigidity lemma; scan138, Proposition3, `S réduit connexe`. Kind: own idea, high confidence in this elementary counterexample; it tests the dropped hypothesis, not the source's qualified statement. Context searches: `réduit`, `provisoires`, `sections`, `identiques`, `admissibles`; compare Hua, modernised reading of cote29, “Le dispositif” (Hua pp.124–126, selected witness scan126) and “Les groupes admissibles” (Hua pp.136–137 = scans137–138). Relevant register: Hua, findings register,29-fundamental-group-scheme-via-torsors.

Take S=Spec k[epsilon]/(epsilon^2) in characteristic p>0, G=alpha_p,S, and the trivial torsor P=G. The sections T=0 and T=epsilon are distinct because epsilon is nonzero, and both satisfy T^p=0 because p>=2; their values agree at the unique geometric point of S. Translation by epsilon is therefore a nonidentity G-equivariant automorphism fixing the geometric marking. Thus reducedness cannot be dropped from this rigidity assertion merely because it is unnecessary for uniqueness of the infinitesimal kernel; this refines the scope of the provisional-hypotheses discussion without claiming that reducedness is needed for every possible fundamental-group construction.

This is a targeted counterexample checked directly in the coordinate ring. It is not a counterexample to Proposition3 as qualified in the source.
