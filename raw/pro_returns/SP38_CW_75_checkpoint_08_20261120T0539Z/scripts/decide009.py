from pathlib import Path
import json,copy,hashlib
root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan009'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan009_main_observations.json').read_text())
def get(r,n):
    key=f'R1-{n:03d}' if r=='R1' else f'R3-009-{n:03d}' if r=='R3' else n
    return next(f for f in rep[r]['findings'] if f['id']==key)
def rp(r,s):return f'readings/scan009/{r}/{s}.png'
def mp(s):return f'crops/scan009/{s}.png'
paths={
'family':rp('R1','14_detached_classification_mark'),'transitivity':rp('R3','02_transitivity'),'cor_glyph':rp('R3','03_cor_glyph'),
'table_classes':rp('R2','03_table_first_row'),'a_glyph':rp('R3','04_a_glyph'),'a4':rp('R3','05_a4_cancel'),
'chain':rp('R3','06_first_chain'),'identity':rp('R3','07_split_identity'),'hom':rp('R3','14_hom_word'),
'inclusion':rp('R1','07_second_inclusion'),'second_note':rp('R3','08_second_note'),'group_word':rp('R3','09_group_word'),
'aut':rp('R3','10_aut_subscript'),'left':rp('R3','11_left_note'),'right':rp('R3','12_right_note'),'laws':rp('R3','13_laws'),
'cor_layout':mp('01_cor_layout'),'rectification':mp('02_rectification'),'heading':mp('03_heading_gpes'),'donner':mp('04_donner_placement'),'product':mp('05_product_Z')}
keys=['family','transitivity','cor_glyph','a_glyph','a4','a4','a4','a4','chain','chain','identity','identity','second_note','second_note','group_word','aut','left','left','left','left','left','laws','right','transitivity','cor_glyph','cor_layout','cor_layout','cor_layout','table_classes','a4','rectification','rectification','rectification','heading','donner','chain','hom','inclusion','second_note','product','laws','laws','left','left','right','right','right','right']
r1=list(range(1,24))+[24,25,26,None,None,None,27,28,29,30,31,32,33,34,35,13,36,37,None,38,39,42,43,44,41]
r3=[1,2,4,8,9,10,11,12,19,20,22,24,28,29,30,31,33,34,35,36,38,43,45,3,5,6,7,7,None,13,14,16,15,17,18,21,25,27,28,32,41,42,37,39,44,46,47,49]
fs=copy.deepcopy(rep['R2']['findings'])
assert len(fs)==len(keys)==len(r1)==len(r3)==48
fallback={26:'Left rule includes the opening Cor line.',27:'Centered sum on its own line.',28:'classes',41:r'(z)\cdot z\prime'}
for i,f in enumerate(fs):
    f['readers']={'R1':get('R1',r1[i])['final'] if r1[i] else fallback[i], 'R2':f['final'],'R3':get('R3',r3[i])['final'] if r3[i] else 'classes'}
    f['crop']=paths[keys[i]];f['evidence']=obs['observations'][keys[i]]
    f['decision']='Main inspected this crop and adopts the stated reading from its ink; all three independent readings are recorded.'
by={f['id']:f for f in fs}
def upd(id,**kw):by['R2-'+id].update(kw)
upd('D02',final=r'\Leftrightarrow',confidence='high',diff_c=True,doubt_action='resolve',s_decision='CONFIRMED: equivalence arrow and au plus are both visible. The mathematical criticism is separately checked in M009-T and M009-T1.',decision='R1/R2 resolve the equivalence sign; R3 retains a left-arrow alternative. Main sees a right return/head and resolves with R1/R2.',consequential=True)
upd('D07',final=r'\sigma_{\unsure{34|24}}',diff_c=False,doubt_action='retain',confidence='low',decision='Retain C with R1/R3; the first digit remains crossed. Reject R2 resolution.')
upd('D08',final=r'\sigma_{\unsure{1234|4234}}',diff_c=False,doubt_action='retain',confidence='low',decision='Retain C with R1/R3; the first low upright meets cancellation. Reject R2 resolution.')
upd('D09',decision='Resolve double-stroking with R1/R2; the extra inner stroke is visible despite thick retracing.',confidence='high',diff_c=True,doubt_action='resolve')
upd('D10',final='1q',confidence='high',diff_c=True,doubt_action='resolve',decision='Resolve the additional q with R1/R3; its bowl and tail are distinct from 1.',consequential=True)
upd('D11',final=r'\unsure{p|q}qp=\operatorname{id}_{\Gamma}',h=r'pq=\mathrm{id}_{\Gamma}',consequential=True,math_note='Keep the extra first character and the clear qp order. A usual-composition type check identifies the mismatch but cannot repair the flanking overwritings.')
by['R2-D11']['readers']['R3']=get('R3',22)['final']+'; '+get('R3',23)['final']
upd('D12',decision='R1 resolves q; R2/R3 retain q|p. Main keeps the doubt because the filled bowl and retracing obscure the stem.')
upd('D15',final=r'\unsure{grs|gpes}',diff_c=True,doubt_action='retain',confidence='medium',decision='Choose R1 primary grs, retaining gpes; R2 resolves gpes and R3 keeps gpes first. The short middle shoulder favors r without settling the abbreviation.')
upd('D17',final=r'\unsure{Parler}',diff_c=True,doubt_action='retain',confidence='medium',decision='Choose R3: initial size excludes lowercase parler, but the first word remains partly compressed. Narrow the alternatives without declaring complete resolution.')
upd('D19',final='inverseur',diff_c=True,doubt_action='resolve',confidence='medium',decision='Choose R3: the final r exit is followed by a space, with no independent s.')
upd('D20',final=r'\unsure{car|où}',diff_c=False,doubt_action='retain',confidence='low',decision='Retain C with R1/R3. The short compressed marks do not justify R2 resolution of car.')
upd('D21',final=r'\deleted{\unsure{Aut(Z)|AutZ|Aut}}',diff_c=True,doubt_action='retain',confidence='low',decision='Prefer R2/R3 Aut(Z), retain R1 AutZ and C Aut. Crossing and edge interference leave all three candidates open.')
upd('D23',consequential=True,math_note='The crossed base favors R, with Gamma retained. H supplies a separate live Gamma that is not securely present; the expected quotient is not supplied.')
upd('H04',c='Left rule encloses the entire Cor paragraph.',final='Left rule beside the continuation beginning aux partitions and the final sum; opening Cor line outside it.',diff_c=True,decision='All three readers put the opening line inside the rule. Main crop shows the rule beginning below it and restores that extent.')
by['R2-H04']['readers']={r:'Left rule encloses the opening Cor line and continuation.' for r in rep}
upd('H05',decision='Choose R2/R3 left-aligned sum on its own line; R1 and C center it and H puts it inline.')
upd('N01',decision='Keep R2 new doubt classes|classe. R1/R3 read classes without qualification; the final exit stroke does not settle a separate s.')
upd('H07',consequential=True,math_note='The written reason is car on ne veut pas de polygone à 1 coté. H substitutes different wording; the crop supports the fixed-point exclusion as written.')
upd('H11',c='donner, before a separate displayed chain',h='donnée, before a separate displayed chain',final='donner alongside the first 1 and chain',diff_c=True,decision='Choose R3 adjacent placement; the final r and absent acute agree with C/R1/R2 wording.')
upd('H13',final='un hom. de ...',decision='All three read hom., not homom.; the separate following group-word doubt is recorded in its own row.')
upd('H15',consequential=True,math_note='The live target Gamma over a canceled iso/is is retained; H lacks that target and its overwrite state.')
upd('H18',final=r"ici d'un ... d'extensions ... cela permet d'introduire $\operatorname{Aff}(Z)\simeq Z.\operatorname{Aut}Z$",diff_c=True,consequential=True,math_note='The note has Aff(Z) and a semidirect-product-like expression, not H squared of Gamma,Z. The low point is retained; the preceding compressed words remain separately qualified.')
upd('N03',final='Left margin selected; slanted note reproduced in a rotated TikZ node beneath its descending divider.',decision='Use R1 geometrical slant and explicit left margin, with R2/R3 low product point. A comment about slant alone does not reproduce it.')
by['R2-N03']['readers']['R1']=get('R1',39)['final']+'; '+get('R1',40)['final']+'; rotated text node'
by['R2-N03']['readers']['R3']=get('R3',39)['final']+'; '+get('R3',40)['final']+'; unrotated text'
upd('H21',final=r"G'\simeq\mathbb{Z}.\Gamma'",diff_c=True,decision='Use doubled Z and the low product point with R2/R3. R1 centers the dot; H uses plain Z.')
by['R2-H21']['readers']['R3']=get('R3',47)['final']+'; '+get('R3',48)['final']
for r,n,key,others in [('R1',45,'right',{'R2':'Ss-groupes','R3':'Ss-groupes'}),('R1',46,'family',{'R2':'no detached mark','R3':'no detached mark'}),('R3',26,'hom',{'R1':'groupes','R2':'groupes'})]:
    f=copy.deepcopy(get(r,n));f['readers']={**others,r:f['final']};f['crop']=paths[key];f['evidence']=obs['observations'][key]
    f['decision']='Main retains this additional reader finding after crop inspection; it is a new doubt, not a prior C doubt.'
    fs.append(f)
text=(root/'readings/scan009/R2/reading.tex').read_text()
old='=\\text{famille de cardinaux}\\quad (a_{i})_{i\\in\\mathbb{N}}'
new=(root/'readings/scan009/R1/reading.tex').read_text().split('\\[',1)[1].split('\\]',1)[0].strip()
assert old in text;text=text.replace(old,new)
text=text.replace('\\noindent\\begin{tabular}{@{}|@{\\hspace{.6em}}p{\\dimexpr\\linewidth-1em\\relax}@{}}\n','',1)
text=text.replace('correspondent $1$-$1$ aux','correspondent $1$-$1$\\par\n\\noindent\\begin{tabular}{@{}|@{\\hspace{.6em}}p{\\dimexpr\\linewidth-1em\\relax}@{}}\naux',1)
text=text.replace(r'\sigma_{\unsure{12|13}}\sigma_{34},\sigma_{1234}',r'\sigma_{\unsure{12|13}}\sigma_{\unsure{34|24}},\sigma_{\unsure{1234|4234}}')
text=text.replace('donner\n\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,column sep=small]\n1','\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,column sep=small]\n\\text{donner}\\&[-1ex]1',1)
text=text.replace(r'1\unsure{q}',r'1q',1).replace('hom. de groupes',r'hom. de \unsure{gpes|groupes}',1)
text=text.replace('ou à donner gpes',r'ou à donner \unsure{grs|gpes}',1)
r1text=(root/'readings/scan009/R1/reading.tex').read_text()
left=r1text[r1text.index('\\reversemarginpar'):r1text.index('\\normalmarginpar')+len('\\normalmarginpar')]
left=left.replace('rotate=-27','rotate=-31').replace('Parler ici',r'\unsure{Parler} ici').replace(r'\unsure{inverseur|inverseurs}','inverseur').replace(r'Z\cdot\operatorname{Aut}Z',r'Z.\operatorname{Aut}Z').replace(r'AutZ|Aut(Z)|Aut',r'Aut(Z)|AutZ|Aut')
a=text.index('\\reversemarginpar');b=text.index('\\normalmarginpar')+len('\\normalmarginpar');text=text[:a]+left+text[b:]
a=text.index('% right margin note');right=r1text[r1text.index('% Lower-right note'):]
right=right.replace(r'\mathbb{Z}\cdot\Gamma',r'\mathbb{Z}.\Gamma').replace('at (0.6,-0.2)','at (1.8,-0.2)')
text=text[:a]+right
(root/'decisions/scan009_final.tex').write_text(text)
inv=copy.deepcopy(rep['R3']['inventory'])
inv.insert(2,dict(sheet_kind='text',hand='his hand',element='classification family display',kind='display',position='upper continuation y205–285',first_words_or_objects='= famille de cardinaux (a_i) indexed by N',transcribed='yes'))
inv.insert(3,copy.deepcopy(rep['R1']['inventory'][2]))
for x in inv:
    if x['element']=='corollary vertical rule':x['first_words_or_objects']='rule beside continuation and sum, below opening Cor line'
    if x['element']=='third description of group data':x['first_words_or_objects']='ou à donner grs/gpes Z,Gamma avec op. ...'
    if x['element']=='left marginal note':x['first_words_or_objects']='Parler? ici d’un gr inverseur d’extensions car/où ... Aff(Z)';x['position']+='; slant reproduced'
    if x['element']=='left note last canceled word':x['first_words_or_objects']='Aut(Z)/AutZ/Aut'
    if x['element']=='right marginal note':x['first_words_or_objects']='Ss-groupes/Ss-gpes ... ss-gpe ... et on a ...'
events=json.loads((root/'pending_events/scan009.json').read_text())
for e in events:
    e['who']=e['who'].replace(' preliminary check','')
    e['outcome']=e['outcome'].replace('the written arrow and wording await independent visual adjudication.','the main crop confirms the written equivalence arrow and au plus.').replace('its occurrence in canceled writing still awaits the ink decision.','the primary canceled reading is 1234, with 4234 retained because cancellation obscures the initial digit.').replace('conditional on its letters and deletion state.','The ink keeps the canceled base unresolved; no missing live quotient is supplied.')
    if e['statement_id']=='M009-R':e['outcome']+=' This uses a directed-edge orientation, with the same qualification about the automorphism-based definition as M007-ZNF.'
ids={'R1':['M009-T','M009-TABLE','M009-ALT','M009-PQ','M009-LAW'],'R2':['M009-F','M009-T','M009-TABLE','M009-PQ','M009-LAW'],'R3':['M009-T','M009-TABLE','M009-PQ','M009-LAW','M009-SG']}
for r in rep:
    for sid,c in zip(ids[r],rep[r]['checks']):
        evtype='refuted' if sid=='M009-T' else 'targeted proof check'
        events.append(dict(statement_id=sid,date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan009 {r}',type=evtype,outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']+(' Refined statement: M009-T1.' if evtype=='refuted' else '')))
unresolved=[('Decorative S',r'\mathfrak S',r'\mathscr S','medium'),('Decorative A',r'\mathfrak A',r'\mathscr A','medium'),('S2 row ending','classes','classe','medium'),('Canceled A4 first item','1','i','low'),('Canceled A4 first index','12','13','low'),('Canceled A4 second index','34','24','low'),('Canceled A4 final index','1234','4234','low'),('Identity left flank','p','q','low'),('Identity right flank','q','p','low'),('Word under target Gamma','iso','is','low'),('Restriction final word','iso','is','medium'),('After hom. de','gpes','groupes','medium'),('After ou à donner','grs','gpes','medium'),('Left note first word','Parler','word contours partly compressed; no secure alternative','medium'),('Left note connective','car','où','low'),('Left note canceled word','Aut(Z)','AutZ; Aut','low'),('Live-law rounded variable',r"z'",r"{\mathcal Z}'",'medium'),('Right note first word','Ss-groupes','Ss-gpes','medium'),('Right note canceled base','R',r'\Gamma','low'),('Detached classification trace','V-like mark','surface trace; attribution to writing unresolved','low')]
notes="""The page has three numbered topics: “Ens. avec permutation”, “Rectification”, and “Produit 1/2 direct de gpes”. It classifies permutation sets as Z-sets, gives a finiteness condition, describes permutation conjugacy classes by partitions, excludes fixed points from oriented contours, and gives split-extension, complement, action and multiplication descriptions of semidirect products. The lower margins concern Aff(Z) and subgroups containing the kernel. No date is written. Archive foliation 8 remains comment-only.

The author's question mark after S5 is preserved. The A4 representatives, an overwritten iso/is, the first multiplication law, the left note’s last word and the right note’s base are canceled as written. The A4 label is live. The faint detached V-like trace has uncertain status as writing. The notation changes from a_i to n_i, and the extra q beside the first chain’s terminal 1 remains. The clear qp core and uncertain flanking p/q characters are not repaired. The corollary rule starts beside its continuation; its sum is left aligned. Donner shares the first chain’s baseline. Both marginal dividers, the short companion stroke and the left note’s slant are reproduced. All 23 C doubts have explicit dispositions; new doubts are distinguished from them.

SA01-K75-01 is confirmed on the ink: the outer sign is equivalence and the ending includes au plus. The stated condition is insufficient: u=(12)(34) has n₂=2 and all other counts zero, yet has two orbits. Under the nonempty one-orbit convention the refinement is Σn_i=1. The counterexample and all other actual checks are recorded in CHECK_EVENTS.tsv; none changes the text. Integer powers give the permutation/Z-action correspondence, and orbit stabilizers iZ give the classification and finiteness test. Cycle decomposition gives the conjugacy/partition correspondence, interpreting the written entiers as nonnegative counts. Exact enumeration confirms the live counts 2,3,5 for S2,S3,S4 and 1,3 for A2,A3. The primary canceled 4-cycle would be odd; this does not decide its obscured digit or explain the cancellation. The written S5 question is not completed.

The fixed-point-free construction yields a degree-two directed-edge-oriented graph, retaining distinct parallel edges for a 2-cycle; this uses the orientation qualification already recorded on scan007. The usual section identity is pq=id_Γ, while the written central qp has the wrong type under ordinary composition. The overwrite marks remain unresolved. A section gives a complement and a conjugation action; the live multiplication is associative under that action. The canceled law is compatible with the alternative coordinates q(γ)z, so its cancellation does not make it mathematically false. The affine-group formula is checked conditionally under the usual meaning of affine transformations, and inverse images under the quotient give the subgroup correspondence. No external material was used."""
dec=dict(base='R2',text_file='decisions/scan009_final.tex',findings=fs,inventory=inv,notes=notes,events=events,unresolved=[dict(place=p,reading=x,alternatives=a,confidence=c) for p,x,a,c in unresolved],abbreviations=rep['R1']['abbreviations'],main_crop_count=5,main_crop_views=obs['main_crop_views'])
(root/'decisions/scan009.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root/'readings/scan009').glob('R*/*')) if p.name in ('reading.tex','report.json')}
(root/'decisions/scan009_reader_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print({'findings':len(fs),'inventory':len(inv),'events':len(events),'doubts':len(unresolved),'views':len(obs['main_crop_views'])})
