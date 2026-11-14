#!/usr/bin/env python3
"""Restore exact duplicate historical QA images from explicit byte aliases.

Only raster QA images are eligible. All code, mathematical inputs, outputs,
certificates and current main-PDF page images remain ordinary ZIP members.
No image is resampled or re-encoded. Each restored byte string is checked
against the same SHA-256 and size as the original logical file.
"""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,re

def sha(data):
    return hashlib.sha256(data).hexdigest()

def plan_image_aliases(payload,current_statement_count):
    groups={}
    for name,data in payload.items():
        p=PurePosixPath(name)
        if p.suffix.lower() not in {'.jpg','.jpeg','.png'}:continue
        if 'qa' not in p.parts:continue
        groups.setdefault((sha(data),len(data)),[]).append(name)
    def protected(name):
        return (name.startswith('qa/contact_') or
                name.startswith('qa/detail'+str(current_statement_count)+'_'))
    def key(name):
        p=PurePosixPath(name)
        return (not protected(name),'history' in p.parts,len(p.parts),name)
    aliases=[]
    for (digest,size),names in sorted(groups.items()):
        names=sorted(names,key=key);canonical=names[0]
        for name in names[1:]:
            if protected(name):continue
            assert payload[name]==payload[canonical]
            aliases.append({'path':name,'storage_path':canonical,'bytes':size,'sha256':digest})
    aliases.sort(key=lambda r:r['path'])
    alias_names={r['path'] for r in aliases}
    assert not any(r['storage_path'] in alias_names for r in aliases)
    return {'format_version':1,
            'scope':'Only byte-identical duplicate QA raster images; all mathematical records and current main-PDF page images are ordinary files.',
            'current_statement_count':current_statement_count,
            'aliases':aliases}

def inside(root,name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and '..' not in p.parts and p.parts,name
    assert p.suffix.lower() in {'.jpg','.jpeg','.png'} and 'qa' in p.parts,name
    q=root.joinpath(*p.parts)
    assert q.resolve().is_relative_to(root.resolve()),name
    assert not q.is_symlink(),name
    return q

def materialize(root,verify_only=False):
    root=Path(root).resolve()
    manifest=root/'ledger/archive_image_aliases.json'
    d=json.loads(manifest.read_text());assert d['format_version']==1
    names={r['path'] for r in d['aliases']}
    assert len(names)==len(d['aliases'])
    created=0;checked=0;total_bytes=0
    for r in d['aliases']:
        assert r['storage_path'] not in names
        source=inside(root,r['storage_path']);target=inside(root,r['path'])
        data=source.read_bytes()
        assert len(data)==r['bytes'] and sha(data)==r['sha256'],r['storage_path']
        if target.exists():
            assert target.read_bytes()==data,r['path']
        else:
            assert not verify_only,'Missing image: '+r['path']
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(data);created+=1
        assert target.stat().st_size==r['bytes'] and sha(target.read_bytes())==r['sha256'],r['path']
        checked+=1;total_bytes+=r['bytes']
    return {'status':'PASS','alias_manifest_sha256':sha(manifest.read_bytes()),
            'aliases_checked':checked,'exact_images_created':created,
            'logical_image_bytes_checked':total_bytes,
            'overwritten_nonmatching_files':0,'resampled_or_reencoded_images':0}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--verify-only',action='store_true')
    a=ap.parse_args();print(json.dumps(materialize(a.root,a.verify_only),indent=2))

if __name__=='__main__':main()
