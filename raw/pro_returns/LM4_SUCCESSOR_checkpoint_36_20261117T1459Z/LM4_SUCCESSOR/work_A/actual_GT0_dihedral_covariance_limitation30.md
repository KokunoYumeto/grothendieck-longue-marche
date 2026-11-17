# The actual dihedral covariance gives no additional one-cover equation

Cycle30. This preserves the complete read-only deduction made during checkpoint29 capture. All frozen29 files remain unchanged. The data are the actual negative GT0 involution of A87, not arbitrary module parameters.

## 1. The literal cusp-preserving reflection

Retain B=C2(s) amalg C3(r), delta=sr, x=delta^-2, y=sxs, z=(xy)^-1, the actual alpha, v=u^-1s and tau=v alpha. Let d=d_alpha, m=(d-1)/2, T_d=v delta^d and Xi_d=T_d^3. A87 supplies

    tau(T_d)=T_d^-1,    Xi_d in F',    tau(Xi_d)=Xi_d^-1.

Since Xi_d commutes with T_d, the product T_d^-1 tau also reverses Xi_d. Its literal semidirect-product expression is

    T_d^-1 tau=delta^-d v v alpha=delta^-d alpha.

Thus sigma_d=Ad(delta^-d) alpha sends Xi_d to Xi_d^-1. As delta^-d=x^m delta^-1,

    sigma_d=Inn(x^m) sigma_1,
    sigma_1=Ad(delta^-1) alpha.

The original-marking calculation of A87 is

    sigma_1(x)=x^-1,
    sigma_1(y)=j_delta(f)^-1 x y j_delta(f),
    j_delta=Ad(delta^-1).

Consequently sigma_d preserves K_x=closed normal closure of x and induces the identity on its retained procyclic y quotient. The actual d is odd; this is essential for the retained-head assertion. A45 further gives m even, so

    sigma_d=Ad(x^(m/2)) sigma_1 Ad(x^(-m/2)).

This is an equality of the existing full automorphisms, not the construction of a prospective positive cusp map.

## 2. Its action on the entire integral cover abelianization

Put M_x=K_x/closed[K_x,K_x]. No freeness assertion about this compact module is needed. Its topological generators are the classes of y^lambda x y^-lambda, lambda in Zhat: the quotient F/K_x has its literal y section, and conjugation by the K_x factor is trivial on M_x.

The image sigma_d(y^lambda) has the same retained head y^lambda. Hence

    [sigma_d(y^lambda x y^-lambda)]
      =-[y^lambda x y^-lambda] in M_x.

Continuity and topological generation prove that sigma_d acts as -Id on the WHOLE M_x. Inner conjugation by x^m also acts trivially, as the earlier formula predicts. The same statement holds on every invariant abelian coefficient quotient. In characteristic two this action is the identity.

Therefore sigma_d(Xi_d)=Xi_d^-1 becomes exactly -[Xi_d]=-[Xi_d]. The complete hexagon word is H_d=u Xi_d^-1 u^-1, so its integral cover class is -[Xi_d], and its mod-two class R_d equals [Xi_d]. The reversal/cube identities alone supply only R_d=R_d. They do not supply the separate weighted symmetry

    bar(R_d)=T^d R_d

required by A89/A90.

## 3. The simultaneous three-cover description

For i=x,y,z let K_i be the actual closed normal peripheral kernel and M_i its compact abelianization. Conjugation by delta fixes K_x and exchanges K_y,K_z; conjugation by v exchanges K_x,K_y and fixes K_z. Since d is odd, t=Ad(T_d) cyclically permutes K_x,K_y,K_z in that order. The actual alpha preserves every peripheral normal subgroup, so tau exchanges K_x,K_y and fixes K_z.

On M=M_x direct-sum M_y direct-sum M_z, these are continuous automorphisms. The cube t^3=Ad(Xi_d) is identity on every summand: Xi_d lies in F', hence in every K_i, and inner K_i conjugation is trivial on M_i. Together with tau^2=1 and tau t tau=t^-1 they give the actual dihedral/S3 module action. The stabilizer reflection t^-1 tau on M_x is precisely the -Id action proved above.

Let i_x denote the inclusion of M_x in the direct sum. The map

    a -> i_x(a)+t i_x(a)+t^2 i_x(a)

is a continuous isomorphism from M_x onto

    {w in M : t(w)=w and tau(w)=-w}.

Indeed t cycles the three summands, so every t-fixed vector is determined uniquely by its x component. The stabilizer formula gives tau i_x(a)=-t i_x(a); using tau t^j=t^-j tau shows that tau negates the displayed sum. Its inverse is the x-coordinate projection.

Thus the actual dihedral covariance conditions, considered on the complete three-cover abelianization, allow every x-coordinate. This is a statement about the actual operators, not a generic ring counterexample.

## 4. Exact remaining scope

The actual common-word map F' -> M sends Xi_d to a vector of the displayed type. We do NOT claim that every vector of that type comes from one full word, still less from the cube defect of a canonical GT0 word. Common-word, full pentagon and marked relative-lifting compatibility remain genuine constraints.

For arbitrary GT0 data this calculation does not add an odd-head identity to A89. For full-GT data A89's dyadic comparison remains proved, while A90's actual all-odd-head test remains open. The nonlinear Xi_d/Omega_alpha gate remains separate. No finite-head enumeration, new quotient target, or external recognition theorem is used.
