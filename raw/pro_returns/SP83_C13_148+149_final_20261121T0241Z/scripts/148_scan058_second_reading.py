from pathlib import Path
import csv,json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan058'
readings={
'B01':r'''14''',
'B02':r'''\deleted{\unsure{des|de}}''',
'B03':r'''partie \inserted{ouv. et f.}''',
'B04':r'''$\Sigma'\subset\Sigma_0$''',
'B05':r'''$A'$ de $A_0$''',
'B06':r'''\deleted{\unsure{sol.}}\inserted{\unsure{liés|libres}}\unsure{)|\deleted{)}},
% The cancellation meets the bottom of the closing parenthesis. The raised replacement and the old abbreviated word are not fully secure.''',
'B07':r'''cette-fois ci''',
'B08':r'''de ``gommer\unsure{''|'} i.e de contracter en\\
un point, mais de ``découper'', ce''',
'B09':r'''Le \uline{marquage suit}.
\deleted{\unsure{Les|Je} \illegible{1}, \unsure{pour} \unsure{un|une} \unsure{à}}
% The partly visible Mais at the right and the upper fragments belong to adjacent live context. The cancelled line has one physically unreadable word, with the other uncertain groups retained in place.''',
'B10':r'''\unsure{considérée} \inserted{en $C$} ---
% The addition stands above the baseline, with a curved insertion leader descending after the word and before the dash.''',
'B11':r'''où \deleted{il y a lieu de \unsure{marquer|marqué}}\inserted{$C$ est effectivement marqué i.e. $C\cap R\neq\varnothing$}\\
i.e. $C\subset\overset{\unsure{\mathrm{cc}}}{\Sigma}^{+}$ --- \unsure{sauf|\deleted{sauf}} à peu de chose
% The replacement occupies the line above the cancelled phrase. The small mark above Sigma has two c-like runs and is retained as uncertain cc; no normalization from another page is used. The short word after the dash has heavy crossing strokes, so its cancellation state remains open.''',
'B12':r'''\unsure{une|un}. fois, \deleted{\unsure{)}}
% The looped right-hand cancellation is read provisionally as an overwritten closing parenthesis; it is not treated as a secure numeral.''',
'B13':r'''\unsure{en|un} \unsure{près|pres})
% The p descender is clipped at the lower edge; the two high detached dots do not securely settle the grave accent.''',
'B14':r'''peut se \unsure{récréer|récrire},''',
'B15':r'''à l'aide du''',
'B16':r'''produit de cette opération''',
'B17':r'''marqué,''',
'B18':r'''57''',
}
boxes=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(encoding='utf-8'),delimiter='\t'))
assert list(readings)==[r['box'] for r in boxes]
out=root/'result/second'/f'{page}_second.tsv'
assert not out.exists(),'Independent TSV already exists; do not overwrite a frozen reading.'
with out.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',lineterminator='\n')
 w.writeheader();w.writerows({'box':box,'reading':reading} for box,reading in readings.items())
rows=list(csv.DictReader(out.open(encoding='utf-8',newline=''),delimiter='\t'))
assert len(rows)==18
assert [r['box'] for r in rows]==[r['box'] for r in boxes]
assert all(set(r)=={'box','reading'} and r['reading'] for r in rows)
for row in rows:
 text='\n'.join(line.split('%')[0] for line in row['reading'].splitlines())
 depth=0
 for ch in text:
  if ch=='{':depth+=1
  if ch=='}':depth-=1
  assert depth>=0,(row['box'],'unbalanced braces')
 assert depth==0,(row['box'],'unbalanced braces')
manifest_path=root/'result/second'/f'{page}_second_crop_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
assert len(manifest['crops'])==18
for crop in manifest['crops']:
 crop['viewed']=True
manifest['all_canonical_crops_directly_viewed']=True
manifest['additional_crops']=[]
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
notes={
 'page':page,'reader':'reader_c','phase':'blind independent second reading','frozen':True,
 'authorized_inputs':['source/SP83_C13_148+149_scans/148_scan058.jpg','result/second/148_scan058_boxes.tsv','result/scripts/second_reader_guide.md'],
 'original_directly_viewed':True,'canonical_crop_count':18,'all_canonical_crops_directly_viewed':True,
 'canonical_crops':[f'result/crops/{page}_second_B{i:02}.png' for i in range(1,19)],
 'supplementary_crops':[],'first_or_comparison_material_seen':False,
 'boundary_issues':{
  'B09':'Adjacent main-text word Mais is clipped at the right; it is context, not part of the cancelled target. Upper adjoining-line fragments are likewise excluded.',
  'B10':'Upper neighbouring-line words are cut by the box; the raised en C, its leader, the baseline word and following dash are present.',
  'B11':'Top contains clipped fragments of the preceding line, excluded from the target. Both complete displayed formulas within the target are recorded.',
  'B13':'The descender of the p-like initial in près reaches the lower boundary. The target words and closing parenthesis are otherwise visible.',
  'B14':'Upper descender fragment and lower neighbouring-letter tips are context, excluded.',
  'B16':'Upper descender fragments and lower neighbouring-line tips are context, excluded.',
  'B17':'A fragment of the following line touches the lower edge, excluded; marqué and its comma are complete.'},
 'independent_reading_doubts':{
  'B02':'Cancelled des/de, heavily overwritten within one word unit.',
  'B06':'Old abbreviated sol. is doubtful; upper liés/libres and the cancellation extent at the parenthesis remain uncertain.',
  'B08':'First closing raised quote may be a single rather than paired stroke; no separate point is seen after i.e.',
  'B09':'Cancelled line: first word, one unreadable word, and subsequent short words remain uncertain. Upper marquage suit is underlined, not cancelled.',
  'B10':'Baseline considérée reading is provisional; en C and insertion leader are visible.',
  'B11':'Old final word marquer/marqué; small cc-like mark above Sigma; short word sauf and its cancellation state. Numeric/source signs are recorded from the crop, without notation lookup.',
  'B12':'First short word un/une plus a visible point; looped cancellation provisionally hides a closing parenthesis, not a secure numeral.',
  'B13':'Initial en/un and accent of près; no wording supplied from syntax.',
  'B14':'Verb after peut se has low compressed runs; récréer/récrire retained as competing readings.'},
 'clear_numeric_readings':{'B01':'14','B04':'Sigma subscript 0','B05':'A subscript 0','B18':'57'},
 'validation':'Exact columns box/reading, 18 nonempty rows in supplied order; balanced braces in transcription fields; no OCR, research, comparison or TeX compilation.',
 'sha256':hashlib.sha256(out.read_bytes()).hexdigest()
}
(root/'result/second'/f'{page}_second_reading_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(out)
print('18 rows; all 18 canonical crops directly viewed; frozen SHA256',notes['sha256'])
