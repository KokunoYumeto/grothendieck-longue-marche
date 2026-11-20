"""Root adjudication of scan032; independent returns remain untouched."""
from common import *
R=load_page(32)
T={r:(W/f'readers/032/{r}/reading.tex').read_text() for r in 'ABC'}
A=R['A']['changes'];B=R['B']['changes'];C=R['C']['changes']
text=T['B']
def repl(old,new):
 global text
 assert text.count(old)==1,(old,text.count(old))
 text=text.replace(old,new,1)
def ap(i):return f'readers/032/A/crops/{i:02}.jpg'
def bp(i):return f'readers/032/B/crops/crop{i:02}.jpg'
def cp(i):return f'readers/032/C/crops/{i:02}.jpg'
def rp(name):return 'crops/032/'+name+'.jpg'
repl('l.6, '+B[1]['reading'],'l.6, '+A[0]['reading'])
ref428=A[12]['reading']+r" ``we'd better\unsure{''|'}"
repl(B[2]['reading'],ref428)
phrase440=r"``\deleted{allows one} \unsure{to|\deleted{to}}''"
terminal440=C[3]['reading']
repl(B[6]['reading'],phrase440+terminal440)
repl(B[12]['reading'],A[5]['reading'])
repl('``'+B[14]['reading']+" don't''",C[8]['reading'])
repl('$'+B[17]['reading']+'$',C[9]['reading'])
repl(B[18]['reading'],C[16]['reading'])
nine456=r'\tikz[baseline=(nine456C.base)]{\node[inner sep=0pt] (nine456C) {9};'+C[17]['reading']+'}'
repl("``its'' \\quad l 9 ``don't''", "``its'' \\quad l "+nine456+" ``don't''")
right456=r'\tikz[overlay,x=1em,y=1ex]{\draw[line width=.4pt,line cap=round] (9,-.66)..controls(8.985,-.73)and(8.985,-.80)..(9.005,-.86);}'
repl(B[19]['reading'],right456)
repl(B[21]['reading'],C[10]['reading'])
repl(B[23]['reading'],C[11]['reading'])
low468=r'\tikz[baseline=(ref468R.base)]{\node[inner sep=0pt] (ref468R) {l.8};\fill[overlay] ([xshift=-.45em,yshift=-.15ex]ref468R.base east) circle (.06ex);}'
repl('l.8 '+C[11]['reading'],low468+' '+C[11]['reading'])
edge448=r'\fill (.05,-1.0) ellipse [x radius=.08ex,y radius=.05ex];'
edge447group=B[11]['reading'][:-2]+edge448+'}}'
repl(B[11]['reading'],edge447group)
right468=r'\hfill\tikz[baseline=0pt,x=1ex,y=1ex]{\fill (0,1.3) ellipse [x radius=.045ex,y radius=.065ex];}'
repl("\\hspace*{.8em}467 \\quad l 8 ``quasi-isomorphism'' \\quad l-1 ``its''", "\\hspace*{.8em}467 \\quad l 8 ``quasi-isomorphism'' \\quad l-1 ``its''"+right468)
leftRule=r'\draw[line width=.35pt] ([yshift=-.25ex]s32B-lefttop)--([yshift=2.3ex]s32B-lefttop |- s32B-bottom);\draw[black!35,line width=.3pt] ([yshift=2.3ex]s32B-lefttop |- s32B-bottom)--(s32B-lefttop |- s32B-bottom);\fill[black!55] (s32B-lefttop) circle (.025ex);\fill[black!80] ([yshift=-.12ex]s32B-lefttop) circle (.025ex);'
rightRule=r'\draw[line width=.35pt] ([yshift=-.25ex]s32B-righttop)--([yshift=3.6ex]s32B-righttop |- s32B-bottom);\draw[line width=.3pt,black!45] ([yshift=3.6ex]s32B-righttop |- s32B-bottom)--([yshift=2.7ex]s32B-righttop |- s32B-bottom);\draw[black!22,line width=.25pt] ([yshift=2.3ex]s32B-righttop |- s32B-bottom)..controls([xshift=.12em,yshift=1.5ex]s32B-righttop |- s32B-bottom)and([xshift=.05em,yshift=.7ex]s32B-righttop |- s32B-bottom)..([xshift=.08em]s32B-righttop |- s32B-bottom);\fill[black!60] (s32B-righttop) circle (.025ex);\fill[black!85] ([yshift=-.12ex]s32B-righttop) circle (.03ex);'
# Intermediate coordinates make the vertical shifts act on the bottom anchors.
leftRule=leftRule.replace('s32B-lefttop |- s32B-bottom','s32B-leftend')
rightRule=rightRule.replace('s32B-righttop |- s32B-bottom','s32B-rightend')
repl('\\coordinate (s32B-bottom) at (0,-1.2ex);',r'\coordinate (s32B-bottom) at (0,-4ex);\coordinate (s32B-leftend) at (s32B-lefttop |- s32B-bottom);\coordinate (s32B-rightend) at (s32B-righttop |- s32B-bottom);')
repl(B[24]['reading'],leftRule)
repl(B[25]['reading'],rightRule)
D=[]
amap=[11,0,12,13,None,1,2,3,14,4,15,16,5,6,7,17,None,8,18,19,20,9,21,10,23,24]
cmap=[12,0,None,13,None,1,2,None,None,4,5,None,6,7,8,14,15,9,16,None,18,10,19,11,20,21]
crops=[bp(1),ap(2),ap(3),rp('01_point434'),bp(8),ap(5),ap(6),ap(7),ap(7),ap(8),ap(8),rp('06_point447_far'),ap(9),ap(11),ap(12),rp('02_points452'),bp(17),cp(11),ap(14),rp('07_point456_right'),rp('03_points462'),ap(15),ap(15),ap(18),[rp('04_left_rule_top'),ap(19)],[rp('05_right_rule_top'),ap(18)]]
for j,x in enumerate(B):
 D.append(dict(id='032-'+x['id'],place=x['place'],c=x['c'],h=None,final=x['reading'],diff_c=True,diff_h=False,kind=x['kind'],marked_in_H=False,confidence=x['confidence'],evidence=x['evidence'],crops=crops[j] if isinstance(crops[j],list) else [crops[j]],readers={'A':A[amap[j]]['reading'] if amap[j] is not None else 'retains witness C / omitted','B':x['reading'],'C':C[cmap[j]]['reading'] if cmap[j] is not None else 'retains witness C / omitted'}))
def update(i,final=None,evidence=None,confidence=None):
 if final is not None:D[i]['final']=final
 if evidence is not None:D[i]['evidence']=evidence
 if confidence:D[i]['confidence']=confidence
update(1,A[0]['reading'],'Two limbs share a narrow bent body. Root follows A/C in retaining double-first versus single uncertainty against B’s resolution; joinedness alone does not decide the count.','medium')
update(2,A[12]['reading'],'Existing A03 separates four small dark bodies in two groups above the reference, including a tiny companion to the left point. Root adopts A’s four marks against B’s single point and C’s omission; pale surrounding texture is excluded.','medium')
update(6,phrase440,'Both high quotation groups lie outside the cancellation. The words allows one are crossed; the final diagonal meets the t entry/cross-strokes, leaving the state of to uncertain. Root favors live to but retains the cancelled alternative, against A’s cancellation and C’s live-only reading. The elevated following mark is handled separately.','medium')
D[6]['c']=r"\deleted{``allows one to''}"
D[6]['consequential']='At440 the cancellation certainly covers allows one; to remains live/cancelled uncertain. This changes the scope of the abandoned proposal without changing the later replacement sentence.'
update(8,evidence='A small separate black point lies above-left of the internal apostrophe; root accepts A/B against C’s omission. The next row’s i-dot is not copied as another mark.')
update(12,A[5]['reading'],'Raised cancelled one is readable above the gap. The upper curved connection and lower returning path remain visible around the old loop; root adopts A’s fuller geometry, retaining the o/connector uncertainty and representing the old loop once.','medium')
update(14,C[8]['reading'],'The detached low point is certain, below/right of the opener and above the word baseline. Root uses C’s anchored geometry and does not assign a full-stop function.','high')
update(17,C[9]['reading'],'Top, dense retraced middle and bottom levels have visible left returns. Root adopts C’s geometric drawing under the first i; A/B’s E-first and witness C’s equivalence-first interpretations remain possible functions, not imposed glyph identities.','medium')
D[17]['kind']='drawing or diagram'
update(18,C[16]['reading'],'The upper small body, larger angular patch and lower separate round point are distinct. Root adopts C’s relative positions; gray texture is not joined into an extra connector.','high')
update(19,right456,'The new crop confirms one short slightly curved dark stroke in the right blank. Root preserves its bend, rather than A’s round point or B’s straight short stroke.','medium')
update(21,C[10]['reading'],'The old l is clear; a lower-right loop and hook may be9 but remain entangled with cancellation. Root retains A/C’s letter doubt against B’s resolution and keeps the lowered position.','medium')
update(23,C[11]['reading'],'Two apparent lower legs share a compact upper cap. Root follows A/C’s double-first uncertainty against B’s certain pair.','medium')
update(24,leftRule,'Upper endpoint crop shows a fading, segmented start into the black rule. The lower crop shows an interrupted pale continuation to the sheet edge. Both parts are retained with origin unassigned.','medium')
update(25,rightRule,'Upper endpoint has small separate dark/gray segments before the continuous black run. The lower rule fades, with a small pale gap before the lower trace; root follows A’s separated low continuation rather than a uniformly connected line. Origin remains unassigned.','medium')
def add(id,place,c,final,abc,evidence,crop,confidence='medium',diff=True,kind='other'):
 D.append(dict(id='032-'+id,place=place,c=c,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=[crop] if isinstance(crop,str) else crop,confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
add('428-better-closer','428 first l-9, better closing group',"better''",r"better\unsure{''|'}",["better''"]*3,'A long left descending stroke turns right into a short pendant end. The asymmetric connected group favors a pair but does not securely exclude one bent stroke; root marks this occurrence independently.',ap(3))
add('440-terminal-height','440 elevated terminal segment and cross',r'\unsure{-+|+}',terminal440,[A[2]['reading'],B[6]['reading'],terminal440],'The cross stands high and the preceding horizontal touches the closing stroke. Root retains the inherited minus-plus/plus uncertainty against B’s semantic resolution, while correcting its height.',ap(6),kind='insertion or placement')
add('456-nine-point',C[17]['place'],'',C[17]['reading'],['omitted','omitted',C[17]['reading']],'Existing C11 shows a distinct small dark point below the bowl of9, left of its descending stem. It is preserved geometrically without a punctuation value.',cp(11),'high',kind='drawing or diagram')
add('468-low-point','468 l.8, below-left of8','',low468,[A[22]['reading'],'omitted','omitted'],'The low black point is separate from the numeral and from the abbreviation point between l and8. Root preserves this part of A’s proposal.',ap(17),'high',kind='drawing or diagram')
add('468-pale-rim','468 above l.8, pale ring and horizontal return','', '',[A[22]['reading'],'omitted','omitted'],'The pale upper ring and thin gray extension have diffuse material-like edges, unlike the compact black point below8. Root rejects A’s additional drawn upper mark and retains the witness omission.',ap(17),'medium',False,'drawing or diagram')
add('447-lower-edge-point','Below far-right447 fleck, near paper edge','',edge448,['omitted']*3,'The first far-right crop revealed a separate adjacent lower body. One newly frozen crop of that distinct locus confirms a compact horizontal black oval on the white paper; origin unassigned.',rp('08_edge_point448'),'medium',kind='drawing or diagram')
add('468-outer-fleck','Right margin between467 and468, outside long rule','',right468,['omitted']*3,'Existing A18 shows a compact dark fleck outside the right rule and upper-left of the pale circular material rim. It is copied separately; the diffuse circle is excluded.',ap(18),'medium',kind='drawing or diagram')
cd=doubt_decisions(copy.deepcopy(R['C']),32,'C')
cropmap={0:ap(4),1:ap(6),2:ap(9),3:ap(11),4:ap(12),5:cp(11),6:ap(15),10:ap(11),12:bp(5)}
for i,p in cropmap.items():
 cd[i]['crop']=p
 cd[i]['evidence']=cd[i]['evidence'].split(' Crop:')[0]+' Root evidence: '+p
cd[2]['evidence']='Old loop remains uncertain, while A09 confirms both the upper connector and its lower return; the loop is represented once. Crop: '+ap(9)
cd.append(dict(place='440 terminal to cancellation scope',c=r"\deleted{``allows one to''}",reading=phrase440,resolved=False,confidence='medium',decision='Revised: quotation marks live; to live-first/cancelled uncertain.',evidence=D[6]['evidence']+' Crop: '+ap(6),crop=ap(6)))
doubts=copy.deepcopy(R['C']['remaining_doubts'])
doubts += [dict(place='428 better closer',reading=r"\unsure{''|'}",alternatives='double; one bent closing stroke',confidence='medium',reason='Long left limb and very short returned right end share one transverse stroke.'),dict(place='440 final to scope',reading=r'\unsure{to|\deleted{to}}',alternatives='live to; cancelled to',confidence='medium',reason='Last diagonal meets the t letter strokes.'),dict(place='441 dont opener',reading=r'\unsure{`|``}',alternatives='single; fused double',confidence='medium',reason='Short upper spur joins the dense hook.'),dict(place='right rule lower trace',reading='pale separate continuation',alternatives='same rule continuation; separate material trace on its axis',confidence='low',reason='A short pale gap separates the low trace; no joining segment is invented.')]
inv=[]
def new(kind,pos,label):return dict(sheet_kind='list',hand='origin unassigned' if kind=='drawing' else 'another unnamed hand',element='new',kind=kind,position=pos,first_words_or_objects=label,transcribed='yes')
for i,x in enumerate(R['C']['inventory']):
 x=copy.deepcopy(x)
 if i==5:x['first_words_or_objects']='Detached bent dark point'
 if i==21:x['first_words_or_objects']="l-7 wouldn't"
 if i==24:x['first_words_or_objects']='cancelled allows one; to live/cancelled uncertain; elevated terminal mark'
 inv.append(x)
 if i==7:inv.append(new('drawing','428 above first l-9','Four separated small dark bodies in two groups'))
 if i==25:inv.append(new('deletion','440 terminal to','Live-first versus cancelled uncertainty'))
 if i==28:inv.append(new('drawing','441 above internal apostrophe','Separate dark point'))
 if i==39:
  inv.append(new('drawing','447 far right edge','Short dark near-vertical fleck'))
  inv.append(new('drawing','below447 far-right fleck','Separate compact horizontal black oval'))
 if i==44:inv.append(new('drawing','449 around doubtful old loop','Upper curved connector and lower return, loop once'))
 if i==62:inv.append(new('drawing','456 right blank','Small curved dark stroke'))
 if i==85:inv.append(new('drawing','right margin between467 and468','Dark fleck outside rule, distinct from circular material rim'))
 if i==88:inv.append(new('drawing','468 l.8 lower-left of8','Compact dark point, separate from abbreviation stop'))
for i,x in enumerate(inv,1):
 x['element']=f'{i:03}'
 if x['hand']=='his hand':x['hand']='another unnamed hand'
 if x['kind']=='drawing':x['hand']='origin unassigned'
notes=copy.deepcopy(R['C']['notes'])
notes[3]='At440 the revision concerns its diagonal map would allow one to recover. The earlier l-5 its and allows one are visibly cancelled; the quotation edges stand above the cancellations. The final to retains an independent live/cancelled uncertainty.'
notes += [
 'Root retains live-first/cancelled uncertainty for the final to at440: the last diagonal and the t strokes overlap. The high quotation marks are certainly outside the cancellation. The elevated segment/cross keeps its minus-plus versus quotation-return-plus doubt.',
 'At449 the cancelled one is raised. Upper and lower connector portions are visible around the doubtful old baseline loop; that loop is represented only once. At455 the three-level shape is drawn without deciding E, equivalence-like or emphasis function.',
 'Detached compact marks and both long fading rules have unassigned origin. The pale ring above the468 reference and circular right-margin rims are excluded as material traces. The extra low dark point at468 and the separate outer fleck are retained.',
 'The list has no heading, signature, date, own pagination or stated manuscript page count. References426–468 are source-page citations with gaps, not a count of this manuscript. Archive31 is comment-only; the hand is unnamed.',
 'Actual conditional mathematical check: if hat A denotes Set-valued presheaves, take A to be the terminal one-object category. Its presheaf category is Set; initial empty set and terminal singleton are not isomorphic, so no zero object exists and this category is not abelian. This gives a counterexample to a general claim under that interpretation only. It does not identify the intended A, decide M/m, prove the proposed indexed category abelian, or supply missing definitions. The absent438 formula is not checked. See records/math_scan032_root.md.'
]
mathnote=len(notes)
events=[dict(statement_id='S032-presheaf-abelian-conditional',date='2026-11-20',who_model_effort_run='GPT-6 Astra Pro; effort not exposed; /root',type='targeted proof check',outcome=f'Actual conditional counterexample with terminal one-object A and Set-valued presheaves: Set has distinct initial and terminal objects, hence no zero object and is not abelian. No conclusion about the undefined proposed indexed category or the M/m ink. Note N032.{mathnote}.')]
notation=copy.deepcopy(R['C']['notation'])
notation[7]['reading']=r"Local quotation-count doubts at428 allows/better,441 dont and468 ending; quotation marks at440/447 live. Final to at440 retains a separate live/cancelled doubt."
notation += [dict(sign='449 raised cancellation and connection',location='449 l11',reading=A[5]['reading'],evidence='A09 upper curve and lower return; doubtful old loop represented once.'),dict(sign='dark points and pale material',location='428,441,447 far right,456 right,468',reading='Compact dark marks preserved; pale ring above468 omitted as material.',evidence='Existing reader crops plus frozen root edge crops; no joining of separate marks.')]
viewed=json.loads((W/'records/root_032_viewed.json').read_text())
assert all(p in viewed for d in D for p in d['crops'])
coverage='All three completed readings, changes, C/context decisions, notes and inventories compared. Seven explicit C doubts retained or decided from ink, independently of one bounded root mathematical check. Every reader/witness or reader/reader disagreement adjudicated with recorded crop evidence. Root viewed29 distinct existing reader crops and8 new crops, each new crop for a separately frozen locus. No OCR, outside research or compilation; no H text rows because H is descriptive.'
rec=write_record(32,'C','brief_v15.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=events,inventory=inv,notation=notation)
print('scan032',len(D),'decisions',sum(d['diff_c'] for d in D),'C changes',len(doubts),'doubts',len(inv),'inventory',rec['crop_counts'])
