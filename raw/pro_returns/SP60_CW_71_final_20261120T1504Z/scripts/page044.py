from record import *
s=44
src=ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-06/pages/J71-06_71_scan044.tex'
t=src.read_text(encoding='utf-8')
repls=[
(r'\mspage{XVI}',r'\mspage{$\underline{\overline{\mathrm{XVI}}}$}'),
(r'\unsure{\phi|\varnothing}',r'\varnothing'),
(r'\phi',r'\varnothing'),
(r'\Gamma^{\unsure{1|\prime}}',r'\Gamma^{1}'),
(r'\unsure{defnition|definition}',r'\unsure{definition|defnition}'),
(r'\textcircled{\scriptsize\unsure{XIV|XV}}',r'\textcircled{\scriptsize$\underline{\overline{\mathrm{XIV}}}$}'),
(r'\unsure{s}pour',r's$\dot{\mathrm{p}}$our'),
(r'\unsure{conjonction|conjonetion}',r'\unsure{conjonetion|conjonction}'),
(r'\unsure{thēorēme|théorème}',r'thēorēme'),
(r'\unsure{théorēme|théorème}',r'théorēme'),
(r'\deleted{\unsure{s|S}}',r'\deleted{\unsure{S|s}}'),
(r"\unsure{interieur|intérieur}",r'interieur'),
(r"\deleted{\unsure{l'arc|le}}",r"\deleted{l'arc}"),
(r'\deleted{\unsure{f}}',r'\deleted{f}')]
for a,b in repls:
 assert a in t,a
 t=t.replace(a,b)
(ROOT/'pages'/src.name).write_text(t,encoding='utf-8')
H='No source text (editorial synopsis only)'
change(s,'044-C01','manuscript folio','XVI',H,'XVI with upper and lower rules','Halves: separate horizontal rules above and below the numeral.',c=True,kind='omission')
for ident,place,box in [('044-C02','first definition 1','(585,572,770,668)'),('044-C03','second definition 1','(1150,941,1357,1027)')]:
 change(s,ident,place,'defnition | definition',H,'definition | defnition','Scan 44 crop '+box+': an additional undotted minim between f and n favors definition; the cramped junction remains uncertain.','medium',c=True,kind='misread word')
 doubt(s,place,'definition','defnition','medium',reason='Extra minim visible, but f/i/n junction is crowded.')
change(s,'044-C04','circled inserted lemma reference','circled XIV | XV',H,'circled XIV with upper/lower rules','Scan 44 crop (760,1010,868,1097): central upright gives XIV; horizontal rules lie inside the circle.',c=True,kind='omission')
change(s,'044-C05','s before pour','unsure s + pour',H,'s + p with a dot above + our','Scan 44 crop (704,1115,816,1190): small live s overlaps the left side of p; a separate dark point is immediately above the p. The point is retained without assigning meaning.',c=True,kind='omission')
change(s,'044-C06','concluding conjunction','conjonction | conjonetion',H,'conjonetion | conjonction','Scan 44 crop (236,1310,422,1400): the letter before t has a closed upper eye and a lower exit stroke, favoring e rather than open c.','medium',c=True,kind='misread word')
change(s,'044-C07','cancelled symbol before card','deleted s | S',H,'deleted S | s','Scan 44 crop (772,1592,826,1670): broad rounded upper and lower lobes favor capital S; cancellation leaves case uncertain.','medium',c=True,kind='misread symbol or index')
for ident,place,C,F,box,ink,conf in [
('044-R01','J-polygone','J | j | y','J | j | y','(1271,1460,1322,1547)','Looped lower body with upper entry flourish; no separate dot. Jordan notation favors J, but the written outline resembles y.','medium'),
('044-R02','cancelled opening word','Posons?','Posons?','(196,1850,307,1928)','P and successive round lower loops survive the hatching; internal joins are partly hidden.','medium'),
('044-R03','cancelled word before les','égale | égals','égale | égals','(632,1845,740,1934)','Descending g, a bowl and tall l remain visible; final e/s and initial accent intersect hatching.','low'),
('044-R04','les deux arcs','deux | dex','deux | dex','(805,1851,880,1926)','The u/x area is heavily retraced; two stems favor ux, but the older stroke cannot be separated completely.','medium'),
('044-R05','cancelled text after Λ¹',"l’arc | le","l’arc",'(874,2002,984,2077)','Tall initial l, detached apostrophe and space for a-r-c under the cancellation.','high'),
('044-R06','cancelled letter before obtenu','f?','f','(1464,1970,1620,2057)','A tall ascender and a descender loop make f; a diagonal stroke cancels it before the separate o.','high'),
('044-R07','recollement accent','rēcollement | récollement','rēcollement | récollement','(1090,2082,1325,2161)','Short nearly horizontal accent above the first e, with a slight rise; not confidently distinguished from an acute.','medium')]:
 change(s,ident,place,C,H,F,'Scan 44 crop '+box+': '+ink,conf,record_type='crop decision')
for place,rd,alt,conf,why in [
('concluding conjunction','conjonetion','conjonction','medium','Closed eye in letter before t.'),
('J-polygone','J','j; y','medium','Looped cursive form; contextual notation supports J without fully resolving the shape.'),
('cancelled symbol before card','S','s','medium','Case obscured by cancellation.'),
('cancelled opening word','Posons','','medium','Hatching hides internal joins.'),
('cancelled word before les','égale','égals','low','Hatching obscures the ending.'),
('les deux arcs','deux','dex','medium','Retracing over ux.'),
('recollement accent','rēcollement','récollement','medium','Short accent almost horizontal.')]:doubt(s,place,rd,alt,conf,reason=why)
for place,rd,why in [
('empty-set notation','varnothing','Same loop-and-stroke set symbol as the preceding pages; all occurrences are made consistent.'),
('first Γ exponent','1','Upright numeral; paired Γ² and the established arc notation agree with the ink.'),
('circled reference','XIV','Central I is visible between X and V.'),
('before pour','s','Small live s remains before the p; not a cancellation.'),
('theorem 1 conclusion','thēorēme','Both accents are flat in the half image.'),
('section 4 heading','théorēme','First accent rises; second is flat.'),
('visible de l’interieur','interieur','No acute over the first e.'),
('cancelled text after Λ¹',"l’arc",'Initial l, apostrophe and three further letter shapes are visible.'),
('cancelled letter before obtenu','f','Ascender and descender loops survive the diagonal cancellation.')]:doubt(s,place,rd,status='resolved',confidence='high',reason=why)
inv(s,[('text','top right','XVI with rules'),('text','top','Lemme XVII. Si x∈Γ'),('text','upper','Démonstration : D’aprés'),('text','upper-middle','Si x∈Γ¹ss′'),('text','middle','Soit maintenant un disque Ds'),('insertion','middle above lemme','circled XIV with rules'),('display','middle','Ds∩ext Λ¹≠∅ et Ds∩(int Λ¹−int Λ²)≠∅'),('insertion','below left side of display','∩ over V'),('insertion','below right side of display','∩ over U'),('text','middle','ce qui suffit à prouver'),('text','middle-lower','La conjonetion du lemme XVI'),('text','lower','4- Preuve du théorēme 2'),('insertion','section 4 heading above tout Γ','polygone'),('text','lower','On procède par récurrence'),('deletion','before card S(Γ)−2','S/s'),('text','lower','On choisit s,s′∈S(Γ)'),('text','lower','Soient Γ¹ss′ et Γ²ss′'),('deletion','paragraph opening','Posons'),('insertion','above Posons','Soient'),('deletion','before les deux','égale/égals'),('deletion','after Appelons Λ¹',"l’arc"),('deletion','before obtenu','f'),('text','foot','Il est clair que card S(Λ¹)<card S(Γ)'),('insertion','above first S(Λ¹)','card')])
notation('Λ¹, Λ² in section 4','The two polygons formed by joining complementary Γ-arcs to [s,s′]','44–45','New construction using vertices visible from the interior; do not silently import the earlier nested configuration.')
hand('A cramped f-i-n junction can hide the undotted i','44 twice in definition','Both local instances show an extra minim; no universal spelling rule inferred','C’s primary defnition changed to doubtful definition at both places.')
hand('Cursive J can look like y','44 J-polygone','Local ornate loop; compare context, do not replace clear y elsewhere','C doubt retained.')
note(s,"""**Page:** manuscript XVI, archive number 43. Lemme XVII and section “4- Preuve du théorēme 2”. No date. H contains only an editorial synopsis.

**044-N1 — Local incidence with both regions.** Lemme XVII says that each admissible disk centered on Γ meets both U and V. In the Γ¹ case, the manuscript explicitly concludes Dₓ∩V≠∅ twice. The second conclusion follows premises Dₓ⊂ext Λ² and Dₓ∩int Λ¹≠∅, which directly give Dₓ∩U≠∅ with the revised U of scan 42. This checks the missing implication; it does not make the written V claim false, since V is also meant to be met. The repeated V is retained. The disk hypothesis is kept as written, without adding an openness convention.

**044-N2 — Endpoint and completion claims.** The endpoint argument invokes the circled XIV and adds ∩ over V and U beneath the two displayed regions. Those marks are retained as additions, not interpreted as arrows or corrected containments. The page then asserts that XVI and XVII establish theorem 1. These references and the asserted completion were read, not independently re-proved.

**044-N3 — New induction.** Section 4 begins induction on card S(Γ)−2, chooses interior-visible vertices using XI, and forms Λ¹, Λ² by adding [s,s′] to each complementary Γ-arc. XI is outside the supplied excerpt and was not independently checked. The strict cardinality assertions continue on scan 45. The heading actually says “On suppose que tout polygone Γ est un J-polygone”; no more suitable verb was substituted.

The live s before pour, the isolated point above its p, uncertain conjonetion spelling, accents and cancelled words remain diplomatic. The circled XIV is an attention mark; it is not by itself evidence of an authorial question. No explicit reservation is written.""")
event('044-N1','targeted proof check','For any point in Dₓ∩int Λ¹, Dₓ⊂ext Λ² excludes RΛ², so the point lies in U as defined on scan 42. Source repeats V, leaving this U conclusion unstated.')
done(s)
