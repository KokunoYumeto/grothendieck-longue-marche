"""Reconcile the root's visually read transcription; no OCR and no context input."""
from pathlib import Path
import csv, re, hashlib, json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_15_034-086"
SCANS = [34,36,38,40,42,44,46,48,50,52,54,56,60,61,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,85,86]
REUSED = {67,69,71,73,75,77,79,85}

def escaped(s, i):
    k=i-1
    while k>=0 and s[k]=="\\": k-=1
    return (i-k-1)%2==1

def macros(s,name):
    for m in re.finditer(r"\\"+name+r"\{",s):
        start=m.end(); j=start; depth=1
        while j<len(s) and depth:
            if not escaped(s,j):
                if s[j]=="{":depth+=1
                elif s[j]=="}":depth-=1
            j+=1
        if depth:raise ValueError(f"Unclosed {name}")
        yield m.start(),j,s[start:j-1]

def clean(s):
    return re.sub(r"\s+"," ",s).strip()

def table(s):
    return clean(s).replace("|",r"\|")

def reconcile():
    rows=[]; doubts=[]; counts={}; validations=[]
    for scan in SCANS:
        p=ROOT/"pages"/f"{PREFIX}_15_scan{scan:03d}.tex"
        s=p.read_text()
        events=[]; structural=[]
        for name,kind in [("margin","margin note"),("diagram","diagram"),("figure","drawing"),("inserted","insertion"),("deleted","deletion")]:
            for a,b,body in macros(s,name):
                events.append((a,b,kind,body))
                if name in ("margin","diagram","figure"):structural.append((a,b))
        for m in re.finditer(r"\\\[(.*?)\\\]",s,re.S):
            # A display containing only a diagram/box is already inventoried as a diagram.
            if r"\diagram{" not in m[1]:
                events.append((m.start(),m.end(),"display",m[1]))
            structural.append((m.start(),m.end()))
        for m in re.finditer(r"\\begin\{center\}(.*?)\\end\{center\}",s,re.S):
            events.append((m.start(),m.end(),"text",m[1]))
            structural.append((m.start(),m.end()))
        masked=list(s)
        for a,b in structural:
            for i in range(a,b):
                if masked[i]!="\n":masked[i]=" "
        # Record all remaining prose runs, retaining inline formulae in their text block.
        ms="".join(masked)
        for m in re.finditer(r"(?:[^\n]|\n(?!\s*\n))+",ms):
            body=re.sub(r"(?m)^\s*%[^\n]*","",m[0])
            body=re.sub(r"\\(?:cotefile|scanpage|mspage)\{[^}]*\}","",body).strip()
            if body:
                events.append((m.start(),m.end(),"text",body))
        events.sort(key=lambda e:(e[0],-e[1],e[2]))
        counts[scan]={}
        for n,(a,b,kind,body) in enumerate(events,1):
            line=s.count("\n",0,a)+1
            counts[scan][kind]=counts[scan].get(kind,0)+1
            rows.append([15,scan,"reused_typed" if scan in REUSED else "text",n,kind,
                         f"reading order {n}; fragment line {line}",clean(body)[:220],"yes"])
        page_doubts=[]
        for macro in ["unsure","illegible"]:
            for a,b,body in macros(s,macro):
                line=s.count("\n",0,a)+1
                pos=f"fragment line {line}"
                if macro=="unsure":
                    parts=body.split("|",1); reading=parts[0]
                    alt=parts[1] if len(parts)>1 else "Incomplete or ambiguous strokes; no second reading asserted"
                    confidence="low" if scan in {34,44,52,60,72,74,76,84,86} or len(reading)>65 else "medium"
                    if "|" in body and scan not in {77,79,85}:confidence="low"
                else:
                    reading=r"\illegible{"+body+"}"; alt="Overwritten words not recoverable on enlargement"; confidence="low"
                row=f"| 15 | {scan} | {pos} | {table(reading)} | {table(alt)} | {confidence} |"
                page_doubts.append((a,row))
        page_doubts.sort()
        (ROOT/"records"/f"doubts_scan{scan:03d}.md").write_text("\n".join(r for _,r in page_doubts)+"\n")
        doubts.extend(r for _,r in page_doubts)
        # Check actual TeX delimiter escaping (an even run of backslashes is not an escape).
        t=re.sub(r"(?m)^[ \t]*%[^\n]*","",s)
        stack=[]
        for i,c in enumerate(t):
            if c in "{}" and not escaped(t,i):
                if c=="{":stack.append(i)
                elif not stack:raise ValueError(f"{scan}: excess close brace")
                else:stack.pop()
        if stack:raise ValueError(f"{scan}: open braces")
        dollars=sum(c=="$" and not escaped(t,i) for i,c in enumerate(t))
        if dollars%2:raise ValueError(f"{scan}: odd dollar count {dollars}")
        env=[]
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",t):
            if m[1]=="begin":env.append(m[2])
            elif not env or env.pop()!=m[2]:raise ValueError(f"{scan}: mismatched environment")
        if env:raise ValueError(f"{scan}: unclosed environment")
        if r"\documentclass" in t or r"\includegraphics" in t:raise ValueError("Forbidden preamble/image")
        validations.append(f"{scan:03d}: braces, dollar parity, environment nesting checked; {len(events)} inventory rows; {len(page_doubts)} doubt occurrences.")
    with (ROOT/f"{PREFIX}_inventory.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["cote","scan","sheet_kind","element","kind","position","first_words_or_objects","transcribed"])
        w.writerows(rows)
    (ROOT/"records/inventory_counts.json").write_text(json.dumps(counts,indent=2)+"\n")
    intro=(ROOT/"records/doubts_frontmatter.md").read_text()
    end=(ROOT/"records/doubts_endmatter.md").read_text()
    (ROOT/f"{PREFIX}_doubts.md").write_text(intro+"\n"+"\n".join(doubts)+"\n"+end)
    pages=[ROOT/"pages"/f"{PREFIX}_15_scan{n:03d}.tex" for n in SCANS]
    combined=ROOT/f"{PREFIX}_transcription.tex"
    combined.write_text("\n\n".join(p.read_text().rstrip() for p in pages)+"\n")
    log=(ROOT/"progress.log").read_text()
    for n in SCANS:
        assert re.search(fr"^scan {n:03d} audited ",log,re.M),f"Missing audit {n}"
    assert combined.read_text().startswith("\\cotefile{15}\n\\scanpage{34}")
    validations += [
      f"TOTAL: {len(pages)} page fragments; {len(rows)} inventory rows, all yes; {len(doubts)} local doubt occurrences.",
      "23 handwritten subject sheets and 8 reused typescript/printed sheets.",
      "Inventory rows follow the diplomatic reading order. Nested insertions/deletions have separate rows; their text also remains in the containing block.",
      "Fragment line numbers are exact locators in the supplied page files, not invented manuscript line numbers. The scans have no ruled or author-numbered lines.",
      "A full TeX compilation was attempted but the installed pdfTeX engine has no pdflatex format or LaTeX package tree (latex.ltx, amsmath.sty, tikz-cd.sty were not found). No compiled-layout validation is claimed.",
      "The QA wrapper displays editorial wrappers transparently; it is a validation aid, not a publisher's rendering specification.",
      "All image reading and both visual passes were performed by the root reader; no OCR and no transcription delegation.",
    ]
    (ROOT/"records/validation_before_context.txt").write_text("\n".join(validations)+"\n")
    print(validations[-7])
    print(f"Reconciled {len(rows)} inventory rows and {len(doubts)} doubts.")
    return pages+[combined]

def freeze(files):
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/"records/frozen_sha256.json").write_text(json.dumps(hashes,indent=2)+"\n")
    with (ROOT/"progress.log").open("a") as f:
        for name,digest in hashes.items():f.write(f"SHA-256 {digest}  {name}\n")
        f.write(f"transcription frozen {now}\n")
    print("transcription frozen",now)

if __name__=="__main__":
    import sys
    files=reconcile()
    if "--freeze" in sys.argv:freeze(files)
