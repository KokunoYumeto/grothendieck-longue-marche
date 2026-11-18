from pathlib import Path
p=Path('MPL_159/MPL_159_doubts.md')
s=p.read_text()
body=s[s.index('## Doubts by page'):]
notation=r'''# MPL 159 — Notation and doubts

## Notation table

Maintained during the personal visual reading and compared across the full series before any context contents were opened. A recurring sign is not silently standardized where the ink differs; unresolved distinctions remain marked at each occurrence. The table identifies transcription conventions, not mathematical identifications.

| Ink / recurring usage | LaTeX convention | Scans / cautions |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes | Used where paired quotation marks occur; isolated ditto strokes on 31 remain isolated ditto strokes. |
| Auxiliary module, later Hodge bundle | `\Omega` | Auxiliary module on 2–10; Hodge bundle on 11–13; formal augmentation quotient on 25–34. These are local definitions, not one object throughout. |
| Small differential omega | `\omega` | Plain on 11–13. A section and a bundle are not distinguished by an editorial font change. |
| Underlined small omega | `\underline{\omega}`; doubtful occurrences give underlined/plain alternatives | Distinct lower strokes occur on 18–22. The music-paper ruling and cancellation strokes make several occurrences uncertain, especially on 18–19. Clear local differences are retained. |
| Script torsor / tangent letter | `\mathcal T` | Torsor on 2–9 and tangent sheaf on 12. Kept distinct from `\Gamma`. |
| Symmetric / divided / exterior powers | `\operatorname{Sym}^n`, `\Gamma^n`, `\bigwedge^n` | Especially 11–13; their different glyphs are preserved. |
| Script structure sheaf and ideal; later plain ideal | `\mathcal O`, `\mathcal J`; `J` | Indices follow the page even when another base is mathematically plausible. Plain `J` on 33–34 is not converted to script. |
| Completed objects | `\widehat S`, `\widehat P`, `\widehat L` | Hats follow the written object; tensor-completion hats are retained separately. |
| Point and algebra actions | `u_a^*`, `u_{a*}` | Star position is significant on 4–7; module-action superscripts retained. |
| Script de Rham object | `\mathcal{DR}` | 11–13. The separate Lie-algebra letter on 16 and 20 is tentatively `\mathfrak g`, explicitly uncertain. |
| Dual vee | `\check\Omega`, `\check{\mathcal{DR}}`, `^\vee` | Placement follows the ink and is not flattened to a star. |
| Zigzag stratification label | `\unsure{\xi\|\zeta}` | Persistent on 15–23. Its shape is reproducible but its identification as xi or zeta is unresolved. |
| Exclamation exponent | `^!` | Hom locus on 17–18; Iso loci on 27. A separate dot is visible; these are not primes. |
| Primes and double primes | `'`, `''` | In particular d′/d″ on 16 and the comparison calculations on 25–32. |
| Teichmüller group glyph | `\unsure{\gamma\|\Gamma}` | 18; kept distinct from an unambiguously written section-space Gamma. |
| Group notation | `GL(r)`, `GP(r)`, `\operatorname{Aff}(r)` | The author's notation is not changed to PGL. |
| Principal-parts symbol | `P^n_{X/S}` | On 13 the two disputed exponents are `3+` / `2+`, with the first alternative following the enlarged ink. |
| Formal algebra versus projective bundle | `\mathcal P` versus `P`; local alternatives on 25 | The formal-algebra script on 26 and 33–34 is distinct from the paired object `(P,\sigma)`. Three occurrences on 25 remain uncertain. |
| Barred coefficient sign | `\unsure{\varpi_i\|\bar\omega_i}` | 28–34. The upper sweep/bar is clear but does not securely decide between these two typeset glyphs. Early formulas on 31 have a different, apparently ordinary omega with index −1 and are marked separately. |
| Normalization groups and orders | `G`, `G_0`, `G_1`, `G_2`; `J^3`, `J^4` | All indices and orders follow individual occurrences. In particular 27's `G_2` is not normalized to `G_0`. |
| Underlining and deletion | `\uline`, `\uuline`, `\deleted` | Lower bars on symbols use standard mathematical underlining. Scan 26's inserted “très régulière” has an explicitly doubtful deletion/underlining state. |
| Foliation | `% archive foliation: n` | Pencil corner foliation is recorded as a comment, not an authorial `\mspage`. No secure authorial page numbering was identified. |

'''
append=r'''
## Abbreviations encountered

Expansions below are interpretive aids only. They are not inserted into the transcription; doubtful abbreviations remain doubtful there. Punctuation and plural endings can vary by occurrence.

| Written form | Probable expansion / explanation |
|---|---|
| `af.`, `aff.` | affine; the short `af.` occurrence is retained as written. |
| `alg.`, `Alg.`, `algéb.` | algébrique; Algèbre where capitalized in an algebra designation. |
| `an.` | analytique. |
| `augm.` | augmentation / augmenté(e), depending on syntax. |
| `aut.`, `auto`, `autom.`, `autom` | automorphisme(s). |
| `bij.` | bijection / bijectif. |
| `can.`, `canon.` | canonique. |
| `car.`, `car` | caractéristique. |
| `cat.` | catégorie. |
| `condit.` | condition. |
| `conn.`, `conn`, `connex.` | connexion(s); in a hypothesis on a curve, connexe. |
| `corr.` | correspondance. |
| `déf.` | défini / défini par / définition, according to the occurrence. |
| `diff.` | différentielle(s). |
| `dim`, `dim rel.` | dimension; dimension relative. |
| `ens.`, `ens` | ensemble. |
| `ép(i)`, `épi` | épimorphisme. |
| `eq.`, `équiv.` | équivalence / équivalent. |
| `etc.` | et cetera; on 25 this competes with the unresolved `étg`. |
| `ex.` | extension or exacte, according to the occurrence. |
| `ext.`, `int.` | extérieur / intérieur in automorphism groups; extension where used for an extension. |
| `f.`, `t.f.` | The finite-type abbreviation on 17 is uncertain; probably “type fini.” |
| `form.` | formel(le). |
| `géom.`, `geom.` | géométrique(s); accent retained or absent as in the transcription. |
| `gr.`, `gpe`, `ss-gpe` | groupe; sous-groupe. |
| `hom.` | homomorphisme. |
| `i.e.` | id est. |
| `id`, `id.` | identité. |
| `inf.` | infinitésimal, where used of an infinitesimal neighbourhood. |
| `inv.`, `inv` | inversible or invariant, as indicated by the local syntax. |
| `iso`, `iso.`, `isom`, `isom.` | isomorphisme. |
| `lin.`, `lin` | linéaire. |
| `loc.`, `Localt`, `localt` | local / localement. |
| `Mod.`, `loc. lib` | modules; localement libres. |
| `N.B.`, `NB` | nota bene. |
| `néc.`, `néces.` | nécessairement. |
| `op.` | opération(s). |
| `Pb` | problème. |
| `pol.`, `princ.` | polarisation / polarisé(e); principal(e). |
| `Pr.`, `Prop.`, `prop.`, `Th.` | proposition; théorème. The opening abbreviation on 26 is doubtful. |
| `proj.` | projectif / projective. |
| `pt`, `pt.` | point. |
| `quelc.` | quelconque(s). |
| `réd.` | réduction / réduit, according to local syntax. |
| `rel.`, `relat.` | relatif / relative. |
| `Rem.` | remarque. |
| `resp.` | respectivement; on 34 the competing reading `unq.` is unresolved and has no secure expansion. |
| `rev.` | revêtement. |
| `schém.`, `sch.` | schéma. |
| `sect.` | section. |
| `sép.` | séparée. |
| `ser.` | probably “serait/seront”; the ending is doubtful on 22. |
| `tjrs` | toujours. |
| `top.` | topologie. |
| `tors.` | torseur. |
| `tt`, `tte` | tout; toute. |
| `VA` | variétés abéliennes. |
| `vois.` | voisinage. |
| `WTS` | Possibly “want to show” in the cancelled English-looking fragment on 32; both the reading and expansion are low confidence. |
| `Q.S.` | Unresolved label before the stabilizer question on 32; no expansion supplied. |
| `régt` | Possible abbreviation for “régulière(s)” in the doubtful insertion on 34; “un peu fort” remains the competing reading. |

## Legibility and confidence

The ink ranges from clear blue writing to faint grey pencil or faded ink; music-paper ruling, show-through, overwritten symbols, folds, cropped right edges, and large cancellations complicate several pages. All 32 supplied whole-page images and their 64 supplied halves were personally read in order without OCR, and each page received a separately logged second comparison. Additional crops and rotations were used only to inspect difficult ink. The page files preserve unresolved readings rather than supplying words or factors from mathematical expectation.

I trust the continuous, uncancelled prose and many of the main displays more than the scratch calculations and overwritten insertions. The least secure areas are the cancelled passages on 4 and 12; the fragmented constructions on 13; the dense two-column sheet 18 and underlined-omega distinctions on 18–19; the overwritten local calculation on 20; the revised existence sentence on 25; the left insertion on 26; the scattered lower calculations on 27; the cropped formula edge on 29; the early coefficient formula and cancellations on 31; the sloping margin and cancelled last line on 32; and the left margin and parenthetical qualifications on 34. The recurring coefficient glyph on 28–34 and the stratification glyph on 15–23 remain deliberately unresolved throughout.

“Medium” in the occurrence table means a plausible reading with imperfect letter or stroke evidence, not a mathematical verification; “low” indicates weak or competing visual evidence. Newly introduced doubts conservatively receive low confidence unless an explicit visual assessment already supplied another label. These are qualitative confidence labels, not probabilities. `\illegible{n}` is restricted to a few obscured words and never substitutes for a mathematical symbol; no claim of error-free palaeographic transcription is made.

The final fragment and every page are frozen before the context is opened. Any later suggestion from the context is recorded only as a research reading question and never incorporated into the frozen transcription.
'''
p.write_text(notation+body.rstrip()+'\n'+append)
