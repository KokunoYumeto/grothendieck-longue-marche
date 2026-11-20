from record import *
s=48
src=ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-06/pages/J71-06_71_scan048.tex'
t=src.read_text(encoding='utf-8')
t=t.replace(r'\mspage{XIX}',r'\mspage{$\overline{\underline{\mathrm{XIX}}}$}')
t=t.replace(r'tou\deleted{\unsure{s}}\unsure{tes|ts}',r'tou\deleted{s}tes')
for a,b in [(r"\unsure{1'|11}","1'"),(r"\unsure{n'ya|n'y a}","n'ya"),(r'\unsure{récurrence|récurence}','récurrence'),(r'\unsure{foçon|façon}','foçon'),(r'\unsure{evidente|évidente}','evidente'),(r'\unsure{\Lambda|A}',r'\Lambda'),(r'\unsure{c.q.f.d.|c.q.s.d.}','c.q.f.d.'),(r'\unsure{interieur|intérieur}','interieur'),(r"\unsure{qu il|qu'il}",'qu il'),(r'\unsure{exterieur|extérieur}','exterieur'),(r'\unsure{précedent|précédent}','précedent'),(r'\unsure{corespondent|corespondant}','corespondent'),(r'\unsure{juillet|jullet}','juillet')]:t=t.replace(a,b)
t=t.replace(r'\deleted{\unsure{A|R}}',r'\deleted{\unsure{R|A}}',1)
old=r'\inserted{appliqué $n$ fois\unsure{,|.} Le même argument avec $\Lambda^2$ prouve le reste,}'
new=r'''\inserted{\tikz[baseline=(a.base)]{
\node[inner sep=1pt] (a) {appliqué $n$ fois Le même argument avec $\Lambda^2$};
\node[anchor=west,inner sep=1pt] (b) at ([xshift=120pt,yshift=-11pt]a.south west) {prouve le reste,};
\draw ([xshift=-4pt,yshift=-4pt]a.south west) -- (a.south west) -- ([xshift=115pt]a.south west) .. controls ([xshift=130pt,yshift=1pt]a.south west) and ([xshift=-8pt,yshift=7pt]b.south west) .. (b.south west) -- ([xshift=10pt]b.south east);
}}'''
assert old in t;t=t.replace(old,new)
old=r'\margin{\unsure{faux}, \unsure{si on} \unsure{ne choisit} \unsure{pas bien} \unsure{ses|s.} \unsure{notations|solutions} \unsure{--|…}}'
new=r'''\margin{\tikz[baseline=(m.base)]{\node[align=left,inner sep=1pt] (m) {faux, si on\\ne choisit\\pas bien\\\unsure{s.|ses} \unsure{notations|solutions} \unsure{--|…}};\draw ([xshift=2pt]m.north east) -- ([xshift=-5pt]m.south east);}}'''
assert old in t;t=t.replace(old,new)
(ROOT/'pages'/src.name).write_text(t,encoding='utf-8')

change(s,'048-C01','manuscript folio','XIX without rules','not transcribed','XIX between upper and lower rules','Two oblique horizontal rules enclose the upper-right folio. Seen on whole and top half.',c=True,h=True,kind='omission')
change(s,'048-C02','cancelled letter before first A(Γ)','deleted A|R','not transcribed','deleted R|A','Scan 48 crop (147,149,197,201): a right-hand upper bowl and a downward diagonal leg favor R beneath the hatching; A remains possible.','low',c=True,kind='misread symbol or index')
change(s,'048-C03','insertion after second XIX, punctuation after fois','comma|period','not transcribed','no separate punctuation before Le','Scan 48 crop (976,876,1630,984): the descending last stroke of s meets the lower attachment rule and the following L. There is no distinct comma or full stop between the words.','medium',c=True,kind='text not on the page')
change(s,'048-C04','insertion after second XIX, connecting line','words of insertion only','not transcribed','two-line insertion with bent lower connecting rule','Scan 48 crop (976,876,1630,984): a lower rule starts beside XIX, runs beneath the first part, bends down-left, then continues under prouve le reste. This is an attachment outline, not a cancellation.',c=True,kind='omission')
change(s,'048-C05','long pencil margin, last line first group','ses|s.',r'\ill{}','s.|ses','Scan 48 crop (15,1390,173,1745), rotated −46°: a single compressed s-like trace followed by a detached dot is visible. The expanded ses reading is less well supported.','low',c=True,h=True,kind=r'readable ink left as \ill{}',marked='yes')
change(s,'048-H01','long pencil margin, before choisit','ne choisit?',r'\ill{} \uncertain{choisit}','ne choisit','Scan 48 crop (15,1390,173,1745), rotated −46°: two low humps of ne precede c, tall h, rounded o, two i marks and final t. The negative particle is recoverable.','medium',h=True,kind=r'readable ink left as \ill{}',marked='yes')
change(s,'048-H02','long pencil margin, third line','pas bien?',r'\ill{}','pas bien','Scan 48 crop (15,1390,173,1745): descending p, a small round a and final s precede the tall b and ien ending.','medium',h=True,kind=r'readable ink left as \ill{}',marked='yes')
change(s,'048-H03','long pencil margin, last word','notations|solutions',r'\ill{}','notations|solutions','Scan 48 crop (15,1390,173,1745): tall central strokes and a compressed ending support notations, but the pale opening and joins do not exclude solutions. The uncertain partial recovery is retained.','low',h=True,kind=r'readable ink left as \ill{}',marked='yes')
change(s,'048-H04','long pencil margin, trailing marks','--|…','not transcribed','--|…','Scan 48 crop (15,1390,173,1745): two pale short marks lie beyond the last word; dash-like form favored, exact punctuation unresolved.','low',h=True,kind='omission')
change(s,'048-C06','long pencil margin, side stroke','no side stroke','no side stroke','long oblique side stroke','Scan 48 crop (15,1390,173,1745): one long straight stroke runs alongside the comment and toward the adjacent assertion, crossing its far-right letter strokes incidentally. It is retained as a drawn attachment/side mark.',c=True,h=True,kind='omission')
change(s,'048-H05','lower underlined pencil word','douteux|donc ?',r'\ill{}','douteux|donc ? (underlined)','Scan 48 crop (17,1852,180,1980), rotated −31°: a looped d, low ou-like middle, tall t-like stroke and compressed final marks favor douteux. The ending is too faint for certainty; the long underline is clear.','medium',h=True,kind=r'readable ink left as \ill{}',marked='yes')

ret=[
 ('048-R01','opening correction','tou[deleted s?]tes|ts','tou[deleted s]tes',(130,61,239,120),'The old s remains below a long replacement t; the following e loop and final s are distinct.','high'),
 ('048-R02','cancelled fragment and following dot','so|sa; dot?','same',(297,70,377,115),'Two loops survive crossing strokes, with a distinct detached dot to the right; its textual function is uncertain.','low'),
 ('048-R03','struck bien','bien?','same',(1427,247,1513,296),'Tall b loop and i dot survive; en is partly buried under the horizontal cancellation.','medium'),
 ('048-R04','cancelled letter before Λ¹⁽ⁿ⁾','A|R','same',(620,356,677,411),'Oblique legs converge above; horizontal hatching obscures any original bar or upper bowl.','low'),
 ('048-R05','récurrence','récurrence|récurence','récurrence',(1199,336,1368,397),'Two separate short r shoulders follow u before the e loop.','high'),
 ('048-R06','foçon','foçon|façon','foçon',(1384,332,1485,394),'The first vowel is a closed isolated oval without an a downstroke, matching the earlier foçon form.','high'),
 ('048-R07','b), letter inside A(...)','Λ|A','Λ',(852,668,907,737),'The two legs have no internal crossbar; the extra stroke lies across the apex and outside the right leg.','high'),
 ('048-R08','exìste','exìste|existe','same',(981,1235,1073,1293),'The i mark is long, downward-curving to the right; an unusually dragged dot remains possible.','medium'),
 ('048-R09','exterieur','exterieur|extérieur','exterieur',(772,1320,950,1395),'No detached accent occurs above either e; the dot belongs to i.','high'),
 ('048-R10','first numèro','numèro|numéro|numero','same',(206,1422,350,1485),'A short upright mark leans downward-right above e; the direction is not completely secure.','medium'),
 ('048-R11','cancelled prefix before -relativement','co|lo','same',(278,1590,324,1647),'Two low lobes remain, with tall intersecting hatching on the left; neither first-letter candidate is secured.','low'),
 ('048-R12','précedent','précedent|précédent','précedent',(1257,1532,1437,1605),'One acute stands over the first e; none appears over the second.','high'),
 ('048-R13','cancelled partial word before bon sommet','trian|triang','same',(953,1632,1062,1693),'Tall initial t, i dot and low joined ending remain under the strike; a terminal g cannot be securely isolated.','low'),
 ('048-R14','corespondent','corespondent|corespondant','corespondent',(367,1737,645,1809),'The vowel after d is an open e-like loop, unlike the a in the preceding lemma statement.','high'),
 ('048-R15','overwritten opening of conclusion','deleted Le|Les; live Le|Lee','same',(151,1931,240,1999),'Overlapping large L loops and a circled/overworked small loop precede a separate e. Which old strokes belong to the discarded word remains uncertain.','low'),
 ('048-R16','montent','montent|montrent','same',(1136,1957,1307,2020),'The tall t joins almost directly to e; a compressed r could share that joining stroke. Do not insert r from grammar.','medium'),
 ('048-R17','month in date','juillet|jullet','juillet',(1114,2070,1250,2155),'A short additional upright occurs between the u strokes and the first of the two l loops. Dots are faint, but the i stroke is present.','high'),
 ('048-R18','signature','Mauré|Mouré|Maury|Maurice','same',(1166,2140,1366,2240),'Long M, overlapping small oval and stem, joined u/r-like strokes, e-like terminal loop and raised accent/flourish. The name cannot be securely identified.','low')]
for id,p,c,f,b,why,co in ret:change(s,id,p,c,'not transcribed as continuous source text',f,f'Scan 48 crop {b}: '+why,co,record_type='crop decision')

for p,r,a,co,why in [
 ('cancelled opening fragment','so','sa','low','Two heavily crossed loops; 048-R02.'),('dot after cancelled fragment','.','','low','Distinct spot, unclear whether punctuation; 048-R02.'),
 ('cancelled letter before first A(Γ)','R','A','low','Bowl and diagonal leg; 048-C02.'),('cancelled bien','bien','','medium','Ending buried beneath strike; 048-R03.'),
 ('cancelled letter before Λ¹⁽ⁿ⁾','A','R','low','Dense hatching; 048-R04.'),('exìste','exìste','existe','medium','Long grave-like i mark; 048-R08.'),
 ('first numèro','numèro','numéro; numero','medium','Short ambiguous-direction accent; 048-R10.'),('pencil final-line opening','s.','ses','low','Compressed trace plus dot; 048-C05.'),
 ('pencil final word','notations','solutions','low','Pale compressed handwriting; 048-H03.'),('pencil trailing marks','--','…','low','Two small pale marks; 048-H04.'),
 ('cancelled prefix before -relativement','co','lo','low','Hatched loops; 048-R11.'),('cancelled trian','trian','triang','low','Ending obscured; 048-R13.'),
 ('underlined pencil word','douteux','donc ?','medium','D, ou-like middle and tall t; ending pale; 048-H05.'),('cancelled opening of conclusion','Le','Les','low','Overlapping earlier loops; 048-R15.'),
 ('live opening of conclusion','Le','Lee','low','Extra e-like loop may belong to discarded word; 048-R15.'),('concluding verb','montent','montrent','medium','No independently formed r; 048-R16.'),
 ('signature','Mauré','Mouré; Maury; Maurice','low','Flourished joined letters do not establish a name; 048-R18.')]:doubt(s,p,r,a,co,reason=why)
for p,r,a,why in [
 ('opening correction','tou[deleted s]tes','uncertain s; tes/ts','Old s and live tes are separable; 048-R01.'),
 ('opening Λ superscript',"1'",'11','Hooked 1 plus short separate prime; same notation as scan 47.'),
 ('Comme il n’ya',"n'ya","n'y a",'y and a are joined without a word-sized gap on top half.'),
 ('récurrence','récurrence','récurence','Two r shoulders; 048-R05.'),('foçon','foçon','façon','Round isolated first vowel; 048-R06.'),
 ('parenthetic adjective','evidente','évidente','No acute over initial e, top half.'),('b), nested polygon','Λ','A','No crossbar between legs; 048-R07.'),
 ('first proof ending','c.q.f.d.','c.q.s.d.','Tall third-letter loop matches the final proof ending.'),
 ('XXI insertion','interieur','intérieur','No e accent visible, top and overlapping bottom halves.'),('Demonstration clause','qu il',"qu'il",'No apostrophe between groups, bottom half.'),
 ('exterieur','exterieur','extérieur','No detached acute, 048-R09.'),('long pencil beginning','faux, si on','doubt marks','f, final x, s/i and o/n groups are distinguishable in rotated crop.'),
 ('long pencil second line','ne choisit','doubt marks','Low ne and tall h/t with two i marks, rotated crop; 048-H01.'),('long pencil third line','pas bien','doubt marks','p and b start the groups; 048-H02.'),
 ('précedent','précedent','précédent','Only first e carries an acute; 048-R12.'),('corespondent','corespondent','corespondant','e loop after d; 048-R14.'),
 ('month','juillet','jullet','Additional short upright before double l; 048-R17.')]:doubt(s,p,r,a,'high' if p not in ('long pencil second line','long pencil third line') else 'medium','resolved',why)

body=[
 ('continuation of XX, opening','toutes les [deleted so?] .? arêtes ... A(Λ¹′)∩A(Γ)<A(Γ)∩A(Λ¹)','Two lines preserve the corrected opening word, le cardinal de vérifie, and strict comparison of written set expressions.'),
 ('finite descent and case a)','Comme il n’ya ... a) Il existe n ... appliqué n-fois,','Five lines include struck bien, iterated superscript 1(n), inserted bon and arêtes Γ without de. The pencil ou bien, is separately transcribed by H and agrees.'),
 ('case b) beyond H locator','b) ... donc card A¹⁽ⁿ⁾=3 ... c.q.f.d.','The continuation after H’s short cardinality locator, inserted seul, and the added sentence about Λ² are written.'),
 ('Lemme XXI','Si Γ est un polygone non-convexe ... le interieur du triangle corespondant ... extΓ','Ruled lemma number and underlined heading, with the insertion interieur du, are present.'),
 ('XXI demonstration beyond H locators','Demonstration : le lemme VIII ... ce qui permet de prouver le lemme.','Seven lines preserve the two Λ labels, V formula, substitutions, cancellations, unaccented a and corespondent; H gives partial locators only.'),
 ('conclusion','Le lemme XX le lemme XXI ... montent|montrent le théorème 2, c.q.f.d.','Two lines conclude the memoir; the overwritten opening and doubtful verb are preserved.'),
 ('dated closing and signature','le 15 juillet 1976, Montpellier; Mauré|Mouré|Maury|Maurice.','Date, place and a signed name occur at lower right. H mentions them only inside its editorial note; the signature remains uncertain.')]
for i,(p,f,why) in enumerate(body,1):change(s,f'048-HB{i:02}',p,f,'not transcribed beyond editorial quotation locators',f,why+' Read on the supplied halves; individual uncertain places have the crops listed above.',h=True,kind='omission')

inv(s,[('text','top right','XIX between rules'),('text','top body','toutes les arêtes de Λ¹′'),('deletion','first word','old s beneath t'),('deletion','before arêtes','so|sa'),
 ('deletion','before A(Γ), second line','R|A'),('text','upper body','Comme il n’ya qu’un nombre fini'),('deletion','before a :','bien'),
 ('text','upper body','a) Il existe n tel que'),('deletion','before Λ¹⁽ⁿ⁾','A|R'),('insertion','a) before sommet','bon'),
 ('insertion','left between a) and b)','ou bien,'),('text','upper-middle','b) il existe n tel que card'),('insertion','b) before sommet','seul'),
 ('insertion','above end of b), after XIX','appliqué n fois Le même argument avec Λ² prouve le reste, and bent attachment rule'),
 ('text','middle','Lemme XXI : Si Γ est un polygone non-convexe'),('insertion','XXI before triangle','interieur du'),
 ('text','middle-lower','Demonstration : le lemme VIII montre'),('margin note','left beside intΛ²⊂extΓ','faux, si on ne choisit pas bien s.|ses notations|solutions --|…'),
 ('margin note','right edge of same pencil annotation','long slanted side/attachment stroke'),('deletion','non ... -relativement','co|lo'),
 ('deletion','before lemme précedent','L’argument du'),('insertion','same place above deletion','Le'),('deletion','before bon sommet','trian|triang'),
 ('margin note','left beside s appartient','underlined douteux|donc ?'),('text','bottom body','Le lemme XX le lemme XXI'),('deletion','overwritten conclusion opening','Le|Les'),
 ('text','lower right','le 15 juillet 1976, Montpellier'),('text','below date','signature Mauré|Mouré|Maury|Maurice.')])
notation(r'\Lambda^{1(n)}','Entire 1(n) is superscripted for the iteration; A(Γ) denotes the edge set','48, a) and b)','Keep the separate literal card A^{1(n)}=3, whose A has a visible crossbar; do not replace it by Λ or A(Λ).')
hand('A dot above i may be dragged into a grave-like curved stroke.','45 exìste (twice); 48 exìste','Variable: ordinary dots also occur. Preserve local ambiguity; this is not a general accent normalization rule.','C’s doubtful exìste retained at these places.')
hand('Compressed pencil abbreviations may end in a detached point.','48, last line of faux comment','Single occurrence, tentatively s.; no identity attributed to the pencil writer.','C’s ses|s. is reordered to s.|ses; H leaves it illegible.')
note(s,"""**Sheet and content:** manuscript XIX, archive 47; closes the memoir with “le 15 juillet 1976, Montpellier” and an uncertain signature (Mauré / Mouré / Maury / Maurice). No total-page declaration. The page completes XX by a finite descent on original edges, proves XXI about an exterior good triangle for a nonconvex polygon, and invokes XX–XXI plus the stated convex-polygon fact to conclude theorem 2. The signature does not securely identify the writer.

**048-N1, finite descent.** The elementary termination step was checked conditionally: an integer k counting original edges cannot decrease strictly indefinitely. If every replacement polygon has all but one edge original and has at least three edges, k≥2, and k=2 forces three edges. This validates the numerical implication under those construction hypotheses; the preceding replacement construction and its asserted strict decrease remain unproved. The opening actually compares the written edge sets with < and says “le cardinal de vérifie”; no cardinal operators or missing words are supplied. The later formula is literally card A¹⁽ⁿ⁾=3, with a barred A, although nearby polygon letters are Λ. The first b) letter inside A(...) is Λ, resolved from its open interior.

**048-N2, the choice of labels in XXI.** The pencil warning about notations has mathematical force. A direct example checks the need to choose the labels: take Γ with successive vertices (0,0),(2,0),(2,2),(1,1),(0,2), and the exterior chord from (2,2) to (0,2). The two closed curves cut off are the outer rectangle and the notch triangle. If Λ² labels the rectangle, (1,1/2) is in intΛ² and intΓ, contradicting intΛ²⊂extΓ. Refinement 048-N2-R chooses Λ² as the notch triangle, whose interior lies above the two notch edges and outside Γ; the local containment then holds in this example. This is a counterexample to an unlabeled/general assertion, not a re-proof of XXI. Non-relative-compactness of V follows from its including extΛ¹, but alone does not establish that V is a component of the complement of Γ. The lower reuse of the preceding lemma to obtain a suitable original-edge vertex is marked “douteux” in pencil and is not certified here.

**Interventions and fidelity.** Pencil “ou bien,” attaches between a) and b). The longer margin reads “faux, si on ne choisit pas bien s.|ses notations|solutions --|…” with its last line still uncertain; its side stroke is retained. The lower underlined word is most plausibly “douteux”. The main hand inserts bon, seul, the sentence about applying XIX n times and Λ², and interieur du; it replaces “L’argument du” with “Le” and cancels a partial trian/triang before bon sommet. No independent punctuation is visible between fois and Le in the long insertion. The conclusion’s overworked Le, the montent/montrent reading, two cancelled capital letters and the signature remain doubtful. The closed-triangle wording in the proof differs from the inserted interior qualifier in XXI and is not silently repaired. H’s body synopsis is editorial; its source marginals and short quotation locators are distinguished from its untranscribed coverage.""")
event('048-N1','targeted proof check','Conditional integer descent and edge count checked: k decreases, k≥2, and one nonoriginal edge gives total k+1, hence 3 at k=2. No certification of the replacement construction.')
event('048-N2','refuted, with refined statement id','Concrete notched pentagon and exterior chord: labeling the outer rectangle Λ² makes (1,1/2) an interior point of both Λ² and Γ. Refinement 048-N2-R labels the notch triangle Λ²; its interior is outside Γ in the example.')
event('048-N2 / unbounded V','targeted proof check','V contains extΛ¹, hence is unbounded for a compact polygon Λ¹. This fact alone gives neither disjointness from Γ nor the asserted component identification.')
done(s)
