# Twenty-fourth-hour research report

INCOMPLETE. Both main full decisions remain Open. This interval continues
the actual icosahedral source-centralizer route, with every comparison
restricted to its named group and topology. We have not restarted the
stopped affine/metabelian census or the two unresolved solver jobs.

## Formal progress: B115--B117

B115 proves that the actual prefix substitution on the common neck
K=F(a,B,d,e,f) has no extension to the unchanged regional group R that
sends its base generator k to an ordinary element of odd geometric base
winding. The proof uses an explicit quotient of the full seventeen-relator
regional presentation onto (F2)^12 semidirect S3, of order 24576. The image
of theta(a)=aB has trivial centralizing permutation part. The permutation
sign equals the original ordinary-cover character plus geometric winding
modulo two. These are actual characters of R, not the auxiliary height
or graph-color characters. The quotient argument proves the same assertion
in full profinite completion. It also excludes all conjugates of k and
their corrections by the closed normal closure of the four deleted
families. It does not assert that this quotient survives the two cross
relations, or forbid a change of generators with all relators transported.

B116 supplies an intrinsic discrete obstruction independent of the
proposed image of k. Using the complete infinite regional graph and a
direct HNN centralizer proof, we compute

C_R(a)=<a> times (Z^2(b,k) * F(CaC,CdC,CeC)),
C_R(aB)=<aB> times F(b,CaC).

Their abelianizations have ranks six and three. Consequently no discrete
automorphism of R sends a to aB, and no such automorphism extends the
prefix substitution. All ten edge types and every height/translate are
retained. The proof is a complete special-case argument; it does not cite
an unread general graph-group centralizer theorem. No formula for either
infinite-order centralizer in the full profinite completion is asserted.

B117 identifies the actual subgroup L=<K,k> inside the ordinary regional
group as a retract. Its presentation is

L=<h,k,V1,...,V4 | [h^2,k], [k,Vi]>,
(V1,...,V4)=(a,d,e,f^-1 B f),  h=fk.

The retraction is proved on the entire regional graph by its two colors,
not on a finite truncation. For the auxiliary character h->1 modulo two,
the kernel is the eleven-vertex, ten-edge tree graph group with generators
t=h^2, k0=k, k1=hkh^-1, Vi, hVi h^-1. The actual index-two neck subgroup
has rank nine and retains F=f^2=k1^-1 t k0^-1. Replacing F by the coordinate
t would change the embedded subgroup and is not done. Actual retractions
and finite index prove all stated full induced profinite topologies.
The auxiliary character is not identified with the geometric ordinary cover.

All three formal sources have complete root and independent reviews.
Their integrated copies are byte-identical to the reviewed frozen drafts;
hash bindings are in checkpoint24_root_formal_reviews.json and
checkpoint24_formal_source_copies.json. The final paper has 286 statements:
242 Proved, 19 Refuted, 19 Open and 6 Known. All 49 task/lead rows remain.

## Actual full-boundary and corner research

The exact actual selected cone is c=aCa^-1. The physical ordinary boundary
prefix is P5=aBfde, so the full boundary is

T=cP5=a b z d e k^-1,  [k,T]=1.

In the full mirror presentation set D=j c j and u=T D. The complete
fifth-prefix mirror equation becomes juj=u^-1, and the actual cross
commutator together with [k,T] becomes [k,D]=[k,u]=1. This isolates the
proper discrete cyclic amalgam

((C2(D)*Z(u)) times Z(k)) *_{Z(u)} (Z(u) semidirect C2(j)).

The entire actual group still has fifteen further explicit relations in
the eight-generator, twenty-four-relator transformed presentation: five
generic relations and all ten actual node words. The six actual source
words and both independent characters are transported literally. The
executed producer checks all sixteen inverse generator compositions,
fourteen literal retained-relator comparisons, the boundary commutation
steps and the six source words. Its ordinary normal-form reductions are
not used as an oracle for the quotient by those fifteen further relations.

The isolated corner's j-even subgroup is the graph product on the path
D--k--u--k'--c, with endpoint groups C2 and three infinite cyclic interior
groups. Its discrete centralizers are computed exactly. The common
subgroup <c,k,T> is C2*Z^2 by the ordinary amalgam normal form. Its full
induced topology in the corner also has a direct index-two retraction
argument, recorded in the root boundary proof candidate.

The older triangle of the regional group, mirror vertex and elementary
cross corner has shortest alternating relation lengths 4,4,8. Its angle
sum is 5pi/4. A sufficient nonpositive-angle theorem cannot be invoked
from that calculation; no nondevelopability conclusion is inferred.
Even after filling all deleted families, two nontrivial relations remain
in the j-even corner, namely [c,uDk] and [D,u^-1 c k']. They form one
mirror orbit in the full corner. Thus the corner is not silently equated
with the actual coarse bundle.

An additional exact branch-parity argument explains why the original
branch peripheral class cannot be replaced by an eta-inverted lift with
the same mod-two peripheral vector. In K semidirect_eta C2, a free product
of six involution groups, such a lift would give an involution whose
abelianization has three nonzero factor coordinates. Discrete and full
profinite free-product torsion force a single coordinate. The useful full
prefix changes that fine parity. This is not an obstruction to the valid
complete presentation change above.

Primary research records and genuine output:
work_A/actual_boundary_corner_presentation24.md,
work_A/annular_boundary_corner24.json,
work_A/code/compile_annular_boundary_corner24.py/.out/.err,
work_DE/next_marginal_source/actual_mirror_triangle_and_boundary_corner24.md,
work_DE/next_marginal_source/check_boundary_corner24.py/.out/.err.

## Regional boundary subgroup: a further concrete comparison

The root candidate records an exact quotient R_e retaining one deleted
family. Its auxiliary C-parity kernel is the graph group on the five-cycle
k--z--K--E--e--k. This character is explicitly different from the ordinary
cover character. The selected c maps to C and T maps to z e k^-1.

Put r=e^-1 E and s=z e. The four-vertex path group is
F(k,K,r) semidirect_alpha Z(e), with alpha fixing k,r and sending
K to r^-1 K r. The remaining z relations give a proper HNN group J
over F(k,K,r), with edge <k,r K r^-1> mapped to <k,K>. Replacing r by
s^-1 q identifies J as Z^2(k,s)*Z^2(K,q), where q=zE. A second proper
amalgam embeds J in the five-cycle graph group. The involution swaps its
two free factors. This yields an explicit candidate proof that the actual
regional <c,k,T> is C2*Z^2.

The full-topology argument takes an arbitrary finite quotient
of J, refines its restriction to the finitely generated free base by a
characteristic finite-index subgroup, and uses finite graphs of finite
groups to extend the quotient. It is not an inference from residual
finiteness alone or from a noncofinal sequence. A direct finite permutation
construction supplies the needed finite-graph residual-finiteness step.
The full note is records/pentagon_hnn_boundary_proof_candidate24.md.
Both DE and A independently read its complete proof and passed the
discrete embedding, full induced topology, corner retraction and the
additional exact discrete intersection K intersect <c,k,T>=<P5>.
The latter uses a second actual HNN presentation over C2*Z^2 and a
nonzero stable-height test for every power of P5. At that review time
the completed intersection remained separate; the subsequent retraction
addendum below closes it. Exact source/review hashes
are retained in the late-review audit; no additional numbered theorem
is added in checkpoint24.

Even if this common-subgroup comparison is verified, properness of a
corresponding full profinite amalgam and survival through the remaining
four actual prefix mirror relations are separate questions. We do not
swap a closure with an intersection or infer a post-cross centralizer.

## Actual ordinary cover and the coarse bundle

The CE compiler starts from every relation of the actual nine-generator,
thirty-six-relator annular presentation and changes both cone gauges to
the selected cones. The universal ordinary kernel is free of rank fifteen
before regional relations. The two actual cross relations eliminate
precisely two barred base generators, leaving thirteen generators and
sixty-four regional relators. Both selected-cone involutions, every
inverse marked-generator comparison and all six source words are retained.

Filling exactly the eight deleted-family generators leaves the actual
five-generator coarse quotient. Eight remaining relators give an explicit
F3(f,g,x) semidirect F2(kminus,kplus) presentation. The positive actions are

kminus: f -> f^-1 g f, g -> f, x -> x g^-1 f;
kplus: f -> f x g x^-1 f^-1,
       g -> g x^-1 f x g^-1, x -> f x g^-1.

Both inverse automorphisms and every filled relator are checked by exact
free reduction. The complete converse presentation is now proved in
work_CE/annular_ordinary_and_coarse_comparison24.txt. A separate literal
source replay gives the six source images exactly as
(1,1,1,1,f^-1 kplus,kminus). Both surviving lifts are fixed by the actual
selected plus cone. They freely split the base, and the fiber fixed
group is trivial by the factor-centralizer computation in C2*C2*Z.
Thus the coarse ordinary fixed subgroup is exactly
F(kminus,f^-1 kplus), also in full profinite completion. The fiber has
full induced topology by its cofinal characteristic finite quotients;
the completed extension remains split. Root read the complete proof and
both producers. No splitting or fixed-lifting assertion through the
unfilled-family kernel is made.

Records: work_CE/code/compile_annular_ordinary13_24.py/.out/.err,
work_CE/next_symmetric_nodes/annular_ordinary13_24.json,
work_CE/code/check_annular_coarse_source24.py/.out/.err and
work_CE/next_symmetric_nodes/annular_coarse_source24.json, together with
the complete companion proof above. Its final independent review is
recorded in the capture audit.

## Sources, typesetting and archive preservation

No bibliography entry was added this interval. The original Servatius
centralizer paper was sought: author abstract and publisher metadata were
opened, but the full original proof was not obtained. B116 instead gives
its complete direct proof. A mistakenly guessed unrelated arXiv identifier
was rejected, not used as evidence. Existing primary dependencies retain
their precise opened-source scope. All 111 bibliography entries are printed.

The first combined build is clean in 450 pages. Initial/final overfull
counts are 0/0, with no warnings, undefined references or errors. Fresh
visual review covers five contact sheets spanning 39 pages and 15 pages
opened individually, including all new mathematical pages 352--361.
Exact QA and PDF hash are in checkpoint24_typesetting.txt and
checkpoint24_visual_review.json. A truncated multi-image tool output was
not counted; every contact sheet was opened separately afterward.

Checkpoint24 uses a standard TAR of historical/preview PDFs, compressed
as a ZIP-LZMA member, in addition to the existing standard PNG TAR.
The current main PDF stays directly in the ZIP. All original logical
paths and bytes remain in the manifest. Compatibility was checked against
the actual immutable checkpoint23 without creating an extra ZIP. A fresh
workspace estimate includes the new renders and prospective PDF history,
with a five-million-byte allowance. Both actual containers will be
restored independently with native tar after capture. Earlier archives
are never modified, renamed, deleted or overwritten.

The UTC date rollover interrupted the three research agents; all three
were explicitly resumed and that fact is recorded in
records/date_rollover_research_resume24.json. A later single executor
transport failure was followed by a successful same-directory command;
no workspace loss was observed. At 00:41 a further status check found
all three agents interrupted; they were explicitly resumed again, and
the final proof/review work was saved. No causal link between these
interruptions is assumed. Exact records are late_research_resume24.json
and the computation audit. Operational interruptions are not represented
as completed calculations.

## Decision and next mathematical gate

### Final addendum: the full completed boundary/neck intersection

Before capture, root found a direct retraction in the same actual
one-family quotient R_e: send C,k to 1, z to the actual f=C z k^-1,
and e to e. This is a genuine retraction onto K_e=F(e,f), and it
sends the embedded H_e=<C,k,z e> onto <p=f e>. It follows directly
in the completed groups that K_ehat intersect H_ehat=closure(<p>).
The actual quotient sends K onto K_e and is injective on the completed
boundary subgroup by the already reviewed full-topology argument.
Since q(P5)=p, pullback proves

Khat intersect <c,k,T>hat=closure(<P5>) in Rhat.

No exchange of closure and intersection is used. The complete proof is
records/completed_boundary_neck_intersection24.md. A independently
checked the marked retraction, all five quotient relators, both actual
subgroup images and the completed pullback, and passed them in a
read-only review before capture. No agent file or producer was started.
The response and exact source hash are retained in
records/checkpoint24_completed_intersection_review.json. This addendum
supersedes the earlier research status that left this one intersection
open. It creates no new formal row in the frozen 286-statement paper.

We continue. The three formal actual-group results and the exact further
boundary/ordinary-cover comparisons constitute substantive progress on
the Main-B route. The remaining target is the selected source centralizer
in the full unfilled annular group after both cross relations, followed
by the other necks and the proved global/joint-source transfer. Main A's
full involution-conjugacy decisions also remain Open. No partial regional,
coarse, finite or pro-prime calculation is a decision of either main claim.
