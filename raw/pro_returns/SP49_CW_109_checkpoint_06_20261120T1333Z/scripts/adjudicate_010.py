"""Root decisions after independent returns and crop review; no image recognition."""
from pathlib import Path
import json,copy
W=Path(__file__).resolve().parents[1]
R={r:json.loads((W/f'readers/010/{r}/report.json').read_text()) for r in 'ABC'}
text=(W/'readers/010/C/reading.tex').read_text()
(W/'pages/H109-01_109_scan010.tex').write_text(text)
reused={
 'opening_n_possible':'readers/010/C/crops/01_article_correction.jpg',
 'aside_open':'readers/010/C/crops/02_open_parentheses.jpg',
 'aside_close_thus':'readers/010/B/crops/03_him_punctuation.jpg',
 'provocatively_underline':'readers/010/B/crops/04_provocatively_underline.jpg',
 'naive_quotes':'readers/010/C/crops/04_naive_quotes.jpg'}
dec=[]
for x in R['A']['changes']:
 if x['id']=='for_me_insertion':continue
 d=copy.deepcopy(x); i=d['id'];d['final']=d.pop('reading')
 d['readers']={r:d['final'] for r in 'ABC'}
 d['crops']=[reused[i]] if i in reused else [f'crops/010/{i}.jpg']
 if i=='pursuing_quotes':d['crops'].append('crops/010/pursuing_quotes_2.jpg')
 for k in ['crop','source','bbox','other_bboxes']:d.pop(k,None)
 d['evidence']='Main reader confirmed on the cited crop: '+d['evidence']
 if i=='opening_n_possible':
  d['final']=r'a\deleted{\unsure{n}} \inserted{possible}'
  d['readers']={'A':r'a\deleted{n} \inserted{possible}', 'B':r'a\deleted{n} \inserted{possible}', 'C':d['final']}
  d['diff_c']=False;d['confidence']='medium'
  d['evidence']='The live a has an unscored loop. Only the following low character is cancelled; there is no second a. A surviving hump suggests n, as A and B read, but the central original strokes are buried under scoring. The root agrees with C in retaining n as a doubtful reading. The deletion extent is clear even though the cancelled letter is not certain. Possible is below the line with a connector. H explicitly acknowledges its interlineation in its note, so that placement alone is not a separate H difference.'
 elif i=='aside_close_thus':
  d['evidence']='The underline stops before the comma. A comma precedes the closing parenthesis; the next low mark has two legs and is the caret for interlinear thus, not another comma. H includes the comma in its emphasis and prints an extra comma after the parenthesis. H explicitly records the interlineation of thus in its note; that equivalent encoding is not separately counted.'
 elif i in ['heading_plural','thes_final']:
  d['evidence']+=' H transparently marks its extra letter as editorially supplied; the row records an absent-ink addition, not an unmarked misreading.'
 dec.append(d)
cd=[]
for d in copy.deepcopy(R['C']['c_doubts']):
 d['decision']=('Resolved/confirmed: ' if d['resolved'] else 'Retained: ')+d['reading']
 if d.get('crop'):d['evidence']+=' Reader crop: readers/010/C/'+d['crop']
 cd.append(d)
inv=copy.deepcopy(R['C']['inventory'])
for d in inv:d['sheet_kind']='letter'
record={'scan':10,'folder':'H109-01','hua_has':'text','filename':'H109-01_109_scan010.tex',
 'readers':['/root/scan010_a','/root/scan010_b','/root/scan010_c'],'brief':'brief_v02.md',
 'decisions':dec,'c_doubts':cd,'doubts':R['C']['remaining_doubts'],'inventory':inv,
 'notes':R['C']['notes']+['There is no mathematical argument or proof to check on this editorial prose page. The awkward spelling sythesis, the missing final e in Thes, the singular heading Mathématique, and the punctuation are preserved as written. The scope of the red underline within provocatively and the comma/caret distinction at him were decided from ink, not grammar.'],
 'check_events':[],'abbreviations':R['C']['abbreviations'],
 'coverage':'All three readers viewed the whole and each half once, compared every word/state/mark with both witnesses, and returned full page texts. The texts differ only in certainty of the cancelled n (and cote wrapper metadata). The root inspected all witness-disagreement loci on 14 crops and retained both explicit C doubts. All five text blocks, four insertions, two deletions, twelve underline spans and the archive corner number are inventoried.',
 'equivalences':['H explicitly explains the interlineations for me, possible and thus in its page note. Their plain running-text placement is not counted as an omitted insertion where that note supplies the same information.','H emph and struck are treated as equivalent to uline and deleted when their scope agrees. Six visible double-quote versus guillemet differences are counted because quote shape is explicitly required by the task.'],
 'crop_counts':{'A':4,'B':5,'C':4,'main_new':9,'main_reused':5},
 'main_viewed_crops':list(reused.values())+sorted(str(p.relative_to(W)) for p in (W/'crops/010').glob('*.jpg')),
 'display_incident':'An earlier attempt to display five existing crops returned an output-truncation notice without visible images. The five crops were then displayed successfully in smaller groups; this is not counted as a second visual examination.'}
(W/'records/scan010.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
with (W/'notation.md').open('a') as f:
 for x in R['A']['notation']:
  cells=[x['sign'],'010, '+x['location'],x['reading'],x['evidence']]
  f.write('| '+' | '.join(s.replace('|','&#124;') for s in cells)+' |\n')
print('Scan 010 adjudicated:',len(dec),'H loci; 0 C changes; 2 retained doubts.')
