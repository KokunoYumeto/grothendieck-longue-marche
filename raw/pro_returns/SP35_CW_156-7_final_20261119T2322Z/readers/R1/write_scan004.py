from pathlib import Path
from datetime import datetime, timezone
import json
p=Path(__file__).parent
crop=lambda x:f'readers/R1/crops/scan004_{x}.jpg'
tex=r'''\scanpage{4}
\mspage{3}
(et je suis resté muet sur ce support dans la mouture précédente \unsure{GF|CF} $\underline{\overline{\mathrm{VI}}}$). Quand on interprète $F$ comme figure ensembliste dans l'ens. des lieux $\unsure{L|\mathcal L}$ \deleted{\unsure{ou|de}} (pratiquement cela signifie qu'on a un atelier ensembliste), on l'écrira $\mathrm{mulomb}(F)$ (petite multiombre), son support sera $\mathrm{omb}(F)$.

% The live prefix pre is shared; the crossed cluster is local to the following stem.
\uline{Données} \uline{pre\deleted{\unsure{l}}mières} :
\[
\left\{\begin{aligned}
&\unsure{\mathscr F|\mathcal F} &&\text{ensemble de figures}\\
&\leq &&\text{\unsure{rellation|relation} d'\uline{inclusion} de figures}\\
& &&F\leq G\ \overset{\text{déf}}{\Longleftrightarrow}\ F\ \text{sous figure de }G\\
&\ll &&\text{relation de raffinement}\\
& && F\ll G\ \overset{\text{def}}{\Longleftrightarrow}\ F\ \text{raffine }G
\end{aligned}\right.
\]
avec
\[
F\leq G\ \Longrightarrow\ F\ll G\tag*{\makebox[0pt][r]{\makebox[\displaywidth][l]{\uline{At} 0}}}
\]
% Slanted note, independently rotated once.
\margin{NB. Ce sera aussi contenu dans \uline{At}~4 plus bas}
-- axiome si évident que je ne l'avais pas inclus dans les axiomes numérotés.

\diagram{\(\begin{array}{@{}clp{.53\linewidth}@{}}
\text{\textcircled{\scriptsize a}} & F\vee G\ \text{ou }F\cup G &
\uline{figure} @@\uline{engendrée}'' ou @@\uline{réunion}'' ou @@\uline{somme}'' : c'est le sup au sens de $\leq$ (quand il existe\unsure{\}|)} -- auquel cas c'est aussi un sup pour $\ll$\\
\end{array}\)}
\margin{\deleted{\unsure{Question}}\inserted{NB.} : Si $(F,G)$ ont un sup pour $\ll$ (c'est tjrs le cas dans le cas ensembliste $\mathrm{Fig}(L)$), ce n'est pas néc. un sup pour $\leq$}
\margin{\uline{NB} $\widetilde{F\cap G}=\widetilde F\cap\widetilde G$}
\diagram{\(\begin{array}{@{}clp{.53\linewidth}@{}}
\text{\textcircled{\scriptsize b}} & \begin{aligned}&F\wedge G\ \text{ou } F\cap G\\&\quad(=\mathrm{Inf}^{\leq}(F,c))\end{aligned}
& figure \uline{intersection}\inserted{ou Inf pour $\leq$} -- existe toujours ($\overline{\mathrm m}$ pour \unsure{familles|famille} infinie (non vide)) ; quand en $=$ temps $F\vee C$ existe, alors c'est aussi le Inf pour $\ll$.\\
\end{array}\)}
\margin{\uline{NB} Existe dans le cas ensembliste $\mathrm{Fig}(L)$ et dans le cas mechisé}
\diagram{\(\begin{array}{@{}clp{.53\linewidth}@{}}
\text{\textcircled{\scriptsize c}} & F\mathbin{\ldotp}G\quad (=\mathrm{Inf}^{\ll}(F,c)) &
figure @@\uline{intersection} \uline{fine}'' (quand elle existe) : Inf pour $\ll$.\\
&\deleted{\unsure{CG|G}}&\\
\text{\textcircled{\scriptsize\unsure{d}}} & \varnothing_{\mathscr F} &
figure vide : plus petit élément de $\mathscr F$ (pour $\leq$ \uline{et} pour $\ll$)\\
\end{array}\)}
'''.replace('@@',chr(96)*2)
(p/'scan004.tex').write_text(tex)
D=[]
def add(place,C,H,reading,dc,dh,kind,conf,evidence,cr=None,cd='not applicable',mh=False,mc=None):
 D.append(dict(id=f'R1-004-{len(D)+1:02d}',place=place,C=C,H=H,reading=reading,diff_C=dc,diff_H=dh,kind=kind,marked_in_H=mh,confidence=conf,evidence=evidence,crop=crop(cr) if cr else None,C_doubt_status=cd,math_consequence=mc))
add('Opening punctuation','(et','» (et','(et',False,True,'text not on the page','high','The first baseline begins with a curved opening parenthesis; no closing guillemet precedes it. Whole and top half.')
add('Opening clause','je suis resté muet',r'je suis tenté \uncertain{maintenant}','je suis resté muet',False,True,'misread word','high','The short second word has m/u/e/t rather than the long -aintenant run; resté has the initial r and the crossed t before final accented e. Top half.',mh=True)
add('Reference initials',r'\unsure{GF|CF}','GF',r'\unsure{GF|CF}',False,False,'other','medium','A broad open C-shaped arc ends with a short descending right tip; the latter permits G, but it does not supply an unambiguous internal G bar. F has two arms.','GF','retained')
add('Reference Roman numeral',r'\underline{\overline{\mathrm{VI}}}','VI',r'\underline{\overline{\mathrm{VI}}}',False,True,'omission','high','Both a long upper rule and a lower rule enclose VI.','GF')
add('After comme','comme figure','comme une figure','comme figure',False,True,'text not on the page','high','Figure follows comme directly; there is no separate une on the baseline. Top half.')
add('Lieux-set letter',r'\unsure{L|\mathcal L}',r'\mathcal L',r'\unsure{L|\mathcal L}',False,False,'other','medium','The capital has a sloped ascender, a lower-left loop and a broad right foot. These establish L but do not settle its plain/calligraphic typographic representation.','L_deleted','retained')
add('Crossed word after L',r'\deleted{\unsure{ou|de}}',r'\struck{ce}',r'\deleted{\unsure{ou|de}}',False,True,'misread word','low','Two small upper curves remain above a strong strike; the first loop and short following turn favour ou, with de still possible. The strike makes ce insecure.','L_deleted','retained')
add('Comma after L','no comma before cancellation','comma before cancellation','no comma before cancellation',False,True,'text not on the page','high','No discrete comma occurs between the long foot of L and the cancellation.','L_deleted')
add('Parenthetic demonstrative','pratiquement cela signifie','pratiquement ceci signifie','pratiquement cela signifie',False,True,'misread word','high','The terminal a of cela is closed and joined to its exit; there is no i dot. Top half.')
add('Parenthetic existence clause',"qu'on a un atelier","que c'est un atelier","qu'on a un atelier",False,True,'misread word','high','An apostrophe separates qu from on, followed by a small a; no c’est group is present. Top half.')
add('End of atelier parenthesis',"), on l'écrira",") on l'écrira","), on l'écrira",False,True,'omission','high','The closing parenthesis is followed by a separate low comma before on. Top half.')
add('Lowercase multiombre operator',r'\mathrm{mulomb}(F)',r'\mathrm{multomb}(F)',r'\mathrm{mulomb}(F)',False,True,'misread symbol or index','high','The word has m-u-l-o-m-b in a continuous run, with no t between the looped l and o. The initial m and initial o of omb are lowercase. Top half.',mc='The operator is mulomb on this page; preserve its actual spelling and lowercase initial.')
add('Heading live word',r'\unsure{premières}','préliminaires','premières',True,True,'misread word','high','The shared pre is followed by the retraced m and the visible i-è-r-e-s ending. There is no long -liminaires ending.','heading','resolved')
add('Heading cancelled cluster and anchor',r'\deleted{\unsure{pré}} before premières','no cancellation',r'pre\deleted{\unsure{l}}mières',True,True,'deletion state (struck given live or live given struck)','low','The live p-r-e at the left is not barred. The cancellation is concentrated on a tall looped stem immediately after that prefix, above/across the live m. A former l is the best tentative reading; a whole separately cancelled pré is not clearly visible.','heading','changed')
add('Figure-set alphabet, including empty-set subscript and final prose',r'\unsure{\mathscr F|\mathcal F}; later \mathscr F',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}; later \mathscr F',False,True,'misread symbol or index','medium','The first symbol is a long hooked cursive F with a narrow top loop and an elongated descending curve, not a blackletter F. The final occurrences repeat the script sign; mathscr versus mathcal remains open.','setF','retained',mc='A script figure-set F is distinct from the plain figure variables F and G.')
add('Inclusion noun',r'\unsure{rellation|relation}','relation',r'\unsure{rellation|relation}',False,False,'other','medium','Two close high strokes follow the first small loop after r; one can be a second l, but its lower part merges into a. The shorter spelling cannot be ruled out solely from the merged strokes.','rellation','retained')
add('After inclusion',r'\unsure{de|des}','des','de',True,True,'misread word','medium','After the d ascender there is one small e turn and a long exit stroke. I do not see an independently formed final s.','de_des','resolved')
add('Data-table punctuation and sous figure','no commas after figures/raffinement; sous figure','commas after figures/raffinement; sous-figure','no commas after figures/raffinement; sous figure',False,True,'other','high','The formula lines are separate baselines after the prose descriptions; no comma is written at either prose end. Sous and figure are separated by a blank, without a hyphen. Top half.')
add('First equivalence label',r'\unsure{déf|def}','déf','déf',True,False,'other','medium','A small detached rising stroke lies over the reduced e immediately to the left of the tall f.','def_first','resolved')
add('Second equivalence label','def','déf','def',False,True,'abbreviation expanded or spelling modernised','high','The small e turns directly into the f; there is no separate mark above it comparable to that in the first label.','def_second')
add('Left brace joining the data','drawn left brace','described in editorial note','drawn left brace',False,True,'drawing or diagram','high','A single large left brace spans the ensemble and two relation entries. The transcription reproduces it as a brace, rather than replacing it with prose. Whole and top half.')
add('At 0 label underline',r'\uline{At} 0',r'\emph{At 0}',r'\uline{At} 0',False,True,'other','high','The line under the label stops after At; the baseline 0 is outside the underline. Top/bottom overlap.')
add('Axiom commentary',"je ne l'avais pas inclus",r'je ne \uncertain{le mets} pas \uncertain{inclus}',"je ne l'avais pas inclus",False,True,'misread word','high','The short apostrophized l’ leads into avais, with v and the final low is stroke; inclus follows pas as a clear word. Both halves overlap this passage.',mh=True)
add('Slanted At 0 marginal note',r'NB. Ce sera aussi contenu dans \uline{At} 4 plus bas',r'NB. Ce \uncertain{serait} \ill{} dans At 4 plus bas',r'NB. Ce sera aussi contenu dans \uline{At} 4 plus bas',False,True,r'readable ink left as \ill{}','high','On the rotated baseline the short sera ends before aussi; the next line spells contenu with a tall t. At is underlined, the 4 is on the baseline, and plus bas follows.','At0_note',mh=True)
add('Circled labels a and b','circled a and b','(a) and (b), uncertain in a note','circled a and b',False,True,'drawing or diagram','high','Each character sits inside a continuous oval, rather than between two separate parentheses. The lower-case a and b stems are distinguishable in the lower half.',mh=True)
add('Row a underlining','figure, engendrée, réunion, somme all underlined','no corresponding underlines','figure, engendrée, réunion, somme all underlined',False,True,'omission','high','Horizontal strokes run beneath each of the four separate words; the quote marks remain above the line. Bottom half.')
add('Row a closing mark',r'\unsure{)|\}}',')',r'\unsure{\}|)}',True,True,'other','low','The mark has an inward middle notch and two curved parts, favouring a closing brace; an overtraced angular parenthesis remains possible.','a_close','changed')
add('Row a terminal punctuation','no semicolon','semicolon after misplaced insertion','no semicolon',False,True,'text not on the page','high','The row ends at the double refinement sign without a following semicolon. Bottom half.')
add('Struck Question and inserted NB',r'\deleted{\unsure{Question}}\inserted{NB.}',r'NB, with separate note describing perhaps Question',r'\deleted{\unsure{Question}}\inserted{NB.}',False,True,'deletion state (struck given live or live given struck)','medium','The opening Q loop and remaining low strokes lie under a heavy horizontal strike. NB. is above them, a replacement heading. The interior of the cancelled word remains uncertain.','Question','retained',True)
add('First left note abbreviation tjrs','tjrs','toujours','tjrs',False,True,'abbreviation expanded or spelling modernised','high','Only the compact t-j-r-s group appears between est and le cas. Bottom half.')
add('First left note abbreviation néc.','néc.','nécessairement','néc.',False,True,'abbreviation expanded or spelling modernised','high','The word stops after c with a small point; the long expansion is not written. Bottom half.')
add('L in both Fig marginal operators',r'\mathrm{Fig}(L)',r'\mathrm{Fig}(\mathcal L)',r'\mathrm{Fig}(L)',False,True,'misread symbol or index','medium','The argument is the same simple sloping L with long foot used for lieux; I use plain L consistently after the first alphabet doubt. Bottom half.','mechise')
add('NB underlining in second and third left notes',r'\uline{NB}','NB',r'\uline{NB}',False,True,'omission','high','Short rules are visible beneath the NB labels in the last two left notes. Bottom half.')
add('Insertion ou Inf pour ≤ and its anchor','after intersection in row b','after row a','after intersection in row b',False,True,'insertion or placement','high','The leader runs under the raised text then curves down to the gap immediately after the underlined intersection in row b. It does not descend to row a.','b_prose',mh=True,mc='The inclusion infimum description belongs to the intersection operation F∧G / F∩G.')
add('Second arguments in both Inf expressions',r'row b \unsure{c|G}; row c c','G in both expressions','c in both expressions',True,True,'misread symbol or index','high','In row b the open letter is distinctly shorter than the preceding F and has no internal bar or downstroke. Row c repeats a small open c in the bottom half.','b_argument','resolved',mc='The written c is preserved although the adjacent operation is expressed with F and G; no silent variable correction.')
add('Row b transition after intersection','-- existe toujours','(existe toujours','-- existe toujours',False,True,'other','high','The short straight dash precedes existe. The large curved line above it is the insertion leader, not a new opening parenthesis.','b_prose')
add('Parenthesis before barred m',r'\unsure{(|et (}','( within a larger uncertain phrase','(',True,False,'other','high','A single tall curved stroke precedes the barred m. There are no separate e and t letters. Two closing parentheses follow non vide.','b_prose','resolved',True)
add('Barred m abbreviation',r'\overline{\mathrm m}','même',r'\overline{\mathrm m}',False,True,'abbreviation expanded or spelling modernised','high','A small m has a separate straight bar over it; the letters ê-m-e are not written.','b_prose',mh=True)
add('Famille(s) noun',r'\unsure{familles}','familles within uncertain phrase',r'\unsure{familles|famille}',True,False,'other','medium','The end of the long f-am-ill-e run joins into a low terminal flourish. That can include s but does not isolate it decisively; famille remains possible.','b_prose','changed',True)
add('Infinitary parenthesis agreement','infinie (non vide)','infinies (non vides)','infinie (non vide)',False,True,'abbreviation expanded or spelling modernised','high','Infinie ends after its e; vide likewise ends before the closing parenthesis without an added s.','b_prose',mh=True)
add('Time phrase',r'en $=$ \unsure{temps|tps}',r'\uncertain{en outre}',r'en $=$ temps',True,True,'misread word','high','Two parallel horizontal strokes follow en. The following word contains a crossed t, low e/m run, descending p and terminal s, supporting the full temps.','b_prose','resolved',True)
add('Join in row b prose',r'F\vee\unsure{C|G}',r'F\vee G',r'F\vee C',True,True,'misread symbol or index','high','The capital after the v is an open arc with no internal bar or descending finish. It is larger than the c in the Inf argument.','b_prose','resolved',mc='Preserves F∨C in the prose even though the operation row uses F∨G.')
add('Row b terminal punctuation','full stop','semicolon','full stop',False,True,'other','high','There is one point after the final refinement sign, without the upper/lower pair of a semicolon.','b_prose')
add('Final left note adjective',r'\unsure{méchisé|mechisé|quoted mechisé}',r'\uncertain{rectiligne}','mechisé',True,True,'misread word','medium','The word shows the initial low m/e run, a c curve, a tall h, i, s and final accented é. There is no separate accent over the first e. The final high short stroke is the accent on é, not a closing quote.','mechise','resolved',True)
add('Circled third label',r'\textcircled{\unsure{c}}','(c), uncertain in note','circled c',True,True,'drawing or diagram','medium','Inside the circle the stroke is open to the right: it runs left from the upper right, down, and back to the lower right. It is an angular c touching the circle.','label_c','resolved',True)
add('Row c low product dot',r'F\mathbin{\ldotp}G',r'F\cdot G',r'F\mathbin{\ldotp}G',False,True,'misread symbol or index','high','The small point between the letters lies low, near their feet, rather than at mid-height. Bottom half.',mc='Preserves the author’s low point operator.')
add('Row c underline intersection',r'\uline{intersection} \uline{fine}',r'intersection \emph{fine}',r'\uline{intersection} \uline{fine}',False,True,'omission','high','Separate rules are visible under intersection and fine. Bottom half.')
add('Row c terminal punctuation','full stop','semicolon','full stop',False,True,'other','high','A lone dot follows the final refinement sign, not a semicolon. Bottom half.')
add('Crossed text below product',r'\deleted{\unsure{G|CG}}','described as a short crossed word without reading',r'\deleted{\unsure{CG|G}}',True,True,'omission','low','Below the long horizontal strike, a left C-like curve and a second right-hand curved/horizontal group remain. CG is slightly favoured, but a heavily retraced single G is possible.','deleted_c','changed',True)
add('Circled fourth label',r'\textcircled{\unsure{d}}','(d), uncertain in note',r'\textcircled{\unsure{d}}',False,True,'drawing or diagram','medium','A tall inner stem partly follows the enclosing ring and a low hooked loop can form d. The merger with the circle prevents a secure reading.','label_d','retained',True)
add('Final row parentheses and terminal point','(pour ≤ et pour ≪), no final point','pour ≤ et pour ≪, followed by a point','(pour ≤ et pour ≪), no final point',False,True,'other','high','An opening parenthesis stands before pour and a curved closing mark follows the last order sign. No separate terminal point is visible. Bottom half.')
add('Quotation glyphs in rows a and c','paired high strokes','guillemets','paired high strokes',False,True,'other','high','The opening and closing marks consist of pairs of short high strokes, not the angled shapes of guillemets. Bottom half.')
A=[
('GF|CF','retained',r'\unsure{GF|CF}','GF','Open capital has a short descending tip but no decisive internal G bar.'),
('L|mathcal L','retained',r'\unsure{L|\mathcal L}','L_deleted','Cursive stem and foot do not decisively select a typographic alphabet.'),
('deleted ou|de','retained',r'\deleted{\unsure{ou|de}}','L_deleted','Thick strike obscures small upper loops.'),
('deleted pré above heading','changed',r'pre\deleted{\unsure{l}}mières','heading','Only the central tall stem after the live pre is crossed; no separately barred pre is secure.'),
('premières','resolved','premières','heading','The live pre and ières ending surround a retraced m; not préliminaires.'),
('mathscr F|mathcal F','retained',r'\unsure{\mathscr F|\mathcal F}','setF','Hooked cursive F is certain; exact script font is not.'),
('rellation|relation','retained',r'\unsure{rellation|relation}','rellation','Two high strokes follow re but one merges into a.'),
('de|des','resolved','de','de_des','Small e followed by exit line, no independently drawn final s.'),
('déf|def, first equivalence','resolved','déf','def_first','Detached rising mark sits over e before f.'),
(')|} after existe, row a','changed',r'\unsure{\}|)}','a_close','Notched two-part curve favours brace; retraced parenthesis still possible.'),
('deleted Question','retained',r'\deleted{\unsure{Question}}','Question','Initial Q and short inner strokes visible under heavy strike.'),
('c|G in Inf arguments, rows b and c','resolved','c in both','b_argument','Small open c in b, repeated in c; no internal G bar.'),
('(|et ( before barred m','resolved','(','b_prose','Only one large curved stroke; no separate et.'),
('familles','changed',r'\unsure{familles|famille}','b_prose','Final joined flourish leaves presence of s uncertain.'),
('temps|tps','resolved','temps','b_prose','Low e/m run is present between t and descending p.'),
('C|G in F∨C','resolved','C','b_prose','Large open arc lacks the internal/descending stroke of G.'),
('méchisé|mechisé|quoted mechisé','resolved','mechisé','mechise','First e has no separate accent; final e has an acute; no distinct quotation pair.'),
('circled c','resolved','circled c','label_c','Inner angular curve is open to right and has no closed bowl.'),
('deleted G|CG','changed',r'\deleted{\unsure{CG|G}}','deleted_c','Two lower curves favour CG, but heavy retracing leaves G possible.'),
('circled d','retained',r'\textcircled{\unsure{d}}','label_d','Inner stem merges with enclosing circle; d plausible but not secure.')
]
cropdata=json.loads((p/'scan004_crops.json').read_text())
lookup={x['file']:x for x in cropdata}
for d in D:
 if d['crop']:
  d['crop_coordinates']=lookup[d['crop']]['box']
  d['crop_rotation_degrees']=lookup[d['crop']]['rotation_degrees']
res=dict(
reader='R1',scan=4,start_utc=(p/'scan004_start.txt').read_text().strip(),
end_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
model='GPT-6 Astra Pro; inherited configuration; effort setting not exposed',
images_viewed=['H156-01_156-7_scan004.jpg','H156-01_156-7_scan004_a.jpg','H156-01_156-7_scan004_b.jpg']+[x['file'] for x in cropdata],
visual_output_note='The initial batch emission of 17 existing crops was truncated by the output/context limit; all 17 existing crops were then actually inspected in smaller batches. No crop was recreated or re-enlarged.',
coverage=['Manuscript page number 3','Complete opening parenthesis and following paragraph, including barred VI, L, cancellation, mulomb(F), omb(F)','Both underlined heading words and local correction inside premières','Left data brace: script F, ≤ and ≪, both F/G variable pairs, both equivalence arrows and def labels','At 0 label, rightward implication, accompanying prose, complete slanted NB note','Circled a, F∨G / F∪G, all underlined words, quotes, closing punctuation and continuation','First left note: cancelled Question, inserted NB., (F,G), both orders, tjrs, néc., Fig(L)','Second left note: underlined NB and complete tilde intersection identity','Circled b, F∧G / F∩G, Inf superscript ≤, arguments F,c and enclosing parentheses','Row b prose including correctly anchored insertion, barred m, parenthesis nesting, spelling, equals sign in en = temps and F∨C','Third left note including Fig(L) and mechisé','Circled c, low product point, Inf superscript ≪, F,c arguments, quotation and underlining, tiny crossed text beneath','Circled d, empty sign and script-F subscript, final script F, both orders and underlined et, final parentheses'],
notation=[{'sign':'Lowercase operators','reading':r'\mathrm{mulomb}(F), \mathrm{omb}(F)','evidence':'No t in mulomb; lowercase initial m and o.'},{'sign':'Figure set','reading':r'\unsure{\mathscr F|\mathcal F}, repeated as \mathscr F','evidence':'Long hooked script F; definitely distinct from plain F variables and from blackletter.'},{'sign':'Orders','reading':r'\leq and \ll','evidence':'Single angle plus lower bar versus two closely spaced left-facing angles.'},{'sign':'Inf labels','reading':r'\mathrm{Inf}^{\leq}(F,c), \mathrm{Inf}^{\ll}(F,c)','evidence':'Order signs are raised superscripts; argument c is small and open.'},{'sign':'Binary signs','reading':r'\vee,\cup;\ \wedge,\cap;\ \ldotp','evidence':'Angular and rounded pairs distinguished; product dot is low.'},{'sign':'Tildes','reading':r'\widetilde{F\cap G}=\widetilde F\cap\widetilde G','evidence':'One wave spans entire left intersection; right letters each carry their own wave.'},{'sign':'Empty figure','reading':r'\varnothing_{\mathscr F}','evidence':'Slashed empty sign with low script-F index.'},{'sign':'Abbreviations','reading':r'ens.; tjrs; néc.; \overline{\mathrm m}; At','evidence':'Literal short forms preserved; only the notes may expand them.'}],
math_notes=[{'claim':'The page introduces the figure set, inclusion ≤, refinement ≪ and At 0: inclusion implies refinement. It then lists join, intersection, fine intersection, and the empty figure.','status':'Read and transcribed; no proof of the axioms supplied or independently checked.'},{'claim':'The written Inf arguments are F,c although the neighbouring operation names use F,G; the row b prose writes F∨C.','status':'Literal variable mismatch noticed while following formulas and resolved by the strokes. It is not silently repaired to G.'},{'claim':'The raised ou Inf pour ≤ is attached to intersection in row b.','status':'Reading decision from the drawn leader, not from assuming a mathematical identity.'},{'claim':'The page says a ≤ supremum is also a ≪ supremum and warns that the converse need not hold; it distinguishes the two infimum constructions.','status':'Authorial claims recorded, not independently re-proved.'}],
author_qualifications=['(quand il existe[closing mark uncertain])','auquel cas c’est aussi un sup pour ≪','ce n’est pas néc. un sup pour ≤','quand en = temps F∨C existe','(quand elle existe)','Ce sera aussi contenu dans At 4 plus bas'],
unresolved=[dict(original=a,reading=c,confidence='low' if d in ['heading','a_close','deleted_c','L_deleted'] and 'L|' not in a else 'medium') for a,b,c,d,e in A if b in ['retained','changed']],
differences=D,
C_doubt_audit=[dict(original=a,status=b,reading=c,crop=crop(d),crop_coordinates=lookup[crop(d)]['box'],evidence=e) for a,b,c,d,e in A],
missing_from_both=[],
sweep_S='No in-scope S row for scan 004.')
(p/'scan004.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
md='''# R1 scan 004

The whole image and both supplied halves were viewed once. Seventeen targeted crops were created once; the slanted At 0 note was rotated by −36°. The first combined image emission was truncated, so the existing crops were displayed and inspected in smaller batches.

## Principal findings

The opening is “resté muet”; no leading closing guillemet and no “une” before figure appear. The operators are lowercase mulomb(F) and omb(F), with no t in mulomb. Both rules enclosing VI are present.

The live heading reads premières. The live pre at the left is not itself crossed; the local cancelled cluster after it resembles an old l underneath the m. I therefore propose pre + deleted unsure l + mières, at low confidence for the cancelled letter and anchor, instead of adding a separately deleted pré before the entire word.

The inclusion line reads de figures; the first equivalence label has a small accent, déf, and the second is unaccented def. The first relation noun remains rellation|relation. The complete slanted note reads “NB. Ce sera aussi contenu dans At 4 plus bas”.

The raised “ou Inf pour ≤” is attached by its leader to intersection in row b. Both Inf expressions have small open c as their second argument; the prose join is F∨C, with a larger open capital. These are preserved even though the adjacent operation labels use G. The row b prose has a barred m, singular infinie and non vide, and “en = temps”. The final left note reads mechisé with an acute only on the final e and no secure quotation marks.

The operation labels are circled. The c is readable; d remains uncertain. The crossed group below row c favours CG over G, but neither is secure. All twenty C doubt entries have a disposition in the JSON audit.

## Unresolved readings

- GF|CF.
- L|calligraphic L and script-F font choice.
- Deleted ou|de after the lieux-set letter.
- Local deleted l in the heading, including its exact correction anchor.
- rellation|relation.
- Row a closing brace|parenthesis.
- Cancelled Question.
- familles|famille.
- Cancelled CG|G below row c.
- Circled d.

No independent mathematical proof check was performed. The notes distinguish the author’s claims from literal formula checks.
'''
(p/'scan004.md').write_text(md)
print('Saved',len(D),'difference rows and',len(A),'C-doubt audit rows.')
