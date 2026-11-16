# A.178: exact sources and scope audit

Source: sections/metabelian_finite_support.tex.

This draft proves finite-support rigidity for locally point/cusp-matching
sections of the actual quotient \(E_X/H_3'\), and then of \(E_X/\Pi''\),
for every smooth geometrically connected hyperbolic curve over a number
field. It also proves that the first quotient separates actual full
point and cusp reference classes. All these domains are stated in the
source; the theorem does not assert that every metabelian section is
locally geometric or has finite support.

## Primary source checks made on 16 November 2026

### Harari–Stix, Theorem 2.1

- Primary PDF: <https://arxiv.org/pdf/1005.1302>
- Version opened: arXiv:1005.1302v2, 26 May 2010.
- Exact passages: PDF printed pp. 11–12, Theorem 2.1, implication
  (iii) to (i); the following unnumbered **Remarks (3)**.
- Short literal excerpt, from (iii): “the sections \(s_v\) come from a
  global section \(s\).”
- Actual use: the proper geometric commutator quotient section supplies
  a global pullback class for every finite commutative torsor.
  Evaluation at each selected proper local point is the restriction of
  that class. The source proves the stronger statement for all finite
  torsors whose geometric monodromy is abelian.
- No rational point or degree-one divisor is assumed in this passage.
- The exact map in A.178 is the descended fundamental-group cocycle,
  followed by pullback along the section, not an identification of an
  unsplit arithmetic extension with a Tate-module semidirect product.
- Existing bibliography key: AgentHarariStix.

The 14-page author version dated **11 February 2011** was also opened:
<https://www.imo.universite-paris-saclay.fr/~david.harari/articles/finidesc.pdf>.
Its exact corresponding pointer is **Remarks 2.2(3), printed p. 8**;
Theorem 2.1 has the same number, and Corollary 3.1 on printed p. 9
repeats the proper geometrically abelian consequence. The main source
now states both version-specific pointers, matching the bibliography's
published 2012 reference and later author URL.

The attached 2010 primary TeX also records this statement:
background/literature/harari_stix/src_arXiv_1005.1302/main.tex,
section “Results over number fields”. Its relevant pointer is the
unnumbered Remarks (3); the 2011 author version numbers it 2.2(3).

### Stoll, Theorem 8.2

- Author PDF: <https://www.mathe2.uni-bayreuth.de/stoll/papers/covers-revised.pdf>
- Version opened: 28 September 2007, printed p. 36.
- Short literal excerpt: “for a set of places \(v\) of \(k\) of density 1”.
- Actual use: a proper positive-genus curve, a finite subscheme, and a
  modified adelic point surviving finite abelian descent. The finite
  support on the stated density-one set forces a rational point.
- This supplies the rational origin **after** descent has been proved.
  It does not require a rank or Tate–Shafarevich hypothesis.
- The same PDF, printed p. 10, Proposition 3.7, is used only on the
  compatible inverse Selmer class once that origin is available.
- Existing bibliography key: LegStoll2007.

The attached primary TeX has Theorem BM0:
background/literature/stoll_finite_descent/src_arXiv_math_0606465/main.tex.
The PDF numbering, rather than an assumed source-label numbering, is
used in A.178.

### Stoll's errata

- Primary PDF:
  <https://www.mathe2.uni-bayreuth.de/stoll/papers/Errata-FiniteDescent-ANT.pdf>
- Version opened: 29 March 2017, complete three pages.
- Exact passages: §1 on omitting complex factors; §3 on the real-place
  issue in the proof of Proposition 8.5.
- Short literal excerpt: “we only need that \(P_v\in Z(k_v)\) for a set
  of places of density 1”.
- A.178 records equality of actual points only at finite places.
  At real places it uses the corrected modified-adelic component
  convention. No injectivity on all real points is inferred.
- Existing bibliography key: LegStollErrata2017.

## Exact maps and the potential gaps checked

1. \(H_n\) is the kernel of the actual finite geometric abelianization.
   It is characteristic in \(\Pi\), so \(H_n'\) is normal in the
   arithmetic fundamental group. The inclusion \(\Pi'\subset H_n\)
   gives \(\Pi''\subset H_n'\), with all commutators closed.
2. The arithmetic cover subgroup is the preimage of the literal finite
   section in \(E_X/H_n\). It has geometric group \(H_n\), maps onto
   \(G_k\), and has constant field \(k\). For divisibility of levels,
   these subgroups, and hence the actual covers, are nested.
3. The one-puncture meridian is zero in geometric abelianization.
   Its proper cover is unramified, with \(n^{2g}\) distinct geometric
   boundary points. For at least two punctures, each meridian has
   exact order \(n\), giving the distinct ramification formula.
   For all hyperbolic types the level-three proper genus is positive
   and every nonempty lifted boundary has at least two points.
4. The proper torsor argument comes before choosing a rational origin.
   Stoll 8.2 then gives that origin. Only the ensuing compatible
   finite Kummer classes enter the inverse Selmer localization map.
5. The nonsplit boundary module is the literal permutation Tate module
   modulo its sum. A.169's split-field coordinate detection and
   restriction maps recover the rational cusp inertia line.
   No local-global theorem for an arbitrary torus is substituted.
6. Full reference injectivity is first proved on the fixed positive-genus
   cover. A geometric conjugator downstairs is lifted to the original
   geometric group; both full references then lie in the same
   arithmetic cover subgroup. This handles finite-sheet ambiguity.
7. The higher full references are compared on that same level-three
   curve. They therefore give one fixed full point/cusp reference,
   including its entire tangent parameter. All compact conjugator
   sets lie in the single group \(H_3/\Pi''\).
8. The identity \(\bigcap H_{3j!}'=\Pi''\) is proved for the actual
   profinite surface group by extending a finite character of
   \(\Pi'\) to \(\Pi'W\). It does not require the group to be free.
9. The tripod equations and transition constants are displayed
   separately. The quotient at level three has an open
   \(\widehat{\mathbf Z}^{10}\) kernel, so it is explicitly an
   all-coefficient quotient, not a finite detector.

## Reproducible finite checks

code/metabelian_finite_support_certificate.py computes the integral
boundary Smith forms in the actual Fermat cover graphs, verifies the
genus/boundary identities across hyperbolic types, and checks the
literal polynomial cover maps and their compositions.
Its output and JSON data are retained next to the code.

Executed result: eight actual Fermat cover graphs with primitive
integral boundary Smith forms; 264 hyperbolic surface cases; 40 literal
Fermat maps; 96 transition compositions. Every check passed.

Root and Birational independently passed the saved main proof through
A.178.21; Birational independently reran the certificate and reopened
the cited primary statements.

The root-requested rational Abel–Jacobi corollary was then appended as
A.178.22–24. Its exact new map is the closed fibre
Spec(k) ×_J C. An actual local point forces that closed subscheme of
Spec(k) to equal Spec(k), hence gives the unique rational centre.
The point/cusp classification and full tangent injection then use
the proved fixed-cover comparison. Both peers have been asked to
audit this appended form. Both Birational and Local have now passed the
complete A.178.1–24 source, including the identical local-cover constant
in the tangent comparison. Both independently reran the full certificate
and reread the retained primary theorem passages. Root has the stable
source and all three audit results. Parent integration remains root-owned.
