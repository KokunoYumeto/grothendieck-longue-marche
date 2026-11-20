import json
from pathlib import Path
report={
 'scan':56,
 'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan056_a',
 'started_utc':'2026-11-20 03:36:43 UTC',
 'finished_utc':'2026-11-20 03:39:36 UTC',
 'source_dimensions':[1675,2157],
 'rows':[
  {'id':'M1103','scan':56,'decision':'undecided','reading':r'\unsure{est}','what the ink shows':'A compact word is covered by dense black retracing. An upright remains at the right, but its junction with the overwrite does not securely separate the proposed e, s and t.','crop':[1135,110,1230,170],'confidence':'low'},
  {'id':'M1104','scan':56,'decision':'undecided','reading':r'l\unsure{e} p\unsure{r.}','what the ink shows':'The initial tall closed loop of l and the later looped descender of p remain distinct. The connecting e and the end of the abbreviated group, including its proposed stop, are swallowed by the horizontal cancellation.','crop':[190,300,370,375],'confidence':'low'},
  {'id':'M1105','scan':56,'decision':'undecided','reading':r'cel\unsure{a se vo}it','what the ink shows':'At the left an open c, low linked e and tall looped l remain visible; at the right there is a detached dot followed by the upright and cross-stroke of t. The intervening baseline letters are crossed through or too faded to confirm.','crop':[1010,300,1425,365],'confidence':'low'},
  {'id':'M1106','scan':56,'decision':'undecided','reading':r'\unsure{suivant}','what the ink shows':'The deleted line below the inserted bien connu is a thick continuous cancellation with only a few isolated upper and lower protrusions. These remnants do not separate the proposed letters of suivant.','crop':[1180,353,1405,419],'confidence':'low'},
  {'id':'M1107','scan':56,'decision':'undecided','reading':r'\unsure{et $h$}','what the ink shows':'The first short group has a flattened loop and an oblique stroke; the later group retains one upright ascender. The long cancellation covers their joins and the proposed h arch, preventing a secure reading of either group.','crop':[190,420,510,495],'confidence':'low'},
  {'id':'M1108','scan':56,'decision':'first','reading':r'$U$','what the ink shows':'The character has two full-height stems joined by a deep rounded bowl, with a short upper-right exit. It matches the tall capital U forms in the preceding line; the neighboring lowercase u in u=Uh is a much shorter baseline bowl.','crop':[860,716,921,772],'confidence':'high'},
  {'id':'M1109','scan':56,'decision':'first','reading':'1','what the ink shows':'Below the sum is a single long near-vertical stroke with a slight top hook and no detached dot. The nearby left-hand sum index i has a separate round dot and a shorter hooked lower stroke.','crop':[1198,1014,1220,1041],'confidence':'medium'},
 ],
 'views':[],
 'other_errors':[],
 'patterns':[
  {'name':'Full-height capital U versus shallow lowercase u','marks':['M1108'],'description':'In the immediately preceding line, source box [270,645,725,715], capital U has two tall stems, whereas u in u=Uh has a short shallow bowl; M1108 shares the tall capital form.'},
  {'name':'Separated dot in a nearby summation index','marks':['M1109'],'description':'The summation index in source box [325,940,500,1050] has a distinct detached dot; M1109 instead shows a continuous upright stroke without a visibly separated dot.'},
 ],
 'notes':['All 19 current-page mark boundaries M1103–M1121 were read in the page source; only assigned M1103–M1109 are submitted. No unmarked correction is proposed.','M1109 was sent to the coordinator as a selective peer target because an undotted i remains a possible competing interpretation; the present own-ink preference is literal 1.','M1104 and M1105 retain uncertainty inside the supplied candidate rather than completing cancelled letters. The original surrounding deletion layers are left to reconciliation.','Initial primary review completed without waiting for peer review.']
}
views=[
 ('full',[0,0,1675,2157],[834/1675,1075/2157],1,'Locate all current-page mark regions.'),
 ('upper',[150,75,1635,530],1.5,1,'Read upper lines and locate M1103–M1107.'),
 ('formulas',[180,575,1635,1050],1.5,1,'Read formula context for M1108–M1109.'),
 ('m1103',[1080,105,1240,165],4,1,'Inspect deleted short word after orthonormal.'),
 ('m1104',[180,295,380,375],3,1,'Inspect deleted initial loop and abbreviation.'),
 ('m1105_m1106',[1000,290,1515,440],2.5,1,'Distinguish adjacent cancellation and insertion layers.'),
 ('m1107',[185,425,415,500],3,1,'Inspect cancelled group before un op.'),
 ('m1108',[835,655,1040,800],3,1,'Inspect letter before the expansion.'),
 ('m1109',[1135,935,1280,1040],4,1,'Inspect index under the right-hand summation.'),
 ('sum_i_compare',[325,940,500,1050],3,1,'Compare dotted i under neighboring sum.'),
 ('deleted_words',[1000,300,1425,380],4,1.7,'Separate visible M1105 fragments from cancellation.'),
 ('m1107_wide',[190,420,510,495],4,1.3,'Include complete final cancelled ascender and following un.'),
 ('m1103_contrast',[1135,110,1230,170],6,1.7,'Check whether terminal upright can be separated from overwrite.'),
 ('m1104_contrast',[190,300,370,375],5,1.4,'Inspect l loop, p descender and obscured abbreviation ending.'),
 ('m1106_detail',[1180,353,1405,419],5,1.4,'Inspect deleted layer below bien connu.'),
 ('u_compare',[270,645,725,715],3,1,'Compare same-line lowercase u and capital U forms.'),
 ('m1105_left',[1010,300,1160,360],5,1,'Inspect opening c/e/l fragments.'),
 ('m1105_middle',[1155,300,1310,360],5,1,'Inspect faded intermediate letters.'),
 ('m1105_right',[1295,300,1425,360],5,1,'Inspect terminal detached dot and t.'),
]
for name,box,scale,contrast,purpose in views:
 report['views'].append({'path':f'work/scan056_a_{name}.'+('jpg' if name=='full' else 'png'),'box':box,'scale':scale,'contrast':contrast,'purpose':purpose})
text=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
for name in ['work/scan056_a.initial.json','work/scan056_a.json']:
 Path(name).write_text(text)
print('Saved 7 rows: 2 first; 5 undecided. 19 inspected views.')
