from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan074/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
ds=copy.deepcopy(B)
for i,d in enumerate(ds):
 d['id']=f'M074-{i+1:02}'
 d['readers']={a:R[a]['decisions'][i]['reading'] for a in 'ABC'}
 d['marked_in_H']='no; supplied restoration marked' if i in (0,3) else 'no'
 d['crop']='readers/scan074/A/'+['074_A_01_disol_edge.jpg','074_A_02_preferable_overtype.jpg','074_A_02_preferable_overtype.jpg','074_A_03_apres_edge.jpg','074_A_04_lower_curve.jpg'][i]
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
ds[0].update(reading=A[0]['reading'],alternatives='partial n; partial u; partial m; partial r',scan_shows='The last visible form has a short horizontal top serif, a dark upright and a basal left foot. Its top is at the height of s/o, appreciably below the ascender of d in the same crop; a full l ascender is unsupported. The clipped right side removes the distinguishing shoulder or additional stems. All readers prefer n and retain u/r; A also retains m, whose first stem is equally compatible with the remnant. Main preserves those four alternatives and supplies no following s. H explicitly marks ns as editorial restoration, rather than as visible ink.')
ds[1]['scan_shows']='A separate acute diagonal is visible above the corrected position, with a round e bowl and horizontal middle stroke below it. The live r contributes a heavier upright, foot and hooked shoulder. Main confirms C and all three readers: the underlying é remains readable and is retained as deleted. H gives the final r without this underprint.'
ds[2]['scan_shows']='The live a has its own bowl and right stem, while an extra upper serif/shoulder and upright are visible within the left portion. These support an underlying r, but the superposition hides the right join and prevents a secure full-letter separation. Main retains C’s explicit doubt, as all three readers do. H gives only a.'
ds[3]['scan_shows']='After the grave-accented è, the surviving left part of the final letter includes an upper curved turn, narrow middle and lower dark curved portion. The right edge clips it, but the remaining two levels of curvature identify s. Main confirms all three readers and C. H marks the whole s as supplied; the collation records the difference in source status, not a spelling change.'
ds[4].update(reading=C[4]['reading'],scan_shows='The narrow irregular trace slopes down and right from a short raised nub, steepens and rounds downward at the right end, then hooks a short distance left at its foot. Its shape is recoverable; no letter or signature can be read. A and B retain C’s basic contour, while C preserves its lower-right position and fuller aspect ratio. Main adopts C’s anchored rendering. The dark patches and pale border do not decide between pen ink and an incidental surface trace, so the previously unmarked graphic gains an explicit uncertainty. C’s context table already raised that material doubt; H omits the shape.')
s=(O/'readers/scan074/C/reading.tex').read_text().replace(C[0]['reading'],A[0]['reading'])
(O/'pages/B37-04_37_scan074.tex').write_text(s.rstrip()+'\n\\clearpage\n')
inv=copy.deepcopy(R['C']['inventory'])
for x in inv:
 if x['kind']=='drawing':x['hand']='unnamed hand if authored; surface-trace origin unresolved'
notes="""One unsigned typescript letter leaf, headed ‘Massy le 3.11.1970’ and addressed ‘Cher Ferrand,’. The writer asks whether SGA 6 XI can be received ‘d’ici fin décembre’, considers publishing SGA 6 without that exposé, and asks where a separate ‘article d’exposition’ might appear so the introduction can refer to it. It closes ‘Bien cordialement’. There is no title, signature, author’s own page number or explicit total page count; archive number 73 is recorded as a comment. No mathematical argument or explicit author doubt mark appears.

The right edge leaves diso plus an x-height stem, recorded as n/u/m/r, and clips a still recognizable s in après. H explicitly supplies ns and s respectively; the first is not completed from the intended wording, and the second is read from surviving strokes. Both explicit C text doubts remain uncertain, with revised alternatives at the edge. The two overprints in préférable are preserved: é is readable under r, and r remains tentative under a. The detached lower-right curve is drawn with an explicit uncertainty about its material origin; C’s context table already noted this issue. No proof or computation was performed."""
notation=copy.deepcopy(R['A']['notation']);notation[2]['latex']=ds[4]['reading']
out=dict(scan=74,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=R['A']['math_reading_decisions'],notation=notation,abbreviations=R['A']['abbreviations'],slips=R['A']['slips'],check_events=[],main_crops=[])
(O/'decisions/scan074.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nScan 074: A/B/C returned five mandatory loci and made 4/3/3 crops. Main viewed A’s four crops, with one crop serving the two adjacent overprints, and made none. The new m alternative at the clipped edge was retained because its first x-height stem cannot be separated from the other partial forms. H’s supplied-letter markers are distinguished from explicit doubt markers in the collation. The material doubt mentioned only in C’s context for the curve is now marked in the text. No brief change was required.\n')
print('Wrote scan 074: five H differences, two C changes, all explicit C doubts reviewed.')
