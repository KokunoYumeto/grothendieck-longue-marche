#!/usr/bin/env python3
"""Final read-only validation of the pages, concatenation, and inventory.

Only explicitly named TeX/CSV inputs are read. No scans/context are accessed.
Output is a JSON technical record, never a change to manuscript inputs.
"""
from pathlib import Path
import argparse, collections, csv, datetime, hashlib, json, re
from static_latex_check import Checker, TOK

EXPECTED_SCANS = [n for n in range(46, 90) if n not in {79, 88}]
STANDARD_ENVIRONMENTS = {'aligned', 'array', 'tabular', 'tikzcd', 'tikzpicture', 'pgfonlayer', 'gathered'}
EDITORIAL = set('cotefile scanpage unsure deleted inserted margin diagram figure uline uuline'.split())
STANDARD = set('''Delta Gamma Longleftrightarrow Longrightarrow Omega Phi Pi Sigma
Vert alpha arrow bar begin begingroup beta bigl bigr bigwedge boxed bullet cdot
cdots chi circ coordinate coprod cos dfrac displaystyle downarrow draw ell end
endgroup ensuremath exists fill forall foreach frac gamma geq hfill in infty
lambda ldots leadsto left leftarrow leftrightarrow leq longleftarrow
longleftrightarrow longmapsto longrightarrow mathbb mathbf mathcal mathfrak
mathord mathrm mid middle mp mu ne node nu omega operatorname overbrace overline
overset par pgfdeclarelayer pgfsetlayers pi pm prod qquad quad rho right rule
scriptsize setminus sigma sim simeq sin subset substack sum supset tau text
textcircled textsc textsuperscript texttt tfrac times to underbrace underline
underset varepsilon varnothing varphi varprojlim vdots vee vphantom wedge
widehat widetilde xi xrightarrow zeta'''.split())
SYMBOLS = {r'\\', r'\&', r'\ ', r'\,', r'\;', r'\:', r'\!', r'\{', r'\}',
           r'\[', r'\]', r'\(', r'\)', r'\#', r'\%', r'\_', r'\-', r'\$'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def local_loops(c):
    loops=[]
    for m in re.finditer(r'\\foreach\s+(.*?)\s+in\s*', c.s, re.S):
        variables=re.findall(r'\\([A-Za-z@]+)',m[1])
        values=c.group(m.end(),len(c.s))
        body=c.group(values[1]+1,len(c.s)) if values else None
        if body:
            loops.append({'variables':variables,'start':m.start(),'end':body[1]+1,
                          'line':c.line(m.start()), 'values':c.s[values[0]+1:values[1]]})
    return loops


def command_review(c):
    loops=local_loops(c)
    counts=collections.Counter()
    unknown=[]
    symbol_counts=collections.Counter()
    for m in TOK.finditer(c.s):
        t=m[0]
        if not t.startswith('\\'):
            continue
        if re.fullmatch(r'\\[A-Za-z@]+',t):
            name=t[1:]
            counts[name]+=1
            local=any(name in x['variables'] and x['start']<=m.start()<x['end'] for x in loops)
            if name not in EDITORIAL|STANDARD and not local:
                unknown.append({'file':c.path.name,'line':c.line(m.start()),'command':t})
        else:
            symbol_counts[t]+=1
            if t not in SYMBOLS:
                unknown.append({'file':c.path.name,'line':c.line(m.start()),'command':t})
    groups=[]
    delimiters=[]
    for m in TOK.finditer(c.s):
        t=m[0]
        if t==r'\begingroup': groups.append(m.start())
        elif t==r'\endgroup':
            if groups: groups.pop()
            else: unknown.append({'file':c.path.name,'line':c.line(m.start()),'issue':'unmatched endgroup'})
        elif t==r'\left': delimiters.append(m.start())
        elif t==r'\right':
            if delimiters: delimiters.pop()
            else: unknown.append({'file':c.path.name,'line':c.line(m.start()),'issue':'unmatched right delimiter'})
    for p in groups: unknown.append({'file':c.path.name,'line':c.line(p),'issue':'unclosed begingroup'})
    for p in delimiters: unknown.append({'file':c.path.name,'line':c.line(p),'issue':'unclosed left delimiter'})
    return {'commands':dict(sorted(counts.items())), 'control_symbols':dict(sorted(symbol_counts.items())),
            'local_foreach_variables':loops, 'unknown_or_group_issues':unknown}


def matrix_review(c):
    diagrams=[]
    problems=[]
    for begin,(content,stop,finish,name) in sorted(c.envs.items()):
        if name!='tikzcd': continue
        opt=c.brackets(content,stop)
        options=c.s[opt[0]+1:opt[1]] if opt else ''
        start=opt[1]+1 if opt else content
        row,col=1,1
        cells=[]
        i=part=start
        while i<stop:
            if c.s[i]=='{' and i in c.groups:
                i=c.groups[i]+1; continue
            if c.s.startswith(r'\begin',i) and i in c.envs:
                i=c.envs[i][2]; continue
            if c.s[i]=='\\':
                m=TOK.match(c.s,i)
                t=m[0] if m else c.s[i]
                if t==r'\arrow':
                    a=c.brackets(m.end(),stop)
                    i=a[1]+1 if a else m.end(); continue
                if t in {r'\&',r'\\'}:
                    cells.append({'row':row,'column':col,'start':part,'end':i,
                                  'source':c.s[part:i].strip()})
                    i=m.end()
                    if t==r'\&': col+=1
                    else:
                        row+=1; col=1
                        a=c.brackets(i,stop)
                        if a: i=a[1]+1
                    part=i; continue
                i=m.end() if m else i+1; continue
            if c.s[i]=='&':
                problems.append({'file':c.path.name,'line':c.line(i),'issue':'raw ampersand in replacement matrix'})
            i+=1
        cells.append({'row':row,'column':col,'start':part,'end':stop,'source':c.s[part:stop].strip()})
        indexed={(x['row'],x['column']):x for x in cells}
        references=[]
        for a in c.arrows:
            if not start<=a['offset']<stop: continue
            source=next((x for x in cells if x['start']<=a['offset']<x['end']),None)
            if not source:
                problems.append({'file':c.path.name,'line':a['line'],'issue':'arrow source cell not located'}); continue
            d=a['direction']
            if not d:
                problems.append({'file':c.path.name,'line':a['line'],'issue':'arrow has no recognized relative direction'}); continue
            target=(source['row']+d.count('d')-d.count('u'),source['column']+d.count('r')-d.count('l'))
            dest=indexed.get(target)
            exists=bool(dest and dest['source'])
            ref={'line':a['line'],'source':[source['row'],source['column']],
                 'direction':d,'target':list(target),'target_exists':exists,
                 'explicit_empty_target':bool(dest and dest['source']=='{}')}
            references.append(ref)
            if not exists:
                problems.append({'file':c.path.name,'line':a['line'],'issue':'arrow targets a missing or blank matrix cell',**ref})
        matrix_name=re.search(r'every matrix/\.append style=\{\s*/tikz/name=([A-Za-z0-9_-]+)\s*\}',options)
        construction=[]
        if matrix_name:
            prefix=matrix_name[1]
            for m in re.finditer(re.escape(prefix)+r'-(\d+)-(\d+)(?:\.[A-Za-z ]+)?',options):
                target=tuple(map(int,m.groups()))
                dest=indexed.get(target)
                exists=bool(dest and dest['source'])
                ref={'line':c.line(opt[0]+1+m.start()),'target':list(target),'target_exists':exists}
                construction.append(ref)
                if not exists: problems.append({'file':c.path.name,'issue':'construction path references absent matrix cell',**ref})
        if 'ampersand replacement=\\&' not in options:
            problems.append({'file':c.path.name,'line':c.line(begin),'issue':'missing explicit ampersand replacement'})
        diagrams.append({'file':c.path.name,'begin_line':c.line(begin),'rows':row,
                         'columns':max(x['column'] for x in cells),
                         'row_lengths':dict(sorted(collections.Counter(x['row'] for x in cells).items())),
                         'arrow_references':references,'construction_references':construction})
    return {'diagrams':diagrams,'issues':problems}


def named_picture_refs(c):
    pictures=[]
    issues=[]
    for begin,(start,stop,finish,name) in sorted(c.envs.items()):
        if name!='tikzpicture': continue
        body=c.s[start:stop]
        declarations=set(re.findall(r'\\(?:node|coordinate)\s*(?:\[[^]]*\]\s*)?\(([A-Za-z][A-Za-z0-9_-]*)\)',body))
        refs=[]
        for m in re.finditer(r'\((?:\[[^]]*\])?([A-Za-z][A-Za-z0-9_-]*)(?:\.[A-Za-z ]+)?\)',body):
            ref={'name':m[1],'line':c.line(start+m.start()),'declared':m[1] in declarations}
            refs.append(ref)
            if not ref['declared']: issues.append({'file':c.path.name,'issue':'unresolved named TikZ coordinate',**ref})
        pictures.append({'file':c.path.name,'begin_line':c.line(begin),'declarations':sorted(declarations),'references':refs})
    return {'pictures':pictures,'issues':issues}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'final_validation.json')
    args=ap.parse_args()
    pages=sorted((args.root/'pages').glob('*.tex'))
    combined=args.root/'MPL_138_046-089_transcription.tex'
    inventory=args.root/'MPL_138_046-089_inventory.csv'
    checks=[Checker(p).run() for p in pages+[combined]]
    page_checks=checks[:-1]
    blockers=[]
    cmd_results={}
    matrices={}
    pictures={}
    for c in checks:
        blockers.extend(c.findings)
        cmd_results[c.path.name]=command_review(c)
        matrices[c.path.name]=matrix_review(c)
        pictures[c.path.name]=named_picture_refs(c)
        blockers.extend(cmd_results[c.path.name]['unknown_or_group_issues'])
        blockers.extend(matrices[c.path.name]['issues'])
        blockers.extend(pictures[c.path.name]['issues'])
    actual_scans=[int(re.search(r'scan(\d+)\.tex$',p.name)[1]) for p in pages]
    marker_errors=[]
    for c,n in zip(page_checks,actual_scans):
        markers=[int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',c.s)]
        if markers!=[n]: marker_errors.append({'file':c.path.name,'markers':markers,'expected':n})
    if actual_scans!=EXPECTED_SCANS: blockers.append({'issue':'page scan set/order mismatch','actual':actual_scans})
    blockers.extend(marker_errors)
    raw_parts=[p.read_bytes() for p in pages]
    combined_bytes=combined.read_bytes()
    expected_bytes=b'\n'.join(raw_parts)
    concat={'exact_ordered_pages_with_one_lf_separator':combined_bytes==expected_bytes,
            'direct_without_added_separators':combined_bytes==b''.join(raw_parts),
            'separator_hex':'0a','separator_count':len(pages)-1,
            'page_bytes_total':sum(map(len,raw_parts)),'combined_bytes':len(combined_bytes),
            'expected_sha256':sha(expected_bytes),'actual_sha256':sha(combined_bytes),
            'scan_markers':[int(x) for x in re.findall(rb'\\scanpage\{(\d+)\}',combined_bytes)]}
    if not concat['exact_ordered_pages_with_one_lf_separator']: blockers.append({'issue':'combined transcription differs from ordered source bytes'})
    if concat['scan_markers']!=EXPECTED_SCANS: blockers.append({'issue':'combined scan markers mismatch'})
    with inventory.open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
    ids=collections.Counter(r['element'] for r in rows)
    inv_scans=sorted(set(int(r['scan']) for r in rows))
    bad_ids=[{'csv_line':i+2,'scan':r['scan'],'element':r['element']} for i,r in enumerate(rows)
             if not re.fullmatch(f"{int(r['scan']):03d}-[0-9]+",r['element'])]
    inv={'fields':fields,'rows':len(rows),'unique_ids':len(ids),'duplicate_ids':[k for k,v in ids.items() if v>1],
         'scans':inv_scans,'exact_scan_set':inv_scans==EXPECTED_SCANS,
         'cotes':dict(collections.Counter(r['cote'] for r in rows)),
         'statuses':dict(collections.Counter(r['transcribed'] for r in rows)),
         'bad_element_scan_prefixes':bad_ids,
         'rows_per_scan':dict(sorted(collections.Counter(int(r['scan']) for r in rows).items())),
         'malformed_rows':[i+2 for i,r in enumerate(rows) if None in r or any(v is None for v in r.values())]}
    if inv['duplicate_ids'] or bad_ids or inv['malformed_rows'] or not inv['exact_scan_set'] or inv['statuses']!={'yes':len(rows)} or inv['cotes']!={'138':len(rows)}:
        blockers.append({'issue':'inventory integrity failure','details':inv})
    current_hashes={p.name:sha(p.read_bytes()) for p in pages+[combined,inventory]}
    env_counts=collections.Counter(name for c in page_checks for _,_,_,name in c.envs.values())
    unknown_envs=sorted(set(env_counts)-STANDARD_ENVIRONMENTS)
    changed=[c.path.name for c in checks if sha(c.raw.encode('utf-8'))!=current_hashes[c.path.name]]
    if unknown_envs or changed:
        blockers.append({'unrecognized_environments':unknown_envs,'changed_during_validation':changed})
    result={'validation_kind':'STATIC_ONLY_NO_COMPILE','status':'PASS' if not blockers else 'BLOCKERS_FOUND',
       'generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'scope':'42 saved page sources, combined TeX, and inventory CSV only; no images/context/archive access',
       'expected_scans':EXPECTED_SCANS,'actual_page_scans':actual_scans,'file_sha256':current_hashes,
       'final_environment_inventory':dict(sorted(env_counts.items())),
       'unrecognized_environments':unknown_envs,'input_hashes_stable_during_validation':not changed,
       'changed_during_validation':changed,
       'editorial_macro_allowlist':sorted(EDITORIAL),'standard_command_allowlist':sorted(STANDARD),
       'command_review':cmd_results,'static_findings':{c.path.name:c.findings for c in checks},
       'underlining_in_math':{c.path.name:c.ulines for c in checks},
       'tikzcd':matrices,'tikz_named_coordinates':pictures,
       'concatenation':concat,'inventory':inv,'blockers':blockers,
       'limitations':['Static token analysis does not expand arbitrary TeX macros.',
         'Editorial macro definitions are required and must preserve caller mode and accept their saved paragraph/display arguments.',
         'No mathematical or manuscript-reading correctness is asserted.',
         'An explicitly created empty TikZ target is accepted as a technical node; its intended geometry is not judged.',
         'No successful compilation is claimed.']}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'files':len(checks),'inventory_rows':len(rows),
        'page_tikzcd_diagrams':sum(len(matrices[c.path.name]['diagrams']) for c in page_checks),
        'page_arrows':sum(len(c.arrows) for c in page_checks),'blockers':blockers},ensure_ascii=False,indent=2))


if __name__=='__main__': main()
