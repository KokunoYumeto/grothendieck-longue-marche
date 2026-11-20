from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan003_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan003_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan003_boxes.tsv')}
dot=r'\unsure{\cdot|=}'
sigma=r'\unsure{\sigma_0|\sigma_0\prime|\dot\sigma_0}'
# A prime is serialized with the edition's ordinary prime convention.
sigma=r"\unsure{\sigma_0|\sigma_0'|\dot\sigma_0}"
oldfactor=r'\deleted{\unsure{l_1^\mu}}';newfactor=r'\deleted{\unsure{l_1^\mu|h_1}}'
oldgamma=r"\unsure{\gamma'|\gamma-\mu}";newgamma=r"\unsure{\gamma'|\gamma-\mu|\gamma}"
oldrho=r'\rho^{\unsure{\deleted{-1}|-1|1}}'
newrho=r'\unsure{\rho^{\deleted{\unsure{-1}}}|\rho^{-1}|\rho^1|\hat\rho}'
oldint=r'\operatorname{int}(h_1)';newint=r'\unsure{\operatorname{int}(h_1)|\operatorname{int}h_1}'
arrow=r'\figure{\begin{tikzpicture}[baseline]\draw[->] (0,0.7)--(0,0);\draw (-0.1,0.7)--(0.1,0.7);\end{tikzpicture}}'
new14=f['B14'].replace(oldfactor,newfactor).replace(oldgamma,newgamma).replace(oldrho,newrho).replace(r"({h_1'}^{-1})",r"(h_1')^{-1}")
c={
'B01':{'use_first':True,'adjudication':'Retain à lacets, the capital indexed Pi, equality and small unindexed pi; preserve the cancelled-word doubt.','ink':'The raised insertion has the long l and t strokes and terminal s of à lacets, not the short int sequence. The left group sign has two upright legs; the right has a short curved foot. The upper equality stroke has an entry hook but does not independently establish a tilde. The dark cancelled knot remains unreadable in full.'},
'B02':{'use_first':True,'adjudication':'Same reading with math delimiters added by the blind reader.','ink':'The first argument index is a black teardrop permitting 1 or 0. The following g1, target l1 and raised p agree. No doubt is resolved by the matching target.'},
'B03':{'use_first':True,'adjudication':'Retain the first complete formula; the page already supplies the margin wrapper.','ink':'The last l has a tall loop, a round lower0 and a detached raised p, including near the crop border. The brace, its g0 label and the negative gamma exponent are visible. The second reader’s added doubt on the final target is unnecessary.'},
'B04':{'use_first':True,'adjudication':'Retain et barred-m pas and the separately underlined u with exclamation.','ink':'After the barred double-curved m, the word has the descending p, small a and final s downturns. It lacks a separate u/r sequence supporting pour. The two underlines are distinct.'},
'B05':{'use_first':True,'adjudication':'Equivalent math delimiters only.','ink':'The complete boxed relation has the three l powers, both inner-automorphism expressions and the closing equals1. All indices, gamma signs and inverse on rho agree.'},
'B06':{'final':f['B06'].replace(r'\cdot',dot),'changed':True,'adjudication':'Keep multiplication as the preferred reading, but mark the short mark versus equality uncertain.','ink':'One dark compact horizontal mark lies between l-infinity to minus-gamma and h1. A paler short parallel trace lies underneath. The final equals sign has two dark strokes; here the lower trace cannot securely be assigned to writing rather than paper. The whole relation was reread.'},
'B07':{'use_first':True,'adjudication':'Retain the existing equality/inequality doubt and readable passer.','ink':'The comparison sign remains crowded and oblique. Passer has a descending p followed by compressed a/ss/e/r joins, and the small ab is visible below the group parenthesis. The second uncertainty wrapper changes scope, not the surviving letters.'},
'B08':{'final':f['B08'].replace(r'\sigma_0',sigma),'changed':True,'adjudication':'Retain ordinary sigma-zero first, with prime and dotted alternatives for the tiny upper mark.','ink':'A tiny dark tick or point occurs at the upper right of sigma beyond its roof. It could be a prime, a point, or the end of its entry stroke; the crop does not securely distinguish them. The lower0 and the remaining inverse-product definition agree.'},
'B09':{'use_first':True,'adjudication':'Keep both alternatives for the cancelled exponent preceding beta.','ink':'The old exponent is a black crossed loop immediately before a clear beta. The cancellation does not recover enough of its contour to exclude alpha in favour of gamma. All surrounding factors agree.'},
'B10':{'final':f['B10']+' '+arrow,'changed':True,'adjudication':'Retain récrire and add the omitted downward arrow with its short top bar.','ink':'The word lacks the tall d needed for réduire and has the repeated low r/i joins of récrire. To its right a separate short horizontal top bar meets a descending shaft, whose lower point reaches the upper rule of the next boxed formula. This is a drawing separate from the letters.'},
'B11':{'final':f['B11'].replace(oldint,newint),'changed':True,'adjudication':'Retain parenthesized int(h1) first, but mark the crowded parenthesis boundary locally uncertain.','ink':'At the junction after int, the terminal t stroke, opening curve and h stem touch. The closing curve after h1 and the following l1 argument are present. The crop does not fully separate an opening argument parenthesis from the neighbouring letter stroke.'},
'B12':{'use_first':True,'adjudication':'Prime serialization only.','ink':'A detached short raised prime is visible beside h1; writing it with an apostrophe or a prime command denotes the same ink.'},
'B14':{'final':new14,'changed':True,'adjudication':'Move the final inverse outside the h1-prime closing parenthesis; broaden only the genuinely overwritten alternatives.','ink':'The clear closing curve after h1-prime stands to the left of the raised minus1, followed by the outer int closing curve. Both first witnesses had put this inverse inside the inner parenthesis. The cancelled earlier factor has intersecting tall strokes admitting l1-to-mu or h1. The gamma cluster admits an unprimed gamma as well as the previous alternatives. Above rho the black roof can be a cancelled inverse or a hat; neither the old glyph nor its state is secure. The saved full-formula crop confirms the same placement.'},
'B15':{'use_first':True,'adjudication':'Retain the singular relation, correspondante, reference (2) subscript2 and the existing cancelled-text doubts.','ink':'Et on a la relation has a separate small la and one singular word. Correspondante ends in t/e joins. A tiny2 sits low to the right of the parenthesized2. The old beta is dark beneath the live beta-prime; the cancelled additive term does not securely exclude a2 before mu. The existing à/colon doubt remains.'},
'B17':{'use_first':True,'adjudication':'Same formula with explicit math delimiters in the second reading.','ink':'The underbrace spans sigma0(g1), with g-infinity beneath its cusp. Both readings give the visible u(l-infinity), int and final l-infinity to p.'},
'B18':{'final':f['B18'].replace(r'\in\pi',r'\in\Pi'),'changed':True,'adjudication':'Read capital Pi in this membership statement; retain où.','ink':'The group sign has a detached flat cap and two short straight upright legs without the curved right foot of the small pi in the opening identification. After the opening parenthesis, the low joined o/u and detached grave support où. There is no i/c/i sequence. The following beta, gamma, hatted Z and g1,p agree.'},
'B19':{'use_first':True,'adjudication':'Prime commands and whitespace around the final colon only.','ink':'Each replacement formula has a separate high prime. The paragraph ends with two vertically aligned dark points after the int expression. En, the negative mu and the order of factors agree; the lower display is adjudicated separately in B14.'}}
for x in r['changes']:
 if x['id']=='s003-07':x['final']=x['final'].replace(r'\sigma_0',sigma)
 if x['id']=='s003-15':x.update(final=newfactor,ink=c['B14']['ink'],crop='crops/second_145_scan003_B14.png',box=b['B14'])
 if x['id']=='s003-16':x.update(final=newrho,ink=c['B14']['ink'],crop='crops/second_145_scan003_B14.png',box=b['B14'])
for ident,place,C,H,final,box,kind,cats,conf,consequence in [
 ('s003-22','downward drawing between récrire and relation (1-prime)','absent','absent',arrow,'B10','drawing or diagram',[3,4],'high',''),
 ('s003-23','last display, inverse on the value of rho',r"\rho^{\unsure{1|-1}}({h_1'}^{-1})",r"\rho^{-1}(h_1'^{-1})",newrho+r"(h_1')^{-1}",'B14','misread symbol or index',[1],'high','The inverse is written after the inner closing parenthesis. Its position is preserved even though an automorphism commutes with taking an inverse.'),
 ('s003-24','parameter paragraph, group containing g-one',r'g_1\in\pi\bmod L_1',r'g_1 \in \pi \bmod L_1',r'g_1\in\Pi\bmod L_1','B18','misread symbol or index',[1],'high','The written group sign is capital Pi in this clause; the small pi of the opening identification is not globally replaced.')]:
 r['changes'].append({'id':ident,'place':place,'C':C,'H':H,'final':final,'ink':c[box]['ink'],'confidence':conf,'kind':kind,'c_changed':True,'h_changed':True,'marked_in_H':'no','crop':f'crops/second_145_scan003_{box}.png','box':b[box],'error_category':cats,'math_consequence':consequence})
for x in r['doubts']:
 if x['reading']==oldfactor:x.update(reading=newfactor,alternatives=[r'l_1^\mu',r'h_1'],reason=c['B14']['ink'])
 if x['reading']==oldgamma:x.update(reading=newgamma,alternatives=[r"\gamma'",r'\gamma-\mu',r'\gamma'],reason=c['B14']['ink'])
 if x['place']=='last display, rho superscript':x.update(reading=newrho,alternatives=[r'\rho^{\deleted{\unsure{-1}}}',r'\rho^{-1}',r'\rho^1',r'\hat\rho'],reason=c['B14']['ink'])
for place,reading,alts,box in [
 ('boxed relation (2), mark before h-one',dot,[r'\cdot','='],'B06'),
 ('definition of h-one, upper mark on sigma',sigma,[r'\sigma_0',r"\sigma_0'",r'\dot\sigma_0'],'B08'),
 ('boxed relation (1-prime), first inner-automorphism argument boundary',newint,[oldint,r'\operatorname{int}h_1'],'B11')]:
 r['doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':c[box]['ink']})
for x in r['decisions']:
 if x['id']=='M0763':x.update(reading=newgamma,ink=c['B14']['ink'],crop='crops/second_145_scan003_B14.png',box=b['B14'])
 if x['id']=='M0764':x.update(reading=newrho,ink=c['B14']['ink'],crop='crops/second_145_scan003_B14.png',box=b['B14'])
for x in r['inventory']:
 if x['element']=='T02':x['first_words_or_objects']=x['first_words_or_objects'].replace('∈ π','∈ Π')
 if x['element']=='D04':x['first_words_or_objects']=newfactor
 if x['element']=='D05':x['first_words_or_objects']=newrho
r['inventory'].insert(next(i for i,x in enumerate(r['inventory']) if x['element']=='F07'),{'element':'DR01','kind':'drawing','position':'right of récrire, pointing down to the top rule of (1-prime)','first_words_or_objects':'downward arrow with a short transverse top bar','box':b['B10'],'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
r['notes']=[x.replace('Equation (2) has','Under the preferred product reading of the short mark in (2), that equation has').replace('Abelianizing (2) gives','Under that same product reading, abelianizing (2) gives') for x in r['notes']]
r['notes'].append('The independent blind audit recovers a small downward arrow with a transverse top bar between the prose récrire and (1′), capital Pi in g1∈Pi mod L1, and the placement rho(h1′)^(−1) with the inverse outside the inner parenthesis. The inverse placement is a diplomatic correction, not a different group identity. The audit also preserves local uncertainty in a short multiplication/equality mark, the small upper mark on sigma, the crowded int argument boundary and the overwritten last display. The two local algebra checks above are conditional on the preferred product reading and do not identify that pale mark. No additional mathematical result is claimed from the audit.')
r['hand'].append('Blind audit: a straight two-legged capital Pi occurs in the parameter paragraph, whereas the small pi after the opening equality has a curved right foot. Both witnesses had regularized the former to lowercase. In the final formula a raised minus1 lies after the inner closing curve; its placement must not be moved inside merely because the resulting group elements are equal. A short top-barred downward arrow, absent from both witnesses, connects the rewriting prose with the next box.')
page_edits=[
 {'old':r'l_\infty^{-\gamma}\cdot h_1','new':r'l_\infty^{-\gamma}'+dot+r' h_1'},
 {'old':r'h_1=\sigma_0(g_1)^{-1}g_1','new':'h_1='+sigma+r'(g_1)^{-1}g_1'},
 {'old':f['B10'],'new':f['B10']+'\n'+arrow},
 {'old':r"(1')\qquad\boxed{l_\infty^{p}\cdot\operatorname{int}(h_1)",'new':r"(1')\qquad\boxed{l_\infty^{p}\cdot"+newint},
 {'old':oldfactor,'new':newfactor},{'old':oldgamma,'new':newgamma},{'old':oldrho,'new':newrho},
 {'old':r"({h_1'}^{-1})",'new':r"(h_1')^{-1}"},
 {'old':r'g_1\in\pi\bmod L_1','new':r'g_1\in\Pi\bmod L_1'}]
write_adjudication(3,'/root/reader_b',c,page_edits,report_replace={k:r[k] for k in ['changes','doubts','decisions','inventory','notes','hand']})
