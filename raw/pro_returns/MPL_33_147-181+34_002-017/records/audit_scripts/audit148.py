import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
revise(33,148,'et ses accouplements',r'et \unsure{ses|les} accouplements')
revise(33,148,r'\margin{\textcircled{c}}',r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)--(1.8,.03);\draw (.28,-.15)--(1.45,-.13);\draw (.58,-.3)--(1.28,-.29);
\end{tikzpicture}}
\margin{\textcircled{c}}''')
p=page(33,148);t=p.read_text();t=t.replace(r'\diagram{\begin{tikzcd}[column sep=small]',r'\diagram{\fbox{\begin{tikzcd}[column sep=small]')
t=t.replace(r'\times\mathrm{R}\mathcal{H}om(\operatorname{pr}_2',r'\times & \mathrm{R}\mathcal{H}om(\operatorname{pr}_2')
t=t.replace('K^\\bullet_{X\\times_S Y}',r'&K^\bullet_{X\times_S Y}').replace(r'\end{tikzcd}}',r'\end{tikzcd}}}')
p.write_text(t)
add_element(33,148,'drawing','between trace formula and c','three diminishing horizontal separator strokes')
audit(33,148,'Both halves re-read: checked the live M target of the composition despite its mathematical anomaly, signs in the trace formula, low complex dots, exceptional exclamation marks, and all cancellation and insertion blocks. Added the three separator strokes and the visible frame around the pairing; moved the lower object under the right factor to preserve the right-hand vertical arrow. Marked the opening determiner uncertain.')
