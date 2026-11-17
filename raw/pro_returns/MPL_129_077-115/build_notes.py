"""Build the post-freeze research notes and a per-item context-search record."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,subprocess,re
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from notes_data import NOTES,H
CTX=ROOT.parent/'context'
FILES=[CTX/'README.md',CTX/'notes/RESULTS_STATE.md',CTX/'hua_project/README.md',CTX/'hua_project/129.modern.tex']
def clean(t): return t.replace('\\\\','\\')
search=[]
for n in NOTES:
    args=['rg','-n','-i','-F']
    for term in n['terms']:args+=['-e',term]
    args += [str(p) for p in FILES]
    result=subprocess.run(args,text=True,capture_output=True)
    assert result.returncode in (0,1),(n['id'],result.stderr)
    hits={}
    for line in result.stdout.splitlines():
        m=re.match(r'(.+?):(\d+):',line)
        if m:
            f=str(Path(m[1]).relative_to(CTX)); hits.setdefault(f,[]).append(int(m[2]))
    search.append(dict(id=n['id'],terms=n['terms'],matches={f:sorted(set(ns)) for f,ns in hits.items()},searched_files=[str(p.relative_to(CTX)) for p in FILES]))
(ROOT/'context_searches.json').write_text(json.dumps(search,ensure_ascii=False,indent=2)+'\n')
header=r'''# Research notes — MPL_129_077-115

## Scope, evidence and status

These notes concern **cote129, scans077–115, excluding079 and089:37 supplied scans**. The transcription was read visually in one stream, audited against every supplied page and frozen before the context was opened; its final freeze is **2026-11-17 18:30:25 UTC**, with context opening at **18:30:35 UTC**. No reading below is fed back into the frozen TeX.

A manuscript assertion is not automatically a proved theorem. The supplied `notes/RESULTS_STATE.md` was read in full, including its status cautions; its run statuses are claims unless a particular review is stated. Its three directly relevant findings belong to **Michel Hua’s project**, not to this return. His complete `hua_project/129.modern.tex` was read after freezing, together with both READMEs; it explicitly describes itself as an AI-produced modernization and identifies mathematical repairs and unverified literature citations. Every item below gives its own source scans, a brief source phrase, a kind and a contextual comparison; **own ideas carry confidence and a reason**.

In the item metadata, **“Hua” always means “Hua, modernised reading of cote129”, `hua_project/129.modern.tex`, at the named subsection**. The scan numbers following that citation are the corresponding scans in this package, not Hua’s page numbers. His page76 matches our077, his page81 our082, and his final page114 our115; N96 records a concrete locator problem in the context. No pages of another cote, nor the unprovided earlier scans of129, have been inspected for this return.

Each item was searched separately in all four supplied context files using its objects, words or notation. `context_searches.json` records the search terms and every matching line number without repackaging the supplied source files. A no-direct-ID entry means the context supplies no result on that precise issue; it does not mean that the issue is new to the literature.

### What this selection changes in the contextual picture

| Planning/context question | Answer from the scans | Detailed items |
|---|---|---|
| Is this the BT/crystalline line? | Yes: the corrected course plan, deformation outline, co-Lie calculations and Nice programme give direct evidence. Six reused typed pages concern unrelated analysis;112 has no author text. | N01–N02, N69–N76, N77–N92 |
| Is the arbitrary-f, one-index Tate assertion written and argued? | Yes:098 states the general setting and100 works through the difficult direction. Degree bounds and n=1 need qualification. | N47–N57 |
| What is added to the co-Lie/truncated-BT finding? | Exact source hypotheses, stabilization and zero maps, unfilled deformation formulas, uncertain indices, and the separation between assertions and proofs. | N28–N46 |
| Is the odd-p Ext² claim still a “no reference found” lead? | There is a primary-source match for the additive-coefficient odd-p statement; the full arbitrary-quasi-coherent formulation still needs a scope check. | N43–N46; [I85], [B75] |
| Does the selection settle ANABELIAN_SUCCESSOR A.57? | No. Hasse-zero degeneration and BT deformation data suggest local diagnostics, but no universal supersingular correspondence is constructed. | N11–N12, N77 |
| Can the four names in the archive title be assigned to individual sheets? | No secure assignment follows from this selection. The English pencil note also has no identified writer here. | N02, N62 |
| Are there changes to the GT/tower/homotopy register statuses? | No. The matched GT and homotopy entries are not addressed by these scans; similarity of words such as “groupe”, “filtration” or “strates” is not a mathematical bridge. | Status map below |

### Register status map

| Entry | Supplied status | What this return contributes |
|---|---|---|
| Hua, findings register, **129-tate-object-one-index** | Literature match claimed for f=p; intake says new to us; no referee verdict supplied | Confirms the arbitrary-f source and actual proof sketch; identifies endpoint, truncation and locator qualifications. |
| Hua, findings register, **129-colie-truncated-bt-package** | Literature match claimed; intake says new to us; no referee verdict supplied | Source-level distinctions and a checked published statement locator for the Ext comparison. |
| Hua, findings register, **129-ext2-vanishing-p-odd** | Candidate/no-reference claim; intake says new to us | Partial literature match, careful sheaf/global distinction, and a remaining coefficient-generalization question. |
| **ANABELIAN_SUCCESSOR A.57** | Open, return’s claim; only a truncated statement is supplied | An indirect local lead; no proof, counterexample or status change. |
| **WG2 §2.4 #5** | Unchecked planning question | A possible divided-power comparison datum; the other cotes are not supplied. |
| **LM4 C.12, LM7_PUSH E.3, EXIT_TOWER E.24/E.45/E.T3**, and the other tower/homotopy rows | Preserve their individual supplied statuses and review qualifications | No direct bearing found in this selection; none is silently marked settled or re-derived. |

## Item-by-item notes
'''
lines=[header]
for n in NOTES:
    lines += [f"### {n['id']}. {n['title']}",'',f"**Source:** 129.pdf / cote129, scan(s) {n['scans']}. **Kind:** {n['kind']}.",'',f"**Source phrase:** {clean(n['quote'])}",'',clean(n['body']),'']
    ctx=[]
    for key in n['keys']:
        title,scans=H[key];ctx.append(f'Hua, §“{title}” (corresponding scans {scans})')
    lines += ['**Context:** '+'; '.join(ctx)+'.', '**RESULTS_STATE:** '+(n['register'] or 'No directly matching programme result ID was identified in the supplied register')+'.']
    if n['confidence']:lines.append('**Own-idea confidence:** '+n['confidence']+'; reason given in the item.')
    lines.append('')
lines += [r'''## Standing question 1 — steps the manuscript itself marks as unverified

This is an index to the separate items above. It distinguishes an explicit doubt, an admitted input, an expectation and a request to add exposition; an omitted proof without such a signal is not automatically an authorial doubt.

| Cote / scan | His words or visible signal | Status on the sheet | Item |
|---|---|---|---|
|129 /078|“programme préliminaire”; inserted “et problèmes”|Programme explicitly left open|N01|
|129 /082|“préciser ce que ça veut dire … Frob. et Versch. itérés”|Definition/explanation to complete|N06|
|129 /084|“Il devrait être vrai”; “le noyau devrait être fini localement libre”|Explicit expectation|N09|
|129 /084 margin|“La condition suppl. à rajouter devrait être … hauteur localement constante”|Proposed additional hypothesis|N11|
|129 /084–085|“prouvera par la suite”|Proof postponed|N13|
|129 /085|“sans doute équivalentes”|Equivalence qualified|N10|
|129 /086|“qui figure dans EGA IV ?”|Bibliographic uncertainty; not itself a proof|N18|
|129 /090|“Cf. prop.14 des Notes I”; “Cf. prop.1 des Notes I”|Explicit dependence on an absent text|N21|
|129 /090 margin|“donner relation d+d^(t or *)=h”|Result/exposition to add; dual exponent uncertain|N24|
|129 /091|“je ne sais pas procéder directement !”|Direct method explicitly unavailable|N28|
|129 /092|“Définition admise”|Admitted construction; “admise” medium-confidence|N29|
|129 /093 margin|Possible “à vérifier !”|**Low-confidence reading**, not a securely established authorial phrase|N34|
|129 /094|“on aura”; “en fait on aura”; “devrait exister sur toute base”|Conditional dictionary and all-base expectation|N35|
|129 /094 triangle|“?” on a specific arrow|Connecting morphism/degree queried|N36|
|129 /107 pencil|“? Proof of 1st conj.”|Tentative proof; abbreviation and writer uncertain|N62|
|129 /107 ink|“⇒ ?”|A particular inductive implication questioned|N61|
|129 /108|b*) and a*) followed by ellipses|Unfinished dual conditions; ellipses are actual ink|N63|
|129 /113|Ellipses among PD axioms; revised site heading|Outline incomplete; not a claim of falsity|N79–N81|
|129 /114|“Il se pourrait … soit pl. fidèle”|Explicit full-faithfulness conjecture|N84|
|129 /114|“j’ai une idée … l’image essentielle”|Expected characterization, not supplied|N85|

The affirmative “est pleinement fidèle” on115 is deliberately **not** included as the same self-flag as114: it is an unproved assertion, with an incomplete target category, but it is written affirmatively (N90).

### Withdrawals and revisions with both relevant locations

| Original or rejected wording | Replacement or later contrast | Interpretation |
|---|---|---|
|085 recalls the earlier field-only restriction|085 correction, developed on086|Explicit broadening to a one-point base (N16); the earlier field-only page is not independently available beyond082’s perfect-field setting.|
|088 kernel-of-epimorphism claim and two-out-of-three sentence, both deleted|088 retained extension/cokernel claims; compare110 negative smoothness implication|Same-page withdrawal plus a related later-in-scan-order caution, not a claimed chronology (N19–N20,N67).|
|095 O-index in the homomorphism-lifting Ext terms|095 Z inserted; later terms still O-indexed|Partial correction on the same sheet (N38).|
|113 deleted site heading and doubtful naturel/relatif wording|113 inserted “(absolu)”|Same-page revision of the heading (N81).|
|114 deleted Frobenius-lift clause|114 connection description survives|Removal of an auxiliary choice, not proof of the completed comparison (N83).|
|115 deleted “de valuation discrète”|115 inserted complete local hypothesis with doubtful “noeth” qualifier|Same-page broadening that differs from Hua’s final example (N91).|

## Standing question 2 — title sheets, headings and page counts

**No explicit total such as “19 pages” or “Pages1–67” is written on the supplied title sheets.** No secure authorial handwritten page number was found that warranted `\mspage`. Archive foliation is recorded only in TeX comments; the printed reused-page numbers below are neither authorial foliation of the BT notes nor totals for this package.

| Cote / scan | Title or heading as read | Count/pagination evidence |
|---|---|---|
|129 /077|I, II; “Vecteurs de Witt et [théorie?] de Dieudonné”|Cover; no page count; archive76|
|129 /078|Corrected six-part course plan, ending in F-crystals and specialization|Contents sheet; Roman numerals are section numbers, not a page count; archive77|
|129 /080|“Rappels sur la théorie de Dieudonné (sur corps parfait k)”, with I etII|Own-text typescript heading; no count; archive79|
|129 /083|III “Propriétés Générales des B.T.”|Cover; no count; archive84|
|129 /084|“Exemples de groupes de BT.”|Section heading; no count|
|129 /090|“2. Sur certains schémas en groupes finis loc. libres en car. p.”; inserted applications to BT|Section2 and proposition numbers are not pagination|
|129 /091|“4. Déformations de groupes de BT : énoncés”; “5. Rapport sur le complexe cotangent relatif”|Section numbers only|
|129 /092|“Complexe cotangent relatif”, circledA|Report section; no count|
|129 /093–095|CircledB; Dieudonné link; circledC deformation applications; circledD truncated BT|Internal organization; no page totals|
|129 /097|“Sotties” or “Sottises” sur Groupes p-divisibles, et groupes de B.T. (N97)|Cover; first word low-confidence; Hua reads “Sorites”, retained as a contextual alternative rather than an emendation; no count; archive98|
|129 /098,108|“Conditions équivalentes”|Working-section headings, not independent counted texts|
|129 /113|Boxed “Conférence à Nice”; “Groupes de Barsotti–Tate”; boxed p fixé|Three supplied lecture-outline leaves113–115; **three is a supplied-leaf count**, not a manuscript total|
|129 /114–115|4), thenI–V programme; “Cas d’un anneau …”|Internal numbering and a revised example, not pagination|
|129 /112|No author title or text discernible|Included blank-looking sheet/back; archive113 only|

### Reused typescripts: their independent printed pagination

| Scan | Printed page | Printed text number | Visible title/continuation |
|---:|---:|---:|---|
|103|47|380|§4 “Algèbres de fonctions”;1 “Algèbres de fonctions continues bornées”|
|099|48|380|Continuation and spectrum/Stone–Čech propositions|
|101|51|380|3 “Sous-algèbres de B(Ω)”|
|111|15|382|Convergent series;3.3.3 and continuation into3.4.1|
|109|18|382|Analytic Taylor/derivative/contact formulas|
|105|19|382|Continuation;3.6 “Critères d’analyticité”|

The printed numbers establish partial orders **47→48→51** and **15→18→19**; they do not establish the full extent, authorship or date of either reused text. Hua’s modernized reading explicitly omits these pages; their inclusion here adds to his inventory without claiming a mathematical link to the surrounding BT drafts.

## Primary literature consulted after freezing

The supplied context’s literature remarks were not promoted wholesale to verified results. The following narrowly targeted checks were made; the modernized reading’s other literature-from-memory remains contextual evidence only.

- **[I85]** Luc Illusie, *Déformations de groupes de Barsotti-Tate (d’après A. Grothendieck)*, Astérisque127 (1985),151–198. Checked locators: introduction p.151; Proposition2.2.4, pp.162–164; Remark4.6(a), p.178. [Primary article](https://www.numdam.org/article/AST_1985__127__151_0.pdf). These checks support N43,N45,N95; no full proof audit is claimed.
- **[I85-err]** Illusie’s [author-hosted erratum](https://www.imo.universite-paris-saclay.fr/~luc.illusie/ErrBT.pdf), concerning the p.165 formula immediately before Remark2.2.6. It was opened when checking[I85]; it is not used to alter any manuscript reading.
- **[B75]** Lawrence Breen, *Un théorème d’annulation pour certains Ext^i de faisceaux abéliens*, Annales scientifiques de l’École Normale Supérieure,4e série8(3) (1975),339–352. Checked the theorem and Remarks1–3, pp.339–340, for the topology, coefficient scope and local/global distinction. [Primary article](https://www.numdam.org/article/ASENS_1975_4_8_3_339_0.pdf).

The Montréal volume’s [French scan](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/barsottitate.pdf) was located, but the available reader returned no usable page text and its screenshot calls did not expose the page images. **No page-by-page collation with that volume is claimed.** In particular, the context’s literature match for the f=p Tate lemma remains credited to Hua’s project; this return establishes what the supplied manuscript says and argues, not its novelty.

## Remaining work with the highest evidential value

The research priorities follow the items, rather than changing their statuses: resolve the Hodge first term and fibre-condition connectors on115; identify Φ and the base abbreviation on110; type-check the level-two maps and the Frobenius twists on090/106/108; recover the absent Illusie letter and NotesI if they are later supplied; and verify the exact arbitrary-quasi-coherent coefficient scope of the vanishing on096. The three kinds of uncertainty—ink, omitted hypothesis, and unproved mathematics—remain distinct throughout this return.
''']
text='\n'.join(lines)
# Readability only: this does not touch any frozen TeX or source phrase.
text=re.sub(r'\b(cote|scans?|page|pages|before|after|on|and|or|of|our|across|between|excluding|June|Astérisque|Proposition|Remark|theorem|Theorem|equations?|programme|Programme)(?=\d)',r'\1 ',text)
text=re.sub(r'\b(on|of|in|from|to|see|by|and)(?=N\d)',r'\1 ',text)
text=re.sub(r'\b(programme|Programme)(?=[IVX]+\b)',r'\1 ',text)
text=re.sub(r'(?<=[;:])(?=[0-9])',' ',text)
text=re.sub(r'(\d{2}): (\d{2}): (\d{2})',r'\1:\2:\3',text)
text=re.sub(r'\b(pp?\.)(?=[0-9])',r'\1 ',text)
text=text.replace('complete local Noetherian hypothesis','complete local hypothesis with a doubtful Noetherian qualifier')
(ROOT/'MPL_129_077-115_notes.md').write_text(text,encoding='utf-8')
print(f'Built {len(NOTES)} research items; context search results inspected by item ID below.')
for n,s in zip(NOTES,search):print(n['id'], {f:len(ls) for f,ls in s['matches'].items()})
