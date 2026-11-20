from pathlib import Path
import csv,re,json
root=Path(__file__).resolve().parents[2]
src=root/'source/SP41_CW_81_witnesses'
out=root/'runtime_inputs';out.mkdir(exist_ok=True)
page_notes={30: 'C notes: “Le cas où certains des ensembles $U_s,E_a$ pourraient être vides est à examiner avec plus de soin”.', 32: 'C notes: slanted “Version II”, heading “Décompositions n-aires d’un espace topologique”, opening “1.1.”.', 33: 'C notes: “1.2.” above “Deux décompositions binaires”.', 37: 'C notes: “Il reste à voir que l’on n’a pas une inclusion Σ₁⁻ ⊂ Σ₂⁻ ou inclusion inverse”; then “le diagramme (14)” and “ce que l’on a exclu”.', 39: 'C notes: “il faut vérifier la transitivité de cette relation — c’est immédiat”, in the slanted note beside (26).', 41: 'C notes: upper-right title in two lines, “relations d’equiv. / non panachées”; the i in relations, abbreviation and ending were uncertain.', 45: 'C notes: “Structure à étudier” and “Intuition” headings; proposed correspondence from an “ens. bicircularisé avec partition non panachée” to a partition “de degré 2”.', 47: 'C notes: slanted “faux” beside “Montrons dans ce cas … Σ est … connu …”, marking the reconstruction claim at the foot.', 48: 'C notes: NB “il n’est pas vrai que la connaissance de Σ̂* redonne Σ, exemple”, followed by three-chord drawing; four diagonal strokes cancel the attempted statement at the foot.', 49: 'C notes: underlined heading “Segments R saturés”, R added above line.', 52: 'C notes: possible question mark before “les deux extrémités”; internal heading “Partitions non panachées de I”.'}
rows=list(csv.DictReader((src/'page_map.tsv').open(),delimiter='\t'))
for r in rows:
    scan=int(r['our_scan']); folder=r['folder']; d=out/f'scan{scan:03d}';d.mkdir(exist_ok=True)
    c=src/r['codex_file']; h=src/r['hua_file']; text=h.read_text()
    pat=re.compile(r'\\page\{'+r['their_page']+r'\}')
    m=pat.search(text)
    if m:
        end=re.search(r'\\page\{\d+\}',text[m.end():]); ht=text[m.start():m.end()+end.start()] if end else text[m.start():]
    else:
        ht=f"Witness H status: {r['hua_has']}. No page text for archive page {r['their_page']}.\n"
    (d/'H.tex').write_text(ht)
    doubts=(src/f'codex/{folder}/{folder}_doubts.md').read_text()
    selected=['# Witness C page-specific doubt and notation rows\n']+[x for x in doubts.splitlines() if re.match(r'\|\s*0*'+str(scan)+r'(?:\s*\||\s*,)',x)]
    selected+=['\nFolder-wide C notes are held by the main reader; no other-page notes are passed to this fresh reader.']
    if scan in page_notes: selected += ['\n# Page-specific C notes\n', page_notes[scan]]
    (d/'C_context.md').write_text('\n'.join(selected))
    paths={'scan':scan,'folder':folder,'their_page':int(r['their_page']),'hua_has':r['hua_has'],'C':str(c),'H':str(d/'H.tex'),'C_context':str(d/'C_context.md'),'preamble':str(src/f'codex/{folder}/PREAMBLE.tex'),'H_style':str(src/'hua/transcripts/preamble/grothendieck.sty'),'H_drawings':str(src/'hua/transcripts/81/drawings'),'images':[str(root/f'source/SP41_CW_81_scans/{folder}_81_scan{scan:03d}{s}.jpg') for s in ['', '_a','_b']]}
    (d/'packet.json').write_text(json.dumps(paths,ensure_ascii=False,indent=2))
print('Prepared',len(rows),'page packets outside deliverables.')
