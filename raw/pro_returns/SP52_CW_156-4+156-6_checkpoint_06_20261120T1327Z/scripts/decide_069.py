from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1];K='156-4_069'
R=[json.loads((O/'readers'/K/f'R{i}/report.json').read_text()) for i in (1,2,3)]
P=f'readers/{K}/R1/crops/';Q=f'readers/{K}/R2/crops/';S=f'readers/{K}/R3/crops/';A=f'crops/{K}/'
t=(O/'readers'/K/'R1/reading.tex').read_text()
t=t.replace(r'\unsure{on trouvera|on trouve|on retrouve}',r'\unsure{on trouve|on trouvera|on retrouve}')
t=t.replace('de Stone de',r'de \unsure{Stone} de')
t=t.replace(r'\unsure{je} ne vois comment',r'\unsure{je} \unsure{ne vois} comment')
phi=r"\unsure{\Phi'|\overline\Phi|\Phi}"
t=t.replace(r"\unsure{\overline\Phi|\Phi'|\Phi}",phi)
t=t.replace(r"\forall x'\in M'",r"\forall x'\in\unsure{M'|M''}")
stroke=r'  \draw[line width=0.65pt] (1.15,-0.29)--(1.22,-0.32);'
needle=r'  \node[anchor=west] at (0.55,0.53) {\inserted{``ultra}};'
t=t.replace(needle,needle+'\n% Detached short stroke below stonienne; no function is assigned.\n'+stroke)
filename='J156-4-09_156-4_scan069.tex';(O/'pages'/filename).write_text(t)
d={k:copy.deepcopy(R[0][k]) for k in ['differences','c_doubts','inventory','remaining_doubts','abbreviations']}
d.update(key=K,cote='156-4',scan=69,folder='J156-4-09',their_page=68,filename=filename,brief_version='v05',check_events=[])
rows={i+1:x for i,x in enumerate(d['differences'])}
rows[1]['crop']=S+'01_opening.jpg'
rows[7].update(reading=rows[7]['reading'].replace(r'\unsure{on trouvera|on trouve|on retrouve}',r'\unsure{on trouve|on trouvera|on retrouve}').replace('de Stone de',r'de \unsure{Stone} de'),crop=P+'06_margin_middle.jpg; '+A+'a02_margin_ne_vois.jpg',scan_shows='Angular Sigma, three-arm E and lowered disc. with its point are visible. The verb has a crossed t and a long reduced ending; on trouve is first, with trouvera and retrouve retained. The tall S/t-like start and compressed ending of Stone remain partly crossed by body writing. The name is retained with local doubt rather than inferred from the mathematical construction. H gives only editorial fragments of this passage.')
rows[8].update(reading=r'Dans le cas qui vient, \unsure{je} \unsure{ne vois} comment \unsure{prouver}, pour trois supports',change_c=True,crop=P+'07_margin_lower.jpg; '+P+'08_margin_formula.jpg; '+A+'a02_margin_ne_vois.jpg',scan_shows='The complete marginal sequence extends into upright body writing. A descending je loop, two low ne-like humps and a reduced v/o/i/s-like continuation remain visible, but the latter letters are crossed and compressed. Root’s new crop supplies the tail omitted from earlier frames; it warrants a local ne vois doubt. No separate pas-sized group is present before comment. Prouver remains compressed.')
rows[12]['crop']=P+'03_supports.jpg; '+P+'04_compact.jpg'
rows[13]['crop']=Q+'06_compact.jpg'
rows[16]['crop']=A+'a01_involution.jpg; '+S+'03_compact.jpg'
rows[22]['confidence']='medium'
rows[27].update(reading='$'+phi+'$',change_c=True,crop=Q+'10_phi.jpg',scan_shows='Phi has an oval, upright and baseline. The separate upper mark is short, dark and displaced beyond its right edge, favouring a prime as first candidate. Its nearly horizontal shape and dense retracing also permit a displaced bar or an independent blot; the ambiguity is retained.',consequence='The mark on the family-realization symbol may distinguish a prime from a closure bar. Neither interpretation is substituted solely from the construction being described.')
rows[29]['crop']=Q+'11_tuple.jpg'
rows[32].update(c='M',h=r'\mathcal{M}',reading='M',scan_shows='All four M occurrences in the display have the plain peaked form, including the operator subscript and both primed occurrences. This row concerns alphabet alone. The operator, x, relation and final prime-count uncertainty are separate loci.')
rows[38].update(c='M',h=r'\mathcal{M}',reading='M',scan_shows='The two M letters in the bottom note have the plain peaked form. This row concerns alphabet alone; les, connexes and the local accent question are separate loci.')
prime=copy.deepcopy(next(x for x in R[1]['differences'] if x['location']=='Display, last M prime'))
prime.update(id='A-069-D042',h=r"\mathcal{M}'",crop=Q+'13_set.jpg',scan_shows='The final high mark is kinked, with two joined short legs immediately before the closing brace. One prime with a return is preferred, but two linked primes cannot be excluded. The plain M itself is secure. This row concerns the prime count; M alphabet is counted separately.',consequence='The number of primes on the final quantifier-domain M is left open; it is not forced to match the earlier M-prime merely because that is the expected definition.')
d['differences'].append(prime)
small=dict(id='A-069-D043',location='Detached short stroke below stonienne',c='',h='',reading='Short diagonal stroke below the early middle of stonienne in figure R1-F1: '+stroke.strip(),scan_shows='A small independent diagonal stroke lies below the early middle of stonienne, separated from both the word and the insertion arm. Its geometry is reproduced without assigning it a linguistic or mathematical role.',confidence='high',kind='drawing or diagram',marked_in_h='no',change_c=True,change_h=True,crop=Q+'02_ultra.jpg',math_consequential=False)
d['differences'].append(small)
extra=dict(id='A-069-D044',location='Between construction and Sigma',c='',h=r'\ill{}',reading='',scan_shows='Construction ends the main line and Sigma begins the next. There is no additional word between them. H’s separate unreadable-word placeholder at this position has no corresponding manuscript group.',confidence='high',kind='text not on the page',marked_in_h='yes',change_c=False,change_h=True,crop=P+'09_construction.jpg',math_consequential=False)
d['differences'].append(extra)

for x in d['c_doubts']:
 loc=x['location']
 if loc=='Slanted note, verb before le compactifié':x.update(reading=r'\unsure{on trouve|on trouvera|on retrouve}',status='retained',scan_shows='The crossed t and long low continuation leave the exact ending open. On trouve remains first as in C; trouvera and retrouve remain alternatives.',crop=P+'06_margin_middle.jpg')
 if loc=='Live compact/cpct word':x['crop']=Q+'06_compact.jpg'
 if loc in ['High mark at Φ','C_context: Φ with high mark']:x.update(reading=phi,status='revised',scan_shows=rows[27]['scan_shows'],crop=Q+'10_phi.jpg')
 if loc=='C_context: opening and closing quotation pairs':x['crop']=P+'02_ultra_quelc.jpg; '+P+'05_margin_upper.jpg'
 if loc=='C_context: local R forms, all three occurrences':x['crop']=P+'09_construction.jpg; '+Q+'11_tuple.jpg; '+P+'10_set_definition.jpg'
 if loc=='C_context: x prime, comma, final M prime':x.update(reading=r"(x,x'),\quad\forall x'\in\unsure{M'|M''}",status='revised',scan_shows='The pair comma and x primes are visible. The final high M mark has two joined short legs and remains uncertain between one returned prime and two linked primes.',crop=P+'10_set_definition.jpg; '+Q+'13_set.jpg')
 if loc=='C_context: possible pas before comment':x.update(reading=r'\unsure{je} \unsure{ne vois} comment \unsure{prouver}',status='revised',scan_shows='The continuation is crossed by differently oriented body text. Root’s complete tail crop retains uncertainty in ne vois while showing no separately positioned pas-sized word before comment. No absence was inferred from a clipped reader crop.',crop=P+'07_margin_lower.jpg; '+A+'a02_margin_ne_vois.jpg')

for x in d['remaining_doubts']:
 if x['location']=='Slanted note, before compactifié':x.update(reading='on trouve',alternatives=['on trouvera','on retrouve'])
 if x['location']=='Parties symbol':x.update(reading=r"\Phi'",alternatives=[r'\overline\Phi',r'\Phi'],reason=rows[27]['scan_shows'])
d['remaining_doubts'] += [
 dict(location='Slanted note, Stone',reading='Stone',alternatives=[],confidence='medium',reason='Tall S/t-like start and compressed final run are partly crossed by upright body ink; no completion is supplied from the mathematical name.'),
 dict(location='Slanted note, ne vois',reading='ne vois',alternatives=[],confidence='medium',reason='The now fully framed tail has reduced humps and a v/o/i/s-like sequence, crossed by upright prose; the exact lettering remains locally uncertain.'),
 dict(location='Final M in quantifier domain',reading="M'",alternatives=["M''"],confidence='medium',reason=prime['scan_shows'])]

dis=[]
def dispute(loc,a,b,c,final,evidence,crop):dis.append(dict(location=loc,r1=a,r2=b,r3=c,final=final,evidence=evidence+' ['+crop+']'))
dispute('Detached stroke below stonienne','not represented','short diagonal stroke drawn in F01','not represented',small['reading'],small['scan_shows'],small['crop'])
dispute('Marginal verb before compactifié',r'\unsure{on trouvera|on trouve|on retrouve}',r'\unsure{on trouve|on trouvera|on retrouve}',r'\unsure{on trouvera|on trouve}',r'\unsure{on trouve|on trouvera|on retrouve}','A crossed t and low long run precede a reduced ending. The final curve does not securely establish the longer -ra ending; all three proposed forms remain open.',P+'06_margin_middle.jpg')
dispute('Marginal Stone','Stone',r'\unsure{Stone}','Stone',r'\unsure{Stone}','The tall initial S/t group is distinguishable, but its last reduced humps are interfered with by body writing. The proper name remains a best uncertain reading.',P+'06_margin_middle.jpg; '+A+'a02_margin_ne_vois.jpg')
dispute('Marginal ne vois','ne vois','ne vois',r'\unsure{ne vois}',r'\unsure{ne vois}',rows[8]['scan_shows'],A+'a02_margin_ne_vois.jpg')
dispute('Extra opening mark in marginal equality',r'\unsure{\{|(}',r'\unsure{\{|(}',r'\unsure{(|\{}',r'\unsure{\{|(}','A distinct hooked upper turn and descending arm favour a brace; overlapping body strokes keep a round-parenthesis interpretation possible.',P+'08_margin_formula.jpg')
dispute('Terminal marginal equality mark',r'\unsure{\}|.|,|)}',r'\unsure{\}|.|,|)}',r'\unsure{.|,|)}',r'\unsure{\}|.|,|)}','The high curled two-turn mark allows a closing-brace interpretation beyond C’s point/comma/parenthesis alternatives. Its extent and relation to crossing prose remain uncertain.',P+'08_margin_formula.jpg; '+S+'11_margin_upper_right_tail.jpg')
dispute('Donc certainty',r'\unsure{Donc}',r'\unsure{Donc}','Donc',r'\unsure{Donc}',rows[10]['scan_shows'],rows[10]['crop'])
dispute('Supports verb certainty',r"\unsure{s'identifient|s'identifieraient}","s'identifient",r"\unsure{s'identifient|s'identifieraient}",rows[11]['reading'],rows[11]['scan_shows'],rows[11]['crop'])
dispute('Fera certainty',r'\unsure{fera}','fera','fera',r'\unsure{fera}',rows[17]['scan_shows'],rows[17]['crop'])
dispute('Inserted relation alphabet',r'\mathcal R',r'\unsure{\mathcal R|R}',r'\mathcal R',r'\mathcal R','The inserted form has a full rounded outside return and descending right leg, unlike the simpler short-bowl R in the tuple. Local script form is accepted at medium confidence.',P+'09_construction.jpg; '+Q+'11_tuple.jpg')
dispute('Small toute insertion',r'\unsure{toute|toutes}','toute',r'\unsure{toute|toutes}',r'\unsure{toute|toutes}',rows[24]['scan_shows'],rows[24]['crop'])
dispute('High mark at Phi',r"\unsure{\overline\Phi|\Phi'|\Phi}",phi,r"\unsure{\overline\Phi|\Phi'|\Phi}",phi,rows[27]['scan_shows'],rows[27]['crop'])
dispute('Final M prime',"M'",r"\unsure{M'|M''}","M'",r"\unsure{M'|M''}",prime['scan_shows'],prime['crop'])
dispute('Bottom saturées accent',r'\unsure{saturées|saturees}','saturées',r'\unsure{saturées|saturees}',r'\unsure{saturées|saturees}',rows[37]['scan_shows'],P+'11_bottom_note.jpg; '+Q+'20_bottom_note.jpg')
d['disputes']=dis
idx=next(i for i,x in enumerate(d['inventory']) if x['element']=='Long slanted left note')
d['inventory'].insert(idx,dict(element='Detached stroke below stonienne',kind='drawing',position='below early middle of stonienne in opening paragraph',first_words_or_objects='one short down-right stroke; no assigned function',sheet_kind='text',hand='his hand',transcribed='yes'))
for x in d['inventory']:
 if x['element']=='Cosupport set display':x['first_words_or_objects']=r"\operatorname{cosup}_M(M')=\{x\in M\mid(x,x')\in\mathcal R\quad\forall x'\in\unsure{M'|M''}\}"
d['witness_reviews']=[dict(reference='Witness S: 156-7_CORRECTIONS.tsv, SA21-K7-10; where 156-7/064-065 (and 156-4/069)',claim='The row identifies distributivity of the support lattice as the author’s conjecture and reports its later refutation. Its quoted wording and counterexamples refer to other scans.',decision='Confirmed for the local transcription scope: scan069 calls the Boolean-algebra claim a presumption and writes the three-support distributivity equality with a statement that its proof is not seen. No refutation or counterexample is written on this page. The later mathematical refutation reported by S was neither checked nor adopted as a theorem in this run.',evidence='The raised présume replaces cancelled dis. The slanted note contains the je/ne vois/comment/prouver sequence, retaining the listed reading doubts, and the visible P,Q,R wedge/vee formula. The extra formula delimiters remain uncertain. No wording from the other cited pages is imported.',crop=S+'01_opening.jpg; '+P+'07_margin_lower.jpg; '+P+'08_margin_formula.jpg; '+A+'a02_margin_ne_vois.jpg')]
d['notes']={
 'summary':'The continuation describes arbitrary suprema by saturation of a union, then says Je [dis struck] présume that the supports form a Boolean algebra. Its long oblique note says this should hold in the set-like case and named examples, relates Sigma to parts of E and a Stone compactification, and states difficulty proving the written three-support distributivity formula. The body describes supports as clopen parts of a spectrum and involution as complementation. It then says the construction depends on the ordered M with compatibility, gives a cosupport set definition, and cites connected components as examples using C4. These are the manuscript’s statements, not proved results of this run.',
 'math_reading_decisions':[
  'The recognizable distributivity pattern prompted inspection of each P,Q,R, wedge, vee and delimiter. The visible extra opening hook and terminal curled mark remain in place with alternatives; the formula was not regularized to an expected form.',
  'The inserted compatibility relation has a curled form; the tuple uses a plainer R, and the displayed relation has a pronounced outside oval. Alphabets were read locally, not selected solely from mathematical roles.',
  'The short mark high to the right of Phi is placed first as a prime, with displaced bar and unrelated-mark interpretations retained. No choice between realization and closure was made from the argument.',
  'The final M mark in the quantifier domain has two joined short legs; one returned prime and two linked primes remain alternatives, despite the expected match with earlier M-prime.',
  'Cosup has one descending p. All M forms are plain; the x letters are smaller than M and read lowercase. Case and alphabet changes alone are not treated as changed mathematical assertions.',
  'The compact word is graphically abbreviated or severely reduced: cpct and cpt precede compact among the alternatives. It is not expanded silently. Stone remains uncertain where body text crosses its ending.'
 ],
 'author_checks':[
  'Je [dis struck] présume is preserved with its raised insertion and connector. The qualified statement is not converted into a theorem.',
  'The oblique je ne vois comment prouver sequence retains local doubts. Root inspected the previously unframed ne vois continuation; no pas-sized word is supplied.',
  'Il faudra y revenir is completely struck through. The cancelled groups around the compact word remain transcribed with their doubts.',
  'The bottom example explicitly says utiliser C4. This is the author’s reference; C4 was not proved or reapplied as a check by this run.',
  'Witness S row SA21-K7-10 is locally confirmed as referring to a conjectural distributivity claim. Its later refutation lies outside these images and remains an unverified witness report here.'
 ],
 'title_dates_pagination':'Manuscript number 68 at the top; archive scan69. No separate title or date. The page carries a long oblique left note, a slanted bottom example, four insertion leaders, a detached short stroke below stonienne and a long rule touching connexes.'
}
d.update(reader_crop_counts={'R1':11,'R2':20,'R3':11},adjudicator_crop_count=2,workflow_note='Three fresh isolated readers used v05 and each viewed whole/halves once, then their own 11/20/11 crops. Root viewed 21 existing reader crops: all11 R1; R2 02,06,10,11,13,18,20; R3 01,03,11. Two new root crops supplied the separate involution continuation and the still-open marginal ne vois tail. Root a01 clipped the high head of passage, already agreeing in C/H; the existing R3 crop03 supplied it without recropping. R3 honestly disclosed that its tail crop did not securely frame ne vois, leading to root’s new complete target. The three returns were compared after completion. A text-only audit identified the missing detached low stroke and a separate H ill placeholder before Sigma, and checked quotation/count scopes. R3’s string yes/no flags were not used for totals; consolidated flags are booleans. All listed crops were actually displayed. No OCR, outside research, compilation or mathematical validation occurred.')
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['bbox_image','source']}
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,str):return x.replace(str(O)+'/', '')
 return x
d=clean(d);(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':K,'differences':len(d['differences']),'C':sum(x['change_c'] for x in d['differences']),'H':sum(x['change_h'] for x in d['differences']),'disputes':len(dis),'remaining':len(d['remaining_doubts']),'inventory':len(d['inventory'])}))
