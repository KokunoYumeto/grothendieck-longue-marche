# Bounded prior-source audit: marked_in_H

**Proposal:** change only scan017 decision `017-D04b` from `true` to `false`, together with its local scope explanation. This report preserves the previous values verbatim. The committed records, page files, selected TeX, reader files and C/H count fields were left untouched.

Root has personally read the cited source and agreed with this local flag proposal. Applying a correction remains a separate root action; this audit contains no record mutation.

## Scope and source method

The declaration search was restricted to existing committed records through scan020. The reviewed cases concern deletion, diagram/frame apparatus and the local reach of H uncertainty marks. Each reviewed case below is tied to an exact local H excerpt. Searches served only to discover candidates; source wording and macro scope supply the evidence.

The record set uses both `"yes"`/`"no"` and Boolean `true`/`false`. This report preserves every stored value. For the Boolean display, the explicit mapping is `"yes" → true`, `"no" → false`, `true → true`, `false → false`; it makes no changes to record serialization.

No later packet content, image, crop, OCR, compilation, rendering, internet source, reader file or selected page TeX was used. No new ink adjudication, proof check, mathematical computation, coordinate computation or count correction was performed.

## Proposed local correction — MH-P01

| Field | Current stored value | Proposed stored value |
| --- | --- | --- |
| scan / decision | `scan017 / 017-D04b` | Same decision |
| marked_in_H | `true` | `false` |
| H_count_parent | `017-H-MARGIN-ILL` | Retained |

Record: `out/records/scan017.json`; pointer `/decisions/19`.  
Record SHA-256: `14267ac7d837730db5c89883cc14e56c2f8c108ee16b2cd13e68e259e5a9fcb1`.

### Exact previous fields, preserved as history

```json
{
  "marked_in_H": true,
  "marked_in_H_scope": "Covered source-placeholder locus; the marginal parent makes no exact positional-identity claim."
}
```

### Proposed replacement fields

```json
{
  "marked_in_H": false,
  "marked_in_H_scope": "The attached local H span writes E_j without a doubt marker. H's \\ill{} follows the set's closing brace; the local marked_in_H flag is false. The existing 017-H-MARGIN-ILL count-parent grouping is retained."
}
```

### Source and scope

**packets/017/H.tex:30–31**; characters `1152:1238` (end exclusive).

File SHA-256: `e84853244fc6ca5d0471b63ceb14c92a595d2f037646c3055a346baf6417687c`  
Excerpt SHA-256: `20c1b6d5b1b44aed1975a7944b085ae2671cb58b104d0d3433bedf1b04c7a57d`

```tex
\marginal{introduisons la partition
$\Pi_j = \{E_j, \Sigma_j^+, \Sigma_j^-\}$ \ill{}}
```

The record’s existing H attachment is preserved exactly:

```json
{
  "manifest": "packet.H.tex",
  "char_start": 1189,
  "char_end": 1228,
  "line_start": 31,
  "line_end": 31,
  "excerpt": "\\Pi_j = \\{E_j, \\Sigma_j^+, \\Sigma_j^-\\}",
  "literal_sha256_utf8": "1f384983019ae079ecbfeb5a026cf5b1d0b9b6a6b61efd41bfd96371e2d76776"
}
```

The exact H attachment for this decision ends at the set's closing brace. Its local E_j has no uncertainty macro. The source places \ill{} after that brace. The current scope text records count-parent coverage while expressly withholding an exact positional-identity claim. For the local doubt field, false is proposed. The count-parent assignment and prior wording remain preserved.

This proposal addresses the stored local H doubt flag and its explanation. The existing parent grouping, H attachment, evidence, selected reading, difference flags, C doubt status and count fields remain outside the proposed patch.

## Reviewed cases retaining their current values

| Audit | Decisions | Stored → proposed | Exact H lines | Basis |
| --- | --- | --- | --- | --- |
| MH-R01 | `003-11`, `003-15`, `003-16` | `"yes"` → `"yes"` | `packets/003/H.tex:10–12` | The local scopes carry uncertain avec or the struck ill placeholder used by the committed cancellation-group mapping. That mapping is retained without ink reassessment. |
| MH-R02 | `003-33` | `"yes"` → `"yes"` | `packets/003/H.tex:35–35` | The local cancelled source group is \struck{\ill{}}; its nested ill marker supports yes. |
| MH-R03 | `003-40`, `003-47` | `"no"` → `"no"` | `packets/003/H.tex:41–41`, `packets/003/H.tex:43–43` | The local H struck arguments carry no uncertainty or ill marker; no is retained. |
| MH-R04 | `004-80`, `004-84` | `"no"` → `"no"` | `packets/004/H.tex:11–11` | The local frame declaration reads Encadré, pour; it supplies no local doubt mark for these frame loci. |
| MH-R05 | `006-04`, `006-05` | `"yes"` → `"yes"` | `packets/006/H.tex:33–33` | The committed witness_context points both local predecessor/open-fragment decisions to H line 33, whose corresponding tail is an explicit ill placeholder. That scope is retained without mathematical evaluation. |
| MH-R06 | `011-D09`, `011-D12`, `011-D13`, `011-D14` | `"no"` → `"no"` | `packets/011/H.tex:11–12` | The note reports an overwritten letter and a struck Hom expression. Its exact local text supplies no doubt wording or uncertainty macro for these decisions. |
| MH-R07 | `011-D62`, `011-D63`, `011-D64`, `011-D65`, `011-D66` | `"no"` → `"no"` | `packets/011/H.tex:3–5`, `packets/011/H.tex:22–28` | These exact note/drawing blocks describe the respective sketches. The explicit doubtful-letter note at line 17 is recorded separately below with its existing unchanged-audit pointer. |
| MH-R08 | `012-D01` | `"yes"` → `"yes"` | `packets/012/H.tex:9–9` | H explicitly gives the local label alternatives « OK » (ou « ok »). The actual note text supports yes at this label locus. |
| MH-R09 | `012-D04`, `012-D26`, `012-D29` | `"no"` → `"no"` | `packets/012/H.tex:2–9` | H supplies direct local descriptions for these drawing/boundary loci. The OK/ok alternative in the same note attaches to the marked disks at 012-D01; its scope is retained there. |
| MH-R10 | `015-D01a`, `015-H-TITLE`, `015-D15`, `015-D19`, `015-D19-glyph`, `015-G12`, `015-G14`, `015-G-VOIS-CANCEL`, `015-G-IL-CANCEL`, `015-G-REMNANT-ANGULAR` | `"no"` → `"no"` | `packets/015/H.tex:2–2`, `packets/015/H.tex:32–33`, `packets/015/H.tex:42–43`, `packets/015/H.tex:46–46` | These exact local H arguments use plain struck commands. The quoted arguments and cancellation declarations carry no local uncertainty macro; no is retained. |
| MH-R11 | `015-H-DRAW` | `"no"` → `"no"` | `packets/015/H.tex:25–29` | The drawing block directly describes the disk, chords, labels and braces; no local doubt is attached to this parent declaration. |
| MH-R12 | `015-D16`, `015-H17`, `015-G10a`, `015-G10b`, `015-S-NOTE-SECOND`, `015-G10-GROUP` | `"yes"` → `"yes"` | `packets/015/H.tex:48–48` | The H marginal-note tail has an explicit ill placeholder. The committed tail coverage for these textual/graphic components is retained; no graphic position or count-parent assignment was reassessed. |
| MH-R13 | `016-D05` | `"yes"` → `"yes"` | `packets/016/H.tex:4–4` | The local cancelled group is struck ill; its actual ill marker supports yes. |
| MH-R14 | `016-G08`, `016-BR-PAIR` | `"no"` → `"no"` | `packets/016/H.tex:16–18`, `packets/016/H.tex:44–44` | The brace-pair note gives labels directly and the lower cancellation uses a plain struck argument. These exact local descriptions carry no doubt mark. |
| MH-R15 | `017-D01a`, `017-D05`, `017-D06a`, `017-D06b` | `false` → `false` | `packets/017/H.tex:4–4`, `packets/017/H.tex:18–19` | The local spans use plain struck wording and an add command for intersection. Their false flags are retained. |
| MH-R16 | `017-D04a` | `false` → `false` | `packets/017/H.tex:30–31` | The local partition-letter declaration is supplied directly. The trailing ill placeholder remains at the end of the marginal note. |
| MH-R17 | `017-G12`, `017-H-MARGIN-ILL` | `true` → `true` | `packets/017/H.tex:30–31` | These declarations expressly refer to the trailing ill placeholder after the closing brace; true is retained for that source-placeholder scope. |
| MH-R18 | `L018-13`, `L018-18`, `L018-25`, `L018-26`, `L018-29`, `L018-38` | `false` → `false` | `packets/018/H.tex:14–15`, `packets/018/H.tex:17–18`, `packets/018/H.tex:21–21` | The local H cancellations use plain struck arguments for la, un, choisie, est and et. Their false flags are retained. |
| MH-R19 | `L019-19`, `L019-23`, `L019-24`, `L019-25` | `true` → `true` | `packets/019/H.tex:23–23`, `packets/019/H.tex:28–29` | The local scopes carry uncertain On a, Au and dernier, or a struck ill placeholder. Those actual marks support true. |
| MH-R20 | `L019-26` | `false` → `false` | `packets/019/H.tex:30–30` | The exact text is se borner : \ill{} sur les. The colon precedes the placeholder and is supplied directly; the local colon flag remains false. |
| MH-R21 | `L019-27` | `true` → `true` | `packets/019/H.tex:30–30` | The adjoining word locus is represented by the actual ill placeholder after the colon. Its existing true flag is retained at that scope. |
| MH-R22 | `L020-09`, `L020-10`, `L020-23`, `L020-35` | `true` → `true` | `packets/020/H.tex:8–8`, `packets/020/H.tex:11–11`, `packets/020/H.tex:24–24` | The respective cancelled H groups are explicit struck ill placeholders. Existing component coverage inside those local groups is retained. |
| MH-R23 | `L020-33` | `true` → `true` | `packets/020/H.tex:23–23` | H supplies \add{\uncertain{non vide}} at this inserted phrase, supporting true. |
| MH-R24 | `L020-31`, `L020-32` | `false` → `false` | `packets/020/H.tex:21–22` | The exact note directly describes the upper label. It supplies no local question or uncertainty marker for this brace/label apparatus. |

The retained table preserves the existing committed locus-to-placeholder mappings where the local H source supplies an actual uncertainty or illegibility marker. No geometric remapping or count-parent revision was attempted. The exact excerpts and hashes follow in the evidence appendix.

## Explicit H prose doubt outside an existing marked_in_H field

`011-U01` is already present at `out/records/scan011.json/unchanged_audit/0` and has no `marked_in_H` field. H’s explicit wording is retained here for exact scope:

**packets/011/H.tex:14–17**; characters `862:1041` (end exclusive).

File SHA-256: `6b4140c82b8cb3770e5e9ce6a3fff8660a62c6b9f6d8101f71165d7340445ac6`  
Excerpt SHA-256: `d251019eadd132cac031872d4850cb560c4890ae92d3bb73590d29b724508dce`

```tex
\mathrm{Hom}(\mathcal{E},\ \underline{\mathrm{Hom}}(X,Z)) =
\mathbb{P}(\underline{\mathrm{Hom}}(X,Z))
\]
\note{la première lettre de cette ligne, lue $\mathcal{E}$, est douteuse}
```

H expressly says la première lettre de cette ligne, lue $\mathcal{E}$, est douteuse. The matching unchanged-audit entry already mentions H editorial doubt and has no marked_in_H field. This audit creates no new decision or field.

Preserve the exact source note; no field creation or record mutation proposed.

## Apparatus with no per-decision H declaration

The drawing description includes apparemment and a quoted « ? ». All committed scan010 per-decision H declarations are null. This bounded local-declaration audit establishes no new locus mapping from that description to those field values.

**packets/010/H.tex:2–12**; characters `9:807` (end exclusive).

File SHA-256: `2f41c8d9a130ac36c090ccbe94f62900cb88c165ef40a5393d425d38b81815cc`  
Excerpt SHA-256: `9e6b8aed70daa31ec674abb7565a7e8c4748576cbee74df3a2ac6fecab787bbe`

```tex
\drawing{feuillet de dessins, sans texte. Trois rangées de disques coupés par
des cordes (droites ou arcs), parfois concourantes en un point marqué, une
région parfois hachurée ; sous chaque disque ou groupe de disques réuni par
une accolade, un petit graphe : un point, deux points, un segment, trois
points, un segment et un point, un chemin à trois sommets, un triangle —
apparemment le graphe dont les sommets sont les cordes et les arêtes leurs
croisements. Plusieurs dessins sont marqués « ok » de sa main (le disque à
trois cordes concourantes au-dessus d'un segment, le disque au triangle
hachuré au-dessus du triangle, avec en variante « ou » un disque à cordes
concourantes) ; sous une rangée de disques à quatre cordes parallèles, un
« ? ». En bas à droite, des lignes brisées épaisses}
```

Exact apparatus wording preserved for scope; no metadata proposal.

## Untouched scope

All other decisions retain their existing values outside this proposal. Missing fields, not-applicable fields, unrelated lexical, mathematical, ordering and graphic decisions were not converted or re-adjudicated.

The scan011 local prose doubt remains associated with its existing unchanged-audit entry. The scan012 “OK”/“ok” alternative remains local to `012-D01`; the drawing descriptions retain their existing values. At scan019, `L019-26` retains `false` for the directly supplied colon and `L019-27` retains `true` for the following `\ill{}` placeholder.

## Supplied H apparatus definitions

These exact definitions document the source expansions used in the audit. The marked argument and the local note wording were read together with their surrounding source scope.

**source/SP40_CW_81_witnesses/hua/transcripts/preamble/grothendieck.sty:150–155**; characters `8133:8409` (end exclusive).

File SHA-256: `c304e6cbcadf931c621698d2ac00331fe734625976265ae8fe0cd400f0e5e0b9`  
Excerpt SHA-256: `5f4c916a2f21b106220c8d12cce92ad19b29678699a1f9cbb8ce4c3aba8aa882`

```tex
% Illegible: never guessed. An invented word that reads like the others is the
% worst possible outcome.
\newcommand{\ill}{\textcolor{red!60!black}{[\,\ldots\,]}}

% A doubtful reading: the word is given, and flagged as uncertain.
\newcommand{\uncertain}[1]{\uline{#1}}
```

**source/SP40_CW_81_witnesses/hua/transcripts/preamble/grothendieck.sty:175–180**; characters `9544:9877` (end exclusive).

File SHA-256: `c304e6cbcadf931c621698d2ac00331fe734625976265ae8fe0cd400f0e5e0b9`  
Excerpt SHA-256: `728646082061bea57735004f4eb2b8da422042f01b45363ee3864739198cfc99`

```tex
% Struck out by Grothendieck himself. What he crossed out is part of the
% document: a deletion often shows where the thought changed direction.
\newcommand{\struck}[1]{\sout{#1}}

% The transcriber's note, on the state of the page.
\newcommand{\note}[1]{\par\smallskip{\small\color{gray!60!black}\textit{[#1]}}\par\smallskip}
```

**source/SP40_CW_81_witnesses/hua/transcripts/preamble/grothendieck.sty:201–203**; characters `11172:11360` (end exclusive).

File SHA-256: `c304e6cbcadf931c621698d2ac00331fe734625976265ae8fe0cd400f0e5e0b9`  
Excerpt SHA-256: `380bececc1b123fae5e6ac36e846e35fbb1d18640f1047e02d6baae620035a95`

```tex
% A marginal note of Grothendieck's, distinct from the body of the text.
\newcommand{\marginal}[1]{\par\smallskip\noindent\hspace{1em}%
  {\small\color{gray!60!black}#1}\par\smallskip}
```

## Evidence appendix: retained local H excerpts

### MH-R01

Decisions: `003-11`, `003-15`, `003-16`.

**packets/003/H.tex:10–12**; characters `355:577` (end exclusive).

File SHA-256: `f5449009733bfcec6c20dad74636d65f2b4fe75030d7b3cb3efb62023f6119e4`  
Excerpt SHA-256: `ebe033bb1884039b3cbf728ca698f269dad1ac0bf32b6be99d03a4572f09866f`

```tex
$f(\infty)=\infty$ et telles que pour $z\in\mathbb{C}$ \struck{telle que}
\uncertain{avec} $f(z)\notin\{0,\infty\}$, $f'(z)=0$, on ait $f(z)=1$
\struck{\ill{}} \add{et de plus} $f''(z)\neq 0$ (i.e.\ la ramification de $f$
```

### MH-R02

Decisions: `003-33`.

**packets/003/H.tex:35–35**; characters `1499:1639` (end exclusive).

File SHA-256: `f5449009733bfcec6c20dad74636d65f2b4fe75030d7b3cb3efb62023f6119e4`  
Excerpt SHA-256: `1ccd5ba23d81e89ad839055856664fbdd997d49dbea7f17296f2a47ea74950fd`

```tex
pour $P(z), Q(z)\neq 0$, donc si cette quantité est nulle (i.e.\ $f'(z)=0$), alors $P(z)=Q(z)$ \struck{\ill{}} i.e.\ $Q(z)-P(z)=0$ implique
```

### MH-R03

Decisions: `003-40`, `003-47`.

**packets/003/H.tex:41–41**; characters `1864:1934` (end exclusive).

File SHA-256: `f5449009733bfcec6c20dad74636d65f2b4fe75030d7b3cb3efb62023f6119e4`  
Excerpt SHA-256: `dcbaf06075955e47b9e2ec765e1e9e37a80c10e2ca351edf9385e67b5414bb77`

```tex
\struck{Prenons $Q(T)=$} Prenons p.ex.\ $Q=1$, les conditions sur $P$
```

**packets/003/H.tex:43–43**; characters `2007:2071` (end exclusive).

File SHA-256: `f5449009733bfcec6c20dad74636d65f2b4fe75030d7b3cb3efb62023f6119e4`  
Excerpt SHA-256: `400781ca8a4ad7f2b85a960a61a3f0536e7882faabcecc7615d8a567bcb34cd5`

```tex
$\deg P\geq 1$, donc \struck{$P(T) =$} $P(T)=T\,P_0(T)$ où on a
```

### MH-R04

Decisions: `004-80`, `004-84`.

**packets/004/H.tex:11–11**; characters `365:399` (end exclusive).

File SHA-256: `dc0291b12631327434004fd78ff1e357f3a483ac772b9d4f74070b27f6f96e90`  
Excerpt SHA-256: `414eb8e3365a946268cae63f9bb7541501c25226e1e922a169a7029fff6f0c44`

```tex
Encadré, pour $1\leq i\leq d-2$ :
```

### MH-R05

Decisions: `006-04`, `006-05`.

**packets/006/H.tex:33–33**; characters `1143:1222` (end exclusive).

File SHA-256: `358af76acb5deefe62269a0522dee090d6c35687575ed17b402b0339fa3e4c09`  
Excerpt SHA-256: `3ae89e91b42668590d1d659753427f1d8b156e66aff7985bb6233628e4c715a2`

```tex
\Bigl(\frac{P}{Q}\Bigr)'' = \frac{P''}{Q} - 2P'\frac{Q'}{Q^2} + \ill{}, \qquad
```

### MH-R06

Decisions: `011-D09`, `011-D12`, `011-D13`, `011-D14`.

**packets/011/H.tex:11–12**; characters `723:859` (end exclusive).

File SHA-256: `6b4140c82b8cb3770e5e9ce6a3fff8660a62c6b9f6d8101f71165d7340445ac6`  
Excerpt SHA-256: `099391bb02bbd877cf1ba2a28961d0ad237c4347066e41310929c588e76c1cf3`

```tex
\note{dans le second membre, une première lettre surchargée en $Z$ ; avant
le troisième, \struck{$\underline{\mathrm{Hom}}(X)$}, biffé}
```

### MH-R07

Decisions: `011-D62`, `011-D63`, `011-D64`, `011-D65`, `011-D66`.

**packets/011/H.tex:3–5**; characters `52:577` (end exclusive).

File SHA-256: `6b4140c82b8cb3770e5e9ce6a3fff8660a62c6b9f6d8101f71165d7340445ac6`  
Excerpt SHA-256: `f5ebf17af3a8304351ef65ab84707bc763cd17ed875a1cae0b186da348ff12a4`

```tex
\note{à côté, un dessin : une droite verticale traversant un petit disque
aux rayons marqués, d'où partent des boucles en pétales}
\drawing{à droite de « $\mathbb{P}(X)$ » et de « $O\subset\mathbb{P}(X)$ », un croquis à main levée : un petit disque d'où partent des rayons (cinq traits issus de son centre, dont trois dépassent le bord), traversé par une longue droite presque verticale, épaisse au-dessus du centre ; du disque montent des boucles en pétales, et en haut une grande boucle que croisent deux traits obliques.}
```

**packets/011/H.tex:22–28**; characters `1189:2019` (end exclusive).

File SHA-256: `6b4140c82b8cb3770e5e9ce6a3fff8660a62c6b9f6d8101f71165d7340445ac6`  
Excerpt SHA-256: `9c88ec55f79fbd8e45711b2f4a54c1055a00e33bd09c28dfde8641808a7c244f`

```tex
\note{la lettre notée $\mathcal{E}$ est une grande capitale bouclée, que la
page ne définit pas. À droite, un croquis de flèches : $P\times X\times Y
\supset H$, avec $H\to P\times X$ (flèche oblique) et une flèche verticale
$P\times X\times Y\to P\times X$, puis $P\times X\to P$ ; à côté,
$U\times_V U$ et $V\leftarrow U$ au-dessus d'un $P$. En bas, un polygone et
des lignes brisées épaisses, et une ellipse traversée de courbes}
\drawing{au bas de la feuille, trois croquis à main levée : à gauche un polygone à six côtés dont deux côtés consécutifs, en bas, sont repassés d'un trait épais, avec à son angle inférieur gauche un petit cercle et un enchevêtrement de traits fins ; au milieu une ligne brisée épaisse en « V » ouvert, doublée de traits fins ; à droite une ellipse traversée de six courbes à peu près verticales.}
```

### MH-R08

Decisions: `012-D01`.

**packets/012/H.tex:9–9**; characters `514:786` (end exclusive).

File SHA-256: `4314f36bb657c89b46b29cabfd477c228ed75d701832d8012e9a4ffe43b9ff0c`  
Excerpt SHA-256: `f74aebdb542ac9d0c604dba71d150cdad66a4c03d27ee6d305b017a53a403bc5`

```tex
\note{relu sur le fac-similé : quatre disques sont marqués « OK » (ou « ok »), non trois ; seul l'axe horizontal porte une pointe. Tout le coin inférieur droit, les deux axes en équerre et ce qu'ils renferment (les courbes qui se croisent et les deux disques), est biffé}
```

### MH-R09

Decisions: `012-D04`, `012-D26`, `012-D29`.

**packets/012/H.tex:2–9**; characters `10:786` (end exclusive).

File SHA-256: `4314f36bb657c89b46b29cabfd477c228ed75d701832d8012e9a4ffe43b9ff0c`  
Excerpt SHA-256: `e40973dc8969b9d39f2625101cb9136237446a421bdd9391eca246ea2f30821f`

```tex
\drawing{feuillet de dessins de la même famille que la page 9 : disques coupés
de cordes, une région triangulaire ou quadrangulaire hachurée, trois marqués
« OK », des variantes introduites par « ou » ; sous eux les graphes : un
triangle, un point, un tripode épais en « Y », un carré, un triangle
surmonté d'un segment, un rectangle coupé d'une diagonale, un triangle à
point intérieur. À droite, deux axes fléchés en équerre et, dans l'angle,
des courbes qui se croisent et deux disques coupés d'arcs}
\note{relu sur le fac-similé : quatre disques sont marqués « OK » (ou « ok »), non trois ; seul l'axe horizontal porte une pointe. Tout le coin inférieur droit, les deux axes en équerre et ce qu'ils renferment (les courbes qui se croisent et les deux disques), est biffé}
```

### MH-R10

Decisions: `015-D01a`, `015-H-TITLE`, `015-D15`, `015-D19`, `015-D19-glyph`, `015-G12`, `015-G14`, `015-G-VOIS-CANCEL`, `015-G-IL-CANCEL`, `015-G-REMNANT-ANGULAR`.

**packets/015/H.tex:2–2**; characters `10:38` (end exclusive).

File SHA-256: `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546`  
Excerpt SHA-256: `6ee958054557599d7abaa8e6aa9cffec1830a192f24f63e6ba98aa855fa92e08`

```tex
\struck{V} \emph{Version I}
```

**packets/015/H.tex:32–33**; characters `1620:1768` (end exclusive).

File SHA-256: `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546`  
Excerpt SHA-256: `e248f50ac52aeaa173aaa6217ede6d9dc3679b7b9d834ed615aff2137e04f1dd`

```tex
  \struck{résulte de} \struck{$\Sigma_1^-\supset\Sigma_2^+$} équivaut à :
  \struck{$\Sigma_2^-\supset\Sigma_1^+$} $\Sigma_1^+\subset\Sigma_2^-\cup
```

**packets/015/H.tex:42–43**; characters `2015:2158` (end exclusive).

File SHA-256: `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546`  
Excerpt SHA-256: `80ff38165a87af9995c11ebe84a322b7c2173a5a93befdaa2a4a21de382f2e39`

```tex
Comme $\Sigma_2^-\supset E_1$, \struck{vois.\ ouvert} i.e.\ $\Sigma_2^-$ est
un \emph{vois.}\ ouvert de $E_1$, \struck{il contient les} on a :
```

**packets/015/H.tex:46–46**; characters `2268:2345` (end exclusive).

File SHA-256: `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546`  
Excerpt SHA-256: `884bddd2e8181d19f6333123289cb81a4ba04961af7f0b94b098757cd7582802`

```tex
\add{ouvert,} serait fermé dans $X$, donc \struck{$\Sigma_1^+\neq\emptyset$}
```

### MH-R11

Decisions: `015-H-DRAW`.

**packets/015/H.tex:25–29**; characters `1195:1547` (end exclusive).

File SHA-256: `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546`  
Excerpt SHA-256: `dfde3eaf587dc0936b4dfaee3f12622c0f1ca9b3de249f2c4db98ed40628c724`

```tex
\drawing{à gauche, un dessin : un disque coupé de deux cordes horizontales
$E_1$ (en haut) et $E_2$ (en bas) ; au-dessus de $E_1$, la calotte
$\Sigma_1^+$, et une accolade à droite réunit tout ce qui est sous $E_1$ :
$\Sigma_1^-$ ; sous $E_2$, la calotte $\Sigma_2^+$, et une accolade à gauche
réunit tout ce qui est au-dessus de $E_2$ : $\Sigma_2^-$}
```

### MH-R12

Decisions: `015-D16`, `015-H17`, `015-G10a`, `015-G10b`, `015-S-NOTE-SECOND`, `015-G10-GROUP`.

**packets/015/H.tex:48–48**; characters `2369:2432` (end exclusive).

File SHA-256: `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546`  
Excerpt SHA-256: `5aa5453bb67a24774812fe8ebb732f48bb0d99b046f4f4a77e70646de94b46e3`

```tex
\marginal{$\overline{\Sigma_1^+}\cap E_1\neq\emptyset$ \ill{}}
```

### MH-R13

Decisions: `016-D05`.

**packets/016/H.tex:4–4**; characters `154:228` (end exclusive).

File SHA-256: `a22952dab19274cb174e8057c9e3ab2c355ce9058d343b2a4c8e860fbd90253f`  
Excerpt SHA-256: `e3490b57c949f5e6e7030e98f217b4d6a425dae32aa513db6b3d7e1d66a1ce6f`

```tex
\add{de $X\setminus E_2$}, donc \struck{\ill{}} égal à $\Sigma_2^-$, donc
```

### MH-R14

Decisions: `016-G08`, `016-BR-PAIR`.

**packets/016/H.tex:16–18**; characters `481:661` (end exclusive).

File SHA-256: `a22952dab19274cb174e8057c9e3ab2c355ce9058d343b2a4c8e860fbd90253f`  
Excerpt SHA-256: `5aaa5163104438dc8b696fd4c5dc6ab53cf378fd64d57815cd07a147d66131bf`

```tex
\note{une accolade au-dessus de $\Sigma_1^+\sqcup E_1\sqcup\Sigma_{12}$ porte
$\Sigma_2^-$, une accolade au-dessous de $\Sigma_{12}\sqcup E_2\sqcup
\Sigma_2^+$ porte $\Sigma_1^-$}
```

**packets/016/H.tex:44–44**; characters `1368:1442` (end exclusive).

File SHA-256: `a22952dab19274cb174e8057c9e3ab2c355ce9058d343b2a4c8e860fbd90253f`  
Excerpt SHA-256: `2b1d72abe2e355152dcbefb96918e702b97dc03787a2f1db6f2adf5b9d7b6add`

```tex
\struck{alors $\Sigma_{12}\sqcup E_2\sqcup\Sigma_2$} \add{en considérant}
```

### MH-R15

Decisions: `017-D01a`, `017-D05`, `017-D06a`, `017-D06b`.

**packets/017/H.tex:4–4**; characters `35:112` (end exclusive).

File SHA-256: `e84853244fc6ca5d0471b63ceb14c92a595d2f037646c3055a346baf6417687c`  
Excerpt SHA-256: `f8bb55fa402c144aee4ad770d636548493cfc3950f39d603cf0bd20e1b292b95`

```tex
Supposons que $\forall i\in I$, \struck{$E_i$ soit rare dans $X$} on ait (où
```

**packets/017/H.tex:18–19**; characters `531:672` (end exclusive).

File SHA-256: `e84853244fc6ca5d0471b63ceb14c92a595d2f037646c3055a346baf6417687c`  
Excerpt SHA-256: `ee776e10c07cce0ecb4adb33d3815f7b289b0a4f80878a96e1a870f046cb4777`

```tex
la partition \add{$\Pi_J$} de $X$ \struck{définie} définie par les $E_j$
($j\in J$), \struck{intersection} \add{intersection} des partitions
```

### MH-R16

Decisions: `017-D04a`.

**packets/017/H.tex:30–31**; characters `1152:1238` (end exclusive).

File SHA-256: `e84853244fc6ca5d0471b63ceb14c92a595d2f037646c3055a346baf6417687c`  
Excerpt SHA-256: `20c1b6d5b1b44aed1975a7944b085ae2671cb58b104d0d3433bedf1b04c7a57d`

```tex
\marginal{introduisons la partition
$\Pi_j = \{E_j, \Sigma_j^+, \Sigma_j^-\}$ \ill{}}
```

### MH-R17

Decisions: `017-G12`, `017-H-MARGIN-ILL`.

**packets/017/H.tex:30–31**; characters `1152:1238` (end exclusive).

File SHA-256: `e84853244fc6ca5d0471b63ceb14c92a595d2f037646c3055a346baf6417687c`  
Excerpt SHA-256: `20c1b6d5b1b44aed1975a7944b085ae2671cb58b104d0d3433bedf1b04c7a57d`

```tex
\marginal{introduisons la partition
$\Pi_j = \{E_j, \Sigma_j^+, \Sigma_j^-\}$ \ill{}}
```

### MH-R18

Decisions: `L018-13`, `L018-18`, `L018-25`, `L018-26`, `L018-29`, `L018-38`.

**packets/018/H.tex:14–15**; characters `532:681` (end exclusive).

File SHA-256: `84e217399be12cf590899be9ef901b4ef5f0937cc163db6ca00e98cd4b13487d`  
Excerpt SHA-256: `260bd9d8eb555da34f8fb725be6ebb1187e6d3b751cb563da20bce0ccf7a155f`

```tex
C'est presque une tautologie : Dire \add{qu'une} \struck{la} classe donnée
\add{$U_\alpha$ de $\Pi_J^0$} \struck{un} ne contient pas $E_i$ i.e.\ est
```

**packets/018/H.tex:17–18**; characters `742:895` (end exclusive).

File SHA-256: `84e217399be12cf590899be9ef901b4ef5f0937cc163db6ca00e98cd4b13487d`  
Excerpt SHA-256: `23e91406c3f64f7ab09cdf18300cacd94735f5555ba43126aef6c68de9e07983`

```tex
$\Sigma_j^+\in\pi_0(X\setminus E_j)$ \struck{choisie} “composante” de cette
classe \struck{est} soit l'élément de $\pi_0$ qui ne contient pas $E_i$ ; il
```

**packets/018/H.tex:21–21**; characters `1016:1065` (end exclusive).

File SHA-256: `84e217399be12cf590899be9ef901b4ef5f0937cc163db6ca00e98cd4b13487d`  
Excerpt SHA-256: `8c5bdfb5f26d40b9b616c478b629c9e49ae1230a8df614a9707634457051f7af`

```tex
$\operatorname{card}I=2$, \struck{et} à fortiori
```

### MH-R19

Decisions: `L019-19`, `L019-23`, `L019-24`, `L019-25`.

**packets/019/H.tex:23–23**; characters `710:744` (end exclusive).

File SHA-256: `f4eec6deb1c5d6bda0620c121f5c125c6e228212cb989e192303edd23ead408c`  
Excerpt SHA-256: `6c382abd31e1b87ce9b4a1702df3ceb76fcdc0ed13b6b4c3397b6118e306b232`

```tex
\struck{On} \uncertain{On a} donc
```

**packets/019/H.tex:28–29**; characters `876:1014` (end exclusive).

File SHA-256: `f4eec6deb1c5d6bda0620c121f5c125c6e228212cb989e192303edd23ead408c`  
Excerpt SHA-256: `ac011c46039f3a6ecb3e1662e634d5e17f38710d4582cbb47d5cf01f8310076f`

```tex
\struck{Soit} \uncertain{Au} \uncertain{dernier} $=$, dans la
\struck{\ill{}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$,
```

### MH-R20

Decisions: `L019-26`.

**packets/019/H.tex:30–30**; characters `1014:1072` (end exclusive).

File SHA-256: `f4eec6deb1c5d6bda0620c121f5c125c6e228212cb989e192303edd23ead408c`  
Excerpt SHA-256: `7d22682fc02cb47ac489ef6059aae8c1375980b9f8ce6409ec65685c7b2cd655`

```tex
il suffit de se borner : \ill{} sur les \struck{$\Sigma$}
```

### MH-R21

Decisions: `L019-27`.

**packets/019/H.tex:30–30**; characters `1014:1072` (end exclusive).

File SHA-256: `f4eec6deb1c5d6bda0620c121f5c125c6e228212cb989e192303edd23ead408c`  
Excerpt SHA-256: `7d22682fc02cb47ac489ef6059aae8c1375980b9f8ce6409ec65685c7b2cd655`

```tex
il suffit de se borner : \ill{} sur les \struck{$\Sigma$}
```

### MH-R22

Decisions: `L020-09`, `L020-10`, `L020-23`, `L020-35`.

**packets/020/H.tex:8–8**; characters `252:307` (end exclusive).

File SHA-256: `d67166fdd096bc3a2341b67f2df20595b4b02c954dfe922c490cb57734fa0687`  
Excerpt SHA-256: `d1bd578b65a90890b5d6dee22035a59e36e3bf6cbf6dcbbe526dc198b78a8f0c`

```tex
\struck{\ill{}} $U_{J,i}$ est un voisinage de $E_i$ et
```

**packets/020/H.tex:11–11**; characters `426:454` (end exclusive).

File SHA-256: `d67166fdd096bc3a2341b67f2df20595b4b02c954dfe922c490cb57734fa0687`  
Excerpt SHA-256: `50294abdd00def4f00bdeb2ce60096a059cb0fd8f8b6ef3d518bcdbd8c7b97bb`

```tex
classes est \struck{\ill{}}
```

**packets/020/H.tex:24–24**; characters `976:1014` (end exclusive).

File SHA-256: `d67166fdd096bc3a2341b67f2df20595b4b02c954dfe922c490cb57734fa0687`  
Excerpt SHA-256: `a25b3edb37baf57ee73dc6089e07baf1b1b45aa1a6dffbad19c851b464627660`

```tex
$\forall\alpha\in K$, \struck{\ill{}}
```

### MH-R23

Decisions: `L020-33`.

**packets/020/H.tex:23–23**; characters `916:976` (end exclusive).

File SHA-256: `d67166fdd096bc3a2341b67f2df20595b4b02c954dfe922c490cb57734fa0687`  
Excerpt SHA-256: `f68d16542c305bcc86d8d1cc9ca5e892e89c9208c5f7713a1610e7563456d011`

```tex
où $K$ est une partie \add{\uncertain{non vide}} de $I$, et
```

### MH-R24

Decisions: `L020-31`, `L020-32`.

**packets/020/H.tex:21–22**; characters `827:916` (end exclusive).

File SHA-256: `d67166fdd096bc3a2341b67f2df20595b4b02c954dfe922c490cb57734fa0687`  
Excerpt SHA-256: `59b48d083907ae0580ba46f18b16dba4444e293de5197443d627a05c94535d7c`

```tex
\note{au-dessus de $\Sigma_\alpha^+\cup E_\alpha$, il écrit
$\widehat{\Sigma}_\alpha^+$}
```

## Provenance and integrity

The JSON companion preserves exact decision pointers, stored field values, record hashes, excerpt hashes and packet metadata. Packet metadata names the original H source file; this audit uses the supplied per-scan `H.tex` extraction and does not open the full batch transcript.

All source fingerprints below were rechecked at the end of extraction. Source files retained the same bytes during extraction.

| Input | SHA-256 |
| --- | --- |
| `out/records/scan002.json` | `2e74e8552a88ac431781de79d25aed10b79042c0060b5bfb828983e1c62a6090` |
| `out/records/scan003.json` | `e43d07f93ef52257c6847aad0b587452e9a6dafd2e99674347d8e5cdbd1958b4` |
| `out/records/scan004.json` | `c87f5e0d193546ad4d741f728b203332356f75ec1298ed5907c60de7b0a2af60` |
| `out/records/scan005.json` | `9d281343f19e111e7e9bc20c65364ef10a9056701573da4dcbb12fb3c78e2ac3` |
| `out/records/scan006.json` | `e6e2765140f0f6401ea6fe97e4bd72cc7e2154515c89caa75a88287f963998a1` |
| `out/records/scan007.json` | `288ee0d1630a9d3394a3a60401dbe7500baf5e4140f7aae5143b81b6e0b9a7a6` |
| `out/records/scan008.json` | `4acbce58e47cfd644964e0d31b242a58693270c15721b07005fa51bb5f4c858f` |
| `out/records/scan010.json` | `6771151bcc08fba043b685c7cee2ebf96649a144e4d04224d01920c903fd6cd7` |
| `out/records/scan011.json` | `7e7ff055ccd845b940b56982321aa52cf729e65be403a9667ec760268e8c3fab` |
| `out/records/scan012.json` | `e3be43673fcf88fc07d1bd91f2c318435fee83886a516178494253c091135f0f` |
| `out/records/scan013.json` | `a67817cd2be56e78809da14b657488434f1e8c0a9bbef562cd4d41a6d1671036` |
| `out/records/scan014.json` | `9f4ee210e791ff218f84e5ab08c4a6f264ebbdfbe042d52dfb97ffa3235cfc61` |
| `out/records/scan015.json` | `a609c226bb92b7efd75529f16cd944f72c075532665123eee6aa92025e4567d6` |
| `out/records/scan016.json` | `538d97ecc9b18921d356abb3ea4e368a558f43be9fb52910e6d2799dbe8dd647` |
| `out/records/scan017.json` | `14267ac7d837730db5c89883cc14e56c2f8c108ee16b2cd13e68e259e5a9fcb1` |
| `out/records/scan018.json` | `42a52aebd1f3157cf16540f01407289091564676f9e7b792c33e93a06dd118c4` |
| `out/records/scan019.json` | `ce6d53c8af00e27b2ea2bbfef3fb0b4bdfc26ad9abe67fde64f22dfa913ab618` |
| `out/records/scan020.json` | `a5b7bf0e6a5c4bdf7b2b86c42b3f36520bc90718db1a99d0ce3b1f5acafd2cce` |
| `packets/017/H.tex` | `e84853244fc6ca5d0471b63ceb14c92a595d2f037646c3055a346baf6417687c` |
| `packets/003/H.tex` | `f5449009733bfcec6c20dad74636d65f2b4fe75030d7b3cb3efb62023f6119e4` |
| `packets/004/H.tex` | `dc0291b12631327434004fd78ff1e357f3a483ac772b9d4f74070b27f6f96e90` |
| `packets/006/H.tex` | `358af76acb5deefe62269a0522dee090d6c35687575ed17b402b0339fa3e4c09` |
| `packets/011/H.tex` | `6b4140c82b8cb3770e5e9ce6a3fff8660a62c6b9f6d8101f71165d7340445ac6` |
| `packets/012/H.tex` | `4314f36bb657c89b46b29cabfd477c228ed75d701832d8012e9a4ffe43b9ff0c` |
| `packets/015/H.tex` | `f1af2e2e55b6d04dff9e5d98d0a87742fc562ccd1a68ef9e9e86a738e9d59546` |
| `packets/016/H.tex` | `a22952dab19274cb174e8057c9e3ab2c355ce9058d343b2a4c8e860fbd90253f` |
| `packets/018/H.tex` | `84e217399be12cf590899be9ef901b4ef5f0937cc163db6ca00e98cd4b13487d` |
| `packets/019/H.tex` | `f4eec6deb1c5d6bda0620c121f5c125c6e228212cb989e192303edd23ead408c` |
| `packets/020/H.tex` | `d67166fdd096bc3a2341b67f2df20595b4b02c954dfe922c490cb57734fa0687` |
| `packets/010/H.tex` | `2f41c8d9a130ac36c090ccbe94f62900cb88c165ef40a5393d425d38b81815cc` |
| `packets/003/metadata.json` | `325f3684eeca1200a457fc16b6aa68f515877004e318a14e80476347e887637c` |
| `packets/004/metadata.json` | `d3f2de73b58a721155e2848ee0ea61f60ac53ac544c6ee66856b062edfaacaa4` |
| `packets/006/metadata.json` | `d6fe2a8eb766d751c4e28ecc42091c667260fc169c29423c31cf4382d84279e6` |
| `packets/010/metadata.json` | `01fcb1b3f0fd7c9b6eff14ca7b078d2f15b41679f22eef404ff17bce09b52da3` |
| `packets/011/metadata.json` | `e272a6020afba7242e71b1b1cb100bb07149563dee66dd93cf31fec8c1904469` |
| `packets/012/metadata.json` | `03220d7014fd1d34b09bd3c4fbd9bcefd9e54d9ab1a34c901f263dd2d8d73be8` |
| `packets/015/metadata.json` | `535118d287652702e1758bee8c6fb802cc8d70de2dc5813d5b20f20f69dcb882` |
| `packets/016/metadata.json` | `b4553b7b42ee041813fae2dafdcd005a9996978e59ce0fc10505883be032f978` |
| `packets/017/metadata.json` | `6c3918282d28ae0fc83af3855b91cdf9e16945a82f7440217c7a6dc497b085e3` |
| `packets/018/metadata.json` | `894a9d6bdc7cf98377271373cf347b328b3bfbcefd079283a15720f55d5b5423` |
| `packets/019/metadata.json` | `75620ce0539cbc4252487b8615d64ade2ce0a86622053b3f9b5762fe36fe4717` |
| `packets/020/metadata.json` | `2c41896da2e5132499dea2f53ef9a3424cc38cff6b317bb510a8a938dc4c4208` |
| `source/SP40_CW_81_witnesses/hua/transcripts/preamble/grothendieck.sty` | `c304e6cbcadf931c621698d2ac00331fe734625976265ae8fe0cd400f0e5e0b9` |

JSON companion SHA-256: `16c7fa5d1c3a74ca90c23b4e4171e599b22639189d41e247d191324a8f42b7be`.

Read-only extractor: `out/checks/extract_marked_H_prior_source_audit.py`; SHA-256 `f14d5156acad2b603e5fe876e1eeca2f509544dd13a09864f1e59742669eb92b`. It writes only JSON to stdout; the script itself performs no file mutation.

Source line ranges are one-based and inclusive. Character offsets are zero-based Unicode code-point offsets in the exact UTF-8-decoded source, with an exclusive end. File hashes use original bytes; excerpt hashes use the exact quoted UTF-8 bytes. The JSON preserves original line endings; Markdown fences present the same text for review.
