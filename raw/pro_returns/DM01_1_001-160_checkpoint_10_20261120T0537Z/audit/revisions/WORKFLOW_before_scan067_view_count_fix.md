# Workflow: DM01_1_001-160

## Initial setup — 2026-11-19 22:06:43 UTC

All 2,684 listed marks are to be inspected visually, with no OCR or text recognition. Pages are completed in source scan order; a page is not marked done until every listed mark on it has an ink-based record. The supplied alternative transcription is a comparison aid, never proof.

A fresh reader context will be used for successive page readings where feasible to keep earlier images out of later visual work. Readers inspect the original page for location, then use pixel crops enlarged with Pillow (and contrast adjustment only when needed). Several adjacent marks can share one crop; every mark must still be visually checked. Parallel work is restricted to the current page and mechanical tooling, so it does not defeat the required page order. Difficult places may receive an independent reading before the page is committed.

Decisions are recorded with observed strokes, original-image crop coordinates, confidence, reader/run identity and UTC check times. Unsettled ink remains explicitly uncertain, including completely illegible spans. Only mark spans may be replaced in the LaTeX; a balanced-brace parser and source/output comparison check this mechanically. Unmarked errors are recorded separately without correction.

The initial pass has no measured throughput yet. Per-page timing and crop-use measurements will be recorded in the page audit files; changes in method will include before/after measurements when available.

Checkpoints are due every 45 minutes from the first line of progress.log. They contain current deliverables, audit files, and scripts, excluding source attachments, images, source text copies and earlier ZIPs. They are newly named and never overwrite earlier checkpoints. The final package includes the complete deliverable state.

## Execution log

### 2026-11-19 22:09:17 UTC — source geometry and indexing (logged)

The supplied scan003 is 1746×2230 pixels. All coordinates therefore use measured file dimensions, not the generic dimensions stated in the prompt. The balanced-source parser identified nested marks and several MARKS.tsv escape/newline artifacts; these are documented in audit/SOURCE_ANOMALIES.md. This is a correctness adjustment before first-page commit, so no before/after throughput comparison is yet available.


### 2026-11-19 22:11:22 UTC — sequential page coordinator and fresh reader contexts

After scan 003, a dedicated coordinator handles source-order dispatch, completeness/evidence review, mechanical reconciliation, and immediate dispatch of the next page. Each subsequent page has a fresh reader context; root handles timed checkpoints and user updates. Independent readings remain restricted to the same current page. The reason is to avoid carrying old scan images into later visual contexts while retaining one ordered, auditable commit stream.

Baseline: scan 003's 16 marks took 154 seconds of declared primary reading time (374.0 marks/hour), with 9 primary crop views (0.562 crops/mark) and 9 independent crop views (1.125 total crop views/mark including rechecks). Its 16 recorded decisions comprise both settled and explicitly undecided readings. No after-change throughput is available yet; the coordinator will calculate it from committed page timing without estimating unseen work.

### 2026-11-19 22:16:22 UTC — first fresh-context page measured; same-page splitting begins next

Scan 004 recorded all 13 marks in 276.3 seconds of primary reader elapsed time (169.4 marks/hour), versus 374.0 marks/hour on scan 003. It used 26 primary crops (2.000 per mark) and 9 independent crops for two difficult margin marks (2.692 total crops per page mark including rechecks). Eight marks were settled; five retained narrowed or original uncertainty. Independent reinspection concentrated uncertainty on the argument of M0024 while securing its T and two primes. Different handwriting density, deletion severity, and marginal crowding mean this is not a controlled speed comparison. A fresh context avoids old images but did not by itself make this more difficult page faster.

Starting scan 005, pages with at least 24 marks will use two fresh primary readers on disjoint contiguous ID subsets of the SAME page. Smaller pages retain one primary reader. Both halves must finish and every ID must pass evidence/semantic review before a single ordered page commit; no future page starts earlier. Full half submissions and per-mark reader identities are retained. This uses available parallel capacity without reducing inspection of any assigned mark. After-change measurements will report page wall interval and total observed crop count; per-reader intervals are retained separately. No effect is claimed before the first split page completes.

Metric accounting correction at 2026-11-19 22:17:07 UTC: a full-image view recorded with numeric full-extent bounds counts as a page view, just as a box labeled `page` does. Scan004 therefore has one primary page view plus 26 crops and one independent page view plus 9 crops. The measured paragraph above and METRICS.tsv use these corrected counts; this changes no ink decision.

### 2026-11-19 22:20:56 UTC — first split-page measurements

Scan 005's two disjoint primary readings covered all 25 marks over 166.5 seconds from the earliest reader start to the latest primary finish (540.6 marks/hour). Elapsed time through accepted page commit, including coordinator review and the five reciprocal independent checks, was 245.9 seconds (366.1 marks/hour). The primary readers inspected 2 full-page views and 32 crops (1.280 crops/mark); independent checks added 8 crops, giving 1.600 combined crops/mark.

The two-reader setup settled 19 marks and retained 6 uncertainties. Three corrected upward-arrow readings were independently confirmed; two narrowed text uncertainties also agreed. The primary wall rate exceeds scan 004's 169.4 marks/hour, but the pages differ in density and difficulty, and the full accepted-commit interval includes additional checking. These measurements support continuing the threshold of 24 marks for a two-reader current page; they do not establish a controlled causal speedup. Raw half submissions and each mark's actual reader are preserved in audit/parts and CHECK_EVENTS.

### 2026-11-19 22:29:08 UTC — deletion stopping criterion and lower splitting threshold

Scan 006 recorded 10 marks: one first reading, three corrected Greek-letter alternatives, and six undecided readings. Primary reading and one targeted reconciliation occupied 353.0 seconds (102.0 marks/hour); elapsed through accepted commit was 432.0 seconds (83.3 marks/hour). Actual primary views were 1 full-page and 29 crops; independent views added 1 full-page and 14 crops, or 4.300 total crops per mark. Repeat inspections are counted as actual views, including the three declared final repeat views.

The evidence stopping criterion is now explicit: once adequate enlarged own-ink views and an independent inspection disagree without a surviving distinguishing feature, retain the shared clear text and mark the rest uncertain. One targeted reconciliation of M0060/M0061 removed an initially overconfident et and restored uncertainty to réciproque. No additional identical crops were requested after that reconciliation. M0058 retains the primary's narrower candidate set and its disagreement with the broader independent set is documented.

From scan 007, the two-reader threshold is lowered from 24 to 10 marks; pages with fewer than 10 retain one primary reader. Scan 006's small mark count nevertheless required two contexts because of several difficult deletions and repeated Greek forms. Disjoint primary halves from the start should use available parallel capacity better, with selective reciprocal checks afterward. Each mark must still receive adequate visual inspection. Scan 006 supplies the above observed baseline; an after-change rate will be recorded once 007 finishes, with page-complexity differences stated.

### 2026-11-19 22:36:08 UTC — first page below the old split threshold; shared crops next

Scan 007's two primary readers covered 16 marks, including final targeted reconciliation, over 389.0 seconds (148.1 marks/hour). Through accepted commit the interval was 425.6 seconds (135.3 marks/hour). Actual primary views were 2 page views and 28 crops (1.750 crops/mark); reciprocal checks added 13 crops (2.562 combined crops/mark). Eight marks were settled and eight retained uncertainty. The missing marginal l was removed after both readers saw blank paper; a complement symbol was selected and the margin wording changed to condition/technique at medium confidence. Differences in the reciprocal readers' confidence remain explicit in the audit.

Compared with scan 006's accepted-commit rate of 83.3 marks/hour, this split page has the above observed rate; the different page size and handwriting prevent isolating the effect of allocation. The large crop count also indicates avoidable image-context repetition.

From scan 008, readers will group neighboring assigned marks into readable enlarged line or band crops after locating them on the page, then use a tight detail crop for a specific unresolved small feature. Each mark still receives its own visual check and stroke evidence; no crop cap is imposed. This should allow a single adequate image to support several adjacent decisions. The next page's actual crop count and throughput will be reported before claiming any measured effect.

### 2026-11-19 22:46:02 UTC — shared-band measurements and coordinator handoff

Scan 008's two primary readers recorded 34 marks, including the final targeted reconciliation, over 496.7 seconds (246.4 marks/hour). Through accepted commit the interval was 562.7 seconds (217.5 marks/hour). They inspected 2 full-page views and 33 crops (0.971 primary crops/mark); reciprocal proof added 9 crops (1.235 combined crops/mark). Eighteen marks were settled and sixteen retained uncertainty.

The shared bands were actually used for adjacent marks, including the four cancelled-line marks M0090–M0093 and several margin marks. Primary crop ratio compares with scan 007's 1.750, and accepted-commit throughput compares with 135.3 marks/hour there. The recorded values show the observed outcome on a larger page; handwriting density, marginal rotation and cancellation severity differ, so this is not a controlled estimate of the crop method's effect.

After scan 008, root takes over routine coordinator duties. The former dedicated coordinator becomes inactive, freeing the third visual-reader slot. New pages with at least 30 marks will use three fresh disjoint readers, those with 10–29 use two, and those below 10 use one. Nested parent/child IDs remain together. Scripts support all three configurations, preserve full raw parts and per-mark reader provenance, and retain strict global page order. Shared-band inspection and selective reciprocal proof continue. The reason is to reduce elapsed reading time and accumulated images per reader while using the available four slots as root plus up to three visual readers. No effect of three-reader allocation is yet measured; the first such page under this policy is expected to be scan 010, and its actual outcome must be logged afterward.

### 2026-11-19 22:53:39 UTC — first timed checkpoint confirmed

Checkpoint 01 was created at 2026-11-19 22:52:12 UTC, 29 seconds after its 22:51:43 due time, and its persistent save has been confirmed. It contains the 114 committed decisions through scan 008, all documentation and scripts then written, and six complete pending scan-009 submissions; it does not promote pending rows into decisions or progress. It excludes source attachments, inspection images and earlier ZIPs. The first save therefore occurred after 45 minutes 29 seconds of work; the actual timing is retained rather than rounded to 45 minutes. The next checkpoint is due 45 minutes after this creation time.

Root has taken coordination after scan 008. Scan 010 is the first actual three-reader page (31 marks); its measured effect will be added after completion. Each reader now generates its own band crops containing several of its assigned marks. “Shared” refers to reuse across marks in one view, not a dependency on another reader to prepare images.

### 2026-11-19 23:00:07 UTC — first three-reader page measured

Scan 010 assigned 31 marks to three fresh contexts (11/10/10) on the same page. The initial primary interval, retaining the pre-reconciliation B submission, was 227.2 seconds (491.2 marks/hour); elapsed time through accepted commit was 382.0 seconds (292.1 marks/hour). There were 36 primary crop views (1.161 per mark) and 3 full-page views; nine independent mark checks added 16 crop views.

The page resolved 19 marks and retained 12 uncertainties. The checks confirmed the raised plus in R_*^+, a mu reading, and branching lambdas; the relation and worked delimiter traces in M0148 remain uncertain separately from its clear 0 and t. Accepted-commit throughput was 292.1 marks/hour versus 217.5 on scan 008 under two readers. Content and recheck work differ, so this is an observed comparison, not a controlled effect. The three-context policy continues for pages with at least 30 marks because it reduces each reader's assigned image/text span; smaller pages retain the established 1/2-reader allocation.

### 2026-11-19 23:16:11 UTC — staged coordinator phases

After committing scan 013, coordination changes to bounded phases. The coordinator reviews completed reports, reconciles or commits the current page, dispatches at most two visual workers, writes audit/COORDINATION.json and immediately returns. Readers report material progress and completed files directly to root. Root starts any third reader after the coordinator becomes inactive and triggers the next review phase when reports are ready.

This keeps three visual-reader slots available while the coordinator is idle and limits the coordinator's active text context during the long run. It preserves fresh per-page visual contexts, strict page order, own-ink inspection, selective reciprocal checks, and one targeted reconciliation only when a specific surviving feature can distinguish readings. Pending original submissions are retained under audit/revisions before any requested revision. Root continues the 45-minute checkpoints and saves.

This orchestration change starts with scan 014's two disjoint primary readers. No after-change throughput or crop-use effect is yet measured; actual page intervals and views continue in audit/METRICS.tsv. The first accepted page under staged coordination will supply an observed comparison, with page-complexity differences acknowledged.

### 2026-11-19 23:20:44 UTC — concurrent spare-slot peer on scan 014

While the staged coordinator was inactive, root used the spare third visual slot for an independent scan014 check of M0242, M0249 and M0252. The peer confirmed one infinity sign and the cancelled plus current W arguments; its terminal-s observation on M0242 prompts one targeted primary reinspection. The primary and independent reports retain separate identities and timestamps. This is an observed use of available parallel capacity; no isolated speed effect is estimated.

### 2026-11-19 23:22:34 UTC — duplicate error-list entry consolidated

The two scan-003 espaces/anneaux reports concern the same unmarked location. They are now one other_errors.tsv entry, retaining both original observations in the page and independent audit files. No manuscript text or mark decision changed.

### 2026-11-19 23:22:40 UTC — first completed staged-coordination page measured

Scan 014 completed 15 marks: eight first, one alternative, two other and four undecided. The primary interval including the targeted M0242 revision was 315.9 seconds (171.0 marks/hour); through accepted commit it was 360.7 seconds (149.7 marks/hour). Primary readers inspected 1 page views and 25 crops (1.667 crops/mark), while the concurrent independent reader added 1 page views and 10 crops (2.333 combined crops/mark).

The independent report confirmed M0249 and M0252 and supplied the specific terminal-s feature that one primary reinspection accepted in M0242. All three final readings agree with that peer report. These are observed measurements for the first completed staged page, not an isolated causal estimate of orchestration speed; page size and complexity differ from the preceding page.

### 2026-11-19 23:25:40 UTC — checkpoint timer separated from visual coordination

A yielding background checkpoint service now waits for the existing 45-minute due time, then creates the complete ZIP under the reconciliation lock and saves it with the prepared-upload helper. It never creates an early checkpoint and stops on an ambiguous upload rather than retrying blindly. Root monitors its state and stops it before final packaging. This removes dependence on a short gap in visual coordination; the prior manual checkpoint was 29 seconds late. No manuscript-reading throughput effect is asserted. The next due time remains 23:37:12 UTC; actual creation and save times will be recorded.

### 2026-11-19 23:28:49 UTC — root-direct visual dispatch

Scan 015's B reader completed its existing report after a period when root's agent inventory did not show that child. The report's interrupted crop requests without returned views were excluded from its evidence list. No duplicate reading was created and no missing report was fabricated. The cause of the visibility gap is unconfirmed.

Beginning scan 016, root directly spawns visual readers from the coordinator's persisted exact assignments/prompts. The staged coordinator continues bounded report review, reconciliation and commit phases, and returns promptly; root owns worker visibility and dispatch. This simplifies lifecycle tracking while retaining the same own-ink requirements. No causal speed or reliability effect is asserted before observation. Scan 016 has 14 marks and therefore needs two readers under either the current allocation or root's proposed lower three-reader threshold.

### 2026-11-19 23:30:13 UTC — allocation thresholds broadened for fresh visual contexts

Starting with the next uncommitted page, allocation uses three readers for at least 18 marks, two for 6–17, and one below 6. The current scan016 assignment is unchanged. The former thresholds were 30 and 10. Scan015 demonstrated a strongly uneven visual workload even with 9/8 mark halves: one primary took 125 seconds (259.2 marks/hour) and the other 295 seconds (97.6 marks/hour); word cancellation and marginal rotation, rather than mark count alone, caused difficult work. Smaller groups can use available parallel capacity and limit accumulated images per context. Selective reciprocal checks remain available after one primary finishes; there is no new quota for peer checks or forced resolution. The first newly split pages will provide actual after-change timings and crop counts, with content differences acknowledged. No throughput gain is claimed in advance.

### 2026-11-19 23:33:58 UTC — scan 016 supports the uncertainty stopping rule

All four independent scan016 checks remained undecided. They used 1 page view(s) and 8 crop views, and settled zero additional marks. Two reports expanded the stated alternatives without revealing a discriminating surviving stroke; those differences are preserved. The coordinator accepted the primary uncertainties and requested no repeated consensus pass.

For subsequent peer selection, priority remains a plausible competing reading with a specific visible feature, or a substantial recovered correction. Routine extra inspection of wholly obscured text is not a route to recovering ink that is absent. Every mark still requires adequate own band/detail inspection before an undecided result is recorded. This page documents the observed limit of additional inspection, not a reduction in the required primary care.

### 2026-11-19 23:35:54 UTC — direct root completion of a small page

Root reviewed scan017’s four-row report and committed it directly, without a separate coordinator turn. The fresh reader inspected one page view and seven crops over 64.1 seconds (224.7 marks/hour); accepted commit followed at 23:35:16 UTC, 71.4 seconds from the declared start (201.8 marks/hour). Three marks resolved and one remained uncertain. This is an observed small-page result, not evidence of faster ink reading. Scan018 is the first page newly split by the lower six-mark threshold: nine marks in groups of five and four. Its measured outcome will be recorded after commit. The new record_dispatch.py helper stores only actual dispatched assignments for restoration; it makes no manuscript decisions.

### 2026-11-19 23:37:17 UTC — timed checkpoint 02 confirmed

The complete checkpoint ZIP was created at 2026-11-19 23:37:12 UTC and its persistent save was confirmed at 2026-11-19 23:37:17 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

### 2026-11-19 23:39:38 UTC — first page under the lower two-reader threshold measured

Scan018 assigned nine marks as five/four to two fresh readers. The primary interval was 181.1 seconds (178.9 marks/hour), and accepted commit took 196.1 seconds (165.2 marks/hour). There were 24 primary crop views (2.667 per mark) and two page views; three independent checks added 11 crop views (3.889 combined crops per mark). Four marks resolved and five retained uncertainty. The peer corroborated the recovered Corollaire 2 heading; the interval and overwritten proposition numeral remained uncertain.

Scan017 under one reader had 201.8 accepted marks/hour and 1.750 primary crops/mark. Scan018 was slower and used more crops per mark despite parallel reading; its cancellation, overwritten numeral and comparison work differed, so these observations do not isolate the threshold effect. The lower allocation threshold remains a trial, with subsequent actual rates retained in METRICS.tsv. Root reviewed both complete row sets and the independent report, then committed and imported checks directly; no separate coordinator turn was needed.

The B submission phrase “Root independently supported” refers to root relaying /root/scan018_check’s independent visual result. Root did not inspect these page images. The raw original note remains preserved; the CHECK_EVENTS identities correctly attribute the visual checks to /root/scan018_b and /root/scan018_check.

### 2026-11-19 23:39:38 UTC — checkpoint timer outcome

Checkpoint02 was created exactly 45 minutes after checkpoint01, at its scheduled 23:37:12 UTC time, and its persistent save was confirmed five seconds later. The prior manual creation was 29 seconds late. The verified ZIP contains 290 committed marks on 15 pages and 131 files, with no source image, source folder or nested ZIP. This measures timer adherence only; it makes no claim about manuscript-reading throughput. The service continues to the next scheduled interval and will be stopped before final packaging.

### 2026-11-19 23:45:44 UTC — first page under the lower three-reader threshold measured

Scan020 is the first 18–29-mark page assigned to three readers under the revised threshold: 19 marks in groups of 7/6/6. The actual primary interval was 111.9 seconds (611.1 marks/hour), and accepted commit took 150.9 seconds (453.2 marks/hour). There were 3 full-page views and 22 primary crops (1.158 crops/mark). One reader, after finishing its primary subset, independently inspected another reader’s M0332 in one new crop; the 23 combined crops give 1.211 per mark. Its timing and view are separate from the primary report. Seven marks resolved and twelve retained uncertainty. The independent check confirmed the tall l-like loop making Cela plausible, but did not recover the canceled continuation, so it produced no additional resolved mark.

The preceding two-reader scan019 completed 16 marks at 296.9 accepted marks/hour, with 1.750 primary crops per mark. Scan020’s faster observed rate is not an isolated causal estimate: mark lengths, cancellation severity and recheck work differ. The three-reader threshold continues, with every mark still inspected in its own ink.

Routine review is now performed directly by root: read every submitted row’s stroke evidence and all selected independent reports, resolve any concrete inconsistency, merge, commit and import checks, then dispatch the next page. The coordinator remains available for complex source-span or reconciliation issues. This extends the direct process first used on scan017 and keeps an otherwise redundant coordinator turn out of straightforward pages. It changes orchestration only, not visual proof ownership. On scan020, the final independent report finished at 23:44:24.569749 UTC and commit followed at 23:44:53 UTC; these actual timestamps are retained without attributing the interval to faster handwriting reading.

### 2026-11-19 23:51:20 UTC — supplemental primary timing made explicit

Scan021 used five independent checks and two targeted primary revisions. The un/son comparison narrowed M0338 to borélienne dans un with complément still uncertain; M0345 retained uncertainty because the apparent membership sign matched a possible qui and its source-span boundary could not be isolated. The Ω and differing C subscripts were confirmed. Original primary submissions and all independent reports remain intact.

B recorded its M0345 supplemental review through 23:49:21.490286 UTC but left its earlier primary finish in the top-level field. Root normalized that field to the already recorded supplemental finish before merging, preserving both the initial finish and the complete pre-normalization report. No row or view changed in that metadata correction. The reader contract now explicitly requires final primary finish to include later own-ink revisions, while independent work keeps separate times and views. These are elapsed workflow intervals, including possible waits, not continuous active-reading time. This clarification changes timing accounting only; no manuscript-resolution effect is claimed.

### 2026-11-19 23:58:10 UTC — checkpoint process monitor strengthened

The yielding execution session for the timer was no longer available, and a process inspection found no checkpoint_service.py process. Its last persisted state was the successful checkpoint02 save; the next deadline remained 00:22:12 UTC, still in the future. The cause of process loss is not established. Root restarted the same due-only service as a detached process, with a PID file, a process log and a 30-second heartbeat in its working state. The singleton lock prevents concurrent copies. No early checkpoint was created or prior checkpoint altered. Root will inspect liveness/heartbeat during ongoing coordination and stop the service before final packaging. This is checkpoint reliability work, not a change in ink adjudication.

### 2026-11-20 00:01:02 UTC — heartbeat verified; detached attempt did not start

The detached timer invocation produced neither a log line nor a new working-state heartbeat, so it was not treated as a running service. Root restarted the due-only timer in a yielding execution session at 23:59:31 UTC. Its heartbeat advanced through 00:00:31 UTC and was verified afterward. The reason the detached child did not persist is unestablished. The direct-dispatch helper now reports heartbeat age and flags an error/stopped state or age above 90 seconds at each page dispatch. Root will check/resume a missing session using actual state; the existing due time stays 00:22:12 UTC. These attempts created no additional ZIP.

### 2026-11-20 00:05:49 UTC — audited amendment A0001_unift_020_021

The accepted independent re-proof refutes first/uniformt in M0334 (scan 020) and M0335 (scan 021): the surviving descending f is followed immediately by a raised t, with no written orm sequence. The clear same-page fully written uniforme supplies a positive comparison. Both marked readings become other/unift at medium confidence, preserving the written abbreviation rather than expanding it. Accepted by /root, following the independent own-ink report from /root/abbrev_recheck_020_021. The authoritative independent report is preserved unchanged at audit/amendments/A0001_unift_020_021/independent_report.json.

The separate re-proof interval was 2026-11-19T23:54:17Z to 2026-11-19T23:55:04Z (47 seconds). It covered 2 marks in 8 actual views: 1 whole-page view(s) and 7 crops. These are recorded review intervals, not a claim of uninterrupted viewing. The original primary timing and view metrics remain intact.

Only M0334, M0335 were amended. Original statements and all prior check events remain in the before archive; the refined statements are M0334@v2, M0335@v2. Separate refutation and independent re-proof events use the actual reader and check time. The amendment regenerates affected pages from original source, preserves every unmarked byte, and leaves page completion order unchanged.

### 2026-11-20 00:22:16 UTC — timed checkpoint 03 confirmed

The complete checkpoint ZIP was created at 2026-11-20 00:22:12 UTC and its persistent save was confirmed at 2026-11-20 00:22:16 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

### 2026-11-20 00:25:47 UTC — dense-page measurements and concise annotations

Scan024 completed 66 marks with three 22-mark primary groups: 30 first, 2 other and 34 undecided. The primary interval including two targeted revisions was 591.5 seconds (401.7 marks/hour); accepted commit took 636.5 seconds (373.3 marks/hour). Primary views: 3 pages and 56 crops (0.848 crops/mark). Nine selected independent checks confirmed the phi/index layers and successive canceled A/underlined-b, while preserving the unresolved margin mapping and formula attachment. Those peer reports log 19 additional crop views.

Starting with scan025, readers are asked to keep evidence to concise, specific one- or two-sentence observations and view-purpose notes brief, while retaining every distinguishing stroke and limitation. Relative view paths and explicit tuple-to-row serialization are allowed to reduce repeated annotation code; unread rows and bulk default decisions remain prohibited. The scan024 baseline comprises 2815 observation words (42.7 per mark) and 56046 bytes across its three final primary JSON files. No handwriting-reading speed gain is claimed; subsequent actual rates, annotation sizes and resolution counts will show the observed result with page-complexity differences stated.

Targeted peers with supplied coordinates should start from an adequate contextual crop, using a full page only if the target cannot be located. Extra views must address a named remaining feature, with no hard crop cap. On scan024 these bounded fresh peers used 9 views for the margin and 10 for the formula/word group; this is a recorded use of the approach, not a controlled comparison to scan023’s single rotated-word check.

### 2026-11-20 00:36:11 UTC — scan025 annotation measurements

Scan025 completed 42 marks: 25 first, 3 alternative and 14 undecided. The three final primary reports contain 1438 observation words (34.2 per mark) and 39920 bytes, compared with scan024’s 42.7 words per mark and 56046 bytes for 66 marks. The primary interval including the targeted M0480 revision was 538.4 seconds (280.8 marks/hour); accepted commit took 546.5 seconds (276.7 marks/hour), compared with scan024’s 373.3 accepted marks/hour. There were 2 primary page views and 65 crop views (1.548 crops/mark), compared with 0.848 crops/mark on scan024. Seven independent checks used 16 additional crops and no full-page views.

The concise annotation instruction reduced observed words per mark, while this page used more crops per mark and had lower accepted throughput. Different ink, mark lengths, interruptions and reinspection intervals prevent attributing a speed or accuracy change to annotation length. The checks confirmed 2 versus 1 and ayant versus muni, supported the four-word phrase order, and narrowed M0480 from mu/rho to mu/nu without resolving it. The script C/E, contracted insertion and canceled two-word fragment remained uncertain. No additional fully resolved mark came from these seven peer checks; their value was corroboration and a more accurate uncertainty set.

### 2026-11-20 00:36:42 UTC — include prefixed reader scripts in timed packages

Inspection found reader serialization scripts named write_scan025_b.py and similar names outside the former scan* snapshot glob. The package collector now accepts a scan number at the start or after an underscore, while retaining its explicit documentation/script suffix filter and JSON completeness check. Thus build_scanNNN.py and write_scanNNN.py are included at the next scheduled checkpoint and final package. The previous package script is preserved under audit/script_versions. No extra ZIP was created; no manuscript decision or reading rate changed.

### 2026-11-20 00:51:29 UTC — independent unmarked-error provenance

A new bounded importer incorporates an explicitly accepted peer other_errors entry into an uncommitted merged report, with the peer identity, actual check time, source report path/hash and exact accepted entries. It leaves all decision rows and primary timing/view metadata unchanged, and refuses to target primary parts or already committed pages. Its first actual use records scan027’s omitted unmarked donc before dans (5), from /root/scan027_peer; the source prose remains untouched. The actual before/after comparison confirmed every other merged field unchanged. This changes error-list bookkeeping only, adds zero resolved marks, and claims no reading-rate gain. M0538 remains uncertain despite a peer preference for the source reading, because the two reports describe the same obscured letter junctions without a new discriminator.

### 2026-11-20 01:07:19 UTC — timed checkpoint 04 confirmed

The complete checkpoint ZIP was created at 2026-11-20 01:07:12 UTC and its persistent save was confirmed at 2026-11-20 01:07:19 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

### 2026-11-20 01:07:44 UTC — count baseline letters before accepting a power reading

On scan030, M0607 was initially read as A^2 at high confidence. A supplemental 5x primary view revealed the second baseline A beneath cancellation; a same-line raised-glyph comparison then supported A^*A. The primary’s actual revision interval was 23 seconds with two added crops. An independent reader confirmed the second A but initially retained star/2 uncertainty; two concrete comparator crops, reviewed over an additional recorded 18-second interval, distinguished the forked closed-loop star form from an open numeral2. The final independent result is A^*A at medium confidence. All initial primary and peer reports are preserved; the erroneous draft was corrected before page commit. One draft mark changed, with no claim of a general accuracy or speed effect.

Beginning with scan031, the reader contract explicitly calls for counting each baseline letter and distinguishing its superscript from cancellation before high-confidence resolution of repeated-letter/power alternatives. This asks for adequate feature accounting, not a fixed zoom or an automatic extra crop. Subsequent observed metrics remain in METRICS.tsv; no after-change rate is asserted here.

### 2026-11-20 01:12:18 UTC — first page after explicit formula-letter accounting

Scan031 completed 13 marks with 9 first readings and 4 undecided. Its accepted interval was 241.0 seconds (194.2 marks/hour), with 24 primary crop views (1.846 per mark) and 2 page views. The preceding scan030 completed 17 marks in 329.0 seconds (186.0 marks/hour), with 1.000 primary crops/mark. These different pages and review workloads do not isolate an effect of the new guidance.

The scan031 readers explicitly separated U and its raised star at M0612 and the three lower letters E-A-E in the later M0621 term. Two independent checks used six crops. They did not add a fully resolved mark: the earlier struck fragment in M0621 was changed from a resolved draft to retained uncertainty, while its later three-letter subscript remained clear; M0620 narrowed to a/A with case unsettled. A final primary review added two crops. This demonstrates a documented correction of uncertainty boundaries, not a measured general accuracy gain.

### 2026-11-20 01:40:04 UTC — preserve source candidate metadata

A scan036 draft supplied M0719 candidate metadata B^*/B while its original candidates were B^*/E. Root removed that metadata override without changing the then-proposed uncertain reading, evidence, views or times, preserving the original report. The reader contract now explicitly says candidate metadata encodes source boundaries only; new possibilities belong in the reading. This is a schema clarification, with zero directly resolved marks and no claimed reading-rate or crop-count effect. A separate actual peer challenge and final primary view subsequently restored E to M0719’s uncertainty set; that visual revision and its 7× crop have their own timestamps and preserved reports.

### 2026-11-20 01:46:45 UTC — explicit empty replacement for absent marked ink

M0777 on scan038 is an other decision with an empty reading cell. Both the primary and independent reader inspected the complete deleted formula and its blank terminal region: the ink ends at the tensor sign, with no e-loop or index trace corresponding to the marked e_i. The empty value deliberately removes that marked token only; it is not a missing decision. Both full reports and actual view logs are preserved. Existing reconciliation already supports an empty other reading, so no source-application code changed. This accepted absence check corroborated one primary other decision rather than adding another resolved mark. Scan038 also resolved one previously uncertain draft, M0755, to rho_i(uv) after counting two baseline argument glyphs against same-page u/v comparators; M0764 remained undecided with a more literal abbreviated prefix.

### 2026-11-20 01:52:17 UTC — timed checkpoint 05 confirmed

The complete checkpoint ZIP was created at 2026-11-20 01:52:12 UTC and its persistent save was confirmed at 2026-11-20 01:52:17 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

### 2026-11-20 01:57:28 UTC — refresh final coordination counts

A mechanical completion recorder now refreshes counts from the actual decisions, check-event tables and receipts before archiving each page’s final coordinator state. Earlier manual final coordinator snapshots retained dispatch-time aggregate counts even after their final conclusions were appended; the authoritative tables and receipts were correct. Those earlier snapshots remain intact. This changes audit bookkeeping only, with zero ink decisions, no added crops and no claimed throughput effect.

### 2026-11-20 02:00:55 UTC — measured follow-up through scan039

The text-only synthesis in audit/WORKFLOW_FINDINGS_039.md records the next eight supplied pages after the formula-accounting clarification: 210 marks, 270.2 accepted marks/hour over the summed page intervals, and 1.433 primary crops/mark. The single scan030 comparison page had 186.0 accepted marks/hour and 1.0 crops/mark. These heterogeneous workloads do not establish causation or an accuracy rate. The synthesis links actual corrected drafts, narrowed or widened uncertainties and corroborated absences to their mark IDs.

### 2026-11-20 02:03:47 UTC — resumed readers and checkpoint service after interruption

At 02:02:28 UTC the prior checkpoint session was unavailable, its last heartbeat was 01:57:18 UTC, and the reader inventory showed scan040 A/B interrupted while C was not listed as live. The cause is not established. The filesystem and generated crops remained present, but no scan040 primary report had yet been saved. Root sent actual resume tasks to all three readers, requiring their own preserved-view history or reinspection rather than treating generated crops as viewed. Reader C confirmed that its prior context and personally viewed crops were intact. Actual resumed intervals remain in the primary reports; the precise interruption time is not invented.

The due-only checkpoint service restarted at 02:03:13 UTC in a new yielding execution session. The next deadline remains 02:37:12 UTC, 45 minutes after checkpoint05 creation; no early ZIP was created. The lost session is not reused. This interruption affects elapsed timing and must not be interpreted as continuous active reading or attributed to the handwriting workflow.

## 2026-11-20 02:19:25 UTC — current-document curation after scan 040

A text-only audit of scans 030–040 verified current row/reader consistency and mechanical substitution at 868 marks, 37 pages and 1,045 check events. One stale PATTERNS sentence for M0696/M0697 was updated from a pending check to its completed, still-uncertain outcome. The raw observations and historical snapshots remain intact. This documentation edit changes no reading, check event, crop or timing, and has no separately measurable reading-rate effect. See audit/AUDIT_040.json.

## 2026-11-20 02:27:21 UTC — unreadable fragments with unknown extent on scan 042

M0875 contains a separately established cancelled group between secure words; M0881 contains an unresolved crossed fragment before two secure v factors and a star. The notation \unsure{\ldots} is used as an explicitly editorial placeholder when the identity or extent cannot be counted, with \deleted{} only where cancellation is established. It does not assert written dots or a word count. Primary notes distinguish these meanings, and actual own-ink review times are unchanged by later notation edits. Both marks remain undecided, with narrower uncertainty. Seven selective peer checks on this page prompted three additional primary views; M0888 and M0889 became resolved, while the difficult fragments remained uncertain. These are within-page outcomes, not an isolated estimate of a speed effect; actual page intervals and view counts remain in METRICS.tsv.

### 2026-11-20 02:37:17 UTC — timed checkpoint 06 confirmed

The complete checkpoint ZIP was created at 2026-11-20 02:37:12 UTC and its persistent save was confirmed at 2026-11-20 02:37:17 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

## 2026-11-20 02:39:23 UTC — current coordination metadata clarified

The dispatch helper still labeled the optional earlier audit helper as coordinator, although root has directly reviewed and reconciled the recent pages. Future dispatches and current scan045 now identify /root as the coordinator; historical snapshots remain unchanged, and the prior script is retained under audit/revisions. The current stage records that all initial primary reports have been reviewed and lists the actual two peer assignments. This corrects work-state metadata only, with no change to ink readers, decisions, check events, view counts or measured reading rates.

## 2026-11-20 02:54:36 UTC — audited consolidation of repeated unmarked-error observations

OE0001_exact_aliases_042_044_046 was applied at 2026-11-20T02:53:43.996158+00:00. The table previously held 14 differently worded observations for 11 distinct errors: primary and peer reports for scans 042, 044, 046 had both been appended by import-check. Three explicitly reviewed full-row aliases now retain the existing primary rows verbatim, giving 11 error rows; both original reports and complete before/after tables remain archived. The correction addendum explicitly qualifies the inaccurate no-duplicate statements in historical scan 042/044 coordination notes, which were preserved. Both commit and independent import now use the same exact-field/SHA-256 alias registry; no similarity heuristic merges locations or readings. The verifier also rejects registered aliases and exact duplicate rows. Focused tests preserved an unregistered same-scan/same-reading observation at a different place, and the ordinary verifier passed at 965 marks, 42 pages, 1,175 check events after application. This record correction changes no ink decision, page text, proof event, reading interval or crop count, so it has no independent reading-rate effect. See audit/other_error_normalizations/OE0001_exact_aliases_042_044_046/CORRECTION.md.

## 2026-11-20 03:02:23 UTC — text-only pattern index through scan048

Integrated `audit/PATTERN_INDEX_048.md`, preserving its initial draft in `audit/revisions/`. The index summarizes current readings through 977 marks on 43 pages, including counterexamples, cancellation limits, factor counting, layer allocation and verified blank replacements. Two stale prospective sentences in PATTERNS.md (M0113; M0401/M0402) now state the already completed independent outcomes; raw historical reports remain unchanged. This documentation curation adds no ink checks, decisions, crops or measured reading-rate effect.

## 2026-11-20T03:04:14.820744+00:00 — scan003 exact error-provenance aliases

A text-only completeness audit found that the historically combined scan003 anneaux error row did not have registered aliases for its preserved raw primary and independent observations. Root reviewed both exact rows and added two aliases to the existing combined row in `audit/other_error_normalizations/OE0002_exact_aliases_003/`. The 11-row error table, marked decisions, check events, progress and page text are unchanged. This corrects provenance/reimport behavior only; there are no new ink checks, crops or reading-rate effects.

## 2026-11-20 03:05:39 UTC — error-table completeness audit through048

The bounded text-only audit `audit/OTHER_ERROR_COMPLETENESS_048.json` accounts for 43 committed primary reports, 96 referenced raw parts, 66 ordinary imported peer reports and the accepted amendment report. All 15 distinct raw error-observation identities map to the 11 canonical table rows after OE0002; no accepted observation is missing, no table row lacks provenance and all 213 independent events through048 have preserved report provenance. This supplements ordinary verify, which checks canonical uniqueness but not report-to-table completeness. The audit adds no ink judgment, check event, crop or reading-rate effect.

## 2026-11-20 03:19:53 UTC — crop-boundary clarification following scan052

The M1026 review found that the initially reported tight primary and peer boxes clipped part of the decisive right edge, although both readers had already inspected larger complete views. At 03:14:35–03:14:36 UTC they corrected only row crop metadata to actual inspected boxes, preserving initial reports and actual ink-finish times. Dispatch reminders now explicitly require the full decisive glyph within the reported crop. This clarifies existing provenance requirements: zero reading changes, zero added ink views and no reading-rate effect from the metadata correction. See the scan052 primary/peer reports and coordination record.

## 2026-11-20 03:21:52 UTC — explicit uncertainty-scope reminder

After M1051, dispatch wording now reiterates that words left outside an uncertainty wrapper require their own supported sequence, rather than only a few stems and an expected phrase. This clarifies the existing evidence standard. M1051 remained undecided; one additional actual own view over twelve seconds broadened its uncertainty, with no newly settled mark. Together with the crop-boundary reminder, a common prior cohort (scans048–052) is recorded in `audit/WORKFLOW_REMINDERS_054_BASELINE.json`; scans054–058 will supply an observational comparison. The comparison will report rates and crops without claiming causation across different page difficulty.

### 2026-11-20 03:22:16 UTC — timed checkpoint 07 confirmed

The complete checkpoint ZIP was created at 2026-11-20 03:22:12 UTC and its persistent save was confirmed at 2026-11-20 03:22:16 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

## Scan056 notation clarification

The existing unknown-fragment convention was applied to M1117 at the separately recorded primary/peer annotation times (03:43:22.568027 and 03:43:30 UTC). The literal `v. N.` was already visible in their own inspections; unallocated prefix strokes are represented by an editorial unsure-ellipsis, not guessed parentheses/dashes or a spelled-out word. Both original reports are preserved, actual ink finish/views remain unchanged, and no additional mark became settled. This is a notation clarification with zero new crop views or reading-rate effect.

### 2026-11-20 03:59:16 UTC — completed reminder comparison through scan058

The pending scans054–058 after cohort is complete. The unchanged scans048–052 baseline reproduced: 65 marks versus 106 after, accepted-window rates 159.17 versus 173.79 marks/hour, summed individual-primary-interval rates 134.35 versus 115.39, and primary crops/mark 1.815 versus 1.774. Final category counts before: 24 first, 1 alternative, 2 other, 38 undecided; after: 37 first, 3 alternative, 2 other, 64 undecided. These descriptive differences do not establish a causal effect because content, difficulty, allocation and revision gaps differ. Windows omit interpage gaps; individual intervals include waits and are not active/CPU time. Direct triggers remain M1026: 0 new ink views/0 reading changes; M1051: 12 seconds/1 view/broader uncertainty/0 newly settled marks. See audit/WORKFLOW_FINDINGS_058.md and .json, reproducible scripts/measure_workflow058.py, and the preserved input metrics snapshot. This completed finding supersedes the pending status in the unchanged historical baseline.

### 2026-11-20 04:07:17 UTC — timed checkpoint 08 confirmed

The complete checkpoint ZIP was created at 2026-11-20 04:07:12 UTC and its persistent save was confirmed at 2026-11-20 04:07:17 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

### 2026-11-20 04:15:57 UTC — incremental pattern synthesis through scan060

A text-only auditor checked all 219 accepted rows from scans049–060 and prepared audit/PATTERN_INDEX_060.md. Root reviewed the full index, its 43 mark examples and 26 explicit report links. No substantive stale pattern claim was found; a current prose label for M0992 was corrected from donne/fourni to donné/fourni, with before/after hashes and a preserved prior PATTERNS file. No ink reading, decision or check event changed. The index is a historical snapshot at 1,196 marks/55 pages, supplementing the earlier scan048 index. The short pause and resumption of this auxiliary task freed a slot for a current-page visual peer; it changed no inspection method. See audit/PATTERN_INDEX_060_REVIEW.json for integration and the historical auxiliary-status clarification.

### 2026-11-20 04:52:17 UTC — timed checkpoint 09 confirmed

The complete checkpoint ZIP was created at 2026-11-20 04:52:12 UTC and its persistent save was confirmed at 2026-11-20 04:52:17 UTC. It includes all deliverables and documentation then written, plus complete pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, source attachments and inspection images are excluded. The next checkpoint is due 45 minutes after this creation time.

### 2026-11-20 04:56:18 UTC — Scan 067 inspection cost and reconciliation

The 49-mark page required 110 primary views (A 51, B 30, C 29), including two full-page views and 108 crop views, plus 21 independent crop views for five selected marks. The sideways marginal text required rotation and multiple location/extent checks; A retained the actually viewed inverted locator and tight preliminary crops in its log. Later full-height crops supply the decisive recorded boxes. These are observed page-specific costs, not a new workflow or a before/after speed claim. Nine first readings, three listed alternatives and one other reading were accepted; 36 marks retain uncertainty. One initial lexical resolution (M1330) was withdrawn by text-only reconciliation because the ending did not establish the whole word. No added ink view was claimed for that withdrawal.
