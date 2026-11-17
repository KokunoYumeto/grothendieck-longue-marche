from audit_support import revise
revise(44,replacements=[
(r'=\operatorname{Hom}^\bullet_k(\alpha^\bullet(x),C^\bullet_F),',r'\operatorname{Hom}^\bullet_k(\overset{\text{\'\'}}{\alpha^\bullet(x)},C^\bullet_F),'),
(r'\prod_i\operatorname{Hom}_k(K^i,C^i)\xrightarrow{\delta}',r'\prod_i\operatorname{Hom}_k(K^i,C^i)\mathrel{\substack{\xrightarrow{\delta}\\[-.4ex]\deleted{\unsure{\longleftarrow|\longrightarrow}}}}'),
(r'$K^\bullet$ \deleted{\unsure{est}} $\in\operatorname{Ob}',r'$K^\bullet$ \deleted{\unsure{est}} \deleted{\unsure{plein}} $\unsure{=|\subset}\in\operatorname{Ob}')],
doubts=[('repeated Hom formula','two vertical ditto strokes above alpha(x)','no equality sign is visible at left','high'),('lower arrow beneath delta','cancelled leftward arrow','overwritten rightward arrow','low'),('line before Mais de façon générale','cancelled plein and equality-like sign','short word and sign obscured by cancellation','low')],
elements=[('deletion','beneath delta arrow','overwritten lower arrow'),('deletion','beneath est before membership','plein (uncertain)')],
notation=[('ditto strokes over repeated expression',r"\overset{\text{''}}{\alpha^\bullet(x)}",'The scan has two short vertical strokes above the repeated expression; an unwritten equals sign has not been supplied.')],
note='Second visual audit of whole scan and all text bands, with original-color enlargements of the ditto mark and overwritten lower arrow. Removed an unwritten equals sign before the repeated Hom expression and reproduced the visible ditto strokes. Added the lower arrow and obscured cancellation/sign near membership with explicit doubts. Confirmed the margin instruction, abélienne deletion/stable par Ker insertion, and the unfinished final words et les deux.')
