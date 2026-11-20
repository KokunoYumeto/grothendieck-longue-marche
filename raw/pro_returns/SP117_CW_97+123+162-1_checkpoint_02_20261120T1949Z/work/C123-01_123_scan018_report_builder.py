from pathlib import Path
import json
P='C123-01_123_scan018'
base=Path('/workspace/scratch/d27bd2a88bca')
manifest=json.loads((base/'out/work'/f'{P}_crop_manifest.json').read_text())
M={x['id']:x for x in manifest}
R={'page':P,'line_count':28,'changes':[],'doubts':[],'inventory':[],'notes':[],'check_events':[],'visual_audit_events':[],'notation':[],'hand_log':[],'boxes':[]}
def change(id,line,c,h,final,shows,crop,conf,kind,C,H,marked=False,cons=False,certainty=False):
    m=M[crop]
    R['changes'].append(dict(id=id,line=line,c=c,h=h,final=final,scan_shows=shows,crop=m['crop'],box=m['box'],confidence=conf,kind=kind,changed_C=C,changed_H=H,marked_in_H=marked,consequential=cons,certainty_only=certainty))
change('r01','L01',r'\deleted{sur la catégorie}','sur la catégorie',r'\deleted{sur la catégorie}','All three words are visibly canceled with mechanical x overstrikes; the heading underline remains.','b01','high','deletion state (struck given live or live given struck)',False,True)
change('r02','L03 insertion',r"``exactes'",'« exactes »',r"``exactes'",'Two opening strokes and only one clear closing apostrophe; the asymmetric quotation is retained.','b02','high','other',False,True)
change('r03','L05',r'\unsure{il}','il',r'i\deleted{\unsure{o}}l\deleted{\illegible{1}}','A tall l is superposed on a rounded o-like body. A further glyph immediately to its right is heavily canceled; its identity is not recovered. Final il is plausible, but underletter and canceled glyph remain uncertain.','b05','low','deletion state (struck given live or live given struck)',True,True)
change('r04','L05',r'\deleted{un}','[omitted]',r'\deleted{un}','The letters u and n remain under x overstrikes between donner, and pour.','b06','high','omission',False,True)
change('r05','L05',r'G_{\unsure{o|0}}',r'G_0',r'G_o','Small rounded subscript has the lowercase-o size and contour, unlike the larger baseline numeral zero visible in the exactes insertion.','b07','high','misread symbol or index',True,True,False,True)
change('r06','L06',r'\deleted{homomorphisme}','[omitted]',r'\deleted{homomorphisme}','Every letter of homomorphisme is visible beneath mechanical x cancellation.','b08','high','omission',False,True)
change('r07','L06',r'\operatorname{Hom}(\underline G_m,T_o)/W=M/W; T_o=M\unsure{\otimes|\mathbin{\text{\textcircled{x}}}}\underline G_m',r'\operatorname{Hom}(\underline G_m,T_0)/W=M/W; T_0=M\otimes\underline G_m',r'\operatorname{Hom}(\underline G_m,T_o)/W=M/W; T_o=M\otimes\underline G_m','Both subscripts are small o. Tensor sign is mechanically composed from an O and x, the same visible construction as the later tensor sign; it is rendered otimes.','b09','high','misread symbol or index',True,True,False,True)
change('r08','L07',r'\operatorname{Auext}G_o=E_o',r'\operatorname{Autext}G_0=E_0',r'\operatorname{Auext}G_o=E_o','Typed Auext has no t between u and e; the G and E subscripts, and earlier G in this same crop, are lowercase-sized o.','b10','high','misread word',False,True,False,True)
change('r09','L08',r'\deleted{homomorphisme $\underline G_m\unsure{\to}T$}','[omitted]',r'\deleted{homomorphisme $\underline G_m\unsure{\to}T$}','The full canceled phrase remains on the page. X overstrikes obscure the arrow, whose uncertainty is retained.','b12','high','omission',False,True)
change('r10','L09',r'M\otimes_{\underline Z}\underline R',r'M\otimes_{\mathbf Z}\mathbf R',r'M\otimes_{\underline Z}\underline R','Z and R are single typewritten capitals with separate short underline strokes; not bold or doubled capitals.','b13','high','misread symbol or index',False,True,False,True)
change('r11','L09',r'\handwritten{\unsure{\Gamma\prime|\Gamma}}',r'\Gamma',r'\handwritten{\Gamma}','The upper-right descending stroke is joined to the extended top bar. It is the terminal of Gamma, not a separate prime. A typed I-like body is completed by pen.','b14','high','misread symbol or index',True,False,False,True)
change('r12','L10',r'\handwritten{\unsure{\underline\phi|\underline\varnothing}_c}',r'\underline\varnothing_c',r'\handwritten{\underline\varnothing}_c','Oval ring with a pronounced lower-left to upper-right slash and underline; same slashed-ring construction in the insertion and display. Literal varnothing-shaped glyph chosen, without interpreting it as the empty set.','b16','high','misread symbol or index',True,False,False,True)
change('r13','L11 insertion',r'\handwritten{il} est',"c'est",r'\deleted{\unsure{c\prime}}\handwritten{il} est','A machine c-like shape is under the pen correction reading il. A possible old apostrophe is obscured by the pen l and cannot be separated securely. H takes the undertext as live; proposed old c-apostrophe remains doubtful.','b18','low','deletion state (struck given live or live given struck)',True,True,True)
change('r14','L11 insertion',r'est\inserted{\handwritten{$\sim$}} un','est un',r'est\inserted{\handwritten{$\sim$}} un','A separate handwritten tilde lies above the gap between est and un.','b18','high','omission',False,True,True,True)
change('r15','L11 insertion','orbite rationelle sous G','orbite rationnelle sous G','orbite rationelle sous G','The typed spelling has one n between o and e.','b18','high','misread word',False,True,True)
change('r16','L11 insertion',r"soit $c'$,",r"soit $c'$.",r"soit $c'$,",'The handwritten tail after c-prime is a comma, not a full stop.','b18','high','other',False,True,True)
change('r17','L13','Il','Il',r'I\deleted{\unsure{l|t}}l','The second letter contains two vertically displaced stem-and-foot impressions. An l-like lower impression is visible; t remains an alternative. Overprint order/underletter are uncertain, so the proposed deletion is explicitly doubtful.','b20','low','deletion state (struck given live or live given struck)',True,True)
change('r18','L15 insertion',r"pour $P$\inserted{ou encore $\handwritten{\underline\phi}$} de classe $c'$",r"$P$ soit de classe $c'$\add{ou encore $\underline\varnothing$}",r"pour $P$\inserted{ou encore $\handwritten{\underline\varnothing}$} de classe $c'$",'The pen connector descends to the gap immediately after P in pour P on the following baseline. The glyph is again an underlined ring with oblique slash.','b21','high','insertion or placement',True,True,True,True)
change('r19','L16','où un sous-groupe','ou un sous-groupe','où un sous-groupe','A clear grave accent is present over u. Source où is retained.','b22','high','misread word',False,True)
change('r20','L17',r'\deleted{\unsure{un homo}}\inserted{deux}',r'deux',r'\deleted{un homo}\inserted{deux}','The crossed sequence un homo can be followed letter by letter; deux is typed immediately above.','b24','medium','omission',True,True)
change('r21','L17','morphismesde','morphismes de','morphismesde','No space is typed between final s and d.','b24','high','other',False,True)
change('r22','L19 display',r'\operatorname{ST}_c\to\underline\phi_c',r'\mathrm{ST}_c\to\underline\varnothing_c',r'\operatorname{ST}_c\handwritten{\longrightarrow\underline\varnothing}_c','The display repeats the obliquely slashed ring, with underline and typed subscript c. Both right-pointing arrows are handwritten.','b26','high','misread symbol or index',True,False,False,True)
change('r23','L20',r'\unsure{da|du} foncteurs fibres','du foncteur fibres',r'd\unsure{\deleted{u}a|\deleted{a}u} foncteurs fibres','The second letter has a closed a-like contour and additional u-like strokes. Overtyping is visible, but order is not secure; both orders are retained. The final s of foncteurs is clear. No grammatical repair is made.','b27','medium','other',True,True)
change('r24','L21',r'\deleted{\unsure{d}}en','en',r'\deleted{d}en','The ascender, leftward top serif, and lower bowl identify the crossed letter d before en.','b28','high','omission',True,True)
change('r25','L24',r'fi_o',r'fi_0',r'fi_o','The subscript has the same lowercase-o size and contour as G_o, T_o and E_o on this sheet.','b29','high','misread symbol or index',False,True,False,True)
change('r26','L26 insertion',r'de stabilisateur $Z_o$ ... ces $Z_o$',r'de stabilisateurs $Z_0$ ... ces $Z_0$',r'de stabilisateur $Z_o$ (il faudrait regarder la structure de ces $Z_o$;','There is no s after stabilisateur. Both handwritten indices are small round o forms, read consistently with the sheet’s typed subscript o. The parenthetical question is live.','b34','high','misread word',False,True,True,True)
change('r27','L28',r'\deleted{celle de}','[omitted]',r'\deleted{celle de}','The two words are still readable under mechanical x overstrikes and a pen line.','b39','high','omission',False,True)
R['doubts']=[
 {'line':'L03 insertion','reading':r'\unsure{dernière}','alternatives':[],'confidence':'medium','reason':'Final letters are overtyped. The candidate word is plausible, but a clean sequence cannot be recovered from b02.'},
 {'line':'L05','reading':r'i\deleted{\unsure{o}}l\deleted{\illegible{1}}','alternatives':['underletter other than o','terminal canceled k-like character'],'confidence':'low','reason':'Rounded underletter and heavily canceled following glyph at b05; underlying text not confidently recovered.'},
 {'line':'L08 deletion','reading':r'\underline G_m\unsure{\to}T','alternatives':['arrow head/shaft not recoverable'],'confidence':'low','reason':'Mechanical x overstrikes cross the arrow in b12.'},
 {'line':'L09 right edge','reading':r'\unsure{schéma}','alternatives':[],'confidence':'medium','reason':'The word reaches the black scan edge; terminal letter is partly clipped in b15.'},
 {'line':'L11 insertion','reading':r'\deleted{\unsure{c\prime}}\handwritten{il}','alternatives':['undertext c without a recoverable apostrophe'],'confidence':'low','reason':'Pen il obscures the machine c-like initial and the position of a possible old apostrophe in b16/b18.'},
 {'line':'L13','reading':r'I\deleted{\unsure{l|t}}l','alternatives':['t under l','repeated l impression, with no distinct letter correction'],'confidence':'low','reason':'Two vertically displaced impressions; chronological interpretation cannot be proved from ink in b20.'},
 {'line':'L20','reading':r'd\unsure{\deleted{u}a|\deleted{a}u}','alternatives':['u overwritten by a','a overwritten by u'],'confidence':'medium','reason':'Both closed a-like and u-like strokes visible in b27; order remains uncertain. The semantic expectation du is not used to settle it.'}
]
# Top-down inventory, one entry per principal baseline and each distinct added/deleted element.
def inv(y,element,kind,words,hand='typewriter',pos=None):
    R['inventory'].append({'scan':18,'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':pos or f'y≈{y}','first_words_or_objects':words,'transcribed':'yes','_y':y})
lines=[
(142,'L01','Interprétations en termes de filtrations du foncteur oubli'),
(209,'L02',"des représentations linéaires de dimension finie de G. (Il s'agit de fil-"),
(274,'L03','trations compatibles au produit tensoriel ... Supposons fixé une classe de'),
(341,'L04',"telles filtrations (NB elle n'admet pas nécessairement un représentant"),
(405,'L05','rat/k); il revient au même de se donner, ... pour le Chevalley G_o associé'),
(471,'L06','à G, un ... élément de Hom(G_m,T_o)/W=M/W (T_o=M⊗G_m est le to-'),
(537,'L07','re maximal type de G_o) invariant par le sous-groupe ... de Auext G_o=E_o image'),
(600,'L08','de Gal(bar k/k), ou encore un ... élément de M qui soit dans'),
(666,'L09','la chambre de Weyl de M⊗_Z R et qui soit stable par Γ. On a alors le schéma'),
(732,'L10','underlined varnothing_c des filtrations de classe c, qui est un espace homogène sous G, de'),
(799,'L11','stabilisateur des points des paraboliques; ... On peut regarder aussi le schéma'),
(865,'L12','ST_c des homomorphismes i:G_m→G de classe c, qui est donc une orbite'),
(931,'L13','rationelle de G opérant sur Homgr(G_m,G). Il est canoniquement isomorphe au'),
(998,'L14',"schéma des couples de Lévi (P,L) tels que P soit de classe c'. (En d'autres"),
(1064,'L15',"termes, grâce au choix d'un c, pour P ... de classe c' donné, il revient au"),
(1130,'L16','même de se donner un i:G_m→P de la classe définie par c, où un sous-grou-'),
(1194,'L17','pe de Lévi de P, à i étant associé Cent(i).) On a ... morphismesde'),
(1263,'L18','schémas canoniquement isomorphes'),
(1396,'L20','le premier en termes de théorie des filtrations da/du foncteurs fibres, le'),
(1462,'L21','deuxième ... en termes de groupes paraboliques.'),
(1527,'L22',"Supposons maintenant que k soit de car. nulle (j'ignore dans quelle"),
(1594,'L23',"mesure c'est vraiment nécessaire). On peut alors considérer le Schéma"),
(1660,'L24','Dyn_c des homomorphismes f:Sl(2,k)→G tels que fi_o soit de classe c. Sup-'),
(1727,'L25','posons-le non vide ... i.e. c une classe de Dynkin ... Alors Dyn_c est un tor-'),
(1793,'L26','seur sous G ... (en fait, il est can. is. au torseur Isom(G_1,G), où G_1 est le'),
(1859,'L27','groupe quasi-déployé correspondant à G). Soit Un_c le schéma des éléments'),
(1925,'L28','unipotents ... dont la classe corresponde à ... c par la correspondance')]
for y,l,w in lines: inv(y,l,'text',w,'typewriter with pen additions where separately inventoried',f'{l}; main baseline y≈{y}')
inv(142,'I01','deletion','sur la catégorie','typewriter x cancellation','L01 right end')
inv(234,'I02','insertion',r'et ``exactes\prime,cette dernière cond. aut. si car.k=0','typewriter; pen callout','between L02 and L03, attached after tensoriel')
inv(245,'I03','insertion','c','typewriter; pen callout','above classe de on L03')
inv(309,'I04','insertion','conjugaison, rationelle sur k, de','typewriter; pen connector','between L03/L04, after de before telles')
inv(405,'I05','deletion','rounded underletter beneath l; canceled terminal glyph','typewriter overprint and cancellation','L05 after rat/k);')
inv(405,'I06','deletion','un','typewriter x cancellation','L05 between donner, and pour')
inv(471,'I07','deletion','homomorphisme','typewriter x cancellation','L06 after à G, un')
inv(502,'I08','insertion','Γ','mixed typed I-like stem and pen top bar; pen callout','above sous-groupe de on L07')
inv(600,'I09','deletion','homomorphisme G_m→T','typewriter x cancellation, arrow partly obscured','L08 after ou encore un')
inv(666,'I10','text','Γ','mixed typewriter and pen','L09 after stable par')
inv(732,'I11','text','underlined varnothing_c','mixed typed ring/underline/subscript and pen slash','L10 initial symbol')
inv(732,'I12','text','c','pen hand 1','L10 after classe')
inv(766,'I13','insertion',"il est ~ un sous-schéma ouvert de Par(G), orbite rationelle sous G, soit c',",'typewriter with pen correction il, pen tilde and ending soit c-prime','between L10 and L11; connector after paraboliques')
inv(766,'I14','deletion',"uncertain c' beneath il",'typed undertext corrected by pen','initial word of I13')
inv(752,'I15','insertion','~','pen hand 1','above est un in I13')
inv(865,'I16','text','i:G_m→G','typewriter; pen arrow','L12 central formula')
inv(931,'I17','deletion','uncertain l/t beneath l in Il','typewriter doubled impression','L13 after Homgr(G_m,G).')
inv(1028,'I18','insertion','ou encore underlined varnothing','typed words/ring/underline, pen slash and connector','between L14/L15; connector after P in pour P')
inv(1130,'I19','text','i:G_m→P','typewriter; pen arrow','L16')
inv(1111,'I20','text','grave accent on où','pen-like accent above typewritten u','L16 after classe définie par c,')
inv(1194,'I21','insertion',')','pen hand 1','L17 after Cent(i).')
inv(1180,'I22','insertion','deux','typewriter','above un homo in L17')
inv(1194,'I23','deletion','un homo','typewriter x cancellation','L17 after On a')
inv(1331,'L19','display',"ST_c→underlined varnothing_c, (CL)_{c'}→Par_{c'},",'typewriter with pen arrows and slash','centered two-arrow display')
inv(1396,'I24','deletion','uncertain a/u overtype in da/du','typewriter overprint','L20 before foncteurs fibres')
inv(1462,'I25','deletion','d','typewriter x cancellation','L21 immediately before en')
inv(1660,'I26','text','f:Sl(2,k)→G; fi_o','typewriter; pen arrow','L24')
inv(1698,'I27','insertion','et non réduit à un point,','pen hand 1','between L24/L25, callout after non vide')
inv(1690,'I28','insertion','≠1','pen hand 1','above L25, callout after Dynkin')
inv(1695,'I29','insertion','espace','pen hand 1','above canceled tor- at right end of L25')
inv(1727,'I30','deletion','tor-','typewriter word with pen cancellation; underline','right end of L25, continuing seur next line')
inv(1764,'I31','insertion','homogène','pen hand 1','above canceled seur at left of L26')
inv(1793,'I32','deletion','seur','typewriter word with pen cancellation; underline','left of L26, continuation of tor-')
inv(1764,'I33','insertion','de stabilisateur Z_o (il faudrait regarder la structure de ces Z_o;','pen hand 1','between L25/L26, attached after sous G')
inv(1793,'I34','deletion','(en fait, il est can. is. au torseur Isom(G_1,G), où G_1 est le','typewriter with continuous pen cancellation','L26 after sous G, first canceled parenthesis line')
inv(1830,'I35','insertion','dimension, semi-simplicité).','pen hand 1','between L26/L27; continuation of I33')
inv(1859,'I36','deletion','groupe quasi-déployé correspondant à G).','typewriter with continuous pen cancellation','L27, end of canceled parenthesis')
inv(1895,'I37','insertion','de G','pen hand 1','between L27/L28; connector before dont')
inv(1925,'I38','deletion','celle de','typewriter x cancellation and pen line','L28 between corresponde à and c')
inv(2080,'I39','margin note','17','separate archive hand, attribution unestablished','bottom-left archive foliation; TeX comment only')
R['inventory'].sort(key=lambda x:x['_y'])
for x in R['inventory']: x.pop('_y')
readings={
'b01':r'\deleted{sur la catégorie}',
'b02':r'\inserted{et ``exactes\prime,cette \unsure{dernière} cond. aut. si $\operatorname{car}.k=0$}',
'b03':r'\inserted{$c$}',
'b04':r'\inserted{conjugaison, rationelle sur $k$, de}',
'b05':r'i\deleted{\unsure{o}}l\deleted{\illegible{1}}',
'b06':r'donner,\deleted{un} pour',
'b07':r'Chevalley $G_o$ associé',
'b08':r'un \deleted{homomorphisme} élément de',
'b09':r'$\operatorname{Hom}(\underline{G}_m,T_o)/W=M/W$ ($T_o=M\otimes\underline{G}_m$',
'b10':r'$G_o$) invariant par le sous-groupe\inserted{\handwritten{$\Gamma$}} de $\operatorname{Auext}G_o=E_o$ image',
'b11':r'$\operatorname{Gal}(\bar{k}/k)$,',
'b12':r'\deleted{homomorphisme $\underline{G}_m\unsure{\to}T$}',
'b13':r'$M\otimes_{\underline{Z}}\underline{R}$',
'b14':r'par $\handwritten{\Gamma}$.',
'b15':r'le \unsure{schéma}',
'b16':r'$\handwritten{\underline{\varnothing}}_c$ des filtrations',
'b17':r'classe $\handwritten{c}$,',
'b18':r'\inserted{\deleted{\unsure{c\prime}}\handwritten{il} est\inserted{\handwritten{$\sim$}} un sous-schéma ouvert de $\uline{Par}(G)$, orbite rationelle sous $G$,\handwritten{soit $c\prime$,}}',
'b19':r'$i:\underline{G}_m\handwritten{\to}G$',
'b20':r'$\uline{Homgr}(\underline{G}_m,G)$. I\deleted{\unsure{l|t}}l est',
'b21':r'$P$\inserted{ou encore $\handwritten{\underline{\varnothing}}$} de classe $c\prime$',
'b22':r'par $c$, où un sous-groupe',
'b23':r'$i:\underline{G}_m\handwritten{\to}P$',
'b24':r'On a \deleted{un homo}\inserted{deux}morphismesde',
'b25':r'$\operatorname{Cent}(i)$.\handwritten{)}',
'b26':r'$\operatorname{ST}_c\handwritten{\longrightarrow\underline{\varnothing}}_c\quad,\quad(\operatorname{CL})_{c\prime}\handwritten{\longrightarrow}\operatorname{Par}_{c\prime}\quad,$',
'b27':r'd\unsure{\deleted{u}a|\deleted{a}u} foncteurs fibres,',
'b28':r'\deleted{d}en termes',
'b29':r'$f:\operatorname{Sl}(2,k)\handwritten{\longrightarrow}G$ tels que $fi_o$',
'b30':r'\inserted{\handwritten{et non réduit à un point,}}',
'b31':r'\inserted{\handwritten{$\ne1$}}',
'b32':r'\deleted{\uline{tor-}}\inserted{\handwritten{espace}}',
'b33':r'\deleted{\uline{seur}}\inserted{\handwritten{homogène}}',
'b34':r'\inserted{\handwritten{de stabilisateur $Z_o$ (il faudrait regarder la structure de ces $Z_o$;}}',
'b35':r'\inserted{\handwritten{dimension, semi-simplicité).}}',
'b36':r'\deleted{(en fait, il est can. is. au torseur $\uline{Isom}(G_1,G)$, où $G_1$ est le}',
'b37':r'\deleted{groupe quasi-déployé correspondant à $G$).}',
'b38':r'\inserted{\handwritten{de $G$}}',
'b39':r'\deleted{celle de}',
'b40':r'% archive sheet number: 17'
}
kind={k:'text' for k in readings}
for k in ['b01','b05','b06','b08','b12','b20','b24','b27','b28','b32','b33','b36','b37','b39']:kind[k]='deletion'
for k in ['b02','b03','b04','b10','b18','b21','b25','b30','b31','b34','b35','b38']:kind[k]='insertion'
kind['b26']='display';kind['b40']='margin note'
for m in manifest:
    x0,y0,x1,y1=m['box']; k=m['id']
    R['boxes'].append(dict(box=k,kind=kind[k],x0=x0,y0=y0,x1=x1,y1=y1,reading=readings[k]))
R['notes']=[
'Whole sheet viewed once for layout, followed by each half once against both C and H. All 40 saved crops were displayed and read; no OCR, recognition library, web lookup or TeX compilation was used.',
'Line count is 28 principal typewriter baselines, including the single display line. Interlinear material and the archive foliation are separately inventoried. No drawing or mathematical diagram occurs.',
'All changes are based on visible ink; no theorem was checked or repaired. The source parenthesis “j\'ignore dans quelle mesure c\'est vraiment nécessaire” records uncertainty about the characteristic-zero assumption and remains in the candidate.',
'The live inserted parenthesis “il faudrait regarder la structure de ces Z_o; dimension, semi-simplicité” is a source research question, not an established stabilizer-structure claim. Its wording remains in the candidate, and no proof/check is claimed.',
'The deleted claim identifying the former torseur with Isom(G_1,G) is wholly retained as deleted. It is not treated as an assertion endorsed or verified in this reading.',
'Slips retained: fixé une classe; rationelle at all three occurrences; asymmetric exactes quotation; Auext; morphismesde; accented où in the alternative; plural foncteurs fibres; uncorrected da/du overprint ambiguity.',
'H’s note saying that all additions are handwritten is editorial, not page text. Several additions are mechanical typewriter insertions with pen callouts; hand attribution changes alone were not counted as substantive text changes.',
'B05, b18 and b20 proposed underlying characters remain explicitly uncertain. The order of a/u impressions in b27 remains uncertain; grammatical du or des cannot settle the ink.',
'B16/B21/B26 show an underlined ring with a markedly oblique slash; consistent literal varnothing encoding is used. This is a transcription of shape, without a mathematical interpretation as the empty set.',
'All deletion spans were audited, including title cancellation; un; both homomorphisme passages; small overprints; un homo; d; split torseur; the two-line parenthesis; and celle de. Heavy cancellation flourishes over tor/seur are cancellation strokes, not additional recovered words.',
'The archive 17 is not an author page label and is preserved only as a TeX comment. It is inventoried and boxed.',
'Original pixel coordinates are retained in all report boxes. Crops include adjacent context for location; box readings specify the complete target text rather than incidental clipped neighboring fragments.',
'No mathematical consistency inference was needed to change a word. The possible grammatical expectation after filtrations was explicitly excluded when assessing da/du.'
]
R['visual_audit_events']=[
 {'statement_id':'018-layout','type':'used and rechecked in this run','outcome':'visual transcription check only: whole page and both halves read against both witnesses; no proof attempted.'},
 {'statement_id':'018-deletions-insertions','type':'used and rechecked in this run','outcome':'visual transcription check only: every visible addition/deletion and each witness-different word audited on saved crops.'},
 {'statement_id':'018-symbols','type':'used and rechecked in this run','outcome':'visual transcription check only: lowercase o, unprimed Gamma, tensor construction, underlined Z/R, and three slashed-ring glyphs compared within this sheet.'}
]
R['notation']=[
'First G subscript and repeated T,G,E,i subscripts are lowercase-sized typewritten o, not the baseline numeral zero. Handwritten Z indices are also read o, without importing a mathematical normalization.',
'The two Gamma signs have a typewriter I-like stem completed with a pen top-right bar/terminal; the terminal at stable par is joined, not a prime.',
'Three filtration signs are single rings with an oblique slash and short underline; render underline{varnothing} consistently. The slash is handwritten; parts of the ring/underline/subscript are mechanical.',
'Tensor signs are mechanical O+x constructions rendered otimes. Z and R are underlined single capitals, not bold or double struck.',
'All source abbreviations remain: NB, rat/k, cond., aut., car., i.e., can., is., and Sl. No expansions supplied.',
'Typed quotation is asymmetric: two opening strokes and one closing apostrophe after exactes. Preserve the source slip.'
]
R['hand_log']=[
'Principal text is typewritten. One consistent dark pen hand supplies arrows, callout leaders, slashes, corrected il, tilde, c, soit c-prime, the closing parenthesis, and lower interlinear notes; identity is not inferred.',
'Exactes clause, inserted c above classe, conjugaison phrase, main long subschéma insertion, ou encore and deux are typewritten; their leaders are pen. First c insertion is mechanical, whereas c after classe on L10 is pen.',
'Gal(bar k/k) has a mechanical k; its bar has a straight keyed-looking shape. Candidate removes C’s whole-bark handwriting wrapper without counting a substantive text difference.',
'At où the visible grave is pen-like above a typed u; lexical accent retained without trying to assign a separate TeX hand wrapper to the accent.',
'Bottom archive 17 is a separate numeral annotation; hand identity and date unestablished.'
]
R['crop_transforms']=[{'crop':M['b38']['crop'],'box_id':'b38','original_box':M['b38']['box'],'rotation_clockwise_degrees':12,'source':'existing saved crop, no recrop','resampling':'BICUBIC','expanded_canvas':True,'fill':'white','purpose':'upright de G handwriting'}]
R['crop_processing']={'source_size':[1670,2143],'width_pixels':2500,'resize':'LANCZOS','autocontrast_cutoff':0.2,'sharpen':'UnsharpMask radius 1.2 percent 110 threshold 3','displayed_crop_ids':[m['id'] for m in manifest]}
(base/'out/work'/f'{P}_report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(f"Saved report: {len(R['changes'])} changes, {len(R['inventory'])} inventory elements, {len(R['boxes'])} boxes, {len(R['doubts'])} open readings.")
