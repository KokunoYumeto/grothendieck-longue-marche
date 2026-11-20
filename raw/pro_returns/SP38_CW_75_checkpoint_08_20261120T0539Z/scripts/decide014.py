from pathlib import Path
import copy,json

root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan014'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan014_main_observations.json').read_text())
def get(r,k):return next(f for f in rep[r]['findings'] if f['id']==k)
def vals(r,ks):return '; '.join(get(r,k)['final'] for k in ks.split('+'))
def p(r,n):
    names={('R2',1):'01_c_formula',('R1',4):'crops/04_sequence_comment',('R1',5):'crops/05_margin_oval',('R3',17):'crop17_detached_marks',('R2',4):'04_vector',('R1',6):'crops/06_vector_insertion',('R1',8):'crops/08_cancelled_E',('R2',6):'06_affine_data',('R1',7):'crops/07_vector_article_noun',('R2',7):'07_torsor_open',('R1',10):'crops/10_sous_groupe',('R1',11):'crops/11_cancelled_application',('R2',9):'09_cancelled_map',('R2',10):'10_torsor_close',('R2',11):'11_affine_underlining',('R1',13):'crops/13_cancelled_Gamma',('R1',14):'crops/14_comm_et',('R2',13):'13_projective_P',('R2',14):'14_definition',('R1',16):'crops/16_projective_annotation',('R1',19):'crops/19_projective_Isom_subscript',('R2',16):'16_bottom_caption'}
    return f'readings/scan014/{r}/{names[r,n]}.png'
def m(n):return 'crops/scan014/'+{1:'01_sequences',2:'02_considered_base',3:'03_ss_grpe',4:'04_hom',5:'05_projective_layout',6:'06_bottom_layout'}[n]+'.png'
mapping={f'C{i:02d}':(f'C{i:02d}',f'C{i:02d}') for i in range(1,15)}
mapping.update({'X01':('F02','F02'),'X02':('F03','F02'),'X03':('F04','F03'),'X04':('F05','F04'),'X05':('F06','F05+F06'),'X06':('F07','F08'),'X07':('F08','F10+F12'),'N01':('F09','F13'),'X08':('F09','F13'),'X09':('F09','F14'),'X10':('F10','F15'),'N02':('N05','F16'),'X11':('F11','F18'),'X12':('F12','F20'),'X13':('N07+F13','F19'),'X14':('F12','F20'),'X15':('F14','F21'),'X16':('F15','F22'),'N03':('F16','F23'),'X17':('F15','F24'),'X18':('F17','F25'),'X19':('F18','F26'),'X20':('F19','F27'),'N04':('',''),'X21':('F20','F28'),'X22':('F21','F29'),'X23':('F22','F30'),'S01':('S01','S01')})
cp={'C01':[p('R2',1)],'C02':[p('R2',1)],'C03':[p('R1',4)],'C04':[p('R1',5)],'C05':[p('R1',7)],'C06':[p('R1',7)],'C07':[p('R1',8)],'C08':[p('R2',7)],'C09':[p('R1',11)],'C10':[p('R2',9)],'C11':[p('R1',13)],'C12':[p('R2',13)],'C13':[p('R1',16)],'C14':[p('R2',16)],'X01':[m(1)],'X02':[m(1)],'X03':[p('R1',5)],'X04':[p('R1',5)],'X05':[p('R2',4),p('R1',6)],'X06':[p('R1',8)],'X07':[p('R2',7)],'N01':[p('R1',10)],'X08':[p('R1',10),m(2)],'X09':[m(2)],'X10':[p('R1',11)],'N02':[p('R1',11)],'X11':[m(3)],'X12':[p('R2',10)],'X13':[p('R2',10)],'X14':[p('R2',10)],'X15':[p('R2',11)],'X16':[p('R1',14)],'N03':[p('R1',14)],'X17':[m(4)],'X18':[p('R2',13)],'X19':[p('R2',14)],'X20':[p('R2',14)],'N04':[p('R1',19)],'X21':[p('R1',16),m(5)],'X22':[m(5)],'X23':[m(6),p('R2',16)],'S01':[p('R1',8),p('R2',6)]}
oi={'C01':0,'C02':0,'C03':1,'C04':2,'C05':7,'C06':7,'C07':5,'C08':8,'C09':10,'C10':11,'C11':14,'C12':16,'C13':18,'C14':20,'X01':21,'X02':21,'X03':2,'X04':2,'X05':4,'X06':5,'X07':8,'N01':9,'X08':22,'X09':22,'X10':10,'N02':10,'X11':23,'X12':12,'X13':12,'X14':12,'X15':13,'X16':15,'N03':15,'X17':24,'X18':16,'X19':17,'X20':17,'N04':19,'X21':18,'X22':25,'X23':26,'S01':6}
fs=copy.deepcopy(rep['R1']['findings'])
for f in fs:
    k=f['id'];a,b=mapping[k]
    f['readers']={'R1':f['final'],'R2':vals('R2',a) if a else r'Plain ens in reading.tex; no separate uncertainty.','R3':vals('R3',b) if b else r'Plain ens in reading.tex; no separate uncertainty.'}
    f['crop']='; '.join(cp[k]);f['evidence']=obs['observations'][oi[k]]['decision']
    f['decision']='All three complete final returns were compared before main crop review. '+f['evidence']
by={f['id']:f for f in fs}
def upd(k,**kw):by[k].update(kw)
upd('C01',evidence='Open enclosing scroll and central return are clear; Fraktur versus calligraphic S remains insecure.')
upd('C02',evidence='The tall crossed and reinforced A has no separately recoverable canceled underform; Fraktur/calligraphic alternatives remain.')
upd('C04',final=r'\mathbb{P}(V)',doubt_action='resolve',confidence='high',diff_c=True,diff_h=False)
upd('C06',final=r'\unsure{élemt|élémt|élement|élément}',diff_c=True,confidence='low')
upd('C08',final=r'\unsure{général|générale}',diff_c=True,diff_h=True,doubt_action='retain')
upd('C09',c=r'\deleted{\unsure{savoir application}}',h=r'\struck{\ill{}}',final=r'\deleted{\unsure{savoir application}}',evidence='The crossed low savoir sequence and tall/descending application strokes support the primary words but leave letters obscured. The separate product/shaft is recorded at N02.')
upd('C10',place='Canceled map, result characters and their state',c=r'\deleted{...\unsure{6x|sx}}',h=r'\struck{...\mapsto}\ill{}',final=r'\deleted{\unsure{6x|sx|\delta x}}',diff_c=True,evidence='The result has a high curving hook and lower loop followed by x; 6, s and delta remain possible. The deletion crosses both result characters. The shaft is treated separately at Y08.')
upd('C13',final=r'\unsure{(0)|(0}',doubt_action='retain',confidence='low',diff_c=True,diff_h=True)
upd('X03',final=r'\operatorname{GP}(V)\text{ \unsure{opere|opère} dessus}, with no colon or y',diff_c=True,confidence='medium')
upd('X07',place='Raised torseur replacement, words and placement',c=r'\deleted{espace affine}\inserted{torseur (à droite, disons) $E$}',h=r'(\uncertain{torseur} \uncertain{Ed} \uncertain{abstrait}, disons) $E$ before canceled predecessor',final=r'\inserted{torseur (à droite, disons) $E$} above its canceled predecessor',evidence='The raised line reads torseur (à droite, disons) E, with E outside the parenthesis; it overlays the old phrase. The old phrase ending is independently treated at Y07.')
upd('N01',final=r'sous \unsure{grpe|groupe} non précisé',c='sous groupe non précisé',h='sous un groupe non précisé')
upd('X08',c='peut être considéré comme',h="que l'on considère comme",final='peut être considéré comme')
upd('X09',c='sur le seul ens de base E,',h='sur le seul ens. E,',final='sur le seul ens de base E,')
upd('X10',c=r'\inserted{p.ex. donnée d’un} after the cancellation',h=r'\uncertain{précisément} donnée d’un',final=r'\inserted{p.ex. donnée d’un} raised above canceled application',evidence='The small upper line reads p.ex. donnée d’un; it lies above the deletion, not on its baseline. The readable canceled words and formula are separate findings.')
upd('N02',c=r'\deleted{$E\times E\times E\mathbin{\text{---}}E$}',h=r'\uncertain{\ill{}} $E$ \struck{\ill{}}',final=r'\deleted{$E\times E\times E\unsure{\mathbin{\text{---}}|\longrightarrow}E$}')
upd('X13',final=r'\unsure{valable} pour ens. à grpe d’op \uline{fidèle}',diff_c=True,confidence='medium')
upd('N03',final=r'\unsure{\deleted{et}|et}',diff_c=True,diff_h=True,confidence='low')
upd('X22',final='Stepped divider drawn in the same layout as the source quotient: higher left portion, descending bend and lower right continuation',diff_c=True,evidence='The higher segment runs below Isom and above Aff, bends down beside the quotient, and continues beneath it to the right. It is tied to that annotation rather than detached into a subsequent centered figure.')
upd('S01',s_decision='confirmed',consequential=True,math_note='SA01-K75-02 confirmed from ink: prose E versus Isom target V. Retain V. M014-AFF-MIXED refutes the unqualified mixed-base classification; refined M014-AFF-STRUCT uses E on both sides.')

def add(k,place,c,h,final,readers,crops,ob,kind='other',dc=True,dh=True,confidence='medium',evidence=None):
    ev=evidence or obs['observations'][ob]['decision']
    f=dict(id=k,place=place,c=c,h=h,final=final,readers=readers,crop='; '.join(crops),evidence=ev,decision=ev,kind=kind,diff_c=dc,diff_h=dh,marked_in_H=False,confidence=confidence,doubt_action='',s_id='',math_note='')
    fs.append(f);by[k]=f
add('Y01','c), opening delimiter after first Aff',r'\operatorname{Aff}(2,\mathbb F_2)',r'\operatorname{Aff}(2,\mathbf F_2)',r'\operatorname{Aff}\,2,\mathbb F_2)',{'R1':'Opening parenthesis present; crop outcome explicitly resolves it.','R2':vals('R2','F01'),'R3':vals('R3','F01')},[p('R2',1)],0,'text not on the page',confidence='high')
add('Y02','Vector correspondence, continuation placement','Entire correspondence in one prose paragraph','Formula separately centered after prose','First line ends at the element noun; de and Isom quotient continue beneath the right side',{'R1':'One ordinary prose paragraph with inline quotient.','R2':'Two aligned rows in reading.tex.','R3':vals('R3','F07')},[p('R2',4)],4,'insertion or placement',confidence='high')
add('Y03','Affine correspondence, two rows','One display row','Inline correspondence and quotient','Correspondence and datum words above; quotient beneath, beginning farther right',{'R1':'One centered display row.','R2':'Two aligned rows in reading.tex.','R3':vals('R3','F09')},[p('R2',6)],6,'insertion or placement',confidence='high')
add('Y04','Affine datum, element noun','élément','élément',r'\unsure{élémt|élément}',{'R1':'élément','R2':vals('R2','N01'),'R3':'élément'},[p('R2',6)],6,'abbreviation expanded or spelling modernised')
add('Y05','Affine denominator, opening parenthesis',r'\operatorname{Aff}(n,k)',r'\operatorname{Aff}(n,k)',r'\unsure{\operatorname{Aff}n,k)|\operatorname{Aff}(n,k)}',{'R1':r'\operatorname{Aff}(n,k)','R2':vals('R2','N02'),'R3':r'\operatorname{Aff}(n,k)'},[p('R2',6)],6,'misread symbol or index',confidence='low')
add('Y06','Canceled first clause, group noun',r'\deleted{si $Z$ est un groupe}',r'\struck{si $Z$ est un groupe}',r'\deleted{si $Z$ est un \unsure{groupe|grpe}}',{'R1':'groupe, certain','R2':vals('R2','N03'),'R3':'groupe, certain'},[p('R2',7)],8,'misread word',dh=False,evidence='The canceled noun has a long g descender and compressed following strokes. The crossing obscures whether the full ou sequence is written. Retain groupe|grpe; H primary agrees, so no substantive H difference.')
add('Y07','Canceled predecessor, affine ending',r'\deleted{espace affine}',r'\struck{espace aff.}',r'\deleted{espace \unsure{affine|aff.}}',{'R1':'espace affine, certain','R2':vals('R2','N04'),'R3':vals('R3','F11')},[p('R2',7)],8,'misread word',confidence='low',evidence='Two tall f strokes and the flattened ending lie under cancellation; affine remains primary, aff. possible. This is separate from the raised replacement wording and placement.')
add('Y08','Canceled pointwise map, shaft',r'\longmapsto',r'\mapsto',r'\unsure{\mathrel{\mapstochar\relbar\joinrel\relbar}|\longmapsto}',{'R1':r'\longmapsto, certain','R2':vals('R2','N06'),'R3':vals('R3','F17')},[p('R2',9)],11,'misread symbol or index',confidence='low',evidence='Left vertical tail is certain. The right terminal blot meets the crossing and does not securely show a head. Choose barred headless first, maps-to alternative; canceled result letters are C10.')
add('Y09','Detached pair right of c)','Absent','Absent','Two drawn points, upper dark and lower gray, uncertain writing/surface origin',{'R1':'Absent','R2':'Absent','R3':vals('R3','F31')},[p('R3',17)],3,'drawing or diagram',confidence='low')

text=(root/'readings/scan014/R2/reading.tex').read_text()
text=text.replace(r'\operatorname{Aff}2,',r'\operatorname{Aff}\,2,',1)
text=text.replace(r'$\operatorname{GP}(V)$ opère',r'$\operatorname{GP}(V)$ \unsure{opere|opère}',1)
text=text.replace(r'\unsure{élémt|élément}}\\',r'\unsure{élemt|élémt|élement|élément}}\\',1)
text=text.replace(r'\unsure{générale|général}',r'\unsure{général|générale}',1)
text=text.replace('sous groupe non précisé',r'sous \unsure{grpe|groupe} non précisé',1)
text=text.replace(r'comm, \deleted{et} un',r'comm, \unsure{\deleted{et}|et} un',1)
marks=(root/'readings/scan014/R3/reading.tex').read_text().split('% Two detached points')[1].split('\nd)')[0]
text=text.replace('\nd)\n','\n% Two detached points'+marks+'\nd)\n',1)
# Place the divider with its projective annotation, using the geometry returned by R3.
r3=(root/'readings/scan014/R3/reading.tex').read_text()
new=r3.split('Structure de $k$-espace projectif')[1].split('\\diagram{')[0]
new=new.replace(r'\operatorname{Isom}_{\text{ens}}',r'\operatorname{Isom}_{\text{\unsure{ens|ens,}}}')
new=new.replace(r'\unsure{(0)|\{0\}|0}',r'\unsure{(0)|(0}')
head,tail=text.split('Structure de $k$-espace projectif',1)
tail='\\diagram{'+tail.split('\\diagram{',1)[1]
text=head+'Structure de $k$-espace projectif'+new+tail
(root/'decisions/scan014_final.tex').write_text(text)

inventory=copy.deepcopy(rep['R2']['inventory'])
inventory.insert(2,copy.deepcopy(rep['R3']['inventory'][1]))
for x in inventory:
    e=x.get('element','')
    if e=='circumscribed projective marginal note':x['first_words_or_objects']='P(V) ≃ V/k*; GP(V) opere/opère dessus'
    if e=='vector structure and datum':x['first_words_or_objects']='Structure de k-vectoriel sur ens V ↔ donnée d’un/une élemt/élémt/élement/élément'
    if e=='affine Isom quotient and datum':x['first_words_or_objects']='↔ donnée d’un élémt/élément de; Isom_ens(k^n,V)/Aff n,k), opening-parenthesis alternative'
    if e=='opening bracket and opening prose':x['first_words_or_objects']='[ De façon général/générale, ... la notion de'
    if e=='torsor live continuation':x['first_words_or_objects']='sous grpe/groupe non précisé peut être considéré comme structure sur le seul ens de base E'
    if e=='projective Isom quotient':x['first_words_or_objects']='↔ donnée de Isom with ens/ens, subscript (P^{n−1}(k),P)/GP(n−1,k)'
    if 'et'==x.get('first_words_or_objects','') or 'et cancellation' in x.get('element','').lower():
        x['first_words_or_objects']='et: canceled/live state uncertain, canceled primary'
    if 'glyph' in x.get('element','').lower() and 'P' in x.get('first_words_or_objects',''):pass
    if 'foliation' in x.get('element','').lower():x['hand']='unnamed hand'

events=copy.deepcopy(json.loads((root/'pending_events/scan014.json').read_text()))
for r,d in rep.items():
    for i,c in enumerate(d['checks'],1):
        events.append(dict(statement_id=f'R014-{r}-{i:02d}',date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan014 {r} independent reader',type='targeted proof check',outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']))
u=[
('First decorative S','Fraktur S','calligraphic S; later occurrences use primary','medium'),
('First decorative A','Fraktur A','calligraphic A; later occurrences use primary','medium'),
('Sequence comment','splitte','compressed ending prevents fuller certainty','medium'),
('Marginal verb','opere','opère','medium'),
('Vector datum article','un','une','medium'),
('Vector datum noun','élemt','élémt; élement; élément','low'),
('Affine datum noun','élémt','élément','medium'),
('Affine denominator','Aff n,k)','Aff(n,k)','low'),
('Bracket opening','général','générale','medium'),
('Canceled group noun','groupe','grpe','medium'),
('Canceled affine ending','affine','aff.','low'),
('Live group noun after sous','grpe','groupe','medium'),
('Canceled application words','savoir application','crossing leaves individual letters insecure','medium'),
('Canceled E-product shaft','headless dash','right arrow','low'),
('Canceled pointwise shaft','barred headless shaft','maps-to arrow','low'),
('Canceled result','6x','sx; delta x','low'),
('Applicability word','valable','compressed internal strokes','medium'),
('Canceled words after avec','Gamma com','heavily crossed initial and ending','low'),
('et after comm','canceled et','live et','low'),
('Projective prose P','plain P','double-stroked P','medium'),
('Last Isom subscript','ens','ens,','medium'),
('Zero enclosure','(0)','(0 without a secure closing small curve','low'),
('Last caption word','enveloppant','enveloppe','low'),
('Upper detached pair','two drawn points','writing versus surface traces; no punctuation assigned','low')]
notes=r'''Items c) and d) continue the small-cardinal group identifications. The author writes a question mark after A4 ≃ Aff(1,F4). The heading is Quelques groupes classiques sur un corps k. Two sequences with a common nonsplitting comment are followed by a slanted left note and descriptions of vector, affine, torsor and projective structures. The final two-row diagram links Gl, Aff and GP with three kinds of structure. No date or manuscript pagination appears; archive foliation 13 is comment-only and assigned to unnamed hand.

All three final complete returns were compared before the main inspected 28 crops, 22 reused and six newly made only for missing loci or geometry. All 14 original C doubts were explicitly reviewed: the marginal doubled P and canceled E resolve; twelve remain, some with revised candidates. Twelve new uncertainty loci are retained. The first Aff lacks an opening parenthesis, while retaining its close; the later affine denominator has an explicit missing/present-opening doubt. The two sequence strokes are headless. Raised replacements, the dimension insertion and its curled lead, the open marginal oval, the open-top déf enclosure and downward arrow, three written closing square brackets after one opener, the vertical source annotation and its stepped divider are preserved. A separate upper point pair is drawn with uncertain writing/surface status. H's declared bold/double-stroke encodings, equivalent operator/emphasis macros, and confidence-only agreements are not counted as collation differences. Ordinary prose wraps are joined; the two correspondence continuations retain their meaningful right-side display placement.

SA01-K75-02 is confirmed from ink: the affine prose names E, but Isom_ens(k^n,V) has target V. No E is substituted. Under the standard interpretation, the projective prose's dimension n also disagrees with its model P^{n−1}(k), and the marginal V/k* includes a zero orbit. These issues prompted careful visual attention but do not authorize corrections of the manuscript. The smaller zero enclosure below the projective source remains doubtful, and the large opening parenthesis remains unmatched.

Actual checks are recorded separately in CHECK_EVENTS.tsv and decisions/scan014_math_work.md. The small-group identifications are supported by explicit actions: Aff(2,F2) and PGL2(F3) give S4; Aff(1,F4) acts by twelve even permutations on four points, giving A4; PGL2(F4) gives A5. PGL2(F5) has 120 elements and acts faithfully by conjugation on the five Klein-four subgroups of its determinant-square subgroup, giving S5. The finite certificate checks the complete permutation image and all 14,400 products for that action. Thus the S5 formula is not refuted by this run; the earlier C context's possible-slip suggestion does not stand. The author's question mark after the A4 identity nevertheless remains ink. The shared non-splitting claim has a concrete example in GL2(F3): a projective involution represented by a matrix whose square is −I has no order-two lift.

Transport of operations proves the vector-structure orbit classification and the affine classification when the same underlying set occurs on both sides. The mixed E/V formulation fails, for example with k=F2, n=2, V=F2² and E a two-point set: the displayed orbit set has one member whereas E admits no two-dimensional affine structure. This is M014-AFF-MIXED, refined to M014-AFF-STRUCT. The marginal all-V quotient fails because zero supplies an extra orbit; M014-PROJ-NONZERO removes zero. The projective model in the displayed quotient has dimension n−1 under the usual convention, not n: for F2 and n=2, it has three points rather than the seven of a projective plane (M014-PROJ-DIM, refined M014-PROJ-MODEL).

The torsor discussion is checked for nonempty regular actions, with the opposite-group convention required for a right action: right translations compose in reverse order. A faithful action is determined by its image subgroup; a regular abelian subgroup together with a unital map k→End_Z(Γ) supplies the affine k-torsor structure, with a separate dimension condition when n is prescribed. Finally the block matrices [A b; 0 1] verify Aff_n→PGL_{n+1} and the displayed forgetting-origin/projective-completion chain. The finite enumeration certificate performs 32,976 product checks in total. R1's separate order calculations are recorded as order checks, not proofs of isomorphism; R2's E/V check and R1's zero-orbit check are also recorded at their actual scope.'''
dec=dict(base='R2',text_file='decisions/scan014_final.tex',findings=fs,inventory=inventory,notes=notes,events=events,unresolved=[dict(place=a,reading=b,alternatives=c,confidence=d) for a,b,c,d in u],abbreviations=copy.deepcopy(rep['R2']['abbreviations'])+[{'written':'élemt / élémt','expansion':'élément'},{'written':'grpe','expansion':'groupe'}],main_crop_count=6,main_crop_views=obs['views'])
(root/'decisions/scan014.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
coverage=json.loads((root/'decisions/scan014_C_doubt_coverage.json').read_text())
for i,d in enumerate(coverage['doubts'],1):
    k=f'C{i:02d}';f=by[k];d.update(c_doubt_id=k,disposition=f['doubt_action'],findings=[f'S014-{fs.index(f)+1:03d}'],final=f['final'],crop=f['crop'])
(root/'decisions/scan014_C_doubt_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
pp=root/'decisions/scan014_witness_comparison_pending.json';d=json.loads(pp.read_text());d.update(status='Complete; initial questions retained for audit',main_status='All final complete returns compared before main image review; all reader/witness disagreements, every C doubt and the S row inspected. No pending locus.');pp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(root/'decisions/scan014_review_state.json').write_text(json.dumps(dict(scan=14,status='Adjudication complete, ready for commit',all_three_final_returns_fully_read_and_compared=True,main_crops_created=6,main_views=28,C_resolved=2,C_retained=12),indent=2)+'\n')
assert text.count('\\unsure{')==len(u),(text.count('\\unsure{'),len(u))
assert all(x in obs['views'] for f in fs for x in f['crop'].split('; '))
print(dict(findings=len(fs),inventory=len(inventory),events=len(events),doubts=len(u),views=len(obs['views'])))
