from pathlib import Path
import json,re

BASE=Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACK=Path('/workspace/scratch/481648fc487b/reader_packets/150_scan045')
C=(PACK/'C.tex').read_text()
H=(PACK/'H.tex').read_text()

def macro_at(s,prefix):
    a=s.index(prefix); j=s.index('{',a)+1; depth=1
    while depth:
        if s[j]=='{':depth+=1
        elif s[j]=='}':depth-=1
        j+=1
    return s[a:j]

mb_c=macro_at(C,r'\margin{Ceci')
mc_c=macro_at(C,r'\margin{Implique')
mbc_c=macro_at(C,r'\margin{\textcircled{b}')
md_c=macro_at(C,r'\margin{implique')
mb_h=macro_at(H,r'\marginal{\uncertain{Considérons}')
mc_h=macro_at(H,r'\marginal{Implique')
mbc_h=macro_at(H,r'\marginal{(b) et (c)')
md_h=macro_at(H,r'\note{« d » cerclé ; en travers')
mb_f=r"\margin{Ceci implique que $d,d'$ sont des drap. tels que $d''=d\cup d'$ soit un drapeau et que $d,d'$ y soient \unsure{cofinaux} i.e. $d,d'$ aient $=$ élément final $i$, alors $\Sigma_{d''}=\Sigma_d\cap\Sigma_{d'}$ dans $\Sigma_i$}"
mc_f=r"\margin{Implique que si $d,d'$ sont deux drapeaux ayant $=$ élément final $k$, et si $d\cup d'$ n'est pas un drapeau, alors $\Sigma_d\cap\Sigma_{d'}=\phi$}"
mbc_f=r"\margin{\textcircled{b} et \textcircled{c} impliquent que si $(d_\alpha)_\alpha$ est une famille \inserted{\unsure{finie}} de drapeaux de $I$, \deleted{\unsure{$\forall\alpha$}} \unsure{$\forall\alpha\in A$} \unsure{aient|sont} final $k$, donc les $\Sigma_{d_\alpha}\subset\Sigma_k$, alors $\bigcap\Sigma_{d_\alpha}$ est \uline{vide} si $\bigcup d_\alpha$ n'est pas un drapeau, et $=\Sigma_{\cup d_\alpha}$ sinon}"
md_f=r"\margin{implique le $=$ dans les $\Sigma_d$\unsure{;|,} \unsure{on prend} les $\Sigma_{d'}\subset\Sigma_d$ (i.e. but pour $d'\supsetneqq d$, et $d$ cofinal dans $d'$) \unsure{ce qui} \unsure{les} bord-ts\inserted{$d'=d\cup\{i\}$} \unsure{qui sont} toutes pour dans $\Sigma_d$ \unsure{liss.|lisses}}"

tex=C
for a,b in [(mb_c,mb_f),(mc_c,mc_f),(mbc_c,mbc_f),(md_c,md_f)]:
    assert a in tex
    tex=tex.replace(a,b)
repls=[
 (r'\unsure{\textcircled{a}|$1^\circ$}',r'\textcircled{a}'),
 (r'\Sigma_{*\leq z}\hookrightarrow I_{\leq k}'+'\n'+r'\]'+'\n'+r') induit',r'\Sigma_{*\leq z}\hookrightarrow I_{\leq k}'+'\n'+r'\]'+'\n'+r'\margin{\uline{injection}}'+'\n'+r') induit'),
 (r'\varnothing',r'\phi'),
 (r'\unsure{Gros}','Gros'),
 (r'\unsure{bord-ts}','bord-ts'),
 (r'grâce à \unsure{(30)}',r'grâce : (30)'),
 ('que si on a un drapeau',r'que si \unsure{on a} un drapeau'),
 (r'd=(i_0,--i_n,k)',r'd=(i_{\unsure{0|1}},--i_n,k)'),
 (r'\Sigma_{i_0k},\Sigma_{i_1k}-\Sigma_{i_n,k}',r'\Sigma_{i_{\unsure{0|1}}k},\Sigma_{i_{\unsure{1|2}}k}\mathinner{\cdotp-}\Sigma_{i_n,k}'),
 (r'\unsure{bordants}',r'\unsure{bordants|bord-ts}'),
 (r'\Sigma_{i_0- i_n,k}',r'\Sigma_{i_{\unsure{0|1}}-i_n,k}'),
 (r'\mspage{44}',r'\margin{44}'),
]
for a,b in repls:
    assert a in tex,a
    tex=tex.replace(a,b)
(BASE/'reader_returns/150_scan045.tex').write_text(tex)

xy={
'page18':[48,32,105,88], 'opening':[310,62,1074,146],
'condition_b':[50,145,288,326], 'display28':[285,168,1680,282],
'au_dessus_hom':[303,300,1677,485], 'first_maps':[574,466,1488,704],
'display29':[295,751,1148,886], 'order_note':[1252,733,1640,944],
'margin_b':[20,384,565,1088], 'no_minorant':[295,962,1640,1166],
'empty_main':[692,1160,1125,1265], 'minorant_paren':[310,1267,1318,1525],
'condition_c':[22,1195,379,1419], 'margin_c':[18,1170,580,1818],
'margin_bc':[1177,1020,1680,1587], 'fixed_k':[303,1563,1560,1755],
'bord_ts':[305,1755,1016,1881], 'reference30':[319,1824,1453,1974],
'flag_bottom':[303,1960,1545,2075], 'sigma_list':[330,2058,1665,2181],
'transversal_final':[350,2158,1645,2338], 'condition_d':[69,1765,319,1948],
'margin_d':[20,1785,810,2340], 'folio44':[20,2290,78,2348],
'margin_bc_full':[1140,950,1681,1610], 'margin_d_overlap':[270,1840,835,2110],
'reference30_complete':[1030,1765,1315,1985],
}
d=dict(scan=45,reader='reader_b',line_count=20,changes=[],marks=[],inventory=[],doubts=[],notes=[],check_events=[],notation=[],abbreviations=[],hand_log=[],second_boxes=[])

def ch(place,c,h,f,crop,evidence,kind='misread word',err='words',cc=False,hh=True,conf='high',marked=False,effect=''):
    d['changes'].append(dict(place=place,C=c,H=h,final=f,evidence=evidence,crop='150_scan045_'+crop+'.jpg',box=xy[crop],confidence=conf,kind=kind,error_kind=err,marked_in_H=marked,change_C=cc,change_H=hh,consequential=effect))
def mark(m,context,decision,reading,crop,evidence,conf='medium'):
    d['marks'].append(dict(mark=m,context=context,decision=decision,reading=reading,evidence=evidence,crop='150_scan045_'+crop+'.jpg',box=xy[crop],confidence=conf))
def inv(e,k,p,w,hand='his hand'):
    d['inventory'].append(dict(element=e,kind=k,position=p,first_words_or_objects=w,sheet_kind='text',hand=hand,transcribed='yes'))
def doubt(p,r,a,conf='medium'):
    d['doubts'].append(dict(place=p,reading=r,alternatives=a,confidence=conf))
def box(e,k,p,r,reason):
    d['second_boxes'].append(dict(box=e,kind=k,coords=xy[p] if isinstance(p,str) else p,reading=r,reason=reason))

ch('opening, terminal punctuation',r'On suppose, pour $i<j<k$',r'On suppose, pour $i<j<k$,',r'On suppose, pour $i<j<k$','opening','The line ends with the final k, followed by blank paper. H supplies a comma that has no independent ink.',kind='text not on the page',err='text not on page')
ch('upper condition heading, initial case',r'\margin{Condition \textcircled{b}}',r'\marginal{condition (b)}',r'\margin{Condition \textcircled{b}}','condition_b','The first letter is a tall capital C. The circled b is also described by H’s editorial note and its enclosure is not counted as a separate H omission.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling')
ch('explanatory sentence, au dessus','au dessus','au-dessus','au dessus','au_dessus_hom','The two word groups are separated by blank paper; no independent hyphen joins them.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling')
ch('explanatory sentence, d’un',r"au dessus d'un $k\in I$",r'au-dessus de $k\in I$',r"au dessus d'un $k\in I$",'au_dessus_hom','The next line starts with d, an apostrophe and the joined u/n run before k. The small diagonal drapeau strokes nearby belong to the marginal note, not this main line.')
ch('explanatory sentence, homomorphism abbreviation',"l'hom. d'ens.",r"l'\uncertain{hom.\ déf.}","l'hom. d'ens.",'au_dessus_hom','The first group is hom.; the next begins d-apostrophe and has a low e-n-s run and a final point, not déf. The abbreviations are not expanded.',marked=True)
ch('parenthetical insertion above induit',r'\inserted{qui par \unsure{\textcircled{a}|$1^\circ$}}',r'\uncertain{qui} \add{\uncertain{est} \ill{}}',r'\inserted{qui par \textcircled{a}}','first_maps','Qui par lies above the main baseline and is attached by a bent leader. The small closed circle contains a compact a-like body; there is no independent 1 followed by a raised degree circle. The short word par has a descending p and rightward continuation rather than est.',kind='insertion or placement',err='insertion placement',cc=True,marked=True,conf='medium')
ch('order note, subscript',r"l'ordre de $(\Sigma_*)_z$",r"l'ordre de $(\Sigma_{*})_{\le z}$",r"l'ordre de $(\Sigma_*)_z$",'order_note','Only z follows the closing parenthesis; there is no less-than-or-equal sign before it. The lower-ideal notation in the neighboring display is not imposed on this separate right-hand note.',kind='misread symbol or index',err='symbols and indices',effect='Preserves the note’s bare z subscript despite the nearby lower-ideal formulas.')
ch('order note, terminal stop',r'par celui de $I_{\leq k}$',r'par celui de $I_{\le k}$.',r'par celui de $I_{\leq k}$','order_note','The note ends at the k; there is no independent period after it.',kind='text not on the page',err='text not on page')
ch('first diagonal note, opening words','Ceci implique',r'\uncertain{Considérons}','Ceci implique','margin_b','Ceci and the separate implique outline are visible, including the tall l and descending p. There is no single Considérons word.',marked=True,conf='medium')
ch('first diagonal note, supplied si',r"Ceci implique que si $d,d'$",r"\uncertain{Considérons} \uncertain{que} si $d,d'$",r"Ceci implique que $d,d'$",'margin_b','The first diagonal line ends at que and the next starts directly with d,d-prime. No separate si strokes lie between these lines. Both witnesses supply the word; the resulting source grammar is retained.',kind='text not on the page',err='text not on page',cc=True)
ch('first diagonal note, abbreviated flag word',r'\unsure{drap.}',r'sont des drapeaux',r'sont des drap.','margin_b','After sont des the short d-r-a-p run ends in a point. No e-a-u-x ending belongs to this occurrence. It is distinct from the complete singular drapeau at the end of the next diagonal line.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling',cc=True,conf='medium')
ch('first diagonal note, phantom drapeaux insertion',r'\unsure{drap.}\inserted{drapeaux}',r'sont des drapeaux',r'drap.','margin_b','No third flag word or insertion leader exists here. C’s alleged inserted drapeaux reuses the singular drapeau that terminates d-double-prime=d union d-prime soit un drapeau on the next diagonal line. The crossing underlined d’un belongs to the main sentence.',kind='insertion or placement',err='insertion placement',cc=True,hh=False,effect='Removes a duplicate transcription of the next diagonal line’s ending.')
ch('first diagonal note, cofinal clause',r"et que $d,d'$ \unsure{ay. même} élément final $i$",r"et que $d,d'$ \ill{} \ill{}",r"et que $d,d'$ y soient \unsure{cofinaux}",'margin_b','A descending y is followed by the s/i and final t strokes of soient. The following c-o-f-i run has a tall f and a compressed naux ending; crossing ink leaves cofinaux narrowly uncertain. Élément final i belongs to the following aient-equals clause, not this line.',cc=True,marked=True,conf='medium')
ch('first diagonal note, verbal equality and final-element phrase',r"i.e. $d,d'$ aient \unsure{$=$} \uline{\unsure{l'injection|l'égalité}}",r"i.e.\ $d,d'\subset$ \ill{}",r"i.e. $d,d'$ aient $=$ élément final $i$",'margin_b','Two parallel short strokes after aient form a verbal equality sign, not a subset sign. The diagonal continuation reads élément final i. The underlined horizontal injection belongs to a separate annotation, so it is not used to complete this sentence.',kind='misread symbol or index',err='symbols and indices',cc=True,marked=True,conf='medium')
ch('independent horizontal annotation, injection',r"\uline{\unsure{l'injection|l'égalité}}",r'\emph{injection}',r'\margin{\uline{injection}}','margin_b','The underlined word is horizontal beside the first lower-ideal map, while the surrounding note rises diagonally. Its letters read injection, without a separate l-apostrophe prefix. It is transcribed as a separate marginal annotation, not as part of the diagonal conclusion.',kind='insertion or placement',err='insertion placement',cc=True,conf='medium')
ch('first diagonal note, end punctuation',r'dans $\Sigma_i$.',r'dans $\Sigma_i$ \ldots',r'dans $\Sigma_i$','margin_b','The note ends with Sigma_i. Neither a period nor an ellipsis follows on that diagonal baseline.',kind='text not on the page',err='text not on page',cc=True)
ch('no-common-minorant clause, insertion attachment',r"n'ont pas de minorant \inserted{dans $I$}, alors",r"$i,j\le k$ \add{dans $I$} n'ont pas de minorant, alors",r"n'ont pas de minorant \inserted{dans $I$}, alors",'no_minorant','Dans I is raised above minorant and its curved leader points to the gap after that word. It does not attach immediately after i,j≤k.',kind='insertion or placement',err='insertion placement')
ch('main emptiness equation, written glyph',r'\Sigma_{ik}\cap\Sigma_{jk}=\varnothing',r'\Sigma_{ik}\cap\Sigma_{jk}=\emptyset',r'\Sigma_{ik}\cap\Sigma_{jk}=\phi','empty_main','The empty-set notation is a small loop crossed by a long descending stem, a phi-like handwritten form. The literal glyph is retained, consistently with the established notation snapshot.',kind='misread symbol or index',err='symbols and indices',cc=True)
ch('minorant parenthesis, noun and baseline',r'(si $i,j$ ont un minorant $l$, alors',r'(si $i,j$ \add{\uncertain{ont}} \uncertain{un minimum} $l$, alors',r'(si $i,j$ ont un minorant $l$, alors','minorant_paren','Ont is on the ordinary baseline. The following noun has the extended m-i-n-o-r-a-n-t run and final t, rather than minimum; l is a separate looped letter.',marked=True,conf='medium')
ch('unfinished subset, supplied illegible target',r'\Sigma_{ik}\cap\Sigma_{jk}\subset\ )',r'\Sigma_{ik}\cap\Sigma_{jk}\subset\ \ill{}\ )',r'\Sigma_{ik}\cap\Sigma_{jk}\subset\ )','minorant_paren','The subset sign is followed by blank paper and then the closing parenthesis. There is no ink requiring an illegibility marker or a completed target.',kind='text not on the page',err='text not on page',marked=True,effect='Preserves the visibly unfinished relation without supplying its expected right-hand side.')
ch('middle condition heading, initial case',r'\margin{Condition \textcircled{c} \unsure{Gros}}',r'\marginal{condition (c)}',r'\margin{Condition \textcircled{c} Gros}','condition_c','Condition begins with a capital C. H’s note already reports the circled c and Gros, so neither annotation is counted as an H omission.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling')
ch('middle heading, Gros',r'\unsure{Gros}',r'\uncertain{Gros}','Gros','condition_c','The separate word has an open capital G, followed by r, a looped o and the returning s stroke. H reports the same candidate in editorial prose; only the C doubt is resolved here.',kind='other',err='other',cc=True,hh=False,conf='medium')
ch('second diagonal note, recovered prose',mc_c,mc_h,mc_f,'margin_c','The note reads Implique que si d,d-prime sont deux drapeaux, then the common-final-element phrase, then et si d union d-prime n’est pas un drapeau, alors and the intersection equation. H leaves sont and most of those clauses illegible. The additional verbal equality and élément, the final phi glyph and absent terminal stop are accounted separately against C.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
ch('second diagonal note, common-final-element phrase',r'ayant final $k$',mc_h,r'ayant $=$ élément final $k$','margin_c','After ayant there are two short parallel strokes. The next diagonal line begins élément before final k. C omits both the verbal equality and the word élément. H’s recovery is included in the whole-note row.',kind='omission',err='omissions',cc=True,hh=False,conf='medium')
ch('second diagonal note, emptiness glyph',r'\Sigma_d\cap\Sigma_{d\prime}',r'\Sigma_d\cap\Sigma_{d\prime}',r'\phi','margin_c','Placeholder replaced below.',kind='misread symbol or index',err='symbols and indices',cc=True,hh=False)
# Use exact primed-index excerpts rather than an editorial synonym.
d['changes'][-1].update(C=r"\Sigma_d\cap\Sigma_{d'}=\varnothing",H=r"\Sigma_d\cap\Sigma_{d'}=\emptyset",final=r"\Sigma_d\cap\Sigma_{d'}=\phi",evidence='The final symbol is again a loop with a long descending crossing stroke, not a normalized empty-set glyph. H’s whole-note recovery is counted once above; this local row records the separate C symbol change.')
ch('second diagonal note, supplied terminal stop',r"$\Sigma_d\cap\Sigma_{d'}=\varnothing$.",mc_h,r"$\Sigma_d\cap\Sigma_{d'}=\phi$",'margin_c','No separate point follows the terminal phi on the diagonal baseline. The source note ends there.',kind='text not on the page',err='text not on page',cc=True,hh=False)
ch('right diagonal note, family introduction and upper index',r"\textcircled{b} et \textcircled{c} impliquent que si $(d_\alpha)_{\alpha\in\unsure{A}}$ est une famille",r'(b) et (c) impliquent que, pour une famille $(d_\alpha)$',r'\textcircled{b} et \textcircled{c} impliquent que si $(d_\alpha)_\alpha$ est une famille','margin_bc_full','The complete upper line reads impliquent que si, the parenthesized family with a single alpha below it, and est. There is no upper ∈A after that alpha. The larger A and quantified/overstruck group are on a later line and must not be duplicated in this index.',kind='misread symbol or index',err='symbols and indices',cc=True,conf='medium')
ch('right diagonal note, finite-family insertion',r'\inserted{\unsure{finie}}',mbc_h,r'\inserted{\unsure{finie}}','margin_bc_full','A small raised word is inserted above famille/de drapeaux, with a tall f and small dotted strokes. Finie remains tentative because of crossing ink; H omits this independent insertion.',kind='omission',err='omissions',marked=True,conf='low')
bc_quant=r"de drapeaux de $I$, \deleted{\unsure{$\forall\alpha$}} \unsure{$\forall\alpha\in A$} \unsure{aient|sont} final $k$"
ch('right diagonal note, ambient index set and quantified revision',bc_quant,r'de drapeaux ayant \uncertain{même} \uncertain{point final} $k$',bc_quant,'margin_bc_full','De I is written after drapeaux. Beneath it a crossed group and a separate live group lead into the compressed word before final k. The quantifier candidates remain honestly doubtful. H supplies même point and omits the visible ambient I and revision; those words are not recovered from the ink.',kind='insertion or placement',err='insertion placement',marked=True,conf='low')
ch('right diagonal note, donc',r'donc les $\Sigma_{d_\alpha}\subset\Sigma_k$',r'\ill{} les $\Sigma_{d_\alpha}\subset\Sigma_k$',r'donc les $\Sigma_{d_\alpha}\subset\Sigma_k$','margin_bc_full','The low d-o-n-c run follows the comma after final k. It is readable independently of the uncertain preceding quantified phrase.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='medium')
ch('right diagonal note, alors',r'alors $\bigcap\Sigma_{d_\alpha}$',r'$\Sigma_{d_\alpha}\subset\Sigma_k$, $\bigcap\Sigma_{d_\alpha}$',r'alors $\bigcap\Sigma_{d_\alpha}$','margin_bc_full','Alors is written on the short line before the intersection. H omits it.',kind='omission',err='omissions',conf='medium')
ch('right diagonal note, terminal stop',r'$=\Sigma_{\cup d_\alpha}$ sinon.',r'$=\Sigma_{\bigcup d_\alpha}$ sinon',r'$=\Sigma_{\cup d_\alpha}$ sinon','margin_bc_full','The note ends at sinon without an independent point. Cup versus bigcup is only typesetting size here and is not counted as a symbol difference.',kind='text not on the page',err='text not on page',cc=True,hh=False)
ch('transversality paragraph, cancelled prefix',r'\deleted{bord}',r'\struck{bordants}',r'\deleted{bord}','bord_ts','The cancellation covers b-o-r-d, with the tall final d still visible. No additional ants letters precede the new live bord-ts.',kind='text not on the page',err='struck text',conf='medium')
ch('transversality paragraph, live abbreviation',r'\unsure{bord-ts}',r'\struck{bordants} bordants',r'bord-ts','bord_ts','The live word has b-o-r-d, a separate hyphen, and the compact t/s ending. It is an abbreviation rather than the fully written bordants.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling',cc=True)
ch('reference parenthesis, supplied à',r'grâce à',r'\uncertain{grâce à}',r'grâce','reference30','The written word ends after grâce and is followed by a colon. No independent à body or accent appears between it and the two punctuation points.',kind='text not on the page',err='text not on page',cc=True,marked=True)
ch('reference parenthesis, colon',r'grâce à \unsure{(30)}',r'\uncertain{grâce à} : (30)',r'grâce : (30)','reference30','Two vertically separated points form a colon immediately before (30). The omitted à and the reading of the digits are recorded separately.',kind='omission',err='omissions',cc=True,hh=False)
ch('reference number, 30',r'\unsure{(30)}',r'(30)',r'(30)','reference30','Inside the inner parentheses the first digit has the curved double part of 3 and the second a low closed return, read 0. No equation sequence from another page is used.',kind='other',err='other',cc=True,hh=False,conf='medium')
ch('reference insertion, et 28',r'\inserted{et 28,}',r'\add{et (28),}',r'\inserted{et 28,}','reference30_complete','The upward completion contains every stroke of et 28,. The long left lead-in joins the upper curve of 2; there is no separate opening parenthesis. The single mark after 8 starts low and descends below the numeral baseline, so it is a comma, not a full-height closing parenthesis. A leader enters after (30), not after the earlier transversaux comma.',kind='insertion or placement',err='insertion placement',conf='medium')
ch('flag example, verbal opening',r'que si on a un drapeau',r'que si \uncertain{$d$ est} un drapeau',r'que si \unsure{on a} un drapeau','flag_bottom','The small opening before un drapeau is crowded by diagonal note ink. The on-a candidate is retained narrowly; the exposed shapes do not show H’s separate d est. The main horizontal un drapeau is not reused to finish the marginal note.',marked=True,conf='low')
flag_f=r'd=(i_{\unsure{0|1}},--i_n,k)'
ch('flag example, continuation marks',r'd=(i_0,--i_n,k)',r'd=(i_0,\ldots,i_n,k)',flag_f,'flag_bottom','Two short headless horizontal strokes follow the first comma, and no comma follows them before i_n. The first small digit is filled/retraced and remains 0/1 uncertain; adding that uncertainty alone is not counted as a C textual change.',kind='misread symbol or index',err='symbols and indices',conf='medium')
list_f=r'\Sigma_{i_{\unsure{0|1}}k},\Sigma_{i_{\unsure{1|2}}k}\mathinner{\cdotp-}\Sigma_{i_n,k}'
ch('list of bordering subsets, indices and continuation',r'\Sigma_{i_0k},\Sigma_{i_1k}-\Sigma_{i_n,k}',r'\Sigma_{i_0,k},\Sigma_{i_1,k},\ldots,\Sigma_{i_n,k}',list_f,'sigma_list','The first two nested indices have no comma before k; the last has a clear low comma. Between the second and last Sigma there are two marks, a tiny point and a short dash, not one dash or three points. The first small digit is an upright/filled stroke (0/1); the second has a low bent foot (1/2). Those doubts are not resolved by the expected sequence.',kind='misread symbol or index',err='symbols and indices',cc=True,conf='medium')
ch('bordering subsets, abbreviated noun','sous-ens','sous-espaces','sous-ens','sigma_list','The short word after sous- has only the low e-n-s run. The longer espaces ending is not written.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling')
final_eq=r'\Sigma_d=\Sigma_{i_{\unsure{0|1}}-i_n,k}'
ch('last equality, continuation dash',r'\Sigma_d=\Sigma_{i_0- i_n,k}',r'\Sigma_d=\Sigma_{i_0\cdots i_n,k}',final_eq,'transversal_final','The lower line has one short horizontal dash between the initial indexed i and i_n. The final low comma before k is visible. The first small digit is an upright/filled 0-or-1 form and remains doubtful without imposing the flag’s expected starting index.',kind='misread symbol or index',err='symbols and indices',conf='medium')
ch('lower condition heading, initial case',r'\margin{Condition \textcircled{d}}',r'\marginal{condition (d)}',r'\margin{Condition \textcircled{d}}','condition_d','The heading begins with a capital C. H separately reports the circled d, so its enclosure is not counted as a new omission.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling')
ch('lower diagonal marginal note, opening words',r'implique le $=$ dans les $\Sigma_d$',md_h,r'implique le $=$ dans les $\Sigma_d$','margin_d','H’s editorial note explicitly quotes partial source readings, reproduced verbatim in the H field. Its opening implique que does not match the visible le followed by two verbal equality strokes and dans. Editorial framing is evidence only and is not inserted into the transcription.',conf='medium')
md_middle=r"\unsure{on prend} les $\Sigma_{d'}\subset\Sigma_d$ (i.e. but pour $d'\supsetneqq d$, et $d$ cofinal dans $d'$)"
ch('lower diagonal marginal note, inclusion and cofinal parenthesis',r"\unsure{on prend} les $\Sigma_{d'}\subset\Sigma_d$ (i.e. but pour $d'\supsetneqq d$, et $d$ cofinal dans $d'$)",md_h,md_middle,'margin_d','The quoted H fragment intersperses illegibility marks and an isolated d-prime before the inclusion. The complete visible sequence has the inclusion followed by the i.e. but pour parenthesis, the strict superset relation, and d cofinal dans d-prime. On prend remains tentative. This records recoverable source content within H’s quoted evidence, not an absent whole note.',kind=r'readable ink left as \ill{}',err='readable ink left as illegible',marked=True,conf='low')
md_end=r"\inserted{$d'=d\cup\{i\}$} \unsure{qui sont} toutes pour dans $\Sigma_d$ \unsure{liss.|lisses}"
ch('lower diagonal marginal note, raised formula and ending fragment',r"\inserted{$d'=d\cup\{i\}$} \unsure{qui sont} toutes pour un drapeau de $d'$ dans $\Sigma_d$ \unsure{lisses}",md_h,md_end,'margin_d','The quoted H reading omits the independent raised formula d-prime=d union {i} and the visible later fragment. The small qui sont and final liss./lisses groups remain doubtful. Main horizontal un drapeau and other already-used d-prime strokes are not borrowed to complete the fragment.',kind='omission',err='omissions',conf='low')
ch('lower diagonal marginal note, borrowed main-line words',r"toutes pour un drapeau de $d'$ dans $\Sigma_d$",md_h,r'toutes pour dans $\Sigma_d$','margin_d_overlap','The obvious un drapeau is horizontal main text. No second independently written un drapeau de d-prime follows the diagonal toutes pour. The other visible d-prime strokes already belong to cofinal dans d-prime and the raised formula. C reuses those strokes to complete a fragment; the duplicate words are removed.',kind='insertion or placement',err='insertion placement',cc=True,hh=False,effect='Leaves the marginal sentence fragment incomplete instead of filling it from crossing main text.')
ch('lower diagonal marginal note, bordering abbreviation',r'\unsure{les} bord.',md_h,r'\unsure{les} bord-ts','margin_d','The separate diagonal bordering word has a visible shortened bord stem followed by a dash and compact t/s ending, above the raised d-prime formula. It is distinct from the larger main-line bord-ts, does not end at C’s bord., and does not spell out H’s quoted bordant.',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling',cc=True,conf='medium')
ch('bottom-left foliation',r'\mspage{44}','[absent]',r'\margin{44}','folio44','Two thin grey open-angle 4 forms appear at the bottom-left edge. This is separate foliation, with hand attribution uncertain; it is not another main handwritten page number.',kind='omission',err='omissions')

# Every original C uncertainty, in original order, including struck ink.
mark(r'\unsure{\textcircled{a}|$1^\circ$}',r'qui par \unsure{\textcircled{a}|$1^\circ$}','first',r'\textcircled{a}','first_maps','A small closed circle encloses a compact a-like ink body; there is no separate numeral 1 to its left. The full insertion and both adjacent maps have been read.')
mark(r'\unsure{drap.}',r'des \unsure{drap.}\inserted{drapeaux}','first','drap.','margin_b','The short d-r-a-p run and following point belong to the diagonal sont des line. The complete drapeau at the next line end is separate.')
mark(r'\unsure{ay. même}',r"$d,d'$ \unsure{ay. même} élément final",'other','y soient','margin_b','The descending y and following s/i/t strokes support y soient. The next word cofinaux remains separately marked where crossing ink obscures its middle; élément final i belongs to the following clause.')
mark(r'\unsure{$=$}',r"aient \unsure{$=$}",'first','$=$','margin_b','Two short parallel strokes are present after aient; this is not H’s single curved subset sign.','high')
mark(r"\unsure{l'injection|l'égalité}",r"\uline{\unsure{l'injection|l'égalité}}",'other',r'\margin{\uline{injection}}','margin_b','The underlined word reads injection, with no separate l-apostrophe, and follows a horizontal baseline beside the lower-ideal map. The diagonal note has a different baseline and is transcribed separately.')
mark(r'\unsure{Gros}',r'\textcircled{c} \unsure{Gros}','first','Gros','condition_c','Open capital G followed by r, rounded o and a returning s stroke.')
mark(r'\unsure{A}',r'$(d_\alpha)_{\alpha\in\unsure{A}}$','other',r'$(d_\alpha)_\alpha$','margin_bc_full','The expanded crop shows a single lower alpha and then the separate word est. No ∈A is written in that upper index; the large lower A belongs to the later revision.')
mark(r'\unsure{finie}',r'\inserted{\unsure{finie}}','undecided',r'\unsure{finie}','margin_bc_full','The raised word has a tall f and small dotted strokes, but the descender of impliquent crosses it. The full word remains tentative.','low')
mark(r'\unsure{$\forall\alpha$}',r'\deleted{\unsure{$\forall\alpha$}}','undecided',r'\unsure{$\forall\alpha$}','margin_bc_full','A heavy horizontal cancellation cuts the small group. Its quantifier/alpha interpretation is not independently secure.','low')
mark(r'\unsure{$\forall\alpha\in A$}',r'\deleted{\unsure{$\forall\alpha$}} \unsure{$\forall\alpha\in A$}','undecided',r'\unsure{$\forall\alpha\in A$}','margin_bc_full','A separate live group has an enlarged A-like body and adjoining small strokes, but the precise quantifier and membership sequence is crowded by revision ink. It is kept distinct from the upper family index.','low')
mark(r'\unsure{aient|sont}',r'\unsure{aient|sont} final $k$','undecided',r'\unsure{aient|sont}','margin_bc_full','The low linked group before final k does not give every letter clearly; no grammatical completion is used to select a candidate.','low')
mark(r'\unsure{bord-ts}',r'\deleted{bord} \unsure{bord-ts}','first','bord-ts','bord_ts','The live stem bord is followed by a detached hyphen and compact t/s ending.','high')
mark(r'\unsure{(30)}',r'grâce à \unsure{(30)}','first','(30)','reference30','The inner pair of parentheses encloses a curved 3 and low closed 0; both digits are read with the complete reference and inserted et 28.')
mark(r'\unsure{bordants}',r'sous-ens \unsure{bordants}','undecided',r'\unsure{bordants|bord-ts}','sigma_list','The final bordering word is compressed at the right edge; the ending may be fully written ants or another abbreviated t/s ending. Neither expansion is certified.')
mark(r'\unsure{on prend}',r'$\Sigma_d$, \unsure{on prend}','undecided',r'\unsure{on prend}','margin_d','The p and final d-like form are recoverable, but the first short word and internal links are crowded by crossing main-line ink.')
mark(r'\unsure{ce qui}',r"$d$ cofinal dans $d'$) \unsure{ce qui}",'undecided',r'\unsure{ce qui}','margin_d','The small diagonal continuation is crowded by main ce qui signifie at another angle; its local letters and attachment remain tentative.','low')
mark(r'\unsure{les}',r'\unsure{ce qui} \unsure{les} bord.','undecided',r'\unsure{les}','margin_d','A short linked group precedes the diagonal bord-ts, but the exact l/e/s strokes are not all separate.','low')
mark(r'\unsure{qui sont}',r"\inserted{$d'=d\cup\{i\}$} \unsure{qui sont}",'undecided',r'\unsure{qui sont}','margin_d_overlap','There is diagonal q-like and following low ink, distinct from the main horizontal un drapeau, but the compressed group remains tentative.','low')
mark(r'\unsure{lisses}',r'dans $\Sigma_d$ \unsure{lisses}','undecided',r'\unsure{liss.|lisses}','margin_d','The small final word has an l/i-like beginning and very compressed ending. An abbreviation liss. is possible; the full lisses is not certified.','low')

inv('N01','text','upper-left corner','18, main handwritten page number')
inv('T01','text','first main line','On suppose, pour i<j<k, without terminal comma')
inv('M01','margin note','upper-left beside (28)','Condition, circled b')
inv('F01','display','second main baseline','(28), Sigma_ijk equality and a priori inclusion, right parenthesis at the sheet edge')
inv('T02','text','next two main lines','ce qui signifie aussi que forall z; au dessus d’un k; l’hom. d’ens.')
inv('M02','margin note','upper-left diagonal note','Ceci implique que d,d′ sont des drap.; union flag; y soient cofinaux doubtful; aient = élément final i; intersection conclusion')
inv('I01','insertion','above the first induit','qui par circled a, with bent attachment leader')
inv('F02','display','map below l’hom. d’ens.','Sigma-star to I')
inv('F03','display','inside the following parenthesis','Sigma_(star≤z) hooked arrow I_≤k')
inv('M03','margin note','horizontal beside the first lower-ideal map','underlined injection, separate from the diagonal note')
inv('T03','text','parenthetical map context','induit une application; closing parenthesis; induit')
inv('F04','display','formula (29)','(Sigma-star)_≤z hooked arrow I_≤k')
inv('M04','margin note','right of formula (29)','l’ordre de (Sigma-star)_z est underlined induit par celui de I_≤k')
inv('T04','text','next two main lines','On suppose de plus; i,j≤k n’ont pas de minorant; alors')
inv('I02','insertion','above minorant, with curved leader','dans I, attached after minorant')
inv('F05','display','middle main equation','Sigma_ik cap Sigma_jk = phi')
inv('M05','margin note','left beside emptiness equation','Condition, circled c; Gros')
inv('T05','text','following parenthetical sentence','si i,j ont un minorant l, alors')
inv('F06','display','unfinished parenthetical formula','Sigma_ik cap Sigma_jk subset, blank target, closing parenthesis')
inv('M06','margin note','left middle diagonal note','Implique que si d,d′ sont deux drapeaux ayant = élément final k; nonflag union; empty intersection')
inv('M07','margin note','right middle diagonal note','circled b et circled c; family (d_alpha)_alpha; finite-family and quantified revision; intersection and union alternatives')
inv('I03','insertion','within right diagonal note above famille/de drapeaux','finie, doubtful')
inv('C01','deletion','within right diagonal note below de I','forall alpha candidate, obscured by a horizontal strike')
inv('T06','text','opening of final paragraph','On suppose enfin que le système des Sigma_ik, pour k fixé, qui sont des sous-espaces')
inv('I04','insertion','above the parenthesis pour k fixé','i in I_<k, curved leader into the parenthesis')
inv('C02','deletion','start of next main line','bord, crossed out')
inv('T07','text','live continuation after crossed bord','bord-ts de Sigma_k, sont underlined transversaux')
inv('M08','margin note','left of final paragraph','Condition, circled d')
inv('M09','margin note','lower-left diagonal note','implique le = dans les Sigma_d; included Sigma_d′; cofinal parenthesis; diagonal bord-ts; unresolved unfinished final fragment')
inv('I05','insertion','raised within the lower diagonal note',"d′=d union {i}, with its attachment curve")
inv('T08','text','main reference clause','ce qui signifie (grâce : (30) et 28,) que si')
inv('I06','insertion','above the reference parenthesis','et 28, with leader after (30), no extra parentheses')
inv('F07','display','flag inside main running line','d=(i_(0/1), two continuation dashes i_n,k), first digit doubtful')
inv('F08','display','next main running line','Sigma_(i_(0/1)k), Sigma_(i_(1/2)k), point-and-dash continuation, Sigma_(i_n,k)')
inv('T09','text','last two main prose lines','sous-ens, bordering ending doubtful; qui se coupent underlined transversalement le long de Sigma_d')
inv('F09','display','final equality continued on bottom line','Sigma_d=Sigma_(i_(0/1)-i_n,k), one dash and final period')
inv('N02','margin note','bottom-left edge','44','thin separate foliation; attribution uncertain')

doubt('first diagonal note, cofinal adjective',r'\unsure{cofinaux}','The cofi stem and naux-like ending are visible but crossed by neighboring main-line ink.')
doubt('right diagonal note, finite insertion',r'\inserted{\unsure{finie}}','A tall f and small dotted strokes are present; crossing ink obscures the full word.','low')
doubt('right diagonal note, cancelled quantifier',r'\deleted{\unsure{$\forall\alpha$}}','The heavy strike masks the small quantifier/alpha shapes.','low')
doubt('right diagonal note, live quantified group',r'\unsure{$\forall\alpha\in A$}','The enlarged A-like form and neighboring marks do not settle the complete sequence.','low')
doubt('right diagonal note, word before final',r'\unsure{aient|sont}','The low linked letters are compressed; syntax does not decide the reading.','low')
doubt('flag-example verbal opening',r'\unsure{on a}','Diagonal note strokes cross the opening of the main line.','low')
doubt('flag-example first digit',flag_f,'The first small digit is filled/retraced; 0 and 1 are not independently distinguished.')
doubt('bordering-subset list, first two digits',list_f,'The first digit is upright/filled (0/1); the second has a low bent foot (1/2). Both are kept with the complete list.')
doubt('last bordering adjective',r'\unsure{bordants|bord-ts}','The compact right-edge ending may be written ants or the abbreviated t/s ending.')
doubt('last equality, first digit',final_eq,'A small upright/filled stroke may be 0 or 1; the expected sequence is not used to decide.')
doubt('lower diagonal note, punctuation after Sigma_d',r'$\Sigma_d$\unsure{;|,}','A short punctuation group could be a semicolon or comma; the vertically separate part is small.')
doubt('lower diagonal note, on prend',r'\unsure{on prend}','The compressed two-word group is crossed by main-line ink.')
doubt('lower diagonal note, ce qui',r'\unsure{ce qui}','The diagonal continuation is crowded and its attachment remains uncertain; main horizontal ce qui signifie is separately transcribed.','low')
doubt('lower diagonal note, les',r'\unsure{les}','Small linked group immediately before the diagonal bord-ts.','low')
doubt('lower diagonal note, qui sont',r'\unsure{qui sont}','A diagonal q-like group and following low strokes are distinct from the main un drapeau, but not fully secure.','low')
doubt('lower diagonal note, last word',r'\unsure{liss.|lisses}','The source may abbreviate the word; the full ending is not plainly exposed.','low')

d['notes']=[
 'The page has main handwritten number 18, formulas (28) and (29), a later written reference (30) and raised et 28, three circled condition letters, and separate thin foliation 44. The line_count records 20 principal baselines; all marginal lines and insertions are separately inventoried and included in complete audit boxes.',
 'The principal text states intersection and no-common-minorant conditions, relates a lower-ideal map to the order on I, and then requires bordering subspaces to meet transversally. Marginal notes describe consequences for unions of flags and families of flags. These are reported manuscript claims, not independently verified mathematical conclusions.',
 'The upper diagonal note has no si after Ceci implique que. It uses the abbreviated drap., followed on the next line by the separate singular drapeau. C duplicates that latter word as an insertion. The main d’un k line crosses the note and its strokes are not reused as marginal text.',
 'The underlined injection is horizontal beside the first lower-ideal map. It is a separate annotation, not the object of the diagonal aient = clause. That diagonal clause continues élément final i. The preceding clause reads y soient, with cofinaux narrowly uncertain.',
 'The right order note writes (Sigma-star)_z without a less-than-or-equal sign. The displayed maps do have ≤z. The mismatch is retained without importing notation from one occurrence to another.',
 'The no-common-minorant equation and the second diagonal note use a loop-and-long-stem phi form for the empty set. The parenthetical subset relation is genuinely unfinished: blank paper separates the subset sign from the closing parenthesis.',
 'The right marginal family is written (d_alpha)_alpha, followed by est. The later enlarged A and quantified/overstruck group are separate. Their letters remain doubtful rather than being copied into the upper index.',
 'The written reference is grâce : (30), with no independent à. Et 28, is raised and attached after (30), without separate parentheses around 28. No later equation sequence is used to read the numbers.',
 'Continuation notation is local: two short dashes in the flag, one point plus one short dash in the Sigma list, and one dash in the final subscript. The small starting digits remain uncertain, including the possible 1/2 second list digit; neither witness’s expected enumeration resolves them.',
 'The lower diagonal note is incomplete and heavily crossed by main text. The obvious horizontal un drapeau and already-used d-prime strokes do not supply a second un drapeau de d-prime after toutes pour. Those duplicate words are removed. Remaining diagonal word groups and the last liss./lisses reading remain marked; no missing phrase is supplied.',
 'All whole-page/native-half viewing limits were observed. Twenty-four distinct places produced 27 saved images: the right-note expansion restores its clipped upper line, an unrotated completion of the lower note distinguishes its diagonal words from crossing main baselines, and the reference completion includes every upper stroke of raised et 28,. Every saved image was viewed.',
 'H’s lower-note editorial paragraph explicitly quotes partial source readings. That paragraph is reproduced verbatim as witness evidence in the affected collation rows. Its recoverable and mistaken quoted portions are collated; the editorial framing itself is excluded from the source transcription.',
 'No mathematical proof check, computation, or independent re-proof was performed. check_events is empty. Noting mismatches and unfinished formulas is a transcription finding only.',
]
d['notation']=[
 {'form':r'\Sigma_{ijk},\Sigma_{ik},\Sigma_{jk}','meaning_or_shape':'Sigma’s long upper cap can be retraced or detached; it is not an independent overbar. Lower k has an h-like tall stem and branch.','places':'(28), middle equations, final paragraph'},
 {'form':r'\Sigma_{*\leq z},\quad(\Sigma_*)_{\leq z},\quad(\Sigma_*)_z','meaning_or_shape':'The first map places star and ≤z below Sigma; (29) places ≤z after the closing parenthesis; the separate order note has only z.','places':'first map, (29), right order note'},
 {'form':r'\hookrightarrow','meaning_or_shape':'A curved upper-left hook joins a horizontal shaft ending in a clear right-pointing head.','places':'two lower-ideal maps'},
 {'form':r'\textcircled{a},\textcircled{b},\textcircled{c},\textcircled{d}','meaning_or_shape':'Reference letters enclosed in hand-drawn loops; the small inserted a is almost filled.','places':'qui par insertion; condition labels; right-note opening'},
 {'form':'=','meaning_or_shape':'Two short horizontal strokes used verbally, likely for même, without expanding the source.','places':'upper note aient =; middle note ayant =; lower note implique le ='},
 {'form':r'\phi','meaning_or_shape':'Small loop crossed by a long descending stem, used for the empty set.','places':'main no-minorant equation; second diagonal note'},
 {'form':r'(d_\alpha)_\alpha','meaning_or_shape':'Only alpha is visible below the closing parenthesis, followed by est on the baseline.','places':'right marginal note'},
 {'form':r'--,\quad\mathinner{\cdotp-},\quad-','meaning_or_shape':'Two short dashes, a point followed by a dash, and one dash respectively; no generic three-dot normalization.','places':'flag tuple; Sigma list; final equality subscript'},
 {'form':r'i_{\unsure{0|1}},\quad i_{\unsure{1|2}}','meaning_or_shape':'Very small digits can be filled upright strokes or bent low feet; the specific occurrences remain doubtful.','places':'flag, first two Sigma-list terms, final equality'},
]
d['abbreviations']=[
 {'form':'hom.','expansion':'homomorphisme'},
 {'form':"d’ens.",'expansion':'d’ensembles'},
 {'form':'drap.','expansion':'drapeaux'},
 {'form':'i.e.','expansion':'id est'},
 {'form':'bord-ts','expansion':'bordants; abbreviation retained literally'},
 {'form':'sous-ens','expansion':'sous-ensembles'},
 {'form':'liss.','expansion':'Possibly an abbreviated lisses; the final source word remains doubtful.'},
]
d['hand_log']=[
 {'habit':'Diagonal marginal writing crosses horizontal main text and can be transcribed twice unless baselines are traced.','places':'upper drap./drapeau; horizontal injection; lower un drapeau and raised d-prime','consistent':'Three distinct attachment corrections are supported by full local geometry.','witness_errors':'C creates phantom drapeaux and a borrowed un drapeau de d-prime fragment, and attaches injection to the wrong sentence.'},
 {'habit':'Tiny numerical subscripts may collapse into filled upright marks or low bent feet.','places':'first flag digit, first two Sigma-list digits, last equality','consistent':'All remain locally doubtful; equation labels 28,29,30 and foliation44 have larger distinguishable forms.','witness_errors':'C and H both state the conventional 0,1 sequence too confidently; new uncertainty alone is not counted as textual collation.'},
 {'habit':'The writer varies continuation-mark count and form.','places':'two dashes in the flag, point-plus-dash in the list, one dash in the final index','consistent':'Each local count is retained.','witness_errors':'H normalizes all three to three-point ellipses; C omits the point preceding the list dash.'},
 {'habit':'Verbal equality signs replace a word without grammatical expansion.','places':'aient =, ayant = élément final, implique le =','consistent':'Each is two short parallel bars.','witness_errors':'C omits the middle-note equality; H reads the upper one as a subset sign.'},
 {'habit':'Live technical adjectives and nouns are sometimes abbreviated.','places':'drap.; bord-ts; sous-ens; doubtful final liss.','consistent':'Full drapeau elsewhere is distinct from abbreviated drap.; the final adjective’s ending remains uncertain.','witness_errors':'H expands several abbreviated forms; C truncates the lower diagonal bord-ts to bord.'},
 {'habit':'A phi-like loop and stem is used for emptiness.','places':'main middle equation and second diagonal note','consistent':'Both visible forms have a small loop and a stem extending far below.','witness_errors':'C and H normalize to conventional empty-set macros.'},
]

# Complete audit readings. Categories reflect source content, not editorial normalization.
box('b01','handwritten number','page18',r'\mspage{18}','Both digits of the main page number.')
box('b02','C/H word difference','opening',r'On suppose, pour $i<j<k$','Complete opening, including the absent H terminal comma.')
box('b03','margin note|C/H word difference','condition_b',r'\margin{Condition \textcircled{b}}','Full condition heading and circled letter.')
display28=tex[tex.index(r'\['):tex.index(r'\]')+2]
box('b04','handwritten number','display28',display28,'Complete (28) equality and a priori inclusion, both digits and the edge-ending parenthesis.')
mainex=r"ce qui signifie aussi que $\forall z\in\Sigma_*$ au dessus d'un $k\in I$ (i.e. $z\in\Sigma_k$), l'hom. d'ens."
box('b05','C/H word difference','au_dessus_hom',mainex,'Complete two-line explanation, including au dessus, d’un and l’hom. d’ens.')
box('b06','margin note|insertion|C/H word difference|low-confidence departure','margin_b',mb_f,'Whole upper diagonal note, including all corrected attachments, the verbal equality and the full intersection formula. The phantom insertion is absent.')
firstmaps=r'\['+'\n'+r'\Sigma_*\longrightarrow I'+'\n'+r'\]'+'\n'+r'(\inserted{qui par \textcircled{a}} induit une application'+'\n'+r'\['+'\n'+r'\Sigma_{*\leq z}\hookrightarrow I_{\leq k}'+'\n'+r'\]'
box('b07','insertion|doubt formula|handwritten number|C/H word difference|low-confidence departure','first_maps',firstmaps,'Complete first two maps and inserted qui par circled a; includes the original a/1-degree doubt and its number candidate.')
box('b08','margin note|C/H word difference|low-confidence departure',[309,638,515,708],r'\margin{\uline{injection}}','The complete horizontal underlined annotation, independently of the diagonal note.')
display29=r'\['+'\n'+r'(29)\qquad (\Sigma_*)_{\leq z}\hookrightarrow I_{\leq k}'+'\n'+r'\]'
box('b09','handwritten number','display29',display29,'Complete (29) map and both formula-label digits.')
order=r"\margin{l'ordre de $(\Sigma_*)_z$ est \uline{induit} par celui de $I_{\leq k}$}"
box('b10','margin note|C/H word difference','order_note',order,'Whole right order note, including its bare z subscript, underline and lack of terminal stop.')
nomin=r"On suppose de plus que si $i,j\leq k$ n'ont pas de minorant \inserted{dans $I$}, alors"
box('b11','insertion|C/H word difference','no_minorant',nomin,'Complete clause and the dans I insertion with its attachment after minorant.')
box('b12','C/H word difference','empty_main',r'\['+'\n'+r'\Sigma_{ik}\cap\Sigma_{jk}=\phi'+'\n'+r'\]','Whole emptiness equation, retaining the phi-like glyph.')
box('b13','margin note|C/H word difference|low-confidence departure','condition_c',r'\margin{Condition \textcircled{c} Gros}','Full heading, circled c and resolved Gros.')
paren=r'(si $i,j$ ont un minorant $l$, alors'+'\n'+r'\['+'\n'+r'\Sigma_{ik}\cap\Sigma_{jk}\subset\ )'+'\n'+r'\]'
box('b14','C/H word difference','minorant_paren',paren,'Complete parenthetical wording and unfinished formula, including the genuinely blank target.')
box('b15','margin note|C/H word difference|low-confidence departure','margin_c',mc_f,'Whole middle diagonal note, literal ayant = élément final and complete phi-valued intersection formula.')
box('b16','margin note|insertion|struck passage|doubt formula|C/H word difference|low-confidence departure','margin_bc_full',mbc_f,'Whole right note: complete upper family, finie insertion, both cancelled/live quantified groups, every nested alpha and the complete intersection/union alternatives.')
fixed=r'On suppose enfin que le système des $\Sigma_{ik}$ (pour $k$ fixé, \inserted{$i\in I_{<k}$}), qui sont des sous-espaces'
box('b17','insertion',[300,1540,1662,1760],fixed,'Full fixed-k parenthesis and the i in I_<k insertion with its strict inequality; the bounds include the complete surrounding two-line main passage.')
box('b18','struck passage|C/H word difference','bord_ts',r'\deleted{bord} bord-ts de $\Sigma_k$','The complete cancelled bord, live abbreviated replacement and following object.')
box('b19','margin note|C/H word difference','condition_d',r'\margin{Condition \textcircled{d}}','Full lower condition heading and circled letter.')
box('b20','margin note|insertion|doubt formula|C/H word difference|low-confidence departure','margin_d',md_f,'Whole lower diagonal note and full inclusion/cofinal/raised-formula context. All doubtful fragments remain visible in the proposed reading; borrowed horizontal main words are excluded.')
ref=r'ce qui signifie (grâce : (30)\inserted{et 28,}) que si'
box('b21','insertion|handwritten number|C/H word difference|low-confidence departure',[303,1765,1453,2007],ref,'Complete reference clause, all four digits in 30 and 28, the colon and every stroke of the raised addition, its comma and attachment leader.')
flagline=r'\unsure{on a} un drapeau $'+flag_f+r'$, alors les'
box('b22','doubt formula|handwritten number|C/H word difference|low-confidence departure',[303,1960,1545,2115],flagline,'The complete flag tuple and adjacent wording, including full word descenders, its first small digit and both continuation dashes.')
listline=r'$'+list_f+r'$ dans $\Sigma_k$ sont des sous-ens \unsure{bordants|bord-ts}'
box('b23','doubt formula|handwritten number|C/H word difference|low-confidence departure','sigma_list',listline,'The whole three-term list, both doubtful small digits, each comma and the point-and-dash continuation, plus the abbreviated noun and uncertain final adjective.')
finalline=r'qui se coupent \uline{transversalement} le long de $'+final_eq+r'$.'
box('b24','doubt formula|handwritten number|C/H word difference|low-confidence departure',[350,2125,1650,2340],finalline,'Complete equality across its two source lines, including all upper letter strokes, the doubtful initial digit, single dash, comma before k and terminal period.')
box('b25','margin note|handwritten number','folio44',r'\margin{44}','Both thin foliation digits, kept separate from the main number 18.')

def norm(s):return re.sub(r'\s+',' ',s).strip()
issues=[]
for i,r in enumerate(d['changes'],1):
    if norm(r['final']) not in norm(tex):issues.append(f'change {i} final missing: {r["place"]}')
    if r['C']!='[absent]' and norm(r['C']) not in norm(C):issues.append(f'change {i} C missing: {r["place"]}')
    if r['H']!='[absent]' and norm(r['H']) not in norm(H):issues.append(f'change {i} H missing: {r["place"]}')
    if not (BASE/'crops'/r['crop']).is_file():issues.append(f'change {i} crop missing')
    if not (r['change_C'] or r['change_H']):issues.append(f'change {i} empty accounting')
for i,r in enumerate(d['marks'],1):
    if norm(r['context']) not in norm(C):issues.append(f'mark {i} context missing')
    if norm(r['reading']) not in norm(tex):issues.append(f'mark {i} reading missing')
    if not (BASE/'crops'/r['crop']).is_file():issues.append(f'mark {i} crop missing')
for r in d['second_boxes']:
    if norm(r['reading']) not in norm(tex):issues.append(f'{r["box"]} reading missing')
    a,b,c,e=r['coords']
    if not (0<=a<c<=1682 and 0<=b<e<=2360):issues.append(f'{r["box"]} bounds invalid')
orig=[]
for m in re.finditer(r'\\(?:unsure|illegible)\{',C):
    j=m.end();depth=1
    while depth:
        if C[j]=='{':depth+=1
        elif C[j]=='}':depth-=1
        j+=1
    orig.append(C[m.start():j])
if orig!=[r['mark'] for r in d['marks']]:issues.append('Original mark coverage/order mismatch')
depth=0
for m in re.finditer(r'(?<!\\)[{}]',tex):
    depth+=1 if m.group()=='{' else -1
    if depth<0:issues.append('Unmatched early closing brace')
if depth:issues.append('Unbalanced TeX braces')
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for r in d['changes']:
    if r['kind'] not in allowed:issues.append('Invalid collation kind '+r['kind'])
if any(ord(c)<32 and c not in '\n\r\t' for c in tex):issues.append('Unexpected TeX control character')
(BASE/'reader_returns/150_scan045.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(d['changes']),change_C=sum(r['change_C'] for r in d['changes']),change_H=sum(r['change_H'] for r in d['changes']),marks=len(d['marks']),resolved_marks=sum(r['decision']!='undecided' for r in d['marks']),inventory=len(d['inventory']),doubts=len(d['doubts']),second_boxes=len(d['second_boxes']),crop_places=24,crop_images=len(xy),issues=issues),ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
