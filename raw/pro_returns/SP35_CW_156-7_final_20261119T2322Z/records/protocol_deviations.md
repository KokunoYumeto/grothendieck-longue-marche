# Recorded protocol deviation

During a separate notation-equivalence audit, R2 attempted three LaTeX compilations of a synthetic glyph diagnostic despite the instruction prohibiting compilation. The calls used `pdflatex` once and `lualatex` twice. They failed or produced no readable PDF. No manuscript page, reader transcription, or consolidated transcription was compiled.

The main reader identified the issue in R2's audit, required an explicit account, stopped further diagnostic rendering/compilation, and disclosed the deviation in the conversation. The precise commands, captured error excerpts, available time bounds, and scope are recorded in `readers/R2/macro_equivalence_audit.json` and `.md`. Exact per-command UTC timestamps were not captured. The available bounds are after 2026-11-19 22:41:02 UTC and before 22:54:12 UTC.

Before the main reader requested preservation, R2 had removed the unsuccessful synthetic source/output/log files during an audit-save cleanup. This loss is explicitly recorded. The two source variants retained in the archive are labeled reconstructions from the recorded commands, not original surviving source files or logs. A later font-outline diagnostic PNG survives; it was made from the local AMS font contours and recorded drawing coordinates, without OCR.

The final validation uses source inspection, brace/environment checks, documentary coverage checks, ZIP integrity checks, and SHA-256 comparison. No further compiler or rendering invocation is authorized or used by those validation scripts. The compilation prohibition was therefore not followed perfectly in this run; the narrower statement that no manuscript transcription was compiled is accurate.
