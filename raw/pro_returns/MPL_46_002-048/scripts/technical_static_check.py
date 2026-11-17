#!/usr/bin/env python3
"""Read-only syntax checks; no image/context access or manuscript changes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import re

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("archive_tools", ROOT/"scripts/archive_tools.py")
archive_tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archive_tools)
APPROVED = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
STANDARD = set("Delta Gamma Longleftrightarrow Longrightarrow Omega Rightarrow S Sigma Vert alpha arrow begin beta bigcup bigl bigr bigwedge boxed bullet cdots check circ cup dashrightarrow delta dfrac draw end exists forall frac geqslant hfill in lambda langle ldots left longleftarrow longleftrightarrow longmapsto longrightarrow mapsto mathbb mathbf mathbin mathcal mathrm mu ne node nu omega operatorname otimes overline overset par partial pi qquad quad rangle rho right rightarrow rightsquigarrow sim simeq subset substack supset text textcircled textsuperscript times to underbrace underline underset varphi varprojlim widetilde wr xi xrightarrow".split())
TEXT_MACROS = set("text mbox hbox textnormal textbf textrm textit textsf texttt textup textsl textsc".split())

def tokens(s):
    i=0
    while i<len(s):
        start=i
        c=s[i]
        if c=="%":
            end=s.find("\n",i)
            i=len(s) if end<0 else end
            continue
        if c=="\\":
            i+=1
            if i>=len(s):
                yield ("command","",start,i)
                break
            if s[i].isalpha():
                j=i
                while i<len(s) and s[i].isalpha(): i+=1
                yield ("command",s[j:i],start,i)
            else:
                i+=1
                yield ("command",s[start+1:i],start,i)
            continue
        if c=="$":
            i+=1
            if i<len(s) and s[i]=="$": i+=1
            yield ("math",s[start:i],start,i)
            continue
        i+=1
        yield ("character",c,start,i)

def next_nonspace(s,i):
    while i<len(s) and s[i].isspace(): i+=1
    return i

def arrow_options(s,start):
    """Find optional argument end, ignoring brackets inside brace groups."""
    i=next_nonspace(s,start)
    if i>=len(s) or s[i]!="[":
        return None
    start=i
    depth=1
    braces=0
    quote=False
    quote_count=0
    for kind,value,a,b in tokens(s[start+1:]):
        a+=start+1;b+=start+1
        if kind!="character":
            continue
        if value=="{": braces+=1
        elif value=="}": braces-=1
        elif value=='"':
            quote=not quote
            quote_count+=1
        elif value=="[" and braces==0 and not quote:
            depth+=1
        elif value=="]" and braces==0 and not quote:
            depth-=1
            if depth==0:
                return (start,b,quote_count,False)
    return (start,len(s),quote_count,True)

def check_page(path):
    source=path.read_text(encoding="utf-8")
    issues=[]
    archive_tools.tex_structure(path,issues)
    commands=set()
    modes=[]
    groups=[]
    last_command=None
    environments=[]
    lefts=[]
    arrow_count=0
    def error(at,msg):
        issues.append(f"{path.name}:{source.count(chr(10),0,at)+1}: {msg}")
    for kind,value,start,end in tokens(source):
        if kind=="command":
            if value.isalpha():
                commands.add(value)
            if value in APPROVED:
                j=next_nonspace(source,end)
                if j>=len(source) or source[j]!="{":
                    error(start,f"approved macro \\{value} has no braced argument")
            if value in {"[","("}:
                if modes and not any(g in TEXT_MACROS for g in groups):
                    error(start,f"nested explicit math opener \\{value}")
                modes.append(("\\"+value,start))
            elif value in {"]",")"}:
                expected="\\"+{"]":"[",")":"("}[value]
                if not modes or modes[-1][0]!=expected:
                    error(start,f"math closer \\{value} has no matching opener")
                else:
                    modes.pop()
            elif value in {"begin","end"}:
                match=re.match(r"\s*\{([^{}]+)\}",source[end:])
                if match:
                    environment=match.group(1)
                    if value=="begin":
                        if environment in {"aligned","gathered","split","alignedat"}:
                            if not modes and "tikzcd" not in environments:
                                error(start,f"{environment} appears outside explicit math or a tikzcd cell")
                        environments.append(environment)
                    elif environments:
                        environments.pop()
            elif value=="left":
                lefts.append(start)
            elif value=="right":
                if lefts: lefts.pop()
                else: error(start,r"\right has no preceding \left")
            elif value=="arrow":
                arrow_count+=1
                result=arrow_options(source,end)
                if result:
                    a,b,count,unclosed=result
                    if unclosed:
                        error(start,"arrow optional argument or double-quoted label is unclosed")
                    elif count%2:
                        error(start,"arrow label has an odd number of double quotation marks")
            last_command=value
        elif kind=="math":
            if modes and modes[-1][0]==value:
                modes.pop()
            else:
                if modes and not any(g in TEXT_MACROS for g in groups):
                    error(start,f"nested/mismatched explicit math delimiter {value}")
                modes.append((value,start))
            last_command=None
        elif value=="{":
            groups.append(last_command)
            last_command=None
        elif value=="}":
            if groups: groups.pop()
            last_command=None
        elif not value.isspace():
            last_command=None
    for mode,at in modes:
        error(at,f"unclosed explicit math delimiter {mode}")
    for at in lefts:
        error(at,r"\left has no matching \right")
    unknown=commands-APPROVED-STANDARD
    if unknown:
        issues.append(f"{path.name}: unrecognized command token(s): "+", ".join("\\"+x for x in sorted(unknown)))
    return issues,arrow_count

def main():
    issues=[]
    arrow_count=0
    before={}
    for scan in archive_tools.SCANS:
        path=archive_tools.page_path(ROOT,scan)
        before[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
        found,count=check_page(path)
        issues.extend(found)
        arrow_count+=count
    changed=[name for name,digest in before.items()
             if hashlib.sha256((ROOT/"pages"/name).read_bytes()).hexdigest()!=digest]
    if changed:
        issues.append("Concurrent changes during check: "+", ".join(changed))
    combined=ROOT/"MPL_46_002-048_transcription.tex"
    combined_source=combined.read_bytes()
    expected=archive_tools.combined_bytes(ROOT,list(archive_tools.SCANS))
    identical=combined_source==expected
    combined_scan_order=[int(x) for x in re.findall(rb"\\scanpage\s*\{\s*(\d+)\s*\}",combined_source)]
    combined_order_ok=combined_scan_order==list(archive_tools.SCANS)
    if not combined_order_ok:
        issues.append("Combined fragment scan order differs from the required 42 scans.")
    if not identical:
        issues.append("Combined fragment is stale or uses a different concatenation rule; regenerate with archive_tools.py combine before freezing.")
    timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    report=[
        "# Technical compilation and final static check", "",
        "Final static-check time: "+timestamp, "",
        "## Concrete syntax findings", "",
        ("No concrete syntax error was detected." if not issues else
         "\n".join("- "+x for x in issues)), "",
        "## Scope and checks", "",
        f"All 42 page files were inspected solely as TeX source. The check covered balanced unescaped braces; nested begin/end environments; matching explicit math delimiters; paired left/right delimiters; approved diplomatic macro arguments; recognized control sequences; and balanced optional arguments and double-quoted labels for {arrow_count} TikZ-cd arrows.", "",
        "The checker recognizes LaTeX text wrappers when checking explicit math nesting. It also checks that aligned/gathered/split environments occur within explicit math or a TikZ-cd cell. This is a static syntax check, not a proof that every TeX package will process or render the source successfully.", "",
        "Combined fragment scan order: "+("correct." if combined_order_ok else "requires correction."),
        "Combined fragment equals the documented ordered page concatenation: "+("yes." if identical else "no."),
        "Concurrent page changes detected during check: "+("none." if not changed else ", ".join(changed)), "",
        "Combined SHA-256 at this check: "+hashlib.sha256(combined_source).hexdigest()+".", "",
        "## Compiler availability", "",
        "The earlier compiler attempt remains valid as an environment finding: XeLaTeX, LuaLaTeX and pdfLaTeX binaries are present, but no LaTeX format, core source, document class, or required package files were discoverable. XeLaTeX stopped before manuscript input with 'I can't find the format file xelatex.fmt!'. The exact attempt is preserved in compiler_attempt.txt. Compilation was not repeated, and no TeX installation was attempted.", "",
        "## Harness and limitations", "",
        "compile_harness.tex defines the approved diplomatic macros and preserves their ambient math/text mode. It retokenizes diagram bodies for TikZ-cd ampersands inside macro arguments. The harness is disposable technical support; it does not alter the transcription.", "",
        "No manuscript image or context archive was opened. No page, combined transcription, inventory, doubts file, core archive script, or progress log was modified. Visual accuracy, interpretation, completeness, and final rendered appearance are outside this technical check.", "",
        "An earlier apparent \\X command was a regex false positive: the source has valid row separators followed by X. No change was required.", ""
    ]
    (ROOT/"records/technical/technical_report.md").write_text("\n".join(report),encoding="utf-8")
    print("\n".join(issues) if issues else "No concrete syntax concern detected.")
    print(f"Checked 42 page files and {arrow_count} TikZ-cd arrows; combined current: {identical}; scan order correct: {combined_order_ok}.")
    print("Report: records/technical/technical_report.md")

if __name__=="__main__":
    main()

