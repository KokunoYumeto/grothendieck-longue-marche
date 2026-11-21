from pathlib import Path
import json, csv

ROOT=Path('/workspace/scratch/0cab6a548abb')
PAGE='149_scan117'
REVIEW=ROOT/'edition'/'review'
BOXES=json.loads((REVIEW/f'{PAGE}_crop_boxes.json').read_text())

def cp(p): return f'crops/{PAGE}_{p}.png'
def rec(ident,p,place,C,H,final,evidence,confidence='high',vs_C=False,vs_H=True,
        kind='misread word',error_category='Words',H_marked=False,consequential=False,**extra):
 return dict(id=ident,place=place,C=C,H=H,final=final,evidence=evidence,crop=cp(p),bbox=BOXES[p][0],confidence=confidence,vs_C=vs_C,vs_H=vs_H,kind=kind,error_category=error_category,H_marked=H_marked,consequential=consequential,**extra)

eq23=r'''(23)\qquad
\mathcal E_X^{\deleted{\unsure{K}}\inserted{\overline L}}
=\mathcal E_L^{\unsure{g|G}\overline L}
\simeq\mathcal E_U^{\overline L}/\begin{gathered}\text{ss-groupe fermé}\\\text{inv. engendré}\\\text{par les }\unsure{L_{x_i'}|I_{x_i'}}\\(i\in I)\end{gathered}'''
eq24=r'(24)\qquad\mathcal E_L^{\overline L}\simeq\lim_{\substack{\longleftarrow\\U}}\mathcal E_U^{\overline L}'
eq25=r'(25)\qquad\unsure{\Pi|\pi}_{L/K}^{\overline L}\simeq\lim_{\substack{\longleftarrow\\U}}\unsure{\Pi|\pi}_{U/K}^{\overline L}.'
margin_lines=[
 'Dans les',
 'considérations qui',
 r'suivent, $K$ (et $X,U$)',
 'ne jouent provisoirement',
 r'aucun rôle --- \unsure{(|[}Mais on pourrait',
 r"``plus gén.'' \unsure{regarder|remplacer} groupes de décomp.",
 r"\deleted{\unsure{de dimension relative}} d'un des ``$U$''",
 r"\uline{mais seulement} \uline{\unsure{épis-comp|épi-s-comp|épi-scop}} (la ``généralisation'' étant",
 'triviale,',
 r'$\mathcal E_L\longrightarrow\mathcal E_U$)',
]
nb_lines=[
 r"NB on \unsure{n'utilise}",
 r"en termes ``absolus'' que",
 'pour des',
 r'schémas \uline{épais}',
 '(quasi-proj. ?)',
 r'\uline{réguliers}',
]
margin1='\\margin{'+('\\newline\n'.join(margin_lines))+'}'
margin2='\\margin{'+('\\newline\n'.join(nb_lines))+'}'
tex=r'''\scanpage{117}
\mspage{58}
\[
'''+eq23+r'''
\]
Notons que $\mathcal E_L^{\overline L}$ est la limite
projective des $\mathcal E_U^{\overline L}$, pour des
modèles réguliers (affines si on y tient)
variables
\[
'''+eq24+r'''
\]
et de $=$, bien sûr
\[
'''+eq25+r'''
\]
Comment récupérer les $\mathcal E_U^{\overline L}$ \unsure{à}
$\mathcal E_L^{\overline L}$ ? Pour \uline{tt}
sous-anneau \inserted{d-vr $V$} de \unsure{ess.|en.} de type
\unsure{fini} sur $K$ (\unsure{correspond|correspondant} à un
``germe de modèle'' de $L/K$, au
voisinage d'un pt de codim $1$ i.e.
du pt gén. d'un diviseur), considé-\newline
rons le point fermé $x$ de $S_x=\operatorname{Spec}(V)$,

'''+margin1+'\n\n'+margin2+r'''

\margin{116}
'''

changes=[
 rec('p01a','p01','Display (23), overwritten first superscript',
     r'\mathcal E_X^{\deleted{\unsure{K}}\inserted{\overline L}}',
     r'\mathcal{E}^{\overline{L}}_{X}',
     r'\mathcal E_X^{\deleted{\unsure{K}}\inserted{\overline L}}',
     'A bar and an L-shaped replacement share the exponent area with crossed underlying strokes. The dark cancellation and surviving oblique strokes are real; the proposed underlying K is not fully recoverable. H retains only the final replacement and omits the correction.',
     confidence='medium',kind='omission',error_category='Struck text'),
 rec('p01b','p01','Display (23), denominator second baseline',
     'inv. engendré','invariant engendré','inv. engendré',
     'The first word consists of a dotted i, reduced n/v strokes and a separate stop. No full invariant ending is written. The following engendré has a long g descender crossing the generator on the line below.',
     kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised'),
 rec('p01c','p01','Display (23), complete denominator generator expression',
     r'\unsure{L_{x_i\prime}|I_{x_i\prime}}',r'I_{x\prime_i}',r'\unsure{L_{x_i\prime}|I_{x_i\prime}}',
     'The generator has a long vertical stroke and a lower right foot. The apparent upper cap coincides with the descender of engendré above, so L versus I is not securely resolved. The lower x, the smaller i and the raised prime are visible. Prime/subscript ordering in the two TeX spellings does not create an additional ink difference.',
     confidence='low',vs_H=False,kind='misread symbol or index',error_category='Symbols and indices',consequential=True,unresolved=True),
 rec('p03','p03','Main line 10, written shorthand between displays',
     r'et de $=$, bien sûr','et de même, bien sûr',r'et de $=$, bien sûr',
     'Two separate horizontal strokes, followed by a comma, are written after de. They are the sign =, not the letters of même. The remaining bien sûr includes its circumflex.',
     kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised'),
 rec('p04a','p04','Main line 12, opening question',
     r'Comment récupérer les $\mathcal E_U^{\overline L}$',
     r'Les \ill{} \ill{} \ill{} les $\mathcal{E}^{\overline{L}}_{U}$',
     r'Comment récupérer les $\mathcal E_U^{\overline L}$',
     'The first word has a large initial C, a sequence of reduced m strokes and the tall terminal t of Comment. The next word has its r entry, accented e, c/u sequence and long p descender; the diagonal marginal text crosses this area but does not supply extra main-line words. Read récupérer, followed by les and the complete E_U formula.',H_marked=True),
 rec('p04b','p04','Main line 12, small sign after E_U before the next-line E_L',
     r'\unsure{à}',r'\ill{}',r'\unsure{à}',
     'A very reduced lower stroke and a separate raised stroke follow the E_U expression. They are compatible with à, but the little body is not a securely resolved letter. No expanded phrase such as à partir de is supplied.',
     confidence='low',vs_H=False,kind='other',error_category='Other',H_marked=True,unresolved=True),
 rec('p04c','p04','Main line 13, underlined short form after Pour',
     r'\uline{\unsure{tt}}',r'\emph{\ill{}}',r'\uline{tt}',
     'Two tall short t stems share a transverse stroke; a separate lower horizontal line underlines the pair. The short form is tt, not an expanded word.',
     kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',H_marked=True),
 rec('p05a','p05','Insertion above main line 14',
     r'\inserted{\unsure{d-vr} $V$}',r'\emph{\ill{} $V$}',r'\inserted{d-vr $V$}',
     'The addition has a looped d with ascender, a separate short hyphen, a reduced v/r sequence and a large V. The final short return after the v-shaped part supports r. These are written above the main baseline.',
     kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',H_marked=True),
 rec('p05b','p05','Main line 14 and the attachment of its upper insertion',
     r'sous-anneau \inserted{\unsure{d-vr} $V$} de',
     r'(\emph{\ill{} $V$}) \ill{} du',
     r'sous-anneau \inserted{d-vr $V$} de',
     'The main line has sous, a written hyphen, and anneau. The long curved line under the upper d-vr V addition descends after anneau, indicating attachment there. It is not a pair of parentheses around an ordinary inline phrase.',
     kind='insertion or placement',error_category='Insertions put in the wrong place',H_marked=True),
 rec('p05c','p05','Main line 14, before de type',
     r'de \unsure{ess.|en.} de type',r'du \ill{} de type',r'de \unsure{ess.|en.} de type',
     'The first group is de, with the looped d and reduced e. The next group is very short and followed by a separate stop; the low middle strokes do not securely distinguish ess. from en. The following de type is clear. No missing L is inserted to repair the syntax.',
     confidence='medium',H_marked=True),
 rec('p06a','p06','Main line 15, word before sur K',
     r'\unsure{fini}',r'\ill{}',r'\unsure{fini}',
     'A descending f-like stem and short dotted strokes on the main baseline support fini, but diagonal marginal writing interferes with the middle. The existing uncertainty is retained.',
     confidence='medium',vs_H=False,kind='other',error_category='Other',H_marked=True,unresolved=True),
 rec('p06b','p06','Main line 15, verb or participle inside the parenthesis',
     'correspond','correspondant',r'\unsure{correspond|correspondant}',
     'The beginning correspond- is recognizable. Several small strokes after the final tall rise cannot be securely assigned to a contracted ending or separated terminal strokes. Neither witness ending is adopted as certain.',
     confidence='medium',vs_H=False,unresolved=True),
 rec('p06c','p06','Main line 16, quotation signs around germe de modèle',
     "``germe de modèle''",'« germe de modèle »',"``germe de modèle''",
     'The opening and closing signs are paired short quotation strokes, not angular guillemets. They are rendered with two backticks and two apostrophes under the supplied convention.',
     kind='other',error_category='Other'),
 rec('p06d','p06','Main line 16, after L/K and comma',
     'au',r'\ill{}','au',
     'A low two-part au follows the comma on the same main baseline. It continues with voisinage on the next line.',
     kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',H_marked=True),
 rec('p07a','p07','Main lines 18–19, divided final verb',
     'considérons',r'considé\-rons',r'considé-\newline rons',
     'The last group on the upper line is considé followed by a separate horizontal hyphen. The next line begins rons. The actual division is preserved, without turning it into an ordinary internal lexical hyphen.',
     vs_C=True,vs_H=False,kind='other',error_category='Other'),
 rec('p07b','p07','Main line 19, before point',
     'le',r'\struck{\ill{}} le','le',
     'There is one looped l followed by e. Its foot is dark and retraced, but no separate cancelled word can be isolated before it. H’s additional struck illegible item has no distinct written counterpart.',
     kind='text not on the page',error_category='Text that is not on the page',H_marked=True),
 rec('p07c','p07','Main line 19, before fermé',
     'point',r'\ill{}','point',
     'The p entry, reduced oi, n and final t-like return form point before the clearly accented fermé.',
     kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',H_marked=True),
 rec('p07d','p07','Main line 19, full final formula',
     r'S_x=\operatorname{Spec}(V)',r'S=\operatorname{Spec}(V)',r'S_x=\operatorname{Spec}(V)',
     'A distinct small x is below S. Both equality strokes and the full Spec(V) expression follow. H omits the lower x.',
     kind='misread symbol or index',error_category='Symbols and indices',consequential=True),
 rec('p08','p08','First marginal note, opening five baselines',
     r'Dans les considérations qui suivent, $K$ (et \unsure{$X,U$}) ne jouent provisoirement aucun rôle --- (Mais on pourrait',
     r'Dans les considérations qui suivent, $K$ (et $X$, $U$) un \ill{} \uncertain{provisoirement} \ill{} \ill{} \ill{} \ill{} [Mais on \uncertain{pourra}',
     r'Dans les considérations qui suivent, $K$ (et $X,U$) ne jouent provisoirement aucun rôle --- \unsure{(|[}Mais on pourrait',
     'After rotation the first five baselines read Dans les / considérations qui / suivent, K (et X,U) / ne jouent provisoirement / aucun rôle — [opening sign] Mais on pourrait. The two crossed diagonals of X, comma and U cup are clear. The final t of pourrait is visible. The opening sign before Mais is straighter than a normal parenthesis and remains parenthesis/bracket uncertain separately.',H_marked=True),
 rec('p10a','p10','First margin line 6, after the quoted plus gén.',
     r'\unsure{remplacer}',r'\ill{}',r'\unsure{regarder|remplacer}',
     'An early descending loop in this word can be a g, supporting regarder; the alternative remplacer would require assigning it to a p at a later position. Crossing strokes and the reduced interior prevent a secure choice. The new possibility is retained without claiming a resolved C correction.',
     confidence='low',vs_H=False,kind='other',error_category='Other',H_marked=True,unresolved=True),
 rec('p10b','p10','First margin lines 6–7, neighboring phrase',
     r"\unsure{groupes|les groupes} \unsure{de décomp.|par des} \unsure{d'un des|l'un des} ``$U$''",
     r'\ill{} \ill{} \ill{}',
     r"groupes de décomp. [next baseline after the cancelled phrase:] d'un des ``$U$''",
     'A g-shaped beginning and the reduced roup/es sequence support groupes, with no distinct preceding les. The next two d entries and final abbreviated comp. support de décomp., rather than par des. The following baseline’s right continuation has a looped d entry, apostrophe, un, des and quoted U. Its initial loop supports d’un rather than l’un. These words are preserved without supplying an unwritten article.',H_marked=True,
     supporting_crops=[cp('p11')]),
 rec('p10c','p10','First margin line 7, cancelled phrase and its position',
     r"d'un des ``$U$'' \deleted{\unsure{de dimension relative}}",
     '[absent]',
     r"\deleted{\unsure{de dimension relative}} d'un des ``$U$''",
     'The cancelled phrase is at the left of the same sloping baseline whose right continuation is d’un des quoted U. C places the cancellation after U. Its actual left-to-right written position is retained. The cancellation crosses reduced letter groups compatible with de dimension relative, but its interior remains obscured and its intended syntactic attachment is not inferred.',
     confidence='medium',vs_C=True,kind='deletion state',error_category='Struck text'),
 rec('p10d','p10','First margin line 8, first underlined phrase',
     r'\uline{\unsure{mais seulement}}',r'\ill{}',r'\uline{mais seulement}',
     'The initial m/a/i/s strokes and the separate seulement group with looped l and terminal t are visible. A full separate line underlines this phrase.',
     kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',H_marked=True),
 rec('p10e','p10','First margin line 8, second underlined short form',
     r'\uline{\unsure{épi-s-comp|épi-scop}}',r'\uncertain{après coup}',
     r'\uline{\unsure{épis-comp|épi-s-comp|épi-scop}}',
     'An e-like entry, descending p, short i/s-like strokes, a clearly visible hyphen before the comp-like ending, and a final descending p are present. A distinct hyphen between i and s is not secure, so épis-comp is included first while the supplied alternatives remain. The complete letter grouping is still doubtful; it does not support a confident après coup reading.',
     confidence='low',H_marked=True,unresolved=True),
 rec('p11a','p11','First margin lines 8–10, final parenthesis and formula',
     r"(la ``\unsure{généralisation|géométrie}'' étant \unsure{triviale|prise}, $\mathcal E_L\longrightarrow\mathcal E_U$))",
     r'\ill{}',
     r"(la ``généralisation'' étant\newline triviale,\newline $\mathcal E_L\longrightarrow\mathcal E_U$)",
     'The longer quoted word has its g entry and the extended -ralisation ending, supporting généralisation rather than the shorter géométrie. The next line begins with a tall t and has the dotted i and v/l strokes of triviale, not an initial descending p. The E_L to E_U arrow formula begins on the lower short baseline. One final closing parenthesis is visible; no second closing stroke is supplied.',
     vs_C=True,kind='omission',error_category='Omissions',H_marked=True),
 rec('p11b','p11','First margin end, count of closing signs',
     '))',']',')',
     'One long closing curve follows the final E_U. There is no distinct second closing curve. The opening sign before Mais remains uncertain, and no missing closing sign is added to balance the prose.',
     vs_C=True,kind='text not on the page',error_category='Text that is not on the page'),
 rec('p12a','p12','NB margin line 1, verb after on',
     r"\unsure{n'intéresse|s'intéresse}",r'\ill{}',r"\unsure{n'utilise}",
     'The initial n and apostrophe are followed by a low u-like group, tall t/l-like strokes, dotted short strokes and a reduced terminal se. These favor n’utilise over the supplied longer intéresse readings. Adjacent strokes and the very reduced ending prevent complete certainty, so the new reading is itself marked unsure. The small final dark point is not securely separable from the terminal letter and is not independently asserted as a stop.',
     confidence='medium',vs_C=True,H_marked=True),
 rec('p12b','p12','NB margin lines 2–6',
     r"en termes ``\unsure{absolus}'' \unsure{que pour des schémas} \uline{\unsure{épais}} (\unsure{quasi-proj.} ?) \uuline{réguliers}",
     r'\ill{} \ill{} \ill{} \ill{} \ill{} des solutions \uncertain{régulières} \ill{}',
     r"en termes ``absolus'' que\newline pour des\newline schémas \uline{épais}\newline (quasi-proj. ?)\newline \uline{réguliers}",
     'The quoted word has the a/b beginning, tall l and final us of absolus. The following que / pour des / schémas are on three successive baselines; schémas has its initial sch cluster, not solutions. The underlined épais has an e entry, descending p and dotted i before final s. In the parenthesis, quasi-, a separate hyphen, proj. and a distinct question mark are written. The final word is réguliers, with no added feminine ending. Its underline is assessed separately below.',H_marked=True),
 rec('p12c','p12','NB margin line 6, underline extent',
     r'\uuline{réguliers}',r'\uncertain{régulières}',r'\uline{réguliers}',
     'One straight underline extends across the complete word. The shorter curved lower-left return is connected with the descending g; it does not form a second full underline. This is an ink/markup reading difference, not a TeX-macro preference.',
     vs_C=True,vs_H=False,kind='drawing or diagram',error_category='Drawings and diagrams',H_marked=True),
 rec('p09','p09','Bottom-left standalone foliation',
     r'\margin{116}','[absent]',r'\margin{116}',
     'Two narrow numeral-one strokes followed by the looped 6 form the small number 116. The lower dark band is the photographed sheet edge.',
     kind='omission',error_category='Omissions'),
]

D=[]
def decision(ident,p,which,reading,evidence,confidence='high'):
 D.append(dict(id=ident,cote='149',scan='117',decision=which,reading=reading,evidence=evidence,crop=cp(p),bbox=BOXES[p][0],confidence=confidence))
decision('M0076','p01','undecided',r'\unsure{g|G}','The small exponent letter has an angled upper entry, an internal return and a descending right stroke; g/G case is not securely distinguished.','low')
decision('M0077','p01','undecided',r'\unsure{L_{x_i\prime}|I_{x_i\prime}}','The lower right foot favors an L-shaped form, but a possible upper cap overlaps the preceding engendré-g descender. The x, i and prime are visible.','low')
decision('M0078','p04','undecided',r'\unsure{à}','Reduced lower body and raised stroke are compatible with à but not fully resolved.','low')
decision('M0079','p04','first',r'\uline{tt}','Two t stems share a transverse stroke; a separate underline lies below them.')
decision('M0080','p05','first','d-vr','The upper addition has a looped d, separate hyphen, reduced v and a short r-like return before V.')
decision('M0081','p05','undecided',r'\unsure{ess.|en.}','The short group ends in a separate stop, but the low middle strokes permit either ss or n.','medium')
decision('M0082','p06','undecided',r'\unsure{fini}','A descending f-like stem and short dotted strokes support fini; crossing marginal writing prevents a fully secure isolation of the middle.','medium')
decision('M0083','p08','first',r'$X,U$','Two crossing diagonals form X; a comma separates it from the U-shaped letter.')
decision('M0084','p10','undecided',r'\unsure{regarder|remplacer}','The early descending loop can be g, favoring regarder; the interior and allocation of crossing strokes do not securely exclude remplacer.','low')
decision('M0085','p10','first','groupes','The group begins with a descending g shape; no independent preceding les is visible.')
decision('M0086','p11','first','de décomp.','The two initial d loops and the abbreviated comp-like ending with stop are visible; par des would require different initial descenders.')
decision('M0087','p11','first',"d'un des",'The initial looped d, apostrophe, reduced un and second des are distinguishable before quoted U.')
decision('M0088','p10','first',r'\uline{mais seulement}','The m/a/i/s group and seulement with looped l and terminal t are present above a full underline.')
decision('M0089','p10','undecided',r'\uline{\unsure{épis-comp|épi-s-comp|épi-scop}}','The hyphen before the comp-like ending is plain; a separate hyphen between i and s is not secure. The complete reduced short form remains doubtful.','low')
decision('M0090','p11','first','généralisation','The extended quoted word has a g beginning and the longer -ralisation ending, unlike géométrie.')
decision('M0091','p11','first','triviale','A tall initial t, short dotted strokes, v and l-like ascender support triviale; no initial p descender is present.')
decision('M0092','p12','other',r"\unsure{n'utilise}",'The n/apostrophe, u-like beginning, tall t/l-like strokes and short terminal se support n’utilise. The ending is still reduced and intertwined enough to retain an unsure mark.','medium')
decision('M0093','p12','first','absolus','The quoted word has a/b at its beginning, a tall l and a reduced us ending.')
decision('M0094','p12','first','que pour des schémas','The phrase occupies the end of NB line 2 and the next two baselines; q, the descending p of pour, and the sch cluster are visible.')
decision('M0095','p12','first',r'\uline{épais}','The short underlined word has e, a descending p, a small a and dotted i before final s.')
decision('M0096','p12','first','quasi-proj.','The q/u/a/s/i group, hyphen, proj. ending and separate following question mark are visible; the short form is preserved.')

main_lines=[
 r'(23) $\mathcal E_X^{\deleted{\unsure{K}}\inserted{\overline L}}=\mathcal E_L^{\unsure{g|G}\overline L}\simeq\mathcal E_U^{\overline L}/$ ss-groupe fermé',
 'inv. engendré',r'par les $\unsure{L_{x_i\prime}|I_{x_i\prime}}$',r'$(i\in I)$',
 r'Notons que $\mathcal E_L^{\overline L}$ est la limite',
 r'projective des $\mathcal E_U^{\overline L}$, pour des',
 'modèles réguliers (affines si on y tient)','variables',eq24,
 r'et de $=$, bien sûr',eq25,
 r'Comment récupérer les $\mathcal E_U^{\overline L}$ \unsure{à}',
 r'$\mathcal E_L^{\overline L}$ ? Pour \uline{tt}',
 r'sous-anneau [upper insertion: d-vr $V$] de \unsure{ess.|en.} de type',
 r'\unsure{fini} sur $K$ (\unsure{correspond|correspondant} à un',
 r"``germe de modèle'' de $L/K$, au",
 r"voisinage d'un pt de codim $1$ i.e.",
 r"du pt gén. d'un diviseur), considé-",
 r'rons le point fermé $x$ de $S_x=\operatorname{Spec}(V)$,',
]

inventory=[
 dict(sheet_kind='text',hand='author numbering hand',element='e01',kind='text',position='Top-center standalone author page number',first_words_or_objects='58',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e02',kind='display',position='Main lines 1–4, display (23), four denominator baselines',first_words_or_objects=eq23,transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e03',kind='deletion',position='First exponent of (23), overlapped by replacement',first_words_or_objects=r'\unsure{K}',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e04',kind='insertion',position='Replacement in the same exponent area of (23)',first_words_or_objects=r'\overline L',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e05',kind='text',position='Main lines 5–8',first_words_or_objects='Notons que ... est la limite projective',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e06',kind='display',position='Main line 9, display (24)',first_words_or_objects=eq24,transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e07',kind='text',position='Main line 10',first_words_or_objects=r'et de $=$, bien sûr',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e08',kind='display',position='Main line 11, display (25)',first_words_or_objects=eq25,transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e09',kind='text',position='Main lines 12–19, lower question and valuation-ring paragraph',first_words_or_objects='Comment récupérer les ... Pour tt sous-anneau',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e10',kind='insertion',position='Separate upper baseline attached after sous-anneau on main line 14',first_words_or_objects=r'd-vr $V$',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e11',kind='margin note',position='Ten oblique baselines at left and across the main question, including two short final continuation baselines',first_words_or_objects='Dans les considérations qui suivent',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e12',kind='deletion',position='First margin line 7, left of the continuation d’un des quoted U',first_words_or_objects=r'\unsure{de dimension relative}',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e13',kind='margin note',position='Six oblique NB baselines below the first note',first_words_or_objects=r"NB on \unsure{n'utilise}",transcribed='yes'),
 dict(sheet_kind='text',hand='unattributed numbering hand',element='e14',kind='margin note',position='Bottom-left standalone foliation',first_words_or_objects='116',transcribed='yes'),
]

U=[]
def doubt(place,reading,alts,p,confidence='low',**extra):
 U.append(dict(place=place,reading=reading,alternatives=alts,confidence=confidence,crop=cp(p),bbox=BOXES[p][0],**extra))
doubt('Display (23), cancelled exponent',r'\deleted{\unsure{K}}','Underlying K is tentative; crossing strokes leave only part of its obliques visible.','p01')
doubt('Display (23), second superscript letter',r'\unsure{g|G}','g | G','p01')
doubt('Display (23), full generator expression',r'\unsure{L_{x_i\prime}|I_{x_i\prime}}','L-shaped lower foot; possible upper cap overlaps the engendré-g descender.','p01')
doubt('Display (25), source pi-shaped sign',r'\unsure{\Pi|\pi}_{L/K}^{\overline L}',r'\Pi | \pi; flat cap and two legs, but their case is not independently secure.','p03','medium')
doubt('Display (25), target pi-shaped sign',r'\unsure{\Pi|\pi}_{U/K}^{\overline L}',r'\Pi | \pi; assessed locally, not harmonized from earlier absolute-group notation.','p03','medium')
doubt('Main line 12, small joining sign after E_U',r'\unsure{à}','à remains tentative; do not expand into an unwritten phrase.','p04')
doubt('Main line 14, abbreviated word before de type',r'\unsure{ess.|en.}','ess. | en.; no extra L supplied.','p05','medium')
doubt('Main line 15, first word',r'\unsure{fini}','fini; diagonal note crosses its middle strokes.','p06','medium')
doubt('Main line 15, ending after correspond-',r'\unsure{correspond|correspondant}','correspond | correspondant; final small strokes cannot be allocated securely.','p06','medium')
doubt('First margin line 5, opening sign before Mais',r'\unsure{(|[}','Opening parenthesis | opening square bracket; short upright with lower foot, upper form not decisive.','p10','medium')
doubt('First margin line 6, verb after plus gén.',r'\unsure{regarder|remplacer}','regarder | remplacer; early loop can be g, interior crossed/reduced.','p10')
doubt('First margin line 7, cancelled phrase',r'\deleted{\unsure{de dimension relative}}','de dimension relative; crossed interior and uncertain intended attachment. Literal order is retained before d’un des quoted U.','p10')
doubt('First margin line 8, underlined short form',r'\uline{\unsure{épis-comp|épi-s-comp|épi-scop}}','épis-comp | épi-s-comp | épi-scop; exact internal division and reduced letters remain uncertain.','p10')
doubt('NB margin line 1, proposed new verb',r"\unsure{n'utilise}","n'utilise is favored; C's n'intéresse/s'intéresse are not adopted. Some ending strokes remain intertwined and reduced.",'p12','medium')

unlisted=[
 dict(place='Display (23), nested cancelled-exponent C doubt',decision='undecided',reading=r'\deleted{\unsure{K}}',evidence='Crossing strokes obscure part of the underlying letter; bar/L replacement is visible.',crop=cp('p01'),bbox=BOXES['p01'][0],confidence='low'),
 dict(place='First margin line 7, nested cancelled-phrase C doubt',decision='undecided',reading=r'\deleted{\unsure{de dimension relative}}',evidence='Reduced letter groups and a cancellation are visible, but the interior is not fully recoverable. Preserve actual baseline order before d’un des quoted U.',crop=cp('p10'),bbox=BOXES['p10'][0],confidence='low'),
]

def audit(name,kind,bbox,reading,context_note=None):
 d=dict(box=name,kind=kind,bbox=bbox,reading=reading)
 if context_note: d['context_note']=context_note
 return d

context_margin=(
 'Main writing intersected by this rectangle, in its separate horizontal reading direction: '
 'Comment récupérer les; the complete E_L^{bar L} question formula and question mark, followed by a clipped beginning of Pour; '
 'the inserted d-vr V and sous-anneau de, followed by a clipped beginning of ess./en.; '
 'fini sur K (correspond/correspondant, without its following à un; '
 'the quoted germe de modèle and de, followed by a clipped L/K; '
 'voisinage d’un pt de followed by a clipped codim; '
 'du pt gén. d’un followed by a clipped diviseur; '
 'rons le point fermé x de followed by a clipped S_x. '
 'These are boundary fragments of the already transcribed main lines, not additional marginal words.'
)
audit_boxes=[
 audit('b01','insertion; deletion; doubtful formula; handwritten number; C/H word difference',BOXES['p01'][0],r'\mspage{58}'+'\n'+eq23,
       'The rectangle includes the entire display and denominator, including the crossing engendré descender. At the bottom center it also clips the upper bar/upper stroke of the following ordinary E_L^{bar L} in Notons que; that fragment is not part of (23).'),
 audit('b02','handwritten number',[290,740,1505,995],'variables\n'+eq24),
 audit('b03','doubtful formula; handwritten number; C/H word difference',BOXES['p03'][0],r'et de $=$, bien sûr'+'\n'+eq25,
       'At the lower edge are clipped upper components of the later oblique marginal ending and its closing curve, fully read in b08. The complete display (25), including both superscript bars and the limit-index U, is included.'),
 audit('b04','doubtful formula; C/H word difference',BOXES['p04'][0],main_lines[11]+'\n'+main_lines[12],
       'Diagonal writing crossing the two main lines belongs to the first marginal note, including parts of its later words and E_L to E_U formula. Its complete reading and formula occur in b08; it is not inserted into the main question. Both main E formulae and the underlined tt are complete here.'),
 audit('b05','insertion; C/H word difference',BOXES['p05'][0],r'sous-anneau \inserted{d-vr $V$} de \unsure{ess.|en.} de type',
       'At the left/top edge are diagonal fragments of the first marginal note, including the cancelled phrase, underlined short form and nearby words, fully read in b08. The long curved line beneath d-vr V is its leader, not parentheses.'),
 audit('b06','C/H word difference; less-than-high C departure',[270,1725,1570,2035],main_lines[14]+'\n'+main_lines[15],
       'The upper-left diagonal context belongs to the first note and NB note, fully read in b08. The lower bound includes the complete descending g of germe. Any tiny tip at the lower right belongs to the following numeral 1, fully read in b07.'),
 audit('b07','handwritten number; C/H word difference',BOXES['p07'][0],main_lines[16]+'\n'+main_lines[17]+'\\newline\n'+main_lines[18],
       'At the upper left are the lower g descender from preceding germe and clipped oblique NB strokes. The numeral 1, written line-end hyphen, full le and point groups, and entire S_x=Spec(V) formula are included.'),
 audit('b08','margin note; deletion; doubtful formula; C/H word difference; less-than-high C departure',BOXES['p08'][0],margin1+'\n'+margin2+'\n[Boundary context, in main-line direction: '+context_margin+']',
       'Both complete oblique notes are included, with the entire E_L to E_U formula. The listed main-line boundary context is not supplied as part of the notes; clipped portions are explicitly identified. The saved view is rotated clockwise 35 degrees.'),
 audit('b09','margin note; C/H word difference; less-than-high C departure',BOXES['p12'][0],margin2+'\n[Upper diagonal context: parts of ne jouent, aucun rôle, quoted plus gén., regarder/remplacer, the cancelled de dimension relative, and underlined mais seulement; lower/right context: clipped portions of germe, voisinage, du pt and rons le from the main text.]',
       'The complete NB note is the target. The upper neighboring margin is already read in b08. One full straight underline is present below réguliers; the curved lower-left return is the g descender.'),
 audit('b10','handwritten number',BOXES['p09'][0],r'\margin{116}',
       'The lower dark strip is the sheet edge, not another written stroke.'),
]

report=dict(
 page=PAGE,scan=117,reader='reader_a',line_count=38,
 line_count_detail=dict(main=19,margin=16,insertion=1,standalone_numbers=2),
 line_count_note='Main count includes the four baselines of display (23), four prose lines before (24), the two further displays, the intervening shorthand line and eight lower main lines. The first margin has ten baselines, including the separate triviale and E_L to E_U continuations; the NB note has six. The d-vr V addition is one separate logical baseline. The overwritten exponent in (23) occupies the existing exponent area and is inventoried as a correction without adding a separate text line. Formula labels share their display baselines; standalone 58 and 116 are counted separately.',
 line_map=dict(main=[dict(line=i+1,reading=s) for i,s in enumerate(main_lines)],
               margin_1=[dict(line=i+1,reading=s) for i,s in enumerate(margin_lines)],
               margin_2=[dict(line=i+1,reading=s) for i,s in enumerate(nb_lines)],
               insertion=[r'd-vr $V$'],standalone_numbers=['58','116']),
 changes=changes,decisions=D,unlisted_doubt_decisions=unlisted,
 inventory=inventory,doubts=U,audit_boxes=audit_boxes,
 notes=[
  'The page gives a quotient expression, two inverse-limit identities, and a question about recovering model groups from a field-level group; its lower paragraph introduces a d-vr subring and a closed point of Spec(V). The oblique notes qualify the role of K and the schemes. No missing hypotheses or definitions are imported from another page.',
  'All supplied IDs M0076–M0096 are represented once in decisions. The cancelled K and cancelled de dimension relative are nested C doubts absent from marks.tsv and appear only in unlisted_doubt_decisions, without invented IDs.',
  'The g/G letter and L/I generator of (23) remain unresolved. The whole formula, denominator and the engendré descender that overlaps the generator are preserved in the initial crop and audit box.',
  'Both pi-shaped signs in (25) were assessed locally. Their flat caps and legs are compatible with capital Pi, but case is retained as Pi/pi uncertainty; neither earlier notation nor the mathematical role decides them.',
  'The visible shorthand =, tt, inv., d-vr, pt, codim, gén., décomp. and quasi-proj. is not expanded. No stops are added after pt or codim.',
  'The main de ess./en. de type is retained literally. No unwritten L is added. The tiny à is not expanded, and the correspond/correspondant ending remains doubtful.',
  'The cancelled phrase is placed before d’un des quoted U on its actual shared baseline. Its intended attachment is left uncertain rather than moving it to fit grammar.',
  'The opening sign before Mais remains parenthesis/bracket uncertain. Only one final closing parenthesis is written after the marginal E_U; no second closing sign is added to balance the text.',
  'The early descending loop supports regarding regarder as a genuine alternative to remplacer. The underlined short form épis-comp/épi-s-comp/épi-scop is left unresolved, including its internal division.',
  'The NB verb is proposed as n’utilise, still marked unsure. The tiny terminal dark point cannot securely be separated from the reduced ending and is not independently asserted to be a stop. The underline beneath réguliers is single: the shorter lower-left curved stroke belongs to g.',
  'The written considé-/rons line division is retained with a line break. A dark retraced foot in le is not turned into an additional separate cancelled word as H does.',
  'There are no incomplete-view repair crops on this page. Initial crops p01–p09 include the targeted complete formulae and overlap context. p10–p12 are focused enlargements of still-unresolved marginal regions from p08; they do not revisit a decided reading and are not treated as independent evidence.',
  'The complete sheet and both native halves were inspected once. Every saved crop p01–p12 was inspected visually. No OCR, text-recognition library, external research, PDF text layer, other page’s source, or TeX compilation was used.',
  'No independent mathematical proof verification is claimed for the quotient or inverse-limit assertions on this isolated leaf; checks is intentionally empty.',
 ],
 checks=[],
 hand_observations=[
  dict(habit='Crossing descenders can supply a false apparent cap or decoration to the next line.',places='engendré above the generator in (23); regulars-g below the NB note.',holds='Both local overlaps were inspected in full context.',witness_errors='The generator case stays uncertain; C’s second underline beneath réguliers is rejected because the extra curved stroke is the g descender.'),
  dict(habit='Short forms are written with very reduced low strokes and explicit stops where present.',places='inv. in (23), tt after Pour, ess./en., décomp., quasi-proj.',holds='Clear short forms are retained; ess./en. and the underlined épis-comp-like form remain uncertain.',witness_errors='H expands inv. to invariant and = to même, while leaving several other short forms illegible.'),
  dict(habit='A long curved lower leader joins a supralinear addition to the main baseline.',places='d-vr V above sous-anneau.',holds='The leader attaches after anneau; it is not an enclosing pair of parentheses.',witness_errors='H linearizes the addition in parentheses.'),
  dict(habit='Oblique marginal text continues across the main writing and uses progressively longer baselines.',places='First ten-line margin and six-line NB note.',holds='Words were assigned by writing direction and actual baseline order, including two short final continuation lines.',witness_errors='H loses much of the note; C moves its cancelled phrase and supplies an extra closing parenthesis.'),
  dict(habit='Line-end hyphen is a separate visible stroke.',places='Main lines 18–19, considé- / rons.',holds='One confirmed divided main word.',witness_errors='C joins the word without preserving the written hyphen.'),
 ],
 notation=[
  dict(written=r'$\mathcal E_X^{\deleted{\unsure{K}}\inserted{\overline L}}$',meaning_or_use='First term of (23), with a corrected exponent; underlying K remains doubtful.',places='Display (23).'),
  dict(written=r'$\mathcal E_L^{\unsure{g|G}\overline L}$',meaning_or_use='Second term of (23); the extra superscript letter is unresolved from ink.',places='Display (23).'),
  dict(written=r'$\unsure{L_{x_i\prime}|I_{x_i\prime}}$, $(i\in I)$',meaning_or_use='Generators of the written closed invariant subgroup in the quotient denominator; the generator letter remains L/I uncertain.',places='Display (23), denominator.'),
  dict(written=r'$\mathcal E_L^{\overline L}\simeq\lim_{\substack{\longleftarrow\\U}}\mathcal E_U^{\overline L}$',meaning_or_use='Written inverse-limit identity for varying regular models.',places='Display (24).'),
  dict(written=r'$\unsure{\Pi|\pi}_{L/K}^{\overline L}\simeq\lim_{\substack{\longleftarrow\\U}}\unsure{\Pi|\pi}_{U/K}^{\overline L}$',meaning_or_use='Second inverse-limit identity; case of both pi-shaped symbols remains locally uncertain.',places='Display (25).'),
  dict(written=r'$S_x=\operatorname{Spec}(V)$',meaning_or_use='Scheme whose closed point x is introduced in the final main line; lower x on S is visibly written.',places='Main line 19.'),
  dict(written=r'$\mathcal E_L\longrightarrow\mathcal E_U$',meaning_or_use='Unadorned map in the last short marginal baseline.',places='First marginal note, line 10.'),
 ],
 abbreviations=[
  dict(written='ss-groupe',expansion='sous-groupe (report only; not expanded in the transcription)'),
  dict(written='inv.',expansion='invariant (report only)'),
  dict(written='=',expansion='même in the phrase et de = (report only)'),
  dict(written='tt',expansion='tout (report only)'),
  dict(written='d-vr',expansion='Abbreviation retained literally; no expanded wording substituted.'),
  dict(written='ess. / en.',expansion='Unresolved short form; no expansion imposed.'),
  dict(written='pt',expansion='point (report only)'),
  dict(written='codim',expansion='codimension (report only; no stop added)'),
  dict(written='i.e.',expansion='id est (report only)'),
  dict(written='gén.',expansion='générique or général according to the local phrase (report only)'),
  dict(written='décomp.',expansion='décomposition (report only)'),
  dict(written='quasi-proj.',expansion='quasi-projectif (report only)'),
 ],
 inspection=dict(whole=True,halves=['top','bottom'],crops=[cp(f'p{i:02d}') for i in range(1,13)],crop_count=12,deletions_insertions_checked=True,
                 incomplete_view_repairs=[],focused_unresolved_views=[dict(overview='p08',focused=['p10','p11','p12'],reason='Still-open dense marginal words, cancellation, formula context and NB verb/underlining; no decided place was re-cropped.')]),
)

with (ROOT/'packets'/PAGE/'marks.tsv').open(newline='') as f:
 supplied=[r['id'] for r in csv.DictReader(f,delimiter='\t')]
assert [d['id'] for d in D]==supplied, ([d['id'] for d in D],supplied)
assert len(D)==21
assert len(main_lines)==19 and len(margin_lines)==10 and len(nb_lines)==6
assert sum(report['line_count_detail'].values())==38
for p in report['inspection']['crops']:
 assert (ROOT/'edition'/p).exists(),p
assert tex.count('{')==tex.count('}')
def literal_primes(value):
 if isinstance(value,str):
  return value.replace('x_i\\prime',"x_i'").replace('x\\prime_i',"x'_i")
 if isinstance(value,list):
  return [literal_primes(v) for v in value]
 if isinstance(value,dict):
  return {k:literal_primes(v) for k,v in value.items()}
 return value
report=literal_primes(report)
for entry in report['changes']:
 if entry['id']=='p11a':
  entry['vs_C']=False
  entry['scope_note']='The separate closing-sign correction is recorded once, in p11b; this entry logs the words and map left illegible in H.'
 if entry['id']=='p12b':
  entry['scope_note']='The C underline correction is recorded separately in p12c; this entry logs the lexical readings of the NB note.'
 if entry['id']=='p12c':
  entry['scope_note']='The H feminine-word reading is addressed in p12b; this record addresses only C’s extra underline.'
(REVIEW/f'{PAGE}.tex').write_text(tex,encoding='utf-8')
(REVIEW/f'{PAGE}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(page=PAGE,changes=len(changes),decisions=len(D),crops=12,doubts=len(U),audit_boxes=len(audit_boxes),line_count=38),ensure_ascii=False))
