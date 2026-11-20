from audit_amend import *

t=(WORK/'pages/15_scan193.tex').read_text()
replacements=[
    (r'\inserted{[$\pi_1(X)$ opère sur $\xi_\ell$]}',r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {[$\pi_1(X)$ opère sur $\xi_\ell$]};\draw (-2.45,-.48)--(-2.4,-.12) .. controls (-2.3,.03) and (-.7,-.02) .. (1.9,-.02) .. controls (2.5,-.02) and (2.65,.08) .. (2.5,.18);\end{tikzpicture}}}', 'upper inserted bracket', 'A left descending hook joins a long shallow curve immediately beneath the bracketed insertion and a small upward return at its right end.'),
    (r'\inserted{de $X$}',r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {de $X$};\draw (-.6,-.43) .. controls (-.28,-.1) and (.7,-.04) .. (.65,.17);\end{tikzpicture}}}', 'de X insertion', 'The short curved insertion leader runs upward and right from pt to the words de X above it.'),
    (r'\inserted{(étendus à $\mathbb{W}_p(k)$)}',r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {(étendus à $\mathbb{W}_p(k)$)};\draw (-1.8,-.45)--(-1.75,-.12) .. controls (-1.5,.02) and (-.4,.01) .. (1.25,.01) .. controls (1.9,.01) and (2.05,.1) .. (2.08,.2);\end{tikzpicture}}}', 'Witt-ring parenthesis insertion', 'A descending hook at the left turns into a long curve beneath the inserted parenthesis, with an upward-curled right end.'),
]
ivs=[r for r in readrows(PREFIX+'_inventory.csv') if r['scan']=='15/193']
changes=[]; additions=[]
for old,new,place,evidence in replacements:
    assert old in t
    t=t.replace(old,new)
    changes.append(change(place+' leader','words without a drawn leader','words without a drawn leader','inserted words and curved leader',evidence,'drawing or diagram',c=True))
    needle = 'opère' if place.startswith('upper') else ('de X' if place.startswith('de X') else 'étendus')
    candidates=[r for r in ivs if r['kind']=='insertion' and needle in r['first_words_or_objects']]
    if not candidates:
        candidates=[r for r in ivs if needle in r['first_words_or_objects']]
    assert len(candidates)==1, (needle,candidates)
    additions.append((int(candidates[0]['element']),inv('drawing',place, 'curved insertion leader')))
amend('15','193',t,changes,additions)
