"""Record the main reader's decisions after visual adjudication; no recognition."""
from pathlib import Path
import json, copy, re
O=Path(__file__).resolve().parents[1]
K='156-4_066'
R=[json.loads((O/'readers'/K/f'R{i}'/'report.json').read_text()) for i in (1,2,3)]
t=(O/'readers'/K/'R1/reading.tex').read_text()
t=t.replace(r'^{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}!}',r'^{\substack{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}\\!}}')
t=t.replace(r'\unsure{d|!}',r'\unsure{\underset{\circ}{d}|!}')
t=t.replace(r'\unsure{à|:}',r'\unsure{:|à}')
t=t.replace(r'$\unsure{.|,}',r'$,')
t=t.replace('toutes les strates',r'toutes les \unsure{strates}')
figure=r'''\figure{\begin{tikzpicture}[every node/.style={inner sep=1pt}]
  \node[anchor=base west] (initial) at (0,0) {$\unsure{\mathcal C|\mathscr C|C}$};
  \node[anchor=base west] (prefix) at (initial.base east) {$=(\mathcal F,\leq,$};
  \node[anchor=base west] (relation) at (prefix.base east) {$\unsure{\preceq|\leqslant|\deleted{\preceq}|\deleted{\leqslant}}$};
  \node[anchor=base west] (rest) at (relation.base east) {$)$, on pose aussi $\pi_0(\mathcal C)$.};
  \draw[thin] (initial.south) ++(0,-0.05) -- ++(-0.07,-0.43);
  \path (initial.south) ++(-0.07,-0.60)
    node[anchor=north] {\unsure{Contrée|Contrie}};
  \draw[thin] (relation.south) ++(0,-0.58) -- ++(0,0.40);
  \draw[thin] (relation.south) ++(-0.14,-0.15)
    .. controls +(0.10,0.10) and +(-0.03,0.12) .. ++(0.29,-0.02);
  \path (relation.south) ++(0,-0.73)
    node[anchor=north,align=left] {qui ne sert\\\unsure{pourtant|pour\deleted{tant}|\deleted{pourtant}} \unsure{:|à}\\rien ici};
\end{tikzpicture}}'''
start=t.index(r'\figure{');end=t.index(r'\end{tikzpicture}}',start)+len(r'\end{tikzpicture}}')
t=t[:start]+figure+t[end:]
filename='J156-4-09_156-4_scan066.tex'
(O/'pages'/filename).write_text(t)
d={k:copy.deepcopy(R[0][k]) for k in ['differences','c_doubts','inventory','remaining_doubts','abbreviations']}
d.update(key=K,cote='156-4',scan=66,folder='J156-4-09',their_page=65,filename=filename,brief_version='v02',check_events=[])
rows={i+1:x for i,x in enumerate(d['differences'])}
own={1:'a01_du_C4',2:'a01_du_C4',7:'a02_Tous',10:'a03_Notations_NB',11:'a03_Notations_NB',13:'a04_transitivite',14:'a05_pi_M',22:'a06_pi_plain_F',36:'a07_axiome',37:'a07_axiome',38:'a08_C4bis',41:'a09_live_family',51:'a10_Phi_family'}
for n,name in own.items():rows[n]['crop']=f'crops/{K}/{name}.jpg'
for n in [48,49]:rows[n]['crop']=f'readers/{K}/R3/crops/12_heading.jpg'
for n in [57,58]:rows[n]['crop']=f'readers/{K}/R3/crops/16_footer.jpg'
rows[39]['crop']=f'readers/{K}/R3/crops/10_c4_cancelled_exists.jpg'
rows[20].update(reading=r'\unsure{\underset{\circ}{d}|!}',change_c=True,scan_shows='A d-shaped closed loop adjoins a thick upright; a separate hollow lower point survives. The first alternative retains both components rather than dropping the lower point. Their correction state remains uncertain.')
rows[32]['reading']=rows[32]['reading'].replace(r'\unsure{à|:}',r'\unsure{:|à}')
rows[32]['change_c']=False # The two changed internal loci are counted separately in D33/D34.
rows[34].update(reading=r'\unsure{:|à}',scan_shows='Two short vertically separated strokes are visible, with no secure a body. The literal colon-like form is listed first; accented a remains an alternative.')
rows[35]['reading']=figure
rows[35]['crop']=f'readers/{K}/R1/crops/09_tuple_left_gloss.jpg; readers/{K}/R1/crops/10_tuple_relation_gloss.jpg'
rows[45].update(reading=',',scan_shows='The terminal punctuation is a bent descending stroke rather than a round dot; the main reader adopts the comma, as R3.',confidence='medium')
d['differences'].append(dict(id='A-066-D59',location='Notations, vertical position of the cancelled first exponent',c=r'\pi_0^{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}!}',h=r'\pi_0^{\cdot}',reading=r'\pi_0^{\substack{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}\\!}}',scan_shows='The crossed letters stand above the surviving upright and point, not alongside them. This row counts the C placement correction; H exponent content is counted separately.',confidence='high',kind='insertion or placement',marked_in_h='yes',change_c=True,change_h=False,crop=f'readers/{K}/R1/crops/05_first_superscript.jpg',math_consequential=False))
d['differences'].append(dict(id='A-066-D60',location='Bottom paragraph, strates',c='strates',h='strates',reading=r'\unsure{strates}',scan_shows='The s/t/r and later t/es strokes are visible, but the a-position is only a tiny isolated mark. The word is plausible without being secure in every letter.',confidence='medium',kind='other',marked_in_h='no',change_c=True,change_h=True,crop=f'readers/{K}/R2/crops/16_last_cancelled.jpg',math_consequential=False))
for x in d['c_doubts']:
 if x['location']=='Notations, second exponent':x.update(reading=rows[20]['reading'],status='revised',scan_shows=rows[20]['scan_shows'])
 if x['location']=='Notations, à in right gloss':x.update(reading=rows[34]['reading'],scan_shows=rows[34]['scan_shows'])
 if '19_final_posons' in x.get('crop',''):x['crop']=rows[58]['crop']
d['remaining_doubts']=[x for x in d['remaining_doubts'] if x['location']!='C4 bis, final punctuation']
for x in d['remaining_doubts']:
 if x['location']=='Notations, second exponent':x.update(reading=rows[20]['reading'],alternatives=[r'\underset{\circ}{d}','!','d written over !'])
 if x['location']=='Notations, right gloss, à':x.update(location='Notations, mark after pourtant',reading=rows[34]['reading'],alternatives=[':','à'])
 if x['location']=='Notations, C alphabet, both occurrences':x.update(location='Notations, initial C alphabet',reason='The initial inward curl does not settle the alphabet; the later C inside pi_0(C) has a clearer loop and is rendered calligraphically.')
d['remaining_doubts'].append(dict(location='Bottom paragraph, strates',reading=r'\unsure{strates}',alternatives=['strates'],confidence='medium',reason='The expected a body is reduced to an isolated small mark.'))
dis=[]
def dispute(place,a,b,c,final,evidence,crop):
 dis.append(dict(location=place,r1=a,r2=b,r3=c,final=final,evidence=evidence+' ['+crop+']'))
P=f'readers/{K}/R1/crops/'
dispute('Cancelled mark after pi_0(G)',r'\deleted{\unsure{)}}',r'\deleted{\unsure{)}}',r'\deleted{\unsure{)|?}}',rows[12]['reading'],rows[12]['scan_shows'],P+'04_notations_cancelled_parenthesis.jpg')
dispute('First exponent placement','cancelled cat/act followed by !','cancelled cat/act followed by !','cancelled cat/act above !',d['differences'][-2]['reading'],d['differences'][-2]['scan_shows'],P+'05_first_superscript.jpg')
dispute('Low point inside first family parenthesis',r'\unsure{.}',r'\unsure{.}','omitted',rows[18]['reading'],rows[18]['scan_shows'],P+'05_first_superscript.jpg')
dispute('Second exponent',r'\unsure{d|!}',r'\unsure{\underset{\circ}{d}|!}',r'\unsure{d|!}',rows[20]['reading'],rows[20]['scan_shows'],P+'07_second_superscript.jpg')
dispute('Article before Sup',r'\unsure{du|des}',r'\unsure{du|des}','du',rows[23]['reading'],rows[23]['scan_shows'],P+'08_quotation.jpg')
dispute('Initial C alphabet',rows[27]['reading'],rows[27]['reading'],r'\mathcal C',rows[27]['reading'],rows[27]['scan_shows'],P+'09_tuple_left_gloss.jpg')
dispute('Third tuple relation',rows[29]['reading'],rows[29]['c'],r'\unsure{\preceq|\leqslant|\deleted{\preceq}}',rows[29]['reading'],rows[29]['scan_shows'],P+'10_tuple_relation_gloss.jpg')
dispute('Right gloss, pourtant state',rows[33]['reading'],r'\deleted{\unsure{pourtant}}',r'\deleted{\unsure{pourtant}}',rows[33]['reading'],rows[33]['scan_shows'],P+'10_tuple_relation_gloss.jpg')
dispute('Right gloss, following mark',r'\unsure{à|:}',r'\unsure{à}',r'\unsure{à}',rows[34]['reading'],rows[34]['scan_shows'],P+'10_tuple_relation_gloss.jpg')
dispute('Cancelled axiom fragment',rows[40]['reading'],r'\deleted{\exists\unsure{\mathcal F|F}}',r'\deleted{\unsure{\exists F|\exists\mathcal F}}',rows[40]['reading'],rows[40]['scan_shows'],P+'12_axiom_right_deletion.jpg')
dispute('Overwritten result F_i',rows[43]['reading'],r'\deleted{\unsure{\mathcal F|F}}F_i',r'\deleted{\unsure{\mathcal F}}F_i',rows[43]['reading'],rows[43]['scan_shows'],P+'13_axiom_corrected_fi.jpg')
dispute('Final axiom punctuation',r'\unsure{.|,}','.',',',',',rows[45]['scan_shows'],P+'14_axiom_terminal_relation.jpg')
dispute('Inserted H_i connector','TikZ connector','TikZ connector','insertion macro only',rows[53]['reading'],rows[53]['scan_shows'],P+'16_bottom_initial_deletion.jpg')
dispute('Bottom strates','strates',r'\unsure{strates}','strates',r'\unsure{strates}',d['differences'][-1]['scan_shows'],d['differences'][-1]['crop'])
d['disputes']=dis
# The C context's explicit notation checks also require a disposition.
context_checks=[
 ('Notations, plain F and G forms',r'\pi_0(F),\pi_0(G)',r'\pi_0(F),\pi_0(G)','Straight F arms and open G with its low tail; the pi has two uprights and a low oval index.',f'crops/{K}/a03_Notations_NB.jpg; '+P+'04_notations_cancelled_parenthesis.jpg'),
 ('Notations and C4 bis, family alphabet',r'\mathcal F,\mathcal F_i',r'\mathcal F,\mathcal F_i','The slanting upper arm and curved foot recur in the family arguments, product and live membership.',P+'05_first_superscript.jpg; '+f'readers/{K}/R3/crops/10_c4_cancelled_exists.jpg; crops/{K}/a09_live_family.jpg'),
 ('Notations, first live exponent',r'\pi_0^!',r'\pi_0^!','A separate upright and point remain below the cancelled letters.',P+'05_first_superscript.jpg'),
 ('Notations, quotation strokes',"`` ... ''","``en tenant compte \\unsure{du|des} Sup''",'Paired opening and closing strokes enclose the whole phrase; the separate article doubt remains.',P+'08_quotation.jpg'),
 ('C4 bis and bottom, indices, restriction and Phi',r'F_i,\;F\mid M_i,\;\Phi',r'F_i,\;F\mid M_i,\;\Phi','The indices are short dotted i, the restriction stroke is vertical, and Phi has an oval across its stem.',P+'13_axiom_corrected_fi.jpg; '+f'crops/{K}/a10_Phi_family.jpg'),
 ('Lemma and bottom, abbreviations','f et s; f et s.','f et s; f et s.','Both are abbreviated; only the lower occurrence has a final separate point.',P+'02_lemma_abbreviation.jpg; '+P+'18_disjointe.jpg')
]
for place,c,reading,evidence,crop in context_checks:
 d['c_doubts'].append(dict(location=place,c=c,reading=reading,status='resolved',scan_shows=evidence,crop=crop))
d['c_doubts'].append(dict(location='Bottom, article before ens. (prior C audit)',c='une ens. / un ens. (audit alternatives; C.tex has un ens.)',reading='un ens.',status='resolved',scan_shows='The first word has the joined u/n run and a long exit, with no further e body. The following ens. is separated by a clear gap. The nearby une in une figure has an additional small return.',crop=f'crops/{K}/a11_un_ens.jpg'))
d['notes']={
 'summary':'The opening refers the preceding result to corollary 1 and a lemma: F is of finite type (respectively finite) precisely when its component figures F_i have that property and all but finitely many are empty. The Notations paragraph records pi_0, a map induced by F ≤ G and transitivity, then distinguishes a component notation taking Sup into account from pi_0(F, ≤). A tuple for a contrée carries two linked glosses. C4 bis asserts a global figure restricting to an arbitrary prescribed component family. The lower section begins the residual contrée, support and cosupport: disjointness from every H_i is said to be testable on all strata of F, with C3 cited. The definition introduced by the final Posons continues beyond this page. These are manuscript assertions, not proofs validated in this transcription run.',
 'math_reading_decisions':[
 'The different roles of a figure and a family made the plain F in pi_0(F, ≤) consequential: the crop has straight arms, unlike the looped family symbols elsewhere on this page.',
 'The first surviving exponent has an upright and a point, hence !, below cancelled cat/act. The second has a d-like upper loop and a separate hollow lower point; both components remain in the doubtful transcription.',
 'The expected membership in the C4 bis index clause prompted a close look. Its ink is a straight upright with one rightward bar, so i \\vdash I is preserved literally. No membership sign is substituted.',
 'The third tuple relation and final F_i correction each occupy one worked glyph-sized group. No independently legible complete undertext was established; uncertainty includes correction state instead of asserting a mathematical repair.'
 ],
 'author_checks':[
 'He writes “Attention” (lettering still doubtful) before distinguishing the two component constructions.',
 'The note attached to the third relation reads “qui ne sert … rien ici”; the intervening pourtant has uncertain cancellation and the following two-stroke mark is retained as \\unsure{:|à}.',
 'The claim about strata is attributed by him to “à cause de C3”. Its proof was not reconstructed here.',
 'The unclosed Attention parenthesis, cancelled existential fragment and terminal i \\vdash I remain literal manuscript features. No extra closing parenthesis, grammar repair or index repair was supplied.'
 ],
 'title_dates_pagination':'Manuscript page 65 at top centre, archive scan 66. Headings: Lemme; Notations; Axiome renforcé; C4 bis; Contrée/Contrie résiduelle; Support et cosupport. No date or separate page count appears.'
}
d.update(reader_crop_counts={'R1':19,'R2':16,'R3':16},adjudicator_crop_count=11,
 workflow_note='Three isolated v02 readers, each whole and halves once. Root inspected 22 existing reader crops and 11 new targeted crops; it never viewed a whole or half page. The first display attempt for root crops a01–a03 was truncated and not counted as seen; existing files were subsequently displayed successfully in smaller batches, without recropping. An administrative text-only audit identified six C-context notation checks and the older un/une ens. question requiring explicit record entries; the latter received one new root crop. R2 attempted LuaLaTeX despite the inherited no-compile instruction; the attempt failed before compilation because lualatex.fmt was missing, and no render was viewed. R1 and R3 confirmed no compiler use. Structural validation only for the consolidated page. v03 explicitly forbids compilers and clarifies single rendering of connected glosses. C_context included an unrelated scan-70 reference; readers report not using it.')
def clean(x):
 if isinstance(x,dict):
  return {k:clean(v) for k,v in x.items() if k not in ['bbox_image']}
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,str):return x.replace(str(O)+'/', '')
 return x
d=clean(d)
(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':K,'differences':len(d['differences']),'C_doubts':len(d['c_doubts']),'disputes':len(dis),'remaining':len(d['remaining_doubts'])}))
