from reading_support import *
save_tex(23,r'''\scanpage{23}
\uline{Contour \inserted{(comb.)} connexe} \inserted{$C$} définit

\textcircled{1} L'ens $\omega=\omega(C)$ à deux \unsure{éléments|élémts} de ses deux orientations.

À partir de là, on peut déjà écrire (à isom can. près) le groupe des translations du contour, \unsure{par}
\[
 G^+=\operatorname{Aut}^+(C)\xleftarrow{\sim}\omega\wedge_{\{\pm1\}}\mathbb Z_n
\]
(où $\{\pm1\}$ opère sur $\mathbb Z_n$ par homotheties)

\textcircled{2} Un torseur sous $G^+$

\deleted{\uline{\unsure{Exercice|Exercices}}} Et \unsure{inversmt|inversemt|inversement}, le couple formé par $(\omega,T)$, où $\omega$ un \deleted{tors} à $2$ él et $T$ un torseur sous $G^+\mathrel{\unsure{\ne|=|\leftrightarrows}}\omega\wedge_{\{\pm1,\}}\mathbb Z_n$, définit un
% archive sheet number: 22
''')
doubts(23,[('first item','éléments','élémts','medium','Crop (947,172,1337,250): medial letters run into a level stroke; full and contracted spelling cannot be separated.'),('right edge before first display','par','p followed by off-edge continuation','low','The word runs into the image boundary; a complete par is not securely present.'),('cancelled heading','Exercice','Exercices','low','Crop (256,914,496,1002): underline and cancellation survive separately; final small turn may include s.'),('after Et','inversmt','inversemt; inversement','low','Crop (574,889,820,969): compressed flat ending does not distinguish the omitted vowels.'),('second formula relation','ne','equals; opposing arrows','low','Crop (681,1093,964,1184): two bars, with an oblique/vertical stroke through the lower bar; no secure pair of arrowheads. Unlike the earlier equivalence, the sign is not mathematically unambiguous.')])
changes(23,[
('heading abbreviation','comb.','combin.','comb.','Left half: short comb with a b ascender and dot; no in continuation.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('heading adjective','connexe','convexe','connexe','Left half: paired low arches follow con; the middle is not a v.','high',False,True,'misread word','yes',2,'The contour is connected, not described as convex.'),
('heading underline','underlined Contour ... connexe','no underline','underlined Contour ... connexe','Left half: one horizontal line under the whole heading, stopping before C.','high',False,True,'other','no',10,''),
('C before définit','inserted C','baseline C','inserted C','Left half: capital C is raised above the line before définit.','high',False,True,'insertion or placement','no',6,''),
('first item abbreviation','L’ens','L’ens.','L’ens','Left half: no independent stop after ens.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('parenthesis after écrire','à isom can. près','sinon compris (doubtful)','à isom can. près','Halves: à is followed by isom can.; next line starts près). Both parts of the parenthesis are visible.','high',False,True,'misread word','yes',2,'The assertion is made up to canonical isomorphism.'),
('first formula relation','left arrow with sim above','simeq','left arrow with sim above','Right half: lower shaft has a left-pointing head and the upper short stroke is wavy, not a symmetric equivalence glyph alone.','high',False,True,'misread symbol or index','no',4,'The displayed identification has an explicit leftward arrow.'),
('cyclic group alphabet, three occurrences','mathbb Z_n','bold Z_n','mathbb Z_n','Halves: all three Z letters have two diagonal strokes.','high',False,True,'misread symbol or index','no',1,''),
('parenthetical action, last word','homothéties | homotheties','homothéties','homotheties','Right half: final plural s is visible, but no accent is visible over the internal e.','medium',True,True,'abbreviation expanded or spelling modernised','no',8,''),
('cancelled exercise heading','deleted underlined Exercice | Exercices','deleted Exercice, no underline','deleted underlined Exercice | Exercices','Crop scan 023 (256,914,496,1002): separate lower underline remains below the slanted cancellation.','high',False,True,'other','no',10,''),
('after Et','inversmt | inversemt | inversement','inversement','inversmt | inversemt | inversement','Crop scan 023 (574,889,820,969): contracted nearly flat tail; full spelling not securely present.','low',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('couple phrase','le couple formé','les couples formés','le couple formé','Right half: singular le and formé; no trailing s at either place.','high',False,True,'misread word','no',2,''),
('after où omega un','deleted tors | ens','deleted ill then live ens.','deleted tors, no live ens','Crop scan 023 (843,1012,974,1077): t ascender and o-like loop survive in the crossed group; directly followed by à. There is no extra live word ens.','medium',False,True,'text not on the page','yes',9,'The grammatical noun missing from the live sentence is not supplied.'),
('two-element abbreviation','él','él.','él','Right half: ends after the l before et, without a dot.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('second formula relation','= | simeq | opposing arrows','equals','ne | equals | opposing arrows','Crop scan 023 (681,1093,964,1184): two dark horizontal bars and a crossing stroke on the lower bar; unlike the first display no secure arrowhead. The visible crossing motivates ne, with explicit alternatives.','low',True,True,'misread symbol or index','no',1,'A possibly unequal sign is preserved as doubtful rather than made equal to fit the preceding formula.'),
('second formula group braces','±1 with doubtful comma','±1','±1,','Crop scan 023 (681,1093,964,1184): detached short low angled mark after 1, inside the brace.','high',False,True,'omission','no',3,'')])
inventory(23,[('text','heading','Contour (comb.) connexe C définit'),('insertion','above heading','(comb.)'),('insertion','above définit','C'),('text','first item','① L’ens ω=ω(C) ... orientations'),('text','before first formula','À partir de là ... par'),('display','middle','G⁺=Aut⁺(C) leftward identification ω∧Z_n'),('text','below display','où {±1} opère ... homotheties'),('text','second item','② Un torseur sous G⁺'),('deletion','below second item','underlined Exercice(s)'),('text','closing paragraph','Et inversmt, le couple ... définit un'),('deletion','after ω un','tors')])
append_md('SP61_CW_75_notes.md',r'''## Scan 023

This landscape sheet concerns a “Contour (comb.) connexe.” Its orientation set ω has two elements; its translation group is identified with the sign-twist of Z_n, and the contour supplies a torsor under that group. The converse begins here and continues with “contour.” on scan 024. No date or authorial page count; pencil archive number 22.

**Mathematics and reading.** Connectedness, not convexity, is legible in the heading. Choosing an orientation gives a generator of the cyclic translation group, and reversing orientation negates that generator; this is the sign-twist calculation S023-SIGN. It supports looking closely at the two displayed identifications but does not settle the lower sign. The first display has a left arrow marked with a wavy equivalence sign. The second has two bars and a crossing stroke through the lower one: ne is retained as a tentative visual reading, with equals and opposing arrows as alternatives. It may be a slip or a poorly formed correspondence sign; it is not silently corrected.

The parenthesis after écrire is “à isom can. près,” not H’s doubtful “sinon compris.” In the last sentence the text is singular “le couple formé ... définit,” and after ω un the only noun-like group is cancelled tors. H’s extra live ens. has no separate ink. The missing noun is not supplied. The edge-clipped par and the compressed inversmt remain doubtful.''')
append_md('SP61_CW_75_doubts.md',r'''### Scan 023 — certainty-only decisions

The possessive in item ① reads ses (crop (947,172,1337,250), initial descending loop); the cancelled group before à 2 él reads tors (crop (843,1012,974,1077)). The low comma after 1 in the last brace is distinct. The internal spelling éléments/élémts and the cancelled Exercice/Exercices ending remain open. The phrase at the right edge is still only provisionally par.
''')
append_md('SP61_CW_75_hand_log.md',r'''## Added on scan 023

- **Several interior letters flatten into one stroke.** Inversmt may be an abbreviation, whereas éléments may be full spelling; the flat medial strokes do not justify a general expansion rule. C marks these doubts; H expands inversement.
- **Arrow and relation signs must be read separately.** The first identification has a real left-pointing head. The last formula has crossed bars but no secure arrowhead. Their similar mathematical role is not used to standardize the ink.
- **Double diagonals mark Z here.** All three cyclic-group occurrences have doubled strokes, unlike the plain Z of the later abstract semidirect-product notation. H's bold alphabet does not reproduce this visible distinction.
- **Cancelled nouns are not replaced by a grammatical supply.** Tors is readable under cancellation, and no live ens follows it. H adds one.
''')
checks([('S023-SIGN','targeted proof check','For the cyclic contour model with n vertices, an orientation identifies its orientation-preserving translation group with Z/nZ by sending 1 to the next-vertex translation. Reversing orientation replaces that generator by its inverse. Thus the map from orientation choice and cyclic coordinate descends under (orientation reversed,k)~(orientation,−k), giving the sign-twist description of G⁺. The vertices form a simply transitive G⁺-set. This checks the cyclic model used on the page; it does not determine the visibly doubtful lower relation sign.')])
assemble();log('scan 023 done')
print(checkpoint_due())
