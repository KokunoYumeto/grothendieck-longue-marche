"""Approved final documentation refresh; no assembly or TeX changes."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
BT=chr(96)
paths=['notation_final.md','legibility_note.md','sheet_feedback_details.md','records/148_scan072.json']
raw={name:(ROOT/name).read_bytes() for name in paths}
texts={name:raw[name].decode() for name in paths if name.endswith('.md')}
record=json.loads(raw['records/148_scan072.json'])
record_before=copy.deepcopy(record)
edits=[]

def replace(name,old,new,basis):
    # Keep the consolidated table's existing inline-code style.
    if name=='notation_final.md':
        new=new.replace(r'\(',BT).replace(r'\)',BT)
    assert texts[name].count(old)==1,(name,old[:100],texts[name].count(old))
    texts[name]=texts[name].replace(old,new,1)
    edits.append({'file':name,'operation':'replace','before':old,'after':new,
                  'basis':basis,'new_ink_decision':False})

def row(prefix,new,basis):
    found=[s for s in texts['notation_final.md'].splitlines() if s.startswith(prefix)]
    assert len(found)==1,(prefix,len(found))
    replace('notation_final.md',found[0],new,basis)

row('| '+BT+r'\gamma'+BT+' |',
    r'| \(\gamma\) | A low loop with a descending return, sometimes with a long right tail; its upper arm varies in height and can become almost flat. | 148:048, 049 and 067 have consistent clear gamma forms. The local weight glyph on 053 retains sigma/gamma alternatives; including that page here does not certify gamma. Overwritten divisors and indices remain separately doubtful. |',
    ['NQ01','records/148_scan053.json: local sigma/gamma notation','records/148_scan067.json: gamma notation'])
row('| Star, f, chi and epsilon |',
    r'| Star, f, chi, epsilon and fraktur s | Crossed curves, a long returning sweep or an overworked multistroke cluster require local comparison. | 148:062 has a clear lower star but an earlier f-like index remains doubtful; 063 preserves its target-index uncertainty. The signature label on 071 retains \(\chi\), \(\varepsilon\) and \(\mathfrak{s}\) as alternatives. No universal substitution is imposed. |',
    ['records/148_scan071.json: doubt M0949'])
row('| '+BT+r'\widetilde\Sigma'+BT,
    r'| \(\widetilde\Sigma\), \(\overline\Sigma\), plain \(\Sigma\), \(\widetilde R\), \(\Gamma\) | A separate upper run may be an accent; its separation and shape must be read locally. A connected lower foot belongs to the letter. | On 056 the cancelled opening has a clear tilde, while the live pi-zero formula retains tilde/plain Sigma. On 064 the tuple retains tilde/plain Sigma, and the margin separately retains tilde/bar/plain Sigma. The cancelled lower square on 050 remains doubtful. A retraced Gamma foot on 062 is not converted into an underline. |',
    ['NQ02','records/148_scan056.json: tilde/plain notation','records/148_scan064.json: separate tuple and margin notation'])
old=next(s for s in texts['notation_final.md'].splitlines() if s.startswith('| '+BT+r'\underline r'+BT+' |'))
new=r'| Dotted and undotted divisibility | The raised item-2 heading on 061 has two dots immediately left of a divisibility upright, rendered \(\mathrel{:\!\vert}\); the lower main relation has an undotted upright. | This is an occurrence-specific graphic distinction. The marginal relation remains divisibility/not-equal uncertain. Item 3 retains unindexed target Z letters and a \(d\)/\(d_a\) multiplier doubt; no missing indices are supplied. |'
replace('notation_final.md',old,old+'\n'+new,['NQ03','records/148_scan061.json: dotted divisor notation and quotient doubt'])
row('| '+BT+'='+BT+' as a word abbreviation |',
    r'| \(=\) as a word abbreviation | Two horizontal bars stand for même in phrases such as de =. | 148:055, 061, 063, 067 and 071. The separate equality/cancelled-ou group on 061 remains doubtful. The parenthetical opening before catégorie fibre on 071 retains la, equality and en alternatives; it is not settled by the clear shorthand elsewhere. |',
    ['records/148_scan071.json: fibre parenthetical opening','records/148_scan061.json: footnote equality/cancelled ou'])
row('| '+BT+'c_i^0'+BT+', '+BT+'c_i^1'+BT+'; literal '+BT+r'\pi(j)'+BT+' |',
    r'| Inter-hole c/a and c/b alternatives; literal \(\pi(j)\) | Retraced outer c-like curves coexist with closed or ascending inner strokes compatible with a or b. The descending j remains j even when the argument suggests another index. | On 148:067 each of the four 0-side labels retains \(c_i^0/a_i^0\) alternatives, and each of the four 1-side labels retains \(c_i^1/b_i^1\) alternatives. The c readings are low-confidence primaries. The separate possible pi(j) index slip is discussed only in the notes. |',
    ['NQ06','records/148_scan067.json: eight retraced inter-hole initials and pi(j)'])
row('| '+BT+r'E_{\bar K/K}'+BT+' and '+BT+r'\Pi_K'+BT+' |',
    r'| \(E_{\bar K/K}\), \(\Pi_K\) and the extension separator | Plain capital E; bar over the first K only in the displayed quotient index. On 149:003 the separator varies from almost upright to oblique. | 149:003–004 retain their local field indices. The five extension separators on 003 are consistently rendered as slash after local comparison; the near-upright form is not read as a new conditional relation. Repeated witness agreement was checked against each occurrence. |',
    ['records/149_scan003.json: E index and field-extension separator notation'])
row('| Numeric labels in drawings |',
    r'| Numeric labels in drawings | 0, 1, infinity and local branch weights retain their own positions and enclosures. | On 148:069 the upper-left a label retains infinity/0, upper b retains 0/infinity, left-boundary d is doubtful infinity without a secure alternative, and upper-central e retains 1/infinity. On 072 the heavy two-digit weight retains 15/25; the separate upper-vertex lower annotations 1 and 9 are not combined into 19. |',
    ['records/148_scan069.json: four local label doubts','records/148_scan072.json: heavy two-digit weight doubt'])
old=next(s for s in texts['notation_final.md'].splitlines() if s.startswith('| Short forms and category abbreviations |'))
new=r'| Raised point abbreviations | A descending p is followed by a distinctly raised crossed t. A raised ts ending is a separate written form. | 149:003 has \(p^t\); 149:004 has \(p^t\). in the object description and \(p^t\) without a point in the corresponding-points sentence. On 148:064 the base-point short form has raised ts. The superscripts, punctuation and absence of an extra s are preserved locally. |'
replace('notation_final.md',old,old+'\n'+new,
        ['records/149_scan003.json: change 149_scan003-07','records/149_scan004.json: changes 149_scan004-21 and -22','records/148_scan064.json: raised ts-base notation'])
old=next(s for s in texts['notation_final.md'].splitlines() if s.startswith('| '+BT+r'\unsure{\wedge|\cap}'+BT))
replace('notation_final.md',old,old.replace(BT+r'\unsure{\wedge|\cap}'+BT,r'\(\wedge\) / \(\cap\)'),
        ['Markdown table formatting only: remove an unescaped cell-delimiter pipe; accepted wedge/cap alternatives unchanged'])

old=('Scan 067 contains pale and overwritten mathematical layers whose partial survival does not support a complete confident recovery. '
     'Some of the printed zero pattern near the upper edge of 068, several enclosed labels on 069, the unidentified cancelled and isolated marks on 071, '
     'the coined caption and small isolated mark on 072, and the six overworked superscripts on 149:004 remain less secure than the surrounding text.')
new=('Scan 067 contains pale and overwritten mathematical layers whose partial survival does not support a complete confident recovery; '
     'its eight inter-hole labels retain low-confidence c/a or c/b alternatives. Some of the printed zero pattern near the upper edge of 068, '
     'the four doubtful vertex labels on 069, the unidentified cancelled and isolated marks and the chi/epsilon/fraktur-s label on 071, '
     'the coined caption, small isolated mark and heavy 15/25 weight on 072, and the six overworked superscripts on 149:004 remain less secure than the surrounding text.')
replace('legibility_note.md',old,new,['records/148_scan067.json: eight label doubts','records/148_scan069.json: four label doubts','records/148_scan071.json: M0949','records/148_scan072.json: heavy two-digit weight'])
old='Both drafts agree at some wrong places: the boundary labels on 067 and the initial accents in réconstitue / réconstituer on 149:003–004 are concrete examples.'
new=('Both drafts agree at some wrong places: the detached initial accents in réconstitue / réconstituer and the raised t in the point abbreviations on 149:003–004 are concrete examples. '
     'The boundary labels on 067 are a different case: the witnesses’ a/b readings remain alternatives to the low-confidence c readings and are not counted here as securely refuted shared readings.')
replace('legibility_note.md',old,new,['NQ06','root-requested secure shared-error examples','records/149_scan003.json: change 149_scan003-07','records/149_scan004.json: changes 149_scan004-21 and -22'])

old=next(s for s in texts['sheet_feedback_details.md'].splitlines() if s.startswith('| Source spelling is lost despite C/H agreement. |'))
new=('| A raised abbreviation ending is flattened or read as an extra plural. | 149:003–004. The point abbreviation has p with a raised crossed t. '
     'Both drafts flatten it on 003 and at the first occurrence on 004; at the second occurrence on 004 both read pts. '
     'Preserve the raised t, the point after the first 004 occurrence and the absence of a point after the second. The raised ts in 148:064 is a distinct form. |')
replace('sheet_feedback_details.md',old,old+'\n'+new,['root-approved raised-t recurrence','records/149_scan003.json: change 149_scan003-07','records/149_scan004.json: changes 149_scan004-21 and -22'])

idx=next(i for i,x in enumerate(record['notation']) if x['sign']=='Flagged 1; crossed 7')
updates={
    'sign':'Flagged 1; crossed 7; doubtful 15/25 weight',
    'meaning_or_form':'The large 1 below the upper vertex has a diagonal entry flag and horizontal foot. These clear 1 features do not settle the overworked first digit of the heavy 15/25 weight. The 7 is crossed in the graph and folio.',
    'places':'Right graph: large 1, doubtful 15/25 weight, 7 and 17; lower folio 71',
    'universality':'The clear 1 and 7 occurrences were compared locally. Neither the heavy 15/25 weight nor the separate small doubtful mark in the left drawing is resolved from those clearer forms.',
    'witness_errors':'H combines the upper vertex lower pair 1 and 9 into 19. Both witnesses read 15 at the heavy weight; the completed audit retains 15/25 uncertainty, a certainty change without a new material witness-change row.'
}
for key,value in updates.items():
    edits.append({'file':'records/148_scan072.json','json_pointer':f'/notation/{idx}/{key}',
                  'operation':'replace','before':record['notation'][idx][key],'after':value,
                  'basis':['records/148_scan072.json: completed audit; heavy two-digit weight doubt'],'new_ink_decision':False})
    record['notation'][idx][key]=value

check=copy.deepcopy(record);check['notation'][idx]=record_before['notation'][idx]
assert check==record_before
protected=list((ROOT/'pages').glob('*.tex'))+[f for f in (ROOT/'second').iterdir() if f.is_file()]
protected_hashes={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in protected}
for name in paths:
    assert (ROOT/name).read_bytes()==raw[name],f'Concurrent modification: {name}'
for name,value in texts.items():(ROOT/name).write_text(value)
(ROOT/'records/148_scan072.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
assert all(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h for name,h in protected_hashes.items())

log={
    'schema_version':1,'editor':'reader_c','performed_at_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Root-approved documentation refresh after completion of all 23 audits; no new image views or ink decisions.',
    'edited_files':paths,'edits':edits,'edit_count':len(edits),
    'file_hashes':{name:{'before_sha256':hashlib.sha256(raw[name]).hexdigest(),
                         'after_sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in paths},
    'accepted_page_and_second_files_verified_unchanged':len(protected),
    'assembly_run':False,'new_ink_decisions':[],
    'prior_metadata_corrections_verified':'All 35 after-values from reader_c_metadata_corrections.json remained present at the preceding read-only check.',
    'requirements_check':{
        'all_required_top_level_components_present':True,'accepted_pages':23,
        'combined_fragment_contains_all_current_page_texts':True,'combined_fragment_has_no_preamble':True,
        'collation_decisions_inventory_check_events_headers_match_prompt':True,
        'second_boxes_first_and_second_files_present_for_all_pages':True,
        'remaining_root_steps':['Assemble once from the corrected records and three documentation templates.',
                                'Validate final counts and completed audit set, then freeze the 24 transcription hashes.',
                                'Recheck frozen hashes and package the required sole final ZIP.']
    },
    'not_modified':['Accepted page TeX','Frozen and other second-reading files','All records except the authorized 072 notation row',
                    'Combined transcription','Aggregate reports/tables','Progress log','Prior metadata correction logs']
}
out=ROOT/'qa/reader_c_final_documentation_updates.json'
out.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'edited_files':paths,'edits':len(edits),'log':str(out),'assembly_run':False},indent=2))
