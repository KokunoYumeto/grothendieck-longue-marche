from pathlib import Path
import csv, json, hashlib

root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan053'
readings={
'B01':r'''9''',
'B02':r'''\uline{NB}''',
'B03':r'''groupoïde équivalent à''',
'B04':r'''``\unsure{réconstrui}\unsure{'|''}
% The terminal letters and quote strokes meet the black right scan edge; the incomplete word is not completed here.''',
'B05':r'''\unsure{les|le} \deleted{\unsure{pour plus|par plus}}''',
'B06':r'''(Gr. pond. rep)''',
'B07':r'''\unsure{alors} on aura \deleted{\unsure{par}}''',
'B08':r'''\deleted{\unsure{une} \illegible{1}}\inserted{l'équivalent de}''',
'B09':r'''\deleted{de}''',
'B10':r'''\uline{en plus}''',
'B11':r'''\deleted{déjà} \unsure{i.e.|ici}''',
'B12':r'''avec la''',
'B13':r'''\unsure{évidemment|évident}''',
'B14':r'''\diagram{\begin{tikzcd}[row sep=large]
S_*\mathcal T D_{\mathrm{top}}^\pm\quad\text{(à sous ens. }\inserted{\text{de sommets-repères}}\text{ marqué }R'\text{)}\arrow[d]\\
S_*\mathcal T D_{\mathrm{top}}^\pm
\end{tikzcd}}
% The added de sommets- / repères lies below sous ens., within the parenthetic qualifier.''',
'B15':r'''et \deleted{donc} il nous faudra donc \inserted{décrire} un foncteur
% The top of the raised décrire is clipped; fragments of the following quoted line at the bottom are outside this target line.''',
'B16':r'''\diagram{\begin{tikzcd}[column sep=large]
S_*\mathcal T D_{\mathrm{top}}^\pm\left(\substack{\text{avec}\\\deleted{\unsure{R}}\inserted{R'}\\\text{marqué}}\right)
\arrow[rr,"{\substack{\text{gommage}\\\text{de }\unsure{R'|R_1}}}"]\arrow[r]
&{}&S_*\mathcal T D_{\mathrm{top}}^\pm
\end{tikzcd}}
% Two heads occupy one horizontal shaft. The short mark after R in the label may be a low prime or the index 1; it is not silently resolved.''',
'B17':r'''\deleted{Cela \unsure{s'exprime|s'exprimera}, sur le}''',
'B18':r'''donnant lieu : un diagramme comm. de foncteurs''',
'B19':r'''\diagram{\begin{tikzcd}[row sep=large,column sep=large]
S_*\mathcal T D_{\mathrm{top}}^\pm(\ldots R'\ldots)
\arrow[rr,"{\substack{\text{gommage}\\\text{de }R'}}"]
\arrow[d,"{\substack{\text{oubli du }\deleted{\unsure{R'}}\inserted{\text{marquage}}\\\inserted{R'}}}"']
&&S_*\mathcal T D_{\mathrm{top}}^\pm\arrow[ddl]\\
S_*\mathcal T D_{\mathrm{top}}^{\deleted{\unsure{R|\sharp}}\,\pm}\arrow[dr]&&\\
&\text{(Gra}\deleted{\unsure{\text{ph}}}\text{i pond)}\arrow[r]
&\substack{\text{gr. plus }\unsure{\text{une}|\text{un}}\\\text{pondération}\\\text{par }\unsure{\sigma|\gamma}\text{, mais}\\\text{non par }r\text{,}}
\end{tikzcd}}
% The old R-like mark is overwritten at the beginning of marquage. The old glyph after the lower D and the crossed middle of the bottom target remain uncertain. The side note is reached by a short upward pointer. Its last comma touches the lower boundary.''',
'B20':r'''alors qu'au niveau''',
'B21':r'''52''',
'B22':r'''\margin{\uline{NB} Cette opération\\
a l'air d'un\\
\uline{affaiblissement} de\\
structure --- mais\\
affaiblissement, \unsure{pour|par}\\
une composante\\
donnée de $\Sigma^+$,\\
lorsqu'on ``gomme'' \uline{tous}\\
les repères du contour\\
\unsure{Mais c'est au}\\
plutôt dans le \unsure{sens} d'un\\
\unsure{renforcement} de structure,\\
\unsure{tôt}, \unsure{de|des} \illegible{1}\\
\unsure{des} \inserted{$R'_C=R'\cap C$}, \illegible{1}\\
\unsure{isotopies} par \illegible{1}}
% The lower-left crop edge cuts the beginning of the line ending tôt and subsequent marginal lines. No completion is supplied for the clipped beginnings. Several crossing large main-text letters are excluded.''',
'B23':r'''\margin{\uline{\unsure{affaiblis}}\\
structure ---\\
affaiblissement,\\
une composante\\
donnée de $\Sigma^+$,\\
lorsqu'on ``gomme'' \uline{tous}\\
les repères du contour\\
\unsure{Mais c'est au}\\
plutôt dans le \unsure{sens} d'un\\
\unsure{renforcement} de structure,\\
--- ou plutôt, \unsure{de|des} \illegible{1}\\
\unsure{de} \illegible{1} \unsure{des} \inserted{$R'_C=R'\cap C$}, \illegible{1}\\
\unsure{isotopies} par \illegible{1}\\
\illegible{1} \unsure{de} \illegible{1}\\
\unsure{l'application|l'opération}\\
\unsure{des}\\
\unsure{de}}
% This box clips the heading, the end of the first underlined word, the continuation after structure and after the second affaiblissement, and the beginnings of the lowest marginal lines. The isolated lower fragments belong to the margin, not the slanting main text.''',
'B24':r'''\margin{\uline{\unsure{affaiblis}}\\
structure ---\\
affaiblissement,\\
une composante\\
donnée de $\Sigma^+$,\\
lorsqu'on ``gomme'' \uline{tous}\\
les repères du contour\\
\unsure{Mais c'est au}\\
plutôt dans le \unsure{sens} d'un\\
\unsure{renforcement} de structure,\\
--- ou plutôt, \unsure{de|des} \illegible{1}\\
\unsure{de} \illegible{1} \unsure{des} \inserted{$R'_C=R'\cap C$}, \illegible{1}\\
\unsure{isotopies} par \illegible{1}\\
\inserted{\unsure{catégories|catégorie}}\\
\unsure{l'opération|l'application} \unsure{de} \illegible{1}\\
\deleted{\unsure{\illegible{1}|\illegible{2}}}\\
\unsure{de sous-groupes} \illegible{1}\\
\unsure{les|des} images \unsure{de}\\
\unsure{équivalences} \unsure{de}\\
\unsure{groupoïdes}. Il faudrait \unsure{distinguer}\\
\unsure{les deux} \illegible{1}\\
\uline{\unsure{gommage}} \uline{\unsure{considérées}}}
% The complete R'_C formula is visible, but its insertion attachment and the nearby catégories replacement scope are uncertain. The cancelled run cannot be securely segmented into one versus two words. The upper and lower-left boundaries cut marginal words/lines; the lower underlined phrase is only partly present. Dark diagonal main text and diagram fragments are excluded.''',
'B25':r'''\margin{\unsure{Mais}\\
plutôt \unsure{dans}\\
\unsure{renforcement}\\
--- ou plutôt, \unsure{de|des}\\
\unsure{de} \illegible{1} \unsure{des} \inserted{$R'_C=R'\cap$}\\
\unsure{isotopies} par\\
\inserted{\unsure{catégories|catégorie}}\\
\unsure{l'opération|l'application} \unsure{de} \illegible{1}\\
\deleted{\unsure{\illegible{1}|\illegible{2}}}\\
\unsure{de sous-groupes} \illegible{1}\\
\unsure{les|des} images \unsure{de}\\
sont des \unsure{équivalences} de\\
\unsure{groupoïdes}. Il faudrait \unsure{distinguer}\\
\unsure{bien} les deux\\
\uline{opérations de gommage} \uline{\unsure{considérées}}\\
(qui \unsure{changent} \unsure{le genre}\\
et les \unsure{contours}.}
% Upper/right boundaries clip the ends of the first marginal lines and the final C of the R'_C formula. The margin's final parenthesis has no secure closing stroke. The large main-text letters and diagram are background to this marginal target.''',
}

boxes=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(encoding='utf-8'),delimiter='\t'))
assert list(readings)==[r['box'] for r in boxes]
path=root/'result/second'/f'{page}_second.tsv'
assert not path.exists(), 'Independent reading already exists; do not overwrite a frozen TSV.'
with path.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',lineterminator='\n')
 w.writeheader()
 w.writerows({'box':b,'reading':v} for b,v in readings.items())
parsed=list(csv.DictReader(path.open(encoding='utf-8',newline=''),delimiter='\t'))
assert len(parsed)==25
assert all(set(row)=={'box','reading'} and row['reading'] for row in parsed)
assert [r['box'] for r in parsed]==[r['box'] for r in boxes]
notes={
 'page':page,'reader':'reader_c','phase':'blind independent second reading','frozen':True,
 'source':'source/SP83_C13_148+149_scans/148_scan053.jpg',
 'authorized_inputs':['source/SP83_C13_148+149_scans/148_scan053.jpg','result/second/148_scan053_boxes.tsv','result/scripts/second_reader_guide.md'],
 'prior_readings_seen':False,
 'canonical_crops':[f'result/crops/{page}_second_B{i:02}.png' for i in range(1,26)],
 'canonical_crop_count':25,
 'canonical_crops_all_directly_viewed':True,
 'supplementary_details':[f'result/crops/{page}_second_detail_{n}.png' for n in ['upper','middle','lower','end']],
 'supplementary_detail_source':'Own canonical B24 and B25 only; crop coordinates retained in supplementary generator.',
 'transport_event':'A batched request for B14-B16 returned exec-server transport closed and delivered no images; those three were then viewed individually successfully.',
 'boundary_issues':{
  'B03':'Descender grazes lower edge without preventing the word reading.',
  'B04':'Terminal letters and final raised quote at right scan edge; word recorded as partial rather than completed.',
  'B15':'Top of raised décrire clipped; subsequent quoted line is only fragmentary context at the bottom.',
  'B17':'Descender grazes bottom; cancelled phrase still readable with stated verbal-ending doubt.',
  'B18':'Some lower descender tips clipped; phrase legible.',
  'B19':'Final side-note comma touches/crosses lower edge.',
  'B22':'Note heading present; lower-left oblique boundary clips beginnings of later marginal lines.',
  'B23':'Top clips heading/first underlined word and some upper line ends; lower-left clips subsequent marginal beginnings.',
  'B24':'Top clips upper-note material and lower-left clips late marginal lines. Main-text diagram fragments not imported.',
  'B25':'Upper/right clipping affects opening marginal line ends and final C of the displayed R formula. No secure closing parenthesis for final marginal parenthetical.'},
 'major_independent_doubts':[
  'B04 terminal word and quote clipping',
  'B05 cancelled phrase letters',
  'B07 initial word and cancelled short word',
  'B08 old word under heavy cancellation',
  'B11 i.e./ici',
  'B13 long adverb ending',
  "B16 low prime versus index 1 in arrow label; old R replacement",
  'B17 cancelled verb ending',
  'B19 overwritten label, old symbol after D, crossed bottom-target letters, side-note weight glyph',
  'B22-B25 obscured marginal text and line attachment; uncertain unreadable-word segmentation and insertion/cancellation scope'],
 'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'validation':'Exact columns box/reading; 25 nonempty rows; IDs and order match assigned boxes. No compilation.'}
(root/'result/second'/f'{page}_second_reading_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(path)
print('25 rows; frozen SHA256',notes['sha256'])
