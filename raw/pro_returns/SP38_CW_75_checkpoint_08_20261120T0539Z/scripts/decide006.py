"""Main-reader scan006 adjudication, from the recorded visual crop decisions."""
from pathlib import Path
import json, copy
O=Path(__file__).resolve().parents[1]
reports={r:json.loads((O/f'readings/scan006/{r}/report.json').read_text()) for r in ['R1','R2','R3']}
obs_path=O/'decisions/scan006_main_observations.json'
obs=json.loads(obs_path.read_text())
for p in ['crops/scan006/07_considerez_line.png','readings/scan006/R2/crops/15_group_map.png','crops/scan006/08_hom.png','crops/scan006/09_ss_grpe.png','crops/scan006/10_corollary.png','crops/scan006/11_final_ss_grpe.png']:
    if p not in obs['main_crop_views']:obs['main_crop_views'].append(p)
obs['observations'].update({'map':'Short shaft has only a tiny downward spur, no resolved paired wings; retain dash|arrow.','considerez_layout':'The word and formula share one baseline.','hom':'Short h plus low om; no point, no second om.','live_subgroup':'Two s strokes, hyphen and compressed grpe, without the ou of full groupe.','corollary_layout':'Underlined Corollaire, formula and où H begin on one baseline, with gloss above.','last_subgroup':'Same two-s, hyphen, grpe contraction; no ou.'})
obs['stage']='all 42 adjudication loci decided; final record assembly'
obs_path.write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n')

# R2 supplies the base; no other reader's raw return is changed.
text=(O/'readings/scan006/R2/reading.tex').read_text()
reps={
    r"\uuline{d'orientation}":r"\unsure{\uuline{d'orientation}|\deleted{\uline{d'orientation}}}",
    r" & $2^{\circ})$":r"\deleted{\unsure{$\{$|$f$}} & $2^{\circ})$",
    "\n\\deleted{\\unsure{$\\{$|$f$}}\n":"\n",
    r"\deleted{\unsure{déf.|b)}}":r"\deleted{\unsure{def.|déf.|b)|Si}}",
    r"\deleted{autom. d'}\unsure{orientations|orientation}":r"\deleted{\unsure{autom.} d'}\unsure{orientation|orientations}",
    r"Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.":r"\inserted{Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.}",
    r"\operatorname{Aut}^{\unsure{e|\varepsilon|+}}(X)":r"\operatorname{Aut}^{\unsure{e|\varepsilon|c|+}}(X)",
    r"\inserted{(produit $\frac{1}{2}$ direct):}":r"\inserted{(\unsure{produit|produits} $\frac{1}{2}$ direct):}",
    r"où $H$ est":r"où $H$ \unsure{est|$\to$}"
}
for a,b in reps.items():
    assert text.count(a)==1,(a,text.count(a))
    text=text.replace(a,b)
# Fixed-width paragraph columns keep the two numbered conditions beside their left-hand marks.
text=text.replace(r'\begin{tabular}{@{}l@{\quad}l@{}}',r'\begin{tabular}{@{}p{.30\linewidth}@{\quad}p{.63\linewidth}@{}}')
(O/'decisions/scan006_final.tex').write_text(text)

fs=copy.deepcopy(reports['R2']['findings'])
f1={int(x['id'][1:]):x for x in reports['R1']['findings']}
f3={int(x['id'].split('-')[-1]):x for x in reports['R3']['findings']}
mapping={2:(1,1),3:(2,2),4:(3,3),5:(4,4),6:(5,5),7:(6,6),8:(7,8),9:(8,9),10:(9,10),11:(10,11),12:(11,12),13:(12,13),14:(13,14),15:(14,15),16:(16,16),17:(17,17),18:(18,18),19:(19,20),20:(19,21),21:(21,22),22:(22,23),23:(23,24),24:(24,25),25:(24,26),26:(25,27),27:(26,28),28:(27,29),29:(28,30),30:(29,31),31:(30,32),32:(31,33),33:(32,34),34:(33,None),35:(34,35),36:(35,36),37:(36,37),38:(37,38),39:(38,39),40:(39,40),41:(40,41),42:(41,7)}
for i,f in enumerate(fs,1):
    if i==1:f['readers']={'R1':'sous-groupes','R2':f['final'],'R3':'sous-groupes'}
    else:
        a,b=mapping[i];f['readers']={'R1':f1[a]['final'],'R2':f['final'],'R3':f3[b]['final'] if b else r'\operatorname{Aut}^{+}(X)'}
    f['decision']='All three readings compared. Main crop supports the consolidated reading; surviving uncertainty is kept in place.'
    f.pop('consequential',None)
    f.pop('math_note',None)

def update(n,**kw):fs[n-1].update(kw)
def proof(n,key,crop=None):
    update(n,evidence=obs['observations'][key])
    if crop:update(n,crop=crop)
rootc=lambda name:'crops/scan006/'+name+'.png'
r2c=lambda name:'readings/scan006/R2/crops/'+name+'.png'
proof(1,'opening');update(1,diff_h=False,kind='other',decision='R2 retained because the contracted middle does not securely show ou. H has the same primary reading, so no H confidence-only row is counted.')
proof(2,'opening')
proof(3,'five_dots',rootc('01_opening_dots'))
proof(4,'heading_tail');proof(5,'prop',rootc('02_prop'));proof(6,'soit_tail');proof(7,'strict_word')
update(8,place='Part a: Un replacement and punctuation after X',c=r'\deleted{Un}\inserted{Soit $g$ un} autom. $g$ de $X$',h=r'Soit \struck{Un} $g$ un autom. $g$ de $X$.',final=r'\deleted{Un}\inserted{Soit $g$ un} autom. $g$ de $X$')
proof(8,'a_rewrite',rootc('03_a_rewrite'))
update(9,place='Part a: canceled predicate and Conditions équiv. insertion',c=r'\deleted{est dit \uline{\unsure{direct}}.}\inserted{Conditions équiv.}',h=r'\emph{Conditions équiv.} \struck{\ill{}} :',final=r'\deleted{est dit \uline{\unsure{direct}}.}\inserted{Conditions équiv.}')
proof(9,'direct_conditions','readings/scan006/R1/crops/05_direct_conditions.png')
update(10,final=r"\unsure{\uuline{d'orientation}|\deleted{\uline{d'orientation}}} beside first condition",confidence='low',diff_h=False,decision='Choose R3 ordering: live double underline first, cancellation alternative retained. Layout follows the shared baseline seen in the context crop, not R3’s separate paragraph.')
proof(10,'separate_dorientation');fs[9]['evidence']+=' '+obs['observations']['condition_layout']+'; context crop '+rootc('04_conditions_layout')
proof(11,'si');proof(12,'A_gap',rootc('05_A_gap'));proof(13,'brace')
update(13,c=r'\deleted{\unsure{$\{$|$f$}} after the second condition',final=r'\deleted{\unsure{$\{$|$f$}} left of the second condition',diff_c=True,decision='R1 retains the observed side-by-side placement; R2/R3 put the sign below the pair. Main context crop shows it to the left of 2°. Sign identity stays uncertain.')
fs[12]['evidence']+=' Placement: '+rootc('04_conditions_layout')
update(14,final=r'\deleted{\unsure{def.|déf.|b)|Si}}',decision='Main favors a lower-case def. from initial loop, medial curve, long final descender and point. Keep accented and heavily obscured C alternatives; R3 capital D is not securely present.')
proof(14,'before_on_dit')
fs[14]['readers']['R1']=f1[14]['final']+' '+f1[15]['final']
proof(15,'d_prefix');update(15,decision='Choose R2: cancellation continues through d′; retain the doubt on the underlying autom. R1’s state alternative and R3’s live prefix are recorded.')
proof(16,'omega_subset','readings/scan006/R1/crops/11_omega_subset.png');proof(17,'omega_subset')
proof(18,'ens_des');fs[17]['readers']={'R1':r"l'ens des\unsure{.}",'R2':r"l'ens des\unsure{.}",'R3':r"l'ens des\unsure{.}"}
proof(19,'b_cancellation');update(19,final=r"\deleted{\unsure{autom.} d'}",confidence='medium',diff_c=True,decision='Choose R3 doubt on autom. under the heavy crossing; d′ is securely canceled.')
proof(20,'b_cancellation');update(20,final=r'\unsure{orientation|orientations}',diff_h=False,decision='Choose R3’s singular-first order: there is no separately resolved final s. H’s primary orientation agrees; its prefix cancellation is handled in the preceding locus.')
update(21,final=r'\inserted{Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.} before Alors',diff_c=True,confidence='medium',decision='Choose R3 insertion state: smaller interlinear writing lies between the two larger lines. R1/R2 preserve sentence order but omit insertion status.')
proof(21,'inverse_placement',rootc('06_inverse_context'))
proof(22,'strictness_clause');proof(23,'strictness_clause');proof(24,'strictness_clause');proof(25,'strictness_clause')
update(24,decision='Choose R2 c=: its low return and the separate equals are visible. R1/R3 retain the opening-parenthesis alternative, which the main crop resolves.')
for n in [26,27,28,29]:proof(n,'canceled_c','readings/scan006/R3/crops/15_cancelled_c.png')
proof(30,'map');proof(31,'considerez_layout',rootc('07_considerez_line'));proof(32,'hom',rootc('08_hom'));proof(33,'live_subgroup',rootc('09_ss_grpe'))
proof(34,'aut_superscript');update(34,final=r'\operatorname{Aut}^{\unsure{e|\varepsilon|c|+}}(X)',decision='R2’s letterlike e first, with epsilon and R1’s c and plus retained. R3 resolves plus; main finds no secure straight crossing. No algebraic expectation is used to choose the glyph.',consequential=True,math_note='The superscript identifying the purported cyclic subgroup is letterlike and unresolved; C/H’s unmarked + is not forced into the ink.')
proof(35,'tt');proof(36,'corollary_layout',rootc('10_corollary'))
proof(37,'product_gloss');update(37,final=r'\inserted{(\unsure{produit|produits} $\frac{1}{2}$ direct):}',diff_c=True,confidence='medium',decision='Keep R3’s uncertainty on produit(s); direct and the colon are secure. The gloss remains an insertion.')
proof(38,'h_est');update(38,final=r'où $H$ \unsure{est|$\to$}',diff_c=True,confidence='low',decision='Retain R1’s est/arrow alternative. The flat trace resembles other compressed est but has an arrowlike upturn; R2/R3 resolve est more strongly than the main crop supports.')
proof(39,'last_subgroup',rootc('11_final_ss_grpe'));proof(40,'etant');proof(41,'fixe');proof(42,'pentagon')
update(40,decision='Choose R1/R2’s unaccented etant|etans|dans. R3’s acute variants are unsupported by a separate mark above the first letter.')
update(42,decision='Use R2’s rendering of detached patches. R1 agrees on detachment; R3 keeps C’s joining stroke, but blank paper separates the patch from the right vertex. Do not assign these marks arrow or vertex semantics.')

# All 17 original C doubts have a recorded disposition; strict and autom stay doubtful.
assert {4,6,7,9,11,13,14,15,16,22,23,24,28,30,35,40,41}=={i+1 for i,f in enumerate(fs) if f.get('doubt_action')}
for f in fs:
    assert f['crop'] in obs['main_crop_views'],(f['id'],f['crop'])

inventory=copy.deepcopy(reports['R3']['inventory'])
for x in inventory:
    el=x['element']
    if el=='Cancelled marker before definition':x['first_words_or_objects']='def. | déf. | b) | Si, all canceled'
    if el=='Definition sentence':x['first_words_or_objects']='On dit que g est une [canceled autom. d′] orientation de X.'
    if el=='Cancelled word in definition':x['first_words_or_objects']='autom. (uncertain) and d′, canceled'
    if el=='Inserted strictness qualification and curved connector':x['first_words_or_objects']='(si X est strict i.e. si c=card S ne 2), attached after cardinality assertion'
    if el=='Cyclic generation statement':x['first_words_or_objects']='De plus, Aut with unresolved raised e | epsilon | c | plus ... engendré par tt g in omega(X).'
    if el=='Underlined corollary and quotient expression':x['first_words_or_objects']='Corollaire Aut(X) simeq Z/2Z dot Z/H, où H est | arrow ...'
    if el=='Final parenthesis':x['first_words_or_objects']='(g etant | etans | dans une orientation fixé)'
    if el=='Pentagon with angular strokes and detached lower ink':x['first_words_or_objects']='five sides, corner patches, heavier lower-right side, detached right and lower marks'

unresolved=copy.deepcopy(reports['R2']['unresolved'])
for u in unresolved:
    if u['place']=='Canceled label before On dit':u.update(reading='def.',alternatives='déf.; b); Si')
    if u['place']=='b orientation ending':u.update(reading='orientation',alternatives='orientations')
    if u['place']=='Superscript on Aut in De plus':u['alternatives']='epsilon; c; plus'
unresolved.extend([
 {'place':'Separate d’orientation beside condition 1','reading':'live, doubly underlined d’orientation','alternatives':'canceled, singly underlined d’orientation','confidence':'low'},
 {'place':'b canceled prefix','reading':'autom.','alternatives':'No equally supported complete alternative; interior covered by cancellation.','confidence':'medium'},
 {'place':'Corollary inserted gloss','reading':'produit','alternatives':'produits','confidence':'medium'},
 {'place':'Corollary after H','reading':'est','alternatives':'right arrow','confidence':'low'}])
# Keep doubts in manuscript order.
order=['Opening subgroup word','Canceled heading tail','Canceled sign after Soit','Canceled interlinear qualification','Canceled direct','Separate d’orientation beside condition 1','Isolated canceled sign','Canceled label before On dit','Canceled autom. after une','Point after des in b','b canceled prefix','b orientation ending','Punctuation after cardinality 2','Canceled membership target after 2','Canceled triv ending','Map sign after Considérons','Superscript on Aut in De plus','Corollary inserted gloss','Corollary after H','Final parenthesis word after g']
unresolved.sort(key=lambda x:order.index(x['place']))

events=json.loads((O/'pending_events/scan006.json').read_text())
events[1]['outcome']=events[1]['outcome'].replace('This check awaits visual adjudication of the manuscript wording and supplies no transcription.','Main crop now confirms the wording Conditions équiv.; the false equivalence is preserved as written, conditional on the stated adjacency interpretation.')
for r in ['R1','R2','R3']:
    for j,ch in enumerate(reports[r].get('checks',[])):
        sid='M006-K' if (r=='R1' or r=='R2' and j==0) else 'M006-I'
        events.append({'statement_id':sid,'date':'2026-11-20','who':f'GPT-6 Astra Pro; effort inherited/not exposed; scan006 {r}','type':'targeted proof check','outcome':ch['statement']+' '+ch['reasoning']+' '+ch['outcome']})

notes="""The page continues the classification by proper subgroups H of Z, then bears the underlined heading “Orientation d'un contour”. It gives two conditions labeled “Conditions équiv.”, defines the orientation set, asserts two inverse orientations in the strict case, and states the automorphism action, index-two kernel, cyclicity and a half-direct-product corollary. The initial strict is both inserted and canceled; the later strictness qualification is attached to the cardinality assertion. The small inverse sentence is an interlinear insertion before Alors. Two contour sketches, the abandoned three-line c) definition and its unfinished “[i.e.” are retained. The duplicate g in the rewritten a) sentence and final “une orientation fixé” remain as written. The later Aut superscript is unresolved (e/epsilon/c/+); the algebra does not select its ink.

Mathematical checks: under distinct vertex/edge adjacency, the four-cycle refutes the asserted equivalence (M006-E). Label vertices modulo 4: g(s)=1−s sends every vertex to a neighbor, but fixes two edges and exchanges two disjoint edges; g(s)=−s gives the reverse failure. Complete enumeration of all eight automorphisms confirms that requiring both conditions selects only the two unit rotations (M006-O4). For a connected strict contour, the separately checked conjunction refinement M006-O gives the two unit rotations, cyclic translation kernel and semidirect product by inversion. This does not validate the written equivalence, which is transcribed unchanged. The two-vertex/two-parallel-edge case has automorphism group C2×C2 and, under the conjunction, a singleton orientation set (M006-D2); thus the later two-element target/index assertion needs strictness if that case was intended to be included. These checks prompted attention to Conditions équiv., the canceled strict, the c=card S≠2 insertion and Aut superscript; each was decided from its crop. Reader checks M006-K and M006-I establish only the conditional kernel-index inference and elementary inverse-pair cardinality.

No secure explicit authorial doubt formula or date appears. The canceled heading abbreviation is not expanded into an authorial claim. Archive foliation 5 is retained only as a comment; there is no author page count."""
ab=copy.deepcopy(reports['R2']['abbreviations'])
for a in ab:
    if a['written'].startswith('déf.'):a['written']='def. | déf. (uncertain, canceled)'
ab.append({'written':'sous-grpes (alternative reading)','expansion':'sous-groupes'})
dec={'base':'R2','text_file':'decisions/scan006_final.tex','findings':fs,'inventory':inventory,'notes':notes,'events':events,'unresolved':unresolved,'abbreviations':ab,'main_crop_count':11,'main_crop_views':obs['main_crop_views']}
(O/'decisions/scan006.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
print({'findings':len(fs),'C_doubts':sum(bool(f.get('doubt_action')) for f in fs),'unresolved':len(unresolved),'inventory':len(inventory),'main_views':len(obs['main_crop_views']),'events':len(events)})
