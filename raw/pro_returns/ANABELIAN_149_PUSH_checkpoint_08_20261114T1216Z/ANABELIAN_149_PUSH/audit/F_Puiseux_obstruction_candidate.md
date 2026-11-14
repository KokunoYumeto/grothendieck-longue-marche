# A Galois-theoretic classification obstruction, including a countable pair

**Status:** independently reviewed by root and the finite-field agent, approved and integrated as Claim F.42 (Proved) in sections/F.tex. This note preserves the candidate derivation. Reconstruction means the actual closed-point-preserving relative small-étale-topos property of CHW throughout. This does not rule out a criterion using the field's arithmetic; it rules out one depending only on its topological absolute Galois group and cyclotomic character, even with field cardinality added.

## 1. The exact Puiseux fields

Let F have characteristic zero. Choose an algebraic closure Fbar and coherent symbols t^{1/n}, with (t^{1/mn})^m=t^{1/n}. All fields below lie in the formal Puiseux field over Fbar. Put

\[
 P(F)=\bigcup_{n\ge1}F((t^{1/n})),\qquad
 \Omega=\bigcup_{\substack{L/F\text{ finite},\ L\subset\bar F\\n\ge1}}
                       L((t^{1/n})).                         (1)
\]

The union uses common multiples of root degrees and composita of coefficient fields. Every element of Omega has coefficients in **one finite extension** L/F and a bounded denominator for its exponents. No series with arbitrarily increasing coefficient fields is silently included.

The exact Proposition on p.314 of van den Dries–Ribenboim(1984) states that this Omega is an algebraic closure of F((t)). The primary publisher PDF was reopened and its full proposition and proof read. Its proof checks L((t^{1/n}))=F((t))(L,t^{1/n}), so algebraicity is literal. It then uses henselianity, divisible value groupQ, algebraically closed residueFbar and residue characteristic zero to prove algebraic closedness. Thus Omega is also an algebraic closure of P(F), which is algebraic over F((t)). The statement is for every characteristic-zeroF; no number-field or completeness assumption onF is required.

Every element of Omega is in P(F)Fbar. Indeed, a finite F-basis of L decomposes any series in L((t^{1/n})) into a finite linear combination of series in F((t^{1/n})). Therefore

\[
                            \Omega=P(F)\bar F.                (2)
\]

The constants satisfy P(F)∩Fbar=F. To see this, an element of F((v)) algebraic overF has valuation zero (unless it is zero); reducing its irreducible polynomial modulo v gives a root inF, so that polynomial is linear. This also gives A(F)∩Fbar=F for the core below.

Restriction gives a topological isomorphism

\[
                     G_{P(F)}\xrightarrow{\sim}G_F.          (3)
\]

Its inverse acts coefficientwise and fixes every chosen t^{1/n}. This action fixes P(F), and(2) shows that an automorphism over P(F) is determined by its restriction toFbar. The map is continuous because the coefficients of each element lie in one finite extension; restriction is continuous as well. Thus(3) is an isomorphism of profinite groups, not merely an abstract group isomorphism.

All roots of unity lie inFbar, so the isomorphism preserves the full cyclotomic character. It preserves every open subgroup and its character restriction. In fact the finite extension E/F corresponds explicitly to

\[
 P(F)E=P(E)=\bigcup_n E((t^{1/n})).                            (4)
\]

Equality follows again by a finite coefficient-basis decomposition. Consequently all finite Galois-category data and all continuous Galois cohomology with matched finite modules, including Tate twists, agree under(3).

## 2. Failure of reconstruction despite(3)

F.41 proves failure over F((t)). If P(F) reconstructed, F.32 applied to the algebraic extension P(F)/F((t)) would make F((t)) reconstruct. This is a contradiction. Hence P(F) fails for everyF, and so does every algebraic extension of P(F), by the same contrapositive of F.32.

There is also an explicit witness: the formal substitution

\[
                 \sigma(t)=t+t^2,
 \qquad \sigma^{-1}(t)=r(t)=\frac{-1+\sqrt{1+4t}}2             (5)
\]

fixingF preservesP(F). Its extension toOmega fixesFbar and sends

\[
 t^{1/n}\longmapsto t^{1/n}(1+t)^{1/n},                       (6)
\]

with the constant-term-one binomial root. The formulas are compatible at all finite levels and have compatible inverse substitutions. This automorphism commutes with the coefficientwise G_F action. Its restriction toP(F) is nonidentity and has trivial outer Galois action. F.40 therefore gives a nonalgebraic, nonconstant, closed-point-preserving relative geometric endomorphism of the full Gm étale topos. On rational points its function is sigma^{-1}; values at1,2,t exclude all algebraic monomials.

## 3. A countable version with exactly the same Galois group

Define the algebraic Puiseux core

\[
 A(F)=\{\alpha\in P(F):\alpha\text{ is algebraic over }F(t)\},
\]

and let

\[
 \Omega_0=\{\alpha\in\Omega:\alpha\text{ is algebraic over }F(t)\}.
\]

The latter is algebraically closed: a root inOmega of a polynomial whose coefficients are algebraic overF(t) is again algebraic overF(t). It is algebraic overA(F), since F(t)⊂A(F). ThusOmega0 is an algebraic closure ofA(F).

We claim

\[
                            \Omega_0=A(F)\bar F.              (7)
\]

Take alpha∈Omega0. Choose a finite Galois extension L/F insideFbar and n such that alpha∈L((t^{1/n})). Let e_1,...,e_d be an F-basis ofL and e_1^*,...,e_d^* its trace-dual basis. For v=t^{1/n}, put

\[
 a_i=\operatorname{Tr}_{L((v))/F((v))}(e_i^*\alpha)
     =\sum_{g\in\operatorname{Gal}(L/F)}g(e_i^*\alpha).
\]

Here g acts coefficientwise and fixes t. Thus every summand is algebraic overF(t); so is a_i. By construction a_i∈F((v))⊂P(F), hence a_i∈A(F). The trace-dual identity gives alpha=sum_i e_i a_i. This proves one inclusion in(7); the other holds becauseA(F) andFbar lie inOmega0.

Restriction and coefficientwise action now give

\[
                         G_{A(F)}\simeq G_F,                 (8)
\]

again topologically and preserving the entire cyclotomic character. Continuity is verified by the same finite-coefficient argument. Equations(7)–(8) also identify every finite extension ofA(F) with A(F)E for a finite extensionE/F. A parallel trace argument gives A(F)E=A(E), when E is regarded inFbar.

The substitution(5) preservesA(F). In the forward direction, sigma(alpha) is algebraic over sigma(F(t))=F(t+t²)⊂F(t). In the inverse direction, sigma^{-1}(alpha) is algebraic overF(r(t)), which is algebraic overF(t). Both substitutions preserveP(F), so both preserve its algebraic core. The same argument preservesOmega0. OnOmega0 the extension(6) commutes with the coefficientwise action ofG_F; hence sigma|A(F) has trivial outer Galois action. Since it moves t, F.40 proves failure of reconstruction overA(F), with the same explicit full-topos endomorphism witness. Every algebraic extension ofA(F) also fails, by F.32.

The fieldA(F) is algebraic overF(t), so its cardinality is max(|F|,aleph0). In particularA(Q) is countable. The positive fieldQ reconstructs by F.37, whereasA(Q) does not, but

\[
 (G_{A(\Q)},\chi_{A(\Q)})\simeq(G_{\Q},\chi_{\Q})
\]

and both fields are countable. This proves that neither the profinite Galois group alone, nor that group with its full cyclotomic character, all open-subgroup data, and field cardinality, determines the reconstruction property.

The conclusion does not say that no intrinsic criterion on fields can exist. It requires such a criterion to use arithmetic information not contained in the indicated Galois data. F.9's full necessary-and-sufficient field classification remains unresolved.

## Primary source reopened

L. van den Dries and P. Ribenboim(1984), *The Absolute Galois Group of a Rational Function Field in Characteristic Zero is a Semi-Direct Product*, Canadian Mathematical Bulletin27(3),313–315, exact Proposition p.314 and full proof. Primary PDF:
<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D25D46CEEAC14FF372584F2603E86360/S0008439500067916a.pdf/the-absolute-galois-group-of-a-rational-function-field-in-characteristic-zero-is-a-semi-direct-product.pdf>.

The current web open is turn557view0; the exact proposition appears in lines46–51 of its extraction. Existing bibliography keyF_vanDenDriesRibenboim1984 applies. The coefficient decomposition, algebraic-core argument, semilinear topos witness and contrast of fields are proved here, using F.32,F.37,F.40–F.41.
