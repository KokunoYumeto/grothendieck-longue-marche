from pathlib import Path
import json
ROOT=Path('/workspace/scratch/f28c4f52d3ec');P='148_scan058'
B=json.loads((ROOT/'proposed'/f'{P}_crop_boxes.json').read_text())
D={'page':P,'reader':'reader_a','lines_read':27,'changes':[],'decisions':[],'implicit_decisions':[],'doubts':[],'inventory':[],'notes':[],'check_events':[],'notation':[],'abbreviations':[],'second_boxes':[]}
def change(place,c,h,final,dc,dh,kind,ek,evidence,crop,confidence='high',marked=False,consequential=False):
 D['changes'].append({'id':f'{P}-{len(D["changes"])+1:02d}','place':place,'c':c,'h':h,'final':final,'diff_c':dc,'diff_h':dh,'kind':kind,'error_kind':ek,'evidence':evidence,'crop':f'crops/{P}_{crop}.png','box':B[crop],'confidence':confidence,'marked_in_h':marked,'consequential':consequential})
change('Upper paragraph, replacement above cancelled edge adjective',r'\deleted{\unsure{ordinaires}} \inserted{liées}',r'\add{liées} \struck{ordinaires}',r'\deleted{\unsure{ordinaires}} \inserted{liées}',False,True,'insertion or placement','Insertions put in the wrong place','liées is raised directly over the cancelled adjective. The old word is retained first and the raised replacement attached to it; its l loop, i and accented e sequence are visible. The old adjective remains uncertain because its interior is buried.','liees')
change('Upper paragraph, cette fois ci','cette fois ci','cette fois-ci','cette fois ci',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','There is a blank between the final s of fois and ci. The separate stroke to the left belongs to the f crossbar, not to a hyphen between the words.','fois_ci')
change('Upper paragraph, quotation marks around both operations',"``gommer''; ``découper''",'« gommer »; « découper »',"``gommer''; ``découper''",False,True,'other','Other','The quotation marks are raised pairs of short strokes, sometimes touching as a small wave. They are not angled guillemets.','quotes')
change('Second paragraph, underline',r'Le \uline{marquage suit}.','Le marquage suit.',r'Le \uline{marquage suit}.',False,True,'other','Other','A separate horizontal rule runs under marquage suit, beginning after Le and ending before the point.','marquage_cancel')
change('First long cancellation, paragraph attachment',r'Le \uline{marquage suit}. \deleted{Ici encore, pour \unsure{un|une} \illegible{1}} Mais il y',r'Le marquage suit. Mais il y \struck{\ill{} \ill{}, par un \ill{}}',r'Le \uline{marquage suit}. \deleted{Ici encore, pour un \illegible{1}} Mais il y',False,True,'insertion or placement','Insertions put in the wrong place','The crossed line starts below the completed Le marquage suit sentence, to the left of the live Mais. It is an abandoned continuation after that sentence, not a clause interrupting Mais il y a.','marquage_cancel')
change('First cancelled line opening','Ici encore,',r'\ill{} \ill{},','Ici encore,',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The initial capital I, small c and i, then the low e/n/c/o/r/e sequence and comma remain visible along the cancellation.','marquage_cancel','high',True)
change('First cancelled line preposition','pour','par','pour',False,True,'misread word','Words','After the p descender is an o/u run before the final short r. The interior is longer than a single a body.','marquage_cancel')
change('Second paragraph, operation adjective','anodine','ordinaire','anodine',False,True,'misread word','Words','The word begins with low a/n then a small o, a looped d ascender, dotted i and the n/e ending. There is no initial or- or final -aire group.','anodine_enC','high',False,True)
change('Second paragraph, raised component words',r'\inserted{en $C$}',r'\add{où $C$}',r'\inserted{en $C$}',False,True,'misread word','Words','The raised first word is a low e followed by n; there is no rounded ou pair or grave accent. The following capital C is open on the right.','anodine_enC','high',False,True)
change('Second paragraph, raised component attachment',r"opération anodine \inserted{en $C$} ---",r"le cas \add{où $C$} d'une opération ordinaire",r"opération anodine \inserted{en $C$} ---",False,True,'insertion or placement','Insertions put in the wrong place','The insertion mark points to the gap after anodine and before the dash. It does not attach after cas on the line above.','anodine_enC','high',False,True)
change('Marked case, live où and cancelled clause order',r"où \deleted{il y a \unsure{bel et bien|tel et un}} \inserted{$C$ est effectivement marqué}",r"où $C$ est effectivement \struck{marqué} \struck{où il y a \ill{}}",r"où \deleted{il y a \unsure{bel et bien|tel et un}} \inserted{$C$ est effectivement marqué}",False,True,'insertion or placement','Insertions put in the wrong place','The initial où is left of and outside the long cancellation. The crossed il y a phrase lies on the lower baseline, and the C est effectivement marqué replacement is raised above it. The low a of il y a falls above Sigma on the next line; it is not a Sigma index.','replacement','high',True,True)
change('Marked case, cancelled tail',r'\deleted{il y a \unsure{bel et bien|tel et un}}',r'\struck{où il y a \ill{}}',r'\deleted{il y a \unsure{bel et bien|tel et un}}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','Some tall and low strokes after il y a are compatible with bel et bien or tel et un, but the rule merges their interior bodies. The inherited alternatives remain doubtful; this is only partial recovery from H\'s illegible group.','replacement','low',True)
change('Marked case, live replacement ending',r'\inserted{$C$ est effectivement marqué}',r'$C$ est effectivement \struck{marqué}',r'\inserted{$C$ est effectivement marqué}',False,True,'deletion state (struck given live or live given struck)','Struck text','marqué occupies the raised replacement baseline. Its body and accent are above the cancellation; only the long q descender intersects the lower strike. The word is live.','replacement','high',False,True)
change('First marked-case formula, empty-set sign',r'C\cap R\ne\varnothing',r'C\cap R\neq\emptyset',r'C\cap R\ne\phi',True,True,'misread symbol or index','Symbols and indices','The final sign has a small oval on a long oblique descending stem, the handwritten phi form used for the empty set. The entire C-cap-R non-equality was read with it.','replacement','high',False,True)
change('After first marked-case formula',r'$C\cap R\ne\varnothing$ i.e.',r'$C\cap R\neq\emptyset$, i.e.',r'$C\cap R\ne\phi$ i.e.',False,True,'text not on the page','Text that is not on the page','No comma follows the final phi before the next i.e. starts on the following physical line. The long final stroke belongs to phi itself.','replacement')
change('After second marked-case formula','qui',r'\ill{}','qui',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The q body and descender are followed by a compact u and short i stroke on the same baseline after the dash.','qui_choses','high',True)
change('Near reversibility qualifier','à peu de choses près','à peu de chose près','à peu de choses près',False,True,'misread word','Words','The final word has a distinct low -es ending after the c/h/o/s sequence and a terminal downward s turn. The plural is retained.','qui_choses')
change('Cancelled closing parenthesis after fini',r'fini, \deleted{)}',r'fini, \ill{}',r'fini, \deleted{)}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The live comma is followed by the large closing curve of a parenthesis, with added looping strokes crossing it. It is cancelled rather than a live closure.','finite_close','high',True)
change('M0746, short parenthetical expression',r'\unsure{en plus|à isom près|ou pas}',r'\ill{}',r'\unsure{en près|en plus}',True,True,'misread word','Words','A faint low first run favours en. The second starts with a long p descender and ends in s; its middle is a short r/è-like group rather than a clear tall l. en près is intentionally retained as an odd possible reading, with en plus as the surviving alternative. The longer à isom près and ou pas are not supported.','enplus','low',True,True)
change('M0747, verb after peut se',r'\unsure{réverser|renverser|inverser}','« inverser »',r'\unsure{réverser|inverser}',False,True,'misread word','Words','The first group can be r plus accented e or dotted i followed by n; the following v/e/r/s/e/r sequence is clearer. No separate extra n supports renverser, but the dot-versus-accent question prevents a final choice.','reverse','medium',False,True)
change('Quotation marks around the doubtful verb','absent','« inverser »','absent',False,True,'text not on the page','Text that is not on the page','No opening or closing quotation strokes surround the verb. The only raised mark is over its initial letter group, and the following curved stroke is the sentence comma.','reverse')
change('After à l’aide','du','des','du',False,True,'misread word','Words','The d has a small lower loop and tall looped ascender, followed by one flattened u ending. There is no separate e/s sequence.','aide_du')
change('Object of à l’aide',r'produit de cette opération',r'\ill{} \ill{})',r'produit de cette opération',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','produit has p and d stems, dotted i and a tall final t; de is separate; cette has paired t strokes; opération has the p descender and -tion ending. No closing parenthesis is written after the phrase.','produit','high',True,True)
change('After final marked/unmarked contrast','marqué. Mais','marqué. Mais','marqué, Mais',True,True,'misread symbol or index','Symbols and indices','After the accented marqué is a thick curved descending comma, not a round point. The following Mais is capitalized as written.','marque_comma')
change('Lower handwritten folio',r'\mspage{57}','absent',r'\mspage{57}',False,True,'omission','Omissions','The 5 has an upper cap and lower bowl; the following 7 has an upper bar, long descending stroke and middle crossbar.','folio57')
# Only supplied MARKS IDs belong here.
def decision(id,choice,reading,evidence,crop,confidence):D['decisions'].append({'id':id,'decision':choice,'reading':reading,'evidence':evidence,'crop':f'crops/{P}_{crop}.png','box':B[crop],'confidence':confidence})
decision('M0746','undecided',r'\unsure{en près|en plus}','The first low run favours en; the next word has p and s, with a short r/è-like middle and no secure tall l. The odd en près is not normalized from grammar. à isom près and ou pas are excluded by the visible length and strokes.','enplus','low')
decision('M0747','undecided',r'\unsure{réverser|inverser}','Initial r-é and i-n remain difficult to distinguish because the raised mark can be an acute or a dot. The following verser sequence is legible; no extra n supports renverser.','reverse','medium')
def imp(id,choice,reading,evidence,crop,confidence):D['implicit_decisions'].append({'id':id,'decision':choice,'reading':reading,'evidence':evidence,'crop':f'crops/{P}_{crop}.png','box':B[crop],'confidence':confidence})
imp('C058-D01','undecided',r'\deleted{\unsure{de}}','A d-like loop/stem and following short body survive beneath heavy overwriting; the second letter is not independently secure.','opening_de','low')
imp('C058-D02','undecided',r'\deleted{\unsure{ordinaires}}','The first low body and tall d-like loop are visible, but most internal letters lie under the long deletion stroke.','liees','low')
imp('C058-D03','first','un','The cancelled word shows distinct u and n low arches, then a gap before the last unreadable group. There is no separate e after the n.','marquage_cancel','high')
imp('C058-D04','undecided',r'\deleted{il y a \unsure{bel et bien|tel et un}}','The il y a sequence is readable, including its unusually low a. The later crossed groups remain insufficiently separate to choose between the inherited alternatives.','replacement','low')
def doubt(place,reading,alternatives,confidence,reason):D['doubts'].append({'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason})
doubt('Heading, cancelled preposition',r'\deleted{\unsure{de}}','de; no secure alternative','low','Overwriting obscures the second letter; no resolution from the witnesses’ agreement.')
doubt('Upper paragraph, cancelled edge adjective',r'\deleted{\unsure{ordinaires}}','ordinaires; no secure alternative','low','The old adjective is mostly under a horizontal strike beneath the raised liées.')
doubt('First long cancelled line, final group',r'\illegible{1}','No legible complete word','low','Only two small upper traces and the cancellation line remain. A lexical reading is physically unrecoverable in the evidence crop.')
doubt('Marked case, cancelled tail',r'\unsure{bel et bien|tel et un}','bel et bien / tel et un','low','The strike merges the internal letter bodies and no fully legible candidate is available.')
doubt('Parenthesis after fini',r'\unsure{en près|en plus}','en près / en plus','low','The first word is faint and the second has a short r/è-like group rather than a secure l. The unusual possible wording is preserved.')
doubt('Verb after peut se',r'\unsure{réverser|inverser}','réverser / inverser','medium','The raised initial mark can be an accent or i dot, and the initial connected group remains ambiguous.')
def inv(kind,position,first):D['inventory'].append({'element':f'E{len(D["inventory"])+1:02d}','sheet_kind':'text','hand':'his hand','kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('text','Top centre','14')
inv('text','Heading and first paragraph','C) Découpage suivant une partie Sigma prime subset Sigma zero')
inv('deletion','Heading after Découpage','de')
inv('insertion','Above partie at the right of the first line','ouv. et f.')
inv('text','Upper paragraph, interpretation in graph terms','cela correspond à une partie A prime de A zero')
inv('deletion','Inside the edge-type parenthesis','ordinaires')
inv('insertion','Above the deleted edge adjective','liées')
inv('text','Rest of first paragraph','mais cette fois ci il ne s’agit pas de gommer ... remplacer par deux arêtes libres')
inv('text','Start of second paragraph','Le marquage suit.')
inv('deletion','Below Le marquage suit and before Mais','Ici encore, pour un [one unreadable word]')
inv('text','Middle paragraph','Mais il y a ici à distinguer entre le cas d’une opération anodine')
inv('insertion','Above the gap after anodine','en C')
inv('deletion','Below marked-case replacement','il y a bel et bien / tel et un')
inv('insertion','Raised above the cancelled il y a clause','C est effectivement marqué')
inv('text','Marked-case formulas and qualifier','i.e. C cap R not equal phi i.e. C subset Sigma plus — qui à peu de choses près')
inv('deletion','After fini comma inside the finite-ambiguity parenthesis','Closing parenthesis')
inv('text','Last five physical lines','en près / en plus ... peut se réverser / inverser ... à l’aide du produit de cette opération')
inv('text','Bottom continuation','C n’est pas marqué, Mais il semble que dans la façon dont nous allons travailler')
inv('text','Lower left folio','57')
D['notes']=[
 {'id':P+'-N01','text':'Item C describes cutting along an open and closed subset Sigma prime of the cutting circles Sigma zero, corresponding to a subset A prime of the linked graph edges A zero. On the graph this cuts an edge at its middle and replaces it by two free edges. The marking is said to follow the operation.'},
 {'id':P+'-N02','text':'The page distinguishes an operation called anodine en C when C is marked, expressed by C intersect R not equal phi and C contained in Sigma plus, from the case in which C is not marked. The two markedness conditions are carried as the author’s stated equivalence; no definition of Sigma plus is reconstructed from other pages.'},
 {'id':P+'-N03','text':'The marked case is described as recoverable up to a finite ambiguity from the result of the operation. The short expression in the parenthesis and the verb remain uncertain: en près/en plus and réverser/inverser. The grammatical oddity of the first candidate is not corrected. No existence or uniqueness proof of the inverse construction is supplied on this page.'},
 {'id':P+'-N04','text':'The raised C est effectivement marqué is live; its q descender crosses the cancelled line below but does not cancel the word. The low a above the Sigma-plus formula is part of the deleted il y a phrase, not a formula decoration.'},
 {'id':P+'-N05','text':'The final marked clause ends with a comma before capital Mais, although both witnesses give a period. The final sentence continues beyond this page and stops here at travailler. Both handwritten folios, 14 at the head and 57 at the foot, are retained.'},
 {'id':P+'-N06','text':'The original and both prepared halves were read once, including every shared witness reading. The physical row count includes inserted/cancelled rows and both handwritten folios. Sixteen first-pass evidence crops were inspected; no second reading, OCR, web consultation, or TeX compilation was performed.'}
]
D['check_events']=[
 {'statement_id':P+'-N01','type':'used and rechecked in this run','outcome':'The stated local graph operation was checked against its own description: one edge cut at an interior point gives two pieces with new free ends, matching the written replacement by two free edges. This is a local combinatorial consistency check, not a proof of a global construction.'},
 {'statement_id':P+'-N02','type':'carried as background without fault found','outcome':'The identification of marked components with the two displayed conditions is transcribed as asserted. The definition of Sigma plus is not present here, so no independent proof of the equivalence was attempted.'},
 {'statement_id':P+'-N03','type':'carried as background without fault found','outcome':'The asserted near reversibility with finite ambiguity is recorded, with the doubtful words left marked. No inverse functor or finite ambiguity set was constructed or proved in this reading.'}
]
D['notation']=[
 {'sign':r'\phi','meaning_or_form':"ϕ : l'ensemble vide; small oval on a long descending oblique stem.",'places':'Marked-case condition C cap R not equal phi.','universality':'One occurrence on this page; checked with the supplied notation habit, not imposed on a different visible shape.','witness_errors':'C uses varnothing and H emptyset; both replace the handwritten phi form.'},
 {'sign':'un','meaning_or_form':'Separate low u/n arches followed by a blank before the next group; no added e loop.','places':'First long cancellation, pour un unreadable word.','universality':'One disputed occurrence here; other ordinary un occurrences were checked directly.','witness_errors':'C leaves un/une doubtful; the crop resolves un. H already has un.'},
 {'sign':'Raised replacement versus cancelled baseline','meaning_or_form':'The cancellation runs through the abandoned lower line; descenders from a live upper replacement may cross it without making the upper word struck.','places':'C est effectivement marqué above il y a ...; low a above the following Sigma.','universality':'The replacement and low a were checked together in one complete clause crop.','witness_errors':'H strikes marqué and relocates the old clause; neither witness supplies a spurious Sigma index.'},
 {'sign':'Initial r-é / i-n','meaning_or_form':'A short connected initial group with one raised mark can resemble r plus accented e or i followed by n.','places':'réverser/inverser after peut se.','universality':'One unresolved occurrence; no general letter substitution rule is asserted.','witness_errors':'C offers three readings; renverser is not supported by an extra n, while H chooses quoted inverser without retaining the uncertainty.'}
]
D['abbreviations']=[{'form':'ouv.','expansion':'ouverte'},{'form':'f.','expansion':'fermée'},{'form':'i.e.','expansion':'id est'},{'form':'ens.','expansion':'ensemble'}]
# One unique rectangle per audit target; a single rectangle can cover multiple required categories.
def audit(kind,box,reading):D['second_boxes'].append({'box':f'B{len(D["second_boxes"])+1:02d}','kind':kind,'x0':box[0],'y0':box[1],'x1':box[2],'y1':box[3],'reading':reading})
audit('handwritten number',B['folio14'],r'\mspage{14}')
audit('struck passage',B['opening_de'],r'\deleted{\unsure{de}}')
audit('insertion',[1367,118,1650,266],r'partie \inserted{ouv. et f.}')
audit('handwritten number',[428,286,680,371],r'$\Sigma\'\subset\Sigma_0$')
D['second_boxes'][-1]['reading']=D['second_boxes'][-1]['reading'].replace("\\'","'")
audit('handwritten number',[941,500,1240,593],r'$A\'$ de $A_0$')
D['second_boxes'][-1]['reading']=D['second_boxes'][-1]['reading'].replace("\\'","'")
audit('insertion',B['liees'],r'\deleted{\unsure{ordinaires}} \inserted{liées}),')
audit('different words',B['fois_ci'],'cette fois ci')
audit('different words',[398,717,1647,944],"de ``gommer'' i.e. de contracter en un point, mais de ``découper'', ce")
audit('struck passage',B['marquage_cancel'],r'Le \uline{marquage suit}. \deleted{Ici encore, pour un \illegible{1}}')
audit('insertion',B['anodine_enC'],r'anodine \inserted{en $C$} ---')
audit('struck passage',B['replacement'],r'où \deleted{il y a \unsure{bel et bien|tel et un}} \inserted{$C$ est effectivement marqué} i.e. $C\cap R\ne\phi$ i.e. $C\subset\Sigma^+$ --- qui à peu de choses')
audit('struck passage',B['finite_close'],r'ens. fini, \deleted{)}')
audit('low-confidence departure',B['enplus'],r'\unsure{en près|en plus})')
audit('different words',B['reverse'],r'peut se \unsure{réverser|inverser},')
audit('different words',B['aide_du'],"à l'aide du")
audit('different words',B['produit'],'produit de cette opération')
audit('different words',B['marque_comma'],'marqué,')
audit('handwritten number',B['folio57'],r'\mspage{57}')
# Metadata and literal-structure verification only; no TeX compilation or image second pass.
required=[line.split('\t')[0] for line in (ROOT/'packets'/P/'MARKS.tsv').read_text().splitlines()[1:] if line]
assert [x['id'] for x in D['decisions']]==required
tex=(ROOT/'proposed'/f'{P}.tex').read_text()
assert tex.count('{')==tex.count('}')
assert len({tuple((z['x0'],z['y0'],z['x1'],z['y1'])) for z in D['second_boxes']})==len(D['second_boxes'])
for row in D['changes']+D['decisions']+D['implicit_decisions']:
 assert (ROOT/'result'/row['crop']).is_file(),row['crop']
macros=[];pos=0
while True:
 a=tex.find('\\unsure{',pos)
 if a<0:break
 j=a+8;depth=1
 while depth:
  if tex[j]=='{':depth+=1
  elif tex[j]=='}':depth-=1
  j+=1
 macros.append(tex[a:j]);pos=j
assert all(any(m in d['reading'] for d in D['doubts']) for m in macros)
(ROOT/'proposed'/f'{P}.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':P,'changes':len(D['changes']),'decisions':len(D['decisions']),'implicit_decisions':len(D['implicit_decisions']),'doubts':len(D['doubts']),'audit_rectangles':len(D['second_boxes']),'duplicate_rectangles':0,'crops':len(B)}))
