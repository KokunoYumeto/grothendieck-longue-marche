# Scan016 source attention before final selection

This preparation record uses the packet and completed reader text sources only. It makes no ink choice. The final selected-source audit will be recorded separately in `scan016_source_audit.md`.

## Literal source loci requiring explicit linkage

1. **First partition endpoint.** `packets/016/H.tex` has a comma after the first partition equation. A records its removal as `A016-W21`; B records it as `B016-D23`. C's `reading.tex` also omits the comma, while C's report has no dedicated difference row for that punctuation locus. Preserve the A/B provenance and the literal H locus in the final union.
2. **Comma after the right insertion.** Packet C and H both carry a comma after inserted `de X…E_2`, before the next `donc`. A and C print that comma and identify the detached lower curved mark with it. B's TeX has no ordinary comma there and instead draws `G02c`, described as a detached return with unassigned framing/guiding role. Root has been asked to give this one physical mark an explicit selected representation and role record.
3. **Original C doubt row 12.** The actual source table says both joins under the long final bar retain a cup/square-join doubt. Packet C.tex marks only the first live cup. The earlier source-map string for the second local locus says “live cup”; the final map must retain the table's second-join doubt explicitly. The 13 original source-row identities yield 19 primary physical clusters and 21 local predecessor/live components. A records its two join clusters as two combined state/form entries; B and C give four component entries. Keep each raw representation and its mapping.
4. **A brace provenance.** A's `BRACE01` and `BRACE02` appear in its TeX, `graphical_components`, and inventory `A016.15`. They have no separate A difference rows. Their source provenance remains available through those existing records.

The preparatory review found no additional common word or formula omitted from all three completed return mappings. The selected final TeX, root decisions, graphical command selection, final attachments, and counting parents remain for the one final coverage pass.

## Existing A source-image comparison event

At root's request, the reviewer read the existing `out/readers/016/A/make_crops.py` and `crop_manifest.json`. Neither file was executed. No image was opened by this reviewer.

The script iterates the fixed pairs `('a', 0)` and `('b', 1101)`. It loads each supplied half and computes:

```python
delta = ImageChops.difference(im.crop((0,y0,1685,y0+1261)), half)
ImageStat.Stat(delta).mean
```

The existing manifest records:

| Half | Stored size | Stored full origin | Stored mean absolute channel differences, in returned channel order |
|---|---|---|---|
| a | `[1685, 1261]` | `[0, 0]` | `[0.004762364192141793, 0.004896966045976416, 0.007469932251969022]` |
| b | `[1685, 1261]` | `[0, 1101]` | `[0.9677270876818125, 0.9683662111696006, 1.2771885155439255]` |

The script labels its printed object `half_coordinate_verification`. It contains these two fixed-origin comparisons and supplies no alignment-search loop or acceptance threshold. The recorded event is available for root's actual-check attribution; the readers' empty mathematical `check_events` arrays remain preserved as returned.

## Reviewer scope

The reviewer read packet C/H, source doubts/notes/inventory, the source map and witness-attention record, and all three completed TeX/report/audit returns. A was read only after root announced its completion. The scan015 audit supplied style and schema only. No image, OCR, external research, compiler, renderer, installation, ink adjudication, mathematical computation, numerical geometry calculation, or delegation was used. Only source text and existing recorded outputs were inspected.
