# Hand attribution audit: scans 170–180

## Scope

Written-record metadata review only: all 11 `decision.json` inventories (141 rows) and all 33 corresponding A/B/C `report.json` inventories (421 rows), with relevant attribution/origin notes in those same records. Rows were matched by element, object and position, not merely by index. No image, scan, OCR, PDF extraction, internet, rendering, TeX engine or future-page file was consulted. All indices below are zero-based. No decision file was edited by this auditor.

## Additional definite contradiction

`scan172/decision.json`, `inventory[13].hand`, initially read **`his hand`** for the bottom-left archive sheet number **172**. All three written reader records distinguish this entry from authorial writing:

| Record | Inventory row | Recorded hand |
|---|---:|---|
| `scan172/A/report.json` | 12 | `archive pencil; additional hand not identified` |
| `scan172/B/report.json` | 13 | `archive pencil; not attributed to the author` |
| `scan172/C/report.json` | 13 | `archive pencil hand` |

Suggested correction: set `scan172/decision.json` → `inventory[13].hand` to **`archive pencil; not attributed to the author`**, preserving the wording of its corresponding B row. This corrects the metadata without identifying a particular archival writer. The decision's own notes also call the number archive pencil 172.

At report save, that field reads: `his hand`.

## Known scan 180 correction

The previously identified `scan180/decision.json` → `inventory[10].hand` concerns archive sheet number **180**. Its source rows are A[10] (`archive pencil; not assigned to the author`), B[9] (`archive pencil hand, separate from the main writing`), and C[10] (`archive pencil hand`). At report save, the decision reads **`archive pencil hand; distinct from main writing`**; this agrees with the written evidence.

## Remaining records

No additional definite hand-attribution contradiction was found in the reviewed decisions. Existing uncertain or unassigned labels for isolated marks were retained as evidence, without converting possible main-ink appearance or uncertain semantic role into a new hand attribution. Scan 172's separate inline point at `inventory[12]` has authorial hand labels in all three reader inventories and is not another demonstrated normalization error.

## Disposition after recovery

The preceding report is restored from the retained original writing/tool-call text. Its “At report save” statements describe the original audit snapshot.

Root reports that both accepted metadata fixes are now applied:

| Decision field | Accepted hand value |
|---|---|
| `scan172/decision.json` → `inventory[13].hand` | `archive pencil; not attributed to the author` |
| `scan180/decision.json` → `inventory[10].hand` | `archive pencil hand; distinct from main writing` |

These fixes change hand-attribution metadata only; there is no transcription change. The helper's author normalization now matches only explicit author-hand labels, not substrings such as “not attributed to the author.” This recovery restored only this report and added this disposition; it did not repeat the audit, read images or change decisions.
