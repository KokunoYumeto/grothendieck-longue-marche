"""Write the completed Reader C audit of scan024. Static validation only."""
from pathlib import Path
import copy
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/8f839dff4bf0')
WORK=ROOT/'SP74_C13_143+145_work'
KEY='143_scan024'
packet=json.loads((ROOT/'reader_packets'/f'{KEY}.json').read_text())
page_path=WORK/'pages'/f'{KEY}.tex'
prior_path=WORK/'reviews'/f'{KEY}_accepted.json'
accepted=page_path.read_text()
prior_bytes=prior_path.read_bytes()
prior=json.loads(prior_bytes)

opening_before=r"Inversement, donnons-nous \inserted{un groupe $T$ abélien} un $T$-groupoïde \deleted{\unsure{connexe}} $\Lambda$,"
opening_after=r"""\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=base west,inner sep=0pt,text width=7.9cm] at (0,1.10) {Inversement,\hfill donnons-nous};
\node[anchor=base west,inner sep=0pt] at (-0.85,0) {un $T$-groupoïde \deleted{\unsure{connexe}} $\Lambda$,};
\node[anchor=base west,inner sep=0pt] (abelianaddition) at (5.20,0) {\inserted{un groupe $T$ abélien}};
\draw[thin] (5.04,-0.12) .. controls (5.00,0.18) and (5.12,0.43) .. (5.42,0.45)
 .. controls (6.60,0.46) and (7.60,0.65) .. (8.20,1.10)
 .. controls (8.22,0.83) and ([xshift=-0.65cm,yshift=0.78cm]abelianaddition.base east) .. ([xshift=-0.32cm,yshift=0.62cm]abelianaddition.base east)
 .. controls ([xshift=0.06cm,yshift=0.47cm]abelianaddition.base east) and ([xshift=0.16cm,yshift=0.24cm]abelianaddition.base east) .. ([xshift=0.12cm,yshift=-0.02cm]abelianaddition.base east);
\end{tikzpicture}}"""

bracket_before=r"\underbrace{\operatorname{Isom}_\Lambda(t,t')}_{\pi_{t,t'}}"
bracket_after=r"""\begin{tikzpicture}[baseline=(isomop.base),x=1cm,y=1cm]
\node[anchor=base west,inner sep=0pt] (isomop) at (0,0) {$\operatorname{Isom}_\Lambda$};
\node[anchor=base west,inner sep=0pt] (isomargs) at (isomop.base east) {$(t,t')$};
\draw[thin] ([xshift=-0.30cm,yshift=-0.35cm]isomop.base east)
 .. controls ([xshift=-0.23cm,yshift=-0.40cm]isomop.base east) and ([xshift=-0.12cm,yshift=-0.40cm]isomop.base east) .. ([yshift=-0.44cm]isomop.base east)
 .. controls ([xshift=0.08cm,yshift=-0.47cm]isomop.base east) and ([xshift=0.20cm,yshift=-0.47cm]isomop.base east) .. ([xshift=0.26cm,yshift=-0.45cm]isomop.base east)
 .. controls ([xshift=-0.45cm,yshift=-0.41cm]isomargs.base east) and ([xshift=-0.32cm,yshift=-0.41cm]isomargs.base east) .. ([xshift=-0.24cm,yshift=-0.38cm]isomargs.base east);
\node[anchor=base west,inner sep=0pt] at ([xshift=0.14cm,yshift=-0.75cm]isomop.base east) {$\pi_{t,t'}$};
\end{tikzpicture}"""

a_before=r'\Pi\text{ égaux à }\widetilde\Pi'
a_after=r'\Pi\text{ égaux \unsure{à|:} }\widetilde\Pi'
candidate=accepted
for before,after in [(opening_before,opening_after),(bracket_before,bracket_after),(a_before,a_after)]:
    assert candidate.count(before)==1,before
    candidate=candidate.replace(before,after)

crop_names=[
    '143_scan024_readerB_opening_attachment.png',
    '143_scan024_readerB_injection.png',
    '143_scan024_readerB_codomain_and_action.png',
    '143_scan024_readerB_cancelled_adjective.png',
    '143_scan024_readerB_object_set.png',
    '143_scan024_readerB_mais_and_bracket.png',
    '143_scan024_readerB_family_and_bitorsors.png',
    '143_scan024_main_composition.png',
    '143_scan024_main_subgroups.png',
]
viewed={'crops/'+name for name in crop_names}
boxes={row['crop']:row['box'] for row in prior['changes']}
boxes['crops/143_scan024_readerB_injection.png']=[571,1274,1254,1460]
opening_crop='crops/143_scan024_readerB_opening_attachment.png'
injection_crop='crops/143_scan024_readerB_injection.png'
codomain_crop='crops/143_scan024_readerB_codomain_and_action.png'

findings=[
    {
        'id':KEY+'-auditC-F1',
        'place':'Opening insertion un groupe T abélien, broad physical attachment call',
        'before':opening_before,'after':opening_after,
        'reason':'A continuous broad asymmetric arch encloses the insertion from above, with downward ends on both sides and a pointed summit rising to the gap after donnons-nous on the preceding line. The left shoulder is long and shallow; the right shoulder is shorter and more curved. The inserted words are already present, but their physical call is omitted by the plain inserted wrapper. The candidate draws it and retains the insertion to the right of the second-line Lambda while its summit reaches the opening-line gap.',
        'confidence':'high','crop':opening_crop,'box':boxes[opening_crop],
        'against_C':True,'against_H':True,
        'C':r'\inserted{un groupe $T$ abélien}',
        'H':'(un\ngroupoïde $T$-\\uncertain{fidèle})',
        'kind':'drawing or diagram','consequential':False,'marked_in_H':True,
        'decision_updates':[],'certainty_only':False,
        'inventory_parent':'E03','inventory_addition':'E03a',
        'relation_to_existing_change_row':{'row':2,'explanation':'Existing wording and attachment interpretation remain; this separately restores the physical guide omitted by both witness encodings.'},
    },
    {
        'id':KEY+'-auditC-F2',
        'place':'Isom diagram, shape and extent of the bracket above pi-sub-t,t-prime',
        'before':bracket_before,'after':bracket_after,
        'reason':'The drawn stroke begins beneath the final m/end of Isom and stops beneath the second t, before its prime and the closing parenthesis. It is a shallow irregular curve with a broad low central region, without a sharp central cusp. The pi label starts below that low region and continues to the right. A full-expression conventional underbrace gives the stroke a longer extent and a cusp not established by the ink. The candidate retains all symbols and the connector alternatives, replacing only the bracket geometry and label placement.',
        'confidence':'high','crop':injection_crop,'box':boxes[injection_crop],
        'against_C':True,'against_H':True,
        'C':bracket_before,
        'H':r"\underbrace{\mathrm{Isom}_{\Lambda}(t, t')}_{\pi_{t,t'}}",
        'kind':'drawing or diagram','consequential':False,'marked_in_H':False,
        'decision_updates':[],'certainty_only':False,
        'inventory_element':'E10',
    },
    {
        'id':KEY+'-auditC-F3',
        'place':'First diagram codomain, reduced mark after égaux',
        'before':a_before,'after':a_after,
        'reason':'The local mark consists of two compact bent or angled strokes, without a securely complete a loop. Its form admits a reduced accented a or colon. The adjacent initial é in égaux also has a compact body and detached accent, supporting the possibility of such compression. Keep à first cautiously and retain the colon alternative. The word égaux and its long leftward g return remain clear; that return is part of the letter, not a guide.',
        'confidence':'low','crop':codomain_crop,'box':boxes[codomain_crop],
        'against_C':False,'against_H':False,
        'C':r'\Pi\text{ égaux à }\widetilde\Pi',
        'H':r'$\Pi$ égaux à $\widetilde{\Pi}$',
        'kind':'misread symbol or index','consequential':False,'marked_in_H':False,
        'decision_updates':[],'certainty_only':True,
        'preferred_reading_unchanged':True,
        'separate_word_confidence':{'word':'égaux','confidence':'high'},
    },
]

observations=[
    'The top-line low strokes finish donnons-nous; no independently localizable two-word passage follows them. The adjacent large stroke is the insertion call. M0704 remains omitted at medium confidence.',
    'Un groupe T abélien is added to the opening datum, beside the second-line Lambda, and attached upward by the broad call. The words and insertion interpretation remain; the missing physical call is drawn separately.',
    'Only an initial rounded trace, low humps and terminal raised remnants survive the heavy cancellation. Connexe remains doubtful inside deletion.',
    'The opening action letter has an angular upper return and lower foot; E/Sigma remains unresolved, low confidence and non-consequential.',
    'The first hom has no detached point before de; read in native half1.',
    'Before un seul objet are two compact dark strokes, with no secure full a loop. Existing à-first/colon alternative remains low confidence.',
    'The codomain has four lines in the accepted order. The second reduced à now admits colon explicitly, but the line-order finding remains high confidence.',
    'Rev. has its short r/e/v trace and final point, without ê or t.',
    'Autom has no detached point after its final m before sont. Its small internal mark is not moved to the abbreviation boundary.',
    'The covered capital Pi ends its line without an ellipsis. Its preceding reduced à is separately uncertain, not the absence of terminal points.',
    'After avec, the word is action with its crossed t and dotted i; there is no preceding les or p-descender for opérations.',
    'The compatibility-line group glyph has a rounded upper bowl and lower curl. Keep E/Sigma uncertainty.',
    'Soit is followed by the flag-top object glyph, equality, Ob and Lambda. Ob has no comma before Lambda.',
    'Immediately after the opening bracket is donc, with a tall looped d and low onc exit, not lequel.',
    'The second object glyph has the same compact flag and single lower return before est un.',
    'The bracket-line action letter is angular with returning upper and lower strokes; E/Sigma remains open.',
    'The group letter ends one line and ens begins the next. Neither a detached hyphen nor an ens abbreviation period is visible.',
    'The descending comma is inside, to the left of the closing bracket. No extra comma follows the bracket.',
    'An explicit upright U/V-like universal sign with a crossing stands between pour and t,t-prime. It is not a spacing-macro comma.',
    'The t, comma, t-prime, membership sign and third flag-top object glyph are followed by a source comma; no index is regularized.',
    'The second hom has no boundary period; the following dots belong to injectif. Checked in native half1.',
    'Injectif is legible and has one independent underline, crossing the descender area; checked in native half1.',
    'Avec passes directly to composition; no extra la is written.',
    'The prose isom begins with a small i-like tick and ends with a point, unlike the tall ruled I in the display.',
    'The last paragraph starts with looped On, a tiny separate a, then exprimé with its x, p descender and final accent. Checked in native half2.',
    'One uninterrupted strike starts before Mais and continues through its possible on continuation. No independent dash precedes it. The last word remains doubtful.',
    'The short word after faut is se, with a small rising s and low e exit; donner begins the next line.',
    'Sous before groupes has its low ou and separated final s return. No compound hyphen is visible.',
    'The family formula retains pi-sub-t, its parentheses and t-in-object-set index. The fourth object glyph is flag-topped, not a plain T or a newly supplied Z.',
    'The short d’ens sequence ends before the next word; ensembles would expand the source abbreviation.',
    'Vides has dotted i, tall looped d and es; ou is reduced to two small low traces. M0705’s first reading remains medium confidence without adding words.',
    'The next line reads bitorseurs sous, with tall b, dotted i, crossed t, low ending and final s.',
    'The word before the two pi groups has a tall open l followed by es; retain les rather than ces.',
    'Pale pencil 23 was read at the lower left in the original and half2; no author is assigned to its hand.',
]
assert len(observations)==len(prior['changes'])==34
collation_confirmation=[]
literal_updates=[]
for number,(row,observation) in enumerate(zip(prior['changes'],observations),1):
    reading=row['final'].replace(a_before,a_after)
    status='confirmed without revision'
    if reading!=row['final']:
        status='preferred reading confirmed; literal final synchronized with certainty-only mark'
        replacement=copy.deepcopy(row)
        replacement['final']=reading
        replacement['ink'] += ' The reduced mark after égaux is separately retained as à/colon uncertainty at low confidence; this does not reduce confidence in the placement/no-ellipsis finding.'
        replacement['local_mark_confidence']={'after égaux':'low','égaux':'high'}
        literal_updates.append({'accepted_change_row':number,'replacement':replacement,'material_change':False})
    evidence=row['crop'] if row['crop'] in viewed else ('half1' if number in (5,21,22) else 'half2')
    collation_confirmation.append({'accepted_change_row':number,'place':row['place'],'C':row['C'],'H':row['H'],'reading':reading,'status':status,'confidence':row['confidence'],'observation':observation,'audit_evidence':evidence,'crop_reused_in_this_audit':row['crop'] in viewed,'prior_crop':row['crop'],'new_material_change':False})

inventory_obs=[
    'Pencil 12 at upper right read in original/half1, unnamed hand.',
    'All opening words, three plain T forms, Lambda, operation, pair and hom/groupoïdes retained; no M0704 two-word passage found.',
    'Inserted abelian-group datum retained; its broad physical call is added as child drawing E03a.',
    'Heavy cancelled adjective remains doubtful connexe; no newly recoverable letters supplied.',
    'Lambda, headed right arrow, foncteur and twice-underlined fidèle checked; all four codomain lines retained. Both reduced à/colon forms now explicit.',
    'Compatible avec action de the group glyph and period retained.',
    'Soit, object glyph, equality, Ob and Lambda retained without a spurious comma.',
    'Opening bracket, donc, object set, est un, group letter, line-broken ens, inside comma and closing bracket checked.',
    'Et pour, explicit universal sign, t/t-prime, membership, object set, on a un hom and singly-underlined injectif checked.',
    'Isom subscript Lambda, arguments, pi label and connector retained. Replace full conventional underbrace with the short shallow irregular bracket from under m to under second t; no sharp cusp.',
    'Compatible avec composition des lower-case isom. read; no extra article.',
    'On a exprimé, donnée, faithful functor, groupoïde Lambda, dans and single-angle-bracket pi retained.',
    'One long cancellation passes through Mais and uncertain on; no independent dash.',
    'Full bracketed family/subgroup/empty-set/bitorsor passage read, including all t indices, first group’s prime and comma separating the two groups.',
    'The page ends On va maintenant introduire les op. de; no continuation consulted or supplied.',
    'Pencil 23 at lower left, unnamed hand.',
]
assert len(inventory_obs)==len(prior['inventory'])==16
inventory_confirmation=[{'element':row['element'],'position':row['position'],'status':'checked','observation':obs} for row,obs in zip(prior['inventory'],inventory_obs)]
guide_inventory={'sheet_kind':'text','hand':'his hand','element':'E03a','parent':'E03','kind':'drawing','position':'Broad peaked call above and around un groupe T abélien; summit reaches the preceding opening line','first_words_or_objects':'Asymmetric shallow left shoulder, pointed summit, shorter right shoulder and downward ends enclosing the added phrase','transcribed':'yes','crop':opening_crop,'box':boxes[opening_crop]}
e10=copy.deepcopy(prior['inventory'][9])
e10['first_words_or_objects']='Isom_Lambda(t,t-prime), short shallow irregular bracket from beneath final m to beneath second t, pi_(t,t-prime) label beginning below its low region, hooked connector to pi; right head uncertain'

doubts=copy.deepcopy(prior['remaining_doubts'])
doubts.append({'place':findings[2]['place'],'reading':r'\unsure{à|:}','alternatives':'Reduced accented a; colon','confidence':'low','reason':findings[2]['reason'],'crop':codomain_crop,'box':boxes[codomain_crop],'certainty_only':True})

raw_map=[[],[],[1,2],[3],[2],[4],[5],[],[],[],[6],[7,9],[8],[7,10],[11],[12],[13],[],[14,15],[16],[17,18],[19],[20],[21,22],[],[],[],[],[23,24],[25],[26],[26],[27],[28],[29],[30,31,32,33],[34]]
assert len(raw_map)==len(packet['differences'])==37
special={
    1:'Scanpage locator is editorial. The actual pencil 12 is separately present at the upper right.',
    2:'H’s attribution de l’auteur is editorial; the manuscript numeral 12 is retained with unnamed hand.',
    3:'M0704 has no separate locatable words; insertion text retained and the omitted physical call restored as finding F1.',
    5:'H’s parenthetic T-fidèle paraphrase does not replace the actual inserted un groupe T abélien or its physical call.',
    8:'Tikzcd environment name is markup only.',9:'Ampersand-replacement options are markup only.',10:'Arrow-option syntax is not manuscript wording; the actual headed arrow was checked.',
    11:'The packet row is malformed by embedded tab/page fields. Its recoverable content concerns the diagram and H’s double-underline note. Foncteur fidèle and its two rules were visually checked; the first codomain à/colon uncertainty remains.',
    14:'Codomain line order and absent ellipsis retained. The second reduced à gets a certainty-only colon alternative.',
    18:'H’s comma comes from the spacing command after Ob; there is no literal source comma before Lambda.',
    22:'The raw comma is a spacing-command artifact. The actual universal sign omitted from H is retained.',
    25:'Diagram wrapper only; the actual second diagram was read in full.',26:'Diagram options only; no source words are added.',
    27:'Hook-arrow macro alignment differs. Hook and uncertain head remain; the separate shallow bracket is corrected graphically in F2.',
    28:'Target pi and diagram-wrapper alignment; pi remains lower-case.',
    31:'The apparent dash is the uninterrupted cancellation extending before Mais; no independent dash is restored.',
    36:'Every abbreviation/word and the pi pair was checked locally; M0705 remains first reading at medium confidence.',
}
raw_checks=[{'packet_difference_number':n,'raw':copy.deepcopy(row),'accepted_change_rows':refs,'status':'checked','disposition':special.get(n,'Literal difference checked against the source; accepted preferred reading retained as detailed in referenced row(s).')} for n,(row,refs) in enumerate(zip(packet['differences'],raw_map),1)]

old_n2=next(n for n in prior['notes'] if n['id']==KEY+'-N2')
new_n2=copy.deepcopy(old_n2)
new_n2['text']="The author defines the object set, whose tau/T glyph remains unresolved, as Ob Lambda and describes it as an E/Sigma set. For the explicitly quantified pair t,t', the page writes an injective homomorphism from Isom_Lambda(t,t') to pi. A short shallow irregular bracket begins under the final m of Isom and stops under the second t, before the prime and closing parenthesis; the pi_(t,t') label begins below its low central region. The source then states compatibility with composition. Fidèle is double-underlined, injectif singly underlined. The connector has a definite left hook but an uncertain small right head."
notes=[
    {'id':KEY+'-auditC-N1','text':'The inverse-construction datum and faithful-functor diagram were read line by line. The opening abelian T is plain capped T, distinct from the later flag-shaped set letter. The broad peaked insertion call is now drawn, with a child inventory record under E03. M0704 remains omitted because no separate two-word ink is localizable.'},
    {'id':KEY+'-auditC-N2','text':'Both local codomain à/colon forms were inspected in this page’s existing crop. The first remains low-confidence à-first uncertainty; the second gains the same explicit alternatives without changing preferred wording. Égaux is clear and its long returning g descender is not an independent guide.'},
    {'id':KEY+'-auditC-N3','text':'The Isom display’s symbols, low Lambda, t/t-prime arguments, indexed pi label and connector alternatives remain. Its conventional full-expression underbrace is replaced by the observed short shallow irregular bracket, with no sharp central cusp and no extension to the first I or closing parenthesis. The existing N2 and E10 descriptions are revised to match this physical evidence.'},
    {'id':KEY+'-auditC-N4','text':'The object-set bracket keeps its comma inside the closing bracket and the missing compound hyphen across the group-letter/ens line break. The explicit universal sign, singular underlining of injectif, lower-case prose isom., cancelled Mais and possible on, M0705 wording, all subgroup indices and the pi_(t-prime),pi_t order remain.'},
    {'id':KEY+'-auditC-N5','text':'This second reading performs visual transcription checks, not a new mathematical proof. The accepted report’s targeted bitorsor proof, statement 143_scan024-N6, remains attributed to the main reader who performed it. It is neither repeated nor claimed as Reader C’s work.'},
    {'id':KEY+'-auditC-N6','text':'The two pencil numerals, 12 above and 23 below, remain assigned to unnamed hand(s). The final phrase ends les op. de; no continuation was inspected. Six prior doubts are retained and the reduced mark after égaux adds a seventh. No OCR, external research, new crop, recrop or TeX compilation was used.'},
]

hand_log=[
    {'habit':'An insertion call can be a broad asymmetric peaked arch rather than a small caret.','places':'Opening un groupe T abélien.','scope':'Original, upper half and one existing opening crop inspected.','misreadings':'Both witness encodings omit its actual guide shape; added as E03a under insertion E03.'},
    {'habit':'A label bracket can cover only part of the printed expression and have no sharp cusp.','places':'Below Isom_Lambda(t,t-prime).','scope':'Original, lower half and existing injection crop inspected.','misreadings':'Both witnesses use a full-expression underbrace; the actual curve begins under m and ends under second t.'},
    {'habit':'Reduced accented vowel bodies can resemble two punctuation marks.','places':'Both codomain à/colon graphs; compact initial é of égaux.','scope':'All compared within this page’s codomain crop, not inferred solely from another page.','misreadings':'Keep both à-first alternatives low confidence; do not transfer high confidence from égaux to its following mark.'},
    {'habit':'Plain capped T and the flag-top object glyph have distinct structures.','places':'Three plain T occurrences in opening datum; four object-set occurrences later.','scope':'Every occurrence checked individually in the page and corresponding crops.','misreadings':'Preserve plain T; keep tau/calligraphic-T unresolved without turning it into Z.'},
    {'habit':'Angular and rounded returning forms coexist in the action-group letter.','places':'All three E/Sigma positions.','scope':'Opening, codomain/action and object-set crops inspected once.','misreadings':'Shared E/Sigma uncertainty remains low and non-consequential.'},
    {'habit':'A short word or group can be largely absorbed by a long cancellation stroke.','places':'Connexe; possible on after Mais.','scope':'Both existing cancellation crops inspected once.','misreadings':'No new letters certified and no independent dash extracted from the continuous Mais strike.'},
    {'habit':'Abbreviation points and compound hyphens are not automatic.','places':'Hom twice, autom, line-broken group-letter ens, rev., isom., d’ens, op.','scope':'Every local occurrence checked, including its punctuation.','misreadings':'Retain actual missing points/hyphen and the inside-bracket comma rather than H/C normalizations.'},
    {'habit':'Tiny indices, joined strokes and a filled connector endpoint need separate checks.','places':'Isom arguments and pi label, family index, final pi_(t-prime),pi_t pair, hooked connector.','scope':'Existing injection and family crops inspected; whole formulas read, not only disputed endpoints.','misreadings':'Keep the source indices and group order; hook-arrow/bare hooked-shaft uncertainty remains confined to the right tip.'},
    {'habit':'The capital display I is taller and ruled compared with the prose i tick.','places':'Isom in the display; isom. in the composition clause.','scope':'Both existing crops compared within this page.','misreadings':'H’s prose capitalization is not adopted.'},
]

report={
    'key':KEY,'reader':'C','stage':'second reading','first_reader':'B',
    'image_views':['original','half1','half2'],
    'image_view_details':[
        {'view':'original','path':packet['image'],'successful_views':1},
        {'view':'half1','path':packet['halves'][0],'box':packet['half_boxes'][0],'successful_views':1},
        {'view':'half2','path':packet['halves'][1],'box':packet['half_boxes'][1],'successful_views':1},
    ],
    'existing_crop_views':[{'crop':'crops/'+name,'box':boxes['crops/'+name],'successful_views':1} for name in crop_names],
    'new_crops':[],'findings':findings,'confirmed':[
        {'place':'Entire opening datum','checked':'All opening words, the insertion, cancelled adjective, three plain T forms, all Lambda forms, operation on (T,Lambda), first hom without a point, and both pencil numerals were checked. M0704 has no separate locatable text.','evidence':['original','half1',opening_crop,'crops/143_scan024_readerB_cancelled_adjective.png']},
        {'place':'First faithful-functor diagram','checked':'The source Lambda and headed arrow, foncteur fidèle label with two distinct underlines, all four target lines, capitals Pi/covered Pi versus lower pi, both reduced à marks, rev. and autom punctuation and absence of an ellipsis were checked.','evidence':['half1',codomain_crop]},
        {'place':'Object-set paragraph','checked':'Soit, equality, Ob Lambda, bracket start and donc, all set/group glyphs, missing hyphen, inside comma and bracket end, et pour, explicit universal sign, both t arguments and prime, membership comma, on a un hom and single underline of injectif checked.','evidence':['half1','half2','crops/143_scan024_readerB_object_set.png']},
        {'place':'Second diagram and composition line','checked':'Read operator Isom with low Lambda, t/comma/t-prime, pi label indices, left hook, shaft and uncertain right terminal, final pi and full bracket geometry. Composition has no inserted la and ends with lower-case isom. and its point.','evidence':['half2',injection_crop,'crops/143_scan024_main_composition.png']},
        {'place':'Last paragraph and final bracket','checked':'Read all words from On a exprimé through les op. de, single angle brackets around pi, continuous Mais cancellation, square brackets, family index, d’ens vides ou, bitorseurs sous les, the t-prime/t order, separating comma and continuation points. M0705 remains first reading. No next-page continuation was consulted.','evidence':['half2','crops/143_scan024_readerB_mais_and_bracket.png','crops/143_scan024_main_subgroups.png','crops/143_scan024_readerB_family_and_bitorsors.png']},
        {'place':'Page-wide witness agreement and physical inventory','checked':'All C/H agreements were checked against ink alongside differences. Margins, text ends, overwritten/cancelled traces, guides, underlines, primes and tildes were included. No additional independent marginal text was found; guide and bracket changes are physical corrections without new source wording.','evidence':['original','half1','half2']},
    ],
    'collation_confirmation':collation_confirmation,
    'existing_difference_updates':literal_updates,
    'remaining_doubts':doubts,
    'remaining_doubt_disposition':[{'existing_place':d['place'],'status':'retained unchanged'} for d in prior['remaining_doubts']],
    'decisions':copy.deepcopy(prior['decisions']),
    'mark_confirmations':[dict(copy.deepcopy(d),audit_status='confirmed unchanged',audit_reader='C') for d in prior['decisions']],
    'inventory_confirmation':inventory_confirmation,
    'inventory_additions':[guide_inventory],
    'inventory_updates':[{'element':'E10','before':copy.deepcopy(prior['inventory'][9]),'after':e10,'reason':'Replace full-underbrace wording with observed short shallow irregular bracket.'}],
    'existing_note_updates':[{'id':old_n2['id'],'before':old_n2['text'],'after':new_n2['text'],'reason':'Describe the physical bracket extent and label placement, without changing the source mathematical assertion.'}],
    'raw_difference_checks':raw_checks,'notes':notes,
    'check_events':[
        {'statement_id':notes[0]['id'],'type':'carried as background without fault found','outcome':'Reader C visually read the inverse-construction datum and faithful functor without proving the construction.','checked_by':'Reader C, second reading'},
        {'statement_id':notes[2]['id'],'type':'carried as background without fault found','outcome':'Reader C checked the Isom display and source injectivity/composition claims. No proof of injectivity or compatibility was performed.','checked_by':'Reader C, second reading'},
        {'statement_id':notes[3]['id'],'type':'carried as background without fault found','outcome':'Reader C visually checked the family and empty-set/bitorsor wording and group order; no new mathematical proof was performed.','checked_by':'Reader C, second reading'},
    ],
    'prior_check_event_attribution':[{'statement_id':event['statement_id'],'type':event['type'],'who':event.get('who','prior accepted reading'),'audit_status':'existing event retained under original attribution; not performed by Reader C'} for event in prior['check_events']],
    'hand_log':hand_log,
    'main_consultation':'Main independently re-inspected opening_attachment and injection and agreed to the peaked arch and short shallow bracket, requesting E03 child drawing and N2/E10 revisions. Main then inspected codomain_and_action and agreed to the second à-first/colon uncertainty while retaining the first at low confidence and keeping égaux/g descender unchanged.',
    'accepted_fragment_sha256_before':hashlib.sha256(accepted.encode()).hexdigest(),
    'accepted_report_sha256_before':hashlib.sha256(prior_bytes).hexdigest(),
    'counts':{'material_findings':2,'certainty_only_findings':1,'prior_collation_rows_checked':34,'packet_difference_rows_checked':37,'original_marks_checked':2,'existing_inventory_elements_checked':16,'new_inventory_child_drawings':1,'remaining_doubts':7,'existing_crops_reused':9,'new_crops':0},
}

# Source-literal and structural checks only. No image opening or TeX execution.
for f in findings:
    assert f['before'] in accepted and f['after'] in candidate,f['place']
    assert f['C'] in packet['witness_C'],f['C']
    assert f['H'] in packet['witness_H'],f['H']
for row in collation_confirmation:
    assert row['C']=='[no witness]' or row['C'] in packet['witness_C'],row
    assert row['H']=='[no witness]' or row['H'] in packet['witness_H'],row
    assert row['reading'] in candidate,row
assert {d['id'] for d in report['decisions']}=={m['id'] for m in packet['marks']}
assert candidate.count(r'\unsure{à|:}')==2
assert candidate.count(r'\mspage{')==2 and candidate.count(r'\scanpage{')==1
assert r'\underbrace' not in candidate
assert r'\unsure{\hookrightarrow|\lhook\joinrel\relbar}' in candidate
assert r'\deleted{Mais \unsure{on}}' in candidate
for crop in viewed:assert (WORK/crop).is_file(),crop
depth=0;i=0
while i<len(candidate):
    char=candidate[i]
    if char=='%':
        end=candidate.find('\n',i);i=len(candidate) if end<0 else end+1;continue
    if char=='\\':
        i+=1
        if i<len(candidate) and candidate[i].isalpha():
            while i<len(candidate) and candidate[i].isalpha():i+=1
        else:i+=1
        continue
    if char=='{':depth+=1
    if char=='}':depth-=1;assert depth>=0
    i+=1
assert depth==0
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',candidate):
    if m.group(1)=='begin':stack.append(m.group(2))
    else:assert stack.pop()==m.group(2)
assert not stack
assert page_path.read_text()==accepted and prior_path.read_bytes()==prior_bytes
report['validation']={'literal_C_H_excerpts':'passed','literal_before_after':'passed','original_MARKS_coverage':'passed','balanced_braces_and_environments':'passed','existing_crop_paths_and_boxes':'passed','accepted_files_unchanged':'passed','tex_compilation':'not performed','new_crops_or_recrops':'none','ocr_or_external_research':'not performed'}
tex_out=WORK/'reviews'/f'{KEY}_auditC.tex';json_out=WORK/'reviews'/f'{KEY}_auditC.json'
tex_out.write_text(candidate)
json_out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tex':str(tex_out),'report':str(json_out),'counts':report['counts'],'validation':report['validation']},ensure_ascii=False,indent=2))
