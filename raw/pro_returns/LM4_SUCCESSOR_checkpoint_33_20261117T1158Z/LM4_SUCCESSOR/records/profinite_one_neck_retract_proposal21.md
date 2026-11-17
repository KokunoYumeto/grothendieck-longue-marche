# Proposed full profinite upgrade of the one-neck comparison

Late checkpoint21 research proposal, awaiting independent review. It is
not a formal result or a decision of the global problem. The new input
is DE's observed actual retraction of the common K from each bad vertex's
ordinary index-two subgroup on the simply connected slit base.

## 1. Actual scope and a general finite-head construction

Let G=R1 *_K R2 be the genuine discrete one-neck amalgam already proved
in work_CE/shared_five_generator_neck_21h.txt. Each Ri has its actual
orientation character to C2, with ordinary kernel Hi of index two.
The edge K=F5 lies in both Hi. On the slit base, one-family filling maps
Hi to the fiber group F7; its geometric free-factor retraction to K is
the identity on the literal K. Thus there are actual retractions
ri:Hi to K. These do not assert that filling is equivariant.

For a finitely generated group K there is a cofinal family of fully
invariant finite-index normal subgroups L: intersect the kernels of all
maps to finite groups of order at most n. There are finitely many such
maps, and precomposition with any endomorphism preserves the defining
kernel intersection. Every given finite-index normal subgroup contains
one of these L, by including its finite quotient among the targets.

Choose a representative ti of the other coset of Hi in Ri. For a
fully invariant L, put Pi=ker(Hi --ri--> K --> K/L) and take its
index-two core Ni=Pi intersect ti Pi ti^-1 in Ri. The restriction of
Pi to K is exactly L. The second restriction contains L, because

    k -> ri(ti^-1 k ti)

is an endomorphism of K and L is fully invariant. Hence Ni intersect
K=L. The subgroup Ni is normal finite-index in Ri and is contained
in Hi, so the finite quotient Ai=Ri/Ni retains orientation and embeds
the common edge K/L. If a prescribed finite-index normal Mi in Ri
must also be killed, choose L contained in Mi intersect K and replace
Ni by Ni intersect Mi; its intersection with K is still exactly L.
The same L can be used for both vertices.

This proves a stronger compatibility statement than separate full
edge topology: every pair of prescribed finite vertex quotients has
refinements with exactly the same finite edge kernel.

## 2. Finite-group amalgams and properness after completion

For each such pair of finite quotients form

    G_head=A1 *_(K/L) A2.

This ordinary amalgam is virtually finitely generated free and residually
finite. Here is an elementary verification. Let the two finite vertex
groups act on a common finite set by enough copies of their regular
actions. Their restrictions to K/L are isomorphic free K/L-sets;
identify those actions. The universal map to the resulting finite
permutation group is injective on both vertices. Its kernel acts
freely on the ordinary amalgam tree and is therefore free; it has
finite index and finite rank. Residual finiteness follows from that
of the free subgroup by taking finite-index cores.

Every finite quotient of the original G factors through one of these
G_head: apply the preceding construction to its two restricted kernels.
Conversely, any specified finite vertex quotient extends, after such
a refinement, to a finite quotient of G_head which embeds its finite
vertex images. Thus both Ri carry their full induced topology from G,
and both Rihat embed into Ghat. The abstract universal property then
identifies Ghat with the proper full profinite amalgam of the two
vertex completions over Khat. This argument does not assume residual
finiteness of the original unknown Ri.

## 3. Proposed centralizer upgrade using only the verified element case

Let tau be the selected cone in R1, of order two and odd orientation.
In every G_head its image is a nontrivial order-two element in A1,
and cannot be conjugate into the edge K/L, whose orientation is even.
The ordinary amalgam tree therefore gives

    C_(G_head)(tau_head)=C_(A1)(tau_head).

The full-completion step should use only the already audited
Boggi--Zalesskii prime-order ELEMENT centralizer theorem from B1,
not their nonsolvable finite-subgroup claim. Its hypotheses must be
rechecked explicitly here: G_head is virtually finitely generated free,
has virtual cohomological dimension one, and is good (the free
finite-index subgroup is good, and goodness passes to a finite-index
overgroup by the usual finite-index cohomology comparison). If that
verified element theorem applies in exactly this stated form, then

    C_(G_headhat)(tau_head)=C_(A1)(tau_head),

the latter finite group already closed. No profinite tree fixed-subtree
theorem would be needed for this step.

Now let g in Ghat centralize tau. Its images in every G_headhat lie in
the corresponding finite A1. These heads factor every finite quotient
of G. If g did not belong to the compact image of R1hat, some finite
quotient would separate it from that image; factoring that quotient
through a head would contradict its membership in A1. Hence g belongs
to R1hat, and necessarily

    C_(Ghat)(tau)=C_(R1hat)(tau).

The reverse inclusion is immediate. This is a full profinite upgrade
of the one-neck centralizer REDUCTION, not a computation of the right
side and not a global five-neck theorem.

## 4. Required next audit

Independently check the retractions on the slit ordinary vertex groups,
the fully invariant common-kernel construction, finite-head cofinality,
and the exact hypotheses/proof of the already audited prime-two element
centralizer theorem at this use. The claim in section3 remains a
proposal until this audit and primary-source check are completed.
The three natural mixed-neck edge maps are already noninjective, so
this lemma cannot be applied to them before their actual quotient-edge
groups and embeddings are determined. No arbitrary infinite-index
completion or nonsolvable centralizer equality is assumed.
