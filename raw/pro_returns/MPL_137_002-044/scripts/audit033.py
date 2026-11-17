from audit_support import revise
revise(33,replacements=[
(r"\unsure{\tau|\tau'}",r"\unsure{\mathcal{T}|\mathcal{T}'}"),
(r'\tau',r'\unsure{\mathcal{T}|\tau}'),
(r'\arrow[r,hook]',r'\arrow[r,phantom,"\subset"]')],
doubts=[('diagram and throughout','script T (prime in specified places)','tau; one direct-limit type may have a prime','medium')],
note='Second visual audit of whole scan and enhanced bands. All four drawn inclusions in the upper diagram have subset strokes rather than arrowheads, now represented by phantom arrows labelled subset. Compared every looped type sign with scan 032; retained the genuinely uncertain prime and C|D readings.')
