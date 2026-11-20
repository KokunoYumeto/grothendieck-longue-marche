from pathlib import Path
import copy,json,hashlib

root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan012'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan012_main_observations.json').read_text())
ob={x['place']:x for x in obs['observations']}
def get(r,k):return next(f for f in rep[r]['findings'] if f['id']==k)
def vals(r,keys):return '; '.join(get(r,k)['final'] for k in keys.split('+'))

# Each R1 locus is mapped to the corresponding independently returned readings.
# Empty entries below have explicit text-based comparisons, never inferred agreement.
mapping={
 'F01':('F01','F01','opening'),
 'C01':('C01','C01','first Aut argument and upper traces'),
 'F02':('','','first Aut argument and upper traces'),
 'F25':('F02','','upper calculation layout'),
 'C02':('C02','C02','corollary overwritten form'),
 'F03':('F03','F02',"l'ens and canceled des"),
 'C03':('C03','C03',"l'ens and canceled des"),
 'C04':('C04','C04+F03','polygon abbreviation and omitted phrase'),
 'C05':('C05','C05','cotés and applic raised n'),
 'F04':('F04','F04','cotés and applic raised n'),
 'F05':('F05','F05','tt before sommet'),
 'C06':('C06','C06','autom'),
 'C07':('C07','C07','corollary final word'),
 'C08':('C08','C08','NB elle and ce'),
 'C09':('C09','C09','NB bijectif'),
 'C10':('C10','C10','NB canceled mais'),
 'C11':('C11','C11','NB canceled pour tt'),
 'F06':('F06','F06','NB fibres'),
 'F07':('F11','F08','headings'),
 'C12':('C12','C12','left note lettering'),
 'F08':('F07','M01','left note content and strokes'),
 'F09':('F08','M01','left note content and strokes'),
 'C13':('C13','C13+M02','left note content and strokes'),
 'C14':('C14','C14','left note lettering'),
 'F10':('F09','N03','left note lettering'),
 'C15':('C15','C15+M03','left note lettering'),
 'F11':('F10','F07','left note content and strokes'),
 'F12':('F12','F09','headings'),
 'C16':('C16','C16','square'),
 'F13':('F13','F10','square'),
 'F14':('F14','F10+F11','set block layout and equality'),
 'F15':('','N04','right detached pair'),
 'C17':('C17','C17','detached hook'),
 'F16':('F15','F12','Pb'),
 'F17':('F16','N05','lower group paragraph'),
 'F18':('F17','F13+N06','lower group paragraph'),
 'F19':('F18','N07','lower group paragraph'),
 'F20':('F19+F20','N08+N09','lower group paragraph'),
 'F21':('F21','F14','kernel relations'),
 'C18':('C18','C18','surjectivity insertions and parentheses'),
 'F22':('F22','F15+F16','surjectivity insertions and parentheses'),
 'F23':('F24','F16','surjectivity insertions and parentheses'),
 'C19':('C19','C19','cartesian line'),
 'F24':('F25','F17','cartesian line'),
 'C20':('C20','C20','final ex. and noun'),
 'C21':('C21','C21','final ex. and noun')}
fallback={('F02','R2'):'No upper detached traces in reading.tex or report.',('F02','R3'):'No upper detached traces in reading.tex or report.',('F25','R3'):'First two formula starts aligned left, box inset to the right in reading.tex.',('F15','R2'):'No far-right point pair in reading.tex or inventory.'}
fs=copy.deepcopy(rep['R1']['findings'])
assert len(fs)==46 and set(mapping)=={f['id'] for f in fs}
for f in fs:
 k=f['id'];r2,r3,o=mapping[k];z=ob[o]
 f['readers']={'R1':f['final'],'R2':vals('R2',r2) if r2 else fallback[(k,'R2')],'R3':vals('R3',r3) if r3 else fallback[(k,'R3')]}
 f['crop']='; '.join(z['crops']);f['evidence']=z['evidence']
 f['decision']='Main compared all three complete returns and inspected the named crop; retain the recorded ink reading.'
by={f['id']:f for f in fs}
def upd(k,**kw):by[k].update(kw)
upd('F01',final=r'Donnée de $q$ équivaut : \unsure{l|la} donnée de',confidence='medium',decision='Resolve the colon with R1/R3, but retain R2’s article doubt. The isolated tall loop establishes l; no separate a is secure. Singular Donnée and équivaut are clear. These adjacent opening changes are counted as one phrase locus.')
upd('F02',decision='Retain R1’s two geometrically drawn detached traces with writing-versus-surface uncertainty; R2/R3 omit them. No punctuation meaning is assigned.')
upd('C02',doubt_action='retain',decision='Retain q|g from R1. The lower loop is compatible with either underform; R2/R3 retain q without another candidate. The overwritten state is definite.')
upd('C04',doubt_action='retain',decision='Prefer pl.|pol. with R1/R3 over R2’s opposite order. Preserve the whole un ... à un nb phrase omitted in H.')
upd('C05',doubt_action='resolve',decision='All readers and the main crop resolve cotés without a circumflex; preserve the written spelling.')
upd('C06',final='autom',doubt_action='resolve',confidence='medium',decision='Resolve the compressed abbreviation with R2 and omit the absent point; R1/R3 retain some uncertainty. The letters are supported and the broad following gap has no point.')
upd('C07',doubt_action='resolve',decision='All three readers and main resolve bijection. Preserve the grammar as written; no grammatical repair to bijective.')
upd('C08',c=r'\deleted{\unsure{elle}}',h='elle',final=r'\unsure{\deleted{elle}|elle}',doubt_action='retain',confidence='low',decision='The word elle is clear, but its cancellation is not. Follow R3’s state alternatives, with deleted primary; R1 resolves deletion/word and R2 doubts only the word. The following ce is handled separately below.',kind='deletion state (struck given live or live given struck)')
upd('C09',doubt_action='resolve',decision='Resolve bijectif with all three readers; its final f is visible. H’s bijective is not adopted.')
upd('C10',doubt_action='retain',decision='Retain R1/C’s doubt beneath the long cancellation; R2/R3 resolve mais. H has the same primary deleted word, so no confidence-only H change is counted.',diff_c=False,diff_h=False)
upd('C11',doubt_action='retain',decision='Retain pour tt under the strike. It belongs before ses fibres on the preceding line; H’s struck illegible fragment before Sommet represents this same cancellation, and is counted once for reading/placement.')
upd('F06',consequential=True,math_note='The ink says vides ou de cardinal 2, not H’s toutes de cardinal 2. The n=4 certificate refutes the latter statement for fibres over the full reflection coset; see M012-H-EVEN and M012-N4-CERT.')
upd('C12',doubt_action='resolve',decision='Resolve gén. with R1/R3; R2 retains it. The g descender, small raised accent, short n and point are supported.')
upd('C13',final=r"\uline{unique} \uline{\unsure{élémt|élément} d'ordre} 2 de $Z$ appelé \unsure{symétrie|symetrie}",doubt_action='retain',decision='Retain élémt|élément. This row records H’s missing unique/order/called-symmetry clause as a single omission; the new accent doubt in symétrie is separately recorded without double-counting that H omission. The C update counted here is the element-word alternatives; its separate accent update is N02.')
upd('C14',doubt_action='resolve',decision='Resolve Mon with all readers: no final t or point is visible. Its possible expansion remains in the abbreviation notes only.')
upd('F10',decision='Prefer sss|ssi with R1/R2, while R3 favors ssi|sss. No independent final i dot is secure; retain both.')
upd('C15',doubt_action='retain',decision='Retain conjugués, whose ending crosses the enclosure. Preserve the visible surrounding sont and mod omitted in H.')
upd('F11',decision='Preserve R1’s slanted line-node geometry with the left margin explicitly selected and then reset. A short heavy rule and a separate sweeping thin curve are drawn; no closed rectangular frame or arrow meaning is supplied.')
upd('C16',doubt_action='retain',decision='All readers and main retain S|B; the reinforced stem does not warrant a certain reading. H’s primary S matches, so no H confidence-only change is counted.')
upd('F13',decision='Use the actual tikzcd square from R2: E/S above P/F, with both vertical arrows upward. R1/R3 use generic TikZ for the same geometry. H’s editorial note acknowledges the manuscript orientation, but its actual diagram reverses it.')
upd('F14',decision='Place the set block beside the lower square row. Preserve vertical equality below the initial P, no second P, and no comma. The wider root crop examines this separate layout locus, not a second reading of the settled S/B object.')
upd('F15',decision='Retain R1/R3’s detached pair as uncertain drawn points. R2 omits them; writing versus surface trace remains unresolved.')
upd('C17',final='Detached definite hooked stroke, geometrically drawn without a lexical assignment.',diff_c=True,diff_h=True,doubt_action='resolve',confidence='high',kind='drawing or diagram',decision='Choose R2/R3’s direct drawing. This resolves how the mark is represented, without asserting that it is the letter s or assigning its purpose; R1/C’s lexical doubt is recorded in the comparison.')
upd('F17',final=r'\unsure{grpes|groupes}',diff_c=True,diff_h=True,decision='Prefer R2/R3’s contracted grpes, retaining R1/C/H groupes as an alternative. This is a reading change as well as a new C doubt, not merely an H confidence change.')
upd('F18',final=r'hom de \unsure{grpe|groupe}',decision='No point follows hom. Retain the noun doubt with R1/R3; R2 resolves grpe. The compressed middle cannot securely exclude groupe.')
upd('F19',decision='All readers retain grpe|groupe here; the occurrence is judged independently from the preceding noun.')
upd('F20',decision='Retain ds|dans with R1/R3, despite R2’s resolved ds; all retain the final noun grpes|groupes. The paragraph’s two contractions are not silently expanded.')
upd('C18',doubt_action='resolve',decision='All readers and main find no independent opening parenthesis; the stroke is joined to b. Preserve the separate closing parenthesis as written.')
upd('F22',decision='Preserve the actual raised :E—S and its curved lower connector, using R1’s stacked placement. The map stroke is headless; no arrowhead is supplied from its mathematical role.')
upd('C19',doubt_action='retain',decision='Retain diagrammes under the cancellation: d and g survive, but much of the middle is obscured. H’s same primary reading differs only in confidence and is excluded.')
upd('C20',doubt_action='resolve',decision='All readers and main resolve ex. without t; its possible expansion is not placed in the transcription.')
upd('C21',final=r'\unsure{grpe|groupe|grpes|groupes}',doubt_action='retain',decision='Choose R2/R3’s four candidates, contracted singular first. The compact middle and ending do not securely determine ou or final s; R1’s full singular primary is not forced.')

def add(k,place,c,h,final,ok,readers,kind,dc=True,dh=True,confidence='low',decision=''):
 z=ob[ok]
 fs.append(dict(id=k,place=place,c=c,h=h,final=final,crop='; '.join(z['crops']),evidence=z['evidence'],readers=readers,kind=kind,diff_c=dc,diff_h=dh,marked_in_H=False,confidence=confidence,decision=decision,doubt_action='',s_id='',math_note=''))
add('N01','NB short live word following elle','ce','(omitted)',r'\unsure{ce}','NB elle and ce',{'R1':'ce','R2':'ce','R3':r'\unsure{ce}'},'omission',decision='Retain R3’s new uncertainty: the small word is separate from elle, but its e is compressed. Its omission in H is distinct from the deletion-state disagreement.')
add('N02','Marginal accent in symétrie','symétrie','Inside the clause already counted as omitted at C13',r'\unsure{symétrie|symetrie}','left note lettering',{'R1':'symétrie','R2':'symétrie','R3':r'\unsure{symétrie|symetrie}'},'other',dh=False,decision='Retain R3’s accent doubt. No independent acute is secure in the slanted word. The larger H clause omission is already counted at C13, so it is not counted a second time.')
add('F26','Second opening parenthesis before bijectif','(bijectif)','(bijectif)','bijectif)','surjectivity insertions and parentheses',{'R1':'(bijectif)','R2':'bijectif)','R3':'(bijectif)'},'text not on the page',confidence='medium',decision='Choose R2: the tall initial stroke joins the b body, with no separate opening curve. The separate right parenthesis and final stop remain.')

text=(root/'readings/scan012/R1/reading.tex').read_text()
text=text.replace('équivaut : la donnée de',r'équ ivaut : \unsure{l|la} donnée de'.replace('équ ivaut','équivaut'))
text=text.replace(r'\unsure{autom} non orienté','autom non orienté')
text=text.replace(r"\deleted{elle} ce n'est pas",r"\unsure{\deleted{elle}|elle} \unsure{ce} n'est pas")
text=text.replace('{appelé symétrie};',r'{appelé \unsure{symétrie|symetrie}};')
r2=(root/'readings/scan012/R2/reading.tex').read_text()
start=text.index(r'\diagram{');end=text.index('% Detached pair',start)
s2=r2.index(r'\diagram{');e2=r2.index('% Detached, definite',s2)
text=text[:start]+r2[s2:e2]+text[end:]
h2=r2.index('% Detached, definite');he2=r2.index("Solution d'un",h2)
text=text.replace(r'\unsure{$s$}',r2[h2:he2].strip())
text=text.replace(r'\unsure{groupes|grpes}',r'\unsure{grpes|groupes}')
text=text.replace('surjectif (bijectif).','surjectif bijectif).')
text=text.replace(r'\unsure{groupe|groupes|grpe}',r'\unsure{grpe|groupe|grpes|groupes}')
(root/'decisions/scan012_final.tex').write_text(text)

inventory=copy.deepcopy(rep['R1']['inventory'])
inventory[0]['first_words_or_objects']='Donnée de q équivaut : l/la donnée'
inventory[10]['element']='elle, cancellation-state uncertainty'
inventory[10]['first_words_or_objects']='elle, probably canceled but live alternative retained'
inventory[19]['kind']='drawing'
inventory[20]['element']='detached hooked stroke'
inventory[20]['first_words_or_objects']='definite dark upper bulb and lower left hook; no lexical assignment'
inventory[22]['first_words_or_objects']='Si E,F,S des grpes/groupes'
inventory[29]['first_words_or_objects']='Image inverse d’ex. de grpe/groupe/grpes/groupes'

events=copy.deepcopy(json.loads((root/'pending_events/scan012.json').read_text()))
for e in events:
 e['who']=e['who'].replace('main preliminary check','main check')
for r,d in rep.items():
 for i,c in enumerate(d['checks'],1):
  events.append(dict(statement_id=f'R012-{r}-{i:02d}',date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan012 {r} independent reader',type='targeted proof check',outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']))

unresolved=[
 ('Opening article','l','la; no separate a is secure','low'),
 ('Two upper traces','drawn point and paler lower mark','writing versus surface traces','low'),
 ('First Aut argument','G','Z','low'),
 ('Overwritten corollary form','q','g; lower loop beneath sigma','low'),
 ('Canceled des','des','interior strokes obscured by cancellation','low'),
 ('Polygon abbreviation','pl.','pol.','low'),
 ('NB elle state','deleted elle','live elle; the heavy line overlaps cursive joins','low'),
 ('NB small live word','ce','inner e not independently secure','medium'),
 ('Canceled mais','mais','opening and middle obscured by the strike','low'),
 ('Canceled pour tt','pour tt','middle of pour obscured','low'),
 ('Marginal noun','élémt','élément','medium'),
 ('Marginal accent','symétrie','symetrie','low'),
 ('Marginal shorthand','sss','ssi','low'),
 ('Marginal relation word','conjugués','ending intersects enclosure','low'),
 ('Square target','S','B','medium'),
 ('Far-right detached pair','two drawn points','writing versus surface trace','low'),
 ('First lower group noun','grpes','groupes','medium'),
 ('After hom de','grpe','groupe','low'),
 ('After P un','grpe','groupe','low'),
 ('Before cat.','ds','dans','low'),
 ('Parenthetical final noun','grpes','groupes','low'),
 ('Canceled diagrammes','diagrammes','middle and ending concealed by strike','low'),
 ('Final noun','grpe','groupe; grpes; groupes','low')]
notes="""This handwritten page continues the choice of a section q, describes it by an involution sigma over −1, computes the change from sigma_t to sigma_tg, and states odd/even consequences. A slanted left note treats opposite generators, the unique element of order two, and opposite vertices. The lower Parenthèse introduces the fiber product of sets and groups, its kernels, and preservation of surjectivity and bijectivity. Internal underlined labels include Corollaire, NB, Sommet, opposé and Parenthèse. There is no date or independent title; archive 11 is comment-only. Mon remains literal lettering, not an expanded instruction. No explicit authorial doubt wording is securely identified. There is no S row.

All 21 C doubts were explicitly inspected. Nine were resolved: cotés, autom without a point, bijection, bijectif, gén., Mon, the detached hook’s geometric representation, the absent first opening parenthesis, and ex. Twelve remain, including elle’s deletion state rather than its readable word. Eleven new uncertainties concern the opening article, detached trace pairs, ce, the marginal accent and equivalence shorthand, and independent lower contractions. C changes include these editorial doubt updates, not only errors. H macro equivalents for emphasis are excluded. Its missing marginal clause is counted once; the additional accent doubt is not a second H omission. The cancellation before ses fibres is the same fragment H relocates before Sommet, not an extra deletion.

The opening keeps singular Donnée and équivaut, a colon, and the uncertain article l|la. The first formula starts are left-aligned, and the boxed repeat lies below the right end. The margin retains actual slanted lines, a separate heavy rule and a thin sweeping curve. The square is written in tikzcd with E/S above P/F and upward q and q′; the set description starts beside the lower row, with a vertical equality and no extra P. Both headless map strokes, the raised :E—S with its curve, the raised carrés replacement, and both unmatched closing parentheses are preserved. The detached hook has no assigned lexical value; separate point pairs retain writing-versus-surface uncertainty.

The mathematical checks in CHECK_EVENTS.tsv are actual checks, distinct from reading. In the inherited cyclic torsor setting with n≥3 and distinct ±1, a homomorphic section is equivalent to an element sigma over −1 satisfying sigma²=1. Choosing a cyclic coordinate writes every such map as x↦b−x; the unique one fixing t has b=2t. Conjugating by translation a gives sigma_(t+a), and direct multiplication verifies every equality in the displayed chain. The n=2 case needs the earlier exception: the sign quotient then collapses, so an arbitrary involution does not specify a section of it.

Multiplication by 2 on Z/n is invertible for odd n. For n=2m its kernel is {0,m}; each nonempty fibre has two elements and other fibres are empty. An explicit computed n=4 certificate lists all four reflections: b=0 has fixed vertices 0,2; b=2 has 1,3; b=1 and b=3 have none. This refutes H’s claim that all fibres have cardinal two over the full reflection coset; the refined statement is M012-EVEN. It does not select manuscript wording. The element s=u^m=bar(u)^m has order two and is independent of the chosen generator; multiplication by s gives the canonical opposite-vertex involution. The marginal phrase conjugués mod {1,s} is interpreted conditionally as belonging to the same orbit, not literal group conjugacy. For a cyclic polygon with n≥3, adjacency-preserving maps are x↦b±x; the manuscript’s non orienté is interpreted here as orientation-reversing, as indicated by p=−1. Interpreting it as all unoriented graph automorphisms would include the identity and destroy the stated uniqueness. No interpretation is inserted into the ink transcription.

For sets, P={(x,y):p(x)=q(y)} with its coordinate projections has the universal property by the unique pair map. For groups it is a subgroup of E×F, and the same pair map is a homomorphism. The kernel isomorphisms are explicit: k↦(k,1) identifies ker p with ker p′, and k↦(1,k) identifies ker q with ker q′. The fibre of p′ over y is p^−1(q(y)), proving preservation of surjectivity and bijectivity without choosing a global family of lifts. Conditionally interpreting ex. as extension, pulling back 1→K→E→S→1 gives 1→K→P→F→1. That check does not settle the abbreviation’s expansion."""
dec=dict(base='R1',text_file='decisions/scan012_final.tex',findings=fs,inventory=inventory,notes=notes,events=events,unresolved=[dict(place=p,reading=x,alternatives=a,confidence=c) for p,x,a,c in unresolved],abbreviations=copy.deepcopy(rep['R1']['abbreviations']),main_crop_count=7,main_crop_views=obs['views'])
(root/'decisions/scan012.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
coverage=json.loads((root/'decisions/scan012_C_doubt_coverage.json').read_text())
for d in coverage['doubts']:
 k=d['c_doubt_id'];f=by[k];index=next(i for i,x in enumerate(fs,1) if x['id']==k)
 d.update(disposition=f['doubt_action'],findings=[f'S012-{index:03d}'],final=f['final'],crop=f['crop'])
assert sum(x['disposition']=='resolve' for x in coverage['doubts'])==9
(root/'decisions/scan012_C_doubt_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
p=root/'decisions/scan012_witness_comparison_pending.json'
d=json.loads(p.read_text());d['status']='Complete; original comparison questions retained for audit.';d['main_status']='All three final returns read and compared before image review; all listed disagreements and all 21 C doubts inspected; no pending loci.';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(root/'decisions/scan012_review_state.json').write_text(json.dumps(dict(scan=12,status='Adjudication complete, ready for structural validation and commit',all_three_final_returns_fully_read_and_compared=True,all_final_texts_unchanged_from_initial=True,main_crops_created=7,main_views=27,C_resolved=9,C_retained=12),indent=2)+'\n')
print(dict(findings=len(fs),inventory=len(inventory),events=len(events),doubts=len(unresolved),views=len(obs['views'])))
