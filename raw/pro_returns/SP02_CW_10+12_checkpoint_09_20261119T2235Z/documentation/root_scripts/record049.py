import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-02',10,49);ch=r.change
r.edit(r'\unsure{pas}',r'pas')
r.edit(r"l'envelopp\unsure{e}",r"l'enveloppe")
r.edit(r'\mathrm{GL}(n)_k',r'\mathrm{Gl}(n)_k')
r.edit(r'(\unsure{grou}',r'(grou')
r.edit(r'\uline{Proposition} 11.11.',r'\uline{Proposition} 11.\begin{tikzpicture}[x=1cm,y=1cm,baseline=(n.base)]\node (n) at (0,0) {11};\draw (-.15,.3)--(-.02,.3);\draw (-.07,-.08)--(-.07,-.25);\end{tikzpicture}.')
r.edit(r'un\inserted{$k$-}schéma',r'un\inserted{\begin{tikzpicture}[x=1cm,y=1cm,baseline=(n.base)]\node (n) at (0,0) {$k$-};\draw (-.15,-.5) .. controls (-.05,-.15) and (.35,-.25) .. (.4,.15);\end{tikzpicture}}schéma')
ch('manuscript number','17','omitted','17','Tall 1 and diagonal 7 with crossing stroke.','number','omission')
ch('heading underline','Proposition underlined','whole heading bold','Proposition underlined','One line runs below Proposition and stops before its number.','heading','other')
ch('struck opening ent',r'Soi\deleted{\unsure{ent}}t',r'Soit \struck{un}',r'Soi\deleted{\unsure{ent}}t','Typed e is under the new tall pen t, n survives to its right, and the last letter is covered by hatching; no separate un is visible.','ent','misread word','low')
ch('condition iv pas',r'\unsure{pas}','pas','pas','Left descending stem and rounded upper bowl form p; a and s remain clear despite local overprinting.','pas','other','medium',True,False)
ch('condition v cancelled hypothesis',r'\deleted{(si G est de type fini sur k),}',r'\struck{\ill{}}',r'\deleted{(si G est de type fini sur k),}','Upper/lower letter parts remain readable between the large diagonal hatch strokes, including si, est, type fini and final k),.','conditions','readable ink left as \\ill{}','high',False,True,True)
ch('condition v group notation',r'\mathrm{GL}(n)_k',r'\mathrm{Gl}(n)_k',r'\mathrm{Gl}(n)_k','Second letter has a long left top serif and a centered lower foot, the typewriter lower-case l form; no capital L rightward bottom arm.','Gl','misread symbol or index','high',True,False,False,True)
ch('Démonstration underline','underlined','italic','underlined','Separate straight pen line under the complete word.','middle','other')
ch('cancelled first proof clause','fidèlement sur X quasi-affine sur k, alors il opère fidèlement sur ...',r'\ill{}; editorial note says alors G opère','fidèlement sur X quasi-affine sur k, alors il opère fidèlement sur ...','Original typed letter tops and bottoms are visible through x overstrikes; after alors the tall i and l are distinct.','middle','readable ink left as \\ill{}','high',False,True,True)
ch('cancelled enveloppe ending',r'envelopp\unsure{e}',r'\ill{}','enveloppe','Last e has a rounded bowl and short middle bar immediately before the blank and affine.','enveloppe','readable ink left as \\ill{}','medium',True,True,True)
ch('cancelled affine formula',r"X'=Spec(\Gamma(",r'\ill{}',r"X'=Spec(\Gamma(",'Prime is a raised slant after X; both opening parentheses and handwritten Gamma survive the overtyping.','enveloppe','readable ink left as \\ill{}','high',False,True,True)
ch('replacement clause placement','inserted above cancelled clause','ordinary baseline clause','inserted above cancelled clause','Sur X quasi-compact ... aussi is typed one half line above the x-cancelled words.','middle','insertion or placement')
for locus in ['Gamma(X,O_X) after sur le vectoriel','f_*(O_X)','Spec(Gamma(X,O_X))','V=Gamma(X,O_X)']:
 ch(locus+' alphabet',r'\underline{O}_X',r'\underline{\mathcal{O}}_X',r'\underline{O}_X','Typed plain circular O with a separate short underline; no script flourish.','middle','misread symbol or index')
ch('cancelled hypothesis after maintenant','que G est de type fini, et',r'\ill{}','que G est de type fini, et','The typed q/G, long type/fini letters, comma and et are distinguishable across pen hatching.','lower','readable ink left as \\ill{}','high',False,True,True)
ch('cancelled Aut argument',r'\deleted{\unsure{(V_i)}}','omitted',r'\deleted{\unsure{(V_i)}}','Large opening parenthesis and V strokes remain, with a lowered i-like serif; the heavy hatch obscures the closing portion.','Aut','omission','low')
ch('cancelled final K formula',r'K_{\unsure{1|i|l}}=e',r'\ill{}',r'K_{\unsure{1|i|l}}=e','K, equals sign and e survive x overtyping. Lower glyph has a long upper serif and foot but no separable dot; index alternatives remain open.','last','readable ink left as \\ill{}','low',False,True,True)
ch('cancelled final grou fragment',r'\unsure{grou}',r'\ill{}','grou','g descender, r shoulder, closed o and the u bottom/right stem can be separated from the x strokes. The fragment stops there.','last','readable ink left as \\ill{}','medium',True,True,True)
ch('left grouping stroke','TikZ vertical line','omitted','TikZ vertical line','Long nearly vertical pen stroke runs alongside the conditions.','margin','drawing or diagram')
for element,place,shape,crop in [('049-29','proposition number','short bar above first 1 after the point and a short stem below it','number-edit'),('049-30','inserted k-','curving insertion stroke rising at the right of k-','conditions')]:
 ch(place+' marks','omitted','omitted','TikZ '+shape,'Visible '+shape+'; no textual expansion inferred.',crop,'drawing or diagram','high',True,True)
 r.r['inventory_extra'].append(dict(scan='10:049',sheet_kind='typescript',hand='his hand',element=element,kind='drawing',position=place,first_words_or_objects=shape,transcribed='yes'))
for p,rd,alt in [('amended Soient','ent',''),('cancelled Aut argument','(V_i)',''),('last cancelled K index','1','i; l')]:r.doubt(p,rd,alt,'low')
r.notation('typed general linear group name',r'Gl(n)_k','10/049 condition (v)','read: lower-case l; compare individual occurrences, do not normalize')
r.r['crops']=json.loads(Path('work/crops049.json').read_text())
r.r['inspection_note']='Whole then both halves read in order. All agreed prose, signs, indices and arrows checked; every cancellation, addition and margin enlarged. Slanted algébrique sur le rotated upright. Inventoried all 28 witness elements and two omitted graphical marks. The unusual un vectoriel and final noethé continuation remain as ink. No context or mathematical check.'
r.save('work/record049.json')
