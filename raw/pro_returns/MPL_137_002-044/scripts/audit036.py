from audit_support import revise
revise(36,replacements=[
(r'\unsure{\mathbf Z|k}',r'\unsure{k|\mathbf Z}'),
('$S$',r'$\unsure{\mathcal{S}|S}$'),
(r'S_{ab}',r'\unsure{\mathcal{S}|S}_{ab}'),
(r'\alpha:S^\circ',r'\alpha:\unsure{\mathcal{S}|S}^\circ'),
(r'\operatorname{Ob}S$',r'\operatorname{Ob}\unsure{\mathcal{S}|S}$'),
(r'\operatorname{Hom}_S',r'\operatorname{Hom}_{\unsure{\mathcal{S}|S}}'),
('\n---\n','\n----\n')],
doubts=[('category letter throughout','script S','S','medium')],
notation=[('ornate two-loop category S',r'\unsure{\mathcal{S}|S}','Looped outline in both its initial occurrence and evaluation formula; preserve alphabet uncertainty rather than silently selecting ordinary roman S.')],
note='Second audit of whole scan, comparing the ornate S in the definition and all formulas. The top vertical inclusion here has a visible hooked shaft and downward arrowhead, unlike the cap sign on 035. Rechecked alpha, opposite-circle placement, cancellations and insertions.')
