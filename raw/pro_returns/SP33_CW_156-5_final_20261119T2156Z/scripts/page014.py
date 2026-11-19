from work import *
from record_helpers import *
n=14;s=ctext(n).replace(r'\Phi',r'\mathscr{L}')
s=s.replace(r'$\mathscr{L}\unsure',r'$\unsure{\mathscr{L}|\Phi}\unsure',1)
for a,b in [(r'\unsure{la|le}','le'),(r'\unsure{cardi}','cardi'),(r'\unsure{\subset|\in}',r'\subset'),(r'\unsure{que|pour}','pour'),(r'\unsure{compatible|compatibles}','compatible')]:assert a in s,a;s=s.replace(a,b)
r={'changes':[
D('family convention','Phi','fraktur L','scr L with first unsure L|Phi','014_middle.jpg: looped family glyph with foot.',True,False,'misread symbol or index','medium'),
D('opening shorthand','= comp.','même comp.','= comp.','014_top.jpg: two bars at start.',False,True,'abbreviation expanded or spelling modernised'),
D('article and object name','unsure la|le multistrate','la multiplicité','le multistrate','014_top.jpg: l then open e loop; strates letter sequence.',True,True,'misread word'),
D('cancelled card abbreviation','unsure cardi','cardinal','cardi','014_top.jpg: c-a-r-d-i with final dot over short stem; no nal.',True,True,'abbreviation expanded or spelling modernised'),
D('power-set alphabet','unsure cal P|frak P','frak P','unsure cal P|frak P','014_top.jpg: large P has horizontal crossed-loop lower curve, not safely one named typeface.',False,False,'other','medium'),
D('containment sign','unsure subset|in','subset','subset','014_middle.jpg: thick c-shaped mark without middle membership bar.',True,False,'misread symbol or index'),
D('first crossed relative clause','qui sont unsure des sont que','qui sont dans','qui sont unsure des sont que','014_middle.jpg: two sont-shaped groups separated by short d/e/s-like group; trailing que crossed.',False,True,'omission','medium'),
D('telles insertion','inserted telles','live baseline telles','inserted telles','014_middle.jpg: word above crossed line, replacement at its right end.',False,True,'insertion or placement'),
D('second crossed clause','old unsure {family} qui ne contiennent pas emptyset','ill ne contiennent pas emptyset','old unsure {family} qui ne contiennent pas emptyset','014_middle.jpg: brace/loop crossed at far left, surviving qui before ne.',False,True,'readable ink left as \\ill{}','medium',marked_h='yes'),
D('live connector','unsure que|pour','que','pour','014_middle.jpg: long descending p stem and joined our run.',True,True,'misread word'),
D('M singleton placement','inline with following a un seul élément','display isolated','inline with following a un seul élément','014_middle.jpg: one continuous baseline across full width.',False,True,'insertion or placement'),
D('Prop punctuation','underlined Prop','Prop.','underlined Prop','014_prop.jpg: no terminal stop.',False,True,'abbreviation expanded or spelling modernised'),
D('old Card beneath L','deleted unsure Card','omitted','deleted unsure Card','014_prop.jpg: short old word under overlaid L.',False,True,'omission','medium'),
D('old symbol beneath X','deleted unsure Y|F','clean X','deleted unsure Y|F','014_prop.jpg: extra vertical and transverse remnants beneath X.',False,True,'omission','medium'),
D('component clause','tous dans la =','dans une même','tous dans la =','014_prop.jpg: tous at left then dans la and two bars.',False,True,'misread word'),
D('restriction opening','si on se borne','si l’on se borne','si on se borne','014_bottom.jpg: no extra l/apostrophe before on.',False,True,'text not on the page'),
D('finite figures term','figures ensemblistes finies','figures [added ou] multiplicités finies','figures ensemblistes finies','014_bottom.jpg: ensemblistes begins next line; no ou addition.',False,True,'misread word',consequential='Restores figures ensemblistes in the finite restriction, without H’s added “ou multiplicités”.'),
D('parenthetical reservation','ce qui n’offre pas d’inconvénient à mes yeux','ce qui unsure suffira, unsure j’imagine','ce qui n’offre pas d’inconvénient à mes yeux','014_bottom.jpg: n’offre, pas, d’inconvénient, à mes yeux fully legible over two lines.',False,True,'misread word',marked_h='yes'),
D('after parenthesis','M est connexe','M ill est connexe','M est connexe','014_bottom.jpg: no intervening writing between M and est.',False,True,'text not on the page',marked_h='yes'),
D('compatibility adjective','unsure compatible|compatibles','compatibles','compatible','014_bottom.jpg: open e followed by closing parenthesis; no distinct s.',True,True,'abbreviation expanded or spelling modernised'),
D('S SA21-K5-01, ink portion','connectedness and C4 automatique','same conclusion','same conclusion, with literal braces and ≥1','014_top.jpg/014_prop.jpg/014_bottom.jpg: braces, ≥1, and automatique are written; no retraction on this page. Mathematical status deferred.',False,False,'other',id='SA21-K5-01/014')],
'doubt_decisions':['Resolved le, cardi, subset, pour, compatible. Retained P alphabet in crossed line; des, old {family}, old Card, old Y/F. S SA21-K5-01 confirmed as a description of the ink-level assertion, without yet adopting its mathematical verdict.'],
'unresolved':['Overwritten old family/Card/Y/F; short des in crossed clause; named typeface of cancelled power-set symbol.'],
'doubts':[Q('family','scr L','Phi'),Q('cancelled power set','cal P','frak P'),Q('crossed clause','des'),Q('crossed old object','{family}'),Q('old word','Card'),Q('old symbol','Y','F')],
'inventory':[E('text','opening','same component via multistrate'),E('display','upper','{{{x}},{L minus {x}}}'),E('text','empty case','Si L=emptyset'),E('deletion','empty case','de card.1; P(L) est de cardi'),E('text','singleton case','Card L=1; P(L)={emptyset,L}'),E('deletion','singleton case','qui sont des sont que; {family} qui ne contiennent pas emptyset'),E('insertion','singleton case','telles'),E('text','singleton conclusion','pour emptyset notin family; M={{L}}'),E('text','transition','Donc'),E('text','proposition','card L≤1; card L≥1; minimal elements'),E('deletion','proposition','Card; Y/F'),E('text','finite restriction','figures ensemblistes finies'),E('deletion','finite restriction','familles'),E('text','final claim','C4 decomposition automatic'),E('deletion','final claim','est ici de')]
}
save(n,s,r)
