"""Assemble root's crop-based decisions for the 162-1 cover."""
from pathlib import Path
import copy, json

O = Path(__file__).resolve().parents[1]
stem = 'H162-01_162-1_scan002'
reports = {r: json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
texts = {r: (O/'readers'/stem/r/'reading.tex').read_text() for r in reports}
t = texts['R2']
old = r'''    \draw[line width=.25pt] (7,22)--(27,8).. controls (35,4) and (38,2) .. (35,0);
    \fill (35,1) ellipse (2 and 2.5);
    \fill (2,28) circle (1.1);'''
new = r'''    \fill (1,25) circle[radius=.65];
    \draw[line width=.20pt] (6,24)--(31,5);
    \draw[line width=.40pt] (31,5)..controls(35,2)and(34,0)..(29,0);'''
assert t.count(old) == 1
t = t.replace(old,new)
base = reports['R2']
R1 = 'readers/'+stem+'/R1/crops/'
diffs = {d['id']: d for d in base['differences']}
trace = '\\unsure{\\begin{tikzpicture}[x=.0078cm,y=-.0078cm,baseline=0pt]\n'+new+'\n  \\end{tikzpicture}}'
overrides = {
 'R2-D01': {
  'crop':R1+'roman.png',
  'readers':r'R1 and R3: $\overline{\underline{\mathrm{III}}}$; R2: ordinary III with two explicit slightly sloping rules. All resolve III. Final uses R2’s literal rules; this encoding distinction alone is not a C correction.',
  'evidence':'Three separate upright shafts stand between an uneven upper cap and a longer lower rising rule. The root crop confirms III and both strokes. H marks the numeral uncertain within its cover synopsis and omits the rules.'},
 'R2-D02': {
  'crop':R1+'parenthetical.png',
  'readers':r'R1: (\unsure{8|8.}\ \raisebox{-.3ex}{\unsure{p|p.}}); R2/R3: (\unsure{8|8.}\ \unsure{p|p.}). All retain both punctuation doubts. Final keeps R2’s ordinary p descender and the smaller pencil-note font; no extra lowered baseline is asserted.',
  'evidence':'Opposing curved brackets surround a double-bow 8 and a p-shaped stem with an upper loop. The p descends below the numeral. The tiny low points cannot securely be separated from the mottled surface, so C’s two punctuation alternatives remain. H’s synopsis leaves the entire parenthesis explicitly unread.'},
 'R2-D03': {
  'crop':'decisions/rootcrops/'+stem+'/upper_arrangement.png',
  'H':reports['R3']['differences'][0]['H'],
  'readers':'R1/R2/R3 all put III far left of the upper-right title and the parenthetical count below and slightly right of III. R1 preserves the full blank cover height; R2/R3 use an upper annotation panel. Final uses R2’s smaller pencil-note scale and coordinates, preserving all written elements without making blank height a textual difference.',
  'evidence':'The root’s single new upper-arrangement crop shows Papiers prêtés at the upper right and the faint two-line pencil group far to its left. This is not the right-margin arrangement produced by C’s margin macros. H’s quoted words are compatible editorial placement synopsis, not source text or a contrary reading.'},
 'R2-D04': {
  'crop':R1+'right_trace.png', 'final':trace, 'confidence':'medium',
  'readers':'R1: one hooked path, no detached point; R2: diagonal, rounded dark terminal and detached low-left point; R3: connected diagonal and left-returning hook plus detached point. The root chooses R3’s hooked contour and R2/R3’s detached point, at R2’s scale and placement. Function and ink-versus-surface status remain doubtful.',
  'evidence':'The local root view shows a thin rising diagonal, tapering at lower left and curling into a darker upper-right head that returns a short way left. A small separate dark point lies further down-left. The final two path pieces share (31,5); the point is separately drawn. No character, arrow or purpose is assigned, and the point may be an unrelated surface speck.'}
}
inv = copy.deepcopy(base['inventory'])
for item in inv:
 item['transcribed']='yes'
 if isinstance(item['position'],dict): item['position']='Whole-image box '+str(item['position']['bbox'])
 if item['element']=='Archive sheet number':item['element']='Archive sheet number, required comment only'
 if item['element'] in ('Roman numeral with top and bottom rules','Parenthetical count and abbreviation'):item['kind']='margin note'
cd = copy.deepcopy(base['c_doubts'])
for item in cd:
 item['crop']=R1+('roman.png' if 'Upper pencil' in item['place'] else 'parenthetical.png')
rd = copy.deepcopy(base['remaining_doubts'])
rd[-1]['reading']=trace
for item in rd:
 if isinstance(item['alternatives'],list):item['alternatives']='; '.join(item['alternatives'])
notes=(O/'decisions'/f'{stem}_pending_notes.md').read_text().split('\n\n',1)[1]
spec={
 'stem':stem,'base_reader':'R2','brief':'reader_v13.md',
 'text_edits':[{'old':texts['R2'],'new':t}],
 'exclude_difference_ids':['R2-D05'],
 'difference_overrides':overrides,'additional_differences':[],
 'c_doubts':cd,'remaining_doubts':rd,'inventory':inv,'notes':notes,
 'abbreviations':[{'form':'p (possibly p.)','expansion':'page(s), editorial proposed expansion only; the abbreviation is not expanded in the source text.'}],
 'main_new_crops':1,'consequential':[],
 'check_events':[{'statement_id':'162-1-002-package-count','who':'GPT-6 Astra Pro; effort not exposed; root','type':'used and rechecked in this run','outcome':'Counted page_order.json entries for cote 162-1 after scan 002: eight, scans 003–010. This checks the supplied package count only, not the number of physical sheets, their writing, or the expansion of p. No other-page image was used for this check.'}],
 's_decisions':[],
 'workflow_note':'Three fresh readers used v13, with 3/2/3 crops. Root compared all complete texts/reports and viewed three existing R1 crops plus one new bounded upper-arrangement crop. All readers resolve III and retain C’s punctuation doubts. R1 omitted the detached point from its trace drawing; root selected the point present in R2/R3 and the left-returning hook in R3. C’s recovered scan-002 metadata was sent to each reader before completion after zero-padded keys defeated the original packet filter. A text-only audit of the twelve earlier packets found no missing current-page table rows. R2’s archive-number-only difference is excluded: C’s required comment and H’s page marker do not establish a contrary manuscript reading. The archive mark remains in all readings and the inventory. Invalid verbose yes values are normalized to the required inventory enum. v14 will clarify metadata-only exclusions and exact inventory values; a per-page metadata recovery script prevents recurrence of the packet-selection issue.'
}
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(json.dumps({'page':stem,'loci':4,'inventory':len(inv),'doubts':len(rd)}))
