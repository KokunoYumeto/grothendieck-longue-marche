from reading_support import *
save_tex(24,r'''\scanpage{24}
contour

\uline{Exos} (DEA) Soit $G=Z.\Gamma$ produit $1/2$ direct de $\deleted{\unsure{I|\Gamma}}Z$ et $\deleted{Z}\Gamma$ ($\Gamma$ opère sur $Z$). Montrer que la \unsure{donnée|donné} d'un torseur \inserted{$T$} sous $G$ équivaut \unsure{:|à} celle de

a) d'un torseur $\omega$ sous $\Gamma$

b) d'un torseur $T_0$ sous $\,{}^\omega Z=\omega\wedge_\Gamma Z$

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.48pt,line cap=round] (0,0) .. controls (.48,-.65) and (1.35,-1.84) .. (2.08,-2.48);
\end{tikzpicture}}
% archive sheet number: 23
''')
doubts(24,[('old letter under first Z','I','Gamma','low','Crop (211,258,458,330): upright and horizontal strokes are shared by overwritten forms; old I versus Gamma cannot be separated.'),('Montrer que la ...','donnée','donné','medium','Crop (1480,303,1640,363): the closing e-like strokes are small and detached; final extra e remains doubtful.'),('before celle de',':','à','medium','Crop (1234,400,1280,459): two detached marks, the lower slightly elongated; colon is the closer literal outline, although an extremely reduced à is possible.')])
changes(24,[
('continuation at top','contour','contour.','contour','Left half: word ends with a rising terminal stroke; no separate period.','high',False,True,'other','no',10,''),
('exercise heading','Exos | Exo, underlined','Exer, italic','Exos, underlined','Crop scan 024 (227,140,356,217): Ex followed by a round o and short descending s; separate underline.','high',False,True,'misread word','no',8,''),
('product description','1/2 direct','½-direct','1/2 direct','Right half: diagonal fraction followed directly by direct; no separate hyphen.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('overwritten pair after de','deleted I | Gamma then Z; deleted Z | I then Gamma','uncertain Z and Gamma, surcharge noted','deleted I | Gamma then Z; deleted Z then Gamma','Crop scan 024 (211,258,458,330): distinct earlier upright in the first Z; second has an earlier diagonal Z under the live Gamma. H describes the surcharge but does not record its readable earlier letters.','low',False,True,'omission','yes',7,''),
('parenthetical action','Gamma opérant sur Z','Gamma opère sur Z','Gamma opère sur Z','Crop scan 024 (574,284,718,341): accented e after p, a low r continuation and final loop e; no ant ending.','high',True,False,'misread word','no',2,''),
('stop after action parenthesis','no stop','period','period','Halves: a detached baseline dot after the closing parenthesis.','high',True,False,'omission','no',3,''),
('before celle de','à | colon','à','colon | à','Crop scan 024 (1234,400,1280,459): two detached points; lower mark is longer but has no secure a loop.','medium',True,True,'misread word','no',2,''),
('lower free stroke','TikZ descending curved stroke','omitted','descending curved stroke, no arrowhead','Whole and halves: a single thin stroke curves down and right in otherwise blank lower space, unattached to the exercise.','high',False,True,'drawing or diagram','no',4,'')])
inventory(24,[('text','top continuation','contour'),('text','exercise','Exos (DEA) Soit G=Z.Γ ... celle de'),('deletion','first factor name after de','old I/Gamma'),('deletion','second factor name after et','old Z'),('insertion','above torseur','T'),('text','item a','d’un torseur ω sous Γ'),('text','item b','d’un torseur T_0 sous omega twist Z'),('drawing','lower blank area','single curved diagonal stroke')])
append_md('SP61_CW_75_notes.md',r'''## Scan 024

The top word completes scan 023: “contour.” The manuscript itself has no following stop. Underlined “Exos (DEA)” asks: “Montrer que la donnée d'un torseur T sous G équivaut ... celle de” a Γ-torsor ω and a torsor T₀ under the twisted group {}^ωZ, for `G=Z.Γ` and Γ acting on Z. The lower diagonal ink stroke is reproduced without assigning it mathematical meaning. No date or authorial page count; pencil archive number 23.

**Mathematics and reading.** The source says opère, not opérant. Z and Γ are overwritten after the product description; their live order agrees with the definition, while the earlier letters remain separately recorded. Z is an abstract group here and is written with a single diagonal, unlike the double-stroke cyclic Z_n on scan 023. The twist exponent is a left upper ω and the group below the wedge is Γ. The event S024-SEMIDIRECT checks the exercise in the set-torsor setting by constructing both directions. It does not resolve the two tiny marks before celle de: the transcription preserves colon as the closer visible shape with à as alternative, without correcting the sentence.''')
append_md('SP61_CW_75_doubts.md',r'''### Scan 024 — certainty-only decisions

The heading is Exos, and the second overwritten letter is Z. The given T₀ has a round subscript zero. The live first factor is Z and the second Γ. The first overwritten letter, donnée/donné ending, and colon/à remain explicitly doubtful after their single crops.
''')
append_md('SP61_CW_75_hand_log.md',r'''## Added on scan 024

- **Abstract Z is single-stroke.** The semidirect-product group is written with a single diagonal at all live occurrences here; this is distinguished from the double-stroke cyclic group on scan 023. No automatic conversion to blackboard Z is made.
- **A tiny accented word can resemble punctuation.** Before celle de, the upper and lower marks are detached. The literal colon outline is preferred cautiously to à; this does not establish a rule for other à occurrences.
- **Overwriting keeps old factor names visible.** The live order Z, Γ is secure, with an earlier Z visible under the second factor. The first earlier capital is not secure enough to call a transposition without qualification.
''')
checks([('S024-SEMIDIRECT','targeted proof check','Use right torsors and G=Z semidirect Gamma with multiplication (z,gamma)(z′,gamma′)=(z gamma(z′),gamma gamma′). Given a G-torsor T, put omega=T/Z and U=T/Gamma. H=omega×_Gamma Z acts on U by [t]·[tZ,z]=[tz]; changing t to t gamma changes z to gamma^{-1}(z), so this is well-defined. Conversely from omega and an H-torsor U, take T=omega×U with (a,u)·(z,gamma)=(a gamma,u·[a,z]). The identity [a gamma,z′]=[a,gamma(z′)] verifies the multiplication law. The action is free and transitive by the torsor laws. Its two quotients recover omega and U, and t↦(tZ,tGamma) identifies the reconstruction with T. This supplies the requested set-theoretic equivalence, without imposing abelianity on Z.')])
assemble();log('scan 024 done')
print(checkpoint_due())
