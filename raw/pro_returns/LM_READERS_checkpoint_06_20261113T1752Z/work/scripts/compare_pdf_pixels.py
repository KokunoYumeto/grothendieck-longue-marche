#!/usr/bin/env python3
"""Compare every corresponding page raster, optionally transfer evidenced reviews.

The target's selected pages must already be rendered. A review can transfer only
from an attributed, previously reviewed source row whose stored image hashes
match both its actual image file and the freshly rendered source/target pixels.
This never creates an inspection claim for a new image.
"""
from __future__ import annotations
import argparse
import csv
import json
import os
from pathlib import Path
import pymupdf as fitz
from verify_pdf import (sha256, pixmap_pixel_sha256, image_pixel_sha256,
                        review_is_attributed, REVIEW_FIELDS)


def load_review(directory):
    path=Path(directory)/'VISUAL_REVIEW.tsv'
    if not path.exists():return {}
    with path.open(newline='') as f:
        return {int(r['page']):r for r in csv.DictReader(f,delimiter='\t')}


def render_hash(page,width):
    pix=page.get_pixmap(matrix=fitz.Matrix(width/page.rect.width,width/page.rect.width),colorspace=fitz.csRGB,alpha=False)
    return {'pixel_sha256':pixmap_pixel_sha256(pix),'width':pix.width,'height':pix.height}


def compare(source,target,output,source_review=None,target_review=None,width=900,transfer=False):
    source,target,output=Path(source),Path(target),Path(output)
    source_hash,target_hash=sha256(source),sha256(target)
    sr=load_review(source_review) if source_review else {}
    tr=load_review(target_review) if target_review else {}
    rows=[];transfers=[];blocked=[];differences=[]
    with fitz.open(source) as a,fitz.open(target) as b:
        counts=(len(a),len(b))
        for pno in range(1,max(counts)+1):
            ah=render_hash(a[pno-1],width) if pno<=len(a) else None
            bh=render_hash(b[pno-1],width) if pno<=len(b) else None
            same=ah is not None and ah==bh
            row={'page':pno,'source':ah,'target':bh,'identical_pixels':same}
            rows.append(row)
            if not same:differences.append(pno)
            if not transfer or pno not in tr or review_is_attributed(tr[pno]):continue
            previous=sr.get(pno,{});target_row=tr[pno]
            if not same:
                blocked.append({'page':pno,'reason':'Corresponding rendered pages differ.'});continue
            if not review_is_attributed(previous):
                blocked.append({'page':pno,'reason':'Source page has no attributed completed visual review.'});continue
            if previous.get('pdf_sha256')!=source_hash or target_row.get('pdf_sha256')!=target_hash:
                blocked.append({'page':pno,'reason':'Review row belongs to a different PDF hash.'});continue
            source_image=Path(source_review)/previous['full_page_image']
            target_image=Path(target_review)/target_row['full_page_image']
            if not source_image.is_file() or not target_image.is_file():
                blocked.append({'page':pno,'reason':'Required selected-page image absent.'});continue
            valid=True
            for record,path,fresh in ((previous,source_image,ah),(target_row,target_image,bh)):
                if (record.get('png_sha256')!=sha256(path) or
                    record.get('rendered_pixel_sha256')!=image_pixel_sha256(path) or
                    record.get('rendered_pixel_sha256')!=fresh['pixel_sha256']):valid=False
            if not valid:
                blocked.append({'page':pno,'reason':'Stored image evidence differs from actual or freshly rendered pixels.'});continue
            if previous['png_sha256']!=target_row['png_sha256']:
                blocked.append({'page':pno,'reason':'PNG files differ despite RGB equality; no automatic review transfer.'});continue
            target_row.update({'status':'reviewed','reviewer':previous['reviewer'],
              'observations':'Review inherited through verified exact pixel identity. Source observation: '+previous['observations'],
              'review_basis':'Corresponding master page is pixel-identical to an attributed reviewed apparatus-reader page.',
              'reviewed_at_utc':previous.get('reviewed_at_utc',''),
              'review_reference_pdf':source.name,'review_reference_pdf_sha256':source_hash,
              'review_reference_page':str(pno),'review_reference_pixel_sha256':previous['rendered_pixel_sha256'],
              'review_reference_png_sha256':previous['png_sha256'],
              'review_reference_image':Path(os.path.relpath(source_image,Path(target_review))).as_posix()})
            transfers.append({'page':pno,'source_page':pno,'source_pdf':source.name,
              'source_pdf_sha256':source_hash,'target_pdf_sha256':target_hash,
              'pixel_sha256':ah['pixel_sha256'],'png_sha256':previous['png_sha256'],
              'reviewer':previous['reviewer'],'source_observation':previous['observations']})
    if sha256(source)!=source_hash or sha256(target)!=target_hash:
        raise RuntimeError('An input PDF changed during the raster comparison; no review transfer saved.')
    result={'source_pdf':source.name,'target_pdf':target.name,'source_pdf_sha256':source_hash,'target_pdf_sha256':target_hash,
      'render_width_pixels':width,'colorspace':'RGB without alpha','source_pages':counts[0],'target_pages':counts[1],
      'page_counts_equal':counts[0]==counts[1],'identical_page_count':sum(r['identical_pixels'] for r in rows),
      'different_or_missing_pages':differences,'every_corresponding_page_compared':True,'pages':rows,
      'review_transfer_requested':transfer,'transferred_reviews':transfers,'blocked_transfers':blocked,
      'policy':'Transfer only previously attributed visual reviews with exact freshly rendered pixel and PNG-file identity. No new inspection claimed.'}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    if transfer:
        target_path=Path(target_review)/'VISUAL_REVIEW.tsv'
        with target_path.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=REVIEW_FIELDS,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(tr[p] for p in sorted(tr))
        if transfers:
            with (Path(target_review)/'REVIEW_HISTORY.jsonl').open('a') as f:
                for r in transfers:f.write(json.dumps({'action':'transfer reviewed status from identical source page',**r},ensure_ascii=False)+'\n')
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_pdf');ap.add_argument('target_pdf');ap.add_argument('--output',required=True)
    ap.add_argument('--source-review');ap.add_argument('--target-review');ap.add_argument('--width',type=int,default=900)
    ap.add_argument('--transfer-reviewed',action='store_true');a=ap.parse_args()
    if a.transfer_reviewed and (not a.source_review or not a.target_review):ap.error('Review transfer requires both review directories.')
    r=compare(a.source_pdf,a.target_pdf,a.output,a.source_review,a.target_review,a.width,a.transfer_reviewed)
    print(json.dumps({k:r[k] for k in ('source_pdf','target_pdf','source_pages','target_pages','identical_page_count','different_or_missing_pages')} |
                     {'transferred_reviews':len(r['transferred_reviews']),'blocked_transfers':len(r['blocked_transfers'])}))


if __name__=='__main__':main()
