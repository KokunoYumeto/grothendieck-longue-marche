"""Inventory unambiguous source-local tag/diagram pairs for exact replay.

This is an offline inventory builder, not a runtime pagination callback. It
accepts only standalone numeric tags immediately before a diagram in text
mode, records every exact fragment, and leaves all other source untouched.
"""
from pathlib import Path
import sys,re,json,collections
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial

TAG=re.compile(r'^\(\s*(\d+)\s*(bis|ter|quater|[a-zA-Z])?\s*\)$')

def parse_tag(text):
    s=editorial.blank_comments(text).strip()
    s=re.sub(r'^\\noindent\s*','',s)
    s=re.sub(r'(?:\s*\\(?:quad|qquad|enspace|hfill))*\s*$','',s).strip()
    for opening,closing in [(r'\(',r'\)'),(r'\[',r'\]'),('$$','$$'),('$','$')]:
        if s.startswith(opening) and s.endswith(closing):
            s=s[len(opening):-len(closing)].strip();break
    s=re.sub(r'(?:\s*\\(?:quad|qquad|enspace|hfill))*\s*$','',s).strip()
    if s.startswith(r'\unsure{'):
        try:end=editorial.brace_end(s,len(r'\unsure'))
        except ValueError:return None
        if end==len(s):s=s[len(r'\unsure{'):-1].strip()
    s=re.sub(r'\\(?:text|textrm|mathrm)\{\s*(bis|ter|quater|[a-zA-Z])\s*\}',r'\1',s)
    m=TAG.fullmatch(s)
    return m[1]+(m[2] or '') if m else None

def inventory(text):
    result=[];masked=editorial.blank_comments(text);modes=editorial.math_mode_map(text)
    for m in re.finditer(r'\\diagram\s*\{',masked):
        # A number-only prefix occupies no more than four non-comment lines;
        # eight physical lines allow source editorial comments between them.
        stop=m.start();line_start=text.rfind('\n',0,stop)+1;starts=[line_start]
        for _ in range(8):
            if line_start==0:break
            line_start=text.rfind('\n',0,line_start-1)+1;starts.append(line_start)
        matches=[]
        for start in starts:
            # Begin at the first non-comment, non-space token. Blank/comment
            # padding belongs to the original context, not the tag binding.
            lead=re.search(r'\S',masked[start:stop])
            if not lead:continue
            start+=lead.start()
            if modes[max(0,start-1)]:continue
            tag=parse_tag(text[start:stop])
            if tag:matches.append((start,tag))
        if not matches:continue
        starts_unique={x[0]:x[1] for x in matches}
        assert len(starts_unique)==1,(starts_unique,text[max(0,stop-250):stop])
        start,tag=next(iter(starts_unique.items()))
        end=editorial.brace_end(text,m.end()-1)
        old=text[start:end]
        scan=editorial.at_scan(text,start)
        assert scan>0
        result.append(dict(scan=scan,tag=tag,start=start,end=end,old=old,
            new=r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'))
    return result

def main():
    rows=[];summaries=[]
    for pkg in layout_repairs.COVERAGE:
        paired={}
        for lang in ['fr','en']:
            original=build_readers.raw_package(pkg,lang)
            views={}
            for mechanical in [False,True]:
                t=original
                if mechanical:t,_=mechanical_repairs.repair(t,pkg,lang)
                t,_=layout_repairs.repair(t,pkg,lang,include_pagination=False)
                views[mechanical]=inventory(t)
            keys=lambda rs:[(r['scan'],r['tag']) for r in rs]
            assert keys(views[False])==keys(views[True]),(pkg,lang,'normalization changed inventory')
            counts=collections.Counter(keys(views[False]));seen=collections.Counter()
            for raw,mechanical in zip(views[False],views[True]):
                key=raw['scan'],raw['tag'];seen[key]+=1
                suffix=chr(96+seen[key]) if counts[key]>1 else ''
                cote=layout_repairs.COVERAGE[pkg]['cote']
                variants=[{k:raw[k] for k in ['old','new']}]
                if mechanical['old']!=raw['old']:variants.append({k:mechanical[k] for k in ['old','new']})
                rows.append(dict(id=f'{cote}-{raw["scan"]}-K{raw["tag"]}{suffix}',language=lang,
                    package=pkg,scan=raw['scan'],tag=raw['tag'],kind='equation-tag pagination',
                    reason=f'Keep the unchanged standalone equation number ({raw["tag"]}) with its directly following complete diagram using a local samepage group; only page-break penalties change.',
                    source_pattern='Standalone numeric tag directly before diagram, starting in text mode',variants=variants))
            paired[lang]=keys(views[False])
            summaries.append(dict(package=pkg,language=lang,standalone_tag_diagram_pairs=len(views[False])))
        assert paired['fr']==paired['en'],(pkg,'FR/EN numeric-tag inventory differs',paired)
    output=Path('work/layout_probes/all_tag_bindings_candidate.json')
    output.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    Path('work/layout_probes/all_tag_bindings_inventory_summary.json').write_text(json.dumps(dict(
        scope='Exact source-local standalone numeric tags directly followed by a diagram in text mode; no runtime discovery.',
        records=len(rows),paired_sites=len(rows)//2,all_language_pairs_match=True,packages=summaries),ensure_ascii=False,indent=2)+'\n')
    print(len(rows),'exact records;',len(rows)//2,'paired standalone tag/diagram sites')

if __name__=='__main__':main()
