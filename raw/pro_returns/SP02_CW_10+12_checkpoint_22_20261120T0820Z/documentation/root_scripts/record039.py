import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,39);ch=r.change
r.edit(r'ou \unsure{bien bien|bien}',r'ou bien bien')
r.edit(r'\textcircled{\unsure{40|10}}',r'\textcircled{40}')
r.edit(r'\handwritten{\gamma}_{\handwritten{\eta}}:',r'\handwritten{\unsure{\gamma|\upsilon}}_{\handwritten{\eta}}:')
ch('manuscript number','7','omitted','7','Handwritten 7 with a crossbar.','number','omission')
for p,crop in [('first citation','top'),('au sens de VIII','top'),('Il résulte alors','top'),('proof VI_A','proof')]:
 ch(p,r'\deleted{Exp.}','Exp. (deletion mentioned in a note)',r'\deleted{Exp.}','Single diagonal stroke through Exp. in each cited position. ',crop,'deletion state (struck given live or live given struck)')
ch('after présentation','fini',r'fini\supplied{e}','fini','Only fini is typed before the comma; no e is visible.','top','text not on the page')
ch('10.12 heading','underlined and short dash','bold and em dash','underlined and short dash','Same typeweight as adjacent text; long rule underneath and short dash following number.','prop-upper','other')
ch('10.12 assertion','underlined throughout','no underline','underlined throughout','Rules beneath every physical line through final reference.','prop-upper; prop-lower','omission')
ch('after G un',r'\deleted{S-préschéma}',r'\struck{\ill{}}',r'\deleted{S-préschéma}','Individual S, p, accent, schéma letters legible between repeated overtyped Xs.','S-preschema','readable ink left as \\ill{}','high',False,True,True)
ch('old connectedness clause',r'\deleted{ou bien A soit à fibres connexes}',r'\struck{\ill{}}',r'\deleted{ou bien A soit à fibres connexes}','All original letters remain visible between regular X overstrikes; fibres is plural.','old-clause','readable ink left as \\ill{}','high',False,True,True)
ch('second alternative, cancelled words',r'\deleted{ou \unsure{bien bien|bien}}',r'\struck{\ill{}}',r'\deleted{ou bien bien}','Two distinct groups bien follow ou; a second b ascender and i dot occur near the right.','ou-bien','readable ink left as \\ill{}','medium',True,True,True)
ch('second alternative, new marker',r'\inserted{(resp.}','live (resp. before cancellation',r'\inserted{(resp.}','Typed replacement sits above the cancelled ou bien bien; opening parenthesis and period visible.','prop-upper; ou-bien','insertion or placement')
ch('before new alternative','comma','omitted','comma','Comma remains after the cancelled first clause, before the replacement alternative.','prop-upper','omission')
ch('after D prime soit',r'\deleted{co}',r'\struck{\ill{}}',r'\deleted{co}','Open c and closed o survive two overtyped crosses.','co','readable ink left as \\ill{}','high',False,True,True)
ch('proof after second EGA 9.3.3',r'\inserted{)}','omitted',r'\inserted{)}','Large handwritten closing parenthesis descends below typed baseline.','proof','omission')
ch('last line first map',r'\unsure{\gamma|\upsilon}',r'\psi',r'\unsure{\gamma|\upsilon}','Two upper arms join one descending stem; there is no independent central upright as in psi. Gamma/upsilon analogy remains uncertain.','formula; gamma1','misread symbol or index','medium',False,True,False,True)
ch('last line second map',r'\gamma',r'\psi',r'\unsure{\gamma|\upsilon}','Same two-armed fork as first map, with a short central descender and a curved right branch; doubt made consistent locally.','formula; gamma2','misread symbol or index','medium',True,True,False,True)
ch('footnote number',r'\textcircled{\unsure{40|10}}',r'\uncertain{40} in editorial note',r'\textcircled{40}','Left numeral has an angled limb and crossing upright, followed by a closed zero, enclosed in an oval.','footnote','other','high',True,True,True)
ch('footnote separator','long horizontal rule','omitted','long horizontal rule','A single line separates footnote from preceding formula.','formula; footnote','drawing or diagram')
r.doubt('last line first map',r'\gamma',r'\upsilon','medium','Two arms, no third central stroke; H psi rejected.')
r.doubt('last line second map',r'\gamma',r'\upsilon','medium','Same fork-shaped glyph as first occurrence; must compare later recurring forms before freezing.')
r.r['crops']=json.loads(Path('work/crops039.json').read_text())
for n,b,s in [('ou-bien',[1376,967,1577,1001],5),('S-preschema',[1191,820,1376,859],4),('old-clause',[842,961,1357,997],4),('co',[564,1175,605,1205],6),('gamma1',[618,2017,674,2078],6),('gamma2',[1156,2024,1213,2087],6)]:r.crop(n,b,scale=s)
r.notation('commutator map glyph',r'\gamma | \upsilon','10/039 final line twice; two-armed fork, H psi not supported','ambiguous')
r.r['inspection_note']='Whole then both halves read; entire text in enlarged blocks; every cancellation and insertion inspected separately. All eta, primes, powers and base-field product indices checked. Corrected uncertainty for repeated map symbol, resolved duplicated bien and circled 40. C inventory matched in full.'
r.save('work/record039.json')
