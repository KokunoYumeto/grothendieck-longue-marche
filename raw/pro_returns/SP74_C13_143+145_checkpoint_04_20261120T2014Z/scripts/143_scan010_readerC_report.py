import json
from pathlib import Path
ROOT=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
(ROOT/'reviews').mkdir(parents=True,exist_ok=True)
tex=r'''\scanpage{10}
\mspage{5}
d'où
\[
(1)\qquad1\longrightarrow G'\longrightarrow\mathcal G'\longrightarrow\Gamma
\]
et un germe de relèvement
\[
(2)\qquad\diagram{\begin{tikzcd}[ampersand replacement=\&]
\mathcal G'\arrow[r]\&\Gamma\arrow[d,phantom,"\cup" description,"{\text{ss-gp ouvert}}"']\\
\&\Gamma'\arrow[ul]
\end{tikzcd}}
\]
\margin{pour mémoire : relation avec variations des corps de base\ldots}
\uline{Choisissons} (cf normalisations plus bas)
\textcircled{$\overline{\underline{\mathrm{III}}}$} \uline{un rev. universel}
$\unsure{\widetilde{\mathfrak X}'|\widetilde X'}$ de $\unsure{\mathfrak X'|X'}$,
d'où
\deleted{posons}
\[
\pi_1(\unsure{\mathfrak X'|X'})=\operatorname{Aut}(\unsure{\widetilde{\mathfrak X}'|\widetilde X'}/\unsure{\mathfrak X'|X'})
\]
On trouve alors

(3) \deleted{(3)} structure d'extension
\[
1\longrightarrow\pi_1(\unsure{\mathfrak X'|X'})\longrightarrow\mathcal E'\longrightarrow\mathcal G'\mathbin{-}1
\]
\margin{pour mémoire : relation entre pts de $\unsure{\mathfrak X'|X'}(\overline{\mathbf Q})$ et scindages partiels de l'extension (3)\ldots}
\[
(4)\qquad\mathcal E'\text{-ensembles}\quad\left\{\begin{array}{l}\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(I)\\\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(J)\end{array}\right.
\]
(5) Opérations de $\mathcal E'$ sur $I,J$ via $\mathcal G'$, et
$\mathcal E'$-applications
\[
\left\{\begin{array}{l}
\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(I)\mathbin{-}I\\
\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(J)\mathbin{-}J\simeq\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(J)/\pi_1
\end{array}\right.
\]
\mspage{9}
'''
(ROOT/'reviews/143_scan010_readerC.tex').write_text(tex,encoding='utf-8')
P='crops/143_scan010_readerC_'
changes=[]
def change(place,C,H,final,against_C,against_H,kind,ink,confidence='high',crop='page',box=None,marked_in_H=False,consequential=False):
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=against_C,against_H=against_H,kind=kind,ink=ink,confidence=confidence,crop=crop,box=box,marked_in_H=marked_in_H,consequential=consequential))
change('Diagram (2), relation between Gamma and Gamma-prime',r'\Gamma\arrow[d,phantom,"\cup" description]',r"\Gamma'\arrow[u,hook]",r'\Gamma\arrow[d,phantom,"\cup" description]',False,True,'drawing or diagram','Between the two Gamma forms is an isolated U-shaped inclusion sign, with a long left upright and a short right upright. There is no vertical arrow shaft joining the objects.',crop=P+'diagram-label.png',box=[1060,510,1510,636])
change('Diagram (2), label to the right of inclusion',r'\text{ss-groupe ouvert}','s-gp ouvert',r'\text{ss-gp ouvert}',True,True,'abbreviation expanded or spelling modernised','Two small connected s forms precede the hyphen. After it there are only g and p, the first with a looped descender and the second with a separate downstroke; the rest of groupe is absent.',crop=P+'diagram-label.png',box=[1060,510,1510,636])
change('After diagram (2), separate parenthetical sentence in H','[no witness]',r"($\Gamma' \subset \Gamma$ s-gp ouvert).",'[no separate sentence]',False,True,'text not on the page','The inclusion and its label occur inside the diagram. The white space below it contains no repeated Gamma-prime subset Gamma expression and no enclosing sentence parentheses.')
change('Upper oblique margin, word after avec',r'\unsure{restrictions|variétés}',r'\uncertain{variétés}','variations',True,True,'misread word','The word begins with a v-shaped stroke, has the repeated small i strokes and the long ending -tions; no initial r/e/s cluster supports restrictions. The ending extends past the t/i sequence as -ons, rather than -étés.',confidence='medium',crop=P+'upper-margin.png',box=[20,345,390,775],marked_in_H=True,consequential=True)
change('Upper oblique margin, end of note',r'des corps de base\ldots',r'\ill{} \ill{} \ill{}…',r'des corps de base\ldots',False,True,'readable ink left as \\ill{}','After variations, des has the tall d and hooked s. On the final line corps has a long p descender, followed by de and base; separate dots continue at the right.',crop=P+'upper-margin.png',box=[20,345,390,775],marked_in_H=True)
change('Parenthesis after Choisissons','(cf normalisations plus bas)',r'(cf.\ normalisation plus bas)','(cf normalisations plus bas)',False,True,'misread word','There is no dot between the descending f and normalisations. The long final n-stroke of normalisations is followed by a separate hooked final s before plus.',crop=P+'normalisations.png',box=[595,728,1155,831])
change('Choice number III',r'\textcircled{III}','(III)',r'\textcircled{$\overline{\underline{\mathrm{III}}}$}',True,True,'omission','An ellipse surrounds the three upright numeral strokes. Inside the ellipse a horizontal rule appears above III and a shorter rule below; neither is the outer ellipse.',confidence='high')
change('Universal-cover choice, the two X forms',r"$\widetilde X'$ de $X'$",r"$\widetilde{\mathfrak{X}}'$ de $\mathfrak{X}'$",r"$\unsure{\widetilde{\mathfrak X}'|\widetilde X'}$ de $\unsure{\mathfrak X'|X'}$",True,False,'misread symbol or index','Both X forms have a loop at upper right, a central descending stroke, and a transverse leftward stroke. This supports the ornate/fraktur rendering, but the page supplies no contrasting ordinary X; the alphabet remains explicitly doubtful.',confidence='low',crop=P+'x-form.png',box=[944,827,1402,960],consequential=True)
change('Fundamental-group identity, X alphabet',r"\pi_1(X')=\operatorname{Aut}(\widetilde X'/X')",r"\pi_1(\mathfrak{X}') = \mathrm{Aut}(\widetilde{\mathfrak{X}}'/\mathfrak{X}')",r"\pi_1(\unsure{\mathfrak X'|X'})=\operatorname{Aut}(\unsure{\widetilde{\mathfrak X}'|\widetilde X'}/\unsure{\mathfrak X'|X'})",True,False,'misread symbol or index','All three forms retain the looped upper part and cross stroke of the X in the cover choice; all three primes and the tilde on the numerator are present. Alphabet doubt is shared with the representative crop.',confidence='low',crop=P+'x-form.png',box=[944,827,1402,960],consequential=True)
change('Heading of (3), cancelled duplicate number',r'(3) \deleted{(3)}','(3)',r'(3) \deleted{(3)}',False,True,'deletion state','A live (3) stands farther left. Another (3) directly before structure is crossed by oblique strokes; the curved parentheses and central 3 survive below the strike.',crop=P+'extension.png',box=[324,1350,1240,1588])
change('Heading of (3), structure','structure',r'str.','structure',False,True,'abbreviation expanded or spelling modernised','After str, the connected low strokes continue through u/c and another tall t before the terminal ure. The ink is a full word rather than str followed by a stop.',crop=P+'extension.png',box=[324,1350,1240,1588])
change('Extension (3), complete expression',r"1\longrightarrow\pi_1(X')\longrightarrow\mathcal E'\mathbin{-}\mathcal G'\mathbin{-}1",r"1 \to \pi_1(\mathfrak{X}') \longrightarrow \Sigma' \longrightarrow \mathcal{G}' \to 1",r"1\longrightarrow\pi_1(\unsure{\mathfrak X'|X'})\longrightarrow\mathcal E'\longrightarrow\mathcal G'\mathbin{-}1",True,True,'misread symbol or index','The extension letter has two rounded E lobes, rather than the angular form of Sigma, and has a prime. The E-to-G stroke ends in a small raised triangular head comparable with this page’s compact arrowheads. The G-to-1 stroke is flat and has no head. The same looped X occurs in pi_1.',confidence='medium',crop=P+'extension.png',box=[324,1350,1240,1588],consequential=True)
change('Lower oblique margin, opening words','pour mémoire : relation entre pts de',r'\ill{} \ill{}','pour mémoire : relation entre pts de',False,True,'readable ink left as \\ill{}','Rotating the note exposes pour mémoire with its colon, then relation entre on the next line; pts de appears before the mathematical X, with a descending p and the small raised ts.',crop=P+'lower-margin.png',box=[18,1285,322,1817],marked_in_H=True)
change('Lower oblique margin, points expression',r"X'(\overline{\mathbf Q})",r'\mathfrak{X}(\overline{\mathbb{Q}})',r"\unsure{\mathfrak X'|X'}(\overline{\mathbf Q})",True,True,'misread symbol or index','A separate short prime is visible at upper right of X, before the left parenthesis. Q is a single round capital with tail and a separate overbar; no second left stem is visible. The X alphabet is the same unsettled ornate form as in the text.',confidence='medium',crop=P+'lower-margin.png',box=[18,1285,322,1817],consequential=True)
change('Lower oblique margin, remainder','et scindages partiels de l\'extension (3)'+r'\ldots',r'\ill{} \ill{}…','et scindages partiels de l\'extension (3)'+r'\ldots',False,True,'readable ink left as \\ill{}','The short et follows the closing parenthesis. The next line reads scindages, with a descending g, and partiels with a tall p and l. The final line reads de l’extension, followed by a parenthesized 3 and dots.',crop=P+'lower-margin.png',box=[18,1285,322,1817],marked_in_H=True,consequential=True)
change('Display (4), E-sets and X alphabet',r"\mathcal E'\text{-ensembles}\quad\left\{\begin{array}{l}\widetilde X'(I)\\\widetilde X'(J)\end{array}\right.",r"\Sigma'\text{-ensembles}\quad \left\{\begin{array}{l}\widetilde{\mathfrak{X}}'(I)\\\widetilde{\mathfrak{X}}'(J)\end{array}\right.",r"\mathcal E'\text{-ensembles}\quad\left\{\begin{array}{l}\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(I)\\\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(J)\end{array}\right.",True,True,'misread symbol or index','The initial letter repeats the two rounded lobes of the extension E and has a prime. Both entries have tildes and primes; I has horizontal serifs and J a long right-hand stroke with lower turn. Both Xs share the looped/transverse form already cropped.',confidence='medium',consequential=True)
change('(5), operations, acting letter',r"Opérations de $\mathcal E'$",r"Opérations de $\Sigma'$",r"Opérations de $\mathcal E'$",False,True,'misread symbol or index','The acting letter is the same rounded two-lobed E with a separate prime, rather than a Sigma with straight upper and lower horizontals.',consequential=True)
change('(5), applications, acting letter',r"$\mathcal E'$-applications",r"$\Sigma'$-applications",r"$\mathcal E'$-applications",False,True,'misread symbol or index','The prefix has the repeated two-lobed E shape, a small prime at upper right, then the hyphen and applications.',consequential=True)
change('(5), first map',r"\widetilde X'(I)\mathbin{-}I",r"\widetilde{\mathfrak{X}}'(I)\to I",r"\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(I)\mathbin{-}I",True,True,'misread symbol or index','The connector is a single slightly rising horizontal stroke ending with a flat rounded nib mark, with neither upper nor lower arrowhead branch. The tilde, prime and argument I are present; X retains the shared alphabet doubt.',confidence='medium',crop=P+'final-maps.png',box=[602,1998,1430,2220],consequential=True)
change('(5), second map and quotient',r"\widetilde X'(J)\mathbin{-}J\simeq\widetilde X'(J)/\pi_1",r"\widetilde{\mathfrak{X}}'(J)\to J\simeq\widetilde{\mathfrak{X}}'(J)/\pi_1",r"\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(J)\mathbin{-}J\simeq\unsure{\widetilde{\mathfrak X}'|\widetilde X'}(J)/\pi_1",True,True,'misread symbol or index','The connector before J has no head at either end. The comparison sign has a short curved upper stroke over a straight lower one. Tildes, primes and the final pi subscript 1 are all visible. The two X forms preserve the shared alphabet doubt.',confidence='medium',crop=P+'final-maps.png',box=[602,1998,1430,2220],consequential=True)
change('Bottom left pencil page number',r'\mspage{9}','[no witness]',r'\mspage{9}',False,True,'omission','At the lower left edge a small pale numeral has a closed upper loop and descending curved tail, reading 9.')
inv=[]
def item(n,kind,position,words):
 inv.append(dict(sheet_kind='text',hand='his hand',element=f'E{n:02d}',kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
item(1,'text','top right','pencil page number 5')
item(2,'text','top, first line',"d'où")
item(3,'display','upper part, y 160–280',"(1) 1 → G′ → cal G′ → Gamma")
item(4,'text','below (1)',"et un germe de relèvement")
item(5,'diagram','upper middle, (2)',"cal G′ → Gamma; Gamma′ → cal G′; upright inclusion cup and ss-gp ouvert")
item(6,'margin note','upper left, four oblique lines',"pour mémoire : relation avec variations des corps de base…")
item(7,'text','middle, y 745–820',"Choisissons (cf normalisations plus bas); Choisissons underlined")
item(8,'text','left of universal-cover choice','circled III with horizontal rules above and below')
item(9,'text','middle, y 835–950',"un rev. universel [underlined] tilde X′ de X′,")
item(10,'text','below cover choice',"d'où")
item(11,'deletion','above fundamental-group identity','posons, crossed horizontally')
item(12,'display','middle, y 1065–1145',"pi_1(X′) = Aut(tilde X′/X′)")
item(13,'text','below page fold',"On trouve alors")
item(14,'text','heading above extension',"(3) structure d'extension")
item(15,'deletion','between live (3) and structure','crossed duplicate (3)')
item(16,'display','lower middle, y 1440–1560',"1 → pi_1(X′) → E′ → cal G′ — 1")
item(17,'margin note','lower left, five oblique lines',"pour mémoire : relation entre pts de X′(bar Q) et scindages partiels de l'extension (3)…")
item(18,'display','(4), y 1610–1795',"E′-ensembles, brace, tilde X′(I), tilde X′(J)")
item(19,'text','(5), two lines, y 1850–2010',"Opérations de E′ sur I,J via cal G′, et E′-applications")
item(20,'display','bottom, y 2025–2200',"brace; tilde X′(I) — I; tilde X′(J) — J ≃ tilde X′(J)/pi_1")
item(21,'text','bottom left','pencil page number 9')
report={
 'key':'143_scan010','reader':'C','stage':'first','image_views':['original','half1','half2'],
 'changes':changes,
 'decisions':[{'id':'M0662','decision':'other','reading':'variations','ink':'The initial v and the extended -tions/-ons ending are visible in the rotated crop; the word is neither restrictions nor variétés.','crop':P+'upper-margin.png','box':[20,345,390,775],'confidence':'medium'}],
 'inventory':inv,
 'remaining_doubts':[{'place':'All twelve X occurrences, beginning with the universal-cover choice','reading':r'\unsure{\mathfrak X|X}','alternatives':r'\mathfrak X versus ordinary X in a looped handwriting form','confidence':'low','reason':'The X always has the same looped upper-right portion and transverse stroke. There is no ordinary contrasting X on this page to establish whether the ornate alphabet is semantically distinct. The first reading follows the visible ornate form, but all occurrences retain the doubt.'}],
 'certainty_resolutions':[],
 'notation':[{'form':r'\mathcal E\,\text{(with prime)}','meaning':'The middle group of extension (3), also acting on the displayed sets and maps.','evidence':'The letter has two rounded lobes in all four occurrences; it is not H’s angular Sigma.'},{'form':r'\cup\ \text{between vertically stacked }\Gamma,\Gamma\prime','meaning':'The page’s vertically arranged inclusion relation; Gamma-prime is labelled an open subgroup.','evidence':'An isolated U-shaped sign lies between the two Gamma objects, not a drawn shaft or hooked arrow.'},{'form':r'\mathbin{-}','meaning':'Headless connector strokes in the final extension link and both maps in (5); preserved as drawn.','evidence':'The three strokes end flat, unlike the visibly headed connectors earlier on the page.'},{'form':r'\unsure{\mathfrak X|X}','meaning':'The object whose universal cover is chosen; a shared unresolved alphabet distinction.','evidence':'The looped/crossed X form is consistent in all twelve occurrences on this page, with no contrasting form.'},{'form':r'\overline{\mathbf Q}','meaning':'The barred Q in the point expression of the lower margin note.','evidence':'A single round Q, tail and separate overbar are visible; no doubled stem is present.'}],
 'abbreviations':[{'form':'ss-gp','expansion':'sous-groupe'},{'form':'rev.','expansion':'revêtement'},{'form':'cf','expansion':'confer / comparer'},{'form':'pts','expansion':'points'},{'form':'Aut','expansion':'automorphismes'}],
 'hand_log':[{'habit':'The extension letter is a rounded calligraphic E, which can be mistaken for Sigma.','places':'143_scan010: (3), (4), and twice in (5).','scope':'All four occurrences inspected; the two rounded lobes recur.','misreadings':'H reads Sigma at all four places; C reads cal E.'},{'habit':'The X form has a small upper-right loop and a long transverse stroke through a descending central stroke.','places':'143_scan010: universal-cover choice, fundamental-group identity, extension, lower margin, displays (4) and (5).','scope':'All twelve occurrences inspected; the alphabet distinction remains qualified, not established.','misreadings':'C renders X; H renders fraktur X. No definite misreading is asserted until cross-page comparison.'},{'habit':'Some rightward arrowheads are compressed to a small raised tip at the right end of the shaft.','places':'143_scan010: last arrow of (1), horizontal arrow of (2), and E-prime to cal G-prime in (3).','scope':'These occurrences inspected and compared; genuine flat-ended strokes remain in the last link of (3) and both maps of (5).','misreadings':'C gives the E-to-G connector in (3) as a bar; H adds heads to the three flat-ended connectors.'},{'habit':'Roman III is enclosed in an ellipse and additionally ruled above and below.','places':'143_scan010: universal-cover choice.','scope':'One occurrence on the assigned page.','misreadings':'C omits the internal rules; H also replaces the ellipse with parentheses.'}],
 'notes':[{'id':'143_scan010-N1','text':'The page starts with the displayed sequence (1) and a germ of a lifting (2) from an open subgroup Gamma-prime. It then chooses, under the circled III, a universal cover and writes the fundamental group as its automorphism group. The page proceeds to an extension (3), sets with an E-prime action (4), actions on I and J through cal G-prime, and the displayed applications (5). This is an account of the source, not a proof of its assertions.'},{'id':'143_scan010-N2','text':'The two oblique reminders ask about the relation with “variations des corps de base” and the relation between points over barred Q and “scindages partiels de l’extension (3)”. Neither note states or proves that correspondence. The cancelled word “posons” and the cancelled duplicate “(3)” are retained.'},{'id':'143_scan010-N3','text':'The final map strokes and the last link of extension (3) are headless in the manuscript. They are retained as bars even though the accompanying words call the final expressions applications. No mathematical regularization was used to add arrowheads. The X alphabet remains explicitly doubtful throughout; a broader notation comparison is needed.'}],
 'check_events':[{'statement_id':'143_scan010-N1','type':'carried as background without fault found','outcome':'The fundamental-group identity, extension, actions and quotient identification were read as source assertions. No proof or independent mathematical verification was performed, and none was used to override the visible ink.'}],
 'unresolved_for_main':[{'place':'The shared X alphabet at all twelve occurrences','question':'Adjudicate ordinary X versus fraktur X using notation evidence from the other assigned pages; this reader did not inspect them. Candidate keeps every occurrence in unsure.','crop':P+'x-form.png','box':[944,827,1402,960]}],
 'raw_difference_disposition':'All 38 packet difference entries were inspected against both full-resolution halves. Material differences are covered individually or within one mathematical expression by the changes rows, including readings retained from C. Pure macro syntax, braces around math alphabets, display wrappers, line wrapping, and H’s editorial page/synopsis or marginal-location prose were excluded. The separate Gamma-prime-subset-Gamma parenthetical supplied by H was assessed as non-source duplication, not ignored as markup. The full page and each half were viewed once; seven unique tight crops were created from the original, each only once. No web, OCR, recognition software or TeX compilation was used.'
}

# Apply the main reader's shared-notation adjudication received after this independent reading.
def settle_x(s):
 return s.replace(r"\unsure{\widetilde{\mathfrak X}'|\widetilde X'}",r"\widetilde{\mathfrak X}'").replace(r"\unsure{\mathfrak X'|X'}",r"\mathfrak X'")
def shared_final(s):
 return settle_x(s).replace(r"\mathcal E'",r"\unsure{\mathcal E|\Sigma}'")
tex=shared_final(tex)
(ROOT/'reviews/143_scan010_readerC.tex').write_text(tex,encoding='utf-8')
for row in changes:
 row['final']=shared_final(row['final'])
 if row['place']=='Universal-cover choice, the two X forms':
  row['ink']='Both X forms have a loop at upper right, a central descending stroke, and a transverse leftward stroke. The shared notation table supplied by the main reader now fixes this recurring form as fraktur X; this reader inspected no other pages.'
  row['confidence']='high'
 elif row['place']=='Fundamental-group identity, X alphabet':
  row['ink']='All three forms retain the looped upper part and cross stroke of the X in the cover choice; all three primes and the tilde on the numerator are present. The main reader’s shared notation table fixes the recurring glyph as fraktur X.'
  row['confidence']='high'
 elif row['place']=='Extension (3), complete expression':
  row['ink']='The extension letter has two rounded lobes and a prime. This reader favours calligraphic E, while the main reader retains the E/Sigma doubt because the independent readings differ. The E/Sigma-to-G stroke ends in a small raised triangular head comparable with this page’s compact arrowheads. The G-to-1 stroke is flat and has no head. The looped X is encoded fraktur under the supplied notation table.'
 elif row['place']=='Lower oblique margin, points expression':
  row['ink']='A separate short prime is visible at upper right of X, before the left parenthesis. Q is a round capital with tail and a separate overbar. The main reader’s notation table selects fraktur X for the recurring looped form, and treats C’s bold Q versus H’s blackboard Q as rendering of the same notation. The material difference from H here is the visible prime.'
  row['confidence']='high'
 elif row['place']=='Display (4), E-sets and X alphabet':
  row['ink']='The initial letter repeats the two rounded lobes of the extension glyph and has a prime; its E/Sigma identification remains open under the shared notation table. Both entries have tildes and primes; I has horizontal serifs and J a long right-hand stroke with lower turn. Both Xs share the looped/transverse form, now encoded fraktur by the main reader’s notation decision.'
 elif row['place']=='(5), operations, acting letter':
  row['ink']='The acting letter repeats the rounded two-lobed extension glyph with a separate prime. This reader favours calligraphic E, but the shared notation table retains the E/Sigma doubt consistently.'
  row['confidence']='medium'
 elif row['place']=='(5), applications, acting letter':
  row['ink']='The prefix has the repeated rounded extension glyph, a small prime at upper right, then the hyphen and applications. The shared notation table retains the E/Sigma doubt consistently.'
  row['confidence']='medium'
 elif row['place']=='(5), first map':
  row['ink']='The connector is a single slightly rising horizontal stroke ending with a flat rounded nib mark, with neither upper nor lower arrowhead branch. The tilde, prime and argument I are present. X is encoded fraktur under the supplied common notation.'
  row['confidence']='high'
 elif row['place']=='(5), second map and quotient':
  row['ink']='The connector before J has no head at either end. The comparison sign has a short curved upper stroke over a straight lower one. Tildes, primes and the final pi subscript 1 are all visible. Both X forms are encoded fraktur under the supplied common notation.'
  row['confidence']='high'
report['remaining_doubts']=[{'place':'The extension/action-group glyph, four occurrences in (3), (4), and twice in (5)','reading':r"\unsure{\mathcal E|\Sigma}'",'alternatives':'Calligraphic E or capital Sigma, each with a prime','confidence':'medium','reason':'This reader favours E from the two rounded lobes, but the main reader reports differing independent readings and instructs a consistent E/Sigma uncertainty under the updated shared notation table.'}]
report['notation'][0]={'form':r"\unsure{\mathcal E|\Sigma}'",'meaning':'The middle group of extension (3), also acting on the displayed sets and maps.','evidence':'The rounded glyph recurs at all four places. This reader’s first reading is calligraphic E; the main reader’s common notation retains E/Sigma uncertainty because independent readers disagree.'}
report['notation'][3]={'form':r'\mathfrak X','meaning':'The object whose universal cover is chosen.','evidence':'The looped/crossed X is consistent in all twelve occurrences on this page. The main reader’s supplied notation table resolves its encoding as fraktur X from broader comparison, which this reader did not independently inspect.'}
report['notation'][4]={'form':r'\overline{\mathbf Q}','meaning':'The barred Q in the point expression of the lower margin note.','evidence':'A round Q, tail and separate overbar are visible. The updated common notation treats bold versus blackboard Q as rendering of the same notation.'}
report['hand_log'][0]={'habit':'The extension/action-group glyph has two rounded lobes and can be read as cursive E or Sigma.','places':'143_scan010: (3), (4), and twice in (5).','scope':'All four occurrences inspected; the form recurs. Identification remains qualified under the main reader’s shared notation decision.','misreadings':'C gives cal E; H gives Sigma. This reader favours E, but no definite misreading is asserted in the common candidate.'}
report['hand_log'][1]={'habit':'The X form has a small upper-right loop and a long transverse stroke through a descending central stroke.','places':'143_scan010: universal-cover choice, fundamental-group identity, extension, lower margin, displays (4) and (5).','scope':'All twelve occurrences inspected; the main reader’s updated notation table selects fraktur X for this form.','misreadings':'C renders ordinary X, H fraktur X. This reader now follows the supplied common fraktur encoding, without inspecting other pages.'}
report['notes'][0]['text']='The page starts with the displayed sequence (1) and a germ of a lifting (2) from an open subgroup Gamma-prime. It then chooses, under the circled III, a universal cover and writes the fundamental group as its automorphism group. The page proceeds to an extension (3), sets with an action of the extension group (4), actions on I and J through cal G-prime, and the displayed applications (5). The extension group’s letter remains marked E/Sigma. This is an account of the source, not a proof of its assertions.'
report['notes'][2]['text']='The final map strokes and the last link of extension (3) are headless in the manuscript. They are retained as bars even though the accompanying words call the final expressions applications. No mathematical regularization was used to add arrowheads. After the independent reading, the main reader supplied a shared notation decision: use fraktur X for the recurring looped form, and retain the extension glyph as unsure between calligraphic E and Sigma. These decisions are reflected consistently in the candidate.'
report['unresolved_for_main']=[{'place':'The extension/action-group glyph at all four occurrences','question':'The candidate retains the main reader’s provisional E/Sigma notation consistently. This reader favours E from the rounded lobes; the common uncertainty remains for final adjudication.','crop':P+'extension.png','box':[324,1350,1240,1588]}]
report['raw_difference_disposition']+=' The main reader subsequently supplied common notation decisions for X, the provisional E/Sigma glyph, and Q rendering; these were applied without reading any other page.'
(ROOT/'reviews/143_scan010_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote candidate and report:',len(changes),'changes;',len(inv),'inventory items')
