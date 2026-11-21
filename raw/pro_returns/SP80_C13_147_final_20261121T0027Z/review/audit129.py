from edition.scripts.root_audit import Audit

a=Audit(129)
oldbracket=r"\overbrace{\mathcal D_r\longrightarrow D_*}^{\inserted{\text{morphismes ``premier sommet''}}}"
newbracket=r'''\overset{\inserted{\text{morphismes ``premier sommet''}}}{
\begin{tikzpicture}[baseline=(m.base)]
\node[inner sep=0pt] (m) {$\mathcal D_r\longrightarrow D_*$};
\draw[line width=.3pt] ([xshift=-3pt,yshift=2pt]m.north west)
.. controls ([xshift=-6pt,yshift=7pt]m.north west) and ([xshift=-3pt,yshift=10pt]m.north west) .. ([yshift=10pt]m.north west)
-- ([yshift=10pt]m.north east)
.. controls ([xshift=3pt,yshift=10pt]m.north east) and ([xshift=5pt,yshift=11pt]m.north east) .. ([xshift=5pt,yshift=14pt]m.north east);
\end{tikzpicture}}'''
oldrange=r'd_0\geq d_1\cdots\geq d_r\geq0'
newrange=r'd_0\geq d_1\mathord{\cdot\,-\,-}\geq d_r\geq0'
oldtuple=r'D_{d_0,\ldots,d_r}'
newtuple=r'D_{d_0,\mathord{\cdot\,-\,\cdot},d_r}'
f=a.comparison['B01']['first'].replace(oldbracket,newbracket).replace(oldrange,newrange).replace(oldtuple,newtuple).replace(r'\mathbf N',r'\mathbb N')
a.change('B01',f,'The bound after d_1 has one point and two short strokes, with no intervening inequality. The lower defining-map source has three separated marks: point, short stroke, point. The N has two close left strokes separated by white space. The first short connector has only its upward end turn; the following two maps have full rightward heads. The left brace ends before i.e. The annotation line has a downward left curve, a horizontal span and an upward right curl, without the central cusp supplied by an overbrace.')
a.replace(a.comparison['B01']['first'],f)
a.update_row(0,'B01',final=newrange,against_C=True)
a.update_row(1,'B01',final=f)
a.add_row('B01','(206), natural-number alphabet',r'\mathbf N',r'\mathbb{N}',r'\mathbb N','high','symbol','alphabet',True,False)
a.add_row('B01','(206), source tuple after défini par les',oldtuple,r'D_{d_0,\dots,d_r}',newtuple,'high','symbol','continuation shapes',True,True)
f=a.comparison['B02']['first'].replace(oldbracket,newbracket)
a.change('B02',f,'The raised first word begins with low m joins and has the o/r/p/h sequence of morphismes, not the initial a plus paired p descenders of applications. The line beneath the caption runs over the map with asymmetric curved ends and no central brace cusp. That line is drawn literally while retaining the raised caption and full rightward map head.')
a.update_row(3,'B02',final=newbracket)
a.keep('B03','The small diagram has three filled points: isolated0, upper0 and lower1. The diagonal has a complete head; the upper vertical segment is headless. The next segment ends in a short leftward hook rather than a complete two-wing head, and the last downward arrow has a complete head. The numbers, vertical continuation marks and enclosing prose parentheses retain their first arrangement.')
oldannot=r'\overbrace{P_{d_0}}^{G_d\text{-torseur}}'
newword=r'\unsure{\text{torseur}|\text{fibré}|\text{fibrés}}'
newannot=r'\overset{\underbrace{G_d\text{-}'+newword+r'}}{P_{d_0}}'
f=a.comparison['B04']['first'].replace(oldannot,newannot)
a.change('B04',f,'The annotation has G with one lower d and no additional0. Its first tall crossed stroke and compressed subsequent joins favor torseur, but the alternative f/i/b/r/é segmentation cannot be excluded. The bracket is beneath the wide annotation and turns down toward P, so it is represented as an underbrace of the annotation above P. The written du, lower brace, single and paired continuation strokes, restriction bar and short downward connector finish remain as first read.')
a.replace(a.comparison['B04']['first'],f)
a.update_row(7,'B04',final=newannot,confidence='medium',against_C=True)
a.doubt('(207), word in the G_d annotation',newword,'The tall crossed initial and following joined loops favor torseur, but fibré/fibrés cannot be excluded from the compressed word. No grammatical role decides the reading.','medium')
a.keep('B05','The baseline begins with c and an apostrophe followed by an e-like loop; later strokes merge with the insertion leader. A distinct full a/i/e/n sequence for c-é-taient is not separable. The first uncertain c-est and raised là|sont remain unresolved, without adding letters from the proposed longer word.')
f=r'les Groupes, \unsure{analytiques|analytiq}'
a.change('B06',f,'The first word has a tall l loop and no initial d bowl. Groupes begins with the large capital curve over a retraced lower loop. A detached descending curved mark follows its final letter before the next word: this comma was missing in the first reading. The visible a/n/a/l/y/t/i/q-like body continues to the scan edge, so the existing analytique-ending uncertainty remains.')
a.replace(a.comparison['B06']['first'],f)
a.add_row('B06','Comma after Groupes','Groupes analytiques','groupes analytiques',r'Groupes, \unsure{analytiques|analytiq}','high','punctuation','omitted comma',True,True)
oldend=r'G^*_{d_0,-,d_r}&=G_{d_0,-,d_r}\mid D^*_{d_0,-,d_r}.'
newend=oldend[:-1]+r'\unsure{.|-}'
f=a.comparison['B07']['first'].replace(oldend,newend)
a.change('B07',f,'Each of the five continuation marks is one horizontal stroke. The small base after sur contains a tall looped glyph and a separate low oval0, retaining D_0|d_0 without a second d. The map ends with an upward turn only. At the far right the terminal mark is elongated and oblique rather than round, so point versus short dash remains explicit. There is no left brace around these lines.')
a.replace(a.comparison['B07']['first'],f)
a.add_row('B07','Final punctuation after (208)','.','.',r'\unsure{.|-}','medium','punctuation','elongated terminal mark',True,True)
a.doubt('Final punctuation after (208)',r'\unsure{.|-}','The isolated terminal mark is short, oblique and elongated; point with a pen exit versus short dash is unresolved.','medium')
a.keep('B08','The square has four objects, three fully headed sides and a bottom shaft with one upward turn. The lower-right Pi has no low1 and its D has no separate star. The upper-left named index has a rough short stroke, distinct from the clearly separated pair in the adjacent P index; the lower named index keeps its comma and single stroke. The crossed lower-left D, Pi case distinctions, first curve, number and lower definition accent remain locally uncertain. The central label reads2-cart. with a point.')
a.keep('B09','The pencil digits have an initial1, an open curved2 and two connected bowls of8. Their margin placement is already represented in the first version; the blind version differs only by omitting that wrapper.')
replacements=[(oldbracket,newbracket),(oldrange,newrange),(oldtuple,newtuple),(r'\mathbf N',r'\mathbb N'),(oldannot,newannot),(oldend,newend)]
for e in a.report['inventory']:
 for old,new in replacements: e['first_words_or_objects']=e['first_words_or_objects'].replace(old,new)
for n in a.report.get('notation',[]):
 for key in ('notation','meaning_or_form'):
  if key in n:
   n[key]=n[key].replace(r'G_d\text{-torseur}',r'G_d\text{-}'+newword)
a.report['unresolved']=[f"{d['place']}: {d['reading']} — {d['alternatives']}" for d in a.report['doubts']]
a.note('Blind audit: all9 differing boxes were inspected. Five boxes changed. (206) now records its point/stroke sequences, double-stemmed N and literal asymmetric annotation line; the (207) annotation bracket is placed beneath its wording and its compressed word retains torseur/fibré/fibrés; the comma after Groupes is restored; and the elongated final mark of (208) retains point/dash alternatives. All short connector finishes, the four square objects, the absent bottom-right low1, and unresolved overwritten glyphs were checked without completing expected notation.')
a.finish()
