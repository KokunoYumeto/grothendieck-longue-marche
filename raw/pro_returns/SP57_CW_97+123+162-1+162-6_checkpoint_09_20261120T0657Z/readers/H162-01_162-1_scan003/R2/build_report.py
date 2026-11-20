from pathlib import Path
import json,re
root=Path('out/readers/H162-01_162-1_scan003/R2')
C=Path('packets/H162-01_162-1_scan003/C.tex').read_text()
H=Path('packets/H162-01_162-1_scan003/H.tex').read_text()
manifest=[json.loads(x) for x in (root/'crops/crop_manifest.jsonl').read_text().splitlines()]
crops={int(x['dest'].split('_')[0]):x for x in manifest}
errors=[]
def lit(s,q):
    if not q:return ''
    m=re.search(r'\s+'.join(re.escape(x) for x in q.split()),s)
    if m:return m.group(0)
    errors.append(q)
    return q
D=[]
def d(place,c,h,r,e,box=None,crop=None,conf='high',kind='misread word',cc=False,hc=True):
    if crop:
        box=crops[crop]['box'];path='readers/H162-01_162-1_scan003/R2/crops/'+crops[crop]['dest'];src='whole'
    else:path=None;src='whole; observed in a' if box and box[1]<995 else 'whole; observed in b'
    D.append(dict(id=f'R2-{len(D)+1:03d}',place=place,C=lit(C,c),H=lit(H,h),reading=r,evidence=e,confidence=conf,kind=kind,marked_in_H=bool(re.search(r'\\(?:uncertain|ill)\b',h)),c_changed=cc,h_changed=hc,crop=path,bbox=box,bbox_source=src))

d('Head: cancellation of Deligne and suite',r'\deleted{\uline{Deligne} (\unsure{suite})\quad \unsure{Libermann|Libermans}, thèse}',r'\textbf{Deligne} \emph{(suite)}',r'\deleted{\uline{Deligne} (\unsure{suite})}', 'The long dark horizontal crosses the name and parenthesis before continuing through the surname. The terminal of suite remains partly covered; H has no uncertainty marker.',[166,27,930,97],kind='deletion state (struck given live or live given struck)')
d('Head: crossed surname',r'\unsure{Libermann|Libermans}',r'\struck{Hironaka, thèse}',r'\unsure{Libermann|Libermans}', 'Tall initial with adjoining dotted short stroke and low repeated terminal humps; the covered middle does not establish Hironaka. Retain C alternatives, without treating the name as certain.',crop=1,conf='low')
d('Printed letterhead',C[C.index('INSTITUT'):C.index('928-48-53')+9],'',r'INSTITUT\\ DES HAUTES ÉTUDES SCIENTIFIQUES\\ 91 - BURES-SUR-YVETTE\\ 928-48-53','All four printed lines are visible; the last is crossed by the manuscript Giraud cancellation but remains legible.',[136,139,614,325],kind='omission')
d('Giraud: Notes sur and lowered letter',r'Notes sur \unsure{$B_G$|$B_g$}',r'Notes sur \ill\ 67',r'Notes sur \unsure{$B_G$|$B_g$}','A large looped B precedes one lower right loop-and-stem glyph. No independent 67 follows it. The G/g distinction remains open.',crop=6,conf='medium',kind='misread symbol or index')
d('Left label Klose',r'\uline{Klose}',r'\textbf{\struck{\ill}} — \struck{Lettre sur Hartshorne}',r'\deleted{\uline{Klose}}','Separate K arms, tall looped l, low o and final s/e contours survive the crossing.',crop=7,kind='readable ink left as \\ill{}')
d('Klose: letter subject',r'lettre sur \unsure{Ulmers|Ulmer}',r'Lettre sur Hartshorne',r'lettre sur \unsure{Ulmers|Ulmer}','Initial U and following tall narrow stroke are visible; the end is covered by the doubled cancellation. No initial H or long Hartshorne sequence is visible. Lowercase initial l in lettre.',crop=7,conf='low')
d('Upper right: vertical marks before Griffiths',r'\tikz[baseline=-.45ex]{\draw (0,0)--(.06,.52) (.09,.04)--(.15,.49);}','',r'\draw (936,100)--(943,29) (948,96)--(956,33) (960,81)--(966,49);','Two long slanted uprights and one shorter right upright remain distinct. They cross the cancellation and are reproduced without a letter value.',crop=2,conf='medium',kind='drawing or diagram',cc=True)
d('Griffiths: périodes uncertainty',r'\unsure{périodes}',r'\struck{\uncertain{Griffiths} périodes}',r'\unsure{périodes}','A descender and spaced narrow stems survive, but two crossing strokes hide enough of the word that the unmarked H word is too definite.',crop=2,conf='low',kind='other')
d('Griffiths: faint terminal marks',r'\unsure{\ldots|.}',r'\struck{\uncertain{Griffiths} périodes}',r'\unsure{\ldots|.}','Faint separated short marks continue to the right of périodes below the main cancellation; their punctuation count is not secure.',crop=2,conf='low',kind='omission')
d('SGA abbreviation uncertainty',r'\unsure{SGA|SG}',r'SGA 6 XIV',r'\unsure{SGA|SG}','The first abbreviation is partly obscured by staining and crossing strokes; a final tall form may be A. Retain the local C alternative.',crop=3,conf='medium',kind='other')
d('SGA roman numeral',r'$\overline{\underline{\mathrm{XII}}}$',r'SGA 6 XIV',r'$\overline{\underline{\mathrm{XII}}}$','After X there are two narrow uprights, not the oblique arms of V. Independent upper and lower rules span XII.',crop=3,kind='misread symbol or index')
d('Chern entry',r'Classes de Chern des représentations.',r'Chern et classes de Chern des représentations',r'\deleted{Classes de Chern des représentations.}','The first large C belongs to Classes, followed directly by de Chern; there is no preceding Chern et. A final point is visible.',[971,124,1647,169])
d('Quillen/Adams colon and abbreviation',r'Quillen : sur \unsure{conj.} de Adams',r'Quillen sur \uncertain{sém.} de Adams',r'Quillen : sur conj. de Adams','A colon follows Quillen. The abbreviated word has c/o/n followed by a distinct descending j and a small point, supporting conj., not sém.',crop=4,cc=True)
d('Artin line: initial numeral',r'\unsure{2|2)}',r'2 lettres',r'2','The numeral has a curved upper stroke, slanting descent and low base. The following crossing belongs to the separate X-shaped mark; there is no closing parenthesis beside 2.',crop=5,kind='misread symbol or index',cc=True,hc=False)
d('Artin line: crossed shape between 2 and lettre',r'\deleted{\unsure{x|X}}',r'2 lettres',r'\draw (948,224)--(977,257) (977,222)--(951,259);','The mark is two long diagonals, extending above and below the word line. Preserve the cross as cancellation ink rather than selecting a lowercase or capital letter.',crop=5,kind='drawing or diagram',cc=True)
d('Artin line: lettre and named subject',r'\unsure{lettre} : Artin (sur Atiyah-Adams)',r'2 lettres à \ill\ sur Atiyah--Adams)',r'lettre : Artin (sur Atiyah-Adams)','The ending of lettre stops after e; the following separated points are a colon. Artin has a distinct A and tall t. An opening parenthesis before sur survives. No plural s or à occurs.',crop=5,cc=True)
d('Point below 2/cross','','',r'\unsure{\tikz[baseline=0pt]{\fill (0,0) ellipse (.55pt and .22pt);}}','A detached dark short oval occurs below the numeral, left of the cross. Its relation to the cancellation is uncertain; no punctuation value is assigned.',crop=5,conf='low',kind='omission',cc=True)
d('Inserted, cancelled date',r'\inserted{\deleted{\unsure{10.3.66|10.5.66}}}',r'\add{du} 10.I.66',r'\inserted{\deleted{\unsure{10.5.66|10.3.66|10.I.66}}}','The middle digit has an upper turn and a lower return, favouring 5 over 3; the crossing prevents certainty and also leaves a narrow I-shaped form possible. Two sixes and the separators survive. The date is on a separate lower insertion line and is crossed. There is no du.',crop=5,conf='medium',cc=True)
d('Date: shallow upper curve','','',r'\draw (1127,279) .. controls (1144,249) and (1146,246) .. (1173,246) .. controls (1204,253) and (1235,244) .. (1269,246);','A shallow arch rises from the low left of the date and continues above it. Its shape is preserved independently of the date text.',crop=5,kind='drawing or diagram',cc=True)
d('Goodman thesis',r'Thèse \uline{Goodman}',r'thèse \ill',r'\deleted{Thèse \uline{Goodman}}','Tall capital T; Goodman has initial G, two rounded o forms and distinct final m/a/n run. A separate underline lies beneath the surname.',crop=8,kind='readable ink left as \\ill{}')
d('Quillen title Deviations',r'Quillen \unsure{Deviations|Derivations} \ldots',r'Quillen, \emph{Derivations} \ill',r'Quillen Deviations \unsure{....|\ldots}','After De the next joined form is a v; no separate r precedes it. The rest reads iations. No comma is visible after Quillen.',crop=8,conf='medium',cc=True)
d('Quillen title cancellation state',r'\deleted{Quillen \unsure{Deviations|Derivations} \ldots}',r'Quillen, \emph{Derivations} \ill',r'\deleted{Quillen Deviations \unsure{....|\ldots}}','A dark line crosses Quillen and the title continuously. H leaves the entry live.',crop=8,kind='deletion state (struck given live or live given struck)')
d('Quillen title final points',r'\ldots',r'Quillen, \emph{Derivations} \ill',r'\unsure{....|\ldots}','Two dark points and two lighter short marks follow the title; the last approaches the enclosure. Four are preferred but three remain possible.',crop=8,conf='medium',kind='other',cc=True)
d('Quillen title oval','','',r'\draw (994,324) .. controls (1106,310) and (1310,322) .. (1408,319) .. controls (1454,321) and (1445,346) .. (1416,356) .. controls (1281,387) and (1060,370) .. (1002,359) .. controls (989,354) and (983,334) .. (994,324);','A separate thin closed oval surrounds the struck Quillen entry; its lower curve reaches left beneath Quillen.',crop=8,kind='drawing or diagram',cc=True)
d('Hartshorne title wording',r'Hartshorne \uline{On Cohomological \unsure{dimension|dimensions}}\unsure{..|\ldots}',r'Hartshorne \ill\ cohomologie \ill',r'Hartshorne On Cohomological dimension..','On is followed by the English word Cohomological. The final word ends in the low n terminal, with no separate s; exactly two dark final points remain.',crop=9,conf='high',kind='readable ink left as \\ill{}',cc=True)
d('Hartshorne low contour versus title underline',r'\uline{On Cohomological \unsure{dimension|dimensions}}',r'Hartshorne \ill\ cohomologie \ill',r'On Cohomological dimension..','The low line continues left beneath Hartshorne and curves into the large enclosure; it is not a distinct underline restricted to the English title. The contour is reproduced as a drawing.',crop=9,conf='medium',kind='drawing or diagram',cc=True,hc=False)
d('Long contours above and below Hartshorne','','',r'\draw (600,132) .. controls (837,123) and (875,130) .. (884,207) .. controls (890,274) and (887,340) .. (911,359) .. controls (934,372) and (1494,358) .. (1636,378); \draw (901,346) .. controls (909,377) and (907,400) .. (940,407) .. controls (1100,427) and (1467,415) .. (1653,410);','One long curve starts in the blank area to the right of the letterhead and turns down toward the top of Hartshorne; a second low contour passes under the row. Their close approach at left is not forced into a common endpoint.',[599,124,1660,425],conf='medium',kind='drawing or diagram',cc=True)
d('Algèbre III rules',r'$\overline{\underline{\mathrm{III}}}$',r'Notes Algèbre III Bourbaki',r'$\overline{\underline{\mathrm{III}}}$','Three uprights are bounded by separate cap and base rules.',[767,443,823,488],kind='misread symbol or index')
d('Shih first item',r'Rapport à Bourbaki calcul différentiel',r'R. Wood à Bourbaki, calcul différentiel',r'R. Wood à Bourbaki calcul différentiel','R is followed by a distinct point and a large W with two deep troughs; the following low o/o/d sequence belongs to Wood. There is no comma after Bourbaki.',crop=10,cc=True)
d('Schwarzenberger initial 3 underline',r'\uline{3}',r'3 articles Schwarzenberger',r'\unsure{\uline{3}|3}','The 3 itself is definite. A faint low rightward trace may be an underline, but its connection and extent beneath the numeral are uncertain.',crop=36,conf='low',kind='other',cc=True)
d('fibrés punctuation',r'\unsure{fibrés|fibrés,}',r'fibrés vectoriels',r'fibrés vectoriels','The terminal s turns down; after it there is a blank gap before vectoriels, with no comma.',crop=11,kind='other',cc=True,hc=False)
d('Hatched left label below Résumé',r'\deleted{\uline{\unsure{N|M}\illegible{1}}}',r'\textbf{\struck{\ill}} — \struck{\ill} Papiers Atiyah',r'\deleted{\uline{\unsure{N|M}\illegible{1}}}','The first angular letter survives sufficiently for N/M alternatives. The remaining short group is repeatedly crossed and cannot be recovered word by word.',crop=12,conf='low',kind='readable ink left as \\ill{}')
d('PTTM crossed abbreviation',r'\deleted{\unsure{PTTM|PTT M}}',r'\struck{\ill} Papiers Atiyah',r'\deleted{\unsure{PTTM|PTT M}}','P, two separate T crossbars and a final M trough survive. Whether the final M is set off by a space remains uncertain.',crop=13,conf='medium',kind='readable ink left as \\ill{}')
d('Hatching of two labels below Résumé','','',r'\draw (185,756)--(212,718) (201,764)--(224,722) (215,769)--(235,727) (230,774)--(252,727) (247,773)--(266,738) (268,775)--(279,746); \draw (451,770)--(501,710) (490,765)--(529,713) (530,765)--(559,709) (541,756)--(580,717) (575,763)--(607,716) (588,759)--(620,723);','Separate slanting hatch strokes cross both cancelled labels; the strokes are retained in addition to the deletion state.',[177,703,625,782],kind='drawing or diagram',cc=True)
d('Atiyah line underlining and punctuation',r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}',r'Papiers Atiyah, topologie et opérateurs elliptiques',r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}','Two low parallel rules run under Papiers Atiyah; one each under topologie and op. elliptiques. No comma follows Atiyah.',[647,682,1645,785],kind='omission')
d('Atiyah abbreviated op.',r'op. elliptiques',r'opérateurs elliptiques',r'op. elliptiques','Only o, a descended p and a point precede elliptiques.',[1325,682,1642,749],kind='abbreviation expanded or spelling modernised')
d('Bertin EGA IV',r'EGA $\overline{\underline{\mathrm{IV}}}$ 16--19',r'EGA IV 16--19',r'EGA $\overline{\underline{\mathrm{IV}}}$ 16--19','The numeral has a separate cap and lower rule.',[477,802,815,857],kind='misread symbol or index')
d('Bertin photocopies',r'\unsure{photocopies}',r'16--19, photocopie',r'16--19 photocopies','The final downward hook after ie gives plural s; the two p descenders and the h/t stems remain visible. No comma is present before the word.',crop=14,cc=True)
d('Madame abbreviation uncertainty',r'\unsure{Mme|Mne}',r'Mme Hakim',r'\unsure{Mme|Mne}','A capital M is followed by a small covered group; m versus n in that group is not settled by the cancellation.',crop=15,conf='medium',kind='other')
d('Underlined surname after Mme',r'\uline{\unsure{Mathieu|Mathies}}',r'Mme Hakim',r'\uline{\unsure{Mathieu|Mathies}}','The initial is a large M, followed by a low a bowl and tall joined th-like stroke. The final hook does not settle u/s; Hakim is not supported by the visible start.',crop=15,conf='low')
d('Séminaire Gabriel subject and punctuation',r'Séminaire Gabriel deux schémas,',r'Séminaire Gabriel, deux séminaires,',r'Séminaire Gabriel deux schémas,','No comma stands after Gabriel. The following word after deux has the sché-mas contour, not the longer repeated séminaires.',crop=16)
d('Exp abbreviation',r'\unsure{Exp|Ex.}',r'exp.~7',r'Exp','The final p has a distinct descent below x, and there is no separate abbreviation point after it. The initial E is tall.',crop=17,kind='abbreviation expanded or spelling modernised',cc=True)
d('Exp numeral',r'$\unsure{7|\mathrm I}$',r'exp.~7',r'7','The long upper arm and descending stem with a short crossbar establish a crossed 7, not Roman I.',crop=17,kind='misread symbol or index',cc=True,hc=False)
d('Bertin/Mme spanning cancellation','','',r'\draw (bertin.base west) .. controls (210,922) and (214,955) .. (232,981) .. controls (593,978) and (1129,963) .. (1392,915);','A low boundary runs from Bertin down through the following label and across the seminar row. A broad repeated wavy stroke rises between these rows, and a separate upper-right turn closes near Exp 7. All three paths are in reading.tex.',[191,797,1410,1003],kind='drawing or diagram',cc=True)
d('Ferrand EGA IV',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20,21',r'EGA IV 20, 21',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20,21','The IV has its own upper and lower strokes; the comma between 20 and 21 is visible.',[526,1060,832,1110],kind='misread symbol or index')
d('Ferrand cancelled photocopies and épreuves',r'\deleted{\unsure{photocopies}} épreuves',r'\struck{\ill}',r'\deleted{\unsure{photocopies}} épreuves','The first word is additionally hatched; p descenders and several loops support photocopies with doubt. The following épreuves has an accent, descended p and final s; the long row cancellation also crosses it.',crop=18,conf='medium',kind='readable ink left as \\ill{}')
d('Dieudonné letter separator',r'Lettre : Dieudonné',r'Lettre à Dieudonné',r'Lettre : Dieudonné','Two separated points, not an a-shaped body with accent, occur after Lettre.',[529,1130,979,1182])
d('Dieudonné subject word',r'\unsure{parafactoriel|par.factoriel}',r'Lettre à Dieudonné sur \ill\ de dimension 2',r'\unsure{par.factoriel|parafactoriel}','A small detached filled mark lies between par and the tall f. It may be a stop or a compressed a; par.factoriel is placed first without deleting the longer alternative.',crop=19,conf='low',cc=True)
d('Dieudonné preposition before dim',r'\unsure{en|de}',r'de dimension 2',r'\unsure{de|en}','The first small low loop leads to a higher peaked stem, favouring d plus e, but the compressed connected group also permits en.',crop=19,conf='low',kind='other',cc=True)
d('Dieudonné dim abbreviation',r'dim 2',r'dimension 2',r'dim 2','Only the short dim group is present before 2; there is no stop after it.',crop=19,kind='abbreviation expanded or spelling modernised')
d('Circled RR question: H descriptive replacement',r'\node[inner sep=2pt] (rr) {\deleted{Notes sur R.R.}};\draw (rr.center) ellipse [x radius=3.1em,y radius=.74em];',r"\add{entouré, suivi d'un point d'interrogation}",r'\deleted{Notes sur R.R.}\quad ?','The thin oval and separate live question mark are actual source marks. H describes them editorially rather than reproducing them; that description is not source text.',[529,1179,919,1255],kind='drawing or diagram')
d('Foncteur',r'\unsure{foncteur}',r'Notes sur \ill\ dét.',r'Notes sur le foncteur dét.','The visible f stem, rounded o, n/c joins, tall t and eur ending support foncteur. The preceding le is also visible in the half.',crop=20,conf='medium',kind='readable ink left as \\ill{}',cc=True)
d('Picard underlining and full stop',r'\uline{sur cat. de Picard} .',r'sur cat.\ de Picard',r'\uline{sur cat. de Picard} .','One continuous low rule runs from sur through Picard; a separated final point follows the group.',[1171,1165,1621,1249],kind='omission')
d('Inserted Papiers Hartshorne',r'Papiers Hartshorne',r'\struck{Papiers \uncertain{Hertzbrouck}}',r'\inserted{Papiers Hartshorne}','H/a/r/t/sh/o/r/n/e strokes belong to the raised entry; that entry is not crossed. The cancellation below passes through Notes cohomologie instead.',crop=21,kind='misread word')
d('Raised parenthetical abbreviation',r'(dim. coh.)','',r'(dim. \unsure{ch.|coh.})','After dim. a small low c-like form and a tall looped h are visible. A distinct intervening o is not secure; retain ch./coh. locally rather than completing the familiar abbreviation.',crop=21,conf='low',kind='other',cc=True)
d('Raised Goodman continuation',r'et Goodman',r'\add{et} Godement',r'\inserted{et Goodman}','Two rounded o forms precede d, followed by m/a/n. The words stand at the high right end of the Hartshorne insertion, not after the Picard entry.',crop=21)
d('Raised insertion position',r'\uline{Jouanolou}\quad 1\qquad \inserted{Papiers Hartshorne (dim. coh.) et Goodman}',r'\add{et} Godement ; \struck{Papiers \uncertain{Hertzbrouck}}',r'\node (hartshorneadd1) at (632,1286) {\inserted{Papiers Hartshorne}}; \node (hartshorneadd2) at (1056,1268) {\inserted{(dim. \unsure{ch.|coh.}) et Goodman}};','The addition rises to the right and sits above the struck cohomologie row. C marks insertion but places it linearly after Jouanolou; H divides it between unrelated entries. Both physical heights are retained.',crop=21,kind='insertion or placement',cc=True)
d('Cancelled cohomology entry',r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}','',r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}','The darker low row reads Notes cohomologie followed by a looped tall letter, hyphen and adique. Its long cancellation remains distinct from the live words above.',crop=21,conf='medium',kind='omission')
d('Papier Hirzebruch wording',r"Papier Hirzebruch (Congrès d'Amsterdam",r"Papiers Hirzebruch (congrès d'Amsterdam ?)",r"Papier Hirzebruch (Congrès d'Amsterdam",'The first word is singular Papier; the following initial C in Congrès is large. H adds a plural s and lowers the initial C.',[551,1330,1558,1408])
d('Amsterdam closing marks',r'\unsure{?\,)|?} )',r"Papiers Hirzebruch (congrès d'Amsterdam ?)",r'?\,)\,)','A small closing curve immediately follows the question mark; a second, much taller closing parenthesis follows it. Both are certain visible strokes.',crop=22,kind='misread symbol or index',cc=True)
d('Serre two-line brace',r'\left\{\begin{array}{l}',r'Lettre : Serre \add{sur} \ill\ fonctionnelles, suite, début de monodromie \ill',r'\draw (864,1407) .. controls (853,1405) and (857,1422) .. (861,1434) .. controls (865,1441) and (860,1447) .. (849,1449) .. controls (861,1451) and (861,1457) .. (860,1470) .. controls (859,1482) and (860,1490) .. (866,1491);','A left brace groups the two subject lines, with Lettre : Serre beside its middle. The L remains on the upper text baseline.',[547,1396,1425,1494],kind='drawing or diagram')
d('Serre upper abbreviation and singular adjective',r'\unsure{équ.} fonctionnelle',r'\ill\ fonctionnelles',r'\unsure{équ.} fonctionnelle','Compressed first group has an accented e, descended q and a small terminal point, but remains tentative. The following word ends with e after two tall l strokes; no final s or following comma is seen.',crop=23,conf='medium',kind='readable ink left as \\ill{}')
d('Serre fonction L',r'\unsure{fonction|fonctions} }L','',r'\unsure{fonction|fonctions} $L$','A second fonction-like word occurs after fonctionnelle, followed by a separate plain capital L on the same slanted baseline. The terminal plural remains uncertain.',crop=23,conf='medium',kind='omission')
d('H inserted sur at Serre','',r'\add{sur}',r'Lettre : Serre','No sur or insertion caret occurs between Serre and the brace.',[545,1423,877,1484],kind='text not on the page')
d('Serre début',r'\unsure{début|défaut}',r'début de monodromie',r'début','After dé a closed b bowl survives; it is followed by u and a tall terminal t. There is no f descent or separate a.',crop=24,kind='other',cc=True,hc=False)
d('Serre terminal points',r'\unsure{....|\ldots}',r'monodromie \ill',r'monodromie ....','Four separated small marks follow the final e: two darker points and two lighter short dashes.',crop=24,conf='medium',kind='readable ink left as \\ill{}',cc=True)
d('Deligne right note wording',r'Lettre Deligne \unsure{complexes} elliptiques',r'lettre Deligne sur opérateurs elliptiques',r'Lettre Deligne complexes\\elliptiques','After Deligne the sequence has c/o/m, a descended p, tall l and exes, supporting complexes; there is no sur or opérateurs. The initial L of Lettre is tall.',crop=25,cc=True)
d('Deligne right note position and rule',r'\margin{\noindent\vrule height 1ex depth 4.8ex width .35pt\hspace{.2em}\parbox[t]{.86\linewidth}{\deleted{Lettre Deligne \unsure{complexes} elliptiques}}}',r'\struck{lettre Deligne sur opérateurs elliptiques}',r'\node (delignenote1) at (1253,1495) {\deleted{Lettre Deligne complexes}}; \node (delignenote2) at (1431,1522) {\deleted{elliptiques}}; \draw (1237,1472)--(1244,1623);','The second line is indented far to the right, beneath the end of the first. A separate long left rule begins near the first line and descends well below it. C generic margin wrapping does not retain this indentation; H runs the note into the body list.',crop=25,kind='insertion or placement',cc=True)
d('Berthelot RR punctuation',r'Notes RR (copie de Serre)',r'Notes R.R.\ (copie de Serre)',r'Notes RR (copie de Serre)','No detached points follow the two R forms here; the points of the earlier circled R.R. are visibly different.',crop=26,kind='misread symbol or index')
d('Notes Serre small formula',r'${\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0$',r'Notes Serre sur \ill',r'${\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0$','A low curved initial and tall second stem sit below a narrow raised cluster. The equality and closed zero are clear; the baseline first letter and final exponent character are crossed. Retain all C alternatives.',crop=27,conf='low',kind='readable ink left as \\ill{}')
d('Calcul K grouping and superscript',r'K\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}',r'Calcul \ill',r'K(\mathrm{P}^{n}','A low opening curve separates K from a tall P; the small raised n is to the upper right of P. The curve lacks the body and terminals of a separate C.',crop=28,kind='misread symbol or index',cc=True)
d('Calcul inner letter and short bar',r'\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}',r'Calcul \ill',r'\unsure{\mathrm L^{-}|\overline{\mathrm L}|\overline{\mathrm C}}','The main inner form has an upright and rightward foot. The short detached bar lies above and to the right; a superscript minus is preferred, but an overbar and the more heavily curved C alternative remain possible under the crossing.',crop=28,conf='low',kind='misread symbol or index',cc=True)
d('Rapport Serre punctuation',r'Rapport Serre représentations de groupes finis',r'Rapport Serre, représentations de groupes finis',r'Rapport Serre représentations de groupes finis','The space after Serre contains no separate comma; the next word begins directly after the gap.',[588,1648,1465,1712],kind='text not on the page')
d('Kleiman photocopies',r'\unsure{photocopies|Photocopies}',r'Manuscrits ? EGA IV 20',r'\unsure{photocopies|Photocopies}','Initial loop/stem followed by h and the two p descents supports photocopies. Capital versus lowercase initial remains open; neither Manuscrits nor a question mark occurs.',crop=29,conf='medium')
d('Kleiman EGA IV rules',r'\unsure{photocopies|Photocopies} EGA $\overline{\underline{\mathrm{IV}}}$ 20',r'Manuscrits ? EGA IV 20',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20','The IV has independent cap and base strokes amid the two row cancellations.',crop=29,kind='misread symbol or index')
d('EGA V rules',r'EGA $\overline{\underline{\mathrm{V}}}$',r'EGA V',r'EGA $\overline{\underline{\mathrm{V}}}$','A V-shaped numeral has a distinct upper cap and lower rule.',[838,1737,1041,1781],kind='misread symbol or index')
d('Chev. abbreviation',r'Notes Chev. sur',r'Notes Chevalley sur',r'Notes Chev. sur','The source has the short Chev. form before sur, not the expanded surname.',[556,1798,1003,1846],kind='abbreviation expanded or spelling modernised')
d('Grassmannian word',r'\unsure{grassmanniennes|grassmaniennes}',r'groupes \ill',r'\unsure{grassmanniennes|grassmaniennes}','After initial descended g the joined low humps continue into the long -iennes ending. The count of n humps remains obscured. There is no independent groupes word.',crop=30,conf='medium')
d('Note Agison title',r'Note \unsure{Agison|Agišon} \unsure{bidéterminants|holodéterminants}',r'Notes \ill',r'Note \unsure{Agison|Agišon} \unsure{bidéterminants|holodéterminants}','Note ends without a separate s. The name starts with an A arch and g loop; a small mark over the central letters may be intrinsic or cancellation. The following title has multiple covered initial strokes, so both C alternatives remain.',crop=31,conf='low',kind='readable ink left as \\ill{}')
d('Problèmes cancellation',r'\deleted{Problèmes de Géométrie Algébrique}',r'\emph{Problèmes de Géométrie Algébrique}',r'\deleted{Problèmes de Géométrie Algébrique}','A dark horizontal crosses this entire row, in addition to the large diagonal and wavy cancellations. H gives it live.',[555,1846,1212,1904],kind='deletion state (struck given live or live given struck)')
d('Verdier SGA final sign',r'\unsure{SGAA|SGA 4}',r'SGA 4 fasc.~1',r'\unsure{SGAA|SGA 4}','The last sign has two converging upper strokes and an inner cross stroke, closely resembling the preceding A. A handwritten 4 remains possible; H unmarked 4 is too definite.',crop=32,conf='low',kind='other')
d('Verdier personal-copy wording',r'fasc. 1, mon exemplaire personnel',r'fasc.~1, \ill',r'fasc. 1, mon exemplaire personnel','After the comma the sequence mon, exemplaire and personnel is visible along the long slanting row.',[736,1880,1603,1950],kind='readable ink left as \\ill{}')
d('Verdier entry cancellation',r'\deleted{\uline{Verdier}\qquad \unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}',r'\textbf{\struck{Verdier}} — SGA 4 fasc.~1, \ill',r'\deleted{\uline{Verdier}\qquad \unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}','The same long rising dark stroke crosses the label and the complete item text. H strikes only the label.',[235,1880,1605,1966],kind='deletion state (struck given live or live given struck)')
d('Gabriel',r'\unsure{Gabriel}',r'\struck{Gabriel}',r'Gabriel','G/a, tall b, r/i and terminal looped l remain distinguishable below and above the broad strike.',crop=33,conf='medium',kind='other',cc=True,hc=False)
d('Terjanian label',r'\uline{\unsure{Terjanian|Terzanian}}',r'\textbf{\struck{\ill}} — \struck{Article \uncertain{Grünberg} sur \ill}',r'\uline{Terjanian}','After Ter the letter has one smooth long descending hook, supporting j; a sharp z body is absent. The remaining a/n/i/a/n run survives.',crop=34,conf='high',kind='readable ink left as \\ill{}',cc=True)
d('Article(s) uncertainty',r'\unsure{Articles|Article}',r'Article \uncertain{Grünberg}',r'\unsure{Articles|Article}','The final low horizontal and down-turn are partly on the strike. A final s cannot be excluded or isolated confidently.',crop=35,conf='medium',kind='other')
d('Greenberg',r'Greenberg',r'\uncertain{Grünberg}',r'Greenberg','Two consecutive low e-shaped joins follow Gr; no umlaut points stand above them. The tall b and final descending g survive.',crop=35)
d('Final C subscript',r'\unsure{$C_i$|$C_1$}',r'Article \uncertain{Grünberg} sur \ill',r'\unsure{$C_i$|$C_1$}','A plain capital C is followed by a small low right mark and a separate upper mark. The crossing leaves i/1 unresolved; the symbol is not wholly unreadable.',crop=35,conf='medium',kind='readable ink left as \\ill{}')
d('Spanning lower-list cancellations','','',r'\draw (bertname.south) .. controls (365,1688) and (467,1868) .. (568,1977);','Several thin diagonals descend from the Berthelot/Deligne region through later rows; the broad wavy run traverses Kleiman through the final Article(s) row, with a large rounded right contour. All four thin tracks, two terminal spurs, the broad wave and outer curve are explicitly drawn relative to the positioned text. Individual deletion wrappers alone do not preserve this coverage.',[274,1504,1602,2059],kind='drawing or diagram',cc=True)
d('H list-joining separators','',r'—',r'(no dash or semicolon at the blank joins between separate list entries)','H repeatedly joins the physical list entries with em dashes and semicolons. These are absent at the corresponding blank joins on this sheet; source colons, commas and stops are retained individually in reading.tex. This row records the repeated editorial joining punctuation, not the source punctuation within an entry.',[164,28,1654,2074],kind='text not on the page')

report=dict(page='H162-01_162-1_scan003',reader='R2',viewed=dict(whole='source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003.jpg',a='source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003_a.jpg',b='source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003_b.jpg'),reading_file='out/readers/H162-01_162-1_scan003/R2/reading.tex',differences=D,c_doubts=[],inventory=[],remaining_doubts=[],notes=[],notation=[],abbreviations=[],math_checks=[],crop_count=len(manifest),workflow_feedback=[])

def q(place,c,r,e,crop=None,box=None,conf='medium',status='retained'):
    if crop:box=crops[crop]['box'];path='readers/H162-01_162-1_scan003/R2/crops/'+crops[crop]['dest'];src='whole'
    else:path=None;src='whole; half evidence'
    report['c_doubts'].append(dict(id=f'CQ-{len(report["c_doubts"])+1:03d}',place=place,C=lit(C,c),decision=r,evidence=e,crop=path,bbox=box,bbox_source=src,confidence=conf,status=status))
q('Head parenthesis',r'\unsure{suite}',r'\unsure{suite}','s/u/i/t are supported, but the low terminal remains on the cancellation.',1)
q('Head surname',r'\unsure{Libermann|Libermans}',r'\unsure{Libermann|Libermans}','Tall beginning and repeated low final humps survive; the crossed middle and final n/s do not decide the surname.',1,conf='low')
q('Giraud lower letter',r'\unsure{$B_G$|$B_g$}',r'\unsure{$B_G$|$B_g$}','The lower right bowl has a right terminal stem; its G/g form is not settled beneath the line.',6)
q('Klose letter subject',r'\unsure{Ulmers|Ulmer}',r'\unsure{Ulmers|Ulmer}','Initial U and tall following stroke survive; a possible final s is entangled with the lower strike.',7,conf='low')
q('Upper right name',r'\unsure{Griffiths}',r'\unsure{Griffiths}','Large G loop and multiple tall stems support the proposal, but two strokes and staining obscure the bodies.',2,conf='low')
q('Upper right périodes',r'\unsure{périodes}',r'\unsure{périodes}','Descender and narrow stems remain, but the middle and accent region are heavily crossed.',2,conf='low')
q('Upper right terminal punctuation',r'\unsure{\ldots|.}',r'\unsure{\ldots|.}','Several faint short marks lie below/right of the main strike; punctuation count remains uncertain.',2,conf='low')
q('SGA letters',r'\unsure{SGA|SG}',r'\unsure{SGA|SG}','The last tall form before 6 may be A; the stained crossed abbreviation remains locally uncertain.',3)
q('Quillen/Adams abbreviation',r'\unsure{conj.}',r'conj.','A c arc, joined o/n, descending j and following small point are visible.',4,conf='high',status='resolved')
q('Artin initial numeral',r'\unsure{2|2)}',r'2','The separate X-shaped crossing explains the adjacent strokes; there is no independent close-parenthesis curve.',5,conf='high',status='resolved')
q('Artin cross',r'\unsure{x|X}',r'\draw (948,224)--(977,257) (977,222)--(951,259);','Two large diagonals are transcribed as cancellation ink, without a lowercase/capital letter value.',5,conf='high',status='revised as graphic')
q('Artin lettre',r'\unsure{lettre}',r'lettre','The looped l, two t strokes and final re sequence survive; no plural s follows.',5,conf='high',status='resolved')
q('Inserted date',r'\unsure{10.3.66|10.5.66}',r'\unsure{10.5.66|10.3.66|10.I.66}','Middle digit upper turn and low return favour 5, but the main crossing leaves 3 and a narrow I-shaped form possible. The two sixes and separators are visible.',5,conf='medium',status='revised preference')
q('Second Quillen title',r'\unsure{Deviations|Derivations}',r'Deviations','The letter immediately after De has the v contour; no intervening r survives. iations follows.',8,conf='medium',status='resolved')
q('Hartshorne terminal noun',r'\unsure{dimension|dimensions}',r'dimension','The final n stops before two points; no separate s contour follows.',9,conf='high',status='resolved')
q('Hartshorne punctuation',r'\unsure{..|\ldots}',r'..','Two discrete dark points occur at the end.',9,conf='high',status='resolved')
q('Schwarzenberger fibrés',r'\unsure{fibrés|fibrés,}',r'fibrés','No separate comma occurs in the blank gap after the s terminal.',11,conf='high',status='resolved')
q('Hatched left initial',r'\unsure{N|M}',r'\unsure{N|M}','Two tall stems and a crossing diagonal remain, but their overlap with hatching leaves N/M open.',12,conf='low')
q('Hatched unreadable remainder',r'\illegible{1}',r'\illegible{1}','An attempted reading cannot recover the covered short letter group after the initial; one word remains an estimate.',12,conf='low')
q('Hatched PTTM',r'\unsure{PTTM|PTT M}',r'\unsure{PTTM|PTT M}','P, T, T and M are recoverable. The final gap is not distinct enough to decide separation.',13)
q('Bertin photocopies',r'\unsure{photocopies}',r'photocopies','The p descenders, tall h/t and terminal plural hook survive the lighter crossing.',14,conf='high',status='resolved')
q('Mme abbreviation',r'\unsure{Mme|Mne}',r'\unsure{Mme|Mne}','The small letters after M are on the cancellation; the m/n distinction remains open.',15)
q('Mme surname',r'\unsure{Mathieu|Mathies}',r'\unsure{Mathieu|Mathies}','Large M, a bowl and joined tall th-like form survive; the final low hook does not distinguish u/s.',15,conf='low')
q('Seminar Exp',r'\unsure{Exp|Ex.}',r'Exp','A p descender follows x; no independent period follows.',17,conf='high',status='resolved')
q('Seminar 7',r'\unsure{7|\mathrm I}',r'7','A top arm projects right; the long stem has a small crossing bar. The form is a crossed 7.',17,conf='high',status='resolved')
q('Ferrand photocopies',r'\unsure{photocopies}',r'\unsure{photocopies}','The extra hatching masks several letter bodies despite surviving p descenders and loops.',18)
q('Dieudonné parafactoriel',r'\unsure{parafactoriel|par.factoriel}',r'\unsure{par.factoriel|parafactoriel}','The small separate mark before f is stop-like but could be a compressed a, as another a is also small in this hand.',19,conf='low',status='revised preference')
q('Dieudonné preposition',r'\unsure{en|de}',r'\unsure{de|en}','A low initial loop and high connected stem favour de; compression permits en.',19,conf='low',status='revised preference')
q('Foncteur',r'\unsure{foncteur}',r'foncteur','Tall f and t, low o/n/c joins and eur ending are visible independently of the upper ellipse.',20,conf='medium',status='resolved')
q('Cohomology initial letter',r'\unsure{\ell|l}',r'\unsure{\ell|l}','A narrow looped tall form nearly meets the deletion; its loop does not distinguish mathematical ell from cursive l here.',21)
q('Amsterdam question/closing curve',r'\unsure{?\,)|?}',r'?\,)','The smaller close-parenthesis curve is separate from the question mark and from the taller following parenthesis.',22,conf='high',status='resolved')
q('Serre équ.',r'\unsure{équ.}',r'\unsure{équ.}','Accented first small curve, descended q and final point support équ., but the compressed central stroke remains uncertain.',23)
q('Serre fonction(s)',r'\unsure{fonction|fonctions}',r'\unsure{fonction|fonctions}','The last joined low terminal before L could include s; its boundary is not clear.',23)
q('Serre début',r'\unsure{début|défaut}',r'début','A closed b bowl follows dé and is followed by u/t; no descended f or extra a appears.',24,conf='high',status='resolved')
q('Serre four points',r'\unsure{....|\ldots}',r'....','Four separate small marks follow the e, the last two lighter and dash-shaped.',24,conf='medium',status='resolved')
q('Deligne complexes',r'\unsure{complexes}',r'complexes','The m humps, p descent, tall l and exes ending are visible around the strike.',25,conf='high',status='resolved')
q('Notes Serre baseline letters',r'\unsure{\mathrm{ch}|\mathrm{dh}}',r'\unsure{\mathrm{ch}|\mathrm{dh}}','The low left curve and tall right stem survive; a possible first ascender is covered by crossing ink.',27,conf='low')
q('Notes Serre exponent',r'\unsure{n-i|n-1|n-\nu}',r'\unsure{n-i|n-1|n-\nu}','The narrow high cluster crosses two rules. No secure final dot, serif or descender settles i/1/nu.',27,conf='low')
q('Calcul outer grouping',r'\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}',r'(\mathrm{P}^{n}','A separate open curve lies between K and P, and the n is raised to the right of P.',28,conf='high',status='resolved')
q('Calcul inner letter/bar',r'\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}',r'\unsure{\mathrm L^{-}|\overline{\mathrm L}|\overline{\mathrm C}}','An upright with a rightward foot is favoured; the short bar is displaced high/right. Its attachment and the covered curved alternative remain uncertain.',28,conf='low',status='revised preference')
q('Kleiman photocopies case',r'\unsure{photocopies|Photocopies}',r'\unsure{photocopies|Photocopies}','The initial loop is tall but runs into the following ascender and cancellation; initial case is not settled.',29)
q('Grassmannian spelling',r'\unsure{grassmanniennes|grassmaniennes}',r'\unsure{grassmanniennes|grassmaniennes}','The long low sequence is visible but two crossing diagonals obscure the count of n humps.',30)
q('Agison name',r'\unsure{Agison|Agišon}',r'\unsure{Agison|Agišon}','A small upper stroke near the central letters may belong to s or to cancellation, leaving the diacritic uncertain.',31,conf='low')
q('Déterminants title',r'\unsure{bidéterminants|holodéterminants}',r'\unsure{bidéterminants|holodéterminants}','Several tall and looped initial forms are crossed by two different strokes. The shared déterminants ending is better supported than the first syllables.',31,conf='low')
q('Verdier SGA final sign',r'\unsure{SGAA|SGA 4}',r'\unsure{SGAA|SGA 4}','The final triangle and inner crossbar resemble A; a cursive 4 can have the same contour. Retain both.',32,conf='low')
q('Gabriel',r'\unsure{Gabriel}',r'Gabriel','The tall b and terminal l loop, with intervening small r/i strokes, remain recoverable below the strike.',33,conf='medium',status='resolved')
q('Terjanian',r'\unsure{Terjanian|Terzanian}',r'Terjanian','The contested letter has a long smooth descending hook, supporting j rather than z.',34,conf='high',status='resolved')
q('Articles ending',r'\unsure{Articles|Article}',r'\unsure{Articles|Article}','The final e/s boundary is partly on the rule; singular/plural remains open.',35)
q('Final C index',r'\unsure{$C_i$|$C_1$}',r'\unsure{$C_i$|$C_1$}','Small high and low marks follow C at lowered right; the long strike separates them ambiguously.',35)

# The C question packet also flags clear notation/layout features separately.
q('Question packet: SGA numeral cap/base',r'$\overline{\underline{\mathrm{XII}}}$',r'$\overline{\underline{\mathrm{XII}}}$','X and two uprights have independent upper/lower rules; no V contour.',3,conf='high',status='confirmed')
q('Question packet: Algèbre III cap/base',r'$\overline{\underline{\mathrm{III}}}$',r'$\overline{\underline{\mathrm{III}}}$','Three uprights and both spanning rules are visible in half a.',box=[768,443,823,488],conf='high',status='confirmed')
q('Question packet: detached Shih 1',r'\uline{Shih}\quad 1',r'\uline{Shih}\quad 1','One small pale numeral stands high to the right of Shih, without a visible underline.',box=[319,529,344,566],conf='high',status='confirmed')
q('Question packet: detached Jouanolou 1',r'\uline{Jouanolou}\quad 1',r'\uline{Jouanolou}\quad 1','One pale numeral is above/right of the label, independently of the raised body insertion.',box=[466,1295,494,1328],conf='high',status='confirmed')
q('Question packet: Atiyah double underline',r'\uuline{Papiers Atiyah}',r'\uuline{Papiers Atiyah}','Two parallel rules are distinct below the phrase.',box=[649,688,1003,784],conf='high',status='confirmed')
q('Question packet: topologie underline',r'\uline{topologie}',r'\uline{topologie}','One independent low rule runs under topologie.',box=[1013,682,1234,760],conf='high',status='confirmed')
q('Question packet: earlier R.R. points',r'Notes sur R.R.',r'Notes sur R.R.','A separate point follows each R inside the oval; the live question mark is outside.',box=[534,1180,914,1252],conf='high',status='confirmed')
q('Question packet: later RR without points',r'Notes RR (copie de Serre)',r'Notes RR (copie de Serre)','The two R forms are not followed by detached points.',26,conf='high',status='confirmed')
q('Question packet: Serre brace',r'\left\{\begin{array}{l}',r'\left\{\begin{array}{l}\text{upper subject}\\\text{lower subject}\end{array}\right.','The physical brace groups two subject lines and stands beside the Serre label; actual source text, not these descriptive labels, is in reading.tex.',box=[845,1398,872,1493],conf='high',status='confirmed')
q('Question packet: PTT before Grenoble',r'Résumé PTT Grenoble',r'Résumé PTT Grenoble','Three capitals P/T/T precede Grenoble; no additional letter occurs.',box=[497,644,968,693],conf='high',status='confirmed')
q('Question packet: baseline L',r'}L',r'$L$','The plain L is on the upper subject baseline, not an exponent or subscript.',23,conf='high',status='confirmed')
q('Question packet: two literal question marks',r'\deleted{Notes sur R.R.}',r'Notes sur R.R.\quad ?','A live question mark follows the circled item; the other explicit question mark follows Amsterdam and is separately decided above. They qualify inventory entries, not a mathematical argument.',box=[530,1177,1558,1390],conf='high',status='confirmed')

def inv(element,kind,box,first,hand='main manuscript hand, dark pen',note=''):
    report['inventory'].append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,position={'bbox':box,'bbox_source':'whole','note':note},first_words_or_objects=first,transcribed='yes'))
def block(name,box,first,cancel=False,hand='main manuscript hand, dark pen',kind='text'):
    inv(name,kind,box,first,hand)
    if cancel:inv(name+' — cancellation','deletion',box,first,hand,'State marked with deleted; spanning strokes are separately inventoried.')
block('Opening Deligne/suite and surname line',[166,25,935,100],'Deligne (suite) Libermann, thèse',True)
block('Printed IHES letterhead, four lines',[136,139,615,325],'INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53',False,'printed letterhead')
block('Giraud label and Notes sur entry',[161,284,824,352],'Giraud — Notes sur B_G',True)
block('Klose label and letter entry',[161,375,895,442],'Klose — lettre sur Ulmers',True)
block('Griffiths périodes entry',[935,22,1455,98],'Griffiths périodes',True)
block('SGA 6 numeral entry',[964,78,1235,132],'SGA 6 XII',True)
block('Chern classes entry',[970,122,1648,171],'Classes de Chern des représentations.',True)
block('First Quillen entry',[969,153,1548,212],'Quillen : sur conj. de Adams',True)
block('Artin/Atiyah-Adams entry',[917,190,1662,262],'2 lettre : Artin (sur Atiyah-Adams)',True)
block('Date under Artin entry',[1126,242,1328,285],'10.5.66 | 10.3.66 | 10.I.66',True,kind='insertion')
block('Goodman thesis entry',[971,279,1386,326],'Thèse Goodman',True)
block('Second Quillen entry',[983,316,1450,373],'Quillen Deviations ....',True)
block('Hartshorne English title entry',[993,361,1663,421],'Hartshorne On Cohomological dimension..',True)
block('Algèbre III entry',[475,441,1065,492],'Notes Algèbre III Bourbaki',True)
block('Shih label and first report entry',[179,525,1410,597],'Shih 1 — R. Wood à Bourbaki calcul différentiel')
block('Schwarzenberger article entry',[482,597,1588,653],'3 articles Schwarzenberger sur fibrés vectoriels',True)
block('PTT Grenoble entry',[496,645,968,695],'Résumé PTT Grenoble')
block('Hatched initial and unreadable left label',[179,702,301,783],'N|M [illegible remainder]',True)
block('Hatched PTTM label',[444,695,631,779],'PTTM | PTT M',True)
block('Atiyah topical heading',[648,680,1647,787],'Papiers Atiyah topologie et op. elliptiques')
block('Bertin and EGA IV 16–19 entry',[188,800,1150,877],'Bertin — EGA IV 16–19 photocopies',True)
block('Mme Mathieu and Gabriel seminar entry',[116,890,1416,1010],'Mme Mathieu — Séminaire Gabriel deux schémas, Exp 7',True)
block('Ferrand label and detached numeral',[220,1071,440,1131],'Ferrand 1')
block('Ferrand EGA IV entry',[525,1035,1373,1114],'EGA IV 20,21 photocopies épreuves',True)
inv('Additional hatching of Ferrand photocopies','deletion',[893,1045,1143,1093],'photocopies','main manuscript hand, dark pen','Nested deleted state retains local hatching distinct from the whole-row strike.')
block('Dieudonné letter entry',[528,1101,1634,1187],'Lettre : Dieudonné sur par.factoriel de dim 2')
block('Circled RR entry',[531,1182,879,1256],'Notes sur R.R.',True)
block('Determinant/Picard entry',[537,1169,1621,1280],'Notes sur le foncteur dét. / sur cat. de Picard .')
block('Jouanolou label and detached numeral',[224,1290,501,1358],'Jouanolou 1')
block('Raised Hartshorne and Goodman insertion',[623,1225,1597,1294],'Papiers Hartshorne (dim. ch.|coh.) et Goodman',False,kind='insertion')
block('Cancelled adic cohomology entry',[555,1267,1195,1328],'Notes cohomologie ell/l-adique',True)
block('Hirzebruch/Amsterdam entry',[549,1320,1566,1414],"Papier Hirzebruch (Congrès d'Amsterdam ?) )")
block('Serre letter label',[544,1424,833,1482],'Lettre : Serre')
block('Serre upper braced subject',[882,1377,1422,1441],'équ. fonctionnelle fonction(s) L')
block('Serre lower braced subject',[881,1430,1447,1495],'suite, début de monodromie ....')
block('Berthelot and stratifications entry',[202,1491,1011,1557],'Berthelot — Notes sur stratifications',True)
block('Deligne note, two staggered lines',[1233,1453,1664,1542],'Lettre Deligne complexes / elliptiques',True,kind='margin note')
block('RR copy entry',[533,1536,1164,1609],'Notes RR (copie de Serre)',True)
block('Serre small formula entry',[540,1579,1040,1647],'Notes Serre sur ch^(n-i)=0',True)
block('Calcul K entry',[541,1628,929,1690],'Calcul K(P^n(L^-))',True)
block('Finite-group representation report',[584,1642,1470,1716],'Rapport Serre représentations de groupes finis',True)
block('Kleiman and photocopies EGA IV entry',[215,1684,1160,1774],'Kleiman — photocopies EGA IV 20',True)
block('EGA V entry',[837,1736,1045,1790],'EGA V',True)
block('Chev. Grassmannian entry',[552,1776,1416,1852],'Notes Chev. sur grassmanniennes',True)
block('Agison déterminants entry',[551,1817,1107,1881],'Note Agison bidéterminants',True)
block('Algebraic geometry problems entry',[550,1844,1221,1910],'Problèmes de Géométrie Algébrique',True)
block('Verdier SGA entry',[232,1875,1607,1971],'Verdier — SGAA|SGA 4 fasc. 1, mon exemplaire personnel',True)
block('Gabriel entry below Verdier',[554,1928,799,1991],'Gabriel',True)
block('Terjanian label',[229,2002,549,2083],'Terjanian',True)
block('Final Greenberg article entry',[592,1989,1312,2074],'Articles|Article Greenberg sur C_i|C_1',True)
inv('Detached pale numeral beside Shih','text',[320,530,345,566],'1','pale pencil; hand not securely differentiated')
inv('Detached pale numeral beside Ferrand','text',[410,1076,438,1109],'1','pale pencil; hand not securely differentiated')
inv('Detached pale numeral beside Jouanolou','text',[467,1295,498,1330],'1','pale pencil; hand not securely differentiated')
inv('Three upright marks before Griffiths','drawing',[934,26,970,104],'two long slanted uprights and one short right upright')
inv('Cross between 2 and lettre','drawing',[946,219,981,263],'two crossing diagonals')
inv('Detached low point beneath Artin numeral','drawing',[928,260,946,269],'short low oval','main manuscript hand, dark pen','Identity/function uncertain; explicit local unsure graphic.')
inv('Shallow date arch','drawing',[1125,242,1274,282],'arch above inserted date')
inv('Oval enclosing Quillen Deviations','drawing',[983,316,1450,375],'closed thin oval')
inv('Two extended Hartshorne contours','drawing',[597,123,1660,425],'long curve from letterhead blank and low enclosing curve','main manuscript hand, thin pen','Near-junction not forced into a shared endpoint.')
inv('Possible low underline beneath 3','drawing',[483,612,533,649],'3 with faint low right stroke','mixed dark and pale ink','Underline preserved as a local underline/no-underline alternative.')
inv('Hatches over left unreadable label','drawing',[180,708,296,781],'six slanting hatch strokes')
inv('Hatches over PTTM label','drawing',[447,699,626,780],'six slanting hatch strokes')
inv('Bertin/Mme low connecting cancellation','drawing',[190,831,1405,999],'line from Bertin to Mme and seminar row')
inv('Bertin/Mme repeated broad wave','drawing',[268,834,1185,988],'five high turns and intervening low waves')
inv('Bertin/Mme upper right turned contour','drawing',[1077,799,1407,934],'turned line above photocopies to Exp 7')
inv('Thin oval around Notes sur R.R.','drawing',[528,1177,884,1258],'oval around cancelled RR item')
inv('Live question mark outside RR oval','text',[886,1193,918,1237],'?')
inv('Second closing curve after Amsterdam question','drawing',[1451,1320,1567,1388],'question mark, small close, larger close')
inv('Brace grouping Serre subjects','drawing',[846,1398,872,1496],'left brace beside two physical subject lines')
inv('Long vertical rule at left of Deligne note','drawing',[1233,1465,1249,1628],'separate left vertical rule')
inv('Thin cancellation from Berthelot label','drawing',[274,1539,574,1983],'descending diagonal through lower labels/entries')
inv('Thin cancellation beginning near first lower RR entry','drawing',[653,1548,958,2005],'long diagonal down/right')
inv('Thin cancellation beginning above Serre copy area','drawing',[970,1533,1211,1944],'long diagonal down/right')
inv('Thin cancellation beneath Deligne note and terminal spurs','drawing',[1274,1507,1454,1848],'diagonal with two small terminal spurs near lower report','main manuscript hand, thin pen','The note-line anchor, shaft and two spurs are drawn explicitly.')
inv('Broad wavy lower cancellation','drawing',[550,1654,1447,2062],'long repeated down/up wave across Kleiman through final row')
inv('Rounded outer right cancellation contour','drawing',[1040,1649,1606,2053],'top arch and long right descending side')
inv('Archive pencil number, comment only','text',[53,2059,102,2119],'2','archive pencil hand not identified','Encoded only as the required archive-number comment; not an authorial page number.')

report['remaining_doubts']=[dict(place=x['place'],reading=x['decision'],alternatives=x['decision'],confidence=x['confidence']) for x in report['c_doubts'] if x['status'] in ['retained','revised preference']]
report['remaining_doubts'] += [
 dict(place='Quillen title terminal marks',reading=r'\unsure{....|\ldots}',alternatives=['four points','three points, last short trace belongs to oval'],confidence='medium'),
 dict(place='Raised Hartshorne parenthesis',reading=r'\unsure{ch.|coh.}',alternatives=['ch.','coh.'],confidence='low'),
 dict(place='Initial 3 underline',reading=r'\unsure{\uline{3}|3}',alternatives=['independent underline','faint low trace unrelated to underline'],confidence='low'),
 dict(place='Point beneath Artin numeral/cross',reading=r'\unsure{\tikz[baseline=0pt]{\fill (0,0) ellipse (.55pt and .22pt);}}',alternatives=['detached cancellation ink','unassigned point'],confidence='low'),
 dict(place='Hartshorne contours near x=900,y=350',reading='two nearby but separately drawn contours',alternatives=['physical contact may occur','separate near-contacting paths'],confidence='low')]
report['notes']=[
 'This is a handwritten inventory/checklist of mathematical papers, notes, letters and copied material, arranged beside underlined names on a printed IHES letterhead. Many entries have local strokes, several have additional grouped cancellations, and a smaller group remains live.',
 'The live central entries include R. Wood à Bourbaki, Résumé PTT Grenoble, the double-underlined Papiers Atiyah heading, the Dieudonné letter, the determinant/Picard note, the raised Hartshorne/Goodman entry, the Hirzebruch item and the two Serre subjects. This describes their source state, not the status or whereabouts of the documents named.',
 'Explicit source hesitations are the question mark after the circled “Notes sur R.R.” and the question mark in “Congrès d\'Amsterdam ? ) )”. The small and larger closing curves after the latter are both visible.',
 'The short date under the Artin entry is read tentatively as 10.5.66, with 10.3.66 and 10.I.66 retained. It is itself crossed. No calendar inference was used to select the middle digit.',
 'The pencilled lower-left 2 is recorded as an archive-number comment only. The visible IHES text includes the printed postal line and telephone line.',
 'All C/H-agreement text was read from the halves, including the longer live entries and each lower cancelled list line. C and H were used as unverified witnesses, not as substitutes for ink.',
 'H’s separate note is editorial commentary, not source ink. It is not reproduced. H’s descriptions of the RR enclosure are identified as descriptions in the corresponding difference, rather than falsely quoted as manuscript words.',
 'The complete reading uses one positioned TikZ list so the raised and staggered additions and all long cancellation tracks remain associated with the affected rows. It contains no new notation macro. Graphic paths are schematic reproductions of observed strokes; near-contact at the Hartshorne contours is not made a definite junction.'
]
report['notation']=[
 {'form':r'$\overline{\underline{\mathrm{XII}}}$','place':'SGA 6','decision':'Plain handwritten X and two I uprights, with independent cap/base rules; not XIV.'},
 {'form':r'$\overline{\underline{\mathrm{III}}}$','place':'Algèbre III','decision':'Three plain uprights, independently checked in half a, with cap and base.'},
 {'form':r'$\overline{\underline{\mathrm{IV}}}$','place':'Bertin EGA','decision':'Ordinary handwritten roman IV, with separate upper/lower rules.'},
 {'form':r'$\overline{\underline{\mathrm{IV}}}$','place':'Ferrand EGA','decision':'Ordinary handwritten roman IV, checked separately; upper/lower rules.'},
 {'form':r'$\overline{\underline{\mathrm{IV}}}$','place':'Kleiman EGA','decision':'Ordinary handwritten roman IV; separate rules amid the deletion.'},
 {'form':r'$\overline{\underline{\mathrm{V}}}$','place':'EGA V','decision':'Ordinary handwritten V, with distinct cap/base.'},
 {'form':r'\unsure{$B_G$|$B_g$}','place':'Giraud','decision':'Plain looped B; lowered right G/g ambiguity retained at its only occurrence.'},
 {'form':r'$L$','place':'Serre upper subject','decision':'Plain capital L on the subject baseline, not raised.'},
 {'form':r'$\unsure{\ell|l}$','place':'Cancelled adic cohomology','decision':'Looped lowercase pen form; ell/cursive-l distinction remains unresolved.'},
 {'form':r'${\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0$','place':'Notes Serre','decision':'Plain lower letters under a raised cluster; equals and baseline oval zero are visible. No alphabet substitution or exponent normalization.'},
 {'form':r'$K(\mathrm{P}^{n}(\unsure{\mathrm L^{-}|\overline{\mathrm L}|\overline{\mathrm C}}))$','place':'Calcul','decision':'Plain handwritten K/P and inner letter; independent raised n and short high/right bar. No blackboard or script alphabet inferred.'},
 {'form':r'\unsure{$C_i$|$C_1$}','place':'Final Greenberg entry','decision':'Plain capital C with lowered right small mark; i/1 remains local.'},
 {'form':'1','place':'Shih, Ferrand, Jouanolou','decision':'Each detached pale numeral independently seen; no superscript reference function assigned.'}
]
report['abbreviations']=[
 {'form':'conj.','expansion':'conjecture (editorial expansion)'},
 {'form':'op.','expansion':'opérateurs (editorial expansion)'},
 {'form':'dim','expansion':'dimension (editorial expansion; source has no point)'},
 {'form':'dim.','expansion':'dimension (editorial expansion; source has a point in the raised parenthesis)'},
 {'form':'ch. | coh.','expansion':'cohomologique/cohomologie (conditional editorial expansion; the literal abbreviation remains doubtful)'},
 {'form':'cat.','expansion':'catégorie(s) (editorial expansion; number not supplied)'},
 {'form':'dét.','expansion':'déterminant (editorial expansion)'},
 {'form':'équ.','expansion':'équation (conditional editorial expansion)'},
 {'form':'Exp','expansion':'exposé (editorial expansion; no source point supplied)'},
 {'form':'Mme | Mne','expansion':'Madame (conditional editorial expansion of Mme only)'},
 {'form':'fasc.','expansion':'fascicule (editorial expansion)'},
 {'form':'Chev.','expansion':'Chevalley (proposed editorial expansion; kept abbreviated in the reading)'},
 {'form':'RR / R.R.','expansion':'Riemann–Roch (editorial expansion; source punctuation differs locally)'},
 {'form':'SGA / EGA','expansion':'Acronym expansion not established from this sheet; none supplied in transcription.'},
 {'form':'PTT / PTTM','expansion':'Expansion not established from this sheet; none supplied.'},
 {'form':'R.','expansion':'Personal initial; full name not supplied by this page.'}
]
report['math_checks']=[
 {'type':'ink/placement check only','place':'Notes Serre formula','result':'Read the equality and baseline zero and retained the uncertain base letters and exponent. No truth of the formula was checked.'},
 {'type':'ink/placement check only','place':'Calcul K expression','result':'Checked that the raised n belongs to P and that the opening curve follows K. The inner bar placement remains uncertain; no K-theory computation was performed.'},
 {'type':'document classification','place':'whole page','result':'The sheet records document titles and subjects. It supplies no mathematical derivation or argument to verify, and this reading is not described as a proof.'}
]
report['workflow_feedback']=[
 'Viewed the whole image once and each supplied half once. Dimensions are 1683×2150 for the whole and 1683×1155 for each half; half b begins at whole y=995. Thirty-six local crops were made with the supplied crop.py and each was viewed once.',
 'All required briefs and PREAMBLE.tex were read. An initially truncated combined text output was replaced by complete separate reads of conventions, preamble and notation. The corrected current-page C_questions.md was reloaded; removed out-of-page snippets were not used.',
 'The complete reading.tex was saved before this longer report. No OCR, recognition, web, external edition, other page image, other reader file or root decision file was consulted; no subagent was spawned.',
 'A final new local question about the underline under 3 was resolved by its one permitted crop; the numeral stayed definite and underline uncertainty is marked.',
 'No TeX compilation was performed. A text-only audit checks literal witness quotations, complete nonempty reading fields, allowed kind values, exact inventory transcribed=yes, and correspondence of the described graphic tracks to saved drawing commands.'
]

if errors:
    raise ValueError('Witness strings not found literally: '+repr(errors))
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Saved report.json: {len(D)} differences; {len(report["c_doubts"])} C doubt/notation decisions; {len(report["inventory"])} inventory elements; {len(report["remaining_doubts"])} remaining doubts; {len(manifest)} crops.')
