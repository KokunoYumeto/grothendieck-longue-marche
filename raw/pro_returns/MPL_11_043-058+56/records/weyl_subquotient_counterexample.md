# A concrete check of the Weyl-subquotient statement on 56/016

Research-only calculation, 16 November 2026. This record concerns the literal frozen statement in `pages/MPL_11_043-058+56_56_scan016.tex`, Lemma 2.3, and the map discussed in N069 of the main notes. No transcription or source image was changed. The lemma on that sheet names an affine smooth algebraic group over an algebraically closed field and an inclusion R⊂T of two subtori; maximality of T is not stated there. The selected sheet cancels the opening of its proof.

## 1. Explicit groups and maps

Work over k=ℂ and put

\[
G=\operatorname{SL}_{4,k},\qquad
D=\{\operatorname{diag}(t_1,t_2,t_3,t_4):t_1t_2t_3t_4=1\}.
\]

Define

\[
r=(3,1,-1,-3),\qquad a=(1,2,-7,4),
\]
\[
R=\{\operatorname{diag}(s^3,s,s^{-1},s^{-3}):s\in\mathbb G_m\},
\]
\[
\chi_a:D\longrightarrow\mathbb G_m,
\quad \operatorname{diag}(t_i)\longmapsto t_1t_2^2t_3^{-7}t_4^4,
\qquad T=\ker\chi_a.
\]

The inclusion R→D is a closed torus embedding: its inverse on its image is the second diagonal coordinate. Both vectors have coordinate sum zero, and

\[
a\cdot r=3+2+7-12=0.
\]

Hence the composite R→D→𝔾_m is the unit map, giving the exact inclusion R⊂T.

The character lattice of D is

\[
X^*(D)=\mathbb Z^4/\mathbb Z(1,1,1,1).
\]

The lattice isomorphism to ℤ³ sends a class [b] to
\((b_1-b_4,b_2-b_4,b_3-b_4)\). It sends [a] to

\[
(-3,-2,-11),\qquad\gcd(-3,-2,-11)=1.
\]

Thus [a] is primitive, and the quotient lattice \(X^*(D)/\mathbb Z[a]\) is free of rank two. The associated exact character sequence is

\[
0\longrightarrow\mathbb Z[a]\longrightarrow X^*(D)
\longrightarrow X^*(T)\longrightarrow0.
\]

The same torus assertion has a completely explicit coordinate verification:

\[
\theta:\mathbb G_m^2\xrightarrow{\sim}T,
\quad(s,u)\longmapsto
\operatorname{diag}(s^3u^2,su^{-3},s^{-1},s^{-3}u).
\]

Its inverse is

\[
s=t_3^{-1},\qquad u=t_4t_3^{-3}.
\]

To check the inverse, the determinant equation and χ_a=1 give
\(t_2=t_3^8t_4^{-3}\) and \(t_1=t_3^{-9}t_4^2\), exactly the first two entries of θ after substitution. Under θ, the inclusion R⊂T is \(s\mapsto(s,1)\). In particular, these are concrete smooth connected subtori of dimensions one and two.

## 2. Exact centralizers

The action of R on k⁴ has four distinct characters, with exponents 3,1,−1,−3. Commutation with every element of R forces the off-diagonal matrix entries to vanish: the (i,j) entry is multiplied by the character \(s^{r_i-r_j}\), which is nonconstant for i≠j. Intersecting the resulting diagonal invertible matrices with SL₄ gives

\[
C_G(R)=D.
\]

The four characters of T, in the θ coordinates, are

\[
(3,2),\quad(1,-3),\quad(-1,0),\quad(-3,1).
\]

They are pairwise distinct. The identical entrywise calculation gives

\[
C_G(T)=D.
\]

Equivalently, a root character e_i−e_j cannot lie in the rational span of a and (1,1,1,1): at the two coordinates outside {i,j}, it vanishes, whereas those two coordinates of a differ. This forces the coefficient of a to vanish, and then the constant coefficient to vanish as well.

## 3. Normalizer quotient for R

Every matrix normalizing R permutes its four one-dimensional weight spaces, so it is monomial. Its permutation part acts on the cocharacter r. An automorphism of the torus R≅𝔾_m acts on its character lattice ℤ by +1 or −1, so the permutation must send r to r or −r.

The entries of r are distinct. Exactly two permutations do this:

\[
\mathrm{id},\qquad w=(14)(23).
\]

The permutation matrix P of w has determinant +1 and belongs to SL₄. Its conjugation acts by

\[
P\operatorname{diag}(s^3,s,s^{-1},s^{-3})P^{-1}
=\operatorname{diag}(s^{-3},s^{-1},s,s^3),
\]

which is the displayed element of R with parameter s^{-1}. Therefore

\[
N_G(R)=D\rtimes\langle P\rangle,\qquad
W(R)=N_G(R)/C_G(R)\simeq C_2.
\]

## 4. Normalizer quotient for T

The four T-weight spaces are also distinct one-dimensional coordinate lines, so a normalizer of T is monomial. Its permutation σ preserves the kernel of χ_a precisely when it preserves the primitive rank-one character subgroup ℤ[a]. At the lattice level this gives

\[
\sigma(a)=\varepsilon a+c(1,1,1,1),
\qquad\varepsilon\in\{1,-1\},\quad c\in\mathbb Z.
\]

Both a and σ(a) have coordinate sum zero. Summing that equation gives 4c=0, hence c=0. The entries of a are pairwise distinct, so σ(a)=a forces σ=id. The two multisets

\[
\{1,2,-7,4\},\qquad\{-1,-2,7,-4\}
\]

differ, excluding σ(a)=−a. Consequently

\[
N_G(T)=D,\qquad W(T)=N_G(T)/C_G(T)=1.
\]

This calculation concerns the full normalizer: the distinct-weight-space argument accounts for every possible matrix normalizer before the permutation check begins.

## 5. The exact map in N069

The map proposed there is

\[
H=\frac{N_G(R)\cap N_G(T)}{C_G(T)}
\longrightarrow\frac{N_G(R)}{C_G(R)}=W(R),
\qquad gC_G(T)\longmapsto gC_G(R).
\]

For the displayed groups,

\[
N_G(R)\cap N_G(T)=D=C_G(T),\qquad
H=1,\qquad W(R)=C_2.
\]

Its image is the identity subgroup. Moreover W(T)=1 has only the trivial subgroup and only the trivial quotient, while W(R) has two elements. This establishes a concrete counterexample to the unrestricted subquotient conclusion as transcribed. It also pinpoints the map whose surjectivity cannot be established for these exact groups.

The calculation does not alter the frozen wording or propose a replacement conditional theorem. Its documentary consequence is to check the role and scope of T in the source's statement and proof, retaining the literal current reading.

## 6. Primary printed comparison

[SGA 3, Exposé XII, checked re-edition](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo12.pdf), pp. 128–129: the proof uses “puisqu’ils sont maximaux dans G”. The main notes give the version and statement/proof comparison. This was a local witness check, without an all-editions or errata search or a novelty claim.

## 7. Reproducible finite calculation

`records/weyl_subquotient_permutation_check.py` uses only Python's standard library and integer arithmetic. It checks the primitive character, all 24 coordinate permutations, the r-line stabilizer, the [a]-line stabilizer in ℤ⁴/ℤ(1,1,1,1), and their intersection. It also checks that the [a]-quotient calculation agrees with the sum-zero ±a calculation for every permutation. Run from any working directory; its full result is printed as JSON. The script corroborates the finite permutation step. The preceding distinct-weight arguments prove why that finite step computes the full normalizers.
