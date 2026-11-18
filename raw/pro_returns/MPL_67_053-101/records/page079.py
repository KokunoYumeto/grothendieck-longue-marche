import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{79}
% archive foliation: 81
plongés dans $X''$ normalisé de $X'''$ \deleted{dont}\inserted{duquel} on
part, et \deleted{on} trouve des antiiso entre
leurs bords \deleted{de ces} de $D_i',D_i''$ ---
d'où possibilité de les recoller pour
trouver un $X$ surface holo (à bord,
si on a aussi enlevé des disques ouv.
$\mathring D_\alpha^{\unsure{*}}$ correspondant aux pts marqués $x_\alpha$,
sinon une surface à pts marqués),
découpée par les cercles $\Gamma_i$ qui ne
sont \deleted{pas}\inserted{peut-être pas} \unsure{néc.} géodésiques
($??$ \deleted{\unsure{on a}}\inserted{à}
examiner de plus près) mais définissant
des cercles géodésiques uniques,
par les principes de Thurston.

Il faudrait voir que le résultat
obtenu ne dépend pas du choix des
paires $(D_i',D_i'')$ mut.\textsuperscript{t} polaires, il y
a un argument heuristique pour
cela tout à fait vaseux, consistant
à dire qu'une petite variation de \unsure{celle|cette},
"""
save(79,tex,[('text','upper to middle','plongés dans X double-prime normalisé'),('deletion','top right','dont'),('insertion','top right above dont','duquel'),('deletion','line 2 after et','on'),('deletion','line 3 after bords','de ces'),('deletion','before géodésiques','pas'),('insertion','above pas','peut-être pas'),('deletion','parenthesis after ??','on a'),('insertion','above parenthesis','à'),('text','bottom','Il faudrait voir que le résultat')],doubts=[('open disc notation','mathring D_alpha with star','The extra superscript stroke is a star-like mark, possibly a correction.','low'),('before géodésiques','néc.','Likely abbreviation but tightly written.','low'),('parenthetical deletion','on a','Very heavy cancellation, perhaps more than two short words.','low'),('last word','celle','cette; continuation on next page.','low')],abbreviations=[('holo','holomorphe'),('ouv.','ouverts'),('néc.','nécessairement'),('mut. avec t en exposant','mutuellement')],leads=['Self-flagged geodesicity of surgically produced seam circles: peut-être pas, ?? à examiner de plus près; unique geodesic representatives attributed to Thurston.','Independence of polar disc choices explicitly remains to be checked, with argument called tout à fait vaseux.'])
