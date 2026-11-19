from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
d={'cote':53,'scan':4,'sheet_kind':'text','hand':'his hand','replace':[
 (r'\unsure{\mu_p|\mathbb{H}_p}',r'\unsure{\mu_r|\mathbb{H}_r}'),
 (r'\unsure{k[[t|k[[+}',r'k[[t'),
 (r'\unsure{\mathbb A b|\mathrm{Ab}}',r'\mathbb A b'),
 (r'G^{\unsure{n|h}}',r'G^{h}'),
 (r'\unsure{\prime\prime|\prime}',r'\prime\prime'),
 (r'G^n\unsure{-|\longrightarrow}G^m',r'G^n-G^m'),
 (r'(\mathrm{ENS})\unsure{)|{}}',r'(\mathrm{ENS})'),
 (r'\unsure{FN|EN}',r'FN'),
 (r'\unsure{topos|transp.}',r'\unsure{transp.|topos}'),
 (r'\unsure{\mathrm{sp}|\mathrm{sr}}',r'\mathrm{sp}'),
 (r'\unsure{cardinalité|cofinalité}','cardinalité'),
 (r'\deleted{\unsure{si}}',r'\deleted{si}'),
 (r'\inserted{\unsure{=}}',r'\inserted{=}'),
 (r'\uuline{\unsure{Lemme}}',r'\uuline{Lemme}'),
 (r'\unsure{UV|U.V}',r'UV'),
 (r'\unsure{int.|inter.}','int.'),
 (r'\unsure{gén.}','gén.'),
 (r'\unsure{a|.}',r'\unsure{.|a}')
], 'review': 'Personally read the whole scan and both supplied halves in order, then all upper cancelled working, both diagrams, the complete live proof, every local deletion and insertion, and the lower cancelled attempts in enlarged crops. The left Lemme was rotated clockwise 20 degrees and enlarged 3×. Broad crops at 2× were followed by 4× details and a 6× inspection of the opaque deleted word. H is textual on this page, so differences in its upper description are collated. The upper drafts remain transcribed, not replaced by descriptions. No mathematical repair has been made.',
'decisions':[], 'inventory':[]}
def add(place,c,h,final,shows,confidence='high',cc=False,hc=False,kind='other',marked='no',conseq=None):
 x=dict(place=place,c=c,h=h,final=final,shows=shows,confidence=confidence,c_changed=cc,h_changed=hc,kind=kind,marked_in_H=marked)
 if conseq:x['consequential']=conseq
 d['decisions'].append(x)
add('upper-left first symbol',r'\unsure{\mu_p|\mathbb H_p}',r'\mu_r',r'\unsure{\mu_r|\mathbb H_r}','The small suffix has a short right shoulder rather than the bowl of p; the doubled long left stroke of the main character remains ambiguous. Whole (100,56,155,131), 4×.','medium',True)
add('upper-left truncated series',r'\unsure{k[[t|k[[+}',r'k[[t]]',r'k[[t','Two opening brackets and a stem with short cross stroke; nothing closing follows. Upper symbols (90,35,1030,226), 2×.','high',True,True,'text not on the page')
add('upper-left second line k','k','K','k','The looped ascender and right branches form the same lowercase k as the preceding series. Upper symbols, 2×.',hc=True,kind='misread symbol or index')
add('upper-left overwritten reduced symbol',r'\deleted{\unsure{\mathcal O|G}}\unsure{k_{\mathrm{red}}|G_{\mathrm{red}}}',r'G_{\mathrm{réd}}',r'\deleted{\unsure{\mathcal O|G}}\unsure{k_{\mathrm{red}}|G_{\mathrm{red}}}','Overlapping loops and rising diagonal do not securely separate the two stages; no distinct acute on red. (289,99,373,161), 4×.','low',hc=True,kind='deletion state (struck given live or live given struck)')
add('upper Delta relation',r'\Delta_0\unsure{\ni|\supset|\Rightarrow}\Delta',r'\Delta_0\supset\Delta',r'\Delta_0\unsure{\ni|\supset|\Rightarrow}\Delta','The center is filled ink; a putative inner bar cannot be separated securely. Upper symbols (90,35,1030,226), 2×.','low')
add('upper category name R',r'\unsure{\mathcal R|R}',r'\mathcal R',r'\unsure{\mathcal R|R}','The heavy R has a loop and diagonal leg, but handwritten alphabet style remains uncertain. Categories (92,268,921,473), 2×.','medium')
add('upper Ab alphabet',r'\unsure{\mathbb A b|\mathrm{Ab}}',r'\mathrm{Ab}',r'\mathbb A b','A has a separate parallel left stroke, also present in the lower repetition. Categories (92,268,921,473), 2×.','high',True,True,'misread symbol or index')
add('upper C alphabet',r'\unsure{\mathcal C|C}',r'\mathcal C',r'\unsure{\mathcal C|C}','An inner curved stroke is visible, but it does not settle ordinary versus calligraphic handwriting. Categories, 2×.','medium')
add('upper barred R',r'\unsure{\overline{\mathcal R}|\overline R}','omitted',r'\unsure{\overline{\mathcal R}|\overline R}','A horizontal bar stands over the separately crossed R. Its alphabet remains uncertain. (435,291,511,350), 4×.','medium',hc=True,kind='omission')
add('upper sigma exponent',r'\sigma=\{G^{\unsure{n|h}}\}',r'\sigma=\{G^n\}',r'\sigma=\{G^h\}','The exponent has a tall left ascender above the rounded shoulder. (743,260,781,295), 4×.','medium',True,True,'misread symbol or index')
add('upper repeated-category marks',r'\unsure{\prime\prime|\prime}','omitted',r'\prime\prime','Two separate short oblique marks sit below the first category equality. Categories, 2×.','high',True,True,'omission')
add('upper map G^n to G^m',r'G^n\unsure{-|\longrightarrow}G^m',r'G^n\to G^m',r'G^n-G^m','The stroke has no arrowhead; the following G^n to G line has a plainly pointed arrowhead. Categories, 2×.','high',True,True,'misread symbol or index','no','The first horizontal sign is retained as a dash, with no added arrowhead.')
add('upper Hom outer parenthesis',r'(\mathrm{ENS})\unsure{)|{}}',r'(\mathrm{ENS}))',r'(\mathrm{ENS})','Only one right parenthesis is present after ENS. (284,541,340,604), 4×.','high',True,True,'text not on the page')
add('upper Hom prime, underline and sigma',r"\uuline{Hom}'(\textcircled{\sigma},(ENS)",r'\underline{Hom}(\sigma,(ENS))',r"\uuline{Hom}'(\textcircled{\sigma},(ENS)",'Separate prime, two short underline strokes, and an oval round sigma are visible. Diagram (42,536,649,805), 2×.',hc=True,kind='drawing or diagram')
add('upper diagram FN',r'\unsure{FN|EN}','omitted','FN','The first letter has top and middle arms without a bottom arm. (572,547,657,595), 4×.','high',True,True,'drawing or diagram')
add('upper diagram left-arrow label',r'\unsure{topos|transp.}','top.',r'\unsure{transp.|topos}','The word has an initial t and closely joined humps followed by a descending p-like stroke; transp. is favored, without resolving the compressed middle. (397,622,486,682), 4×.','low',True,True,'drawing or diagram')
add('upper diagram lower label',r'\unsure{sp|sr}\mathcal R\Rightarrow',r'(ENS)_{/R}',r'sp\;\mathcal R\Rightarrow','The small second letter has a closed upper loop and descender. R and a separate double arrow sit to its right, not beneath ENS. (292,767,340,805), 4×; diagram 2×.','high',True,True,'drawing or diagram')
add('upper diagram structure','two opposed curved vertical arrows and a left arrow','description of connected ENS objects and marked arrows','C diagram retained','Both vertical arrowheads, opposite directions, the left-pointing horizontal arrow and broad cancellation strokes were followed. Diagram, 2×.',hc=True,kind='drawing or diagram')
add('upper-right opening and deleted lead-in',r'\deleted{Soit} Disons posant ... \deleted{C_i prime est tel que}','omitted','C retained','The initial Soit is individually barred; Disons posant and the cancelled phrase after the ordered pairs remain readable under the three oblique cancellation strokes. Ordinal1 (960,191,1648,535), 2×.',hc=True,kind='omission')
add('upper-right indexing map',r'\psi(i)',r'\varphi(i)',r'\psi(i)','The symbol has two upper branches joining a descending central stem, repeated in the diagram. Ordinal1, 2×.',hc=True,kind='misread symbol or index')
add('upper-right diagram deleted index',r'i\deleted{\unsure{+1|+n}}','diagram omitted',r'i\deleted{\unsure{+1|+n}}','A dot and i remain left of a dense crossed horizontal addition; the last character is not securely separated. (1072,430,1144,469), 4×.','low',hc=True,kind='drawing or diagram')
add('upper-right diagram remaining objects and arrows',r"C_i prime to C_{i+1} prime; C_{psi(i)}, C_{psi(i+1)}=g psi(i)",'omitted','C retained','Top rightward arrow and two vertical equal strokes are visible; all four indexed objects and the equality on the lower right were read. Ordinal1, 2×.',hc=True,kind='drawing or diagram')
add('upper-right préexact',r"\lambda_i prime-préexact",r"\lambda_i prime-précisantes",r"\lambda_i prime-préexact",'After pré the strokes form exact, ending in a crossed t. Ordinal2 (705,548,1684,806), 2×.',hc=True,kind='misread word')
add('upper-right cardinal word',r'\unsure{cardinalité|cofinalité}','omitted','cardinalité','The middle has an ascending d and following compressed inal; no f descender is present. (1497,625,1678,663), 4×.','medium',True,True,'omission')
add('upper-right deleted si',r'\deleted{\unsure{si}}','omitted',r'\deleted{si}','The s is crossed and the i retains its separate dot. (1104,688,1171,733), 4×.','high',True,True,'omission')
add('upper-right inserted equals',r'\inserted{\unsure{=}}','omitted',r'\inserted{=}','Two short parallel strokes appear above the line, with insertion guide. (1313,662,1376,695), 4×.','high',True,True,'omission')
add('upper-right lambda exponent',r'\lambda_\omega^{\prime\unsure{\star|{}}}','omitted',r'\lambda_\omega^{\prime\unsure{\star|{}}}','A clear prime is followed by a forked oblique mark; the latter is retained as uncertain. (740,746,839,799), 4×.','low',hc=True,kind='omission')
add('upper-right remainder of ordinal proof','Donc si omega prime ... exact dans C prime omega; deleted donc g(omega)=; cqfd','summary only','C retained with the local decisions above','The ordinal inequality, pi prime, parenthesized lemme du 1°, final category index, and separately barred donc g(omega)= were each read. Ordinal2, 2×.',hc=True,kind='omission')
add('left margin heading',r'\uuline{\unsure{Lemme}}','omitted',r'\uuline{Lemme}','L and joined emme are legible after rotation; two underline strokes remain. (39,815,234,911), clockwise 20°, 3×.','high',True,True,'omission')
add('after a) est trivial',r'\unsure{$\sim$|v}','omitted',r'\unsure{$\sim$|v}','Small curved down-and-up mark cannot be securely named. (992,909,1046,949), 4×.','low',hc=True,kind='omission')
add('b opening deletion',r'\deleted{Soit x\in}',r'\struck{Soit x}',r'\deleted{Soit x\in}','The membership sign follows x under the cancellation. Bfirst (582,956,1700,1365), 2×.',hc=True,kind='omission')
add('b second cancelled phrase',r'\deleted{\illegible{1} si pour}',r'\struck{\ill{} à prouver}',r'\deleted{\illegible{1} si pour}','The first overwritten word remains physically opaque at 6×; following si pour is readable in the broad crop. (1234,950,1335,1005), 6×; Bfirst 2×.','medium',hc=True,kind='misread word')
add('b inserted coordinates',r'\inserted{(u_0\in U(k),v_0\in V(k))}','coordinates inline',r'\inserted{(u_0\in U(k),v_0\in V(k))}','Both coordinate conditions are above the main line and connected at x=u0v0. Bfirst, 2×.',hc=True,kind='insertion or placement')
add('b cancelled parenthesis',r'\deleted{(tel à U.V)}',r'\struck{(W=U.V)}',r'\deleted{(tel à U.V)}','The three low letter forms before à are tel, not a W followed by equality. Bfirst, 2×.','medium',hc=True,kind='misread word')
add('b image inverse object',r'\unsure{UV|U.V}','U.V','UV','No separate dot is visible between the two capitals, unlike U.V in the preceding cancelled parenthesis. Bfirst, 2×.','high',True,True,'misread symbol or index')
add('b cancelled est st','est st','est stable','est st','Only st is written after est. Bfirst, 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
add('b after g in G^0',r'\unsure{\ldots}','on a',r'\unsure{\ldots}','Short separated marks have no readable o/n/a forms. Bfirst, 2×.','low',hc=True,kind='text not on the page')
add('b base extension parenthesis','après ext. de la base','pour ext. de k ill.','après ext. de la base','Initial après and final la base are readable in the running cursive. Bfirst, 2×.',hc=True,kind='misread word')
add('b deleted extension coordinates',r'\deleted{p. u\in G^0(k prime),v\in}',r'\struck{\ill{}}','C retained','The letters p., u, the superscript 0, parenthesized k prime and following v in remain under the line. Bfirst, 2×.',hc=True,kind=r'readable ink left as \ill{}')
add('b before Ou encore',r'\deleted{\unsure{Ou|Or}}',r'\struck{\ill{}}',r'\deleted{\unsure{Ou|Or}}','Initial O is legible but the joined final stroke is heavily filled. (694,1384,767,1437), 4×.','low',hc=True,kind=r'readable ink left as \ill{}')
add('b Ou encore','Ou encore','On aura','Ou encore','The second word has initial en followed by core; the first ends in a simple u stroke. Bmid (675,1373,1700,1769), 2×.',hc=True,kind='misread word')
add('b inverse image formula',r'\varphi^{-1}(W)=W',r'\varphi^{-1}(V)=W',r'\varphi^{-1}(W)=W','The inner letter has two bottom joins, matching W at the right of the equality. Bmid, 2×.',hc=True,kind='misread symbol or index',conseq='The written inverse image is of W, not H’s V; the mathematical surprise remains.')
add('b deletions before irreducibility and nonempty intersection',r'\deleted{U\cap}; \deleted{T\cap U\ne\varnothing}',r'\struck{\ill{}}; \struck{\ill{}}','C retained','The capital U, cap, and second T-cap-U expression can be followed beneath their horizontal strikes. Bmid, 2×.',hc=True,kind=r'readable ink left as \ill{}')
add('b overwritten factor in gW inverse intersection',r'\cap\deleted U T',r'\cap T',r'\cap\deleted U T','A small crossed U precedes the replacement T. Bmid, 2×.',hc=True,kind='omission')
add('b ouverts ending',r'\unsure{ouverts|ouvert}','ouverts',r'\unsure{ouverts|ouvert}','The very compressed final down-turn does not distinguish a separate s securely. Bend (711,1789,1695,1917), 2×; (1556,1792,1686,1832), 4×.','low')
add('b cancelled conclusion',r'\deleted{\unsure{sont intersectés|se coupent}}','uncertain d’intersection, live',r'\deleted{\unsure{sont intersectés|se coupent}}','A full horizontal strike traverses the old phrase; its joined letters remain uncertain. Bend, 2×; (1448,1846,1684,1898), 4×.','low',hc=True,kind='deletion state (struck given live or live given struck)',marked='yes')
add('b replacement conclusion',r'\inserted{\unsure{int.|inter.} \ne\varnothing,OK}','d’intersection nonempty, cqfd',r'\inserted{int. \ne\varnothing,OK}','The short abbreviation ends after a tall t and dot; OK is large and clear to its right above the cancelled line. (1448,1846,1684,1898), 4×.','high',True,True,'insertion or placement','yes')
add('c final word','du','uncertain dans','du','Only d followed by a low u is written. Lemma (178,1927,1699,2266), 2×.',hc=True,kind='misread word',marked='yes')
add('lemma first cancelled statement',r'Soit \unsure{T|J} une partie de X stable par G^0 \unsure{est} stable par spécialisation.','Soit T ill., partie de X stable ill.','C retained','The horizontal cancellation crosses a full readable statement; the capital T/J and compressed est remain doubtful. Lemma 2×; (487,2001,559,2048) and (1190,1994,1305,2050), 4×.','medium',hc=True,kind=r'readable ink left as \ill{}')
add('lemma deleted label',r'\deleted{\unsure{a)}}','omitted',r'\deleted{\unsure{a)}}','A small filled loop and closing curve under the insertion cannot be completely separated from the cancellation. (438,1983,483,2017), 4×.','low',hc=True,kind='omission')
add('lemma inserted hypothesis indices',r'\varphi_x:G_{\unsure{\kappa|x}}\to X_{\unsure{\kappa|x}}',r'\varphi_x:G_{k prime}\to X_{k prime}','C retained','Both suffixes have low joined strokes without a separate prime; kappa versus x remains uncertain. (739,1960,892,2019), 4×.','low',hc=True,kind='misread symbol or index')
add('lemma inserted hypothesis abbreviation',r'\unsure{gén.}','uncertain générisants','gén.','A compact gén with terminal dot is written, without the longer ending. (908,1964,1007,2008), 4×.','high',True,True,'abbreviation expanded or spelling modernised','yes')
add('lemma deleted Si pi générisant',r'\deleted{Si \pi générisant}',r'\struck{\ill{} générisants}','C retained','Si and pi remain distinguishable at the start of the barred line; no final s is separately written. Lemma, 2×.',hc=True,kind=r'readable ink left as \ill{}')
add('lemma example','p. ex. X un ps torseur','p. ex. X ill.','p. ex. X un ps torseur','The compact ps and all of torseur can be followed before the closing parenthesis. Lemma, 2×.',hc=True,kind=r'readable ink left as \ill{}')
add('lemma assertion and equivalences','alors une partie W de X est stable par G^0 ssi ...; ssi elle est ouverte et fermée','Une partie W de X ill., stable ... est-elle ill. ...; est-elle ouverte et fermée','C retained','The connecting alors and est are visible, and each ssi consists of two joined s forms followed by i. No question-mark ending appears. Lemma, 2×.',hc=True,kind='misread word',conseq='Two written equivalences are restored where H presents questions.')
add('lemma noetherian abbreviation',r'\unsure{noeth|nœth}','noeth.',r'\unsure{noeth|nœth}','The compressed oe/œ join is not resolved; no distinct final period is present. (1010,2115,1170,2193), 4×.','low',hc=True,kind='abbreviation expanded or spelling modernised')
add('lower proof deleted heading',r'\deleted{\unsure{Dém|Réc}}','Dém live',r'\deleted{\unsure{Dém|Réc}}','A separate short deletion crosses the heading; initial and last letters remain overwritten. (353,2267,453,2321), 4×.','low',hc=True,kind='deletion state (struck given live or live given struck)')
add('lower proof number',r'\unsure{b)|1)}','1)',r'\unsure{b)|1)}','The filled small upright before the parenthesis leaves a possible loop. (353,2267,453,2321), 4×.','low')
add('lower inserted action hypothesis',r'\inserted{i.e. \pi induit G^0\times W\to W, donc}','same words inline','C retained','The entire clause is above Supposons and is led into the line; it is not part of the cancelled next sentence. Lemma and deletedproof crops, 2×.',hc=True,kind='insertion or placement')
add('lower cancelled soit and x',r'soit \unsure{x\in|x} x,y\in X \unsure{tq}, y\in\overline{\{x\}}, prouvons','ill. x,y in X ill.','C retained','soit, x,y, the closure braces and prouvons are readable; earlier x with possible membership and tq remain crossed. Deletedproof (168,2262,1692,2499), 2×; (1044,2276,1121,2325), (1270,2261,1398,2329), 4×.','medium',hc=True,kind=r'readable ink left as \ill{}')
add('lower cancelled induced action map',r'i.e. G\times X\to X\times X induit G^0\times W\to W\times W','only latter map','C retained, all deleted','The smaller line to the left contains both maps and induit, enclosed by cancellation guides. Deletedproof, 2×.',hc=True,kind='omission')
add('lower cancelled equivalence and first attempt',r'\deleted{que x\in W iff y\in W. \unsure{1)} x\in W prouvons y\in W. OPS x\in W(k),}','equivalence live, remainder omitted','C retained, all deleted','Horizontal strokes cancel the equivalence and attempted direction; the small 1-like label remains uncertain. Deletedproof 2×; (811,2357,877,2390), 4×.','medium',hc=True,kind='deletion state (struck given live or live given struck)')
add('lower margin',r'\margin{\deleted{Or G\times W\to W\times W est générisant et G}}','same words live with an ill. tail','C retained','The left-margin text is enclosed and crossed along with the proof attempt; no additional readable tail follows G. Marginproof (54,2363,289,2483), 2×.',hc=True,kind='deletion state (struck given live or live given struck)',marked='yes')
add('lower final cancelled attempts',r'\deleted{Mais alors Soit en effet}; \deleted{Si W est st. Mais G^0\times W est stable}','parts ill.; Mais G^0 times W to ill. live','C retained','All words, including est stable which wraps at left, are beneath the enclosing cancellation; no live map arrow is read there. Deletedproof and marginproof, 2×.',hc=True,kind='deletion state (struck given live or live given struck)')
add('live final proof beginning','x générise y; Or OPS','x générisant y; On OPS','x générise y; Or OPS','The verb ends in a short e stroke; the next sentence starts Or. Endproof (302,2470,1693,2780), 2×.',hc=True,kind='misread word')
add('live final proof two maps',r'\varphi:g\mapsto gy, G\to X, induisant \unsure{\varphi prime|g prime}:G^0\to W',r'\varphi:g\mapsto gy, G^0\to W, induisant ill.','C retained','The first source G has no superscript and its target is X; G^0 to W occurs after induisant. The repeated map-label loop remains ambiguous. Endproof, 2×; (312,2552,371,2603), 4×.','medium',hc=True,kind='misread symbol or index',conseq='The two successive maps G→X and G^0→W are both retained.')
add('live final proof générisant accents',r'\unsure{générisant|generisant}','générisant',r'\unsure{générisant|generisant}','Tiny humps above the joined letters do not securely distinguish detached accents from connecting strokes. (785,2551,933,2597), 4×.','low')
add('live final proof On followed by dot',r'On \unsure{a|.}','On a',r'On \unsure{.|a}','The following mark appears as a solid point without a loop or exit stroke; a highly reduced a cannot be excluded. (1020,2614,1139,2656), 4×.','low',True,True,'misread word')
d['unresolved']='Upper μ/outlined H (suffix r), overwritten O/G and k_red/G_red, Delta relation, R and C alphabets, barred R alphabet, transp./topos, deleted diagram index +1/+n, lambda star, mark after a), one opaque deleted word, ellipsis, deleted Ou/Or, ouverts ending and cancelled intersection phrase; lower cancelled T/J, est and a), base suffixes κ/x, noeth/nœth, cancelled Dém/Réc and proof numbering, cancelled x∈/x and tq, final φ prime/g prime, accents in générisant, On followed by a dot or a highly reduced a.'
inv=[
('deletion','upper left line 1','mu_r; G; G^0; k[[t'),
('deletion','upper left line 2','k; overwritten O/G; k_red/G_red'),
('deletion','upper left line 2','Delta_0 relation Delta'),
('deletion','upper category line 1','R=Ab(C)^op; barred R; sigma={G^h}'),
('deletion','upper category line 2','double repetition marks; G^n-G^m'),
('deletion','upper category line 3','Ab(C); G^n→G'),
('diagram','upper left','Hom prime; circled sigma; ENS; FN; transp.; sp R'),
('deletion','upper diagram','broad oblique cancellation strokes'),
('deletion','upper right opening','Soit'),
('deletion','upper right block','Disons posant (C_i prime,lambda_i prime)'),
('deletion','upper right after ordered pairs','C_i prime est tel que'),
('diagram','upper right','C_i prime→C_{i+1} prime; C_psi(i); C_psi(i+1)=g psi(i)'),
('deletion','upper right diagram index','+1/+n'),
('deletion','upper right ordinal proof','est lambda_i prime-préexact. Donc si omega prime'),
('deletion','inside ordinal proof','si'),
('insertion','above ordinal proof','equals sign'),
('deletion','ordinal proof ending','donc g(omega)='),
('margin note','left above proof','double-underlined Lemme'),
('text','proof heading','Dém prop; a) est trivial; small mark'),
('text','b opening','OPS U,V nonempty, on est ramené'),
('deletion','b opening','Soit x in'),
('deletion','b first line','illegible si pour'),
('deletion','b after si','x in W=U.V W(k)'),
('insertion','b coordinates above line','u_0 in U(k),v_0 in V(k)'),
('deletion','b after coordinates','tel à U.V'),
('text','b map and base change','alors l’image inverse de UV'),
('deletion','b before contient','est st'),
('deletion','b base extension','p. u in G^0(k prime),v in'),
('text','b equivalences','Ou encore u inverse gx in V'),
('deletion','b preceding Ou encore','Ou/Or'),
('deletion','b third equivalence','u in g'),
('text','b intersections','donc il suffit de voir'),
('deletion','b before T est irréductible','U intersection'),
('deletion','b following irréductible','T intersection U nonempty'),
('deletion','b gW inverse intersection','U overwritten by T'),
('text','b bracketed verification','car gu_0 in T'),
('text','b end','Mais alors gW inverse intersection T'),
('deletion','b end','sont intersectés/se coupent'),
('insertion','b end above line','int. nonempty, OK'),
('text','c','Résulte de la partie a) du'),
('text','lemma heading','Lemme'),
('deletion','lemma first statement','Soit T/J une partie de X'),
('deletion','lemma small label','a)'),
('insertion','lemma hypothesis above line','Si les phi_x:G_suffix→X_suffix gén.'),
('deletion','lemma superseded hypothesis','Si pi générisant'),
('text','lemma statement','p. ex. X un ps torseur, alors'),
('text','lemma parenthetical equivalence','i.e. si X loc noeth'),
('deletion','lower proof heading','Dém/Réc'),
('text','lower proof opening','b)/1) Supposons W stable'),
('insertion','above lower proof','i.e. pi induit G^0×W→W, donc'),
('deletion','lower proof first attempt','soit x in/x x,y in X tq'),
('deletion','lower proof smaller left line','i.e. G×X→X×X induit'),
('deletion','lower proof equivalence','que x in W iff y in W'),
('deletion','lower proof first direction','1) x in W prouvons y in W, OPS'),
('margin note','lower left','Or G×W→W×W est générisant et G'),
('deletion','lower left marginal attempt','Or G×W→W×W est générisant et G'),
('deletion','lower proof second attempt','Mais alors Soit en effet'),
('deletion','lower proof third attempt','Si W est st. Mais G^0×W est stable'),
('text','bottom live proof','Montrons que si y in W, x générise y'),
('text','bottom last argument','or phi est générisant; On . / a prouvé')
]
d['inventory']=[list(x) for x in inv]
runpy.run_path(str(root/'scripts/review.py'))['commit'](d)
