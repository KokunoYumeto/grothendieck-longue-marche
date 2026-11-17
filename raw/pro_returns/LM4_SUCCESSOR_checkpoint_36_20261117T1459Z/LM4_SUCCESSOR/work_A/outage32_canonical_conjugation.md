# Conjugation law for the canonical dihedral parameter and signed obstruction

Conversation-level direct derivation, fully checked by root and A; CE independent audit requested. Historical A45 source comparison remains deferred, so no claim of bibliographic novelty. No file, execution, formal promotion, or CM-frame identification.

## General normalized peripheral automorphism

Let gamma=(lambda,f) act by gamma(x)=x^lambda, gamma(y)=f^(-1)y^lambda f, with lambda in Zhat^times and f in Fhat', and suppose the original third peripheral z=(xy)^(-1) maps to a conjugate of z^lambda. On the full dihedral quotient D=Zhat_T semidirect C2_x, write f_D=T^s with s in 2 Zhat. Since lambda is odd, gamma_D fixes x and sends T to T^(1+2s). Original z conjugacy makes 1+2s=epsilon lambda for one GLOBAL sign epsilon in {+1,-1}. The left side is 1 modulo4; therefore
D_gamma:=1+2s=chi4(lambda)lambda,
where chi4(lambda)=+1 for lambda=1 modulo4 and -1 for lambda=-1 modulo4.
This already follows from the original peripheral data, without a canonical norm or involution assumption.

## Exact canonical conjugation law, without a surjectivity assumption

Let alpha be an actual normalized negative involution with parameter phi and unique Fhat' norm solution u=phi alpha(u). Put alpha'=gamma alpha gamma^(-1). The exact normalized parameter is
phi'=f gamma(phi) alpha'(f^(-1)).
For v=f gamma(u), compute
phi' alpha'(v)
=f gamma(phi) alpha'(f^(-1)) alpha'(f) gamma(alpha(u))
=f gamma(phi alpha(u))=v.
Thus v lies in Fhat' and solves the new norm. Uniqueness transfers under conjugation (fixed subgroups conjugate), so v is the unique Fhat' norm word. When alpha,gamma belong to GT0, it is their existing canonical u_alpha'. This does not assume the endomorphism psi_u is an automorphism.

Writing u_D=T^k and u'_D=T^(k'), we get
k'=s+D_gamma k,
d'=1+2k'=D_gamma(1+2k)=chi4(lambda)lambda d.
Consequently the unit status of d at every prime is invariant under such conjugation.

## Actual signed quotient for general gamma

Use the original X,Y in SL2(F3), J=diag(1,-1), j=AdJ. The triangle-translation proof from the signed-alpha theorem works with chi gamma=e chi, e=lambda modulo3 in {+1,-1}. It gives actual projective A4 kernel stability. The unique signed lift agrees on x,y because their actual images still have order3; a central sign would change that order to6. Thus gamma induces an actual beta_gamma on SL2(F3).

Since beta_gamma(X)=X^e, uniquely
beta_gamma=Inn(X^nu) j^delta,
delta=(1-e)/2, nu in F3.
Comparing its value on Y with f's actual conjugation and using q(f) in Q8 gives
q(f)=epsilon_gamma F_nu,
F_nu=Y^nu X^(-nu),
epsilon_gamma in {+1,-1}.
The centralizer used here is C_SL2(F3)(Y)=<Y,-I>; abelianization C3 forces the same exponent nu.

For two such normalized pairs, literal multiplication gives
F_nu beta_(e,nu)(F_mu)
=Y^nu X^(-nu) X^nu Y^(e mu) X^(-e mu) X^(-nu)
=F_(nu+e mu).
Thus the actual finite triples compose by
(e,nu,epsilon)(e',mu,epsilon')
=(ee',nu+e mu,epsilon epsilon').
In particular epsilon_gamma is a continuous character on this normalized-pair image, abstractly a subgroup of C2 times S3. This formula alone is not identified with the separate CM character.

## Original GT0 three-cycle determines this character

Let m=(lambda-1)/2 in Zhat and retain the ORIGINAL ordered f three-cycle word
f(x,y)x^m f(z,x)z^m f(y,z)y^m.
Let C=XYX^(-1). The cyclic signed discrepancy vanishes on f in Fhat', but Z^m contributes the ONE central factor (-1)^m relative to (-Z)^m. Hence
q(hex_f)=(-1)^m (q(f) X^m C^(-1))^3.
Since F_nu=U_(-nu), the previously proved exact trace is
tr(F_nu X^m C^(-1))=m-1=-e in F3.
The determinant-one cube is therefore e I. Multiplying by epsilon_gamma gives
q(hex_f)=(-1)^m epsilon_gamma e I.
The original GT0 three-cycle relation sets this to I. Since (-1)^m=chi4(lambda), it follows that
epsilon_gamma=chi4(lambda)e ALREADY FOR GT0.
No canonical-u pentagon, new canonical hexagon, or E61/E65 comparison has entered this step.

## Canonical signed conjugacy invariant

If beta_alpha=Inn X^mu j and q(u)=epsilon_u U_mu, conjugation gives
mu'=2nu+e mu.
The actual u'=f gamma(u) and the finite-pair law give
epsilon_u'=epsilon_gamma epsilon_u.
On the branch d modulo3 is nonzero,
q(H_d)=epsilon_u (d mod3) I.
Combining the exact transformations gives
epsilon_u'(d' mod3)
=epsilon_gamma chi4(lambda)e epsilon_u(d mod3)
=epsilon_u(d mod3)
for gamma in GT0.
Thus the actual scalar q(H_d) is invariant under GT0 conjugation. The 3-unit branch itself is conjugacy invariant. The character which could have changed the scalar is identically trivial on GT0 by its ORIGINAL three-cycle relation; it is not a new GT0 obstruction character.

This is a necessary conjugacy invariant relevant to Main A. It does not evaluate the canonical sign, prove all canonical d are units at GT0 scope, identify either CM-frame bit, or prove the canonical hexagon.
