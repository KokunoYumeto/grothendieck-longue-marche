from edition.scripts.root_audit import Audit

a=Audit(127)
f=r'\deleted{On a envie de définir des \unsure{torseurs|homs}}'
a.change('B01',f,'The opening On a envie de définir des survives the horizontal strike. The next line has one tall loop, a low oval and compressed terminal joins, but the full middle of torseurs is not independently letter-complete. Torseurs remains the leading reading, with the blind homs alternative explicitly retained under cancellation.')
a.replace(a.comparison['B01']['first'],f)
a.update_row(0,'B01',final=f,confidence='low',against_C=True)
a.doubt('Noun in the canceled opening',r'\unsure{torseurs|homs}','The tall initial loop and surviving low joins do not secure all the intervening letters beneath the strike.','low')
a.keep('B02','Both lower d,d-prime pairs, the two high stars, the restriction bar and ouvert de are visible under the separate horizontal cancellation. The second version changes only display and spacing wrappers.')
f=r"\deleted{(quand \unsure{on|\mbox{-\kern.3em-}} fait l'\unsure{hyp}}"
a.change('B03',f,'The opening curve, q descender, following low joins and final tall d support (quand. Fait has a long f loop and the surviving a/i/t strokes, followed by l-prime and an uncertain hyp-like ending. Between quand and fait there are two detached short low strokes; compressed on is possible, but two literal strokes cannot be excluded. No final point or closing parenthesis is supplied.')
a.replace(a.comparison['B03']['first'],f)
a.update_row(1,'B03',final=f,confidence='medium')
a.doubt('Upper canceled parenthetical',f,'The middle on may instead be two short separated strokes. The final hyp group remains compressed under cancellation, without a secure final point.','medium',replace_place='Upper canceled hyp ending')
a.keep('B06','The raised universal quantifier ends with the double-stemmed N and no separate comma. Its insertion and attachment are retained; mathbb braces and thin spacing do not change the reading.')
a.keep('B07','The de is independently raised. In the following word the retraced stroke after déplo descends below the line, favoring y; the possible i layer remains uncertain. The existing y|i alternative records that geometry without imposing spelling.')
a.keep('B09','A crossed old d-like cluster precedes the separate dotted live i. The angle brackets around the raised d and the right-hand lower d+i,d are visible. The difference is the order of subscript and superscript commands.')
a.keep('B10','Four short horizontal strokes remain separated. After them a long p-like stem with a small right arch is followed by separate me joins. There is no letter-complete pour; the first p|je uncertainty is retained without adding a point.')
a.keep('B11','After the p descender the small e loop and n shoulder support dispens rather than dispos. The final compressed continuation does not securely distinguish dispenser from dispense, so the first alternatives remain.')
a.keep('B12','Four separate groups show au, a tall l and descending g in long, the crossed t in et, then au. The strokes do not form analogues. The first au long et au reading is retained.')
a.keep('B13','The initial tall l, low a/r joins and g descender support large, followed by a closing parenthesis and separate avec. There is no independent ce qui sequence. The first reading is retained.')
f=r'les $=$ propriétés --- \unsure{elle|elles}'
a.change('B14',f,'The two equality strokes, propriétés and one following horizontal dash are visible. The pronoun has two tall l loops and a terminal low curl, but that ending does not securely distinguish e from es. Elle remains primary with elles retained; the hyphen count is only the LaTeX encoding of one written dash.')
a.replace(a.comparison['B14']['first'],f)
a.add_row('B14','Pronoun after les = propriétés','elle','elle',r'\unsure{elle|elles}','medium','word','compressed ending',True,True)
a.doubt('Pronoun after les = propriétés',r'\unsure{elle|elles}','Two l loops are clear; the terminal low curl does not secure the final number.','medium')
a.keep('B15','The live capital is an oval crossed by a horizontal bar, supporting Theta rather than G. Its lower d is distinct. The adjacent locally canceled notation remains too densely crossed to resolve beyond the first D(d)/cf alternatives.')
a.keep('B16','The two p descenders of support, est noté, the high star on D_d and the final point are visible. The only difference is braces around the superscript star.')
a.keep('B18','The repeated number (203), both d,d-prime pairs, both stars and the vertical restriction bar survive the horizontal strikes. The two readings differ only in display wrappers and spacing.')
a.keep('B19','The angular Delta and both lower prime pairs in the right-column comment are clear. At the far right the returning curve could close the parenthetical or belong to the attachment stroke; the first uncertain closing parenthesis is therefore retained. The surrounding margin wrapper is already present in the page.')
a.keep('B20','A separate opening curve precedes image, whose deep g loop survives below the cancellation. Inverse de remains readable. The final capital has angular rising and basal strokes, favoring Delta, while the strike leaves Theta/D possible. Only one final closing curve is visible, so no additional prose parenthesis is supplied.')
a.keep('B21','The old verb has p/o and a small crossed s/e sequence, favoring posera over pourra; its final joins remain incomplete, retaining posera|pose. The raised replacement begins with a low v rather than a p descender. The local canceled des remains identifiable before morphismes, independently of the broad oblique cancellation.')
a.keep('B22','The formula has a four-sided rectangular frame and a separate full rightward arrowhead. A low comma separates the two arrow-label indices, and the second d has one prime. The curled label intersects a descending stroke above, retaining gamma|r; the short target low upright merges with the oblique cancellation, retaining uncertain1. These are not resolved by expected notation.')
a.keep('B23','The number itself reads (203) and has no local strike through its digits. It labels the boxed formula within the broadly canceled lower passage, so the first deleted scope is retained; the second crop alone does not capture that larger cancellation state.')
a.keep('B25','Both underline strokes begin inside the first word, to the right of the initial h stem, and stop before the closing quotation ticks. The first limited om de générisation span approximates those visible endpoints more closely than underlining the entire hom. The paired quotes and absence of a point after hom are retained.')
for e in a.report['inventory']:
 if e['element']=='E01': e['first_words_or_objects']=a.choices[0]['final']
 if e['element']=='E03': e['first_words_or_objects']=a.comparison['B03']['first'].replace('on',r'\unsure{on|\mbox{-\kern.3em-}}',1)
a.report['unresolved']=[f"{d['place']}: {d['reading']} — {d['alternatives']}" for d in a.report['doubts']]
a.note('Blind audit: all20 differing boxes were inspected. The canceled opening noun now retains torseurs|homs; the two short strokes between quand and fait retain on versus two strokes; the pronoun after propriétés retains elle|elles. The literal equality sign, four separated dashes, raised insertions, distinct cancellation layers, two occurrences of (203), boxed arrow, partial double underline, and unresolved symbol/index shapes remain supported by the images.')
a.finish()
