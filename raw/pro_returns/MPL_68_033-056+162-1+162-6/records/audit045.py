import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(45,[
 (r'au \unsure{même}',r'au $=$'),
 (r'\unsure{tels|telles}',r'\unsure{telles|tels}'),
 (r'\unsure{ces condts sont équivalentes}',r'\unsure{ces cond\textsuperscript{ts} st équivalentes|ces cond\textsuperscript{ts} sont équivalentes}'),
],doubts=[
 ('cancelled NB under part 1',r'ces cond\textsuperscript{ts} st équivalentes',r'sont; letters crossed by two rules','low'),
 ('part 2, inserted qualification','telles','tels','medium'),
],comment='Re-read both halves, rotated left margin, cancelled NB and inserted qualification. Preserved the literal equals shorthand and the visible feminine-looking ending; retained every withdrawn and replacement condition.')
