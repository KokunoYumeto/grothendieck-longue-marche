#!/usr/bin/env python3
"""Assemble the reader's notation/legibility register and final doubt table.

Run after finalize_mechanical.py --write. Never edits transcription fragments.
The confidence downgrades below are the primary reader's assessments of
specific visually reviewed regions; the source readings remain unchanged.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_15_195-228+18_002-017'

HEADER = r'''# Doubts and notation register

## Package notation register

This register was begun with the first page and completed in the pre-context notation audit. Renderings distinguish visible forms; they do not make all occurrences of a mathematical object typographically identical when the manuscript itself varies. Cote/scan references below identify the supplied scan numbers, not the manuscript's handwritten pagination.

| Seen sign or usage | LaTeX rendering | Reading caution and checked occurrences |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes, ` ``...'' ` | Used for double quotation marks in both handwriting and typescripts; TikZ's straight double quotes are arrow-label syntax, not manuscript punctuation. No guillemets were introduced. |
| Exclamation superscript versus prime | `^!` versus `'` | Explicitly audited across the package. No secure exclamation superscript was identified in these 49 sheets; none was supplied. The prime families listed below are retained as primes, not inferred exceptional-inverse-image notation. |
| Single and double prime on involutions | `\tau'`, `\tau''` | 15/203: one versus two upper strokes, distinguished from the separate baseline exclamation point near the real Frobenius remark. |
| Prime on groups, torsors, subgroups and periods | `G'`, `P'`, `P''`, `H'`, `U'`, `B'`, `L'`, `j'_0`, `\omega'_i`, `\eta'_i` | 18/6, 11–13; compare the ordinary primes on `f'`, `g'`, `v'`, `X'` and basis vectors in the reused sheets and 15/223, 18/15–16. |
| Ambiguous trailing upper stroke | `\unsure{G_\xi(\mathbb Z)|G_\xi(\mathbb Z)'}` | 15/213: possible prime versus following punctuation remains unresolved. |
| Fibre-functor xi | `\xi` | Recurrent in 15/195–223. Distinct from the uncertain normalizing letter in 18/12. The point/locality symbol in 18/12 is `\unsure{\xi_0|g_0}`. |
| Zeta/xi in normalized periods | `\unsure{\zeta|\xi}^{-1}` | All four occurrences in 18/12 carry the same unresolved reading; no interpretation from period theory was used to select the letter. |
| Fundamental-group index or exponent | `\pi_1`, `\pi^1` | Both occur. The raised `1` in 15/223 was retained; it was not silently converted to a subscript or a profinite-completion mark. Other uncertain upper marks remain marked locally. |
| Decorated versus plain T | `\mathbb T`, `T`, `T_\alpha`, with `\unsure` where needed | 15/195, 199, 207, 213; first-sheet decoration is especially weak. A script or double-struck alphabet was not imposed globally on the plain forms. |
| Decorated M | `\mathbb M` and plain `M` | Categorical notation and individual motives are retained with the written decoration; see 15/217–221. |
| Script function spaces and filter letters | `\mathcal K`, `\mathcal K_+^*`, `\mathfrak B`, `\mathfrak F` | Reused Haar-measure sheets, especially 15/224–228. |
| Underlined Lie-algebra letters | `\underline g`, `\underline h` | Reused Lie-algebra sheets use underlining; it was not replaced by a Fraktur alphabet. The primes on these letters remain separate. |
| Diagonal-map capital letter | `\unsure{\Gamma|T}` | All four occurrences in 15/210 and both in 18/16 are consistently marked; the typescript glyph alone does not securely settle the alphabet. |
| Half-linear / half-simple notation | `\frac12` | Retained as the written fraction before the French adjective, rather than expanded to “semi-”. |
| Lowercase u versus n in a group exponent | `G^{\unsure{u|n}}` | 18/12: all occurrences consistently marked; not normalized using the conjecture's expected meaning. |
| Lowercase k versus capital K | `\unsure{K|k}` where unresolved | 18/11: the first two consequent degree denominators visibly differ from the later short lowercase form; both are flagged. |
| Latin l versus Greek ell | `l` or `\ell` | Preserved by sheet. In particular the local list in 18/5 reads an ell-adic qualifier; it has not been changed to a p-adic qualifier. |
| Constant sheaves and underlined cohomology | `\underline Q`, `\underline Z`, `\underline H`, `\underline{\underline H}` | 18/7 and 15–17: underlines and double underlines are kept where visible, with doubtful supports and indices marked locally. |
| Plain stroke versus arrow | `\arrow[...,dash]`, `\arrow[...,no head]`, or a plain relation stroke | No arrowhead is supplied where the ink shows only a stroke. Difficult overwritten direction/decorations remain inside `\unsure` at the corresponding diagram position. |
| Inclusion, isomorphism, inequality | `\subset`, `\supset`, `\simeq`, `\leq`, `\geq` | Read by direction. The inequalities in 18/11 and the reused Haar-measure sheets were checked individually. |
| Cancellation, insertion and marginal text | `\deleted`, `\inserted`, `\margin` | Cancellations remain readable in the source where possible; nested alterations are preserved. Margin notes are not silently merged into running text. |
| Underlining | `\uline`, `\uuline` | A third visible stroke is represented by nested single/double underlining where necessary; underline extent is preserved rather than expanded to a whole sentence. |
| Written ellipsis | `\ldots` or literal periods | Used only where periods/ellipsis are actually visible. They are not omission placeholders. |
| Incomplete syntax or unexpected mathematics | literal transcription plus local doubt where warranted | Examples include missing parentheses in 18/9, the uncompleted endings in 18/7 and 17, and the visible `n-p` / `i+p` degrees in 18/15–17. No mathematical correction was made. |

## Reading doubts

Every final `\unsure` and `\illegible` occurrence is listed below, including those inside cancellations, insertions and diagrams. “Line” means the physical line of the corresponding individual page `.tex` file, not an inferred manuscript line and not a line in the combined fragment. The complete raw arguments, positions and alternatives are also retained in `records/final_doubt_rows.jsonl`.

Confidence is confidence in the proposed reading, not in the truth of the mathematics: **medium** means a plausible but unresolved reading; **low** means that cancellation, compression, faintness or overlap materially prevents a secure choice. No doubt has been promoted to a confident reading merely because it is mathematically plausible. `\illegible{n}` occurs only for prose after attempted reading; no mathematical symbol is replaced by that macro.

'''

TAIL = r'''
## Abbreviations encountered

These expansions are editorial possibilities, supplied only here. They are not substituted into the diplomatic transcription. A form may have more than one expansion, and uncertain abbreviated readings remain uncertain.

| Form | Possible expansion |
|---|---|
| alg., Alg. | algébrique(s); algebra / algèbre in a title |
| ann. | anneau |
| applic. | application(s) |
| autom. | automorphisme(s) |
| bigrad. | bigraduation |
| can. | canonique / canoniquement |
| car., caract. | caractéristique |
| cat. | catégorie |
| cf., Cf. | confer; compare |
| Ch., Coh. | cohomologie; the short form in 18/17 is uncertain |
| chap., Chap. | chapitre |
| comm. | commutativité / commutatif, according to the phrase |
| comp. | composante; in the field diagram, compositum/composition is a possible sense |
| cond. | condition(s) |
| conj. | conjugaison / conjecture, depending on the occurrence |
| Conj. | conjecture |
| conn. | connexe |
| constr. | construction |
| cor., Cor. | corollaire; “cor.” after réseau may instead be a compressed lattice qualifier |
| cov. | covariant; only an uncertain alternative after réseau |
| d.f. | dimension finie |
| deg., degr. | degré |
| décr. | décroissante |
| déf. | définition / défini |
| dém. | démonstration |
| diff. | différentielle |
| dim | dimension |
| e.g. | exempli gratia |
| ess. | essentiellement |
| ex., exer., exerc. | exemple / exercice, according to the sheet |
| exple | exemple (uncertain abbreviated reading) |
| ext. | extension |
| fonct., Fonct. | foncteur(s) |
| fpqc | fidèlement plat et quasi-compact |
| fr. | fractions |
| géné., génér\textsuperscript{t} | généralement |
| Gén. | généralisation; only an alternative to Cor. in 18/17 |
| géom. | géométrique |
| gr., gr.pe | groupe |
| hom. | homogène / homomorphisme, by context |
| i.e. | id est |
| indép. | indépendant |
| int. | intégrale / intérieur, depending on the phrase; uncertain in 18/11 |
| irred., irréd. | irréductible |
| isom | isomorphe / isomorphisme |
| l. | ligne (in typescript correction lists) |
| lint. | linéairement (uncertain compressed form) |
| loc. cit | loco citato |
| loct | localement |
| m\textsuperscript{e} | même |
| m.m. | possibly monomorphisme; unresolved in 18/11 |
| mod | modulo |
| mult. | multiplication |
| nb, nbs, nbres | nombre(s) |
| NB, N.B. | nota bene |
| néc. | nécessaire |
| Ob | objets |
| ord. | ordinaire / orienté; cancelled short form in 18/17 uncertain |
| p., pp. | page(s) |
| p-fait | parfait |
| par. à | par rapport à |
| Pb | problème |
| pl. | place(s) |
| prop. | proposition |
| pt, pts | point(s) |
| quelc. | quelconque |
| rad. | radical |
| rat | rationnel |
| réd | réduit |
| représ. | représentation(s) |
| rés | résiduel |
| resp. | respectivement |
| s.t | sont |
| sec. | section |
| seult. | seulement |
| sol. | solution |
| syst. | système |
| th. | théorème / théorie, by occurrence |
| tjs | toujours |
| top, topol. | topologique |
| tot. | totalement |
| tr., trans., transc. | transcendance / transcendant |
| ts, tt | tous / tout |
| uni. | unique |
| val. | valeur / valuation |
| var. | variété |
| Vect. | vectoriel |
| vraimt | vraiment |
| Math. Scand. | Mathematica Scandinavica |
| J. of Approx. Theory | Journal of Approximation Theory |
| J. of Funct. Analy. | Journal of Functional Analysis |
| Proc. Amer. Math. Soc. | Proceedings of the American Mathematical Society |
| Trans. Amer. Math. Soc. | Transactions of the American Mathematical Society |
| Bull. Amer. Math. Soc. | Bulletin of the American Mathematical Society |
| Proc. | Proceedings |

## Legibility and limits of this transcription

All 49 supplied nonblank scan pages, their 49 whole-page images and 98 overlapping half-page images were read by the primary transcriber, in the specified order, without OCR. Each page was saved before proceeding, and all pages received a later second visual reading before context was opened. Additional crops, rotations and contrast inspection were used only as viewing aids; they did not generate text.

The reused typescripts are generally clearer than the handwritten sheets, but correction lists contain small punctuation, underlining and mathematical alphabets that remain vulnerable to error. The highest-risk handwriting is in the cancelled or compressed passages of 15/195, 207, 219, 225 and 227, the crowded lower-left edge and marginal notes of 18/11, the cancelled draft 18/12, and the overwritten cohomology diagrams and NB in 18/15–17. Faint ordinary words may be less secure than a familiar mathematical formula; uncertainty is therefore retained in prose as well as symbols. The few physically unreadable prose spans remain localized and counted approximately.

The diagram source preserves the identified objects, relations, arrow directions and labels, including cancelled material and explicit doubts. Its spacing and the curves of the nonmathematical TikZ drawings are approximations of the handwriting, not a geometric facsimile. Page-state macros require definitions supplied by the reader's LaTeX wrapper; the requested fragments deliberately contain no preamble or macro definitions. The records distinguish mechanical validation from the primary reader's visual audit. Completion of the reading is not a claim that all ambiguous handwriting has been resolved.

The page fragments and combined transcription are the canonical final text. The dated writing scripts and initial per-page inventories in `records/` document the first pass and may contain superseded readings; the final inventory and this register were regenerated after the visual audit. Any interpretation or proposed alternative prompted by context belongs only in the research notes.
'''

def main():
    rows=[json.loads(x) for x in (ROOT/'records/final_doubt_rows.jsonl').read_text().splitlines() if x.strip()]
    for row in rows:
        # Regions assessed by the reader as especially insecure.
        cote,scan=int(row['cote']),int(row['scan'])
        raw=str(row.get('argument_raw',row.get('reading','')))
        if (cote,scan)==(15,225) or ((cote,scan)==(15,227) and any(x in raw for x in ['anabélien','voire','global','l\'un'])):
            row['confidence']='low'
        if (cote,scan)==(18,11) and any(x in raw for x in ['réseau cor.','classe','définit','donc']):
            row['confidence']='low'
        if (cote,scan)==(18,12) and any(x in raw for x in ['pré-minimal','localité','connu','beta','beta']):
            row['confidence']='low'
        if (cote,scan)==(18,15) and any(x in raw for x in ["c'est acquis",'déjà','sinon']) or ((cote,scan)==(18,17) and any(x in raw for x in ['Y|X','i|*','a|Z','Z|a'])):
            row['confidence']='low'
    (ROOT/'records/final_doubt_rows.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
    def esc(x):return str(x).replace('|',r'\|').replace('\n',' ')
    lines=['| File / cote | Scan | TeX line | Reading | Alternatives | Confidence |','|---|---:|---:|---|---|---|']
    for r in rows:
        alt=r.get('alternatives',[])
        if isinstance(alt,list):alt=' / '.join(alt)
        lines.append('| '+ ' | '.join([str(r['cote']),str(r['scan']),str(r.get('line',r.get('tex_line',''))),'`'+esc(r.get('reading',''))+'`',esc(alt),r['confidence']])+' |')
    table='\n'.join(lines)+'\n'
    (ROOT/'records/final_doubt_table.md').write_text(table)
    (ROOT/f'{PREFIX}_doubts.md').write_text(HEADER+table+TAIL)
    print(f'Wrote doubt register with {len(rows)} occurrences.')

if __name__=='__main__':main()
