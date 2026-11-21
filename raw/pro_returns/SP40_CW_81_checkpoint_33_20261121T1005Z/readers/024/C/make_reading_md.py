from pathlib import Path
import json
D=Path('out/readers/024/C');r=json.loads(D.joinpath('report.json').read_text());m=json.loads(D.joinpath('group_metadata.json').read_text())
text=r'''# Scan 024 — independent reader C

The whole sheet and both supplied halves were read once, followed by 22 distinct local enlargements. The visual phase is complete. This reading attributes the assertions to the manuscript and supplies no mathematical proof check.

## Complete verbal and mathematical reading

The following block exposes the selected wording and every principal textual alternative. Pipes are editorial alternatives. The exact literal shapes, old/live annotations, and the separate small marks belong to `reading.tex`; their complete source spans are in `source_map.json`.

```latex
\unsure{Considerons|Considérons} la partition $\Pi_I^{\unsure{\circ|0}}$ de
$X\setminus\bigcup_{\alpha'\in I}E_{\alpha'}$, soit $S$ l'ens des classes,
notées $U_s$ $(s\in S)$. \deleted{\unsure{On a|On}} Considérons la
\deleted{\uline{Lemme} $\forall i\in I$,}
\inserted{Relation $R$ entre $S$ et $I$}
\[
\deleted{\unsure{U|E}}(s,i)\in R\
\overset{\text{def}}{\Longleftrightarrow}\
\overline{U_s}\cap E_i\ne\varnothing.
\]

\uline{Lemme} Cette relation fait de
$\unsure{(S,I)\deleted{R})|(S,I\deleted{)},R)}$
un graphe strict ayant $S$ comme \unsure{ens de|ens des} sommets,
$I$ comme ens. d'\unsure{aretes|arêtes|arètes}.)
\deleted{Cette relation} \unsure{Le|Ce} graphe est un \uline{arbre}

\unsure{le|Le} fait \unsure{qu'on a} un graphe strict signifie que a)
$\forall i\in I$, Il \deleted{\unsure{existe|ex}} y a exactement deux
$U_s$ tels que $\overline{U_s}\cap E_i\ne\varnothing$, et b) $i$ est
caractérisé par \unsure{l'ens|l'une} de ces deux $U_s$.

\unsure{Soient|Soit} $\Sigma_i^+,\Sigma_i^-$ les deux comp.
\unsure{connexes|conn} de $X\setminus E_i$, alors a) se précise en :
il y a \unsure{exactemt|exactement} \uline{un}
$\unsure{U_{s_+}|U_{s_-}}$ contenu dans
$\unsure{\Sigma_i^-|\Sigma_i^+}$ tel que
$\unsure{\overline{U_{s_+}}|\overline{U_{s_-}}}\cap E_i\ne\varnothing$
(et de $=$ pour $\Sigma_i^-$, \unsure{de|dé|qui} definit un
$U_{s_-}\subset\Sigma_i^-$ tel que
$\overline{U_{s_-}}\cap E_i\ne\varnothing$),
% archive sheet number: 23
```

The first signed Sigma has a detached bent head, an interrupted pale upper-body start, dotted i, and clear plus. The second has a detached short head, a separate thin upper arm, hooked foot, a short dotless i candidate, and clear minus. Their detached heads retain head/retrace or independent-upper-run roles. The later three Sigma heads join their bodies locally. The contained-in Sigma carries the solid minus/plus raised block; its index and the parenthetical Sigma index retain the short dotless i qualification. The last Sigma has a firm dotted i. These local qualifications remain with their complete glyphs; the first-occurrence printing rule is recorded in the TeX and report.

The two dense signs beneath s in the first plain and first barred U remain independent plus/minus readings. Each has its own literal solid contour. The source prints the recurring sign qualifier first and preserves the later local doubt in its comment, invisible annotation, and public record.

The entire reduced **qu'on a** phrase remains qualified. Its final solid point supports the a reading and an independent, unassigned-point reading: the complete alternatives are **qu'on a** and **qu'on followed by an unassigned point**. The q descender and adjoining words stay in the same source group. The point's role and hand remain separate questions.

## Line-by-line visual audit

Coordinates below refer to the native supplied half named in the first column, with the origin at its upper-left. They are manually selected reading locations, without a calculated full-page alignment.

| Half and approximate line | Readable ink and retained local decisions |
| --- | --- |
| a, opening line, y 90–206 | Considerons/Considérons; la partition; Pi with lower I and circle/zero; de X minus the union. Both union and E indices resolve as alpha-prime from their own loops and raised marks. A comma closes the line. |
| a, y 220–309 | soit S l'ens des classes, notées. The first ens has no point. The tiny point above initial s is separate from the word's i dot and remains a qualified graphic. |
| a, y 320–411 | U_s (s in S). Cancelled On a/On, then firm accented Considérons la. O, lower remnants, crossing and terminal are all retained. |
| a, y 416–555 | Raised Relation R entre S et I; cancelled underlined Lemme and forall i in I comma below. The R in Relation is capital. One rising strike and separate old underline are drawn once. |
| a, y 516–641 | Crossed U/E predecessor beside live (s,i), membership R, unaccented def, double-shaft arrow, barred U_s cap E_i crossed equality slashed empty-set form, period. A separate high point over the predecessor retains its own scope. |
| a, y 674–794 | Underlined Lemme; Cette relation fait de; complete two-state revised tuple. First closer, R crossings and long final-hook return remain literal. |
| a, y 789–909 | un graphe strict ayant S comme. The left rule begins with a hooked retrace. |
| a, y 907–989 | ens de/ens des sommets, I comme ens. The first abbreviation has no dot; the last ens. has a visible point. |
| a, y 970–1108 | d'aretes/arêtes/arètes, point and closing curve; deleted Cette relation; complete Le/Ce with a detached upper zigzag; graphe. |
| a, y 1123–1195 | est un underlined arbre; no following manuscript point. The whole left rule endpoint and a separated two-run oblique trace are retained. |
| b, y 99–264 | le/Le fait; complete reduced qu'on a phrase; un graphe strict. A pale bent trace below-left of fait is a separate qualified graphic. Both f and q descenders were included in the local crop. |
| b, y 204–344 | signifie que a) forall i in I comma; live Il; cancelled existe/ex; live y a. The capital I cap and the pale entry into a are separately represented. |
| b, y 320–448 | exactement deux U_s tels que barred U_s cap E_i crossed equality slashed empty-set form, comma. All bars, low indices and separators were read in the supplied half. |
| b, y 439–570 | et b) i est caractérisé par l'ens/l'une de. The local complete word remains qualified; adjoining par and de are firm. |
| b, y 574–641 | ces deux U_s, followed by a point. |
| b, y 632–756 | Soient/Soit, the two complete signed Sigma groups, les deux. The first i is dotted; the second short index stays locally qualified. |
| b, y 625–727, right continuation | comp. connexes/conn de. comp. has a point; the following reduced word has none. |
| b, y 735–857 | X minus E_i comma, alors a) se précise en : il y. en and the two-point colon are retained; H's ainsi differs. |
| b, y 850–979 | a exactemt/exactement; one live underlined un; U_s with solid plus/minus block; contenu dans Sigma with a horizontal solid raised block, minus primary and plus alternative. Tiny neighboring tick/point remain separate from the U sign. |
| b, y 970–1107 | tel que; barred U_s with independently qualified low sign; cap E_i crossed equality slashed empty-set form. The literal E has a separated upper arm and extended middle/index return. |
| b, y 939–1068, right continuation | (et de = pour joined-head Sigma_i-minus, de/dé/qui. The p descender ends above the next line's closure bar with a visible gap. |
| b, y 1076–1195 | Unaccented definit un; U_s-minus subset joined-head Sigma_i-minus; tel que barred U_s-minus cap dotted E_i crossed equality slashed empty-set form, close and comma. The complete f descender and endpoint are present. |
| b, lower-left corner | Archive 23 is recorded only as the required comment, with undetermined hand. |

## Original C doubts

Each row below keeps the original `C_doubts.txt` row identity. R02 has both opening indices; R09 retains its combined word/accent/punctuation scope; R13 keeps its first-sign scope and its explicitly recorded contextual later occurrence. No notation-table row is counted as another doubt.

'''
text+='| Source row | Original locus | Status and complete selected reading |\n| --- | --- | --- |\n'
by={d['id']:d for d in r['differences']}
for row in r['C_source_doubts']:
 d=by[row['local_entries'][0]]
 reading=d['reading'].replace('|',r'\|')
 ext='; additional endpoint presence resolved' if row['id']=='C024-R09' else '; both local indices resolved' if row['id']=='C024-R02' else ''
 text+=f"| {row['id']} | {d['location']} | {row['overall_status']}{ext}: `{reading}` |\n"
text+='\n## Complete literal-group ownership and qualifications\n\n'
for gid,g in m.items():
 alts='; '.join(g.get('alternatives',[])) or 'No second character/word candidate is supplied.'
 text+=f"**{gid}** owns {', '.join(g['owns'])}. Primary: `{g['reading']}`. Alternatives: {alts}. {g['qualification']}\n\n"
text+=r'''## Attributed content and limits

The author names the partition classes U_s, writes the intersection relation, and labels the ruled statement “Lemme.” The sheet calls its graph an “arbre,” then gives the two written explanations a) and b) and the final signed-component passage. No explicit authorial “à vérifier” or comparable verbal uncertainty was read. No date or written total page count appears.

All graphical placements are manual visual approximations from the once-viewed targets. The file has source inspection and structural checking; it has no compiled or rendered validation. The small gray traces retain their unestablished roles, hands, attachments and surface origins. The only recorded computations are the ordinary crop/enlargement operations and source offsets/hashes; `check_events` is empty because no mathematical check was performed.

## Viewing and source record

'''
text+=f"Start UTC: {r['start_utc']}. Finalization UTC is recorded in report.json.\n\n"
text+=f"One whole image, half a once, half b once, and 22 distinct crops once: 25 successful deliveries. Failed/unseen deliveries: 0. Successful reopens: 0. The original 18 C rows comprise 3 resolved rows and 15 retained rows; R09 additionally has its endpoint sublocus resolved. The report contains {len(r['differences'])} difference/source-choice records and {len(r['inventory'])} inventory elements.\n\n"
text+='The original combined text read was truncated; the complete required files were then read in bounded outputs. No image delivery failed. The root-requested snapshot pause occurred after half b and before the first local crop; no delivered image was reopened.\n\n'
text+='`source_map.json` gives exact character/UTF-8/line spans, complete source excerpts, literal paths and nodes, wrappers, parent environments and units, source-row links, and every word-bearing group boundary. The report preserves raw witness flags and physical-cluster identities separately.\n'
# The illustrative verbal block uses ordinary spacing commands, never an accidental bare double slash.
text=text.replace('\\in R\\\\\n','\\in R\\quad\n').replace('\\Longleftrightarrow}\\\\\n','\\Longleftrightarrow}\\quad\n')
text=text.replace(r'\in R'+'\\'+'\n',r'\in R\quad'+'\n').replace(r'\Longleftrightarrow}'+'\\'+'\n',r'\Longleftrightarrow}\quad'+'\n')
D.joinpath('reading.md').write_text(text)
print('reading.md written',len(text),'characters')
