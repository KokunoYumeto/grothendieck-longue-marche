# Primary readings and the bounded orbit-configuration bridge

## Purpose and search scope

After the actual annular centralizer proof, we searched for a theorem
that could establish goodness or a free-group tower for the complete
surface, bypassing the remaining neck quotients. Queries concerned
orbit configuration spaces, finite Mobius groups, poly-free fundamental
groups and the actual moduli setting. A second search verified the
primary records and located the revised 2026 paper below. This bounded
search is not a claim that no applicable theorem exists.

## Primary records opened

Maassarani, M. (2021). Algebraic invariants of orbit configuration spaces
in genus zero associated to finite groups. *Topology and its Applications,
302*, Article107847. https://doi.org/10.1016/j.topol.2021.107847

We opened the primary author PDF https://arxiv.org/pdf/2007.01352 and
its arXiv metadata. We read the introduction, the hypotheses and definition
in Section2.1 (printed page10), and the displayed fibration consequences
in Section5.1 (printed pages24--26). Its setting requires a finite group
action on a punctured sphere with the removed set invariant and containing
the irregular points. We did not establish that identification for our
surface, and do not use its group-structure conclusion here. This is a
scope check, not a claimed full audit of every theorem in the paper.

Roushon, S. K. (2026). A four-term exact sequence of fundamental groups
of orbit configuration spaces. *European Journal of Mathematics,12*,
Article37. https://doi.org/10.1007/s40879-026-00912-6

We opened https://arxiv.org/abs/2502.19853,
https://arxiv.org/html/2502.19853v2 and its complete PDF endpoint.
The primary metadata records revision2 dated16 April2026 and the
published journal reference. We read Definition1.1, the standing action
hypotheses, Theorem1.5 and the discussion of nonfree actions and the
four-term sequence. The hypotheses include an effective properly
discontinuous action on the specified surface. The current statement
retains a kernel term for nonfree actions; we do not replace it with a
short exact free-fiber sequence. No theorem of this paper is applied to
our actual surface, and no complete proof audit is claimed here.

Root retrievals: turn951search0/turn951academia25/27/29 (discovery),
turn952view0/1 (primary metadata), turn953view0/1 and
turn954view0--4 (primary scope, definitions and stated consequences).
No full third-party source is copied into the checkpoint.

## The actual coordinate shortcut fails for an exact reason

The actual Z of B106, in its given (v,w) coordinates, removes among
its graph divisors

    w=g1(v)=u/v,
    w=g2(v)=1-u+u/v,

for every nontrivial fifth root u. Both appear literally in the
supplied equations. But g1 is an involution and

    g2 composed with g1(v)=v+1-u.

This is a nonidentity translation of infinite order. Thus these
listed maps cannot be contained in a finite Mobius group. More
strongly, the finite actual forbidden graph family is not closed
under this composition. For a primitive fifth root u, the point

    (v,w)=(10,11-u)

is in the actual Z but satisfies w=(g2 composed with g1)(v).
The exact producer code/check_orbit_configuration_bridge23.py checks
all actual excluded factors modulo the fifth cyclotomic polynomial;
its genuine output and records/orbit_configuration_bridge23.json
are retained. This verifies the scope obstruction without a numeric
picture. The coordinate domain itself is a sphere minus finitely
many points, and g2 does not preserve that puncture set either.

Consequently the direct orbit-configuration identification in these
coordinates does not meet either paper's hypotheses. This does not
refute an unidentified topological, birational or group-theoretic
replacement. No formal main-task decision, source equality or goodness
claim follows from this failed bridge. We continue with the exact
annular-neck presentation and its actual based maps.
