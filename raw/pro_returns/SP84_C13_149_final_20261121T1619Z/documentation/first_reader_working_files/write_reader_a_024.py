from pathlib import Path
import json
P=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads((P/'work/149_scan024_reader_a_crop_boxes.json').read_text())['boxes']
def crop(n): return f'crops/149_scan024_c{n:02d}.png'
def box(n): return boxes[str(n)]
tex=r'''\scanpage{24}
\uline{\unsure{Corollaire|Corollaires}} ``purement \unsure{géométrique|géométriques}'':

\uline{Corollaire} 1 Soient $X,Y$ des schémas \inserted{de t.f. réduits connexes} sur un corps alg. clos, $k$, et $f,g:X\longrightarrow Y$ deux morphismes, on suppose que $\pi_1(f),\pi_1(g):\pi_1(X)\rightrightarrows\pi_1(Y)$ sont égaux (en tant qu'hom. extérieurs). Alors

a) Si $Y$ \deleted{est \unsure{une|un} extension \unsure{d'une|d'un}} \inserted{se plonge par un $i:Y\text{—}G$ en un groupe algébrique commutatif $G$} extension d'une VA par un tore, il existe un $a\in Y$ (unique) tel que $g(x)=f(x)+a$ $\forall x\in X(k)$, i.e. $(i\circ g)=\tau_a\circ(i\circ f)$ ($\tau_a$ la translation par $a$).

b) Si $Y$ est une variété élémentaire d'\unsure{Artin} ou \deleted{\unsure{une}} \unsure{fibrée|fibrées} \unsure{successive|successives} des \unsure{courbes} anabéliennes, \inserted{et $X$ \deleted{normal} \inserted{irred} et si $f$ ou $g$ est dominant,} alors $f=g$.

\margin{\uuline{b)} \unsure{\deleted{Ce cas n'est prouvé qu'en car. $0$ \unsure{pour les courbes}; en car. \unsure{$p>0$}, on ne sait \unsure{rien sur la} structure du $\pi_1$ (\unsure{pro-$p$}, \unsure{pro-prime à $p$}), \unsure{et même} les centres des $\pi_1$\ldots}}}
\margin{Une conjecture forte établirait l'unicité des morphismes, avec $X$ irréductible et \unsure{quels} \illegible{1} applications $f,g$, \unsure{sans les supposer|faut les supposer} \unsure{dominantes|dominant}.}
\margin{En fait dans a) il suffit de supposer que $H_1(f,\mathbb Z_\ell)=H_1(g,\mathbb Z_\ell)$ pour un $\ell$ premier à la car. \deleted{\unsure{exp.}}}

\uline{Démonstration} a) L'unicité de $a$ est claire -- et \deleted{il} \inserted{l'existence} revient, \inserted{remplaçant $Y$ par $G$ et} en choisissant une ``origine'' $a\in X(k)$, et en se ramenant au cas $f(a)=g(a)=0$, à prouver qu'alors $f=g$. D'ailleurs l'hyp. $\pi_1(f)=\pi_1(g)$ peut être affaiblie en l'hyp. que \deleted{\unsure{$f_1$|$f$} est} $H_1(f,\mathbb Z_\ell)=H_1(g,\mathbb Z_\ell)$, \inserted{$\ell$ premier à car.} -- \unsure{i.e.|ici} il suffit
\margin{23}
'''
(P/'edition/reviews/149_scan024.tex').write_text(tex)
changes=[]
def ch(place,C,H,final,evidence,n,confidence='high',ac=False,ah=True,kind='misread word',category='Words',marked=False,math=False):
    ident=f'c{len(changes)+1:02d}'
    changes.append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=evidence,crop=crop(n),box=box(n),confidence=confidence,against_C=ac,against_H=ah,kind=kind,error_category=category,marked_in_H=marked,mathematical=math))
    return ident
ids={}
ids['heading']=ch('Title, first word',r'\uline{Corollaires}',r'\struck{Corollaire}',r'\uline{\unsure{Corollaire|Corollaires}}','The long underline is below the word. Heavy black strokes retrace individual letter bodies rather than crossing the word uniformly. After the dotted i the compressed re-ending has a returning loop, but no securely separable final s. The singular is provisionally first; the plural remains possible.',1,'medium',True,True,'deletion state','Struck text')
ids['geometry']=ch('Title, quoted phrase',r"``purement géométriques''",'« purement géométrique »',r"``purement \unsure{géométrique|géométriques}''",'Both quotation marks consist of paired high pen strokes, not angled guillemets. The last low run after the q-descender can be the ue-ending and terminal return; a separate plural s is not certain. The final colon is plainly two vertically separated dots.',2,'medium',True,True)
ids['label']=ch('Corollary label',r'\uline{Corollaire} 1',r'\textbf{Corollaire 1.}',r'\uline{Corollaire} 1','A single independent stroke underlines Corollaire. The numeral is one tall upright with a small upper lead. The white interval after it contains no stop.',3,'high',False,True,'other','Other',math=True)
ids['connexes']=ch('First statement, addition above schémas / sur un',r'\inserted{de t.f. réduits connexes} sur un',r'\add{de t.f. réduits \struck{\ill{}}} (sur un',r'\inserted{de t.f. réduits connexes} sur un','The lower added word has the connected c-o-n-n-e-x-e-s run. Its first loop touches the long insertion leader, which continues beneath the word and bends down before sur. There is no independent cancellation through the other letters and no separate opening parenthesis.',4,'high',False,True,'deletion state','Struck text',True)
ids['commas']=ch('First statement, corps alg. clos, k,',r'clos, $k$,',r'clos $k$),',r'clos, $k$,','A dark detached low comma follows the s of clos. A second descending comma follows the k; it is not a closing parenthesis paired with the insertion leader above.',5,'high',False,True,'other','Symbols and indices')
ids['par']=ch('Item a, first added row',r'se plonge par un',r'se plonge dans un',r'se plonge par un','The disputed word starts with a closed upper p-loop and a long downstroke, then an a-body and small r-like terminal rise. It has neither a d-ascender nor the four-letter dans outline.',7)
ids['shaft']=ch('Item a, inserted map',r'$i:Y\longrightarrow G$',r'$i:Y\to G$',r'$i:Y\text{—}G$','The entire map is visible: dotted i, colon, capital Y, one horizontal shaft, capital G. At the right end of the shaft there is a tiny terminal thickening/upturn, without the two branches of an arrowhead. The headless shaft is retained literally.',7,'high',True,True,'misread symbol or index','Symbols and indices',math=True)
ids['groupe']=ch('Item a, second added row and its right leader',r'en un groupe algébrique commutatif \unsure{$G$}',r'(un groupe algébrique commutatif $G$)',r'en un groupe algébrique commutatif $G$','The beginning has the short en followed by un; the following p-descender, algébrique ascenders and final commutatif t/f forms are visible. The raised terminal G has a round upper body and internal angular return. The long enclosing curve at the right continues the insertion leader; it is not an independently written closing parenthesis.',8,'high',False,True,'insertion or placement','Insertions put in the wrong place',math=True)
ids['duplicate']=ch('Item a, cancelled phrase before the live extension clause',r"\deleted{est \unsure{une|un} extension \unsure{d'une|d'un}}",r"\struck{est une extension d'une} ... \struck{\ill{} extension d'une}",r"\deleted{est \unsure{une|un} extension \unsure{d'une|d'un}}",'There is one old baseline est ... extension d\'... traversed by one long stroke, below the new insertion. H gives the same old extension phrase a second time after the insertion. No second cancelled occurrence is visible. The small old articles remain partly masked and are not resolved.',6,'medium',False,True,'text not on the page','Text that is not on the page',True)
ids['ou']=ch('Item b, after the name',r'ou',r'\ill{}',r'ou','Two low linked bowls form ou after the name and before the cancelled short article; there is no ascender or other unreadable intervening word.',9,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True)
ids['old_article']=ch('Item b, cancelled short article',r'\deleted{\unsure{une}}',r'\struck{\ill{}}',r'\deleted{\unsure{une}}','The short old word has low u/n-like arches and a small final e-like return beneath the crossing stroke. Une remains a tentative reading; the masking prevents complete resolution, but the surviving letters are recorded rather than replacing the entire unit with an illegible marker.',9,'low',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True)
ids['fibree']=ch('Item b, succession phrase',r'\unsure{fibrée successive des}',r'fibrations successives des',r'\unsure{fibrée|fibrées} \unsure{successive|successives} des','The first word has a tall f-loop, dotted i and b-ascender, followed by a short low ending. Its visible extent does not support the extra ations sequence in H. The short ending does not firmly settle a final s. The following succession word has the succ... and dotted i run, but its final return also leaves singular/plural open. The terminal des has a d-ascender and low es.',9,'medium',False,True)
ids['courbes']=ch('Item b, next baseline, first word',r'\unsure{variétés}',r'courbes',r'\unsure{courbes}','The first letters are crossed by the oblique marginal note, but the rounded c/o/u run and a later tall b form favor courbes. There is no visible t/accented-é sequence for variétés. The overlapped beginning is kept doubtful.',10,'medium',True,False)
ids['anabeliennes']=ch('Item b, next baseline, second word',r'élémentaires',r'\uncertain{anabéliennes}',r'anabéliennes','The word begins with low a-n-a forms, followed by the distinct tall b, a detached accent, tall l and dotted i, then the low ennes run. That sequence supports anabéliennes; it does not show the initial é-l of élémentaires.',10,'high',True,False,'misread word','Words',True,True)
ids['irred']=ch('Item b, replacement below cancelled normal',r'\inserted{irred.}',r'\add{réduit}',r'\inserted{irred}','The new short word begins with a dotted i and two short r-like arches, followed by a low e and upright d. Its ending is not the uit run of réduit. No detached period follows the d; the nearby long descending stroke belongs to the enclosing insertion mark.',11,'high',True,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',math=True)
ids['condition']=ch('Item b, attachment of added condition',r'\inserted{et $X$ \deleted{normal} \inserted{irred.} et si $f$ ou $g$ est dominant,}',r'\add{(et $X$ \struck{\uncertain{normal}} \add{réduit}) et si $f$ ou $g$ est dominant)}',r'\inserted{et $X$ \deleted{normal} \inserted{irred} et si $f$ ou $g$ est dominant,}','The old normal is struck through its letter bodies; the shorter replacement is written beneath it. A continuous lower leader encloses the added condition and dips down immediately before alors. Its left curve and the replacement enclosure are leaders, not a pair of textual parentheses. The condition is placed before alors.',11,'high',False,True,'insertion or placement','Insertions put in the wrong place',True,True)
ids['negative']=ch('Upper left marginal note, opening',r'Ce cas est',r'\uncertain{Un cas où} ...',r"Ce cas n'est",'The opening capital C and e are followed by cas. Before est there is an additional low n-like stroke followed by a detached high apostrophe. It reads n\'est, not est or où.',12,'high',True,True,'misread word','Words',True)
ids['quen']=ch('Upper left marginal note, second row',r'\unsure{prouvé} \unsure{par nous} en',r'\ill{}',r"prouvé qu'en",'The first word has p-descender, r/ou/v run and an accent over the final é. The next group begins with a long q-descender and has the short u, apostrophe and en run. There is no distinct par followed by a separate nous group.',12,'high',True,True,'misread word','Words',True)
upper=r"\uuline{b)} \unsure{\deleted{Ce cas n'est prouvé qu'en car. $0$ \unsure{pour les courbes}; en car. \unsure{$p>0$}, on ne sait \unsure{rien sur la} structure du $\pi_1$ (\unsure{pro-$p$}, \unsure{pro-prime à $p$}), \unsure{et même} les centres des $\pi_1$\ldots}}"
ids['upper']=ch('Upper left marginal note, full extent and state',r'\margin{\uuline{b)} \deleted{Ce cas est ... les centres des $\pi_1$\ldots}}',r'\marginal{\uncertain{Un cas où} \ill{} \uncertain{premier} \ill{} \uncertain{structure des $\pi_1$} \ill{} ...}',r'\margin{'+upper+'}', 'The separate double-underlined b) and the successive rows car. 0, courbes, en car., on ne sait, structure du pi with subscript 1, and the terminal les centres des pi with subscript 1 and three dots are present. Several intervening small words are crossed by the note and retain local doubts. The long oblique stroke crosses multiple independent baselines and ends inside this marginal block without an identifiable arrowhead or main-text attachment. It supports paragraph cancellation, but does not cross each lowest row individually; the outer doubt qualifies cancellation scope.',12,'medium',False,True,'omission','Omissions',True,True)
lower=r"Une conjecture forte établirait l'unicité des morphismes, avec $X$ irréductible et \unsure{quels} \illegible{1} applications $f,g$, \unsure{sans les supposer|faut les supposer} \unsure{dominantes|dominant}."
ids['lower']=ch('Lower left marginal note, readable opening and full separate note',r"\margin{\unsure{Une conjecture forte établirait l'unicité des} \unsure{morphismes}, avec $X$ irréductible ...}",r'\marginal{... \uncertain{l’unicité} \ill{} \uncertain{irréductibilité} \ill{}}',r'\margin{'+lower+'}', 'The separate lower note has the readable successive rows Une conjecture / forte établirait / l\'unicité des / morphismes, then avec X irréductible. The conjecture tail is also present in the overlapping c12 evidence. This note is not crossed by the cancellation of the upper note. The applications word and f,g row are separately visible. H\'s scattered tentative nouns do not transcribe these sentences. The quantifier and final qualification remain local doubts, handled in the next entry and decisions.',13,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True,True)
ids['quantifier']=ch('Lower left marginal note, after et',r'\unsure{quels que soient les}',r'\ill{}',r'\unsure{quels} \illegible{1}','After et there is a q-loop with a long descender, a compressed low run and a tall l-like stroke, provisionally quels. A following very short detached group is unreadable as a complete word at this scale. The ink does not establish all three further words que soient les, which are not supplied. The one illegible unit records that short written group, not three inferred words.',13,'low',True,True,'misread word','Words',True)
ids['enfait']=ch('Right marginal note, opening punctuation',r'En fait, dans',r'En fait, dans',r'En fait dans','After the final t of fait the next word dans begins after open space. No independent low comma is visible in that gap; the nearby larger descending loop belongs to f and the next lines.',14,'high',True,True,'text not on the page','Text that is not on the page')
ids['exp']=ch('Right marginal note, last cancelled word',r'\deleted{\unsure{exp.}}',r'(omitted)',r'\deleted{\unsure{exp.}}','A separate short final word is heavily crossed: an initial loop, a central crossed body and a descender remain, consistent with exp., but not all letters or its stop are plain. The whole cancelled word is retained with doubt.',14,'medium',False,True,'omission','Struck text')
ids['demonstration']=ch('Proof heading',r'\uline{Démonstration}',r'\emph{Démonstration.}',r'\uline{Démonstration}','The word has a long independent underline; the final low n-return is followed by blank space, without a period. The underline is not italicization in the manuscript.',15,'high',False,True,'other','Other')
ids['aextra']=ch('Proof first row, de a est',r'de $a$ est',r'de $a$ \struck{\ill{}} est',r'de $a$ est','The small a is heavily retraced, but its triangular/looped body remains in the ordinary text position. The thick lower return stays within the glyph. No separate intervening cancelled word lies between a and est.',16,'high',False,True,'text not on the page','Text that is not on the page',True)
ids['il']=ch('Proof second row, cancelled word and replacement',r'\deleted{\unsure{il}} \inserted{l’existence}',r'\add{l’existence} \struck{est}',r"\deleted{il} \inserted{l'existence}",'Under the heavy short strike there is a separate i-dot and the tall oval loop of l. The visible surviving letters support il and do not show an est sequence. The new l\'existence is above the old word, with its apostrophe, x and tall t visible. Revient on the baseline remains readable despite local retracing.',17,'high',False,True,'misread word','Struck text')
ids['remplacant']=ch('Proof, inserted clause before en choisissant',r'\inserted{remplaçant $Y$ par $G$ et} en choisissant',r'(en choisissant \add{remplaçant $Y$ par $G$ et,}',r'\inserted{remplaçant $Y$ par $G$ et} en choisissant','The inserted remplaçant Y par G et lies above the baseline and its continuous leader bends down before en. En choisissant remains on the baseline in that order. The curve before en is attached to the leader and is not an opening parenthesis; the upturn after et is the other end of that same leader, not a comma.',18,'high',False,True,'insertion or placement','Insertions put in the wrong place')
ids['origine']=ch('Proof, quotation marks around origine',r"``origine''",r'« origine »',r"``origine''",'The opening is two high short pen strokes. The closing mark has two joined short lobes. Neither side has the angled chevron strokes of guillemets.',19,'high',False,True,'other','Other')
ids['findex']=ch('Proof, cancelled phrase before the homology equality',r'\deleted{$f$ est}',r'\struck{$f_1$ \ill{}}',r'\deleted{\unsure{$f_1$|$f$} est}','The large looped f is crossed at its lower body. A separate short low upright to its right favors an index 1, but the cancellation and overlapping return prevent certainty. The following e-loop and s/t strokes support est; that word is not wholly illegible. Both f-index alternatives are retained.',20,'medium',True,True,'misread symbol or index','Symbols and indices',True,True)
ids['ell']=ch('Proof last row, appended prime condition and attachment',r'\inserted{$\ell$ premier à car.,}',r'\add{\uncertain{$\ell$ premier à la car.}} before the equality',r'\inserted{$\ell$ premier à car.}','The small added line reads looped ell, premier, à, car. and is linked down after the homology equality. There is no separate la between à and car.; the tall loop crossing that interval comes from the lower baseline. The curved hook after car. joins the insertion leader and does not supply an extra comma. The ordinary comma after the equality remains outside the insertion.',21,'high',True,True,'insertion or placement','Insertions put in the wrong place',True,True)
ids['tail']=ch('Proof last row, after the added prime condition',r'car ici',r'— i.e.',r'-- \unsure{i.e.|ici}','A separate horizontal dash precedes the next group. The group begins with a dotted i, a very small middle speck/curve, then an open e/c-like form and a terminal stop. I.e. is favored over C\'s ici, but the compact intermediate strokes leave a localized reading doubt. There is no car word at this baseline position.',21,'medium',True,False,'misread word','Words')
ids['folio']=ch('Bottom left pen folio',r'\margin{23}',r'(omitted)',r'\margin{23}','The thin first numeral has an upper curve, diagonal descent and long lower horizontal for 2; the next numeral has two rightward bowls for 3. This is the pen folio 23, distinct from scan metadata 24.',22,'high',False,True,'omission','Omissions')

decisions=[]
def dec(mid,decision,reading,evidence,n,confidence):
    decisions.append(dict(id=mid,decision=decision,reading=reading,evidence=evidence,crop=crop(n),box=box(n),confidence=confidence))
dec('M1039','first',r'$G$','The raised terminal sign has a large round upper body and the internal angular return of the G in the preceding map; it is not just the enclosing leader.',8,'high')
dec('M1040','undecided',r'\unsure{Artin}','A large A, subsequent r/t strokes, dotted i and low ending favor Artin. The angled marginal text crosses the name and prevents every letter being independently plain.',9,'medium')
dec('M1041','undecided',r'\unsure{fibrée|fibrées} \unsure{successive|successives} des','The f-i-b opening and short ending exclude a confident expansion to fibrations. The endings of both words remain compressed; des is readable. Keep the local singular/plural alternatives.',9,'medium')
dec('M1042','other',r'\unsure{courbes}','The rounded initial run and tall internal b support courbes, while marginal overlap masks part of the opening. No reliable variétés outline is visible.',10,'medium')
dec('M1043','first',r"Une conjecture forte établirait l'unicité des",'The successive lines show Une with capital U, conjecture with long j-descender, forte with tall f/t, établirait with its ascenders and accent, and l\'unicité des with its apostrophe, dotted i and accented ending. The top-right tail is also available in overlapping c12.',13,'high')
dec('M1044','first',r'morphismes','The separate row has m-o-r-p-h, including the p-descender and h-ascender, then dotted i and the smes run, followed by a comma.',13,'high')
dec('M1045','other',r'\unsure{quels} \illegible{1}','The long q-descender and compact group can be quels; the following very short detached group cannot be read as a complete word. No full que soient les sequence is established. The unreadable unit is not silently expanded.',13,'low')
dec('M1046','first',r'applications','The word has the paired p-descenders, tall l, dotted i, c/a/t run and terminal ions strokes. These belong to one complete word, applications.',13,'high')
dec('M1047','undecided',r'\unsure{sans les supposer|faut les supposer}','The low initial run favors sans, but the long q-descender from the row above crosses it and could be mistaken for an f-ascender. Les and the double p-descenders in supposer are visible; the disputed opening remains unresolved.',13,'low')
dec('M1048','undecided',r'\unsure{dominantes|dominant}','The beginning and central dom...nant run are heavily retraced. The terminal upright and small return do not securely distinguish antes from ant. The expected agreement is not supplied.',13,'low')

inventory=[]
def inv(element,kind,position,first,hand='manuscript hand'):
    inventory.append(dict(scan=24,sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('title','text','top, first baseline','Corollaire(s) purement géométrique(s)')
inv('corollary_statement','text','upper main block','Corollaire 1 Soient X,Y')
inv('statement_addition','insertion','above schémas / before sur un','de t.f. réduits connexes')
inv('item_a','text','upper-middle main block','a) Si Y')
inv('item_a_old_phrase','deletion','after Si Y, old baseline',"est une/un extension d'une/d'un")
inv('item_a_replacement','insertion','two rows above the old phrase','se plonge par un i:Y—G en un groupe')
inv('item_b','text','middle main block','b) Si Y est une variété')
inv('item_b_old_article','deletion','between ou and the short fibration phrase','une')
inv('item_b_condition','insertion','above alors f=g, connected down by leader','et X normal / irred et si f ou g')
inv('item_b_old_adjective','deletion','within the added condition','normal')
inv('item_b_new_adjective','insertion','under normal','irred')
inv('upper_left_note','margin note','oblique upper-left note beside item b','double-underlined b), Ce cas n’est')
inv('upper_left_note_cancellation','deletion','oblique stroke across upper-left note; paragraph scope uncertain','Ce cas n’est prouvé qu’en')
inv('lower_left_note','margin note','oblique lower-left note beside proof','Une conjecture forte établirait')
inv('right_note','margin note','oblique right margin beside item b and proof heading','En fait dans a) il suffit')
inv('right_note_cancelled_tail','deletion','last row of right note','exp. (doubtful)')
inv('proof','text','lower main block, continues off leaf','Démonstration a) L’unicité de a')
inv('proof_old_pronoun','deletion','after claire -- et','il')
inv('proof_new_subject','insertion','above deleted il',"l'existence")
inv('proof_change_of_target','insertion','above en choisissant, attached before en','remplaçant Y par G et')
inv('proof_old_formula_phrase','deletion','after en l’hyp. que','f_1 / f est')
inv('proof_prime_condition','insertion','above last baseline, attached after H_1 equality','ell premier à car.')
inv('folio','text','bottom left','23','thin pen foliation; hand attribution not established')

notes=[
    'Reader: /root/reader_a; GPT-6 Astra Pro; effort not exposed; run SP84_C13_149. Scan 024 only. No external research, OCR, TeX compilation, or mathematical proof checking was performed.',
    'Layout: one handwritten text sheet; heading, corollary statement, items a and b, three oblique marginal notes, and the beginning of a proof. No separate diagram or drawing is present. Thin bottom-left foliation reads 23; scan metadata is 24.',
    'Reading count: 57 physical lines/rows inspected: 21 title and main baselines, 9 separate interlinear addition rows, 9 rows in the upper-left note, 8 in the lower-left note, 9 in the right note including its struck tail, and one folio row. Whole source and each prepared half were viewed once; all 22 saved detail crops were personally read.',
    'S024.1 (transcribed claim, not checked): the corollary begins with two morphisms f,g whose displayed fundamental-group maps are equal as exterior homomorphisms. Item a concerns an insertion describing a map of Y into a commutative algebraic group and a translation parameter. The source says a in Y; it has not been changed to G. The i:Y—G shaft has no clear head and is rendered literally.',
    'S024.2 (transcribed claim, not checked): item b concerns an elementary variety/name and a short, partly uncertain fibration phrase followed by courbes anabéliennes. A condition on X and dominance is added before the stated f=g conclusion. Normal is cancelled within that insertion and replaced by the written short form irred without a period.',
    'The upper-left note begins Ce cas n’est prouvé qu’en, differing from C’s est / par nous. Its double-underlined b) is separate. A long oblique stroke traverses several independent rows and ends within the note, supporting cancellation, but does not individually cross the lowest rows. The outer unsure around deleted qualifies that paragraph-level scope, not a claim that every lower letter carries a strike. Local masked words and the p>0 formula remain doubtful.',
    'The lower-left note is live and separate from the upper cancellation. Its opening Une conjecture forte établirait l’unicité des morphismes and avec X irréductible are readable. After et the compact group does not establish C’s entire quels que soient les; the proposed fragment preserves the tentative quels plus one unreadable written group. No expected quantifier is silently supplied. The sans/faut and dominant ending remain local doubts.',
    'S024.3 (transcribed claim, not checked): the right note states a homology equality condition involving H_1 and Z_ell, followed by a prime-to-characteristic phrase and a heavily struck short tail. The Z signs have a second diagonal return supporting the witnesses’ double-stroke rendering; no alphabet normalization was made merely from agreement.',
    'S024.4 (transcribed proof opening, not checked): the proof first discusses uniqueness of a, replaces il with l’existence, and adds remplaçant Y par G et before en choisissant. The cancelled phrase before H_1 favors an f with low index 1 but preserves f as an alternative. The final added ell condition is attached after the equality; the page ends after a dash and a doubtful i.e./ici group followed by il suffit.',
    'Quotation marks are paired pen ticks, rendered as two backticks and two apostrophes. Insertion leaders near sur un, the item-a group, the condition before alors, and en choisissant are not supplied as textual parentheses. H’s editorial observations about the preceding page are excluded from the source fragment.',
    'No cross-page source comparisons were made. All local resolutions rely on this leaf and its packet notation snapshot. Any confidence-only changes are recorded in decisions/doubts rather than counted as substantive changes.'
]
hand=[
    dict(habit='Heavy retracing of a letter can leave a dark baseline without cancelling the word.',pages='024',consistency='Verified in the title word and the a of L’unicité de a; separate independent strikes elsewhere have different extent.',misread='H strikes the title and inserts an illegible cancelled unit after the proof’s a.'),
    dict(habit='Long enclosing insertion leaders bend down to the attachment point and can resemble opening/closing parentheses or commas.',pages='024',consistency='Verified above sur un, in the item-a insertion, the condition before alors, before en choisissant, and after the final prime condition.',misread='H supplies parentheses at several leaders and moves the remplaçant clause; C supplies a comma after the final leader hook.'),
    dict(habit='A short p-descender and final r distinguish par from a compact dans.',pages='024',consistency='Verified in the item-a insertion; no general claim beyond this occurrence.',misread='H reads dans for par.'),
    dict(habit='Compressed re/ue and final low returns do not reliably distinguish singular from a final s.',pages='024',consistency='Title Corollaire(s), géométrique(s), and the fibration phrase remain locally unresolved; comparison to the singular Corollaire label does not settle them.',misread='C and H disagree on the title endings; neither witness is adopted as certain.'),
    dict(habit='A q-descender from an upper oblique row can enter a lower word and resemble an f-ascender.',pages='024',consistency='Visible in the lower-left note at the quantifier and sans/faut rows; limits the reading there.',misread='The lower note’s sans/faut choice remains unresolved rather than completed by grammar.'),
    dict(habit='Paired high ticks are used for double quotation marks.',pages='024',consistency='Verified at the title phrase and origine.',misread='H prints guillemets.'),
    dict(habit='The written short replacement irred has no independent stop.',pages='024',consistency='One local occurrence beneath normal; terminal enclosure is distinct from punctuation.',misread='C supplies irred.; H reads réduit.')
]
notation=[
    dict(written='one horizontal shaft between Y and G, tiny terminal upturn without two branches',rendering=r'$i:Y\text{—}G$',meaning='written map-like expression in the insertion; literal shaft shape retained',evidence='024 c07, whole expression from i through G'),
    dict(written='pi forms with low numeral 1',rendering=r'$\pi_1$',meaning='fundamental-group notation as used in the statement, margins and proof',evidence='024 prepared halves and upper-left note c12; every instance checked and boxed'),
    dict(written='H with low 1 and coefficient Z carrying ell',rendering=r'$H_1(f,\mathbb Z_\ell)$',meaning='homology notation in the right note and final proof line',evidence='024 right note c14 and lower half; Z has a visible second diagonal return'),
    dict(written='tau with low a',rendering=r'$\tau_a$',meaning='the source calls it la translation par a',evidence='024 upper half, item a formula and following parenthesis'),
    dict(written='thin pen 23',rendering=r'\margin{23}',meaning='physical folio written at bottom left; distinct from scan number',evidence='024 c22')
]
abbreviations=[
    dict(form='t.f.',expansion='type fini',place='addition above schémas'),
    dict(form='alg.',expansion='algébriquement',place='corps alg. clos'),
    dict(form='hom.',expansion='homomorphismes',place='hom. extérieurs'),
    dict(form='VA',expansion='variété abélienne',place='item a'),
    dict(form='i.e.',expansion='id est',place='item a; final proof group remains doubtful'),
    dict(form='irred',expansion='irréductible',place='replacement below normal in item b'),
    dict(form='car.',expansion='caractéristique',place='upper-left note, right note and last proof addition'),
    dict(form='hyp.',expansion='hypothèse',place='proof'),
    dict(form='exp. (doubtful)',expansion='exponentielle, only a possible expansion if the struck letters are exp.',place='right-note cancelled tail')
]
doubts=[
    dict(place='Title, first word',reading='Corollaire',alternatives=['Corollaires'],confidence='medium',reason='Independent underline is clear; the heavily retraced final return does not settle a separate s. c01.'),
    dict(place='Title, adjective',reading='géométrique',alternatives=['géométriques'],confidence='medium',reason='After the q-descender the compressed ue/return can conceal a final s. c02.'),
    dict(place='Item a, first cancelled article',reading='une',alternatives=['un'],confidence='low',reason='The cancellation masks the low ending. Retained C doubt; certainty-only, no substantive change. c06.'),
    dict(place='Item a, second cancelled article',reading="d'une",alternatives=["d'un"],confidence='low',reason='The old small letters lie under the continuous crossing stroke. Retained C doubt. c06.'),
    dict(place='Item a, terminal G in addition',reading=r'$G$',alternatives=[],confidence='high',reason='C doubt resolved by round body and angular return, comparable to G earlier in the same insertion. Certainty-only. c08.'),
    dict(place='Item a, unique',reading='(unique)',alternatives=[],confidence='high',reason='Both parentheses and the low letters with q-descender and dotted i are visible in the upper half; H’s doubt does not alter the reading.'),
    dict(place='Item b, name',reading='Artin',alternatives=[],confidence='medium',reason='Favors A-r-t-i-n, but angled marginal strokes overlap some letters. Retained C doubt. c09.'),
    dict(place='Item b, cancelled article',reading='une',alternatives=[],confidence='low',reason='Short u/n/e run is visible through cancellation but not every letter is plain. Retained C doubt. c09.'),
    dict(place='Item b, short succession words',reading='fibrée successive des',alternatives=['fibrées successives des','mixed singular/plural endings'],confidence='medium',reason='Short f-i-b... word lacks H’s full ations run; the two terminal returns do not settle final s. c09.'),
    dict(place='Item b, courbes',reading='courbes',alternatives=[],confidence='medium',reason='Tall internal b and rounded run favor the reading; first letters overlap the upper marginal note. c10.'),
    dict(place='Upper-left marginal note, deletion scope',reading='paragraph-level cancellation',alternatives=['a more limited cancelled span across the traversed rows'],confidence='medium',reason='Oblique stroke crosses several independent baselines without a main-text attachment, but does not individually strike every lowest row. The outer unsure explicitly qualifies this scope. c12.'),
    dict(place='Upper-left note, after car. 0',reading='pour les courbes',alternatives=[],confidence='low',reason='Some low letters are crossed by the oblique cancellation and adjacent writing. Retained local C doubt. c12.'),
    dict(place='Upper-left note, positive-characteristic formula',reading=r'$p>0$',alternatives=[],confidence='low',reason='The p and 0 are visible; the intervening relation is crowded at a crossing. Whole formula retained under doubt and included in whole-note audit. c12.'),
    dict(place='Upper-left note, after on ne sait',reading='rien sur la',alternatives=[],confidence='low',reason='Compact connected forms meet the crossing stroke and main-text intrusions. Retained C doubt. c12.'),
    dict(place='Upper-left note, parenthetical labels',reading=r'(pro-$p$, pro-prime à $p$)',alternatives=[],confidence='low',reason='Large intruding strokes mask parts of both short labels; no completion beyond C’s qualified reading. Whole parenthetical expression is in the note audit. c12.'),
    dict(place='Upper-left note, before les centres',reading='et même',alternatives=[],confidence='low',reason='The small joining letters are partly masked. Retained C doubt. c12.'),
    dict(place='Lower-left note, opening',reading="Une conjecture forte établirait l'unicité des morphismes",alternatives=[],confidence='high',reason='Resolved C doubts from separate readable rows; this certainty change alone is not a change row against C. c13 plus overlapping c12.'),
    dict(place='Lower-left note, quantifier',reading=r'\unsure{quels} \illegible{1}',alternatives=['unresolved short quantifier group'],confidence='low',reason='The initial q/l-like group is compressed, and the following small written unit cannot be read. C’s full que soient les sequence is not established. c13.'),
    dict(place='Lower-left note, applications',reading='applications',alternatives=[],confidence='high',reason='Paired p-descenders, l, dotted i and terminal ions are readable. Certainty-only resolution of C. c13.'),
    dict(place='Lower-left note, qualification',reading='sans les supposer',alternatives=['faut les supposer'],confidence='low',reason='The long q-descender above passes through the first word; subsequent les supposer is readable. c13.'),
    dict(place='Lower-left note, last word',reading='dominantes',alternatives=['dominant'],confidence='low',reason='Heavy retracing and terminal upright/return prevent secure ending. c13.'),
    dict(place='Right note, cancelled tail',reading='exp.',alternatives=[],confidence='low',reason='Initial loop, central crossing and descender survive but not all letters/stop. Retained C doubt. c14.'),
    dict(place='Proof, cancelled il',reading='il',alternatives=[],confidence='high',reason='Separate i-dot and tall l-loop survive the strike; C’s first reading resolves on c17, H’s est differs substantively.'),
    dict(place='Proof, revient',reading='revient',alternatives=[],confidence='high',reason='The r, e/v run, dotted i and tall final t are visible despite retracing; H’s uncertainty does not change the adopted word. c17.'),
    dict(place='Proof, cancelled f',reading=r'$f_1$',alternatives=[r'$f$'],confidence='medium',reason='A short detached low upright favors index 1 but overlaps strike/return. Whole cancelled formula phrase is boxed. c20.'),
    dict(place='Proof, final abbreviation',reading='i.e.',alternatives=['ici'],confidence='medium',reason='Dotted i, small middle mark and open terminal e/c with a stop favor i.e.; the compact stroke sequence is not fully decisive. c21.')
]

audit=[]
def ab(kind,coords,reading):
    audit.append(dict(box=f'b{len(audit)+1:02d}',kind=kind,x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
ab('prose',[282,74,1227,196],r"\uline{\unsure{Corollaire|Corollaires}} ``purement \unsure{géométrique|géométriques}'':")
ab('handwritten number',box(3),r'\uline{Corollaire} 1')
ab('insertion',box(4),r'\inserted{de t.f. réduits connexes} sur un')
ab('prose',box(5),r'clos, $k$,')
ab('formula',[290,412,1610,615],r'$\pi_1(f),\pi_1(g):\pi_1(X)\rightrightarrows\pi_1(Y)$')
ab('deletion',box(6),r"\deleted{est \unsure{une|un} extension \unsure{d'une|d'un}}")
ab('insertion',[610,613,1665,790],r'\inserted{se plonge par un $i:Y\text{—}G$ en un groupe algébrique commutatif $G$}')
ab('prose',[275,1220,1500,1580],r"b) Si $Y$ est une variété élémentaire d'\unsure{Artin} ou \deleted{\unsure{une}} \unsure{fibrée|fibrées} \unsure{successive|successives} des \unsure{courbes} anabéliennes, \inserted{et $X$ \deleted{normal} \inserted{irred} et si $f$ ou $g$ est dominant,} alors $f=g$.")
ab('insertion',box(11),r'\inserted{et $X$ \deleted{normal} \inserted{irred} et si $f$ ou $g$ est dominant,}')
ab('deletion and insertion',[760,1375,922,1463],r'\deleted{normal} \inserted{irred}')
ab('margin note',[20,1285,563,1785],r'\margin{'+upper+'}')
ab('margin note',[15,1640,425,2300],r'\margin{'+lower+'}')
ab('margin note',[1372,1215,1670,1855],r'\margin{En fait dans a) il suffit de supposer que $H_1(f,\mathbb Z_\ell)=H_1(g,\mathbb Z_\ell)$ pour un $\ell$ premier à la car. \deleted{\unsure{exp.}}}')
ab('prose',box(15),r'\uline{Démonstration}')
ab('prose',box(16),r'de $a$ est')
ab('deletion and insertion',box(17),r"\deleted{il} \inserted{l'existence} revient,")
ab('insertion',box(18),r'\inserted{remplaçant $Y$ par $G$ et} en choisissant')
ab('prose',box(19),r"``origine''")
ab('formula',[295,1855,1560,2025],r'$f(a)=g(a)=0$')
ab('formula',[760,1935,1560,2070],r'$\pi_1(f)=\pi_1(g)$')
ab('deletion',box(20),r'\deleted{\unsure{$f_1$|$f$} est}')
ab('formula',[300,2110,1070,2310],r'$H_1(f,\mathbb Z_\ell)=H_1(g,\mathbb Z_\ell)$')
ab('insertion',[960,2110,1537,2292],r'\inserted{$\ell$ premier à car.} -- \unsure{i.e.|ici} il suffit')
ab('handwritten number',box(22),r'\margin{23}')

coverage=[]
def cv(row,classification,cid,reason): coverage.append(dict(row=row,classification=classification,change_id=cid,reason=reason))
cv(1,'material',ids['heading'],'Heading singular/plural and underline/cancellation are adjudicated on c01; C scan 24 is metadata and H’s preceding-page note is editorial, not source. Quotation shape also handled in '+ids['geometry']+'.')
cv(2,'material',ids['geometry'],'Adjective ending remains local singular/plural doubt; paired tick quotations are retained.')
cv(3,'material',ids['label'],'No stop follows numeral 1; label underline is represented.')
cv(4,'material',ids['connexes'],'Connexes is readable live insertion text; the curve before sur un is its leader, not a parenthesis.')
cv(5,'material',ids['commas'],'Independent comma after clos is present.')
cv(6,'material',ids['commas'],'The mark after k is a comma, not H’s added closing parenthesis.')
cv(7,'reading-agrees',None,'The first cancelled article is retained as une|un under doubt; difference is certainty/alternative only. c06 evidence is cited in doubts and the cancellation change.')
cv(8,'reading-agrees',None,'The second cancelled article is retained as d’une|d’un under doubt; no certainty-only substantive change row. c06.')
cv(9,'material',ids['par'],'The p-descender and r-ending give par. The whole inserted map’s headless shaft is separately recorded in '+ids['shaft']+'.')
cv(10,'material',ids['groupe'],'En un is visible; the enclosing curve is an insertion leader.')
cv(11,'material',ids['duplicate'],'H’s duplicated cancelled extension phrase and the supplied closing parenthesis are not independent source text; see also '+ids['groupe']+'.')
cv(12,'material',ids['upper'],'This long alignment span contains item b and the margins. Every difference is covered by '+', '.join(ids[k] for k in ['ou','old_article','fibree','courbes','anabeliennes','irred','condition','negative','quen','upper','lower','quantifier','enfait'])+'. Source order follows C’s main-text/margin treatment; all three margins remain separate.')
cv(13,'material',ids['exp'],'Cancelled exp-like tail omitted in H is retained. The reordered item-b/margin span is exhaustively covered by the same item-b and margin changes listed for row 12; the proof heading is covered by '+ids['demonstration']+'.')
cv(14,'material',ids['demonstration'],'No period after Démonstration; independent underline.')
cv(15,'macro-only',None,'C double hyphen and H long dash represent the same written dash after claire; no substantive difference.')
cv(16,'material',ids['il'],'Cancelled il is visible beneath inserted l’existence; H’s wording/order is corrected. H’s extra supposed cancellation after a is separately excluded in '+ids['aextra']+'.')
cv(17,'material',ids['il'],'H est is the same short cancelled unit; i-dot and l-loop support il.')
cv(18,'material',ids['remplacant'],'The curve is a leader; the remplaçant addition attaches before en choisissant.')
cv(19,'material',ids['remplacant'],'Baseline en choisissant follows the added clause. The hook after et is not a comma.')
cv(20,'material',ids['origine'],'The source has paired ticks, not guillemets.')
cv(21,'material',ids['findex'],'The cancelled phrase is f_1/f est, with index doubt. The ell addition belongs after the following equality and is covered by '+ids['ell']+'.')
cv(22,'material',ids['ell'],'Ell prime condition is restored to its post-equality attachment. H’s dash and abbreviated group are handled in '+ids['tail']+'.')
cv(23,'material',ids['tail'],'There is a dash and doubtful i.e./ici, not car ici. The additional comma after car. is a leader hook, as recorded in '+ids['ell']+'.')
cv(24,'material',ids['folio'],'Thin pen folio 23 is included; H omitted it.')
report=dict(scan=24,reader='/root/reader_a',lines_read=57,changes=changes,decisions=decisions,inventory=inventory,notes=notes,checks=[],hand=hand,notation=notation,abbreviations=abbreviations,doubts=doubts,audit_boxes=audit,diff_coverage=coverage)
(P/'edition/reviews/149_scan024.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert len(coverage)==24
assert len(decisions)==10
assert len({v['box'] for v in audit})==len(audit)
assert all((P/'edition'/v['crop']).exists() for v in changes+decisions)
assert all(v['against_C'] or v['against_H'] for v in changes)
assert '\\prime' not in tex
assert tex.count('{')==tex.count('}')
print(json.dumps({'saved':['edition/reviews/149_scan024.tex','edition/reviews/149_scan024.json'],'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),'audit_boxes':len(audit),'diff_rows':len(coverage),'lines_read':57},ensure_ascii=False))
