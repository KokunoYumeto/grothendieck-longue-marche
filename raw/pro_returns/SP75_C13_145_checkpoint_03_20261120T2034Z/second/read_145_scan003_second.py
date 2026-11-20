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
