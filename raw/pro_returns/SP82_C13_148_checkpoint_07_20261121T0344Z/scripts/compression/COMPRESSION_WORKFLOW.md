# Lossless evidence encoding optimization

The complete checkpoint06 ZIP initially exceeded the available transfer gateway's 536,870,912-byte limit. No crop, document, reading, diagram, or image pixel was removed to meet that limit. The optimization changes only the lossless entropy/prediction coding of selected JPEG XL images.

## Inputs and immutability

- `work/checkpoint06_source` is the immutable full snapshot containing the original saved PNG/WebP evidence.
- `work/checkpoint06_jxl/stage` is the previously validated, complete lossless JPEG XL stage.
- `work/checkpoint06_jxl/SP82_C13_148_checkpoint_06.zip` remains untouched.
- A new full stage and ZIP are built in `work/checkpoint06_optimized`.
- Existing JPEG files are copied unchanged. Transcription fragments and locked first/second/comparison/token-difference TSVs remain byte-for-byte identical.

## Encoding

The installed libjxl 0.11.2 exposes more lossless controls than the installed FFmpeg command line exposes directly. The included C shim forwards FFmpeg's normal encoder calls to the same installed libjxl, then supplies these frame settings immediately before image submission:

| API option | Value | Role |
|---|---:|---|
| 29 | 11 | Modular previous-channel context |
| 26 | 3 | Modular group size selection |
| 27 | 15 | Modular predictor selection |
| 28 (float API) | 25 or 100 | MA-tree learning percentage, recorded per candidate |

The baseline FFmpeg settings remain `-distance 0 -effort 9`. The shim's optional higher-effort test facility was investigated but is not used for the adopted encoding. The shim enables the library's exported expert-option entry point; no encoder source binary is edited.

Compile the shim from its included source:

```sh
cc -shared -fPIC -O2 -o jxl_tune2_shim.so jxl_effort_shim.c -ldl
```

An individual encoding follows this form, with absolute paths substituted:

```sh
EVIDENCE_JXL_TUNE=29:11,26:3,27:15,28:100 \
LD_PRELOAD=/absolute/path/jxl_tune2_shim.so \
ffmpeg -v error -nostdin -n -i input.png -c:v libjxl \
  -distance 0 -effort 9 -frames:v 1 -threads 2 output.jxl
```

## Verification and selection

For each candidate, the saved source image is decoded by Pillow and converted to RGBA bytes. The candidate JPEG XL is decoded by FFmpeg to raw RGBA bytes. The entire byte strings must be equal. The SHA-256 of the RGBA byte string is the cache key and is recorded with dimensions in the evidence encoding manifest. A candidate is used only when that equality holds and its file is smaller than the previous encoding. No resize, contrast adjustment, sharpening, cropping, rotation, OCR, or other change occurs during this encoding search.

`lossless_optimization.json` records each attempted crop, before and after sizes, source pixel hash, chosen parameters, and successful pixel comparison. The complete archive is checked for a valid ZIP CRC and all expected files. Locked transcription and blind-reading files are compared byte for byte with the prior stage before packaging.

## Reusing the results

`build_best_cache.py` creates `work/jxl_best_evidence_cache` from the smallest verified encoding for each pixel hash. It copies files atomically, preserving both the default cache and the tuned cache. Later invocations of the existing `reencode_snapshot_jxl.py` can use this best cache as their cache argument; that script again checks every decoded pixel against the then-current immutable snapshot. Larger subsequent snapshots can therefore reuse the smaller files while preserving their own full inventory.

## Later scheduling adjustment

After checkpoint06, 25% MA-tree learning was also used to reduce encoding time. A comparison on a fixed representative crop gave 236,734 bytes at25% and233,703 at100%, against252,168 for the default encoding; all decoded pixels were identical. The lower training fraction changes the compression model, not the image. The accepted parameter string is recorded for each candidate and each tuned archive image. Completed100% candidates are retained when they are smaller; no earlier checkpoint is modified.

For later complete ZIPs, already compressed image files are stored directly as standard ZIP entries, while text and code use ZIP Deflate. This avoids spending time recompressing high-entropy image streams and preserves their bytes exactly.
