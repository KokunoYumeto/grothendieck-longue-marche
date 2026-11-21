"""Apply the main reader's recorded visual decisions for scan 005."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
choices={}
def c(k,e,selection='first',final=None,changed='no'):
 d={'personally_inspected':True,'selection':selection,'evidence':e,'changed':changed}
 if final is not None:d['final']=final
 choices[k]=d
c('b01','The numeral has a rounded top, diagonal descent and long baseline: 2. The independent bare numeral and the first mspage wrapper carry the same ink reading.')
c('b02','Four objects K, K prime, barred K and barred K prime, and four plain connecting shafts are present. The lower right cap is thick but does not show two separate wings. No extra doubtful written label is present. The two column arrangements encode the same topology; the first spacing and undecorated link are retained.')
c('b03','The narrow looped, retraced subscript has an angled entry and descending return matching the 1 in the independently agreed boxes b05 and b06, both personally inspected as comparators. The opening subscript is somewhat broader but does not establish a distinct oval 0. K_1 is retained on this local hand comparison, with the adjacent definition supporting identification rather than replacing the strokes.')
c('b04','The raised letters are a, looped l, descending g, without a separate stop. The baseline sep. is also visible, with its accent and final stop; the curved placement line stays above its bodies. The independent return scoped only the raised word. Retain inserted alg followed by live sép.')
c('b07','After K the low separated hook is a comma, not an index 1 plus stop. The following ink separates into et (low e and crossed tall t), on, and en before the clear conclut; no separate terminal c belonging to donc is visible. The second prose reading is adopted, while its K_1 and full stop are rejected.','custom',r'de $K$, et on en conclut','yes')
c('b08','The word after est has a tall initial b ascender, compressed i/e, and final n. It cannot be the entirely low un. The parenthesized reference is 3; retain (3) est bien.')
c('b09','The accent, g descender, a and tall final l are visible; the horizontal terminal line belongs directly to l and does not form an extra e. The following sign consists of two detached vertically separated points, without an a loop or connecting stroke: a colon. The complete E index has a bar on the first K and an oblique separator. Adopt égal : and retain the surrounding words/formula.','second',changed='yes')
c('b10','Three small linked bent s strokes repeat the forms in b14 and b15. There is no tall initial d ascender or separate e loop; des is rejected and literal sss retained.')
c('b11','Two short horizontal bars remain distinct; the small tick at the upper one does not cross the lower bar, so this is equals, not not-equals. After K are a short dotted upright i, stop, e and stop; there is no descending p. The raised insertion and its attachment are retained as K_1=K i.e.')
c('b14','The three abbreviation strokes repeat s, each with a bent return; the last has no detached i dot and is not a bare upright. Injectif is agreed. Retain literal injectif sss.')
c('b15','Three connected angular s forms are visible, including a bent final return rather than a dotted i. This matches the two earlier occurrences on the same page; retain sss.')
c('b16','The initial tall b, joined or/n, small o oval, and final ns form the continuous word bornons. There is no word gap making bon nom and no extra er. The following open parenthesis and provisoir- are visible, including the p descender, dotted i strokes and line-end hyphen. The cropped line ending is not expanded in this box.')
c('b18','The raised word has a tall d followed by joined low onc; its leader ends between signifie and que. The short stroke below signifie joins its g descender, not an underline. The clear raised word remains donc without an added doubt.')
c('b20','The shaft has a right-end cap with upper and lower curved wings around the point. It is more articulated than the disputed single ticks elsewhere on the page. Its left end has no perpendicular bar. Retain K right-arrow B_K.')
c('b23','The target has an open c/o start, repeated low m humps and a terminal e return. Pen lifts segment this compressed single word but do not supply the extra letters of les uns. The independent expanded segmentation is rejected; retain comme.')
c('b26','The long q descender and following u are clear. The terminal short dark run has no securely detached i dot and no securely open e loop. The independent que therefore cannot be rejected with high confidence. Preserve qui as the favored short-stroke reading with que as an alternative.','custom',r'\unsure{qui|que}','yes')
c('b27','The initial f is partly at the crop boundary but its tall crossed stroke remains identifiable; the next small oval is o, followed by a low n hump and tall terminal t. No separate dotted i or clear a supports fait. The following de K prime une is clear. Retain font de K prime une.')
c('b28','After K is a dark oval point with a much paler oblique trail. The trail may be a comma tail but is not as dark as the written point. The second comma does not settle that distinction; retain the localized stop/comma doubt. The leftmost fragment belongs to preceding context.')
(R/'documentation/149_scan005_audit_choices.json').write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan005.tex'; t=p.read_text()
t=t.replace(r'\unsure{donc on|et on en} conclut','et on en conclut').replace(r'\unsure{égal|égale} \unsure{à|:}','égal :').replace(r'\deleted{\unsure{pour}} qui font',r'\deleted{\unsure{pour}} \unsure{qui|que} font');p.write_text(t)
p=R/'reviews/149_scan005.json';r=json.loads(p.read_text());by={x['id']:x for x in r['changes']}
for key,final,b,ac,ah,conf in [('c03','et on en conclut','b07',True,False,'medium'),('c05','égal','b09',True,False,'high'),('c22',':','b09',True,True,'high'),('c16',r'\unsure{qui|que} font de K\' une ext.','b26',False,True,'medium')]:
 x=by[key];x.update(final=final,evidence=choices[b]['evidence']+((' '+choices['b27']['evidence']) if key=='c16' else ''),crop=f'crops/149_scan005_second_{b}.png',against_C=ac,against_H=ah,confidence=conf)
 if b=='b07':x['box']=[260,480,1145,615]
 if b=='b09':x['box']=[255,685,865,805]
 if b=='b26':x['box']=[1478,2168,1590,2240]
r['doubts']=[x for x in r['doubts'] if x['place'] not in ('line 5, before conclut','line 7, égal/égale','line 7, à before E')]
r['doubts'].append({'place':'line 20, after the cancelled word','reading':'qui','alternatives':['que'],'confidence':'medium','reason':choices['b26']['evidence']})
r['notes'][3]="Lines 17–21 call the functors to B_K, Pi_K and E_{bar K/K} conservative for finite-type extensions. The live wording is \\unsure{qui|que} font de K' une ext., without a separate est."
r['notes'][8]="The independent audit resolves the first phrase as et on en conclut and the later wording as égal :. The final punctuation after the last K still has a dark point with a much fainter oblique trail, so stop/comma remains doubtful. The final short qui/que remains uncertain."
r['notes'].append('Independent audit: the initial K subscript was compared with the same-page 1 forms in b05 and b06; the looped 1 is retained. This is a handwriting comparison, not a proof check. All eighteen differing boxes were inspected by the main reader; three changed the consolidated text.')
r['hand'][-1]['consistency']='Observed in et on en, bornons and comme. The audit resolves égal and the colon; the short final qui/que remains doubtful.'
r['hand'][-1]['misread']='C reads donc on and bornerons; H substitutes alors for bien and aux for comme.'
for d in r['diff_coverage']:
 if d.get('change_id')=='c03':d['reason']='Independent crop audit reads the three groups et on en before conclut.'
 if d.get('change_id')=='c05':d['reason']='Independent crop audit resolves égal without an extra final e.'
 if d.get('change_id')=='c16':d['reason']="Live wording is \\unsure{qui|que} font de K' une ext.; the preceding pour is cancelled and no separate est is present."
r['root_review_note']='First review and subsequent independent audit are preserved in their respective records. Current readings and remaining doubts are those in this report and the consolidated page.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
