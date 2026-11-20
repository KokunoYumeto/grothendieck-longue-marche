from adjudication_helpers import *

d,rs,ts=start(10)
text=ts['R1'].replace(r'\handwritten{24.4,67}',r'\hfill\handwritten{24.4,67}',1)
form=r'fo\unsure{rm|rmm}ulas'
sep=r'\deleted{sep\unsure{ara}te}'
standard=r'sta\unsure{\deleted{dn}nd|\deleted{nd}dn}ard'
text=text.replace(r'fo\unsure{\deleted{m}r|\deleted{r}m|r}mulas',form)
text=text.replace(r'\deleted{separ\unsure{a|t}te}',sep)
text=text.replace(r'sta\unsure{\deleted{n}d|\deleted{d}n|d}\unsure{\deleted{d}f|\deleted{f}d|f}ard',standard)
text=text.replace('% In the three crowded words above, alternative overprint orders are not treated as established correction chronology.','% Overprint orders are not established. The dn/nd component analysis is itself provisional.\n% The crowded formulas/formmulas run does not establish a separate cancelled impression.')
old=text[text.index(r'\margin{\handwritten'):text.index(r'\normalmarginpar')]
new=r'''\margin{\unsure{\figure{\begin{tikzpicture}[x=.014cm,y=.014cm]
\draw[gray!45,line width=.25pt] (26,64) .. controls (29,51) and (34,35) .. (30,22);
\draw[gray!55,line width=.25pt,dash pattern=on 1pt off 1.2pt] (30,22) .. controls (28,10) and (14,4) .. (0,0);
\end{tikzpicture}}}}
'''
text=text.replace(old,new)
cropmap={1:'readers/scan010/R1/01_date.jpg',2:'readers/scan010/R3/crop_02.jpg',3:'readers/scan010/R1/03_ramification_edge.jpg',4:'readers/scan010/R1/04_deleted_as.jpg',5:'readers/scan010/R1/05_formulas.jpg',6:'readers/scan010/R1/06_deleted_separate.jpg',7:'readers/scan010/R1/07_standard.jpg',8:'crops/scan010/01_year_hyphen.jpg',9:'readers/scan010/R1/08_group.jpg',10:'readers/scan010/R1/08_group.jpg',11:'readers/scan010/R1/10_left_margin_mark.jpg',12:'crops/scan010/02_short_dash.jpg',13:'readers/scan010/R1/09_final_what.jpg'}
r2map={2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:14,12:12,13:13}
r3map={2:3,4:4,5:5,7:6,8:7,9:9,10:10,11:8,12:11,13:12}
evidence={
1:'The handwritten second day digit has the open angular top and long downstroke of 4, not a 9 bowl. The first separator is a compact point; the second is a visibly slanting elongated stroke below the main numeral body. Main reads 24.4,67, resolving C’s separator doubt and rejecting H’s 29 and second point.',
2:'The fourth cell shows a tall serifed upright and a low closed oval crossing it and extending to its right. Main favours R1/R3’s superposed l/o analysis over R2’s single d/h/l candidates. Relative darkness does not establish which impression came first; both orders remain.',
3:'Only the left serifed stem of the terminal cell survives before the physical paper edge. The arch is not complete enough to certify the entire n. Main retains R1/R2’s local n candidate and cutoff comment rather than R3’s certain completion; no wholly absent character is supplied.',
4:'Capital A and low s remain visible beneath crossing cancellation overtypes immediately after these. H omits the two cancelled letters; all readers and C retain them.',
5:'The f, o and terminal u-l-a-s are separable. The intervening low arches and stems are crowded and overlap. Their spacing favours the shorter rm run, but does not securely exclude rmm or identify a distinct cancelled impression. Main selects R2’s formulas-first uncertainty, rejects a confident m/r correction decomposition, and keeps the alternative formmulas.',
6:'The cancelled word has distinguishable initial s-e-p and terminal t-e. Crossed impressions obscure the central three cells, including a tall stroke in the later part. Main narrows C’s whole-word doubt only to ara, following R2; R1’s single-cell doubt is too narrow, while R3’s whole-word retention obscures the clear endpoints.',
7:'Both medial cells have a high right upright with a leftward top serif, plus low bowl/arch traces. These favour superposed n/d components in each cell; the top shape is less like the rightward f hook visible elsewhere in the same crop evidence. Main selects R2’s provisional dn/nd overprint analysis, with both orders and low confidence. The component analysis, as well as chronology, remains uncertain; no selection follows from the expected word standard.',
8:'The year separator is one short horizontal typewriter impression, approximately one character width. H’s en-dash-length rendering is not the visible mark; 1960-61 is retained.',
9:'After The group, the paper has a blank gap, then upright R with a separate underline above a lowered 1. No base pi or other base glyph is visible. The parentheses contain S, a comma and an empty second slot. H supplies a mathematical symbol absent from the ink.',
10:'The closing parenthesis lies immediately beside the physical right edge. No separate terminal point survives on the narrow paper strip; H’s point is omitted without reconstructing anything beyond the edge.',
11:'A faint, thin descending contour bends left at its bottom. The lower part is visibly broken into short darker segments. Main preserves that geometry provisionally in the left margin between items 2 and 3. Neither graphite authorship nor a semantic function can be established; the drawing is locally uncertain and has no definite handwritten attribution.',
12:'The separator before Par.1 is a single short horizontal stroke, similar in width to one typewriter cell. The long dash in H is not supported.',
13:'The last word’s first cell contains the high curled f hook, comparable to the preceding for, and low doubled diagonal/vertical strokes belonging to w. Both impressions survive; their order cannot be recovered. C’s t alternative is unsupported, and H omits the f impression.'
}
for i in range(1,14):
 r=row_from(rs['R1'],i,crop=cropmap[i],scan_shows=evidence[i])
 r['readers']={'R1':rs['R1']['differences'][i-1]['reading']}
 r['readers']['R2']='24.4,67' if i==1 else rs['R2']['differences'][r2map[i]-1]['reading']
 r['readers']['R3']='24.4,67' if i==1 else ('ramification [partly cut final n retained without doubt]' if i==3 else (r'\deleted{\unsure{separate}}' if i==6 else rs['R3']['differences'][r3map[i]-1]['reading']))
 if i==5:r.update(final=form,against_h=False,kind='misread word',confidence='medium')
 if i==6:r.update(final=sep,confidence='medium')
 if i==7:r.update(final=standard,confidence='low')
 if i==9:r['consequential']='Retains the visible R/1 stack and empty second argument; removes H’s supplied pi base.'
 if i==11:r['final']=new.strip()
 d['rows'].append(r)
d['doubts']=[rs['R1']['remaining_doubts'][0],rs['R1']['remaining_doubts'][1],rs['R2']['remaining_doubts'][2],rs['R2']['remaining_doubts'][3],rs['R2']['remaining_doubts'][4],rs['R1']['remaining_doubts'][5],rs['R1']['remaining_doubts'][6]]
d['doubts'][4]['confidence']='low'
d['inventory']=rs['R1']['inventory']
d['inventory'][5].update(kind='text',first_words_or_objects='Crowded formulas/formmulas, no definite cancellation decomposition')
d['inventory'][6]['first_words_or_objects']='Cancelled sep[ara]te; central three cells uncertain'
d['inventory'][7]['first_words_or_objects']='Provisional dn/nd overprint in two medial cells; both orders retained'
del d['inventory'][8]
for inv in d['inventory']:
 if inv['kind']=='display' and inv['position'].startswith('inline'):inv['kind']='text'
 if inv['kind']=='drawing':inv['hand']='origin uncertain: possible hand mark or incidental surface trace'
for i,inv in enumerate(d['inventory'],1):inv['element']=f'E{i:02d}'
d['notes']=rs['R2']['notes']
d['notes']['math_reading_decisions']=[
 'Three underlined upright R forms are retained. Main’s group crop confirms the R/1 stack, missing base glyph and blank second argument; no conventional pi is supplied.',
 'The quotation retains n.th and S. The six headings and proposed appendix name topics; no theorem statement is proved or used as a premise here. All are reported as unverified page content, so no mathematical check event is claimed.',
 'The extra main crop of list numeral 3 shows a flat angular upper stroke, inward diagonal and rounded lower hook. This resembles the already recorded scan008 reference-3 shape and supports the typewriter-first alternative, but one matching outline cannot establish instrument. The scan008 uncertainty is retained unchanged; no old image was re-viewed.'
]
d['check_events']=[]
d['slips']=['to carefully, catégory, Abhyankars, and the verbless The sections 6 to 10 essentially the same are preserved.']
d['workflow']=dict(brief='brief_v007_scan010.md',r1_crops=10,r2_crops=10,r3_crops=11,main_crops=3,main_reader_crops_viewed=10,feedback='Main compared all three returns, viewed ten existing crops and three new crops (two short separators and a numeral comparison). An initial multi-image call exceeded the available context and displayed no usable image; its targets were then viewed once successfully in smaller calls. Final selects R1/R3 opening l/o, R2 formulas and cancelled-separate scope, and provisional R2 dn/nd components. Correction order remains uncertain. A faint curve is retained with uncertain origin. No mathematical checks or external research were performed. The next brief explicitly distinguishes uncertainty in component identification from uncertainty in overprint order, and requires local uncertainty without definite hand attribution for an indeterminate surface trace.')
d['main_adjudication_complete']=True
save(d,text)
