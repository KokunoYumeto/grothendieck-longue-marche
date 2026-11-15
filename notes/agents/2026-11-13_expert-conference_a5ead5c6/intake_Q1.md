# Floor question from the intake agent (round 2)

**Can an index category show the F.21 profile?**

Statement to prove or refute. Let `A` be a small category with common successors and finite hom-sets. If
`colim_A` is exact on `F_p`-vector space diagrams for every prime `p`, then it is exact on `Q`-vector space diagrams.

Equivalent forms.
- (Dual, by `lim^n_{A^op} Hom(M, R/Z) = Hom(T_n^A(M), R/Z)`.) If `lim¹_{A^op}` vanishes on every diagram of profinite
  abelian groups, it vanishes on every diagram of compact abelian groups.
- (Equalizers.) If a finite parallel family `a_0, …, a_k: p → q` has an `F_p`-affine equalizer for every `p`, it has
  a rational one. A counterexample needs objects `r_n` and integral `t_n ∈ Z[A(q, r_n)]` with
  `t_n(a_i − a_0) ∈ N_n Z[A(p, r_n)]`, `aug t_n ≡ 1 mod N_n`, `N_n` divisible by every prime eventually, and no
  `t ≠ 0` at any object with `t(a_i − a_0) = 0`, `aug t ≠ 0`.

Why it matters. With TOTAL_EXACT_2 A.2 it decides whether "exact on finite coefficients" is exactness. A
counterexample would be LM8 F.21 (zero at every finite coefficient level, non-zero integrally) realized by the
shape of an index instead of a non-compact coefficient group.

Known. `FI` shows the converse fails (`Q`-exact, `F_p`-exact for no `p`). Groups give no information (both sides
force the trivial group). `C_δ` fails both sides.

Belongs in: FRAISSE_EXACT (next Dérivateurs prompt).
