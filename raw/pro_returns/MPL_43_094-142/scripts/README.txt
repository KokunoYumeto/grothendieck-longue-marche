Mechanical validation and packaging
===================================

This standard-library utility checks file structure, inventory values, sequence
and audit records, selected LaTeX syntax, exact combined-file concatenation,
and recorded SHA-256 hashes. It cannot certify the handwriting readings or
that every mark on each source image is represented.

It was prepared without reading any source image, context member, or existing
transcription. The transcriber runs it on the resulting files.

Commands, from any working directory:

  python /workspace/scratch/21054de32227/MPL_43_094-142/scripts/validate_package.py --stage checkpoint
  python /workspace/scratch/21054de32227/MPL_43_094-142/scripts/validate_package.py --stage final

Add --root /absolute/package/directory to validate an extracted checkpoint.
Add --zip /absolute/path/MPL_43_094-142_checkpoint_01.zip or the final ZIP path
to package after validation succeeds. Existing ZIPs are never overwritten.
The script does not schedule checkpoints, save to Library, alter page files,
or edit the progress log. The transcriber decides when a checkpoint is due.

Output is a JSON report on standard output. Exit 0 means mechanical checks
passed; exit 1 means validation or packaging failed. Argument errors use exit 2.
To retain the report, redirect stdout to a file outside the package directory,
then copy the finished report into records before the next packaging operation.
Do not redirect into a file while that same file is being packaged.

Checkpoint stage permits a partial, contiguous prefix of the 46 requested
pages. It does not require a combined transcription, notes, doubts, a freeze,
or completed second-reading audits. Existing page files must have their done
events and inventory records. Existing combined files must be current, exact
concatenations. Any freeze already recorded receives full hash/audit checks.

Final stage requires all 46 pages, the combined transcription, doubts, notes,
inventory, completion/audit events, the freeze hashes, a later context-open
event, and a final unchanged-hashes event. Notes and doubts are checked only
for presence, UTF-8 encoding, and nonempty content, not substantive adequacy.

The combined transcription must be exactly:

  b''.join(page_path.read_bytes() for page_path in scan_order)

Therefore each page should carry its own intended trailing newline(s).
The first page begins with \cotefile{43} then \scanpage{94}. Each subsequent
page has one matching \scanpage macro and does not repeat \cotefile.

Progress-log forms recognized:

  2026-11-16 21:41:51 UTC
  43 scan 094 done 2026-11-16 22:00:00 UTC
  scan 094 audited 2026-11-17 03:00:00 UTC
  sha256 <64 hexadecimal characters> pages/MPL_43_094-142_43_scan094.tex
  sha256 <64 hexadecimal characters> MPL_43_094-142_transcription.tex
  transcription frozen 2026-11-17 04:00:00 UTC
  context opened 2026-11-17 04:00:01 UTC
  frozen hashes unchanged 2026-11-17 06:00:00 UTC

These example timestamps are illustrative, not records of work. The first
line of the actual log is its actual starting UTC time. Explicit UTC ISO 8601
timestamps are also accepted. Every file hash precedes the freeze event; all
46 second-reading audit events follow the complete first pass and precede
the freeze. Record the unchanged-hashes line only after checking actual hashes.

Archives contain files at the package root, without an extra wrapper folder.
They include scripts, records, logs, notes, and page files, including any
additional text documentation in the package directory. They exclude image
files, PDFs, ZIPs, temporary files, Python bytecode, and the scans/upload/context
directories. Symlinks are refused. Supplied attachments should remain outside
the package directory. Excluded paths are listed in the JSON report.


Isolated LaTeX compiler check
============================

  python /workspace/scratch/21054de32227/MPL_43_094-142/scripts/compile_check.py

The companion utility snapshots the existing combined transcription and page
files, then compiles the combined fragment with XeLaTeX in a new temporary
directory. It does not edit the sources or open scans/context. If the combined
compilation fails, it compiles each saved page separately to identify errors
by filename and local source line. --combined-only disables that isolation.
Page isolation uses four independent compiler processes in separate output
directories; --jobs 1 selects sequential compiler execution. This does not
involve additional readers or any transcription work.

The harness defines all allowed editorial macros as content-preserving
wrappers, loads standard mathematical packages and tikz-cd, and first compiles
a synthetic fixture. An active ampersand retaining ordinary alignment-tab
meaning allows both TikZ matrices and arrays inside the editorial arguments.
The harness checks execution/syntax, not editorial decoration or final layout.
Within diagram, a bare array table receives local math mode; arrays already
inside explicit math delimiters retain their existing mode.
fontspec uses its no-math option so that classical mathematical accent commands
retain their standard font encoding. Missing glyphs are treated as compiler
errors by setting tracinglostchars=3. Missing-glyph messages that TeX still
emits as warnings, and invalid-mode command warnings, also make the check fail;
the actual engine exit code is retained separately.

--work-dir /absolute/new/directory selects an external work directory; otherwise
a new directory under the system temporary directory is used. All temporary
harnesses, snapshots, logs, and PDFs remain there. The work directory must be
outside the deliverable. --report /absolute/report.json also saves the report
at that path. The report lists source hashes, scan markers reached, compiler
diagnostics, missing-glyph messages, and layout-warning counts.

On installations whose package files exist but whose filename databases or
XeLaTeX format are absent, the utility uses direct directory lookup and builds
the format in its temporary directory. It does not install packages or change
the system TeX installation. The report records any such environment setup.
When no aggregate PDF font map exists, the harness explicitly loads an
installed Latin Modern math map. This supports standard textcircled symbols
without modifying their source commands.

Exit 0 means the combined compilation completed without syntax errors,
missing glyphs, or invalid-mode command warnings. Exit 1 means those checks
failed. Exit 2 means the environment, synthetic preflight, or required input
prevented a manuscript compilation. Layout warnings remain visible in the
report even after a successful compilation.


Text-only notation inventory
============================

  python /workspace/scratch/21054de32227/MPL_43_094-142/scripts/notation_inventory.py --out-prefix /absolute/new/report_prefix

This companion tool reads a stable byte snapshot of the 46 page files and
writes CSV, JSON, and a readable TXT inventory. It does not select readings,
edit pages, read images, or open context material. It locates nested unsure
macros, unbraced formatting commands followed by unsure, prime/exclamation
superscripts and prime candidates, quotation forms, alphabet macros, capital
N forms, and sigma/gamma/tau command or Unicode occurrences.

Every row includes the scan, local line/column, exact extracted TeX, nearby
context, and enclosing uncertainty/deletion/insertion markup. The math-context
field is a lexical delimiter/environment aid, not a TeX execution trace.
Literal quote delimiters in TikZ arrow options are identified separately.
Counts include alternatives and deleted content, with those states retained.
The output JSON records the source-file hashes and capture time. Existing
report prefixes are never overwritten.
