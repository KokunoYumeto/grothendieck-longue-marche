"""Capture the twentieth hourly checkpoint after its timed review and writer pause."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,20,49,30,tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_20.zip').exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the timed review.'
while remaining>0:
 time.sleep(min(0.5,remaining));remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
m=json.loads((ROOT/'records/checkpoint20_metrics.json').read_text())
assert m['statements']==274 and m['task_rows']==49
assert m['statuses']=={'Known':6,'Proved':230,'Refuted':19,'Open':19}
assert m['bibliography_entries']==108
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
qa=(ROOT/'records/checkpoint20_typesetting.txt').read_text()
assert m['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint20_writer_pause.md').exists()
computations=(ROOT/'records/checkpoint20_computation_audit_state.md').read_text()
review=f'''# Twentieth-hour progress review

Scheduled review:2026-11-16 20:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. This hour replaces the infinite
source-orbit list by an actual finite free cellular model with its whole
coefficient group and genuine involution, proves all eight actual row
stabilizers, and resolves the actual covering-space image of a previously
undetermined sphere. These are changes to the main B obstruction problem,
not a further affine/metabelian census or a finite-depth orbit search.
The full research record is records/twentieth_hour_research_report.md.

B101 determines all eight diagonal augmented-row stabilizers inside the
actual old-base kernel. It retains the four marked section maps, three
actual bridges, their inverse arrays and both signed normal-closure
operators. The actual coordinate swap compares constant and moving
sections. Both cone classes are covered. Auxiliary Nielsen lifts are
not substituted for the full geometric surface monodromy.

B102 identifies the actual nodal E-cover by a relative homotopy comparison
of underlying spaces and fixed subspaces. It retains every based collar,
the primitive exterior products, and the fixed-node source peripheral ab.
Its H1 is M_ab and its H2 is the full Z2. The bounded Tate complex gives
the reduced fixed-coset module and exactly the old kappa edge. Ordinary
Brown--Loday coinvariants lose the needed E action. The Hopf sequence
retains the separate nonspherical quotient H2(M). A fixed graph of
dimension one does not prove kappa vanishes. The applicable full primary
Brown--Loday proofs were reopened and read at this use.

B103 gives a complete integral root-path normal form and exact boundary
integration for the full product-tree module. The actual124-letter
node(8,0) and its119780-letter transported image have42 and33162 terms.
The actual bi-order proves every unit of Z[G] is a signed group element;
such a unit can at most double the normal-form support. Thus the full
geometric head stabilizer fails every unit-multiple shortcut. The entire
input, operator words, reduction DAGs, dictionaries and boundaries have
independent exact replays. No whole-span nonmembership is inferred.

B104 proves faithful21-row and16-row models with the unique retained
forest completion and all genuine semilinear source Fox maps. Its exact
Tate extractor retains every transported diagonal coefficient. The
actual even-base finite model has32 one-cells and359 two-cells, over
G_ev=G semidirect F11:231 source cylinders and128 actual node faces.
All35 matrices,735 columns and695738 terms have independent replay,
as do all128 node cycles and every coefficient of the finite359 columns.
The latter have319438 terms and zero next-boundaries. All231 cylinder
and128 node two-cell involution maps are the genuine geometric maps,
not arbitrary lifts from one-chains; all node physical mates, signs,
conjugators,10144 boundary coefficients and double-F identities pass.
The prefilled cover is K(N_gen,1) with N_gen free, so its source-face
boundary is injective. The actual relative exact sequence
0→Z2→Λ^128→P→M_ab→0 identifies the entire node-orbit kernel; each
node-coordinate relation has a unique source-cylinder completion.
No kernel-finiteness or localization claim is made.

B105 resolves the actual image of the B100 torus attaching sphere.
Its old0 far lift has empty source correction. The actual node disk
and specified prefilled cylinder disks give a complete ten-term sphere
chain with sole node coefficient u-1, where u has infinite order in
the actual deck group. Finite support, rather than an unproved domain
claim for Λ, proves this coefficient has no left annihilator. The
sphere is therefore nonzero in Z2 and generates a free Λ orbit. Its
physical involution mate is a different node, with the full raw
conjugator and sign checked. The two private node rows give a free
rank-two spherical block. F exchanges its two basis vectors, so this
particular block is C2-induced and Tate-acyclic. It does not exhaust
Z2 or decide kappa. Root and independent full-proof reads and two
complete finite-matrix verifiers check the entire construction.

The reflection chart gives a separate exact geometric route: the
actual Z is a complement of22 affine lines and four conics, with
F(a,b)=(a,-b) and actual base point(199/200,0). Its fixed source has19
proved distinct punctures. Fourteen explicit squared puncture functions
give an actual equivariant28-puncture bundle off a finite discriminant.
Its source is exactly its fixed subgroup, discretely and in full
completion. The actual basepoint is checked over Q(zeta5). Inserting
critical fibers still requires a true fixed-lifting comparison; source
lassos at the19 punctures are not killed as extending section loops.
This route is retained as research without inflating the formal register.

The actual source image also has a finite operator description in the
enlarged fixed coefficient group: H=I semidirect S has19 specified
generators, and K/H=R/I with K=R semidirect S. The permutation module
has a finite presentation over F2[K], and J_I is generated there by the
eight peripheral operator seeds. The reduced augmentation kernel is
not thereby proved finitely presented. These categories are kept distinct.

The nonlinear comb basis gives exact group words, not only chain
coordinates. All128 node words have4946 letters and individual primitive
witnesses. The existing geometric stabilizer image has46944 letters,
with exactly the previously verified33162 abelian terms. All short
expansions and both full abelianizations have independent replay.
The actual coefficient section has a nontrivial commutator cocycle;
its conjugating corrections and involution defect are now explicitly
proved, with seven universal free-word identities independently checked.
This is a crossed action before abelianization. A compatible chosen
tree gives the precise generic selected-cone free product. The actual
node quotient and all source translates remain essential. Neither
individual primitivity nor this crossed action gives simultaneous
elimination, cone-class injectivity or a fixed lift in the filled group.

All five formal proofs pass complete independent review. The final
paper has{m['pages']} pages and274 statements:230 Proved,19 Refuted,
19 Open and6 Known. It has108 bibliography records with explicit
verification status and all49 task/lead rows. The final log is clean.
The exact visual inspections and before/after layout counts are in
records/checkpoint20_typesetting.txt. The failed initial TeX-format
attempt, unsuccessful exact-text patch diagnostics and successful
builds before and after the cosmetic bibliography repair are retained.

Main A remains at full marked generation and the actual Fox-unit gate.
Its previously screened full-profinite realization problem is not
replaced by a pro-p or unmarked recognition theorem. Main B remains
at the whole Smith edge, including nonspherical H2, the nonlinear
defect, actual compact coefficient comparison, projected source
comparison and final joint-source condition. The next work attacks
these using the finite exact complex, the genuine nonlinear free
basis behind the root paths, and the actual critical projection.

Every earlier checkpoint entry remains byte-exactly retained with
zero omissions. The one checkpoint ZIP now groups verification PNGs
inside a standard TAR, with standard hard links for identical bytes.
All original logical paths are individually digest-verified. PDFs,
mathematical sources, code, complete data, logs and reports remain
direct ZIP entries. This is a lossless encoding change; all nineteen
earlier archives are unchanged. Exact restoration instructions and
the nested-container hash are included.

The exact computation state at immutable capture follows:

{computations}

Final PDF SHA256:{m['pdf_sha256']}.
Next hourly review/checkpoint:2026-11-16 21:49:30 UTC.
We resume substantive work as soon as immutable capture completes.
'''
(ROOT/'records/progress_review_20h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md';s=p.read_text()
assert '## Twentieth-hour progress review\n' not in s
s+=f'''\n## Twentieth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B101--B105 determine all
eight row stabilizers, the actual full E-cover and Smith edge comparison,
complete integral chain coordinates, the finite whole-source-orbit
complex and a nonzero actual spherical block with its exact involution
cohomology. The full obstruction and both main decisions remain Open.
All49 task rows remain tracked. The complete timed review and research
records are records/progress_review_20h.md and
records/twentieth_hour_research_report.md. Next review/checkpoint:
2026-11-16 21:49:30 UTC.
''';p.write_text(s)
p=ROOT/'records/continuation_state.md';p.write_text(p.read_text()+f'''\n## Actual twentieth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_20h.md.
All writers are paused for immutable capture. Release immediately
when the ZIP completes, then independently verify and save that snapshot.
Both main full decisions remain Open. No checkpoint20 bytes may change
after capture. The standard nested verification-images TAR preserves
all original image bytes and paths; extract it with the supplied command
when restoring this checkpoint. Next review/checkpoint:
2026-11-16 21:49:30 UTC.
''')
print('Timed twentieth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
 subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention=json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==19 and retention['archive_entries']==44877
assert retention['omissions']==0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'20'],check=True)
archive=ROOT.parent/'LM4_SUCCESSOR_checkpoint_20.zip'
assert archive.stat().st_size<=536870912,'Captured snapshot requires another lossless encoding; never mutate it.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
