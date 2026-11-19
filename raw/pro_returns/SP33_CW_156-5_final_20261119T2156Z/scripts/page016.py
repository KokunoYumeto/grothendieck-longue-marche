from work import *
from record_helpers import *
n=16;s=ctext(n)
for a,b in [(r'\unsure{de|dans}','de'),(r'\unsure{sss|ssi}','sss'),(r'\unsure{notion|relation}','notion')]:assert a in s,a;s=s.replace(a,b)
s=s.replace('% Paper watermark, sideways, partial impressions: RONG / EXTRA STR…',r'''% Paper watermark; sideways and faint; partial impressions, not manuscript prose.
\margin{\unsure{RONG}\quad\unsure{EXTRA STR}}''')
r={'changes':[
D('heading','Supports et cosupports.','Supports et complément.','Supports et cosupports.','016_top.jpg: second word repeats support letter forms with co prefix and final s.',False,True,'misread word',consequential='Restores the heading “Supports et cosupports.”'),
D('opening preposition','unsure de|dans','dans','de','016_top.jpg: small looped d then single low e stroke; no ans.',True,True,'misread word'),
D('figure alphabet','unsure cal F|scr F','frak F','unsure cal F|scr F','016_top.jpg: long top bar and curved lower foot of F; alphabet name remains conventional.',False,False,'other','medium'),
D('order qualification','inserted au sens de leq','plain parenthesis','inserted au sens de leq','016_top.jpg: curved insertion leader starts after disjoints and reaches phrase above.',False,True,'insertion or placement'),
D('iff abbreviation','unsure sss|ssi','ssi','sss','016_top.jpg: three linked small s strokes, no final dotted i.',True,True,'abbreviation expanded or spelling modernised'),
D('relative predicate','celles qui deleted sont satisfont','celles qui sont deleted sont telles que','celles qui deleted sont satisfont','016_top.jpg: one crossed sont only, followed by sat…font joined word.',False,True,'misread word'),
D('transition','on voit que','unsure moyennant que','on voit que','016_top.jpg: separate on and voit with visible final t; not one word.',False,True,'misread word',marked_h='yes'),
D('first conceptual noun','unsure relation|notion','notion','unsure relation|notion','016_middle.jpg: low first strokes and medial tall stroke could encode relation or notion; retained.',False,True,'misread word','medium'),
D('second conceptual noun','unsure notion|relation','notion','notion','016_middle.jpg: n, tall t and short ending ion; no medial l.',True,False,'misread word'),
D('crossed opening lower paragraph','Le F(Lprime without closing parenthesis','Les F(Lprime) with close','Le F(Lprime without closing parenthesis','016_bottom.jpg: singular Le; no closing curve after prime before end of deletion line.',False,True,'misread symbol or index'),
D('ens abbreviation','L’ens','L’ens.','L’ens','016_bottom.jpg: no stop after final s.',False,True,'abbreviation expanded or spelling modernised'),
D('de Lprime insertion attachment','after figures, before de support','after crossed est','after figures, before de support','016_bottom.jpg: insertion written directly above interval between figures and de support.',False,True,'insertion or placement'),
D('paper watermark','comment-only partial RONG / EXTRA STR','omitted','doubtful partial RONG; EXTRA STR in margin encoding','016_watermark.jpg and 016_watermark_upright.jpg: very faint impressed block letters, partial repeated wording. These are paper marks, not authorial prose.',True,True,'omission','low')],
'doubt_decisions':['Resolved de, sss and the second notion. Retained first relation/notion and calligraphic F alphabet. Added explicitly doubtful partial paper-watermark letters to visible text instead of leaving them only in a comment.'],
'unresolved':['First relation/notion; exact typeface convention; partial faint watermark letters.'],
'doubts':[Q('figure alphabet','cal F','scr F'),Q('complementarity noun','relation','notion'),Q('watermark partial impressions','RONG; EXTRA STR','','low','Faint paper impressions, not ink; fragmentary rather than completed from a brand name.')],
'inventory':[E('text','heading','Supports et cosupports.'),E('text','first paragraph','disjoint figures and supports'),E('insertion','upper right','au sens de leq'),E('display','upper inline','|F| cap |G|=emptyset'),E('deletion','relative clause','sont'),E('display','upper middle inline','Lprime=L minus union_i |G_i|'),E('text','middle','supports and arbitrary subsets; complementarity'),E('deletion','lower opening','Le F(Lprime'),E('text','lower paragraph','figures of support subset Lprime'),E('insertion','lower above line','de Lprime'),E('deletion','lower right','est'),E('display','lower inline','F(Lprime) subset F(L)'),E('text','last lines','sous-ens. saturés; leq and disjonction'),dict(kind='text',position='lower right sideways paper watermark',text='partial doubtful RONG / EXTRA STR',hand='paper watermark')]
}
save(n,s,r)
