from pathlib import Path
from datetime import datetime,timezone
import json

out=Path(__file__).parent
m=json.loads((out/'scan007_crops.json').read_text())
cm={Path(x['file']).stem.removeprefix('scan007_'):x for x in m}
D=[]
def row(n,place,C,H,reading,dc,dh,kind,evidence,crop=None,confidence='high',marked=False,cd='not applicable',math=None):
 c=cm.get(crop)
 D.append(dict(id=f'R2-007-{n:02d}',place=place,C=C,H=H,reading=reading,diff_C=dc,diff_H=dh,kind=kind,marked_in_H=marked,confidence=confidence,evidence=evidence,crop=c['file'] if c else None,crop_coordinates=c['box'] if c else None,C_doubt_status=cd,math_consequence=math))

row(1,'cancelled first line M',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}',False,True,'misread symbol or index','The two raised stems and curved connecting valley give the familiar handwritten M, with no secure distinction between plain and calligraphic alphabet.','initial','medium',False,'retained')
row(2,'cancelled first line Phi',r'\unsure{\Phi|\varphi}',r'\Phi',r'\Phi',True,False,'misread symbol or index','The oval, straight central stem and broad horizontal lower foot together identify the capital Phi form. The foot is separate from the cancellation rule.','initial','medium',False,'resolved')
row(3,'figure-set alphabet throughout',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}',False,True,'misread symbol or index','A looped, swept upper arm and middle crossbar are cursive rather than Gothic. Script versus calligraphic remains ambiguous.','initial','medium',False,'retained')
row(4,'cancelled first statement ending',r'\unsure{élément}','élément','élément',True,False,'misread word','The accented first e, tall l and final t are visible above the rule, with the intervening low run of élément.','element','medium',False,'resolved')
row(5,'upper-margin old number',r'\deleted{\unsure{6}}5','5, old numeral omitted',r'\deleted{\unsure{6}}5',False,True,'omission','A small older rounded trace remains inside the live 5. It permits 6 but does not expose a whole unambiguous numeral.','upper_margin','low',False,'retained')
row(6,'upper-margin termes',r'\unsure{termes|terme}','termes','termes',True,False,'misread word','After the e-like low curve there is a separate short final s turn.','upper_margin','medium',False,'resolved')
row(7,'upper-margin full prose','J’ai exprimé At5 sans référence à F ou à tilde F, mais directement en termes de ...','J’ai exprimé At5 [ill.] [ill.] F [ill.] tilde F, mais directement en termes de ...','J’ai exprimé At5 sans référence à F ou à tilde F, mais directement en termes de ...',False,True,r'readable ink left as \ill{}','Sans référence, the first à, ou and the second à are readable in the margin. The f descender of référence has its own loop and should not be mistaken for a missing word. At is underlined.','upper_margin','high',True)
row(8,'upper-margin arrow','northeast arrow','arrow described only in editorial note','northeast arrow reproduced',False,True,'drawing or diagram','A separate sloping shaft runs from the note to the upper right and ends in a pointed head.','upper_margin')
row(9,'a abandoned opening word','Posant','Posons','Posant',False,True,'misread word','The cancelled word ends with a tall t-like stroke after the low a/n run, not with a final s.','cancel_starts','medium')
row(10,'a abandoned first relation and arrow',r'X\ll Y\ \unsure{\Longleftrightarrow|\Longrightarrow}',r'X\overset\circ\ll Y\overset{déf}{\Longleftrightarrow}',r'X\ll Y\ \unsure{\Longleftrightarrow|\Longrightarrow}',False,True,'misread symbol or index','The baseline old relation is an undecorated doubled angle. The connector has two horizontal shafts and a clear right turn; the possible left head is entangled with cancellation. No independent circle above this old relation can be separated.','cancel_starts','low',False,'retained')
row(11,'a abandoned letter after arrow',r'\unsure{Y}','X',r'\unsure{Y}',False,True,'misread symbol or index','A fork and downward stem remain beneath a strong diagonal crossing. They favour Y, but the crossing makes the reading tentative.','cancel_starts','low',False,'retained')
row(12,'a abandoned verb after Y',r'\unsure{contient}',r'\ill{}',r'\unsure{contient}',False,True,r'readable ink left as \ill{}','The first rounded c/o-like group, a tall middle stroke and an exiting terminal stroke survive, consistent with contient. Much of the low sequence remains covered.','cancel_starts','low',True,'retained')
row(13,'separate cancelled interlinear starts','distinct cancelled forall X,Y∈M, X≪ ... and est minimal ...','one combined cancelled sentence','separate cancelled starts retained in their order',False,True,'insertion or placement','The quantified start is above the Posant baseline, and the est/minimal group sits separately over its right end. Their distinct writing levels are visible.','cancel_starts','high')
row(14,'interlinear abbreviation after X≪',r'\unsure{défini}','déf as label in a combined formula',r'\unsure{dfn|défini}',True,True,'abbreviation expanded or spelling modernised','The separable forms are a looped d, a tall f and a short n-like exit. The longer défini is not fully recoverable; dfn is the literal first candidate, consistent with the visible short group rather than an expanded word.','cancel_starts','low',False,'changed')
row(15,'old interlinear word before minimal',r'\unsure{est|ent}','not separately transcribed','est',True,True,'omission','The leading loop, low s-like curve and tall final t can be distinguished above the crossing rule.','cancel_starts','medium',False,'resolved')
row(16,'old interlinear final adjective',r'\unsure{minimal|minimum}','minimal',r'\unsure{minimal|minimum}',False,True,'misread word','The crowded minims run into a high final stroke. Minimal remains first, but the heavily crossed ending does not exclude minimum.','cancel_starts','low',False,'retained')
row(17,'live clause cancelled phrase','plus petit élément',r'\struck{\ill{}}','cancelled plus petit élément',False,True,r'readable ink left as \ill{}','The p descenders, tall t strokes and the accented élément start remain visible beneath the horizontal rule.','replacement','medium',True)
row(18,'replacement after un',r'\inserted{élément \unsure{minimal|minimum|privilégié}}',r'\add{minimal}',r'\inserted{élément \unsure{minimal|minimum|privilégié}}',False,True,'omission','The addition begins with a separate élément above the cancelled phrase. The following adjective has crowded minims and a high terminal stroke; its exact reading remains open.','replacement','low',False,'retained')
row(19,'dans before selected set',r'\inserted{dans}','ordinary dans',r'\inserted{dans}',False,True,'insertion or placement','Dans is written above the baseline before tilde Y^X, after the replacement phrase, rather than as part of the earlier line.','replacement')
row(20,'cancelled i.e. condition',r'\deleted{\unsure{i.e.} ...}',r'i.e. within a larger deleted block',r'\deleted{i.e. ...}',True,False,'misread word','Small separated points and the short i/e strokes are visible before the X of the lower crossed implication. The whole implication remains deleted.','replacement','medium',False,'resolved')
row(21,'parenthetic notation insertion',r'\inserted{(\unsure{posons|posant} X\overset\circ\ll Y si c’est Y)}',r'\struck{posons X\overset\circ\ll Y si [ill.]}',r'\inserted{(posons X\overset\circ\ll Y si c’est Y)}',True,True,'deletion state (struck given live or live given struck)','The parenthesis and posons line lie above the old crossed implication. Its final word turns through a low s, not a tall t. The crossing belongs to the old implication underneath; the notation parenthesis remains live.','replacement','medium',True,'resolved')
row(22,'AtM6 old digit',r'\deleted{\unsure{5}}6','6 with overwrite described',r'\deleted{\unsure{5}}6',False,True,'omission','A short older horizontal survives inside the lower loop of the new 6, but the overwritten form is not fully separable.','Atnumbers','low',True,'retained')
row(23,'AtM5 old digit',r'\deleted{\unsure{6}}5','5 with overwrite described',r'\deleted{\unsure{6}}5',False,True,'omission','The current 5 has an extra prior curved/upper trace. An old 6 is plausible but not recoverable as a complete independent shape.','Atnumbers','low',True,'retained')
row(24,'curved interchange drawing','TikZ connection of two labels','drawing described in editorial note','TikZ connection of two labels',False,True,'drawing or diagram','One rounded lower loop and an upward bent arrow run beside the two axiom labels. They are reproduced as strokes, without renumbering the text.')
row(25,'D’autre part main clause','on peut laisser tomber l’élément de structure',r'\add{bien \uncertain{connues}} [ill.] l’élément de structure','on peut laisser tomber l’élément de structure',False,True,r'readable ink left as \ill{}','The short on peut begins the line, followed by laisser with tall double s-like turns and tomber with its t and b ascenders. There is no inserted bien connues.',None,'high',True)
row(26,'structure symbol at clipped right edge',r'\unsure{\widetilde{\mathscr F}|\mathscr F}',r'\widetilde{\mathfrak F}',r'\unsure{\widetilde{\mathscr F}|\mathscr F}',False,True,'misread symbol or index','The edge clips the letter’s right side. A small upper detached trace permits a tilde, but its full wave cannot be separated securely from the clipped strokes.','edge_F','low',False,'retained')
row(27,'au profit insertion',r'\inserted{au profit de [compatibility],}',r'\add{[ill.] au profit de [compatibility]}',r'\inserted{au profit de [compatibility],}',False,True,'text not on the page','The interlinear addition starts directly au profit de, followed by the compatibility sign and a comma. No extra preceding illegible word occupies that locus.',None,'high',True)
row(28,'connector between AtM1 and AtM3','à','à',';',True,True,'misread symbol or index','An upper detached dot stands over a lower curved comma-like stroke. There is no closed a body or separate grave stroke: the literal mark is a semicolon.','range','high',False,'not applicable','The expected range wording is not supplied; the semicolon is copied literally.')
row(29,'par (a) following words','de la','et la','de la',False,True,'misread word','The first short group begins with a d loop/stem before e; it is not et.')
row(30,'old cancelled axiom number before (tf)',r'\unsure{1|0}','number left unread','1',True,True,'misread symbol or index','The numeral has a high oblique entry and a vertical main stroke. There is no closed oval suggesting 0. Its rightward lower curve overlaps the following opening parenthesis.','oldaxiom','medium',True,'resolved')
row(31,'cancelled group before page 5',r'\deleted{\unsure{At}}',r'\struck{\ill{}}',r'\deleted{\unsure{At}}',False,True,r'readable ink left as \ill{}','An A-like first shape and a short crossbar survive. Additional diagonal overwriting obscures the remaining extent; At stays tentative.','page5','low',True,'retained')
row(32,'reference word before 5',r'\unsure{page|p.}',r'\uncertain{Voir} p.','page',True,True,'abbreviation expanded or spelling modernised','The word has two descending forms, compatible with p and g, with low intervening and final curves. It is longer than a single p abbreviation and does not have a separate Voir plus p. sequence.','page5','medium',True,'resolved')
row(33,'asterisk on compatibility in condition b','compatibility with superscript star','plain compatibility','compatibility with superscript star',False,True,'omission','A small distinct star is raised immediately above and right of the compatibility sign before the sentence point. It is not part of the crossing strokes of the relation.')
row(34,'slanted margin implication form','rounded return / pointed implication alternatives','pointed implication','two shafts with a rounded upper right return, drawn in TikZ',True,True,'misread symbol or index','Rotation shows two separate horizontal shafts. The upper one curls downward at its right end; it does not form a pointed two-sided arrowhead.','margin_arrow','high',False,'resolved')
row(35,'first primed variable in slanted note',"X'","X'",r"\unsure{X'|Y'}",True,True,'misread symbol or index','The first primed character after et has a short lower-right limb and a longer descending opposite limb. X′ is first, but the compressed form also permits Y′. The following bound is clearly X.','margin_arrow','low',False,'not applicable','The possible variable mismatch remains marked rather than being repaired from the hereditary-compatibility condition.')
row(36,'Dans le cas général clause','quand on a simplement [compatibility] satisfaisant cette condition b)',r'grâce à \uncertain{laquelle} [compatibility] satisfait cette condition b)','quand on a simplement [compatibility] satisfaisant cette condition b)',False,True,'misread word','The sequence quand on a is readable before simplement; satisfaisant has the ending -sant, not the shorter satisfait.',None,'high',True)
row(37,'finite-family insertion placement and stroke','linear inserted Phi de t.f., without curved stroke','insertion described in editorial note','Phi de t.f. interlinear above de M,≤, with a long curved insertion stroke',True,True,'insertion or placement','The addition sits above the final de M,≤. Its curved leader starts at the left insertion point below the added phrase, runs beneath it and curls upward at the right. The TeX now draws both placement and stroke.','finite_layout','high')
row(38,'finite-family order notation','de M,≤','de (M,≤)','de M,≤',False,True,'text not on the page','The de is followed directly by M, comma and ≤. No enclosing parentheses are drawn. The nearby curved stroke belongs to the insertion above, not to a pair of parentheses.','finite_layout','high')
row(39,'finite-family deleted first word',r'\unsure{formées}','deleted word only mentioned in editorial note','formées',True,True,'omission','The long f descender, rounded middle run and final e/s turn are visible below the deletion rule. The word reads formées.','finite_deleted','medium',True,'resolved')
row(40,'finite-family deleted short group',r'\unsure{t.q.}','omitted',r'\unsure{t.q.}',False,True,'omission','A short upright and a following loop/descending stroke lie below the inserted que, with tiny points partly obscured. T.q. remains tentative.','finite_deleted','low',True,'retained')
row(41,'finite-family replacement phrase and colon',r'\inserted{telles que :}','ordinary telles que; insertion only described','inserted telles que :',False,True,'insertion or placement','Telles que is above the crossed formées/t.q. line. A colon follows que before the mathematical condition.','finite_deleted','high')
row(42,'finite-family implication drawing','straight Longrightarrow','straight Longrightarrow','double-stroked implication with curved upper lead-in',True,True,'drawing or diagram','The upper shaft begins in a long curved descending lead-in, then joins the straight rightward arrow. The lower shaft is straight. The f descender from fermées above touches the upper-shaft junction; it is not an extra relation.','finite_layout','high')
row(43,'additional structure phrase','un choix de structure de plus','un choix de structure en plus','un choix de structure en plus',True,False,'misread word','The short word after structure consists of low connected e/n humps, with no tall d ascender. It reads en, agreeing with H.')
row(44,'ordered-family abbreviation','l’ens ordonné','l’ens. ordonné','l’ens ordonné',False,True,'other','No independent point follows ens before ordonné.')
row(45,'operator names, both occurrences','Mulomb(F)','Multomb(F)','Mulomb(F)',False,True,'misread symbol or index','The operator runs from the tall l straight into the low o/m sequence; no intervening t is written. This agrees with the earlier Mulomb spelling.')
row(46,'où before second operator equation',r'\deleted{\text{où}}','live où','deleted où',False,True,'deletion state (struck given live or live given struck)','The grave accent remains above the u, while a separate straight horizontal stroke crosses the lower o/u traces.','ou','medium')
row(47,'first crossed object in Mulomb braces',r'\deleted{\unsure{X}}','sign mentioned only in editorial note',r'\deleted{\unsure{X}}',False,True,'omission','Two large crossed diagonals remain beneath additional looped cancellation strokes. X is plausible, but the upper added strokes prevent a clean reading of the whole group.','foot_X','low',True,'retained')
row(48,'argument of Omb inside Mulomb set','Omb(x)','Omb(X)','Omb(x)',False,True,'misread symbol or index','The argument is a small lowercase crossed x; the separate bound variable after the vertical separator is a larger capital X.')
row(49,'final lower order index',r'M_{\ll x}',r'\mathcal M_{\ll X}',r'M_{\ll x}',False,True,'misread symbol or index','The final x in the subscript is small and cursive, contrasting with the capital X named on the left of the equality.')
row(50,'foot reference letters',r'\unsure{GF|GE}','GF','GF',True,False,'misread word','The second capital has an upper arm and one middle crossbar. It lacks the additional lower horizontal needed for E.','GF','high',False,'resolved')
row(51,'cf punctuation','cf Scholie','cf. Scholie','cf Scholie',False,True,'other','No point is visible between cf and Scholie.')
row(52,'reference after et axiomes','ou mieux à la page 32, page 32 underlined',r'en \uncertain{nombre} de [ill.] p.32','ou mieux à la page 32, page 32 underlined',False,True,r'readable ink left as \ill{}','The next line begins mieux, preceded by ou at the end of the prior line, then à la and the written word page. The rule runs beneath page and 32 together.',None,'high',True)
row(53,'final comparison','comme sous-atelier','comme un sous-atelier','comme sous-atelier',False,True,'text not on the page','Sous-atelier begins directly after comme at the new line; there is no un.')
row(54,'final parenthetic adjective','spacieux','spécieux','spacieux',False,True,'misread word','After s/p, the low open a-form has no middle e cross-stroke and no acute above it. The following c/i/e/u/x sequence is visible.','spacieux','medium')

A=[
 ('M|mathcal M','cancelled first line','retained',1),
 ('Phi|varphi','cancelled first line','resolved: Phi',2),
 ('mathscr F|mathcal F','cancelled first line','retained',3),
 ('élément','cancelled first statement ending','resolved: élément',4),
 ('old 6','upper-margin At5','retained',5),
 ('termes|terme','upper margin','resolved: termes',6),
 ('Longleftrightarrow|Longrightarrow','abandoned a connector','retained',10),
 ('Y','abandoned a after arrow','retained',11),
 ('contient','abandoned a verb','retained',12),
 ('défini','cancelled interline','changed: dfn|défini',14),
 ('est|ent','cancelled interline','resolved: est',15),
 ('minimal|minimum','cancelled interline ending','retained',16),
 ('minimal|minimum|privilégié','inserted adjective','retained',18),
 ('i.e.','cancelled condition','resolved: i.e.',20),
 ('posons|posant','live notation insertion','resolved: posons',21),
 ('old 5','AtM6 label','retained',22),
 ('old 6','AtM5 label','retained',23),
 ('tilde F|F','clipped right edge','retained',26),
 ('1|0','old AtM(tf) number','resolved: 1',30),
 ('At','cancellation before page5','retained',31),
 ('page|p.','reference word','resolved: page',32),
 ('rounded return|Longrightarrow','slanted margin','resolved: rounded return drawing',34),
 ('formées','finite-family deletion','resolved: formées',39),
 ('t.q.','finite-family deletion','retained',40),
 ('X','Mulomb deletion','retained',47),
 ('GF|GE','foot reference','resolved: GF',50),
]
ix={int(x['id'].rsplit('-',1)[1]):x for x in D}
audit=[dict(C_reading=a,place=b,status=c,evidence=ix[n]['evidence'],crop=ix[n]['crop'],crop_coordinates=ix[n]['crop_coordinates'],difference_id=ix[n]['id']) for a,b,c,n in A]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

data=dict(reader='R2',scan=7,start_utc='2026-11-19 22:05:37 UTC',end_utc=end,
 model='GPT-6 Astra Pro; inherited effort setting not exposed; R2',
 images_viewed=['H156-01_156-7_scan007.jpg','H156-01_156-7_scan007_a.jpg','H156-01_156-7_scan007_b.jpg']+[x['file'] for x in m],
 coverage=[
  'page number 6 and entire cancelled AtM4 statement, including colon, variables, fonts, tilde, exponents, set builder and least-element conclusion',
  'all three abandoned starts of the revised AtM4(a), their separate writing levels, relations, letters, words and crossing strokes',
  'complete live Si X≪Y clause, erased plus petit élément, inserted élément/adjective and dans, selected-set formula, erased i.e. implication, live parenthetic posons notation',
  'AtM4(b) internal-refinement uniqueness with both primes and compatibility condition',
  'upper-left full explanatory note, old numeral, term ending, underline and arrow',
  'corrected AtM6 and AtM5 formulas, overwritten numerals and complete curved interchange connector',
  'D’autre part paragraph, clipped structure symbol, au profit insertion, literal semicolon range connector, cancelled axiom version, deleted At, page5 reference, compatibility superscript star',
  'slanted hereditary-compatibility note, every primed variable and both relations, rounded two-shaft implication',
  'general-case paragraph and full finite-family display with both interlinear additions, both erased words, no added ordered-pair parentheses, curved insertion stroke and curved implication lead-in',
  'additional structure paragraph with en plus, antifiltres infinis, abbreviation punctuation and literal ellipsis',
  'all three lower operator equations: Mulomb without t, second Mulomb argument F independently inspected, deleted où and X, lower-case Omb(x), upper-case bound X, final lower-case order index',
  'complete concluding reference, GF, page32 underline, no added un, and spacieux',
  'comparison of current live AtM4(a) with the previously read S row only; no other S row, later page, or other-reader/main decision inspected'],
 notation=[
  dict(form='M and figure-set alphabets',reading='M|mathcal M and mathscr F|mathcal F',evidence='recurring handwritten forms; font uncertainty marked at first occurrence'),
  dict(form='Phi',reading='capital Phi in first cancelled line',evidence='oval, straight stem and clear lower bar'),
  dict(form='AtM range connector',reading='literal semicolon between 1 and 3',evidence='separate upper dot and lower comma stroke'),
  dict(form='interlinear abbreviation',reading='dfn|défini',evidence='short d/f/n-like group, no recoverable full ending'),
  dict(form='marginal implication',reading='two shafts with rounded upper return',evidence='no pointed arrowhead'),
  dict(form='finite display',reading='Phi de t.f. above final de M,≤; curved insertion leader; curved implication lead-in',evidence='explicit node positions and strokes drawn in TikZ'),
  dict(form='operator',reading='Mulomb(F) at both occurrences, no t',evidence='second argument independently cropped: one stem and two rightward arms identify F, not X'),
  dict(form='lowercase variables',reading='Omb(x) and M_llx versus uppercase bound X',evidence='literal size/shape differences preserved'),
  dict(form='reference',reading='GF; page32 underlined; cf without point; spacieux',evidence='literal visible letters and rules')],
 math_notes=[
  dict(type='summary, not proof check',text='Revises the stratum-level axiom into an existence condition under X≪Y and a uniqueness condition for two compatible internal refinements. Two later axioms are interchanged by numbering and a drawn connector. For finite-type figures, the text drops the chosen family in favour of compatibility and describes the corresponding finite closed compatible subsets.'),
  dict(type='S comparison, separate from ink',text='The current live AtM4(a) explicitly starts Si X≪Y. This supports S’s proposed refinement hypothesis as an intended formulation at the level of strata. The earlier page still literally writes X triangleleft F and must remain so. The current text has been revised from a least-member phrase to an inserted adjective read tentatively as minimal, plus compatible uniqueness; it is not a literal restatement of the earlier sentence.'),
  dict(type='targeted counterexample to cancelled draft',statement_id='R2-007-M1',text='For nonempty M the cancelled first universal statement fails when Phi is empty: choose M={a}, the closed-set family {empty,{a}}, and Phi=empty. Then Phi^a is empty and has no least element. This concerns only the abandoned universal draft, not the live axiom.'),
  dict(type='targeted local check',statement_id='R2-007-M2',text='In the live selected family tilde Y^X={Z≤Y : X≪Z}, the hypothesis X≪Y guarantees nonemptiness: reflexivity gives Y≤Y, so Y itself belongs. This does not prove existence of a minimal member and does not settle the uncertain inserted adjective.'),
  dict(type='unproved author claims',text='The finite-family reconstruction, the additional choice of infinite antifilters, and the final shadow-set representation are copied without an independent proof. No external pages named in the foot reference were consulted.'),
  dict(type='literal mismatches retained',text='The semicolon in the AtM1/AtM3 range, the lower-case x inside Omb(x) with uppercase bound X, and the lower-case terminal index x remain literal. The marginal first primed letter is newly doubtful rather than repaired from the expected hereditary condition.')],
 author_qualifications=['pour des F à figures de type fini','Dans le cas général','il faut cependant un choix de structure en plus','pas néc. spacieux'],
 author_explicit_verification_requests=[],
 unresolved=[dict(place=x['place'],reading=x['reading'],confidence=x['confidence']) for x in D if x['C_doubt_status'] in ('retained','changed')]+[dict(place='first primed variable in slanted note',reading='X′|Y′',confidence='low')],
 differences=D,C_doubt_audit=audit,
 S_comparison=[dict(row_id='SA21-K7-01',previous_page_literal='X triangleleft F (i.e. X in tilde F)',current_page_literal='Si X≪Y, alors il y a un ... dans tilde Y^X',outcome='Current live text supports a refinement hypothesis at the stratum level. It strengthens the interpretation of S as an intended mathematical emendation; it does not change the literal sign on scan006 or certify the full earlier quantification after a one-symbol replacement.',limits='The inserted adjective remains minimal|minimum|privilégié. No other S row or later manuscript page was read.')],
 new_omissions_from_both=[
  dict(place='AtM1 to AtM3 connector',reading='semicolon substituted by à in both witnesses',confidence='high'),
  dict(place='finite-family display',reading='long curved insertion stroke and curved upper lead-in of the implication are not fully drawn by either witness',confidence='high')],
 parent_requested_checks=[
  dict(place='range connector',reading='semicolon',evidence='upper dot plus lower comma',crop='readers/R2/crops/scan007_range.png'),
  dict(place='second Mulomb argument',reading='F',evidence='one stem with two rightward arms; the upper arm is oblique',crop='readers/R2/crops/scan007_second_argument.png'),
  dict(place='finite-family display',reading='interlinear Phi de t.f.; curved leader; curved implication upper lead-in',evidence='layout and individual curves retained in TikZ',crop='readers/R2/crops/scan007_finite_layout.png')],
 crop_manifest='readers/R2/scan007_crops.json',
 check_events=[
  dict(statement_id='R2-007-M1',date=end,who='GPT-6 Astra Pro; inherited effort setting not exposed; R2',type='targeted proof check',outcome='Explicit singleton-M, empty-Phi counterexample to the cancelled unrestricted least-element draft.'),
  dict(statement_id='R2-007-M2',date=end,who='GPT-6 Astra Pro; inherited effort setting not exposed; R2',type='targeted proof check',outcome='The live hypothesis X≪Y makes Y itself a member of the selected family; nonemptiness verified, minimal-element existence not proved.')])

(out/'scan007.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(out/'scan007.md').write_text('''# R2 — independent reading, scan 007

The whole page and both supplied halves were inspected once. Eighteen distinct targeted crops were made and viewed, including the three small-layout loci requested by the parent while this page was in progress. All 26 C doubts have individual decisions. No other reader/main decisions, other S rows, or later pages were read.

## Principal findings

The connector between AtM1 and AtM3 is a literal semicolon: an upper dot over a separate comma-shaped lower stroke. Both witnesses normalize it to à. The additional-structure sentence says en plus, agreeing with H against C’s de plus. Both operator names are Mulomb without t. A targeted crop confirms that the second Mulomb argument is F, with a stem and two rightward arms; its oblique top arm does not make it X.

The finite-type-family display is drawn with the added Phi de t.f. above the final de M,≤. Its long curved insertion stroke and the curved upper lead-in of the following implication are reproduced. No parentheses have been added around M,≤. The f descender of fermées touches the implication shaft in the handwriting; it is not another logical mark.

The upper corrections remain difficult. The old abbreviation following X≪ is now dfn|défini; the old contains verb and minimal/minimum endings remain doubtful. The live replacement adjective remains minimal|minimum|privilégié. The parenthetic posons X internal-refines Y si c’est Y is live inserted text, whereas the i.e. implication underneath is deleted. The first primed variable in the slanted marginal note is marked X′|Y′ because its small lower limbs are not fully separable. The clipped right-edge family glyph still permits tilde F or F.

The upper-margin full prose, all cancelled drafts, both overwritten numbering traces, the finite-display deleted words, the cancelled où, the small crossed X before Omb, and all lower-case x occurrences are retained. The ending reads GF, ou mieux à la page32 (underlined), comme sous-atelier, and pas néc. spacieux.

## S reference and mathematics

The current live AtM4(a) explicitly starts Si X≪Y. This supports S’s intended refinement hypothesis at the stratum level, while scan006’s literal triangle remains unchanged. The current revised condition and the compatible-uniqueness clause are kept in their actual form; the uncertain inserted adjective is not settled by the mathematics.

Two narrow checks are recorded: the cancelled universal least-member draft has a counterexample with nonempty M and empty Phi; the live X≪Y hypothesis makes Y itself a member of the selected family. No proof of minimal-element existence, full finite-family reconstruction, antifilter completion, or the shadow-set representation is claimed.
''')
print(len(D),'difference rows;',len(A),'C doubts;',len(m),'crops')
print('C differences',sum(x['diff_C'] for x in D),'H differences',sum(x['diff_H'] for x in D))
