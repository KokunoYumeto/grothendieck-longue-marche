"""Record root's completed comparisons of the previously viewed source crops."""
from pathlib import Path
from datetime import datetime, timezone
import json

B=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
np=B/'notation_crosscheck.json'; n=json.loads(np.read_text())
assert n['status'].startswith('in progress')
n['status']='complete: all 23 independent audits and root crop decisions recorded'
n['review_completed_utc']=stamp
for name in ['149_scan073_B19_second.png','149_scan076_B09_second.png','149_scan077_B09_second.png','149_scan077_B17_second.png','149_scan078_B19_second.png','149_scan078_B20_second.png','149_scan078_B21_second.png','149_scan078_B16_second.png','149_scan078_B22_second.png']:
 path='crops/'+name
 assert (B/path).is_file()
 if path not in n['root_reopened_existing_crops']:n['root_reopened_existing_crops'].append(path)
n['observation']='Every supplied page has completed its independent reading and root adjudication. The cross-page decisions concern the recorded contours and positions. Clearer neighboring forms serve as explicit comparisons; unresolved local forms retain their own alternatives. No automatic substitution across pages was made, and frozen audit inputs/returns remain unchanged.'
n['shorthand_final']='The pronounced entrance cup, central cusp and low right return beneath a separate upper bar support barred m at 067 P18, 070 P03, 071 P04, 072 P09 and 076 P11. The flattened lower contours at 055 P09, 057 P14, 058 P09, the 059 margin, the five 060 occurrences, 061 P01 and 077 P16 remain equals/barred-m alternatives. The two post-audit changes on 055/071 are dated in their reports; 077 was reopened during its own audit. No occurrence is expanded to the full word même in the transcription.'
n['Pi_comparison']='054 P10 has broad caps and long essentially straight legs. Both 076 B09 forms likewise retain broad caps and straight descending legs, supporting Pi. 060 P01 has a distinctly curved right foot; the three 078 B19 forms also retain shorter curved right returns, supporting pi. The compressed oblique 073 B19 form does not expose that foot securely and remains pi/Pi. Each index, bar and argument retains its local reading; this contour correspondence does not supply an identification of the source groups.'
n['nested_index_comparison']='070 P09 retains eta/K at all five recorded occurrences: a short arched/branched body is crossed by the attachment stroke. 073 P10 retains eta/K/kappa in its very compressed lower index. The continuous arch and low right return at 074 P02 support eta there; the upright and two right branches at 075 P06 support K there. Their blind decisions preserve these local differences in stroke evidence, without filling the unclear indices from nearby formulas.'
n['J_superscript_comparison']=r'The two tiny dark raised marks in 077 P08 / B09 have a short upright or wedge-like extent. The more complete numeral 1 and hollow 0 in B10 supply the direct comparison. The two small marks remain \unsure{\bullet|0|1|\prime}: their tiny filled bodies do not settle a point, closed zero, short one or prime. C’s point/zero and H’s one remain explicit alternatives; no resolved material correction is counted at those two signs.'
n['k_comparison']=r'The paired forms in 078 B20 and B21 both have a tall stem with two right branches below its top. Both retain \unsure{k|\kappa|K}; the paired fork contours supply no secure case/alphabet decision. The blind f alternative is recorded in the fixed return, while the two right arms and absence of the proposed f loop sequence support the retained alternatives.'
n['margin_boundary_comparison']='078 B22 ends at original x=357. The complete original and overlapping B16 locate the terminal exclamation stem and its separate point around (384,1895), beyond that right edge. The longer lower edge stroke around x=346,y=1930–1977 continues into the L of Le in B16. The note retains its actual terminal exclamation and records both accent doubts.'
np.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')

ep=B/'final_editorial.json'; e=json.loads(ep.read_text())
e['notation_review']="""The entries below record visible forms and the manuscript's own statements about them. All 23 pages have completed the independent image-only reading and root crop adjudication. The explicit comparisons are recorded in `notation_crosscheck.json`; the fixed readings and their decisions remain in `second/`.

The two-level prose shorthand reads barred m at the recorded occurrences on scans 067, 070, 071, 072 and 076: beneath a separate upper bar, the lower contour has an entrance cup, central cusp and long right return. The flatter contours on 055, 057, 058, 059, 060, 061 and 077 remain equals/barred-m alternatives. The local readings are retained without expanding the abbreviation in the transcription. The round Gamma mark on 061 keeps its actual lower or raised position. Both natural signs on 066 have matching offset bars and opposing stems. The two tiny raised J marks in the canceled display on 077 remain point/zero/one/prime alternatives; their uncertainty survives the comparison with the clearer 1 and hollow 0 elsewhere on that leaf.

The broad caps and long straight legs at 054 and 076 support the listed Pi readings. The curved right returns at 060 and 078 support the listed pi readings. The compressed oblique form on 073 remains pi/Pi. The nested eta/K forms on 070 and eta/K/kappa on 073 also remain open after comparison with the clearer arch on 074 and forked K on 075. The paired tall forked letters on 078 retain k/kappa/K in both places. These observations preserve each written index, bar and argument separately.

For witness wrappers excluded from the material counts, `accounting_review.json` and the per-page uncounted observations retain the occurrence key, witness expression, final expression and source contour. For example, the recorded two-lobed E body at one fixed coordinate is represented by H's mathcal-E wrapper and the final E; the original witness field retains the wrapper. On 078 the three J wrappers map individually to the same three hooked bodies in the display, and the two U wrappers map individually to the same two lower curves and rising right limbs. These are correspondences between transcription encodings of specified ink occurrences; no additional map between the mathematical objects is supplied."""
e['hand_review']="""
## Cross-page limits and comparisons

Each observation retains its local scope. Short terminal returns are read with the neighboring letter bodies, and the position of an accent, stop or index is recorded independently. The broad Pi forms on 054 and 076, the curved right foot of pi on 060 and 078, and the unresolved compressed form on 073 have been compared directly. Scan 061 preserves the two heights of the round Gamma mark. The paired natural signs on 066 have matching offset bars and opposing stems; the two much smaller raised J marks on 077 remain point/zero/one/prime alternatives after comparison with its clear 1 and hollow 0.

For nested U indices, the arched form on 074 P02 and branched K on 075 P06 supply explicit local comparisons. The shorter intersected forms on 070 P09 and 073 P10 remain uncertain after their blind audits. Both forked letters on 078 keep k/kappa/K. The shorthand comparison resolves the pronounced cup/cusp form on 071 while preserving the flat forms on 055 and 077 as open; dated decisions retain the original fixed audit record.

On 078 the frozen margin box clips the terminal exclamation at its right edge. The original page and overlapping B16 locate that punctuation separately from the lower edge stroke, which continues into the L of Le. This boundary correspondence is recorded with its coordinates. Abbreviation expansions remain confined to the abbreviation list.
"""
e['sheet_feedback']="""The page references in the table count each material decision place once under its primary category. Several places involve more than one feature, such as an inserted abbreviation whose attachment and stop both need reading; one primary category prevents duplicate totals. Audit changes of certainty alone remain in the audit tables and doubts list, outside the material totals.

Useful additional examples for the sheet are the paired raised natural signs at 066 P13/P14, with offset bars and opposing stems, and the unresolved tiny raised marks on J at 077 P08/B09. At the latter two positions, point/zero/one/prime remain alternatives despite comparison with the same page's clearer 1 and hollow 0. The broad symbols-and-indices category covers these places; the local contour records show why an apparently solid mark can remain undecided.

The recurring shorthand illustrates the value of retaining the lower contour: an entrance cup and cusp support barred m at five listed page occurrences, while flatter examples remain equals/barred-m. The other repeated difficulties have direct counterparts in the supplied sheet: insertion leaders meeting formula indices; short returns resembling extra letters or stops; Pi height and case; round marks at different index levels; overwritten S/T; cancellations with a live following comma; and physical word divisions. Their decisions and scope are recorded in the changes and hand logs.

A further boundary example is the oblique note on 078: its frozen crop clips the actual terminal exclamation, and a different lower edge stroke belongs to the main paragraph's L. The original page and the overlapping B16 identify both contours without assigning the same stroke to two text elements. This is recorded as a crop-boundary observation rather than a new handwriting rule."""
e['completed_utc']=stamp
ep.write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
with (B/'progress.log').open('a') as f:f.write(f'final cross-page notation review completed {stamp}: all 23 independent audits recorded; local unresolved contours retained; no additional mathematical check\n')
print(json.dumps({'notation_review_completed_utc':stamp}))
