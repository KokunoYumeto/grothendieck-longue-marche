# Root reverse derivation of the actual annular candidate relations

Late research after the formal B108--B111 build. This is a complete
algebraic derivation to be independently checked against the actual
ten adapted records. It has been sent to A. No new formal row or
annular centralizer conclusion is claimed by this note.

Use the actual common adapted basis a=Y1,b=Y2,c=Y3,f=Y4,d=Y5,e=Y6.
Write bar(x)=cxc and h for the actual even c-source stable generator.
In THIS note k=f^-1 h=g0, the retained far-section generator. This
k is the variable called l in annular_generic_graph_presentation22.md;
it is not that note's different odd generator h*c.

The exact generic relations become

    c^2=1, [h,c]=1, h k h^-1=bar(k),
    [k,a]=[k,b]=[k,d]=[k,e]=1,
    f=h k^-1.

These are equivalent in both directions to the source-action relations
already certified on all six adapted generators. Set p=h d h^-1 and
q=h e h^-1 when the following calculations introduce them.

## 1. Seven relations before the last pair calculation

The beta11 word is [b,bar(b)^-1], equivalent to [b,bar(b)]. The
beta33 and beta44 words give [d,bar(d)] and [a,bar(a)]. The first
node at alpha14 gives [a,b]. The beta34 node gives [bar(a),d].
Thus these five relations are established before any subsequent use.

The beta24 node is [a,bar(d)bar(e)bar(d)^-1]. The c-image of
[bar(a),d] is [a,bar(d)], so the node is equivalent to [a,bar(e)],
or to its c-conjugate [bar(a),e]. Whole-relator conjugation is
retained in this equivalence; no individual whisker is erased.

For the other node at the shared alpha14=beta23 value set

    C'=f^-1 c f = k c k^-1.

The equality follows from f=h k^-1 and [h,c]. Its raw two adapted
peripherals are d and d^-1 C' d e d^-1 C' d. Conjugating the entire
commutator by d gives [d,C' d e d^-1 C']. Since k commutes with
d,e, this is equivalent to [d,bar(d)bar(e)bar(d)^-1]. The already
proved d-diagonal reduces it to [d,bar(e)]. This proves the seventh
relation without using the e-diagonal.

## 2. The remaining contact diagonal

In the beta22 cone peripheral the middle word is

    c b^-1 c b^-1 c b c b c.

Its ordinary part is bar(b)^-1 b^-1 bar(b)b, followed by c. The
already established b-diagonal therefore reduces it to c. The cone
peripheral becomes

    e^-1 d^-1 f^-1 c f d e.

As above f^-1 c f=k c k^-1. Since k commutes with d,e, the whole
contact commutator is equivalent to

    [e, d^-1 c d e d^-1 c d].

The second entry is d^-1 bar(d)bar(e)bar(d)^-1 d. The d-diagonal
and [d,bar(e)] remove d and d^-1 from that conjugation, leaving
bar(d)bar(e)bar(d)^-1. The c-image of [d,bar(e)] says that e
commutes with bar(d), so this contact relation is equivalent to
[e,bar(e)]. All relations used were established earlier; there is
no circular appeal to the desired full graph.

## 3. The beta12/beta13 pair

Set X=d e d^-1 and V=f^-1 b f. In their common adapted peripheral,
the middle word c b^-1 c b c b c reduces to b using the b-diagonal.
That peripheral is therefore u=X^-1 V X. The two nodes, up to
whole-relator inversion, are

    [X,u], [u,d].

Whole conjugation by X makes these equivalent to

    [X,V], [V,X d X^-1].

Since f=h k^-1 and k commutes with d,e, whole conjugation and
removal of k make the pair equivalent to

    [h X h^-1,b], [b,h(X d X^-1)h^-1].

Put p=h d h^-1, q=h e h^-1 and X'=p q p^-1. This is

    [X',b], [b,X' p X'^-1].

The first relation removes X' from the conjugation in the second,
giving [b,p]. Then the first is equivalent to [b,q]. Conversely
[b,p] and [b,q] recover both displayed relations. This establishes
the full reverse implication, not just a homomorphism into a group
in which the nodes happen to vanish.

## 4. Redundant graph edges and the actual HNN form

The ten physical relations are therefore equivalent, after the exact
generic substitutions, to the four diagonals for a,b,d,e and

    [a,b], [bar(a),d], [bar(a),e], [d,bar(e)], [b,p], [b,q].

Adjoin p=h d h^-1 and q=h e h^-1. We may add the following base
relations because they are h-conjugates of already proved ones:

    [p,bar(p)], [q,bar(q)], [p,bar(q)],
    [bar(k),p], [bar(k),q].

Their c-conjugates are retained as well. Eliminating p,q recovers
exactly the original relations, so these additions are redundant.
Together with the generic [k,a/b/d/e] relations, the base is the
fourteen-vertex,thirty-two-edge graph group semidirect C2 in CE's
candidate. The full associated subgraphs on

    {k,bar(k),d,bar(d),e,bar(e)}
and {k,bar(k),p,bar(p),q,bar(q)}

are isomorphic under k↦bar(k),d↦p,e↦q, with c fixed. Coordinate
retractions prove their ordinary full-subgraph inclusions. The
orbifold associated groups include c; this is not an even-edge
HNN as in B110. It has the marked stable direction

    h<c,k,d,e>h^-1=<c,bar(k),p,q>.

The next step is to compare this algebraic argument with the full
actual word certificates and construct its exact infinite graph
unfolding. The height h↦1,k↦0 is a new presentation character;
it is NOT the original geometric q0 character, which sends h and
k=g0 both to1. No topology claim about that geometric cyclic cover
is made here.
