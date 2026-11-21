from edition.scripts.root_audit import Audit

a=Audit(126)
a.keep('B03','The third initial has two rising strokes and an inward diagonal like M, and no independent opening parenthesis can be isolated before the following d. The alternative compressed P-plus-parenthesis remains possible. The first reading correctly keeps the initial and delimiter as one unresolved unit.')
old=r"\unsure{d'|q'}";new=r"\unsure{q'|d'}"
f=a.comparison['B04']['first'].replace(old,new)
a.change('B04',f,'The new middle index has an oval head and a long right descender returning upward at its foot, unlike the upright ascenders of the adjacent new d indices. This favors q-prime visually. A descending d form occurs elsewhere, so d-prime remains an explicit alternative. The three old parenthesized d arguments and their prime counts survive the strikes.')
a.replace(old,new)
a.update_row(3,'B04',final=r"D_{\inserted{\unsure{q'|d'}}}\deleted{(d')}",confidence='medium')
a.doubt('Middle replacement index below D',r"\inserted{\unsure{q'|d'}}",'The oval head and hooked right descender favor q-prime graphically; an unusually descending d-prime remains possible. No index is normalized from the surrounding diagram.','medium',replace_place='Middle replacement index below D')
a.keep('B05','There are four objects and three descending edges with visible tips. The lower indices are d, d-prime and d-double-prime, and the detached dark point lies at the lower-right level. The difference is the encoding of that point and diagram spacing.')
a.keep('B06','The final letter of Prenant rises into an angular t with a short crossing, rather than ending in a low s. The next word is de and the two horizontal strokes form an equals sign; the first literal abbreviation is retained.')
a.keep('B07','The second fan has four objects and three headed descending edges. Its lower pairs are d,d-prime; d-prime,d-double-prime; and d,d-double-prime. The two readings differ only in spacing options.')
a.keep('B08','The word before the disputed noun has an extended terminal s turn, supporting des. The final e/s joins of types remain compressed, so the existing types|type alternative is retained. The three references and transitivités are legible.')
old=r"T(d,d',d'')_{d'}\arrow[r]"
cap=r'\arrow[r,no head,to path={(\tikztostart.east)--([xshift=-2pt]\tikztotarget.west)--++(0,-.045)--++(0,.09)\tikztonodes}]'
new=r"T(d,d',d'')_{d'}"+cap
f=a.comparison['B09']['first'].replace(old,new)
a.change('B09',f,'The system has nine objects, three long curved headed edges, five short shafts with downward terminal turns, and a top-row middle-to-last shaft ending in a transverse cap. That last cap has no complete pair of converging barbs, so the previously supplied full arrowhead is replaced by its observed geometry. No vertical edges are present; the left brace, label (202), indices and final point are retained.')
a.replace(old,new)
a.update_row(9,'B09',final=f)
a.add_row('B09','System (202), T middle-to-last connector',r'\arrow[r]',r'\arrow[r]',cap,'medium','diagram','full head supplied for terminal cap',True,True,True)
a.doubt('System (202), T middle-to-last connector',cap,'The terminal is a short transverse cap; reduced arrow intention versus pen finish is unresolved. Its geometry is drawn without a full head.','medium')
a.keep('B10','The second letter carries a clear circumflex, followed directly by short r/e joins and the ment ending. There is no additional i dot or extended rieusement sequence. Sûrement is retained.')
f=r'\unsure{:|à} \deleted{toute la force de}'
a.change('B11',f,'The first mark consists of two detached strokes, an oblique upper tick and a filled lower oval with no separate a exit. Colon is therefore the leading graphical reading, while à remains possible. Beneath the strike, the final small return after the tall t supports toute, followed by readable la force de.')
a.replace(a.comparison['B11']['first'],f)
a.update_row(11,'B11',final=r'\unsure{:|à}',confidence='medium')
a.doubt('After appel',r'\unsure{:|à}','Two detached marks favor colon; an accent above an extremely compressed a remains possible.','medium',replace_place='After appel')
f=r"l'hypothèse ``\unsure{croisements|croisement}"
a.change('B12',f,'Hypothèse and the two opening quote strokes are clear. At the end of croisements the tall t and its horizontal exit meet the scan edge; a final separate s cannot be secured. Plural remains the first candidate, with singular retained as the blind alternative.')
a.replace(a.comparison['B12']['first'],f)
a.add_row('B12','Ending of the first quoted word in the final sentence','croisements','croisements',r'\unsure{croisements|croisement}','medium','word','terminal letter not separable',True,True)
a.doubt('Ending of the first quoted word in the final sentence',r'\unsure{croisements|croisement}','The final t exit is visible near the edge, but a separate terminal s is not securely distinguishable.','medium')
a.keep('B13','The abbreviation after dans consists of two baseline tall strokes; neither a raised t nor a separate e is visible. The paired closing quotes, sa force, three terminal dots and closing parenthesis are retained.')
for e in a.report['inventory']:
 e['first_words_or_objects']=e['first_words_or_objects'].replace(r"\unsure{d'|q'}",r"\unsure{q'|d'}").replace(old,new)
a.report['unresolved']=[f"{d['place']}: {d['reading']} — {d['alternatives']}" for d in a.report['doubts']]
a.note('Blind audit: all 11 differing boxes were inspected. The middle inserted index now leads with q-prime while retaining d-prime; the top-row second short connector in (202) is drawn with its visible transverse cap; colon leads the unresolved punctuation after appel; and the quoted word retains croisements|croisement. The M/no-separate-parenthesis ambiguity, two fans, literal de =, surely accented sûrement, and tt remain as written.')
a.finish()
