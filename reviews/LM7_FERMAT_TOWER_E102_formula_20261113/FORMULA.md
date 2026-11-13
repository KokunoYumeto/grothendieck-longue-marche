# The formula behind E.102 of LM7_FERMAT_TOWER (13 Nov 2026)

By Claude Fable 5.2 at effort max, launched by the main session (Claude Opus 5.5 at effort max). E.102 is a statement
of GPT-6 Astra (ChatGPT Pro mode); its Smith form was confirmed by the main session (RESULT.md) and again here with
separate code. All code here is my own; from the return only the degree-one data were read (never run).

## 1. The formula

Notation. O = Z_3[zeta], s = sqrt(-3). V = Z_3^10 = H_1 of the Fermat cubic minus its 9 flexes, 0 -> C -> V -> W -> 0,
W = O (tau = multiplication by pi = 1 + 3 zeta, c = conjugation), C = the 8 cusp loops (tau = chi = 7,
c = -(permutation Q -> conj Q of the cusp labels in O/3)). The c-signs on C are (C+, C-) = (3, 5).
K_4 = Lambda^2 Lambda^2 V, C_4 = K_4/(T_4 - 1)K_4^{c=+1}.

**Formula.** Put d+ = C+ - 1 = 2, d- = C- - 1 = 4, n = d+ + d- = 6, a = C(d+,2) + C(d-,2) = 7, b = d+ d- = 8. Then

| factor | multiplicity | value |
|---|---|---|
| C_3  | n^2 + n + a + C(a,2) + C(b,2) + d+ a + d- b | 36 + 6 + 7 + 21 + 28 + 14 + 32 = **144** |
| C_9  | b + d- + d+ b + d- a | 8 + 4 + 16 + 28 = **56** |
| C_27 | 2 + 2b + 2n | 2 + 16 + 12 = **30** |
| C_81 | a + d+ | 7 + 2 = **9** |
| Z_3  | rank K_4^{c=-1} | **504** |
| unit pivots | rank K_4^{c=+1} - (144 + 56 + 30 + 9) | 486 - 239 = **247** |

It comes from three facts (proved in section 2) and one table:

1. **Torsion = Galois invariants.** tors C_4 = H^0(<tau, c>, K_4 (x) Q_3/Z_3), and C_4/tors is free of rank
   rank K_4^{c=-1}.
2. **Splitting.** Over <tau, c>:  V = V_1 (+) chi (x) D_0, where
   V_1 = {(w, w') in O x O : w = w' mod 3}, tau = (pi, chi), c = (conj, conj) (rank 4: W glued to a rank-2 part of C
   by the Weil pairing), and D_0 = Z_3^6 with tau = 1 and c-signs (d+, d-) = (2, 4). Only V_1 is non-split; six of the
   eight cusp directions are plain copies of the cyclotomic character with a sign.
3. **Six pieces.** K_4 = sum of P (x) (sign space), with the pieces P and multiplicities (m+, m-):

| piece P | rank | (m+, m-) in general | for (2,4) | Q+(P) | Q-(P) |
|---|---|---|---|---|---|
| a: Lambda^2 Lambda^2 V_1 | 15 | (1, 0) | (1, 0) | C_27^2 | C_9^2 + C_81 |
| b: chi^2 Lambda^2 V_1 | 6 | (d+^2 + d-^2, 2 d+ d-) | (20, 16) | C_3 | C_3 + C_27 |
| c: chi^2 S^2 V_1 | 10 | (a, b) | (7, 8) | C_3 + C_81 | C_9 |
| d: chi^4 | 1 | (C(a,2) + C(b,2), a b) | (49, 56) | C_3 | 0 |
| e: chi Lambda^2 V_1 (x) V_1 | 24 | (d+, d-) | (2, 4) | C_3 + C_27^2 + C_81 | C_3 + C_9 + C_27^2 |
| f: chi^3 V_1 | 4 | (d+ a + d- b, d+ b + d- a) | (46, 44) | C_3 | C_9 |

   Here Q+-(P) = torsion of P/(tau - 1)P^{c=+-1} = H^0(<tau,c>, P (x) sgn^{+-} (x) Q_3/Z_3), and

   **tors C_4 = sum over P of Q+(P)^{m+} (+) Q-(P)^{m-}.**

   C_3: 20 + 16 (b) + 7 (c) + 49 (d) + 2 + 4 (e) + 46 (f) = 144. C_9: 8 (c) + 4 (e) + 44 (f) = 56.
   C_27: 2 (a) + 16 (b) + 4 + 8 (e) = 30. C_81: 7 (c) + 2 (e) = 9.

The nine C_81 are: the 7 c-even pairs of free cusp directions tensored with S^2 V_1, and the 2 c-even free cusp
directions tensored with Lambda^2 V_1 (x) V_1.

The table is valid for chi = N(pi) and every CM value pi = 1 + 3a with a = a0 + a1 s, a0 and a1 both units
(N(pi) not 1 mod 9, pi not conj(pi) mod 9): checked for all 36 such pi with a = x + y zeta, |x|, |y| <= 4
(`fable_step6_table_scan.py`). Facts 1-3 hold for every pi = 1 mod 3, chi = 1 mod 3, every c-equivariant glue and
all signs; outside that class the six entries Q+-(P) change and are computed from the same six small modules.

## 2. Derivation

**2.1 Torsion = invariants.** T - 1 is injective on K_Q (no eigenvalue 1). x -> (T-1)x identifies tors C_4 with
{y in K_Q^{c=+} : (T-1)y in K}/K^{c=+}. Such a y gives a class in K_Q/K fixed by T and c; conversely a class fixed by
both has the representative (y + cy)/2 (2 is a unit), unique modulo K^{c=+}. So tors C_4 = (K (x) Q_3/Z_3)^{<T,c>},
and the number of factors of order >= 3^k is dim_{F_3} of the image of (K/3^k)^{<T,c>} in K/3. The free quotient has
rank 990 - 486. The group depends only on the closure of <T, c>; T' = cTc commutes with T, and the closure of
<T, T'> is {(u, N(u)) : u in 1 + 3O} acting by u on W and by the norm N(u) on C.

**2.2 The splitting.** In the coordinates (w, gamma), gamma = z - U w/3 (z the cusp coordinates of the return, U the
8 x 2 matrix with row (v, -u) at the cusp u + v zeta), the lattice is V = {(w, gamma) : gamma + U w/3 integral} and
tau = (pi, 7), c = (conj, c_C) are diagonal. U mod 3 is the Weil pairing w -> (Q -> e_3(w, Q)) : W/3 -> C/3; it is
injective and c-equivariant. Put phi = (U + c_C U c_W)/2 : W -> C. Then phi = U mod 3 and phi c_W = c_C phi. Hence
V_1 = {(w, -phi(w')/3) : w = w' mod 3} is a sublattice of V of rank 4, stable under tau (pi = 7 = 1 mod 3) and c;
V_1 meets C in phi(W), and V = V_1 (+) C_2 for any c-stable complement C_2 of phi(W) in C (2 is a unit). C_2 = 7 (x) D_0
with signs (3,5) - (1,1) = (2,4). Verified exactly: `fable_step2_pieces.py` prints the base change S (det 4) with
S^-1 T S = T_{V_1} (+) 7*1_6 and S^-1 J S = J_{V_1} (+) diag(1,1,-1,-1,-1,-1).
The same argument gives V = V_core (+) chi D_0 for a glue of rank 1 (V_core of rank 3) or 0 (V_core = W).

**2.3 Six pieces.** With D = chi D_0 a sum of c-eigenlines with scalar tau:
Lambda^2 V = Lambda^2 V_1 (+) V_1 (x) D (+) Lambda^2 D, and Lambda^2 of that sum is
Lambda^2 Lambda^2 V_1 (+) [Lambda^2 V_1 (x) S^2 D (+) S^2 V_1 (x) Lambda^2 D] (+) Lambda^2 Lambda^2 D
(+) Lambda^2 V_1 (x) V_1 (x) D (+) Lambda^2 V_1 (x) Lambda^2 D (+) V_1 (x) D (x) Lambda^2 D
(ranks 15 + 126 + 150 + 105 + 144 + 90 + 360 = 990). The multiplicities are the c-signs of S^2 D_0 (+) Lambda^2 D_0,
Lambda^2 D_0, Lambda^2 Lambda^2 D_0, D_0, D_0 (x) Lambda^2 D_0. Invariants of P (x) (sign space) are
Q+(P)^{m+} (+) Q-(P)^{m-}.

**2.4 The table.** Each Q+-(P) is the Smith form of an explicit integer matrix of size <= 24 (`fable_step2_pieces.py`,
computed modulo 3^9 and 3^12; ranks as expected). By hand:

- d: Z_3/(7^4 - 1) = C_3 (2400 = 3 * 800), c-even.
- Ring description. V_1 is free of rank one over the Gorenstein ring B = {(w, w')} = O[eps]/(eps^2 - 3 eps),
  eps = (3, 0), and tau, tau' act by multiplication by (pi, chi), (conj pi, chi). For a piece P cut out of
  chi^k V_1^{(x)m} by a 2-group of permutations, duality gives
  Q+-(P) = (isotypic part of A_m)^{c = +-(-1)^m},  A_m = B^{(x)m}/(chi^k tau^{(x)m} - 1, chi^k tau'^{(x)m} - 1),
  a finite ring (the sign (-1)^m because the generator of Hom(B, Z_3) is c-odd). Checked on all six pieces by
  `fable_step5_ring_check.py`.
- f (m = 1): the ideal is 3{(x, y) in O^2 : x = -y mod s}, so A_1 = C_9 * 1 (+) C_3 * s; hence Q-(f) = C_9, Q+(f) = C_3.
- b, c (m = 2), sketch: write E = eps_1 + eps_2, P = eps_1 eps_2. The scalar u in 1 + 3Z_3 acts by
  u^8 (1 - t eps_1)(1 - t eps_2), t = (u-1)/(3u). With eps_i^2 = 3 eps_i this forces E = 3 mu, P = 9 rho (rho a unit,
  mu = 8 mod 9), and E P = 6 P then gives 27 rho (mu - 2) = 0, i.e. 81 = 0: the unit element of A_2 has order 81.
  Continuing with the norm-one generator gives A_2^{sym} = (C_81 * 1 (+) C_3) (+) C_9 * (s_1 + s_2) and
  A_2^{alt} = C_3 (+) (C_27 * (s_1 - s_2) (+) C_3), c-even part first: rows c and b. The exact orders are the
  machine result.
- a, e (m = 4, 3): machine only (ranks 15 and 24).

**2.5 Where the exponents come from.** A scalar u in 1 + 3Z_3 acts on a tensor with m factors from W and 4 - m from C
by u^{8-m}; this is 1 mod 9 only for m = 2 (the "resonance" that gives the C_9 of the split model). The glue lets an
invariant have denominator 3 once per factor V_1. Row c: resonance 9 times two glue factors = 81. With the glue set to
zero the same formula (core W, D_0 = C with signs (3,5)) gives Z^504 + C_3^443 + C_9^43, the main session's split model.

## 3. Tests (`fable_step3_tests.py`, output `fable_step3_tests.out`)

Each line compares the direct Smith form of (T_4 - 1)(1 + J_4) on the rank-990 module (modulo 3^10) with the formula
(facts 1-3; the six Q+-(P) from the small modules of that datum). All agree.

| changed datum | direct Smith form = formula |
|---|---|
| none (actual) | Z^504 + C3^144 + C9^56 + C27^30 + C81^9 |
| glue 0 (split) | Z^504 + C3^443 + C9^43 |
| glue of rank 1, kernel the s-line | Z^504 + C3^233 + C9^77 + C27^38 |
| glue of rank 1, kernel the 1-line | Z^504 + C3^127 + C9^99 + C27^7 + C81^9 |
| other rank-2 glues (U*conj, 2U) | as actual (predicted: only the rank and c-type of the glue matter) |
| chi = 4 | Z^504 + C3^339 |
| chi = 10, 19 | Z^504 + C3^46 + C9^112 + C27^72 + C81^9 |
| chi = 16 | as actual |
| chi = 28 | Z^504 + C3^46 + C9^10 + C27^102 + C81^72 + C243^9 |
| pi = 1-3z, 4+3z (chi = 13), 1+6z (chi = 31) | as actual (same class) |
| pi = -2+3z (chi = 19), 4-3z (chi = 37) | Z^504 + C3^100 + C9^196 + C27^9 + C81^34 |
| pi = 1+9z, chi = 73 | Z^504 + C3^247 + C9^144 + C27^56 + C81^30 + C243^9 (the actual list, shifted by one) |
| pi = 4, chi = 16 | Z^504 + C3^113 + C9^91 + C27^18 + C81^52 |
| pi = 1-3z, chi = 7 | Z^504 + C3^339 |
| pi = 4+9z, chi = 7 | Z^504 + C3^120 + C9^111 + C27^13 + C81^30 |
| conjugation shifted by s on the cusps | as actual |
| cusp loops with +(Q -> -conj Q), signs (5,3) | Z^504 + C3^142 + C9^56 + C27^30 + C81^11 |
| D_0 signs (0,6) | Z^464 + C3^162 + C9^96 + C27^14 + C81^15 |
| D_0 signs (6,0) | Z^464 + C3^252 + C27^14 + C81^21 |
| D_0 signs (3,3) | Z^500 + C3^144 + C9^57 + C27^32 + C81^9 |
| D_0 signs (1,5) | Z^504 + C3^142 + C9^65 + C27^24 + C81^11 |
| rank-1 core (kernel the 1-line), D_0 signs (5,2), chi = 10 | Z^504 + C3^54 + C9^102 + C27^77 + C81^11 |

The closed polynomials of section 1 (`fable_formula.py`, no linear algebra) give the sign variants (4,2), (0,6),
(6,0), (3,3), (1,5) before the direct runs; they agree. The sign variants (0,6) to (1,5) are built as
V_1 (+) chi D_0 in a random basis, so they test the bookkeeping, not the splitting; the splitting is tested by the
cusp-model lines.

## 4. Lower degrees and the class-three step of E.23

The splitting is stable under the whole Galois image on V (G_{Q(zeta_3)} acts on W through O and on the cusp loops by
a scalar; c respects the glue), so every layer L_r(N) = Lie_r(V) splits the same way. Computed directly and by pieces
(`fable_step4_degree3.py`), for C_r(N) = L_r/(T_r - 1)L_r^{c=+}:
degree 1: Z^6 + C3^3; degree 2: Z^24 + C3^9 + C9^5;
degree 3: **Z^166 + C3^7 + C9^56 + C27^25 + C81^3** (rank 330; direct = formula), with pieces

| piece of L_3 | rank | (m+, m-) | Q+ | Q- |
|---|---|---|---|---|
| Lie_3 V_1 | 20 | (1, 0) | C3 + C27 + C81 | C3 + C9 + C27 |
| chi V_1 (x) V_1 | 16 | (d+, d-) = (2, 4) | C3 + C9 + C81 | C3 + C27^2 |
| chi^2 V_1 | 4 | (d+^2 + d-^2, 2 d+ d-) = (20, 16) | C9 | C27 |
| chi^3 = Z_3(3) | 1 | signs of Lie_3 D_0 = (34, 36) | C9 | 0 |

**What this says about the class-three step of E.23.** The layer L_3(N) is central in N/gamma_4 N, so the group that
holds the obstruction to lifting a class-two section, H^2(G, L_3(N)), and the group that moves the lifts,
H^1(G, L_3(N)), are sums over these four Galois modules with the multiplicities above: the class-three step has
coefficients in four modules of ranks 20, 16, 4 and 1 instead of one of rank 330, and 70 of the 330 dimensions are
the plain twist Z_3(3) with a sign. For the group unramified outside 3 the formula gives the exact coefficient group
above. The resonance moves with the degree: scalars act by u^{2r-m} on the part with m factors from W, so the weights
divisible by 9 are m = 2 in degree four and m = 0, 3 in degree three; at class three the resonant pieces are the pure
cusp part Z_3(3) (34 c-even lines, each C_9, since 7^3 = 1 mod 9) and Lie_3 V_1. The formula does not decide the image
of Sect(N/gamma_4) -> Sect(N/gamma_3): that needs the nonlinear obstruction class of each class-two section and the
ramified primes. It reduces the coefficient module and gives the torsion of the unramified part.

## 5. From memory, and what is open

From memory (not checked against a source here): gr of a free pro-3 group is the free Lie ring on V and
K_4 = [L_2, L_2] = Lambda^2(Lambda^2 V) (as in RESULT.md); the multigraded decomposition of Lie_3(A (+) B) and the
free Lie ring being a direct summand of the tensor ring (the code checks stability and the direct = formula
agreement); the reading of V as the 1-motive lattice of E minus E[3] glued by the Weil pairing (the computation only
uses that U is the symplectic form v a - u b); Gorenstein duality for B (its consequence is checked in step 5).

Open: (i) rows a and e of the table have no hand derivation (exact machine computation on ranks 15 and 24); the hand
derivation of rows b, c is a sketch. (ii) The validity class of the table is established on a grid of 36 values of pi,
not proved for all pi in the class. (iii) No closed expression in pi and chi for the six entries outside that class.
(iv) Degree four of the whole group N (L_4, rank 2475) and the marked quotient were not computed here.

## 6. Files (this folder)

`fable_e102_lib.py` (3-adic Smith form, functors, data), `fable_step1_direct.py` (direct E.102: 247, 144, 56, 30, 9),
`fable_step2_pieces.py` (splitting verified exactly; the six pieces), `fable_step3_tests.py` + `.out` (28 tests),
`fable_step4_degree3.py` (degrees 1-3), `fable_step5_ring_check.py` (ring description),
`fable_step6_table_scan.py` (validity class of the table), `fable_formula.py` (the closed formula).
Run with `python -I -B <file>` from this folder.
