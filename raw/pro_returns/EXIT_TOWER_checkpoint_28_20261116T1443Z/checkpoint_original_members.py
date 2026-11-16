#!/usr/bin/env python3
"""Stream and verify original members of raw or complete portable checkpoints."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,io,json,lzma,os,sys,tarfile,zipfile
sys.dont_write_bytecode=True
runtime=Path(__file__).resolve().parent/'runtime'
if runtime.is_dir():sys.path.insert(0,str(runtime))

def digest(path):
    with Path(path).open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def safe(name):
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or not p.parts:raise ValueError('Unsafe original path')
    return Path(*p.parts)
def record_of(archive):
    names=archive.namelist()
    if len(names)!=len(set(names)):raise ValueError('Duplicate ZIP entry')
    if 'CHECKPOINT_RESUME.json' not in names:return None
    record=json.loads(archive.read('CHECKPOINT_RESUME.json'))
    if record.get('encoding_version')!=3 or not record.get('complete'):raise ValueError('Incomplete portable checkpoint')
    return record
class Counted:
    def __init__(self,raw):self.raw=raw;self.h=hashlib.sha256();self.n=0
    def read(self,n=-1):
        data=self.raw.read(n);self.h.update(data);self.n+=len(data);return data
    def tell(self):return self.n
    def readable(self):return True
    def seekable(self):return False
def encoded_members(archive,record):
    seen=set()
    for chunk in record['chunks']:
        safe(chunk['name']);info=archive.getinfo(chunk['name'])
        if info.file_size!=chunk['bytes']:raise ValueError('Wrapped chunk length differs')
        names=[]
        with archive.open(info) as source:
            counted=Counted(source)
            with lzma.LZMAFile(counted,'rb') as decoded:
                with tarfile.open(fileobj=decoded,mode='r|') as tar:
                    for item in tar:
                        if not item.isfile() or item.name in seen or item.name not in record['blobs']:
                            raise ValueError('Unexpected encoded member')
                        desc=record['blobs'][item.name];data=tar.extractfile(item).read()
                        if len(data)!=item.size or len(data)!=desc['encoded_bytes'] or hashlib.sha256(data).hexdigest()!=desc['encoded_sha256']:
                            raise ValueError('Encoded member bytes differ')
                        names.append(item.name);seen.add(item.name);yield item.name,desc,data
                for tail in iter(lambda:decoded.read(1024*1024),b''):
                    if any(tail):raise ValueError('Nonzero encoded tar tail')
            if source.read(1):raise ValueError('Unconsumed compressed data')
        if names!=chunk['blobs'] or counted.n!=chunk['bytes'] or counted.h.hexdigest()!=chunk['sha256']:
            raise ValueError('Compressed chunk sequence or checksum differs')
    if seen!=set(record['blobs']):raise ValueError('Missing encoded blob')

def iter_original_members(path):
    """Yield every original (path, bytes), including every alias, exactly once."""
    with zipfile.ZipFile(path) as archive:
        record=record_of(archive)
        if record is None:
            for info in archive.infolist():
                if info.is_dir():continue
                safe(info.filename);yield info.filename,archive.read(info)
            return
        for name,expected in record['runtime_hashes'].items():
            safe(name)
            if hashlib.sha256(archive.read(name)).hexdigest()!=expected:raise ValueError('Embedded runtime checksum differs')
        from png_private_compressed_rows import Decoder
        from png_exact_preconditioning import restore as restore_png
        from pdf_exact_preconditioning import restore as restore_pdf
        from png_exact_parameters import library,restore as restore_parameter_png
        by_blob={}
        for name,desc in record['members'].items():
            safe(name);by_blob.setdefault(desc['blob'],[]).append((name,desc))
        if set(by_blob)!=set(record['blobs']):raise ValueError('Original alias map differs')
        restored=0;lib=library()
        with Decoder(':memory:') as rows:
            for name,desc,encoded in encoded_members(archive,record):
                codec=desc['codec']
                if codec=='original':raw=encoded
                elif codec=='png-disk-rows-v2':raw=restore_png(rows.decode(encoded))
                elif codec=='png-idat-v1':raw=restore_png(encoded)
                elif codec=='pdf-zlib-v1':raw=restore_pdf(encoded)
                elif codec=='png-exact-parameters-v1':raw=restore_parameter_png(encoded,lib)
                else:raise ValueError('Unknown exact codec')
                sha=hashlib.sha256(raw).hexdigest()
                for original,expected in by_blob[name]:
                    if len(raw)!=expected['bytes'] or sha!=expected['sha256']:raise ValueError('Original member integrity differs: '+original)
                    restored+=1;yield original,raw
            if rows.count!=record['row_count'] or rows.blocks!=record['row_blocks']:raise ValueError('Original row stream counters differ')
        if restored!=len(record['members']):raise ValueError('Original member omitted')

def verify(path,compare_source=None,compare_tree=None,destination=None,tar_output=False):
    path=Path(path);seen=set();count=0;total=0
    with zipfile.ZipFile(path) as archive:
        record=record_of(archive)
        if archive.testzip() is not None:raise ValueError('Archive CRC failure')
    if compare_source and compare_tree:raise ValueError('Choose one original comparison source')
    source=zipfile.ZipFile(compare_source) if compare_source else None
    if compare_source and record and record.get('source_zip_sha256') and digest(compare_source)!=record['source_zip_sha256']:
        raise ValueError('Pinned original ZIP differs')
    if destination:
        destination=Path(destination)
        if destination.exists() and any(destination.iterdir()):raise ValueError('Restoration destination must be empty')
        destination.mkdir(parents=True,exist_ok=True)
    tar=tarfile.open(fileobj=sys.stdout.buffer,mode='w|',format=tarfile.PAX_FORMAT) if tar_output else None
    try:
        for name,data in iter_original_members(path):
            if name in seen:raise ValueError('Duplicate original member')
            if source is not None and data!=source.read(name):raise ValueError('Literal original ZIP member comparison failed: '+name)
            if compare_tree:
                original=Path(compare_tree)/safe(name)
                if original.is_symlink() or data!=original.read_bytes():raise ValueError('Literal frozen-tree comparison failed: '+name)
            if destination:
                target=destination/safe(name);target.parent.mkdir(parents=True,exist_ok=True)
                with target.open('xb') as stream:stream.write(data)
            if tar is not None:
                item=tarfile.TarInfo(name);item.size=len(data);tar.addfile(item,io.BytesIO(data))
            seen.add(name);count+=1;total+=len(data)
        if source is not None:
            original_names=[x.filename for x in source.infolist() if not x.is_dir()]
            if len(original_names)!=len(set(original_names)) or seen!=set(original_names):raise ValueError('Original ZIP path set differs')
        if compare_tree:
            policy=record.get('source_tree_exclusions') if record else None
            if policy is not None and policy!={'components':['B_146_ranges','B_148_ranges','__pycache__'],'suffixes':['.zip']}:
                raise ValueError('Unknown frozen source-file domain')
            names={str(p.relative_to(compare_tree)) for p in Path(compare_tree).rglob('*') if p.is_file()
                   and (policy is None or (not set(policy['components']).intersection(p.relative_to(compare_tree).parts)
                                          and p.suffix not in policy['suffixes']))}
            if names!=seen:raise ValueError('Frozen-tree path set differs')
    finally:
        if source:source.close()
        if tar is not None:tar.close()
    if compare_source and record and record.get('source_zip_sha256') and digest(compare_source)!=record['source_zip_sha256']:
        raise ValueError('Original ZIP changed during verification')
    return {'status':'PASS','all_original_members_verified':True,'retained_members':count,'original_member_bytes':total,
            'exact_source_comparison':bool(compare_source or compare_tree),'source_kind':'portable' if record else 'raw-ZIP',
            'wrapper_path':str(path),'wrapper_bytes':path.stat().st_size,'wrapper_sha256':digest(path),
            'no_external_checkpoint_dependency':True,'payload_chunks_extracted':False,'private_cache_written':False,
            'original_member_tar_stream':tar_output}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('wrapper',type=Path)
    p.add_argument('--verify-only',action='store_true');p.add_argument('--compare-source',type=Path)
    p.add_argument('--compare-tree',type=Path);p.add_argument('--destination',type=Path);p.add_argument('--members-tar',action='store_true')
    a=p.parse_args()
    if a.verify_only and a.destination:p.error('Choose verification or restoration')
    result=verify(a.wrapper,a.compare_source,a.compare_tree,a.destination,a.members_tar)
    print(json.dumps(result,indent=2),file=sys.stderr if a.members_tar else sys.stdout,flush=True)
