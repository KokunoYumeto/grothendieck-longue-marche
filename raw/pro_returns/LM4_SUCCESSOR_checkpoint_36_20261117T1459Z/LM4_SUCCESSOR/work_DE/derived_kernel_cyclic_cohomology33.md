# The whole cyclic cohomology of the actual derived congruence kernel

Separate checkpoint33 research. This strengthens the preceding r-frame criterion without choosing its remaining sign. Frozen A105 and all other formal sources are unchanged. The preliminary full proof received independent conversation-level checks from root and CE; this is the first saved source.

## 1. Exact original ambient objects

Use the actual free profinite product B=C2(s) amalg C3(r) and its original epimorphism to S3. Let F be its kernel, the full rank-two free profinite group on

 x=(sr)^{-2}=r^{-1}s r^{-1}s,
 y=sxs=s r^{-1}s r^{-1},
 z=(xy)^{-1}.

Write F' for its closed derived subgroup. The order-three automorphism rho=Ad(r)|F has the literal substitutions

 rho(x)=y, rho(y)=z, rho(z)=x.

These follow by substituting the displayed words and using s²=r³=1. In the ordered abelian basis (x,y), its matrix and the relevant difference are

 rho_ab=[[0,-1],[1,-1]],
 I-rho_ab=[[1,1],[-1,2]],  det(I-rho_ab)=3.

A second literal word needed below is

 s r^{-1}s = y r.

These are the original based words, not a changed free basis or a projective matrix substitution.

The finite-factor Herfort--Ribes torsion/centralizer input used in A105 applies to this very B: every element of order three is conjugate to r or r^{-1}, and C_B(r)=C3(r). In particular F^rho=1 and (F')^rho=1, because the original S3 quotient is injective on C3(r). No assertion about a completion of a discrete infinite-index subgroup is involved.

## 2. Every continuous C3-cocycle in F' is trivial

Let h in F' satisfy h rho(h) rho²(h)=1. Then h r is an order-three element of B, since its S3 image is the nontrivial r. Apply the finite-factor torsion theorem.

If h r=g r g^{-1}, the S3 image of g centralizes r and lies in <r>. Right multiplying g by a suitable power of r does not change its conjugate and makes g belong to F. Thus this case has

 h r=f r f^{-1}, f in F,
 h=f rho(f)^{-1}.

Its abelianization gives (I-rho_ab) f_ab=0. Multiplication by3 on Zhat is injective, so the determinant calculation forces f_ab=0. Therefore f lies in F', and h=(f^{-1})^{-1}rho(f^{-1}) is an F'-coboundary.

If h r=g r^{-1}g^{-1}, the S3 image of g inverts r and belongs to the transposition coset s<r>. Right multiplying by an appropriate power of r again preserves the conjugate and normalizes that image to s. Write the resulting g as f s, f in F. Using the literal identity above gives

 h r=f(s r^{-1}s)f^{-1}=f y r f^{-1},
 h=f y rho(f)^{-1}.

Let f_ab=(a,b). Since h_ab=0, this requires

 (I-rho_ab)(a,b)=-e_y,
 a+b=0,  -a+2b=-1.

Hence3b=-1 in Zhat, impossible after projection to Z3. This entire second torsion class is excluded. Therefore

 H1(C3,F') has exactly the basepoint.

The conclusion concerns continuous cocycles in the actual compact closed subgroup F'. It does not use an unrestricted infinite-basis completion or a profinite Kurosh theorem for that subgroup.

## 3. The entire derived congruence-kernel cohomology has two points

Retain the original signed q3:F->SL2(F3) of A105, with X=I+2E12, Y=I-2E21, and C=J mod3=XYX^{-1} mod3. On F' the actual rho action agrees with Ad(C), since its central sign discrepancy on F kills all commutators. Put

 K3'=ker(q3|F').

Thus K3' is rho-stable. The complete quaternion calculation in A105 gives q3(F')=Q8 and Q8^rho=C_Q8(C)={I,-I}. Both facts concern the actual signed marking. The whole kernel ker(q3) on F is not substituted for K3'; its failure of rho-stability was preserved explicitly in the preceding note.

There is a natural pointed bijection

 {I,-I} -> H1(C3,K3'),
 a -> [g^{-1}rho(g)], where g in F' and q3(g)=a.

A lift exists because q3(F')=Q8. Since a is fixed by rho, the cocycle belongs to K3'. Changing g to gn with n in K3' changes it to n^{-1}(g^{-1}rho(g))rho(n), so its class is independent of the lift.

Surjectivity follows from Section2: every cocycle in K3' is an F'-coboundary g^{-1}rho(g). Its image in Q8 then forces q3(g) to be fixed, hence to be I or -I.

For injectivity, suppose the cocycles of g1,g2 become equal after K3' conjugation. Absorb that conjugator into g1 to arrange

 g1^{-1}rho(g1)=g2^{-1}rho(g2).

Then g2 g1^{-1} is fixed by rho and lies in F'. The exact centralizer input gives g2=g1; before absorption their Q8 images were already equal. Thus the two labels are distinct. In particular the -I label gives the unique nonbase class.

This is also a homeomorphism. The cocycle set in the compact group K3' is closed, its compact conjugation-orbit relation is closed, and hence its quotient H1 is compact Hausdorff. A bijection from the finite discrete two-point space is a homeomorphism. This classification gives no unasserted group law to the pointed cohomology set.

## 4. The exact original CM choice inside these two points

Retain A105's original LM7_PUSH E61/E65 frames and write

 q3(A_r)=epsilon_A X^nu C^{-nu},
 a_epsilon=epsilon X^nu C^{-nu}, epsilon in {1,-1}.

For any t in F' lifting a_epsilon, the preceding note defines

 z_t=t^{-1}phi^{-1}rho(t).

Since phi^{-1}=A_r rho(A_r)^{-1}, put b=A_r^{-1}t. Then, in the printed order,

 z_t=b^{-1}rho(b),
 q3(b)=q3(A_r)^{-1}a_epsilon=epsilon_A epsilon I.

Consequently the obstruction class is precisely the point labelled epsilon_A epsilon in the two-point space of Section3. The actual finite transporter candidates exhaust the entire cohomology space; they do not give two possible actual normalized profinite frames.

For full-GT negative alpha, A105 gives epsilon_u=d mod3 and (-1)^{Delta(alpha)}=epsilon_A epsilon_u. The desired candidate epsilon=d mod3 therefore has obstruction label

 epsilon_A(d mod3)=(-1)^{Delta(alpha)}.

This identifies the original CM character with the exact C3-cohomology choice. It does not determine that choice, prove Delta(alpha)=0, or strengthen the frozen formal claim.

## 5. Limits and dependencies

The previously saved transporter-only coprime-p limitation still applies: every actual rho-equivariant finite p-group image of K3', p not equal to3, kills both of these cohomology classes. The distinctness in the actual compact group is established above by the centralizer argument, not by a finite target computation. Relative-three and coupled full-pentagon targets remain possible; no claim about them is made.

Inputs: the exact original based modular words and finite-factor theorem printed in work_DE/A105_original_CM_parity_proposed.tex; its original source binding work_DE/original_CM_source_binding33.md; and the preserved earlier corrected note work_DE/original_r_frame_cohomology_gate33.md. The accepted finite-factor theorem is the already audited A_HR1985 input. No new primary retrieval, finite census, group producer, private PDF, or shared-file edit occurred for this proof.

Saved UTC: 2026-11-17T11:38:06.403474+00:00
