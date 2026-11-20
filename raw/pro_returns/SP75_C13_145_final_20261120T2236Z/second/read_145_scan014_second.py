from pathlib import Path
import csv, json
base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition')
readings=[]
observations={}
def add(box,reading,notes=()):
    readings.append((box,reading))
    observations[box]=list(notes)

add('B01',r'\[\begin{aligned}\varepsilon_0^2&=l_0\\\varepsilon_1^2&=l_1\\\varepsilon_\infty^2&=l_\infty\end{aligned}\]', ['All three exponents are positive 2. No punctuation is added to the three equations.'])
add('B02',r'Ce qui redonne', ['The q descender meets the bottom crop boundary. The selected phrase ends before the next word.'])
add('B03',r'\deleted{\unsure{par}}', ['The long descending first stem supports p. The horizontal strike obscures the following small letters, so the cancelled word remains doubtful.', 'A clipped fragment of the preceding comma appears at the far left; it is incidental to the selected cancelled word.'])
add('B04',r'\[\begin{aligned}\sigma_0&=\varepsilon_0\varepsilon_1^2\\\sigma_1\unsure{.}&=\varepsilon_1\varepsilon_\infty^2\\\sigma_\infty&=\varepsilon_\infty\varepsilon_0^2\end{aligned}\]', ['All indices and three positive 2 exponents are visible.', 'A small isolated low dark mark follows the subscript 1 in the middle left-hand sigma. It is recorded as a doubtful dot; whether it is intentional punctuation or incidental ink is unresolved.'])
add('B05',r'\[\left\{\begin{aligned}\varepsilon_0^2\varepsilon_1^2\varepsilon_\infty^2&=1\\(\varepsilon_0\varepsilon_1^2)^2&=1\\(\varepsilon_1\varepsilon_\infty^2)^2&=1\\(\varepsilon_\infty\varepsilon_0^2)^2&=1\end{aligned}\right.\]', ['The single tall left brace groups all four relations. Every index, exponent and terminal one is included.'])
add('B06',r'On retrouve $\rho$ \deleted{\unsure{comme}} par', ['The cancelled middle word begins with a visible c-like curve, but the horizontal stroke merges with its remaining low letters. No abbreviation or punctuation is supplied.'])
add('B07',r'\[\begin{array}{l}\deleted{\rho=\sigma_0\sigma_1=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0}\\\qquad\Vert\\\qquad\deleted{\varepsilon_0\varepsilon_1^3\unsure{\varepsilon_\infty|\varepsilon_0}}\end{array}\]', ['The upper formula is crossed by a continuous line; its sigma bodies and indices remain distinguishable.', 'Two separate small vertical parallel strokes stand between the formula and the lower product.', 'The lower product is separately struck. Its final epsilon index is compact and obscured; infinity and zero remain alternatives. No exponent is recovered after that last epsilon.'])
add('B08',r'\inserted{$\sigma_0\sigma_1=l_1^{-1}\rho$}', ['The minus and one are separate clear superscript strokes. The lower crop edge includes only a clipped portion of the crossed formula below, not additional insertion text.'])
add('B09',r'\margin{donc \[\begin{aligned}\rho&=l_1\sigma_0\sigma_1\\&=\varepsilon_1^2\varepsilon_0\varepsilon_1^2\varepsilon_1\varepsilon_\infty^2\\&=\varepsilon_1^2\varepsilon_0\unsure{\varepsilon_1^{\deleted{\unsure{3|2}}}\underbrace{\varepsilon_1^2\varepsilon_\infty^2}_{\varepsilon_0^{-2}}}\end{aligned}\]}', ['The full three-line marginal calculation is retained, including the lower epsilon_0 to the power minus 2.', 'A dense crossed superscript above the first of the last three epsilon factors cannot be read securely as 3 or 2.', 'The following epsilon_1 body is retraced, with its positive 2 visible.', 'The long lower bracket ends under the final infinity factor. Its angled left end reaches back toward the preceding epsilon_1; the preferred scope starts under the final two factors, but inclusion of that preceding factor remains uncertain. The whole local group is marked doubtful for this reason.', 'No terminal punctuation is supplied.'])
add('B10',r'\[\begin{aligned}\rho&=\varepsilon_1^2\varepsilon_0\varepsilon_1\varepsilon_0^{-2}\\&=\varepsilon_\infty^2\varepsilon_1\varepsilon_\infty\varepsilon_1^{-2}\\&=\varepsilon_0^2\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-2}\end{aligned}:\]', ['The last index in the first row is zero. The three final exponents are explicitly minus 2.', 'Two separated marks at the lower right form the terminal colon.'])
add('B11',r'\margin{ces relations \unsure{en|se} \unsure{résultent|déduisent} par conjugaison des autres}', ['A long vertical rule separates this three-line marginal note from the formulas.', 'The short group after relations and the compressed verb on the second line remain uncertain. The last line is read des autres, without a final stop.'])
add('B12',r"multipliant \deleted{\unsure{dans|donc}} ces relations dans l'ordre inverse et écrivant $\rho^3=1$, on trouve", ['The cancelled short word has a clear initial d-like ascending stroke, but its middle letters overlap the strike.', 'The live inverse, et écrivant, exponent 3, equality to 1, comma and on trouve are all retained.', 'Some upper strokes of the first line touch the crop boundary; no continuation is supplied outside the selection.'])
add('B13',r'\[(\varepsilon_0\varepsilon_1\varepsilon_\infty)^2=1\]', ['The outer right parenthesis is angular but continuous. The final one has a broad baseline foot; it is not separately underlined.'])
add('B14',r", car il n'y a pas d'autres", ['The leading comma is included. The phrase ends at the page foot without a terminal stop or supplied continuation.'])
add('B15',r'\mspage{13}', ['Both digits are visible.'])

out=base/'second/145_scan014_second.tsv'
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['box','reading']); w.writerows(readings)
mp=base/'second/145_scan014_second_manifest.json'
manifest=json.loads(mp.read_text(encoding='utf-8'))
for item in manifest:
    item['observations']=observations[item['box']]
    item['inspected']=True
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Saved {len(readings)} independent readings and {len(manifest)} inspected crop records; not yet submitted.')
