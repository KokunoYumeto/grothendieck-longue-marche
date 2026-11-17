import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(36,[
(r"\unsure{par l'identité} \unsure{d'indéterminées}",r"\unsure{par introduction|par l'introduction} \unsure{d'indéterminées}"),
(r'\unsure{\alpha_A|\alpha_U}:A',r'\unsure{\alpha_U|\alpha_A}:A'),
(r'\alpha_A(x)=0',r'\unsure{\alpha_U|\alpha_A}(x)=0'),
(r'\alpha_A(x)=1',r'\unsure{\alpha_U|\alpha_A}(x)=1'),
(r'\unsure{U|M}',r'\unsure{M|U}'),
(r'\deleted{\unsure{L=\text{pos}}}',r'\deleted{\unsure{\text{Ceci posé}}}')
],doubts=[
('audit left margin after réciproque?','par introduction / par lintroduction dindéterminées','faint slanting writing; identité no longer preferred','low'),
('audit quotient map and fibre formulas','alpha_U','alpha_A; subscript visibly round u-shaped while algebra A is overwritten','medium'),
('audit second description of L','u in M','u in U; strongly drawn M-like letter retained first','medium'),
('audit final cancelled fragment','Ceci posé','not L=pos; letters eci and final accent visible in enlargement','medium')],comment='Re-read both halves, rotated faint margin, and enlarged quotient subscripts and bottom cancellation. Preserved exp 1=0 and the locally inconsistent M/U reading.')
