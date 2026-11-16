# Further descent: exact structural gate after C44

Status: notes-only research. No additional large numerical search has been started. C44 is proved and integrated. The separate larger-peripheral surjectivity argument is a complete candidate at `notes/pbc_peripheral_descent_surjectivity_draft.tex` and is not yet registered.

## What the new exact ghost settles

C44 gives an actual full multiplier-one element e with D(e)=1 and Delta(e)=1. Thus the same e has parity vector (1,0,0,...) at every finite depth. There is no longer a need to recompute a new ghost word at each deeper level. This does **not** supply preimages of e under the restriction of D to the gentle group. C31 proves three independent iterated characters; nonzero later coordinates still require a new actual prelifting argument.

The word is `[[x^2,y^2],z^2]^2`, freely reduced length44, in the temporary marking of C23. It lies in the full kernel of every peripheral modular filling, not merely in all finite detectors tried so far. The closed-normal relative refinement is the reason this exact word supplies an actual full group element.

## The larger peripheral map is a different problem

The candidate C45 shows D:P→GT0 is onto. For the one filling F→Gamma, H2(Gamma,Zhat)=0 forces its actual central kernel N/[F,N] to inject into F_ab. A product discrepancy between three lifted peripheral conjugates is central and has zero abelianization, hence iszero. The full central criterion then lifts any target positive modular automorphism to P. This step does not give geometric S3 symmetry in the source.

Thus the actual remaining prelifting problem is the simultaneous six-coordinate symmetric one. It cannot be replaced by the single-filling problem or by an arbitrary peripheral preimage.

## A precise finite obstruction, with frames kept

Let q:Gamma→G be an actual finite marked quotient factoring the standard quotient to S3. Write F_G for its pure kernel and retain s,r,tau=sr. Let A_G be the finite group of automorphisms alpha of G which fix tau, induce identity on S3, and conjugate s and r by elements of F_G. Put E=Gamma/[N,Gamma], N=ker q, K=ker(E→G). The actual five-term sequence identifies K intersect E' with M=H2(G,Zhat). The possible extra quotient of K embeds into Gamma_ab; no arbitrary Schur cover is substituted for E.

Choose pure frames B_s,B_r in G for alpha, and any lifts to E. The product discrepancy

T_alpha=(B_s s B_s^-1)(B_r r B_r^-1)tau^-1

belongs to M. It is independent of the central choices of those lifts. For c in C_G(s) intersect F_G define j_s(c)=[c,s] in M, and define j_r similarly. These are homomorphisms and have exponents dividing2 and3, respectively. Replacing a frame on the right by a genuine pure centralizer changes T_alpha by exactly the corresponding j-value.

Consequently the class

delta_G(alpha)=[T_alpha] in M/(im j_s+im j_r)

is independent of the choices of pure frames. It vanishes **if and only if** alpha is induced by an actual full positive peripheral automorphism of Gamma fixing tau literally. For sufficiency, zero supplies corrected pure frames whose product is tau in the actual E. The source presentation then defines an automorphism of E: Hopf naturality gives H2(alpha) on M, and the induced action on the remaining abelian kernel is identity. The modular central criterion gives the full lift with cusp frame1. Necessity follows by taking its two actual pure frames in E.

This is exactly the framed finite gate solved for the explicit C27 and C31 candidates. It is stronger than a finite automorphism enumeration, and it is independent of the choice of a pc presentation or a relation-lattice reduction.

The pure-centralizer images equal the full-centralizer images in this situation. Indeed C_G(s) maps into C_S3(s)=<s>, so multiplying a centralizer by a power of s makes it pure without changing its commutator class. The same argument applies to r. Thus the quotient is the usual reduced Schur multiplier for the two torsion conjugacy classes, with the cusp frame fixed separately. The standard definition was freshly opened in Roberts–Venkatesh, *Hurwitz monodromy and full number fields*, section4.2, equations(4.1)–(4.2), printedpage7, https://math.stanford.edu/~akshay/research/full.pdf (refs turn1186view0, turn1187view0–2). No vanishing theorem from that paper is invoked; its pseudosimple hypotheses do not apply to the present solvable groups.

There is also an exact crossed law. A choice of the two lifted torsion frames defines an automorphism tilde-alpha of E before imposing the cusp condition, with tilde-alpha(tau)=T_alpha tau. Composing two such automorphisms gives

delta_G(alpha beta)=delta_G(alpha)+alpha_*delta_G(beta).

The induced H2 action preserves both centralizer images. Thus actual finite cusp-fixed images are the stabilizer of zero for this explicit affine action. The kernel of a crossed homomorphism need not be normal; no normality is inferred.

## Normalization is uniform once the actual tuple is obtained

Use the old marking and the exact cycle rho_plus(x)=y,rho_plus(y)=z. For any source word f set v=phi(f), u=phi(rho_plus(f)f). Under an abelian normalization f_a=y^(-a) f x^a with a divisible6, the identities in the full target are

v_a=tau^(-a)v,   u_a=u.

The second follows from rho_plus(f_a)f_a=z^(-a)(rho_plus(f)f)x^a and s^a=r^a=1. Thus the two descended pure frames, including an unchanged possible right r^k purity correction, acquire the same pure left cusp factor tau^(-a). A full inner adjustment by tau^a removes it. This is the uniform mechanism already used in C31. It works at every depth once the actual source tuple and abelian normalization data are present; it does not assert that an arbitrary proposed tuple lies in the actual joint word image.

## Exact outstanding gate before any next large calculation

For a new deeper target one must first specify one actual finite marked joint quotient of the six fillings, together with a tuple in its actual derived word image, and an actual finite automorphism with the required pure frames. One must then prove delta_G(alpha)=0 in the exact reduced Schur quotient above. A sufficient structural induction would show that the new relative H2 layers have zero pairing with this particular framed product discrepancy, after the already solved quotient layers are removed. C31 did this by a three-primary natural homology isomorphism, an original-row two-primary identity, and two actual quadratic central covers. The numerical cancellation in those two covers is not yet a theorem for all subsequent layers.

The next useful investigation is therefore a structural description of those relative H2 modules and the induced discrepancy, or a simultaneous symmetric lift of a full target through the six fillings. Merely increasing the degree of the permutation representation, checking a finite automorphism, or seeing zero in a processed relation lattice would not resolve the missing gate. No claim that all iterated parity characters are independent is made.
