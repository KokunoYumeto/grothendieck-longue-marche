"""Standard ZIP-LZMA document dictionary for checkpoint36 and later."""
from contextlib import contextmanager
import lzma
import struct
import zipfile

DOCUMENT_DICTIONARY_BYTES = 128 * 1024 * 1024


class DocumentLZMACompressor(zipfile.LZMACompressor):
    """Keep standard method14 framing; set only the dictionary property."""
    def _init(self):
        props = lzma._encode_filter_properties({
            'id': lzma.FILTER_LZMA1,
            'dict_size': DOCUMENT_DICTIONARY_BYTES})
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack('<BBH', 9, 4, len(props)) + props


@contextmanager
def standard_document_dictionary():
    """Scope the document dictionary to one synchronous writestr operation."""
    original = zipfile.LZMACompressor
    zipfile.LZMACompressor = DocumentLZMACompressor
    try:
        yield
    finally:
        zipfile.LZMACompressor = original
