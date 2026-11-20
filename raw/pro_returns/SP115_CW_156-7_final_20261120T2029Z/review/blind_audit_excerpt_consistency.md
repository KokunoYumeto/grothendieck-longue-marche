# Blind-audit excerpt consistency review — scans002–007

Review window: **2026-11-20 20:11:54 UTC–2026-11-20 20:17:40 UTC**. Read-only comparison of decision JSON, current/frozen-initial pages, adjudication TSVs, final review change records and stored audit excerpts. No crops were viewed and no ink decision was made.

## Result

**One concrete stale excerpt was found and resolved during the review. No outstanding contradiction was identified in the six completed audits at the final recheck.**

### Resolved: scan006 B022 / change place006-A05

The adjudication `final` initially remained `\deleted{\unsure{x}}`. The authoritative decision evidence, patch, `change_updates["006-18"].final`, and current page line14 require the retained alternatives `\deleted{\unsure{x|de}}`. The patch targets the wider string `\forall\deleted{\unsure{x}}X`, so it could not update B022’s narrower frozen first excerpt automatically.

Reader A synchronized `decisions.boxes.B022.final`, the B022 adjudication `final`, and the B022 entry in `review.audit_changes`. All three were independently rechecked here as `\deleted{\unsure{x|de}}`. The current page already carried that reading. This was synchronization of existing root authority; no new ink decision or K change.

## Checks completed

- 178 adjudication rows across six scans were checked against the decision records and stored audit excerpts.
- All six current pages exactly equal their frozen initial pages after the recorded ordered patch sequences (43 patches).
- All 31 `change_updates` records and 10 `new_changes` records agree with the corresponding final review metadata.
- No duplicate review change IDs were found. Blind audit place IDs were treated as a separate namespace from review/collation change IDs.
- Narrow or incomplete excerpts, TeX layout wrappers, and reduced diagram excerpts were not treated as page omissions. In particular, scan006 B047’s empty frozen first excerpt is not an omission of the formula from its frozen initial/current page.

## Snapshot hashes

The following hashes describe the final reread, after Reader A’s scan006 synchronization. They are metadata checkpoints, not a new freeze.

```text
scan002 (16 adjudication rows)
  page: 117aa6458bc330e149d20a53e4131f0364b6051933abe476cd81fede41bd83ba
  decisions: c228134eb5835cee02cd9599ab87b2c456420dcb3fe40442d451c17d4fdbe44d
  adjudication: e4f2f35c3360fcbec66548e5387f77525528e83aa971534d6485f2945e34235a
  review: d2435d1d06ed47813fb3ca4eb9984fa525e7d3c8b259e83e1252602064a08d48
  initial: e53511a2120a9fa187f41390796c49bfda3c6cf29a331b5fd8d85c30424efb66
scan003 (13 adjudication rows)
  page: 53b94d6ebf40be70862d37ccd09206f14f5daa04fa5a0cae248626e3519f9aa7
  decisions: de4ff31b82f17af18061f79b7ac8277aa4cf872fa1618053a9a2cd7563ed84eb
  adjudication: 1475a6ffde32fa6193c36241c2b7ead89f169788147e4435ca85b4d30221c5ef
  review: 9a6e199ad177e3b74f1ab9dfaffe5d65b8b1d2b5e6eeb598b6cec356dd3639d1
  initial: 83263f844fcb11a6e3fcabdcd1605b6fc3d11a02aeef19b1afea087e6eaa93a6
scan004 (24 adjudication rows)
  page: 90181e8a84b859c602ae371d278908fb7d354ee0d8da3b63a9d38743793f6ef0
  decisions: b6b59ccdeffd907883477fc982ec447225355a15dd150cc74489797a3a6752d0
  adjudication: 472a6a0d200b047338e258d5364d72ceee72a1191735437defd832fc89513150
  review: 0d9ccfd4728e7162c7a6370e1fafedb2c8daceacd6c2860a6dfa09ded3754732
  initial: 11bfd0bbdd5dad4d507205d38a21837d66165a5d9dac1158c44a5836ace10b81
scan005 (43 adjudication rows)
  page: beb00da309ce969a517be848163af8ec55f579e90f5d55d2bf6b46c64b49c797
  decisions: c19c94e29f1db00476ad6ecd25dc9f629b5aba3f0e919c5b4c9d8bb3d2b08fab
  adjudication: 0d0d2fd3551ab5449e32a3067218c2bc783f0dd5681544f43960596cbfc45231
  review: d294ba0cc559349fe9b13f449663d9520cbdc74bc0c4bbb46eb250373128c7ac
  initial: f403b4a83a6e4aac240932dcb08aed9849c868b852c9f9c95f26a062959f236d
scan006 (47 adjudication rows)
  page: 268817bc4186f5e48297353aed32aaf4916c47b7c44c2a21da8a2447cf310430
  decisions: bfe700ff721ef9252330bb18b548e341672b12a1fbfdff34cf4d80b479f08c82
  adjudication: 5f1169c19ec0124d52aa7910aa2fadb1d711fea497796958b1cae0c32d94a94b
  review: 8645587a65e90cda4b0fc9cec22981b43473162c7e563f6742382665abde0855
  initial: ac10295a550ab3de910fbd7b5a74d35d65e2c2b08b5810aba188e1c453bc3238
scan007 (35 adjudication rows)
  page: ceb5de05a8b5b933f25de8e3473958b742d001201e9dd85d54f1a1ff589ebfae
  decisions: f96842f674e297432a57b5c0c877dff69b4b81274a0161d5e7af3822906c45a5
  adjudication: 42fb448779b419cda88b5c64bf4c2eaf881d5bc391697123de8bb1a5516a31fe
  review: c77e4ca1520c6a1558b1a3dbd5c3e87673eb0ce0b48813869a605e2b1bb9f960
  initial: fc66fb2c84ebab8239d635ddda8bfa825a73da12c40548bd5b3db58dc29e3335
```

Only this review note and the separately authorized integrity-script corrections were written by this reviewer. The authorized integrity run wrote `review/deliverable_integrity.json`; it preceded the subsequent root-extent support patch and is not a final-pass certificate. No transcription, frozen first/second/boxes TSV, decision, adjudication or root review file was edited by this reviewer.

## Scan008 addendum

Metadata snapshot: **2026-11-20 20:23:46 UTC**. The same read-only comparison was extended to completed scan008. No source images were consulted and no ink decisions were made.

**No concrete excerpt inconsistency was identified.** All 32 adjudication rows agree with their decision records and stored audit excerpts. The current page exactly equals the frozen initial page after the eight ordered patches. All nine `change_updates` agree with final review metadata; there are no `new_changes`. The seven unique changed-place IDs are `008-A01` through `008-A07`.

Changed excerpts and overlapping scopes were checked explicitly at B003, B004, B006, B011, B012, B014, B020, B021, B031, B032 and B040. Each final excerpt is the frozen first excerpt after the applicable recorded patches, or the explicit authoritative box override. No superseded patched span was found in a changed final excerpt. Narrower excerpts and the globally cancelled draft were evaluated in their full page context rather than treated as independent page omissions.

```text
scan008
  page: 55a3872da2206b770473290ec83cf0079c4ce7e3b4fcb9e792b47d3509b4b17d
  decisions: f38b6729c3af0fc97b315c5c7ed3a0f5438945854719aed07bee60ff0c6603bf
  adjudication: 3f0ac90d1aa0df9f62602e3baaa86f1d35c2b93a45af4e91a31a5f0402a4d9e2
  review: 3016fe956fabc184f29039c74e679ba0710846ea76047684acc9c00bce81c06d
  initial: 4c4020de2ecc04c946c762002fecd5957f93c95434d3c9c33111010fe613fe2b
```

These are review snapshots, not final-freeze records. This addendum changes only the metadata review report.

## Scan009 final addendum

Metadata snapshot: **2026-11-20 20:28:59 UTC**, after Reader B confirmed the authorized separator repair and final metadata synchronization. No source images were consulted and no ink decision was made.

**No concrete excerpt inconsistency remains.** All 30 adjudication rows match the authoritative decision transformations or explicit box overrides. All 12 stored `audit_changes` final excerpts match adjudication. The current page exactly equals its frozen initial page after the 18 ordered recorded patches; all 14 `change_updates` and three `new_changes` match final review metadata. The 18 unique changed-place IDs remain `009-A01` through `009-A18`.

Changed and overlapping excerpts were inspected at B003, B004, B006, B007, B009, B010, B012, B016, B024, B025, B029 and B030. B007 consistently includes the repaired `\Longrightarrow Z` token boundary in the page, decision override, adjudication and stored audit excerpt. The retained `\deleted{\unsure{impossible}}` inside the newly prefixed phrase is intentional, not a superseded old-span remnant. Narrow excerpts preserve their source-state wrappers and are not treated as page omissions. The separately identified transient separator error was a TeX repair by Reader B under root authority, without a new ink decision or K change.

```text
scan009
  page: 1446d1135a0ecf30e7eb39ece913bb2d29a0ebc20a42abe6733875709437e77a
  decisions: c9e431ac53133d8ccd201d8e1edec5bd8df7c8024ee5709f3f29dce162459ecf
  adjudication: 982b2af9212bf98bc012446634f09d3886b8d75a68dc8a28772b6d88ec9f40bb
  review: 01ea580e8fc9d4299850ba7d8792616ca6f54e58c1315b659739e9f70cae4f89
  initial: f2b59d9af15c50fb79bfb44bf8f799f73dd82f62f1d283d2abdd2492c5007b8f
```

All eight page hashes and the combined-transcription hash still match the recorded 20:27:43 UTC freeze at this review snapshot. This is a metadata snapshot check; the required end-of-run log entry remains root’s responsibility. Across scans002–009, this report covers 240 adjudication rows, 69 ordered patches, 54 change updates and 13 new change records. No outstanding contradiction was identified after the authorized synchronizations. Only review reports were changed in this final pass.
