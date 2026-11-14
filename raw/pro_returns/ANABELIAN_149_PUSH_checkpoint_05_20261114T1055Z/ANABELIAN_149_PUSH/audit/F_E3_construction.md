# Completion of E3 by a Hausdorff algebraic presentation

Status: independently reviewed and accepted by the root agent, 14 November 2026; the proof is in sections/E_extension.tex, E.8--E.9, with two Proved rows in audit/E_extension_results.json. This note does not modify E.tex. Its definition expressly imposes a Hausdorff presentation; it does not identify the naive abstract quotient of profinite path sets with its Hausdorff quotient.

## Proved result

The category C_diag of E.5 is the Betti realization of the following algebraic generators and relations. Replace every Betti fundamental groupoid by its étale fundamental groupoid and take the universal Hausdorff topological category with profinite automorphism groups satisfying the same algebraic relations. This algebraic category exists and is canonically equivalent, up to the usual marking choices, to the profinite envelope of E.6. In particular its Hom spaces are precisely the finite coproducts of closed-coset spaces in E.6. This settles E3 for the isotopy relation already specified in E.5 and the explicitly Hausdorff algebraic presentation.

The key point is a universal-property proof with a separation argument for the stabilizers. No assertion that completion commutes with arbitrary ordinary quotients is needed.

## 1. Algebraic presentation data

Objects are smooth connected hyperbolic complex algebraic curves. For each type use the moduli stack of curves with unordered punctures; labelled or coloured punctures are obtained by the corresponding finite covers and symmetric-group quotients. The generators are:

1. paths in the fundamental groupoid of each moduli stack;
2. actual finite étale maps of curves;
3. actual puncture fillings, namely the inclusions obtained by deleting a smaller subset of a smooth proper compactification.

Identify an actual isomorphism with its canonical path in the stack groupoid. Impose the path groupoid laws. For every finite chain of specified covers and fillings, form its algebraic diagram stack D. For a path gamma in D from a chain w_0 to a chain w_1, with source path alpha and target path beta, impose the naturality relation

    beta * w_0 = w_1 * alpha.

Finally identify two chains of actual algebraic maps whose composite maps are equal. Impose these relations inside arbitrary longer words, so the relation is a congruence.

These diagram stacks are algebraic of finite type. A filling is described by a configuration of extra disjoint marked points on the target, together with the retained/forgotten colouring. For a cover, use the finite collection of smooth Hurwitz stacks of the given degree and boundary ramification partitions; non-Galois maps are included by Bertin–Romagny Theorem 6.20. Their finite fibre products over the intermediate moduli stacks give the chain stacks. Hyperbolicity makes their automorphism groups finite, so these are Deligne–Mumford stacks. The local cover deformation is the deformation of the marked target, as stated explicitly in the opened proof of Bertin–Romagny 6.20. No representability of a Hurwitz discriminant morphism is asserted: deck automorphisms are retained in the stacks.

There are two versions of this presentation: use ordinary topological paths in the analytic stacks for the Betti version B, and continuous étale path groupoids for the étale version.

The **Hausdorff étale presentation** means the universal category representing these data in Hausdorff topological categories whose automorphism groups are profinite. Its universal property requires continuity on each étale path groupoid and of composition. The existence proof below exhibits a representative, so this is a definition by algebraic generators, relations, and a precisely stated universal property, not an unsupported existence assumption. Equivalently the relations are required in their closed congruence, not merely in their abstract set-theoretic congruence.

## 2. The Betti presentation is C_diag

The topological fundamental groupoid of the moduli stack is the groupoid of oriented surface markings up to isotopy. This follows from the contractibility of Teichmüller space and its stack quotient by the mapping class group; the precise marked and unordered formulations are in Schneps (2003), section 2.1. Underlying-surface monodromy therefore sends the Betti path generators to the isomorphism arrows of C_diag.

A path in an analytic chain stack can be locally trivialized topologically along the interval. It gives a family of the specified fixed diagram of covers and fillings. Its endpoint transports satisfy precisely the diagram-isotopy relation of E.5. Equality of algebraic composite maps is equality of their underlying maps. Thus there is a functor B -> C_diag.

Here is an inverse construction, including why the diagram relation is the intended one. Choose a complex structure on each object surface. For a topological word ending in a surface T, keep the chosen complex structure on T and propagate it backwards through the word. A covering pulls back a complex structure uniquely; a puncture filling restricts the complex structure across the omitted points. Every arrow then becomes holomorphic on the open curves and extends holomorphically to their compactifications, hence is algebraic. The source may now have a different complex structure on the same marked surface. Connect it to the chosen one through marked complex structures. Contractibility of Teichmüller space says that the resulting moduli path with its prescribed identity marking is unique up to the relevant homotopy.

This construction respects each relation. Along a topological diagram isotopy, work backwards from the fixed target complex structure. A filling gives a continuous path of extra-point configurations in the target family. A cover gives the finite-cover transport over that path. Iterating gives a continuous path in the analytic diagram stack. One can see this locally over the interval using analytic target charts: the covering charts are pulled back, and finite marked configurations are sections of the analytic universal curve. Thus no differentiability assumption on the original isotopy is required. The source marking remains the given identity marking, so the naturality square makes the constructed Betti arrows equal.

If two topological words have the same actual composite, pulling the target complex structure back gives the same source complex structure. Both factorizations are simultaneously holomorphic, and their composites are equal algebraic maps. The stipulated equal-composite relation identifies them. Compatibility with composition follows by transporting the first diagram along the marked complex-structure path used for the second diagram; the same naturality square supplies the needed equality. These statements also show that the inverse construction is independent of its marked paths and that the two functors are inverse up to the canonical marking isomorphisms.

Consequently B is equivalent to C_diag. This proof does not replace diagram isotopy by two-sided homeomorphism orbits; the example E.7 remains identified by a diagram path.

## 3. Profinite paths preserve the entire presentation by density

Let D_target be any Hausdorff topological category with profinite automorphism groups. Consider a functor F from C_diag to D_target. Via section 2 it supplies a realization of the Betti presentation. On each moduli-stack fundamental group, F is a homomorphism into a profinite automorphism group, and therefore extends uniquely to the full profinite completion. Choosing one ordinary path to each endpoint extends the same statement from groups to path groupoids; changing such choices changes the expression by an ordinary loop and gives the same extension.

Noohi's Theorem 20.4 and its following corollary identify that completion with the étale fundamental group. These hypotheses hold for the finite-type complex Deligne–Mumford stacks here: their analytic stacks are locally path connected and semilocally 1-connected. Every ordinary path torsor is dense in its étale path torsor, component by component.

Now take any one of the algebraic diagram stacks D and an étale path gamma in it. In the naturality relation, both sides are continuous functions of gamma into the Hausdorff Hom space of D_target: the endpoint maps on fundamental groupoids and composition are continuous. They agree on the dense subset of ordinary paths because F realizes the Betti presentation. Their equalizer is closed, so they agree for every étale path. This works for every diagram stack and after every insertion into longer words. The equal-actual-composite relations are unchanged.

Thus every functor C_diag -> D_target extends uniquely to a realization of the full étale presentation. Conversely, restricting any continuous étale realization to ordinary paths and using section 2 gives such a functor. These constructions are inverse, also on compatible natural transformations.

## 4. Existence, comparison, and the exact closed stabilizers

By E.6, the Hausdorff profinite envelope C_hat_diag represents the functor

    D_target -> Fun(C_diag, D_target).

By section 3 this is exactly the functor of realizations of the algebraic étale presentation. Therefore C_hat_diag is a representative of that presentation. This proves existence of the purely algebraically specified universal category and its comparison with E.6.

For clarity, the stabilizer closure is not hidden in this universal-property argument. Let S_u be the discrete right stabilizer of an arrow u of C_diag. Every Hausdorff realization kills its closure in Mhat_S, because its orbit map is continuous. Conversely, if a is outside closure(S_u), C_hat_diag itself is one realization of the algebraic étale presentation, and the distinct cosets closure(S_u) and closure(S_u)a separate u and ua in that realization. Consequently no universal closed relation can identify them. Thus the exact stabilizer in the algebraic presentation is closure(S_u), with neither a separability assumption on S_u nor an interchange of completion and an arbitrary ordinary quotient.

The Hom formula, compactness, continuous composition, and automorphism groups are now those of E.6. For the pure-cover subcategory, defect zero excludes every genuine filling at every intermediate relation, so the discrete stabilizers coincide with the covering-only ones; their closures coincide as well. Its completed category embeds with the required Hom spaces. The labelled puncture-forgetting operations are the forgetful maps already included in the algebraic presentation, and their composite relations are literal equality of algebraic maps.

The deliberate Hausdorff clause is essential. This argument does not assert that the unseparated abstract category obtained by quotienting finite words in profinite paths already has Hausdorff Hom spaces.

## 5. Concrete degree-two cover followed by one filling

As a direct check, fix the three labelled target punctures 0,1,infinity. For b in Y=P1 minus {0,1,infinity}, let

    f_b(z)=z^2+b,
    X_b=P1 minus {0,infinity, roots(-b), roots(1-b)}.

The map factors as a degree-two finite étale cover

    X_b -> Y minus {b}

followed by the filling Y minus {b} -> Y. The source has six punctures. The diagram component with branch values b and infinity, fixed labelled target, is Y times B(mu_2): the displayed family exists globally and every such double cover is uniquely isomorphic to it up to its deck involution. Its source map gives the braid monodromy

    phi : pi1(Y) times C2 -> M_(0,[6]).

Its profinite étale image is exactly the closure of phi's ordinary image: Noohi identifies pi1_et(Y times B(mu_2)) with the profinite completion of that product, and a continuous image of a compact group in Mhat_(0,[6]) is closed. No injectivity or subgroup-separability assertion is required.

For this ramification component, the stabilizer is this diagram image. Indeed the degree is two and the defect is two. The single omitted ramification point over the interior critical value b already contributes the full defect, so there are no further omitted interior points. Any factorization through finite covers and fillings must therefore remove exactly b on the target before taking the cover; fillings before the degree-two cover would insert the ramification point and prevent that factor from being étale. Apart from homeomorphisms and trivial factors, the cover-then-fill diagram is forced. This identifies the extra-point braid contribution and its closure directly. It illustrates, rather than replaces, the full presentation argument above.

## Sources actually opened for this note

- Bertin–Romagny, supplied `background/literature/bertin_romagny/src_arXiv_math_0701680/Hurwitznew.tex`: Theorem 2.9 and its preceding Teichmüller discussion; Proposition 6.14 including the explicit nonrepresentability footnote; Theorem 6.20 and its proof, especially the equivalence of deformations with those of the marked target. Sections 6.9,6.14,6.20 were also already opened by root.
- Noohi, supplied `background/literature/noohi/src_arXiv_math_0503247/foundations.tex`: exact statement and proof of Theorem 20.4 (`T:StackyRiemann`), and the following corollary (`C:profinitecompletion`). The theorem concerns representable finite étale covers of the stack; it does not require the diagram stack's own map to a curve-moduli stack to be representable.
- Schneps, L. (2003), *Special loci in moduli spaces of curves*, in *Galois Groups and Fundamental Groups*, MSRI Publications 41, section 2.1. Primary publisher-hosted PDF https://library.slmath.org/books/Book41/files/schneps.pdf. Its text extraction is corrupted, so screenshots of section 2.1 were actually opened: Teichmüller contractibility, full/pure mapping class groups, and the quotient description. Web refs turn90view0 and turn88view0 show the relevant pages. These supply the marked moduli-path dictionary, not a theorem about the new diagram category.
- Bresciani 2021 appendix was checked but is **not** a source for Teichmüller contractibility: its relevant final propositions concern invariance of étale fundamental gerbes under base extension. No such misattribution is made here.
