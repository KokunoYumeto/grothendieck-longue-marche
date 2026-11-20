# Final staged serialization plan — reader C

**Prepared and released for root review; no stage has been executed.** The script defaults to a read-only preflight. Applying a stage requires both `--apply` and the exact reviewed plan SHA-256. Preflight creates no receipt, lock, progress entry, or other file.

## Final artifacts and hashes

- [staged_serialization_c.py](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py) — SHA-256 `a44e25b216f928870ebfe8a258243a6e2d88c972fd436a52aeedf25293aa5878`.
- [staged_serialization_plan_c.json](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_plan_c.json) — SHA-256 `945a58018a53d7e50db53c1487b4009794212c41159a75f1ec108f6e06dba36a`.
- [final_static_recheck_c.md](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/reader_reports/final_static_recheck_c.md) — SHA-256 `be4fd9f73a732e1a60ddbbb56df5ec8dff58f8e996d5d84c9afd6b1aebc0ac6e`.
- The initial [final_static_review_c.md](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/reader_reports/final_static_review_c.md) remains unchanged at SHA-256 `af29108936aecfa2927c89d315f5bc2e7bce8b4d4eb8b9d6d6a8f52624d092a7`.

The machine plan contains every full old/new replacement string, exact JSON pointer, row identity, old/new string hash, reference input/output file hash, and historical exclusion. The script was syntax-parsed without importing or executing it. Reference outputs were calculated in memory while preparing the plan; no target was written.

Reference hashes were refreshed at **2026-11-20T22:32:50.147827+00:00**, after root applied A/B's unrelated metadata operations. The 019, 026, and 027 reviewed-report hashes were repinned; all selected old values and identities still matched. All requested 021–027 source risks have been checked, and the final recheck is pinned as a script guard.

## Stage summary

| Stage | Page scope | Current JSON fields | Operations | Target files |
|---|---|---:|---:|---:|
| `serialization` | 10 blocks on 6 pages | 35 | 45 | 18 |
| `gamma` | 7 occurrences on 024 | 13 | 14 | 3 |
| `prime026` | 1 occurrence on 026 | 7 | 8 | 3 |
| `superscript027` | 1 grouping on 027 | 9 | 10 | 3 |

There are 77 listed operations across 27 target files: nine page fragments, nine current reviewed reports, and nine accepted adjudications. The 64 JSON operations each name one complete string field. A page operation can replace one block or, for Gamma, seven occurrences of one exact token. These numbers are operation counts, not newly adjudicated manuscript readings.

### serialization — original ten page operations

D1–D4 affect page 013; D5 affects 019; D6 affects 012; D7 affects 015; D8–D9 affect 018; I1 affects 014. Their exact page old/new blocks remain those reviewed and approved by root.

Every cancelled constituent retains its cancellation. D7 specifically moves the margin command outside the outer `\sout` and retains the note's cancellation as `\margin{\deleted{...}}`. The note does not become live. D9 retains both existing deletion layers on the formula and boxes the existing inline TikZ picture without changing its paths. I1 remains a live insertion.

All 45 stage-one page/field operations passed the in-memory payload-token comparison after removal of only moved serialization wrappers and added `\displaystyle`. The explicit old/new nesting, rather than token equality alone, records cancellation scope.

### gamma — separate page 024 stage

The final audited page has seven `\mathbb\Gamma` tokens. Each is replaced by the following inline code, with no new macro or preamble edit:

```tex
\mathord{\text{\begin{tikzpicture}[
  x=1em,y=1ex,baseline=0pt,
  line width=.045em,line cap=butt,line join=miter]
  \draw (.04,0)--(.04,1.60)--(.58,1.60)--(.58,1.40);
  \draw (.16,0)--(.16,1.40)--(.58,1.40);
\end{tikzpicture}}}
```

The short downturned right tip was added at root's request from the already recorded shape: the outer top continues from `(.58,1.60)` to `(.58,1.40)`. Its height is 0.20 ex. The nonzero dimensions and stroke width use `em`/`ex`; the supplied `\text` implementation selects font size for the math style. `\mathord` retains ordinary math-atom behavior.

The stage includes fourteen Gamma substitutions across ten current report fields and seven across three adjudication excerpts, in addition to the seven page occurrences: 28 exact token substitutions in fourteen operations. The audited undersets, marginal NB, and word uncertainty remain unchanged.

### prime026 — literal apostrophe

The exact serialization change is:

```tex
\alpha\prime  ->  \alpha'
```

The complete uncertainty remains `\unsure{\alpha^i|\alpha_i|\alpha'}`. This follows root's explicit prime convention and makes no new ink decision. Six current report fields, including `notation[6].form`, and one accepted adjudication excerpt mirror the page change.

The post-audit release is now open. Its final page 027 gate accepts only two explicitly pinned full-file hashes: the completed root adjudication and that same adjudication after the exact planned S1 excerpt grouping. This allows P1 and S1 to be applied in either order without accepting unrecognized adjudication content.

### superscript027 — uncertain-base grouping and one explicit current-quote synchronization

The brace-only operation is:

```tex
\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}
```

to:

```tex
{\unsure{\dot\rho|\rho}}^{\deleted{\unsure{2}}}
```

The extra grouping prevents an additional superscript from attaching directly after `\unsure`'s own question-mark superscript. Both cancellation-scope alternatives, the uncertain exponent 2, and both uncertainty levels remain intact.

Reader A/root also handed off only `c_markup_audit.items[1].reading`, which still quoted the older `\deleted{\unsure{\dot\rho}}`. The plan labels its synchronization to accepted U027-02 as `S1-current-quote-c_markup`, separately from the brace-only changes. Its new value is:

```tex
\unsure{\deleted{\unsure{\dot\rho^2}}|{\unsure{\dot\rho|\rho}}^{\deleted{\unsure{2}}}}
```

The associated `source_span`, ordinal, historical witness quotation, and prior instruction payloads remain unchanged. A's fourteen other 027 metadata edits were applied before this plan's reference hashes were refreshed and are preserved.

## Exact current-field plan

Pointers use zero-based array indices. The entire old and new field strings, their hashes, and any identity guard are in the machine plan. Only these raw JSON string-literal spans may change; the enclosing objects are never reserialized.

### serialization

**`reader_reports/145_scan012_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/audit/differences/2/final` | D6 | B03 |
| `/audit/differences/4/final` | D6 | B05 |

**`second/145_scan012_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/2/final` | D6 | B03 |
| `/differences/4/final` | D6 | B05 |

**`reader_reports/145_scan013_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/audit/differences/8/final` | D1 | B09 |
| `/audit/differences/13/final` | D2 | B14 |
| `/audit/differences/14/final` | D3 | B15 |
| `/audit/differences/17/final` | D4 | B18 |

**`second/145_scan013_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/8/final` | D1 | B09 |
| `/differences/13/final` | D2 | B14 |
| `/differences/14/final` | D3 | B15 |
| `/differences/17/final` | D4 | B18 |

**`reader_reports/145_scan014_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/changes/9/final` | I1 | s014-10 |
| `/audit/differences/2/final` | I1 | B08 |

**`second/145_scan014_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/2/final` | I1 | B08 |

**`reader_reports/145_scan015_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/audit/differences/1/final` | D7 | B02 |
| `/audit/differences/2/final` | D7 | B04 |

**`second/145_scan015_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/1/final` | D7 | B02 |
| `/differences/2/final` | D7 | B04 |

**`reader_reports/145_scan018_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/changes/4/final` | D8 | s018-05 |
| `/changes/20/final` | D9 | s018-21 |
| `/doubts/12/reading` | D9 | — |
| `/inventory/9/first_words_or_objects` | D8 | — |
| `/inventory/20/first_words_or_objects` | D9 | — |
| `/inventory/24/first_words_or_objects` | D9 | — |
| `/audit/differences/1/final` | D8 | B02 |
| `/audit/differences/5/final` | D9 | B06 |
| `/audit/differences/6/final` | D9 | B07 |

**`second/145_scan018_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/1/final` | D8 | B02 |
| `/differences/5/final` | D9 | B06 |
| `/differences/6/final` | D9 | B07 |

**`reader_reports/145_scan019_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/changes/13/final` | D5 | s019-14 |
| `/inventory/8/first_words_or_objects` | D5 | — |
| `/audit/differences/5/final` | D5 | B07 |

**`second/145_scan019_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/5/final` | D5 | B07 |

### gamma

**`reader_reports/145_scan024_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/changes/3/final` | F1 | s024-04 |
| `/changes/4/final` | F1 | s024-05 |
| `/changes/7/final` | F1 | s024-08 |
| `/changes/9/final` | F1 | s024-10 |
| `/decisions/3/reading` | F1 | M0857 |
| `/doubts/7/reading` | F1 | — |
| `/doubts/7/alternatives/1` | F1 | — |
| `/audit/differences/0/final` | F1 | B01 |
| `/audit/differences/1/final` | F1 | B02 |
| `/audit/differences/3/final` | F1 | B04 |

**`second/145_scan024_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/0/final` | F1 | B01 |
| `/differences/1/final` | F1 | B02 |
| `/differences/3/final` | F1 | B04 |

### prime026

**`reader_reports/145_scan026_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/changes/31/final` | P1 | s026-32 |
| `/doubts/12/reading` | P1 | — |
| `/doubts/12/alternatives/2` | P1 | — |
| `/inventory/0/first_words_or_objects` | P1 | — |
| `/audit/differences/0/final` | P1 | B01 |
| `/notation/6/form` | P1 | — |

**`second/145_scan026_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/0/final` | P1 | B01 |

### superscript027

**`reader_reports/145_scan027_reviewed.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/changes/6/final` | S1 | s027-07 |
| `/unlisted_decisions/1/reading` | S1 | U027-02 |
| `/doubts/4/reading` | S1 | — |
| `/doubts/4/alternatives/1` | S1 | — |
| `/inventory/12/first_words_or_objects` | S1 | — |
| `/inventory/13/first_words_or_objects` | S1 | — |
| `/audit/differences/4/final` | S1 | B05 |
| `/c_markup_audit/items/1/reading` | S1 — quotation sync | ordinal 2 / E14 / B05 |

**`second/145_scan027_adjudication.json`**

| JSON pointer | Case | Identity |
|---|---|---|
| `/differences/4/final` | S1 | B05 |

## Hash and exact-field protections

Pages, accepted adjudications, the initial static report, the final recheck, and the supplied preamble are bound to their reviewed full-file SHA-256 hashes. The script also verifies its own digest against the plan, validates each stage's fixed target and operation counts, and checks each old/new string hash.

For current reviewed reports only, root authorized tolerance of unrelated metadata changes. Every listed field must still have its exact old value/hash and row identity. The script replaces only that field's raw JSON string-literal span, verifies that the changed leaf paths are exactly the approved pointers, and preserves every unlisted byte of the observed report.

If the report matches its reference input hash, the complete output must match the precomputed reference output hash and byte count. If unrelated field drift is present, the script records that fact, preserves those observed fields, and pins the observed full preimage and computed full output hashes for the operation. Apply rechecks the observed full preimage immediately before writing. It does not ignore a changed selected field, infer a replacement, or recursively rewrite JSON.

Receipts and preflight output distinguish reference hashes from observed hashes and flag `unrelated_field_drift`. This prevents earlier A/B metadata edits from being overwritten while retaining exact selected-field and immediate-preimage hash checks.

## Historical fields and files intentionally unchanged

- Initial reader report JSON/TeX, the initial static review, and every independent first or second reading.
- Comparison TSVs, token-difference files, reading receipts, assignments, boxes, crops/manifests, seals, witnesses, source packets, images, and checkpoints.
- Existing evidence, reading, review, adjudication-generation, and prior synchronization scripts.
- Witness fields `changes[*].C` and `changes[*].H`; `second_boxes[*].reading`; and `audit.differences[*].first` / `second`.
- Adjudication `page_edits`, both old and new, and entire `report_replace` / `report_append` subtrees. These preserve prior instructions and are not current excerpt fields.
- The original C-audit `source_span` associated with the handed-off 027 current reading.

The machine plan lists 87 matching historical pointers individually. It also documents two current page 013 excerpt pointers deliberately outside this stage: `audit.differences[1].final` and `differences[1].final` for the independently cancelled top formula already represented safely in the page's TikZ node. Those two isolated excerpts are not silently included among the ten page fixes or mislabeled as history.

Prior instruction payloads must not be replayed as though they describe the post-serialization state. New receipts record the later serialization layer without rewriting the earlier instructions.

## Apply receipts and progress logging

Apply takes a dedicated staging lock and reserves a new directory under `reader_reports/serialization_receipts/`. It saves exact observed `before/` copies and planned `after/` copies of every target. The receipt records the plan/script hashes, source guards, stage, UTC times, reference and observed input/output hashes, operation IDs, pointers, counts, old/new string hashes, drift flags, and committed paths.

Each target replacement is atomic. The multi-file stage is not one filesystem transaction, so root should run these stages sequentially with other writers to the same targets paused. On failure, a target is restored only if its observed current hash still matches this stage's output; an unexpected newer value is left for manual recovery. The receipt records each rollback result.

`progress.log` receives append-only started/applied entries, or a distinct failure entry, containing UTC time, stage, plan digest, and receipt path. Preflight creates none of those files or entries. The script does not compile TeX, update seals, edit run-state metadata, regenerate aggregate apparatus, or import any existing evidence/build script.

## Commands for root

These commands have not been run by C. Default and explicit preflights are read-only:

```bash
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage gamma
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage prime026
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage superscript027
```

After root's review, the explicit apply commands for this exact plan revision are:

```bash
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage serialization --apply --plan-sha256 945a58018a53d7e50db53c1487b4009794212c41159a75f1ec108f6e06dba36a
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage gamma --apply --plan-sha256 945a58018a53d7e50db53c1487b4009794212c41159a75f1ec108f6e06dba36a
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage prime026 --apply --plan-sha256 945a58018a53d7e50db53c1487b4009794212c41159a75f1ec108f6e06dba36a
python3 /workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/scripts/staged_serialization_c.py --stage superscript027 --apply --plan-sha256 945a58018a53d7e50db53c1487b4009794212c41159a75f1ec108f6e06dba36a
```

Any plan change produces a new digest. The old digest is not accepted for modified contents. Each invocation acts on one stage only.

## Reference file hashes

These projected output hashes do not imply that any target has been written. For reviewed-report drift, the receipt additionally records the actual observed/computed hashes as described above.

### serialization

| Target | Reference input SHA-256 | Reference output SHA-256 |
|---|---|---|
| `pages/145_scan012.tex` | `09207aeeedb709e590754c3d57e27888de8b02a864e9d3216140cdb91d39b64a` | `f11e6f5eaae5687fb14daab83de366a1acf758f09cabb15ee035a210562004de` |
| `reader_reports/145_scan012_reviewed.json` | `5b1be5dc623edada906d18cda9de027fe453f55545127d5dbe3d205f7bc8c7bc` | `6e6c581b4ab4a33a2b1cd6d92ee048f17f1aecba4d416ed792cea913f5a55a5f` |
| `second/145_scan012_adjudication.json` | `088f8ae04167d29a6f44062c06cb333dee8b2a2e857f599f7ef5c7f042cc736d` | `5042a49acbbfe68120111098fce6b8884bfe6083626fb1827b3fa73e1db29ea9` |
| `pages/145_scan013.tex` | `2310034831c3c556b6d3e73a4705a09dea3ed2ec1c5186b385b9f82165c69ca5` | `9150c90da2a1da8e7b3e5ea6ef0504ec142a0dac9a73a358f709f12aea91d008` |
| `reader_reports/145_scan013_reviewed.json` | `8edb2a8df52ed90868fd73ee4d83affb983a0b0aeb73ce2cf20009c8365d30f5` | `9b3b559d33ac593660537fc9666b33bd8b7bb672a624283e9da56620230488ce` |
| `second/145_scan013_adjudication.json` | `e8a3e92d6e33bdae0e939b48e13bacbe3ec0c386bb1e2891d81751f5607f4d8f` | `59df298a69fc1ae7a252f90db3a0c90a3232a568ca9230231ff7bd8541a19f5a` |
| `pages/145_scan014.tex` | `1ebf61d87d5442562d84bfd712e1d17e5c4cb72d4cab9c0afe9d507c61ba42f9` | `fed6e6a08410645cc3a696c240d6de7c5bf8da657ae2f6acbf1bebb8e5efb89b` |
| `reader_reports/145_scan014_reviewed.json` | `4c4811bf3c2528ab1671f11d14bbf5113376cb01cef11b5c19f927a8bb183d82` | `03a433fecd4d91bea041bf7203d1a238081b02d770070f5ef2f3ec6f6c7c3ee5` |
| `second/145_scan014_adjudication.json` | `25a955a7a15261ce71c2440b2f92742b2a5987f24e25b062f77c770048533c8e` | `84b4e94ff2923eface8870417bb7edcb182db24f56f8e8a0c244a1834bfd88a8` |
| `pages/145_scan015.tex` | `aa4f0dd4382ffccdf0f898c84c1aee7fcf11ba2acb7a325a452dd64dbb115f0b` | `fd0c931adda5b93f52fd21e0ab2ea0730d5899e35373cce2ff71d8cd1d8c41b6` |
| `reader_reports/145_scan015_reviewed.json` | `dcbd5986fee6db9939be5ad04719cc77cb689ba6bd7800197afb184dc4aa7d6a` | `3609ac39e104c74046084ccbc0ae26ac228b54ba7fbbf32ff3e1b99e6dbbc08a` |
| `second/145_scan015_adjudication.json` | `d4d8d095fda53ae723ebcc5cbc63687429a5c85bb25fc7d627a6c8cb34a60a55` | `cd521bc7ce39b3b829be465c3415e065c558f023116f902ac53edebf8b68bf37` |
| `pages/145_scan018.tex` | `8922fd22e4007f3734f3b75182f244b313d725abae9ffd1dfe1b610789a4709a` | `941e538efc1cd9f045c28d84d4a1788417e8d4818bfe97ecb2ccbf566145a2e1` |
| `reader_reports/145_scan018_reviewed.json` | `8b5c0848c4f7f3081ee14fe958473b8190146dc443051679fb7a91883ae7a8c0` | `3023596ede35cdbfc481e6b4c4fb8f57eeb86d33d5c33a482984e90560e158f0` |
| `second/145_scan018_adjudication.json` | `fe449640b5ac1e84a56087f30e5fb9ee22dfd86f84788f188cb1d78366415ff1` | `ac4bfde8f2c64e3bb4c3f9610e52b26cff67adcf79a050a31e8a75da0b50a7a5` |
| `pages/145_scan019.tex` | `115c6c2ae5ed7157dc64843715a6d5b1287638c4beec932ceae9a29f59224582` | `c9399560e111577ae5f93040ef808dba1462513682b48c43d50769797cd8f378` |
| `reader_reports/145_scan019_reviewed.json` | `26386853ae866e4ab3926fc2e0eeaf9f592495619ae82a195babfe70958f6b3f` | `fef1d2ef3a77da08f10a9f58d7904450bf5243eaaf31514270530f5bad897eee` |
| `second/145_scan019_adjudication.json` | `a74375fb5e97818b45101285d699fcc114fb54d715fd05bf464dc9664b1b087c` | `472f8f6211655e529a1573396248784d395dbb73765423a456e628972d6bc113` |

### gamma

| Target | Reference input SHA-256 | Reference output SHA-256 |
|---|---|---|
| `pages/145_scan024.tex` | `6c3df672a4036dd92bb200d68332b7b21720bc0693bb20739dde34bbb4fa4ae8` | `212f61b4ca5dfa5a80a2c7748bb1cbbce6009fc808d1ee08d88fd4631841e887` |
| `reader_reports/145_scan024_reviewed.json` | `ff32ae779b73e2a380758fe704ba46ebf0e5748ffd7965ac8d0d0185c8cff09e` | `451b780838da0f2566328b00672f25c6fa041d4a00a32ce595f8f644f77c1d0f` |
| `second/145_scan024_adjudication.json` | `8d03c4868590ab97f2c329cf33efc775f7e2d4c0b1e78e45a5c6c82553f8487c` | `4b23b85bed970fcbeac61f940894167b1753f4f0add09940bb06f4c7f8d2646f` |

### prime026

| Target | Reference input SHA-256 | Reference output SHA-256 |
|---|---|---|
| `pages/145_scan026.tex` | `6274529774467672879b1fa78b398733ce2b8987fcbcac44791f63e6e5ff4175` | `78b4cf0f9899e56321cc8efbffe3da786f3c2927ea3331935911dcd238cfbcf7` |
| `reader_reports/145_scan026_reviewed.json` | `0378fea2b6186f20189a93891b50821d05503957cb275193f5074348e211e148` | `9f124904eb72222bc97a980d407b76bdcf28732f5e1d6469a815274e2d7911a3` |
| `second/145_scan026_adjudication.json` | `02cfb6539fe07a604e6c6829aff597fddc5f227775740b700f956d042b6a151f` | `3ef2f66093fecfbdf09952cc0c64c629a4bde3d72c41308e5c4de20b562b8329` |

### superscript027

| Target | Reference input SHA-256 | Reference output SHA-256 |
|---|---|---|
| `pages/145_scan027.tex` | `6005f8f6ab5c5b4495c0b8d256f4783535b4dba504d64a5be87998a61206a8a6` | `53322eee4a7d803956ae2893a12f57a67934549c5bc79390f48c0a0ee72b7b26` |
| `reader_reports/145_scan027_reviewed.json` | `d8c709f9d4f11d3ca5b6bab048ad434b90881fc848954fd6966f82f0530af054` | `994bdc291f26da178cdbdb47a177e2afc2c0949b14906f3a15f61137dd34a89b` |
| `second/145_scan027_adjudication.json` | `8f778d391e72405d990565cc01e471aac413de0a4ef451bad144fdd8e3a254c5` | `53026629dee4df3441352432d9cee9c993bc7e55e64861c2ec5d08f5fe339037` |

## Completion state

The final static recheck is complete. The script and exact-field plan are ready for root's review/application. Only staging and review artifacts were written by this task; no proposed page/report/adjudication edit or receipt/progress event has been applied.

