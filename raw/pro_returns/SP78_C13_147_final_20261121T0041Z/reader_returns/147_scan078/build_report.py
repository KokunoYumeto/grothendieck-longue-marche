from pathlib import Path
from datetime import datetime, timezone
import json

HERE=Path(__file__).parent
WORK=HERE.parent.parent
PACKET=Path('/workspace/scratch/ea90d891106a/runtime/packets/147_scan078')
P=(HERE/'proposed.tex').read_text()
C=(PACKET/'C.tex').read_text()
H=(PACKET/'H.tex').read_text()
boxes=json.loads((HERE/'crop_boxes.json').read_text())

def groups(text,macro):
    found=[]; start=0; needle=macro+'{'
    while (start:=text.find(needle,start))>=0:
        depth=0
        for end in range(start+len(macro),len(text)):
            ch=text[end]
            if ch in '{}' and (end==0 or text[end-1]!='\\'):
                depth+=1 if ch=='{' else -1
                if depth==0:
                    found.append(text[start:end+1]);start=end+1;break
        else: raise ValueError('Unclosed '+macro)
    return found

pd=groups(P,r'\diagram'); cd=groups(C,r'\diagram')
pm=groups(P,r'\margin'); cm=groups(C,r'\margin'); hm=groups(H,r'\marginal')
h97=r'\begin{tikzcd}'+H.split(r'\begin{tikzcd}',1)[1].split(r'\marginal',1)[0].strip()
trace=P[P.index(r'$\underset'):P.index('$ (97)')+1]
formula96=P[P.index(r'\['):P.index(r'\]')+2]

changes=[]
def add(place,c,h,final,evidence,crop,confidence='high',against_C=False,against_H=True,kind='misread word',marked=False,error='words',consequential=False):
    changes.append(dict(id=f'078-{len(changes)+1:02d}',place=place,C=c,H=h,final=final,evidence=evidence,crop=f'147_scan078_place{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,marked_in_H=marked,error_sheet_kind=error,consequential=consequential))

add('C inserted after ens.',r'\inserted{$C$}',r'$C$',r'\inserted{$C$}','The separate capital C is above the baseline. A tall V-like connector ends in the gap between ens. and d’arêtes; it is not ordinary inline text.','02',kind='insertion or placement',error='insertions put in wrong place')
add('Diagram (97), arrow ends and canceled upper portion',cd[0],h97,pd[0],'The live left vertical trace curls at its top and ends bluntly below: neither lower arrowhead arm is present. The canceled right vertical trace has a top hook and two lower arms forming a downward head. The upper horizontal arrow, upper-right object and right vertical arrow are crossed; H omits them from its diagram and discusses them in an editorial note. Direct TikZ preserves the unequal arrow ends and the crossed right-hand path. The canceled roofs remain doubtful, as recorded separately.','05',against_C=True,kind='drawing or diagram',error='drawings and diagrams',consequential=True)
add('Canceled roof above upper-left M in (97)',r'\deleted{\unsure{\wedge}}','',r'\deleted{\unsure{\wedge}}','A compact multiply crossed mark stands above the live upper-left M. Parts of an angular roof are compatible with the strokes, but the crosswork prevents an unqualified reading. H neither draws nor mentions this canceled accent.','05',confidence='low',kind='omission',error='omissions')
add('Canceled upper-right object in (97)',r'\deleted{\unsure{\widehat M_{\underline G\'}}}',r'M_{\underline{G}\'}',r'\deleted{\unsure{\widehat M_{\underline G\'}}}','M, the underlined G and its separate prime can be followed beneath the cancellation. The upper roof merges with a zigzag strike; a hat is preferred but not established. H’s editorial note names the object without a hat. This remains an unresolved comparison, not a declaration that H’s bare reading is disproved.','05',confidence='low',kind='misread symbol or index',error='symbols and indices')
add('First oblique margin note',cm[0],hm[0],pm[0],'Déployer has one p-descender, a tall l, then a long y-descender and reduced er; no second p sequence supports développer. The following groups are la déf. de, with the f cross-stroke and abbreviation point. Both G indices have separate underlines, the group superscript has a stem and dot, and another independent exclamation mark closes the note. H’s diptyque et gît en does not match these groups.','06',kind='misread word',error='words',consequential=True)
add('Before Si at start of subgroup paragraph','',r'\struck{\ill{}}','','No separate canceled word is visible before Si. The oblique strokes adjoining the S continue the marginal déf. above; the main S and dotted i remain live.','07',kind='text not on the page',marked=True,error='text not on page')
add('Si on','on',r"\uncertain{l'on}",'on','After Si there is a small reduced o and a short n run. There is no additional l ascender or apostrophe before them.','07',marked=True)
add('Between the two group names','ou','=', 'ou','A compact o-like dot/group is followed by a separate low u stroke along one baseline. There are not two parallel bars. Completion crop 18 includes both whole group formulas, their superscript stem-and-dot exclamations, and every index and underline.','18',kind='misread word',error='words',consequential=True)
add('Abbreviation before qui transforment','autom',r'\uncertain{automorphismes}','autom','The short run ends after autom, with no following morphismes syllables and no separate period. The next word begins with the distinct q-descender of qui.','08',kind='abbreviation expanded or spelling modernised',marked=True,error='abbreviations expanded spelling modernised')
add('Condition on the automorphisms',r'qui transforment $C$ en lui-$=$, et','',r'qui transforment $C$ en lui-$=$, et','The q-descender, tall initial t and descending f of transforment are visible, followed by a separate C, en, and lui with a dotted i. A short hyphen and two-bar repetition sign follow. The continuation et is read on the following native baseline. H drops this entire stability condition before qui induisent.','08',kind='omission',error='omissions',consequential=True)
add('Article before flèche','la',r'\uncertain{alors} le','la','The initial looped l and low a form one short word. There is no preceding group for alors and no separate terminal e for le; adjacent dark oblique strokes belong to the margin note.','09',marked=True)
add('M1072, noun before canceled verticale',r'\unsure{flèche}',r'\uncertain{morphisme}',r'\unsure{flèche}','The reduced word has an upper detached accent and short rising/returning strokes compatible with flèche, but several letter bodies are compressed and partly meet neighboring ink. It remains doubtful. H’s longer morphisme, which would require different descenders and more letter groups, is not substituted.','09',confidence='low',marked=True)
add('Canceled adjective after flèche',r'\deleted{\unsure{verticale}}',r'\struck{\ill{}}',r'\deleted{\unsure{verticale}}','The underlying letter sequence is compatible with verticale, including tall central strokes and later loops, but two horizontal cancellation strokes obscure its middle. Every letter cannot be separated, so the C doubt stays; this is a tentative reading against H’s illegible placeholder.','09',confidence='low',kind=r'readable ink left as \ill{}',marked=True,error='readable ink left as illegible')
add('Inserted replacement adjective',r'\inserted{horizontale}',r'\add{horizontal}',r'\inserted{horizontale}','The replacement stands above the canceled adjective. After the tall h, o, r/i and angular z, the final tall l returns into a short terminal e. The source’s feminine ending is retained.','09')
add('Small overworked trace below de before (97)','','',trace,'A separate dark interlinear trace has intersecting triangular/looped strokes and a short tail. No reliable letter or cancellation state can be recovered. The trace is reproduced graphically beneath de with an explicit doubt, without reading en or another word into it. Neither witness preserves it as a separate visible element.','10',confidence='medium',against_C=True,kind='omission',error='omissions')
add('Canceled word before une',r'\deleted{donc}','',r'\deleted{\unsure{donc}}','The d loop and low run are visible, but the thick horizontal strike obscures the central and terminal letters. Donc remains the tentative reading; the added doubt relative to C changes certainty only. H omits the canceled word.','20',confidence='low',kind='omission',error='struck text')
add('Unsupported separate en','en',r'\uncertain{en}','','The completed beginning of the line shows one continuous raised une-like run, not separate en and une groups. The strokes to its left belong to the oblique vérifier... margin note. The other interlinear trace under de (97) is unreadable and is preserved separately, so it cannot license en here. An en would make syntactic sense, but syntax does not provide recoverable letters.','20',confidence='medium',against_C=True,kind='text not on the page',marked=True,error='text not on page',consequential=True)
add('Raised replacement une','une',r'\uncertain{une}',r'\inserted{une}','The broad initial u bowl, following n humps and terminal e return form one run above the struck donc. Its higher position is a replacement/insertion, not the old baseline word.','20',against_C=True,kind='insertion or placement',marked=True,error='insertions put in wrong place')
add('Punctuation after display number (98)','(98)','(98)','(98):','Two distinct dark points stand immediately after the closing parenthesis. They are also visible in the independently rotated margin crop 12 and form a colon-like pair; both witnesses omit them.','11',against_C=True,kind='other',error='other')
add('Beginning of second oblique margin','Ce ne sont peut-être',r'que \uncertain{ce} \uncertain{ne} \uncertain{sont} \uncertain{peut-être}','Ce ne sont peut-être','The margin begins with a large open C and its e return, then the small ne and sont groups. No separate preceding q-descender or que occurs at the start. Peut-être has its p-descender, hyphen and tall t strokes.','12',marked=True)
add('Underline in second margin',r'\uline{locales}',r'\uncertain{locales}',r'\uline{locales}','One independent straight line runs immediately below locales and stops before its comma. The other words in the note are not included in that underline.','12',kind='other',marked=True,error='other')
add('End of second margin','il me semble -- à vérifier\\ldots',r'il \uncertain{paraît} \ill{}…','il me semble -- à vérifier\\ldots','After the comma are a dotted i, tall l and reduced me; the next line has the long m/b/l construction of semble. A dash precedes the accented à and vérifier, whose f descender and ending remain visible. Three terminal dots follow. H’s paraît and illegible remainder do not preserve these words.','12',marked=True)
add('Underline in germ definition',r'\uline{germe de multiplicité}',r'\emph{germe de} multiplicité',r'\uline{germe de multiplicité}','The straight line under germe de continues as a second straight segment under multiplicité on the next physical line. The latter is independent of the oblique marginal writing that crosses nearby.','13',kind='other',error='other')
add('Word before display (99)','induite','','induite','Completion crop 19 shows the initial reduced i/n run, the central d peak, the u/i run, and the final tall t with a detached rightward bar and e return. H omits the word.','19',kind='omission',error='omissions',consequential=True)
add('Display (99), first G in Gamma index',r'\Gamma^!_{\underline G,\underline G\'}',r'\Gamma^{!}_{\underline{G},\underline{G}\'}',r'\Gamma^!_{G,G\'}','The first G inside the Gamma index has no separate horizontal stroke below its body. This contrasts with the explicit underline under the adjacent M subscript and with the earlier Gamma indices in (98). Only this occurrence is changed.','15',against_C=True,kind='misread symbol or index',error='symbols and indices',consequential=True)
add('Display (99), second G-prime in Gamma index',r'\Gamma^!_{\underline G,\underline G\'}',r'\Gamma^{!}_{\underline{G},\underline{G}\'}',r'\Gamma^!_{G,G\'}','The second G-prime inside the Gamma index likewise has no independent underline; its prime is a separate raised stroke. The right-hand M subscript does have a clear underline. No bar is supplied by the surrounding notation.','15',against_C=True,kind='misread symbol or index',error='symbols and indices',consequential=True)
add('Third margin, defined germ wording','défini par',r', \uncertain{à} \uncertain{définir} \uncertain{par}','défini par','The line begins with the looped d and f-descender of défini, followed by a separate par with p-descender. There is no preceding à or terminal r of définir, and no independent comma is visible after multiplicité.','16',marked=True)
add('Third margin, local immersion phrase',r"l'\uline{immersion locale}",'',r"l'\uline{immersion locale}",'The apostrophe after l is followed by immersion and locale, each with a straight underline beneath it. The two segments exclude the l’ and are distinct from the crossing main-text strokes. H omits the phrase.','16',kind='omission',error='omissions',consequential=True)
add('Third margin, target of the map',r'\widehat M_{\underline G\'}',r'M_{\underline{G}\'}',r'\unsure{M_{\underline G\'}|\widehat M_{\underline G\'}}','The target M has no independently separable two-arm roof. The upper mark meets the descending stroke of par on the previous margin line. Bare M is preferred from the visible contour, while a hat remains possible; the expected ambient object does not settle the stroke. C supplies a hat and H gives a bare M, so neither alternative is declared disproved.','16',confidence='low',against_C=True,against_H=False,kind='misread symbol or index',error='symbols and indices',consequential=True)
add('Third margin, group-action wording and order',r'et faire opérer $\Gamma^!_{\underline G,\underline G\'}$ dessus',r'\uncertain{dessus} $\Gamma^{!}_{\underline{G},\underline{G}\'}$',r'et faire opérer $\Gamma^!_{\underline G,G\'}$ dessus','The words et faire opérer follow the map and its comma; faire has a tall f and dotted i, and opérer has its rounded start and descending p despite crossing main-text strokes. The Gamma formula comes next and dessus follows it, with a final comma. H omits the action words and puts dessus before the group. The local missing second underline is reported separately.','16',kind='omission',marked=True,error='omissions',consequential=True)
add('Third margin, second G-prime in Gamma index',r'\Gamma^!_{\underline G,\underline G\'}',r'\Gamma^{!}_{\underline{G},\underline{G}\'}',r'\Gamma^!_{\underline G,G\'}','The first G has a short independent bar beneath it; the second G-prime has only its letter body and raised prime, with no underline. The final M formula on the next margin line has two clearly separate bars, providing a local contrast.','16',against_C=True,kind='misread symbol or index',error='symbols and indices',consequential=True)
add('M1073, third margin connective',r'\unsure{et ce sera}',r'\ill{}',r'\unsure{et ce sera}','The reduced groups are compatible with et ce sera, but a long crossing line through the later letters prevents complete separation. This remains an unresolved C reading, not a complete decipherment of H’s illegible remainder.','16',confidence='low',kind=r'readable ink left as \ill{}',marked=True,error='readable ink left as illegible')
add('Third margin, final named germ',r'$M_{\underline G,\underline G\'}$','',r'$M_{\underline G,\underline G\'}$','The final margin line contains an M followed by two G indices separated by a comma. Each G has its own clear underline, and the second has a raised prime. H’s marginal transcription ends in an illegible placeholder without this formula.','16',kind='omission',marked=True,error='omissions',consequential=True)
add('End of third margin','.','','','After the final M formula and its prime there is no independent terminal point. The nearby strokes belong to the (99) display label and other writing. C’s final period is not retained.','16',against_C=True,against_H=False,kind='text not on the page',error='text not on page')
add('Pencil foliation',r'\margin{77}','',r'\margin{77}','The pale lower-center pencil group has two tall 7 strokes, each with a top bar and a separate crossing stroke. It is distinct from the ink display label (99).','17',kind='omission',error='omissions')

# Apostrophes in TeX are literal prime characters, not backslash escapes.
def fix_primes(value):
    if isinstance(value,str): return value.replace("\\'", "'")
    if isinstance(value,list): return [fix_primes(v) for v in value]
    if isinstance(value,dict): return {k:fix_primes(v) for k,v in value.items()}
    return value
changes=fix_primes(changes)

inventory=[]
def item(kind,where,words,hand='his hand'):
    inventory.append(dict(scan=78,sheet_kind='text',hand=hand,element=f'{len(inventory)+1:02d}',kind=kind,position=where,first_words_or_objects=words,transcribed='yes'))
item('text','Top center','38')
item('text','First three body baselines','Soit donc ... sous-jacent à G')
item('insertion','Above gap after ens.','C, with connector to the baseline')
item('display','First display','(96), underlined G-prime = underlined G / C, terminal point')
item('text','Above canonical diagram','On a alors un ... morphismes canoniques')
item('insertion','Above morphismes; connector before that word','diagramme de')
item('diagram','Upper middle, numbered (97)','Four-node draft with canceled upper/right portion; live left hook has no lower head')
item('deletion','Above upper-left M in (97)','Doubtful angular roof')
item('deletion','Upper and right paths of (97)','Horizontal arrow, doubtful hatted upper-right M object, hooked downward arrow')
item('margin note','First oblique left note, two baselines','déployer la déf. de Gamma! ... !')
item('text','Subgroup-definition paragraph','Si on désigne ... se factorise ... immersion de multiplicités')
item('deletion','After doubtful flèche','verticale, tentative under strike')
item('insertion','Above canceled verticale','horizontale')
item('drawing','Directly below de before (97)','Small overworked interlinear trace; no reliable letter or definite cancellation state')
item('deletion','Beginning of immersion line','donc, tentative under thick strike')
item('insertion','Above canceled donc','une; no separately recoverable en')
item('diagram','Below subgroup paragraph','(98): hooked map from (M-hat_G,Gamma!) to M-hat_G-prime')
item('margin note','Second oblique left note, four baselines','Ce ne sont peut-être que des immersions locales ... à vérifier...')
item('text','Germ definitions, four prose baselines','Je désigne par ... le germe de multiplicité ... inclusion induite')
item('diagram','Bottom display','(99); both Gamma indices bare, M indices underlined')
item('margin note','Third oblique left note, seven baselines','Il vaut mieux considérer ... final M_{underlined G,underlined G-prime}')
item('margin note','Lower center, pencil','77',hand='pencil foliation; hand not established')

doubts=[
 dict(place='Canceled upper-left roof in (97)',reading=r'\deleted{\unsure{\wedge}}',alternatives='An angular roof is plausible beneath the crosswork.',confidence='low',reason='Multiple strokes cover the original mark. This C doubt is unindexed in MARKS.tsv and is not resolved.'),
 dict(place='Canceled upper-right object in (97)',reading=r'\deleted{\unsure{\widehat M_{\underline G\'}}}',alternatives='The same M object with no hat remains possible.',confidence='low',reason='The letter body, index and prime can be followed, but the roof merges with a cancellation zigzag. H names the object without a hat.'),
 dict(place='M1072',reading=r'\unsure{flèche}',alternatives='flèche remains tentative',confidence='low',reason='The accent and reduced strokes support the preferred word, but letter bodies meet compressed or neighboring ink.'),
 dict(place='Canceled adjective',reading=r'\deleted{\unsure{verticale}}',alternatives='verticale remains tentative under cancellation',confidence='low',reason='Two horizontal strike strokes conceal central letters. Unindexed C doubt retained.'),
 dict(place='Interlinear trace below de (97)',reading=trace,alternatives='Overworked graphical trace, possibly a canceled attempt; no letter assigned.',confidence='low',reason='The crossing strokes do not recover en or another character. The shape and its physical location are retained without a definite verbal or cancellation interpretation.'),
 dict(place='Canceled donc',reading=r'\deleted{\unsure{donc}}',alternatives='donc or partly unreadable canceled letters',confidence='low',reason='The d loop survives, but the thick strike buries the middle and ending. This is an added certainty-only doubt relative to C.'),
 dict(place='Third margin map target',reading=r'\unsure{M_{\underline G\'}|\widehat M_{\underline G\'}}',alternatives='Bare M preferred; hatted M possible.',confidence='low',reason='The possible upper mark meets the preceding par-descender; no independent two-arm roof separates. Mathematical expectation does not settle it.'),
 dict(place='M1073',reading=r'\unsure{et ce sera}',alternatives='et ce sera remains tentative',confidence='low',reason='A long crossing main-text stroke traverses the reduced letter groups. The final named M formula is separately readable.'),
]
doubts=fix_primes(doubts)

notes=[
 'The manuscript takes an MD-graph quotient by an edge set C and writes underlined G-prime = underlined G/C as (96), followed by a point. The number is transcribed as written. The editorial statement in H about a prior use of (96) was not treated as source ink or independently checked against another page.',
 'The manuscript presents a canonical diagram, defines Gamma! using automorphisms preserving C and inducing the identity on the quotient, and claims a factorization through the displayed immersion (98). This is a source assertion; no proof of the factorization or immersion property was performed.',
 'The second margin explicitly questions whether these are only local immersions and asks for verification. The third recommends taking the germ defined by a local immersion and then making the group act on it. These are the author’s reservations and proposed reformulation; the reader has not resolved them.',
 'The main text names hatted and unhatted germs from inclusions (98) and (99). The group indices in (99) are both bare, while adjacent M indices remain underlined; in the third margin only the first Gamma index has an underline. These local omissions are preserved without deciding whether they are intended notational distinctions or slips.',
 'The left vertical trace in (97) has a top hook but no lower arrowhead. The canceled right vertical trace has both a hook and a downward head. Direct TikZ within diagram{} preserves these unequal paths and the right cancellation; no completion of the live left arrow is supplied. The upper roofs remain doubtful under the strikes.',
 'The small overworked mark below de before (97) is preserved as a doubtful graphical trace at that location. Its letter content and cancellation state cannot be recovered. The raised group above canceled donc is one continuous une-like word; there is no independently recoverable en. Both witnesses supply en. Although en would make syntactic sense, that consideration is not used to invent its letters or read them into the trace.',
 'The first margin’s déployer is resolved from the single p, tall l and long y-descender. The other indexed doubts, flèche and et ce sera, remain open. Verticale, donc and the canceled roofs remain uncertain under crossing strokes. The third-margin target has a bare/hat alternative, bare first, because par’s descender prevents separating an independent roof. Its final formula has no separate terminal period.',
 'Count: 38 physical writing units were read: 14 ordinary prose baselines, four complete mathematical display/diagram units, four separate interlinear insertion levels, 13 oblique marginal baselines (2 + 4 + 7), the authorial heading, the pencil foliation, and one independent overworked interlinear trace. Canceled words are counted with their associated prose baseline. All labels and paths inside each mathematical unit were read.',
 'The full scan and each existing native half were viewed once. Twenty PNG crops were saved and read: 17 initial crops and three completion crops for the clipped second Gamma exclamation stem, the clipped word induite, and the previously incomplete une/donc placement region. The latter two were undecided until complete evidence was available. Saved crops were reused only within the same first pass. No OCR, research, TeX compilation, or second reading was undertaken.',
 'The two bars of the repetition sign in lui-= are retained literally, and autom, ens. and déf. remain abbreviated. All three marginal notes remain marginal; the long main underline covers germe de multiplicité, while the second margin underlines only locales and the third underlines immersion locale. The author’s 38 and separate pencil 77 are represented with mspage{} and margin{}, respectively.',
 'Whole diagrams and all formulas with doubts are reproduced as exact TeX in the blind boxes, including the small graphical trace. The boxed paired Gamma formulas include both complete exclamation stems and dots. The (99) blind box extends above its initial crop to retain the entire right-hand roof. Completion crop 19 supplies the full word induite, and crop 20 supplies the whole raised une plus canceled donc.'
]

second=[]
def blind(kind,coords,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
blind('handwritten number',boxes['01'],r'\mspage{38}')
blind('insertion',boxes['02'],r"ens. \inserted{$C$} d'arêtes")
blind('handwritten number',boxes['03'],formula96)
blind('insertion',[620,475,1170,592],r'un \inserted{diagramme de} morphismes')
blind('doubtful formula',boxes['05'],pd[0])
blind('margin note',boxes['06'],pm[0])
blind('word disagreement',[269,865,1575,1040],r"Si on désigne par $\Gamma^!_{\underline G,C}$ ou $\Gamma^!_{\underline G,\underline G'}$ le")
blind('word disagreement',boxes['08'],r'autom qui transforment $C$ en lui-$=$,')
blind('struck passage',boxes['09'],r'la \unsure{flèche} \deleted{\unsure{verticale}} \inserted{horizontale}')
blind('non-high-confidence change',[1002,1385,1670,1535],trace+' (97) se factorise')
blind('struck passage',[470,1510,1670,1635],r'\deleted{\unsure{donc}} \inserted{une} immersion de multiplicités')
blind('handwritten number',boxes['11'],pd[1])
blind('margin note',boxes['12'],pm[1])
blind('word disagreement',[290,1749,1625,2045],r"Je désigne par $\widehat M_{\underline G,\underline G'}$ le \uline{germe de multiplicité} défini par l'inclusion (98),")
blind('word disagreement',boxes['19'],'induite')
blind('handwritten number',[248,2180,1290,2342],pd[2])
blind('margin note',boxes['16'],pm[2])
blind('margin note',boxes['17'],pm[3])

date=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
events=[]
for n,outcome in [
 (1,'Recorded the quotient notation and written display label. No independent graph-theoretic check or cross-page numbering audit was performed.'),
 (2,'Carried the subgroup definition and factorization/immersion assertion as source mathematics. No proof, computation, or formal verification was performed.'),
 (3,'Recorded the author’s local-immersion reservation and proposed group-action reformulation. The reader did not resolve the issue raised by the margin notes.'),
 (4,'Recorded the named germs and the locally missing underlines. Visual comparison of strokes is not a mathematical recheck of the definitions or inclusions.')]:
    events.append(dict(statement_id=f'147-078-N{n}',date=date,who='reader_a; GPT-6 Astra Pro; inherited reasoning effort not separately exposed',type='carried as background without fault found',outcome=outcome))

report=dict(
 scan=78,reader='reader_a',physical_lines_read=38,changes=changes,
 decisions=[
  dict(id='M1071',cote=147,scan=78,decision='first',reading='déployer',ink='One p-descender, a tall l, then the long y-descender and reduced er are distinct. There is no second p sequence for développer. The complete margin phrase, group formula and terminal exclamation were read.',crop='147_scan078_place06.png and (34,863,438,1225), rotated -38 degrees',confidence='high'),
  dict(id='M1072',cote=147,scan=78,decision='undecided',reading=r'\unsure{flèche}',ink='The detached accent and reduced rising/returning strokes support flèche, but the compressed letter bodies and neighboring ink do not permit complete separation.',crop='147_scan078_place09.png and (285,1360,1000,1518)',confidence='low'),
  dict(id='M1073',cote=147,scan=78,decision='undecided',reading=r'\unsure{et ce sera}',ink='The short groups are compatible with et ce sera; a long crossing line covers part of the later letters. The adjacent final M formula remains separately legible.',crop='147_scan078_place16.png and (16,1850,655,2341), rotated -38 degrees',confidence='low')
 ],inventory=inventory,doubts=doubts,notes=notes,check_events=events,
 notation=[
  dict(sign=r'\Gamma^!_{G,G\'}',reading='Both Gamma indices bare in (99).',evidence='Neither index has a separate horizontal bar, unlike the adjacent M indices.',scope='Display (99) only; earlier underlined Gamma indices stay underlined.'),
  dict(sign=r'\Gamma^!_{\underline G,G\'}',reading='Only the first Gamma index underlined in the third margin.',evidence='A short bar occurs under the first G and none under the second; the final M has both bars.',scope='Third oblique margin on scan 078 only.'),
  dict(sign='Top hook with blunt lower end',reading='Uncompleted live vertical trace in (97), reproduced without a lower head.',evidence='One curved upper hook and a plain lower tip; canceled right path instead has two lower arrowhead arms.',scope='Two vertical traces in (97), each checked independently.'),
  dict(sign=r'lui-$=$',reading='Literal repetition sign, expansion même in abbreviation list only.',evidence='Hyphen followed by the two-bar sign, after dotted lui.',scope='Automorphism condition on this page.')
 ],
 hand_log=[
  dict(habit='A small y-descender distinguishes déployer from développer.',pages=[78],all_occurrences='The one occurrence in the first oblique margin was read with its whole phrase.',witness_misreadings='C retained déployer/développer doubt; H gave diptyque. The crop supports déployer.'),
  dict(habit='Oblique marginal writing crosses main text without necessarily canceling it.',pages=[78],all_occurrences='Checked the déf.-descender near Si, the margin near la flèche, and all crossings in the final margin.',witness_misreadings='H supplies a canceled placeholder before Si and misreads several phrases near crossings. Flèche, et ce sera and the margin target roof remain doubtful where separation fails.'),
  dict(habit='Reduced ou may appear as a small dot-like group followed by a low u stroke.',pages=[78],all_occurrences='The single ou between the two group names was inspected in the complete paired-formula crop.',witness_misreadings='H gives an equals sign; the two marks occupy one baseline rather than two parallel bars.'),
  dict(habit='Underlines are locally omitted, even within repeated Gamma notation.',pages=[78],all_occurrences='All Gamma and M indices in the main prose, displays and three margins were inspected separately.',witness_misreadings='Both witnesses supplied two missing bars in (99) and one missing bar in the last margin. No global normalization was made.')
 ],
 abbreviations=[dict(written='ens.',expansion='ensemble'),dict(written='autom',expansion='automorphismes'),dict(written='déf.',expansion='définition'),dict(written='=',expansion='même')],
 second_boxes=second,
 unresolved=[
  'The canceled roofs in (97) remain doubtful under crossing strokes.',
  'M1072 flèche and canceled verticale remain uncertain.',
  'The interlinear trace below de before (97) has no recoverable character or definite cancellation state; it is preserved graphically.',
  'Canceled donc is partly covered by its strike.',
  'The third-margin map target remains bare/hat, bare first.',
  'M1073 et ce sera remains uncertain beneath a crossing line.'
 ],
 witness_comparison='C preserves most prose, abbreviations, margin wording and correction states much better than H. H’s prose drops the C-stability condition, expands autom, and replaces or omits several margin phrases. Both witnesses complete the live left arrow in (97), supply an unsupported separate en, omit the small interlinear trace and colon after (98), and normalize locally absent Gamma underlines. H’s bare target M in the third margin is preferred but remains an open bare/hat reading against C. Tentative canceled words and unresolved roof/word readings remain explicitly doubtful.'
)
report=fix_primes(report)
(HERE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'against_C':sum(c['against_C'] for c in changes),'against_H':sum(c['against_H'] for c in changes),'inventory':len(inventory),'doubts':len(doubts),'second_boxes':len(second),'crop_images':len(boxes),'physical_lines_read':38},indent=2))
