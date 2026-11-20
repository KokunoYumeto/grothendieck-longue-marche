"""Root scan 011 decisions after all three readings and individual crop review."""
from pathlib import Path
import json,copy
W=Path(__file__).resolve().parents[1]
R={r:json.loads((W/f'readers/011/{r}/report.json').read_text()) for r in 'ABC'}
text=(W/'readers/011/B/reading.tex').read_text()
if not text.startswith('\\cotefile'):text='\\cotefile{109}\n'+text
(W/'pages/H109-01_109_scan011.tex').write_text(text)
reused={
 'quotes_motives':'readers/011/A/crops/06_motives.jpg',
 'quotes_pursuing_stacks':'readers/011/A/crops/08_title_quotes.jpg',
 'study_interlineation':'readers/011/A/crops/01_studying.jpg',
 'comprehensive_resolved':'readers/011/A/crops/02_comprehensive.jpg',
 'abound_resolved':'readers/011/A/crops/03_abound.jpg',
 'overwritten_of_uncertain':'readers/011/A/crops/04_of_for.jpg',
 'plain_P':'readers/011/A/crops/05_pi.jpg',
 'no_outer_prose_close':'readers/011/A/crops/05_pi.jpg',
 'terminal_comma':'readers/011/A/crops/05_pi.jpg',
 'two_relocation_and_buried_word':'readers/011/C/crops/07_two_relocation.jpg',
 'started_dash':'readers/011/A/crops/09_started.jpg'}
dec=[]
for x in R['C']['changes']:
 d=copy.deepcopy(x);i=d['id'];d['final']=d.pop('reading')
 d['readers']={r:d['final'] for r in 'ABC'}
 d['crops']=[reused[i]] if i in reused else [f'crops/011/{i}.jpg']
 for k in ['crop','source','bbox']:d.pop(k,None)
 d['evidence']='Main reader confirmed on the cited crop: '+d['evidence']
 if i.startswith('quotes_'):
  d['evidence']+=' All three full transcriptions use these double quotes. A and B classified H guillemets as equivalent typography and omitted collation rows; C and the main reader count the visible quote-shape difference under the explicit quotation convention.'
 if i=='two_relocation_and_buried_word':
  d['readers']['A']=r'The \inserted{two} first \deleted{two} volumes'
  d['evidence']+=' A reads the cancelled word without doubt; B, C and the main reader retain two as the best but not fully recoverable reading. The visible raised replacement is not evidence for the hidden middle stroke.'
 if i=='started_dash':
  d['final']=r'started\textendash{} through'
  d['readers']={'A':d['final'],'B':d['final'],'C':r'started\textendash through'}
  d['diff_h']=False
  d['h']='started through; H preceding page note: un petit trait rouge suit aussi « started » à la page 10'
  d['evidence']+=' The H note introducing both sheets, present before their page 9, explicitly records this red stroke on their page 10. That inherited note was absent from the isolated page-11 convenience input. Root therefore does not count an H omission. The empty TeX group after textendash merely preserves the following space.'
 if i=='plain_P':d['consequential']='The mathematical alphabet is plain P, not H’s blackboard P; the barred double-stroked Q remains a subscript. No unstated projective-space index is added.'
 dec.append(d)
cd=[]
for x in R['A']['c_doubts']:
 d=copy.deepcopy(x);d['decision']=('Resolved/confirmed: ' if d['resolved'] else 'Retained: ')+d['reading']
 if 'pi argument' in d['place']:d['confidence']='medium'
 if d.get('crop'):d['evidence']+=' Crop: readers/011/A/'+d['crop']
 cd.append(d)
inv=copy.deepcopy(R['C']['inventory'])
for x in inv:x['sheet_kind']='letter'
notes=copy.deepcopy(R['A']['notes'])+[
 'The Galois-group and fundamental-group examples were checked for transcription: Gal has barred/unbarred double-stroked Q in its subscript; P in the pi example has only one stem. Two opening round delimiters are followed by only one closing round delimiter. The missing prose close is preserved, and the following small slant is read as a comma. This is local notation/delimiter inspection, not a proof or verification of a mathematical claim.',
 'The visible reading two first is retained even though ordinary word order might suggest first two. The live raised two is secure; the older cancelled two has a buried middle stroke and remains doubtful. The overwritten of likewise remains doubtful. The low red stroke after started is a dash, not a comma; H already describes that mark in its note introducing this pair of pages.'
]
rec={'scan':11,'folder':'H109-01','hua_has':'text','filename':'H109-01_109_scan011.tex',
 'readers':['/root/scan011_a','/root/scan011_b','/root/scan011_c'],'brief':'brief_v03.md',
 'decisions':dec,'c_doubts':cd,'doubts':R['C']['remaining_doubts'],'inventory':inv,
 'notes':notes,'check_events':[],'abbreviations':R['C']['abbreviations'],
 'equivalences':['H’s note before their page 9 applies to both scans 010–011. It records the red mark after started and the interlinear two. The stroke is therefore not an H omission; the position of two is nevertheless wrong in H running text and is a substantive difference.','H operatorname/mathrm, bar/overline, emph/uline, struck/deleted and ellipsis macro differences are not counted when content and scope agree. The nine guillemet substitutions are literal glyph differences and are counted.','All three readers and C set the incomplete One of the leading threads line apart. Root additionally inspected the line transition: the previous line fills the width, so a flow/paragraph distinction cannot be established securely from that boundary alone. C’s block structure is retained and no H error is counted for mere reflow.'],
 'coverage':'All three full readings agree except for the cancelled two certainty and insignificant TeX wrappers/space control. All five explicit C doubts, three punctuation alternatives and three notation observations were addressed. Root inspected every differing reading on retained crops; four main text blocks, both inline formulae, six underline spans, three insertions, four deletions and the archive number are covered by 20 inventory rows.',
 'crop_counts':{'A':9,'B':8,'C':7,'main_new':8,'main_reused':9},
 'main_viewed_crops':sorted(set(reused.values()))+sorted(str(p.relative_to(W)) for p in (W/'crops/011').glob('*.jpg'))}
(W/'records/scan011.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2))
with (W/'notation.md').open('a') as f:
 for x in R['A']['notation']:
  f.write('| '+' | '.join(s.replace('|','&#124;') for s in [x['sign'],'011, '+x['location'],x['reading'],x['evidence']])+' |\n')
print('Scan 011 adjudicated:',len(dec),'loci; 5 C changes, 15 H differences; two remaining doubts.')
