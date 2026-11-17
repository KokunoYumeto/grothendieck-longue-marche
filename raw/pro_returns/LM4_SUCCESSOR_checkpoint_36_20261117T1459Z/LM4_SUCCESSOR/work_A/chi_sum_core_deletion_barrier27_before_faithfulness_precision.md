# The actual index-two free-ten trial and a structural limit of core deletion

Research, checkpoint27. The single free-ten trial below is a valid actual quotient, but it does not improve the lower bound for the five-source subgroup. The subsequent obstruction treats all free quotients obtained by deleting peripheral Schreier generators in this same index-two cover; it is a mathematical incidence argument, not a census of finite targets or periods.

## 1. Actual cover and the executed trial

Use B123's free group F=F(a,B,d,e,bar a,bar B,bar d,bar e)*F(f,g,x), its complete defining normal subgroup N, and chi_sum(f)=chi_sum(g)=1, chi_sum(x)=0. Let F2=ker(F->C2) with transversal {1,f}. Its free Schreier basis has the sixteen peripheral generators U_(i,0)=U_i, U_(i,1)=f U_i f^-1 and the five retained generators f², g f^-1, fg, x, fxf^-1. All N lies in F2.

The one executed trial retains a_0,B_0,d_0,e_0,bar a_1 and all five retained generators, and kills the other eleven peripheral basis generators. The complete forty seed pairs and the common retained-head character shift of every signed source operator show that no relation in the entire source/deck/normal family can have both peripheral cores survive. The quotient is therefore an actual free group F10 quotient of W2=F2/N. This uses all signed source words, rather than a bounded orbit. Actual m has common head character zero, so the deletion kernel is m-invariant. Both m directions were checked on the complete21 Schreier generators; their induced automorphisms are inverse on the ten retained generators.

The exact whole-word source result is

| actual source basis | free-ten image |
|---|---|
| A_s=s1 s4^-1 s1^-1 | a_0 |
| B_s=A_s^-1 s1^-1 A_s | B_0 |
| D_s=s2 s1 s3^-1 s1^-1 s2^-1 | d_0 |
| E_s=s2^-1 | 1 |

The actual induced m fixes a_0 and d_0. Both D_s defects therefore vanish in this quotient. This is a genuine negative result for the intended lower-bound presentation: the quotient is not faithful on the actual source subgroup, since B131 proves [m,D_s] is nontrivial.

Producer: `work_A/code/compile_even_sum_a_source_quotient27.py`, genuine `.out/.err`, and `work_A/even_sum_a_source_quotient27.json`. The initial producer/output/JSON are retained with suffix `_initial`; the only cleanup removed a redundant always-true assertion, leaving the immediately following correct invariant assertion and all output unchanged. No second target was attempted.

## 2. Precisely defined class of possible repairs

Consider any quotient of F2 obtained by killing a subset of its sixteen peripheral Schreier basis generators while retaining all five retained free generators and imposing no other relation. This is a free quotient on the remaining basis. Assume it kills the entire actual N, so it induces a quotient of W2. We call this a basis-core deletion quotient only for the statement below; arbitrary changes of basis, added relations, other covers, or arbitrary free quotients are outside the claim.

If the four actual contact words A_s,B_s,D_s,E_s have linearly independent images in the abelianization of this quotient, then the quotient kills every peripheral generator from one of the two original families. Consequently it factors through the corresponding one-family filling. In particular, when equipped with its induced actual m action, it cannot distinguish the actual D_s commutator: that commutator vanishes in either one-family filling.

## 3. Complete actual incidence input

For each pair consisting of one unbarred and one barred family color, the complete seed list has at least one node and has the following unique difference of retained chi_sum heads modulo2:

| first/second | bar a | bar B | bar d | bar e |
|---|---:|---:|---:|---:|
| a | 0 | 0 | 0 | 0 |
| B | 0 | 0 | 1 | 1 |
| d | 0 | 1 | 0 | 0 |
| e | 0 | 1 | 0 | 0 |

Denote this entry c_ij. The actual signed source operators preserve the retained character and have a common head shift, independent of color: 0 for m and m^-1, -1 for v, +1 for v^-1. Thus source operators preserve pair differences. Retained deck conjugation shifts both heads equally. Every nonlinear connector remains present, but does not change which peripheral basis generator is the core of a conjugate.

A necessary condition for a core-deletion quotient to kill N is:

if U_(i,r) and bar U_(j,s) both survive, then r-s is different from c_ij modulo2.

Indeed, take a seed for that color pair and conjugate it by 1 or f to make its two retained residues exactly r,s whenever r-s=c_ij. This conjugate belongs to the actual N because N is normal in the whole F. In the free quotient its two peripheral factors are conjugates of two distinct surviving free basis generators (up to sign). Such factors cannot commute: centralizers of nontrivial elements of a free group are cyclic, whereas the two factors have independent nonzero abelianizations. Hence their commutator would survive, contradicting that the quotient kills N. This necessity does not discard or linearize the nonlinear connectors.

## 4. The four actual contact classes force a whole family choice

Directly rewriting the full actual source words gives the following family part of their abelianizations in F2; their retained-generator abelianizations are zero:

A_s = a_0 + bar a_0,
B_s = B_0 + bar B_0,
D_s = d_0 + bar d_0,
E_s = e_1 + bar e_1.

These four supports are disjoint. Rank four after core deletion therefore requires at least one generator from each displayed pair to survive.

Suppose a_0 survives. The first row of the incidence table forbids bar B_0 and bar d_0, so rank four forces B_0 and d_0. The B/bar e entry then forbids bar e_1, forcing e_1. Thus the surviving set contains a_0,B_0,d_0,e_1. These four generators exclude every barred generator at either residue:

- a_0 excludes all four barred residue-zero generators;
- e_1 excludes bar a_1;
- d_0 excludes bar B_1;
- B_0 excludes bar d_1 and bar e_1.

If instead bar a_0 survives, the transposed argument forces bar B_0,bar d_0,bar e_1, and excludes every unbarred generator at both residues. Both a_0 and bar a_0 cannot survive, since their own pair has entry zero. This exhausts the alternatives without enumerating subsets or target groups.

Therefore every such rank-four core-deletion quotient factors through one of the two one-family fillings. The entire actual m action descends to those fillings. The already established one-sided normal form proves [m,D_s]=1 there; equivalently both signed full D_s defects reduce literally to the empty word after deleting either entire family. The exact checker verifies these four existing comparisons as controls.

## 5. Consequence and remaining route

A pure deletion free target in this cover cannot simultaneously retain all four contact abelian classes and improve on the one-sided source quotient. In particular, simply adding more retained peripheral cores to the successful B132 free-seven quotient cannot yield a faithful five-source presentation by this method. This does not obstruct a quotient with genuine relations, a different marked presentation, or a separate normal-form proof.

A possible next exact construction would retain a_0,B_0,bar d_0 and impose the actual a/bar d relations instead of deleting one core. Their full nonlinear connectors and all signed source/deck translates would have to be controlled. No graph-product or finite relation presentation for that construction is asserted here.

## Exact certificate and scope

`work_A/code/check_core_deletion_barrier27.py/.out/.err` and `work_A/core_deletion_barrier27.json` retain all16 seed witnesses, the complete forty-input parity calculation, all four signed color/character checks, the four whole-word contact abelianizations, explicit exclusions for both forced choices, and both signed one-family controls. The certificate supports the finite input; Sections3–4 give the uniform mathematical implication. No conclusion about the full actual source kernel, any selected centralizer, or the original main decisions follows.
