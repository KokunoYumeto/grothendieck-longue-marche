"""The link annotations of a PDF: page, rectangle (points, PDF coordinates: origin bottom left), target. Read-only,
13 Nov 2026. The PDF is decompressed with mutool clean -d into a temporary file and read as text.
usage: python -I -B list_links_20261113.py FILE.pdf [--count | FIRST LAST]"""
import os
import re
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")


def links(pdf):
    """list of (page, (x0, y0, x1, y1), uri), pages numbered from 1"""
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "d.pdf")
        subprocess.run(["mutool", "clean", "-d", pdf, out], capture_output=True)
        t = open(out, "rb").read().decode("latin-1")
    objs = {int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) 0 obj\r?\n(.*?)\r?\nendobj", t, re.S)}
    kids = []

    def walk(n):
        o = objs[n]
        if re.search(r"/Type\s*/Pages", o):
            for k in re.findall(r"(\d+) 0 R", re.search(r"/Kids\s*\[(.*?)\]", o, re.S).group(1)):
                walk(int(k))
        else:
            kids.append(n)

    root = int(re.search(r"/Root (\d+) 0 R", t).group(1))
    walk(int(re.search(r"/Pages (\d+) 0 R", objs[root]).group(1)))
    res = []
    for pno, n in enumerate(kids, 1):
        m = re.search(r"/Annots\s*(\[(.*?)\]|(\d+) 0 R)", objs[n], re.S)
        if not m:
            continue
        arr = m.group(2) if m.group(2) is not None else objs[int(m.group(3))]
        for a in re.findall(r"(\d+) 0 R", arr):
            o = objs[int(a)]
            u = re.search(r"/URI\s*\((.*?)\)", o, re.S)
            r = re.search(r"/Rect\s*\[\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)", o)
            if u and r:
                res.append((pno, tuple(float(x) for x in r.groups()), u.group(1)))
    return res


if __name__ == "__main__":
    L = links(sys.argv[1])
    if "--count" in sys.argv:
        scans = [x for x in L if "viewer.html" in x[2]]
        print("links:", len(L), "| to a scan in the archive's viewer:", len(scans), "| distinct scan pages:",
              len({x[2] for x in scans}), "| pages with such links:", len({x[0] for x in scans}))
    else:
        a, b = int(sys.argv[2]), int(sys.argv[3])
        for p, r, u in L:
            if a <= p <= b:
                print("%d\t%.1f %.1f %.1f %.1f\t%s" % (p, *r, u))
