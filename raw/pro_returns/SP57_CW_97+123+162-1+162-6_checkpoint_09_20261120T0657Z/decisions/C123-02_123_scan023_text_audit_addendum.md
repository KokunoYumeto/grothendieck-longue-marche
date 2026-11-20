# Text-only audit addendum — decision spec and preview

Checked the current `C123-02_123_scan023_spec.json`, `_preview.tex`, `_notes.md`, `out/scripts/decide_p10.py`, and the assembly behavior in `out/scripts/finalize_page.py` against the already-read complete reader files, packet questions, and the exact enums in `out/briefs/reader_v10.md`. No image was opened; no decision or reader file was changed; finalization was not run.

## Result

**No remaining concrete coverage or structural issue found.**

The effective record contains 36 difference loci, 47 inventory rows, 18 C-doubt entries covering all 16 packet questions, 20 remaining doubts, and three independent reader arithmetic-check events. The grouped/split loci in R2 and R3 remain covered by the R1-based union and the explicit reader-comparison overrides. Full saved reader constructions at the varied loci were compared, including beinteresting, n-, A/D, homogeneous, dimension, the O-adjacent sign, both answer cells, closing/signature, and the lower trace.

The preview contains the added cancellation x, D tail, definite lower dimension e plus uncertain upper o/e and all three additional strokes, local O/F-prime/sign geometry, signature point, five lower segments plus upper point, and the separate uncertain point beneath the later W. Their inventory descriptions and remaining-doubt scopes agree. All ordinary text, formulas, deleted layers, inserted phrases, source spellings, and conditional wording remain covered.

## Concrete issues found and fixed during this check

1. **Stale D33 adopted figure:** the inherited full closing figure lacked the newly adopted upper point. Root updated D33.final; it now matches the adopted figure in the preview exactly.
2. **ROOT-01 source coordinates:** the new W-point difference initially lacked bbox and bbox_source. Root added the whole-image coordinates/source; the complete difference schema now passes.

The D35 final field describes the lower trace in prose, but the actual adopted drawing is present in both the preview and updated D33 figure. There is no prose-only replacement of that source mark.

## Required validation

- Applying the spec’s text edit to the R1 source reproduces the preview exactly.
- The saved notes and the spec notes are identical.
- All required effective-difference fields are present. Difference kinds, confidence values, yes/no H markers, boolean witness-change flags, inventory kinds, sheet kinds, and inventory transcription flags use the required values.
- H is explicitly marked uncertain only at R1-D11 and R1-D12. Editorial notes are not treated as uncertainty markers.
- All 36 effective-difference crop references exist, representing 24 unique final crop paths. Reader/C-doubt references were also checked: 174 crop references in total, with no missing file. Referenced whole-image source paths exist; coordinate arrays are well formed and within the recorded image dimensions. This was metadata-only validation.
- Preview braces balance. All 20 TikZ environment pairs close in stack order. The 74 dollar delimiters pair; the 38 inspected node contents have balanced local dollar delimiters. No display/inline delimiter imbalance was found. No TeX compilation was performed.
- The v10 brief expressly permits mathbb for a same-letter typewriter double impression. The retained doubtful same-letter alternatives therefore do not create a new convention violation.

No broader testing, mathematical rechecking, or additional source inspection was undertaken.

