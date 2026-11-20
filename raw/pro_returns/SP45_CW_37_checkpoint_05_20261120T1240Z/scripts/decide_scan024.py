#!/usr/bin/env python3
"""Main-reader decisions, after all three returns and the recorded crops."""
from pathlib import Path
import copy,json
R=Path(__file__).resolve().parents[1]
D={r:json.loads((R/f'readers/scan024/{r}/report.json').read_text()) for r in ('r1','r2','r3')}
C=copy.deepcopy(D['r3']['changes'])
map1={0:0,1:1,2:2,3:3,4:4,5:5,6:5,7:5,8:7,9:6,10:8,11:9,12:10,13:11,14:12,15:13,16:14,17:15,18:16,19:17,20:18,21:19,23:20,24:21,25:21,26:22,27:23,28:24,29:25,30:26,32:27,33:28,34:29,36:30,37:31,38:32,39:33,40:34}
map2={i:i for i in range(22)}
map2.update({6:7,7:6,22:22,23:23,24:24,25:24,26:25,27:26,28:27,29:28,30:29,31:30,32:31,33:32,34:33,36:34,37:35,38:36,39:37,40:38})
plain1={22:'Right margin anchored after En deduire/déduire',31:r"sss $X'$ est \deleted{\illegible{1}}.; low remnants included in cancellation",35:'Not reproduced'}
for i,c in enumerate(C):
 c['readers']={'r1':D['r1']['changes'][map1[i]]['reading'] if i in map1 else plain1[i], 'r2':D['r2']['changes'][map2[i]]['reading'] if i in map2 else 'Not reproduced','r3':c['reading']}
 c['mathematical_consequence']=''
 c['evidence']='Main inspected the cited crop: '+c['evidence']
new={0:'letterhead',2:'Ajouter',15:'b_label',34:'double_divider',36:'IX',37:'pour',38:'single_divider',39:'bottom_VII'}
for i,p in new.items():C[i]['crop']=f'crops/scan024/main_{p}.jpg'
C[0].update(diff_c=True,kind='insertion or placement',reading='Printed INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / short rule, centred within the left approximately two-thirds of the sheet',evidence='Main letterhead crop includes both page edges: the printed block and short rule are centred around the left two-thirds, with a substantially wider blank region on the right. r2 retains that placement in a left 0.66-textwidth minipage; C/r1/r3 centre it over the whole text width. The letters, acute on É and separate printed rule are clear. H describes IHES paper but omits the printed text and rule.')
C[0]['c']=r'\begin{center} I N S T I T U T / DES HAUTES ÉTUDES SCIENTIFIQUES / \rule{1cm}{0.4pt} \end{center}'
C[0]['readers']={'r1':'Printed block centred across the full text width','r2':'Printed block centred in left 0.66-textwidth minipage','r3':'Printed block centred across the full text width'}
C[1]['evidence']='Main r3 crop 01 shows V and two separate following upright I strokes, between an upper and lower line. All readers resolve C001 to VII. H emph does not reproduce these two strokes.'
C[2]['evidence']='Main Ajouter crop shows a continuous separate horizontal underline under the whole word. The source state is not reproduced by H italic emph.'
C[3]['evidence']='Main r3 crop 02 shows the small a within a closed pale oval, not two open parentheses. All three agree.'
C[4]['evidence']='Main r3 crop 02 separates the upper wave over X from the lowered bare e and t. No acute is supplied in the subscript.'
C[5]['evidence']='Main r3 crop 03 shows a looped d with a tall right stem, followed by an independent dot, then t/o/r/s/i/o/n. No e follows d. The comma after algébrique is separate; the apparent mark after torsion is continuous with the long insertion call. All three agree, resolving C002 and rejecting H cf. fonction.'
C[5]['mathematical_consequence']='The inserted property reads d. torsion, whereas H reads cf. fonction; the literal property wording is restored without expanding d. in the transcription.'
C[6]['evidence']='Main r3 crop 03 shows three nested call paths: the long call before localement, the smaller call from algébrique to its higher ref, and the separate call after localement cohérent. All three draw these paths; r2 geometry is retained. C attachment macros and H descriptive note do not draw the nested paths.'
C[6]['reading']='Three nested insertion calls drawn in the r2 TikZ setting, with the upper reference and long turned terminal retained.'
for i in (7,8):C[i]['evidence']='Main r3 crop 03 shows the unaccented letters (ref), with its call and above-line position as transcribed. No independent acute is present; H writes réf. The uncertainty on H fonction is not a doubt on this separate reference.'
C[9]['evidence']='Main r3 crop 03 shows one low dot followed by tall capital I and l. No detached upper semicolon dot is present. All three agree on . Il.'
C[10]['evidence']='Main r3 crop 04 shows unaccented (ref) above the crossed word following the second cohérent. The cancelled mass itself remains unreadable in all three readings and C. H has a doubt on that mass, but not on the differing reference accent or placement; marked_in_H is therefore false for this row.'
C[10]['marked_in_H']=False
C[11]['evidence']='Main r3 crop 05 shows opening parenthesis, compressed r/e/s, p descender and dot, quasi-séparé, the added unaccented (ref), and closing parenthesis. All readers resolve resp. H keeps the reference but omits the parenthetical phrase.'
C[11]['mathematical_consequence']='H omits the written parenthetical resp. quasi-séparé case. The consolidated reading retains that case and its separate reference slot.'
C[12]['evidence']='Main r3 crop 05 shows three s-shaped hooks after the dense cancellation, with no final i dot. All three resolve C006 to literal sss.'
C[13].update(diff_c=True,reading=r'\deleted{\unsure{quasi-cpt|qu.-cpt}}',confidence='medium',evidence='Main r3 crop 06, inspected for the cancelled word only, exposes initial q and final c/p/t while the strike conceals the middle. r1/r3 retain quasi-cpt alone; r2 also allows qu.-cpt. Neither middle can be excluded by the covered strokes, so both are retained. H expands the ending to compact, which the ink does not spell out.')
C[14].update(diff_c=True,reading=r'qu. cpt qu. \unsure{sép|sep}',confidence='medium',crop='readers/scan024/r1/crops/07_explanatory_abbreviations.jpg',evidence='Main r1 crop 07 was inspected for the live abbreviation after i.e. The qu forms, their dots and cpt are clear. The raised trace over the last short sep run is not separable enough to establish an acute. r2 sép|sep is retained over r1/r3 plain sép. H expands both abbreviations.')
C[15]['evidence']='Main b-label crop shows a closed pale oval around the b. H correctly describes the enclosure in an ordinary note, but gives parentheses instead of drawing it; that note is not a doubt flag.'
C[16]['evidence']='Main r3 crop 09 shows separate lines above and below ordinary I and V. C records only the lower line, H neither.'
C[17]['evidence']='Main r3 crop 09 shows a separate low curved comma after the closing parenthesis, without the detached upper dot needed for a semicolon. All three and H agree against C.'
C[18]['evidence']='Main r3 crop 10 shows a detached roof above a complete A. All three resolve C009 to Âlors; the anomalous accent is retained.'
C[19]['evidence']='Main r3 crop 10 shows bare e/t below X and a separate wave above X. All three omit H acute on the subscript.'
C[20]['evidence']='Main r3 crop 10 shows l/i/m/t/o/p on the same baseline, p descending through the shaft, and a left arrow below the entire run. All three and C agree. H explicitly doubts its placement of top as a lower index.'
C[21].update(diff_c=True,reading=r'En \unsure{deduire|déduire} pour 5.7.',confidence='medium',crop='readers/scan024/r1/crops/11_deduire.jpg',evidence='Main r1 crop 11 shows the complete En deduire run, pour and 5.7. but does not isolate a secure acute over the first e of deduire. r1 retains both accent states; r2/r3 resolve déduire. The consolidated reading keeps r1 doubt rather than supply the accent. H leaves the words unreadable.')
cor='readers/scan024/r3/crops/11_corollary.jpg'
for i in range(22,34):C[i]['crop']=cor
C[22]['evidence']='Main r3 corollary crop locates the block level with the displayed conclusion and above/right of En deduire. r2 anchors it before the display; r3 after the display; r1 after En deduire. The r2 anchor is adopted to retain the source relationship. H makes it ordinary following text; C anchors it after En déduire.'
C[23]['evidence']='Main corollary crop shows a distinct line directly under Cor., before 5.6.1. H omits that underline.'
C[24]['evidence']='Main corollary crop shows X-prime, membership, Ob, then ordinary X with low et. No wave is above that X and no Et(X) parentheses occur. All three resolve C010 to X_et; the independent lower curve is recorded in the next row.'
C[25]['evidence']='Main corollary crop shows a shallow detached upward-ended curve BELOW et. All three draw the stroke there, without moving it to an overhead tilde or assigning it a mathematical function. It is absent as a separate graphic from C and H.'
C[26].update(confidence='low',evidence='Main corollary crop leaves a tall middle fragment and a t-like ending under the crossing immediately after est, enough only for tentative cohérent. All readers retain the doubt. H leaves it unreadable and places its cancellation later, after the X_et expression; both reading and source location are preserved here.')
C[27].update(marked_in_H=True,evidence='Main corollary crop shows qu., a gap, and c/p/t within the left oval, with no independent hyphen. r2/r3 resolve qu. cpt; r1 retains qu.-cpt doubt. The former is adopted at medium confidence. The oval and small outer loop are drawn. H expressly marks its quasi-sép. reading as uncertain and locates it in this left oval, so the physical-locus flag is true.')
C[28]['evidence']='Main corollary crop shows a live parenthesis after the cancellation, before dans. The compressed qu. and sep run support the abbreviation, while the small upper trace does not decide the accent. r3 qu. sép|qu. sep is retained, making r1/r2 implicit accent doubt explicit. H expands and relocates the expression to the left oval.'
C[29]['evidence']='Main corollary crop shows the second X with bare lower e/t after dans. All three agree; no acute is supplied.'
C[30]['evidence']='Main corollary crop shows three low s hooks before X-prime, without a detached final i dot. All three and C agree; this also resolves the second part of the prior C question.'
C[31]['evidence']='Main corollary crop shows two separate low dots between est and the crossed cluster. r2/r3 distinguish them, whereas r1 includes them among cancelled remnants. Their detachment supports preserving exactly two dots, without lexical expansion.'
C[32]['evidence']='Main corollary crop shows the crossed cluster followed by a dot, then the right circled addition. No separate live q and c are visible there. All three reject H live q.c. The H illegibility mark on the neighbouring cancellation does not mark doubt on this added q.c.; marked_in_H is false.'
C[32]['marked_in_H']=False
C[33]['reading']=r'\inserted{resp. coh} inside right oval, with separate vertical leader from the inline parenthesis above'
C[33]['readers']['r1']+='; vertical leader drawn'
C[33]['readers']['r2']+='; vertical leader omitted'
C[33]['readers']['r3']+='; vertical leader omitted'
C[33]['evidence']='Main corollary crop resolves resp., then c/o/h, without a point after h. It also shows a separate near-vertical leader down from the inline parenthesis to the right oval; this is distinct from the p descender. r1 draws that line, r2/r3 omit it. Its geometry is added to the r2 setting. H describes the enclosure but does not draw it; no doubt is marked on resp. coh.'
C[34]['evidence']='Main double-divider crop shows two long gently curved rising strokes, each with a short turned right end. r2/r3 curvature is supported; r1 straight segments preserve the turns but flatten the lines. C lacks the turns. H accurately describes the double line without drawing it. The r2 paths are retained, without interpreting the turns as arrows.'
C[35]['evidence']='Main r3 crop 12 shows a tiny faint bent stroke to the left of SGA 4 IX. r3 alone includes it; r1/r2 and both witnesses omit it. It is drawn literally, with no assigned letter, number or editorial function.'
C[36]['evidence']='Main IX crop shows separate top and bottom strokes around I and X. H italic emph is not equivalent to those two source lines.'
C[37]['evidence']='Main pour crop shows descending p, joined ou and final r, with a separate underline. All three and C read pour; H leaves that word unreadable.'
C[38].update(diff_c=True,evidence='Main single-divider crop shows a long pencil line rising by roughly 65 source pixels over about 1000, with a shallow curved course. r1/r3 draw curvature; r2 has a steeper straight segment. The r3 curved path is adopted. C gives a much shallower straight segment; H omits the line. This is a graphic shape/relative-position correction, not a new textual mark.')
C[39]['evidence']='Main bottom-VII crop shows V and two distinct I strokes between separate upper and lower lines. All three and C agree; H gives italic emphasis only.'
C[40].update(crop='readers/scan024/r1/crops/13_bottom_corriger.jpg',evidence='Main r1 crop 13 shows initial c/o, two r strokes, dotted i, descending g and final e/r over an underline. All three and C read corriger. H tentative erroné has incompatible initial and terminal letter shapes.')
cd=copy.deepcopy(D['r3']['c_doubts'])
for j,i in [(0,1),(1,5),(3,11),(5,12),(6,13),(8,18),(9,24),(10,26),(11,27),(12,28),(14,33),(15,30)]:
 cd[j].update(evidence=C[i]['evidence'],crop=C[i]['crop'])
cd[6]['reading']=C[13]['reading'];cd[10]['reading']=r'\deleted{\unsure{cohérent}}'
cd[2]['evidence']='All three retain the opaque short cancellation; main r3 crop 04 also leaves it physically unreadable.'
cd[4]['evidence']='All three retain the dense long cancellation; main r3 crop 05 also leaves it physically unreadable.'
cd[7]['evidence']='All three independent half/crop readings retain this same isolated cancellation. Their reports agree that no full word can be recovered. No extra main crop was taken at this agreed unchanged locus.'
cd[13]['evidence']='All three retain the last opaque corollary cluster, also unresolved in main corollary crop. The preceding two dots and following dot are recorded separately.'
un=copy.deepcopy(D['r2']['unresolved'])
un[6].update(reading=r'\unsure{qu. sép|qu. sep}',alternatives=['qu. sép','qu. sep'])
un.insert(5,copy.deepcopy(D['r1']['unresolved'][4]))
un+=copy.deepcopy(D['r3']['unresolved'][7:9])
inv=copy.deepcopy(D['r2']['inventory'])
inv[21]['first_words_or_objects']='Doubtful (qu. sép / qu. sep)'
inv[23]['first_words_or_objects']='resp. coh in a long shallow oval with separate vertical leader'
inv[24]['first_words_or_objects']='En deduire/déduire pour 5.7.'
inv[27]['first_words_or_objects']='Single long rising, shallowly curved pencil divider'
inv.insert(26,copy.deepcopy(D['r3']['inventory'][25]))
notes=copy.deepcopy(D['r2']['notes'])
notes[3]['text']=notes[3]['text'].replace('qu. sép.','qu. sép/qu. sep.').replace('preserved spatially','preserved spatially')
notes[4]['text']='The instruction below the display reads En deduire/déduire pour 5.7.; the first e accent remains uncertain. The final pencil instruction is corriger, underlined. These are editorial instructions, not evidence that a mathematical claim was disproved or verified.'
notes.append({'id':'s024-note08','text':'The small lower curve under the first corollary et and a faint bent left-margin stroke are drawn without assigned meaning. The marginal corollary is aligned with the display; its right oval has a separate vertical leader. Two low dots before its final cancellation remain dots. No word is restored from them.','basis':'Main corollary and r3 left-mark crops; documentary observations only.'})
nt=copy.deepcopy(D['r2']['notation'])
nt.append(copy.deepcopy(D['r3']['notation'][7]))
nt.append({'sign':'Corollary call geometry','latex':'TikZ left oval with outer loop; right oval with vertical leader','locus':'Cor. 5.6.1.','evidence':'Main r3 corollary crop; right vertical line independently drawn by r1.','alternatives':'No interpretation or edit chronology assigned.'})
repls=[(r'En déduire pour 5.7.',r'En \unsure{deduire|déduire} pour 5.7.'),(r'(\unsure{qu. sép})',r'(\unsure{qu. sép|qu. sep})'),(r'\draw[line width=.35pt,rotate around={6:(365,-91)}]',r'\draw[line width=.35pt] (365,-54)--(365,-87);'+'\n'+r'\draw[line width=.35pt,rotate around={6:(365,-91)}]')]
r3tex=(R/'readers/scan024/r3/reading.tex').read_text()
mark=r3tex[r3tex.index('% Isolated faint bent stroke'):r3tex.index(r'\handwritten{SGA 4 $\overline{\text{\uline{IX}}}')]
repls.append((r'\handwritten{SGA 4 $\overline{\text{\uline{IX}}}',mark+r'\handwritten{SGA 4 $\overline{\text{\uline{IX}}}'))
single=r3tex[r3tex.index(r'\figure{\begin{tikzpicture}[x=.012cm,y=.012cm]',r3tex.index('% Isolated faint bent stroke')):r3tex.index(r'\handwritten{$\overline',r3tex.index('% Isolated faint bent stroke'))].strip()
repls.append((r'\figure{\begin{tikzpicture}\draw (0,0)--(12,0.76);\end{tikzpicture}}',single))
viewed=[f'readers/scan024/r3/crops/{n}.jpg' for n in ['01_top_roman','02_a_symbol','03_upper_insertions','04_second_coherent_cancel','05_parenthesis_sss','06_quasi_cpt','09_b_limit_ref','10_alors_display','11_corollary','12_pencil_left_mark']]+[f'readers/scan024/r1/crops/{n}.jpg' for n in ['07_explanatory_abbreviations','11_deduire','13_bottom_corriger']]+[str(p.relative_to(R)) for p in sorted((R/'crops/scan024').glob('main_*.jpg'))]
cfg={'approved_by_main_reader':True,'scan':24,'base_reader':'r2','brief_version':'v008','changes':C,'c_doubts':cd,'unresolved':un,'inventory':inv,'notes':notes,'notation':nt,'abbreviations':D['r2']['abbreviations'],'replacements':repls,'main_crop_count':8,'main_viewed_crops':viewed,'adjudications':[],'workflow_observation':'All three complete readings and every report section compared. Main inspected 13 existing reader crops and 8 new tight crops; no whole/half source view. One attempted three-image response was truncated before delivery and counted as no inspection; those existing paths were then displayed once successfully. The cancelled quasi-cpt crop and live-abbreviation crop were each used for their separate locus. Source graphics were checked independently of editorial meaning.','adjudication_note':'r2 base, with r1 deduire accent doubt and right-oval vertical leader; r3 corollary accent alternative, faint left bent mark and curved single divider. Main retains r2 additional cancelled qu.-cpt alternative and live sép/sep doubt. All C001–C015 and the prior joint sss question are explicit. Two H doubt flags were confined to the differing words, not neighbouring illegibilities. No mathematical proof check was performed.'}
(R/'decisions/approved_scan024_config.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print('approved',len(C),'changes',sum(c['diff_c'] for c in C),sum(c['diff_h'] for c in C),'views',len(viewed))
