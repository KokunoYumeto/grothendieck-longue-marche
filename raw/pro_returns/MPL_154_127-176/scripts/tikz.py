"""Serialize manually sight-read coordinates. No image reading or OCR."""
def start():
    return r'\figure{\begin{tikzpicture}[x=.55cm,y=-.55cm,line cap=round,line join=round,g/.style={olive!80!yellow,line width=1.7pt},r/.style={orange!80!brown,line width=1.8pt},w/.style={red!60!black,line width=1.5pt},b/.style={blue!60!black,line width=1.4pt},p/.style={gray!70,thin},k/.style={black,line width=1.2pt},every node/.style={font=\scriptsize}]'+'\n'
def end():
    return '\\end{tikzpicture}}\n'
def path(style,points,smooth=True,close=False):
    coords=' '.join('('+p+')' for p in points.split())
    if smooth:
        body='plot[smooth'+(' cycle' if close else '')+'] coordinates {'+coords+'}'
    else:
        body='--'.join('('+p+')' for p in points.split())+('--cycle' if close else '')
    return '\\draw['+style+'] '+body+';\n'
def paths(style,lines,smooth=True,close=False):
    return ''.join(path(style,s.strip(),smooth,close) for s in lines.strip().split(';') if s.strip())
def dots(style,points,r='.045'):
    return ''.join('\\fill['+style+'] ('+p+') circle ('+r+');\n' for p in points.split())
def labels(items):
    return ''.join('\\node at ('+xy+') {$'+s+'$};\n' for xy,s in items)
def comment(s):
    return '% '+s+'\n'
