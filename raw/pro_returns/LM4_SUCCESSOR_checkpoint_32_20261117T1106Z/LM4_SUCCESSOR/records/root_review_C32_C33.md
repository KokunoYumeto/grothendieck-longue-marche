# Independent root review of C.32 and C.33

Date: 16 November 2026, fourth research hour. Status: accepted after reading the complete formal proofs and independently deriving the critical identity. This review is part of the AI-produced work and claims no external referee authority or priority.

## C.32: the actual relative completion

The group is the quotient of the full completion of B_n by the kernel of its full pure subgroup onto P_n^(p). It retains the entire finite quotient S_n. It is neither the maximal pro-p quotient of B_n nor an unspecified induced completion.

In the split Fadell–Neuwirth sequence, the pure braid action on the free kernel is trivial on its abelianization. For each characteristic finite p-group quotient of that kernel, its induced automorphisms lie in the p-group kernel of the automorphism action on the Frattini quotient. The resulting finite p semidirect products give the full induced pro-p topology. The completed split sequence is therefore exact. The cohomology induction uses all finite p-primary modules with continuous pro-p action, not just the trivial module. The free kernel has finite cohomology in each degree and zero cohomology above degree one. Its comparison is natural for the base action, so the finite cohomology modules used by Hochschild–Serre extend continuously to the completed base.

For the preimage G of a Sylow p subgroup of S_n, P_n has p-power index. Intersecting the finite set of G-conjugates of a normal p-index subgroup of P_n supplies the full induced pro-p topology. The resulting completed extension is exact and its finite quotient is a p-group. Hochschild–Serre therefore gives the same p-goodness for G. Its actual configuration-space covering has finite-dimensional contractible universal cover. Thus cd_p(G^(p)) is finite, so G^(p) has no element of order p. This is an actual cohomological-dimension argument; virtual finite dimension alone would not suffice.

The pro-p completion of the labelled PaB groupoid retains its objects, and the free S_n label-orbit quotient recovers precisely the relative braid completion. The elementary braiding is sent to the original braiding followed by a pro-p power of its pure double. Consequently permutations remain fixed, including at an odd prime when the parameter is zero. The ribbon presentation gives the same exact full-twist identity as in C.31. The p-strand rotation then creates a nontrivial element of order p if the parameter is p-divisible, contradicting the preceding actual Sylow comparison. No surjectivity of the proposed endomorphism was used.

## C.33: independent affine calculation

Use [x,y]=xyx^-1y^-1. The universal integral affine module sends the commutator to

    w0=(1-b)e1+(a-1)e2.

The closed normal generation of the free pro-p commutator group by [x,y] gives a unique integral coefficient F(a,b) multiplying w0. The module of such multiples is compact and closed; uniqueness uses the integral power-series domain. Duality makes F symmetric. One can also obtain the divisibility directly from the relation (a-1)A+(b-1)B=0 for the two translation coefficients; no assertion about arbitrary closed subgroups is needed.

Set a=1+T, x=(a,T), y=(a^-1,0), z=(1,-T), and m=(mu-1)/2. Write U=F(a,a^-1), V=F(1,a), W=F(a^-1,1). Independent multiplication of the six hexagon factors, followed by division of the translation by T a^m, gives

    T a^(-m-1)U+(1-a^-m)/T+T V+(T/a)W-m=0.

After a is replaced by a^-1, the two axis terms cancel on addition. Multiplication by T a^m gives exactly

    (a^mu-1)(1-T^2 U/a)=mu T a^m.

For mu nonzero this is the identity used by C.33. Its comparison with the prounipotent image is coefficientwise: at every finite degree the Magnus coefficients and the logarithmic substitution are continuous for the p-adic coefficient topology. The chosen affine matrices are congruent to the identity modulo T, so their logarithms are well-defined in the T-adically nilpotent matrix quotients. There is no assumption that a general quadratic exponent has an integral binomial series in all degrees.

Put R=1-T^2 U/a and H=(a^mu-1)/(mu T). Then R is integral with constant one and R H=a^m. The coefficients of H through degree p-2 have denominators dividing (p-1)!, and the degree p-1 coefficient of a^m has denominator (p-1)!. They are integral because mu and m are integral over Z_p. The product recurrence forces the coefficient

    product_(j=1)^(p-1)(mu-j)/p!

to be integral too. Hence mu^(p-1)-1 belongs to p O_E. Since mu^2=D belongs to Z_p, this implies D^((p-1)/2)=1 modulo p. Thus D is a nonzero quadratic residue and has a unit square root in Z_p. The intersection p O_E with Q_p is exactly p Z_p, so the argument also covers a ramified quadratic extension. Reduction modulo its maximal ideal gives an alternative proof of the same nonzero-square conclusion.

The case D=0 cannot be obtained by taking a limit while keeping f fixed: the added affine equation then degenerates. C.32 supplies the separate exclusion. The cases p=2 and p=3 already follow from D=1+24c2(f) and their elementary unit-square criteria. For the resulting integral roots, the injective pro-p-to-prounipotent comparison brings the hexagons back to the actual free pro-p group.

The exact symbolic verification is in `code/check_metabelian_hexagon_identity.py`, with actual standard output beside it. It verifies the six-factor affine product, the inverse-specialization identity, the first-denominator polynomial modulo seven primes, and the quadratic sign at mu=3. These calculations support the displayed proof; they do not stand in for the general coefficient argument.

## Scope retained

For a full GT involution, A.37's canonical word therefore gives its prescribed peripheral conjugator at every maximal pro-p quotient, and its parameter D has a full unit square root in Zhat. This does not provide the full profinite hexagon for any chosen global root, does not treat all relative characteristic levels, and does not decide full involution conjugacy. The specified-root S4 counterexample in C.34 reinforces this distinction. Its failure does not refute the existential choice of a root.
