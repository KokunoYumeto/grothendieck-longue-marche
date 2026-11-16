#!/usr/bin/env python3
"""Build the final uncertainty index from the reader's current page files.

This is a structural extraction of explicit doubt macros, not OCR or a reading
of the manuscript. The notation, caveats and abbreviation glossary below were
written by the sole reader after comparing the images.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

INTRO = r'''# Notation table

This table records the sole reader's final comparisons across the package, made before the context archive was opened. It describes transcription conventions, not corrections to the manuscript. Differences supported by the ink remain differences; unresolved differences remain marked in the text.

| Recurring sign or alphabet | LaTeX transcription | Comparison and limits |
|---|---|---|
| Ordinary Latin capitals and lower-case letters | `A,B,E,F,G,M,N`, `u,v`, etc. | Case and visible strokes govern the reading. In particular the changes between `E` and `F` on 91/011–012 and between `X` and a module in 91/011 are retained. |
| Cursive category, algebra and ring letters | `\mathcal C_i`, `\mathcal U_i`, `\mathcal A^\bullet` | Compared on 90/008,010,020–024. The first category name on 90/008 remains uncertain; no alphabet is inferred solely from its role. |
| Underlined structure-sheaf O | `\underline O_X`, `\underline{O}_{X'}` | The lower stroke is distinct on 90/014,016,018 and 91/012–018. Compressed or overwritten instances on 90/020,022 and 91/005,007 retain the alternative script O. The local-ring O in the reused typed 90/025 is separately retained as script O. |
| Dual mark over B | `\check B_i` | V-shaped accent, compared on 90/008,016,018; not a hat or prime. |
| Saturation tildes | `\tilde N` | Compared on 90/002,004. Unequal presence of tildes in the last formula of 90/004 is literal; later untilded factors were not supplied with tildes. |
| Associated-sheaf tilde | `\widetilde{M_\bullet}` or the source's other visible tilde form | Kept separately from underdots and graded superscripts on 90/022–024. The insertion on 90/024 does not acquire an invisible tilde. |
| Completion hats | `\hat A`; visibly doubled hat retained | Compared in the reused typed sheets. The two hat impressions on 90/005 are not reduced to one. |
| Henselization and strict henselization | `${}^h A`, `${}^{\mathrm{hs}}A` | Left superscripts retained on 90/011,013,017,019,021,023,025; the s is not silently dropped. |
| Typed variable index resembling digit 1 | `\unsure{1|i}` | Compared on 90/007,009,017,021,023,025. In the affected variable formulas the first alternative follows the typewritten shape, even where the intended variable would normally be i. Clear handwritten i and explicit indices 1 or 2 are not changed. |
| Direct and inverse limits | `\varinjlim`, `\varprojlim` | Each direction checked; the manuscript's cancelled inductive/projective wording on 90/006 remains cancelled rather than replaced silently. |
| Coaction signs | `\delta`, `\Delta` | Lower- and upper-case forms kept distinct on 90/004,008,018. |
| Straight headed, headless and hooked maps | `\to`, `\longrightarrow`, `-`, TikZ `no head`, `\hookrightarrow` | No head is supplied from mathematical expectation. Numerous headless maps remain on 90/008,016,020 and 91/010–018; the arrow by X/R on 91/013 retains its directional alternative. |
| Wavy map and headless correspondence | `\rightsquigarrow`; `\unsure{\sim|\mapsto}` or a literal headless relation | The reused typed arrows on 90/007,009 have right heads; the handwritten correspondences on 90/020,022 do not establish the same head. |
| Underlined Gamma, dot and deleted star | `\underline{\Gamma}`, `\Gamma^\bullet`, `\Gamma_{\deleted{*}}^\bullet` | Compared on 90/020–024. Underlining, upper dots, lower dots and crossed stars are separate marks; their presence is not normalized between formulas. |
| Coproduct and unindexed sum | `\coprod_n`, `\sum M^i` | The symbol on 90/020 is a coproduct; the sum on 90/022 has no supplied summation index. |
| Primes, exclamation/question marks, stars and small dots | `'`, `\prime`, `!`, `?`, `*`, `\cdot` as individually read | The raised sign by G_i on 91/008 remains `?` with `!` alternative. Both small marks before the stars in 91/016 remain prime/circle alternatives; the first M_v on 91/017 has dot/prime alternatives; the irregular raised mark in the upper-left Hom of 91/018 remains star/prime. None is normalized to a familiar operation. |
| The local-test label | `(L)` | The native-resolution letter on 91/008 has the same vertical stem and foot as 91/012; the earlier h alternative was superseded before freezing. |
| Identity component and geometric point | `G_{\bar s}^0`, bars on s | The 0 and bar remain separate from punctuation and from the uncertain raised mark on the earlier G_i of 91/008. |
| Generic point on the last sheet | `\eta` | The manuscript's y-like eta is consistent within 91/018; no index is changed to match another formula. |
| Equals sign used as a verbal abbreviation | `$=$`, including `De $=$` and `lui-$=$` where written | Compared on 90/018,022 and 91/009,010,013. The sign is not expanded into “même” in the transcription. The written word “même” on 91/005 remains a word. |
| Double quotation strokes | Two backticks and two apostrophes | Used for the manuscript's double quotes throughout. No typographic curly double quotes or guillemets are substituted. |
| Underlining versus cancellation | `\uline`, `\uuline`, `\deleted` | Checked against the stroke's position, including cancelled blocks containing live insertions. Underlining inside a withdrawn passage is retained. |
| Brackets, ovals, emphasis strokes and pencil marks | `\figure{\begin{tikzpicture}…}` | Nonverbal marks are drawn, not paraphrased. Text enclosed by an oval remains text inside the approximation. The faint ovals surrounding the Hom functors on 91/016 use ellipse nodes. |
| Blank typed relations | Literal space (`\quad` where needed) | On reused typed sheets a blank is not filled with an expected relation, arrow or inequality. |

# Final doubt index

The table below is generated from every current `\unsure{…}` and `\illegible{…}` occurrence in the 39 page files. It therefore supersedes preliminary readings retained in the working JSON records; those records remain in the archive as an audit trail. Page-file names below omit the common prefix `MPL_90+91_002-018_`; **TeX line** is the line in that individual page fragment, and the short neighboring text locates the corresponding manuscript line approximately.

The first reading is the reading of the ink, not a proposed correction. “Low” means a seriously compressed, overwritten, crossed or ambiguous reading; “medium” means a plausible visible reading with a localized uncertainty. A word-count estimate in `\illegible` has low confidence and does not claim to recover the hidden word. No `\illegible` is used in place of mathematical notation. Alternatives are printed literally; a lone reading means no second reading was secure enough to offer.

| Page file | Scan | Approximate location | Current reading | Alternative / issue | Confidence |
|---|---:|---|---|---|---|
'''

SUPPLEMENT = r'''
# Other fidelity and attachment cautions

These cautions concern layout, scope or surprising literal content and are not replacements for the in-text doubt marks.

| File / scan | Location | Retained reading or issue | Confidence |
|---|---|---|---|
| 90 / 002 | top cancellations and condition c | The small cancelled fragments are separate; the A/O letter and the split condition remain doubtful. | low |
| 90 / 003,005 | missing typed relations and unfinished references | Blank relational gaps and unfinished reference fields remain blank; two hat impressions and the typed “la fibres” are retained. | high |
| 90 / 004 | final tensor formula | Later N factors lack the tildes present earlier in the same formula. | high |
| 90 / 007,009,015 | graph argument and continuation | Page 007's repeated equals sign and final “Appli-” continue to 015; the corresponding older passage on 009 is withdrawn. | high |
| 90 / 009 | remark 18.9.6 | The characteristic-zero expectation lies inside a cancelled block and ends unfinished. | high |
| 90 / 010,012 | base letters and continuation | The visible S after S′ is retained; the three-line continuation belongs to the representation argument. | medium |
| 90 / 013,019 | Ass hypotheses and proof marks | The printed conditions differ (`p∈A` versus `p∩A`); curved and vertical proof marks are drawings, not a conjectured “cf.”. | high |
| 90 / 014 | cancelled proposition and interline | The faithful-flatness proposition is withdrawn; the oval condition's attachment is less secure than its individual words. | low |
| 90 / 016 | conclusion of assertion 4 | The sentence does not visibly impose finite type on the initial O_X-G-module; no qualifier was added. | high |
| 90 / 018,020 | revisions to assertions 2 and 3 | Nested strikes, retained fragments and interlinear hypotheses are kept as states of the page. Their final intended logical combination is not reconstructed. | medium |
| 90 / 020 | end of revised assertion 3 | The isolated “à” and the unfinished phrase are retained. | low |
| 90 / 021 | compactness lemma | The text has an unindexed Y at one point and repeated punctuation; no index or stop is normalized. | high |
| 90 / 023 | cancelled universal-property paragraph | The whole hybrid formulation is withdrawn; its semi- insertions remain inside the deletion. | high |
| 90 / 024 | left margin | “Rédiger mieux…” and its later compressed words are among the least secure live marginal readings. The rising connector is drawn. | low |
| 90 / 025 | Hom statement | The singular printed “bijectif” remains after the inserted plural verb “sont”. | high |
| 91 / 005 | Artin argument | The structure-sheaf letters are partly overwritten; the upper and lower brown staple traces were treated as paper damage, not pen drawings. | medium |
| 91 / 007 | condition 7 conclusion | The manuscript concludes X=Y rather than supplying T subscripts; the word read “magique” is cancelled. | high |
| 91 / 008 | local-test phrase and interline | “voisinage ouvert induit”/“ouvert infinit.” and the localité/constructibilité insertion are insecure; they should not support an exact theorem statement without image review. | low |
| 91 / 009 | last corollary | The transporter phrase lies below the ends of some diagonal strokes; it is included in the surrounding withdrawn corollary, with scope noted as uncertain. | low |
| 91 / 011–012 | module notation | F appears after E, X appears in the modularity tests, and “fibre générique” is visible; the text is not repaired to an expected flattening criterion. | high |
| 91 / 012 | margin and condition (ii) | The word after T is read irréduc./primaire, and the first symbol of (ii) is read varphi_2/p_2 (pr_2 also conceivable); the label pr_1 on the arrow is clearer. | low |
| 91 / 013 | bracket beside functor cases | The fpqc equivalence is positioned at its insertion, but its exact attachment is geometrically uncertain. | medium |
| 91 / 016 | differential formulas and pale ovals | Small primes/circles are insecure, including both marks before stars; the two pale functor ovals and the margin oval/connector are reproduced. | low |
| 91 / 017 | proof and marginal reduction | The colon after v is retained. “sans doute sur” is plausible but compressed, so it is not treated as an unqualified secure self-flag. | medium |
| 91 / 018 | margin, diagrams and ending | “Tout reste à rédiger” retains uncertain words; the stars marking two torsor-square corners are distinct from the irregular raised mark in the Hom square. The last sentence really stops at “aux coins”. | medium |

# Abbreviations met

The expansions below are editorial suggestions **only in this glossary**. No abbreviated manuscript word has been expanded in the transcription. Punctuation varies in the manuscript and is retained there; a doubtful abbreviated spelling is still marked in its page file.

| Written form | Possible expansion or sense |
|---|---|
| `tt`, `tte` | tout, toute |
| `ts que` | tels que |
| `ds` | dans |
| `i.e.` | id est; c'est-à-dire |
| `p.ex.` | par exemple |
| `N.B.`, `NB` | nota bene |
| `O.K.`, `OK` | okay; accepted at this point |
| `cf.` | confer; compare |
| `resp.` | respectivement |
| `th.`, `Th` | théorème |
| `prop.`, `Prop.` | proposition |
| `cor.`, `Coroll.` | corollaire |
| `Dém`, `dém.` | démonstration |
| `Cond.`, `cond.` | condition(s) |
| `gr.`, `gr` | groupe |
| `schém.`, `préschém.` | schéma, préschéma |
| `mor.`, `morph.` | morphisme(s) |
| `hom`, `homs`, `Hom` | homomorphisme(s); Hom notation where mathematical |
| `s-foncteur` | sous-foncteur, probably; the exact prefix is doubtful |
| `syst.` | système |
| `ens`, `ens.` | ensemble(s) |
| `pt`, `pts` | point(s) |
| `loc.` | local, localement |
| `noeth.`, `noeth` | noethérien |
| `irréd.`, `irréduc.` | irréductible |
| `alg.` | algébriquement, algèbre or algébrique according to phrase |
| `Alg.` | algèbre |
| `géom.` | géométriquement |
| `hyp.` | hypothèse(s) |
| `rés.` | résiduel |
| `car.` | caractéristique |
| `dim` | dimension |
| `val` | valuation |
| `qu.`, `quasi` | quasi |
| `cpt`, `qu. cpt` | compact, quasi-compact |
| `sép.`, `(qu) sép.` | séparé, (quasi-)séparé |
| `coh`, `coh.` | cohérent |
| `t.f.` | type fini |
| `prés. finie` | présentation finie |
| `inv`, `inv.` | inversible |
| `rel`, `rel.`, `rel/S` | relatif; relativement à S |
| `fid`, `fid.`, `fid plat` | fidèlement; fidèlement plat |
| `imm`, `imm.`, `imm.f.`, `immers.` | immersion; immersion fermée |
| `quasi-proj.` | quasi-projectif |
| `surj.` | surjectif |
| `repr.` | représentation or représentable, according to phrase |
| `isom.`, `Isom.` | isomorphe |
| `quac.` | quasi-compact, probably; the spelling is uncertain |
| `ass.` | associatif |
| `op.` | opération(s) |
| `contt` | contenant |
| `canoniqut` | canoniquement |
| `trivialt` | trivialement |
| `triv.` | trivial |
| `ssi` | si et seulement si |
| `impliq.` | implique |
| `Suppos.` | supposons |
| `const.` | construction or constante; insecure in its cancelled phrase |
| `infinit.` | infinitésimal, probably; the reading is uncertain |
| `fact direct` | facteur direct |
| `comm` | commutatif (for a diagram) |
| `princ.` | principal |
| `form.` | formellement / formant; insecure in the phrase on 91/018 |
| `élémts` | éléments; the abbreviated reading itself is uncertain |
| `ess. libre` | essentiellement libre |
| `f.s.` | faut et suffit, probably |
| `chgt` | changement |
| `par. cqt` | par conséquent |
| `Sp` | spectre |
| `spectr.` | spectre |
| `lim.` | limite |
| `pr.` | projection |
| `Cent.`, `Norm`, `Transp` | centralisateur, normalisateur, transporteur (mathematical names) |
| `Top.gén.` | Topologie générale (reference abbreviation) |
| `chap.` | chapitre |
| `éd.` | édition |
| `etc.` | et cetera |
| `CQFD.`, `cqfd.` | ce qu'il fallait démontrer |
| `fpqc` | fidèlement plat et quasi-compact |
| `EGA` | Éléments de géométrie algébrique (reference abbreviation) |
| `=` in prose | même; the sign is transcribed as a sign, not expanded |

# Legibility and limits of trust

All 39 full-page images and all 78 half-page images were personally read by one reader, without OCR. The second audit again compared each page and its halves with its saved transcription; further crops and rotations were used only for visual inspection. Mechanical assistance checked file structure and completeness, not handwriting or mathematical interpretation.

The reused typed sheets are generally clearer than the handwritten notes, but their blacked-out cancellations, missing typed relation signs, small variable indices and handwritten revisions are locally difficult. Their inverted orientation and separate original foliation were kept distinct from scan order. The handwritten sheets range from reasonably open writing to extreme compression, especially in interlines and margins. The least trustworthy live passages are 90/002 and 024, 91/008, the margin and factorization symbols on 91/012, the N.B. on 91/013, and the tiny decorations and marginal phrases on 91/016–018. Broadly cancelled paragraphs on 90/014,020,023 and 91/007,009 require separate caution even where many words are legible.

The drawings are vector approximations of visible geometry, including faint proof marks and ovals; they are not facsimiles. Insertion attachment and the full scope of diagonal cancellations can remain less certain than the words themselves. The explicit uncertainty index should therefore accompany use of the transcription. Apparent grammatical or mathematical anomalies, dangling clauses and unfinished sentences were not repaired.

The 39 page fragments and their exact concatenation were checked structurally. A compilation wrapper is supplied among the validation records, but no successful typeset compilation is claimed: this environment has TeX executables without the required class/package tree (including article, amsmath, ulem and tikz-cd). The deliverable is the requested preamble-free LaTeX fragment, with standard LaTeX and TikZ content inside the specified state macros.
'''

def escaped(s):
    return s.replace('|', r'\|').replace('\n', ' ').strip()

def code(s):
    s = escaped(s)
    longest = max([len(x) for x in re.findall(r'`+', s)] or [0])
    delimiter = '`' * max(2, longest + 1)
    return delimiter + ' ' + s + ' ' + delimiter

def body_at(s, start):
    depth = 1
    p = start
    while p < len(s):
        if s[p] == '\\':
            # Only literal escaped braces suppress brace nesting.
            if p + 1 < len(s) and s[p+1] in '{}':
                p += 2
                continue
        if s[p] == '{': depth += 1
        elif s[p] == '}':
            depth -= 1
            if not depth: return s[start:p], p+1
        p += 1
    raise ValueError('unclosed explicit doubt macro')

rows = []
counts = {'unsure': 0, 'illegible': 0}
for page in sorted((ROOT/'pages').glob('*.tex')):
    text = page.read_text()
    record = json.loads((ROOT/'records'/page.with_suffix('.json').name).read_text())
    for hit in re.finditer(r'\\(unsure|illegible)\{', text):
        macro = hit.group(1)
        value, end = body_at(text, hit.end())
        counts[macro] += 1
        line = text.count('\n', 0, hit.start()) + 1
        before = re.sub(r'\s+', ' ', text[max(0,hit.start()-48):hit.start()]).strip()
        after = re.sub(r'\s+', ' ', text[end:end+40]).strip()
        location = f'TeX {line}; …{before} ⟦…⟧ {after}…'
        first, sep, alternative = value.partition('|')
        confidence = 'medium' if macro == 'unsure' else 'low'
        if sep or len(value) > 32: confidence = 'low'
        # Use the root reader's recorded literal confidence when a distinctive
        # reading is found in the matching page record. Never elevate to high.
        candidates = []
        for d in record.get('doubts', []):
            if len(d) >= 4 and len(first) >= 3 and (first in d[1] or d[1] in value):
                candidates.append(d[3])
        if 'low' in candidates: confidence = 'low'
        if macro == 'illegible':
            first = '\\illegible{' + value + '}'
            alternative = f'Approximately {value} physically unreadable word(s); no wording supplied'
        elif not sep:
            alternative = 'Reading doubtful; no second alternative supplied'
        rows.append('| ' + ' | '.join([
            code(page.name.replace('MPL_90+91_002-018_','')),
            str(record['scan']), code(location), code(first),
            code(alternative), confidence
        ]) + ' |')

assert len(rows) == sum(counts.values())
out = INTRO + '\n'.join(rows) + '\n' + SUPPLEMENT
(ROOT/'MPL_90+91_002-018_doubts.md').write_text(out)
(ROOT/'validation'/'doubt_index_counts.json').write_text(json.dumps({**counts,'total':len(rows)},indent=2)+'\n')
print(f'Built {len(rows)} current doubt rows: {counts}')
