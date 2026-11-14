# Finite CM refinement and GT0 shadows

The statement and proof are D.25 in `sections/D_cm_shadow.tex`. The program `code/d_cm_shadow.py` has run successfully and retains all exact data in its `.json` and `.out` files.

## Exact field comparison

Let r=(3/4)^(1/4). The full four-torsion field of E3:y²=x³+1 is Q(i,r), and this is also the field of all x-coordinates of E4[3], where E4:y²=x³−x. Explicit inverse algebraic formulas prove both equalities. On E3 the point Q0=(0,1) has order3. For P∈E3[4], the identity y(P)=x(P)²[x(P−Q0)−x(P+Q0)]/4 recovers the full four-torsion field from the projective twelve-torsion field. This is the exact reason the single global sign matters: separate projective E3[4] gives only Q(ζ12), while projective E3[12] contains the full nonabelian field.

## Actual finite calculation

Let B=C2*C3 and Q=SL2(Z/12)/global±1, of order576. Its torsion-free kernel N has rank97. The Bass–Serre quotient graph has480 vertices and576 edges, and its97 fundamental cycles explicitly model N^ab. The program represents B/[N,N]N^p inside F_p[Q]⋊Q, for p=2,3. Its group law and two m=0 hexagons are checked directly.

There are six A reductions and eight beta reductions with multiplier1,V12=I. Among their48 pairs,24 satisfy the CM relation and24 violate it. The cusp equation has12+12 solutions at p=2 and24+24 at p=3. Every surviving combined pair has an induced97-by97 kernel map of rank97 in both characteristics. Thus they define genuine automorphisms of the specific finite quotient G6=B/[N,N]N^6, of order576·6^97. CRT coefficients for the single common conjugators are saved, so this is not a comparison of unrelated local candidates.

The finite centralizer checks show q(C_G2(s)∩F)=1 and q(C_G3(r)∩F)=1. Hence the action on G6 determines both matrix conjugator reductions, eliminating the ambiguity that remains in a matrix calculation alone.

For each finite automorphism, lift beta to F=<x,y>, write beta_ab=a x+b y, and gauge by x^(b−a). The resulting f'=s beta' s beta'^{-1} lies in F'. The identities alpha'(s)=s f', alpha'(r)=f'^{-1}r and alpha'(u)=u are precisely the two m=0 finite hexagons. Pulling the finite kernel back to B3 gives a normal finite-index subgroup contained in PB3; its Nord is36, so multiplier1 is a unit, and finite automorphism supplies surjectivity. These are actual finite GT0 shadows under the definition in the opened primary paper.

The twelve extra pairs give distinct shadows that cannot arise from G_Q, because their two restrictions to the same field Q(i,r) disagree. They are **nonarithmetical finite shadows**. D.27 subsequently proves these **selected** shadows nongenuine by the complete two-prime class-two test. It also gives an alternate homology action with the same extra CM pair that survives both tests and extends to H2 times_Q P3. Genuineness of that alternate action and realization of the CM pair remain unresolved under the all-finer-finite-quotients test of D.22.

Independent audit: agent A checked the two exact field equalities and the global-sign normalization; parent checked the cusp gauge and finite-shadow conversion. The code's exact witness checks remain reproducible in the deliverable.
