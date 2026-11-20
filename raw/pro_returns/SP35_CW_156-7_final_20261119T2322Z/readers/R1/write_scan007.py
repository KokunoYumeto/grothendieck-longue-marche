from pathlib import Path
import json
from datetime import datetime, timezone

root = Path('/workspace/scratch/2b715fe259c4')
out = root/'SP35_CW_156-7/readers/R1'
source = root/'source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan007.tex'
Ctext = source.read_text()
crops = json.loads((out/'scan007_crops.json').read_text())
cropmap = {Path(c['file']).stem.removeprefix('scan007_'):c for c in crops}
COMP = r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
ROUND = r'\mathrel{\tikz[baseline=-.15ex,x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.42,.42) and (1.48,.15) .. (1.32,.12);}}'

tex = Ctext
tex = tex.replace(r'\unsure{\Phi|\varphi}',r'\Phi',1)
tex = tex.replace(r'\unsure{élément}.}',r'\unsure{élément}}',1)
tex = tex.replace(r'\unsure{Y}$ \unsure{contient}',r'\unsure{Y|X}$ \unsure{contient}',1)
tex = tex.replace(r'\inserted{élément \unsure{minimal|minimum|privilégié}}',r'\inserted{élément minimal}',1)
tex = tex.replace(r'\unsure{posons|posant}',r'posons',1)
tex = tex.replace(r'\mathrm{At}_{M}\,1$ à $\mathrm{At}_{M}\,3',r'\mathrm{At}_{M}\,1$ ; $\mathrm{At}_{M}\,3',1)
tex = tex.replace(r'\unsure{1|0}',r'1',1)
tex = tex.replace(r'\deleted{\unsure{At}} \unsure{page|p.} 5',r'\deleted{At} page 5',1)
oldround = r'\unsure{\mathrel{\tikz[x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.35,.42) and (1.38,.23) .. (1.28,.2);}}|\Longrightarrow}'
assert oldround in tex
tex = tex.replace(oldround,ROUND,1)

finite_start = tex.index(r'\[',tex.index('Dans le cas général'))
finite_end = tex.index(r'\]',finite_start)+2
finite = r'''% The added Phi de t.f. sits above the far-right de M,leq.
% The two curved strokes are reproduced as geometry, without assigning a
% parenthesis or an additional logical relation to either one.
\figure{\begin{tikzpicture}[x=1em,y=1em,baseline=(current bounding box.center),every node/.style={inner sep=0pt}]
  \node[anchor=west] at (0,0) {$\widetilde{\mathscr F}_{\mathrm{tf}}=$};
  \node[anchor=west] at (4.1,0) {ensemble des parties fermées};
  \node[anchor=west] at (25.9,1.5) {\inserted{$\Phi$ de t.f.}};
  \node[anchor=west] at (26.6,0) {de $M,\leq$};
  \draw (25.95,-.3)..controls(25.75,.55)and(27.8,.98)..(30.25,1.02)
        ..controls(31.9,1.08)and(33,1.08)..(33.05,1.7);
  \node[anchor=west] at (4.3,-2.1) {\deleted{\unsure{formées|fermées} t.q.}};
  \node[anchor=west] at (4.5,-1.05) {\inserted{telles que :}};
  \node[anchor=west] at (16.2,-1.65) {$X,Y\in\Phi$};
  \node[anchor=west] at (22.1,-1.65) {$\Longrightarrow$};
  \node[anchor=west] at (26,-1.65) {$X@COMP@Y.$};
  % Thin return below the long f-stroke of fermées, toward the implication.
  \draw[line width=.25pt] (20.9,-.45)..controls(20.72,-1.15)and(21.05,-1.65)..(22.2,-1.65);
\end{tikzpicture}}'''.replace('@COMP@',COMP)
tex = tex[:finite_start]+finite+tex[finite_end:]
tex = tex.replace('un choix de structure de plus','un choix de structure en plus',1)
tex = tex.replace(r'\deleted{\text{où}}\quad\mathrm{Mulomb}(F)',r'\text{\unsure{\deleted{où}|où}}\quad\mathrm{Mulomb}(\unsure{F|\mathscr F})',1)
tex = tex.replace(r'\deleted{\unsure{X}}',r'\deleted{\unsure{x|X}}',1)
tex = tex.replace(r'\unsure{GF|GE}',r'GF',1)
tex = tex.replace('néc. spacieux','néc. '+r'\unsure{spacieux|specieux}',1)
tex = ('% Independent reader R1, scan 007 only. Ink decisions, not mathematical emendations.\n'
       '% Cursive alphabet conventions remain provisional at the first occurrence.\n'+tex)
(out/'scan007.tex').write_text(tex)

rows=[]
audits=[]
def D(place,C,H,reading,dc,dh,kind,evidence,crop=None,conf='high',marked=False,status='not applicable',math=None):
    r={'id':f'R1-007-{len(rows)+1:03d}','place':place,'C':C,'H':H,'reading':reading,
       'diff_C':dc,'diff_H':dh,'kind':kind,'marked_in_H':marked,'confidence':conf,
       'evidence':evidence,'crop':cropmap[crop]['file'] if crop else None,
       'crop_coordinates':cropmap[crop]['box'] if crop else None,
       'crop_rotation_degrees':cropmap[crop]['rotation_degrees'] if crop else None,
       'C_doubt_status':status,'math_consequence':math}
    rows.append(r)
    return r
def A(n,place,C,H,reading,decision,evidence,crop,conf='medium',marked=False,kind='misread word',math=None):
    dc=decision in ('resolved','changed')
    r=D(place,C,H,reading,dc,True,kind,evidence,crop,conf,marked,
        'resolved' if decision=='resolved' else 'retained',math)
    audits.append({'number':n,'place':place,'C':C,'reading':reading,'status':decision,
                   'confidence':conf,'evidence':evidence,'crop':r['crop'],
                   'crop_coordinates':r['crop_coordinates'],'difference_id':r['id']})

A(1,'Cancelled opening, domain M',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}','retained',
  'Two tall strokes joined by a low rounded/pointed middle remain visible under the strike. They identify M but do not fix a plain-versus-calligraphic typeset alphabet.','fonts',kind='misread symbol or index')
A(2,'Cancelled opening, Phi',r'\unsure{\Phi|\varphi}',r'\Phi',r'\Phi','resolved',
  'A broad closed oval sits on a vertical stem with a distinct horizontal foot; the capital Phi form is visible above and below the cancelling stroke.','fonts','high',kind='misread symbol or index')
rows[-1]['diff_H']=False
A(3,'Cancelled opening, figure-family alphabet',r'\widetilde{\unsure{\mathscr F|\mathcal F}}',r'\widetilde{\mathfrak F}',r'\widetilde{\unsure{\mathscr F|\mathcal F}}','retained',
  'A tall cursive F with upper loop/arm and separate upper tilde is visible. The manuscript does not securely distinguish the proposed script font families. The later repeated F family uses the same provisional convention.','fonts',kind='misread symbol or index')
A(4,'Cancelled opening, final noun',r'\unsure{élément}','élément',r'\unsure{élément}','retained',
  'An accented initial and tall l survive; much of the latter half is absorbed in the horizontal cancellation and heavy terminal ink. The ending cannot be independently recovered letter by letter.','old_element','low')
D('Cancelled opening, ending punctuation','élément.','élément','élément (no separately visible final point)',True,False,'other',
  'The cancelling line continues to a blunt right endpoint after the overwritten word; the crop shows no distinct terminal point. No punctuation has been supplied from sentence grammar.','old_element','medium')
A(5,'Upper-left note, old digit under live At 5',r'At\deleted{\unsure{6}}5','At 5',r'At\deleted{\unsure{6}}5','retained',
  'The live 5 has a top bar and lower curve. An overwritten lower enclosure is compatible with 6, but the old and new ink cannot be cleanly separated.','upper_margin','low',kind='omission')
A(6,'Upper-left note, en terme(s)',r'\unsure{termes|terme}','termes',r'\unsure{termes|terme}','retained',
  'The t and following low connected letters are legible, but the final small trail is crowded at the far right of the marginal line; the single crop also ends near that trail. It does not settle singular/plural.','upper_margin','low')
D('Upper-left note, underline on At',r'\uline{At}','At',r'\uline{At}',False,True,'other',
  'One separate horizontal stroke lies directly under At, ending before the numeral.','upper_margin')
D('Upper-left note, sans référence à / ou à','sans référence à F ou à tilde F',r'\ill{} \ill{} F \ill{} tilde F','sans référence à F ou à tilde F',False,True,r'readable ink left as `\ill{}`',
  'The s-a-n-s sequence, long descending f of référence, following à, and short ou à between the two family letters are visible in the two marginal lines.','upper_margin',marked=True)
D('Upper-left note, northeast arrow','nearrow','described in note','drawn northeast arrow',False,True,'drawing or diagram',
  'A thin diagonal shaft runs from the note toward the upper right and ends in a visibly pointed two-stroke head.','upper_margin')
D('First cancelled attempt, opening verb','Posant','Posons','Posant',False,True,'misread word',
  'After P-o-s-a-n the terminal stroke rises to a tall t-like point; it is not the low ending of the live posons below.','a_trials','medium',marked=True)
A(7,'First cancelled attempt, equivalence/implication',r'\unsure{\Longleftrightarrow|\Longrightarrow}',r'\Longleftrightarrow',r'\unsure{\Longleftrightarrow|\Longrightarrow}','retained',
  'Two horizontal shafts and a right point survive. The short left mass is overstruck and does not securely establish a left head.','a_trials','low',True,'misread symbol or index')
A(8,'First cancelled attempt, letter after arrow',r'\unsure{Y}','X',r'\unsure{Y|X}','changed',
  'The heavy fork/cross immediately to the right of the arrow has two upper branches and a long lower stroke, favoring Y; a further diagonal through the cancellation prevents exclusion of X.','a_trials','low',True,'misread symbol or index')
A(9,'First cancelled attempt, final verb',r'\unsure{contient}',r'\ill{}','\\unsure{contient}','retained',
  'Several low connected arches and a taller middle/terminal stroke survive under the cancelling line, but the crossing erases the internal sequence. Contient remains only a proposed reading.','a_trials','low',True)
D('Two cancelled attempts, quantifier line and refinement sign',r'\forall X,Y\in M, X\ll (separate line)',r'Posons \forall X,Y\in M, X\overset{\circ}{\ll}Y (combined)',r'\forall X,Y\in M, X\ll (separate cancelled upper line)',False,True,'insertion or placement',
  'The quantifier and X,Y∈M occupy an upper cancelled baseline; Posant X≪Y occupies the lower baseline. The small mark above the lower chevrons lies with the upper-line punctuation and does not securely supply an independent hollow circle.','a_trials','medium',marked=True)
A(10,'Cancelled upper attempt, défini',r'\unsure{défini}',r'\mathrm{déf} above arrow',r'\unsure{défini}','retained',
  'The d/é/f region, including a long descending f stroke, is readable on the upper cancelled baseline; its short trailing connected strokes are covered. It is not securely a clean superscript déf over the lower arrow.','a_trials','low',True)
A(11,'Cancelled right interlinear words, first word',r'\unsure{est|ent}',r'\ill{}',r'\unsure{est|ent}','retained',
  'Only a small e-like loop followed by crossed low strokes survives before the adjective. The internal consonant cannot be separated from the cancelling line.','a_trials','low',True)
A(12,'Cancelled right interlinear adjective',r'\unsure{minimal|minimum}','minimal',r'\unsure{minimal|minimum}','retained',
  'The m-i-n-i-m portion and dots are visible, but the overstruck ending does not securely distinguish al from um.','a_trials','low',True)
D('Revised a, cancelled phrase','plus petit élément',r'\struck{\ill{}}',r'\deleted{plus petit élément}',False,True,r'readable ink left as `\ill{}`',
  'The long p descender, plus, separate petit with tall t strokes, and the following élément remain readable below the replacement.','a_replacement','high',True)
A(13,'Revised a, inserted adjective',r'\unsure{minimal|minimum|privilégié}','minimal','minimal','resolved',
  'The replacement line shows m-i-n-i-m followed by the low a and final rising l; it lacks the long descender and different sequence required by privilégié, and the ending is not um.','a_replacement','high',True)
rows[-1]['diff_H']=False
D('Revised a, noun in replacement','élément minimal','minimal','élément minimal',False,True,'omission',
  'A separate accented élément precedes minimal above the struck plus petit élément. H retains only the adjective.','a_replacement','high',True)
D('Revised a, dans insertion',r'\inserted{dans}','dans',r'\inserted{dans}',False,True,'insertion or placement',
  'Dans is written higher than the live sentence baseline, directly before the displayed tilde-Y fiber.','a_replacement')
A(14,'Revised a, old i.e. condition',r'\unsure{i.e.}','i.e.',r'\unsure{i.e.}','retained',
  'Small separated vertical/dotted remnants occur immediately before the struck X≪Y′≤Y condition. The horizontal cancellation crosses their baseline, so the entire abbreviation remains uncertain.','a_replacement','low',True)
A(15,'Revised a, live naming parenthesis',r'\unsure{posons|posant}','posons (struck)','posons','resolved',
  'The parenthetical word has low rounded final n-s strokes and no final tall t. It lies on the added line above the separately struck old condition.','a_replacement','high',True)
D('Revised a, state and end of naming parenthesis','inserted (posons X circle≪Y si c’est Y)','struck posons X circle≪Y si ill','live inserted (posons X circle≪Y si c’est Y)',False,True,'deletion state (struck given live or live given struck)',
  'The cancellation belongs to the lower i.e. X≪Y′≤Y⇒Y′=Y line. The parenthesis is above it; its posons, circle over the double angle, si c’est and terminal Y remain live.','a_replacement','high',True,
  math='The live text defines the circled refinement relation; treating it as cancelled removes its definition.')
A(16,'Renumbered compatibility axiom, old digit',r'\deleted{\unsure{5}}6','6 (overwriting mentioned only)',r'\deleted{\unsure{5}}6','retained',
  'The new 6 has a closed lower loop. An older bar/curve survives inside it but is too merged to read 5 without a doubt mark.','renumbered','low',True,'omission')
A(17,'Renumbered transitivity axiom, old digit',r'\deleted{\unsure{6}}5','5 (overwriting mentioned only)',r'\deleted{\unsure{6}}5','retained',
  'The new 5 is clear; the old upper and lower remnants are overlapped by its tall left stroke and return. Old 6 remains provisional.','renumbered','low',True,'omission')
D('Margin beside renumbered axioms, two curved strokes','upper pointed curve and lower open return','curve described as interchanging two lines','upper pointed curve and lower open return, drawn',False,True,'drawing or diagram',
  'One long curve climbs from the left toward an upper-right arrowhead. A separate lower curved return has open endpoints and no second arrowhead.','renumbered')
D('Finite-type transition, first clause','on peut laisser tomber',r'\add{bien \uncertain{connues}} \ill{}','on peut laisser tomber',False,True,'misread word',
  'The supplied upper half shows the continuous on peut laisser tomber line; no separate inserted bien connues occurs there.',conf='high',marked=True)
A(18,'Finite-type transition, right-edge figure-family symbol',r'\unsure{\widetilde{\mathscr F}|\mathscr F}',r'\widetilde{\mathfrak F}',r'\unsure{\widetilde{\mathscr F}|\mathscr F}','retained',
  'The main F upper bar and stem are clipped at the black edge. A separate short upper curve favors a tilde, but part of the decoration is beyond the usable right boundary.','edge_structure','medium',False,'misread symbol or index')
D('Finite-type transition, insertion au profit',r'\inserted{au profit de COMPAT,}',r'\add{\ill{} au profit de COMPAT}',r'\inserted{au profit de COMPAT,}',False,True,r'readable ink left as `\ill{}`',
  'Au profit de and the compatibility sign form the complete raised insertion; a comma follows the sign. No additional unreadable word precedes au.',crop='range_connector',marked=True)
D('Finite-type transition, connector At_M1 … At_M3','à','à',';',True,True,'other',
  'Between 1 and the following At there are two vertically separated marks: a small upper point and a lower diagonal comma stroke descending left. There is no a body or grave-accented word.','range_connector','high',
  math='Literal punctuation is preserved; the transcription does not impose a range word.')
D('Finite-type transition, par (a) de la','de la','et la','de la',False,True,'misread word',
  'After (a), the connector starts with the loop and rising stroke of d, followed by e; the following la is separate.','range_connector')
A(19,'Cancelled finite-type axiom label, digit',r'\unsure{1|0}','number omitted','1','resolved',
  'The digit has a slanting upper entry and tall narrow stem/foot; there is no closed oval counter of 0.','old_tf_label','medium',True,'misread symbol or index')
D('Cancelled finite-type axiom label, tf','(tf)',r'(\ill{})','(tf)',False,True,r'readable ink left as `\ill{}`',
  'The parentheses enclose a short t and a tall looped f with long descender, crossed by the same horizontal cancellation. No points occur between t and f.','old_tf_label',marked=True)
A(20,'Before page 5, cancelled At',r'\unsure{At}',r'\struck{\ill{}}','At','resolved',
  'The triangular A and adjacent tall t remain visible at the left of the heavy crossing. The diagonal strokes that follow are the cancellation.','page5','medium',True,'readable ink left as `\ill{}`')
A(21,'Before page 5, live reference word',r'\unsure{page|p.}',r'\uncertain{Voir} p.','page','resolved',
  'Following the cancelled At are a tall descending p and several distinct connected low letters, including a g-like loop and final e stroke. This is a word, not p. alone; no preceding Voir is visible.','page5','medium',True)
D('End of finite-type replacement paragraph, compatibility star','COMPAT^*','COMPAT','COMPAT^*',False,True,'omission',
  'A small raised star is visible to the upper right of the compatibility sign in the supplied upper half.',
  math='Preserves the explicitly starred occurrence rather than silently identifying it with the unstarred sign.')
A(22,'Slanted i.e. margin, implication-like sign','rounded-ended double stroke | standard implication','standard implication','literal double shaft with rounded upper right return','resolved',
  'The upright crop shows two nearly parallel horizontal shafts. The upper one bends down at the right into a rounded return; no angular arrowhead is present.','ie_margin','high',False,'drawing or diagram')
D('General case, introduction','quand on a simplement',r'grâce à \uncertain{laquelle}','quand on a simplement',False,True,'misread word',
  'The supplied lower half gives the separate quand, on, a, and long simplement word before the compatibility sign.',marked=True)
D('General case, participle','satisfaisant','satisfait','satisfaisant',False,True,'misread word',
  'The final connected a-n-t sequence is visible after satisfa-i-s; the word is longer than satisfait.')
A(23,'Finite-type display, cancelled word',r'\unsure{formées}','unnamed struck word in note',r'\unsure{formées|fermées}','changed',
  'The long f descender, following low connections and final accented/looped ending survive. The first internal vowel is covered by the strike and may be o or e.','finite_cancellations','low',True,'omission')
A(24,'Finite-type display, cancelled abbreviation',r'\unsure{t.q.}','omitted','t.q.','resolved',
  'Below the inserted que, the old tall t stroke and following q-like loop remain with small separated points; they are crossed by the old baseline cancellation.','finite_cancellations','medium',True,'omission')
D('Finite-type display, colon in insertion','telles que :','telles que','telles que :',False,True,'other',
  'Two vertically spaced points follow the inserted que at the right end of the raised phrase.','finite_cancellations')
D('Finite-type display, Phi de t.f. placement','insertion linearized immediately before de M,≤','insertion mentioned in note, placed inline','insertion above the far-right de M,≤',True,True,'insertion or placement',
  'Phi de t.f. sits a full short line above the final de M,≤, not between the preceding printed baseline words. Its curved guide is drawn under the insertion.','finite_placement')
D('Finite-type display, parentheses around ordered M','M,≤','(M,≤)','M,≤',False,True,'text not on the page',
  'The left curved stroke rises toward and under the added Phi de t.f.; it continues far beyond the short de M,≤ phrase. No matching closing parenthesis occurs after ≤.','finite_placement',
  math='Does not add a pair of grouping delimiters absent from the source.')
D('Finite-type display, curved strokes','not reproduced','partly interpreted as a parenthesis','curved guide under insertion and thin lower return near implication, reproduced',True,True,'drawing or diagram',
  'The long upper curve starts left of de M and runs under the insertion to a raised right endpoint. Another thin return comes down below the long f-stroke of fermées toward the implication shaft. Their graphic geometry is retained without inventing semantic arrowheads.','finite_placement')
D('Antifilter paragraph, structure … plus','de plus','en plus','en plus',True,False,'misread word',
  'The connector begins with a small low e-loop and continues into a low n; it has no ascender required by d. The following plus is separate and clear.','structure_plus')
D('Antifilter paragraph, abbreviation ens','ens','ens.','ens',False,True,'abbreviation expanded or spelling modernised',
  'The lower half shows a gap after the final s before ordonné, with no isolated abbreviation point.')
D('First Mulomb occurrence in family set','Mulomb','Multomb','Mulomb',False,True,'misread word',
  'The lower half shows M-u-l-o-m-b; there is no separate t stem or crossbar after l.')
D('Second Mulomb occurrence in defining equation','Mulomb','Multomb','Mulomb',False,True,'misread word',
  'The targeted crop shows the same M-u-l-o-m-b sequence, including the tall looped l and final b-like return; no t is present.','mulomb_argument')
D('Second Mulomb occurrence, argument','F','F',r'\unsure{F|\mathscr F}',True,True,'misread symbol or index',
  'Inside the parentheses the F-like glyph has a high curving upper arm and a separate short horizontal middle arm, with a crossed/curved main stroke. Its exact plain-versus-cursive alphabet is less secure than a normalized F suggests; no prime or index is visible.','mulomb_argument','low',
  math='The written argument is not silently changed to match the surrounding intended definition; the alphabet uncertainty is explicit.')
D('Tiny où before second Mulomb, ink state',r'\deleted{où}','où',r'\unsure{\deleted{où}|où}',True,True,'deletion state (struck given live or live given struck)',
  'The o/u and grave mark are visible. A heavy horizontal stroke crosses their middle but stays close to the word’s own connecting stroke; it favors cancellation, without an unambiguous extended strike on both sides.','deleted_ou','low')
A(25,'Crossed object before Omb(x)',r'\unsure{X}','unnamed struck sign in note',r'\unsure{x|X}','changed',
  'A small hooked crossed letter sits above a much larger cancelling X. Its curved hooks and relative size favor lowercase x, but the broad cancellation prevents a secure case decision.','deleted_X','low',True,'misread symbol or index')
D('Omb argument inside Mulomb defining set','Omb(x)','Omb(X)','Omb(x)',False,True,'misread symbol or index',
  'The lower half shows a small x between parentheses, distinctly smaller than the following capital X in X∈tilde F.',
  math='Preserves a literal case mismatch instead of standardizing the bound letter.')
D('After Mulomb defining set, punctuation','no comma','comma','no comma',False,True,'text not on the page',
  'The defining line ends at the right brace; the lower half shows no comma following it.')
D('Final principal-lower-set subscript',r'M_{\ll x}',r'\mathcal M_{\ll X}',r'M_{\ll x}',False,True,'misread symbol or index',
  'The subscript after the double angle contains a small crossing x; it is not raised to the full capital X used earlier in Omb X.',
  math='The manuscript’s local case is kept even though the displayed formula also uses capital X.')
D('Final reference, cf abbreviation','cf','cf.','cf',False,True,'abbreviation expanded or spelling modernised',
  'The supplied lower half has cf followed directly by Scholie, without a separate point.')
A(26,'Final reference, GF/GE',r'\unsure{GF|GE}','GF','GF','resolved',
  'The second capital has a vertical stem, short upper arm and longer middle arm, with no lower horizontal arm. It is F, following the large G.','GF','high',False,'misread symbol or index')
rows[-1]['diff_H']=False
D('Final reference, alternative page citation','ou mieux à la page 32',r'en \uncertain{nombre} de \ill{} p. 32','ou mieux à la page 32',False,True,'misread word',
  'The lower half gives short ou, the long m-i-e-u-x word, à la and the full written page before 32.',marked=True)
D('Final reference, page 32 underline',r'\uline{page 32}','p. 32 (not underlined)',r'\uline{page 32}',False,True,'other',
  'A separate horizontal line runs under both the word page and 32 in the lower half.')
D('Final interpretation, comme sous-atelier','comme sous-atelier','comme un sous-atelier','comme sous-atelier',False,True,'text not on the page',
  'The words comme and sous-atelier are adjacent with an ordinary word gap; no separate un is written.')
D('Final parenthesis, adjective','spacieux','spécieux',r'\unsure{spacieux|specieux}',True,True,'misread word',
  'The s-p and c-i-e-u-x portions are visible. The intervening low open vowel is faint and does not securely distinguish a from e; no acute accent is separately visible over it.','spacieux','low')

coverage = [
 'Handwritten page number 6 and opening entirely cancelled At_M4 assertion, all domains, fiber exponent X, delimiters and least-element wording.',
 'Upper-left note in full: underline At, overwritten numeral, sans référence à, two figure-family symbols, directement en terme(s), ordered tuple and northeast arrow.',
 'All cancelled initial trials of a: Posant line, separate upper quantifier/definition line, right interlinear word pair, their arrow and letter doubts.',
 'Live a: Si X≪Y; cancelled plus petit élément; inserted élément minimal and dans; tilde-Y fiber, Z and X≪Z; cancelled i.e. formula; live inserted naming parenthesis.',
 'Live b in full, both hollow circled refinement signs, Y/Y′ compatibility, conclusion Y=Y′, primes and punctuation.',
 'Renumbered live At_M6 compatibility implication, old numeral, inequality and upper curved arrow.',
 'Renumbered live At_M5 circled-refinement transitivity, old numeral and lower open return.',
 'D’autre part paragraph: figure-family symbol, figures de type fini, on peut laisser tomber, clipped structure symbol, raised au profit de insertion, literal semicolon between axiom references, par (a) de la.',
 'Fully cancelled finite-type axiom label At_M1(tf) and sentence Toute partie fermée majorée de M est de t.f.',
 'Crossed At, live page 5, full repeated parenthesis, condition b, starred compatibility sign, full final (page 5).',
 'Slanted i.e. marginal note, both inequalities and primes, compatibility signs and rounded-ended double shaft, read in its one rotated crop.',
 'General-case sentence: quand on a simplement, satisfaisant, condition b), At_M4,5,6 and on trouve.',
 'Complete finite-type-family display: tilde/script letter and tf subscript; ensemble des parties fermées; elevated Phi de t.f.; de M,≤; deleted formées/fermées and t.q.; inserted telles que :; pairwise compatibility formula; final point; curved stroke geometry.',
 'Antifilter paragraph in full: cependant, un choix de structure en plus, certains antifiltres infinis, ens without point, tilde-F_tf, précédent and ellipsis.',
 'On peut aussi interpréter sentence, exact figure-family symbol and en termes de.',
 'Script-F-star set of Mulomb(F), membership F∈script F, subset of Fig(M), all delimiters.',
 'Tiny où and its uncertain state; second Mulomb spelling and argument alphabet; cancelled x/X; Omb(x); upper-case X∈tilde F; brace and lack of added comma.',
 'Omb X set, Y∈M and Y≪X, equality to M subscript double-angle small x, terminal point.',
 'Final full reference and interpretation: cf without point; Scholie GF p.28; et axiomes; ou mieux à la; underline page 32; comma and comme sous-atelier; pas néc. spacieux/specieux; Fig(M) and final point.'
]

proof = {
 'statement_id':'R1-007-minimal-plus-compatible-uniqueness',
 'type':'targeted proof check',
 'who':'GPT-6 Astra Pro, inherited configuration; effort setting not exposed; R1',
 'statement':'Assume At_M4(a,b) as written on scan007. If A⊂M is downward closed and pairwise compatible, and A_X={Y∈A | X≪Y} is nonempty, then A_X has a least element.',
 'steps':[
   'Choose Y0∈A_X. By a, the fiber {Z≤Y0 | X≪Z} has a minimal element Z0.',
   'Downward closure gives Z0∈A. If W≤Z0 and X≪W, then W lies in the same fiber below Y0; minimality forces W=Z0. Therefore Z0 is minimal in its own fiber, so X circle≪Z0 by the live parenthetical definition.',
   'For arbitrary Y∈A_X, repeat a to obtain a minimal Z≤Y. Again Z∈A and X circle≪Z.',
   'Since A is pairwise compatible, Z0 and Z are compatible. Clause b gives Z=Z0. Hence Z0≤Y for every Y∈A_X; Z0 is least.'
 ],
 'outcome':'Verified under the explicitly stated closure, compatibility and nonemptiness assumptions. This conditional lemma does not identify an unwritten intended correction to scan006 or assert that its entire domain is identical to A_X.',
 'effect_on_transcription':'None. The written word minimal is retained; it is not replaced by least/plus petit.'
}

S = {
 'row_id':'SA21-K7-01',
 'scope':'Only this already-authorized row was consulted; no other S rows or later manuscript pages were opened.',
 'row_summary':'S calls the scan006 At6 incidence hypothesis a slip, proposes X≪F, and cites scan007 At_M4a and the circled-refinement definition.',
 'actual_007_ink':'The live a begins Si X≪Y; the live insertion says élément minimal; the live naming parenthesis says posons X circle≪Y si c’est Y. An earlier unconditional least-element assertion and the later words plus petit élément are cancelled.',
 'confirmation':'The specific textual cross-reference to refinement X≪Y is confirmed. The new page also confirms that the circled relation is defined in the live revision.',
 'qualification':'The scan007 wording is minimal, not an unqualified least-element assertion. Its b clause adds compatible uniqueness. The conditional proof recorded here shows how a and b yield leastness in a nonempty downward-closed pairwise-compatible fiber.',
 'status_of_006_correction':'No alteration of the scan006 diplomatic text. That page visibly wrote X◁F with the membership parenthesis; its redundancy proof is already in R1-006-S-At6-incidence-triviality. Scan007 supplies additional support for S’s diagnosis, but an inferred authorial intention remains separate from ink.',
 'new_mathematical_check_event':proof['statement_id']
}

unresolved = [
 {'place':a['place'],'reading':a['reading'],'confidence':a['confidence'],'evidence':a['evidence'],'crop':a['crop']}
 for a in audits if a['status']!='resolved'
]
for r in rows:
 if r['place'] in ('Second Mulomb occurrence, argument','Tiny où before second Mulomb, ink state','Final parenthesis, adjective'):
  unresolved.append({'place':r['place'],'reading':r['reading'],'confidence':r['confidence'],'evidence':r['evidence'],'crop':r['crop']})

end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report={
 'reader':'R1','scan':'007','H_page':6,
 'start_utc':(out/'scan007_start.txt').read_text().strip(),'end_utc':end,
 'model':'GPT-6 Astra Pro, inherited configuration; effort setting not exposed',
 'independence':'Only own earlier outputs, C/H for scan007, governing instructions, current scan images and the one authorized S row were consulted. No other reader or main adjudication output and no later manuscript page was read.',
 'images_viewed':[
   {'file':f'source/SP35_CW_156-7_scans/H156-01_156-7_scan007{s}.jpg','role':role,'views':1}
   for s,role in [('', 'whole layout'),('_a','upper full-resolution half'),('_b','lower full-resolution half')]
 ]+[dict(c,role='targeted unresolved-locus crop',views=1) for c in crops],
 'view_note':'The first attempted combined crop-display call was truncated before usable images reached the reader. Existing crops were subsequently displayed in small calls and inspected; no crop was recreated. Whole and supplied halves were not reopened.',
 'coverage':coverage,
 'notation':[
   {'sign':'Figure-family alphabet','reading':r'\unsure{\mathscr F|\mathcal F} at first occurrence, then \mathscr F by provisional consistency','evidence':'Repeated cursive F, unlike a separately distinguishable printed font; exact family remains doubtful.'},
   {'sign':'M alphabet','reading':r'\unsure{M|\mathcal M} initially, then M','evidence':'Repeated tall M outline; the stylization does not independently settle font family.'},
   {'sign':'Phi','reading':r'\Phi on this page','evidence':'Clear closed wide oval, axial stem and horizontal foot in the first crop.'},
   {'sign':'Refinement','reading':r'\ll and \overset{\circ}{\ll}','evidence':'Plain and hollow-circle-decorated double angles remain distinct in the live a/b and transitivity lines.'},
   {'sign':'Compatibility','reading':'opposed overlapping chevrons drawn in TikZ; one explicit raised star in the finite-type paragraph','evidence':'Same repeated two-chevron shape. Macro syntax alone is not counted as a difference.'},
   {'sign':'Margin implication-like mark','reading':'two horizontal shafts, rounded upper-right return','evidence':'Single rotated crop shows no angular arrowhead.'},
   {'sign':'Axiom separator','reading':'; between At_M1 and At_M3','evidence':'Upper point and lower descending comma, no letter a.'},
   {'sign':'Operator spelling','reading':'Mulomb, twice','evidence':'No t in either occurrence.'},
   {'sign':'Local case','reading':'Omb(x), X∈tilde F, Omb X, M_{≪x}','evidence':'Small x and full capital X remain visibly distinct; no normalization.'},
   {'sign':'Abbreviations','reading':'tf in axiom label; t.f. in prose; t.q.; ens without point; cf without point; néc.','evidence':'Literal local point patterns retained.'}
 ],
 'math_notes':[
   {'claim':'The page revises At_M4 into refinement-fiber minimality plus compatible uniqueness, defines circled refinement, and retains compatibility implication and circled-refinement transitivity under revised numbers.','status':'Read and transcribed; no proof of the entire axiom system claimed.'},
   {'claim':proof['statement'],'status':'Targeted proof actually performed; steps and exact assumptions recorded in check_events.'},
   {'claim':'For finite-type figure families the page proposes replacing the figure-family structure by compatibility with further conditions; in the general case it asks for a choice of certain infinite antifilters and interprets the family as a sub-atelier of Fig(M).','status':'Read and transcribed only; the equivalence/construction has not been independently proved.'},
   {'claim':'The live wording supports S’s cross-reference to refinement, while scan006 incidence remains the actual ink of that page.','status':'Textual comparison confirmed; authorial correction remains an inference, not an emendation of either page.'}
 ],
 'check_events':[dict(proof,date=end)],
 'author_qualifications':['il faut cependant un choix de structure en plus','On peut aussi interpréter','pas néc. '+r'\unsure{spacieux|specieux}'],
 'author_qualifications_note':'No separate à vérifier, sauf erreur, je présume or isolated doubt-question is visible on this page. The qualifications above are literal scope/modality words, not invented declarations of proof status.',
 'differences':rows,'C_doubt_audit':sorted(audits,key=lambda a:a['number']),
 'unresolved':unresolved,
 'missing_from_both':[
   {'place':'At_M1 … At_M3 connector','content':';','evidence':'Both witnesses replace the two-component punctuation by à.','crop':cropmap['range_connector']['file']},
   {'place':'Finite-type-family display','content':'Explicit curved guide under the raised Phi de t.f. and thin lower return near the implication','evidence':'Neither witness reproduces both strokes geometrically; H turns part of the upper one into parentheses.','crop':cropmap['finite_placement']['file']}
 ],
 'S_comparison':S,
 'counts':{'difference_rows':len(rows),'diff_C':sum(r['diff_C'] for r in rows),'diff_H':sum(r['diff_H'] for r in rows),
           'C_doubts':len(audits),'C_doubts_resolved':sum(a['status']=='resolved' for a in audits),
           'C_doubts_retained':sum(a['status']=='retained' for a in audits),'C_doubts_changed':sum(a['status']=='changed' for a in audits),
           'targeted_crops':len(crops),'unresolved_loci':len(unresolved)}
}
assert len(audits)==26
assert [a['number'] for a in sorted(audits,key=lambda a:a['number'])]==list(range(1,27))
(out/'scan007.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

lines=[
 '# R1 independent reading — scan 007 (H page 6)','',
 f"Completed {end}. {len(rows)} recorded difference/audit loci; {report['counts']['diff_C']} differ from C and {report['counts']['diff_H']} from H. All 26 C doubt instances are audited: 9 resolved, 14 retained, 3 changed. Nineteen targeted crops; the whole and each supplied half were read once.",'',
 '## Principal ink decisions','',
 '- The live revision says **élément minimal**. **Dans** and the parenthesis **(posons X circled-≪ Y si c’est Y)** are insertions. The parenthesis is live; the lower **i.e. X≪Y′≤Y ⇒ Y′=Y** line is cancelled.',
 '- The range-like connector is a literal **semicolon**: **At_M 1 ; At_M 3**. Both witnesses supply **à**.',
 '- Read **structure en plus**, confirming H and changing C’s **de plus**.',
 '- Read the cancelled label **At_M 1 (tf)**, then crossed **At** and live **page 5**. The right-edge figure-family decoration remains uncertain because the scan clips it.',
 '- The slanted margin has a double shaft with a **rounded upper-right return**, not a normal pointed implication arrow. Its primes and inequalities are preserved.',
 '- **Φ de t.f.** is written above the far-right **de M,≤**, with a long curved guide. A further thin return descends beneath the long f-stroke of **fermées** toward the implication. Both shapes are drawn. The manuscript has no enclosing pair of parentheses around **M,≤**.',
 '- **Mulomb** has no t in either occurrence. The second argument remains **F|script F** because the exact alphabet of the curved/crossed F-like glyph is not secure. **Omb(x)** and **M_{≪x}** retain lowercase x, alongside the capital X elsewhere.',
 '- The tiny **où** favors cancellation, but its stroke can merge with the word’s own joining stroke; state remains **deleted où | live où**. The crossed entry before **Omb(x)** is **x|X**.',
 '- The final reference is **GF**, then **ou mieux à la page 32** with **page 32** underlined. There is no added **un** in **comme sous-atelier**. The faint adjective is **spacieux|specieux**; no acute accent is visible on the disputed vowel.','',
 '## Remaining doubts','',
 'The opening M and figure-family alphabets, the end of the cancelled élément, old overwritten numerals, terme(s), several heavily cancelled trial words/signs, clipped right-edge decoration, cancelled formées|fermées, the second Mulomb argument, tiny où state, crossed x|X, and spacieux|specieux remain explicitly doubtful. Full literal readings and individual stroke evidence are in the JSON and TeX.','',
 '## S SA21-K7-01 and mathematics','',
 'Scan 007 confirms the sweep row’s cited live condition **Si X≪Y** and the live circled-refinement definition. It also writes **minimal**, after cancelling **plus petit élément**. This is textual support for S’s diagnosis of the earlier incidence wording, not permission to change scan 006’s actual ink.','',
 'A targeted conditional proof was performed: if A is downward closed and pairwise compatible and A_X is nonempty, clauses a and b give A_X a least element. For each Y in the fiber, a supplies a minimal Z≤Y; it is minimal in its own fiber and hence circled-related to X. Closure places each such Z in A, compatibility and b identify them all, and the common Z lies below every Y. Exact assumptions and steps are recorded in check event **R1-007-minimal-plus-compatible-uniqueness**. No proof of the entire figure-family reconstruction or of an unwritten authorial correction is claimed.','',
 '## Independence and scope','',
 'Only scan 007 and its C/H page were read in this gate; only S row SA21-K7-01 was consulted. No scan 008, other-reader report, or main decision was opened. Awaiting the next page assignment.',''
]
(out/'scan007.md').write_text('\n'.join(lines))
print(json.dumps(report['counts'],ensure_ascii=False))
print('Saved scan007.tex, scan007.json, scan007.md and retained scan007_crops.json')
