# The actual canonical involution on the retained sphere kernel

Cycle31 research. This continues the complete marked normal form in `actual_sphere_kernel_relative_two31.md`. It retains the original full-GT involution and its entire inner correction. The auxiliary reflection below is an inner **twist**, not an assumed conjugate of the original involution.

## 1. Actual four kernel peripheral words

Use

    G=P4/<Delta4^2>=N semidirect B,
    N=F(P,A,C), B=F(d,f),
    P=def, A=af^-1, C=cd^-1,
    R=PA, S=CP, L=CPA=S P^-1 R.

The exact original relations give

    P^-1=abc,
    R=ade,
    S=cef,
    L^-1=f b d=f(bdf)f^-1.                              (1)

For R use [a,P]=[a,f]=1. For S use its definition. For L use [c,d]=1 and b^-1=cPa, which follows from b=a^-1P^-1c^-1 after removing only Delta4^2. Thus the four words (S,P^-1,R,L^-1) have product1 and are the four marked triple-full-twist classes complementary to the four finite labels. The bases (P,R,S) and (L,A,C) are both free bases of N, by the displayed inverse substitutions.

The action table of the preceding note shows that B preserves every one of these four N-conjugacy classes and fixes L literally. Indeed d fixes R and C, conjugates P and S by C^-1, and fixes L; f fixes S and A, conjugates P and R by A^-1, and fixes L.

## 2. Why the ORIGINAL full-GT action preserves this kernel

Let alpha be the actual multiplier-minus-one involution in full GT, acting in the original based four-strand parenthesized braid group. The action on Delta4^2 is inversion, so it descends to Ghat. The complete actual operadic cabling/peripheral argument of A36 and C28 says that every labelled triple full twist is sent to a conjugate of its inverse. The same holds for every pair twist. This is the established genuine full-GT operad action; nothing here supplies a four-strand action for a general GT0 element.

Equation(1) consequently sends the normal closure of P,R,S into itself. The inverse automorphism gives equality. But that closed normal closure is precisely Nhat by the inverse presentation, since killing P,R,S kills A,C and leaves the actual Bhat section. Thus alpha preserves Nhat and induces an involution alpha0 of Bhat=Ghat/Nhat.

On the original pair-twist images d,f, alpha0 preserves the respective conjugacy classes with exponent-1. The third pair twist b has image (df)^-1, so alpha0 also sends df to a conjugate of (df)^-1. In particular alpha0 is an actual negative peripheral involution of the quotient pants group and acts as -I on its abelianization. No GT0 normalization or arbitrary choice of alpha0 is inserted.

For every kernel peripheral in(1), an ambient conjugator can be replaced by one in Nhat: write it as n b and use the explicitly verified B-action on that N-conjugacy class. In particular alpha(L) is Nhat-conjugate to L^-1. The induced action on Nhat_ab is -I, because (P,R,S) is a free basis and each is inverted up to Nhat-conjugacy.

The only geometric input in this step is the actual labelled cabling/full-twist powering already proved and used in A36/C28. The identities(1) ensure that it is being applied to the specified original words, not an arbitrary new puncture marking.

## 3. A canonical full correction and an exact invariant section

Since B fixes L literally, and L is primitive in N,

    C_Ghat(L)=Zhat(L) times Bhat.                        (2)

Indeed an element n b centralizes L exactly when n does, and the full centralizer of the primitive free factor L in Nhat is Zhat(L). The two factors in(2) intersect trivially and commute.

Choose h in Nhat satisfying

    alpha(L)=h^-1 L^-1 h.                               (3)

Two such h differ on the left by a unique power of L. In the free basis (L,A,C), exactly one has zero L-coordinate in its abelianization. Denote that actual full word by h0. This fixes the entire transporter, rather than only its image in a module.

Put beta=Inn(h0) alpha. It sends L to L^-1 and preserves Nhat. Since alpha²=1, beta²=Inn(h0 alpha(h0)); the inner head lies in Nhat and centralizes L, hence is a power of L. It is fixed by beta: direct substitution gives beta(h0 alpha(h0))=h0 alpha(h0). But beta inverts L. Therefore this power is equal to its inverse, and torsion-freeness of Zhat(L) gives

    h0 alpha(h0)=1, beta²=1.                            (4)

Thus beta is a genuine involution, but(4) does not assert that h0 is an alpha-coboundary. No conjugacy of alpha and beta is assumed.

The automorphism beta preserves the centralizer(2) and induces the same alpha0 on its quotient Bhat. Consequently, for b in Bhat,

    beta(b)=L^chi(b) alpha0(b)

with a continuous homomorphism chi:Bhat->Zhat, since L is central in(2). Applying beta twice gives chi(alpha0(b))=chi(b). But alpha0 acts as -I on Bhat_ab, so chi(alpha0(b))=-chi(b). Cancellation of2 in Zhat proves chi=0. Hence the ACTUAL specified section is invariant:

    beta|Bhat=alpha0,
    beta(n b)=beta_N(n) alpha0(b),
    alpha(b)=h0^-1 alpha0(b) h0.                        (5)

In particular both base generators have the SAME actual full correction h0. Erasing that word and substituting beta for alpha would discard the canonical data; equation(5) is the retained comparison.

## 4. Every actual odd-dihedral relative pro-two head

For odd n let H_n be the kernel of the specified base map

    Bhat -> D_(2n), d -> D0, f -> F0,
    D0²=F0²=(D0F0)^n=1.

This kernel is invariant under alpha0. Indeed its closed normal defining relators d²,f²,(df)^n go to conjugates of their inverses by the exact negative peripheral property. Put K_n=Nhat semidirect H_n. Then K_n is invariant under beta and under alpha, because their difference is the inner twist by h0 in Nhat. Its characteristic pro-two residual O²(K_n) is likewise invariant.

The complete IA/Frattini argument of the preceding note proves that the quotient

    Ghat/O²(K_n)

retains an embedded free pro-two N^(2) with primitive boundary P. It is a split extension of N^(2) by the actual relative base quotient Bhat/O²(H_n). The base action factors continuously because its finite two-group images are Frattini-trivial and hence form two-groups. Both original alpha and beta act on THIS actual quotient. Their formulas are the images of(4)--(5), with the complete h0 retained.

Equivalently the normalized kernel action satisfies the genuine compatibility

    beta_N theta_b beta_N^-1=theta_(alpha0(b)),

where theta_d and theta_f are the explicit two partial-inner automorphisms of the free-three kernel. This is an exact actual-canonical constraint on a nonlinear free pro-two kernel; it is not replaced by independently chosen module cocycles.

## 5. Remaining comparison

This supplies a concrete source, an embedded full nonlinear boundary kernel, an invariant family of actual relative quotients, and the exact correction relating their normalized involution to the original alpha. It does not compute h0 in terms of the original canonical u or identify the resulting cusp-frame coefficient with d_alpha. It also does not prove that a fixed element created in a quotient lifts to a fixed full element.

The next needed step is an identity relating this SAME h0 and the original canonical norm/associativity words, with all labelled cabling conjugators retained. No prospective positive modular map is used, no missing cubic relation is assumed, and no application of R2 precedes its actual marked peripheral input. The all-odd coefficient equality and nonlinear Omega gate remain open.

No finite-head census or producer was used. All new group changes, topology arguments and correction identities are printed in the two cycle31 sphere-kernel notes.
