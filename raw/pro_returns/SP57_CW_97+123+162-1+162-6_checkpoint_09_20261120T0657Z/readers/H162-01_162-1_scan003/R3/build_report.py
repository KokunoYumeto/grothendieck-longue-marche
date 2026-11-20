import json,re
from pathlib import Path
root=Path('out/readers/H162-01_162-1_scan003/R3')
Ctext=Path('packets/H162-01_162-1_scan003/C.tex').read_text()
Htext=Path('packets/H162-01_162-1_scan003/H.tex').read_text()
Rtext=(root/'reading.tex').read_text()
manifest=json.loads((root/'crop_manifest.json').read_text())
def crop(n): return f'readers/H162-01_162-1_scan003/R3/crops/{n}.png' if n else None
def box(n,b=None): return manifest[n] if n else b
D=[]; Q=[]; literal_errors=[]
def diff(place,C,H,reading,evidence,confidence='high',kind='other',cc=True,hc=True,n=None,b=None,mh=None):
    if not reading: raise ValueError(place)
    if C and C not in Ctext and C.replace('\\\n','\\\\\n') in Ctext: C=C.replace('\\\n','\\\\\n')
    if C and C not in Ctext: literal_errors.append(('C',place,C))
    if H and H not in Htext and H.replace('\\n','\n') in Htext: H=H.replace('\\n','\n')
    if H and H not in Htext and H.replace("\\'","'") in Htext: H=H.replace("\\'","'")
    if H and H not in Htext: literal_errors.append(('H',place,H))
    if mh is None: mh=bool(re.search(r'\\(?:uncertain|ill)\b',H))
    D.append(dict(id=f'R3-D{len(D)+1:03}',place=place,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=mh,c_changed=cc,h_changed=hc,crop=crop(n),bbox=box(n,b),bbox_source='whole image, original 1683 by 2150 pixel coordinates'))
def doubt(place,C,reading,evidence,confidence,n,H='',changed=False,kind='other',hchanged=True):
    Q.append(dict(place=place,C=C,decision=reading,evidence=evidence,confidence=confidence,crop=crop(n),bbox=box(n),bbox_source='whole image, original 1683 by 2150 pixel coordinates'))
    if changed or hchanged:
        diff(place,C,H,reading,evidence,confidence,kind,changed,hchanged,n=n)

# Each of C's 48 unsure occurrences and its one illegible occurrence is reconsidered separately.
doubt('Deligne heading: parenthesized suite',r'\unsure{suite}','suite','The lower u arch, dotted i, tall t and right terminal survive the horizontal strike. The parentheses are separate.','high','01_head',r'\emph{(suite)}',True,hchanged=False)
doubt('Thesis surname after Deligne',r'\unsure{Libermann|Libermans}',r'\unsure{Libermann|Libermans}','A tall initial, dotted i and low connected ending survive, but the crossing hides the middle and terminal divisions. The visible ending does not justify Hironaka.','low','01_head','Hironaka',False,'misread word')
doubt('Giraud: lower letter after B',r'\unsure{$B_G$|$B_g$}',r'\unsure{$B_G$|$B_g$}','The large B has a tall upright and two turns; the smaller right-lower loop has a right descending stem, leaving capital G versus g unsettled.','medium','08_BG',r'Notes sur \ill\ 67',False,r'readable ink left as \ill{}')
doubt('Klose: final surname',r'\unsure{Ulmers|Ulmer}',r'\unsure{Ulmers|Ulmer}','Two initial uprights and low intervening loops support Ulmer; the final s-like hook is crossed by the broad lower stroke.','low','09_ulmers','Hartshorne',False,'misread word')
doubt('Upper right: Griffiths',r'\unsure{Griffiths}',r'\unsure{Griffiths}','The opening G arc and several tall shafts are visible; the stain and two cancellations cover the bodies.','low','02_griffiths',r'\uncertain{Griffiths}',False,hchanged=False)
doubt('Upper right: périodes',r'\unsure{périodes}',r'\unsure{périodes}','The p descender and low round bodies survive below the strike; the middle and accent remain partly covered.','low','02_griffiths','périodes')
doubt('After périodes: punctuation',r'\unsure{\ldots|.}',r'\unsure{\ldots|.}','Several pale separated trailing marks are visible, but their status as dots versus a stretched terminal remains uncertain.','low','02_griffiths','')
doubt('Upper right: SGA abbreviation',r'\unsure{SGA|SG}',r'\unsure{SGA|SG}','S/G lower curves survive under the stain and crossing; two tall following strokes favour A but do not resolve it securely.','medium','03_sga','SGA')
doubt('Quillen/Adams: conj.',r'\unsure{conj.}','conj.','An open c, round o, n shoulder, descending j and a small right point are separable.','high','04_conj',r'\uncertain{sém.}',True,'misread word')
doubt('Artin line: initial numeral',r'\unsure{2|2)}','2','The curved upper stroke and lower horizontal form 2. The following crossed diagonals are not a closing parenthesis.','high','05_artin_date','2',True,hchanged=False)
doubt('Artin line: crossing after 2',r'\unsure{x|X}',r'\draw (949,225)--(980,258) (979,222)--(951,261);','Two large diagonal cancellation strokes lie between 2 and lettre. Their character value is not established, so the trace is drawn without assigning x or X.','high','05_artin_date','',True,'drawing or diagram')
doubt('Artin line: lettre',r'\unsure{lettre}','lettre','Tall l, two t shafts, a short r and rounded e survive; there is no separate plural s.','high','05_artin_date','lettres',True,'misread word')
doubt('Date below Artin',r'\unsure{10.3.66|10.5.66}',r'\unsure{10.5.66|10.3.66}','The middle digit has a top stroke and a descending bent lower stroke, favouring 5. Its top meets the enclosing curve and the lower half meets the cancellation; 3 remains possible. Two dot separators and both sixes survive.','medium','05_artin_date','10.I.66',True,'misread symbol or index')
doubt('Second Quillen entry: title',r'\unsure{Deviations|Derivations}','Deviations','After De there is one v-shaped pair of strokes followed by a dotted i; no separate r before that v is visible. The following ations is readable.','high','06_deviations','Derivations',True,'misread word')
doubt('Hartshorne title: dimension ending',r'\unsure{dimension|dimensions}','dimension','The final n returns downward before two detached points; a separate s is not present.','high','07_hartshorne',r'\ill',True,r'readable ink left as \ill{}')
doubt('Hartshorne title: trailing punctuation',r'\unsure{..|\ldots}','..','Two detached dark points follow the final n.','high','07_hartshorne',r'\ill',True,r'readable ink left as \ill{}')
doubt('Schwarzenberger entry: fibrés and possible comma',r'\unsure{fibrés|fibrés,}',r'\unsure{fibrés}','The cancellation still hides some letter tops and the accent. The space after the final s is open and contains no separate comma.','medium','10_fibres','fibrés',True)
doubt('Hatched left label: initial',r'\unsure{N|M}',r'\unsure{M|N}','Two tall sides with a low middle turn favour M; intersecting hatch strokes still admit N.','low','11_label',r'\ill',True,r'readable ink left as \ill{}')
doubt('Hatched left label: remaining covered letters',r'\illegible{1}',r'\illegible{1}','Several lower loops and a final raised curl survive, but the six slanting hatch strokes prevent a stable word reading; one short group is retained as illegible.','low','11_label',r'\ill',False,hchanged=False)
doubt('Hatched central abbreviation',r'\unsure{PTTM|PTT M}','PTTM','P, two separate T caps/stems and M are visible. The spacing before M is comparable to the other letter intervals.','high','12_PTTM',r'\ill',True,r'readable ink left as \ill{}')
doubt('Bertin: photocopies',r'\unsure{photocopies}','photocopies','The two descending p forms, h/t uprights, low o/c loops, dotted i and final s-like turn survive independently of the single crossing.','high','13_photocopies','photocopie',True,'misread word')
doubt('Title before Hakim',r'\unsure{Mme|Mne}','Mme','A large M is followed by the compact low me group; the reduction is an abbreviation, not an expanded word.','high','14_mme_name','Mme',True,hchanged=False)
doubt('Name below Bertin',r'\unsure{Mathieu|Mathies}','Hakim','The first capital has an H cross-connection, followed by a, one tall k stroke, a dotted i and the low final m. The extra tall letters required by Mathieu are absent.','high','14_mme_name','Hakim',True,'misread word',False)
doubt('End of Gabriel entry: Exp',r'\unsure{Exp|Ex.}','Exp','An E and x are followed by a descending p shaft; there is no separate abbreviation point.','high','15_gabriel_seminaire',r'exp.~7',True,'misread word')
doubt('End of Gabriel entry: numeral',r'\unsure{7|\mathrm I}','$7$','The high horizontal cap and oblique descending stroke form 7; a short crossing lies across the middle.','high','15_gabriel_seminaire','7',True,hchanged=False)
doubt('Ferrand: hatched photocopies',r'\unsure{photocopies}',r'\unsure{photocopies}','Two descenders and parts of photo/copies remain, but the dense repeated strokes cover several cells. Retained tentative rather than resolved from the other occurrence.','medium','16_ferrand_photocopies',r'\ill',False,r'readable ink left as \ill{}')
doubt('Dieudonné entry: par.factoriel',r'\unsure{parafactoriel|par.factoriel}',r'\unsure{par.factoriel|parafactoriel}','A small isolated point-like mark precedes the tall f after the initial par group. The highly reduced strokes still permit an a.','medium','17_parafactoriel',r'\ill',True,r'readable ink left as \ill{}')
doubt('Dieudonné entry: en',r'\unsure{en|de}','en','A low opening loop enters a single n shoulder; there is no tall d stem.','high','17_parafactoriel','de',True,'misread word')
doubt('Picard entry: foncteur',r'\unsure{foncteur}','foncteur','The long descending/ascending f loop and the following oncteur run can be separated from the nearby oval; the word is readable.','high','18_picard_hartshorne',r'\ill',True,r'readable ink left as \ill{}')
doubt('Cancelled cohomology entry: letter before -adique',r'\unsure{\ell|l}',r'\unsure{\ell|l}','A small upper loop touches the crossing; it can be a looped ell or ordinary cursive l.','medium','18_picard_hartshorne','')
doubt('Hirzebruch entry: two closing curves',r'\unsure{?\,)|?}',r'?\,)','A short dark closing curve follows the question mark; a second, taller closing parenthesis stands farther right. Both are preserved.','high','19_hirzebruch','?)',True,'misread symbol or index')
doubt('Serre brace, first abbreviation',r'\unsure{équ.}','équ.','The initial accented e, q descender, u turn and terminal point are visible.','high','20_serre_brace',r'\ill',True,r'readable ink left as \ill{}')
doubt('Serre brace: fonction before L',r'\unsure{fonction|fonctions}','fonction','The last small n turns down directly before the detached baseline L; no separate s follows.','high','20_serre_brace','',True,'omission')
doubt('Serre brace: début',r'\unsure{début|défaut}','début','A small upper b loop and following u are present; the long descending f required by défaut is absent.','high','20_serre_brace','début',True,hchanged=False)
doubt('Serre brace: terminal points',r'\unsure{....|\ldots}','....','Two dark points and two paler short points follow monodromie, all separated.','medium','20_serre_brace',r'\ill',True,r'readable ink left as \ill{}')
doubt('Right note: complexes',r'\unsure{complexes}','complexes','A c/o opening, m run, p descender, tall l and exes ending survive the line crossing.','high','21_complexes','opérateurs',True,'misread word')
doubt('Notes Serre formula: baseline letters',r'\unsure{\mathrm{ch}|\mathrm{dh}}',r'\unsure{\mathrm{ch}|\mathrm{dh}}','A low left curve and tall right shaft remain beneath two cancellations. The covered left upper contour leaves c versus d unresolved.','low','22_serre_formula',r'\ill',False,r'readable ink left as \ill{}')
doubt('Notes Serre formula: raised cluster',r'\unsure{n-i|n-1|n-\nu}',r'\unsure{n-i|n-1|n-\nu}','The raised n and a short separating stroke survive; the final small descending turn lacks a securely isolated dot and can be i, 1 or nu.','low','22_serre_formula',r'\ill',False,r'readable ink left as \ill{}')
doubt('Calcul: grouping before P and raised n',r'\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}',r'(\mathrm{P}^{n}','A separate open left parenthesis is followed by a P stem and bowl; n is raised above its right side. The first curve is not joined as a capital C.','high','23_calcul',r'\ill',True,r'readable ink left as \ill{}')
doubt('Calcul: inner capital and short upper stroke',r'\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}',r'\unsure{\mathrm L^{-}|\overline{\mathrm L}}','The capital has a straight upright and a low right foot, fixing L rather than C. A short detached horizontal sits above/right of it; superscript minus is favoured, but overbar placement remains possible.','medium','23_calcul',r'\ill',True,r'readable ink left as \ill{}')
doubt('Kleiman: photocopies initial case',r'\unsure{photocopies|Photocopies}',r'\unsure{photocopies|Photocopies}','The initial loop and low descending shaft favour p, but its upper height and the crossing do not securely exclude P. The remaining photocopies run is visible.','medium','24_kleiman','Manuscrits ?',False,'misread word')
doubt('Chev. entry: grassmanniennes spelling',r'\unsure{grassmanniennes|grassmaniennes}',r'\unsure{grassmanniennes|grassmaniennes}','The initial descending g and following low run survive; the reduced middle humps do not fix whether both n strokes were written.','medium','25_grassmanniennes',r'groupes \ill',False,'misread word')
doubt('Note entry: Agison',r'\unsure{Agison|Agišon}',r'\unsure{Agison|Agišon}','A, descending g, dotted i and son-like ending survive. The short high stroke over the middle can belong to the cancellation or to the letter.','low','26_agison',r'\ill',False,r'readable ink left as \ill{}')
doubt('Note entry: determinant word',r'\unsure{bidéterminants|holodéterminants}',r'\unsure{bidéterminants|holodéterminants}','Several upright/looped initial strokes are crossed. The dé/terminants ending is more recoverable than the initial syllables; both candidates remain.','low','26_agison',r'\ill',False,r'readable ink left as \ill{}')
doubt('Verdier: final sign in SGA group',r'\unsure{SGAA|SGA 4}',r'\unsure{SGAA|SGA 4}','The last two signs both have an apex, two sides and an internal cross stroke; the last also has a returning lower right end compatible with handwritten 4.','medium','27_sgaa','SGA 4')
doubt('Below Verdier: Gabriel',r'\unsure{Gabriel}',r'\unsure{Gabriel}','The opening G, a and tall b/l strokes survive, but the central small letters and right end lie beneath broad strokes and hatching.','medium','28_gabriel','Gabriel')
doubt('Final left recipient',r'\unsure{Terjanian|Terzanian}','Terjanian','The third/fourth letter has a long descending j curve touching the underline, followed by an, a separately dotted i and an.','high','29_terjanian',r'\ill',True,r'readable ink left as \ill{}')
doubt('Final row: Articles ending',r'\unsure{Articles|Article}',r'\unsure{Articles|Article}','The terminal low turn after the l/e group coincides with the cross-line; an s-like end is favoured but a separate s cannot be fixed.','medium','30_articles','Article')
doubt('Final row: subscript after C',r'\unsure{$C_i$|$C_1$}',r'\unsure{$C_i$|$C_1$}','A small lower-right mark and short separate upper stroke are visible after C; the line crosses their junction, leaving i versus 1 open.','medium','30_articles',r'\ill',False,r'readable ink left as \ill{}')

# Additional wording, states, omissions, punctuation and spatial relationships.
diff('Deligne heading cancellation',r'\deleted{\uline{Deligne} (\unsure{suite})\quad \unsure{Libermann|Libermans}, thèse}',r'\textbf{Deligne} \emph{(suite)}',r'\deleted{\uline{Deligne} (suite)}','The same long horizontal crosses the recipient, parenthesis and thesis entry. H leaves the recipient and suite live.','high','deletion state (struck given live or live given struck)',False,True,n='01_head')
diff('Printed IHES letterhead', 'INSTITUT\\\nDES HAUTES ÉTUDES SCIENTIFIQUES\\\n91 - BURES-SUR-YVETTE\\\n928-48-53','', 'INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53','Four printed lines are visible at upper left; the telephone overlaps the handwritten Giraud crossing. H omits the printed block.','high','omission',False,True,b=[138,140,615,324])
diff('Mark before Griffiths: shorter third shaft and nearby point',r'\tikz[baseline=-.45ex]{\draw (0,0)--(.06,.52) (.09,.04)--(.15,.49);}','',r'\draw (935,100)--(946,29) (945,91)--(957,32); \draw (.05,-.55)--(.14,.55); \fill (1176,83) circle[radius=1.4];','Besides the two tall shafts, a shorter nearby shaft survives at their right and a separate small point occurs below the text run. Their function is not assigned.','medium','drawing or diagram',True,True,n='02_griffiths')
diff('SGA line: numeral and its two rules',r'$\overline{\underline{\mathrm{XII}}}$','SGA 6 XIV',r'$\overline{\underline{\mathrm{XII}}}$','The X is followed by two independent uprights, not an I and V. Separate upper and lower rules span XII.','high','misread symbol or index',False,True,n='03_sga')
diff('Chern entry opening and punctuation','Classes de Chern des représentations.','Chern et\nclasses de Chern des représentations','Classes de Chern des représentations.','The entry begins directly with a tall capital C in Classes. No preceding Chern et is written; a terminal point is visible at the right.','high','text not on the page',False,True,b=[968,120,1646,171])
diff('Quillen/Adams colon','Quillen : sur','Quillen sur','Quillen : sur','Two point positions occur between the name and sur; the upper is touched by the crossing.','medium','omission',False,True,n='04_conj')
diff('Artin name and punctuation','lettre} : Artin (sur Atiyah-Adams)',r'lettres à \ill\ sur Atiyah--Adams)','lettre : Artin (sur Atiyah-Adams)','Artin has a tall A and rtin strokes; a colon precedes it and an opening parenthesis precedes sur. H substitutes à and leaves the name unread.','high',r'readable ink left as \ill{}',False,True,n='05_artin_date')
diff('Date: position, cancellation and surrounding curve',r'\inserted{\deleted{\unsure{10.3.66|10.5.66}}}',r'\add{du} 10.I.66',r'\node (date) at (1155,273) {\inserted{\deleted{\unsure{10.5.66|10.3.66}}}};','The date is below Artin, crossed by a separate horizontal, with a thin curved enclosure above/around it. There is no written du. C marks insertion/deletion but linearizes its position and omits the curve; H leaves the date live.','high','insertion or placement',True,True,n='05_artin_date')
diff('Goodman thesis entry',r'Thèse \uline{Goodman}',r'thèse \ill',r'Thèse \uline{Goodman}','The tall initial T and the Goodman G, two o loops, d upright and man ending survive. Goodman has a separate underline.','high',r'readable ink left as \ill{}',False,True,b=[974,282,1378,320])
diff('Quillen Deviations: deletion state',r'\deleted{Quillen \unsure{Deviations|Derivations} \ldots}',r'Quillen, \emph{Derivations} \ill',r'\deleted{Quillen Deviations \unsure{....|...}}','A dark continuous stroke crosses Quillen and the title. H leaves the line uncancelled and inserts a comma after the name.','high','deletion state (struck given live or live given struck)',False,True,n='06_deviations')
diff('Quillen Deviations: terminal marks',r'\ldots',r'\ill',r'\unsure{....|...}','Two points and two short rightward marks follow the title; the last may join the oval. Four versus three source points remains doubtful.','medium','other',True,True,n='06_deviations')
diff('Quillen Deviations: oval',r'\deleted{Quillen \unsure{Deviations|Derivations} \ldots}','',r'\draw (990,333)..controls(1009,316)and(1170,322)..(1283,319)..controls(1394,316)and(1438,315)..(1437,338)..controls(1430,367)and(1200,375)..(1023,360)..controls(1000,355)and(988,344)..(990,333);','A separate thin oval encloses the entire crossed line. Neither witness draws it.','high','drawing or diagram',True,True,n='06_deviations')
diff('Hartshorne title language',r'On Cohomological \unsure{dimension|dimensions}',r'cohomologie', 'On Cohomological dimension..','The English On and capital C followed by ohomological are visible, then dimension and two points. H gives cohomologie among illegible spans.','high','misread word',False,True,n='07_hartshorne',mh=True)
diff('Upper return contours and Hartshorne underline interpretation',r'\uline{On Cohomological \unsure{dimension|dimensions}}','',r'\draw (600,133)--(784,130)..controls(869,129)and(879,152)..(885,236)..controls(890,313)and(891,357)..(924,364)..controls(1110,372)and(1439,363)..(1590,374); \draw (897,347)..controls(904,387)and(905,397)..(934,405)..controls(1075,429)and(1450,416)..(1650,410);','The low rule extends left of Hartshorne and returns upward into a long contour beginning in the blank left area; a second rightward return is visible. It is not encoded solely as an underline on the title.','high','drawing or diagram',True,True,b=[595,125,1657,426])
diff('Giraud entry: extra 67 in H',r'Notes sur \unsure{$B_G$|$B_g$}',r'Notes sur \ill\ 67',r'Notes sur \unsure{$B_G$|$B_g$}','The small right-lower contour belongs with B; no separate two-digit 67 follows it.','high','text not on the page',False,True,n='08_BG')
diff('Klose recipient',r'\uline{Klose}',r'\textbf{\struck{\ill}}',r'\uline{Klose}','The K arms, tall l and low ose sequence are readable in the left label despite the horizontal strike.','high',r'readable ink left as \ill{}',False,True,b=[163,378,306,438])
diff('Algèbre numeral III rules',r'$\overline{\underline{\mathrm{III}}}$','III Bourbaki',r'$\overline{\underline{\mathrm{III}}}$','Three ordinary uprights stand between separate upper and lower horizontal rules.','high','misread symbol or index',False,True,b=[765,444,821,483])
diff('Shih: Rapport',r'Rapport à Bourbaki calcul différentiel','R. Wood à Bourbaki, calcul différentiel','Rapport à Bourbaki calcul différentiel','The initial R leads into a, two descending p strokes and ort. There is no point after R or independent Wood, and no comma after Bourbaki.','high','misread word',False,True,b=[476,530,1403,585])
diff('Schwarzenberger numeral underline',r'\uline{3}','3 articles',r'\uline{3}','The numeral has a separate short lower stroke in addition to the long crossing through the row.','medium','omission',False,True,b=[481,605,519,645])
diff('Hatched label and PTTM: diagonal cancellations',r'\deleted{\uline{\unsure{N|M}\illegible{1}}}\qquad \deleted{\unsure{PTTM|PTT M}}','',r'\draw (187,765)--(203,719) (201,769)--(218,721) (216,771)--(233,727) (233,772)--(252,726) (251,773)--(268,743) (270,775)--(286,751); \draw (451,772)--(490,709) (482,766)--(522,714) (511,763)--(551,711) (546,762)--(579,715) (582,766)--(618,721) (602,768)--(626,735);','Six oblique hatch strokes cross each short group. They are distinct from the underline of the left label and leave Papiers Atiyah live on the same row.','high','drawing or diagram',True,True,b=[166,700,630,785])
diff('Atiyah row underlines and abbreviation',r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}',r'Papiers Atiyah, topologie et opérateurs\nelliptiques',r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}','Two separate lines run below Papiers Atiyah; topologie and op. elliptiques each have one. The written abbreviation is op.; no comma separates Atiyah and topologie.','high','abbreviation expanded or spelling modernised',False,True,b=[650,680,1645,784])
diff('Bertin EGA IV rules and photocopies punctuation',r'EGA $\overline{\underline{\mathrm{IV}}}$ 16--19',r'EGA IV 16--19, photocopie',r'EGA $\overline{\underline{\mathrm{IV}}}$ 16--19 photocopies','IV has independent top/base rules. The space after 19 has no comma; the photocopies ending has a final s.','high','misread symbol or index',False,True,b=[478,800,1159,861])
diff('Mme Hakim: schémas and accent uncertainty','deux schémas,','deux séminaires,',r'deux sch\unsure{é|e}mas,','After deux the word has the compact sch...mas run, not the longer séminaires. The crossing leaves the accent over e insecure. A separate comma follows.','medium','misread word',True,True,n='15_gabriel_seminaire')
diff('Cancellation shared by Bertin and Mme Hakim entries',r'\deleted{\unsure{Mme|Mne} \uline{\unsure{Mathieu|Mathies}}\qquad Séminaire Gabriel deux schémas, \unsure{Exp|Ex.} $\unsure{7|\mathrm I}$}','',r'\draw[line width=.5pt] (198,838)..controls(205,905)and(217,961)..(232,980)--(276,852)..controls(314,957)and(352,1000)..(480,857)..controls(528,979)and(561,1001)..(678,872)..controls(724,969)and(761,988)..(882,852)..controls(916,939)and(970,952)..(1048,848)..controls(1081,884)and(1121,908)..(1183,901);','One broad series of connected troughs crosses the space and both rows, with a separate upper return at the photocopies end. Linear per-entry strike macros omit this shared extent.','high','drawing or diagram',True,True,b=[188,805,1402,1007])
diff('Ferrand EGA IV rules',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20,21','EGA IV 20, 21',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20,21','IV has a distinct top and base rule, independent of the diagonal cancellation across the row.','high','misread symbol or index',False,True,b=[525,1060,822,1109])
diff('Ferrand: épreuves and dense deletion',r'\deleted{\unsure{photocopies}} épreuves',r'\struck{\ill}',r'\deleted{\unsure{photocopies}} épreuves','Épreuves is readable to the right of the separately hatched photocopies, and the outer long strike crosses both. H leaves the continuation illegible.','high',r'readable ink left as \ill{}',False,True,n='16_ferrand_photocopies')
diff('Ferrand photocopies hatch strokes',r'\deleted{\unsure{photocopies}}','',r'\draw[line width=.4pt] (899,1080)--(921,1056)--(911,1080)--(940,1054)--(928,1080)--(959,1054)--(944,1076)--(976,1054)--(960,1076)--(992,1054)--(980,1077)--(1014,1054)--(1000,1077)--(1034,1055)--(1020,1075)--(1055,1054)--(1043,1077)--(1075,1055)--(1067,1076)--(1100,1055)--(1086,1076)--(1134,1056);','A dense repeated diagonal run crosses photocopies in addition to the long row cancellation. The two states are retained separately.','high','drawing or diagram',True,True,n='16_ferrand_photocopies')
diff('Dieudonné entry: colon and abbreviation','Lettre : Dieudonné','Lettre à\nDieudonné', 'Lettre : Dieudonné','Two detached points follow Lettre. There is no accented à.','high','misread symbol or index',False,True,b=[526,1132,977,1189])
diff('Dieudonné entry: dim','dim 2','dimension 2','dim 2','Only d, dotted i and m precede 2; the expansion dimension is not written.','high','abbreviation expanded or spelling modernised',False,True,n='17_parafactoriel')
diff('Notes sur R.R. oval and external question mark',r'\tikz[baseline=(rr.base)]{\node[inner sep=2pt] (rr) {\deleted{Notes sur R.R.}};\draw (rr.center) ellipse [x radius=3.1em,y radius=.74em];}\ ?',r'\add{entouré, suivi d\'un point d\'interrogation}',r'\node (rr) at (548,1236) {\deleted{Notes sur R.R.}}; \draw (531,1223)..controls(520,1180)and(851,1165)..(872,1207)..controls(892,1251)and(551,1266)..(531,1223); \node at (892,1229) {?};','A thin oval surrounds the cancelled entry; the question mark is outside at its right. H mentions these graphically in an editorial add rather than transcribing the marks.','high','drawing or diagram',False,True,n='18_picard_hartshorne')
diff('Picard title underlining and point',r'\uline{sur cat. de Picard} .',r'sur cat.\ de Picard',r'\uline{sur cat. de Picard} .','The whole sur cat. de Picard group has a separate underline. A detached final point lies farther right.','high','omission',False,True,n='18_picard_hartshorne')
diff('Raised Hartshorne/Goodman entry: Hartshorne name',r'Papiers Hartshorne (dim. coh.) et Goodman',r'Papiers \uncertain{Hertzbrouck}',r'Papiers Hartshorne (dim. \unsure{coh.|ch.}) et Goodman','The tall H, art, shorn sequence and ending e occur in the added line. H places a different doubtful surname into its corresponding entry.','high','misread word',False,True,n='18_picard_hartshorne')
diff('Raised Hartshorne/Goodman entry: middle abbreviation uncertainty','dim. coh.','',r'dim. \unsure{coh.|ch.}','Dim. is legible. In the next small group an open low curve and tall h survive, but a separate intervening o is not fixed. The supplied unmarked coh. is made local and tentative.','medium','other',True,True,n='18_picard_hartshorne')
diff('Raised Hartshorne/Goodman entry: Goodman name','et Goodman',r'\add{et} Godement','et Goodman','Goodman has G, two o bodies, a d upright and man ending. No middle e/t sequence for Godement is visible.','high','misread word',False,True,n='18_picard_hartshorne')
diff('Raised Hartshorne/Goodman entry: placement and live state',r'\inserted{Papiers Hartshorne (dim. coh.) et Goodman}',r'\struck{Papiers \uncertain{Hertzbrouck}}',r'\node[rotate=3] (insertedpapers) at (638,1295) {\inserted{Papiers Hartshorne (dim. \unsure{coh.|ch.}) et Goodman}};','The line begins above and to the right of cancelled Notes cohomologie and rises toward Goodman. Its text is live; the strong line below belongs to the cohomology entry. C marks insertion but does not raise it. H assigns a cancellation and moves the final words beside Picard.','high','insertion or placement',True,True,n='18_picard_hartshorne')
diff('Cancelled cohomology entry wording',r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}','',r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}','The underlying line begins Notes and contains the cohomologie run before the looped letter and -adique. It is separately crossed beneath the added papers line. H omits this source entry.','high','omission',False,True,n='18_picard_hartshorne')
diff('Hirzebruch: Papier and Congrès case','Papier Hirzebruch (Congrès',r'Papiers Hirzebruch (congrès',r'Papier Hirzebruch (Congrès','The first word ends in an r-like terminal without a further s. Congrès begins with a large capital C.','high','misread word',False,True,n='19_hirzebruch')
diff('Serre entry: unwritten sur',r'Lettre : Serre',r'\add{sur}','Lettre : Serre','The name leads directly to a brace with two subjects. No written sur is inserted beside it.','high','text not on the page',False,True,n='20_serre_brace')
diff('Serre entry: fonctionnelle singular',r'fonctionnelle',r'fonctionnelles,','fonctionnelle','The word ends in the low e after two l shafts, with no final s or following comma; another word fonction follows on the same line.','high','misread word',False,True,n='20_serre_brace')
diff('Serre entry: baseline L and left brace',r'\left\{\begin{array}{l}',r'Lettre : Serre \add{sur} \ill\ fonctionnelles, suite, début de monodromie \ill',r'\node[rotate=3] (serretop) at (886,1438) {équ. fonctionnelle fonction $L$}; \draw (860,1407)..controls(852,1431)and(871,1446)..(851,1450)..controls(868,1457)and(860,1481)..(862,1505);','A large separate L shares the first subject baseline. A left brace groups that subject with suite, début de monodromie on the second line. H loses both the L and grouping.','high','drawing or diagram',False,True,n='20_serre_brace')
diff('Right Deligne note: source placement and shared strike',r'\margin{\noindent\vrule height 1ex depth 4.8ex width .35pt\hspace{.2em}\parbox[t]{.86\linewidth}{\deleted{Lettre Deligne \unsure{complexes} elliptiques}}}',r'lettre\nDeligne sur opérateurs elliptiques',r'\node (elliptiques1) at (1254,1492) {\deleted{Lettre Deligne complexes}}; \node (elliptiques2) at (1380,1524) {\deleted{elliptiques}}; \draw (1237,1469)--(1243,1623);','The note is two staggered rows at the right, alongside the Serre/Berthelot transition, with a long vertical stroke on its left. Its top cancellation is continuous with the Berthelot row; the second line has a separate short cancellation. No sur is written.','high','insertion or placement',True,True,b=[1234,1451,1660,1626])
diff('Notes RR entry: no points between letters','Notes RR (copie de Serre)',r'Notes R.R.\ (copie de Serre)','Notes RR (copie de Serre)','Both R capitals stand next to each other with no separate punctuation points, unlike the circled R.R. above.','high','misread symbol or index',False,True,b=[535,1547,1155,1602])
diff('Notes Serre formula: equality and zero',r'=0',r'Notes Serre sur \ill',r'${\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0$','After the raised cluster are two short horizontal equality strokes and a baseline closed oval. These remain legible despite the cancellations.','high',r'readable ink left as \ill{}',False,True,n='22_serre_formula')
diff('Calcul formula full extent',r'Calcul $K\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}(\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}))$',r'Calcul \ill',r'Calcul $K(\mathrm{P}^{n}(\unsure{\mathrm L^{-}|\overline{\mathrm L}}))$','K, the P with raised n, the inner L and both closing parentheses are present. H leaves the whole formula unread. No computation follows this list reference.','high',r'readable ink left as \ill{}',True,True,n='23_calcul')
diff('Rapport Serre: no comma after name','Rapport Serre représentations de groupes finis','Rapport Serre,\nreprésentations de groupes finis','Rapport Serre représentations de groupes finis','The name is followed directly by the word représentations, with no separate low comma in the gap.','medium','text not on the page',False,True,b=[591,1646,1459,1708])
diff('Kleiman EGA IV rules',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20','EGA IV 20',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20','IV has separate cap and base strokes, not merely the broad row cancellation.','high','misread symbol or index',False,True,n='24_kleiman')
diff('EGA V numeral rules',r'EGA $\overline{\underline{\mathrm{V}}}$','EGA V',r'EGA $\overline{\underline{\mathrm{V}}}$','A V is written between independent upper and lower rules on its own cancelled line.','high','misread symbol or index',False,True,b=[830,1736,1041,1779])
diff('Chev. abbreviation and tentative point','Chev.','Chevalley',r'Chev\unsure{.}','Only the short Chev group is written. A possible terminal point is difficult to separate from the crossing/terminal, so it is retained with local doubt.','medium','abbreviation expanded or spelling modernised',True,True,n='25_grassmanniennes')
diff('Agison entry: singular Note',r'Note \unsure{Agison|Agišon}',r'Notes \ill',r'Note \unsure{Agison|Agišon}','The low e is followed by space before the name; there is no additional s turn.','high','misread word',False,True,n='26_agison')
diff('Problèmes entry cancellation',r'\deleted{Problèmes de Géométrie Algébrique}',r'\emph{Problèmes de Géométrie Algébrique}',r'\deleted{Problèmes de Géométrie Algébrique}','A horizontal cancellation cuts through the whole phrase, with the larger descending strokes crossing it as well. H marks it only typographically live.','high','deletion state (struck given live or live given struck)',False,True,b=[551,1844,1215,1899])
diff('Verdier entry: cancelled body and personal copy wording',r'\deleted{\uline{Verdier}\qquad \unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}',r'SGA 4 fasc.~1, \ill',r'\deleted{\unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}','The long crossing passes through both the recipient and the body. Mon exemplaire personnel is visible across the right portion. H leaves the body live and its final words unread.','high','deletion state (struck given live or live given struck)',False,True,b=[232,1881,1606,1965])
diff('Gabriel ending: local hatching',r'\deleted{\unsure{Gabriel}}','',r'\draw (707,1953)--(721,1967)--(727,1952)--(740,1970)--(748,1955)--(759,1972)--(769,1957)--(779,1970);','Small irregular cross-hatching at the right of the already crossed Gabriel entry is distinct from the large diagonal and the main horizontal.','medium','drawing or diagram',True,True,n='28_gabriel')
diff('Final row: Greenberg name','Greenberg',r'\uncertain{Grünberg}','Greenberg','The opening G is followed by r, two low e turns, n, a tall b and erg. No umlaut points occur over the initial vowel group.','high','misread word',False,True,n='30_articles')
diff('Lower list cancellation coverage across recipients and entries',r'\deleted{\uline{Berthelot}\qquad Notes sur stratifications}','',r'\draw (283,1551)--(570,1981); \draw (658,1554)--(947,1998); \draw (979,1551)--(1217,1977); \draw (1284,1521)--(1424,1843); \draw[line width=.45pt] (564,1719)..controls(568,1818)and(580,2026)..(607,2054)..controls(626,2024)and(713,1744)..(738,1699)..controls(770,1768)and(790,1970)..(888,2029)..controls(919,2002)and(1025,1745)..(1052,1699)..controls(1066,1824)and(1086,1977)..(1139,2003)..controls(1176,2004)and(1332,1694)..(1367,1657)--(1442,2042);','Several slender diagonals cross rows, and a broad repeated return traverses the lower group from Kleiman through the final Articles line. A separate outer right curve reaches the bottom. Per-entry deletion wrappers alone do not preserve their extent and intersections.','high','drawing or diagram',True,True,b=[215,1517,1608,2063])

# Inventory: every physical text block, then its cancellation state and the distinct graphical additions.
I=[]
def inv(element,kind,b,first,hand='principal manuscript hand; personal attribution not independently established',state=None):
    row=dict(sheet_kind='list',hand=hand,element=element,kind=kind,position=dict(bbox=b,bbox_source='whole image, 1683 by 2150 pixels'),first_words_or_objects=first,transcribed='yes')
    if state: row['source_state']=state
    I.append(row)
texts=[
('Deligne and thesis entry',[165,25,931,91],'Deligne (suite); Libermann, thèse',True),
('Printed letterhead',[137,139,616,325],'INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53',False),
('Giraud entry overlapping telephone',[164,282,816,350],'Giraud; Notes sur B_G/B_g',True),
('Klose entry',[160,374,895,440],'Klose; lettre sur Ulmers/Ulmer',True),
('Algèbre/Bourbaki entry',[475,443,1063,490],'Notes Algèbre III Bourbaki',True),
('Griffiths entry',[970,22,1450,88],'Griffiths périodes ...',True),
('SGA entry',[969,85,1224,136],'SGA/SG 6 XII',True),
('Chern entry',[969,120,1652,174],'Classes de Chern des représentations.',True),
('Quillen/Adams entry',[968,164,1546,211],'Quillen : sur conj. de Adams',True),
('Artin entry',[918,202,1666,265],'2; lettre : Artin (sur Atiyah-Adams)',True),
('Date below Artin',[1123,244,1327,291],'10.5.66/10.3.66',True),
('Goodman thesis entry',[975,281,1380,322],'Thèse Goodman',True),
('Quillen Deviations entry',[984,313,1460,370],'Quillen Deviations .... / ...',True),
('Hartshorne title entry',[992,366,1665,423],'Hartshorne On Cohomological dimension..',True),
('Shih recipient and report',[180,525,1413,590],'Shih; Rapport à Bourbaki calcul différentiel',False),
('Schwarzenberger articles entry',[481,589,1586,653],'3 articles Schwarzenberger sur fibrés vectoriels',True),
('PTT Grenoble summary entry',[496,644,970,690],'Résumé PTT Grenoble',False),
('Hatched left label',[166,700,303,783],'M/N and unread group',True),
('Hatched PTTM group',[444,700,628,783],'PTTM',True),
('Atiyah papers entry',[650,680,1646,784],'Papiers Atiyah topologie et op. elliptiques',False),
('Bertin recipient and EGA entry',[187,798,1161,872],'Bertin; EGA IV 16--19 photocopies',True),
('Mme Hakim recipient and Gabriel seminar entry',[108,889,1424,1011],'Mme Hakim; Séminaire Gabriel deux schémas/schemas, Exp 7',True),
('Ferrand recipient',[222,1077,438,1128],'Ferrand 1',False),
('Ferrand EGA continuation',[525,1031,1374,1111],'EGA IV 20,21 photocopies épreuves',True),
('Dieudonné letter entry',[526,1097,1631,1192],'Lettre : Dieudonné sur par.factoriel/parafactoriel en dim 2',False),
('Circled R.R. entry',[527,1177,914,1261],'Notes sur R.R. ?',True),
('Picard functor entry',[535,1177,1630,1285],'Notes sur le foncteur dét. / sur cat. de Picard .',False),
('Jouanolou recipient',[227,1291,497,1358],'Jouanolou 1',False),
('Raised Hartshorne and Goodman papers line',[631,1220,1601,1310],'Papiers Hartshorne (dim. coh./ch.) et Goodman',False),
('Cancelled cohomology line',[558,1270,1193,1325],'Notes cohomologie ell/l-adique',True),
('Hirzebruch congress paper entry',[550,1321,1577,1410],"Papier Hirzebruch (Congrès d'Amsterdam ? ) )",False),
('Serre letter with two subjects',[540,1381,1442,1506],'Lettre : Serre; équ. fonctionnelle fonction L; suite, début de monodromie ....',False),
('Berthelot recipient and stratifications entry',[188,1488,1007,1553],'Berthelot; Notes sur stratifications',True),
('Right Deligne elliptic complexes note',[1234,1451,1660,1626],'Lettre Deligne complexes / elliptiques',True),
('Notes RR entry',[535,1547,1157,1603],'Notes RR (copie de Serre)',True),
('Notes Serre formula entry',[536,1558,1035,1639],'Notes Serre sur ch/dh raised n-i/n-1/n-nu =0',True),
('Calcul K entry',[546,1620,909,1689],'Calcul K(P^n(L with upper stroke))',True),
('Serre finite group representations entry',[591,1646,1459,1712],'Rapport Serre représentations de groupes finis',True),
('Kleiman recipient and photocopies entry',[215,1682,1160,1767],'Kleiman; photocopies/Photocopies EGA IV 20',True),
('EGA V entry',[830,1736,1041,1780],'EGA V',True),
('Chev. grassmanniennes entry',[548,1776,1408,1845],'Notes Chev. sur grassmanniennes/grassmaniennes',True),
('Agison determinant entry',[548,1825,1063,1884],'Note Agison/Agišon bidéterminants/holodéterminants',True),
('Algebraic geometry problems entry',[551,1844,1215,1900],'Problèmes de Géométrie Algébrique',True),
('Verdier and personal fascicle entry',[232,1881,1607,1966],'Verdier; SGAA/SGA 4 fasc. 1, mon exemplaire personnel',True),
('Gabriel entry',[553,1945,795,1999],'Gabriel',True),
('Final Terjanian and Greenberg entry',[228,2001,1548,2087],'Terjanian; Articles/Article Greenberg sur C_i/C_1',True)
]
for label,b,first,deleted in texts:
    hand='printed letterhead' if label=='Printed letterhead' else 'principal manuscript hand; personal attribution not independently established'
    inv(label,'margin note' if label=='Right Deligne elliptic complexes note' else ('insertion' if label in ['Date below Artin','Raised Hartshorne and Goodman papers line'] else 'text'),b,first,hand,'cancelled' if deleted else 'live')
    if deleted: inv(label+' cancellation','deletion',b,first)
for label,b,first in [
('Two tall shafts, shorter third shaft and detached point before/below Griffiths',[931,20,1184,104],'two long shafts; shorter uncertain shaft; separate point'),
('Artin cross and detached low point',[923,216,987,271],'two crossing diagonals; low point'),
('Date enclosing curve',[1123,239,1326,294],'thin hooked enclosure around the lower date'),
('Quillen Deviations oval',[984,312,1461,373],'thin closed contour around cancelled title'),
('Long upper return contours',[595,125,1657,426],'left horizontal, descending return and two lower rightward tails'),
('Hatched left label: six slants',[166,700,303,783],'six diagonal strokes with independent underline'),
('Hatched PTTM: six slants',[444,700,628,783],'six diagonal strokes'),
('Atiyah underlines',[650,680,1646,784],'double under Papiers Atiyah, single under topologie and op. elliptiques'),
('Bertin/Mme Hakim connected cancellation',[188,805,1402,1007],'repeated troughs spanning two rows; upper return at right'),
('Ferrand photocopies extra dense hatching',[881,1031,1149,1100],'repeated diagonals within outer row cancellation'),
('R.R. oval and question',[527,1177,914,1261],'thin oval plus external question mark'),
('Serre left brace',[842,1403,875,1508],'two-subject left brace'),
('Deligne note vertical stroke',[1234,1467,1248,1626],'vertical left stroke; separate cancellation of second row'),
('Gabriel ending hatching',[702,1948,787,1983],'small irregular mesh at right ending'),
('Lower long diagonal cancellations',[274,1517,1430,2005],'four long diagonals and a small angled spur'),
('Lower broad repeated cancellation and outer return',[555,1638,1608,2063],'three large return troughs; rising limbs; descending right terminal; outer right curve')]: inv(label,'drawing',b,first)
inv('Detached 1 beside Shih','text',[322,530,345,566],'1','pale handwritten numeral, possibly pencil')
inv('Detached 1 beside Jouanolou','text',[470,1291,495,1331],'1','pale handwritten numeral, possibly pencil')
inv('Detached 1 beside Ferrand','text',[410,1077,440,1115],'1')
inv('Archive sheet number, preserved as comment only','text',[49,2054,113,2127],'2','pencilled archive hand')

remaining=[]
for q in Q:
    reading=q['decision']
    if '\\unsure' in reading or '\\illegible' in reading:
        remaining.append(dict(place=q['place'],reading=reading,alternatives=reading[reading.find('{')+1:reading.rfind('}')].split('|') if '\\unsure' in reading else ['unread covered word'],confidence=q['confidence']))
remaining += [
 dict(place='Shorter shaft beside the two tall upper-right shafts',reading='drawn shorter shaft with local unsure wrapper',alternatives=['part of adjacent graphic','independent trace; function unidentified'],confidence='low'),
 dict(place='Quillen Deviations terminal marks',reading=r'\unsure{....|...}',alternatives=['four points','three points; last mark belongs to oval'],confidence='medium'),
 dict(place='Gabriel seminar entry accent in schémas',reading=r'sch\unsure{é|e}mas',alternatives=['schémas','schemas'],confidence='medium'),
 dict(place='Raised papers line small abbreviation',reading=r'\unsure{coh.|ch.}',alternatives=['coh.','ch.'],confidence='medium'),
 dict(place='Chev. terminal point',reading=r'Chev\unsure{.}',alternatives=['abbreviation point','terminal/cancellation trace'],confidence='medium')
]
notes=[
'The sheet records recipients and titles of notes, letters, papers, theses and photocopies. It is a distribution/inventory list; it does not perform a mathematical computation or supply a proof.',
'The live recipient headings include Shih, Ferrand and Jouanolou, each with a detached 1. Many other headings and titles are crossed. Long cancellations connect multiple entries, especially Bertin/Mme Hakim and the entire lower block.',
'The printed letterhead is INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53. The lower-left archive mark is 2 and is kept only in the required comment. Its agreement with H page 2 is metadata, not a reading difference.',
'The only numeral group read as a date is the cancelled small insertion below the Artin entry: first candidate 10.5.66, with 10.3.66 retained. H reads 10.I.66 and supplies an editorial discussion; no historical conclusion is drawn here.',
'The explicit source hesitations are the question mark outside the circled Notes sur R.R. and the question mark in Congrès d\'Amsterdam ? ) ). The latter is followed by two visibly separate closing curves, preserved as written.',
'The added Papiers Hartshorne (dim. coh./ch.) et Goodman line is physically raised above cancelled Notes cohomologie ell/l-adique. The continuation et Goodman is not moved into the Picard sentence.',
'All C/H agreements were read from the supplied ink, including the letterhead, PTT Grenoble, the three detached numerals, abbreviations, underlines, cancellation states, RR versus R.R., and the barred Roman numerals. The current-page non-doubt rows of C_questions are covered by these checks and the notation entries.',
'Unresolved covered letters are retained locally. A change in uncertainty is distinguished from a demonstrated different word by the kind and evidence fields. H editorial additions describing a graphic are identified as such; they are not treated as source words.',
'Graphic paths are diplomatic approximations of observed extent and contact. Source-sized coordinates anchor them to the text rows; no mathematical or chronological meaning is assigned to the cancelling curves.',
'The corrected C_questions packet was reread after the parent reported its repair; removed out-of-page snippets were not used.'
]
notation=[
 dict(form='Barred Roman numerals',reading=r'\overline{\underline{\mathrm{XII}}}, \overline{\underline{\mathrm{III}}}, \overline{\underline{\mathrm{IV}}}, \overline{\underline{\mathrm{V}}}',places=['SGA line','Algèbre Bourbaki','Bertin EGA','Ferrand EGA','Kleiman EGA','EGA V'],evidence='Ordinary handwritten uprights/diagonals with independent top and bottom rules; XII has two I shafts after X.'),
 dict(form='Giraud subscript',reading=r'\unsure{B_G|B_g}',places=['Notes sur'],evidence='Capital B followed by smaller lower-right loop; case of the lower glyph unresolved.'),
 dict(form='Cohomology letter',reading=r'\unsure{\ell|l}',places=['cancelled cohomology entry'],evidence='Looped tall letter adjacent to cancellation.'),
 dict(form='Serre letter L',reading='L',places=['first braced subject'],evidence='Large ordinary handwritten L on the baseline after fonction; no index, bar or superscript.'),
 dict(form='Notes Serre formula',reading=r'{\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0',places=['lower cancelled note'],evidence='Covered baseline cluster and raised small cluster; equality and final oval retained.'),
 dict(form='Calcul reference',reading=r'K(\mathrm P^n(\unsure{\mathrm L^{-}|\overline{\mathrm L}}))',places=['lower Calcul entry'],evidence='Ordinary K and P; independent raised n; definite L and detached upper-right short rule.'),
 dict(form='Final C subscript',reading=r'\unsure{C_i|C_1}',places=['Greenberg entry'],evidence='Lower-right short stroke with another upper mark, crossed by cancellation.'),
 dict(form='Underline count',reading=r'\uuline{Papiers Atiyah}; \uline{topologie}; \uline{op. elliptiques}',places=['Atiyah row'],evidence='Two parallel rules under first phrase, one under each later group.'),
 dict(form='RR punctuation',reading='R.R. / RR',places=['circled Ferrand-area note','lower Berthelot-area note'],evidence='First pair has separate points; lower pair does not.'),
 dict(form='Nonalphabetic cancellation marks',reading='TikZ paths, no character value assigned',places=['before Griffiths','after 2 before lettre','two hatch groups','cross-entry contours','lower diagonal/wavy paths'],evidence='Source graphic traces reproduced rather than normalized as mathematical symbols.')
]
abbreviations=[
 dict(form='conj.',expansion='conjecture (editorial expansion)'),
 dict(form='Mme',expansion='Madame (editorial expansion)'),
 dict(form='Exp',expansion='exposé (editorial expansion)'),
 dict(form='op.',expansion='opérateurs (editorial expansion)'),
 dict(form='dét.',expansion='déterminant (editorial expansion; contextual)'),
 dict(form='cat.',expansion='catégorie or catégories (editorial expansion; number unspecified)'),
 dict(form='dim',expansion='dimension (editorial expansion; no point supplied in transcription)'),
 dict(form='dim.',expansion='dimension (editorial expansion)'),
 dict(form='coh.|ch.',expansion='cohomologique if coh. is the reading (editorial tentative expansion)'),
 dict(form='équ.',expansion='équation (editorial expansion)'),
 dict(form='fasc.',expansion='fascicule (editorial expansion)'),
 dict(form='Chev.',expansion='Chevalley (editorial suggestion from H; source writes only the short form, with doubtful point)'),
 dict(form='PTT / PTTM',expansion='no secure expansion established from this sheet (editorial statement)')
]
report=dict(page='H162-01_162-1_scan003',reader='R3',viewed=dict(whole='source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003.jpg',a='source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003_a.jpg',b='source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003_b.jpg'),reading_file='out/readers/H162-01_162-1_scan003/R3/reading.tex',differences=D,c_doubts=Q,inventory=I,remaining_doubts=remaining,notes=notes,notation=notation,abbreviations=abbreviations,math_checks=[dict(scope='small formula references in the list',performed='Symbol-by-symbol visual comparison only: baseline versus raised positions, grouping, bars, equals sign and zero were checked against the ink.',result='No theorem or computation is performed on the source page. No proof was attempted or claimed, and no reading was repaired from mathematical expectations.')],crop_count=30,workflow_feedback=['Whole image viewed once; each supplied half viewed once; 30 distinct tight enlarged crops viewed once each. No recrops, OCR, recognition, web, other pages, other reader/root files or subagents used.','reading.tex was saved before report construction. No optional TeX compilation was performed.','The page requires shared source-coordinate drawing paths to preserve cancellations spanning several rows; isolated deletion wrappers would omit that information.'])
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Saved report:',len(D),'differences,',len(Q),'C doubt occurrences,',len(I),'inventory rows,',len(remaining),'remaining doubts.')

for err in literal_errors: print(repr(err))
