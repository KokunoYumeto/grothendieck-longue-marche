# Actual full-boundary regrouping of the mirror presentation

Research, checkpoint24. This is an exact change of the complete marked
presentation. An isolated cyclic amalgam appears, but its injection after
the remaining fifteen relations is not assumed.

## 1. The actual boundary word

Use the B112/B114 common marking `K=F(a,B,d,e,f)`, with
`B=C b C`, `h=fk`, `z=C h`, and selected gap cone `c=a C a^-1`.
The actual physical ordinary comb is O=(x1,x3,x4,x5,x6), and its
complete product is

`P5=O1...O5=a B f d e`.

Consequently the full six-puncture boundary, with the actual cone
whisker included, is

`T=c P5=a b C f d e=a b z k^-1 d e=a b z d e k^-1`.

The last equality uses exactly `[k,d]=[k,e]=1`. Since k also commutes
with a,b,z, the actual regional relations imply `[k,T]=1`. No
replacement of the selected cone by adapted C has occurred. This
calculation is also consistent with preservation of the full boundary
by the actual based braid, but no external braid theorem is needed.

In the exact mirror vertex, j has order two and `j P5 j=P5^-1`.
The added actual cross relation is `[j c j,k]=1`.
Define

`D=j c j`, `u=T D`.

Then `D²=1`, `T=u D`, `c=j D j`, and

`P5=cT=j D j u D`.

Substituting this expression shows, by cancelling on the two sides,
that `j P5 j=P5^-1` is precisely `j u j=u^-1`. Further,
`[k,D]=[k,T]=1` is equivalent to `[k,D]=[k,u]=1`.

## 2. The isolated corner and the exact extra relations

The isolated group on j,D,u,k is therefore

`C0=<j,D,u,k | j²,D², juj=u^-1, [k,D],[k,u]>`

`   = ((C2(D)*Z(u)) times Z(k)) amalgam_Z(u) (Z(u) semidirect C2(j))`.

Both cyclic edge embeddings in this display are explicit, so it is a
genuine discrete amalgam. Its elementary normal forms are independently
reviewed in DE's
`next_marginal_source/actual_mirror_triangle_and_boundary_corner24.md`.
This assertion concerns C0 itself. The actual full folded group is a
quotient of `C0*C2(r1)*C2(r2)*C2(r3)*C2(r4)` by the fifteen explicitly
retained relations below. No Freiheitssatz or corner injection is
inferred from the amalgam description.

Set `P_i=j r_i` for i=1,...,4 and `P5=j D j u D`. Recover the
literal common letters by the inverse free-basis substitutions

`a=P1^-1 P2`, `B=P2^-1 P1 P2`, `d=P3^-1 P4`,

`f=P3^-1 P5 P4^-1 P3`, `e=P5^-1 P3 P2^-1 P5`.

Recover the adapted cone and remaining regional letters as

`C=a^-1 j D j a`, `b=C B C`, `h=fk`, `z=C f k`.

The fifteen extra relations are the five generic relations

`[C,z]`, `[k,a]`, `[k,b]`, `[k,d]`, `[k,e]`,

and the ten actual node relations

`[v,CvC]` for v=a,b,d,e,

`[a,b]`, `[CaC,d]`, `[CaC,e]`, `[d,CeC]`,

`[b,f d f^-1]`, `[b,f e f^-1]`.

All ten node words are independent of k in this marking. The final
two are the actual `[b,h d h^-1]` and `[b,h e h^-1]`, simplified
using the already retained `[k,d]=[k,e]=1` and h=fk. Their based
conjugators f remain present.

This gives eight generators and exactly twenty-four ordinary free-group
relators: six involution squares (j,D,r1,...,r4), the dihedral relation,
two k commutations, five remaining generic relations and ten node words.

## 3. Two-sided equivalence, including the replaced generic relation

The generator substitutions are invertible before any regional node
relation is used. In the earlier eight-generator presentation, retain
j=r0 and r1,...,r4, and put

`D=j(a C a^-1)j`, `u=(a C a^-1) P5 D`.

The inverse sends old r5 to `D j u D` and old C to
`a^-1 j D j a`. The old r5-square is equivalent to the dihedral
relation, and the old C-square is equivalent to D². All sixteen
generator compositions are exact in the corresponding free products
with involutions and the one dihedral relation.

It remains to justify a genuine relation replacement, not just a
generator change. In the original z marking the generic relations are
`[C,z]`, `[k,z]`, and the four `[k,v]`, v=a,b,d,e. Given the four
latter relations, the boundary identity above makes `[k,T]` equivalent
to `[k,z]`. Given the added cross relation `[k,D]`, the equality
u=TD makes `[k,T]` equivalent to `[k,u]`. Thus replacing `[k,z]`
by `[k,u]` is reversible. The old source formula
`h k h^-1=C k C` is the same `[k,z]` relation; explicitly its
relator is the C-conjugate of the inverse of `[k,z]`. The source
relation `[h,C]` is literally `[C,z]` after z=Ch.

Conversely, the new four `[k,v]`, `[k,D]`, and `[k,u]` give
`[k,T]`, then `[k,z]`; the remaining original generic relation
and all original node relations follow by reversing the same two
steps. This proves equality of the two actual normal closures.
Every original outer relation is still the mirror conjugate of its
inner counterpart, as in the already verified full folded presentation.

## 4. Exact executed certificate and marked source data

Producer/output:
`work_A/code/compile_annular_boundary_corner24.py/.out/.err`.
Full data: `work_A/annular_boundary_corner24.json`.

The producer reads the previously verified actual 8/24 presentation
and performs an independent reduction in the free product
`D_infinity(j,u)*C2(r1)*...*C2(r4)*C2(D)*Z(k)`.
It checks all sixteen generator inverse compositions; the selected
cone, P5, T=uD and both inversion identities; fourteen literal
retained-relator comparisons; both original characters; and the two
explicit k/d,e boundary-commutation steps. The logical equivalence
of the changed generic relator is the proof in Section3, not an
unsupported quotient-normal-form assertion by the code.

All six actual based source words are transferred in full. Their
reduced lengths in this free/dihedral marking are

`6,18,54,30,14,1`.

The original orientation sends D to1 and all other new generators to0.
The mirror parity sends j,r1,...,r4 to1 and D,u,k to0. The six source
words have both parities zero. The original actual one-neck group is
the mirror-parity kernel after all twenty-four relations are imposed.

## 5. A distinct, exact branch-class obstruction

The useful prefix P5 changes fine peripheral parity. It cannot be
replaced by an eta-inverted lift which retains the mod2 peripheral
vector of the actual branch f. Indeed, in the genuine free product

`Q=K semidirect_eta C2(j)=C2(r0)*...*C2(r5)`,

we have `j=r0`, `O_i=r_(i-1)r_i`, and f is conjugate in K to O5.
If s has the same vector as f in `K_ab tensor F2`, then its vector
in `Q_ab` is r4+r5. If eta(s)=s^-1, then js is an involution,
whose abelianization would be r0+r4+r5. Every nontrivial finite-order
element of the discrete free product is conjugate to a factor; its
abelianization is therefore one basis vector, a contradiction.

Exactly the same proof holds in the full completion using the already
audited full profinite free-product torsion theorem and the continuous
finite abelian quotient. The subgroup Khat is the actual open
mirror-parity kernel of Qhat. In particular no conjugate of an odd
power of f can be eta-inverted. More generally, an eta-inverted
element of K has mod2 peripheral vector either zero or one of the
prefix vectors O1+...+Oi. Since only O5 has nonzero branch winding,
an eta-inverted odd-branch element must have vector O1+...+O5.

This does not prevent a presentation change: P5 is the required
example with changed fine parity. It explains precisely why a naive
simultaneous coarse section retaining the old branch class fails.
The remaining fifteen actual relations, not their coarse images,
still determine the post-cross centralizer.
