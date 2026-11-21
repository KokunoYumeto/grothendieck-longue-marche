# Scan 022 — initial source-only audit

Status: two bounded source repairs required; the complete record has not yet been released for audit. Root ink choices remain the authority. This audit supplies no ink approval.

## Frozen release

| Artifact | SHA-256 |
|---|---|
| `out/checks/scan022_final_draft.tex` | `843d6f48ca05cc4ecebce7a9fd2ced57005aece94e3b7b073f10acba3326b5e6` |
| `out/checks/scan022_final_source_map.json` | `55bb48d1bee684955fdef861d78da6fb94a329c79acadae06f098efa90d710f9` |
| `out/checks/scan022_assembler_source_validation.json` | `60cf4046e150459de06fa88b329dd8c5d99ae04f89b12b3141ef159c3f14a9dd` |

Exact initial copies are retained in `out/checks/scan022_source_audit_initial_release/`.

## Completed source review

The full selected LaTeX was read against root journal §§01–15 and the literal A/B/C sources. Its 23 recorded operations replay exactly; 47 assembly segments cover the selected source. All 889 recorded text-span occurrences and 507 source-bank pointers resolve. The source contains 44 selected groups, 67 A word-label spans, 142 node commands and 107 draw/fill paths. No selected original path span is duplicated. Braces, environments and math boundaries balance. Active picture declarations use `x=0.085mm,y=-0.085mm`. Origin, anchor, baseline and path declarations were checked literally; no coordinate arithmetic or physical-scale validation was performed.

The selected wording and graphical components reflect all 15 root choice sections. This includes the complete closer alternatives, both lower-annotation states, the crowded C S10 qualifier, the S11/frame shared-run ownership, the two B lower-frame runs, the C relation after Z and the two separately owned final points. The map carries C42/H32 and the authorized three resolved/four retained original C rows. The source catalog preserves seven actual C rows and exactly seven canonical `-1` parts. The current map content note remains attributed, with empty `check_events`.

## Defects and smallest repairs

### QA022-S01 — joined group-marker comments

At initial draft lines 27, 440 and 520, the preceding END marker and next BEGIN marker share one comment line: G01→B M01, G12→B M06 and G14→B M07. The preceding map group span consequently contains the following BEGIN marker. The later active code remains present. Insert one newline at each join and refresh the affected final spans, offsets, hashes and exact current mirrors.

### QA022-S02 — donor and selected word-label references

| Imported group | Original donor ownership | Selected ownership |
|---|---|---|
| B022-M01 | B T03: `pour` | A T06: `pour prouver que` |
| B022-G08 | B T10: live `\ne\varnothing` | A T15: live `\ne\varnothing` |
| B022-M06 | B T32: qualified `formule|relation` | A T48: firm `formule` |

The active imported comments carry the donor T labels without their namespace. Change those three comments to identify the selected A labels; retain the original donor comments in provenance. tex022 has reported root authorization for these six edits: three newlines and three comment substitutions.

## Pending frozen record review

The complete record review will cover all 66 scopes and their confidence/count flags; all A/B/C readings and qualifier provenance; exact canonical C parts; local H marker flags; all count-parent mirrors; reciprocal graphical associations; the A71-plus-four inventory and hand scopes; selected attachments; and attributed notes with empty page check events. No record approval is implied by this initial source pass.

## Scope and preservation

Only text sources, offsets, hashes, source balancing and clerical counts were used. No images or image hashes, crops, OCR, compilation/rendering, research, installation, mathematical proofs or coordinate computations were accessed or performed. The auditor changed no selected draft, map or record, and prepared no later scan. This initial audit remains unchanged; the repair review and record audit will be a separately hashed closure.

Initial JSON audit SHA-256: `aa5e3d1d23552403bf3c68f7c0436794c48afe143b6549ad0bfd40e27c0d3dc8`.
