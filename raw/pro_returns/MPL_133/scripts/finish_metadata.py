"""Consolidate pre-freeze notation and observations after the visual audit."""
from pathlib import Path
import json
from record_page import ROOT,REC,utc,refresh
assert 'transcription frozen ' not in (ROOT/'progress.log').read_text()
rows=[s for s in (REC/'notation.md').read_text().splitlines() if s.startswith('|')]
rows=[s.replace('earliest occurrences remain doubtful pending audit','the earliest occurrence on 018 remains explicitly doubtful after audit').replace('Audit the heavy overwritten initial letters on scans 020–021 directly against these forms before freeze.','Audit resolves seven Mon occurrences on 021; the overwritten 020 form retains Mon/Hom doubt.').replace('`\\mathbb{\\Omega}`','small double-contour TikZ glyph') for s in rows]
extra=r'''| Literal shorthand for même/mêmes | `$=$`, `$=^{s}$` within doubt macros | Scans 026, 033 and 044: two horizontal strokes are not expanded silently. Written Même on 036 and même on 043 were rechecked separately and remain words. |
| Go-board side variable | `\unsure{v\|\nu}` | Scans 030–031: every recurrence, including its square, retains the same unresolved reading. |
| Go count variables | `P,Q,T,N,D`; `p,q,t,n,d` and primes | Scans 030–034: changes of case and primes are preserved. |
| Centre and derived-group names | `Z(G)`, `\operatorname{Cent}`, `DG`, `\operatorname{Der}`, `\operatorname{D\acute{e}r}` | Scans 036–054: spelling and accent variations remain as written; accent-safe encoding changes no reading. |
| Central-intersection letter | `\mathfrak z` | Scans 039–044; uncertain instances remain marked. |
| Crossed-module maps and actions | `d`, `d'`, `D_1`, `D_2`, `\theta`, `\Theta` | Scans 036–047: case, primes and indices compared across diagrams; overwritten initial formulas on 046 remain doubtful. |
| Kernel and action variables | `\zeta`, `\zeta_0`, `\zeta_G`, `\varphi_G`, `\psi_G` | Scans 047–052: repeated Greek forms compared, including barred psi and the doubtful G index on 051. |
| Commutator quotient | `\eta`, `\eta_0` | Scans 052–054: compressed 052 subscript remains doubtful; 053 explicitly shows `(N_{\mathrm{comm}})_M`. |
| Stars and their position | `\pi_0^*`, `\pi_{1*}` | Scans 049–054: cancelled upper stars and inserted lower stars on 054 are both retained. |
| Exclamation-like, prime-like and looped exponents | Literal signs or doubt alternatives | The ambiguous exponent on 023 remains a loop/exclamation alternative; prime/index doubts on 038–039 remain. No global normalization from theory. |
| Headless diagram connectors | `dash` | Directions are not supplied where no secure arrowhead is visible. |
| Headless hooks | `dash,hook` / `dash,hook'` | Scans 037 and 046: option order preserves the hook without adding a terminal arrowhead. |
| Single and double-headed arrows | `\longrightarrow`, `\twoheadrightarrow`, tikz-cd arrows | In particular the first double head on 054 remains although the following condition asks for surjectivity. |
| Underlining versus descenders | `\uline`, `\uuline` only for independent strokes | False underlines removed on 006, 007, 008 and 044 after close inspection. |'''
(REC/'notation.md').write_text('## Notation table checked before the freeze\n\nThe root transcriber compared recurring forms across all 50 pages during the sequential first reading and the separate visual audit. Differences that the ink did not decide remain marked; mathematical expectations did not decide them. The typed articles keep their own typographic conventions.\n\n'+'\n'.join(rows)+'\n'+extra+'\n\nAll tikz-cd matrices use `ampersand replacement=\\&` so that editorial macros can capture diagrams without changing alignment tokenization. The outlined Omega on scan027 is drawn with TikZ because the available AMS blackboard font maps that input to another glyph. These are encoding conventions, not new readings.\n')
(REC/'legibility.md').write_text('''The printed articles (011–017) and university notices (048, 050) are generally clear; apparent spelling and mathematical anomalies are retained. The handwritten pages vary from readable dark ink to very rapid, faint grey notes. All 50 pages had a sequential first reading including the full image and both supplied halves, and a separate visual audit by the same root transcriber; this is not an independently transcribed second version. No OCR was used, and no context member was opened before the freeze.

The least reliable material is the pale machine text visible on the reused sheet 018, where numerous estimated unreadable word groups remain; the dense overlapping additions on music paper 036; the heavily cancelled initial formulas and German margin on 046; and overwritten or clipped passages on 043–044 and 051–054. Scan 044's short marginal note and insertion are especially uncertain as complete phrases. Cancellation can erase the letter bodies themselves, so a plausible marked formula must not be treated as securely recovered text.

TikZ diagrams reproduce objects, connections, relative placement and recoverable decorations. Small pen flourishes and irregular enclosures are approximations, not facsimiles. Signatures are given as doubtful name readings with the recoverable flourish drawn separately. The scope of the lower cancellation on 051 and the instruction “annulé?” on 052 remains explicitly uncertain; inspect the original images when using those passages as mathematical evidence.

Confidence describes the ink reading, not the mathematical truth of a statement. A high-confidence observation can concern an unexpected but clear source form. Detailed page-specific observations qualify the automatic listing of individual doubt macros; a low-confidence whole-phrase or cancellation observation takes precedence over an otherwise generic medium label. The audit record preserves how readings changed before freezing.
''')
for n in [30,33,43,44,46,52,53]:
 p=REC/f'scan{n:03}.json';d=json.loads(p.read_text());rs=d['doubts']
 if n==30: rs[0][2]='The board-side variable is a rounded v/nu; every repetition and square now carries the same unresolved reading.'
 if n==33: rs[1][1]='au = / au même';rs[1][2]='Two short interlinear groups are partly struck; literal shorthand retained before its possible expansion.'
 if n==43: rs=[r for r in rs if r[0]!='characteristic positive paragraph']
 if n==44: rs=[r for r in rs if r[0]!='middle insertion']
 if n==46: rs=[r for r in rs if r[0]!='German margin']
 if n==52: rs=[r for r in rs if r[0]!='coinvariant notation']
 if n==53: rs=[r for r in rs if r[0] not in ['variation parenthesis','vanishing condition']]
 d['doubts']=rs;p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
with (REC/'abbreviations.md').open('a') as f:
 f.write('''
| Additional written form | Possible expansion (editorial only) |
|---|---|
| alg. | algébrique(s) |
| aff. | affine(s) |
| comm., commut | commutatif(s) |
| gr., grpe | groupe(s) |
| ss-grpe, ss-groupe | sous-groupe |
| conn. | connexe(s) |
| unipot., quasi-unip. | unipotent, quasi-unipotent |
| puiss. | puissance |
| car., Car. | caractéristique |
| V.A. | variété abélienne |
| tjrs | toujours |
| sss, ssi | si et seulement si |
| Pb | problème |
| sol. | solution |
| op. | opération(s) |
| déf. | défini / définition; phrase dependent |
| trivialt | trivialement |
| inv (subgroup context) | invariant |
| iso | isomorphisme / isomorphe |
| mono | monomorphisme |
| épi | épimorphisme |
| p.ex. | par exemple |
| t. mult. | type multiplicatif |
| égalis. | égales; compressed form on 044 remains an editorial interpretation |
| =, = with raised s | même, mêmes; literal shorthand retained in the transcription |
| E.S. | entrées-sorties (typed notice 050) |
| U.C. | unité centrale (typed notice 050) |
| U.S.T.L. | Université des Sciences et Techniques du Languedoc |
| C.H.U. | centre hospitalier universitaire |
| St | Saint |
| MR | Monsieur |
''')
(REC/'WORK_STATUS.md').write_text('''# Work status before freeze

All 50 first-pass pages and all 50 second visual audits are complete. Root alone read and transcribed the images in sequence. Notation comparison is complete, including Mon/Hom, tau/T, Greek letters, stars, primes/exclamation-like marks, shorthand equals signs and arrow decorations. A real LaTeX integration check is being rerun on the repaired exact combined fragment. Context remains closed; research notes have not begun.

First hourly checkpoint saved at 22:38 UTC; next is due 2026-11-16 23:38:17 UTC. Source archives and images must not enter deliverable ZIPs. After successful validation, hash the 50 page files and exact concatenation, record transcription frozen, then record context opened and read README.md and notes/RESULTS_STATE.md before research. Never modify frozen transcription afterward.
''')
with (ROOT/'progress.log').open('a') as f:f.write('notation comparison completed '+utc()+' all 50 scans; recurring forms checked against ink before context access\n')
refresh()
print('Final notation register and metadata refreshed.')
