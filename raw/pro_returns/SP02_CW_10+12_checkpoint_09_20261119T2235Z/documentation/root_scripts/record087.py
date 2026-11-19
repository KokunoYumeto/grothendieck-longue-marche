import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-06',10,87,kind='reused_typed');ch=r.change
src=Path('source/SP02_CW_10+12_witnesses/codex/B10-06/pages/B10-06_10_scan087.tex').read_text()
old=src[src.index(r'\handwritten{\diagram{\(\begin{array}{ll}'):src.index('\n\n\\handwritten{\\diagram{\\(\\begin{array}{lcl}')]
new=r'''\handwritten{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.25pt] (-.17,.6)--(-.19,.27);
\draw[line width=.25pt] (-.2,.2)--(-.22,-.28);
\draw[line width=.25pt] (-.22,-.35)--(-.24,-.92);
\draw[line width=.25pt] (-.24,-1) .. controls (-.25,-1.25) and (-.16,-1.35) .. (.06,-1.47);
\fill (-.8,.1) circle (.018cm);
\draw[thin] (.93,.48)--(.94,.62);
\node[anchor=base west] at (0,0) {$A_n,\ A_n^{\unsure{\mathrm{ad}|{\cdot}d|-d}},\ (A_n,d)\quad(d\mid n,\ \unsure{\rlap{$d$}t}\,\unsure{\leq}\,\unsure{d'}<n)$};
\node[anchor=base west] at (0,-.65) {$B_n,\ B_n^{\mathrm{ad}}$};
\node[anchor=base west] at (0,-1.3) {$C_n,\ C_n^{\mathrm{ad}}$};
\node[anchor=base west] at (0,-1.95) {$D_n,\ D_n^{\mathrm{ad}},\ D'_n,\ D''_n\quad(\text{si }n\text{ pair }\geq6)$};
\draw[thin] (1.7,-2.12) .. controls (1.7,-2.27) and (1.78,-2.31) .. (1.9,-2.31);
\node[anchor=base west] at (1.7,-2.58) {orth};
\node[anchor=base west] at (0,-2.85) {$E_6\quad E_6^{\mathrm{ad}}$};
\node[anchor=base west] at (0,-3.55) {$E_7,\ E_7^{\mathrm{ad}}$};
\node[anchor=base west] at (0,-4.25) {$E_8,$};
\node[anchor=base west] at (0,-4.85) {$F_4\unsure{.|,}$};
\node[anchor=base west] at (0,-5.45) {$G_2$};
\node[anchor=base west] at (9,0) {$\widetilde{A}_n,\ \widetilde{A}_n^{\mathrm{ad}},\ (\widetilde{A}_n,d)$};
\node[anchor=base west] at (9,-1.58) {$\widetilde{D}_n,\ \widetilde{D}_n^{\mathrm{ad}},\ \widetilde{D}_n^{\mathrm{orth}},$};
\node[anchor=base west] at (9,-2.43) {$\widetilde{E}_6,\ \widetilde{E}_6^{\mathrm{ad}}$};
\end{tikzpicture}}}'''
r.edit(old,new)
r.edit(r'\unsure{compacts connexes gr. de réf.|comp. et ce comme gr. de réf.|compacts connexes gr. de Lie}',r'\unsure{comp. et connexes|compacts connexes|comp. et ce comme} \unsure{gr. p\textsuperscript{r} de réf.|gr. de réf.|gr. de Lie}')
r.edit(r'\unsure{gr. p\textsuperscript{r} de réf.|gr. de réf.|gr. de Lie}.}',r'\unsure{gr. p\textsuperscript{r} de réf.|gr. de réf.|gr. de Lie.}}')
r.edit(r'\unsure{de|des}','des')
r.edit(r'\scanpage{87}',r'\scanpage{87}'+'\n'+r'\mspage{86}')
r.edit('% archive sheet number: 86','')
ch('first ad-shaped superscript','ad/dot-d/minus-d uncertain','ad','uncertainty retained','The tiny first component is a filled oval or short stroke beside a tall d; the clearer arch-shaped repetitions elsewhere support but do not force ad at this locus.','Aad; Bfull; Cfull; tildeA; tildeD; tildeE','misread symbol or index','medium',False,True,False,True)
ch('left parenthesized A parameter','shared or baseline d uncertain','shared subscript n,d','A_n,d with baseline d','The d ascender reaches the A top and its main body stands at the ordinary baseline, unlike the low short n.','Aparam','misread symbol or index','medium',True,True,False,True)
ch('first bound numeral','1','1','qualified d/t overlap; d/1 or1 alternatives in doubts','A pale left oval survives beside a dark upright with a short middle arm and lower foot; these strokes prevent an unqualified numeral reading.','Aineq; ineq-close','misread symbol or index','low',True,True,False,True)
ch('first bound relation','less than','less than or equal','qualified less than or equal; less-than alternative','A low extra stroke lies below the upper less-than arms, but the heavy overstroke merges its right end.','Aineq; ineq-close','misread symbol or index','medium',True,True,False,True)
ch('second d in bound','d','d','qualified d-prime; d alternative','A small detached upright stroke stands immediately above and right of d, before the separate less-than sign.','Aineq','misread symbol or index','medium',True,True,False,True)
ch('right parenthesized A parameter','baseline d','shared subscript n,d','baseline d','The d is full-height and separated from the lowered n by a low comma.','tildeA; Aend','misread symbol or index','high',False,True,False,True)
ch('right A-row terminal comma','comma after closing parenthesis','none','none','No foreground comma follows the closing arc; the lower gray crescent belongs to the faint mirrored typescript level.','Aend','text not on the page','high',True,False)
ch('left grouping stroke','drawn','omitted','drawn','A broken brown near-vertical line runs beside A/B/C and curves toward the D row.','writing; rowA; Bfull; Cfull; rowD','drawing or diagram','high',False,True)
ch('small isolated point left of A row','omitted','omitted','point drawn','A small black oval point sits to the far left of the A-row writing in reading orientation.','leftdot','drawing or diagram','high',True,True)
ch('short tick above A row','omitted','omitted','tick drawn','A short brown upright stroke lies above the first superscript area and is separate from the letters.','Aad','drawing or diagram','high',True,True)
ch('staggered right-column layout','tilde D aligned with C; tilde E with D','tilde D described opposite D; tilde E opposite E','staggered columns drawn','The tilde-D baseline falls between C and D, and the tilde-E baseline between D and E6. The A rows are level.','writing; rowD; rowE','drawing or diagram','high',True,True)
ch('orth label below D-prime','label and curved leader','omitted','label and curved leader','A short hooked stroke leads down from D-prime to the connected orth letters.','orth; rowD','omission','high',False,True,False,True)
ch('third tilde-D exponent','orth/orb uncertain','uncertain prime','orth','The exponent has an initial loop and r rise followed by two taller t/h strokes and a terminal shoulder; it matches the separate orth label below D-prime.','tildeD; orth','misread symbol or index','medium',True,True,True,True)
ch('tilde-D row final comma','comma','omitted','comma','A black low comma follows the third tilde-D term.','tildeD','omission','high',False,True)
ch('left E6 separator','space without comma','comma','space without comma','The gap between the two E6 terms is blank at the writing baseline.','rowE','text not on the page','high',False,True)
ch('E8 final comma','comma','omitted','comma','A distinct descending comma follows E8.','rowE8','omission','high',False,True)
ch('F4 punctuation','point/comma uncertain','point','point/comma uncertainty retained','The small brown mark has an arched upper edge but no secure surviving tail; it remains distinct from the numeral.','rowF','other','medium',False,True)
ch('cas à examiner emphasis','words underlined','unmarked','words underlined','One long line runs from beneath cas to the end of examiner;21 is outside the rule.','count','other','high',False,True)
ch('brace joining a and b','drawn','bullet list','brace drawn','A single left brace extends beside both prose lines with a middle cusp level with the count.','writing; notea; noteb','drawing or diagram','high',False,True)
ch('a-line opening','en partant des groupes','un produit illegible des groupes','en partant des groupes','The opening e-n wave and long p descender are followed by the repeated partant form, then des and the two descending stems of groupes.','notea; a-des','misread word','high',False,True)
ch('a-line compressed adjectives','three long phrase alternatives, first compacts connexes','illegible','qualified comp. et connexes with alternatives','The p descender is followed by a separate point and pale e/t-like strokes; the next compressed run begins co and has repeated low humps. Full compacts is not imposed.','comp; notea','readable ink left as \\ill{}','low',True,True,True)
ch('a-line ending abbreviations','gr. de réf. or gr. de Lie within phrase alternatives','illegible','qualified gr. p-superscript-r de réf. with alternatives','A looped abbreviation and point precede an additional descending loop with a raised short stroke; de and the tall final f with terminal point are visible. The extra compressed group remains qualified.','noteend; noteend-full','readable ink left as \\ill{}','low',True,True,True)
ch('b-line opening','en partant','un illegible','en partant','The low en wave and the long p descender, following small letters, and final triangular t match the a-line form.','noteb','readable ink left as \\ill{}','high',False,True,True)
ch('b-line before Chevalley','de/des uncertain','des','des','After the d loop, a low e wave continues into a dark terminal s-like wedge, as in des on the a-line.','bde-full; a-des','misread word','medium',True,False)
ch('horizontal rule','drawn','omitted','drawn','A long slightly wavering line spans nearly the width below the cases in reading orientation.','rule','drawing or diagram','high',False,True)
ch('two short marks beside rule','drawn','omitted','drawn','Two short thin strokes lie just beside the long line near its middle.','rule','drawing or diagram','high',False,True)
ch('isolated oblique stroke beyond rule','drawn','omitted','drawn','A short thin sloping stroke is separate from the mirrored typewriter show-through.','stray','drawing or diagram','high',False,True)
ch('folio','comment only','omitted','mspage86','The lower-left pencil figures in supplied orientation form8 and6.','folio','omission','high',True,True)
for line,read,alt,conf in [('first superscript','ad','dot-d; minus-d','medium'),('first bound numeral','d/t overlap','d/1 overlap;1','low'),('first bound relation','less than or equal','less than','medium'),('second bound d','d-prime','d','medium'),('F4 punctuation','point','comma','medium'),('a-line adjectives','comp. et connexes','compacts connexes; comp. et ce comme','low'),('a-line ending','gr. p-superscript-r de réf.','gr. de réf.; gr. de Lie','low')]:r.doubt(line,read,alt,conf)
r.notation('ad-shaped exponent','short oval/arch/dash followed by tall d; recurring ambiguity marked at first occurrence, with ad as first reading','10/087',status='qualified')
r.notation('primes in D row','single prime on D-prime and two separate short strokes on D-double-prime; no factorial','10/087')
r.notation('tilde and orth','wavy tilde above each right-column type; orth written below left D-prime and as last right-D exponent','10/087')
r.notation('A-parameter bound','heavily overwritten first bound qualified; final d has a possible raised prime','10/087',status='qualified')
r.r['inventory_overrides']={'087-004':{'first_words_or_objects':'A_n, qualified ad-shaped exponent, (A_n,d); bound numeral, relation and possible prime qualified'},'087-005':{'first_words_or_objects':'tilde A_n, tilde A_n^ad, (tilde A_n,d); no final comma'},'087-008':{'first_words_or_objects':'tilde D_n, tilde D_n^ad, tilde D_n^orth; positioned between C and D'},'087-011':{'first_words_or_objects':'tilde E6 and tilde E6^ad, positioned between D and E6'},'087-020':{'first_words_or_objects':'a) en partant des groupes; compressed comp./connexes and gr./pr/ref phrase retained qualified'},'087-021':{'first_words_or_objects':'b) en partant des Chevalley'}}
for ident,pos,txt,kind in [('leftdot','far left of A row','isolated black point','drawing'),('tick','above A superscript','short brown upright tick','drawing'),('folio','lower left in supplied orientation','86','margin note')]:r.r['inventory_extra'].append(dict(scan='10:087',sheet_kind='reused_typed',hand='unnamed hand',element='087-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/087') for a,b in [('ad','adjoint, if the small first glyph is a'),('orth','orthogonal'),('comp.','compact, provisional'),('gr.','groupe, provisional'),('p-superscript-r','pour, provisional'),('réf.','référence, provisional')]]
r.r['crops']=json.loads(Path('work/crops087.json').read_text())
r.r['inspection_note']='Whole and both halves viewed before C/H, C doubts and inventory. All34 crop recipes displayed; all upside-down foreground writing rotated180 degrees. Crops initially cutting B/C superscripts were supplemented by Bfull/Cfull; the clipped ending was supplemented by noteend-full. Every group letter, superscript, subscript, prime, tilde, punctuation mark and condition checked; every C doubt resolved or explicitly retained. Faint mirrored type is show-through from086, not an independent text. H section/editorial note after this marker concerns later excluded scans and is not087 manuscript text. No OCR, parallel transcription, compilation, audit or sealed-context access.'
r.save('work/record087.json')
