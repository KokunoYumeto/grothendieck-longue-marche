#!/usr/bin/env python3
"""Assemble the human-reviewed notation/abbreviation record and exact doubt index."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
assert 'transcription frozen' not in (ROOT/'progress.log').read_text()
rows=list(csv.DictReader((ROOT/'records/uncertainty_occurrences.tsv').open(),delimiter='\t'))
intro=r'''# MPL_33_002-049 — notation, doubts and abbreviations

## Notation table

This is the single notation table for cote 33, scans 002–049. It began with the first page and was completed after the serial visual reading and the second visual audit, before the context archive was opened. The table records the forms used in the transcription; it does not repair the mathematics. Recurring variants were compared against the images, and unresolved differences remain marked in place.

| Recurring sign or letter family | LaTeX transcription | Visual distinction and reconciliation |
|---|---|---|
| Ordinary Latin site and scheme letters | `X`, `Y`, `S`, `U`, `V`, `k` | Preserve case, primes, bars and placement; do not supply a missing prime from the geometry. |
| Étale suffix and tilde over site | `_{\mathrm{ét}}`, `\widetilde X` | Accent and tilde are distinct; abbreviated prose forms are retained as written. |
| Script structure-sheaf O | `\mathcal O`, occasionally `\underline{\mathcal O}` | Underlining is retained where visible (004); it is not changed to a Gothic letter. |
| Underlined typescript ideals and category letters | `\underline p`, `\underline m`, `\underline C` and analogous letters | Typescript underlining is retained as underlining; no inferred Gothic alphabet is substituted. |
| Handwritten integer/complex coefficient symbols versus upright typed symbols | `\mathbf Z`, `\mathbf C`; `\mathrm Z`, `\mathrm R` | The handwritten and typed alphabet styles are kept distinct; literal dimensions such as the 4 in scan 049 are retained. |
| Pullback star and direct-image star | `f^*`, `f_*` | Superscript versus subscript is taken from the ink. A small doubtful star in 034 remains marked. |
| Proper-support notation on R | `R^i_!f_*`, `R_!f_*` | The exclamation is attached to R where written, including the headings in 014 and 018; it is not moved to f. |
| Extension by zero / ordinary lower shriek | `i_!`, `f_!` | Kept separately from the support notation on R; scan 020 explicitly contains both. |
| Cancelled lower shriek | `R^{-i}_{\deleted{!}}`, `R^{2d-i}_{\deleted{!}}` | Both right-hand ! marks in 048 are cancelled. The ! in the intervening parenthetical sentence is live and remains live. |
| Ambiguous overwritten R subscript | `\unsure{\deleted{!}\|\xi}` | Scan 018: cancellation shape compared with 048; crossed ! is the first reading, xi remains an alternative. |
| Ordinary primes and multiple primes | `'`, `''` | Primes on objects remain distinct from exclamation marks and prose quotation marks. |
| Complex degree marks and duals | `\bullet`, `*`, `\vee` | A complex dot, a star and a dual vee are not interchanged; particularly checked in 038–040 and 048. |
| Derived-category bounds | `D^+`, `D^-`, `D^b`, `D` | Bounds retained separately at each occurrence, including the unbounded claim in 042. |
| Derived Hom and underlined derived Hom | `R\operatorname{Hom}`, underlined forms as written | Underlining distinguishes internal from ordinary symbols only where the ink supplies it; no missing underline is inferred in 048. |
| Supported sections/local cohomology | `\Gamma_Y`, `\underline\Gamma_Y`, `H^i_Y`, `\underline H^i_Y` | Underlines and support indices remain distinct from global cohomology and from the unrelated root-system Gamma. |
| Local-class beta | `\underline\beta` in 022/024; `\beta` in 026 | The visible underline is restored in 022/024; its absence in 026 is preserved. The cancelled epsilon naming in 022 is retained. |
| Local-class gamma | `\gamma`, `\underline\gamma`; `\unsure{\gamma\|\sigma}` in 024 | Clearer forms in 026/028 support gamma; the less decisive forms on 024 retain their explicit alternative. |
| Connecting boundary | `\partial_n`, with `\unsure{\partial_n\|\delta_n}` in 024 | Compared with the clearer boundary in 028; no unmarked normalization of the doubtful stroke. |
| xi and epsilon | `\xi`, `\varepsilon` | The dubious lattice generator in 017 remains `\unsure{\xi_i\|\varepsilon_i}` with the xi-like ink first. |
| Curly nu in typescripts | `\unsure{\nu_i}`, `\unsure{\nu(i)}` | Comparable small curly forms in 011, 027 and 031 are consistently nu first; doubts are retained. |
| F and the second complex letter | `F`, `\unsure{G\|C}` | Every occurrence of the ambiguous second complex letter on 040 is explicitly G/C; the variable is not decided by the expected formula. |
| i / u for the open immersion | `\unsure{i\|u}` in 022 | All indistinct repeated occurrences are marked; the clearly written initial u is retained. |
| Round subscript on root lattices and stabilizer | `_{\unsure{o\|0}}` | Twenty-five o-shaped circles in 013/015/017/019/021/023/037/049 do not distinguish letter o from numeral 0. The visible o-like form is first throughout. |
| Distinct root-lattice subscript 2 | `\Gamma_2` | Clear 2 in 023, visually distinguished from the round o/0 glyph, is not normalized away. |
| Simple roots, highest root and weights | `\alpha_i`, `\widetilde\alpha`, `\omega_i`, `\rho` | Tildes, subscripts and all coefficients kept separately; doubtful numeric subscripts/bounds in 029/031 remain marked. |
| Curly epsilon basis and dual basis | `\varepsilon_i`, `\varepsilon_i^*` | The star stays on the basis vector, not on the index; separate from xi coefficients. |
| Bilinear pairing | `(x\|y)` | The short vertical stroke is preserved; no angle-bracket convention is substituted. |
| Equivalence/isomorphism/equality | `\simeq`, `\sim`, `=`, and stacked forms as written | Wavy strokes, equals strokes and arrowheads are read individually. |
| Plain connector | `\mathbin{-}` or `\arrow[...,no head]` | No inferred arrowhead: checked especially in 003, 018, 020, 036 and 038. |
| Arrows and inclusions | `\to`, `\longrightarrow`, hooked/dashed TikZ arrows, `\subset` | Direction, hooks, dashes and absence of heads retained from the page; uncertain symbols marked within diagrams. |
| Limits | `\varinjlim`, `\varprojlim`, `\lim` | Direction is marked doubtful when the tiny stroke is weak (002/004); no direction is supplied to a plain lim. |
| Inequalities | `<`, `>`, `\leq`, `\geq`, `\ne` | Strict versus non-strict is kept separate; scan 010's `\unsure{>\|\geq}` is unresolved. |
| Prose double quotation marks | two backticks followed by two apostrophes | Consistent TeX double quotes; the closing quote around “dérivé gauche” in 038 was confirmed on enlarged ink. |
| Ditto marks | `\text{'' }` | The repeated-value mark in 012 is a ditto mark, not an unmatched opening prose quote. |
| Underline and double underline | `\uline{…}`, `\uuline{…}` | Distinct from mathematical bars and cancellation strokes. |
| Ellipses and unfinished expressions | dots exactly as visible, including `....`, `.....`, `\ldots` | No editorial omission marks added. Unclosed source parentheses and unfinished expressions remain unclosed. |
| Insertions, deletions and marginalia | `\inserted`, `\deleted`, `\margin` | Attachment follows the caret/position; nested cancellations remain nested, including the wholly cancelled sheet 047. |
| Section and folio numbers | literal section numbers; `\mspage{…}` for visible handwritten foliation | Repeated/changed section numbers and competing foliation are preserved. Source pagination is distinguished from the small folio sequence in the title register; some upper page numbers are also encoded with `\mspage`. |

## Doubts: every explicit uncertainty occurrence

**233 `\unsure` occurrences; no `\illegible` placeholders.** Each row indexes one occurrence, including repeats within the same line. “Line” gives the reproducible line in the named per-page `.tex` fragment, rather than pretending that the reflowed paragraph has the same lineation as the scan; the inventory supplies physical locations. File `33.pdf` is the archive file, and scan numbers identify the corresponding page file unambiguously.

Confidence concerns the proposed reading of the ink, not mathematical truth: **high** would mean a strong reading with a small residual ambiguity; **medium** means a plausible first reading with incomplete strokes or a credible alternative; **low** means faint, overwritten, clipped or seriously ambiguous ink. None of these marked readings is promoted to “high” merely because it fits a familiar formula. A dash in the alternative column means that no second defensible reading has been identified, not that the first reading is certain.

| File | Scan | Line in page fragment | Reading | Alternative | Confidence |
|---|---:|---:|---|---|---|
'''
# Human confidence assignments based on the root reader's visual audit.
low_scans={3,36,47}
low_pairs={
 (2,'plus'),(2,'bien avant'),(2,'donnant'),
 (4,r'\xi_X'),(4,'hensélien et'),(4,r'\widetilde F'),
 (6,'8°)'),(6,'si on fait|sauf'),(6,'avec'),(6,'Hom'),(6,'Ét'),(6,'les'),(6,'à rédiger'),(6,'anneau'),(6,'espace'),(6,'schéma'),(6,'A pour un faisceau'),(6,'faisceau'),
 (8,'maintenant'),(8,r'X_\xi'),(8,'Gagas'),(8,'t'),
 (12,'Soient'),(12,'donc'),(12,'un'),(12,'a'),(12,'fai'),(12,'Défin.'),(12,'définition'),(12,'lisse'),
 (14,'avec|sans'),(14,'lissité'),(14,'compactifiables'),(14,'On factorise en'),(14,"X'"),(14,r'\perp'),(14,'imm.'),
 (16,'un morphisme'),(16,'ou prop.'),(16,'directes'),(16,'génériques'),
 (18,'préschémas|premiers'),(18,'ou plus'),(18,'présch.'),(18,'égale car.'),(18,'en'),(18,r'\deleted{!}|\xi'),
 (20,'certaines'),(20,'égales'),
 (22,'n'),(22,r'H^1'),
 (28,'il va résulter des'),(28,'C'),(28,'th. de'),(28,'rat'),(28,'prouver'),(28,'pour'),(28,'A'),(28,'ici'),(28,'le compa'),(28,'ramenant'),
 (30,r'\Gamma'),(32,'trace|hom'),(34,'Catégories dérivées'),
 (38,'triangulés|triangulées'),(38,'doivent'),(38,'distingués'),(38,'idem'),(38,'y'),
 (42,'cd'),(46,r'\S'),(48,r'S=\operatorname{Spec}k'),(48,'2d-i')
}
def split_top(s):
 depth=0
 for i,c in enumerate(s):
  if c=='{': depth+=1
  elif c=='}': depth-=1
  elif c=='|' and depth==0:return s[:i],s[i+1:]
 return s,''
def code(s):
 return '`'+s.replace('|',r'\|').replace('\n',' ⏎ ')+'`' if s else '—'
out=[intro]
for r in rows:
 s=r['content'];reading,alt=split_top(s);scan=int(r['scan'])
 conf='low' if scan in low_scans or (scan,s) in low_pairs else 'medium'
 out.append(f"| 33.pdf | {scan:03} | {r['source_line']} | {code(reading)} | {code(alt)} | {conf} |\n")
out.append(r'''
## Abbreviations encountered

Expansions below are interpretive aids only. They are not inserted into the transcription; an expansion with alternatives remains uncertain. Capitalization and punctuation variants are grouped here, although each occurrence remains literal in the page files.

| Form(s) on the pages | Tentative expansion or interpretation |
|---|---|
| Alg., alg. | Algèbre / algèbre(s); a bibliographic title in some typescripts |
| alg.top.; alg. top. | algèbre(s) topologique(s) |
| augm. | augmentée(s) |
| bilin. | bilinéaire |
| can. | canonique |
| car.; car | caractéristique(s) |
| cat. | catégorie |
| cf; cf. | confer / compare |
| chgts | changements |
| chap. | chapitre |
| coalg. | coalgèbre |
| coh. | cohomologie / cohomologique, according to context |
| comm. | commutative(s), including the bibliographic title Algèbre commutative |
| conn. | connexe(s) |
| cons.; constr. | constructible(s); `par constr.` on 009 means par construction |
| Cor.; cor. | corollaire |
| cpt.; cpts; quasi-cpt | compact; compacts; quasi-compact |
| ct.; cts | constant / constants (the latter reading itself doubtful on 044) |
| deg.; dim.; Dim.; codim | degré; dimension; codimension |
| déf.; Défin. | définition |
| Dém | démonstration |
| div. | diviseur(s) |
| éd. | édition |
| élts; élts. | éléments |
| Ens; ens | ensembles |
| ét.; Ét | étale(s); the isolated capitalized reading on 006 is doubtful |
| Ex; Ex.; ex. | exemple(s) |
| ext.; Ext | extension; capitalized in `Ext de base` on 034, distinct from the mathematical Ext functor |
| factor. | factorisation |
| fond | fondamentale(s) |
| Gal | Galois / groupe de Galois |
| GAGA; Gaga; Gagas | Géométrie algébrique et géométrie analytique, used for comparison assertions; the plural-looking form on 008 remains doubtful |
| gr. | groupe or gradué, according to context |
| Géom.; géom. | Géométrie / géométriquement |
| hom; hom. | homomorphisme |
| hyp; hyp. | hypothèse(s) |
| i.e.; i.e | id est / c'est-à-dire |
| imm. | immersion |
| int. | intersection |
| isom; isom. | isomorphisme / isomorphe |
| loc; loc.; localt; loc\textsuperscript{t} | localement; the last two forms are doubtful readings |
| mod. | modulo |
| mult. | multiplication |
| n°; n\textsuperscript{o} | numéro |
| NB; NB.; N.B | nota bene |
| noeth | noethérien |
| OK.; OK | approval/agreement mark; not expanded in the transcription |
| ouv. | ouverte |
| p.ex.; p.ex | par exemple |
| P. | page, in the editorial references of 009 |
| Pb | problème |
| pr. | propre, in the doubtful support label on 036 |
| présch. | préschéma(s), doubtful on 018 |
| proj. | projectif |
| prop. | proposition in bibliographic references; propre in `X prop. sur k` |
| pt; pt. | point(s) |
| qu. | quasi, in qu. cpt., qu. sép. and qu. proj. |
| qconques; quelc. | quelconques / quelconque(s) |
| qt | uncertain cancelled fragment on 026; perhaps an abandoned start of quand, with no secure expansion |
| rat | rationnel, within a heavily cancelled passage on 028; expansion tentative |
| resp. | respectivement |
| rés. | résiduel(le)s in 004/006; résolutions in 038 |
| SGA | Séminaire de géométrie algébrique |
| sing. | singularités |
| slt | seulement |
| ssi | si et seulement si |
| spect. | spectre |
| strict.t | strictement |
| supp. | support(s) |
| sép.; sép | séparé / séparablement, according to context |
| t.f. | type fini |
| Th.; th.; th; théor. | théorème |
| tjrs | toujours (reading doubtful on 010) |
| top. | topologie / topologique(s) |
| tt | tout / toute / tous / toutes, according to context |

## Legibility and limits of confidence

All 48 whole-page images and all 96 supplied half-page images were personally read in the serial first pass, followed by a separate visual audit of each of the 48 pages. No OCR was used and no page transcription was delegated. The context archive remained closed throughout these readings and the notation reconciliation.

The clean blue typescripts are generally more secure than the fast cursive notes, but faint overtyping, handwritten indices, line-end damage and apparent typescript errors remain material. The recurrent small round subscript cannot be confidently distinguished as o or 0. The most fragile handwritten regions are the pale pencil diagrams of **003**, the dense/cancelled GAGA passage of **006**, the first comparison formula and marginal prose of **008**, the cancelled starts and tiny margin on **012**, the overwritten purity qualification and abandoned compactification passage of **014**, the constructibility criterion on **016**, and the inserted qualifications and overwritten R subscript of **018**. The cancelled point-class discussion on **028**, the large revised diagrams of **036**, the opening of **038**, the ambiguous second complex letter throughout **040**, and the cancelled title and final functor on **048** also deserve particular caution. The entire reused sheet **047** is crossed through and has especially dense local blackouts; its two best-effort readings should be treated as low confidence.

The diagrams and drawings are TikZ reconstructions of visible marks, not inserted scan images. Their connectivity, labels, direction and cancellation state were checked against the scans; exact handwriting shape and incidental pen curvature cannot be reproduced perfectly. The irregular diagram on **036** and the pale diagrams on **003** remain the least secure geometrically. Small nonverbal strokes are retained as drawings rather than assigned an unsupported verbal meaning. Source ellipses, absent parentheses, inconsistent-looking indices and striking numerical assertions are deliberately preserved; mathematical plausibility did not license an emendation.

The uncertainty index is exhaustive for the explicit doubt macros, but it is not a claim that all remaining readings are infallible. No quantitative error rate has been measured. The number of doubt marks measures recorded uncertainty, not the number of proven errors. The fragment has been checked mechanically for structure and concatenation; a complete LaTeX compilation was unavailable because the installed engines lack their required formats/packages (see `records/compilation_attempt.md`).
''')
(ROOT/'MPL_33_002-049_doubts.md').write_text(''.join(out),encoding='utf-8')
print(f'Wrote doubts table with {len(rows)} individual occurrences.')
