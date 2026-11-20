# Contents and path conventions

The requested deliverables are the files beginning `SP46_CW_37_`, `pages/`, `progress.log` and `CHECK_EVENTS.tsv`. `PREAMBLE.tex` is the supplied macro preamble for interpreting the fragments. `readers/` preserves the three independent returns and their crops for each processed page. `decisions/` holds the main reader’s structured decisions from which the tables are generated. `crops/` holds additional main-reader crops. Brief versions, their history and scripts document the process.

The main changes log uses crop paths relative to this archive’s root. Some original reader returns record absolute paths from the working session. For a path containing `/out/readers/` or `/out/crops/`, the part after `/out/` is the corresponding path in this archive. Source image paths name the original attachment and are not copied here. No source scan, witness attachment or earlier checkpoint ZIP is included.

## Resuming a checkpoint

Restore this archive under `out/` in a working directory, and unpack the original supplied ZIP under `source/`. `scripts/resume_packets.py` reconstructs only the page packets from those supplied files and the accumulated notation. Do not rerun `scripts/init_work.py`: it is the historical initial setup and initializes empty logs. Read `progress.log`, the brief history, decisions and any incomplete reader returns before continuing. Start fresh independent agents for any page whose reading must be redone after an environment loss. Checkpoints are numbered separately and must not be overwritten or nested.

Source-reading decisions and documentary checks are distinct from mathematical proof checks. The event table identifies what actually occurred. TeX validation checks grouping and record structure without claiming a successful compilation.


If a checkpoint contains an unfinished current page, retain its partial reader files as documentation under an incomplete-run directory before starting three fresh independent readers for that page. Never treat a partial report as a completed pass, and never overwrite a completed decision or an earlier checkpoint. Source-image reads must be performed anew by the fresh readers; only the main reader may use completed earlier-page decisions and notation.
