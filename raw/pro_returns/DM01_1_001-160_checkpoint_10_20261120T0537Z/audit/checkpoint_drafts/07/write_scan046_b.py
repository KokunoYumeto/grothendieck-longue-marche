import json
from pathlib import Path
p={
 'scan':46,
 'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan046_b',
 'started_utc':'2026-11-20T02:41:38+00:00',
 'finished_utc':'2026-11-20T02:43:35+00:00',
 'rows':[
  {'id':'M0954','scan':46,'decision':'first','reading':'fait','what the ink shows':'The word immediately before the obscured middle cluster has a tall f with a lower loop, a low joined ai stroke, and a sharply crossed terminal t. The f and terminal t agree with the uncanceled fait later on this page; a separate short canceled word precedes it.','crop':[420,810,550,905],'confidence':'medium'},
  {'id':'M0955','scan':46,'decision':'undecided','reading':r'\illegible{2}','what the ink shows':'Between fait and the barred E, low separated humps and a right-hand dot remain below an upper retraced cancellation. The two long cancellation strokes mask the letter bodies and do not permit a secure two-word recovery.','crop':[545,800,915,915],'confidence':'low'},
  {'id':'M0956','scan':46,'decision':'undecided','reading':r'\illegible{3}','what the ink shows':'After the barred E, the deleted span retains a few low humps, a loop dropping beneath the cancellation, and a later tall upright. Almost all connecting letter bodies coincide with the two deletion lines, so the three words cannot be distinguished securely.','crop':[975,845,1445,920],'confidence':'low'},
  {'id':'M0957','scan':46,'decision':'undecided','reading':r'\unsure{définie}','what the ink shows':'Below the insertion, the canceled word retains a looped initial d-like stroke and a tall f with a lower loop. The thick horizontal cancellation covers the accent and remaining low letters, so définie remains plausible but not fully demonstrable.','crop':[425,910,655,970],'confidence':'low'},
  {'id':'M0958','scan':46,'decision':'first','reading':'encore','what the ink shows':'The small interlinear word above the deleted band begins with an open e, continues through angular low n/c strokes and a rounded o, then a short r join and closed terminal e. It is separate from the cancellation and has no tall initial d or f.','crop':[510,895,660,950],'confidence':'medium'},
  {'id':'M0959','scan':46,'decision':'undecided','reading':r'\unsure{isométrie}','what the ink shows':'The canceled word below the insertion has an initial dot and short upright, several mid-word tops, and a late raised stem and dot. The heavy descending strike conceals the o/m bodies and most of the ending; it supports the proposed isométrie only incompletely.','crop':[1485,1525,1680,1595],'confidence':'low'}
 ],
 'views':[],
 'other_errors':[
  {'scan':46,'place':'Canceled line after the unstruck qui and immediately before M0954; source insertion boundary outside every listed mark.','the reading':r'qui \deleted{','what the ink shows':'A further short canceled word at [305,830,400,895] precedes the tall-f fait of M0954. Its hooked initial, flat low join and final dot resemble the uncanceled qui at [775,1400,855,1450], while an additional qui is visibly present at the previous line end [1545,805,1635,855]. This suggests an omitted repeated canceled qui; the concern needs peer review and does not alter any marked span.'}
 ],
 'patterns':[
  {'name':'Baseline obliteration by double cancellation','marks':['M0955','M0956'],'description':'The long pair of deletion strokes coincide with the handwritten baseline; surviving ascenders, dots and descenders do not preserve enough connected letter bodies to recover the obscured spans.'}
 ],
 'notes':'All six assigned marks inspected personally without OCR. Actual source dimensions are 1690 by 2713. All scan046 source mark boundaries were read before noting the possible omitted repeated qui; this concern is separate from mark replacements. M0955–M0957 and M0959 remain uncertain after close views. Initial report saved before any peer-driven revision. The elapsed interval includes tool processing, not continuous active reading.'
}
views=[
 ('full',[0,0,1690,2713],[834/1690,1075/2713],1,'Full-page locator; this initial thumbnail has nonuniform reduction.'),
 ('cancelled',[240,750,1635,1000],2,1,'Locate M0954–M0958 and their cancellation layers.'),
 ('cancel_left',[285,810,930,930],4,1.5,'Inspect surviving words before barred E.'),
 ('cancel_right',[885,815,1485,945],4,1.5,'Inspect surviving descenders and upright after barred E.'),
 ('def_encore',[410,875,650,968],5,1.3,'Separate canceled définie band and upper encore insertion.'),
 ('isometrie',[280,1355,1685,1605],2,1,'Locate M0959 with surrounding sentence and insertion.'),
 ('isometrie_detail',[1465,1475,1685,1595],5,1.3,'Inspect dotted letters and cancellation in M0959.'),
 ('fait_comparison',[1230,1380,1395,1500],4,1,'Same-page uncanceled fait letter comparison.'),
 ('cancel_first',[285,820,505,915],5,1,'Separate short initial deleted word from following f-stem.'),
 ('cancel_middle',[420,790,940,915],4,1,'Inspect fait and following obscured span boundaries.'),
 ('line_begin',[235,735,700,985],3,1,'Check three text baselines and deleted line beginning.'),
 ('par_compare',[620,1620,1050,1770],3,1,'Compare the hooked initial of par with the canceled first word.'),
 ('fait_isometrie_context',[1140,1360,1685,1595],3,1,'Compare uncanceled fait and nearby M0959 cancellation.'),
 ('qui_boundary',[1330,745,1685,940],4,1,'Verify unstruck qui at preceding line end.'),
 ('qui_compare',[750,1385,870,1465],5,1,'Same-page uncanceled qui comparison for omitted word concern.'),
 ('fait_target',[420,810,550,905],5,1,'Resolve M0954 f loop and crossed terminal t.'),
 ('encore_target',[510,895,660,940],6,1,'Inspect all letters of the encore insertion.'),
 ('definie_target',[425,915,655,970],5,1,'Check remaining d/f strokes and masked ending of M0957.')
]
for name,box,scale,contrast,purpose in views:
 p['views'].append({'path':f'work/scan046_b_{name}.'+('jpg' if name=='full' else 'png'),'box':box,'scale':scale,'contrast':contrast,'purpose':purpose})
Path('work/scan046_b.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
Path('work/scan046_b_initial.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
print('Saved work/scan046_b.json and preserved work/scan046_b_initial.json; 6 rows, 18 inspected views.')
