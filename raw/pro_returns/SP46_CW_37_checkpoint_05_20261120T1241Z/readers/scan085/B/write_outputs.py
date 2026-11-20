from pathlib import Path
import json

root=Path('/workspace/scratch/006c0e32b2af')
out=root/'out/readers/scan085/B'
packet=root/'packets/scan085'
source=root/'source/SP46_CW_37_scans/B37-04_37_scan085.jpg'

marginal=r'''\begingroup
\reversemarginpar
\margin{\figure{\handwritten{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\draw[line width=0.5pt]
 (0,6.80) .. controls (0.50,7.00) and (1.15,7.25) .. (1.62,7.15)
 .. controls (2.05,7.06) and (2.23,6.60) .. (2.13,6.12)
 .. controls (2.05,5.10) and (1.77,4.02) .. (1.46,2.77)
 .. controls (1.32,2.40) and (1.37,2.15) .. (1.69,2.10)
 .. controls (2.02,2.02) and (2.30,2.36) .. (2.55,2.18);
\draw[line width=0.5pt] (3.34,0.15) .. controls (3.64,0.28) and (3.91,0.22) .. (4.10,0.16);
\end{tikzpicture}%
}}}}
\endgroup'''

cancelled=r'''\figure{%
\begin{tikzpicture}[x=0.105mm,y=-0.105mm]
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\ttfamily\small] at (13,41)
 {\deleted{2.4. Fonctions constructibles}\deleted{\mbox{............................}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\ttfamily\small] at (13,94)
 {\deleted{2.5.}};
% The deletion macros record state; this path records the observed freehand course.
\handwritten{\draw[line width=0.45pt]
 (49,10) -- (23,81)
 .. controls (31,70) and (56,27) .. (65,17)
 .. controls (60,40) and (38,78) .. (33,87)
 .. controls (43,86) and (72,47) .. (81,37)
 .. controls (74,52) and (63,73) .. (64,80)
 .. controls (71,82) and (93,53) .. (103,42)
 .. controls (100,53) and (81,69) .. (90,71)
 .. controls (102,69) and (124,43) .. (137,25)
 .. controls (135,43) and (119,61) .. (128,64)
 .. controls (141,67) and (164,42) .. (180,28)
 .. controls (176,40) and (162,56) .. (166,60)
 .. controls (175,68) and (209,42) .. (227,31)
 .. controls (224,46) and (224,58) .. (239,56)
 .. controls (269,53) and (308,32) .. (333,25)
 .. controls (357,17) and (387,2) .. (405,13)
 .. controls (414,22) and (420,32) .. (436,30)
 .. controls (460,23) and (497,9) .. (516,16)
 .. controls (535,20) and (542,33) .. (555,33)
 .. controls (601,34) and (652,35) .. (703,34)
 .. controls (758,31) and (808,36) .. (862,33)
 .. controls (906,36) and (951,31) .. (1001,33)
 .. controls (1046,34) and (1093,33) .. (1165,32);}
\end{tikzpicture}%
}'''

reading=(packet/'C.tex').read_text()
reading=reading.replace(r'\mspage{538}',r'\mspage{- 538 -}')
oldcancel=r'''\margin{\handwritten{?}}
\noindent\qquad \deleted{2.4. Fonctions constructibles}\deleted{\mbox{............................}}

\noindent\qquad \deleted{2.5.}'''
assert oldcancel in reading
reading=reading.replace(oldcancel,marginal+'\n'+cancelled)
oldword=r'réci\deleted{\unsure{r}}p\deleted{p}roques'
newword=r'réci\deleted{\unsure{r}}p\deleted{p}roque\unsure{s|\deleted{s}s}'
assert oldword in reading
reading=reading.replace(oldword,newword)
(out/'reading.tex').write_text(reading)
manifest=json.loads((out/'crop_manifest.json').read_text())

D=[]
def decision(id,place,c_reading,reading,diff_c,c_doubt,unresolved,alternatives,confidence,kind,scan_shows,bbox,crop=''):
 D.append(dict(id=id,place=place,c_reading=c_reading,h_reading=None,reading=reading,diff_c=diff_c,diff_h=False,c_doubt=c_doubt,unresolved=unresolved,alternatives=alternatives,confidence=confidence,kind=kind,scan_shows=scan_shows,crop=str(out/crop) if crop else '',bbox=bbox))

decision('B085-01','Top-centre pagination',r'\mspage{538}',r'\mspage{- 538 -}',True,False,False,[],'high','omission','The typed 538 is flanked by a separate short horizontal stroke on each side. Both strokes are preserved inside the pagination field; the numeral itself is unchanged.',[793,56,946,96])
decision('B085-02','Round character after CHAPITRE',r'\unsure{O|0}',r'\unsure{O|0}',False,True,True,['O','0'],'medium','other','One closed upright oval with a slightly angular top and bottom and no slash, internal point or differentiating appendage. The adjacent typed capital O forms provide no secure distinction between the letter and a zero made with the same form. C\'s exact doubt is retained.',[428,334,455,366],'B01_chapter_round_character.jpg')
decision('B085-03','Left margin beside the cancelled 2.4 and 2.5 rows',r'\margin{\handwritten{?}}',marginal,True,False,True,['question mark','elongated 2 with a detached low stroke','non-alphabetic hooked mark with a detached stroke'],'medium','drawing or diagram','A short upper stroke runs right into a rounded turn; its long stem descends slightly left, then turns right into a short curled foot. A separate low horizontal dash lies below and to the right. The shape and relative placement are secure, but an ordinary question mark is not uniquely fixed by those strokes. The transcription now draws the mark and retains uncertainty of interpretation.',[247,1116,292,1194],'B02_left_marginal_mark.jpg')
decision('B085-04','Freehand cancellation across the old 2.4 and 2.5 rows',r'\noindent\qquad \deleted{2.4. Fonctions constructibles}\deleted{\mbox{............................}}'+'\n\n'+r'\noindent\qquad \deleted{2.5.}',cancelled,True,False,False,[],'high','drawing or diagram','The old 2.4 text and leaders and the isolated old 2.5 are cancelled as C states. The cancelling stroke begins in tall overlapping oblique runs through both number fields, continues in repeated low-returning curves under and through Fonctions, rises twice across constructibles, then runs almost horizontally through the dotted leaders to their far right. The text is still readable. No independent typed-x cancellation can be identified. C recorded deletion state but did not reproduce this graphic course.',[332,1097,1490,1189],'B03_two_row_cancellation.jpg')
decision('B085-05','Live 2.5 reference',r'2.5?',r'2.5?',False,False,False,[],'high','other','After 5 there is a curved question-mark head with a left ball terminal, a short central stem and a separate low round impression matching the nearby typewritten full stop. Its regular alignment and typeface construction settle the material reading as typed. It is not replaced with a full stop.',[330,1257,417,1291],'B04_live_2_5_mark.jpg')
decision('B085-06','Entry 3.5, linked p/r overtyping in réciproques',r'\deleted{\unsure{r}}p\deleted{p}r',r'\deleted{\unsure{r}}p\deleted{p}r',False,True,True,['r beneath the first live p; p beneath the following live r'],'low','other','The first corrected position has a live p with a lower descender and foot, together with an additional foot at the ordinary baseline and a merged upper return that is compatible with underlying r. The first upper contour is too merged to remove the doubt on r. The next position has a live r with a top hook and ordinary baseline foot, plus a lower p-like bowl, stem and foot. C\'s linked underprint reading is retained unchanged; the terminal s is a separate decision.',[658,1842,712,1881],'B05_reciproques_overtype.jpg')
decision('B085-07','Entry 3.5, terminal s of réciproques',r'roques de préfaisceaux',r'roque\unsure{s|\deleted{s}s} de préfaisceaux',True,False,True,['s with ink spread or a doubled impression','a faint underlying s and a darker live s'],'medium','deletion state (struck given live or live given struck)','A pale offset s-shaped contour extends to the right of the dark terminal s: an upper turn and a lower bowl are visible. It could be an offset impression of the same typed letter or a recoverable underlying s; the scan does not securely establish a separate correction operation. Ordinary s remains the preferred reading, with the underprint alternative now explicit. This was first noticed within the retained single crop of the corrected word and was not cropped or viewed again.',[783,1841,824,1878],'B05_reciproques_overtype.jpg')

I=[]
def inv(element,kind,position,first,hand='typewriter'):
 I.append({'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('Pagination','text','Top centre, y56–96','- 538 -')
inv('Title','text','Top centre, y122–155','TABLE DES MATIERES')
inv('Front-matter entry','text','y202–232','AVANT-PROPOS; dotted leaders')
inv('Front-matter entry','text','y270–300','INTRODUCTION; dotted leaders')
inv('Chapter heading','text','y330–367','CHAPITRE O/0 .- Préliminaires; dotted leaders')
inv('Section heading','text','y399–435','§ 1. Foncteurs représentables; dotted leaders')
for ref,y,words in [
 ('1.1',469,'Foncteurs représentables'),('1.2',519,'Produits fibrés dans une catégorie'),('1.3',571,'Changement de base'),('1.4',620,'Noyaux ; morphisme diagonal'),('1.5',671,'Foncteurs adjoints'),('1.6',721,'Structures algébriques dans les catégories'),('1.7',771,'Morphismes fonctoriels représentables')]:
 inv('Contents entry '+ref,'text',f'y{y}–{y+36}',ref+'. '+words+'; dotted leaders')
inv('Section heading','text','y836–875','§ 2. Compléments de topologie; dotted leaders')
for ref,y,words in [('2.1',904,'Espaces irréductibles'),('2.2',954,'Espaces localement noethériens')]:
 inv('Contents entry '+ref,'text',f'y{y}–{y+35}',ref+'. '+words+'; dotted leaders')
inv('Contents entry 2.3','text','y1003–1084, two physical lines','2.3. Ensembles quasi-constructibles et ensembles constructibles; dotted leaders')
inv('Old contents entry 2.4','deletion','y1105–1138','2.4. Fonctions constructibles; dotted leaders')
inv('Marginal hooked mark and separate short stroke','margin note','Left of cancelled rows, x247–292 y1116–1194','Question-like hooked shape with a low displaced dash','unnamed hand')
inv('Old number field 2.5','deletion','y1158–1189','2.5.')
inv('Cancellation graphic','drawing','Across old entries 2.4 and 2.5, x332–1490 y1097–1189','Repeated oblique and curved strokes, then a long nearly horizontal continuation','unnamed hand')
inv('Replacement contents entry 2.4','text','y1205–1238','2.4. Ensembles constructibles dans les espaces noethériens; no dotted leaders')
inv('Replacement contents entry 2.5','text','y1257–1291','2.5? Fonctions constructibles; dotted leaders')
for ref,y,words in [('2.6',1307,"Parties très denses d'un espace topologique"),('2.7',1358,'Quasi-homéomorphismes'),('2.8',1408,'Espaces de Jacobson'),('2.9',1458,'Espace sobre associé à un espace topologique'),('2.10',1509,'Applications ouvertes en un point')]:
 inv('Contents entry '+ref,'text',f'y{y}–{y+36}',ref+'.'+('' if ref=='2.10' else ' ')+words+'; dotted leaders')
inv('Section heading','text','y1576–1613','§ 3. Compléments sur les faisceaux; dotted leaders')
for ref,y,words in [('3.1',1643,'Faisceaux à valeurs dans une catégorie'),('3.2',1694,"Préfaisceaux sur une base d'ouverts"),('3.3',1745,'Recollement de faisceaux'),('3.4',1795,'Images directes de préfaisceaux'),('3.5',1842,'Images réciproques de préfaisceaux')]:
 inv('Contents entry '+ref,'text',f'y{y}–{y+37}',ref+'. '+words+'; dotted leaders')
inv('First underlying letter in 3.5','deletion','Within réciproques, x658–687 y1842–1881','r? underneath p')
inv('Second underlying letter in 3.5','deletion','Within réciproques, x683–712 y1842–1881','p underneath r')
inv('Possible same-letter overtype in 3.5','deletion','At end of réciproques, x783–824 y1841–1878','s; alternative faint underlying s explicitly marked')
inv('Contents entry 3.6','text','y1895–1931','3.6. Faisceaux simples et faisceaux localement simples; dotted leaders')
inv('Contents entry 3.7','text','y1944–2035, two physical lines',"3.7. Images réciproques de faisceaux de groupes ou d'anneaux; dotted leaders")
inv('Archive number recorded in a comment','text','Lower left, x173–221 y2070–2111','84','unnamed hand')

R={
 'scan':85,'reader':'B','image_views':manifest['source_views'],'reading_path':str(out/'reading.tex'),
 'crops':[{k:c[k] for k in ['file','bbox','rotation','reason']} for c in manifest['crops']],
 'decisions':D,'inventory':I,
 'notes':"One typescript contents page, titled TABLE DES MATIERES without a grave accent on the capital E. The page is numbered - 538 - at the top; archive number 84 is at lower left and is recorded only in a comment. There is no date, salutation or signature. The contents comprise AVANT-PROPOS, INTRODUCTION, CHAPITRE O/0 .- Préliminaires, section 1 with entries 1.1–1.7, section 2 with entries 2.1–2.10 plus cancelled old 2.4 and 2.5 entries, and section 3 with entries 3.1–3.7. Two live replacement entries follow the cancelled pair; no renumbering or spelling correction has been made. The replacement 2.5? has a typed question mark, an explicit authorial questioning mark whose scope is unstated. The separate marginal mark may also be a question mark, but its actual hooked contour and displaced low dash are drawn with interpretive uncertainty. The cancellation is freehand; no writer is named or inferred. The p/r pair in entry 3.5 contains overtyping, and the faint offset terminal s is separately marked as uncertain in material interpretation. H supplies description only and was unavailable as a transcription: every h_reading is null and every diff_h is false. No historical identification or speculative hand attribution from H has been adopted.",
 'math_reading_decisions':[
  'The page contains section signs and decimal contents references, but no mathematical formula, statement, proof or computation. No theorem or consistency check event is claimed.',
  'Every heading and entry was read in order. All printed letters, accents, singular/plural endings, spaces within the numbering fields, semicolon in Noyaux ; morphisme diagonal, apostrophes, hyphens and leaders were inspected. The half images settled those not recorded separately.',
  'The unmarked C-context title target is confirmed as TABLE DES MATIERES: there is no grave above E. The ordinary typewritten capitals were not turned into mathematical double-struck letters.',
  'The chapter O/0 cannot be distinguished from its closed oval outline; the exact C doubt is retained.',
  'The two old entries remain deleted, and the live replacements remain in their actual order. The replacement 2.4 has no leaders. The punctuation of the replacement 2.5? is confirmed as typed.',
  '2.10.Applications has no intervening space after the final point. The section signs and every individual reference number are retained without renumbering.',
  'The authorial question-mark value is secure after live 2.5; the separate marginal shape is not used to infer a missing instruction, word or insertion.',
  'The linked underprint r? / p in the corrected word is retained, while a new independent material uncertainty at the terminal s is marked explicitly. Neither is silently normalized to the expected word.'
 ],
 'check_events':[],
 'notation':[
  {'sign':'Chapter oval','latex':r'\unsure{O|0}','evidence':'Closed upright oval without a differentiating slash or appendage.','place':'Chapter heading'},
  {'sign':'Section signs and decimal references','latex':r'\S\ 1.; \S\ 2.; \S\ 3.; 1.1.; 2.10.; 3.7.','evidence':'Each section sign has two opposed curved loops; each decimal field has the printed digits and low points individually inspected.','place':'Section headings and contents entries'},
  {'sign':'Typed authorial question mark','latex':'2.5?','evidence':'Curved head with ball terminal, short stem, and a low circular impression matching the typewriter punctuation.','place':'Live replacement 2.5'},
  {'sign':'Leaders','latex':r'\dotfill','evidence':'Regular series of low rounded typewriter points to the right of entries; absent on the replacement 2.4 and the otherwise blank old 2.5.','place':'Contents entries'},
  {'sign':'Unresolved marginal graphic','latex':marginal,'evidence':'Long upper hooked stroke with a right-turning foot and a separate low dash displaced right.','place':'Left of old 2.4 and 2.5'},
  {'sign':'Handwritten cancellation','latex':cancelled,'evidence':'Tall crossing obliques through both old number fields, followed by low-returning waves and a long near-horizontal stroke through leaders.','place':'Old 2.4 and 2.5'},
  {'sign':'Corrected letter pair','latex':r'\deleted{\unsure{r}}p\deleted{p}r','evidence':'Overlaid ordinary-baseline and descender feet with merged top contours at first position; a p-like lower contour beneath the next r.','place':'Entry 3.5, réciproques'},
  {'sign':'Terminal same-letter impression uncertainty','latex':r'\unsure{s|\deleted{s}s}','evidence':'Faint s-shaped upper turn and lower bowl offset right of the dark final s; overtyping versus ink spread not secure.','place':'Entry 3.5, terminal s of réciproques'}
 ],
 'abbreviations':[],
 'slips':[
  'The page retains an old deleted 2.4. Fonctions constructibles and an isolated old 2.5. before live replacement 2.4 and 2.5?; this revision is preserved rather than renumbered.',
  'The live 2.5 field ends in a typed question mark; it is preserved instead of silently replacing it with a full stop.',
  'Entry 3.5 shows linked p/r overtyping and a possible offset same-letter impression at the final s; the uncertain physical traces remain explicit.'
 ],
 'completion':'Complete independent diplomatic reading of scan 085 only. The whole image was viewed once for layout, half a once and half b once in that order, with every line read against C. Five unique tight enlarged crops were then made and each viewed once; all source bounds, processing parameters and actual/requested view counts are retained in crop_manifest.json. No OCR, text extraction, research, other-page inspection, peer-reader file inspection, delegation or TeX compilation was used. H was treated exclusively as unavailable descriptive context. Every explicit C transcription doubt, every substantive C difference and each new uncertainty has an individual decision with original-image coordinates. All contents blocks, pagination, dotted leaders, cancelled rows, freehand graphic, marginal mark, corrected/possibly overtyped letters and archive number are represented. Structural checks are recorded separately.'
}
(out/'report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reading':str(out/'reading.tex'),'report':str(out/'report.json'),'decisions':len(D),'differences_from_C':sum(d['diff_c'] for d in D),'explicit_C_doubts':sum(d['c_doubt'] for d in D),'inventory_rows':len(I),'crops':len(R['crops'])},ensure_ascii=False))
