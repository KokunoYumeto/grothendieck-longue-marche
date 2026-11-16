"""Assemble the post-freeze research apparatus; never write transcription files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / 'records'
PREFIX = 'MPL_33_147-181+34_002-017'


def read(name):
    return (REC / name).read_text(encoding='utf-8')


def between(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def change(text, old, new):
    assert old in text, f'Missing assembly-edit anchor: {old[:100]}'
    return text.replace(old, new, 1)


d = read('research_duality_final.md')
m = read('research_monodromy_final.md')
r = read('research_reused_sheets_final.md')
i = read('research_integration.md')

d_notes = '### D01. ' + between(d, '### D01.', '## B. Separate inventory')
d_notes = change(
    d_notes,
    'the final (H^{2d|pd}$X,$',
    r'the final `H^{\unsure{2d|pd}}(X,`'
)
m_notes = between(m, '## Research notes', '## Compact inventory')
m_notes = change(
    m_notes,
    'finite generation of its adic inverse limit',
    r'finite generation of the adic inverse limit $\varprojlim_\nu H^i(X_{\bar K},\mathbb Z/\ell^\nu)$'
)
m_notes = change(
    m_notes,
    r'$H^{\unsure{i|1}}(X_{\bar K})\unsure{?}$',
    r'`H^{\unsure{i|1}}(X_{\bar K})\unsure{?}`'
)
r_notes = '### R01. ' + between(r, '### R01.', '## Exact title and numbering catalogue')
r_notes = r_notes.replace('## Two supplemental notes requested after the first memo\n\n', '')
r_notes = change(r_notes, 'and Jan-Erik Roos under a title', 'and “JAN-ERIK ROOS” under a title')
r_notes = change(r_notes, 'but explicitly defers its proof to §3;', 'but says “qui sera démontré dans le § 3”;')
r_notes = change(r_notes, 'to distinguish fields, together with', 'to “distinguer les corps entre eux,” together with')
r_notes = change(r_notes, 'The opening definition presents the Jacobson condition', 'The opening definition of “préschéma de Jacobson” presents the condition')
r_notes = change(r_notes, 'The editor calls the last sentence of old proposition 11 false', 'The editor writes “sauf la dernière phrase qui est fausse” about old proposition 11')
r_notes = change(r_notes, 'then asserts properness of addition on C × C', 'then says addition on $C\\times C$ “est propre”')
r_notes = change(r_notes, 'the preceding description of the ambient weak space and cone', 'the preceding hypotheses on $F$ and $C$')
r_notes = change(r_notes, 'distinguish separation in each variable from a pairing separating in both.', 'distinguish “séparante en $F$” from separation in the other variable and in both.')
r_notes = change(r_notes, 'and the algebraic dual acquires no unstated topology.', "and the continuous dual $E'$ receives no topology unless one is explicitly specified.")
r_notes = change(r_notes, 'postpones its proof to use “le th. de Grothendieck.”', "postpones its proof to proceed “à l'aide du th. de Grothendieck.”")
r_notes = change(r_notes, 'The closedness argument writes the relevant subspace', 'The assertion “Si les $G_i$ sont fermés” is proved by writing the relevant subspace')
r_notes = change(r_notes, 'literally begins with x in R', 'literally begins with “$x$ in $R$”')
r_notes = change(r_notes, 'Lemma 1 identifies the exceptional quotient', 'Under the regular-local hypotheses with $n>1$, Lemma 1 identifies the exceptional quotient')
r_notes = change(r_notes, 'Under its equal-dimension, common-residue-field and maximal-ideal-extension hypotheses,', 'For the two regular local domains under its equal-dimension, common-residue-field and maximal-ideal-extension hypotheses,')
r_notes = change(r_notes, 'asserts that a completion of the overring', 'uses “any completion of” the overring and asserts that this')
r_notes = change(r_notes, 'The Fredholm-reduction section, operator algebra, symbol construction and section-number progression', 'The heading “Reduction of a singular equation to the Fredholm case,” operator algebra, symbol construction and section-number progression')
r_notes = change(r_notes, 'why zero global symbol implies', 'why zero “global symbol” implies')
r_notes = change(r_notes, "the numerator polynomial's n subscript", "the odd-index integrand polynomial's $n$ subscript")
r_notes = change(
    r_notes,
    'For real H = ℓ²(ℕ₀), x = e₀ and G = span{eₙ + n e₀ : n ≥ 1}, G excludes e₀ but is norm dense, since n⁻¹(eₙ + n e₀) converges to e₀ and then every basis vector lies in its closure. Thus σ(H,G) is Hausdorff and weaker than the ordinary weak topology, while both topologies agree on the weakly compact unit ball by the compact-to-Hausdorff argument. Its continuous dual is G, whereas every supporting functional of that ball at e₀ is a positive multiple of e₀, so no continuous supporting hyperplane remains.',
    r'For real $H=\ell^2(\mathbb N_0)$, $x=e_0$ and $G=\operatorname{span}\{e_n+n e_0:n\geq1\}$, $G$ excludes $e_0$ but is norm dense, since $n^{-1}(e_n+n e_0)\to e_0$ and then every basis vector lies in its closure. Thus $\sigma(H,G)$ is Hausdorff and weaker than the ordinary weak topology, while both topologies agree on the weakly compact unit ball by the compact-to-Hausdorff argument. Its continuous dual is $G$, whereas every nonzero supporting functional of that ball at $e_0$, oriented to attain its maximum there, is a positive multiple of $e_0$, so no continuous supporting hyperplane remains.'
)
# Treat the Stacks Project as one continuously updated reference, with exact tags.
r_notes = re.sub(r'n\.d\.-[abcd]', 'n.d.', r_notes)
r_supplement = read('research_reused_sheets_supplement_final.md')
r_notes += '\n\n### R27. ' + between(r_supplement, '### R27.', '## Search provenance')
i_notes = '### I01. ' + between(i, '## I01.', '## I05.')
i_notes = re.sub(r'^## (I0[234]\.)', r'### \1', i_notes, flags=re.M)
i_notes = change(i_notes, 'Illusie (2026, opening historical sections)', 'Illusie (2026, author version p. 4, “The writing up: Exposés I, II, III”)')
i_notes = change(i_notes, 'our proposal adds a three-column comparison of the actual maps', 'our proposal adds a comparison of map existence, invertibility and compatibility')

intro = r'''# Research notes: Montpellier cotes 33 and 34, scans 147–181 and 003–017

## 1. Scope, evidence and locator conventions

These **100 research notes** accompany the **49 retained scan pages**: 34 from cote 33 and 15 from cote 34. They were written after the diplomatic transcription, its second visual audit and the notation audit were complete, and after all 49 page files and the combined transcription were frozen at **2026-11-16 00:02:21 UTC**. The context archive was then opened; neither the context nor the literature was used to revise a frozen reading. The transcription and its inventory preserve the supplied scan order, including all reused typed sheets; the discussions below are arranged by subject to make their dependencies easier to inspect.

There is one item per research point: **D01–D40** for the handwritten duality and trace material; **M01–M28** for the local-monodromy exposé; **R01–R28** for the reused typed sources; and **I01–I04** for the historical and publication comparisons requested by the plan. Each item has one to four prose sentences; file, locator, kind, confidence and context fields are metadata. Formulas quoted from a frozen reading are evidence for that reading, including when their type or scope is questioned. An `\unsure{...}` marks the transcriber's uncertainty, not an authorial question unless an actual question mark is separately observed. The dedicated inventories below distinguish questions, promises, completed local checks, cancellations and our own proposed tests.

**Current-file key.** A locator such as **33/172:4–6** means file **33.pdf**, scan **172**, approximately lines 4–6 of `pages/MPL_33_147-181+34_002-017_33_scan172.tex`; the same convention applies to cote 34. A short `scanNNN.tex` in an M item means `pages/MPL_33_147-181+34_002-017_34_scanNNN.tex`. Line numbers refer to the frozen per-page TeX, not image baselines or lines in the combined file. R-item source voices are those of the typed text; its presence among papers in Grothendieck's hand does not establish that he authored it.

**Earlier-context key.** **A** means supplied `same_cote_33/MPL_33_002-049_notes.md`; **B** means supplied `same_cote_33/MPL_33_098-146_notes.md`. Their N/T/section IDs and cited scans remain **first-pass, unchecked leads**; earlier scans themselves were not supplied. `README.md` supplies the **S19** programme of questions, source accounting and comparisons; `notes/RESULTS_STATE.md` supplies statuses and source-file references. A note's “Register IDs” field is a reference to that register, not an assertion that the present note proves the entry. All 44 returned-package entries and the seven other substantive rows are explicitly disposed of in section 10.

**Interpretation limits.** The finite-field Ext example, infinite-dimensional biduality example, smooth-curve codimension test and quartic Picard example test precisely stated interpretations of the frozen wording. They do not recover a missing hypothesis, settle an uncertain symbol, or establish historical novelty. Our dense-subspace construction and central-extension example are explicitly our deductions. Primary comparisons use the exact passages listed in section 11; the limits of original-source collation remain stated.

## 2. Handwritten duality, trace and research programme
'''

self_flags = r'''## 6. Standing question: steps explicitly marked unverified, conditional or deferred

The following is an index of the author's or typed source's own words. A proof obligation that is subsequently addressed is marked as such; a cancelled caution is not left live. Purely editorial reading doubts, type mismatches identified by us and unfinished formulas without an authorial warning are discussed in the numbered notes, but are not automatically counted as the author's doubts. In the reused sources, “author” means the voice of that source, whose individual identity may be unknown.

### 6.1. Cote 33 handwritten leaves

| Frozen locus | Source words or narrowly delimited feature | Status on these leaves; research note |
|---|---|---|
| 150:32 | “hom. en sens inverse”; “montrer que c'est un isomorphisme” | Invertibility remains a stated task after constructing a reverse arrow; D04. |
| 152:14–16 | “Ceci ne devrait pas offrir de difficulté”; bracketed isomorphism expectation | Canonicity and invertibility are expected; the adjacent signs/cones wording is too uncertain to turn into a definite sign-check quotation; D05. |
| 154:11–19; 156:3–11 | “appliquée deux fois”; “la résolution des singularités à la Hironaka est possible”; “Il semble préférable” | Conditional local Künneth input followed by a tentative finite-map route, whose final sentence ends with a dash; D07–D09. |
| 158:25,40–49 | “ne doit être autre”; “on aura”; “plats de type fini en chaque degré !” | Expected local/global compatibility and explicit model qualification; D10–D11. |
| 165:7,11–14 | “Applications — possibles”; “Consulter notes de Verdier” | Possible injective-dimension applications and a direction to consult another source; D18. |
| 165:19–21 | “On peut globaliser” | Proposed extension to relative schemes over a ringed étale site, ending as a sketch; D19. |
| 166:2–18 | “Sujets de recherches” | Research programmes a–e; the distinct cancellation of f is recorded in section 7; D20–D22. |
| 167:14–27 | “+ résolution et pureté sur X” | Explicit dependency of the local-duality scope, not a theorem proved on this leaf; D23. |
| 170:2 | “Énoncés plausibles” | Conjectural heading for the displayed category equivalences; D25. |
| 170:30–36 | “formelle”; “utiliser la bidualité” | Forward direction asserted formal; reverse direction left as an instruction ending with a dash; D26. |
| 170:38 | “en admettant l'équivalence (**)” | Gorenstein-fibre conclusion explicitly conditional on (**); D28. |
| 172:2–3 | “à vérifier !”; uncertain generalization instruction | Explicit warning on the proposed theorem; the uncertain Ext notation remains a separate reading question; D29–D30. |
| 172:16 → 174:2–3 | “par passage à la limite”; “Attention, est-il vrai”; “fibres injectives ??” and a separate “?” | Reduction stops at the constructible-approximation question; deleted “ses” and uncertain inserted “filtrante” retained; D31–D32. |
| 180:7 | “dualité parfaite ??” | Open-term perfection explicitly questioned; D37. |

### 6.2. Cote 34 handwritten exposé
'''

m_flags = between(m, '### Promises, cautions and steps explicitly set for verification', '### Other literal future formulations')
m_future = between(m, '### Other literal future formulations and compressed inputs', '### Major withdrawals')
r_flags = between(r, '## Explicit self-flags and withdrawal boundaries', '**Observed local replacements')
r_flags = r_flags.replace('| 151:18 |', '| 151:18 |').replace('not yet a proved theorem for every topology here. |', 'not yet a proved theorem for every topology here; R25. |')
r_flags = r_flags.replace('for the reorganized number. |', 'for the reorganized number; R26. |')
r_flags = r_flags.replace('| 155:20 |', r'| 155:8 | “une référence pour $B(\mathbb N)$” | Explicit bibliographical request; intended reference and expansion of the notation not supplied; R27. |' + '\n| 155:20 |')
r_flags = r_flags.replace('| 168:8 |', '| 161:6 | “On verra que”; “le topos associé”; “beaucoup plus intrinsèque” | Promised later explanation of the relation between a site presentation and its topos; no precise general theorem formulated here; R28. |\n| 168:8 |')

withdrawals = r'''## 7. Withdrawals, corrections and replacement arguments

The inventory gives both observed states and their loci. Cancellation of a proof or a programme entry is not by itself a refutation of its theorem; reports about a missing earlier book page have only one observed locus in this package.

### 7.1. Cote 33 handwritten revisions

| Earlier or cancelled locus | Live or subsequent locus | What the evidence supports |
|---|---|---|
| 148:14–15, cancelled $L\to L$ | 148:15, composite ending in $M$ | Local formula replacement; the live target remains a type question, D02. |
| 152:23–25, deleted affine-generator proof of the named Verdier lemma | 154:3–20, local Künneth strategy; 156:3–11, finite-map refinement | A changed proof route, not a written denial of the lemma, D04 and D06–D09. |
| 154:17, target finite-Tor and constructibility conditions deleted | Same line, inserted category bound with frozen `D^{\unsure{-|+}}` uncertainty | Revised target hypotheses; the sign is not normalized from expectations, D08. |
| 158:10–16, immediate cup-product construction deleted | 158:18–25, application of $R\Gamma$ and expected global pairing | Restarted local/global construction, D10. |
| 165:23, deleted possible “article séparé” | 166:23, parallel deletion of depths/Lefschetz research item f | Two observed programme cancellations; neither supplies a theorem-refutation statement, D22. |
| 180:12–15, cancelled earlier arrows | 180:21–27, local-cohomology/double-dual route | Revised sketch with unresolved comparison and degree conventions, D38. |
| 180:54, cancelled tensor–Hom expression | 180:55, distinct surviving identity | Keep both formulas and their distinct scope; no universal claim of falsity, D40. |

### 7.2. Cote 34 revisions
'''
m_withdraw = between(m, '### Major withdrawals and their replacement loci', '## Titles and pagination')
m_withdraw = re.sub(r'\| R(\d\d) \|', r'| MW\1 |', m_withdraw)
m_withdraw += r'''
| MW14 | 004:6,13,22, inserted “comm.” and “pour $i=1$” | Same loci; properness and $i=1$ retained in the reordered Picard sentence | Commutative-group and degree-one/proper scope retained; M03/M04 |
| MW15 | 007:20, deleted “Sa puissance” | Same line, inserted “Sa puiss. tensorielle” | Tensor-power operation made explicit; negative-power convention still a comparison question; M10 |
| MW16 | 011:4, deleted “l'isomorphisme de” | 011:4, inserted “l'opération naturelle”; 011:10, inserted “primitives” | Natural action distinguished from generator choice; uncertain overwritten text at 011:6 remains unresolved; M16 |
| MW17 | 012:10, deleted “extension” | Same line, inserted “clôture” before “séparable” | Separable closure specified; the repeated field labels remain separate reading questions; M17 |
'''
withdraw_end = r'''### 7.3. Reused typed sheets and reported external retractions

| Cancelled or earlier locus | Replacement or report locus | Classification and limit |
|---|---|---|
| 175:8, deleted chart-coordinate formula | 175:8, inserted $y_i=x_i/x_1$ | A same-line formula replacement within Lemma 1, not withdrawal of the whole lemma; R16. |
| 181:4, cancelled sign transcribed uncertainly as `<` | 181:4, inserted non-strict bound $q\leq m$ | Same-line inequality revision; preserve the uncertainty of the cancelled sign; R19. |
| Old-book p. 120, line 9, **not supplied** | 155:26, “la conjecture de la l. 9 est fausse” | Reported refutation with a counterexample sketch; original conjecture cannot be recovered from the notice alone; R08–R09. |
| Old-book p. 102, proposition 11's last sentence, **not supplied** | 157:12, “sauf la dernière phrase qui est fausse” | Reported error, with an implication involving vague metrizability; missing original hypotheses still matter; R10. |

## 8. Standing question: title sheets, headings and page counts

**No retained leaf states an explicit total page count.** The scan set contains **34 cote-33 pages** and **15 cote-34 pages**; these are counts of the supplied retained images, not manuscript claims about the length of a work. Blank 33/169 and 34/002 were omitted from the supplied set. Source pagination, archive numerals, internal theorem/formula numbers and references to older book pages are recorded separately below.

### 8.1. Reused source families, the cover and the research list
'''
r_titles = between(r, '## Exact title and numbering catalogue', '## Explicit self-flags')
r_titles = r_titles.split("The root's handwriting/duality memo",1)[0].strip()
r_titles = r_titles.replace('### Exact research-list headings on scan 166', '#### Research-list headings on scan 166')
r_titles = r_titles.replace('`Proposition 3.`', '`Proposition 3.-`')
r_titles = r_titles.replace('`Théorème 1.` and `Lemme 2.`', '`Théorème 1.-` and `Lemme 2.-`')
r_titles = r_titles.replace('`Remarque 1.` and `Remarque 2.`', '`Remarque 1.-` and `Remarque 2.-`')
r_titles = r_titles.replace('Fredholm case`;', 'Fredholm case.`;')
r_titles = r_titles.replace('No new section title; Zariski-site exposition.', '`Proposition et définition 1.-`; Zariski-site exposition.')
r_titles = r_titles.replace('No new section title; open-immersion covering condition.', '`Démonstration de la proposition 1.-`; open-immersion covering condition.')
r_titles = r_titles.replace('`§ 2. Caractérisation', '`Résumé des propositions 2 et 3.-`; `§ 2. Caractérisation')
d_titles = between(d, '## C. Titles, continuation labels, and page accounting', '## D. Register disposition')
d_titles = d_titles[d_titles.index('| Scan(s)'):]
d_titles_intro = r'''### 8.2. Other handwritten duality headings and continuation labels

The 17 handwritten mathematical leaves treated in D01–D40 have small lower numerals 147, 149, 151, 153, 155, 157, 159, 161, 164, 165, 166, 169, 171, 173, 175, 177 and 179, respectively. These numerals equal the scan number minus one; they do not express a total length. Scan 166 appears in both tables because it is both a research-list heading and a mathematical programme.
'''
m_titles = between(m, '## Titles and pagination of all fifteen retained scans', '## Primary comparisons')

search_section = r'''## 9. Search provenance and remaining collation work

Each numbered note was tested against the supplied context for the same objects, notation and words. A zero exact match is recorded as such and supplemented only by an identified thematic or provenance lead; it is not converted into a novelty claim. The search records preserve the actual queries and hits or no-hit results, including supplementary and adaptive queries.

| Final items | Actual context-search record | Coverage |
|---|---|---|
| D01–D40 | `records/research_duality.md`, section F and adaptive-query follow-ups | Both earlier-note files, README and results register; note-level IDs, scans and status fields in the final items |
| M01–M28 | `records/research_monodromy.md`, per-candidate search records | Both earlier-note files and the supplied programme/register comparisons; exact earlier-note and register IDs distinguished |
| R01–R24 and reused-source catalogue | `records/reused_context_search.json`; interpretation in `records/research_reused_sheets.md` | Actual searches of all four supplied context files |
| R25–R26 | `records/reused_context_search_supplement.json` | Actual supplementary searches of all four context files |
| R27–R28 | `records/reused_context_search_final_supplement.json` | Actual final supplementary searches of all four context files, including no exact notation/promise match |
| I01–I04 and register-comparison candidates | `records/integration_context_search.json`, generated by `records/integration_context_search.py` | Actual searches of all four context files; unused I05–I10 are retained as working comparisons, not extra final note items |

The records contain earlier working formulations as part of the audit trail; this final notes file supersedes them. In particular, the final mathematical tests retain their interpretation conditions, the final R13 distinguishes the continuous dual from an algebraic-dual convention, and the current title census uses the retained scan counts above. No exact operator-source publication or expansion of [A6], [A7] or [18a] was established. `records/operator_source_search.md` documents a bounded publication-identification attempt; its possible matches remain unverified. The earlier Abhyankar suggestion remains B N56's low-confidence lead. Full collation of the manuscript with original SGA 5 and SGA 7 remains open; the particular printed and primary comparisons actually inspected are listed next.
'''

register = read('results_disposition.md')
register = change(register, '## Disposition of the supplied results register', '## 10. Disposition of the supplied results register')
register = change(register, 'a doubtful sign-verification margin', 'a margin with unresolved signs/cones wording')
register = register.replace('33/177–179', '33/177,179')
register = register.replace('self-flag inventory below', 'self-flag inventory in section 6')

primary = read('primary_sources.md')
primary = change(primary, 'opening historical sections |', 'author version p. 4, subsection “The writing up: Exposés I, II, III” |')
primary = change(
    primary,
    '| Stacks Project, [0HB2]',
    '| Stacks Project, [0DW6](https://stacks.math.columbia.edu/tag/0DW6) | §47.21, Definition 47.21.1 | Local Gorenstein condition through the coefficient ring as a dualizing complex; coefficient-level comparison only |\n| Stacks Project, [0G2B](https://stacks.math.columbia.edu/tag/0G2B) | §63.11, Lemma 63.11.1 and the displayed counit | Extraordinary inverse image is right adjoint to proper-support direct image for the stated separated finite-type, quasi-compact/quasi-separated, torsion-coefficient setting; comparison with the support question on 33/160 |\n| Stacks Project, [0HB2]'
)
primary_table = between(primary, '## Root independently retrieved', '## APA reference forms')
refs = primary.split('## APA reference forms',1)[1].strip()
primary_intro = r'''## 11. Checked primary comparisons and APA references

These sources were retrieved after the transcription freeze on **16 November 2026**. The exact inspected passages and limits below govern the citations in the numbered notes. A modern theorem may test a chosen interpretation or supply a comparison, but cannot determine a doubtful stroke or transfer its hypotheses silently into the diplomatic text.
'''
internal_refs = r'''

*Context for the research notes: Package 212 (cotes 33, 34).* (2026, November 12; addenda November 15). [Supplied planning document, `README.md`].

*Our results so far on these folders (package 212: cotes 33, 34).* (2026, November 15, 16:00 UTC). [Supplied research-status register, `notes/RESULTS_STATE.md`].

*MPL_33_002-049_notes.* (2026). [Supplied first-pass, unchecked research notes; `same_cote_33/MPL_33_002-049_notes.md`; cited as A with exact note IDs and scans].

*MPL_33_098-146_notes.* (2026). [Supplied first-pass, unchecked research notes; `same_cote_33/MPL_33_098-146_notes.md`; cited as B with exact note IDs and scans].

The present manuscript witness is cited by cote, scan and frozen TeX line throughout; archive date ranges are not assigned as composition dates to individual sheets. Named source text on a reused leaf is attributed only to the extent visible in its own title or independently established by a checked comparison.
'''

parts = [
    intro, d_notes,
    '## 3. Local monodromy and henselian valuation theory', m_notes,
    '## 4. Reused typed sources', r_notes,
    '## 5. S19: folder placement and publication comparisons', i_notes,
    self_flags, m_flags,
    '### 6.3. Other future formulations and compressed inputs in cote 34', m_future,
    '### 6.4. Reused typed sources: deferred steps, checks and reports', r_flags,
    withdrawals, m_withdraw, withdraw_end, r_titles,
    d_titles_intro, d_titles,
    '### 8.3. Cote 34: all fifteen retained leaves', m_titles,
    search_section, register, primary_intro, primary_table,
    '### APA references', refs, internal_refs
]
out = '\n\n'.join(part.strip() for part in parts) + '\n'

# A vertical bar remains a table separator even within a Markdown code span.
lines = []
for line in out.splitlines():
    if line.startswith('|'):
        line = re.sub(r'`([^`]+)`', lambda match: '`' + match.group(1).replace('|', r'\|') + '`', line)
        line = re.sub(r'\$([^$]+)\$', lambda match: '$' + match.group(1).replace('|', r'\vert ') + '$', line)
    lines.append(line)
out = '\n'.join(lines) + '\n'

ids = re.findall(r'^### ([DMRI]\d\d)\.', out, re.M)
expected = [f'{letter}{n:02d}' for letter, maximum in [('D',40),('M',28),('R',28),('I',4)] for n in range(1,maximum+1)]
assert ids == expected, (len(ids), ids)
assert r'$H^{\unsure' not in out
assert '(H^{2d|pd}$X,' not in out
(ROOT / f'{PREFIX}_notes.md').write_text(out, encoding='utf-8')
print(f'Assembled {len(ids)} research notes; {len(out.split())} words; {len(out.encode())} bytes')
