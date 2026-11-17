from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/(ROOT.name+'_doubts.md')
history=ROOT/'records/reading_doubts_history.md'
if not history.exists():history.write_text(p.read_text())
notation=r"""# Notation table

This table was consolidated before any research context was opened. The same reader compared recurring signs across the whole sequence during the second visual reading. Consistency means using the same encoding for the same visible sign; changes of letter, accent, index or spelling actually present in the ink remain changes. Compact and wide LaTeX accent commands differ only in typesetting width.

| Manuscript feature | LaTeX treatment | Scans and cautions |
|---|---|---|
| Archive / scan / author numbering | `\cotefile{154}`, `\scanpage{N}`, `\mspage{n}` | Scan 11 is absent from the supplied retained set. Author numbering restarts at scan 12; scan 10 has `6'`. |
| Pencil archival foliation | `\margin{n}` | Pencil sequence 1–44 on retained scans 2–45 (10 is absent with omitted scan 11), including reused printed sheets; these are not silently attributed as author page numbers. |
| Looped capital surface letter versus plain capital | `\mathcal X` versus `X` | Especially scans 2–10 and 33–45. Looping strokes, not the role of the surface, decide the alphabet. |
| Curves / pseudo-lines | `D`, `D_i`, `L`, `\Delta`, `\Delta_i` | Distinct letter shapes are retained. Doubtful D/Delta and subscripts remain marked. |
| Prime, repeated prime | `D'`, `D''`, `D'''`, `t'`, `t''` | Compared throughout; especially 20–25, 27, 39 and 45. The sequence of t-primes in scan 45 changes between tuple and prose and is not repaired. |
| Possible exclamation-like raised stroke | `D^{\prime\,\unsure{1}}` | Scan 39: enlargement shows a prime and a further raised 1-like stroke. It is not confidently read as `^!`; no prime was converted on mathematical grounds. |
| Tilde / parallel or lifted object | `\widetilde D`, `\widetilde L`, `\widetilde X`, `\widetilde\Delta`, `\widetilde P` | Wavy marks are retained, including the nested tildes in scan 20. Scan 9 has a genuine unresolved tilde/hat ambiguity. |
| Hat and doubled accent on polygon notation | `\widehat P`, `\widehat{\operatorname{Pol}}`; explicitly doubtful doubled accent | Scans 18–25. The upper mark on the marginal P in scan 18 may be a tilde over a hat or a second hat; this remains an alternative. |
| Curved arc accents | `\overset{\frown}{ax}`, and similarly for `a,x`, `x,b`, `b,a` | Scan 24: all four marks were compared again and are curved, unlike the angular polygon hats. |
| Family / system | `\Sigma`, `\underline\Sigma`, `\overline\Sigma` | Underlines and overlines are separate source marks. Scan 13 has `\unsure{\widetilde\Sigma|\Sigma'}`; no normalization to a preferred system notation. |
| Relative-position spaces | `P`, `\widetilde P`, `\operatorname{Pol}`, `\operatorname{Pol}^*`, `\overline{\operatorname{Pol}}` where written | Scans 12–29. Augmented, hatted, barred and starred variants are kept apart. |
| Graphs and structure | `\Gamma`, `\Gamma^*`, `\operatorname{Str}`, `K`, `K_0`, `K_1`, `K'`, `L` | Graph notation changes between sections; cancelled predecessors are retained. |
| Vector versus barred edge set | `\vec A`, `\vec a`, `\overline A_s` | Scans 31–33. At the end of scan 31 the accent may be an arrow or a bar; both doubtful occurrences are explicitly marked. |
| Orientation letter | `\varphi`, with the doubtful `\varphi`/`\xi` reading at scan 12 | Later clear phi forms do not retrospectively resolve the earlier weak stroke. |
| Orientation torsors and values | `\omega`, `\underline\omega`, indexed `\omega_s`, `\omega_t` | Underlining is retained where present, notably scan 39; the diagram in scan 42 has plain omega. |
| Local multiplicity and permutation letters | `\nu`, `\sigma`, `\rho`, `\varepsilon`, `\alpha`, `\beta` | Small nu/u, sigma/s and alpha-like terminal graph components are marked where the ink does not settle them. |
| Flag operations | `\sigma_0`, `\sigma_1`, `\sigma_2`; `\widetilde\sigma_i^s` | Scan 32: products, order, inverse signs and the doubtful subscript 1/4 remain as written. |
| Polygon / segment letters | `\mathbb I` versus `\mathrm I` | Scan 29: doubled versus serifed upright remains explicitly doubtful. No additional blackletter alphabet has been inferred. |
| Ordinary maps, inclusions, equivalences | `\to`, `\hookrightarrow`, `\subset`, `\in`, `\simeq`, `\xrightarrow{\sim}` as individually drawn | A source dash remains `\mathbin{-}` or `\text{---}`. Examples include scans 9, 29, 31, 40 and 45. |
| Two horizontal strokes inside prose | `$=$` | Preserved as a symbol, not expanded to “même”; frequent from scan 9 onward. |
| Inequalities | `\le`, `\ge`, `\ne` with the visible direction | Special checks: scan 27 primes and inequalities; scan 36 cardinality at least 2. Scan 25 says order 2 with no visible inequality. |
| Quotation marks | two backticks and two apostrophes | The same convention throughout. Quotation strokes are not converted to French guillemets. |
| Underlining | `\uline{...}`, `\uuline{...}` | Underlining is distinguished from crossing-out by its vertical placement; residual ambiguity is recorded, e.g. scans 12 and 15. Circled h on scan 45 has two separate underlines. |
| Revisions and margins | `\deleted`, `\inserted`, `\margin` | Nested states preserve revised insertions and revisions within cancelled passages. No grammatical completion of interrupted text. |
| Diagrams / tables / drawings | `tikzcd` / `array` / `tikzpicture` inside the required macros | Four commutative or mapping diagrams use tikz-cd. Arrays align tables or braced textual/formula lists. All drawings are vector reconstructions with written labels, not raster inclusions. |

# Doubts

The register below indexes **every current `\unsure` occurrence** and every physically unreadable word group in the final page fragments. The line locator refers to the per-page `.tex` file, so it can be checked exactly; it is not an invented count of handwritten lines. A nested uncertainty has its own row. “No fixed alternative” means that the given reading is tentative, not that nothing is visible. Confidence is medium for a provisional readable form and low for crossed, overwritten, particularly compressed, or very small material; no uncertain form is labelled high.

The earlier working register, including readings subsequently corrected during the audit, is retained as `records/reading_doubts_history.md`. It is a history, not a competing transcription.

| File | Scan | Approximate line / location | Current reading | Alternatives / issue | Confidence |
|---|---:|---|---|---|---|
"""

def args(s,macro):
 for m in re.finditer(r'\\'+macro+r'\{',s):
  i=m.end();start=i;depth=1
  while depth:
   if s[i]=='{' and s[i-1]!='\\':depth+=1
   elif s[i]=='}' and s[i-1]!='\\':depth-=1
   i+=1
  yield m.start(),i,s[start:i-1]

def esc(x):return re.sub(r'\s+',' ',x).replace('|',r'\|').strip()
rows=[]
for page in sorted((ROOT/'pages').glob('*.tex')):
 s=page.read_text();n=int(re.search(r'scan(\d+)',page.name).group(1));deleted=list(args(s,'deleted'))
 for start,end,arg in args(s,'unsure'):
  line=s[:start].count('\n')+1
  in_deleted=any(a<=start< b for a,b,c in deleted)
  before=s[:start].split('\n')[-1]
  drawing='\\node' in before or '\\draw' in before
  level=0; split_at=None
  for j,ch in enumerate(arg):
   if ch=='{' and (j==0 or arg[j-1]!='\\'):level+=1
   elif ch=='}' and (j==0 or arg[j-1]!='\\'):level-=1
   elif ch=='|' and level==0 and (j==0 or arg[j-1]!='\\'):split_at=j;break
  reading=arg if split_at is None else arg[:split_at]
  sep='' if split_at is None else '|'
  alternative='' if split_at is None else arg[split_at+1:]
  confidence='low' if in_deleted or drawing or n in (10,12,26,39,44,45) else 'medium'
  where=f'fragment l. {line}'+(' (cancelled)' if in_deleted else ' (drawing label)' if drawing else '')
  issue=esc(alternative) if sep else 'No fixed alternative; compressed or ambiguous ink.'
  rows.append((n,start,f'| 154 | {n} | {where} | `{esc(reading)}` | '+(f'`{issue}`' if sep else issue)+f' | {confidence} |\n'))
 for start,end,arg in args(s,'illegible'):
  line=s[:start].count('\n')+1
  rows.append((n,start,f'| 154 | {n} | fragment l. {line} (cancelled) | `\\illegible{{{arg}}}` | Estimated {arg} physically obscured word(s); enlarged before this mark was retained. | low |\n'))

abbreviations=r"""
# Abbreviations

Expansions in this section are editorial suggestions only; none has been inserted into the transcription. An abbreviation with an uncertain reading remains uncertain even when a likely expansion is available. These entries cover the mathematical prose; printer commands and identifiers are listed separately below.

| Written form | Tentative expansion / sense | Example scans |
|---|---|---|
| `p.r.`, `pr`, `pos. rel.` | position(s) relative(s); in connective “p.r. à”, par rapport à | 2–5, 18, 37, 45 |
| `ps.dr.`, `ps. dr.`, `ps. droite(s)`, `p. dr.` | pseudo-droite(s) | 2, 9, 12, 23–25, 28, 34 |
| `pt`, `pts` | point, points | 2–45 |
| `nb`, `Nb.` | nombre | 3, 17–18, 44 |
| `ens`, `ens.`; `sous-ens.` | ensemble; sous-ensemble | 12–45 |
| `élts` | éléments | 44 |
| `tt`, `t` with raised `t`; `tte`, `t` with raised `te`; `ttes` | tout; toute; toutes, as appropriate to the written form | 16, 31, 35, 39, 44 |
| `ds` | dans | 24, 25 |
| `qd` | quand | 10 |
| `syst.` | système | 2–44 |
| `str.` | structure | 20, 32 |
| `comb.` | combinatoire | 31–34, 38 |
| `pol.` | polygonal / polygone, depending on the construction | 26, 32 |
| `géom.` | géométrique | 36 |
| `top.` | topologique | 42 |
| `lin.` | linéaire | 38 |
| `spéc.`, `sp.` | spécialisation(s) | 5, 14–15, 23, 38, 40 |
| `gén.`, compressed `généristé` | générisation(s); the latter is a tentative compressed spelling | 15, 18, 38, 40 |
| `rev.`; doubtful `rec.` alternative | revêtement, in `rev. des vis`; the alternate letters are not expanded confidently | 3, 12, 15–16, 34 |
| `isom`, `isom.`, `iso.` | isomorphisme / isomorphe | 15–45 |
| `isomo` (unfinished) | beginning of isomorphisme or isomorphie; not completed | 45 |
| `can.` | canonique / canoniquement | 3, 16, 18, 24, 34 |
| `homéom.` | homéomorphe(s) | 9 |
| `hom.` | probably homéomorphe in the polygon comparison; abbreviation itself does not settle the intended morphism | 3 |
| `comp.`, `comp. conn.`, `comp. connexes` | composante(s), composante(s) connexe(s) | 9, 16, 33–34, 44–45 |
| `corr.` | correspondance | 33, 35, 40 |
| `rep.` | repère(s) | 32 |
| `adh.` | adhérence(s) | 44 |
| `adj.` | adjacent(s) | 13 |
| `int.` | intérieur | 7 |
| `inv.` | inverse | 18 |
| `cell.` | cellulaire | 5 |
| `subd.` | subdivision | 5 |
| `bar.` | barycentrique | 5 |
| `faç` | façon, visibly shortened | 5 |
| `conv.` | probably convenable, in the tubular-neighbourhood phrase | 9 |
| `flè.` | flèche(s) | 16 |
| `or.` | orienté / orientation | 12 |
| `néc.` | nécessairement | 23 |
| `ch.` | chaque / chacun; source word division is retained | 12, 35 |
| `équi.` | équivalence | 35 |
| `tot.` with raised `t` | totalement, in the doubtful strict-system gloss | 35 |
| `bds` | bords | 35 |
| `ord` | ordinaires | 44 |
| `1er` | premier | 44 |
| `ssi` | si et seulement si | 45 |
| `resp.` | respectivement | 13, 17, 31, 45 |
| `i.e.` | id est | throughout |
| `cf.`, `cf`, `Cf` | confer / voir | 13, 25, 33, 44 |
| `p.ex.` | par exemple | 19; compressed equivalent in 23 |
| `d'autre p.` | d'autre part | 12 |
| `tout à l'h.` | tout à l'heure | 9 |
| `con.` (cancelled) | uncertain, perhaps a shortened earlier adjective; no reliable expansion | 12 |
| `prè. de` (cancelled) | perhaps près de; reading remains doubtful | 44 |
| `dvt` alternative | perhaps doivent, but the ink may instead read singular doit | 14 |
| `NB` | nota bene | several scans |
| `Cor` | corollaire | 45 |
| `St`, `Str`, `Pol`, `Spec`, `Sp`, `Gen`, `Dis`, `Rep` | Mathematical names or operator labels; possible expansions are étoile, structure, polygone, spécialisation, générisation, disque and repères, but the source forms are kept distinct | 12–45 |

On the reused printed stock (scans 6, 8, 10, 21, 27, 30, 33), `JOB`, `EXEC`, `DD`, `SYSOUT`, `SYSPRINT`, `SYSUT1`, `SYSUT2`, `IEBGENER`, `ACCT`, `MSGCLASS`, `MSGL`, `ON`, `CFT`, `CRAY2`, `IBM`, `JESNEWS`, `PR1`, `L`, `CR`, and the alphanumeric job identifiers are literal program, printer or job-control tokens. They have not been translated or “corrected”; plausible English or French expansions are not needed to recover their printed spelling. `HEBDO.` is hebdomadaire, and `CDE` is probably commande in the retained notice. The four zero-character figures, CRAY2 banners, asterisk frames, dates, times and job rows are reproduced rather than summarized.

# Legibility and reliability

The main live prose is usually readable, but the writing is exceptionally compressed and often laid over earlier revisions. The least secure material is the cancelled weight-definition prose (scans 12, 17–20, 24–26 and 44–45), the tiny polygon accents and primes, labels entangled with coloured strokes in scans 27, 30 and 39–42, and the faint repeated-character printer borders. There are four `\illegible` groups, totalling an estimated seven words, all inside physically obscured cancellations; mathematical symbols instead retain a proposed reading with `\unsure`.

Every retained whole-page image and both supplied halves was viewed directly, followed by a second comparison. Local enlargements and rotations were used for crowded or sideways text; no OCR was used. The TikZ drawings preserve the intended visible strokes, colour distinctions, relative locations, labels and cancellation layers as closely as practicable, but they are not pixel tracings: fine pen jitter, exact curve curvature and printer spacing should not be treated as measurements. A doubtful drawing label has the same evidential status as a doubtful prose word.

The 44 page fragments and combined fragment were checked for structure and compiled with a temporary macro wrapper before freezing. Compilation verifies syntax, not the truth of the mathematics or the correctness of an uncertain reading. The final fragment deliberately has no preamble and does not supply definitions for the user-specified page-state macros. A reproduction must define those macros and load TikZ/tikz-cd and the standard mathematics packages.
"""
p.write_text(notation+''.join(t for _,_,t in sorted(rows))+abbreviations)
print(len(rows),'current doubt rows, including four illegible groups')
