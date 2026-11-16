# Root full audit of A.76: cyclic index two and odd abelian factors

**PASS.** Root read the complete written candidate and its full certificate
source, reran all 3,101 consistent presentations, and obtained byte-identical
JSON. The A.75 dependency has separately passed full root and DE audits.
Canonical integration remains deferred until after checkpoint15 is saved.

The actual extension presentation has the two necessary consistency
congruences k^2=1 and (k-1)h=0 modulo2^a. It is sufficient for the
classification argument because the given group already has exactly the
number of normal forms allowed by those relations. Changing the outside
generator changes h by (1+k)b. For a at least3 the valuation argument
gives the four possible roots of one, and the displayed gcd computations
give exactly the dihedral, quaternion, semidihedral and modular cases.
The abelian cases distinguish odd and even h. The separate a=0,1,2
discussion retains the trivial/cyclic, V4, D8 and Q8 cases. The image of
the cyclic subgroup proves that the class is closed under quotients.

The coprime product argument applies to the actual covering subgroup and
normal quotient kernel: suitable powers isolate the two coordinates.
Thus the actual odd abelian factor is an unramified elliptic isogeny,
and its field is linearly disjoint from the actual two-power intermediate
field. This identifies the connected compositum and its cusp pairs.
There is no unsupported choice of a component with a convenient genus.

For a nonabelian closure, the four already audited families supply good
Jacobian reduction, rank zero and actual cusp torsion, hence the stronger
rational joining-path property. The proof correctly retains that property
instead of attempting to pull a fixed-element equality through a finite
cover. A genus-one intermediate is handled independently as an unramified
elliptic cover.

The map to the good elliptic model is the extended relative Abel map
composed with the actual Jacobian homomorphism. This construction works
through nodes and inserted rational components. The odd isogeny extends
finite etale because its kernel has order prime to two. The resulting
model is the actual connected semistable pullback. Its compact type is
proved separately from the nilpotent total closure and its Jacobian norm;
it is not deduced merely from finite etaleness of a pullback of a tree.

Every selected rational joining subtree maps constantly to the origin.
Pulling it back along the good odd isogeny gives literal disjoint copies
indexed by the reduced odd kernel. The chosen cusp determines a copy
containing a distinct companion cusp. Contraction of rational unstable
components preserves a rational joining path, and the independently
established tree property makes it the path required by A.42. The final
normalizer argument uses A.59 at its nilpotent-closure scope. Finite field
extensions, packet restriction and inner base-point ambiguities remain
the ones proved in the earlier geometric criteria. No zero-rank statement
is claimed for the whole odd pullback, and no cofinality is inferred.

## Exact sources and execution

Root freshly reopened Dupuy--Rabinoff, Theorem1.1 and Proposition3.2,
including their extension through nodes and componentwise Abel-map
description: <https://arxiv.org/pdf/1705.03034>, retrieval references
`turn1200view0` and `turn1201view0`. The full nilpotent-cover hypotheses
were freshly checked in the A.75 root audit at Lehr--Matignon
Theorem6.13, `turn1198view0`. These are the precise external geometric
inputs. The elementary group classification is proved in the draft.

The complete candidate hash is
`b271501e3966da29889faf5297c0a4654c59acc72ab2aeef968dbea59bd88f87`.
The independently executed source has hash
`185baad9a7af3bec5d8954a23a70e3dbf1ef5769d839c6dbb1f1575808315c02`.
The whole output has hash
`de60bb36f2fb0d19d1487d1420e7c69bb6096f2688b6942413372a01e504cb25`.
All eleven levels through cyclic subgroup order1024 passed. The exact
runner and outputs are retained under `code/root_A76_certificate_rerun.py`
and `notes/root_A76_certificate_*`. DE independently read and reran the
same complete proof and certificate. The finite range supports the
uniform classification; it does not replace the structural proof.
