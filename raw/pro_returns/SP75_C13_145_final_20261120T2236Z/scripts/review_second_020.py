from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan020_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan020_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan020_boxes.tsv')}
n=dict(f);edits=[]
def edit(old,new):
 edits.append({'old':old,'new':new});return (old,new)
braces=[]
for term,label in [(r'\rho^{-1}\sigma_\infty\sigma_0\deleted{\rho}',r'l_\infty'),(r'\rho^{-1}\sigma_1\sigma_\infty\deleted{\rho}',r'l_1'),(r'\rho^{-1}\sigma_0\sigma_1\deleted{\rho}',r'l_0')]:
 old=r'\overbrace{('+term+r')}^{'+label+'}'
 new=r'(\overbrace{'+term+r'}^{'+label+'})'
 braces.append(edit(old,new));n['B03']=n['B03'].replace(old,new)
etc=edit(r'\sigma_1$ etc.',r'\sigma_1$ etc');n['B06']=n['B06'].replace(*etc)
def bracket(term,label):
 return r'\underset{'+label+r'}{\begin{tikzpicture}[baseline=(term.base)]\node[inner sep=1pt] (term) {$'+term+r'$};\draw ([yshift=-1pt]term.south west) -- ++(0,-3pt) -| ([yshift=-1pt]term.south east);\end{tikzpicture}}'
oldproduct=f['B07']
newproduct=oldproduct.replace(r'[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}]',r'['+bracket(r'\rho^{-1}\sigma_0\rho',r'\sigma_\infty')+r'\sigma_0\rho^{-1}]')
for term,label in [(r'\rho\sigma_0\rho^{-1}',r'\sigma_1'),(r'\rho^{-1}\sigma_0',r'\sigma_\infty'),(r'\rho^{-1}\sigma_0\rho',r'\sigma_\infty')]:
 newproduct=newproduct.replace(r'\underbrace{'+term+r'}_{'+label+'}',bracket(term,label))
edit(oldproduct,newproduct);n['B07']=newproduct
trial=edit(r'\deleted{\unsure{(\rho\sigma_0\rho^{-1})^2}}',r'\deleted{\unsure{(\rho\sigma_0\rho^{-1})^2|(\sigma_0\rho)^2}}')
edit('). Noter\n\\[','). Noter que\n\\[')
n['B09']='que\n'+f['B09'].replace(*trial)
nbterm=edit(r'l_1\deleted{\unsure{l_\infty^{-1}}}',r'l_1^{\deleted{\unsure{-1}}}\deleted{\unsure{l_\infty^{-1}|l_0^{-1}}}')
n['B12']=f['B12'].replace(*nbterm)
phrase=edit(r'\unsure{de notre groupe}',r'\unsure{de notre groupe|de sorte que}')
symbol=edit("\\unsure{\\mathcal E'|\\sigma_i'}","\\unsure{\\mathcal E'|\\sigma_i'|\\sigma'}")
n['B15']=f['B15'].replace(*phrase).replace(*symbol)
stop=edit('si on y remplace les $l_i$ par les $l_i^{-1}$.','si on y remplace les $l_i$ par les $l_i^{-1}$')
n['B16']=f['B16'].replace(*stop)
prime=edit(r"\sigma'_{\dot\rho^{-1}(i)}",r'\sigma^{\unsure{\prime|1}}_{\dot\rho^{-1}(i)}')
n['B17']=f['B17'].replace(*prime)
insert=edit(r'\inserted{(i,j,k)\text{ distincts})}',r'\inserted{(i,j,\unsure{k|h})\text{ distincts})}')
n['B18']=f['B18'].replace(*insert)
gen=edit('étant un des générateurs du centralisateur',r'étant \unsure{donc un|un des} \unsure{générateurs|générateur} \unsure{du|des} centralisateur')
punct=edit(r'$\mathcal E^+$. (ou',r'$\mathcal E^+$\unsure{.|,} (ou')
n['B19']=f['B19'].replace(*gen).replace(*punct)
chgts=edit('chgts. de notation indiqués',r'chgts de \unsure{notation|notations} indiqués')
n['B20']=f['B20'].replace(*chgts)
n['B21']=r'''\[
\deleted{(8)}\quad\left\{\begin{aligned}
\unsure{\deleted{\varepsilon_0}|\varepsilon_0}&=l_0^{\deleted{\unsure{-1|4}}}\sigma_1 l_{\unsure{0|1}}^{\deleted{\unsure{-1|4}}}\\
\unsure{\deleted{\varepsilon_1}|\varepsilon_1}&=\unsure{\deleted{l_\infty^{-1}}|l_\infty^{-1}}\sigma_\infty \deleted{l_1^{-1}}\ \inserted{l_1}\\
\varepsilon_\infty&=l_0^{-1}\sigma_0 l_\infty
\end{aligned}\right.
\]'''
edit(f['B21'],n['B21'])
c={
'B01':{'use_first':True,'adjudication':'Retain the handwritten8 in pagination markup.','ink':'The isolated mark has two connected loops crossing at the waist. The independent bare8 and the first mspage form encode the same number; attribution remains indeterminate.'},
'B03':{'final':n['B03'],'changed':True,'adjudication':'Keep the crossed rho factors; place the overbraces inside the parentheses.','ink':'Each crossed final letter retains a loop-headed descending rho body. The overbrace endpoints lie above the internal factors, inside the enclosing parentheses; neither parenthesis is included beneath its brace. All labels and surviving exponents are visible. The current bracket scope in both witnesses extended over the parentheses.'},
'B04':{'use_first':True,'adjudication':'Retain relation(5) unchanged.','ink':'All three raised2 figures, indices0/1/infinity, equality signs and final1 are distinct. Inline versus display delimiters do not alter the handwritten formula.'},
'B05':{'use_first':True,'adjudication':'Retain relation(6) without a final point.','ink':'Rho has its loop and long descender, the raised3 has two turns, and the final1 has a connected rightward hooked foot. No separate full stop follows.'},
'B06':{'final':n['B06'],'changed':True,'adjudication':'Retain the margin wording; remove the supplied stop after etc.','ink':'Ajouter, les relations, On a deux gén. and en fait avec relations are readable with their characteristic ascenders/descenders. The compact etc has joined letter strokes and no separate terminal point. The stop after gén. is separate and remains. The comma after1 and the following la are clear.'},
'B07':{'final':n['B07'],'changed':True,'adjudication':'Keep both whole-product alternatives; restore the first sigma-infinity annotation and flat bracket shapes.','ink':'The first square bracket and the adjacent close/open boundary are visible despite diagonal hatching. Below its initial rho^-1 sigma0 rho group there is an independent short flat rule with a sigma-infinity label; that first annotation was omitted. Two further flat-ended rules carry sigma1 and sigma-infinity. The latter endpoint and a possible additional rho remain entangled, so both existing alternatives are retained. The high inverse above the next rho has short minus/upright strokes, favouring the first reading over the blind un-inverted sequence. No =1 is written beyond the terminal bracket. The rules are represented literally as flat brackets, not detached empty underbraces.'},
'B08':{'use_first':True,'adjudication':'Retain conséquence des précédentes (vient du fait...) and the crossed illegible item.','ink':'The apparently long descender through précédentes belongs to the q in conséquence on the upper line. The lower word itself has the p beginning, low ré/cé course, d loop and t ending of précédentes. The following separate opening parenthesis and v-shaped beginning support vient; du fait continues on the next slanted line. The formula inverse strokes and closing parenthesis are visible. Between the two identities a crossed short item remains unreadable. Noter is clear; the following que is recovered in B09.'},
'B09':{'final':n['B09'],'changed':True,'adjudication':'Restore que after Noter and broaden the crossed trial expression.','ink':'Above the l0 calculation, a separate small word has a q loop and long descender followed by low u/e bodies: que. The initial crossed parenthesized expression has a sigma-like roof, rho-like loops and a raised2, but its crowded factor count permits both recorded alternatives. The subsequent live rho^-1(sigma0 rho)^2 rho and boxed five-factor result remain readable; the terminal high minus/1 belong to the final rho.'},
'B10':{'use_first':True,'adjudication':'Retain both cancelled rho fragments and uncertainty about the initial inverse in l-infinity.','ink':'The two large square exponents are distinct from the small inverse region. The latter is crossed by a thick short zigzag, favouring cancellation of -1 but not excluding a live inverse. The blind reading did not resolve that material-state ambiguity. Both rho-like cancelled letters remain qualified.'},
'B11':{'use_first':True,'adjudication':'Retain the three inner-conjugation formulas.','ink':'The first two rows have bare right-hand l-infinity and l1, with no exponents. The third contains parentheses around l0 and two separated raised-1 exponents. The independent extra margin wrapper changes excerpt scope only; the page already places these rows within the margin.'},
'B12':{'final':n['B12'],'changed':True,'adjudication':'Restore a cancelled exponent on l1 and broaden the following crossed index; retain itou.','ink':'The first right-member index has two joined low loops, with retracing, supporting infinity. Above the live l1 in the third row is a separate high crossed minus/upright cluster, compatible with a cancelled-1. The following cancelled factor’s small low loop permits infinity or0 under the hatching. The final word after et has a high t with a crossbar and low ou course, supporting itou rather than idem. No final point follows the sigma list.'},
'B13':{'use_first':True,'adjudication':'Retain the main NB wording, comma, cancelled donc and p.v./p.r. doubt.','ink':'Comme has its low c/o/m course despite the neighbouring margin. The small curved comma after rho^3=1 descends below the baseline. The struck word has d/o remnants compatible with donc. The qualifier after un mot has a v-like body but a compressed r cannot be excluded, so both alternatives remain. Three terminal points after the sigma list are visible.'},
'B14':{'use_first':True,'adjudication':'Retain live débuts and the already qualified cancelled clause and index.','ink':'Débuts lies before the long strike, with its d/b ascenders and following comma. Cancellation begins on the following si/dans clause. On the next line the word primes, conjunction et and q descender of qu’on interprète are supported. The latter reading has the p descender and tall t ending, but remains qualified. The second formula’s right index has a rho-like descender, high dot and parenthesis traces; it is not a plain i.'},
'B15':{'final':n['B15'],'changed':True,'adjudication':'Preserve the separate raised crossed line; broaden the lower phrase and final symbol.','ink':'The upper i.e. sigma_i has its own strike and lies above the lower phrase. Its stops and sigma subscript remain visible. Below, the tall t and long following descender permit de notre groupe and de sorte que; hatching prevents a secure full word sequence. The final symbol has a broad E-like body, with the cancellation supplying a possible middle stroke; sigma_i prime and sigma prime therefore remain alternatives. Its raised mark is a single prime-like stroke, not an independently established inverse.'},
'B16':{'final':n['B16'],'changed':True,'adjudication':'Remove the supplied full stop after the final inverse.','ink':'The line ends with l_i raised-1. Blank paper follows the upright1; no separate low punctuation point is visible.'},
'B17':{'final':n['B17'],'changed':True,'adjudication':'Retain dotted inverse rho in the index; reopen the high sigma mark as prime/1.','ink':'The right sigma has one high upright with a small upper flag, admitting a prime or numeral1. There is no minus at that height. The lower rho has a separate high dot and its own explicit-1 followed by(i). The prime-versus-inverse decision remains correct about the absence of an inverse, but does not rule out a numeral1.'},
'B18':{'final':n['B18'],'changed':True,'adjudication':'Retain the revision and comment; qualify the third letter in the inserted tuple.','ink':'The current main-line k has two dark arms beside the earlier long descender, whose j-like head remains doubtful. In the smaller raised tuple the third letter has a tall stem and short low return, permitting k/h. The two closing parentheses are distinct and remain. The separate et is crossed. The deleted comment retains the d-like opening and qualified dernier/devenir sequence, followed by dotted-rho index and s’en déduit par(1). The lower live action has a clear dot over rho and no terminal point.'},
'B19':{'final':n['B19'],'changed':True,'adjudication':'Reopen the short generator phrase and punctuation; retain capital L_i and the two centralizer references.','ink':'After étant the first compact word begins with a d-like loop and extends into a low nc-like course, favouring donc, followed by low un; un des remains possible at this scale. The terminal course of générateur(s) and the following du/des are not securely separated. Centralisateur and normalisateur retain singular-looking r endings; the latter has no separate s before its comma. The later L has a straight tall stem and foot without the loop of lowercase l. After E-plus the dark low mark has a small hook, admitting period/comma. Idem, le centralisateur in the next parenthesis, and the subsequent full stop are retained.'},
'B20':{'final':n['B20'],'changed':True,'adjudication':'Remove the stop after chgts and qualify the possible plural of notation.','ink':'The abbreviation ends in a connected small s-like turn followed by white space, with no separate point. Notation has its t ascenders and long final course; the short last hook could be an exit or an additional s, so singular/plural remains open. Indiqués and donnent retain their q descender, dotted i and final t.'},
'B21':{'final':n['B21'],'changed':True,'adjudication':'Separate the local cancellation layers and replacement l1; remove the misassigned final inverse.','ink':'The relation number is crossed by several long oblique strokes. Other large strokes pass through the first two left-member labels and the second row’s initial factor; their exact cancellation scope remains uncertain and is encoded locally. Both first-row high clusters are heavily crossed, admitting inverse-looking-1 or4-like remnants. The second row’s final l1^-1 has a clear long crossing stroke; a separate l with low1 is written farther right and slightly below as its replacement. That complete l1 body is not an exponent attached to the third row. The third row’s final l-infinity has no independent high inverse strokes and no cancellation crosses that entire row. A blanket whole-system deletion is therefore replaced by explicit local states and a note about uncertain overall scope.'}}
for x in r['changes']:
 bid=None
 if x['id']=='s020-02':
  for p in braces:x['final']=x['final'].replace(*p)
  x.update(c_changed=True,error_category=[1,4,5,6,7]);bid='B03'
 if x['id']=='s020-04':x.update(final=x['final'].replace(*etc),c_changed=True,error_category=[1,2,3,5,6,8,9,10]);bid='B06'
 if x['id']=='s020-06':x.update(final=newproduct,error_category=[1,3,4,5,6,7,9]);bid='B07'
 if x['id']=='s020-08':x['final']=x['final'].replace(*trial);bid='B09'
 if x['id']=='s020-12':x['final']=x['final'].replace(*nbterm);bid='B12'
 if x['id']=='s020-20':x['final']=x['final'].replace(*phrase).replace(*symbol);bid='B15'
 if x['id']=='s020-22':x.update(final=x['final'].replace(*prime),confidence='medium',math_consequence='The high mark has no minus; its distinction as prime versus numeral1 remains unresolved. The inverse dotted rho belongs to the lower index.');bid='B17'
 if x['id']=='s020-24':x.update(final=x['final'].replace(*insert),confidence='medium');bid='B18'
 if x['id']=='s020-28':x.update(final=gen[1],c_changed=True,confidence='medium');bid='B19'
 if x['id']=='s020-31':x.update(final=r'$\mathcal E^+$\unsure{.|,}',confidence='medium');bid='B19'
 if x['id']=='s020-33':x.update(final=chgts[1],c_changed=True,confidence='medium',error_category=[2,8,9,10]);bid='B20'
 if x['id']=='s020-35':x.update(final=n['B21'],c_changed=True,confidence='low');bid='B21'
 if x['id']=='s020-36':x.update(final=r'\varepsilon_\infty=l_0^{-1}\sigma_0 l_\infty',c_changed=True,h_changed=False,confidence='high',kind='text not on the page',error_category=[1,6,9],math_consequence='The apparent final inverse was the separate replacement l1 beside the preceding row; it supplies no exponent to this row.');bid='B21'
 if bid:x.update(ink=c[bid]['ink'],crop=f'crops/second_145_scan020_{bid}.png',box=b[bid])
r['changes'].extend([
 {'id':'s020-38','place':'left margin, after Noter and before l0 calculation','C':'Noter','H':'Noter','final':'Noter que','ink':c['B09']['ink'],'confidence':'high','kind':'omission','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan020_B09.png','box':b['B09'],'error_category':[2,3],'math_consequence':''},
 {'id':'s020-39','place':'end of si on y remplace line','C':stop[0],'H':stop[0],'final':stop[1],'ink':c['B16']['ink'],'confidence':'high','kind':'text not on the page','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan020_B16.png','box':b['B16'],'error_category':[9,10],'math_consequence':''},
 {'id':'s020-40','place':'system(8), global cancellation scope and second-row replacement','C':f['B21'],'H':r'\struck{(8) ... \varepsilon_1=l_\infty^{-1}\sigma_\infty l_1^{-1} ...}','final':n['B21'],'ink':c['B21']['ink'],'confidence':'low','kind':'deletion state','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan020_B21.png','box':b['B21'],'error_category':[1,3,5,6,7],'math_consequence':'The explicitly inserted l1 is associated with the second row. The overall abandonment of the proposal may be intended, but exact deletion scope is not inferred from the next page.'}])
updates={
 'Left margin, cancelled product':(newproduct,['two factor/scope alternatives reproduced in the transcription'],'B07'),
 'Left margin, cancelled first expression for l_0':(trial[1],[r'(\rho\sigma_0\rho^{-1})^2',r'(\sigma_0\rho)^2'],'B09'),
 'Right NB, crossed final term':(r'\deleted{\unsure{l_\infty^{-1}|l_0^{-1}}}',[r'l_\infty^{-1}',r'l_0^{-1}'],'B12'),
 'Cancelled phrase below i.e.':(phrase[1],['de notre groupe','de sorte que'],'B15'),
 'Cancelled final group symbol':(symbol[1],[r"\mathcal E'",r"\sigma_i'",r"\sigma'"],'B15'),
 'Relation (8), first cancelled exponent':(r'\deleted{\unsure{-1|4}}',['-1','4'],'B21'),
 'Relation (8), second cancelled exponent':(r'\deleted{\unsure{-1|4}}',['-1','4'],'B21')}
r['doubts']=[x for x in r['doubts'] if x['place']!='Relation (8), last exponent in epsilon_infinity row']
for x in r['doubts']:
 if x['place'] in updates:
  val,alts,bid=updates[x['place']];x.update(reading=val,alternatives=alts,reason=c[bid]['ink'])
for place,val,alts,bid in [
 ('Right NB, cancelled high cluster on live l1',r'\deleted{\unsure{-1}}',['-1'],'B12'),
 ('Introduction to(7), high mark on right sigma',r'\unsure{\prime|1}',[r'\prime','1'],'B17'),
 ('Inserted distinctness tuple, third letter',r'\unsure{k|h}',['k','h'],'B18'),
 ('Generator phrase after étant',gen[1],['donc un / un des; générateurs / générateur; du / des'],'B19'),
 ('Punctuation after E-plus',r'\unsure{.|,}',['.',','],'B19'),
 ('Final prose, notation singular/plural',r'\unsure{notation|notations}',['notation','notations'],'B20'),
 ('System(8), cancellation scope',n['B21'],['local states are reproduced; whole-system abandonment is possible but not imposed'],'B21')]:
 r['doubts'].append({'place':place,'reading':val,'alternatives':alts,'confidence':'low' if bid in ['B12','B21'] else 'medium','reason':c[bid]['ink']})
for x in r['decisions']:
 if x['id']=='M0841':x.update(decision='undecided',reading=prime[1],ink=c['B17']['ink'],confidence='medium',crop='crops/second_145_scan020_B17.png',box=b['B17'])
for x in r['unlisted_decisions']:
 up={'U020-01':(newproduct,'B07'),'U020-02':(trial[1],'B09'),'U020-05':(r'\deleted{\unsure{l_\infty^{-1}|l_0^{-1}}}','B12'),'U020-09':(phrase[1],'B15'),'U020-12':(r'\deleted{\unsure{-1|4}}','B21'),'U020-14':(r'\deleted{\unsure{-1|4}}','B21'),'U020-15':(r'l_\infty','B21')}
 if x['id'] in up:
  val,bid=up[x['id']];x.update(reading=val,ink=c[bid]['ink'],crop=f'crops/second_145_scan020_{bid}.png',box=b[bid])
  if x['id']=='U020-15':x.update(decision='other',confidence='high')
for x in r['inventory']:
 changes={
 'E03':('three parenthesized products, overbraces internal to parentheses',None),
 'E11':('two bracketed products, three flat annotation rules labelled sigma-infinity, sigma1, sigma-infinity; factor/scope alternatives retained',None),
 'E12':('relation(4) est conséquence ... Noter que',None),
 'E15':('(rho sigma0 rho^-1)^2 / (sigma0 rho)^2, cancelled and doubtful',None),
 'E23':('l-infinity^-1 / l0^-1, crossed and doubtful',None),
 'E30':('de notre groupe / de sorte que; E-prime / sigma_i-prime / sigma-prime, cancelled and doubtful',None),
 'E31':(prime[1],None),
 'E34':(insert[1],None),
 'E37':('On voudrait ... '+gen[1]+'; L_i; E-plus period/comma; chgts de notation/notations',None),
 'E38':(n['B21'],'display'),
 'E39':('-1 /4, doubtful and locally cancelled',None),
 'E40':('-1 /4, doubtful and locally cancelled',None)}
 if x['element'] in changes:
  val,kind=changes[x['element']];x['first_words_or_objects']=val
  if kind:x['kind']=kind;x['position']='Main bottom system(8), local revisions and uncertain overall cancellation scope'
 if x['element'] in ['E39','E40']:x['position']=x['position'].replace('Within cancelled (8)','Within revised (8)')
r['inventory'].extend([
 {'element':'E42','kind':'deletion','position':'Right NB, superscript above live l1 in third row','first_words_or_objects':r'\deleted{\unsure{-1}}','box':b['B12'],'sheet_kind':'text','hand':'his hand','transcribed':'yes'},
 {'element':'E43','kind':'insertion','position':'Right/below second row of system(8), replacing struck l1 inverse','first_words_or_objects':r'\inserted{l_1}','box':b['B21'],'sheet_kind':'text','hand':'his hand','transcribed':'yes'}])
for x in r['abbreviations']:
 if x['form']=='etc.':x.update(form='etc',place=x['place']+'; no terminal stop')
 if x['form']=='chgts.':x.update(form='chgts',place=x['place']+'; no terminal stop')
for x in r['diff_coverage']:
 cid=x.get('change_id')
 if cid in ['s020-06','s020-08','s020-12','s020-20','s020-22','s020-24','s020-28','s020-31','s020-33','s020-35','s020-36']:
  x['explanation']='See the audited final wording and state in '+cid+'. '+{'s020-06':'The whole-product doubt now also preserves three flat annotation rules.','s020-08':'The crossed trial admits two expressions; Noter que is restored separately.','s020-12':'The third row includes a cancelled exponent on l1 and a following index alternative.','s020-20':'Both phrase and final-symbol alternatives remain explicit.','s020-22':'No inverse is written above sigma; prime/numeral1 remains open, with dotted inverse rho in the index.','s020-24':'The inserted tuple has third letter k/h and retains its extra close.','s020-28':'The short generator phrase is explicitly qualified, preferring donc un.','s020-31':'The visible low punctuation is period/comma.','s020-33':'The abbreviation is chgts without stop; notation/notations remains open.','s020-35':'Local cancellation states and the second-row replacement l1 are distinguished.','s020-36':'The third row ends in bare l-infinity; the supposed exponent belongs to the second-row replacement l1.'}[cid]
r['notes']=[x.replace('The whole proposed relation (8) is cancelled, with two further local exponent cancellations. Its first-row last index and final-row exponent remain doubtful.','System(8) has a crossed number and several larger strokes whose exact scope is uncertain, together with local exponent cancellations. The second row’s crossed final l1 inverse is replaced by a separate l1 to the right/below. The third row ends in bare l-infinity. Its first-row last index remains doubtful.').replace('The inventory explicitly accounts for every one of C’s 19 deleted spans and both inserted spans, plus the newly uncertain exponent-cancellation state.','The inventory accounts for every span marked by C and for the newly identified local exponent and replacement layers; C’s blanket system(8) deletion is qualified in the audit.').replace('the sigma_infinity underbrace endpoint','the sigma_infinity annotation endpoint').replace('the second underbrace endpoint','the final flat-bracket endpoint') for x in r['notes']]
r['notes'].append('The blind audit restores Noter que and the first sigma-infinity annotation beneath the crossed marginal product; all three annotation rules there are flat brackets. In(4) the overbraces lie inside the parentheses. The right NB includes a cancelled inverse-looking cluster above live l1. Local doubts now include two crossed prose phrases, the high prime/1 on sigma before(7), the inserted tuple’s k/h, and the generator phrase preferring donc un. Chgts and etc lack final stops, and the si on y remplace line has no final point. System(8) is not uniformly struck at every visible component: its number is crossed, several local cancellation scopes are uncertain, and the second-row l1 replacement is distinct from the third row. The mathematical certificates use only the explicitly stated live words and conditional exponent choice; no computation selects the newly uncertain letters or the cancellation scope. No new check event is claimed.')
r['hand'].append('Blind audit: large cancellation strokes must be distinguished from local replacements. A low replacement l1 at the end of the second row can be mistaken for a high exponent on the next row. In the slanted margin, descenders from an upper line cross a lower word and must not be reassigned to that word. Braces in(4) end inside the parentheses; the smaller cancelled product has three flat labelled rules.')
write_adjudication(20,'/root/reader_c',c,edits,report_replace={k:r[k] for k in ['changes','doubts','decisions','unlisted_decisions','inventory','abbreviations','diff_coverage','notes','hand']})
