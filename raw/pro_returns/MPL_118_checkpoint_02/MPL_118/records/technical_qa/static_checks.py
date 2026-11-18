#!/usr/bin/env python3
"""Technical-only LaTeX checks; reads page fragments, never scans or context."""
import argparse, collections, hashlib, json, re, subprocess
from datetime import datetime, timezone
from pathlib import Path

ALLOWED_CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
STANDARD = set("""Delta Leftarrow Longleftarrow Longleftrightarrow Longrightarrow Phi Pi Rightarrow Sigma Theta Updownarrow Vert alpha amalg arrow backslash bar begin beta big bigcap bigcup boxed bullet cap cdots check circ cline coprod cup delta displaystyle downarrow draw end equiv eta exists flat forall gamma geq hfill hline hookrightarrow hrulefill hspace in infty int joinrel lambda ldots left leftarrow leq lhook longleftrightarrow longmapsto longrightarrow mathbb mathbin mathcal mathrm mid multicolumn ne neq node not notin operatorname overline overrightarrow overset phantom pi prime prod psi qquad quad rho right sharp sigma sim simeq subset substack supset text textcircled times to underbrace underline underset varepsilon varinjlim varnothing varphi vphantom widehat wr xi xleftarrow xrightarrow""".split())

def control(s, i):
    assert s[i] == "\\"
    j = i + 1
    if j == len(s):
        return "", j
    if s[j].isalpha() or s[j] == "@":
        k = j + 1
        while k < len(s) and (s[k].isalpha() or s[k] == "@"):
            k += 1
        return s[j:k], k
    return s[j], j + 1

def uncomment(s):
    out = list(s)
    i = 0
    while i < len(s):
        if s[i] == "\\":
            _, i = control(s, i)
        elif s[i] == "%":
            j = s.find("\n", i)
            if j < 0:
                j = len(s)
            out[i:j] = " " * (j-i)
            i = j
        else:
            i += 1
    return "".join(out)

def line(s, pos):
    return s.count("\n", 0, pos) + 1

def group(s, i, opening="{", closing="}"):
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s) or s[i] != opening:
        return None, i
    start = i
    depth = 1
    brace = 0
    quote = False
    i += 1
    while i < len(s):
        if s[i] == "\\":
            _, i = control(s, i)
            continue
        c = s[i]
        if opening == "[":
            if c == "{":
                brace += 1
            elif c == "}":
                brace -= 1
            elif brace == 0 and c == '"':
                quote = not quote
            if brace or quote:
                i += 1
                continue
        if c == opening:
            depth += 1
        elif c == closing:
            depth -= 1
            if depth == 0:
                return s[start+1:i], i+1
        i += 1
    return None, len(s)

def environment_ranges(s):
    stack = []
    pairs = []
    issues = []
    i = 0
    while i < len(s):
        if s[i] != "\\":
            i += 1
            continue
        name, end = control(s, i)
        if name in ("begin", "end"):
            env, end = group(s, end)
            if env is not None:
                if name == "begin":
                    stack.append((env, i, end))
                elif not stack or stack[-1][0] != env:
                    issues.append({"kind":"environment_mismatch","line":line(s,i),"environment":env})
                else:
                    opened, pos, body_start = stack.pop()
                    pairs.append((opened, pos, body_start, i, end))
        i = end
    for env, pos, _ in stack:
        issues.append({"kind":"unclosed_environment","line":line(s,pos),"environment":env})
    return sorted(pairs, key=lambda x:x[1]), issues

def arrow_grid(s, env):
    _, start, body_start, body_end, _ = env
    opts, nextpos = group(s, body_start, "[", "]")
    if opts is not None:
        body_start = nextpos
    replacement = bool(opts and re.search(r"ampersand\s+replacement\s*=\s*\\&", opts))
    rows = [[[]]]
    arrows = []
    row, col, brace, nested = 1, 1, 0, 0
    i = body_start
    while i < body_end:
        c = s[i]
        if c == "\\":
            cmd, end = control(s, i)
            if cmd in ("begin", "end"):
                name, j = group(s,end)
                if name is not None:
                    nested += 1 if cmd == "begin" else -1
                    rows[row-1][col-1].append(s[i:j])
                    i = j
                    continue
            if nested == 0 and cmd == "arrow":
                options, j = group(s,end,"[","]")
                if options is not None:
                    arrows.append({"source":[row,col],"options":options,"line":line(s,i)})
                    i = j
                    continue
            if nested == 0 and brace == 0 and cmd == "\\":
                row += 1
                col = 1
                rows.append([[]])
                i = end
                # Optional spacing after row ending is not a matrix cell.
                spacing, j = group(s,i,"[","]")
                if spacing is not None:
                    i = j
                continue
            if nested == 0 and brace == 0 and cmd == "&" and replacement:
                col += 1
                rows[-1].append([])
                i = end
                continue
            rows[row-1][col-1].append(s[i:end])
            i = end
            continue
        if nested == 0:
            if c == "{": brace += 1
            elif c == "}": brace -= 1
            elif c == "&" and brace == 0 and not replacement:
                col += 1
                rows[-1].append([])
                i += 1
                continue
        rows[row-1][col-1].append(c)
        i += 1
    # Ignore an entirely empty last row due to a final \\.
    if len(rows)>1 and len(rows[-1]) == 1 and not "".join(rows[-1][0]).strip():
        rows.pop()
    nrows = len(rows)
    ncols = max(map(len, rows), default=0)
    issues = []
    for a in arrows:
        source = a["source"]
        explicit_from = re.search(r"(?:^|,)\s*from\s*=\s*(\d+)-(\d+)", a["options"])
        explicit_to = re.search(r"(?:^|,)\s*to\s*=\s*(\d+)-(\d+)", a["options"])
        if explicit_from:
            source = list(map(int,explicit_from.groups()))
        if explicit_to:
            target = list(map(int,explicit_to.groups()))
        else:
            direction = re.match(r"\s*([udlr]+)\s*(?:,|$)", a["options"])
            if not direction:
                issues.append({"kind":"unresolved_arrow_target","line":a["line"],"source":source,"options":a["options"]})
                continue
            d = direction.group(1)
            target = [source[0]+d.count("d")-d.count("u"),source[1]+d.count("r")-d.count("l")]
        a["resolved_source"] = source
        a["target"] = target
        for role, point in (("source",source),("target",target)):
            if not (1<=point[0]<=nrows and 1<=point[1]<=ncols):
                issues.append({"kind":"off_grid_arrow_"+role,"line":a["line"],"source":source,"target":target,"grid":[nrows,ncols],"options":a["options"]})
    return {"start_line":line(s,start),"rows":nrows,"max_columns":ncols,"row_columns":list(map(len,rows)),"arrow_count":len(arrows),"arrows":arrows}, issues

def check_page(path):
    raw = path.read_text()
    s = uncomment(raw)
    issues = []
    commands = collections.Counter()
    depth = 0
    dollars = []
    leftright = []
    math_delimiters = []
    i = 0
    while i < len(s):
        if s[i] == "\\":
            cmd, end = control(s,i)
            if cmd.isalpha():
                commands[cmd] += 1
            if cmd == "left":
                leftright.append((depth,line(s,i)))
            elif cmd == "right":
                if not leftright:
                    issues.append({"kind":"right_without_left","line":line(s,i)})
                else:
                    left_depth,left_line = leftright.pop()
                    if left_depth != depth:
                        issues.append({"kind":"left_right_group_mismatch","line":line(s,i),"left_line":left_line})
            elif cmd in ("[", "("):
                math_delimiters.append((cmd,line(s,i)))
            elif cmd in ("]", ")"):
                wanted = "[" if cmd == "]" else "("
                if not math_delimiters or math_delimiters[-1][0] != wanted:
                    issues.append({"kind":"unmatched_math_delimiter","line":line(s,i),"delimiter":cmd})
                else:
                    math_delimiters.pop()
            i = end
            continue
        if s[i] == "{": depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth < 0:
                issues.append({"kind":"extra_close_brace","line":line(s,i)})
        elif s[i] == "$":
            dollars.append(line(s,i))
        i += 1
    if depth:
        issues.append({"kind":"brace_imbalance","net_open":depth})
    if len(dollars)%2:
        issues.append({"kind":"odd_unescaped_dollar_count","count":len(dollars),"lines":dollars})
    for _,left_line in leftright:
        issues.append({"kind":"left_without_right","line":left_line})
    for delimiter,at_line in math_delimiters:
        issues.append({"kind":"unclosed_math_delimiter","line":at_line,"delimiter":delimiter})
    unknown = sorted(set(commands)-STANDARD-ALLOWED_CUSTOM)
    for name in unknown:
        issues.append({"kind":"unknown_command_candidate","command":name})
    envs, env_issues = environment_ranges(s)
    issues.extend(env_issues)
    grids = []
    for env in envs:
        if env[0] == "tikzcd":
            grid, grid_issues = arrow_grid(s,env)
            grids.append(grid)
            issues.extend(grid_issues)
    return {"path":str(path),"sha256":hashlib.sha256(raw.encode()).hexdigest(),"lines":raw.count("\n"),"commands":dict(sorted(commands.items())),"diagrams":grids,"issues":issues}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--pages",type=Path,default=Path(__file__).resolve().parents[2]/"pages")
    parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parent/"static_report.json")
    args=parser.parse_args()
    pages=[check_page(p) for p in sorted(args.pages.glob("*.tex"))]
    report={"created_utc":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
      "scope":"Technical syntax only; no scans or contextual sources opened; page fragments not modified.",
      "limitations":"Static parsing does not prove renderability or faithfulness. Arrow positions are checked only for matrix bounds, not against ink. Macro definitions and TeX packages need a full compile.",
      "pages":pages}
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"pages":len(pages),"diagrams":sum(len(p["diagrams"]) for p in pages),"arrows":sum(d["arrow_count"] for p in pages for d in p["diagrams"]),"issues":[{"file":Path(p["path"]).name,**e} for p in pages for e in p["issues"]]},indent=2,ensure_ascii=False))

if __name__ == "__main__":
    main()

