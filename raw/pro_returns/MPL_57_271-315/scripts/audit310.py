from pathlib import Path
import json,subprocess
from datetime import datetime,timezone
p=Path('MPL_57_271-315/records/scan310.json');d=json.loads(p.read_text());t=d['tex']
t=t.replace(r'[Vrai \unsure{en les pts} \deleted{\unsure{dont}} \inserted{\unsure{de}} \unsure{\uline{$\tau$}} torsion',r'[Vrai, \unsure{en les pts} \deleted{\unsure{dont la}} \inserted{\unsure{de} $\unsure{\tau}$} torsion')
t=t.replace(r'\unsure{pas asymptotiquement liée|pas aussi évidente ici}',r'\unsure{pas aussi évidente ici|pas asymptotiquement liée}')
t=t.replace(r'\unsure{flèche}',r'\unsure{platitude|flèche}')
t=t.replace(r"irréductibles en dehors d'un ouvert \unsure{dense de $S'$ constructible}",r"irréductibles \unsure{au dessus|en dehors} d'un ouvert \unsure{non vide convenable|dense de $S'$ constructible}")
fig=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (1.8,8.1) ellipse (.26 and .22);
\draw (1.55,7.99) -- (1.3,7.8);
\draw (.9,6.9) ellipse (.72 and .13);
\draw (-.65,6.45) ellipse (.35 and .18);
\draw[->](-.4,6.7)--(-.7,6.25);
\draw (-1.1,5.3) .. controls (-1.35,5.5) and (-1.1,5.9) .. (-.8,5.95) .. controls (.1,6.2) and (.35,5.55) .. (-.2,5.25) .. controls (-.55,5.05) and (-.9,5.13) .. (-1.1,5.3);
\draw (-.95,4.5) ellipse (.35 and .22);
\draw (2.8,3.15) .. controls (3.7,3.22) and (4.4,3.2) .. (4.9,3.13) -- (5,1.4) .. controls (5.1,.75) and (4.7,.8) .. (4.35,.8) -- (2.65,.84) .. controls (2.25,.9) and (2.3,1.2) .. (2.4,1.6) -- (2.8,3.15);
\draw (4.55,.85) .. controls (4.7,.6) and (5.1,.55) .. (5.18,.82);
\draw (-1.25,.15) ellipse (.3 and .17);
\draw (-1.12,-.55) ellipse (.36 and .2);
\draw (-.85,7.65) .. controls (-.65,7.25) and (-.72,6.9) .. (-.8,6.6);
\draw (-.89,7.67) .. controls (-.7,7.25) and (-.77,6.9) .. (-.85,6.61);
\end{tikzpicture}}'''
t=t.replace('\\mspage{309}',fig+'\n\\mspage{309}')
d['tex']=t
d['inventory'].append({'element':'audit-49','kind':'drawing','position':'distributed upper and middle callouts and left answer marks','first_words_or_objects':'circled Non/Oui/oui/non; two callout ovals; right example enclosure; vertical hatching'})
d['doubts'].extend([{'line':'right 3, correction','reading':'dont la deleted; de tau inserted','alternatives':'letters in cancelled la overlap inserted tau','confidence':'low'},{'line':'right continuation of 6','reading':'au dessus; non vide convenable','alternatives':'en dehors; dense de S prime constructible','confidence':'low'},{'line':'lower right, first starred question','reading':'platitude','alternatives':'flèche; contracted ending uncertain','confidence':'low'}])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');subprocess.run(['python3','MPL_57_271-315/scripts/manage.py','save','--input',str(p)],check=True)
with Path('MPL_57_271-315/progress.log').open('a') as f:f.write('scan 310 audited '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
