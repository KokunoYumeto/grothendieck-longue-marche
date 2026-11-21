from pathlib import Path
import json
R=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work');p=R/'reports/151_scan015.json';d=json.loads(p.read_text());tp=R/'reports/151_scan015.tex';t=tp.read_text()
oval=r'\begin{tikzpicture}[baseline=(n.base)]\node[inner sep=0pt] (n) at (0,0) {Hyp};\draw (-.65,-.05)..controls(-.4,.46)and(.28,.57)..(.56,.3)..controls(.83,-.15)and(.38,-.53)..(0,-.51)..controls(-.51,-.51)and(-.72,-.27)..(-.65,-.05);\end{tikzpicture}'
assert r'\textcircled{Hyp}' in t;t=t.replace(r'\textcircled{Hyp}',oval)
for c in d['changes']:
 if r'\textcircled{Hyp}' in c['final']:c['final']=c['final'].replace(r'\textcircled{Hyp}',oval)
d['notes'].append('Independent audit: all seven differing encodings retain the same ink reading. The enclosure around the whole word Hyp is encoded as an inline TikZ oval with a text node so the three letters fit inside it; this replaces the single-character textcircled implementation without changing enclosure scope or correction counts. The final question retains the written equals abbreviation and the visible t after ex. The blind reader noted the central hypothesis/limit block outside the boxes; root checked the stipulated box criteria: it contains no handwritten numeral, doubt, alteration, marginal text, witness-word disagreement, or lower-confidence departure requiring an additional second-reading box.')
e={
'B002':'The b-prime label, phi exclamation indices, F/G product and quantifier agree. A-hat and A with a raised wedge are equivalent encodings of the same written sign; line wrapping adds no reading.',
'B003':'The c-prime fibre product and its base F agree. The cospan has G and H above F with both arrows toward F, and the final A-hat and period remain. Matrix syntax and hat encoding alone differ.',
'B004':'Unique has the initial u/n, dotted i, q descender and ue ending; both readers read it. Hyp 1,2,2-prime and punctuation agree. The second reading moves numerals into math mode and retains a physical line break only.',
'B005':'The complete word Hyp is enclosed by one closed rounded contour. Both readings state that same scope. An inline text-node/oval encoding replaces textcircled for correct width; this is a macro/layout repair, not a changed ink reading.',
'B006':'The word after et has a tall initial d followed by joined low ans; dans is retained. The singleton dot, two discrete dots and three-point cospan agree, as do all quantifiers and the continuation correspondants aux axiomes.',
'B007':'The three labels are Hyp 1, Hyp 2, Hyp 2-prime. The point precedes the closing parenthesis. Math-mode wrappers and whitespace differ only.',
'B008':'Two nearly parallel horizontal strokes encode the written equals abbreviation; mild pen undulation does not establish a separate similarity sign. After ex and its dot there is a distinct tall crossed t; omitting that letter loses ink. The grave-accented à and the question mark following gauche are separate and clear.'}
m={k:dict(changed=False,evidence=v) for k,v in e.items()};m['B005']['final']=oval
(R/'reviews/151_scan015_manual.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');tp.write_text(t)
