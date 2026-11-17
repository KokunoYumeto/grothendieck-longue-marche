# Root review: canonical generation in every A5 quotient

Reviewed 2026-11-16, approximately05:38–05:43UTC. Status: accepted for
formal promotion AFTER checkpoint05, whose paper remains frozen at187
statements. The working proof and both exact certificates are retained.

We read work_CE/research_A5_generation.txt and the independent DE review,
checked C35's full duality identity and C28's section labels/incidence,
read the matrix certificate, and reran check_a5_duality_orbits.py. Its
actual output reports2280 generating pairs in19 Aut(A5)-orbits. Among342
proper-image candidates satisfying the indicated binary constraints,
108 have no required inverting inner involution,208 contradict the
third-cusp section incidence, and26 contradict the one-section lemma.
These are necessary conditions on an actual full word, not an existence
enumeration of full words. DE independently checked the finite structure
with permutations and no imports from the matrix implementation.

The kernel-stability issue is essential: before using an induced alpha,
the finite certificate checks every possible negative conjugating
parameter subject to the actual third-peripheral conjugacy class. It
does not infer stability from generator orders. In each required case
the induced action is inner. Swap stability and the distinction between
the two five-cycle classes are also checked before defining finite v.

For the full maps, v=Inn(u^-1)iota is an involution by duality and
commutes with alpha by iota*alpha=Inn(f)*alpha*iota and alpha(u)=f^-1u.
Thus tau=alpha*v is an involution with regular mod-two homology. It
inverts the third peripheral class. The local correcting conjugator
produces an actual reflection: its square lies in the full procyclic
centralizer of the primitive cusp, and inversion forces that square
to be one.

We reopened Kochloukova and Zalesskii(2007), primary author manuscript,
https://mat.unb.br/~pz/arquivos/Claus3.pdf, Theorem2 and Section1.1,
manuscript pp3–4. The theorem applies to full profinite groups with an
open subgroup of finite cohomological2-dimension and no C2². Those
hypotheses hold here. The high-degree restriction to order-two subgroup
normalizers is a dense embedding; finite-dimensional source makes it
an isomorphism. The regular homology module and split Hochschild–Serre
sequence give dimension1 in every degree at least2. Each section
normalizer contributes at least1, proving exactly one section class.
No assertion that its geometric centralizer is trivial is needed.

Consequently, when tau acts identically on a finite quotient, every
section maps to the same central involution. The two third-cusp
reflections then force the cusp image to be trivial. This excludes the
last cyclic-collapse cases. In the plus case the binary argument is
valid despite central signs in chosen matrix lifts: u is in full F′,
so central changes to either input do not affect its evaluation, while
each lift of a projective involution squares to−I.

Conclusion: every continuous epimorphism F→A5 stays onto after canonical
substitution for a full GT0 involution. The conclusion is confined to
individual A5 quotients. It does NOT yet prove surjectivity to their
complete joint head A5^19, any relative completion over that head,
the A5 third-cusp test, full generation or full conjugacy. A map could
in principle merge distinct kernel orbits; that next issue was sent
to CE explicitly. No additional finite test has been silently treated
as a full profinite conclusion.
