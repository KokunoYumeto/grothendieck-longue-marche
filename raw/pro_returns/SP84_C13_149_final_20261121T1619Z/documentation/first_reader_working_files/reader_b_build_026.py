from pathlib import Path
import json
root=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads(Path('/tmp/reader_b_026_boxes.json').read_text())
d1=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&]\pi_1(X) \arrow[r,dash,"\pi_1(f')","{\unsure{}}"'] \& \pi_1(U) \arrow[r,"\pi_1(j)"] \& \pi_1(Y)\end{tikzcd}}'''
d2=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&]\pi_1(X) \arrow[r,dash,"\pi_1(f')","{\unsure{}}"'] \& \pi_1(U) \arrow[r,dash,"{\pi_1(\unsure{j'|g'})}","{\unsure{}}"'] \& \pi_1(Y)\end{tikzcd}}'''
page=r'''\scanpage{26}
sous l'hypothèse anabélienne faite, et celle de dominance. (Cette deuxième n'est pas superflue, comme on voit en prenant \deleted{\unsure{pour} $Y$ \inserted{$=G\backslash Z$, où $G$ est} un groupe elliptique et $Z$ un sous-groupe fini $\unsure{+1|\ne 1}$, et pour $f,g$} \inserted{deux applications constantes de $X$ dans $Y$!})

Tout d'abord, on vérifie qu'une variété élémentaire d'Artin se plonge bien \inserted{par un $i:Y\longrightarrow G$} dans une ext. d'une V.A. par un tore -- donc on aura $(ig)=\tau_u(i\circ f)$. \deleted{Donc \unsure{tout}} \inserted{D'autre part,} \deleted{Quitte à remplacer} $f$,\deleted{$g$} étant dominante, il existe une partie ouverte \inserted{non vide} $\unsure{V|W}\subset Y$ contenue dans $\operatorname{Im}f$, et on aura donc $\unsure{V|W}+u\subset Y$. Soit $U\subset X$ un ouvert non vide tel que $f(U)\subset V$ \deleted{$g(U)\subset V$} \deleted{\unsure{donc qui} $\unsure{Q}$} quitte à remplacer $X$ par $U$, on est ramené au cas où $f$\deleted{,$g$} envoie $X$ dans un ouvert $V$ de $Y$ tel que $V+u\subset Y$, et $g\circ i=\tau_u(i\circ f)$. On \deleted{\unsure{sait}} \inserted{voit} que $\pi_1(f)$ est un composé (où $f':X\unsure{-|\longrightarrow}U$ est \deleted{$\unsure{f}$} induit par $f$ et $j:U\unsure{-|\longrightarrow}Y$ est l'inclusion)
% Each empty editorial doubt marker below a dashed shaft concerns only its terminal head: dash first, right arrow alternative. Objects and source labels are not thereby made doubtful.
'''+d1+r'''
tandis que $\pi_1(g)$ est le composé
'''+d2+r'''
% The overwritten j'/g' label is one unresolved glyph; the visible overtracing does not securely distinguish a cancelled g from a replacement j.
où $\deleted{\unsure{j}}$ $j':U\unsure{-|\longrightarrow}Y$ est induit par $\tau_u$.
\margin{25}
'''
(root/'edition/reviews/149_scan026.tex').write_text(page,encoding='utf-8')
R={'scan':26,'reader':'/root/reader_b','lines_read':33,'changes':[],'decisions':[],'inventory':[],'notes':[],'checks':[],'hand':[],'notation':[],'abbreviations':[],'doubts':[],'audit_boxes':[],'diff_coverage':[]}
def change(place,C,H,final,evidence,crop,confidence,against_C,against_H,kind,error_category,marked=False,math=False):
    cid=f'c{len(R["changes"])+1:02d}'
    R['changes'].append(dict(id=cid,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/149_scan026_{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked,mathematical=math))
    return cid
change('Opening parenthesis, adjective after Cette','deuxième','dernière','deuxième','The sequence after d/e contains the u/x run and a dotted i; the following accented -ème is compressed but visible. H’s r/n sequence is not the written one.','c01','high',False,True,'misread word','Words')
change('Opening cancelled example, before Y','pour','(nothing)',r'\unsure{pour}','A p descender precedes the small low run and terminal raised r before Y. The heavy cancellation masks much of o/u, so the word is retained with a limited doubt rather than declared wholly legible.','c02','low',False,True,'omission','Omissions')
change('Nested, subsequently cancelled formula',r'G\backslash Z',r'G\times Z',r'G\backslash Z','Between the curved G and angular Z there is one local down-right oblique. The other line that could suggest a cross continues as the cancellation across the entire inserted phrase. No independent multiplication cross is established.','c24','high',False,True,'misread symbol or index','Symbols and indices',math=True)
change('End of nested cancelled insertion, after second G','est',r'\ill{} Y','est','The final run has a low e/s sequence and a raised terminal t. It does not have the fork and descending leg of the Y in the adjoining text. The low letters are compressed, but remain distinguishable from the cancellation.','c24','medium',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('State of the nested formula and words',r'\deleted{...\inserted{$=G\backslash Z$, où $G$ est}...}',r'\struck{...$Y=G\times Z$, où $G$ ...}',r'\deleted{...\inserted{$=G\backslash Z$, où $G$ est}...}','The formula and où G est occupy a separate raised line above the cancelled baseline and are themselves crossed by a separate stroke. The nesting records both addition and subsequent cancellation; neither the raised line nor its strike is a new baseline word.','c24','high',False,True,'insertion or placement','Insertions put in the wrong place',math=True)
change('Cancelled finite-subgroup expression',r'\unsure{\ne 1|+1}',r'\ne 1',r'\unsure{+1|\ne 1}','One short horizontal bar and a nearly upright crossing stroke before 1 are independent of the long cancellation. A possible second equality bar would coincide with that cancellation. Thus +1 is the ink-first reading, while not-equal 1 remains possible; the numeral 1 itself is clear.','c03','low',True,True,'misread symbol or index','Symbols and indices',math=True)
change('Main paragraph, se plonge bien dans','bien',r'\add{\uncertain{bien sûr}}','bien','The word bien is on the main baseline between plonge and dans. The b stem and low i/e/n run are present; there is no separate s/û/r run. The long curved stroke above it is the leader for par un, not an insertion of bien.','c04','high',False,True,'text not on the page','Text that is not on the page',marked=True)
change('Attachment of par un i:Y→G',r'se plonge \inserted{par un $i:Y\longrightarrow G$} bien dans',r'se plonge \add{par un $i:Y\to G$} \add{bien sûr} dans',r'se plonge bien \inserted{par un $i:Y\longrightarrow G$} dans','The continuous underbrace-like leader beneath the raised phrase has its downward cusp in the gap after bien and before dans. Its two ends span the insertion. No parentheses are added. The small right map head has distinct converging components and is retained as headed.','c04','high',True,True,'insertion or placement','Insertions put in the wrong place',math=True)
change('First translation equality, left parenthesized expression',r'(i\circ g)',r'(i\circ g)',r'(ig)','The dotted i is followed directly by the g loop; no separate circle lies between them. In the same formula the right-hand i-circle-f has a distinct small ring, providing a local contrast. The g descender is long; the audit rectangle extends below this first crop to include its complete tail.','c05','high',True,True,'text not on the page','Text that is not on the page',math=True)
change('First translation equality, tau subscript',r'\tau_a',r'\tau_u',r'\tau_u','The subscript has an open descending valley followed by an upturn and short return. There is no closed oval and right stem of a. This instance was read independently of the later parameters.','c05','high',True,False,'misread symbol or index','Symbols and indices',math=True)
change('Cancelled words after the first translation equality',r'\deleted{Donc \unsure{tout}}',r'\struck{Donc}',r'\deleted{Donc \unsure{tout}}','After Donc a short separate run has surviving t uprights/crosses and a compressed middle beneath the strike. The internal o/u cannot both be isolated securely; tout remains qualified, but the extra run cannot be omitted.','c06','low',False,True,'omission','Struck text')
change('First f,g pair before étant',r'$f$,\deleted{$g$}',r'$f,g$',r'$f$,\deleted{$g$}','The g has separate short oblique cancellation strokes. The preceding f and its comma are outside that local hatching and remain live.','c07','high',False,True,'deletion state','Struck text',math=True)
change('Predicate after first f,g pair','dominante','dominants','dominante','The ending has a tall t followed by a low e-like return. There is no terminal s. The preceding dominant- run is legible despite its compressed baseline.','c07','high',False,True,'misread word','Words')
change('After Im f, et','on aura donc',r'\ill{}','on aura donc','The low on run, separate a/u/r/a sequence and d stem followed by o/n/c are visible. The final c is an open return, not an unreadable block.','c09','high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('First translated-open-set inclusion',r'\unsure{V|W}+a\subset Y',r'V+u\subset Y',r'\unsure{V|W}+u\subset Y','After the overwritten initial capital and the separate plus, the parameter is an open u-like valley and return with no closed a bowl. The capital remains independently doubtful; the subset sign and Y are plain.','c09','high',True,False,'misread symbol or index','Symbols and indices',math=True)
change('After Soit U⊂X un ouvert','non vide',r'\add{\uncertain{dense}}','non vide','The phrase is on the main baseline: a low non run, then v, a separate i dot, tall d and final e return. There is no insertion leader at this phrase and no d/e/n/s/e sequence.','c10','high',False,True,'misread word','Words',marked=True)
change('Punctuation following cancelled g(U)⊂V','(no comma)',',','(no comma)','No detached comma follows the cancelled formula. The visible curl/downstroke to the right belongs to the live V and the overwritten lower V; the cancellation runs through the lower formula. The attachment is not converted into punctuation.','c11','medium',False,True,'text not on the page','Text that is not on the page')
change('Cancelled fragment before quitte à remplacer',r'\deleted{\unsure{donc qui} $\unsure{Q}$}',r'\struck{donc \ill{}}',r'\deleted{\unsure{donc qui} $\unsure{Q}$}','The first d loop survives but the following low letters are struck. A large descending q-like loop, a short u/i run and an i-like tick support qui, without exposing every letter. The last large loop has an oblique tail suggestive of Q, but crossed and retraced strokes prevent a secure letter identification.','c12','low',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True,math=True)
change('After replacing X by U','on est ramené',r'on \ill{} se ramène','on est ramené','The short est has its terminal t upturn. It is followed by the r/a/m/e/n/é run, with a detached accent over the last part. There is no separate se before ramené.','c13','high',False,True,'misread word','Words',marked=True)
change('Second cancelled g, after au cas où f',r'\deleted{,$g$}',r'\struck{et $g$}',r'\deleted{,$g$}','Immediately after live f, a short comma-like mark and the loop/descender of g are crossed together by an oblique stroke. There is no separate e/t pair before g.','c14','high',False,True,'misread word','Struck text',math=True)
change('Later translated-open-set inclusion',r'V+a\subset Y',r'V+u\subset Y',r'V+u\subset Y','The V has a single clear valley here. The parameter after plus has an open u valley with an up-and-down final return, not a closed a bowl. The subset sign, Y and comma are distinct.','c15','high',True,False,'misread symbol or index','Symbols and indices',math=True)
change('Connector before g∘i equality','et','où','et','A short open e-like entry is followed by a compressed terminal t return. No separate o bowl or grave-accented u is present. The small flattened run supports et, though it is less articulated than the longer neighboring words.','c15','medium',False,True,'misread word','Words')
change('Later translation equality, tau subscript',r'g\circ i=\tau_a(i\circ f)',r'g\circ i=\tau_u(i\circ f)',r'g\circ i=\tau_u(i\circ f)','The subscript after tau is a low open valley/hump with no closed oval. Both composition circles are visible in this equality. The left-hand order is literally g then circle then i and is preserved.','c15','high',True,False,'misread symbol or index','Symbols and indices',math=True)
change('Cancelled word under inserted voit',r'\deleted{sait}',r'\struck{\ill{}}',r'\deleted{\unsure{sait}}','A hooked initial s, the i dot and the t stem survive below the raised voit. The a region is largely covered by two heavy cancellation strokes, so sait is a qualified reading rather than a resolved word. Adding that qualification alone is not counted against C.','c16','low',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('Cancelled glyph after f′:X–U est',r'\deleted{\unsure{$f$}}','(nothing)',r'\deleted{$\unsure{f}$}','A tall stem with a low hooked return remains under the local crossing beside est. It is f-like, but the crossing and neighboring tall letters prevent all of its parts being separated. The cancelled glyph is retained with C’s doubt.','c17','low',False,True,'omission','Struck text',math=True)
change('Inline map f′:X–U',r"f':X\longrightarrow U",r"f':X\to U",r"f':X\unsure{-|\longrightarrow}U",'The connector has a plain left end and a short downturned cap at its right end. It does not show a securely separate two-branch arrowhead. The entire expression includes a clear prime after f, colon, X and a U-shaped target.','c17','medium',True,True,'misread symbol or index','Symbols and indices',math=True)
change('Inline map j:U–Y before l’inclusion',r'j:U\longrightarrow Y',r'j:U\to Y',r'j:U\unsure{-|\longrightarrow}Y','The connector’s terminal ink is a tiny near-vertical cap rather than an independently resolved pointed head. Both ends and the full j:U-to-Y expression are included in the audit box. U is the literal domain here, despite the earlier V.','c18','medium',True,True,'misread symbol or index','Symbols and indices',math=True)
change('First chain diagram, first connector','right arrow labelled pi_1(f′)','right arrow labelled pi_1(f′)','headless shaft, with head uncertainty, labelled pi_1(f′)','The first long shaft has a small dark cap at its right end, without a clearly separated two-branch head. The second connector on this same row has a large clear pointed head; that contrast is preserved. All three objects, both labels, the prime and five numeric 1 indices are legible.','c19','medium',True,True,'drawing or diagram','Drawings and diagrams',math=True)
change('Second chain diagram, both connectors','two right arrows','two right arrows','two headless shafts, each with head uncertainty','The first shaft ends in a tiny downturned cap. The second ends in a small upright/bar-like stroke. Neither supplies the distinct two-branch point seen on the first diagram’s second arrow. Both source labels remain separate from the editorial head-doubt markers. The overwritten second label remains j′/g′.','c20','medium',True,True,'drawing or diagram','Drawings and diagrams',math=True)
change('Cancelled glyph after final où',r'\deleted{\unsure{j}}','(nothing)',r'\deleted{\unsure{j}}','A descending stem with a leftward lower hook is crossed near its top. The lower contour is j-like; the upper dot/stroke arrangement is obscured by the crossing. It is retained as a separate cancelled doubtful glyph before the live j′.','c21','low',False,True,'omission','Struck text',math=True)
change('Final map j′:U–Y',r"j':U\longrightarrow Y",r"j':U\to Y",r"j':U\unsure{-|\longrightarrow}Y",'The long shaft has a short curled-down terminal return, without a definite independent pointed head. A separate prime follows live j, then the two colon dots, U and Y. No left mapsto bar is present.','c21','medium',True,True,'misread symbol or index','Symbols and indices',math=True)
change('Final translation parameter',r'\tau_a',r'\tau_u',r'\tau_u','The final subscript is an open low u-like contour with a short returning stroke. No closed a oval is present. The tau roof/stem and following full stop are distinct. This occurrence was inspected separately from the other four parameters.','c22','high',True,False,'misread symbol or index','Symbols and indices',math=True)
change('Lower-left foliation',r'\margin{25}','(omitted; H instead has an editorial explanatory note)',r'\margin{25}','The small thin numeral at the lower-left has a curved 2 and a 5 with a short upper bar and lower bowl. Its scale and thin stroke distinguish it from the principal manuscript hand. H’s explanatory sentence about U/V is editorial prose, not manuscript ink.','c23','high',False,True,'omission','Omissions')
assert len(R['changes'])==33
R['decisions']=[
 {'id':'M1051','decision':'undecided','reading':r'\unsure{V|W}','evidence':'The first capital after raised non vide has multiple overlaid down/up strokes and a dark common lower junction. A V is visible in the dominant outline, but an extra internal rise prevents excluding W or an overwritten W. The complete inclusion and its leader were inspected.','crop':'crops/149_scan026_c08.png','box':boxes['c08'],'confidence':'low'},
 {'id':'M1052','decision':'undecided','reading':r'\unsure{V|W}','evidence':'The later capital before +u is independently overwritten, with a dark valley, an extra upward stroke and oblique retracing. The surrounding +u subset Y is clear but does not settle the capital.','crop':'crops/149_scan026_c09.png','box':boxes['c09'],'confidence':'low'},
 {'id':'M1053','decision':'undecided','reading':r"\unsure{j'|g'}",'evidence':'The lower loop and upper overtracing admit a j-like final outline or a g-like looped letter. A single separate prime is clear. Short hatching crosses the upper part, but a cancelled g and a newly written j cannot securely be separated as two chronological letters. The whole diagram, both shafts and all five indices were read.','crop':'crops/149_scan026_c20.png','box':boxes['c20'],'confidence':'low'}]
def inv(element,kind,pos,words,hand='principal manuscript hand'):
 R['inventory'].append(dict(scan=26,sheet_kind='text',hand=hand,element=element,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
inv('Opening continuation paragraph','text','upper page','sous l’hypothèse anabélienne faite')
inv('Cancelled example, two main rows','deletion','upper paragraph, after en prenant',r'\unsure{pour} Y … un groupe elliptique … sous-groupe fini')
inv('Raised formula inside cancelled example','insertion','above first cancelled example row',r'=G\backslash Z, où G est')
inv('Cancellation of the raised formula','deletion','across the raised nested formula',r'\inserted{$=G\backslash Z$, où $G$ est}')
inv('Replacement example','insertion','between the two cancelled example rows','deux applications constantes de X dans Y!')
inv('Main argument paragraph','text','from Tout d’abord to l’inclusion, central page','Tout d’abord, on vérifie')
inv('Embedding-map addition','insertion','above se plonge bien dans; attaches after bien',r'par un i:Y\longrightarrow G')
inv('Cancelled inference opening','deletion','after first translation equality',r'Donc \unsure{tout}')
inv('Replacement transition','insertion','raised above cancelled inference opening','D’autre part,')
inv('Cancelled change-of-domain phrase','deletion','before first live f','Quitte à remplacer')
inv('First separately cancelled g','deletion','after live f and comma, before étant','g')
inv('Nonempty qualification','insertion','above ouverte, attached before first V/W','non vide')
inv('Cancelled image inclusion','deletion','below live f(U) subset V',r'g(U)\subset V')
inv('Cancelled fragment before quitte','deletion','middle page, left of quitte à remplacer',r'\unsure{donc qui} \unsure{Q}')
inv('Later comma and g cancellation','deletion','after au cas où f',',g')
inv('Cancelled sait','deletion','under raised voit',r'\unsure{sait}')
inv('Replacement voit','insertion','raised over sait','voit')
inv('Cancelled glyph after est','deletion','right edge of f′ map line',r'\unsure{f}')
inv('First chain diagram','diagram','lower page, after l’inclusion',r'\pi_1(X),\pi_1(U),\pi_1(Y); labels \pi_1(f\text{ prime}),\pi_1(j)')
inv('Linking prose between diagrams','text','between the two chain rows',r'tandis que \pi_1(g) est le composé')
inv('Second chain diagram','diagram','below linking prose',r"\pi_1(X),\pi_1(U),\pi_1(Y); labels \pi_1(f'),\pi_1(\unsure{j'|g'})")
inv('Final explanatory line','text','bottom main baseline',r"où … j':U-Y est induit par \tau_u")
inv('Final cancelled j-like glyph','deletion','after final où, before live j′',r'\unsure{j}')
inv('Thin foliation','text','far lower-left margin','25','another or uncertain hand; small thin foliation')
R['notes']=[
 'The leaf continues a discussion under an anabelian and a dominance hypothesis, revises a counterexample, and then develops a translation argument with two fundamental-group chain diagrams. This is a transcription summary, not a verification of the argument.',
 'No title, date, author page number or formula number is written at the head. The only foliation is the small thin 25 at the lower left, kept as \\margin{25} and attributed to another or uncertain hand.',
 'The top example contains a raised insertion that was cancelled again, plus the live replacement about two constant applications. The nesting is preserved. The finite-subgroup sign remains +1/not-equal 1 because the cancellation may coincide with a second horizontal bar.',
 'The leader for par un i:Y→G attaches after bien, before dans. Both witnesses placed it before bien. The word bien is baseline ink and no sûr is present.',
 'The first equality literally has (ig), with no composition circle, whereas its right-hand i-circle-f has a clear ring. The later equality literally uses g-circle-i. Neither expression has been corrected from mathematical expectation.',
 'All five written translation parameters were inspected locally: tau in the first equality, u after the first translated V/W, u after the later clear V, tau in the later equality, and final tau. Each has an open u contour rather than a closed a bowl.',
 'The source uses U in f′’s codomain, in the domain of j and j′, and in both middle diagram objects, although the preceding open subset of Y is called V. The literal U is retained. H’s explanatory note is not source text and is excluded.',
 'Three inline map shafts and three diagram shafts retain a local dash/arrow uncertainty. In the diagrams, a small empty \\unsure{} marker below a dashed shaft is editorial and concerns its head only: dash first, right arrow alternative. It does not make any adjacent object or label doubtful. The first diagram’s second arrow is clearly headed.',
 'The second diagram’s last label preserves one uncertain j′/g′ glyph and its prime. Its upper part is overtraced/hatched, but the ink does not securely distinguish a cancelled g from a new j, so no two-letter replacement chronology is asserted.',
 'The cancelled words tout, donc qui, sait and the separate cancelled f/j-like glyphs remain qualified where the strike hides letters. The top cancelled pour is also qualified; adding that uncertainty alone is not counted as a change against C.',
 'All agreed words, punctuation, alphabets, indices and states were checked on the full sheet and prepared halves. The whole and each prepared half were viewed once. Twenty-four required/open crops were read. c24 was made only to complete the still-open upper nested formula whose tops were clipped in c02; no decided crop was replaced or deleted.',
 'The count of 33 written row units includes separately placed additions, diagram label rows and the small foliation. Audit boxes include the finite-subgroup 1, both prose pi_1 occurrences, all ten diagram indices and foliation 25.',
 'Reader: GPT-6 Astra Pro; effort not exposed; run SP84_C13_149. No OCR, external research, TeX compilation or mathematical proof check was performed.'
]
R['hand']=[
 {'habit':'Open u parameters have a descending valley, upward shoulder and short return, without a closed a bowl.','pages':[26],'consistency':'All five local parameters were individually inspected; this entry does not identify a parameter on another leaf.','misread':'C gives a in all five places; the ink supports u in c05, c09, c15 twice and c22.'},
 {'habit':'Short terminal caps on horizontal shafts can resemble miniature arrowheads.','pages':[26],'consistency':'Three inline maps and three diagram connectors have caps; one diagram arrow has a distinctly larger two-branch head. The small caps remain uncertain.','misread':'Both witnesses regularize all six capped connectors as headed arrows.'},
 {'habit':'Retraced V-like capitals can acquire an internal upward stroke resembling W.','pages':[26],'consistency':'The first two open-set capitals are heavily overwritten; the later V in V+u is clear. No uniform resolution is imposed.','misread':'H’s plain V understates the first two local ambiguities; C’s V/W choices are retained.'},
 {'habit':'Very compressed prose can flatten short e/s/n/t runs into low waves, while dots and tall letters remain diagnostic.','pages':[26],'consistency':'Visible in on aura donc, est ramené, the word et and the baseline non vide; cancellation prevents the same method from resolving tout and sait completely.','misread':'H leaves on aura donc unreadable, substitutes se ramène, and reads baseline non vide as an inserted dense.'},
 {'habit':'A continuous curved insertion leader can be mistaken for punctuation or attached to the wrong word.','pages':[26],'consistency':'The par un leader has its cusp after bien; the non vide leader attaches before the overwritten capital. Each attachment was traced separately.','misread':'Both witnesses put par un before bien, and H also marks bien as added.'}
]
R['notation']=[
 {'written':r'G\backslash Z','rendering':r'G\backslash Z','meaning':'Literal quotient-like expression in the subsequently cancelled insertion; no mathematical correction is supplied.','evidence':'c24 shows one local backslash; the apparent crossing line belongs to the cancellation.'},
 {'written':r'\tau_u','rendering':r'\tau_u','meaning':'Translation notation used in the two equalities and final sentence.','evidence':'c05, c15 and c22 independently show open u-like subscripts.'},
 {'written':r'(ig)=\tau_u(i\circ f)','rendering':r'(ig)=\tau_u(i\circ f)','meaning':'The first equality exactly as written.','evidence':'c05 has no ring between left i and g, but a clear ring in the right expression.'},
 {'written':r'g\circ i=\tau_u(i\circ f)','rendering':r'g\circ i=\tau_u(i\circ f)','meaning':'The later equality exactly as written.','evidence':'c15 shows g, separate circle, i in that order; both right-hand letters and circle are also present.'},
 {'written':r'\pi_1(X),\pi_1(U),\pi_1(Y)','rendering':r'\pi_1(X),\pi_1(U),\pi_1(Y)','meaning':'The three repeated fundamental-group objects in the chain diagrams.','evidence':'c19 and c20 preserve numeric 1 under each pi; the middle letter is U in both rows.'},
 {'written':r"\pi_1(f'),\pi_1(j),\pi_1(\unsure{j'|g'})",'rendering':r"\pi_1(f'),\pi_1(j),\pi_1(\unsure{j'|g'})",'meaning':'Source labels on the chain connectors.','evidence':'c19–c20 show the primes separately; only the last letter remains overtraced and uncertain.'}
]
R['abbreviations']=[
 {'form':'ext.','expansion':'extension','place':'main paragraph, dans une ext. d’une V.A.'},
 {'form':'V.A.','expansion':'variété abélienne','place':'main paragraph, extension by a torus'}
]
def doubt(place,reading,alternatives,confidence,reason):
 R['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
doubt('Top cancelled example before Y',r'\unsure{pour}',['pour; middle o/u obscured'],'low','The p descender and terminal r survive, but the heavy strike masks the middle letters.')
doubt('Cancelled finite-subgroup sign',r'\unsure{+1|\ne 1}',[r'+1',r'\ne 1'],'low','Only one short bar is independent of the cancellation; a second equality bar could coincide with the strike.')
doubt('After cancelled Donc',r'\unsure{tout}',['tout; internal letters masked'],'low','The t strokes survive but the middle o/u cannot both be isolated.')
doubt('First open-set capital',r'\unsure{V|W}',['V','W'],'low','Multiple retraced up/down strokes prevent separating a V from a W-like outline.')
doubt('Second open-set capital',r'\unsure{V|W}',['V','W'],'low','Independent heavy overwriting at the second occurrence; the later clear V does not settle it.')
doubt('Cancelled words before quitte',r'\unsure{donc qui}',['donc qui; crossed letters incompletely visible'],'low','d and the descending q-like loop survive, but the low runs are crossed.')
doubt('Last glyph in the cancelled fragment',r'\unsure{Q}',['Q','unresolved looped capital'],'low','A large loop and diagonal tail are present under superposed cancellation/retracing.')
doubt('Cancelled word under voit',r'\unsure{sait}',['sait; a masked'],'low','Initial s, i dot and t stem survive; the a is not independently plain.')
doubt('Map f′:X–U',r"f':X\unsure{-|\longrightarrow}U",['headless/capped shaft','right arrow'],'medium','The terminal cap does not resolve into a separate two-branch head.')
doubt('Cancelled glyph following est',r'\deleted{$\unsure{f}$}',['f','unresolved tall hooked glyph'],'low','The crossing and neighboring tall letters obscure the proposed f.')
doubt('Map j:U–Y',r'j:U\unsure{-|\longrightarrow}Y',['headless/capped shaft','right arrow'],'medium','A very short upright end is present without a securely independent point.')
doubt('First diagram, first connector','dash with editorial head-doubt marker',['headless/capped shaft','right arrow'],'medium','The small terminal cap contrasts with the explicit head on the second connector.')
doubt('Second diagram, first connector','dash with editorial head-doubt marker',['headless/capped shaft','right arrow'],'medium','The end is a tiny downturned cap rather than a secure arrowhead.')
doubt('Second diagram, second connector','dash with editorial head-doubt marker',['headless/capped shaft','right arrow'],'medium','The endpoint is a small bar-like upright; no separate two-branch point is plain.')
doubt('Second diagram, second label',r"\unsure{j'|g'}",["j'","g'",'possible cancellation/overwriting, chronology unresolved'],'low','The loop and upper hatching do not securely distinguish two successive letters; the separate prime is clear.')
doubt('Final cancelled glyph',r'\deleted{\unsure{j}}',['j','unresolved hooked glyph'],'low','A descending stem and lower hook survive but the upper dot/stroke is crossed.')
doubt('Final map j′:U–Y',r"j':U\unsure{-|\longrightarrow}Y",['headless/capped shaft','right arrow'],'medium','The terminal stroke curls downward, without a distinct separate arrowhead.')
def audit(kind,box,reading):
 b=f'b{len(R["audit_boxes"])+1:02d}'
 R['audit_boxes'].append(dict(box=b,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
audit('prose',boxes['c01'],'deuxième')
audit('deletion',[303,323,1570,586],r'\deleted{\unsure{pour} $Y$ \inserted{$=G\backslash Z$, où $G$ est} un groupe elliptique et $Z$ un sous-groupe fini $\unsure{+1|\ne 1}$, et pour $f,g$} \inserted{deux applications constantes de $X$ dans $Y$!})')
audit('insertion',boxes['c24'],r'\deleted{\inserted{$=G\backslash Z$, où $G$ est}}')
audit('insertion',boxes['c04'],r'bien \inserted{par un $i:Y\longrightarrow G$} dans')
audit('formula',[646,864,1054,1000],r'$(ig)=\tau_u(i\circ f)$.')
audit('insertion',boxes['c06'],r"\deleted{Donc \unsure{tout}} \inserted{D'autre part,}")
audit('deletion',boxes['c07'],r'\deleted{Quitte à remplacer} $f$,\deleted{$g$} étant dominante')
audit('insertion',boxes['c08'],r'\inserted{non vide} $\unsure{V|W}\subset Y$')
audit('formula',boxes['c09'],r'on aura donc $\unsure{V|W}+u\subset Y$.')
audit('prose',boxes['c10'],'un ouvert non vide tel que')
audit('deletion',boxes['c11'],r'$f(U)\subset V$ \deleted{$g(U)\subset V$}')
audit('deletion',boxes['c12'],r'\deleted{\unsure{donc qui} $\unsure{Q}$}')
audit('prose',boxes['c13'],'on est ramené au cas où')
audit('deletion',boxes['c14'],r'$f$\deleted{,$g$} envoie')
audit('formula',boxes['c15'],r'$V+u\subset Y$, et $g\circ i=\tau_u(i\circ f)$.')
audit('insertion',boxes['c16'],r'On \deleted{\unsure{sait}} \inserted{voit}')
audit('formula',boxes['c17'],r"$f':X\unsure{-|\longrightarrow}U$ est \deleted{$\unsure{f}$}")
audit('formula',[830,1900,1430,2035],r"$j:U\unsure{-|\longrightarrow}Y$ est l'inclusion)")
audit('formula',[510,1895,700,2000],r'$\pi_1(f)$')
audit('diagram',[478,1970,1195,2110],d1)
audit('diagram',boxes['c20'],r'tandis que $\pi_1(g)$ est le composé '+d2)
audit('formula',boxes['c21'],r"où $\deleted{\unsure{j}}$ $j':U\unsure{-|\longrightarrow}Y$")
audit('formula',boxes['c22'],r'est induit par $\tau_u$.')
audit('number',boxes['c23'],r'\margin{25}')
coverage={
1:('editorial-only',None,'The scan number 26 is edition metadata, not a written numeral on the sheet.'),
2:('material','c01','deuxième is read from its differing letters.'),
3:('material','c02','The cancelled initial pour is present, with a limited reading doubt.'),
4:('material','c03','The complete nested expression has a backslash, not a multiplication cross.'),
5:('material','c04','The raised ending reads est, not H’s Y/illegible treatment; its nested state is also recorded in c05.'),
6:('material','c06','The finite-subgroup sign remains ambiguous, with +1 first from the independent strokes.'),
7:('material','c07','bien is baseline and no sûr is present; the insertion attachment is separately corrected in c08.'),
8:('macro-only',None,'Two ASCII hyphens versus H’s em dash are alternative TeX representations of the same source dash.'),
9:('material','c10','First tau subscript is u; the separate missing-circle departure against both is c09.'),
10:('material','c11','The extra cancelled run after Donc is preserved as doubtful tout.'),
11:('material','c13','The final letter is e, not s; the separate cancellation of g is c12.'),
12:('reading-agrees',None,'C’s first V/W doubt remains unresolved; H’s first reading V is possible. Decision M1051.'),
13:('material','c14','on aura donc is legible and retained.'),
14:('reading-agrees',None,'The second V/W doubt remains unresolved independently. Decision M1052.'),
15:('material','c15','The following translation parameter is u.'),
16:('material','c16','The source has baseline non vide, not inserted dense.'),
17:('material','c17','No detached comma is established after the cancelled formula.'),
18:('material','c18','The cancelled qui and Q-like glyph remain tentatively readable and are not omitted.'),
19:('material','c19','The phrase is est ramené, not se ramène.'),
20:('material','c20','The struck material begins with a comma, not et.'),
21:('material','c21','The later V parameter is independently u.'),
22:('material','c22','The short connector is et; no où accent or bowl is present.'),
23:('material','c23','The later tau parameter is u; literal g-circle-i order is retained.'),
24:('material','c24','The crossed word is preserved as doubtful sait; H leaves it wholly unreadable.'),
25:('material','c25','The cancelled f-like glyph after est remains with its doubt.'),
26:('macro-only',None,'tikzcd wrapper versus display math is rendering syntax.'),
27:('macro-only',None,'ampersand replacement is rendering syntax.'),
28:('macro-only',None,'The witnesses encode the same headed connector in different syntax; the ink-based head departure against both is separately c28.'),
29:('macro-only',None,'Quoted label delimiter is rendering syntax.'),
30:('macro-only',None,'Both witnesses’ second connector is headed; the ink confirms that head.'),
31:('macro-only',None,'Quoted label delimiter is rendering syntax.'),
32:('macro-only',None,'Diagram/display closing syntax is not manuscript text.'),
33:('macro-only',None,'Second tikzcd wrapper versus display math is rendering syntax.'),
34:('macro-only',None,'ampersand replacement is rendering syntax.'),
35:('macro-only',None,'Connector command syntax differs; the independently observed head uncertainty is c29.'),
36:('macro-only',None,'Quoted first-label delimiter is rendering syntax.'),
37:('macro-only',None,'Connector command syntax differs; the independently observed second-head uncertainty is c29.'),
38:('reading-agrees',None,'C’s j′/g′ choice remains unresolved, with the prime preserved and overtrace state expressly qualified. Decision M1053.'),
39:('macro-only',None,'Quoted second-label delimiter is rendering syntax.'),
40:('macro-only',None,'Second diagram/display closing syntax is not manuscript text.'),
41:('material','c30','The separate cancelled j-like glyph before live j′ is present.'),
42:('material','c32','The final tau parameter is independently u.'),
43:('material','c33','The source foliation 25 is retained. H’s explanatory U/V sentence is editorial and excluded; the literal U/V variation is discussed in notes.')
}
R['diff_coverage']=[dict(row=i,classification=coverage[i][0],change_id=coverage[i][1],reason=coverage[i][2]) for i in range(1,44)]
(root/'edition/reviews/149_scan026.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print({'proposal':str(root/'edition/reviews/149_scan026.tex'),'report':str(root/'edition/reviews/149_scan026.json'),'changes':len(R['changes']),'decisions':len(R['decisions']),'inventory':len(R['inventory']),'doubts':len(R['doubts']),'audit_boxes':len(R['audit_boxes']),'diff_rows':len(R['diff_coverage'])})
