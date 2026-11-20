from pathlib import Path
from datetime import datetime, timezone
import json, csv
root=Path('/workspace/scratch/2b715fe259c4/SP35_CW_156-7/readers/R3')
src=Path('/workspace/scratch/2b715fe259c4/source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan008.tex')
s=src.read_text()
repl=[
(r"\inserted{avoir l'air de}",r'''\inserted{\tikz[baseline=(t.base),x=.6em,y=.6em]{\node[inner sep=0pt,anchor=west] (t) at (.15,.55) {avoir l'air de}; \draw (0,-.3)..controls(.1,.05)and(.6,.15)..(6.8,.25)..controls(7.0,.3)and(7.1,.45)..(7.1,.6);}}'''),
(r'\unsure{\mathrm{defn}|\mathrm{défn}}',r'\mathrm{dfn}'),
(r'\varnothing_{\unsure{\mathscr F|\mathcal F|F}}',r'\varnothing_F'),
(r'\unsure{M|\mathcal M}',r'M'),
(r'\deleted{\unsure{résultera}}\unsure{résulte|résultera}',r'résul\deleted{\illegible{1}}\unsure{te|tera}'),
(r'\inserted{précédents}',r'''\inserted{\tikz[baseline=(t.base),x=.6em,y=.6em]{\node[inner sep=0pt,anchor=west] (t) at (.1,.55) {précédents}; \draw (1.2,-.4)..controls(1.3,.05)and(2.4,.15)..(5.6,.35)..controls(6.1,.38)and(6.3,.48)..(6.4,.68);}}'''),
(r'\unsure{i.e.}',r'i.e.'),
(r'\uline{spacieux}',r'\uline{\unsure{spacieux|specieux}}'),
(r'\uline{Axiome des ateliers spacieux}',r'\uline{Axiome des ateliers \unsure{spacieux|specieux}}'),
(r'\unsure{Soient}',r'Soient'),
(r'\inserted{\unsure{soit}}',r'\inserted{soit}'),
(r'\deleted{\unsure{\forall}}',r'\deleted{\forall}'),
(r'\unsure{\widetilde F|F}',r'\unsure{F|\widetilde F}'),
(r'\unsure{Y|y}',r'Y'),
]
for a,b in repl:
 if a not in s: raise SystemExit('Missing replacement '+a)
 s=s.replace(a,b,1)
s=s.replace('(\\uline{NB} Il', '% The shared prefix résul- is clear. Only the t/ending cluster is overwritten; the former terminal group cannot be independently recovered. The surviving ending favors te.\n% The curved stroke beneath précédents descends into the axiomes / que gap: an insertion guide, not an underline.\n(\\uline{NB} Il',1)
s=s.replace('% slanted', '% The marginal note is slanted. A long diagonal of the general cancellation intersects its lower/right portion; no separate note-only cancellation is established.\n% Three long diagonals cancel the following At DC 1 and Cor draft as a block; the outer deleted macros record that state, distinct from the earlier local cancellations.\n% slanted',1)
(root/'scan008.tex').write_text(s)
manifest=json.loads((root/'scan008_crops.json').read_text()); cm={Path(x['file']).stem:x for x in manifest}
rows=[];aud=[]
def add(place,C,H,reading,evidence,kind='other',conf='high',crop=None,dc=False,dh=True,marked=False,doubt='not applicable',math=None):
 ident=f'R3-008-{len(rows)+1:02}'
 rows.append(dict(id=ident,place=place,C=C,H=H,reading=reading,diff_C=dc,diff_H=dh,kind=kind,marked_in_H=marked,confidence=conf,evidence=evidence,crop=('readers/R3/crops/'+crop+'.png') if crop else None,crop_coordinates=cm[crop]['box'] if crop else None,C_doubt_status=doubt,math_consequence=math))
 return ident
def audit(n,place,C,reading,status,evidence,crop,ident):
 aud.append(dict(number=n,place=place,C=C,reading=reading,status=status,evidence=evidence,crop=('readers/R3/crops/'+crop+'.png') if crop else None,crop_coordinates=cm[crop]['box'] if crop else None,difference_id=ident))
def da(n,place,C,H,reading,evidence,crop,dc=False,dh=True,conf='medium',status='retained',kind='other',marked=False,math=None):
 ident=add(place,C,H,reading,evidence,kind,conf,crop,dc,dh,marked,status,math)
 audit(n,place,C,reading,status,evidence,crop,ident)
 return ident
add('opening insertion and anchor',r'\inserted{avoir l’air de} before les en faire dépendre; guide not drawn',r'\add{\uncertain{moins élégants}} after disjonction-compatibilité; no avoir l’air de',r'\inserted{avoir l’air de}, before les en faire dépendre, with curved guide', 'The small raised phrase reads avoir l’air de. Its guide bends toward the gap before les; there is no moins élégants phrase after disjonction-compatibilité. The phrase and guide were clear in the upper supplied half.','insertion or placement',dc=True,marked=True)
add('paired quotes, opening two paragraphs','two backticks/two apostrophes','guillemets','two backticks/two apostrophes around facultatifs and F et G disjoints','Each side consists of two short raised strokes, with no chevron-shaped guillemet.','other')
da(1,'before implications',r'\unsure{des\'|des|d\'}',"d'implications",r"\unsure{des'|des|d'}",'The joined low run after the initial d has an angular terminal hook and is followed by a separate upright raised tick. The middle letters remain compressed; the separate tick is not a reason to normalize the word to d\'.','008_des',conf='low',kind='misread word')
add('disjointness noun phrase','disjoints','disjointes','disjoints','The ending after the tall t is a final s-like exit; no separate e precedes that terminal s. Underlining belongs to disjoints.','misread word')
da(2,'definition label above first equivalence',r'\unsure{\mathrm{defn}|\mathrm{défn}}',r'\mathrm{déf}',r'\mathrm{dfn}','The small label has a looped d, a tall crossed/descending f and a low n run. No distinct e or acute is visible. This continues the literal dfn form read on006 and007.','008_defn',dc=True,status='resolved',conf='high',kind='abbreviation expanded or spelling modernised')
da(3,'empty-set subscript in first display',r'\unsure{\mathscr F|\mathcal F|F}',r'\mathfrak F','F','The enlarged subscript is a simple upright stem with a short top arm and one middle arm. There is no additional script loop or Gothic construction.','008_empty_index',dc=True,status='resolved',conf='high',kind='misread symbol or index',math='Literal alphabet change only; no proposed change of the designated figure family.')
add('introduction to second display','On a d’ailleurs','On a d’autre part','On a d’ailleurs','After d’ the joined run has the a/ill configuration and the final eurs, rather than the separated words autre part.','misread word')
add('transition after second display','donc interprétation','d’où interprétation','donc interprétation','The opening word ends in a small c-shaped hook and has no apostrophe or accent on an ou group.','misread word')
da(4,'interprétation en termes',r'\unsure{termes|terme}','termes',r'\unsure{termes|terme}','The final e/s-like run is almost horizontal, with a small rising hook before the exit. It does not separate the plural s securely from an elongated terminal e.','008_termes',conf='medium')
da(5,'M after dans and its notation on this page',r'\unsure{M|\mathcal M}',r'\mathcal M','M','The letter consists of a rising left stroke, a rounded valley and a tall right stem. It has no added calligraphic flourish. The M beneath the two middle relation signs and in the lower quantifiers is likewise the ordinary manuscript capital.','008_M',dc=True,status='resolved',conf='medium',kind='misread symbol or index')
add('middle display, pas','n’est underlined pas','n’est pas without emphasis','n’est underlined pas','A discrete horizontal underline runs beneath pas.','omission')
add('middle display, restatement punctuation','minoré dans M,≤; then new line i.e. without an added comma','minoré dans M,≤, i.e.','minoré dans M,≤; then i.e.','The restatement starts on its own manuscript line; the line ending after ≤ has no additional comma.','text not on the page')
add('NB label',r'\uline{NB}','NB without emphasis',r'\uline{NB}','A short rule is drawn directly beneath the two capitals.','omission')
verb_evidence='The shared prefix résul- remains clear and is not struck as a separate whole word. Overwriting is concentrated on the tall t stroke and the final e/ending cluster: dark retracing crosses the t junction, with small upper/right loops and a thick lower exit. Those loops do not yield an independently legible earlier tera sequence. The live terminal run favors te, but tera remains possible.'
verb_id=add('NB first verb, shared prefix and overwritten terminal cluster',r'\deleted{\unsure{résultera}}\unsure{résulte|résultera}','résultera with no overwritten layer',r'résul\deleted{\illegible{1}}\unsure{te|tera}',verb_evidence,'deletion state (struck given live or live given struck)','low','008_NB_verb',True,True,False,'changed',None)
audit(6,'NB first verb, old terminal layer',r'\deleted{\unsure{résultera}}',r'shared résul-; \deleted{\illegible{1}} only at the ending','changed',verb_evidence,'008_NB_verb',verb_id)
audit(7,'NB first verb, surviving form',r'\unsure{résulte|résultera}',r'résul- + \unsure{te|tera}','retained',verb_evidence,'008_NB_verb',verb_id)
add('NB précédents insertion guide',r'\inserted{précédents}, guide not drawn',r'\add{précédents}, guide not drawn',r'\inserted{précédents} above the gap after axiomes; curved guide reproduced','The curved line runs beneath the raised word, bends down at its left end into the gap after axiomes and before que, and rises at the right. It is an insertion guide, not an ordinary straight underline under précédents.','drawing or diagram',crop='008_NB_precedents',dc=True)
add('NB predicate after que',r'ça implique',r'\ill{} \uncertain{indique}',r'ça implique','Ça is a short cedilla-bearing group; implique has the tall/descending p and a separate l. No d stem occurs in the position required for indique.','readable ink left as \\ill{}',marked=True)
da(8,'NB cancelled shorthand',r'\unsure{i.e.}','i.e.','i.e.','The i upright, following dot, small e loop and final point can be distinguished beneath the long cancellation rule.','008_NB_strike',dc=True,dh=False,status='resolved',conf='high')
add('NB cancelled words after i.e.',r'c’est un',r'\ill{}',r'c’est un','The c opening, apostrophe, low e/s run and tall t are followed by the low u/n run. The heavy horizontal stroke is cancellation, not the wording.','readable ink left as \\ill{}',conf='medium',crop='008_NB_strike',marked=True)
da(9,'NB cancelled final quantifier',r'\unsure{\exists}',r'\ill{}',r'\unsure{\exists}','A right-hand upright and leftward upper/lower arms suggest the reversed E. The cancellation rule hides the middle; the complete earlier sign cannot be certified.','008_NB_strike',conf='low',kind='readable ink left as \\ill{}',marked=True)
da(10,'NB article before réciproque',r'\deleted{\unsure{la}}','live la',r'\deleted{\unsure{la}}','The initial l-like loop is visible, but a dense horizontal black run covers the short following body. The local cancellation is distinct from the later general diagonal strikes.','008_NB_article',conf='low',kind='deletion state (struck given live or live given struck)')
add('NB second future verb','résultera',r'\uncertain{résultera}','résultera','The second word has a clear r/é/s/u/l/t sequence followed by two separated low terminal turns, unlike the overwritten first verb.','other',crop='008_NB_end',marked=True)
da(11,'NB d’axiome at right edge',r'\unsure{d\'axiome|d\'axiomes}',"d'axiome",r"\unsure{d'axiome|d'axiomes}",'The visible letters run through d’axiome and into the dark scan edge. No independent final s is secured; a clipped terminal s cannot be excluded.','008_NB_end',conf='low')
add('lower draft, cancellation scope','At DC1 and Cor text marked deleted','inline live text; note acknowledges three long diagonal strikes','The full At DC1 and Cor draft is cancelled; earlier local cancellations remain separately nested','Three thin diagonal strokes extend across the lower draft. Their scope includes the heading, conditions and corollary, not merely the individual words physically intersected. H’s prose note recognizes them but its text is given live.','deletion state (struck given live or live given struck)',marked=True)
add('At DC1 label underline','At DC underlined, numeral1 outside','At DC1 emphasized as one unit','At DC underlined, numeral1 outside','The short rule belongs under the letters At DC; the following numeral stands beyond its right end.','other')
add('At DC title adjective','spacieux','spécieux',r'\unsure{spacieux|specieux}','The first vowel after p is a compressed open angular curve. It can be an open a or a small e; no acute accent appears above it. The following c/i/e/u/x run is clear.','misread word',conf='low',crop='008_DC_title',dc=True)
da(12,'At DC Soient',r'\unsure{Soient}','Soient','Soient','The capital S and low o, dotted i, e/n run and tall t are all recoverable. A thin diagonal crosses the middle but does not obscure the word.','008_DC_Soient',dc=True,dh=False,status='resolved',conf='high')
da(13,'At DC insertion before cancelled et and K',r'\inserted{\unsure{soit}}',r'\add{K}; no soit',r'\inserted{soit}; K is base-line text','The raised word has s, rounded o, i dot and tall t, just above and before the cancelled short group. K follows on the main line and is not itself the inserted material.','008_DC_soitet',dc=True,status='resolved',conf='high',kind='insertion or placement')
da(14,'At DC cancelled conjunction before K',r'\deleted{\unsure{et}}','omitted',r'\deleted{\unsure{et}}','A short hooked beginning and right-hand loop survive within a thick horizontal cancellation. They allow et, but the cover prevents a secure recovery of both letters.','008_DC_soitet',conf='low',kind='omission')
da(15,'At DC cancelled word before Supposons',r'\deleted{\unsure{Il}}','omitted',r'\deleted{\unsure{Il}}','The small old group is a dark upright/loop with a lower leftward tail. Il is possible, but its two component letters cannot be fully separated from the retracing.','008_DC_Ilpour',conf='low',kind='omission')
add('At DC raised quantifier phrase',r'\inserted{pour X\prime,Y\prime\in M}',r'pour \add{tous} X\prime,Y\prime\in\mathcal M',r'\inserted{pour X\prime,Y\prime\in M}, without tous','The whole phrase sits below the Supposons que line as an insertion. The word after pour is immediately X′; no tous group stands between them. Both primes and the membership sign are visible.','insertion or placement',crop='008_DC_Ilpour')
da(16,'At DC locally cancelled quantifier',r'\deleted{\unsure{\forall}}','an unread cancelled sign mentioned only in a note',r'\deleted{\forall}','The two converging arms and crossbar of an inverted A remain visible under the added diagonal/zigzag strokes. This is a locally cancelled ∀, independent of the later three general strikes.','008_DC_forall',dc=True,status='resolved',conf='medium',kind='omission',marked=True)
add('At DC concluding bracket, principal words','NB et alors seulement…',r'NB il \ill{} dans tous les cas…','NB et alors seulement…','The small et, the a/l/o/r/s run and the long seulement word can be followed. There is no separate dans tous les cas sequence.','misread word',marked=True)
add('At DC cf Cor insertion and punctuation',r'\inserted{cf Cor}',r'cf. Cor in base text, with placement noted separately',r'\inserted{cf Cor}, below the bracket, without a point after cf','The small cf Cor is tucked beneath the closing part of the bracket. The f exits directly toward Cor without a detached full stop.','insertion or placement',marked=True)
add('Cor family alphabet',r'\mathscr F',r'\mathfrak F',r'\mathscr F','The family letter is a looped manuscript script F with a flowing stem, not the angular Gothic form used by H.','misread symbol or index')
da(17,'Cor Sup, first older letter',r'\deleted{\unsure{\widetilde X|X}}','old layer omitted',r'\deleted{\unsure{\widetilde X|X}}','Diagonal crossing strokes remain beneath the F. They support X, but the mark above cannot be securely assigned to that earlier X rather than to the p of Sup or the later letter.','008_Cor_sup',conf='low',kind='omission')
da(18,'Cor Sup, surviving first letter',r'\unsure{\widetilde F|F}',r'\widetilde F',r'\unsure{F|\widetilde F}','The F stem and two arms are clear. The apparent wave above joins continuously into the descending p of Sup; no separate tilde can be isolated. Bare F is therefore the first ink reading, while a superposed/obscured tilde remains possible.','008_Cor_sup',dc=True,status='changed',conf='low',kind='misread symbol or index',math='The index as literally read may lack a tilde; it is not silently repaired to the expected figure-membership notation.')
da(19,'Cor Sup, older second letter',r'\deleted{\unsure{\widetilde Y|Y}}','old layer omitted',r'\deleted{\unsure{\widetilde Y|Y}}','A forked Y-like trace is enclosed by the later rounded G. The separate wave above G is clear, but its ownership in the earlier layer remains uncertain.','008_Cor_sup',conf='low',kind='omission')
add('Cor circled equivalence abbreviation','ses inside an oval','ssi, noted uncertain and circled','ses inside a horizontal oval','The middle letter closes into a small e loop. The final letter is an s curve, not a second i. The oval surrounds the whole three-letter abbreviation.','abbreviation expanded or spelling modernised',marked=True)
corvar_evidence='The older group has a closed lower loop and a shorter crossing stem, allowing φ or a looped y. The later letter has two high arms converging into a straight descending stem: uppercase Y. The old loop does not make the surviving capital a lowercase y.'
corvar_id=add('Cor quantified second variable and its older layer',r'\deleted{\unsure{\varphi|y}}\unsure{Y|y}','Y with old layer omitted',r'\deleted{\unsure{\varphi|y}}Y',corvar_evidence,'omission','medium','008_Cor_forall',True,True,False,'resolved/retained',None)
audit(20,'Cor older second variable',r'\deleted{\unsure{\varphi|y}}',r'\deleted{\unsure{\varphi|y}}','retained',corvar_evidence,'008_Cor_forall',corvar_id)
audit(21,'Cor surviving second variable',r'\unsure{Y|y}','Y','resolved',corvar_evidence,'008_Cor_forall',corvar_id)
add('Cor quantifier-line punctuation','no comma after M','comma after M','no comma after M','The quantified line ends at M; no separate comma is visible before the next displayed condition.','text not on the page')
add('Cor final display punctuation','no final point','final point','no final point','The final implication ends with Y, without a separate following point in the supplied half.','text not on the page')
add('margin adjective','spacieux','spécieux',r'\uline{\unsure{spacieux|specieux}}','The underlined adjective has the same compressed/open first vowel as in the heading. The following c/i/e/u/x is legible, but the first vowel does not safely distinguish a from e. No acute accent is visible.','misread word',conf='low',crop='008_margin',dc=True)
add('margin condition phrase','s’il satisfait cette condition.',r's’il satisfait \uncertain{cette} condition \ill{}','s’il satisfait cette condition.','The short cette has its tall double-t run and terminal e; condition follows as a continuous word. The long crossing line belongs to the general lower cancellation and does not supply an additional word after condition.','readable ink left as \\ill{}',crop='008_margin',marked=True)
add('margin counterexample abbreviation','Contre-ex. :',r'\uncertain{contre-ex.} :','Contre-ex. :','The initial capital C, the low on run, tall t, remaining re, dash, e/x and punctuation are visible after rotation.','other',crop='008_margin',marked=True)
add('margin example class','les ateliers simpliciaux…',r'les lieux \ill{} \ill{}…','les ateliers simpliciaux…','The first noun has the initial a/t and tall l/i stems of ateliers. Simpliciaux follows across the next run, with the long p/l strokes and final c/i/a/u/x ending. One long diagonal cuts the note but does not erase the readable letters.','readable ink left as \\ill{}',crop='008_margin',marked=True)

coverage=[
'Manuscript page7, opening paragraph in full: disjonction-compatibilité, actual avoir l’air de insertion and guide, two quote pairs, facultatifs, doubtful des′, and implications mutuelles with the final lieux.',
'Disjoints phrase and definition: uppercase F/G, underline, quote ticks, two-bar parallel glyph, three-letter dfn label over ⇔, crossed-angle compatibility glyph, et, intersection, equality, empty set and plain F subscript.',
'Order-only sentence, On a d’ailleurs, second equivalence, one initial ∀, uppercase X/Y, both tildes, comma positions and double bars; no silently added second quantifier.',
'Donc interprétation, retained termes/terme, plain M; complete three-line M-definition with M below both signs, braces, n’est pas and its underline, minoré, M,≤, i.e., nonexistence symbol and both lower-bound inequalities.',
'NB parentheses and underline; clear shared résul- and localized terminal overwrite; des axiomes and inserted précédents with curved guide; ça implique; second nonexistence, Z≪X and Z≪Y; full struck i.e. c’est un and doubtful reversed E; locally struck article; réciproque résultera; edge-truncated d’axiome(s); ci-dessous and ellipsis.',
'Slanted margin in full after one rotation: Un atelier sera dit, underlined uncertain adjective, s’il satisfait cette condition, Contre-ex. : les ateliers simpliciaux…, including the intersection by one general cancellation stroke.',
'Full cancelled At DC1 heading and underlines, parenthetic title, Soient X,Y∈M, inserted soit, old et, K=X∩Y and exact Sup index Z∈X̃∩Ỹ; old Il and Supposons que with inserted pour X′,Y′∈M.',
'At DC condition: locally cancelled ∀, all four prime-bearing antecedent variables, two refinement relations, two parallel relations to K, doubled implication, final X′∥Y′ and point; three overlaid general cancellation diagonals distinguished from relation bars.',
'At DC conclusion: Alors, bracketed NB et alors seulement…, inserted cf Cor below the bracket, uppercase X/Y and compatibility sign.',
'Full cancelled Cor statement: Soient F,G∈script F, K=F∩G, Sup, Z∈, older X and Y layers, surviving first F with uncertain tilde and surviving G with definite tilde; point.',
'Cor conclusion and lower condition: Alors F compatible G, oval around ses, ∀X and overwritten second variable now Y, membership and M; all four refinement/parallel antecedents and final two-shaft implication; no manufactured comma or terminal point.'
]
notation=[
{'symbol':'definition label','reading':'dfn','evidence':'Three connected letter bodies; no separate e or accent, as on scans006 and007.'},
{'symbol':'empty-set index','reading':'plain F','evidence':'Straight stem with two simple arms, without script flourish.'},
{'symbol':'M','reading':'ordinary cursive capital M throughout the page','evidence':'Two high stems and bowed join, without a distinct extra calligraphic construction.'},
{'symbol':'compatibility and disjointness','reading':'crossed-angle compatibility; two upright parallel bars','evidence':'Both lower formula crops distinguish the two bars from independent diagonal cancellation strokes.'},
{'symbol':'Sup indices','reading':'Z∈X̃∩Ỹ above; Z∈(oldX) F? ∩(oldY) G̃ below','evidence':'Both upper tildes and lower G tilde are separate; the lower first apparent wave joins the p descender.'},
{'symbol':'circled shorthand','reading':'ses','evidence':'The middle e is a closed loop; the final character is s, not i.'},
{'symbol':'adjective','reading':'spacieux|specieux in heading and margin, no acute','evidence':'First vowel compressed/open; the ink does not safely select a or e. This does not silently normalize the differently weighted doubt on007.'},
{'symbol':'insertion guide','reading':'curved rule beneath précédents, bending into axiomes/que gap','evidence':'Curvature and endpoint anchor distinguish it from a lexical underline.'}
]
proof1='Conditional check of the NB forward implication. Assume the minimal/minimum reading of scan007 At_M4a and the principal-downset meaning of Ỹ. If X∥Y but Z≪X and Z≪Y, choose A≤X minimal in X̃^Z={T≤X:Z≪T} and B≤Y minimal in Ỹ^Z. Every T≤A with Z≪T also lies in X̃^Z, so minimality forces T=A; hence Z◦≪A under the displayed definition, and likewise Z◦≪B. Downward compatibility gives A compatible B from X compatible Y. At_M4b then yields A=B, producing a common ≤-lower bound of X,Y and contradicting disjointness. Thus the forward assertion follows under these explicitly stated premises. This check does not settle the uncertain minimal/minimum/privilégié word on007, prove the axioms, or establish the proposed At DC1 or Cor.'
proof2='The limited reverse implication is immediate from scan006 At_M0 (≤ implies ≪): a common ≤-lower bound would be a common ≪-refinement. Consequently absence of a common ≪-refinement excludes a common ≤-lower bound. This alone does not establish compatibility, which is also required by the page’s definition of X∥Y. With compatibility assumed, the definition yields disjointness; without it, the full converse remains unproved here. The author’s promised later axiom was not inspected.'
math_notes=[
{'id':'R3-S008-N1','type':'reading summary, not a proof check','content':'The opening explains the intended order of axioms: disjunction–compatibility before loci, to avoid the appearance of dependence. These are described as facultatifs for an atelier, with mutual implications expected.'},
{'id':'R3-S008-N2','type':'reading summary, not a proof check','content':'Disjointness of figures is defined by compatibility and empty intersection, then characterized in terms of all pairs of strata. For M it is compatibility plus absence of a common lower bound. The first two displayed equivalences were read but not independently proved in this run.'},
{'id':'R3-S008-P1','type':'targeted proof check, conditional on the stated ink reading','content':proof1},
{'id':'R3-S008-P2','type':'targeted proof check of a limited converse','content':proof2},
{'id':'R3-S008-N3','type':'reading summary, not a proof check','content':'The cancelled At DC1 draft gives a compatibility criterion involving refinements disjoint from K=X∩Y, and its cancelled corollary gives the analogous condition for figures. The margin names the condition and gives simplicial ateliers as counterexamples. Neither the criterion, the corollary, nor the claimed counterexample class was verified.'},
{'id':'R3-S008-N4','type':'ink and mathematical expectation kept separate','content':'The lower Sup first object remains F|F̃, with bare F first because the apparent wave joins the p of Sup. The expected intersection-of-strata index does not authorize adding a tilde. Likewise the first NB tense and the spacing/spelling des′ are retained as ink doubts, not repaired from grammar or the proof.'}
]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
who='GPT-6 Astra Pro; effort setting not exposed; run R3'
events=[
{'statement_id':'R3-S008-D1','date':end,'who':who,'type':'carried as background without fault found','outcome':'Scan006 At_M0, ≤⇒≪, used as an explicit axiom assumption for P2; not proved.'},
{'statement_id':'R3-S008-D2','date':end,'who':who,'type':'carried as background without fault found','outcome':'Scan007 At_M4a with minimal/minimum reading, and its circled-refinement definition, assumed for P1; the uncertain alternative privileged reading is not covered.'},
{'statement_id':'R3-S008-D3','date':end,'who':who,'type':'carried as background without fault found','outcome':'Downward compatibility condition b on006/007 and At_M4b uniqueness on007 assumed for P1; not independently established.'},
{'statement_id':'R3-S008-P1','date':end,'who':who,'type':'targeted proof check','outcome':'Under D2–D3 and the principal-downset interpretation, X∥Y implies no Z with Z≪X,Z≪Y. Proof in scan008.md/json. Does not decide the word minimal/minimum/privilégié or verify At DC1/Cor.'},
{'statement_id':'R3-S008-P2','date':end,'who':who,'type':'targeted proof check','outcome':'Under D1, no common ≪-refinement implies no common ≤-lower bound. Compatibility is still an additional premise for disjointness; the unconditional converse is not proved.'}
]
checked=[
{'place':'first figure disjointness formula','reading':r'F\parallel G ⇔ F compatible G and F∩G=∅_F','evidence':'Double bars, bidirectional arrow, crossed-angle compatibility and intersection are individually visible; the subscript is separately resolved above.'},
{'place':'universal stratum formula','reading':r'∀X∈F̃, Y∈G̃, X∥Y','evidence':'Both tildes and uppercase variables are visible. There is one initial ∀ and no second quantifier before Y.'},
{'place':'M definition','reading':r'X∥_M Y iff X compatible_M Y and {X,Y} has no ≤-lower bound','evidence':'M is placed under each relation, not under X or Y; the nonexistence sign and both Z≤ inequalities are present.'},
{'place':'At DC Sup index','reading':r'Z∈\widetilde X\cap\widetilde Y','crop':'readers/R3/crops/008_DC_sup.png','crop_coordinates':cm['008_DC_sup']['box'],'evidence':'Both independent waves are clearly separated from X and Y; ∩ is an arch and ∈ is crossed by only the global thin cancellation line.'},
{'place':'At DC full condition','reading':r'X′≪X, X′∥K, Y′≪Y, Y′∥K ⇒ X′∥Y′','crop':'readers/R3/crops/008_DC_formula.png','crop_coordinates':cm['008_DC_formula']['box'],'evidence':'Every prime is a separate upright tick at upper right. Every parallel relation has exactly two bars. The three additional thin diagonals continue beyond the signs and belong to cancellation, not negation or a third bar.'},
{'place':'Cor surviving second Sup object','reading':r'\widetilde G','crop':'readers/R3/crops/008_Cor_sup.png','crop_coordinates':cm['008_Cor_sup']['box'],'evidence':'A separate wave sits above the rounded G; it is clearer than the disputed mark above the first F.'},
{'place':'Cor full condition','reading':r'X≪F, Y≪G, X∥K, Y∥K ⇒ X∥Y','crop':'readers/R3/crops/008_Cor_formula.png','crop_coordinates':cm['008_Cor_formula']['box'],'evidence':'Both refinement signs are double chevrons, all parallel relations have two uprights, and the implication has two horizontal shafts with a right-pointing head. No prime marks appear on the variables.'},
{'place':'margin cancellation extent','reading':'margin text preserved, with a crossing general diagonal acknowledged','crop':'readers/R3/crops/008_margin.png','crop_coordinates':cm['008_margin']['box'],'evidence':'A single long thin diagonal intersects the lower/right note and continues into the cancelled draft. It is not a separate short cancellation aimed only at the marginal sentence; the note is not independently declared deleted.'}
]
unresolved=[]
for a in aud:
 if a['status']!='resolved':
  rr=next(r for r in rows if r['id']==a['difference_id'])
  unresolved.append({'place':a['place'],'reading':a['reading'],'confidence':rr['confidence']})
unresolved += [dict(place='At DC title adjective',reading=r'\unsure{spacieux|specieux}',confidence='low'),dict(place='marginal adjective',reading=r'\unsure{spacieux|specieux}',confidence='low')]
out=dict(reader='R3',scan=8,start_utc=(root/'scan008_start.txt').read_text().strip(),end_utc=end,model=who,
 images_viewed=['H156-01_156-7_scan008.jpg','H156-01_156-7_scan008_a.jpg','H156-01_156-7_scan008_b.jpg']+[x['file'] for x in manifest],
 workflow='Whole once and both supplied halves once before the targeted-crop stage. Twenty initial crops were created. An attempted image-output batch was truncated during context compaction before effective inspection; the existing crops were then each inspected once in small batches, without recropping. One additional, distinct crop of précédents and its insertion guide was created and viewed when the main reader asked for that still-open layout check. Total 21 crops, all coordinates preserved. No later scan, other reader, main decision or additional S row was opened.',
 coverage=coverage,notation=notation,math_notes=math_notes,author_qualifications=['pour ne pas avoir l’air de les en faire dépendre','Les axiomes sont "facultatifs" pour un atelier',r'Il résul\deleted{\illegible{1}}\unsure{te|tera} des axiomes précédents',r'et \deleted{\unsure{la}} réciproque résultera \unsure{d\'axiome|d\'axiomes} ci-dessous…','[NB et alors seulement… cf Cor]','Contre-ex. : les ateliers simpliciaux…'],
 unresolved=unresolved,differences=rows,C_doubt_audit=aud,checked_agreements=checked,check_events=events,
 S_adjudication={'applicable':False,'note':'No S row directly applies to008. No additional S row was consulted.'},
 content_omitted_by_both_witnesses=[{'place':'opening insertion','reading':'actual curved insertion guide for avoir l’air de','evidence':'Guide under the raised words bends toward the les gap, reproduced in TikZ.'},{'place':'NB insertion','reading':'curved guide below précédents, reproduced in TikZ','evidence':'Bends down at the gap axiomes / que; not an underline.'}],
 count_note='The old/live first NB verb is one locus with two C-audit entries, and the old/live Cor variable is one locus with two entries, to avoid counting the same overwritten site twice. The general lower cancellation row does not repeat its text as further whole-block omissions.')
for group in (rows,aud):
 for entry in group:
  for key,value in entry.items():
   if isinstance(value,str): entry[key]=value.replace("\\'", "'")
out['author_qualifications']=[v.replace("\\'", "'") for v in out['author_qualifications']]
(root/'scan008.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (root/'scan008_check_events.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
lines=['# R3 independent reading — scan008 (manuscript page7)','',f'Start: {out["start_utc"]}. End: {end}. {who}.','',f'{len(rows)} locus records; all 21 C doubts audited; 21 targeted crops, with the supplied whole and both halves inspected once each.','',
'## Principal findings','',
'- The actual opening insertion is **avoir l’air de**, anchored before **les en faire dépendre**. The curved guide is reproduced. H’s **moins élégants** is not on the page.',
'- Read the definition label **dfn**, and the lowered empty-set index as a plain **F**. Read **disjoints**, **On a d’ailleurs**, **donc interprétation**, and ordinary **M**. Keep the uncertain **des′|des|d′** and **termes|terme**.',
'- The first NB verb has a clear shared prefix **résul-**. Overwriting is localized to the tall **t** and final cluster. The live ending favors **te**, with **tera** retained as an alternative. An independent complete earlier **résultera** cannot be recovered; the old terminal group is marked illegible, rather than duplicating the clear prefix as a second cancelled word.',
'- The curved stroke beneath **précédents** descends into the **axiomes / que** gap. It is an insertion guide. Read **ça implique**, and recover the struck **i.e. c’est un**. Keep the doubt on its final existential glyph, the cancelled article and edge-truncated **d’axiome|d’axiomes**.',
'- Preserve the whole lower **At DC1 / Cor** draft as cancelled, while keeping its earlier local cancellations distinct. Resolve **Soient**, inserted **soit**, and the locally cancelled **∀**. Preserve old **et** and **Il** as uncertain. The raised phrase is **pour X′,Y′∈M**, without H’s **tous**.',
'- All double-bar relations and all primes in both lower formulas were checked. The apparent third lines belong to the long diagonal cancellation strokes. The At DC Sup index is exactly **Z∈X̃∩Ỹ**.',
'- In the Cor Sup index, the first apparent wave joins the descending **p** of **Sup**. Prefer **F|F̃**, retaining uncertainty; the second surviving **G̃** is clear. Old X/Y layers remain uncertain. Resolve the last quantified variable as uppercase **Y** while retaining the older **φ|y** doubt.',
'- The oval contains **ses**, not **ssi**. The marginal note is complete: **Un atelier sera dit … s’il satisfait cette condition. Contre-ex. : les ateliers simpliciaux…**. The adjective is retained as **spacieux|specieux**, without a visible acute, in both title and margin.',
'', '## Mathematical checks and limits','',proof1,'',proof2,'',
'The figure/strata equivalence, the proposed At DC1, its corollary and the stated simplicial counterexamples were read but not independently verified. No later page or directly applicable S row was consulted. The events file records the conditional proofs and their assumed axioms separately.','',
'## Detailed differences','', '| ID | Place | C | H | R3 | Confidence | Evidence |','|---|---|---|---|---|---|---|']
for r in rows:
 lines.append('| '+' | '.join(str(r[k]).replace('|','\\|').replace('\n',' ') for k in ['id','place','C','H','reading','confidence','evidence'])+' |')
lines += ['', '## C-doubt audit','', '| No. | Place | C | R3 | Status |','|---:|---|---|---|---|']
for a in aud:
 lines.append('| '+' | '.join(str(a[k]).replace('|','\\|').replace('\n',' ') for k in ['number','place','C','reading','status'])+' |')
lines += ['', '## Notes while reading','']+[f'- **{n["id"]} — {n["type"]}: {n["content"]}' for n in math_notes]+['','## Inspection provenance','',out['workflow'],'',out['count_note'],'']
(root/'scan008.md').write_text('\n'.join(lines))
print(json.dumps({'written':['scan008.tex','scan008.json','scan008.md','scan008_crops.json','scan008_check_events.tsv'],'differences':len(rows),'C_doubts':len(aud),'crops':len(manifest),'end_utc':end},ensure_ascii=False))
