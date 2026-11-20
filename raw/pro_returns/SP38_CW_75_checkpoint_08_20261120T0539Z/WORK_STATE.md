# Work state

Updated 2026-11-20 05:00:26 UTC.

Committed scans: 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015.

Current uncommitted scan directories: scan016. Only pages/ and records/ are adjudicated. Partial reader files are preserved as work in progress, not final decisions.

## Recovery and method

Restore this ZIP into out/ and reacquire the original attached source ZIP. The original input is SP38_CW_75.zip, supplied with PROMPT(20261119-225751).md; the final output intentionally has the same basename but is a new file. Original scans and witness files are not copied into this archive. Run scripts/rebuild_packets.py after restoring the input source folder; it derives its workspace path and only rebuilds packets. See RECOVERY.md. Do not rerun the historical setup_work.py over restored work.

Proceed scan by scan through 025. Use three fresh, independent fork_turns=none readers per page with the latest brief and notation snapshot; no OCR or outside research. Main adjudicates all differences on crops, records all C doubt dispositions and S decisions, and commits before starting another page. If active reader contexts are lost, preserve their incomplete attempts and restart that uncommitted page with three fresh readers; never call incomplete reports independent completed readings.

The progress clock began 2026-11-19 23:00:18 UTC. Checkpoints are due every 45 minutes from that time, uniquely numbered, without earlier ZIPs nested. CHECK_EVENTS.tsv includes preliminary checks for uncommitted pages via pending_events/. Final work requires structural verification, all 24 page hashes plus combined-text hash, a transcription-frozen log entry, and a final hash comparison. No LaTeX compilation was requested.
