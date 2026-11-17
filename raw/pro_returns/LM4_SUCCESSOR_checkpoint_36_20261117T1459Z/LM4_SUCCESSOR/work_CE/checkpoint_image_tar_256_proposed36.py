"""Standard ZIP-LZMA image dictionary for checkpoint36 proposed256MiB alternative."""
from contextlib import contextmanager
import lzma
import struct
import zipfile

IMAGE_DICTIONARY_BYTES = 256 * 1024 * 1024


class ImageLZMACompressor(zipfile.LZMACompressor):
    """Keep standard method14 framing; set only the dictionary property."""
    def _init(self):
        props = lzma._encode_filter_properties({
            'id': lzma.FILTER_LZMA1,
            'dict_size': IMAGE_DICTIONARY_BYTES})
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack('<BBH', 9, 4, len(props)) + props


@contextmanager
def standard_image_dictionary():
    """Scope the image dictionary to one synchronous writestr operation."""
    original = zipfile.LZMACompressor
    zipfile.LZMACompressor = ImageLZMACompressor
    try:
        yield
    finally:
        zipfile.LZMACompressor = original
