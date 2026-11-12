"""Mechanical LaTeX repairs of tikz-cd diagrams (content unchanged):
- a tikz-cd inside a macro argument needs "ampersand replacement=\\&" with \\& as column separator;
- an arrow label in quotes that contains a comma outside braces gets braces ("{...}"), or the comma splits the options;
- a gathered block that contains a tikz-cd becomes an array{c} (gathered reads its body as an argument, which breaks
  the tikz-cd matrix);
- a gathered block inside a tikz-cd cell gets braces (its \\\\ would end the row), unless an unmatched \\left before it
  in the cell pairs with a \\right after it.
usage: python -I fix_tikzcd_in_macros.py FILE.tex..."""
import re
import sys

B = "\\"
TIKZ = re.compile(re.escape(B + "begin{tikzcd}") + r"(\[[^\]]*\])?(.*?)" + re.escape(B + "end{tikzcd}"), re.S)
GATH = re.compile(re.escape(B + "begin{gathered}") + r"(.*?)" + re.escape(B + "end{gathered}"), re.S)


def brace_labels(body):
    """wrap "..." arrow labels containing a top-level comma in braces"""
    out, i = [], 0
    for m in re.finditer(r"\\arrow\[", body):
        out.append(body[i:m.end()])
        j, depth, k = m.end(), 1, m.end()
        # find the end of the option list
        while k < len(body) and depth:
            depth += {"[": 1, "]": -1}.get(body[k], 0)
            k += 1
        opts = body[j:k - 1]

        def fix(mm):
            lab = mm.group(1)
            d, top_comma = 0, False
            for ch in lab:
                d += {"{": 1, "}": -1}.get(ch, 0)
                if ch == "," and d == 0:
                    top_comma = True
            return '"{' + lab + '}"' if top_comma and not (lab.startswith("{") and lab.endswith("}")) else mm.group(0)
        out.append(re.sub(r'"([^"]*)"', fix, opts) + "]")
        i = k
    out.append(body[i:])
    return "".join(out)


def env_pairs(s, name):
    """(start, end) of each outermost \\begin{name}...\\end{name}, nesting respected"""
    tok = re.compile(re.escape(B + "begin{" + name + "}") + "|" + re.escape(B + "end{" + name + "}"))
    pairs, depth, start = [], 0, None
    for m in tok.finditer(s):
        if m.group(0).startswith(B + "begin"):
            if depth == 0:
                start = m.start()
            depth += 1
        elif depth:
            depth -= 1
            if depth == 0:
                pairs.append((start, m.end()))
    return pairs


def brace_gathered_cells(body):
    out, i = [], 0
    for a, e in env_pairs(body, "gathered"):
        before = body[max(0, a - 300):a]
        cell_start = max(before.rfind(B + "&"), before.rfind(B + B))
        cell = before[cell_start + 1:] if cell_start != -1 else before
        unmatched_left = cell.count(B + "left") > cell.count(B + "right")
        already = body[max(0, a - 1):a] == "{"
        out.append(body[i:a])
        out.append(body[a:e] if (unmatched_left or already) else "{" + body[a:e] + "}")
        i = e
    out.append(body[i:])
    return "".join(out)


for path in sys.argv[1:]:
    t = open(path, encoding="utf-8").read()
    n_amp = n_lab = n_arr = 0
    # an outermost gathered containing a tikz-cd -> array{c}; inner gathered blocks stay as they are
    parts, i = [], 0
    for a, e in env_pairs(t, "gathered"):
        blk = t[a:e]
        if B + "begin{tikzcd}" in blk:
            inner = blk[len(B + "begin{gathered}"):-len(B + "end{gathered}")]
            blk = B + "begin{array}{c}" + inner + B + "end{array}"
            n_arr += 1
        parts.append(t[i:a] + blk)
        i = e
    parts.append(t[i:])
    t1 = "".join(parts)
    out, i = [], 0
    for m in TIKZ.finditer(t1):
        opts, body = m.group(1) or "", m.group(2)
        new_opts, new_body = opts, body
        if "ampersand replacement" not in opts:
            new_opts = "[ampersand replacement=" + B + "&" + ("," + opts[1:-1] if opts[1:-1].strip() else "") + "]"
            new_body = re.sub(r"(?<!\\)&", lambda _: B + "&", body)
            n_amp += 1
        nb = brace_labels(new_body)
        n_lab += nb != new_body
        new_body = brace_gathered_cells(nb)
        out.append(t1[i:m.start()] + B + "begin{tikzcd}" + new_opts + new_body + B + "end{tikzcd}")
        i = m.end()
    out.append(t1[i:])
    t2 = "".join(out)
    if t2 != t:
        open(path, "w", encoding="utf-8").write(t2)
    print(path.split("/")[-1].split("\\")[-1], "| ampersand:", n_amp, "| labels braced in", n_lab, "diagrams | gathered->array:",
          n_arr)
