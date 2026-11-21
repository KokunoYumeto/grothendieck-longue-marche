import json
from pathlib import Path
p=Path('SP87_C13_149_work/readers/149_scan097')
boxes=json.loads((p/'crop_boxes.json').read_text())

def crop(name): return 'crops/149_scan097_'+name+'.png'
changes=[]
def change(place,c,h,final,evidence,name,kind,ac,ah,confidence='high',marked=False,consequential=False):
 changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop=crop(name),box=boxes[name],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=marked,consequential=consequential))

change('opening_actions',r'actions de $\Gamma\prime$',r'actions \uncertain{extérieures} de $\Gamma\prime$',r'actions de $\Gamma\prime$',
 'The low final s of actions is followed by a clear blank and the looped d of de; there are no intervening letter strokes for extérieures. The Γ prime is separately visible.',
 'actions','text not on the page',False,True,marked=True)
change('barred_M',r'\={M}','Même',r'\={M}',
 'The opening has one capital M, with two tall uprights and a central valley, and a separate horizontal bar above it. No following ême letters are written.',
 'barre_M','abbreviation expanded or spelling modernised',False,True)
change('quand_on_regarde','quand on regarde',r'\add{\ill{}} qui \uncertain{font} apparaître','quand on regarde',
 'After K and its comma, the first word has a long q descender, a low extended u-a-n chain and a final d rise; the next two short marks form on. The following word has the descending g loop and terminal d/e of regarde. There is no independent supralinear insertion here.',
 'quand_regarde','misread word',False,True,marked=True)
change('first_later_Ek_and_comma',r'$\mathcal E_{k\prime}$,',r'$\mathcal E_k$',r'$\mathcal E_k$,',
 'In the first sur des group, the small k ends without a separate raised prime. A distinct downward comma follows at the body baseline. The initial primed E_k on the previous line, retained unchanged, supplies a visible same-page prime control.',
 'insertion_composant','misread symbol or index',True,True,consequential=True)
change('inserted_ou_underline',r'\inserted{ou des sous-groupes ouverts $\Gamma\prime$ de ceux-ci,}',r'\add{ou des sous-groupes ouverts $\Gamma\prime$ de ceux-ci}',r'\inserted{\uline{ou} des sous-groupes ouverts $\Gamma\prime$ de ceux-ci,}',
 'A short separate horizontal stroke lies immediately below ou, distinct from both its low letter returns and the much longer attachment leader below the entire insertion. The words are on two small interlinear rows, and the leader turns down after the first E_k comma.',
 'insertion_composant','other',True,True)
change('en_la_composant_avec','en la composant avec',r'\ill{}','en la composant avec',
 'Below the insertion leader, en has its low connected baseline, la its looped l, and composant its descending p and final t rise. Avec begins the following main line with open a/v/e/c strokes; the words are live running text.',
 'insertion_composant',r'readable ink left as \ill{}',False,True,marked=True)
change('composant_stop','(no stop)','(no stop)',r'\unsure{.}',
 'A small dark oval is separate from the final t of composant and lies just below the insertion leader, to the right of the word in punctuation position. It is comparable in darkness to nearby writing, but an isolated pen deposit cannot be excluded; absence of a stop remains the alternative.',
 'insertion_composant','omission',True,True,confidence='medium',marked=True)
change('second_later_Ek_prime',r'$\mathcal E_{k\prime}$',r'$\mathcal E_k$',r'$\mathcal E_{k\prime}$',
 'At the far right of the next main line, a short raised oblique tick follows the small k and precedes a longer horizontal dash. The tick and dash are distinct marks, so this occurrence retains its prime.',
 'insertion_composant','misread symbol or index',False,True,consequential=True)
change('no_ou_before_sous_groupes','--- des sous-groupes','— ou des sous-groupes','--- des sous-groupes',
 'The preceding line ends with the prime and long dash. The next line begins directly with the looped d of des and then sous-groupes; no ou stands between them.',
 'sous_groupes','text not on the page',False,True)
change('subgroup_Ek_unprimed',r'$\Gamma\prime\subset\mathcal E_{k\prime}$',r'$\Gamma\prime\subset\mathcal E_k$',r'$\Gamma\prime\subset\mathcal E_k$',
 'The final k in the subgroup expression has its upright and low right branch, followed only by the sentence point. There is no small raised tick between k and that point. Γ itself has a clear prime.',
 'sous_groupes','misread symbol or index',True,False,consequential=True)
change('no_closing_parenthesis','(no closing parenthesis)',')','(no closing parenthesis)',
 'Only a compact point follows the final k; the space before the next J’ai is open. No tall curved closing-parenthesis stroke is present. The earlier opening parenthesis remains unbalanced.',
 'sous_groupes','text not on the page',False,True)
change('definition_insertion_attachment',r'$\mathcal E_{k(s)}$, \inserted{définie par (29),} définissant des',r'$\mathcal E_{k(s)}$ définie par (29), \add{ou définissant des}',r'$\mathcal E_{k(s)}$ \inserted{définie par (29)}, définissant des',
 'Définie par (29) is above the body line. Its long leader curves down between E_{k(s)} and the pre-existing body comma. The right upward curl after (29) is continuous with that leader, rather than a second independent comma. Définissant des remains on the body line.',
 'insertion_definition','insertion or placement',True,True,consequential=True)
change('no_ou_before_definissant','définissant des',r'\add{ou définissant des}','définissant des',
 'The live word starts with the dark looped d and its accented e, then the tall f. The faint hollow double outlines immediately to its left are far lighter than the writing and do not establish a live ou or a recoverable cancellation. They are documented for blind review without supplying a word.',
 'insertion_definition','text not on the page',False,True,confidence='medium')
change('effectives',r'\unsure{effectives}','extérieures','effectives',
 'Two separate tall descending f stems follow the initial e entry; the later crossed t, detached i dot, low v, and e/s ending are visible. This sequence supports effectives and lacks the x followed by t of extérieures.',
 'effectives','misread word',False,True,consequential=True)
change('ext_without_stop','ext',r'\uncertain{ext.}','ext',
 'After the open e, crossed x and upright crossed t, there is blank paper before the closing parenthesis. No independent abbreviation stop is visible.',
 'ext','text not on the page',False,True,marked=True)
change('dernieres_derniers','dernières','derniers',r'\unsure{dernières|derniers}',
 'The looped d and compressed der-ni sequence are secure. The final low connected humps favour C’s feminine ending but do not allow every e stroke to be isolated, so H’s shorter ending remains possible. No grammatical agreement has been used to remove that alternative.',
 'dernieres','misread word',False,True,confidence='medium')
change('no_insertion_after_plutot','plutôt comme',r'plutôt \add{\ill{}} comme','plutôt comme',
 'The final t of plutôt has its upright and low right return, with the accent above the preceding o. The following margin/interline area is blank; comme begins normally at the left of the next line. No added word is present.',
 'plutot','text not on the page',False,True,marked=True)
change('live_sous_anneaux','sous-anneaux',r'\struck{\ill{}} anneaux','sous-anneaux',
 'Sous is a live low sequence with separated short returns, followed by a short hyphen and the a-n-n-e-a-u-x sequence. No transverse cancellation crosses the prefix or noun.',
 'sous_anneaux','deletion state',False,True,marked=True)
change('no_locaux','(nothing)','locaux','(nothing)',
 'After the crossed final x of anneaux and the punctuation, the next letter is the tall open capital C of Cependant. There are no intervening l-o-c-a-u-x strokes.',
 'sous_anneaux','text not on the page',False,True)
change('colon_after_anneaux','.', '.', ':',
 'Two short separated dark marks are vertically aligned after the final x: an upper point and a lower point. They form a colon rather than the single point supplied by both witnesses.',
 'sous_anneaux','misread symbol or index',True,True)
change('folio_96',r'\margin{96}','(omitted)',r'\margin{96}',
 'The lower-left margin has a narrow 9 with a descending curved tail and a separate 6 with an enclosed lower loop. The small thin writing is distinct from the main prose hand.',
 'folio','omission',False,True)

tex=r'''\scanpage{97}
\mspage{48}
correspondante de $\mathcal E_{U_K}$ sur $\Gamma'$ --- d'où, en particulier, des actions de $\Gamma'$ sur $\pi$.

(\={M} chose d'ailleurs pour des sous-corps $k'$ quelconques de $K$, quand on regarde $\mathcal E_K$ comme étant sur $\mathcal E_{k'}$ : la section (29) donne une famille de sections de $\mathcal E_{U_K}$ sur des $\mathcal E_k$, \inserted{\uline{ou} des sous-groupes ouverts $\Gamma'$ de ceux-ci,} en la composant\unsure{.} avec des sections de $\mathcal E_K$ sur des $\mathcal E_{k'}$ --- des sous-groupes $\Gamma'\subset\mathcal E_k$. J'ai envie d'avoir une vue d'ensemble sur cette famille de sections, et de la mettre en relation avec la famille de sections des $\mathcal E_{X_s}$ sur les $\mathcal E_{k(s)}$ \inserted{définie par (29)}, définissant des actions effectives (pas seulement ext) des $\mathcal E_{k(s)}$ sur $\pi$. Pour ces \unsure{dernières|derniers}, les $k(s)$ n'apparaissent pas comme des sous-corps de $K$, mais plutôt comme des $\underline{\mathcal O}_s/\mathfrak m_s$ --- des corps résiduels de sous-anneaux : Cependant, si on suppose $S$ de dim \deleted{\unsure{finie}} \inserted{relative 1} sur
\margin{96}
'''
(p/'draft.tex').write_text(tex)

inventory=[]
def inv(element,kind,position,words,hand='his hand'):
 inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('author_page_number','margin note','top centre above the first line','48')
inv('opening_continuation','text','main lines 1–2',r'correspondante de $\mathcal E_{U_K}$')
inv('main_parenthetical_text','text','main lines 3–20',r'(\={M} chose d’ailleurs pour des sous-corps')
inv('open_subgroups_insertion','insertion','two smaller rows between main lines 6–7, attached after the E_k comma',r'\uline{ou} des sous-groupes ouverts $\Gamma\prime$ de ceux-ci,')
inv('definition_insertion','insertion','between main lines 12–13, attached before the body comma after E_{k(s)}','définie par (29)')
inv('cancelled_dimension_word','deletion','main line 20, after dim',r'\unsure{finie}')
inv('relative_dimension_replacement','insertion','above the cancelled word on main line 20','relative 1')
inv('lower_foliation','margin note','bottom-left margin','96','another unnamed hand')

second=[]
def sb(num,kind,box,reading):
 second.append(dict(box=f'097_B{num:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
sb(1,'handwritten number',[808,32,882,88],'48')
sb(2,'word difference',boxes['actions'],r'des actions de $\Gamma\prime$ sur $\pi$.')
sb(3,'word difference',boxes['barre_M'],r'(\={M} chose d’ailleurs')
sb(4,'word difference',[920,340,1625,470],r'$K$, quand on regarde')
sb(5,'handwritten number',[298,620,409,698],'(29)')
sb(6,'formula and punctuation',[790,678,918,779],r'$\mathcal E_k$,')
sb(7,'insertion',[896,620,1624,704],r'\inserted{\uline{ou} des sous-groupes ouverts $\Gamma\prime$ de ceux-ci,}')
sb(8,'doubtful punctuation',[944,698,1520,775],r'en la composant\unsure{.}')
sb(9,'word difference',[315,822,633,902],'avec des')
sb(10,'formula',[1496,742,1646,837],r'$\mathcal E_{k\prime}$ ---')
sb(11,'word and formula differences',boxes['sous_groupes'],r'des sous-groupes $\Gamma\prime\subset\mathcal E_k$.')
sb(12,'insertion and word difference',boxes['insertion_definition'],r'$\mathcal E_{k(s)}$ \inserted{définie par (29)}, définissant des')
sb(13,'resolved doubt',[610,1480,930,1670],'effectives')
sb(14,'word difference',boxes['ext'],'ext)')
sb(15,'word difference',boxes['dernieres'],r'ces \unsure{dernières|derniers},')
sb(16,'open place',boxes['napparaissent'],r'$k(s)$ n’apparaissent')
sb(17,'word difference',boxes['plutot'],'plutôt')
sb(18,'whole formula',boxes['residual'],r'$\underline{\mathcal O}_s/\mathfrak m_s$')
sb(19,'word and punctuation differences',boxes['sous_anneaux'],'de sous-anneaux : Cependant,')
sb(20,'deletion and insertion',boxes['final_edit'],r'$S$ de dim \deleted{\unsure{finie}} \inserted{relative 1} sur')
sb(21,'handwritten number',boxes['folio'],'96')

coverage=[]
def dc(d,disposition,place=''):
 coverage.append(dict(diff_id=d,disposition=disposition,change_place=place))
dc('D0463','editorial-only: C scan marker 97 versus H author-page note; source author number 48 is retained in mspage')
dc('D0464','editorial-only: de l’auteur belongs to H’s page note and is not manuscript text')
dc('D0465','macro/editorial-only: TeX triple hyphen and Unicode em dash encode the same manuscript dash')
dc('D0466','substantive: unsupported H word omitted','opening_actions')
dc('D0467','substantive: unexpanded written short form retained','barred_M')
dc('D0468','substantive: C phrase confirmed on its mandatory crop','quand_on_regarde')
dc('D0469','substantive: unprimed k with the visible following comma','first_later_Ek_and_comma')
dc('D0470','substantive: live phrase recovered from H illegibility','en_la_composant_avec')
dc('D0471','substantive: small prime retained at this occurrence','second_later_Ek_prime')
dc('D0472','substantive: H adds ou after the manuscript dash','no_ou_before_sous_groupes')
dc('D0473','substantive: final subgroup index lacks a prime','subgroup_Ek_unprimed')
dc('D0474','substantive: no closing parenthesis in the source','no_closing_parenthesis')
dc('D0475','substantive: the insertion attaches before the existing body comma; no duplicate comma','definition_insertion_attachment')
dc('D0476','substantive: no live ou before définissant','no_ou_before_definissant')
dc('D0477','substantive: effectives read from paired f stems; M1286 first resolved','effectives')
dc('D0478','substantive: abbreviation has no stop','ext_without_stop')
dc('D0479','substantive: C’s feminine reading preferred, H retained as alternative','dernieres_derniers')
dc('D0480','macro/editorial-only: spacing around the same apostrophe and n; H’s uncertainty is separately recorded as certainty-only')
dc('D0481','macro/editorial-only: TeX triple hyphen and Unicode em dash encode the same manuscript dash')
dc('D0482','substantive: live sous- is present and is not cancelled','live_sous_anneaux')
dc('D0483','substantive: locaux is not written','no_locaux')
dc('D0484','macro/editorial-only: normal versus nonbreaking space before the same inserted digit 1')
dc('D0485','substantive: manuscript margin number retained','folio_96')

report=dict(
 scan=97,line_count=20,changes=changes,
 marks=[dict(id='M1286',decision='first',reading='effectives',evidence='The crop shows the two separate tall f descenders, followed by the crossed t, detached i dot, and low v/e/s sequence. It is not the x-t start required by extérieures.',crop=crop('effectives'),box=boxes['effectives'],confidence='high')],
 inventory=inventory,second_boxes=second,
 notes=(
  'Page content: The leaf continues a discussion of sections of the groups attached to U_K and K, and of the resulting actions of Γ′ on π. It considers arbitrary subfields k′ of K and sections over their groups or open subgroups. The author wants an overall view of this family and a relation with the family of sections over the residue fields k(s), defined by (29). The latter are described as defining actions effectives, not merely ext, on π. The page contrasts these residue fields with subfields of K, writes them as O_s/m_s for subrings, and ends mid-sentence with S of relative dimension 1. The printed diplomatic word effectives is retained as manuscript language; no assertion of proved faithfulness is inferred from it.\n\n'
  'Visual review: One successful whole-sheet view and both full-resolution halves were read, including words on which the witnesses agree. There are twenty main prose rows, no display, diagram or drawing, three insertions, one struck word, the author’s top number 48, and a thin lower-left foliation 96 in another unnamed hand. Fifteen single crops cover every substantive word difference, the resolved supplied doubt, and the crowded or open places. No OCR, external research, recropping or compilation was used. Every C deletion/insertion was traced for state and attachment. The first long insertion follows the comma after the first unprimed E_k; its initial ou has an independent underline. The second insertion precedes the existing comma after E_{k(s)}. Its right hook belongs to the attachment leader. The final relative 1 replaces the struck finie after dim.\n\n'
  'Local reading decisions: Prime presence is deliberately left uneven: the initial E_{k′} and the later far-right E_{k′} retain visible ticks, while the first later E_k and the subgroup E_k have no prime. The dark oval after composant is provisionally a doubtful full stop; no stop, if this is an isolated pen deposit, is the alternative. The unclosed opening parenthesis is not balanced editorially. The very faint hollow outlines before définissant are not dark live letter strokes and have not been supplied as H’s ou; their region is included in the blind box. Dernières is preferred but derniers remains possible because the final low humps are compressed. Finie remains doubtful under the strike: its f and two i dots survive, but the intervening body is merged with the cancellation. The source has a colon after sous-anneaux. The underlined O_s/m_s was checked as a complete formula. E versus mathcal E and the O macro convention are not counted as lexical changes.\n\n'
  'Actual mathematical checks: This first reader performed no independent proof, computation, mathematical use or refutation. The check_events list is therefore empty; the reviews above are visual collation checks only.'
 ),
 check_events=[],
 hand_observations=[
  dict(habit='Paired tall f stems can be compressed into a single-looking initial cluster.',pages=[97],evidence='The effectives crop separates two descending stems and the later t/i/v sequence.',witness_errors=['H reads extérieures; C left effectives doubtful.']),
  dict(habit='A capital M with a separate overbar is an unexpanded short form.',pages=[97],evidence='The opening parenthetical word consists only of M and its horizontal upper bar.',witness_errors=['H expands it to Même.']),
  dict(habit='Insertion leaders may end before existing body punctuation and have a comma-like terminal hook.',pages=[97],evidence='The leader below définie par (29) curls down before the body comma; its right hook remains continuous with the leader.',witness_errors=['C duplicates the comma around the insertion; H assigns insertion status to the later body phrase.']),
  dict(habit='Small primes must be read occurrence by occurrence, even in repeated notation.',pages=[97],evidence='The first later E_k and the subgroup E_k have no tick; the intervening far-right E_{k′} has a separate raised tick before its dash.',witness_errors=['C supplies primes at two unprimed occurrences; H omits the visible prime at the intervening occurrence.'])
 ],
 notation_additions=[dict(written='Capital M with a separate upper horizontal bar',transcription=r'\={M}',evidence='barre_M crop: a single capital M and independent bar; short form for même, with expansion only in abbreviations.')],
 abbreviations=[dict(form=r'\={M}',expansion='Même'),dict(form='ext',expansion='extérieures'),dict(form='dim',expansion='dimension')],
 unresolved=[
  dict(place='composant_stop',reading=r'\unsure{.}',alternatives='No stop: the isolated oval may be a pen deposit rather than punctuation.',confidence='medium'),
  dict(place='dernieres_derniers',reading=r'\unsure{dernières|derniers}',alternatives='derniers',confidence='medium'),
  dict(place='struck_finie',reading=r'\deleted{\unsure{finie}}',alternatives='finie is the preferred reading, but the struck low letter bodies are not independently recoverable.',confidence='medium'),
  dict(place='pale_traces_before_definissant',reading='No word transcribed from the pale hollow traces.',alternatives='Possible erased or nontextual trace; a live ou is not supported.',confidence='medium')
 ],
 certainty_only=[
  dict(place='H_n_apparaitre',c="n’apparaissent",h=r'\uncertain{n\prime} apparaissent',final="n’apparaissent",evidence='The low n stroke and detached apostrophe precede the a and paired p descenders.',crop=crop('napparaissent'),box=boxes['napparaissent'],confidence='high'),
  dict(place='struck_finie',c=r'\deleted{\unsure{finie}}',h=r'\struck{finie}',final=r'\deleted{\unsure{finie}}',evidence='The f descender and two dots are visible, while the low interior letters merge with the horizontal strike. The primary word is unchanged and uncertainty is retained.',crop=crop('final_edit'),box=boxes['final_edit'],confidence='medium')
 ],
 diff_coverage=coverage
)
# Use conventional prime notation in all report readings as in the draft.
def conventional(x):
 if isinstance(x,str): return x.replace('\\prime', "'")
 if isinstance(x,list): return [conventional(i) for i in x]
 if isinstance(x,dict): return {k:conventional(v) for k,v in x.items()}
 return x
report=conventional(report)
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'marks':len(report['marks']),'inventory':len(inventory),'second_boxes':len(second),'crops':len(boxes),'diff_coverage':len(coverage),'unresolved':len(report['unresolved'])}))
