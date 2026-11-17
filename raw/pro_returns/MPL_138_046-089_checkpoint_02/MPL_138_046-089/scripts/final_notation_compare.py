"""One-time pre-freeze changes made after direct cross-page visual comparison."""
from pathlib import Path
from datetime import datetime, timezone
import csv, re

ROOT=Path(__file__).resolve().parents[1]
def change(scan, pairs):
    p=ROOT/'pages'/f'MPL_138_046-089_138_scan{scan:03}.tex'
    s=p.read_text()
    for old,new in pairs:
        if old not in s: raise ValueError((scan,old))
        s=s.replace(old,new)
    p.write_text(s)

change(47,[(r'D_\infty=(Z_{/2})',r'\mathbb D_\infty=(\mathbb Z_{/2})'),
           ('\\[\n\\begin{array}{ll}', '\\diagram{\\[\n\\begin{array}{ll}'),
           ('\\end{array}\n\\]', '\\end{array}\n\\]}')])
change(62,[('\\[\n\\begin{array}{ll}', '\\diagram{\\[\n\\begin{array}{ll}'),
           ('\\end{array}\n\\]', '\\end{array}\n\\]}')])
change(66,[('\\[\n\\left\\{\\begin{array}{lll}', '\\diagram{\\[\n\\left\\{\\begin{array}{lll}'),
           ('\\end{array}\\right.\n\\]', '\\end{array}\\right.\n\\]}')])
change(68,[('Z',r'\mathbb Z')])
change(76,[(r'\unsure{prolibres|problèmes}',r'\unsure{prolibres}')])

# Upright Gamma in 081/083/089 and a genuinely different, cursive form in
# 084--087 were compared as enlarged crops before any contextual source opened.
# Preserve the visibly T-like form first, with Gamma as an explicit alternative.
for scan in [84,85,86,87]:
    p=ROOT/'pages'/f'MPL_138_046-089_138_scan{scan:03}.tex'
    s=p.read_text()
    s=re.sub(r'\\widetilde\\Gamma(_(?:\\nu|2))',lambda m:r'\widetilde{\unsure{\mathcal T|\Gamma}}'+m[1],s)
    s=re.sub(r'\\Gamma(_(?:\\nu|2))',lambda m:r'\unsure{\mathcal T|\Gamma}'+m[1],s)
    p.write_text(s)

change(89,[(r'''\text{l'hom de}\\
\inserted{\widehat L_\nu}\deleted{\unsure{\widehat F([0,\nu])}}\longrightarrow\pi\\
\lambda_i\longmapsto h_i
\end{gathered}
\]''',r'''\text{l'hom de}
\end{gathered}
\]
\diagram{\begin{tikzcd}
\inserted{\widehat L_\nu}\deleted{\unsure{\widehat F([0,\nu])}}\arrow[r]&\pi\\
\lambda_i\arrow[r,mapsto]&h_i
\end{tikzcd}}''')])

inv=ROOT/'MPL_138_046-089_inventory.csv'
with inv.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
newrows=[]
for r in rows:
    s,e=int(r['scan']),int(r['element'])
    if (s,e) in [(47,11),(62,12),(66,28)]: r['kind']='diagram'
    if s==82 and e==8:
        d=r.copy();d.update(kind='deletion',position='beside cancelled Changeons',first_words_or_objects='On');newrows.append(d)
        r['first_words_or_objects']='prendre x il suffit de prendre un xi'
    newrows.append(r)
    if s==54 and e in [2,3]:
        d=r.copy();d.update(kind='drawing',position='inverted letterhead separator '+('upper' if e==2 else 'lower'),first_words_or_objects='short printed horizontal rule');newrows.append(d)
counts={}
for r in newrows:
    counts[r['scan']]=counts.get(r['scan'],0)+1;r['element']=str(counts[r['scan']])
with inv.open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(newrows)

stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:f.write('final cross-page notation comparison completed '+stamp+'\n')
with (ROOT/'audit_notes.md').open('a') as f:f.write('''## Final cross-page notation comparison

Compared the enlarged doubled D and Z on 047, the Z forms on 068 and 071/075/080–089, and restored the doubled alphabet where the ink supports it. Compared the distinct hat-bearing scheme words on 047 and 051; their different uncertain readings remain, rather than making them agree from mathematical expectation. Compared the cover word on 076 with the explicit title on 089: retained prolibres with a single doubt, dropping the visually weaker problèmes alternative.

Directly compared enlarged upright Gamma forms on 081, 083 and 089 with the cursive forms on 084–087. The latter have a central slanting stem, a looped head and a curved foot: they are now marked calligraphic T first, Gamma as alternative. This is an alphabet doubt, not a mathematical identification; the upright Galois Gamma remains unchanged. All raised exclamation marks remain !, distinct from prime strokes and raised zero.

Put the three genuine tabular arrays on 047, 062 and 066 inside diagram macros, and the two-line mapping in the hypothesis on 089 into tikz-cd. These are encoding changes only. Reconciled the inventory with the two printed separator drawings on 054 and the separately cancelled On on 082. No context source had been opened.
\n''')
print(stamp, 'notation comparison recorded;',len(newrows),'inventory rows')
