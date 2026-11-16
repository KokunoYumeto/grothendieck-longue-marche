"""Assemble audited modules, renumber statements and produce the results register.
Raw modules are retained for provenance; sections/P.tex,A.tex,B.tex are generated.
"""
from pathlib import Path
import re,csv,json
ROOT=Path(__file__).resolve().parents[1]
blocks={}

def parse(path):
    text=(ROOT/path).read_text()
    tokens=list(re.finditer(r'^\\begin\{statement\}|^\\paragraph\{[A-Za-z][\w.-]* \(|^\\subsection\{|^\\section\*?\{',text,re.M))
    for j,m in enumerate(tokens):
        end=tokens[j+1].start() if j+1<len(tokens) else len(text)
        chunk=text[m.start():end].strip()
        if chunk.startswith('\\begin{statement}'):
            h=re.match(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}',chunk)
            key,status=h.groups()
            # Title may include nested braces. Find its balanced closing brace.
            start=h.end(); assert chunk[start]=='{'
            lev=0;stop=start
            for stop in range(start,len(chunk)):
                if chunk[stop]=='{':lev+=1
                elif chunk[stop]=='}':
                    lev-=1
                    if lev==0:break
            title=chunk[start+1:stop]
            body=chunk[stop+1:]
            blocks[key]={'id':key,'status':status,'title':title,'body':body,'env':True,'source':path}
        elif chunk.startswith('\\paragraph{'):
            # Paragraph headings may wrap in the source and may contain nested
            # TeX groups. Read their balanced braces before matching the ID.
            start=len('\\paragraph{'); lev=1; stop=start
            for stop in range(start,len(chunk)):
                if chunk[stop]=='{':lev+=1
                elif chunk[stop]=='}':
                    lev-=1
                    if lev==0:break
            head=re.sub(r'\s+',' ',chunk[:stop+1])
            body=chunk[stop+1:].lstrip('.\n ')
            h=re.match(r'\\paragraph\{([^ ]+) \((.*)\)[:.]?(.*?)\}\.?$',head)
            if not h:raise ValueError(head)
            key,info,rest=h.groups()
            status=next((s for s in ['Proved','Refuted','Known','Open'] if info.startswith(s)), 'Open')
            title=rest.lstrip(': ').rstrip('.') or info
            if title==info:
                title=re.sub(r'^(Proved|Refuted|Known|Open)[^:]*:\s*','',info)
            blocks[key]={'id':key,'status':status,'title':title,'body':body,'env':False,'source':path}

paths=['sections/P_root.tex','sections/A_root.tex','sections/A_fields.tex','sections/B_root.tex',
'agent_lifting/lifting_results.tex','agent_lifting/lifting_units.tex','agent_lifting/lifting_manuscript.tex',
'agent_lifting/lifting_pentagon_gap.tex','agent_literature/A2_and_AA_proofs.tex',
'agent_literature/B7_comparison_proofs.tex','agent_five/five_point_results.tex']
for p in paths:parse(p)
plans={
'P':[("Opened literature and exact scope",[f'PR.{i}' for i in range(1,7)]),
     ("An integral construction proving strict inclusion",[f'LP.{i}' for i in range(1,6)]),
     ("The relative abelianization",['P-L1'])],
'A':[("The sign object, scalar compression, finite levels and descent",[f'A.{i}' for i in range(1,18)]),
     ("The three arithmetic CM fields",[f'AF.{i}' for i in range(1,8)]),
     ("The categorical and theta tests",[f'A.2-L{i}' for i in range(1,8)]),
     ("Algebraically ample subgroups",['A.3-L1']),
     ("Five-point frames and the harmonic cover",[f'FP.{i}' for i in range(1,12)]),
     ("Atkin--Lehner defects and finite five-point targets",[f'FP.{i}' for i in range(17,23)]),
     ("The restricted pentagon lifting problem",[f'LX.{i}' for i in range(1,5)])],
'B':[("Character consequences and dependency repairs",[f'B.{i}' for i in range(1,11)]),
     ("Weights, the complete frame image and the arithmetic replacement",[f'LB.{i}' for i in range(1,8)]),
     ("Metabelian units and arithmetic compatibility",[f'LU.{i}' for i in range(1,7)]),
     ("The manuscript dictionary",[f'LD.{i}' for i in range(1,3)]),
     ("Sewing and comparison source checks",[f'B.7-L{i}' for i in range(1,5)]),
     ("Higher-point rigidity and the manuscript's five-point configurations",[f'FP.{i}' for i in range(12,17)])]
}
# New completed modules may be appended without altering the established labels.
extras=ROOT/'records/assembly_extras.json'
if extras.exists():
    for item in json.loads(extras.read_text()):
        if item['path'] not in paths:parse(item['path'])
        plans[item['part']].append((item['heading'],item['ids']))
mapids={}
for part,sections in plans.items():
    n=0
    for _,ids in sections:
        for old in ids:
            if old not in blocks:raise ValueError('missing '+old)
            n+=1;mapids[old]=f'{part}.{n}'
# Put the intended final references into the root text before local identifier expansion.
for k,b in blocks.items():
    if k in ['FP.50','FP.51','FP.55','FP.56']:
        b['body']=b['body'].replace('FP.52','RA.3')
    if k in ['RA.3','RA.4','RA.5','RA.6']:
        b['body']=b['body'].replace('RA.2','FP.50')
    if k=='PR.1':b['body']=b['body'].replace('P.10 below','LP.5 below')
    if k=='B.1':b['body']=b['body'].replace('B.23 below','LB.4 below')
    if k=='B.6':b['body']=b['body'].replace('P.4 below','P-L1')
    if k=='B.10':
        b['body']=b['body'].replace('B.20--B.22','LB.1--LB.3').replace('in P.10','in LP.1')
    if k=='A.8':b['body']=b['body'].replace('A.30 below','A.2-L1 below')
    if k=='B.8':b['body']=b['body'].replace('We do not identify it with\n$\\rho_\\Phi$ on typographical grounds.',
      'LD.1--LD.2 below now compute it from the supplied scan-12 relation,\nand prove that it is not $\\rho_\\Phi$.')
    if k=='B.7-L4':b['status']='Proved'
    if k=='FP.1':b['body']=b['body'].replace('Since $\\lambda$ is odd, Thus','Since $\\lambda$ is odd,')

def renumber(s):
    keys=sorted(mapids,key=len,reverse=True)
    pat=r'(?<![\w.])('+ '|'.join(re.escape(k) for k in keys)+r')(?!\w|\.\d)'
    s=re.sub(pat,lambda m:mapids[m.group()],s)
    s=s.replace('{LochakSchneps1997}','{LitLochakSchneps1997}')
    s=s.replace('{LiftHarbaterSchneps2000}','{LitHarbaterSchneps2000}')
    s=s.replace('{LiftNakamuraSchneps2000}','{LitNakamuraSchneps2000}')
    s=s.replace('{LiftTsunogaiNakamura2002}','{LitTsunogaiNakamura2002}')
    return s

# Explicit citations attach the primary sources to the relevant argument.
cites={
'LP.3':r'\citep[Propositions 3--4 and Theorem 2]{LiftHarbaterSchneps2000}',
'LP.4':r'\citep[equations (1.2)--(1.4)]{LiftCohen2001}',
'LB.3':r'\citep[Theorem 0.1]{LiftEnriquez2006}',
'LB.5':r'\citep[Section 8.5]{LiftHainMatsumoto2003}',
'LU.1':r'\citep{LiftChenDeligne2017}',
'LU.4':r'\citep{LiftSerre2007,LiftMilneCFT2020,LiftMilneLEC2013}',
'A.2-L3':r'\citep{LitAtiyah1987}',
'A.2-L4':r'\citep[Section 4]{LitDrinfeld1991}',
'A.2-L7':r'\citep{LitAtiyah1987}',
'A.3-L1':r'\citep[Definition 5.12 and Theorem 5.17(ii)]{LitHoshiMochizukiTsujimura2025}',
'P-L1':r'\citep[Question 1.2]{LitLochakSchnepsOpenProblems}',
'FP.2':r'\citep[Theorem 2 and Proposition 3(iii)]{LochakSchneps1997}',
'FP.3':r'\citep[Theorem B\(^{\prime}\)]{HerfortRibes1985}',
'FP.4':r'\citep[Theorem 3.3]{Collas2012GenusZero}',
'FP.10':r'\citep{Maier2009,Colo2022}',
'B.7-L1':r'\citep{LitBoggi2026v6,LitMargalitWinarski}',
'B.7-L2':r'\citep[Propositions 4.11 and 4.13]{LitNakamuraTsunogaiYasuda2010}',
'B.7-L3':r'\citep{LitLochakNakamuraSchneps2026,LitNakamuraTsunogaiYasuda2010}',
'B.7-L4':r'\citep[Proposition 2.4 and Definition 5.1]{LitNakamuraSchneps2000}'
}
cites.update({
'FP.26':r'\citep[Theorem B$^{\prime}$]{HerfortRibes1985}',
'A4.M3':r'\citep{LitLochakSchneps1997}',
'A4.M5':r'\citep[Theorems 1 and 2]{LitTsunogaiNakamura2002}',
'A4.M6':r'\citep[Theorems 1 and 2]{LitTsunogaiNakamura2002}'
})
cites.update({
'FC.3':r'\citep[Sections 2.9 and 2.15]{LitNakamuraTsunogaiYasuda2010}',
'RP.1':r'\citep[Sections 2.9 and 2.15]{LitNakamuraTsunogaiYasuda2010}',
'KM.1':r'\citep[Theorem 1 and Section 2]{LitIhara2000BetaGammaII}',
'KM.2':r'\citep[p.~657]{LitSchneps2006}',
'KM.4':r'\citep[Proposition 4.4]{LitNakamuraTsunogaiYasuda2010} \citep[Introduction and Section 2]{LitIhara2000BetaGammaII}',
'FP.34':r'\citep[Proposition 4.4]{LitNakamuraTsunogaiYasuda2010}',
'MD.1':r'\citep[Theorem 1]{LitIhara2000BetaGammaII} \citep[p.~100]{LitFurusho2003GTA}',
'MD.6':r'\citep[Theorems 3.1 and 3.4]{LitFurusho2003GTA} \citep[Theorems 2--3 and Appendix]{LitLochakNakamuraSchneps2004Eigenloci}'
})
answers={
**{f'PR.{i}':'P.1' for i in range(1,7)},**{f'LP.{i}':'P.2' for i in range(1,6)},'P-L1':'P.1(ii); B.2; B.6(d)',
'A.1':'Lead 1; Lead 2; A.1(a)','A.2':'A.1(b,c)','A.3':'A.1(d)(ii)','A.4':'Lead 1; A.1(a)',
'A.5':'Lead 2; A.1(d)(iii)','A.6':'Lead 2; A.2(a)','A.7':'Lead 8; A.5(a); B.2','A.8':'Lead 8; A.5(a)',
'A.9':'A.6; B.6(c)','A.10':'A.6; B.6(c)','A.11':'A.6; A.7; A.8','A.12':'Lead 7; A.4(d)',
'A.13':'A.4(d); R6','A.14':'Lead 5; A.4(a)','A.15':'Lead 5; A.4(a,b)','A.16':'Lead 9; A.6','A.17':'A.3(f,g)',
**{f'AF.{i}':'A.3(g,h)' for i in range(1,8)},
**{f'A.2-L{i}':'Lead 3; A.2' for i in range(1,8)},'A.3-L1':'A.3(i); R10',
**{f'LX.{i}':'Lead 10; A.6; A.7; A.8' for i in range(1,5)},
'FP.1':'Lead 4; A.3(a)','FP.2':'A.3(b)','FP.3':'A.3(a,f)','FP.4':'A.3(a,f)','FP.5':'A.3(a)',
'FP.6':'A.3(a)','FP.7':'A.3(c)','FP.8':'A.3(e)','FP.9':'Lead 6; A.4(b)','FP.10':'Lead 8; A.5(c)',
'FP.11':'A.5(c)','FP.12':'B.1','FP.13':'B.3','FP.14':'B.3','FP.15':'B.3','FP.16':'A.3(g); B.3',
'FP.17':'A.5(b)','FP.18':'A.5(b)','FP.19':'A.3(c)','FP.20':'A.3(d)','FP.21':'A.3(f,g)','FP.22':'A.3(e,f); A.6',
**{f'LB.{i}':'B.4' for i in range(1,4)},'LB.4':'B.5','LB.5':'B.5; R9','LB.6':'B.6(a)','LB.7':'B.6(e)',
**{f'LU.{i}':'B.4' for i in range(1,7)},'LD.1':'B.5; R11','LD.2':'B.5; R11',
**{f'B.7-L{i}':'B.7; A.4(e)' for i in range(1,5)},
'B.1':'B.2','B.2':'B.6(b)','B.3':'B.6(c)','B.4':'B.6(c)','B.5':'B.6(d)',
'B.6':'B.6(d)','B.7':'Lead 10; A.7','B.8':'B.5; B.8','B.9':'B.5; B.8','B.10':'B.8'
}
answers.update({
**{f'FC.{i}':'Lead 4; A.3(e,f); A.6; A.7; A.8' for i in range(1,4)},
**{f'FR.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in range(1,8)},
**{f'RP.{i}':'Lead 4; Lead 10; A.3(e,f,g); A.6; A.7; A.8' for i in [1,2,3,5,6,7,8]},
**{f'FA.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in range(1,4)},
**{f'RA.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in [3,4,5,6]},
**{f'GD.{i}':'Lead 4; Lead 10; A.3(e,f); A.6; A.7; A.8; B.2' for i in range(1,4)},
**{f'FF.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in range(1,9)},
**{f'DF.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in [2,3]},
'FP.51':'Lead 10; A.3(e,f); A.6; A.7; A.8',
**{f'MF.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in [2,3]},
**{f'FP.{i}':'Lead 10; A.3(e,f); A.6; A.7; A.8' for i in [40,41,42,44,45,46,47,48,49,50,54,55,56]},
'FP.34':'Lead 3; A.2; A.3(e,f); A.8',
'FP.35':'A.6; B.6(c)',
'FP.36':'Lead 10; A.3(e,f); A.6; A.7; A.8',
'LI.7':'Lead 5; A.4(a,c); A.8',
'LI.8':'Lead 10; A.4(c); A.6; A.7; A.8; B.6(a,c)',
'LI.9':'Lead 10; A.3(e,f); A.6; A.7; A.8',
**{f'RH.{i}':'A.6; B.6(c)' for i in range(1,4)},
**{f'KM.{i}':'Lead 3; Lead 5; A.4(a,c); A.8' for i in range(1,6)},
**{f'MD.{i}':'Lead 3; Lead 5; A.4(a,c,e); A.8' for i in range(1,11)},
'LH.1':'A.6; B.6(c)',
'LH.2':'B.6(c)',
'FP.37':'Lead 4; A.3(e,f); A.8',
'FP.38':'Lead 10; A.6; A.7; A.8',
'PC.1':'P.2; A.8; Lead 1; Lead 7',
'FP.30':'A.3(e,f); A.6; A.7; A.8',
'FP.31':'A.3(e,f); A.6; A.7; A.8',
'FP.32':'Lead 4; A.3(c,e,f); A.8',
'FP.33':'A.3(e,f); A.6; A.7; A.8',
**{f'LI.{i}':'Lead 5; A.4(c); A.7; A.8; B.2' for i in range(1,7)},
'AO.1':'Lead 1; A.1(d); A.3(e,f); A.6; A.7; A.8',
'AO.2':'Lead 5; A.4(a,c)','AO.3':'Lead 8; A.5(b,c)',
'BO.1':'B.1','BO.2':'B.2','BO.3':'B.6(c)',
**{f'E67.R{i}':'B.7; E.67' for i in range(1,4)},
**{f'FP.{i}':'A.6; B.6(c)' for i in [23,24,25,28,29]},
'FP.26':'B.7; E.39; E.64.7','FP.27':'A.3(b,e,f)',
**{f'A4.M{i}':'Lead 5; A.4(a,c); R12' for i in range(1,7)},
**{f'LC.{i}':'Lead 5; A.4(a,c); R12' for i in range(1,6)},
**{f'AD.{i}':'Lead 7; A.4(d)' for i in range(1,4)}
})
rows=[]
for part,sections in plans.items():
    out=[]
    for heading,ids in sections:
        out.append(('\\Needspace{10\\baselineskip}\n' if any(x in ids for x in ['LI.9','FP.41','FP.44','FF.1']) else '')+'\\subsection{'+heading+'}\n')
        for old in ids:
            b=blocks[old]; new=mapids[old];body=renumber(b['body']);title=renumber(b['title'])
            head='\\begin{statement}{'+new+'}{'+b['status']+'}{'+title+'}'
            if b['env']:
                out.append(head+body)
            else:
                out.append(head+'\n'+(renumber(cites.get(old,''))+'\n' if old in cites else '')+'\\end{statement}\n'+body)
            dep=sorted(set(re.findall(r'\b(?:[PAB]\.\d+|R\d+)\b',body))-{new})
            rows.append({'id':new,'statement':title,'status':b['status'],'where_proved':f'sections/{part}.tex; source {b["source"]} ({old})',
             'depends_on':'; '.join(dep),'answers (lead or task)':answers.get(old,''),'notes':'See complete statement and proof for hypotheses and scope.'})
    (ROOT/'sections'/f'{part}.tex').write_text('\n\n'.join(out)+'\n')
with (ROOT/'DELTA_ON_GT_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','statement','status','where_proved','depends_on','answers (lead or task)','notes']);w.writeheader();w.writerows(rows)
(ROOT/'records/statement_mapping.json').write_text(json.dumps(mapids,indent=2)+'\n')
print('Assembled',len(rows),'statements:',{p:sum(r['id'].startswith(p+'.') for r in rows) for p in plans})
print('Statuses:',{s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']})
