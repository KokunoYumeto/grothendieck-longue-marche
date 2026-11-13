#!/usr/bin/env python3
"""Verify a La Longue Marche reader, including every page and every marked link.

Inputs are a PDF and its adjacent .log, .lm-links.tsv and .lm-scans.tsv files.
The custom /NM identifiers in PDF link annotations are independently matched
against the LuaTeX mark-expansion trace. Parent coverage intentionally counts
once for every explicit descendant in an annotation, matching book_links.lua;
therefore mark-run totals are not confused with the PDF annotation count.

Usage:
 python scripts/verify_pdf.py build/LM_FR_diplomatique.pdf --render
 python scripts/verify_pdf.py build/LM_EN_reading.pdf --before-log records/before.log

All output paths in records are filenames or relative artifact paths. Visual
review templates are marked pending: rendering is never claimed as inspection.
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,json,math,re
from pathlib import Path
from urllib.parse import urlparse,parse_qs
import pymupdf as fitz
from PIL import Image,ImageDraw,ImageFont
import page_bounds_20261113 as bounds

ROOT=Path(__file__).resolve().parents[2]
DEFAULT_EXPECTED={'140-1':37,'140-2':575,'140-3':696,'140-4':280}
URI_RE=re.compile(r'^https://grothendieck\.umontpellier\.fr/web/viewer\.html\?file=\.\./(140-[1-4])\.pdf#page=(\d+)$')

def sha256(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def sanitize(s):
    # A mathematical map such as f:\mathcal must not be mistaken for a
    # Windows drive path. Match recognizable absolute filesystem roots only.
    s=re.sub(r'(?<![\w\\])[A-Za-z]:\\(?:Users|Windows|Program Files(?: \(x86\))?|texlive|workspace|home|Temp|tmp)(?:\\[^\s\n]*)?', '[local path omitted]', s, flags=re.I)
    s=re.sub(r'/(?:workspace|home|root|usr|opt|tmp|var)/[^\s\n]+','[local path omitted]',s)
    s=re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[address omitted]',s)
    return s

def parse_log(path):
    path=Path(path)
    if not path.exists():return {'file':path.name,'present':False,'errors':['Build log not present.']}
    raw=path.read_text(errors='replace')
    # TeX can wrap in the middle of a field; preserve original lines for location
    # and remove only wrapping inside the bounded diagnostic's next 240 chars.
    boxes=[]
    for m in re.finditer(r'Overfull\s+\\([hv])box\s*\(',raw):
        snippet=raw[m.start():m.start()+450]
        joined=snippet.replace('\r','').replace('\n','')
        n=re.match(r'Overfull\s+\\([hv])box\s*\(([\d.]+)pt too (wide|high)\)(.*)',joined)
        if not n:continue
        loc=re.search(r'(?:at lines?|detected at line)\s*(-?\d+)(?:--(-?\d+))?',n.group(4))
        boxes.append({'kind':n.group(1)+'box','pt':float(n.group(2)),'direction':n.group(3),
          'first_line':int(loc.group(1)) if loc else None,'last_line':int(loc.group(2)) if loc and loc.group(2) else None,
          'log_line':raw.count('\n',0,m.start())+1,'message':sanitize(n.group(0)[:230])})
    missing=[]
    for m in re.finditer(r'^Missing character:',raw,re.M):
        following=raw[m.start():].splitlines();msg=following[0]
        if len(following)>1 and not following[1].startswith(('Missing character:','[','!','Overfull','Underfull')):msg+=' '+following[1]
        missing.append(sanitize(msg))
    errors=[sanitize(m.group(0)) for m in re.finditer(r'^! .+|^(?:LaTeX|Package [^\n]+|Class [^\n]+) Error:.*',raw,re.M)]
    if 'Fatal error occurred' in raw and not errors:errors.append('Fatal error occurred.')
    warnings=[sanitize(m.group(0)) for m in re.finditer(r'^(?:LaTeX(?: Font)?|Package [^\n]+?|Class [^\n]+?) Warning:.*',raw,re.M)]
    undefined=[x for x in warnings if re.search(r'\b(?:references?|citations?)\b',x,re.I) and re.search(r'undefined|not defined',x,re.I)]
    runtime=None
    m=re.search(r'LM-AUDIT\s',raw)
    if m:
        chunk=raw[m.start():m.start()+650].replace('\n','').replace('\r','')
        fields=re.findall(r'([a-z_]+)=(\d+)',chunk)
        runtime={k:int(v) for k,v in fields}
    return {'file':path.name,'present':True,'overfull_count':len(boxes),
      'overfull_gt_2pt':sum(x['pt']>2 for x in boxes),'maximum_overfull_pt':max((x['pt'] for x in boxes),default=0),
      'overfull_boxes':boxes,'missing_character_count':len(missing),'missing_characters':missing,
      'error_count':len(errors),'errors':errors,'warning_count':len(warnings),'warnings':warnings,
      'undefined_reference_warnings':undefined,'underfull_count':len(re.findall(r'Underfull\s+\\[hv]box',raw)),
      'output_written':bool(re.search(r'Output written on ',raw)),'lm_audit':runtime}

def read_trace(path):
    if not Path(path).exists():return None
    with Path(path).open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    out={}
    for row in rows:
        marker=int(row.get('marker',row.get('mark_id',row.get('id','0'))))
        pages=row.get('physical_pages',row.get('physical_page',row.get('page','')))
        out[marker]={'marker':marker,'kind':row.get('kind',''),'cote':row.get('cote',''),'scan':int(row.get('scan',0)),
          'tex_line':int(row.get('tex_line',0)),'parent':int(row.get('parent',0)),
          'source_id':row.get('source_id',''),'expansions':int(row.get('expansions',1)),
          'linked_runs':int(row.get('linked_runs',row.get('annotation_count',row.get('segments',0)))),
          'physical_pages':sorted({int(x) for x in re.split('[,; ]+',pages) if x})}
    return out

def pdf_links(doc):
    rows=[]
    for pno,page in enumerate(doc,1):
        for link in page.get_links():
            if link.get('kind')!=fitz.LINK_URI:continue
            uri=link.get('uri','');match=URI_RE.fullmatch(uri)
            xref=link.get('xref',0);nm=''
            if xref:
                k,v=doc.xref_get_key(xref,'NM')
                if k=='string':nm=v
            ids=[]
            if re.fullmatch(r'LM\d+(?:,\d+)*',nm):ids=[int(x) for x in nm[2:].split(',')]
            rows.append({'page':pno,'xref':xref,'uri':uri,'rectangle':list(link['from']),
              'annotation_name':nm,'markers':ids,'cote':match.group(1) if match else '',
              'scan':int(match.group(2)) if match else None,'is_scan':bool(match)})
    return rows

def audit_links(rows,trace,expected,runtime=None,npages=None):
    scans=[r for r in rows if r['is_scan']]
    per_cote={};scan_pages=collections.defaultdict(set)
    for row in scans:scan_pages[f"{row['cote']}:{row['scan']}"] .add(row['page'])
    for cote,count in expected.items():
        actual={r['scan'] for r in scans if r['cote']==cote}
        per_cote[cote]={'expected_distinct_scans':count,'actual_distinct_scans':len(actual),
          'missing_scans':sorted(set(range(1,count+1))-actual),'unexpected_scans':sorted(actual-set(range(1,count+1))),
          'annotation_count':sum(r['cote']==cote for r in scans)}
    problems=[];run_counts=collections.Counter();pages=collections.defaultdict(set);unknown=set();target_mismatches=[]
    if trace is None:problems.append('No mark-expansion trace: individual mark completeness is not established.')
    else:
        for row in scans:
            if not row['markers']:problems.append(f"Archive link without a recognized marker identifier on PDF page {row['page']} (annotation {row['xref']}).")
            for marker in row['markers']:
                node=marker;visited=set()
                while node:
                    if node in visited:problems.append(f'Cycle in parent chain at marker {node}.');break
                    visited.add(node)
                    if node not in trace:unknown.add(node);break
                    m=trace[node];run_counts[node]+=1;pages[node].add(row['page'])
                    if m['cote']!=row['cote'] or m['scan']!=row['scan']:
                        target_mismatches.append({'marker':node,'page':row['page'],'expected_cote':m['cote'],'expected_scan':m['scan'],'actual_cote':row['cote'],'actual_scan':row['scan']})
                    node=m['parent']
        for marker in sorted(unknown):problems.append(f'PDF refers to unknown marker {marker}.')
    per_kind=collections.defaultdict(lambda:{'expanded_marks':0,'pdf_linked_marks':0,'unlinked_marks':0,'trace_run_mismatches':0,'trace_page_mismatches':0})
    per_cote_marks=collections.defaultdict(collections.Counter);mismatches=[]
    if trace is not None:
        for marker,m in trace.items():
            k=per_kind[m['kind']];k['expanded_marks']+=1;per_cote_marks[m['cote']][m['kind']]+=1
            if run_counts[marker]>0:k['pdf_linked_marks']+=1
            else:k['unlinked_marks']+=1
            if run_counts[marker]!=m['linked_runs']:
                k['trace_run_mismatches']+=1;mismatches.append({'marker':marker,'kind':'run count','trace':m['linked_runs'],'pdf_reconstructed':run_counts[marker]})
            if sorted(pages[marker])!=m['physical_pages']:
                k['trace_page_mismatches']+=1;mismatches.append({'marker':marker,'kind':'page set','trace':m['physical_pages'],'pdf_reconstructed':sorted(pages[marker])})
        if any(k['unlinked_marks'] for k in per_kind.values()):problems.append('One or more expanded marked readings have no reconstructed PDF link.')
        if mismatches:problems.append('Mark trace differs from independently reconstructed PDF annotation coverage.')
        if target_mismatches:problems.append('One or more marker IDs point to a different scan in the PDF.')
    malformed=[r for r in rows if 'grothendieck.umontpellier.fr/web/viewer' in r['uri'] and not r['is_scan']]
    if malformed:problems.append('One or more archive viewer URIs do not follow the required exact pattern.')
    runtime_checks={}
    if runtime:
        pairs={'links':len(scans),'markers':len(trace) if trace is not None else None,
          'unlinked':sum(k['unlinked_marks'] for k in per_kind.values()),'scans':len(scan_pages),'pages':npages}
        for name,value in pairs.items():
            if name in runtime and value is not None:
                runtime_checks[name]={'log':runtime[name],'pdf_or_trace':value,'agrees':runtime[name]==value}
                if runtime[name]!=value:problems.append(f'LM-AUDIT {name} disagrees with PDF/trace count.')
    complete_scans=all(not v['missing_scans'] and not v['unexpected_scans'] for v in per_cote.values())
    return {'total_external_uri_links':len(rows),'archive_scan_links':len(scans),'distinct_scan_pages':len(scan_pages),
      'physical_pages_with_scan_links':len({r['page'] for r in scans}),'per_cote':per_cote,
      'expanded_marker_count':len(trace) if trace is not None else None,
      'distinct_source_ids':len({m['source_id'] for m in trace.values() if m.get('source_id')}) if trace is not None else None,
      'macro_expansion_count':sum(m.get('expansions',1) for m in trace.values()) if trace is not None else None,'per_kind':dict(per_kind),
      'marks_by_cote':{k:dict(v) for k,v in per_cote_marks.items()},'scan_to_physical_pages':{k:sorted(v) for k,v in scan_pages.items()},
      'malformed_scan_uris':malformed,'unknown_markers':sorted(unknown),'trace_mismatches':mismatches,
      'wrong_scan_targets':target_mismatches,'runtime_summary_checks':runtime_checks,'problems':problems,
      'scan_coverage_complete':complete_scans,'individual_mark_links_complete':trace is not None and not problems}

def audit_source_ids(pdf,trace):
    """Validate shipped IDs against literal source instrumentation.

    The common body contains alternate branches for three edition forms; an
    unexecuted literal branch is not a missing shipped mark. This therefore
    validates all expanded runtime IDs without asserting all literal IDs expand.
    """
    lang='en' if '_EN_' in Path(pdf).stem else 'fr' if '_FR_' in Path(pdf).stem else None
    path=Path(pdf).with_suffix('.tex')
    if path.exists():
        body=path.read_text();records=[]
        cotes=list(re.finditer(r'\\LMcote\{(140-[1-4])\}',body))
        scans=list(re.finditer(r'\\scanpage\{(\d+)\}',body))
        pattern=re.compile(r'\\LMsourceMark\{(M\d+)\}\{\s*\\(unsure|illegible|LMdoubtcopy|LMcancelledDoubts|LMuncertaindeletion|scanpage|margin|mspage)\b\s*\{')
        ci=si=0;cote='';scan=''
        for m in pattern.finditer(body):
            while ci<len(cotes) and cotes[ci].start()<m.end():cote=cotes[ci][1];ci+=1
            while si<len(scans) and scans[si].start()<m.end():scan=scans[si][1];si+=1
            records.append({'id':m[1],'kind':m[2],'cote':cote,'scan':scan})
        inventory_method='Literal LMsourceMark calls in this PDF’s adjacent TeX source.'
    else:
        path=Path(pdf).parent/(str(lang)+'_source_marks.json')
        records=json.loads(path.read_text()) if lang and path.exists() else None
        inventory_method='Fallback shared language instrumentation JSON; ensure it belongs to this build.'
    if records is None:
        return {'present':False,'file':path.name if lang else None,'complete':False,
          'problems':['Literal source instrumentation inventory not present.']}
    source={r['id']:r for r in records};problems=[];mismatches=[]
    if len(source)!=len(records):problems.append('Duplicate literal source IDs in instrumentation inventory.')
    if trace is None:
        return {'present':True,'file':path.name,'complete':False,'problems':['No runtime mark trace to compare.']}
    mapping={'scanpage':'scan','unsure':'unsure','illegible':'illegible','LMdoubtcopy':'residual-unsure',
      'LMcancelledDoubts':'cancelled-anchor','LMuncertaindeletion':'cancelled-anchor'}
    ids=collections.Counter(m.get('source_id','') for m in trace.values())
    duplicates=sorted(k for k,v in ids.items() if v>1)
    if duplicates:problems.append('A literal source ID is assigned multiple runtime marker IDs.')
    for marker,m in trace.items():
        sid=m.get('source_id','');s=source.get(sid)
        if s is None:
            mismatches.append({'marker':marker,'source_id':sid,'error':'source ID absent from literal inventory'});continue
        comparisons={'kind':(m['kind'],mapping.get(s['kind'])), 'cote':(m['cote'],s['cote']),
          'scan':(m['scan'],int(s['scan']) if str(s['scan']).isdigit() else None)}
        bad={k:{'runtime':a,'literal_source':b} for k,(a,b) in comparisons.items() if a!=b}
        if bad:mismatches.append({'marker':marker,'source_id':sid,'mismatches':bad})
    if mismatches:problems.append('Runtime marker metadata disagrees with literal source instrumentation.')
    return {'present':True,'file':path.name,'sha256':sha256(path),'literal_source_records':len(records),
      'runtime_marker_records':len(trace),'distinct_runtime_source_ids':len(ids),'duplicates':duplicates,
      'mismatches':mismatches,'problems':problems,'complete':not problems,
      'inventory_method':inventory_method,
      'scope':'All expanded runtime IDs checked; unexecuted alternate edition branches are not omissions.'}

def selected_pages(npages,linkaudit,bbox,site_files,spread=40,language=None):
    chosen=collections.defaultdict(set);unmapped=[]
    scanmap={k:set(v) for k,v in linkaudit['scan_to_physical_pages'].items()}
    scanorder=sorted(scanmap,key=lambda k:(int(k.split(':')[0].split('-')[-1]),int(k.split(':')[1])))
    nextscan={key:scanorder[i+1] if i+1<len(scanorder) else None for i,key in enumerate(scanorder)}
    for filename in site_files:
        path=Path(filename)
        if not path.exists():continue
        data=json.loads(path.read_text());data=data if isinstance(data,list) else data.get('sites',[])
        for i,row in enumerate(data,1):
            if path.name=='layout_repairs_applied.json':
                if row.get('kind')=='empty diagram cell':continue
                if language and row.get('language') not in (None,language):continue
            cote=row.get('cote');scan=row.get('scan')
            if not cote or scan is None:continue
            scan=int(scan);key=f'{cote}:{scan}';pages=scanmap.get(key,set())
            label=f"{path.name}:{row.get('record',i)} {key}"
            if not pages:unmapped.append({'site_file':path.name,'record':row.get('record',i),'cote':cote,'scan':scan});continue
            start,end=min(pages),max(pages)
            nextpages=scanmap.get(nextscan.get(key),set())
            if nextpages:end=max(end,min(nextpages))
            elif nextscan.get(key) is None:end=npages
            for page in range(start,min(npages,end)+1):chosen[page].add(label)
    for page in bbox['landscape_pages']:chosen[page].add('landscape page')
    for page in bbox['off_sheet_pages']:chosen[page].add('ink beyond sheet: inspect and repair')
    for page in bbox['outside_type_area_pages']:chosen[page].add('ink outside type area: inspect and repair or verify single letter')
    if npages:
        for i in range(min(spread,npages)):
            p=1+round(i*(npages-1)/max(1,min(spread,npages)-1));chosen[p].add('evenly spaced sample')
    return [{'page':p,'reasons':sorted(why)} for p,why in sorted(chosen.items())],unmapped

def close_review_pages(selected,bbox,site_files):
    """Identify selected pages requiring individual-image or close-sheet review."""
    sites={}
    for filename in site_files:
        path=Path(filename)
        if not path.exists():continue
        data=json.loads(path.read_text());data=data if isinstance(data,list) else data.get('sites',[])
        for i,row in enumerate(data,1):sites[(path.name,str(row.get('record',i)))]=row
    result=[]
    for item in selected:
        reasons=[]
        for reason in item['reasons']:
            if reason.startswith(('landscape','ink beyond','ink outside')):reasons.append(reason);continue
            m=re.match(r'([^:]+):(\d+)\s',reason)
            if not m:continue
            source,record=m.groups();site=sites.get((source,record),{})
            if source=='layout_pass_sites.json':reasons.append('Previous scaling/rotation: '+reason)
            elif source=='layout_repairs_applied.json':reasons.append('Current '+site.get('kind','layout repair')+': '+reason)
            elif source=='layout_before_sites.json':
                kind=site.get('kind','').lower()
                if 'display' in kind or 'tikzcd' in kind or float(site.get('pt_too_wide',0) or 0)>25:
                    reasons.append('Prior mathematical or large overflow: '+reason)
        if reasons:result.append({'page':item['page'],'reasons':sorted(set(reasons)),
          'full_page_image':f"page_{item['page']:04d}.png"})
    return result

def font(size):
    try:return ImageFont.truetype('DejaVuSans.ttf',size)
    except OSError:return ImageFont.load_default()

REVIEW_FIELDS=['page','pdf_sha256','reasons','full_page_image','contact_sheet','overview_sheet',
  'image_width','image_height','rendered_pixel_sha256','png_sha256','status','reviewer','observations',
  'review_basis','reviewed_at_utc','review_carryover_from_pdf_sha256','review_reference_pdf',
  'review_reference_pdf_sha256','review_reference_page','review_reference_pixel_sha256',
  'review_reference_png_sha256','review_reference_image']

def pixmap_pixel_sha256(pix):
    if pix.n!=3:raise ValueError('Review raster must be RGB without alpha.')
    return hashlib.sha256(f'RGB:{pix.width}:{pix.height}:'.encode()+pix.samples).hexdigest()

def image_pixel_sha256(path):
    with Image.open(path) as im:
        rgb=im.convert('RGB')
        return hashlib.sha256(f'RGB:{rgb.width}:{rgb.height}:'.encode()+rgb.tobytes()).hexdigest()

def review_is_attributed(row):
    return row.get('status')=='reviewed' and bool(row.get('reviewer','').strip()) and bool(row.get('observations','').strip())

def short_reasons(item):
    reasons=[]
    for r in item['reasons']:
        group='prior overflow' if r.startswith('layout_before') else 'prior fit pass' if r.startswith('layout_pass') else 'current layout repair' if r.startswith('layout_repairs') else r
        if group not in reasons:reasons.append(group)
    return '; '.join(reasons)

def render_selected(pdf,selected,outdir,pdfhash,width=900):
    outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    oldfile=outdir/'VISUAL_REVIEW.tsv';old={}
    if oldfile.exists():
        with oldfile.open(newline='') as f:
            old={int(r['page']):r for r in csv.DictReader(f,delimiter='\t')}
    rows=[];pages=[];image_info={}
    with fitz.open(pdf) as doc:
        for item in selected:
            page=doc[item['page']-1]
            pix=page.get_pixmap(matrix=fitz.Matrix(width/page.rect.width,width/page.rect.width),colorspace=fitz.csRGB,alpha=False)
            filename=f"page_{item['page']:04d}.png";pix.save(outdir/filename)
            image_info[item['page']]={'image_width':pix.width,'image_height':pix.height,
              'rendered_pixel_sha256':pixmap_pixel_sha256(pix),'png_sha256':sha256(outdir/filename)}
            pages.append((item,filename))
    sheet_names={}
    for index in range(0,len(pages),4):
        chunk=pages[index:index+4];imgs=[Image.open(outdir/n).convert('RGB') for _,n in chunk]
        maxheight=max(im.height for im in imgs);tileh=maxheight+62;tilew=width+16
        canvas=Image.new('RGB',(tilew*2,tileh*2+42),'#d7d7d7');draw=ImageDraw.Draw(canvas)
        draw.text((12,8),f'{Path(pdf).stem} | sheet {index//4+1}',fill='black',font=font(19))
        sheet=f'sheet_{index//4+1:03d}.png'
        for j,((item,n),im) in enumerate(zip(chunk,imgs)):
            x=(j%2)*tilew+8;y=(j//2)*tileh+42
            title=f"Page {item['page']} | "+short_reasons(item)
            draw.text((x,y+4),title[:110],fill='black',font=font(16))
            canvas.paste(im,(x,y+36));sheet_names[item['page']]=sheet
        canvas.save(outdir/sheet,optimize=True)
        for im in imgs:im.close()
    overview_names={};overview_width=550
    for index in range(0,len(pages),16):
        chunk=pages[index:index+16];imgs=[]
        for item,n in chunk:
            with Image.open(outdir/n) as original:
                rgb=original.convert('RGB');im=rgb.resize((overview_width,round(rgb.height*overview_width/rgb.width)),Image.Resampling.LANCZOS)
                imgs.append(im)
        tileh=max(im.height for im in imgs)+46;tilew=overview_width+16
        canvas=Image.new('RGB',(tilew*4,tileh*4+42),'#d7d7d7');draw=ImageDraw.Draw(canvas)
        draw.text((12,8),f'{Path(pdf).stem} | overview {index//16+1} | selected pages',fill='black',font=font(19))
        name=f'overview_{index//16+1:03d}.png'
        for j,((item,n),im) in enumerate(zip(chunk,imgs)):
            x=(j%4)*tilew+8;y=(j//4)*tileh+42
            draw.text((x,y+2),f"Page {item['page']} | "+short_reasons(item)[:65],fill='black',font=font(15))
            canvas.paste(im,(x,y+28));overview_names[item['page']]=name
        canvas.save(outdir/name,optimize=True)
        for im in imgs:im.close()
    carried=0;reset=0;history=[]
    for item,n in pages:
        pno=item['page'];prior=old.get(pno,{});info=image_info[pno]
        keep=review_is_attributed(prior) and all(prior.get(k)==info[k] for k in ('rendered_pixel_sha256','png_sha256'))
        row={k:'' for k in REVIEW_FIELDS}
        row.update({'page':pno,'pdf_sha256':pdfhash,'reasons':'; '.join(item['reasons']),
          'full_page_image':n,'contact_sheet':sheet_names[pno],'overview_sheet':overview_names[pno],**info,'status':'pending'})
        if keep:
            row.update({k:prior.get(k,'') for k in REVIEW_FIELDS[10:]})
            row['review_basis']=row.get('review_basis') or 'Direct visual inspection recorded previously.'
            if prior.get('pdf_sha256')!=pdfhash:
                row['review_carryover_from_pdf_sha256']=prior['pdf_sha256']
                row['review_basis']='Previously reviewed page; identical RGB pixels and PNG file after rebuild.'
                carried+=1
                history.append({'page':pno,'action':'carry reviewed status across identical raster','old_review':prior,
                  'new_pdf_sha256':pdfhash,'new_rendered_pixel_sha256':info['rendered_pixel_sha256']})
        elif review_is_attributed(prior):
            reset+=1
            history.append({'page':pno,'action':'reset review: rendered image changed or prior image hashes absent',
              'old_review':prior,'new_pdf_sha256':pdfhash,'new_rendered_pixel_sha256':info['rendered_pixel_sha256']})
        rows.append(row)
    if sha256(pdf)!=pdfhash:raise RuntimeError('PDF changed during rendering; review records were not updated.')
    if history:
        with (outdir/'REVIEW_HISTORY.jsonl').open('a') as f:
            for record in history:f.write(json.dumps(record,ensure_ascii=False)+'\n')
    with oldfile.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=REVIEW_FIELDS,delimiter='\t');w.writeheader();w.writerows(rows)
    return {'rendered_pages':len(rows),'contact_sheets':math.ceil(len(rows)/4),'image_width_pixels':width,
      'overview_sheets':math.ceil(len(rows)/16),'overview_page_width_pixels':overview_width,
      'reviewed_pages':sum(r['status']=='reviewed' for r in rows),'review_record':'VISUAL_REVIEW.tsv',
      'reviews_carried_across_identical_renders':carried,'reviews_reset_after_image_change':reset,
      'rendering_is_not_visual_inspection':True}


def read_visual_review(directory,pdfhash,selected):
    directory=Path(directory);path=directory/'VISUAL_REVIEW.tsv';rows={}
    if path.exists():
        with path.open(newline='') as f:
            rows={int(r['page']):r for r in csv.DictReader(f,delimiter='\t') if r.get('pdf_sha256')==pdfhash}
    required={x['page'] for x in selected}
    rendered=set();bad=[]
    for p,r in rows.items():
        image=directory/r.get('full_page_image','')
        if not image.is_file():continue
        if sha256(image)!=r.get('png_sha256') or image_pixel_sha256(image)!=r.get('rendered_pixel_sha256'):
            bad.append(p);continue
        rendered.add(p)
    reviewed={p for p,r in rows.items() if review_is_attributed(r) and p in rendered}
    return {'selected_pages':len(required),'rendered_pages':len(required & rendered),
      'reviewed_pages':len(required & reviewed),'pending_pages':sorted(required-reviewed),
      'image_hash_mismatch_pages':sorted(required & set(bad)),
      'complete':required<=reviewed and required<=rendered,'review_record':'VISUAL_REVIEW.tsv',
      'rendering_is_not_visual_inspection':True}

def accepted_letter_overhangs(exceptions,pdfname,pdfhash,bbox):
    accepted=[];rejected=[]
    for ex in exceptions or []:
        if ex.get('file')!=pdfname:continue
        pno=int(ex.get('page',0));reason=None
        if ex.get('pdf_sha256')!=pdfhash:reason='PDF hash differs.'
        elif not 1<=pno<=bbox['pages']:reason='Page is absent.'
        elif ex.get('kind')!='single-letter-overhang':reason='Only single-letter overhang is an allowed exception.'
        elif len(ex.get('character',''))!=1 or not ex['character'].isalpha():reason='One alphabetic character must be identified.'
        elif not ex.get('reason') or not ex.get('reviewed_by'):reason='Visual review attribution and reason are required.'
        else:
            row=bbox['page_results'][pno-1]
            if row['off_sheet']:reason='Ink beyond the sheet is never an allowed letter-overhang exception.'
            elif not row['outside_type_area']:reason='Page has no type-area overhang to except.'
            elif any(o['kind'] not in ('fill-text','stroke-text') for o in row['offending_objects']):reason='A non-text painted object also exceeds the type area.'
        if reason:rejected.append({**ex,'rejection':reason})
        else:accepted.append(ex)
    return accepted,rejected

def write_rows(path,rows,fields):
    with Path(path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader()
        for r in rows:w.writerow({k:json.dumps(r.get(k),ensure_ascii=False) if isinstance(r.get(k),(list,dict)) else r.get(k,'') for k in fields})

def verify(pdf,outdir,geometry=None,before_log=None,site_files=(),expected=None,render=False,spread=40,width=900,exceptions=None):
    pdf=Path(pdf);outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True);stem=pdf.stem
    pdfhash=sha256(pdf);log=parse_log(pdf.with_suffix('.log'));before=parse_log(before_log) if before_log else None
    bbox=bounds.analyze(pdf,geometry)
    with fitz.open(pdf) as doc:links=pdf_links(doc)
    trace=read_trace(pdf.with_suffix('.lm-links.tsv'))
    la=audit_links(links,trace,expected or DEFAULT_EXPECTED,log.get('lm_audit'),bbox['pages'])
    source_ids=audit_source_ids(pdf,trace)
    language='en' if '_EN_' in stem else 'fr' if '_FR_' in stem else None
    selected,unmapped=selected_pages(bbox['pages'],la,bbox,site_files,spread,language)
    close_pages=close_review_pages(selected,bbox,site_files)
    verification={'file':pdf.name,'sha256':pdfhash,'pages':bbox['pages'],'log_before':before,'log_after':log,
      'page_bounds':{k:v for k,v in bbox.items() if k!='page_results'},'links':la,'source_id_validation':source_ids,
      'selected_pages':selected,'close_review_pages':close_pages,'unmapped_prior_sites':unmapped,
      'visual_review':{'status':'pending','selected_pages':len(selected),'rendered_pages':0,'reviewed_pages':0},
      'gates':{'compile_without_errors':log.get('present',False) and log.get('error_count',1)==0 and log.get('output_written',False),
        'no_overfull_gt_2pt':log.get('overfull_gt_2pt',1)==0,'no_missing_characters':log.get('missing_character_count',1)==0,
        'no_ink_beyond_sheet':not bbox['off_sheet_pages'],'no_ink_outside_type_area':not bbox['outside_type_area_pages'],
        'complete_scan_link_coverage':la['scan_coverage_complete'],'every_expanded_mark_linked':la['individual_mark_links_complete'],
        'every_prior_site_mapped':not unmapped,'runtime_source_ids_verified':source_ids['complete'],'visual_review_complete':False}}
    if render:render_selected(pdf,selected,outdir/stem,pdfhash,width)
    verification['visual_review']=read_visual_review(outdir/stem,pdfhash,selected)
    verification['gates']['visual_review_complete']=verification['visual_review']['complete']
    accepted,rejected=accepted_letter_overhangs(exceptions,pdf.name,pdfhash,bbox)
    verification['accepted_single_letter_overhangs']=accepted
    verification['rejected_overhang_exceptions']=rejected
    accepted_pages={int(x['page']) for x in accepted}
    verification['gates']['no_unexplained_ink_outside_type_area']=set(bbox['outside_type_area_pages'])<=accepted_pages and not rejected
    bounds.write_tsv(bbox,outdir/(stem+'.page_bounds.tsv'))
    (outdir/(stem+'.page_bounds.json')).write_text(json.dumps(bbox,ensure_ascii=False,indent=2)+'\n')
    write_rows(outdir/(stem+'.links.tsv'),links,['page','xref','uri','rectangle','annotation_name','markers','cote','scan','is_scan'])
    write_rows(outdir/(stem+'.SELECTED_PAGES.tsv'),selected,['page','reasons'])
    write_rows(outdir/(stem+'.CLOSE_REVIEW_PAGES.tsv'),close_pages,['page','reasons','full_page_image'])
    (outdir/(stem+'.verification.json')).write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n')
    return verification

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('pdf',nargs='+');ap.add_argument('--output-dir',default=str(ROOT/'work/verification'))
    ap.add_argument('--geometry');ap.add_argument('--before-log');ap.add_argument('--site-file',action='append')
    ap.add_argument('--expected');ap.add_argument('--exceptions');ap.add_argument('--render',action='store_true');ap.add_argument('--spread',type=int,default=40);ap.add_argument('--width',type=int,default=900)
    a=ap.parse_args();geometry=json.loads(Path(a.geometry).read_text()) if a.geometry else None
    expected=json.loads(Path(a.expected).read_text()) if a.expected else None
    exceptions=json.loads(Path(a.exceptions).read_text()) if a.exceptions else None
    sites=a.site_file or [ROOT/'work/data/layout_before_sites.json',ROOT/'work/data/layout_pass_sites.json',ROOT/'work/data/layout_repairs_applied.json']
    for pdf in a.pdf:
        r=verify(pdf,a.output_dir,geometry,a.before_log,sites,expected,a.render,a.spread,a.width,exceptions)
        print(json.dumps({'file':r['file'],'pages':r['pages'],'overfull_gt_2pt':r['log_after'].get('overfull_gt_2pt'),
         'widest_overfull_pt':r['log_after'].get('maximum_overfull_pt'),'missing_characters':r['log_after'].get('missing_character_count'),
         'off_sheet_pages':len(r['page_bounds']['off_sheet_pages']),'outside_type_area_pages':len(r['page_bounds']['outside_type_area_pages']),
         'scan_links':r['links']['archive_scan_links'],'distinct_scans':r['links']['distinct_scan_pages'],
         'unlinked_expanded_marks':sum(x['unlinked_marks'] for x in r['links']['per_kind'].values()),
         'link_problems':len(r['links']['problems']),'selected_pages':len(r['selected_pages']),
         'rendered_pages':r['visual_review'].get('rendered_pages',0),'gates':r['gates']},ensure_ascii=False))
if __name__=='__main__':main()
