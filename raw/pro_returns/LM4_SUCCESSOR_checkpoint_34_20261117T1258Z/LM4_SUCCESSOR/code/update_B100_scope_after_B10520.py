"""Replace a now-stale forward scope by the completed B102/B105 comparison."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'sections/b_symmetric_nonasphericity.tex';s=p.read_text()
start=s.index('The new sphere uses an actual old-$0$ relation among nodal')
end=s.index('\n\\begingroup\\raggedright',start)
old=s[start:end]
new='''The sphere uses an actual old-$0$ relation among nodal relations.
B.95's overlap calculation places the corresponding column slots in
paired involution summands with vanishing second involution cohomology.
The required geometric-to-presentation comparison is supplied in B.102.
B.105 then chooses explicit node and cylinder disks, proves that their
sphere survives in the actual $Z_2$, and identifies its free rank-two
induced involution block. Its existence alone still gives no nonzero
class in the domain or image of $\\kappa$. The full equivariant relation
kernel, its Smith edge, and the nonlinear and compact fixed-lifting
steps remain to be determined.
'''
(root/'records/B100_scope_before_B105_update20.tex').write_text(old+'\n')
p.write_text(s[:start]+new+s[end:])
(root/'records/B100_scope_update20.md').write_text('The earlier B100 scope paragraph said its geometric-to-presentation comparison had not yet been supplied. We replaced that stale forward scope with explicit cross-references to the now proved B102 and B105 results, retaining the unresolved full Smith/nonlinear/compact scope. No B100 mathematical claim or proof changes. The original paragraph is retained verbatim in the adjacent .tex record. An initial exact-text replacement failed at its assertion because the expected source spacing differed; no source was changed by that failed attempt, and the build5 then repeated the unchanged repaired bibliography build. The robust bounded-paragraph replacement here succeeds.\n')
print('Updated B100 scope to cite the actual B102/B105 comparison.')
