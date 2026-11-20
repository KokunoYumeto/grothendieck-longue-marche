from pathlib import Path
import json, copy
o=Path(__file__).resolve().parent.parent
p='H63-01_63_scan003'; rp=o/'readers'/p; ap=o/'adjudication'/p; ap.mkdir(exist_ok=True)
r={k:json.loads((rp/k/'report.json').read_text()) for k in ['R1','R2','R3']}
paths=[str(rp/'R1'/s) for s in ['01_entry3.png','02_application.png','03_entry7.png','05_page7.png']]
shows=[
 'The initial has two high joined arms, visibly taller than the following e. Its height favors W, but the arms are short relative to the adjacent M and the case remains uncertain. The raised pale fleck before Minimal is preserved separately as an uncertain apostrophe.',
 'One small detached dark point follows the final n of Application. There is no second vertically aligned point.',
 'The separator after 7 is a low oblique mark, tapering toward the upper right and extending down to the left. It is retained as a comma.',
 'A short hooked cap runs rightward into a slanting descending stroke; a detached point lies almost directly below its end. The cap and diagonal favor 7 followed by a low point, but their arrangement also permits a question mark. The expected page sequence does not decide the glyph.'
]
reads=[{'R1':'weierstrass','R2':r'\unsure{weierstrass|Weierstrass}','R3':r'\unsure{Weierstrass|weierstrass}'},dict.fromkeys(r,'.'),dict.fromkeys(r,','),{'R1':r'\unsure{?|7.}','R2':'7.','R3':'7.'}]
changes=[]
for i in range(4):
 x={'source':['R3',i] if i<3 else ['R1',3], 'reader_readings':reads[i], 'evidence':paths[i], 'crop':paths[i], 'scan_shows':shows[i], 'confidence':['medium','high','medium','medium'][i], 'mathematical_consequence':None}
 if i==3:
  x['final']=r'p~\unsure{7.|?}'; x['reader_readings']={k:'p~'+v for k,v in x['reader_readings'].items()}
 changes.append(x)
cd=copy.deepcopy(r['R3']['c_doubts'])
for d,i in zip(cd,[0,0,1,2]):d.update(crop=paths[i],evidence=shows[i])
cd[0]['evidence']='A small raised brown vertical fleck precedes the M. Its intended textual role remains uncertain; no closing quotation mark is supplied.'
remaining=copy.deepcopy(r['R3']['remaining_doubts'])
remaining[0].update(crop=paths[0],reason=cd[0]['evidence'])
remaining[1].update(crop=paths[0],reason=shows[0])
remaining.append({'place':'Entry 6, page reference','reading':r'p~\unsure{7.|?}','alternatives':['p 7.','p ?'],'confidence':'medium','reason':shows[3],'crop':paths[3]})
inv=copy.deepcopy(r['R3']['inventory'])
for x in inv:x['sheet_kind']='list'
inv[6]['first_words_or_objects']='6. The Neron minimum model; uncertain p 7. / p ?'
inv[-1]['kind']='text'
notes=copy.deepcopy(r['R3']['notes'])
notes['titles_dates_pagination'][6].update(text='p 7. / p ? (uncertain)',form='handwritten reference with a low detached point')
notes['titles_dates_pagination'].append({'place':'Page','text':'No date, signature or author page count is visible','form':'absence reported by all three whole-page readers'})
notes['reference_decision']=shows[3]
notation=copy.deepcopy(r['R3']['notation'])
notation[-1]['visible_shape']=shows[0]
notation.append({'sign':'reference numeral and low point','latex':r'\unsure{7.|?}','place':'entry 6','visible_shape':shows[3],'alternatives':['7.','?']})
prior=copy.deepcopy(r['R3']['prior_flags'])
prior[3].update(reading=r'p 1., p 2., p 3., p 4., p 6., p \unsure{7.|?}, p 8., p 10.; coördinates',status='other references confirmed; entry 6 left uncertain after main crop review')
cfg={'base_reader':'R3','replacements':[{'old':r'model \qquad p~7.','new':r'model \qquad p~\unsure{7.|?}'}], 'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inv,'notes':notes,'notation':notation,'prior_flags':prior,'adjudicated_crops':paths,'reader_only_decisions':[],'rejected_difference_rows':[]}
(ap/'decision.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2))
with (o/'notation.md').open('a') as f:
 f.write('\n## Evidence added at cote 63, scan 003\n\n| Sign | Reading | Place | Visible form / residual alternatives |\n|---|---|---|---|\n')
 for n in notation:f.write('| '+n['sign']+' | `'+n['latex'].replace('|',r'\|')+'` | '+n['place']+' | '+n['visible_shape'].replace('|',r'\|')+' |\n')
with (o/'records/tool_delivery_notes.md').open('a') as f:
 f.write('\n- Scan 63/003: the first root delivery of R1/01_entry3.png was explicitly discarded for context/output limits. The same existing crop was resent successfully; no second crop was made and only the successful delivery counts as a root view. All four adjudication crops were then viewed one per result.\n')
print('003: four C changes, three remaining doubts, ten inventory elements. Brief v09 retained; the disagreements were glyph uncertainty, already covered by its instructions.')
