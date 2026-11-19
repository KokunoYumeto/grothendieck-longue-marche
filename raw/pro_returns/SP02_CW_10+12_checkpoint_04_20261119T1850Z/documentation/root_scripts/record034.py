import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-01',10,34)
r.edit(r'\unsure{0|O}_{\mathrm{III}}',r'0_{\mathrm{III}}')
added=r'''
% Cancelled text visible through the pasted lower strip. The last line is
% read after vertical reflection; the other lines remain in the scan orientation.
\deleted{\unsure{10.4. Soit} $\unsure{\mathbb{P}}$ \unsure{l'une des propriétés} \illegible{5} \unsure{de préschémas en groupes} \illegible{1}}

\deleted{\unsure{(ii)|(i)} être un monomorphisme, \unsure{(i.e.} $\unsure{G}$ \illegible{7} $\unsure{H}$\unsure{)}}

\deleted{\unsure{(iii)|(ii)} être une immersion \unsure{(i.e.} $\unsure{G}$ \unsure{est un sous-préschéma en groupes de} $\unsure{H}$\unsure{)}}

\deleted{\unsure{(iv)|(iii)} être une immersion fermée \unsure{(i.e.} $G$ est un sous-préschéma en groupes fermé}
'''
# Append through a unique final anchor, preserving the page's first-pass text.
a=r'donnée en (EGA $\unsure{0|O}_{\mathrm{III}}$ 8.2.5 et 8.2.6).'
b=r'donnée en (EGA $0_{\mathrm{III}}$ 8.2.5 et 8.2.6).'
r.edit(b,b+'\n'+added)
ch=r.change
ch('top centre','2','omitted','2','Handwritten numeral 2 at page head.','whole','omission')
ch('upper paragraph after ainsi',r'\deleted{\unsure{pour}}',r'\struck{\ill{}}',r'\deleted{\unsure{pour}}','p descender and several surviving typed letter parts support pour; overstrike prevents certainty.','upper','readable ink left as \\ill{}','medium',False,True,True)
ch('upper paragraph covering criterion','underlined phrase','no underline','underlined phrase','Pencil rules run from dans le cas through présentation finie.','upper','omission')
ch('before fidèlement',r'\unsure{/|f}','omitted',r'\unsure{/|f}','Separate dark oblique mark stands before typed f; slash or letter remains uncertain.','upper','omission','low')
ch('after Exp. IV 6.3.1 (i)',r'\deleted{,}','omitted',r'\deleted{,}','Comma-shaped type is inked over immediately after closing parentheses.','upper','omission')
ch('10.2 number','handwritten 2','struck 1 then added 2','handwritten 2','The visible digit has a curved/diagonal descent and horizontal foot; an underlying separate 1 cannot be recovered.','heading-2','text not on the page','medium')
ch('between 10.2 and Dans',r'\deleted{\unsure{a)}}','omitted',r'\deleted{\unsure{a)}}','A separately cancelled old label sits after the point, not at the place of the new 2.','heading-2','omission','low')
ch('10.2 after soient',r'\deleted{\unsure{pour}}',r'\struck{\ill{}}',r'\deleted{\unsure{pour}}','Four-letter typed cluster with initial p remains partly visible under hatching.','10-2','readable ink left as \\ill{}','medium',False,True,True)
ch('10.2 j comparison',r'j\leqq i',r'j\leqslant i',r'j\leqq i','Left angle has two separate horizontal lower bars.','10-2','misread symbol or index')
ch('10.2 before H_i',r'\deleted{\unsure{G}}','omitted',r'\deleted{\unsure{G}}','Small blackened round capital precedes H_i; candidate G retained with doubt.','10-2','omission','low')
ch('10.2 first Hom base',r'\mathbb{S}_i',r'S_i',r'\mathbb{S}_i','Offset doubled typewriter S produces two outlines, unlike the single S in the following Hom base.','10-2','misread symbol or index')
ch('10.2 assertion','underlined','no underline','underlined','Four pencil rules under all assertion lines.','10-2','omission')
ch('10.3 number','handwritten 3','struck 2 then added 3','handwritten 3','Visible new digit is 3; no separately recoverable deleted 2 at this position.','heading-3','text not on the page','medium')
ch('between 10.3 and Dans',r'\deleted{\unsure{b)}}','omitted',r'\deleted{\unsure{b)}}','Old label is separately hatched to right of new heading; final parenthesis visible.','heading-3','omission','low')
ch('10.3 after présentation',r'\deleted{f}','omitted',r'\deleted{f}','Cancelled single typewriter f at right edge, with ascender and crossbar.','f-struck','omission')
ch('10.3 assertion','underlined','no underline','underlined','Rules below each of the three lines.','10-3','omission')
ch('proof first assertion number',r'\unsure{2|1}','struck 1 then added 2',r'\unsure{2|1}','Dark digit has a narrow bend and foot; cannot separate a deleted earlier digit from the live form.','first-ref','deletion state (struck given live or live given struck)','medium')
ch('proof second assertion number','handwritten 3','struck 2 then added 3','handwritten 3','New 3 present; independently readable cancelled 2 not discernible.','proof','text not on the page','medium')
ch('proof cancelled citation','(EGA IV 8.8.2 et 8.8.3)','EGA IV 8.8.2 et 8.8.3','(EGA IV 8.8.2 et 8.8.3)','Opening and closing parentheses belong to cancelled reference.','proof','omission')
ch('proof added citation','(10.0) et (10.1),','(10.0) et (10.1)','(10.0) et (10.1),','Comma after handwritten closing parenthesis at right.','proof','omission')
ch('last EGA reference',r'\unsure{0|O}_{III}','0_{III}','0_{III}','Tall narrow typewriter oval agrees with 0 of 10.0; capital O is wider elsewhere on these typescripts.','proof','other','high',True,False)
for label,text,crop in [('covered heading',added.split('\n')[3],'strip-head-L; strip-head-R'),('covered monomorphism item',added.split('\n')[5],'strip-i-L; strip-i-R'),('covered immersion item',added.split('\n')[7],'strip-ii-L; strip-ii-R'),('covered closed immersion item',added.split('\n')[9],'under-strip-flip')]:
 ch('pasted lower strip: '+label,'omitted','description only; text omitted',text,'Faint typed text and large diagonal cancellations are visible through the strip; unreadable areas explicitly marked, no reconstruction from mathematical expectation.',crop,'omission','low',True,True)
 r.r['inventory_extra'].append({'scan':'10:034','sheet_kind':'cancelled_draft','hand':'typewriter','element':label,'kind':'deletion','position':'bottom beneath pasted strip','first_words_or_objects':text,'transcribed':'yes'})
for line,reading,alt,conf in [('after ainsi','deleted pour','','medium'),('before fidèlement','/','f','low'),('old first label','a)','','low'),('after soient','deleted pour','','medium'),('before H_i','deleted G','','low'),('old second label','b)','','low'),('before S-isomorphisme','one illegible deleted word','','low'),('first assertion reference','2','1','medium'),('lower covered strip','four cancelled text elements with in-place doubts and illegible word counts','physically obscured text; last line read with vertical reflection','low')]:r.doubt(line,reading,alt,conf)
r.r['crops']=json.loads(Path('work/crops034.json').read_text())
for name,b in [('heading-2',[312,959,459,1020]),('heading-3',[310,1260,466,1321]),('first-ref',[589,1536,679,1604]),('f-struck',[1565,1337,1631,1385])]:r.crop(name,b,scale=5)
for name,b in [('strip-head-L',[295,1781,970,1889]),('strip-head-R',[945,1781,1660,1889]),('strip-i-L',[350,1897,990,1970]),('strip-i-R',[950,1897,1660,1970]),('strip-ii-L',[350,1976,990,2041]),('strip-ii-R',[960,1976,1660,2041])]:r.crop(name,b,autocontrast=2)
r.crop('under-strip-flip',[290,1773,1660,2140],flip='vertical',autocontrast=2)
r.notation('left comparison',r'\leqq','10/034 §10.2 confirms angle plus TWO lower bars')
r.notation('doubled typewriter S',r'\mathbb{S}','10/034 §10.2 first Hom base: displaced double impression')
r.r['inspection_note']='Whole, a, b viewed; all paragraphs/formulas/edits checked; all C doubts revisited in crops. Additional faint cancelled text under pasted strip inspected upright, rotated, reflected, enlarged, and contrast-remapped; transcribed only recoverable parts with remaining doubt. No mathematical proof checking.'
r.save('work/record034.json')
