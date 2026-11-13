"""Combine the exact leading-tag inventory with confirmed special cases."""
from pathlib import Path
import sys,json,re,argparse,hashlib
from functools import lru_cache
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial

D=Path('work/layout_probes')

@lru_cache(maxsize=None)
def view(pkg,lang,mechanical):
    t=build_readers.raw_package(pkg,lang)
    if mechanical:t,_=mechanical_repairs.repair(t,pkg,lang)
    return layout_repairs.repair(t,pkg,lang,include_pagination=False)[0]

def main():
    args=argparse.ArgumentParser();args.add_argument('--commit',action='store_true');args=args.parse_args()
    rows=json.loads((D/'all_tag_bindings_candidate.json').read_text())
    # Section V's reviewed opening group already includes its leading (1).
    # One larger exact binding preserves both, without nested duplicate groups.
    rows=[r for r in rows if r['id']!='140-3-548-K1']
    for lang in ['fr','en']:
        for scan,tag in [(503,'9'),(506,'21')]:
            pkg='LM_C3-492-510';variants=[]
            for mechanical in [False,True]:
                t=view(pkg,lang,mechanical)
                a,b=next((a,b) for s,a,b in layout_repairs._scan_ranges(t) if s==scan);part=t[a:b]
                trailing=r'\hfill('+tag+')'
                assert part.count(trailing)==1
                end=part.index(trailing)+len(trailing);start=part.rindex(r'\diagram{',0,end)
                old=part[start:end];new=r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'
                if not any(p['old']==old for p in variants):variants.append(dict(old=old,new=new))
            rows.append(dict(id=f'140-3-{scan}-K{tag}trailing',language=lang,package=pkg,scan=scan,tag=tag,
                kind='equation-tag pagination',source_pattern='Visually confirmed trailing number immediately after diagram',
                reason=f'Keep the unchanged trailing equation number ({tag}) with its preceding complete diagram using a local samepage group; only page-break penalties change.',variants=variants))
        pkg='LM_C3-530-548';scan=548;variants=[]
        for mechanical in [False,True]:
            t=view(pkg,lang,mechanical)
            a,b=next((a,b) for s,a,b in layout_repairs._scan_ranges(t) if s==scan);part=t[a:b]
            anchor=r'\[\overline{\underline{\mathrm V}}\]';assert part.count(anchor)==1
            start=part.index(anchor);di=part.index(r'\diagram{',start);end=editorial.brace_end(part,di+len(r'\diagram'))
            old=part[start:end];new=r'\begin{samepage}'+'\n'+old+'\n'+r'\end{samepage}'
            if not any(p['old']==old for p in variants):variants.append(dict(old=old,new=new))
        rows.append(dict(id='140-3-548-KV',language=lang,package=pkg,scan=scan,tag='V',
            kind='section-heading pagination',source_pattern='Visually confirmed section V opening',
            reason='Keep section V, its unchanged short marginal heading, and the opening sentence and diagram together using a local samepage group; only page-break penalties change.',variants=variants))
    rows.sort(key=lambda r:(r['package'],r['scan'],r['language'],r['id']))
    assert len({(r['id'],r['language']) for r in rows})==len(rows)
    dest=Path('work/data/layout_tag_bindings.json') if args.commit else D/'complete_tag_bindings_candidate.json'
    dest.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    # Exercise each accepted syntax, plus the two reverse cases and the
    # marginally titled section, under an intentionally constrained page foot.
    ids=['140-2-568-K67','140-3-562-K65','140-3-335-K58','140-4-203-K30',
         '140-4-35-K9','140-2-407-K22','140-3-622-K5bis',
         '140-3-506-K21trailing','140-3-503-K9trailing','140-3-548-KV']
    lookup={(r['id'],r['language']):r for r in rows}
    for lang in ['fr','en']:
        for form in [0,1,2]:
            parts=[build_readers.preamble(lang,form),r'\begin{document}']
            for ident in ids:
                r=lookup[(ident,lang)];t=view(r['package'],lang,True)
                p=[p for p in r['variants'] if t.count(p['old'])==1];assert len(p)==1
                body=p[0]['new'];body,_,_=editorial.annotate(body,r['package'],lang)
                parts += [r'\clearpage',r'\noindent Pagination probe: '+ident+'.',
                    r'\par\vspace*{\dimexpr\textheight-50pt\relax}\par\penalty0',body]
            parts += [r'\end{document}']
            (D/f'tag_pattern_stress_{lang}_{form}.tex').write_text('\n'.join(parts))
    (D/'tag_pattern_stress_index.json').write_text(json.dumps(dict(repair_ids=ids,
        probe_case_count=len(ids),language_forms=6,candidate_records=len(rows),
        expected_behavior='The complete tag/diagram group moves to the following page when it cannot fit at the constrained page foot.'),indent=2)+'\n')
    print(len(rows),'exact pagination records;',len(rows)//2,'paired sites;',dest)

if __name__=='__main__':main()
