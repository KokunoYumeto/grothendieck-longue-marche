from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[1];stem='H156-01_156-7_scan002'
co={r['box']:[int(r[k]) for k in ('x0','y0','x1','y1')] for r in csv.DictReader((R/'second'/f'{stem}_boxes.tsv').open(),delimiter='\t')}
cfg={'reader':'reader_b (GPT-6 Astra Pro; effort not exposed)','patches':[
 {'old':r'\unsure{50}-58','new':r'\unsure{50}-\unsure{58}'},
 {'old':r'\inserted{\uline{proprement}}','new':r'\inserted{proprement}'},
 {'old':r'\unsure{simplexe|simplexes}','new':r'\unsure{simplexe|simplexes|simplex}'},
 {'old':r'\unsure{facultatif|facultatifs}','new':'facultatif'},
 {'old':'Ils pourront sans doute un rôle crucial','new':r'Ils \unsure{pourront|pourraient|pourrait} \unsure{sans|donc}, \unsure{doute|donc|dans} un rôle crucial'}
], 'boxes':{},'change_updates':{},'new_doubts':[], 'remove_doubt_places':['Body line 12, simplexe(s)','Body line 19, facultatif(s)']}
def d(b,decision,evidence,ids=(),final=None):
 x={'crop':f'crops/second_scan002_{b}.png','box_coords':co[b],'decision':decision,'evidence':evidence,'changed_place_ids':list(ids)}
 if final is not None:x['final']=final
 cfg['boxes'][b]=x
d('B003','retain first','The open initial with inward low return still permits G or connected C; the uncertainty is retained with G first. F and VII are clear. Both TikZ encodings represent the left and lower frame; the established encoding is kept, without treating coordinate syntax as another source mark.')
d('B004','mark doubt','23 is still legible: the long intervening upright descends from Cf, not a third digit. The retraced 50 and 58 are retained, with an added doubt on the source state of 58. The oval encloses 110-113 and its arrow points to the gap after 23. All alternate TikZ coordinates encode that same observed arrangement. No extra comma after 23 or 59 is supplied.',['002-A01'])
d('B006','retain page; scope-only difference','The crop plainly shows the closing quotes followed by a comma. That comma is already present in the page file; the first TSV excerpt ended before it. No page change is required.',final="``algèbre des figures'',")
d('B007','retain page; scope-only difference','The separate final point follows the two quotation ticks and the underline. It is already present in the page file; the first excerpt did not include it.',final="``\\uline{atelier}''.")
d('B008','retain first','The broken marginal trace has no letter, attachment, or function as a textual dash. Its new autocontrasted enlargement does not establish deliberate writing; retain the initial exclusion as an incidental mark. No TikZ textual object is added.')
d('B011','retain first','A round isolated point is visible below and to the right of des. It has no sentence boundary or formula function here and cannot securely be identified as deliberate punctuation; the supplied rule for incidental points therefore still excludes it. The word des remains unchanged.')
d('B013','retain page; scope-only difference','The opening parenthesis and following comma are plainly visible and are both already present around densité in the page. The initial excerpt covered the word only.',final='(densité,')
d('B014','revise','The long low stroke curves down toward the insertion point before géométriques and rises at the far right; no independent second underline is visible. Treat this stroke as the insertion leader and remove the redundant underline state while keeping the word inserted before géométriques.',['002-A02'])
d('B015','retain page; scope-only difference','The right parenthesis is plain and is already present in the complete page. The initial excerpt ended after figures.',final='de figures)')
d('B018','retain first','The initial loop, shallow u, tall crossed t, next o-u and detached final r support autour. The high initial lead-in is a flourish and does not yield another word. The second reading changes certainty only; root retains the plain reading.')
d('B019','mark doubt','The crossed x is followed by a low terminal stroke before the separate full stop. Its segmentation as e, e+s, or the final arm of x remains uncertain; add simplex to the existing alternatives without silently normalising the spelling. The page already carries the final period.',['002-A03'],r'\unsure{simplexe|simplexes|simplex}.')
d('B020','retain page; scope-only difference','The full crop shows the paired quotes and the strokes of sine qua non, then At 1 à At 7 and a comma. The blind excerpt selected the numeral range only. Retain the quoted phrase and the comma already in the page.',final="``sine qua non'' At 1 à At 7,")
d('B024','resolve doubt','The tall final f has a single right shoulder ending before blank paper and the raised closing ticks. There is no separate continuing s stroke; retain singular facultatif and resolve the previous ending doubt.',['002-A04'])
d('B025','mark doubt','The p descender and ou-rr group are visible, but the low middle/end strokes do not securely distinguish -ont from -aient or -ait. The separate dot does not have an unambiguous i-stem partner. Preserve pourront as primary and explicitly retain the blind alternatives.',['002-A05'],r'\unsure{pourront|pourraient|pourrait}')
d('B026','revise and mark doubt','The opening low loop and two short rises are compressed enough to permit sans or donc; the detached descending comma at the right is clear. Retain sans first, add donc as alternative, and transcribe the comma.',['002-A06'],r'\unsure{sans|donc},')
d('B027','mark doubt','The initial looped d is plain. The flattened central run and tight final crossed/looped group favour doute but do not exclude donc or dans on this crop. The uncertainty is restored instead of relying on the familiar phrase sans doute.',['002-A07'],r'\unsure{doute|donc|dans}')
cfg['change_updates']={
 'scan002-17':{'final':r'\inserted{proprement}','scan_shows':cfg['boxes']['B014']['evidence'],'confidence':'medium','crop':'crops/second_scan002_B014.png','box':co['B014'],'against_C':True},
 'scan002-28':{'final':'facultatif','scan_shows':cfg['boxes']['B024']['evidence'],'confidence':'high','crop':'crops/second_scan002_B024.png','box':co['B024']},
 'scan002-30':{'final':r'\unsure{pourront|pourraient|pourrait}','scan_shows':cfg['boxes']['B025']['evidence'],'confidence':'low','crop':'crops/second_scan002_B025.png','box':co['B025']},
 'scan002-31':{'final':r'\unsure{sans|donc}, \unsure{doute|donc|dans}','scan_shows':cfg['boxes']['B026']['evidence']+' '+cfg['boxes']['B027']['evidence']+' The words are followed directly by un rôle; no additional infinitive is visible. Second crop: crops/second_scan002_B027.png, original box '+str(co['B027'])+'.','confidence':'low','crop':'crops/second_scan002_B026.png','box':co['B026'],'against_C':True}
}
for b,place,reading,alts in [
 ('B004','Slanted reference note, retraced 58',r'\unsure{58}',['58 with retracing','58 over an unrecoverable earlier entry']),
 ('B019','Body line 12, simplexe(s)','simplexe',['simplexes','simplex']),
 ('B025','Body line 20, verb after Ils','pourront',['pourraient','pourrait']),
 ('B026','Body line 20, word before the comma','sans',['donc']),
 ('B027','Body line 21, before un rôle','doute',['donc','dans'])]:
 cfg['new_doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low' if b!='B019' else 'medium','reason':cfg['boxes'][b]['evidence']+' New blind crop '+cfg['boxes'][b]['crop']+'; original box '+str(co[b])+'.'})
(R/'second'/f'{stem}_decisions.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
