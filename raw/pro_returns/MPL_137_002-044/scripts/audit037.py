from audit_support import revise
revise(37,replacements=[
(r'\unsure{\mathbf Z|k}',r'\unsure{k|\mathbf Z}'),
(r'S^\circ',r'\unsure{\mathcal{S}|S}^\circ'),
(r'$S=\widehat\Delta=\mathrm{Ss}$',r'$\unsure{\mathcal{S}|S}=\widehat\Delta=\unsure{\mathrm{S}_s|\mathrm{Ss}}$'),
(r'\unsure{nous}',r'\unsure{donc|nous}'),
(r'\operatorname{Hom}_{\widehat\Delta}',r'\operatorname{Hom}_{\unsure{\widehat\Delta|\Delta}}')],
doubts=[('opening category notation','S subscript s','Ss','medium'),('opening conjunction','donc','nous','medium'),('two Hom subscripts','Delta with hat','Delta','medium')],
note='Second audit of whole scan and enlarged bands. Compared the ornate S with scan 036, retained uncertainty in the small s and hats, inspected both abelian/additive margin notes, torsion-free condition and all deleted qualifications. Star indices agree with the ink and the earlier audited pages.')
