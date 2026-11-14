# Revision724 additive local-proof records

## Scope and current state

The new scripts are staged replacements for the proof-record and validation-refresh operations only. At the namespace-correction handoff, root has prepared and checked the additive446-row proof ledger, with no production installation. The validation capture and separate new stress compilation remain unrun. The synthetic control report is `work/layout_probes/revision724_proof_writer_synthetic_controls.json`; it pins the exact tested script bytes and lists the passing positive or rejection controls.

The earlier proposed workflow is preserved under `work/layout_probes/revision724_additive_tool_review_history/pre_namespace_fix/`. Its instruction to rerun the old stress helper is superseded by the separate revision724 workflow below. Neither the old helper nor its files are changed by the new workflow.

`write_visual_repairs_revision724.py` preserves the complete existing `VISUAL_REPAIRS.tsv` byte stream as the prefix of the new table, including its original header and all296 historical rows. It preserves every historical object in `visual_repair_proof_inventory.json`. The expected addition is150 paired-language rows for75 source sites, subject to the exact completed manifest. Superseded source bindings do not remove historical visual proofs.

Each new row retains an OPEN publication status and an empty current-publication evidence list. Its accepted-local-proof object binds the exact manifest, candidate, validation, source bytes, source finding, selection record, actual observation file/key/hash, reviewer and unchanged observation text. Selected PDF/TeX/log files must belong to the same corrected/apparatus after fixture. The selected image is rerendered at its recorded page, clip and scale and must match both PNG bytes and decoded RGB pixels. The structured object is stored in the existing TSV field `publication_closure_inventory_json.accepted_local_proof` and in the new inventory row's `proof_binding`; no historical header rewrite is needed.

Copied new evidence uses content-addressed filenames under `work/visual_repair_proofs`. Development PDFs remain checkpoint evidence and are not added to FINAL. The writer never creates an actual-view observation or closes a publication finding.

## Required order

Run from the project root. Stage directories are exclusive: if one already exists, inspect its report and preserve it; use a new stage name for a new attempt. The commands below are the intended later execution order, not a record that they have run.

1. **Before source integration or stress recompilation**, capture the unchanged724 validation and stress baseline:

   ```sh
   python work/scripts/refresh_layout_validation_revision724.py capture
   ```

2. Once the final accepted manifest exists and all selected actual observations are pinned, prepare and inspect the additive proof table:

   ```sh
   python work/scripts/write_visual_repairs_revision724.py prepare --expected-historical 296 --expected-new 150
   python work/scripts/write_visual_repairs_revision724.py check
   ```

   The default manifest is `work/data/layout_residual_batch_revision724.json`. The default proof stage is `work/layout_probes/revision724_visual_proofs_staged`. Every manifest item must reference selections with exactly the same `(repair_id, language)` set as its candidate. In particular, the editorial40-row batch and the separate V548 two-row batch require separate exact selection subsets; the combined42-row handoff cannot be reused for the40-row manifest item.

3. Root performs the separately audited source integration. Only after `layout_residual_revision724_integration_result.json` reports its exact successful integration may the append be installed:

   ```sh
   python work/scripts/write_visual_repairs_revision724.py commit
   ```

   The commit requires the exact manifest digest, expected active source count and all appended active identities. It creates an exclusive `commit_backup` of both historical ledgers before any replacement. An interrupted commit remains pending and requires recovery from that backup; it is never silently treated as successful.

4. The audited integration finalizer emits six new `tag_pattern_stress_revision724_{fr,en}_{0,1,2}.tex` sources, `tag_pattern_stress_revision724_index.json`, and `tag_binding_replay_revision724_validation.json`. Compile only these separately named sources:

   ```sh
   python work/scripts/refresh_tag_stress_revision724.py compile
   ```

   The helper copies the six new TeX files byte-for-byte into the exclusive `work/layout_probes/tag_pattern_stress_revision724_run/` directory and compiles those copies. Its source index binds each original stress case to the exact current resolved source binding. It checks all60 groups: the constrained page contains only the fixture heading, and the complete source group moves to the following page. Unexpected page counts or attachment failures stop the run.

   The established French diplomatic and English reading coverage requires20 reviewed groups. An earlier actual observation can carry only when the case specimen, exact binding identity, full-page PNG bytes and decoded RGB pixels are all unchanged. A wider resolved binding remains pending even if its rendered pixels happen to match. The other40 groups are explicitly recorded as machine-only fixtures.

   Pending actual-review items and their schema are in `tag_pattern_stress_revision724_run/REVIEW_QUEUE.json`. Actually view both the prepared current full-page image and native3× crop for each pending item, then save the specific attributed observations in a new file and record them:

   ```sh
   python work/scripts/refresh_tag_stress_revision724.py record --observations work/data/NEW_STRESS_ACTUAL_OBSERVATIONS.json
   python work/scripts/refresh_tag_stress_revision724.py check
   ```

   Replace the observation filename with the actual new file. The recorder requires exactly the pending keys, the current PDF hash and both prepared image hashes. It preserves the pre-observation report before adding the supplied records. Do not continue until `tag_pattern_stress_revision724_validation.json` is PASS with no pending actual inspections. The new report is `tag_pattern_stress_revision724_refresh.json`; **no legacy stress source, PDF, log, PNG, index, validation or report is rewritten**.

   Each new compile log is processed with `verify_pdf.sanitize` before its digest is recorded. The verifier requires sanitization to be idempotent, so package delivery cannot silently change the pinned log bytes. New console output is sanitized before saving as well.

5. Stage, check and install the current validation record and new source freeze:

   ```sh
   python work/scripts/refresh_layout_validation_revision724.py prepare
   python work/scripts/refresh_layout_validation_revision724.py check
   python work/scripts/refresh_layout_validation_revision724.py commit
   ```

   The default validation stage is `work/layout_probes/revision724_validation_refresh_staged`. Supply `--proof-stage` and `--stage` consistently if different exclusive directories were chosen. If root has already created the exact new source freeze, pass `--preserve-freeze` to `prepare`; this mode requires the current record count and all eight dependency hashes to match and leaves that freeze byte-for-byte unchanged at commit.

6. Proceed to the frozen seven-book build and the separate current-publication checks. Local-proof acceptance does not replace final selected-page, native finding, pagination, generated-heading, source, margin, privacy or master-transfer gates.

## Historical compatibility

The old `write_visual_repairs.py` rebuilds ledgers from currently active source IDs. It must not be used to refresh this appended history: a superseded binding can disappear from the active lookup even though its actual historical proof must remain.

The new validation refresher copies the previous object and updates current source-audit fields while adding `revision724_residual_accepted_probes` and `revision724_pagination_stress`. It preserves the earlier `current_batch_accepted_probes`, the complete `revision578_residual_accepted_probes`, prior all-form probes and their dependencies exactly. The old `pagination_stress_probes`, `pagination_stress_scope` and `pagination_stress_recompilation` fields also remain exactly unchanged. The new section pins the revision724 source index, replay report, compilation report, complete review validation and current proof artifacts. It records an immutable copy of the previous full validation object.

Downstream current-build reporting must require the new `revision724_pagination_stress.status == PASS` section and its exact current hashes. The preserved legacy stress section is historical evidence, not a substitute for compiling and reviewing the newly emitted sources.

The historical French-diplomatic stress row exposes an existing delivery mismatch: its flat delivered TeX/log copies differ from the source hashes recorded in the validation metadata. The staged refresher does not rewrite that historical record or overwrite those copies. The separate revision724 stress TeX, portable logs and cited images are copied to new content-addressed delivery names with their exact hashes; the historical object remains unchanged and is also available in the captured baseline.

Actual-observation schema adapters are narrow. The typeset record's `physical_page` is treated as the same one-based PDF page as `page`, and conflicting aliases are rejected. The explicit root status `PASS_ACTUAL_NATIVE_VISUAL_REVIEW` is accepted alongside the other recorded actual-pass statuses. Reviewers, observation text, source identities and image geometry are not synthesized or rewritten.

## Evidence and limits

The new writers use exclusive backups and commit journals. The proof commit record is at `<proof-stage>/COMMIT.json`; the validation commit record is at `<validation-stage>/COMMIT.json`. Each pins its plan, inputs and resulting outputs. Repeating a successful commit checks the pinned outputs and evidence; a failed or partial journal blocks a silent retry.

The scripts preserve historical publication traces exactly, even where those traces name an earlier PDF revision. They make no claim that an earlier publication page number or hash describes the forthcoming build. Any explicit later publication-trace/status refresh belongs to the separately validated final-closure operation.
