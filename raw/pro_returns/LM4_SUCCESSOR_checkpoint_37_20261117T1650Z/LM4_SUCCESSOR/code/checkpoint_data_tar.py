"""Exact data selection and a standard ZIP-LZMA dictionary for checkpoint30+."""
from contextlib import contextmanager
from pathlib import PurePosixPath
import lzma
import struct
import zipfile

DATA_BUNDLE = 'LM4_SUCCESSOR/historical_data.tar'
DATA_DICTIONARY_BYTES = 64 * 1024 * 1024


def is_data_bundle_member(relative, size, checkpoint_number=36):
    """Legacy selection through36; lossless solid research storage from37.

    The default deliberately preserves every older caller. Original logical
    paths and bytes remain represented; this predicate only chooses a container.
    Current root deliverables, code, formal sections and the two newly generated
    checkpoint manifests stay direct. Historical versions retain the old rule.
    """
    path = PurePosixPath(relative)
    suffix = path.suffix.lower()
    if suffix in {'.png', '.pdf', '.tar'}:
        return False
    if (relative.startswith('checkpoint_history/') or
            (suffix == '.json' and size >= 1_000_000)):
        return True
    if checkpoint_number < 37:
        return False
    if len(path.parts) == 1 or path.parts[0] in {'code', 'sections'}:
        return False
    if relative in {
            f'records/checkpoint_{checkpoint_number:02d}_contents_sha256.tsv',
            f'records/checkpoint_{checkpoint_number:02d}_packaging.json'}:
        return False
    return True


class DataLZMACompressor(zipfile.LZMACompressor):
    """Same ZIP method14 framing; only the standard dictionary property differs."""
    def _init(self):
        props = lzma._encode_filter_properties({
            'id': lzma.FILTER_LZMA1, 'dict_size': DATA_DICTIONARY_BYTES})
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack('<BBH', 9, 4, len(props)) + props


@contextmanager
def standard_data_dictionary():
    """Scope the dictionary change to one synchronous writestr operation."""
    original = zipfile.LZMACompressor
    zipfile.LZMACompressor = DataLZMACompressor
    try:
        yield
    finally:
        zipfile.LZMACompressor = original
