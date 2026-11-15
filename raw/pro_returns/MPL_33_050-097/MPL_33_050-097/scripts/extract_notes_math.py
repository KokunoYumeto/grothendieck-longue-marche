"""Generate a disposable TeX syntax check of the Markdown research formulas."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
text = (root/'MPL_33_050-097_notes.md').read_text()
formulas = re.findall(r'\$([^$\n]+)\$',text)
target = Path(sys.argv[1]) if len(sys.argv)>1 else root.parent/'validation/notes_math_check.tex'
target.parent.mkdir(parents=True,exist_ok=True)
preamble = r'''\documentclass{article}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{fontspec}
\begin{document}
'''
target.write_text(preamble+'\n'.join(str(i+1)+': $'+m+'$\\par' for i,m in enumerate(formulas))+r'\end{document}'+'\n')
print(len(formulas),'inline mathematical spans extracted to',target)

