#!/usr/bin/env python3
"""Mechanical checks only: no image, OCR, context, or reading assessment."""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent
BASE = 'MPL_36_053-085+39'
EXPECTED = [(36, n) for n in range(53,86)] + [(39,n) for n in range(3,21) if n not in (9,18)]
CUSTOM = set('cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible'.split())
STANDARD = set('Delta Gamma Lambda Leftrightarrow Longleftrightarrow Longrightarrow Phi Psi S Theta Updownarrow Vert alpha arrow bar begin beta bigl bigr cap cdot cdots circ cong cos deg delta det dim dot draw ell end equiv eta exists exp fbox forall foreach frac gamma ge geq hat hfill hookrightarrow in inf int kappa ker lambda ldots le left leq linewidth log longleftarrow longmapsto longrightarrow mapsto mathbb mathbf mathbin mathcal mathfrak mathrel mathrm mathscr mid mu ne neq nmid node noindent notin nu operatorname oplus otimes overline overset parbox partial phi pi psi qquad quad rho right rule sigma sim simeq sin smallmatrix subset sum supset text textcircled theta times to underbrace underline underset varepsilon varinjlim varnothing varphi varpi varprojlim widehat widetilde xi xrightarrow zeta'.split())
STANDARD_SYMBOLS = set(' &,{ }[]()\\%$#_^~'.replace(' ','')) | {' '}
STANDARD.add('bullet')
MATH_ENVS = set('aligned array cases gathered smallmatrix tikzcd equation equation* align align* gather gather*'.split())
TEXT_COMMANDS = {'text','mbox','hbox','operatorname'}
issues = []
facts = []
macro_counts = Counter()
environment_counts = Counter()

def issue(level, path, line, message):
    issues.append({'severity':level,'file':str(path.relative_to(ROOT)),'line':line,'message':message})

def coarse_position_rank(position):
    """Coarse metadata-only heuristic, not an interpretation of manuscript text."""
    pos=position.strip().lower()
    if any(word in pos for word in ('original','rotated','whole')):return None
    if re.match(r'^(?:top|upright top|above (?:first|top) line|within top note)',pos):return 0
    if re.match(r'^(?:upper[- ]middle|upper to middle)',pos):return 2
    if pos.startswith('upper'):return 1
    if re.match(r'^(?:middle[- ]lower|middle to lower|lower[- ]middle|lower middle)',pos):return 4
    if pos.startswith('middle'):return 3
    if pos.startswith('lower'):return 4
    if re.match(r'^(?:bottom|foot)',pos):return 5
    return None

def lexical_tokens(text):
    token = re.compile(r'%[^\n]*|\\(?:[A-Za-z]+|.)|\$\$|[${}]|[^\\%${}]+', re.S)
    for m in token.finditer(text):
        if m[0].startswith('%'):
            continue
        yield m.start(), m[0]

def argument(text, pos):
    """Return a balanced braced argument, without interpreting its contents."""
    while pos < len(text) and text[pos].isspace(): pos += 1
    if pos >= len(text) or text[pos] != '{': return None
    start=pos+1; depth=1; pos += 1
    while pos<len(text):
        if text[pos]=='\\':
            m=re.match(r'\\(?:[A-Za-z]+|.)',text[pos:],re.S)
            pos += len(m[0]); continue
        if text[pos]=='%':
            end=text.find('\n',pos); pos=len(text) if end<0 else end+1; continue
        if text[pos]=='{': depth+=1
        if text[pos]=='}':
            depth-=1
            if not depth:return text[start:pos],pos+1
        pos+=1
    return None

def inspect_page(path,cote,scan):
    text=path.read_text(encoding='utf-8')
    line=lambda p:text.count('\n',0,p)+1
    marks=re.findall(r'\\scanpage\{([^}]*)\}',text)
    if marks!=[str(scan)]:issue('error',path,1,f'scanpage markers {marks!r}, expected [{scan!r}]')
    cote_marks=re.findall(r'\\cotefile\{([^}]*)\}',text)
    wanted=[str(cote)] if (cote,scan) in ((36,53),(39,3)) else []
    if cote_marks!=wanted:issue('error',path,1,f'cotefile markers {cote_marks!r}, expected {wanted!r}')
    prefix=(f'\\cotefile{{{cote}}}\n' if wanted else '')+f'\\scanpage{{{scan}}}'
    if not text.startswith(prefix): issue('warning',path,1,'File does not begin with the expected page marker sequence')
    if re.search(r'\\(?:documentclass|usepackage|input|include)\b',text):issue('error',path,1,'Fragment contains a preamble or file-inclusion command')
    braces=[]; envs=[]; math_delims=[]; group_commands=[]; last_command=None; text_groups=[]
    consumed_until=-1
    for pos,tok in lexical_tokens(text):
        if pos<consumed_until:continue
        ln=line(pos)
        if tok.startswith('\\'):
            cmd=tok[1:]; macro_counts[cmd]+=1
            if cmd not in CUSTOM|STANDARD|STANDARD_SYMBOLS and cmd!='x':
                issue('error',path,ln,'Unrecognized/non-whitelisted command '+tok)
            if cmd=='x' and '\\foreach' not in text:
                issue('warning',path,ln,'\\x has no foreach declaration in this page')
            if cmd in CUSTOM:
                arg=argument(text,pos+len(tok))
                if arg is None:issue('error',path,ln,tok+' has no balanced braced argument')
                elif cmd=='diagram' and not re.search(r'\\begin\{(?:tikzcd|array)\}',arg[0]):
                    issue('warning',path,ln,'diagram argument has no tikzcd or array environment')
                elif cmd=='figure' and '\\begin{tikzpicture}' not in arg[0]:
                    issue('warning',path,ln,'figure argument has no tikzpicture environment')
                elif cmd=='illegible':
                    if not re.fullmatch(r'\d+',arg[0].strip()):issue('warning',path,ln,'illegible argument is not an integer')
                    math_context=bool(math_delims) or any(e[0] in MATH_ENVS for e in envs)
                    if math_context:
                        in_text=bool(text_groups)
                        issue('review',path,ln,'illegible occurs within a mathematical region'+(' inside a text argument; verify it represents words, not symbols' if in_text else '; verify it represents words, not symbols'))
            if cmd in ('begin','end'):
                arg=argument(text,pos+len(tok))
                if arg:
                    name,end=arg; consumed_until=end
                    if cmd=='begin':envs.append((name,ln));environment_counts[name]+=1
                    elif not envs:issue('error',path,ln,f'Unexpected end of {name}')
                    else:
                        opening,oln=envs.pop()
                        if opening!=name:issue('error',path,ln,f'Environment mismatch: {opening} opened at line {oln}, ended with {name}')
                last_command=None;continue
            if cmd in ('[','('):math_delims.append((cmd,ln))
            elif cmd in (']',')'):
                target='[' if cmd==']' else '('
                if not math_delims or math_delims[-1][0]!=target:issue('error',path,ln,f'Unexpected math closer \\{cmd}')
                else:math_delims.pop()
            last_command=cmd
        elif tok=='{':
            braces.append(ln);group_commands.append(last_command)
            if last_command in TEXT_COMMANDS:text_groups.append(len(braces))
            last_command=None
        elif tok=='}':
            if not braces:issue('error',path,ln,'Unmatched closing brace')
            else:
                if text_groups and text_groups[-1]==len(braces):text_groups.pop()
                braces.pop();group_commands.pop()
            last_command=None
        elif tok in ('$','$$'):
            if math_delims and math_delims[-1][0]==tok:math_delims.pop()
            else:math_delims.append((tok,ln))
            last_command=None
        elif tok.strip():last_command=None
    for ln in braces:issue('error',path,ln,'Unclosed opening brace')
    for name,ln in envs:issue('error',path,ln,f'Unclosed {name} environment')
    for delim,ln in math_delims:issue('error',path,ln,f'Unclosed math delimiter {delim}')
    # Delimiter sizing commands must be paired within each page at minimum.
    left=[line(m.start()) for m in re.finditer(r'\\left\b',text)]
    right=[line(m.start()) for m in re.finditer(r'\\right\b',text)]
    if len(left)!=len(right):issue('error',path,1,f'left/right count mismatch: {len(left)} vs {len(right)}')
    for m in re.finditer(r'\\(?:draw|node)\b',text):
        later=text[m.end():];semicolon=later.find(';')
        next_statement=re.search(r'\\(?:draw|node|end)\b',later)
        if semicolon<0 or (next_statement and next_statement.start()<semicolon):
            issue('warning',path,line(m.start()),'Possible missing TikZ statement semicolon')
    return text

def main():
    expected_paths=[ROOT/'pages'/f'{BASE}_{c}_scan{n:03d}.tex' for c,n in EXPECTED]
    actual=set((ROOT/'pages').glob('*.tex'))
    for missing in set(expected_paths)-actual:issue('error',missing,1,'Expected page file missing')
    for extra in actual-set(expected_paths):issue('error',extra,1,'Unexpected page file')
    page_texts=[]
    hashes={}
    for path,(cote,scan) in zip(expected_paths,EXPECTED):
        if path.exists():
            page_texts.append(inspect_page(path,cote,scan))
            hashes[str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
    facts.append(f'{len(actual)} page files; expected {len(EXPECTED)}.')
    combined=ROOT/f'{BASE}_transcription.tex'
    if combined.exists():
        intended='\n'.join(t.rstrip()+'\n' for t in page_texts)
        if combined.read_text()!=intended:issue('warning',combined,1,'Combined transcription differs from concatenation of current page files; may be concurrent audit work')
        else:facts.append('Combined transcription equals the expected ordered concatenation of all page files.')
        hashes[str(combined.relative_to(ROOT))]=hashlib.sha256(combined.read_bytes()).hexdigest()
    else:issue('error',combined,1,'Combined transcription missing')
    inventory=ROOT/f'{BASE}_inventory.csv'
    required=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
    coverage=Counter();elements=defaultdict(list);inventory_rows=[]
    with inventory.open(newline='') as f:
        rows=csv.DictReader(f)
        if rows.fieldnames!=required:issue('error',inventory,1,f'Inventory schema mismatch: {rows.fieldnames!r}')
        for row_number,row in enumerate(rows,2):
            inventory_rows.append(row)
            try:key=(int(row['cote']),int(row['scan']))
            except (KeyError,ValueError):issue('error',inventory,row_number,'Noninteger cote/scan');continue
            coverage[key]+=1;elements[key].append(row['element'])
            if key not in EXPECTED:issue('error',inventory,row_number,'Inventory contains unexpected cote/scan')
            if row['transcribed']!='yes':issue('error',inventory,row_number,'Inventory transcribed value is not yes')
            if row['sheet_kind'] not in {'text','reused_typed','cancelled_draft','cover'}:issue('error',inventory,row_number,'Unknown sheet_kind')
            if row['kind'] not in {'text','display','diagram','drawing','margin note','insertion','deletion'}:issue('error',inventory,row_number,'Unknown element kind')
            if any(row[k]=='' for k in required):issue('warning',inventory,row_number,'Empty required inventory field')
    for key in EXPECTED:
        if not coverage[key]:issue('error',inventory,1,f'No inventory rows for cote {key[0]} scan {key[1]:03d}')
        elif elements[key]!=[str(n) for n in range(1,len(elements[key])+1)]:issue('error',inventory,1,f'Nonsequential element IDs for cote {key[0]} scan {key[1]:03d}')
    facts.append(f'Inventory: {sum(coverage.values())} elements across {len(coverage)} pages.')
    page_order={page:n for n,page in enumerate(EXPECTED)}
    prior_key=None;prior_positions={}
    for csv_line,row in enumerate(inventory_rows,2):
        page=(int(row['cote']),int(row['scan']))
        current_key=(page_order[page],int(row['element']))
        if prior_key is not None and current_key<=prior_key:
            issue('error',inventory,csv_line,'Inventory page/element order is non-increasing')
        prior_key=current_key
        rank=coarse_position_rank(row['position'])
        if rank is None:continue
        prior=prior_positions.get(page)
        if prior and prior['rank']-rank>=2:
            issue('review',inventory,csv_line,f"Position-order candidate for {page[0]}/{page[1]:03d}: element {row['element']} ({row['position']}) follows element {prior['element']} ({prior['position']}, CSV line {prior['line']}); coarse metadata-only ranking, inspect before reordering")
        prior_positions[page]={'rank':rank,'position':row['position'],'element':row['element'],'line':csv_line}
    expected_rows=[]
    for record_path in sorted((ROOT/'records').glob('*.json')):
        rec=json.loads(record_path.read_text())
        for n,(kind,pos,words) in enumerate(rec['elements'],1):
            expected_rows.append({'cote':str(rec['cote']),'scan':str(rec['scan']),'sheet_kind':rec['sheet_kind'],'element':str(n),'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
    if inventory_rows!=expected_rows:issue('error',inventory,1,'Inventory differs from its source records')
    else:facts.append('Inventory exactly matches the structured element records.')
    progress=(ROOT/'progress.log').read_text()
    audited=[(int(c),int(n)) for c,n in re.findall(r'^(36|39) scan (\d{3}) audited ',progress,re.M)]
    facts.append(f'{len(audited)} audit log entries; complete page coverage: {set(audited)==set(EXPECTED)}; expected order: {audited==EXPECTED}.')
    engines={name:shutil.which(name) for name in ['pdflatex','xelatex','lualatex','latexmk','tectonic']}
    texfiles={}
    if shutil.which('kpsewhich'):
        for name in ['pdflatex.fmt','xelatex.fmt','lualatex.fmt','article.cls','amsmath.sty','amssymb.sty','tikz-cd.sty','tikz.sty','mathrsfs.sty','ulem.sty']:
            result=subprocess.run(['kpsewhich',name],capture_output=True,text=True)
            texfiles[name]=result.stdout.strip() or None
    report={'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'scope':'Mechanical syntax and inventory checks only; no visual or reading audit. Source images and context not accessed.','facts':facts,'issues':issues,'macro_counts':dict(sorted(macro_counts.items())),'environments':dict(sorted(environment_counts.items())),'engines':engines,'tex_dependencies':texfiles,'snapshot_hashes':hashes}
    destination=ROOT/'qa';destination.mkdir(exist_ok=True)
    (destination/'structural_qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    lines=['# Mechanical structural QA','',report['checked_utc'],'',report['scope'],'','## Summary','']+[f'- {x}' for x in facts]
    lines+=['','## Findings','','| Severity | File | Line | Finding |','|---|---|---:|---|']
    for item in issues:lines.append(f"| {item['severity']} | `{item['file']}` | {item['line']} | {item['message'].replace('|','&#124;')} |")
    if not issues:lines.append('| — | — | — | No mechanical findings. |')
    lines+=['','## Compilation availability','','TeX executables are present where listed below, but a real compilation requires the format, class, and packages. No compilation was attempted when these dependencies were missing.','']
    lines += [f'- `{k}`: {v or "not found"}' for k,v in {**engines,**texfiles}.items()]
    lines+=['','## Limits','','These checks do not establish completeness against the manuscript, accuracy of readings, attachment of insertions, arrow directions, or visual fidelity of drawings. The custom macros have no supplied definitions in a fragment, so their final rendering cannot be assessed here. The report hashes identify the checked byte snapshot; later root audit changes may make the report stale.','']
    (destination/'structural_qa.md').write_text('\n'.join(lines))
    print(json.dumps({'facts':facts,'issues':issues,'engines':engines,'tex_dependencies':texfiles},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
