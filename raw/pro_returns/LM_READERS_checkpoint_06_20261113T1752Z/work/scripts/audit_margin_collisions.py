"""Find candidate collisions between separately typeset right-margin notes.

This is a geometric candidate generator, not a visual pass/fail assertion.
Only separate PDF text lines with substantial horizontal overlap and very
close baselines are considered. Every candidate still requires inspection.
"""
from pathlib import Path
import datetime,hashlib,json,re
import pymupdf as fitz

ROOT=Path(__file__).resolve().parents[2]
BOOKS=(
    'LM_FR_diplomatique','LM_FR_corrige_apparat','LM_FR_texte_de_lecture',
    'LM_EN_corrected_apparatus','LM_EN_reading',
    'LM_FR_master_annotated','LM_EN_master_annotated',
)

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def candidates(pdf):
    rows=[]
    with fitz.open(pdf) as doc:
        for pno,page in enumerate(doc,1):
            if page.rect.width>page.rect.height:continue
            mainright=page.rect.width-25*72/25.4
            spans=[]
            for bi,block in enumerate(page.get_text('dict')['blocks']):
                for li,line in enumerate(block.get('lines',[])):
                    for si,span in enumerate(line['spans']):
                        if span['bbox'][0]<mainright-1:continue
                        if len(re.sub(r'\W','',span['text']))<2 and not span['text'].startswith('['):continue
                        spans.append(dict(line=[bi,li],text=span['text'],bbox=list(span['bbox']),
                                          origin=list(span['origin']),size=span['size']))
            for i,a in enumerate(spans):
                for b in spans[i+1:]:
                    if a['line']==b['line']:continue
                    ax0,ay0,ax1,ay1=a['bbox'];bx0,by0,bx1,by1=b['bbox']
                    x=min(ax1,bx1)-max(ax0,bx0);y=min(ay1,by1)-max(ay0,by0)
                    if x<=0 or y<=0:continue
                    if x/min(ax1-ax0,bx1-bx0)<.5:continue
                    if abs(a['origin'][1]-b['origin'][1])>=.65*min(a['size'],b['size']):continue
                    rect=fitz.Rect(min(ax0,bx0),min(ay0,by0),max(ax1,bx1),max(ay1,by1))
                    links=[]
                    for link in page.get_links():
                        if link.get('uri') and fitz.Rect(link['from']).intersects(rect):links.append(link['uri'])
                    rows.append(dict(file=Path(pdf).name,page=pno,first=a,second=b,
                        horizontal_overlap_fraction=x/min(ax1-ax0,bx1-bx0),
                        baseline_separation_pt=abs(a['origin'][1]-b['origin'][1]),
                        targets=sorted(set(links)),status='pending visual inspection'))
    return rows

def main():
    rows=[];readers=[]
    for book in BOOKS:
        pdf=ROOT/'work/build'/(book+'.pdf')
        before=digest(pdf)
        with fitz.open(pdf) as doc:page_count=len(doc)
        new=candidates(pdf)
        if digest(pdf)!=before:raise RuntimeError('PDF changed during marginal-line audit: '+pdf.name)
        rows+=new
        readers.append(dict(file=pdf.name,sha256=before,pages=page_count,candidate_count=len(new)))
        print(pdf.name,len(new),flush=True)
    out=ROOT/'work/data/margin_collision_candidates.json'
    cropdir=ROOT/'work/margin_collision_probes';cropdir.mkdir(exist_ok=True)
    for i,row in enumerate(rows,1):
        with fitz.open(ROOT/'work/build'/row['file']) as doc:
            page=doc[row['page']-1]
            a=fitz.Rect(row['first']['bbox']);b=fitz.Rect(row['second']['bbox']);r=a|b
            r=fitz.Rect(max(0,r.x0-100),max(0,r.y0-35),min(page.rect.width,r.x1+10),min(page.rect.height,r.y1+35))
            name=f"candidate_{i:03}.png";page.get_pixmap(matrix=fitz.Matrix(3,3),clip=r,alpha=False).save(cropdir/name)
            row['detail_image']='work/margin_collision_probes/'+name
    out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    # A completed empty candidate list still needs a current, seven-book
    # provenance record. COMPLETE describes execution, not visual clearance.
    for reader in readers:
        if digest(ROOT/'work/build'/reader['file'])!=reader['sha256']:
            raise RuntimeError('PDF changed before marginal-line audit completion: '+reader['file'])
    audit=dict(schema='margin-collision-audit-v1',status='COMPLETE',
        generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        readers=readers,total_candidates=len(rows),
        candidate_file='work/data/margin_collision_candidates.json',
        method='Distinct right-margin text lines with substantial horizontal overlap and close baselines; landscape pages and isolated one-character components are excluded. Candidates require visual inspection.')
    manifest=ROOT/'work/data/margin_collision_audit.json'
    pending=manifest.with_suffix('.pending.json')
    pending.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    pending.replace(manifest)
    print('Candidate pairs',len(rows),flush=True)

if __name__=='__main__':main()
