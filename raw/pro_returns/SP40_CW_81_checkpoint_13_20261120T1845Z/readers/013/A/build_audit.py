from pathlib import Path
import json,datetime
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/A')
r=json.loads((R/'report.json').read_text())
r['end_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(R/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
L=['# Scan 013 — independent reader A','',f"Start: {r['start_utc']}. End: {r['end_utc']}.",'',
'## Scope and viewing record','',
'Assigned C text, C doubts, C notes, inventory, metadata, preamble and notation snapshot read. H has status `nothing`; its supplied text is empty. No H collation is claimed. The whole scan was viewed once for layout, then half a once and half b once, followed by crops 01–24 in order, once each. There were no failed unseen image deliveries and no repeat crops.', '',
'Full image: 2365 × 1688 px. Half a: 1242 × 1688 px, full-image origin (0, 0). Half b: 1243 × 1688 px, full-image origin (1122, 0). All report boxes use full-image coordinates, top-left origin. Crop bounds and transformations are in `crops.json`.', '',
'## Line-by-line reading audit','',
'| Physical line / region | Individually read ink | Qualification / placement |','|---|---|---|']
rows=[
('Top heading line','Notes / Notes / Notes / Notes / Notes / Notes','All six words read on the appropriate half.'),
('Numeric heading line','1 / 5 / 7 / 15 / 20 / 23','Individual numeral strokes retained; the long 7 descender is not a new entry.'),
('Below Notes 1','A (1976/77)','Readable under oblique cancellation; fourteen approximation paths preserve merged hatching and lower returns.'),
('Upper left margin','bar over an upward arrow; long brace; ?; downward and upward small arrows','M01–M04 preserve the dark paths, pale parallel traces, curved intervening run and small detached mark above the bar.'),
('Main letter line','A / B / C / D / E / E','Pale A beneath the first dark A resolves as a glyph; its cancelled/live state remains qualified.'),
('Year line','(1976/77) / (1978/79) / (1979/80) / (1980) / (1981) / (1981)','Each date and parenthesis inspected; no number repair or year expansion.'),
('Between first year and first title','two bent arrows','The lower arrow has an extra converging horizontal rule. A nearby pale crescent, slash and dot are separately retained.'),
('Main title line, A','Découverte','Acute over é retained.'),
('A short intermediate line','de la','Ordinary lower-case words retained.'),
('A final title line','Méditation','Singular ending resolved in crop 02. Pale vertical remnants remain graphical, with no supplied extra word.'),
('B main title, three physical lines','Réveil / en / Cascades','C/Ca overlap at the start of Cascades remains doubtful. Interrupted traces adjoining initial R are preserved as graphics.'),
('C main title and translation','Die Eltern / (Les parents)','Capitals and parentheses retained; no extra punctuation.'),
('D main title and translation',"Das Kind / (L'enfant)",'Apostrophe and paired parentheses retained.'),
('E, Notes 20, title and translation','Der Baumeister / (Le Bâtisseur)','Circumflex in Bâtisseur retained.'),
('E, Notes 23, title','Le Bâtisseur','Same visible title read separately in its own column.'),
('Crossed subdivision line','A: (i)?; B: (ii); C: (i\u007cii)?; D: (i); E20: (i\u007cii)?; E23: (iv\u007ciii)?','Every interior judged on local crop strokes. B and D resolve; remaining listed interiors retain uncertainty. Explicit hatch paths preserve each cancellation.'),
('Below first crossed subdivision','pale ? and downward arrow','Question-mark glyph resolves from half a; upper hooked arrow entry retained.'),
('Before B live subdivision','faint curved arrow down and right','L02 preserves the actual curved shaft and head legs.'),
('Live subdivision line','(i) / (ii) / (i) / (i) / (i) / (iv)','All six live entries read. Pale A and D forms resolve as (i), with state qualification. Pale C has a fuller (i) candidate and opening-parenthesis-only alternative.'),
('Secondary title line, A','Envol','Capital E and terminal l retained.'),
('Secondary title line, B','Vers un plus long Voyage','plus resolves from its own p–l–u–s strokes. A detached dark dash below long is separately retained.'),
('Secondary title and translation, C','Bild und Wahrheit / (Image et Réalité)','Word divisions, capital I/R and both acute accents preserved.'),
('Secondary title and translation, D','Der Wolf / (Le Loup)','Capital W/L and paired parentheses retained.'),
('Secondary title and translation, E20','Spiel- und Sucht / (Jeu - et Fringale)','Both written hyphens retained with their local spacing.'),
('Secondary title, E23','Le ``Maître\'\'','Paired double ticks on both sides and circumflex on î retained.'),
('Blank lower area','interrupted trace above first foot; gray dot below Fringale; short dash in last column; local rule darkenings','All are graphics with unassigned character value, role, hand and/or surface origin.'),
('Footer line','M 1976 * / M 1979 / HS I / Sch I / Sch VI / Sch IX','Baseline star, I serif forms and shared upper/lower bars of VI and IX retained; abbreviations unexpanded.'),
('Below first footer','small interrupted pale/dark trace','G03 preserves the separated pieces.'),
('Right boundary, ten positions','E01–E10 local strokes','One-for-one map to C’s ten original subpaths; slopes, branching, gaps and terminal returns differ locally and are drawn explicitly.'),
('Lower right, sideways','12','Archive numeral recorded only as `% archive sheet number: 12` and included in the inventory.')]
for a,b,c in rows:
    L.append('| '+a.replace('|','\\|')+' | '+b.replace('|','\\|')+' | '+c.replace('|','\\|')+' |')
L += ['', '## Every C doubtful-readings source row', '',
'Row identifiers below follow the order of the supplied **Doubtful readings** table. The supplied notation table and abbreviations table are recorded separately and contribute no invented doubt rows. Source row 13 names two physical subloci, which are audited independently.', '',
'| Source row | Local decision | Status of original doubt | Evidence file / location |', '|---|---|---|---|']
for sm in r['C_doubt_source_map']:
    for loc in sm['local_decisions']:
        d=next(x for x in r['differences'] if x['id']==loc['difference_id'])
        val=d['reading'].replace('|','\\|')
        evidence=d['readers_crop'] or 'half a, full box '+str(d['bbox']['xyxy'])
        L.append('| '+sm['source_row_id']+(' / '+d.get('source_sublocus','') if d.get('source_sublocus') else '')+' | `'+val+'` | '+d['C_doubt_status']+' | '+evidence+' |')
L += ['',
'Eight original word/glyph doubts resolve and six local doubts remain. The resolved glyphs of the pale A, pale A (i), and pale D (i) still carry a separate cancelled/live qualification. Pale C retains both extent and state uncertainty. In the TeX, the first pale-state candidate preserves the source deletion annotation using invisible boxing; the second candidate preserves a live reading. The visible graphic receives no invented horizontal strike.', '',
'Five unchanged retained qualifications have `diff_C=false`; their actual path or overlap changes have separate graphical rows. The fuller primary candidate at source row 13b creates a qualified reading change. Each actual physical `change_group` contributes one C change.', '',
'## Graphical additions and exact local mappings','',
'All graphics are direct approximations of visible paths. Gray values distinguish the observed relative darkness. Character value or mathematical meaning is not supplied for detached traces.', '',
'| Report row | Local graphic | Evidence |', '|---|---|---|']
for d in r['differences']:
    if d['id'].startswith('A-G'):
        ev=d['readers_crop'] or 'supplied half image(s); exact box in report'
        if d.get('additional_crops'):ev+='; '+', '.join(d['additional_crops'])
        L.append('| '+d['id']+' | '+d['reading'].replace('|','\\|')+' | '+ev+' |')
L += ['', '### Crop-boundary qualifications', '',
'- Crop 04 includes part of the adjoining pale upper hook at its left boundary. The complete hook and descending arrow were read on half a and are preserved in L01.',
'- Some pale upper continuations meet crop 02’s top boundary. The reading supplies the supported residual paths and no second word. The horizontal line below the title is already R07 and is represented once.',
'- Crop 23 contains the local rule darkening G07 and its right endpoint; the long rule continues through the left boundary and was read on half b.', '',
'## Inventory and remaining uncertainty', '',
'All 48 supplied inventory items are covered. The return adds the archive numeral and explicit path-cluster entries, giving 64 inventory items. The original ten edge components have an individual C-source-path map. Cancellation path counts describe the explicit approximation paths in `reading.tex`, without reconstructing the number or order of original pen movements.', '',
'The remaining word/glyph candidates are C/Ca at Cascades; the A crossed i; C crossed i/ii; E20 crossed i/ii; E23 crossed iv/iii; and the fuller-versus-partial pale form at the third live subdivision. The pale doubled A, A (i), C form and D (i) also retain state qualifications. Detached marks and pale residual paths have local shape-confidence statements and unassigned roles/hand/surface origin in `report.json`.', '',
'The author’s two question-mark glyphs are retained as written. No verbal statement of authorial uncertainty, date heading or page-count description is added.', '',
'## Structural synchronization', '',
'`reading.tex` and `report.json` were checked together for balanced braces, environments and inline math delimiters; allowed macro names; source-doubt coverage; inventory identifiers; path-count consistency; all referenced crop files; absent H rows; and the specific resolved and retained readings. Every actual C change group is unique. `check_events` is empty.', '',
'No OCR, text recognition, PDF text layer, other page, other reader, external source, browser, compiler, renderer, installation or delegated reader was used. No compilation or rendered-layout validation is claimed.', '',
'Files: `reading.tex`, `report.json`, `reading.md`, `crops.json`, `validation.json`; crop PNGs 01–24; scripts `make_crops.py`, `build_return.py`, `build_report.py`, `validate_return.py`, `build_audit.py`.', '']
(R/'reading.md').write_text('\n'.join(L))
assert '13a:' in '\n'.join(L) and '13b:' in '\n'.join(L)
print('Wrote complete reading.md; synchronized end time:',r['end_utc'])
