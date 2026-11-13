# E.58: relative lifting and a full extra-CM gentle element

## Outcome and exact construction

The source proof is `sections/E_relative_cm_lift_agent.tex`. It proves
the relative extension of D.50 for any specified open normal subgroup
(U) of the free pants or modular source. In every finite collection,
retain (Gamma/U) and use (A=\gamma_\infty(\operatorname{im}U)).
Its actual central detector has nilpotent (U)-image and therefore
factors through (Gamma/R_{\rm nil}(U)). The same complete conjugator
compactness proof gives a full peripheral automorphism. No invariance
of an arbitrary finite source kernel is presumed.

The local comparison is the actual fibre product

\[
 \Gamma/R_{\rm nil}(U)
  \simeq\prod_{p,\Gamma/U}\Gamma/O^p(U).
\]

The CM application uses (H=F'F^3), where (F\triangleleft\mathcal B)
is the actual free pure subgroup. It is characteristic, and
(D=\mathcal B/H) has order 54. Under the fixed E.1 map
(q:\mathcal B\to Q=\operatorname{SL}_2(\mathbf Z/12)/\{\pm I\}),
the unique mod-four Klein-four representative gives the exact maps

\[
 q(F)\simeq C_2^2\times\operatorname{SL}_2(\mathbf F_3),\qquad
 q(H)\simeq C_2^2\times Q_8.
\]

The actual joint source is
(J=Q\times_{Q/q(H)}D), of order 1728. Its specific element
(([5I],1)) has the literal (H)-word preimage ([x,y]^2).
The map (Gamma_2=\mathcal B/O^2(H)\to J) has pro-two kernel.
Coprime complement conjugacy for the actual element (r) of order
three gives (c\in C_{\Gamma_2}(r)\cap H^{(2)}) over (([5I],1)).

Put (c) in the two-component of the relative fibre product and
identity in every other component. This is an actual (r)-centralizer
element with common (D)-value one. Use the identity automorphism in
every component, this prescribed (r)-frame, and identity (s)- and
(\tau)-frames. The relative theorem supplies a full automorphism,
normalized to fix (\tau), with

\[
 f\in R_{\rm nil}(H)\subset F',\qquad
 q(A)=[5I],\quad q(\beta)=q(V)=1.
\]

The full factor-centralizer theorem makes (A,\beta\in F) unique.
Thus the nontrivial relative frame is retained by the constructed full
automorphism; it is not asserted to lift to a full centralizer. In
E.1's positive convention, (A^{-1}) acts by (-1) on the fixed
three-torsion line, and (eta^{-1}=I). The bits are exactly ((1,0)).
This proves the positive answer to Task E.2.

The entire (G_6) quotient does not factor through (Gamma_2):
(x^6=\tau^{-12}\in H\cap N_B) has primitive (N_B)-abelianization
and order six in (G_6). The full constructed automorphism nevertheless
preserves (N_B), since (q\Phi=q), and hence its characteristic
(N_B'N_B^6). Its actual (G_6) projection supplies a new genuine
point in the whole CM matrix fibre. No rejected old representative is
reused.

## Independent finite certificate and replay

Run `python code/bc_relative_cm_sources.py`; no package or project-code
dependency is required. The authoritative run took 0.166 seconds and
saved adjacent `.json` and `.out` files. It checks:

- all 576 projective matrices, the literal generators, and both subgroup
  images of orders 96 and 32;
- all 9,216 products in the exact (q(F)) CRT splitting;
- the affine (D) model and its 54-element image, where (x,y) are the
  standard translations;
- the complete 1,728-element joint image and its precise 18-element
  common quotient;
- the literal commutator square ([x,y]^2\mapsto[5I]), its centrality,
  and the exact positive CM bits;
- the 24-edge integral cycle of (\tau^{12}), zero boundary, and unit
  coefficient proving primitive (N_B)-abelianization.

The finite program verifies the inputs and maps. The infinite
centralizer and peripheral lifts are proved in the source.

## Preserved attempts and review

The first sign assertion mistakenly used the lexicographic projective
representative of (r), which is the negative of E.1's specified
positive matrix. It failed before producing a positive certificate.
The initial program and failure explanation are retained in
`research/E58_source_sign_preserved/`. The corrected calculation uses
the original positive (R) for its fixed three-torsion line; the
projective source is unchanged.

The first written TeX source is retained in
`research/E58_draft_preserved/initial_written_source.tex`. The next
revision only split displays and made the exact (G_6) descent explicit.
Standalone LuaLaTeX QA passes twice with the project format, producing
six pages with no overfull/underfull boxes or warnings. The two earlier
environment failures (missing default format and missing default TEXMF
lookup) are preserved under `research/E58_build_check/`; they preceded
reading the mathematical fragment.

Arithmetic's complete independent proof/program read passed, including
the normal-(U) variant and all frames. The parent independently
derived and checked the centralizer construction before integration.

## Exact primary input

Herfort and Ribes, *Torsion elements and centralizers in free products
of profinite groups*, J. reine angew. Math. 358 (1985), 155--161,
DOI `10.1515/crll.1985.358.155`. Theorem B in the introduction and
Theorem B′ in Section 4, printed page 159, give the factor-centralizer
equality. The full text and its proof were independently reopened at

<https://www.academia.edu/104225124/Torsion_elements_and_centralizers_in_free_products_of_profinite_groups>.

The exact theorem applies to the actual factors (C_2,C_3) in
(\mathcal B=C_2\amalg C_3), yielding
(C_{\mathcal B}(r)=\langle r\rangle) and
(C_{\mathcal B}(s)=\langle s\rangle). Their intersections with (F)
are trivial because the given (S_3) quotient embeds both factors.
The separate BibTeX entry is `research/E58_references.bib`.
