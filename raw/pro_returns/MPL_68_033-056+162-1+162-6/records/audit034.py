import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(34,[
(r'\deleted{\unsure{alors}} et',r'\deleted{\unsure{alors on a}} et'),
(r'Soit $(C;$ un jeu',r'Soit $(C;\unsure{)}$ un jeu'),
(r'\deleted{\unsure{G(j)\subset}}',r'\deleted{\unsure{G_0(j)\subset}}')
],doubts=[
('audit cancellation after lautre','alors on a','last strokes may include a capital G rather than on a','low'),
('audit Cor opening','(C;)','closing curved stroke partly joined to un','medium'),
('audit Cor cancelled formula','G_0(j) subset','final relation and subscript small and crossed','low')],comment='Both halves and three enlarged cancellations checked. Added omitted subscript and cancelled words; left unrestricted quantifiers in conditions 1 and 2 exactly as written.')
