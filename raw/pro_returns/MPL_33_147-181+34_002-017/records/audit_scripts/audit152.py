import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,152);t=p.read_text().replace(r'\underline{D}',r'\unsure{\underline{D}|D}').replace("s'en\\unsure{va}","s'en \\unsure{va}")
t=t.replace(r'\unsure{sinon} \unsure{les} \unsure{vibrations} \unsure{des cônes} \unsure{inquiétants}',r'\unsure{sinon} \unsure{la|les} \unsure{vérification|vibrations} \unsure{des signes|des cônes} \unsure{inquiétante|inquiétants}')
t=t.replace('ou si $X$ et $Y$',r'ou si $X$ \unsure{et|ou} $Y$').replace(r'j:V\longrightarrow\unsure{X|Y}',r'j:V\longrightarrow X')
p.write_text(t)
audit(33,152,'Re-read both halves and enlarged/rotated the tiny left note. The note remains exceptionally uncertain; plausible letter-based alternatives «vérification», «des signes», and «inquiétante» are now recorded without treating the apparent sentence as established. Retained the extra parenthesis in the first formula, restored separation in «s’en va», marked the D-baseline ambiguity, and resolved the cancelled j-target to the visibly written X.')
