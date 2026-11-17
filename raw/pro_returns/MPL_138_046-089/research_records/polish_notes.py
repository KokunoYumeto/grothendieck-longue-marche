"""Spacing-only cleanup of research prose; never reads or edits page TeX."""
from pathlib import Path
import re

path = Path(__file__).resolve().parent.parent / 'MPL_138_046-089_notes.md'
s = path.read_text()
parts = re.split(r'(`[^`]*`|\\\(.*?\\\)|\\\[.*?\\\]|https?://[^\s)]+)',s,flags=re.S)
words = r'Scans?|scans?|levels?|rank|June|August|September|cote|pages?|line|count|circa|Theorem|Corollary|Proposition|genre|coefficient|orders|above|to|is|or|most|exceeding|say|lemme|original|published|on|and|at'
for i in range(0,len(parts),2):
    parts[i] = re.sub(r'\b('+words+r')(?=\d)',r'\1 ',parts[i])
    parts[i] = re.sub(r'\batL(?=\d)',r'at L',parts[i])
    parts[i] = parts[i].replace('atL94','at L94').replace('Pages1','Pages 1')
s=''.join(parts)
s=s.replace('*14(2)', '* 14(2)').replace('*111(4)', '* 111(4)')
s=s.replace('(1980),247–256','(1980), 247–256').replace('(1979),267–276','(1979), 267–276').replace('(2015),775–796','(2015), 775–796')
s=s.replace('arXiv:1309.1968v2,20','arXiv:1309.1968v2, 20').replace('date,2 August','date, 2 August')
path.write_text(s)
print('Research prose spacing updated; frozen files untouched.')
