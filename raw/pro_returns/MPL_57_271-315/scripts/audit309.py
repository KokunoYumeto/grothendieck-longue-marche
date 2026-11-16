from pathlib import Path
import json,subprocess
from datetime import datetime,timezone
p=Path('MPL_57_271-315/records/scan309.json'); d=json.loads(p.read_text());t=d['tex']
t=t.replace(r"il suffit en \unsure{fait} \unsure{que l'on} \unsure{ait} un Pic. \unsure{connexe} \unsure{de type} \unsure{fini sur un} \unsure{complet}.",r"il suffit en \unsure{fait} \unsure{que} un Pic. \unsure{connexe} \unsure{des fibres en soit complet}.")
t=t.replace(r'\unsure{géom. normales|projnormales}',r'\unsure{primaires|prénormales}')
t=t.replace(r'\unsure{Dim.|Min.}',r'\unsure{Min.|Dim.}')
t=t.replace(r'\unsure{géom. connexes}',r'\unsure{géom. intègres|géom. connexes}')
t=t.replace(r'\unsure{0|\tau}',r'\unsure{\tau|0}')
fig=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,5.8) .. controls (-.2,6.2) and (1.1,6.4) .. (1.4,6.05) .. controls (1.6,5.75) and (.3,5.55) .. (0,5.8);
\draw (.15,5.72) -- (.1,5.4);
\draw (2.9,4.25) .. controls (2.4,4.45) and (2.6,5.15) .. (3.15,5.12) .. controls (3.8,5.3) and (4.6,4.9) .. (4.85,4.86);
\draw (2.85,4.3) .. controls (3.4,4.05) and (4.3,3.95) .. (4.9,4.05);
\draw (2.82,4.7) .. controls (2.3,4.35) and (2.2,4.1) .. (2.05,3.8);
\draw (0,2.65) .. controls (-.3,3.05) and (1.9,3.1) .. (2.1,2.8) .. controls (2.2,2.45) and (.15,2.4) .. (0,2.65);
\draw (.15,2.5) -- (0,2.28);
\draw (2.75,.1) -- (3.65,2.15);
\draw (3.15,0) -- (4.05,2.05);
\draw (3.7,0) -- (4.5,1.95);
\draw (4.25,.08) -- (4.85,1.6);
\end{tikzpicture}}'''
t=t.replace('\\mspage{308}',fig+'\n\\mspage{308}')
d['tex']=t
d['inventory'].append({'element':'audit-44','kind':'drawing','position':'upper insertion, right c, d insertion, lower-right g','first_words_or_objects':'two insertion enclosures; right callout and leader; four oblique cancellation strokes'})
d['doubts'].extend([{'line':'slanting left marginal note, final two lines','reading':'un Pic. connexe des fibres en soit complet','alternatives':'very uncertain connected strokes; replaces initial speculative reading involving type fini','confidence':'low'},{'line':'right d, last parenthesis','reading':'primaires','alternatives':'prénormales; initial reading géom. normales rejected after enlargement','confidence':'low'},{'line':'b prime and last h display','reading':'Min.; Pic tau','alternatives':'Dim.; Pic 0','confidence':'low'}])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');subprocess.run(['python3','MPL_57_271-315/scripts/manage.py','save','--input',str(p)],check=True)
with Path('MPL_57_271-315/progress.log').open('a') as f:f.write('scan 309 audited '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
