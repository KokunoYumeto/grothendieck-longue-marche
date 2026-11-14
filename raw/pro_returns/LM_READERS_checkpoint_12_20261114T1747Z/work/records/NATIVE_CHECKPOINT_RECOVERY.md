# Exact native-image recovery in compact checkpoints

This extension changes the storage representation of a progress checkpoint. It does not change manuscript sources, publication PDFs, observations, proof images, or the final publication approval rules. The ordinary final archives retain native proof PNG bytes physically, using exact aliases where appropriate.

## Supported recipe kinds

| Recipe kind | Source and qualification | Exact output rule |
| --- | --- | --- |
| `pymupdf-full-page-rgb-png` | Existing attributed `reviewed` row, its archived ledger, and its exact publication PDF | The original 900-pixel-wide full-page contract is unchanged. |
| `pymupdf-native-rgb-png` | Exact archived JSON record and scalar PDF selector, with the original PNG identity, physical page, scale and clip | PyMuPDF 1.26.6 / MuPDF 1.26.11, RGB, no alpha, annotations included, native PNG writer; both PNG bytes and dimensioned RGB must match. |
| `pillow-unresized-rgb-panels-png` | Exact archived proof-sheet or page-pair record, literal residual canvas, and complete primitive panel references | Pillow 13.0.0, zlib compile/runtime 1.3.2, RGB PNG, compression level 6, no optimization; unresized integer-pixel pastes only. |

The native branch does not require or infer a new visual inspection. It preserves the status and attribution already present in the source metadata. A pending, rejected or historical image remains pending, rejected or historical after recovery.

Supported sheet layouts are the existing two-placement vertical sheets, six-cell sheets with three columns, and native 2.5× page-boundary pairs. The original header and background pixels are stored literally. Recovery does not recreate fonts or captions. Panels may be stored PNGs or direct PDF primitives; a composite may not depend on another composite. Literal canvases remain stored objects.

## Qualification and fallback

The builder considers only PNG hashes already present in the logical checkpoint collection and PDF bytes already retained in that collection. It imports no additional older PDF generation merely to obtain a compression saving. Each source reference is bound to exact packaged metadata bytes and a JSON pointer. Each recipe pins PDF bytes, page geometry, rotation, matrix, clip, engine, PNG byte count and hash, pixel dimensions, and dimensioned RGB hash.

Every candidate is rendered during packaging and compared with the existing PNG. Every sheet is reconstructed and compared with both its complete original PNG encoding and decoded RGB. A mismatch remains a stored original payload and is listed explicitly in the recipe inventory. The initial read-only measurement found one such mismatch, `frapp578_p0072_cube_6x.png`; its full bytes are retained.

Compiler-output privacy projections are a separate, manifest-authorized process. Their raw and portable identities remain explicit in the compiler-output registry. Native-image recovery neither rewrites those observations nor claims that a portable log is a raw-byte copy.

## Independent restoration

The command remains:

```text
python restore_checkpoint.py CHECKPOINT.zip --output-dir restored_checkpoint --verify --report restore_validation.json
```

The archive supplies its own pinned top-level helper. The helper verifies the ordinary physical manifest, complete logical manifest, object and alias identities, metadata references, primitive dependencies, and every reconstructed PNG before writing logical destinations. It refuses path traversal, symlinked destinations, differing existing files, missing dependencies, composite dependency chains, moved or resized panels, engine or encoding changes, and byte or RGB mismatches. It then independently rehashes every restored logical file.

No earlier checkpoint ZIP or original workspace is required. Later generations preserve immutable PDF objects, exact metadata, literal canvases and any auxiliary panel PNGs. Auxiliary panels may themselves be direct PNG recipes; both repeated checkpoint inheritance and final-policy imports resolve only these explicitly qualified primitive dependencies.

The full archive size is measured before creation and checked again afterward. The existing delivery limit remains 536,870,912 bytes. The measured proposal reserved space for a further complete seven-book PDF generation; each real checkpoint still requires its own actual size gate and complete standalone recovery validation.

## Final ordinary delivery

Only the existing attributed 900-pixel publication-raster kind can enter the separate full-page omission policy. Native and composite recipe hashes are protected and retained as physical proof PNGs in the ordinary final archive set. If a protected older native hash is not otherwise present, the final policy recovers and retains those exact bytes.

Recovery-only PDF inputs are excluded from publication only through exact path, byte count, SHA256 and source-qualified development or book provenance. Unknown or ambiguous PDFs block packaging. The final set still contains exactly seven publication PDFs. Language-specific allocation among the final archives is a separate policy and does not alter these bytes or the logical retention inventory.

## Verification evidence

Pre-extension helper bytes, the prior eleven-control report, and its runbook are preserved in `work/layout_probes/checkpoint_native_recovery_v1/before/`. Focused controls are implemented in `work/scripts/check_native_checkpoint_storage.py`; they use temporary synthetic fixtures and create no publication-review claims. The final handoff report records exact code hashes, the control results, fresh real-payload recipe counts, rejected candidates, and the measured compact size. A progress-checkpoint restore is necessary evidence of recoverability, not a substitute for final source, numerical or actual-page review gates.
