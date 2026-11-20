from pathlib import Path
import csv, json, re

ROOT = Path('/workspace/scratch/d7b9f54fbe44')
REVIEW = ROOT / 'deliverable/review'
manifest = json.loads((REVIEW / 'scan033_crop_manifest.json').read_text())
crops = {c['locus']: c for c in manifest}
C = (ROOT / 'packets/033/C.tex').read_text()
H = (ROOT / 'packets/033/H.tex').read_text()
draft = (REVIEW / 'scan033_draft.tex').read_text()
changes = []

def change(n, place, c, h, final, evidence, crop, kind, ac=False, ah=False,
           confidence='high', hm=False, certainty=False, consequential=False):
    m = crops[crop]
    changes.append(dict(id=f'033-{n:02d}', place=place, C=c, H=h, final=final,
        evidence=evidence, crop=m['crop'], box=m['box'], rotation=m['rotation'],
        confidence=confidence, kind=kind, against_C=ac, against_H=ah,
        H_marked=hm, certainty_only=certainty, consequential=consequential))

change(1, 'folio at head', r'\mspage{32.}', '(omitted)', r'\mspage{32.}',
       'Two connected bowls form 3; the second digit has an upper curve and lower foot of 2; the final dark point is separate.',
       'number', 'omission', ah=True)
change(2, 'opening cancelled glyph before 1°)', r'\deleted{\unsure{R|P}}', r'\struck{Or}',
       r'\deleted{\unsure{R|P|Or}}',
       'Cancellation leaves a vertical, loop and rightward trailing stroke. R/P remain plausible; the crossing does not exclude a fused Or. No forced resolution.',
       'top_initial', 'misread word', ah=True, confidence='low')
change(3, '1°), first F', r'\unsure{F|\mathcal F}', 'F', 'F',
       'A plain upright and separate short middle bar remain visible beneath a bent top arm; no script-family stroke requires a calligraphic letter.',
       'top_initial', 'other', certainty=True)
change(4, 'sideways margin, opening three words', r'\unsure{voir} \unsure{une|sa} \unsure{simplification}',
       r'\uncertain{va se simplifier}', 'va se simplifier',
       'After rotation −90°, va is two short letter groups, followed by se; the long word ends with the short -fier sequence rather than -fication. The p descender and the tall l/f strokes are visible.',
       'margin', 'misread word', ac=True, hm=True)
change(5, 'sideways margin, final word', 'bas', r'\ill{}', 'bas',
       'The b ascender and following rounded a plus terminal s follow plus; the word is legible on the rotated crop.',
       'margin', r'readable ink left as \ill{}', ah=True, hm=True)
change(6, '2°), after initial F\\G', '(no point)', '.', '(no point)',
       'The space between the terminal G and Soit has no punctuation point of writing density.',
       'two_start', 'text not on the page', ah=True)
change(7, '2°), underline/bracket of the two formulas', r'\underline{\rule... A\prime\subset A... , A\prime^{\circ(F\prime)}\subset A^{\circ(F)}...\rule...}',
       '(no underline or end ticks)',
       r'\underline{\rule[-.15ex]{.35pt}{.55ex}\,A\prime\unsure{\subset|\in}A^{\deleted{\unsure{\prime|\ast|?}}},\ A\prime^{\circ(F\prime)}\subset A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}\,\rule[-.15ex]{.35pt}{.55ex}}',
       'A continuous lower stroke with short upturned ends brackets both formulas. It is genuine ink, so H loses a graphical emphasis even though the rule dimensions in the TSV are TeX syntax.',
       'two_underlined_formula', 'other', ah=True)
change(8, '2°), first A superscript cancellation', r'\deleted{\unsure{\prime|\ast|?}}', '(omitted)',
       r'A^{\deleted{\unsure{\prime|\ast|?}}}',
       'A small dark worked-over elevated mark follows the first A. Crossing obscures the original glyph; none of prime, star or hook/question-like form can be excluded.',
       'two_underlined_formula', 'omission', ah=True, confidence='low', consequential=True)
change(9, '2°), second A superscript cancellation', r'\deleted{\unsure{\prime|\ast|?}}', '(omitted)',
       r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}',
       'A separate worked-over elevated mark precedes the open-circle stratum superscript. It is not the circle itself; the underlying form remains unresolved.',
       'two_underlined_formula', 'omission', ah=True, confidence='low', consequential=True)
change(10, '2°), first relation in underlined formula', r'\subset', r'\subset',
       r'\unsure{\subset|\in}',
       'The relation has a C-shaped upper sweep and a heavily retraced lower return. A middle bar cannot be separated from the dense return, so membership remains a visual alternative.',
       'two_first_relation', 'other', confidence='low', certainty=True, consequential=True)
change(11, '2°), parenthesis after A′=A', r"d'où $A\in F$", r"d'où $A'\in F$", r"d'où $A\in F$",
       'The A has no raised prime in the clear gap before the membership sign. The unprimed letter is retained even though the proof mentions A′.',
       'two_conclusion', 'misread symbol or index', ah=True, consequential=True)
change(12, '2°), terminal cancelled words', r'\deleted{On a}', r'\struck{Or}',
       r'\deleted{\unsure{On a|Or}}',
       'The broad initial loop is followed by a low n-like run and a separated last trace, favouring On a; cancellation prevents every letter from being securely read.',
       'two_conclusion', 'misread word', ah=True, confidence='low')
change(13, 'Je dis, cancelled et before Il', r'\deleted{\unsure{et}}', r'\struck{et}', r'\deleted{et}',
       'The small e loop and following t stem/crossbar can both be followed through the crossing strokes. This resolves only C’s doubt wrapper.',
       'jedis_et', 'other', certainty=True)
change(14, 'Je dis, interlinear insertion', r"il suffirait $F'\ll F$", r"i.e. sachant $F'\ll F$",
       r"\inserted{il suffirait $F'\ll F$}",
       'A dotted i and tall l begin il; suffirait shows two f uprights and the ending -rait. There is no i.e. or sachant sequence. The two leftward angle tips in the formula are separate.',
       'jedis_insertion', 'misread word', ah=True)
change(15, 'Je dis, old closing parenthesis after F′≼F', r'\deleted{)}', '(omitted)', r'\deleted{)}',
       'The former closing curved stroke is darkened/crossed at the insertion attachment after F; cf lemme plus bas continues to a later live close.',
       'jedis_relation', 'omission', ah=True)
change(16, 'Je dis, words after cf lemme plus bas)', r'et \deleted{\unsure{bien}}', r"\uncertain{d'autre part}",
       r'et \unsure{\uline{bien}|\deleted{bien}}',
       'The live et and following b initial, i/minim run and terminal n read et bien; the longer phrase d’autre part is not supported. State of the lower stroke beneath bien is treated separately.',
       'jedis_et_bien', 'misread word', ah=True, hm=True)
change(17, 'Je dis, state of bien', r'\deleted{\unsure{bien}}', r"\uncertain{d'autre part}",
       r'\unsure{\uline{bien}|\deleted{bien}}',
       'The short horizontal stroke lies mainly below the letter bodies, favouring an underline. It might still be a low cancellation; the draft marks both states instead of silently changing the scope.',
       'jedis_et_bien', 'deletion state (struck given live or live given struck)', ac=True,
       confidence='low', consequential=True)
change(18, 'Je dis, cancelled sign before A,A′', r'\deleted{$\unsure{F|\in}$}', r'\struck{$\exists$}',
       r'\deleted{$\unsure{F|\in|\exists|E}$}',
       'A left upright and upper/middle rightward bars favour F. The large bottom return may belong to the cancellation, leaving E or a curved membership-like body possible; the crossing prevents excluding H’s ∃ absolutely.',
       'jedis_deleted_symbol', 'misread symbol or index', ah=True, confidence='low', consequential=True)
change(19, 'Donc, overwritten sign before live A′', r'\deleted{\unsure{F|A}}', '(omitted)',
       r'\deleted{\unsure{F|A}}A\prime\in F\prime\setminus G\prime\Rightarrow A\prime\in F',
       'The cap/left upright and diagonal traces underneath the live A′ are distinct from the final letter. F/A cannot be separated under the overtracing; the entire implication is read in the larger crop.',
       'donc_formula', 'omission', ah=True, confidence='low', consequential=True)
change(20, 'Donc, parenthesis and cancelled close around d’où…qed',
       r"(d'où $A'\in F\setminus G$\deleted{)}, qed)",
       r", d'où $A'\in F\smallsetminus G$ (qed)",
       r"(d'où $A'\in F\setminus G$\deleted{)}, qed)",
       'The opening curve precedes d’où. A crossed old close follows G, then a live comma and qed, then the live close. No opening parenthesis is present immediately before qed.',
       'donc_parenthesis', 'insertion or placement', ah=True)
change(21, 'Donc, Sinon versus Si', 'Sinon', 'Si', 'Sinon',
       'The first word has additional joined low strokes after Si and ends before the separately begun on. Those strokes support -non.',
       'donc_sinon', 'misread word', ah=True)
change(22, 'Donc, aurait versus avait', 'aurait', 'avait', 'aurait',
       'The verb after on has the au/r sequence and additional minim before -ait; the shorter avait does not account for the ink.',
       'donc_sinon', 'misread word', ah=True)
change(23, 'cancelled b⇒c block, interlinear On suppose',
       r"\inserted{On suppose b) i.e. $\varphi$ induit $F'\setminus G'\overset{\sim}{\longrightarrow}F\setminus G$}",
       '(reported in an editorial note rather than transcribed as an insertion)',
       r"\deleted{\inserted{On suppose b) i.e. $\varphi$ induit $F'\setminus G'\overset{\sim}{\longrightarrow}F\setminus G$}}",
       'All words and the single rightward arrow with a tilde above are visible. A long curved leader attaches the interlinear sentence before Soit. Later oblique cancellation strokes cross the insertion too.',
       'cancel_insert', 'insertion or placement', ah=True)
change(24, 'cancelled b⇒c, apparent opening parenthesis before Soit', '(no parenthesis)', '(', '(insertion leader, not a parenthesis)',
       'The curve before Soit is continuous with the long leader from the inserted sentence above. It is not a textual opening bracket.',
       'cancel_first', 'text not on the page', ah=True)
change(25, 'cancelled b⇒c, ouverte', 'ouverte', r'\ill{}', 'ouverte',
       'The o/u low sequence, v, tall t and final e are visible within the underlined wording despite the diagonal crossing.',
       'cancel_underlined', r'readable ink left as \ill{}', ah=True, hm=True)
change(26, 'cancelled b⇒c, inner cancellation dans la', r'\deleted{dans \unsure{la}}', '(omitted)',
       r'\deleted{dans \unsure{la}}',
       'A local cancellation crosses dans; the following densely hatched group permits la but does not show every letter. The surviving de belongs after this local deletion.',
       'cancel_underlined', 'omission', ah=True, confidence='low')
change(27, 'cancelled b⇒c, underlined phrase', r"\uline{strate ouverte \deleted{dans \unsure{la}} de $F'$}", '(no underline)',
       r"\uline{strate ouverte \deleted{dans \unsure{la}} de $F'$}",
       'The long low stroke starts under strate and continues under the phrase to F′. The oblique cancellations are separate strokes crossing it.',
       'cancel_underlined', 'other', ah=True)
change(28, 'cancelled b⇒c, de after élément', r'\deleted{de}', '(omitted)', r'\deleted{de}',
       'The d loop and following e remain readable under a local horizontal cancellation between élément and tel.',
       'cancel_de', 'omission', ah=True)
change(29, 'cancelled b⇒c, final Prouvons sentence state',
       r"\deleted{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.}",
       r"\struck{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.}",
       r"\unsure{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.|\deleted{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.}}",
       'Every large oblique cancellation ends above this last baseline; none crosses Prouvons or its equality. A semantic cancellation of the whole abandoned paragraph remains possible but is not demonstrated by a stroke through this line.',
       'cancel_block', 'deletion state (struck given live or live given struck)', ac=True, ah=True,
       confidence='low', consequential=True)
change(30, 'bottom, punctuation after U', ',', '.', ',',
       'The mark after U has a descending tail and is a comma.',
       'bottom_start', 'misread symbol or index', ah=True)
change(31, 'bottom, overwritten sign between F′ and G′',
       r'\deleted{\unsure{\times|\setminus}}\unsure{\setminus}', r'\smallsetminus',
       r"F'\deleted{\unsure{\times|\setminus}}\unsure{\setminus}G'=I'^{\ast}",
       'Several crossing angular strokes form an overwritten patch. A descending diagonal supports the live set-difference reading, but the earlier sign and the separation of writing states remain uncertain.',
       'bottom_indices', 'omission', ah=True, confidence='low', consequential=True)
change(32, 'bottom, ens abbreviation punctuation', 'ens', 'ens.', 'ens',
       'The joined low terminal s is followed by blank space before d’indices; there is no independent period.',
       'bottom_ens', 'abbreviation expanded or spelling modernised', ah=True)
change(33, 'bottom, cancelled triangular character after I', r'\deleted{$\unsure{A|\Delta}$}', '(omitted)',
       r'\deleted{$\unsure{A|\Delta}$}',
       'A triangular body with a mid-height crossing survives under darker diagonal retracing. The original lower boundary cannot distinguish A from Δ.',
       'bottom_F', 'omission', ah=True, confidence='low', consequential=True)
change(34, 'bottom, comma immediately after I', ',', '(no comma)', ',',
       'An isolated descending comma lies between I and the cancelled triangular character.',
       'bottom_F', 'omission', ah=True)
change(35, 'bottom, letter in (=F)', 'F', 'F', r'\unsure{F|P}',
       'The upper arm loops back into a near-enclosed lobe; a lower rightward stroke favours F but P remains a visual possibility. The surrounding index identification is not used to repair the letter.',
       'bottom_F', 'other', confidence='low', certainty=True, consequential=True)
change(36, 'bottom, after I′(=F′)', '(no outer close)', ')', '(no outer close)',
       'There is one closing parenthesis after F′ and then a period. No second closing curve follows it; the earlier opening before parties remains unbalanced on the sheet.',
       'bottom_last', 'text not on the page', ah=True)

rule_candidate = r'\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[line width=.4pt] (.65,0) -- (.90,10);\node[rotate=90,anchor=west,scale=.8] at (0,3.7) {va se simplifier, cf plus bas};\end{tikzpicture}}}'
changes.append(dict(id='033-37', place='long separator adjoining the left margin note',
    C='(not represented)', H='(described in an editorial note)', final=rule_candidate,
    evidence='The once-viewed whole sheet shows a long slightly slanting separator to the right of the sideways note, approximately x200–270, y145–1735. TikZ reproduces the stroke beside the note; geometry is approximate pending root review.',
    crop='source/SP114_CW_156-5_scans/J156-5-04_156-5_scan033.jpg', box=[65,145,285,1735], rotation=0,
    confidence='medium', kind='drawing or diagram', against_C=True, against_H=False,
    H_marked=False, certainty_only=False, consequential=False))

unresolved = []
def doubt(place, reading, alternatives, reason, confidence='low'):
    unresolved.append(dict(place=place, reading=reading, alternatives=alternatives, reason=reason, confidence=confidence))
doubt('opening cancelled glyph', 'R', ['P','Or'], 'Crossing obscures the loop and final stroke; R only preferred, not established.')
doubt('2°), first underlined relation', r'\subset', [r'\in'], 'Heavily retraced lower return could include a membership bar.')
doubt('2°), first cancelled superscript', r'\prime', [r'\ast','?'], 'Tiny worked-over angular mark does not resolve.')
doubt('2°), second cancelled superscript', r'\prime', [r'\ast','?'], 'Tiny worked-over angular mark does not resolve; separate from the following circle.')
doubt('2°), terminal cancelled phrase', 'On a', ['Or'], 'Several low residual strokes favour On a but every letter is not visible.')
doubt('Je dis, bien state', r'\uline{bien}', [r'\deleted{bien}'], 'Line below the letter bodies favours underlining; low cancellation remains possible.')
doubt('Je dis, cancelled glyph before A,A′', 'F', [r'\in',r'\exists','E'], 'Left upright with two rightward bars favours F; lower curve is entangled with crossing.')
doubt('Donc, faint words before prouvé', 'on a', [], 'Two light groups are compatible with on a but individual bodies are not all recoverable.')
doubt('Donc, overwritten sign before A′', 'F', ['A'], 'Cap, upright and diagonals merged with live A′.')
doubt('cancelled b⇒c, local word after dans', 'la', [], 'Heavy hatch leaves a possible long initial but not both complete letters.')
doubt('cancelled b⇒c, final Prouvons sentence', r"Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.",
      [r"\deleted{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.}"],
      'No cancellation stroke crosses the line, while both witnesses extended the cancellation semantically to it.')
doubt('bottom, repeated I superscript', r'\ast', ['k','+'], 'Stem and rightward branches recur in both superscripts; repetition does not distinguish a star from k/cross.', 'medium')
doubt('bottom, old sign between F′ and G′', r'\times', [r'\setminus'], 'Overwritten crossing patch hides earlier strokes.')
doubt('bottom, live sign between F′ and G′', r'\setminus', [], 'A descending diagonal is visible inside the correction but its state is difficult to separate.')
doubt('bottom, cancelled character after I', 'A', [r'\Delta'], 'Triangular form and cancellation crossbar remain merged.')
doubt('bottom, letter in (=F)', 'F', ['P'], 'Looped upper arm and lower detached stroke admit P despite the stronger F reading.')

inventory = []
def inv(element, kind, position, first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,hand='handwritten'))
inv('folio','text','top centre, y15–80','32.')
inv('1° proof','text','top main column, y70–330',r'1°) $F\setminus G\subset F\prime\setminus G\prime$')
inv('opening cancellation','deletion','before 1°), y70–155',r'\unsure{R|P|Or}')
inv('cancelled membership','deletion','1°), line 3, y245–330',r'$A\in$')
inv('sideways comment','margin note','left edge, x65–205,y340–1140; reading upwards','va se simplifier, cf plus bas')
inv('long separator','drawing','right of the marginal note, approximately x200–270,y145–1735','long slightly slanting line')
inv('2° opening proof','text','upper middle, y325–640',r'2°) $F\prime\setminus G\prime\subset F\setminus G$')
inv('cancelled first On a','deletion','2°), line 2, y395–475','On a')
inv('bracketed underlined formulas','text','2°), line 3, y465–570',r"$A'\unsure{\subset|\in}A^{\deleted{\unsure{\prime|\ast|?}}}, A'^{\circ(F')}\subset A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}$")
inv('first cancelled elevated mark','deletion','2°), first A superscript, y465–570',r'\unsure{\prime|\ast|?}')
inv('second cancelled elevated mark','deletion','2°), second A superscript, y465–570',r'\unsure{\prime|\ast|?}')
inv('terminal cancelled On a/Or','deletion','end 2°), y545–640',r'\unsure{On a|Or}')
inv('Je dis proof','text','middle, y660–1240',r'Je dis que $A\in F\setminus G$')
inv('cancelled Mais','deletion','Je dis, y795–890','Mais')
inv('cancelled et','deletion','Je dis, y895–990','et')
inv('il suffirait insertion','insertion','above car formula, y950–1095',r"il suffirait $F'\ll F$")
inv('old close after car formula','deletion','after F′≼F at insertion attachment, y1000–1110',')')
inv('bien state','deletion','after cf lemme plus bas), y980–1090',r'\unsure{\uline{bien}|\deleted{bien}}')
inv('cancelled F-like symbol','deletion','before A,A′, y1090–1210',r'$\unsure{F|\in|\exists|E}$')
inv('Donc conclusion','text','lower middle, y1260–1705',r'Donc \unsure{on a} prouvé que')
inv('overwritten F/A','deletion','before live A′ in Donc, y1260–1380',r'\unsure{F|A}')
inv('old close before qed','deletion','after d’où A′∈F\\G, y1415–1530',')')
inv('cancelled b⇒c argument','deletion','lower third, y1630–1970, last sentence state open',r'b) $\Rightarrow$ c) Soit $A\in F\setminus G$')
inv('On suppose insertion later cancelled','insertion','above cancelled b⇒c, y1630–1755',r'On suppose b) i.e. $\varphi$ induit')
inv('underlined strate phrase','text','inside cancelled argument, y1790–1915',r'strate ouverte \deleted{dans \unsure{la}} de $F\prime$')
inv('inner dans la cancellation','deletion','inside strate phrase, y1790–1915',r'dans \unsure{la}')
inv('inner de cancellation','deletion','after élément, y1880–1970','de')
inv('Prouvons equality with open state','text','last line of abandoned argument, y1935–2055',r"Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.")
inv('renewed b⇔c argument','text','bottom, y2020–2340',r'b $\Longleftrightarrow$ c')
inv('cancelled Posons','deletion','after b⇔c, y2020–2145','Posons')
inv('overwritten difference sign','deletion','between F′ and G′, y2100–2220',r'\unsure{\times|\setminus}')
inv('cancelled A/Delta','deletion','after I, y2170–2290',r'$\unsure{A|\Delta}$')

state_specs = [
('deletion',1,'top_initial','Scope: initial glyph only, before 1°). Retain cancellation; reading unresolved.'),
('deletion',2,'top_deleted_A','Scope: A∈ only, before (comme G≤F). Both signs readable.'),
('deletion',3,'two_on_a','Scope: On a, immediately before live Soit A. Both witnesses confirmed.'),
('deletion',4,'two_underlined_formula','Scope: first small elevated mark after A. Mark is cancelled; underlying prime/star/hook unresolved.'),
('deletion',5,'two_underlined_formula','Scope: second small elevated mark before the circle on A. Keep separate from the stratum superscript.'),
('deletion',6,'two_conclusion','Scope: terminal On a/Or after (d’où A∈F). Cancellation clear, words unresolved.'),
('deletion',7,'jedis_mais','Scope: Mais only; cancellation does not include following Donc.'),
('deletion',8,'jedis_et','Scope: et only before Il. Each letter visible; C’s doubt resolved.'),
('deletion',9,'jedis_relation','Scope: old closing parenthesis after car F′≼F. It is crossed at the insertion attachment.'),
('deletion',10,'jedis_et_bien','C’s cancellation of bien is questionable: stroke lies below letters. Draft explicitly gives underline/cancellation alternatives.'),
('deletion',11,'jedis_deleted_symbol','Scope: one symbol immediately before A,A′, cancellation clear; F/∈/∃/E reading remains open.'),
('deletion',12,'donc_formula','Scope: overwritten F/A under the live A′, not the whole implication.'),
('deletion',13,'donc_parenthesis','Scope: old closing parenthesis after F\\G; comma, qed and later close remain live.'),
('deletion',14,'cancel_block','Diagonal strokes certainly cancel header, insertion and first three baselines through φ(A′)=A. They end above final Prouvons line; scope to that final sentence explicitly doubted.'),
('deletion',15,'cancel_underlined','Inner cancellation scope: dans plus doubtful la, inside already cancelled and underlined phrase. Following de remains distinct.'),
('deletion',16,'cancel_de','Inner cancellation scope: de only, after élément and before tel.'),
('deletion',17,'bottom_start','Scope: Posons only, after renewed b⇔c and before On a.'),
('deletion',18,'bottom_indices','Scope: earlier sign in dense patch between F′ and G′; old ×/setminus uncertain. Live descending stroke also uncertain.'),
('deletion',19,'bottom_F','Scope: triangular A/Δ after I, and before live (=F/P).'),
('insertion',1,'jedis_insertion','Inserted il suffirait F′≪F above line; attaches after F′≼F and before cf lemme plus bas, with the former close suppressed.'),
('insertion',2,'cancel_insert','Inserted On suppose b) i.e. φ induit… attaches after heading b)⇒c), before Soit, by long curved leader. Insertion subsequently cancelled with its host block.')
]
def macro_contents(s, command):
    result=[]
    for m in re.finditer(r'\\'+command+r'\{',s):
        j=m.end(); start=j; depth=1
        while depth:
            depth += (s[j]=='{')-(s[j]=='}'); j+=1
        result.append(s[start:j-1])
    return result
state_audit=[]
for kind,index,locus,decision in state_specs:
    macro='deleted' if kind=='deletion' else 'inserted'
    m=crops[locus]
    state_audit.append(dict(id=f'C-{macro}-{index:02d}',kind=kind,C_scope=macro_contents(C,macro)[index-1],
        decision=decision,attachment=decision,crop=m['crop'],box=m['box'],rotation=m['rotation']))

doubt_specs = [
('retained with Or alternative','top_initial','R/P initial remains under crossing.'),
('resolved: F','top_initial','Upright with two arms is plain F.'),
('changed: va','margin','Rotated short word has va strokes, not voir.'),
('changed: se','margin','Middle two-letter group reads se, not une/sa.'),
('changed: simplifier','margin','Ending is -fier, not -fication.'),
('retained','two_underlined_formula','First cancelled elevated mark unresolved.'),
('retained','two_underlined_formula','Second cancelled elevated mark unresolved.'),
('resolved: et','jedis_et','Both e and t independently visible through crossing.'),
('word resolved; state open','jedis_et_bien','bien readable, underline versus cancellation unresolved.'),
('retained with ∃/E alternatives','jedis_deleted_symbol','Left upright and two bars favour F; lower return unclear.'),
('retained','donc_begin','Faint on a has incomplete bodies.'),
('retained','donc_formula','Old F/A merges with live A′.'),
('retained','cancel_underlined','Hatchet obscures la.'),
('retained','bottom_indices','First star/k/+ remains ambiguous; second occurrence shares the same form.'),
('retained','bottom_indices','Earlier ×/setminus in dense patch unresolved.'),
('retained','bottom_indices','Live descending set-difference stroke remains uncertain.'),
('retained','bottom_F','Cancelled triangular A/Δ unresolved.')
]
c_doubt_audit=[]
for n,(status,locus,evidence) in enumerate(doubt_specs,1):
    m=crops[locus]
    c_doubt_audit.append(dict(id=f'C-unsure-{n:02d}',C=macro_contents(C,'unsure')[n-1],status=status,
        evidence=evidence,crop=m['crop'],box=m['box'],rotation=m['rotation']))
formula_doubt_audit = [
dict(place='C_doubts row 1: F/G',decision='Plain F resolved; G retains its inward terminal as ordinary G.',crop=crops['top_initial']['crop']),
dict(place='C_doubts row 2: F^{A′}, circles and parenthesized F/F′',decision='Read full local formula. F^{A′} and both circle superscripts retained; both cancelled elevated marks remain doubtful; first inclusion gains membership alternative.',crop=crops['two_underlined_formula']['crop']),
dict(place='C_doubts row 3: ≼ and ≪',decision='Curved comparison with lower stroke and two separate angle tips retained; no change from H’s equivalent macro.',crop=crops['jedis_insertion']['crop']),
dict(place='C_doubts row 4: arrows',decision='Inserted arrow has one shaft, right head, tilde above. Lower b⇔c arrow has two shafts and heads at both ends.',crop=crops['cancel_insert']['crop'],additional_crop=crops['bottom_start']['crop']),
dict(place='C_doubts row 5: I upper marks',decision='Both marks inspected in complete pair of index definitions. Star/k/+ remains open and is marked at first occurrence only.',crop=crops['bottom_indices']['crop']),
dict(place='C_doubts final row: d’où A∈F',decision='Unprimed A retained on ink; no correction to A′.',crop=crops['two_conclusion']['crop'])
]

rows=list(csv.DictReader((ROOT/'packets/033/differences.tsv').open(),delimiter='\t'))
row_decisions={
1:('033-01,033-02','Folio 32. retained; opening cancelled R/P/Or remains open. Archive scan number 33 is metadata.'),
2:('033-03','Plain F resolved; calligraphic alternative removed with crop evidence.'),
3:('033-04,033-05','Same marginal note as row 14: va se simplifier, cf plus bas.'),
4:('033-06','No period between initial formula and Soit.'),
5:('033-07','Numeric rule dimensions are macro syntax; the actual underline and left end tick are preserved and absent in H.'),
6:('033-08','First cancelled superscript retained with unresolved reading.'),
7:('033-09','Second cancelled superscript retained with unresolved reading.'),
8:('033-07','Numeric rule dimensions are macro syntax; the actual right end tick is present.'),
9:('033-11','Unprimed A retained.'),
10:('033-12','Cancelled On a preferred; Or remains an alternative.'),
11:('033-14','il suffirait, not i.e. sachant.'),
12:('033-15','Cancelled old close retained.'),
13:('033-16,033-17,033-18','et bien read; bien state open; next cancelled sign favours F but remains unresolved.'),
14:('033-04,033-05,033-37','Same note as row 3; H’s descriptive note is editorial, while its separator is reproduced graphically.'),
15:('033-19','Old F/A under live A′ retained.'),
16:('033-20','Actual opening parenthesis precedes d’où.'),
17:('033-20','Old close after F\\G is cancelled, followed by comma; no opening before qed.'),
18:('033-21','Sinon retained.'),
19:('033-22','aurait retained.'),
20:('033-23,033-24','Actual On suppose insertion restored in place; H’s apparent opening bracket is its leader.'),
21:('033-25,033-26,033-27','ouverte readable; local struck dans la retained with la doubtful; underline retained.'),
22:('033-28','Local struck de retained.'),
23:('033-23','H’s prose note is editorial; its quoted source insertion is represented once in the page.'),
24:('033-30','Comma after U.'),
25:('doubt: bottom I upper marks','First superscript remains ast/k/+; star preferred. H certainty does not resolve it.'),
26:('033-31','Overwritten patch and uncertain live setminus retained.'),
27:('macro-only','C ast and H * are the same chosen star reading; tokenizer omitted C’s command. Shared glyph ambiguity is marked only at first occurrence.'),
28:('033-32','ens without a period.'),
29:('033-33,033-34','Comma and cancelled A/Delta retained.'),
30:('033-36','No second closing parenthesis; source punctuation remains unbalanced.')}
coverage=[]
for i,row in enumerate(rows,1):
    refs,decision=row_decisions[i]
    coverage.append(dict(row=i,words_before=row['words before'],C=row['witness C'],H=row['witness H'],
        references=refs,decision=decision,macro_only=(refs=='macro-only')))

cancel_insert = r"\deleted{\inserted{On suppose b) i.e. $\varphi$ induit $F'\setminus G'\overset{\sim}{\longrightarrow}F\setminus G$}}"
cancel_full = r"\deleted{b) $\Rightarrow$ c) \inserted{On suppose b) i.e. $\varphi$ induit $F'\setminus G'\overset{\sim}{\longrightarrow}F\setminus G$} Soit $A\in F\setminus G$, prouvons que $A^{\circ(F)}$ est une \uline{strate ouverte \deleted{dans \unsure{la}} de $F'$}. Soit $A'\in F'\setminus G'$ l'unique élément \deleted{de} tel que $\varphi(A')=A$.} \unsure{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.|\deleted{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.}}"
second_readings={
'number':r'\mspage{32.}',
'top_initial':r"\deleted{\unsure{R|P|Or}} 1°) $F\setminus G\subset F'\setminus G'$",
'top_deleted_A':r"$|G|$ donc \deleted{$A\in$} (comme $G\leq F$) $A\in G$.",
'two_start':r"2°) $F'\setminus G'\subset F\setminus G$ Soit",
'two_on_a':r"et d'abord $A'\in F$. \deleted{On a} Soit $A$ le",
'two_underlined_formula':r"$F^{A'}$ donc $\underline{\rule[-.15ex]{.35pt}{.55ex}\,A'\unsure{\subset|\in} A^{\deleted{\unsure{\prime|\ast|?}}},\ A'^{\circ(F')}\subset A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}\,\rule[-.15ex]{.35pt}{.55ex}}$",
'two_conclusion':r"prouvons que $A'=A$ (d'où $A\in F$). \deleted{\unsure{On a|Or}}",
'margin':r'\margin{va se simplifier, cf plus bas}',
'jedis_mais':r"absurde. \deleted{Mais} Donc $A\in F\setminus G$",
'jedis_et':r"donc $A\in F'$, \deleted{et} Il en résulte",
'jedis_equality':r"$A^{\circ(F)}=A^{\circ(F')}$",
'jedis_insertion':r"(car $F'\preceq F$\inserted{il suffirait $F'\ll F$}\deleted{)} cf lemme plus bas)",
'jedis_relation':r"(car $F'\preceq F$\inserted{il suffirait $F'\ll F$}\deleted{)} cf lemme plus bas)",
'jedis_et_bien':r'et \unsure{\uline{bien}|\deleted{bien}}',
'jedis_last_formula':r"\deleted{$\unsure{F|\in|\exists|E}$} $A,A'\in F'$ tels que $A'^{\circ(F')}\subset A^{\circ(F')}$, ce qui",
'donc_begin':r"Donc \unsure{on a} prouvé que $\deleted{\unsure{F|A}}A'\in F'\setminus G'$",
'donc_parenthesis':r"(d'où $A'\in F\setminus G$\deleted{)}, qed)",
'donc_sinon':r"Sinon on aurait $A'\in G$",
'cancel_insert':cancel_insert,
'cancel_first':r"\deleted{b) $\Rightarrow$ c) Soit $A\in F\setminus G$, prouvons que}",
'cancel_underlined':r"\deleted{$A^{\circ(F)}$ est une \uline{strate ouverte \deleted{dans \unsure{la}} de $F'$}. Soit}",
'cancel_de':r"\deleted{l'unique élément \deleted{de} tel que $\varphi(A')=A$.}",
'cancel_equality':r"\unsure{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.|\deleted{Prouvons $A'^{\circ(F')}=A^{\circ(F)}$.}}",
'bottom_start':r"b $\Longleftrightarrow$ c \deleted{Posons} On a $|F|\setminus|G|=|F'|\setminus|G'|$, soit $U$,",
'bottom_indices':r"$F\setminus G=I^{\unsure{\ast|k|+}},\ F'\deleted{\unsure{\times|\setminus}}\unsure{\setminus}G'=I'^{\ast}$",
'bottom_ens':r"des ens d'indices ordonnés $I$, \deleted{$\unsure{A|\Delta}$} $(=\unsure{F|P})$,",
'bottom_last':r"$I'(=F')$. On a",
'two_first_relation':r"$A'\unsure{\subset|\in} A^{\deleted{\unsure{\prime|\ast|?}}}$",
'jedis_deleted_symbol':r"\deleted{$\unsure{F|\in|\exists|E}$} $A,A'$",
'donc_formula':r"Donc \unsure{on a} prouvé que $\deleted{\unsure{F|A}}A'\in F'\setminus G'\Rightarrow A'\in F$.",
'cancel_block':cancel_full,
'bottom_F':r"$I$, \deleted{$\unsure{A|\Delta}$} $(=\unsure{F|P})$,"
}
second_boxes=[]
for m in manifest:
    loc=m['locus']; x0,y0,x1,y1=m['box']
    kinds=[]
    if loc in ['number','top_initial','two_start']:kinds.append('handwritten number')
    if loc=='margin':kinds.append('margin note; word difference')
    if loc in ['jedis_insertion','cancel_insert','cancel_block']:kinds.append('insertion')
    if loc not in ['number','margin','two_start','jedis_equality','donc_sinon','bottom_last']:kinds.append('deletion or state audit')
    if loc in ['top_initial','two_underlined_formula','two_first_relation','jedis_deleted_symbol','donc_formula','bottom_indices','bottom_F','cancel_equality','cancel_block']:kinds.append('doubtful formula or character')
    if loc in ['two_conclusion','jedis_insertion','jedis_et_bien','donc_sinon','cancel_underlined','cancel_de','bottom_ens']:kinds.append('word difference')
    second_boxes.append(dict(box='033-'+loc,kind='; '.join(kinds) or 'formula or punctuation audit',
        x0=x0,y0=y0,x1=x1,y1=y1,reading=second_readings[loc],crop=m['crop'],rotation=m['rotation']))
second_boxes.append(dict(box='033-margin-rule',kind='margin note; graphical stroke; departure from C',
    x0=65,y0=145,x1=285,y1=1735,reading=rule_candidate,
    crop='source/SP114_CW_156-5_scans/J156-5-04_156-5_scan033.jpg',rotation=0))

times={
'top_initial':'19:00:20','margin':'19:00:45','number':'19:01:14','top_deleted_A':'19:01:14',
'two_start':'19:01:23','two_on_a':'19:01:23','two_underlined_formula':'19:01:40','two_conclusion':'19:01:40',
'two_first_relation':'19:02:39','jedis_mais':'19:03:03','jedis_et':'19:03:03','jedis_equality':'19:03:18',
'jedis_insertion':'19:03:18','jedis_relation':'19:03:37','jedis_et_bien':'19:03:37',
'jedis_last_formula':'19:04:19','donc_begin':'19:04:19','jedis_deleted_symbol':'19:05:05','donc_formula':'19:05:05',
'donc_parenthesis':'19:05:32','donc_sinon':'19:05:32','cancel_insert':'19:05:58','cancel_first':'19:05:58',
'cancel_underlined':'19:06:21','cancel_de':'19:06:21','cancel_equality':'19:09:21','bottom_start':'19:09:24',
'bottom_indices':'19:09:28','bottom_ens':'19:09:35','bottom_last':'19:09:47','cancel_block':'19:09:59','bottom_F':'19:10:11'}

result=dict(scan='033',manuscript_page='32.',reader='B',line_count=27,
    line_count_method='27 main handwritten baselines; folio, sideways note and two interlinear insertions recorded separately. Formula wraps are counted as baselines, not invented displays.',
    image_dimensions=[1679,2359],bottom_half_y_offset=1099,
    image_views=[
        dict(image='whole',path='source/SP114_CW_156-5_scans/J156-5-04_156-5_scan033.jpg',utc='2026-11-20 18:57:53 UTC',purpose='one layout/inventory pass',count=1),
        dict(image='a',path='source/SP114_CW_156-5_scans/J156-5-04_156-5_scan033_a.jpg',utc='2026-11-20 18:58:18 UTC',purpose='one line-by-line token pass against C and H, including agreements',count=1),
        dict(image='b',path='source/SP114_CW_156-5_scans/J156-5-04_156-5_scan033_b.jpg',utc='2026-11-20 18:58:37 UTC',purpose='one line-by-line token pass against C and H, including agreements',count=1)],
    crop_views=[dict(locus=m['locus'],crop=m['crop'],box=m['box'],rotation=m['rotation'],
        utc='2026-11-20 '+times[m['locus']]+' UTC') for m in manifest],
    changes=changes,unresolved=unresolved,inventory=inventory,
    hand_habits=[
        dict(habit='Plain F often has a bent or hooked upper arm; a middle arm and upright still distinguish it from a script family.',evidence='Initial F at top_initial and ordinary Fs throughout this page; the exceptional looped (=F/P) remains locally open.',scope='scan033; do not claim every F variant resolved',witness_effect='C opening F/calligraphic doubt resolved; new local F/P doubt at bottom.'),
        dict(habit='Low joined minims can erase word boundaries, while ascenders and descenders survive.',evidence='Rotated margin va se simplifier; il suffirait insertion; Sinon on aurait.',scope='relevant occurrences on scan033 only',witness_effect='C margin noun and H insertion/conditional words differ from visible letter sequence.'),
        dict(habit='Cancellation may cross high above or through letters; a low stroke can instead be an underline.',evidence='bien stroke lies below bodies; long strate underline is separate from the large oblique deletions.',scope='separate state decision at each locus',witness_effect='C bien deletion questioned; both witnesses’ final Prouvons cancellation scope questioned.'),
        dict(habit='Very compact elevated star-like marks resemble k or a cross.',evidence='I and I′ superscripts in bottom_indices.',scope='both occurrences on this page',witness_effect='C ambiguity retained, marked only at first occurrence.'),
        dict(habit='Primes are short raised isolated strokes and cannot be supplied from the proof’s subject.',evidence='Clear A′ forms beside the unprimed A in d’où A∈F.',scope='all primes checked in half pass, local decision cropped',witness_effect='H added prime removed at d’où A∈F.')],
    notation=[
        dict(symbol='F,G',meaning='plain capitals as written',evidence='Two arms/upright F at opening, G with inward terminal; shared table followed.',scope='page033, except local (=F/P) doubt'),
        dict(symbol=r'\preceq',meaning='comparison with curved upper and bowed lower stroke',evidence='car F′≼F at jedis_relation; H preccurlyeq is equivalent notation, not a different reading.'),
        dict(symbol=r'\ll',meaning='two leftward wedges',evidence='Inserted F′≪F at jedis_insertion; both tips visible.'),
        dict(symbol=r'A^{\circ(F)}',meaning='circle stratum superscript with parenthesized figure',evidence='Open small circle distinguishable from the adjacent worked-over marks; formulas read in full.'),
        dict(symbol=r'\varphi',meaning='map named in the cancelled b⇒c argument',evidence='On suppose insertion and φ(A′)=A; no empty-set use on this sheet.'),
        dict(symbol=r'I^{\unsure{\ast|k|+}}',meaning='upper mark remains asterisk/k/cross; preferred ast used unmarked on I′',evidence='Both superscript bodies have stem and short rightward branches.',scope='mark at first occurrence only'),
        dict(symbol=r'\overset{\sim}{\longrightarrow}',meaning='single rightward arrow with tilde label',evidence='Cancelled On suppose insertion; arrow head and tilde separately visible.'),
        dict(symbol=r'\Longleftrightarrow',meaning='double shaft with arrowheads at both ends',evidence='Renewed b⇔c heading at bottom_start.')],
    abbreviations=[
        dict(form='i.e.',expansion='id est',places='1°), Je dis, On suppose insertion',decision='Preserved with stops; no expansion in text.'),
        dict(form='él.',expansion='élément',places='2°), plus petit él.',decision='Preserved.'),
        dict(form='cf',expansion='confer / compare',places='margin and cf lemme plus bas',decision='No period supplied.'),
        dict(form='qed',expansion='quod erat demonstrandum',places='Donc conclusion',decision='Lower-case unexpanded form and surrounding punctuation preserved.'),
        dict(form='ens',expansion='ensembles',places='bottom paragraph',decision='No period added; H ens. differs from ink.')],
    notes=[
        dict(type='method',text='Rules, both witnesses, all 30 supplied difference rows, C doubt sheet and current notation table read. Whole once, halves once each; remaining decisions used saved crops. No OCR, external research or TeX compilation.'),
        dict(type='claim_unverified',text='The two numbered parts assert opposite set inclusions F\\G⊂F′\\G′ and F′\\G′⊂F\\G. This is a source claim, not a checked theorem.'),
        dict(type='claim_unverified',text='Je dis claims equality of the two A-strata for F and F′, citing a lemma below and inserting that F′≪F would suffice. No missing lemma has been imported.'),
        dict(type='author_slip_or_mismatch',text='The parenthesis after A′=A has d’où A∈F with clear unprimed A. Retained despite H’s A′ and the surrounding proof’s subject.'),
        dict(type='author_revision',text='The b⇒c proof is abandoned under oblique strokes and restarts b⇔c below. Exact cancellation of its final Prouvons sentence is visually open.'),
        dict(type='author_punctuation',text='The bottom parenthesis opened before parties is not closed by an additional outer parenthesis before the final period; source imbalance retained.'),
        dict(type='author_question_or_check',text='No explicit author question was confidently identified on this page. The cf lemme plus bas reference is a forward reference, not a verification supplied by this reader.'),
        dict(type='open_math_check',text='Whether the claimed stratum equality follows under the written comparison remains unchecked. Any later mathematical test should be logged as such and must not alter clear ink.'),
        dict(type='open_math_check',text='The bottom index definitions and relation b⇔c continue beyond the visible final On a; no continuation or missing close has been supplied.'),
        dict(type='editorial_exclusion',text='H’s prose descriptions of the margin and cancelled insertion are not source text. Their observed physical content is represented by margin/TikZ and insertion/deletion macros.'),
        dict(type='image_view_accounting',text='A tool result containing cancel_equality/bottom_start was truncated before either image could be read. Only the successful individual inspections at 19:09:21 and 19:09:24 are counted.')],
    check_events=[],
    C_state_audit=state_audit,C_doubt_audit=c_doubt_audit,C_formula_doubt_audit=formula_doubt_audit,
    difference_coverage=coverage,second_boxes=second_boxes,
    agreement_audit=dict(completed=True,basis='Both halves read token by token against both witnesses; all agreed words, formulas and punctuation included in the visual pass. Agreement was not treated as evidence.',
        additional_agreement_doubts=['first underlined inclusion/membership sign','bien deletion state','final Prouvons deletion scope','bottom (=F/P) letter']),
    source_claims_verified=False,
    files=dict(draft='deliverable/review/scan033_draft.tex',crop_manifest='deliverable/review/scan033_crop_manifest.json'))

out=REVIEW/'scan033_findings.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(result[k]) for k in ['changes','unresolved','inventory','C_state_audit','C_doubt_audit','difference_coverage','second_boxes','crop_views']},ensure_ascii=False))
