# Evidence image encoding

All saved evidence crops are included. They use lossless JPEG XL or the original lossless PNG/WebP, whichever is smaller. Every decoded RGBA pixel was compared with the immutable source image and found identical. Dimensions and pixel hashes are recorded in evidence_encoding.json. No crop was resized, altered, removed, or subjected to text recognition during encoding. Evidence references in audit metadata use the actual archive suffix. Transcription fragments and the original first/second reading and comparison files remain byte-for-byte unchanged; the manifest maps any original evidence filename to its archive filename. Earlier checkpoints were not changed.

JPEG XL images can be decoded to PNG with an FFmpeg build supporting libjxl: `ffmpeg -i input.jxl output.png`. The included script records the precise lossless encoding and raw-pixel comparison procedure.

Selected images use additional lossless frame-option tuning. lossless_tuning_manifest.json identifies their actual archive files. The exact parameter values and C shim are included under scripts/compression. Every source RGBA byte was compared with the decoded cache image in this packaging run.
