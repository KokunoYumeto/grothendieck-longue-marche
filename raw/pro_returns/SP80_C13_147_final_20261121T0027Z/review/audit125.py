from edition.scripts.root_audit import Audit

a=Audit(125)
a.keep('B02','The top edge has a full rightward head; both vertical pairs of strokes are equalities with unaccented def written to their right. The lower-left G carries a low d with its own loop. The upper-right extra dark high mark remains compatible with a retraced single prime or a second prime, as already recorded.')
a.keep('B03','The first stroke is a shallow turn, and the next oval and i join are compressed. Both voit and sait remain graphically possible; reversing candidate order would add no certainty. The existing two alternatives are retained.')
a.keep('B04','The horizontal relation is a wave above a straight bar. The brace covers only the first right P term and connects to the right equality; the product at lower left has a dark circled-cross form. The small low stroke after the G under the wedge remains d versus joined exit uncertain. The lower P_d and P_d-prime are kept in their written positions.')
a.keep('B05','The two live replacement lines are separately raised above the two crossed lines: On a des relations de transitivité, then pour les morphismes précédents. In the canceled text the A/u opening, niveau joins, descending groupoïdes and split fondamentaux remain readable; its Pi-P formula is separately visible. The first layout preserves this interleaving.')
a.keep('B06','The live word begins with short r-e joins and a tall l, followed by compressed letters ending at a long f-like descender. This supports the existing relatifs|relatives uncertainty rather than treating the descender as an independent drawing. The separately crossed Pi-P formula remains tentative; after it a is unaccented and no separate la is visible before donnée d\'un triple.')
a.keep('B08','The three T expressions retain identical d,d-prime,d-double-prime arguments and successive lower indices d, d-prime and d-double-prime, with visible separating commas. The left number is retraced but reads (199); the difference is display wrappers.')
old=r"G(d,d',d'')_{d'}"
new=r"G(d.d',d'')_{d'}"
f=a.comparison['B09']['first'].replace(old,new)
a.change('B09',f,'The three G expressions and their successive terminal indices are visible. In the middle expression the first separator, immediately after d, is a small round low point with no descending tail, unlike the following comma and the commas in the other expressions. The literal point is retained instead of harmonizing the tuple.')
a.replace(old,new)
a.add_row('B09','First argument separator in the middle expression of (200)',old,old,new,'high','punctuation','comma substituted for literal point',True,True)
a.keep('B10','The pencil digits read 124, with a curved 2 and open-topped angular 4. The margin macro is the only difference.')
for e in a.report['inventory']:
 e['first_words_or_objects']=e['first_words_or_objects'].replace(old,new)
a.note('Blind audit: all eight differing boxes were inspected. The first separator in the middle expression of (200) was changed from a comma to the visible round point. Existing ambiguities in the terminal primes, product sign, low group index, voit|sait and relatifs|relatives remain explicit. Both replacement lines, canceled prose, and the written a donnée without a supplied article were retained.')
a.finish()
