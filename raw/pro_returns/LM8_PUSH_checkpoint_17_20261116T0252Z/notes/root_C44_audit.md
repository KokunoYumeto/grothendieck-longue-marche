# Root complete proof and execution audit of C.44

**PASS.** Root read the entire candidate
`notes/pbc_exact_descent_kernel_draft.tex`, SHA-256
`d90fbae3686a5349b2e20ea6e970713032aa12749b04508d76aa12729f665378`,
and every line of `code/pbc_exact_descent_kernel_word.py`. Root
independently executed its complete `run()` without changing owner
outputs. The whole JSON, including its source hash, is byte-identical,
SHA-256 `1d74a886ae2978ce3fd5c9a9e0cb102593c08d65fde5bf334973e6c540576324`.
The source SHA-256 is
`a4226d90ccc326d95dcd961ba7e0ba02a83ec7c8d403844dfc5fe90a5d9cd9c2`.

The conclusion is an actual multiplier-one full gentle element e
with D(e)=1 and Delta(e)=1. It is not merely an element with a finite
number of vanished detector values. Consequently D is noninjective,
and the same e has the entire iterated-parity vector (1,0,0,...).
Neither surjectivity of D nor independence of all later characters
is asserted.

## Closed normal residual and full relative lifting

For an arbitrary profinite U, the intersection of its closed lower
central series is exactly the intersection of finite nilpotent
quotient kernels. The bounded-class quotients are profinite
nilpotent groups, and every finite nilpotent quotient has bounded
class. Under any finite source quotient, images commute with this
descending intersection by compactness of the nested nonempty
fibres. Thus the image of the residual is exactly the finite
nilpotent residual, not merely contained in it.

Root reread P.3's full finite scalar-cover construction, trace
count, subgroup comparison, Mobius inversion and compactness
passage, and the exact C.23/C.31 relative uses. For a closed normal
U, q_E(U) is still a finite normal subgroup. Taking its nilpotent
residual A gives the actual retained quotient E/A. Every auxiliary
source map into a central extension of E/A has nilpotent U-image,
because it lies in a central extension of q_E(U)/A. It therefore
kills R_nil(U). Precomposition with the retained automorphism
supplies exactly the same finite comparison. No step requires
Gamma/U finite or U finitely generated.

All finitely many prescribed conjugator values and generation
conditions fit one finite joint quotient of Gamma. Compactness
in Gamma cubed then gives simultaneous frames and generation in
every finite quotient; the finitely generated profinite Hopf
argument makes the resulting endomorphism an automorphism. A
cusp frame retained as one can be removed by an inner correction
in R_nil(U). This correction preserves all retained data.

The relative fibre-product equality is also proved rather than
assumed. The image of U in any finite product of finite p-group
quotients for different primes is the full product by coprime
subdirectness. Compactness gives U/R_nil(U)=product U^(p).
Choosing a lift of the common Gamma/U coordinate then proves the
relative statement for Gamma. The compact-to-Hausdorff bijection
is a topological isomorphism.

## Six actual full filling identities

In the temporary marking x=tau^(-2), y=sxs, the filling sends
x to tau^(-1), y to s and z to r. The actual conjugations by r
and s give the six displayed representatives of the outer S3
action. Their composition ambiguities are inner in F, so the
intersection of their filling kernels is normal in Gamma. Its
intersection with the characteristic H=F'F^3 is closed normal;
no openness is claimed.

The explicit word is w=[[x^2,y^2],z^2]^2. It lies in F'. Every
actual filling kills one of the three squared peripheral
elements; the relevant inner or outer commutator is therefore
literally one in the full free product. The certificate separately
substitutes all six actual words and reduces them in the normal
form of C2*C3. It also verifies the old marking and inverse word.
The displayed expression has 48 letters before free cancellation
and 44 afterwards; these are not two different words.

In the canonical signed original matrix representation, the
two commutators have the exact modulo-three values displayed in
the proof, and the final square is minus the identity. Modulo
four the original squared generators are already identity. Thus
q(w)=[5I]. The previous actual H calculation places q(U) inside
the two-group q(H); it is used only for the pro-two factorization.
The finite matrices certify that retained central value, while
the free-product reductions establish full filling vanishing.

## Centralizing frame over a compact quotient

The image J in Q12 times Gamma/U need not be finite. Nevertheless
Gamma/O^2(U) maps onto J with pro-two kernel. The retained element
([5I],1) has a preliminary lift in U^(2). Its conjugation of r
and r itself give two complements over the finite C3 subgroup of
J. Finite coprime complement conjugacy in invariant quotients of
the pro-two kernel, followed by compactness, gives a correcting
element of the kernel. The common image of the generators ensures
r is matched to r, rather than its inverse. This supplies the
actual centralizer element c with the prescribed q-value even
though J is compact infinite.

The relative product therefore carries the identity automorphism
with identity s and cusp frames and the specified r-centralizer
frame at prime two. The closed-U lifting gives the full peripheral
automorphism with all three frames retained. Since U is contained
in F, the lifted frames are pure and the automorphism preserves
the actual pure subgroup. Its pure torsion frames have the exact
Q12 values ([5I],1) used by the already checked CM normalization.

## Zero normalization and exact descent

The conjugator f=s*Phi(s) belongs to R_nil(U). This residual is
contained in the closed commutator U', since every finite abelian
quotient is nilpotent. Hence f belongs to F'. The abelian
normalizing exponent is exactly zero. This is essential: a mere
finite divisibility would not preserve all full filling kernels.

Returning to the original marking and applying the specified
inner adjustment replaces the normalized conjugator by f inverse
in the old letters. It still belongs to the actual filling kernel.
The induced modular automorphism fixes s and conjugates tau by
phi(f inverse)=1, so it is the identity on the full modular group.
Its pure restriction is identity. This proves D(e)=1 exactly.

The original q kills R_nil(U), so q*Phi=q, and the cusp intertwiner
is exactly the identity by the already proved uniqueness. The
retained pure CM frames detect Delta=1. The old-marking adjustment
has q(f)=1 and changes none of those data. The actual e therefore
survives in the abelian arithmetic-normal quotient, detected by
Delta, while D kills its class. This proves the induced
noninjectivity without assuming that D is onto.

## Search and scope record

At 00:31 UTC root made targeted literature searches for
`"Grothendieck" "Teichmüller" "gentle" "kernel" descent` and
`"Grothendieck-Teichmüller" "C_2" "C_3" automorphism lifting`.
They returned related tower and geometric-compatibility papers,
including Schneps's author-hosted tower paper and
Hatcher--Lochak--Schneps's tower paper. This limited search did
not supply the exact closed-U/descent-kernel assertion. No
priority or exhaustive novelty claim is made, and no theorem is
imported from a search snippet. The proof relies on the full
P.3 argument reread above and the already audited exact C.12,
C.19--C.20 and C.23 comparisons. Search refs are turn1189search5
and turn1189search6; they are discovery records, not proof inputs.

Canonical integration was approved after root's full review and
exact execution, conditional on the separate full FGH audit.
