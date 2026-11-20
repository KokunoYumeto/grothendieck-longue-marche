import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,40);ch=r.change
r.edit(r'\handwritten{\gamma}',r'\handwritten{\unsure{\gamma|\upsilon}}',count=7)
ch('manuscript number','8','omitted','8','Handwritten two-loop numeral 8.','number','omission')
for k,p in enumerate(['first morphism','second morphism','base-change equality left','base-change equality right','before soit plat','deduced surjective morphism','n+1 covering morphism','last fibre morphism']):
 ch(p,r'\unsure{\gamma|\upsilon}' if k==0 else r'\gamma',r'\psi',r'\unsure{\gamma|\upsilon}','Two-armed fork with short descending stem, no independent central prong. Same letter form throughout; local uncertainty retained consistently.','top' if k<7 else 'proof-end','misread symbol or index','medium',k!=0,True,False,True)
ch('base-change equality placement',r"\gamma'^n_{(\kappa(\eta))}",r"\psi'^n(\kappa(\eta))",r"\unsure{\gamma|\upsilon}'^n_{(\kappa(\eta))}",'Parenthesized field expression is lowered below the map and its exponent, rather than following it on the baseline.','top','misread symbol or index','high',False,True,False,True)
ch('inserted EGA reference','11.2.6','17.2.6','11.2.6','Second numeral is a narrow vertical 1 with top serif, matching the preceding 1; no descending diagonal 7.','reference','misread symbol or index','high',False,True,False,True)
ch('old EGA closing parenthesis',r'\deleted{)}','omitted',r'\deleted{)}','Old typed right parenthesis crossed by insertion leader, with replacement closing parenthesis above.','reference','omission')
ch('corollary heading','underlined; short dash','bold; em dash','underlined; short dash','Rule below heading and short dash.','corollary','other')
ch('corollary statement','underlined','no underline','underlined','Rules under all five physical lines.','corollary','omission')
ch('corollary final second index',r'\unsure{e|s}','s',r'\unsure{e|s}','Black oval with a pale horizontal slit has an e-like loop, unlike adjacent typed s; overinking prevents decision.','index','misread symbol or index','medium',False,True,False,True)
for p,old,new in [('first transition reference','1','2'),('second transition reference','2','3')]:
 ch(p,new,r'\struck{'+old+r'}\add{'+new+'}',new,'Current handwritten numeral is visible; no separately recoverable earlier numeral can be securely distinguished beneath the thick stroke.','references','text not on the page','medium')
ch('transition after finie','[','omitted','[','Tall open-right square bracket immediately before s’étendent.','transition','omission')
ch('transition cancelled noun',r'\deleted{préschéma}',r'\struck{\ill{}}',r'\deleted{préschéma}','p descender, ré accent, schéma forms remain readable through repeated Xs.','cancelled','readable ink left as \\ill{}','high',False,True,True)
ch('10.14 label','double underline','bold','double underline','Straight rule with second short wavy stroke beneath label.','bottom','other')
ch('10.14 opening statement','underlined','no underline','underlined','Faint rules remain below the two typed lines.','bottom','omission','medium')
r.doubt('eight map symbols',r'\gamma',r'\upsilon','medium','All are two-armed, excluding H psi; first C doubt carried through recurring instances.')
r.doubt('corollary final second index','e','s','medium')
r.doubt('transition reference underlayers','no separately readable old digits','H suggests cancelled 1 and 2','low','Only present digits 2 and 3 are transcribed; underlayers cannot be separated.')
r.r['crops']=json.loads(Path('work/crops040.json').read_text())
r.notation('commutator map glyph',r'\gamma | \upsilon','10/040 eight occurrences, with primes, n and n+1 exponents, field subscript','ambiguous')
r.r['inspection_note']='Whole then both halves read; all proof formulas checked in enlarged blocks including primes, subscript versus argument, powers n/n+1 and all s/eta subscripts. Every C doubt and witness difference enlarged. Inserted reference is 11.2.6. Inventory checked completely.'
r.save('work/record040.json')
