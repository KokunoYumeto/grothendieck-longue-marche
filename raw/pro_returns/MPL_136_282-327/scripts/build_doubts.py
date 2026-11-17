#!/usr/bin/env python3
"""Build the final doubt register from root-reviewed readings; no image or context access."""
from pathlib import Path
import csv,json,html
R=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((R/'records/inline_doubts.csv').open()))
readings=[json.loads(x) for x in (R/'reading_doubts.jsonl').read_text().splitlines() if x.strip()]
# Root's second visual pass changed these preferred readings / cancellation states.
for x in readings:
 if x['scan']==291 and x['line']=='(10.2) second Hom exponent': x.update(reading='b',alternatives='0; overwritten; b preferred after second visual comparison')
 if x['scan']==314 and x['line']=='left functor superscripts': x.update(reading='! above Hom cancelled; ! below Hom live',alternatives='upper cancellation strokes weak; all three recorded explicitly')
 if x['scan']==318 and x['line']=='right lower': x.update(reading='évidentes, deleted pour, sur',alternatives='évidemment; short cancelled word before sur uncertain')
 if x['scan']==320 and x['line']=='upper left annotations': x.update(reading='f^(rs) in; f pq',alternatives='pq possible in first exponent; rs favoured after enlargement')
(R/'reading_doubts.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in readings))
header=r'''# Notation, doubts, and abbreviations — MPL_136_282–327

## Notation table

This table records the principal reader's cross-page comparison, completed before the context archive was opened. A typographic rendering identifies a visible sign; it is not a repair of the mathematics. The supplied whole-page and half-page images were personally read by the principal reader, without OCR; subagent work was limited to mechanical file checks before the freeze.

| Recurring ink / convention | LaTeX rendering | Comparison and reservation |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes | Used throughout for handwritten double quotation marks; not converted into guillemets. |
| Prime, double prime | `'`, `''` or `\prime` | Kept distinct from the exclamation marks on scans 313–314. |
| Exclamation marks attached to Hom | `^!`, `_!` | Scans 313–314: live and cancelled upper/lower positions are distinguished; the overwritten marks remain doubtful. |
| Opposite category | `^o` | Small letter o retained, not changed to an exponent 0 or “op”. |
| Ordinary integer zero | `0` | Not silently identified with a circular O in the faint final sheets. |
| Degree star | `_*`, `^*` | Position is read separately; cancelled stars remain present inside `\deleted`. |
| Chain/cochain degree dot | `_\cdot`, `^\cdot` | One dot encoding across scans 306–318; not replaced by a star. |
| Bracketed ordinal and degree | `[n]`, `K_{[n]}`, `K^{[n]}` | Kept distinct from unbracketed chain/cochain degrees. |
| Staggered upper/lower indices | e.g. `{\Delta^n}_*` | Braces preserve the visible upper-left/lower-right arrangement on 303–305; they do not reverse variance. |
| Simplex and simplex category | `\Delta`, `\boldsymbol\Delta` | Heavy/doubled category sign distinguished from ordinary simplex notation where visible. |
| Presheaf category | `\widehat{\boldsymbol\Delta}` | Hat retained; no modern replacement by a different category notation. |
| Dold–Puppe / non-degenerate labels | `\mathrm{DP}`, `\mathrm{ND}` in mathematics | Compared on 306–308, 311, 315, 318; same uppercase letter forms. The source's apparent ND/DP substitutions are not repaired. |
| Universal chain functor C | `\mathbb C_*`, `\mathbb C_\cdot` | Doubled C stem compared on 311–318. A generic ordinary C remains ordinary C where its stem is not doubled. |
| Number systems | `\mathbb Z`, `\mathbb N`, `\mathbb R`, `\mathbb C` | Double-stroke form retained; the same C glyph also occurs for a chain functor, whose meaning is not encoded by changing its alphabet. |
| Categories Ab, Ens; operator words | `\mathrm{Ab}`, `\mathrm{Ens}`, `\operatorname{Hom}`, etc. | Roman letter groups are typesetting of the manuscript's abbreviations, not their expansion. |
| Index-family L and category U | `\unsure{\mathcal L\|L}`, `\unsure{\mathcal U\|U}` | Compared on 316–318; the cursive/plain distinction is not securely decidable, so one doubtful encoding is used. This does not affect ordinary chain-object L. |
| Base coefficient h / k | `\unsure{h\|k}` or the locally preferred reverse order | Angular strokes vary; no global algebraic correction was imposed. |
| Superscript on S in the graded-module sheets | `\unsure{b\|h}` | Compared on 287 and 291; never silently replaced by a familiar standard notation. |
| Lowercase ell / digit one | `\ell` / `1` | Tate modules and graded indices checked independently of mathematical expectations. |
| Ordinary M, checked M, decorated duals | `M`, `\check M`, prime / vee / tilde as visible | Typed and handwritten sheets retain their own distinctions; missing decorations are not supplied. |
| Filtration indices | `M_N`, `M^N`, `M_{\leq N}` | Lower and upper placements retained, including the unusual inequality on 297. |
| Tensor and cartesian product | `\otimes`, `\times` | Overwritten products in diagrams marked doubtful instead of inferred from a universal property. |
| Boxed/circled tensor | `\boxed{\otimes}`, `\bigotimes` or explicit drawn enclosure as present | Particular source decoration retained; no automatic identification with the ordinary tensor product. |
| Gamma and gamma | `\Gamma`, `\gamma` | Uppercase divided-power symbol distinguished from coefficient/label letters. |
| Product vs sum in exponents | `pq` / `p+q` | Checked diagram by diagram on 320–325; both genuinely occur. |
| Parenthesized divided power | `f^{(p)}` | Kept distinct from a literal `f^p` where parentheses are absent. |
| Structure maps | `\sigma_{pq}`, `\beta`, `u_p`, `\Delta` | Labels retained locally, with uncertainty on compressed or overwritten subscripts. |
| Dashed / plain connections | `\mathrel{-}`, `dash`, `no head` | A visible line without a secure head is not promoted to an arrow; alternatives remain in `\unsure` where needed. |
| Equivalence / isomorphism sign | `\approx`, `\simeq`, `\sim` | Local strokes kept distinct; weak tilde-like arrow labels remain doubtful. |
| Inverse / direct limit shorthand | `\varprojlim`, `\varinjlim`, `\underline{\lim}` | Arrow direction follows ink. The last inverse-limit sign on 316 remains inverse even where duality might suggest a correction. |
| Projective-group lettering | `\mathrm{G\ell}`, `\mathrm{GP}`, `\mathrm{G.P}` | Source lettering on 326–327 retained; not modernized to GL or PGL. |
| Circular O / zero on final sheets | `\unsure{\mathcal O\|0}` | Particularly weak on 326–327; retained as a reading question. |
| Line-bundle Omega powers | `\Omega^{-1}`, `\Omega^2`, etc. | Negative signs and powers checked against the blue and grey strokes separately. |
| Underlining and enclosures | `\uline`, `\uuline`, `\boxed`, TikZ strokes | Textual underlining, mathematical boxes, and free-standing separators remain distinct. |
| Page numbering | `\mspage{...}` and `\margin{...}` | Apparent author/text page numbers use mspage; pale archive-style marginal numbering is retained as margin. Attribution of those pale numerals is uncertain. |
| Abbreviated wording | Exact source letters | Expansions occur only in the abbreviation table below. |

## Legibility and limits of confidence

The reused typescripts are generally the clearest material, but their overtyped cancellations (especially scan 292) are poor. The handwritten notes vary from comparatively open prose to compressed drafts; the least secure passages are the coaction diagrams on 283–285, cancelled graded-module formulas on 291 and 295, the lower diagram on 299, the overwritten proof and category indices on 313–317, the last Hom formula on 320, and the faint/corrected geometric scratchwork on 326–327. The three words marked `\illegible{3}` on 292 remained physically unreadable after enlargement; no formula or diagram symbol was replaced by that macro.

Every explicit doubt in the final page files appears below. Physical `.tex` line numbers identify exact saved-file locations, not an invented numbering of the manuscript's lines. “Low” is assigned conservatively to inline readings lacking a separately recorded individual judgement; it is not a statistical error estimate. “Medium” means a plausible letter/stroke reading with a material reservation; “high” in the supplementary register records a clear but surprising literal reading. Repeated occurrences and nested doubts each have their own row. The supplementary register adds descriptive positions and reservations; where it paraphrases a reading, the exact inline text is authoritative.

All 45 whole pages and their 90 supplied half-page images were inspected, and all 45 pages received a further visual audit after the first pass was finished. This is a diplomatic transcription with substantial unresolved readings, not a claim of error-free decipherment. TikZ drawings approximate spatial contours; their labels and remaining uncertainties are retained. The two lower-right strokes on 325 may be paper furniture rather than autograph marks; they are reproduced to avoid silently discarding visible strokes.

## Complete inline doubt table

'''

def cell(x): return '<code>'+html.escape(str(x),quote=False).replace('|','&#124;').replace('\n','<br>')+'</code>'
def split_alts(x):
 depth=0;esc=False
 for i,c in enumerate(x):
  if esc:esc=False;continue
  if c=='\\':esc=True;continue
  if c=='{':depth+=1
  elif c=='}':depth-=1
  elif c=='|' and depth==0:return x[:i],x[i+1:]
 return x,'no separate alternative proposed'
parts=[header,f"Count: **{len(rows)} occurrences**, comprising **499 unsure** and **1 illegible** (estimated **3 words**). Exact source hashes and character offsets are preserved in `records/inline_doubts.csv`.\n\n",'| File | Scan | Approximate location | Preferred reading | Alternative(s) / reservation | Confidence | Occurrence |\n|---|---:|---|---|---|---|---|\n']
for r in rows:
 reading,alt=split_alts(r['raw_argument'])
 conf='low'
 matches=[x for x in readings if str(x['scan'])==r['scan'] and x['reading'] in (r['raw_argument'],reading)]
 if len(matches)==1:conf=matches[0]['confidence']
 if r['macro']=='illegible':reading=f"{r['raw_argument']} physically unreadable words";alt='overtyped cancelled passage; no secure reading'
 loc=f".tex line {r['line_start']}, column {r['column_start']}"
 if r['enclosing_doubt_id']:loc+='; nested in '+r['enclosing_doubt_id']
 parts.append('| '+' | '.join(map(cell,[r['filename'],r['scan'],loc,reading,alt,conf,r['occurrence_id']]))+' |\n')
parts.append('\n## Positioned reading reservations\n\nThese are the principal reader’s page-by-page location notes, updated for the second audit. They supplement rather than replace the exact inline table; some describe a group of nearby occurrences.\n\n| File | Scan | Approximate manuscript position | Reading | Alternatives / reservation | Confidence |\n|---|---:|---|---|---|---|\n')
for r in readings:
 parts.append('| '+' | '.join(map(cell,[r['cote'],r['scan'],r['line'],r['reading'],r['alternatives'],r['confidence']]))+' |\n')
abbr=[
('cat.; catég.','catégorie(s)'),('fonct.; fct','foncteur / fonction, as the local wording requires'),('inv.','invariant(s)'),('op.','opération(s)'),('cov.','covariant(s)'),('contravar.; contrav.','contravariant(s)'),('ss-cat.; ss-catégorie; ss-','sous-catégorie; sous-'),('ens.','ensemble(s)'),('hom.; Hom','homomorphisme(s); set or object of morphisms'),('gr.','groupe; sometimes gradué in the graded-module setting'),('mod.; Modgr.','module(s); modules gradués'),('alg.','algébrique / algèbre'),('coalg.; Co.algèbres','coalgèbre(s)'),('copr.','coproduit / coproduits (tentative on 283)'),('comm.; commut','commutatif / commutant, depending on syntax'),('ass','associatif'),('counit','counitaire'),('coaugm','coaugmentation / coaugmenté'),('p.d.; p. div.','puissances divisées'),('bil.','bilinéaire(s)'),('lin','linéaire'),('add.','additif / additive'),('diff.; diffs.','différentielle(s), or différent(s) where appropriate'),('simp.; simplic.','simplicial / simplicialité'),('ND','non-dégénéré (the manuscript supplies this expansion on 306)'),('DP; D.P.','Dold-Puppe (the manuscript supplies the name on 306)'),('comm. aux lim','commutant aux limites'),('proj.','projectif / projection / projecteur, according to context'),('repr.; représent.; représent.bles','représentable(s)'),('équiv.','équivalence / équivalent'),('adj.','adjoint / adjonction'),('isom.','isomorphisme'),('autom.','automorphisme'),('can.','canonique'),('imm.','immersion (reading itself uncertain on 327)'),('conn.','connexion'),('rev.','revêtement'),('ext.','extension'),('top.','topologique'),('cohomolog.','cohomologique'),('t.f.; d.t.f.','type fini; de type fini'),('fid.','fidèlement / fidèle'),('g.; pl.','gauche; plat(e), where the local phrase supports it'),('p.r.','par rapport'),('resp.','respectivement'),('i.e.','id est'),('p.ex.; p.e.','par exemple'),('cf.','confer / comparer'),('th.; Th','théorème'),('prop.; Prop.','proposition'),('Cor','corollaire'),('Rem','remarque'),('NB','nota bene'),('hyp.','hypothèse(s)'),('cond.','condition(s)'),('déf.','définition'),('conv.; convent.','convention(s)'),('ess.; essentiellt','essentiel / essentiellement'),('exactt','exactement'),('génér.','général / généralement'),('néc.','nécessairement'),('p.; part.','page; particulier / partie'),('val.','valeur(s)'),('suppl.','supplémentaire'),('tt; tte; ttes','tout; toute; toutes'),('tjrs','toujours'),('ms','mêmes'),('élt','élément'),('mb.','membre'),('rel.','relatif / relative'),('préf.','préférence'),('Groth.','Grothendieck'),('purs.','unresolved abbreviation on 314; do not expand confidently'),('en. commut / an. commut','possibly anneau commutatif; doubtful marginal reading on 325'),('box.','unresolved short form on 283; no secure expansion'),('re.; connais.','compressed / cancelled wording; expansion not secure')]
parts.append('\n## Abbreviations met\n\nExpansions are interpretive aids in this table only; no abbreviated manuscript word was expanded in the transcription. Some short forms have several context-dependent expansions.\n\n| Source form | Likely expansion / reservation |\n|---|---|\n')
for a,b in abbr:parts.append('| '+cell(a)+' | '+b+' |\n')
parts.append('\n## Transcription mechanics\n\nThe combined file is a fragment without a preamble; the editorial macros are intentionally left for the receiving edition to define. Brace, environment, marker, inventory, and doubt-extraction checks were performed. A full LaTeX/TikZ compilation could not be run because the available runtime lacked the LaTeX format and required packages; the environment check is retained in `records/tex_compile_environment.txt`. No successful compilation is claimed.\n')
(R/'MPL_136_282-327_doubts.md').write_text(''.join(parts))
print('Wrote doubt register with',len(rows),'inline rows and',len(readings),'positioned reservations')
