"""Main reader's explicit scan-007 adjudication; refuses to alter a committed page."""
import json,copy
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan007.json'
if p.exists() and json.loads(p.read_text()).get('committed'): raise SystemExit('Page already committed')
rs=[json.loads((O/f'readers/scan007/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
rows=[]
maps2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,None,None]
maps3=[1,2,3,4,5,5,6,7,8,9,10,11,12,13,14,15,18,19,20,0,17]
for i,x in enumerate(a):
 r=copy.deepcopy(x);r['final']=r.pop('reading');r['id']=f'007-{i+1:02}'
 r['readers']={'R1':x['reading'],'R2':b[maps2[i]]['reading'] if maps2[i] is not None else x['reading']+' (in complete reading; no separate report row)','R3':c[maps3[i]]['reading']}
 r['mathematical']=False
 rows.append(r)
def setrow(i,**kw): rows[i].update(kw)
setrow(0,crop='crops/scan007/01_parenthesis.jpg',evidence='Main crop: à ne is followed by the long descending p of pas and f of confondre; after the comma, avec les is readable. H’s ill/un peu/abusivement/ou tokens align to à/ne/pas/confondre/avec, rather than an extra omitted phrase.',mathematical='Restores the explicit warning not to confuse the lieux of a figure with its strata that are lieux.')
setrow(1,evidence='Main inspected the doubled low runs at the beginning of multiombre. They permit an older om but do not separate it conclusively from retracing of the live initial. The final alternatives explicitly qualify the physical deletion state; all three readers recognized this uncertainty.',confidence='low')
setrow(2,evidence='Main crop shows the acute over a single flattened final run; no distinct extra e can be isolated. Formé remains first, formée possible. The feminine subject is not used to supply a letter.',confidence='medium')
setrow(3,crop='crops/scan007/02_deployement.jpg',evidence='Main crop shows a long oblique descender between plo and ement, establishing y. The manuscript spelling déployement is retained.',confidence='high')
setrow(4,evidence='Main crop shows the live first d’ followed by an older looped d and apostrophe under a strong horizontal cancellation. The following overlapped uprights and loops favor d’ordre but do not exclude d’inclu. H’s illegibility mark is replaced by these uncertain candidates.',confidence='low')
setrow(5,against_C=False,against_H=True,evidence='Main sees the live ending sion and a tall l/u-like middle but cannot isolate every initial replacement stroke from the cancellation. R2 resolves inclusion; R1 and R3 retain lexical doubt. The final keeps that doubt and marks the replacement with inserted. C’s canceled-start context and H’s add already indicate the same physical correction; the macro alone is not a separate disagreement.',confidence='medium')
setrow(6,evidence='Main crop shows a detached final open return with a long downturned ending; a plural s is plausible but compressed ce versus ces remains unresolved. All three readers retain the alternatives.',confidence='medium')
setrow(7,crop='readers/scan007/R3/14_F_after_strates.jpg',evidence='Main crop shows the dot above i, followed by e and one baseline stop after e. There is no intervening stop, so the literal abbreviation is ie.',confidence='high')
for i in [8,9]:
 setrow(i,final=r'\unsure{de|dans}',against_C=False,against_H=True,confidence='low',evidence='Main crop shows a clear looped d followed by a long flattened shallow return. De is the first candidate, as R1 reads it, but the compressed tail does not securely distinguish e from ans. R2 and R3 retain both; the final does likewise without choosing from mathematical expectation.')
setrow(10,evidence='Main crop shows an open c and its descending hooked cedilla, followed by a. The next word has the low rev sequence, dotted i and crossed terminal t of revient, with retracing in the middle. H’s se réduisant is not supported.',confidence='high')
setrow(11,evidence='Main crop shows a straight upper bar over a lower stroke with a trough and internal kink. The lower member is letter-shaped, so barred m is retained literally, not an equality sign.',confidence='high',mathematical='The mark is a verbal abbreviation, not an equation sign.')
setrow(12,crop='crops/scan007/03_negative_reconstruction.jpg',evidence='Main crop shows two separate short words ne se and a verb ending in tue, without the able ending in H. The literal clause is ne se réconstitue.',confidence='high')
setrow(13,crop='readers/scan007/R3/13_reconstitue_start.jpg',evidence='The main crop shows the accented ré prefix with doubled loops, followed by the clear constitue ending. R2 marks the prefix doubtful because of its physical state; R1 and R3 read it. The live prefix is legible, and no independent older word or cancellation can be separated, so no deletion is invented and réconstitue is retained.',confidence='medium')
setrow(14,crop='crops/scan007/04_pourtant.jpg',evidence='Main crop resolves the long p, following ou/r, crossed medial t and terminal nt as pourtant. Local retracing does not establish another word.',confidence='high')
setrow(15,place='Line 17, overwritten initial beneath souvent',c=r'\deleted{\unsure{à}}',h=r'\struck{donc}',final=r'\deleted{\unsure{à|d}}',kind='deletion state',marked_in_H='no',confidence='low',evidence='Main crop shows a closed low loop, tall upright and a separate oblique upper stroke at the overwritten initial. These allow à or d; the old letters onc required by H’s donc cannot be recovered. R2 prefers d; the other readers prefer à. Both are retained. R1 marks the live replacement s with inserted; this records the overwrite already evident in the other returns, not a separate textual addition.')
rows[15]['readers']['R1']=r'\deleted{\unsure{à|d}}\inserted{s}ouvent'
rows[15]['readers']['R2']=r'\deleted{\unsure{d|à}}souvent'
rows[15]['readers']['R3']=r'\deleted{\unsure{à|d}}souvent'
often=copy.deepcopy(b[16]);often['id']='007-22';often['final']=often.pop('reading');often['against_C']=False;often['against_H']=True;often['readers']={f'R{i}':'souvent' for i in range(1,4)};often['crop']=rows[15]['crop'];often['evidence']='Main crop shows the separate o after the overwritten initial, followed by u/v/e, n and the high final t. The live word is souvent. H’s uncertain dans occupies this token, independently of the older canceled fragment.';often['mathematical']='Restores the frequency word souvent in the reconstruction claim.'
setrow(16,final=r'\unsure{\deleted{a}A|A}teliers',evidence='Main sees an extra low loop and crossing/doubled uprights inside the capital A. An older lowercase a is possible; a retraced capital remains possible. All three readers preserve that physical-state uncertainty, with equivalent scopes of unsure. The compact final form confines it to the initial.',confidence='low')
setrow(17,evidence='Main crop separates a tall old d-like stem and a small e-loop at its lower right from the new large a bowl and grave. These support de replaced by à. R2 keeps old à as an alternative, but its reading does not account for the separate e. The final resolves old de and marks the live replacement à.',confidence='medium')
setrow(18,final=r'\S{}',evidence='Main crop shows joined upper and lower returns, a central enclosure and a long lower exit. These support § rather than a simple S. The crosswise segment belongs to the sign itself; no independent strike-through is present. R2’s S alternative is rejected; H’s cancellation is rejected.',confidence='high')
setrow(19,crop='crops/scan007/05_open_quote_figure.jpg',evidence='Main inspected both the opening pair (this crop) and the closing pair in crops/scan007/06_close_quote_figure.jpg. They are short upper strokes, not chevrons. The single underline is shared by both witnesses and is not collated as a separate difference.',confidence='high')
setrow(20,evidence='Main inspected the two upper strokes before A in this crop and the closing pair in crops/scan007/07_close_quote_ateliers.jpg. Both are ordinary paired quotation marks, not guillemets.',confidence='high')
rows.insert(16,often)
tex=(O/'readers/scan007/R1/reading.tex').read_text()
tex=tex.replace(r'ie. la relation de $\widetilde F$',r'ie. la relation \unsure{de|dans} $\widetilde F$').replace(r'$\leq$ de $\mathcal M$',r'$\leq$ \unsure{de|dans} $\mathcal M$')
tex=tex.replace(r'\unsure{\deleted{a}Ateliers|Ateliers}',r'\unsure{\deleted{a}A|A}teliers').replace(r'\S\ Il',r'\S{} Il')
(O/'decisions/scan007_final.tex').write_text(tex)
cd=copy.deepcopy(rs[0]['c_doubts'])
links=[1,2,4,5,6,8,9,10,11,14,15,16,17,18]
for j,idx in enumerate(links):
 rr=rows[idx if idx<16 else idx+1]
 cd[j].update(evidence=rr['evidence'],crop=rr['crop'])
for j in [5,6]:cd[j].update(reading=r'\unsure{de|dans}',disposition='retained')
cd[11]['reading']=r'\unsure{\deleted{a}A|A}teliers'
cd[13]['reading']=r'\S{}'
inv=copy.deepcopy(rs[0]['inventory'])
inv[9]['first_words_or_objects']='la relation d’incidences/incidence entre strates de F, ie. la relation de/dans tilde F induite par ≤ de/dans M (ou par ≪ au choix, ça revient au barred m).'
inv.insert(11,{'element':'retraced_second_reconstitue','kind':'text','position':'Line 17, initial ré','first_words_or_objects':'réconstitue; live prefix read despite retracing, no independent prior word recoverable','sheet_kind':'text','hand':'his hand','transcribed':'yes'})
notes={'content':'The shadow is described as the lieux refining a figure, with an explicit caution against confusing these with strata that are lieux. The multiombre consists of the strata’s shadows, indexed by the deployment of F. The inclusion relation in the set-theoretic figure is identified with incidence among its strata and with the induced order from M; the author says either ≤ or ≪ gives the same result. A figure is said practically never to reconstruct from its shadow, but often to reconstruct from its multiombre in the case of “Ateliers ensemblistes”. The final unfinished paragraph introduces canonical order relations.',
 'math_reading_decisions':['The two order signs and deployment tildes are distinct. The ordinary F after strates has a retraced upper arm, not a further bar or tilde.','The literal spelling déployement and unresolved formé/formée, incidence(s), and de/dans are preserved.','The barred m is transcribed literally; its explanatory expansion appears only in the abbreviation table.','The page supplies assertions rather than a proof. No proof of reconstruction or equivalence of induced relations was attempted.'],
 'author_doubts':['No explicit authorial doubt or checking request occurs.','“(ou par ≪ au choix, ça revient au [barred m])” asserts equivalence; “Nous y reviendrons.” promises later discussion. Neither is a completed verification.'],
 'titles_dates_counts':'Manuscript page 6, scan 007. No title, date, archive pencil number, display, diagram, drawing or independent marginal note. Two prose paragraphs, the second unfinished; 22 body lines reported by all three readers. One single underline across two manuscript lines. Four correction regions and one possible earlier a beneath A are represented; the om and a physical states remain uncertain.'}
events=[]
for i,r in enumerate(rs,1):
 for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan007 R{i}'))
events.extend([dict(e,who='GPT-6 Astra Pro; effort not exposed; main reader; scan007') for e in rs[0]['check_events']])
un=[]
for x in cd:
 if x['disposition']=='retained':un.append({'place':x['place'],'reading':x['reading'],'alternatives':'Alternatives and physical-state possibilities are explicit in the reading.','confidence':'medium' if x['place'] in ['Line 6, formé/formée','Line 11, incidence(s)','Line 9, live inclusion'] else 'low','evidence':x['evidence']})
d={'scan':7,'mspage':'6','folder':'J156-6-01','filename':'J156-6-01_156-6_scan007.tex','brief':'v002','committed':False,'adjudicated_all':True,'differences':rows,'adjudications':[],'c_doubts':cd,'s_rows':[],'inventory':inv,'notes':notes,'check_events':events,'unresolved':un,'abbreviations':rs[0]['abbreviations']}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Prepared scan007: 22 loci, 14 C doubts, 9 retained doubts, 21 inventory elements.')
