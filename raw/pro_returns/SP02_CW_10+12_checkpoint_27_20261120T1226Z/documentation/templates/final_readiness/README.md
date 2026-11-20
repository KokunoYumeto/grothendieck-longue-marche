# Incomplete final-readiness templates

The JSON templates are incomplete root-populated schemas, not live evidence.
The question placeholder has no invented question ID or classification.
The CHECK_EVENTS.tsv template contains only the exact user-required header;
it has zero events. Do not replace the live log with this template.

The five event columns are `statement_id,date,who,type,outcome`.
Only actual mathematical-work events belong in that log. Accepted types are:

- `targeted proof check`
- `independent re-proof`
- `computation or formal certificate`
- `used and rechecked in this run`
- `carried as background without fault found`
- `refuted`

A refuted event must name its refined statement ID in the outcome, for example
with the label `refined statement ID:`, or use the supported equivalent type
form `refuted: ID`. These are schema descriptions, not recorded checks.
Background status is valid coverage and is distinct from newly performed work.

Bibliographic and transcription standing questions need concrete reviewed
notes evidence but no CHECK_EVENTS row. Do not create administrative or
transcription event types. See ../../final_readiness_schema.md for exact keys,
phase ordering, and supported refined-ID forms.
