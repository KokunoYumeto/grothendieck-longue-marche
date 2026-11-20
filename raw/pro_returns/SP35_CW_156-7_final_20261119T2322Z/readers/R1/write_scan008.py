from pathlib import Path
import json
from datetime import datetime, timezone

base=Path('/workspace/scratch/2b715fe259c4')
out=base/'SP35_CW_156-7/readers/R1'
src=base/'source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan008.tex'
tex=src.read_text()
crops=json.loads((out/'scan008_crops.json').read_text())
cm={Path(c['file']).stem.removeprefix('scan008_'):c for c in crops}

# Curved insertion guides are not lexical underlining.
air=r'''\tikz[baseline=(air.base)]{\node[inner sep=1pt] (air) {\inserted{avoir l'air de}};\draw ([xshift=-.2em,yshift=-.7em]air.south west)..controls([xshift=-.25em,yshift=-.05em]air.south west)and([xshift=.3em,yshift=-.08em]air.south west)..([yshift=-.08em]air.south east)--([yshift=.22em]air.south east);}'''
prev=r'''\tikz[baseline=(pr.base)]{\node[inner sep=1pt] (pr) {\inserted{précédents}};\draw ([xshift=-.2em,yshift=-.55em]pr.south west)..controls([xshift=.4em,yshift=-.12em]pr.south west)and([xshift=-.2em,yshift=-.12em]pr.south east)..([xshift=.2em,yshift=.15em]pr.south east);}'''
tex=tex.replace(r'\inserted{avoir l\'air de}',air) if False else tex.replace("\\inserted{avoir l'air de}",air,1)
tex=tex.replace(r'\unsure{\mathrm{defn}|\mathrm{défn}}',r'\mathrm{defn}',1)
tex=tex.replace(r'\varnothing_{\unsure{\mathscr F|\mathcal F|F}}',r'\varnothing_F',1)
tex=tex.replace(r'Il \deleted{\unsure{résultera}}\unsure{résulte|résultera}',r'Il résult\deleted{\unsure{era}}\inserted{\unsure{e|era}}',1)
tex=tex.replace(r'\inserted{précédents}',prev,1)
tex=tex.replace(r'$Z\ll X,Z\ll Y$,',r'$Z\ll X,Z\ll Y$\unsure{)|,}',1)
tex=tex.replace(r'\deleted{\unsure{i.e.} c\'est un $\unsure{\exists}$}',r'',0) if False else tex
tex=tex.replace("\\deleted{\\unsure{i.e.} c'est un $\\unsure{\\exists}$}","\\deleted{i.e\\unsure{.} c'est un $\\exists$}",1)
tex=tex.replace(r'\deleted{\unsure{la}}',r'\deleted{\unsure{la|le}}',1)
margin="Un atelier sera dit \\uline{spacieux} s'il satisfait cette condition. Contre-ex. : les ateliers simpliciaux\\ldots"
tex=tex.replace('\\margin{'+margin+'}',r'\margin{\unsure{\deleted{'+margin+'}|'+margin+'}}',1)
tex=tex.replace(r'\unsure{Soient}',r'Soient',1)
tex=tex.replace(r'\inserted{\unsure{soit}}',r'\inserted{soit}',1)
mark=r'''\unsure{\tikz[baseline=-.25ex,x=.5em,y=.35em]{\draw (.13,.55)--(0,.2)--(1.35,.2)..controls(1.5,.22)and(1.29,.52)..(.98,.4)--(0,.2);}|\deleted{et}}'''
tex=tex.replace(r'\deleted{\unsure{et}}',mark,1)
tex=tex.replace(r'\deleted{\unsure{\forall}}',r'\deleted{\forall}',1)
tex=tex.replace(r'\deleted{\unsure{\widetilde X|X}}\unsure{\widetilde F|F}',r'\deleted{\unsure{\widetilde X|X}}F',1)
tex=tex.replace(r'\deleted{\unsure{\varphi|y}}\unsure{Y|y}',r'\deleted{\unsure{\varphi|y}}Y',1)
tex=tex.replace(r'\draw (s.center) ellipse [x radius=1.05em,y radius=.72em];',r'\draw (.55em,.62em)..controls(-.1em,.9em)and(-1.05em,.55em)..(-1.06em,-.08em)..controls(-1.07em,-.7em)and(.55em,-.92em)..(.99em,-.25em)..controls(1.2em,.17em)and(.94em,.46em)..(.75em,.5em);',1)

# Keep the cancellation macros for state, and reproduce the three long strokes
# as an overlay on the entire cancelled At DC / Cor block.
start=tex.index(r'\deleted{\uline{At DC}')
body=tex[start:].strip()
overlay=r'''% Three global biffure strokes. Their source endpoints are recorded in JSON.
\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt,text width=.94\linewidth,font=\small] (dc) at (0,0) {%
@BODY@
};
\draw ($(dc.north west)!.03!(dc.north east)+(0,1.4em)$)--($(dc.south west)!.31!(dc.south east)+(0,1.0em)$);
\draw ($(dc.north west)!.36!(dc.north east)$)--($(dc.south west)!.67!(dc.south east)$);
\draw ($(dc.north west)!.73!(dc.north east)$)..controls($(dc.center)!.8!(dc.east)$)and($(dc.south west)!.92!(dc.south east)+(0,4em)$)..($(dc.south west)!.98!(dc.south east)+(0,3em)$);
\end{tikzpicture}}
'''.replace('@BODY@',body)
tex=tex[:start]+overlay
tex='% R1 independent scan008 reading; local overwritten layers remain explicit.\n\\usetikzlibrary{calc}\n'+tex
(out/'scan008.tex').write_text(tex)

rows=[]; audit=[]
def D(place,C,H,reading,dc,dh,kind,evidence,crop=None,confidence='high',marked=False,status='not applicable',math=None):
 c=cm.get(crop)
 row={'id':f'R1-008-{len(rows)+1:03d}','place':place,'C':C,'H':H,'reading':reading,'diff_C':dc,'diff_H':dh,
      'kind':kind,'marked_in_H':marked,'confidence':confidence,'evidence':evidence,
      'crop':c['file'] if c else None,'crop_coordinates':c['box'] if c else None,
      'crop_rotation_degrees':c['rotation_degrees'] if c else None,'C_doubt_status':status,'math_consequence':math}
 rows.append(row);return row
def A(n,place,C,H,reading,decision,evidence,crop,confidence='medium',marked=False,kind='misread word',dh=True,math=None):
 r=D(place,C,H,reading,decision in ('resolved','changed'),dh,kind,evidence,crop,confidence,marked,
     'resolved' if decision=='resolved' else 'retained',math)
 audit.append({'number':n,'place':place,'C':C,'reading':reading,'status':decision,'confidence':confidence,
               'evidence':evidence,'crop':r['crop'],'crop_coordinates':r['crop_coordinates'],'difference_id':r['id']})

D('Opening insertion and anchor','avoir l’air de, inserted between pas and les','moins élégants, inserted after disjonction-compatibilité','avoir l’air de, inserted between pas and les',False,True,'insertion or placement',
  'The upper half shows avoir, l’air and de on the raised line; its curved guide hooks down immediately before les. There is no moins élégants there.',marked=True)
D('Opening curved insertion guide','insertion macro only','different insertion position','curved guide under avoir l’air de, with left hook to the insertion gap',True,True,'drawing or diagram',
  'The long line beneath the inserted phrase bends down at the left before les and ends with a short upturn at the right. It is not an underline of the sentence.')
D('Quoted facultatifs and later disjoints','double tick quotation marks','guillemets','double tick quotation marks',False,True,'other',
  'The upper half shows pairs of short raised strokes rather than chevrons at both quoted expressions.')
A(1,'Opening, before implications',r"\unsure{des'|des|d'}","d'",r"\unsure{des'|des|d'}",'retained',
  'A clear d loop and ascender lead into a prolonged low connected stroke with a final small turn; a separate raised apostrophe follows. Whether the low trail supplies e/s cannot be securely decided.','opening_des','low')
D('Quoted definition phrase','F et G disjoints','F et G disjointes','F et G disjoints',False,True,'misread word',
  'The upper half shows the t-s ending immediately before the closing quote strokes; no extra e separates t and s.')
D('Underline on disjoints',r'\uline{disjoints}','emphasis only',r'\uline{disjoints}',False,True,'other',
  'A separate horizontal stroke lies beneath the whole adjective.')
A(2,'Definition label over equivalence',r'\unsure{defn|défn}','déf','defn','resolved',
  'The crop has d, a low e, tall f and a connected terminal n. No independent acute stroke appears above e.','definition_label','high')
A(3,'Empty symbol subscript',r'\unsure{\mathscr F|\mathcal F|F}',r'\mathfrak F','F','resolved',
  'The small lowered letter has a straight stem and two simple horizontal arms, without the looped/hooked top of the larger family letter. The literal small glyph is plain F.','empty_subscript','high',kind='misread symbol or index',
  math='Literal alphabet only. No inference about which mathematical object the author intended is substituted for the written subscript.')
D('Transition after first definition','On a d’ailleurs','On a d’autre part','On a d’ailleurs',False,True,'misread word',
  'The upper half shows the apostrophe after d and the connected ailleurs word; there is no separate part.')
D('Transition after universal disjointness display','donc interprétation','d’où interprétation','donc interprétation',False,True,'misread word',
  'The word starts with d and has a connected o-n-c trail; there is no isolated apostrophe or grave accent.')
A(4,'Transition, en terme(s)',r'\unsure{termes|terme}','termes',r'\unsure{termes|terme}','retained',
  'The tall t and low connected following letters survive clearly; the last horizontal return does not securely distinguish a final s from the finishing stroke of e.','termes_M','medium')
A(5,'Transition, M alphabet',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}','retained',
  'Two upright/pointed stems join through a bowed middle. The letter M is clear but its plain/calligraphic alphabet remains provisional, as on prior pages.','termes_M','medium',kind='misread symbol or index')
D('Lower-set definition, emphasis on pas',r'\uline{pas}','pas',r'\uline{pas}',False,True,'other',
  'The lower half shows a short separate line under pas only; it does not underline n’est or minoré.')
D('Lower-set definition, punctuation after M,≤','M,≤ followed by next line i.e.','M,≤, i.e.','M,≤ followed by next line i.e.',False,True,'text not on the page',
  'The written ≤ ends its line; there is no added comma after it before the lower i.e. line.')
D('NB heading underline',r'\uline{NB}','NB',r'\uline{NB}',False,True,'other',
  'A short line under NB is separate from the opening parenthesis and from the following Il.')
A(6,'NB first verb, earlier layer',r'\deleted{\unsure{résultera}}','résultera (single word)',r'résult\deleted{\unsure{era}}','changed',
  'The prefix résult- is shared and readable. Overwriting is confined to the terminal group just after the t; the t crossbar is also touched. Small upper loops could belong to era, but no independently cancelled full second word exists. The old ending cannot be recovered confidently.','NB_verb','low',kind='deletion state (struck given live or live given struck)')
A(7,'NB first verb, later ending',r'\unsure{résulte|résultera}','résultera',r'résult\inserted{\unsure{e|era}}','retained',
  'The strongest low terminal return favors e, hence résulte, but heavy loops above it leave the longer ending possible. The reading is kept local to the overwritten ending rather than duplicating the clear prefix.','NB_verb','medium')
D('NB précédents, insertion guide','inserted précédents','added précédents','inserted précédents with a curved guide, not an underline',True,True,'drawing or diagram',
  'The stroke begins low at the insertion gap before que, rises under the added word and curls up at the right. It is a placement guide; the word is not given lexical underlining.','NB_insertion')
D('NB, ça implique',r'ça implique',r'\ill{} \uncertain{indique}','ça implique',False,True,'misread word',
  'The lower half shows ça and the long descending p of implique. A word beginning ind- would not account for that descender.',marked=True)
D('NB, mark immediately after Z≪Y',',','comma or no explicitly identified extra mark',r'\unsure{)|,}',True,True,'other',
  'A lower curved return is visible immediately after Y, while an upper curved edge enters the black right boundary. Together they favor a closing-parenthesis-like mark, but clipping prevents exclusion of a comma. The mark is not safely absent.','NB_formula_end','low',
  math='This may be an unmatched closing parenthesis in the draft. No punctuation is silently repaired to make the outer NB parenthesis regular.')
A(8,'NB cancelled restatement, i.e.',r'\unsure{i.e.}','i.e.',r'i.e\unsure{.}','changed',
  'The i stem and dot, separating point, and e are readable under the strike. A separate final point after e cannot be isolated from the crossing line; only that point remains doubtful.','NB_deleted','medium')
D('NB cancelled restatement, c’est un','c’est un',r'\ill{}','c’est un',False,True,r'readable ink left as `\ill{}`',
  'The short c, apostrophe, following connected est and the separated low un sequence remain readable beneath the horizontal rule.','NB_deleted',marked=True)
A(9,'NB cancelled restatement, existential sign',r'\unsure{\exists}',r'\ill{}',r'\exists','resolved',
  'The right-end sign has a turned-E outline with upright right side and leftward horizontal strokes. No separate oblique negation slash survives; the long horizontal crossing is the line’s cancellation.','NB_deleted','medium',True,'misread symbol or index')
A(10,'NB, deleted article before réciproque',r'\unsure{la}','la (live)',r'\deleted{\unsure{la|le}}','changed',
  'A tall looped l precedes a heavily blackened short final letter. The final vowel is not separable as a versus e. A local dark strike crosses this group before the clear réciproque.','NB_deleted','low',kind='deletion state (struck given live or live given struck)')
D('NB, second verb','résultera',r'\uncertain{résultera}','résultera',False,True,'misread word',
  'The second occurrence is not overwritten: the r/é, long l/t strokes and terminal ra can be followed across the line.','NB_ending','high',True)
A(11,'NB, d’axiome(s)',r"\unsure{d'axiome|d'axiomes}","d'axiome",r"\unsure{d'axiome|d'axiomes}",'retained',
  'The d, raised apostrophe and axiome sequence run to the black edge. The final e trail reaches the boundary, so a terminal s cannot be excluded.','NB_ending','low')
D('Slanted margin, full wording','Un atelier sera dit spacieux s’il satisfait cette condition. Contre-ex. : les ateliers simpliciaux…',r'Un atelier sera dit spécieux s’il satisfait \uncertain{cette} condition \ill{} \uncertain{contre-ex.} : les lieux \ill{} \ill{}…','Un atelier sera dit spacieux s’il satisfait cette condition. Contre-ex. : les ateliers simpliciaux…',False,True,r'readable ink left as `\ill{}`',
  'In the single rotated crop, atelier, sera dit, s’il satisfait, cette condition, Contre-ex., les ateliers and the split-but-continuous simpliciaux sequence are readable. The adjective has a low a-shaped vowel and no acute accent.','margin','high',True)
D('Slanted margin, underline',r'\uline{spacieux}','emphasis only',r'\uline{spacieux}',False,True,'other',
  'One long line runs directly under spacieux and stops before s’il.','margin')
D('Slanted margin, scope of global cancellation','margin given live','margin given live; note says crossed by a biffure',r'\unsure{deleted marginal note|live marginal note}','true'=='true',True,'deletion state (struck given live or live given struck)',
  'The first long diagonal cancellation continues through sera/s’il and onward into the At DC block. It clearly intersects the note, but whether the entire marginal paragraph is cancelled with the draft is not independently settled. Both state alternatives are retained in TeX.','margin','low',True)
D('Whole lower At DC / Cor block, global state','cancelled','body typeset live; note acknowledges three long biffures','cancelled, with three long strokes reproduced',False,True,'deletion state (struck given live or live given struck)',
  'The lower half shows three long diagonal strokes running through the At DC heading, hypotheses, bracketed NB and corollary. The complete crossed block remains transcribed.',marked=True)
D('Whole lower block, biffure geometry','state macros only','three strokes described in note','three diagonal strokes drawn across the block',True,True,'drawing or diagram',
  'The left stroke begins in the slanted margin and reaches the corollary; the middle reaches the final quantifier line; the right curves out to the lower right before the final corollary formula.',marked=True)
D('At DC heading underline',r'\uline{At DC} 1','emphasis on At DC 1',r'\uline{At DC} 1',False,True,'other',
  'The underline ends after DC, before the separate 1.')
D('Parenthetical axiom title','Axiome des ateliers spacieux','Axiome des ateliers spécieux','Axiome des ateliers spacieux',False,True,'misread word',
  'The lower half shows spacieux with no acute accent on its first vowel. A continuous underline covers the title words inside the parentheses.')
D('Parenthetical title underline','underlined title','emphasis only','underlined title',False,True,'other',
  'The line beneath Axiome des ateliers spacieux is separate from the three diagonal cancellation strokes.')
A(12,'At DC, initial Soient',r'\unsure{Soient}','Soient','Soient','resolved',
  'The large S, following low o, dotted i, e/n sequence and tall terminal t are all visible; the diagonal global stroke passes between the early letters without erasing the word.','Soient','high',dh=False)
A(13,'At DC, inserted soit',r'\unsure{soit}','omitted','soit','resolved',
  'A small s, rounded o, dotted i and tall crossed t are visible left of and slightly below the K line. The word is displaced as an insertion.','soit_et','high',kind='insertion or placement')
A(14,'At DC, local mark immediately before K',r'\deleted{\unsure{et}}','omitted','low left-pointing guide-like mark | deleted et','changed',
  'The crop shows a very low elongated shaft/loop with a short rising stroke at its left endpoint and a thick return at the right. It does not expose separable e and t. A left-pointing insertion guide toward the displaced soit is plausible; a locally cancelled word remains possible. The observed shape is drawn as the first alternative.','soit_et','low',kind='drawing or diagram')
D('At DC, K insertion status','K on main line',r'\add{K}','K on main line',False,True,'insertion or placement',
  'K begins the same main baseline as =X∩Y=Sup Z. The displaced inserted word is soit at the left, not K.','soit_et')
A(15,'At DC, local crossed fragment before Supposons',r'\unsure{Il}','omitted',r'\unsure{Il}','retained',
  'A tiny tall loop with overlapping upright strokes and a dark lower crossing follows the point after Sup Z. Il remains plausible, but the two proposed letters cannot be cleanly isolated.','Il','low',kind='omission')
D('At DC, pour insertion','inserted pour X′,Y′∈M','pour plus added tous X′,Y′∈M','inserted pour X′,Y′∈M',False,True,'insertion or placement',
  'Pour is followed directly by X′, comma, Y′ and ∈M on the added lower line. No tous lies in the gap. The crop also confirms one separate prime on each letter.','pour')
A(16,'At DC, locally cancelled quantifier',r'\unsure{\forall}','unnamed struck sign',r'\forall','resolved',
  'Despite the diagonal overwriting, two upper arms converge at a low point and a crossbar survives, identifying the inverted-A quantifier. The short faint trailing stroke is part of the crossing, not a new variable.','forall','medium',True,'misread symbol or index')
D('At DC, bracketed NB','NB et alors seulement…',r'NB il \ill{} dans tous les cas…','NB et alors seulement…',False,True,'misread word',
  'The crop gives et, then the looped alors and long seulement. The three terminal points precede the closing square bracket.','NB_bracket','high',True)
D('At DC, cf Cor placement and punctuation','inserted cf Cor',r'cf. Cor; note says below bracket','inserted cf Cor below the bracketed phrase',False,True,'insertion or placement',
  'The small cf Cor sits below the middle of the bracketed phrase, with no point after f. It is attached to that NB, not to the following compatibility conclusion.','NB_bracket','high',True)
D('Cor heading underline',r'\uline{Cor}','emphasis only',r'\uline{Cor}',False,True,'other',
  'A short separate stroke lies directly below Cor.')
A(17,'Cor Sup index, first older letter',r'\deleted{\unsure{\widetilde X|X}}','not represented',r'\deleted{\unsure{\widetilde X|X}}','retained',
  'Crossing diagonal strokes remain beneath the live F. They support an old X; any old tilde is inseparable from the descending Sup stroke immediately above.','Cor_sup','low',kind='omission')
A(18,'Cor Sup index, first live letter',r'\unsure{\widetilde F|F}',r'\widetilde F','F','resolved',
  'The live F has a stem and two right arms. The apparent wave above it is visibly continuous with the long p-descender of Sup; no independent tilde is present over this F.','Cor_sup','medium',kind='misread symbol or index',
  math='The literal index is Z∈F∩tilde G. The missing independent tilde is not supplied from the analogous earlier formula or expected set notation.')
A(19,'Cor Sup index, second older letter',r'\deleted{\unsure{\widetilde Y|Y}}','not represented',r'\deleted{\unsure{\widetilde Y|Y}}','retained',
  'A fork and lower stroke survive inside the live G loop. The independent wave over the live G cannot be confidently assigned to the older layer as well.','Cor_sup','low',kind='omission')
D('Cor, letters inside oval','ses',r'ssi (uncertain)','ses',False,True,'misread word',
  'The middle letter is a closed e-loop, between two s forms. There is no separate i stem and dot.','ses','high',True)
D('Cor, oval shape','closed ellipse','parentheses in text; oval described','oval with small upper-right gap',True,True,'drawing or diagram',
  'The curve stops above the right side of the word and resumes slightly lower/right, leaving a visible small gap. The lower and left sides form a continuous loop.','ses','high',True)
A(20,'Cor quantified pair, older second letter',r'\deleted{\unsure{\varphi|y}}','not represented',r'\deleted{\unsure{\varphi|y}}','retained',
  'A closed low loop and crossing/descending stem remain beneath the newer fork. They permit the phi-like old form or a looped y, without securely choosing one.','Cor_letters','low',kind='omission')
A(21,'Cor quantified pair, live second letter',r'\unsure{Y|y}','Y','Y','resolved',
  'The two upper branches start at approximately the height of the capital M nearby and join into a long lower stem. The capital Y form is clearer than a small y.','Cor_letters','medium',kind='misread symbol or index',dh=False)
D('Final corollary formula, terminal punctuation','no final point','final point','no final point',False,True,'text not on the page',
  'The lower half shows the final Y followed by clear blank paper; no terminal point is present.')

end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
counts={'difference_rows':len(rows),'diff_C':sum(bool(r['diff_C']) for r in rows),'diff_H':sum(bool(r['diff_H']) for r in rows),
        'C_doubts':len(audit),'C_doubts_resolved':sum(a['status']=='resolved' for a in audit),
        'C_doubts_retained':sum(a['status']=='retained' for a in audit),'C_doubts_changed':sum(a['status']=='changed' for a in audit),
        'targeted_crops':len(crops)}
unresolved=[{k:a[k] for k in ['place','reading','confidence','evidence','crop']} for a in audit if a['status']!='resolved']
unresolved += [{k:r[k] for k in ['place','reading','confidence','evidence','crop']} for r in rows if r['place'] in ['NB, mark immediately after Z≪Y','Slanted margin, scope of global cancellation']]
report={
 'reader':'R1','scan':'008','H_page':7,'model':'GPT-6 Astra Pro, inherited configuration; effort setting not exposed',
 'start_utc':(out/'scan008_start.txt').read_text().strip(),'end_utc':end,
 'independence':'No other reader or main report, no later manuscript image, and no S row was opened for this page. Current C/H text and C metadata were compared with the current images.',
 'images_viewed':[{'file':f'source/SP35_CW_156-7_scans/H156-01_156-7_scan008{s}.jpg','role':role,'views':1} for s,role in [('', 'whole page'),('_a','supplied upper half'),('_b','supplied lower half')]]+[dict(c,role='targeted unresolved-locus crop',views=1) for c in crops],
 'coverage':[
  'Handwritten page number 7; complete opening paragraph, all quotation strokes, inserted avoir l’air de and its guide, des/des′/d′ ending, final period.',
  'Complete Une notion essentielle paragraph, exact disjoints spelling and underline, definition equivalence label, compatibility, intersection, empty sign and lowered F.',
  'Notion qui ne dépend que de ≤, On a d’ailleurs; universal disjointness formula with X∈tilde F, Y∈tilde G, both parallel signs, equivalence and comma.',
  'Donc interprétation en terme(s) de X∥Y dans M, qui y signifie; all letters and comma.',
  'Full intrinsic-M display, M under both relation signs, {X,Y}, underlined pas, minoré dans M,≤, i.e. ∄Z avec Z≤X,Z≤Y.',
  'Complete NB: underlined heading, shared first-verb prefix and local old/new endings, preceding-axiom insertion and guide, ça implique, two refinement inequalities, clipped mark after final Y, cancelled restatement and existential, local cancelled article, reverse-direction sentence and ending.',
  'Complete slanted spacieux note, underlining, condition sentence, Contre-ex., les ateliers simpliciaux and ellipsis; crossing stroke and uncertain scope of cancellation.',
  'All three broad diagonal cancellation strokes and their extent across the lower At DC/Cor draft.',
  'At DC 1 heading and underline; full underlined parenthetical title; Soient X,Y∈M; inserted soit; local guide-like/cancelled-word mark before K.',
  'K=X∩Y=Sup Z with Z∈tilde X∩tilde Y; terminal point and local crossed Il fragment; Supposons que and inserted pour X′,Y′∈M.',
  'Hypothesis formula, local cancelled ∀, all four hypotheses, commas, each prime, both K letters, double angles, parallel signs, implication, final X′∥Y′ and point.',
  'Alors [NB et alors seulement… cf Cor] X COMPAT Y; exact cf punctuation and lowered insertion position.',
  'Cor underline, Soient F,G∈script F, K=F∩G=Sup Z; first old X/live F layer and absent independent live tilde, second old Y/live tilde G layer, point.',
  'Alors F COMPAT G; literal ses in an oval open at upper right; ∀X, old phi/y and new Y, membership M.',
  'Full final corollary implication, all X/Y/F/G/K letters, double angles and parallel signs, commas, arrow, final X∥Y without point.'
 ],
 'notation':[
  {'sign':'Disjointness','reading':r'\parallel, with M below when written','evidence':'Two separate near-vertical strokes; the intrinsic relation has the small M directly below.'},
  {'sign':'Compatibility','reading':'opposed overlapping chevrons, with M below when written','evidence':'Same recurring manuscript sign; equivalent macro names alone are not counted as differences.'},
  {'sign':'Definition label','reading':'defn','evidence':'Terminal n visible, no independent acute over e.'},
  {'sign':'Empty-set index','reading':'plain lowered F on this page','evidence':'Straight stem with two short simple arms.'},
  {'sign':'Cor first Sup index','reading':'live F, old X/tilde X doubtful','evidence':'The curve above the live F continues from Sup p; it is not an independent tilde.'},
  {'sign':'Circled abbreviation','reading':'ses in an open oval','evidence':'Middle closed e loop; small gap in oval at upper right.'},
  {'sign':'Local overwriting','reading':'shared résult-, old era?, new e|era','evidence':'Only final group is overwritten; no duplicated complete word in ink.'},
  {'sign':'Abbreviations','reading':'NB; defn; i.e.; Contre-ex.; At DC; Cor; cf; ses','evidence':'No expansion in transcription; cf has no point.'}
 ],
 'agreed_symbol_checks':[
  {'place':'Upper universal disjointness formula','reading':'F,G,X,Y with both tildes and all parallel signs','evidence':'Read directly in supplied upper half.'},
  {'place':'At DC intersection Sup index','reading':'Z∈tilde X∩tilde Y','evidence':'Both waves are separate above the corresponding letters in the lower half.'},
  {'place':'Inserted quantified pair','reading':'pour X′,Y′∈M','evidence':'One separate prime on each capital; no extra prime or tous.','crop':cm['pour']['file']},
  {'place':'Last K in At DC hypothesis','reading':'K, not a demonstrable overwritten different variable','evidence':'A stem and two arms are visible. The upgoing arm is retraced, but no separate old letter can be securely isolated.','crop':cm['lastK']['file']},
  {'place':'Cor second Sup index, live layer','reading':'tilde G','evidence':'A separate wave is visibly detached above the G, unlike the first live F.','crop':cm['Cor_sup']['file']}
 ],
 'math_notes':[
  {'claim':'The page proposes putting the disjunction/compatibility axioms before the axioms on lieux, calling them facultatifs for an atelier and anticipating mutual implications.','status':'Read and transcribed, not independently proved.'},
  {'claim':'It defines F∥G by compatibility and empty intersection, then states a reduction to all strata and an intrinsic-M criterion using compatibility and absence of a common lower bound.','status':'All symbols checked against ink; no independent proof of the equivalences performed in this reading.'},
  {'claim':'The NB attributes one implication about common refinement predecessors to preceding axioms and defers the converse to an axiom below.','status':'Author’s dependency claim recorded literally; no proof check claimed.'},
  {'claim':'The crossed lower draft gives a spacieux axiom and corollary; the margin names simplicial ateliers as a counterexample.','status':'Cancelled draft and marginal scope retained; the proposed axiom/corollary and counterexample are not independently proved here.'},
  {'claim':'The first live F under Cor Sup has no independent tilde, although the earlier analogous formula has tildes.','status':'The mismatch prompted a targeted ink inspection. It is a textual/alphabet decision, not a mathematical correction or proof event.'}
 ],
 'check_events':[],
 'check_events_note':'No independent mathematical proof, computation or formal check was performed on scan008. Reading and comparing these assertions is not entered as a proof check.',
 'author_qualifications':[
  {'words':'``facultatifs\'\'','state':'live opening prose'},
  {'words':'des axiomes précédents','state':'live, précédents inserted'},
  {'words':"et [deleted la|le] réciproque résultera d’axiome|d’axiomes ci-dessous…",'state':'live NB with local cancellation'},
  {'words':'NB et alors seulement… cf Cor','state':'within globally cancelled lower draft'},
  {'words':'Contre-ex. : les ateliers simpliciaux…','state':'slanted note crossed by one global biffure; full-note state uncertain'}
 ],
 'source_metadata_warning':'The C audit section headed Scan 8 contains a long NB margin not present in the current manuscript image. It was not imported. The actual scan008 marginal note is the spacieux/ateliers simpliciaux paragraph.',
 'global_biffure_geometry':{'source':'source/SP35_CW_156-7_scans/H156-01_156-7_scan008.jpg','approximate_paths':[[[263,1494],[450,1885],[678,2179]],[[728,1647],[920,1905],[1150,2221]],[[1204,1645],[1410,1900],[1584,2083]]],'note':'Approximate endpoints from the single whole/half views; these are cancellation paths, not logical arrows. The TeX overlays three correspondingly slanted strokes on the cancelled main block.'},
 'differences':rows,'C_doubt_audit':sorted(audit,key=lambda x:x['number']),'unresolved':unresolved,
 'missing_from_both':[
  {'place':'NB right-edge punctuation after Z≪Y','reading':'parenthesis-like return | comma','confidence':'low','crop':cm['NB_formula_end']['file']},
  {'place':'Insertion guides','reading':'curved leaders beneath avoir l’air de and précédents','confidence':'high','crop':cm['NB_insertion']['file']},
  {'place':'Cor oval','reading':'upper-right gap','confidence':'high','crop':cm['ses']['file']}
 ],
 'S_audit':'No S row applies directly to scan008; none was opened in this page task.',
 'counts':counts
}
assert len(audit)==21
assert sorted(a['number'] for a in audit)==list(range(1,22))
(out/'scan008.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
md=f'''# R1 independent reading — scan 008 (H page 7)

Completed {end}. {counts['difference_rows']} difference/audit rows; {counts['diff_C']} differ from C and {counts['diff_H']} from H. All 21 C doubts audited: {counts['C_doubts_resolved']} resolved, {counts['C_doubts_retained']} retained, {counts['C_doubts_changed']} changed. The whole and both supplied halves were read once, followed by 20 once-only targeted crops.

## Main decisions

- The opening insertion is **avoir l’air de**, attached between **pas** and **les**, with a curved guide. H’s **moins élégants** is not the written insertion.
- Read **disjoints**, **defn** without an acute, **On a d’ailleurs**, and **donc interprétation**. The empty-symbol subscript is a plain **F**.
- The first NB verb has a shared **résult-** prefix. Only the ending is overwritten: old **era?**, new **e|era**, favoring **résulte**. C’s full deleted word followed by a second complete word duplicates unaffected ink. The t crossbar is touched by the overwriting, but the shared stem/prefix remains visible.
- The stroke beneath **précédents** is an insertion guide from the gap before **que**, not a lexical underline.
- Immediately after **Z≪Y** at the clipped right edge, a return favors a closing-parenthesis-like mark, with comma retained as an alternative. It is not safely absent. The resulting possible extra parenthesis is not regularized.
- The cancelled NB restatement has readable **i.e** with its final point doubtful, **c’est un**, and **∃**. The deleted article before **réciproque** is **la|le**. **d’axiome|d’axiomes** remains clipped and uncertain.
- The slanted note reads **Un atelier sera dit spacieux s’il satisfait cette condition. Contre-ex. : les ateliers simpliciaux…**. **Spacieux** is underlined. One of the broad cancellation strokes crosses the note; whether the entire note is cancelled remains explicit as a state doubt.
- **Soient**, inserted **soit**, and the locally cancelled **∀** are resolved. Before **K**, the low elongated mark is not securely the deleted word **et**: a left-pointing insertion guide is also plausible. Its actual outline is drawn as the preferred graphical alternative, with **deleted et** retained.
- The added phrase is **pour X′,Y′∈M**, without **tous**. The bracket reads **NB et alors seulement…**, with **cf Cor** added below and no point after **cf**.
- The first live **F** under the corollary’s **Sup** has no independently written tilde; the apparent wave belongs to the descending **p** above. The second **G** has a separate tilde. Old **X/tilde X** and **Y/tilde Y** layers remain doubtful.
- The oval contains **ses**, and its outline has a small upper-right gap. The live second quantified letter is **Y**; the old loop below it remains **varphi|y**. There is no point after the final corollary formula.

## Mathematics and limits

The page’s assertions, dependencies, cancelled spacieux axiom/corollary, and simplicial counterexample are recorded as authorial claims. No independent proof or computation was performed here, so no mathematical check event is claimed. The missing independent tilde in the first corollary index is an ink decision and is not repaired from the analogous earlier formula.

The C audit section labelled Scan 8 describes a different NB margin absent from this image; that text was not imported. No S row applies directly here. No scan009, other-reader report, or main decision was opened. Awaiting the next gate.
'''
(out/'scan008.md').write_text(md)
print(json.dumps(counts))
print('Saved scan008.tex/json/md and crop metadata.')
