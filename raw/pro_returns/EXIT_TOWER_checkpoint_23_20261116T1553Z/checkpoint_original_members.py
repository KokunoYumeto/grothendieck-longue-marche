#!/usr/bin/env python3
"""Read exact original members while verifying every explicitly carried raw blob."""
from pathlib import Path
import argparse,hashlib,json,lzma,re,sys,tarfile,zipfile
import checkpoint_original_members_base as base
POLICY='all-carried-raw-integrity-v1'
legacy_record_of=base.record_of
legacy_iter_original_members=base.iter_original_members
digest=base.digest
safe=base.safe

def record_of(archive):
    record=legacy_record_of(archive)
    if record is None:return None
    policy=record.get('carried_blob_policy')
    if policy is None:
        if 'carried_original_integrity' in record or 'unreferenced_blobs' in record:
            raise ValueError('Unversioned carried-blob metadata')
        return record
    if policy!=POLICY:raise ValueError('Unknown carried-blob policy')
    def unique(pairs):
        result={}
        for k,v in pairs:
            if k in result:raise ValueError('Duplicate manifest key')
            result[k]=v
        return result
    record=json.loads(archive.read('CHECKPOINT_RESUME.json'),object_pairs_hook=unique)
    chunks=[x['name'] for x in record['chunks']]
    runtime=set(record['runtime_hashes']);fixed={'CHECKPOINT_RESUME.json','READ_ME_FIRST.txt'}
    if len(chunks)!=len(set(chunks)) or set(chunks)&(runtime|fixed) or runtime&fixed:
        raise ValueError('Overlapping wrapper entry roles')
    if set(archive.namelist())!=set(chunks)|runtime|fixed:raise ValueError('Unexpected wrapper entry')
    if archive.comment:raise ValueError('Unexpected ZIP comment')
    here=archive.fp.tell();archive.fp.seek(-22,2);tail=archive.fp.read(22);archive.fp.seek(here)
    if tail[:4]!=b'PK\x05\x06' or tail[-2:]!=b'\0\0':raise ValueError('Trailing ZIP data')
    return record

class SingleXZ:
    """Bounded decompression of exactly one XZ stream, without ignored suffixes."""
    def __init__(self,source):
        self.source=source;self.decoder=lzma.LZMADecompressor(format=lzma.FORMAT_XZ);self.done=False
    def read(self,n):
        if n<0:raise ValueError('A bounded XZ read is required')
        result=bytearray()
        while len(result)<n and not self.done:
            if self.decoder.needs_input:
                packed=self.source.read(65536)
                if not packed:raise EOFError('Incomplete XZ stream')
            else:packed=b''
            result.extend(self.decoder.decompress(packed,max_length=n-len(result)))
            if self.decoder.eof:
                if self.decoder.unused_data or self.source.read(1):raise ValueError('Trailing compressed data')
                self.done=True
        return bytes(result)

def exact_read(stream,n):
    result=bytearray()
    while len(result)<n:
        data=stream.read(n-len(result))
        if not data:raise EOFError('Incomplete canonical encoded member')
        result.extend(data)
    return bytes(result)

def carried_encoded_members(archive,record):
    seen=set()
    for chunk in record['chunks']:
        safe(chunk['name']);info=archive.getinfo(chunk['name'])
        if info.file_size!=chunk['bytes']:raise ValueError('Wrapped chunk length differs')
        with archive.open(info) as source:
            counted=base.Counted(source);decoded=SingleXZ(counted);offset=0
            for name in chunk['blobs']:
                safe(name)
                if name in seen or name not in record['blobs']:raise ValueError('Repeated or unknown encoded blob')
                desc=record['blobs'][name];n=desc['encoded_bytes']
                if type(n) is not int or n<0:raise ValueError('Invalid encoded length')
                item=tarfile.TarInfo(name);item.size=n;header=item.tobuf(format=tarfile.PAX_FORMAT)
                if exact_read(decoded,len(header))!=header:raise ValueError('Canonical encoded header differs')
                data=exact_read(decoded,n);padding=(-n)%512
                if exact_read(decoded,padding)!=b'\0'*padding:raise ValueError('Encoded member padding differs')
                if hashlib.sha256(data).hexdigest()!=desc['encoded_sha256']:raise ValueError('Encoded member integrity differs')
                offset+=len(header)+n+padding;seen.add(name);yield name,desc,data
            tail=1024+(-(offset+1024))%tarfile.RECORDSIZE
            if exact_read(decoded,tail)!=b'\0'*tail:raise ValueError('Canonical tar terminator differs')
            if decoded.read(1):raise ValueError('Trailing encoded tar data')
            if counted.n!=chunk['bytes'] or counted.h.hexdigest()!=chunk['sha256']:
                raise ValueError('Compressed chunk integrity differs')
    if seen!=set(record['blobs']):raise ValueError('Missing encoded blob')

def iter_original_members(path):
    with zipfile.ZipFile(path) as archive:
        record=record_of(archive)
        if record is None or record.get('carried_blob_policy') is None:
            yield from legacy_iter_original_members(path);return
        for name,expected in record['runtime_hashes'].items():
            safe(name)
            if hashlib.sha256(archive.read(name)).hexdigest()!=expected:raise ValueError('Embedded runtime checksum differs')
        by_blob={}
        for name,desc in record['members'].items():
            safe(name);by_blob.setdefault(desc['blob'],[]).append((name,desc))
        pins=record['carried_original_integrity'];all_blobs=set(record['blobs'])
        if not set(by_blob)<=all_blobs or set(pins)!=all_blobs:raise ValueError('Carried original integrity domain differs')
        if record['unreferenced_blobs']!=sorted(all_blobs-set(by_blob)):raise ValueError('Unreferenced blob partition differs')
        if record.get('committed_blobs')!=len(all_blobs):raise ValueError('Committed blob count differs')
        for pin in pins.values():
            if set(pin)!= {'bytes','sha256'} or type(pin['bytes']) is not int or pin['bytes']<0 or not re.fullmatch('[0-9a-f]{64}',pin['sha256']):
                raise ValueError('Invalid carried original integrity pin')
        from png_private_compressed_rows import Decoder
        from png_exact_preconditioning import restore as restore_png
        from pdf_exact_preconditioning import restore as restore_pdf
        from png_exact_parameters import library,restore as restore_parameter_png
        restored=0;lib=library()
        with Decoder(':memory:') as rows:
            for name,desc,encoded in carried_encoded_members(archive,record):
                codec=desc['codec']
                if codec=='original':raw=encoded
                elif codec=='png-disk-rows-v2':raw=restore_png(rows.decode(encoded))
                elif codec=='png-idat-v1':raw=restore_png(encoded)
                elif codec=='pdf-zlib-v1':raw=restore_pdf(encoded)
                elif codec=='png-exact-parameters-v1':raw=restore_parameter_png(encoded,lib)
                else:raise ValueError('Unknown exact codec')
                h=hashlib.sha256(raw).hexdigest();pin=pins[name]
                if len(raw)!=pin['bytes'] or h!=pin['sha256']:raise ValueError('Carried original blob integrity differs: '+name)
                for original,expected in by_blob.get(name,[]):
                    if len(raw)!=expected['bytes'] or h!=expected['sha256']:raise ValueError('Original member integrity differs: '+original)
                    restored+=1;yield original,raw
            if rows.count!=record['row_count'] or rows.blocks!=record['row_blocks']:raise ValueError('Original row stream counters differ')
        if restored!=len(record['members']):raise ValueError('Original member omitted')

# The verified original comparison, restoration and tar-stream code is unchanged.
base.record_of=record_of
base.iter_original_members=iter_original_members
verify=base.verify
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('wrapper',type=Path)
    p.add_argument('--verify-only',action='store_true');p.add_argument('--compare-source',type=Path)
    p.add_argument('--compare-tree',type=Path);p.add_argument('--destination',type=Path);p.add_argument('--members-tar',action='store_true')
    a=p.parse_args()
    if a.verify_only and a.destination:p.error('Choose verification or restoration')
    result=verify(a.wrapper,a.compare_source,a.compare_tree,a.destination,a.members_tar)
    print(json.dumps(result,indent=2),file=sys.stderr if a.members_tar else sys.stdout,flush=True)
