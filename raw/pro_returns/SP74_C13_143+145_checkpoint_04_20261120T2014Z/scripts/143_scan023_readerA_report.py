import json
from pathlib import Path

ROOT=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
packet=json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan023.json').read_text())
candidate=(ROOT/'reviews/143_scan023_readerA.tex').read_text()
boxes={
    'first-map':[480,278,1630,419],
    'interlinear-isom':[650,1455,1468,1630],
    'est':[1020,1640,1230,1745],
    'lower-indices':[620,1760,1125,1895],
    'diagram-target':[1165,1870,1640,2285],
    'closing':[435,2238,1645,2346],
}
changes=[]
def add(place,C,H,final,aC,aH,kind,ink,confidence='high',crop='page',marked=False,consequential=False):
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=aC,against_H=aH,kind=kind,ink=ink,
                        confidence=confidence,crop='page' if crop=='page' else f'crops/143_scan023_A_{crop}.png',
                        box=None if crop=='page' else boxes[crop],marked_in_H=marked,consequential=consequential))
def domain(place,crop='page'):
    add(place,r'\tau',r'\mathcal{T}',r'\unsure{\tau|\mathcal T}',False,False,'other',
        'The domain letter has a hooked upper stroke, an oblique descent and a lower right curl. It differs from the plain T in the Hom argument, but the ink alone on this page does not securely distinguish Greek tau from a calligraphic capital T. The same unresolved alphabet identification is applied at this occurrence.',
        'medium',crop,False,False)

add('opening: word introducing the first displayed map','à',r'\ill{}','à',False,True,r'readable ink left as \ill{}',
    'The reduced word consists of a small upper accent-like stroke over a dark lower body. Its two-part shape matches the à before tilde Pi in the lower diagram target; it is not treated as a new colon.',
    'medium','first-map')
add('first display: map label',r'\Phi',r'\ill{}',r'\Phi',False,True,r'readable ink left as \ill{}',
    'A large loop is crossed by a descending central stem with a small return at the foot. The following colon is two separate points.',
    'high','first-map',False,True)
domain('first display: domain letter','first-map')
add('first display: connecting stroke',r'\arrow[r,dash]',r'\to',r'\unsure{\longrightarrow|\mathbin{-}}',
    False,False,'other',
    'The shaft ends in a tiny asymmetric triangular thickening, unlike the more explicit head on the lower diagram arrow. The thickening could be a small head or a pressure-shaped endpoint. Both readings remain visible in the candidate.',
    'low','first-map',False,True)
add('first display: target',r'\operatorname{Hom}_{\mathrm{gr}}(T,\pi)',r'\ill{}',
    r'\operatorname{Hom}_{\mathrm{gr}}(T,\pi)',False,True,r'readable ink left as \ill{}',
    'A tall H is followed by compressed joined om; the low subscript has a descender and short shoulder supporting gr. The arguments show the plain capital T, a separate comma and a lowercase pi, enclosed by parentheses.',
    'high','first-map',False,True)
add('first prose paragraph: short form hom','hom','hom.','hom',False,True,'text not on the page',
    'The final m-stroke runs into the following blank before du. There is no independent full stop after hom.')
domain('first prose paragraph: groupoid in angle brackets')
add('first prose paragraph: abbreviation for coverings','rev.','revêt.','rev.',False,True,
    'abbreviation expanded or spelling modernised',
    'The short word has r, e and v followed by a detached point. It has neither a t nor a circumflex.')
add('first prose paragraph: constant or construits','constant','construits','constant',False,True,'misread word',
    'The word begins with the small rounded c/o sequence and continues through short n/s joins, a tall crossed t, the low a/n joins and the final t. There is no intervening r-u-i sequence supporting construits.',
    'high','page',False,True)
add('first prose paragraph: objects and value','objets et de valeur',
    r'''\ill{} ;
explic.\ : \ill{} à valeurs''',
    'objets et de valeur',False,True,'misread word',
    'The object word has the long j descender and a crossed t, followed by its final s. The next two short words are et and de. Valeur has a tall l and no separate final s. No source phrase explic. occurs here.',
    'high','page',True,True)
add('first prose paragraph: after ceux-ci','qui envoie donc',r'\ill{} dans','qui envoie donc',False,True,'misread word',
    'The first word has a descending q and dotted i; the next sequence has the joined humps of envoie. The following word begins with a tall d and ends in a short open c-like return.',
    'high','page',True,True)
add('first prose paragraph: first ens abbreviation',"l'ens","l'ens.","l'ens",False,True,'text not on the page',
    'The abbreviation ends with its small s stroke at the end of the line; no separate point follows it.')
add('first prose paragraph: object sent into pi','flèches',r'\ill{}','flèches',False,True,r'readable ink left as \ill{}',
    'The word has the long descending f, a tall l, an accent over the following vowel and the joined ch/e/s ending.',
    'high','page',True,True)
add('first prose paragraph: after the dash','et qui pour','et pour','et qui pour',False,True,'omission',
    'Between et and pour there is a small q with a descender followed by a short joined u/i graph.',
    'high','page',False,True)
domain('first prose paragraph: membership condition for t and t prime')
add('before the indexed pi','désignant par','pour','désignant par',False,True,'misread word',
    'The first word begins with d and an accented short vowel, then the dotted and descending joins of désignant. Par starts the next line with a long p descender.',
    'high','page',False,True)
add('interlinear Isom formula: relation sign',r'=\operatorname{Isom}',r'\simeq\; \mathrm{Isom}',
    r'\simeq\operatorname{Isom}',True,False,'misread symbol or index',
    'The upper stroke visibly rises and falls in a wave, while the lower stroke is short and straight. This is a simeq-shaped relation, not two parallel straight equals strokes.',
    'high','interlinear-isom',False,True)
domain('interlinear Isom formula: groupoid subscript','interlinear-isom')
add('interlinear Isom formula: attachment guide','[no witness]','rattaché par un trait',
    r'\draw[thin] (1.02,-0.12) .. controls (0.78,0.28) and (1.05,0.40) .. (2.10,0.40) .. controls (3.55,0.40) and (5.35,0.65) .. (5.10,0.76);',
    True,False,'drawing or diagram',
    'A fine curved guide runs beneath the added formula, curling down toward the gap just after the main-line indexed pi and extending right beneath the addition. It has no arrowhead and is not a strike through the formula.',
    'high','interlinear-isom')
add('definition of indexed pi: second ens abbreviation',"l'ens","l'ens.","l'ens",False,True,'text not on the page',
    'The final s-like return in ens is joined to the word; no detached period is present before des.',
    'high','interlinear-isom')
add('after lambda t equals t prime: est','est',r'\ill{}','est',False,True,r'readable ink left as \ill{}',
    'A heavily retraced low e/s body ends in the pointed return of t. Its compressed form matches the est that begins the closing sentence. The extra-looking horizontal stroke is part of the retraced graph; no independent cancellation is identified.',
    'medium','est',True,True)
add('inclusion sentence: comma in the indexed pi',r"\pi_{t,t'}",r"\pi_{t t'}",r"\pi_{t,t'}",
    False,True,'misread symbol or index',
    'The first t’s joined right return descends below the subscript baseline, supplying the comma; the second t’s short attached return remains high, supplying the prime. The same contrasting returns occur in the first indexed pi.',
    'high','lower-indices',False,True)
add('before the lower functor diagram','Ce foncteur','Le foncteur','Ce foncteur',False,True,'misread word',
    'The initial capital has an open curved C outline followed by a small e. It lacks the upright-plus-foot structure of an L.')
domain('lower functor diagram: domain in angle brackets')
add('lower functor diagram: abbreviation in target','rev.','revêt.','rev.',False,True,
    'abbreviation expanded or spelling modernised',
    'The target again has the short r/e/v graph and its point, without an added ê or t.',
    'high','diagram-target')
add('lower functor diagram: restriction to equal coverings','égaux à',r'\ill{}',
    r'''égaux}\\
\text{à }''',False,True,r'readable ink left as \ill{}',
    'The word begins with an accented short vowel and the long descending g, then the low aux strokes. The next line begins with the same reduced two-part à graph as the first display’s introduction.',
    'high','diagram-target',True,True)
add('lower functor diagram: relation and opening parenthesis',r'\widetilde\Pi\\\simeq(',
    r'($\widetilde{\Pi}$ ;',r'''\widetilde\Pi\\
\simeq(''',False,True,'misread symbol or index',
    'Tilde Pi stands on its own line after the restriction. Below it, a heavily retraced sign has an upper wavy body and a lower horizontal stroke, followed by an opening parenthesis. There is no semicolon after tilde Pi, and the parenthesis does not begin before it.',
    'medium','diagram-target',False,True)
add('lower functor diagram: first words in parenthesis','un objet',r'\uncertain{un seul objet}',
    'un objet',False,True,'text not on the page',
    'The low un is followed directly by the object word. There is no intervening group of strokes long enough for seul.',
    'high','diagram-target',True,True)
add('lower functor diagram: short form for isomorphisms',"d'isom---",r"d'\uncertain{isom.}","d'isom---",
    False,True,'abbreviation expanded or spelling modernised',
    'After d and its apostrophe, the compressed isom graph ends in a long continuation shaft. No detached abbreviation period is visible.',
    'medium','diagram-target',True)
add('lower functor diagram: after the closing parenthesis',r'\pi)',r'$\pi$) \ldots',r'\pi)',
    False,True,'text not on the page',
    'The lower pi is followed by a large closing curve. There are no three suspension points after this parenthesis; the separate closing prose is below.',
    'high','diagram-target')
add('closing prose: before the action-group letter','est évidemment compatible avec op. de',r'\ill{}',
    'est évidemment compatible avec op. de',False,True,r'readable ink left as \ill{}',
    'The first compressed word matches the earlier est. Évidemment has its initial accent and dotted i, compatible has tall crossed/looped middle letters, and the shorter final sequence reads avec op. de. These words occupy the upper of the two compressed closing lines.',
    'medium','closing',True,True)
add('closing prose: action-group letter',r'\mathcal E',r'\Sigma',r'\unsure{\mathcal E|\Sigma}',
    False,False,'other',
    'The letter has three rounded horizontal returns with an open right side, compatible with a cursive E but not sufficient to settle the run’s rounded E/Sigma ambiguity. Shared uncertainty is retained, without claiming a mathematical correction.',
    'low','closing',False,False)
add('closing prose: word before the final sur','donc','donné','donc',False,True,'misread word',
    'The initial d is tall and looped. The word finishes with a short open return; no second n or accented final e is separately present.',
    'high','closing')
add('closing prose: number of continuation points',r'\pi\ldots',r'$\pi$ \ldots',r'\pi\ldots.',
    True,True,'omission',
    'Four distinct dark points follow the last pi. The first display has three, providing a within-page contrast; the final four are not reduced to three.',
    'high','closing')
add('closing prose: H’s extra tail after the final pi',r'$\pi\ldots$',
    r'''compatibles \ill{}
\ill{} \ldots''',r'$\pi\ldots.$',False,True,'text not on the page',
    'After the final pi and its four points the lower line ends. The compatible word belongs to the upper closing line and is singular; no extra compatibles or further words follow the last points.',
    'high','closing',True)
add('bottom-left pencil pagination',r'\mspage{22}','[no witness]',r'\mspage{22}',False,True,'omission',
    'Two faint pencil 2 digits stand at the lower left. No page-local evidence identifies the writer of these numerals.')

decisions=[dict(
    id='M0703',decision='undecided',reading=r'\unsure{\Pi|\widetilde\Pi}',
    ink='The lower capital has two upright legs and a dark cap. The wave-like ink just above it overlaps the middle/lower strokes of évidemment on the line above. A separate tilde cannot be securely isolated or excluded from this crop, so the original alternatives remain.',
    crop='crops/143_scan023_A_closing.png',box=boxes['closing'],confidence='medium'
)]

inventory=[]
def inv(n,kind,position,words,hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=f'E{n:02d}',kind=kind,position=position,
                          first_words_or_objects=words,transcribed='yes'))
inv(1,'text','top two lines and short continuation before display','G — lequel opère donc sur T. Ceci donne naissance automatiquement à')
inv(2,'diagram','upper display','Phi: domain letter; disputed shaft/head; Hom subscript gr(T,pi); three continuation points at the right')
inv(3,'text','from Ceci dit to désignant at right end of line','hom du groupoïde; rev. universels; constant sur les objets et de valeur tilde Pi; qui envoie donc l’ens des flèches; et qui pour t,t prime')
inv(4,'text','main line beneath the insertion','par pi subscript t,t prime; l’ens des lambda in pi')
inv(5,'insertion','above the line after indexed pi','simeq Isom subscript angle-bracketed domain,pi of (t,t prime)')
inv(6,'drawing','under the interlinear formula','thin curved attachment guide without an arrowhead')
inv(7,'text','following two prose lines','tels que lambda t=t prime, est l’inclusion de pi subscript t,t prime dans pi. Ce foncteur')
inv(8,'diagram','lower third, source and arrow at left','angle-bracketed domain,pi with a clear rightward arrow')
inv(9,'text','target block at right of lower arrow','Cat des rev. universels de Pi égaux à tilde Pi')
inv(10,'display','below restriction in target block','simeq (un objet et groupe d’isom--- pi)')
inv(11,'text','two compressed lines along lower edge','est évidemment compatible avec op. de action group sur disputed Pi/tilde Pi donc sur pi, four points')
inv(12,'margin note','bottom left','22','unnamed hand (pencil)')

remaining=[]
for place in ['first displayed map','first prose groupoid','membership condition for t,t prime','interlinear Isom subscript','lower functor diagram']:
    remaining.append(dict(place='domain alphabet: '+place,reading=r'\unsure{\tau|\mathcal T}',
                          alternatives=r'\tau or \mathcal T',confidence='medium',
                          reason='The repeated hooked upper bar and curled lower return can encode either Greek tau or calligraphic T. The page distinguishes it from plain T but does not independently name the alphabet. All five occurrences were inspected; representative crop 143_scan023_A_first-map.png, with the small form also in 143_scan023_A_interlinear-isom.png.'))
remaining.append(dict(place='first map: arrowhead',reading=r'\unsure{\longrightarrow|\mathbin{-}}',
                      alternatives='right arrow with tiny head or bare shaft',confidence='low',
                      reason='The tiny triangular endpoint may be a head or pressure thickening. Existing crop: 143_scan023_A_first-map.png.'))
remaining.append(dict(place='closing action-group letter',reading=r'\unsure{\mathcal E|\Sigma}',
                      alternatives=r'\mathcal E or \Sigma',confidence='low',
                      reason='The rounded capital remains within the shared run-level ambiguity; no separate mathematical correction is asserted. Existing crop: 143_scan023_A_closing.png.'))
remaining.append(dict(place='M0703: closing action target',reading=r'\unsure{\Pi|\widetilde\Pi}',
                      alternatives=r'\Pi or \widetilde\Pi',confidence='medium',
                      reason='Possible overmark is entangled with the writing of évidemment immediately above. Existing crop: 143_scan023_A_closing.png.'))

notation=[
    dict(form=r'\unsure{\tau|\mathcal T}',meaning='Domain/object parameter set in the first map and angle-bracketed groupoid.',evidence='All five occurrences share the hooked upper stroke and curled lower return. The plain T of the Hom argument is graphically distinct; the script/Greek identification remains open.'),
    dict(form=r'T',meaning='The object acted on in the opening sentence and first Hom argument.',evidence='Plain T has a horizontal cap and near-vertical stem, unlike the curled domain letter.'),
    dict(form=r'\Phi',meaning='Label of the first displayed map.',evidence='Large loop with central descending stem and lower return before a colon.'),
    dict(form=r'\pi_{t,t'+ "'" +r'}',meaning='The set described as the lambda in pi carrying t to t prime.',evidence='Both source index pairs retain a low joined comma and a higher joined prime.'),
    dict(form=r'\simeq',meaning='Relation between the indexed set and the Isom expression in the addition.',evidence='Wavy upper and straight lower strokes; this changes C’s equals sign.'),
    dict(form=r'\unsure{\mathcal E|\Sigma}',meaning='Group said to act in the closing compatibility sentence.',evidence='One rounded capital occurrence on this page; shared ambiguity retained at low confidence.'),
]
abbreviations=[
    dict(form='hom',expansion='homomorphisme'),
    dict(form='Hom',expansion='homomorphismes'),
    dict(form='gr',expansion='groupes'),
    dict(form='rev.',expansion='revêtements'),
    dict(form="l'ens",expansion="l'ensemble"),
    dict(form='Isom',expansion='isomorphismes'),
    dict(form='Cat',expansion='catégorie'),
    dict(form='isom---',expansion='isomorphismes'),
    dict(form='op.',expansion='opération'),
]
hand_log=[
    dict(habit='The domain graph has a hooked cap and curled lower stem, unlike plain capital T.',places='143_scan023: first map, first groupoid, membership condition, inserted Isom subscript, lower functor domain.',scope='All five occurrences confirmed as the same graphic form; Greek tau versus calligraphic T remains open.',misreadings='C encodes tau, H calligraphic T. Neither is conclusively rejected here.'),
    dict(habit='A comma or prime can join the cross stroke of a small subscript t, making an h-like pair.',places='143_scan023: both pi subscripts, before the Isom insertion and in the inclusion sentence.',scope='Both index pairs inspected in their single crops. The first return descends below the baseline; the second stays high.',misreadings='H omits the comma in the lower inclusion subscript.'),
    dict(habit='A reduced à consists of an upper accent-like stroke and a tiny lower body.',places='143_scan023: before the first map and before tilde Pi in the lower diagram target.',scope='Both inspected and compared.',misreadings='H leaves these areas illegible; the first reduced à could otherwise resemble a colon.'),
    dict(habit='A g descender can run far left beneath neighboring content.',places='143_scan023: égaux and groupe in the lower diagram target.',scope='These two words only.',misreadings='The long return of g in égaux must not become an added separator or underline.'),
    dict(habit='The word est can compress into a low retraced body and pointed final t return.',places='143_scan023: est l’inclusion and the opening of the closing sentence.',scope='Both within-page forms compared; no independent cancellation identified.',misreadings='H leaves the earlier word and much of the closing clause illegible.'),
    dict(habit='Heavy retracing does not itself establish deletion.',places='143_scan023: est l’inclusion and the simeq before the lower parenthesis.',scope='These two dark graphs inspected; no separately identifiable canceled text recovered.',misreadings='No deletion is supplied merely from the thick strokes.'),
    dict(habit='The number of suspension points varies within the page.',places='143_scan023: first display has three; final pi has four.',scope='Both endings inspected in crops.',misreadings='C and H render only three after the final pi. H also adds suspension text after the diagram’s closing parenthesis.'),
    dict(habit='Short forms preserve their actual endings and punctuation.',places='143_scan023: hom; both rev.; both l’ens; lower d’isom---.',scope='Every occurrence listed was inspected.',misreadings='H supplies a period after hom and both ens, lengthens both rev. to revêt., and replaces the continuation dash after isom with a period.'),
    dict(habit='The closing target’s potential overmark overlaps an earlier line.',places='143_scan023: M0703 beneath évidemment.',scope='Only this compressed lower-edge occurrence.',misreadings='H gives bare Pi; C’s Pi/tilde Pi uncertainty is retained because the strokes cannot be separated securely.'),
    dict(habit='Pencil pagination has no named attribution on the sheet.',places='143_scan023: bottom-left 22.',scope='The only page numeral found in the original/half inspection.',misreadings='H omits the numeral; the hand remains unnamed.'),
]
notes=[
    dict(id='143_scan023-N1',text='The page continues a statement about a G action on T and displays a map labeled Phi into Hom of groups from T to pi. The domain’s tau/calligraphic-T identification and the first connector’s head remain uncertain. The notation is transcribed as evidence, without proving the construction.'),
    dict(id='143_scan023-N2',text='The author describes a homomorphism of the angle-bracketed groupoid into the groupoid of universal coverings of Pi, constant on objects with value tilde Pi. The prose defines the indexed pi sets by lambda t=t prime and identifies the induced maps as inclusions. An interlinear Isom description is attached by a curved guide. Its visible relation is simeq, not the equals sign of witness C. No proof of these assertions was performed.'),
    dict(id='143_scan023-N3',text='The lower diagram describes the category of universal coverings of Pi equal to tilde Pi and then writes a comparison with a single object having isomorphism group pi. The manuscript says un objet, not un seul objet. Its isom--- abbreviation and the restriction égaux à tilde Pi are retained literally.'),
    dict(id='143_scan023-N4',text='The closing sentence states compatibility with the action of the unresolved E/Sigma group on a Pi whose possible tilde overlaps the line above, and consequently on pi. Four final suspension marks are present. H’s later compatibles and additional illegible tails are not separate manuscript words after the final pi.'),
    dict(id='143_scan023-N5',text='No independently identifiable deletion was found on this page. The interlinear formula is an insertion, and its thin curved attachment stroke is reproduced as a drawing. The pencil 22 is attributed only to an unnamed hand.'),
]
check_events=[
    dict(statement_id='143_scan023-N1',type='carried as background without fault found',outcome='Only the writing of the map, its arguments, and the connector endpoints was visually checked. No mathematical construction or homomorphism property was proved.'),
    dict(statement_id='143_scan023-N2',type='carried as background without fault found',outcome='The source’s definition, relation sign, indices, and insertion attachment were visually checked. The groupoid and inclusion assertions were not independently proved.'),
    dict(statement_id='143_scan023-N3',type='carried as background without fault found',outcome='The diagram and explanatory parenthesis were transcribed; the stated category comparison was not mathematically verified.'),
    dict(statement_id='143_scan023-N4',type='carried as background without fault found',outcome='The compatibility sentence was read as manuscript text. No mathematical check decided the target Pi versus tilde Pi, which remains doubtful.'),
]
raw_actions=[
    'Scan metadata only; not an additional manuscript numeral.',
    'Reduced à and Phi label recovered; first displayed map inspected as a whole.',
    'Domain alphabet remains tau/calligraphic T; connector head remains open; Hom-gr target recovered.',
    'Actual Hom target contains (T,pi); H’s token alignment is incomplete and the full formula was checked visually.',
    'No full stop after hom.',
    'First groupoid domain alphabet remains tau/calligraphic T.',
    'Literal rev. retained, not lengthened to revêt.',
    'Constant selected from strokes, not construits.',
    'Objets et de valeur recovered; no explic. or plural valeurs supplied.',
    'Qui envoie donc recovered; H’s dans does not replace this phrase.',
    'No period after the first l’ens.',
    'Flèches recovered from f, l, accent and ending.',
    'Qui is present between et and pour.',
    'Membership-condition domain alphabet remains tau/calligraphic T.',
    'Désignant par recovered rather than pour.',
    'Simeq selected from the wavy upper stroke, changing C equals.',
    'Inserted Isom subscript retains the same unresolved domain alphabet.',
    'H’s editorial insertion description is not source prose; the actual addition and curved attachment guide are reconstructed.',
    'No period after the second l’ens.',
    'Est recovered from its compressed graph and compared with the later est.',
    'Comma retained in the lower indexed pi; the low attached return contrasts with the higher prime.',
    'Ce foncteur, not Le foncteur.',
    'Diagram-environment syntax only.',
    'Lower functor domain alphabet remains tau/calligraphic T.',
    'Both representations have the lower right arrow; its visible head was confirmed.',
    'Second rev. also remains unexpanded.',
    'Égaux à tilde Pi recovered as the category restriction.',
    'Source has tilde Pi followed below by simeq and then the opening parenthesis; H’s semicolon/parenthesis placement rejected.',
    'No seul between un and objet.',
    'Literal d’isom--- retained; no abbreviation period supplied.',
    'Closing est évidemment compatible avec op. de recovered; E/Sigma remains shared low-confidence, non-consequential ambiguity.',
    'M0703 remains Pi/tilde Pi due overlap with upper line; donc selected over donné.',
    'Pencil 22 retained; H’s extra compatibles and illegible tail after the final pi are not source text. Four source points, not three, end the clause.',
]
assert len(raw_actions)==len(packet['differences']), (len(raw_actions),len(packet['differences']))
report=dict(
    key='143_scan023',reader='A',stage='first',
    image_views=['original','half1','half2']+[f'crops/143_scan023_A_{x}.png' for x in boxes],
    changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining,certainty_resolutions=[],
    notation=notation,abbreviations=abbreviations,hand_log=hand_log,notes=notes,check_events=check_events,
    unresolved_for_main=[
        'All five domain-letter occurrences: tau versus calligraphic T. Representative crops/143_scan023_A_first-map.png; small subscript form also in crops/143_scan023_A_interlinear-isom.png. Full-page and halves confirmed the same graph at the other three places.',
        'First display’s endpoint: tiny arrowhead versus bare shaft. crops/143_scan023_A_first-map.png.',
        'One closing action-group letter: E/Sigma, shared ambiguity, low confidence and non-consequential. crops/143_scan023_A_closing.png.',
        'M0703 closing Pi versus tilde Pi: possible overmark overlaps évidemment above. crops/143_scan023_A_closing.png.',
    ],
    raw_difference_disposition='All '+str(len(raw_actions))+' packet differences were inspected against the original, both halves and the six single-locus crops. Every word and symbol was also inspected where C and H agree. Pure macro, spacing and editorial-description differences are excluded as source words. Unresolved witness conflicts set both against_C and against_H false because no witness has been conclusively rejected. Domain alphabet rows are medium-confidence/non-consequential; the pure E/Sigma row is low-confidence/non-consequential. Detailed packet-order disposition:\n'+'\n'.join(f'{i+1}. {a}' for i,a in enumerate(raw_actions))
)
assert [d['id'] for d in decisions]==[m['id'] for m in packet['marks']]
for i,row in enumerate(changes,1):
    for field,witness in [('C','witness_C'),('H','witness_H')]:
        if row[field]!='[no witness]' and row[field] not in packet[witness]:
            raise ValueError(f'Change {i}: {field} excerpt is not exact: {row[field]!r}')
    if row['final'] not in candidate:
        raise ValueError(f'Change {i}: final excerpt is not exact: {row["final"]!r}')
    if row['crop']!='page' and not (ROOT/row['crop']).exists():
        raise ValueError(row['crop'])
path=ROOT/'reviews/143_scan023_readerA.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {path}: {len(changes)} changes; {len(decisions)} original marks; {len(inventory)} inventory elements; {len(remaining)} doubt records.')
