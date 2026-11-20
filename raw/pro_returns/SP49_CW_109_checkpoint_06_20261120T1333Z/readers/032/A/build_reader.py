from pathlib import Path
import json, re, difflib

root=Path('work/readers/032/A')
meta=json.loads(Path('work/inputs/032/metadata.json').read_text())
C=Path('work/inputs/032/C.tex').read_text()
s=C
a,b,w=meta['half_a'],meta['half_b'],meta['whole']
def tx(x): return x.replace('§',chr(92)).replace('¤',chr(96))
def rep(old,new):
    global s
    old,new=tx(old),tx(new)
    if old not in s: raise ValueError('Replacement absent: '+old)
    s=s.replace(old,new,1)
changes=[]
def add(id,place,c,reading,kind,confidence,evidence,source,bbox,crop=None,code_reference=None):
    c,reading=tx(c),tx(reading)
    if c and c not in C: raise ValueError('Nonliteral C field: '+c)
    row=dict(id=id,place=place,c=c,h=None,reading=reading,diff_c=True,diff_h=False,kind=kind,marked_in_H=False,confidence=confidence,evidence=evidence,crop=('crops/'+crop+'.jpg') if crop else None,source=source,bbox=bbox)
    if code_reference: row['code_reference']=code_reference
    changes.append(row)

old=r"""¤allows one to''"""
new=r"""§unsure{¤¤|¤}allows one to''"""
rep(old,new)
add('428-allows-opener','p 428 l.6, opening quotation',old,new,'misread symbol or index','medium','The opening group has a long left limb and a shorter joined right limb. A fused pair is favoured, but a single hooked stroke remains possible; the closing pair is separate and clear.',a,[384,165,736,252],'02')

old=r"""§deleted{l-5 ¤its''}"""
new=r"""§deleted{l-5} ¤§deleted{its}''"""
rep(old,new)
add('440-first-quote-state','p 440, cancelled l-5 its proposal',old,new,'deletion state (struck given live or live given struck)','high','The cancellation runs across the reference and word. The single high opener and both high closing strokes stand above the upper cancellation path, with clear gaps.',a,[575,679,787,767],'05')

old=r"""§deleted{¤¤allows one to''}§unsure{-+|+}"""
new=r"""¤¤§deleted{allows one to}''§unsure{-+|+}"""
rep(old,new)
add('440-second-quote-state','p 440, cancelled allows one to proposal',old,new,'deletion state (struck given live or live given struck)','high','Both opening strokes and the closing group lie outside the zigzag crossing the words. The horizontal segment adjoining the closer and the following cross remain the existing local doubt.',a,[778,677,1114,770],'06')

old=r"""l.3 ¤don't''"""
new=r"""l.3 §unsure{¤|¤¤}don't''"""
rep(old,new)
add('441-dont-opener','p 441 l.3, opening quotation',old.removeprefix('l.3 '),new.removeprefix('l.3 '),'misread symbol or index','medium','The high opener is a hooked body with a short upper-right spur. Its fused top does not securely distinguish one stroke from two; a single opener is the first candidate.',a,[303,794,506,897],'07')

old=r"""§deleted{l 9 ¤¤its''}"""
new=r"""§deleted{l 9} ¤¤§deleted{its}''"""
rep(old,new)
add('447-cancel-quote-state','p 447, cancelled l 9 its proposal',old,new,'deletion state (struck given live or live given struck)','high','The horizontal cancellation passes through l 9 and its; the two opener strokes end just above it and the separate closer pair is much higher than its right endpoint.',a,[1174,994,1404,1085],'08')

old=r"""§deleted{§unsure{o}}§inserted{§deleted{one}}"""
corr449=r"""§tikz[baseline=(old449A.base)]{
  §node[inner sep=0pt] (old449A) {§deleted{§unsure{o}}};
  §node[overlay,anchor=base west,inner sep=0pt] at ([xshift=-.08em,yshift=1.65ex]old449A.base west) {§inserted{§deleted{one}}};
  §draw[overlay,line width=.35pt,line cap=round]
    ([xshift=.08em,yshift=1.15ex]old449A.north west)
    .. controls ([xshift=-.35em,yshift=1.0ex]old449A.north west) and ([xshift=-.30em,yshift=.3ex]old449A.north west)
    .. ([xshift=.02em,yshift=.1ex]old449A.north west);
  §draw[overlay,line width=.35pt,line cap=round]
    ([xshift=.05em,yshift=-.05ex]old449A.south west)
    .. controls ([xshift=.38em,yshift=-.10ex]old449A.south west) and ([xshift=.20em,yshift=-.55ex]old449A.south west)
    .. ([xshift=.04em,yshift=-.80ex]old449A.south west)
    -- ([xshift=.32em,yshift=-.65ex]old449A.south west)
    -- ([xshift=.12em,yshift=-1.15ex]old449A.south west);
}"""
rep(old,corr449)
add('449-raised-correction','p 449 l 11, between allows and us',old,corr449,'insertion or placement','medium','The cancelled one is physically raised above the gap before us. A curved connector extends down along the left of its baseline loop and continues below the line. The loop can still be an old o or part of that connector, so the old-letter doubt is retained.',a,[433,1117,594,1210],'09')

old=r"""§unsure{§&|a}"""
new=r"""§&"""
rep(old,new)
add('450-link-sign','p 450, final reference between -2 and -3',old,new,'misread symbol or index','high','The linking sign has an upper loop, an intersecting diagonal, a separate small lower-left loop and a rising right terminal. These strokes decide an ampersand.',b,[996,163,1180,234],'11')

old=r"""§unsure{.}"""
dot452=r"""§tikz[baseline=0pt,x=1ex,y=1ex]{§fill (.15,.45) circle (.07);}"""
rep(old,dot452)
add('452-low-point','p 452 l-11, below and right of the opener',old,dot452,'other','high','The crop confirms a distinct low dark point before the d. Its geometry is certain; the transcription preserves that position without assigning the mark a punctuation function or origin.',b,[323,223,524,292],'12')

old=r"""§underset{§unsure{§equiv|§mathrm{E}}}{§text{i}}"""
new=r"""§underset{§unsure{§mathrm{E}|§equiv}}{§text{i}}"""
rep(old,new)
add('455-under-i-mark','p 455 l-13, beneath the first i of divided',old,new,'misread symbol or index','medium','Three short dark levels have a visibly inked left join. This makes an E-shaped mark the first candidate. An equivalence-like emphasis mark remains possible; it is directly beneath the first i, not part of the next line quotation.',b,[367,408,587,508],'13')

old=r"""§deleted{§unsure{l 9|l}}"""
new=r"""§deleted{§unsure{l§textsubscript{9}|l}}"""
rep(old,new)
add('466-old-reference-placement','p.466, cancelled group before the live l-9',old,new,'insertion or placement','medium','The tall old loop is certain and the hooked, looped remnant is physically below its right side. The cancellation makes its identification as 9 uncertain. The lower placement is preserved without resolving the l 9 versus l doubt.',b,[228,986,424,1069],'15')

old=r"""¤¤and iterating'"""
new=r"""¤¤and iterating§unsure{''|'}"""
rep(old,new)
add('468-terminal-quote','p 468 l.8, terminal quotation after iterating',old,new,'misread symbol or index','medium','The high terminal group has two descending legs and a small pale inner notch but a fused upper body. A double closer is favoured; a single hooked closer is retained as an alternative.',b,[1340,1094,1615,1261],'18')

# Distinct marks are anchored to neighbouring text; no punctuation function is assigned.
point427=r"""§tikz[overlay,x=1ex,y=1ex]{§fill (-1.35,.08) circle (.055);}"""
rep('p 427 l-6',point427+'p 427 l-6')
add('427-left-point','Left of the p 427 page reference','',point427,'drawing or diagram','high','One small dark point is visibly separate from the page-reference p and the left sheet edge.',a,[62,153,83,174])

ref428=r"""§tikz[baseline=(ref428A.base)]{
  §node[inner sep=0pt] (ref428A) {l-9};
  §fill ([xshift=.40em,yshift=3.15ex]ref428A.base west) circle (.055ex);
  §fill ([xshift=.64em,yshift=3.35ex]ref428A.base west) circle (.030ex);
  §fill ([xshift=1.55em,yshift=2.55ex]ref428A.base west) circle (.040ex);
  §fill ([xshift=1.67em,yshift=2.72ex]ref428A.base west) circle (.040ex);
}"""
rep(r"""§quad l-9 ¤¤we'd better''""",r"""§quad """+ref428+r""" ¤¤we'd better''""")
add('428-reference-points','p 428, above the l-9 reference for wed better','',ref428,'drawing or diagram','high','Four dark points form two separated small groups above the reference. None is the word apostrophe or either quoted edge. Their geometry is preserved without an assigned origin.',a,[747,170,814,205],'03')

sense434=r"""§tikz[baseline=(sense434A.base)]{
  §node[inner sep=0pt] (sense434A) {¤¤makes sense''};
  §fill ([xshift=3em,yshift=1.6ex]sense434A.base east) circle (.045ex);
}"""
rep(r"""l-12 ¤¤makes sense''""",'l-12 '+sense434)
add('434-right-point','Blank area to the right of the p 434 entry','',sense434,'drawing or diagram','high','A separate small dark point lies above and well to the right of the closing quotation, not at the text baseline.',a,[1107,507,1127,528])

dont441=r"""§tikz[baseline=(dont441A.base)]{
  §node[inner sep=0pt] (dont441A) {§unsure{¤|¤¤}don't''};
  §fill ([xshift=.40em,yshift=2.55ex]dont441A.base) circle (.035ex);
}"""
rep(r"""l.3 §unsure{¤|¤¤}don't''""",'l.3 '+dont441)
add('441-high-point','p 441 l.3, above the n/apostrophe area of dont','',dont441,'drawing or diagram','medium','A small separate dark point appears above-left of the internal apostrophe. It is neither the opener nor the apostrophe body and is retained geometrically.',a,[421,814,441,834],'07')

old447=r"""§tikz[baseline=(old447A.base)]{
  §node[inner sep=0pt] (old447A) {§deleted{l 9} ¤¤§deleted{its}''};
  §fill ([xshift=-.40em,yshift=2.4ex]old447A.base) circle (.05ex);
}"""
rep(r"""§deleted{l 9} ¤¤§deleted{its}''""",old447)
add('447-point-above-opener','p 447, above-left of the cancelled entry opener','',old447,'drawing or diagram','high','The extra dark point stands above-left of the two opening strokes. The dot above the i is a different physical mark and is not duplicated.',a,[1258,1010,1279,1031],'08')

edge447=r"""§tikz[overlay,x=1ex,y=1ex]{§fill (12.7,1.7) circle (.035);}"""
rep(old447,old447+edge447)
add('447-far-right-point','Far right sheet area level with p 447','',edge447,'drawing or diagram','medium','A tiny isolated dark point is visible close to the right sheet edge, separate from the cancelled entry and from the vertical rule.',a,[1643,1022,1663,1044])

blank452=r"""§tikz[overlay,x=1ex,y=1ex]{§fill (21.3,-.65) circle (.06);§fill (28.4,-.5) circle (.03);}"""
rep(dot452+r""" don't''""",dot452+r""" don't''"""+blank452)
add('452-right-blank-points','Blank space to the right of the p 452 line','',blank452,'drawing or diagram','medium','The lower half shows a larger separate dark point and a much smaller point farther right. The two remain separated, without an inferred joining stroke.',b,[945,279,1107,302])

ref456=r"""§tikz[baseline=(ref456A.base)]{
  §node[inner sep=0pt] (ref456A) {l.2};
  §fill ([xshift=.12em,yshift=.1ex]ref456A.base east) circle (.035ex);
  §begin{scope}[shift={([xshift=-.18em,yshift=-.65ex]ref456A.base east)},x=1ex,y=1ex]
    §fill (0,.18)--(.15,.12)--(.19,-.07)--(.03,-.15)--(-.11,-.08)--(-.12,.09)--cycle;
  §end{scope}
  §fill ([xshift=-.12em,yshift=-1.5ex]ref456A.base east) circle (.055ex);
}"""
rep('p 456 l.2','p 456 '+ref456)
add('456-reference-marks','Below and just right of p 456 l.2','',ref456,'drawing or diagram','high','The crop separates a small upper point, a larger irregular dark body below the 2, and a lower small point. The abbreviation point between l and 2 is independently present in C and remains a single occurrence.',b,[234,478,352,568],'14')

blank456=r"""§tikz[overlay,x=1ex,y=1ex]{§fill (16.8,-.6) circle (.035);}"""
rep(ref456+r""" ¤¤its'' §quad l 9 ¤¤don't''""",ref456+r""" ¤¤its'' §quad l 9 ¤¤don't''"""+blank456)
add('456-right-blank-point','Blank area right of the p 456 line','',blank456,'drawing or diagram','medium','One short dark point is visible in the otherwise blank area to the right of the entry, below its baseline.',b,[1023,541,1043,562])

blank462=r"""§hfill§tikz[baseline=0pt,x=1ex,y=1ex]{§fill (0,0) circle (.04);§fill (.35,.35) circle (.045);}"""
rep(r"""l-1 ¤¤mimic''""",r"""l-1 ¤¤mimic'' """+blank462)
add('462-right-pair','Right blank area level with the p 462 l-1 continuation','',blank462,'drawing or diagram','high','Two distinct small dark points are arranged obliquely in the right blank area, with space between them.',b,[1424,890,1450,915])

ref466=r"""§tikz[baseline=(ref466A.base)]{
  §node[inner sep=0pt] (ref466A) {l-9};
  §fill ([xshift=.40em,yshift=-.75ex]ref466A.base west) circle (.04ex);
}"""
rep(r"""§deleted{§unsure{l§textsubscript{9}|l}}. l-9 ¤¤enters''""",r"""§deleted{§unsure{l§textsubscript{9}|l}}. """+ref466+r""" ¤¤enters''""")
add('466-lower-point','Below the live l in the p.466 l-9 reference','',ref466,'drawing or diagram','medium','A separate small point sits below the live l and left of the next line opener. It is distinct from the stop following the cancelled group.',b,[320,1049,338,1066],'15')

ref468=r"""§tikz[baseline=(ref468A.base)]{
  §node[inner sep=0pt] (ref468A) {l.8};
  §fill ([xshift=-.45em,yshift=-.15ex]ref468A.base east) circle (.06ex);
  §fill[black!55] ([xshift=-.35em,yshift=2.9ex]ref468A.base east) circle (.055ex);
  §draw[black!55,line width=.25pt,line cap=round] ([xshift=-.28em,yshift=2.9ex]ref468A.base east)--([xshift=-.02em,yshift=2.98ex]ref468A.base east);
}"""
rep(r"""l.8 ¤¤and iterating""",ref468+r""" ¤¤and iterating""")
add('468-reference-marks','Around the l.8 reference on the last line','',ref468,'drawing or diagram','high','The crop shows a low separate dark point beneath the left edge of 8 and a paler high round body with a short rightward tail. The point between l and 8 belongs to the reference and is not duplicated.',b,[1090,1100,1250,1205],'17')

# The rules stay beside/through the list rather than becoming a detached drawing.
anchor_top=r"""§tikz[remember picture,overlay]{
  §coordinate (left032A-top) at (-.2em,1.4ex);
  §coordinate (right032A-top) at ([xshift=.86§linewidth]left032A-top);
}"""
anchor_bottom=r"""§tikz[remember picture,overlay]{§coordinate (list032A-bottom) at (0,-4ex);}"""
rep('p.426 l-16','p.426 '+anchor_top+'l-16')
rep('p 468 l 3','p 468 '+anchor_bottom+'l 3')
left_rule=r"""§coordinate (left032A-end) at (left032A-top |- list032A-bottom);
§draw[line width=.35pt] (left032A-top)--([yshift=2.3ex]left032A-end);
§draw[black!35,line width=.35pt] ([yshift=2.3ex]left032A-end)--(left032A-end);"""
right_rule=r"""§coordinate (right032A-end) at (right032A-top |- list032A-bottom);
§draw[line width=.35pt] (right032A-top)--([yshift=3.6ex]right032A-end);
§draw[black!45,line width=.35pt] ([yshift=3.6ex]right032A-end)--([yshift=2.7ex]right032A-end);
§draw[black!22,line width=.35pt] ([yshift=2.3ex]right032A-end)..controls ([xshift=.12em,yshift=1.5ex]right032A-end) and ([xshift=.05em,yshift=.7ex]right032A-end)..([xshift=.08em]right032A-end);"""
rule_block=r"""
% RULES: dark upper portions, observed fading lower portions; right lower trace kept separate.
§begin{tikzpicture}[remember picture,overlay]
"""+left_rule+'\n'+right_rule+r"""
§end{tikzpicture}
"""
rep('% archive sheet number: 31',rule_block+'\n% archive sheet number: 31')
add('left-vertical-rule','Between page references and correction text, from p426 to the lower sheet edge','',left_rule,'drawing or diagram','high','A narrow dark vertical rule begins near whole-image (216,90), continues between the columns, and fades below the final line to the physical sheet edge near (211,2343). The endpoint crop shows a continuous pale tail to that edge.',w,[205,82,222,2347],'19','reading.tex: anchor_top and % RULES block')
add('right-vertical-rule','Right side of the list, crossing the longest entries','',right_rule,'drawing or diagram','high','A second narrow vertical rule begins near (1494,96). Its lower dark part fades around half-b y1173-1196. A lighter lower trace resumes after a short pale gap and reaches the sheet edge; the gap is preserved rather than connected.',w,[1482,86,1509,2346],'18','reading.tex: anchor_top and % RULES block')

s=tx(r'§cotefile{109}'+'\n')+s
(root/'reading.tex').write_text(s)

# Explicit C doubts and all page-specific context judgements.
c_doubts=[]
def doubt(place,c,reading,resolved,confidence,evidence,source,bbox,crop=None,explicit_c=False):
    c,reading=tx(c),tx(reading)
    if c and c not in C: raise ValueError('Nonliteral doubt C field: '+c)
    c_doubts.append(dict(place=place,c=c,reading=reading,resolved=resolved,confidence=confidence,evidence=evidence,crop=('crops/'+crop+'.jpg') if crop else None,source=source,bbox=bbox,explicit_c=explicit_c))
doubt('p 428 second hatted A, lower-right index',r'§unsure{M|m}',r'§unsure{M|m}',False,'medium','Two angular humps and a long final downstroke favour M, but the small cursive m form remains possible. Case is not inferred from the sentence.',a,[1206,209,1385,337],'04',True)
doubt('p 440 after the cancelled allows one to',r'§unsure{-+|+}',r'§unsure{-+|+}',False,'medium','The horizontal segment touches the second closing stroke; the small following cross is clear, but whether the segment is an independent minus or a quote return is not decided.',a,[778,677,1114,770],'06',True)
doubt('p 449 baseline loop before us',r'§deleted{§unsure{o}}',r'§deleted{§unsure{o}}',False,'low','The loop lies in a descending correction connector; an old cancelled o remains plausible, but connector geometry can account for it. Raised one is separately legible and cancelled.',a,[433,1117,594,1210],'09',True)
doubt('p 450 link between -2 and -3',r'§unsure{§&|a}',r'§&',True,'high','Upper and lower loops with a crossing diagonal and rising exit decide the ampersand.',b,[996,163,1180,234],'11',True)
doubt('p 452 low point before dont',r'§unsure{.}',dot452,False,'medium','A real separate point is visible. Its period function and physical origin are not established, so it is reproduced at its observed height without naming it a full stop.',b,[323,223,524,292],'12',True)
doubt('p 455 mark beneath first i',r'§unsure{§equiv|§mathrm{E}}',r'§unsure{§mathrm{E}|§equiv}',False,'medium','Three dark horizontal levels and a continuous inked left edge favour E-shape. Equivalence-like emphasis remains possible. Alignment attaches the group beneath the first i.',b,[367,408,587,508],'13',True)
doubt('p.466 cancelled old reference',r'§deleted{§unsure{l 9|l}}',r'§deleted{§unsure{l§textsubscript{9}|l}}',False,'low','The upper loop is l-like; the much lower hooked loop can be 9 or part of the cancellation. The live l-9 is not used to force the old numeral.',b,[228,986,424,1069],'15',True)
doubt('p 428, both hatted capital letters',r'§hat{A}',r'§hat{A}',True,'high','Both occurrences have an ordinary single-contour A and a separate pointed roof. The second A cross-stroke loops back but does not produce an independently doubled alphabet.',a,[408,231,1370,327],'04')
doubt('p.438 l 4, isolated delimiter',r'§mbox{$)$}',r'§mbox{$)$}',True,'high','One closing curve is present before missing from formula; no opening mate is written there. The cited formula itself is not supplied and was not reconstructed.',a,[338,567,786,638])
doubt('p 449 l-8, k-modules',r'$k$-modules',r'$k$-modules',True,'high','The lower half shows one lowercase k with its ascender and diagonal limbs, followed by the short hyphen and modules.',b,[1125,108,1375,170])
doubt('p 450 reduced s at foot of l',r'l§textsubscript{s}',r'l§textsubscript{s}',True,'high','A small two-curved s is joined at the foot of the looped l and sits below the main numeral baseline.',b,[996,163,1180,234],'11')
doubt('p 428, qualification after first A statement',r"""¤¤$§hat{A}$ is abelian''. surely not! You mean""",r"""¤¤$§hat{A}$ is abelian''. surely not! You mean""",True,'high','The words surely not!, capital You, and mean are independently legible in the upper half. The note proposes the second indexed A, without supplying definitions.',a,[409,245,1208,326])
doubt('p.431, integration comment',r"""¤¤integration'' is not clear""",r"""¤¤integration'' is not clear""",True,'high','The quoted integration and the following is not clear are legible. No period is added after clear.',a,[387,441,920,499])

remaining=[
dict(place='p 428 l.6 opener',reading=tx(r'§unsure{¤¤|¤}'),alternatives='double opener / single opener',confidence='medium',reason='Connected limbs do not decide original stroke count.'),
dict(place='p 428 second hatted A index',reading=tx(r'§unsure{M|m}'),alternatives='M / m',confidence='medium',reason='Angular small cursive form does not securely decide case.'),
dict(place='p 440 terminal segment and cross',reading=tx(r'§unsure{-+|+}'),alternatives='minus plus / plus with preceding quotation return',confidence='medium',reason='The horizontal segment is joined to the closing quotation stroke.'),
dict(place='p 441 l.3 opener',reading=tx(r'§unsure{¤|¤¤}'),alternatives='single opener / fused double opener',confidence='medium',reason='Short upper-right spur joins the main hook.'),
dict(place='p 449 baseline cancelled loop',reading=tx(r'§deleted{§unsure{o}}'),alternatives='old o / loop belonging to the correction connector',confidence='low',reason='Letter and connector traces occupy the same small physical area.'),
dict(place='p 452 low point',reading=tx(dot452),alternatives='punctuation point / unassigned isolated mark',confidence='medium',reason='The dot is certain but its function and origin are not.'),
dict(place='p 455 under first i',reading=tx(r'§unsure{§mathrm{E}|§equiv}'),alternatives='E-shaped mark / equivalence-like emphasis mark',confidence='medium',reason='Three levels are joined at the left; their meaning remains undetermined.'),
dict(place='p.466 old reference',reading=tx(r'§deleted{§unsure{l§textsubscript{9}|l}}'),alternatives='l with a much lower 9 / l with cancellation remnant',confidence='low',reason='The small lower hook and loop are crossed and can be part of the cancellation.'),
dict(place='p 468 terminal closer',reading=tx(r"§unsure{''|'}"),alternatives='fused double closer / single hooked closer',confidence='medium',reason='Two low legs remain joined in a compact upper body.'),
dict(place='Right rule, pale low continuation',reading=tx(right_rule),alternatives='pale continuation of the rule / separate surface trace on its axis',confidence='medium',reason='The lower pale trace is preserved separately across the observed gap; no continuous joining path is invented.'),
dict(place='Isolated points and short marks itemized in the drawing inventory',reading='Geometric TikZ marks in reading.tex',alternatives='ink specks or incidental marks / other unassigned dark surface features',confidence='medium',reason='No letter, punctuation value or intentional editorial function is assigned merely from a point being dark.')
]

# Ordered inventory: whole-page rules first, then top-to-bottom entries;
# nested physical states immediately follow their parent entry.
inventory=[]
def inv(kind,position,objects,hand='his hand'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=f'{len(inventory)+1:03d}',kind=kind,position=position,first_words_or_objects=tx(objects),transcribed='yes'))
inv('drawing','Whole list, between page-number and correction columns','Left vertical rule; darker upper part and fading tail to physical lower edge')
inv('drawing','Whole list, right side and through the longest entries','Right vertical rule; fading tail, gap, and separate pale low trace')
inv('text','Top line, left entry; p426 l-16','p.426 l-16 its')
inv("text","Top line, second entry; p426 l-4",r"""l-4 ¤¤ones''""")
inv('text','Second line; p427 l-6','p 427 l-6 its')
inv('drawing','Left margin at p427 level','One small separate dark point')
inv("text","p428 first line, left entry",r"""l.6, §unsure{¤¤|¤}allows one to''""")
inv('text','p428 first line, right entry','l-9 wed better')
inv('drawing','Above p428 first-line l-9 reference','Four points, in two separated small groups')
inv('text','p428 second line','l-9 hatted A is abelian. surely not! You mean indexed hatted A')
inv('text','p429 line','p.429 l.1. dont')
inv('text','p430 left entry','l 16 its')
inv('text','p430 middle entry','l.17. doesnt')
inv('text','p430 right entry','l-3 weve')
inv('text','p431 line','l.-8 integration is not clear')
inv('text','p434 left entry','l 12 interpret')
inv('text','p434 right entry','l-12 makes sense')
inv('drawing','Blank area above-right of p434 final quoted span','Separate small dark point')
inv('text','p438 line','l 4 ) missing from formula.')
inv('text','p439 left entry','l-9 developed')
inv('text','p439 middle entry','l-1 make sense')
inv('text','p439 right entry','l 12 divided')
inv('text','p440 first line, left entry','l.-7 wouldnt')
inv('text','p440 first cancelled entry','Old l-5 its proposal with live single opener and paired closer')
inv('deletion','Within p440 first cancelled entry','l-5')
inv('deletion','Within p440 first cancelled entry','its; quotation marks outside cancellation')
inv('text','p440 second cancelled entry','allows one to with live paired quotation and terminal doubtful segment/cross')
inv('deletion','Within p440 second cancelled entry','allows one to; quotation marks outside cancellation')
inv('text','p440 second line','l-5 its diagonal map would allow one to recover')
inv('text','p441 left entry','l.3 dont')
inv('drawing','Above the n/apostrophe area of p441 dont','Small detached point')
inv('text','p441 second entry','l 7 divided')
inv('text','p441 third entry','l 16 divided')
inv('text','p441 right entry, across the right rule','l-10 allows one to')
inv('text','p444 line','l-9 isnt')
inv('text','p445 left entry','l 1 trying to put')
inv('text','p445 right entry','l-4 doesnt')
inv('text','p447 left entry','l 10 commute with')
inv('text','p447 middle entry','l 18 One way to define')
inv('text','p447 right cancelled entry','l 9 its, paired quote edges live')
inv('deletion','Within p447 cancelled entry','l 9')
inv('deletion','Within p447 cancelled entry','its')
inv('drawing','Above-left of p447 cancelled opener','One extra point, distinct from the i dot')
inv('drawing','Far right sheet edge at p447 level','One tiny dark point')
inv('text','p448 line','l-6 its also l 9.')
inv('text','p449 first line, left correction','l 11 allows old loop, raised one, us to')
inv('deletion','p449 baseline between allows and us',r'§unsure{o}')
inv('insertion','p449 above the gap between allows and us','Raised one, attached by the observed curved connector')
inv('deletion','Within p449 raised insertion','one')
inv('drawing','p449 around the baseline loop and raised insertion','Curved connector above the loop and continuation below the baseline')
inv('text','p449 first line, right entry','l-9 To imagine that there is a good')
inv('text','p449 continuation line','l-8 without the homotopy groups being k-modules')
inv('text','p450 left entry','l 2 from the ring.')
inv('text','Within p450 from the ring','Single underline confined to the')
inv('text','p450 middle entry','l-10 divided')
inv('text','p450 right entry','l with lowered s -2 & -3 doesnt')
inv('text','p452 line','l-11 low point dont')
inv('drawing','p452 between opening pair and d','Low point, without an assigned punctuation function')
inv('drawing','Blank area to right of p452 line','One larger and one much smaller separated point')
inv('text','p453 line','l 1 isnt')
inv('text','p454 line','l.11 we had better')
inv('text','p455 line','l-13 divided')
inv('drawing','Directly beneath first i of divided, above the next line','E-shaped/equivalence-like three-level mark')
inv('text','p456 left entry','l.2 its')
inv('drawing','Below/right of p456 l.2','Small upper point, irregular dark body, and smaller lower point')
inv('text','p456 right entry','l 9 dont')
inv('drawing','Blank area right of p456 line','One separate small dark point')
inv('text','p457 line','l-16 its')
inv('text','p458 first entry','l 8 wouldnt')
inv('text','p458 second entry','l 14 doesnt')
inv('text','p458 same-reference continuation','also its')
inv('text','p458 third reference','l 15 its')
inv('text','p458 fourth reference','l 16 its')
inv('text','p459 line','l-5 doesnt')
inv('text','p460 left entry','l 8 quasi-isomorphisms')
inv('text','p460 middle entry','l-11 demand')
inv('text','p460 right entry','l-7 mimic')
inv('text','p462 first entry','l 9 isnt')
inv('text','p462 second entry','l 14 its')
inv('text','p462 third entry','l-7 dont')
inv('text','p462 fourth entry','l-6 didnt')
inv('text','p462 rightmost entry','l-4 dont')
inv('text','p462 separate continuation line','l-1 mimic')
inv('drawing','Right blank area level with p462 continuation','Two separated oblique points')
inv('text','p463 left entry','l 12 doesnt')
inv('text','p463 right entry','l 13 trivial')
inv('text','p466 line','Old reference, stop, l-9 enters')
inv('deletion','p466 before the live l-9',r'§unsure{l§textsubscript{9}|l}')
inv('drawing','Below p466 live l, left of next-line opener','Small separate point')
inv('text','467 left entry; no p prefix','l 8 quasi-isomorphism')
inv('text','467 right entry','l-1 its')
inv('text','p468 first entry','l 3 Postnikovs, closing pair and period')
inv('text','p468 second entry','l 7 this only taking')
inv('text','p468 last entry','l.8 and iterating, doubtful terminal quotation count')
inv('drawing','Around p468 l.8 reference','Low dark point and paler high round mark with short right tail')
inv('margin note','Bottom-right corner, below main text','31; archive number recorded only as a comment','another unnamed hand')

report=dict(
 scan=32,reader='A',model='GPT-6 Astra Pro (inherited)',effort='not exposed',
 viewed=[w,a,b],
 layout='One handwritten correction list on a light sheet with a dark photographic border. Page references 426 through 468 form a narrow left column; corrections extend across the right column, with continuation lines at 428, 440, 449 and 462. A thin vertical rule separates the page references from the wording, and a second runs near the right side through the longest entries. Both rules have darker upper portions and pale lower traces; the right low trace is kept separate across a gap. The text is in one principal hand. Two proposals at 440, one at 447, the raised one and possible baseline old o at 449, and the old reference at 466 are cancelled. There is a visible raised insertion/connector at 449, a single underline beneath the at 450, and a separate three-level mark under the first i at 455. Distinct isolated dark points are itemized. Circular surface impressions at upper right and near the lower-right margin, pale horizontal surface traces, and the sheet border are material/photographic features rather than transcribed ink drawings. The lighter archive 31 is a corner annotation and is kept as a comment. There are no displayed mathematical derivations or arrow diagrams.',
 changes=changes,c_doubts=c_doubts,remaining_doubts=remaining,inventory=inventory,
 notes=[
 'The correction list covers cited pages 426–468; the archive corner number is 31.',
 'At p428 l-9 the writer quotes hatted A is abelian, responds surely not!, and proposes a second hatted A with a doubtful M/m index. At p431 integration is said to be not clear.',
 'At p438 l4 a single closing parenthesis is identified as missing from formula. The cited formula is not reproduced on this sheet.',
 'At p440 the cancelled proposals are followed by its diagonal map would allow one to recover. At p449 the live wording reads allows us to, and another entry reads without the homotopy groups being k-modules.',
 'The at p450 is singly underlined. A separate three-level mark lies under the first i of divided at p455; its identity remains uncertain.',
 'Most other entries are wording or spelling corrections, including quasi-isomorphisms, quasi-isomorphism, divided, mimic and Postnikovs. Apostrophe and quote positions are retained as read, with local uncertainties explicitly marked.'
 ],
 math_checks=[],
 notation=[
  dict(sign=tx(r'§hat{A}'),location='p428 both formula occurrences',reading=tx(r'§hat{A}; §hat{A}_{§unsure{M|m}}'),evidence='Half a and crop04: ordinary A contours, distinct roofs, and an angular lower-right index of unresolved case.'),
  dict(sign=')',location='p438 l4',reading=')',evidence='Half a shows a single closing curve and no matching opener at that place.'),
  dict(sign='k-',location='p449 l-8',reading=tx(r'$k$-modules'),evidence='Half b shows the lowercase ascender and diagonal limbs, followed by a short hyphen.'),
  dict(sign=tx(r'l§textsubscript{s}'),location='p450 final reference',reading=tx(r'l§textsubscript{s}-2 §& -3'),evidence='Crop11: small lowered s, separate minuses, and a two-loop crossed ampersand.'),
  dict(sign=tx(r'§unsure{§mathrm{E}|§equiv}'),location='p455 under first i',reading=tx(r'§underset{§unsure{§mathrm{E}|§equiv}}{§text{i}}'),evidence='Crop13: three short levels with an inked left join; independent of the following line closer.'),
  dict(sign="quotation strokes and cancellation edges",location="p428, p440, p441, p447, 467, p468",reading=tx(r"""Local §unsure{¤¤|¤}, §unsure{¤|¤¤}, and §unsure{''|'} readings; quote edges at 440 and447 remain live"""),evidence="Crops02,05,06,07,08,16,17,18 were inspected separately. Paired 467 and p468 openers are confirmed; compact disputed groups are not normalized by analogy."),
  dict(sign=tx(r'§uline{the}'),location='p450 l2',reading=tx(r'§uline{the}'),evidence='Crop10 shows one heavy horizontal rule confined to the, without a separate second underline.'),
  dict(sign='isolated dark points and narrow vertical rules',location='Locations separately itemized in the inventory and changes',reading='Anchored TikZ in reading.tex',evidence='Both halves and the listed local crops establish distinct geometry. No punctuation or editorial function is assigned to isolated marks.')
 ],
 abbreviations=[
  dict(form='p / p.',expansion='page (tentative list interpretation only)',place='Page references throughout; no p before 467'),
  dict(form='l / l.',expansion='line (tentative list interpretation only)',place='Correction references throughout; punctuation retained locally'),
  dict(form=tx(r'l§textsubscript{s}'),expansion='lines (tentative plural interpretation only)',place='p450 final reference')
 ],
 brief_feedback='No H_context.md or C_context_addendum.md was supplied for this input. H status is desc, so there are no H comparison rows and every h field is null. The whole image was viewed once for layout and each supplied half once line by line. Nineteen unresolved loci were frozen before crop generation; all nineteen enhanced crops were individually displayed once, and no whole/half was reopened. The seven explicit C uncertainty macros and six additional supplied context decisions are all recorded in c_doubts. Inventory order is top-to-bottom and left-to-right, with the two page-spanning rules first and nested insertion/deletion/drawing states immediately following their parent entry. There are no true displayed formulas or diagrams. The cotefile wrapper is supplied as required metadata, not counted as an ink change. No OCR, outside research, other reader output, other page image, compilation or mathematical proof checking was used.'
)

# Inventory locators use the literal contraction spellings.
contractions={'dont':'don'+chr(39)+'t','doesnt':'doesn'+chr(39)+'t','isnt':'isn'+chr(39)+'t','didnt':'didn'+chr(39)+'t','wouldnt':'wouldn'+chr(39)+'t','weve':'we'+chr(39)+'ve','wed':'we'+chr(39)+'d','Postnikovs':'Postnikov'+chr(39)+'s'}
for row in inventory:
    for before,after in contractions.items():
        row['first_words_or_objects']=re.sub(r'\\b'+before+r'\\b',after,row['first_words_or_objects'])
report['notes']=[x.replace('Postnikovs','Postnikov'+chr(39)+'s') for x in report['notes']]
outcomes=[
 'Confirmed l-4, not l-6, and two opening/closing strokes around ones; literal C retained.',
 'Opening count remains double/single; closing pair confirmed.',
 'Closing pair of wed better confirmed; four distinct points above the reference preserved.',
 'Ordinary hatted A and paired edges confirmed; M/m index case remains uncertain.',
 'Reference and its cancelled; opening single and closing pair remain live outside the cancellation.',
 'Words cancelled; quote edges live; terminal minus-plus/plus doubt retained.',
 'Opening single/double count remains uncertain; separate high point preserved.',
 'Reference and its cancelled; both quote pairs live; additional point above-left of opener preserved.',
 'Raised cancelled one, baseline uncertain o and the correction connector are recorded at their physical heights.',
 'One heavy underline confined to the; C single underline confirmed.',
 'Lowered s confirmed; linking sign resolved as ampersand.',
 'Low point confirmed geometrically; punctuation role unassigned.',
 'E-shape preferred over equivalence shape; mark remains under first i and independent of the next line quote.',
 'Three dark separated bodies around/below the reference preserved; ordinary abbreviation point not duplicated.',
 'Old tall loop and lower hooked remnant remain l-plus-low9/l uncertain; separate lower point preserved.',
 'Two joined opening strokes and separate closing pair around its confirmed; C retained.',
 'Two opening strokes after l.8 confirmed; separate low point and paler high mark with short tail preserved.',
 'Terminal double/single quotation remains uncertain; right rule fade and separate lower pale trace recorded.',
 'Left rule fades continuously to the physical sheet edge; no extent beyond that edge is inferred.'
]
frozen=json.loads((root/'frozen_loci.json').read_text())
report['crop_decisions']=[dict(id=z['id'],crop=z['crop'],source=z['source'],bbox=z['bbox'],outcome=o) for z,o in zip(frozen['loci'],outcomes)]

(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(root/'literal_diff.txt').write_text(''.join(difflib.unified_diff(C.splitlines(True),s.splitlines(True),fromfile='C.tex',tofile='A/reading.tex')))

# Static-only checks, with no TeX execution.
stack=[]
for i,ch in enumerate(s):
    if ch in '{}':
        n=0;j=i-1
        while j>=0 and s[j]==chr(92): n+=1;j-=1
        if n%2: continue
        if ch=='{': stack.append(i)
        elif not stack: raise ValueError('Unmatched closing brace at '+str(i))
        else: stack.pop()
if stack: raise ValueError('Unmatched opening braces')
for env in ('tikzpicture','scope'):
    if s.count(tx('§begin{'+env+'}')) != s.count(tx('§end{'+env+'}')): raise ValueError('Environment imbalance: '+env)
if '§' in s or '¤' in s: raise ValueError('Unconverted placeholder')
if s.count(tx('§cotefile{109}'))!=1: raise ValueError('Cote wrapper count')
if s.count('$')%2: raise ValueError('Unbalanced math dollar count')
loaded=json.loads((root/'report.json').read_text())
if sum(x['explicit_c'] for x in loaded['c_doubts'])!=7: raise ValueError('Explicit C doubt coverage')
if len(json.loads((root/'crop_views.json').read_text()))!=19: raise ValueError('Crop view coverage')
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'explicit_c_doubts':sum(x['explicit_c'] for x in c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'crops':19,'math_checks':0,'static_braces':'balanced','reading_lines':len(s.splitlines())}))
