import json
from pathlib import Path

ROOT=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
packet=json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan026.json').read_text())
candidate=(ROOT/'reviews/143_scan026_readerA.tex').read_text()
boxes={
    'opening-deletion':[825,80,1008,167],
    'opening-insertion':[1125,18,1624,178],
    'vertical-labels':[599,365,1105,539],
    'nb-note':[260,707,1630,929],
    'actor':[525,1200,885,1327],
    'object-condition':[320,1995,820,2125],
    'final-phrase':[360,2235,1430,2343],
}
changes=[]
def add(place,C,H,final,aC,aH,kind,ink,confidence='high',crop='page',marked=False,consequential=False):
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=aC,against_H=aH,kind=kind,ink=ink,
                        confidence=confidence,crop='page' if crop=='page' else f'crops/143_scan026_A_{crop}.png',
                        box=None if crop=='page' else boxes[crop],marked_in_H=marked,consequential=consequential))

add('opening: canceled word after que',r'\deleted{\unsure{le|que}}',r'\struck{ensemble}',
    r'\deleted{\unsure{le|que}}',False,True,'misread word',
    'A broad horizontal strike covers the word, with a left curved remnant and a central loop/descender-like remnant. It does not securely expose the longer ensemble sequence. C’s shorter alternatives le/que are retained only as tentative readings; the strike prevents a reliable letter-by-letter recovery.',
    'low','opening-deletion')
add('opening: domain set letter',r'\tau',r'\mathcal{T}',r'\unsure{\tau|\mathcal T}',
    False,True,'misread symbol or index',
    'The letter has the flag-like upper hook and one curved lower return of the shared domain-set graph. Preferred tau with explicit calligraphic-T alternative follows the current notation; this is not a consequential mathematical correction.',
    'medium','page',False,False)
add('opening: parenthetical insertion',r"\inserted{(grâce à l'op. de $\pi$)}",
    r'''(qui \ill{}
l'ensemble $\pi$)''',r"\inserted{(grâce à l'op. de $\pi$)}",
    False,True,'insertion or placement',
    'The upper added line has the descending initial g, a circumflex-like mark in grâce, the reduced accented a, and the l/apostrophe/op/de sequence before pi. Parentheses enclose the addition. Its curved guide attaches after the set letter; l’ensemble is not written in that line.',
    'high','opening-insertion',True,True)
add('opening: attachment guide','[no witness]','[no witness]',
    r'\draw[thin] (-0.15,-0.20) .. controls (-0.55,0.40) and (-0.05,0.50) .. (1.10,0.45) .. controls (2.25,0.30) and (4.45,0.25) .. (4.60,0.45);',
    True,True,'drawing or diagram',
    'A long fine stroke runs beneath the parenthetical addition, curling downward at its left end just after the set letter. It passes across the tall f region of définit without canceling the word.',
    'high','opening-insertion')
add('opening: main verb',r'définit',r'(discret)',r'définit',False,True,'misread word',
    'The main-line word has an initial d loop, an accented small vowel, a long descending f and a pointed t ending. The apparent opening parenthesis is the attachment guide, not a parenthesis around discret. H’s remaining illegible slot before un foncteur does not require another source word.',
    'high','opening-insertion',False,True)
add('diagram: relation mark left of upward arrow',r'\simeq',r'\simeq',
    r'\begin{tikzpicture}[baseline=-.4ex]\node[rotate=90,inner sep=0pt] {$\approx$};\end{tikzpicture}',
    True,True,'drawing or diagram',
    'Two parallel, predominantly vertical strokes both curve at top, middle and bottom. Neither is a straight companion bar. The candidate reproduces this spatial shape as a rotated two-wave mark; it does not infer a different mathematical equivalence claim.',
    'high','vertical-labels',False,False)
add('diagram: canceled vertical-arrow label',r'\deleted{\text{via }\widetilde\Pi}',
    "un début d'étiquette biffé",r'\deleted{\text{via : }\widetilde\Pi}',
    True,True,'omission',
    'Under the diagonal cancellation strokes, the short via graph has a dotted i. Two separately isolated dark points then stand vertically before the tilde Pi. The colon is absent in C, and H gives only an editorial description of the canceled label.',
    'medium','vertical-labels')
add('diagram: ring exponent of the covered groupoid',r'\widetilde\Pi^{\circ}',
    r'\widetilde{\Pi}{}^{0}',r'\widetilde\Pi^{\circ}',False,True,'misread symbol or index',
    'A small open, nearly circular ring stands to the upper right of the tilde Pi. Circle is retained as the preferred graphic encoding, as in the note that explains this sign; no numerical assertion is inferred from its shape.',
    'medium','vertical-labels',False,False)
add('diagram: set letter and ring on curved-arrow label',r'\tau^{\circ}',
    r'\mathcal{T}^{0}',r'\unsure{\tau|\mathcal T}^{\circ}',False,True,'misread symbol or index',
    'The curved-arrow label repeats the flag-topped domain graph with one lower curl, followed by a small open ring. Both were independently inspected in the half. The preferred tau/circle rendering preserves the explicit calligraphic-T alternative, with no consequential correction claim.',
    'medium','page',False,False)
add('NB note: underline',r'\uline{NB}','NB',r'\uline{NB}',False,True,'omission',
    'A short dark horizontal line is drawn below the NB letters, independent of the opening bracket.',
    'high','nb-note')
add('NB note: named index sign',r'\circ','0',r'\circ',False,True,'misread symbol or index',
    'The note gives a small round sign, matching the open rings on the two map labels. Circle is the preferred graphic encoding rather than a full-size digit zero.',
    'medium','nb-note',False,False)
add('NB note: verb describing reversal','renversé',r'\uncertain{remplacé}','renversé',
    False,True,'misread word',
    'The word has the low joined ren/ver sequence and its final accented vowel. There is no p descender or tall l supporting remplacé.',
    'high','nb-note',True,True)
add('NB note: operations and purpose clause',r"op. de $\pi$, pour",
    r'''\ill{} \ill{} \ill{}
\ill{}''',r"op. de $\pi$, pour",False,True,r'readable ink left as \ill{}',
    'The low op graph is followed by a distinct period, then de, pi and a detached comma. Pour begins with a long p stem and continues with a low joined return.',
    'high','nb-note',True,True)
add('NB note: final short form','à dr',r': \ill{}','à dr',False,True,'misread word',
    'The reduced two-part accented a is followed by a looped d and short r return. It is the phrase à dr, not a colon followed by missing words.',
    'high','nb-note',True)
add('NB note: closing delimiters and supposed trailing points','dr)',r'\ill{}) \ldots]','dr)',
    False,True,'text not on the page',
    'The note ends with a single rounded closing parenthesis. No suspension points or closing square bracket follow it. The opening square bracket is retained, leaving the source’s mismatched pair.',
    'high','nb-note',True)
add('after the NB note: opening of resumed prose','foncteur commutant',
    r'Foncteur \ill{} \ill{} commutant','foncteur commutant',False,True,'text not on the page',
    'The source begins with the lowercase, descending-loop f of foncteur. The next word is commutant, separated only by blank space; no additional words occupy H’s two illegible slots.',
    'high','page',True)
add('M0709: actor before the parenthesis',r'\unsure{\Gamma|F}',r'F',
    r'\unsure{\Gamma|F}',False,True,'misread symbol or index',
    'The heavily retraced letter has a long upper cap and thick stem, with a very short rightward spur low on the stem. The spur may be a foot on Gamma or a short F crossbar. Gamma remains the preferred first reading, with F explicitly retained; the later gamma variable does not decide the ink.',
    'low','actor',False,True)
add('compatibility sentence: number of the functor','le foncteur','les foncteurs','le foncteur',
    False,True,'misread word',
    'The article has only the l/e return, and foncteur ends in its r stroke without a separate s. Both source words are singular.',
    'high','page',False,True)
add('before the isomorphism display: abbreviation punctuation','des isom','des isom.','des isom',
    False,True,'text not on the page',
    'The short isom sequence at the start of the line ends in the m return. No independent full stop follows it.')
add('object condition below the display: overwritten operators',r'\operatorname{Ob}\operatorname{Rev}\Pi',
    r'\ill{}\ \Pi',r'\operatorname{Ob}\operatorname{Rev}\Pi',False,True,r'readable ink left as \ill{}',
    'After the membership sign, overlapping round and tall strokes support Ob; the following large looped R continues into small e/v joins before the final capital Pi. Heavy retracing makes the run compact, but no distinct canceled replacement is identifiable.',
    'medium','object-condition',True,True)
add('transitivity clause: connecting word','et avec transitivité','et une transitivité','et avec transitivité',
    False,True,'misread word',
    'The small word after et begins with an a-like loop and has a shallow v turn followed by an open terminal c. It does not have the two-hump ending of une.')
add('final line: words before cela','On trouve que','[no witness]','On trouve que',
    False,True,'omission',
    'A large looped O and short n begin the line. Trouve has a tall crossed t and compressed joined continuation; que has a long q descender.',
    'high','final-phrase')
add('final line: spelling and case of cela','celà','Cela','cela',True,True,'misread word',
    'The initial c is lowercase. No separate accent stroke is present above the final a or in its surrounding blank space; the visible high stroke belongs to the l/a joining structure, not a grave accent.',
    'high','final-phrase')
add('final line: last word','signifie',r'\ill{} \ill{} \ill{}','signifie',
    False,True,r'readable ink left as \ill{}',
    'The word has the small s, a dotted i, a long g descender, low n joins and a tall f, followed by the final i/e sequence. No terminal full stop is visible.',
    'high','final-phrase',True)
add('bottom-left pencil pagination',r'\mspage{25}','[no witness]',r'\mspage{25}',False,True,'omission',
    'A faint pencil 2 followed by 5 stands at the bottom left. Its writer is not identified on this sheet.')

decisions=[dict(
    id='M0709',decision='undecided',reading=r'\unsure{\Gamma|F}',
    ink='The upper cap is long, but the only lower rightward projection is a short low spur on a heavily retraced stem. It could be a Gamma foot or an F crossbar. Other clear F letters on the page have longer middle bars; this supports Gamma as the first alternative without resolving the letter.',
    crop='crops/143_scan026_A_actor.png',box=boxes['actor'],confidence='low'
)]
inventory=[]
def inv(n,kind,position,words,hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=f'E{n:02d}',kind=kind,position=position,
                          first_words_or_objects=words,transcribed='yes'))
inv(1,'margin note','top right','13','unnamed hand (pencil)')
inv(2,'text','top main line and following short line','considérer que ... domain set ... définit un foncteur')
inv(3,'deletion','between que and the set letter','doubtful le/que')
inv(4,'insertion','above définit at the top edge','(grâce à l’op. de pi)')
inv(5,'drawing','under the upper parenthetical addition','long curved attachment guide curling down just after the set letter')
inv(6,'diagram','upper third','Rev(Pi) to Ens with F label; pi-Ens below; upward arrow and curved arrow to Ens')
inv(7,'drawing','left of the upward arrow','two vertical parallel wavy strokes')
inv(8,'deletion','right of the upward arrow, above the replacement label','via : tilde Pi')
inv(9,'display','right of upward arrow, below canceled label','E maps to tilde Pi with circle exponent times subscript pi E')
inv(10,'display','along the lower right side of the curved arrow','E maps to domain-set letter with circle exponent wedge subscript pi E')
inv(11,'text','two lines below diagram','[underlined NB l’indice circle indique qu’on a renversé les op. de pi, pour faire opérer pi à dr)')
inv(12,'text','middle paragraph through des isom','foncteur commutant aux direct limits quelconques; Ceci dit ... disputed actor ... le foncteur F')
inv(13,'display','lower quarter','F of gamma-left-superscript Pi prime simeq F of Pi prime')
inv(14,'text','line below display','(Pi prime in Ob Rev Pi) fonctoriels en Pi prime,')
inv(15,'text','penultimate line','et avec transitivité pour gamma variable.')
inv(16,'text','last main line','On trouve que cela signifie')
inv(17,'margin note','bottom left','25','unnamed hand (pencil)')

remaining=[
    dict(place='opening canceled word',reading=r'\deleted{\unsure{le|que}}',alternatives='le; que; H’s ensemble is not securely supported by the exposed remnants',
         confidence='low',reason='The heavy horizontal strike and central overtracing hide the letter sequence. Existing crop: 143_scan026_A_opening-deletion.png.'),
    dict(place='opening domain-set letter',reading=r'\unsure{\tau|\mathcal T}',alternatives=r'\tau or \mathcal T',
         confidence='medium',reason='Shared provisional alphabet identification, confirmed from the flag-topped upper stroke and one lower return in the half. Preferred tau differs from H’s calligraphic T but does not claim a mathematical correction.'),
    dict(place='curved-arrow label: domain-set letter',reading=r'\unsure{\tau|\mathcal T}',alternatives=r'\tau or \mathcal T',
         confidence='medium',reason='The second occurrence was independently checked in the half and has the same graph; its small ring exponent is separately retained as circle.'),
    dict(place='M0709: actor letter',reading=r'\unsure{\Gamma|F}',alternatives=r'\Gamma or F',
         confidence='low',reason='Very short low spur on a thick stem does not securely distinguish a Gamma foot from an F crossbar. Existing crop: 143_scan026_A_actor.png.'),
]
notation=[
    dict(form=r'\unsure{\tau|\mathcal T}',meaning='The set used to define the functor from coverings.',evidence='Opening and curved-arrow label have the same flag-topped, one-return graph; both inspected and the shared alternative retained.'),
    dict(form=r'\circ',meaning='The sign the NB note says reverses the pi operations so that pi acts on the right.',evidence='Small open rings occur on the two diagram labels; the note names the same sign. Circle is the preferred graphic rendering rather than full-size zero, at medium confidence.'),
    dict(form=r'E',meaning='Variable object on the two map labels from pi-Ens.',evidence='Both labels explicitly begin E maps to an expression ending in E. These plain angular E letters are not treated as occurrences of the separate unresolved extension-group capital.'),
    dict(form=r'\widetilde\Pi^\circ\times_\pi E',meaning='Value of the upward diagram assignment.',evidence='The live label has a tilde, small ring, crossed multiplication strokes, a low pi index and final E.'),
    dict(form=r'\unsure{\tau|\mathcal T}^{\circ}\mathbin{\wedge}_{\pi}E',meaning='Value of the curved-arrow assignment.',evidence='A pointed wedge and physically low pi index follow the ringed domain-set letter. No upper index position is imposed.'),
    dict(form='two vertical wavy strokes',meaning='Literal relation mark beside the upward arrow.',evidence='Both curves are wavy; the candidate renders a rotated approx-shaped mark solely to reproduce the source orientation and shape.'),
    dict(form=r'\unsure{\Gamma|F}',meaning='The letter the prose says acts on Rev(Pi) via operations on Pi.',evidence='Cap, thick stem and very short low spur remain inconclusive. The gamma in the later formula is not used to force the capital’s identity.'),
]
abbreviations=[
    dict(form='op.',expansion='opérations'),
    dict(form='Rev',expansion='revêtements'),
    dict(form='Ens',expansion='ensembles'),
    dict(form='NB',expansion='nota bene'),
    dict(form='dr',expansion='droite'),
    dict(form='i.e.',expansion='id est'),
    dict(form='isom',expansion='isomorphismes'),
    dict(form='Ob',expansion='objets'),
]
hand_log=[
    dict(habit='The domain set letter has a flag-like cap and a single curved lower return.',places='143_scan026: opening and curved-arrow label.',scope='Both occurrences inspected; preferred tau and explicit calligraphic-T alternative follow shared notation.',misreadings='H uses calligraphic T; comparison flags record the preferred tau reading only, with medium confidence and no consequential claim.'),
    dict(habit='A thin curved insertion guide can resemble an opening parenthesis or a strike through a tall letter.',places='143_scan026: guide below the upper parenthetical addition and across the f of définit.',scope='One insertion attachment.',misreadings='H’s (discret) is not an additional parenthetical source phrase. The live word is définit.'),
    dict(habit='Canceled text can preserve detached punctuation between the strike strokes.',places='143_scan026: via : tilde Pi in the vertical-arrow label.',scope='This canceled label only.',misreadings='C omits the two-dot colon; H records only a canceled label description.'),
    dict(habit='Equivalence-style marks may be drawn vertically beside a vertical arrow.',places='143_scan026: pair of wavy strokes left of the upward arrow.',scope='Single relation graph, reproduced spatially.',misreadings='Both witnesses normalize it to a horizontal simeq; the source has two vertical wavy curves.'),
    dict(habit='A small open ring is used as an exponent and named again in prose.',places='143_scan026: upward assignment, curved assignment, NB note.',scope='All three ring occurrences inspected; graphic circle encoding retained at medium confidence.',misreadings='H renders each as digit zero.'),
    dict(habit='Reduced à can resemble two vertically stacked points.',places='143_scan026: final phrase à dr in the NB note; also the upper addition.',scope='Both local word contexts inspected.',misreadings='H gives a colon before its illegible end of the NB note.'),
    dict(habit='An unusually short low spur on a heavily retraced capital does not securely identify a crossbar.',places='143_scan026: M0709 actor after on veut que.',scope='Compared with the clear F letters elsewhere on the same page; uncertainty retained.',misreadings='H chooses F; C’s Gamma/F doubt remains unresolved.'),
    dict(habit='Closely joined Ob and Rev can appear to be a single overwritten cluster.',places='143_scan026: object condition below the isomorphism display.',scope='Single operator cluster inspected in a tight crop.',misreadings='H leaves the cluster illegible; the loops and stems support Ob Rev without identifying a separate canceled predecessor.'),
    dict(habit='Punctuation, capitalization and accents vary locally and are not normalized.',places='143_scan026: [NB ... dr); lowercase foncteur; singular le foncteur; isom without point; final cela without accent.',scope='Each listed place inspected individually.',misreadings='H adds a square closer/ellipsis, capitalizes foncteur and pluralizes its later occurrence, and adds a point after isom. C adds a grave accent to cela.'),
    dict(habit='Pencil numerals are kept without identifying their writer.',places='143_scan026: 13 at top right and 25 at bottom left.',scope='Both numerals present; no identifying evidence supplied by the sheet.',misreadings='H’s editorial de l’auteur attribution is not adopted; H omits bottom 25.'),
]
notes=[
    dict(id='143_scan026-N1',text='The opening continues a discussion by saying that the domain set, through its pi operation, defines a functor. The short canceled word remains doubtful. The added parenthesis and its long curved guide are preserved; the live verb is définit. This account reports the source construction without proving it.'),
    dict(id='143_scan026-N2',text='The triangular diagram has Rev(Pi), pi-Ens and Ens as its objects. It labels the upper functor F and supplies two assignments from a variable E. The canceled vertical-arrow label is read via : tilde Pi, including a newly recovered colon. The relation graph at the left is reproduced as two vertical wavy strokes rather than assigned a new mathematical meaning.'),
    dict(id='143_scan026-N3',text='The NB note says that the ring sign means the pi operations have been reversed to make pi act on the right. It literally opens with a square bracket and closes with a round parenthesis. Its short form dr and the point after op. remain as written.'),
    dict(id='143_scan026-N4',text='The page then calls the functor commuting with arbitrary direct limits and asks for compatibility with an action on Rev(Pi). The actor letter is still Gamma/F, and the ink does not justify correcting it from the later gamma variable. The displayed isomorphisms and the following object condition, functoriality and transitivity are transcribed as source assertions, not independently proved.'),
    dict(id='143_scan026-N5',text='The final words are On trouve que cela signifie, with lowercase cela and no visible accent or final stop. The page ends there. Both pencil page numerals are recorded with their hand unnamed.'),
]
check_events=[
    dict(statement_id='143_scan026-N1',type='carried as background without fault found',outcome='The opening words, cancellation and insertion attachment were visually checked. No functor construction was proved.'),
    dict(statement_id='143_scan026-N2',type='carried as background without fault found',outcome='All diagram objects, arrows, labels, products, low indices and deletions were inspected. The category equivalence and assignments were not mathematically verified.'),
    dict(statement_id='143_scan026-N3',type='carried as background without fault found',outcome='The author’s explanation of the ring was read and used to keep the three source graphs consistent. No independent proof concerning reversed actions was performed.'),
    dict(statement_id='143_scan026-N4',type='carried as background without fault found',outcome='The direct-limit and compatibility assertions were transcribed. No proof of commutation, the displayed isomorphisms, or transitivity was performed, and no mathematical expectation settled Gamma versus F.'),
]
raw_actions=[
    'Scan/page metadata syntax only; source 13 was visually checked.',
    'H’s de l’auteur attribution is editorial; pencil numerals retain unnamed hand.',
    'Canceled le/que remains doubtful, without accepting H ensemble. Domain graph retains preferred tau with explicit calligraphic-T alternative.',
    'Upper addition reads grâce à l’op. de pi; main-line définit is not a parenthetical discret. Attachment guide reconstructed.',
    'Définit is readable. H’s illegible slot does not require an extra source word before un foncteur.',
    'Diagram setup syntax only.',
    'Diagram spacing syntax only.',
    'Both vertical-arrow labels inspected: deleted via : tilde Pi, live E assignment, circular exponent, and two-wave vertical relation shape all recorded.',
    'The two bend angles are rendering choices, not distinct source facts; the curved arrow and its head were inspected.',
    'This raw-difference record is visibly malformed. The actual C/H witnesses were compared directly: both assignment labels, their objects, mapsto marks, products, indices and ring signs were inspected, with every material difference recorded.',
    'This second raw record is also malformed across fields. Direct witness comparison replaces its corrupted alignment; the curved label has preferred tau with explicit calligraphic-T alternative, ring exponent, wedge and low pi index.',
    'Circle graph retained in the NB note; H zero is a rendering difference recorded at medium confidence and non-consequential.',
    'Renversé selected from letters, not remplacé.',
    'Op. de pi, pour recovered, including the point after op. and comma after pi.',
    'À dr recovered, not colon plus missing text.',
    'No closing square bracket or suspension points after the source round parenthesis.',
    'M0709 remains Gamma/F, with Gamma first and H’s F explicitly alternative.',
    'Source has singular le foncteur.',
    'No full stop after isom.',
    'Display boundary syntax only. The condition is physically below the isomorphism display with the following prose.',
    'Ob Rev Pi recovered from the overwritten operator cluster.',
    'H’s note about an unread index is editorial. The source condition and its parentheses are fully retained, with no invented canceled predecessor.',
    'Avec selected, not une.',
    'On trouve que cela signifie recovered; C’s added grave on celà is removed. Bottom pencil 25 retained; no final period supplied.',
]
assert len(raw_actions)==len(packet['differences']), (len(raw_actions),len(packet['differences']))
report=dict(
    key='143_scan026',reader='A',stage='first',
    image_views=['original','half1','half2']+[f'crops/143_scan026_A_{x}.png' for x in boxes],
    changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining,certainty_resolutions=[],
    notation=notation,abbreviations=abbreviations,hand_log=hand_log,notes=notes,check_events=check_events,
    unresolved_for_main=[
        'Opening canceled word le/que, with H ensemble unsupported by the exposed sequence: crops/143_scan026_A_opening-deletion.png.',
        'Both domain-set letters retain the shared tau/calligraphic-T alternative; each was inspected in the halves. Alphabet-only preferred-reading rows are medium-confidence and non-consequential.',
        'M0709 Gamma/F remains unresolved: crops/143_scan026_A_actor.png. Short low spur could be a foot or a crossbar; no source slip is asserted from context.',
    ],
    raw_difference_disposition='All '+str(len(raw_actions))+' packet differences were inspected along with every agreement. Two raw records are malformed; their affected expressions were compared from the complete C/H witnesses rather than relying on corrupted token alignment. Pure macro, spacing and editorial descriptions do not become source text. Flags compare each preferred reading with the witnesses while explicit alternatives preserve doubt. Preferred tau and circle encoding rows are against_C false, against_H true, medium-confidence and non-consequential. No E/Sigma extension-group graph occurs on this page; the plain E variables in the diagram remain E. Detailed packet-order disposition:\n'+'\n'.join(f'{i+1}. {a}' for i,a in enumerate(raw_actions))
)
assert [d['id'] for d in decisions]==[m['id'] for m in packet['marks']]
for i,row in enumerate(changes,1):
    for field,witness in [('C','witness_C'),('H','witness_H')]:
        if row[field]!='[no witness]' and row[field] not in packet[witness]:
            raise ValueError(f'Change {i} {field} excerpt is not exact: {row[field]!r}')
    if row['final'] not in candidate:
        raise ValueError(f'Change {i} final excerpt is not exact: {row["final"]!r}')
    if row['crop']!='page' and not (ROOT/row['crop']).exists():
        raise ValueError(row['crop'])
path=ROOT/'reviews/143_scan026_readerA.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {path}: {len(changes)} changes, {len(decisions)} original marks, {len(inventory)} inventory elements, {len(remaining)} doubt records.')
