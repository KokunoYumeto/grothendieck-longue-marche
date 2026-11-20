# Scan183 text-audit refinements

The main reader compared the completed A/B readings with the consolidated record. Two refinements were made before freeze:

1. B’s old fragment before multiplicative is `sou|m|de`, not `sou|de|m`. The comparison table now quotes its actual order. The consolidated m-first reading is unchanged.
2. A’s full return explicitly located the first underline start inside the first n. The main reader’s already inspected C/21_non_abelien_underline.png likewise shows the first n beginning near x304, with the rule beginning near x318. The consolidated rule previously began at the whole n’s left edge. It now uses a short partial-n overlay followed by `uline{on abé}`, in addition to the already preserved partial-l resumption and gap. The observed endpoint coordinates remain unchanged. This is a refinement of the existing underline difference row, not an additional C/H change.

The original reports are unchanged. No image was reopened or recropped, and no new visual inspection is claimed. Notes, inventory, notation and comparison evidence have been aligned with the exact endpoint encoding. No TeX engine or rendering was used. The static structure check is rerun after assembly.

## Accepted H-kind metadata corrections — 2026-11-20 13:25:04 UTC

The main reader accepted technical-audit findings F1 and F2. The expected old values were checked before editing. Only these two fields in `records/scan183/decision.json` changed:

- `differences[3].kind`: `other` → `misread word` (L4 modules ending; the preferred word changes against H).
- `differences[21].kind`: `misread word` → `other` (L14 donnant/donnait; H already has doubtful donnant, so the H change is uncertainty resolution only).

The scan183 page was not changed. Its SHA-256 before and after the edit is `31d93fbb19432cf3c39260c809eedfed6bd00c8449e651d22fcaf123892b2b9d`. The parsed decision record differs only at the two fields listed above.

Aggregate type totals are unchanged: the two corrections exchange one `other` and one `misread word` membership, producing zero net change in every kind total. Scan183's H-kind tally remains misread word 13; other 8; misread symbol or index 1; readable ink left as `\ill{}` 1; omission 9; deletion state 1. Across all 35 scan183 difference rows, other remains 10 and all other kind totals are identical to that H tally. The witness counts remain 21 C differences and 33 H differences. No aggregate file was changed.

Reader reports, the page, other decision metadata and all images were left unchanged. No image inspection, recropping, TeX work, compilation or rendering was performed.
