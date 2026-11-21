# NREV-01 / NREV-02 public-report proposal

**Status: proposal only; no repair applied. Root review and final audit remain scheduled after scan026.**

The proposal supplies exactly **20 decision finals and 20 matching doubt readings**. It carries the source-selected local glyph decorations and retained alternatives into those current public fields. The selected pages, witness and reader fields, confidence, hands, count flags, first-occurrence printing convention, root authorities and approval history remain unchanged.

## Exact target fields and local wording

| Decision | Decision final / doubt reading pointers | Existing root authority | Proposed public wording |
| --- | --- | --- | --- |
| L018-15 | `/decisions/15/final` / `/doubts/6/reading` | scan018-section09 | \Pi_J^\circ \| \Pi_J^0 (inserted recurrence; local circle/zero doubt retained, circle first; \circ prints under the first-occurrence qualification convention). |
| L021-04 | `/decisions/3/final` / `/doubts/1/reading` | scan021-section03 | Complete roofed \Sigma_{\alpha_0}, with the further-lowered 0 and no raised plus; separate short upper-run role remains head/retrace \| independent upper rule. |
| L021-05 | `/decisions/4/final` / `/doubts/2/reading` | scan021-section03 | Complete roofed \Sigma_i^+, with a separate dotted i and raised plus; separate short upper-run role remains head/retrace \| independent upper rule. |
| L021-06 | `/decisions/5/final` / `/doubts/3/reading` | scan021-section04 | Complete \Sigma_{\alpha_0}, with the lower arm shared with the alpha loop and a separate lowered 0; short upper-run role remains head/retrace \| independent upper rule. |
| L021-07 | `/decisions/6/final` / `/doubts/4/reading` | scan021-section04 | Complete \Sigma_i, with the rounded bent body, short descending-sloped head run and small i at the right; short upper-run role remains head/retrace \| independent upper rule. |
| L021-16 | `/decisions/15/final` / `/doubts/9/reading` | scan021-section07 | Complete roofed \Sigma_\alpha^+, with the right-shifted roof, low alpha and raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-23 | `/decisions/22/final` / `/doubts/13/reading` | scan021-section11 | Complete roofed \Sigma_\alpha^+, with the lower arm shared with the alpha loop and the raised plus; separate short upper-run role remains head/retrace \| independent upper rule. |
| L021-26 | `/decisions/25/final` / `/doubts/16/reading` | scan021-section12 | Complete roofed \Sigma_{\alpha_0}^+, with distinct alpha_0 and raised plus; separate short upper-run role remains head/retrace \| independent upper rule. |
| L021-27 | `/decisions/26/final` / `/doubts/17/reading` | scan021-section12 | Complete \Sigma_{\alpha_0}^- \| \Sigma_\alpha^-, with the long high minus and one literal alpha/low-curl index group; the index doubt is retained, and short upper-run role remains head/retrace \| independent upper rule. |
| L021-33 | `/decisions/32/final` / `/doubts/20/reading` | scan021-section14 | Complete upright \Sigma_i^+, with its i and raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-34 | `/decisions/33/final` / `/doubts/21/reading` | scan021-section14 | Complete upright \Sigma_i^-, with its i and raised minus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-35 | `/decisions/34/final` / `/doubts/22/reading` | scan021-section14 | Complete \Sigma_{i\alpha} \| \Sigma_{i,\alpha} \| \Sigma_{\dot\alpha}, with the shared lower-arm hook/dot retained once; the index candidates remain qualified, and short upper-run role remains head/retrace \| independent upper rule. |
| L021-36 | `/decisions/35/final` / `/doubts/23/reading` | scan021-section14 | Complete upright \Sigma_{\alpha_0}^+, with its lowered alpha_0 and raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-42 | `/decisions/41/final` / `/doubts/26/reading` | scan021-section16 | Complete \Sigma_{\alpha_0}^+, with its lowered alpha_0 and clear raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-43 | `/decisions/42/final` / `/doubts/27/reading` | scan021-section16 | Complete \Sigma_i^+, with dotted i, raised plus, bent body, short dark upper run, interrupted pale left extension and small pale point to the left; short upper-run role remains head/retrace \| independent upper rule. |
| L021-48 | `/decisions/47/final` / `/doubts/29/reading` | scan021-section18 | Complete \Sigma_i^+, with the lower arm shared with the i stem, its detached dot and raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-49 | `/decisions/48/final` / `/doubts/30/reading` | scan021-section18 | Complete \Sigma_\alpha^+, with the lower arm shared with the low alpha curl and the raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-55 | `/decisions/54/final` / `/doubts/33/reading` | scan021-section20 | Complete roofed \Sigma_\alpha^+, with the right-shifted roof, low alpha and raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-64 | `/decisions/63/final` / `/doubts/36/reading` | scan021-section22 | Complete leading \Sigma_\alpha^+, with its low alpha and raised plus; short upper-run role remains head/retrace \| independent upper rule. |
| L021-66 | `/decisions/65/final` / `/doubts/37/reading` | scan021-section22 | Complete \Sigma_\alpha in the final X-complement group, retaining its low alpha, short upper run and bent body; short upper-run role remains head/retrace \| independent upper rule. |

All scan018 pointers belong to `out/records/scan018.json`; all scan021 pointers belong to `out/records/scan021.json`. The JSON records each exact old value, proposed value, selected-group span, root-authority span/hash and local qualification fields. Each root section is included verbatim in its authority catalog.

## Qualification and role preservation

L018-15 keeps the inserted Pi recurrence, its circle-first/zero alternative and its unchanged later printed primary. L021-27 keeps both complete minus-bearing index candidates. L021-35 keeps all three complete index candidates and the shared hook/dot. L021-43 retains the dark upper run, interrupted pale left extension and pale point within its own selected A021G12 group. Every listed Sigma retains its local short-head role doubt.

The proposal changes no alternatives array/string and no witness or reader-owned value. It changes no page, graphical path, source excerpt, printed-wrapper flag, count or mathematical-consequence field.

## Historical map dependency

`out/checks/scan018_final_source_map.json#/doubt_coverage/6/reading` contains the former public primary as an assembly snapshot. Per the root instruction, that historical map and all **263** equal-digest record leaves are preserved. The separate dependency JSON identifies the snapshot and the two current record targets. No map replacement or hash rebinding is proposed. Scan021 has no exact copy of the deficient generic-final literal in its source map.

## Reversible patch and byte guards

The JSON contains separate forward and inverse JSON Patch operations for both records, guarded by exact before values and original file hashes. In-memory replay changed only the 40 allowed fields and restored each original record’s exact UTF-8 bytes. No patched record, map or page was saved.

| File | Existing SHA-256 |
| --- | --- |
| `out/records/scan018.json` | `42a52aebd1f3157cf16540f01407289091564676f9e7b792c33e93a06dd118c4` |
| `out/pages/J81-02_81_scan018.tex` | `b194c003d55fa088e4a8db1f64875c59919c253715c510298f7785daa9291e62` |
| `out/records/scan021.json` | `9f98d5d0cdbfe80b530915fdd818b659d8616855c2216538bd68abe035440429` |
| `out/pages/J81-03_81_scan021.tex` | `96772b7d5d36792f72827807deffaa39e746d1876f771e9dd498cbcf0238ddce` |

The page hashes remain invariants. The proposed post-patch record hashes are recorded for later root-authorized application, using the existing JSON serialization. This is a source-only reporting proposal; it does not complete the final audit or add an ink or mathematical decision.
