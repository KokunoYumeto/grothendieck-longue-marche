# Root review of the exact theta/principal-divisor bridge

Reviewed by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

The complete frozen note and program were read. The manifest is
`research_e120/ledger/a_theta_principal_distribution_manifest.json`, SHA-256
`c59f0dcd88e32fcc42422611050ecfe6dac5532ae6936b1d4615b769199f9e26`.
The note hash is
`04ec08d25bb50add080c2588faaea57c299a1470704429da2bfd27f8ca9577c4`;
the source hash is
`a2d2b4a262236559687ab7abcbf6b5bab8a47484b792549621124e24baed40b1`.

## Executed checks

`theta_distribution_replay.py` copied the frozen source and all four
immutable inputs into a fresh directory. It checked all five owned and
four input files before and after execution. The actual source execution
returned zero with empty stderr. The whole stdout, stderr and JSON agree
byte for byte with the author records. The replay audit has SHA-256
`cbdfcb84723983b16b952b353b6753dfeeb59ab14c87c086eea1ffa591ecdc65`.
The two helper entry-point executions are labelled precisely: the field
module is silent, and the Smith module's standalone invocation is its help
entry point. Their arithmetic is exercised by the imported certificate.

`theta_distribution_independent.py` imports no author code. It constructs
the coefficient field by polynomial remainders and Euclidean inverses, and
uses polynomial resultants to evaluate the products over the six nonzero
pi-kernel points. This is independent of the author's three-by-three
multiplication-matrix determinant routine. All 24 literal line-factor
norms, eight function norms, eight full tame products, and the complete
Smith/inverse maps agree. Its actual exit is zero and stderr is empty.
The complete independent JSON has SHA-256
`de0aef9e2ac7e0f4f6f763f923ddf74d2e84820869bf64335ebd115c7fbe7d14`.

## Divisors, tangent constants and actual transfer

Let phi=[pi]:E_source -> E_target, with pi=1+3zeta3. Both curves use
the retained Weierstrass and Fermat models and the tangent s=z/x at O.
The isogeny map already checked in the theta certificate has tangent
derivative pi. Its kernel consists of O and the six points whose
Weierstrass coordinates satisfy X³=27/pi, Y²=X³-27/4.

For each retained normalized function f, write its actual divisor as
sum r_t[t]. The product of theta(Q-t)^r_t has divisor
7 div(f)-phi* phi_* div(f). The right side f(Q)^7/(Norm_phi f)(phi Q)
has precisely this divisor, by the function-field norm. The quotient is
constant on the proper connected curve.

The original frame at O is one and theta has leading term
(-D/(9pi))s^6. Thus the tame value of {theta,f} at O is
(-D/(9pi))^r_O. At every other cusp it is theta(t)^r_t.
At each nonzero pi-kernel point it is f(T), because theta has a simple
pole there. Those lists exhaust the divisors. Their full product is one
by reciprocity, and the independent resultants verify the product for
each of the eight functions. Since theta is even, comparison of the
leading terms at O gives constant one in the function identity.

The isogeny fixes E[3], so Norm_phi f=c_f f. In the source parameter,
the leading term of the norm pulled back by phi is
c_f pi^r_O s^r_O. It is also the product of f(T), T nonzero in E[pi],
times s^r_O. Combining these exact expressions with reciprocity gives
c_f=(3D)^r_O product_(t!=O)theta(t)^(-r_t).
The resulting constants are 729, 1/729, 729, three copies of 9zeta3²,
and two copies of -27. These are checked as elements of Q(zeta3),
including their roots of unity.

## Symbol identity with all constant terms

Pullback is the function-field inclusion phi*:K(E_target)->K(E_source).
Transfer sends K2(K(E_source)) to K2(K(E_target)); both fields are
identified with the retained literal K(E) only after fixing phi.
Apply the function identity to g, take its symbol with f, and transfer.
The projection formula sends {f,phi*(Norm_phi g)} to
{Norm_phi f,Norm_phi g}. Expanding the two complete norms gives

    (7 Norm_phi-1){f,g}
      = Norm_phi sum_t r_t(g){f,theta(Q-t)}
        + {c_f,c_g} + {f,c_g} + {c_f,g}.

This derivation checks the direction and all three signs. It takes place
in the actual function-field K2 group, so each retained tame-corrected
linear combination carries its displayed constant corrections through
the same homomorphism.

On the proper dual coefficient, the pullback is A_E^T and the transfer
is 7A_E^-T. Both compositions are 7I. Hence the left operator is
49A_E^-T-I=[[-15,-21],[21,6]], with determinant 351. Its integral
determinantal divisors give Smith factors 3 and 117. The literal local
change-of-basis matrices in the certificate, with denominators prime to
three, give diag(3,9). Their four inverse products and the rational
inverse (1/117)[[2,7],[-7,-5]] were checked independently. The integral
image therefore has index 27 over Z3, and its quotient is C3 plus C9.

The ordinary-point test also replays in the literal field
Q(zeta3,v), v²=-23/4, using the actual addition and Velu maps. Its role
is to check the retained formulas. The proof of the full function
identity is the divisor and tangent-constant argument above.

## Outcome

The exact distribution, norm constants, K2 transfer identity and typed
proper coefficient operator pass proof review, full fresh replay and
independent resultant/matrix checks. The intrinsic handle coefficient
still requires the actual integral logarithm-torsor evaluation of the
translated theta symbols. The recorded operator and its finite cokernel
remain part of that calculation.
