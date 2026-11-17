import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(48,[
 (r'\unsure{\exists}\rho',r'\unsure{\exists}\deleted{\unsure{a}}\rho'),
],extra=[('deletion','Jeu circulaire, condition 2, after existential sign','a (overwritten trace)')],doubts=[
 ('Jeu circulaire, immediately after existential sign','a','cancelled glyph or part of retraced quantifier','low'),
],comment='Both halves re-read, including enlarged quantifier, NB insertion and cancelled tuple. Included the dark overwritten trace after the quantifier; retained all local x/y uncertainties.')
