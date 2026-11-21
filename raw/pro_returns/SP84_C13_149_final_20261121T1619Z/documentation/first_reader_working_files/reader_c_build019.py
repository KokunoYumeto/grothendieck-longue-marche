from pathlib import Path
import json

root=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads((root/'work/reader_c_scan019_boxes.json').read_text())
tex=r'''\scanpage{19}
\mspage{9}
On a ainsi plusieurs points de vue essentiellement équivalents, pour décrire par voie profinie \unsure{\deleted{une}|une} extension \inserted{$K$} de type fini de $\mathbb Q$ :

1) Par le topos étale $B_K$, en tant que topos pro-galoisien sur $B_{\mathbb Q}$

2) Par le groupoïde fondamental $\Pi_K$ de ce topos, (le groupoïde de ses pts, ou de ses rev. universels) --- en tant que groupoïde au-dessus de $\Pi_{\mathbb Q}$

\deleted{2)} \deleted{\unsure{2}}3) Par le groupe extérieur $E_K$, au-dessus du groupe extérieur $E_{\mathbb Q}\longleftarrow\Gamma_{\mathbb Q}$ (pro-gr)

4) En termes d'une clôture algébrique $\bar K/K$ (i.e. en décrivant le couple $(K,\bar K)$ plutôt que $K$), par un objet $\overline{\mathbb Q}\in\operatorname{Ob}\Pi_{\mathbb Q}$, et un hom de groupes profinis $\unsure{\mathcal E|E}\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}$.
\deleted{un ss-groupe ouvert $\Gamma$ de}

5) En termes d'une clôture alg. \inserted{\unsure{fixée|fixe}} $\overline{\mathbb Q}$ de $\mathbb Q$, \deleted{par le groupe}\inserted{et \unsure{si} $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$}, \deleted{par} considérant les couples $(K,i)$ où $i:k\longrightarrow\overline{\mathbb Q}$ est un plongement de le clôture alg.\inserted{$k$} de $\mathbb Q$ dans $K$ dans $\overline{\mathbb Q}$ : \deleted{\unsure{comme}} par le groupe extérieur $\pi_K\unsure{\neq|=}\pi_1(K)$, sur lequel un sous-groupe ouvert $\Gamma_K\subset\Gamma$ opère extérieurement.

\margin{6) En termes d'un $\overline{\mathbb Q}/\mathbb Q$ : par le groupoïde $\Pi_{K\otimes_{\mathbb Q}\overline{\mathbb Q}}$ (pas néc. connexe) sur lequel $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opère --- ou bien parfois, par le topos galoisien $B_{K\otimes_{\mathbb Q}\overline{\mathbb Q}}$, avec $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opérant dessus\ldots}
\margin{18}
'''
(root/'edition/reviews/149_scan019.tex').write_text(tex)
changes=[]
def ch(place,C,H,final,evidence,crop,confidence,against_C,against_H,kind,error_category,marked_in_H=False,mathematical=False):
    changes.append(dict(id=f'c{len(changes)+1:02d}',place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/149_scan019_{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical))
ch('L3, word before extension','une',r'\struck{une}',r'\unsure{\deleted{une}|une}',
   'The u/n humps and low terminal e remain visible through crowded dark retracing. A short transverse stroke crosses their lower/middle strokes, favoring cancellation, but it merges with the letter connections and does not form the independent continuous strike seen in L16 and L18. The deletion state remains explicitly doubtful.', 'c01','medium',True,False,'deletion state','Struck text')
ch('L3, raised K after extension',r'extension \inserted{$K$}',r'\add{$K$} extension',r'extension \inserted{$K$}',
   'The separately raised K stands above the interval after the final n of extension and before de. Its stem and two arms are visible. It is not positioned above the interval before extension.', 'c01','high',False,True,'insertion or placement','Insertions put in the wrong place',mathematical=True)
ch('L5, end of item 1',r'$B_{\mathbb Q}$',r'$B_{\mathbb Q}$.',r'$B_{\mathbb Q}$',
   'B has two lobes and the low Q its internal stroke and descending tail. The space immediately after the Q tail has no written full stop of the density of the surrounding ink.', 'c02','high',False,True,'text not on the page','Text that is not on the page')
ch('L7, punctuation after ce topos','ce topos, (','ce topos (','ce topos, (',
   'A separate dark bent comma lies between the final s of topos and the short opening-parenthesis stroke before le; it is not a pen return attached to the s.', 'c03','high',False,True,'omission','Omissions')
ch('L9, end of item 2',r'$\Pi_{\mathbb Q}$',r'$\Pi_{\mathbb Q}$.',r'$\Pi_{\mathbb Q}$',
   'The capital Pi roof and two legs, the low Q and its descending tail are complete. There is no separate full stop to their right.', 'c04','high',False,True,'text not on the page','Text that is not on the page')
ch('Isolated cancelled numbering above L10',r'\deleted{2)}','Cancellation described only in an editorial note',r'\deleted{2)}',
   'The upper numeral has the curved head, descending diagonal and lower foot of 2, with a closing parenthesis. Additional oblique retracing crosses this separate upper entry. It is distinct from the lower live numbering.', 'c05','high',False,True,'omission','Omissions',marked_in_H=True)
ch('L10, overwritten number before item 3','3)','3)',r'\deleted{\unsure{2}}3)',
   'The lower live 3 has two heavy rightward lobes. Lighter earlier ink includes a rounded upper sweep, a diagonal descending toward the left and a lower foot, favoring an earlier 2 beneath the 3. Overwriting prevents complete separation of the old digit, so only that underlying digit is marked doubtful; the closing parenthesis is shared and not duplicated.', 'c05','medium',True,True,'omission','Omissions')
ch('L11, entire relation between the exterior groups',r'$E_{\mathbb Q}\longleftarrow\Gamma_{\mathbb Q}$',r'$E_{\mathbb Q}\simeq\Gamma_{\mathbb Q}$',r'$E_{\mathbb Q}\longleftarrow\Gamma_{\mathbb Q}$',
   'There is one shaft with an angular return at its left endpoint. The right endpoint is a terminal thickening, and there is no second parallel shaft or upper wave. Both low Q indices and the capital Gamma roof/stem were checked with the relation.', 'c06','high',False,True,'misread symbol or index','Symbols and indices',mathematical=True)
ch('L11, parenthetical abbreviation','(pro-gr)','(pro-groupe)','(pro-gr)',
   'After pro and the short hyphen there are a descending g loop and a short r, followed immediately by the closing parenthesis at the sheet edge. No o, u, p, e sequence follows that r.', 'c06','high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
ch('L11, end of item 3','(pro-gr)','(pro-groupe).','(pro-gr)',
   'The closing parenthesis reaches the visible sheet edge. No full stop is written after it; no punctuation is supplied beyond the paper.', 'c06','high',False,True,'text not on the page','Text that is not on the page')
ch('L13, description of the pair','le couple','des couples','le couple',
   'The article has one tall l loop and a low e return, with no separate d or final s. The noun shows c, connected ou, the p descender, l and low final e; no extra s follows it before the parenthesis of the pair.', 'c07','high',False,True,'misread word','Words')
ch('L16, abbreviated word in the cancelled line',r'\deleted{un ss-groupe ouvert $\Gamma$ de}',r'\struck{un sous-groupe ouvert $\Gamma$ de}',r'\deleted{un ss-groupe ouvert $\Gamma$ de}',
   'After un are two short s-shaped strokes and a hyphen before the g descender. There is no space or succession of o/u strokes to support sous. A long independent line crosses the entire phrase. The Gamma has its own low roof and upright; nearby descenders from the preceding line were not taken as extra cancelled letters.', 'c09','high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
ch('Raised word attached after alg. in L17',r'\inserted{fixée}',r'\add{fixe}',r'\inserted{\unsure{fixée|fixe}}',
   'The tall looped f, detached i dot, crossed/slanted x form and low following e-run can be traced. A small closed terminal loop above the right branch of the insertion leader can be a second e, but it merges with that branch; an acute stroke is not independently separable. The V-shaped attachment reaches the gap after alg. and before Q-bar. The word is retained with a localized fixe/fixée doubt.', 'c10','medium',False,True,'misread word','Words')
ch('L18, location of the cancelled phrase',r'\deleted{par le groupe}\inserted{et $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$}',r'et si $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$, \struck{par le groupe}',r'\deleted{par le groupe}\inserted{et \unsure{si} $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$}',
   'The lower baseline reads par le groupe beneath the raised et/Gamma line. One long stroke runs through the lower p, l/e and groupe letters. The raised replacement begins over its left end, not after the right-hand comma of the Gamma expression.', 'c11','high',False,True,'insertion or placement','Insertions put in the wrong place')
ch('Raised line over L18, tiny word between et and Gamma',r'et $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$',r'et si $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$',r'et \unsure{si} $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$',
   'Between et and the first Gamma are a detached upper dot and two small lower strokes. These favor si. The small left stroke does not form an unambiguous s, and the right/lower strokes partly overlap or touch the ascender of cancelled le beneath them. The doubtful word is retained without asserting a clean separation from the underlying letter.', 'c11','low',True,False,'omission','Omissions')
ch('Raised replacement line over L18',r'\inserted{et $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$}',r'et si $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$',r'\inserted{et \unsure{si} $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$}',
   'The et, first Gamma, two equality bars and complete second Gamma with Q-bar/Q index occupy the interlinear space above the cancelled phrase. Their baseline and smaller size distinguish this insertion from the live main line. The cancellation passes through the old words below; it does not cancel the raised Gamma equation.', 'c11','high',False,True,'insertion or placement','Insertions put in the wrong place',mathematical=True)
ch('L18, cancelled word immediately before considérant',r'\deleted{par} considérant',r'\struck{par le groupe} en considérant',r'\deleted{par} considérant',
   'Immediately before considérant there is a p with a long descender, an a loop and r return crossed by a short horizontal stroke. There is no independent en between this crossed par and considérant. The longer crossed par le groupe lies earlier, below the insertion.', 'c11','high',False,True,'deletion state','Struck text')
ch('L20, article after plongement de','de le clôture','de la clôture','de le clôture',
   'After de the article has a tall narrow l loop and a small open e return. There is no closed a oval. The clear le is retained despite its grammar; the following clôture and alg., raised k, Q and K were read in the same crop.', 'c12','high',False,True,'misread word','Words')
ch('L21, cancelled word before par le groupe',r'\deleted{\unsure{comme}}',r'\struck{\ill{}}',r'\deleted{\unsure{comme}}',
   'An open initial c and a low rounded next trace survive the strike. Several medial humps and a final small loop are compatible with comme, but the dark horizontal cancellation masks the boundaries of the medial letters. The doubtful reading is preserved, not resolved as a fully readable word.', 'c13','medium',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked_in_H=True)
ch('L22, whole comparison of the two pi expressions',r'$\pi_K\neq\pi_1(K)$',r'$\pi_K=\pi_1(K)$',r'$\pi_K\unsure{\neq|=}\pi_1(K)$',
   'Between the two pi expressions are two horizontal bars and an additional hooked/curved stroke attached at or below the lower bar. This extra ink favors the unequal reading, but it does not plainly cross the upper bar, so an unqualified inequality is not justified. Both pi forms, the K index, the numeric 1 index and the final parentheses were checked as a whole.', 'c14','medium',False,True,'misread symbol or index','Symbols and indices',mathematical=True)
ch('Left vertical margin, rotated row 2, parenthesis','(pas néc. connexe)',r'(\ill{})','(pas néc. connexe)',
   'The upright crop shows p with its descender, low a and s; then the short néc. with accent/dot; then c/o, connected n humps, x crossing and terminal e. Both parentheses are visible. These are ordinary legible marginal words.', 'c15','high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked_in_H=True)
ch('Left vertical margin, rotated row 3, after ou','ou bien parfois, par',r'ou \ill{}','ou bien parfois, par',
   'After ou are a short b stem, dotted i and low en; the next word has a p descender, ar sequence, tall looped f and low ois, followed by a comma. A separate par with p descender follows. The whole phrase fits the written line and is retained.', 'c15','high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked_in_H=True)
ch('Left vertical margin, rotated row 4, after the B expression','avec',r'\ill{} profinis, \ill{}','avec',
   'There is one short low word between the comma after the B expression and the next Gamma: a small initial a, shallow v and connected low e/c strokes. No p descender, f ascender, second word or additional comma is written there; profinis is not on the page.', 'c15','high',False,True,'misread word','Words',marked_in_H=True)
ch('Lower-left foliation',r'\margin{18}','(omitted)',r'\margin{18}',
   'The thin small hand has a sloping lead into an upright 1 followed by an 8 with two closed loops. This is separate from the author’s larger 9 at the head and is retained as marginal foliation.', 'c16','high',False,True,'omission','Omissions')

inventory=[]
def inv(element,kind,position,first,hand='author'):
    inventory.append(dict(scan=19,sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('e01','text','head, near centre','9')
inv('e02','text','main L1–L3','On a ainsi plusieurs points de vue')
inv('e03','deletion','L3, before extension',r'\unsure{\deleted{une}|une}')
inv('e04','insertion','above L3, after extension',r'$K$')
inv('e05','text','main L4–L5','1) Par le topos étale')
inv('e06','text','main L6–L9','2) Par le groupoïde fondamental')
inv('e07','deletion','separate entry above item 3',r'\deleted{2)}')
inv('e08','deletion','beneath the live 3 at the beginning of L10',r'\deleted{\unsure{2}}')
inv('e09','text','main L10–L11','3) Par le groupe extérieur')
inv('e10','text','main L12–L15',"4) En termes d'une clôture algébrique")
inv('e11','deletion','main L16',r'un ss-groupe ouvert $\Gamma$ de')
inv('e12','text','main L17–L24',"5) En termes d'une clôture alg.")
inv('e13','insertion','above L17, attached after alg.',r'\unsure{fixée|fixe}')
inv('e14','deletion','main L18, beneath the raised equation','par le groupe')
inv('e15','insertion','raised line above L18',r'et \unsure{si} $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$')
inv('e16','deletion','main L18, before considérant','par')
inv('e17','insertion','above L20, attached after alg.',r'$k$')
inv('e18','deletion','main L21, before par le groupe',r'\unsure{comme}')
inv('e19','margin note','left margin, vertical, five rows after clockwise rotation',r"6) En termes d'un $\overline{\mathbb Q}/\mathbb Q$")
inv('e20','text','lower-left corner','18','thin smaller foliation hand, distinct from author')

margin=r"\margin{6) En termes d'un $\overline{\mathbb Q}/\mathbb Q$ : par le groupoïde $\Pi_{K\otimes_{\mathbb Q}\overline{\mathbb Q}}$ (pas néc. connexe) sur lequel $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opère --- ou bien parfois, par le topos galoisien $B_{K\otimes_{\mathbb Q}\overline{\mathbb Q}}$, avec $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opérant dessus\ldots}"
audit=[]
def au(kind,box,reading):
    if isinstance(box,str): box=boxes[box]
    audit.append(dict(box=f'b{len(audit)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
au('number',[750,30,830,100],'9')
au('insertion and deletion','c01',r'\unsure{\deleted{une}|une} extension \inserted{$K$} de')
au('number',[325,380,475,480],'1)')
au('formula','c02',r'$B_{\mathbb Q}$')
au('number',[325,590,475,700],'2)')
au('text','c03','ce topos, (le')
au('formula','c04',r'$\Pi_{\mathbb Q}$')
au('number and deletion',[330,930,475,1080],r'\deleted{2)} \deleted{\unsure{2}}3)')
au('formula and text','c06',r'$E_{\mathbb Q}\longleftarrow\Gamma_{\mathbb Q}$ (pro-gr)')
au('number',[325,1160,475,1270],'4)')
au('text','c07','le couple')
au('formula','c08',r'$\overline{\mathbb Q}\in\operatorname{Ob}\Pi_{\mathbb Q}$, $\unsure{\mathcal E|E}\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}$.')
au('deletion','c09',r'\deleted{un ss-groupe ouvert $\Gamma$ de}')
au('insertion',[1230,1495,1475,1670],r'alg. \inserted{\unsure{fixée|fixe}} $\overline{\mathbb Q}$')
au('number',[325,1575,470,1675],'5)')
au('insertion and deletion','c11',r'\deleted{par le groupe}\inserted{et \unsure{si} $\Gamma=\Gamma_{\overline{\mathbb Q}/\mathbb Q}$}, \deleted{par} considérant')
au('insertion and text','c12',r'de le clôture alg.\inserted{$k$} de $\mathbb Q$ dans $K$')
au('deletion','c13',r'\deleted{\unsure{comme}}')
au('formula','c14',r'$\pi_K\unsure{\neq|=}\pi_1(K)$,')
au('margin note','c15',margin)
au('number','c16',r'\margin{18}')

coverage=[]
def dc(row,classification,change_id,reason): coverage.append(dict(row=row,classification=classification,change_id=change_id,reason=reason))
dc(1,'editorial-only','',r'Archive scan header versus H page-marker syntax; the actual handwritten author number 9 is retained as \mspage{9}.')
dc(2,'editorial-only','','de l’auteur belongs to H’s explanatory page marker, not to the manuscript.')
dc(3,'material','c01,c02','The opening word state remains locally doubtful; the raised K is placed after extension from the ink, not before it.')
dc(4,'material','c02','Same physical raised K as row 3; counted once as a placement disagreement.')
dc(5,'macro-only','','Literal 1) and the enumerate wrapper express the same author number; the handwritten 1) was read and audited.')
dc(6,'material','c03','The following item number is an enumerate alignment artifact; H’s full stop after B_Q is absent in the source.')
dc(7,'material','c04','The comma after ce topos is visible.')
dc(8,'macro-only','','Two versus three TeX hyphens encode the same handwritten long dash.')
dc(9,'material','c05,c06,c07','H adds a full stop after Pi_Q and relegates the upper cancelled 2) to a note; the lower live 3 also overlies a doubtful older 2 trace.')
dc(10,'material','c08','One leftward arrow, not an isomorphism sign, is written.')
dc(11,'material','c09','The source ends its abbreviation with gr, not groupe.')
dc(12,'material','c10','The item-4 number is an enumerate alignment artifact; no period follows the item-3 closing parenthesis at the edge.')
dc(13,'material','c11','The source reads le couple in the singular.')
dc(14,'reading-agrees','','M1010 remains undecided between the written E-like alphabet renderings; H gives one allowed alternative. No resolution or material font correction is claimed.')
dc(15,'material','c12','The cancelled line writes ss-groupe, not the expanded sous-groupe.')
dc(16,'macro-only','','The literal item 5) and enumerate numbering agree; 5) was read and audited.')
dc(17,'material','c13','The raised word retains fixée/fixe uncertainty because its terminal loop merges with the attachment stroke.')
dc(18,'material','c14','The crossed par le groupe lies under and before the replacement, not after the equation.')
dc(19,'material','c15,c16','The small strokes after raised et are retained as doubtful si; the whole equation belongs to the interlinear insertion.')
dc(20,'material','c14,c17','The longer deletion is earlier; directly before considérant the source has crossed par and no separate en.')
dc(21,'material','c18','The visible article is le, retained literally.')
dc(22,'material','c19','The crossed word remains tentatively comme, with its masked medial letters explicitly doubtful.')
dc(23,'material','c20','The extra lower hooked stroke is retained in a localized neq/= doubt within the complete formula.')
dc(24,'editorial-only','','The enumerate wrapper and H’s numbering description are editorial. The actual corrections are transcribed and accounted for in c06–c07.')
dc(25,'material','c21','The marginal parenthesis pas néc. connexe is readable in the rotated crop.')
dc(26,'macro-only','','The dash-length difference is TeX rendering only; the manuscript has one long dash.')
dc(27,'material','c22','The words bien parfois, par are legible in the vertical note.')
dc(28,'material','c23','The short word is avec; profinis and an additional comma are not written there.')
dc(29,'material','c24','The terminal three dots are shared content rendered differently; H’s vertical-note comment is editorial, and its text omits the separate thin foliation 18.')

report=dict(
 scan=19,reader='/root/reader_c',lines_read=36,changes=changes,
 decisions=[dict(id='M1010',decision='undecided',reading=r'\unsure{\mathcal E|E}',evidence='The complete map has an open two-lobed E-like first glyph, a single rightward arrow, and Gamma with the full Q-bar/Q extension index. The rounded glyph lacks a decisive upright/three-bar construction and also resembles an epsilon form. The local rounded E in item 3 does not establish a reliable alphabet distinction. The original mathcal-E/E alternatives remain; no mathematical identification resolves the font.',crop='crops/149_scan019_c08.png',box=boxes['c08'],confidence='low')],
 inventory=inventory,
 notes=[
  'Reader: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149. This is a first reading of scan019 only, using its own packet and images. The whole image and both prepared halves were inspected once; every agreed word, abbreviation, sign and index was read against the ink before the mandatory/open-place crops.',
  'Line accounting: 24 main body rows, including the separate crossed un ss-groupe line; four raised insertion groups (K, fixée/fixe, et ... Gamma, k); the isolated upper cancelled number; five rotated marginal rows; and the author number and foliation give 36 inspected rows. The overwritten digit under the live 3 shares that row and is not counted again.',
  'S019.1 — The page says that several essentially equivalent profinite descriptions of a finite-type extension K of Q are available. Its five main items name an étale topos, a fundamental groupoid, an exterior group, data using an algebraic closure of K, and data using a fixed algebraic closure of Q. This records the author’s assertion; it is not a proof check of the claimed equivalences.',
  'S019.2 — A sixth description is written vertically in the left margin. It names the groupoid and the Galoisian topos after tensoring K with Q-bar, with the indicated Gamma action; its parenthesis explicitly says pas néc. connexe. The full note has five rows when rotated clockwise.',
  'S019.3 — The relation in the last main paragraph is preserved as pi_K unsure{neq|=} pi_1(K). Its lower hooked ink does not form a clean upper-bar crossing. No mathematical expectation was used to turn that stroke into an unequivocal equality or inequality.',
  'The literal de le clôture is clear and has not been grammatically repaired. The opening word before extension has uncertain cancellation state; the raised K attaches after extension. The source also has the short forms pts, rev., pro-gr, hom, ss-, alg. and néc.; they are not expanded in the transcription.',
  'The upper crossed 2) and the uncertain old 2 beneath the live 3 are distinct physical corrections. In item 5, the raised replacement equation sits above the cancelled par le groupe, and the later par before considérant is separately crossed. The leaders belonging to fixée/fixe and k are attachment strokes, not extra cancellations.',
  'The author’s page number is 9 at the head. Thin smaller 18 at the lower left is separate foliation in another hand. Neither the archive scan number 19 nor H’s editorial explanatory notes are manuscript prose.',
  'The only prelisted mark M1010 remains undecided. The C-only doubtful crossed comme was separately cropped and remains tentative because the cancellation masks its middle. Other localized doubts are the opening word state, the old numeral under 3, fixée/fixe, the tiny si, and the pi relation. No formula was completed from mathematical context.',
  'Crop c15 was initially found to clip the final row of the still-unresolved vertical note. The same crop file was extended to [0,1000,430,2290] before the full marginal reading was settled; this is the sole saved version. Agreed pen numerals have coordinate-only audit boxes unless a witness omission or actual correction required a crop.',
  'No mathematical proof, refutation, computation or background-use check was performed for this reader return; checks is intentionally empty.'
 ],
 checks=[],
 hand=[
  dict(habit='A tall narrow l loop followed by a compressed low e return can be mistaken for another article or an s-ending.',pages=[19],consistency='Locally verified in le couple (L13) and de le clôture (L20); no general rule inferred for other leaves.',misread='H reads des couples and de la clôture.'),
  dict(habit='Long horizontal cancellations run through old baseline words, while raised replacement text occupies a separate level.',pages=[19],consistency='Clear in L16 and the par le groupe replacement in L18; the short crowded overtrace on une is a limiting case and is not asserted certain.',misread='H moves the longer cancelled phrase after the equation; C leaves the opening une unqualifiedly live.'),
  dict(habit='Interlinear writing can overlap the ascenders of the crossed line beneath it.',pages=[19],consistency='The tiny possible si above cancelled le and the fixée/fixe leader are both locally crowded; their letter boundaries remain doubtful.',misread='C omits possible si; H gives si and fixe without local uncertainty.'),
  dict(habit='The E-like form can have two rounded open lobes.',pages=[19],consistency='Visible in the item-3 Q-indexed symbol and the item-4 first map symbol; this does not settle a plain/calligraphic/epsilon alphabet distinction.',misread='M1010 remains open; H chooses E alone.'),
  dict(habit='A live digit may be heavily overwritten over a lighter earlier numeral.',pages=[19],consistency='One local case: lower live 3 over a 2-like trace, separate from the upper crossed 2).',misread='Both witnesses omit the uncertain underlying lower digit.'),
  dict(habit='Thin small foliation is graphically distinct from the author’s heavier page and item numbers.',pages=[19],consistency='18 in the lower-left corner differs from author 9 and items 1–6.',misread='H omits the foliation 18.')
 ],
 notation=[
  dict(written=r'B_K, B_{\mathbb Q}',rendering=r'B_K, B_{\mathbb Q}',meaning='Topos symbols named by item 1.',evidence='The B forms have two lobes and low indices; the final Q is internally doubled and has a descending tail.'),
  dict(written=r'\Pi_K, \Pi_{\mathbb Q}',rendering=r'\Pi_K, \Pi_{\mathbb Q}',meaning='Fundamental groupoid symbols named by item 2.',evidence='Broad upper roofs with two separate tall legs; item 4 repeats capital Pi in the object expression.'),
  dict(written='one leftward arrow',rendering=r'\longleftarrow',meaning='Written relation between the two Q-indexed symbols in item 3.',evidence='c06 has one shaft and a left angular head; no isomorphism wave or second shaft is present.'),
  dict(written='rounded two-lobed E-like letter',rendering=r'\unsure{\mathcal E|E}',meaning='Source of the homomorphism in item 4; alphabet remains uncertain.',evidence='Whole formula in c08; the form also permits an epsilon-like visual interpretation, which is not resolved from mathematics.'),
  dict(written=r'\Gamma_{\overline{\mathbb Q}/\mathbb Q}',rendering=r'\Gamma_{\overline{\mathbb Q}/\mathbb Q}',meaning='Repeated extension-indexed Gamma in items 4–6.',evidence='One roof and upright; the index has a bar on its first Q only and a slanted separator before the unbarred Q.'),
  dict(written='two bars plus a curved lower hook',rendering=r'\unsure{\neq|=}',meaning='Unresolved relation in the pi comparison of item 5.',evidence='c14: the additional ink attaches at/below the lower bar without a clean crossing of the upper bar.'),
  dict(written=r'K\otimes_{\mathbb Q}\overline{\mathbb Q}',rendering=r'K\otimes_{\mathbb Q}\overline{\mathbb Q}',meaning='Index of both groupoid and topos symbols in the sixth marginal item.',evidence='c15, rotated rows 2 and 4: circled crossed tensor glyph, low Q index, then barred Q.')
 ],
 abbreviations=[
  dict(form='pts',expansion='points',place='L7, item 2'),
  dict(form='rev.',expansion='revêtements',place='L8, item 2'),
  dict(form='pro-gr',expansion='pro-groupe',place='L11, item 3'),
  dict(form='i.e.',expansion='id est',place='L13, item 4'),
  dict(form='hom',expansion='homomorphisme',place='L15, item 4'),
  dict(form='ss-groupe',expansion='sous-groupe',place='L16, cancelled line'),
  dict(form='alg.',expansion='algébrique',place='L17 and L20, item 5'),
  dict(form='néc.',expansion='nécessairement',place='left margin, rotated row 2')
 ],
 doubts=[
  dict(place='L3, word before extension',reading=r'\unsure{\deleted{une}|une}',alternatives=['deleted une','live une'],confidence='medium',reason='Short transverse overtracing merges with the letter connections; the continuous independent strike of the longer cancellations is absent.'),
  dict(place='L10, old digit underneath live 3',reading=r'\deleted{\unsure{2}}3)',alternatives=['earlier 2 under 3','older numeral trace not securely separable'],confidence='medium',reason='A light diagonal and foot favor 2, but the heavy live 3 hides part of the older shape.'),
  dict(place='L15, M1010 source of the whole map',reading=r'\unsure{\mathcal E|E}',alternatives=[r'\mathcal E','E',r'\epsilon as a shape alternative'],confidence='low',reason='Two rounded open lobes do not securely discriminate the alphabet; no mathematical identification is used to settle it.'),
  dict(place='Raised word attached to L17 after alg.',reading=r'\inserted{\unsure{fixée|fixe}}',alternatives=['fixée','fixe'],confidence='medium',reason='The terminal small loop merges with the right branch of the leader, and the acute is not independently isolated.'),
  dict(place='Raised line above L18, between et and Gamma',reading=r'\unsure{si}',alternatives=['si','strokes partly belonging to the underlying cancelled le ascender'],confidence='low',reason='Detached dot and two small strokes favor si, but the s and lower boundaries are not cleanly separable from the older line.'),
  dict(place='L21, cancelled word before par le groupe',reading=r'\deleted{\unsure{comme}}',alternatives=['comme','medial letters unrecoverable under the strike'],confidence='medium',reason='Initial c and rounded traces survive; the dark horizontal line obscures the middle letters, so C’s doubt is not resolved.'),
  dict(place='L22, relation in the whole pi formula',reading=r'\pi_K\unsure{\neq|=}\pi_1(K)',alternatives=[r'\neq','='],confidence='medium',reason='There is extra curved lower ink beyond two equality bars, but no clear diagonal crossing the upper bar.')
 ],
 audit_boxes=audit,diff_coverage=coverage)
(root/'edition/reviews/149_scan019.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan019 proposal and report:', len(changes),'changes;',len(inventory),'inventory elements;',len(audit),'audit boxes;',len(coverage),'difference rows.')
