import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(50,[
 (r'\Omega(W)\simeq\Omega\prime(W)',r'\Omega(W)\xrightarrow{\sim}\Omega\prime(W)'),
] if False else [
 ("\\Omega(W)\\simeq\\Omega'(W)","\\Omega(W)\\xrightarrow{\\sim}\\Omega'(W)"),
 (r'\unsure{p. esp.}',r'\unsure{p. es|p. esp.}'),
 (r"d'une th.} Existence",r"d'une \unsure{th.|théorie}} Existence"),
],doubts=[
 ('orientation heading before vectoriels','p. es','p. esp.; no clear descender in second abbreviation','low'),
 ('cancelled heading before Existence','th.','théorie; ending crossed','low'),
],comment='Both halves and enlarged lemma, axiom, proof and heading regions re-read. Restored the right arrowhead in the proof isomorphism, retained Omega(W) under phi_V and the reversal Omega(V,W) at the foot.')
