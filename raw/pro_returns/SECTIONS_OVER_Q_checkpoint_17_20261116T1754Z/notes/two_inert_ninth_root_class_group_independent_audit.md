# A206 complete independent proof and certificate audit

Reviewer: local_preprint. Date: 2026-11-16, after CP16.
Source: sections/two_inert_ninth_root_class_group.tex.
Certificate: code/two_inert_ninth_root_class_certificate.py.
Result: PASS. The earlier norm-exponent typo is corrected, and the split two-prime scope is explicit in the final source.

## Full source review

I checked the actual C3^2 automorphisms, all four embedded cubic fixed fields, and the transport of the three E2 conjugates by g(t)=zeta9*t. The root-of-unity orders follow from the actual cyclotomic maximal abelian subfield. The group-ring identity forces the ordinary subfield-unit quotient to be killed by three; therefore the completed A199 index is the exact ordinary index3^6, with no unknown prime-to-three factor.

The common-log lattice proof retains both nontrivial maps. For each E2 conjugate, the Kummer restriction kernel has changed-prime valuation two modulo three and excludes any nontrivial unit radical. For F'/F, the exact norm is zeta9^((1+4+7)k)=zeta3^k, so a norm-one ratio is removed by a power of zeta9. The Kronecker argument is supplied directly through bounded monic polynomials of powers. Thus each log lattice intersects the base real space in exactly the base log lattice.

The orthogonal decomposition has common dimension2 and four distinct dimension6 pieces. The sum-map kernel lattice is Lambda_F tensor A3. Its factor4 cancels the factor4 of the sum-map determinant; the embedding covolumes contribute3^10 and the native regulator square-root factors contribute a further3. This gives exactly the regulator ratio3^6/3^11=1/243. The retained 26-by-32 integral lattice certificate independently verifies the same factor by Smith normal form.

The actual permutation-character identity gives the Dedekind-zeta identity, including ramified Euler factors. The four leading signs agree; the roots-of-unity ratio is one. The analytic class-number formula therefore gives |Cl(M){3}|=81 from the already proved intermediate class groups. The zero norm to F' makes the class group a finite Z3[zeta3]-module. Its coinvariant order27 gives three summands with total length4, hence lengths2,1,1 and additive group C3^4. The norm to E2 is the other norm: A191 identifies its quotient by sigma-1 with Cl(E2){3}. This source/target distinction remains explicit.

For h=Gal(M/E2), the one ramified three-prime and the A203 global-unit field-norm index1 give ambiguous order27. Thus h-1 has rank1 and square0 on C3^4; the ideal identity j_h N_h=1+h+h^2 then makes extension zero because the norm is onto. The other ideal composite is exactly multiplication by three.

## Ramified-prime Hilbert90 and localization

The unit norm quotient has order9, and the unit Herbrand quotient1/3 gives H1(h,O_M^times) of order27. The actual capitulation map aO_M=(w) -> h(w)/w is injective: a unit coboundary makes w a base element times a unit, and ideal extension is injective on the divisor group. The capitulating lower C3^3 therefore exhausts H1.

The valuation map [h(w)/w] -> v_P3(w) modulo3 is independent of the Hilbert90 representative and of the unit-coboundary representative. Every class arising from an extended ideal has valuation divisible by the ramification index3. Thus this map is zero. A prime-to-three principal power of P3 would give a nonzero value; consequently its three-primary class is nonzero and has exact order3. Its ideal norm is the zero lower three-prime class. The order comparison identifies it with the entire norm kernel and with both rank-one augmentation images.

The proof of Cl_S(M){3}=C3^3 uses the A191 residue-weighted norm map: every S-prime class lies in that kernel, and P3 itself belongs to S and generates it. This explicitly includes the two lower primes of residue degree6 above2 that split in M/E2. Their individual upper classes have not been replaced by lower ideal extensions and have not been asserted to vanish. This corrects the overly broad preliminary inertness sentence in the conceptual correspondence.

## Primary source verification

I independently opened the Cambridge publisher PDF of Henri Darmon, “Thaine's method for circular units and a conjecture of Gross,” Canadian Journal of Mathematics47(2),1995,302–317, DOI10.4153/CJM-1995-016-6. I read Section2's regulator definition on printed303 and visually inspected Theorem2.1 on printed304. It states the leading coefficient -h_(S,T)R_(S,T)/w_(S,T), with S containing the archimedean places and T an arbitrary finite disjoint set. Taking S exactly archimedean and T empty gives the ordinary formula used here. The additional restriction on T appears only later in Section3.

The downloaded primary PDF and rendered printed304 are retained in sources/darmon1995_thaine.pdf and notes/primary_sources/darmon1995_p304.png. The web retrieval references were turn796view0 and turn797view0. No unverified theorem number is used.

## Independent finite execution

I read the entire certificate and reran it independently. It passed27 literal subgroup-stabilizer tests,54 Euler/inertia polynomial identities, the26-by-32 native lattice Smith factors (15 ones and11 threes), index177147=3^11, actual unit index729=3^6, regulator ratio1/243, roots-of-unity ratio1, class order81, unique module-length pattern(2,1,1), and2080 rank-one nilpotent transfer checks. Its explicit residue-order regression confirms that 2^6 gives splitting, while 2^2,11^2 and59^2 have order3 modulo9.

The finite checks supplement the analytic, logarithmic-lattice, cohomological and actual ideal-map proofs above. No eta-to-psi2 identity is inferred from the computed orders or capitulation alone.
