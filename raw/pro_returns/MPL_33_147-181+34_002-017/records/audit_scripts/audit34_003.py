import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
revise(34,3,r'0.1. \unsure{Notations}.',r'0.1. \uline{\unsure{Notations}}.')
revise(34,3,r'\underset{\nu}{\uline{\lim}}',r'\underset{\nu}{\unsure{\uline{\lim}|\varprojlim}}')
audit(34,3,'Both halves and enlarged notation, ell-condition and final paragraph checked. Underlining of Notations restored; the low stroke under lim is marked underline/left-limit-arrow rather than assuming a direction. Interlinear V and V/m in quotation marks, deleted title and two successive versions of the ell-condition sentence, inserted i entier, empty Hironaka citation parentheses and three cases remain present. The passage about the first part of the seminar and the short sign before strictement locale remain low confidence.')
