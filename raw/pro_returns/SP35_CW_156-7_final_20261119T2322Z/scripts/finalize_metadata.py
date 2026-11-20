"""Final cross-page notation and legibility review, after all eight gates."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
records=[json.loads((root/'records'/f'scan{n:03d}.json').read_text()) for n in range(2,10)]
progress=(root/'progress.log').read_text()
assert all(f'scan {n:03d} done ' in progress for n in range(2,10))
pages=[root/'pages'/f'H156-01_156-7_scan{n:03d}.tex' for n in range(2,10)]
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in pages}
rows=[]
def row(sign,latex,evidence,status='settled unless a local doubt is explicitly noted'):
 rows.append(dict(sign=sign,latex=latex,evidence=evidence,status=status))
row('Quotation marks',"``…''",'002–009: paired short raised strokes, including the quoted support on003, facultatifs/disjoints on008, and propriété on009. Guillemets are not substituted.')
row('Ordinary figure/stratum letters; literal C/G distinctions',r'F,G,X,Y; C,c; C\prime', '004 has small c in the Inf arguments;005–006 retain local C/G doubts.009 distinguishes open C/C′ shapes from adjacent G forms with an inward/lower return. Expected variable matching does not regularize them.','local alternatives and manuscript mismatches retained')
row('Multistrate-set alphabet',r'\unsure{M|\mathcal M}; M','003 and005–007 carry first-occurrence alphabet doubts. Later repetitions use the first candidate.008 and the locally adjudicated009 occurrences follow their own clear stem/valley shapes; one page does not retroactively settle another.','consistent convention; local uncertainty retained')
row('Lieu-set L versus intersection L',r'\unsure{L|\mathcal L}; L; X\prime_L','004’s set-of-lieux L has a looped/cursive ambiguity, inherited by its Fig operators.009 uses L as the named intersection and as a lowered index. Their different roles and local shapes are not globally conflated.','page-specific alphabet decisions retained')
row('Figure-family alphabet',r'\unsure{\mathscr F|\mathcal F};\mathscr F','004–007: looped upper arm, curved descender and middle cross-stroke. Initial script-font uncertainty is retained; subsequent family occurrences use its first candidate. H’s blackletter rendering is separately collated where substantive.','script-family convention consistent; first-occurrence doubts retained')
row('Plain F at the empty-figure subscript',r'\varnothing_F','008: the lowered glyph has a straight stem and two plain arms. It is not forced into the family-set alphabet because of its mathematical role.')
row('Greek subset variable',r'\unsure{\Phi|\varphi};\Phi','005–007: an oval crossed by a stem; capitalization/form remains locally uncertain. The uncertain older φ|y on008 is an overwritten letter, not a reason to change the live capital Y.','local Greek-letter alternatives retained')
row('Tilde and straight overbar',r'\widetilde F;\widetilde X;\widetilde{\mathscr F};\overline{\mathscr F}','003–009: a separately visible wave is a tilde;005 b′ has a straight bar.008 Cor first live F has no independent tilde, unlike its G-tilde neighbour. Sup descenders are not automatically converted into waves.')
row('Primes, case and selected-family exponents',r"X',Y',F',G';F^X;F^x;\widetilde Y^x",'005–009: short raised strokes are primes. Small x and larger X are retained where distinct, especially005 b′ and006 At6/Notation.009’s cancelled F≪F has no supplied prime.','literal prime/case alternation retained')
row('Inclusion and strict order',r'\leq; <','003–009: a single angle with a separate equality bar is ≤.006 AtM2 has a bare strict angle; no lower bar is added from the intended closure condition.')
row('Refinement',r'\ll','004–009: two distinct left-facing angles. It is kept distinct from the closed incidence triangle.')
row('Incidence of a stratum',r'X\triangleleft F','005 definition and006 At6: closed left-facing triangle. The S row’s proposed refinement emendation does not replace the literal triangular ink.','literal triangle settled; intended emendation discussed only in notes')
row('Compatibility base sign',r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}','005–009: two opposing angular paths with a central diamond and four projecting ends. The same inline contour is used. H’s undecorated AMS between symbol is a macro/font realization of this same base sign, not separately counted as an error.','base glyph harmonized; decorations/state checked separately')
row('Compatibility star and relation subscripts',r'{\mathrel{\tikz{...}}}^{*};\underset{M}{\leq};\underset{M}{\ll};\underset{M}{\parallel}','005–008: M sits below whole relation signs;007 has a separate compatibility superscript star. These decorations are not absorbed into the base-sign convention.')
row('Disjointness',r'\parallel','008–009: two upright bars. The lower draft’s general diagonal cancellations are not read as extra negation strokes.')
row('Internal refinement: circle versus filled dot',r'X\overset{\circ}{\ll}Y;Y\overset{\bullet}{\ll}\unsure{:}Z','006–007: open circles above doubled angles;006 At7 has a distinctly filled middle mark and additional doubtful tiny marks. The filled mark is not normalized to an open circle.','local decoration differences retained')
row('Bilateral mapping ticks', 'inline TikZ: horizontal shaft with a perpendicular tick at each end','005 Scholie: the right end has a transverse tick, without a pointed arrowhead. This is kept distinct from mapsto.')
row('Implication, equivalence and rounded shaft returns',r'\Longrightarrow;\Longleftrightarrow;\mathrel{\tikz{...}}','004–009: arrow direction and number of shafts are checked at each locus.007’s slanted implication and009’s doubtful/live shaft loci receive literal contour drawings where the tip is a rounded return rather than a securely isolated triangular head.','local contour decisions retained; no new logical operation inferred')
row('Infimum and supremum labels',r'\mathrm{Inf};\mathrm{Sup}','004 and006–009: capitalization and arguments/indices follow the ink. Inf subscripts distinguish ≤ and ≪; Sup indices retain their individual X/Y/F/G letters, tildes and overwritten layers.')
row('Union annotation',r'\Phi\mathbin{\overset{M}{\cup}}\Psi','006 AtM3: the M belongs above union, not below compatibility.')
row('Operators and their literal case',r'\mathrm{Mulomb},\mathrm{Omb};\mathrm{mulomb},\mathrm{omb}','003 uses upper-case initials;004 has lower-case operators;007 again uses Mulomb/Omb, with no t in Mulomb.007 Omb(x) and M subscript ≪x keep their local lowercase x.','spelling/case variation retained, not standardized')
row('Definition abbreviation',r'\unsure{dfn|defn};\mathrm{dfn}','005–007 retain a locally compressed possible e;008 has a clear d/f/n sequence without a separate e or acute. These are written abbreviations, not expanded definitions.','common primary dfn convention; earlier local alternatives retained')
row('Roman reference numerals and physical bars',r'\underline{\overline{\mathrm{VI}}}','004 and009 references have separately visible upper and lower rules.002’s chapter numeral is VII. Initial-capital and page-number doubts remain local.')
row('Axiom labels, revisions and number order',r'\mathrm{At};\mathrm{At}_M;\mathrm{At\ DC};\mathrm{At\ DD}','002–009: letter order, current/old numbers, and underline spans are transcribed locally.006–007 renumberings and009’s revised lower heading are not standardized to the expected sequence.','local doubts/layers retained exactly in page fragments')
row('Circled equivalence abbreviation', 'ses in an oval open at upper right','008 Cor: the three letters are s/e/s. The drawing retains the small gap; the text is not silently replaced by ssi or expanded.')
row('Hash-like lower relation', 'inline TikZ: two uprights and two short transverse strokes','009 lower slanted counterexample: the visible strokes are retained. Their intended interpretation is not decided by substituting a conventional negated-parallel symbol.','literal contour distinguished from semantic interpretation')
row('Emphasis, insertions and cancellation layers',r'\uline{…};\inserted{…};\deleted{…}','002–009: exact marked spans and local/global cancellation layers are preserved; curved insertion guides are drawn when present.008’s verb is one shared stem with overwritten suffixes, not two independently written whole verbs.','shared macro conventions; local uncertain readings remain marked')
(root/'records/notation_master.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
legibility='''The ordinary body prose and most large formulas are legible enough for close word-by-word comparison, but confidence is uneven. The smallest interlinear additions, overwritten axiom numerals, shared old/new letter strokes, clipped right-edge punctuation and slanted notes crossing other writing are materially harder. The densest limits occur in the long margin on003, the revised axioms and annotations on006–007, the NB and cancelled lower draft on008, and both slanted notes plus the crossed starts on009. Low-confidence alternatives in the transcription should be taken seriously.

C is generally much closer to the visible wording and local layout than H. Many C readings were retained, including surprising spelling, case and formulas. The second pass chiefly corrects or refines insertion attachment, the extent of deletion, fine letter/decoration distinctions, small omitted drawing features and doubts that the crop settles. It also retains or introduces uncertainty where apparently definite text cannot be separated from an overwrite. H more often omits marginal or cancelled wording, supplies plausible connective prose, expands abbreviations, normalizes spelling/letters, or describes a drawing instead of reproducing it. Its editorial notes sometimes correctly acknowledge a cancellation or underline even when the running transcription does not encode it; those acknowledgements are represented in the comparison record.

Agreement between C and H was not treated as evidence. The review includes shared readings overturned from the image, such as the open C′ premises in the two live lower passages on009. Conversely, mathematical inconsistency did not authorize a textual repair: the triangle on006, the lower-case exponents, mismatched letters, K/L alternation and prospective or cancelled assertions remain as written. Apparent a/e endings, calligraphic alphabets and faint strokes are not made certain merely because a conventional expression is expected.

The counts are logged comparison loci, not measured error rates. They mix substantive wording/sign differences, explicit unresolved alternatives, correction-state and placement decisions, and drawing fidelity; confidence describes the ink reading, not whether the manuscript’s mathematics is true. Equivalent emphasis-macro conversions and the ordinary compatibility-glyph rendering are excluded from H-change counts. Only the supplied scans/witnesses/sweep were used for manuscript research. No OCR was used and no manuscript transcription was compiled. A separate prohibited synthetic diagnostic compilation deviation is disclosed in records/protocol_deviations.md; it must not be obscured by a blanket claim of perfect procedural compliance.
'''
(root/'records/legibility.md').write_text(legibility)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in pages};assert before==after
review={'completed_utc':now,'scope':'All8 adjudicated pages, their saved ink/crop decisions and notation entries; no new recognition, compilation or external manuscript research.','checks':['Same undecorated compatibility contour across005–009; separate star and cancellation layers retained.','≤, strict<, ≪ and closed incidence triangle remain distinct.','Open-circle/filled-dot decorations, exponents and primes remain local.','Script family letters are not confused with plain F under the empty sign; first-occurrence alphabet doubts remain local.','Mulomb/mulomb and Omb/omb case differences remain literal; no t supplied.','Definition abbreviation has a consistent dfn primary convention, with earlier e alternatives retained.','Insertion guides, rounded returns, bars, diagram gaps and the hash-like lower009 sign are not normalized from expected mathematics.','All C/H alphabet and emphasis counting reviews applied separately from the fixed page text.'],'page_text_changed_by_this_step':False,'page_sha256':after}
(root/'records/notation_harmonization.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write('notation and documentary harmonization completed '+now+'; all8 page texts compared; no page text changed by metadata consolidation\n')
readme='''# SP35_CW_156-7 — consolidated second-pass transcription

This archive contains all8 requested scans002–009 of cote156-7 (written manuscript pages1–8), read in order by M and three independent readers. Witness H page numbers are one less than the scan numbers. The supplied original scans, witnesses and input archives are deliberately not duplicated here.

## Main deliverables

- `SP35_CW_156-7_transcription.tex`: the complete ordered LaTeX fragment, without a preamble.
- `pages/`: one consolidated fragment per scan, using the supplied PREAMBLE conventions.
- `SP35_CW_156-7_changes.md`: counts, consequential corrections, all three readings at decision loci, evidence, C-doubt audits and remaining uncertainties.
- `SP35_CW_156-7_collation.tsv`: H differences, with the requested columns and scan/page mapping.
- `SP35_CW_156-7_doubts.md`: the consolidated notation table first, followed by remaining doubts, abbreviations and a legibility assessment.
- `SP35_CW_156-7_inventory.csv`: every recorded text, display, drawing, margin, insertion and deletion element, marked transcribed.
- `SP35_CW_156-7_notes.md` and `CHECK_EVENTS.tsv`: page-specific mathematical reading notes, bounded checks, qualifications and the actual check-event ledger.
- `progress.log`: reading gates, timed checkpoints, procedural disclosure and final freeze/hash verification.

## Evidence and work documentation

`readers/` preserves each reader’s complete independent page fragments, reports, C-doubt audits, inspection/crop manifests and relevant audit work. `crops/` contains main-reader evidence crops; reader crops remain in their own directories. `records/` holds the adjudications, notation/counting harmonization, validation reports and saved-checkpoint receipts. `scripts/` records the reproducible assembly, structural checking, freezing and packaging operations. Some scripts expect the original attached source tree alongside this output directory; the input attachments themselves are not copied into this archive.

The manuscript’s slips and uncertainty are intentional features of a diplomatic transcription. A displayed alternative, unmatched punctuation, variable mismatch, surprising spelling or cancelled statement must not be silently repaired. The fragment is to be interpreted with the PREAMBLE supplied in the original witness package. No manuscript transcription was compiled or visually typeset in this run.

The only in-scope sweep row is SA21-K7-01 on006. Its literal triangular reading is confirmed; the redundancy diagnosis and later textual comparison are recorded separately from its conjectured emendation. The exact replacement is not imposed on the transcription.

## Procedural limit

R2 made three prohibited compilation attempts on a synthetic glyph diagnostic during a notation audit. They failed or yielded no readable PDF. No manuscript transcription was the target. The main reader stopped that diagnostic path and disclosed it. The original failed diagnostic files had already been cleaned up; retained reconstructions and available error excerpts are explicitly identified as such. See `records/protocol_deviations.md` and the R2 macro-equivalence audit for the full account. No claim of perfect compliance with the compilation prohibition is made.

## Validation and frozen text

Validation checks source structure, page/reader coverage, every C-doubt count, remaining-doubt coverage, crop paths, inventory/collation columns, ordered concatenation and ZIP integrity. The final SHA-256 manifest freezes all8 page fragments and the combined fragment; the end-of-run verification is written in `progress.log`. These checks do not imply a successful LaTeX compilation or a proof of the manuscript’s general theory.

M/R1/R2/R3 used GPT-6 Astra Pro in this run; the actual effort setting was not exposed. Model/effort descriptions of earlier witnesses are attributed to the supplied metadata rather than to this run.
'''
(root/'README.md').write_text(readme)
print(json.dumps({'notation_rows':len(rows),'page_text_unchanged':True,'metadata_completed_utc':now},indent=2))
