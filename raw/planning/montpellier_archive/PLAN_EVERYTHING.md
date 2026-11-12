# The Montpellier archive: the plan for all of it

The user, 10 Nov 2026: "download fucking everything", "organize it on topic", "Up contrast"; transcription in Pro mode
in packages sized to 60-80 minutes of work; and for the plan: "assume we do everything. This is the way to do
everything, and this is the order in which we probably want to do that". What each section holds, how far Grothendieck
took it and who has edited it: `SECTIONS_STATE.md` (10 Nov). Estimates below come from our own record; the first
package corrects them.

## Scope

- 178 cotes, 16,074 site pages (versos included). About 11,300 pages have no edition, transcription or study.
- Already ours: *La Longue Marche* (cote 140, 1,584 pp.): transcription done, second pass running. *Les Dérivateurs*
  (157-160): the Künzer-Malgoire-Maltsiniotis edition is complete; our companion covers 28 of its 32 chunks.
- Complete outside editions: *Pursuing Stacks* (134-135; arXiv 2021, SMF vol. I) and the *Esquisse* (in print in
  French and English). These are transcribed last, and serve as checks meanwhile.

## The stages, for every section

1. **Download, organize, enhance** (running since 10 Nov): `archive_tool.py download` puts every cote in its topic
   folder (30 of 178 cotes, 1.2 GB on 10 Nov at 23:00 local; the server is slow). Packages use the Longue Marche image
   recipe.
2. **Transcription by GPT-6 Astra in ChatGPT Pro mode.**
   - Each prompt gets one zip of about 45 scans, sized to 60-80 minutes; the Longue Marche's 20-scan packages took
     23-30 minutes.
   - Output: diplomatic LaTeX, a table of doubts, an inventory, pointers, one file per page and a time log
     (`ARCHIVE_PROMPT_TEMPLATE.md`).
   - The first package (MPL_1_002-050) sets the size.
   - About 260 prompts for everything, fewer once blank sheets drop out. Pro mode may be merged by the end of
     November; the user would buy a second Pro account for about 100 more prompts.
3. **Second pass by Claude subagents**, as for the Longue Marche: each package checked against its scans, then the
   global view across each section. It is the largest subscription cost, so it runs in the Ultra weeks (the Fable half
   first: account plan on card plan-now).
4. **Editions on GitHub**, published per book and chapter of the shape below, with the cote order as the second index (Fable, 10 Nov); per section: the diplomatic French and a reading text, anchored to cote and scan, with the
   rights statement and credit to every earlier edition used as a check.
5. **English translation** with the method agreed on 10 Nov for the Longue Marche and *Les Dérivateurs*:
   - a glossary and notation table made by Fable;
   - scripts that lock the formulas and check every unit;
   - the model and route chosen on a small comparison, at the quality of Opus 5.5 at high effort or better.
   - At our transcription price as a ceiling ($0.065 a page), that is about $700 for 11,300 pages; the comparison
     sets the real figure.
6. **Development**, for the sections left as research. Either a companion in the *Dérivateurs* style (commentary
   blocks, later work, examples, what we could push), or a book in the Longue Marche style (his text, then built out).
   - Candidates: *Géométrie des formes*, combinatorial geometry, the notes around the Longue Marche (into the LM book),
     De Rham, motives, stratified spaces.
   - **EGA V and after.** The user, 10 Nov: "It's almost like write EGA5 then"; "whatever stuff would otherwise gone
     there, that isn't already in any of the EGAs"; "there might be more basics implied by the working through of
     this that should be part of that concept"; "regardless, it should be done. What it ends up being called it's not
     necessarily the" point.
     - Scope: his EGA drafts and plans (cotes 21-26), plus the foundational material scattered through the rest of the
       archive. What EGA I-IV, SGA or FGA already contain is cited, not redone.
     - Authorship as it is: his notes and plans, transcribed; the development AI-produced, with each part's author and
       model named ("we don't have to pretend that it was written by the original authors").
     - Title open. First step, once the EGA drafts are transcribed: a map of what they contain against EGA I-IV, SGA
       and FGA.

## Shape and order: Fable's recommendation, adopted (10 Nov, late)

Source: `ORGANIZATION_RECOMMENDATION.md` (Claude Fable 5.2), asked for by the user: "how to organize the whole fucking
blob of this shit in a way that makes it something that people click on and want to read eventually."

- **Working title *The Montpellier Manuscripts*.**
  - Front door: the annotated *Esquisse*, each section linking to the book behind it.
  - Six books: I. Elements, continued ("EGA V and after"); II. Cohomology and motives; III. The Long March; IV. Maps
    and polyhedra; V. Tame topology and the geometry of forms; VI. Stacks and derivators.
  - A workshop: early notes, documents, and the concordance from cote and scan to book and chapter.
- **Every page in three layers:** what the folder is and what became of it; his text, French and English, linked to
  the scan; commentary and, where he left the work open, a development with full proofs. His text and ours never
  share a paragraph. The second pass also produces a register of every question and conjecture in the notes, with
  its status today.
- **Transcription order**, after the pilot (cote 1):
  1. around the Long March: 147, 149, 146, 142;
  2. the 1960s test: 16, 47, 54, 44;
  3. the EGA drafts and plans: 21, 22, 23, 26, 35, 48, 102;
  4. the dated notes around the Long March: 144, 148, 143, 145, 141;
  5. stratified spaces and tame topology: 150-153, 155, 120, 121;
  6. motives: 14, 13, 12, 15, 18;
  7. crystals: 5-9, 4, 100;
  8. the 1976 de Rham notes: 137, 136;
  9. around Pursuing Stacks and the derivators: 158, 103-118, 135;
  10. maps and their arithmetic: 138, 76, 88, 70, 75, 161-6;
  11. the final state of the *Géométrie des formes*: 156-8, 156-1 to 156-3, 156-5, 156-9.

  These come to about 4,200 pages, the first tranche. The rest follows Fable's file.
- **Clean typescripts** (24; 25, "Nouveau EGA V", early; 119, 134, 157, 162-5) go by the clean-scan route over the
  API, not Pro.
- **Before packaging**, an inventory of the versos, so that unrelated pages (administrative circulars, other people's
  typescripts) are left out and listed.
- The download follows this order (`DOWNLOAD_PRIORITY.txt`).

Claude's earlier order (the *Géométrie des formes* second, the combinatorial block whole) is superseded.

## Everything, by route (11 Nov 2026, computed from MANIFEST.csv and Fable's ranks)

| Part | Cotes | Site pages | Route | Pro prompts at 90 pp. (at 45) | Book |
|---|---|---|---|---|---|
| First tranche, ranks 0-11 | see ORGANIZATION_RECOMMENDATION.md §5 | 4,324 | Pro mode | about 54 (101) | III, II, I (plans), V, VI, IV |
| Second tranche, ranks 12-20 | 64, 67, 159; 10, 11, 56, 60; 79, 83, 72, 86, 85, 69, 74; 93; 161-1 to 161-4, 19; 156-4, 156-6, 156-7; 71-89 rest, 154; 43-59 abelian/Picard; 90-101 | 4,362 | Pro mode | about 55 (102) | II, IV, V, I, front door |
| Third tranche, ranks 21-25 | SGA drafts, descent and heights, old elliptic curves, remaining SGA, early notes and remnants | 2,189 | Pro mode | about 27 (52) | I, workshop |
| Clean typescripts | 24, 25 (Nouveau EGA V), 119 (Esquisse), 162-5 | 641 | API (clean-scan route) | 0 | I, front door |
| Pursuing Stacks | 134-1 to 134-8 | 837 | API (clean typescript; the 2021/SMF edition checks it) | 0 | VI |
| Les Dérivateurs, manuscript | 157-1 to 157-5 | 2,135 | done through the printed edition (our transcription and companion) | 0 | VI |
| La Longue Marche | 140-x | 1,584 | done (second pass finishing) | 0 | III |
| Medal | 139 | 2 | concordance only | 0 | workshop |
| **Total** | 178 cotes | **16,074** | | **about 136 (255)**, 2 done | |

Prompt counts assume the small cotes of one rank share a package (the packager needs a multi-cote option) and do not
subtract blank sheets, which the packager drops (about 8 % in the pilot). Cote 110 is not in the manifest.

**Superseded in detail by `PLACEMENT_EVERYTHING.md` / `.csv` (Claude Fable 5.2, 11 Nov):** every cote has a book, chapter, rank, route and package. By route: Pro 10,761 pp. (129 moved to the API: a clean typescript), API 1,592, done 3,719 (Longue Marche; Dérivateurs through the printed edition), medal 2. Pro prompts for everything: 134 at 90 scans (254 at 45), two already sent; upper bounds before blank sheets and inventoried typed sheets drop out. 18 cotes to inventory for versos before packaging (listed there). The packager needs a multi-cote option.

**11 Nov 2026 (user):** *Pursuing Stacks* is already typed up. That was done not by us but by the person who posted
it on arXiv (2021), and the SMF edition exists too. Our CJK translations were made from that typed-up version. The
user was only checking this ("didn't say we shouldn't do it"). The Pursuing Stacks row in the table above stands:
134-1 to 134-8 by the API route, with the typed-up version and the SMF edition as checks.

The API is the scarcer resource. At our measured rate (Opus 5.5 at batch prices, $0.06 a page, Dérivateurs pilot),
the clean typescripts (641 pp.) cost about $38, and a Pursuing Stacks check (837 pp.) about $50.
