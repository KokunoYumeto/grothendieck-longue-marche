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
