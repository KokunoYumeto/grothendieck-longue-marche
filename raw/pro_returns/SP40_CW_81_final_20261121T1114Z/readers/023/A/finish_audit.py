from pathlib import Path
import json,re,hashlib
out=Path('/workspace/scratch/94548b74fbe0/out/readers/023/A')
r=json.loads((out/'report.json').read_text())
s=(out/'reading.tex').read_text()

def unclutter(line):
    # TeX comments are removed only for structural checking; manuscript source is unchanged.
    return re.split(r'(?<!\\)%',line,1)[0]
clean='\n'.join(unclutter(x) for x in s.splitlines())
errors=[]
stack=[]
for pos,ch in enumerate(clean):
    if ch in '{}':
        backslashes=0;j=pos-1
        while j>=0 and clean[j]=='\\':backslashes+=1;j-=1
        if backslashes%2:continue
        if ch=='{':stack.append(pos)
        elif not stack:errors.append('Unmatched closing brace')
        else:stack.pop()
if stack:errors.append('Unclosed braces: '+str(len(stack)))
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    op,name=m.groups()
    if op=='begin':envs.append(name)
    elif not envs or envs[-1]!=name:errors.append('Environment mismatch '+name)
    else:envs.pop()
if envs:errors.append('Unclosed environments '+str(envs))
if len(re.findall(r'(?<!\\)\$',clean))%2:errors.append('Odd dollar delimiter count')
if clean.count('\\[')!=clean.count('\\]'):errors.append('Unmatched display delimiters')
inside=False
blank_math=[]
for no,line in enumerate(s.splitlines(),1):
    live=unclutter(line)
    if not live.strip() and line.strip()=='':
        if inside:blank_math.append(no)
    for tok in re.findall(r'\\\[|\\\]|(?<!\\)\$',live):
        if tok=='\\[':inside=True
        elif tok=='\\]':inside=False
        else:inside=not inside
if blank_math:errors.append('Blank physical lines within math: '+str(blank_math))
# No undeclared custom macros: this is a source whitelist, not a TeX engine check.
allowed=set('scanpage beta in setminus unsure begin end path fill overline cap varnothing deleted inserted reversemarginpar margin normalmarginpar subset draw node scriptstyle alpha phantom widehat Sigma bigvee bigcup text makebox linewidth rotatebox shortstack illegible exists uline mathrel ne Rightarrow qquad hspace raisebox figure Pi circ operatorname geqslant'.split())
commands=set(re.findall(r'(?<!\\)\\([A-Za-z]+)',clean))
unknown=sorted(commands-allowed)
if unknown:errors.append('Commands absent from whitelist: '+str(unknown))
if '\\newcommand' in clean or '\\renewcommand' in clean:errors.append('Macro definition found')
if '\\cotefile' in clean or '\\mspage' in clean:errors.append('Unexpected cote/manuscript page macro')
if '\\scanpage{23}' not in clean:errors.append('Scan page marker missing')
if '% archive sheet number: 22' not in s:errors.append('Archive comment missing')
for e in r['differences']:
    if e['readers_crop'] and not (out/e['readers_crop']).is_file():errors.append('Missing crop '+e['readers_crop'])
    if e['graphic_ref'] and e['graphic_ref'] not in r['graphics_source_map']:errors.append('Missing graphic '+e['graphic_ref'])
assert len({x['source_id'] for x in r['source_C_doubt_rows']})==16
assert all(x['status'] in ['retained','resolved'] for x in r['source_C_doubt_rows'])
required={
'whole onset alternatives':r'\unsure{qui|ce qui}',
'whole verb alternatives':r'\unsure{prouvera|prouve}',
'whole unfinished alternatives':r'\unsure{precise|précise|provient|precise le|précise le}',
'cancelled word ending':r'\deleted{$E_i$ est \unsure{contenu|contenue}}',
'inserted quantifier and full wording':r'\inserted{$\exists\alpha\in K$ tel que}',
'marginal capital alternatives':r'$(i\in\unsure{I|J})$',
'final word accent alternatives':r'\unsure{Immédiat|Immèdiat|Immediat}',
'final recurrence accent alternatives':r'\unsure{récurrence|rècurrence|recurrence}',
'Pi alternatives':r'\Pi_K^{\unsure{\circ|0}}',
'resolved du plus detached group':r'} du\hspace{2em}',
'resolved family K':r')_{\alpha\in K}$,',
'complete formée word owner':r'{ormée};',
'first head-role qualifier':'% BEGIN A023-S05',
'high cross-run':r'\draw[line width=.45pt] (683,160) -- (729,159);',
'shared main f/cup run':'% G07-FCUP-01',
'actual archived number':'% archive sheet number: 22'}
for name,token in required.items():
    if token not in s:errors.append('Required reading/report anchor absent: '+name)
if 'dans un' in clean:errors.append('Unsupported H tail entered the source')
# Each named graphic is complete and unique. Each visible path/fill belongs to one deepest group.
for gid,g in r['graphics_source_map'].items():
    if s.count('% BEGIN '+gid+'\n')!=1 or s.count('% END '+gid+'\n')!=1:errors.append('Graphic boundary multiplicity '+gid)
    sp=g['source_span']
    if hashlib.sha256(s[sp['start_char']:sp['end_char']].encode()).hexdigest()!=sp['sha256']:errors.append('Stale source span '+gid)
# Complete component spans, without duplicating nested source blocks.
line_offsets=[];offset=0
for line in s.splitlines(keepends=True):line_offsets.append(offset);offset+=len(line)
component_ids=[]
for gid,g in r['graphics_source_map'].items():
    for i,c in enumerate(g['path_and_label_components'],1):
        c['component_id']=gid+'-C'+str(i).zfill(2);component_ids.append(c['component_id'])
        start=line_offsets[c['line']-1]
        depth=0;seen_brace=False;end=None
        # For simple draw/fill commands, semicolon is on the initial line.
        if c['complete_command_on_line']:
            end=start+len(s.splitlines(keepends=True)[c['line']-1])
        else:
            # A parent node encloses the nested qualified graphic; retain its complete span.
            for j in range(start,len(s)):
                ch=s[j]
                if ch=='{' and (j==0 or s[j-1]!='\\'):depth+=1;seen_brace=True
                elif ch=='}' and (j==0 or s[j-1]!='\\'):depth-=1
                if ch==';' and seen_brace and depth==0:end=j+1;break
        assert end is not None,(gid,c['line'])
        c['source_span']={'start_char':start,'end_char':end,'start_utf8_byte':len(s[:start].encode()),'end_utf8_byte':len(s[:end].encode()),'start_line':c['line'],'end_line':s[:end].count('\n')+1}
        c['subpath_note']='One source command may contain several disconnected runs; its exact command text is retained.'
    if gid=='A023-G07':
        draws=[c for c in g['path_and_label_components'] if c['kind']=='draw']
        for c,alias in zip(draws,['G07-RULE-01','G07-RULE-02','G07-FCUP-01','G07-FCUP-02','G07-FCUP-03']):c['physical_component_alias']=alias
r['source_checks']={'scope':'source only','brace_balance':'pass' if not stack else 'fail','environment_balance':'pass' if not envs else 'fail','dollar_delimiters':len(re.findall(r'(?<!\\)\$',clean)),'display_pairs':clean.count('\\['),'blank_physical_lines_inside_math':blank_math,'unknown_commands':unknown,'source_graphic_groups':len(r['graphics_source_map']),'graphic_begin_end_uniqueness':'pass','exact_source_spans_current':'pass','crop_files_exist':'pass','C_source_rows_traceable':16,'complete_candidate_anchors_checked':list(required),'errors':errors,'compiled':False,'rendered':False,'mathematical_proof_checks':False}
if errors:
    print(json.dumps(r['source_checks'],ensure_ascii=False,indent=2));raise SystemExit(1)
r['counts']={'difference_rows':len(r['differences']),'flagged_C_physical_rows':sum(e['diff_C'] for e in r['differences']),'flagged_H_physical_rows':sum(e['diff_H'] for e in r['differences']),'original_C_doubt_rows':16,'original_C_resolved':sum(e['status']=='resolved' for e in r['source_C_doubt_rows']),'original_C_retained':sum(e['status']=='retained' for e in r['source_C_doubt_rows']),'literal_graphic_groups':len(r['graphics_source_map']),'successful_image_views':len(r['image_view_audit']),'planned_deep_crops':len(r['crops']),'repeat_views':0,'failed_unseen_deliveries':0,'inventory_rows':len(r['inventory'])}
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(out/'graphics_map.json').write_text(json.dumps(r['graphics_source_map'],ensure_ascii=False,indent=2)+'\n')
(out/'source_check.json').write_text(json.dumps(r['source_checks'],ensure_ascii=False,indent=2)+'\n')

def esc(t):return str(t).replace('|','\\|').replace('\n',' ')
def candidates(e):
    return '; '.join([e['reading']]+e.get('alternatives',[]))
md=['# Scan 023 — independent reading A','','The sheet presents a proposed argument for the barred-V intersection assertion, a **Lemme**, and a **Corollaire** naming the partition. It ends with the manuscript\'s assertion of immediacy by recurrence on `card K ≥ 0`. These are the writer\'s assertions; this reading supplies no proof check. No explicit authorial uncertainty phrase or handwritten question mark was recovered.','', '## Line-by-line reading audit','','Each physical line is accounted for below. The complete diplomatic source is `reading.tex`; cancelled and inserted states remain in place.','',
'| Region | Reading and state |',
'| --- | --- |',
'| Opening | `Soit maintenant β ∈ I ∖ K, prouvons que l\'on` followed by the qualified small mark (`a` / independent lozenge-point); `V̄ ∩ E_β = ∅.` |',
'| Opening correction | `En effet, V ne` **deleted** `contient`, **inserted** `rencontre`, `aucun E_i (i ∈ I) donc`. The raised replacement and the preceding `ne` retain their placement. |',
'| First union | `E_β ⊂ X ∖ V =` the complete crossed/retraced indexed cup, then the complete hatted Sigma with its qualified I/E/predecessor state, plus and alpha; comma. The tiny left-margin point is retained separately. |',
'| Cancelled lead and continuation | **Deleted, qualified** `donc si`; `je dis que si β ∈ I ∖ K,` **qualified** `on a` `en fait`. A brown fleck is retained above the gap before `en`. |',
'| First display | `E_β ⊂ ⋃ Σ_α^+ (ouvert disjoint de V)`. The Sigma head joins its body; no roof is supplied here. |',
'| Slanted margin | `C\'est trivial,` **deleted unreadable compact item, estimated one word**; `du fait que les E_i (i ∈ I/J) sont disjoints`. Three physical lines, complete. |',
'| Following main line | Whole onset **`qui` / `ce qui`**; whole verb **`prouvera` / `prouve`**; `l\'assertion -- mieux,`. A low point beneath the right part of `assertion` is retained without a punctuation role. |',
'| Upper conclusion | `je dis que ∃ α ∈ K tel que E_β ⊂ Σ_α^+.` `Cela revient` **qualified** `au`. The local Sigma head joins its body. |',
'| Lemma lead | Single-underlined `Lemme`; `Soit K ⊂ I,` **deleted** `tel que les`, **deleted** `et`, `des Σ_α^+ (α ∈ K)` **qualified** `tels` `que`. |',
'| Lemma condition | `α [qualified first relation] β ∈ K, α ≠ β ⇒ Σ_α^+ ∩ Σ_β^+ = ∅.` First relation: **`≠` / deleted `≠` with comma**. Both Sigmas keep their separate short upper runs, indices and plus signs. |',
'| Lemma conclusion, first line | `Soit i ∈ I ∖ K tel que E_i ⊂ ⋃ Σ_α^+, alors`. The Sigma\'s short head is retained above its diagonal. |',
'| Lemma conclusion, correction line | **Deleted** `E_i est` **qualified** `contenu` / `contenue`; **inserted** `∃ α ∈ K tel que`; live `E_i ⊂ Σ_α^+.` The high insertion has no recovered comma after K. The final Sigma\'s short head remains literal. |',
'| Unfinished line | `Cela` **deleted** `signifie que`; the complete live alternatives are **`precise`, `précise`, `provient`, `precise le`, `précise le`**, followed by firm `du`. The two right-hand points remain a qualified graphic cluster. |',
'| Corollary lead | Single-underlined `Corollaire`; `Avec les hyp.` **qualified** `préc.` `sur (Σ_i^α)_{α ∈ K},`. Raised alpha, low i hook and its single dot remain in their written positions; the external K is resolved. |',
'| Corollary body | `la partition Π_K^{circle/zero} est formée des Σ_α^+ (α ∈ K) et de V = X ∖ [indexed cup with high cross-run] Σ̂_α^+.` One complete graphical group owns the two text lines, interrupted left rule, shared f/cup run, both local Sigmas, the point by the first plus, all labels and final period. |',
'| Last two lines | Complete first-word alternatives **`Immédiat`, `Immèdiat`, `Immediat`**; `par`; complete second-word alternatives **`récurrence`, `rècurrence`, `recurrence`**; `sur card K ≥ 0.` The lower comparison run slopes upward right. |',
'| Lower-left numbering | Archive `22`, retained only in the TeX comment; hand undetermined. |',
'', '## The sixteen original C doubt rows','','Source-row identities remain the original table identities. The three resolved rows are R10 (`du`), R12 (`K`), and R16 (presence of the high cross-run). Every other source doubt remains qualified.','', '| C row | Original local scope | Status | Complete selected reading and alternatives |','| --- | --- | --- | --- |']
for row in r['source_C_doubt_rows']:
    md.append('| '+row['source_id']+' | '+esc(row['location'])+' | '+row['status']+' | '+esc('; '.join([row['selected_complete_reading']]+row['selected_complete_alternatives']))+' |')
md+=['','## Additional local qualifications','','These are new qualifications or literal mark records. The meanings of the small marks, their hands and their surface origins remain unestablished.','', '| ID | Place | Complete reading and alternatives |','| --- | --- | --- |']
for e in r['doubts']:
    if not e['source_C_doubt_row_id']:
        md.append('| '+e['id']+' | '+esc(e['location'])+' | '+esc(candidates(e))+' |')
md+=['','## Each local Sigma occurrence','','The recurring short-head role is printed as a doubt at S05. Later occurrences retain their complete local alternatives here even where the source prints the first candidate without another doubt wrapper. A joined head at one occurrence supplies no head reading for another occurrence.','', '| Locus | Complete local reading | Local structure and ownership |','| --- | --- | --- |']
for n in r['notation']:
    if n.get('id','').startswith('S'):
        alternatives=n.get('local_alternatives') or n.get('state_alternatives') or []
        md.append('| '+n['id']+' | '+esc('; '.join([n['reading']]+alternatives))+' | '+esc(n['detail'])+' |')
md+=['','## Collation and source boundaries','','The complete C/H ledger is in `report.json`. It records H\'s words literally, keeps same-primary qualifier-only changes at zero H count, and distinguishes qualified primary differences from established ink corrections. The full `precise` family, `qui/ce qui`, `prouvera/prouve`, cancelled `contenu/contenue`, both complete union/relation states, and every later local head-role alternative remain explicit.','','`graphics_map.json` supplies each complete graphic\'s source boundaries, full-scan origin, declared local rectangle, baseline, attached words and labels, and every literal path/label owner. `A023-G07` owns the complete corollary body: the visible **f** is graphical, its node is **ormée**, and together they supply **formée** exactly once. Its main descending stroke is also the right side of the lower cup. The three nested point groups use base-west anchors with zero node separation; S10 and S11 use explicit scope translations within G07. The geometry is a manual approximation with no metric or rendered validation.','','The viewing record is in `view_audit.json`: one whole image for layout, both halves once, eighteen unique target crops once each, and no failed delivery or repeat view. Context-edge limits are recorded in report provenance. The final source check verifies delimiters, braces, environments, permitted commands, complete candidate anchors, graphic ownership and existing crop references directly from source.']
(out/'reading.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'source_checks':'pass','errors':errors,'counts':r['counts'],'reading_md_written':True},ensure_ascii=False))
