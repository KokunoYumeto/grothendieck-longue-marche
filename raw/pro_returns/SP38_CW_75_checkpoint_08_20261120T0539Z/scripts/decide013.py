from pathlib import Path
import copy,json

root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan013'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan013_main_observations.json').read_text())
ob={x['id']:x for x in obs['observations']}
def get(r,k):return next(f for f in rep[r]['findings'] if f['id']==k)
def vals(r,ks):return '; '.join(get(r,k)['final'] for k in ks.split('+'))
def rr(r,n):
    names={
      ('R2',1):'01_vertical_label',('R1',2):'02_splitte',('R1',3):'03_cancelled_une',
      ('R1',4):'04_torseur_preposition',('R1',5):'05_cancelled_sous',('R2',6):'06_overwritten_field',
      ('R2',7):'07_deleted_word',('R2',8):'08_box_S_subscript',('R2',9):'09_A2',
      ('R2',10):'10_field_stack',('R2',11):'11_bottom_correction',('R2',12):'12_top_shafts',
      ('R2',13):'13_bottom_shafts',('R2',14):'14_detached_pair_upper',('R1',13):'13_detached_point',
      ('R2',16):'16_detached_pair_box'}
    return f'readings/scan013/{r}/{names[(r,n)]}.png'
def mm(n):
    return 'crops/scan013/'+{1:'01_rmq',2:'02_both_un',3:'03_formula_left',4:'04_divider',5:'05_phrase_parenthesis',6:'06_box_layout',7:'07_lower_layout',8:'08_tags',9:'09_lower_point'}[n]+'.png'
cp={
 'C01':[rr('R2',1)],'C02':[rr('R1',2)],'C03':[mm(1)],'C04':[rr('R1',3)],
 'C05':[rr('R1',4)],'C06':[rr('R1',5)],'C07':[rr('R2',6)],'C08':[rr('R2',7)],
 'C09':[rr('R2',8)],'C10':[rr('R2',8)],'C11':[rr('R2',9)],'C12':[rr('R2',10)],'C13':[rr('R2',11)],
 'N01':[mm(2)],'N02':[mm(3)],'N03':[mm(4)],'N04':[rr('R1',4)],
 'N05':[mm(5),rr('R2',7)],'N06':[mm(5),rr('R2',6)],'N07':[mm(6)],'N08':[mm(6)],
 'N09':[rr('R2',10)],'N10':[rr('R2',12)],'N11':[rr('R2',13)],'N12':[rr('R2',12)],'N13':[rr('R2',13)],
 'N14':[rr('R2',14)],'N15':[rr('R1',13)],'N16':[rr('R2',16)],'N17':[mm(7)],
 'N15a':[rr('R1',13)],'N18':[rr('R2',10)],'N19':[mm(8)],'N20':[mm(9)],'N21':[rr('R2',11)]}
mapping={f'C{i:02d}':(f'C{i:02d}',f'C{i:02d}') for i in range(1,14)}
mapping.update({
 'N01':('F15','F03'),'N02':('F16',''),'N03':('F17','F04'),'N04':('F18','F05'),
 'N05':('F19','F06'),'N06':('F20',''),'N07':('F22','F08'),'N08':('F21',''),
 'N09':('','F09'),'N10':('F14','F01'),'N11':('F14','F02'),'N12':('F14','F02'),
 'N13':('F14','F02'),'N14':('F24','F11'),'N15':('F25',''),'N16':('','F12'),'N17':('','')})
fallback={
 ('N02','R3'):'reading.tex places Z.Aut(Z). on a separate left-starting line.',
 ('N06','R3'):'reading.tex ends the underline after the canceled preposition, before the field.',
 ('N08','R3'):'reading.tex and inventory reproduce the open frame; no separate F07 finding was supplied.',
 ('N09','R1'):'reading.tex draws a rotated two-component simeq, but the report treats H wr as equivalent notation.',
 ('N15','R3'):'No point by or to the right of the divider in reading.tex or inventory.',
 ('N16','R1'):'No detached pair to the right of the box in reading.tex or inventory.',
 ('N17','R1'):'reading.tex places the A3 identity in a separate centered display.',
 ('N17','R3'):'reading.tex places the A3 identity in a separate centered display.'}
fs=copy.deepcopy(rep['R2']['findings'])
assert len(fs)==30
for f in fs:
    k=f['id'];r1,r3=mapping[k];o=ob['N15b' if k=='N15' else k]
    f['readers']={'R1':vals('R1',r1) if r1 else fallback[(k,'R1')],'R2':f['final'],'R3':vals('R3',r3) if r3 else fallback[(k,'R3')]}
    f['crop']='; '.join(cp[k]);f['evidence']=o['evidence']
    f['decision']='All three complete returns were compared before main crop inspection. '+o['decision']+'.'
by={f['id']:f for f in fs}
def upd(k,**kw):by[k].update(kw)
upd('C01',consequential=True,math_note='H supplies id although the ink remains 2|wr. Splitting follows for the pullback/kernel-isomorphism interpretation; M013-ARBITRARY gives a counterexample for an unrestricted extension morphism. The mathematics does not select the label.')
upd('C02',final=r'\unsure{splitte|splitt.}',diff_c=True,doubt_action='retain',confidence='medium',decision='Retain R1’s two ending alternatives. R2/R3 resolve splitte, but the detached flat ending cannot securely distinguish a compressed e from an abbreviation stop; no accent is supplied.')
upd('C03',final=r'\inserted{Rmq} raised above Toute, with its curved headless lead',doubt_action='resolve',confidence='high',decision='All readers and main resolve the abbreviation. Preserve its raised placement and actual lead; do not expand it to H Remarque.')
upd('C06',final=r'\unsure{\deleted{sous}|\deleted{sur}|sous|sur}',doubt_action='retain',decision='Use R1’s explicit lexical and live/canceled alternatives. R2/R3 regard the crossing as a definite cancellation; main cannot separate it securely from the thick cursive joins.')
upd('C10',final='2',doubt_action='resolve',diff_c=True,diff_h=False,confidence='medium',decision='Resolve the hooked descending index with its long low foot as 2, agreeing with R1. R2/R3 retain n as an alternative. The group-order check was not used to decide the ink.')
upd('C11',place='First rounded A, in the parenthesis below the box',c=r'\unsure{\mathcal{A}|A}_2',h=r'\mathfrak{A}_2',final=r'\unsure{\mathcal{A}|A}_2',decision='Retain calligraphic/plain cursive A with all three readers; later A3 uses the primary alphabet without repeating the glyph doubt. The later H alphabet difference is recorded separately at N21.')
upd('C12',final=r'\rotatebox{90}{$\unsure{\simeq|=}$}',doubt_action='retain',diff_c=False,diff_h=False,confidence='low',decision='Retain R1/C’s two alternatives: the heavy retracing obscures the original relation. R2/R3 resolve simeq. H describes simeq in a note, so the glyph-confidence difference is excluded; the missing drawn geometry is N18.')
upd('C13',doubt_action='resolve',decision='Choose R2/R3’s canceled doubled Z: two old oblique strokes and the base survive beneath F. R1 retains an alphabet doubt. The live F3-plus remains unchanged.')
upd('N02',c=r'\[Z.\operatorname{Aut}(Z).\]',h=r'... splittée $Z.\operatorname{Aut}(Z)$.',final='Z.Aut(Z). on a separate left-starting line',kind='insertion or placement',decision='Correct R2’s witness quotation: both C and H already contain the terminal period. Count only the separate left-starting placement, against C’s centered display and H’s inline formula.')
upd('N04',final=r'\unsure{torseur|torseurs}',diff_c=True,diff_h=True,confidence='medium',decision='Retain R1’s new singular/plural doubt. R2/R3 resolve singular; the detached low ending leaves a compressed extra s possible. Singular remains primary.')
upd('N08',decision='Preserve the enclosure’s two open corners in TikZ. R3’s text and inventory agree despite the missing numbered finding; the glyph crop alone did not show the upper-left corner, hence the new geometry crop.')
upd('N09',decision='Draw the two visible components of rotated simeq. H’s single wr is not one of its declared alphabet macro equivalents; it leaves out the separate straight component.')
upd('N10',decision='Retain R2’s new connector-head doubt. R1 reads a headless shaft and R3 a right arrow; the small terminal spur does not establish two clear wings.')
upd('N11',decision='Retain R2’s new connector-head doubt; R1/R3 read a headless shaft. The separate downward spur does not securely establish an arrowhead.')
upd('N14',kind='drawing or diagram',decision='Preserve the detached pair geometrically with writing-versus-surface uncertainty and unnamed hand; do not assign a punctuation or mathematical value.')
upd('N15',kind='drawing or diagram',decision='Preserve the remote point as an uncertain drawn trace. R1/R2 include it, R3 omits it. The separate tiny point under the lower rule end is N15a.')
upd('N16',kind='drawing or diagram',decision='Preserve R2/R3’s detached oblique pair with uncertain writing status; R1 omits it. Record unnamed hand.')
upd('N17',decision='Use R2’s shared display block, preserving the slight indentation of A3 from the S3 chain start. R1/R3’s separate centered formula changes this observed relation.')

def add(k,place,c,h,final,readers,kind='drawing or diagram',dc=True,dh=True,confidence='low',o=None,decision=''):
    z=ob[o or k]
    f=dict(id=k,place=place,c=c,h=h,final=final,readers=readers,crop='; '.join(cp[k]),evidence=z['evidence'],kind=kind,diff_c=dc,diff_h=dh,marked_in_H=False,confidence=confidence,decision=decision,doubt_action='',s_id='',math_note='')
    fs.append(f);by[k]=f
add('N15a','Tiny detached point below the lower divider endpoint','absent','absent','uncertain drawn point',{'R1':'Included in F25 and reading.tex','R2':'Absent from reading.tex and inventory','R3':'Absent from reading.tex and inventory'},decision='Retain R1’s tiny point separately from the remote divider point, with writing-versus-surface uncertainty.')
add('N18','Drawn vertical comparisons below the two field factors','Both vertical signs drawn','Described only in a note; no signs drawn in the actual display',r'\rotatebox{90}{$\unsure{\simeq|=}$} and \rotatebox{90}{$=$}',{'R1':'Both drawn in reading.tex; H geometry omission not counted','R2':'Both drawn in reading.tex; H geometry omission not counted','R3':'Both drawn in reading.tex; H geometry omission not counted'},dc=False,confidence='high',decision='The report note does not reproduce these written strokes. Count their missing drawn pair once, apart from C12’s retained glyph doubt.')
add('N19','Distance of the extension tags from terminal ones','Tags in a separate last column','Tags in a separate last column','Same last-column tags with a visibly broad blank gap',{'R1':'Added 3em gap','R2':'Added 3em gap','R3':'Ordinary intercolumn gap'},kind='insertion or placement',dc=False,dh=False,confidence='high',decision='Choose R1/R2’s broad gap. Since both witnesses already put the tags in the correct separate column, this is an uncounted spacing refinement, not a substantive collation error.')
add('N20','Detached point below the left side of the lower quotient','absent','absent','uncertain drawn point',{'R1':'Absent','R2':'Absent','R3':'Absent'},decision='Newly exposed during the missing layout review; inspected once in a new tight crop. Preserve the compact point without punctuation value; writing versus surface remains unresolved.')
add('N21','Alphabet of the final A3',r'\mathcal{A}_3',r'\mathfrak{A}_3',r'\mathcal{A}_3',{'R1':get('R1','F23')['final'],'R2':r'\mathcal{A}_3 in reading.tex and C11','R3':get('R3','F10')['final']},kind='misread symbol or index',dc=False,confidence='medium',o='C11',decision='Use the same primary open-bowl A alphabet as the first occurrence, with no repeated uncertainty. The separate final occurrence is a substantive alphabet difference from H.')

text=(root/'readings/scan013/R2/reading.tex').read_text()
text=text.replace('$(E)$ splitte,',r'$(E)$ \unsure{splitte|splitt.},')
text=text.replace(r'$\longleftrightarrow$ torseur ',r'$\longleftrightarrow$ \unsure{torseur|torseurs} ')
text=text.replace(r'\uline{espace affine \deleted{\unsure{sous|sur}}}',r'\uline{espace affine \unsure{\deleted{sous}|\deleted{sur}|sous|sur}}')
text=text.replace(r'\unsure{\mathfrak{S}|\mathcal{S}}_{\unsure{2|n}}',r'\unsure{\mathfrak{S}|\mathcal{S}}_2')
text=text.replace(r'\rotatebox{90}{$\simeq$}&\quad\rotatebox{90}{$=$}',r'\rotatebox{90}{$\unsure{\simeq|=}$}&\quad\rotatebox{90}{$=$}')
needle='  % Isolated point to the right of the divider; possible surface trace.'
text=text.replace(needle,r'''  % Tiny detached point beneath the lower rule endpoint; possible surface trace.
  \node[inner sep=0pt] at (6.98,.015) {\unsure{\begin{tikzpicture}[baseline=0pt]
    \fill (0,0) ellipse[x radius=.009cm,y radius=.011cm];
  \end{tikzpicture}}};
'''+needle)
text=text.replace(r'  \operatorname{Gl}(2,\mathbb{F}_2)/\mathbb{F}_2^{*}',r'''  \begin{tikzpicture}[baseline=(qq.base)]
    \node[inner sep=0pt] (qq) at (0,0) {$\operatorname{Gl}(2,\mathbb{F}_2)/\mathbb{F}_2^{*}$};
    % Detached point below the quotient's left portion; possible surface trace.
    \node[inner sep=0pt] at (-1.25,-.58) {\unsure{\begin{tikzpicture}[baseline=0pt]
      \fill (0,0) ellipse[x radius=.010cm,y radius=.013cm];
    \end{tikzpicture}}};
  \end{tikzpicture}''')
(root/'decisions/scan013_final.tex').write_text(text)

inventory=copy.deepcopy(rep['R2']['inventory'])
for x in inventory:
    if x.get('element') in ['Detached upper trace','Detached divider point','Detached box pair']:
        x['hand']='unnamed hand'
    if x.get('element')=='Cardinal-2 identity':x['first_words_or_objects']='Aff(1,F2) simeq Aff(Z2) simeq decorative S index 2'
    if x.get('element')=='Underlined affine phrase':x['first_words_or_objects']='espace affine and sous/sur, cancellation state uncertain; underline'
    if x.get('element')=='Canceled preposition':
        x['element']='Preposition with doubtful cancellation'
        x['first_words_or_objects']='deleted sous / deleted sur / live sous / live sur'
    if x.get('element')=='Affine group decomposition':x['first_words_or_objects']='vertical simeq; F3 plus . F3 star; lower simeq/equals and equals; Z3 Z2'
inventory.insert(9,dict(sheet_kind='text',hand='unnamed hand',element='tiny point below divider endpoint',kind='drawing',position='[1002,796,1015,809]',first_words_or_objects='Small point, writing versus surface uncertain',transcribed='yes'))
ii=next(i for i,x in enumerate(inventory) if x['element']=='Last alternating-group identity')
inventory.insert(ii,dict(sheet_kind='text',hand='unnamed hand',element='point below lower quotient',kind='drawing',position='[1276,2081,1283,2088]',first_words_or_objects='Small detached point, writing versus surface uncertain',transcribed='yes'))

events=copy.deepcopy(json.loads((root/'pending_events/scan013.json').read_text()))
for r,d in rep.items():
    for i,c in enumerate(d['checks'],1):
        events.append(dict(statement_id=f'R013-{r}-{i:02d}',date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan013 {r} independent reader',type='targeted proof check',outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']))

unresolved=[
 ('Left vertical-arrow label','2','vertical wriggle','medium'),
 ('Verb ending in the first sentence','splitte','splitt.','medium'),
 ('Canceled word in the remark','une','interior obscured by crossing','medium'),
 ('Torsor noun','torseur','torseurs','medium'),
 ('Torsor preposition','sur','sous','medium'),
 ('Word after espace affine','deleted sous','deleted sur; live sous; live sur','low'),
 ('First overwritten letter','double-stroked Z','plain Z','low'),
 ('Canceled word after second ou encore','one illegible word','no defensible lexical candidate','low'),
 ('First decorative S','Fraktur S','calligraphic S; later S3 uses the primary form','medium'),
 ('First rounded A','calligraphic A','plain cursive A; later A3 uses the primary form','medium'),
 ('Lower-left vertical comparison','rotated simeq','rotated equals','low'),
 ('Upper Z-to-G connector','headless shaft','right arrow','low'),
 ('Lower first connector','headless shaft','right arrow','low'),
 ('Two-lobed upper trace','drawn trace','writing versus surface matter','low'),
 ('Tiny point under divider end','drawn point','writing versus surface matter','low'),
 ('Remote divider point','drawn point','writing versus surface matter','low'),
 ('Pair right of box','drawn oblique pair','writing versus surface matter','low'),
 ('Point below quotient','drawn point','writing versus surface matter','low')]
notes=r'''The handwritten page continues the extension discussion, then begins 4) Ens. de petit cardinal, with a) Cardinal 2 and b) Cardinal 3. No date or manuscript page number appears. Archive foliation 12 is retained only as a comment and assigned to unnamed hand. No explicit author doubt word or question mark was identified. The heading, abbreviations, two un words, paragraphing, cancellations, raised Rmq with its lead, two divider strokes, open frame and displaced A2/A3 formulas are preserved. There is one physically unreadable canceled word, following the second ou encore. The decorative S and rounded A ambiguities are marked at their first occurrences only. Local overwrite alphabets are assessed separately. Small detached marks are drawn with writing-versus-surface doubt and no imposed mathematical role. S contains no row for this scan.

All 13 original C doubts were inspected after the three complete independent returns were compared: Rmq, the boxed subscript 2, and the last canceled doubled Z were resolved; ten doubts, including the unreadable word, remain. New doubts concern the torsor noun, two arrow ends and five detached trace loci. Both C and H already have the stop after Z.Aut(Z); the correction there concerns separate left-starting placement only. H's declared bold/double-stroke alphabet encoding, emphasis macro choices, confidence-only agreement for the S index and alphabet, and archive page marker are excluded from error counts. H's prose note about the two lower relations is not a drawn transcription of those strokes.

Actual mathematical checks, separate from reading, establish the pullback and split-extension claims under their required interpretation. For a commutative morphism of short exact extensions with an isomorphism on kernels, the natural map to the fibre product is injective by exactness and surjective by correcting a chosen lift with a kernel element. A section of the upper extension then pulls back. The unrestricted implication is false: the top split extension 0→Z→Z×C2→C2→0 receives the bottom nonsplit extension 0→Z --×2→ Z→C2→0 through n↦(n,n mod 2), with kernel map ×2 and quotient identity. The bottom cannot split because a homomorphism C2→Z is zero. This conditional issue is logged as M013-ARBITRARY, refuted with refined statement M013-SPLIT-PB; it does not choose between 2 and a wriggle in the ink. A chosen splitting also identifies an extension with Z⋊_alpha Gamma, which is the pullback of Z⋊Aut(Z) along its action homomorphism. The baseline product point is not rewritten as a semidirect-product sign in the transcription.

For a two-element set, the unique swap defines its C2 torsor structure. Every one-dimensional F2 vector space has a unique nonzero vector, giving a unique linear isomorphism between two such spaces. The two F2 affine maps give S2, and A2 is trivial. In degree three, the six distinct affine maps of F3 act faithfully, as do the six invertible 2-by-2 matrices on the three nonzero F2 vectors. Under the conditional interpretation GP(1,F2)=PGL2(F2), the scalar quotient is trivial and its projective line has three points. The additive F3 group is C3, its multiplicative group is C2, and inversion supplies the semidirect action; translations are precisely A3. The finite certificate enumerates these actions, checks all 36 products in each six-element group, and checks the parity assertion. These calculations are logged individually and did not determine uncertain glyphs.'''
dec=dict(base='R2',text_file='decisions/scan013_final.tex',findings=fs,inventory=inventory,notes=notes,events=events,unresolved=[dict(place=p,reading=x,alternatives=a,confidence=c) for p,x,a,c in unresolved],abbreviations=copy.deepcopy(rep['R2']['abbreviations']),main_crop_count=9,main_crop_views=obs['views'])
(root/'decisions/scan013.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')

coverage=json.loads((root/'decisions/scan013_C_doubt_coverage.json').read_text())
for i,d in enumerate(coverage['doubts'],1):
    d['c_doubt_id']=f'C{i:02d}';f=by[d['c_doubt_id']]
    d.update(disposition=f['doubt_action'],findings=[f'S013-{fs.index(f)+1:03d}'],final=f['final'],crop=f['crop'])
assert sum(d['disposition']=='resolve' for d in coverage['doubts'])==3
(root/'decisions/scan013_C_doubt_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
p=root/'decisions/scan013_witness_comparison_pending.json';d=json.loads(p.read_text());d['status']='Complete; original comparison questions retained for audit.';d['main_status']='All three final returns fully read and compared before image review. All disagreements, all 13 C doubts and all witness differences inspected. No pending loci.';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(root/'decisions/scan013_review_state.json').write_text(json.dumps(dict(scan=13,status='Adjudication complete, ready for validation and commit',all_three_final_returns_fully_read_and_compared=True,main_crops_created=9,main_views=len(obs['views']),C_resolved=3,C_retained=10),indent=2)+'\n')
manifest_path=root/'crops/scan013/manifest.json';manifest=json.loads(manifest_path.read_text())
if not any(x['path']==mm(9) for x in manifest):manifest.append(dict(path=mm(9),bbox=[1248,2055,1307,2112],reason='New detached point exposed in the missing lower layout crop; no reader crop covers this locus',main_review_after_all_three_returns=True))
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(dict(findings=len(fs),inventory=len(inventory),events=len(events),doubts=len(unresolved),views=len(obs['views'])))
