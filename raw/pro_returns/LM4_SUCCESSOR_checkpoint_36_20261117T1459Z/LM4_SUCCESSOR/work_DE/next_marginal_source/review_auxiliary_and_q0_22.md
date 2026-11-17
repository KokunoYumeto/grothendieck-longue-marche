# Independent auxiliary centralizer and actual old-base review

DE complete proof read of
`work_A/auxiliary_RAAG_HNN_centralizer22.md`: **PASS** on the explicitly
recorded primary dependencies.

The piling argument identifies the graph involution's fixed subgroup
by removing commuting first-letter pairs; only the four diagonal pairs
are eligible. Killing barred and auxiliary vertices gives the actual
free-four detector and the source topology. The finite Salvetti/type
argument and the stated goodness/prime-order theorem hypotheses are
kept separate from the combinatorial normal form. The full auxiliary
completion assertion uses the element-centralizer case, not a theorem
about arbitrary finite subgroups.

For the HNN completion, the finite exponent map gives exactly
\(N\cap E_i=mE_i\) after intersecting a prescribed normal finite-index
subgroup. This equality, rather than just containment, makes the two
edge kernels compatible under every prescribed clique isomorphism.
The finite-base heads preserve both edge embeddings and retain the
odd orientation of the selected cone. Their virtually free kernels
are genuine finite-index free groups. The cofinal finite-quotient
separation argument then forces every completed cone centralizer
element into the compact base vertex. No compatibility choice of
centralizer representatives or unproved profinite-tree injection is
used.

One actual marking precision has been communicated and accepted:
the root's stable letter satisfies

\[
p=w_{\rm root}^{-1}e w_{\rm root},\qquad
r=w_{\rm root}^{-1}\bar b w_{\rm root}.
\]

Hence A's convention
\(w_{\rm aux}^{-1}(p,r)w_{\rm aux}=(e,\bar b)\)
uses \(w_{\rm aux}=w_{\rm root}^{-1}\). This changes no centralizer
conclusion, but must be explicit when the actual presentation is
identified with the auxiliary one.

## Actual q0 saturation is strictly additional

The independent producer
`verify_inner_q0_HNN_independent22.py` imports no CE oracle. It uses
commuting-suffix cancellation for graph-group words, in contrast to
CE's dependence-piling implementation. Reduced support gives exact
coordinate-clique membership; the two literal HNN identifications
are checked before Britton reduction.

Its genuine output and `inner_q0_HNN_independent22.json` verify:

- all ten original full slit relators are trivial;
- all twenty signed actual (q=0\) images match the literal raw
  substitutions, and exactly nine in each direction remain nontrivial;
- the negative image of the beta33 contact relator has two stable
  letters after three exact pinches, with a surviving explicit
  nonmembership certificate between them.

That word is killed in the annular presentation, because it is a
conjugate of a slit relation by the actual retained base lift. It is
nontrivial in the proved slit HNN by Britton's lemma. Thus the slit
group does not embed unchanged into the annular group: the old-base
saturation is a real additional quotient. This is not a refutation
of any annular or global fixed-source equality. It only prevents
promoting the slit centralizer theorem by assuming stability of its
ten-relator kernel.
