# E.3: exact genus-one source audit and the mod-twelve sewing projection

Date: 2026-11-13. The new proved finite projection is E.61, in
`sections/E_genus_one_sewing_agent.tex`. The full E.3 question remains open.
No integrated source, assembler, report, or earlier certificate was changed.

## Primary-source domains checked

Basualdo Bonatto--Robertson, *Galois actions on surfaces and a higher genus
Grothendieck--Teichmüller group*, arXiv2606.01466v2, was opened directly at
Theorem3.18, Proposition4.7, Definition4.8, Theorem4.9 and its full genus-one
verification. Proposition4.7 identifies the full-GT genus-zero endomorphisms.
Theorem4.9 constructs the modular-operad action for the Nakamura--Schneps
subgroup defined by the two additional relations in Definition4.8.
The restriction of that constructed action is the inclusion of that subgroup
in full GT. This particular proved arrow does not give an extension of an
arbitrary full-GT genus-zero action.

Theorem3.18 adds the switch and three relations G1a, G1b and G2. In the proof
of Theorem4.9, pp.42--43, G1a uses symmetry and G1b uses the ordinary hexagon;
the auxiliary rho powers cancel. The G2 computation on pp.43--44 invokes
Nakamura--Schneps, proof of Claim8.3, relation6AS, end of published p.542.
The old source was reopened at the actual formula R' and its four substitutions
of relationIV, author PDF pp.32--33. These are the exact comparisons used here.

Lochak--Nakamura--Schneps, arXiv2602.12462v1, was reopened at §8, printed p.19.
The claimed full-GT action on the one-marked-point groups is an actual input
with that domain. The passage from those actions to the indicated cut
subsurface is explicitly left for future work. The new modular-operad paper
supplies a subgroup action compatible with contractions; it does not supply
that missing full-GT restriction comparison. No global nonexistence claim
about other comparison theorems is made.

Primary URLs:

- <https://arxiv.org/pdf/2606.01466>, current v2, 81 pages.
- <https://arxiv.org/pdf/2602.12462>, v1, 24 pages.
- <https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf>, author version3.14,
  §1 relationsI--IV, §5 Definition5.1, §8 Claim8.3 and R'.
- <https://shpilrain.ccny.cuny.edu/braids.pdf>, standard Artin representation
  and TheoremA, representation(1) with k=1, pp.1--4.

Opened web references: turn555view0/turn556view0/turn558view0 (new operad
paper); turn557view0/turn557view1 (LNS); turn561view0/turn562view0/turn567view0
(NS); turn569view0/turn569view1 (faithful Artin model). The parent must open
these primary URLs before using the web references in a final answer.

## Literal sewing word and braid comparisons

Use the NS word convention already retained by the project's finite braid
programs. The three B4 generators are a,b,c. Put

    E1=(aba)^4, E3=(cbc)^4, E2=cba b^-1 c^-1,
    X12=a², X23=b², X34=c²,
    X45=(aba)², X51=(cbc)², Z=(abc)^4.

The multiplier-one 6AS word is

    R_rho(f)=f(E3,a)c^(-8rho)f(b²,c²)f(E2,E3)f(E1,E2)
             f(a²,b²)a^(8rho)f(c,E1).

The actual four A3 maps, for A3=<u,v | uvuv=vuvu>, are

    (u,v) -> (a,X51), (E2,X51), (E2,X45), (c,X45).

Their respective central squares are

    (uv)² -> X34 Z, X23 Z, X23 Z, X12 Z.

In particular the four relation-IV substitutions in the full braid group
carry Z-powers `2rho,-2rho,2rho,-2rho`. They cancel in their product.
E.61.22 prints every factor, so no central projection is left implicit.
The program records the exact Artin images of all sixteen braid identities.
The faithful representation has

    sigma_i(z_i)=z_i z_(i+1) z_i^-1,
    sigma_i(z_(i+1))=z_i,

and fixes the other free letters. Thus equality in its output proves the
stated discrete braid identities; all resulting homomorphisms extend to
profinite completions. The primary faithfulness statement was opened.

The literal Ferrari fold B4->B3 sends a,c to a and b to b. It sends E1,E3
to the same central element (aba)^4 and E2 to b. Consequently the folded
sewing word is 1 for every symmetric commutator f, before reduction mod12.

## Exact Ferrari-homology projection

Let eta_m map B4 to `(Z/m)^2 semidirect SL2(Z/m)` by

    a -> (0,U), b -> (0,L), c -> (e1,U),
    U=[[1,1],[0,1]], L=[[1,0],[-1,1]].

The braid relations hold over Z, and the literal Ferrari generators
`ca^-1`, `aba c^-1 b^-1 a^-1` map to the two basis vectors. This specifies
the module and its based map. Both E1,E3 map to1.

The translation `t_w` for `w=(0,-1)` simultaneously conjugates the linear
pair `(L²,U²)` to the affine pair `(eta(b)²,eta(c)²)`. The universal free
group map therefore gives the full evaluation, not only its derivative.
For `q_m(f)=[[A,B],[C,D]]`, it gives

    eta_m(R_rho(f)) = ((-B-8rho A, A-1),I).

This equality is valid for each symmetric commutator f, with any chosen rho;
the next step supplies the actual rho of a whole normalized gentle pair.

## Complete frame calculation at modulus12

The actual normalized B automorphism has

    Phi(s)=s f=beta s beta^-1, Phi(r)=f^-1 r, Phi(sr)=sr.

The full pure frame beta is unique by the centralizer result proved and used
in E58. Its inverse h satisfies `f=h(y,x)^-1 h(x,y)`. Since f has zero
abelianization, `beta_ab=(-rho,-rho)`. This proves the rho comparison with
the exact NS frame word, without identifying separate proposed extensions.

At modulus4 the image of F under x->U²,y->L² is an abelian four-group; hence
q4(f)=1. The projective B map uses S=[[0,1],[-1,0]] and
R=[[0,-1],[1,-1]]. The full cubic relation says that `(q12(f)^-1R)^3`
is globally ±I. Its mod4 value is I, so its sign is +. This gives the exact
signed condition at3.

All24 beta matrices in SL2(F3) are checked. The character epsilon sending
U² and L² to1 has quaternion kernel, and epsilon(beta)=rho because
`-2rho=rho mod3`. The cubic condition passes precisely for

    beta=X^k S^j, 0<=k<3, 0<=j<4, X=U².

For these twelve matrices `[S,beta]=[[1,k],[k,1+k²]]` and epsilon(beta)=k.
The other twelve give cubic value -I. Combining mod3 and mod4 yields

    q12(f)=[[1,-8rho],[-8rho,1+64rho²]] mod12

for every full normalized gentle pair of multiplier1. Substituting into
the exact translation formula proves that the sewing projection vanishes
on this entire domain. The identity pair and the actual extra-CM pair of
E58 both lie in this domain, so this specified sewing projection cannot
equal the E1 extra-coset parity.

## Computation and preserved attempt

Replay: `python code/bc_genus_one_sewing.py` (standard Python library only).
Its sole data input is `code/bc_cm_literal_words.json`, SHA256
`38d154896b4a510b6ec131669eb68b2d2996933e6779546c8885b29f53a6a9d8`.
The output keeps all actual E1 beta words recovered by cyclic reduction in
`C2*Z`, their integral rho values, all24 mod3 matrices, the sixteen exact
Artin comparisons and all mod3/mod4/mod12 sewing values.

The first exploratory run searched every one of the4656 literal N_B-basis
commutators as a left correction to beta above the identity G6 point. No
change in the affine sewing value occurred. That complete first program,
JSON and stdout are preserved in `research/E61_initial_affine_probe`.
The completed structural proof explains the negative search and strengthens
it to every actual normalized gentle pair, without assuming cofinality of
the tested corrections.

## Remaining exact transfer under investigation

The full 6AS word is an element of the actual Ferrari kernel after folding.
Its rank-two homology image at12 is now computed on the whole gentle domain.
Higher Ferrari-kernel quotients retain the four evaluations involving E1/E3,
which the homology map killed. The new paper proves the whole word vanishes
on its NS subgroup. Establishing a full-pentagon consequence in one of these
higher actual quotients, or constructing a compatible full-pentagon lift of
the E58 frame, remains to be done. The source audit has not supplied the
unproved full-GT sewing relation and does not use it as an extra axiom.
