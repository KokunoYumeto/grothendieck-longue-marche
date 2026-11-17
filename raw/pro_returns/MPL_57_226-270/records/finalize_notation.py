from pathlib import Path
import sys,re,difflib,collections,csv,json
sys.path.insert(0,str(Path(__file__).parent))
from workflow import BASE,now,log,combine,EXPECTED

# One representation for the visibly headless relation strokes; the alternative
# stays explicit. Each affected occurrence was inspected during the second audit.
for p in sorted((BASE/'pages').glob('*.tex')):
 old=p.read_text();new=old.replace(r'\unsure{-|\to}',r'\unsure{\text{---}|\to}')
 if new!=old:
  p.write_text(new)
  with (BASE/'records/audit_corrections.diff').open('a') as f:
   f.write(f'\n# Notation comparison, scan {p.stem[-3:]}, {now()}\n')
   f.writelines(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=p.name+' before',tofile=p.name+' after'))
  log(f'notation comparison scan {p.stem[-3:]}: headless stroke rendered consistently as text dash; arrow remains alternative {now()}')
combine()
p=BASE/'MPL_57_226-270_doubts.md'
old=p.read_text();(BASE/'records/doubts_before_final_consolidation.md').write_text(old)
body=old.split('# Doubts\n\n',1)[1]
# Make earlier table entries agree with the later, recorded visual audit.
changes={
'| 57 | 237 | deleted parenthesis in (iii) | s.c. + 2 illegible words | s.c. itself uncertain | low |':'| 57 | 237 | deleted parenthesis in (iii) | s.c. est nulle | letters recovered during the second reading; all three words remain uncertain | low |',
'| 57 | 237 | cancelled line below (iii) | en car + 3 illegible words | too much overlap to read remainder | low |':'| 57 | 237 | cancelled line below (iii) | en; 2 illegible words; car > 0 | mixed prose and formula recovered during second reading; overlap remains | low |',
'| 57 | 241 | proof source | thèse de Oort | théorie de Oort | medium |':'| 57 | 241 | proof source | théorie de Oort | thèse de Oort | medium |',
'| 57 | 249 | last paragraph, minimal prime | z | r | medium |':'| 57 | 249 | last paragraph, minimal prime | r | z | medium |',
'| 57 | 252 | last line, crossed word | forment | word body almost wholly crossed | low |':'| 57 | 252 | last line, crossed word | font | forment; word body almost wholly crossed | low |',
'| 57 | 264 | (ii) bracket | donc les comp. universelles | donne les comp. universelles; last word uncertain | low |':'| 57 | 264 | (ii) bracket | donne les comp. universelles | donc les comp. universelles; last word uncertain | low |',
'| 57 | 266 | canceled sentence opening | Il | Je | low |':'| 57 | 266 | canceled sentence opening | Je | Il | low |',
'| 57 | 266 | insertion after Donc | L_0 | L; subscript not separately clear | medium |':'| 57 | 266 | insertion after Donc | L | L_0; subscript not separately clear | medium |',
'| 57 | 266 | two canceled references | (i) | overwritten short labels | low |':'| 57 | 266 | two canceled references | a) | (i); overwritten short labels | low |',
'| 57 | 266 | last paragraph comparison word | Gaga | Gag; final a compressed | medium |':'| 57 | 266 | last paragraph comparison word | Gag | Gaga; fourth letter not separately visible | medium |',
'| 57 | 268 | diagonal marginal note | dégager un énoncé plus général / valable si A est / localisé d’un / schéma | first and final lines compressed; canceled excellent/noethérien | low |':"| 57 | 268 | diagonal marginal note | dégager un énoncé plus général / valable si A est / quotient d'un / régulier | localisé d'un / schéma; canceled excellent / noethérien remains low confidence | medium |",
}
for a,b in changes.items():
 assert a in body,a
 body=body.replace(a,b)
# Stable scan order; detail rows from the audit remain next to the original doubts.
lines=body.splitlines();head=lines[:2];rows=[x for x in lines[2:] if x.startswith('| 57 |')]
rows.sort(key=lambda x:int(x.split('|')[2].strip()))
body='\n'.join(head+rows)+'\n'
notation=r'''# Notation table

This table was maintained during transcription and reconciled against the images before the context archive was opened. The first reading in each doubt macro follows the visible strokes; it does not silently substitute the mathematically expected expression. Equivalent TeX spellings with or without braces around a single letter have the same meaning.

| Sign on page | LaTeX | Scans and comparison decision |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes | Throughout; no typographic smart quotes substituted. The irregular quotation placement at 262 is preserved under doubt. |
| Handwritten double-stroked complex and integer fields | `\mathbb C`, `\mathbb Z` | 226; 248–270. These are distinguished from typed underlined letters. |
| Typed underlined O, m, C, N, Z and ideals a, p, q, m | `\underline{O}`, `\underline m`, etc. | 227–231, 238–240. A bare typed letter is not automatically underlined. |
| Handwritten structure sheaf and maximal ideal | `\mathcal O`, `\mathfrak m` | 239–270; compared against typed O and m. |
| Formal scheme letters | `\mathfrak X`, `\mathfrak Y` | 239, 241, 245, 258. Plain Y at 245 is preserved, with its alphabet doubt in the table below. |
| Invertible sheaf / linear system | `L`, `L_0`, `L_{n_0}`, `\mathcal L` | Reused linear-systems pages and 266; the unclear insertion on 266 is `L` first, `L_0` alternative. |
| Hand-added pencil letter | `\unsure{\mathcal P\|\mathcal S}` | 263; all seven occurrences carry the same alphabet uncertainty. |
| Colored mathematical type | plain lower-case `o,r,f,z,y,p,q,m,n`, with Gothic alternatives at first doubtful occurrences | 249, 251, compared with 253. The colored type is not silently converted to Gothic; the alphabet doubt applies to repeated forms on those sheets as well. |
| Underlined Picard group object | `\underline{\operatorname{Pic}}` | 227, 233–245; plain Pic is `\operatorname{Pic}`. The underlined functor and ordinary group of classes are not conflated. |
| Component-group functor | `\underline{\pi}_0` | 233–237; distinguished from the plain homotopy `\pi_0`, `\pi_1` at 230–231. |
| Kernel, image, cokernel | `\operatorname{Ker}`, `\operatorname{Im}`, `\operatorname{Coker}` | Initial capitalization follows the writing. |
| Identity component | `G^0`, `H^0`, `H'^0` | 233–239; round zero is not a prime. |
| Completion accent on a letter | `\widehat A`, `\widehat X`, `\widehat Y` | 227–231, 256–266; a terminal completion sign on a whole expression is `^{\wedge}`. |
| Wavy accent | `\widetilde X`, `\widetilde Y` | 268–270; preserved as a tilde, not harmonized with earlier hats. |
| Čech accent | `\check{\mathrm H}` | 243–245; the downward angle is distinguished from a completion hat. |
| Typed unit-sheaf dot | `^{\bullet}` | 227–228; the canceled occurrence at 229 is bullet / asterisk under doubt. |
| Two-arm handwritten unit exponent | `^{\unsure{\wedge\|*}}` | 252, 254 and corresponding angular forms at 256. This represents the drawn shape, not an assertion that a wedge is the intended mathematical operation. |
| Clearly crossed unit exponent | `^*`; ambiguous crossed form `^{\unsure{*\|\wedge}}` | 256 diagram and additions; 258 margin. The clearly multiple-stroke stars on the reused 253 are also `*`. The two drawn forms have not been forced into one reading. |
| Direct-image symbol with / without a star | `R^if_*` / `R^if` | Especially 227, 248, 250, 254, 256. An absent or unresolved subscript is not supplied from standard notation. |
| Prime, double prime, exclamation | `'`, `''`, `!` | Primes on points, functions and indices are retained; no exclamation exponent was silently converted to a prime. Ordinary exclamation punctuation remains punctuation. |
| Headless horizontal relation | `\text{---}` or `\mathbin{\text{---}}`; `\arrow[r,dash]` in diagrams | 233, 239, 243, 250, 252, 254, 258, 260, 264, 266, 268, 270. A possible arrowhead is stated as an alternative where needed. |
| Directed or decorated arrow | `\to`, `\longrightarrow`, `\longleftarrow`, `\overset{\sim}{...}`; TikZ arrow keys | Directions and decorations checked individually; final isomorphism on 270 points left. |
| Typewriter spaces with no connective | `\quad` or ordinary math space | 227–231; no arrow or membership sign supplied in a visible blank. |
| Inclusions and inequalities | `\subset`, `\supset`, `\leq`, `\geq` | Checked separately from what the argument would require. Plain inclusion is not strengthened to an equality-bearing sign. |
| Equality shorthand in prose | `$=$` | 233 onward, including “de =”, “lui-=” and “On a de =”; not expanded to a word. |
| Schematic empty continuation or original dots | `\ldots`, dots, or the literal blank | Only where visible in the source; never used as an editorial omission. |
| Repeated or revised condition labels | literal `a)`, `b)`, `(ii)`, etc.; doubt where needed | 235 repeats b); 260 repeats 1.9; 264 and 266 have a)-like forms alongside Roman numerals. These are not renumbered. |
| On-sheet pagination | `\mspage{...}` | Original internal page numbers and the separate pencil sequence are both retained. The macro records visible pagination and does not authenticate who wrote a pencil numeral. |

# Doubts

The table gives current readings after the second visual audit. Additional rows may isolate different aspects of one passage; the chronological corrections are separately recorded in `records/audit_corrections.diff`. “High” means confidence in the literal observation, including an apparent typo or a blank, rather than confidence in a mathematical emendation.

'''
abbr=r'''
# Abbreviations encountered

These are proposed expansions for reference only. They have not been expanded in the transcription, and punctuation or case varies exactly as on the sheets.

| Written form(s) | Probable expansion / interpretation |
|---|---|
| car., car | caractéristique |
| noeth. | noethérien / noetherian, according to the language of the sentence |
| loc. | local, localement |
| alg. | algébrique |
| comm., comm | commutatif |
| gr, grs, sous-grp | groupe, groupes, sous-groupe |
| s-gpe | sous-groupe; reading uncertain on 246 |
| syst., syst | système |
| proj, proj. | projectif / projective |
| géom., géomt, géom with raised t | géométrique / géométriquement |
| pt, pts | point, points |
| mb | membre; especially “deux mb” at 256 |
| hom, hom. | homomorphisme |
| isom, isom. | isomorphisme |
| imm., imm | immersion |
| can., can | canonique |
| inv., inv | inversible |
| coh., coh | cohérent |
| schém., préschém. | schéma, préschéma |
| comp., com. | composante(s); the short reading at 236 and the bracket at 264 remain uncertain |
| irred. | irréductible(s) |
| conn., where abbreviated within fast script | connexe(s); no expansion used to resolve doubtful letters |
| rat/k | rationnel sur k |
| supp | support |
| dim | dimension |
| prof | profondeur |
| fib. | fibre(s) |
| ens | ensemble |
| ext. | extension |
| ess., ess with raised t, constt | essentiellement; constant |
| tq, tq que | tel que / telle que / tels que; doubled “tq que” kept literally |
| tt | tout |
| cad | c'est-à-dire |
| i.e., i.e | id est / c'est-à-dire |
| resp. | respectivement |
| cf, cf. | confer / compare |
| N.B., NB | nota bene |
| Th., th., th | théorème |
| Pr., Prop., prop., cor | proposition; corollaire, as appropriate |
| Dém., Dém | démonstration |
| Réf | référence |
| Sém. | séminaire |
| chap., Chap., n°, N° | chapitre; numéro |
| s.e. | suite exacte (tentative at 235, where “exacte” follows again) |
| s.c. | sans condition (possible only; canceled and uncertain at 237) |
| f. et s., faut s. | faut et suffit; the shortened phrase on 264 is not repaired |
| nec, suff | necessary, sufficient |
| M.L., ML | Mittag-Leffler |
| A.R., M.L.A.R., MLAR | Artin–Rees form of Mittag-Leffler; the letter at 227 actually says “Artin-Riesz”, which remains uncorrected |
| RR | Riemann–Roch |
| EGA, EGA III, 0_III | Éléments de géométrie algébrique; the reference is as written, without supplying a theorem number |
| Gaga, Gag | Géométrie algébrique et géométrie analytique / the comparison theorem; final word at 266 is uncertain |
| VA | Variétés abéliennes; source title abbreviated on the reused 263 |
| EVT | Espaces vectoriels topologiques; reference on the reused 261 |
| HS / ES | Unresolved abbreviated Zariski reference at 244; no expansion asserted |
| univ / an | universel / analytique are possible expansions, but the canceled annotations at 256 remain uncertain |
| Qfd, cqfd | ce qu'il fallait démontrer |
| OK., O.K. | approval / completion notation, as written |
| tél. | téléphone |

# Legibility and limits

The typescripts are generally legible, including the reused sheets; their handwritten corrections, colored type, unusual spellings and indices still require caution. The fast handwritten mathematical drafts are substantially less secure: the most doubtful areas are the upper scratch and canceled N.B. on 239, the cramped annotations on 241 and 243, both oblique marginal proofs and the canceled third diagram row on 256, the bracket and heavily canceled band on 264, and the diagonal request on 268. The full images and their supplied halves were personally inspected; enlarged and rotated crops were used for small or inverted writing, without OCR.

Four regions retain `\illegible{n}`: two canceled passages on 237 (estimated three and two words), three canceled words on 239, and two words beneath opaque hatching on 258. These are estimates of physically obscured words, not missing mathematical symbols; doubtful formulas and diagrams instead retain explicit tentative readings. Initial readings revised during audit remain traceable in the correction record, while this table and the page files give the final pre-context readings.

Diagrams, callout contours and non-diagram strokes are recreated in TikZ; their topology, labels, directions and visible cancellations are the priority, and hand-drawn curves are approximations. The transcription is a fragment using the requested macros, not a standalone typeset edition. Structural checks cover page order, braces, environment pairing, inventory completeness and allowed custom macros; a compilation attempt could not run because this environment lacks the XeLaTeX format and TikZ-CD package files, so a successful TeX build is not claimed.
'''
p.write_text(notation+body+abbr)
log(f'notation comparison completed across all 43 scans: quotation marks, alphabets, unit exponents, completions, Cech marks, primes, maps, indices, abbreviations and pagination {now()}')
print('Notation and doubts consolidated',now())
