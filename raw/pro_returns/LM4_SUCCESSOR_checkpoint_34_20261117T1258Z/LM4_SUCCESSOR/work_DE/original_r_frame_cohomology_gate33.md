# The actual r-frame as an exact C3-cohomology lifting condition

New checkpoint33 research only. All formal sources are unchanged. This is an exact residual condition and a limitation of a specified family of tests; it does not prove the remaining CM sign. No finite target was searched or executed.

## 1. Corrected domain and retained original marking

Let F be the actual full free profinite group on x,y, embedded as the S3 kernel in the original free profinite product C2(s) amalg C3(r). Let rho=Ad(r)|F, of order three, and let F' be the closed derived subgroup. Retain the exact original LM7_PUSH E61/E65 data bound in A105: Sigma=alpha c, Sigma(r)=phi^{-1}r=A_r r A_r^{-1}, and A_r is the unique normalized conjugator in F. Put q3:F->G=SL2(F3), using X=I+2E12 and Y=I-2E21; let C=J mod3=XYX^{-1} mod3, with integral J=[[0,-1],[1,-1]].

A preliminary conversation message used ker(q3) on all F. That scope is explicitly SUPERSEDED. The actual cyclic substitution rho cycles x,y,z, while Ad(C) cycles X,Y,-Z. Consequently q3 rho differs from Ad(C) q3 by a central sign character on F. In particular ker(q3) need not be rho-stable: q3(y^3)=I but q3 rho(y^3)=Z^3=-I. The argument below uses only the correctly typed closed subgroup

 K3' = ker(q3|F').

Every central character kills F', so q3 rho=Ad(C) q3 on F'. Therefore K3' is rho-stable. It is also a closed normal subgroup of F'. No full-topology or abstract completion assertion about a discrete derived subgroup is made.

The following exact inputs are printed and proved in A105. First A_r lies in F': from phi=rho(A_r)A_r^{-1} and phi in F', the abelian vector of A_r is fixed by the cyclic matrix. The determinant of rho-I on F_ab is3; Zhat is torsion-free, so that vector is zero. Second q3(F')=G'=Q8: the displayed quaternion generators and conjugation by X give G=Q8 semidirect C3 and its commutator subgroup Q8. Thus every element of Q8 has a lift in F'. Third, with nu from the exact original beta-frame coordinate,

 Phi=q3(phi)=Y^nu X^{-nu},
 a_+=X^nu C^{-nu},  a_-=-X^nu C^{-nu}

are the two possible finite images of A_r. They both lie in Q8 because the C3 abelianization sends X and C to1, and -I lies in Q8. They satisfy

 a C a^{-1}=Phi^{-1}C,
 equivalently a^{-1}Phi^{-1} C a C^{-1}=I.

These are actual marked inputs, not independently chosen finite parameters.

## 2. Two residual cocycles and the exact sign criterion

Set c=phi^{-1}. Since (Sigma(r))^3=1 in the original modular group,

 c rho(c) rho^2(c)=1.

For either a in {a_+,a_-}, choose any t in F' with q3(t)=a and define

 z_t = t^{-1} c rho(t).

The finite transporter equation and the rho-equivariance on F' give z_t in K3'. Expanding the three factors shows

 z_t rho(z_t) rho^2(z_t)
 = t^{-1} c rho(c) rho^2(c) t =1.

Thus z_t is a continuous C3-cocycle in the actual compact group K3'. If the lift is changed to tn with n in K3', then

 z_(tn)=n^{-1} z_t rho(n).

Its pointed cohomology class therefore depends only on the chosen finite frame a, not on its lift. Write this class as ob(a) in H1(C3,K3').

The exact equivalence is

 ob(a)=basepoint  if and only if  q3(A_r)=a.

Indeed triviality means that for some n in K3', z_(tn)=1. Then A=tn satisfies A^{-1}c rho(A)=1, or A r A^{-1}=c r. Conversely the actual A_r gives a lift with zero residual cocycle. Uniqueness in F is essential: two such A differ by an element centralizing r; the accepted finite-factor centralizer theorem gives C_(C2 amalg C3)(r)=C3(r), whose intersection with the S3 kernel F is trivial. Hence the resulting A is the actual normalized A_r. This proves both directions, with no substitution of an unnormalized frame.

Exactly one of ob(a_+),ob(a_-) is the basepoint. For a full-GT negative involution, A105 gives the actual unit residue d mod3 in {1,-1}. The desired original CM conclusion is precisely

 Delta(alpha)=0  if and only if  ob((d mod3) X^nu C^{-nu})=basepoint.

This recasts the still-open sign in a specified actual closed-kernel cohomology set. It does not decide it.

## 3. Uniform limitation for coprime-p transporter tests

Let p be any prime other than3. Let theta:K3'->P be ANY continuous surjective finite p-group quotient which is equivariant for the actual rho-action. Then every cocycle of C3 in P is a coboundary. In particular theta(z_t) has trivial cohomology class for BOTH finite candidate frames, independently of which is the actual one.

Here is a complete elementary proof, so no Schur--Zassenhaus citation is needed. Induct on |P|. If P is nontrivial, Z=Omega_1(Z(P)) is a nonzero characteristic elementary abelian central subgroup. It is rho-stable. Induction in P/Z lets us conjugate the cocycle so that its value lies in Z. In additive notation its norm is (1+rho+rho^2)z=0. Since3 is invertible in F_p, put

 b=(rho+2rho^2)z/3.

The identity (rho-1)(rho+2rho^2)=3-(1+rho+rho^2) gives (rho-1)b=z. Thus the remaining cocycle is a coboundary in Z, and hence in P. This proves the induction. The same conclusion for an actual continuous pro-p quotient follows from the finite-level statement and the finite-intersection property for the compact sets of conjugators; no abstract pro-p completion is identified.

Therefore this transporter equation, tested only through actual rho-equivariant finite p-quotients of K3' with p not equal to3, cannot distinguish the two finite frame signs. In particular relative-two refinements do not resolve this transporter-only condition. The conclusion does NOT prohibit a coupled target retaining the full pentagon or other original frame data, does NOT exclude relative-three tests, and does NOT say that the two actual compact cocycle classes agree. They do not agree, since exactly one is the basepoint.

## 4. Scope and provenance

The earlier all-F kernel proposal is preserved above as superseded, with its exact failure. The corrected derived-kernel argument was sent to root before this first saved version. The finite image and normalized-frame inputs are source-bound to work_DE/A105_original_CM_parity_proposed.tex and work_DE/original_CM_source_binding33.md. The internal centralizer input is the previously audited finite-factor Herfort--Ribes theorem used in A105; no new primary retrieval is claimed for this note. No formal statement, shared paper, or previous checkpoint bytes were changed.

Saved UTC: 2026-11-17T11:34:44.809935+00:00
