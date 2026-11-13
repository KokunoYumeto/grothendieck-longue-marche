#!/usr/bin/env python3
"""All-page ink bounds, adapted from typeset/scripts/page_bounds_20261113.py.

The supplied script invokes `mutool draw -F bbox`. This version calls the same
native MuPDF fz_new_bbox_device through PyMuPDF, without raster clipping or a
substitute text bounding box. It checks the union of every painted object.

For pdflscape pages the bounding device receives the PDF derotation matrix.
Checks therefore use the original article-sheet coordinates: the landscape
body lies in the original block and the article footer retains its ordinary
position. Display orientation and dimensions are recorded separately.

Default geometry preserves the supplied test: 25 mm margins, a 20 mm right
note column separated by 10 pt, 12 pt head allowance, footer baseline 30 pt
below the text block plus 3 pt ink allowance. Tolerance 1.5 pt for type-area
edges and 0.5 pt for the sheet. No overflow is suppressed as a letter overhang;
possible one-letter cases are only diagnostics requiring visual review.

Usage: python scripts/page_bounds_20261113.py READER.pdf --list
       python scripts/page_bounds_20261113.py READER.pdf --json OUT.json --tsv OUT.tsv
"""
from __future__ import annotations
import argparse,csv,json,math
from pathlib import Path
import pymupdf as fitz

MM=72/25.4
TOL=1.5
SHEET_TOL=0.5
DEFAULT_GEOMETRY={
    'margin_left_mm':25.0,'margin_right_mm':25.0,
    'margin_top_mm':25.0,'margin_bottom_mm':25.0,
    'marginpar_width_mm':20.0,'marginpar_sep_pt':10.0,
    'head_allowance_pt':12.0,'footskip_pt':30.0,'footer_ink_allowance_pt':3.0,
    'type_tolerance_pt':TOL,'sheet_tolerance_pt':SHEET_TOL,
}

def _round(v):return round(float(v),5)
def _rect(rect):return [_round(v) for v in rect]

def ink_bbox(page):
    """Native MuPDF bbox device; coordinates match the unrotated sheet."""
    m=fitz.mupdf
    bbox=m.FzRect(m.fz_empty_rect)
    device=m.fz_new_bbox_device(bbox)
    try:
        matrix=fitz.JM_matrix_from_py(page.derotation_matrix)
        m.fz_run_page(page.this,device,matrix,m.FzCookie())
        m.fz_close_device(device)
    finally:
        del device
    result=fitz.Rect(bbox.x0,bbox.y0,bbox.x1,bbox.y1)
    if not all(math.isfinite(x) for x in result) or result.is_empty:return None
    return result

def _outside(rect,area,tolerance):
    d={'left':area.x0-rect.x0,'right':rect.x1-area.x1,
       'top':area.y0-rect.y0,'foot':rect.y1-area.y1}
    return {k:_round(v) for k,v in d.items() if v>tolerance}

def allowed_area(page,geometry=None):
    g={**DEFAULT_GEOMETRY,**(geometry or {})}
    sheet=page.rect*page.derotation_matrix
    left=sheet.x0+g['margin_left_mm']*MM
    right=sheet.x1-g['margin_right_mm']*MM
    top=sheet.y0+g['margin_top_mm']*MM
    bottom=sheet.y1-g['margin_bottom_mm']*MM
    block=fitz.Rect(left,top,right,bottom)
    allowed=fitz.Rect(left,top-g['head_allowance_pt'],
        right+g['marginpar_sep_pt']+g['marginpar_width_mm']*MM,
        bottom+g['footskip_pt']+g['footer_ink_allowance_pt'])
    if 'allowed_rect_pt' in g:allowed=fitz.Rect(g['allowed_rect_pt'])
    return sheet,block,allowed,g

def diagnose(page,allowed,tolerance):
    """List painted objects outside the permitted area and relevant text spans."""
    logs=page.get_bboxlog()
    trace=None
    out=[]
    for seqno,item in enumerate(logs):
        kind,bbox=item[:2]
        if kind=='ignore-text':continue
        r=fitz.Rect(bbox)
        if r.is_empty:continue
        edges=_outside(r,allowed,tolerance)
        if not edges:continue
        row={'sequence':seqno,'kind':kind,'bbox':_rect(r),'edges_pt':edges}
        if kind in ('fill-text','stroke-text'):
            if trace is None:trace=page.get_texttrace()
            ss=[s for s in trace if s.get('seqno')==seqno]
            chars=[]
            for s in ss:
                for c in s.get('chars',[]):
                    codepoint,glyph,origin,cb=c
                    cr=fitz.Rect(cb)
                    # Exact ink is the object bbox above. Character metric boxes
                    # merely identify letters nearest the offending boundary.
                    near=(('left' in edges and cr.x0<allowed.x0+2) or
                          ('right' in edges and cr.x1>allowed.x1-2) or
                          ('top' in edges and cr.y0<allowed.y0+2) or
                          ('foot' in edges and cr.y1>allowed.y1-2))
                    if near:
                        try:ch=chr(codepoint)
                        except ValueError:ch='?'
                        if not ch.isspace():chars.append({'character':ch,'unicode':codepoint,'glyph':glyph,'metric_bbox':_rect(cr)})
            row['near_boundary_characters']=chars
            row['single_letter_candidate']=(len(chars)==1 and chars[0]['character'].isalpha() and set(edges)<= {'left','right'})
        else:row['single_letter_candidate']=False
        out.append(row)
    return out

def page_record(page,number,geometry=None,diagnostics=True):
    sheet,block,area,g=allowed_area(page,geometry)
    bbox=ink_bbox(page)
    result={'page':number,'rotation':page.rotation,
        'orientation':'landscape' if page.rect.width>page.rect.height else 'portrait',
        'display_size_pt':[_round(page.rect.width),_round(page.rect.height)],
        'sheet_bbox_pt':_rect(sheet),'main_type_block_pt':_rect(block),'allowed_ink_area_pt':_rect(area),
        'ink_bbox_pt':_rect(bbox) if bbox else None,
        'display_ink_bbox_pt':_rect(bbox*page.rotation_matrix) if bbox else None,
        'off_sheet':False,'outside_type_area':False,'in_note_column':False,
        'sheet_edges_pt':{},'type_edges_pt':{},'offending_objects':[]}
    if bbox:
        result['sheet_edges_pt']=_outside(bbox,sheet,g['sheet_tolerance_pt'])
        result['type_edges_pt']=_outside(bbox,area,g['type_tolerance_pt'])
        result['off_sheet']=bool(result['sheet_edges_pt'])
        result['outside_type_area']=bool(result['type_edges_pt'])
        result['in_note_column']=bbox.x1>block.x1+g['type_tolerance_pt']
        if diagnostics and (result['off_sheet'] or result['outside_type_area']):
            result['offending_objects']=diagnose(page,area,g['type_tolerance_pt'])
    return result

def analyze(pdf,geometry=None,diagnostics=True):
    path=Path(pdf)
    with fitz.open(path) as doc:
        rows=[]
        for i,page in enumerate(doc,1):
            g={k:v for k,v in (geometry or {}).items() if k!='pages'}
            g.update((geometry or {}).get('pages',{}).get(str(i),{}))
            rows.append(page_record(page,i,g,diagnostics))
    return {'file':path.name,'backend':'MuPDF native fz_new_bbox_device via PyMuPDF',
        'pymupdf_version':fitz.version[0],'mupdf_version':fitz.version[1],
        'coordinate_system':'unrotated sheet; origin at top left; PDF points (1/72 inch)',
        'geometry':{**DEFAULT_GEOMETRY,**(geometry or {})},
        'pages':len(rows),'off_sheet_pages':[r['page'] for r in rows if r['off_sheet']],
        'outside_type_area_pages':[r['page'] for r in rows if r['outside_type_area']],
        'note_column_pages':[r['page'] for r in rows if r['in_note_column']],
        'landscape_pages':[r['page'] for r in rows if r['orientation']=='landscape'],
        'page_results':rows}

def boxes(pdf):
    """Compatibility with the supplied script's eight-coordinate interface."""
    r=analyze(pdf,diagnostics=False)
    return [tuple(p['ink_bbox_pt'] or [0,0,0,0])+tuple(p['sheet_bbox_pt']) for p in r['page_results']]

def check(pdf):
    r=analyze(pdf,diagnostics=False)
    off=[(p['page'],*p['ink_bbox_pt']) for p in r['page_results'] if p['off_sheet']]
    outside=[(p['page'],p['type_edges_pt']) for p in r['page_results'] if p['outside_type_area']]
    return off,outside,r['note_column_pages']

def write_tsv(result,path):
    fields=['page','orientation','rotation','ink_bbox_pt','off_sheet','sheet_edges_pt','outside_type_area','type_edges_pt','in_note_column']
    with Path(path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
        for row in result['page_results']:
            w.writerow({k:json.dumps(row[k],ensure_ascii=False) if isinstance(row[k],(dict,list)) else row[k] for k in fields})

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('pdf');ap.add_argument('--list',action='store_true')
    ap.add_argument('--json');ap.add_argument('--tsv');ap.add_argument('--geometry');ap.add_argument('--no-diagnostics',action='store_true')
    a=ap.parse_args();geometry=json.loads(Path(a.geometry).read_text()) if a.geometry else None
    r=analyze(a.pdf,geometry,not a.no_diagnostics)
    if a.json:Path(a.json).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    if a.tsv:write_tsv(r,a.tsv)
    print(f"{r['file']}: {r['pages']} pages | off the sheet: {len(r['off_sheet_pages'])} | outside the type area: {len(r['outside_type_area_pages'])} | with ink in note column: {len(r['note_column_pages'])}")
    if a.list:
        for row in r['page_results']:
            if row['off_sheet'] or row['outside_type_area']:
                print(json.dumps({k:row[k] for k in ['page','ink_bbox_pt','sheet_edges_pt','type_edges_pt']},ensure_ascii=False))
if __name__=='__main__':main()
