from record import *
t=(ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-05/pages/J71-05_71_scan039.tex').read_text(encoding='utf-8')
for a,b in [
 (r'\mathrm{\unsure{XII}}',r'\mathrm{XII}'),
 (r'\unsure{\varnothing|\phi}',r'\varnothing'),
 (r'\unsure{commun|comun}','commun'),
 (r'\unsure{entraînent|entraîne}',r'\unsure{entraîne|entraînent}'),
 (r'\unsure{g|s}','g'),
 (r'\inserted{\unsure{-}\qquad',r'\inserted{-\qquad'),
 (r"_{s,s'}\unsure{.}-",r"_{s,s'}.-")]:t=t.replace(a,b)
# Match the literal prime spelling in the manuscript transcription.
t=t.replace("D_s\\unsure{-}[s,s']", "D_s\\deleted{\\unsure{-|\\subset}}[s,s']")
(ROOT/'pages/J71-05_71_scan039.tex').write_text(t,encoding='utf-8')
change(39,'039-C1','XIV, subtraction after second D_s',r'\unsure{-}','no source text',r'\deleted{\unsure{-|\subset}}','Several horizontal overstrikes cover a small looped sign; there is no independently legible replacement. Cancellation state restored, with the original glyph still doubtful. Scan 39 crop (540,419,800,526).','low',c=True,kind='deletion state (struck given live or live given struck)',consequential='The dark mark in the second local containment is cancelled; a live subtraction is no longer silently supplied.')
change(39,'039-C2','after La conjonction, struck verb',r'\deleted{\unsure{entraînent|entraîne}}','no source text',r'\deleted{\unsure{entraîne|entraînent}}','The surviving final loop favors e; no terminal t rises above the cancellation. The ending remains obscured. Scan 39 crop (1030,1408,1210,1506).','low',c=True,kind='misread word')
for id,p,c,f,s,co in [
 ('039-R1','manuscript page number','X bis|XI; XII?','X bis|XI; XII','The final X and two tall uprights are distinguishable; earlier loops below remain ambiguous. Scan 39 crop (1430,15,1590,112).','medium'),
 ('039-R2','before et resp.',r'\deleted{\unsure{(}}',r'\deleted{\unsure{(}}','A curved line coincides with the first letter of et; the cancelled matching closing parenthesis supports but does not settle the opening. Scan 39 crop (990,416,1228,532).','low'),
 ('039-R3','first endpoint in global inclusion','g|s','g','Closed upper bowl and lower return hook, unlike the adjacent open s. Scan 39 crop (390,1490,630,1595).','high'),
 ('039-R4','interlinear annotations','Γ²; isolated dash; Γ^{1|2}; point?','Γ²; isolated dash; Γ^{1|2}; point','Two paired upright ditto strokes, clear isolated dash, dark raised digit favoring 1, and distinct low point after the right subscript. Scan 39 crop (430,1560,1300,1704).','medium')]:change(39,id,p,c,'no source text',f,s,co,record_type='crop decision')
for p,r,a,co,why in [
 ('under overwritten XII','X bis','XI','low','Earlier lettering remains entangled; crop 039-R1.'),
 ('XIV dark subtraction',r'\deleted{-}',r'\deleted{\subset}','low','Cancellation certain; underlying sign uncertain; 039-C1.'),
 ('XIV opening parenthesis',r'\deleted{(}','','low','Overlaps et; crop 039-R2.'),
 ('cancelled verb','entraîne','entraînent','low','Final ending heavily struck; 039-C2.'),
 ('right interlinear Γ exponent','1','2','medium','Raised dark glyph has the downstroke of 1; crop 039-R4.')]:doubt(39,p,r,a,co,reason=why)
for p,r,a,why in [
 ('final manuscript page number','XII','','X and two uprights clear on 039-R1.'),
 ('empty intersections',r'\varnothing',r'\phi','Both occurrences conform to the empty-set notation established on 38.'),
 ('en commun','commun','comun','The two m groups are visible in the top half, compared with the opening commun; no crop needed.'),
 ('global endpoint letter','g','s','A closed bowl and lower hook are clear, even though the argument requires s; 039-R3.'),
 ('interlinear dash and dot','- and .','','Both marks are physically distinct in 039-R4; their purpose is not inferred.')]:doubt(39,p,r,a,'high','resolved',why)
notation('Ditto ticks and interlinear alternatives','Two short upright strokes above an inserted expression, not a horizontal equality sign.','39 below the global inclusions','Kept as ditto marks, with the Γ expressions directly under the corresponding Λ expressions.')
hand('A letter can be a genuine slip rather than an ambiguous cursive form.','39 global inclusion: {g,s′}','The closed g differs from all neighboring s forms; this is not a general s-as-g habit.','C already offered g|s. The crop settles g; no mathematical correction to s is made.')
inv(39,[('text','top right','XII over earlier X bis / XI'),('deletion','top right','earlier page number'),('text','top line','On observe que Λ¹ et Λ²'),('insertion','above shared edge',' , savoir,'),('text','upper body','Lemme XIV and four containments'),('deletion','XIV second subtraction','dark overwritten sign'),('deletion','XIV before et','opening parenthesis'),('insertion','above extΛ²','que'),('deletion','end XIV','closing parenthesis'),('text','proof opening','Demonstration : D’aprés le lemme XIII'),('text','middle','Comme Λ¹∩D_s et Λ²∩D_s'),('insertion','left above extΛ¹∩D_s','secteur angulaire'),('display','middle-lower','two interior containments'),('deletion','second interior term','ext'),('text','below display','c.q.f.d.'),('text','lower-middle','La conjonction du lemme XII et du lemme XIII'),('deletion','before montre','entraîne / entraînent'),('display','lower body','two global interior alternatives and exterior consequences'),('insertion','below first inclusion','ditto; Γ²_{s,s′}−{s,s′}'),('insertion','between alternatives','isolated dash'),('insertion','below second inclusion','ditto; Γ^{1|2}_{s,s′}.−{s,s′}'),('text','near foot','Supposons pour fixer les idées'),('text','foot lead-in','On a donc :'),('text','foot lemma','Lemme XV : intΛ²⊂intΛ¹')])
note(39,"""**Content and marks.** Manuscript XII over an earlier number, archive 38. Lemme XIV gives the two local nesting alternatives around s; the proof uses angular sectors and their nonempty exterior intersection. Global containments follow, one case is selected, and Lemme XV asserts `int Λ²⊂int Λ¹`. No date or total count.

**Checks and decisions.** 039-N1: the proof’s use of a common open exterior sector is coherent with the nonempty intersections; the φ-shaped signs are empty sets, as on scan 38. 039-N2: combining a local alternative with XII’s connected-arc argument is the intended local-to-global step. The written reference is XII and **XIII**, although the immediately preceding local-alternative lemma is XIV. This was checked against the ink and retained. 039-N3: the upper global formula genuinely reads `{g,s′}`: the g has a closed bowl and lower hook. It is not regularized to s. The lower interlinear formula reads `{s,s′}`. The dark operation after the second D_s in XIV is cancelled; its former value is not secured, so a mathematically convenient live minus is not supplied.

**Authorial revisions and reservations.** Insertions “, savoir,”, “que”, and “secteur angulaire”; cancelled parentheses, ext changed to int, and the struck verb before “montre”. The interlinear Γ-arcs sit below ditto ticks. “(sans peine)” is the author’s only explicit comment on the ease of a step, not a doubt mark. The glyphs “arète”, “coté”, “definition”, “D’aprés”, “determinés”, “précisement” are kept. The page does not prove XV; its proof starts on scan 40.""")
event('039-N1','used and rechecked in this run','Empty-set notation checked in both nonempty exterior-intersection statements; the angular-sector step was followed but not independently re-proved here.')
event('039-N2','targeted proof check','The local-to-global mechanism requires XII plus the local nesting alternative of XIV. The ink says XIII; this reference discrepancy is retained.')
event('039-N3','used and rechecked in this run','Endpoint role requires s, but the visible g is distinct; this is a recorded textual slip, not a repaired theorem.')
done(39)
