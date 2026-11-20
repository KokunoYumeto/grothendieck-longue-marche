from pathlib import Path
import json,copy,hashlib

root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan011'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan011_main_observations.json').read_text())
ob={x['place']:x for x in obs['observations']}
def get(r,k):return next(f for f in rep[r]['findings'] if f['id']==k)
def rp(r,k):return f'readings/scan011/{r}/{k}.png'
def mp(k):return f'crops/scan011/{k}.png'
paths={
 'heading':rp('R2','01_heading'),'cancel':rp('R3','L02_cancelled_opening'),
 'split':rp('R3','L03_splitting'),'verb':rp('R2','03_verb'),
 'brace':rp('R3','L05_verification'),'gamma':rp('R2','05_cancelled_gamma'),
 'sub':rp('R3','L07_proof_subscript'),'itou':rp('R3','L08_itou'),
 'nb':rp('R3','L09_nb'),'relation':rp('R3','L10_cancelled_gamma_subset'),
 'dihedral':rp('R3','L11_dihedral'),'insertion':rp('R3','L12_final_insertion'),
 'point':rp('R2','11_detached_point'),'points':rp('R2','13_right_detached'),
 'upper':mp('01_upper_sequence'),'cases':mp('02_defining_cases'),
 'arrow':mp('03_gamma_arrow'),'or':mp('04_or'),'indent':mp('05_proof_left_starts'),
 'example':mp('06_example_block'),'lower':mp('07_lower_affine'),
 'half':mp('08_half_fraction'),'bottom':mp('09_bottom_sequence')}
r1=[*['C%02d'%i for i in range(1,15)],'F01',None,'F02',None,'F04','F05','F06','F07','C02','F08','C02','F09','F11','F10','F12','F13',None,'F03',None]
r3=['C01','C02','C03-C05','C03-C05','C03-C05','C06','C07','C08','C09','C10','C11','C12','C13','C14',None,'C02','F01',None,'F02','F03','F04','F05','C02','F06','C02','F13','F07','F10','F08','F09',None,'F11',None]
keys=['heading','heading','cancel','cancel','cancel','split','verb','brace','gamma','sub','nb','relation','dihedral','insertion','heading','upper','upper','cases','arrow','brace','or','itou','itou','itou','example','example','dihedral','point','insertion','bottom','half','split','points']
oks=['heading','heading','canceled opening','canceled opening','canceled opening','splitting sentence','verb','verification brace and circle','canceled gamma','proof subscript','NB','canceled relation','dihedral note','final correction','heading','upper sequence','upper sequence','defining cases','gamma arrow','verification brace and circle','or','Itou note','Itou note','Itou note','example block','example block','dihedral note','affine comparison','final correction','bottom sequence','half fraction','splitting sentence','upper right points']
fallback={('R1',16):'Repeated doubled Z in reading.tex; first occurrence retains doubled/plain doubt.',('R1',18):'The two defining equalities are aligned in reading.tex.',('R1',31):'Baseline 1/2 in reading.tex.',('R1',33):'No upper-right points in reading.tex or report.',('R3',15):'Clear à in reading.tex.',('R3',18):'The two defining equalities are aligned in reading.tex.',('R3',31):'Baseline 1/2 in reading.tex.',('R3',33):'No upper-right points in reading.tex or report.'}
fs=copy.deepcopy(rep['R2']['findings']);assert len(fs)==33
for i,f in enumerate(fs):
 f['readers']={'R1':get('R1',r1[i])['final'] if r1[i] else fallback.get(('R1',i+1),'See independent reading.tex.'),'R2':f['final'],'R3':get('R3',r3[i])['final'] if r3[i] else fallback.get(('R3',i+1),'See independent reading.tex.')}
 f['crop']=paths[keys[i]];f['evidence']=ob[oks[i]]['evidence']
 f['decision']='Main compared all three full returns and inspected this crop; the final reading follows the stated ink evidence.'
by={i+1:f for i,f in enumerate(fs)}
def upd(n,**kw):by[n].update(kw)
upd(1,final=r'\unsure{grp|grpe}',decision='Choose R2 primary grp, retaining grpe from C/R1/R3 because the last exit may contain a compressed e.',confidence='medium')
upd(2,final=r'\unsure{\mathbb{Z}|Z}',doubt_action='retain',confidence='medium',decision='Follow R1 in retaining doubled/plain Z uncertainty; narrow C by excluding both G forms. R2/R3 resolve doubled Z. Later local repetitions use the primary doubled form without repeated marks.')
upd(3,diff_c=False,diff_h=False,marked_in_H=False,decision='Retain C outer structural doubt. The nested D/T change is counted only in C05; H lower labels and argument differences are itemized separately, avoiding duplicate counts for the whole expression.')
upd(4,marked_in_H=False,doubt_action='retain',decision='Retain var|op: crossing and compressed lower strokes do not resolve the second label. H describes added words but does not transcribe them.')
upd(5,marked_in_H=False,doubt_action='retain',decision='All readers favor D|T over C T|D; keep both because the strike can supply part of the bowl.',confidence='low')
upd(6,final='un splitting $q_t$, défini par',doubt_action='resolve',confidence='high',decision='Resolve splitting with R1/R2; R3 retains it. The visible descenders and tall middle run support the word, and un/défini lack H’s final e.')
upd(8,final=r'\operatorname{int}(i(g))\unsure{\circ}(q_t(\gamma))',diff_c=False,doubt_action='retain',confidence='low',decision='Retain C/R1/R3 separate-circle doubt; R2 resolves the loop, but it still touches the opening-parenthesis return.')
upd(9,doubt_action='resolve',decision='Resolve gamma with R2/R3; R1 retains uncertainty. Its descending loop and upper limbs remain visible through the retracing.',confidence='high')
upd(10,consequential=True,math_note='The ink favors b|t at the second q-subscript. A general q_b need not fix t; the conditional counterexample and the q_t refinement are recorded separately in M011-INDEX and M011-CHANGE.',doubt_action='retain')
upd(11,doubt_action='retain',diff_h=False,decision='All three retain si uncertainty; H has the same primary reading, so this confidence-only difference is excluded from H collation.')
upd(12,final=r'\deleted{\unsure{\Gamma\in|\Gamma\subset}}',doubt_action='retain',confidence='low',decision='Favor membership with R2/R3, but retain subset as R1/C allow because the cancellation may create the middle stroke; do not adopt R2’s full resolution.')
upd(13,final="diédral d'indice",doubt_action='resolve',marked_in_H=True,decision='Resolve diédral with R2/R3; R1 retains diédhral. No extra h ascender is present. H’s d’indice doubt has the same primary wording and is not counted.')
upd(14,doubt_action='retain',final=r"\deleted{\unsure{d'ordre $n$}.}",decision='Retain R1/R2 uncertainty beneath the strike; R3 resolves the phrase. Preserve the canceled period missing from H.',confidence='medium')
upd(24,marked_in_H=False)
upd(27,final=r'\mathbb{D}_n',decision='Resolve doubled D with R1/R2 over R3 doubled/plain doubt: two separated upright strokes are visible. H’s bold encoding is treated as the same doubled/heavy glyph.',confidence='high')
upd(28,final='Detached short upright with a rightward foot, drawn without assigned meaning.',decision='Follow R1/R3 on the dark angular stroke; R2 doubts whether it is writing. Reproduce the secure physical shape without giving it mathematical or punctuation meaning.',confidence='high')
upd(29,diff_c=True,final="Raised inserted inverses l'un de l' above the canceled phrase, with autre continuing on the baseline.",decision='Use R1’s actual stacked placement. R2 raises the insertion after the deletion and R3 applies insertion markup without raised geometry; those code choices do not match their own placement observations.')
upd(31,diff_h=False,decision='Choose R2’s raised numerator/lowered denominator over the baseline 1/2 in C/R1/R3. H’s ½ is equivalent geometry, so no H macro-only change is counted.')
def add(place,c,h,final,evkey,cropkey,readers,kind='insertion or placement',dc=True,dh=True,confidence='high',decision='',marked=False):
 f=dict(id='added',place=place,c=c,h=h,final=final,evidence=ob[evkey]['evidence'],crop=paths[cropkey],readers=readers,kind=kind,diff_c=dc,diff_h=dh,confidence=confidence,marked_in_H=marked,decision=decision or 'Main compared all returns and chose the geometry visible in the named crop.',doubt_action='',s_id='',math_note='')
 fs.append(f);return f
add('First lower label of canceled Aut',r'G\text{-ens}','Two added words described, not transcribed',r'G\text{-ens}','canceled opening','cancel',{r:r'G\text{-ens}' for r in rep},kind='omission',dc=False)
add('Upper curved-return label side','q_t on default lower side of bowed return','q_t on default lower side of bowed return','q_t above the bowed return, inside its arc','upper sequence','upper',{'R1':'Swapped label side, above the arc.','R2':'Default label side in reading.tex.','R3':'Default label side in reading.tex.'})
add('Left starts of four verification rows','All four rows left-aligned','Separate canceled rows and centered live equations','Successive rows indented slightly farther right','proof indentation','indent',{'R1':'All rows left-aligned.','R2':'Small, one-quad, then two-quad offsets.','R3':'All rows left-aligned.'})
add('Second affine formula horizontal placement','Same left edge as upper formula','Same left edge as upper formula','Lower Aff formula slightly to the right','affine comparison','lower',{'R1':'30 source-coordinate-unit right offset.','R2':'Half-em right offset.','R3':'Small right offset.'})
add('Dihedral annotation placement','Right margin','Following body paragraph','Right-margin note beside lower Aff formula','dihedral note','dihedral',{r:'Right-margin note.' for r in rep},dc=False,marked=True)
add('Bottom return label and curve','q on default lower label side','q on default lower label side','q centered on the return curve; its stem intersects the shaft','bottom sequence','bottom',{r:'q with default tikz-cd label side in reading.tex.' for r in rep},decision='All readers preserve the q text but their default label placement separates it from the shaft. Main preserves the visible intersection using an unfilled centered label.')
fs.append(dict(id='attribution',place='Archive foliation hand attribution',c='Archive 10 represented only by a comment.',h='Editorial page marker 10; no writer attribution.',final='Archive 10 remains comment-only; inventory hand unnamed.',evidence=ob['archive hand attribution']['evidence'],crop='crops/scan011/10_foliation.png',readers={'R1':'unnamed hand','R2':'his hand','R3':'unnamed hand'},kind='other',diff_c=False,diff_h=False,confidence='low',marked_in_H=False,decision='Do not infer a person from the numeral or from its writing medium. This records an inventory-attribution disagreement, not a C/H transcription correction.',doubt_action='',s_id='',math_note=''))

text=(root/'readings/scan011/R2/reading.tex').read_text()
text=text.replace(r'\unsure{grp|grpe} $\mathbb{Z}$',r'\unsure{grp|grpe} $\unsure{\mathbb{Z}|Z}$')
text=text.replace(r'bend left=28,"q_t"]',r'bend left=28,"q_t"\prime]')
# The quote-swap character is a literal apostrophe in tikz-cd, not a prime command.
text=text.replace(r'"q_t"\prime]', '"q_t"\']')
text=text.replace(r'{$(i(g))\circ(q_t$}',r'{$(i(g))\unsure{\circ}(q_t$}')
text=text.replace(r'\deleted{\Gamma\in}',r'\deleted{\unsure{\Gamma\in|\Gamma\subset}}')
text=text.replace(r'\unsure{\tikz[baseline=-.1ex]{\draw[line width=.7pt,line cap=round] (0,.04)--(0,0)--(.025,0);}}',r'\tikz[baseline=-.1ex]{\draw[line width=.7pt,line cap=round] (0,.04)--(0,0)--(.025,0);}')
text=text.replace('% The two upper-right points and the lower-left hooked point have no assigned function; ink/surface status is unresolved.','% The upper-right points have uncertain writing status. The separate lower-left stroke is drawn without assigned function.')
old=r"\deleted{\unsure{d'ordre $n$}.}\raisebox{.7ex}{\inserted{inverses l'un de l'}}autre."
new=r"""\tikz[baseline=(old.base)]{
\node[anchor=base west,inner sep=0pt] (old) at (0,0) {\deleted{\unsure{d'ordre $n$}.}};
\node[anchor=south west,inner sep=0pt] at ([yshift=.14em]old.north west)
 {\inserted{inverses l'un de l'}};}autre."""
assert old in text;text=text.replace(old,new)
text=text.replace(r'bend left=25,"q"]',r'bend left=25,"q"{auto=false,inner sep=0pt}]')
(root/'decisions/scan011_final.tex').write_text(text)

inventory=copy.deepcopy(rep['R2']['inventory'])
for it in inventory:
 if 'Archive foliation' in it['element']:it['hand']='unnamed hand'
 if 'Canceled Gamma' in it['element']:it['first_words_or_objects']='Γ∈ / Γ⊂, canceled and uncertain'
for it in inventory:
 if 'hooked' in it['element'].lower() or 'hooked' in it['first_words_or_objects'].lower():it['first_words_or_objects']='Detached dark upright with rightward foot; no assigned meaning'
events=copy.deepcopy(json.loads((root/'pending_events/scan011.json').read_text()))
for e in events:
 e['who']=e['who'].replace('main preliminary check','main check')
 e['outcome']=e['outcome'].replace('whether the ink has t, b or an unresolved form awaits adjudication, and mathematics does not select the letter.', 'the crop favors b|t, and mathematics does not select the letter.')
 e['outcome']=e['outcome'].replace('; its written labeling still awaits ink adjudication','; the written label i is retained').replace(' The canceled first gamma remains an ink question for the readers and main adjudication.',' The canceled first gamma was independently resolved from the crop.').replace(' Ink choice is still pending; this does not select the glyph.',' The crop favors b|t; this check does not select the glyph.')
for r,d in rep.items():
 for i,c in enumerate(d['checks'],1):events.append(dict(statement_id=f'R011-{r}-{i:02d}',date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan011 {r} independent reader',type='targeted proof check',outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']))
unresolved=[
 ('Heading sign',':','à; two detached points, no secure a body','low'),
 ('Heading contraction','grp','grpe','medium'),
 ('Recurring upper group alphabet',r'\mathbb Z','Z; later local repetitions use the primary form','medium'),
 ('Canceled opening expression','Aut with two lower G labels and one D/T argument, mapping to Aut(G)','overall structure partly covered by crossing','low'),
 ('Canceled second lower label','var','op','low'),
 ('Canceled argument','D','T','low'),
 ('Detached trace above un','short horizontal dark trace','intentional writing versus incidental ink/surface trace','low'),
 ('Verb before t-prime','avait','aurait','medium'),
 ('Verification joining mark',r'\circ','curled return of the opening parenthesis, not a separate sign','low'),
 ('Second q-subscript in live proof','b','t','medium'),
 ('NB short word','si','compressed undivided strokes; no competing word secured','medium'),
 ('Canceled relation below Ex',r'\Gamma\in',r'\Gamma\subset','low'),
 ('Two raised points after direct)','two diagonally arranged points','intentional writing versus incidental ink/surface traces','low'),
 ('Canceled final phrase',"d'ordre n",'middle and final strokes partly obscured by strike','medium')]
notes="""This handwritten page studies a right torsor, the automorphism sequence, a splitting q_t indexed by a chosen point, and the relation between two such splittings. It gives a bracketed verification, a cyclic example, the affine and dihedral groups, and a final sequence for a cyclic torsor with inverse generators. There is no date or independent title. Archive foliation 10 is comment-only. The author asks “Quelle est la relation entre q_t et q_{t′} ?” and closes the verification with “ok”; NB singles out n=2. These are his words, distinct from editorial doubts. There is no S row.

All fourteen C doubts were examined on crops: splitting, the first canceled gamma, and diédral were resolved; eleven were retained, sometimes with narrowed or reordered candidates. The opening sign is colon-like, the group contraction favors grp, and the recurring upper Z remains doubled/plain; the final paragraph and sequence have plain Z. The canceled argument favors D|T. The live proof subscript favors b|t, with no substitution based on expected algebra. The small canceled Gamma relation favors membership but remains uncertain. The final canceled phrase retains its stop, and inverses l’un de l’ is placed above it. The left Itou enclosure, partial brace, slanted equality, staggered proof starts, bottom-aligned example, fraction placement and arrow-label sides are reproduced. Detached marks are retained without assigning mathematical functions. C’s rotated subset and H’s cup for the upward-open curve are equivalent geometry; H’s bold number-group and D encodings are not counted as macro-only differences.

The actual checks are recorded individually in CHECK_EVENTS.tsv. For affine pairs (gamma,f) on a right G-torsor, fixing t gives q_t(gamma)(th)=t gamma(h), the unique map over gamma fixing t; direct composition makes this a homomorphic section. The kernel is Aut_G(T). A chosen t identifies it with G by i_t(g)(th)=tgh, and then t′=tg gives q_{t′}=int(i_t(g))∘q_t. A bare right translation x↦xg is not generally this kernel map for nonabelian G; the qualification is about interpretation, not a correction of ink. The canceled computation q_t(gamma)(t′)=t gamma(g) is algebraically valid despite being canceled.

If the disputed subscript denotes an independent b, the equality q_b(gamma)t=t is false in general: on the additive integer torsor, q_a(−1)(x)=2a−x, so t=0 and b=1 give q_b(−1)(t)=2. This refutes only that conditional interpretation; the refined q_t statement is M011-CHANGE. No mathematical check selected b or t.

For Z/n, an endomorphism is determined by the image of 1, and invertibility is exactly the unit condition. The affine law is (b,a)(c,d)=(b+ac,ad). Translation and inversion give 2n distinct maps and the dihedral relations for n≥3. The n=2 NB is correct because the two signs coincide; n=1 would also collapse if allowed, while the final paragraph explicitly assumes n≥3. Inverse images of subgroups Gamma and preservation of the inverse-generator pair give the stated restricted split sequences under these definitions. Nothing beyond the supplied pages was researched."""
ab=copy.deepcopy(rep['R1']['abbreviations'])
ab.extend([dict(written='ens',expansion='ensembles'),dict(written='var / op',expansion='possibly variables / opérations; canceled label too uncertain for a definite expansion'),dict(written='Aff',expansion='transformations affines')])
dec=dict(base='R2',text_file='decisions/scan011_final.tex',findings=fs,inventory=inventory,notes=notes,events=events,unresolved=[dict(place=p,reading=x,alternatives=a,confidence=c) for p,x,a,c in unresolved],abbreviations=ab,main_crop_count=obs['main_crop_count'],main_crop_views=obs['main_crop_views'])
(root/'decisions/scan011.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
coverage=json.loads((root/'decisions/scan011_C_doubt_coverage.json').read_text())
for d,n in zip(coverage['doubts'],range(1,15)):
 d.update(disposition=by[n]['doubt_action'],findings=[f'S011-{n:03d}'],final=by[n]['final'],crop=by[n]['crop'])
assert all(d['disposition'] in ('retain','resolve') for d in coverage['doubts'])
(root/'decisions/scan011_C_doubt_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
pending=root/'decisions/scan011_witness_comparison_pending.json'
if pending.exists():
 d=json.loads(pending.read_text());d['status']='Completed main adjudication; original draft questions retained as an audit trail.';d['main_status']='All listed witness differences inspected and covered in scan011.json; all reader texts compared; no pending loci.';pending.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root/'readings/scan011').glob('R*/*')) if p.name in ('reading.tex','report.json')}
(root/'decisions/scan011_reader_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(dict(findings=len(fs),inventory=len(inventory),events=len(events),doubts=len(unresolved),views=len(obs['main_crop_views'])))
