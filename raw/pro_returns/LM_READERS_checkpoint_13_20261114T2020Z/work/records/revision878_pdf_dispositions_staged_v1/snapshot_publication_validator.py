def validate_snapshot_publication_pdf(root, name, row, snapshots):
    """Qualify one exact preserved whole book without reading a current PDF."""
    q = row['source_scope_qualification']
    if q.get('kind') != 'immutable_snapshot_publication_pdf':
        raise ValueError('Not an exact preserved snapshot publication PDF.')
    ref = q['snapshot']
    snapshot_path = safe_name(ref['path'])
    if (not snapshot_path.startswith('work/data/audit_history/') or
            not snapshot_path.endswith('/SNAPSHOT_COMPLETE.json')):
        raise ValueError('Snapshot book authority has an unexpected location.')
    key = (snapshot_path, ref['sha256'], ref['bytes'])
    if key not in snapshots:
        path = root / snapshot_path
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('Snapshot book authority escapes its root.')
        data = path.read_bytes()
        if digest(data) != ref['sha256'] or len(data) != ref['bytes']:
            raise ValueError('Snapshot book authority changed.')
        snapshots[key] = json.loads(data)
    document = snapshots[key]
    if (document.get('schema') != 'audit-revision-snapshot-v1' or
            document.get('status') != 'COMPLETE_RECORD_SNAPSHOT_NOT_RELEASE_APPROVAL' or
            document.get('additive_label') != 'final_discovery' or
            type(document.get('revision')) is not int or
            document['revision'] != q.get('snapshot_revision') or
            document.get('observations_generated_by_script') is not False or
            document.get('publication_closure_claim') is not False):
        raise ValueError('Snapshot book authority is not exact historical discovery evidence.')
    pdfs = document.get('pdfs', [])
    if (not isinstance(pdfs, list) or len(pdfs) != 7 or
            {p.get('reader') for p in pdfs} != set(BOOKS)):
        raise ValueError('Snapshot book inventory is incomplete or ambiguous.')
    index = q.get('snapshot_pdf_index')
    if type(index) is not int or not 0 <= index < len(pdfs):
        raise ValueError('Invalid exact snapshot book index.')
    captured = pdfs[index]
    book = captured['reader']
    expected_path = (Path(snapshot_path).parent / 'pdfs' / (book + '.pdf')).as_posix()
    original = 'work/build/' + book + '.pdf'
    if (captured.get('path') != original or captured.get('preserved_path') != expected_path or
            q.get('snapshot_pdf_record') != captured or q.get('original_path') != original or
            safe_name(name) != expected_path or row.get('path') != name or row.get('reader') != book or
            row.get('source_pdf_sha256') != captured.get('sha256') or
            row.get('source_pdf_bytes') != captured.get('bytes') or
            type(captured.get('bytes')) is not int or captured['bytes'] <= 0 or
            not re.fullmatch('[0-9a-f]{64}', str(captured.get('sha256'))) or
            type(captured.get('pages')) is not int or captured['pages'] <= 0):
        raise ValueError('Snapshot book path, identity or exact source association differs.')
    if (row.get('final_archive') != 'LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip' or
            row.get('final_path') != book + '.pdf'):
        raise ValueError('Snapshot book disposition names a different final publication.')
    preserved = root / name
    if not preserved.resolve().is_relative_to(root.resolve()):
        raise ValueError('Preserved snapshot book escapes its root.')
    data = preserved.read_bytes()
    if (len(data) != captured['bytes'] or digest(data) != captured['sha256'] or
            not data.startswith(b'%PDF-')):
        raise ValueError('Preserved snapshot book bytes differ from their exact authority.')

