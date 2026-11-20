import json
from datetime import datetime, timezone
from pathlib import Path

base = Path('/workspace/scratch/811dda00717a/work/readers/scan035/R3')
scanbase = '/workspace/scratch/811dda00717a/source/SP41_CW_81_scans/'
cropbase = str(base / 'crops') + '/'
F = []

def finding(place, c, h, reading, against_C, against_H, kind, confidence, evidence, bbox, crop=None, doubt_ids=(), status='none', marked_in_H=False, mathematical_note='', **extra):
    obj = {
        'id': f'scan035-R3-F{len(F)+1:02d}', 'place': place,
        'c': c, 'h': h, 'reading': reading,
        'against_C': against_C, 'against_H': against_H,
        'kind': kind, 'marked_in_H': marked_in_H,
        'confidence': confidence, 'evidence': evidence,
        'bbox': bbox, 'crop': cropbase + crop + '.png' if crop else None,
        'c_doubt_ids': list(doubt_ids), 'c_doubt_status': status,
        'mathematical_note': mathematical_note,
    }
    obj.update(extra)
    F.append(obj)

finding('First display: earlier horizontal after X',
    r'\deleted{\unsure{-}}', 'absent', r'\deleted{-}',
    True, True, 'omission', 'high',
    'Crop 01 separates a thin horizontal protruding to the left of the heavy descending strokes. The visible original is a horizontal minus. Its overwritten state is preserved. H gives only the final separator.',
    [758,149,802,184], '01_top_sign', ['C035-D001'], 'resolved',
    mathematical_note='The original horizontal was read from the surviving stroke, independently of the set-complement interpretation.')
finding('First display: live separator after X',
    r'\unsure{\setminus|-}', r'\smallsetminus', r'\unsure{\setminus|-}',
    False, False, 'other', 'medium',
    'Crop 01 shows a heavily retraced diagonal descending to the right over the horizontal. The dense overlap leaves some uncertainty about the final stroke sequence, so the setminus/minus alternatives remain. The first reading remains setminus.',
    [758,149,802,184], '01_top_sign', ['C035-D002'], 'retained',
    mathematical_note='The separate diagonal in the lower annotation is a local visual comparison. It does not decide the dense overwritten sign by mathematical expectation.')
finding('Line after the first display: first word',
    r'\unsure{donc}', 'donc', r'\unsure{donc}',
    False, False, 'other', 'low',
    'Crop 02 shows a closed low bowl, tall looped d stem, and a long nearly level continuation. The ending does not resolve into independently clear o/n/c bodies. The witness reading donc is retained with the original doubt.',
    [262,237,365,282], '02_donc', ['C035-D003'], 'retained',
    mathematical_note='The consequence introduced by the following formula does not supply the compressed letter endings.')
finding('Third display: first Pi glyph',
    r'\Pi_1', r'\Pi_{1}', r'\unsure{\Pi|\pi}_1',
    True, False, 'other', 'medium',
    'Crop 03 shows a long common cap over two descending legs, with a short return at the upper right. The glyph is Pi-shaped, but this page supplies no independently contrasting upper/lower-case pair. Case uncertainty is recorded at the first occurrence, and Pi is used subsequently.',
    [476,541,540,596], '03_pair_annotation',
    mathematical_note='The family role of the symbol does not settle its handwritten case.')
finding('Annotation beneath Sigma2+: overwritten lower index of Sigma-minus',
    r'\Sigma_{\unsure{1|2}}^-', r'\Sigma_{1}^{-}',
    r'\Sigma_{\unsure{\deleted{2|1}}\unsure{1|2}}^-',
    True, True, 'other', 'low',
    'Crop 03 shows a blackened near-vertical body, a small hooked shoulder to its left, and a leftward low foot. The live first reading remains 1 with 2 retained as an alternative. The surplus shoulder/foot are preserved as an uncertain overwritten earlier 2 or 1. H explicitly reports that this index is rewritten; its note does not identify the old numeral.',
    [649,635,681,673], '03_pair_annotation', ['C035-D004'], 'retained',
    mathematical_note='The following positive member has a clear index 1, but it is not used to repair the obscured negative-member index.',
    h_editorial_note='sous $\\Sigma_{2}^{+}$, l’indice de $\\Sigma^{-}$ est récrit ; on lit $\\Sigma_{1}^{-}$',
    state_uncertainty='The older numeral identity and part of its overwritten state remain open.')
finding('Same annotation: horizontal at the top of X',
    'X', 'X', r'\unsure{\deleted{{-}|\Sigma}}X',
    True, True, 'omission', 'low',
    'Crop 03 shows a broad horizontal extending beyond both upper X arms. The crossed live X is legible below it. The earlier horizontal is retained, with its identity as a simple bar or remnant of Sigma and its separate overwritten state both uncertain.',
    [678,615,732,663], '03_pair_annotation',
    mathematical_note='The visible X is kept. No earlier complete mathematical term is supplied from the surrounding equality.',
    state_uncertainty='A distinct older glyph versus a joined/reinforced upper stroke cannot be settled.')
finding('Conclusion line: cancelled Pi before the live equality',
    r'\deleted{\unsure{\Pi_2|\Pi_1}}', r'\struck{\ill{}}', r'\deleted{\unsure{\Pi_2|\Pi_1}}',
    False, True, r'readable ink left as \ill{}', 'medium',
    'Crop 04 separates the cap and left leg of Pi beneath cancellation strokes. The low right mass includes a short rightward foot, supporting the first reading 2, but its overlap with the cancellation leaves 1 possible. The glyph is partly readable and is not replaced by an illegibility marker.',
    [535,696,598,753], '04_cancelled_and_live_pi', ['C035-D005'], 'retained', marked_in_H=True,
    mathematical_note='The cancelled index is retained independently of the live equality that follows.')
finding('Conclusion line: opening connective',
    'alors', 'donc', 'alors',
    False, True, 'misread word', 'high',
    'Half a shows a low opening a, tall l, then the extended low ending of alors. This is settled from the half and was not cropped.',
    [260,697,375,747],
    mathematical_note='No change was made to make the conclusion more idiomatic.')
finding('Conclusion line: final live Pi index',
    r'\Pi_1=\Pi_{\unsure{3|2}}', r'\Pi_{1}=\Pi_{2}', r'\Pi_1=\Pi_3',
    True, True, 'misread symbol or index', 'high',
    'Crop 04 shows two successive rightward curves at the last lowered digit, ending in a descending leftward tail. The adjacent clear 2 in the preceding display has a low rightward foot. The live index here reads 3; the C doubt is resolved without changing its primary reading.',
    [802,695,878,771], '04_cancelled_and_live_pi', ['C035-D006'], 'resolved',
    mathematical_note='The earlier line names Pi1 and Pi2. That mathematical context was recognized but did not replace the written 3.')
finding('After contrairement: two small marks',
    r'\unsure{:|à}', 'à', ':',
    True, True, 'misread word', 'high',
    'Crop 05 shows two detached compact ink marks vertically aligned. Neither is a closed low a body. The source punctuation is transcribed as a colon.',
    [1354,698,1379,733], '05_colon_hypothese', ['C035-D007'], 'resolved',
    mathematical_note='The phrase’s expected preposition was not substituted for the two visible marks.')
finding('Conclusion line: hypothèse and its accent',
    r'\unsure{hypothèse}', 'hypothèse', r'\unsure{hypothèse|hypothese}',
    True, False, 'other', 'medium',
    'Crop 05 preserves the tall h, long y and p descenders, and the compressed terminal group. The primary word reading remains hypothèse. A separately identifiable grave accent is not secure in the terminal group, so the unaccented alternative is added rather than claiming resolution.',
    [1471,664,1667,793], '05_colon_hypothese', ['C035-D008'], 'retained',
    mathematical_note='The source’s appeal to the hypothesis is reported without verifying the preceding argument.')
finding('Replacement heading: underline belongs to the cancelled Corollaire',
    r'\deleted{\uline{Corollaire}} \inserted{Proposition}', r'\emph{Proposition}',
    r'\deleted{\uline{Corollaire}} \inserted{Proposition}',
    False, True, 'other', 'high',
    'Half a shows Proposition written above the crossed Corollaire. A separate straight underline lies below Corollaire; no independent underline runs beneath Proposition. H’s explicit note already identifies the replacement and is acknowledged. The finding concerns emphasis scope, not an additional insertion-state difference.',
    [257,879,505,994],
    mathematical_note='The author’s change of heading is retained as a documentary revision.',
    h_related=r'\marginal{\struck{Corollaire}}',
    h_editorial_note='« Proposition » est écrit au-dessus de « Corollaire », biffé ; l’énoncé est marqué d’un trait vertical dans la marge',
    bbox_components=[[260,879,505,935],[257,923,494,994]])
finding('Proposition opening: Soient/Soit',
    r'\unsure{Soient|Soit}', 'Soient', r'\unsure{Soient|Soit}',
    False, False, 'other', 'low',
    'Crop 06 shows S, a low rounded continuation, a detached dot, and the terminal crossed stroke. Between the dotted segment and the final upright the writing is flattened into a long run; e/n cannot be separated securely. The original two readings remain.',
    [562,905,674,975], '06_soient_separator', ['C035-D009'], 'retained',
    mathematical_note='The following two Pi terms do not establish a plural verb ending from the ink.')
finding('Proposition opening: separator between Pi1 and Pi2',
    r'\unsure{;|,}', ',', ';',
    True, True, 'misread symbol or index', 'high',
    'Crop 06 shows a short detached upper dash and a separate comma-like lower curved stroke. Both marks belong to the separator. The semicolon reading is resolved.',
    [785,929,818,974], '06_soient_separator', ['C035-D010'], 'resolved',
    mathematical_note='The separator is retained as written; no punctuation normalization is applied.')
finding('Proposition opening: surplus upright at the second Pi',
    r'\Pi_2', r'\Pi_{2}', r'\unsure{\deleted{\vert}}\Pi_2',
    True, True, 'other', 'low',
    'Crop 06 shows an additional thin upright above the left cap and a longer downstroke below the ordinary left leg, beside a dark reinforced turn. The live Pi2 is clear. The surplus upright is retained as an uncertain older vertical stroke; a separate cancellation versus reinforcement remains open.',
    [835,899,914,981], '06_soient_separator',
    mathematical_note='No earlier whole numeral or letter is supplied: the tentative original is represented only by its visible vertical stroke.',
    state_uncertainty='Older separate upright versus reinforced continuation of the live Pi.')
finding('Proposition: adjective after mutuellement non',
    r'\unsure{panachées}', 'parallèles', 'panachées',
    True, True, 'misread word', 'high',
    'Crop 07 shows the long p descender, low a/n/a runs, a low c leading into one tall h, then the accented ending ées. The detached accent rises rightward. This resolves the C primary reading panachées.',
    [1352,981,1660,1083], '07_panachees', ['C035-D011'], 'resolved',
    mathematical_note='The word was chosen from its letter sequence, without importing a definition of panachées from another page.')
finding('Ordered pair: first Sigma superscript',
    r'\Sigma_1^{\unsure{+|\top}}', r'\Sigma_{1}^{+}', r'\Sigma_1^{\unsure{\top|+}}',
    True, True, 'misread symbol or index', 'medium',
    'Crop 08 shows a long horizontal cap with a stem descending from its middle. No separately clear upward arm emerges above the cap. The first reading is therefore top-shaped; an asymmetrically written plus remains an alternative. The nearby second exponent has four visible arms.',
    [561,1208,660,1280], '08_ordered_pair', ['C035-D012'], 'retained',
    mathematical_note='The other plus-marked Sigma terms were used as visual comparators only; they do not justify supplying an upper arm here.')
finding('Intersection display: terminal point supplied by H',
    r'\Sigma_1^+\cap\Sigma_2^+=\varnothing', r'\Sigma_{1}^{+}\cap\Sigma_{2}^{+}=\emptyset .',
    r'\Sigma_1^+\cap\Sigma_2^+=\varnothing',
    False, True, 'text not on the page', 'high',
    'Half b shows the crossed oval and its full descending slash followed by clear blank space. No separate terminal point is visible. The point is present in H’s exact formula line; it is not transcribed.',
    [584,1424,1021,1528],
    mathematical_note='This finding concerns terminal punctuation only; the empty-set glyph is retained.')
finding('Display (17): first low double-bowl letter',
    r'\unsure{\omega_1|w_1}', r'\omega_{1}', r'\omega_1',
    True, False, 'other', 'high',
    'Crop 09 shows two rounded lower bowls with inward-curved open ends, followed by a separate lowered upright 1. The second occurrence has the same rounded form and lowered 2. The omega reading is resolved.',
    [982,1669,1058,1721], '09_omega', ['C035-D013'], 'resolved',
    mathematical_note='The repeated form was compared within this page only.')
finding('Display (18): target capital P form',
    r'\unsure{\mathfrak{P}|\mathcal{P}}', r'\mathfrak{P}', r'\unsure{\mathfrak{P}|\mathcal{P}}',
    False, False, 'other', 'medium',
    'Crop 11 shows a long descending upright, broad top stroke, angular right bowl, and a middle stroke curling back to the left. The precise Fraktur/calligraphic rendering remains uncertain; the first reading remains Fraktur P.',
    [857,1936,964,2047], '11_targetP', ['C035-D014'], 'retained',
    mathematical_note='The capital’s role as the mapping target does not decide a font family.')
finding('Display (18): target subscript',
    r'\unsure{\mathrm{finies}|\mathrm{ferm\acute{e}s}|\mathrm{foncier}}', r'\text{fermé}',
    r'\unsure{\text{finies}|\text{fermés}|\text{fermé}}',
    True, True, 'misread word', 'low',
    'Crop 11 shows a tall f, compressed low continuations, a single detached late dot-like mark, and a descending terminal curl. Finies remains the first reading; fermés and fermé remain alternatives. The medial letters and final number ending cannot be separated securely. The supplied C_context comparison with another scan was not used or inspected.',
    [945,1976,1088,2040], '11_targetP', ['C035-D015'], 'retained',
    mathematical_note='Neither a finite-subset meaning nor a closed-subset meaning was imposed on the unclear handwritten subscript.')
finding('Display label (18): original 7 beneath 8',
    r'\tag*{(1\deleted{\unsure{7}}8)}', r'\tag{18}', r'\tag*{(1\deleted{7}8)}',
    True, True, 'omission', 'high',
    'Crop 12 shows the earlier long top bar and descending stroke of 7, with the live 8’s two lobes added across it. The earlier numeral 7 is resolved. H’s note acknowledges rewritten numbering but does not supply this readable original digit.',
    [263,1971,378,2049], '12_label18', ['C035-D016'], 'resolved',
    mathematical_note='The earlier digit was read from the top bar and downstroke rather than inferred from a numbering sequence.',
    h_editorial_note='les numéros (17), (18), (19) sont récrits sur d’autres ; la phrase se poursuit à la page suivante')
finding('Display label (19): original 8 beneath 9',
    r'\tag*{(1\deleted{\unsure{8}}9)}', r'\tag{19}', r'\tag*{(1\deleted{8}9)}',
    True, True, 'omission', 'medium',
    'Crop 13 shows the live large upper bowl and long downstroke of 9, with two smaller old loop remnants against the lower part of that stroke. The old 8 is read from those loop remnants. H acknowledges rewriting in its note but leaves the old numeral untranscribed.',
    [274,2143,364,2205], '13_label19', ['C035-D017'], 'resolved',
    mathematical_note='No sequence-based reconstruction of the earlier label was used.',
    h_editorial_note='les numéros (17), (18), (19) sont récrits sur d’autres ; la phrase se poursuit à la page suivante')
finding('Final line: et before laquelle',
    r'\unsure{et|à}', 'et', 'et',
    True, False, 'other', 'high',
    'Half b shows a closed low e-like loop followed by a tall crossed t. The et reading is settled from the half; no additional crop was made.',
    [263,2219,324,2281],
    doubt_ids=['C035-D018'], status='resolved',
    mathematical_note='The written et is retained despite the grammatical cue toward à.')
finding('Final inline citation (18): earlier 7',
    r'(1\deleted{\unsure{7}}8)', '(18)', r'(1\deleted{7}8)',
    True, True, 'omission', 'medium',
    'Crop 14 shows a higher bent top stroke, a central descending stroke, and a rightward transverse bar under the live 8 loops. These surviving strokes support the earlier 7. The overwritten original is retained in the inline citation as well as in the display label.',
    [1138,2222,1212,2286], '14_inline18', ['C035-D019'], 'resolved',
    mathematical_note='The label reference did not supply the older numeral; the reading uses its surviving strokes.')
finding('Final line: injective',
    r'\unsure{injective}', 'injective', 'injective',
    True, False, 'other', 'medium',
    'Crop 15 separates the dotted opening i, low n run, long looped j, connected e/c group, crossed tall t, short following i stroke, and compressed terminal ve with its trailing curl. Injective is resolved; the adjacent abbreviation remains i.e.',
    [1340,2210,1568,2295], '15_injective', ['C035-D020'], 'resolved',
    mathematical_note='The application mentioned in the sentence supplied context but did not replace any written letter.')

I=[]
def inv(element, kind, position, first, hand='his hand', **extra):
    item={'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':hand,'transcribed':'yes'}
    item.update(extra)
    I.append(item)
inv('scan035-I01','text',[261,64,372,122],"d'où")
inv('scan035-I02','display',[510,124,1107,212],r'\Sigma_{12}=X…(\Sigma_1^+\cup\Sigma_2^+)')
inv('scan035-I03','deletion',[758,149,802,184],r'earlier horizontal minus at X')
inv('scan035-I04','text',[260,220,1155,345],r'donc \Sigma_{12}=\varnothing signifierait que')
inv('scan035-I05','display',[573,345,964,407],r'X=\Sigma_1^+\amalg\Sigma_2^+')
inv('scan035-I06','text',[264,454,644,527],'et par suite')
inv('scan035-I07','display',[474,512,1304,621],r'\Pi_1=\{\Sigma_1^+,\Sigma_2^+\},\quad\Pi_2=\{\Sigma_2^+,\Sigma_1^+\}')
inv('scan035-I08','insertion',[617,582,797,679],r'\Vert, then \Sigma^-_{…}=X\setminus\Sigma_1^+ beneath \Sigma_2^+')
inv('scan035-I09','deletion',[649,635,681,673],'uncertain older index 2 or 1 beneath the annotation index',state_uncertainty=True)
inv('scan035-I10','deletion',[678,615,732,663],'uncertain older bar/Sigma at annotation X',state_uncertainty=True)
inv('scan035-I11','text',[260,664,1670,794],r'alors … \Pi_1=\Pi_3 contrairement : l’hypothèse.')
inv('scan035-I12','deletion',[535,696,598,753],r'cancelled \Pi_2 or \Pi_1')
inv('scan035-I13','text',[264,805,751,864],'On trouve donc')
inv('scan035-I14','deletion',[257,923,494,994],'Corollaire, with its retained underline')
inv('scan035-I15','insertion',[260,879,505,935],'Proposition written above Corollaire')
inv('scan035-I16','text',[263,892,1665,1242],'Soient … deux décompositions binaires … Alors il existe un unique couple',bbox_components=[[560,892,1545,984],[263,982,1665,1085],[265,1109,1265,1242]],emphasis='unique underlined')
inv('scan035-I17','deletion',[835,899,866,981],'possible older upright at second Pi in proposition opening',state_uncertainty=True)
inv('scan035-I18','margin note',[241,992,274,1191],'long vertical emphasis stroke beside binaires and Alors',representation='standard LaTeX rule beside the corresponding two source lines')
inv('scan035-I19','display',[526,1203,1135,1303],r'(\Sigma_1^{\top|+},\Sigma_2^+)\in\Pi_1\times\Pi_2')
inv('scan035-I20','text',[265,1310,793,1435],"tel que l'on ait")
inv('scan035-I21','margin note',[239,1308,261,1385],'short vertical emphasis stroke beside tel',representation='standard LaTeX rule at tel')
inv('scan035-I22','display',[584,1424,943,1528],r'\Sigma_1^+\cap\Sigma_2^+=\varnothing')
inv('scan035-I23','text',[376,1609,616,1679],'Soit alors')
inv('scan035-I24','display',[263,1667,1216,1778],r'(17) C=\Pi_1\amalg\Pi_2=\omega_1\amalg\omega_2')
inv('scan035-I25','text',[263,1728,1593,1955],"l'ensemble somme, qui a quatre éléments. On a une application canonique",bbox_components=[[263,1728,1593,1846],[263,1852,1210,1955]])
inv('scan035-I26','display',[263,1936,1223,2053],r'(18), earlier 17: C\longrightarrow\mathfrak P_{finies|fermés|fermé}(X)')
inv('scan035-I27','deletion',[299,1973,345,2044],'earlier 7 in the display label 18')
inv('scan035-I28','text',[263,2051,899,2148],'qui a comme image')
inv('scan035-I29','display',[274,2126,1200,2208],r'(19), earlier 18: \{\Sigma_1^+,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-\},')
inv('scan035-I30','deletion',[309,2143,342,2205],'earlier 8 in the display label 19')
inv('scan035-I31','text',[263,2198,1648,2341],"et laquelle on l'identifie si (18) est injective, i.e.")
inv('scan035-I32','deletion',[1162,2222,1201,2286],'earlier 7 in the inline citation 18')
inv('scan035-I33','text',[17,2301,76,2349],'archive sheet number 34','another unnamed hand (pencil archive numbering)',representation='% archive sheet number: 34')

notes=[
    {'id':'scan035-note-01','text':"The opening writes the Sigma12 expression, followed by the source words ‘signifierait que’, a disjoint-sum display, and two displayed Pi decompositions. The following source conclusion reads Pi1=Pi3, followed by ‘contrairement : l’hypothèse’. The written final 3 and colon are preserved. The surrounding names Pi1 and Pi2 were recognized as a mathematical cue, not used to replace the final digit.",'source_findings':['scan035-R3-F08','scan035-R3-F09','scan035-R3-F10']},
    {'id':'scan035-note-02','text':"An annotation beneath the first displayed Sigma2+ uses two short vertical strokes as a vertical equality mark, then the negative-Sigma expression. Its lower index is heavily overwritten. The first reading of the live index remains 1, while the old index and long horizontal at X remain uncertain. The clear final positive-Sigma index 1 was checked visually but does not determine the obscured index.",'source_findings':['scan035-R3-F05','scan035-R3-F06']},
    {'id':'scan035-note-03','text':"The author replaces the underlined, cancelled heading ‘Corollaire’ with ‘Proposition’. The paragraph concerns two ‘décompositions binaires’ and uses the words ‘mutuellement non panachées’, then an underlined ‘unique’. Its ordered pair and the following empty-intersection display are transcribed. The first ordered-pair superscript has a horizontal cap and downward stem; the visibly fuller nearby plus is a comparator, not a reason to fill the missing upper arm.",'source_findings':['scan035-R3-F12','scan035-R3-F16','scan035-R3-F17']},
    {'id':'scan035-note-04','text':"Two separated vertical emphasis strokes occur in the left margin: a long one beside the binaires/Alors lines and a short one beside tel. Both are represented with LaTeX rules at those positions. C’s explicit comment already identifies both scopes, and H’s editorial note acknowledges marginal emphasis; no independent omission claim is made from their macro arrangements.",'source_positions':[[241,992,274,1191],[239,1308,261,1385]]},
    {'id':'scan035-note-05','text':"The lower block defines C by the displayed sum of the Pi and omega terms and calls it ‘l’ensemble somme, qui a quatre éléments’. The next display is an application with a script-P target. The target subscript remains finies/fermés/fermé-uncertain. The text then lists four Sigma terms as its image. No interpretation of the target subscript was imposed from the surrounding mathematics.",'source_findings':['scan035-R3-F19','scan035-R3-F20','scan035-R3-F21']},
    {'id':'scan035-note-06','text':"The page ends with ‘et laquelle on l’identifie si (18) est injective, i.e.’ The written et is retained. The last abbreviation is not expanded in the transcription. No following page was inspected and no continuation supplied.",'source_findings':['scan035-R3-F24','scan035-R3-F25','scan035-R3-F26']},
    {'id':'scan035-note-07','text':"The display labels 18 and 19 preserve earlier 7 and 8 respectively; the final inline 18 preserves an earlier 7. Each reading follows surviving numeral strokes. H’s explicit note recognizes rewritten display numbering, so the reported additional material is the old numeral itself, not an invented omission of revision state. Crop 10 was made for label 17 because H also describes it as rewritten; that crop did not yield a separately decipherable prior numeral, and (17) is retained without inventing one.",'source_findings':['scan035-R3-F22','scan035-R3-F23','scan035-R3-F25'],'label17_bbox':[263,1711,354,1774],'label17_crop':cropbase+'10_label17.png'},
    {'id':'scan035-note-08','text':"No source date or separate author page number is visible. The pencil 34 at the lower left is treated as archive sheet numbering and retained as a TeX comment. The page has handwritten prose and displays, the correction/addition layers inventoried above, and emphasis strokes; it contains no independent drawn figure or commutative diagram. No mathematical proof check or computation was performed."},
]

notation=[
    {'scan':35,'form':r'\Sigma,\Sigma_{12},\varnothing','evidence':'Both halves: angular Sigma with long cap and base; 12 on one low level; empty set a small oval crossed by a long rising slash.','reading':r'\Sigma,\Sigma_{12},\varnothing'},
    {'scan':35,'form':r'\deleted{-}\unsure{\setminus|-}','evidence':'Crop 01: thin horizontal protrudes left of a dense diagonal descending rightward.','reading':'Earlier horizontal resolved as minus; final separator remains setminus/minus-uncertain.'},
    {'scan':35,'form':r'\Pi|\pi','evidence':'Crop 03: long common cap and two descending legs; no separate contrasting case glyph on this page.','reading':r'\unsure{\Pi|\pi} at first occurrence; \Pi subsequently.'},
    {'scan':35,'form':'overwritten lower index in annotation','evidence':'Crop 03: black near-vertical with a hooked upper-left shoulder and low leftward foot.','reading':r'\unsure{\deleted{2|1}}\unsure{1|2}; identities and the old layer remain uncertain.'},
    {'scan':35,'form':'horizontal at annotation X','evidence':'Crop 03: long bar extends beyond both upper X arms.','reading':r'\unsure{\deleted{{-}|\Sigma}}X; separate older layer versus joined/reinforced stroke remains open.'},
    {'scan':35,'form':'final live Pi index in conclusion','evidence':'Crop 04: two rightward curves followed by a downward-left tail.','reading':r'\Pi_3'},
    {'scan':35,'form':'colon before l’hypothèse','evidence':'Crop 05: two vertically aligned detached small marks.','reading':':'},
    {'scan':35,'form':'separator in Pi1;Pi2','evidence':'Crop 06: independent upper dash and lower comma-like curved body.','reading':';'},
    {'scan':35,'form':'extra upright at proposition Pi2','evidence':'Crop 06: thin extension above cap and longer stroke below ordinary left leg.','reading':r'\unsure{\deleted{\vert}}\Pi_2; older stroke versus reinforcement remains uncertain.'},
    {'scan':35,'form':r'\top|+ in first ordered-pair exponent','evidence':'Crop 08: horizontal roof and descending stem, with no distinct upward arm.','reading':r'\unsure{\top|+}'},
    {'scan':35,'form':r'\omega_1,\omega_2','evidence':'Crop 09: two rounded low bowls with inward-curved ends, followed by separate lowered numerals.','reading':r'\omega_1,\omega_2'},
    {'scan':35,'form':r'\mathfrak P|\mathcal P','evidence':'Crop 11: long downstroke, broad cap, angular bowl and leftward middle curl.','reading':r'\unsure{\mathfrak P|\mathcal P}'},
    {'scan':35,'form':'target subscript','evidence':'Crop 11: tall f, low compressed runs, one late dot-like mark and curled terminal.','reading':'finies | fermés | fermé'},
    {'scan':35,'form':'rewritten display and inline labels','evidence':'Crops 12–14: older top bar/downstroke in each 18; small old loop remnants beneath live 9 in label19.','reading':r'(1\deleted{7}8), (1\deleted{8}9), (1\deleted{7}8)'},
    {'scan':35,'form':'et at start of final line','evidence':'Half b: low closed loop and tall crossed t.','reading':'et'},
]

U=[]
def unres(place, reading, alternatives, confidence, reason, refs=(), **extra):
    item={'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason,'finding_ids':list(refs)}
    item.update(extra)
    U.append(item)
unres('First display separator',r'\setminus',['-'],'medium','Heavy diagonal and earlier horizontal overlap; final stroke sequence remains dense.',['scan035-R3-F02'])
unres('Compressed connective after first display','donc',[],'low','Only the d and a nearly level ending are independently clear.',['scan035-R3-F03'])
unres('First Pi case',r'\Pi',[r'\pi'],'medium','Common cap/two-leg form without an independent case contrast.',['scan035-R3-F04'])
unres('Annotation: older index',r'\unsure{\deleted{2}}',['older 1','uncertain separate overwritten state'],'low','Hooked shoulder and foot survive within a blackened index.',['scan035-R3-F05'])
unres('Annotation: live index','1',['2'],'low','Dark near-vertical and lower mass do not fully separate the live numeral.',['scan035-R3-F05'])
unres('Annotation: older stroke at X',r'\deleted{-}',[r'\deleted{\Sigma}','joined or reinforced X stroke'],'low','A long upper horizontal survives; full old outline and its state are not independently separable.',['scan035-R3-F06'])
unres('Cancelled Pi index in conclusion',r'\Pi_2',[r'\Pi_1'],'medium','Cancellation covers the small right subscript.',['scan035-R3-F07'])
unres('hypothèse terminal accent','hypothèse',['hypothese'],'medium','The terminal group is compressed and the grave accent is not separately secure.',['scan035-R3-F11'])
unres('Proposition verb','Soient',['Soit'],'low','The post-i run is flattened into the terminal crossed stroke.',['scan035-R3-F13'])
unres('Surplus upright at proposition Pi2',r'\unsure{\deleted{\vert}}',['reinforced or extended live Pi stroke'],'low','Upper and lower extensions are visible, but a separate older character is not identifiable.',['scan035-R3-F15'])
unres('First ordered-pair exponent',r'\top',['+'],'medium','T-shaped written form has no distinct upper arm; a flattened plus remains possible.',['scan035-R3-F17'])
unres('Target P rendering',r'\mathfrak P',[r'\mathcal P'],'medium','Angular-bowled manuscript P does not uniquely determine the typographic rendering.',['scan035-R3-F20'])
unres('Target subscript','finies',['fermés','fermé'],'low','Compressed medial run and one late dot-like mark leave both letters and final ending open.',['scan035-R3-F21'])

coverage={}
for f in F:
    for d in f['c_doubt_ids']:
        coverage[d]={'finding_id':f['id'],'status':f['c_doubt_status']}
expected={f'C035-D{i:03d}' for i in range(1,21)}
assert set(coverage)==expected, (expected-set(coverage),set(coverage)-expected)
assert all(f['confidence'] in ['high','medium','low'] for f in F)
assert all(len(f['bbox'])==4 and 0<=f['bbox'][0]<f['bbox'][2]<=1693 and 0<=f['bbox'][1]<f['bbox'][3]<=2362 for f in F)
assert (base/'reading.tex').is_file()

manifest=[json.loads(line) for line in (base/'crops'/'crop_manifest.jsonl').read_text().splitlines()]
ret={
    'scan':35,'reader':'R3','model':'GPT-6 Astra Pro','effort':None,
    'effort_note':'Inherited effort; not exposed to this reader.',
    'start_utc':'2026-11-20T10:54:53Z',
    'start_utc_note':'First recorded UTC at the beginning of actual image viewing; brief/witness preparation immediately preceded it.',
    'end_utc':datetime.now(timezone.utc).isoformat(),
    'images_viewed':[
        {'path':scanbase+'J81-05_81_scan035.jpg','role':'whole','view_count':1,'actual_viewing':True,'purpose':'layout'},
        {'path':scanbase+'J81-05_81_scan035_a.jpg','role':'a','view_count':1,'actual_viewing':True,'purpose':'line-by-line reading'},
        {'path':scanbase+'J81-05_81_scan035_b.jpg','role':'b','view_count':1,'actual_viewing':True,'purpose':'line-by-line reading'},
    ],
    'actual_viewing_only':True,
    'crops_viewed':[{'path':x['target'],'bbox':x['bbox'],'view_count':1,'actual_viewing':True} for x in manifest],
    'transcription_file':str(base/'reading.tex'),
    'transcription_complete_utc':'2026-11-20T11:00:52Z',
    'complete_transcription_saved_before_return':True,
    'findings':F,'inventory':I,'notes':notes,'check_events':[],
    'notation':notation,
    'abbreviations':[{'scan':35,'form':'i.e.','expansion':'id est'}],
    'unresolved':U,'crop_count':len(manifest),
    'c_doubt_coverage':coverage,
    'counts':{
        'findings':len(F),'findings_against_C':sum(f['against_C'] for f in F),'findings_against_H':sum(f['against_H'] for f in F),
        'c_doubts_total':len(coverage),'c_doubts_resolved':sum(x['status']=='resolved' for x in coverage.values()),'c_doubts_retained':sum(x['status']=='retained' for x in coverage.values()),
        'inventory_elements':len(I),'unresolved':len(U),'crops':len(manifest),
    },
    'workflow_feedback':{
        'brief':'reader_brief_v07.md followed; current notation table and every page-specific packet text input were read.',
        'image_order':'Whole image once for layout, half a once, half b once, then each of 15 enlarged local crops once.',
        'crop_processing':'Single crop operation per open locus; original-coordinate boxes; width 3000 px; LANCZOS; autocontrast; UnsharpMask. No rotation was needed.',
        'target_clipping':'No target mark was clipped. Incidental neighboring strokes enter some crop boundaries; they were not re-cropped.',
        'coordinate_system':'All bbox values use the 1693 by 2362 original whole image. Half b begins at whole y=1101.',
        'closed_loci':'Clear half-settled differences, including alors, heading emphasis, absent formula point and final et, have exact whole-image bounds but were not cropped.',
        'wrapped_loci':'The stacked heading correction has component boxes. Wrapped inventory text blocks also include component boxes.',
        'label17':'A single crop was warranted by H’s explicit rewritten-number note. No separately decipherable older numeral was supplied for label17.',
        'independence':'Only assigned scan035, its supplied packet inputs, the reader brief and the allowed current notation table were inspected. Other page images, other readers and root decisions were not consulted.',
        'forbidden_processes':'No OCR, recognition, PDF text extraction, external research or LaTeX compilation was used.',
        'mathematics':'Mathematical context was a reading cue only. No theorem was proposed, no source mathematics was silently repaired, and no proof/computation check is claimed.',
        'count_interpretation':'Against-C counts include removal/change of doubt markup and are not an error count. H uncertainty-only comparisons with the same primary reading are false. Explicit confident H notes are not marked_in_H doubts.',
    }
}
(base/'return.json').write_text(json.dumps(ret,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(ret['counts']))
print('return.json written; complete reading.tex already existed')
