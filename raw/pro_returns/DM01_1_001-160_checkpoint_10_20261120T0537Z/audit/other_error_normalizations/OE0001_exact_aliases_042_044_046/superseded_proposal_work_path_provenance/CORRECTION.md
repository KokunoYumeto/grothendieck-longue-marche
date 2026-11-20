# Addendum: duplicated unmarked-error observations

This addendum corrects earlier coordination descriptions without rewriting the
historical records or the primary and peer reports.

- The final scan042 coordination record said the peer observation of the
  unmarked word before M0888 had not duplicated the error row. In fact, the
  primary and peer used different full-row text, and `import-check` appended
  both rows. The pre-normalization table contains both observations.
- The final scan044 coordination record likewise said no duplicate peer error
  row was added for the unmarked sequence before M0920/M0921. Both differing
  full rows were appended and are retained in the before snapshot.
- Scan046 also has two differently worded observations of the same accepted
  unmarked error before M0954. The root explicitly selected the final primary-B
  row as canonical and the peer row as its alias.

The root reviewed these three exact pairs. This transaction retains the
existing primary row for each pair verbatim, removes only the three registered
peer aliases from the authoritative error table, and retains both complete
observations in their original reports and the before snapshot. The table
therefore changes from 14 observation rows to 11 distinct error rows.

This is a text-only record and tooling correction. It adds no image inspection,
handwriting judgment, reading revision, mark decision, check event, or reading
time. Existing report text, receipt history, and historical coordination notes
remain unchanged.

The alias registry compares all four serialized TSV fields exactly and verifies
their SHA-256 hashes. It does not merge errors by scan, place similarity,
reading similarity, or any other inferred relationship. Future alias groups
require their own explicit root review and an audited registry update.

The original `reconcile.py verify` did not inspect `other_errors.tsv` and did
not enforce any exact union of report errors. The added check establishes only
that the table contains no registered alias and no exact duplicate. It does
not claim that every possible report error has been included; report-to-table
completeness remains a separate review responsibility.
