# E.122 — independent proof, literal-field and finite-map audit

**Verdict: PASS. No mathematical correction requested.**

Reviewer: `/root/d_galois`. I reviewed the complete 624-line final proof
`research_e122/sections/E_fiftythree_higher_action.tex`, SHA-256
`93f321471c5b1f6b4da11fe6290e16a82ea77a5e18a8827b1bcb735e8358abdd`.
The frozen manifest is
`9f63758a401fad7db429d657ab7008f98d0f4e864580b9ca517876597735cd9e`.
All 171 listed files match their recorded byte counts and hashes, both
before and after this review. No author file was modified.

## Scope and actual executions

I read the three complete mathematical GP sources, the complete relative-ring
checker and finite-map checker, totalling 470 source lines. I also read the
portable replay driver, source-evidence ledger and dependency material.
The earlier E119 and E121 maps used here are covered by my separate complete
audits in `d_e119_audit` and `d_e121_audit`; their actual class-field and
Hilbert90 maps were checked again where they enter this proof.

I wrote and ran two new focused programs, importing no author executable:

* `code/d_e122_maps.py` uses a separate integer polynomial-convolution and
  monic-reduction implementation of the 54-dimensional relative field. It
  checks every literal cube and relative norm. It enumerates both full HNF
  genus groups, their restriction kernels, and the actual norm before Smith
  coordinates. It reconstructs all upper character columns from the lower
  norm coordinates and checks the complete embedded completed-unit norm
  lattice and its inverse maps.
* `code/d_e122_ideals.gp` initializes the degree-eighteen candidate field
  independently, factors all ten candidate principal ideals, and rebuilds
  each principal HNF from its full prime factorization. It checks the exact
  absolute norms and the support at three and fifty-three.

Both executions returned exit zero and explicit PASS records. The GP stderr
contains only its expected stack-allocation warning. All exact candidate
norms and divisor data agree with the author certificate. The complete new
stdout, stderr, JSON and source are retained. There was no failed or replaced
execution of these two peer programs.

This is an independent full proof/source review and focused literal-field,
ideal and finite-map execution. I did not rerun the author's complete
three-stage local/genus/witness reconstruction. Parent `/root` separately
reported that full reconstruction; its execution is not attributed to me.

## The actual all-level class-field argument

The six prime chains and their uniformizers are correctly marked. At three,
the actual rational cube root has `v3(a0+1)=2`; the decomposition
`a0 xi^k+1=(1-xi^k)+(a0+1)xi^k`, for `k=1,4,7`, gives valuation one.
The successive translated cubic polynomials are Eisenstein. At fifty-three
the literal radical is a uniformizer, and the unshifted cubic is Eisenstein.
This proves that each chain has one prime at every step and that every
vertical extension is totally ramified at the six ordered places. The
defining polynomial discriminants exclude ramification elsewhere.

For the actual S-Hilbert three-class field, the two inclusions in the proof
are valid with the stated maps. Base change gives `H_D^S E` inside `H_E^S`.
Total ramification gives `E intersect H_D^S=D`, so restriction is the onto
ideal norm. Killing the six local decomposition images in the abelianization
gives exactly `H_D^S`, because this imposes splitting at S and leaves the
already unramified outside-S condition. Thus the subgroup `I` is generated
by the six actual order-three decomposition images.

The normalizer action on `I` is the identity. It fixes the six lower places,
and any different prolongation only conjugates its decomposition group.
After abelianization this ambiguity disappears. Restriction identifies
each decomposition image with the same subgroup of the literal cyclic
vertical extension; the normalizer commutes with that generator. Induction
therefore gives `T Gamma` contained in `I`, `T I=0` and `T^2 Gamma=0`.
Changing the lift of the normalizer also acts by an inner automorphism on
`Gamma`, so it does not change this conclusion.

On the entire unknown upper class group, put `s=g^3-1`, `M=sA`. The actual
ideal identity is `jN=1+sigma+sigma^2=3+3s+s^2`. Norm equivariance and the
proved lower action give `TjN=0`; the displayed polynomial calculations then
put `M` inside `(3,T)M`. The actual action satisfies `g^9=1`, even though a
chosen lift to the class field need not have order nine: its ninth power
belongs to the abelian class subgroup and hence conjugates that subgroup
trivially. Thus `T^9` is divisible by three in the acting group ring.
For a finite group killed by `3^e`, `(3,T)^(9e)` acts as zero. Iteration
forces `M=0`, proving the full vertical action. This reasoning does not
replace the unknown group by its coinvariants. It then gives `T^2=0` and
`3T=0` on that same full group.

The local-coordinate identification of `ker N_d` also checks with its
inverse. The product of the six local reciprocity maps gives
`I=F3^6/chi_d(U_d)`. Their common restriction to the degree-three field is
the coordinate sum. Its kernel is therefore precisely the actual class
norm kernel, once the full vertical action has been proved trivial. An
inverse sends a coordinate vector to the product of those marked local
Artin elements. The product formula and the diagonal S-unit relation
give exactly the two relations stated in the proof.

The corestriction calculation retains the correct factor. Norm of the
coherent higher radical is the lower radical, while local invariant
composed with corestriction is the lower invariant. It follows that the
included lower S-unit characters are unchanged. No local-degree factor
is inserted. The same argument from level two later retains all five
independent characters.

For the recurrence, the order-nine local decomposition groups in
`Gal(H_E^S/D0)` really are cyclic of order nine: their restriction to
`E/D0` is an isomorphism, since the places split over E. Writing their
positive generators as `gamma_i=gamma_0 a_i` gives
`gamma_i^3 gamma_0^(-3)=3a_i`, using the already proved
`1+g+g^2=3`. The potential conjugation by `g^3` is trivial on the class
group at this point. Restriction sends the differences to `N_d(a_i)`;
these generate the preceding kernel, while the cubed differences generate
the new kernel. Consequently `K_d=j_d K_(d-1)` is an equality of the actual
subgroups. The proof correctly records the changes caused by prolongations
and by the choice of reference generator.

The inverse-limit argument is valid independently of its later finite
evaluation. The finite relation `3M_(e,d)=M_(e,d+1)` follows by induction
using both the onto top norm and the complete top kernel. Compactness then
gives `B_(d+1)=3B_d`; the finite solution sets have the finite-intersection
property. The topological Nakayama argument works in the profinite topology
because every finite quotient has bounded three-power exponent. When
`K_2=0`, the recurrence directly makes every later norm an isomorphism,
and the actual projection to `A_2` identifies the limit with `A_2`.

## Local ninth characters and literal upper witnesses

The local ninth-norm calculation has a complete index argument. The
exponential range implies that `1+lambda^16 O` consists of ninth powers.
The fifty-five displayed resultants are norms of actual local units.
Their log columns span a subgroup of index nine; the local norm-index
theorem gives the same index for the full local norm subgroup. This
proves equality by the actual inclusion. It does not require those
fifty-five upper units to be a basis.

The calibration at four fixes the character generator and sign. The
rational pair `(a0,4)` has trivial odd-order Hilbert symbol by complex
conjugation. Arithmetic local reciprocity sends the cyclotomic radical
by exponent `4^(-6)=37 mod81`, giving the three marked values `4,7,1`.
At fifty-three the negative residue logarithm agrees with the positive
arithmetic Artin convention on the fixed radical. The recorded
coefficient/divisor precision bound controls both evaluation error and
normalizing-uniformizer error; its lower bound exceeds sixteen. The
approximate radical differs from the exact one by a ninth power, so
the local extension and its marked generator agree.

My finite check verifies all 165 local log columns, each complete Smith
identity, all character-kernel containments, and all three calibrations.
It separately enumerates the genus groups of orders 729 and 2187 and
their 243-element restriction kernels. The raw comparison is the identity
on the nine idelic coordinates. It is checked on every kernel element
before applying the exact Smith forward and inverse maps. Those ambient
forward maps have rational entries; my certificate stores exact strings
and asserts their decoding. The induced four-coordinate map is literally
the identity, with the stated multiplication-by-three extension map.

The new polynomial implementation checks all twenty-two literal identities
`v_k^3=product w_i^a_ki` by cross multiplication in the exact relative field.
It also checks all twenty-two products `v_k sigma(v_k) sigma^2(v_k)` against
their complete lower-unit coordinates and signs. The independent ideal
program proves every candidate is an S-unit. Hence the cube identities
make every `v_k` an actual S-unit without an upper unit-basis assertion.

From the six-by-fifteen lower ninth-character matrix and the full
fifteen-by-twenty-two norm-coordinate matrix, I independently reconstruct
every upper character by division by three followed by reduction modulo
three. This agrees with all retained upper columns. The indicated five
columns have determinant `-4` in their first five rows. I enumerate all
243 images of the five-dimensional source and obtain exactly the
product-formula hyperplane. Thus `chi_2(U_2)` is the entire hyperplane,
and the exact class-field map gives `K_2=0`. The previously proved
recurrence then gives the stable full class groups and actual transition
maps at every level. This is a finite witness inside an all-level proof,
with no inference of stability from a bounded table of class numbers.

## Embedded unit norms and completed kernels

The first completed norm subgroup is evaluated through its actual lattice.
The field-norm condition has index nine. The separately proved Hilbert90
divisor map identifies the further unit obstruction with `C3^4`. Hence the
full completed unit-norm index is `3^6`. All twenty-two norm columns and
the lower cubes are actual norms. Their HNF has determinant 729, proving
equality with the full subgroup.

My checker verifies the full rank-fifteen matrix `M`, determinant
`94770=3^6*130`, its exact rational inverse, and both lattice inclusions
over `Z3`. It reconstructs the six-row congruence matrix `Q`, its displayed
right inverse, and all 729 quotient values. The actual torsion relation
`9e1` is killed. The inverse map in the proof uses the nine literal signed
root units and six included lower units with the `Z3` exponents `M^-1 x`.
Its norm is the required lower unit. Changing `x` by the torsion relation
alters that preimage by a genuine norm-one element. All other preimages
are obtained using the completed kernel; the statement retains this
choice ambiguity.

At every later level, the included five characters give the exact
field-norm quotient `C3^5`. The outside-S divisor construction from E121
applies with the now trivial full vertical class action: it identifies
the additional unit defect with `A_(d+1)/j_d A_d=C3^4`. The divisor
choice, the choice of a field-norm preimage, and the prime-to-three
projection are handled by the same explicit Hilbert90 inverse maps.
Every included lower cube is a norm, so the combined cokernel is killed
by three and has order `3^9`. This proves the stated `C3^9` quotient.

The torsion and free rank of the completed kernel are also correct.
The extension by `mu27` splits at a fifty-three place of `Q(xi)`, whereas
the radical tower is totally ramified there and has only one prime. Its
inclusion would inject a product of three local fields into a field,
which is impossible. Thus the three-primary roots of unity remain
the literal `mu9`; the kernel of their norm is the literal `mu3`.
The S-unit ranks differ by `2*3^(d+1)`. The proof's product of chosen
quotient-basis lifts gives an actual topological isomorphism with
`mu3 plus Z3^(2*3^(d+1))`, together with its inverse and both coordinate
ambiguities. It does not assign a numerical upper unit basis.

## Primary readings and retained limits

For this review I freshly opened Milne's original *Class Field Theory*
v4.03, III Lemma2.4, Lemma2.7, Theorem3.1 with the complete cup-product
argument, and Theorem3.4. I also freshly read the official PARI
`idealstar`/`ideallog` contracts, including the `cycmod=9` and explicit
generator flags. The global reciprocity, Hilbert-class and cyclic
Hasse-norm proofs were independently read in my retained E119/E121 audits.
The unfinished proof notice after Milne III Lemma3.2 is not represented
as a read proof; the actual restriction/corestriction argument used here
is the complete preceding cup-product calculation.

The conclusion is the entire specified positional S-class tower, its
actual norm/extension/normalizer maps, the embedded first unit-norm
subgroup, and all later unit norm quotients and completed kernels. The
proof keeps the separate maps to the intrinsic section problem. This
audit does not upgrade those maps or claim an uncomputed upper ordinary
class group or an explicit numerical basis of all upper S-units.
