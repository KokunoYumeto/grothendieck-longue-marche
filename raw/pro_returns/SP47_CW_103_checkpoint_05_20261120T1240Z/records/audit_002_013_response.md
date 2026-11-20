# Response to AUD-S002-001

## Completed change

Changed `decisions/scan002.json`, JSON pointer `/inventory/19/first_words_or_objects`, element **Heading final s**:

- Previous value: `s, preferably live; alternate cancelled state marked`
- New value: `live handwritten s`

The new inventory description agrees with the already adjudicated live handwritten `s` in `/changes/7/final` and the committed page. This is a documentary synchronization only. A structural comparison confirmed that this one JSON field is the only change to the decision.

## Builder/configuration check

Searched `decisions`, `adjudication`, and `scripts` for the exact stale wording. The only occurrence was the final decision field above. No scan002 adjudication configuration or builder contained that literal, so none was changed.

The located builder, `scripts/decide_scan002.py`, copies the historical reader A inventory at line 67 (`inv=copy.deepcopy(reports['A']['inventory'])`). Its source does not contain the stale wording. The historical reader return remains untouched as instructed; rerunning that original decision builder would copy that historical description again. No builder, assemble, or workflow command was run.

## Changed paths

- `decisions/scan002.json` — the single inventory description above.
- `records/audit_002_013_response.md` — this completion record.

No page text, historical reader return/report, audit finding report, image, or witness was changed. No image or witness was inspected, and no deliverable rebuild was performed.
