from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan086/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
paths=['crops/scan086/pagination.jpg','readers/scan086/C/crop_C01_section4_low_mark.jpg','readers/scan086/A/A086_07_vertical_trace.jpg','readers/scan086/C/crop_C02_53_under_d.jpg','readers/scan086/C/crop_C03_55_under_f.jpg','readers/scan086/B/B086_07_detached_pair.jpg','readers/scan086/B/B086_04_610_under_i.jpg','readers/scan086/C/crop_C05_610_separator.jpg']
cm=[0,1,None,2,3,None,4,6]
ds=copy.deepcopy(B)
for i,d in enumerate(ds):
    d['id']=f'M086-{i+1:02}';d['crop']=paths[i]
    d['h_reading']=None;d['diff_h']=False;d['marked_in_H']='no'
    d['readers']={'A':A[i]['reading'] or 'Not transcribed: identified as surface disruption','B':B[i]['reading'],'C':C[cm[i]]['reading'] if cm[i] is not None else ('Not transcribed: identified as a surface seam in the notes' if i==2 else 'Not represented in the reading')}
    if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
ds[0]['scan_shows']='Separate short horizontal strokes flank the typed 541. The 5 has its upper bar and lower curve, 4 its crossbar and descender, and 1 a single upright with an upper entry. Main confirms all three readers and restores both pagination dashes omitted by C.'
ds[1]['scan_shows']='A small solid oblique oval lies below and right of the larger hollow-edged typed period. It is appreciably smaller, lighter and off the typed baseline. Main confirms all three graphic readings and uses B’s lower-right placement. The original normal period remains; the extra shape is retained without assigning another period character or an authored punctuation function.'
ds[2].update(reading='',diff_c=False,unresolved=False,alternatives='',confidence='high',kind='other',scan_shows='The retained crop shows a narrow pale channel between irregular grey edges. The channel cuts through a dark typed leader point, leaving separated pieces on its sides, and continues below it. Main agrees with A and C that this is surface disruption rather than a separate drawn line. B’s uncertain vertical graphic is excluded; the decision is recorded although the final absence agrees with witness C.')
ds[3]['scan_shows']='The live d has its tall curled right ascender and lower bowl. An extra rounded contour and middle cross-stroke survive inside and left of the bowl, but the older right-hand contour is covered. Main retains a/e with all three readers. The high curl belongs to the live d; no old accent is securely separate.'
ds[4]['scan_shows']='The live f has a hooked top, long stem, crossbar and baseline foot. A rounded lower enclosure and crowded middle curve remain beneath it. The upper and left parts of that older impression merge with the f, leaving s/b unresolved. Main confirms all three readers’ retained C doubt.'
ds[5]['scan_shows']='Two dark shapes lie above the regular hollow leader dots on a rising left-to-right diagonal. The lower-left one has a compact angular contour; the upper-right one is a narrower tilted oval. Main confirms A/B’s omitted pair and adopts B’s relative spacing. C-reader does not represent it. The shapes are drawn with uncertain origin and function, without assigning a colon or another text character.'
ds[6]['reading']=ds[6]['reading'].replace(r'\unsure{l|t}',r'\unsure{l|t|j}')
ds[6]['readers']['C']=C[4]['reading']+'\n'+C[5]['reading']
ds[6]['alternatives']='Underlying l or t with a displaced or unassigned low trace; underlying j whose foot may account for that low trace. No connection or typing sequence is certain.'
ds[6]['scan_shows']='The corrected position has a crowded upright, a broad upper horizontal fragment and overlapping baseline feet. Below a narrow paper-coloured gap is a short dark low contour: a small left spot and a broader lobed right portion, at approximately the neighbouring q-descender level. Main accepts A’s added j as a possible underletter, while keeping l/t because the upper and connecting contours remain merged. B/C preserve the low contour without assigning it. The final record combines these observations in one inseparable correction locus: l/t/j plus B’s observed low contour, whose assignment remains uncertain and which may be the same old letter’s foot.'
ds[7]['scan_shows']='The separator has a dark angular upper body, a short descending-left member and a pale right edge. Main agrees with all readers that the lower extension favours comma, but the broken impression does not exclude a degraded period. The following capital Adhérence does not settle the ink.'
s=(O/'readers/scan086/B/reading.tex').read_text()
assert s.count(B[2]['reading'])==1
s=s.replace(B[2]['reading'],'')
s=s.replace('% Faint unassigned vertical trace between the preceding leaders and the 4.1 leaders.\n% Material/writing status is uncertain; no handwritten attribution is asserted.\n','')
assert s.count(r'\unsure{l|t}')==1
s=s.replace(r'\unsure{l|t}',r'\unsure{l|t|j}')
s=s.replace('\\noindent\\qquad 6.10.Image','% The low contour is part of this uncertain correction cluster; it may be the old j foot.\n\\noindent\\qquad 6.10.Image')
s=s.rstrip()+'\n\\clearpage\n'
(O/'pages/B37-04_37_scan086.tex').write_text(s)
inv=copy.deepcopy(R['B']['inventory']);inv=[x for x in inv if x['element']!='Unassigned vertical trace']
for x in inv:
    if x['element']=='Older character under i':x['first_words_or_objects']=r'\deleted{\unsure{l|t|j}}'
    if x['element']=='Low residual trace at corrected i':x['first_words_or_objects']='Broken low contour within the same correction cluster; possible old j foot, assignment unresolved'
notes="""Undated typescript contents continuation numbered ‘- 541 -’; archive 85 is recorded in a comment. It has no independent title, signature or total page count. The page contains 25 numbered entries, 3.8–3.10, 4.1–4.6, 5.1–5.5 and 6.1–6.11, plus headings for immersions and reduced schemes, separated morphisms and valuative criteria, and relative finiteness conditions. Entries 3.10 and 6.8 have no dotted leader. No authorial question or explicit doubt is written.

Six overtyped positions remain visible. The two Jacobson initials and the j under n in ‘Détermination’ are confirmed; a/e beneath d and s/b beneath f remain unresolved. The low contour at the corrected i in ‘schématique’ supports adding j to l/t as an alternative, but does not establish its relation to the older letter; its observed shape is retained within the same correction cluster. All five explicit C doubts remain, two with more faithful graphic treatment or revised alternatives. The low mark beside the §4 period and the detached pair above 6.3 have uncertain functions. The pale channel cutting a leader dot is treated as surface disruption, not manuscript writing. H has description only; there are no H collation rows and no mathematical proof or computation is claimed."""
math=copy.deepcopy(R['A']['math_reading_decisions'])
math.append('Main retained comma/period after schéma from its degraded angular impression; the following capital does not supply a punctuation decision. The low contour below the corrected i was compared as part of the same uncertain letter cluster, with j added as a possibility rather than asserted as its identity.')
notation=[copy.deepcopy(x) for x in R['B']['notation'] if x['sign']!='Unassigned vertical trace']
notation.append(copy.deepcopy(R['A']['notation'][6]))
for n in notation:
    if n['sign']=='Unassigned low correction trace':n['evidence']='Short broken low contour with a separate small left spot and broader lobed right part; possibly the old j foot, but assignment to an underletter is unresolved.'
out=dict(scan=86,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=[],slips=['Six overtyped letter positions are retained without replacing their underlying forms by the live corrected words.'],check_events=[],main_crops=json.loads((O/'crops/scan086/manifest.json').read_text()),main_views=paths)
(O/'decisions/scan086.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nScan 086: A/B/C made 7/7/5 crops. Main viewed seven retained reader crops and made one missing pagination crop. The vertical-feature dispute was settled as surface disruption because a pale channel cuts an existing printed leader dot. The detached pair was retained from A/B against its absence in C-reader. The 6.10 underletter and low trace were kept as one linked correction locus: main added A’s j alternative while retaining B’s observed contour with uncertain assignment. All five explicit C doubts remain recorded. Version 9 clarifies that established surface damage is documented as an exclusion, rather than reproduced as an uncertain authored graphic.\n')
print('Wrote scan 086:',len(ds),'decisions;',sum(d['diff_c'] for d in ds),'C differences;',sum(d['unresolved'] for d in ds),'unresolved.')
