from pathlib import Path
import json

BASE=Path('/workspace/scratch/d27bd2a88bca')
PAGE='H162-01_162-1_scan003'
WORK=BASE/'out/work'
META=json.loads((WORK/f'{PAGE}_cropmeta.json').read_text())
DRAFT=(WORK/f'{PAGE}_draft.tex').read_text()
TOP=DRAFT[DRAFT.index(r'\figure{'):DRAFT.index(r'\uline{Shih}')].strip()
MARGIN=DRAFT[DRAFT.index(r'\margin{\begin{tikzpicture}'):DRAFT.index('% The diagonal marginal arrow')].strip()
R={
'b01':r'\deleted{\uline{Deligne} (suite)\quad \unsure{Hironaka}, thèse}',
'b02':r'\tikz[baseline=-.45ex]{\draw (0,0)--(.06,.52) (.09,.04)--(.15,.49);}\,\deleted{\unsure{Griffiths} \unsure{périodes}\unsure{\ldots|.}}',
'b03':r'\deleted{\unsure{SGA|SG} 6 $\overline{\underline{\mathrm{XII}}}$}',
'b04':r'\deleted{Classes de Chern des représentations.}',
'b05':r'\deleted{Quillen : sur \unsure{conj.} de Adams}',
'b06':r'\deleted{\unsure{2|2)}\deleted{\unsure{x|X}}\unsure{lettre} : Artin (sur Atiyah-Adams)}',
'b07':r'\inserted{\deleted{\unsure{10.5.66|10.3.66}}}',
'b08':r'\deleted{Thèse \uline{Goodman}}',
'b09':r'\tikz[baseline=(qq.base)]{\node[inner sep=2pt] (qq) {\deleted{Quillen Deviations \ldots}};\draw (qq.center) ellipse [x radius=7.3em,y radius=.8em];}',
'b10':r'\deleted{Hartshorne On Cohomological dimensions..}',
'b11':TOP,
'b12':'% letterhead\nINSTITUT\\\\\nDES HAUTES ÉTUDES SCIENTIFIQUES\\\\\n91 - BURES-SUR-YVETTE\\\\\n928-48-53',
'b13':r'\deleted{\uline{Giraud}\quad Notes sur $B_G$}',
'b14':r'\deleted{\uline{Klose}\quad lettre sur \unsure{Ulmers|Ulmer}}',
'b15':r'\deleted{Notes Algèbre $\overline{\underline{\mathrm{III}}}$ Bourbaki}',
'b16':r'\uline{Shih}\quad 1',
'b17':r'Rapport à Bourbaki calcul différentiel',
'b18':r'\deleted{\uline{3} articles Schwarzenberger sur fibrés vectoriels}',
'b19':r'\deleted{\uline{\unsure{N|M}\illegible{1}}}\qquad \deleted{\unsure{PTTM|PTT M}}',
'b20':r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}',
'b21':r'\deleted{\uline{Bertin}\qquad EGA $\overline{\underline{\mathrm{IV}}}$ \unsure{16--19|16 19} photocopies}',
'b22':r'\deleted{\unsure{Mme|Mne} \uline{\unsure{Hakim}}}',
'b23':r'\deleted{Séminaire Gabriel deux schémas, Exp $7$}',
'b24':r'\uline{Ferrand}\quad 1',
'b25':r'\deleted{EGA $\overline{\underline{\mathrm{IV}}}$ 20,21 \deleted{\unsure{photocopies}} épreuves}',
'b26':r'Lettre : Dieudonné sur par.factoriel en dim 2',
'b27':r'\tikz[baseline=(rr.base)]{\node[inner sep=2pt] (rr) {\deleted{Notes sur R.R.}};\draw (rr.center) ellipse [x radius=3.1em,y radius=.74em];}\ ?',
'b28':r'Notes sur le foncteur dét. / \uline{sur cat. de Picard} .',
'b29':r'\inserted{Papiers Hartshorne (dim. \unsure{ch.|coh.}) et Goodman}',
'b30':r'\uline{Jouanolou}\quad 1',
'b31':r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}',
'b32':r"Papier Hirzebruch (Congrès d'Amsterdam ?) )",
'b33':r'Lettre : Serre $\left\{\begin{array}{l}\text{\unsure{équ.} fonctionnelle \unsure{fonction|fonctions} }L\\ \text{suite, début de monodromie \unsure{....|\ldots}}\end{array}\right.$',
'b34':r'\deleted{\uline{Berthelot}\qquad Notes sur stratifications}',
'b35':MARGIN,
'b36':r'\deleted{Notes RR (copie de Serre)}',
'b37':r'\deleted{Notes Serre sur ${\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0$}',
'b38':r'\deleted{Calcul $K\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}(\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}))$}',
'b39':r'\deleted{Rapport Serre représentations de groupes finis}',
'b40':r'\deleted{\uline{Kleiman}\qquad \unsure{photocopies|Photocopies} EGA $\overline{\underline{\mathrm{IV}}}$ 20}',
'b41':r'\deleted{EGA $\overline{\underline{\mathrm{V}}}$}',
'b42':r'\deleted{Notes Chev. sur \unsure{grassmanniennes|grassmaniennes}}',
'b43':r'\deleted{Note \unsure{Agison|Agišon} \unsure{bidéterminants|holodéterminants}}',
'b44':r'\deleted{Problèmes de Géométrie Algébrique}',
'b45':r'\deleted{\uline{Verdier}\qquad \unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}',
'b46':r'\deleted{\unsure{Gabriel}}',
'b47':r'\deleted{\uline{\unsure{Terjanian|Terzanian}}}',
'b48':r'\deleted{\unsure{Articles|Article} Greenberg sur \unsure{$C_i$|$C_1$}}',
'b49':'% archive sheet number: 2',
}
CHANGES=[]
def add(b,c,h,description,kind='misread word',cc=False,ch=True,confidence='high',marked=False,certainty=False,consequential=False):
    CHANGES.append({'id':f'r{len(CHANGES)+1:02d}','line':META[b]['line'],'c':c,'h':h,'final':R[b],
      'scan_shows':description,'crop':META[b]['crop'],'box':META[b]['box'],'confidence':confidence,'kind':kind,
      'changed_C':cc,'changed_H':ch,'marked_in_H':marked,'consequential':consequential,'certainty_only':certainty})

add('b01',r'\deleted{\uline{Deligne} (\unsure{suite})\quad \unsure{Libermann|Libermans}, thèse}',r'\textbf{Deligne} \emph{(suite)} — \struck{Hironaka, thèse}',
    'Top entry: the horizontal cancellation crosses Deligne, the parenthesis, and the thesis name. The parenthesis reads suite. After the independent root crop review, Hironaka is preferred to C’s Libermann/Libermans: an H-like opening and the terminal sequence support it, but the central letters remain crossed, so the whole name stays doubtful. H incorrectly leaves Deligne (suite) live.',cc=True,ch=True,confidence='medium')
add('b02',R['b02'],r'\struck{\uncertain{Griffiths} périodes}',
    'At the top of the right column: two separate near-vertical pen strokes precede the cancelled, stained Griffiths/périodes entry. Faint terminal points or a point remain after périodes. C’s name, noun and punctuation doubts are retained; H omits the separate strokes and terminal punctuation.',kind='omission',marked=True,confidence='low')
add('b03',R['b03'],r'\struck{SGA 6 XIV}',
    'Immediately below Griffiths: the barred Roman numeral has X followed by two uprights, XII, not XIV. The initial SGA/SG is obscured by the stain and cancellation and remains doubtful. Both upper and lower Roman-numeral rules are retained.',kind='misread symbol or index',confidence='medium')
add('b04',R['b04'],r'\struck{Chern et classes de Chern des représentations}',
    'The line begins Classes de Chern des représentations. There is no preceding Chern et. A terminal point is visible and the full entry is cancelled.',kind='text not on the page')
add('b05',R['b05'],r'\struck{Quillen sur \uncertain{sém.} de Adams}',
    'Between Quillen and Adams: a colon follows Quillen, then sur and a compact conj.-like abbreviation with a descending j. It is not H’s sém. The cancelled abbreviation stays doubtful as in C.',confidence='medium',marked=True)
add('b06',R['b06'],r'\struck{2 lettres à \ill\ sur Atiyah--Adams)}',
    'The crossed entry has an initial 2-like mark, a separately crossed x/X, lettre, a colon, and Artin, followed by the parenthetical sur Atiyah-Adams. The opening cancellation leaves the 2/2), x/X and singular lettre doubtful. H loses Artin, the colon, opening parenthesis and the earlier crossed x/X, and gives lettres à.',confidence='medium',marked=True)
add('b07',r'\inserted{\deleted{\unsure{10.3.66|10.5.66}}}',r'\add{du} 10.I.66',
    'Beneath the Artin entry: the inserted date is itself cancelled. The middle digit has a descending left stroke and lower curved part, favoring 5 over 3; its upper construction is crossed, so both remain. H’s I and added du are not supported, and H loses the date’s cancellation.',kind='misread symbol or index',cc=True,confidence='medium',consequential=True)
add('b08',R['b08'],r'\struck{thèse \ill}',
    'The cancelled line reads Thèse Goodman. Goodman is readable and separately underlined; H’s illegible thesis name is recoverable.',kind=r'readable ink left as \ill{}',marked=True)
add('b09',r'\deleted{Quillen \unsure{Deviations|Derivations} \ldots}',r'Quillen, \emph{Derivations} \ill',
    'The word after Quillen has De followed by v and i; no extra r appears as in Derivations. Deviations is cancelled by a horizontal stroke through the line, and the whole Quillen entry is also enclosed in a thin oval. C loses the oval and leaves the word doubtful; H misreads the title and gives the entry live. The terminal points are retained.',cc=True,confidence='high',marked=True)
add('b10',r'\deleted{Hartshorne \uline{On Cohomological \unsure{dimension|dimensions}}\unsure{..|\ldots}}',r'\struck{Hartshorne \ill\ cohomologie \ill}',
    'The cancelled Hartshorne entry reads On Cohomological dimensions, with a visible final s and two separate terminal points. The lower long line belongs to the branching callout geometry rather than an independent title-only underline; that geometry is preserved in the positioned upper block.',cc=True,marked=True)
add('b11','No separate branching callout; title underlined in the Hartshorne entry','No branching callout recorded',
    'A long line begins in the blank area above the letterhead, bends down beside the right column, and branches: the upper branch ends in a right arrowhead just above the Hartshorne entry; the lower branch passes below that entry. The Quillen oval is separate. The full upper layout is reproduced in TikZ so the lines remain attached to their observed positions.',kind='drawing or diagram',cc=True,confidence='high')
add('b12',R['b12'],'(printed letterhead omitted)',
    'The printed stationery has four lines: INSTITUT; DES HAUTES ÉTUDES SCIENTIFIQUES; 91 - BURES-SUR-YVETTE; 928-48-53. The Giraud cancellation crosses the vicinity of the phone line, but is attached to the handwritten register entry. H omits the letterhead.',kind='omission')
add('b13',r'\deleted{\uline{Giraud}\quad Notes sur \unsure{$B_G$|$B_g$}}',r'\textbf{\struck{Giraud}} — \struck{Notes sur \ill\ 67}',
    'In the cancelled Giraud entry, the whole final formula is B with a lowered G. The lower glyph has an open bowl/right return, rather than a closed upper loop of g. It is not a separate 67 after an unreadable phrase. The underlined Giraud and cancellation are retained.',kind='misread symbol or index',cc=True,marked=True)
add('b14',R['b14'],r'\textbf{\struck{\ill}} — \struck{Lettre sur Hartshorne}',
    'The underlined cancelled left name is Klose. The right entry starts lower-case lettre sur and ends in a name with initial U and tall l, consistent with Ulmers/Ulmer, not Hartshorne. Heavy cancellation conceals the terminal s question, so C’s alternative remains.',confidence='medium',marked=True)
add('b15',R['b15'],r'\struck{Notes Algèbre III Bourbaki}',
    'The cancelled Notes Algèbre entry contains III with an upper and lower rule. H’s unadorned III omits these visible rules.',kind='misread symbol or index')
add('b17',R['b17'],'R. Wood à Bourbaki, calcul différentiel',
    'The live entry opposite Shih reads Rapport à Bourbaki calcul différentiel. The a and o are small loops/points and the two p descenders join into a W-like form; they form a single word Rapport, not an initial R. and surname Wood. No comma is visible after Bourbaki.')
add('b18',r'\deleted{\uline{3} articles Schwarzenberger sur \unsure{fibrés|fibrés,} vectoriels}',r'\struck{3 articles Schwarzenberger sur fibrés vectoriels}',
    'In the cancelled three-article entry, fibrés is followed by a clear gap before vectoriels; there is no separate comma in that gap. C’s comma alternative is removed. The source’s 3 is also underlined.',kind='other',cc=True,ch=False,certainty=True)
add('b19',R['b19'],r'\textbf{\struck{\ill}} — \struck{\ill}',
    'On the next entry, an underlined crossed borrower name starts with N/M but the remaining letters cannot be recovered securely. The right-hand crossed capital sequence is tentatively PTTM or PTT M. H leaves both spans wholly illegible; C’s partial readings and doubts are retained.',kind=r'readable ink left as \ill{}',confidence='low',marked=True)
add('b20',R['b20'],'Papiers Atiyah, topologie et opérateurs elliptiques',
    'The live entry reads Papiers Atiyah topologie et op. elliptiques. The abbreviation op. is explicit and is not expanded. Papiers Atiyah has two rules beneath it, while topologie and op. elliptiques each have one. No comma separates Atiyah from topologie.',kind='abbreviation expanded or spelling modernised')
add('b21',r'\deleted{\uline{Bertin}\qquad EGA $\overline{\underline{\mathrm{IV}}}$ 16--19 \unsure{photocopies}}',r'\textbf{\struck{Bertin}} — \struck{EGA IV 16--19, photocopie}',
    'The cancelled Bertin entry has a barred IV, the numbers 16 and 19, and the readable plural photocopies. A separate range dash is not distinguishable from the cancellation, so a new 16--19/16 19 doubt is shown. H’s singular photocopie and added comma do not match the line.',cc=True,confidence='medium')
add('b22',r'\deleted{\unsure{Mme|Mne} \uline{\unsure{Mathieu|Mathies}}}',r'\textbf{\struck{Mme Hakim}}',
    'The cancelled underlined name favors Hakim: an H-like initial, a, one forked k stem, an i dot, and a final m. It does not show a separate t and h as in Mathieu. Cancellation still affects the small strokes, so Hakim remains explicitly doubtful. The preceding Mme/Mne uncertainty is retained.',cc=True,ch=False,confidence='medium')
add('b23',r'\deleted{Séminaire Gabriel deux schémas, \unsure{Exp|Ex.} $\unsure{7|\mathrm I}$}',r'\struck{Séminaire Gabriel, deux séminaires, exp.~7}',
    'The cancelled item reads Séminaire Gabriel deux schémas, Exp 7. The second long noun is schémas, not séminaires. Exp has a descending p, with no secure separate abbreviation point, and the final numeral has the shape and middle cross-stroke of 7, not Roman I. No comma follows Gabriel.',cc=True,confidence='high')
add('b25',R['b25'],r'\struck{EGA IV 20, 21} \struck{\ill}',
    'Beside live Ferrand 1, the entire EGA IV 20,21 line is cancelled. Within it photocopies is separately hatched/cancelled before épreuves. The earlier word remains doubtful under the hatching, but épreuves is readable. Both rules of IV and the two levels of cancellation are retained.',kind='omission',confidence='medium',marked=True)
add('b26',r'Lettre : Dieudonné sur \unsure{parafactoriel|par.factoriel} \unsure{en|de} dim 2',r'Lettre à Dieudonné sur \ill\ de dimension 2',
    'The live letter entry has a colon after Lettre, a clear point after par, then factoriel, en, and dim 2. The preposition lacks a d ascender and reads en. H’s à, de and expansion dimension are not the written forms. C’s abbreviation and preposition doubts are resolved.',cc=True,confidence='high',marked=True)
add('b28',r'Notes sur le \unsure{foncteur} dét. / \uline{sur cat. de Picard} .',r'Notes sur \ill\ dét.\ / sur cat.\ de Picard \add{et} Godement',
    'The line beneath the circled R.R. note reads Notes sur le foncteur dét. / sur cat. de Picard, followed by a terminal point. Foncteur is readable; sur cat. de Picard is underlined. H’s et Godement belongs to its misreading of the separate inserted line below, not this entry.',kind=r'readable ink left as \ill{}',cc=True,marked=True)
add('b29',r'\inserted{Papiers Hartshorne (dim. coh.) et Goodman}',r'\add{et} Godement ; \struck{Papiers \uncertain{Hertzbrouck}}',
    'Between the determinant/Picard entry and the cancelled cohomology entry is the live inserted line Papiers Hartshorne (dim. ch./coh.) et Goodman. Hartshorne and Goodman are separate readable names, not H’s Hertzbrouck and Godement. The compact abbreviation after dim. appears ch.-like but may contain a compressed o; both are retained. Its position supports C’s interlinear placement near the Jouanolou group, without an explicit caret.',kind='insertion or placement',cc=True,confidence='medium',marked=True)
add('b31',R['b31'],'(line omitted; H attaches a cancelled Papiers Hertzbrouck reading to this region)',
    'Directly beneath the inserted Hartshorne/Goodman line, a separate cancelled line begins Notes cohomologie and ends in an ell/l-adique expression. It is distinct from the inserted papers entry. The looped-versus-plain l question remains under the cancellation.',kind='omission',confidence='medium',marked=True)
add('b32',r"Papier Hirzebruch (Congrès d'Amsterdam \unsure{?\,)|?} )",r"Papiers Hirzebruch (congrès d'Amsterdam ?)",
    'The first noun is singular Papier. After the conference note’s question mark, a short right parenthesis is followed by a second, larger right parenthesis. Both closing marks are visible and are retained, leaving the source’s unmatched extra close unchanged.',kind='other',cc=True,confidence='high')
add('b33',r'Lettre : Serre {\unsure{équ.} fonctionnelle \unsure{fonction|fonctions} L; suite, \unsure{début|défaut} de monodromie \unsure{....|\ldots}}',r'Lettre : Serre \add{sur} \ill\ fonctionnelles, suite, début de monodromie \ill',
    'The Serre entry has a left brace with two lines. The first includes the doubtful abbreviated équ., singular fonctionnelle, another fonction/fonctions word, and capital L. The second reads suite, début de monodromie and a series of points. The b in début is visible, so défaut is rejected. There is no added sur after Serre. The first abbreviation, second noun’s ending and dot count remain doubtful.',kind='omission',cc=True,confidence='medium',marked=True)
add('b35',r'\margin{\noindent\vrule height 1ex depth 4.8ex width .35pt\hspace{.2em}\parbox[t]{.86\linewidth}{\deleted{Lettre Deligne \unsure{complexes} elliptiques}}}',r'\struck{lettre Deligne sur opérateurs elliptiques}',
    'At the right margin, two cancelled lines read Lettre Deligne complexes / elliptiques. The first noun remains doubtful under its strike, but there is no separate sur and no opérateurs. A vertical rule stands at the left and a distinct diagonal arrow descends toward the lower cancelled block. C omits the arrow; H loses the marginal geometry and changes the words.',kind='drawing or diagram',cc=True,confidence='medium')
add('b36',R['b36'],r'\struck{Notes R.R.\ (copie de Serre)}',
    'The cancelled item reads Notes RR (copie de Serre). The two R letters are written without the interposed/terminal points that occur in the earlier R.R. entry; H regularizes this occurrence to R.R.',kind='misread symbol or index')
add('b37',R['b37'],r'\struck{Notes Serre sur \ill}',
    'The entire cancelled formula after Notes Serre sur was inspected together. A ch/dh-like base with superscript n-i/n-1/n-nu, then =0, is partly readable, but two heavy cancellation strokes cross its letters and exponent. All C alternatives remain; no expected mathematical vanishing statement is substituted.',kind=r'readable ink left as \ill{}',confidence='low',marked=True)
add('b38',R['b38'],r'\struck{Calcul \ill}',
    'The full cancelled K-expression shows K, a parenthesis/C-like sign, P with n above it, an inner parenthesis, an L/C-like glyph with a short upper bar or minus, and closing parentheses. C’s whole expression and its alternatives are retained. The ink does not decide a standardized projective-space formula.',kind=r'readable ink left as \ill{}',confidence='low',marked=True)
add('b39',R['b39'],r'\struck{Rapport Serre, représentations de groupes finis}',
    'The cancelled entry reads Rapport Serre représentations de groupes finis. There is no separate comma after Serre; the crossing lines are cancellations.',kind='text not on the page',confidence='medium')
add('b40',R['b40'],r'\textbf{\struck{Kleiman}} — \struck{Manuscrits ? EGA IV 20}',
    'After the cancelled underlined Kleiman, the crossed word is photocopies/Photocopies, not Manuscrits followed by a question mark. Initial case remains uncertain; the word’s remaining profile and letters fit photocopies. EGA IV 20 follows, with upper and lower rules on IV.',confidence='medium')
add('b41',R['b41'],r'\struck{EGA V}',
    'The cancelled EGA V entry has a separate top rule and a separate bottom rule around V. These are retained as barred Roman-numeral construction.',kind='misread symbol or index')
add('b42',R['b42'],r'\struck{Notes Chevalley sur groupes \ill}',
    'The first name is written in the abbreviated form Chev., not expanded Chevalley. The following long word begins grass- and continues with the grassmanniennes/grassmaniennes profile, not the shorter groupes. The crossed repeated-n sequence remains doubtful.',kind='abbreviation expanded or spelling modernised',confidence='medium',marked=True)
add('b43',R['b43'],r'\struck{Notes \ill}',
    'The cancelled entry begins singular Note, followed by an Agison/Agišon-like name and a long determinant word. The name and bidéterminants/holodéterminants alternatives remain unresolved under crossing strokes. H’s wholly illegible remainder loses this partly recoverable content.',kind=r'readable ink left as \ill{}',confidence='low',marked=True)
add('b44',R['b44'],r'\emph{Problèmes de Géométrie Algébrique}',
    'A cancellation passes through the whole Problèmes de Géométrie Algébrique line, with additional group-cancellation strokes crossing it. H presents the entry as live italic text.',kind='deletion state (struck given live or live given struck)')
add('b45',R['b45'],r'\textbf{\struck{Verdier}} — SGA 4 fasc.~1, \ill',
    'The long cancellation crosses both the underlined Verdier and the right-hand entry. The final A/4 in SGAA/SGA 4 stays doubtful. The words fasc. 1, mon exemplaire personnel are readable beneath the strike. H leaves the right-hand item live and its last phrase illegible.',kind='deletion state (struck given live or live given struck)',confidence='medium',marked=True)
add('b47',R['b47'],r'\textbf{\struck{\ill}}',
    'The underlined cancelled borrower name has the Terjanian/Terzanian sequence. The long descending middle glyph may be j or the writer’s descending z, and its top is crossed; C’s two alternatives are retained. H’s whole-name illegibility is excessive.',kind=r'readable ink left as \ill{}',confidence='medium',marked=True)
add('b48',R['b48'],r'\struck{Article \uncertain{Grünberg} sur \ill}',
    'The final cancelled entry has Articles/Article, then Greenberg: two e-like low loops appear before n and there is no umlaut. After sur the whole formula is C with a lowered i/1-like mark. The noun’s final s and index remain doubtful, but H’s Grünberg is not supported.',confidence='medium',marked=True)

DOUBTS=[]
def doubt(line,reading,alternatives,reason,confidence='medium'):
    DOUBTS.append({'line':line,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason})
doubt('L01',r'\unsure{Hironaka}',['Hironaka'],'The preferred name follows the full letter profile and the independent root crop review. A strong cancellation crosses its central letters; confidence is not sufficient to remove a whole-name doubt.')
doubt('L02',r'\unsure{Griffiths}',['Griffiths'],'Staining and two cancellation strokes interrupt several letters of the name.','low')
doubt('L02',r'\unsure{périodes}',['périodes'],'The faint noun under the cancellation is compatible with périodes, but not every letter survives distinctly.','low')
doubt('L02',r'\unsure{\ldots|.}',[r'\ldots','.'],'The terminal faint points/streaks after périodes cannot be counted securely.','low')
doubt('L03',r'\unsure{SGA|SG}',['SGA','SG'],'The opening letters sit under staining and cancellation; the last A cannot be separated confidently.','low')
doubt('L05',r'\unsure{conj.}',['conj.'],'The compact abbreviation has a j-like descender, but the cancellation overlaps its small middle letters.')
doubt('L06',r'\unsure{2|2)}',['2','2)'],'The initial 2 is recognizable; an adjoining mark may be a close parenthesis or belong to the cancellation.')
doubt('L06',r'\deleted{\unsure{x|X}}',['x','X'],'The earlier crossed x/X is overlaid by the larger cancellation; its case is uncertain.','low')
doubt('L06',r'\unsure{lettre}',['lettre'],'The letter-entry noun is heavily struck; singular lettre is preferred without silently adding H’s final s.')
doubt('L07',r'\unsure{10.5.66|10.3.66}',['10.5.66','10.3.66'],'The cancelled inserted date has a middle digit with a stem and lower curve favoring 5; the top is crossed, so 3 remains possible. H’s I is not preferred.')
doubt('L12',r'\unsure{Ulmers|Ulmer}',['Ulmers','Ulmer'],'The initial U and l are visible, but the terminal part is under two heavy cancellation strokes.','low')
doubt('L17',r'\uline{\unsure{N|M}\illegible{1}}',['N followed by an unreadable remainder','M followed by an unreadable remainder'],'The crossed underlined borrower name begins with an N/M-like capital. The following letter sequence cannot be recovered securely even on the enlarged crop. No external name is supplied.','low')
doubt('L17',r'\unsure{PTTM|PTT M}',['PTTM','PTT M'],'The capital sequence is separately hatched. The final M is visible, but its separation from PTT is uncertain.','low')
doubt('L19',r'\unsure{16--19|16 19}',['16--19','16 19'],'A separate dash between the two numbers cannot be distinguished from the cancellation that runs through them. Both numerals themselves are readable.')
doubt('L20a',r'\unsure{Mme|Mne}',['Mme','Mne'],'The small letters following the initial M are covered by the horizontal strike.','low')
doubt('L20a',r'\unsure{Hakim}',['Hakim'],'The single forked k stem and following i dot favor Hakim, but the initial and terminal connections are crossed. The name is kept cautious rather than silently certified.')
doubt('L21b',r'\deleted{\unsure{photocopies}}',['photocopies'],'The earlier word is separately hatched before épreuves and then the whole line is struck. Several internal letters remain obscured.','low')
doubt('I01',r'\unsure{ch.|coh.}',['ch.','coh.'],'The small abbreviation after dim. has a c-like curve and tall h; a compressed o may be present in the joining ink. The first reading follows the visible short profile, without expanding the abbreviation.')
doubt('I01','Placement of the Hartshorne–Goodman insertion',['interlinear addition above the cancelled Notes cohomologie entry in the Jouanolou group','unattached added item between the adjacent groups'],'Its position above the cancelled cohomology line supports C’s placement, but there is no unequivocal caret attaching it to a single borrower. The text is not merged into the preceding Picard entry.')
doubt('L25b',r'$\unsure{\ell|l}$-adique',[r'\ell-adique','l-adique'],'The letter preceding -adique is crossed and overlaps the inserted line’s descenders. Its looped-versus-plain form remains uncertain.','low')
doubt('L27',r'\unsure{équ.}',['équ.'],'The first abbreviated expression in the brace is compact; it is not expanded from the subject matter.')
doubt('L27',r'\unsure{fonction|fonctions}',['fonction','fonctions'],'The final joined stroke before L does not securely decide the second noun’s final s.')
doubt('L28',r'\unsure{....|\ldots}',['....',r'\ldots'],'The sequence of faint terminal points after monodromie remains uncertain in count.')
doubt('M02',r'\unsure{complexes}',['complexes'],'The profile and descender/ascender pattern favor complexes, but the strike crosses the small central letters. No sur is inserted.')
doubt('L31',R['b37'],[r'\mathrm{ch}^{n-i}=0',r'\mathrm{ch}^{n-1}=0',r'\mathrm{ch}^{n-\nu}=0',r'\mathrm{dh}^{n-i}=0',r'\mathrm{dh}^{n-1}=0',r'\mathrm{dh}^{n-\nu}=0'],'The whole formula is crossed by two heavy strokes. The base’s first letter and the last exponent character are not physically decidable. No mathematical expectation resolves them.','low')
doubt('L32',R['b38'],[r'K(\mathrm P^n(\overline{\mathrm L}))',r'K(\mathrm P^n(\mathrm L^{-}))',r'K(\mathrm P^n(\overline{\mathrm C}))',r'K\mathrm{CP}^n(\overline{\mathrm L}))',r'K\mathrm{CP}^n(\mathrm L^{-}))',r'K\mathrm{CP}^n(\overline{\mathrm C}))'],'The first parenthesis/C-like sign and inner barred L/C or L-with-minus remain under the cancellation. The apparent parenthesis counts are preserved rather than regularized.','low')
doubt('L34',r'\unsure{photocopies|Photocopies}',['photocopies','Photocopies'],'The first crossed loop/stem could be capital or lower-case; the word photocopies is otherwise supported.')
doubt('L36',r'\unsure{grassmanniennes|grassmaniennes}',['grassmanniennes','grassmaniennes'],'The repeated small n strokes are crossed and interleaved with the large group cancellation; they cannot be counted securely.','low')
doubt('L37',r'\unsure{Agison|Agišon}',['Agison','Agišon'],'The name’s small mark near the s may belong to the letter, a diacritic, or an intersecting stroke. The identity is not inferred externally.','low')
doubt('L37',r'\unsure{bidéterminants|holodéterminants}',['bidéterminants','holodéterminants'],'The crossed prefix and adjoining tall strokes do not decide between the two readings. The determinant word is not restored from a known title.','low')
doubt('L39',r'\unsure{SGAA|SGA 4}',['SGAA','SGA 4'],'The last glyph has an A/4-like construction under the cancellation; no series knowledge is used to regularize it.')
doubt('L40',r'\unsure{Gabriel}',['Gabriel'],'The cancelled name’s initial and middle profile are visible but the last letters meet dense crossing ink.')
doubt('L41a',r'\unsure{Terjanian|Terzanian}',['Terjanian','Terzanian'],'The middle descending glyph can be j or a descending handwritten z; its upper part is crossed.')
doubt('L41b',r'\unsure{Articles|Article}',['Articles','Article'],'The final stroke of the noun falls under the cancellation and does not decisively establish a final s.')
doubt('L41b',r'\unsure{$C_i$|$C_1$}',[r'C_i',r'C_1'],'The complete formula has C and a lowered short mark. A possible i dot coincides with the cancellation, so digit 1 cannot be excluded.')

# The inventory follows physical top-to-bottom position. A deletion item includes its text.
ITEMS=[]
def inv(b,kind,first,hand=None,position=None,box=None):
    bounds=box or META[b]['box']
    ITEMS.append({'scan':'3','sheet_kind':'handwritten register on printed stationery',
      'hand':hand or 'handwritten register in ink; hand unattributed; cancellation strokes in ink/pencil',
      'element':'','kind':kind,'position':position or f'original pixels x{bounds[0]}–{bounds[2]}, y{bounds[1]}–{bounds[3]}',
      'first_words_or_objects':first,'transcribed':'yes','_bounds':bounds})
for b in R:
    if b=='b11':
        inv(b,'drawing','Bent branching callout: upper right arrow and lower line around Hartshorne')
    elif b=='b12':
        inv(b,'text','INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53','printed letterhead')
    elif b=='b07':
        inv(b,'insertion',R[b])
        inv(b,'deletion',r'\deleted{\unsure{10.5.66|10.3.66}}')
    elif b=='b09':
        inv(b,'deletion',r'Quillen Deviations ...')
        inv(b,'drawing','Thin oval around the cancelled Quillen Deviations entry')
    elif b=='b27':
        inv(b,'deletion',r'Notes sur R.R.')
        inv(b,'drawing','Oval around the cancelled Notes sur R.R.')
        inv(b,'text','?',box=[883,1186,918,1235])
    elif b=='b29':
        inv(b,'insertion',R[b])
    elif b=='b33':
        inv(b,'display',R[b])
    elif b=='b35':
        inv(b,'margin note',r'\deleted{Lettre Deligne \unsure{complexes} elliptiques}')
        inv(b,'deletion',r'Lettre Deligne \unsure{complexes} / elliptiques',box=[1250,1458,1650,1530])
        inv(b,'drawing','Vertical left rule and diagonal descending arrow',box=[1227,1469,1385,1706])
    elif b=='b49':
        inv(b,'margin note','Archive sheet number 2','archive pencil numbering; hand unattributed')
    elif b in {'b16','b17','b20','b24','b26','b28','b30','b32'}:
        inv(b,'text',R[b])
    else:
        inv(b,'deletion',R[b])
inv('b02','drawing','Two near-vertical separate pen strokes before the Griffiths entry',box=[929,24,964,104])
inv('b25','deletion',r'\deleted{\unsure{photocopies}} inside the already cancelled EGA IV 20,21 entry',box=[892,1042,1149,1103])
inv('b06','deletion',r'\deleted{\unsure{x|X}} inside the cancelled letter entry',box=[944,211,988,264])
inv('b18','text','Résumé PTT Grenoble',box=[488,646,980,698])
ITEMS.sort(key=lambda v:(v['_bounds'][1],v['_bounds'][0],v['kind']))
for i,v in enumerate(ITEMS,1):
    v['element']=f'i{i:02d}'
    del v['_bounds']

BOXES=[]
for i,b in enumerate(R,1):
    x0,y0,x1,y1=META[b]['box']
    kind='deletion'
    if b in {'b16','b17','b20','b24','b26','b28','b30','b32'}: kind='text'
    if b=='b12': kind='text'
    if b in {'b07','b29'}: kind='insertion'
    if b in {'b02','b09','b11','b27'}: kind='drawing'
    if b=='b33': kind='display'
    if b in {'b35','b49'}: kind='margin note'
    if b=='b11':
        # Full upper block, so the callout has complete text/printed context, not cropped fragments.
        x0,y0,x1,y1=124,18,1669,505
    BOXES.append({'box':f's{i:02d}','kind':kind,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':R[b]})
BOXES.append({'box':'s50','kind':'text','x0':488,'y0':646,'x1':980,'y1':698,'reading':'Résumé PTT Grenoble'})

REPORT={
 'page':PAGE,
 'line_count':48,
 'changes':CHANGES,
 'doubts':DOUBTS,
 'inventory':ITEMS,
 'reading_notes':[
   'A handwritten lending register occupies printed IHES stationery. Borrower names stand mainly at the left, with papers or book sections to the right. Many individual entries and larger groups are cancelled.',
   'The list mentions theses, EGA and SGA portions, cohomology, Chern classes, topology, elliptic complexes, representations and algebraic geometry. These are labels for borrowed material, not an argument or a proof; the displayed vanishing/K expressions are not independently checked.',
   'There is one cancelled inserted date, tentatively 10.5.66 or 10.3.66. No date is established beyond those written alternatives. The lower pencil 2 is an archive sheet number, and the isolated 1 marks beside Shih, Ferrand and Jouanolou have no stated function or inferred count.',
   'The source explicitly has a question mark beside the circled Notes sur R.R. and another in the Amsterdam conference note. The Amsterdam note has two closing parentheses; that apparent source slip is retained.',
   'No overall register title or total page count is written on this sheet. The printed institutional letterhead is transcribed in full. The crossed thesis name and Mme name are preferred as Hironaka and Hakim, both cautiously; other badly cancelled names and titles remain doubtful.'
 ],
 'notes':[
   'Only the assigned scan003 packet and shared permitted reference files were consulted. No other page result, published text, external identity lookup, OCR, text-recognition tool, or TeX compilation was used.',
   'The whole image was inspected once for layout, followed by the upper and lower halves once each against both witnesses. All 49 saved evidence crops were then displayed and inspected.',
   'Crop b28 was extended at its right boundary to include the visible terminal point; it keeps the same crop ID. The updated crop was displayed. Slanted line crops have their clockwise rotation recorded in metadata.',
   'Every cancelled entry was checked, including the earlier x/X inside the cancelled letter entry, the inserted date that was itself cancelled, the separately hatched photocopies inside the cancelled Ferrand item, and the lower group cancellations.',
   'The broad wavy and diagonal strokes through the Bertin/Mme region and the lower register are treated as cancellation strokes, not as independent illustrative figures. The Quillen and R.R. ovals, upper branching callout, Serre brace, and right marginal rule/arrow are reproduced as visible nonverbal structure.',
   'The upper block uses positioned text nodes to retain the letterhead and callout geometry. This typesetting choice is not itself a textual change. It replaces C’s title-only underline on the Hartshorne entry with the observed lower callout line.',
   'Root independently inspected all saved crops while this first-reader report was prepared. Its review favored Hironaka and Hakim, retained the 5/3 date uncertainty and hard formula doubts, and confirmed the double close after the Amsterdam question mark. Those scoped findings are reflected here; this remains a candidate, not a page commit.',
   'H’s editorial prose about chronology or a following/other register page is not source ink and is not transcribed. Its added du, sur, punctuation, expanded words, and rearranged entry content are distinguished from actual page marks in the changes.',
   'H’s bold borrower-name formatting is treated as an equivalent convention where it represents the same source underline; such markup differences alone are not change records. H’s prose description of the R.R. oval/question mark is also not counted as an additional lexical difference.',
   'The unfamiliar names and compressed abbreviations are not supplied from biographical or mathematical knowledge. The two wholly crossed formulas remain whole-formula doubts rather than being normalized to expected formulas.',
   'The insert Papiers Hartshorne (dim. ch./coh.) et Goodman stands between lines. It is kept with the nearby Jouanolou/cohomology group as in C, but the absence of an unequivocal caret is noted as a placement doubt.',
   'No mathematical assertion was proved, computed, refuted, or adopted as a checked theorem in this reading. Consequently check_events is empty; all audit events below are visual only.'
 ],
 'check_events':[],
 'visual_audit_events':[
   {'statement_id':'scan003-layout','type':'visual transcription audit','outcome':'Whole and both half views establish the two-column handwritten register, printed letterhead, interlinear material, marginal note and archive 2. Visual check only.'},
   {'statement_id':'scan003-upper','type':'visual transcription audit','outcome':'Upper entries checked against both witnesses, with the thesis name, SGA numeral, Adams/Artin line, date, Goodman, Deviations, Hartshorne title and all cancellation states supported by saved crops.'},
   {'statement_id':'scan003-central','type':'visual transcription audit','outcome':'Central borrower/item lines checked letter by letter; Rapport, Hakim, schémas/Exp 7, nested photocopies, par.factoriel/en and the interlinear Hartshorne–Goodman entry are recorded without expansions.'},
   {'statement_id':'scan003-graphics','type':'visual transcription audit','outcome':'Both ovals, the upper branched callout with arrowhead, the Serre brace, the marginal vertical rule and diagonal arrow, and the source double closing parenthesis are preserved.'},
   {'statement_id':'scan003-lower-formulas','type':'visual transcription audit','outcome':'The entire ch/dh vanishing expression, the whole K-expression and the final C index were inspected from their own source boxes. Their doubts remain; no mathematical check was performed.'},
   {'statement_id':'scan003-completeness','type':'visual transcription audit','outcome':'All deleted/inserted spans, pen/pencil numerals, marginal material, differing words and open readings have neutral blind boxes with full target readings. All 49 evidence crops were displayed; no compilation was used.'}
 ],
 'notation':[
   r'On this sheet the Roman numerals XII, III, IV and V have distinct upper and lower rules, transcribed with \overline{\underline{\mathrm{...}}}; crossing-out strokes are not substituted for those rules.',
   r'The Giraud formula is $B_G$: the lowered G has an open bowl and right return. The first C B_g alternative is rejected on the whole formula crop.',
   r'The final C index remains \unsure{$C_i$|$C_1$}. The ch/dh exponent and barred-L K-expression remain whole-formula uncertainties.',
   'Source abbreviations are retained: conj., op., Exp, par.factoriel, dim, dét., cat., ch./coh., équ., Chev. and fasc. No name or title is expanded from external knowledge.',
   'RR in the lower copied-Serre entry has no visible points; the earlier circled R.R. entry has points after both letters. These occurrences are transcribed separately.',
   'The little 1 marks beside three live borrower names are transcribed as numerals, without interpreting their administrative meaning.'
 ],
 'hand_log':[
   '162-1/003, L14 and L33: p descenders in Rapport are long. In the compact live Rapport at L14, the adjacent pp join into a W-like form; H split this into R. Wood. The lower cancelled Rapport provides another long-descender occurrence, but the observation is scoped to this sheet.',
   '162-1/003, Hironaka/Hakim/Hartshorne entries: capital H can have a low curved bridge and an extended right stem, superficially resembling another capital. Full letter sequences, not name familiarity, control the readings; the crossed Hironaka and Hakim remain doubtful.',
   '162-1/003: several small a/o loops are reduced nearly to dots, especially in Rapport. Dots inside these connected words are not automatically punctuation.',
   '162-1/003: z may have a long descending return, visible in Hirzebruch. That habit prevents a silent resolution of the j/z alternative in the cancelled Terjanian/Terzanian name.',
   '162-1/003: all inspected Roman numerals in this register use separate upper and lower horizontal rules. The ordinary cancellation often crosses between them, so the numeral strokes and two rules must be counted separately.',
   '162-1/003: the inserted date’s middle digit is not certified from its expected chronology; the visible stem/lower curve favors 5 but permits 3 under the strike. The isolated pencilled 1 marks and archive 2 are independently clear.',
   '162-1/003: the cancelled ell/l-adique letter, ch/dh base and exponent, barred-L K formula, and final i/1 index do not establish a general notation habit; each remains locally doubtful.'
 ],
 'boxes':BOXES,
 'metadata':{
   'full_image_size':[1683,2150],
   'upper_half_size':[1683,1155],
   'lower_half_size':[1683,1155],
   'lower_half_original_y0':995,
   'line_count_basis':'41 numbered main handwritten entry lines/fragments, four printed letterhead lines, one Hartshorne–Goodman interlinear line, and two right-marginal text lines. Aligned borrower names and item text are counted together where they form one entry; the archive numeral is separate.',
   'crop_transforms':META,
   'whole_view_count':1,
   'half_view_counts':{'upper':1,'lower':1},
   'crop_display_complete':True,
   'blind_box_reading_scope':'Each reading gives the complete designated target element; neighboring intersecting fragments are covered by their own targets. s11 additionally gives the complete upper block for callout geometry.',
   'source_reading_status':'first-reader candidate, including scoped root crop-review feedback; not committed'
 }
}
OUT=WORK/f'{PAGE}_report.json'
OUT.write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n')
# Structural/documentary validation only; no TeX engine is invoked.
assert len({v['id'] for v in CHANGES})==len(CHANGES)
assert len({v['box'] for v in BOXES})==len(BOXES)
assert len({v['element'] for v in ITEMS})==len(ITEMS)
for v in CHANGES:
    assert Path(v['crop']).is_file()
    assert v['changed_C'] or v['changed_H']
for v in BOXES:
    assert 0<=v['x0']<v['x1']<=1683 and 0<=v['y0']<v['y1']<=2150
    assert v['reading']
stack=[]
for i,c in enumerate(DRAFT):
    if c not in '{}': continue
    j=i-1
    while j>=0 and DRAFT[j]=='\\': j-=1
    if (i-1-j)%2: continue
    if c=='{': stack.append(i)
    elif stack: stack.pop()
    else: raise ValueError(f'Unmatched closing brace at {i}')
assert not stack
assert DRAFT.count(r'\begin{tikzpicture}')==DRAFT.count(r'\end{tikzpicture}')
assert DRAFT.count(r'\begin{array}')==DRAFT.count(r'\end{array}')
assert json.loads(OUT.read_text())['page']==PAGE
print(json.dumps({'page':PAGE,'changes':len(CHANGES),'doubts':len(DOUBTS),'inventory':len(ITEMS),'boxes':len(BOXES),'evidence_crops':len(META),'structural_validation':'passed; no compilation'},ensure_ascii=False))
