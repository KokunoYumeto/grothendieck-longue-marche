#!/usr/bin/env python3
"""Read-only candidates for bare equation numbers stranded at page breaks.

This is a review queue, not an assertion that every candidate is defective.
Unlike a last-extracted-line check it excludes footers, marginal scan/page
marks, source anchor identifiers, and isolated daggers. It also checks the
reverse case: a trailing bare number at the start of the following page.
"""
from __future__ import annotations
import argparse, csv, datetime, hashlib, json, re, unicodedata
from pathlib import Path
import fitz
from PIL import Image, ImageDraw

SCAN_URI = re.compile(r'^https://grothendieck\.umontpellier\.fr/web/viewer\.html\?file=\.\./(140-[1-4])\.pdf#page=(\d+)$')

BOOKS = ['LM_FR_diplomatique','LM_FR_corrige_apparat','LM_FR_texte_de_lecture',
         'LM_EN_corrected_apparatus','LM_EN_reading','LM_FR_master_annotated','LM_EN_master_annotated']
TAG = re.compile(r'^\((?:\d{1,4}[a-z]*(?:bis|ter)?[\u2032\u2033\'\"]*|[IVX]{1,7})\)$',re.I)
TAG_WITH_MAP = re.compile(r'^(?P<tag>\((?:\d{1,4}[a-z]*(?:bis|ter)?[\u2032\u2033\'\"]*|[IVX]{1,7})\))(?P<map>[A-Za-zΑ-Ωα-ω][\u2032\u2033\'\"]?:)$', re.I)
MAP_NAME = re.compile(r'^[A-Za-zΑ-Ωα-ω][\u2032\u2033\'\"]?:$')
TAG_PREFIX = re.compile(r'^(?P<tag>\((?:\d{1,4}[a-z]*(?:bis|ter)?[\u2032\u2033\'\"]*|[IVX]{1,7})\))(?P<suffix>.+)$', re.I)
SOURCE_TAGGED_INTRO = re.compile(r'^[ \t]*(?:\\noindent\s*)?(?:\$|\\\()?'
    r'(?P<tag>\((?:\d{1,4}[a-z]*(?:bis|ter)?[\u2032\u2033\'\"]*|[IVX]{1,7})\))'
    r'(?P<suffix>[^\n]{1,600})\n[ \t]*\\diagram\{', re.I | re.M)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for part in iter(lambda:f.read(1024*1024),b''):h.update(part)
    return h.hexdigest()

def normalize(s):return re.sub(r'\s+','',s).replace('\u00a0','')

def tag_text(s):
    # A marginal anchor or dagger may be appended to the equation number in
    # the same extracted line, even though it is only an editorial marker.
    s=re.sub(r'\b[mdi]\d+\b','',s)
    return normalize(unicodedata.normalize('NFKC',s)).replace('\u2236',':').strip('\u2020\u2021')

def lines(page):
    out=[]
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            t=''.join(s['text'] for s in l['spans']).strip()
            if t:
                box=fitz.Rect(l['bbox'])*page.rotation_matrix
                out.append({'text':t,'bbox':list(box)})
    return sorted(out,key=lambda r:(round(r['bbox'][1],2),r['bbox'][0]))

def ignored(line,page):
    t=normalize(line['text']);x0,y0,x1,y1=line['bbox'];w,h=page.rect.width,page.rect.height
    if y0<48 or y1>h-62:return True
    if x0>w-73:return True
    if re.fullmatch(r'[\u2020\u2021\u2022\u22c5.,;:]*',t):return True
    if re.fullmatch(r'[mdi]\d+',t):return True
    if re.match(r'^\[(?:scan|p\.)',t,re.I):return True
    # Manuscript page numbers can be printed without brackets in the outer
    # body column. Mathematical numerals elsewhere are retained as content.
    if re.fullmatch(r'\d{1,4}[a-z]?',t) and x0>w-110:return True
    return False

def page_scans(book,doc=None):
    # Read current PDF annotations when available. A previously generated TSV
    # can describe an older pagination even when the new PDF is already stable.
    if doc is not None:
        out={}
        for page in doc:
            for link in page.get_links():
                match=SCAN_URI.match(link.get('uri',''))
                if match:out.setdefault(page.number+1,set()).add((match[1],int(match[2])))
        return {p:[{'cote':c,'scan':s} for c,s in sorted(v)] for p,v in out.items()}
    path=Path('work/verification')/(book+'.links.tsv');out={}
    if path.exists():
        with path.open(newline='') as f:
            for r in csv.DictReader(f,delimiter='\t'):
                if r.get('cote') and r.get('scan'):
                    out.setdefault(int(r['page']),set()).add((r['cote'],int(r['scan'])))
    return {p:[{'cote':c,'scan':s} for c,s in sorted(v)] for p,v in out.items()}

def source_tagged_introductions(language):
    """Inventory literal source tag introductions directly followed by diagrams.

    Source qualification prevents an arbitrary complete tagged formula with
    a right-hand side from being treated as an unfinished introduction. The
    source text is only read; all candidates still require actual inspection.
    """
    result={}
    index=Path('sources/fr/records/CURRENT_TEXT_INDEX.tsv')
    with index.open(newline='') as f:
        packages=list(csv.DictReader(f,delimiter='\t'))
    for info in packages:
        package=info['package']
        path=Path('sources')/('fr/texts' if language=='fr' else 'en/packages')/(package+('_en' if language=='en' else '')+'.tex')
        source=path.read_text()
        for match in SOURCE_TAGGED_INTRO.finditer(source):
            suffix=re.sub(r'\\(?:quad|qquad|hfill|noindent)\b|\\[()]|\$|\s','',match['suffix'])
            if not suffix:continue
            scan_marks=list(re.finditer(r'\\scanpage\{(\d+)\}',source[:match.start()]))
            if not scan_marks:continue
            scan=int(scan_marks[-1][1]);tag=normalize(match['tag'])
            record={'package':package,'cote':info['cote'],'scan':scan,'tag':tag,
                    'source_path':path.as_posix(),'source_sha256':sha(path),
                    'source_line':source[:match.start()].count('\n')+1,
                    'source_introduction':source[match.start():source.index(r'\diagram{',match.start())].rstrip()}
            result.setdefault((info['cote'],scan,tag),[]).append(record)
    return result

def scan_book(path,old):
    book=path.stem;before=sha(path);doc=fitz.open(path);scans=page_scans(book,doc);found=[]
    introductions=source_tagged_introductions('en' if '_EN_' in book else 'fr')
    for i,page in enumerate(doc):
        ls=lines(page);body=[l for l in ls if not ignored(l,page)]
        for k,l in enumerate(body):
            tag=tag_text(l['text']);map_name=None;source_intro=[]
            if not TAG.fullmatch(tag):
                named=TAG_WITH_MAP.fullmatch(tag)
                if named:
                    tag=named.group('tag');map_name=named.group('map')
                else:
                    prefixed=TAG_PREFIX.fullmatch(tag)
                    if not prefixed:continue
                    for context in scans.get(i+1,[]):
                        source_intro.extend(introductions.get((context['cote'],context['scan'],prefixed['tag']),[]))
                    if not source_intro:continue
                    tag=prefixed['tag']
            if not source_intro:
                for context in scans.get(i+1,[]):
                    source_intro.extend(introductions.get((context['cote'],context['scan'],tag),[]))
            x0,y0,x1,y1=l['bbox'];cy=(y0+y1)/2
            peers=[o for o in body if o is not l and abs((o['bbox'][1]+o['bbox'][3])/2-cy)<max(3.5,(y1-y0)*.42)]
            if peers:
                # TeX's quad can cause MuPDF to extract the adjacent map name
                # as its own same-baseline line; retain the whole introduction.
                if source_intro and all(o['bbox'][0]>=x0 and o['bbox'][0]<=page.rect.width-73 for o in peers):
                    pass
                elif len(peers)==1 and not map_name and MAP_NAME.fullmatch(tag_text(peers[0]['text'])) and 0<=peers[0]['bbox'][0]-x1<=60:
                    map_name=tag_text(peers[0]['text'])
                else:continue
            grouped={id(l),*(id(o) for o in peers)}
            below=[o for o in body if id(o) not in grouped and o['bbox'][1]>=y1-1]
            above=[o for o in body if id(o) not in grouped and o['bbox'][3]<=y0+1]
            direction=None
            if not below and y0>=page.rect.height*.47 and i+1<len(doc):direction='number_before_next_page_display'
            # Trailing source tags may be left-aligned inside a marginal note,
            # as in C3:506 (20bis); a right-half filter would miss them.
            elif not above and y1<=page.rect.height*.24 and i>0:direction='number_after_previous_page_display'
            if not direction:continue
            adjacent=i+1 if direction.startswith('number_before') else i-1
            other=lines(doc[adjacent]);otherbody=[o for o in other if not ignored(o,doc[adjacent])]
            row={'reader':book,'page':i+1,'tag':tag,'direction':direction,'bbox':l['bbox'],
                 'tag_line_text':l['text'],'map_name_suffix':map_name,
                 'same_baseline_introduction_parts':[o['text'] for o in peers] if source_intro else [],
                 'source_tagged_introduction_candidates':source_intro,
                 'prior_lines':[o['text'] for o in body[max(0,k-5):k]],
                 'following_lines':[o['text'] for o in body[k+1:k+6]],
                 'adjacent_page':adjacent+1,'adjacent_text':('\n'.join(o['text'] for o in otherbody[:35]) if adjacent>i else '\n'.join(o['text'] for o in otherbody[-35:])),
                 'scan_context':scans.get(i+1,[]),'adjacent_scan_context':scans.get(adjacent+1,[]),
                 'already_in_original_queue':(book,i+1,tag) in old,'inspection_status':'UNREVIEWED_CANDIDATE'}
            found.append(row)
    pages=len(doc);doc.close();after=sha(path)
    if after!=before:raise RuntimeError('PDF changed during pagination audit: '+book)
    return {'reader':book,'sha256':before,'pages':pages,'stable_during_audit':True,'candidate_count':len(found)},found

def render_pair(row,root):
    path=Path('work/build')/(row['reader']+'.pdf');d=fitz.open(path);p=row['page'];q=row['adjacent_page']
    if q>p:
        seq=[(p,fitz.Rect(0,max(0,row['bbox'][1]-115),d[p-1].rect.width,d[p-1].rect.height)),
             (q,fitz.Rect(0,0,d[q-1].rect.width,min(320,d[q-1].rect.height)))]
    else:
        seq=[(q,fitz.Rect(0,max(0,d[q-1].rect.height-330),d[q-1].rect.width,d[q-1].rect.height)),
             (p,fitz.Rect(0,0,d[p-1].rect.width,min(320,d[p-1].rect.height)))]
    images=[]
    for pn,clip in seq:
        pix=d[pn-1].get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=clip,alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);images.append((pn,im))
    width=sum(im.width for _,im in images)+24;height=max(im.height for _,im in images)+72
    sheet=Image.new('RGB',(width,height),'#e9edf1');draw=ImageDraw.Draw(sheet);x=8
    for pn,im in images:
        draw.text((x,7),row['reader']+' | physical '+str(pn)+' | tag '+row['tag'],fill='black')
        sheet.paste(im,(x,36));x+=im.width+8
    safe=re.sub(r'[^a-zA-Z0-9]+','',row['tag']);f=root/(row['reader']+f'_p{p:04}_{safe}.png')
    sheet.save(f);d.close()
    row['native_pair_image']=f.as_posix();row['native_pair_image_sha256']=sha(f)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--book',action='append',choices=BOOKS)
    ap.add_argument('--output',default='work/data/equation_tag_pagination_expanded.json')
    ap.add_argument('--render-new',action='store_true');ap.add_argument('--render-dir',default='work/visual_repair_proofs/pagination_expanded')
    a=ap.parse_args();oldpath=Path('work/data/equation_tag_pagination_candidates.json')
    olddata=json.loads(oldpath.read_text()) if oldpath.exists() else []
    old={(r['reader'],int(r['page']),normalize(r['tag'])) for r in olddata}
    files=[];rows=[]
    for book in a.book or BOOKS:
        f,r=scan_book(Path('work/build')/(book+'.pdf'),old);files.append(f);rows.extend(r)
        print(book,':',len(r),'candidates;',sum(not x['already_in_original_queue'] for x in r),'new',flush=True)
    if a.render_new:
        root=Path(a.render_dir);root.mkdir(parents=True,exist_ok=True)
        for r in rows:
            if not r['already_in_original_queue'] and 'master' not in r['reader']:render_pair(r,root)
    result={'status':'CANDIDATES_REQUIRE_VISUAL_AND_SOURCE_REVIEW','generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'scope':'All pages of the named publication PDFs. Bare equation numbers, equation numbers followed by a one-letter map name and colon, and source-qualified tagged introductions directly followed by a diagram are checked at page ends/starts, at every horizontal position. Same-baseline text split by MuPDF is retained. Source qualification uses the exact package, cote, scan, tag and literal introduction. Footers, marginal scan and manuscript-page markers, source anchors, and isolated daggers are excluded. A candidate is not automatically a defect.',
       'files':files,'candidate_count':len(rows),'new_candidate_count':sum(not r['already_in_original_queue'] for r in rows),'candidates':rows}
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':a.output,'candidates':len(rows),'new':result['new_candidate_count']}))

if __name__=='__main__':main()
