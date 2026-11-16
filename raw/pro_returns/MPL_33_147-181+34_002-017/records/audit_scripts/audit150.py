import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,150);t=p.read_text().replace(r'\underline{D}',r'\unsure{\underline{D}|D}')
t=t.replace(r'\unsure{d’après|d’abord}',r'\unsure{d’abord|d’après}').replace(r"\unsure{d'après|d'abord}",r"\unsure{d'abord|d'après}")
t=t.replace(r"\unsure{d'obtenir|d'arriver}",r'\unsure{à valeurs}')
t=t.replace('Pour ceci,',r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (1,0)..controls(.8,-.4) and (.3,-.4)..(0,.1);
\end{tikzpicture}}
Pour ceci,''')
p.write_text(t)
add_element(33,150,'drawing','below homomorphism before Pour ceci','curved arrow pointing back toward the left')
audit(33,150,'Both halves and the rotated margin checked again. The marginal closing words are now tentatively «à valeurs»; the repeated Hom sources are deliberately preserved. Added the curved reversal arrow. The long low stroke of D may be part of the letter rather than a separate underline, so every previously confident underlined D on this leaf is explicitly marked with plain D as an alternative; ! and * are read separately from this uncertainty.')
