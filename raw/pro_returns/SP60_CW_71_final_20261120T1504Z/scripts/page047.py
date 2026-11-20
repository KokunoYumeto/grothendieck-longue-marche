from record import *
s=47
src=ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-06/pages/J71-06_71_scan047.tex'
t=src.read_text(encoding='utf-8')
t=t.replace(r'\mspage{XVIII}',r'\mspage{$\overline{\underline{\mathrm{XVIII}}}$}')
t=t.replace(r'\unsure{\phi|\varnothing}',r'\varnothing').replace(r'\phi',r'\varnothing')
for a,b in [(r'\unsure{premiēre|première}','premiēre'),(r'\unsure{c.q.f.d.|c.q.s.d.}','c.q.f.d.'),(r'\unsure{hypothēse|hypothèse}','hypothēse'),(r'\unsure{example|exemple}','example'),(r'\unsure{1|\prime}','1'),(r'\unsure{interieur|intérieur}','interieur'),(r'\unsure{Considerons|Considérons}','Considerons'),(r"\unsure{1'|11}","1'"),(r'\unsure{inferieur|inférieur}','inferieur'),(r'\unsure{mais|Mais}',r'\unsure{Mais|mais}'),(r'\unsure{so what|So what}','so what'),(r'\unsure{…}',r'\ldots')]:
 t=t.replace(a,b)
old=r'\inserted{non consécutifs si $\unsure{p|n}=$ \unsure{nb|nbre} de \unsure{côtés|cotés} de $\Gamma\geq4$,}'
new=r'''\inserted{\tikz[baseline=(ann.base)]{
\node[inner sep=2pt] (ann) {non consécutifs si $p=$ nb de \unsure{cotés|côtés} de $\Gamma\geq4$,};
\draw ([xshift=-2pt]ann.north west) .. controls ([xshift=-6pt]ann.west) and ([xshift=-5pt]ann.south west) .. (ann.south west) -- (ann.south east) .. controls ([xshift=5pt]ann.south east) and ([xshift=5pt]ann.east) .. ([xshift=2pt]ann.north east);
\draw ([xshift=18pt]ann.south west) -- ++(0,-4pt);
}}'''
assert old in t;t=t.replace(old,new)
t=t.replace(r'\inserted{\unsure{interieurs|intérieurs} des}',r'''\inserted{\tikz[baseline=(ins.base)]{\node[inner sep=1pt] (ins) {interieurs};\draw (ins.south west) -- ([xshift=-2pt]ins.south) -- ([yshift=-3pt]ins.south) -- ([xshift=2pt]ins.south) -- (ins.south east);} des}''')
(ROOT/'pages'/src.name).write_text(t,encoding='utf-8')

change(s,'047-C01','manuscript folio','XVIII without rules','not transcribed','$\\overline{\\underline{\\mathrm{XVIII}}}$','Two horizontal rules enclose XVIII at the upper right; seen on whole and top half.',c=True,h=True,kind='omission')
change(s,'047-H01','pencil addition to XX, number of sides','p|n','n','p','Scan 47 crop (820,378,1650,485), rotated −3°: the letter has a long descending stem and a right bowl; the stem continues toward the attachment line. It is p, not n.',h=True,kind='misread symbol or index',consequential='The pencil strengthening uses p for the number of sides, rather than H’s n.')
change(s,'047-C02','pencil addition to XX, cotés','côtés|cotés','côtés (within uncertain nb de côtés)','cotés|côtés','Scan 47 crop (820,378,1650,485): no secure circumflex is visible over o; the small rising mark is nearer e. Preserve the uncertain unmodernized form first.','medium',c=True,h=True,kind='abbreviation expanded or spelling modernised',marked='yes')
change(s,'047-C03','outline and attachment of pencil addition to XX','insertion without outline','opening parenthesis only','three-sided curved enclosure, lower rule and attachment stem','Scan 47 crop (820,378,1650,485): the left curve is continuous with a long lower line which curls upward at the right; a short descending attachment stands under the left part. It is represented as a connected drawn enclosure, not an isolated unmatched parenthesis.',c=True,h=True,kind='drawing or diagram')
change(s,'047-C04','insertion interieurs des, attachment stroke','insertion words only','not transcribed in its lemma locator','interieurs des with lower line and downward attachment notch','Scan 47 crop (820,378,1650,485), lower part: the word interieurs has a line beneath it with a downward notch toward the insertion position after les. The drawing preserves this attachment without assigning an emphatic meaning.',c=True,kind='omission')
change(s,'047-H02','left margin beside bon sommet','tel que? …?',r'\ill{}',r'\unsure{tel que}\ldots','Scan 47 crop (28,743,220,861), rotated −35°: tall t and l, descending q, and faint ue are distinguishable; three small trailing marks support the ellipsis. The words remain moderately uncertain.','medium',h=True,kind=r'readable ink left as \ill{}',marked='yes')
change(s,'047-H03','left margin below the two cases','deleted faux?',r'\ill{}',r'\deleted{\unsure{faux}}','Scan 47 crop (39,1277,147,1394), rotated −30°: a tall f-like stroke, rounded middle and ux-like ending survive under crossing strokes. The reading faux is tentative; deletion is visible.','low',h=True,kind=r'readable ink left as \ill{}',marked='yes')
change(s,'047-C05','before nécessairement','mais|Mais','not transcribed','Mais|mais','Scan 47 crop (1248,1716,1345,1770): the angular initial has a long first upright, about twice the height of a, and a second high peak. Capital M is favored, but overwriting leaves lowercase possible.','medium',c=True,kind='misread word')

ret=[
('047-R01','example','example|exemple','example',(817,895,973,954),'The middle vowel has a closed bowl and a right-hand stem, supporting a.','high'),
('047-R02','two cases, last relation',r'\not\subset',r'\not\subset',(1191,1235,1252,1314),'A curved inclusion sign has two long arms and one crossing vertical stroke; not an extra middle arm of membership.','high'),
('047-R03','overwritten opening bracket',r'\deleted{\unsure{[}}]',r'\deleted{\unsure{[}}]',(225,1363,273,1431),'Live left-facing upper and lower feet form ]; an older short right-facing bottom stroke supports the doubtful earlier [.','medium'),
('047-R04','first visible de s′, interieur','interieur|intérieur','interieur',(1214,1335,1430,1407),'Only the i dots occur above the word; no acute over the first e.','high'),
('047-R05','first new polygon after alors',r"\Lambda^{1'}_{\cdot}|\Lambda^{1!}|\Lambda^{11}_{\cdot}",r"\Lambda^{1'}_{\cdot}|\Lambda^{1!}|\Lambda^{11}_{\cdot}",(1276,1401,1363,1481),'A hooked 1 is followed by a tall separate tick and a detached lower dot. Later occurrences support prime notation, but this local mark still resembles an exclamation point.','medium'),
('047-R06','cancelled token after selon',r'\deleted{\illegible{1}}',r'\deleted{\illegible{1}}',(626,1538,673,1593),'Dense opaque ink covers the token; surviving edge projections do not determine a word.','low'),
('047-R07','lower pencil margin','so what|So what','so what',(22,1945,153,2052),'Rotated −32°: the initial is a small cursive s with a high exit, followed by o; w, tall h and final t are readable.','high'),
('047-R08','final visibility sentence, interieur','interieur|intérieur','interieur',(548,2073,779,2153),'No acute stands over e; the long horizontal spot belongs to the initial i dot.','high')]
for id,p,c,f,b,why,co in ret:
 change(s,id,p,c,'not transcribed, except so what in lower margin',f,f'Scan 47 crop {b}: '+why,co,record_type='crop decision')

for p,r,a,co,why in [
 ('pencil cotés','cotés','côtés','medium','No secure circumflex over o; 047-C02.'),
 ('pencil tel que','tel que','','medium','Faint middle and ending; 047-H02.'),
 ('struck pencil word','faux','','low','Hatched middle of tentative word; 047-H03.'),
 ('overwritten bracket','deleted [','','medium','Older right-facing foot only partly visible; 047-R03.'),
 ('first Λ after alors',r"\Lambda^{1'}_{\cdot}",r'\Lambda^{1!}; \Lambda^{11}_{\cdot}','medium','Separate lower dot and tall tick; later prime notation favors first reading; 047-R05.'),
 ('cancelled token after selon',r'\deleted{\illegible{1}}','','low','Ink is physically obscured; 047-R06.'),
 ('before nécessairement','Mais','mais','medium','High angular initial, overwritten strokes; 047-C05.')]:doubt(s,p,r,a,co,reason=why)
for p,r,a,why in [
 ('all empty-set signs',r'\varnothing',r'\phi','The same oval-and-through-stroke notation in empty intersections throughout these scans.'),
 ('opening','premiēre','première','Nearly horizontal accent; top half.'),
 ('proof end','c.q.f.d.','c.q.s.d.','Third letter has the tall loop of f; top half.'),
 ('pencil side count','p','n','Long descender and bowl; 047-H01.'),
 ('pencil abbreviation','nb','nbre','Only n and b precede de; annotation crop.'),
 ('inserted qualifier','interieurs','intérieurs','No e accent; annotation crop.'),
 ('proof opening','hypothēse','hypothèse','Flat accent; top half.'),
 ('margin trailing marks',r'\ldots','uncertain ellipsis','Three small marks; tel que crop.'),
 ('example','example','exemple','Closed a bowl with a right stem; 047-R01.'),
 ('disk argument Γ superscript','1','prime','Hooked numeral, consistent with the first cut arc; top half.'),
 ('visibility, both places','interieur','intérieur','No acute over e in either crop; 047-R04 and R08.'),
 ('construction opening','Considerons','Considérons','No acute over e; bottom half.'),
 ('later Λ superscripts',"1'",'11','Hooked 1 followed by a separate shorter prime; the same construction is repeated.'),
 ('cardinal comparison','inferieur','inférieur','No acute above first e; bottom half.'),
 ('lower pencil margin','so what','So what','Small initial cursive s; 047-R07.')]:doubt(s,p,r,a,'high','resolved',why)

body=[
 ('completion of XIX','mais Λ_zy∩]s,s′[=∅ ... c.q.f.d.','Five lines finish the preceding proof, including the retained exterior inclusion and Λ¹/Λ² interchange.'),
 ('unquoted parts of XX','Lemme XX ... interieurs des triangles corespondants soient contenus dans intΓ','Ruled XX, live statement, struck au moins, and the separate inserted qualifier; H quotes a short locator but does not transcribe the full statement.'),
 ('induction argument and disk parenthesis','Démonstration : L’hypothēse ... def.1 ... etc)','The two t_i choices and disk argument are fully written; H supplies only the bon sommet locator.'),
 ('two-case argument beyond H locators','Dans le cas contraire ... puisque ]s″,s′[⊄Γ','The prose, two alternatives and final justification are present; the first s″ is circled. H quotes partial locators only.'),
 ('polygon reconstruction beyond H locator','Si ]s″,s′[∩Γ=∅ ... réliant s à s′ ... A(Γ)','The paragraph includes the visibility claim, deleted bracket and blackened token, and mismatched arc endpoints; H quotes only the beginning of the gluing clause.'),
 ('cardinality sentence beyond H locators','Mais nécessairement ... au cardinal ... Λ¹ ... A(Γ)','The full strict comparison is written between the two pencil questions; H quotes only portions as locators.'),
 ('last paragraph','Si ]s″,s′[∩S(Γ)≠∅ ... de s=t ... a) ...; b)','Four lines end at the live b); the circle above triangle denotes its interior. H gives no source transcription of this paragraph.')]
for i,(p,f,why) in enumerate(body,1):
 change(s,f'047-HB{i:02}',p,f,'not transcribed beyond editorial quotation locators',f,why+' Read on the supplied halves; no additional crop needed.',h=True,kind='omission')

inv(s,[
 ('text','top right','XVIII between rules'),('text','top body','mais Λ_zy∩]s,s′[=∅'),
 ('text','upper body','Lemme XX. Il y’a deux bons sommets'),('insertion','above XX after Γ','non consécutifs si p=nb de cotés de Γ≥4, with outline and leader'),
 ('deletion','XX before tels que','au moins'),('insertion','XX after les','interieurs des, lower attachment line'),
 ('text','upper-middle','Démonstration : L’hypothēse de récurrence'),('margin note','left of bon sommet','tel que…'),
 ('text','middle, parenthesis','tout point de intΛ¹ peut être relié'),('text','middle','Dans le cas contraire sans perte de généralité'),
 ('margin note','left of Deux cas','?'),('insertion','first two-case formula','circle around first s″'),
 ('margin note','left below two cases','deleted faux?'),('deletion','same pencil marginal word','faux?'),
 ('text','middle-lower','Si ]s″,s′[∩Γ=∅ il est clair'),('deletion','opening interval bracket of that paragraph','earlier [? beneath ]'),
 ('margin note','left of obtenu en récollant','!'),('deletion','after selon','blackened illegible token'),
 ('text','lower body, continuing reconstruction','Il est clair que S(Λ¹′)⊂S(Γ)'),
 ('margin note','left of cardinal comparison','?'),('margin note','left of au cardinal','so what'),
 ('text','bottom body','Si ]s″,s′[∩S(Γ)≠∅ on choisit z'),('insertion','after visible, final paragraph','de s=t'),
 ('insertion','above triangle, last paragraph','small circle denoting interior')])
notation('p in the pencil lemma addition','p = nb de cotés de Γ; p has a descender, unlike n','47, XX','C’s p/n doubt resolved; H’s n is changed to p. This variable is in the annotator’s hand.')
notation(r"\Lambda^{1'}",'Hooked numeral 1 followed by a vertical prime, for the new polygon','47, construction and later repetitions','The first occurrence has a separate dot below the prime; it remains locally doubtful between prime-plus-dot and exclamation point.')
hand('Pencil p has a long descender which can run into the attachment line.','47, non consécutifs annotation','One occurrence here; not generalized to the main writer.','H reads n; C’s p/n uncertainty is resolved as p.')
hand('The main writer’s primes may be tall and vertical; 1 has a leftward hook.','47, new polygon notation','Later occurrences clearly distinguish 1 and prime; first occurrence also has a detached low dot.','C’s 1′/11 uncertainty is resolved except at the first dotted occurrence.')
note(s,"""**Sheet and content:** manuscript XVIII between rules; archive number 46. The page completes XIX and gives XX, asserting two good vertices whose corresponding triangles lie inside Γ. Pencil adds “non consécutifs si p = nb de cotés de Γ ≥4,” and “interieurs des”. The outline of the first addition and the attachment line under the second are preserved. The proof chooses t₁ and t₂ in the cut polygons, then discusses a replacement polygon Λ¹′ and a strict reduction of its Γ-edges. It ends at b), continued on scan 48. No date appears here.

**047-N1, induction and annotation.** A limited combinatorial implication was checked: if a cut polygon with at least four vertices has two nonconsecutive good vertices, the two adjacent cut endpoints s,s′ cannot be the entire good-vertex pair. In a nondegenerate triangle all three corners provide the triangle itself, so an endpoint-free choice is also available under the stated good-triangle condition. This explains the force of the pencil strengthening; it is conditional on that stronger induction statement, not a proof that the manuscript establishes it. The ink p, with a descender, replaces H’s n.

**047-N2, boundary obstruction.** The opening again uses Λ²−{s,s′}⊂extΛ¹, the inclusion questioned in 045-N2: it still contains the shared open chord. The later phrase “le triangle de sommets s,s′,s″ ⊂ intΓ” likewise fails literally for a closed triangle whose listed vertices lie on Γ. Refinement 047-N2-R is the triangle’s interior being contained in intΓ; that removes the immediate boundary obstruction, but is not proved here. The final paragraph explicitly uses a circle over triangle. These distinctions were retained, not homogenized.

**047-N3, construction endpoints.** The gluing set is {s′,s″}, while the arc is written “réliant s à s′”; the first s is visibly unprimed. Those endpoints do not match the proposed joining segment [s′,s″]. Replacing that first s by s″ would address the endpoint mismatch (047-N3-R), but it is not the transcription and does not by itself prove all the construction’s properties. The subsequent strict cardinality claim remains unchecked.

**Reservations and limits.** The pencil gives “tel que…” beside the underlined “bon sommet”, ? beside “Deux cas”, a circle around the first s″, tentative struck “faux”, ! beside the gluing, ? beside the cardinal comparison, and “so what” beside its conclusion. The two-case paragraph does not introduce s″ locally. The implication from a chord meeting Γ to its meeting S(Γ) needs the local ear-triangle geometry; it is not refuted merely by a generic transverse crossing, nor verified here. The first Λ¹′ has a low detached dot and remains locally doubtful; later prime forms are clear. The bottom insertion says “de s=t”, with no visible index on t. Unnumbered Λ in the disk argument, example, Considerons, réliant, arètes, inferieur and the unaccented interieur forms stand as written. The blackened token after selon remains physically unreadable.

H’s body quotations are locators for its marginal transcriptions, rather than a continuous text. Its coverage omissions are counted separately in meaning from incorrect attempted readings; its synopsis is excluded. The main ink and the pencil annotations have visibly different styles, with identities unverified.""")
event('047-N1','targeted proof check','Conditional combinatorial step: a nonconsecutive pair cannot consist of the adjacent cut endpoints; the triangle case supplies a third vertex. The strengthened induction hypothesis is not established by this check.')
event('047-N2 / opening XIX','used and rechecked in this run','The common open chord still lies in Λ²−{s,s′}, so the exterior inclusion has the obstruction recorded in 045-N2.')
event('047-N2 / closed-triangle inclusion','refuted, with refined statement id','Boundary vertices of Γ cannot lie in intΓ. Refinement 047-N2-R replaces the closed triangle by its interior; removal of this immediate obstruction is checked, not the full refined containment.')
event('047-N3 / gluing endpoints','targeted proof check','The printed-in-ink endpoints s,s′ do not equal the declared joining pair s′,s″ for distinct vertices. Refinement 047-N3-R changes s to s″; this repairs endpoint matching only.')
done(s)
