import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,164,r'''\scanpage{164}
\begin{flushright}
Compléments\\
dualité
\end{flushright}
\figure{\begin{tikzpicture}\draw (0,0) .. controls (.2,.15) and (.55,.20) .. (.8,.40);\end{tikzpicture}}
\margin{163}
''',[('text','upper right','Compléments dualité'),('drawing','upper left','isolated oblique stroke'),('margin note','bottom left','163')],sheet_kind='cover',remarks='Whole and both halves read. Cover/title only: Compléments dualité, no page count. Isolated ink stroke reproduced; stains and binding damage are not text.')
