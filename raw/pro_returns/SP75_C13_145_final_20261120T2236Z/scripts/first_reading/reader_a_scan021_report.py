from pathlib import Path
import csv, json, re

ROOT=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
OUT=ROOT/'edition/reader_reports'
PACKET=ROOT/'packets/145_scan021'
crops={x['name']:x for x in json.loads((OUT/'145_scan021_crop_manifest.json').read_text())}

heading='Donc on a les relations'
system13=r'''\[
(13)\quad\left\{\begin{gathered}
\tilde\sigma_0^2=\tilde\sigma_1^2=\tilde\sigma_\infty^2=1\\
\tilde\sigma_0\tilde\sigma_1=\tilde\sigma_1\tilde\sigma_\infty=\tilde\sigma_\infty\tilde\sigma_0
=\overset{\deleted{\sim}}{\rho}\ \deleted{(\unsure{=\rho})}\\
(\overset{\deleted{\sim}}{\rho}{}^3=1\text{ est conséquence des précédentes})
\end{gathered}\right.
\]'''
nb=r'''\margin{NB
\[
\rho\tilde\sigma_i\rho^{-1}=\tilde\sigma_{\dot\rho i}\quad\text{i.e}
\]
\[
\begin{aligned}
\rho\tilde\sigma_0\rho^{-1}&=\tilde\sigma_1\\
\rho\tilde\sigma_1\rho^{-1}&=\tilde\sigma_\infty\\
\rho\tilde\sigma_\infty\rho^{-1}&=\tilde\sigma_0
\end{aligned}
\]}'''
s_first=r'\overset{\deleted{\unsure{\sim}}}{\unsure{\mathfrak S_3|\mathcal S_3}}'
s_other=r'\unsure{\mathfrak S_3|\tilde{\mathfrak S}_3|\mathcal S_3|\tilde{\mathcal S}_3}'
prose1=r"et l'image réciproque $\tilde{\mathcal E}$ de $\varphi("+s_first+r")\subset\Gamma$ (ss-groupe d'indice 2) est produit $\frac12$ direct de $"+s_other+r'$ et de '
prose2=r'''$\Pi$. Il faut expliciter les opérations des $\tilde\sigma_a$ sur $\Pi$ pour avoir la structure complète du groupe, On trouve que $\tilde\sigma_a$ est au dessus '''
prose3=r'''$\varphi(\overset{\deleted{\sim}}{\dot\sigma}_a)$ i.e. la symétrie p.r. au plan passant par $P,\bar P,\deleted{\unsure{a_i}}i$, qui transforme $l_0$ en $l_0^{-1}$, $\deleted{l}l_\infty$ en $l_{\unsure{1|0}}^{-1}$, $l_1$ en $l_\infty^{-1}$ :'''
transport=r'\margin{Ce sont celles obtenues par transport de structure, via les opérations de $'+s_other+r'$ sur $(U,P)$}'
continuation_upper=r'''\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]
\fill (0,0.12)--(0.08,0.32)--(0.15,0.11)--(0.31,0.06)--(0.16,-0.05)--(0.13,-0.22)--(0.04,-0.08)--(-0.09,-0.06)--cycle;
\draw[line width=0.55pt] (0.50,0)--(0.70,0) (0.98,0)--(1.18,0) (1.46,0)--(1.66,0);
\end{tikzpicture}'''
continuation_lower=r'''\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]
\draw[line width=0.55pt] (0,0)--(0.20,0) (0.48,0)--(0.68,0) (0.96,0)--(1.16,0) (1.44,0)--(1.64,0);
\end{tikzpicture}'''
system14=r'''\[
(14)\quad\left\{\begin{array}{lll}
\tilde\sigma_0l_0\tilde\sigma_0^{-1}=l_0^{-1}&
\tilde\sigma_0l_1\tilde\sigma_0^{-1}=l_\infty^{-1}&
\tilde\sigma_0l_\infty\tilde\sigma_0^{-1}=l_1^{-1}\\
\tilde\sigma_1l_1\tilde\sigma_1^{-1}=l_1^{-1}&'''+continuation_upper+r'''&\\
'''+continuation_lower+r'''&&
\end{array}\right.
\]'''
critique=r'''\margin{\uline{Critique} La notation $\tilde\sigma_0$ suggère plutôt que $\tilde\sigma_0$ est au dessus de $\sigma_0$ --- il vaut mieux écrire $\dot\sigma_i'=\dot\sigma_i\tau$ et noter $\tilde\sigma_i'$ au lieu de $\tilde\sigma_i$ $(i\in\{0,1,\infty\})$, ou mieux $\sigma_i'$ (sans $\sim$) --- pour réserver $\tilde\sigma_i'$ à des éléments de $S\mathcal E$, cf plus bas\ldots}'''
relations=r'''Les relations (13) (14), plus la relation fondamentale $l_\infty l_1l_0=1$ (1), font une présentation de '''
eliminate=r'''$\tilde{\mathcal E}$, dont on peut si on veut éliminer $\rho$, \unsure{(}en omettant d'écrire la relation qui le définit)'''
remonter=r'''On peut maintenant remonter $\dot\tau$ en trois manières, à \unsure{sv|savoir}'''
systems15_16=r'''\[
(15)\quad\left\{\begin{aligned}
\tau_0&=\sigma_0\tilde\sigma_0=\tilde\sigma_0\sigma_0\\
\tau_1&=\sigma_1\tilde\sigma_1=\tilde\sigma_1\sigma_1\\
\tau_\infty&=\sigma_\infty\tilde\sigma_\infty=\tilde\sigma_\infty\sigma_\infty
\end{aligned}\right.
\qquad\text{donc}\quad(16)\left\{\begin{aligned}
\tau_0^2&=1\\\tau_1^2&=1\\\tau_\infty^2&=1
\end{aligned}\right.
\]'''
page='\n'.join([r'\scanpage{21}',heading,system13,nb,prose1+prose2+prose3,transport,system14,critique,relations+eliminate,'',remonter,systems15_16,r'\mspage{20}',''])
(OUT/'145_scan021.tex').write_text(page,encoding='utf-8')

changes=[]
def change(place,c,h,final,ink,kind,crop,c_changed=False,h_changed=True,confidence='high',marked='no',categories=(2,),consequence=''):
    ident=f's021-{len(changes)+1:02d}'
    changes.append(dict(id=ident,place=place,C=c,H=h,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c_changed,h_changed=h_changed,marked_in_H=marked,crop=crops[crop]['crop'],box=crops[crop]['box'],error_category=list(categories),math_consequence=consequence))
    return ident
c01=change('Opening line','Donc on a les relations','Donc aussi les relations',heading,'After Donc the small writing separates into an o/n cluster and a following a, not the longer u-ss-i sequence of aussi.','misread word','heading_system13',confidence='medium')
c02=change('System (13), old tildes above both rho occurrences',r'\overset{\deleted{\sim}}{\rho};\quad\overset{\deleted{\sim}}{\rho}{}^3',r'\rho;\quad\rho^3',r'\overset{\deleted{\sim}}{\rho};\quad\overset{\deleted{\sim}}{\rho}{}^3','A short wavy upper sign is locally scribbled through at each rho; the lower rho bodies and exponent 3 remain live. H omits the cancelled upper marks.','deletion state','heading_system13',categories=(3,7))
c03=change('System (13), cancelled parenthesis after the live rho',r'\deleted{(\unsure{=\rho})}',r'\struck{(\ill{})}',r'\deleted{(\unsure{=\rho})}','Both parentheses and a long rho-like descender are visible; the proposed equals strokes and upper rho loop are crossed. The partial reading is retained without resolving the C doubt.','readable ink left as \\ill{}','heading_system13',confidence='low',marked='yes',categories=(5,7))
c04=change('NB margin, index on the general right-hand sigma',r'\tilde\sigma_{\dot\rho i}',r'\tilde\sigma_{\rho(i)}',r'\tilde\sigma_{\dot\rho i}','A separate dot lies above the subscript rho, followed directly by i; there are no enclosing parentheses around i.','misread symbol or index','nb_margin',categories=(1,9),consequence='Preserves the dotted permutation acting on the index and its literal notation.')
c05=change('NB margin, abbreviation after the general formula',r'\text{i.e.}','i.e.',r'\text{i.e}','The point between i and e is visible; no detached terminal point follows the e.','text not on the page','nb_margin',c_changed=True,categories=(9,))
c06=change('NB margin, middle conjugation row',r'\rho\tilde\sigma_1\rho^{-1}=\tilde\sigma_\infty',r'\ill{}',r'\rho\tilde\sigma_1\rho^{-1}=\tilde\sigma_\infty','The looped rhos, inverse exponent, index 1 and two-lobed infinity are all readable on the middle row; both sigma tildes are separate upper strokes.','readable ink left as \\ill{}','nb_margin',marked='yes',categories=(5,))
c07=change('First main paragraph, image réciproque',"l'image réciproque","l'image inverse","l'image réciproque",'The longer word has the r/é opening and internal c-i-p-r sequence; its connected ending is compatible with -oque, not the shorter inverse outline.','misread word','image_reciproque',confidence='medium')
c08=change('First main paragraph, name of the inverse-image group',r'\tilde{\mathcal E}',r'\widetilde{\Sigma}',r'\tilde{\mathcal E}','The base has two rounded E lobes rather than the angular three-stroke outline of Sigma. A separate live wavy tilde is fully visible in the upper-marks crop.','misread symbol or index','upper_e_s_marks',categories=(1,))
c09=change('First main paragraph, upper mark over the S inside phi',r'\unsure{\tilde{\mathfrak S}_3|\tilde{\mathcal S}_3}',r'\mathfrak{S}_3',s_first,'The upper mark is separate from the ornate S and densely scribbled through. An underlying tilde is plausible but not wholly exposed. The dot-like pen stop inside the upper S curl is part of the letter, not a dotted-S operator.','deletion state','upper_e_s_marks',c_changed=True,confidence='medium',categories=(1,7))
c10=change('First main paragraph, comparison with Gamma',r'\subset\Gamma',r'=\Gamma',r'\subset\Gamma','The two horizontal arms are connected by a curved left side, yielding an open-right inclusion sign rather than two separate equal strokes. Gamma has a long left leg and short upper-right tip.','misread symbol or index','image_reciproque',categories=(1,),consequence='The written relation is inclusion, not equality.')
c11=change('First main paragraph, index-two qualification',"ss-groupe d'indice 2",r'\uncertain{ss-groupe diédral 2}',"ss-groupe d'indice 2",'A d and apostrophe precede the compact i-n-d-i-c-e sequence; the final e and following 2 are separate. There is no -éral ending.','misread word','image_reciproque',marked='yes')
c12=change('First main paragraph, second ornate S after direct de',r'\unsure{\tilde{\mathfrak S}_3|\tilde{\mathcal S}_3}',r'\mathfrak{S}_3',s_other,'The upper loop of S and a nearby descender from groupe make a separate live tilde uncertain. The unadorned reading is preferred locally, with both tilde states and both typographic alphabets retained.','misread symbol or index','image_reciproque',c_changed=True,h_changed=False,confidence='low',categories=(1,))
c13=change('Main paragraph, both occurrences of Pi',r'$\pi$. Il faut expliciter les opérations des $\tilde\sigma_a$ sur $\pi$',r'$\Pi$. Il faut expliciter les opérations des $\tilde\sigma_i$ sur $\Pi$',r'$\Pi$. Il faut expliciter les opérations des $\tilde\sigma_a$ sur $\Pi$','Both group signs have a full horizontal cap and two substantial legs, with the right leg reaching the baseline; they are locally capital Pi. The index correction is separately logged.','misread symbol or index','operations_above',c_changed=True,h_changed=False,categories=(1,))
c14=change('Main paragraph, sigma indices in opérations des and On trouve que',r'\tilde\sigma_a;\quad\tilde\sigma_a',r'\tilde\sigma_i;\quad\tilde\sigma_i',r'\tilde\sigma_a;\quad\tilde\sigma_a','Each lower index has a closed rounded body and an exit stroke, forming a rather than the short dotted i of the NB formulas.','misread symbol or index','operations_above',categories=(1,))
c15=change('Main paragraph, On trouve que', 'On trouve que','on trouve pour','On trouve que','The capital O is looped and retraced. Que has a descending q followed by a short connected u/e run, without the extra final r of pour.','misread word','operations_above')
c16=change('Main paragraph, est au dessus', 'est au dessus','ci-dessus','est au dessus','The e-s-t sequence is followed by a separate short au and then dessus; the blank between au and dessus is not a hyphen.','misread word','operations_above',categories=(2,8,9))
c17=change('Main paragraph, the sigma inside phi',r'\varphi(\overset{\deleted{\sim}}{\dot\sigma}_a)',r'\varphi(\tilde\sigma_i)',r'\varphi(\overset{\deleted{\sim}}{\dot\sigma}_a)','The sigma has an independent dot above it, a separately crossed upper wavy mark, and a closed a below. H makes the old tilde live and reads i for the lower loop.','misread symbol or index','plane_and_lacets',categories=(1,7))
c18=change('Main paragraph, description of the plane',r'plan passant par $P,\bar P,',r'plan $(P,\overline P,',r'plan passant par $P,\bar P,','Passant has the long opening p and the s/s/a/n/t run; par follows separately. No opening parenthesis precedes P.','misread word','plane_and_lacets',categories=(2,9))
c19=change('Main paragraph, deleted point-name and live i',r'\deleted{\unsure{a_i}}i',r'a_i)',r'\deleted{\unsure{a_i}}i','A short old cluster is heavily scratched out; its a_i reading stays tentative. A distinct live dotted i follows it, then a comma. No closing parenthesis is written here.','deletion state','plane_and_lacets',confidence='medium',categories=(3,7,9))
c20=change('Main paragraph, images of the three loops',r'qui transforme $l_0$ en $l_0^{-1}$, $\deleted{l}l_\infty$ en $l_1^{-1}$, $l_1$ en $l_\infty^{-1}$ :',r'qui transforme les lacets $l_0^{-1}$, \struck{\ill{}} $l_1$ \uncertain{en} $l_\infty^{-1}$ \struck{\ill{}} :',r'qui transforme $l_0$ en $l_0^{-1}$, $\deleted{l}l_\infty$ en $l_{\unsure{1|0}}^{-1}$, $l_1$ en $l_\infty^{-1}$ :','The first l0 is at the end of the preceding line, followed by en l0^-1. A locally crossed l precedes the live l-infinity. The first following right-member index is a dark narrow upright over a small old loop: 1 is preferred, with 0 retained. The final l1 en l-infinity^-1 and colon are clear; les lacets is not written.','readable ink left as \\ill{}','plane_and_lacets',confidence='medium',marked='yes',categories=(1,3,5,7,9))
c21=change('Transport margin, prose preceding the group sign','Ce sont celles obtenues par transport de structure, via les opérations de',r'ce \uncertain{sont elles} \ill{} \uncertain{transport de structure} \ill{} des \ill{}','Ce sont celles obtenues par transport de structure, via les opérations de','The capital C/e and sont are separate; celles has an opening c before the paired tall l strokes. Obtenues, par, transport de structure and via les opérations de can be read along their slanted baselines.','readable ink left as \\ill{}','transport_margin',marked='yes',categories=(2,5))
c22=change('Transport margin, ornate S with subscript 3',r'\unsure{\tilde{\mathfrak S}_3|\tilde{\mathcal S}_3}',r'\ill{}',s_other,'The large ornate S and its 3 are present. The elaborate upper loop and neighboring strokes do not isolate a certain independent tilde; both states and both alphabets remain explicit.','misread symbol or index','transport_margin',c_changed=True,confidence='low',marked='yes',categories=(1,5))
c23=change('Transport margin, base pair',r'(U,P)',r'(\overline P,P)',r'(U,P)','The first letter has two uprights joined by a low curve, making U. It has no upper P bowl or separate overbar.','misread symbol or index','transport_margin',categories=(1,))
c24=change('Transport margin, end punctuation',r'$(U,P)$.',r'$(\overline P,P)$',r'$(U,P)$','No independent dark full stop follows the closing parenthesis. The larger following strokes in the rotated crop belong to horizontal passant/par, not to the marginal note.','text not on the page','transport_margin',c_changed=True,h_changed=False,categories=(9,))
c25=change('System (14), both continuation sequences',r'\cdots;\quad\cdots',r'\ldots;\quad\ldots',continuation_upper+';\n'+continuation_lower,'Each sequence has four separated marks. The first mark of the upper sequence is blot/star-like and the other three are short strokes; the lower sequence consists of four short strokes. Geometry and count are preserved without assigning an asterisk operator.','drawing or diagram','formula14',c_changed=True,categories=(4,10))
c26=change('Critique margin, heading underline',r'\uline{Critique}','Critique',r'\uline{Critique}','A separate straight line runs beneath Critique and ends after its final letter.','other','critique_margin',categories=(10,))
c27=change('Critique margin, complete notation proposal',critique,r'\marginal{Critique \ill{} $\tilde\sigma_0$ \ill{} \uncertain{s-groupe} \ill{} \ill{} il \uncertain{vaut mieux} écrire $\tilde\sigma_0$ \ill{} \uncertain{plusieurs} \ill{}}',critique,'The slanted prose is readable, including La notation, suggère plutôt, au dessus de, il vaut mieux écrire, et noter, au lieu de, ou mieux, sans, pour réserver, à des éléments de, cf plus bas. Both sigmas in dot-sigma-prime = dot-sigma tau have separate dots; tau is undotted. The later tildes and primes, the three-element index set and S E are visible. The black ou beside the set belongs to this margin, not to a main-line exponent.','readable ink left as \\ill{}','critique_margin',marked='yes',categories=(1,3,5,6,8))
c28=change('Presentation paragraph, verb after (1)','font','forment','font','A tall f is followed by the short connected o-n-t run; the r/m sequence required by forment is absent.','misread word','relations_font')
c29=change('Presentation paragraph, group name after présentation de',r'\tilde{\mathcal E}',r'\widetilde{\Sigma}',r'\tilde{\mathcal E}','The rounded E-like body has a separate wavy tilde; it does not have an angular Sigma outline.','misread symbol or index','elimination',categories=(1,))
c30=change('Presentation paragraph, si on veut','si on veut',r'\uncertain{(si on veut)}','si on veut','The three words run continuously between peut and éliminer, with no parenthesis before si or after veut.','text not on the page','elimination',marked='yes',categories=(9,))
c31=change('Presentation paragraph, en omettant',r"\unsure{(}en omettant d'écrire",r"\uncertain{se contentant} d'écrire",r"\unsure{(}en omettant d'écrire",'En is followed by a rounded o and the connected m/e/t/t/a/n/t sequence. The possible opening parenthesis is entangled with the slanted margin and remains doubtful.','misread word','elimination',marked='yes')
c32=change('Introduction to systems (15) and (16), remonter dotted tau en trois',r'On peut maintenant remonter $\dot\tau$ en trois',r'On peut maintenant \uncertain{revenir} à \uncertain{nos} trois',r'On peut maintenant remonter $\dot\tau$ en trois','Remonter has the m-shaped middle and tall t; a separate dotted tau follows, then en trois. There are no words à nos in that position.','misread word','remonter',marked='yes',categories=(1,2,3))
c33=change('Introduction to (15), manières','manières',r'\ill{}','manières','The m/a/n start, dotted i, accented e and following r/e/s are present on the second line before the comma.','readable ink left as \\ill{}','remonter',marked='yes',categories=(5,))
c34=change('Introduction to (15), after manières comma','à savoir',r'$\sigma$ \uncertain{par}',r'à \unsure{sv|savoir}','The first sign is a small a with an accent. The following writing is very compressed: a tall returning stroke and short upper run do not certify all letters of savoir. The short form sv is preferred, with savoir retained as an alternative; no sigma/par reading is imposed.','abbreviation expanded or spelling modernised','remonter',c_changed=True,confidence='low',marked='yes',categories=(2,8))
c35=change('Lower-right handwritten page number',r'\mspage{20}','',r'\mspage{20}','A hooked 2 and closed oval 0 are clearly written above the bottom edge. H has no transcription of this source number; editorial page identification is separate.','omission','footer20',categories=(3,))

decisions=[]
def decide(dest,ident,decision,reading,ink,crop,confidence='low',**more):
    dest.append(dict(id=ident,decision=decision,reading=reading,ink=ink,crop=crops[crop]['crop'],box=crops[crop]['box'],confidence=confidence,**more))
decide(decisions,'M0843','undecided',s_first,'The ornate alphabet remains unresolved. A separate heavily cancelled upper mark is present; its underlying tilde is retained as doubtful.','upper_e_s_marks')
decide(decisions,'M0844','undecided',s_other,'The upper loop of S and nearby groupe descender prevent a secure independent-tilde reading. Both alphabet and adornment alternatives are retained, preferring the unadorned local outline.','image_reciproque')
decide(decisions,'M0845','undecided',s_other,'The margin has an ornate S3, but neighboring strokes and the letter\'s own loop do not isolate a definite tilde.','transport_margin')
decide(decisions,'M0846','undecided',r'\unsure{(}','Curved strokes before en overlap the slanted margin; a distinct opening parenthesis cannot be separated with certainty.','elimination')
unlisted=[]
decide(unlisted,'U021-01','undecided',r'\unsure{=\rho}','The equals-like strokes and descending rho are partly recoverable, but the scribble crosses the upper letter body and bar region.','heading_system13',place='Cancelled parenthesis in (13)',C_mark=r'\unsure{=\rho}')
decide(unlisted,'U021-02','undecided',r'\unsure{a_i}','The old short point-name is blackened; neither the full a nor its proposed lower i can be certified through the cancellation.','plane_and_lacets',place='Cancelled point-name before live i',C_mark=r'\unsure{a_i}')

doubts=[]
def doubt(place,reading,alternatives,reason,confidence='low'):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
for d in decisions+unlisted:
    doubt(d.get('place',d['id']),d['reading'],['the displayed alternatives or tentative reading'],d['ink'],d['confidence'])
doubt('First ornate S, identity of the cancelled upper mark',r'\deleted{\unsure{\sim}}',[r'\sim','an obscured upper mark'],'The separate mark is certainly cancelled, but its underlying complete shape is not exposed.')
doubt('Main loop-image sentence, first right member after l-infinity',r'l_{\unsure{1|0}}^{-1}',['1','0'],'A narrow dark upright overlies a small loop. One is preferred, but the old rounded component prevents full exclusion of zero.','medium')
doubt('Introduction to (15), word after à',r'\unsure{sv|savoir}',['sv','savoir'],'Only a highly compressed returning stroke and short upper run are clear; a spelled-out word and an abbreviation cannot be distinguished securely.')

inventory=[]
def inv(kind,position,reading,box):
    inventory.append(dict(element=f'I{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=reading,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('text','Top opening line',heading,[352,68,935,131])
inv('display','Top main column, numbered system (13)',system13,[300,123,1338,365])
inv('deletion','Over rho at the end of the second row of (13)',r'\overset{\deleted{\sim}}{\rho}',[934,171,1029,240])
inv('deletion','Parenthesis following that rho',r'\deleted{(\unsure{=\rho})}',[1000,175,1111,274])
inv('deletion','Over rho cubed in the third row of (13)',r'\overset{\deleted{\sim}}{\rho}{}^3',[440,270,549,365])
inv('margin note','Upper-left slanted NB note',nb,[24,263,303,723])
inv('display','General identity in NB',r'\rho\tilde\sigma_i\rho^{-1}=\tilde\sigma_{\dot\rho i}',[24,263,303,510])
inv('display','Three explicit conjugations in NB',r'\rho\tilde\sigma_0\rho^{-1}=\tilde\sigma_1;\quad\rho\tilde\sigma_1\rho^{-1}=\tilde\sigma_\infty;\quad\rho\tilde\sigma_\infty\rho^{-1}=\tilde\sigma_0',[24,407,284,723])
inv('text','Main paragraph from image réciproque through the loop images',prose1+prose2+prose3,[244,302,1636,1187])
inv('deletion','Above the first ornate S inside phi',r'\deleted{\unsure{\sim}}',[1050,315,1135,356])
inv('deletion','Upper mark above dotted sigma in the plane description',r'\overset{\deleted{\sim}}{\dot\sigma}_a',[466,858,547,942])
inv('deletion','Old point-name before live i',r'\deleted{\unsure{a_i}}',[792,1009,854,1060])
inv('insertion','Live replacement i immediately after the old point-name','i',[852,991,897,1054])
inv('deletion','First l in the doubled l before l-infinity',r'\deleted{l}',[505,1106,557,1166])
inv('margin note','Middle-left slanted transport note',transport,[24,740,387,1194])
inv('display','Middle main column, numbered system (14)',system14,[214,1228,1451,1477])
inv('drawing','Second row of (14), continuation after the first formula',continuation_upper,[760,1358,842,1396])
inv('drawing','Third row of (14), continuation below the first column',continuation_lower,[434,1433,527,1469])
inv('margin note','Long lower-left slanted Critique',critique,[16,1128,440,2288])
inv('text','Main paragraph after (14)',relations+eliminate,[224,1480,1663,1910])
inv('text','Two-line introduction to (15)',remonter,[257,1920,1538,2116])
inv('display','Bottom-left system (15)',r'(15)\quad\tau_0=\sigma_0\tilde\sigma_0=\tilde\sigma_0\sigma_0;\quad\tau_1=\sigma_1\tilde\sigma_1=\tilde\sigma_1\sigma_1;\quad\tau_\infty=\sigma_\infty\tilde\sigma_\infty=\tilde\sigma_\infty\sigma_\infty',[278,2112,992,2325])
inv('display','Bottom-right consequence donc (16)',r'\text{donc}\quad(16)\quad\tau_0^2=1;\quad\tau_1^2=1;\quad\tau_\infty^2=1',[1074,2092,1379,2325])
inv('text','Lower-right handwritten number',r'\mspage{20}',[1537,2270,1640,2340])

second=[]
def sb(kind,coords,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,coords=coords,reading=reading))
sb('Opening lexical disagreement; complete numbered system (13), numeric indices/exponents and all local cancellations',[300,68,1338,365],heading+'\n'+system13)
sb('Complete NB margin including all formulas, dotted index, inverse exponents and punctuation',[24,263,303,723],nb)
sb('First two prose lines, E/S upper marks and states, numeric index 3, subgroup index 2 and one-half',[274,302,1636,525],prose1)
sb('Pi case, both sigma-a indices, On trouve que and est au dessus',[276,540,1620,841],prose2)
sb('Plane description, dotted sigma and cancelled tilde, point-name deletion/replacement, all loop images and inverse indices',[244,853,1522,1187],prose3)
sb('Complete transport margin, every word, ornate S3 state, pair (U,P), end punctuation',[24,740,387,1194],transport)
sb('Complete numbered system (14), all formula numerals/exponents and both four-mark continuations',[214,1228,1451,1477],system14)
sb('Complete Critique margin: underlined heading, dots/tildes/primes, index set, all prose and final ellipsis',[16,1128,440,2288],critique)
sb('Presentation statement beginning, references (13),(14),(1), full fundamental relation and font',[224,1480,1616,1692],relations)
sb('Presentation statement ending, E tilde, si on veut, ambiguous opening parenthesis and en omettant',[225,1695,1663,1910],eliminate)
sb('Complete two-line remonter introduction, dotted tau and uncertain word/abbreviation',[257,1920,1538,2116],remonter)
sb('Both complete bottom systems (15),(16), every handwritten formula number, index and exponent',[278,2092,1379,2325],systems15_16)
sb('Handwritten footer 20 omitted by H',[1537,2270,1640,2340],r'\mspage{20}')

mapping={
1:('macro/editorial',[], 'C scan marker is editorial.'),
2:('substantive',[c01],'Opening words.'),
3:('macro/editorial',[],'gathered/cases syntax only.'),
4:('macro/editorial',[],'The comma token is from H\'s thin-space command \\, after rho, not literal punctuation.'),
5:('substantive',[c03],'Partial reading retained inside the cancellation.'),
6:('substantive',[c04,c05,c06,c07,c08],'Long alignment shift spans the NB note and the beginning of the main paragraph. NB placement is marginal; formula content and main lexical readings are explicitly covered.'),
7:('substantive',[c07,c08],'Réciproque and E with live tilde.'),
8:('substantive',[c09],'Alphabet uncertainty remains; the ink additionally requires cancellation of the separate upper mark.'),
9:('substantive',[c10],'Inclusion sign, not equals.'),
10:('substantive',[c11],'D\'indice, not diédral.'),
11:('macro/editorial',[],'LaTeX fraction 1/2 and the single-character half encode the same written fraction.'),
12:('substantive',[c12],'Second ornate S retains alphabet and tilde-state alternatives.'),
13:('substantive',[c14],'Closed a index.'),
14:('substantive',[c15],'Que, not pour; source capital On retained.'),
15:('substantive',[c14,c16],'Second a and the words est au dessus.'),
16:('substantive',[c17],'A index inside phi, together with the dotted/cancelled-tilde state.'),
17:('substantive',[c18],'Passant par is present; the alleged parenthesis is absent.'),
18:('substantive',[c19],'Old point-name cancelled, live i followed by comma.'),
19:('substantive',[c20],'No words les lacets at this place.'),
20:('substantive',[c20],'All three written loop images, the locally deleted l, and the doubtful first right-member index are preserved.'),
21:('substantive',[c21,c22,c23,c24],'Complete transport margin; H places fragmentary marginal matter later.'),
22:('macro/editorial',[],'array/cases syntax only.'),
23:('macro/editorial',[],'Adjacent math tokens versus H thin-space command \\,; no comma is written.'),
24:('macro/editorial',[],'Comma token belongs to H \\, thin-space command.'),
25:('macro/editorial',[],'Adjacent math tokens versus H \\, thin-space command.'),
26:('macro/editorial',[],'Comma token belongs to H \\, thin-space command.'),
27:('macro/editorial',[],'Adjacent math tokens versus H \\, thin-space command.'),
28:('macro/editorial',[],'Comma token belongs to H \\, thin-space command.'),
29:('macro/editorial',[],'Adjacent math tokens versus H \\, thin-space command.'),
30:('macro/editorial',[],'Comma token belongs to H \\, thin-space command.'),
31:('macro/editorial',[],'Environment closure/invisible-delimiter syntax. The source continuation-mark count is separately corrected in s021-25.'),
32:('substantive',[c26,c27],'Critique heading and complete margin note.'),
33:('substantive',[c27],'Critique source prose is retained; H text here is an editorial explanation of the main loop sentence.'),
34:('substantive',[c27],'Critique notation proposal and formula, not H editorial prose.'),
35:('substantive',[c27],'Continuation of the complete Critique.'),
36:('substantive',[c27],'The full three-element index set belongs to the Critique.'),
37:('substantive',[c27],'Remaining Critique, including sans tilde, S E and cf plus bas.'),
38:('macro/editorial',[],'Adjacent math tokens 1l versus 1 l differ only in source spacing.'),
39:('substantive',[c28],'Font, not forment.'),
40:('substantive',[c29],'E with tilde, not Sigma.'),
41:('substantive',[c30],'No opening parenthesis before si.'),
42:('substantive',[c30],'No closing parenthesis after veut.'),
43:('substantive',[c31],'En omettant is readable; the separate C opening-parenthesis doubt remains.'),
44:('substantive',[c32],'Remonter dotted tau en, not revenir à nos.'),
45:('substantive',[c33],'Manières is written.'),
46:('substantive',[c34],'Clear à followed by a compressed uncertain word or abbreviation; H sigma/par not adopted.'),
47:('macro/editorial',[],'aligned/cases syntax only.'),
48:('macro/editorial',[],'Environment closure/invisible-delimiter syntax only.'),
49:('macro/editorial',[],'aligned/cases syntax only.'),
50:('substantive',[c04,c05,c06],'H serializes the marginal NB after the main formulas; the substantive index, missing row and punctuation are covered.'),
51:('substantive',[c04,c05,c06,c21,c22,c23,c24,c26,c27,c35],'Long tail spans the three displaced marginal notes and the handwritten footer 20 omitted by H. H notes and end-document command are editorial.'),
}
with (PACKET/'differences.tsv').open(encoding='utf-8',newline='') as f:
    assert len(list(csv.DictReader(f,delimiter='\t')))==len(mapping)==51
coverage=[]
for row,(status,ids,explanation) in mapping.items():
    item=dict(row=row,status=status,explanation=explanation)
    if ids:item['change_id']=ids[0] if len(ids)==1 else ids
    coverage.append(item)

report=dict(scan=21,reader='/root/reader_a',lines_read=50,
layout='Text sheet in his hand, upright, with no manuscript header number. A main opening and system (13) occupy the top; a long central prose block leads to system (14), a presentation paragraph, a two-line introduction and paired bottom systems (15),(16). Three left-margin notes are slanted: NB, the transport-of-structure note and a long underlined Critique. Handwritten 20 is lower right. The read count includes 25 main text/display/footer baselines and 25 marginal baselines.',
changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
notation=[
 dict(observation='The two Pi group names in the prose have full horizontal caps and two substantial legs.',places=['after et de','after sur'],qualification='Read locally as capital Pi. The separate Gamma after the inclusion sign has only a short right upper tip.'),
 dict(observation='The three prose sigma indices are closed a forms.',places=['opérations des sigma_a','On trouve que sigma_a','phi of dotted sigma_a'],qualification='These a indices are retained, without replacing them by the i used in the NB and Critique.'),
 dict(observation='Dotted, tilded and unadorned sigmas are distinguished.',places=['NB general identity','phi in the main paragraph','Critique equation','systems (13)–(16)'],qualification='The main phi has a live dot and cancelled upper tilde; the Critique equation has two dotted sigmas and an undotted tau.'),
 dict(observation='Ornate S3 occurs three times, with problematic upper marks.',places=['inside phi','after direct de','transport margin'],qualification='The first separate upper mark is cancelled; the other two may be unadorned or tilded. Font family remains unresolved at every occurrence.'),
 dict(observation='System (14) has four continuation marks at each of two places.',places=['second-row continuation','third-row continuation'],qualification='The first upper mark is blot/star-like; no semantic asterisk is inferred.'),
],
hand=[
 dict(observation='The closed a index can be mistaken for a dotted i when a small detached contact mark is nearby.',places=['three prose sigma_a occurrences'],universal_on_page=False,witness_effect='H reads i in all three places.'),
 dict(observation='Slanted marginal writing crosses the vertical level of horizontal main prose.',places=['black ou beside the Critique index set','main fundamental relation','possible parenthesis before en omettant'],universal_on_page=False,witness_effect='The black ou is not a main-line exponent; the opening-parenthesis reading remains uncertain because the baselines overlap.'),
 dict(observation='An ornate S upper curl and neighboring g descender can resemble a separate tilde.',places=['second main ornate S','transport-note S'],universal_on_page=False,witness_effect='C gives live tildes; the local state alternatives are now preserved explicitly.'),
 dict(observation='Compressed cursive may conceal whether a word is abbreviated.',places=['after à before system (15)'],universal_on_page=False,witness_effect='C reads savoir; H reads sigma/par. The local word remains doubtful rather than expanded with certainty.'),
],
abbreviations=[
 dict(form='NB',expansion='nota bene',place='upper-left note'),
 dict(form='i.e',expansion='id est',place='NB general identity; no terminal stop visible'),
 dict(form='i.e.',expansion='id est',place='main plane description; terminal stop visible'),
 dict(form='ss-groupe',expansion='sous-groupe',place='index-two qualification'),
 dict(form='p.r.',expansion='par rapport',place='plane-symmetry description'),
 dict(form='cf',expansion='confer',place='Critique, cf plus bas'),
 dict(form='sv (possible reading only)',expansion='savoir',place='uncertain compressed word after à before (15)'),
],
notes=[
 'The author writes relations (13) for the tilded sigmas and states parenthetically that rho³=1 follows from the preceding relations. Two rho tildes and a parenthetic old (=rho) are cancelled. The NB gives the general cyclic conjugation rule and its three explicit cases. No proof check was carried out by this reader.',
 'The main prose calls the inverse image E-tilde a semidirect product involving the ornate S3 and Pi, then seeks the actions of the tilded sigmas on Pi. Its indices are written a at three places, although i is used elsewhere. The dotted sigma inside phi has its former tilde crossed out. The plane-point name a_i is cancelled before a live i, and an old l is cancelled before l-infinity; both cancellations are preserved.',
 'A newly recorded cancellation lies over the first ornate S inside phi. The underlying upper sign is tentatively a tilde. E immediately to its left has a clear live tilde. The other two ornate S upper signs cannot be securely separated from their curls and neighboring prose; both adornment states and both typographic alphabets remain explicit.',
 'System (14) gives the conjugations of the loop generators and continues with two four-mark sequences. The long Critique proposes changing the notation to dotted sigma-prime = dotted sigma times undotted tau, then using primed sigmas, while reserving tilded primed symbols for elements of S E. The underlined heading and full readable prose are retained, including cf plus bas and its three-dot ellipsis.',
 'The following paragraph says (13), (14) and the fundamental relation present E-tilde and that rho can be eliminated by omitting its defining relation. The author then writes three proposed lifts of dotted tau in (15) and their square-one relations in (16). These are transcribed claims, not independently verified conclusions. The opening parenthesis before en omettant remains doubtful; the compressed word after à before (15) also remains uncertain.',
 'There is no date or manuscript header number. The handwritten footer is 20, counted as a source omission from H separately from its editorial apparatus. H thin-space commands in the formulas are not mistaken for manuscript commas. The main i.e. has a terminal stop, while the NB i.e and the transport note ending (U,P) do not have independently visible terminal stops.',
 'Every main and marginal baseline was read from the whole sheet and native halves, followed by a deletion/insertion audit and thirteen saved locus crops. The thirteenth crop covers upper marks clipped from the first prose crop; it does not repeat a decided upper-mark reading. No OCR, external research, other-page inspection, mathematical check or TeX compilation was used. Root reviewed the crops concurrently; remaining uncertainties are explicit.',
],check_events=[],diff_coverage=coverage)

assert all(x['c_changed'] or x['h_changed'] for x in changes)
assert [x['id'] for x in decisions]==[f'M{x:04d}' for x in range(843,847)]
assert all((ROOT/'edition'/x['crop']).is_file() for x in changes+decisions+unlisted)
assert len(re.findall(r'(?<!\\)\{',page))==len(re.findall(r'(?<!\\)\}',page))
(OUT/'145_scan021.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(changes=len(changes),decisions=len(decisions),unlisted_decisions=len(unlisted),doubts=len(doubts),inventory=len(inventory),second_boxes=len(second),diff_rows=len(coverage),crops=len(crops))))
