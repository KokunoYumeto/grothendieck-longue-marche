from pathlib import Path
import json,re
from datetime import datetime,timezone

P=Path('/workspace/scratch/94548b74fbe0/out/readers/020/A')
tex=(P/'reading.tex').read_text()
report=json.loads((P/'report.json').read_text())
body='\n'.join(re.sub(r'(?<!\\)%.*','',line) for line in tex.splitlines())
stack=[]
brace_errors=[]
for i,c in enumerate(body):
    if c=='{' and (i==0 or body[i-1]!='\\'): stack.append(i)
    elif c=='}' and (i==0 or body[i-1]!='\\'):
        if stack: stack.pop()
        else: brace_errors.append(i)
env_stack=[]; env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    op,name=m.groups()
    if op=='begin': env_stack.append(name)
    elif env_stack and env_stack[-1]==name: env_stack.pop()
    else: env_errors.append([op,name])
required=[
 r'\scanpage{20}',r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_J^\circ',
 r'\unsure{clas.|deux.}',r'\Sigma_{\unsure{j|\deleted{J}i|i}}^+',
 r'\Sigma_{\unsure{j|i}}',r'E_{\unsure{i|j}}',r'On sait donc',
 r'\unsure{tout|est}',r'ce qui achève',r'\unsure{aussi|ainsi}',
 r'\unsure{dém.|dem.}',r'\unsure{par|p}',r'récurrence',
 r'\deleted{I}K',r'\inserted{\deleted{non vide}}',r'\deleted{on a}',
 r'\deleted{\Rightarrow}\in|\deleted{\to}\in|\in',
 r'{\unsure{E|\deleted{\Sigma}E}}_\alpha',
 r'(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)',
 '% archive sheet number: 19'
]
missing_readings=[s for s in required if s not in tex]
missing_files=[]
for r in report['differences']:
    if r['readers_crop'] and not (P/r['readers_crop']).is_file(): missing_files.append(r['readers_crop'])
for c in report['crops']:
    if not (P/c['path']).is_file(): missing_files.append(c['path'])
ids={r['id'] for r in report['differences']}
map_errors=[]
for s in report['C_doubt_source_map']:
    for rid in s['local_reports']:
        if rid not in ids: map_errors.append(rid)
draw_count=len(re.findall(r'\\(?:draw|fill)(?=\[|\s)',body))
known=set(r'begin end scanpage Pi unsure circ deleted cap Sigma quad in tikzpicture useasboundingbox node rlap phantom draw fill ne varnothing overline operatorname uline figure setminus displaystyle bigcup alpha cup inserted widehat forall beta mathrel Rightarrow to pi Longleftrightarrow reversemarginpar margin makebox linewidth rotatebox shortstack normalmarginpar'.split())
commands=set(re.findall(r'(?<!\\)\\([A-Za-z]+)',body))
unknown_commands=sorted(commands-known)
result={
 'check_type':'source-only administrative validation; no compilation or rendering',
 'unclosed_braces':len(stack),'unmatched_closing_braces':brace_errors,
 'unclosed_environments':env_stack,'environment_mismatches':env_errors,
 'dollar_count_even':len(re.findall(r'(?<!\\)\$',body))%2==0,
 'display_open_count':body.count(r'\['),'display_close_count':body.count(r'\]'),
 'required_readings_missing':missing_readings,'crop_files_missing':missing_files,
 'C_row_map_errors':map_errors,'unrecognized_commands_against_local_allowlist':unknown_commands,
 'literal_draw_fill_commands':draw_count,'reported_draw_fill_commands':report['counts']['literal_draw_or_fill_commands'],
 'report_C_flags':sum(r['diff_C'] for r in report['differences']),
 'report_H_flags':sum(r['diff_H'] for r in report['differences']),
 'images_opened_by_this_script':0,'mathematical_checks_performed':0
}
result['passed']=not any([stack,brace_errors,env_stack,env_errors,missing_readings,missing_files,map_errors,unknown_commands]) and result['dollar_count_even'] and result['display_open_count']==result['display_close_count'] and draw_count==result['reported_draw_fill_commands']
(P/'source_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if not result['passed']:
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(1)

end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report['end_utc']=end
report['source_checks']=result
report['image_audit']['next_work']='Complete one-page return; no image target remains.'
report['image_audit']['finished_utc']=end
(P/'image_audit.json').write_text(json.dumps(report['image_audit'],ensure_ascii=False,indent=2)+'\n')
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

md=r'''# Scan020 — reader A complete audit

Complete proposed transcription: reading.tex. Structured decisions: report.json. Image history: image_audit.json. Crop coordinates and processing: crop_manifest.json. Source-only validation: source_checks.json.

Start UTC: 2026-11-20 20:45:40 UTC, recorded before packet reading.
End UTC: END_UTC.

## Scope, sequence and counts

Read the entire assigned packet, brief v18, PREAMBLE and notation snapshot. Viewed the whole scan once for layout, half a once and half b once line by line. Viewed 14 planned local crops and one new complete attachment target. All 18 image deliveries succeeded; there were no failed unseen deliveries, no repeat views and no remaining unviewed targets. The root checkpoint hold was respected after the completed visual phase, then this same context resumed. No other reader or page was inspected.

The actual C Doubtful readings table has 11 source rows. R01 has three independently recorded physical ring occurrences, giving 13 source-doubt subloci. Two source rows are resolved, nine retained. The report has 28 records, with 10 current C difference flags and 22 H difference flags. It contains 15 remaining doubtful loci, 38 inventory entries, seven graphical groups and 13 literal draw/fill commands. Each of H's three struck ill placeholders has one physical parent count.

## Compact line-by-line audit

| Physical location | Selected reading and visual audit |
| --- | --- |
| Opening line | Ainsi les classes de Pi_I are followed by sont les. First small ring retains circle/zero, printed with the page's first qualifier. Crop01. |
| Second line | classes de Pi_J distinctes de overwritten Pi/U_{J,i},. Hooked J and dotted i are readable. The second ring independently retains circle/zero, with only circle printed under the recurrence convention. Crop02; overwritten Pi settled on half a at full-scan box 1310,164–1469,265. |
| Third line | et de plus les clas./deux. parmi. The low humps do not settle the word. The distinct terminal point is retained with both candidates. Crop03. |
| Paired display | U_{J,i} cap Sigma_{j/deleted Ji/i}^+, U_{J,i} cap Sigma_i^-. The first index is a dotted long descent with a doubled low return; j is primary. The second index's dot and lower hook stay together. The Sigma upper strokes belong to their letter heads; no additional closure stroke was inferred here. Crop04. |
| Next two prose lines | qui sont non vides. Or les deux classes en question sont non vides, car. Readable on half a, including the full stops and comma. |
| Cancelled start of voisinage line | Cancelled Sigma with j primary, i alternative. Two observed oblique cancellation runs occur once in A020-G01; the deleted annotation is invisible. H's first ill placeholder is counted once. Crop05. |
| U est un voisinage de E, et | U_{J,i} and voisinage are readable. Sigma survives beneath E; its i/j index remains doubtful. The low comma is separate and retained. Crop06. |
| Low point after voisinage | New complete target crop15 contains the complete g descender and following de. The descender closes separately to the left of the gray rounded point. A020-G02 preserves the shape under a local qualifier; role, hand and surface origin remain unestablished. The E-index target was outside crop15. |
| Two barred formulas | Both closure rules are visible. The first E carries a Sigma predecessor; the second barred Sigma carries an E predecessor; the last E carries a Sigma predecessor. First endpoint comma, second endpoint point. Crop07. Both current C and H already contain the closure bars. |
| On ... donc | sait is the selected resolved reading: low returning initial with upper hook, compressed vowel group, dotted i, tall t. Crop08. |
| Count lead-in | que le nb des classes est en, followed by cancelled tout/est. En is live. A020-G03 records the two crossing runs without an added generic visible rule; the word stays doubtful. Crop09. |
| Count and opening parenthesis | (n-1)+2=n+1=card I+1 (ce qui achève. The count and lower-case card were read on half b. Achève retains its grave, made of two adjoining short fragments. The complete q descender belongs to qui and is retained through the word once. Crop10. |
| Parenthetical next line | aussi remains primary with ainsi alternative. After la, the high dark triangular point is retained once in A020-G04, with unresolved role, hand and surface origin. Crop11. |
| Same line, abbreviation onward | dém./dem. retains the unaccented alternative. The following compressed word is par primary with p as an abbreviation alternative and no endpoint point. Récurrence retains its separately observed acute. Sur and the ending le nb des classes). were read completely. Crop12 and half b. |
| Lemma heading | Lemme has one underline. Toute classe de Pi_I est de la forme is readable. The lemma ring independently retains circle/zero, with the recurring primary alone printed. Crop13. |
| Lemma formula | X setminus bigcup_{alpha in deleted I K}(Sigma_alpha^+ cup E_alpha). The old I is resolved from its upright and left-reaching top/foot. The added hatted Sigma label is present. A020-G05 preserves the main brace run and its closed left retrace beside the unchanged formula. Crop13. |
| Lemma continuation | où K est une partie, inserted and cancelled non vide, de I, et. A020-G06 contains exactly non vide and de I, plus the crossing stroke and long curved guide. Partie and et remain outside that group. Crop13. |
| Slanted margin | K est neq empty / si I neq empty, on two rising lines. Readable on half b; retained as a slanted margin note. |
| First quantified condition | forall alpha in K, cancelled on a, Sigma_alpha^+ [reworked relation] pi_0(X setminus E_alpha), tels que. On a is readable beneath its crossing. H's third ill placeholder is counted once. Crop14. |
| Relation and E state | A020-G07 prints the locally qualified observed outer curve, middle run and small right return. Complete states are deleted Rightarrow then membership, deleted single arrow then membership, or live/retraced membership. They are explicit in the TeX comment and invisible annotation, without duplicate visible operators. The later E remains primary, with a locally qualified Sigma/E predecessor state. Crop14. |
| Final condition | forall alpha,beta in K, alpha neq beta, on ait hat Sigma_alpha^+ cap hat Sigma_beta^+=empty. Both hats, both plus signs, the alpha/beta indices and endpoint empty sign were inspected on half b. |
| Last parenthesis | Longleftrightarrow Sigma_alpha^+ cap Sigma_beta^+=empty. Two-ended double-line arrow, unhatted Sigmas, plus signs, both parentheses and terminal point retained. Half b. |
| Foot | Archive 19 is retained only in its comment; hand undetermined. No date or manuscript page number is supplied. |

## Exact C source-row map

| C row | Supplied source location | Outcome |
| --- | --- | --- |
| R01 | opening and lemma | Retained at all three rings: circle primary, zero alternative. Report 01, 02, 21. |
| R02 | line 3 | Retained clas./deux.; endpoint point preserved with either. Report04. |
| R03 | first paired intersection | Retained complete states; j primary, deleted Ji and i alternatives. Report05. |
| R04 | before U est un voisinage | Retained cancelled Sigma index; j primary, i alternative. Report06. |
| R05 | voisinage de E | Retained i/j. Report08. |
| R06 | word struck at right before count | Retained tout/est; literal crossing geometry added. Report16. |
| R07 | in the parenthesis | Retained dém./dem. Report19. |
| R08 | under K, union index | Resolved old I. Report22. |
| R09 | beside membership sign before pi_0 | Retained full predecessor/live-state alternatives; literal paths locally qualified. Report26. |
| R10 | above the count | Resolved sait. Report14. |
| R11 | in the parenthesis, before la | Retained aussi/ainsi. Report17. |

The notation table and slips-kept-as-written table were read in their separate source categories. No entry from those sections was invented as an extra C doubt row.

## Graphical source boundaries

G01 contains the cancelled Sigma/index and two crossings; following U lies outside. G02 contains only the gray point. G03 contains only the cancelled tout/est and its two crossings; en and the count lie outside. G04 contains only the high triangular point. G05 contains the complete first lemma formula, its parentheses, hatted label and two brace paths. G06 contains the cancelled insertion non vide and adjoining de I, once; partie and et lie outside. G07 contains only the reworked relation paths; its complete state candidates occur in a comment and invisible annotation.

All seven groups declare local source origins, baselines and fixed rectangles. Their manually selected drawing coordinates remain distinct from observed locus boxes and node font extents. The G07 annotation node is overlay, so its invisible alternative text does not enlarge the fixed drawing bounds. No rendered or metric validation is claimed.

## S coverage and attributed mathematics

S row SA01-K81-06 spans scans015–022 and explicitly records an author who viewed no scan. It supplies proposals only. On this sheet, the two Sigma_i closure rules are visible and already present in both current witnesses. The exact Sigma_1 and U_s examples quoted in S do not occur here. The report therefore records local confirmation with zero current-witness bar corrections.

Grothendieck writes the class-count argument, the count (n-1)+2=n+1=card I+1, and the lemma with its pairwise conditions. He also writes the final parenthetical equivalence between the hatted and unhatted disjointness statements. The transcription preserves these assertions; no proof check or optional mathematical computation was performed.

## Completion and limitations

Source-only checks passed: balanced braces and environments, paired math delimiters, required reading selections, crop-file existence, exact C source-row links, allowed command names, and agreement between the 13 literal path commands and the report. There was no OCR, web/research, compilation, rendering, installation, image comparison or optional geometric computation. The low-confidence words, indices, complete-state choices and graphical roles remain explicit in report.json and reading.tex. No further image target is pending.
'''
md=md.replace('END_UTC',end)
(P/'reading.md').write_text(md)
print(json.dumps({'end_utc':end,'source_checks_passed':True,'counts':report['counts']},ensure_ascii=False,indent=2))
