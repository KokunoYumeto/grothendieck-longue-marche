import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,165);t=p.read_text().replace(r'\uline{Applications}\quad\uline{possibles}',r'\uline{Applications} --- \uline{possibles}')
t=t.replace(r'\unsure{Pourrais|Pouvoir}',r'\unsure{Pourrait|Pourrais}')
t=t.replace(r'\textcircled{2}',r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)..controls(-.1,-1.5) and (-.1,-3.5)..(.35,-5.0);
\end{tikzpicture}}
\textcircled{2}''')
p.write_text(t)
add_element(33,165,'drawing','left of item 2 and NB','long faint grouping stroke')
audit(33,165,'Both halves compared, including faint pencil bounds, printed letterhead, and the cancelled third item. Restored the short stroke between the heading words and the long grouping stroke alongside item 2/NB. The cancelled article proposal is tentatively Pourrait/Pourrais; the open bracket before loc. cts remains doubtful, not completed.')
