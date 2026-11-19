import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,36)
ch=r.change
ch('upper left manuscript number','4','omitted','4','Handwritten 4 at upper left.','whole','omission')
ch('10.7 continuation','underlined','no underline','underlined','Six rules under the full continuation.','top','omission')
for p,crop,f in [('10.7 first projection','top',r'\unsure{o|\circ}'),('10.8 pr_1 v','lemma','o'),('diagram upper label','diagram','o'),('diagram left label','diagram','o'),('last proof formula','proof','o')]:
 ch(p,f,r'\circ',f,'Typed oval at x-height rather than a separately drawn mathematical circle; recurring glyph uncertainty retained at first occurrence. It does not alter the interpreted composition. ',crop,'misread symbol or index','medium')
ch('10.7 last quotient',r'R_j{}_{S_j}S_i',r'R_j\times_{S_j}S_i',r'R_j{}_{S_j}S_i','Blank between R_j and the lowered S_j: no crossed strokes occupy the product position.','top','text not on the page','high',False,True,False,True)
ch('after conséquence',r'\deleted{\unsure{du}}','omitted',r'\deleted{\unsure{du}}','Blackened compact typed cluster precedes live du; underlying d/u shapes remain uncertain.','du; intro','omission','medium')
ch('Lemme 10.8 heading','underlined; short dash','bold; em dash','underlined; short dash','Printed heading has underline and short dash, with no bold type.','lemma','other')
ch('10.8 after soient',r'\deleted{\unsure{j\in I,}}',r'\struck{\ill{}}',r'\deleted{\unsure{j\in I,}}','Left descender and right capital pillar with punctuation survive black hatching; entire formula retained as doubtful.','cancelled-j','readable ink left as \\ill{}','low',False,True,True)
ch('10.8 opening statement','underlined','no underline','underlined','Rules beneath all five lines through équivalentes.','lemma','omission')
ch('condition i','underlined','no underline','underlined','Single rule below entire statement.','diagram','omission')
ch('condition ii prose','underlined','no underline','underlined','Rules below both physical lines before diagram.','diagram','omission')
ch('diagram label','(D) typeset beside diagram','(D) only mentioned in note','(D) typeset beside diagram','Typed parenthesized D at left of square.','diagram','drawing or diagram')
ch('projection pair',r'\unsure{\substack{\longrightarrow\\[-.6ex]\rightharpoonup}|\rightrightarrows}',r'\rightrightarrows',r'\unsure{\substack{\longrightarrow\\[-.6ex]\rightharpoonup}|\rightrightarrows}','Upper arrow has full head; lower horizontal stroke has only a short upturned terminal mark, without a visible lower barb.','pair','misread symbol or index','medium')
ch('soit cartésien','underlined','no underline','underlined','Short rule only beneath final phrase.','diagram','omission')
ch('proof right edge after X/R',r'\deleted{\illegible{1}}','omitted',r'\deleted{\illegible{1}}','Solid black cancellation runs into the clipped edge; no complete word recoverable at 5x.','right-edge','omission','low')
for line,reading,alt,co in [('first composition','o',r'\circ','medium'),('after conséquence','deleted du','','medium'),('after soient',r'deleted j\in I,','','low'),('projection pair','upper arrow and lower upper-barbed stroke','two full right arrows','medium'),('proof right edge','one illegible cancelled word','','low')]:r.doubt(line,reading,alt,co)
r.r['crops']=json.loads(Path('work/crops036.json').read_text())
for name,b in [('pair',[863,1571,1045,1629]),('cancelled-j',[1197,783,1306,829]),('du',[817,641,859,674]),('right-edge',[1600,1715,1675,1778])]:r.crop(name,b,scale=5)
r.notation('typed composition glyph',r'o | \circ','10/036 first formula, lemma, two diagram labels, final proof; first occurrence marked, recurring oval retained','ambiguous')
r.notation('topology T',r'\mathbb{T}','10/036 six handwritten occurrences: shared top bar and doubled upright')
r.r['inspection_note']='Whole then both halves viewed. All top formulas and quotient indices, all four diagram objects and all four arrows/labels read, including surprising lower-right X. Blank missing product sign retained from ink. Every C doubt enlarged. No change to C text; all retained doubts explicitly documented.'
r.save('work/record036.json')
