"""Main reader's crop-based adjudication of scan 008. Refuses committed-page edits."""
import json,copy
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan008.json'
if p.exists() and json.loads(p.read_text()).get('committed'):raise SystemExit('Already committed')
rs=[json.loads((O/f'readers/scan008/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
map1=[3,0,1,2,7,8,4,5,6,11,11,11,12,12,14,13,13,16,17,18,19,20,24,21,22,23,9,10]
map2=[None,0,1,2,6,7,3,4,5,10,10,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,8,9]
rows=[]
for i,x in enumerate(c):
 r=copy.deepcopy(x);r['final']=r.pop('reading');r['id']=f'008-{i+1:02}'
 r['readers']={'R1':a[map1[i]]['reading'],'R2':b[map2[i]]['reading'] if map2[i] is not None else '(1.10). (complete reading)','R3':x['reading']}
 r['mathematical']=False;rows.append(r)
def put(i,**kw):rows[i].update(kw)
def r3(name):return 'readers/scan008/R3/crops/'+name+'.jpg'
put(0,crop='crops/scan008/main/01_label_period.jpg',evidence='Main crop shows a distinct low dark point after the closing parenthesis. The numbered label is (1.10)., including that terminal point.',confidence='high')
put(1,crop='readers/scan008/R1/01_third_relation.jpg',evidence='Main crop shows a curved upper cusp and a distinctly curved separate lower rule. This resolves the straight-underbar alternative in C; the sign is preccurlyeq.',confidence='high',mathematical='The third relation is the curved subdivision-order sign, distinct from ≤ and ≪.')
put(2,final=r'\unsure{de|dans}',against_C=True,against_H=True,crop='readers/scan008/R2/crops/01_order_descriptor.jpg',confidence='low',evidence='Main crop shows a looped d followed by one low rise and a long flattened exit. De is the first candidate, but separate a/n strokes cannot be established or excluded. R3 resolves dans; R1 and R2 retain both in opposite priority. The ink does not justify removing the uncertainty.')
put(3,crop='readers/scan008/R2/crops/01_order_descriptor.jpg',evidence='Main sees a long left-extending top arm, upright, middle arm and returned foot: F is secure. The drawn alphabet does not uniquely select calligraphic versus fraktur, so the existing alphabet doubt is retained at this occurrence.',confidence='medium')
put(4,crop='readers/scan008/R2/crops/02_upper_margin.jpg',confidence='medium',evidence='Main crop shows a tall initial stroke with a broad foot; this favors capital L but does not exclude the writer’s tall lowercase l. R1 reads les, R2 puts les first, and R3 puts Les first. Both cases remain explicit.')
put(5,final='discrètes.',against_C=True,against_H=False,crop='readers/scan008/R2/crops/02_upper_margin.jpg',confidence='medium',evidence='Main sees a separate dark point after discrètes in terminal position along the rotated line. R2 includes it and H includes it; R1 and R3 omit it. It is preserved as a period, rather than being assigned to the next marginal inscription.')
put(6,crop=r3('02_bracket_nb'),evidence='Main crop resolves a low n-like course followed by a small b with an ascender and low bowl. This is lowercase nb, not the uppercase marginal NB and not H’s et.',confidence='high')
put(7,crop='crops/scan008/main/02_specifique_dans.jpg',evidence='Main crop resolves the sp beginning, tall looped f, dotted i and descending q with final ue. The word spécifique is legible; H’s lexical doubt is removed.',confidence='high')
put(8,crop='crops/scan008/main/02_specifique_dans.jpg',evidence='Main crop shows the looped d followed by a compressed low ans course before M. The word is dans; H leaves this readable word as ill.',confidence='high')
put(9,crop=r3('05_first_formula'),evidence='Main sees the former upright and two arms of F inside the live rounded G. Both physical states are retained; H supplies only the live G.',confidence='high')
put(10,crop=r3('05_first_formula'),evidence='Main sees two nested angular vertices behind the live ≤, favoring an earlier ≪. Overlap and retracing still permit a single <. The final keeps both, with ≪ first; H omits the earlier comparison.',confidence='low',against_C=True,mathematical='The live comparison is ≤; the uncertain earlier comparison is a manuscript revision and is not substituted for it.')
put(11,crop=r3('05_first_formula'),evidence='Main sees a curved older G around and beneath the live upright and two dark arms of F. H omits the older operand.',confidence='high')
put(12,crop=r3('06_first_prose_G'),evidence='Main crop shows a straight old F stem and arms within the later G bowl and terminal. The prose subject repeats the physical replacement F by G.',confidence='high')
put(13,crop=r3('07_first_prose_F'),evidence='Main sees the old enclosing G curve and low return beneath the live two-armed F at the end of the definition. H records only F.',confidence='high')
put(14,crop=r3('08_first_parenthesis'),evidence='Main sees a high upper curve and a large lower return making capital S before the dotted i. This first parenthesis starts Si; H’s lowercase si is rejected.',confidence='high')
put(15,crop=r3('08_first_parenthesis'),evidence='Main crop shows the old F stem and arms within the baseline G. Only =X is above the line, with a leader anchored after G. H misidentifies the old letter as G and extends the insertion to a second G. C’s exact placement is retained.',confidence='high',mathematical='The insertion is =X after the existing corrected G; it does not introduce another G.')
put(16,crop=r3('09_first_parenthesis_F'),evidence='Main crop shows the former G’s curved upper and lower right strokes behind the live F. The canceled G remains explicit.',confidence='high')
put(17,crop='readers/scan008/R2/crops/08_refinement_X.jpg',evidence='Main sees crossed strokes smaller than G and M, including a curved starting stroke. Lowercase x is favored but a small X cannot be excluded. The distinct inserted X in the preceding parenthesis does not settle this occurrence.',confidence='medium')
put(18,crop=r3('11_element'),evidence='Main sees the accented initial e, high l, another small accent and intervening low strokes before terminal t. Those strokes support the full élément rather than élt.',confidence='medium')
put(19,final=r'o\unsure{m|\deleted{o}m|\deleted{m}m}bre',crop=r3('12_ombre'),evidence='Main sees an enclosed oval and doubled low course and exits within the m region, without a separable cancellation stroke. A retraced live m remains first; an overwritten old o or m remains possible. The final qualifies the physical state rather than asserting C’s definite cancellation or H’s unqualified ombre. R1 excludes old m; R2/R3 retain it, and the doubling does not resolve that alternative.',confidence='low')
put(20,final=r'deu\deleted{\unsure{q|x}}x',crop=r3('13_deux'),evidence='Main sees a small enclosed loop and downward right stem immediately before a separate clear live x, favoring old q over x. The connected deu course is retraced but lacks a separate crossing strike; a whole-word cancellation is not established, and the final x remains live. Thus R2’s local correction is preferred to R3’s broader state alternatives and H’s deletion of the entire word; the old glyph remains doubtful.',confidence='low')
put(21,crop=r3('14_deleted_dans'),evidence='Main sees a clear initial looped d and terminal s-like return with compressed middle ink beneath a long independent strike. These support deleted dans, resolving C’s doubt.',confidence='medium')
put(22,crop='crops/scan008/main/03_sous_figures.jpg',evidence='Main sees a white interval between the final course of sous and the tall f of figures. No hyphen is present in that interval. H’s sous-figures is normalized spelling; the literal sous figures is retained.',confidence='high')
put(23,crop=r3('15_barred_m'),evidence='Main sees a separate straight bar above a lower trough and internal rise. The lower component is letter-shaped, not a second equality bar. Barred m is retained literally and not expanded to H’s même.',confidence='high')
put(24,crop=r3('16_ie'),evidence='Main sees one clear low point after dotted i and a second small smeared mark before the final e. The second mark may be a separate point or part of the following letter course. R1 resolves i..e; R2/R3 retain both. The final keeps i..e|i.e and supplies no terminal point, since the following space is clear.',confidence='medium')
put(25,crop=r3('17_disjoint'),evidence='Main sees a tall final t followed directly by the colon. No final s follows it. The literal singular disjoint is preserved despite the plural subject and the separate plural occurrence in (1.12).',confidence='high')
put(26,final='G',against_C=True,against_H=False,crop='readers/scan008/R2/crops/03_lower_margin.jpg',evidence='Main sees an open rounded capital with flat basal return and short downward hook, matching the second G in this same formula. This visible terminal form favors G over C. R3 retains G/C; R1/R2 resolve G, which the main adopts with medium confidence.',confidence='medium')
put(27,final=r'G\ll F : une',against_C=True,against_H=False,crop='readers/scan008/R2/crops/03_lower_margin.jpg',evidence='Main sees two distinct vertically separated dark points after the final F of the implication. They form a colon. R1 reports one point and R3 none; R2 and H preserve the two-point punctuation.',confidence='high')
for idx in [9,11,12,13,16]:
 for who in ['R1','R2']:rows[idx]['readers'][who]=rows[idx]['final']
rows[10]['readers'].update(R1=r'\deleted{\unsure{<|\ll}}\leq',R2=r'\deleted{\unsure{<|\ll}}\leq')
rows[15]['readers']['R1']=r'\deleted{F}G\inserted{=X}'
tex=(O/'readers/scan008/R2/reading.tex').read_text().replace(r'\unsure{les|Les}',r'\unsure{Les|les}').replace(r'\deleted{\unsure{<|\ll}}',r'\deleted{\unsure{\ll|<}}')
(O/'decisions/scan008_final.tex').write_text(tex)
adj=[{'place':'Second parenthesis, initial si','readers':{'R1':'Si','R2':'si','R3':'si'},'final':'si','evidence':'Main crop shows a small triangular/looped s at baseline followed by dotted i; it is much shorter than the large capital S of the first parenthesis. R1’s capital reading is rejected. Both witnesses’ lowercase is retained.','crop':'readers/scan008/R2/crops/08_refinement_X.jpg'}]
cd=copy.deepcopy(rs[2]['c_doubts']);links=[1,6,26,10,17,18,19,20,21,23,24,25]
for j,idx in enumerate(links):
 rr=rows[idx];cd[j].update(reading=rr['final'].removesuffix(r'\leq') if idx==10 else rr['final'],evidence=rr['evidence'],crop=rr['crop'],disposition='retained' if idx in [10,17,19,20,24] else 'resolved')
inv=copy.deepcopy(rs[0]['inventory'])
inv[1]['first_words_or_objects']=r'(1.10). ≤, ≪, \preccurlyeq; relations d’ordre; de/dans family F (alphabet uncertain)'
inv[4]['first_words_or_objects']='NB Les/les relations d’ordre induites par ≤, ≪ sur L sont discrètes.'
inv[6]['first_words_or_objects']='NB G≤F ⇒ G≪F : une sous-figure de F raffine F'
inv[9]['first_words_or_objects']='≪ or < replaced by ≤'
inv[20]['first_words_or_objects']='(si G=x/X in M, c’est donc un élément de la grande ombre de F)'
inv[21]['first_words_or_objects']='Retraced m, or old o/m overwritten by m; physical state uncertain'
inv[26]['first_words_or_objects']='Old q/x locally canceled before a separate clear live x'
inv[30]['first_words_or_objects']='F et G compatibles: ce sont des sous figures d’une barred-m figure, i..e/i.e {F,G} majoré pour ≤;'
notes={'content':'The page names three order relations on the family of figures and emphasizes the first two induced on M. A bracketed nb describes the third induced order as less important as a specific structure on M. The two oblique NB notes assert that the first two induced orders on L are discrete and that G ≤ F implies G ≪ F. Three aligned entries define sous-figure, raffinement and subdivision. A subfigure X belonging to M is called a strate; the corresponding member for refinement lies in the grande ombre of F. The final section introduces compatibility and disjointness; compatibility is expressed as {F,G} being bounded above for ≤. The disjointness sentence continues off this page after “et leur”.',
'math_reading_decisions':['The third comparison has a curved lower rule and is rendered preccurlyeq. This visual identification does not verify the order axioms.','The live first formula is G ≤ F; its overwritten F/G operands and earlier ambiguous comparison remain explicit.','Only =X is inserted above the first parenthesis. The small x/X in the next parenthesis remains uncertain.','The barred verbal m, singular disjoint and unhyphenated sous figures are preserved literally. No mathematical or grammatical normalization was applied.','The central material is a definition list rather than a diagram; ordinary tabular layout records it without adding an arrow graph.','No proof, targeted mathematical verification or computation was performed on this page.'],
'author_doubts':['No explicit authorial request to verify, question or expression of doubt occurs.','“[nb la relation d’ordre … est moins importante, comme structure spécifique dans M].” is an authorial qualification, not a proof or checking instruction.','The two “NB” notes call attention to assertions.'],
'titles_dates_counts':'Manuscript page 7, scan 008; labels (1.10)., (1.11), (1.12). No title, date or archive pencil number observed by the readers. Two slanted marginal notes, one bracketed nb comment, three definition entries, one =X insertion with leader, seven overwritten operand/comparison positions, two further correction regions and canceled dans. No diagram or drawing.'}
events=[]
for i,r in enumerate(rs,1):
 for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan008 R{i}'))
for e in rs[2]['check_events']:events.append(dict(e,who='GPT-6 Astra Pro; effort not exposed; main reader; scan008'))
un=[{'place':rows[i]['place'],'reading':rows[i]['final'],'alternatives':'Alternatives and physical-state uncertainty are explicit in the reading.','confidence':rows[i]['confidence'],'evidence':rows[i]['evidence']} for i in [2,3,4,10,17,19,20,24]]
d={'scan':8,'mspage':'7','folder':'J156-6-01','filename':'J156-6-01_156-6_scan008.tex','brief':'v002','committed':False,'adjudicated_all':True,'differences':rows,'adjudications':adj,'c_doubts':cd,'s_rows':[],'inventory':inv,'notes':notes,'check_events':events,'unresolved':un,'abbreviations':rs[1]['abbreviations']}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Prepared scan008: 28 loci, 1 additional reader adjudication, 12 C doubts (7 resolved, 5 retained), 8 remaining doubts, 32 inventory elements.')
