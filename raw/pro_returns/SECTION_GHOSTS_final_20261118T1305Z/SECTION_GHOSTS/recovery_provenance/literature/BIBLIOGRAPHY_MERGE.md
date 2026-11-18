# Bibliography merging instructions

Do not concatenate the copied checkpoint bibliography and the recovery bibliography blindly. The checkpoint copy is provenance, not an additional bibliography input.

The recovery file contains 12 entries. Against all checkpoint08 notes bibliographies, 10 keys are new and 2 already occur. Against the actually integrated aggregate SECTION_GHOSTS_references.bib, only Stix2015 already occurs: LitPalSchlank2022 was present only in the unintegrated notes bibliography. The final aggregate therefore adds 11 keys to its original87, yielding98 distinct keys, with no duplicate definitions.

- `LitPalSchlank2022` already occurs in `literature_infinite_matching_references.bib`. Keep the baseline entry, or replace it by the recovery version to include the additional exact author-version locators; the bibliographic fields agree.
- `Stix2015` already occurs in `root_references.bib`. Keep the baseline bibliographic fields; the recovery entry can replace its note/URL with the newly verified v3 and publisher locators.

The following10 keys are absent even from the checkpoint notes. Append them once; additionally append LitPalSchlank2022 to the aggregate master because it was not previously integrated:

- `LitContiDemarcheFlorence2026`
- `LitKhareLarsen2024Heisenberg`
- `LitScavia2026GlobalLifting`
- `LitNeukirch1973Embedding`
- `RecoveryGilleSzamuely2006`
- `RecoveryColliotTheleneSkorobogatov2019`
- `RecoveryBarySorokerJardenNeftin2015`
- `AuditDDM2021`
- `AuditMilneAV2008`
- `LitKhareLarsenRamakrishna2005`

P16 citations also use the pre-existing `CohMilneADT` key; retain the checkpoint entry. The new P16 Brauer corollary uses `RecoveryGilleSzamuely2006` and `RecoveryColliotTheleneSkorobogatov2019`.

Recovered P16 wrapper: `result` environment, identifier P.16, status Proved. Mathematical text through P.16.12 is checkpoint text. New transcription is explicitly confined to the already reviewed P.16.13–16 corollary.
