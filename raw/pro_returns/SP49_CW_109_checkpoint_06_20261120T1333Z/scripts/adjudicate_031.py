"""Root adjudication; preserves the three independent scan031 returns."""
from common import *
R=load_page(31)
T={r:(W/f'readers/031/{r}/reading.tex').read_text() for r in 'ABC'}
A=R['A']['changes']; B=R['B']['changes']; C=R['C']['changes']
text=T['B']
def repl(old,new):
 global text
 assert text.count(old)==1,(old,text.count(old))
 text=text.replace(old,new,1)
def ap(i):return f'readers/031/A/crops/{i:02}.jpg'
def cp(i):return f'readers/031/C/crops/{i:02}.jpg'
def bp(name):return 'readers/031/B/crops/'+name+'.jpg'
hat=r'\tikz[baseline=(hat031.base)]{\node[inner sep=0pt] (hat031) {$\hat{A}_{ab}$};\draw[overlay,line width=.35pt,line cap=round] ([xshift=.14em,yshift=.85ex]hat031.base west)--([xshift=.25em,yshift=1.0ex]hat031.base west);}'
repl(r'$\hat{A}_{ab}$',hat)
repl('l.8 ``its',r'l\unsure{.|,}8 ``its')
repl('``around\'\' but',r"``around\unsure{''|'} but")
old407=B[5]['reading'].replace(r'\deleted{the}',r'\deleted{\unsure{the|its}}')
repl(B[5]['reading'],old407)
as407=B[6]['reading'].replace(r'\deleted{i}',r'\deleted{\unsure{i}}')
repl(B[6]['reading'],as407)
repl(B[7]['reading']+" `relier''",C[6]['reading'])
first410=r"\deleted{l.\unsure{2}} ``\deleted{its}\unsure{\deleted{''}|''}"
repl(B[13]['reading'],first410)
second410=B[15]['reading'].replace('Its|its','its|Its')
repl(B[15]['reading'],second410)
repl('c.f comment on p.407.',r'c.f comment on p.407\unsure{,|.}')
repl("l.9. ``formulary''",r"l.9. \unsure{``|`}formulary''")
repl(B[19]['reading'].split(' ``formulary')[0],C[16]['reading'])
old417=r'\deleted{\unsure{l 1|f}}'
old417withmarks=r'\tikz[baseline=(old417.base)]{\node[inner sep=0pt] (old417) {'+old417+r'};\fill[overlay,black!75] ([xshift=-.15em,yshift=-.5ex]old417.base east) circle (.04ex);\draw[overlay,black!60,line width=.35pt,line cap=round] ([xshift=-.38em,yshift=-.7ex]old417.base east)..controls([xshift=-.47em,yshift=-.9ex]old417.base east)and([xshift=-.46em,yshift=-1.05ex]old417.base east)..([xshift=-.42em,yshift=-1.12ex]old417.base east);}'
repl(r'\deleted{\unsure{l 1}}',old417withmarks)
repl("l 13 ``formulary'' again",r"l 13 ``formulary\unsure{''|'} again")
repl(B[25]['reading'].split('again ',1)[1].rsplit(' l.14.',1)[0],C[23]['reading'])
repl(B[27]['reading'],B[27]['reading'].replace('`|``','``|`'))
D=[]
amap=[0,1,None,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,20,None,21,22,24,25,26,27,None,28,None,None]
cmap=[None,0,None,2,3,4,5,6,8,None,9,10,None,11,12,13,None,14,15,16,17,18,20,21,22,23,None,24,25,26]
crops=[ap(2),ap(3),bp('02_403_cancelled_own'),ap(4),ap(5),ap(7),ap(8),ap(8),ap(9),ap(10),ap(11),cp(14),ap(13),ap(14),ap(16),ap(17),ap(18),ap(20),ap(23),cp(24),ap(24),ap(25),ap(27),ap(28),ap(29),ap(30),bp('36_lower_isolated_mark'),ap(32),[cp(36),cp(38)],[cp(37),cp(39)]]
for j,x in enumerate(B):
 D.append(dict(id='031-'+x['id'],place=x['place'],c=x['c'],h=None,final=x['reading'],diff_c=True,diff_h=False,kind=x['kind'],marked_in_H=False,confidence=x['confidence'],evidence=x['evidence'],crops=crops[j] if isinstance(crops[j],list) else [crops[j]],readers={'A':A[amap[j]]['reading'] if amap[j] is not None else 'retains witness C / omitted','B':x['reading'],'C':C[cmap[j]]['reading'] if cmap[j] is not None else 'retains witness C / omitted'}))
def update(i,final=None,evidence=None,confidence=None):
 if final is not None:D[i]['final']=final
 if evidence is not None:D[i]['evidence']=evidence
 if confidence:D[i]['confidence']=confidence
update(0,evidence='The long descending shaft ends in two returning head strokes, supporting a downward arrow followed by separate6. Root resolves the reference with A/B against C reader’s retained stylised1 alternative; no line-number expectation is used.',confidence='high')
update(1,evidence='The crossed word retains an o loop, two w troughs and an n shoulder. Root resolves own at medium confidence after distinguishing these old letters from the crossing lines; the raised closer remains live.')
update(3,evidence='A horizontal bar has a marked central downward spur, so a plus-shaped sign is placed first. A short minus with a retracing spur remains possible; root follows A/B candidate order against C reader’s minus-first order.')
update(5,old407,'Two horizontal cancellation levels obscure the middle joins. A tall stem and loop favor the but do not exclude its; root retains A’s lexical doubt against B/C resolution. The replacement its is certainly raised above/right of the old word.','high')
update(6,as407,'An old dot and upright overlap the live a; the shared final s is written once. Root retains the old i doubt against B/C resolution while accepting the certain physical overlap.','high')
update(7,C[6]['reading'],'The phrase a p.p of is raised above the gap before relier, whose low forked indicator has one long shaft and an oblique branch. Its medial point is retained without expanding the abbreviation. The opener decision is listed separately.','high')
update(9,evidence='The low terminal body has a vertical upper portion and bent leftward foot. Root follows A/B’s comma against C reader’s unchanged stop.',confidence='high')
update(12,evidence='Small sinuous lobes remain under the long live t stem in the last its. Root preserves tentative old s overlapped by t, with the live i and final s only once; C reader omits this under-writing.')
update(13,first410,'The opening pair lies outside the cancellation. The old2 remains buried under two bands despite A/C resolution. A terminal diagonal meets the closer without deciding the state of both strokes: root retains C reader’s closer-state doubt, separate from the numeral doubt.')
update(14,evidence='The high joined body has two unequal pendant ends, favoring a closing pair. Root retains A/B’s count uncertainty against C reader’s certain pair; the three lower continuation points remain separate.')
update(15,second410,'The opener is outside the cancellation. Buried joins permit its, with the broad first remnants also allowing Its; root puts the inherited lowercase candidate first rather than deciding case from the cancellation. The closer is contacted by the long crossing and retains its separate state doubt.','low')
update(16,evidence='A curved high stroke and a separate short oblique body are both visible. Root follows A/B’s double opener against C reader’s single opener.',confidence='high')
update(19,C[16]['reading'],'The reference has a short hooked horizontal stroke and one low point directly below it. Root adopts C reader’s geometry, preserving the hook as well as the vertical relation. The point is not duplicated as l. and a second drawn point.','high')
update(20,evidence='One vertical body with a short right branch has no separate second stroke. Root follows B/C’s single-first order, retaining fused double as an alternative to A’s double-first reading.')
update(25,'again '+C[23]['reading']+' l.14.','The word in is raised; its i-dot remains in the text. The insertion indicator is a long descending near-vertical with a short right foot and a separate upper point. Root uses C reader’s geometry because A/B omit that detached top component.','high')
update(27,B[27]['reading'].replace('`|``','``|`'),'Two long branches meet at one high apex. Root follows A/C’s double-first order while retaining single as possible; this is independent of other its occurrences.')
for i in [28,29]:
 update(i,evidence='Endpoint crops show a definite narrow upper trajectory, slight bends and interrupted intensity, becoming much paler below. Root preserves the visible trace with fading intensity and origin unassigned. A reader’s material-only omission is not secure; C reader’s uniform gray line overstates the lower contrast. The lower left endpoint remains unbounded; the right trace ends above archive30.',confidence='medium')
def add(id,place,c,final,abc,evidence,crop,confidence='medium',diff=True,kind='other'):
 D.append(dict(id='031-'+id,place=place,c=c,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=[crop] if isinstance(crop,str) else crop,confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
add('hat-small-mark','402 hatted A, small mark near upper-left body',r'$\hat{A}_{ab}$',hat,[r'$\hat{A}_{ab}$']*3,'A short detached dark oblique stands between the left roof branch and the upper-left A body. Root preserves it geometrically once, without making it a second accent or altering the separately clear lowered ab.',ap(2),kind='drawing or diagram')
add('403-l8-punctuation',C[1]['place'],C[1]['c'],C[1]['reading'],['l.8','l.8',C[1]['reading']],'The detached low body after l is oblique and has a short tail; a stop remains plausible. Root follows C reader in marking period/comma uncertainty.',cp(4))
add('407-English-stop','407 first sentence, English. It','English. It','English. It',['English. It']*3,'The low dark body before I is distinguishable from the main serif, despite a fine rising trace toward it. Root withdraws the initial provisional omission and retains the period supported by all three readers.',cp(7),diff=False)
add('407-around-closer','407 parenthetical, first around closer',"around''",r"around\unsure{''|'}",["around''"]*3,'One high arch has two descending limbs sharing its apex. Root records local double/single count uncertainty rather than treating the fused body as a certain pair.',cp(8))
add('407-relier-opener','407 relier opening group',"`relier''",r"\unsure{`|``}relier''",[A[7]['reading'],"`relier''",C[7]['reading']],'A narrow pointed/branched group is joined beneath the raised phrase. Root follows C reader’s single-first doubt against A’s double and B’s single.',ap(8))
add('411-reference-terminal','411 terminal p.407 mark','p.407.',r'p.407\unsure{,|.}',[A[18]['reading'],'p.407.','p.407.'],'The detached mark has a rounded head and a short lower-left stem. Comma is favored, but a compact elongated stop is not excluded; root keeps both against A’s comma and B/C’s stop.',ap(21))
add('412-formulary-opener',A[19]['place'],A[19]['c'],A[19]['reading'],[A[19]['reading'],A[19]['c'],A[19]['c']],'The two limbs meet at one low junction. Root retains A’s local double/single uncertainty against the other readers’ unmarked double.',ap(22))
add('417-false-start',C[19]['place'],C[19]['c'],old417,[A[23]['reading'],r'\deleted{\unsure{l 1}}',old417],'A tall loop and a middle angular upright favor l 1, but the thick diagonal crossing prevents separating all old joins. Root retains C reader’s f alternative against A’s resolution and B’s narrower doubt.',ap(26),'low')
add('417-low-marks','417 below the cancelled false start',old417,old417withmarks,['omitted']*3,'Below the cancellation are two distinct remnants: an upper-right short dark point and a lower-left faint hooked slant. They are spatially separate from the parentheses and preserved without assigning a letter or connecting them into a line.',ap(26),kind='drawing or diagram')
add('422-formulary-closer','422 formulary closing group',"formulary''",r"formulary\unsure{''|'}",["formulary''"]*3,'Two vertical limbs are joined by a high transverse body. Root keeps double first but marks the count ambiguity at this occurrence independently.',ap(30))
cd=doubt_decisions(copy.deepcopy(R['A']),31,'A')
for i,rd,res,ev in [(3,as407,False,'Tentative old i overlaps live a; shared s once.'),(5,r'\unsure{2}',False,'The old numeral is buried under crossing bands; A/C resolution is rejected.'),(7,r'\unsure{its|Its}',False,'Lowercase candidate remains first, but broad old remnants leave capital I possible.'),(8,B[18]['reading'],False,'Tentative old t overlaps live d, shared o once.'),(9,old417,False,'Crossing prevents rejecting the one-body f alternative.'),(14,C[23]['reading'],True,'Raised in and the full long indicator, including detached upper point.'),(24,r"(however I feel it should be not ``around\unsure{''|'} but perhaps ``on and around'')",False,'Qualifying words confirmed; first around closer count locally uncertain.')]:
 cd[i].update(reading=rd,resolved=res,decision=('Resolved/confirmed: ' if res else 'Retained/revised: ')+rd,evidence=ev+' Crop: '+(ap(8) if i==3 else ap(14) if i==5 else ap(17) if i==7 else ap(23) if i==8 else ap(26) if i==9 else ap(30) if i==14 else cp(8)))
cd.append(dict(place='411 terminal p.407 punctuation',c='p.407.',reading=r'p.407\unsure{,|.}',resolved=False,confidence='medium',decision=r'Revised: p.407\unsure{,|.}',evidence='Rounded head and short descending-left stem. Crop: '+ap(21),crop=ap(21)))
doubts=[]
def doubt(place,reading,alt,reason,conf='medium'):doubts.append(dict(place=place,reading=reading,alternatives=alt,confidence=conf,reason=reason))
for place,rd,alt,why,conf in [
 ('403 l8 punctuation',r'l\unsure{.|,}8','period; comma','Compact oblique low mark with short tail.','medium'),
 ('404 sign before5',r'\unsure{+|-}','plus-shaped; minus with spur','Central downward spur on horizontal bar.','medium'),
 ('405 didnt opener',r'\unsure{``|`}','double; single','Joined curved outer stroke and interior branch.','medium'),
 ('407 first around closer',r"\unsure{''|'}",'double; single','Two limbs share one arch.','medium'),
 ('407 old word',r'\deleted{\unsure{the|its}}','the; its','Two cancellation levels hide joins.','low'),
 ('407 old initial',r'\deleted{\unsure{i}}','i; buried form','Dot and old upright overlap a.','low'),
 ('407 relier opener',r'\unsure{`|``}','single; double','One joined angular body.','medium'),
 ('409 old letter',r'\deleted{\unsure{s}}','s; buried form','Sinuous remnants under t.','low'),
 ('410 first old digit',r'\unsure{2}','2; hidden contour','Crossing bands obscure middle.','low'),
 ('410 first closer state',r"\unsure{\deleted{''}|''}",'cancelled; live','Terminal cancellation meets quotation group.','medium'),
 ('410 being closer',r"\unsure{''|`}",'closing pair; single returned stroke','Two unequal pendant ends share top.','medium'),
 ('410 second old word',r'\unsure{its|Its}','its; Its','Buried joins leave initial case unresolved.','low'),
 ('410 second closer state',r"\unsure{\deleted{''}|''}",'cancelled; live','One closer part meets cancellation, another stands separate.','medium'),
 ('411 copy punctuation',r'\unsure{,|.}','comma; period','Short bent descending body.','medium'),
 ('411 p407 punctuation',r'\unsure{,|.}','comma; period','Rounded head, short leftward lower stem.','medium'),
 ('412 first formulary opener',r'\unsure{``|`}','double; single','Two limbs joined at foot.','medium'),
 ('412 old initial',r'\deleted{\unsure{t}}','t; buried joins','Old bar/upright overlaps d.','low'),
 ('413 wont closer',r"\unsure{'|''}",'single; double','Vertical with short right branch.','medium'),
 ('417 old reference',old417,'l 1; f','Crossing hides division into one or two glyphs.','low'),
 ('419 make sense opener',r'\unsure{`|``}','single; double','Long stem with attached short branch.','medium'),
 ('422 formulary closer',r"\unsure{''|'}",'double; single','Two limbs joined by top body.','medium'),
 ('423 first reference glyph',r'\unsure{p|l}','p; l','Long stem and right thickening without clear bowl.','low'),
 ('425 its opener',r'\unsure{``|`}','double; single','Two long branches share one apex.','medium'),
 ('left trace lower endpoint','faded geometry','exact endpoint unbounded','Pale interrupted continuation below425 has no crisp terminal point.','low')]:doubt(place,rd,alt,why,conf)
inv=[]
def newdraw(pos,label):return dict(sheet_kind='list',hand='origin unassigned',element='new',kind='drawing',position=pos,first_words_or_objects=label,transcribed='yes')
for i in [81,82]:inv.append(copy.deepcopy(R['B']['inventory'][i]))
for i,x in enumerate(R['B']['inventory'][:81]):
 x=copy.deepcopy(x)
 if i==21:x['first_words_or_objects']=r'\deleted{\unsure{the|its}}'
 if i==23:x['first_words_or_objects']='tentative old i under a; final s shared'
 if i==41:x['first_words_or_objects']='its, with closer cancellation state uncertain'
 if i==46:x['first_words_or_objects']=r'\unsure{its|Its}'
 if i==68:x['first_words_or_objects']=old417
 if i==77:x['first_words_or_objects']='descending indicator with hooked foot and detached upper point'
 inv.append(x)
 if i==4:inv.append(newdraw('402 hatted A, near upper-left body','separate short dark oblique'))
 if i==68:inv.append(newdraw('417 below cancelled false start','two distinct low remnants: point and faint hooked slant'))
inv.append(copy.deepcopy(R['B']['inventory'][83]))
for i,x in enumerate(inv,1):
 x['element']=f'{i:02}'
 if x['hand']=='his hand':x['hand']='another unnamed hand'
 if x['kind']=='drawing':x['hand']='origin unassigned'
notes=copy.deepcopy(R['C']['notes'])+[
 'Overwritten initials in as, its and do occupy one glyph space; the unchanged adjacent letters are represented once. Cancellation extent and hidden letter identity are decided separately, especially the two quoted deletions at410.',
 'The downward-arrow-plus6 reference and upward arrow above the first ditto pair are resolved from their shafts and two head limbs. The hatted A has ordinary lowered ab; formula references (75)e and (84)e keep baseline e. No missing mathematical content is supplied from those references.',
 'Small detached marks at402,403,408,416,417,420 and423 and the two long fading traces are preserved with origin unassigned. Circular right-margin rims are material features. The lower-left trace has no secure endpoint; its approximation is deliberately pale.',
 'The list has20 referenced-page blocks, not a manuscript page count. No heading, date, signature, own pagination or stated page total appears. Archive30 is comment-only. The hand is unnamed on this sheet.',
 'All three readers and root merely read the notation and correction claims; no proof, computation, or substantive mathematical check event was performed. H contains description only and contributes no textual collation rows.'
]
notation=copy.deepcopy(R['B']['notation'])
notation[8]['reading']=r"Local quote doubts at405,407 around/relier,410 being,412 first formulary,413 wont,419 make sense,422 formulary and425 its; independent cancellation-state doubts at both410 closers."
notation[9]['reading']=as407+'; '+B[12]['reading']+'; '+B[18]['reading']
notation[-1]['reading']=C[16]['reading']
notation += [dict(sign='cancelled false start',location='417 before second(84)',reading=old417,evidence='Loop and middle upright favor l1, but crossing leaves f possible; two low detached remnants preserved separately.'),dict(sign='fading long traces',location='between columns and at right',reading='Two anchored TikZ traces, darker upper and pale lower portions; origin unassigned.',evidence='Endpoint crops distinguish narrow paths from circular material impressions; the lower-left endpoint is unbounded.')]
viewed=json.loads((W/'records/root_031_viewed.json').read_text())
assert all(p in viewed for d in D for p in d['crops'])
coverage='Compared all three completed returns, every change, all11 explicit C uncertainty loci and15 contextual decisions, notes and inventories. Root viewed49 distinct existing reader crops and no new crop. Every reader/witness or reader/reader disagreement is adjudicated on recorded crops, including root-only small marks and quote doubts. The inventory preserves each correction and nested mark in physical order, with long traces anchored beside the list. No OCR, outside research or compilation.'
rec=write_record(31,'B','brief_v15.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=[],inventory=inv,notation=notation)
print('scan031',len(D),'decisions',sum(d['diff_c'] for d in D),'C changes',len(doubts),'doubts',len(inv),'inventory',rec['crop_counts'])
