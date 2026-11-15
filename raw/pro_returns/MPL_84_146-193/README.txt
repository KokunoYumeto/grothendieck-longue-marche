MPL_84_146-193 — COMPLETE TRANSCRIPTION AND RESEARCH NOTES
Montpellier archive, cote 84, scans 146–193

MAIN DELIVERABLES

MPL_84_146-193_transcription.tex
    The frozen diplomatic LaTeX fragment, in scan order, without a preamble.
    It is the newline-joined contents of the 48 files in pages/.

pages/MPL_84_146-193_84_scanNNN.tex
    One frozen fragment for each scan, 146 through 193 inclusive.

MPL_84_146-193_doubts.md
    The shared notation table, 710 indexed doubtful readings, abbreviations,
    and a candid account of legibility and the limits of the reading.

MPL_84_146-193_inventory.csv
    The required eight-column inventory: 750 elements, all transcribed=yes.
    The packet contains 24 text leaves and 24 reused_typed leaves.

MPL_84_146-193_notes.md
    The authoritative assembled research report: 208 indexed items, context
    comparisons, authorial self-checks, titles and pagination, all table and
    enumeration registers, explicit local calculations, and bibliography.

progress.log
    Actual UTC timestamps for initial completion and the second visual audit
    of each page, the notation comparison, freezing, context access,
    checkpoints, final verification, and completion.

RECORDS AND REPRODUCIBILITY

records/ retains the per-page inventory/doubt records, audit records, notation
work, research components, per-item context searches, mathematical check
scripts and results, independent reviews, and technical validation reports.
Research component files document assembly; use the assembled notes file
above as the final report. Historical .patch files record pre-freeze technical
review proposals and are not changes to apply to the frozen transcription.

The supplied photographs and context files are not included in this archive.
No OCR was used. All scan reading and the second visual audit were performed
by the same reader in one sequential stream. Later parallel review concerned
the frozen text, research, mathematical checks, and technical validation.

The TeX is intentionally a fragment. The requested state macros need suitable
definitions in the enclosing document. records/validate_tex.py retains the
complete test preamble and the temporary compilation procedure used here;
its identity-style macro definitions are a syntax-check harness, not a
publication design. The final recorded check compiled all 48 fragments with
no failures or missing-character warnings. Syntax and layout checks cannot
certify the correctness of a doubtful manuscript reading.

The following calculations can be rerun from this directory with Python 3
and SymPy (1.14.0 was used); the typed counting script needs only Python's
standard library:

    python records/early_formula_checks.py
    python records/recompute_quadratic_algebras.py
    python records/recompute_chi_groupoid.py
    python records/recompute_typed_counts.py

Their JSON results distinguish universal identities from finite examples
and author-reported counts from counts recoverable from this packet.

records/transcription_freeze.json records SHA-256 for all 48 page files and
the combined fragment, frozen at 2026-11-15 11:56:21 UTC. The context was
opened only afterward, at 11:56:32 UTC. To verify those hashes again:

    python records/freeze_transcription.py verify

The verify command appends its actual verification time to progress.log;
it does not modify any transcription file. The final verification performed
for this delivery is already recorded in progress.log.
