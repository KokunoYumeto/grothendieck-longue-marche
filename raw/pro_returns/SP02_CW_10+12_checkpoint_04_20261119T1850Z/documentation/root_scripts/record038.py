import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,38);ch=r.change
r.edit(r'\deleted{\unsure{p}}',r'\deleted{p}')
r.edit(r'\unsure{nœ thériens|nœthériens}','nœ thériens')
r.edit(r'\unsure{nœ thérien|nœthérien}','nœ thérien')
ch('manuscript page','6','omitted','6','Large handwritten 6.','number','omission')
ch('first algebra letter',r'\unsure{\mathscr{A}|\mathcal{A}}',r'\mathcal{A}',r'\unsure{\mathscr{A}|\mathcal{A}}','Rounded looped handwritten capital, matching the preceding page; font analogy uncertain.','top','misread symbol or index','medium')
ch('after anneaux',r'\deleted{\unsure{pas}}',r'\struck{\ill{}}',r'\deleted{\unsure{pas}}','Initial p descender and short trailing strokes survive dense crossing; middle cannot be securely isolated.','pas','readable ink left as \\ill{}','low',False,True,True)
for place,old,new,crop in [('first line',r'\unsure{nœ thériens|nœthériens}','nœ thériens','noether'),('second line',r'\unsure{nœ thérien|nœthérien}','nœ thérien','circles')]:
 ch(place,old,new.replace('œ ','oe'),new,'Joined oe ligature followed by a full visible space before th.','top; '+crop,'abbreviation expanded or spelling modernised','high',True,True)
ch('upper-left correction and second line','TikZ oval, circles and exchange curve','described in editorial note','TikZ oval, circles and exchange curve','Slanted intervertir enclosed by an oval; each typed word circled, curved link has heads at both ends.','margin; circles','drawing or diagram')
ch('Proposition 10.11 heading','underlined; short dash','bold; em dash','underlined; short dash','Thin underline and short horizontal dash, no bold type.','heading','other')
for p,crop in [('introductory assertion','heading'),('item i','i'),('item ii','ii'),('item iii','iii')]:
 ch(p,'underlined','no underline','underlined','Rules run beneath all physical lines of this block. ',crop,'omission')
for p,token in [('i before H prime','H'),('i before u prime','u'),('i before v prime','v'),('iii before H prime','H')]:
 ch(p,'resp','resp.','resp','No dot between p and following symbol.','i' if p.startswith('i ') else 'iii','text not on the page')
ch('i after foncteur',r'\deleted{\unsure{s}}','omitted',r'\deleted{\unsure{s}}','Blackened single-character patch immediately after r; underlying s remains uncertain at 6x.','s','omission','low')
ch('ii beneath S',r'\deleted{\unsure{p}}S',r'\struck{S}',r'\deleted{p}S','Full S is live; lower serif and descender of a typed p survive below the S.','p','deletion state (struck given live or live given struck)','high',True,True)
ch('iii representability clause','per','par','per','Middle letter has an open e eye and horizontal crossbar.','typo','misread word')
for p,rd,alt,conf in [('first algebra letter',r'\mathscr{A}',r'\mathcal{A}','medium'),('after anneaux','deleted pas','','low'),('i after foncteur','deleted s','','low')]:r.doubt(p,rd,alt,conf)
r.r['crops']=json.loads(Path('work/crops038.json').read_text())
for n,b,s in [('pas',[1053,103,1110,132],6),('s',[1108,879,1139,925],6),('p',[482,1166,508,1211],6),('typo',[994,1796,1057,1853],5),('noether',[1113,99,1305,139],4),('circles',[800,146,1244,244],3),('heading',[393,447,1655,710],2)]:r.crop(n,b,scale=s)
r.notation('nœ thérien spelling','nœ thérien(s)','10/038 first two lines: visible ligature and space')
r.notation('generic-point letter',r'\eta','10/038 all handwritten subscripts and first proposition; same loop with long descending terminal')
r.r['inspection_note']='Whole and both halves read in order, then all blocks enlarged; intervertir rotated upright. Every hypothesis, prime, eta and functor subscript checked, including absent opening parentheses before H prime and K prime. Three C doubts resolved; other three retained. Every inventory element checked.'
r.save('work/record038.json')
