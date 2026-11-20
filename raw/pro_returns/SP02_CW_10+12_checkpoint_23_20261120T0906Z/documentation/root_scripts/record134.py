from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,134);ch=r.change
k=r'\rlap{\(j\)}k'
al=r'\deleted{a\unsure{\rlap{t}l|l}ors}'
pl=r'\unsure{pl\rlap{t}ûtôt|plûtôt}'
fi=r'fi\rlap{d}è\rlap{d}èle'
ca=r'c\unsure{\rlap{n}a\rlap{n}a|aa|an|na}onique'
r.edit(r'\deleted{\unsure{j|t}}k',k)
r.edit('un bifoncteur $\\otimes$','un bifoncteur $\\unsure{\\otimes|\\Omega}$')
r.edit(r'\deleted{alors}',al)
r.edit(r"s\deleted{e}'envoie",r"s\rlap{e}'envoie")
r.edit(r'8\handwritten{)}',r'8\handwritten{!)}')
r.edit(r'\unsure{plûtôt|plutôt}',pl)
r.edit(r'\unsure{fi\`{d}èle|fièèle|fidèle}',fi)
r.edit(r'\deleted{\unsure{de caté}}',r'\deleted{de caté}')
r.edit(r'un\deleted{\unsure{e|x}}',r'un\deleted{e}')
r.edit(r'do\deleted{j}nt',r'do\rlap{j}nt')
r.edit(r'\unsure{pr\deleted{i}opriétés|pròpriétés|propriétés}',r'pr\rlap{i}opriétés')
r.edit(r'\deleted{(NB $\unsure{i|1}$}',r'\deleted{(NB $i$}')
r.edit(r'c\unsure{aa|an|na}onique',ca)
def leader(text,width):
 return r'''\begin{tikzpicture}[baseline=-.6ex,x=1cm,y=1cm]
\node[anchor=west,inner sep=0] at (0,.42) {'''+text+r'''};
\draw (.06,-.24) .. controls (.02,.12) and (.34,.18) .. (.75,.2) -- ('''+str(round(width-.4,2))+r''',.2) .. controls ('''+str(width)+r''',.22) and ('''+str(width)+r''',.32) .. ('''+str(round(width-.04,2))+r''',.43);
\end{tikzpicture}'''
d=r'\inserted{\handwritten{en termes de $\Delta$}}';r.edit(d,leader(d,4.5))
u=r'\inserted{\handwritten{=k+U^{+}}}';r.edit(u, r'\text{'+leader(r'\inserted{\handwritten{$=k+U^{+}$}}',2.8)+'}')
ch('canceled opening formula',r'\deleted{\unsure{F:C\;\mathrm{Mo}|F:C\;\mathrm{Mod}}}',r'\struck{\ill{}}',r'\deleted{\unsure{F:C\;\mathrm{Mo}|F:C\;\mathrm{Mod}}}','F, colon, open C, M and round o remain visible under the x cancellation. The final covered cell does not securely distinguish an unfilled cancel from d; C alternatives retained.','cancelF; cancelFfine','readable ink left as \\ill{}','medium',False,True,True,True)
for p,c in [('C in opening sentence','Ctop'),('C in display','displayF'),('C before additive','Cadd'),('C before bifunctor','Csupp'),('C before dont','Cconcl')]:
 ch(p,'C',r'\underline{C}','C','The open capital has no separate horizontal underline beneath its baseline.',''+c,'misread symbol or index','high',False,True,False,True)
ch('overlap under first k',r'\deleted{\unsure{j|t}}k','k',k,'The earlier glyph has a dot, upright and descending left hook: j, not t. Its strokes overlap k without a separate cancellation stroke.','kcancel','deletion state','high',True,True,False,True)
ch('first typed tensor',r'\otimes',r'\otimes',r'\unsure{\otimes|\Omega}','The rounded top, crossed interior and divided flat foot leave an Omega-like construction possible. All eight typed occurrences were individually enlarged; the family is qualified at its first occurrence.','tensor1; formula1left; formula1right; Uprod; formula2left; formula2right; tensor7; tensor8','misread symbol or index','medium',True,True,False,True)
ch('second letter of canceled alors',r'\deleted{alors}',r'\struck{alors}',al,'Besides the tall l stem and foot, a distinct short crossbar survives above the blue cancellation. A t/l overlap is favored but a single distorted l remains possible.','alorset; alorsfine','misread word','medium',True,True)
ch('canceled comp punctuation',r'\unsure{comp|comp.}',r'\ill{}',r'\unsure{comp|comp.}','The c opening, o, m shoulders and descending p remain readable. A possible point meets the foot of the following cancel x, so C punctuation doubt remains.','cancelcomp; compfine','readable ink left as \\ill{}','medium',False,True,True)
ch('canceled avec appli',r'avec \unsure{appli}',r'\ill{}',r'avec \unsure{appli}','The avec letters and a, two descending p forms and tall l are visible beneath x strikes. The last canceled cell does not independently expose a secure i dot; appli remains qualified.','cancelcomp; applifine','readable ink left as \\ill{}','medium',False,True,True)
ch('tensor between U and U',r'U\otimes_k U',r'U\widehat{\otimes}_k U',r'U\otimes_k U','The tensor-like cell has clear blank paper above its rounded top. No separate hat is present; the subscript is a plain k.','Uprod','misread symbol or index','high',False,True,False,True)
ch('e overlapping apostrophe in s-envoie',r"s\deleted{e}'envoie","s'envoie",r"s\rlap{e}'envoie",'A pale e bowl and horizontal bar lie below the dark apostrophe. There is no independent deletion stroke; both impressions occupy the same position.','senv','deletion state','high',True,True)
ch('en termes de Delta leader','insertion before comma','marginal after comma','insertion before comma with curved leader','The words en termes de and triangular Delta lie above the line. Their long leader turns down between 6 and the typed comma and curls upward at the right; the text and leader are reproduced together.','deltanote; deltaupright; deltageom','drawing or diagram','high',True,True)
ch('punctuation after reference 8',r'8\handwritten{)}','8)',r'8\handwritten{!)}','An upright hand stem and separate small dot precede the closing parenthesis; a separate larger typed full stop follows. Both witnesses omit the exclamation mark.','eightparen; eightwide','omission','high',True,True)
ch('plutot spelling and overlap',r'\unsure{plûtôt|plutôt}','plutôt',pl,'Two clear circumflex peaks stand over u and o. A tall t-like stem crosses the first accented cell, crowded against the following t; that additional overlap remains qualified. Plain-u plutot is excluded by the visible first circumflex.','plutot; plutotfine','misread word','medium',True,True)
ch('fidèle letter collisions',r'\unsure{fi\`{d}èle|fièèle|fidèle}','fidèle',fi,'Both central cells show a tall d ascender and an e bowl with horizontal bar; both also carry a grave stroke. The two unlike-letter overlaps are retained without inferring typing chronology.','fidele; fidelefine','misread word','high',True,True)
ch('canceled de caté',r'\deleted{\unsure{de caté}}',r'\struck{\ill{}}',r'\deleted{de caté}','The d ascender, e, separate c-a-t-e sequence and final acute survive the x strikes. C doubt is resolved.','decat','readable ink left as \\ill{}','high',True,True,True)
ch('canceled e after un',r'\deleted{\unsure{e|x}}','omitted',r'\deleted{e}','The e upper bowl, middle bar and lower curve remain under the two diagonal cancellation strokes. The x is the cancellation rather than the underlying letter.','uncancel','deletion state','high',True,True)
ch('overlap in dont',r'do\deleted{j}nt','dont',r'do\rlap{j}nt','A dotted j with a descending hook shares the n cell. The n shoulders remain visible and no independent strike crosses the j.','dont','deletion state','high',True,True)
ch('overlap in propriétés',r'\unsure{pr\deleted{i}opriétés|pròpriétés|propriétés}','propriétés',r'pr\rlap{i}opriétés','The first o contains a vertical i stem and a separate dot above it. No grave stroke or separate cancellation is present; the remaining two acute accents are visible.','proprietes','deletion state','high',True,True)
ch('canceled NB fragment',r'\deleted{(NB $\unsure{i|1}$}',r'\struck{\ill{}}',r'\deleted{(NB $i$}','The opening parenthesis, capital N and B, and a last dotted i remain readable below the x strikes. The separate dot excludes digit 1.','NBcancel','readable ink left as \\ill{}','high',True,True,True)
ch('inserted k plus U-positive leader','insertion text','marginal text','same insertion with curved leader','The handwritten equals, k, plus and U with raised plus lie above est le. The long curved leader descends immediately after tilde U and rises at its right end; it is reproduced in TikZ.','Utildeinsert; insertfine','drawing or diagram','high',True,True,False,True)
ch('letters in canonique',r'c\unsure{aa|an|na}onique','canonique',ca,'Both disputed cells have a-like closed lower bowls, while full-height left stems and shoulders also resemble n overprints. The raw n/a overlaps are provisional; C alternatives are retained. No reading is supplied from the expected spelling.','canonique; canoniquefine','misread word','medium',True,True)
ch('upper pale wave above last A',r'\overset{\handwritten{\unsure{\sim}}}{\overset{\handwritten{\sim}}{A}}',r'\widetilde{A}',r'\overset{\handwritten{\unsure{\sim}}}{\overset{\handwritten{\sim}}{A}}','A dark wave is clear immediately above A; a second pale, offset wave is visible farther above. Its status as another mark rather than ghosting is uncertain, so C qualified upper wave remains.','Alast; Alastwide','misread symbol or index','low',False,True,False,True)
for a,b,c,d,e in [
 ('canceled opening formula',r'F:C\;\mathrm{Mo}',r'F:C\;\mathrm{Mod}','medium','Final canceled cell does not securely reveal an ascender.'),
 ('first typed tensor',r'\otimes',r'\Omega','medium','Rounded top and divided flat foot; eight occurrences inspected.'),
 ('canceled alors second cell',r'\rlap{t}l','l','medium','Short black crossbar remains above blue cancellation.'),
 ('canceled comp punctuation','comp','comp.','medium','Possible point meets the next cancel x foot.'),
 ('canceled last word','appli','','medium','a, p, p, l are clear; final i not independently exposed.'),
 ('plûtôt overlap',r'pl\rlap{t}ûtôt','plûtôt','medium','Both circumflexes clear; additional t-like vertical in first accented cell.'),
 ('canonique two cells',r'c\rlap{n}a\rlap{n}aonique','caaonique; canonique; cnaonique','medium','Two closed bowls with n-like stems/shoulders.'),
 ('upper pale wave over last A',r'\sim','','low','A second pale wave is present; possible ghost rather than distinct writing.')]:r.doubt(a,b,c,d,e)
r.notation('typed tensor',r'first \unsure{\otimes|\Omega}, later \otimes','10:134 bifunctor; both positions in first comparison; U product; both positions in second comparison; given data; functor in conclusion','uncertain')
r.notation('plain typewritten C','C','10:134 opening; canceled formula; display; additive; given bifunctor; conclusion after sur')
r.notation('typed functor and algebra alphabets','F,U,A,X,Y,k,End,Modf,Comodf','10:134 display F/C/Modf/k; ni F; End_k(F); dual A; traverse F; Modf(U/k)=Comodf(A/k); both comparisons F(X tensor Y),F(X),F(Y); diagonal U; sur A; U tensor_k U; U sends; conclusion U; degrees U; recovered U,A')
r.notation('hand comparison and map signs',r'\longrightarrow; \simeq','10:134 display arrow; both bifunctor comparisons')
r.notation('compatibility letter and diagonal','c; hand Delta','10:134 avec c; inserted en termes de Delta')
r.notation('finite-field underline',r'\underline{F}_p','10:134 example; horizontal underbar under F only and lowered p')
r.notation('cohomological operation and inequality',r'\pi_i; >0','10:134 hand pi and typed lowered i; hand strict greater and oval zero')
r.notation('hand tildes and insertion',r'\widetilde U; \widetilde A; =k+U^+','10:134 first U and inserted equality; following A; last U; last A with qualified additional pale wave','uncertain')
r.notation('unlike letter overlaps',r'j/k; e/apostrophe; d/è twice; j/n; i/o','10:134 first corps k; s-envoie; fidèle; dont; propriétés')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:134 '+p) for a,b,p in [('i.e.','id est','diagonal application and reciprocal construction'),('NB','nota bene','canceled fragment'),('comp','composition','canceled clause, punctuation uncertain'),('appli','application','canceled clause, final letter uncertain'),('caté','catégories','canceled de caté')]]
r.r['inventory_overrides']={
 '134-08':dict(kind='text',first_words_or_objects='j/k raw overlap, no independent cancellation'),
 '134-09':dict(first_words_or_objects='canceled alors with possible t/l overprint'),
 '134-13':dict(kind='text',first_words_or_objects='e/apostrophe raw overlap in s-envoie'),
 '134-16':dict(first_words_or_objects='hand plural s in générales and astucieuses; hand !) after 8'),
 '134-17':dict(first_words_or_objects='canceled de caté, resolved'),
 '134-18':dict(first_words_or_objects='canceled e after un, resolved'),
 '134-audit-dont':dict(kind='text',first_words_or_objects='j/n raw overlap in dont'),
 '134-audit-proprietes':dict(kind='text',first_words_or_objects='i/o raw overlap in propriétés'),
 '134-21':dict(first_words_or_objects='canceled (NB i, dotted i resolved')}
extras=[('leader of en termes de Delta','drawing','interline after n°6','his hand'),('hand exclamation before closing parenthesis','insertion','after reference 8','his hand'),('possible t/u collision in plûtôt','text','line ending seraient','typewriter'),('two d/è overlaps in fidèle','text','before et additif','typewriter'),('possible n/a overlaps in canonique','text','example paragraph','typewriter'),('curved leader of =k+U-positive','drawing','interline after first tilde U','his hand')]
for i,(s,t,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:134',sheet_kind='typescript',hand=h,element=f'134-R{i:03d}',kind=t,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=sum([json.loads(Path('work/'+p).read_text()) for p in ['crops134.json','crops134_extra.json']],[])
r.r['inspection_note']='Root alone viewed whole134 and both supplied halves before opening C/H, all12 C doubt loci and all28 inventory rows. All72 crop recipes were actually viewed; tensor8 and Cconcl from a truncated output were re-viewed singly. Both hand insertions were rotated -1 degree and all mathematics, cancellations and local overprints enlarged. Both supplied halves were reread line by line before finalization. Every C doubt has an explicit decision; the unusual plûtôt, doubled grave repairs, réfléter and caa/n-like spelling are not normalized. The small hand ! before ) after 8 is added. Archival133 remains solely the comment. No OCR, parallel transcription, context access or mathematical checking occurred.'
r.save('work/record134.json')
