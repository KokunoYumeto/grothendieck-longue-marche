"""Aggregate actual final36 image receipts; never infer inspection from rendering.

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
