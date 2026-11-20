#!/usr/bin/env python3
"""Prepare source-anchored first readings; never read images or perform blind reading.

Default: validate the proposal JSON and print an audit summary. No TSV is written.
After main-reader review, --write-tsv writes *_boxes.tsv and *_first.tsv only,
and only when all eight first adjudications exist. It never writes *_second.tsv.
Recipes retain exact page-source anchors and may add documented inherited state
wrappers to an excerpt. Whitespace is the only source-match normalization.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EDITIONS=range(26,34)
WORD_KINDS={'misread word','abbreviation expanded or spelling modernised','omission','text not on the page'}
DESCRIPTION=re.compile(r'(?i)(manuscript page number|rotation (?:for|[-0-9])|preferred [^}]|calligraphic L|hooked right arrow|underlined\]|\[correction\]|single indexed coproduct|right edge partly clipped|terminal letters doubtful|surviving live comma|next separate cancelled fragment|compare plain F|still doubtful|unlabelled vertical grouping stroke)')

def sha(text): return hashlib.sha256(text.encode('utf-8')).hexdigest()
def norm(text): return re.sub(r'\s+','',text)
def uncomment(text): return re.sub(r'(?<!\\)%[^\n]*','',text)
def boxed(b): return [int(b[k]) for k in ('x0','y0','x1','y1')]
def neutral_kind(kind):
    k=kind.lower()
    if 'diagram' in k:return 'diagram'
    if 'drawing' in k or 'graphic' in k or 'framing' in k:return 'drawing'
    deletion=any(x in k for x in ('deletion','struck','cancel','overwrit'))
    insertion='insertion' in k
    if deletion and insertion:return 'deletion/insertion'
    if deletion:return 'deletion'
    if insertion:return 'insertion'
    if 'margin' in k:return 'marginal note'
    if 'number' in k or 'numeral' in k:return 'number'
    if 'formula' in k:return 'formula'
    return 'word difference'
def overlap(a,b):
    area=max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
    return area/max(1,(a[2]-a[0])*(a[3]-a[1]))
def brace_end(t,start):
    assert t[start]=='{'
    depth=0
    for m in re.finditer(r'\\.|[{}]',t[start:]):
        z=m.group()
        if z=='{': depth+=1
        elif z=='}':
            depth-=1
            if depth==0:return start+m.end()
    raise ValueError(f'Unbalanced page-source brace at {start}')
def macro_spans(t,names):
    pattern=r'\\('+ '|'.join(names)+r')\s*\{'
    out=[]
    for m in re.finditer(pattern,t):
        end=brace_end(t,m.end()-1)
        out.append(dict(start=m.start(),end=end,macro=m[1],text=t[m.start():end]))
    return out

def render_recipe(page,recipe):
    parts=[]; anchors=[]
    for a in recipe['parts']:
        lo,hi=a['start'],a['end']; actual=page[lo:hi]
        if actual!=a['text']:raise ValueError(f'Source anchor changed at {lo}:{hi}')
        parts.append(actual);anchors.append((lo,hi))
    text=recipe.get('prefix','')+recipe.get('joiner','').join(parts)+recipe.get('suffix','')
    if recipe.get('strip_comments',False):text=uncomment(text)
    if DESCRIPTION.search(text):raise ValueError('English description remains in first reading')
    if re.search(r'\\(?:struck|uncertain|marginal|ill|add|note)\b',text):raise ValueError('Witness-only macro remains in first reading')
    return text.strip(),anchors

def covers_span(candidate,span):
    """Require both source provenance at this occurrence and its literal content."""
    a,b=span['start'],span['end']; provenance=any(max(a,x)<min(b,y) for x,y in candidate['_anchors'])
    if not provenance:return False
    target=norm(span['text']); reading=norm(candidate['reading'])
    if target in reading:return True
    # Display/inline wrappers may be supplied for a standalone formula excerpt.
    if span.get('type')=='formula':
        if target.startswith(r'\[') and target.endswith(r'\]'):target=target[2:-2]
        elif target.startswith('$') and target.endswith('$'):target=target[1:-1]
        return target in reading
    return False

def formula_spans(page):
    result=[]
    for m in re.finditer(r'\\\[([\s\S]*?)\\\]',page):
        result.append(dict(start=m.start(),end=m.end(),text=m.group(),type='formula'))
    marks=[m.start() for m in re.finditer(r'(?<!\\)\$',page)]
    for a,b in zip(marks[::2],marks[1::2]):result.append(dict(start=a,end=b+1,text=page[a:b+1],type='formula'))
    return result

def audit_page(page,record,candidates,proposal):
    required=[]
    for i,s in enumerate(macro_spans(page,['deleted','inserted','unsure']),1):
        matches=[b['box'] for b in candidates if covers_span(b,s)]
        required.append(dict(id=f"source-{s['macro']}-{i:03d}",category=s['macro'],source=s['text'],start=s['start'],end=s['end'],covered_by=matches,status='covered' if matches else 'MISSING'))
    doubts=macro_spans(page,['unsure']); formulas=formula_spans(page)
    selected={}
    for u in doubts:
        enclosing=[f for f in formulas if f['start']<=u['start'] and f['end']>=u['end']]
        if enclosing:
            # A doubt inside a display requires that display, not an isolated symbol.
            displays=[f for f in enclosing if f['text'].startswith(r'\[')]
            f=max(displays,key=lambda z:z['end']-z['start']) if displays else min(enclosing,key=lambda z:z['end']-z['start'])
            selected[(f['start'],f['end'])]=f
    for i,f in enumerate(selected.values(),1):
        matches=[b['box'] for b in candidates if covers_span(b,f)]
        required.append(dict(id=f'formula-doubt-{i:03d}',category='whole formula containing a page doubt',source=f['text'],start=f['start'],end=f['end'],covered_by=matches,status='covered' if matches else 'MISSING'))
    for num in proposal.get('numerals',[]):
        s=dict(num['anchor']);s['type']='number'
        matches=[b['box'] for b in candidates if covers_span(b,s)]
        required.append(dict(id=num['id'],category='handwritten numeral',source=s['text'],covered_by=matches,status='covered' if matches else 'MISSING'))
    # Metadata scope audits are a separate obligation from the page macro audit.
    for i,st in enumerate(record.get('C_state_audit',[]),1):
        key=st.get('id',f'C-state-{i}');explicit=proposal.get('state_coverage',{}).get(key)
        target=st.get('box'); geometrical=[]
        if target:geometrical=[b['box'] for b in candidates if overlap(target,boxed(b))>.98]
        matches=explicit or geometrical
        status='covered' if matches else 'REVIEW'
        if 'No inserted macro' in str(st):status='not applicable';matches=[]
        required.append(dict(id=key,category='C state scope and attachment',covered_by=matches,status=status,method='explicit source-scope map' if explicit else 'existing coordinate enclosure',source=st.get('C_scope',st.get('C',st.get('scope','')))))
    # C/H word loci and medium/low departures: use source-reading anchors as well
    # as coordinates. Broad evidence crops need not equal the narrow target box.
    for c in record.get('changes',[]):
        kind=c.get('kind','');flags=c.get('against_C') or c.get('against_H')
        isword=flags and (kind in WORD_KINDS or 'readable ink' in kind or kind=='other')
        low=c.get('against_C') and c.get('confidence') in ('medium','low')
        if not (flags or low):continue
        explicit=proposal.get('change_coverage',{}).get(c['id']); target=c.get('box');matches=[]
        if explicit:matches=explicit
        elif target:
            final=norm(c.get('final',''))
            matches=[b['box'] for b in candidates if overlap(target,boxed(b))>.98 or (final and final in norm(b['reading']) and overlap(target,boxed(b))>0)]
        required.append(dict(id=c['id'],category='medium/low departure from C' if low else ('C/H word or punctuation locus' if isword else 'other recorded C/H difference'),source=c.get('final'),covered_by=matches,status='covered' if matches else 'REVIEW',method='explicit literal-context map' if explicit else 'reading plus existing coordinate metadata'))
    return required

def prepare(root,repair_path,scans=None):
    data=json.loads(repair_path.read_text(encoding='utf-8')); summaries=[]; all_candidates={};audit={};errors=[];warnings=[]
    selected=scans or [int(n) for n in data['pages']]
    for n in selected:
        key=f'{n:03d}'
        if key not in data['pages']:errors.append(f'{key}: no reviewed repair proposal');continue
        proposal=data['pages'][key];path=root/'pages'/f'J156-5-04_156-5_scan{key}.tex';page=path.read_text(encoding='utf-8')
        record=json.loads((root/'review'/f'scan{key}_adjudicated.json').read_text(encoding='utf-8'))
        if sha(page)!=proposal['page_sha256']:errors.append(f'{key}: page-source hash changed; anchors must be reviewed again');continue
        originals={b['box']:b for b in record['second_boxes']};cand=[]
        for item in proposal['candidates']:
            if item['action']=='remove':continue
            boxid=item['box'];base=dict(originals.get(boxid,{}));base.update({k:item[k] for k in ('box','kind','x0','y0','x1','y1','rotation') if k in item})
            try:reading,anchors=render_recipe(page,item['recipe'])
            except (KeyError,ValueError,AssertionError) as exc:errors.append(f'{key}/{boxid}: {exc}');continue
            if boxid in originals and item.get('original_reading')!=originals[boxid]['reading']:errors.append(f'{key}/{boxid}: adjudicated candidate changed after preparation')
            if reading!=item['proposed_reading']:errors.append(f'{key}/{boxid}: stored proposal differs from source recipe')
            if len(boxed(base))!=4 or not(0<=base['x0']<base['x1'] and 0<=base['y0']<base['y1']):errors.append(f'{key}/{boxid}: invalid rectangle')
            dims=record.get('image_dimensions')
            if isinstance(dims,list) and len(dims)==2 and (base['x1']>dims[0] or base['y1']>dims[1]):warnings.append(f'{key}/{boxid}: rectangle exceeds recorded image dimensions; preserve metadata pending main review')
            base.update(reading=reading,_anchors=anchors);cand.append(base)
        ids={b['box'] for b in cand}
        if len(ids)!=len(cand):errors.append(f'{key}: duplicate candidate IDs')
        if set(originals)-{i['box'] for i in proposal['candidates']}:errors.append(f'{key}: original candidate omitted without a decision')
        for group in ('state_coverage','change_coverage'):
            for k,boxes in proposal.get(group,{}).items():
                if set(boxes)-ids:errors.append(f'{key}/{k}: coverage names an absent candidate')
        coverage=audit_page(page,record,cand,proposal);missing=[x for x in coverage if x['status']=='MISSING'];review=[x for x in coverage if x['status']=='REVIEW']
        if missing:errors.extend(f"{key}/{x['id']}: required literal span uncovered" for x in missing)
        if review:warnings.extend(f"{key}/{x['id']}: metadata coverage requires review" for x in review)
        audit[key]=coverage;all_candidates[key]=cand
        summaries.append(dict(scan=key,candidates=len(cand),originals=len(originals),repairs=sum(i['action']=='replace' for i in proposal['candidates']),additions=sum(i['action']=='add' for i in proposal['candidates']),coverage_obligations=len(coverage),missing=len(missing),review=len(review)))
    return dict(purpose='Metadata/source-anchor preparation only; no image access and no blind reading',summary=summaries,errors=errors,warnings=warnings,audit=audit),all_candidates

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repairs',type=Path,default=ROOT/'review/second_candidate_repairs.json')
    ap.add_argument('--scans',nargs='+',type=int)
    ap.add_argument('--report',type=Path,help='Optional JSON audit report; defaults to no file')
    ap.add_argument('--write-tsv',action='store_true',help='Explicit later generation of box/first TSVs after main review; requires all eight adjudications')
    ap.add_argument('--output-dir',type=Path,default=ROOT/'second')
    args=ap.parse_args();report,candidates=prepare(ROOT,args.repairs,args.scans)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if args.write_tsv:
        missing=[f'{n:03d}' for n in EDITIONS if not (ROOT/'review'/f'scan{n:03d}_adjudicated.json').exists()]
        if missing:report['errors'].append('First adjudications incomplete: '+', '.join(missing))
        if report['warnings']:report['errors'].append('Resolve audit warnings before freezing TSVs')
        if not report['errors']:
            args.output_dir.mkdir(parents=True,exist_ok=True)
            for key,boxes in candidates.items():
                stem=f'J156-5-04_156-5_scan{key}'
                for suffix,fields in [('_boxes',['box','kind','x0','y0','x1','y1']),('_first',['box','reading'])]:
                    out=args.output_dir/(stem+suffix+'.tsv')
                    if out.exists():raise SystemExit(f'Refusing to overwrite precommitted file: {out}')
                    with out.open('w',encoding='utf-8',newline='') as fh:
                        writer=csv.DictWriter(fh,fieldnames=fields,delimiter='\t');writer.writeheader()
                        for b in boxes:writer.writerow({k:(neutral_kind(b.get(k,'')) if k=='kind' else b.get(k,'')) for k in fields})
    print(json.dumps({k:report[k] for k in ('purpose','summary','errors','warnings')},ensure_ascii=False,indent=2))
    return bool(report['errors'])
if __name__=='__main__':raise SystemExit(main())
