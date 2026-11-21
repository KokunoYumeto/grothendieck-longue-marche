from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan063'
boxes=json.loads((root/f'proposed/{page}_crop_boxes.json').read_text())
changes=[]
def change(place,c,h,final,diff_c,diff_h,kind,error_kind,evidence,crop,confidence='high',marked_in_h=False,consequential=False):
    changes.append(dict(id=f'{page}-{len(changes)+1:02d}',place=place,c=c,h=h,final=final,diff_c=diff_c,diff_h=diff_h,kind=kind,error_kind=error_kind,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence,marked_in_h=marked_in_h,consequential=consequential))
change('Opening sentence, after essentielle','est donc',r'\ill{} \ill{}','est donc',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The first short run has the joined e/s and raised terminal t; the next starts with a looped d and continues as the low o/n/c run. Both words are present.','opening_est_donc')
change('Cancelled sign after graphe',r'\deleted{$\unsure{\Gamma}$}',r'\struck{\ill{}}',r'\deleted{$\unsure{\Gamma}$}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','A short upright with a rightward upper arm survives the crossing; it permits Gamma, but the overworked junction does not settle the whole glyph. The source doubt is retained.','graph_old_colon','low',True)
change('Punctuation after pondéré','à',':',':',True,False,'misread symbol or index','Other','Two separated dark dots stand one above the other; there is no a bowl or accent.','graph_old_colon')
change('Raised replacement above à repères donné',r'\inserted{\unsure{repères|repéré}}',r'\add{repéré}',r'\inserted{\unsure{repères|repéré}}',False,True,'misread word','Words','The raised r/e/p opening and one central accent are visible. The low final run has a downward hook but does not securely separate final res from ré; repères remains the leading visual reading, with repéré retained.','repere_replacement','medium')
change('First word of cancelled des foncteurs des',r'\deleted{\unsure{des foncteurs des}}',r'\struck{\ill{} foncteurs des}',r'\deleted{\unsure{des foncteurs des}}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The first crossed group has a tall d-like start and a short terminal hook. The f descender and later t/eurs are partly visible, but the cancellation hides enough of the letters to retain the entire old phrase as doubtful.','foncteurs','low',True)
change('Scope of raised et l’explicitation',r'\inserted{et l\'explicitation}',r'\add{et} l\'explicitation',r'\inserted{et l\'explicitation}',False,True,'insertion or placement','Insertions put in the wrong place','All of et l’explicitation occupies the raised row above the old crossed phrase; l’explicitation is not on the old baseline.','foncteurs')
change('Left NB margin, article after tomber','le','les','le',False,True,'misread word','Words','The l loop joins a single low e exit; there is no separate final s before the opening quotation marks.','margin_nb')
change('Left NB margin, two quoted qualifiers',r'``$S$\'\' ou ``$D$\'\'',r'« D », « S »',r'``$S$\'\' ou ``$D$\'\'',False,True,'misread word','Words','The first quoted capital has the two opposing curves of S; the second has a straight stem and rounded bowl of D. Between them is the low joined o/u of ou. The marks are pairs of pen ticks, not guillemets.','margin_nb')
change('Left NB margin, after the quoted qualifiers','contenus déjà',r'\ill{}','contenus déjà',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The next margin row begins c/o/n, has a tall crossed t, and ends in the low enus run; déjà has the initial d loop, j descender and upper accent strokes. Main-body letters at the right are not additional margin words.','margin_nb',marked_in_h=True)
change('Left NB margin, final row',r'dans $\underline\Gamma$',r'dans \ill{} des $\underline{\Gamma}$',r'dans $\underline\Gamma$',False,True,'text not on the page','Text that is not on the page','The final row has dans followed directly by an underlined Gamma. No additional intervening word or des is visible.','margin_nb',marked_in_h=True)
change('Left NB margin, terminal punctuation',r'$\underline\Gamma$.',r'$\underline{\Gamma}$',r'$\underline\Gamma$',True,False,'text not on the page','Text that is not on the page','The underlined Gamma is followed by blank paper in the margin; no independent terminal point is present.','margin_nb')
change('After automatiquement','automatiquement,','automatiquement','automatiquement,',False,True,'omission','Omissions','A separate curved comma descends immediately after the terminal t and before par.','auto_comma')
change('Shorthand before temps',r'$=$ temps','même temps',r'$=$ temps',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','The source has two short, nearly parallel horizontal bars; it does not spell même.','same_temps')
change('Shorthand before façon',r'$=$ façon','même façon',r'$=$ façon',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','Two short parallel bars precede façon; no letters of même are written.','same_facon')
change('First of the paired indexed groupoids',r'$\unsure{S}\mathcal T_{g,\nu}^\pm$',r'$\mathcal{T}^{\pm}_{g,\nu}$ [small raised sign noted but not read]',r'${}^{\unsure{S}}\mathcal T_{g,\nu}^\pm$',True,True,'insertion or placement','Insertions put in the wrong place','The small looped sign stands distinctly above the lower T baseline at the upper left. Its faint upper part does not resolve S. The entire T, g-comma-nu index and two-bar plus/minus superscript were inspected together.','first_groupoid','low',True)
change('Word after the second paired groupoid',r'\unsure{ci-dessus|connus}','connus',r'\unsure{ci-dessus|connus}',False,True,'misread word','Words','The opening c and a low joined middle run are visible, followed by separated short strokes and a terminal s-like hook. The compressed middle does not securely decide ci-dessus versus connus; the C alternatives remain.','second_connus','low')
change('Hole-closing phrase','le bouchage des','les bouclages de','le bouchage des',False,True,'misread word','Words','The article has no separate s; bouchage has the rounded b, low ou, a looped h after c, and descending g, with no separate terminal s; the following des has a distinct final downward hook.','bouchage')
change('Alleged cancelled verb before pourrait','absent',r'\struck{s\'expliciteront}','absent',False,True,'text not on the page','Text that is not on the page','No second verb run is written. The curved stroke passes above the start of the one baseline s’expliciter and attaches the raised pourrait; it does not cross a separate s’expliciteront.','pourrait')
change('Insertion scope at pourrait s’expliciter',r'\inserted{pourrait} s\'expliciter',r'\add{pourrait s\'expliciter}',r'\inserted{pourrait} s\'expliciter',False,True,'insertion or placement','Insertions put in the wrong place','Only pourrait is on the raised row. The single s’expliciter belongs to the baseline after trous.','pourrait')
change('Old phrase before S T and T',r'\deleted{\unsure{analogues des|catégories, ou}}',r'\struck{catégories, ou}',r'\deleted{\unsure{analogues des|catégories, ou}}',False,True,'misread word','Words','The cancellation crosses the first word through most of its middle. A tall stroke, a closed oval with descender and a low terminal hook survive; the last short group looks o/u-like. Those traces do not make every letter of either proposed phrase plain, so the old phrase remains doubtful.','analogs_deleted','low')
change('State of des before the replaced old noun','des',r'\struck{des}','des',False,True,'deletion state (struck given live or live given struck)','Struck text','The des at the left is retraced but sits before the separate long cancellation, which starts to its right. There is no independent crossing through that first des.','structures_deleted','medium')
change('Cancelled noun replaced by structures',r'\deleted{\unsure{données}}',r'\struck{\ill{}}',r'\deleted{\unsure{données}}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The cancelled run has tall looped strokes and the low n/é/e/s-shaped ending compatible with données. The strike obscures its earlier letters and segmentation, so the tentative reading is not resolved.','structures_deleted','low',True)
change('After quoted élémentaires',r'\unsure{à déterminer|: diminution}',': diminution',': diminution',True,False,'misread word','Words','There is a two-dot colon after the closing quotation ticks. The next line begins with a tall looped d and dotted i, followed by the low minution run; no separate à or déterminer is written.','elementaires_diminution','medium')
change('Punctuation after diminution',r'\unsure{à déterminer|: diminution}.','diminution','diminution',True,False,'text not on the page','Text that is not on the page','The final low n ends in a hook; the paper after it is blank and has no separate terminal dot.','elementaires_diminution')
change('State of the double-star display label',r'\deleted{$(**)$}',r'$(**)$',r'$\unsure{(**)|\deleted{(**)}}$',True,False,'deletion state (struck given live or live given struck)','Struck text','Both parentheses are outside the horizontal stroke. The two asterisks are heavily retraced and have a continuous transverse line, but their own horizontal arms could account for part of it. Visible-label first and deleted-label alternative are retained.','lower_diagram','low',False)
change('Cancellation of both S prefixes in the lower arrow',r'\deleted{S}\mathcal T_{g,\nu,\nu\'}^\pm\longrightarrow\deleted{S}\mathcal T_{g,\nu\unsure{-|+}\nu\'}',r'S\mathcal{T}^{\pm}_{g,\nu,\nu\'}\longrightarrow S\mathcal{T}_{g,\nu\,?\,\nu\'} [vertical strokes described in a note]',r'\deleted{S}\mathcal T_{g,\nu,\nu\'}^\pm\longrightarrow\deleted{S}\mathcal T_{g,\nu\unsure{\pm|-|+}\nu\'}',False,True,'deletion state (struck given live or live given struck)','Struck text','Each S is traversed by long upright cancellation strokes. The adjacent calligraphic T letters and all their indices remain live. H describes the strokes but leaves the prefixes live in its mathematical rendering.','lower_diagram',marked_in_h=True,consequential=True)
change('Whole target subscript of the lower arrow',r'\mathcal T_{g,\nu\unsure{-|+}\nu\'}',r'\mathcal{T}_{g,\nu\,?\,\nu\'}',r'\mathcal T_{g,\nu\unsure{\pm|-|+}\nu\'}',True,True,'misread symbol or index','Symbols and indices','Between the two nu letters is a dark upright, a lower horizontal bar and a short upper cross/serif. This resembles the page’s I-shaped plus/minus superscripts, but the upper stroke is too thick to settle it. Both nu letters, the g-comma and final prime were read with the operator.','lower_diagram','medium',True,True)
change('Attachment bracket under the lower source','absent','brace under the source, described editorially','flat U-shaped bracket under the source, with the annotation below it',True,False,'drawing or diagram','Drawings and diagrams','Two short upward end strokes are joined by one nearly horizontal lower stroke beneath the calligraphic T and its indices. The annotation begins directly below that bracket. The TeX reproduces the flat bracket with a three-segment TikZ path.','lower_diagram',consequential=True)
change('Alleged repeated source formula before the footer annotation','absent',r'$\mathcal{T}^{\pm}_{g,\nu,\nu\'}$ :','absent',False,True,'text not on the page','Text that is not on the page','Below the bracket the source begins directly les X. There is no second written T with triple subscript and no introductory colon.','footer_annotation',consequential=True)
change('First word of the footer second line','la',r'\struck{\ill{}}',r'\unsure{la|\deleted{la}}',False,True,'deletion state (struck given live or live given struck)','Struck text','The l loop and following low a are readable. The lower connecting line is heavily retraced but does not clearly form an independent strike; live la is retained first, with cancellation state open.','footer_annotation','medium',True)
change('Footer article before sous ens.',"d'un","d'une","d'un",False,True,'misread word','Words','After d and the apostrophe are two low u/n arches ending in a downward flick. No further e loop follows.','footer_annotation')
change('Footer abbreviation','sous ens.','sous-ens.','sous ens.',False,True,'misread symbol or index','Symbols and indices','The two written word groups are separated by a blank and a short oblique finishing stroke of sous, not a distinct horizontal hyphen. A separate abbreviation point follows ens.','footer_annotation','medium')
change('Footer terminal punctuation',r'$\operatorname{card}I\'=\nu\'$' ,r'$\operatorname{card} I\' = \nu\'$.',r'$\operatorname{card}I\'=\nu\'$',False,True,'text not on the page','Text that is not on the page','The final nu has a separate raised prime; there is no independent dot after that prime.','footer_annotation')
change('Lower folio annotation',r'\mspage{62}','absent',r'\mspage{62}',False,True,'omission','Omissions','The pale lower-left numeral has a closed lower bowl on the first 6 and an arched second digit descending to a rightward foot, hence 62. Its writer is not positively identified.','lower_number')

def decision(i,which,reading,evidence,crop,confidence):
    return dict(id=i,decision=which,reading=reading,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence)
decisions=[
 decision('M0764','undecided',r'\unsure{repères|repéré}','The raised rep opening and a central accent are visible; the compressed ending does not settle res versus ré.','repere_replacement','medium'),
 decision('M0765','first','groupoïde','The final d has a closed lower loop and upright; its e finishes in one downward hook, with no further separable s.','groupoide','high'),
 decision('M0766','undecided',r'{}^{\unsure{S}}\mathcal T_{g,\nu}^\pm','The small upper-left curved sign is faint above its clear lower return. S is retained doubtfully and in its raised position; the whole formula has been checked.','first_groupoid','low'),
 decision('M0767','undecided',r'\unsure{ci-dessus|connus}','The joined middle letters and separated short strokes remain too compressed to select ci-dessus or connus securely.','second_connus','low'),
 decision('M0768','alternative',': diminution','The closing quotation ticks are followed by a colon; the next row has initial d, dotted i and the low minution ending.','elementaires_diminution','medium'),
 decision('M0769','undecided',r'\mathcal T_{g,\nu\unsure{\pm|-|+}\nu\'}','A lower bar, upright and short upper stroke support plus/minus as the leading reading; the overworked top prevents a conclusive distinction. The entire target formula was inspected.','lower_diagram','medium'),
]
implicit_decisions=[
 decision('I01','undecided',r'\deleted{$\unsure{\Gamma}$}','The old upright and upper right arm are crossed by heavy strokes; the Gamma reading remains tentative.','graph_old_colon','low'),
 decision('I02','undecided',r'\deleted{\unsure{des foncteurs des}}','The cancellation overlaps several middle letters and the first short word; not every letter is plain.','foncteurs','low'),
 decision('I03','undecided',r'\deleted{\unsure{analogues des|catégories, ou}}','The first word is crossed through its middle; the final short group is o/u-like but the whole old phrase is not securely recovered.','analogs_deleted','low'),
 decision('I04','undecided',r'\deleted{\unsure{données}}','The earlier part and segmentation of the cancelled run are obscured; données is retained as a tentative recovery.','structures_deleted','low'),
 decision('I05','undecided',r'\unsure{(**)|\deleted{(**)}}','The star arms and an apparent transverse cancellation overlap; the parentheses themselves remain unobstructed.','lower_diagram','low'),
 decision('I06','undecided',r'\unsure{la|\deleted{la}}','The letters la are readable, but the thick lower trace does not conclusively distinguish retracing from cancellation.','footer_annotation','medium'),
]
doubts=[
 dict(place='Cancelled sign after graphe',reading=r'\Gamma',alternatives='Unresolved crossed Gamma-shaped sign',confidence='low',reason='Heavy overwork hides the middle and lower junction.'),
 dict(place='Raised replacement of à repères donné',reading='repères',alternatives='repéré',confidence='medium',reason='The one central accent is clear; final letters are compressed.'),
 dict(place='Cancelled phrase below et l’explicitation',reading='des foncteurs des',alternatives='Unresolved letters within the same cancelled phrase',confidence='low',reason='The strike overlaps the first short group and middle letter bodies.'),
 dict(place='First paired groupoid, small raised left sign',reading=r'{}^{S}\mathcal T_{g,\nu}^\pm',alternatives='S remains unidentified with confidence; no alternative letter is supplied from mathematics',confidence='low',reason='Only the small sign’s lower curve is clear; its upper stroke is faint.'),
 dict(place='Word after the second paired groupoid',reading='ci-dessus',alternatives='connus',confidence='low',reason='Low compressed connections do not separate the middle letters securely.'),
 dict(place='Cancelled phrase before S T and T',reading='analogues des',alternatives='catégories, ou',confidence='low',reason='The first word is crossed; a final o/u-like run does not settle all earlier letters.'),
 dict(place='Cancelled run replaced by structures',reading='données',alternatives='Possible unresolved earlier word boundary within the same cancelled run',confidence='low',reason='More than one tall loop survives, and the crossing hides the intervening connections.'),
 dict(place='Double-star display label',reading='Visible (**) with uncertain deletion state',alternatives=r'\deleted{(**)}',confidence='low',reason='The apparent transverse strike overlaps the stars’ own arms; both parentheses are outside it.'),
 dict(place='Whole target of the lower arrow',reading=r'\deleted{S}\mathcal T_{g,\nu\pm\nu\'}',alternatives=r'\deleted{S}\mathcal T_{g,\nu-\nu\'} ; \deleted{S}\mathcal T_{g,\nu+\nu\'}',confidence='medium',reason='The upper stroke of the I-like operator is heavily inked, though its upright and lower bar are clear.'),
 dict(place='Footer word la',reading='la, live',alternatives=r'\deleted{la}',confidence='medium',reason='The lower trace could be retracing or a short cancellation; the live reading is retained first.'),
]
inv=[]
def inventory(kind,position,words,hand='his hand'):
    inv.append(dict(element=f'E{len(inv)+1:02d}',sheet_kind='text',hand=hand,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inventory('text','Top centre','19')
inventory('text','Opening main paragraph','La question essentielle est donc comment reconstituer')
inventory('deletion','After graphe','Crossed Gamma-like sign')
inventory('deletion','Third main row','à repères donné')
inventory('insertion','Above à repères donné','repères / repéré')
inventory('deletion','After first T-top groupoid','plus')
inventory('insertion','Above plus','avec')
inventory('deletion','After en underlined Gamma','des foncteurs des, doubtful')
inventory('insertion','Above preceding cancellation','et l’explicitation')
inventory('margin note','Oblique left margin','Underlined NB, on laisse ici tomber le S ou D')
inventory('text','Second main paragraph','Pour l’opération 4°), elle sera obtenue automatiquement')
inventory('insertion','Above s’expliciter','pourrait, with curved attachment stroke')
inventory('deletion','After à l’aide','des opérations')
inventory('insertion','Above des opérations','des cas')
inventory('deletion','Before the S T and T pair','analogues des / catégories, ou')
inventory('deletion','After live des in dans le sac des','données, with unresolved segmentation')
inventory('insertion','Above the cancelled noun','structures')
inventory('diagram','Lower display','Double-star label, source-to-target arrow, both S prefixes vertically crossed')
inventory('deletion','Lower display label','Possible cancellation of (**) retained as state doubt')
inventory('deletion','Lower display source and target','Both initial S prefixes')
inventory('drawing','Below lower display source','Flat U-shaped three-segment attachment bracket')
inventory('insertion','Four rows below source bracket','les X in Ob T, avec la donnée d’un sous ens. I-prime')
inventory('deletion','Second annotation row','Possible cancellation of la retained as state doubt')
inventory('margin note','Right of lower display, beside vertical divider','avec ou sans S?')
inventory('text','Pale lower left folio annotation','62','unnamed hand (folio annotation; attribution uncertain)')
notes=[
 dict(id=f'{page}-N01',text='The page states a reconstruction problem: recover the topological groupoid attached to a weighted graph with repères, together with its functorial dependence and the seven operations except 4° and 5°. It proposes obtaining operation 4° from an explicit description, and places hole-closing among elementary structures. This is the content of a mathematical programme, not a proof on this sheet.'),
 dict(id=f'{page}-N02',text='The lower arrow relates the groupoid with a triple index g, nu, nu-prime to a groupoid whose second index combines nu and nu-prime. Its bracketed annotation describes objects X together with a subset I-prime of I(X) of cardinality nu-prime. The middle target operator is visually I-shaped and retained with plus/minus first; the expected effect of filling holes has not been used to substitute a minus.'),
 dict(id=f'{page}-N03',text='The left NB explicitly drops S or D because these are already contained in the underlined Gamma. The later question “avec ou sans S?” is retained beside the lower arrow, and both displayed initial S letters remain visibly cancelled. These source revisions are recorded without forcing a consistent final convention.'),
 dict(id=f'{page}-N04',text='The curved line by pourrait connects the raised insertion to the baseline; it does not provide evidence for H’s additional cancelled s’expliciteront. The lower bracket is flat, with short upward ends, and is reproduced by a TikZ path. H’s repeated T-with-triple-index and introductory colon below it are editorial expansions, not new ink.'),
 dict(id=f'{page}-N05',text='The two page numerals are 19 at the head and a pale 62 at the foot. The lower folio annotation is assigned to an unnamed hand with attribution uncertain; its appearance alone does not establish a different writer.'),
 dict(id=f'{page}-N06',text='Several old readings remain unresolved because the cancellation obscures letters. In the run replaced by structures, the word segmentation is also uncertain. The metadata keeps that limitation explicit rather than treating the clear replacement as proof of the abandoned wording.'),
]
check_events=[
 dict(statement_id=f'{page}-N01',type='carried as background without fault found',outcome='The reconstruction request and proposed operations were transcribed and interpreted as a programme. No mathematical proof, independent re-proof, or theorem verification was performed.'),
 dict(statement_id=f'{page}-N02',type='carried as background without fault found',outcome='The subset/cardinality annotation was read together with the complete displayed source and target. This was a transcription consistency reading only; no formal certificate or proof of the displayed operation is claimed.'),
]
notation=[
 dict(sign=r'\pm',meaning_or_form='Two short horizontal bars with an upright joining them can look like capital I; the target-index occurrence has a particularly short upper stroke.',places='Plus/minus superscripts throughout the page; lower arrow target index',universality='The clear superscripts share this form. The target-index glyph remains explicitly uncertain and is not normalized from the mathematical expectation.',witness_errors='C restricts the target operator to minus/plus; H leaves an unread I-like sign. Plus/minus is retained as the leading new alternative.'),
 dict(sign='=',meaning_or_form='Two horizontal strokes used as the written shorthand for même.',places='en = temps; de la = façon',universality='Both occurrences on this page were separately checked.',witness_errors='H expands both signs to même.'),
 dict(sign='Small raised S-like prefix',meaning_or_form='A small curved sign above the baseline at the upper left of calligraphic T; the letter remains uncertain.',places='First of the paired T-g-nu groupoids',universality='One faint occurrence only; the later full-size S letters are not retroactively used to identify it.',witness_errors='C places its unsure S on the baseline; H notes a raised unread sign and omits it from the formula.'),
 dict(sign='un',meaning_or_form='Two low joined arches with a downward final flick and no separate e.',places='Footer d’un sous ens.',universality='One disputed occurrence; checked directly against the page.',witness_errors='H reads d’une.'),
 dict(sign='Vertical cancellation and bracket strokes',meaning_or_form='Both lower S prefixes are cut by upright strokes; the flat U below the source is an attachment bracket, not part of a subscript.',places='Lower diagram and its object annotation',universality='All these lower diagram strokes were inspected together.',witness_errors='C omits the actual bracket. H records both the cancellations and brace in prose, but its source/target formula leaves the S letters live.'),
]
abbreviations=[dict(form='=',expansion='même'),dict(form='NB',expansion='nota bene'),dict(form='sous ens.',expansion='sous-ensemble'),dict(form='Ob',expansion='objets'),dict(form='card',expansion='cardinal')]
second=[]
def audit(kind,box,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
audit('handwritten number',[0,0,1684,125],r'\mspage{19}')
audit('different words',[255,125,1680,235],'La question essentielle est donc comment')
audit('struck passage',[255,240,1615,355],r'reconstituer, pour un graphe \deleted{$\unsure{\Gamma}$} pondéré :')
audit('insertion',boxes['repere_replacement'],r'\deleted{à repères donné} \inserted{\unsure{repères|repéré}}')
audit('different words',boxes['groupoide'],'groupoïde')
audit('insertion',boxes['plus_avec'],r'\deleted{plus} \inserted{avec}')
audit('insertion',boxes['foncteurs'],r'\deleted{\unsure{des foncteurs des}} \inserted{et l\'explicitation}')
audit('handwritten number',[255,750,1660,990],r'des sept opérations, à l\'exception de $4^\circ)$ et $5^\circ)$.')
audit('margin note',boxes['margin_nb'],r'\margin{\uline{NB} on laisse ici tomber le ``$S$\'\' ou ``$D$\'\', contenus déjà dans $\underline\Gamma$}')
audit('handwritten number',[255,965,1660,1070],r'Pour l\'opération $4^\circ)$, elle sera obtenue')
audit('different words',boxes['auto_comma'],'automatiquement, par')
audit('different words',boxes['same_temps'],r'en $=$ temps')
audit('different words',boxes['same_facon'],r'et de la $=$ façon que')
audit('doubtful formula',boxes['first_groupoid'],r'${}^{\unsure{S}}\mathcal T_{g,\nu}^\pm$')
audit('different words',boxes['second_connus'],r'$S\mathcal T_{g,\nu}^\pm$ \unsure{ci-dessus|connus}),')
audit('different words',boxes['bouchage'],'et le bouchage des')
audit('insertion',boxes['pourrait'],r'trous \inserted{pourrait} s\'expliciter')
audit('insertion',boxes['cas_operations'],r'\deleted{des opérations} \inserted{des cas}')
audit('struck passage',boxes['analogs_deleted'],r'\deleted{\unsure{analogues des|catégories, ou}}')
audit('insertion',boxes['structures_deleted'],r'des \deleted{\unsure{données}} \inserted{structures}')
audit('different words',[1220,1690,1643,1815],r'``élémentaires\'\' :')
tex=(root/f'proposed/{page}.tex').read_text()
diag=tex[tex.index('\\diagram{'):tex.index('\\margin{\\begin{tabular}')]
audit('doubtful formula',[267,1832,1375,2318],'diminution\n'+diag.strip())
audit('margin note',boxes['right_note'],r'\margin{\begin{tabular}{@{}|l@{}}avec ou\\sans $S$?\end{tabular}}')
audit('handwritten number',boxes['lower_number'],r'\mspage{62}')
obj=dict(page=page,reader='reader_c',lines_read=35,line_count_note='Count includes main text/formula rows, separate interlinear and margin rows, the four annotation rows, and both numeral-only rows; line divisions in the sloping text are approximate.',changes=changes,decisions=decisions,implicit_decisions=implicit_decisions,doubts=doubts,inventory=inv,notes=notes,check_events=check_events,notation=notation,abbreviations=abbreviations,second_boxes=second)

# Main-reader review refinements; keep the generator and evidence unchanged.
old_phrase=r"\deleted{\unsure{analogues|catégories}\unsure{,} ou}"
old_noun=r"\deleted{\unsure{\illegible{1} données|données}}"
for row in changes:
    if row['place']=='Old phrase before S T and T':
        row.update(final=old_phrase,diff_c=True,evidence='The final group has a distinct closed o and joined low u, both readable outside the most obscured middle. The first crossed word can be analogues or catégories; a short hook near its end may be punctuation but is not secure. The former alternative des is not retained as a separate word.')
    if row['place']=='Cancelled noun replaced by structures':
        row.update(final=old_noun,diff_c=True,kind='omission',error_kind='Omissions',evidence='After the live des, a separate tall cancelled run is followed by another tall/looped run and a low ending compatible with données. The earlier run cannot be read through the overstroke. A leading unreadable unit is preserved, with the one-word segmentation retained as an explicit lower-confidence alternative; neither segmentation nor the later word is claimed settled.')
    if row['place']=='Attachment bracket under the lower source':
        row.update(consequential=False,h=r'\note{écrit sous une accolade qui porte sur la source de (**)}',final=diag.strip())
    if row['place']=='Alleged repeated source formula before the footer annotation':
        row['consequential']=False
for row in implicit_decisions:
    if row['id']=='I03':
        row.update(reading=old_phrase,evidence='The final o is closed and joins a low u, so ou is recovered outside the word doubt. The crossed middle of the earlier word and a possible terminal comma remain open.')
    if row['id']=='I04':
        row.update(reading=old_noun,evidence='Two separated tall/looped runs are visible under the long cancellation. The earlier unit is physically obscured; the later run tentatively supports données. The leading two-unit segmentation and a single-word alternative are both retained.')
implicit_decisions.append(decision('I07','undecided',r'\unsure{,}','A short hooked trace after the first cancelled word may be a comma or part of its ending/cancellation; no punctuation is resolved from it.','analogs_deleted','low'))
for row in doubts:
    if row['place']=='Cancelled phrase before S T and T':
        row.update(reading='analogues',alternatives='catégories',reason='The first word is crossed through its middle. The following ou is clear and has been removed from this letter-reading doubt.')
    if row['place']=='Cancelled run replaced by structures':
        row.update(reading=r'\illegible{1} données',alternatives='données (single-word segmentation)',reason='An initial tall cancelled run is visibly separated from a later looped run; the strike obscures the first unit and prevents a secure word count or certain reading of données.')
doubts.append(dict(place='Possible punctuation before the cancelled ou',reading='comma, doubtful',alternatives='The hook may belong to the word ending or cancellation',confidence='low',reason='No fully separate comma is clear beneath the strike.'))
for row in inv:
    if row['position']=='Before the S T and T pair':
        row['first_words_or_objects']='analogues / catégories, possible comma, followed by clear cancelled ou'
    if row['position']=='After live des in dans le sac des':
        row['first_words_or_objects']='An unreadable cancelled unit followed by doubtful données; single-word segmentation remains possible'
for row in second:
    if row['reading']==r'\deleted{\unsure{analogues des|catégories, ou}}':
        row['reading']=old_phrase
    if row['reading']==r'des \deleted{\unsure{données}} \inserted{structures}':
        row['reading']='des '+old_noun+r' \inserted{structures}'
for row in notes:
    if row['id']==f'{page}-N02':
        row['text']='The lower arrow relates the groupoid with a triple index g, nu, nu-prime to a groupoid whose second index combines nu and nu-prime. Its bracketed annotation describes X with a subset I-prime of I(X) of cardinality nu-prime. The main reader’s targeted local check is that capping nu-prime distinct selected boundary components of a compact surface with nu boundary components removes exactly those nu-prime components and leaves the genus unchanged, giving target count nu minus nu-prime. This check flags the doubtful written operator but is not an emendation: the I-shaped ink remains plus/minus first, with minus and plus alternatives. It does not prove the reconstruction programme or functorial claims.'
    if row['id']==f'{page}-N06':
        row['text']='Several old readings remain unresolved because cancellation obscures letters. The final ou before the S T/T pair is clear and stands outside the first-word doubt; a possible comma remains uncertain. The run replaced by structures has two separated tall/looped groups: an unreadable initial unit plus doubtful données is the leading segmentation, with the single-word reading explicitly retained as an alternative. No old word is supplied from the clear replacement.'
for row in check_events:
    if row['statement_id']==f'{page}-N02':
        row.update(type='targeted proof check',performed_by='main reader (root)',outcome='Local boundary-count check only: capping nu-prime distinct members of the nu boundary components removes exactly that selected subset and leaves genus unchanged, hence nu minus nu-prime. This does not resolve the ink or establish the general operation; no emendation or full proof is claimed.')

def clean_apostrophes(value):
    if isinstance(value,str):
        return value.replace("\\'", "'")
    if isinstance(value,list):
        return [clean_apostrophes(x) for x in value]
    if isinstance(value,dict):
        return {k:clean_apostrophes(v) for k,v in value.items()}
    return value
obj=clean_apostrophes(obj)

(root/f'proposed/{page}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(f'{len(changes)} material rows; {len(decisions)} supplied decisions; {len(implicit_decisions)} implicit decisions; {len(doubts)} doubts; {len(inv)} inventory elements; {len(second)} audit units.')
