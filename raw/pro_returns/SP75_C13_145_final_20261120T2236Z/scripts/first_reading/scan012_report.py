from pathlib import Path
import json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=root/'edition'/'reader_reports'
boxes={
'cancelled_relation':[515,605,895,720],
'cancelled_subgroups':[275,705,1610,830],
'cancelled_image_formula':[510,825,985,935],
'cancelled_deja_int_modulo':[260,950,1550,1080],
'cancelled_multiplication':[260,1080,1610,1200],
'cancelled_donnee':[265,1200,945,1320],
'des_plus_jolis':[345,1395,825,1500],
'sous_prefix':[1160,1330,1640,1480],
's3_extension':[420,1495,580,1620],
'aut_lac_insertion':[690,1430,1245,1605],
'sigma_rho_and_struck_example':[1190,1590,1635,1725],
'groupes_ramification':[285,1810,1640,1935],
'canoniqt_isomorphes':[285,1920,1510,2050],
'final_autom_insertion':[1000,2180,1658,2285],
'final_classe_mod':[310,2265,1065,2351],
'final_carre_insertion':[1045,2255,1658,2351],
'manuscript_number_eleven':[25,2260,145,2351]
}
def crop(n):return 'crops/145_scan012_'+n+'.png'
tex=r'''\scanpage{12}
\[
\sigma_\infty(g^{-1})=l_0^\beta g l_1^\beta.
\]
Ce qui détermine $\beta$ de façon unique en fonction de $g$.

\deleted{Appliquant la relation fondamentale
\[
u\unsure{g|\rho}=\operatorname{int}(g)\rho u
\]
à $L_0$, on trouve, puisque $u(L_0)=L_0$, $\rho(L_0)=L_1$
\[
u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})
\]
et ceci détermine déjà \deleted{\unsure{$\operatorname{int}(g)$}} modulo multiplication à droite par un él\textsuperscript{t} de $L_1$, \unsure{par|près} le donnée de $u$}

On a des plus jolis générateurs de \unsure{la|l'} \inserted{sous-}extension de $\unsure{\mathfrak S_3|\mathcal S_3}$ par $\pi$ \inserted{dans $\operatorname{Aut}_{\mathrm{lac}}(\pi)$,} que les six générateurs $l_0,l_1,l_\infty,\sigma_0,\sigma_1,\sigma_\infty$ (donnant $\rho$ par $\sigma_0\sigma_1=l_1^{-1}\rho$ \deleted{\unsure{p.ex.}} i.e. $\rho=\sigma_0\sigma_1l_1$ p.ex.), en introduisant les groupes de ramification dans les pts $0,1,\infty$, qui sont canoniq\textsuperscript{t} isomorphes à $\widehat{\mathbb Z}$,
On définira donc $\varepsilon_0,\varepsilon_1,\varepsilon_\infty$ par les relations
\[
\varepsilon_0^2=l_0,\qquad\varepsilon_1^2=l_1,\qquad\varepsilon_\infty^2=l_\infty
\]
et plus précisément, $\varepsilon_i$ sera l'unique \deleted{\unsure{él\textsuperscript{t}}} \inserted{autom.} dans la classe mod $\pi$ des $\sigma_i$, \deleted{et} qui fixe $l_i$ et est \deleted{\unsure{de|$\sigma$}} \inserted{\unsure{de carré $l_i$}}
\mspage{11}
'''
(out/'145_scan012.tex').write_text(tex,encoding='utf-8')
changes=[]
def ch(place,C,H,final,ink,confidence,kind,c,h,marked,n,errs,math=''):
 changes.append(dict(id=f's012-{len(changes)+1:02d}',place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c,h_changed=h,marked_in_H=marked,crop=crop(n),box=boxes[n],error_category=errs,math_consequence=math))
ch('First display inside the large cancelled paragraph',r'u\rho=\operatorname{int}(g)\rho u',r'ug = \mathrm{int}(g)\, \uncertain{\rho}\, u',r'u\unsure{g|\rho}=\operatorname{int}(g)\rho u',
'The left product has a small rounded head to the right and a long right-hand descender ending in a leftward hook, like the g inside int(g). The following rho has its long stem to the left of its loop. A large cancellation stroke crosses the initial u. The left letter therefore favours g, but rho is retained as an alternative. The right rho is plain.', 'medium','misread symbol or index',True,False,'yes','cancelled_relation',[1],'The written left factor may be g rather than the rho expected from the name of the relation; no mathematical correction is silently made.')
ch('Cancelled line beginning à L_0',r'à $L_0$, on trouve, puisque $u(L_0)=L_0$, $\rho(L_0)=L_1$',r'à $l_0$, on trouve, puisque $u(l_0) = l_0$, $\rho(l_0) = l_1$,',r'à $L_0$, on trouve, puisque $u(L_0)=L_0$, $\rho(L_0)=L_1$',
'All five L forms have an upright stem and angular horizontal foot; none has the loop of the later lower-case l. The last numeral is a separate vertical 1. There is no visible comma after the last L_1.', 'high','misread symbol or index',False,True,'no','cancelled_subgroups',[1,10],'Retains capital subgroup notation in the cancelled argument.')
ch('Second cancelled display',r'u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})',r'u(l_1) = \mathrm{int}(g)(l_1)',r'u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})',
'Both L forms have straight stems and feet. The left subscript 1 is separate and plain. The right subscript is densely overwritten; its ink does not securely distinguish 1 from 0.', 'medium','misread symbol or index',False,True,'no','cancelled_image_formula',[1],'The capital L forms are secure; the argument index remains unresolved.')
ch('Cancelled line after et ceci détermine',r'déjà \deleted{\unsure{$\operatorname{int}(g)$}} modulo',r'\ill{}} \struck{\ill{}} \struck{une',r'déjà \deleted{\unsure{$\operatorname{int}(g)$}} modulo',
'The ascender and descending j of déjà are distinct, despite a large diagonal cancellation. A smaller horizontal cancellation crosses the probable int(g), so that expression remains doubtful. The following m-o-d-u-l-o sequence is legible; it is not une.', 'high','readable ink left as \\ill{}',False,True,'yes','cancelled_deja_int_modulo',[2,5,7,9],'Restores the stated modulo qualification without resolving the nested cancelled expression.')
ch('Cancelled line multiplication à droite',r'multiplication à droite par un él\textsuperscript{t} de $L_1$,',r'\uncertain{multiplication} à droite par une \uncertain{puissance} de $l_1$,',r'multiplication à droite par un él\textsuperscript{t} de $L_1$,',
'The long looped l and p in multiplication and the d-r-o-i-t-e strokes in droite remain readable across the large crosses. After par is un, followed by accented é, tall l, and a raised t; there is no letter sequence for puissance. The final L has a straight foot and a clear 1, followed by a comma.', 'high','misread word',False,True,'yes','cancelled_multiplication',[1,2,8],'The manuscript speaks of an element of L_1; puissance is not present.')
ch('Last line of the cancelled paragraph, before donnée',r'\unsure{par} la donnée de $u$',r'près, le donnée de $u$',r'\unsure{par|près} le donnée de $u$',
'The first word is overwritten, with a descending initial trace and only part of the final connected strokes recoverable; par is favoured but près cannot be excluded. The following article is clearly l plus a small looped e. No separate comma is visible between the overwritten word and le.', 'low','misread word',True,True,'no','cancelled_donnee',[2,10],'Preserves the authorial wording le donnée; the obscured preposition remains uncertain.')
ch('End of the cancelled paragraph',r'$u$.',r'$u$',r'$u$',
'The final u is followed by blank paper within the saved crop; no terminal dot is visible.', 'high','text not on the page',True,False,'no','cancelled_donnee',[9,10])
ch('Opening of the live lower paragraph',r'\unsure{des|de}',r'de',r'des',
'After the looped d and compressed e is a distinct small downward terminal hook for s, comparable to the final s in plus nearby.', 'high','misread word',False,True,'no','des_plus_jolis',[2])
ch('Article and inserted prefix before extension',r"de \inserted{\unsure{sous-|sur}} l'extension",r'de \add{la} \uncertain{sous-}extension',r"de \unsure{la|l'} \inserted{sous-}extension",
'The guide rises from immediately before extension, after the article, to the prefix sous-. The baseline article has an a-shaped body after l and a surviving apostrophe-like stroke above it; the correction sequence is indeterminate. The prefix itself has the initial s-o and compressed u-s sequence followed by a separate hyphen. It is an insertion above the line, whereas the article is on the baseline.', 'medium','insertion or placement',True,True,'yes','sous_prefix',[2,6],'The insertion belongs to extension, after the article; neither a corrected article sequence nor a grammatical normalization is imposed.')
ch('Interlinear insertion after par π',r'\inserted{dans $\operatorname{Aut}_{\mathrm{lac}}(\pi)$,}',r'dans $\mathrm{Autext}(\pi)$,',r'\inserted{dans $\operatorname{Aut}_{\mathrm{lac}}(\pi)$,}',
'The interlinear word is dans, followed by Aut and visibly lowered l-a-c: a tall looped l, small a, and open c. A comma follows the closing parenthesis. The guide starts between π and que, after the phrase de S_3 par π, not immediately after extension.', 'high','insertion or placement',False,True,'no','aut_lac_insertion',[1,2,6],'Restores the locally written Aut_lac and the attachment of its ambient-group qualification.')
ch('First live sigma-rho identity',r'\sigma_0\sigma_1=l_1^{-1}\rho',r'\sigma_0\sigma_1 = l_1\rho',r'\sigma_0\sigma_1=l_1^{-1}\rho',
'Above l are a separate horizontal minus and a small slanting 1; below l is the full dark subscript 1. The following rho is separate.', 'high','omission',False,True,'no','sigma_rho_and_struck_example',[1,3],'Restores the inverse exponent in the written relation.')
ch('Example abbreviation after first live sigma-rho identity',r'\deleted{\unsure{p.ex.}}',r'\uncertain{par ex.}',r'\deleted{\unsure{p.ex.}}',
'A horizontal cancellation crosses the short abbreviation after rho. Its p descender is visible, but the following small letters and stops are partly merged with the strike. There is no full par. Retain the p.ex. proposal as doubtful and deleted.', 'medium','deletion state',False,True,'yes','sigma_rho_and_struck_example',[7,8],'The example abbreviation is cancelled, before the uncancelled i.e. reformulation.')
ch('Line beginning groupes de ramification',r'groupes de ramification',r'\ill{} de \uncertain{ramification}',r'groupes de ramification',
'The first word has the descending loop of g, then r-o-u-p-e-s, with the p extending below the line. The next word has r-a-m-i-f-i-c-a-t-i-o-n, including the long f; both words are readable.', 'high','readable ink left as \\ill{}',False,True,'yes','groupes_ramification',[2,5])
ch('Clause after the point list 0,1,∞',r'qui sont canoniq\textsuperscript{t} isomorphes à $\widehat{\mathbb Z}$',r'qui \ill{} \uncertain{conjugués} \ill{} : $\hat{\mathbb{Z}}$',r'qui sont canoniq\textsuperscript{t} isomorphes à $\widehat{\mathbb Z}$',
'After qui is compressed sont. The next word has c-a-n-o-n-i-q and a raised terminal t, followed by the readable i-s-o-m-o-r-p-h-e-s sequence. Before the hatted Z there is an accented à written with small separated strokes, not a colon. No conjugués sequence occurs.', 'high','misread word',False,True,'yes','canoniqt_isomorphes',[2,5,8],'Restores the stated canonical isomorphisms to the hatted integer group.')
ch('Punctuation after the hatted Z',r'$\widehat{\mathbb Z}$.',r'$\hat{\mathbb{Z}}$,',r'$\widehat{\mathbb Z}$,',
'The punctuation is a curved downward comma to the right of the hatted Z, not a dot.', 'high','other',True,False,'no','canoniqt_isomorphes',[10])
ch('Replacement above the word after l’unique',r'\deleted{\unsure{él\textsuperscript{t}}} \inserted{autom.}',r'\struck{\ill{}} \ill{}',r'\deleted{\unsure{él\textsuperscript{t}}} \inserted{autom.}',
'The upper insertion has a-u-t-o-m and a terminal dot. The baseline word is crossed horizontally; accented é, l and a possible raised t can be proposed, but the strike and superposed ascenders prevent a fully certain reading of all letters.', 'high','readable ink left as \\ill{}',False,True,'yes','final_autom_insertion',[5,6,7,8],'The replacement calls ε_i an automorphism, in the abbreviated form autom.; the cancelled earlier noun remains doubtful.')
ch('Last baseline, after dans',r'la classe mod $\pi$',r'le \ill{} $\pi$',r'la classe mod $\pi$',
'The article shows a looped l followed by the small low a-body. The next word has the initial c and tall l, then the connected a-s-s-e strokes. The following m-o-d is present before π. The two looped letters in la are distinct from the le seen in the cancelled donnée line.', 'high','readable ink left as \\ill{}',False,True,'yes','final_classe_mod',[2,5,8],'Restores the class modulo π qualification.')
ch('Last baseline, immediately before σ_i',r'des $\sigma_i$',r'de $\sigma_i$',r'des $\sigma_i$',
'The small terminal descending hook after d-e is present before the separated sigma, matching des in the live paragraph opening.', 'high','misread word',False,True,'no','final_classe_mod',[2])
ch('Last baseline, after σ_i comma',r'\deleted{et}',r'et',r'\deleted{et}',
'The e and tall t are crossed by a short dark horizontal stroke, distinct from the following uncancelled qui.', 'high','deletion state',False,True,'no','final_carre_insertion',[7])
ch('End of last baseline and lower interlinear replacement',r'\deleted{\unsure{de|$\sigma$}} \inserted{\unsure{de carré $l_i$}}',r'\ill{}',r'\deleted{\unsure{de|$\sigma$}} \inserted{\unsure{de carré $l_i$}}',
'The terminal baseline traces are struck and retain the ambiguity between de and sigma. Below are readable de and the main strokes of carré, then a looped l with a small right-lower index at the page edge. The edge and compressed final strokes leave the complete phrase, particularly the index, uncertain. The placement below the line is visible.', 'medium','insertion or placement',False,True,'yes','final_carre_insertion',[1,5,6,7],'The replacement appears to impose the square l_i, but remains uncertain at the clipped edge.')
ch('Lower-left handwritten page number',r'\mspage{11}',r'',r'\mspage{11}',
'Two separate tall angled strokes, each with an initial upstroke and descending main stroke, clearly form 11 in the lower-left margin.', 'high','omission',False,True,'no','manuscript_number_eleven',[3],'This is manuscript pagination, independent of the editorial scan identifier 12.')

def decision(id,dec,reading,ink,n,conf):
 return dict(id=id,decision=dec,reading=reading,ink=ink,crop=crop(n),box=boxes[n],confidence=conf)
decisions=[
 decision('M0798','first','des','A separate final downhook follows the compressed e; compare the s in plus immediately to its right.','des_plus_jolis','high'),
 decision('M0799','first','sous-','The raised prefix has s-o followed by compressed u-s, and a separate hyphen. The guide anchors it after the article, before extension.','sous_prefix','high'),
 decision('M0800','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The large ornamental S has an enclosing outer loop and an internal loop, but this isolated instance does not decisively select a modern Fraktur versus calligraphic font. The subscript 3 is clear.','s3_extension','medium'),
 decision('M0801','undecided',r'\unsure{de carré $l_i$}','The lower insertion supports de carré and a looped l, but the terminal small index lies at the page edge and is insufficiently distinct for an entirely certain phrase.','final_carre_insertion','medium')
]
unlisted=[
 decision('U012-01','undecided',r'\unsure{1|0}','The final subscript in int(g)(L_?) is densely overwritten and cannot be resolved from its surviving outlines.','cancelled_image_formula','low'),
 decision('U012-02','undecided',r'\unsure{$\operatorname{int}(g)$}','The shorter horizontal cancellation crosses the small letters of the proposed int(g); not every letter is plain.','cancelled_deja_int_modulo','low'),
 decision('U012-03','undecided',r'\unsure{par|près}','The word is overwritten; a descender and partial final connected strokes favour par but do not exclude près.','cancelled_donnee','low'),
 decision('U012-04','undecided',r'\unsure{p.ex.}','The p descender is clear, but the following letters and stops merge with the cancellation; the entire abbreviation is not plain.','sigma_rho_and_struck_example','medium'),
 decision('U012-05','undecided',r'\unsure{él\textsuperscript{t}}','Accented é, l and a possible raised t remain visible below the autom. insertion, but the strike and overlapping ascenders prevent resolving every character.','final_autom_insertion','medium'),
 decision('U012-06','undecided',r'\unsure{de|$\sigma$}','The short terminal cancelled shape remains compatible with de or a sigma-like sign.','final_carre_insertion','low')
]
doubts=[
 dict(place='Cancelled relation, first product',reading=r'u\unsure{g|\rho}',alternatives=[r'ug',r'u\rho'],confidence='medium',reason='The head and hooked descender favour g; the cancelled strokes do not justify discarding rho. Root independently agreed with g first.'),
 dict(place='Cancelled image formula, last index',reading=r'L_{\unsure{1|0}}',alternatives=[r'L_1',r'L_0'],confidence='low',reason='The final index is densely blackened.'),
 dict(place='Nested cancellation after déjà',reading=r'\deleted{\unsure{$\operatorname{int}(g)$}}',alternatives=[r'$\operatorname{int}(g)$'],confidence='low',reason='The strike overlaps several of the proposed small letters.'),
 dict(place='Last line of cancelled paragraph, first word',reading=r'\unsure{par|près}',alternatives=['par','près'],confidence='low',reason='Overwriting prevents recovery of the whole word; retain the grammatical irregularity le donnée separately.'),
 dict(place='Article before inserted sous-',reading=r"\unsure{la|l'}",alternatives=['la',"l'"],confidence='medium',reason='An a-shaped baseline body and an apostrophe-like upper stroke coexist. The correction sequence cannot be established.'),
 dict(place='Ornamental S_3 in extension phrase',reading=r'\unsure{\mathfrak S_3|\mathcal S_3}',alternatives=[r'\mathfrak S_3',r'\mathcal S_3'],confidence='medium',reason='The ornamental letter does not securely distinguish modern font choices in this local instance.'),
 dict(place='Cancelled abbreviation after first sigma-rho identity',reading=r'\deleted{\unsure{p.ex.}}',alternatives=['p.ex.'],confidence='medium',reason='The strike crosses the letters and stops after p.'),
 dict(place='Cancelled noun below autom.',reading=r'\deleted{\unsure{él\textsuperscript{t}}}',alternatives=[r'él\textsuperscript{t}'],confidence='medium',reason='Individual upper and baseline strokes overlap the cancellation and replacement.'),
 dict(place='Cancelled terminal baseline word/sign',reading=r'\deleted{\unsure{de|$\sigma$}}',alternatives=['de',r'$\sigma$'],confidence='low',reason='The short struck shape is not sufficiently resolved.'),
 dict(place='Insertion at bottom edge',reading=r'\inserted{\unsure{de carré $l_i$}}',alternatives=[r'de carré $l_i$'],confidence='medium',reason='The words are substantially supported, but the compressed final index at the edge remains uncertain.')
]
inventory=[]
def inv(kind,pos,words,box):
 inventory.append(dict(element=f'I{len(inventory)+1:02d}',kind=kind,position=pos,first_words_or_objects=words,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('display','top',r'\sigma_\infty(g^{-1})=l_0^\beta g l_1^\beta.',[260,45,1640,225])
inv('text','below opening display','Ce qui détermine β de façon unique en fonction de g.',[265,225,1620,450])
inv('deletion','central block, cancelled by two large crosses','Appliquant la relation fondamentale … le donnée de u',[250,440,1640,1335])
inv('display','first display within central cancellation',r'u\unsure{g|\rho}=\operatorname{int}(g)\rho u',boxes['cancelled_relation'])
inv('text','middle of central cancellation',r'à L_0, on trouve, puisque … \rho(L_0)=L_1',boxes['cancelled_subgroups'])
inv('display','second display within central cancellation',r'u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})',boxes['cancelled_image_formula'])
inv('deletion','short nested cancellation after déjà',r'\unsure{$\operatorname{int}(g)$}',[1040,950,1320,1080])
inv('text','lower live paragraph','On a des plus jolis générateurs … isomorphes à Z-hat,',[285,1330,1640,2050])
inv('insertion','above extension, guide after the article','sous-',boxes['sous_prefix'])
inv('insertion','above par π … que les six générateurs',r'dans $\operatorname{Aut}_{\mathrm{lac}}(\pi)$,',boxes['aut_lac_insertion'])
inv('deletion','after first live sigma-rho identity',r'\unsure{p.ex.}',[1505,1590,1635,1725])
inv('text','final defining paragraph','On définira donc ε_0, ε_1, ε_∞ … de carré l_i',[285,2030,1658,2351])
inv('display','within final defining paragraph',r'\varepsilon_0^2=l_0,\quad\varepsilon_1^2=l_1,\quad\varepsilon_\infty^2=l_\infty',[285,2115,1640,2210])
inv('deletion','after l’unique, below autom.',r'\unsure{él\textsuperscript{t}}',[1440,2210,1658,2285])
inv('insertion','above cancelled noun after l’unique','autom.',[1440,2180,1658,2250])
inv('deletion','last baseline after σ_i comma','et',[1060,2265,1140,2325])
inv('deletion','last baseline after et est',r'\unsure{de|$\sigma$}',[1560,2265,1658,2320])
inv('insertion','below final baseline, at page edge',r'\unsure{de carré $l_i$}',[1450,2300,1658,2351])
inv('margin note','lower-left pagination','11',boxes['manuscript_number_eleven'])
second=[]
def sb(reason,box,reading):second.append(dict(box=f'B{len(second)+1:02d}',kind=reason,coords=box,reading=reading))
sb('complete opening formula containing handwritten indices and inverse exponent',[260,45,1640,225],r'\[\sigma_\infty(g^{-1})=l_0^\beta g l_1^\beta.\]')
sb('beginning of crossed-out paragraph',[260,465,1620,600],r'\deleted{Appliquant la relation fondamentale}')
sb('cancelled relation; new symbol doubt',boxes['cancelled_relation'],r'\deleted{\[u\unsure{g|\rho}=\operatorname{int}(g)\rho u\]}')
sb('cancelled line; uppercase/lowercase disagreement and every numerical subscript',boxes['cancelled_subgroups'],r'\deleted{à $L_0$, on trouve, puisque $u(L_0)=L_0$, $\rho(L_0)=L_1$}')
sb('complete cancelled display; overwritten index',boxes['cancelled_image_formula'],r'\deleted{\[u(L_1)=\operatorname{int}(g)(L_{\unsure{1|0}})\]}')
sb('cancelled prose, nested deletion, and lexical recovery',boxes['cancelled_deja_int_modulo'],r'\deleted{et ceci détermine déjà \deleted{\unsure{$\operatorname{int}(g)$}} modulo}')
sb('cancelled prose, abbreviation, subgroup index, and lexical disagreements',boxes['cancelled_multiplication'],r'\deleted{multiplication à droite par un él\textsuperscript{t} de $L_1$,}')
sb('cancelled final line; overwritten word and authorial article slip',boxes['cancelled_donnee'],r'\deleted{\unsure{par|près} le donnée de $u$}')
sb('des disagreement, uncertain article, and interlinear prefix insertion',[330,1330,1640,1480],r"On a des plus jolis générateurs de \unsure{la|l'} \inserted{sous-}extension")
sb('ornamental S_3 with numeral, Aut_lac insertion, and its placement',[285,1465,1640,1625],r'de $\unsure{\mathfrak S_3|\mathcal S_3}$ par $\pi$ \inserted{dans $\operatorname{Aut}_{\mathrm{lac}}(\pi)$,} que les six générateurs')
sb('full six-generator list and first identity, all numbers, deleted abbreviation',[285,1590,1640,1725],r'$l_0,l_1,l_\infty,\sigma_0,\sigma_1,\sigma_\infty$ (donnant $\rho$ par $\sigma_0\sigma_1=l_1^{-1}\rho$ \deleted{\unsure{p.ex.}}')
sb('complete equivalent rho identity with every numerical index',[285,1720,1640,1825],r'i.e. $\rho=\sigma_0\sigma_1l_1$ p.ex.), en introduisant les')
sb('lexical recovery and complete handwritten point list',boxes['groupes_ramification'],r'groupes de ramification dans les pts $0,1,\infty$,')
sb('lexical recovery, abbreviation, and comma correction',boxes['canoniqt_isomorphes'],r'qui sont canoniq\textsuperscript{t} isomorphes à $\widehat{\mathbb Z}$,')
sb('complete inline epsilon list with numerical indices',[285,2030,1640,2130],r'On définira donc $\varepsilon_0,\varepsilon_1,\varepsilon_\infty$ par les relations')
sb('complete square-relation display with all numerical indices and exponents',[285,2115,1640,2210],r'\[\varepsilon_0^2=l_0,\qquad\varepsilon_1^2=l_1,\qquad\varepsilon_\infty^2=l_\infty\]')
sb('full defining line, cancelled noun, and inserted replacement',[285,2180,1658,2285],r"et plus précisément, $\varepsilon_i$ sera l'unique \deleted{\unsure{él\textsuperscript{t}}} \inserted{autom.}")
sb('last line with lexical disagreements, both deletions, and lower insertion',[310,2255,1658,2351],r'dans la classe mod $\pi$ des $\sigma_i$, \deleted{et} qui fixe $l_i$ et est \deleted{\unsure{de|$\sigma$}} \inserted{\unsure{de carré $l_i$}}')
sb('handwritten page number, omitted from H',boxes['manuscript_number_eleven'],r'\mspage{11}')
coverage=[]
def dc(row,status,change=None,explanation=None):
 d=dict(row=row,status=status)
 if change:d['change_id']=f's012-{change:02d}'
 if explanation:d['explanation']=explanation
 coverage.append(d)
dc(1,'macro/editorial',explanation='The 12 is the editorial scan identifier, not manuscript pagination. The actual handwritten 11 is recorded separately in s012-21.')
dc(2,'macro/editorial',explanation='The token is the comma in H’s TeX thin-space command, not ink punctuation.')
dc(3,'macro/editorial',explanation='The token is the comma in H’s TeX thin-space command, not ink punctuation.')
dc(4,'substantive',1)
dc(5,'macro/editorial',explanation='TeX thin-space command only.')
dc(6,'macro/editorial',explanation='TeX thin-space command only.')
dc(7,'macro/editorial',explanation='Display delimiters versus inline formatting; the manuscript display is retained in the page text and inventory.')
dc(8,'substantive',2,explanation='The same clause also contains all capital-L/lower-case-l disagreements, invisible to this token diff.')
dc(9,'substantive',3,explanation='The right index uncertainty is retained; both capital L forms also differ substantively from H.')
dc(10,'substantive',4)
dc(11,'substantive',5)
dc(12,'substantive',6)
dc(13,'substantive',7,explanation='C’s terminal period is unsupported. H’s subsequent note about the crosses and le donnée is editorial, not a manuscript inscription.')
dc(14,'substantive',8)
dc(15,'substantive',9)
dc(16,'substantive',9,explanation='The token run also displaces the Aut note; its reading and attachment are separately recorded in s012-10.')
dc(17,'macro/editorial',explanation='Both witnesses propose S_3; C’s Fraktur/calligraphic font doubt is retained in decision M0800, with a crop. Certainty alone creates no change row.')
dc(18,'substantive',10)
dc(19,'substantive',11)
dc(20,'substantive',12)
dc(21,'macro/editorial',explanation='Token spacing between the subscript 1 and following l only; the complete rho identity is included in second box B12.')
dc(22,'substantive',13)
dc(23,'substantive',14,explanation='The clause’s lexical discrepancies are substantive; the quoted sous-/Autext text in H’s later note is editorial and excluded.')
dc(24,'substantive',14,explanation='The comma/period difference at the end of this same clause is separately recorded in s012-15; H’s remaining explanatory note is editorial.')
dc(25,'substantive',16)
dc(26,'substantive',17)
dc(27,'substantive',18)
dc(28,'substantive',20,explanation='The token run also contains actual handwritten page number 11, recorded separately as the H omission s012-21. The nearby deleted et, not exposed by the token diff, is s012-19.')
report=dict(scan=12,reader='/root/reader_c',lines_read=25,
 layout='Upright text leaf. Opening display and two prose lines; a central seven-line argument is cancelled by two large crosses, with a further short cancellation inside it. The lower live text has an interlinear sous- prefix, an Aut_lac note, two sigma-rho identities, point and epsilon lists, and a square-relation display. The final two lines contain autom. above a cancelled noun, a cancelled et, a final cancelled word/sign, and a lower replacement at the page edge. Handwritten 11 stands at lower left. No diagram or nontextual drawing.',
 changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
 notation=[
 'Upper-case L in the cancelled argument has an upright stem and angular foot, unlike the visibly looped lower-case l in the live formulas. This local distinction is supported in both cancelled formulas and the intervening prose.',
 'In the first cancelled relation, g is favoured on the left because of its right-hand hooked descender; the following rho has a left stem below an upper loop. The left letter remains explicitly uncertain.',
 'The interlinear ambient-group notation is Aut with a lowered lac. This observation is local to the insertion after par π.',
 'The ornamental S in S_3 has an enclosing outer loop and an inner loop. Modern Fraktur versus calligraphic font is not settled by this page.',
 'The lower-case epsilon symbols have indices 0, 1, infinity and i. The three displayed squares each visibly carry exponent 2; none is omitted from the second-reading boxes.',
 'The π forms are retained as in both witnesses; no global case rule is inferred from these unindexed instances.'
 ],
 hand=[
 'Compressed terminal s often ends in a small downward hook: des in the paragraph opening and des before σ_i are both examples, and H omits s at both places. This habit is not asserted for every s on the page.',
 'The le in the cancelled le donnée has a clear small e loop after l; it is preserved despite its grammatical irregularity.',
 'Interlinear insertion guides attach sous- after the article and the Aut_lac note after π; H’s linear order misplaces the latter and C places sous- before the article.',
 'The two large diagonal crosses cancel the central paragraph as a block; a short horizontal strike within that block separately cancels the proposed int(g). The deletion hierarchy is retained.',
 'Small horizontal cancellation strokes also cross the example abbreviation, the noun replaced by autom., et, and the terminal word/sign. These do not justify stripping uncertainty from obscured letters.'
 ],
 abbreviations=[
 dict(form=r'él\textsuperscript{t}',expansion='élément',place='cancelled multiplication clause; a separately cancelled uncertain instance below autom.'),
 dict(form='p.ex.',expansion='par exemple',place='uncertain cancelled occurrence after the first sigma-rho identity; uncancelled occurrence after the i.e. reformulation'),
 dict(form='i.e.',expansion='id est',place='before the reformulated rho identity'),
 dict(form='pts',expansion='points',place='ramification point list'),
 dict(form=r'canoniq\textsuperscript{t}',expansion='canoniquement',place='isomorphes à the hatted integer group'),
 dict(form='autom.',expansion='automorphisme',place='insertion above the cancelled noun after l’unique'),
 dict(form='mod',expansion='modulo',place='last baseline, classe mod π')
 ],
 notes=[
 'The page opens with the asserted relation σ_infinity(g^{-1}) = l_0^β g l_1^β and says that it determines β uniquely as a function of g. This is a transcription of the author’s assertion, not an independent proof.',
 'The abandoned central argument invokes a relation called fondamentale and derives an image of L_1 under u, followed by a modulo qualification involving right multiplication by an element of L_1. Its rightmost image index is blackened, and an expression after déjà is separately cancelled inside the cancelled block.',
 'The first product of the abandoned relation is g-shaped in the ink, although uρ is the mathematically expected form suggested by the surrounding discussion. That expectation was used only to articulate the alternative, not to replace the ink. Root independently reviewed the crop and concurred on u\\unsure{g|\\rho}. The surviving le donnée is an apparent authorial grammatical slip and is left unchanged. No terminal stop after u is supplied.',
 'The lower paragraph proposes more attractive generators of a sous-extension of the ornamental S_3 by π, adding dans Aut_lac(π) interlinearly. The article before extension contains both an a-shaped baseline body and an apostrophe-like upper trace; no correction sequence can be established, so la/l\' remains uncertain.',
 'The author invokes ramification groups at 0, 1, infinity and describes them as canonically isomorphic to the hatted integer group. The manuscript ends that clause with a comma. It then defines ε_0, ε_1, ε_infinity by the three square relations and begins a more precise characterization through an automorphism class modulo π, fixing l_i, with a doubtful lower insertion reading de carré l_i.',
 'No explicit authorial doubt phrase, date, or diagram occurs on this leaf. Handwritten manuscript page number 11 is in the lower-left margin and is omitted in H. The editorial scan identifier 12 is not an inscription. No mathematical verification was performed.'
 ],check_events=[],diff_coverage=coverage)
(out/'145_scan012.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Structural verification only; no TeX compilation.
assert [d['id'] for d in decisions]==['M0798','M0799','M0800','M0801']
assert len(changes)==21 and len(doubts)==10 and len(second)==19
assert [x['row'] for x in coverage]==list(range(1,29))
assert all(x['c_changed'] or x['h_changed'] for x in changes)
assert all((root/'edition'/x['crop']).is_file() for x in changes+decisions+unlisted)
assert len(set(x['box'] for x in second))==len(second)
assert all(x['sheet_kind']=='text' and x['hand']=='his hand' and x['transcribed']=='yes' for x in inventory)
print(json.dumps({'report':'145_scan012','crops':len(boxes),'changes':len(changes),'decisions':len(decisions),'unlisted_decisions':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(coverage)},ensure_ascii=False))
