#!/usr/bin/env python3
"""Repeat the exact interrupted-stream and prefix-content packing audits.

Run against the frozen checkpoint09 extraction, not a later live trace.
This verifies content equivalence, never mathematical completion of C31.
"""
import argparse,gzip,hashlib,json,zlib
from pathlib import Path

def sha_stream(stream):
    h=hashlib.sha256();n=0
    while x:=stream.read(1<<20):h.update(x);n+=len(x)
    return n,h.hexdigest()

def check_raw(base,stem):
    p=base/stem;m=json.loads(Path(str(p)+'.archive.json').read_text())
    raw=base/Path(m['raw_compressed_prefix']).name;part=base/Path(m['partial_record']).name
    dec=zlib.decompressobj(16+zlib.MAX_WBITS);h=hashlib.sha256();n=0;rh=hashlib.sha256()
    with raw.open('rb') as src:
        while x:=src.read(1<<20):
            rh.update(x);y=dec.decompress(x);h.update(y);n+=len(y);assert not dec.unconsumed_tail
    y=dec.flush();h.update(y);n+=len(y);assert not dec.unused_data and not dec.unconsumed_tail
    hh=hashlib.sha256();nn=0
    with gzip.open(p,'rb') as src:
        while x:=src.read(1<<20):hh.update(x);nn+=len(x)
    x=part.read_bytes();hh.update(x);nn+=len(x)
    assert (n,h.hexdigest())==(nn,hh.hexdigest())
    assert rh.hexdigest()==m['raw_compressed_sha256']
    return {'stem':stem,'decoded_work_bytes':n,'decoded_work_sha256':h.hexdigest(),'exact_equal':True,'unconsumed_input_bytes':0}

def check_prefix(base,small,large,spaces):
    p=base/small;q=base/large;h=hashlib.sha256();n=0;size=0
    opener=gzip.open if q.suffix=='.gz' else open
    with gzip.open(p,'rb') as a,opener(q,'rb') as b:
        for line in a:
            source=b.readline()
            if spaces:source=source.replace(b' ',b'')
            assert line==source,n;h.update(line);size+=len(line);n+=1
        partial=Path(str(p)+'.partial_record').read_bytes();following=b.readline()
        if spaces:following=following.replace(b' ',b'')
        assert following.startswith(partial)
    return {'small':small,'source':large,'remove_ascii_spaces':spaces,'complete_records':n,
            'complete_bytes':size,'complete_sha256':h.hexdigest(),'partial_record_hex':partial.hex(),'exact_equal':True}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('code_directory',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();b=a.code_directory
    stems=['pbc_native_modular_iterated_trace.jsonl.gz','pbc_native_modular_v4_iterated_trace.jsonl.gz','pbc_native_modular_v3_iterated_trace.jsonl.gz']
    report={'raw_stream_equivalence':[check_raw(b,s) for s in stems],
            'prefix_equivalence':[check_prefix(b,stems[0],'pbc_iterated_modular_boundary_trace.jsonl',True),
                                  check_prefix(b,stems[1],'pbc_native_modular_v5_iterated_trace.jsonl.gz',False)],
            'status':'Exact work-payload preservation; compression wrappers superseded; C31 remains OPEN.'}
    a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
