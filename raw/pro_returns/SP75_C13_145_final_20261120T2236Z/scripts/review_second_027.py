from adjudication_io import E,read_rows,write_adjudication
import json
r=json.loads((E/'reader_reports/145_scan027_reviewed.json').read_text())
f={x['box']:x['reading'] for x in read_rows(E/'second/145_scan027_first.tsv')}
b={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in read_rows(E/'second/145_scan027_boxes.tsv')}
n=dict(f)
oe=r'_{=\unsure{\mathfrak S_3|\mathcal S_3}}';ne=r'_{\unsure{=|\simeq}\unsure{\mathfrak S_3|\mathcal S_3}}'
oj=r'\bar j';nj=r'\bar{\jmath}'
orr=r'\deleted{\unsure{\dot\rho}}'
nrr=r'\unsure{\deleted{\unsure{\dot\rho^2}}|\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}}'
op='Les pts fixes';np=r'Les p\textsuperscript{ts} fixes'
opi=r'\unsure{\Pi|\pi}';npi=r'\Pi'
oc=r'$\bar P$, s\'obtiennent';nc=r'$\bar P$ s\'obtiennent'
# Apostrophes above are literal text, not a LaTeX control symbol.
oc=oc.replace("\\'", "'");nc=nc.replace("\\'", "'")
oq=r'\deleted{\unsure{qui}}';nq=r'\deleted{\unsure{qui|et}}'
osig=r'\dot\sigma_1,\dot\sigma_\infty,\tau';nsig=r'\dot\sigma_{\unsure{1}},\dot\sigma_\infty,\tau'
oles=r'\unsure{les} produits';nles=r'\unsure{les|leurs} produits'
otau=r'\deleted{\unsure{$\tau$}}';ntau=r'\deleted{\unsure{ou|un|$\tau$}}'
opt=r'pt\deleted{\unsure{s}}';npt=r'p\textsuperscript{t\deleted{\unsure{s}}}'
pairs=[(oe,ne),(oj,nj),(orr,nrr),(op,np),(opi,npi),(oc,nc),(oq,nq),(osig,nsig),(oles,nles),(otau,ntau),(opt,npt)]
for bid in ['B02','B05','B06','B07','B09','B10']:
 for old,new in pairs:n[bid]=n[bid].replace(old,new)
c={
'B01':{'use_first':True,'adjudication':'Retain source header12 as pagination.','ink':'The first numeral is one long upright with a short lower turn; the second has a curved top, diagonal descent and broad foot. Both readers read12; the difference is the pagination wrapper.'},
'B02':{'final':n['B02'],'changed':True,'adjudication':'Qualify the short underbrace relation; retain U=U0,3, capital Pi, the mismatched closing brace and the undotted barred j.','ink':'Before the small ornate S3 label, the relation has a short dark point/stroke and a longer low stroke, insufficient to exclude a weak upper wave; equals remains preferred with simeq as an alternative. The lower label’s second letter has two sides joined below, unlike the clear crossed X on the next lines, so U=U0,3 is retained. All three Pi signs have a cap and two full descending posts. The base point has a separate minus, long j stem with lower loop and one upper bar, with no extra dot; dotless j under the bar is a serialization correction. The final delimiter has a middle kink and lower foot and remains a right brace despite the opening parenthesis.'},
'B03':{'use_first':True,'adjudication':'Retain the cancelled phrase after conjugaison and before de scindages.','ink':'The crossed phrase lies immediately below conjugaison, extending under its descender, and ends before de scindages. Its initial au, central dessus course and separate final des-shaped group support the first reading. Crossing ink still obscures parts of each word, so the whole phrase remains qualified. It is not relocated after partiels.'},
'B04':{'use_first':True,'adjudication':'Retain éventuelles and its attachment before aux comp.','ink':'The insertion has the accented opening, low vent/u/e course, two tall l strokes and short final es, with enclosing parentheses. Its long guide turns down into the space between et and aux. No ment ending is present. The dotted rho and three sigma signs, X0,3, comp. and ens. are unchanged.'},
'B05':{'final':n['B05'],'changed':True,'adjudication':'Record the high2-like remnant and uncertain scope of cancellation before tau; retain the two separate prose insertions and raise the abbreviated ts.','ink':'The rho-like head before the first tau is densely retraced, while its long descender survives. A separate high curved/angled remnant to its right can be read as2. The ink does not securely distinguish cancellation of the whole rho-squared prefix from cancellation of the raised2 alone, so both states are explicit; the whole-prefix cancellation remains preferred. The dot on rho is also uncertain. The later undotted rho has no dot above its open loop. Sont is a small separate insertion after that rho, while the guide under savoir phi(S3) returns after ordre6, not before P. In pts, the small t/s letters stand above the p baseline and are set raised.'},
'B06':{'final':n['B06'],'changed':True,'adjudication':'Resolve Pi in Pi-conjugués as capital; retain the written1,2,3 indices and both insertion attachments.','ink':'The conjugacy letter has a horizontal cap and two distinct full-height posts, comparable with the three opening Pi forms. The darker lower feet are retracing and do not remove that structure, so the local lower-case alternative is resolved. In the preceding list the three sigma indices are a straight1, curved2 and double-lobed3, all with separate over-dots. The à P guide returns after correspondant; entre eux returns before the conjugacy parenthesis closes.'},
'B07':{'final':n['B07'],'changed':True,'adjudication':'Remove the separate comma before s’obtiennent, broaden the old qui/et word and qualify the dark1 in the later list. Retain both élémt abbreviations and au dessus.','ink':'After Pbar there is no separate punctuation before the small curved initial s of s’obtiennent and its high apostrophe. The hook previously assigned as a comma belongs to that initial word, so it is not duplicated. Both élémt forms have compressed middle strokes and a terminal t rather than a fully written ment sequence. The old word before live qui has a loop and dense cross-strokes that allow qui or et. The later soit/sont remains uncertain; au has a low rounded a and u before the separate dessus. In the savoir list the middle sigma’s small index is a dark upright mass favoring1, now locally qualified.'},
'B08':{'use_first':True,'adjudication':'Retain the cancelled two-symbol formula and all live lift lists.','ink':'The cancelled group has a capped first body, low index mass, comma-like separation and a tau-like second body; crossing ink still prevents full resolution. The live sigma, epsilon and tau lists each read0,1,infinity. The split élé-/ments runs across the physical line ending; the connected lexical word is éléments. The space after cet élément has no stop, and the next on begins with the small lower-case o.'},
'B09':{'final':n['B09'],'changed':True,'adjudication':'Broaden the single retraced les/leurs and prefer a cancelled short word ou/un before rho, retaining tau as an alternative.','ink':'The first word has a high l, a small e loop and a dark compressed ending that permits les or leurs; no second preceding token is visible. After par, the cancelled group begins with a small closed rounded head and has a low continuing turn beneath the long strike. That supports ou or un more directly than the former tau-only recovery, although the same bar and downturn still permit tau. The following rho and rho-squared are live, followed by three close points and a separate farther stop.'},
'B10':{'final':n['B10'],'changed':True,'adjudication':'Retain the singular corrections and set the t plus cancelled s at their raised position after p.','ink':'Le has a crossed terminal letter in the s position, with seul written above the following gap. The p has a long lower stem; its t is smaller and raised at the right, with a short crossed/retraced final s-shaped trace at the same raised level. Both underlying s letters remain qualified. Sigma0, the numeral2, the two C2 factors, tau and the unfinished last sentence are unchanged.'}}
for x in r['changes']:
 for old,new in pairs:x['final']=x['final'].replace(old,new)
 if x['id']=='s027-07':x.update(ink=c['B05']['ink'],confidence='low',c_changed=True,crop='crops/second_145_scan027_B05.png',box=b['B05'],error_category=[1,7],math_consequence='Whole-prefix cancellation remains preferred, making tau the first live member; a surviving rho with only its high2 cancelled is explicitly retained as a state alternative. No fixed-point calculation selects between those ink states.')
 if x['id']=='s027-14':x.update(ink=c['B06']['ink'],confidence='high',crop='crops/second_145_scan027_B06.png',box=b['B06'],math_consequence='The capital Pi of the conjugacy qualification is resolved from its two full posts and cap.')
 if x['id']=='s027-16':x.update(final=r'$\bar P$',ink=c['B07']['ink'],c_changed=True,h_changed=False,kind='text not on the page',error_category=[9],crop='crops/second_145_scan027_B07.png',box=b['B07'])
 if x['id']=='s027-19':x.update(ink=c['B07']['ink'],crop='crops/second_145_scan027_B07.png',box=b['B07'])
 if x['id']=='s027-24':x.update(final=r'\unsure{les|leurs}',ink=c['B09']['ink'],crop='crops/second_145_scan027_B09.png',box=b['B09'])
 if x['id']=='s027-25':x.update(place='After par and before rho: cancelled short word or symbol',ink=c['B09']['ink'],c_changed=True,crop='crops/second_145_scan027_B09.png',box=b['B09'],error_category=[2,5,7])
 if x['id']=='s027-28':x.update(ink=c['B10']['ink'],crop='crops/second_145_scan027_B10.png',box=b['B10'])
for x in r['decisions']:
 if x['id']=='M0875':x.update(reading=npt,ink=c['B10']['ink'],crop='crops/second_145_scan027_B10.png',box=b['B10'])
for x in r['unlisted_decisions']:
 for old,new in pairs:x['reading']=x['reading'].replace(old,new)
 if x['id']=='U027-02':x.update(ink=c['B05']['ink'],crop='crops/second_145_scan027_B05.png',box=b['B05'])
 if x['id']=='U027-04':x.update(ink=c['B07']['ink'],crop='crops/second_145_scan027_B07.png',box=b['B07'])
 if x['id']=='U027-06':x.update(ink=c['B09']['ink'],crop='crops/second_145_scan027_B09.png',box=b['B09'])
r['unlisted_decisions'].append({'id':'U027-07','decision':'first','reading':r'\Pi','ink':c['B06']['ink'],'crop':'crops/second_145_scan027_B06.png','box':b['B06'],'confidence':'high','source':'Capital/lower-case doubt added by the first consolidated reading, not an indexed C mark'})
r['doubts']=[x for x in r['doubts'] if x['place']!='Pi in Pi-conjugués']
for x in r['doubts']:
 for old,new in pairs:x['reading']=x['reading'].replace(old,new)
 if x['place']=='Cancelled sign before first invariant-list tau':x.update(reading=nrr,alternatives=[r'\deleted{\unsure{\dot\rho^2}}',r'\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}'],reason=c['B05']['ink'],crop='crops/second_145_scan027_B05.png')
 if x['place']=='Cancelled qui after E':x.update(alternatives=['qui','et'],reason=c['B07']['ink'],crop='crops/second_145_scan027_B07.png')
 if x['place']=='Les before produits: final-letter surface state':x.update(reading=r'\unsure{les|leurs}',alternatives=['les','leurs','retrace or rewrite in the ending'],reason=c['B09']['ink'],crop='crops/second_145_scan027_B09.png')
 if x['place']=='Cancelled tau before rho':x.update(place='Cancelled short word or symbol before rho',alternatives=['ou','un',r'\tau'],reason=c['B09']['ink'],crop='crops/second_145_scan027_B09.png')
 if x['place']=='Cancelled s after pt':x.update(place='Cancelled raised s after pt abbreviation',reason=c['B10']['ink'],crop='crops/second_145_scan027_B10.png')
r['doubts'].extend([
 {'place':'Underbrace label before ornate S3','reading':r'\unsure{=|\simeq}','alternatives':['=',r'\simeq'],'confidence':'medium','reason':c['B02']['ink'],'crop':'crops/second_145_scan027_B02.png'},
 {'place':'Later savoir list, middle sigma index','reading':r'\unsure{1}','alternatives':['1','retrenched upright index'],'confidence':'medium','reason':c['B07']['ink'],'crop':'crops/second_145_scan027_B07.png'}])
for x in r['inventory']:
 for old,new in pairs:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
for x in r['abbreviations']:
 if x['form']=='pts':x['form']=r'p\textsuperscript{ts}'
 if x['form']=='pt':x['form']=r'p\textsuperscript{t}'
r['notation'][0].update(observation='All four group letters, including Pi-conjugués, have a cap and two full descending posts and are read as capital Pi after the blind audit.',qualification='The darker feet in the fourth occurrence are retracing; the cap-and-post structure is separately visible.')
r['notation'][3]['qualification']='The cancelled first rho’s dot and high2-like trace are uncertain; whole-prefix cancellation is preferred, with cancellation of the high2 alone retained as an alternative.'
r['notation'][5]['observation']='The fundamental-group expression ends with a right brace after an opening parenthesis. The base point is minus barred dotless j. Both underbrace labels are present: a qualified equals/simeq before S3, and U=U0,3.'
r['notes'][1]+=' The blind crop additionally supports a high2-like remnant and leaves the cancellation scope uncertain between the whole prefix and its superscript alone.'
r['notes'][3]=r['notes'][3].replace('The literal comma before s’obtiennent and the absence of a stop before lower-case on are preserved, without grammatical rewriting.','The previously supplied separate comma before s’obtiennent is removed because the hook belongs to its initial s; the absence of a stop before lower-case on is retained.')
r['notes'][4]+=' The small t and crossed s after p are raised; the surviving abbreviation is not expanded.'
r['notes'][9]=r['notes'][9].replace('The crossed rho before the first tau in the next list remains crossed and uncertain.','Before the first tau, cancellation of the whole rho-squared-like prefix remains preferred, but cancellation of its high2 alone is also possible.').replace('This is consistent with the cancellation, without resolving the obliterated dot from mathematics.','This checks rho tau only; it cannot decide the dark prefix, its high2-like remnant, dot, or cancellation scope. The calculation is not used to choose the ink state.')
r['notes'].append('The blind audit resolves capital Pi in Pi-conjugués, qualifies the short underbrace relation and the later dark1, broadens the old qui/et and les/leurs readings, and prefers ou/un over tau in the separate cancelled group before rho. The two élémt abbreviations, literal1,2,3 stabilizer indices, the inserted éventuelles and all insertion attachments remain. Raising the small abbreviation letters and using dotless j below its bar are serialization/placement choices, not additional lexical loci.')
r['hand'][3]['affected_places']=['rho-like prefix with high2-like remnant','cancelled qui/et','cancelled sigma0,tau','cancelled ou/un/tau','retraced les/leurs ending','cancelled s after Le and raised t']
r['hand'].append({'observation':'A curved initial s can be mistaken for a separate comma, and abbreviation letters can sit high at the right of p.','affected_places':['s’obtiennent after Pbar','p with raised ts','p with raised t and cancelled s'],'universal_on_page':False,'witness_misreadings_caused':'C’s separate comma before s’obtiennent is removed after the blind crop; raised abbreviation placement is preserved without expanding the word.'})
for x in r['diff_coverage']:
 if x['row']==3:x['explanation']+=' The final equals/simeq qualification is a noncounted certainty observation in the doubts table.'
 if x['row']==24:x['explanation']='The curved mark is assigned to the initial s of s’obtiennent, not a separate preceding comma; the final reading follows H at this punctuation locus.'
edits=[{'old':old,'new':new,'count':1} for old,new in pairs]
write_adjudication(27,'/root/reader_c',c,edits,report_replace={k:r[k] for k in ['changes','decisions','unlisted_decisions','doubts','inventory','abbreviations','notation','notes','hand','diff_coverage']})
