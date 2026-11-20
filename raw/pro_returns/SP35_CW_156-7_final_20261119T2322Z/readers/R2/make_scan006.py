from pathlib import Path
from datetime import datetime, timezone
import json

out=Path(__file__).parent
m=json.loads((out/'scan006_crops.json').read_text())
crops={Path(x['file']).stem.removeprefix('scan006_'):x for x in m}
D=[]
def row(n,place,C,H,reading,dc,dh,kind,evidence,crop=None,confidence='high',marked=False,cd='not applicable',math=None):
 c=crops.get(crop)
 D.append(dict(id=f'R2-006-{n:02d}',place=place,C=C,H=H,reading=reading,diff_C=dc,diff_H=dh,kind=kind,marked_in_H=marked,confidence=confidence,evidence=evidence,crop=c['file'] if c else None,crop_coordinates=c['box'] if c else None,C_doubt_status=cd,math_consequence=math))

row(1,'opening figure-set alphabet',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}',False,True,'misread symbol or index','The long arched upper arm, single middle bar and returning foot are cursive rather than broken Gothic. Script versus calligraphic is still ambiguous.','opening','medium',False,'retained')
row(2,'M alphabet',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}',False,True,'misread symbol or index','The M has two high stems joined by a low curved valley. Its ordinary handwritten form does not uniquely identify a mathematical alphabet.','opening','medium',False,'retained')
row(3,'équivaut punctuation','équivaut :','équivaut à :','équivaut :',False,True,'text not on the page','The word ends before the colon; there is no separate à in the intervening blank.')
row(4,'opening cancelled group',r'\deleted{\unsure{X\leq}[compatibility]}',r'\struck{\ill{}}',r'\deleted{\unsure{X\leq}[compatibility]}',False,True,r'readable ink left as \ill{}','The terminal crossed-angle compatibility sign is distinct. Before it survive crossed diagonals and a long lower stroke, compatible with X≤, but their overlap prevents certainty.','opening','low',True,'retained')
row(5,'opening relation description','relation réflexive sym','relation réflexive symétrique','relation réflexive sym',False,True,'abbreviation expanded or spelling modernised','After réflexive there is only the short sym cluster followed by the closing parenthesis; no étrique is written.')
row(6,'cancelled a-clause initial quantifier',r'\deleted{\unsure{\forall x\in M} ...}',r'\struck{\ill{}}',r'\deleted{\unsure{\forall x\in M} ...}',False,True,r'readable ink left as \ill{}','The old line begins with a V-shaped quantifier, a small cross, a membership-like loop and the two high strokes of M. These remain partly crossed by the long cancellation.','cancel_a','low',True,'retained')
row(7,'interlinear word in cancelled a-clause',r'\inserted{\unsure{posant}}','inserted pour, attached to the live replacement',r'\deleted{...\inserted{posant}...}',True,True,'insertion or placement','The word above the cancelled formula begins with a descending p and rounded o, continues through compressed low strokes and ends at a tall t. It is posant, not pour, and belongs to the abandoned set-definition line.','cancel_a','medium',False,'resolved')
row(8,'cancelled a-clause set definition',r'\widetilde X=\{y\in M\mid y\leq x\}',r'\struck{\ill{}}',r'cancelled \widetilde X=\{y\in M\mid y\leq x\}',False,True,r'readable ink left as \ill{}','Under the oblique strike the tilde, X, equality, opening brace, y, membership, M, separator, second y, inequality, small final x and closing brace can all be followed.','cancel_a','medium',True)
row(9,'end of cancelled a-clause',r'\unsure{être}',r'\ill{}',r'\deleted{\unsure{être}}',False,True,r'readable ink left as \ill{}','A short final run above the last brace has an upright crossed stroke and terminal e-like loop. Être is still tentative because the left part is densely crossed.','cancel_a','low',True,'retained')
row(10,'live fermée in a','baseline fermée','inserted fermée','baseline fermée',False,True,'insertion or placement','Fermée starts the next live line below Toute partie and follows the same baseline as majorée; it is not an interlinear replacement.')
row(11,'Phi after majorée',r'\unsure{\Phi|\varphi}','omitted',r'\unsure{\Phi|\varphi}',False,True,'omission','The oval with a central stem and turned lower foot is a separate mathematical letter between majorée and de. Capital Phi versus cursive varphi remains unresolved.','Phi','medium',False,'retained')
row(12,'cancelled symbol before réunion',r'\deleted{\unsure{$\exists$}}','omitted',r'\deleted{$\exists$}',True,True,'omission','Three leftward horizontal arms join a right upright, with a cancelling stroke extending across the form. This is an existential quantifier.','deleted_exists','high',False,'resolved')
row(13,'a final order index',r'M_{\leq x}',r'\mathcal M_{\leq X}',r'M_{\leq x}',False,True,'misread symbol or index','The final index is a short lowercase x, while the tilde X preceding the equality is substantially larger.')
row(14,'upper-left margin abbreviation','ens des parties','ens. des parties','ens des parties',False,True,'other','No point follows ens in the margin; the short group runs directly into a blank before des.','margin_top')
row(15,'upper-left margin after formées',r'\unsure{de|des} éléments',"d'éléments",r'\unsure{de|des} éléments',False,True,'misread word','A separate d/e-like group appears before éléments. There is no raised apostrophe; its small final hook does not settle whether an s follows.','margin_top','medium',False,'retained')
row(16,'b final punctuation','period','exclamation mark','period',False,True,'other','The prime belongs to Y′; a separate low point follows it. No additional upright of an exclamation mark appears.')
row(17,'At3 first pair',r'F,\unsure{G|C}','F,G','F,G',True,False,'misread symbol or index','The lower end of the second capital has an inward step and a short returning terminal stroke, supporting G rather than a bare C.','At3_G','medium',False,'resolved')
row(18,'At3 erased small variable',r'\deleted{\unsure{x}}','omitted',r'\deleted{\unsure{x}}',False,True,'omission','Immediately above the large live X are small intersecting strokes crossed by an additional diagonal. Lowercase x remains the tentative reading.','At3_x','low',False,'retained')
row(19,'At3 left-margin emphasis','compatibilité and par strates underlined','no emphasis marked','compatibilité and par strates underlined',False,True,'other','Two distinct rules follow compatibilité and par strates; Critère de lies outside those rules.')
row(20,'transition cancelled opening',r'\deleted{\unsure{At}}',r'\struck{At}',r'\deleted{At}',True,False,'misread word','An A-shaped pair of legs and the adjacent t stem/crossbar remain legible inside the cancellation.','transition_At','medium',False,'resolved')
row(21,'transition detached mark',r'\unsure{1}','omitted',r'\unsure{1}',False,True,'omission','A detached near-vertical stroke follows the sentence at some distance from its terminal point. It may be a numeral 1 but has no secure linguistic function.','transition1','low',False,'retained')
row(22,'At4 second initial variable',r'\unsure{c|G}','G',r'\unsure{c|G}',False,True,'misread symbol or index','The second letter is noticeably lower than F and is an open c-shaped curve ending in a short downward touch. A cramped G cannot be ruled out.','At4_c','medium',False,'retained')
row(23,'At4 left-margin rules','raffinement, par strates, Corollaire underlined','no emphasis marked','raffinement, par strates, Corollaire underlined',False,True,'other','The three separate underlines are present in the slanted margin; the surrounding brackets also remain.')
row(24,'small arrow beside corollary bracket','omitted','omitted','small northeast-pointing arrow beside the bracket',True,True,'drawing or diagram','A short doubled diagonal shaft with an arrowhead rises beside the bottom of the corollary bracket, separate from the longer arrow by the following axiom.',None,'medium')
row(25,'Ramène line',r'\inserted{Ramène la connaissance ...}',r'\uncertain{Ramène} la connaissance ... as ordinary prose',r'\inserted{Ramène la connaissance ...}',False,True,'insertion or placement','The line is an added explanatory annotation beneath the equivalence. Ramène is readable with a large capital R and a tall middle stroke; the following order relation carries M below it.',None,'high',True)
row(26,'first corrected axiom old numeral',r'\deleted{\unsure{5}}','5 mentioned only in an editorial note',r'\deleted{\unsure{5}}',False,True,'omission','A separate short middle horizontal and a small older loop survive beneath the heavier new digit. A former 5 remains plausible.','At6number','low',True,'retained')
row(27,'first corrected axiom live numeral',r'\unsure{6|5}','6','6',True,False,'misread symbol or index','The new digit has a long curving upper descent ending in a closed low loop, the form of 6.','At6number','high',False,'resolved')
row(28,'At6 opening quantifier','live ∀',r'\struck{\forall}',r'\deleted{\forall}',True,False,'deletion state (struck given live or live given struck)','Two extra oblique strokes cross the upper arms of the otherwise recognizable inverted-A quantifier; X,F immediately after it remain live.','At6_hypothesis','medium')
row(29,'At6 overwritten relation in set',r'\deleted{\unsure{\leq}}\ll','≪ only',r'\deleted{\unsure{\leq}}\ll',False,True,'omission','Several lower strokes survive behind the two heavy live angle vertices. An earlier ≤ is possible, but the overstrike does not expose a complete independent equality bar.','At6rel','low',False,'retained')
row(30,'At6 second exponent and notation exponent',r'F^{x};\ \widetilde Y^{x}',r'F^{X};\ \widetilde Y^{X}',r'F^{x};\ \widetilde Y^{x}',False,True,'misread symbol or index','The second F exponent and the notation exponent are small crossed cursive x forms. The first defining F exponent is the taller X. The visible case alternation is retained.','Fexp','medium')
row(31,'At6 punctuation','i.e without final point; comma after closing set; Alors','i.e.; period after closing set; Alors','i.e without final point; comma after closing set; Alors',False,True,'other','There is no point after the e in the parenthetical gloss. The set is followed by a low comma, and the next line starts capital Alors.')
row(32,'At6 marginal arrow','simple northeast arrow','arrow omitted','long slightly curved rightward/upward arrow reproduced in TikZ',True,True,'drawing or diagram','The arrow above the axiom label has a long curved shaft and a distinct rightward arrowhead. It is separate from the small arrow beside the previous corollary bracket.',None,'high')
row(33,'Notation heading','no underline','emphasized','no underline',False,True,'other','There is no rule beneath Notation, unlike the axiom labels and the phrase raffinement interne.')
row(34,'notation equivalence abbreviation',r'\unsure{defn|défn}','déf',r'\unsure{dfn|defn}',True,True,'abbreviation expanded or spelling modernised','The visible forms are a looped d, a tall f and a low n-like shoulder. No independent e loop or accent can be isolated. Dfn is first; a fully compressed e remains possible.','notation_label','medium',False,'changed')
row(35,'notation final descriptive phrase','X raffinement interne de Y','dash before X supplied','X raffinement interne de Y',False,True,'text not on the page','The phrase begins with X on its own baseline; no dash precedes it.')
row(36,'At5 margin initial capitals',r'\unsure{G,H}','G,H','G,H',True,False,'misread symbol or index','Rotation separates a rounded G with a return, a comma, and an H with two uprights. Their inconsistency with the later F,G formula is retained.','lower_margins','medium',False,'resolved','The note begins G,H but later uses F and G; it is not regularized.')
row(37,'At5 margin erased centre',r'\deleted{\illegible{2}}',r'\ill{} without separate deletion rendering',r'\deleted{\illegible{2}}',False,True,'deletion state (struck given live or live given struck)','The block below Si G,H is crossed by dense horizontal and diagonal ink; isolated stems survive but neither complete words nor their division can be recovered.','lower_margins','low',True,'retained')
row(38,'At5 margin complete prose','équivaut à : Si ... sont des sous-figures d’une figure F, alors',r'équivalent à : si ... [ill.] des figures [ill.] [ill.]','équivaut à : Si ... sont des sous-figures d’une figure F, alors',False,True,r'readable ink left as \ill{}','The rotated note gives équivaut ending in a tall t, then sont des, and the next lines give d’une figure F and alors. H’s missing phrases are visible.','lower_margins','medium',True)
row(39,'At5 margin object word',r'\unsure{sous-figures|strates}','figures with unread surroundings','sous-figures',True,True,'misread word','The phrase has a low sous group, a short separating stroke, and a following tall f with the g descender and the remaining figures sequence. It is longer and differently structured than strates.','lower_margins','medium',True,'resolved')
row(40,'At5 margin equivalence','F≪G ⇔ F≤G','F≪G ⇒ F≤G','F≪G ⇔ F≤G',False,True,'misread symbol or index','The central double-stroked connector has an arrowhead at each end, not only at the right.','lower_margins','high')
row(41,'At5 margin criterion adjective',r'\unsure{intrinsèq.|intrinsèque|des strates}',r'\uncertain{autonomes}',r'\unsure{extrinsèq.|intrinsèq.|intrinsèque}',True,True,'misread word','The first cluster after raffinement is a thick loop and crossing-like join, followed by a tall t and a narrow rinsèq-like run ending at a point. It looks more like ex- than in-, but the joining ink prevents certainty. Autonomes does not fit the tall t and middle sequence.','lower_margins','low',True,'changed')
row(42,'At5 criterion final noun',r'\unsure{figures|figure}','figures mentioned separately in editorial note','figures',True,True,'insertion or placement','The word at the far right of the slanted criterion has the f ascender, g loop and a distinct final s turn. It continues de figures from the margin across above the body’s Si.','lower_margins','medium',False,'resolved')
row(43,'At5 criterion parentheses','criterion followed by period','no parentheses transcribed','parentheses around the underlined criterion; no added terminal period',True,True,'other','An opening curve precedes the C of Critère and a separate closing curve follows the displaced final figures. The point before de belongs to the abbreviated adjective, not a final sentence stop.','lower_margins','medium')
row(44,'At5 marginal leader with endpoint','large curved connector and crossing stroke only','connection described but not drawn','large connector plus separate thin leader ending at a small hollow quadrilateral',True,True,'drawing or diagram','Besides the large curved enclosure, a thin line rises from the note and ends at a small outlined four-sided mark above the axiom label. This distinct line/endpoint is added to the TikZ drawing.','lower_margins','medium')
row(45,'second corrected axiom old numeral',r'\deleted{\unsure{6}}','old 6 described in editorial note',r'\deleted{\unsure{6}}',False,True,'omission','An older low rounded loop is visible inside the strongly retraced current numeral. It supports a tentative 6, but too much is covered for certainty.','At5number','low',True,'retained')
row(46,'second corrected axiom live numeral',r'\unsure{5|6}','5','5',True,False,'misread symbol or index','The current top has an extended upper bar and the lower part turns through the rounded belly of a 5.','At5number','medium',False,'resolved')
row(47,'At5 implication hypothesis relation',r'\unsure{\ll|\leqslant}',r'\ll',r'\ll',True,False,'misread symbol or index','Two independent upper diagonals descend to two separate left vertices, each with its own lower arm. The lower arms are nearly horizontal, but the doubled angles make ≪ clear.','At5rel','high',False,'resolved')
row(48,'two restatements after At5','ou encore, dans un ...; ou encore, si ...','on en conclut, dans une ...; uncertain ou encore','ou encore, dans un ...; ou encore, si ...',False,True,'misread word','Both starts have the short ou followed by encore; the first article is un without a final e. Neither the extra en nor the distinct word conclut appears.',None,'high',True)
row(49,'third corrected axiom old numeral',r'\deleted{\unsure{6}}','old numeral not read',r'\deleted{\unsure{6}}',False,True,'omission','The low rounded remains are heavily filled by the later stroke. The older 6 remains tentative.','At7number','low',True,'retained')
row(50,'third corrected axiom live numeral',r'\unsure{7|6}','7','7',True,False,'misread symbol or index','A long upper bar and a strongly descending oblique/right stem identify the new 7; the lower heavy lump belongs to the overwriting.','At7number','medium',False,'resolved')
row(51,'At7 middle upper mark',r'\unsure{\bullet|\circ}',r'\circ',r'\bullet',True,True,'misread symbol or index','The middle mark is a filled dark dot. Its first and third neighbours have readily visible white centres, so the literal fill distinction is retained.','At7dots','high',False,'resolved')
row(52,'At7 minute marks after middle relation','omitted','omitted',r'\unsure{:}',True,True,'omission','Two small detached dots lie to the right of the middle doubled angle, one above the other on a slight slant. They may be a colon or incidental ink; the doubtful colon records their presence.','At7dots','low',False,'not applicable','No logical punctuation is inferred from these dots; their function is unresolved.')
row(53,'At7 margin','Transitivité du raffinement interne','Transitivité des raffinements intérieurs','Transitivité du raffinement interne',False,True,'misread word','The rotated note has singular du, a single raffinement and the final word interne. Only Transitivité is underlined; the rounded connector around the axiom label is also reproduced.','lower_margins','high')
row(54,'AtM label rules','At underlined, M below, following numerals','roman At with subscript M','At underlined, M below, following numerals',False,True,'other','Each label has a short rule directly beneath At, with M placed below/right and the numeral to the right. The underlines are visible for all four labels.')
row(55,'AtM2 overstrike',r'\Psi\ \deleted{\unsure{pa}}partie',r'\struck{toute partie}\add{\Psi} fermée',r'\Psi\ \deleted{\unsure{pa}}partie',False,True,'deletion state (struck given live or live given struck)','Psi is live on the baseline. The cancellation is concentrated in the opening p/a strokes of partie; the r/t/i/e ending and following fermée remain live. There is no separate readable toute.','AtM2delete','low',False,'retained')
row(56,'AtM2 closure relation',r'\unsure{<|\leq}',r'\leq','<',True,True,'misread symbol or index','The relation has one upper diagonal turning into a lower arm. The dark lower touch belongs to that angle; there is no separate parallel equality stroke.','AtM2rel','medium',False,'resolved')
row(57,'AtM3 cancelled group',r'\deleted{\unsure{\{X,Y\}}}',r'\struck{\ill{}}',r'\deleted{\{X,Y\}}',True,True,r'readable ink left as \ill{}','Both curly braces are visible. Between them, the crossed X strokes, comma and Y fork remain distinct beneath the diagonal strikes.','AtM3deleted','medium',True,'resolved')
row(58,'AtM3 existential witness and repeated letter',r'\exists\Phi′;\ X,Y\in\Phi′',r'\exists\Phi;\ X,Y\in\Phi',r'\exists\Phi′;\ X,Y\in\unsure{\Phi′|\Phi}',True,True,'misread symbol or index','The existential Phi carries a small detached upper-right stroke. Near the repeated Phi the nearby upper trace is harder to separate from the preceding line; the prime is retained first but now explicitly doubtful.','AtM3phi','medium')
row(59,'AtM3 final union annotation',r'\Phi\overset{M}{\cup}\Psi',r'\Phi\cup\Psi; editorial note says compatibility has M below',r'\Phi\overset{M}{\cup}\Psi',False,True,'misread symbol or index','The small M is above the rounded cup-shaped union, not below the preceding compatibility sign. The compatibility statement and the parenthetical union condition are separate.')

A=[
 ('mathscr F|mathcal F','opening','retained',1),
 ('M|mathcal M','opening','retained',2),
 ('deleted X≤','opening','retained',4),
 ('deleted forall x in M','a cancelled start','retained',6),
 ('inserted posant','a cancelled line','resolved: posant',7),
 ('deleted être','a cancelled end','retained',9),
 ('Phi|varphi','a live clause','retained',11),
 ('deleted exists','before réunion','resolved: exists',12),
 ('de|des','top margin','retained',15),
 ('G|C','At3 initial pair','resolved: G',17),
 ('deleted x','At3 above X','retained',18),
 ('deleted At','transition','resolved: At',20),
 ('1','transition end','retained',21),
 ('c|G','At4 initial pair','retained',22),
 ('old 5','At6 label','retained',26),
 ('live 6|5','At6 label','resolved: 6',27),
 ('deleted ≤','At6 set','retained',29),
 ('defn|défn','notation label','changed: dfn|defn',34),
 ('G,H','At5 margin','resolved: G,H',36),
 ('illegible 2','At5 margin deleted centre','retained',37),
 ('sous-figures|strates','At5 margin','resolved: sous-figures',39),
 ('intrinsèq.|intrinsèque|des strates','At5 criterion','changed: extrinsèq.|intrinsèq.|intrinsèque',41),
 ('figures|figure','At5 criterion final word','resolved: figures',42),
 ('old 6','At5 label','retained',45),
 ('live 5|6','At5 label','resolved: 5',46),
 ('ll|leqslant','At5 hypothesis relation','resolved: ll',47),
 ('old 6','At7 label','retained',49),
 ('live 7|6','At7 label','resolved: 7',50),
 ('bullet|circ','At7 middle upper mark','resolved: bullet',51),
 ('deleted pa','AtM2','retained',55),
 ('<|≤','AtM2 closure relation','resolved: <',56),
 ('deleted {X,Y}','AtM3','resolved: {X,Y}',57),
]
byid={int(x['id'].rsplit('-',1)[1]):x for x in D}
audit=[dict(C_reading=a,place=b,status=c,evidence=byid[n]['evidence'],crop=byid[n]['crop'],crop_coordinates=byid[n]['crop_coordinates'],difference_id=byid[n]['id']) for a,b,c,n in A]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

s_audit=dict(row_id='SA21-K7-01', source='source/SP35_CW_156-7_sweep3/readings/156-7_CORRECTIONS.tsv',
 S_literal_report='At6 writes X triangleleft F, glossed X in tilde F; F^X then has a least element.',
 S_corrected_claim='The hypothesis is X≪F; the written version follows from At5. S also cites scan007.',
 literal_decision='Confirmed: the ink is X triangleleft F, with a single closed triangular sign and the explicit gloss X∈tilde F. The quantifier before X,F is struck.',
 outcome='Partial confirmation: S’s literal report and redundancy diagnosis are confirmed. X≪F is treated as a mathematical emendation, not as the ink reading, and is not substituted into the transcription. The intention of that complete amended axiom is not independently established from the pages read so far.',
 evidence='The hypothesis crop has one closed left-pointing triangle between X and F, whereas ≪ elsewhere has two open angle vertices. The parenthetical X∈tilde F is fully legible and reinforces the literal stratum hypothesis.',
 crop='readers/R2/crops/scan006_At6_hypothesis.png',
 mathematical_check='Using AtM0 and At5 on this page, X is itself in F^X by reflexivity. Every Y in F^X is compatible with X because both are strata of F; At5 yields X≤Y. Thus X is the least member.',
 emendation_limit='Replacing only triangleleft by ≪ also removes the explicit guarantee that X is a multistratum. Since the written quantification names X,F in the figure set, the complete intended restriction on X requires care. S’s cited scan007 and later pages were not opened.',
 confidence='high for literal sign and redundancy; proposed authorial intention not settled')

data=dict(reader='R2',scan=6,start_utc='2026-11-19 21:45:06 UTC',end_utc=end,
 model='GPT-6 Astra Pro; inherited effort setting not exposed; R2',
 images_viewed=['H156-01_156-7_scan006.jpg','H156-01_156-7_scan006_a.jpg','H156-01_156-7_scan006_b.jpg']+[x['file'] for x in m],
 coverage=[
  'page number 5; full opening order/compatibility data, cancelled group and literal abbreviation sym',
  'entire abandoned clause a including quantified variables, inserted posant, set definition and doubtful être',
  'live finite-type condition, Phi, erased existential quantifier, lower-case order index; full top-left characterization note',
  'compatibility monotonicity in b and terminal punctuation',
  'At3 complete formula, tiny variable cancellation, initial G and slanted compatibility criterion',
  'transition cancelled At, sentence, terminal detached vertical mark',
  'At4 full stratum criterion, low c/G, inserted Ramène gloss, corollary and both nearby arrows',
  'At6 corrected numbering, crossed quantifier, literal triangleleft hypothesis and membership gloss, set overstrike, two exponent forms, least-element conclusion',
  'Notation, dfn/defn label, literal X as least element, lower-case x exponent, i.e. implication, Omb(Y) circle and underlined internal refinement',
  'At5 complete rotated margin with G,H, erased centre, sous-figures, F/G mismatch, equivalence, uncertain extrinsèq., displaced figures, parenthesis traces and complete connector drawing',
  'At5 corrected label and double-angle relation, two ou encore restatements with literal un and F,G∈M',
  'At7 corrected label, open/solid/open upper marks, two possible punctuation dots, full transitivity margin and connector',
  'Traduction heading and all AtM0–3 rows, label underlines, Greek letters, overstrike, strict less-than mark, erased braced pair, primes and M-over-union annotation',
  'S correction SA21-K7-01 checked against the actual At6 hypothesis; no later manuscript pages or external research used'],
 notation=[
  dict(form='figure-set and M alphabets',reading='mathscr F|mathcal F; M|mathcal M',evidence='same recurring cursive forms as earlier pages; Gothic not supported'),
  dict(form='compatibility',reading='crossed-angle sign',evidence='same six-ended sign throughout; custom TikZ retained'),
  dict(form='stratum versus refinement',reading='triangleleft in the At6 hypothesis; ll in the selected-stratum condition',evidence='closed triangle differs visibly from two open angles'),
  dict(form='corrected numbering',reading='live 6,5,7; old 5,6,6 remain doubtful',evidence='current upper/lower strokes separate sufficiently for live values, not old values'),
  dict(form='internal refinement marks',reading='open circles in first/last positions of At7; solid dot in middle',evidence='literal fill difference, not regularized'),
  dict(form='definition label',reading='dfn|defn',evidence='d, f and n separable; e not secure; no accent'),
  dict(form='exponents',reading='first F^X, subsequent F^x and tilde Y^x',evidence='small cursive forms retained without case harmonization'),
  dict(form='AtM2 relation',reading='<',evidence='one angular shape, no separate equality bar'),
  dict(form='final union',reading='cup with M above',evidence='M is spatially over the union, not below compatibility')],
 math_notes=[
  dict(type='summary, not proof check',text='Continues the finite-type order reconstruction using a hereditary compatibility relation and finitely generated bounded closed subsets. At3 is a stratum criterion for compatibility; At4 reduces refinement to strata. The remaining numbered assertions concern a least refining stratum, the coincidence of refinement and inclusion on compatible strata, and transitivity of internal refinement.'),
  dict(type='targeted proof check',statement_id='R2-006-M1',text='The written At6 least-member claim is redundant under AtM0 and At5. From X triangleleft F one has X∈tilde F. Reflexivity and AtM0 give X≪X, hence X∈F^X. Any Y∈F^X shares upper bound F with X, so they are compatible; At5 turns X≪Y into X≤Y. Therefore X is the least member. This confirms the redundancy portion of S without changing the triangleleft ink.'),
  dict(type='unestablished emendation',text='S proposes X≪F in place of X triangleleft F. The actual triangle and the following membership gloss are unequivocal. Moreover the written X,F∈script F does not by itself say X∈M after that replacement. The full intended amended hypothesis is not certified from this page; the later page cited by S has not been read.'),
  dict(type='targeted local counterexample',statement_id='R2-006-M2',text='The Notation sentence literally says that X is the least element of tilde Y^x, while the following i.e. condition would make Y the unique member of that selected family. On a two-stratum chain a<b with refinement equal to inclusion, take X=a,Y=b. The selected family is {a,b}, whose least member is X=a, but Y′=a violates the displayed requirement Y′=Y. Thus the two local predicates are not equivalent under the natural reading of the family notation. The text remains X, without correction.'),
  dict(type='conditional refined statement',statement_id='R2-006-M3',text='With Y in place of X in the phrase naming the least member, the local equivalence holds: every candidate Z lies below Y because it is a stratum of Y; if Y is least, antisymmetry gives Z=Y. Conversely X≪Y together with the displayed universal equality makes the selected family the singleton {Y}. This is an editorial mathematical clarification, not a transcription change.'),
  dict(type='reading anomalies retained',text='The margin begins G,H but its formula uses F,G; At4 begins with a low c/G; AtM2 uses a strict less-than sign; At7 has a filled middle marker and two questionable extra dots. These were examined visually and were not regularized.')],
 author_qualifications=['avec figures de t.f.','Toute partie fermée majorée','On aura alors','Critère de compatibilité par strates','Corollaire F≤G⇒F≪G','ou encore'],
 author_explicit_verification_requests=[],
 unresolved=[dict(place=x['place'],reading=x['reading'],confidence=x['confidence']) for x in D if x['C_doubt_status'] in ('retained','changed')]+[
  dict(place='At7 right of middle relation',reading='possible colon from two dots; function unknown',confidence='low'),
  dict(place='AtM3 repeated witness',reading='Phi′|Phi',confidence='medium')],
 differences=D,C_doubt_audit=audit,S_audit=[s_audit],
 new_omissions_from_both=[
  dict(place='At4 corollary margin',reading='small separate northeast arrow',confidence='medium'),
  dict(place='At5 marginal criterion',reading='parentheses around criterion',confidence='medium'),
  dict(place='At5 connector',reading='separate thin leader and hollow four-sided endpoint absent from C drawing and not reproduced by H',confidence='medium'),
  dict(place='At7 middle relation',reading='two minute detached marks, represented as unsure colon',confidence='low')],
 crop_manifest='readers/R2/scan006_crops.json',
 check_events=[
  dict(statement_id='R2-006-M1',date=end,who='GPT-6 Astra Pro; inherited effort setting not exposed; R2',type='targeted proof check',outcome='Written At6 follows from AtM0 and At5; X is its least member. S’s redundancy diagnosis is confirmed.'),
  dict(statement_id='R2-006-M2',date=end,who='GPT-6 Astra Pro; inherited effort setting not exposed; R2',type='refuted, with the refined statement\'s id',refined_statement_id='R2-006-M3',outcome='Two-stratum-chain counterexample separates the literal X-least predicate from the subsequent i.e. predicate, under the natural selected-family reading.'),
  dict(statement_id='R2-006-M3',date=end,who='GPT-6 Astra Pro; inherited effort setting not exposed; R2',type='targeted proof check',outcome='The locally amended Y-least predicate is equivalent to the displayed i.e. predicate by antisymmetry; no text emendation was made.')])

(out/'scan006.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(out/'scan006.md').write_text('''# R2 — independent reading, scan 006

The whole image and both supplied halves were inspected once, followed by 25 distinct crops. Every one of the 32 C doubts has an individual decision, with evidence and a crop reference. C and H were compared in full. Only S row SA21-K7-01 was read; no later manuscript page or other reader/main decision was inspected.

## Literal readings

The live corrected axiom numbers read 6, 5, 7; the overwritten earlier numerals remain doubtful. At6 has a struck quantifier before X,F. Its hypothesis is unequivocally X triangleleft F, followed by X in tilde F. The following selected-stratum condition uses the double angle, with a doubtful older ≤ beneath it. The first defining exponent is X and the later exponents are small x forms. At5’s relation is clearly a doubled angle. AtM2’s closure relation is a literal <. AtM3 retains the prime on the existential witness, while the corresponding final prime is newly marked uncertain.

The At7 middle upper marker is solid, unlike its two open neighbours. Two minute marks just to the right of that relation are transcribed as an unsure colon; their function may instead be incidental ink. The abbreviated notation label looks dfn, with defn retained as an alternative because no independent e can be isolated.

The dense lower margin reads G,H and sous-figures; its final noun is figures. The difficult adjective is proposed as extrinsèq.|intrinsèq.|intrinsèque, with the ex- reading low confidence. Parentheses around the criterion and a separate leader with a hollow endpoint are included. The full note and its final word extend above the body’s Si. The bottom margin reads Transitivité du raffinement interne, singular.

## S row and mathematics

S correctly reports the literal stratum hypothesis. Its claim that the written least-element assertion follows from At5 can be verified on this page: reflexivity and AtM0 put X in the selected set; compatibility of two strata of F and At5 put X below every selected member. Thus X is already the least member.

S’s replacement by X≪F is an emendation, not the ink reading, and has not been substituted. The complete intended corrected hypothesis is not established here: replacing only the triangle also removes the explicit guarantee that X is a multistratum, since the displayed quantification otherwise merely names X,F in the figure set. S’s cited later page was not read.

The Notation passage has a second literal mismatch: it names X as the least element of tilde Y^x, whereas its ensuing i.e. condition characterizes Y as the least/unique candidate. A two-stratum-chain counterexample to the literal local equivalence, and the conditional corrected Y-least equivalence, are recorded as actual check events. The transcription keeps X.
''')
print(len(D),'difference rows;',len(A),'C doubts;',len(m),'crops')
print('C differences',sum(x['diff_C'] for x in D),'H differences',sum(x['diff_H'] for x in D))
