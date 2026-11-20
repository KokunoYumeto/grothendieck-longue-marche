from pathlib import Path
import json
ROOT=Path('/workspace/scratch/811dda00717a')
OUT=ROOT/'work/readers/scan037/R3'
C=ROOT/'source/SP41_CW_81_witnesses/codex/J81-05/pages/J81-05_81_scan037.tex'
H=ROOT/'runtime_inputs/scan037/H.tex'
ct=C.read_text();ht=H.read_text()
crops=json.loads((OUT/'crop_metadata.json').read_text())
bycrop={x['path'].split('/')[-1].split('_')[0]:x['path'] for x in crops}
F=[]
def f(n,place,c,h,reading,ac,ah,kind,marked,conf,ev,bbox,crop=None,ids=(),status='none',math='',**extra):
 d=dict(id=f'scan037-R3-F{n:02d}',place=place,c=c,h=h,reading=reading,against_C=ac,against_H=ah,kind=kind,marked_in_H=marked,confidence=conf,evidence=ev,bbox=bbox,crop=bycrop.get(crop),c_doubt_ids=list(ids),c_doubt_status=status,mathematical_note=math)
 d.update(extra);F.append(d)
f(1,'Upper-left heading',r'\uline{\unsure{Cor|Cor.}}',r'\emph{Cor}\add{ollaire}',r'\uline{Cor}',True,True,'abbreviation expanded or spelling modernised',False,'high','Crop 01 shows C, a low rounded o and final returning r above a separate underline. No detached terminal point or letters ollaire follow the r.',[235,34,315,99],'01',['C037-D001'],'resolved')
f(2,'Starter immediately under Cor',r'Dans',r'\struck{Dans} Dans',r'\deleted{D}ans',True,True,'other',False,'medium','The large D below Cor has a broad oblique cancellation across its stem and bowl. The low continuing ans stroke is written once, before le cas. I retain those uncrossed common letters once. H’s note explicitly acknowledges the crossed D; its body supplies a second complete Dans, for which this crop has no second group.',[264,70,393,135],'01',h_editorial_note='« Cor » est écrit au-dessus d’un « D » biffé',state_scope='D crossed; ans retained once; no second full Dans')
f(3,'Slanted margin, word after relations',r'\unsure{strictes}',r'\uncertain{ci-dessus}',r'\unsure{strictes}',False,True,'misread word',True,'medium','The rotated margin has one compact word after relations, with an initial steep high stroke, a crossed tall stroke and a short final s-like return. These support strictes first; the compressed middle remains unresolved. There is no separated ci- or dessus group.',[161,218,301,355],'02',['C037-D002'],'retained')
f(4,'Slanted margin, parenthesized sign before soient',r'\unsure{(*)}',r'absent',r'$(*)$',True,True,'omission',False,'high','Crop 02 separates an opening curved boundary, a compact crossed centre and a closing curved boundary before soient. The three marks are retained as the parenthesized asterisk.',[31,473,107,548],'02',['C037-D003'],'resolved',math='The nearby display also bears a parenthesized asterisk, but the marginal sign was read directly.')
f(5,'Slanted margin, fourth Sigma index',r'\Sigma_{\unsure{2|1}}^-',r'\Sigma_{2}^{-}',r'\Sigma_{\unsure{1|2}}^-',True,True,'misread symbol or index',False,'low','The fourth Sigma foot ends in a short downward hook. It has no clearly separated upper bow and low right foot like the preceding detached 2. I put 1 first and retain 2 because the low digit and the capital’s terminal merge.',[221,550,261,591],'02',['C037-D004'],'retained',math='The alternating four-term list was not used to supply the last numeral.')
f(6,'Slanted margin, il f et s.',r'\unsure{f|f.} et s.',r'faut et il suffit',r'f et s.',True,True,'abbreviation expanded or spelling modernised',False,'high','The margin has a tall hooked f followed directly by et and the compact s with a detached period. No detached point occurs after f. The written group contains neither the expanded faut/suffit nor a second il.',[255,376,440,559],'02',['C037-D005'],'resolved')
f(7,'Slanted margin, contraction above soient',r'\inserted{\unsure{mutlt.}}',r'absent',r'\inserted{\unsure{mutlt.}}',False,True,'omission',False,'low','A separate narrow word stands above the baseline between soient and distincts, with several low shoulders, a taller final stroke and a small terminal point. Its compact strokes do not securely separate all letters; mutlt. remains the first reading. The raised placement is retained.',[259,496,345,580],'02',['C037-D006'],'retained')
f(8,'Slanted margin, between inclusion and entre',r"relations d'inclusion entre",r"relations d'inclusion \uncertain{non triviales} entre",r"relations d'inclusion entre",False,True,'text not on the page',True,'high','The margin breaks d’inclu- / sion across its lines, then continues entre les ensembles. The two line segments contain no additional non triviales word group.',[15,332,315,692],'02',component_bboxes=[[162,332,315,483],[15,521,190,692]])
f(9,'Slanted margin, after distincts',r'distincts, et',r'distincts et',r'distincts et',True,False,'other',False,'medium','The terminal s ends in its own returning hook; no detached comma is separated before the next-line et. The comma supplied by C is omitted.',[455,386,520,457],'02')
f(10,'Proof opening, line break after inverses',r'inverses, par',r'inverses, \ill{} par',r'inverses, par',False,True,'text not on the page',True,'high','Half a shows inverses followed by its comma at the right of one line, then par hypothèse at the left of the next. There is no intervening written word or unreadable ink patch.',[279,593,1602,751],component_bboxes=[[1361,595,1602,660],[279,671,667,751]],support='half a')
f(11,'D’autre part, on n’a pas: underline scope',r"on n'\uline{a pas}",r"on n'a \emph{pas}",r"on n'\uline{a pas}",False,True,'other',False,'high','Crop 03 shows one horizontal underline beginning directly below the small a and continuing beneath pas; it crosses the p descender and ends under the terminal s. H’s emphasis covers only pas.',[1137,679,1340,747],'03',h_macro_mapping='H uses emph for the author’s emphasis; this finding concerns the included word a, not the choice of macro.')
f(12,'Second relation after on n’a pas',r'\Sigma_1^-\unsure{\subset|\in}\Sigma_1^+',r'\Sigma_{1}^{-}\subset\Sigma_{1}^{+}',r'\Sigma_1^-\unsure{\subset|\in}\Sigma_1^+',False,False,'misread symbol or index',False,'medium','The relation has an open upper-and-lower c-shaped contour, a second left return and a short dark inner upright. No clean independent middle horizontal separates. Subset remains first, with membership retained because the retracing obscures the inner stroke.',[970,780,1023,819],'04',['C037-D007'],'retained')
f(13,'Cancelled pair before the live Sigma1-minus equals X',r'\deleted{\unsure{\Sigma_1^+,\Sigma_1^+}}',r'\struck{$\Sigma_{1}^{+}$, $\Sigma_{1}^{-}$}',r'\deleted{\unsure{\Sigma_1^+,\Sigma_1^+|\Sigma_1^+,\Sigma_1^-}}',True,True,'misread symbol or index',False,'low','Two angular Sigma bodies survive under a long zigzag cancellation. A short crossed high cluster favours the first plus; the second small sign is entangled with the cancellation and a low crossing. The indices and second sign cannot be separated securely, so the whole pair remains uncertain, with C’s primary pair retained and the second-minus alternative explicit.',[282,859,474,918],'05',['C037-D008'],'retained',mathematical_note_extra='No sign was supplied from the live equation that follows.')
f(14,'Proof, de = on n’a pas',r'de $=$',r'de même',r'de $=$',False,True,'abbreviation expanded or spelling modernised',False,'high','Half a clearly shows de followed by two short parallel horizontal bars before on; no letters of même occupy that place.',[750,858,922,902],support='half a')
f(15,'Target capital after Sigma2-plus subset',r'\unsure{\Sigma|E}',r'\Sigma_{2}^{-}',r'\unsure{\Sigma|E}',False,False,'misread symbol or index',False,'low','Crop 06 shows a detached top bar, a right-facing angular upper return and a low base, together with a heavy central upright. Sigma is retained first, with E because the joined upright obscures the capital’s body. The extra upright is separately recorded in F17.',[1481,851,1530,907],'06',['C037-D009'],'retained')
f(16,'Same target, lower numeral',r'\unsure{2|1}',r'\Sigma_{2}^{-}',r'\unsure{2|1}',False,False,'misread symbol or index',False,'low','The low suffix has a curved roof and a descending terminal attached to the capital’s base. Its low rightward foot is not cleanly separated. Keep 2 first and 1 as the alternative.',[1514,886,1534,910],'06',['C037-D010'],'retained')
f(17,'Possible older upright through that target capital',r'absent',r'absent',r'\unsure{\deleted{\vert}}\unsure{\Sigma|E}_{\unsure{2|1}}^-',True,True,'other',False,'low','A thick near-vertical line continues from the upper return through the middle and down to the base of the target. Its identity as older writing versus reinforcement remains open. The transcription retains only the visible upright, with uncertainty over its cancelled state, before the uncertain live capital.',[1486,857,1506,900],'06')
f(18,'Puisque, second Sigma: absent or fused lower numeral',r'\unsure{\Sigma^+|\Sigma_2^+}',r'\Sigma_{2}^{+}',r'\unsure{\Sigma|\Sigma_2}^{\unsure{\top|+}}',False,True,'misread symbol or index',False,'medium','The second Sigma’s low horizontal turns directly downward. No detached numeral is visible; the attached turn still permits a fused 2. Bare Sigma remains first. The high sign is handled separately in F19.',[1356,1051,1405,1095],'07',['C037-D011'],'retained',c_mapping='Factoring the common exponent maps C’s ordered base choices (Sigma-plus, Sigma2-plus) to (Sigma, Sigma2) followed by the common exponent. This reversible factoring alone is not counted against C; F19 records the changed high-sign reading.')
f(19,'Puisque, high sign on second Sigma',r'\Sigma^+|\Sigma_2^+',r'\Sigma_{2}^{+}',r'\unsure{\Sigma|\Sigma_2}^{\unsure{\top|+}}',True,True,'misread symbol or index',False,'medium','Crop 07 shows a short horizontal cap and a downward stem. No distinct rise projects above the cap; a very small thickening at the junction leaves plus possible. The first reading is top-shaped.',[1405,1052,1430,1082],'07')
f(20,'Line break after ou, before inclusion inverse',r'ou inclusion inverse',r"ou l'inclusion inverse",r'ou inclusion inverse',False,True,'text not on the page',False,'high','Half b shows ou at the end of the preceding line and inclusion beginning the next with its dotted initial i. No separate l or apostrophe precedes inclusion.',[281,1241,1604,1410],component_bboxes=[[1527,1265,1604,1316],[281,1367,772,1410]],support='half b')
f(21,'After inclusion inverse, before lit',r'inverse, on lit',r'inverse, or on\n\uncertain{lit}',r'inverse, on lit',False,True,'text not on the page',False,'high','After the comma the ink has one compact on group and then lit. H’s additional or has no independent letter group in the available space. The l of lit has a high loop and a short following dotted i and terminal t.',[771,1336,1055,1411],support='half b',h_exact_source='inverse, or on\n\\uncertain{lit}',h_uncertainty_note='H marks lit uncertain; the extra or itself is not marked.')
f(22,'Cancelled word under la première',r'\deleted{\unsure{cela}}',r'\struck{cela}',r'\deleted{\unsure{cela}}',False,False,'misread word',False,'low','Crop 08 shows a pale initial open c-like body and connected low returns crossed by a dark short line, also touched by the inserted p descender. Cela remains plausible; its middle and ending are obscured.',[571,1454,662,1501],'08',['C037-D012'],'retained')
f(23,'Inserted article and adjective above signifierait',r'\unsure{la première|le premier}',r'la première',r'la première',True,False,'misread word',False,'high','The article has a tall l curve and a low terminal a loop. Première has a descending p, dotted i, an accent above the following vowel and a final low e return after r. The group is interlinear, over a curved leader.',[545,1405,846,1490],'08',['C037-D013'],'resolved',h_editorial_note='H explicitly states that la première p. ex. is added in the interline; no insertion-state difference is counted.')
f(24,'Inserted abbreviation after la première',r'\unsure{p.ex.|p. ex.}',r'\uncertain{p.\ ex.}',r'\unsure{p.ex.|p. ex.}',False,False,'other',True,'medium','A descending p is followed by a small point, open e-like return, crossed/slanting x and terminal point. The amount of separation after the first point does not fix whether to encode a word space.',[877,1408,972,1495],'08',['C037-D014'],'retained',macro_note='The explicit TeX space in H does not produce a separate H primary-text finding here.')
f(25,'Live signifierait que and the curve above it',r'signifierait que',r'\struck{signifierait que\n$\Sigma_{12}\simeq\Sigma_{1}^{-}$}',r'signifierait que',False,True,'deletion state (struck given live or live given struck)',False,'high','The visible letters form signifierait que continuously. The long curved line lies above the body of signifierait and curves down at its beginning, attaching the interlinear la première p.ex.; it crosses the tall f but does not cancel the word body or que. The later equation has its own straight cancellation. H’s note about rewriting has been checked, but does not supply another visible word at this locus.',[713,1447,1180,1558],'08',h_editorial_note='les deux mots entre « la première p. ex. » et « Sigma2-minus = X » sont récrits sur la ligne biffée',crop_limitation='The very bottom of the long que descender reaches beyond crop 08. Half b included its full available extent; no repeat crop was made.')
f(26,'H’s implique before the final Sigma2-minus equals X',r'absent',r'\uncertain{implique}',r'absent',False,True,'text not on the page',True,'high','The available ink in this passage is the live signifierait que, the cancelled equation, then the cancelled short connective on the next line before the live Sigma2-minus = X. No additional implique letter group is visible. The H rewriting note is not used to invent a second live wording.',[713,1447,1180,1558],'08',supporting_crops=[bycrop['09'],bycrop['10']])
f(27,'Cancelled equation, comparison sign',r'\Sigma_{12}\unsure{\simeq|=}\Sigma_1^-',r'\Sigma_{12}\simeq\Sigma_{1}^{-}',r'\Sigma_{12}\simeq\Sigma_1^-',True,False,'misread symbol or index',False,'high','Crop 09 cleanly separates a high wavy stroke and a short lower horizontal bar. The long cancellation passes between them and through both Sigma bodies. The waved-over-bar reading is resolved.',[1371,1437,1443,1484],'09',['C037-D015'],'resolved')
f(28,'Cancelled connective before Sigma2-minus = X',r"\deleted{\unsure{d'où}}",r'\struck{et}',r"\deleted{\unsure{d'où}}",False,True,'misread word',False,'low','The left group has a low loop and tall ascender compatible with d, followed by a small raised trace, a looped right body and compressed low material under a strong horizontal cancellation. These do not support a clear et; d’où remains the uncertain first reading.',[296,1550,408,1606],'10',['C037-D016'],'retained')
f(29,'Proof ending, ce que l’on a exclu',r"ce que l'on a exclu",r"cas que l'on a exclu",r"ce que l'on a exclu",False,True,'misread word',False,'high','Half b has a single open c and low returning e before que, with no separate a bowl or terminal s. Read ce.',[782,1547,861,1600],support='half b')
f(30,'Lower heading Déf',r'\uline{\unsure{Déf|Déf.}}',r'\emph{Déf}',r'\uline{Déf}',True,False,'other',False,'high','Crop 11 shows D, a small accented e and a long f descender crossing the underline. The dark short trace below the e is connected to the heading’s lower strokes; no separate period follows f.',[305,1660,402,1766],'11',['C037-D017'],'resolved')
f(31,'Definition, first Pi and recurring case',r'\Pi_1',r'\Pi_{1}',r'\unsure{\Pi|\pi}_1',True,False,'misread symbol or index',False,'medium','The first Pi has one common cap with two descending stems. Its case is not securely fixed by an independently contrasting form on this page, so capital Pi remains first with lowercase pi retained at the first occurrence.',[859,1680,913,1733],'11')
f(32,'Definition, second Pi-shaped capital',r'\Pi_2',r'\Pi_{2}',r'\unsure{\Pi|R}_2',True,False,'misread symbol or index',False,'medium','The second capital has a top bar curling down at the right, a left stem and a second oblique descending branch. The curling upper-right stroke gives an R-like alternative, although the two descending stems support Pi first. No separate older layer is asserted.',[947,1679,1008,1736],'11')
f(33,'Definition, initial letter of strictement',r'strictement',r'strictement',r'\unsure{strictement|Strictement}',True,False,'misread word',False,'medium','Crop 12 shows a large looped initial s joined to t. Its height makes a capital S possible; the rest of the word is retained as strictement. Lowercase remains first, and the added case uncertainty alone is not an H difference.',[1221,1671,1415,1741],'12')
f(34,'Definition, underlined word continuing after non',r'panachées',r'parallèles',r'panachées',False,True,'misread word',False,'high','Half b shows the long p descender, low ana sequence, c/h group and accented é followed by es. The word is panachées; it carries the continuation of the underline from strictement non.',[299,1793,582,1873],support='half b')
f(35,'Definition, word in the interlinear addition',r'\inserted{si elles sont non panachées, et}',r'si elles sont non parallèles, et',r'\inserted{si elles sont non panachées, et}',False,True,'misread word',False,'high','Half b shows the same panachées word in the added line, with p, low ana, c/h and final ées. The curved leader attaches the entire group before the main-line si. H’s explicit note correctly acknowledges that whole interlinear group, so only the differing word is counted.',[972,1737,1228,1791],support='half b',h_editorial_note='« si elles sont non parallèles, et » est ajouté dans l’interligne')
f(36,'Definition, revised letters in les before quatre',r'\deleted{\unsure{les}}les',r'les',r'l\unsure{\deleted{es}}es',True,True,'deletion state (struck given live or live given struck)',False,'low','Crop 13 has one tall live l loop, followed by a heavy low e/s group with an additional low loop beneath the terminal. No second independent l is visible. I keep the shared l once and retain uncertain older es immediately before the live es; identity and cancellation versus reinforcement remain open.',[755,1791,853,1842],'13',['C037-D018'],'retained')
f(37,'Definition, word and point after distincts',r'\unsure{et.|i.e.}',r'et',r'et.',True,True,'other',False,'high','Crop 14 shows a low e joined to a tall crossed t and a detached round point at the right. The high tall stroke supplies t; the group reads et. The final point is visible and absent from H’s body.',[1138,1864,1210,1910],'14',['C037-D019'],'resolved')
f(38,'Definition, extra curved marks between si and de plus',r'\unsure{((|c}',r'absent',r'\unsure{((|c}',False,True,'omission',False,'medium','Crop 14 separates two nested open curves between the dotted si and de. Their upper ends are close, so a doubled/retraced c remains possible. Both curves are retained with (( first.',[1269,1872,1298,1911],'14',['C037-D020'],'retained')
f(39,'Definition, entre les ensembles',r'entre les ensembles',r'entre ces ensembles',r'entre les ensembles',False,True,'misread word',False,'high','Half b shows a tall looped l before the short es returns in les. H’s ces has no tall initial stroke matching that ink.',[823,2045,911,2124],support='half b')
f(40,'Definition, abbreviation following the dash',r'i.e',r'i.e.\ si',r'i.e',False,True,'other',False,'medium','The half shows a dotted i, a point and an e-like return, then a broad blank before si. There is no detached second point after the e. The written abbreviation is kept as i.e.',[911,1966,994,2015],support='half b')
f(41,'Display (21), after on dit',r'\unsure{donc|alors}',r'donc',r'donc',True,False,'misread word',False,'high','Crop 15 shows a tall looped d followed by low connected on/c strokes. The tall initial supports donc directly; the lower initial and extra letters needed for alors are not present.',[886,2290,962,2337],'15',['C037-D021'],'resolved')
f(42,'Display (21), first Pi subscript',r'\Pi_1',r'\Pi_{1}',r'\Pi_{\unsure{1|2}}',True,False,'misread symbol or index',False,'medium','The first low suffix has a narrow down-going stroke ending in an upward hook near the photograph’s lower edge. It is less separated than the second low 2. Read 1 first and retain 2 as an alternative; the nearby numbered pair does not decide the glyph.',[1063,2313,1092,2347],'15')
# Preserve exact source strings where a surrounding source fragment includes a newline.
F[20]['h']="inverse, or on\n\\uncertain{lit}"
F[24]['h']="\\struck{signifierait que\n$\\Sigma_{12}\\simeq\\Sigma_{1}^{-}$}"
# Extract the literal H i.e. fragment, including its control-space backslash.
F[39]['h']=r'i.e.\ si'
F[39]['c']=r'i.e si'
F[39]['reading']=r'i.e si'

I=[]
def inv(element,kind,bbox,first,hand='his hand',**extra):
 d=dict(element=element,kind=kind,position=bbox,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes');d.update(extra);I.append(d)
inv('Cor heading','text',[235,34,315,99],'Cor',representation=r'\uline{Cor}')
inv('Crossed starter D','deletion',[264,70,347,135],'D',representation=r'\deleted{D}ans')
inv('Opening corollary body','text',[285,88,1532,353],'ans le cas où Card{ }=4')
inv('Opening interlinear inequalities','insertion',[1085,25,1494,165],'et Sigma1-minus not equal X, Sigma2-minus not equal X')
inv('Slanted marginal reformulation','margin note',[22,158,521,978],'Sous forme : Pour que les relations')
inv('Raised contraction in margin','insertion',[259,496,345,580],'mutlt.')
inv('Paired inclusion display','display',[478,392,1052,536],'(*) Sigma1-plus subset Sigma2-minus; Sigma2-plus subset Sigma1-minus')
inv('Proof opening','text',[280,590,1602,752],"En effet, on n'a pas les inclusions inverses")
inv('Opposite-sign same-index relation display','display',[499,757,1553,833],'Sigma1-plus subset Sigma1-minus ou Sigma1-minus subset Sigma1-plus, car on aurait')
inv('Cancelled initial Sigma pair','deletion',[282,859,474,918],'Sigma1-plus, Sigma1-plus')
inv('Proof middle and comparison with diagram (14)','text',[274,849,1647,1413],'Sigma1-minus = X, de =')
inv('Possible older vertical in target Sigma','deletion',[1486,857,1506,900],'vertical stroke',state='possible older stroke; revision/reinforcement open')
inv('Cancelled cela','deletion',[571,1454,662,1501],'cela')
inv('Interlinear la première p.ex.','insertion',[545,1405,1001,1495],'la première p.ex.')
inv('Live signifierait que','text',[713,1447,1180,1558],'signifierait que')
inv('Cancelled Sigma equation','deletion',[1232,1437,1588,1506],'Sigma12 simeq Sigma1-minus')
inv('Cancelled connective before final equation','deletion',[296,1550,408,1606],"d'où")
inv('Proof closing line','text',[452,1537,1427,1623],"Sigma2-minus = X, ce que l'on a exclu")
inv('Definition heading','text',[305,1660,402,1766],'Déf')
inv('Definition paragraph and its inline formulas','text',[298,1671,1654,2282],'On dit que Pi1, Pi2 sont strictement non panachées')
inv('Interlinear definition qualification','insertion',[615,1730,1304,1840],'si elles sont non panachées, et')
inv('Possible overwritten es after shared l','deletion',[779,1804,838,1840],'es',state='identity and deletion versus reinforcement unresolved; common l live once')
inv('Long marginal emphasis rule beside definition','text',[264,1733,287,2314],'vertical emphasis rule',representation=r'\rule[-30ex]{.4pt}{31.5ex}',classification='text emphasis mark; no independent pictorial drawing')
inv('Final display (21)','display',[304,2276,1667,2349],'Sigma1-minus not equal X, Sigma2-minus not equal X; propres; E1, E2')
inv('Archive pencil number','text',[29,2290,90,2340],'36',hand='another unnamed hand, light pencil',representation='% archive sheet number: 36')

notes=[
 {'id':'scan037-note-01','text':'The handwritten sheet contains the heading Cor, its body and two-inclusion display, an oblique marginal reformulation, a proof, and the underlined heading Déf with a long left emphasis rule. No authorial date or separate authorial page number is visible. The light pencil 36 is retained only as archive numbering. H’s page{36} convention refers to the archive’s page unit.'},
 {'id':'scan037-note-02','text':'At the opening, Card is followed by visibly empty braces and =4. The words et and the two inequalities are raised above the line and attached after that comma by a long curve. The display label is (*); its point is present far to the right of the second row. No extra omission is inferred from H’s placement of that terminal point.'},
 {'id':'scan037-note-03','text':'The margin begins “Sous forme :”. It uses the written abbreviated group “il f et s.” and a raised, still uncertain “mutlt.”. The words “strictes” and the fourth low index remain uncertain; the parenthesized asterisk is resolved from its curved boundaries and crossed centre. The four-member mathematical list did not supply its unresolved last index.'},
 {'id':'scan037-note-04','text':'The proof begins “En effet” and contains the literal two-bar abbreviation “de =”. Its remaining task is introduced by the author’s own wording “Il reste à voir”. Later it cites “le diagramme (14)” and ends “ce que l’on a exclu”. These are source statements; no independent proof check of the inclusions or of diagram (14) was performed.'},
 {'id':'scan037-note-05','text':'The proof’s corrections include a cancelled two-Sigma starter, a possible earlier upright in the later target capital, a cancelled cela, the raised la première p.ex., the live signifierait que, a separately crossed Sigma12 simeq Sigma1-minus, and a short cancelled connective tentatively d’où. The curved insertion leader above signifierait was distinguished from the straight cancellation through the equation by its route through the upper rather than the body strokes.'},
 {'id':'scan037-note-06','text':'The second Sigma after puisque has an attached downward foot and no separately readable numeral; bare Sigma is first. Its high sign has a cap and a downward stem, so top is first and plus remains an alternative. The role of the term in the surrounding list was not used to replace those visible features.'},
 {'id':'scan037-note-07','text':'The definition’s repeated written word is panachées. The full raised phrase “si elles sont non panachées, et” is interlinear, as H’s note acknowledges. A single live l in les is shared with the compressed revised ending; it is not duplicated. The terminal point in et. and the two curved marks before de plus are retained. The final display bears (21), the word propres underlined, and the E1/E2 inequalities.'},
 {'id':'scan037-note-08','text':'The final parenthetic reads “on dit donc que”; its d has a distinct tall loop. Pi is read from the common cap and descending stems. First-page case, the R-like curl in the definition’s second Pi, and the compressed first low suffix in (21) remain editorial uncertainties. No mathematical identification of the named objects was used to decide those letterforms.'},
 {'id':'scan037-note-09','text':'H’s explicit notes about the top insertion, the interlinear la première p.ex., the definition addition, and the left rule were read. Those acknowledged states create no new collation difference by themselves. H’s use of emph for the author’s emphasis is treated as its declared convention. The a in a pas still lies outside H’s encoded emphasis and is an actual scope difference.'},
 {'id':'scan037-note-10','text':'No authored question mark, request for verification, or date was observed on this sheet. All unsure marks in reading.tex are editorial accounts of the observed ink. The source’s cancelled and uncertain wording is retained without conjectures, supplementary lemmas, or conditional theorems.'}
]
notation=[
 {'scan':37,'form':r'\operatorname{Card}\{\ \}=4','evidence':'Half a: Card is followed by an opening brace, empty white interval, closing brace, two bars and 4.','reading':r'\operatorname{Card}\{\ \}=4'},
 {'scan':37,'form':'de =','evidence':'Half a: two detached parallel short horizontals occur after de.','reading':r'de $=$'},
 {'scan':37,'form':r'\subset|\in','evidence':'Crop 04: c-shaped open contour, extra left return and short inner upright; no clear independent middle bar.','reading':r'\unsure{\subset|\in}'},
 {'scan':37,'form':'fourth marginal Sigma index','evidence':'Crop 02: the last low suffix is a short down-hook joined to the Sigma foot.','reading':r'\Sigma_{\unsure{1|2}}^-'},
 {'scan':37,'form':'target Sigma/E with extra upright','evidence':'Crop 06: detached cap and angular returns together with a heavy central vertical; lower suffix has a curved roof and downstroke.','reading':r'\unsure{\deleted{\vert}}\unsure{\Sigma|E}_{\unsure{2|1}}^-'},
 {'scan':37,'form':'second Sigma after puisque','evidence':'Crop 07: low bar turns directly downward, without a separate numeral; high sign has a cap and downstem.','reading':r'\unsure{\Sigma|\Sigma_2}^{\unsure{\top|+}}'},
 {'scan':37,'form':r'\simeq','evidence':'Crop 09: high wave and separate low bar, with a longer cancellation passing between them.','reading':r'\simeq'},
 {'scan':37,'form':'Pi case and curled second form','evidence':'Crop 11: first common cap with two stems; second cap curls down and turns into an oblique right branch.','reading':r'\unsure{\Pi|\pi}_1,\unsure{\Pi|R}_2'},
 {'scan':37,'form':'first low Pi suffix in (21)','evidence':'Crop 15: thin low downstroke with upward hook near the photographed lower edge.','reading':r'\Pi_{\unsure{1|2}}'},
 {'scan':37,'form':'two open curves after si','evidence':'Crop 14: nested open curves between si and de.','reading':r'\unsure{((|c}'},
 {'scan':37,'form':'written et.','evidence':'Crop 14: joined low e and tall crossed t, followed by a detached round point.','reading':'et.'},
 {'scan':37,'form':'older es under live les','evidence':'Crop 13: one common l; extra low loop and thick duplicated returns under e/s.','reading':r'l\unsure{\deleted{es}}es'}
]
abbreviations=[
 {'scan':37,'form':'Cor','expansion':'Corollaire'},
 {'scan':37,'form':'Déf','expansion':'Définition'},
 {'scan':37,'form':'f','expansion':'faut'},
 {'scan':37,'form':'s.','expansion':'suffit'},
 {'scan':37,'form':'mutlt.','expansion':'mutuellement (likely; contraction reading remains uncertain)'},
 {'scan':37,'form':'p.ex. / p. ex.','expansion':'par exemple'},
 {'scan':37,'form':'i.e','expansion':'id est'},
 {'scan':37,'form':'= after de','expansion':'même'},
 {'scan':37,'form':'Card','expansion':'Cardinal'}
]
U=[]
def u(place,reading,alts,conf,why,ids=()):
 U.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=why,c_doubt_ids=list(ids)))
u('Margin after relations','strictes',[],'medium','Compressed middle strokes remain inseparable despite the rotated crop.',['C037-D002'])
u('Fourth marginal Sigma index','1',['2'],'low','Low suffix is joined to the capital’s terminal.',['C037-D004'])
u('Raised marginal contraction','mutlt.',[],'low','Several narrow shoulders and the terminal upright do not separate into secure letters.',['C037-D006'])
u('Second same-index relation',r'\subset',[r'\in'],'medium','Additional left return and inner upright obscure the contour.',['C037-D007'])
u('Cancelled two-Sigma starter',r'\Sigma_1^+,\Sigma_1^+',[r'\Sigma_1^+,\Sigma_1^-'],'low','Zigzag cancellation intersects the small indices and signs.',['C037-D008'])
u('Target capital after Sigma2-plus subset',r'\Sigma',['E'],'low','Heavy central upright merges with the angular body.',['C037-D009'])
u('That target’s low numeral','2',['1'],'low','Its curved roof, downstroke and capital base merge.',['C037-D010'])
u('Extra upright through that target',r'\unsure{\deleted{\vert}}',['reinforcement of the live glyph'],'low','Identity as older writing and cancellation state remain open.')
u('Second Sigma after puisque',r'\Sigma',[r'\Sigma_2'],'medium','The foot descends, with no separate numeral.',['C037-D011'])
u('High sign on that Sigma',r'\top',['+'],'medium','Cap and downstem are visible; a minute rise at their junction is unresolved.')
u('Cancelled word before insertion','cela',[],'low','Cancellation and p descender cross the middle/ending.',['C037-D012'])
u('Inserted abbreviation spacing','p.ex.',['p. ex.'],'medium','Points and letters are visible, but the small separation does not settle a word space.',['C037-D014'])
u('Cancelled connective before final equality',"d'où",[],'low','Small raised and low letters are covered by the cancellation.',['C037-D016'])
u('First Pi case',r'\Pi',[r'\pi'],'medium','Common cap and stems do not fix case independently.')
u('Second capital in definition',r'\Pi',['R'],'medium','Curled upper-right stroke and oblique branch give the alternative.')
u('Initial case of strictement','strictement',['Strictement'],'medium','Large initial s loop is joined directly to t.')
u('Old layer in les','es',['reinforcement rather than deleted earlier letters'],'low','Extra loop beneath the e/s group is visible, but one shared l is live.',['C037-D018'])
u('Marks after si','((',['c'],'medium','Two nested open contours have adjoining upper ends.',['C037-D020'])
u('First Pi index in (21)','1',['2'],'medium','Thin hooked suffix is close to the photograph’s lower edge.')

R={
 'scan':37,'reader':'R3','model':'GPT-6 Astra Pro','effort':'inherited; not exposed',
 'start_utc':'2026-11-20 11:28:57 UTC','end_utc':None,
 'start_time_note':'Clock recorded immediately before first image view; supplied textual inputs had already been read.',
 'images_viewed':[
  {'path':str(ROOT/'source/SP41_CW_81_scans/J81-05_81_scan037.jpg'),'role':'whole','actual_viewing_only':True,'views':1,'purpose':'layout inventory'},
  {'path':str(ROOT/'source/SP41_CW_81_scans/J81-05_81_scan037_a.jpg'),'role':'a','actual_viewing_only':True,'views':1,'purpose':'line-by-line reading','whole_image_offset':[0,0]},
  {'path':str(ROOT/'source/SP41_CW_81_scans/J81-05_81_scan037_b.jpg'),'role':'b','actual_viewing_only':True,'views':1,'purpose':'line-by-line reading','whole_image_offset':[0,1100]}
 ],
 'source_inputs_read':[
  str(ROOT/'work/briefs/reader_brief_v07.md'),str(ROOT/'work/briefs/notation_before_scan037.md'),str(ROOT/'runtime_inputs/scan037/packet.json'),str(C),str(H),str(ROOT/'runtime_inputs/scan037/C_context.md'),str(ROOT/'runtime_inputs/scan037/C_doubt_index.tsv'),str(ROOT/'source/SP41_CW_81_witnesses/codex/J81-05/PREAMBLE.tex'),str(ROOT/'source/SP41_CW_81_witnesses/hua/transcripts/preamble/grothendieck.sty')
 ],
 'H_drawings':{'applicable':False,'reason':'The supplied H page contains no drawing, diagram input or drawing reference. No other-page drawing files were opened.'},
 'transcription_file':str(OUT/'reading.tex'),'findings':F,'inventory':I,'notes':notes,'check_events':[],
 'notation':notation,'abbreviations':abbreviations,'unresolved':U,'crop_count':len(crops),'crops':crops,
 'workflow_feedback':{
  'whole_view_count':1,'half_a_view_count':1,'half_b_view_count':1,'enhanced_crop_view_count':15,
  'actual_image_viewing':True,'OCR_used':False,'PDF_text_extraction_used':False,'external_research_used':False,'compiled':False,
  'other_readers_or_root_decisions_opened':False,'other_page_images_opened':False,
  'crop_policy':'Each still-open locus was read from one enhanced crop. Coherent groups share a crop. No target was recropped or re-enlarged after a decision. All output crop widths are 3000 pixels.',
  'rotation':'The complete slanted marginal note was rotated clockwise by 44 degrees within its one crop operation; threshold-based trimming removed outer white padding. Unrelated body context remains at the rotated lower/right edge.',
  'clipping':[
   'Crop 08 cuts the extreme bottom of the long que descender. The complete half b had included its available extent; the whole-image finding bounds extend to y=1558. The word was settled and not recropped.',
   'Crops 11 and 13 truncate portions of already-read interlinear/context letters at their edges; the targeted heading, Pi pair and les are complete.',
   'The final line reaches the source photograph’s lower paper edge. Crop 15 includes that source edge and its black border; the low que descender is source-clipped there.'
  ],
  'storage':'All writes were confined to work/readers/scan037/R3/. reading.tex was completed and saved before return.json composition.',
  'graphic_classification':'There is no independent pictorial drawing or arrow diagram on this sheet. The long vertical mark is a text-emphasis rule, represented beside the definition; the brace belongs to the inclusion display.',
  'verification':'The JSON schema, allowed inventory values, crop bounds and coverage of all 21 C doubt identifiers are checked by a local non-compiling script. No mathematical proof check is claimed.'
 }
}
# Coverage and structural checks only: these do not inspect or recognise image text.
assert {d for x in F for d in x['c_doubt_ids']}=={f'C037-D{x:03d}' for x in range(1,22)}
assert all(x['confidence'] in {'high','medium','low'} for x in F)
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in I)
assert all(0<=x['bbox'][0]<x['bbox'][2]<=1684 and 0<=x['bbox'][1]<x['bbox'][3]<=2361 for x in F)
assert (OUT/'reading.tex').exists()
R['counts']={'findings':len(F),'against_C':sum(x['against_C'] for x in F),'against_H':sum(x['against_H'] for x in F),'C_doubts_covered':21,'C_doubts_resolved':sum(len(x['c_doubt_ids']) for x in F if x['c_doubt_status']=='resolved'),'C_doubts_retained':sum(len(x['c_doubt_ids']) for x in F if x['c_doubt_status']=='retained'),'unresolved_loci':len(U),'crops':len(crops),'inventory_elements':len(I)}
(OUT/'return.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(R['counts'],ensure_ascii=False))
