from audit_support import revise
revise(28,replacements=[
(r'\unsure{déf. can. unique par $A$}',r'\unsure{déf. non unique par $A$|déf. can. unique par $A$}'),
(r"d'\unsure{être déterminer}",r"d'\unsure{être déterminée|être déterminer}"),
(r'\unsure{aux} $k$-simpliciaux ordinaires',r'\unsure{groupes|grps} $\frac12$-simpliciaux ordinaires')],
doubts=[('lines 5–8','déf. non unique par A; être déterminée','déf. can. unique par A; être déterminer','low'),('line 12','groupes ½-simpliciaux','grps ½-simpliciaux','medium')],
notation=[('½-simpliciaux',r'\frac12\text{-simpliciaux}','Diagonal fraction stroke and lower 2 visible in scan 028; not k.')],
note='Second visual audit; inspected whole scan, supplied half and enlarged word regions. Corrected the fraction ½ preceding simpliciaux from its ink. The awkward parenthesis and verb ending remain explicitly uncertain; final operations sign has a Γ-shaped right angle.')
