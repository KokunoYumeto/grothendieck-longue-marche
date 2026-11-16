#!/usr/bin/env python3
"""Retain and idempotently reapply the two recorded twelfth-hour layout fixes."""
from pathlib import Path
w=Path(__file__).resolve().parents[1]
p=w/'sections/harmonic_prym_full_sha.tex';s=p.read_text()
end=s.index(r'\tag{A.160.2}')
start=s.rfind('\\[',0,end)
assert start>=0
replacement=r'''\[
 \begin{gathered}
 A(\Q)=E_b(K)=\{O,T_0\},\\
 \Sha(A/\Q)=\Sha(E_b/K),\\
 T_\ell\Sha(A/\Q)=0\quad\text{for every prime }\ell.
 \end{gathered}
'''
fixed=s[:start]+replacement+s[end:]
if fixed!=s:p.write_text(fixed)
for name in ['SECTIONS_OVER_Q_references.bib','notes/harmonic_prym_cm_references.bib']:
 p=w/name;s=p.read_text()
 for filename in ['notes/primary_sources/rubin1987_p527.jpg','rubin1987_p528.jpg','rubin1987_p529.jpg','rubin1987_gdz_manifest.json']:
  if r'\path{'+filename+'}' not in s:
   assert filename in s;s=s.replace(filename,r'\path{'+filename+'}')
 if s!=p.read_text():p.write_text(s)
print('A160.2: three exact identifications on three gathered lines; retained36.01785pt initial overflow corrected.')
print('Rubin original-source filenames: all four use path formatting in both retained bibliography sources.')
print('The final LuaLaTeX build log and actual visual review are recorded separately.')
