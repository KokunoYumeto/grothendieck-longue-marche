from pathlib import Path
import csv
import json

OUT=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan044')
PACKET=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan044')
candidate=(OUT/'candidate.tex').read_text()
manifest=json.loads((OUT/'crop_plan.json').read_text())
crop={r['label']:r for r in manifest}
def ev(label):return {'crop':crop[label]['crop'],'box':crop[label]['box']}
def macro_at(prefix):
    start=candidate.index(prefix)
    left=candidate.index('{',start)
    depth=0
    for i in range(left,len(candidate)):
        if candidate[i]=='{':depth+=1
        elif candidate[i]=='}':
            depth-=1
            if depth==0:return candidate[start:i+1]
    raise AssertionError(prefix)
upper_note=macro_at(r'\margin{Finalement')
caution=macro_at(r'\margin{\figure{')
signature=macro_at(r'\diagram{')
complex_formula=r'\[S_*\mathcal TD_{\mathrm{top}}^+\quad\text{ou}\quad S_*\mathcal TD_{\mathrm{top}},\]'
final_descriptor="``\\uline{groupoïde de Teichmüller} \\inserted{\\uline{orienté}} \\uline{spécial dévissé topologique}''"

changes=[]
def ch(place,c,h,final,ink,label,confidence,kind,ac,ah,math=False,marks=None):
    row=dict(place=place,c=c,h=h,final=final,ink=ink,**ev(label),confidence=confidence,
             kind=kind,against_c=ac,against_h=ah,math=math)
    if marks:row['mark_ids']=marks
    changes.append(row)

ch('Title: underline and full stop',r'\uline{Groupoïdes de Teichmüller.}',
   r'\emph{Groupoïdes de Teichmüller.}',r'\uline{Groupoïdes de Teichmüller}.',
   'The long rule ends under the last letter of Teichmüller. The separate dark full stop lies farther right, beyond the end of the rule.',
   'title','high','other',True,True)
ch('First groupoid descriptor: terminal colon','(nothing)',':','',
   'The closing parenthesis is visible at the right end of the descriptor. No separate two-dot colon follows it; the oblique margin writing begins farther above and to the right.',
   'oriented_definition','high','text not on the page',False,True)
ch('Objects label: initial case',r'\uline{Objets}',r'\emph{objets}',r'\uline{objets}',
   'The initial small o loop stays below the following tall b stroke. The label has its own short underline and a two-dot colon.',
   'oriented_definition','high','misread word',True,False)
ch('Surface label after orientées',r'(\Sigma)',r'(\ill{})',r'(\Sigma)',
   'Inside the parentheses the sign has a broad upper arm, an angled central return and a lower arm. These strokes support capital Sigma; the neighboring oblique note has a different baseline.',
   'oriented_definition','medium',r'readable ink left as \ill{}',False,True,True)
ch('Punctuation after the surface label','.',',',r'\unsure{,|.}',
   'A small mark follows the closing parenthesis, close to the crossing oblique note. A descending comma-like form is possible, but its separation from the neighboring strokes is insufficient to settle comma against full stop.',
   'oriented_definition','low','other',True,False)
ch('Flèches definition: terminal stop','(nothing)','.','',
   'The line ends with the closing parenthesis after orientation. There is no separate dark full stop after that parenthesis in the visible blank to its right.',
   'oriented_definition','high','text not on the page',False,True)
ch('Upper margin: opening word','Finalement',r'\uncertain{Finalement}','Finalement',
   'A tall F with a detached upper bar is followed by the dotted i, low joined n/a strokes, a tall l and the remaining -ement run. The comma is separate.',
   'upper_note','high','other',False,True)
ch('Upper margin: first clause',"tant qu'on ne travaille pas au point de vue arithmétique",
   r'pour \ill{} \uncertain{travaux} \ill{} \uncertain{ultérieurs}',
   "tant qu'on ne travaille pas au point de vue arithmétique",
   'The first line ends with the tall initial t and final t of tant. The next line has qu’on ne, followed by the tall t and paired l strokes in travaille and the short pas at the edge. Au point de vue is on the next line; the arith-/métique sequence continues across the line break with its tall stems and q descender visible.',
   'upper_note','high','misread word',False,True)
ch('Upper margin: words before gros',"c'est le",'(nothing)',"c'est le",
   'Before the long-descending g there are the short c, apostrophe and est run, followed by the tall looped l and small e. These words are live.',
   'upper_note','high','omission',False,True)
ch('Upper margin: M0679',r'\unsure{gros|gr.}','(nothing)','gros',
   'The g has a closed upper bowl and long descender. After its short r, two further low letter turns are visible for o and s; the ending is not merely a terminal abbreviation point.',
   'upper_note','high','misread word',True,True,marks=['M0679'])
ch('Upper margin: qui and M0680',r'qui \unsure{sera|offre|soit}',r'\uncertain{soit}','qui sera',
   'Qui is visible after the raised sign of the calligraphic T. The following word is compressed into low joined strokes, ending in a small a-like turn rather than a tall t. The long nearby descending stroke belongs to que on the line above; it does not provide two f stems for offre. Sera is retained at medium confidence.',
   'upper_note','medium','misread word',True,True,marks=['M0680'])
ch('Upper margin: M0681',r'\unsure{utilisé}','utilisé','utilisé',
   'The word contains a low initial u, a short crossed t, separate dot/stem traces for the i letters and a tall looped l. The final accented ending is visible before the punctuation.',
   'upper_note','high','misread word',True,False,marks=['M0681'])
ch('Upper margin: cancelled word after utilisé',r"\deleted{\unsure{tout|d'où}}",
   '(nothing)',r"\deleted{\unsure{tout|d'où}}",
   'A horizontal cancellation crosses a short word after the punctuation. Tall residual strokes survive near its ends, but the dense middle does not certify every letter. The alternatives tout and d’où remain in doubt rather than being omitted.',
   'upper_note','low','omission',False,True)
ch('Upper margin: M0682',r'\unsure{mérite}',r'\uncertain{mérite}','mérite',
   'The initial low m run is followed by an accented e, a short r, a dotted i, the tall t and a small final e. The tall t is distinct from the descender of qui immediately before it.',
   'upper_note','high','misread word',True,True,marks=['M0682'])
ch('Upper margin: short form M0683',r'\unsure{gr.\ or.|groupoïde|groupe}',
   'groupoïde',r'\unsure{gr.\ or.}',
   'After le there is a long-descending g and a short low run, then another small group. The long full forms would require additional letter stems and descenders that are not distinct here. The apparent abbreviated gr. or. is retained in doubt; neither the exact terminal letters nor both points are fully certified.',
   'upper_note','low','abbreviation expanded or spelling modernised',False,True)
ch('Upper margin: final verbal phrase',"de s'appeler","s'appellera","de s'appeler",
   'A separate d-loop and e precede s and the apostrophe. The following word has the paired tall l strokes and a low final return; there is no separate final a after it at the edge.',
   'upper_note','medium','misread word',False,True)
ch('Bioriented definition: necessity abbreviation','néct.','néc.',r'néc\textsuperscript{t}.',
   'The accented néc remains on the baseline. A small t is raised at its right, and a separate full stop is lower, before l’orientation. The t is neither a baseline final letter nor absent.',
   'bioriented_prose','high','abbreviation expanded or spelling modernised',True,True)
ch('One-object paragraph: autom abbreviation',"d'autom","d'automorphismes","d'autom",
   'After d’ the short a/u/t/o/m run ends before the gap to the sign and numeral. No continuation morphismes is written, and no distinct terminal abbreviation point is present there.',
   'one_object','high','abbreviation expanded or spelling modernised',False,True)
ch('Fibre line: parenthetical phrase','(ou noyau)',r'(en \uncertain{n’importe}\ \ill{})','(ou noyau)',
   'The first word has a small closed o followed by the low u turn. In noyau the y has the long descending diagonal, followed by the low joined a/u ending. There are no extra letters corresponding to n’importe.',
   'fibre','high','misread word',False,True)
ch('Lower margin: initial doubtful word',r'\unsure{Canulé|Cautèle}',r'\uncertain{canulé}',
   r'\unsure{Canulé|Cautèle}',
   'The first letter is a large open capital C, followed by a closed a, two compressed middle letter groups, a tall looped stroke and an accented ending. The middle groups do not securely distinguish the proposed readings; the doubt remains.',
   'caution','low','misread word',False,True)
ch('Lower margin: M0685',r"\unsure{si on ne se borne|désormais borner|n'a un sens}",
   'si on ne se borne','si on ne se borne',
   'The line begins with s and a separate upright i, followed by the short on and ne groups. Se precedes a clear tall b, rounded o and low -rne ending. The visible word spacing and these stems support si on ne se borne.',
   'caution','high','misread word',True,False,marks=['M0685'])
ch('Lower margin: continuation','à des surfaces connexes!',r'\uncertain{à des surfaces connexes} !',
   'à des surfaces connexes!',
   'The à has its separate accent; des has a looped d and low ending. Surfaces continues across the third line, and connexes is on the last line with its crossed x and final s. The exclamation stroke and its detached dot are clear.',
   'caution','high','other',False,True)
ch('Lower margin: long hooked stroke','(no separate graphic stroke)',
   '(no separate graphic stroke)',caution,
   'Beside the lower words a strong long stroke descends and turns left into a broad hook. The exclamation mark has its own separate shaft and dot to the right. The long hook is reproduced as visible ink without forcing a semantic meaning on the enclosure-like form.',
   'caution','high','drawing or diagram',True,True)
ch('Final descriptor: underlined insertion',r'\inserted{orienté} within the underlined descriptor',
   r'\add{orienté} outside the two emphasized descriptor segments',r'\inserted{\uline{orienté}}',
   'Orienté is on an elevated baseline between Teichmüller and spécial. A short rule runs directly under the inserted word; it is not crossed out.',
   'complex','high','insertion or placement',False,True)
ch('Final descriptor: coined term','dévissé','divisé','dévissé',
   'After the tall d, the first vowel has an accent. The following v, dotted i and two successive s turns precede the accented final e. The source has the longer dévissé sequence.',
   'complex','high','misread word',False,True)
ch('Final descriptor: terminal full stop','(nothing)','.','',
   'Two raised closing quotation strokes follow the end of topologique. No separate baseline full stop follows those strokes in the visible right edge.',
   'complex','high','text not on the page',False,True)
ch('Bottom foliation',r'\mspage{43}','(nothing)',r'\margin{43}',
   'The bottom-left figures are an open 4 with a long right upright and a 3 with two curved parts joined at the waist. They are in a separate thin hand, unlike the dark top-page 1 and circled section numeral.',
   'folio43','high','other',True,True)

decisions=[]
def dec(mid,decision,reading,ink,label,confidence):
    decisions.append(dict(id=mid,decision=decision,reading=reading,ink=ink,**ev(label),confidence=confidence))
dec('M0679','first','gros','The g bowl and long descender are followed by r and two additional low o/s turns, without an isolated terminal abbreviation point.','upper_note','high')
dec('M0680','first','sera','The compressed low word ends in an a-like turn; no final t staff is distinct. The neighboring tall descender belongs to que above, not to two f letters.','upper_note','medium')
dec('M0681','first','utilisé','The u, crossed t, dotted i traces, tall l and accented final ending are visible.','upper_note','high')
dec('M0682','first','mérite','The m run, accent, short r, dotted i, tall t and small final e are distinguishable.','upper_note','high')
dec('M0683','undecided',r'\unsure{gr.\ or.}','The short post-g run and another small group favor an abbreviation, but exact terminal letters and points remain uncertain. The full groupoïde/groupe readings are not certified.','upper_note','low')
dec('M0684','undecided',r'\unsure{Canulé|Cautèle}','Capital C, closed a, compressed middle groups, a tall looped stroke and an accented ending are visible; the middle letters do not settle the word.','caution','low')
dec('M0685','first','si on ne se borne','Separate si/on/ne/se groups precede the tall b, rounded o and low -rne ending.','caution','high')

unresolved=[]
def un(place,reading,issue,alternatives,confidence,label):
    unresolved.append(dict(place=place,reading=reading,issue=issue,alternatives=alternatives,confidence=confidence,**ev(label)))
un('Punctuation after the surface label',r'\unsure{,|.}',
   'The small mark is crowded by the oblique margin note; comma and full stop are not cleanly separated.',[',','.'],'low','oriented_definition')
un('Upper margin: cancelled word',r"\deleted{\unsure{tout|d'où}}",
   'The horizontal cancellation hides parts of the short word; all letters are not plain.',['tout',"d’où"],'low','upper_note')
un('Upper margin: short form after et le',r'\unsure{gr.\ or.}',
   'An abbreviated form is favored, but the exact terminal group and its points remain uncertain.',[r'gr.\ or.','groupoïde','groupe'],'low','upper_note')
un('Lower margin: initial word',r'\unsure{Canulé|Cautèle}',
   'The two compressed middle groups do not distinguish the proposed words.', ['Canulé','Cautèle'],'low','caution')
un('Fibre line: cancelled est',r'\deleted{\unsure{est}}',
   'The t-like upper strokes survive the strike, but the earlier e/s bodies are partly hidden. A doubt is added to the agreed reading without a changes row.', ['est'],'medium','fibre')

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,
        sheet_kind='text',hand=hand,transcribed='yes'))
inv('author-page','margin note','top centre','1')
inv('title','text','top left','Groupoïdes de Teichmüller.')
inv('section-heading','text','below title','circled 1; Cas topologique.')
inv('simple-introduction','text','upper third','La variante la plus simple est')
inv('simple-display','display','upper centre',r'\mathcal T^+_{top} ou \mathcal T_{top}')
inv('simple-descriptor','text','beneath first display','groupoïde de Teichmüller orienté topologique')
inv('objects-definition','text','below first descriptor','objets: surfaces à bord compactes orientées (Sigma)')
inv('arrows-definition','text','beneath objects definition',"flèches: classes d’isotopie d’iso")
inv('upper-note','margin note','upper-right corner, twelve oblique baselines','Finalement, tant qu’on ne travaille pas...')
inv('upper-note-deletion','deletion','after utilisé in upper note',r"\deleted{\unsure{tout|d'où}}")
inv('immediate-introduction','text','middle upper area','Variante immédiate')
inv('bioriented-display','display','below Variante immédiate',r'\mathcal T^\pm_{top}')
inv('bioriented-descriptor','text','below bioriented display','groupoïde de Teichmüller biorienté topologique')
inv('bioriented-arrows','text','two lines below descriptor','mêmes objets, flèches sont les classes...')
inv('one-object-definition','text','middle lower area','Soit [±1] le groupoïde ayant un seul objet...')
inv('signature-introduction','text','above signature diagram','un morphisme de signature')
inv('signature-diagram','diagram','lower centre',r'\mathcal T^\pm_{top} to [\pm1], label \chi')
inv('fibre-line','text','under signature diagram','dont la fibre ... (ou noyau) est...')
inv('fibre-deletion','deletion','between fibre and parenthesis',r'\deleted{\unsure{est}}')
inv('lower-note','margin note','lower-left oblique margin','Canulé|Cautèle, si on ne se borne à des surfaces connexes!')
inv('lower-note-hook','drawing','beside surfaces/connexes, separate from exclamation','long descending stroke with leftward hooked end')
inv('complex-introduction','text','near foot','La variante la plus complexe est')
inv('complex-display','display','under complex introduction',r'S_*\mathcal TD^+_{top} ou S_*\mathcal TD_{top}')
inv('complex-descriptor','text','bottom body line','groupoïde de Teichmüller ... spécial dévissé topologique')
inv('oriente-insertion','insertion','above gap between Teichmüller and spécial','underlined orienté')
inv('folio','margin note','bottom left','43','another unnamed hand')

sign_check=json.loads((OUT/'sign_check.json').read_text())
notes=[
 dict(id='N44-001',statement_id='P44-oriented',kind='claim',place='first definitions',
      text='The sheet defines an oriented topological Teichmüller groupoid using compact oriented surfaces with boundary and isotopy classes of orientation-preserving isomorphisms. Its immediate variant permits homeomorphisms without necessarily preserving orientation. This report records those definitions, not a separate verification of the full theory.',status='transcribed; theory not independently verified'),
 dict(id='N44-002',statement_id='P44-signature-disconnected',kind='mathematical qualification',place='signature/fibre statement and connectedness margin',
      text='If disconnected surfaces and all homeomorphisms are admitted literally, two oriented disks provide four componentwise sign states. Independent reflections form a four-element subgroup whose orientation-preserving sign state is only (++). Enumerating its maps to {±1} gives four homomorphisms with kernel sizes 4,2,2,2; none has that singleton kernel. This conditional obstruction supports the margin’s connectedness caveat. It does not decide the doubtful first word or alter the source formula.',status='finite sign computation checked'),
 dict(id='N44-003',statement_id='P44-marginal-order',kind='placement',place='upper-right note',
      text='The upper note is transcribed beside the first definition, its physical position. The loop/apostrophe-like marks immediately left of its final orienté belong to the crossing body phrase l’orientation; they are not added as l’orienté or as the end of an expanded groupoïde.',status='observed from the existing rotated and body crops'),
 dict(id='N44-004',statement_id='P44-D-ductus',kind='notation qualification',place='last display',
      text='Both operators are retained as capital D. The right occurrence has a more distinctly doubled right curve than the left. This is recorded for the planned notation comparison with later assigned pages; it is not used here to invent a separate algebraic alphabet.',status='provisional ductus observation; parent to compare later'),
 dict(id='N44-005',statement_id='P44-numbering',kind='date and pagination',place='head and foot',
      text='The top 1 is author pagination; the bottom 43 is retained as an unassigned-hand foliation. No manuscript date is visible. H’s comments about page sequences and later usage are editorial material, not text on this sheet and not independently verified here.',status='observed; editorial material excluded'),
 dict(id='N44-006',statement_id='P44-short-forms',kind='abbreviation',place='definitions and upper note',
      text='Iso, autom, the néc abbreviation with raised t, and the doubtful upper-note short form remain unexpanded. No grammatical repair is made to the final de s’appeler construction.',status='preserved'),
 dict(id='N44-007',statement_id='P44-hook',kind='graphic observation',place='lower margin',
      text='The strong long hooked stroke is reproduced alongside the four-line note. It remains distinct from the neighboring exclamation mark; its exact semantic function is not assigned.',status='preserved in TikZ')
]
checks=[dict(statement_id='P44-signature-disconnected',date='2026-11-21',
    who='reader A; GPT-6 Astra Pro; run SP82_C13_148; effort not exposed',
    type='computation or formal certificate',
    outcome='Enumerated all 16 functions from the four componentwise sign pairs to ±1 and checked multiplicativity on all ordered pairs. Exactly four homomorphisms occur, with kernel sizes 4,2,2,2. None has kernel size 1. Under the stated two-disk interpretation, this obstructs a single signature character with precisely the orientation-preserving subgroup as kernel. Full enumeration is saved in sign_check.json.')]

hand_log=[
 dict(pages=['148_scan044'],habit='The calligraphic T sometimes has an additional inner upright and sometimes lacks it.',
      evidence='The first T with a raised plus has an inner stroke; the neighboring T without the plus lacks it, while both share the curved cap and sweeping base.',
      holds_at_every_observed_occurrence=False,
      witness_effect='The variation is treated as ductus; no new alphabet or separate I is introduced.'),
 dict(pages=['148_scan044'],habit='Long descenders in the oblique note cross neighboring text lines.',
      evidence='The g of gros descends into the next line, and the q above the word sera passes close to its compressed strokes.',
      holds_at_every_observed_occurrence=False,
      witness_effect='A crossing descender is not used as an f stroke to select offre at M0680.'),
 dict(pages=['148_scan044'],habit='The necessity abbreviation carries a raised t and a lower terminal point.',
      evidence='In the homeomorphism definition the néc baseline is followed by a small elevated t and a distinct lower dot.',
      holds_at_every_observed_occurrence=True,
      witness_effect='C’s baseline néct and H’s néc omit the vertical placement or the letter; both are corrected to néc with raised t.'),
 dict(pages=['148_scan044'],habit='Capital D can have a retraced outer curve.',
      evidence='The second D in the last display has two close right-hand curves; the first is less distinctly doubled.',
      holds_at_every_observed_occurrence=False,
      witness_effect='Both witnesses’ ordinary D is retained provisionally, with the physical variation flagged for later comparison.')
]
notation=[
 dict(place='oriented definition',form=r'\mathcal T^+_{\mathrm{top}}\ \text{ou}\ \mathcal T_{\mathrm{top}}',observation='The two written names are explicitly presented as alternatives for the oriented topological groupoid.'),
 dict(place='bioriented definition',form=r'\mathcal T^\pm_{\mathrm{top}}',observation='The raised sign has a plus and a separate lower horizontal bar.'),
 dict(place='objects line',form=r'\Sigma',observation='The surface symbol is a capital Sigma inside parentheses.'),
 dict(place='one-object paragraph',form=r'[\pm1],\ e=\varnothing',observation='The example after e= is a small oval crossed by a long oblique stroke; the groupoid sign and numerals remain as written.'),
 dict(place='signature arrow',form=r'\chi',observation='The crossed curved strokes label the arrow above its single shaft; the arrowhead is at the right end.'),
 dict(place='complex display',form=r'S_*\mathcal TD^+_{\mathrm{top}},\ S_*\mathcal TD_{\mathrm{top}}',observation='The stars are low after S; the first expression alone has a raised plus. The D curve retracing is noted without changing the alphabet.'),
 dict(place='upper margin',form=r'\mathcal T^\pm,\ \mathcal T,\ \mathcal T^+',observation='The note discusses giving the simplest notation to the larger variant and the plus notation to the oriented one; no later-page usage is assumed here.')
]
abbreviations=[
 dict(place='flèches definition',form='iso',observation='Short form with no visible terminal point; not expanded in the text.',possible_expansion='isomorphisme(s)'),
 dict(place='one-object paragraph',form='autom',observation='Stops after m before ±1; no morphismes continuation.',possible_expansion='automorphismes'),
 dict(place='bioriented definition',form=r'néc\textsuperscript{t}.',observation='Raised t and lower full stop are distinct.',possible_expansion='nécessairement'),
 dict(place='upper margin',form=r'\unsure{gr.\ or.}',observation='Doubtful short form; the exact terminal letters and points remain open. No expansion is printed.',possible_expansion='unresolved')
]

second_boxes=[]
def sb(name,kind,box,reading):
    second_boxes.append(dict(box='S44-'+name,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
sb('author1','handwritten number',[833,26,882,79],r'\mspage{1}')
sb('title','underline scope',crop['title']['box'],r'\uline{Groupoïdes de Teichmüller}.')
sb('circled1','handwritten number',[203,262,276,321],r'\textcircled{1}')
sb('first-formula','formula and alphabet comparison',crop['oriented_formula']['box'],r'\[\mathcal T^+_{\mathrm{top}}\quad\text{ou}\quad\mathcal T_{\mathrm{top}}\]')
sb('first-descriptor','C/H punctuation difference',[233,542,1320,643],r'(\uline{groupoïde de Teichmüller} \uuline{orienté} \uline{topologique})')
sb('objects','C/H different word and whole doubtful formula',[329,638,1475,735],r'\uline{objets} : surfaces \uline{à bord} compactes orientées $(\Sigma)$\unsure{,|.}')
sb('fleches','C/H punctuation difference',[329,701,1637,817],r"\uline{flèches} : classes d'isotopie d'iso (conservant l'orientation)")
sb('upper-note','margin note and whole doubtful formulas',crop['upper_note']['box'],upper_note)
sb('upper-deletion','struck passage',[1516,290,1665,402],r"\deleted{\unsure{tout|d'où}}")
sb('nect','C/H different short form',[785,1198,1664,1315],r"(ne conservant pas néc\textsuperscript{t}. l'orientation).")
sb('one-object','handwritten numbers and C/H different word',crop['one_object']['box'],r"Soit $[\pm1]$ le groupoïde ayant un seul objet $e$ (par exemple $e=\varnothing$) et comme groupe d'autom $\pm1$. On a")
sb('signature','handwritten number and diagram',crop['signature']['box'],signature)
sb('fibre','C/H different phrase and cancellation',crop['fibre']['box'],r'dont la \uline{fibre} \deleted{\unsure{est}} (ou noyau) est $\mathcal T_{\mathrm{top}}^+=\mathcal T_{\mathrm{top}}$.')
sb('deleted-est','struck passage',[658,1740,774,1812],r'\deleted{\unsure{est}}')
sb('lower-note','margin note and doubtful word and drawing',crop['caution']['box'],caution)
sb('complex-formula','whole formula and notation comparison',[579,1975,1465,2118],complex_formula)
sb('final-descriptor','C/H different word and insertion',[229,2082,1661,2244],final_descriptor)
sb('oriente','insertion',[965,2082,1122,2177],r'\inserted{\uline{orienté}}')
sb('devisse','C/H different word',[1192,2114,1367,2208],r'\uline{dévissé}')
sb('folio43','handwritten number and margin note',[33,2252,105,2326],r'\margin{43}')

reading_rows={
 969:('first descriptor','No terminal colon follows the source closing parenthesis.'),
 970:('surface label','Read capital Sigma from the visible arms and central fold; H’s illegibility is not retained.'),
 971:('surface-line punctuation','Keep comma/full-stop doubt because of the crossing note.'),
 972:('upper margin and flèches line','Read the entire upper-right note at its physical position; its opening clause and several small words differ from H. The flèches line has no separate terminal full stop.'),
 975:('necessity abbreviation','Preserve néc with raised t and the lower full stop.'),
 976:('autom abbreviation','Keep the short written autom, without H’s expansion.'),
 982:('fibre parenthesis','The source reads ou noyau. The cancelled est remains in doubt because its body is crossed.'),
 985:('lower-margin first word','The Canulé/Cautèle alternatives remain unresolved.'),
 986:('lower-margin clause','Resolve si on ne se borne from the written groups and b/-rne stems.'),
 993:('final adjective','Read dévissé from the accent and successive s turns, not divisé.'),
 994:('folio and upper margin','Keep 43 as a margin foliation; the upper note is transcribed near its physical position, without H’s later-page editorial statements. No final full stop follows the quoted descriptor.')
}
macro_notes={
 965:'Source scan marker versus editorial page-reference notation; the actual author 1 is retained.',
 966:'H’s long pagination/sequence note is editorial metadata, not source prose on this sheet.',
 967:'Parenthesized number versus circled-number macro representation.',
 968:'H’s note explicitly describes the circle; the source circled 1 is retained.',
 973:'Order of superscript and subscript commands only.',974:'Order of superscript and subscript commands only.',
 977:'TikZ-cd versus display-math wrapper for the same signature arrow.',
 978:'Ampersand-replacement syntax only.',979:'Arrow-macro syntax; the source direction is unchanged.',
 980:'Arrow-label syntax for the same chi above the shaft.',981:'Diagram/display closing wrapper only.',
 983:'Order of superscript and subscript commands only.',984:'Order of superscript and subscript commands only.',
 987:'H’s prose about the oblique note and chi label is editorial commentary; the actual note and diagram are independently read.',
 988:'Grouping/spacing and exponent placement syntax for the same T-D expression.',
 989:'Equivalent superscript/subscript command order.',990:'Spacing between calligraphic T and D only.',
 991:'Quotation glyph encoding; source double quotation strokes use the required backtick/apostrophe convention.',
 992:'H’s explanatory words about the interlinear insertion are editorial; the inserted orienté and its underline are represented directly.'
}
diffs=list(csv.DictReader((PACKET/'differences.tsv').open(),delimiter='\t'))
differences_review=[]
for row in diffs:
    n=int(row['source_row'])
    if n in reading_rows:
        place,note=reading_rows[n]
        differences_review.append(dict(source_row=n,decision='reading decision',place=place,note=note))
    else:
        assert n in macro_notes,n
        differences_review.append(dict(source_row=n,decision='macro-only',place=row['words before'] or 'editorial page marker',note=macro_notes[n]))

result=dict(scan=44,reader='A',reader_metadata=dict(model='GPT-6 Astra Pro',effort='not exposed',run='SP82_C13_148',date='2026-11-21'),
 lines_read=38,
 reading_workflow=dict(whole_page_views=1,native_half_views=2,crop_views=13,recrops=0,
    half_view_proxies=['half1_q95.jpg','half2_q95.jpg'],
    detail='The whole page was inspected once for layout and both prepared native-dimension overlapping halves were read once line by line, including all agreed words and signs. The 38 baselines comprise 22 body/display/number/insertion baselines, twelve oblique upper-note lines and four lower-note lines. The signature diagram, its two endpoints, shaft, head and chi label were inspected separately. Every saved first crop was viewed once; the rotated crops are reused without recropping. No OCR, external research or TeX compilation was used.',
    crop_method='All change rows cite the original saved rectangles, including the unrotated native coordinates for the two rotated crops. Same-dimension quality95 JPEG proxies were used for display only. Second boxes may be smaller native subrectangles.',
    mathematical_scope='One explicit finite sign-group computation was performed for the connectedness caveat; it does not choose a reading or prove the full groupoid theory.'),
 changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,notes=notes,checks=checks,
 hand_log=hand_log,notation=notation,abbreviations=abbreviations,second_boxes=second_boxes,
 differences_review=differences_review,crop_manifest=manifest,
 check_artifacts=[dict(path='readers/148_scan044/sign_check.json',statement_id='P44-signature-disconnected',kernel_sizes=sign_check['kernel_sizes'])])

marks=list(csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t'))
assert sorted(r['id'] for r in decisions)==sorted(r['id'] for r in marks)
assert len(differences_review)==len(diffs)==len({r['source_row'] for r in differences_review})
assert isinstance(result['lines_read'],int)
assert all(r['seen'] for r in manifest)
assert len(second_boxes)==len({r['box'] for r in second_boxes})
for r in changes:
    assert r['against_c'] or r['against_h']
    assert any(r['crop']==c['crop'] and r['box']==c['box'] for c in manifest)
for r in second_boxes:
    assert 0<=r['x0']<r['x1']<=1681
    assert 0<=r['y0']<r['y1']<=2357
    assert r['reading']
(OUT/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),decisions=len(decisions),inventory=len(inventory),unresolved=len(unresolved),checks=len(checks),second_boxes=len(second_boxes),differences_review=len(differences_review),crops=len(manifest))))
