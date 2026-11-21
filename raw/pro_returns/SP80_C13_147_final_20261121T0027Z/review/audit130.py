from edition.scripts.root_audit import Audit

a=Audit(130)
f=r'les \unsure{fibres|flèches} verticales sont des morphismes'
a.change('B02',f,'After the first long f-like stroke there is a short dotted unit and a further tall loop, closely resembling the dotted i and b in the clear fibres later on this page. Fibres is therefore the graphical leading reading; flèches remains possible because the first tall joins are compressed and partly clipped. The expected mathematical role of the vertical arrows is not used to select the noun.')
a.replace(a.comparison['B02']['first'],f)
a.add_row('B02','Opening noun after les','flèches','flèches',r'\unsure{fibres|flèches}','medium','word','letter sequence',True,True)
a.doubt('Opening noun after les',r'\unsure{fibres|flèches}','The dotted short unit and later tall loop favor fibres by comparison with the clear fibres in (210); the compressed initial joins leave flèches possible.','medium')
a.keep('B03','The Z has two distinct diagonal strokes; the exponent has a d and separate low0. The versions differ only by braces around mathbb Z.')
a.keep('B04','The D index has a comma after d_0 and another small detached curved stroke before d_r, with one dash between them. The star, comma after T_d0 and final prose dash are clear. The first comma-dash-comma form is retained.')
f=r'on \unsure{pose|posera} donc'
a.change('B05',f,'On and donc are separate. After the long p, the small round o and s-like curve are followed by an extended low stroke and detached terminal mark. Pose remains primary, but the last two marks could be compressed r/a, so posera is retained rather than resolved from tense or context.')
a.replace(a.comparison['B05']['first'],f)
a.update_row(2,'B05',final=f,confidence='medium',against_C=True)
a.doubt('Verb before the first display',r'\unsure{pose|posera}','The extended low finish and detached final mark can be e with a pen finish or compressed e/r/a.','medium')
a.keep('B06','The rotated note reads du moins si les, and its first D has a closed high loop with a short return rather than separated star rays. Circle|0 remains unresolved. The second D has a clear star and a crowded internal dash/comma cluster. The concluding sont nuls and three points are visible. The extra T_d0 in the blind string belongs to the neighboring main line, already transcribed.')
oldannot=r'\overbrace{T_{d_0}}^{\substack{\text{syst. loc.}\,\unsure{\text{?}}\quad\inserted{(\overset{\mathrm{loc}}{\simeq}\mathbb Z^{d_0})}}}\text{ (sur }D_{d_0},'
newannot=r'''\begin{tikzpicture}[baseline=(t.base)]
\node[inner sep=0pt] (t) {$T_{d_0}$};
\node[anchor=south,inner sep=0pt] at ([xshift=-6pt,yshift=12pt]t.north) {$\text{syst. loc.}\,\unsure{\text{?}}$};
\draw[line width=.3pt] ([xshift=-12pt,yshift=9pt]t.north west) .. controls ([xshift=-6pt,yshift=9pt]t.north west) and ([xshift=-3pt,yshift=5pt]t.north west) .. ([xshift=-3pt,yshift=-1pt]t.north west);
\draw[line width=.3pt] ([yshift=15pt]t.north east) .. controls ([xshift=-3pt,yshift=14pt]t.north) and ([xshift=-3pt,yshift=5pt]t.north west) .. ([xshift=-3pt,yshift=-1pt]t.north west);
\end{tikzpicture}
\overset{\inserted{(\overset{\mathrm{loc}}{\simeq}\mathbb Z^{d_0})}}{
\begin{tikzpicture}[baseline=(s.base)]
\node[inner sep=0pt] (s) {$\text{ (sur }D_{d_0},$};
\draw[line width=.3pt] ([yshift=3pt]s.north west)--([yshift=3pt]s.north east) .. controls ([xshift=2pt,yshift=3pt]s.north east) and ([xshift=3pt,yshift=4pt]s.north east) .. ([xshift=2pt,yshift=6pt]s.north east);
\end{tikzpicture}}'''
oldprep=r'\text{image inverse de }'
newprep=r'\text{image inverse }\unsure{\text{de}|\text{du}}\text{ }'
f=a.comparison['B07']['first'].replace(oldannot,newannot).replace(oldprep,newprep)
a.change('B07',f,'The short preposition has a d loop followed by compressed low joins, leaving de|du. The first raised caption reads syst. loc. plus a separate unresolved curl and is attached by two curved arms converging beside T. The local-isomorphism parenthesis is separately raised over the opening sur phrase with a long line beneath it. These two attachments replace the single normalized overbrace. The local label has one wave, one lower bar and doubled Z; the base ends with a comma, not a closing parenthesis.')
a.replace(oldannot,newannot)
a.replace(oldprep,newprep)
a.update_row(7,'B07',final=newannot)
a.add_row('B07','Preposition after image inverse in the first display','de','de',r'\unsure{de|du}','medium','word','compressed short word',True,True)
a.doubt('Preposition after image inverse in the first display',r'\unsure{de|du}','The d loop is clear; the short joined ending does not securely separate e from u.','medium')
a.keep('B08','The connector has a long shaft, a thick right cap and one tiny lower return. A separate second barb is not established. Both source commas and the single index dash remain visible; the first literal path is retained.')
a.keep('B09','The canceled initial has a surviving top bar and stem, with no independent complete right bowl of D. Its star and index ends survive; the middle dash meets the cancellation and remains uncertain. The wave-plus-bar relation, syst. local, low1 and parenthesized H_1 are distinct.')
a.keep('B10','The word fibres has the long f, dotted i and tall b; P and D both have a single index dash without flanking commas. Sur is a separate word before a D-shaped base. The versions differ only by text/math wrappers.')
a.keep('B11','The final restriction row has stars on the first T and on D, no commas in the two T indices, but comma-dash-comma in the D index. A separate comma terminates the row. Only superscript order and the punctuation wrapper differ.')
oldnum=r'\unsure{210}'
newnum=r'2\unsure{1|6|0}0'
a.change('B12','('+newnum+')','The outer digits2 and0 are clear. The middle glyph has a tall upright merging into a dark low loop:1 remains first, while6 and0 cannot be excluded from the retracing. The uncertainty is localized to that middle digit rather than asserting the entire number as one undifferentiated candidate.')
a.replace(oldnum,newnum)
a.add_row('B12','Middle digit of the first display number',r'\tag{210}','(210)',r'(2\unsure{1|6|0}0)','medium','number','retraced digit',True,True)
a.doubt('formula number (210)',r'2\unsure{1|6|0}0','Outer2 and0 are clear. The middle upright and merged low loop favor1 but admit6 or0.','medium',replace_place='formula number (210)')
a.keep('B13','The opening group has a tall looped d and following e exit. The next word has the short s opening, low o/r joins and a tall t before que, supporting de sorte que rather than on sait que. The tilde, both index commas and point after ext are retained.')
a.keep('B14','The Pi index has two commas around one dash, while the starred T index has only the first comma. The end point is separate from the low r. The difference is superscript-command order.')
a.keep('B15','The rotated second note has du moins si, a two-legged indexed sign, starred D, one comma before the index dash, closing parenthesis, equality, zero and three points. The adjacent on is outside this marginal qualification and already belongs to the main prose. Existing Pi/pi uncertainty is retained.')
a.keep('B17','The two Pi forms, lower Delta_r, equality and coproduct survive the long crossing strokes. The high rough trace over the first Pi and lower star-like cluster remain unresolved as in the first reading. The small loops near the coproduct are continuous with the cancellation pattern; no separate baseline or recoverable additional label is established, so no new textual unit is invented from them. The right index retains comma-dash-comma.')
oldtuple=r'(d_0,-,d_r)\in\mathbb N^{r+1}'
newtuple=r'(d_0,\mathord{-\, -},d_r)\in\mathbb N^{r+1}'
f=a.comparison['B18']['first'].replace(oldtuple,newtuple)
a.change('B18',f,'The live tuple under the coproduct has two separated short horizontal strokes between its commas. The lower inequality continuation is instead one point and one dash, with no additional inequality after d_1. N has its double stroke and exponent r+1. The retraced left capital remains G|B; the right summand has a stem and two bowls favoring B, with G still possible. The canceled condition remains uncertain.')
a.replace(oldtuple,newtuple)
a.update_row(22,'B18',final=a.report['rows'][22]['final'].replace(oldtuple,newtuple))
a.keep('B20','After torseur the first small s-like mark, separate round o and longer u/s finish support sous, rather than sur. The P summand has both commas around one dash, and the right group is G_Delta_r. The first reading is retained.')
a.keep('B21','The T summand has one dash between commas. Both Pi_1/H_1 separators and the comma after P are visible. Each reduced group after G and after P consists of a short upper mark and a longer lower stroke, without a complete word choix. The literal two-stroke drawings and the separate uncertain ou remain appropriate.')
a.keep('B22','The small word begins with a looped d and has a high point over its middle low joins. No further tall crossed t supports dito, and the initial is not e for etc. The first dire|dira|dés alternatives remain unresolved. Les restrictions à and the starred target are clear, with no terminal point.')
a.keep('B23','The pencil foliation has1, an angled2 and a closed upper loop with descending tail for9. The page already includes the margin wrapper; its absence from the first cropped string is only a span representation difference.')
a.keep('B24','The canceled condition has surviving d stems, lower inequality bars and one central short stroke. The first lower index is heavily retraced, so the whole d_r>=stroke>=d_0 candidate remains uncertain. The second reading does not justify removing that uncertainty.')
f=a.comparison['B25']['first'].replace(oldannot,newannot).replace(oldprep,newprep).replace(oldnum,newnum)
a.change('B25',f,'The full display confirms the two separately placed raised annotations and the localized uncertain middle numeral. It also confirms the brace extends through the last restriction row, the canceled initial T line remains separate from the live local-system description, the connector has its short capped finish, the fibre base is D, and the last row ends with a comma. The de|du uncertainty is retained at its one occurrence.')
f=a.comparison['B26']['first'].replace(oldtuple,newtuple)
a.change('B26',f,'The full system confirms the paired continuation in its live indexing tuple, distinct from the point-plus-dash in the inequality. The brace extends to the starred objects and the final restrictions line. The compressed dire/dira/dés word aligns with that starred-object row, not as an extra line of the preceding local-system description. The two reduced stroke pairs and absence of a final point remain literal.')
for e in a.report['inventory']:
 for old,new in [(oldannot,newannot),(oldprep,newprep),(oldnum,newnum),(oldtuple,newtuple)]:
  e['first_words_or_objects']=e['first_words_or_objects'].replace(old,new)
a.report['unresolved']=[f"{d['place']}: {d['reading']} — {d['alternatives']}" for d in a.report['doubts']]
a.note('Blind audit: all23 differing boxes were inspected. Seven boxes changed: the opening noun now leads with fibres while retaining flèches; pose/posera and de/du remain explicit; the first number has only its middle digit uncertain (1/6/0); the two annotations retain separate leaders and placement; and the live tuple in (211) has two strokes. Both whole-display boxes record the corresponding changes. The margins, capped connectors, cancellations, B/G distinction, Pi case alternatives, final dire/dira/dés, and foliation129 remain as visually adjudicated.')
a.finish()
