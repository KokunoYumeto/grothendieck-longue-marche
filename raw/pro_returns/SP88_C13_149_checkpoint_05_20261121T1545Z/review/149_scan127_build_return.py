from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan127'
PACKET = ROOT/'packets'/PAGE
OUT = ROOT/'edition/review'
GEOM = json.loads((OUT/f'{PAGE}_crop_geometry.json').read_text())
G = {x['id']: x for x in GEOM}

margin = r'''À nouveau se pose la question si $N_V=\operatorname{Norm}(I_V)$
On voudrait que les germes de sections de $\mathcal E_L^{\bar L}$, sur \deleted{$\mathcal E_K$} \inserted{$\mathcal E_{K_1}^{\bar K}$} soient associés aux pts du normalisé $\tilde{\mathfrak X}_{L/K}$ de $\mathfrak X_{L/K}$ dans $\bar L$ --- qu'elles forment un fibré sur $\unsure{\tilde{\mathfrak X}|\mathfrak X}_{L/K}$, à fibres les $H^1(\deleted{\mathcal E_K}\inserted{\mathcal E_{K_1}}^{\unsure{G|\bar K}},I_V)\ldots.$
Ceci est associé à la formule (pour une telle section $s$ de $\mathcal E_L$ sur $\mathcal E_K$) $\mathcal E_L^{(\mathcal E_K^{\unsure{0|\circ}})}\simeq I_V$ --- lié à la conjecture que pour tt s-groupe ouvert de $N_V^{\unsure{0|\circ}}$, ou simpl\textsuperscript{t} tt s-groupe de $N_V$ dont l'image dans $N_V/I_V$ soit ouvert, on a \deleted{\unsure{Centr|tout}} $(\mathcal E_L^{\bar L})^{\Gamma}=I_V$ (ceci pour tt anneau de valuation $V$ de $L/K$, \unsure{présumé} de corps rés. alg/$K$)
En fait, la question est purement géométrique \ldots'''

opening = r'''\unsure{en|à} cette condition --- en fait la section provient d'une section du groupe de décomposition $N_V$ au dessus de $\mathcal E_K$.'''
item = r'''\noindent b) Soit $U$ un modèle ``élémentaire'' de $L$ sur $K$, anabélien. Alors tte section de $\mathcal E_U^{\bar L}$ sur $\mathcal E_K^{\bar K}$ se relève en une section de $\mathcal E_L^{\bar L}$ sur $\mathcal E_K^{\bar K}$.'''
paragraph = r'''Elle peut donc se décrire en termes d'un anneau de valuation $V$ de $L/K$, et qd $V$ a un centre sur $U$, \unsure{on n'a qu'à} se concen-\newline trer au cas d'un pt $x\in U$ rationnel sur $K$, et de la section définie par $x$. Dans ce cas (posant tjrs $\Gamma=\mathcal E_K^{\bar K}$) on conjecture encore, bien sûr'''
f32 = r'''\[
(32)\qquad (\mathcal E_L^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)
\]'''
qualification = r'''(et on peut y remplacer $\Gamma^{\unsure{0|\circ}}$ par $\Gamma^{\unsure{0|\circ}}\unsure{\ne1)|\ne)|\subset}\deleted{\unsure{\Gamma}}$
--- mais en fait ceci (en vertu de $\operatorname{Centr}_\Gamma(\Gamma^{\unsure{0|\circ}})=(1)$) équivaut à la relation analogue \deleted{$\unsure{\Pi|\pi}_{L\unsure{/|,}K}^{\bar L}$}'''
f33 = r'''\[
(33)\qquad (\unsure{\Pi|\pi}_{L,K}^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)
\]'''
ending = r'''qui se déduit d'ailleurs, par dévissage,'''
candidate = '\\scanpage{127}\n\\mspage{63}\n\\margin{' + margin + '}\n' + '\n\n'.join([opening,item,paragraph,f32,qualification,f33,ending]) + '\n\\margin{126}\n'

changes=[]
def change(place,C,H,final,evidence,crop,confidence='high',vs_C=False,vs_H=True,kind='misread word',category='Words',H_marked=False,consequential=False,**extra):
    changes.append(dict(id=f'p{len(changes)+1:02}',place=place,C=C,H=H,final=final,evidence=evidence,
        crop=G[crop]['file'],bbox=G[crop]['bbox'],confidence=confidence,vs_C=vs_C,vs_H=vs_H,
        kind=kind,error_category=category,H_marked=H_marked,consequential=consequential,**extra))

change('Main line 1, opening continuation',r'\unsure{en|à}','par',r'\unsure{en|à}',
       'A short e-like entry and low joined arch favour en. The reduced left entry overlaps the neighboring margin; à is not excluded. No p descender supporting H par is visible.','p01','medium',H_marked=False,unresolved=True)
change('Main line 3, au dessus','au-dessus','au-dessus','au dessus',
       'There is a blank interval between au and dessus; no hyphen crosses it.','p01',vs_C=True,kind='text not on the page',category='Text that is not on the page')
change('Main line 4, quotation around élémentaire',r"``élémentaire''",'« élémentaire »',r"``élémentaire''",
       'Paired short upper strokes surround the word; these are not angled guillemets.','p02',kind='misread symbol or index',category='Symbols and indices')
change('Main line 5, qualifier of the model','anabélien',r'\uncertain{arbitraire}','anabélien',
       'The internal b and l ascenders, accented é, and terminal ien are visible; the middle does not show the tr sequence of arbitraire.','p02',H_marked=True,consequential=True)
change('Main line 5, after Alors','tte',r'\uncertain{toute}','tte',
       'Two t stems with their crossing strokes are followed directly by the small e loop; there are no ou letters.','p02',kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised',H_marked=True)
change('Main line 6, first group of the section',r'\mathcal E_U^{\bar L}',r'\mathcal{E}_K^{\overline{L}}',r'\mathcal E_U^{\bar L}',
       'The subscript has two curved arms joined at the bottom, unlike the branched K shapes in the adjacent expressions. Both upper L bar and lower U are complete in this view.','p03',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('Main line 8, Elle peut donc','Elle peut donc se décrire',r'Elle peut se \uncertain{décrire}','Elle peut donc se décrire',
       'A separate donc group is written between peut and se; décrire has its d stem and accented entry.','p04',kind='omission',category='Omissions',H_marked=True)
change('Main line 10, condition on V','et qd V a un centre',r'et par V \uncertain{un} centre','et qd V a un centre',
       'The short qd has a descending q and compact d. A separate small oval a follows V. Neither par nor the omission of a follows the strokes.','p04',H_marked=True)
change('Main line 11, before se',r"\unsure{on n'a qu'à}",r'\uncertain{tel} que',r"\unsure{on n'a qu'à}",
       'Low joined on-like strokes are followed by a crowded apostrophe/a/n cluster and a descending q. C is plausible, but the individual apostrophes and short letters remain incompletely separable; H would require a tall l that is not visible.','p05','medium',H_marked=True,unresolved=True)
change('Main lines 11–12, verb across the line break',r'\unsure{concentrer} au',r'\uncertain{concentre} \uncertain{pour} le',r'concen-\newline trer au',
       'concen ends the upper baseline with an actual short hyphen; trer starts the next baseline. au immediately follows, without the extra pour le of H. The letters across the break support concentrer.','p05',vs_C=True,H_marked=True,kind='omission',category='Omissions',scope='C departure is preservation of the written line-end hyphen and break, not a different lexical word.')
change('Main line 12, abbreviation for the point','pt',r'p\supplied{oin}t','pt',
       'Only p and t are written before x; there is no oin and no separate abbreviation stop.','p05',kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised')
change('Main line 15, after posant','tjrs','[absent]','tjrs',
       'A compact t/j/r/s group appears before the Gamma equality; the j descends and the terminal s is separate from Gamma.','p06',kind='omission',category='Omissions')
change('Main line 17, complete formula (32)',r'(32)\quad(\mathcal E_L^{\bar L})^{\Gamma^0}=(1)',r'(32)\quad(\mathcal E_L^{\bar L})^{\Gamma^{\circ}}=(1)',r'(32)\quad(\mathcal E_L^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)',
       'The full formula, its bars, both parentheses and digits were read. The raised mark after Gamma is a small closed oval, which does not distinguish 0 from a circle.','p06','medium',vs_H=False,kind='misread symbol or index',category='Symbols and indices',unresolved=True,scope='Collation conflict only; no settled correction to either witness.')
change('Main line 18, replacement of Gamma',r"(et on peut y remplacer $\Gamma^0$ par $\Gamma^0\unsure{\ne1)|\ne)|\subset}\deleted{\unsure{\Gamma}}$",r"(et on \uncertain{peut} y remplacer $\Gamma^{\circ}$ par $\Gamma^{\circ}_{\ill{}}$",r"(et on peut y remplacer $\Gamma^{\unsure{0|\circ}}$ par $\Gamma^{\unsure{0|\circ}}\unsure{\ne1)|\ne)|\subset}\deleted{\unsure{\Gamma}}$",
       'peut and remplacer are readable. Two raised small round marks and the two Gamma bodies are present. After the second are a slanted/angular relation-like cluster, two low short strokes and a long curved/upright stroke, followed by a heavily crossed Gamma-like form. Their segmentation and the status of the long stroke remain unresolved; no balanced parenthesis is supplied.','p13','low',H_marked=True,kind='readable ink left as \\ill{}',category='Readable ink left as illegible',unresolved=True,context_crop=G['p07']['file'])
change('Main lines 19–20, reason preceding the centralizer formula','en vertu de',r'on \uncertain{voit} ou','en vertu de',
       'The sequence begins en, has a v entry and the r/t/u continuation of vertu, then a separate de. The full centralizer expression is in the same inspected context.','p07',H_marked=True)
change('Main line 20, complete centralizer formula',r'\operatorname{Centr}_\Gamma(\Gamma^0)=(1)',r'\operatorname{Centr}_\Gamma(\Gamma^{\circ})=(1)',r'\operatorname{Centr}_\Gamma(\Gamma^{\unsure{0|\circ}})=(1)',
       'Centr, its Gamma index, the inner Gamma, equality and (1) are visible. The raised closed oval is subject to the same unresolved 0/circle distinction as in (32).','p07','medium',vs_H=False,kind='misread symbol or index',category='Symbols and indices',unresolved=True,scope='No settled C correction.')
change('Main line 21, cancelled relative-group expression',r'\deleted{$\pi_{L\unsure{/|,}K}^{\bar L}$}',r'\struck{$\pi_{L/K}^{\overline L}$}',r'\deleted{$\unsure{\Pi|\pi}_{L\unsure{/|,}K}^{\bar L}$}',
       'The expression is crossed. Its cap and two posts favour a capital Pi form, but the tiny curved foot and small height do not settle case. The subscript separator is obscured by the strike; both slash and comma remain possible. The barred L exponent is present.','p07','low',vs_H=False,kind='misread symbol or index',category='Symbols and indices',unresolved=True,scope='Existing cancellation uncertainty retained; additional case doubt is not a settled correction.')
change('Main line 22, complete formula (33)',r'(\pi_{L\unsure{/|,}K}^{\bar L})^{\Gamma^0}=(1)',r'(\pi_{L/K}^{\bar L})^{\Gamma^{\circ}}=(1)',r'(\unsure{\Pi|\pi}_{L,K}^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)',
       'Between L and K is a short curved descending tick, unlike the long straight slash in the body L/K. The two long near-straight Pi legs and cap favour capital case without settling it. The round Gamma superscript remains 0/circle ambiguous. All indices, overbar, parentheses and both handwritten labels were read.','p08','medium',vs_C=True,kind='misread symbol or index',category='Symbols and indices',scope='The settled change is the comma; case and round-superscript changes are uncertainty only.')
change('Lower-left foliation','126','[absent]','126',
       'Thin 1, 2 and 6 are separately visible below the oblique note, in a different hand from the thick authorial writing.','p08',kind='omission',category='Omissions')
change('Marginal lines 1–3, opening question',r'À nouveau se pose la question si $N_V=\operatorname{Norm}(I_V)$.',r'\uncertain{nouveaux pour la question} $N_V=\operatorname{Norm}(\overline I_V)$',r'À nouveau se pose la question si $N_V=\operatorname{Norm}(I_V)$',
       'À has an accent; nouveau, se pose la question and si are distributed over three oblique baselines. I has a top and bottom cap, without a separate overbar. The end of the formula lies at the actual scan edge and no separately readable full stop follows it. p14 repairs p09 clipping; it supplies no text beyond the page edge.','p14','medium',vs_C=True,H_marked=True,kind='misread word',category='Words',context_crop=G['p09']['file'])
change('Marginal lines 4–6 and first correction',r'On voudrait que les germes de sections de $\mathcal E_L^{\bar L}$ sur \deleted{$\mathcal E_K$} \inserted{$\mathcal E_{K_1}^{\bar K}$}',r'\uncertain{on voudrait que} $\mathcal E_{K_1}^{\bar K}$ \ill{} germe de \uncertain{sections} de $\mathcal E_L^{\bar L}$',r'On voudrait que les germes de sections de $\mathcal E_L^{\bar L}$, sur \deleted{$\mathcal E_K$} \inserted{$\mathcal E_{K_1}^{\bar K}$}',
       'les germes is plural in the ink. A detached comma follows the barred-L expression before sur. The old E_K is raised beside the preceding writing; its strike crosses K. The replacement full E has K with a small 1 below, and barred K above. Its curved attachment and relative position were traced separately from its reading.','p14','medium',vs_C=True,H_marked=True,kind='insertion or placement',category='Insertions put in the wrong place')
change('Marginal lines 7–9, normalized space',r'soient associés \unsure{aux} pts du normalisé $\unsure{\tilde{\mathfrak X}|\tilde{\mathcal Z}}_{L/K}$ de $\unsure{\mathfrak X|\mathcal Z}_{L/K}$ dans $\bar L$',r'\uncertain{associés aux} \ill{} \uncertain{dans} $\bar L$ \ill{} de $\mathfrak X_{L/K}$',r'soient associés aux pts du normalisé $\tilde{\mathfrak X}_{L/K}$ de $\mathfrak X_{L/K}$ dans $\bar L$',
       'soient, pts du normalisé and de/dans are visible across the oblique rows. aux is retraced, with an a oval, u trough and crossing final x. The two space letters have intersecting arms and lobed X bodies, not the alternate Z outline; the first has a separate upper wave. The complete L/K indices and barred L were read.','p14','medium',H_marked=True,kind='readable ink left as \\ill{}',category='Readable ink left as illegible')
change('Marginal lines 10–12 and second correction',r"--- qu'elles forment un fibré sur $\unsure{\tilde{\mathfrak X}|\tilde{\mathcal Z}}_{L/K}$, à fibres les $H^1(\deleted{\mathcal E_K}\inserted{\mathcal E_{K_1}}^{\unsure{G|\bar K}},I_V)\ldots$",r'\uncertain{formant un} \ill{} \uncertain{de} \ill{} $I_V$ \ill{} $H^1(\mathcal E_K,\ldots)$',r"--- qu'elles forment un fibré sur $\unsure{\tilde{\mathfrak X}|\mathfrak X}_{L/K}$, à fibres les $H^1(\deleted{\mathcal E_K}\inserted{\mathcal E_{K_1}}^{\unsure{G|\bar K}},I_V)\ldots.$",
       'qu’elles forment un fibré sur and à fibres les are readable. The third X alphabet is clear, but its upper wave meets the descender of f in forment. In H¹ the old index is crossed and a complete E_K1 is written below; the superscript has a G-like internal/lower return but is not fully secure. Four distinct dark dots follow the close. Full formula context is p10; p15 is a focused layer view and does not contain its right endpoint.','p10','medium',vs_C=True,H_marked=True,kind='readable ink left as \\ill{}',category='Readable ink left as illegible',detail_crop=G['p15']['file'],scope='Settled C punctuation change: four dots. Changed uncertainty alternatives do not count as a settled alphabet correction.')
change('Marginal lines 13–16, section and invariant-group formula',r'Ceci est associé à la formule (pour une telle \uline{section} \unsure{$s$} de $\mathcal E_L$ sur $\mathcal E_K$) $\mathcal E_L^{(\mathcal E_K^0)}\simeq I_V$ --- lié',r'\uncertain{la} \ill{} \uncertain{sections} \ill{} \uncertain{associée} \ill{} $\mathcal E_K$ \ill{}',r'Ceci est associé à la formule (pour une telle section $s$ de $\mathcal E_L$ sur $\mathcal E_K$) $\mathcal E_L^{(\mathcal E_K^{\unsure{0|\circ}})}\simeq I_V$ --- lié',
       'Ceci est associé à la formule, pour une telle, de and sur are readable. A standalone curled s follows section. The short apparent underline under the end of section is continuous with the vertical I stroke below and is its upper cap, not independent emphasis. The lower relation has a wavy upper and straight lower stroke. Its full context is p10/p11; p15 focuses the attachment.','p10','medium',vs_C=True,H_marked=True,kind='drawing or diagram',category='Drawings and diagrams',detail_crop=G['p15']['file'])
change('Marginal lines 17–21, subgroup clauses',r"à la conjecture que pour $\forall$ \unsure{s-groupe} ouvert de $N_V^0$, ou \unsure{simplt} $\forall$ \unsure{s-groupe} de $N_V$ dont l'image dans $N_V/I_V$ soit \unsure{ouvert}, on a",r'[absent; H offers only an editorial synopsis of this block]',r"à la conjecture que pour tt s-groupe ouvert de $N_V^{\unsure{0|\circ}}$, ou simpl\textsuperscript{t} tt s-groupe de $N_V$ dont l'image dans $N_V/I_V$ soit ouvert, on a",
       'The two quantifier-shaped abbreviations have separate, almost parallel t stems, with a cross/curled foot on the second, rather than converging arms of ∀. Each s-groupe has one small s, a distinct hyphen, g loop/descender and groupe continuation. The terminal t of simplt is raised. ouvert ends at t before the comma; no e is supplied. The second quantifier is complete in p11; p16 details the first and the raised t.','p11','medium',vs_C=True,kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised',detail_crop=G['p16']['file'],scope='Written tt and raised t are literal forms; no change of mathematical quantification is asserted.')
change('Marginal line 22, cancelled word and invariant formula',r'\deleted{\unsure{Centr|tout}} $(\mathcal E_L^{\bar L})^{\unsure{\Gamma|\bar\Gamma}}=I_V$ (ceci pour',r'[absent from H transcription; its editorial note speculates about a Gamma-circle expression]',r'\deleted{\unsure{Centr|tout}} $(\mathcal E_L^{\bar L})^{\Gamma}=I_V$ (ceci pour',
       'A long horizontal strike crosses the preceding word. Its initial open loop favours C but the interior remains obscured. The following Gamma has a single cap and descending upright, with no separate bar or circle. The E, two L positions, upper L bar, equality and I_V are all present.','p12','medium',kind='readable ink left as \\ill{}',category='Readable ink left as illegible',detail_crop=G['p17']['file'],scope='H editorial synopsis is not copied into the transcription.')
change('Marginal lines 23–26, valuation qualification and ending',r'$\forall$ anneau de valuation $V$ de $L/K$, \unsure{présumé} de corps rés. alg./$K$). En fait, la question est purement géométrique !\ldots',r'[absent]',r'tt anneau de valuation $V$ de $L/K$, \unsure{présumé} de corps rés. alg/$K$) En fait, la question est purement géométrique \ldots',
       'The third short quantifier repeats the two separate t stems. présumé has a clear p descender and a compatible low continuation, but not every interior stroke is secure. rés. has a stop; no distinct stop is seen between alg and its following slash, or beyond the closing parenthesis. The long apparent exclamation before the three final dots is connected to q in question on the previous baseline. The three dots themselves are separate. p12 contains the complete right endpoints; p17 is a focused left/central detail.','p12','medium',vs_C=True,kind='text not on the page',category='Text that is not on the page',detail_crop=G['p17']['file'])

decisions=[]
def decision(n,status,reading,evidence,crop,confidence='medium',**extra):
    decisions.append(dict(id=f'M{n:04}',cote='149',scan='127',decision=status,reading=reading,evidence=evidence,crop=G[crop]['file'],bbox=G[crop]['bbox'],confidence=confidence,**extra))
decision(142,'first','aux','Retraced a oval, following u trough and crossing terminal x are visible; no strike covers the whole word.','p14')
decision(143,'first',r'\tilde{\mathfrak X}','The first normalized-space glyph has crossed/lobed X arms and a separately visible upper wave; its full L/K index is present.','p14','high')
decision(144,'first',r'\mathfrak X','The base-space glyph has two crossing upper arms and a lower paired/lobed return, unlike Z; no upper tilde is present.','p14','high')
decision(145,'undecided',r'\unsure{\tilde{\mathfrak X}|\mathfrak X}','X alphabet is supported, but the apparent upper wave intersects the f descender of forment above; a separate tilde cannot be securely isolated.','p14')
decision(146,'undecided',r'\unsure{G|\bar K}','The raised form has a G-like curved upper entry and internal/lower return. The compressed strokes and correction layers leave barred K possible. The old index is crossed and a complete replacement E_K1 is below.','p15',context_crop=G['p10']['file'],context_bbox=G['p10']['bbox'])
decision(147,'first',r'$s$','After section is a separate small curled s-shaped symbol. Its lower return is distinct from de. The nearby horizontal stroke is the I_V cap in the next line, not an underline.','p15',context_crop=G['p10']['file'])
decision(148,'first','s-groupe','A small initial s is followed by a distinct hyphen, then the loop and descender of g and the groupe continuation.','p11')
decision(149,'first',r'simpl\textsuperscript{t}','The short form reads simpl with a separate raised, crossed terminal t; no expanded letters are inserted.','p16')
decision(150,'first','s-groupe','The second occurrence repeats the single s and hyphen before the looped g and compressed groupe continuation.','p11')
decision(151,'first','ouvert','The final word has low ou/v/e/r joins and a taller crossed terminal t; the following comma is separate and no e is added.','p11')
decision(152,'first',r'\Gamma','One short upper cap and one descending upright make Gamma. There is no second separate bar above it. The entire formula is read in p12.','p12','high')
decision(153,'undecided',r'\unsure{présumé}','The p descender and low continuation fit présumé, but the small medial letters cannot all be separated confidently.','p17',context_crop=G['p12']['file'])
decision(154,'undecided',r'\unsure{en|à}','The entry and low arch favour en; margin overlap and reduction leave à open. H par lacks the needed descending p.','p01')
decision(155,'undecided',r"\unsure{on n'a qu'à}",'Low joined groups and a q descender support C, but the apostrophes and several tiny letters remain compressed and incompletely distinguishable.','p05')
decision(156,'first',r'concen-\newline trer','The upper line ends concen followed by a genuine short line-end hyphen; the next starts trer, giving concentrer without guessing missing letters.','p05','high')
decision(157,'undecided',r'\unsure{\ne1)|\ne)|\subset}','The angular/oblique group, low pair of short strokes and long upright/curved stroke overlap in a way that does not settle relation, numeral or parenthesis segmentation. The crossed Gamma-like endpoint remains separate and doubtful.','p13','low',context_crop=G['p07']['file'])
decision(158,'alternative',',','The live (33) separator is a short curved downward tick. It differs from the tall straight slash in the body L/K. The entire live expression was inspected; this decision does not settle the cancelled separator above.','p08')
decision(159,'first','se','The final word has a retraced s-like sweep and e return. No separate readable former letters are asserted beneath the retracing.','p08')

unlisted=[
 dict(place='Cancelled marginal word before the final invariant formula',C=r'\deleted{\unsure{Centr|tout}}',decision='undecided',reading=r'\deleted{\unsure{Centr|tout}}',evidence='Open initial C-like loop and a possible tall terminal stem survive; the central strike prevents resolution of the interior.',crop=G['p12']['file'],bbox=G['p12']['bbox'],confidence='low'),
 dict(place='Cancelled Gamma-like endpoint after the main qualification',C=r'\deleted{\unsure{\Gamma}}',decision='undecided',reading=r'\deleted{\unsure{\Gamma}}',evidence='A cap/upright-like remnant is crossed by several dark strokes; the exact underlying symbol is not fully readable.',crop=G['p13']['file'],bbox=G['p13']['bbox'],confidence='low'),
 dict(place='Subscript separator in cancelled relative-group expression',C=r'\deleted{$\pi_{L\unsure{/|,}K}^{\bar L}$}',decision='undecided',reading=r'\deleted{$\unsure{\Pi|\pi}_{L\unsure{/|,}K}^{\bar L}$}',evidence='The strike obscures the short separator; the live comma in (33) cannot decide this cancelled occurrence.',crop=G['p07']['file'],bbox=G['p07']['bbox'],confidence='low')
]

main_lines=[
 r'\unsure{en|à} cette condition --- en fait la section',
 r"provient d'une section du groupe de",
 r'décomposition $N_V$ au dessus de $\mathcal E_K$.',
 r'\noindent b) Soit $U$ un modèle ``élémentaire\'\' de',
 r'$L$ sur $K$, anabélien. Alors tte',
 r'section de $\mathcal E_U^{\bar L}$ sur $\mathcal E_K^{\bar K}$ se relève en',
 r'une section de $\mathcal E_L^{\bar L}$ sur $\mathcal E_K^{\bar K}$.',
 r'Elle peut donc se décrire en',
 r"termes d'un anneau de valuation $V$",
 r'de $L/K$, et qd $V$ a un centre',
 r"sur $U$, \unsure{on n'a qu'à} se concen-",
 r"trer au cas d'un pt $x\in U$",
 r'rationnel sur $K$, et de la section',
 r'définie par $x$. Dans ce cas (posant',
 r'tjrs $\Gamma=\mathcal E_K^{\bar K}$) on conjecture encore,',
 r'bien sûr',
 r'$(32)\quad(\mathcal E_L^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)$',
 r'(et on peut y remplacer $\Gamma^{\unsure{0|\circ}}$ par $\Gamma^{\unsure{0|\circ}}\unsure{\ne1)|\ne)|\subset}\deleted{\unsure{\Gamma}}$',
 r'--- mais en fait ceci (en vertu',
 r'de $\operatorname{Centr}_\Gamma(\Gamma^{\unsure{0|\circ}})=(1)$) équivaut à la',
 r'relation analogue \deleted{$\unsure{\Pi|\pi}_{L\unsure{/|,}K}^{\bar L}$}',
 r'$(33)\quad(\unsure{\Pi|\pi}_{L,K}^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)$',
 r"qui se déduit d'ailleurs, par dévissage,"
]
main_lines[3] = r"\noindent b) Soit $U$ un modèle ``élémentaire'' de"
margin_lines=[
 r'À nouveau', r'se pose la question',r'si $N_V=\operatorname{Norm}(I_V)$',
 r'On voudrait que',r'les germes de',r'sections de $\mathcal E_L^{\bar L}$, sur',
 r'soient associés aux',r'pts du normalisé',r'$\tilde{\mathfrak X}_{L/K}$ de $\mathfrak X_{L/K}$ dans $\bar L$',
 r"--- qu'elles forment un",r'fibré sur $\unsure{\tilde{\mathfrak X}|\mathfrak X}_{L/K}$, à fibres',
 r'les $H^1(\deleted{\mathcal E_K}\inserted{\mathcal E_{K_1}}^{\unsure{G|\bar K}},I_V)\ldots.$',
 r'Ceci est associé à la',r'formule (pour une',r'telle section $s$ de $\mathcal E_L$ sur $\mathcal E_K$)',
 r'$\mathcal E_L^{(\mathcal E_K^{\unsure{0|\circ}})}\simeq I_V$ --- lié',
 r'à la conjecture que',r'pour tt s-groupe ouvert',r'de $N_V^{\unsure{0|\circ}}$, ou simpl\textsuperscript{t} tt',
 r"s-groupe de $N_V$ dont l'image",r'dans $N_V/I_V$ soit ouvert, on a',
 r'\deleted{\unsure{Centr|tout}} $(\mathcal E_L^{\bar L})^{\Gamma}=I_V$ (ceci pour',
 r'tt anneau de valuation $V$ de $L/K$,',r'\unsure{présumé} de corps rés. alg/$K$)',
 r'En fait, la question est purement',r'géométrique \ldots'
]

inventory=[]
def element(kind,position,text,hand='his hand',**extra):
    inventory.append(dict(sheet_kind='text',hand=hand,element=f'e{len(inventory)+1:02}',kind=kind,position=position,first_words_or_objects=text,transcribed='yes',**extra))
element('text','Top center, standalone author number','63')
element('text','Main lines 1–3','en/à cette condition; N_V; au dessus de E_K')
element('text','Main lines 4–7','b) Soit U un modèle; anabélien; tte; E_U and the section expressions')
element('text','Main lines 8–16','Elle peut donc; qd; on n’a qu’à; concen-/trer; pt; tjrs; Gamma definition')
element('display','Main line 17','(32), (E_L^barL)^(Gamma^(0|circle))=(1)')
element('text','Main lines 18–21','Gamma replacement; en vertu de; Centr formula; relation analogue')
element('deletion','End of main line 18','Crossed Gamma-like endpoint',reading=r'\deleted{\unsure{\Gamma}}')
element('deletion','Main line 21','Crossed relative-group expression',reading=r'\deleted{$\unsure{\Pi|\pi}_{L\unsure{/|,}K}^{\bar L}$}')
element('display','Main line 22','(33), live comma-indexed relative group fixed expression =(1)')
element('text','Main line 23','qui se déduit d’ailleurs, par dévissage,')
element('margin note','Oblique left margin, 26 textual/formula baselines','À nouveau se pose la question; complete note through géométrique and three dots')
element('deletion','Upper margin beside sections/sur, raised old expression','E_K; the visible strike crosses its K index',reading=r'\deleted{$\mathcal E_K$}')
element('insertion','Upper margin, lowered replacement beside sur','E_{K1}^{barK}',reading=r'\inserted{$\mathcal E_{K_1}^{\bar K}$}',attachment='Replacement of the raised old E_K; connected by the curved correction/attachment. The full new E is written separately.')
element('deletion','Marginal H¹ expression, old group','E_K; dense crossing concentrated on K',reading=r'\deleted{\mathcal E_K}')
element('insertion','Below the old H¹ group baseline','Full E_{K1}',reading=r'\inserted{\mathcal E_{K_1}}',attachment='Replacement lies below the old group, next to the retained raised G/barK form. The exponent attachment is represented as in C, with uncertainty retained.')
element('deletion','Before final marginal invariant formula','Centr/tout',reading=r'\deleted{\unsure{Centr|tout}}')
element('text','Lower-left thin foliation','126','thin foliation hand')

doubts=[
 dict(place='Main line 1',reading='en',alternatives='à',confidence='medium',crop=G['p01']['file']),
 dict(place='Main line 11',reading="on n'a qu'à",alternatives='Unresolved compression of the written phrase; no grammatical expansion supplied.',confidence='medium',crop=G['p05']['file']),
 dict(place='Third marginal space glyph after fibré sur',reading=r'\tilde{\mathfrak X}',alternatives=r'\mathfrak X; the apparent wave meets the preceding f descender.',confidence='medium',crop=G['p14']['file']),
 dict(place='Marginal H¹ exponent',reading='G',alternatives=r'\bar K',confidence='medium',crop=G['p15']['file'],context_crop=G['p10']['file']),
 dict(place='Small round superscripts, seven local occurrences',reading='0',alternatives=r'\circ',confidence='medium',occurrences=['marginal E_K in the invariant exponent','marginal N_V','main formula (32)','first Gamma in replacement phrase','second Gamma in replacement phrase','Gamma inside Centr','main formula (33)'],crops=[G[x]['file'] for x in ['p06','p07','p08','p10','p11']]),
 dict(place='Main Gamma replacement relation',reading=r'\ne1)',alternatives=r'\ne) | \subset; exact stroke segmentation unresolved.',confidence='low',crop=G['p13']['file']),
 dict(place='Cancelled Gamma-like endpoint',reading=r'\Gamma',alternatives='Underlying cap/upright form not securely separated from the strike.',confidence='low',crop=G['p13']['file']),
 dict(place='Pi case in the cancelled and live relative expressions',reading=r'\Pi',alternatives=r'\pi',confidence='medium',crops=[G['p07']['file'],G['p08']['file']]),
 dict(place='Cancelled relative expression separator',reading='/',alternatives=',',confidence='low',crop=G['p07']['file']),
 dict(place='Cancelled marginal word',reading='Centr',alternatives='tout; interior obscured by the horizontal strike.',confidence='low',crop=G['p12']['file']),
 dict(place='Marginal valuation qualifier',reading='présumé',alternatives='Medial letters remain compressed; no extra word supplied.',confidence='medium',crop=G['p17']['file'],context_crop=G['p12']['file'])
]

audit_reading=candidate.replace('\\scanpage{127}\n','',1)
report=dict(
 page=PAGE,scan=127,reader='reader_a',line_count=53,
 line_count_detail=dict(main=23,margin=26,insertion=2,standalone_numbers=2),
 line_count_convention='Main and marginal logical written baselines include display rows. Two displaced replacement inscriptions are additionally counted; ordinary superscripts and the formula numbers on their display baselines are not extra lines. Author 63 and foliation 126 are separate standalone lines.',
 line_inventory=dict(main=[dict(line=i+1,reading=x) for i,x in enumerate(main_lines)],margin=[dict(line=i+1,reading=x) for i,x in enumerate(margin_lines)],insertions=[r'\inserted{$\mathcal E_{K_1}^{\bar K}$}',r'\inserted{\mathcal E_{K_1}}'],standalone_numbers=['63','126']),
 changes=changes,decisions=decisions,unlisted_doubt_decisions=unlisted,inventory=inventory,doubts=doubts,
 audit_boxes=[dict(box='b01',kind='margin note; insertion; deletion; doubtful formula; handwritten number; C/H word difference; less-than-high C departure',bbox=[0,0,1681,2361],reading=audit_reading)],
 audit_geometry_note='The oblique note runs beside and into leading body contexts from the page head through the final lines. A complete-page contextual rectangle includes all of those intersections without inventing clipped-word readings. Its reading is actual manuscript transcription only, excluding the editorial scan identifier.',
 notes=[
  'Authorial manuscript number 63 and thin foliation 126 are both present. The latter is in a different hand.',
  'The page continues a discussion of sections and then gives item b about an elementary anabelian model U. It formulates the fixed-group assertions (32) and (33); the left note asks about normalizers, sections, points of a normalized space, H¹ fibres, subgroup conditions and valuation data.',
  'Every word, formula, marginal baseline and correction on this page was read visually. No external research, OCR, text extraction or TeX compilation was used. This reading does not verify the mathematical conjectures.',
  'The main opening remains en/à uncertain. Literal au dessus is retained without the hyphen supplied by both witnesses.',
  'concen- ends a physical baseline and trer begins the next. The written hyphen and line break are retained rather than becoming an ordinary internal lexical hyphen.',
  'The seven round superscripts are retained as 0/circle uncertain. The page-local strokes do not warrant a semantic normalization of the notation.',
  'The live relative expression uses a comma between L and K. The separator in the crossed predecessor is not resolved by copying this live occurrence. Capital Pi is preferred from the cap/posts but case remains explicit uncertainty in both occurrences.',
  'Both old marginal E_K expressions are superseded by separately written full replacement groups. The visible cancellation is concentrated on K; the deletion wrapper records the superseded group, not a claim that the strike physically traverses every component.',
  'The apparent underline below section is the upper cap of I_V on the following baseline; no separate underline is transcribed. The final exclamation-like upright is traced to the descender of q in question; the three following dots remain.',
  'The three marginal quantifier-like forms are transcribed as the written abbreviation tt, from their separate t stems; no expansion to tout or replacement by a mathematical quantifier is made.',
  'The first two X alphabets are resolved, while the third X upper decoration remains doubtful because of the f-descender intersection. The H¹ exponent and the cancelled words/signs remain explicitly uncertain.',
  'No separately readable full stop is supplied after Norm(I_V) at the scan edge, after alg before its slash, or after the lower closing parenthesis. The upper group expression has a visible comma before sur.',
  'H’s editorial synopsis and page note are excluded from the transcription. Its long marginal gaps are read from the ink and are logged by contiguous manuscript blocks.',
 ],
 checks=[],
 hand_observations=[
  dict(habit='A compact joined K can resemble n or h.',places='Main line 6–7 group expressions; upper marginal replacement',holds='Clear K forms in the same expression establish the branched letter; joining compresses its right arms in later occurrences.',witness_errors='Not used to regularize the unresolved H¹ superscript; H misreads the distinct U subscript as K.'),
  dict(habit='The calligraphic E is drawn with two rounded lobes and may resemble epsilon.',places='All main and marginal group formulas on this page',holds='Repeated consistent group-letter shape throughout the local page.',witness_errors='No independent alphabet correction is asserted.'),
  dict(habit='Top cap of a capital I can appear to underline words above.',places='Marginal section / I_V overlap',holds='The cap is continuous with the upright and lower foot in this occurrence.',witness_errors='C marks section as underlined.'),
  dict(habit='Long q and f descenders overlap punctuation or decorations in the following baseline.',places='Final question / apparent exclamation; forment / third normalized-space glyph',holds='q attachment is traced; exact separation of f and the third tilde remains uncertain.',witness_errors='C gives a final exclamation; its third tilde is not secure from local ink.'),
  dict(habit='Short tt is written with two separate tall stems; the second has a cross and curled foot.',places='Three marginal universal clauses, compared with main tte',holds='Same broad construction at all three marginal occurrences, with different joining at the second.',witness_errors='C renders all three as forall.'),
  dict(habit='Pi-like cap and posts alone do not settle uppercase/lowercase.',places='Cancelled relative expression and live formula (33)',holds='Both forms have long legs; the cancelled form is further obscured.',witness_errors='Both witnesses select lowercase without displaying this case uncertainty.'),
  dict(habit='Retracing can leave extra upper strokes without a separately readable former word.',places='Final se; marginal aux',holds='Current letter paths are readable; no prior letters are invented.',witness_errors='C doubts both places; the present readings are retained with stated evidence.'),
 ],
 notation=[
  dict(written=r'$N_V=\operatorname{Norm}(I_V)$',meaning_or_use='Question written in the upper margin; no separate bar over I.',places='Marginal line 3'),
  dict(written=r'$\mathcal E_U^{\bar L}$',meaning_or_use='Group from which the section over the K group is said to lift.',places='Main line 6'),
  dict(written=r'$\Gamma=\mathcal E_K^{\bar K}$',meaning_or_use='Explicit local Gamma convention.',places='Main line 15'),
  dict(written=r'$\Gamma^{\unsure{0|\circ}}$',meaning_or_use='Raised round-mark form in the fixed-group and centralizer expressions; glyph distinction unresolved.',places='Main (32), qualification, centralizer, (33)'),
  dict(written=r'$\tilde{\mathfrak X}_{L/K}$; $\mathfrak X_{L/K}$',meaning_or_use='Normalized-space and base-space symbols named in the margin; the third upper decoration remains separately uncertain.',places='Marginal lines 9 and 11'),
  dict(written=r'$H^1(\deleted{\mathcal E_K}\inserted{\mathcal E_{K_1}}^{\unsure{G|\bar K}},I_V)\ldots.$',meaning_or_use='Written fibre expression with an altered group and four following dots; superscript unresolved.',places='Marginal line 12 and lower replacement'),
  dict(written=r'$(\mathcal E_L^{\bar L})^{\Gamma}=I_V$',meaning_or_use='Final marginal invariant formula; Gamma has no separate bar/circle.',places='Marginal line 22'),
  dict(written=r'$(\unsure{\Pi|\pi}_{L,K}^{\bar L})^{\Gamma^{\unsure{0|\circ}}}=(1)$',meaning_or_use='Live comma-indexed relative expression in (33), case and round superscript unresolved.',places='Main formula (33)'),
 ],
 abbreviations=[dict(written=a,expansion=b) for a,b in [('tte','toute'),('qd','quand'),('pt','point'),('pts','points'),('tjrs','toujours'),('tt','tout'),('s-groupe','sous-groupe'),('simplᵗ','simplement'),('rés.','résiduel'),('alg','algébrique')]],
 inspection=dict(whole=True,halves=['top','bottom'],crops=[x['file'] for x in GEOM],crop_count=17,deletions_insertions_checked=True,
  image_counts=dict(whole=1,native_top=1,native_bottom=1,successfully_inspected_saved_crops=17),
  unsuccessful_display_attempts=[dict(crop=G['p09']['file'],reason='An initial tool result was truncated by the available context and was not usable as an inspection; the same saved file was successfully displayed after context recovery.')],
  repairs=[dict(crop=G['p14']['file'],repairs=G['p09']['file'],reason='The first upper-margin rectangle clipped right-hand context. The enlarged contextual rectangle reaches the actual scan edge; no off-page completion is made.')],
  focused_views=[dict(crop=G['p13']['file'],purpose='Still-open Gamma qualification and crossed endpoint',whole_context=G['p07']['file']),dict(crop=G['p15']['file'],purpose='Still-open H¹ layers/exponent and section/s/I-cap overlap; right formula endpoints are outside this detail rectangle',whole_context=[G['p10']['file'],G['p11']['file']]),dict(crop=G['p16']['file'],purpose='Still-open first quantifier and raised t; second quantifier complete in p11',whole_context=G['p11']['file']),dict(crop=G['p17']['file'],purpose='Still-open cancellation, third quantifier, compressed qualifier and descender/punctuation attachment; right endpoints complete in p12',whole_context=G['p12']['file'])],
  no_second_audit=True,no_other_pages_accessed=True)
)

assert len(main_lines)==23 and len(margin_lines)==26
assert report['line_count']==sum(report['line_count_detail'].values())
with (PACKET/'marks.tsv').open(newline='',encoding='utf-8-sig') as f:
    supplied={x['id'] for x in csv.DictReader(f,delimiter='\t')}
assert {x['id'] for x in decisions}==supplied
assert len(decisions)==len(supplied)
for row in changes+decisions:
    assert (ROOT/'edition'/row['crop']).is_file()
    x0,y0,x1,y1=row['bbox']
    assert 0<=x0<x1<=1681 and 0<=y0<y1<=2361
stack=[]
for i,c in enumerate(candidate):
    if c=='{' and (i==0 or candidate[i-1]!='\\'): stack.append(i)
    elif c=='}' and (i==0 or candidate[i-1]!='\\'):
        assert stack,(i,'unmatched closing brace')
        stack.pop()
assert not stack
assert candidate.count('$')%2==0
assert not any(x in candidate for x in ['\\ill{','\\uncertain{','\\marginal{','\\note{','\\supplied{','\\struck{'])
assert report['audit_boxes'][0]['reading']==candidate.replace('\\scanpage{127}\n','',1)
(OUT/f'{PAGE}.tex').write_text(candidate,encoding='utf-8')
(OUT/f'{PAGE}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(page=PAGE,changes=len(changes),decisions=len(decisions),doubts=len(doubts),crops=len(GEOM),line_count=report['line_count'],audit_boxes=len(report['audit_boxes'])),ensure_ascii=False))
