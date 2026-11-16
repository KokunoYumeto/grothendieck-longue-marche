# Root audit of A.65 — PASS

The full candidate `notes/fgh_A65_draft.tex` was read after checkpoint 11.
The exact finite subgroup certificate was rerun successfully; its complete
output is `notes/root_A65_certificate_rerun.out`. DE independently read the
complete proof and sources and reran the certificate as well.

The noncentral order-p subgroup is the only remaining subgroup type:
its image in the two-dimensional commutator space is isotropic and it
intersects the center trivially. The proper quotient is an actual étale
degree-p quotient, with the stated genus and p cusps. The isogeny square
to E/T is genuinely equivariant and fixes the target map and removed set.

At an ordinary prime, the two Gaussian connected lines are distinct, so
one place makes every nontrivial subgroup translation nonzero in the
special fibre. The action is then free at every point, including nodes.
The quotient by the constant étale group scheme is an actual étale
torsor. It permutes the marked rational clusters freely, preserving
distinct companion cusps in their quotient.

At an inert prime, potential good reduction of the source Jacobian
passes through the actual surjective norm to the quotient Jacobian.
The resulting semistable quotient has tree dual graph. Resolving the
actual map by point blowups introduces only rational components; proper
surjectivity forces every positive-genus target component to be dominated
by an original positive-genus source component. The source elliptic main
is the only component with nonconstant image, and the other positive
components have constant images away from the origin. The radicial
factorization gives a unique origin point on the target main. The p
marked cusps therefore lie on a connected rational marked fibre. The
proof does not interchange a wild quotient with reduction and does not
invoke the Néron mapping property on a nonsmooth relative source.

The intrinsic exponent-p class-two formulation is justified by the
universal rank-two Heisenberg quotient, with p odd. The ordinary and
inert arguments exhaust all odd primes; p=3 is included. The full
nilpotent and universal covering assertions remain Open. Normalizer
recognition uses A.59 with its proved actual comparisons.

Fresh primary reads completed by root:

- Liu, Proposition 9.2.5 and Theorem 9.2.7, printed pp.396–397,
  exact blowup and indeterminacy statements and proof, browser
  `turn1038view1`; Lemma 7.5.18(b), pp.312–313, `turn1038view0`;
  Remark 10.4.24, p.542, `turn1035view1`.
  https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf
- Serre–Tate, *Good reduction of abelian varieties*, Theorem 1 and
  Corollary 2, p.493, exact statement and Tate-module proof in
  `turn1032view2`.
  https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf
- Silverman, V.3.1, p.145, `turn1030view0`, ordinary/supersingular
  alternatives for all prime-power torsion levels.
  https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf

No mathematical correction was needed in this audit. Integration as a
Proved statement was authorized after all these checks.
