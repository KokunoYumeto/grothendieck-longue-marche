from pathlib import Path
import csv,json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=root/'edition/second/145_scan003_second.tsv'
manifest_path=root/'edition/second/145_scan003_second_manifest.json'
readings=[]
observations={}
def add(box,reading,notes=()):
    readings.append((box,reading))
    observations[box]=list(notes)
def save():
    with out.open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f,delimiter='\t')
        writer.writerow(['box','reading'])
        writer.writerows(readings)
    manifest=json.loads(manifest_path.read_text())
    for m in manifest:
        if m['box'] in observations: m['observations']=observations[m['box']]
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
add('B01',r'Les autom. \inserted{\unsure{int}} de $\widehat{\Pi}_{0,3}\simeq\unsure{\pi|\Pi}$ commutant \deleted{\unsure{à}} $\sigma_0$,',[
 'The short inserted word above de is not fully resolved; its first dotted short stroke and tall final crossing support int provisionally. Its upper contour meets the crop edge.',
 'The small group letter following the relation sign is locally ambiguous in case. The cancelled character before sigma0 is dense and remains uncertain.'
])
add('B02',r'$u(l_{\unsure{1|0}})=\operatorname{int}(g_1)l_1^p$',[
 'The first l subscript is a filled retraced shape; 1 is preferred, with 0 retained as a local alternative. No closing argument parentheses or final stop are added to the right-hand l1 power.'
])
add('B03',r'\margin{\uline{NB} on aura $u(l_0)=\operatorname{int}(\underbrace{g_1l_1^{-\gamma}\rho^{-1}(h_1)}_{g_0})\cdot\unsure{l_0^p}$}',[
 'Only the oblique marginal note is transcribed. Clipped main-body strokes, sigma0 and a rho/comma above it are incidental to this box.',
 'The final l0 power meets a punch hole and the outer page edge; the surviving factor is retained with a local doubt. NB has one underline; the g0 label belongs to the underbrace.'
])
add('B04',r'\margin{\uline{et $\bar m$ pour} \uline{$u$}!}',[
 'The middle abbreviated letter has a separate overbar. One underline extends beneath et, the barred letter and pour; a second underline belongs to u. The exclamation mark is separate.'
])
add('B05',r'$(1)\quad\boxed{l_\infty^p\cdot\operatorname{int}(h_1)(l_1^p)\cdot\operatorname{int}(h_1l_1^{-\gamma}\rho^{-1}(h_1))(l_0^p)=1}$',[
 'The complete rectangular frame and left-hand number1 are included. All three visible p powers and the two lower indices1 plus final0 are read from their strokes.'
])
add('B06',r'et $(2)\quad\boxed{\rho(h_1)(l_\infty^{-\gamma}=h_1l_1^{-\gamma})\rho^{-1}(h_1)=l_0^\beta}$',[
 'Between the linfinity power and h1 inside the parenthesis there are two distinct short horizontal strokes, transcribed as an equals sign without mathematical repair.',
 'The visible initial et and left-hand number2 are included; partial neighboring border/strokes at the edges are incidental.'
])
add('B07',r'\margin{NB. On doit en fait avoir $\beta\unsure{=|\ne}\gamma$ (\unsure{passer} à $(\Pi_{0,3})_{\mathrm{ab}}$)}',[
 'The middle relation sign is small and entangled with adjacent long strokes; its equality/inequality reading remains local.',
 'The parenthetical first word is compressed and remains doubtful. The main-body fragments at the lower and right edges are clipped incidental text and have not been completed.'
])
save()
print('Independent prefix saved:',len(readings),'of19 boxes; not yet submitted as immutable.')
add('B08',r'avec $h_1=\unsure{\dot\sigma_0|\sigma_0^{\prime}}(g_1)^{-1}g_1$',[
 'A small separate mark above/right of sigma is visible, but its placement and short oblique shape leave dot versus prime uncertain.',
 'The word avec begins at the left edge. Incidental marginal fragments and faint isolated traces above/left are not completed into additional text.'
])
add('B09',r'$h_1l_1^{-\gamma}\rho^{-1}(h_1)=l_\infty^\gamma\rho(h_1)^{-1}l_0^{\deleted{\unsure{\gamma}}\beta}$',[
 'A small dense cancelled superscript immediately before the live beta remains doubtful. Gamma is only a provisional recovery of its curled outline.',
 'The prose above and below the formula is clipped by this formula box and is not completed here.'
])
add('B10',r'et en portant dans la première relation, celle-ci peut se \unsure{réduire|récrire} \begin{tikzpicture}[baseline]\draw[->] (0,1)--(0,0);\end{tikzpicture}',[
 'The last verb is affected by faint/overlapping strokes; reducing versus rewriting remains a local lexical alternative.',
 'A downward leader arrow points to the framed formula below. The preceding formula and some upper strokes of relation are clipped at the top; the next formula is clipped below.'
])
add('B11',r'$(1^{\prime})\quad\boxed{l_\infty^p\cdot\unsure{\operatorname{int}h_1|\operatorname{int}(h_1)}(l_1^p)\cdot\operatorname{int}(l_\infty^\gamma\rho(h_1)^{-1})(l_0^p)=1}$',[
 'The first int/h1 group is tightly connected. No separate pair of argument parentheses is confidently isolated there; the two readings preserve that local uncertainty.',
 'The numeral with its prime and the full frame are included. Prose above and the following NB line below are incidental clipped context.'
])
add('B12',r'en $h_1^{\prime}=$',[
 'The formula is cut off immediately after its equality by this narrow box; no right-hand continuation is supplied in this row. The short initial word is read as en.'
])
add('B13',r'en lui appliquant $\operatorname{int}(l_\infty^{-\mu})$:',[
 'The complete requested prose and operator expression are read. The long lower strokes of appliquant meet the bottom edge. The h1-prime formula above and the formula below are clipped incidental passages.'
])
add('B14',r'$l_\infty^p\cdot\operatorname{int}(\unsure{h_1^{\prime}})(l_1^p)\cdot\operatorname{int}(\deleted{\unsure{h_1}}l_\infty^{\unsure{\gamma^{\prime}|\gamma}}\unsure{\rho^{\deleted{\unsure{-1}}}|\widehat\rho}(h_1^{\prime})^{-1})(l_0^p)=1$',[
 'The first h1-prime body is crossed by closely adjacent strokes and remains locally doubtful.',
 'A dense cancelled group occurs immediately after the second int opening parenthesis. The provisional h1 recovery remains uncertain.',
 'The exponent above linfinity has retracing and a possible prime. The small dark mark above rho is not confidently separated into a cancelled inverse exponent or a hat; both states are recorded without algebraic repair.',
 'The upper prose/operator expression and lower prose are clipped context. The visible minus1 above the last h1-prime argument meets the upper crop edge.'
])
add('B15',r'(\uline{i.e.} \uline{$\gamma^{\prime}=\gamma\deleted{\unsure{+\mu}}$}) et on a \unsure{entre les relations|une relation} correspondant à $(2)$, avec $\unsure{\beta^{\prime}}=\beta$.',[
 'There is an underline beneath i.e. and a separate underline beneath the gamma-prime equation. The left underline begins near the opening-parenthesis foot.',
 'The strokes after the live gamma are cancelled and only provisionally recovered as plus mu.',
 'The compressed phrase after et on a is not completely resolved; its alternatives are preserved in the reading. The first beta-prime is heavily retraced, while the final beta and stop are clear.',
 'The preceding formula at the upper edge is clipped and is not completed in this prose box.'
])
add('B16',r'\mspage{2}',[
 'The single handwritten numeral2 is clear.'
])
add('B17',r'$u(l_\infty)=\operatorname{int}(\underbrace{\sigma_0(g_1)}_{g_\infty})l_\infty^p$',[
 'The underbrace spans sigma0(g1), with label ginfinity. No over-dot is visible on this sigma0.',
 'The top of the last p and the lower end of the underbrace label meet the crop edges; their surviving contours are legible.'
])
add('B18',r'avec $g_1\in\Pi\ \mathrm{mod}\ L_1$, $p\in\widehat{\mathbb Z}^{*}$ satisfaisant la condition (\unsure{où|ici} $\beta,\gamma\in\widehat{\mathbb Z}$ sont uniquement déterminés par $g_1,p$)',[
 'Pi has a cap and two full legs; L1 has the straight capital-L form. The operator mod has no visible stop.',
 'The small word after the opening parenthesis has an upper accent/short stroke and compressed lower curves; où is preferred with ici retained locally.',
 'The previous underbrace label is clipped at the top and is not repeated. No colon is supplied after the closing parenthesis.'
])
add('B19',r'\uline{NB} Si on change $g_1$ en $g_1^{\prime}=g_1l_1^\mu$, $h_1$ est remplacé en $h_1^{\prime}=l_\infty^{-\mu}h_1l_1^\mu$, et la relation $(1^{\prime})$ donne, en lui appliquant $\operatorname{int}(l_\infty^{-\mu})$:',[
 'NB is underlined without a separate following stop. The initial Si has a tall first letter. The complete g1 and h1 change formulas, mu powers, and relation number with prime are included.',
 'The uppermost strokes of remplacé and the first mu meet the top edge; the word and letter are recoverable from the remaining strokes. The next formula is clipped along the lower edge and is not completed in this box.'
])
save()
print('Independent complete draft saved:',len(readings),'boxes; awaiting structural checks before submission.')
