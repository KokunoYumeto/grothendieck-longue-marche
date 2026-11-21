from pathlib import Path
import json
R=Path(__file__).parent
p=R/'report.json';r=json.loads(p.read_text());H=Path('packets/025/H.tex').read_text();C=Path('packets/025/C.tex').read_text()
patch={
'C025-R01':r'\Sigma_{i}^{-}', 'C025-R03':r'E_{i}', 'C025-R04':r'\bigcup_{\alpha\in K}\widehat{\Sigma}_{\alpha}^{+}',
'C025-D02':r'\Sigma_{i}^{-}', 'C025-D04':r'E_{i}', 'C025-D07':r'\bigcup_{\alpha\in K}\widehat{\Sigma}_{\alpha}^{+}',
'C025-D08':r'\widehat{\Sigma}_{\alpha}^{+}', 'C025-D10':r'E_{\alpha}', 'C025-D12':r'\Sigma_{\alpha}^{+}',
'C025-D15':r'\Sigma_{\alpha}^{+}', 'C025-D16':r'\Sigma_{i}^{+}', 'C025-D17':r'\Sigma_{i}^{-}',
'C025-D18':r'\{\alpha\in I\mid E_{\alpha}\subset\Sigma_{\alpha}^{-}\}'
}
for d in r['differences']:
 if d['id'] in patch:d['H']=patch[d['id']]
 if d['H'] is not None:
  d['H_anchor_literal']=d['H'];d['H_anchor_found_in_packet']=d['H'] in H
 if d['C'] is not None:d['C_anchor_literal']=d['C'];d['C_anchor_found_in_packet']=d['C'] in C
 if d['id'] in ['C025-R01','C025-R04','C025-D07']:
  d['H_apparatus_literal']=H[H.index(r'\note{dans'):H.index('\n\nIl faut')]
# C row1 uses full source occurrence to avoid reporting a shortened cross-index state as witness text.
for d in r['differences']:
 if d['id']=='C025-R01':
  d['C']=r'\deleted{\unsure{E|I}}\Sigma_i^-';d['C_anchor_literal']=d['C'];d['C_anchor_found_in_packet']=d['C'] in C
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
sm=json.loads((R/'source_map.json').read_text())
lines=['# Scan 025 — independent reader C','',
'The sheet writes the opening conditions on U_s, a large crossed cup expression with a hatted Sigma and two adjoining conditions. The next paragraph begins “Il faut voir que” and ends with “Je dis que” followed by an unfinished right-open set expression. Final alpha is retained. No mathematical proof check was performed.','',
'## Line-by-line reading audit','',
'| Physical line or region | Proposed reading and visible state | Status |',
'| --- | --- | --- |',
'| Top cancelled line | “Soit en effet”, with one long slightly rising crossing run (G01). | Wording and deletion firm. |',
'| Opening line | “Si on a”, U_s subset the complete corrected Sigma (S01), comma, barred U_s, corrected cap (G02), E index (E01), nonemptiness, comma. | a has a small light counter; predecessor E/I, short Sigma index i/prime, cap state, E index i/j and detached-head roles remain qualified. |',
'| End of opening line | Cancelled “et si” (G03), followed by live “alors”. | et si firm against H’s ainsi; its sloping cancellation retained. |',
'| Next left fragment | Complete proposed “on a” (G04), drawn as three separated reduced components. | Whole phrase remains qualified; nonlexical-strokes alternative retained. |',
'| First display line | U_s = X setminus G05, lower alpha in K, complete hatted Sigma_alpha plus (S02); reduced où (G06), i in K subset I. | Cross present; union correction state retained. S02 small upper-alpha traces and G06 whole word/raised-mark attachment qualified. |',
'| Second display line | forall alpha in K, Sigma_alpha plus (S03), membership pi0(X setminus E_alpha), crossed endpoint G07. | pi0 and parentheses firm; E top-arm role qualified; deleted les/K/tel retained. No following comma. |',
'| Third display line | G08, live les, Sigma_alpha plus (S04), mut with raised t and a stop, disjoints. | Entire G08 cancelled/live alternatives preserved; raised t and stop resolved. Right-edge s survives; no separate terminal period is visible. |',
'| First prose line | Il faut voir que; deleted K and raised inserted K setminus braced i (G09); et les; Sigma_alpha plus (S05); complete parenthetical alpha in K setminus braced i. | Replacement and parenthetical firm; long curved run keeps guide/cancellation alternatives; S05 head role qualified. |',
'| Second prose line | sont determinés/déterminés/determines en termes de i et de. | Three complete word candidates retained; full preceding que descender was included in the only crop. |',
'| Third prose line | Sigma_i plus (S06), i.e., Sigma_i minus (S07), point; Je dis que. | Both i.e. points and final point firm. Each later Sigma retains its own short-index/head-role alternatives in the record under the first printed qualifier. |',
'| Final display | K setminus braced i = left brace alpha in I, tall condition stroke, E_alpha subset Sigma_alpha minus (S08). | Final alpha, minus and joined faint head return firm. Right closing brace and endpoint punctuation absent in inspected continuation. |',
'| Lower sheet | Faint interrupted curve M01; two dark flecks M02; archive 24 at bottom left. | Shapes locally qualified with hand/role/surface origin unresolved. Archive numeral firm, hand undetermined; comment only. |','',
'## Original C doubt rows','',
'Exactly eight rows occur under the supplied Doubtful readings heading. The notation table and two slips entries remain separate context.','',
'| Original row | Scope | Decision |', '| --- | --- | --- |']
for row in r['C_doubt_rows']:
 lines.append('| '+row['source_row_id']+' | '+row['physical_scope']+' | '+row['status']+' |')
lines += ['', 'The raised-t row is resolved; the other seven original rows remain qualified. Row 4 retains its whole operator state even though the cross itself is clear. Row 6 retains all three original cancelled candidates and adds complete live states. Row 8 keeps the whole-word scope and all three original spellings.','',
'## Complete local proposals','',
'These are this reader’s own complete candidate descriptions. The literal TeX, including qualifications, phantom state annotations, ownership, paths and exact offsets, is quoted without reconstruction in source_map.json and report.json. Later unwrapped recurring glyphs keep the locally recorded alternatives below.','']
for g in sm['groups']:
 if g['printed_qualifier'] or len(g['complete_candidates'])>1:
  lines += ['### '+g['id'],'',g['owns']+'.','']
  for cand in g['complete_candidates']:lines.append('- `'+cand+'`')
  lines += ['',g['role_and_attachment'] or 'The local shape remains qualified.', 'Hand scope: '+g['hand']+'.','']
lines += ['### Whole participle after sont','', '- `determinés`', '- `déterminés`', '- `determines`','',
'The first spelling is primary. The final rising run remains qualified in relation to the ending and the preceding que descender; no second copy of that mark is supplied.','',
'## Viewing and final source audit','',
'One whole image, each supplied half once, and sixteen local crops once: nineteen successful views, no failed unseen deliveries, no reopen and no recrop. The whole image supplied layout; the halves supplied the complete reading. Crops were limited to listed unresolved targets. Archive 24 and the dark lower pair were settled on half b.','',
'Two text outputs were truncated before image viewing; their missing material was then read in bounded chunks. No image delivery failed. Local path placements are manual approximations. The complete source was checked for braces, environments, dollar/display delimiters, blank lines inside math, command names, exact source offsets, report/source agreement, crop paths and the eight source-row identities. No OCR, external lookup, proof inference, compilation, rendering, package installation or pixel-matching calculation was used.','']
(R/'reading.md').write_text('\n'.join(lines))
print('Wrote reading.md and literal H anchors.')
print('Unfound H anchors:',[(d['id'],d['H']) for d in r['differences'] if d.get('H_anchor_found_in_packet') is False])
print('Unfound C anchors:',[(d['id'],d['C']) for d in r['differences'] if d.get('C_anchor_found_in_packet') is False])
