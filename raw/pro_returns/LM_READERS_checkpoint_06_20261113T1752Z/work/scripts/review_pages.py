#!/usr/bin/env python3
"""List review queues or record observations made after actual image inspection.

This utility does not inspect images or generate observations. The reviewer must
first view the named images and supply per-page observations in a JSON mapping.
Existing PDF/image evidence is checked before recording the supplied review.
"""
from __future__ import annotations
import argparse
import collections
import csv
import datetime
import json
from pathlib import Path
from verify_pdf import REVIEW_FIELDS, sha256, image_pixel_sha256


def load(directory):
    directory=Path(directory)
    with (directory/'VISUAL_REVIEW.tsv').open(newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    return directory,rows


def queue(directory):
    directory,rows=load(directory)
    closefile=directory.parent/(directory.name+'.CLOSE_REVIEW_PAGES.tsv')
    close={}
    if closefile.exists():
        with closefile.open(newline='') as f:close={int(r['page']):r for r in csv.DictReader(f,delimiter='\t')}
    groups=collections.defaultdict(list)
    for r in rows:
        groups[r['overview_sheet']].append({'page':int(r['page']),'status':r['status'],
          'close_review_required':int(r['page']) in close,'full_page_image':r['full_page_image'],
          'contact_sheet':r['contact_sheet']})
    return {'book':directory.name,'selected_pages':len(rows),'close_review_pages':len(close),
      'overview_sheets':[{'image':name,'pages':rs} for name,rs in sorted(groups.items())]}


def record(directory,observations,reviewer,basis,append=False):
    directory,rows=load(directory)
    supplied=json.loads(Path(observations).read_text())
    if not isinstance(supplied,dict):raise ValueError('Observations must map page numbers to observations actually made.')
    notes={int(p):str(note).strip() for p,note in supplied.items()}
    bypage={int(r['page']):r for r in rows}
    if set(notes)-set(bypage):raise ValueError('An observation names a page outside this rendered review inventory.')
    if not reviewer.strip() or not basis.strip() or any(not x for x in notes.values()):raise ValueError('Reviewer, inspection basis and every observation are required.')
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    updates=[]
    for page,note in notes.items():
        r=bypage[page];image=directory/r['full_page_image']
        if (not image.is_file() or sha256(image)!=r.get('png_sha256') or
            image_pixel_sha256(image)!=r.get('rendered_pixel_sha256')):
            raise ValueError(f'Page {page}: stored image evidence no longer matches.')
        updates.append({'page':page,'pdf_sha256':r['pdf_sha256'],'pixel_sha256':r['rendered_pixel_sha256'],
          'png_sha256':r['png_sha256'],'reviewer':reviewer,'basis':basis,'observation':note,'recorded_at_utc':now})
        r.update({'status':'reviewed','reviewer':reviewer,'reviewed_at_utc':now,
          'observations':r['observations']+'; '+note if append and r.get('observations') else note,
          'review_basis':r['review_basis']+'; '+basis if append and r.get('review_basis') else basis})
    tmp=directory/'VISUAL_REVIEW.pending.tsv'
    with tmp.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=REVIEW_FIELDS,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
    tmp.replace(directory/'VISUAL_REVIEW.tsv')
    with (directory/'REVIEW_HISTORY.jsonl').open('a') as f:
        for update in updates:f.write(json.dumps({'action':'record supplied observations after image inspection',**update},ensure_ascii=False)+'\n')
    return {'book':directory.name,'new_observations':len(updates),'reviewed_pages':sum(r['status']=='reviewed' for r in rows),
      'selected_pages':len(rows),'observations_generated_by_script':False}


def main():
    ap=argparse.ArgumentParser(description=__doc__);sp=ap.add_subparsers(dest='command',required=True)
    q=sp.add_parser('queue');q.add_argument('directory');q.add_argument('--output')
    r=sp.add_parser('record');r.add_argument('directory');r.add_argument('--observations',required=True)
    r.add_argument('--reviewer',required=True);r.add_argument('--basis',required=True);r.add_argument('--append',action='store_true')
    a=ap.parse_args()
    result=queue(a.directory) if a.command=='queue' else record(a.directory,a.observations,a.reviewer,a.basis,a.append)
    rendered=json.dumps(result,ensure_ascii=False,indent=2)
    if a.command=='queue' and a.output:Path(a.output).write_text(rendered+'\n')
    else:print(rendered)


if __name__=='__main__':main()
