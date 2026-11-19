import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,35)
r.edit(r'\unsure{fermé}',r'fermé')
r.edit(r'\unsure{v)|i)}',r'\unsure{i)|v)}')
r.edit(r'\deleted{\unsure{p}}du',r'\deleted{p}du')
r.edit('Dans la situation rappelée',r'Dans la s\unsure{i|à}tuation rappelée')
# Reproduce the drawn enclosure while retaining the insertion at its target.
old=r'\inserted{\handwritten{soit un monomorphisme central (resp. un monomorphisme invariant)}}'
new=r''' }\inserted{\handwritten{\figure{\begin{tikzpicture}
\node[align=left,text width=5cm,inner sep=3pt] (n) at (0,0) {soit un monomorphisme central (resp. un monomorphisme invariant)};
\draw[rounded corners=5pt] (n.south west) rectangle (n.north east);
\draw (n.west) -- ++(-.7,-.8);
\end{tikzpicture}}}}\uline{'''
r.edit(old,new)
ch=r.change
ch('top number','3','omitted','3','Handwritten 3 above text.','whole','omission')
ch('cancelled first word',r'\unsure{fermé}','fermé','fermé','The f upright, e-r-m and final accented e survive the crossing strokes.','upper','other','medium',True,False)
ch('first cancelled list label',r'\unsure{v)|i)}','(v)',r'\unsure{i)|v)}','An i-like upright with detached dot is visible; large oblique cancellation obscures a possible v. Ink-first order reversed, not selected from the following vi.','old-item','misread word','low',True,True)
ch('first cancelled item','underlined','no underline','underlined','Straight underline beneath the words, independently of diagonal cancellation.','upper','omission')
ch('second cancelled item','underlined','no underline','underlined','Straight underline beneath second item.','upper','omission')
ch('10.4 replacement clause','inserted at deleted clause','marginal text, replacement explained only in note','boxed insertion at deleted clause','Leader joins the box to the cancelled ait la propriété P.','box; upper','insertion or placement')
ch('10.4 replacement enclosure','no drawing','description of box','TikZ box with leader','Rounded rectangular enclosure and descending leader are visible.','box; upper','drawing or diagram','high',True,True)
ch('10.4 assertion','underlined','no underline','underlined','Rules beneath all three body lines.','upper','omission')
ch('10.4 final symbol',r'\deleted{\unsure{\mathbb{P}}}',r'\struck{\mathbb{P}}',r'\deleted{\unsure{\mathbb{P}}}','Blackened cluster with residual upright does not allow a confident P.','upper','misread symbol or index','low')
ch('proof cancelled reference','(EGA 8.8.2 et 8.8.3)','EGA 8.8.2 et 8.8.3','(EGA 8.8.2 et 8.8.3)','Both parentheses visible under cancellation.','proof','omission')
ch('proof inserted reference','(10.0) et (10.1),','(10.0) et (10.1)','(10.0) et (10.1),','Handwritten comma after closing parenthesis.','proof','omission')
ch('Corollaire','underlined','no underline','underlined','Separate short rule beneath handwritten heading.','corollary','omission')
ch('10.5 heading','double underlining','bold type','double underlining','Two pen strokes under printed number; typewriter has no bold face.','corollary','other')
ch('10.5 assertion','underlined','no underline','underlined','Three rules beneath the assertion.','corollary','omission')
ch('10.5 final product',r'\deleted{\unsure{H}_{\unsure{j|i}}}\inserted{S_i}','S_i',r'\deleted{\unsure{H}_{\unsure{j|i}}}\inserted{S_i}','Separate blackened upper/lower old glyphs below the clean replacement S and i; old capital and index not securely readable.','corollary','omission','low')
ch('10.6 heading','underlined Proposition 10.6.-','bold Proposition 10.6. —','underlined Proposition 10.6.-','Short dash and underline visible; no bold type.','prop-lemma','other')
ch('10.6 initial word','situation','situation',r's\unsure{i|à}tuation','Overprinted second character has loop plus upper mark; i and a-with-mark cannot be separated confidently.','situation','misread word','low',True,True)
ch('10.6 assertion','underlined','no underline','underlined','Pencil rules extend beneath all five assertion lines.','prop-lemma','omission')
ch('before du lemme',r'\deleted{\unsure{p}}du','du',r'\deleted{p}du','Typed p descender survives directly beneath overtyped d.','lemma-overprint','omission','high',True,True)
ch('bottom left T',r'\mathbb{T}','omitted',r'\mathbb{T}','Two vertical stems below a common horizontal top stroke in left margin.','bottom-T','omission')
ch('Lemme 10.7 heading','underlined Lemme 10.7.-','bold Lemme 10.7. —','underlined Lemme 10.7.-','Short hyphen after point, heading underline.','prop-lemma','other')
ch('Lemme 10.7 opening','underlined','no underline','underlined','Horizontal line under opening text to right of heading.','prop-lemma','omission')
for line,reading,alt in [('first cancelled item','i)','v)'),('end 10.4','deleted P',''),('10.5 old product capital','H',''),('10.5 old product index','j','i'),('10.6 overprinted word','situation','sàtuation')]:r.doubt(line,reading,alt,'low')
r.r['crops']=json.loads(Path('work/crops035.json').read_text())
for name,b in [('old-item',[402,141,480,203]),('lemma-overprint',[737,1856,791,1905]),('box',[1182,135,1644,294]),('bottom-T',[105,2003,189,2059])]:r.crop(name,b,scale=4)
r.crop('situation',[732,1417,899,1471],scale=5)
r.r['inventory_extra']=[{'scan':'10:035','sheet_kind':'typescript','hand':'his hand','element':'boxed-insertion-enclosure','kind':'drawing','position':'upper right, leader to deleted property clause','first_words_or_objects':'rounded rectangle and oblique leader','transcribed':'yes'},{'scan':'10:035','sheet_kind':'typescript','hand':'typewriter','element':'overprinted-si','kind':'text','position':'10.6 opening word','first_words_or_objects':r's\unsure{i|à}tuation','transcribed':'yes'}]
r.notation('topology T',r'\mathbb{T}','10/035 lemma and lower left margin: doubled stem under a single top bar')
r.r['inspection_note']='Whole, top half, bottom half read in order; all prose, primes, indices, products, quotient slashes, cancellations and insertions compared. Shared overprint and omitted enclosure added. All six C doubt loci re-examined. No proof-check event claimed.'
r.save('work/record035.json')
