"""Root adjudication of scan028; original independent returns remain untouched."""
from common import *
R=load_page(28)
T={r:(W/f'readers/028/{r}/reading.tex').read_text() for r in 'ABC'}
CH={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
def a(i):return CH['A'][i]
def b(i):return CH['B'][i]
def c(i):return CH['C'][i]
def ap(i):return f'readers/028/A/crops/{i:02}.jpg'
def bp(i):return f'readers/028/B/crops/u{i:02}.jpg'
def cp(i):return f'readers/028/C/crops/{i:02}.jpg'
text=T['A'];replacements=[]
def repl(old,new):
 global text
 assert old in text,old
 text=text.replace(old,new,1);replacements.append((old,new))
repl('is perhaps better.',r'is perhaps better\unsure{,|.}')
repl("{'doesn't''}",r"{\unsure{'|``}doesn't''}")
repl('also in l.15.',r'also \unsure{in|on} l.15.')
repl("l.9 ``its''",r"l.9 \unsure{``|'}its''")
paren=c('345-parenthesis-stroke')['reading']
repl('(again).',paren)
# The old and live a already occupy one physical letter position in A.
# Final marginal cancellation geometry and all apparatus are appended after
# the complete B return has been read and compared with A/C.
foot=c('bottom-note-placement')['reading']
repl(a('bottom_note_placement')['reading'],foot)
lowagain=c('again-low-dash')['reading']
repl(a('again_low_mark')['reading'],lowagain)
extra_ids=['blank_slash_01','blank_point_02','blank_slash_03','blank_point_04','blank_point_05','blank_point_06','blank_faint_dash_07','blank_faint_curve_08','blank_curve_09','blank_gray_mark_10','blank_point_11','blank_mark_12','blank_dash_13','blank_point_15','blank_mark_16','blank_point_18','blank_point_19']
extra={i:b(i)['reading'] for i in extra_ids}
extra['blank_faint_dash_07']=r'\fill[black!40] (104,1502) ellipse[x radius=.6,y radius=.8];\fill[black!35] (107,1503) ellipse[x radius=.6,y radius=.7];\fill[black!40] (111,1505) ellipse[x radius=.7,y radius=.5];'
extra['blank_faint_curve_08']=r'\draw[black!40,line width=.16pt] (369,1653)--(371,1650);'
extra['blank_dash_13']=r'\draw[line width=.20pt] (908,1772)--(910,1773);\draw[black!30,line width=.16pt] (910,1773)--(914,1774);'
repl('% BEGIN bottom_note','% Isolated lower-field marks: shape only, physical origin unassigned.\n'+'\n'.join('% '+i+'\n'+extra[i] for i in extra_ids)+'\n% BEGIN bottom_note')
D=[]
def add(i,place,old,final,abc,evidence,crops,confidence='medium',kind='other',diff=True):
 D.append(dict(id='028-'+i,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
def pick(r,i,abc,evidence,crops,confidence=None,final=None):
 x=CH[r][i];add(i,x['place'],x['c'],final if final is not None else x['reading'],abc,evidence,crops,confidence or x['confidence'],x.get('kind','other'))
add('339-retain','p.339 l-12, crossed final sign',r'\deleted{\unsure{\&|l}}',r'\deleted{\unsure{\&|l}}',[r'\deleted{\unsure{\&|l}}',r'\deleted{\unsure{\&|l}}',c('339-cancelled-sign')['reading']],
 'The upper loop and crossed lower return leave ampersand/l unresolved. Root does not find sufficient evidence to reverse C’s candidate order as reader C proposed; cancellation is certain.',ap(2),'low','other',False)
pick('B','341_better_mark',['better.',b('341_better_mark')['reading'],'better.'],
 'A low oblique filled body descends rightward. Root favors comma but retains period as an alternative; A/C’s certain stop and B’s stop-first order are not adopted.',[ap(4),bp(2)],'medium',r'better\unsure{,|.}')
pick('C','341-opening-quote',["'doesn't''",b('341_doesnt_opener')['reading'],c('341-opening-quote')['reading']],
 'One looped high body has two projecting tips. Root follows B/C in retaining single/fused-double uncertainty; the closing pair is separately clear.',ap(5),'medium')
pick('A','342_ref_stop',['l.-8']*3,'A separate low point lies between the l foot and the minus. All three readers and root confirm the omitted point.',ap(6),'high')
pick('C','345-parenthesis-stroke',['(again).',b('345_again_spur')['reading'],paren],
 'The closing curve has a short transverse stroke joined near the word baseline, not a detached period. Root preserves C reader’s connected geometry. Its punctuation function remains uncertain.',ap(8),'high')
pick('C','350-in-on',['also in l.15.','also in l.15.',c('350-in-on')['reading']],
 'The first low body is looped/closed while a high point sits near its join to n. Root follows reader C in retaining in/on uncertainty; both stops in l.15. are clear.',cp(6),'medium')
pick('A','351_overlap',[a('351_overlap')['reading'],b('351_overwritten_a')['reading'],c('351-overlap')['reading']],
 'The old rounded letter and live first a occupy one glyph space. Root overlays them without duplicating shared surrounding letters. Old a/o remains uncertain; double opener and single closer are independently clear.',ap(12),'high')
pick('C','353-opening-quote',["``its''","``its''",c('353-opening-quote')['reading']],
 'A closed narrow slot and two apparent tips do not securely distinguish a joined pair from one looped stroke. Root retains the local double/single opener doubt against A/B certainty.',cp(10),'medium')
maps=[('left_rule','left_rule','left-rule','crops/028/01_left_rule.jpg'),('right_rule','right_rule','right-rule','crops/028/02_right_rule.jpg')]
for ai,bi,ci,crop in maps:
 pick('A',ai,[a(ai)['reading'],b(bi)['reading'],c(ci)['reading']],
  'The narrow full-extent root crop confirms a nearly continuous dark rule from above the first entry to the paper foot. Slight bends and text crossings are retained in the common coordinate field.',crop,'high')
pick('A','faint_trace',[a('faint_trace')['reading'],b('faint_left_trace')['reading'],c('faint-left-trace')['reading']],
 'A14/A15 and B12/B13 show a pale far-left course with diffuse endpoints. Root retains the fading approximate extent in A, against C’s sharply limited upper start and B’s continuous extension to2338. The lower texture does not securely establish that extension; original endpoints and origin remain open.',[ap(14),ap(15),bp(12),bp(13)],'low')
pick('A','upper_dash',[a('upper_dash')['reading'],b('upper_short_dash')['reading'],c('upper-dash')['reading']],
 'A separate short dark horizontal lies well left of the pale circular material feature; its geometry is preserved without lexical function.',cp(12),'high')
pick('A','right_point',[a('right_point')['reading'],b('point_beside_rule')['reading'],c('right-point')['reading']],
 'The root right-rule crop separates a compact dark point just left of the ruled line at the340 level.', 'crops/028/02_right_rule.jpg','high')
pick('A','afraid_marks',[a('afraid_marks')['reading'],'omitted',c('afraid-low-mark')['reading']],
 'A03 shows an extra upper point apart from the normal i dot, plus two separate low oblique marks. Root preserves all three without assigning punctuation roles.',ap(3),'medium')
pick('A','again_low_mark',[a('again_low_mark')['reading'],b('low_dash_345')['reading'],lowagain],
 'The separate low mark below the closing parenthesis has two discernible pieces, a paler left part and darker right part. Root adopts the two-part geometry rather than joining them.',ap(8),'medium',lowagain)
pick('A','left_352_point',[a('left_352_point')['reading'],b('left_point_352')['reading'],'omitted'],
 'A compact isolated point stands left of the page-reference column between352 and353. Root preserves its observed position.', 'crops/028/03_left_352_point.jpg','high')
pick('A','lower_right_points',[a('lower_right_points')['reading'],b('blank_two_points_14')['reading'],'omitted'],
 'The root crop shows two distinct dark points diagonally separated in the lower-right field. Geometry only; origin and function unassigned.', 'crops/028/04_lower_right_points.jpg','medium')
pick('A','lower_left_marks',[a('lower_left_marks')['reading'],b('blank_left_cluster_17')['reading'],'omitted'],
 'A15 shows a short bent dark mark and a separate upper-right point, immediately left of the reference rule in the lower blank field.',ap(15),'medium')
pick('A','bottom_note_placement',[a('bottom_note_placement')['reading'],b('foot_note_position')['reading']+' '+b('lower_pendant_marks')['reading'],foot],
 'The cancelled end/ed stands outside the right rule at the extreme foot, well below the last entry. Its baseline rises rightward under several returned oblique crossings, and two low vertical traces survive beneath its right side. Root uses C’s slanted placement and multiple-crossing geometry. Buried middle letters remain uncertain.',[ap(13),cp(11)],'high',foot)
for label,bi,ci,crop in [('upper-material-feature','upper_right_loop','upper-ring',cp(12)),('lower-material-feature','lower_faint_loop','lower-ring',cp(11))]:
 add(label,'Pale circular feature at '+('upper-right' if label.startswith('upper') else 'lower-right')+' edge','','',
  ['material feature, not drawn',b(bi)['reading'],c(ci)['reading']],
  'Root agrees with A’s whole-sheet distinction: a pale ragged circular material contour with local fragments, not definite manuscript ink. B/C reproduce the surface feature without identifying its origin. It is recorded here as material appearance, not added to the diplomatic ink drawing.',crop,'medium','other',False)
cropmap={1:5,2:6,3:7,4:7,5:8,6:9,7:10,8:11,9:12,10:13,11:14,12:14,13:15,15:16,16:17,18:18,19:18}
rootfiles={int(p.name.split('_')[0]):str(p.relative_to(W)) for p in (W/'crops/028').glob('*.jpg')}
extra_y={1:1190,2:1219,3:1244,4:1290,5:1368,6:1395,7:1503,8:1652,9:1734,10:1743,11:1749,12:1768,13:1773,15:2090,16:2107,18:2139,19:2159}
for i in extra_ids:
 num=int(i.rsplit('_',1)[1]);ev='The tight root crop shows a distinct compact dark '+('point' if 'point' in i else 'short mark')+' at the reported position. It is preserved geometrically with origin and function unassigned, not asserted to be a letter or intentional drawing.'
 conf='medium'
 if num==7:ev='The tight crop shows three separated dark/gray flecks with lighter texture between. Root preserves them as separate small bodies and rejects B’s joining line.';conf='low'
 if num==8:ev='The proposed curve resolves into disconnected gray flecks. Root preserves only the discernible darker upper slant and rejects an interpolated continuous curve through the surrounding texture.';conf='low'
 if num==9:ev='The crop shows a compact dark upper body with a connected downward-curving tail; root preserves the short curved geometry without assigning a punctuation function.'
 if num==10:ev='The crop shows a short oblique two-lobed connected mark, darker at its ends. Its physical origin remains unassigned.'
 if num==13:ev='The crop shows a short dark left core and a fading rightward continuation, with a gap before a separate pale texture fleck. Root preserves only the discernible short stroke and does not extend it through the gap.'
 pick('B',i,['omitted',b(i)['reading'],'omitted'],ev,rootfiles[cropmap[num]],conf,extra[i])
# C doubts are copied without mutating the independent report; fix its work-relative paths locally.
ar=copy.deepcopy(R['A'])
for x in ar['c_doubts']:
 if x.get('crop','') and x['crop'].startswith('work/'):x['crop']=str(W/x['crop'][5:])
cd=doubt_decisions(ar,28,'A')
cd[7].update(reading=r"``and alongside \uline{got me} back'' is perhaps better\unsure{,|.}",resolved=False,confidence='medium',evidence='The words is perhaps better are certain and retain the writer’s qualification. Root A04/B02 leaves the final oblique mark comma/period uncertain.')
for x in cd:x['decision']=('Resolved/confirmed: ' if x.get('resolved') else 'Retained/revised: ')+x['reading']
doubts=copy.deepcopy(R['A']['remaining_doubts'])
for place,reading,alts,reason in [
 ('p341 after better',r'better\unsure{,|.}','comma; period','Low oblique filled body with no independently resolved tail.'),
 ('p341 l7 opener',r"\unsure{'|``}doesn't''",'single; fused double','Looped high body and projecting tips leave count unresolved.'),
 ('p.345 closing parenthesis',paren,'attached punctuation; nonpunctuating transverse extension','Connected curve and short bar are reproduced; their function is uncertain.'),
 ('p350 after also',r'also \unsure{in|on} l.15.','in; on','Closed low first body and high point support competing readings.'),
 ('p353 l.9 opener',r"\unsure{``|'}its''",'double; single','Fused tips and narrow slot do not decide original stroke count.')]:
 doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=reason))
inv=copy.deepcopy(R['A']['inventory'])
for x in inv:
 for old,new in replacements:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
for x in inv[:2]:x['hand']='ruling hand not independently identified'
inv[27]['first_words_or_objects']='Separate two-part low dash, not joined to parenthesis'
inv[44]['position']='Extreme bottom right, outside right rule; baseline rises rightward'
inv[45]['first_words_or_objects']='Several returned oblique crossings across end/ed, with two low vertical traces'
ys=[90,94,75,110,118,177,168,241,249,305,305,366,378,334,434,435,448,496,499,558,573,578,610,631,685,697,701,729,750,817,831,824,944,947,953,953,953,1005,1018,1066,1073,1134,1984,2125,2306,2310,2350]
for i in extra_ids:
 num=int(i.rsplit('_',1)[1]);inv.append(dict(sheet_kind='list',hand='unassigned origin, isolated dark mark',element='added',kind='drawing',position=b(i)['place']+f', whole-image y{extra_y[num]}',first_words_or_objects=extra[i],transcribed='yes'));ys.append(extra_y[num])
inv.append(dict(sheet_kind='list',hand='his hand',element='added',kind='drawing',position='Nested at closing parenthesis of again, p.345',first_words_or_objects=paren,transcribed='yes'));ys.append(698)
inv=[x for i,x in sorted(enumerate(inv),key=lambda z:(ys[z[0]],z[0]))]
for i,x in enumerate(inv,1):x['element']=f'{i:02}'
notes=copy.deepcopy(R['A']['notes'])
notes[2]='p341 l.2 proposes ``and alongside got me back\'\' and explicitly says is perhaps better, with only its terminal punctuation uncertain. The underline spans got me.'
notes += ['The connected short spur at the closing parenthesis after again is drawn without assigning a punctuation value. Fused opening quotations at p341 and p353, also in/on at p350, and the four inherited letter/underline doubts remain local uncertainties.',
 'The lower blank field contains isolated dark points and short marks of unassigned origin. Distinct visible marks are preserved without interpreting paper texture as letters or joining separated flecks. Two pale circular features at the right edge have a material appearance and are documented as such, not redrawn as manuscript ink.',
 'H gives only a description, so this page has no H collation rows. The isolated usage corrections supply no substantive mathematical assertion or surrounding definitions to test; no mathematical check event is claimed.']
notation=copy.deepcopy(R['A']['notation'])
notation[3].update(reading=r"``and even''; \unsure{'|``}doesn't''; ``with''; (``from''",evidence='Root A01/A05/A07/A10: p341 opener count remains local and uncertain; the other listed pairs are visible.')
notation[6].update(sign='Low oblique terminal mark',reading=r'better\unsure{,|.}',evidence='Root A04/B02: filled descending body; comma favored but period remains possible.')
notation[7].update(sign='Closing parenthesis with joined bar',reading=paren,evidence='Root A08: attached transverse stroke, no isolated period; function left open.')
notation += [dict(sign='fused opening quotation',location='p353 l.9',reading=r"\unsure{``|'}its''",evidence='Root C10: joined tips and slot, original count uncertain.'),dict(sign='short dotted/looped word',location='p350 after also',reading=r'\unsure{in|on}',evidence='Root C06: low closed body and high point do not securely decide first letter.')]
viewed=json.loads((W/'records/root_028_viewed.json').read_text())
coverage='All three final full readings, reports and inventories were compared. All four explicit C doubts and five context issues have decisions. Root adjudicated all reader/witness differences on retained crops, including the rejected candidate reversal, material-circle drawings and continuity proposals. Root reused24 reader crops and generated18 new crops (two narrow complete rules and16 isolated-mark loci, including three close two-mark groups); all were actually displayed. Failed/truncated displays were retried from existing files, without recropping. The inventory has65 elements and10 remaining physical doubt loci. Isolated dark marks are retained with unassigned origin; photographic texture and material features are distinguished in the notes. H is description-only; no OCR, outside research, compilation or mathematical proof was performed.'
rec=write_record(28,'A','brief_v13.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=[],inventory=inv,notation=notation)
print('scan028',len(D),'decisions',sum(x['diff_c'] for x in D),'C changes',len(doubts),'doubts',len(inv),'inventory',rec['crop_counts'])
