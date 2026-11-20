from pathlib import Path
import json, datetime, re, csv
root=Path('/workspace/scratch/811dda00717a/work/readers/scan035/R2')
base='/workspace/scratch/811dda00717a'
whole=base+'/source/SP41_CW_81_scans/J81-05_81_scan035.jpg'
a=base+'/source/SP41_CW_81_scans/J81-05_81_scan035_a.jpg'
b=base+'/source/SP41_CW_81_scans/J81-05_81_scan035_b.jpg'
findings=[]
def F(place,c,h,reading,against_C,against_H,kind,confidence,evidence,bbox,crop=None,doubts=(),status='none',note='',marked=False,**extra):
    entry={'id':f'scan035-R2-F{len(findings)+1:03d}','place':place,'c':c,'h':h,'reading':reading,'against_C':against_C,'against_H':against_H,'kind':kind,'marked_in_H':marked,'confidence':confidence,'evidence':evidence,'bbox':bbox,'crop':str(root/(crop+'.png')) if crop else None,'c_doubt_ids':list(doubts),'c_doubt_status':status,'mathematical_note':note}
    entry.update(extra)
    findings.append(entry)
F('First display, overwritten horizontal immediately after X',r'\deleted{\unsure{-}}',r'X\smallsetminus(\Sigma_{1}^{+}\cup\Sigma_{2}^{+})',r'\deleted{-}',True,True,'omission','high','Crop 01: a thin nearly horizontal stroke projects left from beneath the dense descending diagonal. Its surviving horizontal extent supports the older minus; the live descending stroke crosses it.',[757,151,805,187],'01_after_X',['C035-D001'],'resolved','The surrounding complement expression prompted attention to the separator; the old horizontal is retained from the visible ink.')
F('First display, live separator after X',r'\unsure{\setminus|-}',r'\smallsetminus',r'\setminus',True,False,'misread symbol or index','high','Crop 01: the dominant reinforced mark descends from upper left to lower right, crossing the earlier horizontal. The descending direction is visible independently of the expression.',[757,151,805,187],'01_after_X',['C035-D002'],'resolved','The descending separator in the under-pair annotation supplied a same-page comparison, without replacing the observed upper mark.')
F('Prose before the inline equality Sigma_12 = empty set',r'\unsure{donc}','donc',r'\unsure{donc}',False,False,'other','medium','Crop 02: the initial loop and tall ascender read d, followed by a long low continuous run. The interior o/n/c divisions remain compressed; the complete word is retained as doubtful.',[262,237,364,283],'02_donc',['C035-D003'],'retained','The following consequence wording supports attention to donc but does not resolve the compressed letters.')
F('First Pi in the pair display; recurring letter case',r'\Pi_1',r'\Pi_{1}',r'\unsure{\Pi|\pi}_1',True,False,'other','medium','Crop 03: a common long cap has two descending legs. This page supplies no separately contrasting lower-case form. The first reading is capital Pi, used without repeated uncertainty on later occurrences.',[477,542,535,596],'03_pair_annotation',note='The pair labels are read from their strokes. This is an added case uncertainty only, with the same first reading as H.')
F('Added annotation below Sigma_2^+, revised subscript on the negative Sigma',r'\Sigma_{\unsure{1|2}}^-',r'\Sigma_{1}^{-}; \note{sous $\Sigma_{2}^{+}$, l\'indice de $\Sigma^{-}$ est récrit ; on lit $\Sigma_{1}^{-}$}',r'\Sigma_{\unsure{\deleted{2|1}}1}^-',True,False,'deletion state (struck given live or live given struck)','medium','Crop 03: the dominant subscript has an upright, a hooked upper shoulder, and a low leftward foot, read as the live 1. Dark surplus at the shoulder and right side leaves an earlier 2/1 and its exact overwritten extent unresolved. H explicitly acknowledges rewriting and agrees on the live 1; no H primary-text change is counted here.',[651,639,681,669],'03_pair_annotation',['C035-D004'],'retained','The later positive Sigma has a plainly written 1. It was used as a local comparison, while the crowded older layer remains represented.')
F('Added annotation, horizontal remnant across the upper arms of X','X','X',r'\unsure{\deleted{{-}|\Sigma}}X',True,True,'omission','medium','Crop 03: a long independent-looking horizontal extends across and beyond the upper X arms. Only that horizontal of an earlier layer is separable; the identity minus/Sigma and overwritten state remain uncertain.',[679,616,734,662],'03_pair_annotation',note='The live X is preserved. No complete older letter is supplied with certainty.')
F('Added annotation, low horizontal adjoining the descending separator after X',r'X\setminus\Sigma_1^+',r'X\smallsetminus\Sigma_{1}^{+}',r'X\unsure{\deleted{-}}\setminus\Sigma_1^+',True,True,'omission','medium','Crop 03: a thin low horizontal continues to the right of the short dark descending separator toward the middle stroke of the following Sigma. Its identity as an older minus and its overwritten state remain uncertain, and that uncertainty is explicit.',[709,627,757,655],'03_pair_annotation',note='The upper formula has a separately visible overwritten horizontal. That prompted inspection here; the less isolated lower horizontal is kept doubtful.')
F('Word introducing the cancelled Pi and live equality','alors','donc','alors',False,True,'misread word','high','Half a: an initial low a, a tall l, and the following low linked run are legible at the beginning of this line.',[260,701,372,746],note='Read directly from half a; no additional crop was made at this settled locus.')
F('Cancelled Pi immediately before the live Pi equality',r'\deleted{\unsure{\Pi_2|\Pi_1}}',r'\struck{\ill{}}',r'\deleted{\unsure{\Pi_2|\Pi_1}}',False,True,r'readable ink left as \ill{}','medium','Crop 04: the cap and two legs of Pi survive the cancellation. A low rightward hooked remnant favours subscript 2; cancellation passes through the numeral and leaves 1 open as an alternative.',[536,697,596,752],'04_cancelled_live_Pi',['C035-D005'],'retained','The cancelled item is retained independently of the succeeding equality.',True)
F('Second live Pi in the equality after alors',r'\Pi_{\unsure{3|2}}',r'\Pi_{2}',r'\Pi_3',True,True,'misread symbol or index','high','Crop 04: the subscript has an upper curved shoulder, a second rightward turn, and a lower descending-left finish. Those two turns give the written 3.',[806,699,878,764],'04_cancelled_live_Pi',['C035-D006'],'resolved','The preceding display names Pi_1 and Pi_2. That tension triggered inspection; the visible live 3 is retained.')
F('Mark after contrairement',r'\unsure{:|à}','à',':',True,True,'misread symbol or index','high','Half a: two small separated marks stand one above the other. I did not identify a connected letter body at this locus.',[1355,697,1376,734],doubts=['C035-D007'],status='resolved',note='The usual phrase would encourage à; the transcription follows the two visible marks.')
F('Final word of the alors line',r'\unsure{hypothèse}','hypothèse',r'\unsure{hypothese|hypothèse}',True,True,'other','medium','Crop 05: h, the long y and p descenders, the following small o, and the tall joined middle strokes are visible. The final run is narrow, and a separate grave accent above the relevant e cannot be isolated. The unaccented written reading is first, with hypothèse retained as an alternative.',[1476,667,1668,793],'05_hypothese',['C035-D008'],'retained','The full word is retained rather than omitted; its accent remains unresolved.')
F('Revised heading, underline and emphasis scope',r'\deleted{\uline{Corollaire}} \inserted{Proposition}',r'\marginal{\struck{Corollaire}}; \emph{Proposition}; \note{« Proposition » est écrit au-dessus de « Corollaire », biffé ; l\'énoncé est marqué d\'un trait vertical dans la marge}',r'\deleted{\uline{Corollaire}} \inserted{Proposition}',False,True,'other','high','Half a: the horizontal underline lies beneath the cancelled Corollaire. Proposition is above it, with no separate underline attached to the replacement word. H already records the replacement and its position; the finding concerns the emphasis scope.',[259,881,506,994],note='The heading is a source revision, with the common source order retained in the transcription.')
F('Word after the revised heading',r'\unsure{Soient|Soit}','Soient',r'\unsure{Soit|Soient}',True,True,'misread word','medium','Crop 06: S, the low following letters, and the i dot are visible; the final material is a long low run crossed by a descending terminal stroke. Separate e and n strokes cannot be established. Soit is the first ink reading; Soient remains open.',[561,909,674,972],'06_heading_terms',['C035-D009'],'retained','Plural grammatical expectation is recorded as a cue only and does not supply the missing letter divisions.')
F('Separator between Pi_1 and Pi_2 in the proposition',r'\unsure{;|,}',',',';',True,True,'misread symbol or index','high','Crop 06: a short upper horizontal mark is separated from the lower hooked comma-like stroke. Both components are present.',[786,934,812,970],'06_heading_terms',['C035-D010'],'resolved')
F('Proposition Pi_2, protruding vertical remnant on the first leg',r'\Pi_2',r'\Pi_{2}',r'\unsure{\deleted{\vert}}\Pi_2',True,True,'omission','medium','Crop 06: a thinner vertical protrudes above the Pi cap and continues beside the heavily reinforced first leg; a short left protrusion remains midway. Only the vertical remnant is rendered, with identity and overwritten state uncertain. No complete earlier letter is asserted.',[838,901,915,980],'06_heading_terms',note='This preserves the visible extra stroke separately from the live Pi_2.')
F('Last word in mutuellement non ...',r'\unsure{panachées}','parallèles','panachées',True,True,'misread word','high','Crop 07: a p descender is followed by the low broken runs, then a tall h-like ascender, the accented ending, and terminal s. The accent is a separate rising stroke.',[1359,985,1656,1078],'07_panachees',['C035-D011'],'resolved','The word is read from the letter sequence; no replacement based on a mathematical classification is made.')
F('First exponent in the ordered pair',r'\unsure{+|\top}',r'+',r'\unsure{\top|+}',True,True,'misread symbol or index','medium','Crop 08: the first exponent has a long horizontal cap and a downward stem, with no independently separated upper arm. The neighbouring second exponent has a visible upper arm. The T-shaped reading is first; a flattened plus remains open.',[622,1217,655,1246],'08_pair_first_exponent',['C035-D012'],'retained','The neighbouring plus and the following intersection formula prompted comparison. Their mathematical role does not replace the observed first sign.')
F('Punctuation after the intersection display','absent',r'\emptyset .','absent',False,True,'text not on the page','high','Half b: the empty-set slash and oval are complete, followed by blank space. No terminal point is visible in that display.',[876,1428,1028,1524],note='The point in H is explicit in its supplied formula; this is a checked punctuation difference.')
F('First low letter in the right side of (17)',r'\unsure{\omega_1|w_1}',r'\omega_{1}',r'\omega_1',True,False,'misread symbol or index','high','Crop 09: the letter consists of two low rounded bowls with curled outer ends; its lowered 1 is distinct. The second corresponding letter has the same rounded form.',[983,1673,1057,1719],'09_omega',['C035-D013'],'resolved')
F('Label (17), state described in H editorial note',r'\tag*{(17)}',r'\tag{17}; \note{les numéros (17), (18), (19) sont récrits sur d\'autres ; la phrase se poursuit à la page suivante}',r'\tag*{(17)}',False,True,'other','medium','Crop 10: the readable strokes form 1 and a crossed 7, with the outer parentheses. I did not identify a separate underlying digit at this label. The transcription therefore gives the visible (17) without an older numeral. H\'s general rewriting note is recorded rather than converted into an unseen old glyph.',[264,1710,352,1774],'10_tag17',note='The succeeding tags have visible overpainting; that contrast prompted inspection of this tag, not an inferred numbering history.')
F('Target capital in (18)',r'\unsure{\mathfrak{P}|\mathcal{P}}',r'\mathfrak{P}',r'\unsure{\mathfrak{P}|\mathcal{P}}',False,False,'other','medium','Crop 11: the capital has a long descending stem, an angular wide upper bowl, and a leftward lower curl. Its precise typographic rendering remains open between the stated P forms; the first reading agrees with H.',[858,1940,961,2044],'11_target_subscript',['C035-D014'],'retained','The set-valued target is a cue to the letter P, not a resolution of its manuscript style.')
F('Target subscript in (18)',r'\unsure{\mathrm{finies}|\mathrm{ferm\acute{e}s}|\mathrm{foncier}}',r'\text{fermé}',r'\unsure{\mathrm{finies}|\mathrm{ferm\acute{e}s}|\mathrm{foncier}}',False,True,'misread word','low','Crop 11: the f and its descender/cross stroke are clear; the compressed centre forms several low turns. A small detached late mark is dot-like, followed by a final low run and downturned ending. Finies remains first, but the interior letter divisions do not settle all alternatives.',[952,1980,1089,2035],'11_target_subscript',['C035-D015'],'retained','Only scan035 was read. The C context mention of another page was not followed. No codomain interpretation is used to select fermés or finies.')
F('Label (18), earlier last digit',r'\tag*{(1\deleted{\unsure{7}}8)}',r'\tag{18}; \note{les numéros (17), (18), (19) sont récrits sur d\'autres ; la phrase se poursuit à la page suivante}',r'\tag*{(1\deleted{7}8)}',True,True,'omission','high','Crop 12: a long upper cap and descending right stroke of the old 7 survive behind the live two-loop 8. H acknowledges rewriting, but the readable earlier digit is not transcribed.',[266,1974,373,2049],'12_tag18',['C035-D016'],'resolved')
F('Label (19), earlier last digit',r'\tag*{(1\deleted{\unsure{8}}9)}',r'\tag{19}; \note{les numéros (17), (18), (19) sont récrits sur d\'autres ; la phrase se poursuit à la page suivante}',r'\tag*{(1\deleted{8}9)}',True,True,'omission','high','Crop 13: a smaller lower loop remains to the left of the long live 9 descender, below the shared upper loop. It supports the overwritten 8. H acknowledges rewriting without transcribing that earlier numeral.',[273,2147,362,2207],'13_tag19',['C035-D017'],'resolved')
F('Initial word of the last line',r'\unsure{et|à}','et','et',True,False,'misread word','high','Half b: a low open loop leads into a rising stem with a separate crossing stroke, read as et. This was settled from the half and was not separately cropped.',[266,2225,322,2278],doubts=['C035-D018'],status='resolved',note='The following laquelle can encourage à syntactically; the visible loop-plus-crossed-stem sequence is retained.')
F('Inline citation (18) in the last line, earlier last digit',r'(1\deleted{\unsure{7}}8)','(18)',r'(1\deleted{\unsure{7}}8)',False,True,'omission','medium','Crop 14: the live 8 has two dark loops. A separate high curved cap and a short rightward crossbar remain among the older strokes. The earlier 7 is plausible from these remains but cannot be fully separated, so its uncertainty is retained.',[1141,2230,1212,2282],'14_inline18',['C035-D019'],'retained','The other rewritten (18) supplied a comparison, without resolving the more crowded inline older digit.')
F('Last-line adjective after est',r'\unsure{injective}','injective','injective',True,False,'misread word','medium','Crop 15: the initial dotted i, low n run, long j loop, e/c sequence, tall crossed t, and compact final ive run support injective. The following comma and i.e. are retained.',[1345,2213,1561,2300],'15_injective',['C035-D020'],'resolved','The preceding application wording was used as a cue for inspection; the descending j and the ending were checked in the crop.')

inventory=[]
def I(element,kind,position,first,hand='his hand',**extra):
    item={'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':hand,'transcribed':'yes'}
    item.update(extra)
    inventory.append(item)
I('Opening continuation','text',[266,70,366,121],"d'où")
I('First display','display',[509,123,1104,209],r'\Sigma_{12}=X\deleted{-}\setminus(\Sigma_1^+\cup\Sigma_2^+)')
I('Overwritten minus in first display','deletion',[757,151,805,187],r'\deleted{-}')
I('Consequence prose','text',[262,220,1149,342],r'\unsure{donc} $\Sigma_{12}=\varnothing$ signifierait que')
I('Coproduct display','display',[572,349,960,408],r'X=\Sigma_1^+\amalg\Sigma_2^+')
I('Transition to two pairs','text',[262,459,635,528],'et par suite')
I('Two-pair display','display',[477,514,1308,619],r'\Pi_1=\{\Sigma_1^+,\Sigma_2^+\},\quad\Pi_2=\{\Sigma_2^+,\Sigma_1^+\}')
I('Interlinear equivalence annotation under Sigma_2^+','insertion',[625,588,788,671],r'\Vert;\ \Sigma_1^-=X\setminus\Sigma_1^+',attachment='Directly beneath the second member of the first pair, attached by two short vertical parallel strokes.')
I('Possible older subscript in that annotation','deletion',[651,639,681,669],r'\unsure{\deleted{2|1}} before live 1')
I('Uncertain earlier horizontal at annotation X','deletion',[679,616,734,662],r'\unsure{\deleted{{-}|\Sigma}} before live X')
I('Uncertain older horizontal beside annotation separator','deletion',[709,627,757,655],r'\unsure{\deleted{-}} before \setminus')
I('Line giving live Pi equality','text',[260,667,1668,793],r'alors ... \Pi_1=\Pi_3 contrairement : l\'hypothese.')
I('Cancelled Pi starter on that line','deletion',[536,697,596,752],r'\deleted{\unsure{\Pi_2|\Pi_1}}')
I('Transition to proposition','text',[265,802,756,864],'On trouve donc')
I('Cancelled underlined heading','deletion',[258,922,492,994],r'\deleted{\uline{Corollaire}}')
I('Replacement heading above it','insertion',[263,881,506,941],'Proposition',attachment='Written above the cancelled heading; represented at its replacement point.')
I('Proposition prose','text',[264,906,1659,1242],r'\unsure{Soit|Soient} \Pi_1;\Pi_2 deux décompositions / binaires de X, mutuellement non panachées. / Alors il existe un unique couple',bbox_parts=[[561,906,1552,980],[264,985,1659,1084],[268,1107,1271,1242]])
I('Uncertain earlier vertical at proposition Pi_2','deletion',[838,901,915,980],r'\unsure{\deleted{\vert}}')
I('Underlined word in proposition','text',[817,1117,1041,1242],r'\uline{unique}')
I('Long vertical emphasis stroke','margin note',[243,989,269,1188],'One vertical pen stroke beside binaires and Alors',representation='Rule beside the corresponding two prose lines.')
I('Ordered-pair display','display',[531,1204,1135,1301],r'(\Sigma_1^{\unsure{\top|+}},\Sigma_2^+)\in\Pi_1\times\Pi_2')
I('Prose introducing intersection','text',[269,1312,791,1440],"tel que l'on ait")
I('Short vertical emphasis stroke','margin note',[244,1311,258,1380],'Separate vertical pen stroke beside tel',representation='A second independent short rule.')
I('Intersection display','display',[584,1428,942,1524],r'\Sigma_1^+\cap\Sigma_2^+=\varnothing')
I('Transition to new set C','text',[379,1614,608,1675],'Soit alors')
I('Labelled set C display','display',[264,1668,1211,1774],r'(17)\quad C=\Pi_1\amalg\Pi_2=\omega_1\amalg\omega_2',bbox_parts=[[264,1710,352,1774],[557,1668,1211,1733]])
I('Explanation of C and canonical application','text',[267,1732,1585,1964],"l'ensemble somme, qui a quatre éléments. On a une application canonique",bbox_parts=[[267,1732,1585,1847],[269,1845,1219,1964]])
I('Canonical-application display','display',[266,1940,1217,2049],r'(1\deleted{7}8)\quad C\longrightarrow\mathfrak P_{\unsure{finies|fermés|foncier}}(X)',bbox_parts=[[266,1974,373,2049],[614,1940,1217,2044]])
I('Earlier 7 in displayed label (18)','deletion',[301,1974,344,2049],r'\deleted{7}')
I('Prose introducing image','text',[270,2055,889,2140],'qui a comme image')
I('Image-of-application display','display',[273,2125,1199,2207],r'(1\deleted{8}9)\quad\{\Sigma_1^+,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-\},',bbox_parts=[[273,2147,362,2207],[610,2125,1199,2207]])
I('Earlier 8 in displayed label (19)','deletion',[311,2147,337,2207],r'\deleted{8}')
I('Closing line','text',[266,2205,1650,2334],r'et laquelle on l\'identifie si (1\deleted{\unsure{7}}8) est injective, i.e.')
I('Uncertain earlier 7 in inline (18)','deletion',[1161,2230,1200,2282],r'\deleted{\unsure{7}}')
I('Archive pencil sheet number','text',[23,2306,71,2346],'34','another unnamed hand (pencil archive numbering)',representation='% archive sheet number: 34')

notes=[
 {'id':'scan035-note-01','text':'The sheet opens with the continuation “d\'où”. No separate author title, author page number, date, or explicit author question is visible. The pencil 34 at lower left is retained as an archive-sheet comment.'},
 {'id':'scan035-note-02','text':'The opening block contains the written complement expression for Sigma_12, then the wording “signifierait que”, a coproduct display for X, and two displayed pair definitions. These surrounding expressions prompted inspection of the separators and the negative-member subscript, but all visible older strokes and the remaining uncertainty are retained.'},
 {'id':'scan035-note-03','text':'The annotation below the second member of Pi_1 carries two short vertical parallel marks and the written negative-member identity. Its live subscript reads 1. The older subscript, top horizontal at X, and low horizontal beside the separator remain uncertain. H\'s explicit note about rewriting of the subscript was considered.'},
 {'id':'scan035-note-04','text':'The live equality after the cancelled Pi reads Pi_1 = Pi_3. The preceding displayed pair labels Pi_1 and Pi_2 supplied a mathematical cue to inspect the last numeral, while the crop supports the written 3. The connective is “alors”, and the mark after “contrairement” consists of two separated points.'},
 {'id':'scan035-note-05','text':'The underlined cancelled heading Corollaire has Proposition written above it. The proposition text contains the uncertain Soit/Soient ending, a semicolon, “mutuellement non panachées”, an underlined “unique”, and two separate vertical emphasis strokes. The first ordered-pair exponent is T-shaped; comparison with the neighbouring plus leaves the flattened-plus alternative open.'},
 {'id':'scan035-note-06','text':'The lower block writes C = Pi_1 amalg Pi_2 = omega_1 amalg omega_2 and describes four elements. It then gives a canonical application and its four displayed Sigma values. The target P style and its subscript remain uncertain from scan035 alone; the C context reference to another page was not followed.'},
 {'id':'scan035-note-07','text':'The displayed labels (18) and (19) retain readable older last digits 7 and 8. The inline (18) retains a doubtful older 7. At (17) I could read 1 and a crossed 7 but could not identify a separate earlier numeral; no numbering history is supplied beyond the ink.'},
 {'id':'scan035-note-08','text':'The final line visibly begins “et laquelle” and ends “injective, i.e.”. The syntactic cue toward à was considered without changing the observed et. No following page was read, and the continuation was not supplied.'},
 {'id':'scan035-note-09','text':'No proof check, independent re-proof, computation, or formal certificate was performed. Mathematical context was used only to choose loci for close visual inspection and to report tensions between the written symbols and nearby labels.'}
]
notation=[
 {'scan':35,'form':r'\Pi|\pi','evidence':'Crop 03 and both halves: a common cap with two downward legs; no contrasting case form established on this page.','reading':r'\unsure{\Pi|\pi} at the first occurrence; \Pi afterwards'},
 {'scan':35,'form':r'\deleted{-}\setminus','evidence':'Crop 01: a thin horizontal remains under the reinforced descending diagonal.','reading':r'\deleted{-}\setminus'},
 {'scan':35,'form':r'\Sigma_{\unsure{\deleted{2|1}}1}^-','evidence':'Crop 03: dominant upright 1 with crowded older shoulder and base.','reading':'Live 1; older identity/state unresolved.'},
 {'scan':35,'form':r'\unsure{\deleted{{-}|\Sigma}}X','evidence':'Crop 03: surplus horizontal across both upper X arms.','reading':'Represent horizontal remnant with uncertain older identity and state.'},
 {'scan':35,'form':r'X\unsure{\deleted{-}}\setminus','evidence':'Crop 03: low thin horizontal adjoins short descending separator and following Sigma.','reading':'Uncertain older minus and overwritten state.'},
 {'scan':35,'form':r'\Pi_3','evidence':'Crop 04: two rightward turns and descending-left terminal in the live subscript.','reading':r'\Pi_3'},
 {'scan':35,'form':':','evidence':'Half a: two separated vertically arranged points after contrairement.','reading':':'},
 {'scan':35,'form':';','evidence':'Crop 06: short upper mark above a lower hooked comma stroke.','reading':';'},
 {'scan':35,'form':r'\unsure{\deleted{\vert}}\Pi_2','evidence':'Crop 06: thin vertical protrudes above and beside reinforced Pi first leg.','reading':'Only the visible older vertical remnant is represented; its state remains uncertain.'},
 {'scan':35,'form':r'\unsure{\top|+}','evidence':'Crop 08: horizontal cap and downward stem; no separated upper arm.','reading':r'\top first, + retained as alternative'},
 {'scan':35,'form':r'\omega_1,\omega_2','evidence':'Crop 09: two rounded low bowls with curled outer ends.','reading':r'\omega_1,\omega_2'},
 {'scan':35,'form':r'\mathfrak P|\mathcal P','evidence':'Crop 11: long descender, angular wide bowl, lower-left curl.','reading':'Precise typographic style remains unresolved.'},
 {'scan':35,'form':'finies|fermés|foncier','evidence':'Crop 11: f, compressed low turns, one late detached dot-like mark, and downturned terminal.','reading':'finies first; alternatives retained.'},
 {'scan':35,'form':'(18), (19), inline (18)','evidence':'Crops 12–14: top cap of earlier 7 in first displayed label, lower loop of earlier 8 in second, crowded cap and crossbar in inline citation.','reading':r'(1\deleted{7}8), (1\deleted{8}9), (1\deleted{\unsure{7}}8)'}
]
unresolved=[
 {'place':'Before Sigma_12 = empty set','reading':'donc','alternatives':[],'confidence':'medium','reason':'Only d and a compressed low run can be separated; no complete alternative is established.','finding_id':'scan035-R2-F003'},
 {'place':'First Pi in pair display','reading':r'\Pi','alternatives':[r'\pi'],'confidence':'medium','reason':'Common cap and two legs with no independent case contrast on this page.','finding_id':'scan035-R2-F004'},
 {'place':'Older subscript under Sigma_2^+ annotation','reading':r'\unsure{\deleted{2|1}}1','alternatives':['earlier 1','older layer extent unresolved'],'confidence':'medium','reason':'Live upright 1 readable; dense shoulder/base do not isolate the older form.','finding_id':'scan035-R2-F005'},
 {'place':'Top horizontal at annotation X','reading':r'\unsure{\deleted{{-}|\Sigma}}X','alternatives':[r'\Sigma as older identity','earlier-layer state unresolved'],'confidence':'medium','reason':'Only an extra horizontal survives independently.','finding_id':'scan035-R2-F006'},
 {'place':'Horizontal next to annotation separator','reading':r'\unsure{\deleted{-}}','alternatives':['horizontal attached to neighbouring written strokes'],'confidence':'medium','reason':'The horizontal is visible; its earlier-minus identity and state are inseparable from the adjoining marks.','finding_id':'scan035-R2-F007'},
 {'place':'Cancelled Pi before live equality','reading':r'\Pi_2','alternatives':[r'\Pi_1'],'confidence':'medium','reason':'Pi cap and legs survive; cancellation masks the numeral.','finding_id':'scan035-R2-F009'},
 {'place':'Word at end of alors line','reading':'hypothese','alternatives':['hypothèse'],'confidence':'medium','reason':'No independent grave accent can be isolated from the narrow later strokes.','finding_id':'scan035-R2-F012'},
 {'place':'Word after Proposition','reading':'Soit','alternatives':['Soient'],'confidence':'medium','reason':'The terminal low run does not separate e/n from the final crossed stroke.','finding_id':'scan035-R2-F014'},
 {'place':'Proposition Pi_2 first leg','reading':r'\unsure{\deleted{\vert}}\Pi_2','alternatives':['reinforcement of live first leg'],'confidence':'medium','reason':'The extra high vertical is clear, but older identity/state cannot be fully isolated.','finding_id':'scan035-R2-F016'},
 {'place':'First ordered-pair exponent','reading':r'\top','alternatives':['+'],'confidence':'medium','reason':'Horizontal cap and downward stem are visible; a flattened plus remains open.','finding_id':'scan035-R2-F018'},
 {'place':'Target capital in (18)','reading':r'\mathfrak P','alternatives':[r'\mathcal P'],'confidence':'medium','reason':'Manuscript angular-bowled P admits the two typographic renderings.','finding_id':'scan035-R2-F022'},
 {'place':'Target subscript in (18)','reading':'finies','alternatives':['fermés','foncier'],'confidence':'low','reason':'Interior low letter divisions remain compressed despite enlargement.','finding_id':'scan035-R2-F023'},
 {'place':'Older last digit in final inline (18)','reading':'7','alternatives':[],'confidence':'medium','reason':'High cap and crossbar survive, but the older digit does not separate completely from the live 8.','finding_id':'scan035-R2-F027'}
]
manifest=json.loads((root/'crop_manifest.json').read_text())
source_doubts=list(csv.DictReader(Path(base+'/runtime_inputs/scan035/C_doubt_index.tsv').open(),delimiter='\t'))
covered={d for finding in findings for d in finding['c_doubt_ids']}
expected={row['source_doubt_id'] for row in source_doubts}
assert covered==expected, (expected-covered,covered-expected)
assert all(f['confidence'] in ('high','medium','low') for f in findings)
assert all(len(f['bbox'])==4 and f['bbox'][0]<f['bbox'][2] and f['bbox'][1]<f['bbox'][3] for f in findings)
assert all(0<=f['bbox'][0]<1693 and 0<=f['bbox'][2]<=1693 and 0<=f['bbox'][1]<2362 and 0<=f['bbox'][3]<=2362 for f in findings)
for finding in findings:
    if finding['crop']:
        assert Path(finding['crop']).exists()
for u in unresolved:
    assert u['finding_id'] in {f['id'] for f in findings}
reading=(root/'reading.tex').read_text()
assert reading.startswith('\\scanpage{35}')
result={
 'scan':35,'reader':'R2','model':'GPT-6 Astra Pro','effort':'inherited; not exposed',
 'start_utc':'2026-11-20T10:54:48Z','end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'start_time_note':'First recorded UTC timestamp in this independent reading session.',
 'images_viewed':[{'path':whole,'role':'whole','view_count':1,'purpose':'layout only','actual_viewing':True},{'path':a,'role':'a','view_count':1,'purpose':'line-by-line ink reading beside C and H','actual_viewing':True},{'path':b,'role':'b','view_count':1,'purpose':'line-by-line ink reading beside C and H','actual_viewing':True}],
 'actual_viewing_only':True,
 'whole_image_size':[1693,2362],
 'half_offsets':{'a':[0,0],'b':[0,1101]},
 'crops_viewed':[{'path':m['target'],'bbox':m['bbox'],'view_count':1,'actual_viewing':True} for m in manifest],
 'transcription_file':str(root/'reading.tex'),
 'complete_text_saved_before_detailed_return':True,
 'findings':findings,'inventory':inventory,'notes':notes,'check_events':[],
 'notation':notation,'abbreviations':[{'scan':35,'form':'i.e.','expansion':'id est'}],
 'unresolved':unresolved,'crop_count':len(manifest),
 'counts':{'findings':len(findings),'against_C':sum(f['against_C'] for f in findings),'against_H':sum(f['against_H'] for f in findings),'C_doubt_ids_covered':len(covered),'C_doubts_resolved':sum(len(f['c_doubt_ids']) for f in findings if f['c_doubt_status']=='resolved'),'C_doubts_retained':sum(len(f['c_doubt_ids']) for f in findings if f['c_doubt_status']=='retained'),'unresolved':len(unresolved),'inventory_elements':len(inventory),'drawings':0,'diagrams':0,'margin_emphasis_strokes':2},
 'workflow_feedback':[
  'Read reader_brief_v07, notation_before_scan035, packet.json, C, H, C_context, C_doubt_index, supplied C preamble, and H style instructions before the image sequence.',
  'Viewed the whole image once for layout, then half a once and half b once line by line; no whole or half was re-enlarged or reopened.',
  'Listed genuinely unresolved loci, made one crop for each coherent passage, and viewed each of the 15 crops once. No repeat crop was made.',
  'Crops were made from the whole original with LANCZOS at 3000 pixels width, autocontrast, and UnsharpMask. No rotation was needed. No target clipping was observed; irrelevant adjacent-line strokes can reach a context-crop edge.',
  'The complete reading.tex was saved immediately after image reading finished, and its availability was reported before this detailed JSON was composed.',
  'All 20 supplied C doubt IDs have retained or resolved findings. Clear differences settled from halves also have original-image bounds. No finding phrase wraps to the opposite page edge; component boxes are supplied in the inventory for the long wrapped text blocks and separated display labels.',
  'No OCR, recognition, PDF text extraction, external research, compilation, other-page inspection, other-reader inspection, or root-decision inspection was performed.',
  'No proof-check event is claimed. Uncertainty-only comparisons with unchanged H primary text have against_H=false; H editorial notes were read for revision state and emphasis.',
  'The two vertical margin marks are source emphasis strokes represented as rules. No separate drawing or diagram occurs on this page.'
 ]
}
# Keep primary witness quotations exact; store editorial notes separately.
htext=Path(base+'/runtime_inputs/scan035/H.tex').read_text()
ctext=Path(base+'/source/SP41_CW_81_witnesses/codex/J81-05/pages/J81-05_81_scan035.tex').read_text()
def exact_notes(text):
    ans=[]
    start=0
    while True:
        pos=text.find('\\note{',start)
        if pos<0: break
        depth=1
        end=pos+6
        while depth:
            if text[end]=='{': depth+=1
            elif text[end]=='}': depth-=1
            end+=1
        ans.append(text[pos:end])
        start=end
    return ans
hn=exact_notes(htext)
byid={f['id']:f for f in findings}
byid['scan035-R2-F005']['h']=r'\Sigma_{1}^{-}'
byid['scan035-R2-F005']['h_editorial_note']=hn[0]
byid['scan035-R2-F007']['h']='X\\smallsetminus\n  \\Sigma_{1}^{+}'
byid['scan035-R2-F013']['h']='\\marginal{\\struck{Corollaire}}\n\n\\emph{Proposition}'
byid['scan035-R2-F013']['h_editorial_note']=hn[1]
for fid,tag in [('scan035-R2-F021','17'),('scan035-R2-F024','18'),('scan035-R2-F025','19')]:
    byid[fid]['h']='\\tag{'+tag+'}'
    byid[fid]['h_editorial_note']=hn[2]
for finding in findings:
    assert finding['c']=='absent' or finding['c'] in ctext, ('C exact quotation',finding['id'],finding['c'])
    assert finding['h']=='absent' or finding['h'] in htext, ('H exact quotation',finding['id'],finding['h'])
(root/'return.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['counts'],ensure_ascii=False))
print(str(root/'return.json'))
