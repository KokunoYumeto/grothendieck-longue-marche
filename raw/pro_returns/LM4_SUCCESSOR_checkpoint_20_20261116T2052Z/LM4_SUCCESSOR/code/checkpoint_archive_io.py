"""Read ordinary checkpoint ZIPs and ZIPs with a standard TAR image bundle.

The optional nested TAR is a storage encoding only: its members, including
standard hard links, are exposed as their original full logical paths.
Every PDF, source, data file and manifest remains a direct ZIP entry.
"""
from pathlib import PurePosixPath
import io
import tarfile
import zipfile

PREFIX = 'LM4_SUCCESSOR/'
IMAGE_BUNDLE = PREFIX + 'verification_images.tar'

class CheckpointReader:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        self.tar = None
        self.tar_bytes = None
        self.members = {}
        self.direct = [e.filename for e in self.z.infolist() if not e.is_dir()]
        assert len(self.direct) == len(set(self.direct)), 'Duplicate ZIP names'
        if IMAGE_BUNDLE in self.direct:
            self.tar_bytes = self.z.read(IMAGE_BUNDLE)
            self.tar = tarfile.open(fileobj=io.BytesIO(self.tar_bytes), mode='r:')
            for member in self.tar.getmembers():
                name = member.name
                parts = PurePosixPath(name).parts
                assert parts and parts[0] == 'LM4_SUCCESSOR' and '..' not in parts
                assert not PurePosixPath(name).is_absolute()
                assert member.isfile() or member.islnk(), ('Unexpected TAR entry', name)
                assert name not in self.members and name not in self.direct
                if member.islnk():
                    assert member.linkname in self.members, ('Forward or absent hardlink', name)
                    assert self.members[member.linkname].isfile(), ('Nested hardlink', name)
                self.members[name] = member
        self.logical = [n for n in self.direct if n != IMAGE_BUNDLE] + list(self.members)
        assert len(self.logical) == len(set(self.logical))

    def names(self):
        return self.logical

    def read(self, name):
        if name in self.members:
            stream = self.tar.extractfile(self.members[name])
            assert stream is not None
            return stream.read()
        return self.z.read(name)

    def testzip(self):
        return self.z.testzip()

    def close(self):
        if self.tar is not None:
            self.tar.close()
        self.z.close()
        self.tar_bytes = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
