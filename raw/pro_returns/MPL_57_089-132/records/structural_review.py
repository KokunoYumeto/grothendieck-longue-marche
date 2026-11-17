#!/usr/bin/env python3
"""Read-only source/metadata heuristics; never opens scans or context.

Writes only its requested Markdown report. No findings are corrected automatically.
The results are structural observations, not judgments about manuscript readings.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import re


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    pkg = module(root / 'records/package_tools.py', 'pkg')
    rec = module(root / 'records/refresh_doubts.py', 'rec')
    errors, warnings, scans, missing, rowcount, doubts = pkg.validate(root, complete=True)
    records, record_errors, record_warnings = rec.read_records(root / 'records')
    issues = []
    controls = []
    commands = defaultdict(Counter)
    macro_differences = []
    prime_markers = []
    quote_markers = []
    pic_forms = defaultdict(Counter)
    arrow_count = 0
    custom = {'cotefile','scanpage','mspage','deleted','inserted','margin','uline','uuline','diagram','figure','unsure','illegible'}
    inv = list(csv.DictReader((root / f'{pkg.STEM}_inventory.csv').open(newline='')))
    inv_counts = Counter((int(row['scan']),row['kind']) for row in inv)
    inventory_issues = []
    seen = {}
    sheet_kinds = defaultdict(set)
    for line,row in enumerate(inv,2):
        for key,value in row.items():
            if value is None or not value.strip():
                inventory_issues.append(f'CSV line {line}: empty {key}')
        key = (row['cote'],row['scan'],row['element'])
        if key in seen:
            inventory_issues.append(f'CSV line {line}: element identifier also occurs at line {seen[key]}')
        seen[key]=line
        sheet_kinds[int(row['scan'])].add(row['sheet_kind'])
    for scan,kinds in sheet_kinds.items():
        if len(kinds)>1:
            inventory_issues.append(f'Scan {scan:03d}: multiple sheet kinds {sorted(kinds)}')

    def walk(value, location):
        if isinstance(value,str):
            hits=[f'U+{ord(c):04X} at offset {i}' for i,c in enumerate(value) if ord(c)<32 or ord(c)==127]
            if hits: controls.append(f'{location}: '+', '.join(hits))
        elif isinstance(value,list):
            for i,item in enumerate(value): walk(item,f'{location}[{i}]')
        elif isinstance(value,dict):
            for key,item in value.items(): walk(item,f'{location}.{key}')
    for path in sorted((root/'records').glob('scan*.json')):
        walk(json.loads(path.read_text()),path.name)

    def grouped(text, pos, opening='{', closing='}'):
        while pos<len(text) and text[pos].isspace(): pos+=1
        if pos>=len(text) or text[pos]!=opening: return None
        start=pos; depth=1; pos+=1; braces=0
        while pos<len(text):
            c=text[pos]
            if not pkg.escaped(text,pos):
                if opening=='[':
                    if c=='{': braces+=1
                    elif c=='}': braces-=1
                if braces==0:
                    if c==opening: depth+=1
                    elif c==closing: depth-=1
                if depth==0:return start,pos+1,text[start+1:pos]
            pos+=1
        return None

    for scan,path in pkg.page_files(root):
        original=path.read_text(); text=pkg.uncomment(original)
        line=lambda pos: text.count('\n',0,pos)+1
        prefix=lambda pos: f'Scan {scan:03d}, source line {line(pos)}'
        for i,c in enumerate(original):
            if (ord(c)<32 and c not in '\n\r\t') or ord(c)==127:
                controls.append(f'{path.name}: U+{ord(c):04X} at offset {i}')
        underlines=[]; text_groups=[]
        for m in re.finditer(r'\\([A-Za-z]+)',text):
            if pkg.escaped(text,m.start()):continue
            cmd=m.group(1);commands[cmd][scan]+=1
            if cmd in custom:
                argument=grouped(text,m.end())
                if argument is None:issues.append(f'{prefix(m.start())}: malformed braced argument for \\{cmd}')
                elif cmd=='illegible' and not re.fullmatch(r'\s*\d+\s*',argument[2]):
                    issues.append(f'{prefix(m.start())}: illegible argument is not a word-count integer')
                elif not argument[2].strip():issues.append(f'{prefix(m.start())}: empty \\{cmd} argument')
            if cmd in {'underline','uline','uuline','text'}:
                argument=grouped(text,m.end())
                if argument:
                    (text_groups if cmd=='text' else underlines).append((m.start(),argument[1],cmd))
            if cmd in {'includegraphics','input','include','documentclass','newcommand','renewcommand','def'}:
                issues.append(f'{prefix(m.start())}: \\{cmd} requires review for fragment/source-image constraints')
            if cmd=='arrow':
                arrow_count+=1
                argument=grouped(text,m.end(),'[',']')
                if argument is None:
                    issues.append(f'{prefix(m.start())}: arrow has no balanced optional argument; check legacy syntax manually')
                else:
                    quotes=[i for i,c in enumerate(argument[2]) if c=='"' and not pkg.escaped(argument[2],i)]
                    if len(quotes)%2:issues.append(f'{prefix(m.start())}: odd count of TikZ label double quotes in arrow options')
        stack=[]; environment_ranges=[]
        for m in re.finditer(r'\\(begin|end)\s*\{([^{}]+)\}',text):
            action,env=m.groups()
            if action=='begin': stack.append((env,m.start(),m.end()))
            elif not stack:issues.append(f'{prefix(m.start())}: unmatched end of {env}')
            elif stack[-1][0]!=env:issues.append(f'{prefix(m.start())}: environment {stack[-1][0]} ended as {env}')
            else:
                _,start,body_start=stack.pop();environment_ranges.append((start,m.end(),env,body_start,m.start()))
        issues.extend(f'{prefix(start)}: unclosed {env}' for env,start,_ in stack)
        for opening,closing in [('\\[','\\]'),('\\(','\\)')]:
            opens=[m.start() for m in re.finditer(re.escape(opening),text) if not pkg.escaped(text,m.start())]
            closes=[m.start() for m in re.finditer(re.escape(closing),text) if not pkg.escaped(text,m.start())]
            if len(opens)!=len(closes):issues.append(f'Scan {scan:03d}: {opening} count differs from {closing} count')
            balance=0
            for pos,change in sorted([(i,1) for i in opens]+[(i,-1) for i in closes]):
                balance+=change
                if balance<0:issues.append(f'{prefix(pos)}: {closing} before {opening}');break
        dollars=[m.start() for m in re.finditer(r'\$',text) if not pkg.escaped(text,m.start())]
        if len(dollars)%2:issues.append(f'Scan {scan:03d}: odd unescaped dollar count')
        math_ranges=[(dollars[i],dollars[i+1]) for i in range(0,len(dollars)-1,2)]
        math_ranges.extend((start,end) for start,end,env,_,_ in environment_ranges if env in {'tikzcd','array','aligned','align','equation','gather'})
        math_ranges.extend((m.start(),m.end()) for m in re.finditer(r'\\\[.*?\\\]',text,re.S))
        math_ranges.extend((m.start(),m.end()) for m in re.finditer(r'\\\(.*?\\\)',text,re.S))
        in_math=lambda pos: any(a<=pos<b for a,b in math_ranges) and not any(a<=pos<b for a,b,_ in text_groups)
        for m in re.finditer(r'\^\s*!|\^\s*\{[^{}]*![^{}]*\}|\\prime\b|[A-Za-z0-9}]\s*\x27{1,2}',text):
            if in_math(m.start()) or '\\prime' in m.group():
                prime_markers.append((scan,line(m.start()),m.group().replace('\n',' ')))
        tikz_ranges=[(start,end) for start,end,env,_,_ in environment_ranges if env in {'tikzcd','tikzpicture'}]
        for m in re.finditer(r'"|[“”«»]|``|\x27\x27',text):
            if m.group()=='"' and any(a<=m.start()<b for a,b in tikz_ranges):continue
            if in_math(m.start()):continue
            quote_markers.append((scan,line(m.start()),m.group()))
        for m in re.finditer(r'\\(?:mathrm|operatorname)\{Pic\}',text):
            wrapping=sorted(((b-a,cmd) for a,b,cmd in underlines if a<=m.start()<b))
            form=(wrapping[0][1]+' + ' if wrapping else 'bare ')+m.group()
            pic_forms[form][scan]+=1
        for macro,kind in [('diagram','diagram'),('figure','drawing'),('margin','margin note'),('inserted','insertion'),('deleted','deletion')]:
            n=commands[macro][scan];ni=inv_counts[(scan,kind)]
            if n!=ni:macro_differences.append((scan,macro,kind,n,ni))
        for start,end,env,body_start,body_end in environment_ranges:
            if env!='tikzpicture':continue
            body=text[body_start:body_end]
            starts=list(re.finditer(r'\\(?:draw|node)\b',body))
            for index,m in enumerate(starts):
                stop=starts[index+1].start() if index+1<len(starts) else len(body)
                if ';' not in body[m.end():stop]:
                    issues.append(f'{prefix(body_start+m.start())}: TikZ draw/node statement has no semicolon before next command/end')

    audit_count=sum('audit' in record for record in records)
    out=['# Mechanical review of page sources and metadata','',datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'',f'{len(scans)} page files; {rowcount} inventory rows; {len(records)} page records, of which {audit_count} contain reader audit metadata; {len(doubts)} doubt macro instances; {arrow_count} TikZ arrow commands.','','This review reads only transcription files and their metadata. It does not inspect scans or context, adjudicate readings, establish omissions, or replace the visual audit. The earlier partial combined transcription may intentionally be stale during auditing.','','## Basic validation','']
    out.extend(['- '+e for e in errors+warnings] or ['No errors or warnings.'])
    for title,items in [('Record schema',record_errors+record_warnings),('Control characters',controls),('Additional structural and TikZ heuristics',issues),('Inventory field/identifier checks',inventory_issues)]:
        out.extend(['','## '+title,'']);out.extend(['- '+e for e in items] or ['No issues detected.'])
    explained={
        (92,'margin',3,1):'Explained: two margin macros contain diagrams covered by diagram inventory rows 14–15; the remaining macro is margin-note row 18.',
        (94,'margin',4,3):'Explained: one margin macro contains the cancelled diagram and associated cancelled condition, covered by diagram/deletion rows 7–8.',
        (94,'deleted',10,4):'Explained: six deleted object/relation labels are inside the diagram covered by diagram row 7; four other deletion rows describe the remaining cancelled blocks.',
        (97,'margin',4,6):'Explained: one margin macro is the cancelled note covered by deletion row 33; three table annotations are separately covered by margin-note rows 9, 13, and 14.',
        (97,'deleted',10,9):'Explained: deletion row 24 explicitly groups the two separately marked deleted T tokens.',
        (102,'margin',4,3):'Explained: one margin macro contains the diagram covered by diagram row 4.',
        (102,'inserted',1,5):'Explained: four labels placed beneath relations are represented using underset, and covered by insertion rows 17 and 19–21.',
        (105,'margin',3,2):'Explained: one margin macro wraps the cancelled note covered by deletion row 19.',
        (111,'margin',4,2):'Explained: two margin macros contain diagrams covered by diagram rows 14–15.',
        (111,'margin',5,2):'Explained: two margin macros contain diagrams and one contains the audit-added separating-stroke drawing; those elements are inventoried by their diagram/drawing kinds.',
        (112,'deleted',8,6):'Explained: three paragraph-level deletion macros represent the cancelled whole manuscript body covered collectively by deletion row 1; the five inner cancellations have their own rows.',
        (117,'margin',1,2):'Explained: margin-note row 2 is the top-center number 20 represented by mspage; the bottom number has the margin macro.',
        (117,'margin',8,2):'Explained: seven margin macros wrap audit-added drawings; the two margin-note rows describe one margin macro and the top-center mspage number 20.',
        (119,'margin',2,3):'Explained: margin-note row 1 is the top-center number 19 represented by mspage; the other two margin notes have margin macros.',
        (119,'margin',14,3):'Explained: twelve margin macros wrap audit-added drawings; the three margin-note rows describe two margin macros and the top-center mspage number 19.',
        (124,'margin',2,1):'Explained: one margin macro wraps the audit-added emphasis-stroke drawing, inventoried as a drawing.',
        (126,'margin',3,2):'Explained: one margin macro wraps the audit-added emphasis-stroke drawing, inventoried as a drawing.',
        (127,'margin',5,4):'Explained: one margin macro wraps the audit-added pointer drawing, inventoried as a drawing.',
        (129,'margin',2,1):'Explained: one margin macro wraps the audit-added corollary-stroke drawing, inventoried as a drawing.',
        (131,'margin',3,2):'Explained: one margin macro wraps the audit-added lemma-stroke drawing, inventoried as a drawing.'
    }
    out.extend(['','## Macro-to-inventory counts','','A discrepancy can reflect nested or grouped elements. The explanations below use only explicit source nesting and inventory labels. They do not certify visual completeness. Explanations apply only to the listed count pairs.','','| Scan | Macro | Inventory kind | Macro count | Row count | Structural explanation |','|---|---|---|---:|---:|---|'])
    out.extend(f'| {s:03d} | `{m}` | {k} | {n} | {ni} | {explained.get((s,m,n,ni),"Unclassified count difference; visual reader to assess.")} |' for s,m,k,n,ni in macro_differences)
    out.extend(['','## Prime/exclamation candidates','','These are literal source tokens identified in math-like regions. They are not classifications of manuscript ink. Apostrophes inside notation can have several roles.','','| Scan | Source line | Token |','|---|---:|---|'])
    out.extend(f'| {s:03d} | {line} | `{token}` |' for s,line,token in prime_markers)
    out.extend(['','## Quote-token counts outside TikZ syntax','','Math-region tokens are excluded, except in explicit text groups, so double primes are not counted as closing quotation marks. Literal double quotes inside TikZ environments are excluded because arrow-label syntax uses them. Paired backticks/apostrophes are counted as tokens, not globally paired across unrelated passages. The scan 117 source shares one closing quote between a deleted opening and its inserted replacement; scan 127 uses three standalone opening-quote tokens in inserted labels. These structural facts explain their count imbalances without changing readings.','','| Scan | Token | Count |','|---|---|---:|'])
    quote_counts=Counter((s,token) for s,_,token in quote_markers)
    for (s,token),n in sorted(quote_counts.items()):
        name={'``':'two backticks',"''":'two apostrophes','"':'literal double quote','“':'left curly double quote','”':'right curly double quote','«':'left guillemet','»':'right guillemet'}[token]
        out.append(f'| {s:03d} | {name} | {n} |')
    out.extend(['','## Pic macro variants','','The table reports lexical variants only. An underlined occurrence and a bare occurrence may both accurately represent the page.','','| Variant | Scan: count |','|---|---|'])
    out.extend(f'| `{variant}` | '+', '.join(f'{s:03d}: {n}' for s,n in sorted(counter.items()))+' |' for variant,counter in sorted(pic_forms.items()))
    out.extend(['','## Greek command variants','','All distinctions are preserved; their presence is not a reason to normalize any reading.','','| Command | Scan: count |','|---|---|'])
    greek=['alpha','beta','gamma','Gamma','delta','Delta','epsilon','varepsilon','zeta','eta','theta','vartheta','Theta','iota','kappa','lambda','Lambda','mu','nu','xi','Xi','pi','varpi','Pi','rho','varrho','sigma','Sigma','tau','upsilon','Upsilon','phi','varphi','Phi','chi','psi','Psi','omega','Omega']
    for cmd in greek:
        if commands[cmd]:out.append(f'| `\\{cmd}` | '+', '.join(f'{s:03d}: {n}' for s,n in sorted(commands[cmd].items()))+' |')
    target=args.report or root/'records/mechanical_review_full_pass.md'
    target.write_text('\n'.join(out)+'\n')
    print(target)
    print(f'{len(scans)} pages; {len(issues)} additional structural issues; {len(controls)} control-character issues; {len(macro_differences)} macro/inventory count differences.')
    for item in issues:print(item)
    print('Prime/exclamation candidate counts:',dict(Counter(token for _,_,token in prime_markers)))
    print('Quote-token counts:',dict(quote_counts))
    print('Inventory differences:',macro_differences)


if __name__=='__main__':main()
