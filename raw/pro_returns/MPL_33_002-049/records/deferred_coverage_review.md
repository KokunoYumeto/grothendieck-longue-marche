# Deferred and unfinished-source coverage review

This support review compares explicit markers in the **frozen saved LaTeX** with the research-note manifest. It does not inspect scans, change readings, or establish the authorship of reused typescripts. The original comparison was against N01–N68; the current manifest's N70–N72 now address the three candidates identified below.

## Initial candidates and their current disposition

| Frozen locus | Source wording or state | Initial coverage issue | Current disposition |
|---|---|---|---|
| 017:16; 015:4–26 | “Nous allons voir successivement … nous expliciterons”; the eleven-item catalogue; data “seront rassemblées dans les planches II à X” for nine types | N48/N50/N68 addressed related classification and verification questions, but did not index this exact exposition/plate promise. | **N70** now records the promise, partial supplied continuation, and absence of the complete plate collection. It correctly treats this as deferred exposition, not an unsolved theorem or a manuscript page-count declaration. |
| 012:41 | Bare “Suite” with “exacte” and “spectrale.....” | Within N11's broad locator, but the sequences/maps themselves were not discussed as unwritten. | **N71** now records the unfinished sequence headings and the reconstruction task. |
| 014:16 | “Dém presque immédiate par th. de changement de base......” | N13–N16 discussed purity and twists, but not this particular compressed proof indication. | **N72** now isolates its missing reduction/local model; this is a compressed proof claim, not an explicit confession of doubt. |

## Explicit markers already covered

| Frozen locus | Marker | Manifest coverage |
|---|---|---|
| 002:3–9 | Three-part cohomology/duality, adic, and L-function programme | N01 |
| 006:28 | Doubtfully read “à rédiger” in the GAGA margin | N04; conditional scope test N05 kept separate |
| 007:5 | “il restera ensuite à voir que ces possibilités sont effectivement réalisées” | N48 |
| 008:19 | “À prouver que ce sont des isomorphismes” | N06 |
| 008:21 | “Devrait aussi se généraliser au contexte rigide-analytique” | N07 |
| 008:23–31 | Conditional neighbourhood-limit application | N08 |
| 009:10 | “On ne sait si l'on définira en général la notion d'hyperalgèbre” | N59; treated as reused-source editorial uncertainty |
| 009:22 | “On pourrait donner les sorites suivants pour les noyaux formels” | N60 |
| 012:57 | “Donner [uncertain definition word] de la classe fondamentale … locale” | N12, with its later construction and remaining independence question |
| 014:18 | Boxed “Pb” concerning absolute purity | N13 |
| 014:20,24 | Announced relative purity and extension to normal-crossing divisors | N14 |
| 016:14; 018:2 | Doubtfully read “Question de la généralisation”, followed by a proposed immersion reduction | N18 |
| 019:4 | “Il restera naturellement à vérifier dans chaque cas … réduit et irréductible” | N50 |
| 019:6; 017:16 | “Nous allons voir” construction programme | N50 for casewise verification; N70 for the precise exposition promise |
| 021:6 | “On verra par contre ci-dessous” | N68 |
| 023:12 | “qu'il reste à calculer” | N52 explicitly notes that the same paragraph then supplies the calculation in outline; it is not left marked unresolved |
| 024:22 | “on prouve que cette section ne dépend pas du choix …” | N24; proposed checks in N25 remain own ideas |
| 028:25 | “Il va résulter de le théor. qu'on va [uncertain prouver]” | N29 |
| 036:31–33 | “Compatibilité avec les hom traces ....”; a more complete formulation in the derived category | N34; reconstruction proposal N35 kept separate |
| 038:30 | “dans la suite de ces notes, on explique” the flat-resolution construction | N36 |
| 047:6 | “Nous ignorons s'il en est encore ainsi … pour n quelconque” | N65, with the absent conditions b)/c) and whole-sheet cancellation distinguished |

The scans 031/049 “on vérifie que” phrases assert checks rather than explicitly defer them. Isolated ellipses, such as the unlabelled marginal dots on 004/005, do not identify a further mathematical question. The English proof ending on 043:17 (“Then, by right perfection,”) is a fragment boundary, not an explicit authorial declaration that the argument is unknown; the stronger Hom claim is already separately tested in N63. These distinctions prevent ordinary punctuation or a missing continuation from being inflated into a conjecture.

## Current result

No additional clear author-marked unknown or deferred-exposition statement was found beyond the listed candidates. This is coverage of the available frozen transcription's explicit wording, not a second visual audit and not a guarantee that every compressed claim needs or has a separate research note.

`scripts/review_notes.py` provides the separate read-only structural check of the manifest, eventual rendered notes, and per-note context-search records. Its quotation-marker warnings require reader judgment when an exact mathematical expression is presented without quotation marks; it does not change the notes or infer mathematical confidence.
