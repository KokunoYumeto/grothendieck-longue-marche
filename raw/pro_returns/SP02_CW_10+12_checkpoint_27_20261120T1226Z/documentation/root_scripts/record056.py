import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-03',10,56,kind='text');ch=r.change
r.edit(r'\unsure{un|une}','une')
r.edit(r'\unsure{Dan|Dans}','Dan')
r.edit(r'\unsure{erronée}',r'\unsure{formulée}')
r.edit(r'\deleted{Exp} 4, cor du th.\uline{1}',r'\deleted{Exp} 4, cor du th.\uline{1}\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.1cm]\draw[thin] (0,-.1).. controls (-.1,-.35) and (-1.5,-.1)..(-1.7,-.4)--(-1.75,-.6)--(-1.8,-.35);\end{tikzpicture}')
r.edit(r' comme quotient de $G/G^\circ$, et}',r' comme quotient de $G/G^\circ$, et\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.1cm]\draw[thin] (0,.05).. controls (0,-.25) and (-1.9,-.15)..(-2,-.35)--(-2.02,-.55);\end{tikzpicture}}')
r.edit(r'.. (1.2,0);\end{tikzpicture}',r'.. (1.2,0);\draw (0.8,6.8).. controls (0.7,6.5) and (0.3,6.5)..(-0.2,6.45);\end{tikzpicture}')
ch('BIBLE title','underlined','italic','underlined','A separate pencil line runs below all five capitals.','upper1; reference','other')
ch('cancelled old reference',r'\unsure{VII|VIII}',r'\ill{}',r'\unsure{VII|VIII}','Pale upright strokes remain below dense diagonal cancellations; their number is not securely separable.','reference','readable ink left as \\ill{}','low',False,True,True)
ch('replacement reference Exp','deleted','live','deleted','A heavy oblique stroke cuts through the three letters.','reference','deletion state (struck given live or live given struck)')
ch('replacement cor','cor','cor.','cor','No separate full stop occurs between r and du.','cor','abbreviation expanded or spelling modernised')
ch('theorem numeral','underlined 1','plain 1','underlined 1','An angular upright 1 has a second short separate stroke beneath it.','theorem1','other')
ch('replacement insertion bracket','omitted','omitted','TikZ bracket below raised reference','A long shallow underline curls upward at right and drops to a V-shaped attachment point left of il.','reference; upper1','drawing or diagram','high',True,True)
ch('first affine punctuation','affine. donc','affine, donc','affine. donc','The mark after affine is a small compact baseline stop without a descending tail. The following d is lowercase.','affine-dot; upper2','other')
ch('component superscripts',r'\unsure{\circ|0|o} first occurrence','o',r'\unsure{\circ|0|o} first occurrence; circle thereafter','All five superscripts are handwritten round loops; their exact character class is not distinguished by the ink.','first-super; upper2','misread symbol or index','medium')
ch('quotient insertion bracket','omitted','omitted','TikZ bracket below raised clause','A curved lower stroke runs under comme quotient ... et and hooks downward beside the following G.','upper2','drawing or diagram','high',True,True)
ch('right-margin grouping curve','long curve','omitted','long curve with short left branch','The long near-vertical stroke has a short leftward curving branch near its upper fifth.','right-line','drawing or diagram','high',True,True)
ch('separator above cancelled notes','TikZ curve','editorial mention only','TikZ curve','A continuous shallow arc spans the top of the lower block.','separators','drawing or diagram')
ch('NB heading','underlined N.B.','plain N.B.','underlined N.B.','A distinct separate line sits below N.B., ending before the item number.','NB1','other')
ch('NB1 th','th','th.','th','No stop follows the h before entraîne.','NB1','abbreviation expanded or spelling modernised')
ch('NB1 verb accent',r'\unsure{entraîne|entraine}','entraîne',r'\unsure{entraîne|entraine}','The upper i region is crossed by a diagonal cancellation; an independent circumflex cannot be isolated.','entraine','misread word','medium')
ch('NB1 article',r'\unsure{un|une}','une','une','The final upward loop and rightward return are visible after the n and before the separate r of rep.','un; NB1','misread word','medium',True,False)
for word in ['rep','dim']:
 ch('NB1 '+word,word,word+'.',word,'There is no isolated dot after the abbreviation in the enlarged line.','NB1','abbreviation expanded or spelling modernised')
ch('NB1 terminal point','absent','present','absent','No point follows the final rho before the blank right area.','NB1','other')
for nb in ['NB2','NB3']:
 ch(nb+' réf','réf','réf.','réf','The f descender is followed by whitespace and à; no dot is visible. ',nb,'abbreviation expanded or spelling modernised')
ch('NB3 opening',r'\unsure{Dan|Dans}','Dans','Dan','The a is followed by one low n arch and its outgoing stroke; no separate s is visible.','Dan; NB3','misread word','medium',True,True)
ch('NB3 after BIBLE','BIBLE Supposer','BIBLE, supposer','BIBLE Supposer','No comma occurs after the final E; the following S is a large angular capital.','NB3','misread word')
ch('NB3 qualifying word',r'\unsure{erronée}',r'\ill{}',r'\unsure{formulée}','A tall initial f with descending lower loop, then a partly crossed or/m sequence and a tall l followed by accented e and final e can be distinguished. The cancellation obscures the interior.','erronee; NB3','readable ink left as \\ill{}','medium',True,True,True,True)
ch('NB3 terminal point','absent','present','absent','The final l/e stroke continues into a long flourish with no separate full stop.','NB3; separators','other')
ch('separator below cancelled notes','TikZ curve','editorial mention only','TikZ curve','A separate thin slightly rising line runs below the whole note block.','separators','drawing or diagram')
for element,position,text in [('reference-bracket','below inserted reference','curved bracket with downward attachment'),('quotient-bracket','below quotient insertion','curved bracket with downward left hook')]:
 r.r['inventory_extra'].append(dict(scan='10:056',sheet_kind='text',hand='his hand',element='056-'+element,kind='drawing',position=position,first_words_or_objects=text,transcribed='yes'))
r.r['inventory_overrides']={'group-line':{'first_words_or_objects':'long curved stroke with short left branch'},'nb3':{'first_words_or_objects':'3) Dan la réf à BIBLE; formulée uncertain'}}
for p,rd,alt,co in [('old cancelled reference','VII','VIII','low'),('first component superscript',r'\circ','0; o','medium'),('NB1 verb','entraîne','entraine','medium'),('NB3 word after est','formulée','interior obscured; no secure second candidate','medium')]:r.doubt(p,rd,alt,co)
r.notation('component superscript',r'\circ|0|o','10/056 five G superscripts','unresolved')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/056') for a,b in [('cor','corollaire'),('th','théorème'),('rep','représentation'),('dim','dimension'),('réf','référence'),('dém.','démonstration')]]
r.r['crops']=json.loads(Path('work/crops056.json').read_text())
r.r['inspection_note']='Whole handwritten sheet and both halves read in order. Every line, letter accent, formula, capital, quotient slash, kernel subscript, component loop and punctuation checked in enlarged blocks. All C doubts and C/H differences enlarged. No mathematical correction applied. The cancelled NB3 word has a visible tall f rather than an initial e; its partly crossed middle remains qualified. Cancelled reference numerals and accent remain unresolved. No context opened or mathematical check performed.'
r.save('work/record056.json')
