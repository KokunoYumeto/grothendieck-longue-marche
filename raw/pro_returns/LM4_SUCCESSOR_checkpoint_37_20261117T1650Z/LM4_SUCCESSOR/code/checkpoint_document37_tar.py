"""Standard ZIP-LZMA document dictionary for checkpoint37 proposed256MiB policy."""
from contextlib import contextmanager
import lzma
import struct
import zipfile

DOCUMENT37_DICTIONARY_BYTES = 256 * 1024 * 1024


class Document37LZMACompressor(zipfile.LZMACompressor):
    """Keep standard method14 framing; set only the dictionary property."""
    def _init(self):
        props = lzma._encode_filter_properties({
            'id': lzma.FILTER_LZMA1,
            'dict_size': DOCUMENT37_DICTIONARY_BYTES})
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack('<BBH', 9, 4, len(props)) + props


@contextmanager
def standard_document37_dictionary():
    """Scope the document dictionary to one synchronous writestr operation."""
    original = zipfile.LZMACompressor
    zipfile.LZMACompressor = Document37LZMACompressor
    try:
        yield
    finally:
        zipfile.LZMACompressor = original
