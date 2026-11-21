"""Additional final-only checks; called by reader_a_final_method_audit.py.

Read-only except for the caller's new QA report files. No assembly, OCR,
image regeneration, accepted-file edits, or TeX compilation.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import difflib
import hashlib
import json
import re


def augment(ns):
    root, out, qa = ns['ROOT'], ns['OUT'], ns['QA']
    order, records = ns['order'], ns['records']
    raw, doc, rows, sha = ns['raw'], ns['doc'], ns['rows'], ns['sha']
    check, add = ns['check'], ns['add']
    tokens = lambda s: re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]', s)

    # Preserve the historical 19-audit snapshot and compare all frozen TSVs
    # to that earlier, independent-in-time hash set.
    historical_hashes = {
        'reader_a_method_findings.md': '088ac04f5de485399acee4d91676db7adc602a753a7a94f86cb4055a49f4f58b',
        'reader_a_method_findings.json': '1ccc92c5e569577cb4971c2ce4bee009d9a331ff1aefc872055ca7bbe914fe59',
        'reader_a_method_audit.py': 'ce9a4c3d7315760a1b757d6d3336938d2cc3daefb40448daf06cdb6c64265d3f',
    }
    preserved = {name: {'expected': expected, 'actual': sha(qa/name)} for name, expected in historical_hashes.items()}
    historical = doc(qa/'reader_a_method_findings.json')
    old_pages = {r['page']: r for r in historical['pages']}
    hash_changes = []
    for page_result in ns['page_results']:
        for field in ('first_sha256', 'second_sha256'):
            if page_result[field] != old_pages[page_result['page']][field]:
                hash_changes.append({'page': page_result['page'], 'field': field,
                                     'historical': old_pages[page_result['page']][field], 'current': page_result[field]})
    snapshot_changed = [name for name, row in preserved.items() if row['expected'] != row['actual']]
    check('Historical 19-audit snapshot preserved; all 46 frozen TSV hashes remain identical',
          not hash_changes and not snapshot_changed,
          {'historical_completed_utc': historical['completed_utc'], 'historical_finalized_audits': historical['summary']['finalized_audits'],
           'snapshot_files': preserved, 'frozen_tsv_hashes_compared': 46, 'changed_tsv_hashes': hash_changes})
    if hash_changes or snapshot_changed:
        add('F01', 'action_required', 'Frozen reading or historical snapshot changed',
            {'hash_changes': hash_changes, 'snapshot_changed': snapshot_changed},
            'Investigate the change; do not replace frozen readings or the historical method snapshot.')

    # Recompute the actual comparison and B/D/K counts, rather than trusting
    # stored Boolean flags or counts from the finishing script.
    comparison_issues, audit_count_issues, record_box_issues = [], [], []
    total_boxes = total_differences = total_changed = 0
    kinds = Counter()
    progress = raw(out/'progress.log').decode()
    pattern = (r'^scan (\d+) audited ([0-9:-]+ [0-9:]+ UTC): (\d+) boxes read, '
               r'(\d+) differences, (\d+) changed; cote (\d+); independent reader (reader_[abc])$')
    log_rows = re.findall(pattern, progress, re.M)
    progress_by_page = {}
    for scan, completed, boxes, differing, changed, cote, reader in log_rows:
        page = f'{cote}_scan{int(scan):03}'
        if page in progress_by_page:
            audit_count_issues.append({'page': page, 'issue': 'Duplicate audited progress entry'})
        progress_by_page[page] = {'completed_at': completed, 'boxes': int(boxes), 'differences': int(differing), 'changed': int(changed), 'reader': reader}
    if len(log_rows) != 23 or set(progress_by_page) != set(order):
        audit_count_issues.append({'issue': 'Progress does not contain exactly 23 distinct finalized audit entries', 'count': len(log_rows)})
    for page in order:
        box_rows = rows(out/'second'/f'{page}_boxes.tsv')[1]
        first_rows = rows(out/'second'/f'{page}_first.tsv')[1]
        second_rows = rows(out/'second'/f'{page}_second.tsv')[1]
        first = {r['box']: r['reading'] for r in first_rows}
        second = {r['box']: r['reading'] for r in second_rows}
        comparison = doc(out/'second'/f'{page}_comparison.json')
        adjudications = rows(out/'second'/f'{page}_adjudication.tsv')[1]
        record_boxes = {r['box']: r for r in records[page]['second_boxes']}
        actual_diff = set()
        for row in box_rows:
            kinds[row['kind']] += 1
            rb = record_boxes.get(row['box'], {})
            if rb.get('kind') != row['kind'] or any(str(rb.get(k)) != row[k] for k in ('x0','y0','x1','y1')):
                record_box_issues.append({'page': page, 'box': row['box'], 'issue': 'Accepted prescribed-box metadata differs from frozen box list'})
        for row in comparison:
            box = row['box']
            at, bt = tokens(first[box]), tokens(second[box])
            unequal = at != bt
            if unequal:
                actual_diff.add(box)
            if bool(row.get('same_tokens')) != (not unequal):
                comparison_issues.append({'page': page, 'box': box, 'issue': 'same_tokens disagrees with fresh token comparison'})
            actual_changes = []
            large = max(len(at),len(bt)) > 20000
            for tag,i,j,k,l in difflib.SequenceMatcher(None,at,bt,autojunk=large).get_opcodes():
                if tag != 'equal':
                    actual_changes.append({'type':tag,'first_tokens':at[i:j],'second_tokens':bt[k:l]})
            if row.get('token_changes') != actual_changes:
                comparison_issues.append({'page': page, 'box': box, 'issue': 'Stored token edits disagree with independently recomputed token edits'})
        if {r['box'] for r in adjudications} != actual_diff:
            comparison_issues.append({'page': page, 'issue': 'Adjudication set differs from freshly recomputed unequal boxes'})
        changed = 0
        audit_changes = {r['box']: r for r in records[page].get('audit_changes',[])}
        if set(audit_changes) != actual_diff:
            audit_count_issues.append({'page':page,'issue':'Accepted audit_changes do not cover exactly all differing boxes'})
        for row in adjudications:
            is_changed = tokens(row['first']) != tokens(row['final'])
            changed += is_changed
            if row['changed'] != ('yes' if is_changed else 'no'):
                comparison_issues.append({'page':page,'box':row['box'],'issue':'Changed flag differs from fresh token comparison'})
            accepted = audit_changes.get(row['box'],{})
            if any(accepted.get(k) != row[k] for k in ('first','second','final')) or accepted.get('changed') != is_changed:
                audit_count_issues.append({'page':page,'box':row['box'],'issue':'Accepted audit_changes differ from adjudication TSV'})
            if not row.get('final','').strip():
                audit_count_issues.append({'page':page,'box':row['box'],'issue':'Empty final adjudicated reading'})
        expected = {'boxes':len(box_rows),'differences':len(actual_diff),'changed':changed}
        audit = records[page].get('audit',{})
        for key,value in expected.items():
            if audit.get(key) != value or progress_by_page.get(page,{}).get(key) != value:
                audit_count_issues.append({'page':page,'field':key,'expected':value,'audit':audit.get(key),'progress':progress_by_page.get(page,{}).get(key)})
        for key in ('reader','completed_at'):
            if audit.get(key) != progress_by_page.get(page,{}).get(key):
                audit_count_issues.append({'page':page,'field':key,'issue':'Audit metadata differs from progress entry'})
        total_boxes += len(box_rows); total_differences += len(actual_diff); total_changed += changed
    check('All 339 full token comparisons and edit sequences recomputed', not comparison_issues,
          {'boxes':total_boxes,'different_boxes':total_differences,'changed_boxes':total_changed,'issues':comparison_issues})
    check('All 23 audit B/D/K counts, accepted audit_changes and progress entries agree', not audit_count_issues,
          {'audit_progress_rows':len(log_rows),'issues':audit_count_issues})
    check('Frozen box kinds and original coordinates agree with accepted prescriptions', not record_box_issues,
          {'box_kind_counts':dict(kinds),'issues':record_box_issues})
    for code,title,items in [('F02','Token comparison inconsistency',comparison_issues),('F03','Final audit/progress count inconsistency',audit_count_issues),('F04','Prescribed box metadata mismatch',record_box_issues)]:
        if items:
            add(code,'action_required',title,items,'Resolve the metadata discrepancy without altering a frozen independent reading.')

    # A15 was recovered separately by exact in-memory pixel reconstruction.
    recovery = doc(qa/'early_intermediate_provenance.json')
    recovery_issues = []
    for row in recovery['files']:
        p = root/row['crop']
        v = row['verification']
        if sha(p) != row['crop_sha256_after'] or row['crop_sha256_before'] != row['crop_sha256_after']:
            recovery_issues.append({'crop':row['crop'],'issue':'Recovered crop hash no longer matches'})
        if sha(root/row['source']) != row['source_sha256']:
            recovery_issues.append({'crop':row['crop'],'issue':'Original source hash no longer matches recovery'})
        if any(v[k] != 0 for k in ('pixel_mismatches','channel_mismatches','maximum_absolute_channel_error')) or not v['in_memory_png_byte_identical']:
            recovery_issues.append({'crop':row['crop'],'issue':'Exact reconstruction was not verified'})
    check('A15 exact geometry recovery remains valid for all four retained intermediates',not recovery_issues,
          {'report':'result/qa/early_intermediate_provenance.json','files':len(recovery['files']),'issues':recovery_issues})
    if recovery_issues:
        add('F05','action_required','A15 recovered provenance has changed',recovery_issues,'Investigate and preserve the retained evidence files.')
    else:
        add('R02','resolved_before_final_audit','A15 four early intermediate crop rectangles recovered exactly',
            {'report':'result/qa/early_intermediate_provenance.json','crop_count':4,'pixel_mismatches':0,'png_byte_identical':True},
            'No action; retain the standalone recovery report and unchanged crops.',status='resolved')

    # Check current transcription bytes ourselves; never call the root's
    # freeze/verify script, since even its verify mode appends to progress.log.
    freeze_path = out/'transcription_hashes.tsv'
    freeze_issues=[]
    expected_paths=['pages/'+p+'.tex' for p in order]+[ns['ID']+'_transcription.tex']
    hash_header, hash_rows = rows(freeze_path)
    if hash_header != ['path','sha256'] or [r['path'] for r in hash_rows] != expected_paths:
        freeze_issues.append({'issue':'Freeze does not contain exactly the23 pages and combined transcription in order'})
    if len(hash_rows)!=24 or len({r['path'] for r in hash_rows})!=24:
        freeze_issues.append({'issue':'Freeze count or uniqueness differs from24','count':len(hash_rows)})
    for row in hash_rows:
        actual=sha(out/row['path'])
        if actual != row['sha256']:
            freeze_issues.append({'path':row['path'],'expected':row['sha256'],'actual':actual})
    progress = raw(out/'progress.log').decode()
    frozen_lines=re.findall(r'^transcription frozen (.+ UTC)$',progress,re.M)
    log_hashes=re.findall(r'^sha256 ([0-9a-f]{64}) (.+)$',progress,re.M)
    if len(frozen_lines)!=1 or [(p,h) for h,p in log_hashes] != [(r['path'],r['sha256']) for r in hash_rows]:
        freeze_issues.append({'issue':'Progress freeze line/hashes differ from24-row transcription_hashes.tsv'})
    if frozen_lines:
        frozen_at=datetime.strptime(frozen_lines[-1],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
        last_audit=max(datetime.strptime(records[p]['audit']['completed_at'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc) for p in order)
        if frozen_at < last_audit:
            freeze_issues.append({'issue':'Transcription frozen before final adjudication','frozen_at':str(frozen_at),'last_audit':str(last_audit)})
    verify_lines=re.findall(r'^transcription hashes verified unchanged (.+ UTC): (\d+) files$',progress,re.M)
    verified_in_log=bool(verify_lines and int(verify_lines[-1][1])==24)
    check('All24 frozen transcription hashes and progress hash entries match current files',not freeze_issues,
          {'files':len(hash_rows),'freeze_lines':frozen_lines,'issues':freeze_issues,'unchanged_verification_log_present':verified_in_log,'verify_lines':verify_lines})
    if freeze_issues:
        add('F06','action_required','Final transcription freeze mismatch',freeze_issues,'Stop final packaging and investigate; do not rewrite the freeze to conceal a change.')
    if not verified_in_log:
        add('P03','post_documentation_gate','Root final unchanged-verification log entry remains pending',
            {'all24_hashes_currently_match':not freeze_issues,'log_entry_present':False},
            'After documentation synchronization, root must run freeze_transcription.py verify; reader_a can then refresh only this final audit report.')

    # Count-level freshness is checked here; byte-exact aggregate construction,
    # remaining-doubt mappings and static TeX checks belong to reader_b's
    # complementary final static audit.
    material=[c for p in order for c in records[p].get('changes',[]) if c.get('diff_c') or c.get('diff_h')]
    totals={'places':len(material),'against_C':sum(bool(c.get('diff_c')) for c in material),
            'against_H':sum(bool(c.get('diff_h')) for c in material),
            'inventory_elements':sum(len(records[p].get('inventory',[])) for p in order),
            'remaining_doubts':sum(len(records[p].get('doubts',[])) for p in order)}
    count_issues=[]
    if len(ns['collation'])!=totals['against_H']:
        count_issues.append({'file':'collation','actual':len(ns['collation']),'expected':totals['against_H']})
    if len(ns['inventory'])!=totals['inventory_elements']:
        count_issues.append({'file':'inventory','actual':len(ns['inventory']),'expected':totals['inventory_elements']})
    check('Final aggregate counts agree with current accepted records',not count_issues,{'totals':totals,'issues':count_issues})
    if count_issues:
        add('F07','action_required','Aggregate count freshness mismatch',count_issues,'Root must refresh aggregates after metadata corrections; no frozen transcription change is authorized.')

    ns['final_extensions']={
        'historical_snapshot_preserved':not snapshot_changed,
        'historical_frozen_tsv_hashes_unchanged':not hash_changes,
        'independent_boxes':total_boxes,'different_boxes':total_differences,'changed_boxes':total_changed,
        'final_aggregate_counts':totals,'transcription_hashes':len(hash_rows),
        'transcription_hashes_match':not freeze_issues,'final_unchanged_verification_log_present':verified_in_log,
        'complementary_scope':'Reader_b final static QA owns byte-exact aggregate consistency, remaining-doubt mappings and accepted TeX static structure. This report checks method/identity/freeze/provenance and export counts.',
        'post_package_gate':'The final ZIP does not yet exist at this method snapshot. Its exact contents, restoration and durable save receipt require root post-package verification.',
    }
