import json
from pathlib import Path
rows = [
 dict(id='M0686',scan=35,decision='first',reading=r'\mathcal H', **{'what the ink shows':'The letter has a long rising left shoulder, two narrow joined loops and a right downstroke, like the H in the preceding X\u2032 definition. The nearby X has opposing curved arms and a transverse join instead.', 'crop':[1240,1010,1510,1145],'confidence':'high'}),
 dict(id='M0687',scan=35,decision='first',reading=r'\prec', **{'what the ink shows':'A looped left point opens into separate upper-right and lower-right arms. There is no separate lower wavy or horizontal stroke for lesssim.', 'crop':[875,1260,1130,1380],'confidence':'high'}),
 dict(id='M0688',scan=35,decision='first',reading='implique', **{'what the ink shows':'A short initial i stroke is followed by a low connector, a deep p/l turn and the descending q-shaped turn before the short final e. The same-page impliquerait has the same initial connected turns.', 'crop':[930,1470,1180,1570],'confidence':'medium'}),
 dict(id='M0689',scan=35,decision='first',reading='(t)', **{'what the ink shows':'Under the crossing strokes, a curved left parenthesis, central upright t and closing bowed stroke remain distinguishable. The cancellation overlaps the t crossbar.', 'crop':[670,1720,1310,1825],'confidence':'medium'}),
 dict(id='M0690',scan=35,decision='first',reading='(t)', **{'what the ink shows':'The right-hand deleted group retains a separate curved opening stroke, a central tall t with a transverse stroke and a right closing hook. Diagonal deletion strokes cross the middle.', 'crop':[670,1720,1310,1825],'confidence':'medium'}),
 dict(id='M0691',scan=35,decision='first',reading='2', **{'what the ink shows':'The small leading glyph has a bent upper stroke descending to a short rightward foot. It has no second diagonal crossing through its middle as x would.', 'crop':[1310,1800,1500,1880],'confidence':'medium'}),
 dict(id='M0692',scan=35,decision='undecided',reading=r'\sqrt{\unsure{A}}', **{'what the ink shows':'The radical\u2019s low check and long rising arm survive at the left. The following A-like diagonals are merged with broad cancellation strokes, so the radicand cannot be secured.', 'crop':[1310,1800,1500,1880],'confidence':'low'}),
 dict(id='M0693',scan=35,decision='undecided',reading=r'\unsure{A\in\underline b}', **{'what the ink shows':'Crossing strokes cover the putative A, membership curve and right-hand looped letter. Several upright and curved remnants survive, but their boundaries and a distinct underline are obscured.', 'crop':[1500,1780,1738,1925],'confidence':'low'}),
 dict(id='M0694',scan=35,decision='first',reading='positif', **{'what the ink shows':'The word begins with a long p down-and-up turn, continues through a low connected middle with an i dot, and ends in a tall f with a descending stem. Its upper end touches the deleted note above.', 'crop':[1360,1860,1660,1960],'confidence':'medium'}),
 dict(id='M0695',scan=35,decision='first',reading='preuve', **{'what the ink shows':'In the rotated margin, a long initial p descender leads into a low joined r/e group; two small rises and a final trailing e stroke complete preuve. There is no extra separately written word.', 'crop':[15,735,170,965],'confidence':'medium'}),
 dict(id='M0696',scan=35,decision='undecided',reading=r'\unsure{\varphi|\Phi}', **{'what the ink shows':'The first inserted glyph has a broad open cup and a central stem extending above and below its junction. No upper closing stroke is visible, so its form does not securely distinguish the proposed phi variants; it is also psi-shaped.', 'crop':[10,100,125,480],'confidence':'low'}),
 dict(id='M0697',scan=35,decision='undecided',reading=r'\unsure{\varphi|\Phi}', **{'what the ink shows':'The second inserted glyph has a shallow upturned bowl crossed by a tall central stem, with no closed oval. Its especially flat cup leaves the phi variants unresolved and permits a psi-shaped reading.', 'crop':[10,100,125,480],'confidence':'low'}),
 dict(id='M0698',scan=35,decision='first',reading='1+|A|',candidates=['1+|A|'], **{'what the ink shows':'The lower-right index has a separate initial 1 and plus, then a single A between two upright bars. The A\u2019s center is overtraced, but both legs and its surrounding bars remain visible.', 'crop':[10,100,125,480],'confidence':'medium'}),
 dict(id='M0699',scan=35,decision='first',reading='Équicontinuité', **{'what the ink shows':'An accented capital É is followed by the descending q turn and an open c; the connected continuation has dotted i strokes, crossed t forms and a final accented ending. The long middle connectors compress several letters.', 'crop':[600,1930,975,2040],'confidence':'medium'}),
]
viewdata = [
 ('full.jpg',[0,0,1738,2223],0.6,1,0,'Locate assigned marks on this page.'),
 ('relations.png',[950,960,1550,1385],1.7,1,0,'H/X definitions and comparison relation.'),
 ('cor1.png',[315,1450,1290,1580],1.7,1,0,'Locate implique in Corollaire 1.'),
 ('cor2_3.png',[310,1690,1725,1975],1.6,1,0,'Locate deleted arguments and right-hand cancellation.'),
 ('cor5.png',[345,1950,1700,2060],1.6,1,0,'Locate Équicontinuité.'),
 ('margin.png',[15,190,175,2050],1.5,1,90,'Locate side annotation; this rotation leaves it inverted.'),
 ('M0687.png',[875,1260,1130,1380],3,1,0,'Resolve relation arms and absent lower stroke.'),
 ('M0688.png',[930,1470,1180,1570],3,1,0,'Inspect implique letter turns.'),
 ('M0689_90.png',[670,1720,1310,1825],2.5,1,0,'Inspect both deleted parenthesized arguments.'),
 ('M0691_94.png',[1355,1790,1738,1950],3,1,0,'Inspect cancellation and positif; leading numeral partly clipped.'),
 ('margin_reading.png',[10,185,160,2025],2.5,1,-90,'Read side annotation in its proper orientation.'),
 ('M0699.png',[600,1930,975,2040],3,1,0,'Inspect accented title and joined letters.'),
 ('M0691_93_full.png',[1280,1790,1738,1915],4,1,0,'Inspect complete deleted note with leading numeral.'),
 ('M0694.png',[1360,1860,1660,1960],3,1,0,'Inspect positif and its terminal f.'),
 ('M0695.png',[15,735,170,965],3,1,-90,'Inspect preuve in the margin.'),
 ('M0696_98.png',[10,180,180,720],3,1,-90,'Inspect inserted symbols; rightmost index partly clipped.'),
 ('M0686.png',[1240,1010,1510,1145],3,1,0,'Inspect target H loops and neighboring Y.'),
 ('inserted_phi.png',[10,100,125,480],5,1,-90,'Inspect both open bowls and complete right-hand subscript.'),
 ('radical.png',[1310,1800,1500,1880],6,1.4,0,'Inspect numeral, radical check and obscured radicand.'),
 ('membership.png',[1500,1780,1738,1925],5,1.4,0,'Inspect obscured membership phrase and underline.'),
 ('comparison_words.png',[315,1260,665,1360],3,1,0,'Compare same-page impliquerait beginning.'),
 ('right_context.png',[1260,1715,1738,1985],3,1,0,'Separate canceled note from positif A and following insertion.'),
]
obj = dict(scan=35,reader='GPT-6 Astra Pro; effort not exposed; run /root/scan035_b',started_utc='2026-11-20T01:28:11Z',finished_utc='2026-11-20T01:30:33Z',rows=rows,views=[dict(path='work/views035_b/'+name,box=box,scale=scale,contrast=contrast,rotation=rot,purpose=purpose) for name,box,scale,contrast,rot,purpose in viewdata],other_errors=[],patterns=[dict(name='Open bowl in inserted phi candidates',marks=['M0696','M0697'],description='Both inserted margin symbols have open bowls and stems projecting above and below; neither supplies the closed loop seen in several main-text phi forms. Their letter identification remains unresolved pending the requested independent check.')],notes=['Primary submission covers only M0686–M0699. All 22 logged images were personally viewed; no OCR was used.','M0692 retains only radicand uncertainty; M0693 remains wholly uncertain because cancellation obscures the symbol boundaries.','Independent review was requested through the coordinator for the concrete open-cup/closed-loop issue at M0696 and M0697, with adjacent M0698 available in the same crop. This is the preserved preliminary own-ink report before reconciliation.'])
Path('work/scan035_b.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
Path('work/scan035_b.initial.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('work/scan035_b.json: 14 rows; 10 first, 4 undecided; 22 inspected views')
