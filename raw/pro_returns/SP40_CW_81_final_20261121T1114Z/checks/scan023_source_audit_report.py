"""Emit only the authorized frozen audit, never any selected source or record."""
from pathlib import Path
import hashlib
import json
import runpy

ROOT = Path('/workspace/scratch/94548b74fbe0')
P = ROOT / 'out/checks'
ns = runpy.run_path(str(P/'scan023_source_audit_checks.py'))
validation = ns['run_checks']()
assert not validation['mechanical_failures'], validation['mechanical_failures']
r = json.loads((P/'scan023_record_draft.json').read_text())
m = json.loads((P/'scan023_final_source_map.json').read_text())
draft = (P/'scan023_final_draft.tex').read_text()
walk = ns['walk']
get = ns['pointer_get']
sha = ns['digest']

def compact_ref(ref):
    return {k:v for k,v in ref.items() if k != 'literal'}

def authority(n):
    d = r['decisions'][n-1]
    return {
        'selected_source_attachments_pointer':f'/decisions/{n-1}/source_attachments',
        'selected_source_attachments':[compact_ref(x) for x in d['source_attachments']],
        'journal_sources':[compact_ref(x['journal']) for x in d['root_crop_evidence']],
        'selected_group_ids':d['selected_group_ids'],
        'qualification_pointer':f'/decisions/{n-1}/qualification',
    }

MIRROR_SKIP = {'provenance','reader_source_details','source_attachments','root_crop_evidence','root_viewing_scope','complete_witness_contexts','witness_source_references','selected_source','root_crop_audit','root_count_authorization','root_scope_authorization','source_map_reference','selected_source_map_reference','source_assembly_release','expansion_source','source','root_journal_sources'}

def mirrors(before, origin):
    equal, embedded = [], []
    for pointer, value in walk(r, skip=MIRROR_SKIP):
        if pointer == origin or not isinstance(value,str) or not before:
            continue
        # Own-reader source and candidate fields are independently preserved.
        if '/readers/' in pointer and '/readers/' not in origin:
            continue
        if value == before:
            equal.append(pointer)
        elif before in value and ('/evidence' in pointer or '/reason' in pointer or '/selected_reading' in pointer or '/first_words_or_objects' in pointer):
            embedded.append(pointer)
    return {'exact_current_value_mirrors':equal, 'embedded_current_reading_mentions':embedded}

def target(pointer, after, why, auth=None):
    before=get(r,pointer)
    assert before != after, pointer
    result={'pointer':pointer,'before':before,'proposed_after':after,'defect':why,
            'current_mirror_pointers':mirrors(before,pointer)}
    if auth is not None: result['authority']=auth
    return result

findings=[]
alt_replacements={
    30:[r'Complete $\Sigma_\alpha^+$ with its detached returned upper run assigned an independent-run role; the body and alpha remain continuous.'],
    33:[r'Complete $\Sigma_\alpha^+$ with its detached short upper run assigned an independent-run role; the complete plus, alpha and terminal point remain present.',r'Complete $\Sigma_\alpha^+$ with its detached short head, both plus arms and complete alpha accompanied by an independent point; point attachment, role, hand and surface origin remain undetermined.'],
    39:[r'Complete $\Sigma_\alpha^+$ with its short separate upper bar assigned an independent-run role; both plus arms and continuous alpha remain present.'],
    51:[r'Complete literal $\Pi_K^0$ with its long head, attached left stem and low return, separately starting right stem, hooked lower K and raised ring with entry hook.'],
    54:[r'Complete $\Sigma_{\deleted{i}\alpha}^+$ with both literal points retained: the upper point above-right of plus and the lower point above-left of alpha; predecessor/cancellation chronology remains unresolved.'],
    56:[r'Complete $\bigcup_{\alpha\in K}$ with its definite high cross stopping before the right stem; the cross operation/attachment role remains unassigned.'],
    57:[r'Complete $\widehat{\Sigma}_\alpha^+$ with its firm separate roof, detached short intermediate run assigned an independent-run role, angular body, two-armed plus and continuous alpha.'],
}
alt_targets=[]
for n, values in alt_replacements.items():
    for index,value in enumerate(values):
        alt_targets.append(target(f'/decisions/{n-1}/alternatives/{index}',value,
            'The current alternative uses an anaphoric or partial glyph/mark description; the complete decorated candidate and retained local scope must be explicit.',authority(n)))
findings.append({'id':'SA023-01','title':'Incomplete complete-candidate alternatives','targets':alt_targets,
                 'bounded_repair':'Replace only these current alternatives and their exact current mirrors. Preserve reader-specific original candidates, order and raw provenance.'})

family_candidates=[r'$(\Sigma_i^\alpha)_{\alpha\in K}$,',r'$(\Sigma_i^\alpha)_{\alpha\in I}$,',r'$(\Sigma_i^\alpha)_{\alpha\in\deleted{I}K}$,',r'$(\Sigma_i^\alpha)_{\alpha\in\deleted{K}I}$,']
family_scope=('Both parentheses, the lower hook and its one point, raised alpha, closing-parenthesis/external-alpha junction, in/index cluster and final comma remain present once. '
              'Detached-head role remains locally qualified. The hook/point retains i-like hook with its point versus foot retrace accompanied by an independent point. '
              'The one point has separately undetermined role, hand, attachment and surface origin; the four external-index states and predecessor/cancellation chronology remain unresolved.')
s07_scope=(r'Complete $\Sigma_\alpha^+$ retains detached-head versus independent-upper-run role. The complete $\Sigma_\alpha^+$ also retains alpha-terminal-point versus complete alpha accompanied by an independent point; that point has separately undetermined attachment, role, hand and surface origin.')
s08_scope=(r'Complete $\Sigma_\alpha^+$ with the separate short bar as its head versus complete $\Sigma_\alpha^+$ with that bar assigned an independent-upper-run role; the plus and continuous alpha remain present, followed by one separate full stop.')
s10_scope=(r'Complete $\Sigma_\alpha^+$ versus complete $\Sigma_{\deleted{i}\alpha}^+$; both literal points remain once in either state and predecessor/cancellation chronology remains unresolved. '
           'The lower point above-left of alpha and upper point above-right of plus each have their own undetermined hand, attachment, role and surface-origin scope. '
           'The short additional plus run retains retrace/unassigned-run role and separately undetermined local hand/origin. The main glyph remains in his hand.')
s11_scope=(r'Complete $\widehat{\Sigma}_\alpha^+$ retains its firm roof, detached short head, angular body, two-armed plus and continuous alpha; the lower short run retains head versus independent-run role.')

final_after={}
candidate_ids=[2,6,7,9,25,28,30,31,33,34,36,39,48,49,50,51,54,56,57]
for n in candidate_ids:
    d=r['decisions'][n-1]
    candidates=[d['final']]+alt_replacements.get(n,d['alternatives'])
    if n in [48,49,50]: candidates=family_candidates
    scope=d['qualification']
    if n in [48,49,50]: scope=family_scope
    if n==33: scope=s07_scope
    if n==54: scope=s10_scope
    if n==57: scope=s11_scope
    final_after[n]='Qualified complete candidates (editorial separators; primary first): '+ ' | '.join(candidates)+ ' [Editorial local scope: '+scope+']'
for n in [5,10,18,27,43,44,60]:
    d=r['decisions'][n-1]
    final_after[n]=d['final']+' [Editorial local scope: '+d['qualification']+']'
final_after[22]=r'\uline{Lemme} Soit $K\subset I$, \deleted{tel que les} \deleted{et} des $\Sigma_\alpha^+$ $(\alpha\in K)$ tels que'+r' [Editorial local candidates: complete $\Sigma_\alpha^+$ with a possible pale head/body bridge versus complete angular $\Sigma_\alpha^+$ with a separate short upper run; continuity/head role remains unresolved.]'
final_after[29]=(r'Qualified complete condition candidates (editorial separators): $,\,\alpha\ne\beta\Rightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing.$ | $,\,\alpha\ne\beta\Rightarrow\Sigma_\alpha^+\cap\Sigma_\beta^\top=\varnothing.$ '
                r'[Editorial local scope: S05 is complete $\Sigma_\alpha^+$ with a detached returned head/independent upper-run role and continuous shared alpha. S06 retains its joined head/shared beta and complete plus/top candidates; no extra upper arm is supplied.]')
final_after[32]=r'Soit $i\in I\setminus K$ tel que $E_i\subset\bigcup\Sigma_\alpha^+$, alors'+' [Editorial local scope: '+s07_scope+']'
final_after[37]=(r'Qualified complete raised-clause candidates (editorial separators; primary first): \inserted{$\exists\alpha\in K$ tel que} | \inserted{$\exists\alpha\in K$ tel \deleted{que}} '
                 '[Editorial local scope: open gap after K, no manuscript comma; raised placement and que cancellation target remain under physical parent U023-34.]')
final_after[38]=r'$E_i\subset\Sigma_\alpha^+$.'+' [Editorial local scope: '+s08_scope+']'
final_after[52]=r['decisions'][51]['final']+' [Editorial local scope: the final indexed cup retains its definite high cross, interrupted upper-left stalk and shared f junction; cross operation/attachment role remains unassigned. '+s10_scope+' '+s11_scope+']'
final_after[55]=r['decisions'][54]['final']+' [Editorial local scope: the indexed cup retains the definite high cross; its operation/attachment role remains unassigned. The shared f/cup continuation is represented once.]'
final_targets=[]
for n, after in sorted(final_after.items()):
    final_targets.append(target(f'/decisions/{n-1}/final',after,
        'The emitted Final value does not itself contain all selected complete candidates and/or the locally unresolved role, hand, attachment or state scope. Evidence and separate alternatives retain supporting material, but the builder does not add alternatives to Final.',authority(n)))
findings.append({'id':'SA023-02','title':'Public Final values require complete selected candidates and local scopes','targets':final_targets,
    'emission_evidence':{'path':'out/scripts/build_records.py','sha256':sha((ROOT/'out/scripts/build_records.py').read_text()),'lines':[39,54],
       'behavior':'Changes and collation receive decision final verbatim. Qualification is appended to evidence; decision alternatives are not appended to final. Doubt rows print their own reading and alternatives.'},
    'bounded_repair':'Use the explicit current values below or an exactly equivalent source-supported public wording that retains all listed candidates and local scopes. Synchronize current mirrors and containing-frame component descriptions. No selected TeX, donor, count, confidence, parent or approval change.'})

margin=r"\shortstack[l]{C'est trivial, \deleted{\illegible{1}}\\du fait que les $E_i$ $(i\in\unsure{I|J})$\\sont disjoints}"
assert margin in draft
findings.append({'id':'SA023-03','title':'Marginal-line separators must preserve the source line breaks','targets':[
    target('/decisions/12/final',margin,'Two added semicolons currently stand between the three source lines. The selected literal shortstack has line breaks, without those manuscript semicolons.',authority(13))],
    'bounded_repair':'Print the exact shortstack or explicit editorial line-break notation. Synchronize current mirrors. The selected TeX remains unchanged.'})

reader_targets=[]
reader_issues=[(22,'C','The full Lemme/Soit introduction, its cancellations, S04 and following family/word scope are absent from the public string; it contains only group declarations.'),
    (45,'A','The actual Corollaire/Avec les hyp./qualified préc./sur lead is omitted from the public reader string.'),
    (45,'B','The actual Corollaire/Avec les hyp./firm préc./sur lead is omitted from the public reader string.'),
    (45,'C','The actual Corollaire/Avec les hyp./firm préc./sur lead is omitted from the public reader string.'),
    (50,'A','The public string describes only the local glyph and expressly leaves the surrounding parentheses/external family index outside; it does not show the complete family with A\'s own external K reading.'),
    (52,'C','The public string gives local group declarations and ellipses for the containing corollary; the complete two-line own sentence is absent.')]
for n,who,why in reader_issues:
    pointer=f'/decisions/{n-1}/readers/{who}'
    refs=r['decisions'][n-1]['reader_source_details'][who]['actual_complete_source_spans']
    exact='\n'.join(ref['literal'] for ref in refs)
    after='Actual own complete TeX for this recorded locus:\n'+exact+'\n\n'+get(r,pointer)
    item=target(pointer,after,why,{'own_complete_source_pointer':f'/decisions/{n-1}/reader_source_details/{who}/actual_complete_source_spans','exact_own_source_refs':[compact_ref(x) for x in refs]})
    reader_targets.append(item)
findings.append({'id':'SA023-04','title':'Six public own-reader fields omit complete recorded scope','targets':reader_targets,
    'bounded_repair':'Prepend the already attached exact own-source excerpt and retain the existing raw-report material. Use each reader\'s own source only. Synchronize public reader mirrors; preserve reader_source_details and provenance.'})

# Every proposed witness excerpt is checked against its actual complete witness
# span. No source glyph, spelling, cancellation, whitespace or punctuation is
# silently rewritten here.
cup_c=r'\mathop{\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\bigcup}}\limits_{\alpha\in K}'
note_h=r'\note{la réunion est écrite avec le signe de réunion disjointe}'
scope_specs={
 (6,'C'):[r'\mathop{\unsure{\deleted{\bigvee}\bigcup|\bigcup}}\limits_{\alpha\in K}'],
 (6,'H'):['\\bigcup_{\\alpha\\in\n  K}'],
 (11,'C'):[r'E_\beta'],(11,'H'):[r'E_{\beta}'],
 (14,'C'):[r'\deleted{\illegible{1}}'],
 (16,'H'):['qui'],(21,'H'):['du'],
 (25,'C'):[r'\Sigma_\alpha^+'],(25,'H'):[r'\Sigma_{\alpha}^{+}'],
 (28,'C'):[r'\alpha\mathrel{\unsure{\ne|\deleted{\ne}{,}}}\beta\in K'],(28,'H'):[r'\alpha\neq\beta\in K'],
 (30,'C'):[r'\Sigma_\alpha^+'],(30,'H'):[r'\Sigma_{\alpha}^{+}'],
 (31,'C'):[r'\Sigma_\beta^+'],(31,'H'):[r'\Sigma_{\beta}^{+}'],
 (33,'C'):[r'\Sigma_\alpha^+'],(33,'H'):[r'\Sigma_{\alpha}^{+}'],
 (34,'C'):[r'\deleted{$E_i$ est \unsure{contenu|contenue}} \inserted{$\exists\alpha\in K$ tel que}'],
 (34,'H'):[r'\struck{$E_{i}$ est contenu dans un} $\exists\,\alpha\in K$, tel que'],
 (37,'C'):[r'\inserted{$\exists\alpha\in K$ tel que}'],(37,'H'):[r'$\exists\,\alpha\in K$, tel que'],
 (38,'C'):[r'$E_i\subset\Sigma_\alpha^+$.'],(38,'H'):[r'$E_{i}\subset\Sigma_{\alpha}^{+}$.'],
 (39,'C'):[r'\Sigma_\alpha^+'],(39,'H'):[r'\Sigma_{\alpha}^{+}'],
 (45,'C'):[r'\uline{Corollaire} Avec les hyp. \unsure{préc.} sur'],(45,'H'):[r'\emph{Corollaire} Avec les hyp.\ précédentes sur'],
 (48,'C'):[r'$(\Sigma_i^\alpha)_{\alpha\in\unsure{K|I}}$,'],(48,'H'):[r'$(\Sigma_{i}^{\alpha})_{\alpha\in K}$,'],
 (49,'C'):[r'$(\Sigma_i^\alpha)_{\alpha\in\unsure{K|I}}$,'],(49,'H'):[r'$(\Sigma_{i}^{\alpha})_{\alpha\in K}$,'],
 (50,'C'):[r'$(\Sigma_i^\alpha)_{\alpha\in\unsure{K|I}}$,'],(50,'H'):[r'$(\Sigma_{i}^{\alpha})_{\alpha\in K}$,'],
 (53,'C'):[r'\begin{tabular}{@{}|p{.96\linewidth}@{}}'],
 (54,'C'):[r'\Sigma_\alpha^+'],(54,'H'):[r'\Sigma_{\alpha}^{+}'],
 (55,'C'):['formée',cup_c],(55,'H'):['formée',r'\bigcup_{\alpha\in K}',note_h],
 (56,'C'):[cup_c],(56,'H'):[r'\bigcup_{\alpha\in K}',note_h],
 (57,'C'):[r'\widehat{\Sigma}_\alpha^+'],(57,'H'):[r'\widehat{\Sigma}_{\alpha}^{+}'],
}
witness_targets=[]
for (n,who), excerpts in sorted(scope_specs.items()):
    pointer=f'/decisions/{n-1}/{who}'
    context=r['decisions'][n-1]['complete_witness_contexts'][who]
    exact_refs=[]
    for excerpt in excerpts:
        offset=context['literal'].rfind(excerpt) if n in [21,38,39] else context['literal'].find(excerpt)
        assert offset>=0,(n,who,excerpt)
        start=context['char_start_zero_based']+offset
        exact_refs.append({'path':context['path'],'sha256_utf8':context['sha256_utf8'],'char_start_zero_based':start,'char_end_exclusive':start+len(excerpt),'span_sha256_utf8':sha(excerpt),'literal':excerpt})
    after=excerpts[0] if len(excerpts)==1 else 'Editorially separated exact local witness excerpts: '+' | '.join(excerpts)
    why='The current C/H cell spans unrelated paragraph or display material, obscuring the local complete comparison. Preserve the complete surrounding witness source in its existing provenance.'
    if n in [48,49,50]:why='The complete family source has a final comma, which is omitted from the local public witness reading.'
    if n==53:after='Left rule encoded by the exact column-format excerpt '+excerpts[0]+' [editorial description; full tabular context remains attached].'
    witness_targets.append(target(pointer,after,why,{'complete_context_pointer':f'/decisions/{n-1}/complete_witness_contexts/{who}','exact_local_source_refs':exact_refs}))
cancelled_h=r'\struck{$E_{i}$ est contenu dans un}'
ctx=r['decisions'][34]['complete_witness_contexts']['H']
assert cancelled_h in ctx['literal']
witness_targets.append(target('/decisions/34/H','Cancelled tail dans un within '+cancelled_h+' [editorial scope description].',
    'The bare dans un drops the H source cancellation state. The exact H struck clause contains the tail.',
    {'complete_context_pointer':'/decisions/34/complete_witness_contexts/H','exact_cancelled_clause':cancelled_h,'source':compact_ref(ctx)}))
findings.append({'id':'SA023-05','title':'Local C/H scope, cancellation and punctuation','targets':witness_targets,
    'bounded_repair':'Use the exact local excerpts and explicit editorial scope labels below. Preserve complete_witness_contexts and original source references. Keep H\'s union apparatus in the local cup rows. U35 must explicitly keep H\'s cancelled state.'})

support_paths=[
 'out/briefs/source_record_brief_v05.md','out/briefs/source_record_brief_v06.md',
 'out/checks/scan023_source_assembly_release.json','out/checks/scan023_record_release.json',
 'out/checks/scan023_C_doubt_catalog.json','out/checks/scan023_H_marker_catalog.json','out/checks/scan023_S_scope.json',
 'out/checks/scan023_root_selected_source_review.md','out/checks/scan023_root_record_review.md',
 'out/checks/scan023_record_initial_gate.json','out/checks/scan023_source_assembly_initial_gate.json',
 'out/scripts/build_records.py',
]
support_hashes={p:sha((ROOT/p).read_text()) for p in support_paths}
assert support_hashes['out/briefs/source_record_brief_v06.md']=='68c899416ff5c0a1093da36ce1304fb0883641dbe52ba54375d63530bd96d721'
assert (ROOT/'out/briefs/source_record_brief_v06.md').read_text().startswith((ROOT/'out/briefs/source_record_brief_v05.md').read_text())

report={
 'scan':23,'stage':'one_targeted_final_source_and_record_audit','status':'frozen_with_bounded_public_record_findings',
 'main_approved':False,'selected_page_approved':False,'source_only':True,
 'bound_inputs':validation['checks']['frozen_text_bindings'],
 'additional_text_source_hashes':support_hashes,
 'brief':'v06 is the exact v05 prefix plus the appended public-field requirements; its complete appended section was read during this same targeted audit.',
 'scope':'Selected text source/map/record and public record review only. No crop file or crop metadata was opened, no image hash was calculated, no render/compile/install/research/delegation, no mathematical/coordinate check and no ink choice occurred.',
 'mechanical_validation':validation,
 'manual_coverage':{
   'public_review_lines_read':'1–3437, complete public record review',
   'decisions':69,'doubts':40,'inventory_entries':57,'current_groups':26,'loci':62,
   'canonical_C_parts':16,'C_resolved':4,'C_retained':12,'source_only_S_rows':7,
   'H_local_markers':{'U023-08':'H023-ILL01','U023-41':'H023-UNC01','U023-42':'H023-ILL02'},
   'C_physical_parents':33,'H_physical_parents':37,
   'root_journal':'Actual stroke descriptions were compared with the supplied journal references and exact once-viewed crop paths. No new observation or independent image claim is made.',
   'whole_region_coverage':'The 35 source-partition spans reconstruct complete selected text; all 57 inventory entries are interleaved and carry their selected attachments. Containing regions retain adjoining prose/formulas, child identities and local mixed/undetermined hand scopes.',
   'reader_provenance':'All 62 current reader_source_details dictionaries equal their corresponding frozen union readers exactly; six public summary omissions remain listed separately.',
   'notes_and_abbreviations':'The brief attributed note states manuscript readings; no check event is asserted. All three abbreviation entries preserve form/expansion and probable-expansion attribution.',
   'S10':'Both point scopes and the additional plus-run scope agree with the frozen root scope authorization. The donor\'s different historical point-specific wording remains provenance.',
   'initial_and_bounded_history':'Initial coverage audit hashes remain unchanged. Both source transitions and all 197 record changes were replayed in memory; the record inverse replay equals the initial object. No history file was altered.',
 },
 'findings':findings,
 'repair_boundary':{
   'allowed_scope':'Current public record wording and every affected current mirror, with a new exact bounded old/new closure after root review.',
   'preserve':['selected TeX bytes','selected source-map bytes','all source hashes and exact attachments','raw reader sources and provenance','initial audits and all previous closure snapshots','physical counts and parents','confidence authorizations','H-marker scopes','C canonical outcomes','all approval flags false'],
   'synchronization':'Exact mirrors and embedded current reading mentions are enumerated per target. Containing-frame readings must retain their component qualifications. Replace only the corresponding current statement; do not globally replace text inside source literals or historical reader records.',
 },
 'remaining_source_or_count_defects':[],
}
report['finding_target_counts']={f['id']:len(f['targets']) for f in findings}
out_json=P/'scan023_source_audit.json'
out_json.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

def md_text(s):
    return str(s).replace('|','\\|').replace('\n','<br>')

lines=['# Scan 023 — frozen targeted source and public-record audit','',
 'Status: **bounded public-record repairs required; approval remains false**. No selected-source, source-map, physical-count or canonical-C-outcome defect was found.','',
 'The complete 3,437-line public review was read. The audit covers all 69 decisions, 40 doubts, 57 interleaved inventory entries, 26 current groups, 62 loci, 16 canonical C parts (4 resolved / 12 retained), seven source-only S rows, local H-marker flags and C33/H37 physical parents.','',
 'Only text sources were inspected. The crop names below are references recorded in the root journal; no image or image metadata was accessed. No rendering, compilation, installation, research, delegation, ink selection, mathematical check or coordinate check occurred.','',
 '## Exact frozen bindings','', '| Source | SHA-256 |','|---|---|']
for name,value in report['bound_inputs'].items():lines.append('| '+name+' | `'+value+'` |')
lines += ['','Brief v06: `'+support_hashes['out/briefs/source_record_brief_v06.md']+'`. Its v05 prefix is byte-for-byte unchanged; the appended public-field requirements were read.','',
 '## Verification results','',
 '- All 248 authorized C/H/count-parent/confidence fields agree with root authorization v2. Counted parents are unique within each witness count. The three local H flags remain U08, U41 and U42.','- All current selected group, decision and inventory associations are reciprocal. The 166 commands have one direct owner each; 26 groups, 112 wrappers and 37 contexts remain attached. The 35 source-partition spans reconstruct both original C and the entire selected draft exactly.','- Exact literal/hash/UTF-8 reference checks passed: 4,391 current record-reference occurrences (793 unique spans) and 1,769 current map-reference occurrences (1,223 unique spans). Checks include exact JSON-pointer/source-text agreement for reader records.','- All 31 distinct journal crop references match the recorded once-viewed set; all 67 decision observation attachments reproduce their journal pairing and the public evidence retains the actual stroke description and crop name. Source-only U19, U40 and U62 carry no new crop claim.','- All 62 own-reader source-detail dictionaries equal the frozen union. The six incomplete public summaries are identified below.','- Both source-history transitions replay exactly in memory; all 197 record-history edits replay to the frozen record and invert to the preserved initial record. Initial audit and release history remain unchanged.','- Every current approval flag remains false, the notes are attributed manuscript readings, all three abbreviation schemas are complete, and no mathematical check event is present.','',
 '## Bounded findings','',
 'The JSON companion contains every exact old value, proposed replacement, source authority and affected current-mirror pointer. The following sections give the complete repair scope. These findings concern what the public fields emit; supporting evidence and original candidates remain preserved in the frozen record.','']
for finding in findings:
    lines += ['### '+finding['id']+' — '+finding['title'],'',finding['bounded_repair'],'', '| Exact field pointer | Required repair |','|---|---|']
    for item in finding['targets']:
        if finding['id']=='SA023-04':desc=item['defect']+' Prepend the exact attached own-source span printed in the JSON replacement.'
        elif finding['id']=='SA023-05':desc=item['proposed_after']
        else:desc=item['proposed_after']
        lines.append('| `'+item['pointer']+'` | '+md_text(desc)+' |')
    lines.append('')
lines += ['## Repair and preservation boundary','',
 'The writer may update the listed current public fields and their current mirrors after root review. Each target in the JSON names exact-value mirrors and embedded current-reading mentions. Keep observations, source attachments, root journal references and reader-specific original fields intact. Preserve the existing frozen releases and all initial/alternate snapshots, and append an exact bounded old/new repair closure.','',
 'The selected TeX, selected source map, physical counts, parent assignments, confidence authorizations, H-marker scopes, canonical C outcomes and all false approval flags remain fixed. The audit supplies report wording only and makes no additional ink decision.','']
(P/'scan023_source_audit.md').write_text('\n'.join(lines))
print(json.dumps({'status':report['status'],'finding_target_counts':report['finding_target_counts'],'mechanical_failures':len(validation['mechanical_failures']),
 'files':{name:sha((P/name).read_text()) for name in ['scan023_source_audit.md','scan023_source_audit.json']}},indent=2))
