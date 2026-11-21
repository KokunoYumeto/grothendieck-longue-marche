# Evidence image encoding

All saved evidence crops are included. They use lossless JPEG XL or lossless WebP, whichever is smaller. Every decoded RGBA pixel was compared with the immutable source image and found identical. Dimensions and pixel hashes are recorded in evidence_encoding.json. No crop was resized, altered, removed, or subjected to text recognition during encoding. Filename references use the actual archive suffix. Earlier checkpoints were not changed.

JPEG XL images can be decoded to PNG with an FFmpeg build supporting libjxl: `ffmpeg -i input.jxl output.png`. The included script records the precise lossless encoding and raw-pixel comparison procedure.
