# Literal marking provenance for the affine P4 proof

The main proof `actual_P4_affine_character_pentagon_boundary30.md` remains frozen at80c847800c07e700251dea92a3611e67292bc26d0b3921218fce1949d6887449. This addendum binds its actual input convention; it does not invoke a profinite consequence of a prounipotent theorem.

## Original pentagon

I freshly opened the original publisher PDF of Furusho, H. (2010), *Pentagon and hexagon equations*, Annals of Mathematics,171,545–556, DOI10.4007/annals.2010.171.545:

https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p13-p.pdf

The tool source is turn1056view0. Printed page547, Equation(4), with the immediately following definition of the standard pure generators, is exactly

    f(x12,x23 x24) f(x13 x23,x34)
       = f(x23,x34) f(x12 x13,x24 x34) f(x12,x23).

With (a,b,c,d,e,f)=(A12,A13,A23,A14,A24,A34), this is literally the ordered Equation(11) in the new proof. Only this actual word/marking definition is used from that location, not Theorem2's prounipotent implication.

## Existing retained actual source

The exact inverse actions and the same five pentagon argument pairs were already fixed in `work_CE/research_A5_pentagon_bridge.txt`, Sections2–3, and in `work_CE/code/probe_A5_all_pentagons.py` (`pure_ok` and `ps`). I reread both in full at this use. No earlier finite classification is used in the new exhaustive symbolic proof.

## Direct bridge for every action needed in the new proof

Write the standard pure generators in the Artin braid group as

    Aij=(sigma_(j-1)...sigma_(i+1)) sigma_i^2
                         (sigma_(i+1)^-1...sigma_(j-1)^-1).

The actual three-strand full twists are ade for strands1,2,4 and cef for strands2,3,4. They are central in the corresponding three-strand subgroups. For the first inclusion, the two half twists are sigma1 and sigma3 sigma2 sigma3^-1: its A13 is exactly A14=d, since sigma1 commutes with sigma3, and its A23 is A24=e. Thus this is the marked subgroup, not an independently relabelled free triple. The second inclusion is the adjacent three-strand subgroup.

Centrality of ade gives

    a^-1 d a=(de)d(de)^-1,
    a^-1 e a=d e d^-1.

Centrality of cef gives

    c^-1 e c=(ef)e(ef)^-1,
    c^-1 f c=e f e^-1.

The disjoint/nested strand twists give [a,f]=[c,d]=1. These are precisely the complete a and c rows used to derive the two rank-one matrices.

The actual full twists are Delta3^2=abc and Delta4^2=abcdef in the same standard ordering. Hence Z=abc is central in the P3 base and Z(def) is central in P4. It follows directly that

    Ad(Z^-1)|F(d,e,f)=Ad(def),
    b=a^-1 Z c^-1.

These a/c actions, the full-twist identity, and the actual free fiber are ALL the pure-action dependencies of the classification. The displayed middle b-action row and its separately preserved three-generator free-word check are redundant for that proof: no matrix or case relies on the middle-row interlaced conjugator. This avoids introducing a new dependence on an unchecked alternative convention for A13.

The actual Fadell–Neuwirth free-fiber source is the one already used in the complete C28/A36 proof. The five quotient substitutions in the new proof then follow as literal equalities of the standard marked generators, and every surviving pentagon word is exactly the one in the original publisher Equation(4).
