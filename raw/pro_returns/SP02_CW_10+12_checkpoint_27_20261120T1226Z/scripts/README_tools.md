# Mechanical support tools

These tools do not inspect handwriting, recognize text, decide readings, verify mathematics, or replace the reader. The source packets and research context are not included in the deliverable archive.

## Inspect one page's supplied sources

```bash
python SP02_CW_10+12/scripts/inspect_page_sources.py B10-02_10_scan043
```

This read-only command prints the C page, exact H marker span (when present), C inventory rows, exact C doubt-macro loci, matching rows from C's doubts tables, and absolute whole/half-image and existing crop paths. It also lists saved crop recipes. It never opens images, writes page status, or reads the research context. Use `--sections C,H,doubts` to narrow output, or `--json` for a structured packet. H section boundaries remain explicitly flagged and uninterpreted; no absent H text is supplied by inference. The command extracts H from its source batch directly, so it also works after a workspace restoration when scratch H fragments are absent.

## H fragments

```bash
python SP02_CW_10+12/scripts/split_hua.py \
  --witness-root source/SP02_CW_10+12_witnesses \
  --output work/hua_pages
```

The splitter copies exact source bytes from each explicit H `\page{N}` marker to the following marker or end-document command. It does not infer whether an interposed section heading or editorial note belongs to the current or following page. Such boundaries are flagged for the reader. Numbered text and JSON metadata preserve original batch line numbers, source hashes, and twelve lines of preceding boundary context. The index includes all 106 map entries; only the 91 with H text receive fragments.

## Record a completed page

```bash
python SP02_CW_10+12/scripts/record_page.py work/page_record.json
python SP02_CW_10+12/scripts/record_page.py work/page_record.json --finalize
```

Without `--finalize`, this validates the supplied record without writing. Finalization is the root reader's explicit assertion that the page and inventory have been checked. It starts from C, applies only exact asserted replacements, then writes the page, stores the full record, regenerates the cumulative logs, and appends the actual UTC completion time. An `old` replacement string must occur exactly once unless its `count` is supplied. It enforces page-map order and rejects page mutations after freezing or opening context.

The record schema is:

```json
{
  "folder": "B10-01",
  "cote": "10",
  "scan": 33,
  "edits": [{"old": "exact source substring", "new": "explicit replacement"}],
  "changes": [{
    "place": "location supplied by reader",
    "C": "C reading", "H": "H reading", "final": "final reading",
    "shows": "reader's observation", "crop": "crop identifier",
    "kind": "misread word", "marked_in_H": "no", "confidence": "high",
    "against_C": true, "against_H": true,
    "consequential": "optional explanation of mathematical consequence"
  }],
  "inventory_confirmed": true,
  "inventory_from_C": true,
  "sheet_kind": "typescript",
  "inventory_overrides": {"element identifier": {"field": "replacement"}},
  "inventory_extra": [],
  "inventory_remove_elements": [],
  "remaining_doubts": [{"line": "place", "reading": "reading", "alternatives": "alternatives", "confidence": "low", "comment": "reason"}],
  "notation_updates": [{"sign": "key", "form": "form read in ink", "attestations": "cote:scan:place", "status": "reader's status"}],
  "abbreviations": [{"abbreviation": "abbr.", "expansion": "possible expansion", "attestations": "place"}],
  "crops": [{"id": "crop-id", "source": "scan-filename.jpg", "box": [0, 0, 100, 100], "rotation": 0, "scale": 2, "contrast": 1}]
}
```

The example strings above are placeholders, not manuscript readings. `inventory_rows` can replace `inventory_from_C` with a fully explicit inventory. The reader must affirm `inventory_confirmed: true` in either case. C metadata `typed` becomes `typewriter`, `Grothendieck` becomes `his hand`, and broad `handwritten`/`letter part` inventory kinds become `text` unless explicitly overridden. The reader may override any element needing a more specific classification.

Record validation checks the nested change, doubt, notation, abbreviation and crop structures before publication. Changes require explicit crop references and typed C/H flags; doubt positions/readings/confidences must be present. Crop validation is shared with the image-free `crop_metadata.py` module. Inventory operations must identify exactly one existing element; unknown/ambiguous IDs, duplicate operations and unsupported override fields fail instead of being ignored. An explicit `transcribed: "no"` is rejected, never converted to `"yes"`. Explicit per-element sheet-kind overrides take precedence over a page-wide default. Source C SHA-256 is computed from its raw bytes, independently of the existing normalized-newline edit workflow.

Each change's `crop` reference must resolve to a recorded recipe ID or the established whole-image aliases `whole` and `both halves`. This metadata check does not open images or assert that an image was inspected. An exact complete ID is accepted before separators are parsed. Commas, semicolons and the word `and` separate groups; `+` separates simple IDs within a group. To combine an ID containing a literal `+` with another ID, use a comma, for example `detail+contrast, lower`. Unknown or empty references are rejected in shared first-pass/audit validation.

Before committing a page, the helper stages the complete report projections and validates all metadata they consume. A render failure therefore cannot publish a new page/record without its completion event. Earlier records must also have their actual `done` events before a later page can be finalized. No syntax check or successful metadata validation itself marks a page complete.

Generated Markdown and TSV/CSV files are rebuilt from `documentation/page_records/*.json`. Do not hand-edit those generated files during the reading. Put cumulative prose in `documentation/editorial_metadata.json` as `legibility` and/or `additional_doubts_text`. Repeated notation forms/statuses and abbreviation meanings retain their own attestation lists; the renderer never silently substitutes a later form for an earlier one. Exact duplicate entries may share a row with merged attestations. Counts by confidence cover loci differing from at least one witness; a record of a retained doubt with both difference flags false remains in the per-page table but does not count as a change. Inventory scan labels use `cote:NNN` to distinguish repeated scan numbers between cotes.

Explicit first-pass corrections to a recorded page may use `--allow-update`; this changes the log event to `corrected`. Do not use that C-based replacement path for the second reading. It rejects a page with an active or completed audit, whose accumulated history is managed by the separate audit tool below.

## Record the second reading

Only after every mapped page has a finalized first-pass record, the root reader starts each audit in page-map order:

```bash
python SP02_CW_10+12/scripts/record_audit.py --begin B10-01_10_scan033
```

This records the actual UTC start, hashes the current page and its record, and saves immutable before snapshots. It does **not** mark the page audited. Its response supplies `audit_id`, `baseline_page_sha256`, and stable ids for existing change loci. Only one audit may be active. Root then reads the page and writes an explicit audit JSON, for example:

The gate checks all 106 mapped page/record identities, exact recursive filename sets, current page hashes, explicit first-pass inventory confirmation, and the complete first-pass `done` event order. Earlier audits must have matching completed sessions, record entries, and timestamped start/end events. Missing, malformed, reordered, duplicated, overlapping, or unmatched audit evidence is rejected. The selected unfinished session alone may use the documented interrupted-start recovery; recovery also checks the full completion trail and its immutable decision identity.

```json
{
  "audit_id": "EXACT_ID_FROM_BEGIN",
  "baseline_page_sha256": "EXACT_HASH_FROM_BEGIN",
  "audit_reading_complete": true,
  "audit_inventory_confirmed": true,
  "edits": [],
  "upsert_changes": [],
  "remove_changes": [],
  "observations": "Root's actual second-reading observations, including any accents, formulas, indices, corrections and alphabet checks."
}
```

```bash
python SP02_CW_10+12/scripts/record_audit.py --record work/audit_record.json
python SP02_CW_10+12/scripts/record_audit.py --record work/audit_record.json --finalize
```

The first command validates without mutation. The second explicitly commits the root's completed reading and records the actual UTC completion event. Audit `edits` apply to the **current consolidated page**, preserving all earlier edits. Existing change rows persist by default. To revise a locus, put its stable `id` and the full new change row in `upsert_changes`; to add a locus, use a new id beginning with the page key and a hyphen. To remove an obsolete current locus, supply `remove_changes: [{"id": "...", "reason": "..."}]`. Earlier decisions remain in immutable history even when the current collation changes. Nothing infers equivalence between readings or changes C/H difference flags automatically.

Preview and finalization now perform the same complete metadata and report-projection validation in temporary scratch staging. Preview publishes no page, record, report, history, session, or log event and assigns no completion timestamp. Both modes reject invalid crop metadata or editorial/report metadata before publication. A page/record or projection-metadata change during staging aborts the operation.

Metadata is retained unless explicitly revised:

- `remaining_doubts` replaces that page's current doubt list when supplied.
- `notation_updates_add` and `abbreviations_add` append entries; the corresponding `_replace` keys explicitly replace a complete page list.
- `inventory_patches` maps an exact existing element id to edited row fields; `inventory_extra` supplies complete new rows; `inventory_remove` supplies element ids and reasons. The audit never reloads C's inventory.
- `crops_upsert` supplies complete crop recipes keyed by `id`, preserving all other recipes inside the page record.
- `observations` is the root's actual audit account, stored verbatim as text or JSON and included in the generated audit Markdown.

Audit top-level keys are restricted to the documented audit fields. First-pass keys such as `notation_updates` and `inventory_overrides` are rejected rather than silently ignored; use the explicit audit operations above. Optional `key`, `folder`, `cote`, and `scan` fields are identity assertions and must agree with the selected session/page. `observations` remains extensible root-authored text or JSON. These checks run in the common preview/finalization path before publication.

Inventory row fields are limited to `scan`, `sheet_kind`, `hand`, `element`, `kind`, `position`, `first_words_or_objects`, and `transcribed`. The page's inventory scan identity is immutable: an idempotent patch repeating the same identity is accepted, but another scan label is rejected. Additions must identify that same page and include the complete allowed schema. Unknown fields are rejected rather than silently omitted from CSV output. These identity/field checks also apply to resolved first-pass records.

Resolved inventory element IDs must be nonempty and unique after all removals, patches and additions. An explicit rename to an unused ID is supported; a rename or addition that collides with another current element is rejected in both preview and finalization.

Both begin and finalize reject frozen/context-opened work. Finalization rejects any intervening change in the baseline hashes. It stages all derived reports, preserves immutable before/after snapshots and decisions under `documentation/page_history/`, then replaces current projections; the `audited` line is appended only after those writes succeed. The existing changes/collation files therefore describe cumulative **current** readings, while the history preserves the first pass and all audit revisions.

An interrupted commit remains distinguishable from a completed audit:

```bash
python SP02_CW_10+12/scripts/record_audit.py --status EXACT_AUDIT_ID
python SP02_CW_10+12/scripts/record_audit.py --resume EXACT_AUDIT_ID
```

`--resume` only completes an already root-authorized prepared revision whose immutable after snapshots and hashes agree. It accepts only before/after current file states, rechecks them immediately before replacement, refuses conflicting work and frozen/context-opened work, and does not invent a new reading. It retains the recorded audit time and separately records the actual recovery time. If preparation stopped before all after snapshots were created, repeat `--record ... --finalize` with the **identical** original payload; existing immutable files are accepted only if byte-identical. A startup interrupted before its session file exists leaves its history intact, and a fresh `--begin` uses the next unused id. If the session exists but its start-log append was interrupted, explicit finalization/recovery restores that event from the session's original `began_utc` before logging completion, and separately records recovery time; conflicting or duplicate starts are rejected. A completion already logged without any start requires explicit log reconciliation rather than a silently reordered history. Snapshot bytes are published atomically and exclusively; unfinished preparation temporaries are excluded from archives. No audit operation runs automatically.

`--resume` now honors `--witness-root` for the same complete metadata/event gate used by begin/finalization. The current page-map metadata must therefore be available during recovery. A completion already appended by an interrupted commit is retained exactly once; prepared decision identity, baseline, timestamps, and the latest record event must agree with the selected session.

## Assemble and create navigation indices

```bash
python SP02_CW_10+12/scripts/assemble_and_index.py --write
python SP02_CW_10+12/scripts/assemble_and_index.py --write --require-complete
```

Without `--write`, this is a dry run. The combined fragment is an exact byte concatenation of existing page files in page-map order. It lists missing pages and never fills them from C. It reports repeated `\cotefile` commands without removing them. The reader must make any intended page-file corrections explicitly.

`documentation/notation_occurrences.tsv` lists control sequences, immediate brace arguments, lexical subscript/superscript markers, paired quote marks, source positions, and short context. `notation_groups.tsv` groups identical lexical forms across pages. These are navigation aids, not an exhaustive TeX parse, nor an assertion that forms should agree mathematically. `assembly_report.json` records coverage and hashes. The tool will not change a frozen combined text.

## Reproduce crops

```bash
python SP02_CW_10+12/scripts/render_crops.py \
  --destination work/reproduced_crops --page B10-01_10_scan033
```

Add `--crop ID` for one crop, or omit `--page` for all recorded crops. The source must be inside the supplied/default attached-scan folder. All of these recorded conventions are accepted and anchored to that known folder, independently of the working directory:

- Scan-relative: `filename.jpg` (or an existing relative subpath inside the scan folder).
- Scan-folder-prefixed: `SP02_CW_10+12_scans/filename.jpg`.
- Workspace-relative: `source/SP02_CW_10+12_scans/filename.jpg`.
- An absolute path already inside the known scan directory.

The `resolve_scan_source()` helper exposes the same path-only logic for metadata checks. It refuses `..` traversal, outside absolute paths, a symlink scan root, and symlink components beneath the scan root; it requires an existing regular source file. It never interprets a recipe path relative to process cwd. Existing recipe text is preserved.

Coordinates are source pixels `[left, top, right, bottom]`; right and bottom are exclusive. The exact order is **crop → flip → counterclockwise rotation (expanding with white fill) → optional grayscale → autocontrast → contrast → scale**. `grayscale: true` performs Pillow `convert('L')` immediately before autocontrast and contrast. It accepts only a Boolean; omission or `false` preserves the existing RGB behavior. `flip` accepts `vertical` (top/bottom) or `horizontal` (left/right). `autocontrast: true` uses Pillow cutoff 0; a numeric value such as `2` is the cutoff percentage; `false` or absence disables it. Other defaults remain rotation 0, contrast 1, scale 1. Coordinates are not silently rounded.

For metadata-only checks, the shared `crop_metadata.py` module exposes `CROP_RECIPE_FIELDS`, `TRANSFORM_ORDER`, `grayscale_requested(recipe)` and `validate_crop_metadata(recipe, source_size=None)`. It checks recipe types, supported fields, finite parameters and box geometry without opening files; optional supplied dimensions permit a bounds check. `render_crops.py` re-exports the same helpers. No OCR or image interpretation is performed. PNG crops are scratch products and excluded from archives; their complete reproduction specifications remain in the page records, which this tool does not alter.

## Freeze and verify the transcription

The root reader invokes these commands only when all actual first and second readings are complete. The tool never opens images or context, decides a reading, performs a proof check, or supplies a missing completion event.

```bash
python SP02_CW_10+12/scripts/freeze_transcription.py --freeze
python SP02_CW_10+12/scripts/freeze_transcription.py --freeze --write
```

The first command is a non-writing readiness check. The second explicitly commits a freeze only if all gates pass:

- Exactly the 106 page-map identities exist as page files and first-pass records: 84 pages from cote 10 and 22 from cote 12, with no missing/extra page or record filename.
- First `done` events cover those identities in map order and precede the audit sequence. Cote and audit identifiers disambiguate repeated scan numbers.
- First completed audits cover the pages in map order, all starts and completions agree with their sessions, and no audit remains open. Later repeated audits are allowed; their latest completed revisions determine the final page bytes.
- Current page files and records agree with the latest immutable audited page/record snapshots. Root's explicit reading and inventory completion declarations remain in the immutable decisions.
- The combined file is byte-for-byte equal to `b"".join(page_bytes_in_page_map_order)`. No normalization, separator insertion, or regeneration occurs inside the freeze tool. Assemble it separately if necessary.

The tool writes an immutable `documentation/transcription_freeze.json` containing the 107 file hashes and ordered page identities. It appends a complete `SHA256` block to `progress.log`, rechecks the transcription and audit evidence, and **appends the actual UTC `transcription frozen ...` marker last**. That marker is the commit point. The manifest's `snapshot_utc` records when the hash snapshot was prepared; the actual committed freeze time is the final log marker.

If interrupted before the marker, an unchanged uncommitted manifest can be reused by the same explicit freeze command. A differing uncommitted manifest is preserved and causes an error; it is never silently overwritten. A partial hash block without the commit marker does not count as a successful freeze. Freeze mutations are refused after any freeze marker or after `context opened`.

New manifests also pin a versioned `state_fingerprint` covering page, record, session, immutable-history and combined-file hashes plus the recognized completion/audit event trail. Both read-only and writing retries require the same pin. Newly appended freeze hash blocks do not change that evidence fingerprint. A legacy **uncommitted** manifest without a pin is refused and preserved for explicit reconciliation; a legacy **committed** schema-1 manifest remains verifiable.

Freeze parsing applies the audit parser's strict event checks before readiness or fingerprinting: a completion/audit-looking line with malformed syntax and an event with duplicate identity fields are rejected. Such lines cannot be silently excluded from the retry evidence. Ordinary non-event progress notes and freeze preparation blocks retain their existing treatment.

Freeze success and error results distinguish preparation from commitment. `written` reports observed manifest/log mutation in the invocation (`null` only if an attempted write cannot be read back); `write_attempted`, `prepared`, and `committed` make the phase explicit. `manifest_created`, `manifest_reused`, and `hash_block_appended` record successful preparation steps. An error after preparation can correctly have `written: true, committed: false`; an error after a complete commit marker was observed can have `committed: true`. The final marker, not merely the presence of a manifest or hash block, remains the commit point.

Explicit `--verify --write` logging uses the same observed-write check. If append or `fsync` fails after changing the log, the error accurately retains `written: true` (or `null` if readback fails), sets `logging_ok: false`, and preserves the separate `hashes_ok`, checked-file count and hash-failure details. Read-only verification never attempts a log append.

The root may subsequently append its actual `context opened ...` event and open context through its own workflow; this helper does neither. At the end of the research notes, verify the stored hashes:

```bash
python SP02_CW_10+12/scripts/freeze_transcription.py --verify
python SP02_CW_10+12/scripts/freeze_transcription.py --verify --write
```

Verification trusts the frozen manifest and its committed hash block, rather than reconstructing a new baseline. It checks all 106 page files and the combined fragment, detects missing or changed files and unexpected page files, and returns a nonzero exit status on failure. It does not require the external witness packet, so it also works from the final deliverable folder. Without `--write`, it changes nothing. With `--write`, it appends the actual UTC success **or failure** result only; this logging is permitted after context opening and never modifies any frozen file or the manifest.

## Isolated helper hardening checks

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s SP02_CW_10+12/scripts/tests -p 'test_*hardening.py' -v
```

These tests build invented 106-page datasets only inside temporary `work/helper_hardening_fixtures/` directories, explicitly supply their temporary map/output paths to every operation, and clean up automatically. They do not access live manuscript data or live audit/freeze state. Cases cover inventory identity/field rejection, preview/final validation parity, complete event gates, interrupted audit recovery, honest freeze error phases, pinned-evidence retries, successful unchanged retries, and legacy committed verification.

The later preflight fixes have separate focused regressions: `tests/test_audit_metadata_preflight.py` (unknown audit fields, identity assertions, inventory IDs and crop references), `tests/test_verify_write_status.py` (verification append failures), and `tests/test_package_publication.py` (interrupted or competing archive publication). These use invented temporary fixtures only. Their recorded results do not imply that the older complete suites were rerun.

## Syntax balance

```bash
python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages
python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages --json
```

This is a lexical balance check of braces, math delimiters, and environments. It also rejects math/environment boundaries crossing their enclosing brace groups, while allowing nested mathematics inside text. It ignores comments, escaped punctuation, inline verbatim, and common verbatim environments. It does not expand macros, compile TeX, or validate the mathematics.

## Bounded checkpoint staging

`prepare_checkpoint.py` wraps the existing script-copy, assembly and lexical helpers. It has no packaging, upload, scheduling, audit or freeze action. Supply the expected finalized map prefix explicitly; default mode validates the snapshot and reports the plan without writes:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/prepare_checkpoint.py \
  --checkpoint 15 --expected-pages 75 --last-page B10-09_10_scan128
```

After root has saved the current provisional documentation and paused concurrent record/script changes, add `--write`. Add a separate `--provisional documentation/EXACT_ROOT_SUPPLIED_FILENAME` for every provisional Markdown, recipe JSON and builder copy required in that checkpoint. These files must already exist under output documentation; the helper hashes them without interpreting their contents and never invents observations or copies arbitrary source material. Update `--expected-pages` and `--last-page` if another page finalizes first.

The helper requires an exact page/record filename prefix and agreement between page hashes and stored record identities. It snapshots pages, records, generated reports, progress/CHECK_EVENTS, the map metadata, root script source files and explicitly selected provisional files. It runs the existing refresher, assembler and lexical checker, checks the snapshots between stages and at completion, and confirms exact ordered combined bytes. The assembler is partial for checkpoints; `--require-complete` is not used here. A concurrent change aborts readiness without restoring or overwriting that change.

Successful staging writes `evidence/checkpointNN_refresh_NNN.json`, `checkpointNN_assembly_NNN.json`, `checkpointNN_lexical_NNN.json` and `checkpointNN_preparation_NNN.json`. Here `NNN` is the finalized count. Existing evidence is never overwritten; use a distinct `--label` for a later preparation at the same count, for example `--label 075_provisional`. A failed stage preserves any evidence already written and records the failure when the preparation report can be saved. Only `ready: true` signifies completed staging; default snapshot checks do not run lexical validation and report `ready: false`.

The refresher copies **all** scoped `work/record*.py` files, including a draft if present. Root must therefore finish or pause those files before staging. Arbitrary provisional crop builders/recipe files still require explicit root-selected copies in documentation. Finish all staging/evidence writes before the separate package command. The staging helper neither enforces the checkpoint due time nor creates an archive.

Five focused temporary-fixture regressions in `tests/test_prepare_checkpoint.py` cover read-only operation, successful protected staging, interruption by a concurrent change, refusal of an unrecorded page, and preservation of prior evidence. No live checkpoint is created by those tests.

## Archives

Refresh the explicitly scoped root script documentation before packaging:

```bash
python SP02_CW_10+12/scripts/refresh_checkpoint_documentation.py
```

This copies `work/record*.py` into `documentation/root_scripts/` and `work/library_helpers/*.py` into `scripts/library_helpers/`, verifying identical bytes by SHA-256. It does not collect images, witness splits, or context, and does not create or upload an archive. Existing matching copies are refreshed; unrelated and earlier copies are retained. The copies document this run; Library transfer helpers should still be obtained through the current Library skill when a new run requires them.

```bash
python SP02_CW_10+12/scripts/package_output.py \
  --root SP02_CW_10+12 --destination checkpoints --checkpoint 1
python SP02_CW_10+12/scripts/package_output.py \
  --root SP02_CW_10+12 --destination . --final
```

Add `--dry-run` to either command to list exactly what would be included without creating an archive or directory. The reader or an explicitly authorized mechanical helper invokes actual packaging, at the required checkpoint cadence or final completion. No schedule is started automatically. Archives are created exclusively and cannot overwrite an existing name. Source/scans/witnesses/context folders, previous archives, raster images, symlinks, caches, and git metadata are excluded. **Checkpoint metadata JSON under `documentation/checkpoints/` is included** as work documentation; the narrow exception does not include prior ZIPs, other archive types, or excluded input/context subdirectories. Other `checkpoints/` directories remain excluded. ZIP integrity is checked; content completeness is not certified. Uploading and preserving the checkpoint is a separate root action.

The packager writes an exclusive temporary ZIP in the destination directory, closes and flushes/fsyncs it, validates CRC and computes its metadata before publishing the immutable final name with an exclusive hard link. Failed preparation cannot occupy the final name, and a competing publisher's archive is never replaced. Cleanup removes only the tool-owned temporary name. A killed process or failed cleanup may leave that uniquely named temporary file; a cleanup failure after successful publication is reported as a warning without misreporting the valid archive as uncommitted. Existing checkpoint/final archives remain unchanged.


## Complete crop replay for cote 12, scan 070

`replay_crops12_070.py` embeds the exact JSON byte streams from `work/crops12_070.json` (50 recipes) and `work/fine12_070.json` (17 recipes), including their SHA-256 provenance. It preserves the captured order and all recipe values. The script can therefore replay all 67 crops without the original `work/` JSON files; the bundled `crop_metadata.py` and `render_crops.py` remain its helper dependencies. It does not modify the root recipe builder or the finalized page/record.

Default operation and the explicit metadata-only command validate the embedded metadata, IDs and numeric geometry without importing the image renderer, opening source images, creating a directory, or generating raster evidence:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/replay_crops12_070.py --metadata-only
```

Only an explicit render command reads the attached scans. The destination must be outside `SP02_CW_10+12`; `--scan-root` identifies the directory containing the supplied scan files:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/replay_crops12_070.py \
  --render \
  --scan-root source/SP02_CW_10+12_scans \
  --destination work/replayed_crops12_070
```

Rendering delegates to `render_crops.render_crop`: crop → optional flip → counterclockwise rotation → optional grayscale conversion → autocontrast → contrast → scale. Coordinates have exclusive right/bottom edges. Rendering checks actual image dimensions; metadata-only mode cannot certify pixel extent bounds. The root must choose to execute rendering later. No image rendering was performed when this replay script was prepared.


## Base and later crop replay for cote 12, scan 081

`replay_crops12_081.py` embeds the complete finalized 87-recipe snapshot in its original order: 68 initial recipes from `work/crops12_081.json`, followed by 19 fine recipes from `work/fine12_081.json`. Both exact JSON byte streams are embedded, with these SHA-256 provenance hashes:

- Initial 68: `309610fc4c4187ca2a0b27dc01c496dd615a7135fc2a81ea78070557774468bb`.
- Fine 19: `8f6501e3f7040602229b174f6b9a07bdbd4a7b0ffaece7684508ee10845bbf60`.

Every recipe retains its own source path, including the `_a.jpg` or `_b.jpg` half. The script is portable without either original `work/` JSON file. Its default count is now **87 embedded recipes**, with **zero optional extra recipes**. The initial count of 68 remains separately reported. `work/fine12_081.json` is already embedded and must not be passed again as an extra list; duplicate IDs would be rejected.

Default mode and `--metadata-only` validate metadata without importing `render_crops`/PIL or opening images:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/replay_crops12_081.py --metadata-only
```

Root may explicitly append genuinely additional future recipe lists with repeatable `--extra-recipes`. These example paths identify future root-created metadata, not existing or required files:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/replay_crops12_081.py \
  --metadata-only \
  --extra-recipes work/later12_081.json \
  --extra-recipes work/additional12_081.json
```

Extra files must be explicit, nonsymlink `.json` files containing recipe lists. They are appended after the embedded 68 + 19 recipes in command-line order. Every recipe is validated; duplicate IDs and normalized output-filename collisions are rejected across all embedded and extra sets. The report distinguishes embedded count from optional extra count, gives each source's byte count/SHA-256, and hashes the complete combined recipe list. Metadata-only operation reads only embedded data and any explicitly supplied JSON metadata, never the source images.

Root may later choose to render all 87 embedded recipes with this command; optional future extras can be supplied separately if needed:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/replay_crops12_081.py \
  --render \
  --scan-root source/SP02_CW_10+12_scans \
  --destination work/replayed_crops12_081
```

The destination must be outside the deliverable folder. Rendering delegates to the existing `render_crops.render_crop` implementation and preserves its order: crop → optional flip → counterclockwise rotation → optional grayscale → autocontrast → contrast → scale. Right/bottom coordinates are exclusive. Actual pixel extent bounds are checked only during explicit rendering. No source image, image header, or raster output was opened or rendered while updating this helper; verification used metadata and a tiny invented extra-list fixture only.
