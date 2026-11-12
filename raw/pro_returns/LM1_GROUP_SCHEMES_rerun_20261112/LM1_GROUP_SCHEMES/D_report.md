| Task | Outcome | Statements | Scope and remaining question |
|---|---|---|---|
| D(a) | proved | D.1–D.3 | The final signed modular scheme: integral, all local, profinite integral, and finite adelic points, including the group operations and the local norm restrictions. |
| D(b) | partly settled | D.4–D.7 | Conditional lifted comparison, a closed subgroup of infinite index forced by the global signs, an explicit extra point, finite relations (I)–(II), and a noncongruence quotient. The three actual profinite images, their kernels, and a compatible invisible loop solution remain undecided. |
| D(c) | partly settled | D.8–D.11 | All eight component-group extension classes and the full geometric extension groups for \(M\), \(M(0)\), and \(M[0]\); the prescribed class and its complements; an obstruction at 2. The integral extension classification and arithmetic descent remain undecided. |
| D(d) | refuted | D.12–D.13 | The literal cup product in scans 610–611 is \((-3,3)=0\), of order one. The proposed \((-1,-3)\) is a different class of order two. The \(C_4\) of scan 631 is an inverse-image group. |
| D(e) | refuted | D.14–D.16 | A constant dicyclic lift with the indicated imaginary quadratic sign is impossible. The exact constant lifting criterion and full-image constant and arithmetically twisted replacements are proved, with explicit fields and ramification. |
| D(f) | proved | D.17 | The modular matrices generate \(\mathrm{SL}_2(\mathbb Z/n)\); adding the determinant-minus-one generator gives the determinant-\(\{\pm1\}\) subgroup of \(\mathrm{GL}_2(\mathbb Z/n)\). The indices are computed for every \(1\leq n\leq48\) and proved for every \(n\). |
| D(g) | proved | D.18–D.20 | A precise realization-based motivic definition, the requested torsion and unipotent constructions with theorem-numbered reductions, an obstruction for arbitrary discrete representations, and the exact arithmetic descent condition. |
| Item 3 | proved | D.1–D.3, D.18–D.20 | Adelic points and the two requested geometric representation families are treated; arbitrary discrete input requires the additional structures and descent data explicitly stated in D.20. |
| Item 4 | partly settled | D.8–D.17 | The geometric extension classification, complements, Brauer calculation, corrected class-field exercise, and modular generation are settled. The integral extension classification is the precise remaining obstruction. |
| Lead 4 | refuted | D.8–D.13, D.16 | The written extension is a finite dihedral component-group inflation. Its literal arithmetic cup product vanishes. The symbol \((-1,-3)\), the constant dicyclic lifting obstruction, and the retained arithmetic determinant action are distinguished. |

# Part D: proof, computation, and source report

This report accompanies `sections/D.tex`. The section contains twenty numbered statements: fourteen **Proved**, one **Known** with its reduction, three **Refuted** with replacements, and two **Open** with proved cases, executed computations, and exact remaining questions. No priority is claimed. The mathematical text and programs are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

The coverage table uses “proved” in the prompt's sense, including the strongest explicitly stated correct form. It does not assert that the complete integral extension classification or the three global Galois/GT comparison problems have been solved. Those are the two partial results D.7 and D.11.

## 1. Definition and comparison conventions

The calculations use the final modular group scheme of scans 479–481, with

\[
\rho=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\qquad
\sigma=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]

and triples \((a,b,U)\), where \(a=d+c\rho\),

\[
b=\begin{pmatrix}u&t\\-et&eu\end{pmatrix},\quad
e^2=(e')^2=1,\quad
\det U=e(t^2+u^2)=e'(c^2+cd+d^2).
\]

Here \(e=\varepsilon_2\), \(e'=\varepsilon_3\). This is the convention established in Parts A–B. In particular, the group law is inherited from the three matrix factors; it is not an arbitrary law on a twisted-conjugacy solution space.

D.1 expresses the points as

\[
M(R)=\mathrm{SL}_2(R)\rtimes H_R,
\]

where \(H_R\) is a pair of quadratic-algebra units with equal signed norms, and the action on \(\mathrm{SL}_2(R)\) is conjugation by \(\operatorname{diag}(\chi,1)\). The multiplication on the Gaussian unit factor includes conjugation when \(e=-1\). Over \(\mathbb Z\), this gives

\[
M(\mathbb Z)\cong C_6\times
\bigl(\mathrm{SL}_2(\mathbb Z)\rtimes D_8\bigr).
\]

D.2 gives all local norm images and the norm-one kernels, including residue characteristics 2 and 3. At 2 the Gaussian unit norm is \(1+4\mathbb Z_2\); at 3 the Eisenstein unit norm is \(1+3\mathbb Z_3\). All the other unit norms are surjective. For rational local points, the determinant valuation is even unless \(p\equiv1\pmod {12}\). D.3 proves

\[
M(\widehat{\mathbb Z})=\prod_pM(\mathbb Z_p),\qquad
M(\mathbb A_f)=\prod_p' M(\mathbb Q_p)
\]

with respect to the displayed integral local subgroups; the proof checks finite presentation and the finite-denominator condition.

The comparison target must retain the distinction between a global sign \(C_2\), the group \(\mu_2(\widehat{\mathbb Z})=\prod_pC_2\), and a quotient by the manuscript's finite global scalar group. The source passage does not by itself give an unquotiented homomorphism from each bare profinite group to \(M(\widehat{\mathbb Z})\). D.4 supplies the comparison once a genuine matrix realization and the compatible central lift have been specified, or on the explicitly typed pullback group. It does not silently supply a section of that pullback.

## 2. The comparison question: what has actually been established

For any comparison respecting the global signs, both sign coordinates are constant across all primes. The resulting closed subgroup of \(M(\widehat{\mathbb Z})\) has infinite index and empty interior. D.4 gives an explicit point outside it: at \(p=5\), take \(a=sI\), where \(s^2=-1\) and \(s\equiv2\pmod5\), take \(b=U=I\), and take \((e,e')=(1,-1)\); take the identity at every other prime. The same obstruction survives quotienting by the finite scalar group. This proves the stated nonopenness result whenever the comparison is defined with the manuscript's global signs.

The finite computation uses the conventions for Drinfeld's (I) and (II) from Schneps's primary lecture text, page 19. It evaluates one common commutator word in all the required matrix substitutions, by enumerating the derived subgroup of a generated subgroup of a fourfold product. It also checks the induced finite automorphism condition. It is not an independent choice of four unrelated values of \(f\).

| Modulus | Size of the two-generator matrix group | Size of the evaluated commutator subgroup | Unit multipliers tested | Solutions per multiplier |
|---|---:|---:|---|---:|
| 2 | 1 | 1 | \(1\pmod2\) | 1 |
| 3 | 24 | 8 | \(1,5,7,11\pmod {12}\) | 3 |
| 4 | 4 | 1 | \(1,3\pmod4\) | 1 |
| 6 | 24 | 8 | \(1,5,7,11\pmod {12}\) | 3 |
| 12 | 96 | 8 | \(1,5,7,11\pmod {12}\) | 3 |

These are finite relation solutions. No row identifies them with the actual reduction of \(\widehat{\mathrm{GT}}_0\), \(\widehat{\mathrm{GT}}\), or \(G_{\mathbb Q}\).

D.6 constructs and enumerates the quotient \(\mathrm{SL}_2(\mathbb F_8)\), of order 504. Its conjugacy classes have sizes \(1\), four classes of size \(56\), one of size \(63\), and three of size \(72\); the enumeration proves simplicity by testing unions of conjugacy classes. An elementary argument with congruence \(p\)-kernels and order-\(p\) unipotent generators then proves that this is not a congruence quotient. This establishes a nontrivial modular congruence kernel. It does not establish a nontrivial kernel on the subgroup of loop solutions.

The exact first unresolved finite-to-profinite question is the candidate at modulus 3 with \(\lambda=1\) and

\[
f(x,y)=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]

Does it extend to a compatible profinite pair satisfying (I) and (II), and then to \(\widehat{\mathrm{GT}}\) or the arithmetic image? The second exact obstruction is to find a loop solution that is trivial in every congruence coordinate but nontrivial in the displayed \(\mathrm{SL}_2(\mathbb F_8)\) quotient, or to prove that none exists. Neither follows from the nontriviality of the ambient congruence kernel. The actual bare-source comparison maps, their full images and kernels, and the proposed strict comparison between Galois and \(\widehat{\mathrm{GT}}_0\) remain on the page.

## 3. Central extensions and the obstruction at 2

D.8 computes all eight classes in

\[
H^2(C_2^2,C_2)\cong\mathbb F_2^3
\]

by an exhaustive normalized-cocycle calculation and an independent presentation argument. The isomorphism types are \(C_2^3\), three copies of \(C_4\times C_2\), three copies of \(D_8\), and \(Q_8\), with the fixed identifications of kernel and quotient distinguishing the classes. In the coordinates \(u=\varepsilon_3\), \(v=\varepsilon_2\), the manuscript's cocycle is \(u(x+y)\), representing \(u^2+uv\). Its square function is \(u(u+v)\). The resulting group is \(D_8\), and the specified complements are not normal.

D.9 goes beyond that finite calculation. It proves the full geometric result

\[
\operatorname{Ext}_{\mathrm{cen}}(M_{\mathbb C},\mu_2)
=H^2(BM_{\mathbb C},\mu_2)
\cong\mathbb F_2^5,
\]

and the same result for \(M(0)_{\mathbb C}\) and \(M[0]_{\mathbb C}\). The proof writes the identity component explicitly, uses the Kummer description of its double covers, computes the invariant character classes, constructs an explicit component-group section, and proves that the remaining kernel descends to \(C_2^2\). The two connected-component classes and the three component-group classes account for all five dimensions. No spectral-sequence differential is assumed to vanish without a construction.

D.10 proves that every central extension over \(\mathbb Z_2\), or over \(\mathbb Z\), with exact prescribed kernel \(\mu_2\) and quotient \(\mu_2^2\) is commutative. Indeed, the commutator gives a morphism from the connected scheme \(\mu_2^2\) to the constant dual \(C_2^2\), which must be trivial. Thus the complex dihedral component extension cannot be extended by simply replacing the constant groups with these root-of-unity group schemes. This conclusion concerns that exact kernel and quotient; it does not compute the extensions of the full nonreduced modular scheme.

The remaining integral question is the kernel and image of

\[
\operatorname{Ext}_{\mathrm{cen}}(M[0]_{\mathbb Z_2},\mu_2)
\longrightarrow
\operatorname{Ext}_{\mathrm{cen}}(M[0]_{\mathbb Q_2},\mu_2).
\]

Flat torsors on the nonreduced special fibre and arithmetic descent of the complex classes are not classified here. D.11 records this precise obstruction together with the proved geometric classification and the executed finite and character calculations. The independent review of D.9 and D.10 found no defect in these two arguments.

## 4. Brauer calculation and explicit class-field replacements

Scans 610–611 identify the two quadratic characters with \(\mathbb Q(\sqrt{-3})\) and \(\mathbb Q(\sqrt3)\). Their cup product is therefore

\[
c=(-3,3)=0\quad\text{in }\operatorname{Br}(\mathbb Q).
\]

D.12 gives an explicit splitting by two matrices that square to \(-3\) and \(3\), anticommute, and span the four-dimensional matrix algebra together with their product and the identity. The independent Hilbert-symbol program confirms the local calculation. In particular, this class has order one, including after passage to \(\mathbb Q(i)\).

By contrast, \((-1,-3)\) ramifies exactly at 3 and the real place and has order two. It is the Bockstein obstruction for lifting the character of \(\mathbb Q(\sqrt{-3})\) to a constant \(C_4\), not the literal cup product on scan 611. A nontrivial geometric extension may have trivial pullback to a particular arithmetic group, so the vanishing of \(c\) does not contradict D.9. The cyclic group of order four on scan 631 is an inverse-image group; it cannot be read as the order of this Brauer class.

The constant group \(\mathrm{Dic}_3\) has order 12 and is \(S_3\times_{C_2}C_4\). Every lift of an odd permutation has order four. Complex conjugation therefore prevents a constant \(G_{\mathbb Q}\to\mathrm{Dic}_3\) lift of an \(S_3\)-representation with sign character \(\chi_{-3}\). D.15 proves the exact replacement: an \(S_3\)-representation with nontrivial sign \(\chi_a\) lifts precisely when \(\chi_a\) lifts to \(C_4\), equivalently when \((a,-1)=0\), equivalently when \(a\) is a norm from \(k(i)\). For \(\mathbb Q\) and squarefree \(a=d\), the criterion is \(d>0\) and every odd prime dividing \(d\) is \(1\pmod4\). The proof includes the global class-field reduction and explicit local character construction. Surjectivity of the \(S_3\)-representation gives full image in \(\mathrm{Dic}_3\).

Two explicit full-image fields realize the corrected statements:

| Field | Galois group over \(\mathbb Q\) | Ramified primes | Local \((e,f,g)\) |
|---|---|---|---|
| Splitting field of \(x^3-12x-14\), composited with \(\mathbb Q(\zeta_5)\) | \(\mathrm{Dic}_3\), order 12 | 2, 3, 5 | At 2 and 3: \((3,4,1)\); at 5: \((4,1,3)\). |
| \(\mathbb Q(2^{1/3},3^{1/4},i)\) | \(\mathrm{Dic}_3\rtimes C_2\cong S_3\times_{C_2}D_8\), order 24 | 2, 3 | At both: \((12,2,1)\). |

For the second field, the group over \(\mathbb Q(i)\) is the full \(\mathrm{Dic}_3\). In \(F=\mathbb Q(3^{1/4},i)\), write \(R(3^{1/4})=i3^{1/4}\), \(R(i)=i\), and let \(B\) be complex conjugation. The common quadratic character \(\chi_{-3}\) is rotation parity plus reflection parity; the determinant character \(\chi_{-1}\) is reflection parity alone. The arithmetic involution is represented by \(RB\), not by \(B\). These labels are essential for the stated semidirect product.

The local arguments are supplied in D.16. In particular, the quartic extension at 2 is proved totally ramified by an Eisenstein translate and is proved not to contain \(i\); adjoining \(i\) gives local degree eight, ramification index four, and residue degree two. The programs check discriminants, the cubic integral index, the finite quotient, the quartic characters, and the Eisenstein certificates. The ramification tables are conclusions of the written local proof, not inferred from an unsupported numerical factorization.

## 5. Generation and motivic realization

D.17 proves that \(\rho,\sigma\) generate \(\mathrm{SL}_2(\mathbb Z/n)\) for every \(n\). With the displayed determinant-minus-one matrix \(\tau\), the generated group in \(\mathrm{GL}_2(\mathbb Z/n)\) is exactly the inverse image of \(\{\pm1\}\) under the determinant. Its index is \(\varphi(n)/2\) for \(n>2\), and one for \(n=1,2\). The complete enumeration through \(n=48\) agrees. In the integral profinite group the determinant subgroup is the two global signs, giving infinite index and empty interior. The \(G^+\mid G^*\) reading on scan 652 remains a reading issue; the theorem states both matrix interpretations rather than identifying the symbols without evidence.

D.18 states the realization-based definition of universal mixed elliptic motives from Hain and Matsumoto (2020, Definition 6.1, in the explicitly recorded preprint version). The text supplies the Betti, de Rham, filtered, weight, comparison, and arithmetic compatibility data and treats integral lattices as additional structure. It proves the torsion specialization statement using the finite étale torsion group schemes over the base where the level is invertible and the Weil pairing. For the unipotent fundamental group, it applies Example 6.6, Theorem 6.9, and Corollary 6.10 of that version, with the genuine-versus-outer action and the basepoint/path dependence stated explicitly. The reduction to the weighted-completion results of Hain and Matsumoto (2003) spells out the hypotheses of Theorem A.6, Propositions 8.2–8.3, and Theorem 8.4.

D.19 disproves a construction from an arbitrary discrete representation alone. Its explicit two-dimensional representation of the modular group has cusp eigenvalues of absolute value different from one and hence no positive power of the cusp monodromy is unipotent. A separate quadratic-twist example proves that geometric representations alone do not determine the arithmetic realization. The program counts points at six primes for the two curves and verifies the trace twist. D.20 gives the exact extension condition for a geometric representation along a split arithmetic fundamental-group sequence; the possible extensions are described by continuous nonabelian \(H^1\) with coefficients in the geometric centralizer. No assertion is made that the equations defining \(M\) automatically supply these motivic or arithmetic structures.

## 6. Source audit and reproducibility

The manuscript text was checked against the supplied transcription and the named scans, in particular scans 489, 546, 596–605, 610–611, 629, 631, 634, and 652. The convention at scans 479–481 is shared with the Part A–B reconstruction. Source citations in the paper distinguish the archive scan from the manuscript folio and its lower pagination. Eleven mathematically relevant reading entries are supplied in `D_readings.json`. They cover the quotient by scalar signs, the sign and square formulas, the complement automorphism notation, the \(E\mid E^{\mathrm{ab}}\) kernel, the cohomological-degree slip for characters, the \(C_4\) interpretation, the constant-versus-twisted lift, the generation symbol, and the insufficient reductivity condition in the motivic passage. They are evidence for the editors, not declarations that uncertain handwriting has been settled.

`D_refs.bib` contains five verified entries. In addition to the manuscript, these are Milne's *Class Field Theory*, version 4.03, with Chapter I, Theorem 4.16 and Chapter III, Theorem 4.4; the two Hain–Matsumoto papers with version-specific theorem numbers; and Schneps's primary lecture text with the finite GT conventions. The 2003 journal date of *Weighted Completion* is recorded separately from its 2001 preprint-version BibTeX key. No result from an earlier package or a review is used merely on that package's authority.

The attached programs were executed under Python 3.12.14; `D_number_fields.py` uses SymPy 1.14.0. Each script has a saved `.out` file:

| Program | Executed verification |
|---|---|
| `code/D_finite.py` | Exact generated matrix groups for \(1\leq n\leq48\); exhaustive \(C_2^2\) cocycles; the dicyclic quotient of \(\mathrm{SL}_2(\mathbb Z/4)\); explicit quaternion splitting. |
| `code/D_gt.py` | Relations (I)–(II) and the finite automorphism test at \(2,3,4,6,12\); all elements and conjugacy classes of \(\mathrm{SL}_2(\mathbb F_8)\); norm tests modulo \(4,8,16,9,27,25,49\). |
| `code/D_components.py` | Explicit component section modulo 7 and the invariant Kummer-character calculation. |
| `code/D_number_fields.py` | Cubic irreducibility, discriminant and integral index; Hilbert symbols; quartic characters and local certificates. |
| `code/D_arithmetic.py` | The normal Klein-four quotient of \(\mathrm{GL}_2(\mathbb Z/4)\), its 24 elements, determinant action, and the local Eisenstein certificates used in D.16. |
| `code/D_motives.py` | The cusp counterexample, six elliptic twist point-count comparisons, and free-Lie dimensions \(2,1,2,3,6,9\) in degrees 1–6. The latter are not asserted to be Galois-image dimensions. |
| `code/D_registers.py` | Generation and consistency checking of all twenty statement rows, eleven reading rows, and ten coverage rows against the numbered LaTeX statements. |

To reproduce a calculation, run `python code/D_finite.py` and similarly for the other scripts from the package directory. The saved outputs make the exact computations independently inspectable. The two central-extension arguments and the explicit field/ramification constructions also underwent independent mathematical review by the agent responsible for Part C; this review is a consistency check, not a source of mathematical authority.

The section is supplied for inclusion in the merged LuaLaTeX paper; build and visual inspection are recorded in the package-level report. The remaining mathematical questions are exactly those in D.7 and D.11.
