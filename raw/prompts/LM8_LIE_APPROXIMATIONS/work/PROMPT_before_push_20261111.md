# LM8_LIE_APPROXIMATIONS: Lie approximations of Galois–Teichmüller systems, L-groups, and the special Teichmüller group of type (1,1) (§§52–53)

DRAFT, provisional (11 November 2026); waits for the second pass of cote 140-4, scans 172–280. The statement of this prompt rests on the first-pass transcription and on the author's table of contents, and must be rewritten when the checked text exists. Development prompt for Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981). File prefix for your deliverables: `LM8_LIE_APPROXIMATIONS`.

## What is to be settled

The last two sections (cote 140-4, folios 737–787) turn the example of §51 into a programme. §52, "Approximations de Lie des systèmes de Galois-Teichmüller": 1) the notion of L-group and TL-group, discrete case; 2) profinite case; 3) Lie approximation of Galois–Teichmüller systems; 4) the Lie approximation induced by a "geometric" one. §53, "Le groupe de Teichmüller spécial ST_{1,1} ≅ GL(2, Z)^~ et le groupe SN_{1,1}": 1) differential action and special Teichmüller group (provisional statement); 2) the groups `GL(2, R)^~_{±1}`, `SL(2, R)^~`; 3) the group `GL(2, Z)^~`; 4) the isomorphism `GL(2, Z)^~ ≅ ST_{1,1}`; 5) a digression on coverings of germs of spaces and the relation between topological and differentiable germs of surfaces. The second pass has fixed two readings of the table: "ΠL-groupes" in the struck heading of §52, and "groupe de Teichmüller spécial".

What he states or asks (cote 140-4 scans, first-pass readings):
1. "Il semble que ∀ L-groupe soit isomorphe à un groupe obtenu ainsi", that is, from a finite group acting on a surface (183); centralizer conditions and a characterization up to non-unique isomorphism (185–186); Teichmüller groups defined in this context (187–188).
2. Modular multiplicities over `Q` and `Z` (193–197): is every such multiplicity the quotient of a smooth quasi-projective curve by a finite group?
3. Galois–Teichmüller structures and their axioms (204–208); quasi-unipotent homomorphisms and integral one-parameter subgroups (210–221); presentations by generators and relations (231); a limiting topos (242–243).
4. The successive Lie approximations of `π_1` and of the extension, each refinement calling for a new study of splittings (173, 178), with §51 as the "approximation minima".
5. §53: the special Teichmüller group of type `(1,1)` as a central extension `GL(2, Z)^~`, the group `SN_{1,1}`, and the 140-1 draft's `1 → Z → ? → SL(2, Z) → 1` (scan 29 of cote 140-1).

## Leads (unverified; prove or refute each)

- **Lead 1.** A "Lie approximation" is a functorial quotient of the tower of profinite Teichmüller groups with Galois action in which the geometric fundamental groups are replaced by pro-algebraic (schematic) envelopes of their nilpotent or solvable quotients, as in §50. The later theories it should be compared with: Deligne's and Hain's relative (weighted) completion of mapping class groups; the pro-unipotent Grothendieck–Teichmüller group `GT(k)` and the graded Lie algebra `grt` (Drinfeld); Hain–Matsumoto's weighted completion of Galois groups; Enriquez's elliptic `GT`. Which of these, if any, is his §52.3 object is to be determined from his axioms.
- **Lead 2.** His "special Teichmüller group" `ST_{1,1}` is the mapping class group of the torus with one boundary component (or with a tangent direction at the puncture), a central extension of `SL(2, Z)` by `Z`, namely the braid group `B_3`; `GL(2, Z)^~` adds the orientation-reversing classes. `SN_{1,1}` should then be the corresponding arithmetic extension, with `Gal(Q̄/Q)` acting through the Tate-curve tangential base point (Nakamura).
- **Lead 3.** Item 2 is the uniformization question for one-dimensional Deligne–Mumford stacks: such a stack over a field of characteristic 0 is a global quotient of a curve by a finite group except in known "bad orbifold" cases (the teardrop and the spindle with unequal orders); over `Z` and with gerbe structure the question is finer (Behrend–Noohi).
- **Lead 4.** §53.5, on germs of coverings and topological against differentiable germs of surfaces, is the theory of the "punctured neighbourhood" of a point or of a divisor, that is, tangential base points and the comparison `Homeo` against `Diff` in dimension 2.

## Parts

**A. §52.1–2.** Definitions of L-groups, ΠL-groups and TL-groups, discrete and profinite, as he gives them; item 1 completely (proof or counterexample; the non-uniqueness made exact); the Teichmüller groups of this context identified.

**B. §52.3–4.** His axioms of a Galois–Teichmüller structure written out as a definition; the Lie approximations constructed in general from the envelopes of §50 (use LM1_GROUP_SCHEMES, Part E, if attached); the first two approximations computed for types `(0,3)`, `(0,4)`, `(1,1)`; comparison with the theories of Lead 1, each as a theorem (his object maps to, is, or differs from theirs, with proof); the "limiting topos" of scans 242–243 defined and identified.

**C. Item 2.** State his question on modular multiplicities exactly and answer it over `Q̄`, `Q` and `Z`.

**D. Item 3, the remaining statements:** quasi-unipotent homomorphisms, integral one-parameter subgroups, the presentations of scan 231: proved or corrected.

**E. §53.** The groups `GL(2, R)^~_{±1}`, `SL(2, R)^~`, `GL(2, Z)^~`; the isomorphism with `ST_{1,1}` proved; `SN_{1,1}` constructed with its Galois action; the differential action and the germ statements of §53.5 made precise and proved.

**F. Splittings again (item 4).** For each Lie approximation computed in Part B, the set of splittings of the corresponding extension over `Gal(Q̄/Q)` and what it says about rational points; pass the result to LM6_POINTS_AS_SECTIONS, Part E.

---

THE TEXT YOU ARE GIVEN
- Grothendieck wrote *La Longue Marche à travers la théorie de Galois* by hand between January and June 1981. It was never prepared for print. What is attached is a transcription of the manuscript made by AI from scans (first pass: GPT-6 Astra, ChatGPT Pro mode; second pass, line by line against the scans: Claude, Anthropic), by package. The manuscript is in four archive files: cote 140-2 (folios 1–292, §§1–37), cote 140-3 (folios 293–650, §§38–49), cote 140-4 (folios 650bis–787, §§50–53) and cote 140-1 (a draft of 37 scans). `\scanpage{n}` marks the scan, `\mspage{n}` his folio number.
- Marks in the transcription: `\unsure{a|b}` a doubtful reading with its alternatives; `\illegible{n}` unread words; `\deleted{…}` struck by the author; `\inserted{…}` added by him; `\margin{…}` a marginal note. A reading is never final. Where your mathematics depends on a doubtful or unread place, say so at that place, work with each alternative that makes sense, and report which one the mathematics supports as evidence for the editors, with the scan number. Do not silently choose, and do not call any reading settled. The scans of the pages that matter are attached: look at them.
- His notation changes as he goes, sometimes within a section ("Notations définitives (?)", §46). Fix yours on the first page with a table giving, for each symbol you use, his symbol and the scan where he introduces it.
- He marks his own doubts ("un peu faux", "ultra-faux", "sauf erreur", "peut-être est-ce tout à fait faux ?", "Théorème (!)"). These are part of the text: a statement he doubts is treated as a question, one he withdraws as withdrawn.

WHAT IS ATTACHED
A zip with: the transcription packages listed in the manifest (the current text of each), the scans of the pages named in this prompt, his table of contents, the checked research notes of those packages (notes by the transcribing models on his conjectures, unproved claims and unpursued implications; drafts, not authority), the background papers, and `OVERVIEW.md` (a reading of the whole manuscript by Claude, from which the leads below come).

RULES OF PROOF (they bind every statement you deliver)
1. State the actual claim with all its data: which group (discrete, profinite, pro-ℓ), which field, which type `(g, ν)`, outer or genuine actions, base points and the choices they involve, which topology, which of his numbered conditions in which version. Do not replace it by a convenient special case; if you prove a special case, name it as one and keep the general statement on your list as open.
2. Type every map: source, target, the category in which it is a morphism, and each property you use (continuous, open, compatible with which outer action, defined up to which inner automorphisms).
3. Every reduction ("we may assume", "pass to an open subgroup", "fill the holes", "replace by a covering") comes with its comparison map and a proof that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: a homomorphism and its class modulo inner automorphisms; an isomorphism and a canonical isomorphism; injective, with open image, bijective; a discrete group and its profinite completion (and say when the completion map is injective); a statement over `Q` and over a finite extension.
5. Check the cases he sets aside or forgets: types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)`; `(0,3)` and `(1,1)` against the general anabelian type; residue characteristics 2 and 3; non-orientable and real cases; trivial and non-trivial centres.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you attach. One verified counterexample refutes the statement: say "false", and then find the strongest true statement in its place. An invalid proof alone shows a gap, not falsity.
7. No authority. His assertions, the notes of the transcribing models, and the leads marked "Lead" below (inferences by Claude from one reading, checked by no one) are all to be proved or refuted. If a lead is wrong, say so plainly.
8. Later work (Belyi, Drinfeld, Ihara, Nakamura, Matsumoto, Tamagawa, Mochizuki, Pop, Hoshi, Boggi and others) is to be used, with exact theorem numbers, wherever it proves or refutes what he asks. The task is to do the mathematics he set out, with everything now available, and to carry it to where it stops; it is not a survey. Never invent a reference; mark each bibliography entry `verified` (you opened it) or `unverified`. Before calling anything new, say what you searched.
9. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the smallest undecided instance. Never write it up as proved, and never drop it.
10. Known and Open are not end points. A Known statement is derived from the cited theorem in the form he states it, with the proof of the reduction. An Open statement records your own attack: the strongest partial result you proved, the computations you ran, the obstruction as an exact statement. A row "open, see [reference]" without your own attempt is unfinished.

WHAT TO DELIVER
One ZIP containing:
- `<ID>_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the parts, every statement numbered and labelled Proved / Refuted / Known (with citation) / Open, with complete proofs; each statement that answers a passage of the manuscript cites it by section, folio and scan. English, first person plural, the register of a careful research paper; quote Grothendieck in French where his wording matters, and never write in his voice. This text is meant for a book that reproduces his text and builds it out; how it will be placed there is not decided, so make it readable on its own.
- `<ID>_results.csv`: one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_passages (section; folio; scan), depends_on_doubtful_reading (scan, alternatives), notes`.
- `<ID>_readings.csv`: every place where the mathematics bears on a doubtful reading: `package, scan, the \unsure or \illegible place, what the mathematics supports, how strongly`.
- `<ID>_references.bib`, `<ID>_report.md` (what you read, what you computed, corrections to the leads and to the notes, what remains open), and `code/`.
The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and claim no priority.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go.
