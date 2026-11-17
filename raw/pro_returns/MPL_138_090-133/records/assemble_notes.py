#!/usr/bin/env python3
"""Assemble the research deliverable only; frozen transcription is read-only."""
from pathlib import Path
import hashlib,json,re

R=Path(__file__).resolve().parents[1]
P=R/"records"
PREFIX="MPL_138_090-133"

def source_hashes():
    files=sorted((R/"pages").glob("*.tex"))+[R/(PREFIX+"_transcription.tex")]
    return {str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}

before=source_hashes()
inputs=["early_research.md","maps_moduli_research.md","arithmetic_research.md",
        "root_research.md","maps_moduli_supplement.md","root_research_supplement.md"]
blocks={}
for name in inputs:
    text=(P/name).read_text()
    headings=list(re.finditer(r"^(#{1,3}) (.+)$",text,re.M))
    for k,h in enumerate(headings):
        m=re.match(r"((?:ER|MM|AR|BC|OP|SR)\d\d) — (.+)",h.group(2))
        if not m: continue
        end=len(text)
        for nxt in headings[k+1:]:
            if len(nxt.group(1))<=len(h.group(1)):
                end=nxt.start();break
        ident=m.group(1)
        assert ident not in blocks,ident
        blocks[ident]="### "+h.group(2)+"\n\n"+text[h.end():end].strip()+"\n"
assert len(blocks)==127,len(blocks)

early=(P/"early_research.md").read_text()
context_key=early.split("### Context reference key\n",1)[1].split("## Research items\n",1)[0].strip()
title_audit=early.split("## Standing title, date, and count audit\n",1)[1].split("## Check-event accounting\n",1)[0].strip()
header=r"""# Research notes — MPL_138_090-133

## Scope, evidence and main findings

This report accompanies the diplomatic transcription of all **43 supplied scans**
of cote 138: 90, 91, 93–133. Scan 92 was omitted in the supplied source set. The root
researcher viewed all 129 whole/half images in one transcription stream, completed
the second visual audit of every page, reconciled the notation and uncertainty
apparatus, and froze the 43 page files and combined fragment at
**2026-11-17 23:02:39 UTC**. The context was opened only afterward, at
**23:02:52 UTC**; research assistants worked from the frozen text and context,
not from images, and did no transcription.

There are **127 item-level notes**, each with a source locator, kind, context
relationship and stated scope. Local TeX line numbers are precise locators in
the saved page files, not asserted manuscript lineation. The source retains
all doubtful readings; mathematical corrections, alternative interpretations
and newly supplied arguments occur only here and in the supporting research
records. The doubts file separately records all 335 uncertainty occurrences,
including 332 unsure markers and 3 illegible markers. No result below resolves
a palaeographic uncertainty merely because the mathematics favours one reading.

The supplied context was treated according to its own warnings. The LM text
advertises a second pass; the Esquisse file is an API/collation transcription
not yet checked by eye. Michel Hua's AI-produced modernization is credited
whenever used, with his page numbers one below the present scan numbers.
RESULTS_STATE statuses are quoted as the claims and review statuses of those
runs; neither reading a status nor using a research lead turns it into a
newly proved theorem. The earlier 138 packages 54 and 101 are not present in this
context and have not been reconstructed from their titles.

The principal substantive results are:

- **The manuscript contains the forward arithmetic bridge and a Galois action.**
  Scans 99–103 explicitly connect cartographic classes, algebraic points and
  Γ=Aut(Q̄), and scan 103 says the unpinned action *may* be nontrivial.
  Neither the all-Q̄-curves converse nor global faithfulness is asserted in
  this 43-page range. BC01–BC14 separate this evidence from later statements.
- **The precarte/moduli draft has precise failures.** The literal revised
  morphism rule is not closed under composition (SR01–SR02); cell pinning
  leaves a torus involution, changes ordinary counting and relabelling
  stabilizers, and permits an explicit quadratic-twist obstruction to the
  raw fine moduli functor (MM01–MM11). These findings preserve the valid
  finite geometric-class interpretation.
- **The final sextic question has an exact answer.** Writing
  H=z³(z−1)²(z−c) and reducing modulo
  g=z²−(5c+4)z/6+c/2 gives
  \[
  P(c)=-\frac{(25c^2-32c+16)(25c^3-12c^2-24c-16)}{7776}.
  \]
  With δ(c)=25c²−32c+16, this shows that δ divides P; excluding δ=0 leaves the cubic
  25c³−12c²−24c−16, with arithmetic S3 and geometric monodromy S6.
  The three oriented classes consist of a real class and a mirror pair.
  This is independently certified here and already appears in Jones,
  Example 7.7; no literature novelty is claimed (AR06–AR15).
- **The operation comparison has an arithmetic qualification.** Wood's
  Belyi-extending construction is the requested later reference, but its
  Q-definition condition is essential to the stated Galois-equivariance
  argument. The face-wise pullback criterion, the exceptional endpoint,
  the clean-index condition and orbit-separation limits are treated
  separately (OP10–OP20, OP38–OP46).
- **The holomorphic uniqueness discussion is unfinished and partly false.**
  Hua already observed the positive-dilation counterexample for oranges;
  explicit strict models verify it for every order here. A finite
  face-order sufficient condition is proved with the identity-component
  hypothesis retained, while the infinite case and the full
  rigidification/contractibility claims remain open (OP21–OP37).

The proofs, exact rational-polynomial certificates, finite permutation
enumerations, item-specific context searches, peer reviews and check-event
ledger are included under records/. The ledger distinguishes computation,
targeted checking, independently supplied arguments, background results and
refutations. It does not count ordinary transcription reading as a proof
check. The full small-degree catalogue has not been certified exhaustively;
the checked passports and the remaining interpretation limits are explicit.

## Bridge B6: source evidence versus later conclusions

| Step or question | Evidence in these pages | Conclusion for this package |
|---|---|---|
| A finite map as a cartographic group set | 99:7; 123:8, “groupe cartographique orienté” | Explicitly used, with admissibility and valencies; full classification is an input. |
| A cover of the sphere minus three points | 100–103, covers of P¹; 123–124, cartographic covers and pullback; 129:10–14, explicit holomorphic definition | Present through the covering model; the extra relation at 1 restricts local indices. |
| The associated curve over Q̄ | 103:3–6, equality of Q̄- and C-points | Explicitly asserted. The proposed raw fine-moduli proof needs repair; the forward curve statement is standard background. |
| Γ_Q acting on oriented map classes | 103:6 | Explicit stated conclusion. |
| Commutation with pin relabelling | 103:6 | Explicit, and formally checked for geometric classes with constant labels. |
| Nontrivial arithmetic behaviour | 103:8, complex conjugation; 104–112, examples | The source says “may be nontrivial”; exact examples support it. |
| Every Q̄-curve comes from a map | No assertion found in these 43 pages | The later Esquisse, scans 119/16–17, recalls the question and Belyi's answer; it is retrospective evidence. |
| Faithfulness on all maps or regular maps | No assertion found in these 43 pages | Finite examples do not establish it; the later faithfulness statements must stay separately dated and sourced. |
| The full modern GT action or an equality with Γ_Q | No such construction or identification stated here | The early profinite/Teichmüller questions are relevant precursors, not a completed identification. |

The mathematical dictionary must also retain the distinction between a
branched cover, its underlying curve, an unpinned dessin, a pinned object
and a chosen tuple of monodromy generators. The counterexamples to the
raw pinned moduli functor do not refute the curve-level forward direction.
Conversely, Belyi's curve theorem or later regular-dessin faithfulness
cannot be used to supply a missing claim in an undated draft.

## Standing question 1: steps the author himself leaves unverified

This table distinguishes an actual question or reservation from a proof
claim merely left unwritten. A question inside deleted text is explicitly
marked cancelled. The uncertainty macros are editorial and are not
attributed to the author as his doubts.

| Scan / local line | Author's words or mark | State and corresponding notes |
|---|---|---|
| 90:44 | “Questions … invariant … ? … dist. ds … ?” | Two separate normality questions; ER05–ER06. |
| 90:46–48 | Proposed equality, then “c'est faux pour ν=2” | An equality rejected on the same page; ER07. |
| 99:13 | “Définir ici …” | Explicit drafting instruction, not a completed definition; SR03. |
| 100:20 | “catégorie est rigide”, margin “vérifier” | A genuine verification flag; counterexample in MM02 and explicit descent obstruction in MM05. |
| 107:5–6 | “τ₁₄,τ₄₃ ou τ₄₆ ?”; next alternatives | Cancelled trial, not a surviving conjecture; SR04. |
| 112:3–5 | “Mais pourraient-ils être zéros de … δ(c) … ?” | Answered yes by the exact factorization, with essential degeneracy exclusion; AR09–AR10. |
| 121:3 | “axiomatique provisoire” | Explicit provisional status of the section; OP01. |
| 128:7 | “Que se passe-t-il dans le cas exceptionnel?” | Left open on the sheet; local answer and limits in OP15–OP17. |
| 129:16–29 | “Unicité d'un tel φ?”; “Or c'est faux déjà pour la sphère” | Unconditional uniqueness immediately abandoned; OP26. |
| 130:21–26 | “a-t-on gagné? J'ai l'impression que oui”; margin “au moins pour les cartes finies” | Tentative finite repair; OP30–OP31. |
| 131:9–11 | “il semble que les seuls cas …” | Tentative exception list, refuted by the orange family; OP35. |
| 131:13–16 | “tirer au clair entièrement … voir s'il s'applique aux cartes infinies” | Expressly unfinished conformal argument and infinite extension; OP36. |

Additional proof obligations appear as assertions: scan 98's “foncteur évident”
(SR01), scan 123's “argument … formel” and “On prouve … aussitôt”
(OP05, OP09), and scan 126's “évident” plus the interrupted disc proof
(OP22–OP24). Scan 132 lists conditions without declaring their equivalence
(OP38–OP41). These are recorded separately from the author's explicit
reservation language.

## Standing question 2: title sheets, extent and dated reused matter

"""

status=r"""

## Relation to the supplied results register

| RESULTS_STATE item | Supplied status retained | What this package contributes or does not decide |
|---|---|---|
| EXIT_TOWER E.24 | Open, return's claim | Concrete maps, finite arithmetic actions and naturality tests; no full arithmetic-image computation. |
| LM1 D.7 | Open, return's claim | Early distinction of geometric completion and a larger ambient group; no equality of Galois, GT and GT₀ images. |
| LM4 C.12 | Open, return's claim | Finite-kernel arguments and a sphere action illustrating their limit; not the requested hyperbolic centralizer π₁ comparison. |
| LM4 D.12 | Open, return's claim | Particular complex-conjugation/mirror tests; no classification of all profinite torsion. |
| LM4 D.32 | Proved as claimed in the stated 14 Nov referee review | Used only as a status/scope comparison; its finite three-cusp result is not substituted for an equality of ambient groups. |
| LM4_SUCCESSOR B.38 | Open, return's claim | No computation of its congruence kernels, including K₅. |
| LM4_SUCCESSOR B.12 | Open, return's claim | The weighted presentation in scan 91 is a comparison, not a solution of its corrected orbifold target. |
| LM6 F.35 | Proved, return's claim | A context lead on identifications/forgetful maps; not re-proved here. |
| LM6 B.27 | Open, return's claim | Cyclotomic inertia observations; no answer to its centralizer question. |
| LM7_PUSH E.3 | Open, return's claim | A small Kummer field example; no CM-image answer. |
| EXIT_TOWER E.49 | Explicitly unrefereed claim in the supplied orientation | Not used to declare E.3 settled. |
| LM2 C.d1, C.r1–C.r3 | Unreviewed return claims in LM2_CONGRUENCE_ROWS.md | Bridge B5 is distinguished from this packet's finite maps; no re-proof or status change. |
| WG H1, WG H5 | Unchecked war-game hunches | Peripheral and finite-monodromy comparisons only; not adopted as theorems. |
| MPL_147_003-047 N075 | First-pass research lead | Separates covering naturality from full boundary/gluing compatibility. |
| 138-operations-belyi-extending | Hua candidate finding / research lead | Credited, compared with Wood, and given precise field/index qualifications. |
| 138-operations-subset-criterion | Hua candidate finding / research lead | Its stated condition on A is refuted; a finite face-wise refinement is supplied as OP12. |

These rows do not edit or silently update the external register. The local
checks and refinements have their own note IDs and CHECK_EVENTS rows.

## Context key for the early-page notes

"""

sections=[
 ("1. Peripheral groups, torsors and the common character",
  [f"ER{i:02}" for i in range(1,21)]+["SR06"]),
 ("2. Precartes, pinning, moduli and geometric class spaces",
  ["SR01","SR02"]+[f"MM{i:02}" for i in range(1,13)]+["SR03"]),
 ("3. B6 and the historical scope of the arithmetic programme",
  [f"BC{i:02}" for i in range(1,15)]),
 ("4. Explicit rational functions and the sextic calculation",
  [f"AR{i:02}" for i in range(1,19)]+["SR04","SR05"]),
 ("5. The spherical catalogue and its working annotations",
  [f"MM{i:02}" for i in range(13,18)]+[f"SR{i:02}" for i in range(7,12)]),
 ("6. Spherical operations, rigidification and holomorphic maps",
  [f"OP{i:02}" for i in range(1,47)]+["SR12"]),
]
used=[x for _,xs in sections for x in xs]
assert len(used)==len(set(used))==len(blocks)
assert set(used)==set(blocks)

bibliography=r"""

## Primary literature and exact extent of use

All external references below were opened during the research phase.
The attached context is separately cited by filename and scan/section in
the notes; its supplied transcriptions have not been independently audited
against their original images in this run.

| Key | Source | Exact locus and use |
|---|---|---|
| B | G. V. Belyi, *On Galois extensions of a maximal cyclotomic field*, Russian original 1979; English translation, Mathematics of the USSR-Izvestiya 14 (1980),247–256. [Primary record](https://www.mathnet.ru/eng/im1682), [primary PDF](https://www.mathnet.ru/links/1804cbcccc9d2ceb0aac43687d62147c/im1682_eng.pdf). | §4, Theorem 4; curve/three-point-cover equivalence carried as background, not independently re-proved. |
| GDJZ | G. González-Diez and A. Jaikin-Zapirain, *The absolute Galois group acts faithfully on regular dessins and on Beauville surfaces*, Proceedings of the London Mathematical Society 111 (2015),775–796. [Author PDF](https://matematicas.uam.es/~andrei.jaikin/preprints/galoisactionshort.pdf), [DOI](https://doi.org/10.1112/plms/pdv041). | Theorem 18; later regular-dessin faithfulness comparison only, not a manuscript-era attribution or a proof recheck. |
| W | M. Matchett Wood, *Belyi-Extending Maps and the Galois Action on Dessins d'Enfants*, PRIMS 42 (2006),721–737. [Publisher](https://ems.press/journals/prims/articles/2260), [author preprint](https://arxiv.org/pdf/math/0304489). | §3.1 definition and Proposition 2; §3.2–3.3 construction; Proposition 4's separation example used as a cited result, not recomputed. |
| J | G. A. Jones, *Regular dessins with a given automorphism group*, arXiv:1309.5219v1 (2013). [Primary PDF](https://arxiv.org/pdf/1309.5219). | Example 7.7, printed p. 12; exact known sextic/cubic example matched after the independent calculation. The books cited there were not opened. |
| CK | A. Constantin and B. Kolev, *The theorem of Kerékjártó on periodic homeomorphisms of the disc and the sphere*, L'Enseignement Mathématique 40 (1994),193–204. [Author version](https://arxiv.org/pdf/math/0303256). | Proposition 3.2 and its invariant-arc step; the preceding topological lemma is carried as background. |
| SGA | A. Grothendieck et al., *Revêtements étales et groupe fondamental (SGA 1)*, recomposed edition. [Primary text](https://arxiv.org/pdf/math/0206203). | Exposé XIII, Corollary 2.9, construction 2.10, Lemma 2.11; prime-to-characteristic framework, not proof of the raw pinned functor. |
| ST | The Stacks Project. [Tag 03QR](https://stacks.math.columbia.edu/tag/03QR); [tag 03SF](https://stacks.math.columbia.edu/tag/03SF). | Étale schemes over a field and continuous Galois sets; finite Galois covers and normal subgroups. |
| F | W. Fulton, *Hurwitz schemes and irreducibility of moduli of algebraic curves*, Annals of Mathematics 90 (1969),542–575. [Publisher record](https://annals.math.princeton.edu/1969/91-3/p06). | Bibliographic verification of Hua's reference only; no theorem is claimed checked for the present functor. |

## Reproduction, check boundaries and transcription integrity

The main exact calculations are reproducible by running, from the extracted
package directory, the following scripts:

~~~sh
python3 records/arithmetic_certificate.py
python3 records/arithmetic_supplement.py
python3 records/check_maps_moduli.py
python3 records/operations_certificate.py
~~~

The arithmetic scripts use SymPy; the finite-permutation map script uses
the Python standard library. The accompanying JSON files retain the
successful results even if a reader has no runtime installed. The longer
arguments are in records/maps_moduli_checks.md,
records/maps_moduli_supplement_checks.md and records/operations_proofs.md.
These scripts compute research checks; the historical page-writing scripts
are preserved as work records and should not be rerun over the frozen files.

Peer checks are documented in records/operations_peer_review.md and
records/b6_arithmetic_peer_review.md. The latter found an overly strong
“only G_K” phrase and a section-number slip in a draft research note;
both were corrected in the notes, with the source untouched. Coverage
review found several omitted research dispositions, now SR01–SR12.
These reviews are bounded checks, not an independent re-transcription.

The exact frozen hashes are in records/frozen_hashes.json and progress.log.
The final integrity confirmation is appended to progress.log after
assembly. Structural validation does not prove that every difficult word
or drawn curve has been read correctly; the doubt apparatus and the
explicit limits on catalogue identification remain part of the deliverable.
No source image or context file is included in this package. No compiled
PDF is claimed: the available TeX installation lacked the required format
and class/package files, so the saved source received structural checks
rather than a successful TeX rendering.
"""

parts=[header,title_audit,status,context_key]
for title,idents in sections:
    parts.append("\n\n## "+title+"\n\n")
    parts.extend(blocks[x]+"\n" for x in idents)
parts.append(bibliography)
dest=R/(PREFIX+"_notes.md")
dest.write_text("\n".join(parts))
assert source_hashes()==before,"Assembly changed a frozen source"
manifest={"note_count":len(blocks),"ids":used,"sources":inputs,
          "output":dest.name,"word_count":len(dest.read_text().split()),
          "frozen_source_hashes_unchanged":True}
(P/"notes_assembly.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(manifest,ensure_ascii=False))
