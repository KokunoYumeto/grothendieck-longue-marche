from pathlib import Path
import json,csv
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=root/'edition/reader_reports'
boxes=json.loads((out/'145_scan014_crop_boxes.json').read_text())
def crop(n):return 'crops/145_scan014_'+n+'.png'
opening=r'''\[
\begin{aligned}
\varepsilon_0^2&=l_0\\
\varepsilon_1^2&=l_1\\
\varepsilon_\infty^2&=l_\infty
\end{aligned}
\]'''
sigmas=r'''\[
\begin{aligned}
\sigma_0&=\varepsilon_0\varepsilon_1^2\\
\sigma_1&=\varepsilon_1\varepsilon_\infty^2\\
\sigma_\infty&=\varepsilon_\infty\varepsilon_0^2
\end{aligned}
\]'''
system=r'''\[
\left\{\begin{aligned}
\varepsilon_0^2\varepsilon_1^2\varepsilon_\infty^2&=1\\
(\varepsilon_0\varepsilon_1^2)^2&=1\\
(\varepsilon_1\varepsilon_\infty^2)^2&=1\\
(\varepsilon_\infty\varepsilon_0^2)^2&=1
\end{aligned}\right.
\]'''
chain=r'''\deleted{\[
\rho=\sigma_0\sigma_1=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0
\]}'''
continuation=r'''\[
\begin{gathered}
\Vert\\
\deleted{\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_1}}
\end{gathered}
\]'''
replacement=r'''\inserted{\[
\sigma_0\sigma_1=l_1^{-1}\rho
\]}'''
derivation=r'''\margin{donc
\[
\begin{aligned}
\rho&=l_1\sigma_0\sigma_1\\
&=\varepsilon_1^2\varepsilon_0\varepsilon_1^2\varepsilon_1\varepsilon_\infty^2\\
&=\varepsilon_1^2\varepsilon_0\varepsilon_1^{\deleted{\unsure{2}}}\underbrace{\varepsilon_1^2\varepsilon_\infty^2}_{\varepsilon_0^{-2}}
\end{aligned}
\]}'''
cyclic=r'''\[
\begin{aligned}
\rho&=\varepsilon_1^2\varepsilon_0\varepsilon_1\varepsilon_0^{-2}\\
&=\varepsilon_\infty^2\varepsilon_1\varepsilon_\infty\varepsilon_1^{-2}\\
&=\varepsilon_0^2\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-2}:
\end{aligned}
\]'''
comment=r'''\margin{\begin{tabular}{|l}
ces relations ne\\
semblent pas conséquences\\
des autres
\end{tabular}}'''
closing=r'''Multipliant \deleted{dans} ces relations dans l'ordre inverse et écrivant $\rho^3=1$, on trouve
\[
(\varepsilon_0\varepsilon_1\varepsilon_\infty)^2=1
\]
ce qui est inquiétant, car il n'y a pas d'\unsure{élém\textsuperscript{ts}}
\mspage{13}'''
tex='\n'.join([r'\scanpage{14}','donc',opening,
 r'Ce qui redonne les $l_i$, et aussi les $\sigma_i$, \deleted{\unsure{par}} en termes des $\varepsilon_i$',
 sigmas,"D'où les relations",system,
 r'On retrouve $\rho$ \deleted{\unsure{comme}} par',chain,continuation,replacement,derivation,cyclic,comment,closing])+'\n'
(out/'145_scan014.tex').write_text(tex,encoding='utf-8')
changes=[]
def ch(place,C,H,final,ink,confidence,kind,c,h,marked,n,errs,math=''):
 changes.append(dict(id=f's014-{len(changes)+1:02d}',place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c,h_changed=h,marked_in_H=marked,crop=crop(n),box=boxes[n],error_category=errs,math_consequence=math))
ch('Opening square-relation display, ends of its first two rows',r'\varepsilon_0^2=l_0\\\varepsilon_1^2=l_1',r'\varepsilon_0^2 = l_0, \qquad \varepsilon_1^2 = l_1,',r'\varepsilon_0^2=l_0\\\varepsilon_1^2=l_1',
'The right-hand l_0 and l_1 each end their own line. The paper immediately to the right is blank: neither of H’s literal commas is written. These commas are distinct from TeX thin-space commands.', 'high','text not on the page',False,True,'no','opening_display_punctuation',[9,10])
ch('Sentence after opening display',r'Ce qui redonne',r'Ceux qui redonnent',r'Ce qui redonne',
'The initial word is a large C followed by a small looped e and its terminal sweep, without separate u or crossed x strokes. Redonne ends in a low e-like return, with no following n-t sequence or terminal t ascender.', 'high','misread word',False,True,'no','ce_qui_redonne',[2])
ch('End of first prose line, after σ_i comma',r'\deleted{par}',r'\uncertain{par}',r'\deleted{\unsure{par}}',
'A separate horizontal stroke runs through the whole small word. The long p descender is clear, while the remaining a/r strokes merge with the strike, so the proposed word is retained with doubt. H’s live state is not supported.', 'high','deletion state',False,True,'yes','struck_par',[7])
ch('Sigma-definition display, ends of first two rows',r'\sigma_0=\varepsilon_0\varepsilon_1^2\\\sigma_1=\varepsilon_1\varepsilon_\infty^2',r'\sigma_0 = \varepsilon_0\, \varepsilon_1^2, \qquad\sigma_1 = \varepsilon_1\, \varepsilon_\infty^2, \qquad',r'\sigma_0=\varepsilon_0\varepsilon_1^2\\\sigma_1=\varepsilon_1\varepsilon_\infty^2',
'The first row ends with the raised 2 and lower 1; the second with the raised 2 and infinity index. No comma follows either right-hand expression. The isolated small point low beside the left σ_1 has no syntactic attachment and is not treated as punctuation.', 'high','text not on the page',False,True,'no','sigma_first_two_punctuation',[9,10])
ch('Sigma-definition display, end of third row',r'\sigma_\infty=\varepsilon_\infty\varepsilon_0^2.',r'\sigma_\infty = \varepsilon_\infty\, \varepsilon_0^2',r'\sigma_\infty=\varepsilon_\infty\varepsilon_0^2',
'The final epsilon has a clear lower 0 and upper 2. To its right and below is blank paper; no terminal stop is written.', 'high','text not on the page',True,False,'no','sigma_definition_end',[9,10])
ch('Line introducing the recovery of rho',r'On retrouve',r'\uncertain{Pour obtenir}',r'On retrouve',
'The first word has a rounded O and a compact n. The next has the rising t within r-e-t-r-o-u-v-e and the low final e. There is no initial P or b-shaped ascender corresponding to Pour obtenir.', 'high','misread word',False,True,'yes','retrouve_comme',[2])
ch('Cancelled word between rho and par',r'\deleted{comme}',r'\struck{\ill{}}',r'\deleted{\unsure{comme}}',
'An open c begins the word, followed by low traces consistent with o-m-m-e, but the long dark cancellation hides much of the middle. Comme is a supported proposal, not a fully resolved reading.', 'medium','readable ink left as \\ill{}',False,True,'yes','retrouve_comme',[5,7])
ch('Cancelled epsilon continuation below first cancelled sigma product',r'\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_1}',r'\varepsilon_0\, \varepsilon_1^3\, \varepsilon_{\ill{}}',r'\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_1}',
'The first lower 0, next lower 1 and upper 3 are clear. The last epsilon is clear but its small lower trace is compact and partly darkened; infinity remains the leading proposal, with 1 retained. The continuation is below the first sigma product, rather than beside the full chain.', 'low','misread symbol or index',False,True,'yes','cancelled_rho_chain',[1,5,6],'The final epsilon index remains unresolved and is not supplied from the algebra.')
ch('Vertical connector between the two cancelled formulas',r'''\deleted{\[
\begin{gathered}
\Vert\\
\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_1}
\end{gathered}
\]}''',r'\struck{\varepsilon_0\, \varepsilon_1^3\, \varepsilon_{\ill{}}}',continuation,
'Two short parallel near-vertical strokes stand between the cancelled chain and the cancelled epsilon product. Neither cancellation crosses these strokes. H mentions them only in an editorial note; the diplomatic display must retain them. The lower product alone is crossed.', 'high','deletion state',True,True,'yes','cancelled_rho_chain',[3,6,7],'Preserves the visible vertical equality/connector independently of the cancellation state of its neighboring expressions.')
ch('Replacement above the cancelled rho chain',replacement,r'\sigma_0 \sigma_1 = l_1^{-1} \rho',replacement,
'The sigma relation is a separate short line directly above the cancelled chain. Its l has a lower 1 and visibly raised minus-1; rho follows. It is retained as an above-line replacement, not flattened into the right-hand calculation.', 'high','insertion or placement',False,True,'no','inserted_relation',[6])
ch('Three-line calculation in the right margin',derivation,r'''\text{donc} \qquad
\rho = l_1 \sigma_0 \sigma_1
= \varepsilon_1^2\, \varepsilon_0\, \varepsilon_1^2\, \varepsilon_1\, \varepsilon_\infty^2
= \varepsilon_1^2\, \varepsilon_0\, \varepsilon_1\, \underbrace{\varepsilon_1^2\, \varepsilon_\infty^2}_{\varepsilon_0^{-2}}''',derivation,
'Donc and the rho equation begin in the right margin, with two further equalities written below. The last two factors are grouped beneath by a horizontal brace/bracket and labelled epsilon_0 to the minus 2. The block is physically separate from the left-hand cancelled chain and replacement.', 'high','insertion or placement',False,True,'no','marginal_derivation',[6],'Preserves the marginal derivation and its grouping; no new algebraic identity is inferred.')
ch('Small cancelled exponent in last marginal equality',r'\varepsilon_1^{\deleted{\unsure{2}}}',r'\varepsilon_1',r'\varepsilon_1^{\deleted{\unsure{2}}}',
'A small dark crossed shape lies in superscript position after the epsilon_1 immediately before the underbraced factors. Its surviving bent outline is consistent with 2, but the overstrike prevents resolving the numeral. H drops the cancelled inscription entirely.', 'medium','omission',False,True,'no','marginal_derivation',[1,3,7],'Retains the cancelled exponent without assigning it to the active product.')
ch('Punctuation at end of third cyclic rho expression',r'\varepsilon_0^2\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-2}.',r'\varepsilon_0^2\, \varepsilon_\infty\, \varepsilon_0\, \varepsilon_\infty^{-2}.',r'\varepsilon_0^2\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-2}:',
'Two distinct dark round points stand to the right of the last expression, on a slight diagonal. Neither has a comma tail. Their paired form supports a colon rather than the single stop printed by both witnesses.', 'high','other',True,True,'no','cyclic_rho_display',[10])
ch('Right-margin comment beside the cyclic rho expressions',r'ces relations ne semblent pas \unsure{conséquences} des autres',r'ces relations se \uncertain{déduisent} \ill{} par \uncertain{conjugaison}\uncertain{des autres}',r'ces relations ne semblent pas conséquences des autres',
'The first line ends with n-e. The next begins s-e-m-b-l-e-n-t, with its tall central ascenders, then p-a-s. Conséquences has the c-o-n-s-é sequence, a closed q with long descending stem, and the connected u-e-n-c-e-s ending. The final line reads des autres. There are no déduisent or conjugaison letter sequences.', 'high','misread word',False,True,'yes','marginal_comment',[2,5],'Restores the author’s negative doubt about whether these relations follow from the others; H changes its sense.')
ch('Vertical separator at left of right-margin comment',r'\margin{ces relations ne semblent pas \unsure{conséquences} des autres}',r'\marginal{ces relations se \uncertain{déduisent} \ill{} par \uncertain{conjugaison}\uncertain{des autres}}',comment,
'A continuous vertical rule separates the three cyclic equalities from the three-line marginal comment. It extends below the comment. The ruled tabular inside the margin macro represents this visible separator; H’s explanatory note is not itself transcribed.', 'high','other',True,True,'yes','marginal_comment',[10])
ch('Final word at bottom edge',r"d'\unsure{élém\textsuperscript{ts}}",r"d'élément",r"d'\unsure{élém\textsuperscript{ts}}",
'After d and its apostrophe, the word has a small initial e-like curve, a tall l, and a compressed low continuation. A short raised terminal hook and sweep support an abbreviated ending, but do not securely distinguish the complete raised ts sequence. The full expanded élément is not plainly written. C’s abbreviated proposal remains doubtful.', 'medium','abbreviation expanded or spelling modernised',False,True,'no','final_abbreviation',[2,8],'Preserves the uncertain abbreviated form, including uncertainty about its plural ending.')
ch('Lower-left handwritten pagination',r'\mspage{13}',r'',r'\mspage{13}',
'A tall angled 1 is followed by a clear two-bowed 3. The number stands separately at lower left.', 'high','omission',False,True,'no','manuscript_number_thirteen',[3],'Actual manuscript page number 13 is distinct from the editorial scan identifier 14.')

def dec(id,decision,reading,ink,n,confidence):
 return dict(id=id,decision=decision,reading=reading,ink=ink,crop=crop(n),box=boxes[n],confidence=confidence)
decisions=[
 dec('M0806','first','conséquences','The c-o-n-s-é-q-u-e-n-c-e-s sequence is visible, with the accent and the long q descender particularly diagnostic. The whole marginal phrase supports the negative wording ne semblent pas.','marginal_comment','high'),
 dec('M0807','undecided',r'\unsure{élém\textsuperscript{ts}}','The final word is compressed at the bottom edge. A tall l and abbreviated low body are visible, but the complete raised ending remains uncertain.','final_abbreviation','medium')
]
unlisted=[
 dec('U014-01','undecided',r'\unsure{\varepsilon_\infty|\varepsilon_1}','The epsilon base is clear. Its small final lower trace is too compact to distinguish infinity from 1 securely under the cancellation.','cancelled_rho_chain','low'),
 dec('U014-02','undecided',r'\unsure{2}','The superscript in the last marginal equality is crossed and darkened; a bent 2-like outline survives, but not all strokes are plain.','marginal_derivation','low')
]
doubts=[
 dict(place='Deleted word after σ_i in first prose line',reading=r'\deleted{\unsure{par}}',alternatives=['par'],confidence='medium',reason='The p descender is plain, but the horizontal strike obscures the middle and terminal letters. This is a new certainty qualification, not a substantive change from C’s proposed word.'),
 dict(place='Deleted word after rho in On retrouve line',reading=r'\deleted{\unsure{comme}}',alternatives=['comme'],confidence='medium',reason='The open initial c and remaining low traces support comme; several letters merge with the strike. This new doubt preserves the deletion and C’s proposed word.'),
 dict(place='Last epsilon in cancelled continuation',reading=r'\unsure{\varepsilon_\infty|\varepsilon_1}',alternatives=[r'\varepsilon_\infty',r'\varepsilon_1'],confidence='low',reason='The last lower trace is compact and not fully resolvable; no expected factor is supplied from the calculation.'),
 dict(place='Deleted superscript in marginal derivation',reading=r'\deleted{\unsure{2}}',alternatives=['2'],confidence='low',reason='The bent numeral-like trace is obscured by the cancellation.'),
 dict(place='Final word at lower edge',reading=r'\unsure{élém\textsuperscript{ts}}',alternatives=[r'élém\textsuperscript{ts}',r'élém\textsuperscript{t}'],confidence='medium',reason='The abbreviation is supported, but the small raised ending does not securely distinguish plural ts from singular t.')
]
inventory=[]
def inv(kind,pos,words,box):
 inventory.append(dict(element=f'I{len(inventory)+1:02d}',kind=kind,position=pos,first_words_or_objects=words,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('text','top-left of opening display','donc',[300,65,435,120])
inv('display','top, three stacked square relations',r'\varepsilon_0^2=l_0; \varepsilon_1^2=l_1; \varepsilon_\infty^2=l_\infty',boxes['opening_display_punctuation'])
inv('text','first two prose lines','Ce qui redonne les l_i … en termes des ε_i',[265,350,1620,585])
inv('deletion','right end of first prose line',r'\unsure{par}',boxes['struck_par'])
inv('display','three stacked definitions of sigma',r'\sigma_0=\varepsilon_0\varepsilon_1^2 …',[665,570,1030,825])
inv('text','above the four-relation system',"D'où les relations",[255,845,820,945])
inv('display','four relations with a left brace',r'\varepsilon_0^2\varepsilon_1^2\varepsilon_\infty^2=1 …',[610,940,985,1260])
inv('text','line before cancelled calculations',r'On retrouve $\rho$ … par',boxes['retrouve_comme'])
inv('deletion','between rho and par',r'\unsure{comme}',[825,1290,1075,1350])
inv('deletion','lower-middle left, cancelled chain',r'\rho=\sigma_0\sigma_1=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0',[310,1465,940,1560])
inv('display','between cancelled chain and continuation',r'\Vert',[455,1545,500,1595])
inv('deletion','beneath first sigma product',r'\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_1}',[415,1580,610,1665])
inv('insertion','above cancelled rho chain',r'\sigma_0\sigma_1=l_1^{-1}\rho',boxes['inserted_relation'])
inv('margin note','right of cancelled chain, three-line calculation',r'donc \rho=l_1\sigma_0\sigma_1 …',boxes['marginal_derivation'])
inv('deletion','small superscript in last marginal equality',r'\unsure{2}',[1425,1515,1470,1570])
inv('display','lower left, three cyclic rho expressions',r'\rho=\varepsilon_1^2\varepsilon_0\varepsilon_1\varepsilon_0^{-2} …',boxes['cyclic_rho_display'])
inv('margin note','right of cyclic rho expressions','ces relations ne semblent pas conséquences des autres',boxes['marginal_comment'])
inv('drawing','separator left of the right-margin comment','single vertical separating rule',[868,1688,908,1950])
inv('text','two lines above final equation',"Multipliant … ces relations dans l'ordre inverse et écrivant rho^3=1, on trouve",[280,1965,1540,2165])
inv('deletion','after Multipliant','dans',[680,1980,805,2055])
inv('display','bottom, before final prose line',r'(\varepsilon_0\varepsilon_1\varepsilon_\infty)^2=1',[570,2160,945,2270])
inv('text','final line at bottom edge',r"ce qui est inquiétant, car il n'y a pas d'\unsure{élém\textsuperscript{ts}}",[280,2250,1655,2350])
inv('margin note','lower-left pagination','13',boxes['manuscript_number_thirteen'])
second=[]
def sb(kind,coords,reading):second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,coords=coords,reading=reading))
sb('complete numeric opening display; H-added commas',boxes['opening_display_punctuation'],opening)
sb('Ce/Ceux and redonne/redonnent lexical disagreement',boxes['ce_qui_redonne'],'Ce qui redonne')
sb('struck par and new lexical doubt',boxes['struck_par'],r'\deleted{\unsure{par}}')
sb('complete sigma-definition display, every numerical index and exponent, all punctuation differences',[665,570,1030,825],sigmas)
sb('complete four-relation system, all handwritten numerals',[610,940,985,1260],system)
sb('On retrouve lexical disagreement and doubtful cancelled comme',boxes['retrouve_comme'],r'On retrouve $\rho$ \deleted{\unsure{comme}} par')
sb('complete cancelled chain and continuation; untouched vertical connector; all indices and exponent',boxes['cancelled_rho_chain'],chain+'\n'+continuation)
sb('inserted replacement, complete formula and numerical indices',boxes['inserted_relation'],replacement)
sb('complete marginal calculation, cancelled exponent, underbrace annotation and all numerals',boxes['marginal_derivation'],derivation)
sb('complete three-line cyclic rho display with every numerical exponent and corrected colon',boxes['cyclic_rho_display'],cyclic)
sb('complete marginal comment, resolved C doubt, lexical disagreement and vertical separator',boxes['marginal_comment'],comment)
sb('complete two-line prose passage containing deleted dans and rho cubed',[280,1965,1540,2165],r"Multipliant \deleted{dans} ces relations dans l'ordre inverse et écrivant $\rho^3=1$, on trouve")
sb('complete final numeric formula',[570,2160,945,2270],r'\[(\varepsilon_0\varepsilon_1\varepsilon_\infty)^2=1\]')
sb('final abbreviated word, C doubt and H expansion',boxes['final_abbreviation'],r", car il n'y a pas d'\unsure{élém\textsuperscript{ts}}")
sb('actual handwritten page number',boxes['manuscript_number_thirteen'],r'\mspage{13}')
coverage=[]
def dc(row,status,change=None,explanation=None):
 d=dict(row=row,status=status)
 if change:d['change_id']=f's014-{change:02d}'
 if explanation:d['explanation']=explanation
 coverage.append(d)
dc(1,'macro/editorial',explanation='14 is the editorial scan identifier. The handwritten page number 13 is separately recorded in s014-17.')
dc(2,'macro/editorial',explanation='Aligned environment versus horizontal mathematical formatting; source formulas are stacked in the transcription.')
dc(3,'substantive',1,explanation='This H comma after l_0 is literal punctuation, not a TeX thin space.')
dc(4,'substantive',1,explanation='This H comma after l_1 is literal punctuation, not a TeX thin space.')
dc(5,'macro/editorial',explanation='Aligned environment delimiter only.')
dc(6,'substantive',2)
dc(7,'substantive',2)
dc(8,'macro/editorial',explanation='Aligned environment versus horizontal mathematical formatting.')
dc(9,'macro/editorial',explanation='Comma token from H’s TeX thin-space command between the epsilon factors.')
dc(10,'substantive',4,explanation='Literal comma after the first complete right-hand expression.')
dc(11,'macro/editorial',explanation='Comma token from H’s TeX thin-space command between the epsilon factors.')
dc(12,'substantive',4,explanation='Literal comma after the second complete right-hand expression.')
dc(13,'macro/editorial',explanation='Comma token from H’s TeX thin-space command between the epsilon factors.')
dc(14,'substantive',5,explanation='C’s terminal period is unsupported; the aligned token is only an environment delimiter.')
dc(15,'macro/editorial',explanation='Equivalent braced-system environment syntax; the source’s left brace is retained.')
for n in [16,17,18,19,20]:dc(n,'macro/editorial',explanation='Comma token from H’s TeX thin-space command, not ink punctuation.')
dc(21,'macro/editorial',explanation='Environment syntax and the invisible right delimiter in C’s right-dot command; there is no source terminal period at this point.')
dc(22,'substantive',6)
dc(23,'substantive',7)
dc(24,'substantive',10,explanation='This long realigned token run also contains the right-margin calculation, s014-11, and its omitted cancelled exponent, s014-12. The above-line replacement and the cancelled original remain distinct in source order.')
dc(25,'substantive',8,explanation='The epsilon continuation is below the first cancelled sigma product; the final index remains uncertain. H’s thin-space comma tokens in this run are editorial formatting.')
dc(26,'substantive',9,explanation='The two vertical strokes are actual ink retained outside deletion. H’s prose note describing them is editorial, not transcribed.')
dc(27,'substantive',8,explanation='The continuation’s final index is the substantive local difference. This long token realignment also spans s014-9 through s014-12; H’s accompanying editorial prose is excluded.')
for n in range(28,37):dc(n,'macro/editorial',explanation='Comma token from H’s TeX thin-space command within the cyclic rho display.')
dc(37,'substantive',14)
dc(38,'substantive',15,explanation='H’s note is editorial, but it describes a real vertical separator absent from both rendered transcriptions; the source rule is reproduced and inventoried.')
dc(39,'macro/editorial',explanation='Comma token from H’s TeX thin-space command in the final formula.')
dc(40,'macro/editorial',explanation='Comma token from H’s TeX thin-space command in the final formula.')
dc(41,'substantive',16,explanation='The same token run includes handwritten page 13, separately recorded as the H omission s014-17.')
report=dict(scan=14,reader='/root/reader_c',lines_read=34,
 layout='Upright text leaf with three stacked square relations, two prose lines, three sigma definitions, and a four-relation system under a left brace. Lower down, a cancelled rho chain and cancelled epsilon continuation are linked by two untouched vertical strokes. A replacement is written above the chain; a three-line calculation occupies its right margin. Three cyclic rho expressions below have a right-hand comment separated by a vertical rule. Two further prose lines, a final equation and an incomplete bottom sentence follow. Handwritten 13 stands at lower left.',
 changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
 notation=[
 'Epsilon carries indices 0, 1, infinity and i throughout this page. Its lower-case base has two lobes; sigma has a broad upper bar and open lower hook. All agreed formulas were read locally rather than inferred from these shapes.',
 'The opening equations ε_0²=l_0, ε_1²=l_1 and ε_infinity²=l_infinity are three vertically stacked, unpunctuated rows. The sigma-definition rows are likewise unpunctuated.',
 'The rho forms have a looped head and a long descending stem. The above-line relation visibly has l_1^{-1}rho, while the right margin starts rho=l_1sigma_0sigma_1.',
 'Two parallel short vertical strokes connect the first cancelled sigma product to its cancelled epsilon expansion. Their ink is not crossed even though both neighboring expressions are cancelled.',
 'The last marginal product has a crossed superscript, provisionally 2, and an underbracket/brace grouping the final ε_1² ε_infinity² with the lower label ε_0^{-2}. The bracket’s left end has a retraced oblique stroke; no extra algebraic factor is inferred from it.',
 'The cyclic rho display ends with two dark points, read as a colon after direct crop review. This observation is local and does not impose punctuation on other displays.'
 ],
 hand=[
 'Ce ends in a small loop and sweep without the extra u/x strokes of Ceux; redonne has no terminal n-t sequence. H’s expanded endings are not supported in the first prose sentence.',
 'Thin horizontal cancellations can merge with low letters. Par and comme retain plausible lexical readings but are newly marked doubtful; the cancellation state itself is clear.',
 'The q of conséquences has a closed head and a conspicuous descending stem. The full marginal phrase reads ne semblent pas conséquences, not H’s affirmative paraphrase.',
 'Numeral 2 varies between a curved-head form and a bent foot-like form. Each superscript was read in place; the crossed marginal example alone remains doubtful.',
 'The small point low beside the left-hand σ_1 in its defining row has no syntactic position and is not supplied as punctuation. The paired terminal points of the later cyclic display are a separate, well-placed inscription.',
 'The final bottom-edge abbreviation has a tall l and compressed remaining letters; its raised ending is not sufficiently distinct to settle singular versus plural. No expansion is imposed.'
 ],
 abbreviations=[dict(form=r'\unsure{élém\textsuperscript{ts}}',expansion='éléments (provisional; raised ending uncertain)',place='incomplete final sentence at bottom edge')],
 notes=[
 'The page records three square relations for the epsilon generators and expressions for the sigma generators in terms of them. It then lists a product-of-squares relation and three involutivity relations. These are the author’s written formulas; no independent mathematical verification is claimed.',
 'An initial chain identifying rho with three adjacent sigma products is cancelled, as is an epsilon expansion beneath its first product. The vertical connector between those two cancellations remains physically untouched. The above-line replacement is sigma_0sigma_1=l_1^{-1}rho, followed by a separate right-margin derivation beginning rho=l_1sigma_0sigma_1.',
 'The right-margin derivation contains a small cancelled exponent before its final underbraced factors. That exponent remains doubtful. All factors and their indices, including the ambiguous final epsilon of the abandoned expansion, are preserved in their written order.',
 'The three cyclic rho expressions are followed by the marginal authorial doubt ces relations ne semblent pas conséquences des autres. This negative qualification is legible and materially differs from H’s se déduisent … par conjugaison. The vertical separator between the main display and the comment is represented in the transcription.',
 'The author next says to multiply these relations in reverse order and write rho cubed equal to 1, obtaining the displayed squared epsilon product equal to 1. The next sentence calls this inquiétant and breaks off after an uncertain abbreviation for élément(s). No missing continuation or explanation of the concern is supplied.',
 'Root independently reviewed the first eleven crops and agreed with the substantive readings, the newly retained lexical doubts, the untouched vertical connector, the resolved conséquences, the colon, and the uncertain final abbreviation. The two additional upper-display punctuation crops document literal H commas absent from the ink. No date is present. Handwritten page number 13 is distinct from editorial scan 14. No mathematical verification was performed by this reader.'
 ],check_events=[],diff_coverage=coverage)
(out/'145_scan014.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len(changes)==17 and len(doubts)==5
assert [x['id'] for x in decisions]==['M0806','M0807']
assert [x['row'] for x in coverage]==list(range(1,42))
assert all(c['c_changed'] or c['h_changed'] for c in changes)
assert all((root/'edition'/c['crop']).is_file() for c in changes+decisions+unlisted)
assert len(set(b['box'] for b in second))==len(second)
assert all(0<=b['coords'][0]<b['coords'][2]<=1677 and 0<=b['coords'][1]<b['coords'][3]<=2361 for b in second)
assert all(i['sheet_kind']=='text' and i['hand']=='his hand' for i in inventory)
print(json.dumps({'scan':14,'crops':len(boxes),'changes':len(changes),'decisions':len(decisions),'unlisted_decisions':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(coverage)}))
