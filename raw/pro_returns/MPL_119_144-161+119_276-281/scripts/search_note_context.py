#!/usr/bin/env python3
"""Reproduce the per-note search of supplied context; no scan processing/OCR."""
from pathlib import Path
import argparse,csv,subprocess
p=argparse.ArgumentParser();p.add_argument('--context',default='context');args=p.parse_args()
base=Path(__file__).resolve().parents[1]
queries=list(csv.DictReader((base/'research/context_queries.tsv').open(),delimiter='\t'))
with (base/'research/context_searches.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['note_id','search_terms','context_file','line','matched_text'])
 for q in queries:
  run=subprocess.run(['rg','--no-heading','--line-number','--ignore-case','--',q['terms'],args.context],text=True,capture_output=True)
  if run.returncode not in (0,1): raise RuntimeError(q['note_id']+': '+run.stderr)
  found=[]
  for line in run.stdout.splitlines():
   path,num,body=line.split(':',2);found.append((path,num,body));w.writerow([q['note_id'],q['terms'],path,num,body])
  if not found:w.writerow([q['note_id'],q['terms'],'NO MATCH','',''])
  print(q['note_id'],len(found))
