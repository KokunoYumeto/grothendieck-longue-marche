"""Deterministic standard TAR encoding with exact-content hard links.

This is a lossless storage container. Every original logical path remains
in the checkpoint manifest and is restored by an ordinary system tar.
"""
from pathlib import PurePosixPath
import hashlib
import io
import tarfile

PREFIX = 'LM4_SUCCESSOR/'


def build_standard_tar(files):
    files = sorted(files)
    names = [relative for relative, _ in files]
    assert len(names) == len(set(names)), 'Duplicate logical paths'
    stream = io.BytesIO()
    seen = {}
    links = 0
    with tarfile.open(fileobj=stream, mode='w', format=tarfile.PAX_FORMAT) as tf:
        for relative, data in files:
            path = PurePosixPath(relative)
            assert not path.is_absolute() and '..' not in path.parts
            full = PREFIX + relative
            member = tarfile.TarInfo(full)
            member.mode = 0o644
            member.mtime = 0
            key = (len(data), hashlib.sha256(data).hexdigest())
            if key in seen:
                target, previous = seen[key]
                assert previous == data, 'Hash collision'
                member.type = tarfile.LNKTYPE
                member.linkname = target
                member.size = 0
                tf.addfile(member)
                links += 1
            else:
                member.size = len(data)
                tf.addfile(member, io.BytesIO(data))
                seen[key] = (full, data)
    bundle = stream.getvalue()
    return bundle, {
        'paths': len(files),
        'unique_contents': len(seen),
        'standard_tar_hardlinks': links,
        'original_bytes': sum(len(data) for _, data in files),
        'unique_bytes': sum(size for size, _ in seen),
        'bundle_bytes': len(bundle),
        'bundle_sha256': hashlib.sha256(bundle).hexdigest(),
    }
