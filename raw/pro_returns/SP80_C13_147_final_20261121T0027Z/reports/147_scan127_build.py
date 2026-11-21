import json
from pathlib import Path

base=Path('/workspace/scratch/12caffedf246')
out=base/'edition/reports'
manifest=[json.loads(x) for x in (out/'147_scan127_crops.jsonl').read_text().splitlines()]
crops={Path(x['crop']).stem.removeprefix('147_scan127_'):x for x in manifest}

four_dashes=r'\mbox{-\kern.3em-\kern.3em-\kern.3em-}'
deploiement=r'déplo\unsure{y|i}ement'
inline=r'D_{\deleted{\unsure{d}}i}^{\langle d\rangle}=D_{d+i,d}'
theta=r'\inserted{$\Theta_d$ \deleted{\unsure{$(D(d))$|(cf)}}}'
top_words=r'\deleted{On a envie de définir des torseurs}'
top_formula=r"\deleted{D_{d,d'}^*=D_{d,d'}\mid D_d^*\quad\text{ouvert de }D_{d,d'}}"
top_hyp=r"\deleted{(quand on fait l'\unsure{hyp}}"
first203=r"\deleted{(203)\qquad D_{d,d'}^*=D_{d,d'}\mid D_d^*}"
right_note=r"\deleted{ouvert de $D_{d,d'}$ (complémentaire d'un diviseur à croisements normaux $\Delta(d,d')$ sur $D_{d,d'}$\unsure{)}}"
# The isolated final closing curve is included in each (d) candidate. There is no
# additional closing parenthesis for the opening prose parenthesis on this line.
image_inverse=r"\deleted{(image inverse de $\unsure{\Delta(d)|\Theta(d)|D(d)}$}"
margin=r'\margin{'+right_note+r'\par '+image_inverse+'}'
lower_words=r"\deleted{On \deleted{\unsure{posera|pose} alors} \inserted{veut définir} \deleted{des} morphismes canoniques de groupoïdes}"
boxed=r"\boxed{\Pi_1P_d^*\xrightarrow{\unsure{\gamma|r}_{d,d'}}\Pi_{\unsure{1}}P_{d'}^*}"
second203=r"\deleted{(203)\qquad"+boxed+r"\qquad\text{pour }d'<d}"
caption=r"\deleted{``h\uuline{om de générisation}''}"

tex='\n'.join([
 r'\scanpage{127}',top_words,r'\[',top_formula,r'\]',top_hyp,'',
 r"On suppose maintenant que la situation envisagée provient d'un diviseur à croisements normaux $D$ sur $X=D_0$, en déployant celui-ci. Alors \inserted{$\forall\,d\in\mathbb N$} la structure \inserted{de} "+deploiement+r" induite sur les $D_d$ (en posant $"+inline+r"$ "+four_dashes+r" \unsure{p|je} me \unsure{dispenser|dispense} de développer au long et au large) avec les $=$ propriétés --- elle provient d'un diviseur à croisements normaux "+theta+r" sur $D_d$, dont le complémentaire du support est noté $D_d^*$.",'',
 r'\deleted{On note}',r'\[',first203,r'\]',margin,'',
 lower_words,r'\[',second203,r'\]',caption,r'\margin{126}',''
])
(out/'147_scan127_proposed.tex').write_text(tex)

rows=[]
def row(place,C,H,final,ink,cn,confidence='high',kind='misread word',ac=False,ah=True,math=False,category='Words',marked=False,more=()):
 c=crops[cn]
 x=dict(place=place,C=C,H=H,final=final,scan_shows=ink,crop=c['crop'],box=c['box'],confidence=confidence,kind=kind,against_C=ac,against_H=ah,marked_in_H=marked,math_consequential=math,error_category=category)
 if more:x['supporting_crops']=[dict(crop=crops[n]['crop'],box=crops[n]['box']) for n in more]
 rows.append(x)
row('Canceled opening, first two writing lines',top_words,r'\struck{On a aussi de définir sur tous}',top_words,
 'The first line has envie after On a, followed by de définir des; the next line has torseurs. The dot over the i of envie and the taller strokes of définir survive the horizontal cancellation. The compressed middle of torseurs is partly covered, but the sequence and terminal s support C rather than H\u2019s sur tous.',
 'top_words','medium')
row('Canceled unfinished parenthetical at upper right',r"\deleted{(quand on fait l'hyp.}",r'(complément \ill{} \ill{})',top_hyp,
 'An opening parenthesis, the q descender of quand, on, the tall f of fait and l\u2019 are visible. The compressed final group favors hyp but remains uncertain under the strike. No separate terminal point or closing parenthesis is secure; C\u2019s point is not copied.',
 'top_hyp','medium',ac=True,marked=True)
row('Live paragraph, déployant','déployant','dépliant','déployant',
 'After déplo there is a long descending y stroke, followed by the low a/n joins and final t. The o and y distinguish déployant from dépliant.',
 'deployant')
row('Raised universal quantifier, final punctuation',r'\inserted{$\forall\,d\in\mathbb N$}',r'\add{$\forall d \in \mathbb{N}$,}',r'\inserted{$\forall\,d\in\mathbb N$}',
 'The inserted formula ends at N without a comma. Its curved leader returns to the space after Alors, before la. The nearby comma higher to the right belongs to X=D_0, not to this insertion.',
 'forall',kind='text not on the page',category='Text that is not on the page')
row('Word following inserted de','déploiement','dépliement',deploiement,
 'Déplo is visible. The next letter has a retraced upright and descending loops, favoring y, while i remains a possible earlier or final reading. The following ement is readable. H\u2019s form omits the visible o; C\u2019s i remains admitted, so a new certainty-only error is not assigned to C.',
 'de_deploiement','medium')
row('Canceled old subscript before live i',r'D_{\deleted{\unsure{d}}i}^{\langle d\rangle}',r'D^{\langle d\rangle}_i',r'D_{\deleted{\unsure{d}}i}^{\langle d\rangle}',
 'A dark crossed cluster lies between D and the separate dotted live i. Its bowl and upright favor d, but the cancellation prevents a clean letter reading. H drops the canceled material. The raised angle brackets around d and the whole right-hand D_{d+i,d} are clear.',
 'inline_formula','medium','omission',math=True,category='Omissions')
row('Four separate dash marks before the short first-person phrase','---','----',four_dashes,
 'Four short separated horizontal strokes are visible. They are preserved as four individually spaced hyphens, without adding an arrowhead or merging them into one continuous stroke. H records four hyphens; the distinct source strokes are specified here.',
 'je_me_dash',kind='drawing or diagram',ac=True,ah=False,category='Drawings and diagrams')
row('Short phrase after the four dash marks',r'\unsure{je|p.} me','pour se',r'\unsure{p|je} me',
 'The first group is one long stem/descender with an open right arch. It is p-like, but a compressed je remains possible; there is no separate point after it. The next word has the repeated low joins of me, not se. There are no extra strokes sufficient for the full word pour.',
 'je_me_dash','medium')
row('End of the parenthetical explanation','au long et au large)',r'au long \uncertain{les choses})','au long et au large)',
 'The first crop shows au long et au; the next crop shows large followed by the closing parenthesis. The tall l and descending g of large are distinct, with no les choses sequence.',
 'long_et_au',marked=True,more=('large_avec',))
row('Clause after large)',r'avec les $=$ propriétés','a aussi la même propriété',r'avec les $=$ propriétés',
 'Avec is visible after the closing parenthesis. The next crop gives les, two horizontal equality strokes, and propriétés. The ending is compressed, but the final low sweep after the tall t/accent area supports plural s. The literal equals sign is not expanded into même in the text.',
 'properties','medium',more=('large_avec',))
row('Canceled old notation beside the live Theta insertion',r'\deleted{\unsure{$(D(d))$|(cf)}}','',r'\deleted{\unsure{$(D(d))$|(cf)}}',
 'The live Theta_d is unstruck. Beside it is a separately crossed compact notation with a tall central stroke, looped fragments and parenthesis-like ends. D(d) remains the leading C candidate, but the crossing does not permit resolving the whole cluster. H omits it.',
 'theta_insert','medium','omission',math=True,category='Omissions')
row('End of the live paragraph','du support est noté',r'\ill{} \uncertain{est noté}','du support est noté',
 'Du support is readable, including the two deep p descenders. Est noté follows with a separate accent over é. The subsequent D_d has a clear high star and a terminal point.',
 'support_noted',kind=r'readable ink left as \ill{}',category='Readable ink left as illegible',marked=True)
row('Placement of the two canceled comments associated with first (203)',r"\deleted{ouvert de $D_{d,d'}$ (complémentaire d'un diviseur à croisements normaux $\Delta(d,d')$ sur $D_{d,d'}$)}",r"\marginal{\struck{ouvert de $D_{d,d'}$ (complémentaire d'un diviseur à croisements normaux $\Delta(d,d')$ sur $D_{d,d'}$, image inverse de $\Delta(d)$)}}",margin,
 'The comments occupy the narrow right column beside and below the first (203). A long curve descends from the right-hand factor and turns beneath the note, associating it with that formula. A margin block preserves this placement; the curve is not interpreted as a separate mathematical diagram.',
 'right_note',kind='insertion or placement',ac=True,ah=False,category='Insertions put in the wrong place',more=('image_inverse',))
row('End of the first right-column parenthetical',r"sur $D_{d,d'}$)",r"sur $D_{d,d'}$,",r"sur $D_{d,d'}$\unsure{)}",
 'The descending curve at the far right can be a closing parenthesis, but it is partly shared with the attachment/bracketing curve. The punctuation is left uncertain; no comma is visible. A fresh opening parenthesis begins the following image-inverse line.',
 'right_note','medium','misread symbol or index',category='Other')
row('Canceled image-inverse line, capital and final punctuation',r"\deleted{(image inverse de $\unsure{\Theta(d)|D(d)}$)}",r'image inverse de $\Delta(d)$)',image_inverse,
 'The sign after de has angular rising and basal strokes, favoring Delta over the round Theta/D alternatives. The cancellation crosses it, so all three remain candidates. The line has its own opening prose parenthesis and one isolated final closing curve, used with (d); there is no second visible final closing parenthesis to add.',
 'image_inverse','medium','misread symbol or index',ac=True,math=True,category='Symbols and indices',marked=True)
row('Inserted replacement in the canceled lower sentence',r'\inserted{veut définir}',r'\add{peut définir des}',r'\inserted{veut définir}',
 'The raised first word begins with a low v-shaped join and has no p descender. Définir follows above the old canceled posera/pose alors. The nearby des is separately crossed, rather than part of this insertion.',
 'lower_defining')
row('Local cancellation of des within the globally canceled sentence',r'\deleted{des}',r'\add{peut définir des}',r'\deleted{des}',
 'A short dark crossing lies over des before morphismes, independently of the long oblique cancellation of the whole lower passage. Its local deleted state is retained in addition to the outer cancellation.',
 'lower_defining',kind='deletion state (struck given live or live given struck)',category='Struck text')
row('Arrow label in the boxed second (203)',r'\gamma_{d,d\prime}',r'r_{d,d\prime}',r'\unsure{\gamma|r}_{d,d\prime}',
 'The label has a curled descending stem favoring gamma. Its upper stroke meets the descender from groupoïdes above, so r cannot be excluded. The indices d,d\prime and the separate clear rightward arrowhead are retained. This adds no C error merely for the new uncertainty.',
 'second203','medium','misread symbol or index',math=True,category='Symbols and indices')
row('Rectangular frame around the second (203) morphism',r'\boxed{\Pi_1P_d^*\xrightarrow{\gamma_{d,d\prime}}\Pi_1P_{d\prime}^*}',r'\Pi_1 P^{*}_d \xrightarrow{\ r_{d,d\prime}\ } \Pi_1 P^{*}_{d\prime}',boxed,
 'A four-sided rectangular frame surrounds the morphism. The label (203) and condition pour d\prime<d lie outside it. The oblique cancellation crosses the frame and formula but does not make the frame a deletion stroke.',
 'second203',kind='drawing or diagram',category='Drawings and diagrams')
row('Words and quotation marks of the canceled caption',r'``hom de générisation\prime\prime',r'« homom. de spécialisation »',r'``hom de générisation\prime\prime',
 'The words are hom de générisation, with the descending g and the visible accents/remaining letter sequence. Hom has no terminal point or additional om. Two high ticks occur at each end; no guillemets are drawn.',
 'caption')
row('Extent of the two caption underlines',r"\deleted{\uuline{``hom de générisation''}}",r'\struck{« homom. de spécialisation »}',caption,
 'Two separate underline strokes begin inside hom after the initial h/opening quotes and end before the closing quotes. The limited om de générisation span is double-underlined; the initial h and quotation marks are outside the underlines.',
 'caption',kind='drawing or diagram',ac=True,category='Drawings and diagrams')
row('Lower-left pencil number',r'\margin{126}','',r'\margin{126}',
 'The lower-left pencil digits are 126. The last digit has a curved upper stroke and a closed lower bowl. It is source writing, not an editorial page marker.',
 'archive126',kind='omission',category='Omissions')

decisions=[]
def dec(mid,choice,reading,ink,cn,confidence):
 c=crops[cn];decisions.append(dict(id=mid,decision=choice,reading=reading,ink=ink,crop=c['crop'],box=c['box'],confidence=confidence))
dec('M1276','first','induite','The word begins with the dotted i, followed by n/d/u/i/t and a separate final e exit. No initial s or apostrophe-plus-new-i sequence is present.','induite','high')
dec('M1277','undecided',r'\unsure{p|je}','The first group has a long stem/descender and an open arch to its right. It favors a p-like short form, but compressed je remains possible. No independent dot supports C\u2019s p. alternative. The following me is clear.','je_me_dash','medium')
dec('M1278','undecided',r'\unsure{dispenser|dispense}','The body dispens is readable; the final raised/compressed continuation does not securely distinguish -er from -e. The p/je interpretation was not used to decide the ending by grammar.','dispense','medium')

nested=[]
def nd(place,reading,ink,cn,confidence='medium'):
 c=crops[cn];nested.append(dict(place=place,decision='undecided',reading=reading,ink=ink,crop=c['crop'],box=c['box'],confidence=confidence))
nd('Unindexed canceled old subscript',r'\deleted{\unsure{d}}','A d-like bowl/upright remains beneath the crossing; the separate dotted i is live.','inline_formula')
nd('Unindexed canceled notation beside Theta_d',r'\deleted{\unsure{$(D(d))$|(cf)}}','Crossed tall and looped fragments support the leading D(d)-like candidate, but not a letter-complete reading.','theta_insert','low')
nd('Unindexed canceled image-inverse capital',r'\unsure{\Delta(d)|\Theta(d)|D(d)}','Angular rising/basal strokes favor Delta; the cancellation prevents excluding the older Theta/D alternatives.','image_inverse')
nd('Unindexed canceled posera/pose',r'\unsure{posera|pose}','The horizontal strike hides part of the final continuation; posera leads, but pose remains possible.','lower_defining')

inventory=[]
def inv(kind,position,text,hand='his hand'):
 inventory.append(dict(element=f'E{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=text,sheet_kind='text',hand=hand,transcribed='yes'))
inv('deletion','first two writing lines',top_words)
inv('display','upper canceled restriction formula',top_formula)
inv('deletion','upper-right unfinished parenthetical',top_hyp)
inv('text','main live paragraph, from On suppose to D_d^*.','On suppose maintenant que la situation envisagée')
inv('insertion','above Alors la structure, leader after Alors',r'\inserted{$\forall\,d\in\mathbb N$}')
inv('insertion','above the start of déplo[y|i]ement',r'\inserted{de}')
inv('text','inline formula after en posant',inline)
inv('deletion','old subscript immediately before live i',r'\deleted{\unsure{d}}')
inv('drawing','four separated short dash strokes after the inline formula',four_dashes)
inv('insertion','above normaux sur D_d, leader after normaux',theta)
inv('deletion','small notation inside that insertion',r'\deleted{\unsure{$(D(d))$|(cf)}}')
inv('deletion','at right after the live paragraph\u2019s terminal point',r'\deleted{On note}')
inv('display','first occurrence of (203), horizontal and broad oblique cancellation',first203)
inv('margin note','right column associated by the long descending/returning curve with first (203)',right_note)
inv('margin note','separate canceled parenthetical line below the right-column note',image_inverse)
inv('deletion','lower two-line sentence under the broad oblique cancellation',lower_words)
inv('deletion','older local wording below veut définir',r'\deleted{\unsure{posera|pose} alors}')
inv('insertion','replacement written above the old wording, later canceled with the whole passage',r'\inserted{veut définir}')
inv('deletion','local des before morphismes, inside the broad cancellation',r'\deleted{des}')
inv('display','second occurrence of (203), with boxed morphism and condition outside',second203)
inv('drawing','four-sided box surrounding the morphism',boxed)
inv('deletion','caption beneath the box, with limited double underline',caption)
inv('margin note','lower-left corner','126','unidentified pencil hand')

doubts=[
 dict(place='Upper canceled hyp ending',reading=top_hyp,alternatives='hyp is leading, but its compressed crossed ending is not fully plain; no final point is supplied.',confidence='medium'),
 dict(place='Middle letter of déplo[y|i]ement',reading=deploiement,alternatives='The descending retraced letter favors y; i remains possible. No earlier layer can be isolated securely.',confidence='medium'),
 dict(place='Old canceled subscript before i',reading=r'\deleted{\unsure{d}}',alternatives='d-like crossed character, retained rather than omitted or fully resolved.',confidence='medium'),
 dict(place='First short group before me',reading=r'\unsure{p|je}',alternatives='p without a terminal point versus compressed je; not expanded to pour.',confidence='medium'),
 dict(place='dispenser/dispense ending',reading=r'\unsure{dispenser|dispense}',alternatives='The final continuation is compressed; grammatical pairing with p/je does not settle it.',confidence='medium'),
 dict(place='Canceled old notation beside Theta_d',reading=r'\deleted{\unsure{$(D(d))$|(cf)}}',alternatives='D(d)-like group versus C\u2019s cf-like alternative; parentheses and letter chronology remain obscured.',confidence='low'),
 dict(place='Right-column note, final curve',reading=r'\unsure{)}',alternatives='Closing parenthesis versus part of the attachment/bracketing curve; no comma is secure.',confidence='medium'),
 dict(place='Canceled image-inverse capital',reading=r'\unsure{\Delta(d)|\Theta(d)|D(d)}',alternatives='Delta leads from angular strokes; Theta/D are not excluded under the cancellation. Only one final closing curve is copied.',confidence='medium'),
 dict(place='Old local lower verb',reading=r'\unsure{posera|pose}',alternatives='Final -ra is not letter-complete beneath the horizontal strike.',confidence='medium'),
 dict(place='Boxed morphism label',reading=r'\unsure{\gamma|r}_{d,d\prime}',alternatives='Gamma leads from the curled stem, but its upper stroke meets the descender from groupoïdes above; r remains possible.',confidence='medium'),
 dict(place='Target low index in boxed morphism',reading=r'\Pi_{\unsure{1}}P_{d\prime}^*',alternatives='A short low upright branch survives to the left of the oblique cancellation, favoring 1; its upper part merges with the strike.',confidence='medium')
]

notes=[
 'S127-01. Scan127 has no separate author page number at the head; pencil126 is at lower left. The inventory covers26 main and marginal writing baselines, excluding raised insertions. The whole page and each native half were viewed once, then all23 saved first-pass crops. No other-page files, OCR, external sources or compilation were used.',
 'S127-02. The live paragraph assumes that the situation comes from a normal-crossings divisor D on X=D_0 and asserts a corresponding deployment structure on D_d, with a divisor Theta_d and open complement D_d^*. These are manuscript assertions reported from the leaf, not independently established mathematical claims.',
 'S127-03. The top canceled attempt and the first canceled (203) both write the restriction D_{d,d\prime}^*=D_{d,d\prime}|D_d^*. The final canceled (203) proposes a morphism between fundamental-groupoid expressions for d\prime<d and calls it a hom de générisation. They remain canceled proposals; their existence, canonicity and relation to specialization were not proved.',
 'S127-04. Both occurrences of (203) are copied independently. The first formula has horizontal cancellations, while the lower region also has long oblique cancellation strokes. The final morphism has a genuine four-sided box distinct from those oblique strokes. The main live paragraph ends before canceled On note and is not put under the lower cancellation.',
 'S127-05. The raised universal quantifier attaches after Alors; de attaches before déplo[y|i]ement; Theta_d attaches after normaux before sur D_d. Theta_d itself is live while its adjacent old notation is locally canceled. The lower replacement veut définir was written above the old posera/pose alors, but the entire lower sentence was subsequently canceled; des has its own local cancellation inside that outer state.',
 'S127-06. The old d-like subscript and the live dotted i were read separately; the raised angle-bracketed d and right-hand D_{d+i,d} are clear. This was a visual/notation check only. The canceled cluster was not erased from the transcription because the live index would otherwise be simpler.',
 'S127-07. M1276 is resolved to induite. The p/je and dispenser/dispense choices remain independent uncertainties; their possible grammatical pairings did not determine the strokes. Déplo[y|i]ement also keeps its retraced letter rather than silently imposing conventional spelling. Four separated short dashes are preserved before the uncertain short phrase.',
 'S127-08. The prose has au long et au large, avec les = propriétés and du support est noté. The equals sign is copied literally; its contextual expansion to mêmes belongs only to the abbreviations/notation apparatus. The compressed ending of propriétés is read as plural from its final low sweep, rather than solely from les.',
 'S127-09. The two canceled comments occupy the right margin and are associated with the first (203) by the long descending/returning curve. The far-right curve of the first comment may be its closing parenthesis and remains doubtful. The image-inverse line has its own opening parenthesis and one isolated final closing curve; no second closing parenthesis is added. Its capital leads with Delta from angular strokes, without enforcing agreement with live Theta_d.',
 'S127-10. In the final boxed formula the source Pi_1 is clear, while the target low1 partly merges with an oblique strike and remains locally uncertain. The gamma-like label has its own curled stem, but an upper stroke meets the descender from groupoïdes, so gamma/r remains open. The rightward arrowhead is independently clear. No expected groupoid notation supplied the target index or label.',
 'S127-11. The canceled caption reads hom de générisation with no point after hom, paired high quotation ticks, and two underline strokes beginning after the initial h and ending before the closing quotes. The limited om de générisation span is underlined. The words do not read homom. de spécialisation.',
 'S127-12. All C deletion and insertion spans, including nested uncertain material and the separately canceled des, were checked for state and attachment. Four unindexed C doubts remain in nested_decisions. H\u2019s editorial account of later numbering was excluded from source text; the actual pencil126 omission is collated.'
]
events=[]
for i in [1,4,5,6,7,8,9,10,11,12]:
 events.append(dict(statement_id=f'S127-{i:02d}',type='used and rechecked in this run',outcome={
 1:'The whole-page/native-half/crop workflow and complete page-local inventory were reconciled with C and H.',
 4:'The two number labels, canceled regions, live paragraph boundary and four frame edges were inspected.',
 5:'Each insertion attachment and its final live/canceled state was checked independently from its wording.',
 6:'The old and live index strokes and the whole inline formula were checked; no mathematical claim was proved.',
 7:'Indexed choices and the retraced spelling were read on their crops without resolving one from another\u2019s grammar.',
 8:'The disputed prose, literal equals sign and final plural sweep were checked visually.',
 9:'Margin placement, angular capital, attachment curve and the visible parenthesis count were checked without silently restoring punctuation.',
 10:'The two Pi expressions, stars, low indices, arrow label and separate arrowhead were inspected under the cancellation.',
 11:'Caption letters, quote ticks, point absence and both underline endpoints were reconciled with the witnesses.',
 12:'All nested and outer editorial states and mark IDs were reconciled with the source; H editorial notes were separated from ink.'
 }[i]))
events.extend([
 dict(statement_id='S127-02',type='carried as background without fault found',outcome='Normal-crossings origin, deployment structure and complementary open were transcribed as the page\u2019s assertions only.'),
 dict(statement_id='S127-03',type='carried as background without fault found',outcome='Canceled definitions and groupoid-morphism proposal were reported with their canceled state, without a proof of existence or canonicity.')
])
events.sort(key=lambda x:x['statement_id'])

hand=[
 dict(habit='A short p-like cursive group can compete with compressed je; punctuation must be checked separately.',places='Scan127 after the four short dash marks.',scope='One unresolved group; the missing point is clear, its letter identity is not.',misreadings='C offers p. with a point, H expands to pour and reads se for me.'),
 dict(habit='A retraced descending middle letter can obscure y versus i.',places='Scan127 déplo[y|i]ement, compared locally with the clear y of déployant.',scope='The participle is clear; the noun remains uncertain. No universal spelling rule is asserted.',misreadings='H loses the o/y structure in dépliant and dépliement; C\u2019s noun spelling remains possible but not certain.'),
 dict(habit='An ordinary equals sign can stand in running prose for a repeated property word.',places='Scan127 avec les = propriétés.',scope='One literal occurrence checked here; expansion is confined to the apparatus.',misreadings='H expands and rewrites the surrounding clause.'),
 dict(habit='A word descender from the line above may meet a small mathematical label.',places='Scan127 gamma/r label below groupoïdes.',scope='One intersection; the label is retained under doubt.',misreadings='C reads gamma, H reads r; the crossing limits certainty.'),
 dict(habit='Broad cancellation strokes can obscure a small low index while leaving a short separate branch.',places='Scan127 target Pi index in the boxed second (203).',scope='The source1 is clear, target1 partly merged; no expected repeated notation determines it.',misreadings='Both witnesses give an unqualified target1; this run adds local uncertainty only.'),
 dict(habit='Underline endpoints need not coincide with word or quote boundaries.',places='Scan127 final caption.',scope='Both strokes start after the opening quotes and initial h and end before the closing quotes.',misreadings='C underlines the entire quoted span; H omits the underlining.'),
 dict(habit='Separate local cancellations can survive inside a later broad cancellation.',places='Scan127 old posera/pose alors, des, and the old notation beside live Theta_d.',scope='The nested states are recorded individually on this leaf.',misreadings='H omits the old Theta-adjacent cluster and folds locally struck des into the replacement insertion.')
]
notation=[
 dict(notation=r'D_{d,d\prime}^*=D_{d,d\prime}\mid D_d^*',meaning_or_form='Repeated canceled restriction formula; vertical restriction bar, stars and lower primes remain distinct.',places='Scan127 top attempt and first (203).'),
 dict(notation=inline,meaning_or_form='Angle-bracketed raised d; crossed old index before separate live i; explicit d+i,d lower index on the right.',places='Scan127 main paragraph after en posant.'),
 dict(notation=r'\Theta_d',meaning_or_form='Live inserted oval-with-horizontal-bar Theta and lower d, distinct from the crossed neighboring notation.',places='Scan127 insertion after normaux.'),
 dict(notation=r'\Delta(d,d\prime)',meaning_or_form='Clear angular Delta in the canceled marginal comment; a comparand for the doubtful Delta/Theta/D later in that margin.',places='Scan127 right-column description of the divisor.'),
 dict(notation=r'\unsure{\Delta(d)|\Theta(d)|D(d)}',meaning_or_form='Angular leading candidate retained with alternatives under cancellation; not regularized to live Theta_d.',places='Scan127 canceled image-inverse line.'),
 dict(notation=r'=',meaning_or_form='Literal two-bar sign in avec les = propriétés; contextual expansion mêmes is not substituted in the text.',places='Scan127 main paragraph.'),
 dict(notation=r'\Pi_1P_d^*\xrightarrow{\unsure{\gamma|r}_{d,d\prime}}\Pi_{\unsure{1}}P_{d\prime}^*',meaning_or_form='Boxed and canceled morphism; clear capital Pi shapes, starred P objects, uncertain intersected label and target low1.',places='Scan127 second (203).')
]
abbreviations=[
 dict(form='hyp',expansion='hypothèse (tentative reading of the canceled ending; no expansion or terminal point added)'),
 dict(form='p',expansion='pour (possible abbreviation only; je remains an alternative)'),
 dict(form='=',expansion='mêmes in this plural context'),
 dict(form='hom',expansion='homomorphisme')
]

second=[]
def sb(kind,coords,reading):second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,coords=coords,reading=reading))
def sc(kind,cn,reading):sb(kind,crops[cn]['box'],reading)
sc('struck passage','top_words',top_words)
sc('struck passage','top_formula',r'\['+top_formula+r'\]')
sc('struck passage','top_hyp',top_hyp)
sc('different words','deployant','déployant')
sb('number',[1404,548,1602,618],r'$X=D_0$')
sb('insertion',[1330,603,1538,670],r'\inserted{$\forall\,d\in\mathbb N$}')
sc('insertion','de_deploiement',r'\inserted{de} '+deploiement)
sc('different words','induite','induite')
sc('doubtful formula','inline_formula','$'+inline+'$')
sc('different words','je_me_dash',four_dashes+r' \unsure{p|je} me')
sc('different words','dispense',r'\unsure{dispenser|dispense}')
sc('different words','long_et_au','au long et au')
sc('different words','large_avec','large) avec')
sc('different words','properties',r'les $=$ propriétés --- elle')
sb('insertion',[597,1305,813,1426],theta+' sur')
sc('different words','support_noted',r'du support est noté $D_d^*$.')
sc('struck passage','on_note',r'\deleted{On note}')
sc('struck passage','first203',r'\['+first203+r'\]')
sc('margin note','right_note',right_note)
sc('margin note','image_inverse',image_inverse)
sc('struck passage','lower_defining',r'\deleted{On \deleted{\unsure{posera|pose} alors} \inserted{veut définir} \deleted{des} morphismes}')
sc('doubtful formula','second203',r'\[\deleted{'+boxed+r'}\]')
sb('number',[277,2136,421,2233],r'\deleted{(203)}')
sb('struck passage',[1305,2104,1615,2247],r"\deleted{pour $d'<d$}")
sc('struck passage','caption',caption)
sc('margin note','archive126',r'\margin{126}')
sb('struck passage',[282,2018,1218,2134],r'\deleted{canoniques de groupoïdes}')

checks=[
 dict(span=top_words,finding='Both opening writing lines are horizontally canceled. The cancellation reaches the entire sentence, including the second-line torseurs.'),
 dict(span=top_formula,finding='The restriction formula and the adjoining ouvert de D_{d,d\prime} are crossed together; stars, primes, equality and restriction bar remain legible.'),
 dict(span=r"\deleted{(quand on fait l'hyp.}",finding='The unfinished parenthetical is horizontally crossed; its ending remains uncertain and no terminal point is secure.'),
 dict(span=r'\inserted{$\forall\,d\in\mathbb N$}',finding='The leader ends after Alors before la; the formula is live and has no terminal comma.'),
 dict(span=r'\inserted{de}',finding='The raised de and its curved leader attach before déplo[y|i]ement, after structure.'),
 dict(span=r'\deleted{\unsure{d}}',finding='The crossed old index is distinct from the live dotted i to its right; its exact letter remains doubtful.'),
 dict(span=theta,finding='The whole raised group attaches after normaux. Theta_d is live; only the compact adjacent old notation is separately canceled.'),
 dict(span=r'\deleted{\unsure{$(D(d))$|(cf)}}',finding='Crossing strokes pass through the old compact notation, while Theta_d and the attaching leader remain uncanceled.'),
 dict(span=r'\deleted{On note}',finding='A local horizontal stroke crosses On note after the live D_d^* and point. It does not extend the cancellation into that live ending.'),
 dict(span=first203,finding='The first (203), formula and its stars are within the horizontal and broad oblique cancellation; it is not the final boxed morphism.'),
 dict(span=r"\deleted{ouvert de $D_{d,d'}$ (complémentaire d'un diviseur à croisements normaux $\Delta(d,d')$ sur $D_{d,d'}$)}",finding='The right-column note is crossed by the broad oblique strokes and attached to the first (203); its far-right closing curve remains punctuation/attachment doubtful.'),
 dict(span=r"\deleted{(image inverse de $\unsure{\Theta(d)|D(d)}$)}",finding='The separate line has a local horizontal strike as well as broader cancellation. A fresh opening parenthesis and only one isolated closing curve survive; the capital remains Delta/Theta/D doubtful.'),
 dict(span=r"\deleted{On \deleted{\unsure{posera|pose} alors} \inserted{veut définir} \deleted{des} morphismes canoniques de groupoïdes}",finding='The entire lower sentence is canceled by broad oblique strokes, including its replacement and the following canoniques de groupoïdes line.'),
 dict(span=r'\deleted{\unsure{posera|pose} alors}',finding='A separate older horizontal cancellation crosses the old verb and alors; its final verb letters remain uncertain beneath that stroke.'),
 dict(span=r'\inserted{veut définir}',finding='The replacement sits above the old verb phrase. It excludes the locally struck des and is itself canceled by the later whole-passage strike.'),
 dict(span=r'\deleted{des}',finding='A short independent dark crossing covers des before morphismes, inside the later canceled passage.'),
 dict(span=r"\deleted{(203)\qquad\boxed{\Pi_1P_d^*\xrightarrow{\gamma_{d,d'}}\Pi_1P_{d'}^*}\qquad\text{pour }d'<d}",finding='The second repeated number, boxed morphism and outside condition are canceled together. The rectangle is a frame; the intersecting diagonals are cancellation strokes.'),
 dict(span=r"\deleted{\uuline{``hom de générisation''}}",finding='The caption belongs to the canceled passage. Two separate underline strokes cover the limited om de générisation span; initial h and quotes are not underlined.')
]

report=dict(scan=127,reader='reader_a',line_count=26,rows=rows,decisions=decisions,nested_decisions=nested,inventory=inventory,doubts=doubts,notes=notes,check_events=events,hand_log=hand,notation=notation,abbreviations=abbreviations,second_boxes=second,
 unresolved=[
  'The compressed canceled hyp ending and the retraced y/i in the live noun remain uncertain.',
  'p/je and dispenser/dispense remain independent local choices; no grammatical pairing decides them.',
  'The old canceled index, the Theta-adjacent old notation and posera/pose remain under doubt.',
  'The right-note closing curve is partly shared with its attachment stroke; the following line has only one copied final closing curve.',
  'Delta(d) leads the canceled image-inverse alternatives, without forcing agreement with Theta_d.',
  'The intersected gamma/r label and target low1 remain locally uncertain in the boxed morphism.'
 ],deletion_insertion_checks=checks)

def clean(x):
 if isinstance(x,str):return x.replace(r'\u2019','’').replace(r'd\prime',"d'").replace(r'\prime\prime',"''")
 if isinstance(x,list):return [clean(y) for y in x]
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
 return x
report=clean(report)
(out/'147_scan127_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(rows=len(rows),against_C=sum(x['against_C'] for x in rows),against_H=sum(x['against_H'] for x in rows),decisions=len(decisions),resolved=sum(x['decision']!='undecided' for x in decisions),nested=len(nested),crops=len(crops),inventory=len(inventory),doubts=len(doubts),second_boxes=len(second),state_checks=len(checks))))
