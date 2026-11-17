import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(55,[
 ('% archive foliation: 54\n','% archive foliation: 54\n\\margin{\\illegible{1}}\n'),
],extra=[('margin note','upper right, above heading','faint erased or transferred marks, one word estimated')],doubts=[
 ('upper right above heading','unreadable faint marks','possibly erased/transferred lettering; V-like and vertical traces, no secure word or number','low'),
],comment='Re-read both halves and enlarged the faint mark after t e and the upper-right grey traces. Added the latter explicitly as unreadable; whether they are erased writing or transferred marks remains uncertain.')
