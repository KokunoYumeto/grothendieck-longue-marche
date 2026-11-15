#!/usr/bin/env python3
"""Losslessly encode frozen checkpoint09 proof payloads and verify every byte."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse,gzip,hashlib,json,lzma,subprocess,threading,zipfile,time

BASE=Path(__file__).resolve().parents[1]
SNAPSHOT=BASE.parent/'LM8_PUSH_checkpoint_09.zip'
OUT=BASE.parent/'checkpoint09_binary'
OUT.mkdir(exist_ok=True)
CODEC=BASE/'code/pbc_trace_binary_codec'
N='18366102701919111870287640813247479948797709553001809575936'
CHUNK=1<<20
FILTERS=[{'id':lzma.FILTER_LZMA2,'preset':3,'dict_size':64<<20}]

def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()

with zipfile.ZipFile(SNAPSHOT) as z:
 original={r['path']:r for r in json.loads(z.read('PACKAGE_MANIFEST.json'))['files']}

def convert(name):
 started=time.time();path=OUT/(name+'.pbcbin.xz');path.parent.mkdir(parents=True,exist_ok=True)
 ledger=path.with_suffix(path.suffix+'.json')
 if ledger.exists():
  row=json.loads(ledger.read_text());assert row['original_sha256']==original[name]['sha256'] and sha(path)==row['encoded_xz_sha256'];return row
 proc=subprocess.Popen([str(CODEC),'encode',N],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 incoming=hashlib.sha256();incount=0;errors=[]
 def feed():
  nonlocal incount
  try:
   with zipfile.ZipFile(SNAPSHOT) as z,z.open(name) as raw:
    inp=gzip.GzipFile(fileobj=raw) if name.endswith('.gz') else raw
    for b in iter(lambda:inp.read(CHUNK),b''):
     incoming.update(b);incount+=len(b);proc.stdin.write(b)
    if inp is not raw:inp.close()
   proc.stdin.close()
  except BaseException as e:errors.append(repr(e));proc.kill()
 t=threading.Thread(target=feed);t.start()
 encoded=hashlib.sha256();encount=0
 with lzma.LZMAFile(path,'wb',filters=FILTERS) as out:
  for b in iter(lambda:proc.stdout.read(CHUNK),b''):
   encoded.update(b);encount+=len(b);out.write(b)
 t.join();encoder_log=proc.stderr.read().decode();assert proc.wait()==0 and not errors,(encoder_log,errors)
 if not name.endswith('.gz'):assert incoming.hexdigest()==original[name]['sha256'] and incount==original[name]['bytes']
 print(json.dumps({'encoded':name,'raw_bytes':incount,'binary_bytes':encount,'xz_bytes':path.stat().st_size,'elapsed':time.time()-started}),flush=True)
 dec=subprocess.Popen([str(CODEC),'decode'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 def feed_decode():
  try:
   with lzma.open(path,'rb') as inp:
    for b in iter(lambda:inp.read(CHUNK),b''):dec.stdin.write(b)
   dec.stdin.close()
  except BaseException as e:errors.append(repr(e));dec.kill()
 t=threading.Thread(target=feed_decode);t.start();restored=hashlib.sha256();count=0
 for b in iter(lambda:dec.stdout.read(CHUNK),b''):restored.update(b);count+=len(b)
 t.join();decoder_log=dec.stderr.read().decode();assert dec.wait()==0 and not errors,(decoder_log,errors)
 assert restored.hexdigest()==incoming.hexdigest() and count==incount
 row={'original_path':name,'original_sha256':original[name]['sha256'],'original_bytes':original[name]['bytes'],
      'decoded_sha256':incoming.hexdigest(),'decoded_bytes':incount,'stored_path':name+'.pbcbin.xz',
      'encoded_binary_sha256':encoded.hexdigest(),'encoded_binary_bytes':encount,
      'encoded_xz_sha256':sha(path),'encoded_xz_bytes':path.stat().st_size,
      'codec_source_sha256':sha(BASE/'code/pbc_trace_binary_codec.cpp'),
      'codec_executable_sha256':sha(CODEC),
      'compiler_command':'g++ -std=c++17 -O3 LM8_PUSH/code/pbc_trace_binary_codec.cpp -lgmpxx -lgmp -o LM8_PUSH/code/pbc_trace_binary_codec',
      'codec':'PBCBIN01','kind':'gzip_payload' if name.endswith('.gz') else 'raw_bytes',
      'entire_decoded_byte_hash_verified':True,'encoder_log':encoder_log.strip(),'decoder_log':decoder_log.strip(),
      'seconds':time.time()-started,'scope':'Exact original proof bytes; no proof claim or status change.'}
 ledger.write_text(json.dumps(row,indent=2)+'\n');print(json.dumps({'VERIFIED':name,'xz_bytes':row['encoded_xz_bytes'],'seconds':row['seconds']}),flush=True);return row

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('names',nargs='*');ap.add_argument('--jobs',type=int,default=4);args=ap.parse_args()
 names=args.names or ['code/pbc_iterated_modular_boundary_trace.jsonl','code/pbc_native_modular_v5_iterated_trace.jsonl.gz',
  'code/pbc_iterated_modular_torsion_trace.jsonl','code/pbc_iterated_precollected_trace.jsonl',
  'code/pbc_iterated_modular_coordinates_trace.jsonl','code/pbc_iterated_modular_scan_trace.jsonl',
  'code/pbc_iterated_modular_unit_trace.jsonl','code/pbc_iterated_modular_trace.jsonl']
 results=[]
 with ThreadPoolExecutor(max_workers=args.jobs) as pool:
  for f in as_completed([pool.submit(convert,n) for n in names]):results.append(f.result())
 (OUT/'binary_conversion_manifest.json').write_text(json.dumps({'source_snapshot':str(SNAPSHOT),
  'source_snapshot_sha256':'e594317a692df7d6aa88cfa0f58ebc551a8c7ebf70e153854e37da52ef8f4ada',
  'transforms':sorted(results,key=lambda r:r['original_path'])},indent=2)+'\n')
