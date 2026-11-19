from work import *
from record_helpers import *
n=10;s=ctext(n).replace('\\cotefile{156-5}\n','')
s=s.replace(r'\Phi',r'\mathscr{L}')
s=s.replace(r'$\mathscr{L}$',r'$\unsure{\mathscr{L}|\Phi}$',1)
for a,b in [(r'\unsure{fermé|fermée}','fermé'),(r'\unsure{vient|reste}','vient'),(r'\uline{Corollaire 1}',r'\uline{Corollaire \unsure{1|!}}'),(r'\unsure{impliquer}','impliquer'),(r'\unsure{ens.}','ens.'),(r'\unsure{sss|ssi}','sss')]:
 assert a in s,a;s=s.replace(a,b)
r={'changes':[
D('recurring family sign','Phi throughout','fraktur L','scr L; first occurrence unsure scr L|Phi','010_top.jpg compared with 009_bottom.jpg and 008_top.jpg: same closed loop on upright with horizontal foot continues the same proof. Encoding harmonized, glyph identification still marked.',True,False,'misread symbol or index','medium',consequential='Harmonizes C’s folder-boundary switch from L to Phi without treating the typeface as settled ink.'),
D('page opening','en question','les B en question','en question','010_top.jpg: only en question at top; les B en ends scan009.',False,True,'text not on the page'),
D('closed adjective','unsure fermé|fermée','fermé','fermé','010_top.jpg: final accented e without additional e.',True),
D('parenthesis','et itou; fermé dans','unsure itou; fermé de','et itou; fermé dans','010_top.jpg: et before itou; full dans before union.',False,True,'omission','high',marked_h='yes'),
D('transition','unsure vient|reste','reste','vient','010_top.jpg: low v start and nt ending; no r-s sequence.',True,True,'misread word'),
D('2 degree family overwrite','deleted unsure Psi before Phi','clean L','deleted unsure Psi before L','010_top.jpg: upper horizontal stroke and doubled loop from older sign beneath live glyph.',False,True,'omission','medium'),
D('B subset A overwrite','deleted unsure B beneath A','A only','deleted unsure B beneath A','010_top.jpg: lower loop underneath triangular A.',False,True,'omission','medium'),
D('B membership conclusion overwrite','deleted B beneath Phi','L only','deleted B beneath L','010_top.jpg: clear B lobes under looped family letter.',False,True,'omission'),
D('Mais clause verb','on aura','on a','on aura','010_top.jpg: connected aura, including final short a after r.',False,True,'misread word'),
D('Mais clause crossed start','deleted unsure |B|','deleted ill','deleted unsure |B|','010_top.jpg: B and vertical bounding strokes under crossed lines.',False,True,'readable ink left as \\ill{}','medium',marked_h='yes'),
D('last implication corrections','old subset and Phi beneath in and Psi','clean B in Psi','old subset and family sign beneath in and Psi','010_top.jpg: thick doubled membership curve and old loop under forked Psi.',False,True,'omission','medium'),
D('definition heading accent','unsure Définition|Definition','Définition','unsure Définition|Definition','010_corollary.jpg: compressed heading; small mark over first e not securely separated from pen lift.',False,True,'other','medium'),
D('definition final point','none','period','none','010_corollary.jpg: no distinct point after underlined compatibles.',False,True,'text not on the page'),
D('first corollary label','1','!','unsure 1|!','010_corollary.jpg: straight upright with lower underline segment; no secure numeral hook or separate exclamation dot.',True,True,'misread symbol or index','medium'),
D('support overwrite','deleted A beneath Phi','L only','deleted A beneath L','010_corollary.jpg: triangular A plainly under loop.',False,True,'omission'),
D('second ambient set','partie de Psi','partie de |Psi|','partie de Psi','010_corollary.jpg: bare Psi, no support bars.',False,True,'misread symbol or index',consequential='Preserves the bare Psi in the corollary rather than H’s supplied support bars.'),
D('relation noun','unsure équivalence|équilence','équiv.','unsure équivalence|équilence','010_corollary.jpg: split word continues lence next line; cannot safely regularize internal spelling.',False,True,'abbreviation expanded or spelling modernised','medium'),
D('relation support correction','deleted unsure B beneath family','L only','deleted unsure B beneath family','010_corollary.jpg: doubled older lobes inside support.',False,True,'omission','medium'),
D('same relations shorthand','=s','mêmes','=s','010_corollary.jpg: parallel bars followed by small s.',False,True,'abbreviation expanded or spelling modernised'),
D('impliquer','unsure impliquer','impliquer','impliquer','010_example.jpg: i then mp-l-i-q-u-er trace readable.',True),
D('nullement','nullement','unsure nullement','nullement','010_example.jpg: n/u, double l loops and final ment visible.',False,True,'other','high',marked_h='yes'),
D('example shorthand','ont = support; la = relation','ont même support; la même relation','ont = support; la = relation','010_example.jpg: explicit equals bars at both places.',False,True,'abbreviation expanded or spelling modernised'),
D('sets abbreviation','unsure ens.','ens.','ens.','010_example.jpg: ens with terminal point.',True),
D('cancelled order statement','n’est la = que si','c’est la même que si','n’est la = que si','010_foot.jpg: n apostrophe before est; two bars after la.',False,True,'misread word'),
D('final biconditional shorthand','unsure sss|ssi; sss','ssi; ssi','sss; sss','010_foot.jpg: three similar joined s loops in each occurrence; no dotted i.',True,True,'abbreviation expanded or spelling modernised')],
'doubt_decisions':['Resolved fermé, vient, impliquer, ens., and sss. Added first-occurrence family-glyph doubt during cross-folder harmonization and 1/! doubt in the first corollary label. Retained Définition accent uncertainty, split équivalence/équilence spelling, and all overwritten letters/signs. The repeated cotefile marker is removed from this fragment as required for the single combined transcription; this structural edit is not counted as an ink reading.'],
'unresolved':['First corollary label 1/!; exact family-glyph typography; split noun spelling and old correction layers.'],
'doubts':[Q('family glyph','scr L','Phi'),Q('2 degree old glyphs','Psi; B'),Q('crossed start','|B|'),Q('implication old signs','subset; family sign'),Q('heading','Définition','Definition'),Q('corollary label','1','!'),Q('relation noun','équivalence','équilence'),Q('support old glyph','B')],
'inventory':[E('text','header','page 9; en question sont dans family'),E('text','top continuation','closedness reduces remaining proof'),E('display','2 degree','A in L, B in Psi, B subset A implies B in L'),E('deletion','display','old Psi; B beneath A; B beneath family'),E('text','proof conclusion','Mais on aura … OK'),E('deletion','proof conclusion','old |B|; subset; family under Psi'),E('text','definition','On dit alors … compatibles'),E('text','first corollary','saturation and induced equivalence relations'),E('deletion','corollary support','old A and B'),E('text','warning/example','condition insufficient; stratum family L°'),E('insertion','example','L°'),E('deletion','example explanation','car'),E('deletion','foot before corollary','car la relation d’ordre … n’est la = que si'),E('text','second corollary','support inclusion/equality iff family inclusion/equality')]
}
notn=json.loads((OUT/'records/notation.json').read_text());notn.append(['C folder-boundary Phi/L switch','The same closed-loop, stem-and-foot family sign is encoded consistently as \\mathscr{L}; first occurrence retains \\unsure{\\mathscr{L}|\\Phi}. No inference from context.','009 bottom → 010 top; 010 all bands']);(OUT/'records/notation.json').write_text(json.dumps(notn,ensure_ascii=False,indent=2)+'\n')
save(n,s,r)
