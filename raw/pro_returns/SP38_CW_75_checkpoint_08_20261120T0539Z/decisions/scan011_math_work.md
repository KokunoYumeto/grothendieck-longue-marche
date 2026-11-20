# Scan011 — preliminary mathematical checks

These checks use the draft statements; the readings are not yet adjudicated. No image or external material was used for these calculations.

## M011-SPLIT

For a right G-torsor T, define affine pairs (gamma,f) by f(xh)=f(x)gamma(h). Fix t. Every x=t h uniquely, so q_t(gamma)(t h)=t gamma(h) is uniquely defined, bijective, fixes t and projects to gamma. Composition gives q_t(gamma delta)=q_t(gamma)q_t(delta). Thus the two displayed conditions characterize a splitting, under this definition.

## M011-KERNEL

The kernel of projection to gamma is Aut_G(T). Fixing t identifies it with G by i_t(g)(t h)=t g h; composition i_t(g)i_t(k)=i_t(gk). This identification depends on t for a general nonabelian G. The bare i in the draft can be understood after this choice, or canonically for an abelian acting group; its written labeling still awaits ink adjudication.

## M011-CHANGE

If tprime=t g and i means i_t, conjugating q_t(gamma) by i_t(g) lies over gamma and fixes tprime: i_t(g)^-1(tprime)=t, q_t(gamma)(t)=t, and i_t(g)(t)=tprime. The uniqueness in M011-SPLIT gives q_tprime=int(i_t(g)) composed with q_t. This verifies exactly the basepoint-change computation under the stated identification.

## M011-CONVENTION

A bare right translation R_g:x->xg instead has group component h->g^-1 h g in the affine-pair group; it is not generally in the kernel, and R_g R_k=R_(kg). Thus the basepoint-change proof cannot identify i(g) with R_g for arbitrary nonabelian G without additional conventions. For abelian G, R_g=i_t(g), independently of t. This is an interpretation qualification, not an ink correction or an assertion that the manuscript explicitly claimed canonicity.

## M011-CANCEL

The primary first canceled calculation q_t(gamma)(tprime)=q_t(gamma)(t)gamma(g)=t gamma(g), with tprime=t g, is algebraically correct by equivariance and the fixed-point condition. Its canceled state does not make it a false statement. The actual canceled first gamma still requires visual adjudication.

## M011-GAMMA

For Gamma a subgroup of Aut(G), the inverse image of Gamma is a subgroup; each q_t restricts to a section over Gamma and the same kernel-conjugation relation applies. This checks the mathematical content of the marginal Itou/Idem statement, without deciding its wording.

## M011-CYCLIC

For the additive group Z/n with n positive, an endomorphism is determined by the image a of 1 and acts by multiplication by a. Composition is multiplication modulo n. It is invertible exactly when a is a unit, proving End(Z/n) is the residue ring and Aut(Z/n) its unit group. The affine group has unique pairs (b,a) with law (b,a)(c,d)=(b+ac,ad).

## M011-DIHEDRAL

For n>=3, the residues +1 and -1 are distinct units. The subgroup of affine pairs (b,epsilon), epsilon in {+1,-1}, has 2n elements. With translation a=(1,+1) and reflection r=(0,-1), a^n=r^2=1 and r a r=a^-1, giving the displayed dihedral semidirect product. The inclusion in the full affine group is immediate from {+1,-1} being a subgroup of the unit group.

## M011-TWO

For n=2, +1=-1 modulo 2, so the written set {+1,-1} has one element and its affine semidirect product has only two elements. This verifies the NB and explains the written n!=2 qualification for the intended noncollapsed sign subgroup. At n=1 that sign set also collapses; the final application explicitly uses n>=3, so no extra exclusion is supplied to the text.

## M011-FINAL

For a torsor under a cyclic group of order n>=3 with unordered inverse generators {u,u^-1}, automorphisms carrying that pair to itself are exactly exponent +1 or -1. The two generators are distinct since u=u^-1 would imply order at most 2. After a basepoint choice, affine automorphisms with those components form T-coordinate translations semidirect {+1,-1}; evaluation at the basepoint and the sign give 2n possibilities. This verifies the final split sequence under the usual affine-pair interpretation; the reversal of argument order Aut(Z,T)/Aut(T,Z) is not normalized.

## M011-INDEX

The C alternative b in q_b(gamma)t=t is not generally interchangeable with t. On the additive Z-torsor T=Z, q_a(-1)(x)=2a-x. Taking t=0, b=1 gives q_b(-1)(t)=2, not t. Refined statement M011-CHANGE uses q_t and the chosen-basepoint fixed-point property. This refutes only the interpretation with an independent b; whether the ink has t, b or an unresolved form awaits adjudication, and mathematics does not select the letter.
