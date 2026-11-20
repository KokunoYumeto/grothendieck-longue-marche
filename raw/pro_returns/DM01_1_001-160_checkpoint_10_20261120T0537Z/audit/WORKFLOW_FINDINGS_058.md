# Workflow findings after scan058

Measured 2026-11-20T03:58:15.198981Z by a read-only audit computation reviewed by /root. This completes the pending comparison in WORKFLOW_REMINDERS_054_BASELINE.json; that historical baseline remains unchanged. The full calculations, page and individual-reader intervals, definitions and input hashes are in WORKFLOW_FINDINGS_058.json.

## Changes being observed

The dispatch reminder from scan053 asks that the reported crop contain all decisive ink. The additional reminder from scan054 asks that each word or component left outside an uncertainty wrapper have its own visible support. Both clarify existing inspection requirements; neither reduces inspection depth.

## Descriptive comparison

| Measure | Before: scans048–052 | After: scans054–058 |
|---|---:|---:|
| Marks | 65 | 106 |
| Accepted page windows, seconds | 1470.115734 | 2195.727849 |
| Marks per accepted-window hour | 159.17 | 173.79 |
| Sum of individual primary intervals, seconds | 1741.692546 | 3306.978040 |
| Marks per individual-primary-interval hour | 134.35 | 115.39 |
| Primary crop views | 118 | 188 |
| Primary page views | 11 | 14 |
| Primary crops per mark | 1.815 | 1.774 |

| Final decision category | Before | After |
|---|---:|---:|
| first | 24 | 37 |
| alternative | 1 | 3 |
| other | 2 | 2 |
| undecided | 38 | 64 |

The accepted-window rate increased 9.2%, the individual-reader-interval rate decreased 14.1%, and primary crops per mark decreased 2.3%. These are descriptive differences, not evidence of an effect caused by the reminders. The after cohort contains 42 resolved rows and 64 undecided rows; this is neither an accuracy score nor a count of additional resolutions produced by the reminders.

## Timing and scope limits

Accepted page windows run from the earliest primary start to commit and omit interpage dispatch gaps. Individual intervals are summed across readers, including overlapping work, waiting and revision gaps. They are not continuous active-reading time or CPU time. These individual-reader sums differ from the page primary spans used in some earlier findings. All rate numerators include undecided marks. View counts include primary inspections only, including repeated actual views, and exclude independent-peer views.

Different page content, mark difficulty, reader allocation, peer questions and revision gaps prevent a causal speed or quality conclusion. The unchanged baseline values all reproduced. The exact metrics bytes used in this measurement are preserved at workflow058_inputs/METRICS.tsv because the main metrics table continues to grow.

## Direct observations and practical consequences

M1026 required a crop-metadata correction but 0 new ink views and 0 reading changes. M1051 required a 12-second own revision with 1 new view; it broadened uncertainty and settled 0 additional marks. These directly documented cases are the triggers for the reminders, not estimated effects across the later cohort.

The after cohort also contains bounded reconciliations: M1143 withdrew a star reading when both readers lacked a feature independent of the cancellation junction; M1153 retained only individually supported words after 2 targeted repeated line views over 36.219123 seconds. Those outcomes illustrate why resolving the differing end of a phrase is insufficient to certify every shared preceding word. Their occurrence does not establish that the reminders caused them.

The useful practice is to describe the surviving feature and its obstruction, separate inserted and cancelled layers, and stop when an own inspection plus independent check lacks a discriminator. A broader uncertainty wrapper can be a successful correction even when it adds no resolved mark. More crop views alone do not establish accuracy or recover missing ink.

## Reproduction

Run `python deliverable/scripts/measure_workflow058.py` from the restored workspace, or pass `--workspace` explicitly. The installed script records its execution time and hash; its prepared original is retained under revisions/measure_workflow058_prepared.py. No manuscript images were opened for this measurement. The script validates committed audit inputs and leaves all files unchanged.
