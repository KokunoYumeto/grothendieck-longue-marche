# SP106_CW_103 — notes while reading

These notes concern only the supplied cote 103 scans 15–18. No outside source was consulted. Statements attributed to the letter are reports of what it says, not independently verified historical facts. A textual decision is not a proof of the mathematics. The event IDs below are indexed in `CHECK_EVENTS.tsv`.

## Scan 015 — manuscript continuation on Gr-champs

**N15-M1.** Lines 1–10 say that Gr-champs on X, pinned by a group G and G-module N, form a 2-category, indeed a strict Picard 2-category by an operation “à la Baer”. The corresponding cochain complex truncated at level 2 is given in the display. This classification assertion was read, not proved.

**N15-M2.** The display is `\tau_{\leq 2}(\mathbb R\Gamma(B_G\mathbin{\mathrm{mod}}X,N)[1])`. The NB says that the relative cohomology starts in degree 1. Both instances of R have a supplementary upright; the double-struck alphabet is supported independently at both places (`015_display_left.png`, `015_nb_formula.png`). No shift was added to the NB formula: the written `[1]` occurs only in the display.

**N15-C1 — limited degree check.** With the usual cohomological shift convention, `(K[1])^j=K^{j+1}`, hence `H^j(K[1])=H^{j+1}(K)`. If the unshifted relative complex has no cohomology below degree 1, the shifted complex has no cohomology below degree 0; truncation at 2 retains cohomology corresponding to relative degrees 1, 2 and 3. This says nothing about whether a chosen complex representative has terms below degree 0. This is a check of degree bookkeeping only. It does not establish the claimed correspondence with Gr-champs or the strict Picard structure. The written shift and truncation are consistent with this bookkeeping and were kept from the ink.

**N15-M3.** Lines 13–22 describe the same data geometrically as a 2-gerbe on B_G, linked by N and supplied with a trivialization above X, identified with B_e and the slice by the universal G-torsor P. The page then says that these 2-gerbes form a Picard 3-category “a priori”; the sentence continues on scan 016. The equivalence and 3-category assertion were not independently proved.

**N15-R1 — context versus visible letters.** The subscript after the first B in line 18 is an open e/c-shaped curl. Scan 016 writes `B_e` clearly in the same identification with X; this favors e as the intended common notation, but the remaining stroke uncertainty is documented rather than replaced by a fabricated cross-stroke. P in `(B_G)_{/P}` and the following explanation is clearly capital on this leaf. See the final doubts and audit records for the adopted transcription.

**N15-R2 — incomplete and irregular wording.** At the physical right edge, the first catégorie survives as `catégori`, the later épinglé as `éping`, and trivialisation as `trivialisati`. Their unwritten endings are not supplied. The preceding `géométr…` joins the next line's clear `quement`, with a doubt localized to the partial edge stroke. These are source-edge losses, not proposed author spellings. The written `opération évident`, `cochaines`, `au dessus`, and `le ... objet` remain as written, even where standard French would suggest `évidente`, `cochaînes`, `au-dessus`, or `l'objet`. No grammatical correction changes the page.

**N15-R3 — qualifications, page matter.** The two occurrences of “a priori” are the author's qualifications. There is no explicit “à vérifier”, question mark on a mathematical step, title, date, or stated page count here. The underlined NB and both insertions are source matter. Lower-left pencil 14 is archive foliation, not an autograph page number. No figure or diagram occurs.

## Scan 016 — relative H⁰ and localization

**N16-M1.** Lines 1–8 continue the sentence: the 3-arrows are trivial, with the parenthetical qualification that when source equals target they are identities. The author then treats the 3-category as a 2-category and identifies it with the Gr-champs pinned by G,N. The cropped sign between source and but has two separate horizontal rows and no connecting negation stroke: `=` is the reading. The higher categorical assertion itself was not proved in this run.

**N16-M2 — limited proof check of the parenthesis.** Lines 4–5 write `H^0(B_G/X,N)=0` and explain it by injectivity of `H^0(B_G,N) -> H^0(X,N)`. Under the usual relative convention `RΓ(B_G/X,N)=Cone(RΓ(B_G,N) -> RΓ(X,N))[-1]`, with N a sheaf in degree 0, the long exact sequence gives

`0 -> H^0(B_G/X,N) -> H^0(B_G,N) -> H^0(X,N)`.

Thus the displayed injectivity does imply the stated vanishing. Under the usual interpretation of a G-module on X, global equivariant sections form a subgroup of the underlying global sections, so forgetting equivariance is injective. These are explicit assumptions of this small check; the excerpt does not define the relative complex. This argument verifies that implication and its standard interpretation. It does not prove the asserted classification, the behavior of every 3-arrow, or the later local formula.

**N16-M3.** Lines 9–16 give a complex for the localized Picard 2-champ. The source has a double-struck first R in `\mathbb R p_{G*}`, an ordinary second R in `Rq_{G*}`, and a capital C in `C(q_G^*N)`, overbraced with `rés. inj.`. The annotation identifies the displayed C term as an injective resolution; no different formula has been substituted. The p_G and q_G arrows have ordinary shafts and arrowheads. In the q_G definition the two successive signs are `\approx` and `\simeq`; they are visibly different and are not standardized. The small slice denominator admits P, p and rho from its cramped rounded ink. Because scan 015 explicitly names the same slice object P and identifies its slice with X, the cross-page notation check puts P first while retaining the other visible alternatives. This is a contextual preference within marked ambiguity, not correction of a clearly written lowercase letter. The formula's claimed representational role was not proved.

**N16-M4.** The final paragraph claims compatibility with variation of G,N,X and offers “en principe” a description of the resulting 2-category with these variables. Compatibility is asserted, not derived here. The partly cancelled `do...` is not restored into a clean live `donne` merely because the sentence would become grammatical. The blind audit resolves the surviving prefix as do, but retains uncertainty whether the final e belongs entirely to the cancelled suffix or survives outside it.

**N16-R1.** `cela un fait` has no visible est between the words; the expected `cela est un fait` is not inserted. The final e of `exprime` has no accent; the grammar suggests `exprimé`, but the transcription retains `exprime`. The doubled `champs de Picard` in the description is retained; it is not replaced by an expected Gr-champs. The underline of champ is separate from the insertion leader and from the long g-descender in regardée. The line after the map definition is a paragraph break.

**N16-R2.** The page carries no title, date, or stated page count. Pencil 15 is archive foliation. “en principe” is the explicit qualification. No diagram, drawing, or separate margin prose note occurs.

## Scan 017 — typed jury invitation

**N17-L1.** The heading reads `Villecun|Villecui le 23.6.1974`, with the place-name ending still dependent on damaged type; the date itself is clear. The salutation names Deligne, Giraud and Verdier. There is no separate title or authorial page number. Pencil 16 is archive foliation. The body is one paragraph and the letter continues on scan 018; no signature is on scan 017.

**N17-L2.** The writer reports that Hoang Xuan Sinh had worked, since his Vietnam visit in 1967, on a structural theory of (Gr)-categories and a Picard envelope for a category with associative and commutative product. The typed product sign has a rounded crossed form, recorded as `\unsure{\otimes|\&}` after the blind audit also found an ampersand-like outline. No exact sequence of overtyped keystrokes is asserted. The letter reports receipt of a manuscript and an official report sent to Ta Quang Buu, whose two handwritten accents are separately transcribed. These are contents of the letter, not historical or mathematical verifications.

**N17-L3.** The letter asks whether the recipients would join the thesis jury with the writer. It says Vietnamese approval for presentation and a defense in France was not yet known, and conditionally discusses a Vancouver visit on 20 August 1974 followed by a defense at Orsay in late September or early October. “figurerait”, “Si c'est bien ainsi”, “il me semble plausible”, and “en principe” preserve the letter's conditional status. No subsequent outcome is inferred.

**N17-L4.** The writer offers the complete thesis, a detailed résumé by Sinh, or a less detailed résumé of 13 manuscript pages intended for the CR but judged too long. The 13-page count belongs to that résumé, not to this letter or the package. The report mentioned as “ci-joint” is only mentioned here; these four pages do not establish the larger archive's holdings, so H's editorial assertion about its absence is not adopted as a source fact.

**N17-R1.** The readable typing error `intuile` is preserved. C's single-m `évidement` is rejected: the next-line segment has independent type cells `d-e-m-m-e-n-t`, giving `évidemment` with the preceding `évi-`. The source also has `manuscript`, `ci-joint` after copie, singular `disposé`, and the mixture `rédigées ... trop long`. These were not silently corrected.

**N17-R2.** The raised a is typed. Underletters are preserved before their replacements; some remain uncertain where covered. Handwritten u replaces a typed letter most probably e (with a retained a alternative), genre covers earlier typed cells, and de choses is inserted after genre. The H/X overlap is retained with uncertainty about its typing order; H overwritten by X is the preferred sequence. The two accents above Buu are textual marks encoded with standard LaTeX rather than drawings. A detached hook is not completed into a baseline horn from knowledge of the name. Short typewriter dashes and high paired quotation marks are retained.

## Scan 018 — closing, address and postscript

**N18-L1.** The typed continuation says that the brother of the person named `Mme Hoan Xuan Han` would handle the administrative formalities, gives his address, and requests an early answer. The address begins `Hoang Xuan Sanh`. The visibly different spellings and names are each transcribed locally. The full address line omitted by H belongs to the letter and is restored. It is not treated as a reused administrative list. No attempt was made to identify current residents or validate the historic address or number.

**N18-L2.** The handwritten signature reads Schurik. The PS asks Verdier to forward the letter and report to Giraud because the writer lacks Giraud's address; it says the report should also be usable for university thesis administration in France. The writer's “Je ... pense” is an opinion, not evidence that an administration accepted it. There is no mathematical argument to check on this page.

**N18-R1.** The body name starts Han, with an H comparable to the nearby damaged H of Hoan, not the M preferred by H. The first qui has a damaged but present u; the blind r alternative was checked against its two upright fragments and lower right foot. The telephone digit after 6 remains marked `8|3` after the blind audit, with 8 preferred by the surviving loop fragments. `A toutes fin utile`, `Je,pense`, `celui-ci\_doit`, and `vis à vis` preserve written irregularities. The small line under the final t of attente and the low curve beneath voir are documented with their final audit decisions; neither is silently replaced by expected prose punctuation.

**N18-R2.** No new title, date, or stated page count occurs. Pencil 17 is archive foliation. All source text is in the upper part of the sheet; the lower half has no additional prose. Scattered reproduction marks and faint impressions are not a personal list or a second text and are not transcribed. No legible watermark text was identified anywhere in these four scans. No figure or diagram occurs.

## Scope of the checks

The two mathematical checks above are N15-C1 and N16-M2, and have precisely the limited scopes stated. The categorical equivalences, strictness, local representing complex and compatibility assertions remain source claims. Reading their formulas, correcting a letter, or comparing two transcription witnesses is not an independent proof of those claims. The final audit decisions, including any change after these initial notes, are in `second/`, the changes log, and the doubts table; those records determine the delivered text.
