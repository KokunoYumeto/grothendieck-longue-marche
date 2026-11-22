from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan099';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
p=W/'pages'/f'{pg}.tex';s=p.read_text()
oldblock=s[s.index('\\begin{aligned}',s.index('% The following')):s.index('\\end{aligned}',s.index('% The following'))+len('\\end{aligned}')]
newblock=r'''\begin{gathered}
\deleted{\unsure{V_J^L}\,\unsure{=}\,\bigcup_{\unsure{j\in J}}V_j\cap X_L^*=}\\
\deleted{\bigcup_{\unsure{l\in L}}\unsure{V}_{\unsure{l|L}}^{\unsure{Z|2}}}\\
\deleted{\unsure{\supseteq|\geq}\,\unsure{Z|2}=X_L^*}
\end{gathered}'''
oldcap=r'X_J^*\unsure{\cap}'
newcap=r'X_J^*\unsure{\cap|\cup}'
maincap=r'X_J^{\unsure{*}}\unsure{\cap|\cup}'
oldword=r'\deleted{clairement}';newword=r'\deleted{\unsure{clairement|claire et|claire est}}'
oldlabel=r'\overset{(\overset h\sim)}{\hookrightarrow}';newlabel=r'\overset{\overset h{(\sim)}}{\hookrightarrow}'
reps=[(oldword,newword),(oldlabel,newlabel),(r'(112)\qquad',r'(\unsure{112|111})\qquad'),(r'V_{J_0}\cap \mathord{-}\mathord{-}\cap',r'V_{J_0}\cap \mathord{\cdot}\mathord{-}\cap'),(oldblock,newblock)]
for a,z in reps:assert a in s,a;s=s.replace(a,z)
assert s.count(oldcap)==2;s=s.replace(oldcap,newcap,1).replace(oldcap,maincap,1)
oldlim=r'\lim_{\longrightarrow}';newlim=r'\unsure{\uline{\lim}|\varinjlim}'
s=s.replace(oldlim,newlim,1)
s=s.replace('% The following three-line block is entirely canceled. The lower stars are placed below the baseline; their attachment remains uncertain.','% This wholly canceled block is upside down relative to the main text. Its reading orientation is restored below; all original positions remain documented in the crop.')
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id']=='C04':x['final']=r'\deleted{'+newcap+'}';x['evidence']='X, lower hooked J and the star are visible. The following crossed arch admits cap or cup; its orientation is not secure. The entire old group is canceled before live X_L*.'
 if x['id']=='C06':x.update(final=newword,confidence='low',evidence='The exposed opening has c/l/a/i/r/e strokes and a high final t-like stroke, but the crossed middle cannot securely separate clairement from claire et or claire est. The canceled word is retained with local alternatives; donc si above it is live replacement ink.')
 if x['id']=='C08':x.update(final=r'\deleted{'+maincap+'}',confidence='low',evidence='The X diagonals and lower J survive. The small upper group is star-like but partly merged with cancellation; the following arch permits cap or cup. The separate live X_L* has a forked star, not a closed circle.')
 if x['id'] in ['C10','C12']:x['against_C']=True;x['evidence']+=' The parentheses enclose only the wave; h stands above their top, so the previous parenthesis scope is corrected.'
 if x['id']=='C16':x['evidence']='Between the two intersection arches there is one compact round point and one longer horizontal rule. The first component does not have the horizontal extent of the second; retain point-rule, not two rules.';x['crop']=f'crops/{pg}_blind_B12.png';x['box']=b['B12']['coordinates']
withdrawn=[x for x in r['changes'] if x['id'] in ['C22','C23','C24','C25']]
r['superseded_changes']=r.get('superseded_changes',[])+[dict(reason='Withdrawn after the blind reader identified the upside-down block; replaced by the single orientation-aware C22.',records=withdrawn)]
r['changes']=[x for x in r['changes'] if x['id'] not in ['C22','C23','C24','C25']]
r['changes'].append(dict(id='C22',place='Entire upside-down canceled three-row block',C=r'\deleted{\[\begin{aligned}\unsure{X}&=\unsure{\overline{\mathcal V}_{J}^{L}}\\&\unsure{Z\cap\mathcal V_J}\\&=\unsure{X^*\cup\mathcal V_{J\cup L}\cap\mathcal V_L^*}\end{aligned}\]}',H=r'\struck{\ill{}}',final=newblock,evidence='Rotating the existing crop 180 degrees places both clear X_L* groups with ordinary upper stars and lower L feet. The top row has a large union, lower j/membership/J-like strokes, V_j cap X_L*, and a terminal equals sign. The middle row has a separate U-shaped union, lower l/membership/L-like strokes, a V-like body and a raised Z/2. The last row has a doubtful right-facing relation over a lower rule, Z/2, two equals bars and clear X_L*. Crossings obscure the marked parts. The previous three-row reading and low-star interpretation were based on the wrong orientation and are withdrawn. Reader C independently inspected only the rotated existing images and corroborated the provisional lower-row shapes.',crop=f'crops/{pg}_blind_B13.png',box=b['B13']['coordinates'],confidence='low',kind='misread symbol or index',error_kind='1 symbols/indices',against_C=True,against_H=True,consequential=True,marked_in_H=True,phase='blind audit'))
r['changes'].sort(key=lambda x:int(x['id'][1:]))
for x in r['diff_coverage']:
 if any(a in x['change_ids'] for a in ['C23','C24','C25']):x['change_ids']=list(dict.fromkeys('C22' if a in ['C23','C24','C25'] else a for a in x['change_ids']))
 if x['diff_id']=='D0834':x['reason']='The canceled head word remains clairement/claire et/claire est uncertain; its separately raised donc si replacement is clear.'
 if x['diff_id']=='D0835':x['reason']='H leaves the main canceled group illegible. X and J are visible; its star and cap/cup relation remain uncertain.'
 if x['diff_id']=='D0854':x['reason']='C22 records the complete canceled block after correction of its inverted orientation; C26 records the other-hand 98. H’s dossier-ending statement remains editorial.'
r['doubts']=[x for x in r['doubts'] if not x['place'].startswith('canceled block')]
for x in r['doubts']:
 if x['place'].startswith('marginal canceled'):x.update(reading=newcap,alternatives=['cap','cup'],reason='Cancellation obscures the direction of the final arch; X, J and star are visible.')
 if x['place'].startswith('main canceled'):x.update(place='main canceled group, star and final relation',reading=maincap,alternatives=['star uncertain','cap','cup'],reason='The upper star-like crossing and final arch overlap cancellation; X and J remain visible.')
for place,reading,alts,box,why in [
 ('109 limit lower stroke',newlim,['underlined lim','directed limit'],'B03','The endpoint is a small knob without securely separable arrow arms; a headed limit is not certified.'),
 ('Canceled head word',newword,['clairement','claire et','claire est'],'B05','The crossed middle does not expose all letters or word boundaries.'),
 ('Label preceding ordered bands',r'\unsure{112|111}',['112','111'],'B10','The terminal digit is compressed and its lower turn cannot securely establish2; the expected sequence is not substituted for ink.'),
 ('Inverted canceled block, upper row',r'\unsure{V_J^L}\,\unsure{=}\,\bigcup_{\unsure{j\in J}}V_j\cap X_L^*=',['V_J^L tentative','initial equality and union index uncertain'],'B13','The right X_L* and terminal equality are clear; cancellations cross the opening body, relation and lower index.'),
 ('Inverted canceled block, middle row',r'\bigcup_{\unsure{l\in L}}\unsure{V}_{\unsure{l|L}}^{\unsure{Z|2}}',['l or L index','Z or2 raised character'],'B13','The U-shaped union is clear, while crossed index strokes and the following V-like body remain provisional.'),
 ('Inverted canceled block, lower row',r'\unsure{\supseteq|\geq}\,\unsure{Z|2}=X_L^*',['supseteq','geq','Z or2'],'B13','A right-facing curved/angular return lies above a short lower rule; the following equals and X_L* are clear.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
for x in r['deletion_insertion_review']:
 if x['place']=='marginal X_J^* cap':x['reading']=r'\deleted{'+newcap+'}'
 if x['place']=='main X_J^* cap':x['reading']=r'\deleted{'+maincap+'}'
 if x['place']=='clairement':x['reading']=newword;x['confidence']='low'
 if x['place']=='bottom three-line block':x.update(reading=newblock,bounds='All three formula rows are crossed. The block is inverted relative to the main page; its ordinary upper stars become clear after180-degree rotation.',attachment='Separate upside-down abandoned draft below113, not a continuation of the live equality.')
for x in r['inventory']:
 if x['element']=='canceled draft block':x.update(position='bottom main area, upside down relative to main text',first_words_or_objects=newblock)
 if x['element']=='canceled clairement':x['first_words_or_objects']=newword
 if x['element']=='canceled mathematical group in margin':x['first_words_or_objects']=newcap
 if x['element']=='canceled mathematical group in main condition':x['first_words_or_objects']=maincap
 if x['element']=='formula (112)':x['element']='formula labeled112/111, uncertain last digit'
for x in r['notation']:
 if x['sign']=='continuation marks':x['evidence']='Point-rule in the marginal tuple, the bands chain and four locations of113, including its intersection; two points plus rule in the union-condition stack and nonempty-condition continuation.'
 if x['sign']==r'(\overset h\sim)':x['sign']=r'\overset h{(\sim)}'
 if x['sign']=='low stars in canceled final row':x.update(sign='inverted canceled block',reading='ordinary upper stars after180-degree rotation',evidence='The block has its own opposite orientation. The low-star interpretation from the first pass is withdrawn.')
r['notes']=r['notes'].replace('The main line repeats the condition after replacing clairement with donc si','The main line repeats the condition after replacing a canceled clairement/claire et/claire est group with donc si').replace('Both limit arrows have compact right heads; the (109) tip was separately enlarged.','The113 limit has a right head. The109 lower-stroke endpoint does not securely separate into arrow arms and remains underlined-lim/directed-limit uncertain.').replace('two rules in the intersection chain','point-rule in the intersection chain')
a=r['notes'].index('The canceled head word reads clairement');z=r['notes'].index('\n\nThere is no securely',a)
r['notes']=r['notes'][:a]+'''The canceled head word remains clairement/claire et/claire est uncertain: its middle is obscured. The separate donc si above it is replacement ink. The longer phrase J,L des bandes et J prec L, et si attaches before Z contient by a continuous curved leader. In the margin, X_J* is visible but the following canceled cap/cup is not secure. In the main clause the old star also remains uncertain; the separate live X_L* has a visible forked star.

The bottom canceled block is upside down relative to the main text. A180-degree view reveals an upper union/intersection expression ending X_L*=, a second union with a raised Z/2, and a lower relation followed by Z/2=X_L*. The former upright reading and its low-star interpretation are withdrawn. Both clear X_L* groups have ordinary upper stars and lower L feet in the correct orientation. The heavily crossed opening, indices and lower relation remain explicitly tentative. An additional unfamiliar reader viewed only the existing rotated images, without witnesses or proposed text, and corroborated these shapes. The block is printed in restored reading orientation with its original orientation stated in a source comment.

The parentheses in110 and111 enclose the wave only, with h above them. The chain label’s last digit remains112/111 uncertain; its sequence is not used to force2.''' + r['notes'][z:]
for x in r['hand_log']:
 if x['habit'].startswith('Very compressed'):x['witness_errors']='H leaves on aura illegible and shortens posera to pose; the canceled head word remains uncertain after the blind audit.'
r['hand_log'].append(dict(habit='An isolated canceled calculation can be inverted relative to the surrounding page',places=['bottom three-row block'],scope='150_scan099 only; not a global orientation rule',witness_errors='C and the initial consolidation read the crossed block in the wrong direction. Rotation restores ordinary superscript stars and reveals union/index groups. H leaves the block unread.'))
def put(k,why,changed=False,final=None):
 notes[k]=dict(viewed=True,evidence=why)
 if changed:
  if final is None:
   final=b[k]['first']
   for a,z in reps:final=final.replace(a,z)
  notes[k].update(changed=True,final=final)
put('B01','The upper authorial number has a distinct4 followed by a closed lower6 loop. The mspage wrapper is editorial encoding of the same46.')
put('B03','The whole109 display, indices and phi signs were inspected. The limit endpoint has a small knob but no securely separated arrow arms; retain underline-lim/directed-limit uncertainty. The square-ended bracket and plain down arrow have no left hook, and the vertical wave and separate(h) remain visible.',True,b['B03']['first'].replace(oldlim,newlim))
put('B04','The complete marginal note was viewed. J et L retains the separate upright of et despite overwritten joins. The canceled X/J/star is visible but its arch permits cap or cup. The remaining containment clause, phi-free flag tuple and comma/point/rule sequence agree.',True,b['B04']['first'].replace(oldcap,newcap))
put('B05','The cancellation exposes claire-like opening and a high t-like ending but masks the joined middle. Clearly resolving all letters as clairement is not justified; retain clairement/claire et/claire est alternatives. The distinct live donc si is raised above the cancellation.',True)
put('B06','The long insertion ends at si and attaches before Z contient. The old X and J remain visible, while its upper star is partly merged with the strike and its arch admits cap/cup. The live X_L* has a forked star rather than a closed circle.',True,b['B06']['first'].replace(oldcap,maincap))
put('B07','The comma belongs before on aura and is already present in the complete page. Both words are legible; the blind addition is an excerpt boundary difference.')
put('B08','The whole110 formula shows h above the parentheses surrounding only the wave; correct their scope. The target first index retains J/closed-square doubt: its lighter left vertical closes the contour, unlike a plain I.',True)
put('B09','The entire111 definition was inspected. The small detached mark after J still admits comma/filled0, and déf has its acute. Here too h is above the wave’s parentheses, so correct their scope.',True)
put('B10','The whole bands chain has the same point-rule continuation. Its last label digit is compressed; the lower turn is not secure enough to exclude1. Retain112/111 rather than force the next sequential number.',True)
put('B12','All three113 rows were inspected. The intersection continuation begins with one round point, then one longer rule. The LHS commas, two points plus rule in the union conditions and nonempty conditions, point-rule in the V subscript and Drap argument, both phi signs and headed lower limit agree.',True)
put('B13','The complete canceled block was viewed in the original and180-degree orientations and in the existing lower-detail preview. In the correct orientation the clear X_L* groups have upper stars and low L feet, and the top row ends with two equals bars. The middle U-shaped union and raised Z/2 are distinct; the last right-facing relation over a short lower bar remains doubtful. An independent image-only additional reading by reader C corroborated the provisional l/L indices and lower relation. All three rows remain canceled. The previous orientation-dependent reading is replaced without illegible placeholders inside mathematics.',True,newblock)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('099: eleven differing boxes personally viewed; nine changed; three obsolete block rows consolidated into C22.')
