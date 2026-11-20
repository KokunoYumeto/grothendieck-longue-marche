from record import *
s=45
src=ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-06/pages/J71-06_71_scan045.tex'
t=src.read_text(encoding='utf-8')
for a,b in [(r'\mspage{XVII}',r'\mspage{$\underline{\overline{\mathrm{XVII}}}$}'),(r'\unsure{\subset|\in}',r'\subset'),(r'\unsure{\={a}|à}',r'\={a}'),(r'\unsure{secteur|seeteur}',r'secteur'),(r'\unsure{\phi|\varnothing}',r'\varnothing'),(r'\phi',r'\varnothing'),(r'\deleted{\unsure{et}}',r'\deleted{et}'),(r'\mathbin{\unsure{\dot{-}|-}}',r'\mathbin{\dot{-}}'),(r'\Lambda^{\unsure{1|4|+}}',r'\Lambda^{\unsure{4|1|+}}')]:
 assert a in t,a
 t=t.replace(a,b)
(ROOT/'pages'/src.name).write_text(t,encoding='utf-8')
H='No source text (editorial synopsis only)'
change(s,'045-C01','manuscript folio','XVII',H,'XVII with upper and lower rules','Halves: both horizontal rules visibly bound the numeral.',c=True,kind='omission')
change(s,'045-C02','Lemme XIX proof, Comme Λ exponent','1 | 4 | +',H,'4 | 1 | +','Scan 45 crop (520,1990,594,2064): a diagonal upstroke, long right stem and projecting crossbar favor 4. Retracing leaves 1 or + possible; the expected 1 does not override the crossbar.','medium',c=True,kind='misread symbol or index',consequential='The crowded exponent after Comme is primarily read as 4, with 1 and + alternatives retained; no silently repaired Λ¹ is supplied.')
for ident,place,C,F,box,why,conf in [
('045-R01','under first live inclusion in XVIII','deleted superset?','deleted superset?','(792,336,875,395)','A reverse-curved remnant protrudes to the upper left of the heavy live subset; the underlying sign is not fully separable.','low'),
('045-R02','secteur angulaire','secteur | seeteur','secteur','(645,594,795,667)','Second rounded letter has an opening to the right, unlike the closed first e.','high'),
('045-R03','cancelled et before tel que','et?','et','(179,1053,239,1122)','Low initial loop and tall crossed t survive the diagonal cancellation.','high'),
('045-R04','reworked inclusion after ]s,s′[','deleted not-subset? then subset','same','(1200,1124,1263,1185)','A thinner upright survives inside the heavily retraced inclusion. Its original sign remains doubtful.','low'),
('045-R05','boxed deletion after int Λi','not equal empty | equal empty','same','(1384,1104,1472,1177)','Two short horizontals and the pierced ring survive; diagonal hatching prevents certain separation of a negation stroke.','low'),
('045-R06','cela montre que x∈ext Λi','ext','ext','(1031,1223,1099,1287)','Looped e, crossed x and tall t are separately visible despite heavy ink.','high'),
('045-R07','before ]s,s′[ in Cela permet','deleted cap? and dotted minus?','deleted cap? and dotted minus','(856,1327,935,1411)','The point above the dash is separate and definite; two uprights under hatching favor an earlier cap.','medium'),
('045-R08','cancelled ending of relié','r | e','r | e','(1348,1761,1470,1830)','Dense retracing leaves only short diagonal/curved endings; neither candidate is secure.','low'),
('045-R09','inserted il exìste','exìste | existe','same','(225,2068,362,2127)','Long falling, slightly curved mark over i; it could be an elongated i-dot rather than a grave accent.','medium'),
('045-R10','last line exìste','exìste | existe','same','(199,2260,321,2327)','The falling mark over i is longer than an ordinary dot; lexical expectation alone does not settle its status.','medium'),
('045-R11','opening puìsque','puìsque | puisque','same','(1280,88,1445,158)','Short diagonal falling to the right over i; elongated dot and grave remain possible.','medium')]:change(s,ident,place,C,H,F,'Scan 45 crop '+box+': '+why,conf,record_type='crop decision')
for place,rd,alt,conf,why in [
('opening puìsque','puìsque','puisque','medium','Falling i mark may be an elongated dot.'),
('first inclusion in XVIII, underlying sign','deleted superset','','low','Covered by the live subset.'),
('reworked inclusion after ]s,s′[','deleted not-subset','','low','Only a thin internal upright survives distinctly.'),
('boxed deletion after int Λi','≠∅','=∅','low','Diagonal cancellation masks possible negation.'),
('cancelled sign before dotted minus','cap','','low','Two uprights survive under hatching.'),
('ending of relié','deleted r','deleted e','low','Small blackened ending.'),
('Comme Λ exponent','4','1; +','medium','Crossbar favors 4, but the area is retraced.'),
('inserted il exìste','exìste','existe','medium','Long falling mark over i.'),
('last line exìste','exìste','existe','medium','Long falling mark over i.')]:doubt(s,place,rd,alt,conf,reason=why)
for place,rd,why in [
('opening relation [s,s′] … A(Λ¹)','subset','Open right-hand side without a distinct middle arm; retained despite membership being more natural.'),
('last a in par rapport … et a Λ','ā','A shallow horizontal/bowed accent, distinct from the grave on the preceding à.'),
('secteur','secteur','Right-opening c visible in crop.'),
('cancelled et before tel que','et','Loop and tall crossed t remain readable.'),
('empty-set notation','varnothing','Same pierced ring in intersection formulas as the preceding pages.'),
('dotted minus','dotted minus','Separate round point above the dash.'),
('x∈ext Λi','ext','The three letters remain individually traceable.'),
('last XVIII inclusion exponent','1','Straight upper numeral with no curved 2; the mathematically surprising self-exterior claim remains.')]:doubt(s,place,rd,status='resolved',confidence='high',reason=why)
inv(s,[('text','top right','XVII with rules'),('text','top','[s,s′]⊂A(Λ¹)'),('display','upper',']s,s′[⊂R²−Λ¹ (resp. R²−Λ²)'),('text','upper','Lemme XVIII. Λ²−{s,s′}⊂ext Λ¹'),('deletion','XVIII first inclusion','underlying superset?'),('text','upper','Démonstration : Soit Ds'),('deletion','after par rapport a Λ¹','et'),('text','upper-middle','Observons d’abord que le secteur'),('insertion','above exterieur','Ds∩ext Λ in outline'),('display','upper-middle','Ds∩ext Λ⊂Ds∩ext Λ¹ (resp. Ds∩ext Λ²)'),('text','middle','En effet tout point x'),('display','middle','y∉(int Λ¹∪int Λ²∪int Λ)∪(Λ¹∪Λ²∪Λ)'),('deletion','after union expression','puisque'),('text','middle','(on peut toujours trouver un tel y)'),('deletion','before tel que','et'),('deletion','after ]s,s′[','underlying not-subset?'),('deletion','after int Λi','≠∅ / =∅'),('text','middle-lower','Cela permet de prouver que'),('deletion','before dotted minus','cap?'),('insertion','above On montre aussi que','avec le même argument'),('text','lower','Lemme XIX. int Λ¹⊂ext Λ²'),('text','lower','Demonstration : on montre'),('deletion','after relié','r/e'),('insertion','before Dx','il exìste'),('insertion','in Soit, below i/t','en')])
hand('Small overwritten 1-like exponents may acquire a real crossbar','42 final Λ exponent; 45 Comme Λ exponent','These two retraced places remain doubtful; clear 1 elsewhere is not changed','C primary 1 changed to primary 4 with alternatives at both cropped places.')
hand('Marks over i may be stretched into falling strokes','43,45 exìste; 45 puìsque','A local recurring ambiguity, not a rule that every accent is merely a dot','C’s grave/dot alternatives retained where strokes remain ambiguous.')
note(s,"""**Page:** manuscript XVII, archive number 44; Lemmata XVIII and XIX. No date or explicit reservation. H provides only a synopsis.

**045-N1 — Opening contradiction as written.** The continuation writes [s,s′]⊂A(Λ¹), with ⊂ rather than ∈, then claims ]s,s′[⊂R²−Λ¹ (and similarly Λ²). The construction on scan 44 put the whole segment [s,s′] into each Λⁱ. Thus the displayed disjointness is false for its nonempty open segment. **045-N1-refined:** interior visibility gives ]s,s′[⊂R²−Γ for the original polygon Γ; this repairs this specific mismatch of names. It is stated only in these notes.

**045-N2 — Shared segment in XVIII.** The literal lemma removes only {s,s′} from Λ² or Λ¹, retaining the open common chord, which cannot be in the other polygon’s exterior. The subsequent proof removes ]s,s′[, retaining the common endpoints, so its assertion of disjointness from the other polygon is also false. The last supposedly symmetric claim even ends in ext Λ¹ again. **045-N2-refined:** use Λ²−[s,s′]⊂ext Λ¹ and its symmetric version if the intended separation has been established. Removing the closed shared segment eliminates these immediate boundary counterexamples; this run does not certify the full refined separation proof. The several literal brackets, braces and final exponent 1 are retained.

**045-N3 — Exterior path argument.** The upper proof uses an unnamed parent Λ, but also writes Λxy∩Γ=∅. It claims ]s,s′[⊂int Λⁱ, although the segment was made part of Λⁱ itself. This is another boundary/interior conflict. The apparently intended parent-interior statement is ]s,s′[⊂int Γ (or Λ if it denotes Γ); no identification is silently inserted. The step from a path avoiding Λⁱ and meeting its exterior to its whole connected image being in that exterior is valid when interior/exterior are its two complementary components; this conditional step was checked, not the preceding avoidance argument.

**045-N4 — XIX begins.** It asserts disjoint interiors and starts a polygonal-path proof. A chosen boundary point away from the shared segment would allow a small exterior-of-Λ² disk meeting int Λ¹; a path within int Λ¹ then serves if the required boundary separation is already known. The written Λ¹−{s,s′} premise is affected by the same chord problem as XVIII. The first retraced exponent after Comme looks more like 4 than 1, and is marked 4|1|+; the subsequent clear Λ¹ remains unchanged. The proof continues on scan 47, with an intervening sketch sheet.

Accents, dotted minus, cancellations and the two attached insertions are retained; the circled sector formula is an insertion, not a separate mathematical diagram.""")
event('045-N1','refuted, refined statement 045-N1-refined','From the preceding definition, ]s,s′[ is contained in both Λⁱ, so it cannot be contained in either complement. The refined reference is to Γ.')
event('045-N1-refined','used and rechecked in this run','Interior visibility puts the open segment in int Γ and therefore outside Γ; this verifies only the stated reference correction.')
event('045-N2','refuted, refined statement 045-N2-refined','Any interior point of the common segment refutes the lemma with endpoint removal; s or s′ refutes the later disjointness with open-segment removal. Refined statement removes [s,s′] and switches the final exterior index.')
event('045-N3','targeted proof check','A connected path in the complement lies in one of its two components; if its endpoint is exterior, the whole path is exterior. The hypotheses, including avoidance, are required and not established by this check.')
done(s)
