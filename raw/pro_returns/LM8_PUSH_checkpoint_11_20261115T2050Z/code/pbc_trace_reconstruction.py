#!/usr/bin/env python3
"""Reconstruct superseded native proof-log payloads from retained source logs.

Compression wrappers are deliberately not byte-reconstructed. The exact
mathematical JSONL bytes and the trailing partial record are hash-checked.
The checkpoint09 mathematics and its OPEN C31 status are unchanged.
"""
import argparse,gzip,hashlib,json,lzma
from pathlib import Path

def open_payload(path):
    if path.suffix=='.xz':return lzma.open(path,'rb')
    if path.suffix=='.gz':return gzip.open(path,'rb')
    return path.open('rb')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('mapping',type=Path)
    ap.add_argument('kind',choices=['native_v1','native_v4'])
    ap.add_argument('source',type=Path,help='Retained boundary JSONL or checkpoint09-v5 JSONL payload, optionally XZ/gzip compressed.')
    ap.add_argument('output',type=Path,help='Exact reconstructed JSONL bytes; use .gz for a fresh valid gzip wrapper.')
    ap.add_argument('--partial-output',type=Path)
    args=ap.parse_args();row=json.loads(args.mapping.read_text())['reconstructions'][args.kind]
    h=hashlib.sha256();size=0
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with open_payload(args.source) as src,args.output.open('wb') as file:
        out=gzip.GzipFile(fileobj=file,mode='wb',compresslevel=1,mtime=0) if args.output.suffix=='.gz' else file
        try:
            for i in range(row['complete_records']):
                line=src.readline();assert line and line.endswith(b'\n'),i
                if row['remove_ascii_spaces']:line=line.replace(b' ',b'')
                out.write(line);h.update(line);size+=len(line)
            following=src.readline()
            if row['remove_ascii_spaces']:following=following.replace(b' ',b'')
            partial=bytes.fromhex(row['partial_record_hex'])
            assert following.startswith(partial)
        finally:
            if out is not file:out.close()
    assert size==row['complete_bytes'] and h.hexdigest()==row['complete_sha256']
    if args.partial_output:args.partial_output.write_bytes(partial)
    print(json.dumps({'exact_payload_reconstructed':True,'bytes':size,'sha256':h.hexdigest(),
                      'records':row['complete_records'],'partial_bytes':len(partial),
                      'original_compression_wrapper_superseded':True,'mathematical_status':'C31 OPEN'},indent=2))

if __name__=='__main__':main()
