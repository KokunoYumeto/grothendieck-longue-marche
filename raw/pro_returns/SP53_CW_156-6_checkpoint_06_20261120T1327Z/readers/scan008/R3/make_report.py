import json
from pathlib import Path
from datetime import datetime, timezone
base=Path('/workspace/scratch/42e661864e98/out/readers/scan008/R3')
source='/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan008.jpg'
plan=json.loads((base/'crop_plan.json').read_text())
byid={c['id']:c for c in plan}
def loc(crop=None,box=None):
    if crop:
        p=byid[crop]
        return {'crop':'readers/scan008/R3/crops/'+crop+'.jpg','crop_box':p['box'],'crop_source':source}
    return {'crop':None,'crop_box':box,'crop_source':source}
diffs=[]
def diff(place,c,h,reading,aC,aH,kind,evidence,crop=None,box=None,confidence='high',marked='no',math=False):
    row={'id':f'scan008-R3-D{len(diffs)+1:02d}','place':place,'c':c,'h':h,'reading':reading,'against_C':aC,'against_H':aH,'kind':kind,'marked_in_H':marked,'confidence':confidence,'evidence':evidence,**loc(crop,box),'mathematical':math}
    diffs.append(row)
diff('(1.10), label punctuation','(1.10).','(1.10)','(1.10).',False,True,'omission','A small period is visible immediately after the closing parenthesis; settled in half_a.',box=[218,150,385,225])
diff('(1.10), third relation',r'\unsure{\preccurlyeq|\preceq}',r'\preccurlyeq',r'\preccurlyeq',True,False,'misread symbol or index','Half_a shows the upper curved angle and a separate strongly curved lower stroke, rather than a straight lower rule. The same shape recurs in the subdivision row. No crop was needed.',box=[855,148,960,235],math=True)
diff('(1.10), word before the family F','de','dans','dans',True,False,'misread word','The d is followed by an extended low connecting course with an intermediate rise and a downturned terminal, matching the drawn word dans elsewhere in this half; it is longer than de.','01_domain_phrase')
diff('(1.10), family F alphabet',r'\mathcal{F}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,'misread symbol or index','The letter F is legible, with a long sloping top arm, crossing middle arm, and curved foot. Its exact typographic alphabet is not determined by these strokes; the supplied notation candidates are retained.','01_domain_phrase',confidence='medium',math=True)
diff('Upper slanted NB note, initial word','les','Les',r'\unsure{Les|les}',True,True,'other','The initial is an unlooped upright with a broad low exit. This favors a capital L, but cursive lowercase l is not excluded.','03_upper_margin',confidence='medium')
diff('Upper slanted NB note, after discrètes','discrètes','discrètes.','discrètes',False,True,'text not on the page','The complete rotated note has no terminal punctuation after the last word.','03_upper_margin')
diff('Opening of square bracket',r'\unsure{nb|NB}','et','nb',True,True,'misread word','The first character is low and undulating; the second has a tall single stem and a small lower bowl. These are lowercase n and b, distinct from the large marginal NB.','02_bracket_nb')
diff('Bracket, spécifique','spécifique',r'\uncertain{spécifique}','spécifique',False,True,'other','The half shows the initial sp, accent-bearing é, tall f, dotted i, and descending q; the complete word is readable. This is removal of H uncertainty, not a different lexical reading.',box=[252,687,610,790],marked='yes')
diff('Bracket, word before final M','dans',r'\ill{}','dans',False,True,r'readable ink left as \ill{}','The short d and following low joined ans before the final M are readable in half_a. H leaves precisely this word blank.',box=[630,689,799,755],marked='yes')
diff('First definition formula, left operand',r'\deleted{F}G','G',r'\deleted{F}G',False,True,'deletion state','The old upright and two F arms remain inside the larger curved G, whose lower turn and right hook are distinct.','05_first_formula',math=True)
diff('First definition formula, previous comparison',r'\deleted{\unsure{<|\ll}}\leq',r'\leq',r'\deleted{\unsure{\ll|<}}\leq',True,True,'deletion state','Two angled meeting points are visible above the live separate lower rule. A prior doubled angle is favored, but overlapping retracing still allows a single earlier <. The live sign is clearly <=.','05_first_formula',confidence='low',math=True)
diff('First definition formula, right operand',r'\deleted{G}F','F',r'\deleted{G}F',False,True,'deletion state','A former rounded left/top G stroke survives around the new upright and reinforced horizontal arms of F.','05_first_formula',math=True)
diff('First definition prose, initial subject',r'\deleted{F}G','G',r'\deleted{F}G',False,True,'deletion state','An F stem and two arms remain inside the full replacement G loop and right-hand return.','06_first_prose_G',math=True)
diff('First definition prose, terminal F after de',r'\deleted{G}F','F',r'\deleted{G}F',False,True,'deletion state','The surviving outer rounded stroke and old bottom return belong to G beneath the darker F.','07_first_prose_F',math=True)
diff('First parenthesis, opening Si','Si','si','Si',False,True,'other','The S starts high beside the parenthesis and has a large upper curve and lower loop, unlike the smaller s in the second parenthesis.','08_first_parenthesis')
diff('First parenthesis, overwritten operand and inserted equality',r'\deleted{F}G\inserted{=X}',r'\struck{G}\add{G=X}',r'\deleted{F}G\inserted{=X}',False,True,'insertion or placement','The underlying straight F stem and arms are visible inside G. Only =X is written above; the long slant joins the gap before the membership sign. There is no second inserted G. H notices intervention but assigns different canceled and added content.','08_first_parenthesis',math=True)
diff('First parenthesis, terminal F after strate de',r'\deleted{G}F','F',r'\deleted{G}F',False,True,'deletion state','A thin upper/left rounded trace remains beneath the reinforced F arms and vertical.','09_first_parenthesis_F',math=True)
diff('Second parenthesis, after G=',r'\unsure{x|X}','X',r'\unsure{x|X}',False,True,'misread symbol or index','The crossed diagonals occupy distinctly less height than adjacent G and M and less height than the inserted X above the first row. Lowercase x is favored, but the same two-diagonal form does not settle case completely.','10_second_X',confidence='medium',math=True)
diff('Second parenthesis, after un',r'\unsure{élément|élt}','élément','élément',True,False,'other','After the initial accented e and high l there is another accent/low letter course, a separate reduced middle run, and a final t. The extended course supports the full word rather than élt.','11_element',confidence='medium')
diff('Second parenthesis, ombre intervention',r'o\deleted{\unsure{o|m}}mbre','ombre',r'\unsure{ombre|o\deleted{o}mbre|o\deleted{m}mbre}',True,True,'deletion state','The low m is heavily retraced and contains a small internal oval. There is no independently separable cancellation stroke. Live retracing is the first candidate; an overwritten o or m remains possible. No earlier character is asserted as certain.','12_ombre',confidence='low')
diff('Je note enfin, deux intervention',r'deu\deleted{\unsure{x}}x',r'\struck{deux}',r'\unsure{deu\deleted{x}x|deux|\deleted{deux}}',True,True,'deletion state','The d/e/u run is doubled along its own lower contours. A small looped ending precedes a separate clear x. A local canceled x is favored; simple retracing of deux and a larger deletion remain possible. There is no clean straight strike across the full word.','13_deux',confidence='low')
diff('Before entre figures',r'\deleted{\unsure{dans}}',r'\struck{dans}',r'\deleted{dans}',True,False,'other','The long horizontal strike leaves the initial d stem and oval, low middle remnants, and the curled terminal s. The readable canceled word is dans.','14_deleted_dans',confidence='medium')
diff('Compatibility definition, sous figures','sous figures','sous-figures','sous figures',False,True,'text not on the page','The gap between sous and figures has no hyphen in half_b. This differs from the visibly hyphenated singular sous-figure in the first definition and the marginal note.',box=[1320,2100,1660,2200])
diff('Compatibility definition, abbreviation after d’une',r'\unsure{\overline m|=}','même',r'\overline m',True,True,'abbreviation expanded or spelling modernised','The lower component begins in a curved trough and rises into a short hump before its level exit; the independent upper bar is straight. It is a barred verbal m, not an equality sign. The manuscript does not spell même.','15_barred_m')
diff('Compatibility definition, before {F,G}',r'\unsure{i..e|i.e}','i.e.',r'\unsure{i..e|i.e}',False,True,'other','After the dotted i are two small low marks, the second partly smeared, before the separate e. No dot is visible after e. Two medial points are favored, but a single medial point with stray ink remains possible.','16_ie',confidence='low')
diff('Bottom line, predicate after first F et G',r'\unsure{disjoint|disjoints}','disjoints','disjoint',True,True,'abbreviation expanded or spelling modernised','The last letter has a t-like vertical/downstroke and looped cross; the next marks are the two colon dots. No separate final s is present. The singular ending is retained without grammatical repair.','17_disjoint',confidence='high')

cd=[]
def doubt(place,c,reading,disp,evidence,crop=None,box=None):
    cd.append({'place':place,'c':c,'reading':reading,'disposition':disp,'evidence':evidence,**loc(crop,box)})
doubt('(1.10), third comparison',r'\unsure{\preccurlyeq|\preceq}',r'\preccurlyeq','resolved','Half_a settles the visibly curved separate lower stroke; the subdivision row repeats it.',box=[855,148,960,235])
doubt('Opening of square bracket',r'\unsure{nb|NB}','nb','resolved','Low first letter plus tall-stemmed small b; the marginal uppercase NB is visibly different.','02_bracket_nb')
doubt('Lower left margin, first operand',r'\unsure{G|C}',r'\unsure{G|C}','retained','The open crescent has a short downward basal exit but no decisive inward bar. The repeated same-shaped operand on the right supports consistency, not certainty of identity.','04_lower_margin')
doubt('First row formula, overwritten comparison',r'\deleted{\unsure{<|\ll}}',r'\deleted{\unsure{\ll|<}}','retained','Two overlapping angular vertices favor a former double angle, but the heavy live <= overlays the decisive junctions.','05_first_formula')
doubt('Second parenthesis, after G=',r'\unsure{x|X}',r'\unsure{x|X}','retained','Smaller height favors x; crossed-diagonal shape alone does not finally settle case.','10_second_X')
doubt('Second parenthesis, after un',r'\unsure{élément|élt}','élément','resolved','Extended post-l letter course with second accented position, reduced middle strokes, and terminal t favors the full word.','11_element')
doubt('Second parenthesis, inside ombre',r'o\deleted{\unsure{o|m}}mbre',r'\unsure{ombre|o\deleted{o}mbre|o\deleted{m}mbre}','retained','The small oval is within a retraced m and no distinct crossing line separates a canceled letter. Actual live/deleted state is retained as uncertain.','12_ombre')
doubt('Je note enfin deux',r'deu\deleted{\unsure{x}}x',r'\unsure{deu\deleted{x}x|deux|\deleted{deux}}','retained','A separate clear x follows a small looped dark ending; the rest of deu has retraced contours. The first candidate is a local canceled x, with deletion extent left uncertain.','13_deux')
doubt('Before entre figures',r'\deleted{\unsure{dans}}',r'\deleted{dans}','resolved','Initial d and final s remain legible beneath the long strike; residual middle ink agrees with dans.','14_deleted_dans')
doubt('Compatibility definition, after d’une',r'\unsure{\overline m|=}',r'\overline m','resolved','A curved lower trough/hump distinguishes the abbreviated letter from a second straight equality bar.','15_barred_m')
doubt('Compatibility definition, before {F,G}',r'\unsure{i..e|i.e}',r'\unsure{i..e|i.e}','retained','Two small marks between i and e are visible, but one is partly smeared; no final point after e.','16_ie')
doubt('Bottom line, after first F et G',r'\unsure{disjoint|disjoints}','disjoint','resolved','A final t is immediately followed by the colon; no additional s.','17_disjoint')

# Add two distinct lower-margin witness differences after the core line-by-line entries.
diff('Lower slanted NB note, first operand',r'\unsure{G|C}','G',r'\unsure{G|C}',False,True,'misread symbol or index','The open rounded operand with a low hooked exit admits both G and C. It is not silently resolved by the expected F/G pairing. Later occurrences use the first candidate under the recurrence convention.','04_lower_margin',confidence='medium',math=True)
diff('Lower slanted NB note, after implication formula',r'G\ll F\quad une',r'G\ll F: une',r'G\ll F\quad une',False,True,'text not on the page','The full rotated marginal note shows no colon between the implication and the prose that continues on the next line.','04_lower_margin')

inventory=[]
def inv(element,kind,position,first):
    inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('Author page number','text','top center, y 40–100','7')
inv('Three order-relation display and label','display','upper body, y 150–285',r'(1.10). <=, <<, \preccurlyeq; relations d’ordre dans F')
inv('Transition to induced relations','text','y 300–355','et les relations induites dans M')
inv('Induced-relations display and label','display','y 380–465','(1.11) <=, << dans M')
inv('Upper slanted NB note','margin note','left margin, y 475–1010','NB Les/les relations d’ordre induites par <=, << sur L sont discrètes')
inv('Bracketed comment on the third relation','text','body, y 505–790','[nb la relation d’ordre ... est moins importante, comme structure spécifique dans M].')
inv('First definition formula','display','left definition column, y 780–875','G <= F, with overwritten operands and comparison')
inv('Overwritten first operand of first formula','deletion','x 515–565, y 795–860','F overwritten by G')
inv('Overwritten comparison in first formula','deletion','x 570–620, y 805–860','earlier << or < beneath <=')
inv('Overwritten right operand of first formula','deletion','x 628–680, y 795–865','G overwritten by F')
inv('First definition prose','text','right definition column, y 775–920','G est dit une sous-figure de F; sous and figure separately underlined')
inv('Overwritten subject in first definition prose','deletion','x 840–900, y 780–850','F overwritten by G')
inv('Overwritten terminal variable in first definition prose','deletion','x 1560–1635, y 850–920','G overwritten by F')
inv('Lower slanted NB note','margin note','left margin, y 850–1530','NB G/C <= F implies G << F; une sous-figure de F raffine F')
inv('Equality inserted into first parenthesis','insertion','x 922–1005, y 855–920','=X above line, leader to after G')
inv('First definition parenthesis','text','right column, y 905–985','(Si G=X in M, c’est donc une strate de F); strate underlined')
inv('Overwritten subject in first parenthesis','deletion','x 895–944, y 910–980','F overwritten by G')
inv('Overwritten terminal variable in first parenthesis','deletion','x 1603–1652, y 911–972','G overwritten by F')
inv('Second definition formula','display','left column, y 1010–1070','G << F')
inv('Second definition prose','text','right column, y 990–1070','G est dit un raffinement de F; raffinement underlined')
inv('Second definition parenthesis','text','right column, y 1085–1240','(si G=x/X in M, c’est donc un élément de la grande ombre de F)')
inv('Retraced or canceled letter in ombre','deletion','x 1380–1440, y 1180–1210','m with possible underlying o or m; cancellation state explicitly uncertain')
inv('Third definition formula','display','left column, y 1270–1340',r'G \preccurlyeq F')
inv('Third definition prose','text','right column, y 1260–1510','G est dit une subdivision de F, on dit que la figure G subdivise la figure F.; subdivision underlined')
inv('Introduction of the two other relations','text','body, y 1535–1770','Je note enfin deux autres relations importantes ... entre figures:')
inv('Possible cancellation in deux','deletion','x 790–960, y 1555–1605','deu[deleted x]x, with retracing/full-deletion alternatives')
inv('Canceled word before entre','deletion','x 730–890, y 1680–1740','dans')
inv('Two relations under a left brace, with label','display','body, y 1780–1950','(1.12) F et G compatibles; F et G disjoints; both predicates underlined; comma at right')
inv('Claim that both relations can be expressed via <=','text','body, y 1940–2130','qui l’une et l’autre peuvent s’exprimer en termes de la relation d’ordre <=:')
inv('Compatibility definition','text','body, y 2115–2280','F et G compatibles: ce sont des sous figures d’une barred-m figure, i..e/i.e {F,G} majoré pour <=;')
inv('Beginning of disjointness definition','text','bottom line, y 2260–2345','F et G disjoint: F et G compatibles, et leur')

viewlog=[
 {'image':source,'role':'whole','viewed_utc':'2026-11-20 09:41:04 UTC'},
 {'image':source.replace('.jpg','_a.jpg'),'role':'half_a','viewed_utc':'2026-11-20 09:41:08 UTC'},
 {'image':source.replace('.jpg','_b.jpg'),'role':'half_b','viewed_utc':'2026-11-20 09:41:30 UTC'}]
ctimes={'01_domain_phrase':'09:42:42','02_bracket_nb':'09:42:42','03_upper_margin':'09:42:43','04_lower_margin':'09:43:11','05_first_formula':'09:43:11','06_first_prose_G':'09:43:11','07_first_prose_F':'09:43:11','08_first_parenthesis':'09:43:39','09_first_parenthesis_F':'09:43:40','10_second_X':'09:43:40','11_element':'09:43:40','12_ombre':'09:43:40','13_deux':'09:44:26','14_deleted_dans':'09:44:26','15_barred_m':'09:44:26','16_ie':'09:44:26','17_disjoint':'09:44:26'}
for p in plan:
    viewlog.append({'image':p['path'],'role':'crop','viewed_utc':'2026-11-20 '+ctimes[p['id']]+' UTC'})

unresolved=[
 {'place':'(1.10), family F alphabet','reading':r'\mathcal{F}','alternatives':[r'\mathfrak{F}'],'confidence':'medium','evidence':'F identity clear, exact font underdetermined; crop 01.'},
 {'place':'Upper marginal note, initial Les/les','reading':'Les','alternatives':['les'],'confidence':'medium','evidence':'Unlooped initial favors capital L; cursive l remains possible; crop 03.'},
 {'place':'Lower marginal note, first operand','reading':'G','alternatives':['C'],'confidence':'medium','evidence':'Open crescent and basal hook without a decisive inward bar; crop 04.'},
 {'place':'Earlier comparison beneath first <=','reading':r'\deleted{\ll}','alternatives':[r'\deleted{<}'],'confidence':'low','evidence':'Two angular junctions favored, overlain by heavy live sign; crop 05.'},
 {'place':'Second parenthesis, x/X','reading':'x','alternatives':['X'],'confidence':'medium','evidence':'Smaller letter height favors x; crossed diagonal form does not eliminate X; crop 10.'},
 {'place':'ombre, live/deleted state','reading':'ombre','alternatives':[r'o\deleted{o}mbre',r'o\deleted{m}mbre'],'confidence':'low','evidence':'Low m has retraced plateau and small oval but no independent strike; crop 12.'},
 {'place':'deux, content and extent of intervention','reading':r'deu\deleted{x}x','alternatives':['deux',r'\deleted{deux}'],'confidence':'low','evidence':'A small dark ending precedes clear separate x; doubled deu contours could be retracing; crop 13.'},
 {'place':'Compatibility definition, i..e/i.e','reading':'i..e','alternatives':['i.e'],'confidence':'low','evidence':'Two medial ink marks, one smeared, and no final point after e; crop 16.'}
]
notes={
 'content':[
  'The page enumerates three order relations on the family of figures, and the two induced relations <= and << on M. It says in a bracket that the third induced relation is less important as a specific structure on M.',
  'The three-row list names G<=F a sous-figure relation, G<<F a raffinement relation, and the curved third relation a subdivision relation. The first parenthesis identifies a sub-figure belonging to M as a strate; the second places the corresponding element in the grande ombre.',
  'The upper marginal NB says the induced <= and << relations on L are discrete. The lower NB says G<=F implies G<<F and states that a sous-figure de F raffine F.',
  'The last section introduces compatible and disjoint figures. Compatibility is expressed as {F,G} being bounded above for <=. The disjointness definition begins but ends mid-sentence at et leur on this page.',
  'No drawing or arrow-graph is present. The central material is a two-column definition list. C’s diagram macro is a layout representation, not evidence of a manuscript diagram.'
 ],
 'math_reading_decisions':[
  'The third relation is rendered preccurlyeq because of its curved lower stroke, without replacing it by <=.',
  'The live first formula is G<=F; its former operand shapes and ambiguous canceled comparison are preserved separately.',
  'The inserted text in the first parenthesis is exactly =X. H’s inserted G is not present as an additional character.',
  'The second parenthesis keeps x|X, with x first from relative size; no uppercase X is supplied to enforce mathematical consistency.',
  'The barred m is kept as written, and final disjoint is kept without supplying plural s.',
  'No mathematical claim is proved or refuted in this reading; visual glyph decisions are not classified as proof checks.'
 ],
 'author_doubts':[
  'No explicit authorial question, vérifier, à voir, or other doubt/check command was found.',
  'The bracketed qualification reads: "[nb la relation d’ordre ... induite dans M est moins importante, comme structure spécifique dans M]." It is an authorial qualification, not a request for verification.',
  'The two authorial attention markers are "NB"; they introduce assertions rather than doubts.'
 ],
 'titles_dates_counts':[
  'Author manuscript page number: 7. Scan number: 8. No title or date is inked.',
  'Three numbered labels occur: (1.10)., (1.11), (1.12).',
  'Two slanted marginal NB notes; three definition rows; one inserted =X; no independent drawing; no archive pencil number observed.',
  'Exactly 17 actual enhanced crops were created and each was emitted through view_image once. One whole and the two supplied halves were each emitted once.'
 ]
}
checks=[]
for sid in ['scan008-order-relations','scan008-discreteness-note','scan008-subfigure-refines-note','scan008-three-definitions','scan008-expression-via-order','scan008-compatibility-definition','scan008-incomplete-disjointness-definition']:
    checks.append({'statement_id':sid,'type':'carried as background without fault found','outcome':"read as the author's assertion; no mathematical verification performed"})
notation=[
 {'sign':'third comparison relation','latex':r'\preccurlyeq','ink':'(1.10), bracket, and subdivision row use a curved upper angle and independently curved lower stroke.','alternatives':[r'\preceq rejected for this occurrence: lower rule visibly curved']},
 {'sign':'family F','latex':r'\unsure{\mathcal{F}|\mathfrak{F}}','ink':'Top domain letter has long top arm, central crossbar, and curved lower end.','alternatives':[r'\mathfrak{F}']},
 {'sign':'collection M and L','latex':r'\mathcal{M}, \mathcal{L}','ink':'M repeatedly has two high uprights and a deep central trough; slanted-note L has a tall upper stroke and spreading foot.','alternatives':[]},
 {'sign':'open G','latex':r'\unsure{G|C} at first ambiguous occurrence; G later','ink':'Marginal operands and later ordinary G can be open crescents with a basal hook and no strong interior bar.','alternatives':['C']},
 {'sign':'barred verbal m','latex':r'\overline m','ink':'Near the bottom, a straight upper bar stands above a curved trough/hump and low exit.','alternatives':['= rejected: lower component is not straight']},
 {'sign':'small crossed letter in second parenthesis','latex':r'\unsure{x|X}','ink':'Two diagonals smaller than neighboring G and M; first inserted X is taller.','alternatives':['X']}
]
report={
 'scan':8,'reader':'R3','started_utc':'2026-11-20 09:40:59 UTC','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'status':'complete','actual_crop_count':17,
 'view_log':viewlog,'differences':diffs,'c_doubts':cd,'s_rows':[],'inventory':inventory,'notes':notes,'check_events':checks,'notation_proposals':notation,
 'abbreviations':[{'form':'NB','expansion':'nota bene'},{'form':'nb','expansion':'nota bene'},{'form':'i..e / i.e','expansion':'id est (punctuation retained as uncertain)'},{'form':r'\overline m','expansion':'même (probable expansion; not substituted in reading.tex)'}],
 'unresolved':unresolved,'brief_feedback':[],
 'evidence_crops':plan,
 'limitations':['No reread of a whole or half and no second crop of a locus was made. Eight ambiguities remain explicitly represented in reading.tex and the unresolved list.','Only this packet, its three specified images, and the two referenced preambles were read. No OCR, other-page image, outside transcription, other reader output, or consolidated decision was used.','No LaTeX compilation or mathematical proof verification was performed; the deliverable is the diplomatic source and visual audit.']
}
assert len(cd)==12
assert len([v for v in viewlog if v['role']=='crop'])==17
assert len(plan)==17
assert all(d['confidence'] in ['high','medium','low'] and d['marked_in_H'] in ['yes','no'] for d in diffs)
assert all(i['transcribed']=='yes' for i in inventory)
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':report['status'],'differences':len(diffs),'c_doubts':len(cd),'s_rows':0,'inventory':len(inventory),'unresolved':len(unresolved),'crops':17,'finished_utc':report['finished_utc']},ensure_ascii=False))
