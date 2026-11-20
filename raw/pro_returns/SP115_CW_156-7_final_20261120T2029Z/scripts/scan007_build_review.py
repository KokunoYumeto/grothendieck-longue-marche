from pathlib import Path
import json, csv, re

ROOT=Path('/workspace/scratch/ddf8babdc42e')
OUT=ROOT/'out/review'
C=(ROOT/'packets/scan007/C.tex').read_text()
manifest=json.loads((OUT/'scan007_crop_manifest.json').read_text())
crops={c['name']:c for c in manifest['crops']}
rel=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
hook=r'\mathrel{\tikz[x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.35,.42) and (1.38,.23) .. (1.28,.2);}}'

proposed=C
replacements=[
 (r'\unsure{\mathscr F|\mathcal F}',r'\unsure{\mathscr F|\mathcal F|\mathfrak F}'),
 (r'\unsure{élément}.}',r'\unsure{élément}\unsure{.}}'),
 (r'\unsure{termes|terme}',r'termes'),
 (r'\deleted{Posant $X\ll Y\ \unsure{\Longleftrightarrow|\Longrightarrow}\ \unsure{Y}$ \unsure{contient}} \deleted{$\forall X,Y\in M,\ X\ll$ \unsure{défini}} \deleted{\unsure{est|ent} \unsure{minimal|minimum}}',
  r'\deleted{\unsure{Posant|Posons} $X\ll Y\ \overset{\unsure{\mathrm{déf}}}{\unsure{\Longleftrightarrow|\Longrightarrow}}\ \unsure{Y|X}$ \unsure{contient}} \inserted{\deleted{$\forall X,Y\in M,\ X\ll$}} \inserted{\deleted{\unsure{est|ent} \unsure{minimal|minimum}}}'),
 (r'\deleted{plus petit élément}',r'\deleted{\unsure{plus petit élément}}'),
 (r'\inserted{élément \unsure{minimal|minimum|privilégié}}',r'\inserted{élément minimal}'),
 (r'(\unsure{posons|posant} $X\overset{\circ}{\ll}Y$',r'(posons $X\overset{\circ}{\ll}Y$'),
 (r'\unsure{\widetilde{\mathscr F}|\mathscr F}',r'\widetilde{\mathscr F}'),
 ('un choix de structure de plus','un choix de structure en plus'),
 (r'\mathrm{Omb}(x)',r'\mathrm{Omb}(\unsure{x|X})'),
 (r'M_{\ll x}',r'M_{\ll \unsure{x|X}}'),
 (r'\unsure{GF|GE}','GF'),
 ('pas néc. spacieux',r'pas néc. \unsure{spacieux|spécieux}'),
]
for old,new in replacements:
    assert old in proposed, old
    proposed=proposed.replace(old,new,1)
(OUT/'scan007_proposed.tex').write_text(proposed)

changes=[]
def add(n,place,c,h,final,shows,conf,kind,crop,ac=False,ah=True,mh=False,con=True):
    p=crops[crop]
    changes.append(dict(id=f'S007-{n:03}',place=place,C=c,H=h,final=final,scan_shows=shows,
      confidence=conf,kind=kind,crop=p['file'],box=p['box'],against_C=ac,against_H=ah,
      marked_in_H=mh,consequential=con))

add(1,'cancelled opening axiom, ambient-set letter',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}',
    'The letter has two rounded rises and a longer right stem. The cancellation and ordinary handwritten form do not securely select a mathematical alphabet. C primary retained, with its doubt.', 'low','misread symbol or index','first_cancelled_axiom')
add(2,'first family letter; recurring family alphabet on this page',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F|\mathfrak F}',
    'The first family F has a curved top, central stem and lower turn. The cancellation does not settle script versus calligraphic or Gothic typing. Added the H alphabet as an admissible alternative, and retained the C primary at the other occurrences.', 'low','misread symbol or index','first_cancelled_axiom')
add(3,'end of cancelled opening axiom',r'\unsure{élément}.','élément',r'\unsure{élément}\unsure{.}',
    'A long cancellation runs beyond the last letters. A separate final stop is not securely distinguishable from its endpoint; the C stop is therefore retained only as doubtful.', 'low','other','first_cancelled_axiom',con=False)
add(4,'left margin, lines 2–3','sans référence à F ou à tilde F',r'\ill{} \ill{} F \ill{} tilde F','sans référence à F ou à tilde F',
    'The crop shows the s-a-n-s sequence, the long f descender in référence, and the short ou followed by à before the second F. These words are readable; the two F forms differ by a separate tilde.', 'high',r'readable ink left as \ill{}','margin_main',mh=True)
add(5,'left margin, overwritten number after underlined At',r'\deleted{\unsure{6}}5','5',r'\deleted{\unsure{6}}5',
    'The final 5 is dark and clear. A rounded underlying stroke survives inside it, but it is not sufficiently separable to remove the C doubt on 6. H omits this underlying numeral in the transcription.', 'low','deletion state (struck given live or live given struck)','margin_main')
add(6,'left margin, underline beneath At',r'\uline{\mathrm{At}}','At',r'\uline{\mathrm{At}}',
    'A separate horizontal stroke underlines exactly At, ending before the overwritten numeral.', 'high','other','margin_main',con=False)
add(7,'left margin, end of line directement en termes',r'\unsure{termes|terme}','termes','termes',
    'The enlarged right end shows a terminal returning stroke after the e of termes. Extending the initial frame to x=465 includes the final s. This resolves the C doubt to its existing primary.', 'high','other','margin_main',ah=False,con=False)
add(8,'upward-right arrow attached to first margin note',r'\nearrow','arrow described in editorial note',r'\nearrow',
    'A diagonal shaft from the note ends in a distinct upper-right arrowhead. The arrow is source ink; its description in H is editorial, not a typed reproduction.', 'high','drawing or diagram','margin_main',mh=True,con=False)
add(9,'cancelled beginning of axiom 4(a)','Posant','Posons',r'\unsure{Posant|Posons}',
    'The last surviving tall stroke favours t and thus Posant. The cancellation covers the intervening letters, so Posons is retained as an alternative rather than declaring every letter plain.', 'medium','misread word','a_cancelled_start')
add(10,'cancelled axiom 4(a), first relation X to Y',r'X\ll Y',r'X\overset{\circ}{\ll}Y',r'X\ll Y',
    'The baseline has the two left-facing chevrons. The interlinear cancelled writing lies above them; no independent small circle like those in the live b), At 5 and posons formulas is separable here.', 'medium','misread symbol or index','a_cancelled_start')
add(11,'cancelled axiom 4(a), label above equivalence arrow',r'\unsure{défini} after the interlinear X\ll',r'\overset{\mathrm{déf}}{\Longleftrightarrow}',r'\overset{\unsure{\mathrm{déf}}}{\unsure{\Longleftrightarrow|\Longrightarrow}}',
    'The short three-letter group is above the double-shaft arrow. A descending f is visible, but no following ini is present. Its placement is a label on the arrow, not a full word after the interlinear formula. Cancellation still warrants a doubt on the abbreviation.', 'medium','abbreviation expanded or spelling modernised','a_cancelled_start',ac=True,ah=False)
add(12,'cancelled axiom 4(a), letter following labelled arrow',r'\unsure{Y}','X',r'\unsure{Y|X}',
    'A forked/crossed heavy letter remains where the strike meets it. The lower branch does not securely discriminate Y from X. C primary Y is retained and H X admitted explicitly.', 'low','misread symbol or index','a_cancelled_start')
add(13,'cancelled axiom 4(a), word after that letter',r'\unsure{contient}',r'\ill{}',r'\unsure{contient}',
    'The initial rounded c/o strokes, tall t and final rising stroke are partly visible beneath the strike; the complete word is not plain. Retain the C candidate, without resolving it.', 'low','omission','a_cancelled_start',mh=True)
add(14,'cancelled interlinear formula above the opening of 4(a)',r'\deleted{\forall X,Y\in M,\ X\ll}',r'part of one struck line after Posons',r'\inserted{\deleted{\forall X,Y\in M,\ X\ll}}',
    'This smaller formula lies above the baseline Posant X≪Y and has its own horizontal cancellation. It is an insertion subsequently cancelled. Its terminal X≪ is visible; no extra final Y is supplied. The precise linear order of this draft remains provisional.', 'high','insertion or placement','a_cancelled_start',ac=True)
add(15,'cancelled interlinear words over the right end of 4(a)',r'\deleted{\unsure{est|ent} \unsure{minimal|minimum}}',r'minimal at end of one struck line',r'\inserted{\deleted{\unsure{est|ent} \unsure{minimal|minimum}}}',
    'The words occupy the higher interlinear band over the cancelled contient phrase and are crossed separately. Marking only deletion loses their inserted placement. Both lexical doubts remain.', 'medium','insertion or placement','a_cancelled_start',ac=True)
add(16,'first word in cancelled interlinear est/ent minimal',r'\unsure{est|ent}','omitted',r'\unsure{est|ent}',
    'A short word precedes minimal in the interlinear band. Its final tall crossing supports est, but cancellation prevents a secure full reading. H does not represent that word.', 'low','omission','a_cancelled_start')
add(17,'cancelled phrase after il y a un','plus petit élément',r'\struck{\ill{}}',r'\deleted{\unsure{plus petit élément}}',
    'The baseline phrase is crossed throughout. Parts of plus, the two tall strokes of petit and the ending of élément remain, supporting C, but the broad strike hides enough letters to add a doubt to the whole phrase.', 'medium',r'readable ink left as \ill{}','a_replacement',mh=True)
add(18,'live replacement above plus petit élément',r'\inserted{élément minimal}',r'\add{minimal}',r'\inserted{élément minimal}',
    'A complete separate élément is visible before minimal above the cancelled phrase. H omits that noun.', 'high','omission','a_replacement')
add(19,'word minimal in that live insertion',r'\unsure{minimal|minimum|privilégié}','minimal','minimal',
    'The ending is a clear a followed by a tall l, rather than the u-m of minimum. There is no initial pr- or long intervening sequence for privilégié. This resolves C to its primary.', 'high','other','a_replacement',ah=False,con=False)
add(20,'dans before the definition of tilde Y superscript X',r'\inserted{dans}','dans as baseline text',r'\inserted{dans}',
    'The short word is raised above the original line immediately before the set definition. It is a source insertion, not merely ordinary baseline prose.', 'high','insertion or placement','a_definition_insertion')
add(21,'parenthetical posons definition, above the deleted i.e. formula',r"\inserted{(\unsure{posons|posant} X\overset{\circ}{\ll}Y si c'est Y)}",r'\struck{posons X\overset{\circ}{\ll}Y si \ill{} ...}',r"\inserted{(posons X\overset{\circ}{\ll}Y si c'est Y)}",
    'The small parenthetical sentence is above the horizontal strike and ends with Y) below it. The strike crosses the separate lower i.e. formula, not posons or si c’est. The last letters of posons are rounded o-n-s, resolving the live C doubt to its primary.', 'high','deletion state (struck given live or live given struck)','a_definition_insertion',mh=True)
add(22,'end and parentheses of the live posons insertion',"si c'est Y) with opening (",r'si \ill{} with no represented enclosing parentheses',"(posons ... si c'est Y)",
    'An opening curve precedes posons; c’est is legible after si, and the final Y is followed by a separate closing parenthesis on the lower continuation. These are live insertion text.', 'high','omission','a_definition_insertion',mh=True)
add(23,'number of axiom now reading At_M 6',r'\deleted{\unsure{5}}6','6',r'\deleted{\unsure{5}}6',
    'The final 6 is superposed on another numeral, with an angular upper trace compatible with 5. The underlying digit is not fully separable. H notes the overwrite editorially but omits it from source text.', 'low','deletion state (struck given live or live given struck)','at6_formula',mh=True)
add(24,'number of axiom now reading At_M 5',r'\deleted{\unsure{6}}5','5',r'\deleted{\unsure{6}}5',
    'The final 5 overlies a rounded lower trace compatible with 6. Keep the underlying numeral doubtful. H notes the overwrite editorially but omits it from source text.', 'low','deletion state (struck given live or live given struck)','at5_formula',mh=True)
add(25,'curved transposition drawing left of At_M 6 and At_M 5','two curved strokes, upper one with arrowhead','described in editorial note','C TikZ drawing retained',
    'There are two distinct curved strokes: a lower C-shaped curve without a visible head and an upper rising curve whose terminal diagonal has a head toward the upper numeral. Their two-part shape is reproduced, not converted into explanatory source prose.', 'high','drawing or diagram','interchange_arrow',mh=True,con=False)
add(26,'D’autre part paragraph, line after de type fini','on peut laisser tomber',r'\add{bien \uncertain{connues}} \ill{}','on peut laisser tomber',
    'The baseline shows on, the p stem and terminal t of peut, the long l and s sequence of laisser, and the t/b stems of tomber. This is continuous baseline prose, not the inserted bien connues of H.', 'high','misread word','dautrepart',mh=True)
add(27,'family letter after l’élément de structure',r'\unsure{\widetilde{\mathscr F}|\mathscr F}',r'\widetilde{\mathfrak F}',r'\widetilde{\mathscr F}',
    'At the right edge, a separate short stroke stands above the F top stroke, confirming the tilde. The family alphabet remains covered by the first-occurrence doubt; only the presence of the tilde is resolved here.', 'medium','other','dautrepart',ah=False,con=False)
add(28,'interlinear au profit de relation',r'\inserted{au profit de relation,}',r'\add{\ill{} au profit de relation}',r'\inserted{au profit de relation,}',
    'The raised phrase starts directly with au. No separate preceding word is visible, and a comma follows the relation. Its attachment is between the structure-family clause and et remplacer.', 'high','text not on the page','dautrepart',mh=True)
add(29,'end of et remplacer line','par (a) de la','par (a) et la','par (a) de la',
    'After (a), the first letter is a looped d followed by e; it is not the short e plus tall t of et.', 'high','misread word','dautrepart')
add(30,'cancelled At_M label before (tf)',r'\unsure{1|0}','not represented',r'\unsure{1|0}',
    'Dark small strokes remain immediately before the parenthesized tf label. They do not securely separate 1 from 0. C’s doubtful numeral is retained for adjudication, rather than silently omitted.', 'low','omission','cancelled_tf_axiom')
add(31,'parenthesized qualifier in the cancelled At_M line',r'(\mathrm{tf})',r'(\ill{})',r'(\mathrm{tf})',
    'Within the parentheses a tall crossed t and descending f remain distinguishable despite the long cancellation. No expansion is made.', 'medium',r'readable ink left as \ill{}','cancelled_tf_axiom',mh=True)
add(32,'small cancellation before page/p. 5',r'\deleted{\unsure{At}}',r'\struck{\ill{}}',r'\deleted{\unsure{At}}',
    'Several diagonal strokes cross a short capital-like group. The A outline is partly visible but its following t is not wholly plain; retain At as doubtful.', 'low',r'readable ink left as \ill{}','page5_condition',mh=True)
add(33,'live page reference immediately after that cancellation',r'\unsure{page|p.} 5',r'\uncertain{Voir} p. 5',r'\unsure{page|p.} 5',
    'One short connected group occurs before the numeral 5. The initial descending/looped stroke is compatible with p; the following compressed strokes do not securely settle full page versus p. No separate preceding Voir can be isolated.', 'low','misread word','page5_condition',mh=True)
add(34,'relation after et la condition b sur',r'{relation}^{*}','relation',r'{relation}^{*}',
    'A distinct dark asterisk is placed above and to the right of the crossed-chevron glyph. This decoration is absent from H.', 'high','omission','page5_condition')
add(35,'arrow in slanted margin condition',r'\unsure{'+hook+r'|\Longrightarrow}',r'\Longrightarrow',r'\unsure{'+hook+r'|\Longrightarrow}',
    'After rotation the upper shaft curves downward at the right, while the shorter lower shaft ends without a separate lower diagonal. C’s explicit rounded form is the primary; the conventional implication reading remains an alternative.', 'medium','misread symbol or index','margin_condition')
add(36,'Dans le cas général paragraph, words around relation','quand on a simplement','grâce à laquelle','quand on a simplement',
    'The q descender starts quand; on and a follow on that line, and simplement begins the next. There is no gr- initial and no longer laquelle sequence.', 'high','misread word','general_case',mh=True)
add(37,'same paragraph, participle after relation','satisfaisant','satisfait','satisfaisant',
    'The word continues beyond the second s into the final a-n-t sequence; the descending f is clear in the middle. H loses the participial ending.', 'high','misread word','general_case')
add(38,'Phi de t.f. in definition of tilde F_tf',r'\inserted{\Phi\ \text{de t.f.}}','Phi de t.f. as live baseline text',r'\inserted{\Phi\ \text{de t.f.}}',
    'Phi de t.f. is written above the definition line; a curved insertion stroke leads down before de M. H’s note recognizes the addition but the transcription lacks its source-state mark.', 'high','insertion or placement','Ftf_definition',mh=True)
add(39,'ambient-set phrase at end of first definition line',r'de M,\leq',r'de (M,\leq)',r'de M,\leq',
    'The curved stroke is before de and leads up toward the insertion Phi de t.f.; it is not an opening parenthesis before M. No matching closing parenthesis follows ≤.', 'high','text not on the page','Ftf_definition')
add(40,'cancelled words beneath telles que',r'\deleted{\unsure{formées} \unsure{t.q.}}','omitted, described only as a crossed-out word',r'\deleted{\unsure{formées} \unsure{t.q.}}',
    'The long strike crosses a word with initial f and following connected minims, then a separate short abbreviation. The cancellation conceals parts of both, so formées and t.q. remain doubtful rather than expanded or resolved.', 'low','omission','formees_tq',mh=True)
add(41,'replacement telles que in definition',r'\inserted{\text{telles que :}}','telles que as ordinary text',r'\inserted{\text{telles que :}}',
    'The words are above the crossed-out formées/t.q. line and are not crossed. H mentions this placement editorially but does not mark it in the source transcription.', 'high','insertion or placement','formees_tq',mh=True)
add(42,'punctuation following inserted telles que','telles que :','telles que','telles que :',
    'Two vertically separated dark points follow que, above the strike and before the formula; they form a colon.', 'high','other','formees_tq',con=False)
add(43,'Pour avoir paragraph, un choix de structure','de plus','en plus','en plus',
    'The short word begins with a small e loop and ends in n; there is no tall initial d ascender. H is supported at this place.', 'high','misread word','enplus',ac=True,ah=False)
add(44,'Pour avoir paragraph, abbreviation ens',"l'ens ordonné",r"l'ens.\ ordonné","l'ens ordonné",
    'Between the final s of ens and the following ordonné the paper is blank. No abbreviation stop as dark as the surrounding ink is visible.', 'high','other','ens_ellipsis',con=False)
add(45,'first lower display, operator name','Mulomb(F)','Multomb(F)','Mulomb(F)',
    'After Mul there is a rounded o, followed by connected m and the final b. There is no separate t stem or cross-stroke between l and o.', 'high','misread word','Fstar')
add(46,'second lower display, operator name','Mulomb(F)','Multomb(F)','Mulomb(F)',
    'The repeated operator likewise has the short Mul-o-m-b sequence without an intervening t.', 'high','misread word','mulomb_definition')
add(47,'où at left of second lower display',r'\deleted{\text{où}}','où as live prose',r'\deleted{\text{où}}',
    'A separate horizontal stroke crosses the small où at the left of the display. It is a cancelled word, not a live conjunction introducing a new display.', 'high','deletion state (struck given live or live given struck)','mulomb_definition')
add(48,'cancelled sign after opening brace in Mulomb definition',r'\deleted{\unsure{X}}','omitted in transcription; mentioned in note',r'\deleted{\unsure{X}}',
    'A crossed sign precedes Omb(x). The two diagonal remnants favour X, but the overlying loops and cancellation prevent a secure all-strokes reading. Retain the C doubt.', 'low','omission','mulomb_definition',mh=True)
add(49,'argument of Omb inside the Mulomb definition','x','X',r'\unsure{x|X}',
    'The crossed glyph is smaller than the later X after the condition bar, favouring lower case. Its two strokes have no case-specific form, so the difference remains explicit rather than normalized.', 'medium','misread symbol or index','mulomb_definition')
add(50,'end of Mulomb defining set','closing brace without comma','closing brace followed by comma','closing brace without comma',
    'After the lower endpoint of the closing brace there is no separate comma at the formula baseline. The following definition begins on the next line.', 'high','other','mulomb_definition',con=False)
add(51,'subscript after final M in Omb X definition',r'M_{\ll x}',r'M_{\ll X}',r'M_{\ll\unsure{x|X}}',
    'The subscript has two left-facing chevrons followed by a small cross. Lower-case x is C’s plausible primary, but reduced subscript size prevents a secure capital/lower-case distinction.', 'low','misread symbol or index','omb_definition')
add(52,'start of final parenthesis','cf Scholie',r'cf.\ Scholie','cf Scholie',
    'The f descender is followed directly by the space before Scholie; no separate stop appears after cf.', 'high','other','reference',con=False)
add(53,'reference initials after Scholie',r'\unsure{GF|GE}','GF','GF',
    'The second capital has a top bar and middle bar, but no bottom bar extending right. This is F; the C primary GF is resolved on the crop.', 'high','other','reference',ah=False,con=False)
add(54,'final reference phrase after et axiomes','ou mieux à la page 32',r'en \uncertain{nombre} de \ill{} p. 32','ou mieux à la page 32',
    'The first line ends in ou. The next starts with m-i-e-u-x, then accented à, la, and the compact full word page with its p and g descenders before 32. H’s en nombre de and abbreviation p. do not fit these strokes.', 'high','misread word','reference',mh=True)
add(55,'underline in final reference',r'\uline{page 32}','p. 32 without underline',r'\uline{page 32}',
    'One long separate stroke runs beneath the word page and both digits 32, stopping before the closing parenthesis.', 'high','other','reference',con=False)
add(56,'connection before sous-atelier','comme sous-atelier','comme un sous-atelier','comme sous-atelier',
    'The line ends in comme and the next starts directly with sous-atelier. There is no extra un on either side of the line break.', 'high','text not on the page','reference')
add(57,'adjective in final pas néc. parenthesis','spacieux','spécieux',r'\unsure{spacieux|spécieux}',
    'The faint short vowel after sp favours an a-like rounded stroke and no accent is visible over it. Faintness prevents a confident a/e distinction, so C’s spacieux remains primary with H’s spelling as the alternative.', 'medium','misread word','spacieux')

doubts=[
 {'place':'cancelled opening axiom, M','reading':r'M','alternatives':[r'\mathcal M'],'confidence':'low','reason':'Ordinary rounded handwritten capital under a strike does not securely encode alphabet; retained C doubt.'},
 {'place':'cancelled opening axiom, Phi','reading':r'\Phi','alternatives':[r'\varphi'],'confidence':'medium','reason':'A vertical staff and horizontal foot favour capital Phi, but cancellation overlaps the bowl; C doubt not resolved.'},
 {'place':'family alphabet, first occurrence and thereafter','reading':r'\mathscr F','alternatives':[r'\mathcal F',r'\mathfrak F'],'confidence':'low','reason':'Curved capital F forms are visible, but a specific mathematical font is not certified; first occurrence marked once.'},
 {'place':'cancelled opening axiom, final word','reading':'élément','alternatives':[],'confidence':'medium','reason':'Parts of the last letters intersect the strike; not every letter is plain.'},
 {'place':'cancelled opening axiom, final stop','reading':'.','alternatives':['no distinct punctuation'],'confidence':'low','reason':'A stop cannot securely be separated from the long cancellation endpoint.'},
 {'place':'margin overwritten numeral','reading':'underlying 6, final 5','alternatives':['underlying numeral not separable'],'confidence':'low','reason':'Retained C deleted-numeral doubt; overwrite is clear but underlying identity is not.'},
 {'place':'cancelled Posant','reading':'Posant','alternatives':['Posons'],'confidence':'medium','reason':'Tall last stroke favours t, but intervening cancellation prevents certainty.'},
 {'place':'cancelled first arrow','reading':r'\Longleftrightarrow','alternatives':[r'\Longrightarrow'],'confidence':'low','reason':'Two shafts are visible, but the left end meets the strike and interlinear formula.'},
 {'place':'label on cancelled first arrow','reading':'déf','alternatives':[],'confidence':'medium','reason':'Short d/e/f-like label rather than défini; accent and all letter joins remain partly covered.'},
 {'place':'letter after cancelled labelled arrow','reading':'Y','alternatives':['X'],'confidence':'low','reason':'Heavy crossed fork at the cancellation intersection does not discriminate the lower arm.'},
 {'place':'cancelled contient','reading':'contient','alternatives':[],'confidence':'low','reason':'Word outline and tall t strokes survive, but its middle is crossed.'},
 {'place':'cancelled interlinear est/ent','reading':'est','alternatives':['ent'],'confidence':'low','reason':'The short word has an ending tall stroke, while the middle is crossed.'},
 {'place':'cancelled interlinear minimal/minimum','reading':'minimal','alternatives':['minimum'],'confidence':'low','reason':'Ending intersects cancellation; live minimal elsewhere is not used to settle the cancelled occurrence.'},
 {'place':'cancelled plus petit élément','reading':'plus petit élément','alternatives':[],'confidence':'medium','reason':'Several underlying letters remain visible, but the broad strike hides enough strokes to mark the whole candidate doubtful.'},
 {'place':'cancelled lower formula after the live posons insertion','reading':'i.e.','alternatives':[],'confidence':'low','reason':'Small introductory letters and dots lie directly under the strike; retained C doubt.'},
 {'place':'At_M 6 overwritten label','reading':'underlying 5, final 6','alternatives':['underlying numeral not separable'],'confidence':'low','reason':'Dark final 6 overlays angular remnants; old digit not fully legible.'},
 {'place':'At_M 5 overwritten label','reading':'underlying 6, final 5','alternatives':['underlying numeral not separable'],'confidence':'low','reason':'Dark final 5 overlays rounded remnants; old digit not fully legible.'},
 {'place':'cancelled At_M (tf) label','reading':'1','alternatives':['0'],'confidence':'low','reason':'Small dark strokes before (tf) are partly merged with parentheses/cancellation; C numeral remains provisional.'},
 {'place':'cancelled group before page 5','reading':'At','alternatives':[],'confidence':'low','reason':'Dense diagonal cancelling strokes obscure the group; initial A partly survives.'},
 {'place':'first live reference to page 5','reading':'page','alternatives':['p.'],'confidence':'low','reason':'One compressed group before 5 is clear in extent, but its interior does not securely settle full word versus abbreviation.'},
 {'place':'slanted marginal implication sign','reading':'two horizontal shafts, upper one with rounded downturned end','alternatives':[r'\Longrightarrow'],'confidence':'medium','reason':'The upper shaft turns down rather than forming a clear angular arrowhead; rounded shape retained in TikZ with the C uncertainty.'},
 {'place':'cancelled definition words','reading':'formées t.q.','alternatives':[],'confidence':'low','reason':'The long strike merges with the lower-case joins of formées and with the short abbreviation; both C doubts retained.'},
 {'place':'cancelled sign before Omb(x)','reading':'X','alternatives':[],'confidence':'low','reason':'Diagonal remnants favour X, but heavy cancellation conceals the complete underlying sign.'},
 {'place':'Omb argument in Mulomb definition','reading':'x','alternatives':['X'],'confidence':'medium','reason':'Smaller than the neighbouring capital X but with identical crossed-stroke construction; primary C retained with explicit case doubt.'},
 {'place':'final M subscript in Omb definition','reading':'x','alternatives':['X'],'confidence':'low','reason':'Reduced subscript size removes a secure case criterion; do not normalize to the capital used elsewhere in the formula.'},
 {'place':'spacieux in final parenthesis','reading':'spacieux','alternatives':['spécieux'],'confidence':'medium','reason':'Faint a/e letter favours C; absence of a visible accent alone does not wholly settle the vowel.'},
 {'place':'linear ordering of the cancelled drafts at the start of a)','reading':'C’s local sequence, with interlinear additions marked and déf moved to its arrow','alternatives':['different drafting sequence of the cancelled lines'],'confidence':'low','reason':'Two interlinear cancelled fragments partly overlap the baseline draft; source position is visible but a unique temporal order is not certified.'},
]

inventory=[
 ('page numeral','text','top centre, x790–848 y20–75','6'),
 ('cancelled first axiom','deletion','upper main block, y62–186','At_M 4: ∀X∈M, Φ∈tilde F'),
 ('main label and cancelled draft','deletion','y160–235','At_M 4 a) Posant X≪Y'),
 ('cancelled interlinear formula','insertion','above cancelled draft at y170–205','∀X,Y∈M, X≪; déf above arrow'),
 ('cancelled interlinear words','insertion','above right end of cancelled draft','est/ent minimal/minimum'),
 ('live opening of 4(a)','text','y221–302','Si X≪Y, alors il y a un'),
 ('old minimum phrase','deletion','y260–315','plus petit élément'),
 ('replacement minimum phrase','insertion','above cancelled phrase','élément minimal'),
 ('inserted preposition','insertion','before tilde Y^X definition','dans'),
 ('set in 4(a)','display','right upper block, y222–300','tilde Y^X={Z∈tilde Y|X≪Z}'),
 ('deleted characterization','deletion','below set definition','i.e. X≪Y′≤Y⇒Y′=Y'),
 ('live posons parenthesis','insertion','between set definition and deleted characterization, final Y) below','(posons X circle-≪ Y si c’est Y)'),
 ('first margin note','margin note','left margin, y236–454','J’ai exprimé At [6 overwritten by 5] sans référence'),
 ('arrow from first margin note','drawing','top-right of that margin note','single diagonal upper-right arrow'),
 ('part b display','display','y306–385','b) Alors X circle-≪ Y, X circle-≪ Y′'),
 ('axiom 6 display with overwritten numeral','display','y379–460','At_M [5 overwritten by 6] Si X relation Y'),
 ('axiom 5 display with overwritten numeral','display','y454–550','At_M [6 overwritten by 5] X circle-≪ Y circle-≪ Z'),
 ('transposition strokes','drawing','left of two last axioms, y374–548','two curved strokes, upper one with head'),
 ('finite type paragraph','text','y569–785','D’autre part, pour des F à figures de type fini'),
 ('finite type insertion','insertion','above et remplacer','au profit de relation,'),
 ('cancelled finite type axiom','deletion','y781–863','At_M [1|0] (tf) Toute partie fermée majorée'),
 ('small cancelled group','deletion','left of first page 5 reference','At'),
 ('finite type condition continuation','text','y856–982','page/p. 5 (Toute partie...) et la condition b sur relation*'),
 ('slanted condition note','margin note','left margin, y855–1147','i.e. X relation Y et X′≤X, Y′≤Y'),
 ('general case paragraph','text','y972–1164','Dans le cas général, quand on a simplement'),
 ('definition of tilde F_tf','display','y1141–1304','tilde F_tf=ensemble des parties fermées'),
 ('Phi qualification','insertion','above first definition line','Φ de t.f.'),
 ('cancelled definition words','deletion','second definition line','formées t.q.'),
 ('replacement definition words','insertion','above cancelled words','telles que :'),
 ('choice of structure paragraph','text','y1290–1608','Pour avoir tilde F, il faut cependant'),
 ('interpretation introduction','text','between previous paragraph and lower displays','On peut aussi interpréter F en termes de'),
 ('F star display','display','y1695–1804','F*={Mulomb(F)|F∈F}⊂Fig(M)'),
 ('Mulomb definition','display','y1772–1881','Mulomb(F)={cancelled X Omb(x)|X∈tilde F}'),
 ('cancelled où','deletion','left of Mulomb definition','où'),
 ('cancelled sign before Omb','deletion','inside opening brace of Mulomb definition','X'),
 ('Omb definition','display','y1852–1944','Omb X={Y∈M|Y≪X}=M_{≪x}'),
 ('final reference and continuation','text','y1934–2155','(cf Scholie GF p. 28, et axiomes, ou mieux à la page 32), comme sous-atelier'),
]
inventory=[dict(element=e,kind=k,position=p,first_words_or_objects=f) for e,k,p,f in inventory]

notation=[
 {'form':'rounded capital with two rises','reading':r'M; alternative \mathcal M','place':'first cancelled axiom and all ambient-set occurrences','observation':'First occurrence retains alphabet doubt; subsequent occurrences follow its primary without silent alphabet normalization.'},
 {'form':'curved F with central stem and two bars','reading':r'\mathscr F; alternatives \mathcal F, \mathfrak F','place':'first cancelled axiom; margins; finite/general paragraphs; family displays','observation':'Family alphabet remains uncertain. Ordinary F arguments in Mulomb(F), F∈family and tilde F remain distinct from the family notation.'},
 {'form':'oval Phi with central staff and foot','reading':r'\Phi; alternative \varphi at first cancelled occurrence','place':'first cancelled axiom and tilde F_tf definition','observation':'Capital primary fits live Phi forms, but cancellation prevents resolving the first C doubt.'},
 {'form':'two opposed crossing chevrons with a central diamond-like enclosure','reading':rel,'place':'margin tuple; b); At_M 6; au profit de; starred condition b; both slanted-note relations; general-case paragraph; F_tf predicate','observation':'Retained C explicit drawing consistently. H’s repeated between is treated as an equivalent notation rendering, not independent semantic corrections. The star at the condition-b occurrence is a separate material decoration.'},
 {'form':'double left chevron with small open circle above','reading':r'\overset{\circ}{\ll}','place':'live posons definition, b), At_M 5','observation':'Circle is a distinct separate small loop, unlike an accidental intersection with the cancelled upper draft.'},
 {'form':'short label over the cancelled equivalence arrow','reading':r'\unsure{\mathrm{déf}}','place':'cancelled opening of 4(a)','observation':'Label is three-letter/abbreviated, not the expanded word défini. Placement is on the arrow.'},
 {'form':'two horizontal strokes, upper ending in rounded downward turn','reading':hook,'place':'slanted marginal implication','observation':'Custom primary retained with conventional Longrightarrow as alternative; both ends inspected after rotation.'},
 {'form':'star at upper right of relation','reading':r'{}^{*}','place':'condition b sur relation*','observation':'Independent ink decoration absent from H.'},
 {'form':'two overlapping numeral outlines','reading':'deleted doubtful old numeral before clear final 5 or 6','place':'margin At 5 and labels At_M 6, At_M 5','observation':'Do not remove underlying uncertainty from overwritten digits merely because the final number is clear.'},
 {'form':'compact operator without intervening t','reading':'Mulomb','place':'both lower occurrences','observation':'No t stem or crossbar occurs between l and o; H’s Multomb is not adopted.'},
 {'form':'small crossed x','reading':r'\unsure{x|X}','place':'Omb argument and final M subscript','observation':'Size favours lower case, but generic crossed strokes do not securely settle case in these positions.'},
 {'form':'underlined full word and numeral','reading':r'\uline{page 32}','place':'final reference','observation':'Source has the full word page and one underline across it and 32; not an expanded abbreviation.'},
]

hand_log=[
 {'habit':'compressed cursive can collapse several short letters into a low horizontal run','place':'on peut laisser tomber; quand on a simplement; ou mieux à la page; margin termes','observation':'Read tall p/l/t/f stems, final hooks and word spacing separately. These features favour C’s phrases over H’s alternative words; the faint spacieux remains open.'},
 {'habit':'a final cursive t is taller than the rounded s ending','place':'cancelled Posant versus live posons; satisfaisant','observation':'The live posons ending is clear. The cancelled Posant remains doubtful despite a tall final stroke; satisfaisant has the final a-n-t sequence.'},
 {'habit':'lower-case and capital x use the same two crossed strokes','place':'Omb(x), condition X∈tilde F, Omb X and M_{≪x}','observation':'Relative size helps but does not securely decide the two disputed positions. C lower-case primaries remain marked with X alternatives.'},
 {'habit':'compatibility relation is drawn with opposed crossing curved chevrons','place':'all nine local occurrences listed in notation','observation':'The geometric form is retained consistently; a genuine star is present only at the condition-b reference.'},
 {'habit':'insertions may be written in a narrow interlinear band and then struck again','place':'upper 4(a) draft','observation':'The ∀X,Y... and est/ent minimal fragments need both insertion and deletion states. The later posons parenthesis is live above the separate cancelled i.e. line.'},
 {'habit':'final axiom numerals are written over earlier numerals','place':'first margin note; At_M 6; At_M 5','observation':'Dark final 5/6 are readable; underlying old numbers remain only partly separable.'},
 {'habit':'full page is compressed but has both p and g descenders','place':'underlined page 32','observation':'Its compact form should not be reduced to p.; the earlier page/p. 5 group remains unresolved independently.'},
 {'habit':'French accent direction is not discriminative by itself','place':'référence, général, fermé/fermée, à in final reference','observation':'Where an accent stroke exists the ordinary French accent is used; no absent accent has been invented to decide faint spacieux/spécieux.'},
]

notes=[
 {'id':'N007-01','claim':'This review is limited to scan007 and its permitted packet/common instructions.','source':'packets/scan007/images.json, C.tex, H.tex, differences.tsv; RULES.md, PREAMBLE.tex, NOTATION.md','reasoning_if_any':'No outside text, other page, peer reading, OCR or external research was used.'},
 {'id':'N007-02','claim':'The upper cancelled draft has no certified unique linear drafting order.','source':'out/crops/scan007_a_cancelled_start.png','reasoning_if_any':'The two higher cancelled fragments overlap the baseline draft. The proposed text preserves the C local sequence, marks the fragments as inserted then deleted, and places déf above its visible arrow.'},
 {'id':'N007-03','claim':'The posons parenthesis is live insertion text; the i.e. characterization below it is cancelled.','source':'out/crops/scan007_a_definition_insertion.png','reasoning_if_any':'The horizontal strike follows the lower i.e. formula. The letters posons and si c’est are above it, with the final Y) on a short lower continuation.'},
 {'id':'N007-04','claim':'H editorial notes are not manuscript text.','source':'packets/scan007/H.tex','reasoning_if_any':'Its commentary on ratures, number permutations, marginal placement, and external references is excluded from proposed TeX. A note mentioning a source addition or deletion does not substitute for a source-state mark.'},
 {'id':'N007-05','claim':'No mathematical consistency argument has changed a clear or uncertain source letter.','source':'lower formula crops and retained case doubts','reasoning_if_any':'The same set expression contains capital X elsewhere, but the disputed Omb argument and final subscript are not silently capitalized.'},
 {'id':'N007-06','claim':'The conventional family alphabet and relation rendering remain local diplomatic choices.','source':'first-cancelled-axiom, margin, and display crops','reasoning_if_any':'The alphabet alternatives are marked at first occurrence. Equivalent repeated between/TikZ rendering is excluded from substantive-change counts; the missing star is included separately.'},
 {'id':'N007-07','claim':'Same-primary resolutions are not substantive departures from C.','source':'S007-007, S007-019, S007-021, S007-027, S007-053','reasoning_if_any':'termes, minimal, posons, tilde presence and GF are resolved from crops without changing C’s primary. Their against_C flags remain false.'},
 {'id':'N007-08','claim':'C’s cancelled-text doubts are retained unless all relevant letters are clear.','source':'all cancellation crops','reasoning_if_any':'No uncertain cancelled word or numeral has been promoted to certainty. défini is replaced by a still-doubtful abbreviated arrow label because no ini is visible.'},
 {'id':'N007-09','claim':'Two initial crop frames were extended only while the final source strokes remained unresolved.','source':'scan007_crop_manifest.json','reasoning_if_any':'margin_main right edge changed 447→465, and dautrepart 1671→1684. The manifest records both original and final boxes. No decided place received a new crop.'},
]

audit=[
 (r'\deleted{opening At_M 4 ... élément.}','retain deletion; keep all existing lexical/symbol doubts; add doubt to final stop','opening two lines','One long cancellation crosses both lines; all letters in the existing doubts are not plain. Crop first_cancelled_axiom.'),
 (r'\deleted{\unsure{6}}5','retain overwrite and old-digit doubt','left margin At label','Final 5 is clear, but underlying rounded numeral is only partly separable. Crop margin_main.'),
 (r'\deleted{Posant X≪Y ... contient}','retain deletion; mark Posant/Posons and Y/X; attach doubtful déf above arrow','4(a) old baseline','Strike crosses the entire draft; arrow label sits above it. Crop a_cancelled_start.'),
 (r'\deleted{∀X,Y∈M, X≪ défini}','mark insertion then deletion; move short doubtful déf to arrow label, omit unsupported ini','4(a) upper interlinear formula','Smaller formula has its own higher baseline and strike. Crop a_cancelled_start.'),
 (r'\deleted{est/ent minimal/minimum}','mark insertion then deletion; retain both word doubts','4(a) right interlinear fragment','Raised words above contient are separately crossed. Crop a_cancelled_start.'),
 (r'\deleted{plus petit élément}','retain crossed state; add lexical doubt','4(a) after il y a un','Broad strike crosses baseline phrase, while replacement is above. Crop a_replacement.'),
 (r'\inserted{élément minimal/minimum/privilégié}','retain insertion; resolve live final word to minimal','4(a) replacement','Two live words stand above the cancelled phrase; final a-l is clear. Crop a_replacement.'),
 (r'\inserted{dans}','retain insertion','4(a) before tilde Y^X','Short raised preposition immediately precedes definition. Crop a_definition_insertion.'),
 (r'\deleted{i.e. X≪Y′≤Y⇒Y′=Y}','retain deletion and i.e. doubt','4(a) lower characterization','Horizontal strike crosses this lower formula, with primes and ≤ still visible. Crop a_definition_insertion.'),
 (r'\inserted{(posons/posant X circle-≪ Y si c’est Y)}','retain insertion, live; resolve posons','4(a) parenthetical definition','Letters are above strike; final Y) continues below, outside the lower cancelled formula. Crop a_definition_insertion.'),
 (r'\deleted{\unsure{5}}6','retain underlying 5 doubt and final 6','At_M 6 label','Overwrite is visible; old numeral not wholly separable. Crop at6_formula.'),
 (r'\deleted{\unsure{6}}5','retain underlying 6 doubt and final 5','At_M 5 label','Overwrite is visible; old numeral not wholly separable. Crop at5_formula.'),
 (r'\inserted{au profit de relation,}','retain insertion with comma','finite type paragraph','Smaller phrase is between baseline structure clause and et remplacer. Crop dautrepart.'),
 (r'\deleted{At_M unsure{1|0}(tf) Toute partie ... t.f.}','retain full deletion and numeral doubt','finite type cancelled axiom','Single long strike crosses label and sentence. Crop cancelled_tf_axiom.'),
 (r'\deleted{\unsure{At}}','retain short deletion and doubt','before first page 5 reference','Dense diagonal cancelling strokes cover a short group. Crop page5_condition.'),
 (r'\inserted{\Phi de t.f.}','retain insertion','tilde F_tf definition','Raised group connects by curved insertion stroke before de M. Crop Ftf_definition.'),
 (r'\deleted{formées t.q.}','retain deletion and both C doubts','tilde F_tf definition lower line','Long horizontal strike covers baseline words. Crop formees_tq.'),
 (r'\inserted{telles que :}','retain insertion and colon','above formées t.q.','Live words above strike; two separate colon dots follow que. Crop formees_tq.'),
 (r'\deleted{où}','retain deletion','left of Mulomb definition','A short horizontal stroke crosses this small word. Crop mulomb_definition.'),
 (r'\deleted{\unsure{X}}','retain deletion and candidate doubt','after opening brace in Mulomb definition','A heavily cancelled crossed sign is visible before Omb. Crop mulomb_definition.'),
]
audit=[dict(C_span=s,decision=d,place=p,evidence=e) for s,d,p,e in audit]

# Every raw row is accounted for. Long tokenizer spans are split by the substantive
# change IDs below; no literal TikZ coordinate is mistaken for source text.
rowmap={
287:('page-marker macro difference only; source numeral 6 checked',[]),
288:('macro-only: C thin space tokenized as comma',[]),
289:('macro-only: source colon retained; spacing around quantified formula differs',[]),
290:('retained ambient-alphabet doubt; no source alternative bar', [1]),
291:('retained Phi/varphi doubt; same primary as H; no source alternative bar',[]),
292:('retained family-alphabet doubt',[2]),
293:('mixed moved margin text, source features, and cancelled-line endpoint',[3,4,5,6,7,8,9,14,15]),
294:('macro-only thin space after At_M',[]),
295:('real cancelled word/formula differences',[9,10,12,13]),
296:('real abbreviated arrow label, interlinear placement and omitted word',[11,14,15,16]),
297:('retained cancelled minimal/minimum doubt; no primary-word change',[]),
298:('cancelled phrase partly readable and inserted élément omitted by H',[17,18]),
299:('C live-word doubt resolved to its primary minimal',[19]),
300:('live inserted posons phrase incorrectly included in H cancellation',[21,22]),
301:('live insertion, parentheses, complete wording and source placement',[21,22]),
302:('relation-rendering and aligned syntax only; b formula fully read',[]),
303:('H editorial note excluded from source transcription',[]),
304:('real omitted underlying numeral/source-state mark',[23]),
305:('relation-rendering and syntax only; full At_M 6 formula checked',[]),
306:('real omitted underlying numeral/source-state mark',[24]),
307:('source drawing plus editorial explanation; not only macro syntax',[23,24,25]),
308:('source drawing and moved marginal content; H editorial prose excluded',[4,5,6,7,25]),
309:('tokenizer mismatch between TikZ coordinate and moved margin tuple; source tuple checked',[]),
310:('tokenizer mismatch between TikZ coordinate and moved margin tuple; signs checked',[]),
311:('source drawing syntax versus H editorial location note',[25]),
312:('source drawing and margin arrow represented; H prose excluded',[8,25]),
313:('real prose and source-state differences',[26]),
314:('C tilde-presence doubt resolved to its primary; alphabet covered at first occurrence',[27]),
315:('mainly relation syntax; H extra illegible placeholder before insertion excluded',[28]),
316:('macro-only thin space after At_M',[]),
317:('macro-only thin space after At_M',[]),
318:('real de/et word difference',[29]),
319:('retained doubtful cancelled numeral absent from H',[30]),
320:('cancelled tf qualifier recovered from H illegibility',[31]),
321:('cancelled group and live page-reference wording remain locally doubtful',[32,33]),
322:('real omitted superscript star within long relation-syntax span',[34]),
323:('relation-rendering macro differences only; first slanted-note clause fully read',[]),
324:('real arrow-shape doubt within long macro span',[35]),
325:('continued arrow syntax versus editorial note; no source-coordinate text',[35]),
326:('continued arrow/relation syntax and editorial prose; words checked',[35]),
327:('relation TikZ syntax only; final X′ and Y′ checked',[]),
328:('real prose differences around equivalent relation rendering',[36,37]),
329:('macro-only thin space after At_M; digits 4,5,6 checked',[]),
330:('aligned environment syntax only',[]),
331:('H added ambient-set parenthesis',[39]),
332:('cancelled words omitted and H closing parenthesis added',[39,40]),
333:('source colon omitted by H',[42]),
334:('relation-rendering syntax; source Phi insertion recorded separately',[38]),
335:('aligned environment syntax only',[]),
336:('H editorial description accompanies real missing source-state marks',[38,40,41]),
337:('real C word correction de to en',[43]),
338:('H adds abbreviation stop',[44]),
339:('same three-dot ellipsis: C ldots versus H Unicode; macro-only',[]),
340:('aligned environment syntax only',[]),
341:('real operator spelling difference',[45]),
342:('display-boundary syntax only; no source wording',[]),
343:('operator spelling and cancelled où source state',[46,47]),
344:('cancelled sign missing from H source text',[48]),
345:('H adds comma after defining set',[50]),
346:('aligned syntax; unreported case difference separately logged',[51]),
347:('H adds stop after cf',[52]),
348:('C initials doubt resolved to its primary GF',[53]),
349:('real reference-word differences and underline',[54,55]),
350:('H adds un',[56]),
351:('real faint adjective difference; C primary retained with doubt',[57]),
352:('H editorial note excluded; cancelled sign already represented in source state',[48]),
}
assert set(rowmap)==set(range(287,353))
difference_review=[dict(source_row=r,classification=rowmap[r][0],change_ids=[f'S007-{x:03}' for x in rowmap[r][1]]) for r in range(287,353)]
# Case differences and omitted source-state wrappers are not all exposed by the raw
# tokenizer rows, hence direct full-text collation supplements the row table.

second=[]
def b(label,kind,box,reading):
    second.append(dict(box=label,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
def bc(label,kind,crop,reading):
    b(label,kind,crops[crop]['box'],reading)

bc('007-B01','handwritten number','page_number','6')
bc('007-B02','whole doubtful formula and deletion','first_cancelled_axiom',r'cancelled At_M 4: ∀X∈M, Φ∈tilde F, posant Φ^X={Y∈Φ|X≪Y}, Φ^X a un plus petit élément')
bc('007-B03','whole doubtful formula, deletion, interlinear insertions, differing words, handwritten number','a_cancelled_start',r'At_M 4 a); cancelled Posant; ∀X,Y∈M,X≪; labelled equivalence; Y/X contient; est/ent minimal/minimum')
bc('007-B04','deletion and insertion; differing words','a_replacement','cancelled plus petit élément, live inserted élément minimal')
bc('007-B05','whole doubtful formula, insertion and deletion','a_definition_insertion',r'inserted dans; tilde Y^X={Z∈tilde Y|X≪Z}; live (posons X circle-≪ Y si c’est Y); deleted i.e. X≪Y′≤Y⇒Y′=Y')
bc('007-B06','margin note, overwritten number and arrow','margin_main',r'J’ai exprimé underlined At [deleted 6?]5 sans référence à F ou à tilde F, mais directement en termes de (M,≤,≪,relation); upper-right arrow')
bc('007-B07','whole formula and relation audit','b_formula',r'b) Alors X circle-≪ Y, X circle-≪ Y′, Y relation Y′⇒Y=Y′')
bc('007-B08','whole doubtful formula; overwritten handwritten numbers','at6_formula',r'At_M [deleted 5?]6 Si X relation Y, alors X≪Y⇒X≤Y')
bc('007-B09','whole doubtful formula; overwritten handwritten numbers','at5_formula',r'At_M [deleted 6?]5 X circle-≪ Y circle-≪ Z⇒X circle-≪ Z')
bc('007-B10','drawing','interchange_arrow','two curved transposition strokes, upper stroke ending with a head')
bc('007-B11','differing words, insertion, family doubt and handwritten numbers','dautrepart',r'on peut laisser tomber; tilde F; inserted au profit de relation,; At_M 1 à At_M 3 par (a) de la')
bc('007-B12','deletion; doubtful handwritten number','cancelled_tf_axiom',r'At_M [1|0](tf) Toute partie fermée majorée de M est de t.f.')
bc('007-B13','deletion; differing words; handwritten numbers; relation decoration','page5_condition',r'deleted At?; page/p. 5; condition b sur relation*; (page 5)')
bc('007-B14','margin note; whole doubtful formula','margin_condition',r'i.e. X relation Y et X′≤X,Y′≤Y [rounded two-shaft implication] X′ relation Y′')
bc('007-B15','differing words and handwritten numbers','general_case',r'quand on a simplement relation satisfaisant cette condition b) plus les conditions At_M 4,5,6')
bc('007-B16','whole formula, insertions, deletion and alleged parentheses','Ftf_definition',r'tilde F_tf=ensemble des parties fermées [inserted Φ de t.f.] de M,≤; [deleted formées t.q.] [inserted telles que:] X,Y∈Φ⇒X relation Y.')
bc('007-B17','deletion and insertion','formees_tq','deleted formées? t.q.?; live inserted telles que :')
bc('007-B18','differing word','enplus','un choix de structure en plus')
bc('007-B19','punctuation and abbreviation','ens_ellipsis',"l'ens ordonné tilde F_tf précédent...")
bc('007-B20','differing word; whole formula','Fstar',r'F*={Mulomb(F)|F∈family F}⊂Fig(M)')
bc('007-B21','whole doubtful formula, deletions and differing word/case','mulomb_definition',r'deleted où; Mulomb(F)={deleted X? Omb(x|X)|X∈tilde F}, with no final comma')
bc('007-B22','whole doubtful formula','omb_definition',r'Omb X={Y∈M|Y≪X}=M_{≪x|X}.')
bc('007-B23','differing words, underline and handwritten numbers','reference',r'(cf Scholie GF p.28, et axiomes, ou mieux à la underlined page 32), comme [no un]')
bc('007-B24','differing word','spacieux',r'sous-atelier (pas néc. spacieux|spécieux) de Fig(M).')
# Tight number proposals supplement the whole-context boxes. Coordinates remain
# original whole-image coordinates; no image or OCR inference generates readings.
b('007-N01','handwritten number',[481,68,616,125],'At_M 4 in cancelled opening axiom')
b('007-N02','handwritten number',[481,178,616,232],'At_M 4 before a)')
b('007-N03','handwritten overwritten number',[79,285,183,341],'underlined At, doubtful deleted 6, final 5')
b('007-N04','handwritten overwritten number',[482,386,640,454],'At_M, doubtful deleted 5, final 6')
b('007-N05','handwritten overwritten number',[494,465,646,541],'At_M, doubtful deleted 6, final 5')
b('007-N06','handwritten numbers',[898,708,1279,785],'At_M 1 à At_M 3')
b('007-N07','handwritten doubtful number',[514,781,721,863],'cancelled At_M [1|0](tf)')
b('007-N08','handwritten number',[615,856,835,928],'page/p. 5')
b('007-N09','handwritten number',[1466,900,1666,982],'(page 5)')
b('007-N10','handwritten numbers',[1100,1085,1392,1164],'At_M 4,5,6')
b('007-N11','handwritten number',[907,1934,1099,2017],'p. 28')
b('007-N12','handwritten number',[1027,2010,1177,2096],'32 in underlined page 32')

check_events=[
 {'event':'whole-image visual layout reading','source':'source/SP115_CW_156-7_scans/H156-01_156-7_scan007.jpg','count':1,'result':'Located page numeral, upper cancelled drafts, two margins, transposition strokes, live displays and final reference.'},
 {'event':'top-half line-by-line visual reading','source':'source/SP115_CW_156-7_scans/H156-01_156-7_scan007_a.jpg','count':1,'result':'Compared every line, including agreements, with C and H; queued crowded, differing and doubtful places.'},
 {'event':'bottom-half line-by-line visual reading','source':'source/SP115_CW_156-7_scans/H156-01_156-7_scan007_b.jpg','count':1,'result':'Compared complete lower prose, display indices, cancellations, reference and last line; bottom-half coordinates mapped with y offset 1100.'},
 {'event':'local crop visual readings','source':'scan007_crop_manifest.json','count':25,'result':'Viewed every named saved crop. Rotation used for the slanted marginal formula. A tool result truncated before displaying a batch was not treated as a completed visual reading.'},
 {'event':'unresolved crop framing correction','source':'margin_main and dautrepart','count':2,'result':'Extended right edges while those terminal strokes remained undecided; recorded old and new boxes in manifest.'},
 {'event':'targeted source-state review','source':'upper draft, live posons parenthesis and all C deleted/inserted spans','count':20,'result':'Audited all 14 C deleted spans and 6 C inserted spans individually in deletion_insertion_audit.'},
 {'event':'direct full-text collation','source':'packets/scan007/C.tex and H.tex','result':'Caught source-state and x/X differences not isolated as word differences in the raw TSV.'},
 {'event':'raw difference-row review','source':'packets/scan007/differences.tsv','count':66,'result':'Rows 287–352 all classified; macro coordinates and H editorial prose excluded from source text.'},
]

review=dict(
 scan='007',
 lines_read={
   'count':47,
   'convention':'Count independent physical text/formula baselines, including the page numeral and cancelled baselines; count separately written margin/interlinear inscriptions even if they share a y band with the main block. Do not count superscripts, overwritten digits, or purely graphical arrows as extra lines.',
   'breakdown':{
      'page numeral':1,
      'main text and formula baselines, including cancelled baseline lines':31,
      'independent upper cancelled interlinear band':1,
      'live interlinear élément minimal':1,
      'inserted dans':1,
      'posons parenthesis including short Y) continuation':2,
      'au profit de insertion':1,
      'Phi de t.f. insertion':1,
      'telles que replacement':1,
      'first margin note':5,
      'slanted margin note':2
   },
   'scope_note':'The crowded cancelled upper band is counted as one interlinear baseline with multiple separated fragments; its temporal drafting order remains uncertain.'
 },
 changes=changes,doubts=doubts,inventory=inventory,notation=notation,hand_log=hand_log,
 notes=notes,check_events=check_events,deletion_insertion_audit=audit,
 difference_review=difference_review,second_boxes=second
)
assert sum(review['lines_read']['breakdown'].values())==47
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in changes)
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in inventory)
assert all((ROOT/x['crop']).is_file() for x in changes)
assert len(audit)==C.count(r'\deleted{')+C.count(r'\inserted{')==20
assert len({x['id'] for x in changes})==len(changes)
assert all(0<=z['x0']<z['x1']<=1684 and 0<=z['y0']<z['y1']<=2361 for z in second)
(OUT/'scan007_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'scan':'007','changes':len(changes),'against_C':sum(x['against_C'] for x in changes),'against_H':sum(x['against_H'] for x in changes),'doubts':len(doubts),'inventory':len(inventory),'raw_rows':len(difference_review),'state_audits':len(audit),'second_boxes':len(second),'crops':len(crops)},ensure_ascii=False))

