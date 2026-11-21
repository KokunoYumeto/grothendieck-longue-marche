"""Lossless PNG encoding probe; no manuscript interpretation or source mutation."""
import ctypes
import struct
import zlib
import io
import numpy as np
from PIL import Image

PNG = ctypes.CDLL('/lib/libzopflipng.so.1')
PNG.CZopfliPNGSetDefaults.argtypes = [ctypes.c_void_p]
PNG.CZopfliPNGSetDefaults.restype = None
PNG.CZopfliPNGOptimize.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_size_t)]
PNG.CZopfliPNGOptimize.restype = ctypes.c_int
C = ctypes.CDLL(None)
C.free.argtypes = [ctypes.c_void_p]
C.free.restype = None
D = ctypes.CDLL('libdeflate.so.0')
D.libdeflate_alloc_compressor.argtypes = [ctypes.c_int]
D.libdeflate_alloc_compressor.restype = ctypes.c_void_p
D.libdeflate_free_compressor.argtypes = [ctypes.c_void_p]
D.libdeflate_zlib_compress_bound.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
D.libdeflate_zlib_compress_bound.restype = ctypes.c_size_t
D.libdeflate_zlib_compress.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t]
D.libdeflate_zlib_compress.restype = ctypes.c_size_t


def optimize(data, strong=False, strategy=None, iterations=None):
    options = ctypes.create_string_buffer(256)
    PNG.CZopfliPNGSetDefaults(options)
    assert struct.unpack_from('i', options, 0)[0] == 0
    assert struct.unpack_from('i', options, 4)[0] == 0
    struct.pack_into('i', options, 36, int(strong))
    if strategy is not None:
        strategies = (ctypes.c_int * 1)(strategy)
        ctypes.c_void_p.from_buffer(options, 8).value = ctypes.addressof(strategies)
        struct.pack_into('i', options, 16, 1)
        struct.pack_into('i', options, 20, 0)
    if iterations is not None:
        struct.pack_into('i', options, 40, iterations)
        struct.pack_into('i', options, 44, iterations)
    src = ctypes.create_string_buffer(data)
    output = ctypes.c_void_p()
    length = ctypes.c_size_t()
    error = PNG.CZopfliPNGOptimize(src, len(data), options, 0, ctypes.byref(output), ctypes.byref(length))
    if error:
        raise RuntimeError(('CZopfliPNGOptimize', error))
    result = ctypes.string_at(output, length.value)
    C.free(output)
    return result


def chunks(data):
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    at = 8
    while at < len(data):
        n = struct.unpack_from('>I', data, at)[0]
        kind = data[at+4:at+8]
        payload = data[at+8:at+8+n]
        assert zlib.crc32(kind+payload) & 0xffffffff == struct.unpack_from('>I', data, at+8+n)[0]
        yield kind, payload, data[at:at+12+n]
        at += 12+n
    assert at == len(data)


def compress_zlib(raw, level=12):
    comp = D.libdeflate_alloc_compressor(level)
    if not comp:
        raise MemoryError('libdeflate compressor')
    bound = D.libdeflate_zlib_compress_bound(comp, len(raw))
    src = ctypes.create_string_buffer(raw)
    dest = ctypes.create_string_buffer(bound)
    n = D.libdeflate_zlib_compress(comp, src, len(raw), dest, bound)
    D.libdeflate_free_compressor(comp)
    if not n:
        raise RuntimeError('libdeflate compression failed')
    encoded = dest.raw[:n]
    assert zlib.decompress(encoded) == raw
    return encoded


def replace_idat(data, encoded, new_ihdr=None):
    cs = list(chunks(data))
    n = len(encoded)
    idat = struct.pack('>I', n)+b'IDAT'+encoded+struct.pack('>I', zlib.crc32(b'IDAT'+encoded)&0xffffffff)
    result = bytearray(data[:8])
    wrote = False
    for kind,payload,whole in cs:
        if kind == b'IDAT':
            if not wrote:
                result.extend(idat)
                wrote = True
        elif kind == b'IHDR' and new_ihdr is not None:
            result.extend(struct.pack('>I',len(new_ihdr))+b'IHDR'+new_ihdr+struct.pack('>I',zlib.crc32(b'IHDR'+new_ihdr)&0xffffffff))
        else:
            result.extend(whole)
    return bytes(result)


def recompress_idat(data, level=12):
    cs = list(chunks(data))
    raw = zlib.decompress(b''.join(payload for kind,payload,_ in cs if kind == b'IDAT'))
    return replace_idat(data, compress_zlib(raw,level))


def encode_fixed(data, strategy=2, level=12):
    cs=list(chunks(data))
    ihdr=next(payload for kind,payload,_ in cs if kind==b'IHDR')
    width,height,depth,color,compression,filter_method,interlace=struct.unpack('>IIBBBBB',ihdr)
    if depth!=8 or color not in (0,2) or interlace!=0:
        raise ValueError('Only noninterlaced 8-bit grayscale/RGB supported')
    with Image.open(io.BytesIO(data)) as im:
        arr=np.array(im)
    new_ihdr=None
    if color==2 and all(kind in (b'IHDR',b'IDAT',b'IEND') for kind,_,_ in cs):
        if np.array_equal(arr[:,:,0],arr[:,:,1]) and np.array_equal(arr[:,:,1],arr[:,:,2]):
            arr=arr[:,:,0].copy();color=0
            new_ihdr=struct.pack('>IIBBBBB',width,height,8,0,0,0,0)
    bpp=1 if color==0 else 3
    rows=arr.reshape(height,width*bpp)
    filtered=np.empty((height,rows.shape[1]+1),dtype=np.uint8)
    filtered[:,0]=strategy
    if strategy==0:
        filtered[:,1:]=rows
    elif strategy==2:
        filtered[0,1:]=rows[0]
        np.subtract(rows[1:],rows[:-1],out=filtered[1:,1:])
    else:
        a=np.zeros_like(rows,dtype=np.int16);a[:,bpp:]=rows[:,:-bpp]
        if strategy==1:
            predictor=a
        else:
            b=np.zeros_like(rows,dtype=np.int16);b[1:]=rows[:-1]
            if strategy==3:
                predictor=(a+b)//2
            elif strategy==4:
                c=np.zeros_like(rows,dtype=np.int16);c[1:,bpp:]=rows[:-1,:-bpp]
                p=a+b-c;pa=np.abs(p-a);pb=np.abs(p-b);pc=np.abs(p-c)
                predictor=np.where((pa<=pb)&(pa<=pc),a,np.where(pb<=pc,b,c))
            else: raise ValueError(strategy)
        filtered[:,1:]=(rows.astype(np.int16)-predictor).astype(np.uint8)
    return replace_idat(data,compress_zlib(filtered.tobytes(),level),new_ihdr)
