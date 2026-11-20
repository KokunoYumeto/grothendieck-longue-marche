from audit_amend import *
c,s='15','183'
t=(WORK/'pages/15_scan183.tex').read_text()
t=t.replace(r'\inserted{de type fini,}',r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.3) {de type fini,};\draw (-1,-.6) .. controls (-.85,-.05) and (-.3,-.05) .. (.35,-.05) .. controls (.8,-.05) and (1,.15) .. (.9,.35);\end{tikzpicture}}}')
t=t.replace(r'\inserted{fermés $s$}',r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.3) {fermés $s$};\draw (-.75,-.15)--(-.5,-.55)--(.65,.35);\end{tikzpicture}}}')
amend(c,s,t,[change('insertion leaders','inserted text without drawn leaders','inserted text without drawn leaders','curved leader for de type fini and check-shaped leader for fermés s','The first curve rises from the main line and runs under the top-right insertion; the later check descends then rises to the right of fermés s.','drawing or diagram',c=True)],[(2,inv('drawing','under de type fini','curved insertion leader')),(11,inv('drawing','under fermés s','check-shaped insertion leader'))])
rr=readrows('visual_audit.tsv');HEADERS['visual_audit.tsv']=['cote','scan','audited_UTC','reader','findings']
for r in rr:
    if r['cote']==c and r['scan']==s:r['findings']+=' Two insertion leaders observed during this reread were subsequently added in TikZ and logged.'
write_rows('visual_audit.tsv',rr)
c,s='15','185'
t=(WORK/'pages/15_scan185.tex').read_text().replace('magnifiées, la connaissance','magnifiées, La connaissance')
t=t.replace(r"\inserted{provenant d'un $s$}",r"\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {provenant d'un $s$};\draw (-1.4,-.45) .. controls (-1.5,-.05) and (-.4,-.03) .. (.7,-.03) .. controls (1.1,-.03) and (1.4,.1) .. (1.35,.3);\end{tikzpicture}}}")
t=t.replace(r'\inserted{de $G_{\mathbf R}^{\zeta(s\prime)}$}',r'\inserted{de $G_{\mathbf R}^{\zeta(s\prime)}$}') if False else t
old=r"\inserted{de $G_{\mathbf R}^{\zeta(s')}$}"
new=r"\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {de $G_{\mathbf R}^{\zeta(s')}$};\draw (-1.2,-.45) .. controls (-1.35,-.1) and (-.6,-.02) .. (.5,-.02) .. controls (.9,-.02) and (1.1,.05) .. (1,.3);\end{tikzpicture}}}"
assert old in t;t=t.replace(old,new)
amend(c,s,t,[change('last paragraph, capital','la connaissance','la connaissance','La connaissance','The initial has a tall upright, separate upper return and long horizontal foot, followed by the small a.','other',c=True,crop='(738,2001,828,2081)',confidence='high'),change('two insertion leaders','inserted text without drawn curves','no corresponding drawn leaders','curved leaders under provenant d’un s and de G_R^{ζ(s′)}','Both curves start below the baseline at left, run under the raised words and curl upward at right.','drawing or diagram',c=True)],[(5,inv('drawing','under provenant d’un s','curved insertion leader')),(9,inv('drawing','under de G_R^{ζ(s′)}','curved insertion leader'))])
