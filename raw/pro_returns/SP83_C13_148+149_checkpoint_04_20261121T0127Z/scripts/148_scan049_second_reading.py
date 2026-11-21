from pathlib import Path
import csv, json
root=Path('/workspace/scratch/f28c4f52d3ec')
readings={}
readings['B01']=r'5)'
readings['B02']=r'Cette opération en somme'
readings['B03']=r'''$X$ \deleted{\unsure{est}} connexe $\Longleftrightarrow \Gamma MD(X,\widetilde\Sigma,R)$ connexe'''
readings['B04']=r'''$\pi_0(X)\simeq\pi_0\bigl(\Gamma MD(X,\widetilde\Sigma,R)\bigr)$'''
old_margin_ink=r'''\begin{tikzpicture}[x=.11cm,y=.11cm,baseline=-.2ex,line width=.5pt]
\draw (0,.2) .. controls (1,.7) and (1.1,1.1) .. (1.7,.8) -- (1.1,.2) -- (2.4,.1);
\draw (2.1,1.6) .. controls (3,2.1) and (3.6,1.8) .. (3.1,1.1) .. controls (4,.9) and (3.8,.3) .. (2.8,.2);
\draw (4,1.1) -- (4.1,.1) -- (5,.7) -- (5.5,.3);
\draw (-.2,-.1) -- (5.9,1.1);
\draw (.4,-.2) -- (4.8,.8);
\end{tikzpicture}'''
readings['B05']=r'''\margin{donner la formule pour le genre d'une
$\alpha\in\pi_0(X)\simeq\pi_0(\Gamma)$ en termes
de la \unsure{pondération} --- plus \unsure{généralement}
le \uline{genre total} est donné par
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=base east] at (0,0) {$g=\displaystyle\sum_{s\in S}g_s+$};
\node[anchor=base west] (c) at (0,0) {$c(\Gamma)$};
\node[anchor=north,align=left,text width=5cm] (note) at (-1.6,-.85) {l'indice de\\connexion\\du graphe\\
$=$ \unsure{\inserted{$\operatorname{rg}$}}\unsure{''' + old_margin_ink + r'''}
\unsure{$H_1(\Gamma)$|$H^1(\Gamma)$}};
\draw[->] (.35,-.08) .. controls (.15,-.55) and (-.4,-.55) .. (-1.2,-.78);
\end{tikzpicture}}}'''
readings['B06']=r'''${}^{\circ})$ Cas de $S_*\mathcal T_{\mathrm{top}}^{\pm}$
\deleted{\unsure{$S\mathcal T_{\mathrm{top}}$}}
-- ici $\Sigma=\phi,\ \widetilde\Sigma=\partial X$.'''
readings['B07']=r'''Cela correspond au cas des graphes MD \deleted{qui} où
\inserted{\unsure{toutes} les arêtes sont extérieures, i.e.}
tous les sommets sont isolés (sauf arêtes libres)
\deleted{\unsure{Il}}\inserted{Ce graphe} est donc déterminé par'''
readings['B08']=r'''\diagram{\begin{tikzcd}[column sep=large,row sep=large]
A\quad(\simeq\unsure{\vec A|\bar A}=\unsure{\vec A^{*}|\bar A^{*}|\vec A^{+}})
\arrow[r,"{\unsure{r|\rho}}"] \arrow[d] & \mathbb N \\
S \arrow[r,"\gamma"] & \mathbb N
\end{tikzcd}}'''
readings['B09']=r'''Le cas de $\mathcal T_{\mathrm{top}}^{\pm}$ correspond : celui où $\rho=0$,
donc la \unsure{situation} est donnée par'''
readings['B10']=r'''\diagram{\begin{tikzcd}[column sep=large,row sep=large]
A=A_0 \arrow[d] & \\
S \arrow[r,"\gamma"] & \mathbb N
\end{tikzcd}}. '''
readings['B11']=r'''\margin{\figure{\begin{tikzpicture}[x=.8cm,y=.8cm,line width=.55pt]
\fill (.7,4.6) circle (.06);
\draw (.7,4.6) .. controls (.45,5) and (.45,5.5) .. (.2,5.9);
\draw (.7,4.6) .. controls (1,5.15) and (1.3,5.7) .. (1.65,5.85);
\draw (.7,4.6) .. controls (1.05,4.95) and (1.6,5.15) .. (2,5.3);
\node[anchor=north east] at (.64,4.58) {$g_0$};
\fill (1.1,3.25) circle (.06);
\node[anchor=north east] at (1.02,3.24) {$g_1$};
\fill (2.5,3.83) circle (.06);
\node[anchor=west] at (2.63,3.94) {$\unsure{g_2|g_{\sim}}$};
\fill (1.6,1.82) circle (.07);
\fill[white] (1.58,1.79) circle (.018);
\draw (1.6,1.82) .. controls (1.85,2.4) and (1.8,2.8) .. (1.84,3.3);
\draw (1.6,1.82) .. controls (2.1,2.5) and (2.55,2.72) .. (2.95,2.9);
\draw (1.6,1.82) .. controls (2.12,2.1) and (2.7,2.05) .. (3.06,1.85);
\draw (1.6,1.82) .. controls (2.1,1.48) and (2.3,1.08) .. (2.33,.55);
\node[anchor=north east] at (1.42,1.48) {$g_3$};
\fill (.22,-.78) circle (.07);
\draw (.22,-.78) .. controls (.4,-.3) and (.16,.2) .. (-.1,.45);
\node[anchor=north] at (.38,-.94) {$\unsure{g_4|g_a}$};
\draw[->] (3.6,6.02) .. controls (4.15,5.55) and (3.82,4.05) .. (4.08,3.1)
.. controls (4.12,2.96) and (4.18,2.96) .. (4.24,3.0)
.. controls (3.88,2.14) and (4.12,.35) .. (3.02,-1.25)
.. controls (2.75,-1.5) and (2.1,-1.45) .. (1.72,-1.62);
\end{tikzpicture}}}'''
readings['B12']=r'''Le cas d'une structure connexe $(\operatorname{Card}.\,S=1)$
\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm,baseline=0]
\node[anchor=base] at (0,.25) {i.e. $S=\{s\}$};
\draw (-1.35,.48) .. controls (-1.5,-.08) and (-1.1,-.08) .. (0,-.08)
.. controls (.8,-.1) and (1.4,-.12) .. (1.4,.13);
\draw[->] (.02,-.65) .. controls (-.1,-.35) and (-.03,-.2) .. (.02,-.08);
\end{tikzpicture}}}
\deleted{\unsure{type $(g,\nu)$ d'une surface}}
est \deleted{\unsure{bien spécifié|bien défini}}
\unsure{\inserted{caractérisé}|\deleted{caractérisé}}
\deleted{par le genre}\inserted{par la donnée des}
deux entiers $(g,\nu)$ $(g=\text{genre},\ \nu=\text{nb de trous})$
$g=\gamma(s),\quad\nu=\operatorname{card}A$'''
readings['B13']=r'48'
boxrows=list(csv.DictReader((root/'result/second/148_scan049_boxes.tsv').open(),delimiter='\t'))
assert list(readings)==[r['box'] for r in boxrows]
out=root/'result/second/148_scan049_second.tsv'
with out.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['box','reading'])
 for bid,reading in readings.items(): w.writerow([bid,reading])
notes={
 'page':'148_scan049',
 'reader':'reader_c',
 'boxes':13,
 'original_viewed':True,
 'all_fresh_exact_box_crops_viewed':True,
 'comparison_seen':False,
 'reading_complete_before_comparison':True,
 'boundary_observations':[
  {'box':'B02','note':'Lower end of the p descender in opération meets the lower boundary; the word is readable.'},
  {'box':'B07','note':'The first letter of the inserted toutes is close to or slightly clipped by the left boundary; the whole word is retained with uncertainty. Other crossing marginal/main-text fragments at the edge are not imported into this target.'},
  {'box':'B11','note':'The descender of the lower g label meets the bottom boundary; the visible index is retained as 4|a, independently of the sequence.'},
  {'box':'B12','note':'The final g in the lowest equation has its descender clipped by the lower boundary; the equation itself remains readable.'}
 ],
 'unresolved_layer_notes':[
  {'box':'B05','note':'The terminal rank/homology annotation contains overwritten strokes. A doubtful outline records the crossed cluster, rg is tentatively treated as a raised addition, and the height of 1 on H remains uncertain. Main-text letters crossing the marginal baseline were excluded.'},
  {'box':'B06','note':'The initial circle and parenthesis are visible; no preceding numeral is supplied. The old cancelled category symbol remains uncertain.'},
  {'box':'B08','note':'Bars versus arrows above A, the final upper mark, and r versus rho are retained as glyph uncertainties without deciding from the domain.'},
  {'box':'B12','note':'The old type phrase and bien... wording remain uncertain. The relative deletion/insertion state of caractérisé is unresolved; both states are recorded.'}
 ],
 'crop_filenames':[f'148_scan049_second_{r["box"]}.png' for r in boxrows]
}
(root/'result/second/148_scan049_second_reading_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
with out.open(newline='') as f:
 rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==13 and list(rows[0])==['box','reading']
assert [r['box'] for r in rows]==[r['box'] for r in boxrows]
print(out)
print('Rows:',len(rows),'Columns:',list(rows[0]))
print('Bytes:',out.stat().st_size)
print('Independent readings are complete; no comparison has been read.')
