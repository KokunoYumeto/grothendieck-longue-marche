"""Prepare explicit reviewed tag/diagram bindings and pagination stress probes.

This generator is development tooling.  The runtime repair reads only the
literal generated old/new pairs; it does not discover or rewrite other tags.
"""
from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial

D=Path('work/layout_probes')
# package, scan, visible tag, exact leading anchor, occurrence among identical
# anchors. These sites have been visually confirmed in the full-book PDFs.
TARGETS=[
 ('LM_P057',568,'67',r'\((67)\)',1),
 ('LM_C3-549-567',562,'65','\\[\n(65)\n\\]',1),
 ('LM_C4-058-076',75,'144',r'\((144)\)',1),
 ('LM_C4-077-095',79,'159','\\[\n(159)\n\\]',1),
 ('LM_C4-191-209',203,'30',r'\(\unsure{(30)}\)',1),
 ('LM_C4-191-209',205,'32',r'\((32)\)',1),
 ('LM_C3-321-339',335,'58','$(58)$',1),
 ('LM_C3-435-453',436,'105',r'\noindent(105)',1),
 ('LM_C3-530-548',543,'49','\\[\n(49)\n\\]',1),
 ('LM_P042',417,'26','(26)\n\\diagram',1),
 ('LM_C3-435-453',440,'116',r'\noindent (116)',1),
 ('LM_C3-511-529',524,'3','$(3)$',1),
 ('LM_C4-058-076',76,'148',r'\((148)\)',1),
 ('LM_C3-682-696',689,'126','\\[\n(126)\n\\]',1),
 ('LM_C4-058-076',74,'139',r'\((139)\)',1),
 ('LM_C4-058-076',75,'140',r'\((140)\)',1),
 ('LM_C3-511-529',525,'5','$(5)$',1),
 ('LM_C3-530-548',542,'45','\\[\n(45)\n\\]',1),
 ('LM_C3-606-624',621,'149',r'\( (149) \)\quad',1),
 ('LM_C3-606-624',622,'5',r'\( (5) \)\quad',1),
 ('LM_C3-511-529',524,'1','$(1)$',1),
 ('LM_C3-530-548',545,'57',r'\noindent(57)\quad',1),
 ('LM_C3-530-548',545,'61',r'\noindent(61)\quad',1),
 ('LM_C3-530-548',545,'62b',r'\noindent(62)\quad',2),
 ('LM_C4-020-038',35,'9',r'(9)\quad\diagram',1),
]

def post_geometry(pkg,lang,mechanical):
    t=build_readers.raw_package(pkg,lang)
    if mechanical:t,_=mechanical_repairs.repair(t,pkg,lang)
    t,_=layout_repairs.repair(t,pkg,lang,include_pagination=False)
    return t

def exact_span(t,scan,anchor,n=1):
    a,b=next((a,b) for s,a,b in layout_repairs._scan_ranges(t) if s==scan)
    fragment=t[a:b]
    matches=list(re.finditer(re.escape(anchor),fragment))
    if len(matches)<n:raise ValueError((scan,anchor,n,len(matches)))
    start=matches[n-1].start()
    di=fragment.index(r'\diagram{',start)
    end=editorial.brace_end(fragment,di+len(r'\diagram'))
    return fragment[start:end]

def main():
    rows=[];fragments={};cache={}
    for lang in ['fr','en']:
        for pkg,scan,tag,anchor,n in TARGETS:
            variants=[]
            for mechanical in [False,True]:
                key=pkg,lang,mechanical
                if key not in cache:cache[key]=post_geometry(*key)
                old=exact_span(cache[key],scan,anchor,n)
                new=r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'
                if not any(v['old']==old for v in variants):variants.append(dict(old=old,new=new))
                if mechanical:fragments[(lang,pkg,scan,tag)]=new
            cote=layout_repairs.COVERAGE[pkg]['cote']
            rows.append(dict(id=f'{cote}-{scan}-K{tag}',language=lang,package=pkg,scan=scan,tag=tag,
                kind='equation-tag pagination',reason=f'Keep the unchanged leading equation number ({tag.rstrip("b")}) with its following complete diagram using a local samepage group; only page-break penalties change.',variants=variants))
        # The trailing number is a separate source line after a diagram.
        pkg='LM_C3-492-510';scan=506;tag='21';variants=[]
        for mechanical in [False,True]:
            key=pkg,lang,mechanical
            if key not in cache:cache[key]=post_geometry(*key)
            a,b=next((a,b) for s,a,b in layout_repairs._scan_ranges(cache[key]) if s==scan)
            fragment=cache[key][a:b]
            end=fragment.index(r'\hfill(21)')+len(r'\hfill(21)')
            start=fragment.rindex(r'\diagram{',0,end)
            old=fragment[start:end];new=r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'
            if not any(v['old']==old for v in variants):variants.append(dict(old=old,new=new))
            if mechanical:fragments[(lang,pkg,scan,tag)]=new
        rows.append(dict(id='140-3-506-K21',language=lang,package=pkg,scan=scan,tag=tag,
            kind='equation-tag pagination',reason='Keep the unchanged trailing equation number (21) with its preceding complete diagram using a local samepage group; only page-break penalties change.',variants=variants))
        # Section V and its marginal title must open with the introductory text.
        pkg='LM_C3-530-548';scan=548;tag='V';variants=[]
        for mechanical in [False,True]:
            key=pkg,lang,mechanical
            if key not in cache:cache[key]=post_geometry(*key)
            old=exact_span(cache[key],scan,r'\[\overline{\underline{\mathrm V}}\]')
            new=r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'
            if not any(v['old']==old for v in variants):variants.append(dict(old=old,new=new))
            if mechanical:fragments[(lang,pkg,scan,tag)]=new
        rows.append(dict(id='140-3-548-KV',language=lang,package=pkg,scan=scan,tag=tag,
            kind='section-heading pagination',reason='Keep section V, its unchanged short marginal heading, and the opening sentence and diagram together using a local samepage group; only page-break penalties change.',variants=variants))
    (D/'tag_bindings_candidate.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    order=[(p,s,t) for p,s,t,_,_ in TARGETS]+[('LM_C3-492-510',506,'21'),('LM_C3-530-548',548,'V')]
    for lang in ['fr','en']:
        for form in [0,1,2]:
            parts=[build_readers.preamble(lang,form),r'\begin{document}']
            for pkg,scan,tag in order:
                body=fragments[(lang,pkg,scan,tag)]
                body,_,_=editorial.annotate(body,pkg,lang)
                parts += [r'\clearpage',r'\noindent Pagination probe: '+f'{pkg}, scan {scan}, tag {tag}.',
                    r'\par\vspace*{\dimexpr\textheight-50pt\relax}',body]
            parts += [r'\end{document}']
            (D/f'tag_bindings_{lang}_{form}.tex').write_text('\n'.join(parts))
    print(len(rows),'paired exact pagination candidates;',len(order),'sites; six stress-probe sources')

if __name__=='__main__':main()
