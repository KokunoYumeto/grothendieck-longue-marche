from pathlib import Path
import json

root=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads((root/'work/reader_c_scan012_boxes.json').read_text())
field=r'\overline{\unsure{\deleted{\mathbb Q}K|\deleted{K}\mathbb Q}}'
first_formula=r'\pi_1(U_i(\underset{\unsure{\mathbb Q|k}}{\mathbb C}),\bar\eta)'
margin=r"Cette interprétation n'est évidemment pas particulière au corps de base $\mathbb Q$ --- elle vaut \unsure{pour|pr} tte ext. de corps $K/K_0$"
display=r'''\begin{aligned}
(13)\qquad \pi_{\bar K/K}&\simeq\varprojlim_i\underbrace{\pi_1(\bar U_i,\bar\eta)}_{\pi_i}\\
&\simeq\varprojlim_i\pi_1(U_i(\mathbb C),\bar\eta)^{\wedge}
\end{aligned}'''
tex=r'''\scanpage{12}
sont des groupes fondamentaux ``géométriques'' --- \unsure{qui|que} peuvent d'ailleurs se calculer par voie transcendante, en utilisant un plongement de $FIELD$ dans $\mathbb C$ (d'où un isom $\overline{\mathbb Q}\simeq\overline{\mathbb Q}_0$), comme les complétés profinis des $FIRSTFORMULA$, \unsure{en|où} maintenant $\bar\eta$ est interprété comme un pt \deleted{complexe} commun des espaces top. sous-jacents aux variétés complexes $U_i(\mathbb C)$.

La suite exacte (8) est donc la limite projective des suites exactes d'homotopie (12), ce qui donne en particulier
\[
DISPLAY
\]
\margin{MARGIN}

Utilisant les fibrations des $U_i$ (dans le cas où on s'astreint à prendre des variétés élémentaires d'Artin), on trouve que tout $\pi_i$ est un groupe \deleted{\unsure{par|pr}} extension successive de \inserted{$n$} groupes profinis \uline{libres} (ici $n=\dim U_i=\operatorname{deg.tr.}K/\mathbb Q$). Ceci redonne
\margin{11}
'''.replace('FIELD',field).replace('FIRSTFORMULA',first_formula).replace('DISPLAY',display).replace('MARGIN',margin)
(root/'edition/reviews/149_scan012.tex').write_text(tex,encoding='utf-8')

def crop(n): return f'crops/149_scan012_{n}.png'
def change(id,place,C,H,final,evidence,crop_id,confidence,against_C,against_H,kind,error_category,marked_in_H=False,mathematical=False):
    return dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=crop(crop_id),box=boxes[crop_id],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical)
changes=[
 change('c01','L1, quotation marks around géométriques',"``géométriques''",'« géométriques »',"``géométriques''",'Each side has two short elevated strokes. Neither side has the paired angle strokes of a guillemet. The word and its accent marks are present; the marks are retained in C’s double-quote convention. The different dash lengths in the witnesses are rendering, not a separate reading.','c01','high',False,True,'other','Other'),
 change('c02','L4, field after plongement de',r'\overline{\mathbb Q}',r'\overline K',field,'Under one overbar a complete oval with a lower right tail is crossed by a left upright and two K-like diagonals. A doubled inner stroke also survives. The darker stem and diagonals favor Q beneath K, but the temporal order cannot be established securely from the intersections; the reverse order remains explicitly available. Neither a bare Q nor a bare K accounts for all the ink.','c03','low',True,True,'deletion state','Struck text',mathematical=True),
 change('c03','L6, whole first fundamental-group expression',r'\pi_1(\unsure{U_i(\underset{k}{\mathbb C})|U_i(\mathbb C)},\bar\eta)',r'\pi_1(U_i(\mathbb C),\bar\eta)',first_formula,'The whole expression shows pi with low 1, U with dotted low i, an upper doubled C, the lower extra glyph, the comma and barred eta, and the closing parentheses. The lower glyph is real: it has an oval or loop, an inner upright, and a curled rightward foot. This favors a Q-like form over k, but its letter remains doubtful. No distinct strike or insertion leader establishes a correction sequence; only the vertical position is encoded.','c04','low',True,True,'misread symbol or index','Symbols and indices',mathematical=True),
 change('c04','L6, word immediately before maintenant',r'\unsure{où|en}','en',r'\unsure{en|où}','The small initial form is open or looped, followed by a shoulder and a low terminal run. No clear accent is visible. These strokes favor en slightly, but do not exclude the compressed où reading. The alternatives remain explicit; no grammatical emendation is made.','c05','low',True,False,'misread word','Words'),
 change('c05','L6, between en/où and maintenant','(nothing)','interprétant','(nothing)','After the short en/où form the next visible word starts the m-a-i-n-t sequence of maintenant; the i dot and the tall t are present. There is no intervening word or insertion leader. H’s interprétant before maintenant is not on the page.','c05','high',False,True,'text not on the page','Text that is not on the page'),
 change('c06','L7, immediately after barred eta','est interprété','(nothing)','est interprété','After eta the short est has a low e-s run and terminal t. The next word has the initial i, n run, tall t, descending p, r, second t and terminal accented e of interprété. These are live words following eta and preceding comme.','c06','high',False,True,'omission','Omissions'),
 change('c07','L12, reference immediately after homotopie','(12)','(12) within the marginal note','(12)','The parenthesized digits stand on the horizontal body-text line before the comma and ce qui donne en particulier. The first digit is one upright; the second has the curved top and lower turn of 2. The diagonal note’s baselines pass separately to the left.','c08','high',False,True,'insertion or placement','Insertions put in the wrong place',mathematical=True),
 change('c08','L13, number at the left of the two-row display','(13)','(13) within the marginal note','(13)','The parenthesized number aligns with the first row of the display. The final digit has two rightward lobes, hence 3. It is not a word or reference written along the diagonal note. The full display also confirms both low 1 indices, both limit arrows and both wave-over-bar relation signs.','c09','high',False,True,'insertion or placement','Insertions put in the wrong place',mathematical=True),
 change('c09','Left diagonal note beside (12) and (13), wording through de corps',r"Cette interprétation n'est évidemment pas particulière au corps de base $\mathbb Q$ --- elle vaut \unsure{pour|pr} tte ext. de corps",r'Cette interprétation \ill{} (12) \ill{} en particulier \ill{} (13) \ill{} ext. \ill{}',r"Cette interprétation n'est évidemment pas particulière au corps de base $\mathbb Q$ --- elle vaut \unsure{pour|pr} tte ext. de corps",'On rotating the note clockwise, seven separate diagonal rows can be followed. In n’est évidemment the apostrophe and tall d are visible; particulière has its p descender and tall t; corps has the descending p; base has its b stem; elle has two tall l strokes; vaut has its initial low v and terminal t; tte has two tall t strokes; ext. has its crossing x and stop; de corps is present on that same note row. The short pour/pr form is not fully resolved. H has drawn the horizontal (12), en particulier, and (13) into the note; the note itself contains no such sequence.','c10','medium',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked_in_H=True,mathematical=True),
 change('c10','Final row of the diagonal note',r'K/K_0',r'K/k_0',r'K/K_0','Both letters have a tall upright and two diagonals. The second is visibly capital K, followed by a separate closed low oval 0. The separator between the two letters is long and nearly upright; it is rendered as the slash used in both witnesses.','c10','high',False,True,'misread symbol or index','Symbols and indices',mathematical=True),
 change('c11','L18, cancelled word between groupe and extension',r'\deleted{\unsure{par}}',r'\struck{pr}',r'\deleted{\unsure{par|pr}}','A long p descender survives the cancellation and a small r-like final return is visible. The dense overlapping strokes in the middle allow a small a loop but do not isolate it securely. The word is certainly struck; every letter is not plain, so par/pr remains open.','c11','low',False,True,'misread word','Struck text'),
 change('c12','L20, first word inside the final parenthesis','ici','où','ici','The first short stem has a separate dot. A low c-like turn and a compressed terminal return follow it. This supports ici; there is no initial closed oval supporting H’s o. The middle and last strokes are compressed, so confidence is medium rather than high.','c13','medium',False,True,'misread word','Words'),
 change('c13','Lower left edge, thin small foliation',r'\margin{11}','(nothing)',r'\margin{11}','Two separate thin numerals each have an oblique entry and a tall near-vertical stem. Both are 1. Their small scale and thinner, paler pen differ from the body hand; this is recorded as marginal foliation rather than an author page header.','c14','high',False,True,'omission','Omissions')
]

decisions=[
 dict(id='M0978',decision='undecided',reading=r'\unsure{qui|que}',evidence='The q loop and descender are clear, followed by a low u and a long terminal run ending in a short upturn. Neither a separate i dot nor a decisive e loop is present. The crop does not resolve the last letter.',crop=crop('c02'),box=boxes['c02'],confidence='low'),
 dict(id='M0979',decision='other',reading=r'U_i(\underset{\unsure{\mathbb Q|k}}{\mathbb C})',evidence='The lower glyph beneath C is physically present, so the no-glyph alternative is not retained. Its loop, upright, and curled foot favor a Q-like reading, while k remains an alternative. The complete pi_1 formula was inspected. No correction order or mathematical role is supplied.',crop=crop('c04'),box=boxes['c04'],confidence='low'),
 dict(id='M0980',decision='undecided',reading=r'\unsure{en|où}',evidence='The open initial shape and following shoulder favor en, and no clear accent appears; the compressed strokes still do not exclude où. The uncertainty is retained with the more visually supported reading first. The following source words remain maintenant eta est interprété.',crop=crop('c05'),box=boxes['c05'],confidence='low'),
 dict(id='M0981',decision='undecided',reading=r'\unsure{pour|pr}',evidence='In the rotated note a p descender and r-like terminal stroke are visible, but the intervening low run does not securely separate o and u or establish their absence. Neither the full word nor the abbreviation is certain.',crop=crop('c10'),box=boxes['c10'],confidence='low')
]

def inv(element,kind,position,first,hand='principal handwritten text'):
    return dict(scan=12,sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inventory=[
 inv('p01','text','Main body, L1–L9; upper part of the leaf','sont des groupes fondamentaux'),
 inv('d01','deletion','L4, overlapped field letters below one overbar',field),
 inv('d02','deletion','L8, before commun',r'\deleted{complexe}'),
 inv('p02','text','Main body, L10–L12, above (13)','La suite exacte (8)'),
 inv('f01','display','Main body, L13–L14, with underbrace label on its own lower level',r'(13)\quad\pi_{\bar K/K}\simeq\varprojlim_i\underbrace{\pi_1(\bar U_i,\bar\eta)}_{\pi_i}'),
 inv('m01','margin note','Lower left, seven slanted rows beside (12) and (13)','Cette interprétation'),
 inv('p03','text','Main body, L15–L20, below (13)','Utilisant les fibrations des'),
 inv('d03','deletion','L18, between groupe and extension',r'\deleted{\unsure{par|pr}}'),
 inv('i01','insertion','Above L19; V-shaped leader ends between de and groupes',r'\inserted{$n$}'),
 inv('n01','text','Extreme lower left, separate foliation','11','thin smaller foliation hand')
]

notes=[
 'Reader: GPT-6 Astra Pro; effort is not exposed; run SP84_C13_149. The full page and both supplied halves were personally read once. Existing saved crops were used for all disputed words, symbols and states. No OCR, external research or TeX compilation was used.',
 'Line count 30: twenty main rows including the two display rows, seven rows of the diagonal note, one raised n row, one underbrace-label row, and one foliation row. The main rows are numbered L1–L20 in this report; the underbrace label and raised n are additional inspected physical rows.',
 'S012.1 (L1–L9): The manuscript describes geometric fundamental groups and states a transcendental reading using an embedding into C and profinite completions of topological fundamental groups. This is a transcription summary, not a proof check. The field letters in L4 overlap; the lower letter beneath C in L6 remains doubtful and is preserved without completing the intended mathematics.',
 'S012.2 (L10–L14): The manuscript says exact sequence (8) is the projective limit of the homotopy sequences (12), then writes the two identities labeled (13). The lower note says this interpretation also applies to a general field extension K/K_0. The numbers (12) and (13) belong to horizontal body text and display, not to the note.',
 'S012.3 (L15–L20): The manuscript invokes Artin elementary-variety fibrations and states that each pi_i is a successive extension of n free profinite groups, with n = dim U_i = deg.tr. K/Q. This assertion was read, not independently verified. The page ends at Ceci redonne.',
 'The lower text is darker than the upper writing. The raised n is connected by a V-shaped leader whose point falls between de and groupes; it is not a deletion stroke. The low glyph beneath C in the first pi_1 expression has no comparably clear leader or strike, so no insertion or deletion state is inferred for it.',
 'The word complexe has one horizontal cancellation across its letters; commun to its right is live. The later par/pr is also cancelled, but its interior letters are obscured. The field overlap is separately encoded with uncertainty about the order of the two letters.',
 'The short word before maintenant remains en/où. The physically present continuation is eta est interprété comme; H’s en interprétant maintenant eta comme is not adopted. Any awkwardness in the resulting source wording is retained.',
 'Crops c02, c07, c12, c15 and c16 supplement the change rows: c02 documents unresolved qui/que; c07 confirms the complexe deletion; c12 confirms the n insertion and its attachment; c15 confirms the isomorphism with low zero; c16 confirms reference (8). All c01–c16 were personally inspected. c10 alone is rotated clockwise 38 degrees; its box remains in original page coordinates.',
 'No title, date or author page number is visible. The thin smaller 11 at the lower left is a separate foliation hand and is retained with margin, not mspage.',
 'Audit box b12 is intended to read the diagonal note. The unavoidable neighboring horizontal (12) and (13) lie in the rectangular region but are assigned their own body-text/display boxes. Audit kind labels are neutral. All pen numerals are covered: the 0 in Qbar_0, the 1 indices in the three pi_1 expressions, (8), (12), (13), the 0 in marginal K_0, and foliation 11.'
]
hand=[
 dict(habit='Long low terminal runs compress several letters and can conceal a final vowel or i.',pages=[12],consistency='Visible in qui/que, the diagonal pour/pr, and ici. The crop does not resolve every instance; no general rule is asserted.',misread='H prints qui without doubt; H’s où in the final parenthesis is not supported by the dotted first stem. The unresolved qui/que and pour/pr remain marked.'),
 dict(habit='Capital K has a tall stem with two diagonals; Q and C have an added inner stroke.',pages=[12],consistency='Clear in the final K/Q expression, the note K/K_0, the isomorphism with Qbar_0 and the doubled C symbols. The overlapping L4 field and lower L6 glyph remain exceptions requiring doubt.',misread='H uses lowercase k_0 in the margin. C and H each omit one visible component of the L4 overlap; H omits the low glyph beneath C.'),
 dict(habit='The small pi is drawn with upright legs and a nearly straight roof.',pages=[12],consistency='Observed in the first pi_1, both display pi_1 expressions, the display left-hand pi, and the underbrace pi_i. The local convention is retained without silently promoting the glyph to capital Pi.',misread='No C/H change is required for these pi symbols.'),
 dict(habit='The variable n can be a shallow cup ending in an upward shoulder and downward return.',pages=[12],consistency='The raised insertion and the n at the start of the dimension equality have this form; the insertion leader establishes the raised letter’s attachment.',misread='The leader could be mistaken for a strike; neither witness does so here.'),
 dict(habit='The separate small foliation uses thin, pale strokes with long oblique entries.',pages=[12],consistency='Only the two digits of 11 are observed on this leaf. This observation is limited to that separate hand.',misread='H omits the foliation; it must not be treated as an author page header.')
]
notation=[
 dict(written='pi with subscript bar K/K',rendering=r'\pi_{\bar K/K}',meaning='The group placed on the left of (13).',evidence='First display row: the bar belongs to the first subscript K only; the extension separator is an oblique slash.'),
 dict(written='lim with a left-pointing lower arrow and a lower dotted i',rendering=r'\varprojlim_i',meaning='Projective-limit notation, named in the preceding sentence.',evidence='Both display rows have a left-pointing arrow below lim and a distinct i below the arrow.'),
 dict(written='one wave above one horizontal bar',rendering=r'\simeq',meaning='Written relation in the isomorphism and display (13).',evidence='c15 and c09 show two components, not a wave plus an equals sign.'),
 dict(written='C and Q with an extra inner stroke',rendering=r'\mathbb C,\mathbb Q',meaning='Field symbols used in the opening paragraph and final dimension formula.',evidence='The ordinary non-overlapped field symbols are visible in c15, c09, c10 and c13; this does not settle the uncertain overlapped or low glyphs.'),
 dict(written='eta with one short horizontal bar above',rendering=r'\bar\eta',meaning='The common point named in the paragraph.',evidence='The first pi_1 expression and both rows of (13) carry the same bar and eta form.'),
 dict(written='small raised wedge after the last fundamental-group parentheses',rendering=r'\pi_1(U_i(\mathbb C),\bar\eta)^{\wedge}',meaning='The profinite completion described in the preceding paragraph.',evidence='The final wedge is a distinct two-stroke roof after the closing parenthesis in c09.')
]
abbreviations=[
 dict(form='isom',expansion='isomorphisme',place='L5, before the Qbar isomorphism; no stop supplied'),
 dict(form='pt',expansion='point',place='L7, after comme un'),
 dict(form='top.',expansion='topologiques',place='L8, espaces top.'),
 dict(form='tte',expansion='toute',place='Diagonal note, before ext.'),
 dict(form='ext.',expansion='extension',place='Diagonal note, before de corps'),
 dict(form='pr (alternative only)',expansion='pour',place='Diagonal note, unresolved pour/pr'),
 dict(form='dim',expansion='dimension',place='L20, final equality'),
 dict(form='deg.tr.',expansion='degré de transcendance',place='L20, final equality')
]
doubts=[
 dict(place='L2, relative pronoun',reading=r'\unsure{qui|que}',alternatives=['qui','que'],confidence='low',reason='No distinct i dot or decisive e loop; the terminal run remains ambiguous on c02.'),
 dict(place='L4, overlapped field letters under one overbar',reading=field,alternatives=[r'\overline{\deleted{\mathbb Q}K}',r'\overline{\deleted{K}\mathbb Q}'],confidence='low',reason='Both oval Q-like ink and K-like stem/diagonals survive. Q-under-K is favored, but the ordering of the ink at crossings is not secure; a single letter would discard meaningful strokes.'),
 dict(place='L6, extra low glyph beneath C',reading=r'\underset{\unsure{\mathbb Q|k}}{\mathbb C}',alternatives=[r'\mathbb Q','k'],confidence='low',reason='A loop, inner upright and curled right foot are visible. A Q-like shape is preferred, but the letter and any intended role remain unresolved. The no-glyph alternative is excluded by visible ink.'),
 dict(place='L6, before maintenant',reading=r'\unsure{en|où}',alternatives=['en','où'],confidence='low',reason='The initial loop/open form and shoulder slightly favor en. No clear accent is present, but the compressed shape does not fully exclude où.'),
 dict(place='Diagonal note, after elle vaut',reading=r'\unsure{pour|pr}',alternatives=['pour','pr'],confidence='low',reason='The p and final r are visible; the intervening low run cannot securely establish whether o/u are written.'),
 dict(place='L18, cancelled word',reading=r'\deleted{\unsure{par|pr}}',alternatives=['par','pr'],confidence='low',reason='The cancellation leaves p and a final r-like return, while a possible central a is partly merged with the strike.'),
 dict(place='L20, final parenthesis',reading='ici',alternatives=['où'],confidence='medium',reason='A separate dot over the initial short stem supports ici. Its c and final return are compressed; the retained reading is less certain than the surrounding dark formula.')
]

def audit(id,kind,box,reading):
    return dict(box=id,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading)
audit_boxes=[
 audit('b01','text',[1275,50,1655,178],"``géométriques''"),
 audit('b02','text',[390,180,500,290],r'\unsure{qui|que}'),
 audit('b03','formula',boxes['c03'],r'de $'+field+r'$ dans $\mathbb C$'),
 audit('b04','formula',[510,490,755,600],r'$\overline{\mathbb Q}\simeq\overline{\mathbb Q}_0$'),
 audit('b05','formula',boxes['c04'],'$'+first_formula+'$,'),
 audit('b06','text',[1320,615,1405,710],r'\unsure{en|où}'),
 audit('b07','text',[480,750,985,855],r'$\bar\eta$ est interprété'),
 audit('b08','deletion',[290,880,580,965],r'\deleted{complexe}'),
 audit('b09','number',[900,1100,1005,1170],'(8)'),
 audit('b10','number',boxes['c08'],'(12),'),
 audit('b11','formula',boxes['c09'],r'\['+display+r'\]'),
 audit('b12','margin note',boxes['c10'],r'\margin{'+margin+'}'),
 audit('b13','deletion',[1105,2050,1190,2118],r'\deleted{\unsure{par|pr}}'),
 audit('b14','insertion',[635,2120,1020,2225],r'de \inserted{$n$} groupes'),
 audit('b15','text',[285,2235,405,2325],'ici'),
 audit('b16','number',boxes['c14'],r'\margin{11}')
]
diff_coverage=[
 dict(row=1,classification='macro-only',change_id='',reason='The 12 belongs to the scanpage metadata; it is not a source numeral.'),
 dict(row=2,classification='material',change_id='c01',reason='The ink uses paired high ticks, not guillemets. Dash encoding alone has no separate substantive difference.'),
 dict(row=3,classification='reading-agrees',change_id='',reason='H’s qui is the first C reading; the final retains qui|que because the crop does not settle the ending. The uncertainty difference is recorded in decisions and doubts.'),
 dict(row=4,classification='material',change_id='c02',reason='Both Q-like and K-like components are visible; their overstrike sequence remains uncertain.'),
 dict(row=5,classification='material',change_id='c03',reason='H omits a visible low glyph beneath C; the final narrows the uncertainty to its Q-like/k shape.'),
 dict(row=6,classification='material',change_id='c04',reason='The doubtful word remains open, with en first on the observed shape. The first C alternative is changed but not resolved.'),
 dict(row=7,classification='material',change_id='c05',reason='H adds interprétant before maintenant; there is no word there.'),
 dict(row=8,classification='material',change_id='c06',reason='The live est interprété after eta is on the page.'),
 dict(row=9,classification='material',change_id='c07',reason='(12) is the horizontal text reference after homotopie, not part of the slanted note.'),
 dict(row=10,classification='material',change_id='c08',reason='(13) is the number of the two-row display. The aligned wrapper alone is not material.'),
 dict(row=11,classification='macro-only',change_id='',reason='The closing aligned wrapper has no source reading of its own.'),
 dict(row=12,classification='material',change_id='c09',reason='The diagonal note is substantially readable. Its own words replace H’s illegibility spans and mistaken imports from neighboring horizontal text.'),
 dict(row=13,classification='material',change_id='c09',reason='de corps is written on the diagonal row after tte ext.'),
 dict(row=14,classification='editorial-only',change_id='',reason='H’s explanatory note is editorial and excluded from the page. Its related case error K/k_0 in source transcription is separately covered by change c10.'),
 dict(row=15,classification='material',change_id='c11',reason='The cancelled word cannot be reduced confidently to pr or fully resolved as par; par|pr is retained in the deletion.'),
 dict(row=16,classification='material',change_id='c12',reason='The dotted first stem supports ici rather than H’s où.'),
 dict(row=17,classification='material',change_id='c13',reason='The separate thin foliation 11 is present at the lower left.')
]
report=dict(scan=12,reader='/root/reader_c',lines_read=30,changes=changes,decisions=decisions,inventory=inventory,notes=notes,checks=[],hand=hand,notation=notation,abbreviations=abbreviations,doubts=doubts,audit_boxes=audit_boxes,diff_coverage=diff_coverage)
(root/'edition/reviews/149_scan012.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote 149_scan012.tex and 149_scan012.json')
print(f'{len(changes)} change records; {len(decisions)} mark decisions; {len(inventory)} inventory rows; {len(audit_boxes)} audit boxes; {len(diff_coverage)} difference rows')
