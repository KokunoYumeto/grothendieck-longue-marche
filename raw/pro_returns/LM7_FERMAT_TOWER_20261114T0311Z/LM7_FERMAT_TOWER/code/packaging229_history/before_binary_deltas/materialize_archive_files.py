#!/usr/bin/env python3
"""Restore exact duplicate binary certificates and historical QA images.

Every alias retains its original path, byte count and SHA-256. This program
copies verified original bytes; it performs no numerical conversion, image
resampling, serialization or re-encoding. All text sources and transcripts
remain ordinary ZIP members.
"""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json

BINARY={'.bin','.npz','.npy'}
RASTER={'.jpg','.jpeg','.png'}
def sha(b):return hashlib.sha256(b).hexdigest()
def eligible(name,kind):
    p=PurePosixPath(name)
    if kind=='binary':return p.suffix.lower() in BINARY and p.parts[0] in {'code','inputs'}
    assert kind=='image'
    return p.suffix.lower() in RASTER and 'qa' in p.parts

def plan_binary_aliases(payload):
    groups={}
    for name,data in payload.items():
        if eligible(name,'binary'):
            groups.setdefault((sha(data),len(data)),[]).append(name)
    def key(name):
        p=PurePosixPath(name)
        return ('history' in p.parts,len(p.parts),name)
    aliases=[]
    for (h,n),names in sorted(groups.items()):
        names=sorted(names,key=key)
        for name in names[1:]:
            assert payload[name]==payload[names[0]]
            aliases.append({'path':name,'storage_path':names[0],'bytes':n,'sha256':h})
    aliases.sort(key=lambda x:x['path'])
    names={x['path'] for x in aliases}
    assert not any(x['storage_path'] in names for x in aliases)
    return {'format_version':1,
            'scope':'Only complete byte-identical .bin/.npz/.npy data certificates and inputs. All source programs, text transcripts, JSON records and the current paper remain ordinary ZIP members.',
            'aliases':aliases}

def inside(root,name,kind):
    p=PurePosixPath(name)
    assert not p.is_absolute() and p.parts and '..' not in p.parts,name
    assert eligible(name,kind),name
    q=root.joinpath(*p.parts)
    assert q.resolve().is_relative_to(root.resolve()),name
    for parent in [q,*q.parents]:
        if parent==root:break
        assert not parent.is_symlink(),name
    return q

def materialize(root,verify_only=False):
    root=Path(root).resolve()
    counts={};manifests={};total=0
    for kind,fn in [('image','archive_image_aliases.json'),('binary','archive_binary_aliases.json')]:
        path=root/'ledger'/fn
        if not path.exists():continue
        raw=path.read_bytes();d=json.loads(raw)
        assert d['format_version']==1
        names={x['path'] for x in d['aliases']}
        assert len(names)==len(d['aliases'])
        created=0;checked=0
        for x in d['aliases']:
            assert x['storage_path'] not in names
            source=inside(root,x['storage_path'],kind)
            target=inside(root,x['path'],kind)
            b=source.read_bytes()
            assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['storage_path']
            if target.exists():
                assert target.read_bytes()==b,x['path']
            else:
                assert not verify_only,'Missing logical file: '+x['path']
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(b);created+=1
            actual=target.read_bytes()
            assert len(actual)==x['bytes'] and sha(actual)==x['sha256'],x['path']
            checked+=1;total+=len(actual)
        counts[kind]={'aliases_checked':checked,'files_created':created}
        manifests[fn]=sha(raw)
    assert manifests,'No exact-alias manifests found'
    return {'status':'PASS','manifest_hashes':manifests,'counts':counts,
            'logical_alias_bytes_checked':total,'overwritten_nonmatching_files':0,
            'reserialized_binary_objects':0,'resampled_or_reencoded_images':0}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--verify-only',action='store_true')
    a=ap.parse_args();print(json.dumps(materialize(a.root,a.verify_only),indent=2))
if __name__=='__main__':main()
