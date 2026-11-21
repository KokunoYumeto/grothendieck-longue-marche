from pathlib import Path
import csv,json,hashlib,datetime,os
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan061'
rows=[]
def add(box,reading): rows.append({'box':box,'reading':reading.strip()})
add('B01',r'''17
Récapitulation des opérations élémentaires''')
add('B02',r'''\inserted{$0^\circ)$ Somme disjointe
\unsure{\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline]
\draw (0,0)..controls (0,18) and (0,28)..(4,29)..controls (9,27) and (12,21)..(15,25)..controls (17,29) and (20,15)..(30,0)..controls (32,8) and (30,21)..(35,27);
\draw (-14,36)--(38,36);
\end{tikzpicture}}}
\uline{\unsure{de copies|d'opérations}}, \unsure{i.e.}}''')
add('B03',r'''\unsure{$1^\circ)$|$4^\circ)$} \uline{gommage} des repères se trouvant sur un
cercle \inserted{\unsure{$C_0$|le}} de recollement \inserted{$C_a$}, ou
\deleted{\unsure{sur} un cercle}''')
add('B04',r'''de découpage $\Longleftrightarrow$ suppression \unsure{de la|d'une} \deleted{partie}\inserted{$R_a$}
$(a\in A)\Longleftrightarrow$ modification de $r_a$ en le
\deleted{de $R$ se trouvant sur une partie}
remplaçant par $0$ en $a$.''')
add('B05',r'''\margin{\uline{fortement}\\\uline{\unsure{irréversible|réversible}}\\$r_a\neq0$}''')
add('B06',r'''remplaçant par $0$ en $a$.
\inserted{\uline{gommage} \uline{partiel uniforme : d'exposant $d_a\unsure{\mathrel{:\!|}|\mid}r_a$}}
$2^\circ)$ Restriction des \deleted{scalaires}\inserted{groupes de $R_a$} de
$\mathbb Z_a/r_a\mathbb Z$ à un $\mathbb Z_a/r'_a\mathbb Z_a$, où
$r'_a\mid r_a$\quad\raisebox{-0.5ex}{\unsure{2|?}}
(pour $a$ fixé, il y a $r_a/r'_a=d_a$ choix
possibles, si on suppose $d_a>1$ i.e. $r'_a\neq r_a$).''')
add('B07',r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,align=left,inner sep=0] at (0,0) {\uline{renforcement} des\\\uline{structures} \unsure{\uline{faibles}|\deleted{\uline{faibles}}}\\$r_a\unsure{\neq|\geq}0$\\\deleted{\illegible{1}}\\$r'_a\unsure{\mid|\nmid|\neq}r_a$ et $r'_a\neq r_a$\\i.e. $d_a=\frac{r_a}{r'_a}\neq1$};
\draw (-.1,.2)--(5.5,.2)..controls (5.8,.1) and (5.9,-.4)..(6,-1.4)..controls (6.1,-1.7) and (6.1,-1.9)..(6.2,-2.1);
\end{tikzpicture}}}''')
add('B08',r'''\unsure{$3^\circ)$}
\deleted{Extension des}
\inserted{\uline{\unsure{$-$gommage|dégommage} uniforme} \uline{d'exposant} $d_a>1$}''')
add('B09',r'''-- i.e. extension du groupe de $R_a$ de
$\mathbb Z_a/r_a\mathbb Z_a$ à $\mathbb Z/d r_a\mathbb Z$,''')
add('B10',r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,align=left,inner sep=0] at (0,0) {\uline{affaiblissement des}\\structures \uline{faibles}\\$r_a\neq0$};
\draw (.3,.25)--(5.5,.15)..controls (5.8,.1) and (5.9,-.8)..(6,-1.2);
\end{tikzpicture}}}''')
add('B11',r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[draw,ellipse,inner sep=2pt] at (0,0) {$4^\circ$};
\node[anchor=west,align=left] at (.6,0) {gommage du cercle de découpage $C_a$\\$(a\in A_0)$};
\node[draw,ellipse,inner sep=2pt] at (0,-1.15) {$5^\circ$};
\node[anchor=west] at (.6,-1.15) {bouchage du trou $C_a$ $(a\in\unsure{A_{0,l}|A_{0,2}})$};
\draw (-.6,.8)..controls (-.7,.4) and (-.7,-.2)..(-.8,-.35)..controls (-.7,-.45) and (-.65,-1.1)..(-.6,-1.7);
\end{tikzpicture}}''')
add('B12',r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,align=left,inner sep=0] at (0,0) {fortement\\\unsure{irréversible|réversible}};
\draw (.8,.3)--(4.4,.3);
\draw (3.9,-.1)..controls (3.5,-.45) and (3.7,-.65)..(3.85,-.75)..controls (3.6,-.85) and (3.55,-1.1)..(3.45,-1.35);
\draw (-.15,-1.45)--(3.1,-1.45);
\end{tikzpicture}}}''')
add('B13',r'''\unsure{$6^\circ)$|\textcircled{$6^\circ$}} Découpage le long de $C_a$ $(a\in A_0)$\textsuperscript{*}''')
add('B14',r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,align=left,inner sep=0] at (0,0) {fortement \unsure{irréversible}\\si $r_a=0$, \deleted{faiblement}\\réversible \unsure{à|en} \unsure{condition|\illegible{1}}\\si $r_a\geq1$.};
\draw (.2,.25)--(5.6,.25);
\draw (-.2,-2.05)--(5.3,-2.05);
\end{tikzpicture}}}''')
add('B15',r'''$7^\circ)$ Recollement le long de $C_a$, $C_{a'}$
\inserted{$r_a=r_{a'}$}
\unsure{$(a,a'\in A_l,\ a\neq a')$|$(c,c'\in A_l,\ a\neq a')$}, via un élément de
$R_a\wedge R_{a'}$.''')
add('B16',r'''\margin{$r_a=r_{a'}\unsure{\geq|>}1$\\réversible \unsure{à|en} \unsure{condition|\illegible{1}}}''')
add('B17',r'''\margin{-- * Il faudrait \inserted{peut-être} distinguer
$6^\circ)$ en deux, suivant que
$r_a=0$ ou $r_a\neq0$ (ou
\unsure{\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline]
\draw (3,8)..controls (10,5) and (28,4)..(39,4);
\draw (0,13)..controls (2,17) and (6,22)..(9,20)..controls (12,14) and (17,17)..(23,17)--(43,17);
\end{tikzpicture}}}
exclure le cas $r_a=0$?)}''')
add('B18',r'''\margin{60}''')
assigned=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(encoding='utf-8'),delimiter='\t'))
assert [r['box'] for r in rows]==[r['box'] for r in assigned]
assert len(rows)==18
for r in rows:
 assert r['reading'].strip()
 level=0
 for c in r['reading']:
  if c=='{':level+=1
  elif c=='}':level-=1
  assert level>=0,(r['box'],'negative brace depth')
 assert level==0,(r['box'],'unbalanced braces')
 assert r['reading'].count('$')%2==0,(r['box'],'unpaired math delimiter')
out=root/'result/second'/f'{page}_second.tsv'
with out.open('x',encoding='utf-8',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',lineterminator='\n')
 writer.writeheader();writer.writerows(rows)
back=list(csv.DictReader(out.open(encoding='utf-8',newline=''),delimiter='\t'))
assert back==rows
checksum=hashlib.sha256(out.read_bytes()).hexdigest()
notes={
 'page':page,'reader':'reader_c','phase':'blind independent second reading','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'allowed_inputs':['source/SP83_C13_148+149_scans/148_scan061.jpg','result/second/148_scan061_boxes.tsv','result/scripts/second_reader_guide.md'],
 'source_only':True,'first_reading_or_comparison_opened':False,'original_view_count':1,'canonical_crops_directly_viewed':18,'source_only_details_directly_viewed':13,
 'tsv':str(out.relative_to(root)),'tsv_sha256':checksum,'frozen_before_comparison':True,
 'crop_paths':[f'result/crops/{page}_second_B{i:02}.png' for i in range(1,19)],
 'detail_paths':[f'result/crops/{page}_second_D{i:02}.png' for i in range(1,14)],
 'transport_events':['An initial combined B08/B09 display returned only Output exceeded the available model context and was truncated; no images were delivered. B08 and B09 were subsequently each successfully viewed separately.','The first B18 display attempt returned exec runtime replaced with no image. The subsequent separate call displayed B18 successfully.'],
 'boundary_notes':[
  {'boxes':['B01','B02','B03','B04','B06','B08','B09','B11','B13','B15'],'note':'Wide target boxes include cut fragments of adjacent lines. Only complete target units and intentionally overlapping complete wording were transcribed; clipped neighboring context was not reconstructed.'},
  {'boxes':['B05','B07','B10','B12','B14','B16'],'note':'Rotated marginal crops preserve their exact prescribed original rectangles. Larger main-text letters/labels crossing the marginal baseline were excluded from marginal readings.'},
  {'box':'B03','note':'Lower edge includes the raised R_a belonging to the following replacement; that replacement is transcribed in B04. Tiny raised unit between cercle and de is independently uncertain C_0 versus le, and its attachment is not asserted beyond raised position.'},
  {'box':'B08','note':'The item-number area is overlapped/clipped at the left; 3-degree-close-parenthesis remains tentative. The small prefix before gommage is retained as a visible dash with a degommage alternative, not silently expanded.'},
  {'box':'B11','note':'The left grouping-brace stroke reaches the crop boundaries. The drawing reproduces the visible segment, without claiming a complete closed grouping or extending it to unseen material.'},
  {'box':'B12','note':'The right bracket and bottom neighboring marginal fragments meet the crop edges; the two target words are present. Initial letters of irreversible/reversible remain uncertain.'},
  {'box':'B13','note':'The label overlaps marginal strokes near the left edge; digit 6 and degree mark are clear, enclosure state is uncertain.'},
  {'box':'B14','note':'The end of the first marginal line is close to the right original boundary and crossed by main-label strokes. The target adjective remains doubtful; the main 6-degree label is excluded from the marginal text.'},
  {'box':'B15','note':'The lower edge contains only the upper portion of the footnote. Its complete independent reading is in B17, not completed by inference in B15.'},
  {'box':'B17','note':'The note meets the right scan border but the final question mark and closing parenthesis are visible. The unclassified overwritten two-stroke mark before exclure is drawn, without guessing a mathematical or lexical identity.'},
  {'box':'B18','note':'Folio 60 is complete; scan-bottom dark edge is background, not a cancellation.'}
 ],
 'remaining_uncertainties':[
  {'box':'B02','note':'The underlined run after Somme disjointe is not securely segmented. A separate raised/angled cluster is drawn; de copies and d\'operations are low-confidence possibilities for the following underlined wording. Final i.e. is tentative.'},
  {'box':'B03','note':'Overworked first item label 1/4; tiny raised C_0/le; initial cancelled sur is tentative. The cancelled un cercle and live ou are separable.'},
  {'box':'B04','note':'de la versus d\'une remains open. The deleted line de R se trouvant sur une partie was read from ink.'},
  {'box':'B05','note':'Initial letters of irreversible versus reversible are compressed.'},
  {'box':'B06','note':'Colon-like dots plus a vertical bar in the heading relation retained literally as :| with a simple-divisibility alternative. The detached low 2/question-mark-shaped glyph after r_a is preserved without mathematical attachment. Small d subscripts are read a, with only moderate glyph confidence.'},
  {'box':'B07','note':'Possible crossing/cancellation on faibles; overwritten r_a relation; unread cancelled word; overwritten divisibility/inequality relation. No mathematical argument was used to settle these.'},
  {'box':'B08','note':'Visible dash-like prefix versus degommage segmentation; label 3 tentative at crop edge.'},
  {'box':'B11','note':'Last subscript of the second A is cursive l versus 2; 0 and the separating comma are preserved.'},
  {'box':'B12','note':'Initial i/rr segmentation remains uncertain.'},
  {'box':'B13','note':'Only the enclosing stroke state is uncertain, not the number 6.'},
  {'box':'B14','note':'End of irreversible near crop boundary; compressed phrase after reversible remains low-confidence a/en condition or one unread word. Deleted faiblement and both numeric conditions are retained.'},
  {'box':'B15','note':'Tiny paired variables are a,a-prime versus c,c-prime. A_l subscript has a distinct cursive loop. Product glyph is a visible wedge with no crossing; final punctuation is one dot.'},
  {'box':'B16','note':'Heavily overwritten greater/greater-equal relation; compressed following phrase remains unresolved, with a/en condition only tentative.'},
  {'box':'B17','note':'Unclassified final-line mark is drawn rather than read as a word or relation. Inserted peut-etre is placed between faudrait and distinguer, with its leader understood only as placement evidence.'}
 ],
 'validation':{'exact_columns':['box','reading'],'exact_order':True,'rows':18,'nonempty_readings':True,'brace_balance':True,'paired_dollar_delimiters':True,'csv_roundtrip':True,'ocr_used':False,'web_used':False,'tex_compiled':False},
 'status':'Frozen independent reading; no comparison or adjudication performed.'
}
(root/'result/second'/f'{page}_second_reading_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_path=root/'result/second'/f'{page}_second_crop_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
for c in manifest['crops']:c['viewed']=True
manifest['independent_reading_complete']=True
manifest['independent_tsv_sha256']=checksum
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
details_path=root/'result/second'/f'{page}_second_detail_manifest.json'
details=json.loads(details_path.read_text(encoding='utf-8'))
for d in details:d['viewed']=True
details_path.write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
os.chmod(out,0o444)
print(json.dumps({'page':page,'rows':len(rows),'sha256':checksum,'tsv':str(out),'canonical_crops':18,'detail_crops':13,'frozen':True},ensure_ascii=False))
