from pathlib import Path
import json
root=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads((root/'work/reader_c_scan023_boxes.json').read_text())
tex=r'''\scanpage{23}
\mspage{11}
Écrivons comme tantôt $K=\varinjlim A_i$ donc \deleted{$K\otimes$} $\eta=\operatorname{Spec}(K)=\varprojlim U_i$, on a (en termes d'un pt géom. quelconque $\bar\eta$ de $\operatorname{Spec}K$ i.e. en termes d'un $\bar K$)
\[
\pi_K=\varprojlim_i\pi_1(\bar U_i\deleted{\unsure{\bar\eta|\bar K}},\unsure{\bar\eta|\bar K}),\quad\text{où }\bar U_i=U_i\otimes_{\unsure{k|K}}\overline{\mathbb Q}
\]
et il suffit de voir que $\forall i,\ \overset{f_i}{\overline{f|A_i}}=\overset{g_i}{\overline{g|A_i}}$ : moyennant le fait que
\[
\pi_1(f_i^*)=\pi_1(g_i^*):\pi_{K'}\unsure{\longrightarrow|-}\pi_1(U_i)\deleted{\unsure{K|\bar\eta}}
\]
(comme hom de groupes extérieurs. Or pour $i$ fixé, on a $K'=\unsure{\varinjlim|\underset{-}{\lim}} A'_j$, où les $A'_j$ contiennent $f_i(A_i)$ et $g_i(A_i)$, donc
\[
\pi_{K'}=\varprojlim_j\pi_1(\bar V_j,\bar\eta'),\quad\text{avec }\bar V_j=\operatorname{Spec}(A_j)\otimes_k\overline{\mathbb Q}.
\]
Notons (prenant les $V_j$ \deleted{\unsure{normaux}}\inserted{réguliers}) que les hom de transition dans le syst. projectif des $\pi_1(\bar V_j,\bar\eta')$ sont surjectifs --- donc \unsure{:|..} $\pi_{K'}\longrightarrow\pi_1(\bar V_j,\bar\eta')$ est surjectif, ce qui implique que l'égalité de $f^*$ et $g^*:\pi_{K'}\rightrightarrows\pi_1\deleted{\unsure{K|k}}(\bar U_i)$ (comme hom extérieurs) implique celle des $\pi_1(\bar V_j)\longrightarrow\pi_1(\bar U_i)$.
Donc l'égalité $f_i=g_i$ (d'où $f=g$) sera consé-quence du résultat plus général,
\margin{22}
'''
(root/'edition/reviews/149_scan023.tex').write_text(tex)
changes=[]
def ch(place,C,H,final,evidence,crop,confidence,against_C,against_H,kind,error_category,marked_in_H=False,mathematical=False):
 changes.append(dict(id=f'c{len(changes)+1:02d}',place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/149_scan023_{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical))
ch('L1, word after comme','tantôt',"d'habitude",'tantôt',
 'The initial tall crossed t, compressed an run, second rising t stroke, low o with its upper accent stroke, and final separate t are visible. There is no initial d/apostrophe or the longer h/b/i/u sequence required by d’habitude.', 'c01','high',False,True,'misread word','Words')
ch('L1, punctuation after the opening limit expression',r'$K=\varinjlim A_i$,',r'$K=\varinjlim A_i$,',r'$K=\varinjlim A_i$',
 'After A there is a dotted low i with a curved descending terminal. The space beyond that index contains no separate comma. The curved tail belongs to the index; neither reader nor root could identify an independent punctuation mark after it.', 'c02','high',True,True,'text not on the page','Text that is not on the page')
ch('L2, cancelled fragment before eta',r'\deleted{$\unsure{K_0|K}$}',r'\struck{$K\otimes$}',r'\deleted{$K\otimes$}',
 'The first glyph retains a tall stem and oblique K arms under additional crossing strokes. The second is a closed circle with internal crossing strokes separate from the long horizontal cancellation; it is a circled cross, not a plain low zero or empty space. The fragment is crossed as a whole before the live eta equation.', 'c03','high',True,False,'misread symbol or index','Symbols and indices',mathematical=True)
ch('L5, cancelled low glyph after barred U_i in the first display',r'\deleted{\unsure{\bar\eta|\bar K}}','(omitted)',r'\deleted{\unsure{\bar\eta|\bar K}}',
 'A compact, heavily retraced low glyph stands after U_i and before the comma and live barred glyph. A short upper bar is visible, but the dense crossed lower strokes do not separate eta from K. Its presence and cancelled state are certain; the letter remains qualified.', 'c04','medium',False,True,'omission','Omissions',mathematical=True)
ch('L6, complete restriction equality and its upper labels',r'$\overset{f_i}{\overline{f|A_i}}=\overset{g_i}{\overline{g|A_i}}$',r'$\underbrace{f\mid A_i}_{f_i}=\underbrace{g\mid A_i}_{g_i}$',r'$\overset{f_i}{\overline{f|A_i}}=\overset{g_i}{\overline{g|A_i}}$',
 'The f_i and g_i labels are above two shallow overlines, each over its restriction expression. There are no lower braces or lower labels. The main line has f, its restriction stroke, A_i, two equality bars, g, its restriction stroke and A_i. The tall first label is also visible in the preceding display crop c04; the audit rectangle includes its full top.', 'c05','high',False,True,'insertion or placement','Insertions put in the wrong place',mathematical=True)
ch('L6, punctuation after the restriction equality',':',',',':',
 'Two separate dark points are written after the final A_i, one above the other with a rightward slant. They form the written colon and are not one comma.', 'c05','high',False,True,'misread symbol or index','Symbols and indices')
ch('L8, target U in the second display',r'\pi_1(U_i)',r'\pi_1(\overline U_i)',r'\pi_1(U_i)',
 'The U has its upright/curved body and low i, with blank space directly above it rather than a bar. The nearby high stroke descends from the preceding text line and is not an overbar. The target is left unbarred despite the later barred targets on this leaf.', 'c06','high',False,True,'text not on the page','Text that is not on the page',mathematical=True)
ch('L8, crossed glyph after the target closing parenthesis',r'\deleted{\unsure{K|\bar\eta}}','(omitted)',r'\deleted{\unsure{K|\bar\eta}}',
 'After the target parenthesis there is a narrow upright cluster with oblique K-like arms and additional crossing strokes. Its overtracing obscures whether an upper stroke belongs to a barred alternative. The struck fragment is retained without claiming every stroke is recoverable.', 'c06','medium',False,True,'omission','Omissions',mathematical=True)
ch('L8 right, abbreviation in the parenthetical phrase','(comme hom','(comme hom.','(comme hom',
 'The terminal m ends with its normal low return. The space between that terminal and the sheet edge contains no separate full stop; the dark point within the word belongs to its reduced o, not punctuation after hom.', 'c07','high',False,True,'text not on the page','Text that is not on the page')
ch('L9, end of groupes extérieurs before Or','extérieurs. Or','extérieurs). Or','extérieurs. Or',
 'The terminal s is followed by a single full stop and then a clear capital O/r. There is no closing-parenthesis stroke between the s and the stop. The earlier opening parenthesis is left unbalanced as written.', 'c08','high',False,True,'text not on the page','Text that is not on the page')
ch('L14, abbreviation before de transition','hom de','hom. de','hom de',
 'The h stem and compressed om finish before a blank interval and the next d. No detached dot lies in that interval.', 'c12','high',False,True,'text not on the page','Text that is not on the page')
ch('L14, words after transition','du syst.','dans le syst.','dans le syst.',
 'After transition are a looped d, low a/n/s run, then a separately spaced l loop and low e before syst. The independent le and the longer first word exclude du.', 'c12','high',True,False,'misread word','Words')
ch('L16, connector before donc','--- donc',', donc','--- donc',
 'A separate horizontal stroke precedes the d of donc. It extends sideways rather than forming a comma descent and is the written dash at the start of this row.', 'c13','high',False,True,'misread symbol or index','Symbols and indices')
ch('L16, two points immediately after donc','(nothing)','(nothing)',r'\unsure{:|..}',
 'There are exactly two detached dark points after the final c, sloping down to the right. Their horizontal and vertical separation are comparable, so colon versus two-point punctuation is not securely distinguishable. Both points are preserved explicitly; no third dot is supplied.', 'c13','medium',True,True,'omission','Omissions')
ch('L18, crossed glyph inside the lower paired-arrow expression',r'\pi_1\deleted{\unsure{K|k}}(\bar U_i)',r'\pi_1(\bar U_i)',r'\pi_1\deleted{\unsure{K|k}}(\bar U_i)',
 'A dark stem-and-arms glyph lies after pi_1 and before the opening parenthesis of barred U_i. Extra oblique strokes overtrace it. The capital/lowercase distinction cannot be separated reliably under this cancellation. The two rightward shafts and the overbar on U belong to the live expression.', 'c14','medium',False,True,'omission','Omissions',mathematical=True)
ch('L18 right, second parenthetical hom','(comme hom','(comme hom.','(comme hom',
 'The final m has a low terminating return and then blank space. No separate full stop follows the word.', 'c15','high',False,True,'text not on the page','Text that is not on the page')
ch('L19, word after celle','des','de','des',
 'The d loop is followed by a low e connection and a terminal attached down-curved s stroke extending beyond it. That final return supplies the s; the word is not reduced to de.', 'c16','high',False,True,'misread word','Words')
ch('L20–L21, split word at the last line break','consé-quence','conséquence','consé-quence',
 'The upper row ends with consé and a separate horizontal hyphen. The next row begins quence. Both word parts and the written hyphen are retained; the final sentence ends with a comma on the lower row.', 'c17','high',False,True,'omission','Omissions')
ch('Lower-left foliation',r'\margin{22}','(omitted)',r'\margin{22}',
 'The thin smaller hand writes two digits with rounded upper heads, descending turns and rightward feet: 22. The foliation is separate from the heavier author number 11 at the head.', 'c18','high',False,True,'omission','Omissions')

inventory=[]
def inv(e,kind,pos,first,hand='author'):
 inventory.append(dict(scan=23,sheet_kind='text',hand=hand,element=e,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
inv('e01','text','head, near centre','11')
inv('e02','text','main L1–L4','Écrivons comme tantôt')
inv('e03','deletion','L2, before the live eta equation',r'$K\otimes$')
inv('e04','display','main L5',r'\pi_K=\varprojlim_i\pi_1(\bar U_i\ldots)')
inv('e05','deletion','within L5, after barred U_i',r'\unsure{\bar\eta|\bar K}')
inv('e06','text','main L6–L7, with upper formula labels','et il suffit de voir que')
inv('e07','display','main L8',r'\pi_1(f_i^*)=\pi_1(g_i^*)')
inv('e08','deletion','after the target closing parenthesis in L8',r'\unsure{K|\bar\eta}')
inv('e09','text','L8 right through L11','(comme hom de groupes extérieurs.')
inv('e10','display','main L12',r"\pi_{K'}=\varprojlim_j\pi_1(\bar V_j,\bar\eta')")
inv('e11','text','main L13–L19','Notons (prenant les')
inv('e12','deletion','L13, after V_j',r'\unsure{normaux}')
inv('e13','insertion','above L13, replacing the crossed word','réguliers')
inv('e14','deletion','L18, after pi_1 and before the live argument',r'\unsure{K|k}')
inv('e15','text','main L20–L21',"Donc l'égalité")
inv('e16','text','lower-left corner','22','thin smaller foliation hand, distinct from author')

firstdisplay=r'$\pi_K=\varprojlim_i\pi_1(\bar U_i\deleted{\unsure{\bar\eta|\bar K}},\unsure{\bar\eta|\bar K})$, où $\bar U_i=U_i\otimes_{\unsure{k|K}}\overline{\mathbb Q}$'
second=r"$\pi_1(f_i^*)=\pi_1(g_i^*):\pi_{K'}\unsure{\longrightarrow|-}\pi_1(U_i)\deleted{\unsure{K|\bar\eta}}$"
third=r"$\pi_{K'}=\varprojlim_j\pi_1(\bar V_j,\bar\eta')$, avec $\bar V_j=\operatorname{Spec}(A_j)\otimes_k\overline{\mathbb Q}$."
audit=[]
def au(kind,box,reading):
 if isinstance(box,str): box=boxes[box]
 audit.append(dict(box=f'b{len(audit)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
au('number',[775,30,845,90],'11')
au('text','c01','tantôt')
au('formula','c02',r'$K=\varinjlim A_i$')
au('formula and deletion','c03',r'\deleted{$K\otimes$} $\eta=\operatorname{Spec}(K)=\varprojlim U_i$')
au('formula and deletion',[410,385,1640,570],firstdisplay)
au('formula',[1180,435,1665,665],r'$\forall i,\ \overset{f_i}{\overline{f|A_i}}=\overset{g_i}{\overline{g|A_i}}$ :')
au('formula and deletion',[310,725,1235,875],second)
au('text','c07','(comme hom')
au('text','c08','extérieurs. Or')
au('formula','c09',r"$K'=\unsure{\varinjlim|\underset{-}{\lim}} A'_j$")
au('formula','c10',third)
au('insertion and deletion','c11',r'$V_j$ \deleted{\unsure{normaux}}\inserted{réguliers})')
au('text','c12','hom de transition dans le syst.')
au('formula',[795,1550,1145,1695],r"$\pi_1(\bar V_j,\bar\eta')$")
au('text','c13',r'--- donc \unsure{:|..}')
au('formula',[610,1690,1145,1840],r"$\pi_{K'}\longrightarrow\pi_1(\bar V_j,\bar\eta')$")
au('formula and deletion',[315,1885,1185,2090],r"$f^*$ et $g^*:\pi_{K'}\rightrightarrows\pi_1\deleted{\unsure{K|k}}(\bar U_i)$")
au('text','c15','(comme hom')
au('text','c16','celle des')
au('formula',[1235,2020,1655,2165],r'$\pi_1(\bar V_j)\longrightarrow\pi_1(\bar U_i)$.')
au('text','c17',r"Donc l'égalité $f_i=g_i$ (d'où $f=g$) sera consé-quence du résultat plus général,")
au('number','c18',r'\margin{22}')

coverage=[]
def dc(row,classification,change_id,reason): coverage.append(dict(row=row,classification=classification,change_id=change_id,reason=reason))
dc(1,'editorial-only','','Archive scan header versus H’s pagination note; author 11 is separately transcribed from the ink.')
dc(2,'editorial-only','','The full stop is part of H’s page-note sentence, not a manuscript punctuation mark.')
dc(3,'material','c01','The source word is tantôt.')
dc(4,'material','c03','The cancelled second symbol is a circled cross, resolving the C-only crossed-fragment doubt to K⊗.')
dc(5,'material','c04','The low barred glyph after U_i is present and crossed; its eta/K reading remains qualified.')
dc(6,'reading-agrees','','The live barred glyph retains M1038 eta/K uncertainty; its primary eta reading agrees with H, so uncertainty alone is not counted as a change.')
dc(7,'editorial-only','','H’s tensor-index explanation is not source text. The first index is locally kept as unsure{k|K}; no Q base or case normalization is derived from the editorial comment.')
dc(8,'material','c05','Part of the one restriction-label placement disagreement: the complete formula is present, with labels above the overlines.')
dc(9,'material','c05','Same upper-label placement as row 8; no extra missing A or i is inferred from the linearized diff.')
dc(10,'material','c05','Same complete restriction expression and upper-label placement; counted once.')
dc(11,'material','c05','The right-hand g_i label is above its overline, matching the left-hand construction.')
dc(12,'material','c05,c06','The right-hand label is above, and the source ends the equality with a colon rather than H’s comma.')
dc(13,'material','c07,c08','The crossed glyph after the target is retained; the separately observed unbarred U also differs from H’s barred rendering.')
dc(14,'material','c09','No period follows the first hom abbreviation.')
dc(15,'material','c10','The closing parenthesis supplied by H before . Or is absent.')
dc(16,'material','c11','No period follows hom in the transition-system sentence.')
dc(17,'material','c12','The source has dans le, including a separately spaced le.')
dc(18,'material','c13,c14','A dash precedes donc, and the source additionally carries two oblique points after donc, omitted by both drafts.')
dc(19,'material','c15','The crossed K/k-like glyph inside the lower map expression is retained with its doubt.')
dc(20,'material','c16','The second parenthetical hom also has no written period.')
dc(21,'material','c17','The terminal attached s of des is visible.')
dc(22,'material','c18','The written line-end hyphen divides consé- and quence; it is retained literally.')
dc(23,'material','c19','H omits the separate foliation 22.')

report=dict(
 scan=23,reader='/root/reader_c',lines_read=25,changes=changes,
 decisions=[dict(id='M1038',decision='undecided',reading=r'\unsure{\bar\eta|\bar K}',evidence='The live glyph has a separate short overbar, an upright/angled head and a long descending right stroke. Its crowded head permits barred eta and barred K; the neighboring crossed low glyph also remains unresolved. The complete formula, its limit index, both argument positions and the base-change clause were examined together. Later clear eta forms on this leaf do not erase the local ambiguity.',crop='crops/149_scan023_c04.png',box=boxes['c04'],confidence='low')],
 inventory=inventory,
 notes=[
  'Reader: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149. This is the first reading of scan023 only, using its own C/H packet, corrected 23-row difference file, notation snapshot and images. The complete image and both prepared halves were personally inspected once, followed by the 18 saved mandatory/open-place crops.',
  'Line accounting: 21 main manuscript rows including the three displayed formula rows; the upper f_i/g_i annotation row; the raised réguliers row; and the author number and foliation give 25 inspected rows. Lower indices remain components of their formulas and are not counted as extra text lines.',
  'S023.1 — The leaf writes K as a direct limit, expresses the indicated pi groups as inverse limits of fundamental groups, and states that equality of the restricted field maps f_i and g_i would follow from the indicated exterior-group equality. This describes the written reduction, not a verification of its validity.',
  'S023.2 — The Notons paragraph replaces a crossed tentative normaux by the legible raised réguliers. It asserts surjectivity of transition maps and of the projection from pi_{K-prime}, then uses that assertion in its stated reduction to equality at finite stages. The final two rows announce a more general result on the continuation. None of these mathematical assertions was proof-checked in this reader return.',
  'S023.3 — The third display literally writes Spec(A_j), without the prime carried by A-prime_j in the preceding paragraph. That difference is retained, not silently corrected. The first displayed map target U_i is unbarred, whereas later targets are barred; the written variation is likewise preserved.',
  'The restriction labels f_i and g_i are above overlines, not beneath braces. The first direct-limit arrow has a visible filled right point; the later direct-limit lower shaft and the tiny endpoint of the second display map remain qualified. The later clear surjective-map arrow and both shafts of the paired arrow were read independently.',
  'The first tensor index has a short straight stem and arms but no securely diagnostic lowercase loop, so k/K is left local to that occurrence. The later tensor index has a curled upper turn and is transcribed k. No value of the base field is supplied from H’s editorial explanation or from mathematical expectation.',
  'The opening comma shared by C and H cannot be separated from the dotted curved i tail and is omitted. The parenthesis after (comme hom de groupes extérieurs is not closed before the written full stop; it remains unbalanced. Three occurrences of hom have no terminal point. After donc there are two dark oblique points, preserved with colon/two-point uncertainty.',
  'The C-only doubt on the opening cancelled fragment is resolved from the visible circled cross as K⊗. M1038 and the adjacent cancelled barred glyph remain open. The crossed glyph after the second-display target, the crossed normaux, and the crossed K/k in the lower formula remain qualified; the first-pass crops do not justify recovering every masked stroke.',
  'The author’s number is 11 at the head. A separate thin smaller hand supplies 22 in the lower-left corner. The archive scan number 23 and H’s editorial notes are not manuscript prose.',
  'The final source word is physically divided consé- / quence, with the hyphen retained in the continuous transcription. The last written punctuation is a comma. No margin prose, diagram or drawing appears on this leaf beyond the separate foliation.',
  'Audit rectangles include the complete correction spans, overline labels, all doubtful formulas and all handwritten numeral indices. Agreed pi_1 occurrences have coordinate-only audit boxes where the halves settled them. Wider audit bounds include ascender/descender tips without recropping decided places.',
  'No mathematical proof, refutation, computation, or background-use check was performed for this return; checks is empty.'
 ],
 checks=[],
 hand=[
  dict(habit='A low dotted i can have a curved, comma-like terminal tail.',pages=[23],consistency='Verified locally at the final A_i of the first row; no blanket punctuation rule is inferred for other indices.',misread='Both C and H supply a comma after the opening limit formula, although no independent comma can be identified.'),
  dict(habit='Barred eta and K-like head shapes can be difficult to separate when retraced or crowded.',pages=[23],consistency='The live and crossed glyphs in the first display remain ambiguous; the later eta-prime forms are clearer and do not settle the earlier heads.',misread='M1038 remains open; H suppresses the nearby crossed glyph.'),
  dict(habit='A small cap or downturned endpoint does not always establish an arrowhead.',pages=[23],consistency='The second-display map and later direct-limit shaft have tiny ambiguous endpoints. The first direct-limit arrow, inverse-limit left arrows and later surjective-map arrow have more distinct heads.',misread='Both drafts give unequivocal arrows at the two ambiguous endpoints.'),
  dict(habit='A raised replacement descender can cross the cancelled word beneath it.',pages=[23],consistency='The g of réguliers descends into the old word and its attachment; the long horizontal cancellation belongs to normaux, not to the raised replacement.',misread='Both drafts retain normaux doubt; no new resolved reading is claimed.'),
  dict(habit='The abbreviation hom is written without a terminal full stop.',pages=[23],consistency='All three occurrences in L8, L14 and L18 have blank space after the terminal return.',misread='H supplies hom. at all three places.'),
  dict(habit='The lower small foliation hand is distinct from the heavier author-number writing.',pages=[23],consistency='22 at the lower-left edge versus 11 above the first line.',misread='H omits the separate foliation 22.')
 ],
 notation=[
  dict(written=r'K=\varinjlim A_i',rendering=r'K=\varinjlim A_i',meaning='The first limit expression as written.',evidence='c02: one lower shaft with a filled right point; no index is written beneath lim.'),
  dict(written=r'K\otimes',rendering=r'\deleted{$K\otimes$}',meaning='Cancelled fragment before the live eta equation; not completed.',evidence='c03: a K-like stem/arms and a distinct circled cross under cancellation.'),
  dict(written=r'\pi_K=\varprojlim_i\pi_1(\bar U_i\ldots)',rendering=r'\pi_K=\varprojlim_i\pi_1(\bar U_i\ldots)',meaning='First inverse-limit expression on the leaf.',evidence='c04: a leftward arrow beneath lim, with a separate dotted i below it, and numeric 1 beneath pi.'),
  dict(written='first tensor base-index stem and arms',rendering=r'\otimes_{\unsure{k|K}}',meaning='The first tensor-product subscript; case unresolved.',evidence='c04: the small straight-stem glyph lacks a securely diagnostic lowercase loop. No mathematical identification settles its case.'),
  dict(written='f_i and g_i above overlines',rendering=r'\overset{f_i}{\overline{f|A_i}}=\overset{g_i}{\overline{g|A_i}}',meaning='The two restrictions named on the source line.',evidence='c04–c05: both labels sit above the bars; no lower braces are written.'),
  dict(written=r'\pi_1(U_i)',rendering=r'\pi_1(U_i)',meaning='Target in the second displayed expression.',evidence='c06: the U is unbarred; the later barred targets are not substituted here.'),
  dict(written='lim with a tiny capped lower right endpoint',rendering=r'\unsure{\varinjlim|\underset{-}{\lim}}',meaning='Later limit construction in the K-prime sentence; endpoint remains uncertain.',evidence='c09: a shaft below lim has a small thickened/downturned end but no securely separated two-branch head.'),
  dict(written=r"\pi_{K'}=\varprojlim_j\pi_1(\bar V_j,\bar\eta')",rendering=r"\pi_{K'}=\varprojlim_j\pi_1(\bar V_j,\bar\eta')",meaning='The third display’s inverse-limit expression.',evidence='c10: leftward lower arrow, a j underneath it, primes after K and eta, and numeric 1 beneath pi.'),
  dict(written=r'\bar V_j=\operatorname{Spec}(A_j)\otimes_k\overline{\mathbb Q}',rendering=r'\bar V_j=\operatorname{Spec}(A_j)\otimes_k\overline{\mathbb Q}',meaning='The base-change expression literally supplied in the third display.',evidence='c10: A_j carries no prime; the lower k has a curled upper turn; Q has its inner stroke and separate bar.'),
  dict(written='two parallel rightward arrows',rendering=r'\rightrightarrows',meaning='The pair attached to f-star and g-star in the lower paragraph.',evidence='c14: two separate shafts and two right terminal heads precede the crossed glyph and barred U argument.')
 ],
 abbreviations=[
  dict(form='pt',expansion='point',place='L3'),
  dict(form='géom.',expansion='géométrique',place='L3'),
  dict(form='i.e.',expansion='id est',place='L4'),
  dict(form='hom',expansion='homomorphisme(s)',place='L8, L14 and L18'),
  dict(form='syst.',expansion='système',place='L14')
 ],
 doubts=[
  dict(place='L5, crossed low glyph after U_i',reading=r'\deleted{\unsure{\bar\eta|\bar K}}',alternatives=[r'\bar\eta',r'\bar K'],confidence='low',reason='A short bar survives above dense cancellation; the underlying head and lower strokes cannot be separated reliably.'),
  dict(place='L5, live barred glyph M1038',reading=r'\unsure{\bar\eta|\bar K}',alternatives=[r'\bar\eta',r'\bar K'],confidence='low',reason='An upright/angled head and long right descent permit both readings. The complete formula does not supply a decisive graphic distinction.'),
  dict(place='L5, first tensor subscript',reading=r'\unsure{k|K}',alternatives=['k','K'],confidence='medium',reason='The small stem-and-arms form has no securely diagnostic lowercase loop; its case is not derived from the base field or the later formula.'),
  dict(place='L8, map connector in the complete second display',reading=r'\unsure{\longrightarrow|-}',alternatives=[r'\longrightarrow','headless shaft'],confidence='medium',reason='One shaft ends in a tiny capped/upright cluster; two separate arrowhead branches or a definite right point cannot be made out.'),
  dict(place='L8, crossed glyph after the target parenthesis',reading=r'\deleted{\unsure{K|\bar\eta}}',alternatives=['K',r'\bar\eta'],confidence='low',reason='K-like arms favor the first reading, but several crossing strokes obscure the upper and inner construction.'),
  dict(place='L10, lower shaft beneath lim in the K-prime formula',reading=r'\unsure{\varinjlim|\underset{-}{\lim}}',alternatives=[r'\varinjlim',r'\underset{-}{\lim}'],confidence='medium',reason='The lower line has a tiny thickened/downturned endpoint, insufficient to distinguish a full arrowhead from a terminal pen return.'),
  dict(place='L13, crossed word replaced by réguliers',reading=r'\deleted{\unsure{normaux}}',alternatives=['normaux','medial letters obscured by the cancellation'],confidence='medium',reason='The initial low humps and terminal x-like crossing fit normaux; the middle is crossed by both the cancellation and the replacement’s descender/attachment. Not every letter is plain.'),
  dict(place='L16, punctuation after donc',reading=r'\unsure{:|..}',alternatives=['colon','two points'],confidence='medium',reason='Exactly two dark points descend obliquely to the right, with comparable horizontal and vertical separation; there is no third point.'),
  dict(place='L18, crossed glyph in the complete paired-arrow formula',reading=r'\deleted{\unsure{K|k}}',alternatives=['K','k'],confidence='medium',reason='The heavily overtraced stem and arms do not securely establish case; the surrounding live pi index and barred U argument remain visible.')
 ],
 audit_boxes=audit,diff_coverage=coverage)
(root/'edition/reviews/149_scan023.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan023 proposal/report:',len(changes),'changes;',len(inventory),'inventory elements;',len(audit),'audit boxes;',len(coverage),'difference rows.')
