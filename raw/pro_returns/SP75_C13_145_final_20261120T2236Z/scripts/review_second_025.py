from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan025_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan025_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan025_boxes.tsv')}
n=dict(f)
oldalpha=r'\unsure{\alpha_i}';newalpha=r'\unsure{\alpha_i|\beta_i}'
oldcross=r'\deleted{\unsure{par le couple|par le groupe}}'
newcross=r'\deleted{\unsure{par le couple|par les couples|par le groupe}}'
oldphrase=oldcross+r' groupe des\unsure{.}'
mark=r'''\begin{tikzpicture}[x=0.09cm,y=0.09cm,baseline=0ex]
\draw[line width=0.35pt] (0.45,0) .. controls (0.4,0.65) and (0.05,1.3) .. (0.02,1.05) .. controls (-0.05,0.65) and (0.5,0.35) .. (0.75,0.55) -- (1.15,1.1) -- (1.3,1.0);
\end{tikzpicture}'''
newdes=r'$\overset{\text{'+mark+r'}}{\text{des}}$'
newword=r'\unsure{groupe|formé|formée}'
newphrase=newcross+' '+newword+' '+newdes+r'\unsure{.}'
oldbase=next(x['final'] for x in r['changes'] if x['id']=='s025-16')
newbase=oldbase.replace(r'\cdot',r'\unsure{\cdot|:}')
oldlive=r'\tilde v(\gamma_i(\tilde u)\gamma_i(\tilde v)'
newlive=r'\tilde v(\gamma_i(\tilde u)\gamma_i\unsure{(}\tilde v)'
oldbr=r'\Pi^{\unsure{[0,1,\infty]|\{0,1,\infty\}}}'
newbr=r'\Pi^{[0,1,\infty]}'
olddomain=r'S\overset{\unsure{\sim|\deleted{\sim}}}{\widehat{\widehat{\mathcal E}}}^!\longrightarrow'
newdomain=olddomain.replace('^!','')
n['B01']=f['B01'].replace(oldalpha,newalpha)
n['B05']=f['B05'].replace(oldphrase,newphrase)
n['B07']=f['B07'].replace('et on aura',r'et on aura\unsure{:}')
n['B08']=f['B08'].replace(oldbase,newbase).replace(oldlive,newlive)
n['B10']=f['B10'].replace(oldbr,newbr)
n['B11']=f['B11'].replace(olddomain,newdomain)
c={
'B01':{'final':n['B01'],'changed':True,'adjudication':'Retain header11 as pagination, not primes on g_i; broaden the retraced exponent to alpha_i/beta_i.','ink':'The two upright strokes above g_i occupy the separate header position and have the spacing and height of11; they are not attached primes. Multiplication is a long low connected word after défini with no extra à. The exponent over l_i has a dense double-loop remnant and a separate small index. The nearby parenthetical alpha_i is clearer, but does not resolve whether the retraced exponent is alpha or beta, so both remain possible. The visible gauche and él. are unchanged.'},
'B02':{'use_first':True,'adjudication':'Retain gardant p, et en and its doubtful final hook.','ink':'The scalar has a straight descending stem and small upper right head, the same p form as on024, rather than a rounded rho loop. Gardant p, et en lies above the baseline en remplaçant, with a curved attachment line. The short detached hook after en is visible but still not securely a comma. Both successive g descenders in gg_i are distinct.'},
'B03':{'use_first':True,'adjudication':'Retain the six local scalar letters and the four preliminary inverse-state doubts; do not supply a multiplication dot before v(l_i).','ink':'The p powers have straight stems and small upper heads, while q has a round closed head and descending right stroke. Each inverse position is a dark angular cluster with extra strokes that favor cancellation but obscure the original minus/1. The isolated short dark mark below the first v of the final factor is below that letter, not at the inter-factor position of a centred multiplication dot. No new product sign is established. DonC is written as donc on the following line; no punctuation is supplied from spacing macros.'},
'B04':{'use_first':True,'adjudication':'Retain the complete qualified upper cancellation, straight supporting bar and uncertain main inverse marks.','ink':'Repeated diagonal hatching crosses the upper expression, including the initial h-like stem and tiny exponent, so the whole old expression remains qualified. Its lower support is horizontal with a short downturned left end and a pointed thickening at right; it is not a curly brace. The main v(g_i)h_i factors remain live. Their two raised dark marks retain both glyph and state uncertainty, and the final exponent is pq.'},
'B05':{'final':n['B05'],'changed':True,'adjudication':'Reopen the live groupe/formé/formée word, admit the plural reading in the cancellation, and reproduce the small looped mark above des.','ink':'The live word’s long initial loop can be read as the earlier g or as an f-like entry; its pale later downstroke and compressed ending do not securely distinguish groupe, formé and formée. The crossed preceding phrase exposes par and a short le/les run, while the old noun’s ending is under the strike, allowing the second reader’s plural couples without resolving it. Above des is a separate dark loop rising at left and turning up to the right with a short lower stem; its shape is drawn without assigning it a letter or a mathematical function. The extension prefix is a broad plain S, and the separate wave above two hats remains locally qualified.'},
'B06':{'use_first':True,'adjudication':'Retain via(21), l’isomorphisme, structure à lacets and p étant.','ink':'The raised short word has the low v, tiny dotted i course and final a before(21); its guide bends down before l’isomorphisme. The baseline word has l/apostrophe, a low iso course and the long p stem. After structure the small accented à is followed by a high l and the a/c/e/t/s course of lacets, not a separate le mot phrase. In the parenthesis the word after p contains the longer t/a/n/t run of étant. The upper wave on the S-extension remains separate from its two hats.'},
'B07':{'final':n['B07'],'changed':True,'adjudication':'Retain the crossed E-like sign, capital Pi and barred mapping arrow; add the qualified colon after aura.','ink':'The crossed sign has rounded stacked turns beneath oblique scribble, supporting but not resolving E. The next group has a separate hat, cap and two full legs. The map has a short vertical left bar and a right arrowhead, with gamma_i above. After the final a of aura there are two compact dark marks at different heights in the punctuation position; these are recorded as a doubtful colon.'},
'B08':{'final':n['B08'],'changed':True,'adjudication':'Retain all three correction layers, qualify the old dot/colon separator and the weak opening before the final tilded v.','ink':'The baseline right member is crossed by one continuous stroke. Its central separator has a low point and a second short dark trace above, so dot and colon remain possible under the cancellation. The upper-left trial is independently hatched, and the upper-right expression survives beside a curved attachment line. Only one clear close follows each tilded variable. The stroke before the last tilded v is narrow and partly joined to the adjacent gamma course; its reading as an opening parenthesis is now qualified. The preferred literal expression still has an unmatched outer opening; no balancing close is inserted.'},
'B09':{'use_first':True,'adjudication':'Retain the insertion above the old group, produit du groupe, opposé au groupe and unadorned lower-case pi.','ink':'The replacement group begins S above the struck group and has its own wave, two hats and raised exclamation. The old target phrase exposes a descending g-like loop and a later p stroke, which favor produit du groupe over direct, but the hatching keeps the phrase doubtful. The live opposé au groupe sits above it. The final pi is smaller than the marginal capital Pi and has a curved right foot; no hat is present. The small à belongs at the upper end before the following valeurs line, not an omitted grammatical repair.'},
'B10':{'final':n['B10'],'changed':True,'adjudication':'Resolve the marginal exponent delimiters as square brackets; retain p and capital Systèmes.','ink':'The left delimiter is a straight heavy vertical with short inward top and bottom feet; the right has the corresponding straight wall and inward ends, without a middle waist. These are square brackets around0,1,infinity. The group itself is an unhatted capital Pi with two long posts. The tuple begins with the same straight-stem p, and Systèmes begins with a larger initial S. The NB underline is independent; the group before a été has two hats and a raised exclamation but no extra wave.'},
'B11':{'final':n['B11'],'changed':True,'adjudication':'Omit the unwritten exclamation on the map domain alone; retain the target’s exclamation and all final-factor doubts.','ink':'The first S-extension in Le sous-groupe de has a visible raised upright and dot. In the separate domain immediately before the arrow, the two hats and qualified upper remnant are present but the area to their right has no comparable upright-and-dot sign before the arrow. The Aut ext target does have a distinct raised exclamation farther right. The product subscript has the small i, membership curve and0,1,infinity sequence. The rightmost Z-like factor is retraced and clipped, so its exponent and lower residual strokes remain unresolved. Footer24 has a curved2 and angular4.'}}
for x in r['changes']:
 if x['id']=='s025-12':x.update(place='Definition, crossed words after définie and following live word',final=newcross+' '+newword,ink=c['B05']['ink'],confidence='low',crop='crops/second_145_scan025_B05.png',box=b['B05'])
 if x['id']=='s025-16':x.update(final=newbase,ink=c['B08']['ink'],crop='crops/second_145_scan025_B08.png',box=b['B08'])
 if x['id']=='s025-18':x.update(final=newlive,ink=c['B08']['ink'],confidence='medium',crop='crops/second_145_scan025_B08.png',box=b['B08'])
 if x['id']=='s025-23':x.update(final=x['final'].replace(oldbr,newbr),ink=c['B10']['ink'],confidence='high',crop='crops/second_145_scan025_B10.png',box=b['B10'])
 if x['id']=='s025-26':x['final']=x['final'].removesuffix('^!')
r['changes'].extend([
 {'id':'s025-30','place':'Right of gamma mapping, after aura','C':'et on aura','H':'et on aura','final':r'et on aura\unsure{:}','ink':c['B07']['ink'],'confidence':'medium','kind':'omission','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan025_B07.png','box':b['B07'],'error_category':[3,10],'math_consequence':''},
 {'id':'s025-31','place':'Definition, small mark immediately above des','C':'des','H':'des','final':newdes,'ink':c['B05']['ink'],'confidence':'medium','kind':'drawing or diagram','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan025_B05.png','box':b['B05'],'error_category':[3,4],'math_consequence':''},
 {'id':'s025-32','place':'Final kernel map, domain immediately before arrow','C':r'S\widehat{\widehat{\mathcal E}}^!\longrightarrow','H':r'S\hat{\hat{\mathcal E}}^!\to','final':newdomain,'ink':c['B11']['ink'],'confidence':'high','kind':'text not on the page','c_changed':True,'h_changed':True,'marked_in_H':'no','crop':'crops/second_145_scan025_B11.png','box':b['B11'],'error_category':[1,9],'math_consequence':'The domain is transcribed without the exclamation that is visible on the preceding group and on the map target; no mathematical completion is supplied.'}])
for x in r['decisions']:
 if x['id']=='M0864':x.update(decision='undecided',reading=newword,ink=c['B05']['ink'],confidence='low',crop='crops/second_145_scan025_B05.png',box=b['B05'])
 if x['id']=='M0865':x.update(decision='undecided',reading=newlive,ink=c['B08']['ink'],confidence='medium',crop='crops/second_145_scan025_B08.png',box=b['B08'])
for x in r['unlisted_decisions']:
 if x['id']=='U025-08':x.update(reading=newcross,ink=c['B05']['ink'],crop='crops/second_145_scan025_B05.png',box=b['B05'])
 if x['id']=='U025-10':x.update(reading=newbase,ink=c['B08']['ink'],crop='crops/second_145_scan025_B08.png',box=b['B08'])
r['unlisted_decisions'].append({'id':'U025-14','decision':'first','reading':r'[0,1,\infty]','ink':c['B10']['ink'],'crop':'crops/second_145_scan025_B10.png','box':b['B10'],'confidence':'high','source':'Doubt introduced in the first consolidated reading, not an indexed C mark'})
for x in r['doubts']:
 if x['place']=='U025-08':x.update(reading=newcross,alternatives=['par le couple','par les couples','par le groupe'],reason=c['B05']['ink'])
 if x['place']=='U025-10':x.update(reading=newbase,alternatives=[newbase,'obscured inner letter and dot/colon separator'],reason=c['B08']['ink'])
 if x['place']=='Opening, exponent of l_i':x.update(reading=newalpha,alternatives=[r'\alpha_i',r'\beta_i'],reason=c['B01']['ink'])
r['doubts']=[x for x in r['doubts'] if x['place']!='NB tuple, exponent delimiters on Pi']
r['doubts'].extend([
 {'place':'M0864, live word after the crossed definition phrase','reading':newword,'alternatives':['groupe','formé','formée'],'confidence':'low','reason':c['B05']['ink']},
 {'place':'M0865, opening before last tilded v in surviving(24)','reading':newlive,'alternatives':[oldlive,r'\tilde v(\gamma_i(\tilde u)\gamma_i\tilde v)'],'confidence':'medium','reason':c['B08']['ink']},
 {'place':'After et on aura','reading':r'\unsure{:}','alternatives':['colon','two adjacent small pen traces'],'confidence':'medium','reason':c['B07']['ink']}])
for x in r['inventory']:
 x['first_words_or_objects']=x['first_words_or_objects'].replace(oldcross,newcross).replace(oldbase,newbase).replace(oldlive,newlive)
 if x['element']=='I27':x['first_words_or_objects']=r'et on aura\unsure{:}'
idx=next(i for i,x in enumerate(r['inventory']) if x['element']=='I21')
r['inventory'].insert(idx,{'element':'I46','kind':'drawing','position':'Small separate looped mark above des in definition','first_words_or_objects':mark,'box':b['B05'],'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
r['notation'][4]='The surviving(24) has one clear close after each tilded variable. The weak opening before the last tilded v remains qualified; the preferred first reading still leaves the outer opening unmatched. No parenthesis is added to match the cocycle interpretation.'
r['notation'][5]='The margin Pi exponent has straight square brackets, resolved on the blind crop. The final Z-like factor and exponent remain retraced and edge-crowded; separate small lower traces are reproduced without assigning a subscript.'
r['notation'].append('The final kernel-map domain lacks the exclamation present on the preceding S-extension and on the Aut ext target. The local absence is preserved; it is not regularized from the group’s repeated name.')
r['notes'][0]=r['notes'][0].replace('The alpha_i exponent is retraced and remains doubtful.','The exponent is retraced and remains alpha_i/beta_i; the clear later alpha_i does not settle its earlier layer.')
r['notes'][2]=r['notes'][2].replace('After a crossed phrase the live word is groupe.','After a crossed phrase the live word remains groupe/formé/formée. A separate small looped mark above des is reproduced graphically.')
r['notes'][3]=r['notes'][3].replace('The surviving expression literally lacks an outer closing parenthesis.','The preferred surviving expression lacks an outer closing parenthesis; the weak opening before its final tilded v is now also qualified.')
r['notes'][4]+=' Its exponent delimiters are resolved as square brackets, retaining the author’s actual notation.'
r['notes'][5]+=' The map-domain group immediately before the arrow has no visible exclamation, while the earlier group and the target do; that local omission is preserved.'
r['notes'].append('Blind audit also retains the separate header11 rather than attaching it as primes to g_i, qualifies a colon after aura, and broadens the crossed definition phrase to allow par les couples. The dark inverse-state doubts, p/q distinction, à gauche and gg_i remain unchanged. All mathematical checks below remain conditional on the stated group and conjugator conventions; none chooses a pale letter, restored parenthesis or absent exclamation.')
r['hand'][1]='Long p and g descenders distinguish On passe and gg_i from H’s readings. The pale live word after the crossed definition is less secure: its entry can look g-like or f-like, and groupe/formé/formée remains open. Pi-like signs are judged locally rather than universally capitalized.'
r['hand'].append('Scan025: the small looped mark above des is preserved as a drawing; its possible letter-like shape is not used to supply a word. Header11 is spatially separate from the g_i below. Repeated group-name adornments must be checked occurrence by occurrence.')
for x in r['diff_coverage']:
 if x['row']==23:x['explanation']='Crossed phrase remains par le couple/par les couples/par le groupe; no extra live par le is supplied.'
 if x['row']==24:x['explanation']='The live word remains groupe/formé/formée after the blind audit; no mathematical or grammatical preference resolves it.'
 if x['row']==30:x['explanation']='The surviving formula keeps the preferred literal parenthesis count, with its weak opening before the last tilded v now qualified; no extra close is inserted after tilde u.'
edits=[{'old':oldalpha,'new':newalpha},{'old':oldphrase,'new':newphrase},{'old':'et on aura','new':r'et on aura\unsure{:}'},{'old':oldbase,'new':newbase},{'old':oldlive,'new':newlive},{'old':oldbr,'new':newbr},{'old':olddomain,'new':newdomain}]
write_adjudication(25,'/root/reader_a',c,edits,report_replace={k:r[k] for k in ['changes','decisions','unlisted_decisions','doubts','inventory','notation','notes','hand','diff_coverage']})
