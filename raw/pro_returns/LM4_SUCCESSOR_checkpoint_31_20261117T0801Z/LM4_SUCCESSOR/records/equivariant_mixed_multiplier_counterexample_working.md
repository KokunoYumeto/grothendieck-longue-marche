# An actual-source mixed-multiplier obstruction to equivariant central lifting

Research proof,16November2026; independently checked in read-only discussion
by the A,CE and root branches. This is not the multiplier-one or global
minus-one case required by the main involution construction.

Let F be the full free profinite group onx,y withz=(xy)^-1, letc invertx,y,
and set E0=F semidirect<c>, the full profinite free product of threeC2s.
Put R=R_nil(F). A34 proves [R,F]=R, hence [R,E0]=R. Thus the actual
source-central refinement E0/[R,E0] is E0/R itself.

Write F/R=product_p F^(p). On its2-factor use the canonicalc automorphism;
on every odd factor useidentity. These commute with the externalc,
so together withtheta(c)=c they define a genuine automorphismtheta of
E0/R. On the orientation subgroup it is peripheral with common unit
lambda2=-1 andlambda_p=1 foroddp. It fixesx,y up to their literallambda
powers and takesz to the conjugate ofz^lambda whose conjugator has
2-componentx^-1 and odd components1. Each named reflection class is
preserved, since inversion of its cusp generator is effected by an
orientation-subgroup conjugator in the2-factor. The kernel is an actual
source kernel, not a freely invented finite extension.

There is no full peripheral lift commuting withc, even if the lift
is allowed infinite order. SupposePhi(x)=a x^lambda a^-1 andPhi c=cPhi.
Then a^-1c(a) centralizesx, so it equalsx^t. In full abelianization
Zhat², -2abar=(t,0); thusabar=(r,0) andt=-2r. It follows that
c(a x^-r)=a x^-r. The actual full fixed group C_F(c) is trivial, by
the canonical three-reflection free-product centralizer, so a=x^r.
ConsequentlyPhi(x)=x^lambda. The same argument givesPhi(y)=y^lambda.

Butlambda≡7mod12. The actualS4 quotient fromA39 hasx=(234),y=(1234)
and is onto. In it x^7 y^7=(12), whereas(xy)^7=(1423). These elements
are not conjugate. Hence the third peripheral condition fails. The
existing code work_A/check_A39_mixedpower.py and its retained output
verify the entire24-element quotient and this class distinction.

This strengthens A18's failure of involutory mixed-sign lifting:
even dropping the involution requirement does not permit an equivariant
lift fixingc. It does not refute A3/R2, which do not promise this extra
equivariance. It does not decide the multiplier-one equivariant rule
or construct a full negative involution. The exact full centralizer
statement A6 gives the same no-lift conclusion, but theS4 computation
keeps the finite obstruction explicit.

A suggested further finite-base model in the read-only discussion has
N=ker(F→(Z/12)^2), with orientation class-two presentationx^24=y^24=1
and centralw=[x,y] oforder12, andexternalc inversion. The proposed
order13824 source-central group admitsx→x^7,y→y^7,c→c. This finite
presentation and its exact universal-source comparison have NOT yet
been independently enumerated or formally accepted; CE will check them
after checkpoint10. Do not cite that suggested model as a proved result.

## Post-checkpoint10 resolution of the finite-model question

The preceding paragraph records the exact pre-capture uncertainty. After
checkpoint10 the complete source-central presentation and all13824 normal
forms were independently checked. The model is now proved as A.70 in
work_CE/A70_A71.tex, with the finite certificate, genuine stdout and JSON
in work_CE/research_equivariant_R2/. The finite kernel is exactly
C2^2 times C12, of order48. The automorphism fixes that entire kernel.
Both the full source comparison and the S4 no-lift argument have been
read and accepted by the root, A and CE branches. The theorem still
has the mixed-multiplier scope stated above; it does not assert failure
for a single fixed action with multiplier one or global minus one.
