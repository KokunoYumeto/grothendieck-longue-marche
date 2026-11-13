"""Exact final-zoom label candidates; no checked source or repair module edits."""
from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes')
targets=[('LM_C3-435-453',446),('LM_C3-568-586',574),('LM_C3-549-567',561),('LM_C3-625-643',637),('LM_C3-625-643',638)]
records=[]
for lang in ['fr','en']:
    fragments={}
    for pkg,scan in targets:
        text=build_readers.raw_package(pkg,lang)
        text,_=mechanical_repairs.repair(text,pkg,lang)
        text,_=layout_repairs.repair(text,pkg,lang)
        a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(text) if n==scan)
        diagrams=list(re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',text[a:b],re.S))
        old=next(m[0] for m in diagrams if ('quotient' in m[0] if scan==446 else r'\mathrm{sg}' in m[0] if scan==574 else r'\theta_Z' in m[0] if scan==561 else '(37)' in m[0] if scan==637 else '(38)' in m[0]))
        new=old
        if scan==446:
            matches=re.findall(r'(\\arrow\[rr,hook,"[^\n]+"\x27)(\])',new)
            assert len(matches)==2
            for start,end in matches:
                new=new.replace(start+end,start+r'{yshift=-3pt}'+end)
            reason='Shift both existing quotient labels down by3pt to clear the lower horizontal arrowhead barbs; keep the18pt central gap, endpoints and wording.'
        elif scan==574:
            before=r'"{\unsure{\mathrm{sg}|\mathrm{sgn}}}"'
            assert new.count(before)==1
            new=new.replace(before,before+r'{yshift=4pt}')
            reason='Raise the unchanged uncertain sg|sgn label by4pt to clear its curved arrow; keep the50pt last-column gap and all endpoints.'
        elif scan==561:
            for label,prime in [(r'\varepsilon_{\gamma,\rho}=\varepsilon\x27_\gamma',''),(r'\varepsilon_{\gamma,\sigma}=\varepsilon_\gamma',"'")]:
                label=label.replace(r'\x27',"'")
                before='"{'+label+'}"'+prime
                assert new.count(before)==1,(lang,before)
                new=new.replace(before,before+r'{pos=.75}')
            before=r'\arrow[from=5-2,to=6-7,dashed,"\unsure{\mathrm{pr}}"]'
            assert new.count(before)==1
            new=new.replace(before,before[:-1]+r'{pos=.25}]')
            reason='Place both existing epsilon labels at position0.75 along their own rightward diagonals and the uncertain projection label at0.25 along its dashed arrow, clear of crossing verticals; keep all matrix dimensions and endpoints.'
        elif scan==637:
            for before in [r'\mathcal{M}\x27\x27\x27(-\bar j)\times\mu\arrow[rr,hook,"2"]',r'\mathcal{N}_{\rho}^{?}\arrow[rr,hook,"3"]']:
                before=before.replace(r'\x27',"'")
                assert new.count(before)==1
                new=new.replace(before,before[:-1]+r'{pos=.75}]')
            reason='Place the two middle-row horizontal degree labels at position0.75 along their own arrows, clear of the crossing verticals; keep every endpoint, route and matrix dimension.'
        else:
            for before in [r'\mathcal{N}_{\rho}^{?}'+'\n'+r'  \arrow[uu,hook,"3"\x27]',r'\mathcal{M}^{0}(-\bar j)'+'\n'+r'  \arrow[uu,hook,"2"\x27]']:
                before=before.replace(r'\x27',"'")
                assert new.count(before)==1
                new=new.replace(before,before[:-1]+r'{pos=.7}]')
            reason='Place the upper-right vertical degree3 and upper-middle vertical degree2 labels at position0.7 along their own arrows, clear of the crossing horizontals; keep every endpoint, route and matrix dimension.'
        records.append(dict(package=pkg,scan=scan,language=lang,old=old,new=new,reason=reason))
        fragments[(pkg,scan)]=new
    for form in [0,1,2]:
        parts=[build_readers.preamble(lang,form),r'\begin{document}']
        for pkg,scan in targets:
            diagram=fragments[(pkg,scan)]
            marker=r'\LMcote{140-3}\scanpage{'+str(scan)+'}'
            if scan==561:
                body=r'\begin{landscape}'+marker+r'\begin{center}\((62)\quad\)'+diagram+r'\end{center}\end{landscape}'
            else:
                body=marker+r'\diagram{'+diagram+'}'
            body,_,_=editorial.annotate(body,pkg,lang)
            parts += [r'\clearpage',body]
        parts += [r'\end{document}']
        (D/f'final_residual_labels_{lang}_{form}.tex').write_text('\n'.join(parts))
(D/'final_residual_labels_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
