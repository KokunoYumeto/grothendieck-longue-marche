#!/usr/bin/env python3
"""Exact optional PNG IDAT preparation with recorded deflate parameters.

The original PNG is accepted only after the pinned library recreates its
entire original IDAT stream. Every chunk, IDAT split and file byte is then
reconstructed and verified. Existing PNG codecs and runtimes are unchanged.
"""
from pathlib import Path
import base64,ctypes,hashlib,json,struct,zlib

MAGIC=b'EXITPNGPAR1\x00'
SIGNATURE=b'\x89PNG\r\n\x1a\n'
LIB_SHA='85590dd58edf5445e18bc7193e5ebc01ac5841f1ae187e97705a662e90c6421e'
class Stream(ctypes.Structure):
    _fields_=[('next_in',ctypes.c_void_p),('avail_in',ctypes.c_uint),('total_in',ctypes.c_ulong),
              ('next_out',ctypes.c_void_p),('avail_out',ctypes.c_uint),('total_out',ctypes.c_ulong),
              ('msg',ctypes.c_char_p),('state',ctypes.c_void_p),('zalloc',ctypes.c_void_p),
              ('zfree',ctypes.c_void_p),('opaque',ctypes.c_void_p),('data_type',ctypes.c_int),
              ('adler',ctypes.c_ulong),('reserved',ctypes.c_ulong)]

def library(directory=None):
    path=(Path(directory) if directory else Path(__file__).parent/'recovery_runtime')/'libz.so.1.3.1'
    if hashlib.sha256(path.read_bytes()).hexdigest()!=LIB_SHA:raise ValueError('Pinned deflate library differs')
    lib=ctypes.CDLL(str(path));lib.zlibVersion.restype=ctypes.c_char_p
    lib.deflateInit2_.argtypes=[ctypes.POINTER(Stream),ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_char_p,ctypes.c_int]
    lib.deflateInit2_.restype=ctypes.c_int
    lib.deflateBound.argtypes=[ctypes.POINTER(Stream),ctypes.c_ulong];lib.deflateBound.restype=ctypes.c_ulong
    lib.deflate.argtypes=[ctypes.POINTER(Stream),ctypes.c_int];lib.deflate.restype=ctypes.c_int
    lib.deflateEnd.argtypes=[ctypes.POINTER(Stream)];lib.deflateEnd.restype=ctypes.c_int
    if lib.zlibVersion()!=b'1.3.1':raise ValueError('Pinned zlib version differs')
    return lib

def compress(raw,parameters,lib):
    level,window,memory,strategy=parameters
    if not (0<=level<=9 and 9<=window<=15 and 1<=memory<=9 and 0<=strategy<=4):
        raise ValueError('Invalid recorded deflate parameters')
    if len(raw)>1<<30:raise ValueError('Prepared PNG exceeds bounded deflate size')
    state=Stream()
    if lib.deflateInit2_(ctypes.byref(state),level,8,window,memory,strategy,b'1.3.1',ctypes.sizeof(Stream)):
        raise ValueError('Pinned deflate initialization failed')
    try:
        bound=lib.deflateBound(ctypes.byref(state),len(raw))
        if bound>=1<<32:raise ValueError('Pinned output exceeds deflate buffer range')
        target=ctypes.create_string_buffer(bound);source=ctypes.create_string_buffer(raw)
        state.next_in=ctypes.addressof(source);state.avail_in=len(raw)
        state.next_out=ctypes.addressof(target);state.avail_out=bound
        if lib.deflate(ctypes.byref(state),4)!=1:raise ValueError('Pinned deflate did not finish')
        return target.raw[:state.total_out]
    finally:
        if lib.deflateEnd(ctypes.byref(state)):raise ValueError('Pinned deflate cleanup failed')

def parse_png(data):
    if not data.startswith(SIGNATURE):raise ValueError('Unknown PNG signature')
    pos=8;chunks=[];parts=[];ended=False
    while pos<len(data):
        if len(data)-pos<12:raise ValueError('Truncated PNG chunk')
        size=struct.unpack_from('>I',data,pos)[0];chunk=data[pos:pos+size+12]
        if len(chunk)!=size+12:raise ValueError('Truncated PNG chunk body')
        if zlib.crc32(chunk[4:-4])&0xffffffff!=struct.unpack('>I',chunk[-4:])[0]:raise ValueError('PNG CRC differs')
        if chunk[4:8]==b'IDAT':chunks.append({'IDAT_bytes':size});parts.append(chunk[8:-4])
        else:chunks.append({'original_chunk':base64.b64encode(chunk).decode('ascii')})
        pos+=len(chunk)
        if chunk[4:8]==b'IEND':ended=True;break
    if not ended or pos!=len(data) or not parts:raise ValueError('Incomplete PNG')
    stream=b''.join(parts);decoder=zlib.decompressobj();raw=decoder.decompress(stream,1<<30)
    if not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:raise ValueError('Original PNG deflate framing differs')
    return chunks,stream,raw

def prepare(data,lib,parameters=(6,15,9,1)):
    try:chunks,stream,raw=parse_png(data)
    except (ValueError,zlib.error):return None
    candidate=compress(raw,parameters,lib)
    if candidate!=stream:return None
    meta={'version':1,'parameters':list(parameters),'library_sha256':LIB_SHA,'pinned_zlib_version':'1.3.1',
          'raw_bytes':len(raw),'original_bytes':len(data),'original_sha256':hashlib.sha256(data).hexdigest(),
          'stream_sha256':hashlib.sha256(stream).hexdigest(),'chunks':chunks}
    prefix=json.dumps(meta,separators=(',',':')).encode()
    encoded=MAGIC+struct.pack('>I',len(prefix))+prefix+raw
    if restore(encoded,lib)!=data:raise ValueError('New exact preparation failed its literal inverse')
    return encoded,meta

def restore(encoded,lib):
    if not encoded.startswith(MAGIC) or len(encoded)<len(MAGIC)+4:raise ValueError('Unknown parameter PNG codec')
    pos=len(MAGIC);size=struct.unpack_from('>I',encoded,pos)[0];pos+=4
    if size>len(encoded)-pos:raise ValueError('Truncated parameter metadata')
    meta=json.loads(encoded[pos:pos+size]);raw=encoded[pos+size:]
    if meta['version']!=1 or meta['library_sha256']!=LIB_SHA or meta['pinned_zlib_version']!='1.3.1':raise ValueError('Parameter PNG version differs')
    if len(raw)!=meta['raw_bytes']:raise ValueError('Prepared filtered data length differs')
    stream=compress(raw,tuple(meta['parameters']),lib)
    if hashlib.sha256(stream).hexdigest()!=meta['stream_sha256']:raise ValueError('Original deflate stream checksum differs')
    out=bytearray(SIGNATURE);at=0
    for entry in meta['chunks']:
        if 'IDAT_bytes' in entry:
            n=entry['IDAT_bytes']
            if not isinstance(n,int) or n<0 or at+n>len(stream):raise ValueError('Invalid original IDAT boundary')
            body=stream[at:at+n];at+=n
            out+=struct.pack('>I',n)+b'IDAT'+body+struct.pack('>I',zlib.crc32(b'IDAT'+body)&0xffffffff)
        else:
            chunk=base64.b64decode(entry['original_chunk'],validate=True)
            if len(chunk)<12 or struct.unpack_from('>I',chunk)[0]+12!=len(chunk):raise ValueError('Invalid original PNG chunk')
            if zlib.crc32(chunk[4:-4])&0xffffffff!=struct.unpack('>I',chunk[-4:])[0]:raise ValueError('Original chunk CRC differs')
            out+=chunk
    result=bytes(out)
    if at!=len(stream) or len(result)!=meta['original_bytes'] or hashlib.sha256(result).hexdigest()!=meta['original_sha256']:
        raise ValueError('Restored original PNG checksum differs')
    return result
