from audit_support import revise
revise(41,replacements=[
(r'''\underline{\operatorname{Hom}}_{k\text{-}lin}(A,B)\arrow[d,"\simeq"']''',r'''\underline{\operatorname{Hom}}_{k\text{-}lin}(A,B)\arrow[d,"{F\longmapsto F(C^\bullet_*)}","\simeq"']'''),
('\\[\nF\\longmapsto F(C^\\bullet_*)\n\\]\n','')],
notation=[('complex degree mark on 041',r'C^\bullet_*\quad B^\bullet_k','The upper mark is a filled dot; lower star on C denotes its simplicial grading, visibly distinct in the same expression.')],
note='Second audit of whole scan and enlarged text regions. Confirmed the large cancelled draft boundary, all internal cancellations and insertions, the Λ^(i+1) exponent and T-star wedge differential. Placed F maps to F(C-dot-star) beside its vertical diagram arrow, where written, instead of as a detached display; no content removed.')
