# Lossless packaging of verification images from checkpoint20 onward

The hourly checkpoint remains one ordinary ZIP holding all current work
and all retained earlier versions. To keep that complete ZIP within the
file-size limit, PNG verification images are grouped in the standard TAR
file `LM4_SUCCESSOR/verification_images.tar` inside the ZIP. Every image
keeps its original relative path and exact bytes. Identical image bytes
at different paths are stored using standard TAR hard-link entries.
No image or earlier version is omitted. PDF deliverables, source files,
code, complete computed data, logs, reports and digest manifests remain
direct ZIP entries.

To restore all image paths after extracting the ZIP, run the following
from the directory containing `LM4_SUCCESSOR/`:

    tar -xf LM4_SUCCESSOR/verification_images.tar

All TAR member names begin with `LM4_SUCCESSOR/`. They contain no absolute
paths, parent traversals or symbolic links. A standard TAR extractor
recreates the image files, including their identical-content hard links.
If independent physical copies are required, a normal file copy after
extraction is sufficient; no custom recovery format is involved.

The per-checkpoint SHA256 manifest names every logical file, including
every image path. The per-checkpoint packaging record separately hashes
the nested TAR. The verifier reads the actual TAR, resolves its standard
hard links, and checks every restored logical file against that manifest
and the prior-version retention index. Earlier checkpoint archives remain
unchanged. The code `checkpoint_archive_io.py` merely provides the same
logical-file view to the future preservation audit.

An exact analysis at checkpoint20 preparation found105120048 redundant
PNG bytes among1495 image paths before the next PDF QA. This is the reason
for the encoding change; the mathematical data and visual evidence are
preserved without lowering image quality.
