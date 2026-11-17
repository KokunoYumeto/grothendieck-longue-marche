# Root review: C.39, symmetric-four generation and relative pro-two levels

Reviewed 16 November 2026, approximately 06:07–06:09 UTC. Accepted in
the full peripheral scope stated. We read the entire formal proof and
independently reran `work_CE/code/check_C39_S4.py`; all checks passed.

The symmetric-three step really covers every epimorphism, including
the mixed reflection/rotation cases. The earlier dihedral result is
needed only for the two-reflection case. Each ordered generator-type
possibility is one automorphism orbit, so the kernel is preserved by
the canonical substitution, all unit-power versions, and both involutions.
This establishes descent to the specified actual relative completion.

For S4, every proper subgroup still surjecting onto S3 is one of the
four self-normalizing point stabilizers. A retained element of order
four excludes such a subgroup immediately. The two remaining ordered
passports (2,3,4) and (3,2,4) are single inner orbits; the full negative
automorphism consequently descends and is inner. If the substituted
pair were in a point stabilizer, the inverting element would be its
order-two generator. One of the two relevant section images would
then be central. The full cusp-incidence triangle makes the third
cusp a product of two involutions with one central, contradicting
its order four. This argument needs the full section incidence, not
merely a finite norm equation or a list of candidate pairs.

The separate certificate checks all 30 subgroups and 216 generating
pairs in nine inner orbits. After the S3 condition, it finds exactly
12 improper candidates, all eliminated by that central-section argument.

The relative argument is correctly phrased through a finite quotient
of the actual relative pro-two group; it does not assume that the
substitution descends to every finite quotient. A hypothetical proper
image yields, after the two-group Frattini quotient and the normal
intersection with its image, a split module extension of S3. Passing
to a simple module quotient gives either C2 x S3 or S4. The former
contradicts the invertible mod-two abelianization of the substitution;
the latter contradicts the proved S4 generation theorem. The two
simple F2[S3] modules exhaust the possibilities. Surjectivity plus
finite-generation Hopficity gives the asserted relative automorphism.

No GT0 duality, hexagon or pentagon is used. The conclusion applies
to every peripheral involution, but remains an unmarked conjugacy
statement on the indicated relative completions. Preservation of the
relative third cusp and universal full conjugacy are not concluded.
