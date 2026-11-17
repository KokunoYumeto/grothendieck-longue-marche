from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root));import workflow
for p in sorted((root/'pages').glob('*.tex')):
    s=p.read_text(); old=s
    if r'\text{\uline{$\cos^2u$}}' not in s:
        s=s.replace(r'\uline{$\cos^2u$}',r'\text{\uline{$\cos^2u$}}')
    if 'scan060' in p.name:
        s=s.replace(r'\deleted{\unsure{G_x}}',r'\deleted{\unsure{\ensuremath{G_x}}}')
    if 'scan068' in p.name:
        s=s.replace(r'\deleted{\unsure{\frac1p+\frac13+\frac12}}',r'\deleted{\unsure{\ensuremath{\frac1p+\frac13+\frac12}}}')
    for _,arg in list(workflow.macro_arguments(s,'diagram')):
        if '\\begin{array}' in arg and not arg.lstrip().startswith((r'\(',r'\[',r'\ensuremath',r'\begin{tikzcd}')):
            s=s.replace('\\diagram{'+arg+'}','\\diagram{\\ensuremath{'+arg+'}}')
    def matrix(m):
        body=re.sub(r'(?<!\\)&',r'\\&',m.group(1))
        if 'ampersand replacement=' not in body:
            body=('[ampersand replacement=\\&,'+body[1:]) if body.startswith('[') else '[ampersand replacement=\\&]'+body
        return r'\begin{tikzcd}'+body+r'\end{tikzcd}'
    s=re.sub(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',matrix,s,flags=re.S)
    if s!=old:
        p.write_text(s)
        print(p.name)
workflow.log('Technical encoding pass '+workflow.now()+': explicit math mode for math-only annotations/arrays; ampersand replacement in tikzcd arguments. No intended reading changes. Compilation unavailable: required TeX class/packages/formats absent.')
