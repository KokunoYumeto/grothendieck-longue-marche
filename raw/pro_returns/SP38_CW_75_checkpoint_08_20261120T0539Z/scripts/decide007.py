from pathlib import Path
import json,copy
root=Path(__file__).resolve().parents[1]
reports={r:json.loads((root/'readings/scan007'/r/'report.json').read_text()) for r in ['R1','R2','R3']}
r1=reports['R1'];fs=copy.deepcopy(r1['findings'])
r2map=[1,2,3,4,5,6,7,8,9,10,11,12,12,14,15,15,15,15,16,17,18,19,20,21,22,23,24,25,25,26,26,27,27,27,27,28,28,29]
r3map=[1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15,16,17,18,19,20,20,20,21,22,23,24,25,25,24,24,29,26,27,28,30,30,31]
for i,f in enumerate(fs):
 f['readers']={'R1':r1['findings'][i]['final'],'R2':reports['R2']['findings'][r2map[i]-1]['final'],'R3':reports['R3']['findings'][r3map[i]-1]['final']}
 f['decision']='Main inspected the indicated crop; retain the stated reading from visible ink.'
paths={
 1:'crops/scan007/01_opening_word.png',2:'crops/scan007/02_quotes_equality.png',3:'readings/scan007/R1/c01_opening_bound.png',4:'readings/scan007/R1/c14_top_ou.png',5:'readings/scan007/R1/c15_top_au.png',6:'readings/scan007/R1/c02_sigma.png',7:'readings/scan007/R1/c03_G_superscript.png',8:'readings/scan007/R1/c04_u_subscript.png',9:'crops/scan007/03_intro_layout.png',10:'readings/scan007/R1/c05_group_abbreviation.png',11:'readings/scan007/R1/c06_deleted_ens.png',12:'readings/scan007/R1/c07_deleted_formee.png',13:'readings/scan007/R1/c07_deleted_formee.png',14:'readings/scan007/R3/07_generateur.png',15:'readings/scan007/R2/crops/06_inserted_parenthesis.png',16:'readings/scan007/R2/crops/06_inserted_parenthesis.png',17:'readings/scan007/R2/crops/06_inserted_parenthesis.png',18:'readings/scan007/R2/crops/06_inserted_parenthesis.png',19:'crops/scan007/04_du_moins.png',20:'readings/scan007/R1/c09_deleted_sinon.png',21:'crops/scan007/05_second_bullet.png',22:'crops/scan007/05_second_bullet.png',23:'crops/scan007/05_second_bullet.png',24:'crops/scan007/06_ens.png',25:'readings/scan007/R1/c10_elements_abbreviation.png',26:'crops/scan007/07_separator.png',27:'crops/scan007/08_first_summary.png',28:'readings/scan007/R1/c11_nec_punctuation.png',29:'readings/scan007/R1/c11_nec_punctuation.png',30:'crops/scan007/08_first_summary.png',31:'crops/scan007/08_first_summary.png',32:'readings/scan007/R1/c12_automorphism_clause.png',33:'readings/scan007/R1/c12_automorphism_clause.png',34:'readings/scan007/R1/c12_automorphism_clause.png',35:'readings/scan007/R1/c12_automorphism_clause.png',36:'crops/scan007/09_final_summary.png',37:'crops/scan007/09_final_summary.png',38:'readings/scan007/R1/c13_final_ellipsis.png'}
for i,f in enumerate(fs,1):
 f['crop']=paths[i]
 f['evidence']=f['evidence'].replace('Half a:','Main crop:').replace('Half b:','Main crop:').replace('Half a, continuation also in half b:','Main crop:')
# The open initial counter and flat shoulder favour r; keep sigma as an alternative.
fs[5].update(final=r'\unsure{r|\sigma}:S\longrightarrow A',diff_c=True,diff_h=True,evidence='Main crop shows an open descending left entry and a flat right shoulder; no secure closed counter. This favours r over sigma, but the small compressed glyph remains ambiguous.',decision='Choose R2 primary r; retain R1/R3 sigma as the alternative. No formula expectation used.')
for i in [4,5,13,29]:
 fs[i-1]['doubt_action']=''
 fs[i-1]['decision']='New doubt added to C after main crop inspection; alternatives remain visible possibilities.'
fs[12]['decision']='R1 retains la|2; R2 and R3 resolve la. Main sees a single hooked glyph after clear de, without a securely separate a: retain la|2.'
fs[14]['decision']='All three place the smaller parenthesis between items 2 and 3 as an insertion. Main crop confirms size and location. Word-level differences are counted in separate rows.'
fs[17]['decision']='R1/R2 order alternatives sss|ss|ssi; R3 sss|ssi|ss. Main retains sss first, then ss and ssi; no secure i dot. Alternative ordering makes no substantive H difference beyond the primary sss versus ssi.'
fs[25]['decision']='R1/R2 use a slightly rising TikZ stroke; R3 uses a horizontal rule. Main crop shows a single stroke rising rightwards; keep the TikZ representation. C representation change is not counted as a transcription correction.'
fs[28]['decision']='R1 retains a terminal-point alternative; R2/R3 omit it. Main crop leaves a detached short trace at the e exit: retain connexe|connexe. with no final s.'
fs[37].update(final=r'\unsure{\ldots|un}',diff_c=False,diff_h=False,confidence='medium',doubt_action='retain',evidence='Main crop shows two short separated dot-like marks and a longer third low stroke. Ellipsis is favoured, but a flattened word remains possible; the crop does not securely exclude un.',decision='R1 resolves ellipsis; R2/R3 retain ellipsis|un. Main retains the C doubt with ellipsis first.')
pair=copy.deepcopy(reports['R2']['findings'][12])
pair.update(final=r'\{g,\unsure{s|g}^{-1}\}',diff_c=True,diff_h=True,confidence='medium',doubt_action='',crop='readings/scan007/R2/crops/06_inserted_parenthesis.png',evidence='Main crop: first g has a conspicuous long descender. The second base has a short upper hook and lower return, with no comparable descender, favouring s; compressed g remains possible.',readers={'R1':r'\{g,g^{-1}\}','R2':r'\{g,\unsure{g|s}^{-1}\}','R3':r'\{g,g^{-1}\}'},decision='Main keeps s|g, with s first from the ink. Expected inverse-pair mathematics cannot select g.',consequential=True,math_note='The second base in the pair is retained as s|g, with s preferred from its short shape. The inverse-pair cardinality check applies only to the g alternative.')
para=copy.deepcopy(reports['R2']['findings'][29])
para.update(crop='crops/scan007/03_intro_layout.png',readers={r:r'Se donner un \uline{contour connexe} équivaut : la donnée de' for r in reports},evidence='Main crop shows the colon at the end of the first line and la donnée de at the ordinary next-line spacing, returning to the left edge. No separate indented or spaced paragraph begins there.',decision='All three readers keep the introduction as one paragraph; main crop confirms. H introduces an unsupported paragraph break.')
fs.insert(14,pair)
fs.insert(10,para)
text=(root/'readings/scan007/R1/reading.tex').read_text()
for old,new in [(r'\unsure{\sigma|r}',r'\unsure{r|\sigma}'),(r'\{g,g^{-1}\}',r'\{g,\unsure{s|g}^{-1}\}'),(r'$=\ldots$',r'$=\unsure{\ldots|un}$')]:
 assert text.count(old)==1,(old,text.count(old))
 text=text.replace(old,new)
(root/'decisions/scan007_final.tex').write_text(text)
views=list(dict.fromkeys(paths.values()))
assert len(views)==25,len(views)
# All files below have now actually been displayed to the main reader; failed emission was retried.
obs={'stage':'all three complete readings compared; every disagreement and every C doubt adjudicated on crops','main_created_crop_count':9,'main_crop_views':views,'observations':[{ 'place':f['place'],'reading':f['final'],'evidence':f['evidence'],'decision':f['decision'],'crop':f['crop']} for f in fs], 'image_emission_note':'One three-crop batch was truncated; its images were not counted as seen. The same existing c01, c03 and c04 files were subsequently displayed successfully in smaller batches. No second crop was made.'}
(root/'decisions/scan007_main_observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n')
unresolved=copy.deepcopy(r1['unresolved'])
unresolved[2].update(reading='r',alternatives=r'\sigma')
unresolved.append({'place':'Item 2, second base in inverse-like pair','reading':'s','alternatives':'g','confidence':'medium'})
unresolved.append({'place':'Final summary after equals','reading':r'\ldots','alternatives':'un','confidence':'medium'})
inventory=copy.deepcopy(r1['inventory'])
inventory[0]['first_words_or_objects']=inventory[0]['first_words_or_objects'].replace('σ/r','r/σ')
inventory[4]['first_words_or_objects']='une partie de G⁰; de la/2 forme {g,(s|g)⁻¹}; générateur'
inventory[15]['first_words_or_objects']='Contour (pas néc connexe) = …/un'
events=json.loads((root/'pending_events/scan007.json').read_text())
for e in events:
 e['who']=e['who'].replace(' preliminary check','')
 if e['statement_id']=='M007-F':e['outcome']=e['outcome'].replace('The ink for n in N and the bound remains subject to the readers/main adjudication; no infinity symbol is inserted from this check.','All three complete readings have n in N, and the main bound crop confirms n>=2. No infinity symbol is supplied from this check.')
for r,report in reports.items():
 for i,c in enumerate(report['checks']):
  outcome=c['reasoning']+' '+c['outcome']
  if i==0:outcome+=' Main transcription retains s|g as the second base; this check applies to the g alternative, not arbitrary s.'
  events.append({'statement_id':'M007-I' if i==0 else 'M007-W2','date':'2026-11-20','who':f'GPT-6 Astra Pro; effort inherited/not exposed; scan007 {r}','type':'targeted proof check','outcome':outcome})
notes="""The sheet continues the description of connected oriented contours by a cyclic order n and a torsor, then lists data for a connected contour and replaces its second datum by a two-element Ω mapping to inverse generators. Two lower summaries concern contours not assumed connected; the second ends in an ellipsis-like trace, with un retained as an alternative. There is no title or manuscript date. Archive pencil foliation 6 is comment-only. The inserted tel, smaller interlinear parenthesis, three cancellations, two bullet marks and short rising separator are preserved. The opening parenthesis before savoir remains unclosed. G⁰ becomes bare G in 2 bis; no superscript is supplied.

The main reading of the map is r|σ. The second base in the displayed pair has a short s-like shape unlike the preceding descending g: retain s|g, despite the attractive inverse-pair formula. The three readers' local check (M007-I) that an order-n generator has a two-element inverse pair precisely when n≠2 applies only to the g alternative. The small shorthand remains sss|ss|ssi; that algebra does not decide its letters. M007-W2 checks that two distinct elements of Ω can have the same image when n=2. The author's qualifications Du moins si n≥3 and pas néc. / pas néc are kept; the opening bound is 2, not a written question mark.

Main construction check M007-C builds the degree-two graph from the finite cyclic torsor and the two-element Ω, preserving the parallel edges at n=2. It is not an unqualified equivalence proof. The formulation with ordinary n∈ℕ misses the two-sided infinite contour (M007-F); the infinite cyclic torsor supplies that component (M007-FINF). Interpreting the lower acted-on set as vertices, an arbitrary ℤ-action also allows a fixed point, incompatible with the earlier two-distinct-endpoints axiom (M007-Z). The fixed-point-free successor-permutation construction is checked as M007-ZNF. Its directed-edge notion of orientation is not identified without qualification with scan006's automorphism-based definition, especially at two vertices. These limitations affect only the notes; the written assertions remain unchanged."""
dec={'base':'R1','text_file':'decisions/scan007_final.tex','findings':fs,'inventory':inventory,'notes':notes,'events':events,'unresolved':unresolved,'abbreviations':r1['abbreviations'],'main_crop_count':9,'main_crop_views':views,'c_doubt_coverage':[dict(x,disposition='retain ellipsis|un') if x['c_locus']=='ellipsis|un' else dict(x,disposition='retain, primary r') if x['c_locus']=='sigma|r' else x for x in r1['c_doubt_coverage']]}
assert len(fs)==40 and len(events)==12 and len(unresolved)==16
for f in fs: assert (root/f['crop']).is_file(),f['crop']
(root/'decisions/scan007.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
print({'findings':len(fs),'events':len(events),'inventory':len(inventory),'unresolved':len(unresolved),'main_views':len(views)})
