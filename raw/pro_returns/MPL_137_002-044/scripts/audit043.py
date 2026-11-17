from audit_support import revise
revise(43,replacements=[
(r'\cdots\deleted{\unsure{k}}\longrightarrow0',r'\cdots\underset{\unsure{\text{degr }0}}{\deleted{\unsure{k}}}\longrightarrow0'),
(r"\alpha'^{\vee}",r"(\alpha^{\unsure{\bullet|'}})^\vee"),
(r"(\alpha')^\circ",r"(\alpha^{\unsure{\bullet|'}})^\circ"),
(r'\alpha_k(M)_{\unsure{n|i}}',r'\alpha_{\unsure{k|*}}(M)_{\unsure{n|i}}'),
(r"\alpha'^{\unsure{n|i}}(M)",r'\alpha^{\unsure{n|i}}(M)'),
(r'\operatorname{Hom}(C^{\unsure{n|i}}_*,M)',r'\operatorname{Hom}(C^{\unsure{n|i}}_*,\unsure{M|k})')],
doubts=[('beta(C0) insertion','degr 0 below cancelled term','degree label also possibly cancelled','low'),('triangle and preceding cancelled formula','alpha with raised dot','alpha prime','low'),('Prop. 2 final pairing','alpha subscript k or star; Hom second argument M','star or k; k','low')],
notation=[('alpha degree mark in overwritten 043 text',r"\alpha^{\unsure{\bullet|'}}",'Compared with the unambiguous dot of 042; cancellation strokes prevent a certain decision here. The final indexed alpha has no separate prime.')],
note='Second audit of whole scan, enhanced bands and enlarged original-color formulas. Inspected the beta(C0) insertion and its two degree annotations, cancelled passages and diagonal strikes, both margin regions, duality triangle and faint final pairing. Added explicit uncertainty to the latter rather than supplying expected objects or indices; compared pen-exercise paths with the source drawing.')
