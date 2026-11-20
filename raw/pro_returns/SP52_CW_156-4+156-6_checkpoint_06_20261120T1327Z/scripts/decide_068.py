from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1];K='156-4_068'
R=[json.loads((O/'readers'/K/f'R{i}/report.json').read_text()) for i in (1,2,3)]
P=f'readers/{K}/R1/crops/';Q=f'readers/{K}/R2/crops/';S=f'readers/{K}/R3/crops/';A=f'crops/{K}/'
t=(O/'readers'/K/'R1/reading.tex').read_text()
t=t.replace(r'la contenant)\unsure{,|\relax}',r'la contenant)')
t=t.replace(r'la contenant),',r'la contenant)')
glyph=r'\unsure{\mathscr P|\mathcal F_2|\mathcal F_0|\mathcal F}'
for old in [r'\unsure{\mathcal F_2|\mathcal F_0|\mathcal F|\mathscr P}',r'\unsure{\mathcal F_2|\mathcal F_0|\mathscr P}']:
    t=t.replace(old,glyph)
points=next(x for x in R[1]['differences'] if x['location']=='Two low detached points beneath the middle of réalisations')['reading']
t=t.replace(r'\unsure{réalisations}', '\n% Two detached points beneath the word, with no inferred function.\n'+points+'\n',1)
filename='J156-4-09_156-4_scan068.tex'
(O/'pages'/filename).write_text(t)
d={k:copy.deepcopy(R[0][k]) for k in ['differences','c_doubts','inventory','remaining_doubts','abbreviations']}
d.update(key=K,cote='156-4',scan=68,folder='J156-4-09',their_page=67,filename=filename,brief_version='v04',check_events=[])
rows={i+1:x for i,x in enumerate(d['differences'])}
# Two rows were source-comparison errors, not manuscript differences.
# H's editorial suggestion is reviewed separately; C already has the display comma.
d['differences']=[x for i,x in rows.items() if i not in (26,44)]
rows[2]['crop']=P+'01_cancelled_opening.jpg'
for n in (3,4):rows[n]['crop']=A+'a01_resp_M.jpg'
rows[7].update(reading='la contenant)',crop=A+'a04_parenthesis_stop.jpg',scan_shows='The complete closing parenthesis is one descending curve. Clear paper continues below and to its right to the page margin; no independent comma is visible.')
rows[15]['confidence']='medium'
rows[17]['crop']=A+'a02_sigma_ens.jpg'
rows[18]['crop']=P+'09_M0_leader.jpg; '+P+'10_ou_F0_cancelled.jpg'
rows[28].update(c='du',h='de',reading='de',change_c=True,change_h=False,confidence='medium')
rows[30].update(c='One paragraph through the cancelled attempts and resumed On',h='Paragraph breaks before the cancelled L’application line and before the resumed On',reading='One paragraph through the cancelled attempts and resumed On',change_c=False,change_h=True,scan_shows='The cancelled On attempt is at the right end of the preceding written line; the cancelled L’application is the following line, and the resumed On follows below without a fresh indented block. This row counts paragraph placement only; lexical changes are recorded separately.',crop=P+'10_ou_F0_cancelled.jpg; '+P+'11_cancelled_application.jpg; '+P+'12_desidentifie.jpg')
rows[33].update(reading=r'\deleted{$'+glyph+'$}',crop=Q+'14_cancelled_letter_ses_deux.jpg',scan_shows='The crossed group has a long upright and a broad angular bowl resembling the first power-set P below. A small loop/2-shaped component survives at lower right. Script P is preferred, but a family F with low 2 or 0, or with a worked flourish, remains possible. All alternatives account for the worked lower component.',consequence='The identity of the cancelled mathematical object remains open: a powerset-style capital competes with a family symbol and possible subscript. No certain index or complete extra object is supplied.')
rows[41].update(c='',h=',',reading='')
rows[47].update(c='',h='.',reading='',change_c=False,change_h=True,scan_shows='No separate full stop follows the final displayed F-shaped letter. This row concerns punctuation only; the letter’s local alphabet uncertainty is recorded separately.')
rows[48].update(crop=P+'15_anti_compound.jpg; '+S+'17_anti_correction.jpg',scan_shows='One densely worked suffix follows anti. A dark crossing runs through the early cluster, while a looped ascender and a tion-like ending survive. The ink does not independently establish two complete successive words isomorph/homéo and involution. The first alternative retains a possibly cancelled invo within one word; the other candidates keep the exact lettering and cancellation state open.',consequence='The correction is represented as one uncertain worked mathematical word, rather than asserting a complete deleted morphism term and a separate complete live term. Its exact property remains unresolved.')
for n in (49,50):rows[n]['crop']=A+'a03_bottom.jpg'
pointrow=copy.deepcopy(next(x for x in R[1]['differences'] if x['location']=='Two low detached points beneath the middle of réalisations'))
pointrow.update(id='A-068-D051',c='',h='',confidence='high',marked_in_h='no',scan_shows='Two separate dark points stand below the middle of réalisations, the second lower and to the right. Their drawn geometry is preserved without converting them into word-final punctuation or assigning them a linguistic or mathematical function.')
d['differences'].append(pointrow)
d['witness_reviews']=[dict(reference='H editorial note after manuscript page 67',claim=rows[26]['h'],decision='Rejected as an ink reading: retain the written M. H’s literal transcription also has M, so rejection of the editorial suggestion is not counted as a transcription change.',evidence='After family F_0 the letter has two clear M uprights. No separate underlying F is established. The literal wording is preserved without mathematical repair.',crop=P+'10_ou_F0_cancelled.jpg')]

for x in d['c_doubts']:
    loc=x['location']
    if loc=='Cancelled glyph after Sigma de':x.update(reading=rows[33]['reading'],status='revised',scan_shows=rows[33]['scan_shows'],crop=rows[33]['crop'])
    if loc=='On désigne and displayed subscripts':x['crop']=A+'a02_sigma_ens.jpg; '+P+'14_P2_sigma_display.jpg'
    if loc=='Bottom paragraph: Inf and Sup':x['crop']=A+'a03_bottom.jpg'
    if loc=='l’ens des parties, l’ens des supports, d’ens. ordonnés':x['crop']=P+'06_bijection.jpg; '+A+'a02_sigma_ens.jpg; '+A+'a03_bottom.jpg'
    if loc=='Two power-set letters':x['crop']=P+'13_realisations_P1.jpg; '+P+'14_P2_sigma_display.jpg'
    if loc.startswith('Revised anti compound:'):x.update(reading=rows[48]['reading'][4:],scan_shows=rows[48]['scan_shows'],crop=rows[48]['crop'])
for x in d['remaining_doubts']:
    if x['location']=='Cancelled glyph following Sigma de':x.update(reading=r'\mathscr P',alternatives=[r'\mathcal F_2',r'\mathcal F_0',r'\mathcal F'],reason=rows[33]['scan_shows'])

dis=[]
def dispute(place,a,b,c,final,evidence,crop):dis.append(dict(location=place,r1=a,r2=b,r3=c,final=final,evidence=evidence+' ['+crop+']'))
dispute('Parenthetical initial word',r'\unsure{telles|celles}',r'\unsure{telles|celles}',r'\unsure{celles|telles}',rows[6]['reading'],rows[6]['scan_shows'],rows[6]['crop'])
dispute('Punctuation after la contenant','no comma in final return; earlier draft had comma/absence doubt',',',',','no comma',rows[7]['scan_shows'],rows[7]['crop'])
dispute('Low point before cosup','.',r'\unsure{.}','.','.',rows[9]['scan_shows'],rows[9]['crop'])
dispute('Accent in live definit',r'\unsure{definit|définit}','définit','définit',rows[11]['reading'],rows[11]['scan_shows'],rows[11]['crop'])
dispute('Sur before elles','sur',r'\unsure{sur}',r'\unsure{sur}','sur',rows[15]['scan_shows'],rows[15]['crop'])
dispute('Où accent','où','où',r'\unsure{où|ou}','où',rows[22]['scan_shows'],rows[22]['crop'])
dispute('Cancelled application first preposition','de',r'\unsure{du|de}','de','de',rows[28]['scan_shows'],rows[28]['crop'])
dispute('Cancelled application final word',r'\unsure{d|de}',r'\unsure{d|de}',r'\unsure{de|d}',rows[29]['reading'],rows[29]['scan_shows'],rows[29]['crop'])
dispute('Verb before Sigma',r'\unsure{désidentifie}',r'\unsure{désidentifie|identifie}',r'\unsure{désidentifie}',rows[31]['reading'],rows[31]['scan_shows'],rows[31]['crop'])
dispute('Cancelled capital after Sigma de',r'\unsure{\mathcal F_2|\mathcal F_0|\mathcal F|\mathscr P}',r'\unsure{\mathscr P|\mathcal F}',r'\unsure{\mathcal F}',glyph,rows[33]['scan_shows'],rows[33]['crop'])
dispute('Two points under réalisations','not represented','two points drawn below the word','not represented',points,pointrow['scan_shows'],pointrow['crop'])
dispute('First P alphabet',r'\unsure{P|\mathscr P|\mathcal P}',r'\unsure{\mathscr P|\mathcal P|\wp|P}',r'\unsure{\mathscr P|\mathcal P|\wp}',rows[37]['reading'],rows[37]['scan_shows'],rows[37]['crop'])
dispute('Second P alphabet: report versus fragment',r'\mathscr P',r'\mathscr P',r'\mathscr P in reading.tex; report describes uncertainty at both P occurrences',r'\mathscr P','The second occurrence has a full lower-left curling foot and broad upper bowl in the complete R1 crop. The uncertainty of the first occurrence is not propagated automatically. R3’s crop reaches the lower upright boundary and is not used to claim absence of any further stroke.',P+'14_P2_sigma_display.jpg')
dispute('F argument of second P',r'\unsure{\mathcal F|F}',r'\mathcal F',r'\mathcal F',rows[40]['reading'],rows[40]['scan_shows'],rows[40]['crop'])
dispute('Final F of displayed inclusions',r'\unsure{\mathcal F|F}',r'\mathcal F',r'\mathcal F',rows[46]['reading'],rows[46]['scan_shows'],rows[46]['crop'])
dispute('Worked anti compound',rows[48]['reading'],'One diagram with deleted illegible older layer below uncertain live word','One uncertain suffix with overstrike and residual strokes drawn',rows[48]['reading'],rows[48]['scan_shows']+' Ordinary partial-cancellation notation is used; an additional complete older word is not asserted.',rows[48]['crop'])
d['disputes']=dis

idx=next(i for i,x in enumerate(d['inventory']) if x['element']=='Paired inclusions')
d['inventory'].insert(idx,dict(element='Two low points beneath réalisations',kind='drawing',position='below the middle of réalisations; second point down and right',first_words_or_objects='two detached ink points, drawn without assigned function',sheet_kind='text',hand='his hand',transcribed='yes'))
for x in d['inventory']:
    if x['element']=='Cancelled mathematical glyph':x['first_words_or_objects']=glyph
    if x['element']=='Paired inclusions':x['first_words_or_objects']=r'M_\sigma\subset M,\quad\mathcal F_\sigma\subset\unsure{\mathcal F|F}'
d['notes']={
 'summary':'The page asserts that every part of the figure family or of M is contained in a least saturated part, described as cosupport of cosupport and also called support. It characterizes saturated parts as supports or cosupports and says that cosup reverses inclusion in a self-correspondence of those parts. It introduces Sigma as the set of virtual supports, with realizations represented by M_sigma and family F_sigma. The written phrase family F_0 de M is retained. The final paragraph describes cosupport on Sigma by a heavily revised anti-compound and asserts arbitrary Inf as intersections and arbitrary Sup via saturation; the latter sentence continues beyond the page. These assertions have been transcribed, not proved.',
 'math_reading_decisions':[
  'The literal equals-like mark after elles has two separate horizontal bars. It is not expanded to mêmes, even though that interpretation would complete familiar wording.',
  'The final M in family F_0 de M has two plain uprights. H’s suggested editorial replacement with family F is rejected on the ink, while its literal M transcription is acknowledged as agreeing.',
  'The densely revised anti-compound was inspected because its property matters mathematically. Only one worked suffix is established; neither a complete deleted isomorph/homéo nor a separate certain final word can be asserted. Involution, with possible partial cancellation, remains first among the uncertain candidates.',
  'The first P has a straight stem and angular bowl without a definite lower flourish; plain P is retained among the alternatives. The second P has a lower-left curl. Two reduced F occurrences have local plain/calligraphic doubts instead of inheriting a family alphabet from context.',
  'The cancelled capital after Sigma de has a P-like bowl and a lower-right component; family symbols with possible low indices remain alternatives. The glyph is not replaced by an expected realization symbol.',
  'The displayed separator comma agrees with C and H. An initial R1 comparison misquoted C and was corrected during record audit; no change is counted for that comma.'
 ],
 'author_checks':[
  'Visible drafting revisions include the cancelled opening quotation start, s’appelle du/de, the raised e in bijection, raised M_0 with an oblique leader, cancelled de and two cancelled application starts, the cancelled capital, cancelled pour, and the worked anti-compound.',
  'No explicit à vérifier or sauf erreur is present. The uncertainty in the compound is the transcriber’s, not an added authorial conjecture mark.',
  'Two detached points below réalisations are drawn at their observed positions. No punctuation or mathematical role is inferred for them.',
  'The page ends with an open parenthesis after the description of Sup. No continuation, closing parenthesis or final punctuation is supplied.'
 ],
 'title_dates_pagination':'Manuscript page 67 at the top centre; archive scan 68. Supports and virtuels have separate underlines. No date, title sheet or separate page-count statement is visible.'
}
d.update(reader_crop_counts={'R1':15,'R2':18,'R3':17},adjudicator_crop_count=4,
 workflow_note='Three fresh isolated v04 readers, whole and halves once each, followed by their own crops. Root viewed 18 existing reader crops (all15 R1, R2 14 and15, R3 17) and four new targeted crops for the unframed resp/M line, first Sigma/ens line, bottom notation, and low right space after a closing parenthesis. No whole or half page was viewed by root. R1 disclosed a clipped extreme j tail in crop06; the raised-letter target was complete. R3 disclosed that crop16 touched the bottom of the second P upright; root used the complete R1 crop14 for that occurrence. A text-only administrative audit corrected R1’s false claim that C lacked the display comma and separated H’s editorial proposed repair from counted literal differences. It confirmed the two low points as the sole missing physical group in R1’s inventory. Three returns differed in representing the worked anti-word; final uses one uncertain partially cancelled word, without inventing an additional unreadable complete substrate. No OCR, external research, compiler or mathematical proof check occurred.')
def clean(x):
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['bbox_image','source']}
    if isinstance(x,list):return [clean(v) for v in x]
    if isinstance(x,str):return x.replace(str(O)+'/', '').replace("\\'", "'")
    return x
d=clean(d)
(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':K,'differences':len(d['differences']),'C_doubts':len(d['c_doubts']),'disputes':len(dis),'remaining':len(d['remaining_doubts']),'inventory':len(d['inventory'])}))
