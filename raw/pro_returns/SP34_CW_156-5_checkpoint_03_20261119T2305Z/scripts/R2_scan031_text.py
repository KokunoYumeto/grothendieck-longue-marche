from pathlib import Path
root=Path('/workspace/scratch/4770596940a0')
p=root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan031.tex'
s=p.read_text()
def change(a,b):
 global s
 assert a in s,a
 s=s.replace(a,b,1)
change("${\\unsure{F|\\mathcal F}}'$", "$F'$")
change("% @ upper part, support equality\n\\[\n |F'|=|F|", "% @ upper part, support relation: hooked upper stroke over detached lower bar\n\\[\n |F'|\\unsure{\\supseteq|=}|F|")
change(r'\deleted{\unsure{B}} $x\in B$',r'\deleted{$B\ni$} $x\in B$')
change(r'A^{\unsure{\bullet|\circ}}',r'A^{\unsure{\circ|\bullet}}')
change(r'$\deleted{\unsure{B}}A\in F\prime$',r'$\deleted{B}A\in F\prime$') if r'$\deleted{\unsure{B}}A\in F\prime$' in s else None
change("$\\deleted{\\unsure{B}}A\\in F'$", "$\\deleted{B}A\\in F'$")
change("c'est le plus petit", "c'est lui plus petit")
change(r'\deleted{\unsure{raffine}}',r'\deleted{raffine}')
change("Comme $|F'|=|F|$", "Comme $|F'|\\unsure{\\supseteq|=}|F|$")
change(r'\unsure{seult}', 'seult')
old=r"\deleted{1$^\circ$) \deleted{Soit} $A\in F'$, \unsure{et} l'ens $F^A$ des $B\in F$ tels que $A\subset B$ \unsure{est contenu dans} un plus petit \inserted{\unsure{a un plus petit}} \unsure{élémt|élément|élt} de $F$. C'est évident si $A\in F$ c'est évident. Si}"
new=r"""\deleted{1$^\circ$) \deleted{$\forall$} $A\in F'$, 
% @ upper interlinear addition within the cancelled draft
\inserted{l'ens $F^A$ des $B\in F$ tels que $A\subset B$}
% @ base line: a single short word precedes contenu, not two separate et/est occurrences
\unsure{est|et} \unsure{contenu dans} un plus petit
% @ left slanted addition, with a leader toward the following abbreviation
\inserted{a un plus petit} \unsure{élémt|élément|élt} de $F$. C'est évident si $A\in F$ c'est évident. Si}"""
change(old,new)
change(r"1$^\circ$) \deleted{Soit} $A\in F'$, l'ens",r"1$^\circ$) \deleted{$\forall$} $A\in F'$, l'ens")
change(r'\mid \deleted{\unsure{B}}A\subset B',r'\mid \deleted{B}A\subset B')
(root/'out/readers/R2/scan031.tex').write_text(s)
print('written scan031.tex',len(s))
