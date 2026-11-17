"""Author six new checkpoint36 helper sources; never execute them."""
from pathlib import Path
from datetime import datetime, timezone
import ast,difflib,hashlib,json
P=Path(__file__).resolve().parents[1]
H=lambda b:hashlib.sha256(b).hexdigest()
changes=[]
def save(old,new,text):
    src=P/old;dest=P/new
    assert not dest.exists(),new
    before=src.read_bytes();dest.write_text(text)
    ast.parse(text,filename=new)
    diff=''.join(difflib.unified_diff(before.decode().splitlines(True),text.splitlines(True),fromfile=old,tofile=new))
    dp=P/'work_DE'/('checkpoint36_'+dest.stem+'_source.diff');assert not dp.exists();dp.write_text(diff)
    changes.append(dict(predecessor=dict(path=old,bytes=len(before),sha256=H(before)),source=dict(path=new,bytes=dest.stat().st_size,sha256=H(dest.read_bytes())),exact_diff=dict(path=str(dp.relative_to(P)),sha256=H(dp.read_bytes()))))
# Render only actual current heading intervals; corrected legacy headings are mandatory.
s=(P/'code/render_checkpoint35_pdf.py').read_text().replace('checkpoint35','checkpoint36').replace('Checkpoint35','Checkpoint36').replace('final35','final36').replace('fresh35','fresh36').replace('from35','from36').replace('existing35','existing36')
s=s.replace("range(112, 120)","range(120, 126)").replace("range(167, 169)","range(169, 174)")
s=s.replace("headings['A.112']","headings['A.120']").replace("headings['A.119']","headings['A.125']").replace("headings['B.167']","headings['B.169']").replace("headings['B.168']","headings['B.173']")
s=s.replace('A112_through_A119','A120_through_A125').replace('B167_through_B168','B169_through_B173')
needle="    front = list(range(1, min(7, len(doc)) + 1))"
insert="""    editorial_headings = {}
    for label in ('A.119', 'E.52'):
        hits = statement_pages(texts, label)
        require(len(hits) == 1, 'Expected one corrected legacy heading for ' + label + ': ' + repr(hits))
        editorial_headings[label] = hits[0]
    require(editorial_headings['A.119'] <= a_start, 'A119 follows the new A interval')
    require(b_end < editorial_headings['E.52'] <= reference_start, 'E52 boundary is inconsistent')
    editorial_intervals = {'A119_citation_spacing': [editorial_headings['A.119'], a_start],
                          'E52_citation_spacing': [editorial_headings['E.52'], reference_start]}
    editorial_pages = sorted({n for lo, hi in editorial_intervals.values() for n in range(lo, hi + 1)})
    required_individual = sorted(set(required) | set(editorial_pages))
"""
assert needle in s;s=s.replace(needle,insert+needle)
s=s.replace('front + required + boundaries + references','front + required_individual + boundaries + references')
s=s.replace("'required_new_mathematical_pages': required,","'required_new_mathematical_pages': required,\n        'editorial_statement_heading_pages': editorial_headings,\n        'required_editorial_intervals_inclusive': editorial_intervals,\n        'required_editorial_pages': editorial_pages,\n        'required_individual_pages': required_individual,")
s=s.replace('Entire actual A112-A119 and B167-B168 intervals, inclusive boundary pages, front1-7, all References pages, and final document page.','Entire actual A120-A125 and B169-B173 intervals, plus entire heading-located corrected A119 and E52 intervals, inclusive boundary pages, front1-7, all References pages, and final document page.')
s=s.replace("'contact_sheets': len(contact_names), 'intervals': intervals,","'contact_sheets': len(contact_names), 'intervals': intervals,\n                      'editorial_intervals': editorial_intervals, 'required_individual_pages': required_individual,")
save('code/render_checkpoint35_pdf.py','code/render_checkpoint36_pdf.py',s)
# All actual passes, dynamic metrics, honest underfull delta.
s=(P/'code/audit_checkpoint35_final_pdf.py').read_text().replace('checkpoint35','checkpoint36').replace('checkpoint34','checkpoint35')
save('code/audit_checkpoint35_final_pdf.py','code/audit_checkpoint36_final_pdf.py',s)
# Preconditions: exact current counts, immutable parent and dynamic final metrics.
s=(P/'code/check_checkpoint35_preconditions.py').read_text().replace('checkpoint35','checkpoint36').replace('checkpoint_35.zip','checkpoint_36.zip').replace('checkpoint_34.zip','checkpoint_35.zip').replace('thirty_fifth','thirty_sixth')
s=s.replace('372','383').replace('328','339').replace('116','117').replace('range(112,120)','range(120,126)').replace('range(167,169)','range(169,174)')
s=s.replace("anchor['parent_number']==34 and anchor['child_number']==35","anchor['parent_number']==35 and anchor['child_number']==36")
s=s.replace('529409669','530938760').replace('28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb','33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121')
s=s.replace('10387','10746').replace('152653','163040').replace("anchor['inherited_archives']==33","anchor['inherited_archives']==34")
s=s.replace("[('images',67108864),('documents',67108864),('data',67108864)]","[('images',134217728),('documents',67108864),('data',67108864)]")
s=s.replace("    assert set(visual['required_math_pages'])<=set(visual['individually_inspected_pages'])","    assert visual['required_editorial_pages']==render['required_editorial_pages']\n    assert visual['required_individual_pages']==render['required_individual_pages']\n    assert set(visual['required_individual_pages'])<=set(visual['individually_inspected_pages'])")
s=s.replace('exact closed34 anchor','exact closed35 anchor')
save('code/check_checkpoint35_preconditions.py','code/check_checkpoint36_preconditions.py',s)
# One immutable capture, same fail-closed timing and publication order.
s=(P/'code/capture_checkpoint35.py').read_text().replace('checkpoint35','checkpoint36').replace('checkpoint_35.zip','checkpoint_36.zip').replace('Scheduled35','Scheduled36').replace('immutable35','immutable36').replace('Immutable35','Immutable36').replace('single35','single36').replace('thirty_fifth','thirty_sixth').replace('Thirty-fifth','Thirty-sixth').replace('thirty-fifth','thirty-sixth').replace('progress_review_35h','progress_review_36h')
s=s.replace('datetime(2026,11,17,13,49,30','datetime(2026,11,17,14,49,30').replace('next_due=datetime(2026,11,17,14,49,30','next_due=datetime(2026,11,17,15,49,30')
s=s.replace('2026-11-17 14:49:30 UTC','2026-11-17 15:49:30 UTC')
s=s.replace('372','383').replace('328','339').replace('116','117').replace('All ten new formal','All eleven new formal')
s=s.replace("'Actual central quotient and residual structures, full modular central tower, normalized residual reduction, entire cyclic and involution obstruction spaces, and a strictly larger mixed contact image proved; both main problems and actual CM parity remain open.'","'Actual elliptic cubic, boundary criterion, torsion transporters and derived refinement, plus complete complementary contact targets, proved at their stated scopes; both main problems and actual CM parity remain open.'")
a=s.index('Open. The actual central quotient');b=s.index('\n\nThis is the single36',a)
s=s[:a]+'''Open. The odd coherent coordinates vanish after forgetting the constrained
centralizer. Actual elliptic cubic and torsion classification give unique
continuous derived transporters, while the specified boundary-power and
coherent involution obstructions remain unevaluated. The complete one-sided
and complementary retained contact images have full induced topology,
exact normal restriction kernels and continuous sections. Their different
defects do not prove the whole fixed-source equality. All eleven proofs,
all mandatory new and corrected legacy page intervals, and all preserved
citation-spacing changes are bound to actual final evidence.'''+s[b:]
s=s.replace('pinned34','pinned35').replace('closed34','closed35').replace('10387','10746').replace('152653','163040').replace('163040 resulting','173786 resulting')
s=s.replace("retained['archives']==34 and retained['archive_entries']==163040","retained['archives']==35 and retained['archive_entries']==173786")
s=s.replace("str(root/'code/package_checkpoint.py'),'35'","str(root/'code/package_checkpoint.py'),'36'")
save('code/capture_checkpoint35.py','code/capture_checkpoint36.py',s)
# Publisher: every actual role/file remains mandatory; dynamic PDF identity.
s=(P/'code/publish_checkpoint35_readiness.py').read_text().replace('checkpoint35','checkpoint36').replace('checkpoint_35.zip','checkpoint_36.zip').replace('checkpoint_34.zip','checkpoint_35.zip').replace('Checkpoint35','Checkpoint36')
s=s.replace('28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb','33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121').replace('529409669','530938760')
s=s.replace('372','383').replace('328','339').replace('116','117').replace('range(112,120)','range(120,126)').replace("['B.167','B.168']","['B.'+str(n) for n in range(169,174)]")
s=s.replace("anchor['parent_number'] == 34 and anchor['child_number'] == 35","anchor['parent_number'] == 35 and anchor['child_number'] == 36").replace("anchor['inherited_archives'] == 33","anchor['inherited_archives'] == 34").replace('10387','10746').replace('152653','163040')
s=s.replace("    for kind in ('images', 'documents', 'data'):\n        assert estimate['prospective_bundles'][kind]['dictionary_bytes'] == 67108864","    for kind, dictionary in [('images', 134217728), ('documents', 67108864), ('data', 67108864)]:\n        assert estimate['prospective_bundles'][kind]['dictionary_bytes'] == dictionary")
s=s.replace("assert set(render['required_new_mathematical_pages']) <= set(visual['individually_inspected_pages'])","assert visual['required_math_pages'] == render['required_new_mathematical_pages']\n    assert visual['required_editorial_pages'] == render['required_editorial_pages']\n    assert visual['required_individual_pages'] == render['required_individual_pages']\n    assert set(render['required_individual_pages']) <= set(visual['individually_inspected_pages'])")
s=s.replace("'code/package_checkpoint.py', 'code/checkpoint_data_tar.py',","'code/package_checkpoint.py', 'code/checkpoint_data_tar.py', 'code/checkpoint_image_tar.py',")
s=s.replace('2026-11-17 14:49:30 UTC','2026-11-17 15:49:30 UTC')
s=s.replace('Actual residual and contact comparisons retain their exact scopes; both main decisions, the coherent class, and actual CM parity remain open.','Actual elliptic and complementary contact comparisons retain their exact scopes; both main decisions, the boundary condition, the coherent class, and actual CM parity remain open.')
save('code/publish_checkpoint35_readiness.py','code/publish_checkpoint36_readiness.py',s)
# Finalizer uses explicit actually-viewed receipts; no invented root observations.
s=r'''"""Aggregate actual final36 image receipts; never infer inspection from rendering.

Supply all four reviewer receipts, including root's explicit page/contact
observations. No page count, PDF hash, observation text or producer exit is
invented or inherited from an earlier checkpoint.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json


def main():
    root=Path(__file__).resolve().parents[1]
    read=lambda p:json.loads((root/p).read_text())
    sha=lambda p:hashlib.sha256((root/p).read_bytes()).hexdigest()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reviews',nargs=4,required=True)
    args=parser.parse_args()
    assert len(set(args.reviews))==4
    metrics=read('records/checkpoint36_metrics.json')
    render_path='records/pdf_qa/checkpoint36_final/render_manifest.json'
    render=read(render_path)
    audit=read('records/checkpoint36_final_pdf_audit.json')
    expected=metrics['pdf_sha256']
    assert sha('LM4_SUCCESSOR_paper.pdf')==expected==render['pdf_sha256']==audit['final_pdf_sha256']
    assert metrics['pages']==render['page_count']>0
    assert render['dpi']==144 and render['visual_approval'] is False
    assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
    assert audit['result']=='PASS_FINAL_LOGS' and audit['final_overfull_count']==0
    new=set(render['required_new_mathematical_pages'])
    editorial=set(render['required_editorial_pages'])
    required=set(render['required_individual_pages'])
    rendered=set(render['rendered_pages'])
    assert required==new|editorial and required<=rendered
    assert set(render['required_editorial_intervals_inclusive'])=={'A119_citation_spacing','E52_citation_spacing'}
    individual=set();contacts=set();notes=[];reviewers=set()
    expected_contacts={'records/pdf_qa/checkpoint36_final/'+name for name in render['contact_files']}
    for rel in args.reviews:
        item=read(rel)
        assert item['pdf_sha256']==expected,rel
        reviewers.add(item['reviewer'])
        digest=item.get('render_manifest_sha256')
        if digest is None:digest=item['render_manifest']['sha256']
        assert digest==sha(render_path),rel
        assert not item.get('truncated_outputs_counted',False),rel
        for row in item['pages']:
            assert row.get('result',row.get('status'))=='PASS' and not row.get('issues',[])
            assert row.get('actually_viewed_individually',row.get('actually_viewed')) is True
            n=row['page'];path=row.get('path',row.get('file'))
            assert n in rendered and path==f'records/pdf_qa/checkpoint36_final/page-{n:03d}.png'
            assert sha(path)==row['sha256']
            assert isinstance(row.get('observation'),str) and row['observation'].strip()
            individual.add(n)
            notes.extend([dict(receipt=rel,page=n,note=v) for v in row.get('nonblocking_notes',[])])
        for row in item.get('contacts',[]):
            assert row['path'] in expected_contacts and row['result']=='PASS' and not row.get('issues',[])
            assert row['actually_viewed_separately'] is True and sha(row['path'])==row['sha256']
            contacts.add(row['path'])
        notes.extend([dict(receipt=rel,observation=v) for v in item.get('nonblocking_notes',[])])
    assert reviewers=={'/root','/root/involutions','/root/torus_real','/root/topology_census'}
    assert required<=individual<=rendered
    assert contacts==expected_contacts and len(contacts)==render['contact_sheets']>0
    for row in audit['final_log_and_stdout_audits']:
        assert sha(row['path'])==row['sha256'] and not row['warnings'] and not row['issues']
    underfull_scope=(f"Actual final engine/stabilized stdout each contain {audit['final_underfull_count']} underfull notices. "
        f"Identical multiset to checkpoint35: {audit['underfull_identical_to_checkpoint35']}. "
        f"Added: {audit['added_underfull_notices']!r}; removed: {audit['removed_underfull_notices']!r}. "
        'All required page intervals were individually inspected; underfull counts are not preassigned.')
    summary=dict(recorded_at=datetime.now(timezone.utc).isoformat(),visual_review='PASS',pdf_sha256=expected,
        rendered_pages=render['rendered_pages'],required_math_pages=render['required_new_mathematical_pages'],
        required_editorial_pages=render['required_editorial_pages'],required_individual_pages=render['required_individual_pages'],
        required_editorial_intervals_inclusive=render['required_editorial_intervals_inclusive'],
        individually_inspected_pages=sorted(individual),individual_page_review_receipts={p:sha(p) for p in args.reviews},
        contact_sheets_inspected=len(contacts),each_contact_sheet_opened_separately=True,truncated_outputs_counted=False,
        final_log_and_stdout_case_insensitive='PASS',final_log_and_stdout_audits=audit['final_log_and_stdout_audits'],
        underfull_scope=underfull_scope,nonblocking_editorial_notes=notes,
        final_edition_scope='Actual frozen36 PDF. All new formal proof intervals and complete heading-located corrected A119/E52 intervals individually viewed; every rendered page also covered by separately viewed contact sheets. No prior physical page number or root observation is reused.',
        producer_exit_scope='Actual tool exit observations are recorded separately; this file does not assert an unobserved process result.')
    target=root/'records/checkpoint36_visual_review.json'
    with target.open('x') as stream:json.dump(summary,stream,indent=2);stream.write('\n')
    text=(f"Visual review: PASS\nFinal PDF SHA256: {expected}\n"
          f"{metrics['pages']} pages; {len(new)} new mathematical pages; {len(editorial)} mandatory legacy editorial pages; "
          f"{len(individual)} individually inspected pages; {len(rendered)} rendered pages; {len(contacts)} separately inspected contact sheets.\n"
          'Final engine log and stabilized stdout: no overfull boxes, warnings, unresolved references or errors.\n'+underfull_scope+'\n'
          f"Nonblocking observations preserved: {notes!r}\n")
    with (root/'records/checkpoint36_typesetting.txt').open('x') as stream:stream.write(text)
    print(json.dumps(dict(status='PASS',pdf_sha256=expected,pages=metrics['pages'],required_math_pages=len(new),
        required_editorial_pages=len(editorial),individual_pages=len(individual),rendered_pages=len(rendered),contacts=len(contacts)),indent=2))


if __name__=='__main__':
    main()
'''
save('code/finalize_checkpoint35_visual_record.py','code/finalize_checkpoint36_visual_record.py',s)
manifest=dict(created_at=datetime.now(timezone.utc).isoformat(),author='/root/topology_census',status='SOURCE_ONLY_NOT_EXECUTED',helpers=changes,
    scope='Six new sources only; all predecessor35 bytes unchanged. No helper imported or executed, no PDF/build/render/ZIP/retention/estimator produced. Final PDF values come only from current frozen metrics; explicit page/contact receipts remain mandatory.',
    expected_counts=dict(statements=383,Proved=339,Refuted=19,Open=19,Known=6,references=117,tasks=49),
    scheduled_at='2026-11-17T14:49:30+00:00',next_scheduled_at='2026-11-17T15:49:30+00:00',
    retention=dict(parent=35,child=36,parent_logical_entries=10746,inherited_rows=163040,resulting_rows=173786),
    dictionary_policy=dict(images=134217728,documents=67108864,data=67108864),
    substantive_adaptation='Finalizer takes --reviews with exactly four actual reviewer receipts; it no longer generates root observations, hardcodes final metrics, or mutates reports. Renderer locates A119/E52 full intervals by actual statement headings, and finalizer/preconditions/publisher enforce their individual coverage.',
    ast_parse_only=True,helpers_executed=False,central_files_changed=False)
mp=P/'work_DE/checkpoint36_capture_helpers_source_manifest.json';assert not mp.exists();mp.write_text(json.dumps(manifest,indent=2)+'\n')
for x in changes:print(x['source']['path'],x['source']['sha256'])
print(str(mp.relative_to(P)),H(mp.read_bytes()))
