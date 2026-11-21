# Evidence image encoding

All saved evidence crops are included. They use lossless JPEG XL or the original lossless PNG/WebP, whichever is smaller. Every decoded RGBA pixel was compared with the immutable source image and found identical. Dimensions and pixel hashes are recorded in evidence_encoding.json. No crop was resized, altered, removed, or subjected to text recognition during encoding. Evidence references in audit metadata use the actual archive suffix. Transcription fragments and the original first/second reading and comparison files remain byte-for-byte unchanged; the manifest maps any original evidence filename to its archive filename. Earlier checkpoints were not changed.

JPEG XL images can be decoded to PNG with an FFmpeg build supporting libjxl: `ffmpeg -i input.jxl output.png`. The included script records the precise lossless encoding and raw-pixel comparison procedure.

## Additional lossless coding search

Selected JPEG XL crops were reencoded using the installed libjxl 0.11 expert API with modular previous-channel prediction 11, group size 1024, best modular predictor, and 100% MA-tree learning. Distance remains zero. Each candidate was decoded to RGBA and compared byte for byte with the immutable source PNG; only smaller, identical candidates replaced the default lossless encoding. No image pixel, dimension, crop rectangle or transcription changed. The C shim and exact encoding workflow are included under scripts/compression; lossless_optimization.json records accepted candidates.
