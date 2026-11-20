import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,37)
ch=r.change
r.edit(r'\deleted{\unsure{p}}',r'\deleted{p}')
ch('first paragraph, before de présentation',r'\deleted{\unsure{p}}','omitted',r'\deleted{p}','Lower loop and long descender of p remain distinct beneath the overtyped d.','p','omission','high',True,True)
ch('manuscript page','5','omitted','5','Handwritten numeral at upper left.','whole','omission')
ch('first composition',r'\unsure{o|\circ}',r'\circ',r'\unsure{o|\circ}','Small typewritten oval matches recurring composition glyph; not enough to distinguish letter o from intended circle.','top','misread symbol or index','medium')
ch('10.9 heading','underlined, short dash','bold, em dash','underlined, short dash','Single rule beneath label, short dash following it.','10-9','other')
ch('10.9 assertion','underlined','no underline','underlined','Single rules run under all four lines.','10-9','omission')
ch('10.9 before i in I',r'\deleted{\unsure{un}}',r'\struck{\ill{}}',r'\deleted{\unsure{un}}','Two blackened typewritten characters, the u bowl and final upright partly visible.','un','readable ink left as \\ill{}','medium',False,True,True)
ch('10.9 identity-component superscripts','o',r'\circ','o','Typed small oval o throughout statement and proof, including cancelled inner superscript.','10-9; necessity; G-edit','misread symbol or index','high')
ch('end of necessity proof, corrected group',r'\uline{(G_i^{\deleted{o}})^o}',r'(G_i)^\circ',r'\uline{(G_i^{\deleted{o}})^o}','Old raised o is crossed by inserted right parenthesis; a second live o is written to its upper right; rule underneath.','G-edit','deletion state (struck given live or live given struck)','high')
ch('10.10 heading','single-underlined label, double-underlined prose','bold label, unmarked prose','single-underlined label, double-underlined prose','Label has one straight rule; prose has a straight rule with a second wavy cancellation-like underline below it.','bottom','other')
ch('10.10 terminal punctuation','no readable period','period','no readable period','Closing parenthesis meets clipped black right edge; no distinct period can be read.','heading-end','text not on the page','low')
for p in ['a','b']:
 ch(p+' base index','S_o','S_0','S_o','Lowered rounded glyph has typewriter lowercase o shape, as on preceding pages.','bottom','misread symbol or index')
ch('a after Z','handwritten slash','omitted','handwritten slash','Long oblique stroke separates Z from et.','bottom','omission')
ch('a cancelled adjective',r'\deleted{\unsure{principaux}}',r'\struck{\ill{}}',r'\deleted{\unsure{principaux}}','Initial p descender and terminal aux show through dense overtyping; middle remains partly obscured.','principaux','readable ink left as \\ill{}','medium',False,True,True)
ch('b family alphabet',r'\unsure{\mathscr{A}|\mathcal{A}}',r'\mathcal{A}',r'\unsure{\mathscr{A}|\mathcal{A}}','Handwritten round calligraphic capital with loop at upper right; exact font analogy unresolved.','bottom','misread symbol or index','medium')
r.doubt('first composition','o',r'\circ','medium')
r.doubt('10.9 cancelled word','un','','medium')
r.doubt('10.10 right edge','no readable terminal period','possible clipped period','low','No text is supplied outside the visible field.')
r.doubt('a cancelled adjective','principaux','','medium')
r.doubt('b alphabet',r'\mathscr{A}',r'\mathcal{A}','medium')
r.r['crops']=json.loads(Path('work/crops037.json').read_text())
for n,b in [('p',[1200,157,1245,198]),('un',[752,793,793,833]),('principaux',[1317,1777,1444,1826]),('G-edit',[319,1487,404,1557]),('heading-end',[1576,1638,1663,1700])]:r.crop(n,b,scale=5)
r.notation('identity component exponent','o','10/037 statement 10.9 and proof, typed small o; handwritten correction adds exterior o')
r.notation('calligraphic algebra A',r'\mathscr{A} | \mathcal{A}','10/037 b','ambiguous')
r.r['inspection_note']='Whole then both halves read; top, 10.9, complete necessity proof and bottom enlarged; every C doubt examined at further zoom. All formula indices checked, including structural target S without i and S=kappa(x) without Spec, exactly as visible. C inventory matched to page. Clipped final punctuation left unresolved.'
r.save('work/record037.json')
