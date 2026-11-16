"""Pre-freeze alphabet revisions, after personal visual comparison of every cited leaf."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
from audit_tools import page
from workflow import ROOT,utc

for n in [148,150,154,156,158,160,162,170,176,178,180]:
    p=page(33,n);t=p.read_text()
    t=t.replace(r'\mathrm{R}',r'\mathbb{R}')
    t=t.replace(r'\mathrm{L}',r'\mathbb{L}').replace(r'\mathrm L',r'\mathbb L')
    if n==150:
        start=t.index(r'\margin{\uline{Plus explicit}') if r'\margin{\uline{Plus explicit}' in t else t.index(r'\margin{Plus explicit') if r'\margin{Plus explicit' in t else t.rindex(r'\margin{',0,t.rindex(r'\margin{'))
        t=t[:start]+t[start:].replace(r'\mathbb{R}',r'\unsure{\mathbb{R}|\mathrm{R}}')
    if n==154:
        t=t.replace(r'\unsure{K|R}',r'\unsure{R|K}').replace(r'\mathbf{Z}',r'\mathbb{Z}')
    if n==180:
        t=t.replace(r'\mathbb{R}^i\Gamma_X',r'\unsure{\mathrm{R}|\mathbb{R}}^i\Gamma_X')
        t=t.replace(r'\mathbb{R}\mathcal{H}$}',r'\unsure{\mathrm{R}|\mathbb{R}}\mathcal{H}$}')
    p.write_text(t)
p=page(33,167);t=p.read_text().replace(r'\mathrm{R}^{!}',r'\mathbb{R}^{!}').replace(r'\mathrm{R}_{!}',r'\mathbb{R}_{!}')
t=t.replace(r'\mathrm{R}\mathcal{H}',r'\unsure{\mathrm{R}|\mathbb{R}}\mathcal{H}')
p.write_text(t)
p=page(33,165);p.write_text(p.read_text().replace(r'\mathbf{Z}',r'\mathbb{Z}'))
with (ROOT/'records/audit_observations.md').open('a') as f:
    f.write('''\n## Cross-page alphabet audit\n\nThe doubled stems of derived R and tensor-product L were compared directly on 33/148, 150, 154, 156, 158, 160, 162, 167, 170, 176, 178, and 180. They are encoded with mathbb where visible, correcting the preliminary roman convention. The small margin Rs of 150, the last Hom R of 167, the second top-row R of 180 and its unfinished right-margin RH have local alphabet doubts. Ordinary dualizing-complex R_X remains ordinary R, distinct from derived R. The rounded bowls of the three opening complex letters on 154 favour R, with K retained as the alternative; this is a palaeographic decision, not harmonization of the mathematics. Coefficient Z on 154 and 165 also has doubled diagonals.\n''')
with (ROOT/'progress.log').open('a') as f:f.write(f'cross-page notation and alphabet audit completed {utc()}\n')
