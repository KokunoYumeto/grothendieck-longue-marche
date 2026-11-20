"""Main-reader decisions after comparison of all three returns and visual crop review."""
from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[1]
reports={r:json.loads((W/f'readers/009/{r}/report.json').read_text()) for r in 'ABC'}
base=reports['C']
text=(W/'readers/009/C/reading.tex').read_text()
text=text.replace(r'\deleted{\uline{41}}',r'\deleted{\underline{41}}')
text=text.replace(r'\unsure{!|;|!,}',r'\unsure{!,|!}')
(W/'pages/H109-01_109_scan009.tex').write_text(text)

rootcrops={
'heading':'title','coherator-capital':'references25_26','coherator-reference':'references25_26',
'hot-reference':'references25_26','test-entries':'references25_26','modelizer-brace':'modelizer_brace',
'basic-quote':'basic_group','basic-group':'basic_group','strict-capital':'strict_left','test-period':'strict_left',
'simplices-cubes':'simplices_cubes','canceled-34':'deleted34','aspheric-group':'aspheric_group',
'aspheric-underline':'aspheric_group','weak-heading':'weak_heading','weak-closing-parenthesis':'weak_closing',
'local-group':'local_group'}
decisions=[]
for x in base['changes']:
    d=dict(x);d['final']=d.pop('reading');i=d['id']
    d['readers']={r:d['final'] for r in 'ABC'}
    d['marked_in_H']=bool(re.search(r'\\(?:ill|uncertain|unsure)\b',d.get('h') or ''))
    if i in rootcrops:d['crops']=['crops/009/'+rootcrops[i]+'.jpg']
    else:d['crops']=['readers/009/C/'+d['crop']]
    for k in ['crop','source','bbox']:d.pop(k,None)
    d['evidence']='Main reader confirmed on the cited crop: '+d['evidence']
    if i=='fibre':
        d['readers']['A']=r'\unsure{fibre|fiber}'
        d['confidence']='medium';d['kind']='misread word'
        d['evidence']+=' Reader A retained fibre/fiber; the angular r-like turn precedes the terminal low e, so the final retains fibre.'
    elif i=='site-structure':
        d['readers']['B']=r'\unsure{structure|structures}'
        d['evidence']+=' Reader B retained a possible terminal s; the final wave ends the r/e sequence without a further s stroke.'
    elif i=='test-entries':
        d['readers']['B']=r'\inserted{test category(!)}; test-topology'
        d['evidence']+=' B proposed insertion markup for the whole raised entry. The main reader retains a separate indented entry: it has its own leader/reference and no caret placing it inside the lower, still-live test-topology line. Its raised position is preserved in the inventory.'
    elif i=='canceled-41':
        d['final']=r'\deleted{\underline{41}}';d['readers']['B']=d['final']
        d['confidence']='high'
    elif i=='elementary-punctuation':
        d['final']=r'(\unsure{!,|!})';d['readers']['A']=d['final'];d['diff_c']=True
        d['confidence']='medium';d['kind']='misread symbol or index'
        d['evidence']='Main reader: a long upper upright is an exclamation stem, not an upper semicolon dot. The separate lower point has a substantial tail, supporting a touching comma as the first reading, without excluding a flourished dot. A narrowed unresolved reading !, / ! is retained. B and C kept ! / ; / !,; A narrowed it to !, / !.'
    elif i=='weak-abbreviation':
        d['readers']['A']=r'\unsure{m};'
        d['evidence']+=' A retained doubt on m. Comparing the low initial m in the already inspected map-of-objects crop supports the same reduced m here; no a or p follows. It is retained literally, not expanded.'
    elif i=='strict-reference-stop':
        d['readers']['A']='39'
        d['evidence']+=' A treated this as a speck; the main reader retains the discrete round black point adjacent to the numeral, agreeing with B and C.'
    elif i=='local-accent':d['confidence']='high'
    elif i=='weak-connector':d['kind']='misread symbol or index'
    if i=='raised-29':d['readers']['A']=d['readers']['B']=r'$29^{7}$'
    if i=='canceled-square-drawings':
        drawing=re.search(r'\\figure\{.*?\\end\{tikzpicture\}\}',text,re.S).group()
        d['c']=drawing;d['final']=drawing
        d['readers']={r:'Same detailed TikZ geometry, including cancellation paths' for r in 'ABC'}
    if i=='basic-group':
        d['c']=r'two stacked basic/elementary entries, tall right parenthesis'
        d['final']=r'two stacked basic/elementary entries, tall right parenthesis'
    decisions.append(d)

cd=[]
for x in base['c_doubts']:
    z=dict(x);z['decision']=('Resolved: ' if z['resolved'] else 'Retained: ')+z['reading']
    if 'punctuation after elementary' in z['place']:
        z['decision']=r'Narrowed, unresolved: \unsure{!,|!}'
        z['evidence']='Long upper stem establishes an exclamation; the lower dot has a tail compatible with a comma. Semicolon excluded, but !, versus ! retained. Main crop: readers/009/C/crops/06_elementary_punctuation.jpg.'
    if z.get('crop'):z['evidence']+=' Crop: readers/009/C/'+z['crop']
    cd.append(z)
doubts=base['remaining_doubts']
for x in doubts:
    if 'punctuation' in x['place']:
        x['reading']=r'\unsure{!,|!}';x['alternatives']='!,; !';x['confidence']='medium'
        x['reason']='Long upper stem, but the tailed lower point does not distinguish a touching comma from a flourish.'
inventory=base['inventory']
for x in inventory:
    if x['element'] in ['09c','11a','17a','22a']:x['kind']='text'
    if x['element']=='11':x['first_words_or_objects']='elementary modelizer, parenthesized !, or !'
    if x['element']=='18':x['first_words_or_objects']='underlined Weak equivalence; (f:X dash/arrow Y m; of topos; question-mark reference; no closing parenthesis'
record={
'scan':9,'folder':'H109-01','hua_has':'text','filename':'H109-01_109_scan009.tex',
'readers':['/root/scan009_a','/root/scan009_b','/root/scan009_c'],'brief':'brief_v01.md + clarification_scan009.md',
'decisions':decisions,'c_doubts':cd,'doubts':doubts,'inventory':inventory,
'notes':[
'The underlined heading is “Terminology”. This handwritten English index lists terminology and page references: structures, stacks, Coherator, Hot-equivalence, test notions, modelizers, simplices/cubes, aspheric and weak-equivalence terminology, and local variants. No definitions or proofs are stated.',
'The right-column “?” belongs to “Weak equivalence”; it occupies the reference position. There is no other authorial check or proof qualification. No internal page number, date or total page count is stated. Archive pencil number: 8.',
'The modelizer reference forks from 28 to underlined 41 and 42. The basic/elementary group has 29 with a raised crossed 7. Both square drawings and their separate reference 34 are cancelled; the drawing strokes are retained in TikZ.',
'The only mathematical parsing issue is the fragment f:X—Y m; of topos. A morphism reading would suggest an arrow, but the ink supplies only a horizontal stroke with a one-sided thickened tip. The final retains dash/right-arrow doubt and the visibly unmatched opening parenthesis. This is an ink decision, not a proof check.',
'The cropped m resembles the initial compressed m in the explicit addition “map of objects”; the abbreviation is preserved without expansion. The spelling “catégory”, the point in “test.”, and the single leading quote before “basic” are retained. No mathematical proposition was independently checked on this index page.'
],
'check_events':[],'abbreviations':base['abbreviations'],
'coverage':'All three readers read every entry and both halves. Main reader compared full LaTeX returns, all change lists, all 12 C doubt loci, and inventory coverage. Differences in fibre certainty, site ending, insertion status, elementary punctuation, m certainty, and the lower 39 period were decided on crops.',
'crop_counts':{'A':10,'B':14,'C':14,'main_new':11,'main_reused':14},
'main_viewed_crops':['readers/009/C/crops/'+n for n in ['01_structure.jpg','02_fibre.jpg','04_site_structure.jpg','05_canceled_reference.jpg','06_elementary_punctuation.jpg','07_raised_29.jpg','08_strict_deletion.jpg','11_weak_formula.jpg','12_local_accent.jpg','13_strict_reference.jpg','03_stacks_deletion.jpg','09_square_drawings.jpg','10_aspheric_insertion.jpg']]+['readers/009/B/crops/05_test_category.jpg']+['crops/009/'+n+'.jpg' for n in set(rootcrops.values())]
}
(W/'records/scan009.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
with (W/'notation.md').open('a') as f:
    for x in base['notation']:
        cells=[x['sign'],'009, '+x['location'],x['reading'],x['evidence']]
        f.write('| '+' | '.join(s.replace('|','&#124;') for s in cells)+' |\n')
print('Adjudicated scan 009:',len(decisions),'loci; remaining doubts',len(doubts))
