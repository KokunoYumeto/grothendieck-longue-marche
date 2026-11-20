from pathlib import Path
import json
root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
p=json.loads((root/'reader_packets/143_scan028.json').read_text())
C,H=p['witness_C'],p['witness_H']
key='143_scan028'
tex=r'''\scanpage{28}
\mspage{14}
groupes fondamentaux sont \inserted{en apparence} triviaux :
\[
\pi_1(\mathcal T_{0\nu})=0\qquad 0\leq\nu\leq3
\]
Le Topos $\mathcal T_{0,\nu}$ \deleted{est le \inserted{gros} topos fibré} \inserted{$(\nu\geq4)$ correspond au} \deleted{étale de} \inserted{schéma} des syst. de $\nu-3$ points distincts $(x_1,\ldots,x_{\nu-3})$ dans
\[
\mathbf P^1-\{0,1,\infty\}=\mathbf E^1\setminus\{0,1\}.
\]
Son groupe fondamental est \inserted{le complété profini d'}un groupe de tresses $\Pi_{0,\nu}$, lequel (en tant que ``groupe extérieur'') dépend contra-fonctoriellement de $[1,\nu]$ pour les monomorphismes.

Sur $(\mathcal T_{0,\nu})_{\mathbf Q}$ \inserted{du $(\mathcal T_{\unsure{0\nu|0,\nu}})_{\overline{\mathbf Q}}$} on fait opérer $\mathfrak S_\nu$, donc $\mathfrak S_\nu\times\Gamma$ opère sur $\mathcal T_{0,\nu}$,
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\fill (0,0) circle (.08);
\fill (.85,.15) circle (.085);
\fill (1.75,.3) ellipse (.21 and .24);
\fill (1.05,-.27) circle (.018);
\fill (1.42,-.34) circle (.035);
\end{tikzpicture}}
\mspage{27}
'''
boxes={
 'bound-three':[1043,188,1250,274],
 'topos-type':[238,323,531,411],
 'first-correction':[827,272,1576,407],
 'punctured-line':[807,505,1587,597],
 'en-tant':[1295,739,1645,846],
 'interval-indices':[949,1005,1142,1109],
 'interlinear-du':[622,1138,1508,1328],
 'final-topos-index':[299,1462,531,1578]
}
def crop(name): return f'crops/{key}_readerC_{name}.png' if name else 'page'
changes=[]
def add(place,c,h,final,against_C,against_H,kind,ink,confidence='high',locus=None,marked=False,consequential=False):
 assert c=='[no witness]' or c in C,(place,'C',c)
 assert h=='[no witness]' or h in H,(place,'H',h)
 assert final in tex,(place,'final',final)
 changes.append(dict(place=place,C=c,H=h,final=final,against_C=against_C,against_H=against_H,kind=kind,ink=ink,confidence=confidence,crop=crop(locus),box=boxes.get(locus),marked_in_H=marked,consequential=consequential))

add('Opening line: addition above triviaux',r'\inserted{en apparence}',r'« \ill{} connue »',r'\inserted{en apparence}',False,True,
 'misread word','The addition is two words: a short en, followed by a-p-p-a-r-e-n-c-e with two descending p strokes and the extended low rence ending. It is written above triviaux and is not connue. H places its faulty reading in an editorial note rather than the main line.','high',None,True)
add('First display: index separator',r'\mathcal T_{0\nu}',r'\mathcal{T}_{0,\nu}',r'\mathcal T_{0\nu}',False,True,
 'text not on the page','The round zero and following nu stand next to each other in the first display without a separate comma stroke. This differs from the visibly comma-bearing indices elsewhere on the sheet.')
add('First display: comma after the zero value',r')=0\qquad',r') = 0, \qquad',r')=0\qquad',False,True,
 'text not on the page','After the right-hand zero there is blank space before the separate range condition; no comma is written.')
add('First display: terminal period after 3',r'0\leq\nu\leq3',r'0 \leqslant \nu \leqslant 3 .',r'0\leq\nu\leq3',False,True,
 'text not on the page','The final numeral is a heavily retraced 3 with two rightward curved lobes. There is no terminal dot after it; the two inequalities each have a separate lower bar.','high','bound-three')
add('Description opening: Topos',r'Le Topos',r'Le Type',r'Le Topos',False,True,
 'misread word','After the capital T are a low rounded o, a single deep p descender, and the compressed o-s ending. There is no second descender that would support the y-p sequence of Type.','high','topos-type')
add('Canceled description: est rather than arrow',r'\deleted{est le',r'\struck{$\to$ le',r'\deleted{est le',False,True,
 'misread word','Beneath the horizontal cancellation are the compact e-s strokes and a taller terminal t, followed by the separately visible le. The crossing stroke makes the canceled word look arrow-like; it is not a freestanding arrow.','medium','first-correction')
add('Canceled description: interlinear gros',r'\inserted{\unsure{gros}}',r'le topos \ill{}',r'\inserted{gros}',False,True,
 'omission','Above topos, the small added word has a looped g with a descender, r shoulder, rounded o and terminal s return. It belongs to the canceled wording and is retained inside the deletion. H supplies no corresponding gros.','high','first-correction')
add('Canceled description: fibré',r'topos fibré',r'topos \ill{}',r'topos fibré',False,True,
 'readable ink left as \\ill{}','After topos, the large f descender, dotted i, tall looped b, short r and accented e survive the cancellation strokes.','high','first-correction',True)
add('Replacement above canceled description',r'\inserted{$(\nu\geq4)$ correspond au}',r'($\nu \geqslant 4$) correspond au',r'\inserted{$(\nu\geq4)$ correspond au}',False,True,
 'insertion or placement','The parenthesised nu-greater-or-equal-4 and correspond au are written on the line above the canceled est le ... topos fibré. They are live replacement writing, not baseline prose.','high','first-correction')
add('Next line: schéma replacing étale de',r'\deleted{étale de} \inserted{schéma}',r'schéma \struck{étale de}',r'\deleted{étale de} \inserted{schéma}',False,True,
 'insertion or placement','The words étale de are crossed by a dark horizontal line; schéma is placed just above them as their replacement. The deletion and addition are separately represented in the candidate.')
add('Punctured-line display: first subtraction sign',r'\mathbf P^1-\{0,1,\infty\}',r'\mathbb{P}^1 \smallsetminus \{0, 1, \infty\}',r'\mathbf P^1-\{0,1,\infty\}',False,True,
 'misread symbol or index','The stroke after P superscript 1 is short and horizontal. The separate stroke after E superscript 1 descends diagonally. Their different forms are retained rather than making both set-minus diagonals.','high','punctured-line')
add('Fundamental-group paragraph: profinite-completion addition',r"\inserted{le complété profini d'}un",r"le complété profini d'un",r"\inserted{le complété profini d'}un",False,True,
 'insertion or placement','Le complété profini d\' is written above the main line between est and un groupe, with a curved linking stroke descending toward un. The apostrophe ends the added text, and the original un remains on the baseline.')
add('Parenthesis after lequel: en tant que',r'lequel (\unsure{en tant} que',r'lequel (« groupe',r'lequel (en tant que',False,True,
 'omission','The parenthetical beginning has a low en run followed by a tall crossed first t and a compressed ant ending with a final t return. Que begins the next manuscript line before the quotation. H omits these words.','medium','en-tant')
add('Quotation marks around groupe extérieur',r"``groupe extérieur''",r'« groupe \ill{} »',r"``groupe extérieur''",False,True,
 'other','Two separate high quote ticks appear before groupe and another pair after extérieur. They are double quotation marks, not angle-shaped guillemets.')
add('Quoted group description: extérieur','extérieur',r'groupe \ill{}','extérieur',False,True,
 'readable ink left as \\ill{}','The word shows initial e-x, a tall t with accent above the following e, then the low r-i-e-u-r run before the closing quote pair.','high',None,True)
add('Final paragraph: complete interlinear addition and attachment',
 r'on \inserted{\unsure{du|donc}} fait opérer \inserted{$(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}$}',
 r'du $(\mathcal{T}_{0,\nu})_{\overline{\mathbb{Q}}}$'+'\n'+r'on fait opérer',
 r'\inserted{du $(\mathcal T_{\unsure{0\nu|0,\nu}})_{\overline{\mathbf Q}}$} on fait opérer',True,False,
 'insertion or placement','Du begins above the gap after the baseline Q and before on. The barred-Q topos expression continues that interlinear addition above fait. The candidate keeps the whole addition together before on fait opérer, matching H\'s order rather than splitting it around on/fait opérer as C does. No explicit caret is present; the attachment follows the written interlinear run.','medium','interlinear-du')
add('Interlinear topos expression: tiny index separator',r'(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}',r'(\mathcal{T}_{0,\nu})_{\overline{\mathbb{Q}}}',r'(\mathcal T_{\unsure{0\nu|0,\nu}})_{\overline{\mathbf Q}}',True,True,
 'misread symbol or index','The round zero and nu are visible, but a separate comma between them cannot be isolated as securely as in the baseline and final indices. The leading visual reading is 0 nu without a separate comma; 0,nu remains possible because the tiny left stroke of nu may adjoin a comma.','medium','interlinear-du')
figure=C[C.index(r'\figure{'):C.index(r'\mspage{27}')].rstrip()
assert figure in tex
add('Below final paragraph: five black marks',figure,'le reste de la page est blanc',figure,False,True,
 'drawing or diagram','There are five opaque black marks: two small circles rising slightly left-to-right, a substantially larger oval farther right and above, and two tiny lower dots. The candidate preserves C\'s relative positions and sizes. No mathematical interpretation or authorship is assigned to them.')
add('Heading appended by H but absent from this sheet','[no witness]',r'\section*{Une conjecture arithmético-géométrique}','',False,True,
 'text not on the page','The entire lower sheet was inspected. It contains the five black marks, blank paper and the lower pencil numeral; there is no conjecture heading, underline or circled 9 on this page. The H heading is therefore omitted without assigning it to another uninspected sheet.')
add('Bottom-left pencil numeral',r'\mspage{27}','[no witness]',r'\mspage{27}',False,True,
 'omission','A light pencil 2 followed by a long diagonal-topped 7 appears at the bottom left. The numeral is transcribed with its hand left unnamed.')

report={
 'key':key,'reader':'C','stage':'first','image_views':['original','half1','half2'],
 'changes':changes,
 'decisions':[
  dict(id='M0714',decision='first',reading='en tant',ink='Following the opening parenthesis, the low en run ends before a taller crossed t. A compressed a-n run and final t return follow. These strokes support en tant; que is written at the beginning of the next line.',crop=crop('en-tant'),box=boxes['en-tant'],confidence='medium'),
  dict(id='M0715',decision='first',reading='du',ink='The first letter has a small closed lower bowl and a high looped ascender, followed by a single flattened u return. It is du, with no o-n-c sequence to support donc. Its attachment is handled separately in the placement row.',crop=crop('interlinear-du'),box=boxes['interlinear-du'],confidence='high')
 ],
 'inventory':[
  dict(sheet_kind='text',hand='unnamed hand',element='E01',kind='margin note',position='Top-right pencil numeral',first_words_or_objects='14',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E02',kind='text',position='Opening continuation at top',first_words_or_objects='groupes fondamentaux sont',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E03',kind='insertion',position='Above triviaux at upper right',first_words_or_objects='en apparence',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E04',kind='display',position='Below opening line',first_words_or_objects=r'\pi_1(\mathcal T_{0\nu})=0',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E05',kind='text',position='Description beginning Le Topos, before punctured-line display',first_words_or_objects=r'Le Topos $\mathcal T_{0,\nu}$',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E06',kind='deletion',position='First description line, after the topos symbol',first_words_or_objects='est le ... topos fibré',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E07',kind='insertion',position='Above topos, within the canceled description',first_words_or_objects='gros; included in the deletion',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E08',kind='insertion',position='Above the first canceled description',first_words_or_objects=r'$(\nu\geq4)$ correspond au',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E09',kind='deletion',position='Start of next description line',first_words_or_objects='étale de',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E10',kind='insertion',position='Above canceled étale de',first_words_or_objects='schéma',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E11',kind='display',position='Punctured-line equality after dans',first_words_or_objects=r'\mathbf P^1-\{0,1,\infty\}=\mathbf E^1\setminus\{0,1\}',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E12',kind='text',position='Central paragraph through monomorphismes',first_words_or_objects='Son groupe fondamental est',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E13',kind='insertion',position='Above est un groupe in the fundamental-group paragraph',first_words_or_objects="le complété profini d'",transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E14',kind='text',position='Final three-line action paragraph',first_words_or_objects=r'Sur $(\mathcal T_{0,\nu})_{\mathbf Q}$',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E15',kind='insertion',position='Interlinear run above on fait, beginning after the baseline rational-field expression',first_words_or_objects=r'du $(\mathcal T_{\unsure{0\nu|0,\nu}})_{\overline{\mathbf Q}}$',transcribed='yes'),
  dict(sheet_kind='text',hand='unnamed hand',element='E16',kind='drawing',position='Below and partly alongside the final action paragraph',first_words_or_objects='Five opaque black marks: three upper circles/oval and two lower dots',transcribed='yes'),
  dict(sheet_kind='text',hand='unnamed hand',element='E17',kind='margin note',position='Bottom-left pencil numeral',first_words_or_objects='27',transcribed='yes')
 ],
 'remaining_doubts':[
  dict(place='Interlinear barred-Q topos expression: index punctuation',reading=r'\mathcal T_{\unsure{0\nu|0,\nu}}',alternatives=r'\mathcal T_{0\nu} / \mathcal T_{0,\nu}',confidence='medium',reason='The zero and nu are readable but the tiny possible comma is not securely separable from the left stroke of nu. The first display lacks a comma, while the baseline and final indices have one; those local forms are not used to force this occurrence. See crops/143_scan028_readerC_interlinear-du.png.')
 ],
 'certainty_resolutions':[
  dict(place='Inserted word inside canceled description; not an original packet MARK',C=r'\unsure{gros}',final='gros',ink='The g loop/descender, r shoulder, o loop and s return survive above topos within the correction.'),
  dict(place='M0714',C=r'\unsure{en tant}',final='en tant',ink='The low en run and two t-bearing parts are visible; reading retained with medium confidence.'),
  dict(place='M0715',C=r'\unsure{du|donc}',final='du',ink='A looped tall d is followed by a single u return; no donc-length sequence is present.'),
  dict(place='Tresses: H uncertainty only',C='tresses',final='tresses',ink='The initial t cross stroke, r/e run and repeated s forms are visible. C already reads tresses; H marks the same word uncertain.')
 ],
 'notation':[
  dict(form=r'\mathcal T',meaning='The distinct topos notation on this page, retained from both witnesses',evidence='All five occurrences have a flag-like upper part and curved lower return. The similar shape does not identify this notation with the earlier object-set tau/T. Both witnesses call it mathcal T; no font-only disagreement is manufactured.'),
  dict(form=r'\mathcal T_{0\nu}',meaning='Topos in the initial fundamental-group display',evidence='The first index is written without a separate comma; later comma-bearing occurrences were inspected independently.'),
  dict(form=r'\mathbf P^1-\{0,1,\infty\}=\mathbf E^1\setminus\{0,1\}',meaning='Literal punctured-line expression',evidence='P and E both have doubled left strokes; the right-hand letter is plainly E, not A. Bold encoding follows C\'s field-letter convention. The first difference stroke is horizontal and the second diagonal.'),
  dict(form=r'\Pi_{0,\nu}',meaning='Braid-group notation in the source paragraph',evidence='Capital Pi has two upright legs and a shared top bar; it is distinct from the smaller fundamental-group pi in the first display.'),
  dict(form=r'[1,\nu]',meaning='Interval indexing the stated contravariance',evidence='The left 1 has a rising head and base stroke despite retracing; the right nu has a low left arm and taller curved right arm. Square brackets and comma are visible.'),
  dict(form=r'\mathfrak S_\nu\times\Gamma',meaning='Product action notation in the final paragraph',evidence='The two S graphs have spiral-like open left curves and lower nu labels; the product sign and capped Gamma are present.'),
  dict(form=r'\overline{\mathbf Q}',meaning='Barred rational-field letter in the interlinear expression',evidence='A separate horizontal bar appears directly above the Q. It belongs to the inserted expression rather than the baseline field label.')
 ],
 'abbreviations':[
  dict(form='syst.',expansion='systèmes')
 ],
 'hand_log':[
  dict(habit='A compact Topos can resemble Type when its low o-s ending is compressed.',places='Opening of the description, scan028.',scope='The single capitalized word was cropped; the lower canceled topos was also inspected.',misreadings='H Type; source has only the p descender, with low rounded strokes before and after it.'),
  dict(habit='A cancellation can turn a short word into an arrow-like shape.',places='Canceled est after the topos expression.',scope='Single local occurrence, checked with the complete correction block.',misreadings='H reads an arrow where compact e-s and terminal t lie beneath the cancellation.'),
  dict(habit='Added wording may occupy two interlinear levels while forming one continuous addition.',places='du plus the barred-Q topos expression over on fait.',scope='The complete added run and baseline were inspected in one crop.',misreadings='C splits the two parts around on and fait opérer; H keeps the run together before on.'),
  dict(habit='The topos graph has a flag-like top and curved lower return, but shape alone does not identify its mathematical alphabet.',places='Five topos occurrences across the page.',scope='All occurrences inspected, following main reader\'s instruction to keep this notation distinct from the earlier object set.',misreadings='No material font row: both witnesses use mathcal T.'),
  dict(habit='Commas in indices may be absent, isolated, or close to the left arm of nu.',places='First display, description, final-paragraph baseline, interlinear expression, and final topos index.',scope='All five topos indices inspected; the tiny separator in the interlinear expression remains uncertain.',misreadings='H adds a comma in the first display; both witnesses give a comma in the interlinear expression that is not securely separable in the image.'),
  dict(habit='The final 3 and some later index symbols are strongly retraced.',places='Upper bound 3, interval [1,nu], and heavy nu forms near the bottom.',scope='The upper bound and interval were separately cropped; final readings are retained.',misreadings='H claims a different earlier digit under 3, but the crop does not identify one securely. No canceled numeral is invented.'),
  dict(habit='Doubled left strokes occur in the geometric P and E letters.',places='Punctured-line equality.',scope='Both letters inspected together.',misreadings='The E is retained literally; it is neither normalized to A nor treated as the unrelated provisional E/Sigma action-group letter.'),
  dict(habit='Quote pairs are drawn as high ticks.',places='Before groupe and after extérieur.',scope='Both ends of the quotation inspected.',misreadings='H renders guillemets, while C\'s double-quote convention matches the ticks.')
 ],
 'notes':[
  dict(id='143_scan028-N1',text='The opening continuation says the fundamental groups are “en apparence” trivial and displays pi_1 of the indicated topos as zero for 0 <= nu <= 3. En apparence is an addition above triviaux. The upper bound is a heavily retraced 3; the image does not securely recover a separate earlier numeral, so none is supplied. This account does not prove the displayed assertion.'),
  dict(id='143_scan028-N2',text='The corrected description says the topos for nu >= 4 corresponds to the scheme of systems of nu-3 distinct points in the displayed punctured line. The canceled est le gros topos fibré and étale de are retained, together with the interlinear additions. The right-hand geometric letter in the display is E with a doubled left stroke, and is reproduced as E rather than replaced by a mathematically expected letter.'),
  dict(id='143_scan028-N3',text='The author adds that the fundamental group is the profinite completion of a braid group, then says that this group, “en tant que” a “groupe extérieur”, depends contravariantly on the indicated interval for monomorphisms. En tant que and extérieur are source words omitted or left unread in H. No braid-group presentation or functoriality claim has been proved in this reading.'),
  dict(id='143_scan028-N4',text='The final paragraph describes the symmetric-group action and the product action with Gamma. The interlinear word is du, not donc; the unusual wording is left unchanged. Du and the barred-Q topos expression are kept as one addition before on fait opérer, following their continuous interlinear placement and H\'s order. The tiny comma in that inserted index remains genuinely uncertain, and the paragraph ends with the source comma.'),
  dict(id='143_scan028-N5',text='Five opaque black marks below the final paragraph are reproduced as physical shapes, without asserting that they form an intentional mathematical drawing or that they are in the author\'s hand. The pencil numerals 14 and 27 are assigned to an unnamed hand. H\'s appended conjecture heading, underline and reported circled 9 are absent from this sheet; no other sheet was consulted to relocate them.'),
  dict(id='143_scan028-N6',text='All five topos letters retain the shared C/H mathcal T encoding. Their shape resembles the round object-set glyph encountered in the shared notation table, but the distinct topos notation is not conflated with it. Bold versus blackboard font choices for the field/geometric letters are treated as renderings of the same visible double-stroke convention, not new mathematical symbols.')
 ],
 'check_events':[
  dict(statement_id='143_scan028-triviality',type='carried as background without fault found',outcome='Not proved. The zero fundamental-group display, both inequalities, and final 3 were read from the image. No expected range was used to invent an earlier overwritten numeral.'),
  dict(statement_id='143_scan028-geometric-description',type='carried as background without fault found',outcome='Not proved. The corrected scheme description, nu-3 indices and punctured-line expression were visually checked. The literal E was not changed from a presumed geometric identification.'),
  dict(statement_id='143_scan028-braid-functoriality',type='carried as background without fault found',outcome='Not proved. The completion addition, braid-group name, exterior-group parenthesis and interval [1,nu] were transcribed without proving their asserted functoriality.'),
  dict(statement_id='143_scan028-actions',type='carried as background without fault found',outcome='Not proved. The two symmetric-group labels, Gamma, the product sign, and the barred-Q addition were checked as source notation. Insertion placement was based on the writing, not on correcting the sentence mathematically.')
 ],
 'unresolved_for_main':[
  'Tiny index separator in the interlinear barred-Q topos: candidate has mathcal T_{unsure{0nu|0,nu}}. See crops/143_scan028_readerC_interlinear-du.png.',
  'Review the adopted attachment of the complete du plus barred-Q expression before on fait opérer; the handwriting supplies a continuous interlinear run but no explicit caret. Same crop.',
  'The upper bound is securely 3, but H\'s alleged earlier digit cannot be independently identified. See crops/143_scan028_readerC_bound-three.png; candidate supplies no deleted numeral.',
  'Five black marks are faithfully retained as shapes; their provenance and purpose are not established. No mathematical drawing interpretation is asserted.'
 ],
 'raw_difference_disposition':'All 28 packet differences were checked against the original and both existing native halves, including every agreed source word, formula, index, quote mark, cancellation, insertion and numeral. Differences 1–2 are scan/page-note formatting; the visible pencil 14 is retained. Difference 3 concerns en apparence and is covered with H\'s incorrect known-word note in difference 9. Differences 4–5 and 8 are real punctuation differences; 6–7 and 11 are leq/leqslant or geq/geqslant macro choices, with both lower bars verified in the ink. Differences 9–13 concern Topos and the layered corrected description and are covered by separate word/state rows. Difference 14 is the horizontal subtraction sign. Difference 15 is H\'s editorial note about double-stroked E; the source E is retained, and C-style bold versus H blackboard fonts are treated as rendering conventions. Difference 16 is the macro boundary at d\' plus un, not a changed word; its insertion state is recorded separately. Differences 17–18 are the missing en tant que, quote forms and extérieur. Differences 19–21 concern the complete interlinear du-expression placement. Differences 22–28 are contaminated by comparison of C\'s figure code with H\'s editorial note and appended heading; the five physical marks, absent heading and bottom numeral are explicitly accounted for. No circled 9 or conjecture title appears on this sheet. All eight unique crops were emitted and inspected; no OCR, web research, TeX compilation or audit of other pages was performed.'
}
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert [x['id'] for x in report['decisions']]==[x['id'] for x in p['marks']]
assert len(p['differences'])==28
for row in changes:
 assert row['kind'] in allowed,row['kind']
 if row['crop']!='page': assert (work/row['crop']).exists()
for row in report['decisions']: assert row['reading'] in tex
for name in boxes: assert (work/crop(name)).exists()
(work/'reviews'/f'{key}_readerC.tex').write_text(tex)
(work/'reviews'/f'{key}_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate':str(work/'reviews'/f'{key}_readerC.tex'),'report':str(work/'reviews'/f'{key}_readerC.json'),'changes':len(changes),'decisions':len(report['decisions']),'inventory':len(report['inventory']),'crops':len(boxes)},indent=2))
