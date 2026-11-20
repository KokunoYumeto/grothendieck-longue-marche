# Provisional workflow findings — through scan029

**Scope:** text-only synthesis of existing records for scans003–029 (27 pages, 591 recorded marks). No images were inspected and no new ink check, adjudication or proof is supplied. These lessons remain provisional; the pages differ in difficulty. Sources: [WORKFLOW.md](../WORKFLOW.md), [METRICS.tsv](METRICS.tsv), and the linked audit reports.

## Fresh contexts and allocation

Keep a fresh visual context for each page, with compact textual comparison guidance and mandatory inspection of each occurrence’s own ink. Parallelize only disjoint subsets of the current page; keep nested parent/child marks together and complete review before the next page. Current allocation is one reader below six marks, two for 6–17, and three for at least 18.

Mark count is an imperfect workload proxy: scan015’s 9/8-mark groups took 125/295 seconds. Lower-threshold observations are mixed: accepted rates were 165.2 marks/hour on two-reader scan018 versus 201.8 on one-reader scan017, and 453.2 on three-reader scan020 versus 296.9 on two-reader scan019. Cancellation, rotation, mark length and reconciliation differ; these comparisons establish no causal speed or accuracy gain. [Workflow](../WORKFLOW.md)

## Contextual views and selective peers

Reuse a readable line/band crop across neighboring marks, while checking every mark individually. Each reader must personally inspect any reused crop and record that actual view. Primary crops/mark were 28/16 = 1.750 on scan007 and 33/34 = 0.971 on scan008. Add detail views for named unresolved features; impose no crop cap. Peers supplied with coordinates should begin with an adequate contextual crop and use a full page when localization requires it. [Workflow](../WORKFLOW.md)

Select peers for plausible competing readings with a distinguishable surviving feature, or substantial recovered corrections. After adequate primary views, independent inspection and a targeted reconciliation, stop when no discriminator survives. Preserve clear text and remaining uncertainty rather than seek agreement through repeated identical views.

Scan016’s four checks used eight crops and settled zero additional marks. Scan025’s seven checks used sixteen crops, also settling zero additional marks, while narrowing M0480 to mu/nu. Scan027 M0538 stayed uncertain despite a peer preference; scan028’s final e count and canceled connective remained unresolved. All four scan029 peer targets remained undecided: the sigma/r pair, correspondante/considérée, and alors. [Workflow](../WORKFLOW.md), [scan028](scan028.json), [scan029 peer](scan029_peer.json)

## Concise annotations: measured limits

Keep one or two specific evidence sentences per mark, retaining distinguishing strokes, limitations and actual view provenance.

| Recorded measure | Scan024 | Scan025 |
|---|---:|---:|
| Marks | 66 | 42 |
| Observation words | 2,815 | 1,438 |
| Words/mark | 42.7 | 34.2 |
| Final primary JSON bytes | 56,046 | 39,920 |
| Bytes/mark | 849.2 | 950.5 |
| Primary crops/mark | 0.848 | 1.548 |
| Accepted interval, seconds | 636.5 | 546.5 |
| Accepted marks/hour | 373.3 | 276.7 |

Words/mark fell 19.7%, calculated as `100 × [1 − (1438/42)/(2815/66)]`. Total JSON size fell, but bytes/mark increased. Shorter recorded prose therefore coexisted with more crops/mark and lower throughput; different ink and interruptions prevent attributing speed or accuracy to annotation length. [Workflow](../WORKFLOW.md), [primary parts](parts/), [metrics](METRICS.tsv)

## Timing and amendment identity

Primary elapsed time is latest final primary finish minus earliest start; accepted elapsed time is commit minus earliest start. Rates are `3600 × marks / elapsed seconds`, including undecided marks. These are wall intervals with possible waits, not continuous active reading. Include supplemental own-ink revisions in final primary timing, as corrected for scan021; keep independent timing/views separate. [Provenance](PROVENANCE_NOTES.md)

Preserve original submissions, actual visual-reader identities and previous check events. Amendment A0001 retains stable marks M0334/M0335 while assigning refined statements `M0334@v2`/`M0335@v2`, separate refutation/re-proof events and before/after archives. Its two-mark re-proof took a recorded 47 seconds and seven crops plus one page view; original primary metrics remain intact. Unmarked source bytes and page order are preserved. [Amendment manifest](amendments/A0001_unift_020_021/manifest.json)

## Timed checkpoint reliability

Checkpoint01 creation was 29 seconds late; checkpoints02/03 were created at their due times, exactly 45 minutes apart, with saves confirmed five/four seconds later. This measures scheduling only. Recorded process loss and the ineffective detached restart must remain explicit: their causes are unestablished. Resume from persisted due time, verify heartbeat/liveness, and create no early ZIP on restart. Preserve pending submissions as uncommitted snapshots; exclude source material, inspection images and earlier ZIPs. [Workflow](../WORKFLOW.md), [creation log](checkpoints.tsv), [save log](checkpoint_uploads.tsv)
