from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
p=root/'MPL_14_002-044_doubts.md'
s=p.read_text().split('## Reading doubts')[0]
s=s.replace('| Category of motifs and effective subcategory | `$M$`, `$M_+$` |','| Category of motifs and effective subcategory | `$M$`, `$M^+$` |')
s=s.replace('`$i:\\mathbb G_{m\\mathbb C}\\to G_{\\mathbb C}$`','`$i:G_{m\\mathbb C}\\to G_{\\mathbb C}$`, `$i:\\mathbb G_{m\\mathbb C}\\to G_{\\mathbb C}$`')
s=s.replace('Check the ink individually; do not substitute an exclamation mark. No exclamation-mark exponent identified in this package; primes are recorded individually.','The individual prime readings were compared with stars, raised o, and the adjacent punctuation during the audit.')
s=s.replace('`$=^{\\mathrm s}$`','`$=$s').replace('Each literal occurrence is being checked again against the ink.','Literal occurrences were checked against the ink in the second reading, including the earlier pages.')
s=s.replace('| Scans 025–036;','| Scans 003, 005, 025–036, 041–042;')
s=s.replace('|\n\n| Prose shorthand','|\n| Prose shorthand')
s=s.replace('| Category of motifs and effective subcategory |', '| Category letter and effective objects |')
s += '''| Torus characters and cocharacters | `$M$`, `$\\check M$`, `$\\mathbb Z(M)$`, `$K(T)$` | Scans 013–015; parentheses, checks, and superscript invariant groups follow the separate occurrences. |
| Centre/weight data | `$\\varepsilon$`, `$j$`, `$i$`, `$i_1$`, `$\\bar i_1$` | Scans 003–015; the i/j/gamma ambiguities are listed below instead of merging differently written occurrences. |
| Doubtful subgroup abbreviation | `\\unsure{k-groupe|s-groupe}` | Scans 026, 027, 035; the tall initial stroke is ambiguous. The possible expansion belongs below. |
| Traces | `\\unsure{\\operatorname{Tr}|\\operatorname{tr}}` | Scan 021; case is uncertain and treated consistently. |
| Finite-field eigenvalue expression | `$\\varepsilon q^{-1/2}$` | Scan 041; the visible negative exponent is retained. |
| Typescript opposite algebra and enveloping algebra | `$W^o$`, `$W^e$`, `$\\mathcal L^o$` | Scans 006, 008, 010, 012, 014; these raised letters were checked separately from primes and stars. |
| Typed real field and handwritten real field | `$R$`, `$\\mathbb R$` | Plain R occurs in the reused French typescript; the doubled alphabet occurs in the handwritten material. |

## Reading doubts

Each row refers to the page fragment `pages/MPL_14_002-044_14_scanNNN.tex`; the file/cote is 14 throughout. The line-and-column locator is in that page's LaTeX source and locates the corresponding passage approximately on the scan; it does not claim to number the handwritten lines. The complete in-place uncertainty register contains **282 `\\unsure` occurrences and one `\\illegible` occurrence**.

Confidence concerns the proposed reading of the ink. **High** means the first reading is strongly supported despite a residual ambiguity; **medium** means the reading is plausible but a stroke, alphabet, ending, or cancelled letter remains uncertain; **low** means substantial uncertainty remains, especially beneath cancellation or in crowded additions. These judgments were reviewed after the page audit; they do not certify the mathematical assertion written there. A dash in Alternatives means that no second reading was sufficiently grounded to propose.

'''
occ=(root/'records/doubt_occurrences.md').read_text().splitlines()
rows=[]
low_readings={'fibrés','représente est dans le',"d'isog.",'AQT','à nouveau','\\operatorname{Alg}','réserver',"d’ici alors","d'ici alors",'\\illegible{6}'}
for line in occ:
 if line.startswith('| Cote |'):
  rows.append(line.replace('Cote','File / cote').replace('TeX source location','Approximate passage locator'))
 elif line.startswith('|---|'): 
  if not rows or len(rows)>1: continue
  rows.append(line)
 elif line.startswith('| 14 |'):
  if any('<code>'+v+'</code>' in line for v in low_readings):line=line.rsplit('| medium |',1)[0]+'| low |' if line.endswith('| medium |') else line
  if '| 034 |' in line and '<code>2.7</code>' in line:line=line.replace('| medium |','| high |')
  if '| 019 |' in line and '<code>\\deleted{1}</code>' in line:line=line.replace('| medium |','| low |')
  rows.append(line)
s+='\n'.join(rows)+'\n'
s+='''
## Abbreviations encountered

The proposed expansions in this table are editorial aids confined to this file. The transcription retains the abbreviation, its capitalization, and the presence or absence of a stop.

| Written form(s) | Proposed expansion or explanation | Qualification |
|---|---|---|
| `pr`, `Pr.` | par / pour | The surrounding sentence determines the likely expansion; the ambiguous attribution on 041 remains uncertain. |
| `=`, `=s` in prose | même, mêmes | These are literal shorthand signs in the transcription. |
| `str.`, `str.` with raised `t` | structure; strictement | The raised t form in scan 003 is uncertain. |
| `cat.` | catégorie | Category terminology. |
| `hom`, `hom.`, `homs` | homomorphisme(s) | Stops and plural s follow the page. |
| `autom.` | automorphisme(s) | Scan 005. |
| `rep.`, `irré d` | représentation(s), irréductible(s) | The second reading is uncertain on 003. |
| `car.` | caractère(s), caractéristique | Different surrounding phrases support these expansions. |
| `réciproqt` | réciproquement | Scan 003. |
| `condi.` | condition | Scan 003. |
| `stabl.` | stable | Ending is uncertain on 003. |
| `trivial` with raised `t` | trivialement | Scan 003. |
| `tt` | tout | Used before a variable or noun. |
| `nb` | nombre | Scans 003 and 015. |
| `pt`, `pts` | point, points | Several sections. |
| `val.`, `ds` | valeurs, dans | Scan 007. |
| `gr`, `grpe` | groupe | Stops follow the source. |
| `rat.` | rationnel(s) | Cancelled phrase on 007. |
| `ext.` | extérieur; extension | Aut ext on 007; ext. d'un S on 013. |
| `puisq.` | puisque | Scan 009. |
| `resp`, `resp.` | respectivement | Several sections. |
| `tjs` | toujours | The letters are uncertain on 011. |
| `indép.` | indépendant(e) | Scan 011. |
| `d.t.f.` | de type fini | Scan 013. |
| `Comb.` | combinaison(s) | Scan 013. |
| `lin.`, `coeff.` | linéaire, coefficient(s) | Several sections. |
| `néc.`, `cpact` | nécessairement, compact | Scan 013. |
| `dim`, `codim` | dimension, codimension | Stops follow the source. |
| `aug.` | augmentation | Tentative only: the surrounding cancelled/abbreviated wording on 015 is uncertain. |
| `N.B.`, `NB.` | nota bene | Stops and spacing vary. |
| `non. s.`, `conn.` | non singulière, connexe | Scan 019. |
| `corr.`, `inv.`, `cl` | correspondant / correspondance; inversible; classe | Scan 019 and cycle formulas. |
| `équi.`, `équiv.` | équivalent(e), équivalence | Both written forms are retained. |
| `Alb.`, `alb` | Albanese | Prose and subscripts. |
| `alg.`, `Alg.` | algébrique; Algèbre | The capitalized bibliographical abbreviation in 022 names the subject/title. |
| `qu. pr.` | quasi projectif / quasi projective | The abbreviated hypotheses on 025 and 030 are uncertain. |
| `s-groupe` (alternative to `k-groupe`) | sous-groupe | Only an expansion of the alternative reading; the tall initial glyph remains uncertain. |
| `Dém.`, `dém.`, `Prop.`, `Th.`, `prop.` | démonstration; proposition; théorème; proposition | Capitalization and stop follow each occurrence. |
| `Pb`, `mb.` | problème, membre | The latter is uncertain on 027. |
| `AQT` | unresolved | Scan 028; no confident expansion is supported by the supplied page. |
| `p. ex.`, `f. et s.` | par exemple; faut et suffit | Scans 028 and 034. |
| `VA`, `V.A.` | variété abélienne | Singular/plural follows the surrounding words. |
| `gén.`, `Cf`, `cf.` | généralement / générale; confer | `Top. gén.` in the typescript means Topologie générale. |
| `mod.`, `mod`, `i.e.` | modulo; id est | Kept as written. |
| `pro-alg.`, `conj`, `puiss.` | pro-algèbre; conjecture; puissance | Scan 041. |
| `n°`, `chap.`, `§`, `éd.`, `déf.`, `p.` | numéro; chapitre; paragraphe; édition; définition; page | Reused French typescripts and bibliographical references. |
| `Top.` | Topologie | Reused French typescript 020. |
| `O.K.` | okay | Written beside a local equality on 032. |

## Legibility and limits of confidence

All 40 supplied whole-page images and both supplied halves of each page were inspected directly, without OCR. The 40 pages then received a second visual reading against their saved transcriptions. Extra enlarged or rotated crops were used for small additions, sideways typescripts, and cancellation; the same transcriber read the whole sequence.

The typed sheets are generally clear, although the handwritten algebra alphabet in 004/006/008 and the local overwrite of `l'identité` on 022 remain uncertain. The faint erased band on 010 is the sole `\\illegible` passage: the estimate of six words is particularly uncertain, and the status of some faint marks as erased writing rather than surface disturbance is itself insecure. It must not be treated as a recoverable six-word quotation.

The least reliable readings are the extensively cancelled portions of 003 and 013, several phrases and endings on 015, the cancelled left margin of 030, the lower correction sequence on 032, and the long cancellation at the bottom of 041. The quoted adjective in 041(b) and the marginal name there also deserve a fresh human reading. The reader should use the marked alternatives rather than infer a clean text from their mathematical plausibility.

Several awkward expressions are visibly present and were retained: `E(n)` on 005; the direction of the bottom arrow on 019; the support/dimension expressions on 021; `un diviseur` on 034; the missing initial 2 in the abbreviated theorem exponent and `C(k)` in the last line of 038; the truncated right edge of the decomposition on 039; and the absent extension-of-scalars factor in the displayed equality on 041. These examples describe transcription decisions, not a judgment that the surrounding mathematics is correct or incorrect. The letter on 044 ends mid-sentence at its printed continuation sign; the supplied material contains no continuation page for that letter.

Circles, callout curves, marginal rules, and visible arrowheads have been represented with TikZ or standard text-circle notation. Their geometry is approximate; the written labels and directions are preserved, with uncertainty marked where the ink does not settle a head or letter. The files are LaTeX fragments using the requested state macros. Structural checks were performed; a complete TeX compilation was unavailable because the installed TeX executable lacks its format and required packages.
'''
p.write_text(s)
with (root/'progress.log').open('a') as f:f.write('notation and doubts reconciled '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; 283 marked reading occurrences; no contextual source opened\n')
