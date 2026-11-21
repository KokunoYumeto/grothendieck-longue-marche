from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan016');S=A.c
ret={
'B02':'The old relation has a curved right boundary and short lower return, consistent with superset; no independent shaft and head establish an arrow. The cancelled prose remains only a doubtful candidate. The raised T, un vois., cancelled tub., and live conique absolu de Y occupy a separate replacement line.',
'B04':'The initial P of Pour is retraced and has a small raised remnant, already represented by the doubt. No separate superscript word is recoverable. The crossed formula remains a low-confidence lambda/T-prime candidate. The brace ends above the returned cancelled tubulaire and live cônique continuation.',
'B05':'After On aura, the long word begins with n and accented e, followed by the low joins of nécessairement; no early d ascender supports évidemment. The first dotted T-prime is overworked and remains doubtful. Both intersections and the final semicolon are distinct.',
'B06':'The old line reads Si, the indexed T-family and est une famille beneath a strike. The raised replacement has la donnée de T-prime équivaut à, including the final à body at the right. The second reading omits that clipped last word rather than identifying contrary ink.',
'B07':'The first variable after the second sous-espace has a flat roof and short stem, favoring T-prime over Y-prime; the following Y has a distinct fork. The first T-dot clause has no separate comma before et. A comma does follow the final et. The source oddity and existing variable alternative remain.',
'B09':'In the rotated margin the opening is ces, followed by T-prime, correspondent, donc, aux and fermés. The tall f and accented ending of fermés remain separable. The second reading’s car and second sous-espace are not supported by those letter bodies.',
'B10':'The relation between T and Y has a rounded right-hand curve, supporting superset, rather than two straight rays of a greater-than sign. The last sous- continues as espaces in the next physical row; this line division does not alter the joined word.',
'B11':'Espaces completes the preceding sous-. Fermés is raised above that baseline with an attachment curve before T_i, hence an insertion. The final line has sont côniques pour cette structure, with no changed wording.',
'B12':'The initial of partie has a long p descender with dark retraced upper loops. The uncertainty concerns that initial only; the second reading’s clean p does not remove the visible overwriting. No independent cancelled whole word is recoverable.',
'B16':'The mark above T is a small angular filled dot of the same local form as other dotted T signs, not a broad roof accent. The terminal iso has blank paper after its final o and no supplied punctuation.',
'B19':'The live opening contains the low m/o, looped d and tall f of modifier. Sans doute remains compressed and uncertain, but the independent condition/nouvelle expansion has no separable matching word bodies. Définition des and voisinages côniques are visible; the last tall t and three detached dots support strict with the existing plural alternative.',
'B20':'The isolated stroke has no arrowhead or internal joints. Its apparent horizontal orientation is caused by crop rotation; in the original page it leans slightly right downward. The existing one-segment TikZ rendering preserves that geometry more closely than a perfectly vertical typeset rule.'}
e1='The upper part of the folio digit is compressed and near-vertical; its lower rounded body favors 3, but a 5 cannot be excluded securely. The separate closing parenthesis remains certain. The existing correction for that parenthesis remains, with a new digit doubt only.'
o1=r'\mspage{3)}';n1=r'\mspage{\unsure{3|5})}'
A.replace(o1,n1);A.change('P01a',final=n1,evidence=e1,confidence='medium')
A.inventory('E01',first_words_or_objects='3/5, preferred 3, followed by closing parenthesis')
A.doubt('P01 author digit',r'\unsure{3|5}','3 | 5','The upper portion is compressed; the rounded lower body favors 3 without fixing the upper stroke.','medium')
e3='A low e/n continuation is visible between the dotted i and the terminal tall t, favoring Soient. The compressed joins still allow Soit, now secondary. The lowered epsilon-like group belongs to T-prime and is not a distinct f under the inclusion; its uncertain cancellation state remains.'
o3=r'\unsure{Soit|Soient}';n3=r'\unsure{Soient|Soit}'
A.replace(o3,n3);A.change('P03a',final=n3,evidence=e3,against_c=True,against_h=False,confidence='medium')
A.update('doubts','place','P03 opening verb',reading=n3,alternatives='Soient | Soit',reason='The low joins before t favor an e/n sequence, although their compression leaves Soit possible.')
o8=r"\unsure{\dot T'_\lambda|\dot T'\deleted{_\lambda}}"
n8=r"\dot T'\unsure{\lambda|\deleted{\lambda}|\ell|\}}"
e8='The wider original crop shows on a above the formula. The group after dotted T-prime extends through the normal letter height, with a high pointed loop and lower returning stroke; it is not securely a lowered index. Lambda is retained as a tentative body, with cancelled lambda, ell and closing-brace outlines left explicit. The separate raised unreadable mark belongs above the double-stem I. The connector has only a short upturned tip, so its existing headless/arrow uncertainty remains.'
A.replace(o8,n8);A.change('P08b',final=A.get('changes','id','P08b')['final'].replace(o8,n8),evidence=e8,confidence='low')
A.inventory('E16',first_words_or_objects='full-height lambda/ell/closing-brace-like group after dotted T-prime; live/deleted state unresolved')
A.update('doubts','place','P08 lowered lambda-like group',place='P08 full-height looped group',reading=n8,alternatives='live lambda | cancelled lambda | ell | closing brace',reason='The looped body occupies normal letter height rather than a secure subscript position; crossings prevent a unique letter or cancellation state.',confidence='low')
o15=r"X'{}^*";n15=r"X'{}^{\unsure{*|\mathrm r}}"
e15='The dotted T and open circle over the later T remain distinct. The raised sign on the first X-prime is compact and forked, less clearly multipointed than the next X-star. Star remains preferred with an r-like alternative. The two horizontal strokes after au are the written equals abbreviation, not the word même.'
A.replace(o15,n15)
A.doubt('P14 raised sign on X-prime',r'\unsure{*|\mathrm r}','star | r','This compact raised fork does not show all arms as clearly as the adjacent X-star.','medium')
A.inventory('E20',first_words_or_objects='Soit T … compatible … strictement compatible with true call star … X-prime raised star/r … un iso')
o17=r"\unsure{Définir la notion pour $X'$}"
n17=r"\unsure{Définir la notion pour $X'$|dire \illegible{1} compatible avec $X'$}"
e17='Repeated zigzag cancellation crosses almost the entire first marginal note. The final X-prime is visible; initial tall and looped members and the intervening short bodies do not securely separate the inherited Définir la notion pour candidate from the independent dire … compatible avec candidate. Both are kept under the same certain deletion, without turning the incomplete word sequence into secure text.'
A.replace(o17,n17);A.change('P16a',final=A.get('changes','id','P16a')['final'].replace(o17,n17),evidence=e17)
A.update('doubts','place','P16 cancelled note',reading=r'\deleted{'+n17+'}',alternatives='Définir la notion pour X-prime | dire [one unreadable word] compatible avec X-prime',reason='The repeated zigzag covers most internal joins; only partial letter bodies and the final X-prime survive securely.')
A.inventory('E22',first_words_or_objects='cancelled doubtful Définir la notion pour X-prime / dire … compatible avec X-prime')
o18=r'\unsure{aussi dire}';n18=r'\unsure{aussi dire|transversal}'
e18='A separate star and two underlines are visible. Broad zigzag strokes cross both word bodies, establishing cancellation independently of the underlines. The first body remains too obscured to choose securely between aussi dire and transversal; the earlier candidate remains preferred. The second short group permits strict; no separate non prefix can be isolated from the crossing strokes.'
A.replace(o18,n18);A.change('P17a',final=A.get('changes','id','P17a')['final'].replace(o18,n18),evidence=e18)
A.update('doubts','place','P17 first cancelled underlined group',reading=r'\uline{'+n18+'}',alternatives='aussi dire | transversal',reason='The surviving loops and dotted/tall members are interrupted by repeated zigzag strikes, leaving both outlines plausible.')
A.inventory('E24',first_words_or_objects='starred, cancelled, two underlined groups: doubtful aussi dire/transversal; strict')
N=A.get('notes','id','N08')['text'].replace('The epsilon- and lambda-like lowered groups have uncertain cancellation state.','The epsilon-like lowered group has uncertain cancellation state. In the image formula the following lambda/ell/brace-like group occupies normal letter height; its body and cancellation state remain uncertain.')
A.update('notes','id','N08',text=N)
changes={'B01':(e1,o1,n1),'B03':(e3,o3,n3),'B08':(e8,o8,n8),'B15':(e15,o15,n15),'B17':(e17,o17,n17),'B18':(e18,o18,n18)}
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b in changes:
  e,o,n=changes[b];A.decide(b,e,S[b]['first'].replace(o,n),crop='crops/150_scan016_root_B08_wide.png' if b=='B08' else None)
 else:A.decide(b,ret[b])
Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan016.jpg').crop((280,880,1692,1045)).save(W/'crops/150_scan016_root_B08_wide.png')
A.append('notes',id='N99',text='Independent audit: root personally inspected all 18 nonidentical second-reading boxes, wider original context for the image formula and enlarged marginal crops. Six boxes were revised. The opening verb preference and the full-height placement of the looped formula group change; new alternative-only doubts elsewhere do not create new primary C corrections. All first/second readings remain fixed.')
A.save()
