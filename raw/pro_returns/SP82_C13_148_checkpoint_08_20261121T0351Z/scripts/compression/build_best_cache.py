#!/usr/bin/env python3
"""Create a reproducible cache containing the smallest verified lossless encoding.
It changes no source image, crop evidence, or prior archive.
"""
from pathlib import Path
import json,os,shutil,fcntl
ROOT=Path(__file__).resolve().parents[2]
old=ROOT/'work/jxl_evidence_cache';tuned=ROOT/'work/compression_engineering/cache_tuned';best=ROOT/'work/jxl_best_evidence_cache';best.mkdir(exist_ok=True)
lock=(best.parent/'jxl_best_evidence_cache.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX)
count=0;saved=0
for original in old.glob('*.jxl'):
 if len(original.stem)!=64 or any(c not in '0123456789abcdef' for c in original.stem):continue
 chosen=original;alternative=tuned/original.name;meta=alternative.with_suffix('.json')
 if alternative.is_file() and meta.is_file():
  data=json.loads(meta.read_text())
  if data.get('pixels_identical') and data.get('rgba_sha256')==original.stem and data.get('new_bytes')==alternative.stat().st_size and alternative.stat().st_size<original.stat().st_size:
   chosen=alternative;count+=1;saved+=original.stat().st_size-alternative.stat().st_size
 dest=best/original.name
 if not dest.is_file() or dest.stat().st_size>chosen.stat().st_size:
  tmp=dest.with_name(dest.name+'.best-'+str(os.getpid())+'.tmp');shutil.copy2(chosen,tmp);tmp.replace(dest)
print(json.dumps({'best_cache':str(best),'optimized_entries':count,'bytes_saved':saved}))
