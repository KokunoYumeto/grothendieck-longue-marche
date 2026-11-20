# Structural review

Reviewed 2026-11-20 19:03:38 UTC. Scope: packaging/assembly code, file metadata, mechanical concatenation, record count flags, and Markdown table structure. No manuscript image or reading was inspected, and no page fragment or accepted record was changed.

## Packaging and checkpoints

`manage.py:pack` recursively includes every work-tree file except `__pycache__` contents and files whose suffix is `.zip`, using paths relative to the work root. This covers root documents, scripts, reviews, workflow files, fragments, and crops. At the initial inventory, the selector covered 575 files; the one excluded file was a Python cache. No symlink files or uppercase ZIP files were present.

The original `source/` attachments, original `halves/` tree, and earlier checkpoint ZIPs in `deliverables/` are outside the work root and are not selected. The latest existing checkpoint's central directory contained no source/half trees or nested ZIPs. The checkpoint function refuses to overwrite a prior checkpoint; it packs the current on-disk tree without first invoking `build()`.

**Full-half copies:** the only exclusion issue found was `crops/143_scan034_readerC_native-half1-rot180.png` and `crops/143_scan034_readerC_native-half2-rot180.png`. These are lossless native-half viewing copies, not tight evidence crops. Root has relocated both full-half viewing copies to `halves/` outside the work tree. They are no longer selected by `pack`; the actual tight evidence crops remain in `crops/`. No packaging-code change is needed for that relocation.

## Ordered assembly and final gate

`page_order.json` contains exactly **24 distinct keys**. `build_deliverables.py:load_records()` traverses that order, and `build()` concatenates the corresponding fragments, adding a cote header when the cote changes. The existing combined file exactly matched an in-memory reconstruction from the accepted fragments in that order. No accepted-key mismatch or extra fragment was found.

The builder intentionally permits partial progress by skipping missing accepted records. The review snapshot has **22 accepted fragments**; pending: `143_scan033`, `145_scan002`. This is not a final-completeness claim. The separately inspected `validate_deliverables.py --final` requires all 24 accepted keys, exactly 24 fragments, exact ordered concatenation, complete original MARKS, and the required second-reading records. Final assembly should use the normal build, final validation, then pack sequence.

## Witness H absence on scan034

The accepted scan034 record has **zero material changes, zero against-C counts, and zero against-H counts**. The builder explicitly excludes scan034 from H collation rows. The validation script separately forbids H collation rows for scan034 and checks the total against accepted records excluding that page. Current H totals are therefore not inflated by the missing witness.

The changes-table against-H number is calculated from record flags, while the TSV has the explicit scan034 exclusion. Any later scan034 correction should continue to carry `against_H: false`; absence of H is not a comparison result.

## Notation-table formatting fixed

Two purely structural defects were repaired in `notation.md`:

- The isolated two-cell `\mathfrak Z` row was joined to the preceding table and its existing “(provisional alphabet encoding)” label placed in the second cell, yielding the same three-column structure as the header.
- Six internal pipes in code spans were escaped for GFM tables: the E/Sigma, tt/universal-sign, tau/T, two wave/a alternatives, and accented-a/colon alternatives. Their displayed reading content is unchanged.

All three tables now have a header, separator, and consistently three cells per row, with **11, 11, and 4 data rows**. No wording, uncertainty, or interpretive content was changed. The next normal build propagates this formatting into the generated doubts document; this review did not regenerate aggregate deliverables.

Only `notation.md` and this review were written during this task. No packaging code, page content, or acceptance record was altered.
