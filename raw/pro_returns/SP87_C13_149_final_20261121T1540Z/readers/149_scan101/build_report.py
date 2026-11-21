from pathlib import Path
import json
p=Path('SP87_C13_149_work/readers/149_scan101')
b=json.loads((p/'crop_boxes.json').read_text())
def cp(n): return f'crops/149_scan101_{n}.png'
changes=[]
def ch(place,c,h,final,evidence,n,kind,ac,ah,confidence='high',marked=False,consequential=False):
 changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop=cp(n),box=b[n],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=marked,consequential=consequential))
ch('i_e_stops','i.e.','i.e.','i e.',
 'The i has its detached upper dot and low right return, followed by a separate low e and one terminal point. No independent point follows the body of i; its upper dot is not counted twice.',
 'admissible','text not on the page',True,True)
ch('quelle_underline',r'\uline{quelle}','quelle',r'\uline{quelle}',
 'A separate lower horizontal stroke runs beneath the right portion of quelle. It is detached from the letter bodies and the long q descender, so the written underline is retained.',
 'quelle_underline','omission',False,True)
ch('si_ce_n_est',"si ce n'est",r'\uncertain{i.e. ce serait}',"si ce n'est",
 'The first short word has an s-shaped entry and detached i dot. Ce is followed by the low n, a raised apostrophe and a short e-s-t chain with its final crossed/upturned t. There is no i.e. punctuation or initial long s for serait.',
 'si_ce','misread word',False,True,marked=True)
ch('inexistant','inexistant','inexistante','inexistant',
 'The last written letter is a tall t with a cross-stroke. A blank separates it from the exclamation mark; no final e follows the t. The masculine ending is retained without grammatical correction.',
 'inexistant','misread word',False,True)
ch('margin_phrase',r"mais il y a tjrs une ``arithmétisation''",r'mais si !? \uncertain{très} \ill{} « réduits »',r"mais il y a tjrs une arithmetisation''",
 'On the rotated marginal crop, the initial i/l/y/a are separate forms, then the crossed t and descending j of tjrs and the low humps of une. The next word shows the arithmetisation letter chain, including the tall th and t strokes. There is no detached accent over the first e and no opening quote pair before its a; two closing ticks after the word are plain. Neither si!? nor très nor réduits matches these strokes.',
 'margin','misread word',True,True,marked=True,consequential=True)
ch('margin_innocente',r'\unsure{innocente} !',r'\ill{}','innocente !',
 'After π, the crop shows initial dotted i, two low n joins, compact o, open c/e, another low n, a tall crossed t and final e, followed by a distinct exclamation stroke and dot. The preferred C word is now readable without its doubt.',
 'margin',r'readable ink left as \ill{}',False,True,marked=True)
ch('qu_on_compose_avec',"qu'on compose avec",r'\ill{}',"qu'on compose avec",
 'The main line has a long q descender with raised apostrophe, then the open c/o, descending p and low o-s-e sequence of compose. The following short a-v-e-c chain precedes une; all are live on the same line.',
 'compose',r'readable ink left as \ill{}',False,True,marked=True)
ch('donc_une','donc une',r'qui \uncertain{comprend} \uncertain{une}','donc une',
 'After the dash ending the preceding line, the next main line starts with looped d and a low o-n-c sequence. Une follows as three low connected humps. There is no q descender or room for comprend at this position.',
 'action_effective','misread word',False,True,marked=True)
ch('action_effective',r'action \inserted{effective}',r'\add{affection} \ill{}',r'action \inserted{effective}',
 'Action is on the body line. Above its right end, the inserted word has two long f stems, low e/c, crossed t, i dot and v/e ending. Its curved leader descends between action and de. The placement and final v/e strokes exclude an inserted affection.',
 'action_effective','insertion or placement',False,True,marked=True,consequential=True)
ch('no_dans_une_action','(nothing)',r'\uncertain{dans} une action,','(nothing)',
 'A single horizontal dash follows π at the right end of the body line. The next line begins directly with the long q descender of qu’attendre; no dans une action phrase intervenes.',
 'action_effective','text not on the page',False,True,marked=True)
ch('Sans_state','Sans',r'\struck{Sans} \ill{}',r'\unsure{Sans|\deleted{Sans}}',
 'The dark lower stroke begins at the foot of the capital S and follows the low joins of a/n/s. No clearly independent transverse stroke can be isolated, favouring live Sans. The heavy overdraw still permits a cancellation interpretation, retained explicitly as the alternative. The gap before m’y contains no extra word.',
 'Sans','deletion state',False,True,confidence='medium',marked=True)
ch('me_voici','me voici',r'\ill{}','me voici',
 'The first word has the low m/e humps. The next has a rounded v/o entry, two detached i marks around an open c, and no intervening cancellation. These are ordinary body words before à tâter.',
 'me_voici',r'readable ink left as \ill{}',False,True,marked=True)
ch('un_peu','un peu',r'\ill{} pour','un peu',
 'Un is written at the end of the first line as two low humps. Peu begins the next line with a descending p, small e and final u return; it has no terminal r. The line break does not make the two words an insertion.',
 'un_peu_structure','misread word',False,True,marked=True)
ch('colon_after_structure','à',':',':',
 'After structure, two compact detached marks are vertically aligned. The lower mark has no loop or body of a. The nearby à before tâter has an independently visible small a body beneath its accent, providing a same-page contrast. The colon is retained despite the unusual syntax.',
 'un_peu_structure','misread symbol or index',True,False,consequential=True)
ch('celle_ci_hyphen','celle-ci','celle-ci','celle ci',
 'Celle ends in a low horizontal e return. Blank paper separates it from the open c and dotted i of ci; there is no short hyphen in that gap. The following two-dot colon is separate.',
 'celle_ci','text not on the page',True,True)
ch('conjecture_heading',r'\uline{Conjecture-à-tout-hasard}',r'\textbf{Conjecture de bonne réduction}',r'\uline{Conjecture-à-tout-hasard}',
 'After Conjecture, the crop shows a short dash, accented à, another dash, two t uprights around the low ou of tout, another dash, and hasard with its tall h and final d. One continuous underline lies beneath the title and stops before its colon. H’s de bonne réduction is not written.',
 'conjecture','misread word',False,True,consequential=True)
ch('folio_100',r'\margin{100}','(omitted)',r'\margin{100}',
 'The lower-left margin has a narrow inclined 1 followed by two separate closed zero ovals. Its thin small script is distinct from the main prose hand.',
 'folio','omission',False,True)

tex=r'''\scanpage{101}
\mspage{50}
définit une extension de $\mathcal E_k$ par $\pi$, donc une action extérieure --- est-elle ``admissible'' \unsure{?}, i e. définie par une courbe algébrique ? Sans doute pas --- \uline{quelle} courbe serait-ce, si ce n'est la courbe ``réduite'' de type $(g,\nu)$ (inexistant !) ?
\margin{mais il y a tjrs une arithmetisation'' de $\pi$ innocente !}

Dès lors, si on a une section de (30) qu'on compose avec une de (31) --- donc une action \inserted{effective} de $\mathcal E_k$ sur $\pi$ --- qu'attendre d'une telle action ?

\unsure{Sans|\deleted{Sans}} m'y attendre, me voici à tâter un peu la structure : l'$\infty$ des variétés modulaires de Teichm\unsure{ü|ù}ller !

S'il faut hasarder des conjectures dans cette situation scabreuse, ce pourrait-être celle ci :

\uline{Conjecture-à-tout-hasard} : Les conditions suivantes sont équivalentes

\noindent a) $U_\eta$ a bonne réduction sur $S$

\noindent b) L'action extérieure de $T$ sur $\pi$ est triviale
\margin{100}
'''
(p/'draft.tex').write_text(tex)

inventory=[]
def inv(el,kind,pos,words,hand='his hand'):
 inventory.append(dict(element=el,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('author_number','margin note','top centre above the first prose line','50')
inv('opening_questions','text','main lines 1–6','définit une extension de E_k par π')
inv('slanted_note','margin note','left margin beside main lines 5–8, four short slanted rows',"mais il y a tjrs une arithmetisation''")
inv('sections_paragraph','text','main lines 7–10','Dès lors, si on a une section de (30)')
inv('effective_insertion','insertion','above main line 9, attached between action and de','effective')
inv('moduli_paragraph','text','main lines 11–13',r'\unsure{Sans|\deleted{Sans}} m’y attendre')
inv('possible_Sans_cancellation','deletion','start of main line 11; cancellation is only an alternative state',r'\unsure{Sans|\deleted{Sans}}')
inv('conjecture_introduction','text','main lines 14–16','S’il faut hasarder des conjectures')
inv('conjecture_heading','text','main lines 17–18','Conjecture-à-tout-hasard : Les conditions suivantes sont équivalentes')
inv('condition_a','text','main line 19',r'a) $U_\eta$ a bonne réduction sur $S$')
inv('condition_b','text','main line 20',r'b) L’action extérieure de $T$ sur $\pi$ est triviale')
inv('folio','margin note','lower-left margin','100','another unnamed hand')

second=[]
def sb(num,kind,box,reading):
 second.append(dict(box=f'101_B{num:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
sb(1,'handwritten number',[789,34,858,86],'50')
sb(2,'doubtful punctuation and abbreviation',b['admissible'],r"``admissible'' \unsure{?}, i e.")
sb(3,'underline',b['quelle_underline'],r'\uline{quelle}')
sb(4,'word difference',b['si_ce'],"si ce n’est la courbe")
sb(5,'word difference',b['inexistant'],'(inexistant !) ?')
sb(6,'margin note',b['margin'],r"mais il y a tjrs une arithmetisation'' de $\pi$ innocente !")
sb(7,'handwritten number',[1495,711,1631,794],'(30)')
sb(8,'word difference and handwritten number',b['compose'],r"qu’on compose avec une de (31) --- \inserted{effective}")
sb(9,'insertion and word differences',b['action_effective'],r"donc une action \inserted{effective} de $\mathcal E_k$ sur $\pi$ --- qu’attendre d’une telle action ?")
sb(10,'possible deletion',b['Sans'],r'\unsure{Sans|\deleted{Sans}} m’y')
sb(11,'word difference',b['me_voici'],'me voici')
sb(12,'word and punctuation differences',b['un_peu_structure'],r'\unsure{Sans|\deleted{Sans}} m’y attendre, me voici à tâter un peu la structure : l’$\infty$ des variétés')
sb(13,'name diacritic',b['Teichmuller'],r'Teichm\unsure{ü|ù}ller !')
sb(14,'resolved doubt',b['scabreuse'],'scabreuse,')
sb(15,'punctuation difference',b['celle_ci'],'être celle ci :')
sb(16,'word difference and underline',b['conjecture'],r'\uline{Conjecture-à-tout-hasard} :')
sb(17,'whole formula',b['U_eta'],r'a) $U_\eta$ a bonne réduction sur $S$')
sb(18,'handwritten number',b['folio'],'100')

coverage=[]
def dc(d,disposition,place=''):
 coverage.append(dict(diff_id=d,disposition=disposition,change_place=place))
dc('D0536','editorial-only: C scan marker 101 versus H author-page note; the written author number 50 is retained')
dc('D0537','editorial-only: de l’auteur is part of H’s page note, not source text')
dc('D0538','macro/editorial-only: triple hyphen and Unicode em dash encode the same manuscript dash')
dc('D0539','macro/editorial-only: H’s typographic guillemets versus C’s double-quote convention; the two written quote strokes are represented with backticks/apostrophes')
dc('D0540','macro/editorial-only: triple hyphen and Unicode em dash encode the same manuscript dash')
dc('D0541','substantive: si is read from its s and detached i dot','si_ce_n_est')
dc('D0542','substantive: n’est has the low n, apostrophe and terminal t','si_ce_n_est')
dc('D0543','macro/editorial-only: H’s typographic guillemets versus C’s double-quote convention; the written double strokes are retained')
dc('D0544','substantive: no final e after inexistant','inexistant')
dc('D0545','substantive: marginal phrase recovered; missing opening quote and missing accent retained literally','margin_phrase')
dc('D0546','substantive: innocente and exclamation read; M1295 resolved first','margin_innocente')
dc('D0547','substantive: live body phrase recovered from H illegibility','qu_on_compose_avec')
dc('D0548','substantive: donc une follows the dash','donc_une')
dc('D0549','substantive: body action and supralinear effective are distinct','action_effective')
dc('D0550','substantive: no dans une action phrase between π and qu’attendre; dash glyph difference is editorial','no_dans_une_action')
dc('D0551','substantive: me voici is live body text','me_voici')
dc('D0552','substantive: un at preceding line end joins peu, not pour','un_peu')
dc('D0553','substantive: two separated marks form a colon','colon_after_structure')
dc('D0554','substantive: written heading is Conjecture-à-tout-hasard','conjecture_heading')
dc('D0555','macro/editorial-only: opening enumerate and optional-label syntax')
dc('D0556','macro/editorial-only: closing optional-label delimiter for a)')
dc('D0557','macro/editorial-only: opening optional-label delimiter for b)')
dc('D0558','macro/editorial-only: closing optional-label delimiter for b)')
dc('D0559','substantive: manuscript foliation 100 retained; H enumerate/end-document commands and its note about continuation beyond the lot are editorial','folio_100')

report=dict(
 scan=101,line_count=20,changes=changes,
 marks=[
  dict(id='M1295',decision='first',reading='innocente',evidence='The rotated margin crop shows dotted i, low nn, o/c/e, n, crossed t and final e, followed by the independent exclamation mark.',crop=cp('margin'),box=b['margin'],confidence='high'),
  dict(id='M1296',decision='first',reading='scabreuse',evidence='The crop separates the initial s/c, compact a, tall b, low r/e/u and final s/e sequence; no cancellation obscures the word.',crop=cp('scabreuse'),box=b['scabreuse'],confidence='high')
 ],
 inventory=inventory,second_boxes=second,
 notes=(
  'Page content: The leaf asks whether an extension of E_k by π defines an admissible outer action arising from an algebraic curve, and questions which curve could realise it. A left marginal qualification says that an innocent arithmetisation of π is always available. The next paragraph considers composing sections of (30) and (31), thereby obtaining the action called effective, and asks what to expect from it. The author then describes unexpectedly touching the structure at infinity of Teichmüller moduli varieties and proposes a Conjecture-à-tout-hasard. The two conditions written here are that U_eta have good reduction over S and that the outer action of T on π be trivial. This is a conjectural equivalence on the page, not a proved theorem.\n\n'
  'Visual review: The whole leaf and both full-resolution halves were read once, including every word and symbol on which C and H agree. There are twenty main rows, a four-row slanted marginal note, one interlinear insertion effective, the author number 50, and foliation 100 in another unnamed hand. There is no display, diagram or drawing. Seventeen saved unique crops cover the word differences, supplied doubts and crowded/open places, including H’s omitted underline beneath quelle. The marginal crop was rotated −30 degrees after its original box was recorded. No OCR, external research, recropping or compilation was used. The effective leader lands between action and de.\n\n'
  'Literal reading decisions: The source has only the terminal point in i e.; the i’s upper dot is not an abbreviation stop. In the marginal arithmetisation, no opening quote pair and no detached accent over e are visible; the closing pair is retained without balancing it. Inexistant has no final e. Celle ci has no hyphen. The two separate marks after structure are a colon, despite the syntax that would suggest à; the nearby à before tâter has a distinct small a body. The source’s full heading and its underline are retained. The same-page complete item confirms U_eta locally without turning its rounded subscript into K. The top-half view and des_lors crop show the compact accent in Dès.\n\n'
  'Unresolved state and shape: The heavy lower stroke beneath Sans joins the S foot and low letters, favouring live Sans, but a cancellation remains an explicit alternative. The question mark after admissible is overwritten and remains doubtful; no separate cancelled sign has been invented. A single short oblique mark lies over the u of Teichmüller; the letter sequence is clear, while ü versus ù remains unresolved. Faint hollow traces above the earlier part of that name are much lighter than the body ink and are not transcribed as an extra word.\n\n'
  'Actual mathematical checks: This reader performed no independent mathematical proof, computation, use or refutation. The check_events list is empty. All checks reported above are visual reading and attachment checks. The adjective effective is transcribed without treating it as a demonstrated claim of faithfulness.'
 ),
 check_events=[],
 hand_observations=[
  dict(habit='Capital-S lower return can merge with following low letter joins and resemble a cancellation.',pages=[101],evidence='Sans crop: the dark lower stroke connects to the S foot, while a separate strike cannot be fully excluded.',witness_errors=['H declares Sans struck; C declares it live. The live state is preferred but both remain.']),
  dict(habit='Compact colon marks must be distinguished from the body and accent of à.',pages=[101],evidence='After structure the lower mark is compact and separate, unlike the visible looped a beneath the nearby accent before tâter.',witness_errors=['C reads à where the local stroke comparison supports H’s colon.']),
  dict(habit='A written accent on a proper name can remain ambiguous in shape.',pages=[101],evidence='Teichmuller crop: a single oblique mark occurs over u; two independent diaeresis dots are not recoverable.',witness_errors=['Both witnesses give certain ü; ü|ù is retained.']),
  dict(habit='A small slanted marginal short form retains its letters rather than a guessed expansion.',pages=[101],evidence='The rotated note has crossed t, descending j, r and final s in tjrs.',witness_errors=['H substitutes très amid a misread marginal phrase.'])
 ],
 notation_additions=[],
 abbreviations=[dict(form='tjrs',expansion='toujours'),dict(form='i e.',expansion='id est')],
 unresolved=[
  dict(place='admissible_question',reading=r'\unsure{?}',alternatives='The preferred question mark is heavily retraced; the individual overwritten strokes and any earlier state cannot be separated.',confidence='medium'),
  dict(place='Sans_state',reading=r'\unsure{Sans|\deleted{Sans}}',alternatives=r'\deleted{Sans}',confidence='medium'),
  dict(place='Teichmuller_diacritic',reading=r'Teichm\unsure{ü|ù}ller',alternatives='Teichmùller',confidence='medium')
 ],
 certainty_only=[
  dict(place='admissible_question',c='?',h='?',final=r'\unsure{?}',evidence='The original question shape is heavily retraced; the adjacent comma is separate. No new primary punctuation reading is asserted.',crop=cp('admissible'),box=b['admissible'],confidence='medium'),
  dict(place='scabreuse',c=r'\unsure{scabreuse}',h='scabreuse',final='scabreuse',evidence='All letters are recovered on the mandatory doubt crop; the primary lexical reading is unchanged.',crop=cp('scabreuse'),box=b['scabreuse'],confidence='high'),
  dict(place='Teichmuller_diacritic',c='Teichmüller',h='Teichmüller',final=r'Teichm\unsure{ü|ù}ller',evidence='The word’s letter sequence is intact, but one oblique accent mark does not resolve ü versus ù. The witnesses’ primary reading remains first.',crop=cp('Teichmuller'),box=b['Teichmuller'],confidence='medium')
 ],
 diff_coverage=coverage
)
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'marks':len(report['marks']),'inventory':len(inventory),'second_boxes':len(second),'crops':len(b),'diff_coverage':len(coverage),'unresolved':len(report['unresolved'])}))
