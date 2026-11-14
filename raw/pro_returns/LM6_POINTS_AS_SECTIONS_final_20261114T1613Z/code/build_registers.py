#!/usr/bin/env python3
"""Build complete statement and editorial registers from the actual paper.

The coverage table is maintained explicitly; theorem text and dependencies
are extracted without truncation. This script never changes theorem status.
"""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,re,datetime

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'deliverable';ID='LM6_POINTS_AS_SECTIONS'
paper=(OUT/f'{ID}_paper.tex').read_text()
index=json.loads((ROOT/'statement_index.json').read_text())
meta={}
for name in ['A_results.json','B_results.json','F_results.json','C_results_add.json','E_results_add.json']:
    p=ROOT/name
    if p.exists():
        for r in json.loads(p.read_text()):meta[r['id']]=r
labels={label:r['id'] for r in index for label in r['labels']}

root_tasks={
 'C.1':['Item 3','Lead 3','C(d)'],
 'C.2':['Item 3','Lead 3'],
 'C.3':['Lead 3','C(a)'],'C.4':['C(a)'],'C.5':['C(a)'],
 'C.6':['C(a)'],'C.7':['C(b)'],'C.8':['C(c)'],'C.9':['C(c)','E(b)'],
 'C.10':['C(d)','B(c).equation25'],'C.11':['C(d)'],'C.12':['C(d)'],
 'D.1':['Item 1','Lead 2','D(a)'],'D.2':['D(a)'],'D.3':['D(a)'],
 'D.4':['D(b)'],'D.5':['D(c)'],'D.6':['D(c)'],'D.7':['D(c)'],
 'D.8':['D(c)'],'D.9':['D(c).quotients'],'D.10':['D(c).least_quotient'],
 'D.11':['D(c).least_quotient'],
 'E.1':['Item 4','Lead 4','E(a)'],'E.2':['E(a)'],'E.3':['E(a)'],
 'E.4':['Item 1','Item 4','E(a)','E(c)'],'E.5':['E(b)'],
 'E.6':['E(c)'],'E.7':['E(c)'],'E.8':['E(c)'],'E.9':['E(c)'],
 'E.10':['E(c)'],'E.11':['E(c)'],'E.12':['E(c)'],
 'E.15':['E(b)','LM7-E.23(iv)'],'E.16':['E(b)','LM7-E.23(iii)'],
 'E.17':['E(b)','LM7-E.23(iv)'],'E.18':['E(b)','LM7-E.23(i)'],
 'E.19':['E(b)','LM7-E.23(i)'],'E.20':['E(b)','LM7-E.23(i)','LM7-E.23(ii)'],
 'E.21':['E(b)','LM7-E.23(i)','LM7-E.23(ii)','LM7-E.23(iii)'],
 'E.22':['Lead 4','E(b)'],'E.23':['E(b)','LM7-E.23(i)'],
 'E.24':['E(b)','LM7-E.23(i)'],'E.25':['E(b)','LM7-E.23(i)'],
 'E.26':['E(b)','LM7-E.23(i)'],'E.27':['E(b)','LM7-E.23(i)'],
 'E.28':['E(b)','LM7-E.23(i)'],'E.29':['E(b)','LM7-E.23(i)'],
 'E.30':['E(b)','LM7-E.23(i)'],
 'E.31':['E(b)','LM7-E.23(iii)'],
 'E.32':['E(b)','LM7-E.23(iii)'],
 'E.33':['E(b)','LM7-E.23(iii)'],
 'E.34':['E(b)','LM7-E.23(iii)'],
 'E.35':['E(b)','LM7-E.23(i)'],
 'E.36':['E(b)','LM7-E.23(i)'],
 'E.37':['E(b)','LM7-E.23(i)','LM7-E.23(ii)'],
 'E.38':['E(b)','LM7-E.23(i)','LM7-E.23(iii)','Added LM8 finite/nilpotent inverse limits'],
 'E.39':['E(b)','LM7-E.23(i)']}
for k,tasks in root_tasks.items():meta.setdefault(k,{})['task_ids']=tasks

def brace(s,pos):
    assert s[pos]=='{'
    level=1;j=pos+1
    while level:
        if s[j]=='{' and s[j-1]!='\\':level+=1
        if s[j]=='}' and s[j-1]!='\\':level-=1
        j+=1
    return s[pos+1:j-1],j

chunks={};starts=[]
for m in re.finditer(r'\\begin\{statement\}',paper):
    pos=m.end();args=[]
    for _ in range(3):a,pos=brace(paper,pos);args.append(a)
    end=paper.index(r'\end{statement}',pos)
    starts.append((m.start(),args[0],pos,end))
for i,(start,ident,pos,end) in enumerate(starts):
    nxt=starts[i+1][0] if i+1<len(starts) else paper.index(r'\clearpage',end)
    chunks[ident]={'statement':paper[pos:end],'all':paper[start:nxt]}

def clean(s):
    s=re.sub(r'\\label\{[^}]*\}','',s)
    s=re.sub(r'%[^\n]*','',s)
    return re.sub(r'\s+',' ',s).strip()

aux=(OUT/f'{ID}_paper.aux').read_text() if (OUT/f'{ID}_paper.aux').exists() else ''
pages=dict(re.findall(r'\\newlabel\{st:([A-F]\.\d+)\}\{\{[^}]*\}\{([^}]*)\}',aux))
concord=json.loads((ROOT/'manuscript_concordance.json').read_text())
root_passages={
 'C.1':'§33; folios 221–226v; cote 140-2, scans 437–448',
 'C.2':'§33; folios 237–238; cote 140-2, scans 469–471',
 'C.3':'§§17,33; folios 69,73v,222v–225; cote 140-2, scans 139,148,440–445',
 'C.4':'§33; folios 223–225; cote 140-2, scans 441–445',
 'C.5':'§33; folio 221; cote 140-2, scan 437',
 'C.6':'§33; folio 221; cote 140-2, scan 437',
 'C.7':'§29; folios 191–191v; cote 140-2, scans 377–378',
 'C.8':'§§17,29,33; folios 69,73v,191–191v,221; cote 140-2, scans 139,148,377–378,437',
 'C.9':'§33; folio 221; cote 140-2, scan 437; §51.16, folios 733v–736v, scans 172–178',
 'C.10':'§32; folios 207–207v; cote 140-2, scans 409–410',
 'C.11':'§33; folios 225–226v; cote 140-2, scans 445–448',
 'C.12':'§33; folios 222v–226v; cote 140-2, scans 440–448'}
for n in range(13,20):root_passages[f'C.{n}']='§33; folios 221–226v; cote 140-2, scans 437–448'
for n in range(1,12):root_passages[f'D.{n}']='§8; folio 30v; cote 140-2, scan 65'
for n in range(1,40):root_passages[f'E.{n}']='§51.16; folios 733v–736v; cote 140-4, scans 172–178; §8, folio 30v, cote 140-2, scan 65'

def passages(ident,rec,chunk):
    if ident in root_passages:return root_passages[ident]
    explicit=rec.get('passage_anchors',[])
    base='; '.join(explicit) if explicit else ''
    excerpts=[]
    for m in re.finditer(r'[^\n]*(?:scans?|folio|cote|\\S\d)[^\n]*',chunk):
        line=clean(m.group(0))
        if len(line)<450 and line not in excerpts:excerpts.append(line)
    if not base:base='; '.join(excerpts)
    if ident.startswith('A.'):
        nums=[]
        for m in re.finditer(r'scans?\s+([0-9][0-9–—,; \-]*)',base):
            nums.extend(int(x) for x in re.findall(r'\d+',m.group(1)))
        folios=[f'{n}→{concord["140-2"][str(n)]["folio"]}' for n in dict.fromkeys(nums) if str(n) in concord.get('140-2',{})]
        if folios:base+='; scan→folio concordance: '+', '.join(folios)
        if not base:base='§§5–13,34; folios 7v–56,245–246v; cote 140-2, scans 19–115,483–486'
    elif ident.startswith('B.') and not base:
        base='§§8–9,32,34; folios 28v–37v,200–220v,243–248v; cote 140-2, scans 61–79,395–436,480–490'
    elif ident.startswith('F.') and not base:
        base='1983 anabelian notes; cote 149, scans 44–63,85,99–103,126–127; folios indicated by scan in this unfoliated selection'
    return base

rows=[]
for record in index:
    ident=record['id'];m=meta.get(ident,{})
    full=chunks[ident]['all'];statement=clean(chunks[ident]['statement'])
    refs=[labels.get(x,x) for x in re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',full)]
    cites=[]
    for c in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',full):cites.extend(c.split(','))
    deps=list(dict.fromkeys(refs+cites+m.get('sources',[])))
    deps=[x for x in deps if x!=ident]
    location=f'{ID}_paper.tex, statement {ident} and following proof'
    if ident in pages:location+=f'; PDF p. {pages[ident]}'
    notes=m.get('limitations','')
    status=next(s for s in ['Proved','Refuted','Known','Open']
                if re.match(r'^'+s+r'\b',record['status']))
    if record['status']!=status:notes+=' Printed qualification: '+record['status']+'.'
    if m.get('task_ids'):notes+=' Tasks: '+', '.join(m['task_ids'])+'.'
    doubt='; '.join(clean(x) for x in re.findall(r'[^\n]*(?:doubtful|reading|unsure|illegible)[^\n]*',full) if len(x)<500)
    rows.append({'id':ident,'statement':statement,'status':status,
      'where_proved':location,'depends_on':'; '.join(deps),
      'manuscript_passages (section; folio; scan)':passages(ident,m,full),
      'depends_on_doubtful_reading (scan, alternatives)':doubt or 'No theorem depends on choosing one unresolved transcription alternative.',
      'notes':notes.strip()})
columns=['id','statement','status','where_proved','depends_on',
         'manuscript_passages (section; folio; scan)',
         'depends_on_doubtful_reading (scan, alternatives)','notes']
with (OUT/f'{ID}_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(rows)

editorial=[]
for name in ['A_editorial_readings.json','B_C_editorial_readings.json','F_readings.json','Root_editorial_readings.json']:
    p=ROOT/name
    if p.exists():editorial+=json.loads(p.read_text())
readcols=['package','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly']
with (OUT/f'{ID}_readings.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=readcols);w.writeheader()
    for r in editorial:
        w.writerow({'package':r.get('package',''),'scan':r.get('scan',''),
          readcols[2]:r.get('place',r.get(readcols[2],'')),
          readcols[3]:r.get('support',r.get(readcols[3],'')),
          readcols[4]:r.get('strength',r.get(readcols[4],''))})

coverage=json.loads((ROOT/'coverage.json').read_text())
counts=Counter(r['status'] for r in rows)
report=['INCOMPLETE','',
 '| Item, lead, or task | Numbered statements | State reached |',
 '|---|---|---|']
for r in coverage:
    report.append('| '+r['task']+' | '+r['statements']+' | '+r['state'].replace('|',' / ')+' |')
report+=['','## Scope and provenance','',
 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We claim no priority. '
 'This research return records the complete proofs presently written and leaves the unresolved assertions explicitly open. '
 'A partially settled task is not counted as a finished task.',
 '',f'The paper currently has {len(rows)} numbered statements: '+', '.join(f'{n} {s}' for s,n in sorted(counts.items()))+'.',
 '', 'The local section theorem dated 6 October 2026 and the absolute open Hom theorem dated 5 October 2026 '
 'are unrefereed inputs expressly stipulated by the prompt. We inspected their specified steps and state exactly '
 'where they enter. Those deductions are not presented as an independent certification of the complete supplied proofs. '
 'Other recent supplied preprints carry the same source-specific qualifications in the paper and bibliography.',
 '', 'A `verified` bibliography flag means that the primary source was opened and the cited statement or proof step was inspected. '
 'It does not mean that the entire source was independently proved or that an unrefereed preprint has been refereed. '
 'An `unverified` flag is retained where full primary-source access was not obtained.',
 '', '## Current main results and exact remaining tasks','']
root_report=ROOT/'Root_report.md'
if root_report.exists():report.append(root_report.read_text())
report+=['','## Per-part source audits, attempts, and next steps','']
for name in ['A_audit.md','B_audit.md','C_extra_audit.md','F_audit.md','E_ross_ramified_audit.md','E_integral_detector_audit_B.md','E_integral_path_audit_B.md']:
    p=ROOT/name
    if p.exists():report+=['',f'### {name.removesuffix(".md")}', '',p.read_text()]
for name in ['A_coverage.md','B_C_coverage.md','F_coverage.md']:
    p=ROOT/name
    if p.exists():report+=['',f'### Detailed {name.removesuffix(".md")}', '',p.read_text()]

report+=['','## Typesetting and visual verification','']
check=OUT/'typesetting_check.json'
if check.exists():
    q=json.loads(check.read_text());report.append(
      f'Latest LuaLaTeX log: {q["overfull_total"]} overfull boxes, '
      f'{q["overfull_over_2pt"]} exceeding 2 pt; '
      f'{len(q["missing_characters"])} missing-character messages; '
      f'{len(q["undefined_references_or_citations"])} undefined references or citations. '
      'The actual log and the machine-readable count are retained in verification/.')
visual=ROOT/'visual_qa.json'
if visual.exists():report+=['',json.dumps(json.loads(visual.read_text()),indent=2)]
else:report+=['','Visual verification for this rebuilt checkpoint is pending; it must be completed before this PDF is released.']
report+=['','## Reproduction and package inventory','',
 'The self-contained paper source and bibliography are at the ZIP root. Modular working sections and audit metadata are retained '
 'under research/. Executed mathematical programs and their outputs are under code/. The input manifest records the supplied materials; '
 'copyrighted primary-source PDFs and the large manuscript scan collection are not duplicated in the output ZIP. '
 'They remain identified by their supplied paths, published references, and scan anchors.',
 '', 'The code performs exact finite arithmetic unless a program explicitly says otherwise. Finite certificates establish the finite '
 'claims named in their outputs; the infinite assertions are proved in the paper. The class-three cocycle vector is partially evaluated: '
 'its two rational Kummer coordinates and a primitive integral detector are computed, and its elliptic projection is identified with '
 'an explicit Ross cup-product edge. That value and integral torsion remain unevaluated. The Chebotarev prime sequence in E.38 is '
 'specified through finite arithmetic representations but was not enumerated numerically. No sampled prime calculation is promoted '
 'to a density proof.',
 '', 'No earlier checkpoint is overwritten. The final package retains every earlier checkpoint ZIP verbatim under checkpoints/, '
 'so all earlier files and passages remain available with their original hashes. The files at the root and under code/ and research/ '
 'are the current versions. Later numbered statements explicitly strengthen earlier bounds; those earlier statements remain in the paper. '
 'The checkpoint-01 packaging script completed its archive but then failed when writing the output record because of a path-expression '
 'error. The immutable archive was independently checked against every SHA-256 entry and its record recovered. The current script '
 'corrects that expression; this administrative repair changes no mathematical certificate.']
(OUT/f'{ID}_report.md').write_text('\n'.join(report)+'\n')
summary={'numbered_statements':len(rows),'status_counts':dict(counts),
         'editorial_readings':len(editorial),'coverage_rows':len(coverage),
         'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(ROOT/'register_build_output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
