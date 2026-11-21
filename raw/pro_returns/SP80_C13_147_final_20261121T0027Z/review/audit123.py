from edition.scripts.root_audit import Audit

a=Audit(123)
a.keep('B01','Four detached bang marks are visible, the group bases sit below the m level, and def has no accent. The doubled group strokes and underbrace are retained; the difference is font and math-delimiter encoding.')
a.keep('B04','The abbreviation ends in compressed low joins and a point, with no securely separable t. The roof with two legs before subscript 1 does not settle capital versus lowercase Pi in this hand. Both existing alternatives remain; no terminal point is visible after P_d.')
a.keep('B05','The raised word has a descending q after the opening curved stroke, low u-a-n joins and a final tall d. These support (quand rather than l\'ouvert. The lower le groupoïde is crossed independently.')
a.keep('B06','The word image ends in a short return without a distinct additional s. The connector has one downward terminal, the live D_d is raised above separate crossed lower strokes, and the unit before plus is only a dark blot with no separable o-u pair. Existing literal geometry and uncertainty are retained.')
old=r'\Pi(\underbrace{P_d\mid D_d^*}_{\overset{\mathrm{def}}{=}T_d^*})=\Pi P_d^*.'
new=r'\Pi\underbrace{(P_d\mid D_d^*)}_{\overset{\mathrm{def}}{=}T_d^*}=\Pi P_d^*.'
a.change('B08','$'+new+'$','The brace begins below the lower turn of the opening parenthesis and extends to the lower turn of the closing parenthesis. Its scope is therefore drawn beneath the parenthesized expression. The lower symbol has a roof and stem without a P bowl, supporting T_d^*, and def is unaccented.')
a.replace(old,new)
a.add_row('B08','Extent of the underbrace in the unnumbered groupoid display',r'\Pi(\underbrace{P_d\mid D_d^*}_{\overset{\mathrm{def}}{=}\unsure{T_d^*|P_d^*}})',r'\Pi\bigl(\underbrace{P_d \mid D^{*}_d}_{\overset{\text{déf}}{=} P^{*}_d}\bigr)',new,'medium','diagram','brace extent',True,True)
a.keep('B09','The single secure i dot and absence of a separate tall t favor variance; the suffix remains compressed enough that variation is not finally excluded. The first reading already records both alternatives.')
a.keep('B10','P_d and P_d^* are raised above a curved insertion leader. The following T,G,P each carry a separate upright and dot; both Pi expressions are on the baseline. The difference is only whether math delimiters surround the insertion.')
f=r"\deleted{$d\unsure{\geq|>}d'$}"
a.change('B12',f,'The canceled comparison retains an angular greater-than body, but the cancellation crosses at the height where a lower equality bar would lie. The first geq remains possible, but a strict greater-than sign cannot be excluded from these intersecting strokes; the final prime is clear.')
a.replace(a.comparison['B12']['first'],f)
a.add_row('B12','Relation in the canceled inequality above the live range',r"\deleted{$d\geq d'$}",r"\struck{$d \geqslant d'$}",f,'low','symbol','cancellation obscures lower bar',True,True,True)
a.doubt('Relation in the canceled inequality above the live range',r'\unsure{\geq|>}','The lower bar coincides with the cancellation, so geq versus strict greater-than remains unresolved.','low')
f=r'\deleted{\unsure{avec|(193)}}'
a.change('B15',f,'Heavy cancellation crosses the whole unit. Low joins permit the first candidate avec, but the surviving tall and rounded strokes also permit the blind candidate (193). Neither letters nor a complete three-digit sequence with both parentheses can be securely isolated.')
a.replace(a.comparison['B15']['first'],f)
a.update_row(18,'B15',H=a.report['rows'][17]['H'],final=f,against_C=True,confidence='low')
a.doubt('Unindexed C doubt in the lower cancelled word',f,'Avec remains possible; the blind reading (193) is also compatible with some surviving vertical and rounded strokes. Dense cancellation prevents resolution.', 'low',replace_place='Unindexed C doubt in the lower cancelled word')
a.keep('B16','Both descending fan edges have converging heads, and the top and right indices are legible. The small dark left superscript remains starred-mark versus correction-remnant uncertain. The right label ends in a tall l and short exit that does not securely settle an extra e; the first alternatives retain that ambiguity.')
for e in a.report['inventory']:
 if e['element']=='E14':e['first_words_or_objects']=new.removesuffix('.')
 if e['element']=='E18':e['first_words_or_objects']=r"\deleted{$d\unsure{\geq|>}d'$}"
 if e['element']=='E21':e['first_words_or_objects']=r'\deleted{\unsure{avec|(193)}}'
a.note('Blind audit: all 10 differing boxes were inspected. The underbrace is extended beneath the parentheses, and the two dense cancellations now retain geq|greater-than and avec|(193) alternatives. The image-supported (quand, group-base placement, T beneath the brace, actual connector tips and existing case/abbreviation doubts were retained. The H column for the lower cancellation now quotes its actual editorial note rather than an explanatory placeholder.')
a.finish()
