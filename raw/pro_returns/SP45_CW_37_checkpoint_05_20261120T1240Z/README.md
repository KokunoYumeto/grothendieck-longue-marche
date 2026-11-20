# SP45_CW_37 — consolidated diplomatic second pass

The LaTeX fragment and `pages/` contain the consolidated transcription. They use
the supplied `PREAMBLE.tex`; no additional transcription macros are introduced.
Standard LaTeX and TikZ commands, including local line-thickness settings for
explicitly drawn cancellation geometry, are used where needed.
The scan numbers are the page numbers of the Montpellier archive PDF. H's page
number is one lower. The supplied images and draft witnesses are not copied
into this return.

The changes log records substantive differences from C and H, including
resolved C doubts. The collation TSV contains only differences from H where H
has actual transcribed text. C doubts retained without a textual change are
recorded separately. The inventory lists page elements; the doubts file begins
with the cumulative notation observations. Notes describe only these pages.
`CHECK_EVENTS.tsv` distinguishes documentary checking and mathematical
reasoning from statements merely carried while transcribing.

The workflow record contains the first and last reader briefs, revision
history, and crop counts. `readers/` preserves each fresh reader's independent
complete reading, report and inspection crops. `decisions/` preserves the main
reader's page decisions, including the readings selected between. `crops/`
contains additional main-reader inspection crops. Crop metadata identify
original source coordinates and processing. No OCR or text-recognition output
is used.

`progress.log` gives UTC start and completion times and the frozen
transcription hashes. `scripts/` contains the mechanical record builders and
crop utility. These scripts format decisions and check structure; they do not
read text from images or choose a transcription.

Checkpoint ZIPs are created only at the requested 45-minute intervals. Their
names and saved identities are listed in `CHECKPOINTS.tsv`. No earlier
checkpoint ZIP, full scan image, witness file, or supplied attachment is
nested inside this package.

This file describes the package structure. For actual completion status, use
`progress.log` and `run_state.json`.

For resuming from a checkpoint, the per-page witness packets are regenerated
from the supplied sources with scripts/prepare_packets.py. Then run
scripts/extract_c_marks.py on that packet directory to restore the mechanical
C-mark coverage lists. The packets are deliberately excluded from this ZIP
because they reproduce the supplied witnesses; retained reader reports and
main decisions provide the inspection record.
