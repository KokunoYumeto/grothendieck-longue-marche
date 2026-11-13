# Independent audit of D.65

**Result: PASS.** I read the complete written proof, the metadata, the new bibliography entry, and the exact certificate. I reopened Martino's complete author version and checked the theorem actually used. No mathematical correction is required.

## Exact discrete presentations and axis arguments

The HNN presentation uses the two specified reflection subgroups of the finite dihedral group of order \(2n\). Eliminating \(c\) gives precisely \(c=[g,v]\), and the converse relation \(v[g,v]v=[g,v]^{-1}\) follows from \(v^2=1\). The exponent character \(\ell(g)=1\) proves that the amalgam edge map from the infinite cyclic group is injective. The displayed maps between this amalgam and \(G_n=\langle z,v\mid v^2,[z^2,v]^n\rangle\) invert each other.

The length-one argument does give the complete conjugacy calculation. Both axes contain the vertex \(D_n\), and every vertex on either axis is in one orbit of its length-one translation. Thus a conjugator can be adjusted by a power of the target translation to lie in \(D_n\). Britton reduction then forces this vertex conjugator into the named subgroup \(\langle v\rangle\), giving exactly \(r=0,-1\pmod n\).

For a disallowed residue, the exponent character excludes conjugacy into any other power of the amalgam edge generator. Hence \(c^r g\) fixes exactly the \(H_n\)-vertex of the amalgam tree, and its centralizer lies in \(H_n\). In the HNN tree the same axis adjustment reduces a centralizer element to the vertex subgroup. Britton again leaves only \(1,v\), and
\[
(c^r g)v(c^r g)^{-1}=c^{2r+1}v
\]
excludes \(v\) under the stated unit condition. This proves the entire discrete centralizer, not just its cyclic subgroup. The trees used here are ordinary discrete Bass--Serre trees.

## Actual surface cover and primary theorem

The parity kernel is exactly the torus cone presentation with \(X=zv\), \(Y=vz\). The inverse map \(z=Xv\) and the involution swapping \(X,Y\) verify the full semidirect product presentation. The finite Heisenberg quotient has order \(n^3\), with boundary commutator of order \(n\). Its covering surface therefore has \(n^2\) boundary components of degree \(n\). Filling them kills exactly the Reidemeister--Schreier conjugates of \([X,Y]^n\), producing the stated closed surface group of genus \(1+n^2(n-1)/2\), of index \(2n^3\) in \(G_n\).

Primary source independently reopened:

Armando Martino, *A proof that all Seifert 3-manifold groups and all virtual surface groups are conjugacy separable*, complete author version, 21 April 2005:

https://ddd.uab.cat/pub/prepub/2005/hdl_2072_1728/pr627.pdf

Theorem 3.7 on printed page 5 applies to every group having a surface subgroup of finite index. The definition on printed page 3 includes the closed hyperbolic surfaces constructed here. Applying the theorem separately to every finite-index subgroup of \(G_n\) is valid, because its intersection with the displayed surface subgroup is again a finite-index closed surface subgroup. Lemma 2.1 also supplies the stated full induced topology for finite-index subgroups. The source was reopened as web reference turn805view0.

## Completion bridge and square obstruction

The proof of completed centralizer equality is correct and does not interchange arbitrary closures and intersections. For \(x=h\widehat n\) centralizing \(a\), the actual elements \(a,h^{-1}ah\) lie in the finite-index group \(N\langle a\rangle\) and are conjugate in its full completion. Conjugacy separability in that group gives a conjugator \(na^k\); hence \(hn\) centralizes \(a\) and approximates \(x\) modulo the chosen open normal subgroup. Intersecting these neighborhoods is exactly the definition of the closure of the discrete centralizer.

The exponent character \(\vartheta(z)=1,\vartheta(v)=0\) sends \(c^r g\) to \(2\). Therefore the map from the full \(\widehat{\mathbb Z}\) onto its procyclic closure is injective, since its composite with \(\widehat\vartheta\) is multiplication by \(2\). A square root would commute with this element, belong to that full procyclic centralizer, and solve \(2t=1\). The allowed residues have the explicit discrete square roots \(z\) and \(vzv\). This proves both directions of the exact criterion.

## Application to all units and both reflection labels

Each \(q_n:E_1\to\widehat G_n\) is the actual continuous quotient given by the named generators; the discrete image is dense and the source is compact. For the first label, reducing \(r=(\mu-1)/2\) modulo every \(n\) gives the exact integer input to the square criterion. The resulting congruences modulo \(2n\), over all \(n\), force one global sign by compactness of the two-point set \(\{1,-1\}\).

For the second label the displayed inverse-and-conjugation identity is correct:
\[
g^{-1}\big(c^{(\mu+1)/2}g^{-1}\big)^{-1}g
=c^{-(\mu+1)/2}g.
\]
It is a square whenever the original element is a square, and it is the first-label expression for \(-\mu\). Combining this with D.64's actual character injection and its four exhibited elements proves the stated full Klein four centralizer. The final scope retains the unresolved exhaustion of arbitrary negative-involution conjugacy classes.

## Executed verification

I reran the producer successfully. Captured stdout is in work/part_a/d65_audit_stdout.txt.

- 80 exact free-product word identities;
- 8,382 dihedral calculations;
- 6,716 unit-residue centralizer exclusions;
- 18,495 Heisenberg inverse-coordinate calculations;
- all 15 covering cases \(2\leq n\leq16\), with the displayed boundary degrees, indices, and genera.

The certificate checks the finite presentation and covering identities. The full profinite square criterion is justified by the separate tree, surface-cover, and hereditary-conjugacy-separability proof audited above.
