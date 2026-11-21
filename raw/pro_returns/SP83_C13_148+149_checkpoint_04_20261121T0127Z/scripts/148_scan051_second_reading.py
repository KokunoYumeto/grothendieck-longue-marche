from pathlib import Path
import csv,json
root=Path('/workspace/scratch/f28c4f52d3ec')
r={}
r['B01']=r'\unsure{7|4}'
r['B02']=r'''(correspondant : un $C\in\pi_0(\partial X)$), on peut disposer
\inserted{de} \unsure{l'une|l'un} des deux orientations $\omega(a)$ \unsure{--|$=$} dans le cas'''
r['B03']=r'''où $a$ est une arête ordinaire, indiquons que
l'on tient en réserve, pour chaque $a\in A$, un'''
r['B04']=r'''polygone combinatoire $P_a$, dont l'ens des sommets
est $R_a$, et l'ens des arêtes peut se décrire \deleted{comme}'''
r['B05']=r'''$\omega_a\longrightarrow\operatorname{Circ}(R_a)$. Il peut être plus commode
de se donner d'emblée dans la structure,
où la famille des $(R_a)$ serait remplacée par \unsure{une|un}
\deleted{qui serait \illegible{1} un \unsure{ensemble|système}}'''
r['B06']=r'''\uline{autre condition}, \unsure{ie|i.e.} un ensemble \unsure{des|de}
repères $\underline{\vec R}$ (dits ``repères de rigidification''),
avec une opération de'''
r['B07']=r'''$\mathbb D_\infty=\{\sigma_0,\sigma_1\mid\sigma_0^2=\sigma_1^2=1\}$'''
r['B08']=r'''\diagram{\begin{tikzcd}
\mathbb D_\infty \arrow[r,"\varepsilon"] & \{\pm1\}
\end{tikzcd}}'''
r['B09']=r'''sous ens $\underline{\vec R}_{\ell}^{+}\subset\underline{\vec R}\mid\vec A_{\ell}$'''
r['B10']=r'''définissant une orientation \unsure{des|du}
\unsure{contours|contour} \unsure{correspondants|correspondant}.'''
r['B11']=r'''\margin{($\vec A_{\ell}=$ arêtes libres,
correspondant aux
cercles de \unsure{recollements)|recollements}
i.e. \unsure{les|$C_a$} $\in\pi_0(\unsure{\partial}X)$)}'''
r['B12']=r'50'
boxrows=list(csv.DictReader((root/'result/second/148_scan051_boxes.tsv').open(),delimiter='\t'))
assert list(r)==[x['box'] for x in boxrows]
out=root/'result/second/148_scan051_second.tsv'
with out.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['box','reading'])
 for k,v in r.items():w.writerow([k,v])
notes={
 'page':'148_scan051','reader':'reader_c','boxes':12,
 'original_viewed':True,'all_fresh_exact_box_crops_viewed':True,
 'comparison_seen':False,'reading_complete_before_comparison':True,
 'boundary_observations':[
  {'box':'B01','note':'The upper stroke of the overwritten numeral reaches the black top edge of the supplied scan. Its complete former layer cannot be recovered; 7|4 records the visible numeral alternatives without asserting an order of overwriting.'},
  {'box':'B05','note':'The initial q descender of the cancelled relative clause reaches the crop bottom. The main target line and its revision are retained; neighbouring text above and below is only fragmentary context.'},
  {'box':'B06','note':'The tallest strokes of ensemble/des on the upper continuation are clipped by the top boundary, and the p descender in opération meets the lower boundary. The words remain readable, with de/des retained uncertain.'}
 ],
 'unresolved_layer_notes':[
  {'box':'B02','note':'The l\'une/l\'un run is heavily retraced; no independent cancellation is asserted. The mark after omega(a) may be a dash with an extra stroke or an equals sign.'},
  {'box':'B05','note':'One word in the struck clause is physically unreadable; the final struck word is retained as ensemble|système. The live final article remains une|un.'},
  {'box':'B06','note':'The abbreviated ie/i.e. punctuation and de/des are not resolved from grammar.'},
  {'box':'B10','note':'The article and number endings are retained separately as uncertainties instead of being regularized for agreement.'},
  {'box':'B11','note':'The large terminal curve after recollements may be an independent closing parenthesis. The run after i.e. is les-like or C_a-like; no missing C is supplied. The boundary glyph before X is overwritten and retained as an uncertain partial sign.'}
 ],
 'crop_filenames':[f'148_scan051_second_{x["box"]}.png' for x in boxrows]
}
(root/'result/second/148_scan051_second_reading_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
with out.open(newline='') as f:again=list(csv.DictReader(f,delimiter='\t'))
assert len(again)==12 and list(again[0])==['box','reading']
assert [x['box'] for x in again]==[x['box'] for x in boxrows]
print(out)
print('Rows:',len(again),'Columns:',list(again[0]),'Bytes:',out.stat().st_size)
print('Complete before comparison; no comparison has been read.')
