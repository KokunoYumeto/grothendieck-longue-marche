> **NOT THE USER'S DECISION (8 Nov 2026, 17:50 UTC).** This is Claude's draft. PLAN_RECORD.md section 5b lists what in
> it the user never said: the two publications, [the user's words, omitted], [the user's words, omitted], [the user's words, omitted], the per-topic contribution form, the five-part structure and all the conventions. Do not use it for
> prompts or briefs. Read PLAN_RECORD.md and settle the format with the user first.

# The Even Longer March: format of the book and of its contributions

**Two publications (user, 7 and 8 Nov 2026).** (1) The transcription of La Longue Marche, published as it is:
the diplomatic text of the manuscript. (2) The fixed edition, which is The Even Longer March: "the long march and then
the extension of the long march ... all in one file" (7 Nov). It takes Grothendieck's text, fixed (the corrected
reading, his slips corrected), visibly his and in his order, and builds it out: each of his sections is followed by
the development of its topic. The development is not a commentary and not a literature review: it carries the
mathematics further, building the objects and constructions he envisions, stating and proving the results he
announces or asks for, settling his questions where possible, finding the right statements where his are not quite
right, and going on to the next results. Later work (Ihara, Drinfeld, Nakamura, Tamagawa, Mochizuki, Pop and
others) is ground to build on, cited where it is used. A development that spans several of his sections goes after the
section where its topic first arises, with pointers from the others. Each contribution names its author.

Every development prompt (LM_P161 on) works on one topic of the manuscript and returns one contribution in the form
below, so that it goes into its chapter as it is.

## A contribution, as delivered

1. `LM_P1xx-development.tex`: the contribution, in English, with no preamble and no `\documentclass`. It starts with
   `\section{<title>}` and `\label{P1xx}`, then the author line
   `\contributionauthor{<model name and version> (OpenAI), ChatGPT Pro, <month> 2026}`. It is placed directly
   after Grothendieck's text in the chapter of its topic.
2. `LM_P1xx.bib`: the bibliography, every key prefixed `P1xx-` (for example `P1xx-ihara1991`), with a URL of a freely
   accessible version where one exists.
3. `LM_P1xx-standalone.tex`: a short wrapper (`\documentclass{book}`, the packages below, stub definitions of the book
   macros, `\input{LM_P1xx-development}`, the bibliography), and `LM_P1xx-standalone.pdf` compiled from it, to show
   that the contribution compiles.
4. Everything, together with any code and its output, in `LM_P1xx-artifacts.zip`.

## Conventions inside a contribution

- Packages: amsmath, amssymb, amsthm, mathtools, tikz-cd, tikz, hyperref (all standard). No macros of your own other
  than `\newcommand`s defined at the top of the file with the prefix `\Pxx` (for example `\PxxGT` for the
  Grothendieck-Teichmüller group), so that contributions never collide.
- Theorem environments of the book: `theorem`, `proposition`, `lemma`, `corollary`, `conjecture`, `question`,
  `definition`, `example`, `remark`, and `proof`. Labels prefixed `P1xx:` (for example `\label{P1xx:thm:main}`).
- Citing Grothendieck's text: `\lmp{N}` for manuscript page N of La Longue Marche, `\lmeq{n}` for his display (n),
  `\lmscan{140-2}{N}` for an archive scan when no page number applies. In the book these are links to his text in the
  same chapter or another; the standalone wrapper defines them as plain text, for example
  `\newcommand{\lmp}[1]{[LM, p.~#1]}`.
- Quoting Grothendieck: short quotations in French, in quotation marks, with `\lmp{N}`; an English translation follows
  in parentheses where the wording matters. Never paraphrase him as if quoting. His text is in the chapter already: quote only what
  the argument needs.
- Structure of every contribution (as subsections):
  1. **Starting point.** Where Grothendieck takes the topic (`\lmp{N}`), what he claims, asks or plans there, and what
     is established since: the ground the contribution builds on, in a few paragraphs.
  2. **Development.** The new mathematics, the main body: definitions and constructions, theorems with complete
     proofs, the strongest correct versions of his claims, counterexamples with every hypothesis verified where a
     claim fails, and the results that follow, as far as the run can take it.
  3. **Examples and computations** that test and illustrate the development (code and output in the artifacts ZIP).
  4. **What remains**: the next steps of the programme, sharply stated as conjectures or questions.
  5. **Further consequences**: ideas, labelled as such.
- Attribution inside the text: results of the literature are credited where they are used; anything new is said to be
  new only when the literature check supports it.
