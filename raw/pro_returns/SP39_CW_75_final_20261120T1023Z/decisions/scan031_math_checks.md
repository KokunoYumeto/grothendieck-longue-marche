# Targeted check of the group statement on scan 031

Statement N031.3: the alternating group on five letters is simple and nonabelian. The source additionally calls it the smallest nonabelian simple group; that minimal-order assertion is not covered by the following check.

The reproducible script scripts/check_A5.py enumerates all permutations of {1,2,3,4,5}, retains those of even inversion parity, and obtains 60 elements. Composition is explicit: (p∘q)(i)=p(q(i)). Membership of all 3,600 products and of all inverses is checked.

The script computes the conjugacy orbit of each still-unassigned representative by hgh⁻¹ for every h among those 60 elements. The complete conjugacy-class sizes are 1, 20, 15, 12 and 12, represented by id, (3 4 5), (2 3)(4 5), (1 2 3 4 5), and (1 2 3 5 4), respectively. It adjoins the identity to each class and repeatedly adjoins all products of present elements until the set stabilizes. Each of the four nonidentity classes generates all 60 elements this way. Conjugate elements have the same conjugacy class, so this covers every nonidentity element.

A nontrivial normal subgroup contains a nonidentity element, all of its conjugates and every product of those conjugates. The enumerated closure is the full group in every one of the four cases. Thus A₅ has no nontrivial proper normal subgroup.

The explicitly enumerated elements p=(1 2 3) and q=(3 4 5) satisfy p∘q=(1 2 3 4 5) and q∘p=(1 2 4 5 3); these unequal maps establish noncommutativity. The script’s complete small output is decisions/scan031_A5_check.json.

This is an exhaustive computation with the preceding elementary proof interpretation, not a proof-assistant certificate. It supplies no enumeration or classification of smaller finite groups and no verification of the proposed icosahedron/five-colour dictionary. It does not decide the handwritten capital’s alphabet or any transcription glyph.
