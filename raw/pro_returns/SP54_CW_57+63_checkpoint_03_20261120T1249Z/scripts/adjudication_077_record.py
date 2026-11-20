#!/usr/bin/env python3
"""Record the main reader's completed visual adjudication of scan 077."""
from pathlib import Path
import json,copy
b=Path('/workspace/scratch/b9993b8b5640');o=b/'out';p='A57-02_57_scan077';rp=o/'readers'/p
r={n:json.loads((rp/n/'report.json').read_text()) for n in ['R1','R2','R3']}
map2=[0,1,2,3,4,5,None,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,None,23,24,25,26,27,28,29,30]
map3=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,None,17,18,19,20,21,22,None,23,24,25,26,27,28,29,30]
files=['01_deleted_by_a','02_final_punctuation','03_clipped_S','04_pic_formula','04_pic_formula','04_pic_formula','04_pic_formula','05_have_correction','05_have_correction','06_morphisme_e','07_exact_sequence','07_exact_sequence','07_exact_sequence',None,'08_margin','08_margin','08_margin','08_margin','09_homomorphisme_e','10_morphisms_state','11_specifically_deleted_the','11_specifically_deleted_the','12_f_via','12_f_via','12_f_via','13_deleted_as_you_know','14_finite_insertion',None,None,None,None,None,'19_clipped_of']
paths=[str(rp/'R1/crops'/(f+'.png')) if f else None for f in files]
paths[13]=str(o/'adjudication'/p/'underline_clause.png');paths[27]=str(o/'adjudication'/p/'corollary_number.png')
for i in [28,29]:paths[i]=str(rp/'R3/crops/14_family_and_x.png')
for i in [30,31]:paths[i]=str(rp/'R3/crops/15_corollary_f_finite.png')
shows=[
 'The x cancellation crosses a capital B with two bowls, a descending y, and a separate a after the intervening position. The full By a is recoverable; H omits the a.',
 'An x overprint covers an earlier punctuation position after it. Traces support a colon, while a separate lower full stop remains visible. The cancelled colon retains its C doubt.',
 'At the clipped right edge the upper and lower curves and waist of a capital S remain visible. The letter is resolved, with medium confidence because its rightmost outline meets the dark scan edge.',
 'The raised mark is a compact filled dark spot with no open centre. H cdot and the final bullet encode that same visible filled point; only the C uncertainty is changed.',
 'The first P has displaced overlapping upright and bowl impressions. Those doubled strokes remain visible, while the intended alphabet remains uncertain between the two C candidates.',
 'A separate short narrow raised stroke lies between the target X and its slash. It is distinct from both the X arm and the longer slash. Root follows R1/R2 and H on the prime; the narrow hand-drawn stroke is wrapped as handwritten following R2.',
 'The target formula is followed by a blank typewriter position before the full stop. Root follows R1/R3 on this spacing. The separately recorded target prime is not counted again in this row.',
 'The two angled strokes of the typed v remain below the handwritten replacement s. Both the cancelled typed layer and the live manuscript replacement are preserved.',
 'The following typed e has a surviving curved body crossed by the cancellation. H supplies only has and omits this cancelled final letter.',
 'The x overprint after morphism partly exposes a curved e-like underlayer. Its identity remains uncertain; the cancellation and the tentative e are retained.',
 'The handwritten f crosses most of an older typed character. A rounded body and low trace support tentative g, but the overwritten layer remains too obscured for a confident resolution.',
 'Two parallel horizontal strokes precede h. The upper has a clear right-facing head; the lower ends in a rounded thick terminal whose arrowhead cannot be separated. Both C encodings remain explicit.',
 'The small lower mark on h has distinguishable rays, with the upper portion crowded against the h. The star and upward-mark alternatives remain; no expected descent notation was used to settle it.',
 'A hand-drawn single underline runs under provided we at the right end of one line and continues under replace S by a suitable non empty open set on the next. H records the words without their underline.',
 'The initial of the marginal query consists of open-right curved portions and a short interior trace. The epsilon/e/c/membership candidates remain explicit; the tiny faint form is unresolved.',
 'The marginal word has an n shoulder, small rounded o, and tall crossed t. The word not is readable where H leaves an unreadable marker.',
 'The lower marginal word retains n, two small e forms, a tall d, another e, and a terminal tall d. The joined handwriting supports needed, with medium confidence.',
 'The question mark is visibly separated from the terminal d by a gap. Root follows R1/R2 on needed space question-mark; the uncertainty attached to needed in H is treated in its own row.',
 'A typed x crosses the final e-like letter after homomorphism. The curved underlayer remains partly obscured, so root retains the C/R1/R3 uncertainty rather than adopting R2\'s resolved e.',
 'The final s has extra crossing strokes and extended upper and lower serifs over its curved body. Root reads an x cancellation over s, agreeing with R1/R3 and H, at medium confidence; R2\'s live-state alternative is recorded.',
 'A displaced small e impression overlaps the right of p: its curved lower arm and internal horizontal trace are visible before c. Root resolves specifically following R3; R1\'s uncertain e and R2\'s e/blank alternatives are retained in the comparison.',
 'The crossed word before in occupies three character positions, with t, the tall h and the curved e recoverable. The final group supports the, while H reads that.',
 'The raised mark before via has a dark rounded rim with a pale internal centre. The open-ring reading is retained from C and all three readers.',
 'The raised-f label is immediately followed by via without a separate blank typewriter position. This row records the boundary only; the raised mark has its own row.',
 'A detached dark point sits immediately after u and slightly below its baseline. Its role as intentional punctuation remains uncertain; it is preserved as an uncertain point following R1. R2/R3 and both witnesses have no punctuation at this position.',
 'The cancellation retains recoverable parts of as you know and both, with the intervening comma partly visible. A full blank position between comma and b is not securely recoverable. Root follows R3\'s compact-boundary preference while retaining the spaced alternative; the entire crossed phrase remains uncertain.',
 'The inserted word has a long f stroke, dotted i, n shoulder, second i, tall crossed t and a compact terminal e. The full insertion finite direct sums of is visible within its attachment bracket; finite is resolved at medium confidence.',
 'After Corollary the handwritten mark has a short upright with a leftward flag-like stroke and a detached lower point, above the extended underline. The upper form favors 1, but the detached lower component also supports !. Root retains 1/! alternatives although all readers resolved 1. H omits the entire handwritten mark.',
 'The family subscript has a rounded upper dot above a short stem with a left head-serif and broad foot. Root reads i following C/R2/R3, at medium confidence; R1 retained i/1 and H gives 1.',
 'The X after over has displaced overlapping cross-strokes and doubled edges. The heavy impression supports the C alternatives but does not settle the intended alphabet.',
 'The Corollary raised mark has a dark compact outline and a small pale patch internally. The patch is less distinct than in the factorisation ring. Root retains circle/bullet alternatives following R3; neither a definite ring nor a definite filled point is imposed.',
 'The crossed word retains finit and a partly obscured final cell. An e-like curve is suggested within the cancellation, but its separation remains unclear. Root retains finite/finit following C/R1/R2 rather than resolving it with R3.',
 'The clipped final word retains the round o and the upper hook, upright and cross-stroke of f against the dark edge. The word of is resolved at medium confidence.'
]
conf=['high','medium','medium','high','medium','high','high','medium','medium','medium','low','medium','low','high','low','high','medium','medium','medium','medium','medium','high','medium','high','low','low','medium','low','medium','medium','low','medium','medium']
finals={5:r"\text{\uuline{Pic}}_{X\handwritten{'}/S}",6:r"\text{\uuline{Pic}}_{X\handwritten{'}/S}$ . Assume:",20:'specifically',25:r'\deleted{\unsure{as you know,both|as you know, both}}',27:r'\uline{Corollary \handwritten{\unsure{1|!}}}',28:r'X_{i}',30:r'\unsure{f^{\circ}|f^{\bullet}}'}
changes=[]
for i in range(33):
 reads={'R1':r['R1']['changes'][i]['reading']}
 for n,m in [('R2',map2),('R3',map3)]:
  if m[i] is not None:reads[n]=r[n]['changes'][m[i]]['reading']
  elif i==6:reads[n]=r"\text{\uuline{Pic}}_{X\handwritten{'}/S}$. Assume:"
  elif i==17:reads[n]='needed?'
  elif i==24:reads[n]=r'with $u$ affine'
 x={'source':['R1',i],'reader_readings':reads,'evidence':paths[i],'crop':paths[i],'scan_shows':shows[i],'confidence':conf[i],'mathematical_consequence':None}
 if i in finals:x['final']=finals[i]
 if i==17:x['h_marked']='no'
 if i==20:x.update(differs_c=True,differs_h=False)
 if i in [25,27,30]:x['differs_c']=True
 if i==28:x.update(differs_c=False,mathematical_consequence='The Corollary family index is the letter i; H gives the digit 1.')
 if i==5:x['mathematical_consequence']='The target Picard-functor subscript is X prime/S; C omits the prime.'
 changes.append(x)
cd=copy.deepcopy(r['R1']['c_doubts'])
cdmap=[0,1,2,3,4,9,10,11,12,14,18,20,25,26,29,31,32]
for d,i in zip(cd,cdmap):d.update(evidence=shows[i],crop=paths[i],confidence=conf[i])
cd[11].update(reading='e',status='resolved')
cd[12].update(reading=r'\unsure{as you know,both|as you know, both}',status='revised')
remaining=[]
for i,d in enumerate(copy.deepcopy(r['R1']['remaining_doubts'])):
 if i in [8,11]:continue
 if i==10:d.update(reading=finals[25],alternatives=['as you know,both','as you know, both'],confidence='low',reason=shows[25])
 if i==12:d.update(crop=paths[29],reason=shows[29])
 if i==13:d.update(crop=paths[31],reason=shows[31])
 if i==9:d.update(reason=shows[24])
 remaining.append(d)
remaining += [{'place':'L22, handwritten mark after Corollary','reading':'1','alternatives':['!'],'confidence':'low','reason':shows[27],'crop':paths[27]},{'place':'L24, Corollary raised f mark','reading':r'f^{\circ}','alternatives':[r'f^{\bullet}'],'confidence':'low','reason':shows[30],'crop':paths[30]}]
# Keep physical order in the unresolved list.
remaining.sort(key=lambda d: (17 if d['place'].startswith('Margin') else int(__import__('re').search(r'L(\d+)',d['place']).group(1)),d['place']))
inv=copy.deepcopy(r['R3']['inventory'])
inv[11]['first_words_or_objects']='f raised filled point; double-underlined Pic_X/S to double-underlined Pic_X prime/S; then space and full stop'
inv[30]['first_words_or_objects']='uncertain epsilon/e/c/membership initial; not / needed ?'
inv[38]['first_words_or_objects']='f with filled raised point = vu with u followed by an uncertain point, then affine'
inv[42]['first_words_or_objects']='handwritten 1/! alternatives, with underline continuation'
inv[46]['first_words_or_objects']='finite/finit alternatives under x overstrikes'
inv.insert(13,{'sheet_kind':'letter','hand':'another unnamed hand','element':'pending','kind':'insertion','position':'L12, target Picard subscript','first_words_or_objects':'separate raised prime between X and slash','transcribed':'yes'})
notes={'summary':'The page continues the statement about the n.th power homomorphism in the Picard prescheme. It discusses a method involving non flat descent and the absence of a good effectivity criterion, then states a theorem and a Corollary about representability of Picard-functor homomorphisms. It writes an exactness expression, discusses the factorisation vu, and begins a final continuation. The replacement-of-S clause is underlined and accompanied by a marginal question. These are attributed source statements; no proof verification was performed.',
 'reading_decisions':[{'place':'L12, Picard-functor map','readings':r'X/S versus X\prime/S in the target','reason':'R1/R2 read a prime and R3 read no prime. The separate short stroke between X and slash decides X prime/S. The source and target labels were read from ink without using an expected variance of the functor.'},{'place':'L16, exactness expression','readings':r'\rightrightarrows versus upper arrow/lower bar; h_* versus h_{\uparrow}','reason':'The small lower arrow terminal and the subscript rays remain unresolved in the crop. The alternatives were retained without supplying conventional descent notation.'},{'place':'L23, family subscript','readings':r'X_i versus X_1','reason':'The rounded upper dot and lower stem support i. No choice was made from what an indexing family ought to be.'},{'place':'L19 and L24, raised f marks','readings':r'f^{\circ}; f^{\circ}|f^{\bullet}','reason':'The factorisation mark has a pale open centre; the Corollary mark has a smaller indistinct pale patch, so its ring/filled-point alternatives remain.'}],
 'author_checks':[{'place':'L04','quote':'I do not have any good effectivity criterion'},{'place':'L14','quote':'this is certainly true when $X/S$ is projective'},{'place':'Left margin beside L17','quote':r'\unsure{$\epsilon$|e|c|$\in$} not / needed ?'}],
 'titles_dates_pagination':[{'place':'L10','text':'Theorem','form':'typed, singly underlined'},{'place':'L22','text':r'Corollary \unsure{1|!}','form':'typed heading with manuscript mark and underline extension'},{'place':'Lower left','text':'76','form':'pencil archive number, transcribed as comment'},{'place':'Sheet','text':'No date, signature, authored pagination or explicit total page count is recorded on this continuation.'}]}
notation=copy.deepcopy(r['R1']['notation'])
notation[2].update(sign='open raised f mark',place='L19',visible_shape='Dark small round rim with a pale internal centre.')
notation[4]['latex']=finals[5]
notation[10].update(latex=r'X_i',visible_shape=shows[28],alternatives=[])
notation += [{'sign':'Corollary raised f mark','latex':finals[30],'place':'L24','visible_shape':shows[30],'alternatives':[r'f^{\circ}',r'f^{\bullet}']},{'sign':'heading manuscript mark','latex':r'\handwritten{\unsure{1|!}}','place':'L22 after Corollary','visible_shape':shows[27],'alternatives':['1','!']},{'sign':'possible punctuation point','latex':r'$u$\unsure{.}','place':'L20','visible_shape':shows[24],'alternatives':['punctuation point','incidental ink mark']}]
repl=[(r"\text{\uuline{Pic}}_{X'/S}",finals[5]),(r'sp\unsure{e}cifically','specifically'),(r'\deleted{\unsure{as you know, both}}',finals[25]),(r'\uline{Corollary \handwritten{1}}',finals[27]),(r'X_{\unsure{i|1}}',r'X_{i}'),(r'namely $f^{\circ}$',r'namely $\unsure{f^{\circ}|f^{\bullet}}$')]
cfg={'base_reader':'R1','replacements':[{'old':a,'new':z} for a,z in repl],'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inv,'notes':notes,'notation':notation,'adjudicated_crops':list(dict.fromkeys(paths)),'rejected_difference_rows':[]}
(o/'adjudication'/p/'decision.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2))
with (o/'notation.md').open('a') as f:
 f.write('\n## Evidence added at cote 57, scan 077\n\n| Sign | Reading | Place | Visible form / residual alternatives |\n|---|---|---|---|\n')
 for n in notation:f.write('| '+n['sign']+' | `'+n['latex'].replace('|',r'\|')+'` | '+n['place']+' | '+n['visible_shape'].replace('|',r'\|')+' |\n')
brief=(o/'briefs/reader_brief_v06.md').read_text().replace('brief v06','brief v07',1).replace('First used: cote 57, scan 077.','First used: cote 57, scan 078.',1)
brief+='\n\n## Clarifications introduced in v07\n\n- Inspect manuscript marks in headings as carefully as formula exponents. A numeral-like upper flag combined with a detached lower point can leave numeral/punctuation alternatives unresolved; expected numbering cannot settle that shape. On scan 077 the main crop retained 1/! although the three readers gave 1.\n- Return titles_dates_pagination as a list of strings or of objects with place, text and form, so the visible headings, dates and page counts are retained completely in the assembled notes.\n'
(o/'briefs/reader_brief_v07.md').write_text(brief)
fp=o/'records/brief_changes.json';v=json.loads(fp.read_text());v.append({'version':'v07','first_page':'A57-02_57_scan078','reasons':['All three scan-077 readers gave 1 after Corollary, while the main crop exposed a detached lower point leaving 1/! open. Heading numerals and punctuation now receive explicit attention.','Scan-077 readers supplied title/date metadata as a dictionary rather than the note-section list used in assembly. The list form is now explicit; the main record preserves all values.']});fp.write_text(json.dumps(v,ensure_ascii=False,indent=2))
with (o/'records/tool_delivery_notes.md').open('a') as f:f.write('\nScan 077: all crop outputs reached the main reader individually. R1/R3 preserved the space after the Pic formula; R2 did not. The full-text comparison exposed that difference. R1 alone recorded a possible point after u; the main crop retained it as uncertain. The main heading crop introduced 1/! uncertainty after Corollary despite three numeral-1 readings. No already settled place was recropped.\n')
print('Page 077 decision specification written; 33 rows, '+str(len(remaining))+' remaining doubts, '+str(len(inv))+' inventory elements.')
