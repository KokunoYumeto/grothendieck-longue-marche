#!/usr/bin/env python3
"""Assemble the research notes only; frozen transcription files are not touched."""
from pathlib import Path
p=Path(__file__).resolve().parents[1]
parts=[p/'records'/f'main_notes_part{i}.md' for i in range(1,5)]
text='\n\n'.join(f.read_text().rstrip() for f in parts)+'\n'
(p/'MPL_64_078-115_notes.md').write_text(text)
print(f'Research notes assembled: {len(text.split())} words, {text.count(chr(10))} lines')
