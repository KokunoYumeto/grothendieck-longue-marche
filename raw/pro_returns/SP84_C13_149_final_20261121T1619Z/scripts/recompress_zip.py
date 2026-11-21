"""Losslessly repack an edition as ordinary ZIP method 8 using cached raw DEFLATE.

Caches are optional JSON lists or individual JSON records with name, file and
sha256 keys. They were produced by compressing original file bytes with Zopfli or libdeflate.
Every supplied stream and every finished member is verified before acceptance.
No PNG image is decoded, altered or re-encoded by this procedure.
"""
from pathlib import Path
import argparse, copy, hashlib, json, struct, zipfile, zlib


def sha(data):
    return hashlib.sha256(data).hexdigest()


def compressed_bytes(path, info):
    with path.open('rb') as f:
        f.seek(info.header_offset)
        h=f.read(30)
        assert h[:4]==b'PK\x03\x04'
        namesize,extrasize=struct.unpack_from('<HH',h,26)
        f.seek(namesize+extrasize,1)
        encoded=f.read(info.compress_size)
    assert len(encoded)==info.compress_size
    return encoded


class Preencoded:
    def __init__(self, data):
        self.data=data
    def compress(self, data):
        result,self.data=self.data,b''
        return result
    def flush(self):
        result,self.data=self.data,b''
        return result


def run(root, source, destination, caches):
    assert not destination.exists(), 'Refusing to overwrite an archive'
    frozen=json.loads((root/'documentation/frozen_sha256.json').read_text())['sha256']
    for name,digest in frozen.items():
        assert sha((root/name).read_bytes())==digest, name
    candidates={}
    for cache in caches:
        obj=json.loads(cache.read_text())
        records=obj if isinstance(obj,list) else obj.get('results',[obj])
        for record in records:
            if 'candidate_path' in record:
                record={'name':record['member'],'file':record['candidate_path'],'sha256':record['source_sha256']}
            if not all(k in record for k in ('name','file','sha256')): continue
            p=Path(record['file'])
            if not p.is_file(): continue
            candidates.setdefault(record['name'],[]).append(record)
    members=sorted(p for p in root.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
    expected={str(p.relative_to(root)):sha(p.read_bytes()) for p in members}
    getter=zipfile._get_compressor
    def get_compressor(method,level=None):
        if method==zipfile.ZIP_DEFLATED and isinstance(level,tuple) and level[0]=='verified_raw_deflate':
            return Preencoded(level[1])
        return getter(method,level)
    optimized=0
    saved=0
    zipfile._get_compressor=get_compressor
    try:
        with zipfile.ZipFile(source) as old, zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as new:
            previous={i.filename:i for i in old.infolist()}
            for p in members:
                name=str(p.relative_to(root)); data=p.read_bytes(); digest=expected[name]
                prior=previous.get(name); stream=None
                if prior and prior.compress_type==zipfile.ZIP_DEFLATED and old.read(name)==data:
                    stream=compressed_bytes(source,prior)
                else:
                    encoder=zlib.compressobj(9,zlib.DEFLATED,-15)
                    stream=encoder.compress(data)+encoder.flush()
                baseline=len(stream)
                for candidate in candidates.get(name,[]):
                    if candidate['sha256']!=digest: continue
                    encoded=Path(candidate['file']).read_bytes()
                    if len(encoded)>=len(stream): continue
                    assert zlib.decompress(encoded,-15)==data,name
                    stream=encoded
                if len(stream)<baseline:
                    optimized+=1; saved+=baseline-len(stream)
                info=zipfile.ZipInfo.from_file(p,name)
                new.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=('verified_raw_deflate',stream))
    finally:
        zipfile._get_compressor=getter
    with zipfile.ZipFile(destination) as z:
        infos=z.infolist()
        assert len(infos)==len(expected)
        assert len({i.filename for i in infos})==len(infos)
        assert set(z.namelist())==set(expected)
        for info in infos:
            assert info.compress_type==zipfile.ZIP_DEFLATED,info.filename
            digest=sha(z.read(info))
            assert digest==expected[info.filename],info.filename
            if info.filename in frozen: assert digest==frozen[info.filename]
    result={'path':str(destination),'bytes':destination.stat().st_size,'files':len(members),'sha256':sha(destination.read_bytes()),'method':8,'optimized_entries':optimized,'compressed_bytes_saved':saved,'every_member_matches_edition':True,'frozen_hashes_verified':len(frozen)}
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('root',type=Path)
    parser.add_argument('source',type=Path)
    parser.add_argument('destination',type=Path)
    parser.add_argument('caches',type=Path,nargs='*')
    a=parser.parse_args()
    run(a.root,a.source,a.destination,a.caches)
