# The actual sphere-quotient kernel with its full boundary retained

Cycle31 research. This is an exact new normal form of the marked P4 source, followed by its relative pro-two comparison. The canonical involution-marking problem is explicitly separated at the end. No affine or arbitrary-cocycle replacement is used.

## 1. Remove only the actual central full twist

Use the original standard P4 marking from A94:

    (a,b,c,d,e,f)=(A12,A13,A23,A14,A24,A34),
    Z=abc, P=def,  ZP=Delta4^2.

The actual inverse-base actions give [a,P]=[c,P]=1 and Ad(Z^-1)|F(d,e,f)=Ad(P). Hence the central generator ZP splits off: with

    G=P4/<Delta4^2>,

the original presentation becomes G=F(d,e,f) semidirect F(a,c), with exactly its six a/c action relations. Conversely G times an infinite central generator t recovers P4 by setting Z=tP^-1 and b=a^-1Zc^-1. These are inverse presentation maps. All assertions below concern G; no boundary P is killed.

The actual fifth sphere quotient is the retraction

    q:G -> F(d,f),
    a -> f, c -> d, e -> (fd)^-1,
    d -> d, f -> f.

Its section is the literal subgroup on d,f. Put

    A=a f^-1, C=c d^-1, P=def.

All three have trivial q-image.

## 2. The whole free-three kernel and exact actions

There is an exact inverse presentation

    G = F(P,A,C) semidirect F(d,f),                       (1)

where positive conjugation by the base generators is

    d: P -> C^-1 P C,
       A -> C^-1 P^-1 C P A,
       C -> C;

    f: P -> A^-1 P A,
       A -> A,
       C -> C P A^-1 P^-1 A.                            (2)

Here is a complete Tietze verification. Substitute

    a=A f, c=C d, e=d^-1 P f^-1

in the original six relations. The relations [a,f]=1 and [c,d]=1 give f(A)=A and d(C)=C. The two boundary relations [a,P]=[c,P]=1 give f(P)=A^-1PA and d(P)=C^-1PC. The remaining a relation is

    a^-1 d a=P f^-1 d f P^-1.

Using f(P)=A^-1PA, it is equivalent to [d,PA]=1, and hence to the displayed d(A). The remaining c relation is

    c^-1 f c=d^-1 P f P^-1 d,

equivalent to C^-1fC=P fP^-1 and hence to the displayed f(C). Each step is reversible.

The two endomorphisms in(2) are automorphisms, without relying on this presentation circularly. For d, use the free basis (P,C,R), R=PA. It conjugates P by C^-1 and fixes C,R; its inverse conjugates P by C. For f, use the free basis (P,A,S), S=CP. It conjugates P by A^-1 and fixes A,S; its inverse conjugates P by A. Thus the semidirect product on the right of(1) exists. The two displayed generator changes give inverse homomorphisms with the entire original presentation. Consequently ker(q) is literally the free rank-three group N=F(P,A,C), and P is a primitive, nontrivial kernel element.

It is useful to retain another free basis (P,R,S), with R=PA,S=CP. Both base actions preserve the conjugacy classes of P,R,S and the additional word S P^-1 R=C P A. In fact d fixes R and C, sends P and S to their C^-1 conjugates, and fixes C P A; f fixes S and A, sends P and R to their A^-1 conjugates, and fixes C P A. This verifies the four peripheral-looking word classes algebraically. Their identification with the actual geometric point-forgetting peripheral classes must still retain the chosen basepoint/marking; it is not inferred merely from this algebraic preservation.

## 3. Full completion and actual relative pro-two groups

All base actions in(2) are the identity on N_ab. First, N has its full induced profinite topology in G. Given a characteristic finite-index N0 in the finitely generated free N, the base action on N/N0 has finite image. Intersecting its kernel in F(d,f) with any prescribed finite-index base subgroup gives a finite semidirect quotient retaining N/N0. Characteristic finite-index N0 are cofinal. Hence

    Ghat = Nhat semidirect Fhat(d,f).                     (3)

Now choose any finite quotient Q of the actual base F(d,f), for example a specified odd dihedral quotient, and put H=ker(F(d,f)->Q). Let K=N semidirect H. The pro-two topology on N induced from K is its full pro-two topology. To see this, take a characteristic finite two-group quotient N/N0. Its base action is trivial on its Frattini quotient, because the action was trivial already on N_ab modulo2. The kernel of Aut(N/N0)->Aut((N/N0)/Phi(N/N0)) is a two-group: an automorphism trivial on the Frattini quotient has two-power order, by the usual finite p-group Frattini automorphism lemma. This particular standard lemma is the only additional dependency of this paragraph; its proof/source must be checked in full before promoting this relative statement beyond research.

Subject to that explicitly named elementary lemma, the H-action on N/N0 therefore has finite two-group image. Refining an arbitrary finite two-group quotient of H by its action kernel produces a finite two-group semidirect quotient of K retaining N/N0. Conversely every finite two-group quotient restricts to such quotients. The resulting inverse-limit maps give

    K^(2) = N^(2) semidirect H^(2).                      (4)

In particular O^2(K) meets N exactly in O^2(N). At the full profinite level let Hhat denote the open kernel of Fhat(d,f)->Q and Khat=Nhat semidirect Hhat. It has the same maximal pro-two quotient as K. Thus the ACTUAL relative quotient

    Ghat / O^2(Khat)

retains an embedded N^(2), and P remains a primitive, nontrivial element of that free pro-two kernel. Its quotient by N^(2) is the corresponding actual relative pro-two quotient of Fhat(d,f) over Q. No completion of an infinite abstract relation kernel has been identified with its closure.

## 4. What remains for the canonical alpha

For an actual full-GT involution the original operadic action and strand-forgetting compatibilities are established in A36/C28. To use(1) as a canonical-alpha model, one must identify THIS fifth sphere retraction with the corresponding geometric forgetting map, including its actual based transport, and then give the induced alpha on P,A,C. The automorphism of the original full source is not replaced by an arbitrary negative peripheral involution on N. In particular no preservation of a chosen finite head Q is assumed merely from its abstract isomorphism type.

The normal form retains exactly the boundary P that disappears in the invariant-free sphere lifts. It supplies a concrete finite-rank nonlinear kernel on which to carry out that marked comparison. It does not yet identify the canonical correction word in N^(2), prove its vanishing, or establish a_reg=d or Omega=1. Those gates remain open.

No producer, finite-head enumeration, private render, or central edit was used. The full presentation argument in Sections1--2 is unconditional. The explicitly indicated finite-group lemma and actual-alpha marking are the remaining dependencies of Sections3--4.
