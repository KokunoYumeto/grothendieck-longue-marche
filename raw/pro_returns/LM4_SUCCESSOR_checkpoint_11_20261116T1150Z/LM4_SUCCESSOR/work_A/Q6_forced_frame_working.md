# A forced CM frame over the actual Q6 odd relative head

Status: research after the sixth-hour formal freeze. Exact certificate passes through an actual affine quotient, including its negative square and equivariant s-normalizer. Independent mathematical review is pending. The actual central refinement has NOT been constructed; therefore membership of this quotient automorphism in the image of full GT0 is NOT asserted.

## 1. The head is an actual relative quotient

Let Q6=S3 times A4, with generators

    s=((01),(01)(23)), r=((012),(012)).

Let K6 be the kernel of Pi->Q6. The Bass--Serre quotient graph has72 edges,36 C2-vertices and24 C3-vertices, so K6 is free of rank13. Put

    H=Pi/(K6' K6^7), N=K6/(K6' K6^7)=F7^13.

The graph chain model makes this an exact, not merely proposed, finite head. Label edges by g in Q6, with boundary B_(g<C3>)-A_(g<C2>). N is the13-dimensional kernel of that boundary map. The actual crossed homomorphism into edge chains has s-value0 and r-value e1-e_r. A splitting of the odd extension is obtained by a chain b with boundary A_base minus the uniform average of A-vertices. Average b under s and c (order4, invertible mod7) to make the splitting s- and c-invariant. Then s is pure and the r-vector in the chosen cycle basis is

    (3,4,6,0,5,4,3,6,1,2,6,5,3).

The actual tau^6 vector is the second basis vector. Its nonzero value ensures this head retains genuine cusp data. The congruence-kernel image is N: the head is solvable, a solvable congruence quotient has no7-factor, and its quotient Q6 is congruence. Thus H is a quotient of the initial relative-pronilpotent base C, and the retained h_C acts identically on H.

The c action on Q6 is identity on S3 and conjugation by (23) on A4. On the graph it sends edge g to edge kappa(g)s. It fixes the A-base vertex, gives the actual c action on cycles, and has square1.

The retained CM s-frame has Q6 image beta0=(1,s_A4), whereas the s-generator is (s_S3,s_A4). Its actual H-image can have an N^s translation above beta0. Sections2--5 first calculate with a pure intermediate head frame. Section6 below handles EVERY permissible translation while returning to the original literal C-frame, keeping the base automorphism and all its earlier data fixed. No adjustment of the final retained C-frame is assumed. The r-frame has identity head image in this odd relative component.

## 2. A c-stable module on which the forced frame acts nontrivially

The certificate constructs the covector

    lambda=(1,0,0,6,0,0,0,0,0,6,0,0,1)

on N. It is fixed by s and c. Its Q6 stabilizer is exactly<s>, but beta moves it. Let k=F8 with primitive seventh root zeta. Induce the linear N-character zeta^lambda, extended trivially over<s>, to H. The result V has dimension36 overk. Its distinct N-weight lines form one Q6 orbit, hence it is irreducible overk. No nontrivial Frobenius scalar2 or4 carries lambda into its head orbit; the underlying108-dimensional F2 module is therefore irreducible with endomorphism fieldk. The dual character does lie in the head orbit, so V is self-dual; this fact matters at the unresolved central refinement.

On the36 cosets Q6/<s>, the head acts by permutations and N acts diagonally. The c action is the literal coset permutation g<s> -> kappa(g)<s>. The actual r includes the normalized N-vector above. All module relations are checked exactly.

The relevant k-dimensions are

    dim H1(Pi,V)=8,
    dim H1(<s>,V)=4,
    dim H1(<tau>,V)=4.

Normalize every cocycle to have r-value0. Its s-value lies in ker(1+s), modulo (1+s)V^r. The certificate constructs eight explicit representatives. The combined restriction map

    RES:H1(Pi,V) -> H1(<s>,V) direct-sum H1(<tau>,V)

has exact rank8 and is an isomorphism. On the first boundary space beta-1 has rank2; c-1 has rank1. On the cusp boundary space c acts identically. These are genuine forced-frame effects, unlike a solvable C6 head where the frame image can be trivial.

## 3. The universal affine quotient

Let E=H1(Pi,V), and put A=V tensor_k E^vee, of dimension288 overk. Choose the eight normalized cocycles as coordinates of a universal cocycle d:Pi->A. The actual initial C has H1(C,V)=0, because its normal pro-odd subgroup acts without invariants. Therefore the eight restricted homomorphisms on R are independent. Irreducibility and End_C(V)=k imply d(R)=A. Hence the map

    Pi -> A semidirect C, g -> (d(g),g_C)

is surjective. Its quotient D=A:C is an actual Pi quotient with finite elementary-two residual image. The chosen coordinates satisfy d(r)=0 and d(tau)=d(s).

The positive coefficient action is forced uniquely by RES: on s-cohomology it is beta and on cusp cohomology it is identity. Write its E-matrix as L_E; the corresponding action L on A is its transpose on the multiplicity factor. Write C_E for the cohomology action of c (including the coefficient c-action gamma on V). The actual c coefficient action on A is Gamma=gamma tensor C_E^transpose. The negative coefficient action B=L Gamma has square1, verified both from the boundary map and by exact matrices.

The actual c automorphism of D has the form

    c_D=Inn(w_c) (Gamma,c_C).

Its inner term w_c is determined uniquely by its values on the actual s and r generators. The certificate solves those linear equations and checks w_c+Gamma(w_c)=0, as required by c_D^2=1. Thus it is not replacing the actual c action with an arbitrary linear involution.

## 4. The actual negative norm and the cusp constraint

A positive automorphism over h_C with the forced coefficient action has form

    Phi=Inn(w) (L,h_C).

It fixes the actual cusp precisely when

    (L-1)d(tau)+(1-tau)w=0.

The s-frame equation is solvable because L_E induces beta on H1(<s>,V); the r-frame equation is solvable because its order3 is coprime to the characteristic. The negative companion b=Phi c_D has coefficient action B, base action b_C, and affine inner term

    q=w+L w_c.

Its square is Inn(q+Bq). The initial cusp-normalized choice has NONZERO q+Bq. The allowed cusp-preserving corrections form A^tau, of dimension32 overk. The norm map1+B on that subspace has rank4; adjoining the actual obstruction vector keeps rank4. The exact solver therefore produces a correction with

    q+Bq=0,

while the cusp stays fixed under Phi. This is an actual affine quotient automorphism with involutory negative companion, not just a cohomology-level matrix.

## 5. The stronger equivariant literal frames

Actual b^2=1 is insufficient for full framed continuation. The associated s-normalizer must itself be an involution with its prescribed base image. Let beta also denote its action on A. An element with base beta_C^{-1}b_C has the form (a,beta_C^{-1})b. Its centralizing and square equations are

    (1+s)a=d(s)+beta B d(s)+beta(1+s)q,
    (1+beta B)a=(1+beta)q.

The first equation is solvable by the peripheral frame condition. Its remaining corrections form A^s, of dimension160 overk. The second norm map has rank68, and the augmented rank with the actual obstruction is also68. The certificate produces a simultaneous solution. Thus an actual C2 times C2 s-normalizer with the forced base frame exists at D.

The r-normalizer is simpler because d(r)=0. Its prescribed base image has head s and is the retained involution inverting r. The affine choice a=s q centralizes the required relation and has square

    (1+sB)(s q)+(1+s)q=(1+B)q=0.

It therefore gives the retained S3 r-normalizer as well. No nontrivial square is concealed in either literal frame.

## 6. Every already retained odd translation is handled

Let beta_C be the already retained, fixed literal s-frame of the base b_C. Write its head image as beta_H=(n,beta0). Since it centralizes the pure s, n lies in N^s. Since its associated s-normalizer beta_C^{-1}b_C is involutory, the head norm condition is

    n+beta0 c(n)=0.

Put t=beta0 n/2 in N^s. The odd division is legitimate and gives

    (beta0-c)t=n.

The exact graph certificate checks this on the entire allowed translation space, by a basis calculation, rather than only on a chosen translation.

Lift t to an element k_C in C_C(s) with congruence image1. Such a lift exists: the joint H/congruence image is the full fiber product over Q6, because the congruence-kernel image is N. The pair(t,1) centralizes s there. On the relative-seven component the remaining kernel is pro-seven, so coprime centralizer surjectivity lifts it; use identity on the other relative components. This construction takes place in the already retained C and does not change h_C or b_C.

Define an INTERMEDIATE frame

    beta_C^0=b_C(k_C) beta_C k_C^{-1}.

It is another equivariant s-frame for the same b_C: k_C centralizes s, and direct multiplication gives beta_C^0 b_C(beta_C^0)=1. Its H-image is pure beta0, because its translation is c(t)+n-beta0 t=0. Thus the pure-frame computation above constructs an actual b0 on D over b_C, with this intermediate frame. All other base action/frame data are as before.

Now construct a positive automorphism g_D of D over identity_C, fixing the cusp and having s-frame k_C. This needs no norm condition. The RES isomorphism defines its coefficient action uniquely: rho(t) on H1(<s>,V) and identity on cusp cohomology. Since t centralizes s, the first action is well defined and invertible. The cusp equation has a solution because its quotient condition is exactly the chosen identity action; the s-frame equation has a solution because its quotient condition is exactly rho(t); the r-frame has base1 and is solved as before. These are the same elementary linear peripheral equations used in Section4, with identity_C in place of h_C.

Conjugate the pure-frame construction:

    b=g_D b0 g_D^{-1}.

It has the ORIGINAL base b_C, because g_D is identity on C. It is involutory and inverts the actual cusp, because g_D fixes that cusp. If g_D(s)=k s k^{-1}, the transported s-frame has base

    b_C(k_C)^{-1} beta_C^0 k_C=beta_C.

More explicitly, if d_s^0 is the involutory s-normalizer of b0, then k^{-1} g_D(d_s^0) k is an involutory s-normalizer of b with base beta_C^{-1}b_C. Thus the final literal s-frame is precisely the originally retained one, not merely an element with the same Q6 image. The r-frame transport has base1 for g_D and hence returns to the original prescribed r-normalizer as well. All full C action/frame data are retained literally.

This conjugation argument treats every permissible n. It is not a restart of the existential frame choice, and it does not claim a full Pi or GT0 lift of g_D or b.

## Remaining issue

The central refinement Pi/[W,Pi] and, if needed, its second scalar step have not been constructed. A53 bounds them but does not furnish their automorphisms. V is self-dual, so invariant commutator forms do not vanish automatically. In particular D's framed automorphism has NOT been shown to lie in the actual image of full GT0; A3 cannot yet be applied. The computation shows that the first forced CM frame produces a nonzero affine square which can be canceled, and that its s-normalizer obstruction also cancels. The central layer is the next genuine test.

Certificate: check_Q6_forced_frame.py and check_Q6_forced_frame.out. All arithmetic is exact in F7 andF8. No enumeration of the enormous group H or D is used.
