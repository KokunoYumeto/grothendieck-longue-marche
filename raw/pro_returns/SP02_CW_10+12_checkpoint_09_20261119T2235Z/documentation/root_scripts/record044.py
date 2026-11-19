import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-02',10,44);ch=r.change
r.edit(r'\unsure{\mathrm{Mod.}|\mathrm{Mod;}}',r'\mathrm{Mod;}')
r.edit(r'\node at (0,0) {5}',r'\node at (0,0) {$S$}')
r.edit(r'\unsure{il en est de même de}','il en est de même de')
r.edit(r'\mathcal{O}}_{\mathbb{S}}',r'\mathcal{O}}_{\unsure{\mathbb{S}|S}}')
r.edit(r'Proposition 11.5.- Soient $X$ un $S$-préschéma',r'Proposition 11.5.- Soient $X$ un $S$-p\handwritten{\makebox[0pt][l]{\begin{tikzpicture}[x=.2cm,y=.2cm,baseline=-.3ex]\draw (0,-.2) .. controls (.35,0) and (.55,.4) .. (.8,.4);\end{tikzpicture}}}réschéma')
ch('manuscript number','12','omitted','12','Tall initial 1 followed by hooked curved 2.','top','omission')
for p,crop in [('definition title','top'),('enveloppe affine','top'),('11.4 title','upper'),('proposition heading and assumptions','proposition'),('conditions a, b and Alors','proposition'),('conclusions i, ii','proposition')]:
 ch(p,'underlined','bold/italic or unmarked','underlined','Pen rules lie beneath the relevant words and lines; heading hyphens are short.',crop,'other')
ch('first A',r'\unsure{\mathcal{A}|a}',r'\mathcal{A}',r'\unsure{\mathcal{A}|a}','Low closed bowl and returning upper loop; calligraphic A versus a remains unsettled.','top','misread symbol or index','medium')
ch('mark beneath 11.3',r'\deleted{\unsure{vu}}','omitted',r'\deleted{\unsure{vu}}','Small linked strokes crossed by the heading rule; probable vu, deletion status also uncertain because the rule continues as an underline.','vu1','omission','low')
ch('mark beneath 11.4',r'\unsure{vu}','omitted',r'\unsure{vu}','Two tall linked pencil strokes crossing the underline, first a deep v, second less regular.','vu2','omission','medium')
ch('Exp. I',r'\deleted{Exp.} I','Exp. I',r'\deleted{Exp.} I','Oblique pen stroke crosses Exp., leaving I untouched.','upper','deletion state')
ch('first binivoque',r'bi\deleted{n}\inserted{un}ivoque','biunivoque',r'bi\deleted{n}\inserted{un}ivoque','Typed n crossed obliquely; un written immediately above.','upper','deletion state')
ch('deleted Hom',r'\deleted{\unsure{\operatorname{Hom}}}',r'\struck{\ill{}}',r'\deleted{\unsure{\operatorname{Hom}}}','Several rounded and upright letter remnants beneath close diagonal strokes; Hom remains tentative.','cancellations','readable ink left as \\ill{}','low',False,True,True)
ch('cancelled T in index',r'\deleted{\unsure{T}}','omitted',r'\deleted{\unsure{T}}','Typed upright and foot remain to the right of S under the cancellation patch.','cancellations','omission','low')
for p,rd in [('cancelled opening parenthesis','('),('cancelled closing parenthesis',')')]:
 ch(p,'doubtful cancelled '+rd,'omitted / live closing parenthesis','doubtful cancelled '+rd,'Narrow curved stroke remains under short hatch marks in the indicated position.','cancellations','deletion state','low')
for p in ['first Hom in i.e. addition','second Hom in i.e. addition']:
 ch(p,r'\underline{O}_S',r'\mathcal{O}_S',r'\underline{O}_S','Round upright O with a clear separate horizontal underline, S lower and to the right.','addition','misread symbol or index')
ch('cancelled V/W',r'\deleted{\unsure{\mathbb{V}|W}}',r'\struck{\ill{}}',r'\deleted{\unsure{\mathbb{V}|W}}','Right sloping limb and parallel vertical survive, left part obscured; V or W still uncertain.','second-cancel','readable ink left as \\ill{}','low',False,True,True)
ch('second binivoque',r'bi\inserted{un}nivoque','biunivoque',r'bi\inserted{un}nivoque','un is above a fully visible n with no cancelling line across this second n.','middle','insertion or placement')
ch('last Mod in 11.4',r'\unsure{\mathrm{Mod.}|\mathrm{Mod;}}','Mod.','Mod;','Separate upper dot and lower comma with a small descending tail.','Mod','misread symbol or index','high',True,True)
ch('joining stroke inside préschéma','omitted','omitted','TikZ joining stroke between p and r','Curving pencil stroke rises from the bottom right of p toward the top of r across the unusually wide gap.','prop-correction','drawing or diagram','high',True,True)
ch('vérifiées',r'vérifiée\deleted{s}','vérifiée',r'vérifiée\deleted{s}','Final s remains under a vertical black cancellation.','proposition','omission')
ch('circled marginal symbol','5','S','S','Both ends curve inward and the upper half is rounded, without a horizontal numeral-5 cap; ink reads S.','symbol5','misread symbol or index','high',True,False)
ch('marginal circle','TikZ circle','circle described','TikZ circle','Tall slanted oval surrounds the S.','symbol5','drawing or diagram')
ch('symmetric algebra S, twice',r'\mathbb{S}',r'\mathrm{S}',r'\mathbb{S}','Distinct parallel inner stroke in both upper and lower bowls of the S.','symmS; proposition','misread symbol or index')
ch('final base S',r'\mathbb{S}','S',r'\unsure{\mathbb{S}|S}','Doubled heavy S contours resemble retracing; alphabet intention uncertain.','lastS','misread symbol or index','medium',True,True)
ch('cancelled clause at bottom',r'\unsure{il en est de même de} S(F)',r'\struck{\ill{}}','il en est de même de S(F), cancelled','Typed letters and circumflex of même remain individually visible between X overstrikes; terminal symmetric-algebra symbol and F also readable.','end','readable ink left as \\ill{}','high',True,True,True)
for p,rd,alt,co in [('first A',r'\mathcal{A}','a','medium'),('under 11.3','deleted vu','live vu','low'),('under 11.4','vu','','medium'),('cancelled Hom','Hom','','low'),('cancelled T','T','','low'),('cancelled opening parenthesis','(','','low'),('cancelled closing parenthesis',')','','low'),('cancelled V',r'\mathbb{V}','W','low'),('final base S',r'\mathbb{S}','S','medium')]:r.doubt(p,rd,alt,co)
r.r['crops']=json.loads(Path('work/crops044.json').read_text())
for n,b in [('addition',[941,630,1665,722]),('lastS',[191,2040,241,2090]),('symmS',[948,1562,996,1608]),('second-cancel',[286,790,360,840]),('Mod',[1281,946,1407,1006]),('prop-correction',[605,1148,785,1190])]:r.crop(n,b,scale=5)
r.r['inventory_overrides']={'044-27':{'first_words_or_objects':'S inside oval'}}
r.r['inventory_extra']=[dict(scan='10:044',sheet_kind='typescript',hand='unnamed hand',element='044-36',kind='drawing',position='within préschéma in proposition heading',first_words_or_objects='curved joining stroke from p to r',transcribed='yes')]
r.notation('symmetric algebra letter',r'\mathbb{S}','10/044 two bowls with internal parallel strokes; circled marginal S','read')
r.r['inspection_note']='Whole then both halves read; every formula and all cancellations, margins and C doubts enlarged. Final cancelled clause resolved from letter traces, marginal S distinguished from numeral 5. No argument repaired, including live n under second un addition and cancelled formula parentheses.'
r.save('work/record044.json')
