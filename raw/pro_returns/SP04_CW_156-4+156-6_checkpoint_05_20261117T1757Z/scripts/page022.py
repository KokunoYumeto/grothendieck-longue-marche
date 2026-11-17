from author import Page
import re
p=Page('156-4',22)
p.replace(r'X_{\unsure{i|{}}}\longmapsto',r'X\longmapsto')
p.replace(r'\unsure{L|\mathcal{L}}','L')
p.replace(r'\unsure{\mathcal P|P}',r'\mathcal P')
p.replace(r'\unsure{sur|sûr}','sur')
p.replace(r'\unsure{x|\alpha}','x')
p.replace(r'\unsure{NB}','NB')
p.replace(r'\unsure{L_X^{\circ}|L_{X_i}^{\circ}}',r'\unsure{L_{X_i}^{\circ}|L_X^{\circ}}')
p.replace(r'\unsure{Contr|Cont}','Cont')
p.replace(r'\unsure{\text{--}|.}',r'\text{.-}')
p.replace(r'\unsure{\varnothing|X}',r'\varnothing')
p.replace(r'\unsure{\overline{\leq}|\nleq|\leq}',r'\overline{\leq}')
p.replace(r'\exists\unsure{i|0}',r'\exists i')
p.replace(r'et les $\unsure{X_i|Y_i}$ forment',r'et les $Y_i$ forment')
# Only the overwritten upper block receives additional index doubts.
cut=p.text.index('% @ definition of open-circle L')
upper=p.text[:cut]
upper=upper.replace('X_j',r'X_{\unsure{j|i}}')
# Avoid nested replacements inside existing X_i|Y_i alternatives.
upper=upper.replace('L_{X_i}',r'L_{X_{\unsure{i|j}}}')
upper=upper.replace(r'x\ll X_i',r'x\ll X_{\unsure{i|j}}')
p.text=upper+p.text[cut:]
p.text=re.sub(r'(?<![A-Za-z])L(?![A-Za-z])',lambda m:r'\mathcal{L}',p.text)
p.change('crossed opening noun','multistrate','multiplicité','multistrate','Tall l/t and str cluster survive the horizontal strike.','top',kind='misread word')
p.change('first map, source index','X_i|X','X_i','X','The heavy X is followed directly by the mapsto bar; no separate subscript appears.','top',dc=True,kind='misread symbol or index',consequential='The displayed map starts with an unsubscripted X as written.')
p.change('first map, image index','L_Xi','L_Xi','L_X(i|j)','Subscript after X is overdrawn with a short descending loop; its letter remains uncertain.','top',dc=True,kind='misread symbol or index',confidence='low')
p.doubt('first map, image index','i|j','Overwritten small index is not securely separable','top',confidence='low')
p.change('first map, P alphabet','calligraphic P|P','fraktur P',r'\mathcal P','Broad angular bowl on straight stem with a short lower return.','top',dc=True,kind='misread symbol or index',confidence='medium')
p.change('monotonicity, spelling','sur|sûr','sûr','sur','Low sur with no detached circumflex above the u.','top',dc=True,kind='abbreviation expanded or spelling modernised')
for place,C,H,final in [
('premise left index','j|i','i','j|i'),('premise right variable','X_i|Y_i','X_j','X_i|Y_i'),
('intermediate refinement, left index','j','omitted','j|i'),('intermediate refinement, right variable','X_i|Y','omitted','X_i|Y'),
('inclusion left index','j','i','j|i'),('inclusion right index','i','j','i|j'),
('cancelled symbol after que','X_j|X′','omitted','X_(j|i)|X′, deleted'),
('strict premise left index','j','i','j|i'),('strict premise right index','i|j','j','i|j'),
('strict inclusion left index','j','i','j|i'),('strict inclusion right index','i','j','i|j'),
('witness refinement index','i','j','i|j'),('witness non-refinement index','j','i','j|i')]:
    p.change('upper block, '+place,C,H,final,'Small indices contain repeated superposed loops and descenders; their position is clear but the final i/j choice is not.','top',dc=C!=final,kind='misread symbol or index',confidence='low',marked='unclear')
    p.doubt('upper block, '+place,final,'Repeated overwriting prevents a secure final index reading','top',confidence='low')
p.change('upper block, intermediate implication','X_j << X_i|Y donc','omitted','X_(j|i) << X_i|Y donc','Two open angles and a following donc are written on the next line before the inclusion.','top',dc=True,kind='omission',confidence='medium',consequential='The refinement step between the order premise and inclusion is retained.')
p.change('witness variable','x|alpha','x','x','Two small curved crossing strokes with no closed alpha bowl.','top',dc=True,dh=False)
p.change('NB cancellation','NB?','omitted','NB, deleted and underlined','Initial diagonal N and two B lobes survive the scribbled crossing.','condition',dc=True,kind='omission',confidence='medium')
p.change('circle definition, left index','L_X circle|L_Xi circle','L_X circle','L_Xi circle|L_X circle','Two tiny marks remain to the lower right of the heavily retraced X; retention of i is preferred but its cancellation state is unsettled.','circleindex',dc=True,kind='misread symbol or index',confidence='medium',consequential='The circle definition retains a possible i on its left-hand X; the right-hand L_X remains unsubscripted.')
p.doubt('circle definition, left index','L_Xi circle|L_X circle','Tiny i-like mark beside the heavy X may be an abandoned trace','circleindex')
p.change('margin condition heading','Contr|Cont 3','Cont 3','Cont 3','After low Con the tall t has one short right cross-stroke; no additional r is separated.','leftlabel',dc=True,dh=False,confidence='medium')
p.change('first quantifier, deleted M index','deleted X_j|X subscript','omitted','deleted X_j|X subscript','Crossed small X and descending lower loop are attached below M.','condition',kind='omission',confidence='low')
p.doubt('first quantifier, deleted M index','X_j|X','Overwritten subscript remains undeciphered','condition',confidence='low')
p.change('nonempty condition punctuation','dash|period','dash','.-','A small point and separate short horizontal dash follow the empty-set glyph.','condition',dc=True,kind='other')
p.change('second quantifier cancellation','emptyset|X','omitted','emptyset, deleted','Small loop crossed by an oblique stroke, additionally overwritten, precedes the live X.','condition',dc=True,kind='omission',confidence='medium')
p.change('negative relation in stronger condition','bar over ≤|nleq|≤','not <<',r'\overline{\leq}','One chevron with its lower horizontal bar has a separate long bar above; no second chevron or diagonal negation stroke is visible.','negative',dc=True,kind='misread symbol or index',consequential='The stronger condition uses a bar over ≤; H supplies a negated <<.')
p.change('quantifier abbreviation','tts','tout','tts','Two tall t strokes and terminal low s, no ou.','condition',kind='abbreviation expanded or spelling modernised')
for place,H,final,evidence in [
('first continuation','ill','serait Soient X et Y.','serait and a second tall S with oient survive beneath the horizontal line.'),
('second start','Soient X et Y ill','Soient X et Y deux','Soient X et Y is followed by deux at next line start.'),
('noun','multiplicités','multistrates','Tall l, t and str cluster remain visible.'),
('abandoned formula','ill','X <<?','Crossed X and two short angle-like strokes appear between Supposons and les.'),
('ending','compatibles ill','compatibles. Je dis','Large J with looped base and separate dis remain within the crossed block.')]:
    p.change('large cancellation, '+place,final,H,final,evidence,'cancel',kind='readable ink left as \\ill{}',confidence='low' if place=='abandoned formula' else 'medium',marked='yes')
p.doubt('large cancellation, abandoned formula','X <<','Heavy cancellation overlaps the two small following angles','cancel',confidence='low')
p.change('final paragraph, connector','où X_i ≤ X','X_i ≤ X','où X_i ≤ X','Small où appears between the comma and the next X_i.','bottom',kind='omission')
p.change('final paragraph, underline','égale underlined','égale','égale underlined','A separate underline runs beneath the word égale.','bottom',kind='insertion or placement')
p.change('final existential, deletion state','deleted x? followed by live exists','deleted exists then ill','deleted x? followed by live exists i','The three bars and right stem of exists are complete; a smaller crossed glyph lies over its middle, with a dotted i to the right.','finalexist',dc=True,kind='deletion state (struck given live or live given struck)',confidence='medium',marked='yes',consequential='The existential sign is retained live; the overlaid older x remains doubtful.')
p.doubt('final existential, overlaid cancellation','x','Small overlaid crossing remains uncertain','finalexist',confidence='low')
p.change('final existential, variable','i|0','ill','i','An oval lower stroke has a distinct detached dot above it.','finalexist',dc=True,kind='readable ink left as \\ill{}',marked='yes')
p.change('final cancelled clause, variable','X_i|Y_i','ill','Y_i','Upper fork joins a single downward stem; small i follows, with no independent lower X diagonal.','bottom',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.change('final cancelled clause','et les X_i|Y_i forment un ouvert de M_≤X','ill and et partly live','et les Y_i forment un ouvert de M_≤X, all deleted','One horizontal strike runs from et across les, the variable, and the complete ouvert clause.','bottom',dc=True,kind='deletion state (struck given live or live given struck)',marked='yes')
p.change('last live sentence opening','Il y a un','et [ill] il y a un','Il y a un','New baseline begins with tall I/l; preceding et belongs to the crossed line above.','bottom',kind='insertion or placement')
for place,crop in [('first map image','top'),('first map target','top'),('monotone inclusion left','top'),('monotone inclusion right','top'),('strict inclusion left','top'),('strict inclusion right','top'),('circle definition','condition'),('circle definition right set','condition'),('circle definition union','condition'),('nonempty condition','condition'),('existential ambient set','condition'),('cancelled map image','cancel'),('cancelled map target','cancel'),('final circle family','bottom'),('final inserted containment','bottom'),('final equality target','bottom'),('final point membership','bottom'),('final indexed membership','bottom')]:
    p.change('L alphabet, '+place,'L','calligraphic L',r'\mathcal{L} with written indices/decorations','Tall curved stem and lower looping return recur at this location.','top' if crop=='top' else crop,dc=True,dh=False,confidence='medium')
for place,crop in [('first map domain','top'),('first condition domain','condition'),('second condition domain','condition'),('cancelled opening domain','cancel'),('cancelled map domain','cancel'),('last paragraph domain','bottom'),('last cancelled domain','bottom')]:
    p.change('M alphabet, '+place,'M','calligraphic M','M','Two peaked humps with a short curved entry, retained as the recurring M.','top' if crop=='top' else crop,kind='misread symbol or index',confidence='medium')
p.change('cancelled map, P alphabet','calligraphic P','fraktur P',r'\mathcal P','Broad angular bowl on a straight stem matches the live first map.','cancel',kind='misread symbol or index',confidence='medium')
p.inventory([
('text','header','21'),('deletion','opening','Soit X une multistrate'),('text','opening','L’application'),('display','first map','X mapsto L_Xi ; M_≤X to P(L)'),
('text','monotonicity paragraph','est bien sur croissante'),('display','parenthesized implication','X_j ≤ X_i ⇒ X_j << X_i donc inclusion'),('text','strictness wish','On aimerait'),('deletion','after i.e. que','X_j|X′'),('display','strict implication','X_j<X_i ⇒ strict inclusion'),('text','witness restatement','i.e. exists lieu x'),
('deletion','before Soit','NB'),('display','circle definition','L_Xi circle|L_X circle = difference'),('text','after definition','Condition plus forte'),('margin note','left condition','Cont 3'),('display','strong condition','forall X in M, L_X circle nonempty'),('deletion','M subscript','X_j|X'),
('display','equivalent wording','forall X in M exists x in L'),('deletion','between forall and X','emptyset'),('insertion','above x << X','tel que'),('display','negative condition','x bar-over-≤ X_i pour tts X_i<X'),
('deletion','large block opening','Ainsi, si X in M'),('display','cancelled map','X_i mapsto L_Xi circle ; M_≤X to P(L)'),('deletion','large block continuation','serait Soient X et Y. Soient X et Y deux multistrates'),('deletion','within large block','X <<'),('deletion','large block ending','compatibles. Je dis'),
('text','final paragraph','Soit X in M, considérons'),('insertion','above réunion est','qui est subset L_X'),('deletion','over existential','x'),('deletion','last crossed line','et les Y_i forment un ouvert'),('text','last live line','Il y a un X_i minimal parmi les')])
p.notation('overbar negation',r'\overline{\leq}','One ≤ with a distinct horizontal bar above, no diagonal negation stroke')
p.notation('strict inclusion',r'\subsetneq','Open C-shaped inclusion stroke over an additional lower bar, both crossed by a diagonal')
p.r['abbreviations']=[{'abbreviation':a,'expansion':e,'evidence':'Visible on scan 022'} for a,e in [('i.e.','id est'),('tts','tous'),('Cont','contrée / condition (heading)')]]
p.save()
