from pathlib import Path
import csv,json
base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition')
readings=[];observations={}
def add(box,reading,notes):
    readings.append((box,reading));observations[box]=notes
add('B01',r'Donc les relations \[(13)\quad\left\{\begin{aligned}\unsure{\tilde\sigma_0^2|\widetilde{\tilde\sigma}_0^2}&=\tilde\sigma_1^2=\tilde\sigma_\infty^2=1\\\tilde\sigma_0\tilde\sigma_1&=\tilde\sigma_1\tilde\sigma_\infty=\tilde\sigma_\infty\tilde\sigma_0=\overset{\deleted{\unsure{\sim}}}{\rho}\deleted{\unsure{(=\rho)}}\\\bigl(\overset{\deleted{\unsure{\sim}}}{\rho}^{3}&=1\ \text{est conséquence des précédentes}\bigr)\end{aligned}\right.\]',[
'Handwritten (13) beside a single left brace grouping the display.',
'The first tilde has separated retracing above its main wave; single-versus-double-tilde uncertainty is kept locally.',
'The second-row final rho has dense zigzag ink over its accent and an adjacent parenthetical expression; a cancelled tilde and cancelled (=rho) are provisional underlying readings.',
'The third-row rho similarly has a scribbled-out raised accent, provisionally a tilde. Its exponent 3 remains live.',
'Outer parentheses enclose the complete third-row statement. No article or final punctuation is supplied.'
])
add('B02',r'\margin{NB \[\rho\tilde\sigma_i\rho^{-1}=\tilde\sigma_{\dot\rho i}\quad\text{i.e}\qquad\begin{aligned}\rho\tilde\sigma_0\rho^{-1}&=\tilde\sigma_1\\\rho\tilde\sigma_1\rho^{-1}&=\tilde\sigma_\infty\\\rho\tilde\sigma_\infty\rho^{-1}&=\tilde\sigma_0\end{aligned}\]}',[
'Prescribed crop rotated -45 degrees once. All four complete marginal equations were inspected.',
'Every sigma has a tilde. The general right-hand subscript consists of a dotted rho followed by i with its own dot.',
'The three particular equations have successive indices 0 to 1, 1 to infinity, and infinity to 0. Their rho inverse exponents are retained.',
'NB has no visible punctuation; i.e has no visible final stop. Curved fragments at the right edge belong to the main text.'
])
add('B03',r"et l'image inverse $\widetilde{\mathcal E}$ de $\varphi(\overset{\deleted{\unsure{\sim}}}{\mathfrak S}_3)\subset\Gamma$ (groupe d'indice 2) est produit $1/2$ direct de $\unsure{\widetilde{\mathfrak S}_3|\mathfrak S_3}$ et de",[
'Two main prose lines. The top clipped equation belongs to B01 and is not repeated.',
'The inverse-image group has a clear tilde above an E-shaped glyph; the containing group is capital Gamma, with one vertical wall and a short cap.',
'A dense small raised mark above the first S is read as a cancelled, uncertain tilde. The second S has a short raised mark, retained as a live-tilde-versus-bare-symbol doubt.',
'The handwritten fraction is 1/2 before direct. The source reads groupe d\'indice 2 in parentheses.',
'The sentence continues after et de; no completion is supplied.'
])
add('B04',r'$\pi$. Il faut expliciter les opérations des $\tilde\sigma_a$ sur\unsure{.} $\pi$ pour avoir la structure complète du groupe, On trouve que $\tilde\sigma_a$ est au dessus',[
'Three complete prose lines; the first pi closes the preceding sentence.',
'Both sigma subscripts have an oval and a right downstroke and are read a. Their tildes are clear.',
'A tiny isolated point after sur is recorded as doubtful punctuation.',
'On after the comma begins with a conspicuous capital O. The ending au dessus is left open for the next box.'
])
add('B05',r'$\varphi(\overset{\deleted{\unsure{\sim}}}{\sigma}_a)$ i.e. la symétrie \unsure{p.r.|p.v.} au plan passant par $P$, $\bar P$, $\deleted{\unsure{\infty|a}}i$, qui transforme les $\unsure{l_0\mapsto}l_0^{-1}$, $\unsure{l_\infty|\deleted{l}l_\infty}\mapsto l_{\unsure{1|0}}^{-1}$, $l_1\mapsto l_\infty^{-1}$ :',[
'Three main-text lines. The tilde-like accent over sigma inside phi is scribbled out and its underlying form remains doubtful.',
'The abbreviation after symétrie is provisionally p.r., with p.v. retained as an alternative.',
'A small dense cancellation precedes live i after P and P-bar. Infinity-versus-a remains an uncertain underlying symbol; it is not silently omitted.',
'The initial l0 and arrow overlap marginal writing and are qualified. The linfinity source of the next mapping has doubled ascenders, possibly a local cancelled l plus live linfinity.',
'The next target index is narrow and heavy, favoring 1 over 0, and stays locally qualified. All visible inverse exponents and the final colon are retained.',
'Ornate group and prose fragments at the upper-left belong to the adjoining marginal note, not this main sentence.'
])
add('B06',r'\margin{Ce sont des structures par transport de structure, via les opérations de $\unsure{\varphi(\mathfrak S_3)|\mathfrak S_3}$ sur $(\unsure{\gamma|\eta},\beta)$}',[
'Prescribed crop rotated -40 degrees once. The six-line marginal prose was read in full.',
'The words structures par transport de structure are retained as written, with singular structure after de.',
'The group S with subscript 3 is clear; a preceding long-looped form may be phi and a parenthesis, but overlap/framing keeps that prefix and the closing parenthesis uncertain.',
'The first member of the final parenthetical pair has a curled descending form, provisionally gamma with eta alternative; the second is beta.',
'No terminal punctuation is supplied. Main-text fragments at the right and bottom are identified as incidental.'
])
add('B07',r'\[(14)\quad\left\{\begin{aligned}\tilde\sigma_0l_0\tilde\sigma_0^{-1}&=l_0^{-1}\qquad\tilde\sigma_0l_1\tilde\sigma_0^{-1}=l_\infty^{-1}\qquad\tilde\sigma_0l_\infty\tilde\sigma_0^{-1}=l_1^{-1}\\\tilde\sigma_1l_1\tilde\sigma_1^{-1}&=l_1^{-1}\qquad\unsure{*|\ldotp}\,\ldotp\ldotp\ldotp\\\ldotp\ldotp\ldotp\ldotp\end{aligned}\right.\]',[
'Handwritten (14), a left brace, three complete top-row equations and one complete second-row equation.',
'Every sigma tilde, subscript and inverse exponent was read independently.',
'The second-row continuation has a dark star-like first mark followed by three small horizontal dots/dashes; star-versus-first-dot uncertainty is explicit.',
'The final row contains four separate short continuation marks. They are counted rather than expanded into conjectural equations.',
'Oblique marginal text crossing the left edge is not part of the formula display.'
])
add('B08',r'\margin{\uline{Critique} La n. $\tilde\sigma_0$ suggère plutôt que $\tilde\sigma_0$ est au dessus de $\unsure{\sigma_0|\sigma}$ — il vaut mieux écrire $\dot\sigma_i^{\prime}=\dot\sigma_i\unsure{\bar\imath|\bar\tau}$ et noter $\tilde\sigma_i^{\prime}$ au lieu de $\tilde\sigma_i$ $(i\in\{0,1,\infty\})$, ou mieux $\sigma_i^{\prime}$ (sans $\sim$) — pour réserver $\tilde\sigma_i^{\prime}$ \unsure{à} des éléments de $\unsure{S\Sigma|S\mathcal E}$, cf plus loin...}',[
'Prescribed tall crop rotated -45 degrees once. The entire long marginal Critique note was inspected in source order.',
'Only Critique is underlined. The following abbreviation is read literally La n.; it is not expanded to notation.',
'The sigma at the far right after au dessus de has a clipped/obscured subscript, retained as sigma0-versus-bare-sigma uncertainty.',
'The proposed equation has over-dotted sigmas and a genuine prime on its left sigma. Its final barred character is provisionally dotless i, with barred tau alternative.',
'The note subsequently distinguishes primed tilde-sigma, unprimed tilde-sigma, and primed sigma without tilde. These proposed changes are recorded here, not applied to earlier page text.',
'The parenthetical index set is i in {0,1,infinity}. All three members and braces were read.',
'The last group consists of S followed by an angular three-stroke glyph, uncertain Sigma versus calligraphic E; it is not normalized from context.',
'The final cf has no visible stop; plus loin is followed by three terminal dots.',
'Incidental main-text fragments, labels (14)/(15), brackets and formulas along the right edge are not continuations of this marginal note.'
])
add('B09',r'Les relations (13) (14), plus la relation fondamentale $l_\infty l_1 l_0=1$ (1), font une présentation de',[
'Two complete main-text lines; relation numbers (13), (14) and (1), both commas and the order infinity, 1, 0 in the product are retained.',
'The dark raised zigzag above the gap between the first two factors is overlapping marginal writing from B08, not an exponent or new factor of this equation.',
'The source sentence continues after de; no closing punctuation is added.'
])
add('B10',r'$\unsure{\widetilde G|\widetilde{\mathcal E}}$, dont on peut bien sûr éliminer $\rho$, en omettant d\textquoteright écrire la relation qui \unsure{le|la} définit)',[
'Two main-text lines. The group letter is an open round capital with a small inward foot and a tilde; G is preferred but calligraphic E remains a local alternative.',
'Both commas are visible. The final pronoun has a low terminal stroke, provisionally le with la alternative.',
'A closing parenthesis is visibly present at the far-right end. No matching opening parenthesis is supplied to repair the source.',
'Clipped oblique marginal text at the left edge is not part of the sentence.'
])
add('B11',r'On peut maintenant remonter à \unsure{nos|ces} trois \unsure{anciens}, \unsure{en|6} p',[
'Two short main-text lines before the displayed definitions. The tall internal stroke in remonter is retained.',
'The short determiner before trois and the low, lightly written word anciens remain locally uncertain.',
'The small looped form after the comma is provisionally en but can resemble a 6. The following visible p is not expanded into a conjectural word.',
'No final punctuation is visible.'
])
add('B12',r'\[(15)\quad\left\{\begin{aligned}\tau_0&=\sigma_0\tilde\sigma_0=\tilde\sigma_0\sigma_0\\\tau_1&=\sigma_1\tilde\sigma_1=\tilde\sigma_1\sigma_1\\\tau_\infty&=\sigma_\infty\tilde\sigma_\infty\unsure{\equiv|=}\tilde\sigma_\infty\sigma_\infty\end{aligned}\right.\qquad\text{donc}\qquad(\unsure{16|6})\quad\left\{\begin{aligned}\tau_0^2&=1\\\tau_1^2&=1\\\tau_\infty^2&=1\end{aligned}\right.\]',[
'Two three-row displays with separate left braces and handwritten labels. Left (15) is clear; the right label is provisionally (16), with a local possibility of (6) because the leading stroke is not cleanly detached.',
'Every sigma position, tilde, tau index and positive exponent 2 was inspected. No inverse exponents are supplied to the tau squares.',
'The last middle equality in the left display has a third short slanted upper stroke; equiv-versus-equals is retained locally.',
'The word donc is dark/retraced but not clearly cancelled. No final punctuation is supplied.'
])
add('B13',r'\mspage{20}',[
'Handwritten footer 20, with a closed oval 0; no cancellation or terminal punctuation.'
])
def save():
    with (base/'second/145_scan021_second.tsv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['box','reading']);w.writerows(readings)
    mp=base/'second/145_scan021_second_manifest.json'
    manifest=json.loads(mp.read_text(encoding='utf-8'))
    for e in manifest:
        e['inspected']=e['box'] in observations
        if e['inspected']:e['observations']=observations[e['box']]
    mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Saved {len(readings)} independent readings.')
if __name__=='__main__':save()
