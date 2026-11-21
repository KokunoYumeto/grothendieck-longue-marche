from pathlib import Path
import json,re,hashlib,sys
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/C')
r=json.loads((R/'report.json').read_text())
tex=(R/'reading.tex').read_text()
# Source checks only: this script neither invokes nor emulates a TeX compiler.
clean='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in tex.splitlines())
stack=[]
for n,ch in enumerate(clean):
 if ch not in '{}':continue
 slashes=0;j=n-1
 while j>=0 and clean[j]=='\\':slashes+=1;j-=1
 if slashes%2:continue
 if ch=='{':stack.append(n)
 else:
  assert stack,('unmatched closing brace',n)
  stack.pop()
assert not stack,('unclosed braces',stack)
env=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 if m.group(1)=='begin':env.append(m.group(2))
 else:assert env and env.pop()==m.group(2),('environment mismatch',m.group(0))
assert not env
math=[]
for m in re.finditer(r'\\([()\[\]])',clean):
 tok=m.group(1)
 if tok in '([':math.append(tok)
 else:assert math and math.pop()=={')':'(',']':'['}[tok]
assert not math
allowed={'scanpage','figure','resizebox','linewidth','begin','end','path','draw','node','fill','unsure','deleted','mathrm','mathord','overline','underline','color','fontsize','selectfont'}
macros=set(re.findall(r'\\([A-Za-z]+)',clean))
assert macros<=allowed,sorted(macros-allowed)
assert tex.count(r'\scanpage{13}')==1
assert r'\cotefile' not in tex and r'\mspage' not in tex
assert '% archive sheet number: 12' in tex
assert all(d['H'] is None and d['diff_H'] is False for d in r['differences'])
assert r['check_events']==[]
assert len(r['source_doubt_rows'])==13
assert sum(v['local_locus_count'] for v in r['source_doubt_rows'])==14
assert r['source_doubt_rows'][12]['decisions']==['C013.d13a','C013.d13b']
assert all(d['diff_C'] for d in r['differences'] if d['C_doubt_status']=='resolved')
assert all(not d['diff_C'] for d in r['differences'] if d['C_doubt_status']=='retained')
for c in r['crops']:
 assert (R/c['path']).is_file() and c['viewed']
 x0,y0,x1,y1=c['bbox'];assert 0<=x0<x1<=2365 and 0<=y0<y1<=1688
for d in r['differences']:
 if d['readers_crop']:assert (R/d['readers_crop']).is_file()
for d in r['doubts']:
 if d.get('crop'):assert (R/d['crop']).is_file()
required=['Notes','(1976/77)','(1978/79)','(1979/80)','(1980)','(1981)','Découverte','de la','Méditation','Réveil','en','Cascades','Die Eltern','(Les parents)','Das Kind',"(L'enfant)",'Der Baumeister','(Le Bâtisseur)','Le Bâtisseur','Envol','Vers un plus long Voyage','Bild und Wahrheit','(Image et Réalité)','Der Wolf','(Le Loup)','Spiel- und Sucht','(Jeu - et Fringale)',"Le ``Maître''",'M 1976','M 1979','HS','Sch']
assert all(v in tex for v in required)
assert r'\unsure{Méditation|Méditations}' not in tex
assert r'\unsure{plus}' not in tex
assert r'\unsure{?}' not in tex
assert r'\deleted{\unsure{\mathrm A}}' in tex
assert r'\deleted{\unsure{C|Ca}}Cascades' in tex
assert r'\unsure{\deleted{(\mathrm i)}|(\mathrm i)}' in tex
assert r'\unsure{\deleted{(}|(}' in tex
for g in ['G02','G15a','G16b','G16c','G16d','G12','G23','G24','G25','G26','G27','G28a','G28b','G28c','G29','GhalfB']:
 assert '% '+g+':' in tex,g
edge=tex.split('% Gedge1--Gedge10:',1)[1].split('% G12:',1)[0]
assert len(re.findall(r'^\\draw',edge,re.M))==10
r['end_utc']=sys.argv[1]
r['notes']['structural_validation']='Passed direct source checks of braces, environment nesting, explicit math delimiters, permitted macro names, 13 source rows / 14 local doubt loci, source/report candidate synchronization, all 30 crop references, 10 right-edge path commands, and H-null flags. No compiler, renderer, OCR, text recognition, external source, or mathematical check was used.'
r['counts']={'source_doubt_rows':13,'source_doubt_local_loci':14,'resolved_source_local_loci':7,'retained_source_local_loci':7,'report_decision_rows':len(r['differences']),'diff_C_rows':sum(d['diff_C'] for d in r['differences']),'diff_H_rows':0,'crops':30,'inventory_items':len(r['inventory'])}
# Make the retained glyph and new state qualification visibly traceable as one physical cluster.
r['notes']['physical_locus_counting']='C013.d13a records retained glyph uncertainty without a change; C013.d15 records the additional state alternative at that same physical group. C013.d11 and C013.d13b each combine their glyph resolution with local state qualification. Graphical component identifiers map to explicit paths; source-row totals remain independent of graphical change totals.'
(R/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
md=[]
md += ['# Independent reading audit — scan 013, reader C','',f"Start: **{r['start_utc']}**. Completion: **{r['end_utc']}**.",'','## Scope and viewing record','',
 'Read the assigned brief v11, PREAMBLE.tex, notation snapshot, metadata, C.tex, empty H.tex, C doubts, C notes, and C inventory. All output and crop scripts are confined to this reader directory. The clock was read while loading the brief/preamble/notation, before packet and image reading. No other page or reader was inspected.',
 '', 'Viewed the whole scan once for layout, then half a once and half b once for the complete reading. Viewed 30 distinct local crops once each. The first attempted c10 display aborted before dispatch; its existing file was then displayed successfully once. No decided image was reopened. No OCR, text recognition, PDF text layer, browser, external source, delegation, compiler, renderer, or installation was used.',
 '', 'Full image: 2365 × 1688. Half a: 1242 × 1688, origin (0, 0). Half b: 1243 × 1688, origin (1122, 0). The coordinate boxes in the crop table and report use the upper-left origin of the original full scan.',
 '', 'H is absent: metadata gives `hua_has=nothing`, and H.tex contains no text. Every report H field is null, and every diff_H flag is false. No H collation is supplied.',
 '', '## Line-by-line reading audit','', '| Physical band | Readable ink / recorded content | Qualification or decision |','|---|---|---|']
lines=[
 ('Top heading line','Notes in all six columns.','Six separately formed headings checked on the halves.'),
 ('Number line','1; 5; 7; 15; 20; 23.','Numbers retained in their own columns; no page-count interpretation supplied.'),
 ('Early first-column entry','Cancelled A (1976/77).','Readable beneath diagonal hatching on half a; deletion retained.'),
 ('Upper left margin','Barred upward arrow, long brace, question mark, opposed arrows.','Connected paths, inner loop, parallel pale runs and middle join reproduced; detached pale point preserved separately as G15a.'),
 ('Large capital line','A; B; C; D; E; E.','Dark first A stands over a pale A candidate. Both final E forms have three arms.'),
 ('Date line','(1976/77); (1978/79); (1979/80); (1980); (1981); (1981).','Parentheses and slashes retained; first date repeated in the cancelled early entry.'),
 ('Between first date/title','Two bent arrows, upper upward head and lower downward head.','The lower horizontal run is doubled. Three nearby detached components retained as G16b–d.'),
 ('Main title line 1','Découverte; Réveil; Die Eltern; Das Kind; Der Baumeister; Le Bâtisseur.','Acute and circumflex marks retained from local ink. Detached points near Baumeister are recorded graphically without a diacritic assignment.'),
 ('Main title line 2','de la; en; (Les parents); (L’enfant); (Le Bâtisseur).','Literal apostrophe and parentheses retained. The empty final translation cell remains empty.'),
 ('Main title continuation','Méditation; overwritten C/Ca followed by Cascades.','Méditation resolved with singular ending. C/Ca predecessor remains doubtful.'),
 ('Crossed subdivision line','A: doubtful (i); B: (ii); C: doubtful (i)/(ii); D: (i); E20: doubtful (i)/(ii); E23: doubtful (iv)/(iii).','B and D recovered from their own surviving stems/dots. The other cancelled forms remain explicitly qualified.'),
 ('Intervening pale marks','? with curved-top downward arrow at first column; pale descending arrow before second column.','Question resolved. Arrow paths retain their observed curves and placement.'),
 ('Live subdivision line','(i); (ii); (i); (i); (i); (iv).','Pale lower first-column group, extra third-column opening curve, and displaced upper D group are separately preserved. Their deletion/live states remain explicit alternatives.'),
 ('Lower title line','Envol; Vers un plus long Voyage; Bild und Wahrheit; Der Wolf; Spiel- und Sucht; Le “Maître”.','plus resolved. Lexical hyphen after Spiel and paired quotation ticks retained. Detached dot beneath long retained separately.'),
 ('Lower translation line','(Image et Réalité); (Le Loup); (Jeu - et Fringale).','Accents, capitals, parentheses and the separate hyphen in Jeu - et retained.'),
 ('Foot reference line','M 1976 *; M 1979; HS I; Sch I; Sch VI; Sch IX.','Star at baseline. First I forms have serifs; VI and IX carry common top and bottom bars.'),
 ('Right edge','Ten surviving short stroke components.','All checked individually; component 5 has a downturned terminal and component 10 has a bent thick lower end. No off-sheet continuation supplied.'),
 ('Lower blank areas','Small interrupted first-column marks, pale oblique cluster, spot below Fringale, short dash below last title.','Shapes preserved with local uncertainty; role, hand and surface origin remain unresolved.'),
 ('Lower right archive entry','Sideways 12.','Archive number is inventoried and appears only in the required TeX comment.')]
for a,b,c in lines:md.append('| '+a+' | '+b+' | '+c+' |')
md += ['', '## C doubt source-row map','', 'Thirteen source rows name fourteen local loci. The final source row is split below; its two physical loci are not silently merged. The notation and abbreviation sections supplied context and were not counted as doubts. Seven local glyph readings are resolved and seven retained. New state qualifications are tracked separately from the original glyph doubts.', '', '| Source row | Physical locus | Decision | Crop |','|---|---|---|---|']
for d in r['differences']:
 if not d.get('source_doubt_row'):continue
 row=str(d['source_doubt_row'])+('a' if d['id']=='C013.d13a' else 'b' if d['id']=='C013.d13b' else '')
 desc={'C013.d01':'Retain A candidate under dark A.','C013.d02':'Resolve Méditation.','C013.d03':'Retain C / Ca.','C013.d04':'Retain crossed (i) doubt.','C013.d05':'Resolve crossed (ii) from its two surviving local stems/feet.','C013.d06':'Retain crossed (i) / (ii).','C013.d07':'Resolve crossed (i) from its dot and short upright.','C013.d08':'Retain crossed (i) / (ii).','C013.d09':'Retain crossed (iv) / (iii).','C013.d10':'Resolve ? from the hook, shaft and detached point.','C013.d11':'Resolve displaced glyph (i); preserve deleted/overwritten versus live state. Upper group is above lower dark (i).','C013.d12':'Resolve plus.','C013.d13a':'Retain pale (i) glyph doubt; state alternative recorded in C013.d15.','C013.d13b':'Resolve opening curve as (; preserve deleted/overwritten versus live/retraced state.'}[d['id']]
 md.append('| '+row+' | '+d['location']+' | '+desc+' | '+d['readers_crop']+' |')
md += ['', '## Additional graphical decisions','', 'The complete transcription uses a positioned TikZ table within the figure macro. This preserves the left marginal cluster, the table entries, the cancellation/deletion annotations, ten edge components, and the supported detached shapes. Each new graphical component has an inventory entry or a local component entry. No words are supplied for residual marks.', '', '| Report ID | Local addition or refinement | Qualification |','|---|---|---|']
for d in r['differences']:
 if d['id'].startswith('C013.g') or d['id'].startswith('C013.edge'):
  qualification='Path shape '+d['confidence']+' confidence.'
  if d['id'].startswith('C013.g') and d['id'] not in ['C013.g10','C013.g30']:qualification+=' Detached/faint component role, hand or surface origin unresolved.'
  md.append('| '+d['id']+' | '+d['reading']+' | '+qualification+' |')
md += ['', 'The four pale runs in G02 have low overall interpretive confidence. Their actual short path components are listed in the JSON record. G15a and G16b–d remain independent marks within their larger local graphical clusters. The two upper Baumeister points and the small point left of its B have separate rows and inventory identities. The lower title dash was settled on half b at full-scan box (2248, 1338, 2275, 1350); half-b local coordinates are (1126, 1338, 1153, 1350).',
 '', '## Crop audit and exact coordinates','', 'Boxes are `(left, top, right, bottom)` in the full 2365 × 1688 scan. All rotations are 0°. Every listed crop was displayed. All transforms use PIL LANCZOS enlargement, autocontrast, and mild sharpening; no text recognition was run.', '', '| File | Full-scan box | Local outcome |','|---|---|---|']
verdicts=[
 'Pale A candidate retained; dark A readable.', 'Méditation resolved; pale residual runs separately preserved.', 'C/Ca predecessor remains open.', 'Crossed (i) remains doubtful.', 'Crossed (ii) resolved from local surviving forms.', 'Crossed (i)/(ii) retained.', 'Crossed (i) resolved from local dot/stem.', 'Crossed (i)/(ii) retained.', 'Crossed (iv)/(iii) retained.', '? resolved; curved-top downward arrow drawn.', 'Upper (i) glyph resolved; deleted/live state open.', 'plus resolved; detached point under long retained.', 'Pale lower (i) retained; state separately open.', 'Extra opening parenthesis resolved; state open.', 'Connected brace/arrow/loop/retraces and opposed-arrow join drawn; detached upper point retained.', 'Double lower rule and three detached local marks drawn.', 'Edge pieces 1 and 2 retained.', 'Edge pieces 3 and 4 retained.', 'Edge pieces 5 and 6 retained; fifth downturned end added.', 'Edge pieces 7 and 8 retained.', 'Edge piece 9 retained as detached short slant.', 'Edge piece 10 bent terminal retained; archive 12 confirmed.', 'Interrupted narrow mark preserved; no character.', 'Interrupted slanted trace preserved; no character.', 'Oblique fragment cluster preserved with low interpretation confidence.', 'Curved upright and faint rule continuation preserved.', 'Irregular spot preserved; no character.', 'Baumeister spelling checked; three separate nearby points inventoried.', 'Découverte acute confirmed; small separate point below retained. Context overlaps c16 without re-adjudicating the arrow.', 'Pale long curved arrow shaft and darker terminal retained.'
]
for c,v in zip(r['crops'],verdicts):md.append('| '+c['path']+' | '+str(tuple(c['bbox']))+' | '+v+' |')
md += ['', '## Final source/report checks','', r['notes']['structural_validation'], '',
 f"Final record: {r['counts']['report_decision_rows']} decision/difference rows, {r['counts']['diff_C_rows']} rows flagged as changes to C, no H changes, 65 inventory items, and 30 viewed crops. These report-row counts preserve separate source-doubt and graphical identities; C013.d13a and C013.d15 refer to one physical lower first-column group.",
 '', 'The author’s own visible uncertainty consists of the two question marks described above. No mathematical theorem, repaired statement, conditional result, finite computation, or map has been introduced. `check_events` is empty.',
 '', 'Primary deliverables: `reading.tex`, `report.json`, and this `reading.md`. Crop coordinates and display status also appear in `crops_manifest.json`; local scripts and `structural_checks.json` document the transformations and final source validation.']
(R/'reading.md').write_text('\n'.join(md)+'\n')
checks={'braces':'passed','environment_nesting':'passed','explicit_math_delimiters':'passed','macros':sorted(macros),'all_30_crops_exist_and_viewed':True,'source_doubt_rows':13,'source_doubt_local_loci':14,'right_edge_path_commands':10,'inventory_items':65,'H_fields_null_and_flags_false':True,'check_events_empty':True,'compilation_or_rendering_performed':False,'end_utc':r['end_utc'],'sha256':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['reading.tex','report.json','reading.md','crops_manifest.json']}}
(R/'structural_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'complete','counts':r['counts'],'end_utc':r['end_utc'],'validation':'structural source checks passed; no compiler or renderer'},ensure_ascii=False))
