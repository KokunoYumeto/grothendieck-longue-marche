from record import *
src=ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-05/pages/J71-05_71_scan038.tex'
t=src.read_text(encoding='utf-8').replace(r'\unsure{\varnothing|\phi}',r'\varnothing')
# A cancellation is encoded with the supplied macro; hatching strokes are not readings.
a=t.index(r'\text{\tikz[baseline=(dx.base)]');b=t.index(r'\subset\operatorname{ext}\Lambda^i',a)
t=t[:a]+r'\deleted{D_x}'+t[b:]
t=t.replace(r'\margin{\resizebox{\marginparwidth}{!}{\tikz',r'\margin{\tikz').replace(r'(ex.south);}}}',r'(ex.south);}}')
(ROOT/'pages/J71-05_71_scan038.tex').write_text(t,encoding='utf-8')

notation(r'\Gamma,\Lambda,E,S','Angular Γ and Λ; ordinary roman E and S. E(Γ) is the convex envelope; S(Γ) its vertex set.','38 opening and construction','Shapes distinguish the letters; final E(Λ) is retained even where Γ is expected.')
notation(r'\Gamma^1_{ss\prime},\Gamma^2_{ab},\Lambda^i','Numerical superscripts 1,2 and dotted i; paired ss′ and ab subscripts.','38 construction, XII–XIII','The change of endpoint names is in the manuscript; the pencil asks a=s, b=s′?')
notation(r'\varnothing','Oval crossed by a long nearly vertical stroke, used for the empty set.','38 proof of XII','Resembles φ in isolation; intersection emptiness, with no scalar φ defined, fixes the notation. Check later occurrences.')
notation(r'\operatorname{int},\operatorname{ext},\operatorname{Ext}','Lowercase in main ink, capital E in the pencil formula.','38 XII–XIII and right margin','Capitalization retained by occurrence.')
notation('théorĕme / théorème','Second accent is a shallow concave arc, unlike the rising acute on the first e.','38 title','Breve-like form retained as first candidate, grave alternative; not silently normalized.')
notation('Roman page and lemma numbers','Roman numerals between short upper and lower rules.','38 XI; XII and XIII','Encoded with underline/overline, not as cancelled numerals.')
hand('An empty-set sign resembles φ: a small oval with a long through-stroke.','38 proof of XII','Confirmed at this occurrence; interpretation depends on set-valued context, not inclination alone.','C marked varnothing|phi; resolved as empty set without changing the first reading.')
hand('Lowercase b has a high loop and a short trailing hump, approaching h.','38 XII, the ab subscripts and {a,b}','Consistent in the visible occurrences on this page.','No substantive C/H error here; the endpoint renaming is a manuscript inconsistency, not a b/h correction.')
hand('The grave-like accent in théorème is drawn as a shallow concave arc.','38 title','Only this occurrence checked at this stage.','C preserved a breve/grave doubt; retained after crop rather than normalized.')

ret=[
 ('038-R1','title accent',r'\unsure{théorĕme|théorème}','editorial synopsis only',r'\unsure{théorĕme|théorème}','Concave curved stroke above the second e, not an unequivocal straight grave. Scan 38 crop (280,100,585,205).','medium'),
 ('038-R2','opening, after sommets',r'\deleted{\illegible{1}}','not transcribed',r'\deleted{\illegible{1}}','Compact over-inked blot; no defensible surviving word. Scan 38 crop (530,310,760,425).','low'),
 ('038-R3','XII, exponent after ext',r'\Lambda^{\deleted{\unsure{2}}1}','editorial synopsis only',r'\Lambda^{\deleted{\unsure{2}}1}','Large replacement 1 above crossed smaller bent mark, compatible with 2 but not certain. Scan 38 crop (785,1050,1020,1185).','medium'),
 ('038-R4','proof XII, before R²',r'\deleted{\unsure{\partial|E}}','not transcribed',r'\deleted{\unsure{\partial|E}}','Dense cancellation with a left edge and short right projection; neither candidate is secured. Scan 38 crop (1070,1310,1340,1435).','low'),
 ('038-R5','On suppose, struck word',r'\deleted{\unsure{que}}','not transcribed',r'\deleted{\unsure{que}}','Loop at left, long descender and rightward ending under horizontal hatching. The separately inserted que is clear. Scan 38 crop (710,1590,960,1715).','medium'),
 ('038-R6','XIII, participle',r'\unsure{vérifiont|vérifiant}','editorial synopsis only',r'\unsure{vérifiont|vérifiant}','Rounded closed vowel followed immediately by n; the ordinary a reading remains possible in this cursive join. Scan 38 crop (1250,1685,1590,1795).','medium'),
 ('038-R7','right margin, exponent on R',r'2|7','2',r'\unsure{2|7}','Pencil exponent is a high curved hook descending at right, with no secure lower foot. 2 is favored by the plane notation; the ink does not fully exclude 7. Scan 38 crop (1235,1760,1665,1960).','medium')]
for id,p,c,h,f,s,co in ret:change(38,id,p,c,h,f,s,co,record_type='crop decision')
for p,r,a,c,why in [
 ('title','théorĕme','théorème','medium','Shallow concave accent; crop 038-R1.'),
 ('after sommets',r'\deleted{\illegible{1}}','','low','Over-inked cancellation; crop 038-R2.'),
 ('XII corrected exponent',r'\deleted{2}1','','medium','Underlying digit remains uncertain; crop 038-R3.'),
 ('proof XII before R²',r'\deleted{\partial}','E','low','Cancelled glyph too heavily covered to decide; crop 038-R4.'),
 ('On suppose cancelled word','que','','medium','Surviving loops support que, but hatching obscures the middle; crop 038-R5.'),
 ('XIII participle','vérifiont','vérifiant','medium','Vowel is o-shaped, possibly the cursive a; crop 038-R6.'),
 ('right-margin R exponent','2','7','medium','Curved hook; context favors 2; crop 038-R7.')]:doubt(38,p,r,a,c,reason=why)
doubt(38,'proof XII empty intersection',r'\varnothing',r'\phi','high','resolved','The oval-and-stem sign names the empty set; no scalar φ is involved. Resolved on the bottom half; no crop needed.')

# H supplies actual text only in its two pencil marginal quotations. Its body is an editorial synopsis.
omissions=[
 ('title','3 - Preuve du théorĕme 1','Underlined title, with 1 outside the underline.'),
 ('opening paragraph','Soit Γ un polygone ... (cf. Remarque 1).','Four inked lines; ss′ subscripts, open interval, VIII reference, and inserted (de Γ).'),
 ('construction paragraph',"Soit Λ_ss′ l’arc de polygone [s,s′] ... selon {s,s′}.",'Three inked lines, with Λ_ss′ and the two Γ arcs.'),
 ('Lemme XII','Si Λ¹ (resp. Λ²) est un J-polygone ... ext Λ²)','Three lines of statement; a,b replace s,s′; the two parenthetic alternatives lack a connective in the ink.'),
 ('proof XII','Demonstration : Il est clair que ... c.q.f.d.','Three lines, including struck glyph before R² and the empty intersection.'),
 ('transition','On suppose maintenant [inserted que] Λ¹ et Λ² [deleted que] sont des J-polygones.','Inserted que above the line, cancelled word after Λ².'),
 ('Lemme XIII and display','Si x∈∂E(Γ) ... ext∂E(Γ) ∩ [deleted D_x] ⊂ extΛ^i, i=1,2.','Two prose lines and one display; D_x is crossed out, while the intersection sign remains live.'),
 ('proof XIII','Démonstration : Comme E(Λ^i)⊂E(Γ) ... ext∂E(Λ) ce qui entraîne l’ennoncé.','Two lines; deleted ∂E( and closing parenthesis, final Λ without i, double n in ennoncé.'),
 ('upper-left margin','!','An exclamation mark stands beside the opening paragraph.'),
 ('upper-right margin','vertical stroke','Short vertical mark beside the first paragraph.'),
 ('left margin under endpoint note','1','A small numeral 1 stands below the pencil endpoint equivalences.'),
 ('proof XII side marks','left and right vertical strokes','One vertical marginal stroke on each side of the proof.')]
for i,(p,f,s) in enumerate(omissions,1):change(38,f'038-H{i:02}',p,f,'not transcribed (editorial synopsis / untranscribed marks)',f,s+' Seen on supplied halves; no crop required.',h=True,kind='omission')
inv(38,[
 ('text','top right','XI with upper and lower rules'),('text','top','3 - Preuve du théorĕme 1'),
 ('margin note','upper left','!'),('text','upper body','Soit Γ un polygone'),('margin note','upper right','vertical stroke'),
 ('deletion','opening after sommets','illegible word'),('insertion','above réliant','(de Γ)'),
 ('text','upper-middle','Soit Λ_ss′ l’arc de polygone'),('margin note','left of XII','a=s; b=s′; ?'),
 ('text','middle','Lemme XII and four inclusions'),('deletion','XII exterior exponent','2 replaced by 1'),('margin note','left below endpoint note','1'),
 ('text','middle-lower','Demonstration : Il est clair que'),('deletion','proof XII before R²','∂ or E'),
 ('margin note','left of proof XII','vertical stroke'),('margin note','right of proof XII','vertical stroke'),
 ('text','lower-middle','On suppose maintenant'),('insertion','above transition','que'),('deletion','after Λ²','que'),
 ('text','lower body','Lemme XIII : Si x∈∂E(Γ)'),('display','below XIII','ext∂E(Γ) ∩ D_x ⊂ extΛ^i'),
 ('deletion','display XIII','D_x'),('margin note','right of XIII','Ext(∂E(Γ))=R²−E(Γ) ⊂ Ext(Λ^i), three-sided enclosure'),
 ('text','bottom','Démonstration : Comme E(Λ^i)⊂E(Γ)'),('deletion','bottom proof','∂E( and closing ) around Λ^i')])
note(38,"""**Content and page marks.** Manuscript XI, section “3 - Preuve du théorĕme 1” (accent doubtful), Lemmata XII and XIII; archive number 37. No date or total page count. The page constructs Λ¹ and Λ² by closing the two Γ-arcs with [s,s′]. XII puts the complementary arc in one component of the complement of a J-polygon. XIII concerns the exterior of the convex envelope.

**Reading decisions and checks.** 038-N1: the oval with a long through-stroke in `]s,s′[∩Γ=∅` is an empty-set sign, not an independent scalar φ; this resolves C’s notation doubt. 038-N2: conditional on the stated J-polygon property and the disjointness of the open arc, the connectedness argument in XII is sound: a connected subset of the two-component complement is contained in one component. This is a targeted check of that step, not a proof of the Jordan theorem. 038-N3: the exterior inclusion is consistent with E(Λ^i)⊂E(Γ); the pencil gives the stronger global formulation R²−E(Γ)⊂Ext(Λ^i). The exponent in the pencil is still pale and remains doubtful in the transcription.

**Authorial slips and interventions.** The ink changes s,s′ to a,b in XII; the pencil asks “a=s / b=s′ ?”. The parenthetic pair of inclusions in XII has no written “ou bien”; none is supplied. In XIII only D_x is cancelled, leaving a live intersection sign with no right operand. The last proof ends with E(Λ), although E(Γ) is what the preceding hypothesis supports. The transcript retains Λ. “réliant”, “récollant”, “réfait”, unaccented “Demonstration” and “definition”, and “ennoncé” are preserved. No other verbal reservation is written.""")
event('038-N1','used and rechecked in this run','Set intersection and notation context identify the φ-shaped mark as the empty set; no claim beyond notation identification.')
event('038-XII / 038-N2','targeted proof check','Conditional argument verified: connected subset of a complement with two separated components lies in one component; endpoint naming inconsistency retained.')
event('038-XIII / 038-N3','targeted proof check','Complement inclusion follows from E(Λ^i)⊂E(Γ), together with the usual exterior characterization for the J-polygons. Final E(Λ) and the orphaned intersection sign are textual slips, not silently repaired.')
done(38)
