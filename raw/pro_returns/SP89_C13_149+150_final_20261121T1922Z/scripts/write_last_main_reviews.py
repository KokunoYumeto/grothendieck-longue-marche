from pathlib import Path
import csv
W=Path(__file__).resolve().parents[1]
records={
'150_scan023':[
('P01','Dense retraced author numeral: retain doubtful 6, no reconstructed earlier numeral.'),
('P02','Underlined Thm; Considérons les readable across the sloping marginal overlap.'),
('P03','Raised deux; cancelled phrase preferred ainsi définies over définies ainsi: first low-loop/i body, second tall d/f. Keep doubt under strike.'),
('P04','Cancelled preferred couples over triples, joined middles obscured; raised systèmes, not systèmes inferred from grammar.'),
('P05','Full five-item tuple: tilde X*, dot X, calligraphic E, Y, f. Independent dense upper-right group by dot X remains present unreadable math, not an invented cancelled star.'),
('P06','Full espace; top., has an independent period before comma. dot X partie fermée and calligraphic E un germe.'),
('P07','Singular voisinage cylindrique; no terminal s. dot X and tilde X* read separately.'),
('P08','Y esp. top, has no independent period after top. Map has headless shaft; application legible and final semicolon present.'),
('P09','Singular voisinage cônique with separate accent. Old Comme remains doubtful under strike; old Alors readable and cancelled.'),
('P10','Old le doubtful and cancelled. Live Alors le foncteur naturel; inserted ci-dessus attaches after naturel and before de a).'),
('P11','Rotated marginal text excludes main-text strokes. Analogue and à remain doubtful. Double-underlined voir; after catégories sont, dense cancelled sign and separate preferred équivalentes, including q descender, i dot, l/t. Retain local uncertainty rather than omit the word.'),
('P12','Whole pushout X=tilde X* amalgamated over dot X with Y; no final period.'),
('P13','Marginal NB underlined; pair (tilde X*,dot X), découpage cônique with accent. Final ci-dessus and its attachment locally uncertain.'),
('P14','Underlined NB; live Une partie, raised X′ inserted before de X, then revient donc à une.'),
('P15','Literal tilde X′* de X* (second X has no tilde), Y′ de Y, ayant =. Do not replace shorthand by même.'),
('P16','images inverses dans dot X, et X′ est fermé ssi. Singular fermé retains accent.'),
('P17','Old Pour que X′ soit crossed out; identical raised replacement is live.'),
('P18','Old il f. has looped descending f plus independent point, with doubtful et; bent hook is a leader, not supplied s. Raised une description itself cancelled inside the cancelled clause. Lowered dense star doubtful. New il f et s. que l’on ait: no independent stop after live f; s. point visible.'),
('P19','Literal tilde X′ without star; germe retraced, no distinct earlier word supplied. Calligraphic E de(tilde X,dot X); no period after closing parenthesis.'),
('P20','Preferred lexical completer/compléter over remplacer: initial co/m, p descender and tall l. Detached accent not secure, retain local accent doubt.'),
('P21','Raised tilde X′_1 and whole closure bar over X′ cap X*. No equality sign supplied.'),
('P22','(où X*=tilde X minus dot X), et le germe de tilde X′_1 au vois.; final abbreviation point present.'),
('P23','Thin 22 in another hand, distinct from author numeral.')],
'150_scan024':[
('P01','Plain author 7 without parenthesis.'),
('P02','Full opening formula: dot X subset tilde X; tilde X′_1 cap dot X=dot X′_1, with both lowered 1s and final point.'),
('P03','Corollaire underlined. Raised fermées attaches before X′ by curved leader. cônique has separate accent; completing frame needed for clipped f tip.'),
('P04','One live fermées with heavy retracing, no separate duplicate or recoverable cancelled word. corr. 1-1 and the two pairs retain literal primes.'),
('P05','tilde X′ and germe de clear; upper leader attaches before structure. Interlinear de tilde X,dot X completes a); no added terminal semicolon.'),
('P06','f:dot X to Y arrow head present; old tilde X′ under zigzag remains doubtful. New dot X′ definition has independent accent in déf. Final point after Y′.'),
('P07','Whole Im expression preferred underbrace attachment; physical left end starts below right half of m, before parenthesis. Closure bar independent; nested brace under Y cap X′ labelled Y′. Final union Y′ has no stop. Isolated point near lower X′ not silently made an index.'),
('P08','Long cancellation crosses old underlined strict, compatible and avec. New cônique strict is inserted above, strict singly underlined; old stop uncertain. Live strict resolved from separate t/r/i/c/t strokes.'),
('P09','Both main-line la structure cônique and raised purement are cancelled. Raised leader lands after article before structure. Doubt remains in purement versus germe de and la versus le under strike.'),
('P10','Literal il f et. s.: no point after f, independent points after et and s. Y′=Im(dot X′ to Y), no final stop.'),
('P11','X0 and bordante; literal une germe de retained. Insertion leader attaches germe de before structure.'),
('P12','Calligraphic E/T denote germs; conique has no accent, unlike P03.'),
('P13','Margin au lieu de quoted compatible il est plus parlant de dire quoted underlined transversal. est and parlant resolved at medium from final t, long p and tall l; no terminal stop. Main-text spillover excluded.'),
('P14','Inserted ≃X0×bold I, with visibly heavy I; plain E and T as representatives.'),
('P15','Both cônique words have independent accents; inserted sa before structure with leader.'),
('P16','Three intersection terms and cancelled compat./inserted soient; each E decoration must be retained independently. Root saw separate curved mark over first E and short upper stroke on third; final choice recorded in report after independent trace.'),
('P17','Cancelled bar E cap bar T and homothety sentence; dense beginning not reconstructed beyond recoverable letters.'),
('P18','Cancelled homothety maps retain local base labels and arrow uncertainty; no mathematical completion of obscured strokes.'),
('P19','Margin donc stable par E-homothéties par lambda in [0,1]; no terminal point, surrounding diagram strokes excluded.'),
('P20','Global cancellation diagonals also cross left E i.e. Three-row diagram retains vertical cup inclusions, no inferred heads. Separate dot over middle-left T; E upper marks and right T0 decorations decided locally. Small central crossed group remains doubtful.'),
('P21','Thin 23 in another hand, distinct from author 7.')]
}
for page,rows in records.items():
 with (W/'reports'/page/'main_review.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['place','main_reader_decision']);w.writerows(rows)
