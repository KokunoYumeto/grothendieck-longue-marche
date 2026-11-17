import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(33,[
(r'\unsure{G^*|G^\times}',r'\unsure{G^\times|G^*}'),
(r'\deleted{\unsure{G(j)=\text{face}}}',r'\deleted{\unsure{G(j)=\{x\in}}'),
(r'R(x)\unsure{\subset|\in}G',r'R(x)\unsure{\in|\subset}G')
],doubts=[
('audit cancelled definition above hat C','G(j)={x in','unfinished set-builder expression, not the word face','medium'),
('audit first winning superscript','G cross','G star; x-shaped mark has two clear strokes','medium'),
('audit losing iff explanatory formula','R(x) in G','R(x) subset G; short middle stroke visible','medium')],comment='Re-read both halves against saved text. Corrected a deleted set-builder fragment and first readings of two signs; retained local differences rather than harmonising by meaning.')
