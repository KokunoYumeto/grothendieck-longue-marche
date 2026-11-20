"""Separate three TeX control words from following literal Latin letters.

This is a source-format correction only; it does not change any diplomatic
reading, and is therefore excluded from witness-difference counts.
"""
from workflow import *
for filename,old,new in [
 ('16_scan006.tex',r'\longrightarrowM',r'\longrightarrow M'),
 ('16_scan012.tex',r'\RightarrowL',r'\Rightarrow L'),
 ('16_scan015.tex',r'\quadL',r'\quad L')
]:
 p=WORK/'pages'/filename;t=p.read_text()
 assert old in t,filename
 p.write_text(t.replace(old,new))
 log(f'formatting only {filename} {now()}: separate control word {old} as {new}; no reading change')
rebuild()
