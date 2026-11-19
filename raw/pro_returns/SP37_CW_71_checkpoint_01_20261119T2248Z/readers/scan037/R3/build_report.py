from pathlib import Path
import json
base=Path('/workspace/scratch/9baacadb090c/work/SP37_CW_71/readers/scan037/R3')
src='/workspace/scratch/9baacadb090c/source/SP37_CW_71_scans/'
a=src+'J71-05_71_scan037_a.jpg'
b=src+'J71-05_71_scan037_b.jpg'
def cp(n): return str(base/'crops'/n)
reading=r'''\scanpage{37}\mspage{$\underline{\overline{\mathrm{X}}}$}
% P1; upper pencil objection and its detached diagonal leader.
\margin{!!}Reste le cas $\mathring{T}\cap\Gamma\ne\unsure{\phi|\varnothing}$. Considerons l'enveloppe convexe\margin{\begin{tikzpicture}[x=1mm,y=1mm,baseline]\draw (0,0)--(6,8);\end{tikzpicture}\quad ce n'est \unsure{pas une|pas un} ``\unsure{env. conv.|ens. conv.}''!} $\unsure{\mathbb{C}|C}$ de $(\mathring{T}\cup\inserted{\bigl[}]s',s''[\inserted{\bigr]})\cap\Gamma$.

% P2
On a $\mathbb{C}\subset T-([s,s']\cup[s,s''])$. Observons que $S(\partial C)\deleted{\unsure{\subset|\cap}}\cap\mathring{T}\subset S(\Gamma)$.

% P3; the detached apostrophe between il and y is visible.
Comme $\mathring{T}\cap\Gamma\ne\phi$ il'y a\deleted{\illegible{1}} au moins un sommet de $\partial C$ à l'interieur $\mathring{T}$. \unsure{Le|le} lemme $\underline{\overline{\mathrm{IV}}}$ montre qu'il existe $y\notin S(\partial C)$, $y\in\mathbb{C}$, tel que $y$ est $(\mathbb{R}^2-\mathbb{C})$-visible de $s$

% P4
(Noter aussi que $\mathring{C}\ne\phi$ puisque $\Gamma\cap\mathring{T}\ne\phi\Rightarrow\operatorname{card}(\Gamma\cap]s',s''[)\geq 2$)

% P5
Soit $\alpha\in A(\partial C)$ telle que $y\in\alpha$ le lemme V montre que tout point de $\alpha$ est $(\mathbb{R}^2-C)$-visible de $s$. Si $\alpha=[z,z']$ montrons que $z^{\deleted{\unsure{\prime}}}\notin[s',s'']$ ou bien $z^{\unsure{\prime|\prime\prime}}\notin[s',s'']$. Soit donc $z''\in\mathring{T}\cap\Gamma$ et considerons le triangle $T'$ de sommets $z,z',z''$. Si $z',z''\in[s',s'']$ on voit que $]\unsure{s|S},y[$ ($y\in]z,z'[$) coupe $\mathring{T}'$ selon un ensemble non-vide. Cela contredit le choix de $y$ puisque $\mathring{T}'\subset\mathbb{C}$, \deleted{\unsure{C.a|c.a|c.à}} donc $z'$ par exemple vérifie $z'\notin[s',s'']$, $z'\in S'(\Gamma)$ (puisque $z'\in S(\partial\mathbb{C})\cap\mathring{T}$) et le lemme \deleted{\unsure{3|5}} V montre que $z'$ est $(\mathbb{R}^2-\mathbb{C})$-visible de $s$, donc $\operatorname{int}\Gamma$-visible de $s$, c.q-f.d.
% Long left-margin pencil note, written sideways and in staggered short groups.
% Its long curved pencil rule begins beside On a and continues beside the note.
\margin{\begin{tikzpicture}[x=1mm,y=1mm]\draw (1,40)..controls (-1,27) and (-1,13)..(2,0);\draw (0,19)..controls (1,18) and (1.7,17)..(2,16);\end{tikzpicture}\par compliqué, prendre un sommet de $\Gamma$ $\in$ \deleted{\unsure{$\mathring T$|$\alpha$}} et qui est à dist. max. de la droite \deleted{\unsure{$\Delta$}} $(s's'')$}

% P6: pencil underline and exclamation marks.
\uline{Corollaire à la demonstration du lemme $\underline{\overline{\mathrm{VIII}}}$.} \margin{!!}

% P7: pencil word and its curved insertion leader.
Si $\Gamma$ est un polygone il existe un couple de sommets \inserted{\unsure{distincts}}\margin{\begin{tikzpicture}[x=1mm,y=1mm]\draw (0,0)..controls (-1,4) and (4,4)..(8,5)..controls (12,6) and (15,6)..(16,8);\end{tikzpicture}} $s,s'\in S(\Gamma)$ tels que $s'$ est \deleted{vis} $(\mathbb{R}^2-\Gamma)$-visible de $s$ et $]s',s[\subset\partial E(\Gamma)$.
% archive sheet number: 36
'''
(base/'reading.tex').write_text(reading)
issues=[]
def issue(id,place,C,H,reading,evidence,image,bbox,confidence='high',against_C=False,against_H=False,kind='other',H_marked='not applicable',C_doubt=False):
 issues.append(dict(id=id,place=place,C=C,H=H,reading=reading,evidence=evidence,image=image,bbox=bbox,confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,H_marked=H_marked,C_doubt=C_doubt))
issue('R3-01','P1 first empty-set-role glyph; repeated P3 and P4',r'\unsure{\varnothing|\phi}; later \varnothing',r'Opening literal anchor: \emptyset',r'\unsure{\phi|\varnothing}; later \phi','Half a shows an oval pierced by a steep stem projecting well above and below it. This supports phi as the first graphic candidate; the empty-set role alone does not decide the shape. Repeated forms have the same stem.',a,[305,65,525,145],'medium',True,True,'misread symbol or index','no',True)
issue('R3-02','P1 hull name; recurring reinforced C',r'\unsure{\mathbb{C}|C}',r'Literal hull anchor: C',r'\unsure{\mathbb{C}|C}, later \mathbb C for the same form','The C has short strong uprights at both right ends. The plain C in partial C has different terminals. The reinforced/serif distinction remains typographically ambiguous.',cp('01_top_note.png'),[1045,15,1540,182],'medium',False,True,'misread symbol or index','no',True)
issue('R3-03','Upper pencil objection, article and abbreviation',r'ce n\'est \unsure{pas une} ``\unsure{env. conv.}''!',r'ce n\'est pas un “ens. convexe” !',r'ce n\'est \unsure{pas une|pas un} ``\unsure{env. conv.|ens. conv.}''!','The article is a compressed low sequence with a trailing stroke that may be e. The final character of the first abbreviation remains compressed. The second word is visibly short, conv., not a fully written convexe. Paired upright quotation strokes occur on both sides.',cp('01_top_note.png'),[1045,15,1540,182],'low',True,True,'abbreviation expanded or spelling modernised','no',True)
issue('R3-04','Detached diagonal leader between convexe and hull name','Omitted','Omitted','An unheaded diagonal rising to the upper pencil objection, drawn in reading.tex','Half a shows one long pencil diagonal running from about (1065,140) to (1145,37), separated from the letters; it is not a slash through the mathematical expression.',a,[1045,22,1160,155],'high',True,True,'drawing or diagram','no',False)
issue('R3-05','P2 deleted sign after S(partial C)',r'\deleted{\unsure{\subset|\cap}}','Main text absent; covered by omission block H-P2',r'\deleted{\unsure{\subset|\cap}}','A filled rectangular obliteration hides almost the complete sign. Its faint internal strokes do not determine subset versus intersection.',cp('02_deleted_set_sign.png'),[1190,150,1550,240],'low',False,False,'deletion state','not applicable',True)
issue('R3-06','P3 obliterated word after il y a',r'\deleted{\illegible{1}}','Main text absent; covered by omission block H-P3',r'\deleted{\illegible{1}}','The black oval has no recoverable letter sequence. A tiny rightward terminal survives but does not identify a word.',cp('03_deleted_word.png'),[480,230,910,325],'low',False,False,'deletion state','not applicable',True)
issue('R3-07','P3 apostrophe between il and y','il y a','Main text absent; covered by omission block H-P3',"il'y a",'In the deletion crop, a detached raised vertical stroke stands between the completed l and the separate y; the dot of the initial i is separately present to the left. Preserve the apostrophe without grammatical correction.',cp('03_deleted_word.png'),[480,230,910,325],'high',True,False,'other','not applicable',False)
issue('R3-08','P3 initial of Le lemme IV',r'\unsure{Le|le}','Main text absent; covered by omission block H-P3',r'\unsure{Le|le}','Two overworked upright strokes and a heavy common foot remain. They do not settle whether the final initial was capital or lower-case.',cp('04_le_lemme.png'),[1440,245,1670,340],'low',False,False,'other','not applicable',True)
issue('R3-09','P3 y not in S(partial C)',r'y\unsure{\notin|\in}S(\partial C)','Main text absent; covered by omission block H-P3',r'y\notin S(\partial C)','Half a resolves the crossing stroke: a strong near-vertical stem passes through the membership sign and projects above and below its bars. No additional crop was needed.',a,[460,325,720,423],'high',True,False,'misread symbol or index','not applicable',True)
issue('R3-10','P5 first z in proposed endpoint alternative',r'z^{\deleted{\unsure{\prime}}}','Main text absent; covered by omission block H-P5',r'z^{\deleted{\unsure{\prime}}}','A short raised mark has several transverse ink strokes through it. The cancellation is clear, but the original prime is not recoverable with certainty.',cp('05_z_deleted_prime.png'),[1190,600,1470,705],'low',False,False,'deletion state','not applicable',True)
issue('R3-11','P5 second z at next line start',r'z^{\unsure{\prime|\prime\prime}}','Main text absent; covered by omission block H-P5',r'z^{\unsure{\prime|\prime\prime}}','The raised group is a nearly filled rectangular upright with a lower projection. One versus two primes cannot be separated. Unlike the preceding cancellation, distinct cross-hatching is not clear enough to assert deletion.',cp('06_z_prime.png'),[105,690,425,810],'low',False,False,'misread symbol or index','not applicable',True)
issue('R3-12','P5 interval ]s,y[',r']\unsure{s|S},y[','Main text absent; covered by omission block H-P5',r']\unsure{s|S},y[','The letter has been heavily retraced, widening and enlarging both lobes. Its case remains indeterminate; contextual identification of the point does not remove the visible doubt.',cp('07_interval_s.png'),[945,790,1195,900],'medium',False,False,'misread symbol or index','not applicable',True)
issue('R3-13','P5 cancelled group before donc',r'\deleted{\unsure{C.a|c.a|c.à}}','Main text absent; covered by omission block H-P5',r'\deleted{\unsure{C.a|c.a|c.à}}','Two round letter bodies survive under two heavy rules. The first can be C or c; the original points/accent are obscured by the crossing strokes.',cp('08_deleted_ca.png'),[300,925,560,1080],'low',False,False,'deletion state','not applicable',True)
issue('R3-14','P5 z prime belongs to S prime of Gamma',r"z'\in\unsure{S'|S}(\Gamma)",'Main text absent; covered by omission block H-P5',r"z'\in S'(\Gamma)",'A separate upright tick stands above and to the right of S, before the opening parenthesis. It is distinct from both the S terminal and parenthesis.',cp('09_S_prime.png'),[1320,965,1585,1080],'high',True,False,'misread symbol or index','not applicable',True)
issue('R3-15','P5 cancelled numeral before V',r'\deleted{\unsure{3|5}}','Main text absent; covered by omission block H-P5',r'\deleted{\unsure{3|5}}','The upper and lower curved remains are covered by horizontal and oblique hatching. Neither 3 nor 5 can be ruled out on the surviving strokes.',cp('10_deleted_number.png'),[945,1075,1120,1180],'low',False,False,'deletion state','not applicable',True)
issue('R3-16','Sideways note: article before sommet',r'\unsure{un|le|les}','Part of a passage left as ill',r'un','In the corrected upright crop, the article has two connected short humps, with no independent ascender or terminal s. Read un.',cp('11_side_note.png'),[15,725,195,1580],'medium',True,False,'misread word','yes',True)
issue('R3-17','Sideways note: membership, crossed symbol, and et',r'\unsure{$\in$} \deleted{\unsure{$\mathring T$|$\alpha$}} \unsure{et}',r'\in \Gamma followed by ill',r'$\Gamma$ $\in$ \deleted{\unsure{$\mathring T$|$\alpha$}} et','The upright view separates a membership-shaped open curve with an internal stroke and the small joined et. The crossed symbol has a loop and crossing stems, insufficient to choose ringed T or alpha. Its placement follows Gamma in the staggered note, rather than the H sequence in Gamma.',cp('11_side_note.png'),[15,725,195,1580],'medium',True,True,'insertion or placement','yes',True)
issue('R3-18','Sideways note: deleted mark after droite',r'\deleted{\unsure{$\Delta$}}','Part of a passage left as ill',r'\deleted{\unsure{$\Delta$}}','The dark triangular knot has an interior pale triangular opening and crossing ink. Delta remains a tentative reading; the exact earlier glyph and deletion detail are not securely recovered.',cp('11_side_note.png'),[15,725,195,1580],'low',False,False,'deletion state','yes',True)
issue('R3-19','Sideways pencil annotation, full text','compliqué, prendre un sommet de Gamma in [crossed ringed T/alpha] et qui est à dist. max. de la droite [crossed Delta] (s\'s\'\')',r'\ill{} \uncertain{compliqué} \ill{} $\in\Gamma$ \ill{} $(s\',s\'\')$',r'compliqué, prendre un sommet de $\Gamma$ $\in$ \deleted{\unsure{$\mathring T$|$\alpha$}} et qui est à dist. max. de la droite \deleted{\unsure{$\Delta$}} $(s\'s\'\')$','The rotated note yields the connected words compliqué, prendre, sommet, de, qui est à dist. max. de la droite. C already recovers these words; H leaves most as ill. H also supplies a comma between the endpoint labels that is not discernible in the note.',cp('11_side_note.png'),[15,725,195,1580],'medium',False,True,'readable ink left as \\ill{}','yes',False)
issue('R3-20','Long curved pencil rule beside main proof and marginal note','Omitted','Omitted','A long unheaded curved pencil rule with a short oblique branch, drawn with the margin note','The whole and half a show a thin line beginning beside On a around x110,y195, descending near x80, continuing into the marginal writing, with a short oblique branch near y750. It is visibly separate from the main-text letters.',a,[55,180,145,1320],'high',True,True,'drawing or diagram','no',False)
issue('R3-21','Corollary heading numeral',r'\unsure{VIII|VII}',r'VIII',r'VIII','Half b shows V followed by three individual upright strokes between the upper and lower rules. The last upright is present though it meets the rule. No crop was made for this settled doubt.',b,[965,1320,1050,1385],'high',True,False,'misread symbol or index','no',True)
issue('R3-22','Corollary heading spelling','demonstration',r'Literal quoted anchor: démonstration','demonstration','Half b shows no acute accent over the e in demonstration. The neighbouring à has its visible grave accent, so the source accent omission is retained.',b,[465,1320,800,1415],'high',False,True,'abbreviation expanded or spelling modernised','no',False)
issue('R3-23','Pencil insertion before s,s prime',r'\inserted{\unsure{distincts}}',r'distincts',r'\inserted{\unsure{distincts}}','The opening disti and a final tall/returning group are visible, but middle letters are compressed to low connecting strokes. Distincts remains the plausible reading, with the C uncertainty retained.',cp('12_distincts.png'),[1260,1380,1555,1520],'medium',False,False,'insertion or placement','no',True)
issue('R3-24','Curved pencil insertion leader beneath distincts','Omitted','The insertion is described, but the graphic leader is not represented','Curved unheaded insertion leader, drawn beside inserted distincts','A long curve starts below the gap after sommets, turns under the inserted pencil word, and rises at the far right. It has no clear arrowhead.',cp('12_distincts.png'),[1260,1380,1555,1520],'high',True,True,'drawing or diagram','no',False)
issue('R3-25','Corollary deleted fragment before parenthesized plane',r'\deleted{\unsure{vis}}','Main text absent; covered by omission block H-P67',r'\deleted{vis}','Half b resolves v, a central i with its separate dot, and the small final s under the cancellation rule. No crop was needed.',b,[505,1565,585,1620],'high',True,False,'deletion state','not applicable',True)
# H main-text omissions are reported only as coherent blocks, not word-by-word paraphrase differences.
blocks=[
('H-P1','P1 opening and hull construction','Reste le cas ... Considerons l\'enveloppe convexe ... de (...) cap Gamma.',r'P1 in reading.tex, from Reste le cas $\mathring T\cap\Gamma\ne\unsure{\phi|\varnothing}$ to $\cap\Gamma$.',a,[105,60,1555,180],'H supplies an editorial summary and quotes two fragments as annotation anchors; the complete diplomatic paragraph, its verb and local state are absent. The quoted glyph differences are separately listed.'),
('H-P2','P2 containment and vertex observation','On a ... Observons que ... S(Gamma).',r'P2 in reading.tex, from On a $\mathbb C\subset T-([s,s\']\cup[s,s\'\'])$ through $S(\partial C)\deleted{\unsure{\subset|\cap}}\cap\mathring T\subset S(\Gamma)$.',a,[115,157,1660,240],'The full one-line observation, including the cancelled sign, is visibly present and receives no literal transcription in H.'),
('H-P3','P3 existence of y using lemma IV','Comme ... Le lemme IV montre ... visible de s',r'P3 in reading.tex, from Comme $\mathring T\cap\Gamma\ne\phi$ to $(\mathbb R^2-\mathbb C)$-visible de $s$.',a,[115,240,1665,423],'The two-line argument, its deletion and its quantifiers are absent as transcription; mentioning lemma IV in a summary does not transcribe them.'),
('H-P4','P4 parenthetical nonempty interior/cardinality claim','(Noter aussi que ... >=2)',r'P4 in reading.tex, complete parenthesis beginning (Noter aussi que $\mathring C\ne\phi$ and ending $\operatorname{card}(\Gamma\cap]s\',s\'\'[)\ge2$).',a,[110,420,1600,505],'The parenthetical line is fully visible; H gives no literal counterpart.'),
('H-P5','P5 edge argument and proof conclusion','Soit alpha ... c.q-f.d.',r'P5 in reading.tex, entire proof block from Soit $\alpha\in A(\partial C)$ through donc $\operatorname{int}\Gamma$-visible de $s$, c.q-f.d.',a,[110,520,1620,1290],'H quotes only the opening as a location for its marginal note. All of the subsequent edge/triangle argument and proof ending are absent as a diplomatic transcription.'),
('H-P67','P6 heading and P7 corollary','Corollaire ... Si Gamma ... partial E(Gamma).',r'P6--P7 in reading.tex, from Corollaire à la demonstration du lemme VIII. through $]s\',s[\subset\partial E(\Gamma)$.',b,[160,1295,1580,1645],'H paraphrases the statement in note and quotes the heading in marginal, but does not transcribe the two-line corollary and its cancelled vis. The heading accent difference and insertion graphics are separately recorded.')]
for id,place,C,reading_,im,box,evidence in blocks:
 issue(id,place,C,'Editorial summary/annotation anchor only; full main-text block absent',reading_,evidence,im,box,'high',False,True,'omission','no',False)
inventory=[]
def inv(element,kind,position,words,hand='another unnamed hand (main ink)'):
 inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inv('P1 case and hull construction','text','top main line','Reste le cas')
inv('P2 containment and observation','text','second main line','On a C subset T')
inv('P3 choice of y','text','third and fourth main lines','Comme ringed T cap Gamma')
inv('P4 parenthetical observation','text','fifth main line','(Noter aussi que')
inv('P5 proof with edge and auxiliary triangle','text','middle to proof conclusion','Soit alpha in A(partial C)')
inv('P6 heading','text','lower main area','Corollaire à la demonstration du lemme VIII.')
inv('P7 corollary statement','text','two lines beneath heading','Si Gamma est un polygone')
inv('First exclamation marks','margin note','left of opening line','!!','another unnamed hand (dark annotation; ink/pencil medium not secure)')
inv('Upper objection','margin note','above right end of opening line',"ce n'est pas une/un env./ens. conv.",'another unnamed hand (pencil)')
inv('Upper diagonal leader','drawing','between convexe and the reinforced C, rising toward objection','unheaded diagonal','another unnamed hand (pencil)')
inv('Closed-interval bracket additions','insertion','within first-line hull formula','large added [ and ] outside the original open interval','another unnamed hand (black ink addition)')
inv('Deleted set sign','deletion','after S(partial C) in P2','subset/cap under filled rectangle')
inv('Deleted word','deletion','after il\'y a in P3','one illegible word under filled oval')
inv('Overworked initial','insertion','before lemme IV','Le/le, earlier form not recoverable')
inv('Deleted endpoint prime','deletion','first endpoint alternative in P5','raised prime under hatching')
inv('Cancelled connective fragment','deletion','before donc z prime in P5','C.a/c.a/c.à')
inv('Cancelled lemma numeral','deletion','before V in P5','3/5')
inv('Long sideways annotation','margin note','left margin beside middle/lower proof','compliqué, prendre un sommet de Gamma','another unnamed hand (pencil)')
inv('Long pencil rule and branch','drawing','left of proof from On a downward beside annotation','long curved rule, short branch near note opening','another unnamed hand (pencil)')
inv('Crossed symbol within sideways note','deletion','after membership-like sign near Gamma','ringed T/alpha','another unnamed hand (pencil annotation; crossed symbol dark)')
inv('Crossed triangular symbol within sideways note','deletion','after droite','Delta, uncertain','another unnamed hand (pencil annotation; crossed symbol dark)')
inv('Heading underline','insertion','beneath corollary heading','single long pencil underline','another unnamed hand (pencil)')
inv('Second exclamation marks','margin note','right of corollary heading','!!','another unnamed hand (pencil)')
inv('Distincts insertion','insertion','above gap before s,s prime in corollary','distincts, uncertain','another unnamed hand (pencil)')
inv('Distincts curved leader','drawing','under inserted word, returning to gap before s,s prime','unheaded curved insertion leader','another unnamed hand (pencil)')
inv('Deleted vis','deletion','last main line after est','vis')
doubts=[]
def doubt(place,reading_,alts,conf,reason): doubts.append(dict(place=place,reading=reading_,alternatives=alts,confidence=conf,reason=reason))
doubt('First empty-set-role glyph',r'\phi',[r'\varnothing'],'medium','Stem is nearly vertical, but a graphic empty-set variant remains possible; role does not decide.')
doubt('Hull name',r'\mathbb C',['C with reinforced terminals'],'medium','Two terminal uprights are clear; whether they encode a distinct alphabet is not absolutely settled.')
doubt('Upper pencil article','pas une',['pas un'],'low','Compressed final trace may be e.')
doubt('Upper pencil abbreviation','env. conv.',['ens. conv.'],'low','The end of the first abbreviation is compressed; second is visibly abbreviated.')
doubt('P2 erased sign',r'\subset',[r'\cap'],'low','Filled rectangle conceals nearly all original strokes.')
doubt('P3 erased word',r'\illegible{1}',[],'low','No word is recoverable.')
doubt('P3 initial','Le',['le'],'low','Overwriting confounds initial case.')
doubt('P5 first z raised cancellation',r'\deleted{\prime}',[],'low','Superscript location supports a prime but the original stroke is hidden.')
doubt('P5 second z raised group',r'\prime',[r'\prime\prime'],'low','Solid raised group does not separate into one or two ticks; deletion state is also not secure.')
doubt('P5 interval endpoint','s',['S'],'medium','Heavy retracing makes case uncertain.')
doubt('P5 cancelled connective','C.a',['c.a','c.à'],'low','Rules conceal points/accent and precise case.')
doubt('P5 cancelled numeral','3',['5'],'low','Overlapping curves and hatching remain ambiguous.')
doubt('Side note crossed symbol',r'\mathring T',[r'\alpha'],'low','Loop and crossing stems can be read either way.')
doubt('Side note triangular cancellation',r'\Delta',[],'low','Triangular knot is compatible with delta, but original strokes/deletion state remain uncertain.')
doubt('Pencil insertion','distincts',[],'medium','Opening and final group visible; middle letters are heavily compressed.')
notation=[
 {'sign':'Polygon and boundary/hull','reading':r'\Gamma, E(\Gamma), \partial E(\Gamma)','verification':'Angular single-top-bar Gamma, three-bar E and looped partial are present; no J prefix occurs on this page.'},
 {'sign':'Reinforced hull letter','reading':r'\unsure{\mathbb C|C}; plain C in \partial C and first edge visibility formula','verification':'Short right-end uprights distinguish repeated reinforced forms from plain-end C; first occurrence remains uncertain.'},
 {'sign':'Interior marks','reading':r'\mathring T, \mathring C, \mathring T\prime','verification':'Hollow small circles, not dots/hats, are visible above T/C. The prime to the right of T is separate.'},
 {'sign':'Empty-set-role glyph','reading':r'\unsure{\phi|\varnothing}, then \phi','verification':'Repeated pierced oval with tall nearly vertical stem.'},
 {'sign':'Vertices and edge','reading':r's,s\prime,s\prime\prime,z,z\prime,z\prime\prime,\alpha','verification':'Separate one/two raised ticks are clear except the two overwritten endpoint groups reported as doubts.'},
 {'sign':'Set relations','reading':r'\subset,\cap,\cup,\in,\notin','verification':'Open inclusion, intersection arches and union cups checked against both halves. y notin S(partial C) is settled by crossing stroke.'},
 {'sign':'Intervals','reading':r'[s,s\prime], [s,s\prime\prime], ]s\prime,s\prime\prime[, ]s,y[, ]z,z\prime[','verification':'Inward/outward bracket ends checked; large added closed pair around opening open interval is preserved.'},
 {'sign':'Operators and alphabets','reading':r'S(\partial C), A(\partial C), S\prime(\Gamma),\mathbb R^2,\operatorname{card},\Rightarrow,\ge2,\operatorname{int}\Gamma','verification':'Open S/A parentheses, clear S-prime tick, doubled R upright, separate exponent 2, rightward double arrow and cardinal abbreviation all checked. No ext occurs.'},
 {'sign':'Roman numerals','reading':'X, IV, V, VIII','verification':'X, IV, VIII have upper/lower rules; plain V in lemma mentions has no such surrounding pair. VIII settled on half b.'},
 {'sign':'Quotation form','reading':'paired opening backticks and paired closing apostrophes','verification':'Top pencil note has paired upright strokes, not guillemets.'},
 {'sign':'Entries in supplied table absent here','reading':'Disk D_s; alpha_1, alpha_2, alpha_2 prime; pi; IX; OPS; def.; underlined dém','verification':'No occurrences on this page; no imported normalization.'}
]
views=[]
def view(path,time,role,detail=''):
 views.append({'path':path,'time_utc':time,'role':role,'detail':detail})
view(src+'J71-05_71_scan037.jpg','2026-11-19 22:19:46 UTC','whole','Displayed once for layout; clock immediately before tool display.')
view(a,'2026-11-19 22:19:54 UTC','half_a','Displayed once at supplied full resolution.')
view(b,'2026-11-19 22:20:28 UTC','half_b','Displayed once at supplied full resolution; original y offset 1102.')
for name in ['01_top_note','02_deleted_set_sign','03_deleted_word','04_le_lemme']:
 view(cp(name+'.png'),'2026-11-19 22:21:29 UTC','crop','Clock before sequential four-image display batch; displayed once.')
for name in ['05_z_deleted_prime','06_z_prime','07_interval_s','08_deleted_ca']:
 view(cp(name+'.png'),'2026-11-19 22:21:59 UTC','crop','Clock before sequential four-image display batch; displayed once.')
for name in ['09_S_prime','10_deleted_number','11_side_note','12_distincts']:
 view(cp(name+'.png'),'2026-11-19 22:22:32 UTC','crop','Clock before sequential four-image display batch; side_note initial +90 orientation was upside down, all other crops displayed once.')
view(cp('11_side_note.png'),'2026-11-19 22:23:02 UTC','orientation_correction','Same crop raster turned 180 degrees in place; final original-image rotation -90 degrees. This is one extra display caused by correcting an orientation error, not a new crop.')
view(cp('13_first_visible_join.png'),'2026-11-19 22:25:36 UTC','crop','Single crop of a remaining small punctuation question: the short hyphen connects closing parenthesis to visible; C is confirmed.')
notes={
 'page_content':'Continuation of a proof in the case ringed T cap Gamma is nonempty. It constructs a convex hull, invokes IV for a visible y and V for an edge, argues with an auxiliary triangle, concludes a visible vertex, then states a corollary asserting a pair of distinct polygon vertices with exterior visibility and connecting open interval on the hull boundary.',
 'manuscript_checks_and_doubts_verbatim':[
  "ce n'est \\unsure{pas une|pas un} ``\\unsure{env. conv.|ens. conv.}''!",
  r'(Noter aussi que $\mathring C\ne\phi$ puisque $\Gamma\cap\mathring T\ne\phi\Rightarrow\operatorname{card}(\Gamma\cap]s\',s\'\'[)\ge2$)',
  r'compliqué, prendre un sommet de $\Gamma$ $\in$ \deleted{\unsure{$\mathring T$|$\alpha$}} et qui est à dist. max. de la droite \deleted{\unsure{$\Delta$}} $(s\'s\'\')$',
  '!! beside the opening; !! beside the corollary heading'
 ],
 'mathematical_triggers':[
  {'place':'Empty-set-role glyph throughout','reading_decision':'Role could encourage varnothing, but the near-vertical pierced oval makes phi the first graphic candidate. No set-theoretic argument is used to eliminate the alternative.'},
  {'place':'P3 y notin S(partial C)','reading_decision':'Choice of a point on an edge could suggest nonmembership in the vertex set, but the crossing stroke independently settles notin on half a.'},
  {'place':'P5 endpoint alternatives and later hypothesis','reading_decision':r'The preceding edge is [z,z\prime], while the later ink says z\prime,z\prime\prime in [s\prime,s\prime\prime]. Potential mathematical tension is retained. Neither the overworked prime nor the later hypothesis is repaired.'},
  {'place':'P5 S prime of Gamma','reading_decision':'S prime could be unexpected compared with S(partial C), but its separate raised tick is clear and retained.'},
  {'place':'Side note','reading_decision':'A maximum-distance vertex suggestion makes grammatical and mathematical sense, but does not settle the crossed ringed-T/alpha or triangular symbol.'}
 ],
 'verification_scope':'Visual collation only. No theorem was independently proved, no computation/formal certificate was attempted, and no proof-check event is claimed.',
 'C_guide_verification':'All explicit unsure/illegible places in C have an issue row. The remaining C guide entries were also checked: hollow circles; reinforced/plain C; bracket direction and added pair; Gamma/S/A/partial shapes; double R/exponent/card/double arrow; z-primes and T-prime; quote pairs; absent accents in Considerons, interieur, considerons, demonstration; visible z-prime,z-double-prime hypothesis; S-prime; c.q-f.d. dash. Entries that are mere notation observations are not mislabeled C doubts.',
 'additional_small_sign_check':{'image':cp('13_first_visible_join.png'),'bbox':[1170,335,1580,425],'outcome':'The short horizontal immediately after the closing parenthesis and before visible is present. Retain C hyphen; no witness difference.'},
 'pagination_and_heading':{'manuscript':'X with upper/lower rules','archive_pencil':'36, transcribed only as comment','heading':'Corollaire à la demonstration du lemme VIII.','date_on_page':'none','page_count_on_page':'none'},
 'hands':'Fair-copy main ink and later pencil annotations are distinguished without naming an author; similar ink is not by itself an identity claim.',
 'H_status':'hua_has=text. H note is editorial summary, not a diplomatic transcript. Its literal anchor words and marginal readings have been compared; six coherent absent main-text blocks are reported without treating paraphrases as asserted literal ink.',
 'protocol_exception':'The side-note crop was first rotated +90 degrees, which proved upside down. The existing crop was rotated 180 degrees in place to final -90 degrees and shown once upright. Thus there are 13 distinct crops and 14 crop displays. Whole and halves were each displayed exactly once, in required order. No other pages/readers, OCR, web, or PDF text were consulted.',
 'crop_script':'Used supplied work/SP37_CW_71/scripts/crop.py; root scripts/crop.py did not exist. All crop outputs are in assigned R3 directory; 3000px width, LANCZOS, autocontrast, UnsharpMask radius 1.0 percent 120 threshold 3.'
}
report=dict(scan=37,reader='R3 — GPT-6 Astra Pro; inherited effort (not exposed); run scan037-R3',views=views,crop_count=13,issues=issues,inventory=inventory,doubts=doubts,notation=notation,abbreviations=[{'form':'env. / ens. conv.','place':'top pencil objection','expanded':False,'doubt':'first abbreviation uncertain'}, {'form':'card','place':'parenthetical line','expanded':False}, {'form':'dist. max.','place':'side note','expanded':False}, {'form':'c.q-f.d.','place':'proof ending','expanded':False,'note':'dash between q and f retained'}, {'form':'vis','place':'cancelled fragment in last line','expanded':False}],notes=notes,check_events=[],summary={'complete_page_transcribed':True,'issues_total':len(issues),'against_C_total':sum(x['against_C'] for x in issues),'against_H_total':sum(x['against_H'] for x in issues),'main_changes':'Phi-first recurring glyph; clear y-notin, S-prime, VIII and deleted vis; visible apostrophe in il\'y; un/membership/et in side note; three graphic leaders/rules added. H abbreviations and full side note recovered with retained local doubts; six main-text omission blocks routed by bbox.','unresolved':'Compressed top pencil article/abbreviation, reinforced-C alphabet, several heavy obliterations, overworked endpoint prime and interval s/S, crossed marginal symbols and compressed distincts.','views':'Whole once, halves once each in order; 13 crops with one additional display to correct side-note orientation.'})
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Keep the open-place index consistent with the final single-crop orientation and late punctuation check.
op=json.loads((base/'open_places.json').read_text())
for x in op:
 if x['crop']=='11_side_note': x['rotation']=-90; x['orientation_correction']='One failed +90 display then existing raster turned upright; no recrop.'
op.append({'crop':'13_first_visible_join','bbox':[1170,335,1580,425],'rotation':0,'open_after_halves':'Small joining stroke after closing parenthesis before visible: suspected missing hyphen, resolved by crop as a visible hyphen.'})
(base/'open_places.json').write_text(json.dumps(op,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reading':str(base/'reading.tex'),'report':str(base/'report.json'),'issues':len(issues),'inventory':len(inventory),'doubts':len(doubts),'crops':13},ensure_ascii=False))
