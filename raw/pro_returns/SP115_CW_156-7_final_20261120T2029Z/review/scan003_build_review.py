from pathlib import Path
import json
root=Path('/workspace/scratch/ddf8babdc42e')
manifest=json.loads((root/'out/review/scan003_crop_manifest.json').read_text())
changes=[]
def change(i,place,C,H,final,shows,conf,kind,crop,againstC,againstH,markedH=False,consequential=False,box=None):
    m=manifest[crop] if crop else None
    changes.append(dict(id=f'S003-{i:02d}',place=place,C=C,H=H,final=final,scan_shows=shows,confidence=conf,kind=kind,crop=m['path'] if m else None,box=m['box'] if m else box,against_C=againstC,against_H=againstH,marked_in_H=markedH,consequential=consequential))
change(1,'main line 1, first word',r'\unsure{contexte|contextes}','contexte','contexte','The final crossed t is followed by its low e exit; there is no additional terminal s before the gap and d\'un.','high','C doubt resolved','context',True,False)
change(2,'quotation marks throughout, including contrée; figure élémentaire; multistrate; lieu; lieu ponctuel; point; strates; grande multiombre; grande ombre; support','double quotation marks encoded with two backticks and two apostrophes','French guillemets, with the last pair displaced around support','double quotation marks encoded with two backticks and two apostrophes','The source has pairs of short raised quotation strokes, not angle-shaped guillemets. The marks around the final support precede and follow that word. Confirmed in the halves; the parenthetical and bottom crops show representative pairs.','high','source punctuation form',None,False,True,False,False,[250,170,540,238])
change(3,'main lines 9–11, parenthetical about lieu ponctuel / point','(voire, la notion de ``lieu ponctuel\'\' ou ``point\'\', dont il n\'a pas encore été question...)','(voire, [ill.] la notion de « lieu ponctuel » — ou « point » [ill.] — qui [ill.] par avoir été [ill.]…)','(voire, la notion de ``lieu ponctuel\'\' ou ``point\'\', dont il n\'a pas encore été question...)','The horizontal main line reads ou point, followed by dont il n\'a pas encore été; question is written on the next baseline, before three dots and the closing parenthesis. The extra dash interruptions in H are absent. Diagonal strokes over the area belong to the marginal note.','high','words and omissions','lieu_point',False,True,True,True)
change(4,'eight-line diagonal marginal note, beside main lines 8–20','Full marginal text, with the C doubts itemized separately','L\'autre raison [ill.] « [ill.] » [ill.] simplicité [ill.] figures [ill.] multistrates',r'L\'autre raison, c\'est que, dans le cas d\'une ``application $f$\'\' d\'une ``région\'\' dans une autre, l\'image inverse d\'une ``figure\'\' (\unsure{quand|quant} \unsure{on} peut donner un sens \unsure{géométrique} \unsure{à} \unsure{ce} \unsure{mot|terme}) \deleted{\unsure{sera}} tend à ne \unsure{pas} être \unsure{encore} une figure, mais l\'image réciproque d\'une multistr. est une multistr.','Rotation separates the diagonal baselines from the large horizontal text. It shows application f, région, image inverse, figure, and the final contrast with image réciproque / multistr. The places where the two directions of ink cross remain explicitly doubtful. H\'s marginal synopsis does not transcribe the complete note; its accompanying editorial note is not source text.','medium','marginal text omitted or misread by H','margin',False,True,True,True)
change(5,'margin line 5, peut donner',r'\unsure{donner}','not transcribed','donner','The upright loop of d, low connected o/nn, and the terminal er are visible on the rotated crop. There are no additional letters or strike through this word.','high','C doubt resolved','margin',True,True,True)
change(6,'margin line 6, after cancelled word',r'\unsure{tend}','not transcribed','tend','The live word after the cancellation begins with an upright crossed t; the following connected en and final d can be separated from the horizontal main text.','high','C doubt resolved','margin',True,True,True)
change(7,'main line 13, opening after algébrique,','où',r'\uncertain{quand}','où','Only a short o/u group stands before il; the accent is above the second letter. There is no initial q descender and no sequence long enough for quand.','high','different word','ou_simplicite',False,True,True,True)
change(8,'main line 14, les lieux et multistrates','lieux','figures','lieux','The word ends in a separate small x cross. Its beginning has the tall l followed by the dotted i and low eu strokes; a descending diagonal crossing nearby belongs to the marginal note, not a g in figures.','high','different word','lieux_etant',False,True,False,True)
change(9,'main line 14, comme étant',r'\unsure{étant}','étant','étant','The final short word has the accented e, t, compressed an and terminal t stroke. It is followed on the next line by des figures particulières.','high','C doubt resolved','lieux_etant',True,False)
change(10,'above main line 16, between figure and est',r'\inserted{$F$}','$F$',r'\inserted{$F$}','F is above the baseline and has its own descending attachment into the gap after figure; it is not an ordinary baseline letter.','high','insertion state','figure_insertions',False,True,False,True)
change(11,'insertion above main line 16, par l\'ens de ses strates',r"l'\unsure{ens|ensemble}","l'ens.","l'ens",'There are only the compact ens strokes, followed by the space and de; no following emble and no abbreviation point are written. The entire parenthetical is inserted by a line whose left end descends into the gap before comme.','high','abbreviation and C doubt resolved','figure_insertions',True,True)
change(12,'main lines 16–17, comme partie','comme partie','comme une partie','comme partie','The word comme occupies the end of line 16. Line 17 starts partie. No une is written in the intervening space, above it, or at the start of line 17.','high','H added word','figure_insertions',False,True,False,True)
change(13,'main line 17, de l\'ens M',r"l'\unsure{ens}","l'ens.","l'ens",'The low connected ens group is followed directly by a space and the mathematical capital. There is no separate period after ens.','high','abbreviation and C doubt resolved','figure_insertions',True,True)
change(14,'main line 17, set letter M, recurring in line 20',r'\unsure{M|\mathcal M}; later M',r'\mathcal{M} at both places',r'\unsure{M|\mathcal M}; later M','Both bare set letters have rounded entry/exit strokes and two high stems. Their distinction from an ordinary handwritten M is not secure enough to settle the alphabet on this page alone. The whole isolated symbol was inspected in both contexts; the C doubt is retained at the first occurrence.','low','retained alphabet doubt','figure_insertions',False,True,False,True)
change(15,'lower insertion after set M, ordonné',r'\unsure{ordonné}','ordonnée','ordonné','The accented final e is the last letter before the space to par. There is no further e corresponding to H\'s feminine ending.','high','different ending and C doubt resolved','figure_insertions',True,True,False,True)
change(16,'lower insertion, par ≤',r'\unsure{par|pour}','par','par','After the descending p the short a/r group leads into the space before the inequality. There is no intervening o/u pair. The inequality contains the upper < and the separate lower bar.','high','C doubt resolved','figure_insertions',True,False,False,True)
change(17,'attachment of (ordonné par ≤)',r"de l'ens $M$ \inserted{(ordonné par $\leq$)} des multistrates",r"une partie \add{(ordonnée par $\leq$)} de l'ens $\mathcal M$",r"de l'ens $\unsure{M|\mathcal M}$ \inserted{(ordonné par $\leq$)} des multistrates",'The long insertion bracket below the parenthetical descends at the right of the M on the next baseline. Its attachment is to M; it does not lead to partie at the far left. The other parenthetical, par l\'ens de ses strates, has a separate connector above.','high','insertion attachment','figure_insertions',False,True,False,True)
change(18,'main line 20, nous l\'écrivons',r"\unsure{l'écrivons|l'écrirons}","l'écrivons","l'écrivons",'After écri the next shallow paired stroke is v, followed by ons. There is no second r-shaped upright after the dotted i.','high','C doubt resolved','ensembliste_ecrivons',True,False)
change(19,'main line 21, first functor name',r'\mathrm{Mulomb}(F)',r'\mathrm{Multomb}(F)',r'\mathrm{Mulomb}(F)','The tall loop of l is followed immediately by the round o; no crossed t is written between them. The entire argument (F) is present.','high','functor spelling','mulomb_first',False,True,False,True)
change(20,'main line 22, son support est','est','étant','est','A short e/s stroke leads into the terminal crossed t. The word ends before the wide gap to Omb(F); there is no an group.','high','different word','support_est',False,True,False,True)
change(21,'main line 24, second functor name',r'\mathrm{Mulomb}(F)',r'\mathrm{Multomb}(F)',r'\mathrm{Mulomb}(F)','The second occurrence again has the looped l followed by o, with no t. Both (F) and the following comma are visible.','high','functor spelling','mulomb_permet',False,True,False,True)
change(22,'main line 24, ne permet','permet','permettant','permet','The word has one terminal t stroke at the right of the line. No second t and no following ant are written.','high','different word','mulomb_permet',False,True,False,True)
change(23,'main line 25, réconstituer','réconstituer','reconstituer','réconstituer','A separate, dark ascending accent stroke stands above the first e, between the initial r and the next letter. It is the same ink weight as the writing and is retained as written.','high','written accent','reconstituer_deletion_support',False,True)
change(24,'main line 25, cancellation after F,',r'\deleted{\unsure{il|le}}','omitted',r'\deleted{\unsure{il|le}}','The small cancellation is separate from the live F and comma. Its intersecting strokes obscure the underlying letters; neither il nor le is sufficiently plain to remove the C doubt. The live mais begins on the next line.','low','deleted text omitted by H','reconstituer_deletion_support',False,True,False,True)
change(25,'margin line 6, cancellation before tend',r'\deleted{\unsure{sera}}','omitted',r'\deleted{\unsure{sera}}','A short word before tend is crossed by compact multiple strokes. The beginning is obscured; the cancelled reading sera remains explicitly doubtful, and the live tend is outside the cancellation.','low','deleted text omitted by H','margin',False,True,True,True)

doubts=[
 dict(place='margin line 4',reading='quand',alternatives=['quant'],confidence='medium',reason='The terminal ascender lies in overlapping diagonal and horizontal ink; the distinction d/t remains insufficiently plain.'),
 dict(place='margin line 4',reading='on',alternatives=[],confidence='medium',reason='The short group after quand lies amid crossing main-text strokes; the two-letter reading remains plausible but not fully separable.'),
 dict(place='margin line 5',reading='géométrique',alternatives=[],confidence='medium',reason='The initial/descending forms and overall sequence fit, but central letters cross the larger horizontal writing.'),
 dict(place='margin line 5',reading='à',alternatives=[],confidence='medium',reason='A very short group beside the crowded final part of the parenthesis; accent and base cannot both be isolated confidently.'),
 dict(place='margin line 5',reading='ce',alternatives=[],confidence='medium',reason='Small connected strokes overlap the large body hand; retained from C without asserting certainty.'),
 dict(place='margin line 5',reading='mot',alternatives=['terme'],confidence='low',reason='The final word and closing parenthesis occupy an overlap. Individual letters do not securely decide the two C alternatives.'),
 dict(place='margin line 6, struck word',reading='sera',alternatives=[],confidence='low',reason='The first letters are obscured by the cancellation; not every letter is plain. The C doubt must remain.'),
 dict(place='margin line 6',reading='pas',alternatives=[],confidence='medium',reason='The apparent p and short following strokes cross main-text forms; the complete word is not fully separable.'),
 dict(place='margin line 6',reading='encore',alternatives=[],confidence='medium',reason='The low connected middle letters are crossed by larger horizontal ink; the C doubt is retained.'),
 dict(place='main line 17, first M; recurring line 20',reading='M',alternatives=[r'\mathcal M'],confidence='low',reason='The two bare capitals are consistent with each other, but ordinary cursive M versus intentional calligraphic M cannot be decided securely from this page. The first occurrence remains marked; the second uses the first candidate.'),
 dict(place='main line 25, struck word after F,',reading='il',alternatives=['le'],confidence='low',reason='The compact cancellation covers the diagnostic strokes. Neither candidate can be read letter by letter.'),
]

inventory=[
 dict(element='handwritten page number 2',kind='page number',position='top centre; [792,23,825,55]',first_words_or_objects='2'),
 dict(element='continuation of preceding text',kind='main prose; handwritten',position='main lines 1–2; upper page',first_words_or_objects="contexte d'un atelier définissant une contrée"),
 dict(element='main paragraph',kind='main prose; handwritten',position='main lines 3–26; entire body',first_words_or_objects='Le travail précédent a permis de dégager'),
 dict(element='single underline',kind='underlining',position='main line 7, below figure; about [422,642,598,658]',first_words_or_objects='figure'),
 dict(element='diagonal marginal note',kind='margin note; handwritten',position='eight diagonal baselines crossing left half of body; [15,645,1005,1845]',first_words_or_objects="L'autre raison, c'est que, dans le cas"),
 dict(element='inserted variable',kind='insertion',position='above main line 16, after figure; [650,1365,720,1438]',first_words_or_objects='F'),
 dict(element='upper parenthetical',kind='insertion',position='above main line 16; connector descends before comme; [955,1335,1465,1435]',first_words_or_objects="(par l'ens de ses strates)"),
 dict(element='lower parenthetical',kind='insertion',position='between main lines 16–17, attached at M; [640,1408,1100,1520]',first_words_or_objects='(ordonné par ≤)'),
 dict(element='adjective above figure',kind='insertion',position='above main line 20, attached between figure and dans; [620,1690,980,1790]',first_words_or_objects='ensembliste'),
 dict(element='cancelled marginal word',kind='deletion',position='margin line 6, before tend; [28,1558,125,1672]',first_words_or_objects='sera (doubt retained)'),
 dict(element='cancelled final-line fragment',kind='deletion',position='end of main line 25; [1474,2160,1540,2230]',first_words_or_objects='il / le (doubt retained)'),
]
notation=[
 dict(form='ens',reading='abbreviation for ensemble; no full stop written',place='upper insertion and main line 17',observation='Both occurrences are short ens groups, not expanded ensemble. See scan003_figure_insertions.png.'),
 dict(form=r'M / \mathcal M',reading='set of multistrates; alphabet unresolved',place='main lines 17 and 20',observation='Two repeated bare curved capitals. The first is marked with both candidates, the second follows the first candidate. Do not promote H\'s calligraphic choice to certainty.'),
 dict(form=r'\leq',reading='less than or equal to',place='lower parenthetical insertion',observation='The less-than stroke and separate lower bar are both visible; par and ordonné are part of the same insertion.'),
 dict(form=r'\widetilde F',reading='F with tilde',place='main lines 18 and 24',observation='A separate wavy stroke is placed above the block F in both occurrences. No index or prime is present.'),
 dict(form=r'\mathrm{Mulomb}(F)',reading='grande multiombre',place='main lines 21 and 24',observation='The written operator has no t in either occurrence. The source itself supplies the phrase grande multiombre on line 21.'),
 dict(form=r'\mathrm{Omb}(F)',reading='grande ombre',place='main line 22 and continuation line 23',observation='The open final b resembles an angular hook; (F) is plainly written. The following prose supplies grande ombre.'),
]
hand_log=[
 dict(habit='An isolated small x can decide a word ending.',place='main line 14, lieux',observation='The terminal crossed x distinguishes lieux from H\'s figures; the apparent descending stroke nearby belongs to the diagonal note.'),
 dict(habit='Short abbreviations and common words use low extended connected humps.',place='both ens occurrences; body une and nous',observation='The abbreviation ens is much shorter than ensemble and has no written full stop. Both C doubts at ens are resolved from the crop.'),
 dict(habit='A looped l is followed directly by o in the operator Mulomb.',place='main lines 21 and 24',observation='Both occurrences show no t stroke. H inserts a t at both places; the repeated loop-and-o sequence confirms the local habit.'),
 dict(habit='Bare mathematical M is more rounded than the initial M of a written operator.',place='main lines 17/20 versus 21/24',observation='The distinction is visible, but does not by itself prove a distinct alphabet. The M/calligraphic M doubt is retained rather than standardized.'),
 dict(habit='Large horizontal and small diagonal writing intersect without cancelling one another.',place='main lines 9–15 and marginal note',observation='Crossing strokes must be assigned by baseline direction. In particular the main words question, simplicité and lieux remain live; the diagonal note is not a deletion of them.'),
]
notes=[
 dict(id='N003-01',claim='The page contains no display, diagram or drawing.',source='whole scan003 layout view and both halves',reasoning_if_any='The long curved strokes are insertion connectors; the oblique strokes are the marginal prose note.'),
 dict(id='N003-02',claim='The final source word is seulement, with no terminal punctuation visible.',source='scan003_reconstituer_deletion_support.png',reasoning_if_any='No completion of the unfinished sentence is supplied.'),
 dict(id='N003-03',claim='réconstituer is retained with the written accent.',source='scan003_reconstituer_deletion_support.png',reasoning_if_any='This is a transcription of the visible accent; no correction to usual spelling is made.'),
 dict(id='N003-04',claim='H\'s editorial marginal-note description is excluded from the transcription.',source='packets/scan003/H.tex and scan003_margin.png',reasoning_if_any='Its note is editorial markup, not ink. The actual note occupies eight diagonal baselines, not the editorial estimate of about fifteen.'),
 dict(id='N003-05',claim='The source has comme partie, without une.',source='scan003_figure_insertions.png',reasoning_if_any='The gap from comme to the next baseline contains no word; grammar does not supply one.'),
 dict(id='N003-06',claim='The two parenthetical insertions have different attachment points.',source='scan003_figure_insertions.png',reasoning_if_any='The upper connector descends before comme; the lower connector descends beside M. Their order is transcribed accordingly.'),
 dict(id='N003-07',claim='All 20 C doubt marks were reviewed; nine are resolved and eleven retained.',source='packets/scan003/C.tex; the eleven saved scan003 crops',reasoning_if_any='Resolved: contexte, donner, tend, étant, both ens occurrences, ordonné, par, l\'écrivons. Retained doubts are individually listed.'),
]

audit=[
 dict(C_span=r'\deleted{\unsure{sera}}',decision='Retain deleted state and C doubt.',place='margin line 6, before tend',evidence='scan003_margin.png: compact cancellation crosses the short preceding word only; tend lies to its right and remains live. The initial letters under the strike are not all plain.'),
 dict(C_span=r'\inserted{$F$}',decision='Retain inserted state and placement after figure.',place='main line 16',evidence='scan003_figure_insertions.png: F is above the baseline, and its separate stroke reaches the gap before est.'),
 dict(C_span=r"\inserted{(par l'\unsure{ens|ensemble} de ses ``strates'')}",decision='Retain insertion after interprétée; resolve ens, retaining no abbreviation point.',place='above main line 16',evidence='scan003_figure_insertions.png: the long lower connector bends into the gap immediately before comme; the inserted phrase has only ens, not ensemble.'),
 dict(C_span=r'\inserted{(\unsure{ordonné} \unsure{par|pour} $\leq$)}',decision='Retain insertion after M; resolve ordonné and par.',place='between main lines 16–17',evidence='scan003_figure_insertions.png: bracket descends beside M. The final e of ordonné bears an accent and has no second e. The sign has both < and its lower bar.'),
 dict(C_span=r'\inserted{ensembliste}',decision='Retain inserted state and placement after figure.',place='above main line 20',evidence='scan003_ensembliste_ecrivons.png: adjective is above the line, with a lower connector whose left end descends between figure and dans.'),
 dict(C_span=r'\deleted{\unsure{il|le}}',decision='Retain cancellation and both C candidates.',place='end of main line 25',evidence='scan003_reconstituer_deletion_support.png: short dark cancellation is separate from the live F and comma; diagnostic underlying letters remain obscured. The next-line mais is live.'),
]

rowmap={
36:('scan/manuscript/editorial page-marker syntax; manuscript 2 independently checked',[]),
37:('C alternative removed only after crop; genuine doubt-resolution review',['S003-01']),
38:('quotation glyph form, not a lexical difference',['S003-02']),
39:('quotation glyph form, not a lexical difference',['S003-02']),
40:('quotation glyph form, not a lexical difference',['S003-02']),
41:('quotation glyph form, not a lexical difference',['S003-02']),
42:('quotation glyph form, not a lexical difference',['S003-02']),
43:('quotation glyph form and H illegibility placeholder near same text',['S003-02','S003-03']),
44:('quotation form and H added dash',['S003-02','S003-03']),
45:('different words, missing words and unsupported dash; C confirmed',['S003-03']),
46:('word question readable where H has an illegibility placeholder',['S003-03']),
47:('substantial marginal text absent from H\'s fragmentary note',['S003-04']),
48:('marginal text and C doubts; plus real où/quand difference',['S003-04','S003-05','S003-06','S003-07','S003-25']),
49:('real word difference lieux/figures',['S003-08']),
50:('abbreviation, written point and C doubt',['S003-11']),
51:('quotation glyph form',['S003-02']),
52:('H adds une; absent in the ink',['S003-12']),
53:('real attachment/order difference, abbreviation point, and unresolved alphabet',['S003-13','S003-14','S003-17']),
54:('real ending difference ordonné/ordonnée',['S003-15']),
55:('C par/pour doubt resolved by crop',['S003-16']),
56:('real insertion attachment/order difference and alphabet/abbreviation issues',['S003-13','S003-14','S003-17']),
57:('C verb doubt plus real operator spelling difference',['S003-18','S003-19']),
58:('quotation glyph form',['S003-02']),
59:('quotation glyph form',['S003-02']),
60:('real word difference est/étant',['S003-20']),
61:('quotation glyph form',['S003-02']),
62:('quotation glyph form',['S003-02']),
63:('same written dash encoded as TeX hyphens versus Unicode dash; encoding only',[]),
64:('second real operator spelling difference',['S003-21']),
65:('real word ending difference permet/permettant',['S003-22']),
66:('real written-accent difference',['S003-23']),
67:('H omits cancelled ink; C doubt retained',['S003-24']),
68:('quotation marks belong around support',['S003-02']),
69:('H marginal fragment reviewed against source; its following editorial note excluded',['S003-04']),
}

def sb(n,kind,box,reading):
    return dict(box=f'scan003-b{n:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading)
second=[
 sb(1,'handwritten page number',[788,20,830,60],'2'),
 sb(2,'real differing word / resolved C doubt',[240,75,505,155],'contexte'),
 sb(3,'real differing phrase',[248,734,1662,1013],"(voire, la notion de lieu ponctuel ou point, dont il n'a pas encore été question...)"),
 sb(4,'entire marginal note, including all remaining marginal doubts',[15,645,1005,1845],"L'autre raison ... est une multistr.; see proposed TeX for all retained doubts"),
 sb(5,'marginal deletion',[28,1558,125,1672],r'\deleted{\unsure{sera}}'),
 sb(6,'real marginal word / resolved C doubt',[100,1320,280,1530],'donner'),
 sb(7,'real marginal word / resolved C doubt',[115,1450,220,1570],'tend'),
 sb(8,'real differing word',[260,1108,485,1205],'où'),
 sb(9,'real differing word',[390,1190,595,1310],'lieux'),
 sb(10,'resolved C doubt',[1380,1190,1550,1290],'étant'),
 sb(11,'insertion: whole variable and attachment',[650,1365,725,1445],'F after figure'),
 sb(12,'insertion: whole phrase and attachment',[950,1328,1475,1445],"(par l'ens de ses strates) before comme"),
 sb(13,'real absent word at line break',[270,1380,1455,1565],'comme partie; no une'),
 sb(14,'abbreviation and complete doubtful formula',[585,1475,860,1555],r"l'ens \unsure{M|\mathcal M}"),
 sb(15,'insertion: whole formula/phrase and attachment',[640,1408,1100,1525],'(ordonné par ≤), attached after M'),
 sb(16,'insertion: whole word and attachment',[620,1690,985,1790],'ensembliste after figure'),
 sb(17,'recurring doubtful alphabet: complete formula',[880,1735,990,1805],r'M (same unresolved alphabet as first occurrence)'),
 sb(18,'real verb alternatives / resolved C doubt',[1170,1718,1515,1800],"l'écrivons"),
 sb(19,'real operator spelling: complete formula',[280,1835,700,1915],r'\mathrm{Mulomb}(F)'),
 sb(20,'real differing word',[715,1910,830,1990],'est'),
 sb(21,'real operator spelling: complete formula',[880,2070,1240,2150],r'\mathrm{Mulomb}(F)'),
 sb(22,'real differing word',[1390,2060,1630,2150],'permet'),
 sb(23,'real written accent difference',[1035,2150,1395,2240],'réconstituer'),
 sb(24,'deletion',[1474,2160,1540,2230],r'\deleted{\unsure{il|le}}'),
 sb(25,'final quotation placement',[1010,2235,1270,2310],'double quotation marks around support'),
]

review=dict(scan=3,
 lines_read=dict(count=39,convention='Physical handwritten baselines counted by distinct inscription: 26 main-text lines (including the two-line opening continuation), 8 diagonal marginal-note lines, 4 independently placed insertion lines (F; par l\'ens...; ordonné par ≤; ensembliste), and the isolated page-number line 2. Deletions on existing baselines add no line. No inferred continuation is counted.',main_text=26,margin=8,insertions=4,page_number=1),
 changes=changes,doubts=doubts,inventory=inventory,notation=notation,hand_log=hand_log,notes=notes,
 check_events=[
  dict(action='Read allowed instructions and witnesses',details='Read packets/RULES.md, PREAMBLE.tex, NOTATION.md; scan003 C.tex, H.tex, differences.tsv and images.json only. No other scan, peer output or external source read.'),
  dict(action='Viewed whole original image once for layout',details='1697 × 2369 image: identified page number, two prose blocks, one diagonal marginal note, four insertions, two cancellations and one underline.'),
  dict(action='Viewed first full-resolution half once, line by line',details='Read all visible main and marginal strokes in the upper half against both witnesses; did not enlarge the whole half again.'),
  dict(action='Viewed second full-resolution half once, line by line',details='Read all visible main and marginal strokes in the lower half against both witnesses; overlap used only as part of that supplied half.'),
  dict(action='Audited all C deleted/inserted spans',details='Two deleted spans and four inserted spans checked for exact scope and attachment; all six are individually recorded in deletion_insertion_audit.'),
  dict(action='Created and personally inspected eleven original-image crops',details='Pillow crop, LANCZOS resize to 2800 px (margin initially 3000 px), autocontrast cutoff 0.4 and light unsharp mask. The marginal crop was rotated clockwise 45 degrees and its exterior rotation context trimmed for display while still undecided; it uses one original pixel box. Original boxes are in the crop manifest and changes.'),
  dict(action='Reviewed every C doubt',details='20 marks: nine resolved on named crops; eleven retained with individual evidence. Both doubts inside deleted text retained.'),
  dict(action='Reviewed all supplied raw-difference rows',details='Every source_row from 36 through 69 classified. Literal words, written punctuation and attachment differences retained; page-marker syntax, equivalent dash encoding and H editorial note handled separately.'),
  dict(action='Read every formula and numerical inscription',details='Whole M symbols read in both contexts; both F-tilde expressions, both Mulomb(F) occurrences, Omb(F), inserted F and ≤ inspected. Page numeral 2 is the only handwritten numerical inscription.'),
  dict(action='No recognition or compilation',details='No OCR, text-recognition model, external text, TeX compilation or final-page write was used.'),
 ],
 deletion_insertion_audit=audit,
 difference_review=[dict(source_row=k,classification=v[0],change_ids=v[1]) for k,v in rowmap.items()],
 second_boxes=second)
(root/'out/review/scan003_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote scan003_review.json: {len(changes)} change/review records, {len(doubts)} retained doubts, {len(second)} second-reading boxes; 34 raw rows classified.')
