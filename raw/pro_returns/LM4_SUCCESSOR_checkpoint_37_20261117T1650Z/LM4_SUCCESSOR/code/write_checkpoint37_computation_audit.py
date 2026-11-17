"""Write the completed37 audit only after the final real size producer succeeds."""
from pathlib import Path
from datetime import datetime, timezone
import json

ROOT=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((ROOT/rel).read_text())
m=read('records/checkpoint37_metrics.json')
v=read('records/checkpoint37_visual_review.json')
a=read('records/checkpoint37_final_pdf_audit.json')
e=read('records/checkpoint37_size_estimate.json')
late=read('records/checkpoint37_late_transporter_root_review.json')
assert m['pdf_sha256']==v['pdf_sha256']==a['final_pdf_sha256']==e['current_main_pdf_sha256']
assert v['visual_review']=='PASS' and a['final_overfull_count']==0
assert e['estimated_total_with_allowance']<536870912
assert late['result']=='PASS_COMPLETE_ROOT_AND_INDEPENDENT_SYMBOLIC_SOURCE_REVIEWS'
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_37.zip').exists()

text=f'''# Checkpoint37 computation, source and typesetting audit

Recorded at {datetime.now(timezone.utc).isoformat()}. This audit precedes
the sole immutable capture. Archive closure, post-closure verification and
delivery are not claimed here. Actual producer exit observations are
separately bound by the root pre-capture record.

## Mathematical computation and proof scope

The new Main B producer is
`work_CE/code/check_three_color_source_reduction37.py`, SHA256
`d3eaab5671c63a1fc80f176482d0d20aa5479ba209a1562666ae8afcdd54fccf`.
Its actual run exited0 (CE tool chunk79935c). Its full report contains
353 checks, has45579bytes and SHA256
`e2ba96dc91595647cdf38063ca691ae429d75e111b6b1354037258ab1937ca9a`.
The exact actual-run receipt is
`work_CE/three_color_source_reduction37_observed.json`.
CE and DE read the entire report; root read the entire producer, actual
run receipt and DE's complete independent formal-evidence review. Root
does not claim an additional whole-report reading or a rerun.

The calculation checks the actual index-two source and all signed node
actions at the stated three-color quotient. Its353 checks do not decide
the original Main B centralizer or original joint contact kernel. The
full mathematical proof separately supplies the finite-index transfer
and retains the complete signed source saturation. Later four-color,
bar-B and bar-a explorations are retained at their separately stated
source-only scopes; no unrun checker is presented as a computation.

The six new formal proofs are A.126--A.130 and B.174. Each has complete
root and independent source reviews bound to its exact final bytes.
The existing A.121 proof received a substantive literal-conjugation
repair: the two different meridian conjugates are distinguished, the
shifted mixed relation is proved from the presentation, and the ordered
cubic cancellation is completed. The complete author-version primary
Proposition2.20(2) was freshly reopened at the relevant proof; it printed
the same affected intermediate rows. No unseen publisher-version check
or failed screenshot is claimed. The statement's pentagon-only scope
is retained, without a hexagon or GT structure for the word w.

The later complete explicit-transporter and negative-hexagon proofs now
give a_w=1, b0=1 and the literal h_u=phi(sigma^2,tau^2), with its explicit
Brunnian coboundary and an ORIGINAL-Theta-fixed corrected cubic. Their
entire source proofs and independent reviews are retained in the late
transporter root-review record. They are supplemental research for the
next formal cycle; the frozen PDF count is unchanged. The specified
boundary and original CM frame comparison remain Open.

## Actual build history and corrections

The initial unconfigured invocation exited1 (610bf3), because the TeX
format was unavailable; it did not reach mathematical layout. The
configured second invocation, session79648, exited1 (e4d48f) on an
improper-prevdepth error in an A.127 proof-internal heading. Complete
predecessor sources and logs were retained. The independently reviewed
heading-only repair changed A.127/A.129 proof headings without changing
their mathematics.

The third invocation, session89194, completed its TeX passes but the
wrapper exited1 (1978dc) because one A.130 display overflowed26.55002pt
on physical page246. The complete rejected718-page edition, all logs
and the actual overflow image were preserved. A preservation helper
itself first exited1 (331a0d) after copying all files, because its PDF
text locator expected T(V) while extraction contained T(V ). That
failed helper is unchanged. A separate completion helper exited0
(04d0f9), located page246 and rendered it. Root actually viewed that
overflow image. Splitting the display into three rows repaired it.

A subsequent clean build, session76904, exited0 (b07e37). Its complete
edition was retained before the newly found A.121 mathematical repair.
The final corrected build, session70791, exited0 (20b7cb), with complete
driver output read and empty stderr. Its final pass directory is
`records/build_passes/20261117T154426785434Z`.

During final image review, DE initially reported a missing B_u in the
prose following A.127.27. The literal factor was already present. Exact
source and PDF extraction, and independent full-page views by DE, root
and CE, confirmed it. The alert was explicitly retracted. The attempted
preparation failed at its guard before any mutation; its exact entire
source, exit1/output and retraction remain retained. Root had copied
the unchanged edition while the alert was pending; those additional
copies and the pending-reason record are retained with a separate
retraction. No source, PDF or render changed after this false alert.

## Final PDF and actual visual review

The final paper has {m['pages']} pages, {m['pdf_bytes']}bytes, SHA256
`{m['pdf_sha256']}`. It contains389 statements:345 Proved,19 Refuted,
19 Open and6 Known, with117 bibliography entries and49 task rows.
Both main decisions and actual CM parity remain Open.

Before this integration the accepted36 PDF had zero overfull boxes.
The rejected third37 build had one26.55002pt overflow; after repair and
the A.121 correction the final edition has zero overfull boxes, zero
warnings, zero unresolved references and zero errors. The actual final
engine/stabilized logs each have {a['final_underfull_count']} underfull
notices, versus23 in the accepted36 baseline. The added notice is the
1194-badness paragraph at source lines223--235. It is not an overflow;
all affected/new proof intervals were visually reviewed.

The final144dpi render contains51pages and6contact sheets. All24 new
mathematical pages227--246 and626--629, and all4 mandatory corrected
A.121 pages215--218, were individually opened by the assigned reviewers.
The combined exact-byte record covers37 individually viewed pages.
Root separately opened every contact sheet, plus pages1--7,234,246,708
and719 as individual image blocks. The previously overfull display on
246 now fits in three clear rows. No truncated image output is counted.
The sole nonblocking note is tight spacing at an existing prose/citation
boundary on page6; all characters remain legible. Final visual
aggregation exited0 (249b91), and its complete output/empty stderr was
read in e24897. No old physical page number substitutes for a current
image review.

## Size estimate, failed attempt and lower-memory replacement

The first exact size attempt, session12069, actually exited137 (c11211).
The shell reported Killed. Its last progress line was504365056 of
624814080 input bytes for the prospective image TAR. It produced no
completed bundle certificate or final size report, and no ZIP was
opened. Its entire source, stdout, empty redirected stderr and actual
shell-exit output are preserved under
`records/checkpoint37_failed_size_estimate_137/`. The memory-risk
mechanism was overlapping snapshot buffers, a large encoder and an
online decoder. No inaccessible cgroup limit or unobserved OOM cause
is asserted as fact.

The separately reviewed replacement stages exact frozen logical bytes
and deterministic standard TARs outside the project. The staging
process exits before a fresh streaming encoder, which exits before
independent full standard-library decoding. It retains the512MiB image,
256MiB document and64MiB data dictionaries. Actual newly added duplicate
paths are retained; the earlier failed image length/hash is historical,
not a false identity requirement for a later snapshot.

The second exact streaming run, session41501, actually exited1
(96b054) only at the final delivery-cap assertion. All three encoders and
all three independent decoders had already actually exited0 and fully
verified their streams. Its estimate was545978789bytes before the
unchanged5000000-byte allowance, and550978789bytes with it, exceeding
the536870912-byte cap. Its complete stdout and traceback were read
(503227), and the entire report, source dependencies and logs were
retained by the successful preservation helper (fcc3ed). The failed
outer producer is never presented as successful.

The subsequent reviewed revision preserves every logical byte and
widens solid data storage to supporting text while retaining current
root deliverables, code and formal sections as direct entries. It
keeps all three dictionary sizes unchanged. Freshly staged image and
document TARs may reuse those actual successful worker measurements
only after exact full SHA256, CRC32 and length identity and unchanged
codec/staging bindings have been checked. The retained earlier outer
exit1 remains explicit. The revised data TAR is actually encoded and
independently decoded in separate processes. No unmeasured compression
saving, discarded history, test ZIP, or changed allowance is used.

The actual completed final estimator reports
{e['estimated_before_allowance']}bytes before the unchanged5000000-byte
allowance for headers, manifests, retention growth and late text, and
{e['estimated_total_with_allowance']}bytes including that allowance.
The delivery cap is536870912bytes; conservative estimated headroom is
{e['estimated_headroom_bytes']}bytes. All three actual prospective
streams are bound to full length/SHA256/CRC32 identity, real method14 headers,
decoder EOF and no-tail checks in the size report. No test ZIP or
substituted earlier compression saving is used.

The estimator starts from the exact verified529083340-byte checkpoint36
with SHA2569279885c2a7ab2d1d5396f57c4e372e6fa672b5f7f6dcd4a6965df07297f3f8e.
It predicts all changed36 logical bytes under historical paths. The
old direct main-PDF payload is subtracted exactly once only when its
identical bytes are counted in the prospective historical-document TAR;
its ZIP headers are not subtracted. The actual immutable archive size
and all post-closure verifiers remain the final delivery checks.

## Capture and retained history

The scheduled37 progress review was due15:49:30UTC and was actually
recorded15:52:12.550320UTC, with decision CONTINUE. The next review is
16:49:30UTC. The single capture orchestrator has waited without opening
a ZIP while genuine final readiness is completed. No off-cycle/test
archive has been created.

The closed36 parent anchor pins11156 logical parent entries and173786
inherited historical identities, giving184942 retention rows for37.
Its trusted verifier records have actual observed exit0. Prior archives,
failed attempts, superseded sources and all named proof/review records
remain retained. The exact retention commit and sole37 closure occur
only after explicit writer pauses and all six actual final producer
completions. All three writers are to be released immediately on actual
capture exit0, before the three complete post-closure verifiers and the
single authorized save. None of those future outcomes is preclaimed.
'''
with (ROOT/'records/checkpoint37_computation_audit_state.md').open('x') as stream:
    stream.write(text)
print(json.dumps({'result':'COMPLETED_COMPUTATION_AND_QA_AUDIT_WRITTEN','pdf_sha256':m['pdf_sha256'],
                  'estimated_total_with_allowance':e['estimated_total_with_allowance']}))
