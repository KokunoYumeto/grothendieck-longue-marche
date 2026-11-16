# A.38 working result: prescribed pro-p conjugators for full GT involutions

Historical working note written after the checkpoint03 source freeze. Integrated as A.38 after the snapshot; the formal source supersedes this note.

Let alpha=(-1,f) be a full GT involution. Let k be the unique R1 coboundary f=k^-1 alpha(k), and put u=k^-1. By A.37, u satisfies the full profinite pentagon. Define t=c2(u) in Zhat using the actual lower-central quotient [F,F]/[[F,F],F], with the sign convention matching A.4, and D=1+24t.

For every prime p for which D_p is a square unit in Z_p, choose mu_p in Z_p^times with mu_p^2=D_p. Furusho2010, Corollary12, gives both hexagon relations for (mu_p,u_p): its theorem is first read in the Q_p-prounipotent completion, but mu_p and m=(mu_p-1)/2 are integral in Z_p (at2 mu_p is odd), so all words already lie in F2^(p). The injective comparison F2^(p) -> F2(Q_p) descends those equalities. Consequently x->x^mu_p, y->u_p^-1 y^mu_p u_p is peripheral. Its mod-p H1 matrix is mu_p I, hence it is an automorphism by the pro-p Frattini criterion. The exact identity u=f alpha(u) intertwines this map with alpha_p and c_p.

Conversely, if a peripheral pro-p automorphism has this exact normalized conjugator u_p and multiplier mu_p, the class-three coefficient calculation of A.4 in the Q_p Malcev Lie algebra gives mu_p^2=1+24t_p. Thus the square-unit criterion is necessary and sufficient for a peripheral conjugator with this prescribed u_p. This is not a condition on arbitrary other local conjugators, whose associator parameter can differ because local fixed subgroups need not be trivial.

At p=2, D_2 is always in1+8Z2, so it has a unit square root. At p=3, D_3 is always1mod3, so Hensel's lemma provides a unit square root. Thus every full GT involution admits a peripheral conjugator to c on its maximal pro-2 quotient, with exactly the R1 parameter u and an adjusted dyadic multiplier. The same prescribed-parameter conclusion holds at3. At p>=5 the criterion is simply that D_p modp be a nonzero quadratic residue.

Scope: alpha must initially belong to full GT to invoke the genuine-action pentagon proof; this does not establish the p2 case for arbitrary P/GT0 involutions. These are maximal pro-p quotients, not arbitrary characteristic relative levels F/U^(p). It does not solve full third-cusp compatibility or the full involution problem. The later C.29 audit makes full generation automatic once that peripheral equation holds.

## Exact primary source boundary

Furusho, H. (2010). Pentagon and hexagon equations. Annals of Mathematics,171(1),545–556. DOI10.4007/annals.2010.171.545. Publisher PDF opened and read in full relevant sections: https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p13-p.pdf . Theorem2 printed547, Corollaries12–13 printed554, Question14 printed555.

Corollaries12–13 allow a quadratic-extension multiplier; Furusho explicitly warns the root might not be in Z_p^times. Therefore their general statement does not imply the above integral hypothesis. The special primes2,3 satisfy that hypothesis by elementary arithmetic. Question14 asks whether, in the full profinite group, the pentagon and a profinite root mu^2=1+24c2(f) imply the3-cycle; it already notes that the2-cycle follows from the full pentagon. We do not claim a solution of Question14. The actual printed page was subsequently inspected: its derived-series formula is a typographical error. Use the lower-central degree-two quotient explicitly stated above, not derived abelianization.

The CE agent independently checked all integrality, type, and scope points at03:42 UTC. Parent was notified before checkpoint.
