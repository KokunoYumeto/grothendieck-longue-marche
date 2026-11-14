# E106 complete root audit

**PASS.** The root auditor read the complete 420-line mathematical proof, the
complete final Python and GP programs, and the accompanying dependency and
source records. No mathematical correction was required.

The fresh copied reconstruction returned exit0. Its full Python stdout, JSON,
and GP stdout agree byte for byte with the frozen author files, with no excluded
fields. All six complete inputs and both mathematical sources were hashed before
and after execution. PARI recertified the retained B1 field and recomputed the
literal prime7/73 Frobenii. The root execution is `rebuild.py`, its actual stdout
is `rebuild.out`, and the complete comparison is `comparison.json`.

## Mathematical argument checked

1. The local norm/inclusion square fixes Gal(B3/B1)'s generator by its action on beta3, identifies Gal(B3/B2) with its third power, and divides the actual ninth-character matrix by three only after its restriction to E101's complete ordinary-unit norm lattice.
2. The literal E94 row weights are retained. The six cubic characters have rank4, and the full 19683-residue calculation supplies both finite coordinate inverses and all243 preimages of every image.
3. The ordinary FIELD-norm index81 is used in the ambiguous-class formula. E91's trivial vertical action then identifies the entire three-class group order243. Surjectivity of the actual ninth-genus quotient of that same order proves its isomorphism and W=0.
4. The prime-above-three class is followed through actual ideal norms; the horizontal norm and extension maps yield Cl(L3){3}=C9+C3, q3=3a3, and capitulation kernel<3a3>. The unramified capitulation formula then proves the ordinary horizontal unit norm is onto.
5. The two literal prime ideals over7 and73 are recomputed in the certified B1 field. Their Frobenii determine the claimed horizontal class coordinates, with all243 upper and81 lower coordinates checked.
6. The six S-prime class columns and the displayed principal S-divisor lattice have exact mutually inverse coordinate maps. Earlier actual principal powers establish full principality and remove any dependence on only a three-saturated lattice.
7. The vertical ordinary-unit obstruction is computed after the field-norm test using the exact strongly ambiguous class subgroup. The quotient and completed norm kernels follow with their actual torsion and free ranks.
8. The result determines the finite projection exponent a3=1. It asserts no value for the eventual all-level exponent h and makes no deduction about later transvections from equality of adjacent finite class groups.

## Primary-source checks

Milne's local cup-product compatibility, Hilbert-symbol definition and norm
criterion, complete unit Herbrand quotient proof, and complete cyclic Hasse norm
proof were read in the primary course notes. Lemmermeyer's ambiguous and strongly
ambiguous ideal-class arguments were read through their complete ideal/index
derivation. The exact sections and source limitations are recorded in `audit.json`.
The omitted printed local lemma proof and the notation slip in the ambiguous-class
article are recorded explicitly; the written E106 argument supplies the required
maps through the proved cup-product and orbitwise Hilbert90 constructions.

## Frozen metadata and historical stdout

The refreshed 36-file manifest was checked in full. It changes historical-output
provenance only: the mathematical proof, final programs, inputs and final outputs
retain their audited hashes. The unchanged exploratory wrapper was actually rerun
in an isolated copy. Its new stdout is labelled as a fresh replay, and its complete
arithmetic stream is byte-identical to the retained stream. The preceding author
freeze and manifest remain available. This audit's `finish.py` performs and records
these metadata checks; its actual stdout is `finish.out`.

No separate peer result is asserted. The eventual all-level exponent h and the
unrestricted portions of E.23 remain active.

## Archived paths

The exact historical audit drivers retain their original staging paths. The main owned source is code/e_next_unit_characters.py, its GP source is adjacent, and all six required inputs are in the archive's inputs directory. No previous audit output is overwritten by this integration.
