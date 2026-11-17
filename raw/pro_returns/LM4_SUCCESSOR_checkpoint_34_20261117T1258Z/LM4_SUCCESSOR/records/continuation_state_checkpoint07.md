# Continuation state: recovered seventh-checkpoint freeze

Research began2026-11-16 00:49:30UTC. Original immutable checkpoints01–06
are restored and byte/CRC/manifest verified. The seven-hour review was
scheduled07:49:30 and recorded07:51:06 after the interruption: CONTINUE.
Checkpoint07 is delayed by the original environment loss. This recovered
snapshot is a complete archive, not a summary-only export. The next timed
review remains08:49:30UTC. Do not stop merely because a checkpoint is
complete. Both main decisions remain Open. No ad hoc exports.

## Environment and recovery

Use shell=/bin/bash, login=false and the explicit workdir
/workspace/scratch/a50d05093ca1 in every exec_command. The old default cwd
no longer exists. The active tree is LM4_SUCCESSOR. Original archives01–06
are beside it. The attached prompt and background are recovered under
recovered_inputs, with background extraction under recovered_background;
do not package attached originals.

All3817 entries from the six durable archives are retained by identical
active files or exact historical copies. Run code/preserve_checkpoint_versions.py
again immediately before each snapshot, then independently verify the
retention paths inside that ZIP. That script's scope is durable archives.
Original unarchived seventh-hour files were lost; see recovery_07h_scope.md,
component recovery ledgers and checkpoint07_preoutage_observations.json.
The former234-page PDF and its QA were not recovered identically. We have
reconstructed the seven new statements and rerun their programs. Never
represent fresh outputs as the lost original bytes.

## Frozen formal state and fresh PDF

206 numbered statements:169 Proved,12 Refuted,19 Open,6 Known.83 bibliography
entries,49 requested task rows. The seven formal additions since06 are
A55,A56,A57,B65,B66,C41,C42. The actual TeX input graph controls the register;
separate proposed A58–60 and C43 sources do not count yet.

Fresh recovered PDF:231 pages,1773024 bytes, SHA256
 ddb9c3cb5b5408da09a8d0de38c7dac824d9c93d206daed7f367161b263353cb.
Final log has0 overfull boxes,0 undefined references,0 errors,0 warnings.
54 pages/six contact sheets inspected, plus64,66,144,146,194,195 at full size.
See checkpoint07_recovery_metrics.json and checkpoint07_recovery_typesetting.txt.

The private TeX runtime is repaired: genuine CTAN luaotfload, lualibs,
luatexbase, lua-uni-algos; actual docstrip products; private format and
installed dvips font maps. Recipe, setup logs and archive hashes are in
records/tex_recovery. Build with:
 python3 LM4_SUCCESSOR/code/build_paper.py --env tex_runtime/env.json
TEXMFCACHE and LUAOTFLOAD_CACHE must be relative tex_cache inside the paper
working directory. That cache and third-party runtime packages are excluded;
authored recipes, source, PDF and build stdout are retained. Do not rerun the
old checkpoint06 data helper. update_checkpoint07_data.py is idempotent.

## A55–57: accepted frozen results

A55 determines the exact elementary-two center over an actual relative-
pronilpotent base. It constructs the equivariant class-two extension, repairs
the actual s-square by a C4 carry, proves generation, and proves equality
using the reverse commutator map. The conditional general-base version needs
actual acyclicity, not a finite-head substitute. No action/frame consequence
is inferred from the center calculation alone.

A56 uses Q6=S3×A4, K6 rank13, actual H=Pi/(K6'K6^7), and the forced retained
beta0=(1,(01)(23)). Its self-dual V=F8^36 has binary dimension108 and End=F8.
The full cohomology has dimension8 overF8, with s/cusp restrictions4+4.
The actual residual A=V^8 has binary dimension864; its actual central layer
M=Sym²_F8(F8^8) has dimension108 overF2. The group has order2^972 overC.
The source carry is essential. Actual action and frame equations are solved,
not merely graded. The277-variable homogeneous system has radical250 and
27-variable core. Fresh solver: core assignment27666,18461 visits; fullmask
18677289404303020461252901246388292043973835622281379854.
Independent check_Q6_final_frames.py verifies original group multiplication,
cusp, negative square, s/r conjugacy and s/r frame squares: PASS. Root rerun
is records/root_check_Q6_final_frames_recovered.out.
All allowed odd translations beta=(n,beta0) are handled by t=beta0*n/2,
actual relative-seven centralizer lifting, a positive cusp-fixed gauge over
identity_C, and transport back. Older6/21/42-dimensional simple types are
disjoint, hence compatible by actual joint residual comparison. No cofinality
or full negative involution is proved.

A57: O=GR(4,3)=Z4[T]/(T³+2T²+T+3), T order7. V4=O^36 liftsV. The Bockstein
on Cnew is injective since Pab has exponent2, but inflation toPi has kernel
the4-dimensional cusp summand. Every nonzero such class gives a nonsplit
actual source quotient. Four independent classes are simultaneously attained
with kernelV^4. Literal cocycle representatives are adjusted by lifted
coboundaries. A57 itself makes no new action/frame/stability claim.

## Fixed-r caveat, essential scope

records/fixed_r_subfamily_caveat.md: the failed pre-outage cross-section
calculation fixed a canonical r-normalizer. That restricted-family failure
is NOT an obstruction to the full problem. The92 affine directions and
variable r-normalizer must be retained. The structural pro-two repair needs
an actual base transporter between the local involutions. For the A33
existence family retain that transporter as a closed compact variable;
do not claim every arbitrary previous frame choice has it.

## A58–60 and C43: post-freeze proposals for08

A58_proposed.tex: exact center for all finite abelian residualA under the
specified actual acyclicity. Mp=(wedge²_Z Ap)_{O^p(H)}, M=productMp;
m=max(1,e2+1,2e3+1). The scalar quotients are augmentation powers; the final
center is exact. Ext and Hom invariants vanish under the actual normal
p-prime subgroup. Source s²/r³ are repaired by finite cyclic carries. No
finite-order lifting theorem is inferred. CE review is saved.

A59_proposed.tex: actual Bockstein abelianization V4^4⊕V^4. Multiplicity
T=O^4⊕k^4. Opposite-weight stabilizers impose minus transpose, so the center
is (T tensor_O T)/(u tensor v+v tensor u), retaining diagonal2-torsion.
It is O^6⊕k^30, hence C4^18×C2^90. Reduction to the old k^36 center has
kernel2O^6=k^6,18 binary dimensions. H acts trivially. The actual scalar
commutator subgroup stabilizes after the next step. No frame claim.

A60_proposed.tex and work_CE/research_A57_integral_norm.txt: the zero-s-
restriction integral cohomology is freeO^4 (rank24 normalized cocycles minus
rank20 split coboundaries). Cusp restriction is an isomorphism. Actual
Teichmonomial c acts literally as identity on cusp invariants/coinvariants;
its twisted action on that cohomology is minus identity. Positive h fixes
cusp, acts+1, and has correctionw with Cw=w. The c correctionv satisfiesCv=v.
Thus b=hc has correctionq=v+w, Cq=q, and b² fixes every integral cocycle
value. Together with the old quotient, b²=1 on the actual A57 fiber product.
Different integral lifts give the SAME actual kernel: their difference2t
has t a residue cocycle, all of whose classes inflate fromCnew. Root andCE
reviewed this proof. By the existing scalar-square argument, if b²=id on
Pi/N and b(tau)=tau^-1 literally, the discrepancy onPi/[N,Pi] is a central
homomorphism killed bytau, which generatesPiab=C6; hence it is zero.
This proves action-square through the stable central refinement, separately
from literal normalizer-frame equations.

Integral affine frames: s uses a commuting monomial C2×C2 action; r, after
a coboundary gauge d(r)=0, uses a monomial S3 quotient. Stabilizer orders
have no7-part, so their seventh-root characters are trivial; invariant
reduction is onto. This retains prescribed old affine frames. CE review:
work_CE/review_A60_integral_frames.txt. Actual integral affine data is in
work_CE/Q6_integral_affine_data.json; its generator, c and cusp checks PASS.

Remaining new central gate (active): the exact integral class-two group
has been constructed byA. Its actual s²/r³, standardc, positive cusp-fixed
action, negative square and zero s-conjugacy residue pass. CE's constrained
homogeneous correction map on the new k^6 center has rank5; remaining
annihilator is coordinate01+coordinate02. This is a diagnostic only.
A is evaluating the actual constant with literal old central-frame
transport. A larger existential choice may vary the newA56 central frame
while preserving all older data; it is not the same claim as retaining the
exact stored A56 frame. No obstruction or success is yet recorded.

C43_regular_pants.tex: regular pants involutions have self-centralizing
sections. Keep the swapped cusp pair as E/Dx through the actual surface
boundary duality before localization. The fixed cusp givesDz with two
endpoints in the same global section class. Both endpoint maps have the
same kernel after actual coefficient transport; boundary half-rank forces
surjectivity onto single-section cohomology. A finite permutation module
then detects any nontrivial centralizer and gives a contradiction. This
does not recognize E as a free product or settle generation/third cusp.
Root review records/root_review_C43_recovered.md PASS.

## B65–66 and active Birman problem

B65 proves H5 centralizes the actual D5 inA5. The twelve rigid seven-sets
are two constant D-stable sets and one regularD5 orbit of ten. The one
explicit theta5:F6→PB6 has the complete common rigid kernel; fixed-pair
linking(4,6)=0 supplies the exact sphere comparison. Neither discrete
injection nor profinite embedded topology is proved.

B66 gives a strictly pointed arithmetic diagram of the actual tetrahedral
and cyclic source curves over a number field containing all punctures,
map coefficients and the common base point. The Galois section actions
commute with every actual map andA5. An infinite-order cyclotomic scalar
has distinct powers in every finite nilpotent class; the degree-two
projector yields compatible common eigenlifts. A nonzero commonGa exists
in rational prounipotent completions, killed by all rigid tests. Denominators
are not uniformly bounded; no compact pro-ell or fullK element follows.

work_DE/next_joint_rigid_symplectic/Q_Birman_reconstructed_note.md reduces a
five-strand intermediate question to Q=Z²*Z²*Z, with baseF3=<a,f,e> and
fiberF4=<C,T,R,S>. All action words and the antihomomorphism convention are
checked exactly by reconstruct_Q_birman.py. Injection is equivalent to
free independence of indexed families alpha_g(T),g∈F3/<a>, and
alpha_g(C),g∈F3/<f>. Cyclic stabilizer inclusions alone do not prove it.
The fullF6→PB6 fiber has an additional surviving boundary-commutator gate.
DE's Q_real_deformation.md moves r=ζ5 to2 through a collision-free path,
giving the two-moving real family(1,2,4,s,2s). The deformation does not
apply to the full three-moving-point family; fifth-root collisions split.
DE is studying this exact intermediate geometry.

## Sources, packaging, upload and continuation

New source audits have not supplied a recognition or braid-injectivity
theorem. Herfort–Zalesskii's S3 amalg_C2 S3 counterexample has kernel
C3 coproductC3, not the required freeF2. Haran's real-projective embedding
criterion is not a full profinite free-product recognition theorem.
Jankiewicz–Schreve's high-power twist theorem does not imply the unpowered
Q injection; its lantern example is a relevant caution. Boggi's2026
published nonsolvable centralizer step remains the already recorded gap.

Snapshot workflow: refresh_computation_inventory.py; brief all-agent write
freeze; preserve_checkpoint_versions.py; package_checkpoint.py7 (never
replace an existingZIP); independently check every manifest byte/hash/CRC
and every retention-index path IN THE ZIP. Current archive-numbering and
metadata are in records/checkpoints.md. Update after successful upload.

Cloud Library helper scripts were refreshed into library_helpers_recovered.
Use library_upload.py once with the absolute ZIP path and purpose
create_library_file, library_artifact_type other; inspect its per-item receipt
and metadata. Never call prepare/finalize separately. Do not create a second
upload if the first outcome is uncertain. The checkpoint link is delivered
in commentary; then continue research. This is not a final response.

Agents: involutions ownsA and the central norm computation; torus_real owns
C43 and independently checks A; topology_census ownsB and the real Birman
route. Ask for a brief file-mutation freeze only around snapshot capture.
Earlier continuation_state_checkpoint06.md preserves the complete previous
state, including every still-open peripheral task. The49-row task table is
authoritative for coverage. No task is dropped because the mains dominate.

## Latest post-freeze diagnostic, before the delayed07 snapshot

The integral central baseline has actual s-frame square vector
(4,2,7,6,3,1) overF8. On the two constrained homogeneous correction families
currently computed, the remaining functional z01+z02 has value6. This
refutes correction within that fixed-witness subfamily only. Exhaustiveness
and the freedom to change the newA56 central frame remain under review;
no full norm obstruction is asserted.

The intermediate Q=Z²*Z²*Z braid injection now has an explicit candidate
kernel word, independently evaluated as identity inPB5 by the owning
agent. Its image inPB6 is nonidentity, so this result does not give a
kernel of the fulltheta5 map. The exact proof and certificate are being
saved for independent root review. This is post-freeze research, not an
additional proved statement in the206-row seventh-checkpoint register.

## Post-snapshot continuation

Checkpoint07 is delivered and immutable; see checkpoints.md for exact ID,
155748044bytes and SHA25646e2fefa49e5432b4defed37b545a19cef2b703bc0c865162559c56a4d196dd4.
The next review is08:49:30UTC. Root has read and accepted A58–60 andC43,
and independently rerun/read the intermediate Q counterexample. Those
results are now being integrated for08; the previous206-row count is07's
freeze, not necessarily the current live count. A61's existential central
repair is being written with independent review and exact certificates.
