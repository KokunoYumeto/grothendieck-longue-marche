# Continuation state for the ninth hourly checkpoint

Research began 2026-11-16 00:49:30 UTC. Checkpoint09 and the ninth
progress review are scheduled for 09:49:30 UTC. Consult
progress_review_09h.md for the actual timed decision and checkpoints.md
for the delivered receipt. Both main full profinite decisions remain
Open. Continue substantive research; do not finalize merely because a
checkpoint is ready. The preceding state is preserved verbatim as
continuation_state_checkpoint08.md.

## Environment, build, and exact retention

Always use workdir=/workspace/scratch/a50d05093ca1, shell=/bin/bash,
login=false. The active tree is LM4_SUCCESSOR; immutable checkpoints
01–08 are beside it. The attached originals in recovered_inputs and
recovered_background are excluded from every archive. Before each
snapshot run refresh_computation_inventory.py,
preserve_checkpoint_versions.py, and package_checkpoint.py with a fresh
number. Then independently run verify_checkpoint_snapshot.py. Never
overwrite an earlier archive. The retention helper must preserve its
own three rewritten files: checkpoint_version_retention.csv,
checkpoint_version_retention_summary.json, and checkpoint_history/README.md.

The old environment failed during hour seven. All original checkpoints
01–06 were recovered byte-exactly. Unarchived seventh-hour proofs,
programs, and output were reconstructed and rerun. No claim that the
lost old 234-page PDF, logs, or QA bytes were recovered is permitted.
The actual new seventh checkpoint has 231 pages; its recovery record
is records/recovery_07h_scope.md. Checkpoint08 was captured at
08:49:46.979167 UTC and uploaded at 08:50:21.821543 UTC. It has
174867214 bytes, 1638 entries, and SHA256
1655648f21f466e5d20b4f97733eb3d8134f6a94cdb713aad9d5444303f6c4eb.
Its native Library ID is in checkpoints.md. Independent verification
passed every manifest hash and all 5289 earlier-entry retention checks.
The next archive should compare 6927 earlier entries (verify actual).

Build with:
python3 LM4_SUCCESSOR/code/build_paper.py --env tex_runtime/env.json

The working private runtime is outside the artifact. Do not repair or
reinstall it. Its caches are relative tex_cache; the setup recipe and
actual stdout are retained. Never rerun the checkpoint08 data updater:
code/update_checkpoint09_data.py is the current table/abstract helper.
The actual TeX input graph controls the register through
assemble_register.py. update_checkpoint_report.py replaces the initial
outcome table while preserving the historical prose.

## Formal ninth-hour paper: final build and reviewed hash

222 numbered statements: 183 Proved, 14 Refuted, 19 Open, 6 Known.
86 bibliography entries; all 49 task and lead rows retained. New formal
results are A63, A64, A65, B69, B70, B71, B72, and C44. B69 is Refuted;
the other seven are Proved. A8 and B4 remain Open.

Final PDF: 258 pages, 1929118 bytes, SHA256
28c1aaf175b3e65650f0e0c027a9c80bc0e46831c44090312872923186815548.
Zero overfull boxes, undefined references, errors, or warnings. The
first build stopped at three prose math underscores in A64; these were
fixed. The second build, before B72, had 256 pages/221 statements; its
metrics, logs, QA, and review are retained separately. The final build
is records/checkpoint09_final_build_driver.log. We inspected all seven
contacts of the final 55-page sample and full pages 170, 171, 221, 222.
See checkpoint09_metrics.json, checkpoint09_typesetting.txt, and
pdf_qa/checkpoint09_final_B72/. Do not substitute the older QA hash.

Formal statements are frozen for09. Later research below is recorded
as research, not silently promoted into the PDF. All current source
files, proof notes, programs, and genuine output belong in the archive.

## A63–A65: accepted mathematics and exact next gate

A63 adds six independent cross cups to the four free cusp cocycles of
the integral A62 tower. Over k=F8, V has 36 monomial weights; the new
coefficient T=(V^(2))^6 has literal squared scalars. The residual group
N=V^4 times T has c_ij(a,b)=a_i*b_j, order 2^1080, and derived/Frattini
subgroup T. Its actual source and strict H action are constructed.
The source quotient over retained profinite C is not itself finite.

The original A56 affine datum fails the new s-normalizer norm. The
failure exhausts corrections with that datum fixed; it does not
exclude changing the old affine action/frame. A64 does exactly that:
all 360 old affine bits, old central-class rank83, and zero free t in
all four cusp rows give combined rank227 and 133 homogeneous bits.
The old quadratic norm has zero polar form on this family and admits
a solution. New tuple: work_A/A63_zero_t_A56_solution.json, SHA256
4135fabf1500006d5ec6bbe5dc0571ea91018abf911e32136cf965729d18d4e9.
Six-cup certificate: work_A/A63_zero_t_cross_cup_square.json, SHA256
f5d10fa9f5491651fef0e431edab7a952bf18fa1890073cd9d87c9a8c690de50.
The new negative action squares literally to one; all six s/r norms
are solved (dimensions20/8 and12/5). Root reran the original group law,
six-cup verifier, and read-only witness verifier, with separate outputs
in records/root_A64_*.out. CE independently reviewed them as well.

A65 proves relative perfectness of the actual enlarged source kernel
at every integral level and the inverse limit. In any scalar refinement
the abelianization stays A_n, by original-base H1 and a five-term
argument. The old derived M_n contribution to third commutators vanishes
by odd coinvariants. T has three distinct Frobenius weight families;
the only potentially invariant third argument is in another family,
so the other two actual Jacobi brackets vanish. Thus gamma3 is zero,
even though the abstract invariant tensor space can be nonzero.
The class-two derived group is a quotient of exterior^2_Z A_n. Odd
averaging and H/O^2(H) reduce its invariant part to the old complete
M_n; equality of finite orders kills the new scalar kernel. Actual
finite-image compactness gives the inverse-limit claim. Older retained
families require the explicit 6/21/42 versus108 type separation and
base-change proof, not arbitrary intersection of perfect kernels.

A3 therefore realizes the action and frames by a full positive
peripheral automorphism. Its negative companion is involutory on the
whole enlarged tower. Its full square and tower cofinality remain
Open. Root accepted proofs are in root_review_A64_A65.md; accepted agent
fragments have suffix _accepted.fragment, not the old _proposed.tex.

## A66 research: actual next group, restricted obstructions, new affine search

Agent involutions owns work_A/check_A66_cubic_twenty.py and
A66_cubic_next_layer_working.md. The actual class-three group adds four
UT4 triple cups and sixteen ordinary ordered cusp cups
z_ri(a,b)=a_r^2*b_i. Its kernel is (V^(3))^20. The source relations,
actual quotient attainment, strict H action, and literal canonical c
are checked. The old degree-two shears lift by explicit formulas adding
ordinary z coordinates into the UT4 coordinates. The resulting action
on multiplicities is unipotent, so new cusp-inner corrections can
change the negative square; they cannot simply be discarded.

For the fixed A64 affine datum, its negative-square defect is not in
the new cusp-inner norm image (rank12). Already its ordinary16
projection is nonzero, while all80 cusp-inner columns have ordinary
projection zero; old T-inner action freedom is also invisible there.
CE independently implemented and checked this projection. This is not
an all-affine-choice obstruction.

Root code/check_A66_zero_cusp_action.py retains all360 original bits.
Default W_free=t_free=0 is feasible: combined rank246, homogeneous114.
Agent's exact old norm test has full polar radical114 and image rank2,
but target outside image. --pure-frame instead asks W_free=p_free=0;
it is linearly infeasible, with dual annihilator rows108,117. The
canonical c-inner cusp vector is not beta-fixed. Neither result is a
full negative-order obstruction.

--free-frame imposes only W_free=0 with the first108 old s-class bits,
dropping the432 t=0 bits. This has540 equations, rank102, homogeneous258,
and a directly verified solution of the old source/group-law equations.
The chosen representative's old central norm fails, but the complete
258-dimensional old norm problem now succeeds. Its polar radical has
dimension231 and zero image; exact core27 search finds assignment2128959
after4171819 steps. The saved partial tuple is
work_A/A66_zero_W_free_t_partial.json, with original action/cusp/s-norm
checks passing. The convenient J r-frame fails central-only correction.
The exact matrix,
target, solution, and literal tuple are
records/A66_zero_cusp_action_free_frame_feasibility.json, with genuine
stdout in check_A66_zero_cusp_action_free_frame.out. Agent core/search
certificates are work_A/A66_zero_W_free_t_quadratic_core.json and
A66_zero_W_free_t_quadratic_search.out; producer/stdout are
check_A66_zero_W_free_t_norm.py/.out.

Root extracted the complete19-dimensional W quotient of the old277
homogeneous directions, with19 source lift masks and258 W0 kernel
masks: records/A66_cusp_action_space.json. CE extracted all19 linear
and171 quadratic ordinary-square coefficients, independently checked
64 full-law polarizations, and enumerated all524288 W values. Exactly
408 have zero square. This is the whole ordinary action-square gate
in the current affine family; it is not the whole new frame/scalar
problem. Certificate work_CE/A66_ordinary_action_zero_set.json and
code/check_A66_ordinary_action_space.py/.out.

Within the W0 family's successful old norm core, the231-dimensional
radical has local image rank24. Of841 jointly allowed local frame
pairs,29 belong to its affine coset. Full360-bit correction masks are
in work_A/A66_W0_radical_local_gate.json. Agent is directly rebuilding
these tuples and testing the lower six and ordinary sixteen cup norms.
Do not promote a local pair test into a full group-law norm assertion.

Root wrote and agent independently passed
records/A66_initial_transporter_and_r_frame_review.md. A33 can select
its initial C-frames with an additional closed transporter condition:
the dyadic frame remains conjugate to the actual Galois reflection;
pro-odd C2-complement conjugacy matches finite transporters; compactness
gives a pure transporter from s*d_s to d_r. For those construction-
selected frames, any actual pro-two D->C with involutory action and
s-normalizer has an involutory r-normalizer over the original C-frame,
by A16 and P-conjugacy of order-three complements. This does not apply
to arbitrary later equivariant frame choices without that condition.

## New local scalar cover and actual source directions

Root code/check_suzuki_local_scalar_extension.py and corresponding
records give a complete256-element stem cover. Base S64 has law
(a,z)(b,w)=(a+b,z+w+a^2 b). Its F8-valued C7-invariant cocycle is
f((a,z),(b,w))=z b^4+a^2 w^4. Tr(f)=delta(Tr(a^4 z)+a^7).
Project central F8 along F2*1 to kerTr={0,2,4,6}; the resulting cover
has center4, derived32, and lower central orders256,32,4,1. All262144
cocycle triples,4096 trace pairs,28672 action pairs, and finite-group
checks pass. The three cocycle components span two classes; the only
coboundary functional in that span is trace. Root does not claim an
exhaustive H2 calculation from that component test; agent separately
computed full invariant H2 dimension2 by the normalized bar complex.

Source audit/proof: records/suzuki_local_scalar_proof.md. Root opened
Eaton2024 arXiv2401.04028v2 at its A(m,theta) definition and the primary
ATLAS Sz8 page; these are recognition/consistency checks, not substitutes
for the actual cocycle proof. Higman1963 publisher content was not
retrieved at proof level and is not used. The MO formula is not cited as
authority. Avoid Eaton's literal broad faithfulness phrase for all
automorphisms on the center; no argument depends on that statement.

Agent's next source construction sums the centers of36 weight copies
and uses the four separate cusp diagonals. It attains a quotient C2^8
of the actual new scalar kernel by third commutators. Full scalar
kernel, action, and both normalizer norms remain unsettled.

## B69–B72: full rigid kernel and all discrete conjugates

Agent topology_census owns work_DE. B69 refutes injectivity of the
actual full six-generator cyclic rigid map theta5:F6->PB6. The reduced
word w0=[f5^-1 f1^-1 f0^-1 f2^-1,f1] is nontrivial by an S3 image but
its actual132-letter PB6 substitution has trivial faithful Artin action.
This is not B67's different intermediate-word failure: B68 proves the
latter survives as a filling pseudo-Anosov point push.

B70: discrete kernel free countably infinite; completed kernel free
profinite countably infinite with a basis converging to1, by the
primary-checked Shusterman theorem. Equality of completed kernel with
the closure of the discrete kernel remains Open. It is not the full
profinite completion of that abstract infinite-rank discrete kernel.

B71 uses nine conjugates of w0^20 with zero source abelianization and
mod9 matrix rank9; a determinant -52 is a3-adic unit. Saturated
logarithms and cubing give the whole principal group. In the single
joint quotient of all12 full rigid tests and the integral3-adic
symplectic representation, both compact source closures have exact
common principal image {1} times the three-dimensional Eichler group.
This is an actual joint image result; it does not give a common lift
in the full ambient mapping-class completion.

B72: H_T intersect g H5 g^-1=1 for every discrete ambient g. The
five-fold unramified punctured cover identifies H5 with an index-five
subgroup of pure M04. Nonidentity elements are pA or peripheral powers;
the latter lift to one or five reduction curves. An A4 action on a
set of size1 or5 fixes a curve, whose sides are separately A4 invariant,
contradicting transitivity on12marks. In the pA case A4 and conjugateC5
lie in the same finite dilation kernel, generate actual A5, and force
the rigid discrete centralizer contradiction. Root read McCarthy1994
Lemmas1–4 and checked the explicitly written punctured adaptation.
No profinite Nielsen–Thurston type or completed-intersection conclusion
is claimed. Review: records/root_review_B72.md.

Current full ambient route: the common involution gives a faithful
colored eight-point quotient retaining six ordinary and two branch
points. Forgetting the two C5 poles upstairs gives a decorated
seven-point comparison faithful on H5 and its completion. The actual
matching of the two source lifts remains open. The extra three
colored abelianization directions are anti-invariant under branch
swap; killing only the old cyclic abelianization does not kill them.
These corrections and current questions are in
work_DE/next_common_involution/faithful_quotient_note.md.

## C44 and current full-source finite tests

For the regular pants action sigma with sigma(z)=z^-1, C43 gives the
unique g satisfying sigma(g)g^-1=z. Put K=normal closure(z), A=F/K=Zhat.
C44 computes K/Phi_p(K)=Fp[[A]][z] by cyclic covers and the extension
of continuous characters fromK to an open neighborhood. In characteristic2,
T-1 identifies the completed group algebra with the augmentation ideal.
The equation theta D_a=1, (T-1)D_a=T^a-1 forces a odd and, by evaluating
at primitive odd-prime roots, a full unit. For every p the conjugates
by powers ofg span the Frattini module. Thus g,z generate all relative
pro-p quotients and their actual pronilpotent fiber product overA.
The substitution x->g,z->z is a quotient automorphism and conjugates
the standard regular action there. It need not preserve the original
peripheral marking and does not prove full F generation.

Agent torus_real owns work_CE. Its actual finite test maps to
(A5 times A5) semidirect C2, with swap head and boundary(a3,b5).
Any subgroup containing that boundary and any odd-head element is
all7200 elements; powers isolate the3/5 cycles and no proper A5
subgroup contains both. C44 therefore implies generation in this
nonsolvable quotient. It also forbids a section of Fsolv2->Fhat2 that
fixes literalz. General projectivity/retract arguments without that
literal boundary are insufficient. Exact enumeration and proof:
work_CE/research_regular_pants_wreath.txt and its code/output.

## Sources and work discipline

Current extra recognition audit is records/recognition_source_audit_09h.md.
Do not recycle the already excluded hypotheses: finite-solvable only;
already accessible; already a completion of a discrete virtually-free
group; pro-p only; torsion-free open subgroup only; free-involutory
already assumed; or real-projective embedding without generation.
No unused source is invoked as a theorem here.

Keep actual matrix outputs, exact input hashes, scalar-versus-module
coefficient actions, all finite/source/profinite distinctions, and
both full-versus-quotient negative squares explicit. Do not overwrite
old successful or failed witnesses. The next main work is the larger
A66 affine norm family and full ambient B comparison. Hourly reviews
follow the user's progress rule. No ad hoc checkpoint exports.

## Late09 A66 direct checks (after the local pair enumeration)

The radical-adjusted tuple is saved as
work_A/A66_W0_local_compatible_partial.json, produced by
check_A66_W0_local_adjustment.py/.out. Its old negative square, literal
cusp, s conjugacy/norm, W0, and selected local coordinates all pass.
The independent complete lower-six and ordinary-sixteen source models
both pass action-square and s-normalizer norms; see
check_A66_W0_local_lower.out, check_A66_W0_local_ordinary.out, and their
result JSONs. The r-frame was not computed in these models (some earlier
stdout displayed false beside a None rank; that means skipped, not a
proved failure, and the producer is being clarified). The reviewed
initial-transporter/A16 argument supplies existential r-frames for the
construction-selected initial C-data. Full simultaneous20-factor
UT4/ordinary source and its nonzero scalar refinement remain next.

CE additionally saved research_A66_complete_action_gate.txt, including
an analytic proof of quadraticity and correction-independence for the
408-zero enumeration. research_regular_pants_wreath_general.txt proves
all A5^n semidirect C_n tests with boundary(a3,b5,1,...), and an exact
limitation: z=(a3,a3),x=(t5,1)swap still generate the actual7200 quotient,
but swap,z generate a proper C2 times C3 despite the generator head.
This is not an example of the canonical g or the required negative
action. DE's checked seven-point comparison is independently reviewed
in work_CE/review_decorated_seven_point_reduction.txt.

## Actual ninth-hour review

CONTINUE recorded at 2026-11-16T09:49:30.000180+00:00. See progress_review_09h.md.
The checkpoint is now being captured with every agent writer paused.
Release the agents immediately after immutable ZIP capture; upload and
independent verification follow without modifying that archive.
Next checkpoint/review: 2026-11-16 10:49:30 UTC.

Checkpoint09 is now saved and verified. Its exact identity, size, hash,
receipt, and metadata are in records/checkpoints.md and the09 records.
All1965 manifest rows and6927 earlier-entry retention checks passed.
The immutable archive is212400767 bytes. Research writers are released;
continue until the next substantive progress review at10:49:30 UTC.
