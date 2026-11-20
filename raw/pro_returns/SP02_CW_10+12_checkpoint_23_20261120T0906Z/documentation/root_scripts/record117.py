from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,117);ch=r.change
r.edit(r'\scanpage{117}',r'\scanpage{117}'+'\n'+r'\mspage{116}')
r.edit('% archive sheet number: 116','')
r.edit(r"d'endomorphismes des $\otimes$",r"d'endomorphismes des $\unsure{\otimes|\Omega}$")
r.edit('\n....\n',r'''
\figure{\begin{tikzpicture}[x=1em,y=1em,baseline]
\node at (0,0) {.};\node at (.7,0) {.};\node at (1.4,0) {.};\node at (2.1,0) {.};
\draw[line width=.15pt] (-.3,.35)--(-.3,.65)--(-.1,.63);
\draw[line width=.15pt] (.05,.63)--(.08,.35);
\draw[line width=.15pt] (.27,.35) .. controls (.45,.43) and (.46,.2) .. (.42,.15);
\end{tikzpicture}}
''')
r.edit(r'\unsure{Vinndrait|Viendrait}',r'Vi\unsure{\rlap{e}n\rlap{n}e|nn}dra$\mathbb{i}$t')
r.edit(r'\unsure{É|et}',r'\unsure{É}')
r.edit(r'\unsure{resp. com.}',r'\unsure{resp.} com.')
for place,crop,old,new in [('5.6','num56','4','5'),('5.7','num57','4','5'),('Par.6','num6','5','6'),('Par.7','num7','6','7')]:
 ch(place+' overwritten number','deleted'+old+' plus hand'+new,new+' only','deleted'+old+' plus hand'+new,'The old typed body remains visible under the added handwritten numeral; the old strokes are retained.',''+crop,'deletion state')
for place,crop in [('Par.6','heading6'),('Par.7','heading7')]:
 ch(place+' underline','underlined Par','plain Par','underlined Par','A separate straight horizontal line lies under Par and stops before the number.',''+crop,'omission')
ch('first typed tensor prefix','otimes','otimes',r'\unsure{\otimes|\Omega}','Both typed signs have a crossed interior, rounded arch and long lower feet; the contour does not settle an independent closed outer oval. First occurrence is qualified; the second uses the first candidate.','tensor6a; tensor6b','misread symbol or index','medium',True,True,False,True)
ch('points between headings','four points only','ill and ellipsis','four points with faint traces above the first','Four round typed points are clear. Several small detached vertical and angled strokes remain above and to the left of the first point; they do not establish a word and are reproduced graphically.','dots','drawing or diagram','medium',True,True,True)
ch('Picard parenthesis two overlapping cells',r'\unsure{Vinndrait|Viendrait}','Viendrait',r'Vi\unsure{\rlap{e}n\rlap{n}e|nn}drait','Both adjacent cells have n-like upright stems and an additional central horizontal/curved body resembling e. The first upper counter is dark, so the pair of physical overlaps remains qualified rather than reconstructed as a familiar verb.','vin; vin-over; vin-pair','misread word','medium',True,True)
ch('Picard parenthesis repeated i','ordinary i','ordinary i',r'$\mathbb{i}$','The penultimate typed cell has two offset vertical stems, displaced baseline feet and a broadened double dot. This self-overstrike uses the prescribed blackboard convention.','vin-i; vin','misread symbol or index','high',True,True)
ch('right note accent',r'\unsure{necessairement|nécessairement}','nécessairement',r'\unsure{necessairement|nécessairement} retained','A small raised mark is offset toward the following c; the faint e and mark do not establish the accent attachment securely. The letter sequence itself is readable.','rightnote; necessairement','misread word','medium',False,True)
ch('right note lieu','lieu','uncertain lieu','lieu','The tall l, dotted i and joined low e/u are visible in the rotated note.','rightnote','misread word','high',False,True,True)
ch('canceled Par.8 heading',r'\deleted{\uline{Par}.8 \unsure{É|et}}','live Par; struck ill',r'\deleted{\uline{Par}.8 \unsure{É}}','The blue diagonal cancellation crosses Par and8. The final upright carries three horizontal strokes and a raised oblique mark, favouring the qualified É-shaped reading; a separate e followed by t is not established.','cancelpar8','deletion state','medium',True,True,True)
ch('Plus gén punctuation','Plus gén,','Plus gén.,','Plus gén,','A long comma-like descending stroke follows gén, without a separate abbreviation point. The accent above é is visible.','bottom1','abbreviation expanded or spelling modernised')
ch('canceled catégories',r'\deleted{\unsure{catégories}}','deleted catégories',r'\deleted{\unsure{catégories}} retained','The c/a-like opening, tall t and g descender survive, but the broad cancellation covers most of the remaining joined letters.','monoides','misread word','low',False,True)
ch('inserted monoïdes case and placement',r'\inserted{\unsure{monoïdes|Monoïdes}}','inline monoïdes',r'\inserted{\unsure{monoïdes|Monoïdes}} retained','The replacement is written above the canceled word. The initial has a large looped entry and angular arches, leaving its case unsettled; the following o-n-o-ï-d-e-s strokes are visible.','monoides; bottomall','insertion or placement','medium',False,True)
ch('small left note wording and placement',r'\unsure{resp. com.}','uncertain top. an. between associatif and et',r'\margin{\handwritten{\unsure{resp.} com.}}','The first abbreviation retains uncertain joined r/e/s-like strokes and a long p descender. The next has an open c, small o and two m arches; both terminal points are visible. This note lies below the canceled Par.8 at left, separate from the main sentence.','resp; bottomall','misread word','medium',True,True,True)
ch('last paragraph placement','text under Par.7','marginal paragraph','text under Par.7','The two-line addition occupies the main text area beneath the typed headings, while the short resp. com. note is separately at its left.','bottomall','insertion or placement')
ch('folio','comment only','administrative page116','mspage116','The three lower-left pencil numerals read116.','folio','insertion or placement','high',True,True)
r.doubt('first typed tensor',r'\otimes',r'\Omega','medium','Crossed arch with feet in both typed occurrences.')
r.doubt('Picard parenthesis cells3–4',r'\rlap{e}n\rlap{n}e','nn','medium','Both cells preserve extra bars/curves; first upper counter is heavily inked.')
r.doubt('right note accent','necessairement','nécessairement','medium','Raised small mark is offset and cannot be securely attached to the first e.')
r.doubt('canceled Par.8 terminal shape','É','','medium','Three crossbars and upper oblique mark favour É; cancellation crosses the lower part.')
r.doubt('deleted word after Plus gén','catégories','','low','Broad horizontal cancellation obscures most letter centers.')
r.doubt('replacement above deleted word','monoïdes','Monoïdes','medium','Initial flourish leaves capitalization uncertain.')
r.doubt('small left abbreviation','resp.','','medium','r/e/s joined and faint; p descender and point visible; following com. clear.')
r.notation('typed tensor prefix','crossed arch/feet; tensor/Omega first, first candidate second','10/117','unresolved')
r.notation('typed overlaps','two qualified e/n cells; repeated penultimate i as mathbb','10/117','partly unresolved')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/117') for a,b in [('Par. / par.','paragraphe'),('gén','généralement'),('néc.','nécessairement'),('comm. / com.','commutatif'),('resp.','respectivement (tentative)')]]
r.r['inventory_overrides']={'010':{'first_words_or_objects':'four points and faint nonalphabetic traces above first'},'015':{'first_words_or_objects':'Vi with qualified e/n overlaps; repeated penultimate i; mieux avant par.4'},'018':{'first_words_or_objects':'canceled underlined Par.8 and qualified É-shaped mark'},'021':{'first_words_or_objects':'qualified resp.; resolved com.'}}
extras=[('dot-traces','above first of four points','small detached strokes reproduced as graphic','drawing','unnamed hand'),('folio','lower left','116','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:117',sheet_kind='typescript',hand=hand,element='117-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops117.json').read_text())
r.r['inspection_note']='Whole and both halves read, including lower blank region and folio; C/H and six C doubt loci plus21 inventory rows then compared. All26 crop recipes viewed in order, including every overwritten numeral, both typed tensor signs, handwritten circled cross, canceled and inserted words, and rotated right note. Agreed text read against ink. Two e/n cells remain qualified and the visibly repeated i is encoded by mathbb. Faint strokes above the four points are drawn without inventing a word. H boundary heading/editorial note introduce the next sheet and are excluded here. No OCR, parallel transcription, context, compilation or mathematical check.'
r.save('work/record117.json')
