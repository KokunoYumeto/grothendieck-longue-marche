from pathlib import Path
import csv, json

base = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition')
readings = []
observations = {}
def add(box, reading, notes=()):
    readings.append((box, reading))
    observations[box] = list(notes)

add('B01', r'\mspage{3}')
add('B02', r'$(p;g)$', ['The separator has an upper dot and lower comma: semicolon. Both parentheses are visible.'])
add('B03', r'Ça semble', ['The capital Ç is heavily retraced; a separate cedilla is visible. The selected phrase ends before the following word.'])
add('B04', r'Dans le cas de $\tau$, on a $p=-1$, et $g=l_1$:\[\tau\rho=\operatorname{int}(l_1)\rho\tau\]', ['The colon after l_1 is present. No terminal punctuation is visible after the displayed equation.'])
add('B05', r"On veut exprimer la commutation (\unsure{comme|\deleted{comme}} autom ext \inserted{\unsure{respectant les structures d'inertie}}) non seulement", ['The upper line is clipped along its top and right edges; no continuation outside the box is supplied.', 'The first letters of comme are densely retraced or cancelled; the state is retained as a local alternative.', 'The interlinear phrase is hooked into the parenthesis after ext. Its opening cluster and the letters around les are entangled; the whole proposed insertion remains doubtful.', 'No distinct full stop is visible after autom or ext.'])
add('B06', r'$\unsure{\mathfrak{S}_3^{+}|G_3^{+}}$, mais à $\unsure{\mathfrak{S}_3|G_3}$', ['The two large looped capitals have rounded outer walls and an internal curl; their identification as a script S rather than G remains uncertain. The plus and both subscript threes are clear.'])
add('B07', r'\unsure{r}elation:', ['The left edge clips part of the initial r. The colon has two distinct marks. Incidental fragments of the preceding and following lines are excluded.'])
add('B08', r'mod \unsure{int|entre}', ['The first word ends in a looped d. The following compressed group has a closed initial loop and a tall later stroke; int versus a word resembling entre remains unresolved. No abbreviation stop is visibly separate. The lower edge contains only tops of the following line.'])
add('B09', r"\margin{\uline{NB} \unsure{Cela|Ceci} implique qu'il opère \unsure{triv\textsuperscript{t}} sur l'ens. des trois classes de conjugaison \unsure{de|des} s-groupes d'inertie. \unsure{ce qui précède exprime|ce qui précède explique}}", ['The note is oblique; the saved crop was rotated -42 degrees.', 'The NB underline is visible. Cela/Ceci, the abbreviated group after opère, the small de/des and the last verbal group remain doubtful.', 'A stop is visible after the proposed inertie, but no terminal stop is supplied after the last doubtful verbal group.', 'The last line is difficult to separate at its right end from main-text strokes. Its final proposed word is kept doubtful rather than supplied as certain.', 'Incidental main text includes a large subscript-three group at the right and a clipped c.-like introductory cluster below; these are not appended to the marginal passage.'])
add('B10', r'$u\sigma_\infty=\operatorname{int}(h)\deleted{\unsure{\tau|u}}\sigma_\infty u,$', ['The cancelled symbol between int(h) and the live sigma is densely crossed; tau and u remain alternatives. Both live sigma subscripts are infinity. The final comma is visible.'])
add('B11', r'les arguments', ['The word has initial a-r followed by a deep g descender, then u-m-e-n-t-s. No terminal stop is visible.'])
add('B12', r'$l_0$ et $l_1$. On trouve les conditions', ['The period after l_1 is distinct. Some upper strokes of conditions meet the box boundary.'])
add('B13', r'\[\begin{gathered}u\sigma_\infty(l_0)\\\Vert\\\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}\end{gathered}=\operatorname{int}(h)\underbrace{\sigma_\infty(l_0^p)}_{l_1^p}\qquad\text{i.e.}\quad\operatorname{int}(g^{-1}h)l_1^p=l_1^p\quad\text{i.e.}\]\[g^{-1}h\in L_1\quad\text{i.e.}\quad h=g l_1^{pq}\qquad q\in\widehat{\mathbb Z}\]', ['The first sigma group is retraced. Two small vertical parallel strokes connect its expression to u(l_1) below; they are represented by Vert.', 'Both underbraces and their complete labels are retained.', 'The exponent at the far-right h expression appears to contain p followed by q; it is transcribed as written without using subsequent formulas to normalize it.', 'The final membership sign, capital L with index 1, and hat above Z are visible. The uppermost p strokes touch the crop boundary.'])
add('B14', r'\[u\underbrace{\sigma_\infty(l_1)}_{l_0}=\operatorname{int}(h)\sigma_\infty\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}\qquad\text{i.e.}\quad\unsure{;|:}\]', ['The first underbrace is under sigma_infinity(l_1), not under the initial u.', 'A small i.e. is visible at the upper right. Two low marks farther left resemble a semicolon or colon; their exact role and punctuation form remain uncertain.'])
add('B15', r'\[l_0^p=\operatorname{int}(h\sigma_\infty(g))l_0^p\qquad\text{soit}\]\[l_0^p=\operatorname{int}(g l_1^q\sigma_\infty(g))l_0^p\qquad\text{ce qui équivaut à}\]', ['The lower exponent immediately after l_1 is q. Both outer and inner closing parentheses are preserved. No terminal punctuation follows à.'])
add('B16', r'\deleted{$\unsure{\operatorname{int}(g l_1^q\sigma_\infty g)L_1=L_0}$} i.e. la condition', ['A long cancellation stroke crosses the whole formula through the final L_0. The recovered expression remains a whole-formula doubt.', 'The cluster between g and l_1 includes an additional dense overwritten or cancelled loop. Its independent lexical value cannot be separated securely; the whole-formula uncertainty includes this obscured cluster.', 'The last live phrase reads i.e. la condition without a visible terminal stop.'])
add('B17', r'$\exists q$ tel que $g l_1^q\sigma_\infty(g)\in L_0$', ['The low descenders meet the black scan edge, but the visible heads and strokes support the stated letters. No punctuation is added after L_0.'])
add('B18', r'\mspage{8}', ['The two loops and central crossing of the handwritten eight are visible.'])

out = base / 'second/145_scan009_second.tsv'
with out.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['box', 'reading'])
    writer.writerows(readings)
mp = base / 'second/145_scan009_second_manifest.json'
manifest = json.loads(mp.read_text(encoding='utf-8'))
for item in manifest:
    item['observations'] = observations[item['box']]
    item['inspected'] = True
mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Saved {len(readings)} independent readings and {len(manifest)} inspected crop records; not yet submitted.')
