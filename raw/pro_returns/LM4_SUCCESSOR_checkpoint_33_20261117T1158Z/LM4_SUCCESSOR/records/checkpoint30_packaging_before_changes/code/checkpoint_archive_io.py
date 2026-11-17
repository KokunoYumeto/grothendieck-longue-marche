"""Read ordinary checkpoint ZIPs and ZIPs with standard TAR bundles.

The optional nested TAR is a storage encoding only: its members, including
standard hard links, are exposed as their original full logical paths.
The current main PDF, sources, data files and manifests remain direct ZIP
entries. From checkpoint24, historical and preview PDFs use a second TAR.
"""
from pathlib import PurePosixPath
import io
import tarfile
import zipfile

PREFIX = 'LM4_SUCCESSOR/'
IMAGE_BUNDLE = PREFIX + 'verification_images.tar'
DOCUMENT_BUNDLE = PREFIX + 'historical_documents.tar'

class CheckpointReader:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        self.tar = None
        self.tar_bytes = None
        self.members = {}
        self.document_tar = None
        self.document_tar_bytes = None
        self.document_members = {}
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
        if DOCUMENT_BUNDLE in self.direct:
            self.document_tar_bytes = self.z.read(DOCUMENT_BUNDLE)
            self.document_tar = tarfile.open(fileobj=io.BytesIO(self.document_tar_bytes), mode='r:')
            for member in self.document_tar.getmembers():
                name = member.name
                parts = PurePosixPath(name).parts
                assert parts and parts[0] == 'LM4_SUCCESSOR' and '..' not in parts
                assert not PurePosixPath(name).is_absolute()
                assert member.isfile() or member.islnk(), ('Unexpected document TAR entry', name)
                assert name not in self.document_members and name not in self.members and name not in self.direct
                if member.islnk():
                    assert member.linkname in self.document_members, ('Forward or absent document hardlink', name)
                    assert self.document_members[member.linkname].isfile(), ('Nested document hardlink', name)
                self.document_members[name] = member
        self.logical = [n for n in self.direct if n not in {IMAGE_BUNDLE,DOCUMENT_BUNDLE}] + list(self.members) + list(self.document_members)
        assert len(self.logical) == len(set(self.logical))

    def names(self):
        return self.logical

    def read(self, name):
        if name in self.members:
            stream = self.tar.extractfile(self.members[name])
            assert stream is not None
            return stream.read()
        if name in self.document_members:
            stream = self.document_tar.extractfile(self.document_members[name])
            assert stream is not None
            return stream.read()
        return self.z.read(name)

    def testzip(self):
        return self.z.testzip()

    def close(self):
        if self.tar is not None:
            self.tar.close()
        if self.document_tar is not None:
            self.document_tar.close()
        self.z.close()
        self.tar_bytes = None
        self.document_tar_bytes = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
