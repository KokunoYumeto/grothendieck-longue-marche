from pathlib import Path
import json,re
BASE=Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACK=Path('/workspace/scratch/481648fc487b/reader_packets/150_scan043')
C=(PACK/'C.tex').read_text()
H=(PACK/'H.tex').read_text()
tex=C
repls=[
 ('équivaut à','équivaut :'),
 (r'd_1\subset d_2\cdots\subset d_p',r'd_1\subset d_2\mathinner{\cdotp\cdotp}\subset d_p'),
 (r'\unsure{dans|de}','dans'),
 (r'\deleted{des filt}',r'\deleted{des \unsure{filt|fil}}'),
 (r'\unsure{p+1|p-1}','p-1'),
 (r'\unsure{-|\longrightarrow}\cdots\unsure{-|\longrightarrow}',r'\unsure{-|\longrightarrow}\mathinner{\cdotp\cdotp}\unsure{-|\longrightarrow}'),
 (r'C_\Sigma(d_1,d_2,\ldots,',r'C_\Sigma(d_1,d_2,-,'),
 (r'morphismes \inserted{\unsure{entre eux}} de',r'morphismes de'),
 ('de transition naturels',r'de \unsure{transition|transitions} naturels'),
 (r'\margin{NB ',r'\margin{\unsure{NB} '),
 (r'd_1,\ldots,d_p',r'd_1,\mathinner{\cdotp\cdotp},d_p'),
 (r'\uline{plus tard}.',r'\uline{plus tard}'),
 (r'\unsure{Ab ovo|ab ovo|standart}',r'\unsure{ab ovo|Ab ovo}'),
 (r'\deleted{plongement}',r'\deleted{\unsure{plongement}}'),
 ('un graphe fermé,',r'un graphe fermé\unsure{;|,}'),
]
for a,b in repls:
 assert a in tex,a
 tex=tex.replace(a,b)
oldframe=tex[tex.index(r'\figure{'):tex.index(r'\end{tikzpicture}}')+len(r'\end{tikzpicture}}')]
frame=r'''% A wavy upper frame with two descending sides encloses the formula; its bottom is open.
\[
 \begin{array}{|c|}\hline
 (24)\quad\Sigma_*,
 \end{array}
\]'''
tex=tex.replace(oldframe,frame)
(BASE/'reader_returns/150_scan043.tex').write_text(tex)

xy={
 'page17':[33,35,106,110], 'opening':[280,43,1648,127],
 'flag_chain':[510,192,1613,297], 'initial_revision':[273,303,1645,477],
 'projection_chain':[490,574,1575,704], 'mapping_cone':[280,725,1659,824],
 'cone_tuple':[275,831,1655,985], 'determine':[875,957,1650,1050],
 'entre_eux':[260,1043,1598,1175], 'NB_margin':[16,192,450,604],
 'later_note':[15,1150,530,1657], 'ab_ovo':[277,1480,1595,1620],
 'context':[284,1616,1639,1814], 'On_live':[345,1854,1300,1977],
 'framed24':[1155,1790,1590,1960], 'relation':[290,1977,1648,2175],
 'final_map':[325,2167,1545,2280], 'circled10':[249,1936,349,2045],
 'folio42':[18,2290,83,2350], 'later_note_full':[15,1030,660,1657],
 'inserted_words':[394,1035,610,1146], 'final_map_full':[320,2122,1548,2290],
 'transition_end':[250,1030,1610,1335]
}
d=dict(scan=43,reader='reader_b',line_count=32,changes=[],marks=[],inventory=[],doubts=[],notes=[],check_events=[],notation=[],abbreviations=[],hand_log=[],second_boxes=[])
def ch(place,c,h,f,crop,evidence,kind='misread word',err='words',cc=False,hh=True,conf='high',marked=False,effect=''):
 d['changes'].append(dict(place=place,C=c,H=h,final=f,evidence=evidence,crop='150_scan043_'+crop+'.jpg',box=xy[crop],confidence=conf,kind=kind,error_kind=err,marked_in_H=marked,change_C=cc,change_H=hh,consequential=effect))
def mark(m,context,decision,reading,crop,evidence,conf='medium'):
 d['marks'].append(dict(mark=m,context=context,decision=decision,reading=reading,evidence=evidence,crop='150_scan043_'+crop+'.jpg',box=xy[crop],confidence=conf))
def inv(e,k,p,w,hand='his hand'):
 d['inventory'].append(dict(element=e,kind=k,position=p,first_words_or_objects=w,sheet_kind='text',hand=hand,transcribed='yes'))
def doubt(p,r,a,conf='medium'):
 d['doubts'].append(dict(place=p,reading=r,alternatives=a,confidence=conf))
def box(e,k,p,r,reason):
 d['second_boxes'].append(dict(box=e,kind=k,coords=xy[p] if isinstance(p,str) else p,reading=r,reason=reason))

ch('opening, conjunction','On considère que','On considère pour','On considère que','opening','The short q-initial group is followed by the low u/e run; it reads que. The long p-o-u-r sequence is not present.',conf='medium')
ch('opening, equivalence verb','équivaut','équivalente','équivaut','opening','The word has the compact equivaut outline and no tall l or extended ending needed by équivalente.',conf='medium')
ch('opening, punctuation after equivalence verb','équivaut à','équivalente :','équivaut :','opening','Two vertically separated dots form a colon after the verb. No à body is present. The resulting source syntax is retained.',kind='other',err='other',cc=True,hh=False)
flag_c=r"d_1\subset d_2\cdots\subset d_p\subset d_{p+1}=d'"+'\n'+r" \qquad(p=\operatorname{long}.d')"
flag_f=flag_c.replace(r'\cdots',r'\mathinner{\cdotp\cdotp}')
ch('first flag chain, continuation and missing inclusion sign',flag_c,r"d_1\subset d_2\subset\cdots\subset d_p\subset d_{p+1}=d'\qquad(p=\mathrm{long.}\,d')",flag_f,'flag_chain','Exactly two short continuation strokes follow d_2, without an additional subset sign. The subset before d_p and the clear upright of the plus in p+1 are visible. The full expression and its length parenthesis are read together.',kind='misread symbol or index',err='symbols and indices',cc=True,effect='Retains two written continuation marks and does not insert H’s extra subset sign.')
ch('initial-segment phrase',r"strict \unsure{dans|de}"+'\n'+r"le \deleted{\unsure{précédent}}\inserted{suivant}.",'strict du suivant.',r"strict dans"+'\n'+r"le \deleted{\unsure{précédent}}\inserted{suivant}.",'initial_revision','The first line ends in d-a-n-s; the next begins le. A struck short word lies beneath the raised suivant replacement. The deleted predecessor candidate remains obscured; it is not silently omitted or made live.',cc=True,conf='medium')
ch('cancelled start before une suite',r'\deleted{des filt}',r'\struck{\ill{}}',r'\deleted{des \unsure{filt|fil}}','initial_revision','The strike crosses a readable des and a prefix with long f, dotted i and tall final strokes. The last t/l distinction is obscured, so a narrow filt/fil doubt is added without counting that certainty change against C.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
proj_c=r"\Sigma_{d'}=\Sigma_{d_{\unsure{p+1|p-1}}}\unsure{-|\longrightarrow}\Sigma_{d_p}"+'\n'+r" \unsure{-|\longrightarrow}\cdots\unsure{-|\longrightarrow}\Sigma_{d_2}"+'\n'+r" \unsure{-|\longrightarrow}\Sigma_{d_1}"
proj_f=proj_c.replace(r'\unsure{p+1|p-1}','p-1').replace(r'\cdots',r'\mathinner{\cdotp\cdotp}')
ch('projection chain, first nested index and continuation marks',proj_c,r"\Sigma_{d'}=\Sigma_{d_{p+1}}\longrightarrow\Sigma_{d_p}\longrightarrow\cdots\longrightarrow\Sigma_{d_2}\longrightarrow\Sigma_{d_1}",proj_f,'projection_chain','The small operation in p−1 is a short stroke without the vertical crossing seen in the first chain’s plus. There are two continuation marks. Each long connector ends in a tiny blob/return; dash versus arrow remains in doubt and is not counted as a new H textual error by itself.',kind='misread symbol or index',err='symbols and indices',cc=True,conf='medium',effect='Keeps p−1 despite the earlier explicit p+1.')
ch('mapping construction, object name','mapping-cône','mapping-cylindre','mapping-cône','mapping_cone','After the hyphen the compact c-ô-n-e and its overhead circumflex are visible. The longer cylindre sequence is absent.')
ch('designation, pronoun',"qu'on désigne","que je désigne","qu'on désigne",'cone_tuple','The short opening has q-u, an apostrophe and o-n before désigne; there is no separate je.')
tuple_c=r"C_\Sigma(d_1,d_2,\ldots,"+'\n'+r" \underset{\substack{\Vert\\d'}}{d_{\unsure{p+1|p-1}}})"
tuple_f=tuple_c.replace(r'\ldots','-').replace(r'\unsure{p+1|p-1}','p-1')
ch('cone tuple and lower identity',tuple_c,r"C_\Sigma(d_1,d_2,\ldots,d_{p+1})$ \add{($d_{p+1}=d'$)}",tuple_f,'cone_tuple','A single long dash is written between commas after d_2. The last index again has p−1, with no plus upright. Two short vertical strokes lie between that object and the lower d-prime; the identity is stacked, not a separate horizontal parenthetical equation.',kind='misread symbol or index',err='symbols and indices',cc=True,conf='medium',effect='Preserves the written p−1 index, one continuation dash, and vertical identity arrangement.')
ch('alternative notation, aussi','ou aussi par','ou par','ou aussi par','cone_tuple','The words at the right of the tuple read ou aussi; par continues on the next main line.',kind='omission',err='omissions',conf='medium')
ch('transition sentence, determining verb','On veut déterminer les','On veut définir les','On veut déterminer les','determine','The tall t and following e-r-m-i-n-e-r sequence are visible in déterminer. The shorter définir is not the ink.')
transition_f=r'morphismes de \unsure{transition|transitions} naturels entre'
transition_c=r'morphismes \inserted{\unsure{entre eux}} de transition naturels entre'
ch('transition sentence, duplicated marginal words',r'morphismes \inserted{\unsure{entre eux}} de',r'\add{\uncertain{morphismes de}}','morphismes de','later_note_full','The two slanted groups above morphismes are cette and tard at the right ends of the first two diagonal-note lines. The tight inserted_words crop and this expanded note contain the same original coordinates. C already transcribes those groups in the marginal note and duplicates them as a separate entre eux insertion. No independent insertion remains at the main sentence.',kind='insertion or placement',err='insertion placement',cc=True,hh=False,effect='Preserves the marginal note once and removes its mistaken duplication in the main sentence.')
ch('transition sentence, main-baseline placement',transition_c,r"\add{\uncertain{morphismes de}} \uncertain{transitions} naturels entre",transition_f,'transition_end','Morphismes and de belong to the ordinary main baseline, not a separate insertion. The slanted nearby words belong to the diagonal note, as recorded separately. The final run of transition/transitions is not securely separable, so both endings remain in a local doubt; adding that doubt alone is not counted as a textual change.',kind='insertion or placement',err='insertion placement',marked=True,conf='medium')
ch('transition sentence, supplied article',"naturels entre\n\\[\n C_{\\Sigma,d,d'}.\n\\]",r"naturels entre \uncertain{les} $C_{\Sigma,d,d'}$",r"naturels entre"+'\n'+r"\["+'\n'+r" C_{\Sigma,d,d'}."+'\n'+r"\]",'transition_end','The main line ends with entre and the next displayed object begins directly with C. No les is written in the intervening blank.',kind='text not on the page',err='text not on page',marked=True)
nb_c=r"\margin{NB \(d\) est l'ens des"+'\n'+'éléments maximaux\n'+r"des \(d_1,\ldots,d_p\)}"
nb_f=nb_c.replace('NB',r'\unsure{NB}').replace(r'\ldots',r'\mathinner{\cdotp\cdotp}')
ch('first diagonal margin, maxima note',nb_c,r"\marginal{\uncertain{$d=$} \ill{} $\lbrace i_0,\ldots\rbrace$ \ill{} $d_1,\ldots,d_p$}",nb_f,'NB_margin','The prose reads d est l’ens des éléments maximaux des, followed by d_1, two continuation strokes, d_p. There are no set braces or i_0. The tiny heading is compressed and remains NB doubtful.',kind='misread word',err='words',cc=True,marked=True,conf='medium')
later_c=r"\margin{On reviendra sur cette"+'\n'+r"\uline{construction} \uline{plus tard}."+'\n'+"Elle n'est pas tellement\n"+r"utile finalement \(\cdots\)}"
later_f=later_c.replace(r'\uline{plus tard}.',r'\uline{plus tard}')
ch('second diagonal margin, postponement note',later_c,r"\marginal{\uncertain{On} \ill{} \uncertain{construction} \ill{} \ill{} \uncertain{finalement} \ldots}",later_f,'later_note_full','The note is a four-line slanted passage with separate underlines under construction and plus tard. The complete words On reviendra sur cette construction plus tard / Elle n’est pas tellement utile finalement and the three ending points are readable. Cette and tard are the same ink C duplicates as an alleged entre eux insertion; the expanded rotated crop establishes their line attachment.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
ch('second diagonal margin, supplied stop after tard',r'\uline{plus tard}.',r"\marginal{\uncertain{On} \ill{} \uncertain{construction} \ill{} \ill{} \uncertain{finalement} \ldots}",r'\uline{plus tard}','later_note_full','There is no independent dot following tard along the diagonal note baseline. The nearby heavy curved mark belongs to adjacent main-line mathematical punctuation. Only the three final points after finalement belong to the note’s visible punctuation.',kind='text not on the page',err='text not on page',cc=True,hh=False)
ch('section 10, Latin phrase',r'\unsure{Ab ovo|ab ovo|standart}',r'\uncertain{\ill{}}',r'\unsure{ab ovo|Ab ovo}','ab_ovo','An initial loop, one tall ascent and a low continuation favor ab ovo; there is no clear late d and final t for standart. Initial case is not settled. Narrowing C’s candidates without settling the mark is not counted as a C textual correction.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
ch('new construction, cancelled and live On',r'\deleted{On}'+'\n'+'On a un espace topologique',r'\struck{\ill{}} \uncertain{Alors} on a un espace topologique',r'\deleted{On}'+'\n'+'On a un espace topologique','On_live','A cancelled O-n stands above a separate live On a un espace topologique. The live opening is not preceded by the letters of Alors.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
ch('framed space, formula number and enclosure',oldframe,r'(24)\qquad \Sigma_{*},',frame,'framed24','The number has a clear 2 and an open upper bowl/right downstroke forming 4; it is read without importing later equation numbers. An upper line and two descending sides surround the formula; no lower border is drawn. The formula is ordinary math in an open-bottom ruled array.',kind='drawing or diagram',err='drawings and diagrams',cc=True,conf='medium')
ch('final map, projection label',r'\Sigma_{**}\xrightarrow{\operatorname{pr}_2=\mathrm{but}}\Sigma_*',r'\add{$\mathrm{pr}_1=\mathrm{but}$} $\Sigma_{**}\to\Sigma_{*}$',r'\Sigma_{**}\xrightarrow{\operatorname{pr}_2=\mathrm{but}}\Sigma_*','final_map_full','The small subscript under pr has a curved top and low return, forming 2 rather than a straight 1. The label is above the shaft of the full map, whose source has two stars and target one.',kind='misread symbol or index',err='symbols and indices',effect='Reads pr_2, the projection explicitly labelled but on this leaf.')
ch('final revision, article and insertion',r'soit une \deleted{plongement}\inserted{immersion}',r'soit un \struck{\uncertain{plongement}} \add{\uncertain{\ill{}}}',r'soit une \deleted{\unsure{plongement}}\inserted{immersion}','final_map_full','A separate final e follows un. Immersion is written above the cancelled word and is readable letter by letter. The old plongement candidate remains partly hidden by its strike; its added doubt does not itself change C’s text.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
ch('bottom-left foliation',r'\margin{42}','[absent]',r'\margin{42}','folio42','A thin grey 4 with an open angle is followed by a curved 2 with horizontal foot. This separate foliation is not substituted for the main handwritten page number 17.',kind='omission',err='omissions')

# All eleven original C marks, with repeated formula marks distinguished by context.
mark(r'\unsure{dans|de}',r'strict \unsure{dans|de}', 'first','dans','initial_revision','The d stem and following a-n-s run are visible at the end of the line; le follows on the next line.','high')
mark(r'\unsure{précédent}',r'le \deleted{\unsure{précédent}}\inserted{suivant}', 'undecided',r'\unsure{précédent}','initial_revision','The long cancellation masks most of the internal letters. The inserted suivant is distinct above it; the deleted candidate is not certified.','low')
mark(r'\unsure{p+1|p-1}',r'\Sigma_{d_{\unsure{p+1|p-1}}}', 'alternative','p-1','projection_chain','The entire projection chain has been read. Its small operation is a short horizontal stroke without the upright present in the earlier flag chain’s p+1.')
mark(r'\unsure{-|\longrightarrow}',r'\Sigma_{d_{\unsure{p+1|p-1}}}\unsure{-|\longrightarrow}\Sigma_{d_p}', 'undecided',r'\unsure{-|\longrightarrow}','projection_chain','The first connector is a long shaft with a tiny terminal blob/return; no sufficiently distinct projecting head settles dash versus arrow. Full neighboring nested indices are preserved.')
mark(r'\unsure{-|\longrightarrow}',r'\unsure{-|\longrightarrow}\cdots', 'undecided',r'\unsure{-|\longrightarrow}','projection_chain','The second connector, before the two continuation strokes, has a small raised termination but no unambiguous full arrowhead.')
mark(r'\unsure{-|\longrightarrow}',r'\cdots\unsure{-|\longrightarrow}\Sigma_{d_2}', 'undecided',r'\unsure{-|\longrightarrow}','projection_chain','The third connector is slightly thickened at its right end; the tiny form remains dash/arrow uncertain when read with the full chain.')
mark(r'\unsure{-|\longrightarrow}',r'\unsure{-|\longrightarrow}\Sigma_{d_1}', 'undecided',r'\unsure{-|\longrightarrow}','projection_chain','The fourth termination is more diamond-like, but its projection remains small. No uniform arrow convention is imposed on the four local strokes.')
mark(r'\unsure{p+1|p-1}',r"\underset{\substack{\Vert\\d'}}{d_{\unsure{p+1|p-1}}}", 'alternative','p-1','cone_tuple','The tuple’s final small operation again lacks a plus upright. Both short vertical identity strokes and the lower d-prime were read with the complete tuple.')
mark(r'\unsure{entre eux}',r'morphismes \inserted{\unsure{entre eux}} de', 'other',later_f,'later_note_full','The same two groups are cette and tard, completing the first two diagonal-note lines. Their original coordinates are identical to those in the tight inserted_words crop. They are preserved once in the full marginal note; no separate entre eux is present above the main sentence.','high')
mark(r'\unsure{Ab ovo|ab ovo|standart}',r'description \unsure{Ab ovo|ab ovo|standart}', 'undecided',r'\unsure{ab ovo|Ab ovo}','ab_ovo','The initial loop and one tall ascent followed by a low run favor ab ovo; no clear late d and final t support standart. Initial case remains uncertain.')
mark(r'\unsure{24|29}',r'(\unsure{24|29})\quad\Sigma_*,', 'first','24','framed24','The second digit has an open upper bowl and right descending stroke, not a closed 9 loop. The whole framed formula is read without consulting subsequent pages.')

inv('N01','text','upper-left corner','17, his own page number')
inv('T01','text','opening two main lines','On considère que cette donnée équivaut : celle d’une')
inv('F01','display','below opening, upper middle','d1⊂d2, two continuation marks, ⊂dp⊂d(p+1)=d′; length parenthesis')
inv('M01','margin note','upper-left diagonal margin','NB doubtful; d est l’ens des éléments maximaux des d1, two marks, dp')
inv('T02','text','next three main prose lines','dont chacun est un segment initial strict dans le; Ceci donne donc une suite de projections')
inv('C01','deletion','after le, below inserted suivant','précédent, doubtful')
inv('I01','insertion','above the crossed predecessor word','suivant')
inv('C02','deletion','before une suite de projections','des filt/fil, final letters doubtful')
inv('F02','display','upper projection chain','Σd′=Σd(p−1), four uncertain connectors, two continuation marks, Σdp,Σd2,Σd1')
inv('T03','text','below projection chain','dont on considère le mapping-cône simultané qu’on désigne par')
inv('F03','display','cone tuple','CΣ(d1,d2,-,d(p−1)); two upright identity strokes with d′ below final entry')
inv('T04','text','following alternative notation and transition statement','ou aussi par CΣ,d,d′. On veut déterminer les morphismes de transition/transitions naturels entre')
inv('F04','display','middle page, before large vertical gap','CΣ,d,d′ followed by a full stop')
inv('M02','margin note','left diagonal margin near the transition paragraph','On reviendra sur cette construction plus tard (no terminal stop); Elle n’est pas tellement utile finalement, followed by three points; the right ends cette/tard extend above morphismes')
inv('T05','text','lower half, section heading and parenthesis','underlined 10.; Reprenons la description ab ovo/Ab ovo; Top parenthesis')
inv('C03','deletion','above new construction paragraph','On')
inv('T06','text','lower paragraph','On a un espace topologique; muni d’une relation d’ordre; ayant un graphe fermé, then semicolon/comma doubtful, et tel que')
inv('M03','margin note','left of the new construction paragraph','circled 10')
inv('F05','display','raised at right of On a un espace topologique','(24) Σ*, comma')
inv('D01','drawing','around (24) Σ*','wavy upper border, descending left and right sides, open bottom; represented by a ruled math array and recorded shape')
inv('F06','display','beside relation d’ordre','Σ**⊂Σ*×Σ*')
inv('F07','display','bottom main line','Σ** maps to Σ*, label pr2=but')
inv('C04','deletion','after soit une on bottom line','plongement, interior doubtful beneath strike')
inv('I03','insertion','above crossed plongement','immersion')
inv('T07','text','bottom line end','— plus')
inv('N02','margin note','bottom-left corner','42','thin separate foliation; attribution uncertain')

doubt('crossed predecessor word',r'\deleted{\unsure{précédent}}','The deleted interior is obscured; inserted suivant does not establish the old letters.','low')
doubt('crossed prefix before une',r'\deleted{des \unsure{filt|fil}}','The final tall stroke may be t or the end of l; no completion to filtrations is supplied.')
doubt('first projection connector',r"\Sigma_{d_{p-1}}\unsure{-|\longrightarrow}\Sigma_{d_p}",'Long shaft with a tiny terminal blob/return.')
doubt('second projection connector',r'\Sigma_{d_p}\unsure{-|\longrightarrow}\mathinner{\cdotp\cdotp}','The right end rises slightly; distinct projecting head not certain.')
doubt('third projection connector',r'\mathinner{\cdotp\cdotp}\unsure{-|\longrightarrow}\Sigma_{d_2}','Small thickened termination remains ambiguous.')
doubt('fourth projection connector',r'\Sigma_{d_2}\unsure{-|\longrightarrow}\Sigma_{d_1}','More diamond-like terminal blob, still too abbreviated to certify the head.')
doubt('transition ending',r'\unsure{transition|transitions}','The final low return does not securely distinguish singular from plural.')
doubt('first marginal heading',r'\unsure{NB}','Compressed, joined small strokes; NB remains tentative.')
doubt('section-10 phrase',r'\unsure{ab ovo|Ab ovo}','The letter sequence favors ab ovo; initial case remains uncertain.')
doubt('punctuation after fermé',r'fermé\unsure{;|,}','The upper point(s) and lower comma-like mark are vertically aligned and may form a semicolon; a comma remains possible. Adding this uncertainty is not counted as a textual correction.')
doubt('last cancelled word',r'\deleted{\unsure{plongement}}','The strike obscures the interior; immersion above it does not settle every old letter.','low')

d['notes']=[
 'The leaf bears his own upper-left page number 17, an underlined section heading 10., a separate circled 10 in the left margin, framed formula number 24, and thin separate bottom-left foliation 42. Attribution of the thin foliation is uncertain.',
 'The page reports an equivalence between the data under discussion and an increasing sequence of flags, then introduces a simultaneous mapping cone and seeks natural transition morphisms. The first marginal note identifies d as the set of maximal elements of the flags; the second says the construction will be revisited and is not so useful after all. These are transcribed claims, not verified mathematical conclusions.',
 'The first flag display clearly has p+1. The subsequent projection chain and cone tuple have a minus-like operation, read p−1. This mismatch is retained. No later-page sequence or expected mathematics is used to force a plus.',
 'The first flag chain, projection chain and first marginal flag list each have two short continuation marks. The cone tuple has a single long dash between commas. The final three points in the postponement note are a different, fully visible three-point sequence. Their counts are not normalized to generic ellipses.',
 'The two short strokes beneath the last cone-tuple entry are upright. The lower d-prime remains stacked beneath that vertical identity and is not converted to H’s separate horizontal equation.',
 'The four projection connectors have long shafts and tiny terminal blobs/returns. They remain dash/arrow uncertain. The final pr2 map has an explicit projecting arrowhead.',
 'The opening has équivaut followed by a colon, despite the smoother syntax that à would give. The lower paragraph has une before the cancelled plongement and inserted immersion. No grammatical repair is made.',
 'The alleged entre eux insertion above morphismes is not independent ink: the two groups are cette and tard at the ends of the first two diagonal-note lines. C transcribes them again in that note. The duplication is removed, both words remain once in the margin, and morphismes de stays on the main baseline. No independent terminal period follows tard. The later punctuation after fermé remains semicolon/comma uncertain.',
 'The source outline around (24) Sigma-star has an upper wavy line with descending sides and an open bottom. An open-bottom ruled array preserves that enclosure while the number and formula remain ordinary transcribed math. The exact slant and rounded hooked ends are recorded in the evidence crop and inventory.',
 'Section 10 restarts a description in the setting M=(Top), introduces a topological space with a closed order relation, and begins a condition involving pr2=but and an immersion. The last line ends at plus; no continuation is supplied.',
 'No mathematical proof check, computation, or independent re-proof was performed; check_events is empty. Observing the index mismatch is a reading finding only.',
 'Whole image and native halves were each viewed once. All 23 saved crops were viewed. Supplemental crops were needed for previously clipped high ends of the slanted note, the alleged interlinear words subsequently reassigned to that same note, the complete final insertion/map, and the full disputed transition clause.'
]
d['notation']=[
 {'form':r'd_{p+1},\quad d_{p-1}','meaning_or_shape':'The first operation has a clear upright crossing its horizontal bar; the two later operations lack that upright and are read as minus. The mismatch is retained.','places':'first flag chain; projection chain; cone tuple'},
 {'form':r'\mathinner{\cdotp\cdotp}','meaning_or_shape':'Two short horizontally extended continuation marks, with the count retained.','places':'flag chain, projection chain, first marginal flag list'},
 {'form':'-','meaning_or_shape':'One long headless dash between commas, used as the written continuation in the tuple.','places':'cone tuple after d2'},
 {'form':r"\underset{\substack{\Vert\\d'}}{d_{p-1}}",'meaning_or_shape':'Two upright identity strokes between the last tuple entry and the lower d-prime.','places':'cone tuple'},
 {'form':r'\operatorname{pr}_2=\mathrm{but}','meaning_or_shape':'Small curved subscript 2 under pr; label sits above the map shaft.','places':'bottom map'},
 {'form':r'\Sigma_*,\ \Sigma_{**}','meaning_or_shape':'One or two small star-like strokes are below and right of Sigma; Sigma’s upper cap is part of its letter, not an added overbar.','places':'framed space, relation graph and final map'}
]
d['abbreviations']=[
 {'form':'NB','expansion':'nota bene; heading remains doubtful'},
 {'form':'ens','expansion':'ensemble'},
 {'form':'long.','expansion':'longueur'},
 {'form':'pr','expansion':'projection'},
 {'form':'filt/fil','expansion':'Unfinished cancelled prefix, possibly for a filtration word; no expansion is inserted.'}
]
d['hand_log']=[
 {'habit':'A small plus must be distinguished from a short curved horizontal minus independently in each nested index.','places':'p+1 in first flag chain; p−1 in projection and cone tuple','consistent':'Clear upright in the first occurrence only.','witness_errors':'Both H later indices are normalized to p+1; C’s p−1 alternatives are preferred on the ink.'},
 {'habit':'Continuation notation varies in actual mark count.','places':'two strokes in each chain and first margin list; one dash in tuple; three points after finalement','consistent':'Counts differ locally and are preserved.','witness_errors':'Both witnesses generally standardize the mathematical continuation signs to three-dot ellipses.'},
 {'habit':'Arrowheads can be extremely abbreviated terminal blobs.','places':'four projection connectors','consistent':'All four remain locally doubtful; the bottom pr2 arrow has an ordinary clear head.','witness_errors':'H prints all projection connectors as certain arrows; this is recorded as uncertainty, not a separate textual-error count.'},
 {'habit':'The figure 4 may have an open, rounded upper body that resembles 9.','places':'formula number 24','consistent':'One such main-hand 4 on this page; the grey foliation is a different thin hand and is not used to force the reading.','witness_errors':'C retains 24/29 doubt; H’s editorial reference to following equation numbers is excluded from the decision.'},
 {'habit':'A final low return can hide the singular/plural ending.','places':'transition/transitions','consistent':'This ending remains unresolved.','witness_errors':'C has singular, H uncertain plural; neither is adopted as certain.'},
 {'habit':'Diagonal marginal lines can extend far into the gap above main-line words.','places':'cette and tard, above morphismes at the ends of the first two postponement-note lines','consistent':'Both groups align with their complete diagonal lines.','witness_errors':'C duplicates the same ink as a separate entre eux insertion. H marks main-baseline morphismes de as inserted.'},
 {'habit':'A large cancellation can obscure letters even where the intended old word is obvious from the replacement.','places':'précédent/suivant, des filt/fil, plongement/immersion','consistent':'Unresolved old letters remain marked; replacements are read separately.','witness_errors':'H leaves some recoverable cancelled ink as illegible; C states filt and plongement with more certainty than the exposed letters support.'}
]

# Mandatory second-pass audit boxes.
box('b01','handwritten number','page17',r'\mspage{17}','Both handwritten digits of his own page number, kept distinct from foliation.')
box('b02','C/H word difference|low-confidence departure','opening',"On considère que cette donnée équivaut : celle d'une",'Full opening line, including que/pour, équivaut/équivalente and the explicit colon.')
box('b03','handwritten number|C/H word difference','flag_chain',r'\['+'\n '+flag_f+'\n'+r'\]','Complete first chain and length parenthesis; all digits 1, 2 and the 1 in p+1; two continuation marks; no added subset after d2.')
initial=r'dont chacun est un segment initial strict dans'+'\n'+r'le \deleted{\unsure{précédent}}\inserted{suivant}.'+'\n'+r'Ceci donne donc \deleted{des \unsure{filt|fil}} une'
box('b04','insertion|struck passage|C/H word difference|low-confidence departure','initial_revision',initial,'Both cancelled spans and raised suivant, read with the full initial-segment sentence and following correction.')
box('b05','margin note|handwritten number|doubt formula|C/H word difference|low-confidence departure','NB_margin',nb_f,'Complete first diagonal note; doubtful heading, all recovered words, full d1/two-marks/dp list including its digit 1.')
box('b06','doubt formula|handwritten number|C/H word difference|low-confidence departure','projection_chain',r'\['+'\n '+proj_f+'\n'+r'\]','Whole chain: p−1, every original connector doubt, two continuation marks, all final nested digits 2 and 1.')
box('b07','C/H word difference','mapping_cone','dont on considère le mapping-cône simultané','The whole line containing the cone/cylinder word difference and its circumflex.')
box('b08','doubt formula|handwritten number|insertion|C/H word difference|low-confidence departure',[275,831,1655,1050],"qu'on désigne par\n"+r'\['+'\n '+tuple_f+'\n'+r'\]'+'\n'+r"ou aussi par \(C_{\Sigma,d,d'}\).",'Complete tuple with single continuation dash, every written 1 and 2, p−1 and the lower vertical identity. Qu’on, ou aussi and the adjacent compact notation on the following line are included in the same expanded box.')
box('b09','C/H word difference','determine','On veut déterminer les','The full determining clause; no substitution of définir.')
box('b10','C/H word difference|low-confidence departure','transition_end',transition_f+'\n'+r'\['+'\n'+r" C_{\Sigma,d,d'}."+'\n'+r'\]','Full main-baseline transition clause, its uncertain singular/plural ending, and the following displayed object; no supplied les. The nearby cette/tard groups belong to the complete margin note in b11, not a separate insertion.')
box('b11','margin note|C/H word difference|low-confidence departure','later_note_full',later_f,'Whole slanted postponement note, both underlines, the complete line endings cette and tard, no supplied period after tard, and exactly three ending points. This also covers the C entre eux doubt, resolved as duplicate transcription of these marginal words.')
box('b12','handwritten number|C/H word difference|low-confidence departure','ab_ovo',r'\uline{10.} Reprenons la description \unsure{ab ovo|Ab ovo}','The section digits 1 and 0, underline and final stop, complete phrase with case doubt.')
context=r'(dans le cas \(\mathcal M=(\mathrm{Top})\), pour fixer les idées'+'\n'+"--- c'était le contexte adopté au début de ces notes)."
box('b13','C/H word difference',[277,1480,1639,1814],context,'Full parenthetical context from dans le through notes; no font-macro or H certainty-only differences counted as textual changes.')
box('b14','struck passage|C/H word difference','On_live',r'\deleted{On}'+'\n'+'On a un espace topologique','The cancelled On and separate live On, without H’s additional Alors.')
box('b15','doubt formula|handwritten number|drawing or diagram|C/H word difference|low-confidence departure','framed24',frame,'Complete formula number 24, Sigma-star and comma with the upper-and-side enclosure; lower edge deliberately open.')
box('b16','margin note|handwritten number','circled10',r'\margin{\textcircled{10}}','Both circled digits, 1 and small closed 0.')
relation=r"muni d'une relation d'ordre"+'\n'+r'\['+'\n'+r' \Sigma_{**}\subset\Sigma_*\times\Sigma_*'+'\n'+r'\]'+'\n'+r'ayant un graphe fermé\unsure{;|,} et tel que'
box('b17','C/H word difference|low-confidence departure','relation',relation,'Full order-relation formula and following closed-graph clause, including the disputed comma/semicolon form.')
final_map=r'\['+'\n'+r' \Sigma_{**}\xrightarrow{\operatorname{pr}_2=\mathrm{but}}\Sigma_*'+'\n'+r'\]'+'\n'+r'soit une \deleted{\unsure{plongement}}\inserted{immersion} --- plus'
box('b18','insertion|struck passage|doubt formula|handwritten number|C/H word difference|low-confidence departure','final_map_full',final_map,'Whole final map and label with handwritten digit 2, article une, complete cancelled word candidate and inserted immersion; the page ends at plus.')
box('b19','margin note|handwritten number','folio42',r'\margin{42}','Both thin foliation digits, 4 and 2, read together.')

def norm(s):return re.sub(r'\s+',' ',s).strip()
issues=[]
for i,r in enumerate(d['changes'],1):
 if norm(r['final']) not in norm(tex):issues.append(f'change {i} final missing: {r["place"]}')
 if r['C']!='[absent]' and norm(r['C']) not in norm(C):issues.append(f'change {i} C excerpt missing: {r["place"]}')
 if r['H']!='[absent]' and norm(r['H']) not in norm(H):issues.append(f'change {i} H excerpt missing: {r["place"]}')
 if not (BASE/'crops'/r['crop']).is_file():issues.append(f'change {i} crop missing')
 if not (r['change_C'] or r['change_H']):issues.append(f'change {i} empty accounting')
for i,r in enumerate(d['marks'],1):
 if norm(r['context']) not in norm(C):issues.append(f'mark {i} context missing')
 if not (BASE/'crops'/r['crop']).is_file():issues.append(f'mark {i} crop missing')
for r in d['second_boxes']:
 if norm(r['reading']) not in norm(tex):issues.append(f'{r["box"]} reading missing')
 a,b,c,e=r['coords']
 if not (0<=a<c<=1682 and 0<=b<e<=2359):issues.append(f'{r["box"]} bounds invalid')
orig=[]
for m in re.finditer(r'\\(?:unsure|illegible)\{',C):
 j=m.end();level=1
 while level:
  if C[j]=='{':level+=1
  elif C[j]=='}':level-=1
  j+=1
 orig.append(C[m.start():j])
if orig!=[r['mark'] for r in d['marks']]:issues.append('Original mark coverage/order mismatch')
level=0
for m in re.finditer(r'(?<!\\)[{}]',tex):
 level+=1 if m.group()=='{' else -1
 if level<0:issues.append('Unmatched early closing brace')
if level:issues.append('Unbalanced TeX braces')
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for r in d['changes']:
 if r['kind'] not in allowed:issues.append('Invalid collation kind '+r['kind'])
(BASE/'reader_returns/150_scan043.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(d['changes']),change_C=sum(r['change_C'] for r in d['changes']),change_H=sum(r['change_H'] for r in d['changes']),marks=len(d['marks']),resolved_marks=sum(r['decision']!='undecided' for r in d['marks']),inventory=len(d['inventory']),doubts=len(d['doubts']),second_boxes=len(d['second_boxes']),crops=len(xy),issues=issues),ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)

